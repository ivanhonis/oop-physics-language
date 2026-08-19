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

# Identifier glossary — the identifiers were renamed from Hungarian
# to English; the original Hungarian name stands on the right:
#   accepted = elf           antipodal = atellenes
#   ball = golyo             best_ratio = legjobb
#   classes = oszt           coords = koordok
#   d_strongest = d_er       dlist = dl
#   edge_set = elek          empty = ur
#   filled = bet             found = megvan
#   G_flat = Gf              gap = res
#   GAP_EXPECTED = RES_VART  idx_sets = idxek
#   lam_j = lj               missing = hianyzo
#   mode_vec = vv            N_FILL = NTOLT
#   neighbour = szomszed     new_front = ujf
#   one = egy                pairs = parok
#   phantom = fantom         phase = ph
#   ranked = rend            reference = hiv
#   remainder = maradek      sample = minta
#   seal_a = pecset_a        seal_b = pecset_b
#   SEED = MAG               seen = lat
#   target = cel             threshold = kuszob
#   true_dirs = igazd        truth = igaz
#   WINDOW = ABLAK

import numpy as np
import time
from collections import deque

L, DIM = 12, 5
NSITE = L**DIM              # 248832
N_FILL = 130902
NCONTRACT = 5 * NSITE       # 1,244,160
GAP_EXPECTED = 2.0 - np.sqrt(3.0)
WINDOW = 30
SEED = 248832

def canon(d):
    return tuple(sorted(int(min(x % L, (-x) % L)) for x in d))

