# PKG-14-5 — The re-readout with a fixed scope (II/14)
# The protocol (fixed before the run):
#   - system: J3 space (12x12x12), coordination six, 5184 contracts
#   - filling: the closed degree nearest half filling from above (a deterministic rule)
#   - closeness: the pairwise one-body map G(delta) of the finished state (II/11, tool 4)
#   - RE-READOUT CORRECTION 1 (signed jump): the jump is to be sought on the
#     SIGNED list, not on the absolute value; the antipodal class is to be
#     reported separately together with its sign (closing the sign gap of II/14)
#   - RE-READOUT CORRECTION 2 (band sentinel): the ratio of the weakest accepted
#     and the strongest rejected closeness; below a factor of 2 the reading is
#     partial (widening the narrow "exact agreement" sentinel of II/14)
#   - completeness ledger: found / missing / phantom, all three with numbers
#   - ball reading up to r <= 5 (validity: 2r < 12 wrap-around); the reference
#     sequence is the quadratic law of space: 1, 7, 25, 63, 129, 231 (increment 4r^2+2)
#   - two-route rule: the ladder and the projector in closed form AND by machine eigenproblem
# Verdict conditions (in advance): A1 the closed degree holds; A2 5184/5184, 0 phantom,
# 0 missing; A3 the ball is exact; A4 sentinel >= 2. All hold -> "holds"; any fails -> partial.

# Identifier glossary — the identifiers were renamed from Hungarian
# to English; the original Hungarian name stands on the right:
#   antipodal = atellenes           ball = golyo
#   best_ratio = legjobb            d_strongest = d_erosebb
#   found = megvan                  G_machine = G_gepi
#   gap = res                       half = fel
#   increments = novek              ladder_dev = elteres_letra
#   missing = hianyzo               N_INST = NINST
#   neighbour = szomszed            phantom = fantom
#   projector_dev = elteres_vetito  ranked = rend
#   reference = hivatkozas          remainder = maradek
#   SHELF6 = D6                     strongest_val = erosebb_ert
#   window = ablak

import numpy as np
from collections import deque

L = 12
NSITE = L ** 3            # 1728 sites
NCONTRACT = 3 * NSITE     # 5184 contracts (six per site)
TOL = 1e-9

# --- 1) The ladder by two independent routes ---------------------------------
k = 2.0 * np.pi * np.arange(L) / L
one = 2.0 * (1.0 - np.cos(k))
lam = one[:, None, None] + one[None, :, None] + one[None, None, :]   # closed form
lam_flat = lam.ravel()
lam_sorted = np.sort(lam_flat)

idx = lambda x, y, z: ((x % L) * L + (y % L)) * L + (z % L)
Lap = np.zeros((NSITE, NSITE))
for x in range(L):
    for y in range(L):
        for z in range(L):
            a = idx(x, y, z)
            Lap[a, a] = 6.0
            for d in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]:
                b = idx(x + d[0], y + d[1], z + d[2])
                Lap[a, b] -= 1.0
                Lap[b, a] -= 1.0
w, V = np.linalg.eigh(Lap)                                            # machine route
ladder_dev = float(np.max(np.abs(np.sort(w) - lam_sorted)))
print("ladder by two routes: largest deviation = %.2e" % ladder_dev)
assert ladder_dev < 1e-10

# --- 2) Singling out the closed degree (fixed rule) --------------------------
half = NSITE // 2                                   # 864
B = int(np.sum(lam_flat < 6.0 - TOL))              # the beats below 6
SHELF6 = int(np.sum(np.abs(lam_flat - 6.0) < TOL))     # the width of the shelf at 6
N_INST = B + SHELF6                                     # the first closed degree above half filling
gap = lam_sorted[N_INST] - lam_sorted[N_INST - 1]
print("closed degree: N* = %d (= %d + %d); half filling %d; gap above the degree %.6f"
      % (N_INST, B, SHELF6, half, gap))
assert B < half <= N_INST and gap > 1e-6

# --- 3) Closeness map by two routes ------------------------------------------
occ = lam <= 6.0 + TOL
assert int(occ.sum()) == N_INST
G = np.fft.ifftn(occ.astype(float))                # closed route: G(delta)
assert np.max(np.abs(G.imag)) < 1e-12
G = G.real

occ_cols = w <= 6.0 + TOL                          # machine route: projector from the eigenvectors
assert int(occ_cols.sum()) == N_INST
P0 = (V[:, occ_cols] @ V[0, occ_cols])             # row 0 of the projector
G_machine = np.empty(NSITE)
for x in range(L):
    for y in range(L):
        for z in range(L):
            G_machine[idx(x, y, z)] = G[x, y, z]
projector_dev = float(np.max(np.abs(P0 - G_machine)))
print("projector by two routes: largest deviation = %.2e" % projector_dev)
assert projector_dev < 1e-10

# --- 4) Displacement classes and the antipodal echo --------------------------
def canon(d):
    return tuple(sorted(int(min(x % L, (-x) % L)) for x in d))

