# PKG-15-4 — A kiolvasas (II/15)
# Rendszer (PKG-15-3, V6): J4 hiperkocka-szoves 12x12x12x12, 82944 szerzodes;
# toltes: N = 11075 zart fok (a folotte levo res elore ismert erteke 2 - sqrt(3)).
# Jegyzokonyv a PKG-15-1 §8 szerint, itelet-feltetelek elore:
#   A1 a zart fok all (res = 2 - sqrt(3));
#   A2 teljesseg-szamla 82944/82944, nulla fantom, nulla hianyzo;
#   A3 a golyo r <= 3-ig egzakt a koebos hivatkozasi soron (jelentes r <= 5-ig,
#      ervenyesseg 2r < 12);
#   A4 sav-orszem >= 2 (a legrosszabb helyi ertek).
# Kotelezo kulon sor: az atellenes osztaly elojeles korrelacioja (paros gyoztes).
# Ketutas szabaly: zart (FFT) ut + gepi vetito-ellenorzes (dense sajatfeladat
# sajatvektorokkal). A gepi resz igenye: ~10-11 GB memoria, ~20-40 perc.
# Hasznalat:
#   python3 PKG-15-4-readout.py            # minden (zart ut + gepi ellenorzes)
#   python3 PKG-15-4-readout.py --gep 0    # csak a zart ut (gyors)

import numpy as np
import sys, time
from itertools import product

L, DIM = 12, 4
NSITE = L**DIM              # 20736
NTOLT = 11075               # zart fok (PKG-15-3, V6)
NCONTRACT = 4 * NSITE       # 82944
RES_VART = 2.0 - np.sqrt(3.0)
ABLAK = 30                  # rogzitett keresesi ablak (PKG-15-1 §8)

def canon(d):
    return tuple(sorted(int(min(x % L, (-x) % L)) for x in d))

