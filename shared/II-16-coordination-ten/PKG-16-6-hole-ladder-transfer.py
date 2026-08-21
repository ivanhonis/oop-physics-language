# PKG-16-6-hole-ladder-transfer.py -- the hole ladder at coordination ten
#
# A transfer package, in the manner of PKG-16-5. The hole-ladder theorem and the
# dense-end theorem were derived and confirmed at coordination eight (PKG-15-10,
# PKG-15-11). Their proofs never mention eight: they use only the trace tie, the
# ceiling 4k, and the carrier theorem, all of which are stated for arbitrary k.
# So the transfer needs no new derivation -- but it does need the numbers, on a
# field twelve times larger and one rung higher.
#
# System (PKG-16-1): n = 248832 = 12^5 places, k = 5 pairs, coordination ten.
#   T = 2kn = 2488320   ceiling 4k = 20
#
# What is checked here, with the same codes as PKG-15-11:
#   E1  price(n-m) = T - 4km + D(m), on every entrant, at every filling
#   E2  mirror-marked  <=>  hole ladder == beat ladder
#   E3  the dense-end winner is the entrant with the cheapest hole ladder
#   TA  at the single-hole filling the winner is mirror-marked
#
# The expected pattern from II/16: only the native five-extension carries the
# mirror mark, so unlike coordination eight there is no mirror-marked PAIR and
# hence no tie at the single hole. That difference is itself worth reporting.

import sys
import time
from pathlib import Path

import numpy as np

SHARED = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SHARED))

import summation                                             # noqa: E402

HELYEK = 248832                          # 12^5
FOKOK = 5                                # k
CSUCS = 4.0 * FOKOK                      # 20
NYOM = 2.0 * FOKOK * HELYEK              # 2488320
TURES = summation.TURES

# The main field exactly as PKG-16-1 declares it.
MEZONY = [
    ("J1 line", (HELYEK,), [(1,), (2,), (3,), (4,), (5,)]),
    ("J2 plane", (432, 576),
     [(1, 0), (0, 1), (1, 1), (1, -1), (0, 2)]),
    ("J3 space", (54, 64, 72),
     [(1, 0, 0), (0, 1, 0), (0, 0, 1), (0, 1, -1), (0, 1, 1)]),
    ("J4 four-extension", (18, 24, 24, 24),
     [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1), (0, 0, 1, -1)]),
    ("J5 five-extension (native)", (12, 12, 12, 12, 12),
     [tuple(1 if i == j else 0 for i in range(5)) for j in range(5)]),
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


def savok(nevek, gorbek):
    gy = np.argmin(gorbek, axis=0)
    ki, kezd = [], 0
    for n in range(1, gorbek.shape[1]):
        if gy[n] != gy[kezd]:
            ki.append((nevek[gy[kezd]], kezd + 1, n))
            kezd = n
    ki.append((nevek[gy[kezd]], kezd + 1, gorbek.shape[1]))
    return ki


