# PKG-16-5 — Theorem transfer on the bipartite set (II/16)
# The text of the hole-mirror theorem (PKG-15-5) remains valid unchanged: two
# weaves carrying the bipartite mark, with the same site count and the same
# number of contracts per site. The bipartite set here: J5 (native), KP3, KP4
# (bipartite controls), and the six all-odd family members.
# Checks:
#  E1 mirror identity at machine precision on the four key pairs
#  E2 direction thresholds (N*-machine, pointwise dominance) on the bipartite pairs
#  E3 top consequence: on the mirrored stretch the bipartite candidate that is
#     lower in the sparse order is strictly cheaper (with a margin)
#  E4 field consistency: the full-end winners of the whole field are read from
#     the saved race state — we expect the mirror of the sparse order
#
# Note: this script reads verseny16_allapot.npz, which is produced by
# PKG-16-3-race.py; run that first.

# Identifier glossary — the identifiers were renamed from Hungarian
# to English; the original Hungarian name stands on the right:
#   closed_ladder = zl  cost = kolt         FAMILY = CSAL
#   half_steps = fel    high = felso        ladders = lad
#   last8 = utolso      low = also          MAIN = FO
#   margin = tart       n_star = ng         name_of = nev
#   NAMES = NEVEK       pairs = parok       shape = alak
#   split = megoszlas   tail = szel

import numpy as np
from itertools import combinations

NH = 12**5
MAIN = {
 "J5": ((12,)*5, [tuple(1 if i==j else 0 for i in range(5)) for j in range(5)]),
 "KP3": ((54,64,72), [(1,0,0),(0,1,0),(0,0,1),(1,-1,-1),(1,-1,1)]),
 "KP4": ((18,24,24,24), [(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1),(0,1,1,1)]),
}
def closed_ladder(shape, half_steps):
    dt = np.longdouble
    r = np.meshgrid(*[(2*np.pi*np.arange(L)).astype(dt)/L for L in shape],
                    indexing="ij")
    lam = np.zeros(shape, dtype=dt)
    for s in half_steps:
        lam += 2.0-2.0*np.cos(sum(si*gi for si,gi in zip(s,r)))
    return np.sort(lam.ravel())

print("== PKG-16-5 — theorem transfer on the bipartite set ==")
ladders = {n: closed_ladder(*MAIN[n]) for n in MAIN}
kk = (2*np.pi*np.arange(NH)).astype(np.longdouble)/NH
ladders["V"] = np.sort(sum(2.0-2.0*np.cos(s*kk) for s in (1,3,5,7,9)))
cost = {n: np.cumsum(l) for n, l in ladders.items()}

pairs = [("KP3","KP4"),("KP3","J5"),("KP4","J5"),("V","KP3")]
print("E1 mirror identity and E2-E3 on the pairs:")
for x, y in pairs:
    R = (cost[y]-cost[x])[:NH-1]
    e1 = float(np.max(np.abs(R - R[::-1])))
    j = np.where(ladders[x][1:] > ladders[y][1:] + 1e-12)[0]
    n_star = int(j[0])+1 if len(j) else NH
    low, high = NH-n_star, NH-2
    margin = float(np.min((cost[y]-cost[x])[low-1:high]))
    print("  %s-%s: mirror deviation %.2e | N*-machine %d | top stretch %d..%d, "
          "smallest advantage %.4f — %s"
          % (x, y, e1, n_star, low, high, margin,
             "HOLDS" if e1 < 1e-8 and margin > 1e-9 else "FAILS"))
d = float(abs(cost["KP3"][NH-2]-cost["J5"][NH-2]))
print("  single-hole bipartite tie (KP3-J5): %.2e — %s"
      % (d, "HOLDS" if d < 1e-8 else "FAILS"))

A = np.load("verseny16_allapot.npz")
bid, b1, b2 = A["bid"], A["best1"], A["best2"]
NAMES = ["J1","J2","J3","J4","J5","K1","K2","K3","KA2","KA3","KA4","KP3","KP4"]
FAMILY = list(combinations(range(1,13),5))
def name_of(i): return NAMES[i] if i < 13 else str(FAMILY[i-13])
print("\nE4 full-end winners of the whole field (last 2000 fillings):")
tail = bid[-2001:-1]
split = {}
for i in tail:
    split[name_of(int(i))] = split.get(name_of(int(i)), 0) + 1
print("  ", dict(sorted(split.items(), key=lambda x: -x[1])[:5]))
last8 = [name_of(int(bid[NH-1-m])) for m in range(1, 9)]
print("   winners of the last 8 fillings (the full end): %s" % last8)
