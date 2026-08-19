# PKG-14-3 — The filling race (II/14, the extension staircase)
# According to B3: the ladders are recomputed by a NEW code path (incidence
# matrix: L = B^T B, one row per edge), and the race starts only after they
# agree with the reference values.
# Race: filling from below — cost(N) = the sum of the N smallest beats of the ladder.

# Identifier glossary — the identifiers were renamed from Hungarian
# to English; the original Hungarian name stands on the right:
#   degree_boundaries = fokhatarok  is_connected = osszefuggo
#   j2_beats_control = j2_veri_K    plane_band = sik_sav
#   space_band = ter_sav

import numpy as np
from itertools import combinations
from math import gcd

N = 512
TOL = 1e-9


# ---------- new code path: incidence matrix ----------

def laplacian_incidence(n, edges):
    B = np.zeros((len(edges), n))
    for r, (i, j) in enumerate(edges):
        B[r, i] = 1.0
        B[r, j] = -1.0
    return B.T @ B

def ring_edges(n, steps):
    E = set()
    for i in range(n):
        for s in steps:
            E.add((min(i, (i + s) % n), max(i, (i + s) % n)))
    return sorted(E)

def torus2_tri_edges(L1, L2):
    idx = lambda x, y: (x % L1) * L2 + (y % L2)
    E = set()
    for x in range(L1):
        for y in range(L2):
            a = idx(x, y)
            for dx, dy in [(1, 0), (0, 1), (1, 1)]:
                b = idx(x + dx, y + dy)
                E.add((min(a, b), max(a, b)))
    return sorted(E)

def torus3_edges(L):
    idx = lambda x, y, z: ((x % L) * L + (y % L)) * L + (z % L)
    E = set()
    for x in range(L):
        for y in range(L):
            for z in range(L):
                a = idx(x, y, z)
                for d in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]:
                    b = idx(x + d[0], y + d[1], z + d[2])
                    E.add((min(a, b), max(a, b)))
    return sorted(E)


# ---------- building the field on the new path ----------

field = {}
field["J2 plane 16x32"] = np.sort(np.linalg.eigvalsh(
    laplacian_incidence(N, torus2_tri_edges(16, 32))))
field["J3 space 8x8x8"] = np.sort(np.linalg.eigvalsh(
    laplacian_incidence(N, torus3_edges(8))))
field["control plane 8x64"] = np.sort(np.linalg.eigvalsh(
    laplacian_incidence(N, torus2_tri_edges(8, 64))))
for trip in combinations(range(1, 13), 3):
    field["line %s" % (trip,)] = np.sort(np.linalg.eigvalsh(
        laplacian_incidence(N, ring_edges(N, trip))))

J1 = "line (1, 2, 3)"
J2 = "J2 plane 16x32"
J3 = "J3 space 8x8x8"

# ---------- B3: agreement with the reference values ----------

print("== B3 precondition: independent recomputation ==")
traces = {k: float(v.sum()) for k, v in field.items()}
print("trace sum min/max: %.10f / %.10f (prescribed 3072)"
      % (min(traces.values()), max(traces.values())))
zeros = {k: int((v < TOL).sum()) for k, v in field.items()}
print("zero modes: J1=%d J2=%d J3=%d control=%d; disconnected scan members: %d"
      % (zeros[J1], zeros[J2], zeros[J3], zeros["control plane 8x64"],
         sum(1 for k, z in zeros.items() if k.startswith("line") and z > 1)))
spot = [
    ("J1 2nd beat", field[J1][1], 0.002108),
    ("J2 2nd beat", field[J2][1], 0.076864),
    ("J3 2nd beat", field[J3][1], 2.0 - np.sqrt(2.0)),
    ("J3 top",      field[J3][-1], 12.0),
]
for name, got, ref in spot:
    print("  %-12s %.6f (reference %.6f, deviation %.1e)"
          % (name, got, ref, abs(got - ref)))

