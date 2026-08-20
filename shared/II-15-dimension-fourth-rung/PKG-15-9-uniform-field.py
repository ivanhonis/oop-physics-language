# PKG-15-9-uniform-field.py -- the decisive experiment on the selection rule
#
# The question. The staircase of II/15 turns back at the top: the densest region
# goes to the space, not to the native four-extension. The carrier theorem says
# that can only happen because the space candidate there is mirror-marked, and it
# is mirror-marked only because it was given a BODY diagonal, (1,-1,-1), whose
# coordinate sum is odd. The repository's own selection rule KON-02 would have
# given it a FACE diagonal, (0,1,-1), whose coordinate sum is even -- and that
# one carries no mirror mark.
#
# So the whole turn-back may rest on a single hand-picked step. This script
# rebuilds the field with the KON-02 candidate in place of the crystallographic
# BCC, changing NOTHING else, and re-runs the race.
#
# The prediction was sealed and committed BEFORE this script existed:
# JOS-02, seal db104804893ee3ac, commit 98d1b273 of 2026-08-20T14:52:52+02:00.
#
#   S1  at least 1900 of the top 2000 fillings go to J4, the four-extension
#   S2  the face-diagonal space wins ZERO fillings in that window
#   B1  if the face-diagonal space still takes the top (>= 1000), the carrier
#       half of the top law has failed and the turn-back is not a parity effect
#   K1  control: the full-field top must still be (1, 3, 5, 7); if it moved,
#       the experiment is broken, not a finding
#
# The tie rule is fixed in the register, in advance this time: an entrant wins a
# filling if its cost is within 1e-8 of the minimum, ties credited to all minima.

import itertools
import sys
import time
from pathlib import Path

import numpy as np

SHARED = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SHARED))

import summation                                             # noqa: E402
from parallel.letra_feladat import letra as vonal_letra      # noqa: E402
from parallel.runner import Feladat, futtat                  # noqa: E402

HELYEK = 20736
FOKOK = 4
KOORDINACIO = 2 * FOKOK
CSUCS = 2.0 * KOORDINACIO                # 16 for a mirror-marked entrant
EGZAKT_NYOM = 2.0 * FOKOK * HELYEK       # 165888
TURES = summation.TURES
ABLAK_ELSO, ABLAK_UTOLSO = 18737, 20736
S1_KUSZOB, S2_KUSZOB = 1900, 0

# The field of PKG-15-1, with ONE substitution: J3.
FO_MEZONY = [
    ("J1 line", (HELYEK,), [(1,), (2,), (3,), (4,)]),
    ("J2 plane (king)", (144, 144), [(1, 0), (0, 1), (1, 1), (1, -1)]),
    ("J3' space (KON-02: axes + FACE diagonal)", (24, 24, 36),
     [(1, 0, 0), (0, 1, 0), (0, 0, 1), (0, 1, -1)]),
    ("J4 four-extension (hypercube)", (12, 12, 12, 12),
     [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)]),
]
# kept only to show what was replaced
BCC = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, -1, -1)]


def letra_torusz(oldalak, lepesek):
    """The beat ladder of the weave on the torus with the given sides, from the
    closed Fourier form -- no matrix is ever built."""
    racsok = np.meshgrid(*[np.arange(n) for n in oldalak], indexing="ij")
    lam = np.zeros(oldalak, dtype=np.float64)
    for s in lepesek:
        faz = np.zeros(oldalak, dtype=np.float64)
        for i, n in enumerate(oldalak):
            faz += 2.0 * np.pi * racsok[i] * s[i] / n
        lam += 2.0 - 2.0 * np.cos(faz)
    return np.sort(lam.ravel())


def tukor_jegy(lam):
    return float(np.max(np.abs(np.sort(lam) - np.sort(CSUCS - lam)))) <= TURES


def korbeeres_legalabb(lepesek, oldalak, padlo=8):
    """No wrap shorter than `padlo` graph steps: walk the infinite lattice out to
    padlo-1 steps and check that no lattice vector of the torus is reached."""
    d = len(lepesek[0])
    hely = {(0,) * d}
    perem = {(0,) * d}
    for _ in range(padlo - 1):
        uj = set()
        for p in perem:
            for s in lepesek:
                for jel in (1, -1):
                    q = tuple(p[i] + jel * s[i] for i in range(d))
                    if q not in hely:
                        hely.add(q)
                        uj.add(q)
        perem = uj
    for p in hely:
        if p != (0,) * d and all(p[i] % oldalak[i] == 0 for i in range(d)):
            return False
    return True


def savok(nevek, gorbek):
    """Winner runs over the whole filling range: (label, from, to)."""
    gyoztes = np.argmin(gorbek, axis=0)
    ki, kezd = [], 0
    for n in range(1, gorbek.shape[1]):
        if gyoztes[n] != gyoztes[kezd]:
            ki.append((nevek[gyoztes[kezd]], kezd + 1, n))
            kezd = n
    ki.append((nevek[gyoztes[kezd]], kezd + 1, gorbek.shape[1]))
    return ki


