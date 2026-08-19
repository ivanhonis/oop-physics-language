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

# Identifier glossary — the identifiers were renamed from Hungarian
# to English; the original Hungarian name stands on the right:
#   accepted = elfogadott    antipodal = atellenes
#   ball = golyo             best_ratio = legjobb
#   classes = osztaly        cols = oszlop
#   coords = koord           d_strongest = d_er
#   dev = elt                dlist = dlista
#   edge_set = elek          found = megvan
#   G_machine = G_gepi       gap = res
#   GAP_EXPECTED = RES_VART  machine = gep
#   missing = hianyzo        N_FILL = NTOLT
#   neighbour = szomszed     new_front = ujf
#   one = egy                pairs = parok
#   phantom = fantom         ranked = rend
#   reference = hiv          remainder = maradek
#   seen = lat               target = cel
#   threshold = kuszob       truth = igaz
#   WINDOW = ABLAK           worst = rossz

import numpy as np
import sys, time
from itertools import product

L, DIM = 12, 4
NSITE = L**DIM              # 20736
N_FILL = 11075               # closed degree (PKG-15-3, V6)
NCONTRACT = 4 * NSITE       # 82944
GAP_EXPECTED = 2.0 - np.sqrt(3.0)
WINDOW = 30                  # fixed search window (PKG-15-1 §8)

def canon(d):
    return tuple(sorted(int(min(x % L, (-x) % L)) for x in d))

