# runner.py -- the parallel task runner for package computations
#
# What this is for. The gate rule of the rulebook orders PACKAGES: a package may
# only build on an approved predecessor, so rulebook -> ladders -> race -> readout
# is strictly sequential and must stay that way. Inside a single stage, however,
# the work is a field of independent items -- 503 entrants, 495 family members,
# six pairwise lemmas -- and nothing there depends on the order. That is where
# this runner belongs, and only there.
#
# Three properties this has to guarantee, or parallelism would cost more than it
# buys:
#
#   1. Order independence. The result must not depend on which worker finished
#      first. Results are keyed by task id and returned in the order they were
#      declared, never in completion order. On top of that, `rendproba` re-runs a
#      sample of the tasks serially in this process and compares them bit for bit
#      against the parallel results. That check is to scheduling what the two-way
#      rule is to arithmetic: without it, "it ran faster" is not evidence.
#
#   2. A bounded machine. Never more than MAX_MAG cores -- the rest of the
#      workstation belongs to its owner -- and the children's BLAS/OpenMP pools
#      are pinned to one thread each, otherwise N workers would each open their
#      own pool and the real load would be N x cores. Tasks declared memory-heavy
#      run in a lane of their own.
#
#   3. Failure isolation and resume. One task raising must not lose the other
#      502. Failures come back as markers, and every completed task is cached, so
#      a re-run picks up where the last one stopped. Long fields are worth little
#      if a crash at 90% means starting over.
#
# Windows note: worker functions are named as "module.path:function" strings, not
# passed as objects. Process start-up here is spawn, so a worker must be
# importable in a fresh interpreter -- lambdas and closures cannot cross that
# boundary. Anything that calls futtat() needs an `if __name__ == "__main__":`
# guard for the same reason.
#
# The cache lives in the system temp directory, never in the repository: it is
# intermediate work, not a deliverable.

import hashlib
import importlib
import importlib.util
import os
import pickle
import sys
import tempfile
import time
import traceback
from collections import namedtuple
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

MAX_MAG = 8                     # never take more than this; see the memory note above
EGYSZALU = ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
            "NUMEXPR_NUM_THREADS", "VECLIB_MAXIMUM_THREADS")

ALAP_GYORSITOTAR = Path(tempfile.gettempdir()) / "oop-parallel"


class Feladat(namedtuple("Feladat", "azonosito fuggveny argumentumok memoriaigenyes")):
    """One independent item of a stage.

    azonosito       -- unique, stable, and meaningful: it keys the cache and the
                       report, so "(1, 3, 5, 7)" beats "task_42".
    fuggveny        -- "modul.utvonal:fuggveny_nev"; must be importable in a
                       fresh interpreter.
    argumentumok    -- dict of keyword arguments; must be picklable.
    memoriaigenyes  -- run this one alone, outside the pool.
    """

    def __new__(cls, azonosito, fuggveny, argumentumok=None, memoriaigenyes=False):
        return super().__new__(cls, str(azonosito), fuggveny,
                               dict(argumentumok or {}), bool(memoriaigenyes))


class Hiba(namedtuple("Hiba", "azonosito kivetel nyomkoveto")):
    """A task that raised. Kept as a value so the field still completes."""


Eredmeny = namedtuple("Eredmeny",
                      "ertekek hibak ido gyorsitotarbol futott magok rendproba")


def _modul_ujjlenyomat(fuggveny_nev):
    """The worker module's source, fingerprinted.

    Without this the cache keys on (function name, arguments) alone -- so editing
    the worker and re-running silently returns the OLD numbers. That is the worst
    kind of cache bug, because everything looks like it ran. Hashing the source
    file means a changed worker is simply a cache miss."""
    modul_nev = fuggveny_nev.partition(":")[0]
    try:
        spec = importlib.util.find_spec(modul_nev)
        if spec and spec.origin:
            adat = Path(spec.origin).read_bytes()
            return hashlib.sha256(adat).hexdigest()[:12]
    except Exception:
        pass
    return "ismeretlen"


def _kulcs(feladat):
    nyers = repr((feladat.fuggveny, _modul_ujjlenyomat(feladat.fuggveny),
                  sorted(feladat.argumentumok.items()))).encode("utf-8")
    return hashlib.sha256(nyers).hexdigest()[:24]


def _betolt(fuggveny_nev):
    modul_nev, _, nev = fuggveny_nev.partition(":")
    if not nev:
        raise ValueError("a fuggveny alakja 'modul:fuggveny_nev' kell legyen: %r"
                         % fuggveny_nev)
    return getattr(importlib.import_module(modul_nev), nev)


def _vegrehajt(csomag):
    """Runs in the worker. Module level so spawn can find it."""
    azonosito, fuggveny_nev, argumentumok, gyoker = csomag
    if gyoker and gyoker not in sys.path:
        sys.path.insert(0, gyoker)
    try:
        return azonosito, _betolt(fuggveny_nev)(**argumentumok), None
    except Exception as e:                                   # isolate, never abort
        return azonosito, None, (repr(e), traceback.format_exc())


