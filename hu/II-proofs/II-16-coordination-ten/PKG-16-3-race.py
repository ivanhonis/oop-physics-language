# PKG-16-3 — A verseny (II/16)
# A PKG-16-2 letraira epul, aramoltatott top-2 kovetessel (a teljes
# koltsegmatrix nem fer memoriaba). Elsodleges ut: hosszu-lebegos (H3-szabaly).
# Dolga: negyfoku lepcso-itelet a J1–J5 otoson (a nevesitett visszafordulas-
# esettel); K-a a teto hovatartozasa; teljes-mezony olvasat; K-b fesu;
# K-c dominancia-kuszobok es hezag-aranyok; K-d hej-illeszkedes;
# kiolvasas-elokeszites.

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
        print("== PKG-16-3 — a verseny: nevesitett halok ==")
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
        print("nevesitett resz kesz (%.0f s) — inditsd ujra a csaladhoz"
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
        print("csalad: %d / %d kesz (%.0f s) — %s"
              % (veg, len(CSALAD), time.time()-t0,
                 "inditsd ujra" if veg < len(CSALAD) else "jon az elemzes"))
        return
    letrak5 = {n: zart_letra(*FO[n]) for n in ("J1","J2","J3","J4","J5")}
    print("== PKG-16-3 — elemzes ==")

    # regisztralt tenyek
    print("tenyek: N=1 also ket ar: %.2e / %.2e | N=3 legjobb ar: %.6f (>0) | "
          "teli: |elteres| = %.2e"
          % (float(best1[0]), float(best2[0]), float(best1[2]),
             abs(float(best1[-1]) - 2488320.0)))

    # fo otos: gyoztes-futamok
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
            cimkek.append("H:" + "+".join(kik))
    fut5 = futamok(cimkek)
    print("\ngyoztes-futamok a fo otoson:")
    for f in fut5:
        if f[2]-f[1]+1 >= 3 or f[0].startswith("H"):
            print("   %-18s %7d .. %7d  (%d)" % (f[0], f[1], f[2], f[2]-f[1]+1))

    # K-a: a felso fel es a teto
    felso = cimkek[NH//2:]
    megoszlas = {}
    for c in felso:
        megoszlas[c] = megoszlas.get(c, 0) + 1
    print("\nK-a: a felso fel megoszlasa az otoson: %s"
          % dict(sorted(megoszlas.items(), key=lambda x: -x[1])[:6]))

    # teljes mezony
    szigoru = best2 - best1 > TURES
    gyoz = {}
    for i in np.unique(bid[szigoru]):
        nev = NEVEK[i] if i < 13 else str(CSALAD[i-13])
        gyoz[nev] = int(np.sum((bid == i) & szigoru))
    fo_nyer = sum(gyoz.get(n, 0) for n in ("J1","J2","J3","J4","J5"))
    print("teljes mezony: a fo otos szigoruan nyert toltesei %d / %d; "
          "holtversenyes toltes %d" % (fo_nyer, NH, int(np.sum(~szigoru))))
    print("   legtobbet nyerok: %s"
          % sorted(gyoz.items(), key=lambda x: -x[1])[:6])
    print("K-b fesu (elso 24): %s"
          % " | ".join("%d:%s" % (n+1,
             (NEVEK[bid[n]] if bid[n] < 13 else str(CSALAD[bid[n]-13]))
             if szigoru[n] else "H") for n in range(24)))

    # K-c: paronkenti atbillenesek es dominancia-kuszobok az otoson
    print("\nK-c: par | N*-gepi | ar-atbillenes | arany")
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
                  % (otos[a], otos[b], ng, at if at else "nincs",
                     "%.1f%%" % (100.0*ng/at) if at else "—"))

    # K-d: hej-illeszkedes a fo savhatarokon
    print("\nK-d: savhatar kontra a bejovo gyoztes polc-hatarai:")
    for ix in range(1, len(fut5)):
        c, kezd = fut5[ix][0], fut5[ix][1]
        if c not in otos or fut5[ix][2]-kezd < 3:
            continue
        l = letrak5[c]
        resek = np.where(np.diff(l) > RES_KUSZOB)[0] + 1
        legk = int(resek[np.argmin(np.abs(resek - kezd))])
        print("   %8d (%s): legkozelebbi zart fok %8d, tavolsag %d"
              % (kezd, c, legk, abs(legk - kezd)))

    # kiolvasas-elokeszites: a legmagasabb kiterjedesu allo sav
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
        print("\nkiolvasas: a legmagasabb kiterjedesu allo sav %s (%d..%d); "
              "legszelesebb res %.6f; valasztott zart fok N = %d"
              % (gy, sav[0], sav[1], legszel, val))

if __name__ == "__main__":
    main()
