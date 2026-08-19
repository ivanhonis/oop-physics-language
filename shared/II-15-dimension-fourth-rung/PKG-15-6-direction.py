# PKG-15-6 — Az irany-tetel (II/15)
# Cel-allitas (1. pont): minden kisebb-nagyobb kiterjedesu jelolt-parra
# explicit N* kuszob, ameddig az utemenkenti dominancia all, es igy a kisebb
# kiterjedesu szigoruan olcsobb a 2..N* szakaszon.
# Ket reteg (H2):
#   ANALITIKUS: az 5-7. lemmak lancolata — rendezesi lemma + atforditasi
#     lemma + szendvics-lemma [(4/pi^2)·Q(k) <= lambda(k) <= Q(k), ahol Q a
#     visszahajtott fazisu merevseg-alak] — ebbol tanusitvany:
#     ha Q_X(i) <= (4/pi^2)·Q_Y(i), akkor lambda_X(i) <= lambda_Y(i).
#     N*-analitikus = az elso serules elotti index.
#   GEPI: N*-gepi = a leghosszabb szakasz, amelyen lambda_X(i) <= lambda_Y(i)
#     egzaktul all a rogzitett rendszeren; a rendezesi lemma innen ad
#     ar-dominanciat a teljes 2..N*-gepi szakaszon.
# Jelentendo: a dominancia-hezag (H4) — N*-gepi tavolsaga a mert ar-atbillenestol.

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

print("== PKG-15-6 — az irany-tetel ket retege ==")
L_, Q_ = {}, {}
for nev in FO:
    L_[nev], Q_[nev] = letrak(nev)

# szendvics-lemma gepi hitelesitese (a 7. lemma ellenorzese)
rossz = 0.0
for nev in FO:
    lam, q = letrak(nev)  # rendezetlen parositas nem kell: pontonkent kell
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
print("szendvics-lemma a teljes racson: legnagyobb sertes %.2e — %s"
      % (rossz, "ALL" if rossz < 1e-12 else "BUKIK"))

parok = [(x, y) for x in FO for y in FO if KIT[x] < KIT[y]]
print("\npar        N*-analitikus  N*-gepi   ar-atbillenes  lefedettseg  szigoru")
eredm = {}
for x, y in parok:
    # analitikus tanusitvany
    j = np.where(Q_[x][1:] > SANDW*Q_[y][1:])[0]
    na = int(j[0]) + 1 if len(j) else N
    # gepi kuszob
    j = np.where(L_[x][1:] > L_[y][1:] + 1e-12)[0]
    ng = int(j[0]) + 1 if len(j) else N
    # szigorusag a 2..ng szakaszon
    szig = bool(np.any(L_[x][1:ng] < L_[y][1:ng] - 1e-9))
    # ar-atbillenes
    cx, cy = np.cumsum(L_[x]), np.cumsum(L_[y])
    j = np.where(cx[1:] > cy[1:] + 1e-8)[0]
    at = int(j[0]) + 2 if len(j) else None
    fed = (100.0*ng/at) if at else 100.0
    eredm[(x, y)] = (na, ng, at, fed, szig)
    print("%s-%s      %8d   %8d   %10s   %8.1f%%   %s"
          % (x, y, na, ng, at if at else "nincs", fed, "all" if szig else "NEM"))

# a rendezesi lemma kovetkezmenyenek direkt proba ja: ar-sorrend a 2..N*-gepi-n
print("\nellenproba (rendezesi lemma): ar-dominancia a tanusitott szakaszon:")
for (x, y), (na, ng, at, fed, szig) in eredm.items():
    cx, cy = np.cumsum(L_[x]), np.cumsum(L_[y])
    ok = bool(np.all(cx[1:ng] <= cy[1:ng] + 1e-9))
    print("   %s-%s: 2..%d — %s" % (x, y, ng, "all" if ok else "BUKIK"))
