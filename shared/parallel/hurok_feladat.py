# hurok_feladat.py -- one run of the II/17 loop, as a parallel task
#
# The loop of PKG-17-1, section 4, unchanged:
#
#   content w  ->  finished state  ->  pairwise closeness I  ->  w = f(I), normalised
#
# All the machinery comes from PKG-17-2-verify.py, whose gate is clean: the cost
# operator, the ground space in magnetisation blocks, the exact projector for the
# degenerate case, and the closeness measure of II/11. Nothing is reimplemented
# here -- a second implementation would be a second chance to differ from the
# chapter that has already run.
#
# Two costs are paid for speed, and neither changes a number:
#   * the 66 pair operators are built once and kept as (diagonal, off-diagonal)
#     sparse pairs instead of 66 dense 4096x4096 matrices;
#   * the eigenproblem still runs block by block, exactly as ground_space does.
#
# Everything the rulebook left as an interpretation is marked ERTELMEZES below
# and reported by the driver, so it is visible rather than buried.

import importlib.util
from itertools import combinations
from pathlib import Path

import numpy as np

SHARED = Path(__file__).resolve().parents[1]
_ut = SHARED / "II-17-contract-origin" / "PKG-17-2-verify.py"
_spec = importlib.util.spec_from_file_location("pkg172verify", _ut)
V = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(V)

N = 12
PAROK = list(combinations(range(N), 2))          # 66
DIM = 1 << N
MAG = 1166                                       # the seed fixed by PKG-17-1
KOROK = 200
MEGALLAS = 1e-9                                  # the loop's stopping tolerance
ZAJ = 1e-3                                       # I1's noise magnitude
EMELES = 1.1                                     # the raise factor of I2-I4


def _sparse_parok():
    """The 66 pair operators as (diagonal, row, col, value). The operator of
    PKG-17-2-verify is diagonal plus one swap per state, so this is exact."""
    ki = []
    for i, j in PAROK:
        bi, bj = 1 << (N - 1 - i), 1 << (N - 1 - j)
        s = np.arange(DIM)
        vi, vj = (s & bi) != 0, (s & bj) != 0
        azonos = vi == vj
        diag = np.where(azonos, 1.0, 0.5)
        el = np.where(~azonos)[0]
        ki.append((diag, el, el ^ bi ^ bj))
    return ki


SPARSE = _sparse_parok()
POPC = np.array([bin(s).count("1") for s in range(DIM)])
BLOKKOK = [np.where(POPC == m)[0] for m in range(N + 1)]


def _hamiltonian(w):
    H = np.zeros((DIM, DIM))
    ossz_diag = np.zeros(DIM)
    for wij, (diag, sor, oszlop) in zip(w, SPARSE):
        if wij == 0.0:
            continue
        ossz_diag += wij * diag
        np.add.at(H, (sor, oszlop), 0.5 * wij)
    H[np.arange(DIM), np.arange(DIM)] += ossz_diag
    return H


def _alapallapot(w, tol=1e-9):
    """Block by block, exactly as ground_space -- returns the zero-cost subspace."""
    H = _hamiltonian(w)
    best, vecs = np.inf, []
    for idx in BLOKKOK:
        if idx.size == 0:
            continue
        ertek, vekt = np.linalg.eigh(H[np.ix_(idx, idx)])
        if ertek[0] < best - tol:
            best, vecs = ertek[0], []
        if ertek[0] < best + tol:
            for k in np.where(ertek < best + tol)[0]:
                teljes = np.zeros(DIM)
                teljes[idx] = vekt[:, k]
                vecs.append(teljes)
    return best, vecs


def _kozelseg(vecs):
    """The closeness of II/11, with its own definition enforced.

    The measure is a mutual information, so it is >= 0 as a matter of
    definition. Numerically it underflows past zero once pairs decouple: over
    twelve rounds the most negative value seen was -1.1e-15, against closeness
    values of order 1. Clamping at zero enforces the definition rather than
    changing it -- and without it the damped family member F3 takes the square
    root of a negative number and the run dies, which is how this surfaced."""
    terkep = V.proximity_map(N, vecs)
    return np.maximum(np.array([terkep[p] for p in PAROK]), 0.0)


def _indulo(nev):
    """The four starters of PKG-17-1, section 4.

    ERTELMEZES, marked because the rulebook fixes the magnitudes but not these:
      * I1's noise is uniform on [-ZAJ, +ZAJ] (a distribution had to be chosen);
      * I2 raises the lexicographically first pair, (0,1);
      * I3 raises the matching (0,1)(2,3)...(10,11);
      * I4 raises the ring edges (i, i+1 mod 12).
    """
    w = np.ones(len(PAROK))
    if nev == "I1":
        rng = np.random.default_rng(MAG)
        w = w + rng.uniform(-ZAJ, ZAJ, size=len(PAROK))
    elif nev == "I2":
        w[PAROK.index((0, 1))] *= EMELES
    elif nev == "I3":
        for i in range(0, N, 2):
            w[PAROK.index((i, i + 1))] *= EMELES
    elif nev == "I4":
        for i in range(N):
            a, b = sorted((i, (i + 1) % N))
            w[PAROK.index((a, b))] *= EMELES
    else:
        raise ValueError("ismeretlen indulo: %s" % nev)
    return w


def _normal(w, mod):
    return V.normalise(w, mod, len(PAROK))


def futas(csalad, normalas, indulo, korok=KOROK):
    """One (family member, normalisation, starter) run. Returns a record, never
    a verdict: the classification is the driver's job, from the rulebook."""
    w = _indulo(indulo)
    kezdo_szoras = float(w.std())
    f = V.FAMILY[csalad]
    elfajulasok, valtasok, elozo_db = [], 0, None
    megallt_kor = None

    for kor in range(1, korok + 1):
        _, vecs = _alapallapot(w)
        db = len(vecs)
        elfajulasok.append(db)
        if elozo_db is not None and db != elozo_db:
            valtasok += 1
        elozo_db = db

        I = _kozelseg(vecs)
        nyers = f(I)
        uj = _normal(nyers, normalas)
        if uj is None:                         # the normalisation is meaningless
            w = np.zeros(len(PAROK))           # -- the network has ceased
            megallt_kor = kor
            break
        if csalad == "F6":                     # the halfway step lives in the loop
            uj = _normal(0.5 * (w + uj), normalas)
            if uj is None:
                w = np.zeros(len(PAROK))
                megallt_kor = kor
                break
        elteres = float(np.max(np.abs(uj - w)))
        w = uj
        if elteres < MEGALLAS:
            megallt_kor = kor
            break

    rendezett = np.sort(w)[::-1]
    ossz = float(w.sum())
    return {
        "csalad": csalad, "normalas": normalas, "indulo": indulo,
        "megallt_kor": megallt_kor,
        "kezdo_szoras": kezdo_szoras,
        "vegso_szoras": float(w.std()),
        "vegso_max": float(w.max()),
        "vegso_osszeg": ossz,
        "top6_arany": float(rendezett[:6].sum() / ossz) if ossz > 1e-14 else 0.0,
        "nem_nulla_parok": int(np.count_nonzero(w > 1e-12)),
        "elfajulas_elso": elfajulasok[0] if elfajulasok else None,
        "elfajulas_utolso": elfajulasok[-1] if elfajulasok else None,
        "elfajulas_valtasok": valtasok,
        "tartalom": w.tolist(),
    }
