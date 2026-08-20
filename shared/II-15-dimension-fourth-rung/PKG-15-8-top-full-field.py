# PKG-15-8-top-full-field.py -- the top of the FULL field at coordination eight
#
# The question, registered in advance. The top law (III/1, 8.) says the full end
# is carried by the lowest-extension mirror-marked member of the FULL field. Its
# two theorem legs are proved; its measured leg stands at coordination six and
# ten, and coordination eight has never been read. This script reads it.
#
# The prediction was sealed and committed BEFORE this computation existed:
# JOS-01 in shared/register/predictions.json, seal 4332b127..., commit 751fbab
# of 2026-08-20T13:56:34+02:00. Its criteria, fixed there and not touched here:
#
#   window : the full end, N = 18737 .. 20736 (2000 fillings, the same absolute
#            window PKG-16-5 read at coordination ten, so the two compare)
#   S1     : at least 1900 of the 2000 go to a mirror-marked entrant
#   S2     : the entrant winning the most fillings in the window is (1, 3, 5, 7)
#   B1/B2/B3 : the failure branches, see the register
#
# Route: the H4 portable summation of shared/summation.py throughout. The field
# is the 503 entrants PKG-15-1 declared -- 495 four-step family members, the main
# four, and the four controls.
#
# Mandatory precondition, in the spirit of the two-way rule: the closed-form
# ladders built here must agree with the ladders PKG-15-2 saved, on every cached
# entrant. Two algorithms, not two float widths. If that fails, nothing below is
# worth reading.

import itertools
import sys
import time
from pathlib import Path

import numpy as np

SHARED = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SHARED))

import summation                                             # noqa: E402
from parallel.letra_feladat import letra, paros_jegy         # noqa: E402
from parallel.runner import Feladat, futtat                  # noqa: E402

HELYEK = 20736
FOKOK = 4
KOORDINACIO = 2 * FOKOK                  # eight contracts per place
CSUCS = 2.0 * KOORDINACIO                # 16: the peak beat of a mirror-marked net
LEPES_PLAFON = 12
TURES = summation.TURES                  # 1e-8, the fixed identity tolerance
GYORSITOTAR = SHARED / "II-15-dimension-fourth-rung" / "letrak_gepi"

ABLAK_ELSO, ABLAK_UTOLSO = 18737, 20736  # fixed in JOS-01
S1_KUSZOB = 1900
S2_JOSLAT = (1, 3, 5, 7)


def csalad():
    return list(itertools.combinations(range(1, LEPES_PLAFON + 1), FOKOK))


def tukor_jegy_letrabol(lam):
    """Mirror mark straight from the ladder, independent of how the net was named.

    A d-regular net is bipartite exactly when its beat spectrum is symmetric
    about d, so lam and 2d - lam must be the same multiset. This works for the
    saved main and control ladders too, where the step list is not available."""
    tukrozott = np.sort(CSUCS - lam)
    return float(np.max(np.abs(np.sort(lam) - tukrozott))) <= TURES


def elofeltetel():
    """The closed route against the ladders PKG-15-2 saved."""
    print("== PRECONDITION: closed-form ladders against the saved cache ==")
    fajlok = sorted(GYORSITOTAR.glob("(*.npy"))
    if not fajlok:
        print("   no cached family ladders found -- cannot verify. STOPPING.")
        return False, {}
    legrosszabb, db = 0.0, 0
    for f in fajlok:
        lepesek = tuple(int(x) for x in f.stem.strip("()").split(","))
        mentett = np.sort(np.load(f).astype(np.float64).ravel())
        sajat = letra(HELYEK, lepesek)
        legrosszabb = max(legrosszabb, float(np.max(np.abs(mentett - sajat))))
        db += 1
    all_e = legrosszabb <= TURES
    print("   %d cached family ladders, largest deviation %.3e (tolerance %.1e) -- %s"
          % (db, legrosszabb, TURES, "HOLDS" if all_e else "FAILS"))
    print()
    return all_e, {}


def fo_es_kontroll():
    """The main four and the four controls, from the saved cache."""
    mezony = {}
    for nev in ("J1", "J2", "J3", "J4", "K1", "K2", "K3", "K4"):
        ut = GYORSITOTAR / ("%s.npy" % nev)
        if ut.exists():
            mezony[nev] = np.sort(np.load(ut).astype(np.float64).ravel())
    return mezony