def main():
    kezd = time.time()
    print("== PKG-15-9 -- the uniform-field experiment at coordination eight ==")
    print("   substitution: J3 space gets the KON-02 face diagonal (0,1,-1)")
    print("                 instead of the crystallographic BCC body diagonal (1,-1,-1)")
    print("   everything else identical to PKG-15-1.")
    print()

    print("== PRECONDITIONS ==")
    nevek, letrak = [], []
    for nev, oldalak, lepesek in FO_MEZONY:
        assert int(np.prod(oldalak)) == HELYEK, nev
        lam = letra_torusz(oldalak, lepesek)
        nevek.append(nev)
        letrak.append(lam)
        nyom = summation.pontos_osszeg(lam)
        jegy = tukor_jegy(lam)
        korbe = korbeeres_legalabb(lepesek, oldalak)
        print("   %-42s trace dev %.2e | peak %8.5f | mirror: %-3s | wrap>=8: %s"
              % (nev, abs(nyom - EGZAKT_NYOM), lam[-1],
                 "yes" if jegy else "no", "yes" if korbe else "NO"))
        if abs(nyom - EGZAKT_NYOM) > TURES or not korbe:
            print("   PRECONDITION FAILED -- stopping.")
            return 1

    bcc_letra = letra_torusz((24, 24, 36), BCC)
    print("   %-42s               | peak %8.5f | mirror: %s   (replaced)"
          % ("[the BCC used by II/15, for comparison]", bcc_letra[-1],
             "yes" if tukor_jegy(bcc_letra) else "no"))
    uj_j3_jegy = tukor_jegy(letrak[2])
    print()
    print("   the substitution did what the carrier theorem says: J3' mirror mark "
          "is %s (peak %.5f < %.0f)" % ("GONE" if not uj_j3_jegy else "STILL THERE",
                                        letrak[2][-1], CSUCS))
    print()

    # --- the main-four race ------------------------------------------------
    gorbek = np.array([summation.pontos_cumsum(l) for l in letrak])
    print("== the main-four race, whole range ==")
    for nev, tol, ig in savok(nevek, gorbek):
        print("   %-42s %6d .. %6d  (%d fillings)" % (nev, tol, ig, ig - tol + 1))
    print()

    a, b = ABLAK_ELSO - 1, ABLAK_UTOLSO
    ablak = gorbek[:, a:b]
    minimum = ablak.min(axis=0)
    maszk = ablak <= (minimum + TURES)
    pont = maszk.sum(axis=1)
    holt = int(np.count_nonzero(maszk.sum(axis=0) > 1))

    print("== the window N = %d .. %d (main four) ==" % (ABLAK_ELSO, ABLAK_UTOLSO))
    for i, nev in enumerate(nevek):
        print("   %-42s %5d fillings" % (nev, int(pont[i])))
    print("   tied fillings: %d of %d" % (holt, ablak.shape[1]))
    print()

    # --- K1: the full-field control ----------------------------------------
    print("== K1 control: the full field top must still be (1, 3, 5, 7) ==")
    tagok = list(itertools.combinations(range(1, 13), 4))
    feladatok = [Feladat(azonosito=str(l),
                         fuggveny="parallel.letra_feladat:letra",
                         argumentumok={"n": HELYEK, "lepesek": l}) for l in tagok]
    csalad = futtat(feladatok, magok=8, rendproba=4, gyoker=str(SHARED),
                    cimke="family ladders", halkan=True)
    if csalad.hibak or (csalad.rendproba and csalad.rendproba[1]):
        print("   family computation failed -- stopping.")
        return 1
    teljes_nevek = [str(l) for l in tagok] + nevek
    teljes = np.empty((len(teljes_nevek), HELYEK), dtype=np.float64)
    for i, lam in enumerate(csalad.ertekek):
        teljes[i] = summation.pontos_cumsum(np.sort(lam))
    teljes[len(tagok):] = gorbek

    tablak = teljes[:, a:b]
    tmask = tablak <= (tablak.min(axis=0) + TURES)
    tpont = tmask.sum(axis=1)
    tgyoztes = teljes_nevek[int(np.argmax(tpont))]
    print("   full-field top of the window: %s (%d fillings)"
          % (tgyoztes, int(tpont.max())))
    k1 = tgyoztes == "(1, 3, 5, 7)"
    print("   K1: %s" % ("HOLDS" if k1 else "BROKEN -- stop and find the error"))
    print()

    # --- verdict ------------------------------------------------------------
    j4 = int(pont[3])
    j3 = int(pont[2])
    s1 = j4 >= S1_KUSZOB
    s2 = j3 <= S2_KUSZOB
    b1 = j3 >= ablak.shape[1] // 2
    b3 = holt > ablak.shape[1] // 2

    print("== VERDICT against the sealed criteria of JOS-02 ==")
    print("   S1 (>= %d of 2000 to J4): %s -- J4 has %d"
          % (S1_KUSZOB, "HOLDS" if s1 else "FAILS", j4))
    print("   S2 (J3' wins zero): %s -- J3' has %d"
          % ("HOLDS" if s2 else "FAILS", j3))
    print("   B1 (J3' still takes the top): %s"
          % ("TRIGGERED" if b1 else "not triggered"))
    print("   B3 (ties dominate): %s" % ("TRIGGERED" if b3 else "not triggered"))
    print("   K1 (control): %s" % ("HOLDS" if k1 else "BROKEN"))
    print()
    if not k1:
        print("   The control broke. Nothing above counts as a finding.")
        return 1
    if s1 and s2:
        print("   THE PREDICTION HOLDS: with a uniform selection rule the turn-back")
        print("   disappears, and the top of the main field goes to the native")
        print("   four-extension. The II/15 turn-back was a consequence of the")
        print("   crystallographic BCC choice.")
    elif b1:
        print("   B1 TRIGGERED: the mirror mark is NOT what decides the top.")
        print("   The carrier half of the top law has failed -- record it.")
    else:
        print("   PARTIAL: neither branch is clean. Report the numbers as they are.")
    print()
    print("   (%.1f s)" % (time.time() - kezd))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
