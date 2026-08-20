# demo.py -- a worked, real-scale example of the parallel runner
#
# The field: every four-step weave of the II/15 line family on the fixed system
# of 20736 places -- all 495 of them, the same field PKG-15-1 declared. For each
# entrant this builds the ladder by the closed route, takes its exact trace on
# the H4 portable route, and reads the cost curve at five fillings.
#
# It stops deliberately short of comparing entrants. Who wins the top of the full
# field is the registered blind prediction JOS-01 (milestone P1.1); that
# comparison belongs to its own package, not to a runner demo.
#
# What this demonstrates instead, and what every parallel stage should show:
#
#   * the speed-up, measured against a serial sample rather than asserted;
#   * the built-in check -- all 495 traces must equal 2 * 4 * 20736 = 165888;
#   * the order-independence check, which is what makes the speed-up mean
#     anything at all.
#
# Usage:
#   python shared/parallel/demo.py
#   python shared/parallel/demo.py --magok 4 --tiszta

import itertools
import shutil
import sys
import time
from pathlib import Path

SHARED = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SHARED))

from parallel.runner import ALAP_GYORSITOTAR, Feladat, futtat, jelentes  # noqa: E402
from parallel.letra_feladat import letra_es_gorbe, paros_jegy            # noqa: E402

HELYEK = 20736          # the fixed system of II/15
LEPES_PLAFON = 12       # the declared scope limit HAT-03
FOKOK = 4               # four +/- pairs = coordination eight
EGZAKT_NYOM = 2.0 * FOKOK * HELYEK      # 165888


def mezony():
    """The line family exactly as PKG-15-1 declares it: every four-subset of the
    steps 1..12. C(12,4) = 495 entrants."""
    return list(itertools.combinations(range(1, LEPES_PLAFON + 1), FOKOK))


def main(argv):
    magok = 8
    if "--magok" in argv:
        magok = int(argv[argv.index("--magok") + 1])
    if "--tiszta" in argv and ALAP_GYORSITOTAR.exists():
        shutil.rmtree(ALAP_GYORSITOTAR, ignore_errors=True)
        print("gyorsitotar torolve: %s" % ALAP_GYORSITOTAR)

    tagok = mezony()
    print("== parhuzamos pelda: a II/15 vonal-csalad letrai ==")
    print()
    print("  rendszer   : %d hely, %d +/- par (nyolcas koordinacio)" % (HELYEK, FOKOK))
    print("  mezony     : %d csaladtag (%d-es lepes-plafon)" % (len(tagok), LEPES_PLAFON))
    print("  egzakt nyom: %d minden indulon" % EGZAKT_NYOM)
    print("  gyorsitotar: %s" % ALAP_GYORSITOTAR)
    print()

    # A serial sample first, to have something honest to compare against.
    minta = tagok[:12]
    kezd = time.time()
    for lepesek in minta:
        letra_es_gorbe(HELYEK, lepesek)
    soros_egy = (time.time() - kezd) / len(minta)
    print("  soros mero-minta: %d indulo, %.3f s/indulo -> a teljes mezony "
          "sorosan ~%.1f s" % (len(minta), soros_egy, soros_egy * len(tagok)))
    print()

    feladatok = [Feladat(azonosito=str(lepesek),
                         fuggveny="parallel.letra_feladat:letra_es_gorbe",
                         argumentumok={"n": HELYEK, "lepesek": lepesek})
                 for lepesek in tagok]

    eredmeny = futtat(feladatok, magok=magok, rendproba=8,
                      cimke="csaladtagok", gyoker=str(SHARED))

    kod = jelentes(eredmeny, cimke="a mezony letrai")

    # --- the built-in check every entrant carries ---------------------------
    ertekek = [e for e in eredmeny.ertekek if e is not None]
    legrosszabb = max((e["nyom_elteres"] for e in ertekek), default=float("inf"))
    print("  beepitett ellenorzes -- nyomosszeg %d mind a %d indulon:"
          % (EGZAKT_NYOM, len(ertekek)))
    print("     legnagyobb elteres: %.3e  (a rogzitett tures 1.0e-08) -- %s"
          % (legrosszabb, "ALL" if legrosszabb <= 1e-8 else "BUKIK"))
    if legrosszabb > 1e-8:
        kod = 1

    # --- a field finding that costs nothing extra ---------------------------
    # Not a race, just a census: how much of the field carries the mirror mark.
    tukros = [e for e in ertekek if paros_jegy(e["lepesek"])]
    print()
    print("  mezony-lelet (nem verseny): %d tukor-jegyu (csupa-paratlan lepesu) "
          "tag a %d-bol" % (len(tukros), len(ertekek)))
    if tukros:
        legkisebb = min(tukros, key=lambda e: sum(s * s for s in e["lepesek"]))
        print("     a legkisebb ossz-lepesnegyzetu koztuk: %s (%d)"
              % (str(legkisebb["lepesek"]),
                 sum(s * s for s in legkisebb["lepesek"])))

    if eredmeny.futott and soros_egy > 0:
        becsult = soros_egy * eredmeny.futott
        print()
        print("  gyorsulas: %d indulo sorosan ~%.1f s, parhuzamosan %.1f s -> %.1fx"
              % (eredmeny.futott, becsult, eredmeny.ido,
                 becsult / max(eredmeny.ido, 1e-9)))
    return kod


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
