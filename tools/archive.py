# tools/archive.py — a repó archiválása időbélyeges mappába, rotációval.
#
# Használat (bárhonnan):  python tools/archive.py
# A repó gyökere a szkript helyéből adódik (a tools mappa szülője).
#
# Működés:
#   1. A teljes repót a  !archive/ÉÉÉÉ-HH-NN_ÓÓ-PP/  mappába másolja,
#      kihagyva a KIHAGYOTT_MAPPAK neveit (bármely mélységben).
#   2. Ha ugyanabban a percben már készült archívum, _2, _3 … toldalékot kap.
#   3. Rotáció: ha 50-nél több archívum-mappa van, a legrégebbiek törlődnek
#      (a mappanév dátum-rendezhető, így a névsor a kor szerinti sorrend).
#   4. Hiba esetén a félkész archívum törlődik, a szkript hibával áll le.

import shutil
import sys
from datetime import datetime
from pathlib import Path

KIHAGYOTT_MAPPAK = {"!archive", "!work", ".github", ".venv", "dist",
                    ".git", "__pycache__"}
MEGTARTOTT_DB = 50
ARCHIV_MAPPA = "!archive"


def repo_gyoker() -> Path:
    return Path(__file__).resolve().parent.parent


def cel_mappa(archiv: Path) -> Path:
    nev = datetime.now().strftime("%Y-%m-%d_%H-%M")
    cel = archiv / nev
    sorszam = 2
    while cel.exists():
        cel = archiv / f"{nev}_{sorszam}"
        sorszam += 1
    return cel


def kihagyo(mappa, nevek):
    return [n for n in nevek if n in KIHAGYOTT_MAPPAK]


def masolas(gyoker: Path, cel: Path) -> int:
    try:
        shutil.copytree(gyoker, cel, ignore=kihagyo)
    except Exception:
        if cel.exists():
            shutil.rmtree(cel, ignore_errors=True)
        raise
    return sum(1 for p in cel.rglob("*") if p.is_file())


def rotacio(archiv: Path) -> list[str]:
    mappak = sorted(p for p in archiv.iterdir() if p.is_dir())
    toroltek = []
    while len(mappak) > MEGTARTOTT_DB:
        legregebbi = mappak.pop(0)
        shutil.rmtree(legregebbi)
        toroltek.append(legregebbi.name)
    return toroltek


def main() -> int:
    gyoker = repo_gyoker()
    archiv = gyoker / ARCHIV_MAPPA
    archiv.mkdir(exist_ok=True)

    cel = cel_mappa(archiv)
    darab = masolas(gyoker, cel)
    print(f"archiválva: {cel.relative_to(gyoker)}  ({darab} fájl)")

    toroltek = rotacio(archiv)
    if toroltek:
        print("rotáció törölte:", ", ".join(toroltek))
    else:
        print(f"rotáció: nem kellett törölni "
              f"({sum(1 for p in archiv.iterdir() if p.is_dir())}/{MEGTARTOTT_DB})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
