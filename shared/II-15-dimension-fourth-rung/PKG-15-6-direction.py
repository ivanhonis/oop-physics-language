# PKG-15-6 — The direction theorem (II/15)
# Target claim (point 1): for every lower-vs-higher extension candidate pair an
# explicit N* threshold up to which the beat-by-beat dominance holds, and thus
# the lower extension is strictly cheaper over the stretch 2..N*.
# Two layers (H2):
#   ANALYTIC: the chain of lemmas 5-7 — ordering lemma + inversion lemma +
#     sandwich lemma [(4/pi^2)*Q(k) <= lambda(k) <= Q(k), where Q is the
#     stiffness form with folded-back phases] — hence the certificate:
#     if Q_X(i) <= (4/pi^2)*Q_Y(i), then lambda_X(i) <= lambda_Y(i).
#     N*-analytic = the index before the first violation.
#   MACHINE: N*-machine = the longest stretch on which lambda_X(i) <= lambda_Y(i)
#     holds exactly on the fixed system; from there the ordering lemma gives
#     price dominance over the whole stretch 2..N*-machine.
# To be reported: the dominance gap (H4) — the distance of N*-machine from the
# measured price tipping.

# Identifier glossary — the identifiers were renamed from Hungarian
# to English; the original Hungarian name stands on the right:
#   coverage = fed    EXTENSION = KIT   folded = vissza   grids = racsok
#   half_steps = fel  J2_STEPS = J2LEP  J3_STEPS = J3LEP  ladders = letrak
#   MAIN = FO         name = nev        pairs = parok     phase = fazis
#   ratio = ar        result = eredm    SANDWICH = SANDW  shape = alak
#   strict = szig     tipping = at      UNIT4 = EGYSEG4   worst = rossz

import numpy as np

N = 20736
UNIT4 = [(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)]
J3_STEPS = [(1,0,0),(0,1,0),(0,0,1),(1,-1,-1)]
J2_STEPS = [(1,0),(0,1),(1,1),(1,-1)]
MAIN = {"J1": ((N,), [(1,),(2,),(3,),(4,)]), "J2": ((144,144), J2_STEPS),
      "J3": ((24,24,36), J3_STEPS), "J4": ((12,12,12,12), UNIT4)}
EXTENSION = {"J1": 1, "J2": 2, "J3": 3, "J4": 4}
SANDWICH = 4.0/np.pi**2

def ladders(name):
    shape, half_steps = MAIN[name]
    dt = np.longdouble
    grids = np.meshgrid(*[(2*np.pi*np.arange(L)).astype(dt)/L for L in shape],
                         indexing="ij")
    lam = np.zeros(shape, dtype=dt)
    q = np.zeros(shape, dtype=dt)
    for s in half_steps:
        phase = sum(si*gi for si, gi in zip(s, grids))
        folded = (phase + np.pi) % (2*np.pi) - np.pi     # [-pi, pi)
        lam += 2.0 - 2.0*np.cos(phase)
        q += folded**2
    return np.sort(lam.ravel()), np.sort(q.ravel())

print("== PKG-15-6 — the two layers of the direction theorem ==")
L_, Q_ = {}, {}
for name in MAIN:
    L_[name], Q_[name] = ladders(name)

# machine certification of the sandwich lemma (checking lemma 7)
worst = 0.0
for name in MAIN:
    lam, q = ladders(name)  # no sorted pairing needed: it must hold pointwise
for name in MAIN:
    shape, half_steps = MAIN[name]
    dt = np.longdouble
    grids = np.meshgrid(*[(2*np.pi*np.arange(Lx)).astype(dt)/Lx for Lx in shape],
                         indexing="ij")
    lam = np.zeros(shape, dtype=dt); q = np.zeros(shape, dtype=dt)
    for s in half_steps:
        phase = sum(si*gi for si, gi in zip(s, grids))
        folded = (phase + np.pi) % (2*np.pi) - np.pi
        lam += 2.0 - 2.0*np.cos(phase); q += folded**2
    m = q.ravel() > 1e-15
    ratio = (lam.ravel()[m]/q.ravel()[m]).astype(float)
    worst = max(worst, float(max(np.max(ratio) - 1.0, SANDWICH - np.min(ratio))))
print("sandwich lemma on the full lattice: largest violation %.2e — %s"
      % (worst, "HOLDS" if worst < 1e-12 else "FAILS"))

pairs = [(x, y) for x in MAIN for y in MAIN if EXTENSION[x] < EXTENSION[y]]
print("\npair       N*-analytic    N*-machine  price tipping   coverage   strict")
result = {}
for x, y in pairs:
    # analytic certificate
    j = np.where(Q_[x][1:] > SANDWICH*Q_[y][1:])[0]
    na = int(j[0]) + 1 if len(j) else N
    # machine threshold
    j = np.where(L_[x][1:] > L_[y][1:] + 1e-12)[0]
    ng = int(j[0]) + 1 if len(j) else N
    # strictness over the stretch 2..ng
    strict = bool(np.any(L_[x][1:ng] < L_[y][1:ng] - 1e-9))
    # price tipping
    cx, cy = np.cumsum(L_[x]), np.cumsum(L_[y])
    j = np.where(cx[1:] > cy[1:] + 1e-8)[0]
    tipping = int(j[0]) + 2 if len(j) else None
    coverage = (100.0*ng/tipping) if tipping else 100.0
    result[(x, y)] = (na, ng, tipping, coverage, strict)
    print("%s-%s      %8d   %8d   %10s   %8.1f%%   %s"
          % (x, y, na, ng, tipping if tipping else "none", coverage, "holds" if strict else "NO"))

# direct check of the consequence of the ordering lemma: price order on 2..N*-machine
print("\ncounter-check (ordering lemma): price dominance on the certified stretch:")
for (x, y), (na, ng, tipping, coverage, strict) in result.items():
    cx, cy = np.cumsum(L_[x]), np.cumsum(L_[y])
    ok = bool(np.all(cx[1:ng] <= cy[1:ng] + 1e-9))
    print("   %s-%s: 2..%d — %s" % (x, y, ng, "holds" if ok else "FAILS"))