def main():
    kezd = time.time()
    print("== PKG-15-8 -- the top of the FULL field, coordination eight ==")
    print("   system: %d places, %d contracts each" % (HELYEK, KOORDINACIO))
    print("   window: N = %d .. %d (%d fillings), fixed in JOS-01"
          % (ABLAK_ELSO, ABLAK_UTOLSO, ABLAK_UTOLSO - ABLAK_ELSO + 1))
    print()

    rendben, _ = elofeltetel()
    if not rendben:
        return 1

    tagok = csalad()
    feladatok = [Feladat(azonosito=str(l),
                         fuggveny="parallel.letra_feladat:letra",
                         argumentumok={"n": HELYEK, "lepesek": l}) for l in tagok]
    print("== the field ==")
    eredmeny = futtat(feladatok, magok=8, rendproba=6, gyoker=str(SHARED),
                      cimke="family ladders", halkan=False)
    if eredmeny.hibak:
        print("   %d tasks failed -- STOPPING." % len(eredmeny.hibak))
        return 1
    if eredmeny.rendproba and eredmeny.rendproba[1]:
        print("   ORDER-INDEPENDENCE CHECK FAILED -- STOPPING.")
        return 1

    nevek = [str(l) for l in tagok]
    letrak = list(eredmeny.ertekek)
    lepes_szerint = {str(l): l for l in tagok}

    extra = fo_es_kontroll()
    for nev, lam in extra.items():
        nevek.append(nev)
        letrak.append(lam)
    print("   entrants: %d family + %d main/control = %d"
          % (len(tagok), len(extra), len(nevek)))
    print()

    # --- cost curves on the H4 route ---------------------------------------
    print("== cost curves (H4 portable route) ==")
    gorbek = np.empty((len(nevek), HELYEK), dtype=np.float64)
    egzakt_nyom = 2.0 * FOKOK * HELYEK
    nyom_hiba = 0.0
    for i, lam in enumerate(letrak):
        gorbek[i] = summation.pontos_cumsum(np.sort(lam))
        nyom_hiba = max(nyom_hiba, abs(gorbek[i, -1] - egzakt_nyom))
    print("   built-in check -- exact trace %d on every entrant: largest deviation "
          "%.3e -- %s" % (egzakt_nyom, nyom_hiba,
                          "HOLDS" if nyom_hiba <= TURES else "FAILS"))
    if nyom_hiba > TURES:
        return 1

    tukros = np.array([tukor_jegy_letrabol(np.sort(l)) for l in letrak])
    print("   mirror-marked entrants (spectrum symmetric about %d): %d of %d"
          % (CSUCS, int(tukros.sum()), len(nevek)))
    print()

    # --- the race on the fixed window --------------------------------------
    print("== the race on the window ==")
    a, b = ABLAK_ELSO - 1, ABLAK_UTOLSO          # 0-based slice
    ablak = gorbek[:, a:b]
    legolcsobb = ablak.min(axis=0)
    nyertes_maszk = ablak <= (legolcsobb + TURES)     # ties included
    nyertes_db = nyertes_maszk.sum(axis=0)

    holtverseny = int(np.count_nonzero(nyertes_db > 1))
    egyertelmu = ablak.shape[1] - holtverseny
    print("   fillings: %d | unique winner: %d | tied: %d"
          % (ablak.shape[1], egyertelmu, holtverseny))

    # S1, in both readings -- see the honest note printed at the end
    barmelyik = np.array([bool(tukros[nyertes_maszk[:, j]].any())
                          for j in range(ablak.shape[1])])
    mind = np.array([bool(tukros[nyertes_maszk[:, j]].all())
                     for j in range(ablak.shape[1])])
    print("   S1 permissive (a mirror-marked entrant is among the minima): %d / %d"
          % (int(barmelyik.sum()), ablak.shape[1]))
    print("   S1 strict     (every minimal entrant is mirror-marked)     : %d / %d"
          % (int(mind.sum()), ablak.shape[1]))

    # S2: who wins the most fillings in the window (ties credited to each)
    pontszam = nyertes_maszk.sum(axis=1)
    sorrend = np.argsort(-pontszam)
    print()
    print("   entrants winning the most fillings in the window:")
    for i in sorrend[:8]:
        if pontszam[i] == 0:
            break
        print("      %-16s %5d fillings   mirror-marked: %s"
              % (nevek[i], int(pontszam[i]), "yes" if tukros[i] else "no"))

    gyoztes = nevek[int(sorrend[0])]
    print()
    print("== VERDICT against the sealed criteria of JOS-01 ==")
    s1_lazan = int(barmelyik.sum()) >= S1_KUSZOB
    s1_szigoruan = int(mind.sum()) >= S1_KUSZOB
    s2 = lepes_szerint.get(gyoztes) == S2_JOSLAT
    b3 = holtverseny > ablak.shape[1] // 2

    print("   S1 (>= %d of 2000 to a mirror-marked entrant)" % S1_KUSZOB)
    print("        permissive reading: %s" % ("HOLDS" if s1_lazan else "FAILS"))
    print("        strict reading    : %s" % ("HOLDS" if s1_szigoruan else "FAILS"))
    print("   S2 (the most-winning entrant is %s): %s -- it is %s"
          % (str(S2_JOSLAT), "HOLDS" if s2 else "FAILS", gyoztes))
    print("   B3 (ties dominate the window): %s (%d of %d tied)"
          % ("TRIGGERED" if b3 else "not triggered", holtverseny, ablak.shape[1]))
    print()
    print("   Honest note, stated rather than resolved after the fact: JOS-01 fixed")
    print("   the window and the thresholds but did NOT fix how ties are credited.")
    print("   Both readings are therefore reported, and the tie count with them.")
    print("   Fixing the tie rule in advance is a lesson for the next registration,")
    print("   not something to settle now that the numbers are on the screen.")
    print()
    print("   (%.1f s)" % (time.time() - kezd))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