def _vegrehajt_koteg(csomagok):
    """Several tasks per dispatch.

    Handing over one short task at a time is a bad trade: on spawn platforms the
    pickling and hand-off can cost as much as the arithmetic, and the field then
    runs barely faster than serially. Batching amortises that. It changes nothing
    about the results -- the tasks are independent either way -- only how many
    times the boundary is crossed."""
    return [_vegrehajt(cs) for cs in csomagok]


def _kotegek(elemek, meret):
    for i in range(0, len(elemek), meret):
        yield elemek[i:i + meret]


# One store, not one file per task. Per-task files looked tidy but on Windows
# 495 small reads cost 13 s -- eight times longer than recomputing the field --
# so the cache was a pessimisation exactly where it was meant to help. A single
# pickle is read once, and checkpointed every MENTES_KOZ completions so a crash
# still leaves the finished work behind.
MENTES_KOZ = 50
TAR_NEV = "tar.pickle"


def _tar_betolt(mappa):
    ut = Path(mappa) / TAR_NEV
    if not ut.exists():
        return {}
    try:
        with ut.open("rb") as f:
            tar = pickle.load(f)
        return tar if isinstance(tar, dict) else {}
    except Exception:
        return {}                                            # a damaged store just re-runs


def _tar_ment(mappa, tar):
    try:
        mappa = Path(mappa)
        mappa.mkdir(parents=True, exist_ok=True)
        ideiglenes = mappa / (TAR_NEV + ".uj")
        with ideiglenes.open("wb") as f:
            pickle.dump(tar, f, protocol=pickle.HIGHEST_PROTOCOL)
        ideiglenes.replace(mappa / TAR_NEV)                  # atomic: never a half file
    except Exception:
        pass                                                 # a cache miss is not a failure


def _azonos(a, b):
    """Bit-for-bit sameness, the only comparison worth making for an
    order-independence check. A tolerance here would hide exactly what we look for."""
    try:
        import numpy as np
        if isinstance(a, np.ndarray) or isinstance(b, np.ndarray):
            a, b = np.asarray(a), np.asarray(b)
            return a.shape == b.shape and a.dtype == b.dtype and np.array_equal(a, b)
    except ImportError:
        pass
    if isinstance(a, (list, tuple)) and isinstance(b, (list, tuple)):
        return len(a) == len(b) and all(_azonos(x, y) for x, y in zip(a, b))
    if isinstance(a, dict) and isinstance(b, dict):
        return a.keys() == b.keys() and all(_azonos(a[k], b[k]) for k in a)
    return type(a) is type(b) and a == b


