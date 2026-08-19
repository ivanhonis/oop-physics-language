# tools/assemble.py — egy adott nyelv teljes dumpjanak eloallitasa
#
# Hasznalat:  python tools/assemble.py
#   A nyelvet bekeri (Enter = hu), majd a teljes fa-strukturat bejarva
#   minden, a valasztott nyelvi vegzodesu (_hu / _en) md-fajlt beletesz
#   a dumpba — kiveve a nem tudomanyos fajlokat (lasd EXCLUDE lista).
#   A shared/ mappa teljes tartalma (nyelvfuggetlen kodok, adatok)
#   NYELVTOL FUGGETLENUL minden dump VEGERE kerul.
#
# A dump felepitese:
#   1. blokk: a teljes konyvtarlista (minden bekerulo fajl, utvonallal)
#   2. blokktol: a fajlok egyenkent, igy elvalasztva:
#        <file path="hu\I-language\I-01-concept_hu.md">
#        ...a fajl teljes tartalma valtozatlanul...
#        </file>
#   vegen: a shared/ fajljai ugyanigy.
#
# Kimenet: dist/dump_<nyelv>.md

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SHARED_DIR = ROOT / "shared"

# --- KIHAGYASI LISTA -------------------------------------------------------
# Minden nem tudomanyos fajl es mappa. Szukseg szerint boviheto.
EXCLUDE_FILE_PREFIXES = (
    "README",
    "CONTRIBUTING",
    "CHANGELOG",
    "LICENSE",
    "CITATION",
)
EXCLUDE_DIRS = {".git", ".github", "tools", "dist", "__pycache__", "!work", "!archive"}
# Binaris mellekletek: a tartalmuk nem masolhato a dumpba (nem szoveg),
# de a konyvtarlistaban szerepelniuk kell, mert a repo reszei.
BINARY_SUFFIXES = {".npy", ".npz", ".png", ".jpg", ".jpeg", ".gif", ".pdf", ".zip", ".gz"}
# ---------------------------------------------------------------------------


def excluded(rel: Path) -> bool:
    if any(part in EXCLUDE_DIRS for part in rel.parts):
        return True
    if rel.name.startswith(EXCLUDE_FILE_PREFIXES):
        return True
    return False


def collect_lang(lang: str) -> list[Path]:
    """A valasztott nyelvi vegzodesu md-fajlok, a kihagyasi lista szerint szurve."""
    suffix = f"_{lang}.md"
    files = []
    for p in sorted(ROOT.rglob(f"*{suffix}")):
        rel = p.relative_to(ROOT)
        if excluded(rel) or "shared" in rel.parts:
            continue
        files.append(rel)
    return files


def collect_shared() -> list[Path]:
    """A shared/ teljes tartalma — nyelvtol fuggetlenul, minden dump vegere."""
    if not SHARED_DIR.is_dir():
        return []
    files = []
    for p in sorted(SHARED_DIR.rglob("*")):
        if not p.is_file():
            continue
        rel = p.relative_to(ROOT)
        if excluded(rel):
            continue
        files.append(rel)
    return files


def main() -> int:
    try:
        lang = input("Nyelv / language [hu]: ").strip().lower() or "hu"
    except EOFError:
        lang = "hu"

    lang_files = collect_lang(lang)
    shared_files = collect_shared()
    if not lang_files:
        print(f"Nincs egyetlen *_{lang}.md fajl sem a faban.", file=sys.stderr)
        return 1

    all_files = lang_files + shared_files
    parts = []

    # 1. blokk: a teljes konyvtarlista (nyelvi fajlok, majd a shared)
    parts.append("<directory>")
    for rel in all_files:
        parts.append(str(rel))
    parts.append("</directory>")
    parts.append("")

    # a fajlok, egyenkent file-tagek kozt, valtozatlan tartalommal;
    # a shared a lista vegen all
    for rel in all_files:
        if rel.suffix.lower() in BINARY_SUFFIXES:
            meret = (ROOT / rel).stat().st_size
            content = f"[binaris melleklet, {meret} bajt - a tartalma nem kerul a dumpba]"
        else:
            content = (ROOT / rel).read_text(encoding="utf-8").rstrip("\n")
        parts.append(f'<file path="{rel}">')
        parts.append(content)
        parts.append("</file>")
        parts.append("")

    out_dir = ROOT / "dist"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"dump_{lang}.md"
    out_path.write_text("\n".join(parts), encoding="utf-8")
    print(f"OK: {out_path.relative_to(ROOT)}  "
          f"({len(lang_files)} nyelvi + {len(shared_files)} shared fajl)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
