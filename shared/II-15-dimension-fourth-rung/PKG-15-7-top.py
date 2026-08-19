# PKG-15-7 — The top theorem (II/15)
# Assembly, with no new proof: the direction theorem (PKG-15-6, I2: on the
# space-four-extension pair N* = 2087) + the hole-mirror theorem (PKG-15-5)
# together give:
#   TOP THEOREM: over the stretch 18649 <= N <= 20734 the price of space is
#   strictly smaller than that of four extensions; at N = 20735 an exact tie.
# (18649 = 20736 - 2087; the strictness is the mirror of the direction theorem's.)
# Checks:
#   E1  direct price comparison on the theorem stretch (strict dominance)
#   E2  the single-hole exact tie (N = 20735)
#   E3  exactness of the mirror transfer on the stretch: dPrice(N) = dPrice(20736 - N)
#   E4  coverage: the share of the certified stretch in the measured pairwise
#       upper range (15997..20734)

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

print("== PKG-15-7 — checks of the top theorem ==")
c3 = np.cumsum(letra((24,24,36), [(1,0,0),(0,1,0),(0,0,1),(1,-1,-1)]))
c4 = np.cumsum(letra((12,12,12,12),
                     [(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)]))
d = c4 - c3                        # positive if space is the cheaper one

# E1 — strict dominance on the theorem stretch
szakasz = d[ALSO-1:FELSO]          # N = 18649 .. 20734
legkisebb = float(np.min(szakasz))
print("E1 on the theorem stretch (N = %d..%d) space is strictly cheaper: "
      "smallest advantage %.6f — %s"
      % (ALSO, FELSO, legkisebb, "HOLDS" if legkisebb > 1e-9 else "FAILS"))

# E2 — single-hole tie
print("E2 single-hole tie: |dPrice(20735)| = %.2e — %s"
      % (abs(float(d[N-2])), "HOLDS" if abs(float(d[N-2])) < 1e-9 else "FAILS"))

# E3 — exactness of the mirror transfer on the stretch
tukor = d[np.arange(ALSO, FELSO+1)-1] - d[N - np.arange(ALSO, FELSO+1) - 1]
e3 = float(np.max(np.abs(tukor)))
print("E3 mirror transfer on the stretch: largest deviation %.2e — %s"
      % (e3, "HOLDS" if e3 < 1e-9 else "FAILS"))

# E4 — coverage in the measured pairwise upper range
tanusitott = FELSO - ALSO + 1
mert = FELSO - MERT_KEZDET + 1
print("E4 coverage: %d certified fillings out of the measured %d = %.1f%%; "
      "the remainder of the measured range (%d..%d) stays measured"
      % (tanusitott, mert, 100.0*tanusitott/mert, MERT_KEZDET, ALSO-1))

# bonus: the theorem stretch sits entirely inside the measured winning band of space
print("consistency: the certified stretch is part of the measured space band "
      "(15997..20734): %s" % ("HOLDS" if ALSO >= MERT_KEZDET else "FAILS"))
