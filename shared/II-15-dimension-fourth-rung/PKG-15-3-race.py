# PKG-15-3 — The race (II/15)
# Builds on the outgoing claims of PKG-15-2 (L1-L5). Its business:
#   1) cost curves for N = 1..20736 on all 503 entrants (from the closed ladders)
#   2) winner table on the main four (J1-J4) — the basis of the staircase
#      verdict — and on the full field (the honest reading)
#   3) verdict by the three-rung rule of PKG-15-1 §7; tolerance: 1e-8 (L5)
#   4) checking the pre-registered facts (N = 1, 2, 3, full)
#   5) evaluating the three registered questions (Q-a, Q-b, Q-c)
#   6) independent recomputation: the J1-J4 curves on the extended-precision route too
#   7) preparing the readout: closed degrees in the winner of the highest standing band

import numpy as np
from itertools import combinations, product
import time

N = 20736
TURES = 1e-8          # identity tolerance (L5, fixed)
RES_KUSZOB = 1e-6     # threshold of a closed degree (shelf boundary) — a declared convention

# ----------------------------------------------------------------- field ---
EGYSEG4 = [(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)]
J3LEP = [(1,0,0),(0,1,0),(0,0,1),(1,-1,-1)]
J2LEP = [(1,0),(0,1),(1,1),(1,-1)]
FO = {
    "J1": ((N,),           [(1,),(2,),(3,),(4,)]),
    "J2": ((144,144),      J2LEP),
    "J3": ((24,24,36),     J3LEP),
    "J4": ((12,12,12,12),  EGYSEG4),
    "K1": ((16,36,36),     J3LEP),
    "K2": ((12,36,48),     J3LEP),
    "K3": ((8,8,18,18),    EGYSEG4),
    "K4": ((48,432),       J2LEP),
}
CSALAD = list(combinations(range(1, 13), 4))

def zart_letra(alak, fel, dt=np.float64):
    racsok = np.meshgrid(*[(2*np.pi*np.arange(L)/L).astype(dt) for L in alak],
                         indexing="ij")
    lam = np.zeros(alak, dtype=dt)
    for s in fel:
        fazis = sum(si*gi for si, gi in zip(s, racsok))
        lam += 2.0 - 2.0*np.cos(fazis)
    return np.sort(lam.ravel())

def futamok_rov(lista):
    """Compressing a number sequence into intervals."""
    out = []
    for x in lista:
        if out and out[-1][1] == x-1:
            out[-1][1] = x
        else:
            out.append([x, x])
    return ", ".join("%d..%d" % (a, b) if a != b else str(a) for a, b in out)

def futamok(cimkek):
    """Compressing a label sequence into (label, from, to) runs."""
    out = []
    for i, c in enumerate(cimkek):
        if out and out[-1][0] == c:
            out[-1][2] = i+1
        else:
            out.append([c, i+1, i+1])
    return out

