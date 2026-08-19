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

# Identifier glossary — the identifiers were renamed from Hungarian
# to English; the original Hungarian name stands on the right:
#   certified = tanusitott        grids = racsok
#   half_steps = fel              ladder = letra
#   LOWER = ALSO                  measured = mert
#   MEASURED_START = MERT_KEZDET  mirror = tukor
#   N_STAR = NCSILLAG             shape = alak
#   smallest = legkisebb          stretch = szakasz
#   UPPER = FELSO

import numpy as np

N = 20736
N_STAR = 2087                    # PKG-15-6, I2
LOWER, UPPER = N - N_STAR, N - 2  # 18649 .. 20734
MEASURED_START = 15997                # PKG-15-3 / PKG-15-6

def ladder(shape, half_steps):
    dt = np.longdouble
    grids = np.meshgrid(*[(2*np.pi*np.arange(L)).astype(dt)/L for L in shape],
                         indexing="ij")
    lam = np.zeros(shape, dtype=dt)
    for s in half_steps:
        lam += 2.0 - 2.0*np.cos(sum(si*gi for si, gi in zip(s, grids)))
    return np.sort(lam.ravel())

print("== PKG-15-7 — checks of the top theorem ==")
c3 = np.cumsum(ladder((24,24,36), [(1,0,0),(0,1,0),(0,0,1),(1,-1,-1)]))
c4 = np.cumsum(ladder((12,12,12,12),
                     [(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)]))
d = c4 - c3                        # positive if space is the cheaper one

# E1 — strict dominance on the theorem stretch
stretch = d[LOWER-1:UPPER]          # N = 18649 .. 20734
smallest = float(np.min(stretch))
print("E1 on the theorem stretch (N = %d..%d) space is strictly cheaper: "
      "smallest advantage %.6f — %s"
      % (LOWER, UPPER, smallest, "HOLDS" if smallest > 1e-9 else "FAILS"))

# E2 — single-hole tie
print("E2 single-hole tie: |dPrice(20735)| = %.2e — %s"
      % (abs(float(d[N-2])), "HOLDS" if abs(float(d[N-2])) < 1e-9 else "FAILS"))

# E3 — exactness of the mirror transfer on the stretch
mirror = d[np.arange(LOWER, UPPER+1)-1] - d[N - np.arange(LOWER, UPPER+1) - 1]
e3 = float(np.max(np.abs(mirror)))
print("E3 mirror transfer on the stretch: largest deviation %.2e — %s"
      % (e3, "HOLDS" if e3 < 1e-9 else "FAILS"))

# E4 — coverage in the measured pairwise upper range
certified = UPPER - LOWER + 1
measured = UPPER - MEASURED_START + 1
print("E4 coverage: %d certified fillings out of the measured %d = %.1f%%; "
      "the remainder of the measured range (%d..%d) stays measured"
      % (certified, measured, 100.0*certified/measured, MEASURED_START, LOWER-1))

# bonus: the theorem stretch sits entirely inside the measured winning band of space
print("consistency: the certified stretch is part of the measured space band "
      "(15997..20734): %s" % ("HOLDS" if LOWER >= MEASURED_START else "FAILS"))
