# PKG-15-11-hole-ladder.py -- the hole ladder: the dense end, exactly
#
# PKG-15-10 left one weak link. Its dense-end theorem (TB) bounded the loser's
# top tail by m times its peak, which is generous, so the stretch it certified
# was a conservative lower bound on the real one. This package removes the
# inequality altogether.
#
# The observation. Write every beat as its distance from the ceiling:
#
#     deficit  =  4k - beat,        sorted ascending
#
# The m largest beats are the m smallest deficits, so for EVERY entrant Y,
# without any assumption of symmetry:
#
#     price_Y(n-m)  =  T - 4km + D_Y(m)
#
# where D_Y(m) is the price of filling the DEFICIT ladder from below to m. That
# is an identity, not an estimate.
#
# What it means. Leaving m places empty is the same problem as filling m holes
# from below -- on a second ladder that every entrant carries alongside its own.
# The dense end is not a different kind of race; it is the ordinary race, run on
# the hole ladder. And an entrant is mirror-marked exactly when its hole ladder
# IS its beat ladder, which is the hole-mirror theorem restated as an identity
# between two ladders rather than a relation between two fillings.
#
# Consequences checked here:
#   E1  the identity, on every entrant, at every filling
#   E2  mirror-marked  <=>  hole ladder == beat ladder
#   E3  the dense-end winner is exactly the entrant with the cheapest hole
#       ladder -- no inequality, no certified stretch
#   E4  how conservative PKG-15-10's sufficient condition really was

import sys
import time
from pathlib import Path

import numpy as np

SHARED = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SHARED))

import summation                                             # noqa: E402

HELYEK = 20736
FOKOK = 4
CSUCS = 4.0 * FOKOK                      # 4k = 16, the ceiling of any beat
NYOM = 2.0 * FOKOK * HELYEK              # T = 2kn = 165888
TURES = summation.TURES

MEZONY = [
    ("J1 line",               (HELYEK,),        [(1,), (2,), (3,), (4,)]),
    ("J2 plane (king)",       (144, 144),       [(1, 0), (0, 1), (1, 1), (1, -1)]),
    ("J3 space (BCC)",        (24, 24, 36),     [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, -1, -1)]),
    ("J3' space (face diag)", (24, 24, 36),     [(1, 0, 0), (0, 1, 0), (0, 0, 1), (0, 1, -1)]),
    ("J4 hypercube",          (12, 12, 12, 12), [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)]),
]


def letra(oldalak, lepesek):
    racsok = np.meshgrid(*[np.arange(n) for n in oldalak], indexing="ij")
    lam = np.zeros(oldalak, dtype=np.float64)
    for s in lepesek:
        faz = np.zeros(oldalak, dtype=np.float64)
        for i, n in enumerate(oldalak):
            faz += 2.0 * np.pi * racsok[i] * s[i] / n
        lam += 2.0 - 2.0 * np.cos(faz)
    return np.sort(lam.ravel())


def main():
    kezd = time.time()
    print("== PKG-15-11 -- the hole ladder ==")
    print("   n = %d, k = %d, T = %.0f, ceiling 4k = %.0f"
          % (HELYEK, FOKOK, NYOM, CSUCS))
    print()

    nevek, utemek, arak, hianyok, D = [], [], [], [], []
    for nev, oldalak, lepesek in MEZONY:
        lam = letra(oldalak, lepesek)
        nevek.append(nev)
        utemek.append(lam)
        arak.append(summation.pontos_cumsum(lam))
        h = np.sort(CSUCS - lam)                             # the hole ladder
        hianyok.append(h)
        D.append(summation.pontos_cumsum(h))

    m = np.arange(1, HELYEK)

    # --- E1: the identity ---------------------------------------------------
    print("== E1  price_Y(n-m) = T - 4km + D_Y(m), for every entrant ==")
    legrosszabb = 0.0
    for nev, ar, d in zip(nevek, arak, D):
        bal = ar[HELYEK - m - 1]
        jobb = NYOM - CSUCS * m + d[m - 1]
        elt = float(np.max(np.abs(bal - jobb)))
        legrosszabb = max(legrosszabb, elt)
        print("   %-22s largest deviation over all m: %.3e" % (nev, elt))
    print("   -- %s (tolerance %.0e)"
          % ("HOLDS" if legrosszabb <= 1e-7 else "FAILS", 1e-7))
    print()

    # --- E2: mirror mark as an identity between ladders ---------------------
    print("== E2  mirror-marked  <=>  hole ladder == beat ladder ==")
    tukros = []
    for nev, lam, h in zip(nevek, utemek, hianyok):
        azonos = float(np.max(np.abs(lam - h))) <= TURES
        tukros.append(azonos)
        print("   %-22s peak %8.5f | hole ladder == beat ladder: %s"
              % (nev, lam[-1], "yes" if azonos else "no"))
    print()

    # --- E3: the dense-end winner, exactly ----------------------------------
    print("== E3  the dense-end winner is the cheapest hole ladder ==")
    ar_t = np.array(arak)
    D_t = np.array(D)
    elteres = 0
    for mm in (1, 2, 5, 10, 50, 100, 500, 1000, 2000, 4000, 8000, 10368):
        N = HELYEK - mm
        a = int(np.argmin(ar_t[:, N - 1]))
        b = int(np.argmin(D_t[:, mm - 1]))
        if a != b:
            elteres += 1
        print("   m=%6d (N=%6d): race winner %-22s hole-ladder winner %-22s %s"
              % (mm, N, nevek[a], nevek[b], "" if a == b else "<-- DIFFERS"))
    print("   -- %s" % ("HOLDS on every sampled filling" if not elteres else "FAILS"))
    print()

    # --- E4: how conservative was PKG-15-10's sufficient condition ----------
    print("== E4  PKG-15-10's certified stretch against the exact boundary ==")
    print("   %-22s %-22s %12s %12s %10s"
          % ("mirror X", "non-mirror Z", "certified m", "exact m", "left on table"))
    for xi, xnev in enumerate(nevek):
        if not tukros[xi]:
            continue
        for zi, znev in enumerate(nevek):
            if tukros[zi]:
                continue
            d_z = CSUCS - float(utemek[zi][-1])
            eleg = arak[xi][m - 1] < d_z * m                 # PKG-15-10 (K-PKG1510-5)
            tanusitott = int(np.argmax(~eleg)) if not eleg.all() else HELYEK - 1
            pontos_maszk = D_t[xi, m - 1] < D_t[zi, m - 1]   # the exact criterion
            pontos = int(np.argmax(~pontos_maszk)) if not pontos_maszk.all() else HELYEK - 1
            print("   %-22s %-22s %12d %12d %10d"
                  % (xnev, znev, tanusitott, pontos, pontos - tanusitott))
    print()
    print("   The exact column is the real boundary; the certified one was a")
    print("   lower bound. The gap is what the inequality gave away.")
    print()
    print("   (%.1f s)" % (time.time() - kezd))
    return 0 if legrosszabb <= 1e-7 and not elteres else 1


if __name__ == "__main__":
    raise SystemExit(main())
