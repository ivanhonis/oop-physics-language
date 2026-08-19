# PKG-15-4 — The readout (II/15)
# System (PKG-15-3, V6): J4 hypercube weave 12x12x12x12, 82944 contracts;
# filling: N = 11075, a closed degree (the value of the gap above it is known
# in advance to be 2 - sqrt(3)).
# Protocol per PKG-15-1 §8, verdict conditions fixed in advance:
#   A1 the closed degree holds (gap = 2 - sqrt(3));
#   A2 completeness ledger 82944/82944, zero phantom, zero missing;
#   A3 the ball is exact up to r <= 3 on the cubic reference sequence
#      (reporting up to r <= 5, validity 2r < 12);
#   A4 band sentinel >= 2 (the worst local value).
# Obligatory separate row: the signed correlation of the antipodal class
# (bipartite winner).
# Two-route rule: closed (FFT) route + machine projector check (dense
# eigenproblem with eigenvectors). The machine part needs ~10-11 GB of
# memory and ~20-40 minutes.
# Usage:
#   python3 PKG-15-4-readout.py            # everything (closed route + machine check)
#   python3 PKG-15-4-readout.py --gep 0    # closed route only (fast)

import numpy as np
import sys, time
from itertools import product

L, DIM = 12, 4
NSITE = L**DIM              # 20736
NTOLT = 11075               # closed degree (PKG-15-3, V6)
NCONTRACT = 4 * NSITE       # 82944
RES_VART = 2.0 - np.sqrt(3.0)
ABLAK = 30                  # fixed search window (PKG-15-1 §8)

def canon(d):
    return tuple(sorted(int(min(x % L, (-x) % L)) for x in d))

def main():
    gep = 1
    if "--gep" in sys.argv:
        gep = int(sys.argv[sys.argv.index("--gep")+1])
    print("== PKG-15-4 — the readout (J4, N = %d) ==" % NTOLT)

    # --- 1) ladder and closed degree ---
    k = 2*np.pi*np.arange(L)/L
    egy = 2.0 - 2.0*np.cos(k)
    lam = (egy[:,None,None,None] + egy[None,:,None,None]
           + egy[None,None,:,None] + egy[None,None,None,:])
    lam_flat = np.sort(lam.ravel())
    res = lam_flat[NTOLT] - lam_flat[NTOLT-1]
    A1 = abs(res - RES_VART) < 1e-9
    print("closed degree: gap above degree %d is %.9f (expected 2-sqrt3 = %.9f) — %s"
          % (NTOLT, res, RES_VART, "holds" if A1 else "FAILS"))

    kuszob = lam_flat[NTOLT-1] + 1e-9
    occ = lam <= kuszob
    assert int(occ.sum()) == NTOLT

    # --- 2) closeness map on the closed route ---
    G = np.fft.ifftn(occ.astype(float))
    assert np.max(np.abs(G.imag)) < 1e-12
    G = G.real

    # displacement classes: a weave — exact agreement within a class
    osztaly = {}
    for d in np.ndindex(L, L, L, L):
        if d == (0,0,0,0):
            continue
        osztaly.setdefault(canon(d), []).append(G[d])
    rossz = max(np.std(v) for v in osztaly.values())
    assert rossz < 1e-12

    szomszed = G[1,0,0,0]
    atellenes = G[L//2, L//2, L//2, L//2]
    print("neighbour closeness G(1,0,0,0) = %+.6f" % szomszed)
    print("ANTIPODAL ECHO G(6,6,6,6) = %+.6f  (sign: %s; "
          "|ratio to the neighbour| = %.4f)  [obligatory separate row]"
          % (atellenes, "negative" if atellenes < 0 else "positive",
             abs(atellenes)/szomszed))

    # --- 3) signed jump (fixed window of 30) ---
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
    print("start of the signed list:", np.round(v[:12], 5))
    print("jump after place %d: %.5f -> %.5f (%.1f-fold)"
          % (kstar, v[kstar-1], v[kstar], legjobb))

    maradek = v[kstar:]
    maradek = maradek[np.isfinite(maradek)]
    j = int(np.argmax(np.abs(maradek)))
    d_er = tuple(np.unravel_index(int(rend[kstar+j]), (L,L,L,L)))
    S = v[kstar-1]/abs(float(maradek[j]))
    A4 = S >= 2.0
    print("band sentinel: S = %.4f (threshold 2) — %s; strongest rejected: class %s"
          ", G = %+.6f" % (S, "holds" if A4 else "FAILS",
                           canon(d_er), float(maradek[j])))

    va = np.sort(np.abs(np.where(np.isfinite(g), g, 0)))[::-1]
    r_abs = va[:ABLAK]/np.maximum(va[1:ABLAK+1], 1e-300)
    k_abs = int(np.argmax(r_abs)) + 1
    print("old absolute rule (for comparison): jump after place %d "
          "(%.1f-fold)" % (k_abs, r_abs[k_abs-1]))

    # --- 4) rebuilding and completeness ledger ---
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
    print("completeness ledger: found %d/%d; phantom %d; missing %d — %s"
          % (megvan, NCONTRACT, fantom, hianyzo, "holds" if A2 else "FAILS"))

    # --- 5) ball reading on the rebuilt network (r <= 5) ---
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
    print("ball (r=0..5): %s — reference (cubic): %s — r<=3 verdict: %s; "
          "r<=5 report: %s"
          % (golyo, hiv, "holds" if A3 else "FAILS",
             "agrees" if golyo == hiv else "differs"))

    # --- 6) verdict ---
    print("\nconditions: A1 closed degree %s | A2 completeness %s | A3 ball %s | "
          "A4 sentinel %s" % tuple("holds" if a else "FAILS"
                                   for a in (A1, A2, A3, A4)))
    if all((A1, A2, A3, A4)):
        print("VERDICT (closed route): HOLDS — the winner reads itself as"
              " four-extensional from the inside; for the two-route seal the"
              " machine projector check is still missing (--gep 1).")
    else:
        print("VERDICT: PARTIAL — the failed condition and the mechanism above;"
              " the continuation is the business of PKG-15-5.")

    # --- 7) machine projector check (two-route seal) ---
    if gep:
        print("\nmachine projector check: dense eigenproblem with vectors "
              "(~10-11 GB, ~20-40 minutes)...")
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
        print("projector by two routes: largest deviation = %.2e (%.0f min) — %s"
              % (elt, (time.time()-t0)/60, "HOLDS" if elt < 1e-10 else "FAILS"))
        print("== PKG-15-4 TWO-ROUTE SEAL: %s =="
              % ("HOLDS" if elt < 1e-10 else "FAILS"))

if __name__ == "__main__":
    main()
