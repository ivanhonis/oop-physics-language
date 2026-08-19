# PKG-13-2 — Computation code for the beat ladders
# Package document: PKG-13-2-ladders_hu.md / _en.md (the code is language-independent)
# Output: the ladders of the three candidates and of the complete line-family
# scan, with the self-checks of point 6 of the package.

import math
import numpy as np
from itertools import combinations

N = 16

def circulant_L(steps):
    """Contract matrix of the 16-site weave (a ring with the given step pairs)."""
    L = np.zeros((N, N))
    for i in range(N):
        for s in steps:
            for j in ((i + s) % N, (i - s) % N):
                L[i, j] -= 1.0
        L[i, i] = 2 * len(steps)
    return L

def analytic_circ(steps):
    """The same from the closed formula — an independent check."""
    ks = np.arange(N)
    lam = np.zeros(N)
    for s in steps:
        lam += 2 - 2 * np.cos(2 * np.pi * s * ks / N)
    return np.sort(lam)

def torus_L():
    """Contract matrix of the 4x4 lattice with periodic boundary (plane candidate)."""
    L = np.zeros((N, N))
    def idx(x, y):
        return 4 * x + y
    for x in range(4):
        for y in range(4):
            i = idx(x, y)
            for j in (idx((x + 1) % 4, y), idx((x - 1) % 4, y),
                      idx(x, (y + 1) % 4), idx(x, (y - 1) % 4)):
                L[i, j] -= 1.0
            L[i, i] = 4.0
    return L

def spec(L):
    return np.sort(np.linalg.eigvalsh(L))

# --- the three candidates ---
J1 = spec(circulant_L([1, 2]))
J2 = spec(torus_L())
J3 = spec(circulant_L([2, 4]))          # = two separate, thickened 8-rings
J3_direct = np.sort(np.concatenate([    # independent construction: 2 x C8(1,2)
    np.sort([(2 - 2 * np.cos(2 * np.pi * 1 * k / 8))
             + (2 - 2 * np.cos(2 * np.pi * 2 * k / 8)) for k in range(8)])
] * 2))

print("J1 (line, C16(1,2)):        ", np.round(J1, 4))
print("J2 (plane/torus, C4xC4):    ", np.round(J2, 4))
print("J3 (segmented, 2xC8(1,2)):  ", np.round(J3, 4))

# --- self-checks (package, point 6) ---
print("\nSELF-CHECKS")
print("trace sums (all 64):", round(J1.sum(), 10), round(J2.sum(), 10), round(J3.sum(), 10))
print("zero modes (J1,J2,J3):", int((J1 < 1e-9).sum()), int((J2 < 1e-9).sum()), int((J3 < 1e-9).sum()))
print("J1 analytic vs machinery, largest deviation:", np.max(np.abs(J1 - analytic_circ([1, 2]))))
print("J3 by its two constructions, largest deviation:", np.max(np.abs(J3 - J3_direct)))
q4 = np.sort(np.concatenate([[2 * j] * math.comb(4, j) for j in range(5)]))
print("J2 == binomial ladder of the hypercube? largest deviation:", np.max(np.abs(J2 - q4)))

# --- obligatory scan: all 21 members of the line family ---
print("\nSCAN: C16(a,b), 1<=a<b<=7")
classes = {}
for a, b in combinations(range(1, 8), 2):
    lam = np.round(spec(circulant_L([a, b])), 6)
    zero = int((lam < 1e-9).sum())
    classes.setdefault(tuple(lam), []).append((a, b, zero))
print(f"members: {sum(len(v) for v in classes.values())}, distinct ladders: {len(classes)}")
for key, members in sorted(classes.items(), key=lambda kv: kv[0]):
    lam = np.array(key)
    tags = ", ".join(f"({a},{b})" for a, b, _ in members)
    zero = members[0][2]
    print(f"  steps {tags}: zero-modes={zero}, ladder starts {np.round(lam[:5], 3)}, trace={round(lam.sum(), 6)}")
