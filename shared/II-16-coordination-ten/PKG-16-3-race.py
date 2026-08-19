# PKG-16-3 — The race (II/16)
# Builds on the ladders of PKG-16-2, with streamed top-2 tracking (the full
# cost matrix does not fit in memory). Primary route: extended precision (rule H3).
# Its business: the four-rung staircase verdict on the quintuple J1-J5 (with the
# named turn-back case); Q-a where the top belongs; the full-field reading;
# Q-b the comb; Q-c dominance thresholds and gap ratios; Q-d shell fit;
# preparation of the readout.
#
# Note: the script is sectioned and restartable — it saves its state into
# verseny16_allapot.npz and must be run again until it reports the analysis.

import numpy as np, time
from itertools import combinations

NH = 12**5
TURES = 1e-8
RES_KUSZOB = 1e-6

FO = {
 "J1": ((NH,), [(1,),(2,),(3,),(4,),(5,)]),
 "J2": ((432,576), [(1,0),(0,1),(1,1),(1,-1),(0,2)]),
 "J3": ((54,64,72), [(1,0,0),(0,1,0),(0,0,1),(0,1,-1),(0,1,1)]),
 "J4": ((18,24,24,24), [(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1),(0,0,1,-1)]),
 "J5": ((12,)*5, [tuple(1 if i==j else 0 for i in range(5)) for j in range(5)]),
 "K1": ((48,72,72), [(1,0,0),(0,1,0),(0,0,1),(0,1,-1),(0,1,1)]),
 "K2": ((12,24,24,36), [(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1),(0,0,1,-1)]),
 "K3": ((288,864), [(1,0),(0,1),(1,1),(1,-1),(0,2)]),
 "KA2": ((432,576), [(1,0),(0,1),(1,1),(1,-1),(2,0)]),
 "KA3": ((54,64,72), [(1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,0,1)]),
 "KA4": ((18,24,24,24), [(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1),(1,0,0,-1)]),
 "KP3": ((54,64,72), [(1,0,0),(0,1,0),(0,0,1),(1,-1,-1),(1,-1,1)]),
 "KP4": ((18,24,24,24), [(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1),(0,1,1,1)]),
}
NEVEK = list(FO.keys())
CSALAD = list(combinations(range(1, 13), 5))

def zart_letra(alak, fel):
    dt = np.longdouble
    r = np.meshgrid(*[(2*np.pi*np.arange(L)).astype(dt)/L for L in alak],
                    indexing="ij")
    lam = np.zeros(alak, dtype=dt)
    for s in fel:
        lam += 2.0 - 2.0*np.cos(sum(si*gi for si, gi in zip(s, r)))
    return np.sort(lam.ravel())

def futamok(cimkek):
    out = []
    for i, c in enumerate(cimkek):
        if out and out[-1][0] == c:
            out[-1][2] = i+1
        else:
            out.append([c, i+1, i+1])
    return out

ALLAPOT = "verseny16_allapot.npz"
ADAG = 260

