# PKG-15-10-dense-end.py -- machine confirmation of the dense-end theorem
#
# The idea in one line. Every entrant at a fixed coordination has the SAME total
# ladder weight -- the trace tie of II/12 -- so filling from below to N is the
# same thing as leaving out the top n-N beats. Near the full end the cheapest
# entrant is therefore not the one with the lowest beats but the one whose
# HIGHEST beats are largest. And the highest beat is bounded by twice the
# coordination, with equality exactly for the mirror-marked entrants.
#
# That turns the measured carrier half of the top law into a derivation:
#
#   L1  trace tie      sum of all beats = 2kn, identical for every entrant
#   L2  complement     price(N) = T - S(n-N),  S(m) = sum of the top m beats
#   L3  peak bound     peak <= 4k, equality iff mirror-marked (carrier theorem)
#   TA  single hole    at N = n-1 the winner is mirror-marked, and all
#                      mirror-marked entrants tie -- exactly what PKG-15-5
#                      measured, now derived
#   L4  mirror form    for mirror-marked X: price_X(n-m) = T - 4km + price_X(m)
#                      -- the hole-mirror theorem, in one line
#   TB  stretch        if price_X(m) < m * delta_Z, then the mirror-marked X is
#                      strictly cheaper than the non-mirror Z at N = n-m, where
#                      delta_Z = 4k - peak_Z is Z's peak deficit
#
# TB is a SUFFICIENT condition, so the stretch it certifies is a lower bound on
# the real one. That is the honest form: a certified stretch, in the manner of
# PKG-15-6, not a claim about the whole range.
#
# This script checks every step against the real II/15 ladders.

import sys
import time
from pathlib import Path

import numpy as np

SHARED = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SHARED))

import summation                                             # noqa: E402

HELYEK = 20736
FOKOK = 4                                # k: the number of +- pairs
CSUCS_KORLAT = 4.0 * FOKOK               # 4k = 16 = twice the coordination
NYOM = 2.0 * FOKOK * HELYEK              # T = 2kn = 165888
TURES = summation.TURES

