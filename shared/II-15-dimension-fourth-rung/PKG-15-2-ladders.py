# PKG-15-2 — Beat ladders (II/15)
# Builds on the outgoing claims of PKG-15-1 (A1-A8). Its business:
#   1) building the field: J1-J4, K1-K4, and all 495 members of the line family
#   2) the ladder by the closed Fourier route on all 503 networks
#   3) self-checks (A7): (i) three distinctness marks on the main four;
#      (ii) ladder classification over the full field with a fixed tolerance;
#      (iii) machine wrap-around traversal on every entrant; (iv) trace sum 165888;
#      (v) component count against the disconnection table
#   4) machine route (A8): dense eigenproblem on the 8 main/control networks +
#      24 drawn family members (seed: 20736); restartable — finished networks
#      are skipped. Memory need ~8 GB per network; runtime ~15-20 min/network.
# Usage:  python3 PKG-15-2-ladders.py [--gep N]
#   --gep N : run at most N machine eigenproblems in this run
#             (default: all remaining). --gep 0 runs only the fast part;
#             the batch can be continued later.

import numpy as np
import os, sys, time
from itertools import combinations, product
from collections import deque
from math import gcd
from functools import reduce

N = 20736
NYOM = 2 * 4 * N            # 165888 — the cover of the trace tie
TURES_OSZTALY = 1e-8        # ladder classification quantum (fixed)
MAG = 20736                 # random seed (fixed; numpy PCG64)
GYORSITO = "letrak_gepi"    # cache of the machine leg (for restarting)

# ----------------------------------------------------------------- field ---
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

FO = {  # name -> (shape, half-steps); the full step set arises with the +- pairs
    "J1": ((N,),           [(1,),(2,),(3,),(4,)]),
    "J2": ((144,144),      J2LEP),
    "J3": ((24,24,36),     J3LEP),
    "J4": ((12,12,12,12),  EGYSEG4),
    "K1": ((16,36,36),     J3LEP),
    "K2": ((12,36,48),     J3LEP),
    "K3": ((8,8,18,18),    EGYSEG4),
    "K4": ((48,432),       J2LEP),
}
PAROS_FO = {"J3", "J4", "K1", "K2", "K3"}   # the main/control networks carrying the bipartite mark
CSALAD = list(combinations(range(1, 13), 4))  # 495 members

# -------------------------------------------------- closed Fourier ladder ---
def zart_letra(alak, fel):
    racsok = np.meshgrid(*[2*np.pi*np.arange(L)/L for L in alak], indexing="ij")
    lam = np.zeros(alak)
    for s in fel:
        fazis = sum(si * gi for si, gi in zip(s, racsok))
        lam += 2.0 - 2.0*np.cos(fazis)
    return np.sort(lam.ravel())

# ------------------------------------- (iii) machine wrap-around traversal ---
def korbeeres_kor(lepesek, Nk):
    """1D banded BFS: the shortest word length producing +-Nk.
    The band [-13, Nk+13] is enough: the steps can be rearranged so that the
    partial sum never leaves it (every step <= 12)."""
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
            uj[s:] |= el[:-s]     # +s step
            uj[:-s] |= el[s:]     # -s step
        el = uj
        melyseg += 1
    return None

def korbeeres_torus(alak, fel, plafon):
    """BFS in Z^k from 0; targets: the +-w_j envelope basis vectors, and the first
    nonzero envelope point (the globally shortest wrapping loop up to the ceiling)."""
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

# ---------------------------------------------- machine route: dense builder ---
def gepi_letra(alak, fel):
    """Building the network and a dense eigenproblem — a route independent of the closed one."""
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