def main():
    kezd = time.time()
    print("== PKG-16-6 -- the hole ladder at coordination ten (transfer) ==")
    print("   n = %d = 12^5, k = %d, T = %.0f, ceiling 4k = %.0f"
          % (HELYEK, FOKOK, NYOM, CSUCS))
    print()

    nevek, utemek, arak, hianyok, D = [], [], [], [], []
    for nev, oldalak, lepesek in MEZONY:
        assert int(np.prod(oldalak)) == HELYEK, nev
        lam = letra(oldalak, lepesek)
        nevek.append(nev)
        utemek.append(lam)
        arak.append(summation.pontos_cumsum(lam))
        h = np.sort(CSUCS - lam)
        hianyok.append(h)
        D.append(summation.pontos_cumsum(h))
    print("   five entrants built (%.1f s)" % (time.time() - kezd))
    print()

    print("== precondition: the trace tie at coordination ten ==")
    baj = max(abs(summation.pontos_osszeg(l) - NYOM) for l in utemek)
    print("   largest deviation from %.0f: %.3e -- %s"
          % (NYOM, baj, "HOLDS" if baj <= TURES else "FAILS"))
    bajh = max(abs(summation.pontos_osszeg(h) - NYOM) for h in hianyok)
    print("   the HOLE ladders also sum to %.0f: %.3e -- %s"
          % (NYOM, bajh, "HOLDS" if bajh <= TURES else "FAILS"))
    if baj > TURES or bajh > TURES:
        return 1
    print()

    m = np.arange(1, HELYEK)

    print("== E1  price(n-m) = T - 4km + D(m) ==")
    legrosszabb = 0.0
    for nev, ar, d in zip(nevek, arak, D):
        elt = float(np.max(np.abs(ar[HELYEK - m - 1] - (NYOM - CSUCS * m + d[m - 1]))))
        legrosszabb = max(legrosszabb, elt)
        print("   %-28s largest deviation: %.3e" % (nev, elt))
    print("   -- %s" % ("HOLDS" if legrosszabb <= 1e-6 else "FAILS"))
    print()

    print("== E2  mirror-marked <=> hole ladder == beat ladder ==")
    tukros = []
    for nev, lam, h in zip(nevek, utemek, hianyok):
        azonos = float(np.max(np.abs(lam - h))) <= TURES
        tukros.append(azonos)
        print("   %-28s peak %9.5f | mirror: %s" % (nev, lam[-1], "yes" if azonos else "no"))
    print("   mirror-marked entrants: %d" % sum(tukros))
    print()

    print("== TA  the single-hole filling, N = n-1 ==")
    egy = np.array([a[HELYEK - 2] for a in arak])
    legolcs = egy.min()
    gyoztesek = [nevek[i] for i in range(len(nevek)) if egy[i] <= legolcs + TURES]
    for nev, p in zip(nevek, egy):
        print("   %-28s %16.6f" % (nev, p))
    print("   winners: %s" % ", ".join(gyoztesek))
    ta = all(tukros[nevek.index(g)] for g in gyoztesek)
    print("   every winner mirror-marked: %s -- %s"
          % ("yes" if ta else "NO", "HOLDS" if ta else "FAILS"))
    print("   note: only ONE entrant carries the mark here, so unlike coordination")
    print("         eight there is no tie at the single hole.")
    print()

    print("== E3  dense-end winner == cheapest hole ladder ==")
    ar_t, D_t = np.array(arak), np.array(D)
    elt = 0
    for mm in (1, 10, 100, 1000, 10000, 50000, 124416):
        N = HELYEK - mm
        a, b = int(np.argmin(ar_t[:, N - 1])), int(np.argmin(D_t[:, mm - 1]))
        if a != b:
            elt += 1
        print("   m=%7d (N=%7d): race %-28s hole ladder %-28s %s"
              % (mm, N, nevek[a], nevek[b], "" if a == b else "<-- DIFFERS"))
    print("   -- %s" % ("HOLDS on every sampled filling" if not elt else "FAILS"))
    print()

    print("== the exact dense-end boundaries (K-PKG1511-4) ==")
    print("   %-28s %-28s %12s" % ("mirror X", "non-mirror Z", "X wins N >="))
    for xi in [i for i, t in enumerate(tukros) if t]:
        for zi in [i for i, t in enumerate(tukros) if not t]:
            maszk = D_t[xi, m - 1] < D_t[zi, m - 1]
            hatar = int(np.argmax(~maszk)) if not maszk.all() else HELYEK - 1
            print("   %-28s %-28s %12d" % (nevek[xi], nevek[zi], HELYEK - hatar))
    print()

    print("== the main-four+one race, band structure ==")
    for nev, tol, ig in savok(nevek, np.array(arak)):
        print("   %-28s %7d .. %7d  (%d fillings)" % (nev, tol, ig, ig - tol + 1))
    print()
    print("   (%.1f s)" % (time.time() - kezd))
    return 0 if legrosszabb <= 1e-6 and ta and not elt else 1


if __name__ == "__main__":
    raise SystemExit(main())
