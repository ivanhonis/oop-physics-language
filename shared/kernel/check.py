# check.py -- the gate of the hand-set ledger (shared/kernel/ledger.json)
#
# Why this exists. Several results of Part II rest partly on items the language
# did not derive but we set by hand: borrowed concepts (imports), our own rules
# of play (conventions), raw world data (boundary data) and stated scope limits.
# The repository already names them in prose; what was missing is a single
# machine-checkable register and a gate that refuses to let it grow silently.
#
# This script is bookkeeping, not physics. It never recomputes a result and it
# can never overturn a verdict. It answers exactly three questions:
#
#   A) Is the register internally sound? (schema, unique ids, live references)
#   B) Does it agree with the corpus? (every declared import is registered,
#      and the counts stated in I/1 match what the register actually holds)
#   C) Do the gates hold? (import ratchet, sensitivity coverage, no item left
#      in the dual "candidate import" status without a milestone to close it)
#
# Exit code: 0 if every hard check passes, 1 if any fails. Coverage below the
# declared threshold is a hard failure too -- that is the point of the ratchet.
#
# Run from anywhere:  python shared/kernel/check.py

import json
import re
import sys
from pathlib import Path

try:                                     # accented output where the console allows it
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:                        # older interpreters / exotic consoles
    pass

ROOT = Path(__file__).resolve().parents[2]
LEDGER = Path(__file__).resolve().parent / "ledger.json"
KUTATASI_NYELV = "hu"                    # the language folder the register indexes

RANGOK = ("import", "jelolt-import", "konvencio", "peremadat", "hatokor")
ALLAPOTOK = ("aktiv", "reszben-tetelesitve", "jelolt", "torlesztve", "visszavont")
ERZ_ALLAPOTOK = ("nincs-merve", "merve", "nem-ertelmezheto")
KOTELEZO = ("id", "rang", "nev", "leiras", "bevezette", "hasznaljak",
            "allapot", "torlesztes", "erzekenyseg", "forras")
ID_ALAK = re.compile(r"^(IMP|KON|PER|HAT|JEL)-\d{2}$")

# I/1 states the counts in words; the register must agree with the prose.
SZAMNEVEK = {"nulla": 0, "egy": 1, "ketto": 2, "kettő": 2, "ket": 2, "két": 2,
             "harom": 3, "három": 3, "negy": 4, "négy": 4, "ot": 5, "öt": 5,
             "hat": 6, "het": 7, "hét": 7, "nyolc": 8, "kilenc": 9, "tiz": 10,
             "tíz": 10}

# The register only owes an entry for a proof whose header declares something.
# A bare "nulla" means the chapter took on nothing of its own.
TRIVIALIS_IMPORT = ("nulla",)


class Jelentes:
    """Collects findings so the whole report prints, not just the first failure."""

    def __init__(self):
        self.hibak = []
        self.figyelmeztetesek = []

    def hiba(self, kod, uzenet):
        self.hibak.append((kod, uzenet))

    def figyelem(self, kod, uzenet):
        self.figyelmeztetesek.append((kod, uzenet))


def fejlec(path):
    """The YAML header of a markdown file, as a flat dict of raw strings."""
    mezok = {}
    try:
        sorok = path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeDecodeError):
        return mezok
    if not sorok or sorok[0].strip() != "---":
        return mezok
    for sor in sorok[1:]:
        if sor.strip() == "---":
            break
        m = re.match(r"^([a-z_]+):\s*(.*)$", sor)
        if m:
            mezok[m.group(1)] = m.group(2).strip().strip('"')
    return mezok


def korpusz():
    """id -> file, and id -> declared imports, for every chapter of the
    research language. The register addresses the corpus by id, never by path."""
    id_fajl, id_import = {}, {}
    for path in sorted((ROOT / KUTATASI_NYELV).rglob("*.md")):
        fej = fejlec(path)
        azon = fej.get("id")
        if not azon:
            continue
        id_fajl[azon] = path.relative_to(ROOT).as_posix()
        if "imports" in fej:
            id_import[azon] = fej["imports"]
    return id_fajl, id_import


# ---------------------------------------------------------------- A) soundness