# =================================================================== run ---
def main():
    gep_limit = None
    if "--gep" in sys.argv:
        gep_limit = int(sys.argv[sys.argv.index("--gep")+1])

    t0 = time.time()
    print("== PKG-15-2 — ladders ==")

    # -- closed ladders: main + control --
    letrak = {}
    for nev, (alak, fel) in FO.items():
        letrak[nev] = zart_letra(alak, fel)
    # -- closed ladders: family --
    k = 2.0*np.pi*np.arange(N)/N
    cosok = {s: 2.0 - 2.0*np.cos(s*k) for s in range(1, 13)}
    for tag in CSALAD:
        letrak[str(tag)] = np.sort(cosok[tag[0]]+cosok[tag[1]]+cosok[tag[2]]+cosok[tag[3]])
    print("closed ladders: %d networks, %.1f s" % (len(letrak), time.time()-t0))

    # -- (iv) trace sum --
    rossz = [n for n, l in letrak.items() if abs(l.sum()-NYOM) > 1e-6]
    print("(iv) trace sum 165888 everywhere:", "HOLDS" if not rossz else "FAILS: %s" % rossz)

    # -- (i) three marks on the main four (from the ladder: a = 8 - lambda) --
    # CORRECTION (the II/14 precedent): the J2 row of the table of PKG-15-1 §5
    # was wrong (48 / 1188) — the source enumeration built the diagonal steps
    # twice (a multigraph). The correct values are 24 / 216. The separation of
    # the six pairs is complete as before: the cross pairs are decided by the
    # bipartite mark, the J1-J2 pair by the 3-walks (36 != 24), and the J3-J4
    # pair by the 4-walks (216 != 168); the J2-J3 4-walk agreement (216 = 216)
    # is harmless, because that pair is separated by the bipartite mark.
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
        print("(i) %s: 3-walks %.6f (expected %d), 4-walks %.6f (expected %d), "
              "bipartite mark %s — %s" % (nev, m3, vart3[nev], m4, vart4[nev],
              "present" if paros else "none", "holds" if egyezik else "FAILS"))
    if okI:
        print("(i) CORRECTION recorded: the J2 row of PKG-15-1 §5 (48/1188) was")
        print("    wrong — diagonal steps built twice in the source enumeration;")
        print("    correctly 24/216. The separation of the six pairs still holds.")

    # -- (v) component count against the disconnection table --
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
    print("(v) component count: main/control all 1; family %s — %s"
          % (szamlalo, "HOLDS" if not hiba_v else "FAILS: %s" % hiba_v[:5]))

    # -- (ii) ladder classification over the full field --
    kulcsok = {}
    for nev, l in letrak.items():
        kulcs = np.round(l / TURES_OSZTALY).astype(np.int64).tobytes()
        kulcsok.setdefault(kulcs, []).append(nev)
    osztalyok = list(kulcsok.values())
    tobbes = [o for o in osztalyok if len(o) > 1]
    print("(ii) ladder classes: %d classes on %d networks; coincidences: %s"
          % (len(osztalyok), len(letrak), tobbes if tobbes else "none"))

    # -- (iii) machine wrap-around traversal --
    print("(iii) wrap-around — main and control networks:")
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
        print("   %s: per direction %s, global shortest %d — %s"
              % (nev, sorted(irany.values()), globalis, "holds" if rendben else "FAILS"))
    # family: wrap-around = min word length for +-N; parity only to be noted
    t1 = time.time()
    cs_min, cs_paratlan, cs_jegyu_hiba = 10**9, 0, []
    for tag in CSALAD:
        g = korbeeres_kor(list(tag), N)
        cs_min = min(cs_min, g)
        if g % 2 == 1:
            cs_paratlan += 1
            if all(s % 2 == 1 for s in tag):   # forbidden for a bipartite member
                cs_jegyu_hiba.append(tag)
    print("(iii) family: shortest wrap-around %d (>= 8: %s); members with odd "
          "wrap-around %d — bipartite (all-odd-step) among them: %d (%.0f s)"
          % (cs_min, "holds" if cs_min >= 8 else "FAILS", cs_paratlan,
             len(cs_jegyu_hiba), time.time()-t1))
    if cs_paratlan:
        print("   CORRECTION (the II/14 precedent): the even-wrap-around condition")
        print("   of PKG-15-1 §3 protects the bipartite mark; its literal form was")
        print("   too broad for the non-bipartite family members — it is obligatory")
        print("   on the bipartite entrants (all hold), on the rest only the >= 8.")

    # -- (A8) machine route: dense eigenproblem, restartable --
    rng = np.random.default_rng(MAG)
    minta = [CSALAD[i] for i in sorted(rng.choice(len(CSALAD), 24, replace=False))]
    celok = list(FO.keys()) + [str(t) for t in minta]
    os.makedirs(GYORSITO, exist_ok=True)
    kesz = {c for c in celok if os.path.exists(os.path.join(GYORSITO, c+".npy"))}
    hatra = [c for c in celok if c not in kesz]
    print("(A8) machine leg: %d/%d done; drawn members (seed %d): %s..."
          % (len(kesz), len(celok), MAG, minta[:3]))
    # self-test of the machine builder on small weaves (always before starting the batch)
    proba_elt = 0.0
    for alak_p, fel_p in [((6, 6), J2LEP), ((4, 4, 6), J3LEP),
                          ((4, 4, 4, 4), EGYSEG4)]:
        d = float(np.max(np.abs(gepi_letra(alak_p, fel_p)
                                - zart_letra(alak_p, fel_p))))
        proba_elt = max(proba_elt, d)
    print("(A8) self-test of the machine builder on 3 small weaves: largest deviation %.2e"
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
        print("   %s: machine route done, deviation from the closed one %.2e (%.0f min)"
              % (c, elt, (time.time()-t2)/60))
    # summary from the cache
    megvan = [c for c in celok if os.path.exists(os.path.join(GYORSITO, c+".npy"))]
    if len(megvan) == len(celok):
        for c in celok:
            w = np.load(os.path.join(GYORSITO, c+".npy"))
            legrosszabb = max(legrosszabb, float(np.max(np.abs(np.sort(w)-letrak[c]))))
        print("(A8) COMPLETE: all %d targets by two routes; largest deviation %.2e"
              % (len(celok), legrosszabb))
        print("== PKG-15-2 VERDICT: the five self-checks above and A8 together decide ==")
    else:
        print("(A8) PENDING: %d machine eigenproblems are still missing — the verdict"
              " of the package closes after the batch finishes (re-running the"
              " script continues it)." % (len(celok)-len(megvan)))

if __name__ == "__main__":
    main()
