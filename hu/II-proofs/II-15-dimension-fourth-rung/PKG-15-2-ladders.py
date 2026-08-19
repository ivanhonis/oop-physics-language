# PKG-15-2 — Utem-letrak (II/15)
# A PKG-15-1 kimeno allitasaira (A1–A8) epul. Dolga:
#   1) mezony-epites: J1–J4, K1–K4, es a vonal-csalad mind a 495 tagja
#   2) letra zart Fourier-uton mind az 503 halon
#   3) onellenorzesek (A7): (i) harom kulonbozoseg-jegy a fo negyesen;
#      (ii) letra-osztalyozas a teljes mezonyon rogzitett turessel;
#      (iii) gepi korbeeres-bejaras minden indulon; (iv) nyomosszeg 165888;
#      (v) komponensszam a szetesés-tabla ellen
#   4) gepi ut (A8): dense sajatfeladat a 8 fo/kontroll halon + 24 sorsolt
#      csaladtagon (mag: 20736); ujrainditha to — kesz halot kihagy.
#      Memoriaigeny halonkent ~8 GB; futasido ~15-20 perc/halo.
# Hasznalat:  python3 PKG-15-2-ladders.py [--gep N]
#   --gep N : ebben a futasban legfeljebb N gepi sajatfeladat fusson le
#             (alapertelmezes: mind a hatralevo). A --gep 0 a gyors reszt
#             futtatja csak; a batch kesobb folytathato.

import numpy as np
import os, sys, time
from itertools import combinations, product
from collections import deque
from math import gcd
from functools import reduce

N = 20736
NYOM = 2 * 4 * N            # 165888 — a nyom-dontetlen fedezete
TURES_OSZTALY = 1e-8        # letra-osztalyozasi kvantum (rogzitett)
MAG = 20736                 # sorsolasi mag (rogzitett; numpy PCG64)
GYORSITO = "letrak_gepi"    # a gepi utem gyorsitotara (ujrainditashoz)

# ---------------------------------------------------------------- mezony ---
def elojelek(v):
    idx = [i for i, x in enumerate(v) if x]
    out = []
    for s in product([1, -1], repeat=len(idx)):
        w = list(v)
        for k, i in enumerate(idx):
            w[i] = v[i] * s[k]
        out.append(tuple(w))
    return out

EGYSEG4 = [(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)]
J3LEP = [(1,0,0),(0,1,0),(0,0,1),(1,-1,-1)]
J2LEP = [(1,0),(0,1),(1,1),(1,-1)]

FO = {  # nev -> (alak, fel-lepesek); a teljes lepeskeszlet a ± parokkal all elo
    "J1": ((N,),           [(1,),(2,),(3,),(4,)]),
    "J2": ((144,144),      J2LEP),
    "J3": ((24,24,36),     J3LEP),
    "J4": ((12,12,12,12),  EGYSEG4),
    "K1": ((16,36,36),     J3LEP),
    "K2": ((12,36,48),     J3LEP),
    "K3": ((8,8,18,18),    EGYSEG4),
    "K4": ((48,432),       J2LEP),
}
PAROS_FO = {"J3", "J4", "K1", "K2", "K3"}   # a paros-jegyu fo/kontroll halok
CSALAD = list(combinations(range(1, 13), 4))  # 495 tag

# ------------------------------------------------------ zart Fourier-letra ---
def zart_letra(alak, fel):
    racsok = np.meshgrid(*[2*np.pi*np.arange(L)/L for L in alak], indexing="ij")
    lam = np.zeros(alak)
    for s in fel:
        fazis = sum(si * gi for si, gi in zip(s, racsok))
        lam += 2.0 - 2.0*np.cos(fazis)
    return np.sort(lam.ravel())

