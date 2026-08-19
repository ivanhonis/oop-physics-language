# PKG-16-2 — Beat ladders (II/16)
# Builds on claims A1-A8 of PKG-16-1. 805 entrants (5 main + 8 controls +
# 792 family), streamed processing (the full ladder matrix does not fit in memory).
# Self-checks (A7): mark table by two routes | ladder classification (by digests) |
#   machine wrap-around on every entrant | trace sum 2488320 | component count |
#   wiring-uniqueness assertion.
# Two-route form (A8): (i) sparse residual check (64/16 modes, seed 248832)
#   (ii) moment cover of order<=4 everywhere (iii) dense certification on small
#   instances (iv) the projector seal runs in PKG-16-4.

import numpy as np, hashlib, time
from itertools import combinations, product
from math import gcd
from functools import reduce

NH = 12**5
NYOM = 2 * 5 * NH          # 2,488,320
TURES = 1e-8
MAG = 248832

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
CSALAD = list(combinations(range(1, 13), 5))
KIS = {"J1": (60,), "J2": (12,12), "J3": (12,12,12), "J4": (6,6,6,6),
       "J5": (6,)*5, "K1": (12,12,12), "K2": (6,6,6,6), "K3": (12,12),
       "KA2": (12,12), "KA3": (12,12,12), "KA4": (6,6,6,6),
       "KP3": (6,6,6), "KP4": (6,6,6,6)}

def pm(fel):
    g = list(fel) + [tuple(-x for x in s) for s in fel]
    assert len(set(g)) == 10, "duplicated wiring"      # rule H1
    return g

def zart_letra(alak, fel, dt=np.longdouble):
    r = np.meshgrid(*[(2*np.pi*np.arange(L)).astype(dt)/L for L in alak],
                    indexing="ij")
    lam = np.zeros(alak, dtype=dt)
    for s in fel:
        lam += 2.0 - 2.0*np.cos(sum(si*gi for si, gi in zip(s, r)))
    return np.sort(lam.ravel())

def setak_nd(fel, h):
    g = pm(fel)
    return sum(1 for t in product(g, repeat=h)
               if all(x == 0 for x in map(sum, zip(*t))))