classes = {}
for dx in range(L):
    for dy in range(L):
        for dz in range(L):
            if dx == dy == dz == 0:
                continue
            classes.setdefault(canon((dx, dy, dz)), []).append(G[dx, dy, dz])
for c, vals in classes.items():
    assert np.std(vals) < 1e-12                    # weave: exact within a class

neighbour = G[1, 0, 0]
antipodal = G[L // 2, L // 2, L // 2]
print("neighbour closeness G(1,0,0) = %+.6f" % neighbour)
print("antipodal echo G(6,6,6) = %+.6f  (sign: %s; |ratio to the neighbour| = %.4f)"
      % (antipodal, "negative" if antipodal < 0 else "positive",
         abs(antipodal) / neighbour))

# --- 5) The jump on the SIGNED list (the corrected rule) ---------------------
g = G.ravel().copy()
g[0] = -np.inf                                     # own site excluded
ranked = np.argsort(g)[::-1]                         # signed, decreasing
v = g[ranked]
window = 30                                         # fixed search window
best_ratio, kstar = -1.0, None
for m in range(1, window + 1):
    if v[m] > 0:
        r = v[m - 1] / v[m]
        if r > best_ratio:
            best_ratio, kstar = r, m
print("start of the signed list:", np.round(v[:10], 5))
print("jump after place %d: %.5f -> %.5f (%.1f-fold)"
      % (kstar, v[kstar - 1], v[kstar], best_ratio))

# band sentinel: weakest accepted / strongest rejected (by magnitude);
# the placeholder of the own site (-inf) is not a member of the field
remainder = v[kstar:]
remainder = remainder[np.isfinite(remainder)]
j = int(np.argmax(np.abs(remainder)))
strongest_val = float(remainder[j])
d_strongest = tuple(np.unravel_index(int(ranked[kstar + j]), (L, L, L)))
S = v[kstar - 1] / abs(strongest_val)
print("band sentinel: S = %.4f  (threshold: 2); strongest rejected: class %s, G = %+.6f"
      % (S, canon(d_strongest), strongest_val))

# comparison with the old, absolute-value rule (diagnostics, not the verdict)
va = np.sort(np.abs(np.where(np.isfinite(g), g, 0)))[::-1]
r_abs = va[:window] / np.maximum(va[1:window + 1], 1e-300)
k_abs = int(np.argmax(r_abs)) + 1
print("old absolute rule (for comparison): jump after place %d (%.1f-fold)"
      % (k_abs, r_abs[k_abs - 1]))

# --- 6) Rebuilding and the completeness ledger -------------------------------
top = [tuple(np.unravel_index(int(i), (L, L, L))) for i in ranked[:kstar]]
rec_edges = set()
for x in range(L):
    for y in range(L):
        for z in range(L):
            a = idx(x, y, z)
            for d in top:
                b = idx(x + d[0], y + d[1], z + d[2])
                rec_edges.add((min(a, b), max(a, b)))
true_edges = set()
for x in range(L):
    for y in range(L):
        for z in range(L):
            a = idx(x, y, z)
            for d in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]:
                b = idx(x + d[0], y + d[1], z + d[2])
                true_edges.add((min(a, b), max(a, b)))
found = len(rec_edges & true_edges)
phantom = len(rec_edges - true_edges)
missing = len(true_edges - rec_edges)
print("completeness ledger: found %d/%d; phantom %d; missing %d"
      % (found, NCONTRACT, phantom, missing))

# --- 7) Ball reading up to r <= 5 --------------------------------------------
adj = [[] for _ in range(NSITE)]
for a, b in rec_edges:
    adj[a].append(b)
    adj[b].append(a)
dist = [-1] * NSITE
dist[0] = 0
q = deque([0])
while q:
    u = q.popleft()
    for x2 in adj[u]:
        if dist[x2] < 0:
            dist[x2] = dist[u] + 1
            q.append(x2)
ball = [sum(1 for d in dist if 0 <= d <= r) for r in range(6)]
increments = [ball[i + 1] - ball[i] for i in range(5)]
reference = [1, 7, 25, 63, 129, 231]              # with increment 4r^2+2
print("ball (r=0..5):", ball, " increments:", increments)
print("reference sequence (space, quadratic):", reference)

# --- 8) Verdict according to the fixed conditions ----------------------------
A1 = gap > 1e-6
A2 = (found == NCONTRACT and phantom == 0 and missing == 0)
A3 = (ball == reference)
A4 = (S >= 2.0)
print("\nconditions: A1 closed degree %s | A2 completeness %s | A3 ball %s | A4 sentinel %s"
      % tuple("holds" if a else "FAILS" for a in (A1, A2, A3, A4)))
print("VERDICT:", "HOLDS — the 12-weave size diagnosis is confirmed within scope"
      if all((A1, A2, A3, A4)) else "PARTIAL — the failed condition is named above")