def a_csoport(tetelek, id_fajl, jel):
    latott = set()
    for t in tetelek:
        azon = t.get("id", "<id nelkul>")
        for mezo in KOTELEZO:
            if mezo not in t:
                jel.hiba("A1", "%s: hianyzo kotelezo mezo: %s" % (azon, mezo))
        if not ID_ALAK.match(str(azon)):
            jel.hiba("A2", "%s: az azonosito alakja nem PREFIX-NN" % azon)
        if azon in latott:
            jel.hiba("A2", "%s: ismetelt azonosito -- az id soha nem hasznalhato ujra" % azon)
        latott.add(azon)

        if t.get("rang") not in RANGOK:
            jel.hiba("A1", "%s: ismeretlen rang: %r" % (azon, t.get("rang")))
        if t.get("allapot") not in ALLAPOTOK:
            jel.hiba("A1", "%s: ismeretlen allapot: %r" % (azon, t.get("allapot")))

        erz = t.get("erzekenyseg") or {}
        if erz.get("allapot") not in ERZ_ALLAPOTOK:
            jel.hiba("A1", "%s: ismeretlen erzekenysegi allapot: %r"
                     % (azon, erz.get("allapot")))
        if erz.get("allapot") == "merve" and not erz.get("meres"):
            jel.hiba("A1", "%s: 'merve' allapot meres-forras nelkul" % azon)

        for hiv in t.get("forras", []):
            if not (ROOT / hiv).exists():
                jel.hiba("A3", "%s: a forras nem letezik: %s" % (azon, hiv))

        hivatkozott = [t.get("bevezette")] + list(t.get("hasznaljak", []))
        for cel in hivatkozott:
            if cel and cel not in id_fajl:
                jel.hiba("A4", "%s: feloldhatatlan azonosito: %s" % (azon, cel))


# ------------------------------------------------- B) agreement with the corpus

def b_csoport(tetelek, id_import, jel):
    lefedett = set()
    for t in tetelek:
        if t.get("bevezette"):
            lefedett.add(t["bevezette"])
        lefedett.update(t.get("hasznaljak", []))

    for azon, deklaralt in sorted(id_import.items()):
        if deklaralt.strip().lower() in TRIVIALIS_IMPORT:
            continue
        if azon not in lefedett:
            jel.hiba("B1", "%s: a fejlec importot deklaral, de a nyilvantartas "
                           "nem fedi le -- %r" % (azon, deklaralt[:70]))

    szabaly = ROOT / "hu" / "I-language" / "I-01-concept_hu.md"
    if not szabaly.exists():
        jel.figyelem("B2", "az I/1 nem talalhato; a darabszam-egyeztetes kimarad")
        return

    szoveg = szabaly.read_text(encoding="utf-8")
    minta = {"import": r"\*\*Az importok\s*[-—]\s*(\w+)",
             "konvencio": r"\*\*A kimondott konvenciok?\s*[-—]\s*(\w+)"}
    minta["konvencio"] = r"\*\*A kimondott konvenci[oó]k\s*[-—]\s*(\w+)"

    for rang, mint in minta.items():
        m = re.search(mint, szoveg)
        if not m:
            jel.figyelem("B2", "az I/1-ben nem talalom a(z) '%s' darabszam-mondatot "
                               "-- a szoveg alakja valtozhatott" % rang)
            continue
        kimondott = SZAMNEVEK.get(m.group(1).lower())
        if kimondott is None:
            jel.figyelem("B2", "ismeretlen szamnev az I/1-ben: %r" % m.group(1))
            continue
        tenyleges = sum(1 for t in tetelek
                        if t.get("rang") == rang and t.get("allapot") != "visszavont")
        if kimondott != tenyleges:
            jel.hiba("B2", "az I/1 %d '%s' tetelt mond ki, a nyilvantartasban %d all"
                     % (kimondott, rang, tenyleges))


# ------------------------------------------------------------------- C) gates

