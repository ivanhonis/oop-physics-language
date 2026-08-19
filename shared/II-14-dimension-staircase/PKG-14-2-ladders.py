# PKG-14-2 — The beat ladders (II/14, the extension staircase)
# Every ladder by two independent routes:
#   (1) machinery: eigenproblem of the adjacency-list matrix of the contract network
#   (2) closed formula: the Fourier form of the weaves
# Self-checks: trace sum (3072), zero modes, machine agreement,
# the bipartite mark of the space weave (the ladder is symmetric about 6).

import numpy as np
from itertools import combinations

N = 512
TOL_ZERO = 1e-9


# ---------- (1) the machinery: adjacency-list construction ----------

def laplacian_from_edges(n, edges):
    L = np.zeros((n, n))
    for i, j in edges:
        L[i, i] += 1.0
        L[j, j] += 1.0
        L[i, j] -= 1.0
        L[j, i] -= 1.0
    return L

def ring_edges(n, steps):
    E = set()
    for i in range(n):
        for s in steps:
            E.add((min(i, (i + s) % n), max(i, (i + s) % n)))
    return sorted(E)

def torus2_tri_edges(L1, L2):
    # triangular weave: +-(1,0), +-(0,1), +-(1,1)
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


# ---------- (2) the closed formula: Fourier form ----------

def ring_formula(n, steps):
    k = np.arange(n)
    lam = np.zeros(n)
    for s in steps:
        lam += 2.0 * (1.0 - np.cos(2.0 * np.pi * k * s / n))
    return np.sort(lam)

def torus2_tri_formula(L1, L2):
    k1 = 2.0 * np.pi * np.arange(L1)[:, None] / L1
    k2 = 2.0 * np.pi * np.arange(L2)[None, :] / L2
    lam = (2.0 * (1.0 - np.cos(k1)) + 2.0 * (1.0 - np.cos(k2))
           + 2.0 * (1.0 - np.cos(k1 + k2)))
    return np.sort(lam.ravel())

def torus3_formula(L):
    k = 2.0 * np.pi * np.arange(L) / L
    one = 2.0 * (1.0 - np.cos(k))
    lam = (one[:, None, None] + one[None, :, None] + one[None, None, :])
    return np.sort(lam.ravel())


# ---------- helpers ----------

def ladder_report(lam, head=6):
    """Collected into shelves: the start of the (value, width) pairs"""
    shelves = []
    for v in lam:
        if shelves and abs(v - shelves[-1][0]) < 1e-8:
            shelves[-1][1] += 1
        else:
            shelves.append([v, 1])
    return shelves[:head], len(shelves)

def check_pair(name, lam_machine, lam_formula, report, trip=None):
    diff = float(np.max(np.abs(lam_machine - lam_formula)))
    trace = float(np.sum(lam_machine))
    zeros = int(np.sum(lam_machine < TOL_ZERO))
    report.append((name, trace, zeros, diff, trip))
    return diff


report = []

# --- J1 (line), J2 (plane 16x32), J3 (space 8x8x8), plane control 8x64 ---
J1_m = np.sort(np.linalg.eigvalsh(laplacian_from_edges(N, ring_edges(N, (1, 2, 3)))))
J1_f = ring_formula(N, (1, 2, 3))
check_pair("J1 line (1,2,3)", J1_m, J1_f, report)

J2_m = np.sort(np.linalg.eigvalsh(laplacian_from_edges(N, torus2_tri_edges(16, 32))))
J2_f = torus2_tri_formula(16, 32)
check_pair("J2 plane 16x32", J2_m, J2_f, report)

J3_m = np.sort(np.linalg.eigvalsh(laplacian_from_edges(N, torus3_edges(8))))
J3_f = torus3_formula(8)
check_pair("J3 space 8x8x8", J3_m, J3_f, report)

C1_m = np.sort(np.linalg.eigvalsh(laplacian_from_edges(N, torus2_tri_edges(8, 64))))
C1_f = torus2_tri_formula(8, 64)
check_pair("plane control 8x64", C1_m, C1_f, report)

# --- scan of the line family: every (a,b,c), a<b<c<=12 ---
scan = {}
for trip in combinations(range(1, 13), 3):
    lam_f = ring_formula(N, trip)
    lam_m = np.sort(np.linalg.eigvalsh(laplacian_from_edges(N, ring_edges(N, trip))))
    check_pair(f"line {trip}", lam_m, lam_f, report, trip=trip)
    scan[trip] = lam_f

# ---------- self-checks ----------

print("== 1. trace sum and machine agreement (on all %d networks) ==" % len(report))
traces = [r[1] for r in report]
diffs = [r[3] for r in report]
print("trace sum min/max: %.12f / %.12f (prescribed: 3072)" % (min(traces), max(traces)))
print("largest machinery-formula deviation: %.3e" % max(diffs))

print("\n== 2. zero modes ==")
from math import gcd
bad = []
for name, tr, z, d, trip in report:
    if trip is not None:
        g = gcd(gcd(trip[0], trip[1]), gcd(trip[2], N))
        assert z == g, (name, z, g)
        if z > 1:
            bad.append((trip, z))
    else:
        print("  %-20s zero modes: %d" % (name, z))
print("  scan members with 1 zero mode: %d" % sum(
    1 for n_, t_, z_, d_, tr_ in report if tr_ is not None and z_ == 1))
print("  scan members with >1 zero mode (disconnected weaves): %d" % len(bad))
for trip, z in sorted(bad):
    print("    %s -> %d components" % (str(trip), z))

print("\n== 3. the bipartite mark of space: the J3 ladder is symmetric about 6 ==")
sym3 = float(np.max(np.abs(np.sort(12.0 - J3_f) - J3_f)))
sym1 = float(np.max(np.abs(np.sort(12.0 - J1_f) - J1_f)))
sym2 = float(np.max(np.abs(np.sort(12.0 - J2_f) - J2_f)))
print("J3 symmetry deviation: %.3e (prescribed: 0)" % sym3)
print("J1 symmetry deviation: %.3f, J2: %.3f (prescribed: nonzero)" % (sym1, sym2))

print("\n== 4. ladders (shelf: value x width), first 6 shelves + shelf count ==")
for name, lam in [("J1 line", J1_f), ("J2 plane", J2_f), ("J3 space", J3_f),
                  ("control 8x64", C1_f)]:
    head, nsh = ladder_report(lam)
    s = "; ".join("%.4g x%d" % (v, m) for v, m in head)
    print("  %-14s %s ... (%d shelves)  max: %.6g" % (name, s, nsh, lam[-1]))

print("\n== 5. degree boundaries of J3 (cumulative filling of the closed degrees) ==")
head, _ = ladder_report(J3_f, head=99)
cum = 0
marks = []
for v, m in head:
    cum += m
    marks.append("up to %g: %d" % (round(v, 4), cum))
print("  " + "; ".join(marks))

print("\n== 6. ladder classes of the scan ==")
classes = {}
for trip, lam in scan.items():
    key = tuple(np.round(lam, 9))
    classes.setdefault(key, []).append(trip)
print("  the %d family members fall into %d distinct ladders" % (len(scan), len(classes)))
multi = sorted([v for v in classes.values() if len(v) > 1], key=len, reverse=True)
print("  largest coinciding classes:")
for grp in multi[:5]:
    print("    %s (%d members)" % (", ".join(map(str, grp)), len(grp)))
