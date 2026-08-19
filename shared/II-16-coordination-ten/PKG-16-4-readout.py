# PKG-16-4 — The readout (II/16)
# System (PKG-16-3, V5): J5 hypercube weave 12^5, 1,244,160 contracts;
# filling: N = 130,902, a closed degree (the expected gap above it is 2 - sqrt(3)).
# Protocol per PKG-16-1 §8; verdict conditions in advance:
#   A1 the closed degree holds; A2 completeness 1244160/1244160, 0 phantom, 0 missing;
#   A3 the ball is exact up to r<=3 on the fourth-order sequence (reporting r<=5, 2r<12);
#   A4 band sentinel >= 2. Obligatory row: the antipodal class (bipartite winner).
# Projector seal (A8/iv, sampling sparse form): 64 filled + 64 empty drawn
# modes (seed 248832) — (a) sparse residual check with the graph-built
# adjacency; (b) the direct (non-FFT) summation transform of the G table
# gives exactly the occupancy indicator at the sample modes.

import numpy as np
import time
from collections import deque

L, DIM = 12, 5
NSITE = L**DIM              # 248832
NTOLT = 130902
NCONTRACT = 5 * NSITE       # 1,244,160
RES_VART = 2.0 - np.sqrt(3.0)
ABLAK = 30
MAG = 248832

def canon(d):
    return tuple(sorted(int(min(x % L, (-x) % L)) for x in d))