def main():
    t0 = time.time()
    import os
    if not os.path.exists(ALLAPOT):
        print("== PKG-16-3 — the race: the named networks ==")
        kolt = {}
        for nev in NEVEK:
            kolt[nev] = np.cumsum(zart_letra(*FO[nev]))
        best1 = kolt["J1"].copy()
        best2 = np.full(NH, np.inf, dtype=np.longdouble)
        bid = np.zeros(NH, dtype=np.int16)
        for i, nev in enumerate(NEVEK[1:], start=1):
            c = kolt[nev]
            jobb = c < best1
            best2 = np.where(jobb, best1, np.minimum(best2, c))
            best1 = np.where(jobb, c, best1)
            bid[jobb] = i
        np.savez(ALLAPOT, best1=best1, best2=best2, bid=bid, kesz=0,
                 **{"k_"+n: kolt[n] for n in NEVEK})
        print("the named part is done (%.0f s) — run again for the family"
              % (time.time()-t0))
        return
    A = np.load(ALLAPOT)
    kesz = int(A["kesz"])
    best1, best2, bid = A["best1"], A["best2"], A["bid"].astype(np.int16)
    kolt = {n: A["k_"+n] for n in NEVEK}
    if kesz < len(CSALAD):
        kk = (2*np.pi*np.arange(NH)).astype(np.longdouble)/NH
        cos_tar = {s: 2.0-2.0*np.cos(s*kk) for s in range(1, 13)}
        veg = min(kesz + ADAG, len(CSALAD))
        for j in range(kesz, veg):
            tag = CSALAD[j]
            c = np.cumsum(np.sort(cos_tar[tag[0]]+cos_tar[tag[1]]
                          +cos_tar[tag[2]]+cos_tar[tag[3]]+cos_tar[tag[4]]))
            jobb = c < best1
            best2 = np.where(jobb, best1, np.minimum(best2, c))
            best1 = np.where(jobb, c, best1)
            bid[jobb] = 13 + j
        np.savez(ALLAPOT, best1=best1, best2=best2, bid=bid, kesz=veg,
                 **{"k_"+n: kolt[n] for n in NEVEK})
        print("family: %d / %d done (%.0f s) — %s"
              % (veg, len(CSALAD), time.time()-t0,
                 "run again" if veg < len(CSALAD) else "the analysis follows"))
        return
    letrak5 = {n: zart_letra(*FO[n]) for n in ("J1","J2","J3","J4","J5")}
    print("== PKG-16-3 — analysis ==")

    # registered facts
    print("facts: N=1 lowest two prices: %.2e / %.2e | N=3 best price: %.6f (>0) | "
          "full end: |deviation| = %.2e"
          % (float(best1[0]), float(best2[0]), float(best1[2]),
             abs(float(best1[-1]) - 2488320.0)))

    # main quintuple: winner runs
    J = np.stack([kolt[n] for n in ("J1","J2","J3","J4","J5")])
    cimkek = []
    for n in range(NH):
        o = J[:, n]
        r = np.argsort(o)
        if o[r[1]] - o[r[0]] > TURES:
            cimkek.append(NEVEK[r[0]])
        else:
            kik = sorted("J%d" % (i+1) for i in range(5)
                         if o[i] - o[r[0]] <= TURES)
            cimkek.append("T:" + "+".join(kik))
    fut5 = futamok(cimkek)
    print("\nwinner runs on the main quintuple:")
    for f in fut5:
        if f[2]-f[1]+1 >= 3 or f[0].startswith("T"):
            print("   %-18s %7d .. %7d  (%d)" % (f[0], f[1], f[2], f[2]-f[1]+1))

    # Q-a: the upper half and the top
    felso = cimkek[NH//2:]
    megoszlas = {}
    for c in felso:
        megoszlas[c] = megoszlas.get(c, 0) + 1
    print("\nQ-a: split of the upper half on the quintuple: %s"
          % dict(sorted(megoszlas.items(), key=lambda x: -x[1])[:6]))

    # full field
    szigoru = best2 - best1 > TURES
    gyoz = {}
    for i in np.unique(bid[szigoru]):
        nev = NEVEK[i] if i < 13 else str(CSALAD[i-13])
        gyoz[nev] = int(np.sum((bid == i) & szigoru))
    fo_nyer = sum(gyoz.get(n, 0) for n in ("J1","J2","J3","J4","J5"))
    print("full field: the main quintuple wins strictly at %d / %d fillings; "
          "tied fillings %d" % (fo_nyer, NH, int(np.sum(~szigoru))))
    print("   winning the most: %s"
          % sorted(gyoz.items(), key=lambda x: -x[1])[:6])
    print("Q-b comb (first 24): %s"
          % " | ".join("%d:%s" % (n+1,
             (NEVEK[bid[n]] if bid[n] < 13 else str(CSALAD[bid[n]-13]))
             if szigoru[n] else "T") for n in range(24)))

    # Q-c: pairwise tippings and dominance thresholds on the quintuple
    print("\nQ-c: pair | N*-machine | price tipping | ratio")
    otos = ("J1","J2","J3","J4","J5")
    for a in range(5):
        for b in range(a+1, 5):
            la, lb = letrak5[otos[a]], letrak5[otos[b]]
            j = np.where(la[1:] > lb[1:] + 1e-12)[0]
            ng = int(j[0]) + 1 if len(j) else NH
            ca, cb = kolt[otos[a]], kolt[otos[b]]
            j = np.where(ca[1:] > cb[1:] + TURES)[0]
            at = int(j[0]) + 2 if len(j) else None
            print("   %s-%s  %7d  %10s  %s"
                  % (otos[a], otos[b], ng, at if at else "none",
                     "%.1f%%" % (100.0*ng/at) if at else "—"))

    # Q-d: shell fit at the main band boundaries
    print("\nQ-d: band boundary versus the shelf boundaries of the incoming winner:")
    for ix in range(1, len(fut5)):
        c, kezd = fut5[ix][0], fut5[ix][1]
        if c not in otos or fut5[ix][2]-kezd < 3:
            continue
        l = letrak5[c]
        resek = np.where(np.diff(l) > RES_KUSZOB)[0] + 1
        legk = int(resek[np.argmin(np.abs(resek - kezd))])
        print("   %8d (%s): nearest closed degree %8d, distance %d"
              % (kezd, c, legk, abs(legk - kezd)))

    # readout preparation: the standing band of highest extension
    savok = {}
    for f in fut5:
        if f[0] in otos and f[2]-f[1]+1 >= 3:
            savok.setdefault(f[0], []).append((f[1], f[2], f[2]-f[1]+1))
    gy = None
    for nev in ("J5","J4","J3","J2"):
        if nev in savok:
            gy = nev; break
    if gy:
        sav = max(savok[gy], key=lambda x: x[2])
        l = letrak5[gy]
        resek = np.diff(l)
        benn = [(int(i+1), float(resek[i]))
                for i in np.where(resek > RES_KUSZOB)[0]
                if sav[0] <= i+1 <= sav[1]]
        legszel = max(r for _, r in benn)
        jel = sorted(nf for nf, r in benn if r > legszel - 1e-9)
        felett = [nf for nf in jel if nf >= NH//2]
        val = min(felett) if felett else jel[-1]
        print("\nreadout: the standing band of highest extension is %s (%d..%d); "
              "widest gap %.6f; chosen closed degree N = %d"
              % (gy, sav[0], sav[1], legszel, val))

if __name__ == "__main__":
    main()