def main():
    t0 = time.time()
    print("== PKG-15-3 — the race ==")

    # PRIMARY ROUTE: extended precision (the float64 accumulation error near the
    # full end is ~2e-8, which would cross the fixed 1e-8 tolerance; the
    # extended-precision accumulation error is ~1e-10 — the tolerance stays
    # four orders of magnitude above it)
    nevek = list(FO.keys()) + [str(t) for t in CSALAD]
    letrak = np.empty((len(nevek), N), dtype=np.longdouble)
    kL = (2*np.pi*np.arange(N)).astype(np.longdouble)/N
    for i, nev in enumerate(nevek):
        if nev in FO:
            letrak[i] = zart_letra(*FO[nev], dt=np.longdouble)
        else:
            tag = eval(nev)
            letrak[i] = np.sort(sum(2-2*np.cos(s*kL) for s in tag))
    kolt = np.cumsum(letrak, axis=1)                 # kolt[i, n-1] = price at N=n
    print("cost curves (extended precision): %d networks, %.1f s"
          % (len(nevek), time.time()-t0))

    # -- pre-registered facts --
    t1 = np.sum(kolt[:, 0] < TURES)
    t2 = np.sum(kolt[:, 1] < TURES)
    t3 = [nevek[i] for i in np.where(kolt[:, 2] < TURES)[0]]
    teli = np.max(np.abs(kolt[:, -1] - 165888.0))
    print("registered facts: N=1 at zero %d/503 | N=2 at zero %d (expected 16) | "
          "N=3 at zero %s | full-end deviation %.1e — %s"
          % (t1, t2, t3, teli,
             "HOLDS" if (t1 == 503 and t2 == 16 and t3 == ["(3, 6, 9, 12)"]
                         and teli < 1e-6) else "FAILS"))

    # -- winner table on the main four --
    J = kolt[:4]                                     # J1..J4
    cimkek = []
    for n in range(N):
        oszlop = J[:, n]
        r = np.argsort(oszlop)
        if oszlop[r[1]] - oszlop[r[0]] > TURES:
            cimkek.append(nevek[r[0]])
        else:
            kik = sorted(nevek[i] for i in range(4)
                         if oszlop[i] - oszlop[r[0]] <= TURES)
            cimkek.append("T:" + "+".join(kik))
    fut4 = futamok(cimkek)
    print("\nwinner runs on the main four (label, from, to):")
    for f in fut4:
        print("   %-14s %6d .. %6d   (%d fillings)" % (f[0], f[1], f[2], f[2]-f[1]+1))

    # -- verdict per §7 --
    savok = {}
    for f in fut4:
        if f[0] in ("J2", "J3", "J4"):
            savok.setdefault(f[0], []).append((f[1], f[2], f[2]-f[1]+1))
    print("\nbasis of the verdict: longest connected bands:")
    for j in ("J2", "J3", "J4"):
        if j in savok:
            fo_sav = max(savok[j], key=lambda x: x[2])
            print("   %s: %d..%d (%d fillings); further patches: %d"
                  % (j, fo_sav[0], fo_sav[1], fo_sav[2], len(savok[j])-1))
        else:
            print("   %s: NO winning filling" % j)

    # -- Q-b: data of the mirror question --
    print("\nQ-b (mirror question): ladder width (largest beat): "
          "J3 %.6f, J4 %.6f" % (letrak[2][-1], letrak[3][-1]))
    felso = cimkek[N//2:]
    fj = {c: felso.count(c) for c in set(felso)}
    print("   winner split on the four in the upper half (N > %d): %s"
          % (N//2, dict(sorted(fj.items(), key=lambda x: -x[1]))))

    # -- Q-a: shell fit at the band boundaries --
    print("\nQ-a (shell fit) — band boundary versus the shelf boundaries of the incoming winner:")
    for ix in range(1, len(fut4)):
        c, kezdet = fut4[ix][0], fut4[ix][1]
        if c not in ("J1", "J2", "J3", "J4"):
            continue
        l = letrak[nevek.index(c)]
        resek = np.where(np.diff(l) > RES_KUSZOB)[0] + 1   # closed degrees (in N)
        legkozelebb = int(resek[np.argmin(np.abs(resek - kezdet))])
        print("   %6d (start of the %s band): nearest closed degree %6d, distance %d"
              % (kezdet, c, legkozelebb, abs(legkozelebb - kezdet)))

    # -- full-field reading --
    t2s = time.time()
    also = np.min(kolt, axis=0)
    gyoztes_db = {}
    holtversenyek = 0
    telj_cimkek = []
    for n in range(N):
        kik = np.where(kolt[:, n] - also[n] <= TURES)[0]
        if len(kik) == 1:
            nev = nevek[kik[0]]
            gyoztes_db[nev] = gyoztes_db.get(nev, 0) + 1
            telj_cimkek.append(nev)
        else:
            holtversenyek += 1
            telj_cimkek.append("T")
    fo_nyer = sum(gyoztes_db.get(j, 0) for j in ("J1","J2","J3","J4"))
    top = sorted(gyoztes_db.items(), key=lambda x: -x[1])[:8]
    print("\nfull field (503 entrants): the main four win strictly at %d / %d "
          "fillings; tied fillings %d" % (fo_nyer, N, holtversenyek))
    print("   entrants winning the most fillings: %s" % top)
    print("   (%.0f s)" % (time.time()-t2s))

    # -- Q-c: comb pattern in the lower range --
    print("\nQ-c (comb pattern): winners of the first 24 fillings of the full field:")
    print("   " + " | ".join("%d:%s" % (n+1, telj_cimkek[n]) for n in range(24)))

    # -- independent recomputation: float64 cross-check on the main four --
    Jf = np.empty((4, N))
    for i, nev in enumerate(("J1","J2","J3","J4")):
        Jf[i] = np.cumsum(zart_letra(*FO[nev], dt=np.float64))
    elteres = float(np.max(np.abs(Jf - J.astype(np.float64))))
    cimkek_f = []
    for n in range(N):
        oszlop = Jf[:, n]
        r = np.argsort(oszlop)
        if oszlop[r[1]] - oszlop[r[0]] > TURES:
            cimkek_f.append(nevek[r[0]])
        else:
            kik = sorted(nevek[i] for i in range(4)
                         if oszlop[i] - oszlop[r[0]] <= TURES)
            cimkek_f.append("T:" + "+".join(kik))
    elter_hol = [n+1 for n in range(N) if cimkek_f[n] != cimkek[n]]
    print("\ncross-check (float64): largest cost deviation %.2e; "
          "the winner row differs at %d fillings%s" % (elteres, len(elter_hol),
          " — these: %s" % futamok_rov(elter_hol) if elter_hol else ""))

    # -- preparing the readout: closed degrees in the highest standing band --
    if "J4" in savok:
        gy = "J4"
    elif "J3" in savok:
        gy = "J3"
    else:
        gy = None
    if gy:
        fo_sav = max(savok[gy], key=lambda x: x[2])
        l = letrak[nevek.index(gy)]
        resek = np.diff(l)
        benn = [(int(i+1), float(resek[i])) for i in np.where(resek > RES_KUSZOB)[0]
                if fo_sav[0] <= i+1 <= fo_sav[1]]
        benn.sort(key=lambda x: -x[1])
        legszel = benn[0][1]
        jeloltek_f = sorted(nf for nf, r in benn if r > legszel - 1e-9)
        felett = [nf for nf in jeloltek_f if nf >= N//2]
        valasztott = min(felett, key=lambda nf: nf - N//2) if felett else jeloltek_f[-1]
        print("\nreadout preparation: the winner of the highest standing rung "
              "(by extension) is %s, band %d..%d" % (gy, fo_sav[0], fo_sav[1]))
        print("   the widest gaps of the band (gap %.6f) above these closed degrees: %s"
              % (legszel, jeloltek_f))
        print("   choice rule (fixed): among the widest gaps, the one nearest "
              "half filling from above -> N = %d" % valasztott)

if __name__ == "__main__":
    main()