def c_csoport(meta, tetelek, jel):
    aktiv_import = [t for t in tetelek
                    if t.get("rang") == "import" and t.get("allapot") != "torlesztve"]
    plafon = meta.get("import_plafon")
    if plafon is None:
        jel.hiba("C1", "a meta nem tartalmaz import_plafon-t -- a racsni nem all")
    elif len(aktiv_import) > plafon:
        jel.hiba("C1", "az aktiv importok szama %d, a plafon %d -- az import "
                       "csendben nott" % (len(aktiv_import), plafon))

    merendo = [t for t in tetelek if t.get("rang") in ("import", "konvencio")]
    merve = [t for t in merendo
             if (t.get("erzekenyseg") or {}).get("allapot") == "merve"]
    arany = len(merve) / len(merendo) if merendo else 1.0
    kuszob = meta.get("erzekenyseg_kuszob", 0.0)
    if arany < kuszob:
        jel.hiba("C2", "az erzekenysegi lefedettseg %.0f%%, a kuszob %.0f%%"
                 % (100 * arany, 100 * kuszob))

    for t in tetelek:
        if t.get("rang") == "jelolt-import" and not t.get("torlesztes"):
            jel.hiba("C3", "%s: kettos allasu elem torlesztesi merfoldko nelkul -- "
                           "a magban ilyen nem maradhat" % t.get("id"))

    return aktiv_import, merendo, merve, arany


# ------------------------------------------------------------------- reporting

def tabla(tetelek):
    print("  %-8s %-14s %-46s %s" % ("id", "rang", "nev", "erzekenyseg"))
    print("  " + "-" * 92)
    for t in sorted(tetelek, key=lambda x: x.get("id", "")):
        erz = (t.get("erzekenyseg") or {}).get("allapot", "?")
        jel = {"merve": "[MERVE]", "nincs-merve": "[nincs merve]",
               "nem-ertelmezheto": "[nem ertelmezheto]"}.get(erz, erz)
        print("  %-8s %-14s %-46s %s"
              % (t.get("id"), t.get("rang"), t.get("nev", "")[:46], jel))


def main():
    print("== a kezi beallitasok magja -- kapu-ellenorzes ==")
    print()

    if not LEDGER.exists():
        print("HIBA: a nyilvantartas nem talalhato: %s" % LEDGER)
        return 1
    try:
        tar = json.loads(LEDGER.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        print("HIBA: a nyilvantartas nem ervenyes JSON: %s" % e)
        return 1

    meta = tar.get("meta", {})
    tetelek = tar.get("tetelek", [])
    id_fajl, id_import = korpusz()

    print("nyilvantartas : %s (%d tetel)"
          % (LEDGER.relative_to(ROOT).as_posix(), len(tetelek)))
    print("korpusz       : %d azonositott fajl a(z) %s/ alatt, ebbol %d deklaral importot"
          % (len(id_fajl), KUTATASI_NYELV, len(id_import)))
    print()

    jel = Jelentes()
    a_csoport(tetelek, id_fajl, jel)
    b_csoport(tetelek, id_import, jel)
    aktiv_import, merendo, merve, arany = c_csoport(meta, tetelek, jel)

    tabla(tetelek)
    print()
    print("  aktiv import        : %d / plafon %s"
          % (len(aktiv_import), meta.get("import_plafon")))
    print("  erzekenysegi fedes  : %d / %d = %.0f%% (kuszob %.0f%%)"
          % (len(merve), len(merendo), 100 * arany,
             100 * meta.get("erzekenyseg_kuszob", 0.0)))
    print()

    for kod, uzenet in jel.figyelmeztetesek:
        print("FIGYELEM [%s] %s" % (kod, uzenet))
    for kod, uzenet in jel.hibak:
        print("HIBA     [%s] %s" % (kod, uzenet))
    if jel.figyelmeztetesek or jel.hibak:
        print()

    if jel.hibak:
        print("ITELET: BUKIK -- %d hiba. A kapu zarva: uj csomag nem epulhet, "
              "amig ezek allnak." % len(jel.hibak))
        return 1

    print("ITELET: ALL -- a nyilvantartas ep, egyezik a korpusszal, es a kapuk allnak.")
    if arany < 1.0:
        print("Megjegyzes: %d kezi elem meg megmeretlen. Ez ma nem bukas (a kuszob "
              "%.0f%%), de a P1.3 utan a kuszob emelendo."
              % (len(merendo) - len(merve), 100 * meta.get("erzekenyseg_kuszob", 0.0)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