def main():
    t0 = time.time()
    print("== PKG-16-4 — the readout (J5, N = %d) ==" % NTOLT)
    k = 2*np.pi*np.arange(L)/L
    egy = 2.0 - 2.0*np.cos(k)
    lam = egy.reshape(-1,1,1,1,1)+egy.reshape(1,-1,1,1,1)+egy.reshape(1,1,-1,1,1)\
        + egy.reshape(1,1,1,-1,1)+egy.reshape(1,1,1,1,-1)
    lam_flat = np.sort(lam.ravel())
    res = lam_flat[NTOLT] - lam_flat[NTOLT-1]
    A1 = abs(res - RES_VART) < 1e-9
    print("closed degree: gap above degree %d is %.9f (expected %.9f) — %s"
          % (NTOLT, res, RES_VART, "holds" if A1 else "FAILS"))
    kuszob = lam_flat[NTOLT-1] + 1e-9
    occ = lam <= kuszob
    assert int(occ.sum()) == NTOLT

    G = np.fft.ifftn(occ.astype(float))
    assert np.max(np.abs(G.imag)) < 1e-12
    G = G.real

    # class exactness (a weave)
    oszt = {}
    Gf = G.ravel()
    koordok = np.array(np.unravel_index(np.arange(NSITE), (L,)*DIM)).T
    for i in range(NSITE):
        if i == 0:
            continue
        oszt.setdefault(canon(koordok[i]), []).append(Gf[i])
    assert max(np.std(v) for v in oszt.values()) < 1e-12

    szomszed = G[1,0,0,0,0]
    atellenes = G[(L//2,)*DIM]
    print("neighbour closeness G(1,0,0,0,0) = %+.6f" % szomszed)
    print("ANTIPODAL ECHO G(6,6,6,6,6) = %+.6f (sign: %s; "
          "|ratio| = %.4f) [obligatory row]"
          % (atellenes, "negative" if atellenes < 0 else "positive",
             abs(atellenes)/szomszed))

    g = Gf.copy(); g[0] = -np.inf
    rend = np.argsort(g)[::-1]
    v = g[rend]
    legjobb, kstar = -1.0, None
    for m in range(1, ABLAK+1):
        if v[m] > 0:
            r = v[m-1]/v[m]
            if r > legjobb:
                legjobb, kstar = r, m
    print("start of the signed list:", np.round(v[:14], 5))
    print("jump after place %d: %.5f -> %.5f (%.1f-fold)"
          % (kstar, v[kstar-1], v[kstar], legjobb))
    maradek = v[kstar:]; maradek = maradek[np.isfinite(maradek)]
    j = int(np.argmax(np.abs(maradek)))
    d_er = tuple(koordok[rend[kstar+j]])
    S = v[kstar-1]/abs(float(maradek[j]))
    A4 = S >= 2.0
    print("band sentinel: S = %.4f (threshold 2) — %s; strongest rejected: "
          "class %s, G = %+.6f"
          % (S, "holds" if A4 else "FAILS", canon(d_er), float(maradek[j])))
    va = np.sort(np.abs(np.where(np.isfinite(g), g, 0)))[::-1]
    r_abs = va[:ABLAK]/np.maximum(va[1:ABLAK+1], 1e-300)
    k_abs = int(np.argmax(r_abs)) + 1
    print("old absolute rule: jump after place %d (%.1f-fold)"
          % (k_abs, r_abs[k_abs-1]))

    # rebuilding + completeness
    elf = [tuple(koordok[i]) for i in rend[:kstar]]
    rc = np.arange(NSITE)
    def elek(dl):
        parok = set()
        for d in dl:
            cel = (koordok + d) % L
            b = np.ravel_multi_index(cel.T, (L,)*DIM)
            parok |= set(map(int, np.minimum(rc, b)*NSITE + np.maximum(rc, b)))
        return parok
    rec = elek(elf)
    igazd = []
    for t in range(DIM):
        for sgn in (1, -1):
            d = [0]*DIM; d[t] = sgn % L
            igazd.append(tuple(x % L for x in d))
    igaz = elek(igazd)
    megvan, fantom, hianyzo = len(rec & igaz), len(rec-igaz), len(igaz-rec)
    A2 = (megvan == NCONTRACT and fantom == 0 and hianyzo == 0)
    print("completeness ledger: found %d/%d; phantom %d; missing %d — %s"
          % (megvan, NCONTRACT, fantom, hianyzo, "holds" if A2 else "FAILS"))

    # ball r<=5
    lat = {(0,)*DIM}; front = [(0,)*DIM]; golyo = [1]
    for r in range(1, 6):
        ujf = []
        for p in front:
            for d in elf:
                q = tuple((x+y) % L for x, y in zip(p, d))
                if q not in lat:
                    lat.add(q); ujf.append(q)
        golyo.append(golyo[-1]+len(ujf)); front = ujf
    hiv = [1, 11, 61, 231, 681, 1683]
    A3 = golyo[:4] == hiv[:4]
    print("ball (r=0..5): %s — reference (fourth order): %s — r<=3: %s; "
          "r<=5: %s" % (golyo, hiv, "holds" if A3 else "FAILS",
                        "agrees" if golyo == hiv else "differs"))

    # projector seal: sampling sparse form
    rng = np.random.default_rng(MAG)
    idxek = [np.ravel_multi_index(((koordok + d) % L).T, (L,)*DIM)
             for d in igazd]
    occ_f = occ.ravel()
    pecset_a, pecset_b = 0.0, 0.0
    minta = []
    bet = np.where(occ_f)[0]; ur = np.where(~occ_f)[0]
    minta = list(rng.choice(bet, 64, replace=False)) \
          + list(rng.choice(ur, 64, replace=False))
    for mi in minta:
        n = koordok[mi]
        ph = sum(((n[j]*koordok[:, j]) % L)/L for j in range(DIM))
        vv = np.exp(2j*np.pi*ph)
        Av = np.zeros(NSITE, dtype=complex)
        for ix in idxek:
            Av += vv[ix]
        lj = float(sum(2-2*np.cos(2*np.pi*ni/L) for ni in n))
        pecset_a = max(pecset_a, float(np.max(np.abs(10*vv - Av - lj*vv))))
        # the direct-summation transform of the G table at this mode
        val = complex(np.sum(Gf * np.conj(vv)))
        pecset_b = max(pecset_b, abs(val - (1.0 if occ_f[mi] else 0.0)))
    print("projector seal (64+64 modes, seed %d): residual branch %.2e; "
          "transform branch %.2e — %s"
          % (MAG, pecset_a, pecset_b,
             "HOLDS" if max(pecset_a, pecset_b) < 1e-9 else "FAILS"))

    print("\nconditions: A1 %s | A2 %s | A3 %s | A4 %s"
          % tuple("holds" if a else "FAILS" for a in (A1, A2, A3, A4)))
    print("VERDICT: %s  (%.0f s)"
          % ("HOLDS — the native winner reads itself as five-extensional from"
             " the inside, and the seal holds" if all((A1, A2, A3, A4)) else
             "PARTIAL — the failed condition is above", time.time()-t0))

if __name__ == "__main__":
    main()