# ---------- the race ----------

cost = {k: np.concatenate([[0.0], np.cumsum(v)]) for k, v in field.items()}
# cost[k][n] = cost at n instances

names = sorted(field.keys())
winners = []
for n in range(1, N + 1):
    vals = np.array([cost[k][n] for k in names])
    m = vals.min()
    w = [names[i] for i in np.flatnonzero(vals < m + TOL)]
    winners.append((n, m, w))

# --- the main reading: on the declared triple ---
print("\n== The main reading: J1-J2-J3 pairwise ==")
trio_w = []
for n in range(1, N + 1):
    c1, c2, c3 = cost[J1][n], cost[J2][n], cost[J3][n]
    m = min(c1, c2, c3)
    w = "".join(t for t, c in [("1", c1), ("2", c2), ("3", c3)] if c < m + TOL)
    trio_w.append(w)

def bands(seq, start=1):
    out = []
    for i, w in enumerate(seq):
        n = start + i
        if out and out[-1][0] == w:
            out[-1][2] = n
        else:
            out.append([w, n, n])
    return out

print("bands (winner: from N to N):")
for w, a, b in bands(trio_w):
    print("  J%s: %d..%d" % (w, a, b))

# plane band and space band by the rule (J2 beats both / J3 beats both)
plane_band = [n for n in range(1, N) if trio_w[n - 1] == "2"]
space_band = [n for n in range(1, N) if trio_w[n - 1] == "3"]
def is_connected(xs):
    return bool(xs) and xs[-1] - xs[0] + 1 == len(xs)
print("plane band: %s (connected: %s)" %
      (("%d..%d" % (plane_band[0], plane_band[-1])) if plane_band else "none", is_connected(plane_band)))
print("space band: %s (connected: %s)" %
      (("%d..%d" % (space_band[0], space_band[-1])) if space_band else "none", is_connected(space_band)))

# --- the full field ---
print("\n== Full field: regimes of the strict winners ==")
def short(ws):
    if len(ws) > 3:
        return "%d-fold tie" % len(ws)
    return " + ".join(w.replace("line ", "v").replace(" plane 16x32", "")
                      .replace(" space 8x8x8", "").replace("control plane 8x64", "K8x64")
                      for w in ws)
seq = [short(w) for n, m, w in winners]
for w, a, b in bands(seq):
    n_mid = (a + b) // 2
    print("  N=%3d..%3d  %-28s (e.g. N=%d cost %.3f)"
          % (a, b, w, n_mid, winners[n_mid - 1][1]))

# --- key checks ---
print("\n== Checks ==")
print("N=1: every network pays 0:", all(abs(cost[k][1]) < TOL for k in names))
v512 = [cost[k][N] for k in names]
print("N=512: tie at 3072:", max(v512) - min(v512) < 1e-8,
      " (min %.8f, max %.8f)" % (min(v512), max(v512)))

# shell logic: the band boundary of J3 vs its degree boundaries
degree_boundaries = [1, 7, 19, 27, 33, 57, 81, 87, 126, 186, 198, 222, 290, 314,
              326, 386, 425, 431, 455, 479, 485, 493, 505, 511, 512]
if space_band:
    print("lower boundary of the space band: %d; degree boundaries of J3 nearby: %s"
          % (space_band[0], [f for f in degree_boundaries if abs(f - space_band[0]) <= 6]))

# mirror effect: is the winner of the full end the network with the highest top?
tops = sorted(((field[k][-1], k) for k in names), reverse=True)
print("highest top: %.4f (%s) — the expected winner of the full end" % (tops[0][0], tops[0][1]))

# J2 versus the control: the effect of stretching
j2_beats_control = [n for n in range(1, N) if cost[J2][n] < cost["control plane 8x64"][n] - TOL]
print("the 16x32 plane beats the 8x64 control at %d fillings" % len(j2_beats_control))
