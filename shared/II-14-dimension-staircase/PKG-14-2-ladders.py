# PKG-14-2 — Az ütem-létrák (II/14, kiterjedés-lépcső)
# Minden létra két független úton:
#   (1) gépezet: a szerződésháló szomszédlistás mátrixának sajátfeladata
#   (2) zárt képlet: a szövések Fourier-alakja
# Önellenőrzések: nyomösszeg (3072), nulla-módusok, gépi egyezés,
# a tér-szövés páros-jegye (a létra a 6 körül szimmetrikus).

import numpy as np
from itertools import combinations

N = 512
TOL_ZERO = 1e-9


# ---------- (1) a gépezet: szomszédlistás felépítés ----------

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
    # háromszög-szövés: ±(1,0), ±(0,1), ±(1,1)
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


# ---------- (2) a zárt képlet: Fourier-alak ----------

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


# ---------- segédek ----------

def ladder_report(lam, head=6):
    """polcokra fogva: (érték, szélesség) párok eleje"""
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

# --- J1 (vonal), J2 (sík 16x32), J3 (tér 8x8x8), sík-kontroll 8x64 ---
J1_m = np.sort(np.linalg.eigvalsh(laplacian_from_edges(N, ring_edges(N, (1, 2, 3)))))
J1_f = ring_formula(N, (1, 2, 3))
check_pair("J1 vonal (1,2,3)", J1_m, J1_f, report)

J2_m = np.sort(np.linalg.eigvalsh(laplacian_from_edges(N, torus2_tri_edges(16, 32))))
J2_f = torus2_tri_formula(16, 32)
check_pair("J2 sik 16x32", J2_m, J2_f, report)

J3_m = np.sort(np.linalg.eigvalsh(laplacian_from_edges(N, torus3_edges(8))))
J3_f = torus3_formula(8)
check_pair("J3 ter 8x8x8", J3_m, J3_f, report)

C1_m = np.sort(np.linalg.eigvalsh(laplacian_from_edges(N, torus2_tri_edges(8, 64))))
C1_f = torus2_tri_formula(8, 64)
check_pair("sik-kontroll 8x64", C1_m, C1_f, report)

# --- a vonal-csalad pasztazasa: minden (a,b,c), a<b<c<=12 ---
scan = {}
for trip in combinations(range(1, 13), 3):
    lam_f = ring_formula(N, trip)
    lam_m = np.sort(np.linalg.eigvalsh(laplacian_from_edges(N, ring_edges(N, trip))))
    check_pair(f"vonal {trip}", lam_m, lam_f, report, trip=trip)
    scan[trip] = lam_f

# ---------- önellenőrzések ----------

print("== 1. nyomösszeg és gépi egyezés (mind a %d hálón) ==" % len(report))
traces = [r[1] for r in report]
diffs = [r[3] for r in report]
print("nyomösszeg min/max: %.12f / %.12f (előírt: 3072)" % (min(traces), max(traces)))
print("legnagyobb gépezet–képlet eltérés: %.3e" % max(diffs))

print("\n== 2. nulla-módusok ==")
from math import gcd
bad = []
for name, tr, z, d, trip in report:
    if trip is not None:
        g = gcd(gcd(trip[0], trip[1]), gcd(trip[2], N))
        assert z == g, (name, z, g)
        if z > 1:
            bad.append((trip, z))
    else:
        print("  %-20s nulla-módus: %d" % (name, z))
print("  pásztázók 1 nulla-módussal: %d db" % sum(
    1 for n_, t_, z_, d_, tr_ in report if tr_ is not None and z_ == 1))
print("  pásztázók >1 nulla-módussal (széteső szövések): %d db" % len(bad))
for trip, z in sorted(bad):
    print("    %s -> %d komponens" % (str(trip), z))

print("\n== 3. a tér páros-jegye: a J3-létra a 6 körül szimmetrikus ==")
sym3 = float(np.max(np.abs(np.sort(12.0 - J3_f) - J3_f)))
sym1 = float(np.max(np.abs(np.sort(12.0 - J1_f) - J1_f)))
sym2 = float(np.max(np.abs(np.sort(12.0 - J2_f) - J2_f)))
print("J3 szimmetria-eltérés: %.3e (előírt: 0)" % sym3)
print("J1 szimmetria-eltérés: %.3f, J2: %.3f (előírt: nem nulla)" % (sym1, sym2))

print("\n== 4. létrák (polc: érték x szélesség), első 6 polc + polcszám ==")
for name, lam in [("J1 vonal", J1_f), ("J2 sik", J2_f), ("J3 ter", J3_f),
                  ("kontroll 8x64", C1_f)]:
    head, nsh = ladder_report(lam)
    s = "; ".join("%.4g x%d" % (v, m) for v, m in head)
    print("  %-14s %s ... (%d polc)  max: %.6g" % (name, s, nsh, lam[-1]))

print("\n== 5. J3 fokhatárai (zárt fokok kumulált betöltése) ==")
head, _ = ladder_report(J3_f, head=99)
cum = 0
marks = []
for v, m in head:
    cum += m
    marks.append("%g-ig: %d" % (round(v, 4), cum))
print("  " + "; ".join(marks))

print("\n== 6. a pásztázás létra-osztályai ==")
classes = {}
for trip, lam in scan.items():
    key = tuple(np.round(lam, 9))
    classes.setdefault(key, []).append(trip)
print("  a %d családtag %d különböző létrába esik" % (len(scan), len(classes)))
multi = sorted([v for v in classes.values() if len(v) > 1], key=len, reverse=True)
print("  legnagyobb egybeeső osztályok:")
for grp in multi[:5]:
    print("    %s (%d tag)" % (", ".join(map(str, grp)), len(grp)))
