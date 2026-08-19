# PKG-15-5 — Machine confirmation of the hole-mirror theorem (II/15)
# The theorem: between two weaves carrying the bipartite mark (same site count,
# same number of contracts per site) the cost difference at any filling N equals
# the cost difference at the mirror filling N' = Nsite - N.
# Checks:
#   E1  the mirror identity on the J3-J4 pair (and on the J4-K3 pair) at machine precision
#   E2  consequence: an exact bipartite tie at N = 20735
#   E3  consequence: the peak beat is exactly 16 on every entrant carrying the bipartite mark
#   E4  the sign-change positions of J3-J4 form mirror pairs
#   E5  negative control: on a non-bipartite pair (J1-J2) the identity does NOT hold
#       (the bipartite condition is necessary)

import numpy as np

N = 20736
EGYSEG4 = [(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)]
J3LEP = [(1,0,0),(0,1,0),(0,0,1),(1,-1,-1)]
J2LEP = [(1,0),(0,1),(1,1),(1,-1)]
FO = {
    "J1": ((N,),          [(1,),(2,),(3,),(4,)]),
    "J2": ((144,144),     J2LEP),
    "J3": ((24,24,36),    J3LEP),
    "J4": ((12,12,12,12), EGYSEG4),
    "K1": ((16,36,36),    J3LEP),
    "K2": ((12,36,48),    J3LEP),
    "K3": ((8,8,18,18),   EGYSEG4),
}

def letra(nev, dt=np.longdouble):
    alak, fel = FO[nev]
    racsok = np.meshgrid(*[(2*np.pi*np.arange(L)).astype(dt)/L for L in alak],
                         indexing="ij")
    lam = np.zeros(alak, dtype=dt)
    for s in fel:
        lam += 2.0 - 2.0*np.cos(sum(si*gi for si, gi in zip(s, racsok)))
    return np.sort(lam.ravel())

def tukor_hiba(a, b):
    """max |dPrice(N) - dPrice(N')| over the range N = 1..20735."""
    R = (np.cumsum(letra(a)) - np.cumsum(letra(b)))[:N-1]
    return float(np.max(np.abs(R - R[::-1]))), R

print("== PKG-15-5 — machine confirmation of the hole-mirror theorem ==")

# E1 — mirror identity on bipartite pairs
e_j34, R34 = tukor_hiba("J4", "J3")
e_j4k3, _ = tukor_hiba("J4", "K3")
print("E1 mirror identity: |dPrice(N)-dPrice(N')| at most %.2e (J3-J4), "
      "%.2e (J4-K3) — %s" % (e_j34, e_j4k3,
      "HOLDS" if max(e_j34, e_j4k3) < 1e-9 else "FAILS"))

# E2 — exact tie at a single hole
kolt = {nev: np.cumsum(letra(nev)) for nev in ("J3", "J4")}
d = float(abs(kolt["J3"][N-2] - kolt["J4"][N-2]))
print("E2 single-hole tie: |Price_J3 - Price_J4| at the filling N = %d = %.2e — %s"
      % (N-1, d, "HOLDS" if d < 1e-9 else "FAILS"))

# E3 — the peak beat is exactly 16 on the bipartite entrants (the mirror of the zero mode)
print("E3 peak beat on the bipartite entrants:")
for nev in ("J3", "J4", "K1", "K2", "K3"):
    m = float(letra(nev)[-1])
    print("   %s: %.12f — %s" % (nev, m, "HOLDS" if abs(m-16) < 1e-9 else "FAILS"))

# E4 — do the J3-J4 sign changes form mirror pairs
elojel = np.sign(np.where(np.abs(R34) > 1e-8, R34, 0))
valt = [int(n+1) for n in range(1, N-1)
        if elojel[n] != 0 and elojel[n-1] != 0 and elojel[n] != elojel[n-1]]
parok = all(valt[i] + valt[len(valt)-1-i] == N + 1 for i in range(len(valt)))
print("E4 sign-change positions (price of J4 - price of J3): %s — mirror pairs: %s"
      % (valt, "HOLDS" if parok else "check it"))

# E5 — negative control: on a non-bipartite pair the identity does not hold
e_j12, _ = tukor_hiba("J1", "J2")
print("E5 negative control (J1-J2, non-bipartite): the mirror deviation is at most "
      "%.3f — the bipartite condition is necessary: %s"
      % (e_j12, "HOLDS" if e_j12 > 1.0 else "FAILS"))