MEZONY = [
    ("J1 line",             (HELYEK,),          [(1,), (2,), (3,), (4,)]),
    ("J2 plane (king)",     (144, 144),         [(1, 0), (0, 1), (1, 1), (1, -1)]),
    ("J3 space (BCC)",      (24, 24, 36),       [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, -1, -1)]),
    ("J3' space (face diag)", (24, 24, 36),     [(1, 0, 0), (0, 1, 0), (0, 0, 1), (0, 1, -1)]),
    ("J4 hypercube",        (12, 12, 12, 12),   [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)]),
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
    print("== PKG-15-10 -- the dense-end theorem, machine confirmation ==")
    print("   n = %d places, k = %d pairs, coordination %d" % (HELYEK, FOKOK, 2 * FOKOK))
    print("   T = 2kn = %.0f, peak bound 4k = %.0f" % (NYOM, CSUCS_KORLAT))
    print()

    nevek, letrak, arak = [], [], []
    for nev, oldalak, lepesek in MEZONY:
        lam = letra(oldalak, lepesek)
        nevek.append(nev)
        letrak.append(lam)
        arak.append(summation.pontos_cumsum(lam))

    # --- L1: the trace tie --------------------------------------------------
    print("== L1  trace tie: every entrant sums to T ==")
    legrosszabb = max(abs(summation.pontos_osszeg(l) - NYOM) for l in letrak)
    print("   largest deviation from %.0f: %.3e -- %s"
          % (NYOM, legrosszabb, "HOLDS" if legrosszabb <= TURES else "FAILS"))
    print()

    # --- L2: the complement identity ---------------------------------------
    print("== L2  complement: price(N) + S(n-N) = T, at every filling ==")
    l2 = 0.0
    for lam, ar in zip(letrak, arak):
        forditott = summation.pontos_cumsum(lam[::-1])       # top-m sums
        # price(N) + S(n-N) for N = 1..n-1
        osszeg = ar[:-1] + forditott[len(forditott) - 2::-1]
        l2 = max(l2, float(np.max(np.abs(osszeg - NYOM))))
    print("   largest deviation: %.3e -- %s" % (l2, "HOLDS" if l2 <= TURES else "FAILS"))
    print()

    # --- L3: peak bound and the mirror mark --------------------------------
    print("== L3  peak <= 4k, equality iff mirror-marked ==")
    hiany = {}
    for nev, lam in zip(nevek, letrak):
        csucs = float(lam[-1])
        tukros = float(np.max(np.abs(np.sort(lam) - np.sort(CSUCS_KORLAT - lam)))) <= TURES
        hiany[nev] = CSUCS_KORLAT - csucs
        egyezik = (abs(csucs - CSUCS_KORLAT) <= TURES) == tukros
        print("   %-22s peak %8.5f | deficit %7.5f | mirror: %-3s | L3 %s"
              % (nev, csucs, hiany[nev], "yes" if tukros else "no",
                 "HOLDS" if egyezik else "FAILS"))
    print()

    # --- TA: the single-hole filling ---------------------------------------
    print("== TA  single hole, N = n-1: winner is mirror-marked, mirrors tie ==")
    egylyuk = np.array([a[HELYEK - 2] for a in arak])
    legolcsobb = egylyuk.min()
    gyoztesek = [nevek[i] for i in range(len(nevek))
                 if egylyuk[i] <= legolcsobb + TURES]
    print("   prices at N = %d:" % (HELYEK - 1))
    for nev, p in zip(nevek, egylyuk):
        print("      %-22s %14.6f   (T - peak = %14.6f)"
              % (nev, p, NYOM - float(np.max(letrak[nevek.index(nev)]))))
    print("   winners: %s" % ", ".join(gyoztesek))
    mind_tukros = all(hiany[g] <= TURES for g in gyoztesek)
    print("   every winner mirror-marked: %s -- %s"
          % ("yes" if mind_tukros else "NO", "HOLDS" if mind_tukros else "FAILS"))
    print()

    # --- L4: the mirror form (hole-mirror in one line) ---------------------
    print("== L4  for mirror-marked X: price(n-m) = T - 4km + price(m) ==")
    for nev, lam, ar in zip(nevek, letrak, arak):
        if hiany[nev] > TURES:
            continue
        m = np.arange(1, HELYEK)
        bal = ar[HELYEK - m - 1]
        jobb = NYOM - CSUCS_KORLAT * m + ar[m - 1]
        print("   %-22s largest deviation over all m: %.3e -- %s"
              % (nev, float(np.max(np.abs(bal - jobb))),
                 "HOLDS" if float(np.max(np.abs(bal - jobb))) <= 1e-7 else "FAILS"))
    print()

    # --- TB: the certified stretch -----------------------------------------
    print("== TB  certified stretch: price_X(m) < m * deficit_Z  =>  X beats Z at N = n-m ==")
    print("   %-22s %-22s %10s %14s %10s" % ("mirror-marked X", "non-mirror Z",
                                             "deficit", "certified m", "= fillings N >="))
    for xi, xnev in enumerate(nevek):
        if hiany[xnev] > TURES:
            continue
        for zi, znev in enumerate(nevek):
            if hiany[znev] <= TURES:
                continue
            d = hiany[znev]
            m = np.arange(1, HELYEK)
            teljesul = arak[xi][m - 1] < d * m
            # the certified stretch is the initial run of m where it holds
            hatar = int(np.argmax(~teljesul)) if not teljesul.all() else HELYEK - 1
            # verify the conclusion really holds on that stretch
            valos = bool(np.all(arak[xi][HELYEK - m[:hatar] - 1]
                                < arak[zi][HELYEK - m[:hatar] - 1] + TURES))
            print("   %-22s %-22s %10.5f %14d %10d   %s"
                  % (xnev, znev, d, hatar, HELYEK - hatar,
                     "verified" if valos else "CONTRADICTED"))
    print()
    print("   (a sufficient condition, so the stretch is a lower bound on the real one)")
    print()
    print("   (%.1f s)" % (time.time() - kezd))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