def main():
    gep = 1
    if "--gep" in sys.argv:
        gep = int(sys.argv[sys.argv.index("--gep")+1])
    print("== PKG-15-4 — a kiolvasas (J4, N = %d) ==" % NTOLT)

    # --- 1) letra es zart fok ---
    k = 2*np.pi*np.arange(L)/L
    egy = 2.0 - 2.0*np.cos(k)
    lam = (egy[:,None,None,None] + egy[None,:,None,None]
           + egy[None,None,:,None] + egy[None,None,None,:])
    lam_flat = np.sort(lam.ravel())
    res = lam_flat[NTOLT] - lam_flat[NTOLT-1]
    A1 = abs(res - RES_VART) < 1e-9
    print("zart fok: res a %d. fok folott %.9f (vart 2-sqrt3 = %.9f) — %s"
          % (NTOLT, res, RES_VART, "all" if A1 else "BUKIK"))

    kuszob = lam_flat[NTOLT-1] + 1e-9
    occ = lam <= kuszob
    assert int(occ.sum()) == NTOLT

    # --- 2) kozelseg-terkep zart uton ---
    G = np.fft.ifftn(occ.astype(float))
    assert np.max(np.abs(G.imag)) < 1e-12
    G = G.real

    # eltolas-osztalyok: szoves — osztalyon belul egzakt egyezes
    osztaly = {}
    for d in np.ndindex(L, L, L, L):
        if d == (0,0,0,0):
            continue
        osztaly.setdefault(canon(d), []).append(G[d])
    rossz = max(np.std(v) for v in osztaly.values())
    assert rossz < 1e-12

    szomszed = G[1,0,0,0]
    atellenes = G[L//2, L//2, L//2, L//2]
    print("szomszed-kozelseg G(1,0,0,0) = %+.6f" % szomszed)
    print("ATELLENES VISSZHANG G(6,6,6,6) = %+.6f  (elojel: %s; "
          "|arany a szomszedhoz| = %.4f)  [kotelezo kulon sor]"
          % (atellenes, "negativ" if atellenes < 0 else "pozitiv",
             abs(atellenes)/szomszed))

    # --- 3) elojeles ugras (rogzitett 30-as ablak) ---
    g = G.ravel().copy()
    g[0] = -np.inf
    rend = np.argsort(g)[::-1]
    v = g[rend]
    legjobb, kstar = -1.0, None
    for m in range(1, ABLAK+1):
        if v[m] > 0:
            r = v[m-1]/v[m]
            if r > legjobb:
                legjobb, kstar = r, m
    print("elojeles lista eleje:", np.round(v[:12], 5))
    print("ugras a(z) %d. hely utan: %.5f -> %.5f (%.1f-szeres)"
          % (kstar, v[kstar-1], v[kstar], legjobb))

    maradek = v[kstar:]
    maradek = maradek[np.isfinite(maradek)]
    j = int(np.argmax(np.abs(maradek)))
    d_er = tuple(np.unravel_index(int(rend[kstar+j]), (L,L,L,L)))
    S = v[kstar-1]/abs(float(maradek[j]))
    A4 = S >= 2.0
    print("sav-orszem: S = %.4f (kuszob 2) — %s; legerosebb elutasitott: %s "
          "osztaly, G = %+.6f" % (S, "all" if A4 else "BUKIK",
                                  canon(d_er), float(maradek[j])))

    va = np.sort(np.abs(np.where(np.isfinite(g), g, 0)))[::-1]
    r_abs = va[:ABLAK]/np.maximum(va[1:ABLAK+1], 1e-300)
    k_abs = int(np.argmax(r_abs)) + 1
    print("regi abszolut szabaly (osszevetesul): ugras a(z) %d. hely utan "
          "(%.1f-szeres)" % (k_abs, r_abs[k_abs-1]))

    # --- 4) visszarakas es teljesseg-szamla ---
    elfogadott = [tuple(np.unravel_index(int(i), (L,L,L,L))) for i in rend[:kstar]]
    rc = np.arange(NSITE)
    koord = np.array(np.unravel_index(rc, (L,L,L,L))).T
    def elek(dlista):
        parok = set()
        for d in dlista:
            cel = (koord + d) % L
            b = np.ravel_multi_index(cel.T, (L,L,L,L))
            a2 = np.minimum(rc, b); b2 = np.maximum(rc, b)
            parok |= set(map(int, a2*NSITE + b2))
        return parok
    rec = elek(elfogadott)
    igaz = elek([(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1),
                 (L-1,0,0,0),(0,L-1,0,0),(0,0,L-1,0),(0,0,0,L-1)])
    megvan, fantom, hianyzo = len(rec & igaz), len(rec-igaz), len(igaz-rec)
    A2 = (megvan == NCONTRACT and fantom == 0 and hianyzo == 0)
    print("teljesseg-szamla: megtalalt %d/%d; fantom %d; hianyzo %d — %s"
          % (megvan, NCONTRACT, fantom, hianyzo, "all" if A2 else "BUKIK"))

    # --- 5) golyo-olvasat a visszarakott halon (r <= 5) ---
    lat = {(0,)*DIM}
    front = [(0,)*DIM]
    golyo = [1]
    for r in range(1, 6):
        ujf = []
        for p in front:
            for d in elfogadott:
                q = tuple((x+y) % L for x, y in zip(p, d))
                if q not in lat:
                    lat.add(q)
                    ujf.append(q)
        golyo.append(golyo[-1] + len(ujf))
        front = ujf
    hiv = [1, 9, 41, 129, 321, 681]
    A3 = golyo[:4] == hiv[:4]
    print("golyo (r=0..5): %s — hivatkozas (koebos): %s — r<=3 itelet: %s; "
          "r<=5 jelentes: %s"
          % (golyo, hiv, "all" if A3 else "BUKIK",
             "egyezik" if golyo == hiv else "elter"))

    # --- 6) itelet ---
    print("\nfeltetelek: A1 zart fok %s | A2 teljesseg %s | A3 golyo %s | "
          "A4 orszem %s" % tuple("all" if a else "BUKIK"
                                 for a in (A1, A2, A3, A4)))
    if all((A1, A2, A3, A4)):
        print("ITELET (zart ut): ALL — a gyoztes belulrol negykiterjedesunek"
              " olvassa magat; a ketutas pecsethez a gepi vetito-ellenorzes"
              " hianyzik meg (--gep 1).")
    else:
        print("ITELET: RESZLEGES — a bukott feltetel es a mechanizmus fent;"
              " a folytatas a PKG-15-5 dolga.")

    # --- 7) gepi vetito-ellenorzes (ketutas pecset) ---
    if gep:
        print("\ngepi vetito-ellenorzes: dense sajatfeladat vektorokkal "
              "(~10-11 GB, ~20-40 perc)...")
        t0 = time.time()
        idx = lambda h: int(np.ravel_multi_index(h, (L,)*DIM))
        Lap = np.zeros((NSITE, NSITE))
        for h in np.ndindex(*(L,)*DIM):
            a = idx(h)
            Lap[a, a] = 8.0
            for t in range(DIM):
                for s in (1, -1):
                    q = list(h); q[t] = (q[t]+s) % L
                    b = idx(tuple(q))
                    Lap[a, b] -= 1.0
        w, V = np.linalg.eigh(Lap)
        del Lap
        oszlop = w <= kuszob
        assert int(oszlop.sum()) == NTOLT
        P0 = V[:, oszlop] @ V[0, oszlop]
        G_gepi = np.empty(NSITE)
        for h in np.ndindex(*(L,)*DIM):
            G_gepi[idx(h)] = G[h]
        elt = float(np.max(np.abs(P0 - G_gepi)))
        print("vetito ket uton: legnagyobb elteres = %.2e (%.0f perc) — %s"
              % (elt, (time.time()-t0)/60, "ALL" if elt < 1e-10 else "BUKIK"))
        print("== PKG-15-4 KETUTAS PECSET: %s ==" 
              % ("ALL" if elt < 1e-10 else "BUKIK"))

if __name__ == "__main__":
    main()