def setak_1d(lepesek, h):
    p = np.zeros(25); p[12] = 1.0
    e = np.zeros(25)
    for s in lepesek:
        e[12+s] += 1; e[12-s] += 1
    for _ in range(h):
        p = np.convolve(p, e)
    return int(round(p[len(p)//2]))

def korbeeres_kor(lepesek, cel):
    """Minimum word length producing the target; the non-maximal coefficients
    are bounded by an exchange argument to < 12."""
    e = lepesek[-1]
    tobbi = np.array(lepesek[:-1])
    racs = np.array(np.meshgrid(*[np.arange(-11, 12)]*len(tobbi),
                                indexing="ij")).reshape(len(tobbi), -1)
    osszeg = tobbi @ racs
    maradek = cel - osszeg
    jo = maradek % e == 0
    teljes = np.abs(racs).sum(axis=0) + np.abs(maradek // e)
    return int(teljes[jo].min())

def korbeeres_torus(alak, fel, plafon):
    gens = np.array(pm(fel))
    dim = len(alak)
    OFF = 2*plafon + 4
    bazis = OFF**np.arange(dim)
    front = np.zeros((1, dim), dtype=np.int64)
    lat = {0}
    iranyok, globalis = {}, None
    for m in range(1, plafon+1):
        uj = (front[:, None, :] + gens[None, :, :]).reshape(-1, dim)
        kulcs = uj @ bazis
        _, idx = np.unique(kulcs, return_index=True)
        uj = uj[idx]
        szur = [k not in lat for k in (uj @ bazis)]
        uj = uj[szur]
        for k in (uj @ bazis):
            lat.add(int(k))
        rac = uj % np.array(alak)
        talalt = np.all(rac == 0, axis=1)
        for p in uj[talalt]:
            mm = p // np.array(alak)
            if np.any(mm):
                if globalis is None:
                    globalis = m
                nz = np.nonzero(mm)[0]
                if len(nz) == 1:
                    iranyok.setdefault(int(nz[0]), m)
        front = uj
        if globalis is not None and len(iranyok) == dim:
            break
    return iranyok, globalis

def main():
    t0 = time.time()
    print("== PKG-16-2 — ladders (805 entrants, streamed) ==")
    kivonat, nyomhiba, nullak = {}, 0.0, {}
    mom_hiba = 0.0
    for nev, (alak, fel) in FO.items():
        lam = zart_letra(alak, fel)
        nyomhiba = max(nyomhiba, abs(float(lam.sum()) - NYOM))
        nullak[nev] = int((lam < TURES).sum())
        a = 10.0 - lam
        m3, m4 = float((a**3).mean()), float((a**4).mean())
        k3, k4 = setak_nd(fel, 3), setak_nd(fel, 4)
        mom_hiba = max(mom_hiba, abs(m3-k3), abs(m4-k4))
        kul = hashlib.md5(np.round(lam.astype(np.float64)/TURES)
                          .astype(np.int64).tobytes()).hexdigest()
        kivonat.setdefault(kul, []).append(nev)
    kk = (2*np.pi*np.arange(NH)).astype(np.longdouble)/NH
    cos_tar = {s: 2.0-2.0*np.cos(s*kk) for s in range(1, 13)}
    for tag in CSALAD:
        lam = np.sort(sum(cos_tar[s] for s in tag))
        nyomhiba = max(nyomhiba, abs(float(lam.sum()) - NYOM))
        nullak[str(tag)] = int((lam < TURES).sum())
        a = 10.0 - lam
        m3, m4 = float((a**3).mean()), float((a**4).mean())
        mom_hiba = max(mom_hiba, abs(m3-setak_1d(tag,3)), abs(m4-setak_1d(tag,4)))
        kul = hashlib.md5(np.round(lam.astype(np.float64)/TURES)
                          .astype(np.int64).tobytes()).hexdigest()
        kivonat.setdefault(kul, []).append(str(tag))
    print("ladders + moment cover (order<=4, on all 805): largest "
          "deviation %.2e; trace-sum error %.2e  (%.0f s)"
          % (mom_hiba, nyomhiba, time.time()-t0))

    # component count against the disconnection table
    hiba = [n for n in FO if nullak[n] != 1]
    for tag in CSALAD:
        g = gcd(reduce(gcd, tag), NH)
        if nullak[str(tag)] != g:
            hiba.append(str(tag))
    print("component count: %s" % ("HOLDS" if not hiba else "FAILS: %s" % hiba[:5]))

    tobbes = [o for o in kivonat.values() if len(o) > 1]
    print("ladder classes: %d classes on %d entrants; coincidences: %s"
          % (len(kivonat), 13+len(CSALAD), tobbes if tobbes else "none"))

    # machine wrap-around
    t1 = time.time()
    print("wrap-around — the named networks (per direction | global):")
    for nev, (alak, fel) in FO.items():
        if len(alak) == 1:
            g = korbeeres_kor([1,2,3,4,5], NH)
            print("   %-4s [%d] | %d" % (nev, g, g))
        else:
            ir, gl = korbeeres_torus(alak, fel, max(alak)+4)
            print("   %-4s %s | %d — %s" % (nev, sorted(ir.values()), gl,
                  "holds" if gl >= 8 else "FAILS"))
    cs_min = min(korbeeres_kor(list(t), NH) if gcd(reduce(gcd,t),NH) == 1
                 else korbeeres_kor([s//2 for s in t], NH//2)
                 for t in CSALAD)
    print("wrap-around — family: the shortest is %d (measured on the copy for the "
          "disconnected ones) — %s (%.0f s)"
          % (cs_min, "holds" if cs_min >= 8 else "FAILS", time.time()-t1))

    # (i) sparse residual check
    t2 = time.time()
    rng = np.random.default_rng(MAG)
    minta = [CSALAD[i] for i in sorted(rng.choice(len(CSALAD), 24, replace=False))]
    legmaradek = 0.0
    for nev, (alak, fel) in FO.items():
        Nn = int(np.prod(alak))
        koord = np.array(np.unravel_index(np.arange(Nn), alak)).T
        # the neighbour indices are the same for every mode — built once
        idxek = [np.ravel_multi_index(((koord + s) % np.array(alak)).T, alak)
                 for s in pm(fel)]
        for _ in range(64):
            n = np.array([rng.integers(0, L) for L in alak])
            # exact phase: integer remainder per axis, only then floating point
            ph = sum(((n[j]*koord[:, j]) % alak[j]) / alak[j]
                     for j in range(len(alak)))
            v = np.exp(2j*np.pi*ph)
            Av = np.zeros(Nn, dtype=complex)
            for ix in idxek:
                Av += v[ix]
            # the correct beat formula: the phase is the product with the wiring vector
            lj = float(sum(2-2*np.cos(2*np.pi*sum(ni*si/L for ni, si, L
                       in zip(n, s, alak))) for s in fel))
            legmaradek = max(legmaradek,
                             float(np.max(np.abs(10*v - Av - lj*v))))
    x = np.arange(NH)
    for tag in minta:
        idxek = [(x + s) % NH for s in list(tag)+[-s for s in tag]]
        for _ in range(16):
            n = int(rng.integers(0, NH))
            v = np.exp(2j*np.pi*((n*x) % NH)/NH)
            Av = np.zeros(NH, dtype=complex)
            for ix in idxek:
                Av += v[ix]
            lj = float(sum(2-2*np.cos(2*np.pi*n*s/NH) for s in tag))
            legmaradek = max(legmaradek,
                             float(np.max(np.abs(10*v - Av - lj*v))))
    print("(i) sparse residual check (13x64 + 24x16 modes, seed %d): "
          "largest residual %.2e  (%.0f s)"
          % (MAG, legmaradek, time.time()-t2))

    # (iii) dense certification on small instances
    t3 = time.time()
    legkis = 0.0
    for nev, alak in KIS.items():
        fel = FO[nev][1]
        Nk = int(np.prod(alak))
        koord = np.array(np.unravel_index(np.arange(Nk), alak)).T
        Lap = np.zeros((Nk, Nk))
        Lap[np.arange(Nk), np.arange(Nk)] = 10.0
        for s in pm(fel):
            cel = np.ravel_multi_index(((koord + s) % np.array(alak)).T, alak)
            Lap[np.arange(Nk), cel] -= 1.0
        w = np.linalg.eigvalsh(Lap)
        legkis = max(legkis, float(np.max(np.abs(
            np.sort(w) - zart_letra(alak, fel, np.float64)))))
    print("(iii) dense certification on small instances (13 patterns): largest "
          "deviation %.2e  (%.0f s)" % (legkis, time.time()-t3))
    print("TOTAL: %.0f s" % (time.time()-t0))

if __name__ == "__main__":
    main()
