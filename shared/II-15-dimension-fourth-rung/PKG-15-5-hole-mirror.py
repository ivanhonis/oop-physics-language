# PKG-15-5 — A lyuk-tukor tetel gepi megerositese (II/15)
# A tetel: ket paros-jegyu szoves kozt (azonos helyszam, helyenkent azonos
# szerzodesszam) barmely N toltesen a koltsegkulonbseg egyenlo az
# N' = Nsite - N tukortoltesen vett koltsegkulonbseggel.
# Ellenorzesek:
#   E1  a tukor-azonossag a J3-J4 paron (es a J4-K3 paron) gepi pontossagon
#   E2  kovetkezmeny: N = 20735-nel egzakt paros holtverseny
#   E3  kovetkezmeny: a csucs-utem minden paros-jegyu indulon pontosan 16
#   E4  a J3-J4 elojelvaltasi helyei tukorparok
#   E5  negativ kontroll: nem-paros paron (J1-J2) az azonossag NEM all
#       (a paros feltetel szukseges)

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
    """max |dAr(N) - dAr(N')| az N = 1..20735 tartomanyon."""
    R = (np.cumsum(letra(a)) - np.cumsum(letra(b)))[:N-1]
    return float(np.max(np.abs(R - R[::-1]))), R

print("== PKG-15-5 — a lyuk-tukor tetel gepi megerositese ==")

# E1 — tukor-azonossag paros parokon
e_j34, R34 = tukor_hiba("J4", "J3")
e_j4k3, _ = tukor_hiba("J4", "K3")
print("E1 tukor-azonossag: |dAr(N)-dAr(N')| legfeljebb %.2e (J3-J4), "
      "%.2e (J4-K3) — %s" % (e_j34, e_j4k3,
      "ALL" if max(e_j34, e_j4k3) < 1e-9 else "BUKIK"))

# E2 — egzakt holtverseny egy lyuknal
kolt = {nev: np.cumsum(letra(nev)) for nev in ("J3", "J4")}
d = float(abs(kolt["J3"][N-2] - kolt["J4"][N-2]))
print("E2 egy-lyukas holtverseny: |Ar_J3 - Ar_J4| az N = %d toltesen = %.2e — %s"
      % (N-1, d, "ALL" if d < 1e-9 else "BUKIK"))

# E3 — a csucs-utem a paros indulokon pontosan 16 (a nulla-modus tukre)
print("E3 csucs-utem a paros indulokon:")
for nev in ("J3", "J4", "K1", "K2", "K3"):
    m = float(letra(nev)[-1])
    print("   %s: %.12f — %s" % (nev, m, "ALL" if abs(m-16) < 1e-9 else "BUKIK"))

# E4 — a J3-J4 elojelvaltasok tukorparok-e
elojel = np.sign(np.where(np.abs(R34) > 1e-8, R34, 0))
valt = [int(n+1) for n in range(1, N-1)
        if elojel[n] != 0 and elojel[n-1] != 0 and elojel[n] != elojel[n-1]]
parok = all(valt[i] + valt[len(valt)-1-i] == N + 1 for i in range(len(valt)))
print("E4 elojelvaltasi helyek (J4 ara - J3 ara): %s — tukorparok: %s"
      % (valt, "ALL" if parok else "ellenorizd"))

# E5 — negativ kontroll: nem-paros paron az azonossag nem all
e_j12, _ = tukor_hiba("J1", "J2")
print("E5 negativ kontroll (J1-J2, nem-paros): a tukor-elteres legfeljebb "
      "%.3f — a paros feltetel szukseges: %s"
      % (e_j12, "ALL" if e_j12 > 1.0 else "BUKIK"))