def main():
    machine = 1
    if "--gep" in sys.argv:
        machine = int(sys.argv[sys.argv.index("--gep")+1])
    print("== PKG-15-4 — the readout (J4, N = %d) ==" % N_FILL)

    # --- 1) ladder and closed degree ---
    k = 2*np.pi*np.arange(L)/L
    one = 2.0 - 2.0*np.cos(k)
    lam = (one[:,None,None,None] + one[None,:,None,None]
           + one[None,None,:,None] + one[None,None,None,:])
    lam_flat = np.sort(lam.ravel())
    gap = lam_flat[N_FILL] - lam_flat[N_FILL-1]
    A1 = abs(gap - GAP_EXPECTED) < 1e-9
    print("closed degree: gap above degree %d is %.9f (expected 2-sqrt3 = %.9f) — %s"
          % (N_FILL, gap, GAP_EXPECTED, "holds" if A1 else "FAILS"))

    threshold = lam_flat[N_FILL-1] + 1e-9
    occ = lam <= threshold
    assert int(occ.sum()) == N_FILL

    # --- 2) closeness map on the closed route ---
    G = np.fft.ifftn(occ.astype(float))
    assert np.max(np.abs(G.imag)) < 1e-12
    G = G.real

    # displacement classes: a weave — exact agreement within a class
    classes = {}
    for d in np.ndindex(L, L, L, L):
        if d == (0,0,0,0):
            continue
        classes.setdefault(canon(d), []).append(G[d])
    worst = max(np.std(v) for v in classes.values())
    assert worst < 1e-12

    neighbour = G[1,0,0,0]
    antipodal = G[L//2, L//2, L//2, L//2]
    print("neighbour closeness G(1,0,0,0) = %+.6f" % neighbour)
    print("ANTIPODAL ECHO G(6,6,6,6) = %+.6f  (sign: %s; "
          "|ratio to the neighbour| = %.4f)  [obligatory separate row]"
          % (antipodal, "negative" if antipodal < 0 else "positive",
             abs(antipodal)/neighbour))

    # --- 3) signed jump (fixed window of 30) ---
    g = G.ravel().copy()
    g[0] = -np.inf
    ranked = np.argsort(g)[::-1]
    v = g[ranked]
    best_ratio, kstar = -1.0, None
    for m in range(1, WINDOW+1):
        if v[m] > 0:
            r = v[m-1]/v[m]
            if r > best_ratio:
                best_ratio, kstar = r, m
    print("start of the signed list:", np.round(v[:12], 5))
    print("jump after place %d: %.5f -> %.5f (%.1f-fold)"
          % (kstar, v[kstar-1], v[kstar], best_ratio))

    remainder = v[kstar:]
    remainder = remainder[np.isfinite(remainder)]
    j = int(np.argmax(np.abs(remainder)))
    d_strongest = tuple(np.unravel_index(int(ranked[kstar+j]), (L,L,L,L)))
    S = v[kstar-1]/abs(float(remainder[j]))
    A4 = S >= 2.0
    print("band sentinel: S = %.4f (threshold 2) — %s; strongest rejected: class %s"
          ", G = %+.6f" % (S, "holds" if A4 else "FAILS",
                           canon(d_strongest), float(remainder[j])))

    va = np.sort(np.abs(np.where(np.isfinite(g), g, 0)))[::-1]
    r_abs = va[:WINDOW]/np.maximum(va[1:WINDOW+1], 1e-300)
    k_abs = int(np.argmax(r_abs)) + 1
    print("old absolute rule (for comparison): jump after place %d "
          "(%.1f-fold)" % (k_abs, r_abs[k_abs-1]))

    # --- 4) rebuilding and completeness ledger ---
    accepted = [tuple(np.unravel_index(int(i), (L,L,L,L))) for i in ranked[:kstar]]
    rc = np.arange(NSITE)
    coords = np.array(np.unravel_index(rc, (L,L,L,L))).T
    def edge_set(dlist):
        pairs = set()
        for d in dlist:
            target = (coords + d) % L
            b = np.ravel_multi_index(target.T, (L,L,L,L))
            a2 = np.minimum(rc, b); b2 = np.maximum(rc, b)
            pairs |= set(map(int, a2*NSITE + b2))
        return pairs
    rec = edge_set(accepted)
    truth = edge_set([(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1),
                 (L-1,0,0,0),(0,L-1,0,0),(0,0,L-1,0),(0,0,0,L-1)])
    found, phantom, missing = len(rec & truth), len(rec-truth), len(truth-rec)
    A2 = (found == NCONTRACT and phantom == 0 and missing == 0)
    print("completeness ledger: found %d/%d; phantom %d; missing %d — %s"
          % (found, NCONTRACT, phantom, missing, "holds" if A2 else "FAILS"))

    # --- 5) ball reading on the rebuilt network (r <= 5) ---
    seen = {(0,)*DIM}
    front = [(0,)*DIM]
    ball = [1]
    for r in range(1, 6):
        new_front = []
        for p in front:
            for d in accepted:
                q = tuple((x+y) % L for x, y in zip(p, d))
                if q not in seen:
                    seen.add(q)
                    new_front.append(q)
        ball.append(ball[-1] + len(new_front))
        front = new_front
    reference = [1, 9, 41, 129, 321, 681]
    A3 = ball[:4] == reference[:4]
    print("ball (r=0..5): %s — reference (cubic): %s — r<=3 verdict: %s; "
          "r<=5 report: %s"
          % (ball, reference, "holds" if A3 else "FAILS",
             "agrees" if ball == reference else "differs"))

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
    if machine:
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
        cols = w <= threshold
        assert int(cols.sum()) == N_FILL
        P0 = V[:, cols] @ V[0, cols]
        G_machine = np.empty(NSITE)
        for h in np.ndindex(*(L,)*DIM):
            G_machine[idx(h)] = G[h]
        dev = float(np.max(np.abs(P0 - G_machine)))
        print("projector by two routes: largest deviation = %.2e (%.0f min) — %s"
              % (dev, (time.time()-t0)/60, "HOLDS" if dev < 1e-10 else "FAILS"))
        print("== PKG-15-4 TWO-ROUTE SEAL: %s =="
              % ("HOLDS" if dev < 1e-10 else "FAILS"))

if __name__ == "__main__":
    main()