def futtat(feladatok, magok=MAX_MAG, gyorsitotar=ALAP_GYORSITOTAR,
           rendproba=0, gyoker=None, halkan=False, cimke="feladatok",
           koteg=None):
    """Run an independent field of tasks across processes.

    rendproba -- how many tasks to re-run serially afterwards and compare bit for
                 bit. 0 skips the check; anything above 0 is cheap insurance and
                 the only thing that makes the speed-up trustworthy.
    """
    feladatok = list(feladatok)
    azonositok = [f.azonosito for f in feladatok]
    if len(set(azonositok)) != len(azonositok):
        raise ValueError("ismetlodo feladat-azonosito: a gyorsitotar es a jelentes "
                         "kulcsa serulne")

    magok = max(1, min(int(magok), MAX_MAG))
    gyorsitotar = Path(gyorsitotar) if gyorsitotar else None
    gyoker = gyoker or str(Path(__file__).resolve().parents[1])

    # Set before the pool exists: children inherit it, and they import numpy fresh.
    for kulcs in EGYSZALU:
        os.environ[kulcs] = "1"

    kezd = time.time()
    ertekek, hibak, tarbol = {}, {}, 0
    varo = []

    tar = _tar_betolt(gyorsitotar) if gyorsitotar else {}
    for f in feladatok:
        kulcs = _kulcs(f)
        if gyorsitotar and kulcs in tar:
            ertekek[f.azonosito] = tar[kulcs]
            tarbol += 1
            continue
        varo.append(f)

    parhuzamos = [f for f in varo if not f.memoriaigenyes]
    sorosak = [f for f in varo if f.memoriaigenyes]

    if not halkan:
        print("  %s: %d db | gyorsitotarbol %d | futtatando %d (%d parhuzamos, "
              "%d sorosan) | magok %d"
              % (cimke, len(feladatok), tarbol, len(varo), len(parhuzamos),
                 len(sorosak), magok))

    kesz = 0

    def _feldolgoz(azonosito, ertek, hiba, feladat):
        nonlocal kesz
        kesz += 1
        if hiba is not None:
            hibak[azonosito] = Hiba(azonosito, hiba[0], hiba[1])
        else:
            ertekek[azonosito] = ertek
            if gyorsitotar:
                tar[_kulcs(feladat)] = ertek
                if kesz % MENTES_KOZ == 0:
                    _tar_ment(gyorsitotar, tar)
        if not halkan and (kesz % max(1, len(varo) // 10) == 0 or kesz == len(varo)):
            print("     %d/%d (%.1f s)" % (kesz, len(varo), time.time() - kezd))

    if parhuzamos:
        szerint = {f.azonosito: f for f in parhuzamos}
        if koteg is None:
            # Enough batches to keep every worker fed even if the tasks differ
            # in cost, but few enough that the hand-off stops dominating.
            koteg = max(1, len(parhuzamos) // (magok * 4))
        koteg = max(1, int(koteg))
        csomagok = [(f.azonosito, f.fuggveny, f.argumentumok, gyoker)
                    for f in parhuzamos]
        if not halkan and koteg > 1:
            print("     kotegmeret %d (%d koteg)"
                  % (koteg, (len(csomagok) + koteg - 1) // koteg))
        with ProcessPoolExecutor(max_workers=min(magok, len(parhuzamos))) as pool:
            jovok = [pool.submit(_vegrehajt_koteg, cs)
                     for cs in _kotegek(csomagok, koteg)]
            for jovo in as_completed(jovok):
                for azonosito, ertek, hiba in jovo.result():
                    _feldolgoz(azonosito, ertek, hiba, szerint[azonosito])

    for f in sorosak:
        azonosito, ertek, hiba = _vegrehajt(
            (f.azonosito, f.fuggveny, f.argumentumok, gyoker))
        _feldolgoz(azonosito, ertek, hiba, f)

    if gyorsitotar and varo:
        _tar_ment(gyorsitotar, tar)
    ido = time.time() - kezd

    # --- order independence -------------------------------------------------
    # Re-run a spread-out sample here, in this process, one after another, and
    # demand bitwise sameness. Evenly spaced rather than random so the check is
    # itself reproducible.
    rendproba_eredmeny = None
    if rendproba > 0 and feladatok:
        minta_db = min(int(rendproba), len(feladatok))
        lepes = max(1, len(feladatok) // minta_db)
        minta = [feladatok[i] for i in range(0, len(feladatok), lepes)][:minta_db]
        # The re-run has to happen in a WORKER, not here. The children run with
        # their BLAS pools pinned to one thread; this parent imported numpy
        # before those variables were set, so it still threads. Re-running in
        # the parent therefore compares one-threaded arithmetic against
        # many-threaded arithmetic, and the last bits differ for reasons that
        # have nothing to do with scheduling. Running the sample through a pool
        # of one keeps the comparison bitwise -- which is the point -- while
        # testing what it is meant to test: does the ORDER change the result.
        elteres = []
        with ProcessPoolExecutor(max_workers=1) as ellenorzo:
            valaszok = [ellenorzo.submit(
                _vegrehajt, (f.azonosito, f.fuggveny, f.argumentumok, gyoker))
                for f in minta]
            eredmenyek = [v.result() for v in valaszok]
        for f, (_, ertek, hiba) in zip(minta, eredmenyek):
            if hiba is not None or f.azonosito not in ertekek:
                elteres.append(f.azonosito)
            elif not _azonos(ertek, ertekek[f.azonosito]):
                elteres.append(f.azonosito)
        rendproba_eredmeny = (len(minta), elteres)
        if not halkan:
            if elteres:
                print("     RENDPROBA BUKIK: %d/%d feladat mas eredmenyt adott "
                      "sorosan: %s" % (len(elteres), len(minta), ", ".join(elteres[:5])))
            else:
                print("     rendproba: %d/%d feladat bitre azonos sorosan is -- ALL"
                      % (len(minta), len(minta)))

    # Deterministic order: as declared, never as completed.
    rendezett = [ertekek.get(a) for a in azonositok]
    return Eredmeny(rendezett, hibak, ido, tarbol, len(varo), magok,
                    rendproba_eredmeny)


def jelentes(eredmeny, cimke="futas"):
    """One-screen summary; returns 0 if the run is trustworthy, 1 if not."""
    print()
    print("  == %s ==" % cimke)
    print("     ido            : %.1f s (%d mag)" % (eredmeny.ido, eredmeny.magok))
    print("     gyorsitotarbol : %d" % eredmeny.gyorsitotarbol)
    print("     futott         : %d" % eredmeny.futott)
    print("     hiba           : %d" % len(eredmeny.hibak))
    if eredmeny.rendproba:
        db, elteres = eredmeny.rendproba
        print("     rendproba      : %d mintabol %d elteres -- %s"
              % (db, len(elteres), "BUKIK" if elteres else "ALL"))
    else:
        print("     rendproba      : nem futott -- a gyorsulas igy nem bizonyitott")
    for azonosito, h in list(eredmeny.hibak.items())[:5]:
        print("     [HIBA] %s: %s" % (azonosito, h.kivetel))
    if len(eredmeny.hibak) > 5:
        print("     ... es meg %d" % (len(eredmeny.hibak) - 5))

    rossz = bool(eredmeny.hibak) or bool(eredmeny.rendproba and eredmeny.rendproba[1])
    print()
    print("  ITELET: %s" % ("BUKIK" if rossz else "ALL"))
    return 1 if rossz else 0
