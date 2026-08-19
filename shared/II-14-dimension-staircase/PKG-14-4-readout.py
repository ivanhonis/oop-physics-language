# PKG-14-4 — Closing the loop: readout on the winner (II/14)
# The fixed protocol (PKG-14-1, point 8; PKG-14-3, C4):
#   - winner: J3 space (8x8x8), N = 290 (the first closed degree of the space band)
#   - free excluding instances: the views exactly from the instance correlations
#     (the accelerated form of tool 4) — closeness = the pairwise one-body
#     map G(delta) of the finished state
#   - the neighbour count is singled out by the jump of the closeness list
#   - ball reading up to at most r = 3, against the three reference sequences
#   - resonance sentinel: the antipodal classes reported separately

import numpy as np
from collections import deque

L = 8
Nsite = L ** 3
Ninst = 290

# --- the ladder and the filling (closed form) ---
k = 2.0 * np.pi * np.arange(L) / L
one = 2.0 * (1.0 - np.cos(k))
lam = one[:, None, None] + one[None, :, None] + one[None, None, :]
order = np.argsort(lam.ravel(), kind="stable")
occ_flat = order[:Ninst]
lam_sorted = np.sort(lam.ravel())
print("closed-degree check: beat 290 is %.6f, beat 291 is %.6f (gap %.4f)"
      % (lam_sorted[289], lam_sorted[290], lam_sorted[290] - lam_sorted[289]))
assert lam_sorted[290] - lam_sorted[289] > 0.5

# is the filling the complete lambda<=6 set? (unambiguity)
assert abs(lam_sorted[289] - 6.0) < 1e-9 and lam_sorted[290] > 6.0

# --- closeness map: G(delta) = (1/512) sum_occ e^{i k.delta} ---
occ = np.zeros((L, L, L), dtype=bool)
occ.ravel()[occ_flat] = True
# G(delta) is the inverse Fourier transform of the occupancy indicator
G = np.fft.ifftn(occ.astype(float))  # G[dx,dy,dz], G[0,0,0] = 290/512
assert np.max(np.abs(G.imag)) < 1e-12
G = G.real

# homogeneity: because of the weave G depends only on the displacement — this is
# construction; the protocol asks for the spread to be measured on the
# instance-level map, and for free excluding instances the two are exactly
# identical (tool 4).

# --- displacement classes ---
def canon(d):
    # the octahedral symmetry: up to sign and axis permutation
    v = sorted(min(x % L, (-x) % L) for x in d)
    return tuple(v)

classes = {}
for dx in range(L):
    for dy in range(L):
        for dz in range(L):
            if dx == dy == dz == 0:
                continue
            c = canon((dx, dy, dz))
            classes.setdefault(c, []).append(G[dx, dy, dz])

rows = []
for c, vals in classes.items():
    vals = np.array(vals)
    rows.append((c, float(vals.mean()), float(vals.std()), len(vals)))
    assert vals.std() < 1e-12  # exactly identical within a class

rows.sort(key=lambda r: -abs(r[1]))
print()
print("== closeness classes (decreasing by |G|, the start) ==")
for c, m, s, n in rows[:10]:
    print("  class %-10s  G = %+.6f   (x%d displacements)" % (str(c), m, n))

# --- resonance sentinel: does a non-neighbour class agree with the neighbour? ---
nb = rows[0]
echo = [r for r in rows[1:] if abs(abs(r[1]) - abs(nb[1])) < 1e-12]
print()
print("resonance sentinel: other classes agreeing exactly with the neighbour: %d"
      % len(echo))
print("antipodal echo (4,4,4): G = %+.6f, %.1f%% of the neighbour"
      % (G[4, 4, 4], 100 * abs(G[4, 4, 4] / G[0, 0, 1])))

# --- singling out the jump and the neighbour count, BY TWO RULES ---
# Point 8 of PKG-14-1 did not state whether the jump is to be sought on the
# signed or on the absolute-value closeness list. On this weave the two
# diverge, so the package reports both; the main figures are those of the
# signed reading. (The signed form was raised to a rule by PKG-14-5.)

idx = lambda x, y, z: ((x % L) * L + (y % L)) * L + (z % L)
true_edges = set()
for x in range(L):
    for y in range(L):
        for z in range(L):
            a = idx(x, y, z)
            for d in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]:
                b = idx(x + d[0], y + d[1], z + d[2])
                true_edges.add((min(a, b), max(a, b)))

flat_off = [(dx, dy, dz) for dx in range(L) for dy in range(L) for dz in range(L)
            if not dx == dy == dz == 0]


def olvasat(mod):
    """One readout under the given jump rule: 'signed' or 'absolute'."""
    kulcs = (lambda d: G[d]) if mod == "signed" else (lambda d: abs(G[d]))
    rend = sorted(flat_off, key=lambda d: -kulcs(d))
    vals = np.array([kulcs(d) for d in rend[:30]])
    ratios = vals[:-1] / np.maximum(np.abs(vals[1:]), 1e-300)
    kstar = int(np.argmax(ratios[:20])) + 1

    top = rend[:kstar]
    rec_edges = set()
    for x in range(L):
        for y in range(L):
            for z in range(L):
                a = idx(x, y, z)
                for d in top:
                    b = idx(x + d[0], y + d[1], z + d[2])
                    rec_edges.add((min(a, b), max(a, b)))

    adj = [[] for _ in range(Nsite)]
    for a, b in rec_edges:
        adj[a].append(b)
        adj[b].append(a)
    dist = [-1] * Nsite
    dist[0] = 0
    q = deque([0])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if dist[v] < 0:
                dist[v] = dist[u] + 1
                q.append(v)
    ball = [sum(1 for d in dist if 0 <= d <= r) for r in range(4)]

    print()
    print("== %s jump rule ==" % mod)
    print("  start of the ordered list:", np.round(vals[:10], 5))
    print("  the largest jump after place %d: %.6f -> %.6f (%.2f-fold)"
          % (kstar, vals[kstar - 1], vals[kstar],
             vals[kstar - 1] / abs(vals[kstar])))
    print("  displacement classes drawn in:", sorted({canon(d) for d in top}))
    print("  rebuilding: %d edges; real found %d/%d; phantom %d; missing %d"
          % (len(rec_edges), len(rec_edges & true_edges), len(true_edges),
             len(rec_edges - true_edges), len(true_edges - rec_edges)))
    print("  ball (r=0..3):", ball,
          " increments:", [ball[i + 1] - ball[i] for i in range(3)])
    return kstar, ball


olvasat("signed")     # the published main figures: k*=7, 256 phantom, ball 1,8,32,88
olvasat("absolute")   # the second reading: k*=15, 2304 phantom, ball 1,16,92,296
print()
print("reference sequences: line 1,7,13,19 | plane 1,7,19,37 | space 1,7,25,63")