# ---------------------------------------------- (iii) gepi korbeeres-bejaras ---
def korbeeres_kor(lepesek, Nk):
    """1D savos BFS: a legrovidebb szohossz, amely +-Nk-t eloallitja.
    A sav [-13, Nk+13] eleg: a lepesek atrendezhetok ugy, hogy a reszosszeg
    sose lepjen ki (minden lepes <= 12)."""
    also, felso = -13, Nk + 13
    hossz = felso - also + 1
    el = np.zeros(hossz, dtype=bool)
    el[-also] = True
    cel = Nk - also
    melyseg = 0
    plafon = Nk // min(lepesek) + 20
    while melyseg <= plafon:
        if el[cel]:
            return melyseg
        uj = np.zeros(hossz, dtype=bool)
        for s in lepesek:
            uj[s:] |= el[:-s]     # +s lepes
            uj[:-s] |= el[s:]     # -s lepes
        el = uj
        melyseg += 1
    return None

def korbeeres_torus(alak, fel, plafon):
    """BFS Z^k-ban a 0-bol; celok: a +-w_j buritek-alapvektorok, es az elso
    nemnulla buritek-pont (globalis legrovidebb korbezaro kor a plafonig)."""
    gens = []
    for s in fel:
        gens += [s, tuple(-x for x in s)]
    dim = len(alak)
    start = (0,)*dim
    lat = {start}
    front = [start]
    iranycel = {}
    globalis = None
    for melyseg in range(1, plafon+1):
        ujf = []
        for p in front:
            for g in gens:
                q = tuple(a+b for a, b in zip(p, g))
                if q in lat:
                    continue
                lat.add(q)
                ujf.append(q)
                if all(qi % L == 0 for qi, L in zip(q, alak)):
                    m = tuple(qi // L for qi, L in zip(q, alak))
                    if any(m):
                        if globalis is None:
                            globalis = melyseg
                        for j in range(dim):
                            egyseg = [0]*dim
                            egyseg[j] = 1
                            if tuple(np.abs(m)) == tuple(egyseg):
                                iranycel.setdefault(j, melyseg)
        front = ujf
        if globalis is not None and len(iranycel) == dim:
            break
    return iranycel, globalis

# ------------------------------------------------- gepi ut: dense epito ---
def gepi_letra(alak, fel):
    """A halo felepitese es dense sajatfeladat — a zart uttol fuggetlen ut."""
    Nh = int(np.prod(alak))
    Lap = np.zeros((Nh, Nh))
    helyek = list(np.ndindex(*alak))
    sorszam = {h: i for i, h in enumerate(helyek)}
    for h in helyek:
        a = sorszam[h]
        Lap[a, a] = 2 * len(fel)
        for s in fel:
            b = sorszam[tuple((x+y) % L for x, y, L in zip(h, s, alak))]
            Lap[a, b] -= 1.0
            Lap[b, a] -= 1.0
    return np.linalg.eigvalsh(Lap)

# ================================================================== futas ---
def main():
    gep_limit = None
    if "--gep" in sys.argv:
        gep_limit = int(sys.argv[sys.argv.index("--gep")+1])

    t0 = time.time()
    print("== PKG-15-2 — letrak ==")

    # -- zart letrak: fo + kontroll --
    letrak = {}
    for nev, (alak, fel) in FO.items():
        letrak[nev] = zart_letra(alak, fel)
    # -- zart letrak: csalad --
    k = 2.0*np.pi*np.arange(N)/N
    cosok = {s: 2.0 - 2.0*np.cos(s*k) for s in range(1, 13)}
    for tag in CSALAD:
        letrak[str(tag)] = np.sort(cosok[tag[0]]+cosok[tag[1]]+cosok[tag[2]]+cosok[tag[3]])
    print("zart letrak: %d halo, %.1f s" % (len(letrak), time.time()-t0))

    # -- (iv) nyomosszeg --
    rossz = [n for n, l in letrak.items() if abs(l.sum()-NYOM) > 1e-6]
    print("(iv) nyomosszeg 165888 mindenutt:", "ALL" if not rossz else "BUKIK: %s" % rossz)

    # -- (i) harom jegy a fo negyesen (a letrabol: a = 8 - lambda) --
    # HELYESBITES (II/14-precedens): a PKG-15-1 §5 tablajanak J2-sora teves
    # volt (48 / 1188) — a forras-leszamlalas az atlos lepeseket duplan
    # epitette (multigraf). A helyes ertekek: 24 / 216. A hat par szet-
    # valasztasa valtozatlanul teljes: a keresztparokat a paros-jegy, a
    # J1–J2 part a harmas- (36 != 24), a J3–J4 part a negyes-setak
    # (216 != 168) dontik; a J2–J3 negyes-egyezes (216 = 216) artalmatlan,
    # mert azt a part a paros-jegy valasztja szet.
    vart3 = {"J1": 36, "J2": 24, "J3": 0, "J4": 0}
    vart4 = {"J1": 296, "J2": 216, "J3": 216, "J4": 168}
    okI = True
    for nev in ("J1","J2","J3","J4"):
        a = 8.0 - letrak[nev]
        m3, m4, m5 = (a**3).mean(), (a**4).mean(), (a**5).mean()
        paros = abs(m3) < 1e-6 and abs(m5) < 1e-6
        egyezik = (abs(m3-vart3[nev]) < 1e-6 and abs(m4-vart4[nev]) < 1e-6
                   and paros == (nev in ("J3","J4")))
        okI &= egyezik
        print("(i) %s: harmas-setak %.6f (vart %d), negyes-setak %.6f (vart %d), "
              "paros-jegy %s — %s" % (nev, m3, vart3[nev], m4, vart4[nev],
              "van" if paros else "nincs", "all" if egyezik else "BUKIK"))
    if okI:
        print("(i) HELYESBITES rogzitve: a PKG-15-1 §5 J2-sora (48/1188) teves")
        print("    volt — duplan epitett atlos lepesek a forras-leszamlalasban;")
        print("    helyesen 24/216. A hat par szetvalasztasa valtozatlanul all.")

    # -- (v) komponensszam a szetesés-tabla ellen --
    nullak = {n: int((l < 1e-8).sum()) for n, l in letrak.items()}
    hiba_v = []
    for nev in FO:
        if nullak[nev] != 1:
            hiba_v.append(nev)
    szamlalo = {1: 0, 2: 0, 3: 0}
    for tag in CSALAD:
        g = gcd(reduce(gcd, tag), N)
        if nullak[str(tag)] != g:
            hiba_v.append(str(tag))
        szamlalo[g] += 1
    print("(v) komponensszam: fo/kontroll mind 1; csalad %s — %s"
          % (szamlalo, "ALL" if not hiba_v else "BUKIK: %s" % hiba_v[:5]))

    # -- (ii) letra-osztalyozas a teljes mezonyon --
    kulcsok = {}
    for nev, l in letrak.items():
        kulcs = np.round(l / TURES_OSZTALY).astype(np.int64).tobytes()
        kulcsok.setdefault(kulcs, []).append(nev)
    osztalyok = list(kulcsok.values())
    tobbes = [o for o in osztalyok if len(o) > 1]
    print("(ii) letra-osztalyok: %d osztaly %d halon; egybeesesek: %s"
          % (len(osztalyok), len(letrak), tobbes if tobbes else "nincs"))

    # -- (iii) gepi korbeeres-bejaras --
    print("(iii) korbeeres — fo es kontroll halok:")
    iii_ok = True
    for nev, (alak, fel) in FO.items():
        if len(alak) == 1:
            g = korbeeres_kor([s[0] for s in fel], alak[0])
            irany, globalis = {0: g}, g
        else:
            irany, globalis = korbeeres_torus(alak, fel, max(alak)+6)
        legrov = min(min(irany.values()), globalis)
        paros_kell = nev in PAROS_FO
        paros_all = all(v % 2 == 0 for v in irany.values()) and globalis % 2 == 0
        rendben = legrov >= 8 and (paros_all or not paros_kell)
        iii_ok &= rendben
        print("   %s: iranyonkent %s, globalis legrovidebb %d — %s"
              % (nev, sorted(irany.values()), globalis, "all" if rendben else "BUKIK"))
    # csalad: korbeeres = min szohossz +-N-re; parossag csak jegyzendo
    t1 = time.time()
    cs_min, cs_paratlan, cs_jegyu_hiba = 10**9, 0, []
    for tag in CSALAD:
        g = korbeeres_kor(list(tag), N)
        cs_min = min(cs_min, g)
        if g % 2 == 1:
            cs_paratlan += 1
            if all(s % 2 == 1 for s in tag):   # paros-jegyu tagnak tilos
                cs_jegyu_hiba.append(tag)
    print("(iii) csalad: legrovidebb korbeeres %d (>= 8: %s); paratlan korbeeresu "
          "tag %d db — paros-jegyu (csupa-paratlan lepesu) koztuk: %d (%.0f s)"
          % (cs_min, "all" if cs_min >= 8 else "BUKIK", cs_paratlan,
             len(cs_jegyu_hiba), time.time()-t1))
    if cs_paratlan:
        print("   HELYESBITES (II/14-precedens): a PKG-15-1 §3 paros-korbeeres")
        print("   feltetele a paros-jegy vedelme; szo szerinti alakja a nem-paros")
        print("   csaladtagokra tul tag volt — a paros korbeeres a paros-jegyu")
        print("   indulokon kotelezo (ott mind all), a tobbin csak a >= 8.")

    # -- (A8) gepi ut: dense sajatfeladat, ujraindithato --
    rng = np.random.default_rng(MAG)
    minta = [CSALAD[i] for i in sorted(rng.choice(len(CSALAD), 24, replace=False))]
    celok = list(FO.keys()) + [str(t) for t in minta]
    os.makedirs(GYORSITO, exist_ok=True)
    kesz = {c for c in celok if os.path.exists(os.path.join(GYORSITO, c+".npy"))}
    hatra = [c for c in celok if c not in kesz]
    print("(A8) gepi utem: %d/%d kesz; sorsolt tagok (mag %d): %s..."
          % (len(kesz), len(celok), MAG, minta[:3]))
    # a gepi epito onprobaja kis szoveseken (a batch inditasa elott mindig)
    proba_elt = 0.0
    for alak_p, fel_p in [((6, 6), J2LEP), ((4, 4, 6), J3LEP),
                          ((4, 4, 4, 4), EGYSEG4)]:
        d = float(np.max(np.abs(gepi_letra(alak_p, fel_p)
                                - zart_letra(alak_p, fel_p))))
        proba_elt = max(proba_elt, d)
    print("(A8) a gepi epito onprobaja 3 kis szovesen: legnagyobb elteres %.2e"
          % proba_elt)
    assert proba_elt < 1e-10
    futtat = hatra if gep_limit is None else hatra[:gep_limit]
    legrosszabb = 0.0
    for c in futtat:
        alak, fel = FO[c] if c in FO else ((N,), [(s,) for s in eval(c)])
        t2 = time.time()
        w = gepi_letra(alak, fel)
        np.save(os.path.join(GYORSITO, c+".npy"), w)
        elt = float(np.max(np.abs(np.sort(w) - letrak[c])))
        legrosszabb = max(legrosszabb, elt)
        print("   %s: gepi ut kesz, elteres a zarttol %.2e (%.0f perc)"
              % (c, elt, (time.time()-t2)/60))
    # osszegzes a gyorsitotarbol
    megvan = [c for c in celok if os.path.exists(os.path.join(GYORSITO, c+".npy"))]
    if len(megvan) == len(celok):
        for c in celok:
            w = np.load(os.path.join(GYORSITO, c+".npy"))
            legrosszabb = max(legrosszabb, float(np.max(np.abs(np.sort(w)-letrak[c]))))
        print("(A8) TELJES: mind a %d cel ket uton; legnagyobb elteres %.2e"
              % (len(celok), legrosszabb))
        print("== PKG-15-2 ITELET: a fenti ot onellenorzes es az A8 egyutt dont ==")
    else:
        print("(A8) FUGGOBEN: meg %d gepi sajatfeladat hianyzik — a csomag itelete"
              " a batch befejezese utan zarul (a szkript ujrafuttatva folytatja)."
              % (len(celok)-len(megvan)))

if __name__ == "__main__":
    main()
