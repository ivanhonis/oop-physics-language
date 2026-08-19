# PKG-15-3 — A verseny (II/15)
# A PKG-15-2 kimeno allitasaira (L1–L5) epul. Dolga:
#   1) koltseggorbek N = 1..20736 mind az 503 indulon (zart letrakbol)
#   2) gyoztes-tabla a fo negyesen (J1–J4) — a lepcso-itelet alapja —
#      es a teljes mezonyon (oszinte olvasat)
#   3) itelet a PKG-15-1 §7 haromfoku szabalyaval; tures: 1e-8 (L5)
#   4) az elore regisztralt tenyek ellenorzese (N = 1, 2, 3, teli)
#   5) a harom regisztralt kerdes kiertekelese (K-a, K-b, K-c)
#   6) fuggetlen ujraszamolas: a J1–J4 gorbek hosszu-lebegos uton is
#   7) a kiolvasas elokeszitese: zart fokok a legmagasabb allo sav gyozteseben

import numpy as np
from itertools import combinations, product
import time

N = 20736
TURES = 1e-8          # azonossag-tures (L5, rogzitett)
RES_KUSZOB = 1e-6     # zart fok (polc-hatar) kuszobe — deklaralt konvencio

# ---------------------------------------------------------------- mezony ---
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
    """Szamsor tomoritese intervallumokka."""
    out = []
    for x in lista:
        if out and out[-1][1] == x-1:
            out[-1][1] = x
        else:
            out.append([x, x])
    return ", ".join("%d..%d" % (a, b) if a != b else str(a) for a, b in out)

def futamok(cimkek):
    """Cimkesor tomoritese (cimke, tol, ig) futamokra."""
    out = []
    for i, c in enumerate(cimkek):
        if out and out[-1][0] == c:
            out[-1][2] = i+1
        else:
            out.append([c, i+1, i+1])
    return out

