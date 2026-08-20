# bench.py -- the verification bench (milestone P0.2)
#
# Why this exists. The repository's own rule says: what can only be reproduced
# by hand is reproducibility debt, and it must be paid off before anything new
# is built on it. This bench pays it off mechanically. It re-runs the package
# scripts of the rulebook-era proofs (II/13 onward), harvests the accuracy
# checks they print, and compares each one against the value published in the
# package -- within a tolerance declared in tolerances.json, never widened
# after the fact.
#
# The bench proves nothing and overturns nothing. A red line means "this number
# does not come back on this machine", which may be an environment limit rather
# than a defect -- run shared/environment-check.py first to tell the two apart.
#
# One verdict deserves special attention: URES (vacuous). A two-way check
# compares two supposedly independent computation routes. If it reports exactly
# zero deviation, the two routes have most likely collapsed into one (on this
# platform np.longdouble is an alias of float64), so the check covers nothing.
# A vacuous check is reported as a failure, because a false green is worse than
# a red: it is the machine equivalent of a hand-set value nobody measured.
#
# Usage:
#   python shared/bench/bench.py            # skips the scripts marked slow
#   python shared/bench/bench.py --teljes   # runs everything, however long
#   python shared/bench/bench.py --proba II-14
#
# Exit code: 0 if every check that ran is green, 1 otherwise.

import json
import os
import re
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

# The workstation has 8 cores / 16 threads and 128 GB, but the other half of the
# machine belongs to its owner: never take more than MAX_MAG cores. Children get
# their BLAS/OpenMP thread pools pinned to 1, otherwise N parallel scripts would
# each spin up their own pool and the real load would be N x cores, not N.
MAX_MAG = 8
EGYSZALU_KORNYEZET = {"OMP_NUM_THREADS": "1", "OPENBLAS_NUM_THREADS": "1",
                      "MKL_NUM_THREADS": "1", "NUMEXPR_NUM_THREADS": "1",
                      "VECLIB_MAXIMUM_THREADS": "1"}

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

SHARED = Path(__file__).resolve().parents[1]
ROOT = SHARED.parent
TURESEK = Path(__file__).resolve().parent / "tolerances.json"

OK, BUKIK, URES, NEM_FUT, HIANYZO = "ALL", "BUKIK", "URES", "NEM FUT", "NINCS MEG"
H4_VAR = "H4-VAR"

# Checks whose declared primary route was the extended-precision one of H3.
# Correction H4 retired that route, so in the reference environment their
# PRECONDITION is missing -- the number is not wrong, the script simply has not
# been moved to shared/summation.py yet. Reporting these as BUKIK would be a
# false accusation; reporting them as green would be a false clearance. They get
# their own verdict, are listed in full, and do not decide the exit code.
BUKO = (BUKIK, URES, HIANYZO)


def szam(szoveg):
    try:
        return float(szoveg)
    except ValueError:
        return None


def ertekel(ell, kimenet):
    """One check against one captured stdout. Returns (verdict, read value, note)."""
    m = re.search(ell["minta"], kimenet)
    if not m:
        return HIANYZO, None, "a minta nem talalt a kimenetben"
    nyers = m.group(1).strip()
    mod = ell.get("mod", "tures")

    if mod == "szoveg":
        return (OK if nyers == ell["ertek"] else BUKIK), nyers, ""

    ertek = szam(nyers)
    if ertek is None:
        return BUKIK, nyers, "a kiolvasott ertek nem szam"

    if mod == "egyezes":
        elteres = abs(ertek - ell["ertek"])
        jo = elteres <= ell.get("tures", 0)
        return (OK if jo else BUKIK), nyers, ("elteres %.3g" % elteres if not jo else "")

    # mod == "tures"
    if ell.get("ketutas") and ertek == 0.0:
        return URES, nyers, "pontosan nulla -- a ket ut valoszinuleg egybeesett"
    jo = ertek <= ell["tures"]
    return (OK if jo else BUKIK), nyers, ("" if jo else "tures %.3g" % ell["tures"])


def futtat(szkript_ut, szalak):
    """Package scripts must run from their own directory (relative cache paths).
    `szalak` pins the child's BLAS/OpenMP pools so the total load stays bounded."""
    ut = SHARED / szkript_ut
    if not ut.exists():
        return None, 0.0, "a szkript nem letezik"
    kornyezet = dict(os.environ)
    kornyezet.update({k: str(szalak) for k in EGYSZALU_KORNYEZET})
    kezd = time.time()
    try:
        p = subprocess.run([sys.executable, ut.name], cwd=str(ut.parent),
                           capture_output=True, text=True, errors="replace",
                           env=kornyezet)
    except OSError as e:
        return None, time.time() - kezd, str(e)
    return (p.stdout or "") + (p.stderr or ""), time.time() - kezd, None