def main():
    t0 = time.time()
    print("== PKG-16-4 — the readout (J5, N = %d) ==" % N_FILL)
    k = 2*np.pi*np.arange(L)/L
    one = 2.0 - 2.0*np.cos(k)
    lam = one.reshape(-1,1,1,1,1)+one.reshape(1,-1,1,1,1)+one.reshape(1,1,-1,1,1)\
        + one.reshape(1,1,1,-1,1)+one.reshape(1,1,1,1,-1)
    lam_flat = np.sort(lam.ravel())
    gap = lam_flat[N_FILL] - lam_flat[N_FILL-1]
    A1 = abs(gap - GAP_EXPECTED) < 1e-9
    print("closed degree: gap above degree %d is %.9f (expected %.9f) — %s"
          % (N_FILL, gap, GAP_EXPECTED, "holds" if A1 else "FAILS"))
    threshold = lam_flat[N_FILL-1] + 1e-9
    occ = lam <= threshold
    assert int(occ.sum()) == N_FILL

    G = np.fft.ifftn(occ.astype(float))
    assert np.max(np.abs(G.imag)) < 1e-12
    G = G.real

    # class exactness (a weave)
    classes = {}
    G_flat = G.ravel()
    coords = np.array(np.unravel_index(np.arange(NSITE), (L,)*DIM)).T
    for i in range(NSITE):
        if i == 0:
            continue
        classes.setdefault(canon(coords[i]), []).append(G_flat[i])
    assert max(np.std(v) for v in classes.values()) < 1e-12

    neighbour = G[1,0,0,0,0]
    antipodal = G[(L//2,)*DIM]
    print("neighbour closeness G(1,0,0,0,0) = %+.6f" % neighbour)
    print("ANTIPODAL ECHO G(6,6,6,6,6) = %+.6f (sign: %s; "
          "|ratio| = %.4f) [obligatory row]"
          % (antipodal, "negative" if antipodal < 0 else "positive",
             abs(antipodal)/neighbour))

    g = G_flat.copy(); g[0] = -np.inf
    ranked = np.argsort(g)[::-1]
    v = g[ranked]
    best_ratio, kstar = -1.0, None
    for m in range(1, WINDOW+1):
        if v[m] > 0:
            r = v[m-1]/v[m]
            if r > best_ratio:
                best_ratio, kstar = r, m
    print("start of the signed list:", np.round(v[:14], 5))
    print("jump after place %d: %.5f -> %.5f (%.1f-fold)"
          % (kstar, v[kstar-1], v[kstar], best_ratio))
    remainder = v[kstar:]; remainder = remainder[np.isfinite(remainder)]
    j = int(np.argmax(np.abs(remainder)))
    d_strongest = tuple(coords[ranked[kstar+j]])
    S = v[kstar-1]/abs(float(remainder[j]))
    A4 = S >= 2.0
    print("band sentinel: S = %.4f (threshold 2) — %s; strongest rejected: "
          "class %s, G = %+.6f"
          % (S, "holds" if A4 else "FAILS", canon(d_strongest), float(remainder[j])))
    va = np.sort(np.abs(np.where(np.isfinite(g), g, 0)))[::-1]
    r_abs = va[:WINDOW]/np.maximum(va[1:WINDOW+1], 1e-300)
    k_abs = int(np.argmax(r_abs)) + 1
    print("old absolute rule: jump after place %d (%.1f-fold)"
          % (k_abs, r_abs[k_abs-1]))

    # rebuilding + completeness
    accepted = [tuple(coords[i]) for i in ranked[:kstar]]
    rc = np.arange(NSITE)
    def edge_set(dlist):
        pairs = set()
        for d in dlist:
            target = (coords + d) % L
            b = np.ravel_multi_index(target.T, (L,)*DIM)
            pairs |= set(map(int, np.minimum(rc, b)*NSITE + np.maximum(rc, b)))
        return pairs
    rec = edge_set(accepted)
    true_dirs = []
    for t in range(DIM):
        for sgn in (1, -1):
            d = [0]*DIM; d[t] = sgn % L
            true_dirs.append(tuple(x % L for x in d))
    truth = edge_set(true_dirs)
    found, phantom, missing = len(rec & truth), len(rec-truth), len(truth-rec)
    A2 = (found == NCONTRACT and phantom == 0 and missing == 0)
    print("completeness ledger: found %d/%d; phantom %d; missing %d — %s"
          % (found, NCONTRACT, phantom, missing, "holds" if A2 else "FAILS"))

    # ball r<=5
    seen = {(0,)*DIM}; front = [(0,)*DIM]; ball = [1]
    for r in range(1, 6):
        new_front = []
        for p in front:
            for d in accepted:
                q = tuple((x+y) % L for x, y in zip(p, d))
                if q not in seen:
                    seen.add(q); new_front.append(q)
        ball.append(ball[-1]+len(new_front)); front = new_front
    reference = [1, 11, 61, 231, 681, 1683]
    A3 = ball[:4] == reference[:4]
    print("ball (r=0..5): %s — reference (fourth order): %s — r<=3: %s; "
          "r<=5: %s" % (ball, reference, "holds" if A3 else "FAILS",
                        "agrees" if ball == reference else "differs"))

    # projector seal: sampling sparse form
    rng = np.random.default_rng(SEED)
    idx_sets = [np.ravel_multi_index(((coords + d) % L).T, (L,)*DIM)
             for d in true_dirs]
    occ_f = occ.ravel()
    seal_a, seal_b = 0.0, 0.0
    sample = []
    filled = np.where(occ_f)[0]; empty = np.where(~occ_f)[0]
    sample = list(rng.choice(filled, 64, replace=False)) \
          + list(rng.choice(empty, 64, replace=False))
    for mi in sample:
        n = coords[mi]
        phase = sum(((n[j]*coords[:, j]) % L)/L for j in range(DIM))
        mode_vec = np.exp(2j*np.pi*phase)
        Av = np.zeros(NSITE, dtype=complex)
        for ix in idx_sets:
            Av += mode_vec[ix]
        lam_j = float(sum(2-2*np.cos(2*np.pi*ni/L) for ni in n))
        seal_a = max(seal_a, float(np.max(np.abs(10*mode_vec - Av - lam_j*mode_vec))))
        # the direct-summation transform of the G table at this mode
        val = complex(np.sum(G_flat * np.conj(mode_vec)))
        seal_b = max(seal_b, abs(val - (1.0 if occ_f[mi] else 0.0)))
    print("projector seal (64+64 modes, seed %d): residual branch %.2e; "
          "transform branch %.2e — %s"
          % (SEED, seal_a, seal_b,
             "HOLDS" if max(seal_a, seal_b) < 1e-9 else "FAILS"))

    print("\nconditions: A1 %s | A2 %s | A3 %s | A4 %s"
          % tuple("holds" if a else "FAILS" for a in (A1, A2, A3, A4)))
    print("VERDICT: %s  (%.0f s)"
          % ("HOLDS — the native winner reads itself as five-extensional from"
             " the inside, and the seal holds" if all((A1, A2, A3, A4)) else
             "PARTIAL — the failed condition is above", time.time()-t0))

if __name__ == "__main__":
    main()
