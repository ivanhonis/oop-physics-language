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

import numpy as np

N = 20736
EGYSEG4 = [(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)]
J3LEP = [(1,0,0),(0,1,0),(0,0,1),(1,-1,-1)]
J2LEP = [(1,0),(0,1),(1,1),(1,-1)]
FO = {"J1": ((N,), [(1,),(2,),(3,),(4,)]), "J2": ((144,144), J2LEP),
      "J3": ((24,24,36), J3LEP), "J4": ((12,12,12,12), EGYSEG4)}
KIT = {"J1": 1, "J2": 2, "J3": 3, "J4": 4}
SANDW = 4.0/np.pi**2

def letrak(nev):
    alak, fel = FO[nev]
    dt = np.longdouble
    racsok = np.meshgrid(*[(2*np.pi*np.arange(L)).astype(dt)/L for L in alak],
                         indexing="ij")
    lam = np.zeros(alak, dtype=dt)
    q = np.zeros(alak, dtype=dt)
    for s in fel:
        fazis = sum(si*gi for si, gi in zip(s, racsok))
        vissza = (fazis + np.pi) % (2*np.pi) - np.pi     # [-pi, pi)
        lam += 2.0 - 2.0*np.cos(fazis)
        q += vissza**2
    return np.sort(lam.ravel()), np.sort(q.ravel())

print("== PKG-15-6 — the two layers of the direction theorem ==")
L_, Q_ = {}, {}
for nev in FO:
    L_[nev], Q_[nev] = letrak(nev)

# machine certification of the sandwich lemma (checking lemma 7)
rossz = 0.0
for nev in FO:
    lam, q = letrak(nev)  # no sorted pairing needed: it must hold pointwise
for nev in FO:
    alak, fel = FO[nev]
    dt = np.longdouble
    racsok = np.meshgrid(*[(2*np.pi*np.arange(Lx)).astype(dt)/Lx for Lx in alak],
                         indexing="ij")
    lam = np.zeros(alak, dtype=dt); q = np.zeros(alak, dtype=dt)
    for s in fel:
        fazis = sum(si*gi for si, gi in zip(s, racsok))
        vissza = (fazis + np.pi) % (2*np.pi) - np.pi
        lam += 2.0 - 2.0*np.cos(fazis); q += vissza**2
    m = q.ravel() > 1e-15
    ar = (lam.ravel()[m]/q.ravel()[m]).astype(float)
    rossz = max(rossz, float(max(np.max(ar) - 1.0, SANDW - np.min(ar))))
print("sandwich lemma on the full lattice: largest violation %.2e — %s"
      % (rossz, "HOLDS" if rossz < 1e-12 else "FAILS"))

parok = [(x, y) for x in FO for y in FO if KIT[x] < KIT[y]]
print("\npair       N*-analytic    N*-machine  price tipping   coverage   strict")
eredm = {}
for x, y in parok:
    # analytic certificate
    j = np.where(Q_[x][1:] > SANDW*Q_[y][1:])[0]
    na = int(j[0]) + 1 if len(j) else N
    # machine threshold
    j = np.where(L_[x][1:] > L_[y][1:] + 1e-12)[0]
    ng = int(j[0]) + 1 if len(j) else N
    # strictness over the stretch 2..ng
    szig = bool(np.any(L_[x][1:ng] < L_[y][1:ng] - 1e-9))
    # price tipping
    cx, cy = np.cumsum(L_[x]), np.cumsum(L_[y])
    j = np.where(cx[1:] > cy[1:] + 1e-8)[0]
    at = int(j[0]) + 2 if len(j) else None
    fed = (100.0*ng/at) if at else 100.0
    eredm[(x, y)] = (na, ng, at, fed, szig)
    print("%s-%s      %8d   %8d   %10s   %8.1f%%   %s"
          % (x, y, na, ng, at if at else "none", fed, "holds" if szig else "NO"))

# direct check of the consequence of the ordering lemma: price order on 2..N*-machine
print("\ncounter-check (ordering lemma): price dominance on the certified stretch:")
for (x, y), (na, ng, at, fed, szig) in eredm.items():
    cx, cy = np.cumsum(L_[x]), np.cumsum(L_[y])
    ok = bool(np.all(cx[1:ng] <= cy[1:ng] + 1e-9))
    print("   %s-%s: 2..%d — %s" % (x, y, ng, "holds" if ok else "FAILS"))