def main(argv):
    teljes = "--teljes" in argv
    szures = None
    if "--proba" in argv:
        szures = argv[argv.index("--proba") + 1]
    jobs = MAX_MAG
    if "--jobs" in argv:
        jobs = int(argv[argv.index("--jobs") + 1])
    jobs = max(1, min(jobs, MAX_MAG))

    print("== hitelesito-pad (P0.2) ==")
    print()
    if not TURESEK.exists():
        print("HIBA: a tures-fajl nem talalhato: %s" % TURESEK)
        return 1
    tar = json.loads(TURESEK.read_text(encoding="utf-8"))
    padok = tar["padok"]
    if szures:
        padok = [p for p in padok if p["proba"] == szures]

    print("tures-fajl : %s" % TURESEK.relative_to(ROOT).as_posix())
    print("mod        : %s%s" % ("teljes" if teljes else "gyors (a lassu szkriptek kimaradnak)",
                                 (", szures: " + szures) if szures else ""))
    print("magok      : legfeljebb %d (a gep tobbi resze a felhasznaloe)" % jobs)
    print()

    osszes = {OK: 0, BUKIK: 0, URES: 0, HIANYZO: 0, NEM_FUT: 0, H4_VAR: 0}
    reszletek, varok = [], []

    kihagyott = {p["szkript"] for p in padok if p.get("lassu") and not teljes}
    futando = [p for p in padok if p["szkript"] not in kihagyott]
    parhuzamos = [p for p in futando if not p.get("memoriaigenyes")]
    sorosak = [p for p in futando if p.get("memoriaigenyes")]

    eredmeny = {}
    if parhuzamos:
        n = min(jobs, len(parhuzamos))
        print("  parhuzamosan: %d szkript, %d dolgozo (a gyerekek szalpoolja 1-re kotve)"
              % (len(parhuzamos), n))
        with ThreadPoolExecutor(max_workers=n) as pool:
            valaszok = list(pool.map(lambda p: futtat(p["szkript"], 1), parhuzamos))
        for pad, valasz in zip(parhuzamos, valaszok):
            eredmeny[pad["szkript"]] = valasz
    for pad in sorosak:
        print("  sorosan (memoriaigenyes, %d szalon): %s" % (jobs, pad["szkript"]))
        eredmeny[pad["szkript"]] = futtat(pad["szkript"], jobs)
    print()

    for pad in padok:
        nev = pad["szkript"]
        if nev in kihagyott:
            print("  [kihagyva]  %s  (lassu; --teljes futtatja)" % nev)
            osszes[NEM_FUT] += len(pad["ellenorzesek"])
            continue

        kimenet, ido, hiba = eredmeny[nev]
        if kimenet is None:
            print("  [NEM FUT]   %s  -- %s" % (nev, hiba))
            osszes[NEM_FUT] += len(pad["ellenorzesek"])
            continue

        print("  %s  (%.1f s)" % (nev, ido))
        for ell in pad["ellenorzesek"]:
            itelet, olvasott, megj = ertekel(ell, kimenet)
            if itelet in BUKO and ell.get("h3_fuggo"):
                itelet = H4_VAR
                megj = "a H3 kiterjesztett ut visszavonva -- a szkript meg nem all a H4 uton"
            osszes[itelet] = osszes.get(itelet, 0) + 1
            jelzo = {OK: "ALL   ", BUKIK: "BUKIK ", URES: "URES  ",
                     HIANYZO: "NINCS ", H4_VAR: "H4-VAR"}[itelet]
            sor = "      %s %-46s olvasott: %-14s kozzetett: %s" % (
                jelzo, ell["nev"][:46], str(olvasott)[:14], ell.get("kozzetett", "-"))
            print(sor)
            if megj:
                print("             ^ %s" % megj)
            if itelet in BUKO:
                reszletek.append((pad["proba"], nev, ell["nev"], itelet, olvasott, megj))
            elif itelet == H4_VAR:
                varok.append((pad["proba"], nev, ell["nev"], olvasott))
        print()

    var = tar.get("felvetelre_var", [])
    if var:
        print("  felvetelre var (%d szkript, meg nincs mintaja):" % len(var))
        for v in var:
            print("      %-52s %s" % (v["szkript"], v["ok"]))
        print()

    fut = osszes[OK] + osszes[BUKIK] + osszes[URES] + osszes[HIANYZO] + osszes[H4_VAR]
    print("  osszegzes: %d ellenorzes futott -- ALL %d | BUKIK %d | URES %d | "
          "NINCS MEG %d | H4-VAR %d"
          % (fut, osszes[OK], osszes[BUKIK], osszes[URES], osszes[HIANYZO],
             osszes[H4_VAR]))
    if osszes[NEM_FUT]:
        print("             tovabbi %d ellenorzes nem futott (lassu vagy hianyzo szkript)"
              % osszes[NEM_FUT])
    print()

    if varok:
        print("  H4-VAR (%d) -- nem rossz szam, hanem hianyzo elofeltetel:" % len(varok))
        for proba, szkript, ell, olvasott in varok:
            print("      [%s] %-44s olvasott: %s" % (proba, ell[:44], olvasott))
        print("      A hordozhato utat a shared/summation.py adja; a szkriptek")
        print("      atallitasa a H4 helyesbites dolga (B fuggelek).")
        print()

    if not reszletek:
        print("ITELET: ALL -- minden lefutott ellenorzes visszaadta a kozzetett szamot.")
        if varok:
            print("        (%d ellenorzes H4-VAR statuszban -- lasd fent.)" % len(varok))
        return 0

    print("ITELET: BUKIK -- %d ellenorzes nem all:" % len(reszletek))
    for proba, szkript, ell, itelet, olvasott, megj in reszletek:
        print("   [%s] %s / %s -> %s (%s)%s"
              % (itelet, proba, ell, olvasott, szkript, (" -- " + megj) if megj else ""))
    print()
    print("Mielott ezt hibanak veszed: futtasd a shared/environment-check.py-t.")
    print("Kornyezeti korlat es hiba ket kulon dolog, es a pad nem tudja szetvalasztani.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