def main():
    t0 = time.time()
    print("== PKG-15-3 — a verseny ==")

    # ELSODLEGES UT: hosszu-lebegos (a float64 halmozasi hiba a teli veg
    # kozeleben ~2e-8, ami atlepne a rogzitett 1e-8 turest; a hosszu-lebegos
    # halmozasi hiba ~1e-10 — a tures negy nagysagrenddel folotte marad)
    nevek = list(FO.keys()) + [str(t) for t in CSALAD]
    letrak = np.empty((len(nevek), N), dtype=np.longdouble)
    kL = (2*np.pi*np.arange(N)).astype(np.longdouble)/N
    for i, nev in enumerate(nevek):
        if nev in FO:
            letrak[i] = zart_letra(*FO[nev], dt=np.longdouble)
        else:
            tag = eval(nev)
            letrak[i] = np.sort(sum(2-2*np.cos(s*kL) for s in tag))
    kolt = np.cumsum(letrak, axis=1)                 # kolt[i, n-1] = ar N=n-nel
    print("koltseggorbek (hosszu-lebegos): %d halo, %.1f s"
          % (len(nevek), time.time()-t0))

    # -- elore regisztralt tenyek --
    t1 = np.sum(kolt[:, 0] < TURES)
    t2 = np.sum(kolt[:, 1] < TURES)
    t3 = [nevek[i] for i in np.where(kolt[:, 2] < TURES)[0]]
    teli = np.max(np.abs(kolt[:, -1] - 165888.0))
    print("regisztralt tenyek: N=1 nullan %d/503 | N=2 nullan %d (vart 16) | "
          "N=3 nullan %s | teli-elteres %.1e — %s"
          % (t1, t2, t3, teli,
             "ALL" if (t1 == 503 and t2 == 16 and t3 == ["(3, 6, 9, 12)"]
                       and teli < 1e-6) else "BUKIK"))

    # -- gyoztes-tabla a fo negyesen --
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
            cimkek.append("H:" + "+".join(kik))
    fut4 = futamok(cimkek)
    print("\ngyoztes-futamok a fo negyesen (cimke, tol, ig):")
    for f in fut4:
        print("   %-14s %6d .. %6d   (%d toltes)" % (f[0], f[1], f[2], f[2]-f[1]+1))

    # -- itelet a §7 szerint --
    savok = {}
    for f in fut4:
        if f[0] in ("J2", "J3", "J4"):
            savok.setdefault(f[0], []).append((f[1], f[2], f[2]-f[1]+1))
    print("\nitelet-alap: leghosszabb osszefuggo savok:")
    for j in ("J2", "J3", "J4"):
        if j in savok:
            fo_sav = max(savok[j], key=lambda x: x[2])
            print("   %s: %d..%d (%d toltes); tovabbi foltok: %d"
                  % (j, fo_sav[0], fo_sav[1], fo_sav[2], len(savok[j])-1))
        else:
            print("   %s: NINCS gyoztes toltese" % j)

    # -- K-b: tukor-kerdes adatai --
    print("\nK-b (tukor-kerdes): letra-szelesseg (legnagyobb utem): "
          "J3 %.6f, J4 %.6f" % (letrak[2][-1], letrak[3][-1]))
    felso = cimkek[N//2:]
    fj = {c: felso.count(c) for c in set(felso)}
    print("   a felso fel (N > %d) gyoztes-megoszlasa a negyesen: %s"
          % (N//2, dict(sorted(fj.items(), key=lambda x: -x[1]))))

    # -- K-a: hej-illeszkedes a savhatarokon --
    print("\nK-a (hej-illeszkedes) — savhatar kontra a bejovo gyoztes polc-hatarai:")
    for ix in range(1, len(fut4)):
        c, kezdet = fut4[ix][0], fut4[ix][1]
        if c not in ("J1", "J2", "J3", "J4"):
            continue
        l = letrak[nevek.index(c)]
        resek = np.where(np.diff(l) > RES_KUSZOB)[0] + 1   # zart fokok (N-ben)
        legkozelebb = int(resek[np.argmin(np.abs(resek - kezdet))])
        print("   %6d (%s sav kezdete): legkozelebbi zart fok %6d, tavolsag %d"
              % (kezdet, c, legkozelebb, abs(legkozelebb - kezdet)))

    # -- teljes-mezony olvasat --
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
            telj_cimkek.append("H")
    fo_nyer = sum(gyoztes_db.get(j, 0) for j in ("J1","J2","J3","J4"))
    top = sorted(gyoztes_db.items(), key=lambda x: -x[1])[:8]
    print("\nteljes mezony (503 indulo): a fo negyes szigoruan nyert tolteseinek "
          "szama %d / %d; holtversenyes toltes %d" % (fo_nyer, N, holtversenyek))
    print("   legtobb toltest nyero indulok: %s" % top)
    print("   (%.0f s)" % (time.time()-t2s))

    # -- K-c: fesu-minta az also tartomanyban --
    print("\nK-c (fesu-minta): a teljes mezony elso 24 toltesenek gyoztesei:")
    print("   " + " | ".join("%d:%s" % (n+1, telj_cimkek[n]) for n in range(24)))

    # -- fuggetlen ujraszamolas: float64 keresztellenorzes a fo negyesen --
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
            cimkek_f.append("H:" + "+".join(kik))
    elter_hol = [n+1 for n in range(N) if cimkek_f[n] != cimkek[n]]
    print("\nkeresztellenorzes (float64): legnagyobb koltseg-elteres %.2e; "
          "a gyoztes-sor %d toltesen ter el%s" % (elteres, len(elter_hol),
          " — ezek: %s" % futamok_rov(elter_hol) if elter_hol else ""))

    # -- a kiolvasas elokeszitese: zart fokok a legmagasabb allo savban --
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
        print("\nkiolvasas-elokeszites: a legmagasabb allo fok (kiterjedes "
              "szerint) gyoztese %s, sav %d..%d" % (gy, fo_sav[0], fo_sav[1]))
        print("   a sav legszelesebb resei (res %.6f) e zart fokok folott: %s"
              % (legszel, jeloltek_f))
        print("   valasztasi szabaly (rogzitve): a legszelesebb resek kozul a "
              "fel-tolteshez legkozelebbi felulrol -> N = %d" % valasztott)

if __name__ == "__main__":
    main()
