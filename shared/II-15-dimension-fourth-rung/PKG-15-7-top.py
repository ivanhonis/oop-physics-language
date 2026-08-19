# PKG-15-7 — A teto-tetel (II/15)
# Osszerakas, uj bizonyitas nelkul: az irany-tetel (PKG-15-6, I2: a ter-
# negykiterjedes paron N* = 2087) + a lyuk-tukor tetel (PKG-15-5) egyutt adja:
#   TETO-TETEL: a 18649 <= N <= 20734 szakaszon a ter ara szigoruan kisebb a
#   negykiterjedesenel; N = 20735-nel egzakt holtverseny.
# (18649 = 20736 - 2087; a szigorusag az irany-tetel szigorusaganak tukre.)
# Ellenorzesek:
#   E1  direkt ar-osszevetes a tetel-szakaszon (szigoru dominancia)
#   E2  az egy-lyukas egzakt holtverseny (N = 20735)
#   E3  a tukor-atvitel egzaktsaga a szakaszon: dAr(N) = dAr(20736 - N)
#   E4  lefedettseg: a tanusitott szakasz aranya a mert paronkenti felso
#       tartomanyban (15997..20734)

import numpy as np

N = 20736
NCSILLAG = 2087                    # PKG-15-6, I2
ALSO, FELSO = N - NCSILLAG, N - 2  # 18649 .. 20734
MERT_KEZDET = 15997                # PKG-15-3 / PKG-15-6

def letra(alak, fel):
    dt = np.longdouble
    racsok = np.meshgrid(*[(2*np.pi*np.arange(L)).astype(dt)/L for L in alak],
                         indexing="ij")
    lam = np.zeros(alak, dtype=dt)
    for s in fel:
        lam += 2.0 - 2.0*np.cos(sum(si*gi for si, gi in zip(s, racsok)))
    return np.sort(lam.ravel())

print("== PKG-15-7 — a teto-tetel ellenorzesei ==")
c3 = np.cumsum(letra((24,24,36), [(1,0,0),(0,1,0),(0,0,1),(1,-1,-1)]))
c4 = np.cumsum(letra((12,12,12,12),
                     [(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)]))
d = c4 - c3                        # pozitiv, ha a ter olcsobb

# E1 — szigoru dominancia a tetel-szakaszon
szakasz = d[ALSO-1:FELSO]          # N = 18649 .. 20734
legkisebb = float(np.min(szakasz))
print("E1 a tetel-szakaszon (N = %d..%d) a ter szigoruan olcsobb: "
      "legkisebb elony %.6f — %s"
      % (ALSO, FELSO, legkisebb, "ALL" if legkisebb > 1e-9 else "BUKIK"))

# E2 — egy-lyukas holtverseny
print("E2 egy-lyukas holtverseny: |dAr(20735)| = %.2e — %s"
      % (abs(float(d[N-2])), "ALL" if abs(float(d[N-2])) < 1e-9 else "BUKIK"))

# E3 — a tukor-atvitel egzaktsaga a szakaszon
tukor = d[np.arange(ALSO, FELSO+1)-1] - d[N - np.arange(ALSO, FELSO+1) - 1]
e3 = float(np.max(np.abs(tukor)))
print("E3 tukor-atvitel a szakaszon: legnagyobb elteres %.2e — %s"
      % (e3, "ALL" if e3 < 1e-9 else "BUKIK"))

# E4 — lefedettseg a mert paronkenti felso tartomanyban
tanusitott = FELSO - ALSO + 1
mert = FELSO - MERT_KEZDET + 1
print("E4 lefedettseg: tanusitott %d toltes a mert %d-bol = %.1f%%; "
      "a mert tartomany maradeka (%d..%d) mert marad"
      % (tanusitott, mert, 100.0*tanusitott/mert, MERT_KEZDET, ALSO-1))

# raadas: a tetel-szakasz teljes egeszeben a ter mert gyoztes-savjaban ul
print("konzisztencia: a tanusitott szakasz a mert ter-sav (15997..20734) "
      "resze: %s" % ("ALL" if ALSO >= MERT_KEZDET else "BUKIK"))
