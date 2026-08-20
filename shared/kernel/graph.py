# graph.py -- the dependency graph of the corpus (milestone P0.1, audit P2.4(a))
#
# What this does, and what it deliberately does not.
#
# It builds the graph from the `builds_on` headers the chapters and packages
# already declare, and overlays the hand-set register (ledger.json) on top of it.
# It INVENTS NOTHING: every edge here was written by a human into a header, and
# every ledger placement was entered with a source. A dependency audit that
# guessed its own edges would prove whatever it was built to prove.
#
# Three questions it answers:
#
#   A) Is the declared graph acyclic? A cycle would mean a chapter builds on a
#      descendant of itself -- the derivation would be circular.
#   B) Which hand-set items does each proof inherit? Not just the ones it
#      declares, but everything reachable through its ancestors. A proof that
#      says "imports: nulla" can still stand on an import three chapters back;
#      that is not dishonest, but it has to be visible.
#   C) The named audits. Today's is P2.4(a): does the dimension programme
#      (II/13-II/16) depend, anywhere in its ancestry, on the 1/r attraction
#      import? If it does, the whole programme is circular and its results fall
#      with it. The PROGRAM is explicit that this must be CHECKED, not assumed.
#
# What it cannot do, stated rather than hidden: the graph is only as complete as
# the headers. An input a chapter uses but never declares is invisible here --
# see the note printed at the end. Finding those is human work, and the tool
# reports its own blind spot rather than implying coverage it does not have.
#
# Usage:  python shared/kernel/graph.py
# Exit code: 0 if the graph is sound and every audit passes, 1 otherwise.

import json
import re
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ROOT = Path(__file__).resolve().parents[2]
LEDGER = Path(__file__).resolve().parent / "ledger.json"
NYELV = "hu"

# The named audits. Each asks: can any of `honnan` reach any of `hova`?
# `elvart` is what the repository claims the answer is.
AUDITOK = [
    {
        "kod": "P2.4(a)",
        "kerdes": "A kiterjedes-program (II/13-II/16) tamaszkodik-e az 1/r vonzasalak importra?",
        "honnan": ["II-13", "II-14", "II-15", "II-16"],
        "tetel": "IMP-02",
        "elvart": False,
        "kovetkezmeny": ("Ha IGEN, a kiterjedes-program korkoros: az 1/r-bol vezetne le azt, "
                         "amivel az 1/r-t akarjuk levezetni. A PROGRAM P2.4 (a) pontja szerint "
                         "ez ELLENORIZENDO, nem feltetelezendo."),
    },
    {
        "kod": "P2.5",
        "kerdes": "A kiterjedes-program tamaszkodik-e az elektron-tipusdeklaraciokra?",
        "honnan": ["II-13", "II-14", "II-15", "II-16"],
        "tetel": "IMP-03",
        "elvart": False,
        "kovetkezmeny": "Ha IGEN, a tipusdeklaraciok peremadatta minositese a kiterjedes-programot is erinti.",
    },
]


def fejlec(path):
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


def lista(ertek):
    if not ertek:
        return []
    return [x.strip() for x in ertek.strip("[]").split(",") if x.strip()]


def korpusz():
    """id -> {type, builds_on, part_of, file}. Only what the headers declare."""
    csomopont = {}
    for path in sorted((ROOT / NYELV).rglob("*.md")):
        f = fejlec(path)
        azon = f.get("id")
        if not azon:
            continue
        csomopont[azon] = {
            "tipus": f.get("type", ""),
            "epul": lista(f.get("builds_on", "")),
            "resze": f.get("part_of", ""),
            "importok": f.get("imports", ""),
            "fajl": path.relative_to(ROOT).as_posix(),
        }
    return csomopont


def elerheto(csomopont, kezdo):
    """Everything reachable from `kezdo` through builds_on and part_of.

    part_of counts: a proof chapter is assembled from its packages' outgoing
    statements, so whatever a package stands on, the chapter stands on too."""
    latott, verem = set(), [kezdo]
    while verem:
        n = verem.pop()
        if n in latott or n not in csomopont:
            continue
        latott.add(n)
        verem.extend(csomopont[n]["epul"])
        # the packages of this proof
        verem.extend(k for k, v in csomopont.items() if v["resze"] == n)
    latott.discard(kezdo)
    return latott


def korkeres(csomopont):
    """Any cycle in the declared graph, by depth-first search."""
    SZURKE, FEKETE = 1, 2
    szin, ut = {}, []

    def bejar(n):
        szin[n] = SZURKE
        ut.append(n)
        for k in csomopont.get(n, {}).get("epul", []):
            if k not in csomopont:
                continue
            if szin.get(k) == SZURKE:
                return ut[ut.index(k):] + [k]
            if szin.get(k) is None:
                r = bejar(k)
                if r:
                    return r
        szin[n] = FEKETE
        ut.pop()
        return None

    for n in csomopont:
        if szin.get(n) is None:
            r = bejar(n)
            if r:
                return r
    return None


def main():
    print("== a korpusz fuggosegi grafja (P0.1) ==")
    print()
    csomopont = korpusz()
    tar = json.loads(LEDGER.read_text(encoding="utf-8"))
    tetelek = {t["id"]: t for t in tar["tetelek"]}

    elek = sum(len(v["epul"]) for v in csomopont.values())
    probak = [k for k, v in csomopont.items() if v["tipus"] == "proof"]
    print("   csomopont: %d (ebbol %d proba, %d csomag) | deklaralt el: %d"
          % (len(csomopont), len(probak),
             sum(1 for v in csomopont.values() if v["tipus"] == "package"), elek))
    hianyzo = sum(1 for v in csomopont.values()
                  if v["tipus"] in ("proof", "package") and not v["epul"])
    print("   builds_on nelkuli proba/csomag: %d" % hianyzo)
    print()

    hibak = []

    # --- A) acyclicity ------------------------------------------------------
    print("== A) kormentesseg ==")
    kor = korkeres(csomopont)
    if kor:
        print("   KOR TALALVA: %s" % " -> ".join(kor))
        hibak.append("kor a grafban")
    else:
        print("   a deklaralt graf korMENTES -- all")
    print()

    # --- B) inherited hand-set items ---------------------------------------
    print("== B) melyik proba mit orokol a kezi beallitasokbol ==")
    orokolt = {}
    for p in sorted(probak, key=lambda x: (len(x), x)):
        oseik = elerheto(csomopont, p) | {p}
        talalt = []
        for tid, t in tetelek.items():
            helyek = set([t.get("bevezette")] + list(t.get("hasznaljak", [])))
            if helyek & oseik:
                talalt.append(tid)
        orokolt[p] = sorted(talalt)
        sajat = csomopont[p]["importok"][:34]
        print("   %-7s fejlec: %-34s orokolt: %s"
              % (p, sajat, ", ".join(orokolt[p]) or "-"))
    print()

    # --- C) the named audits ------------------------------------------------
    print("== C) nevesitett auditok ==")
    for a in AUDITOK:
        t = tetelek.get(a["tetel"])
        helyek = set([t.get("bevezette")] + list(t.get("hasznaljak", []))) if t else set()
        talalatok = []
        for h in a["honnan"]:
            if (elerheto(csomopont, h) | {h}) & helyek:
                talalatok.append(h)
        eredmeny = bool(talalatok)
        rendben = eredmeny == a["elvart"]
        print("   [%s] %s" % (a["kod"], a["kerdes"]))
        print("        %s (%s) -- varhato: %s -- %s"
              % ("IGEN, es itt: " + ", ".join(talalatok) if eredmeny else "NEM",
                 "%s helye: %s" % (a["tetel"], ", ".join(sorted(helyek)) or "?"),
                 "igen" if a["elvart"] else "nem",
                 "ALL" if rendben else "BUKIK"))
        if not rendben:
            print("        %s" % a["kovetkezmeny"])
            hibak.append(a["kod"])
    print()

    # --- the tool's own blind spot -----------------------------------------
    print("== A grafa sajat vaksaga, kimondva ==")
    print("   Ez a graf CSAK a fejlecekben deklaralt fuggeseket latja. Egy olyan")
    print("   bemenet, amit egy fejezet hasznal, de sehol nem mond ki, itt")
    print("   LATHATATLAN -- es epp az ilyen a legveszelyesebb. Az ilyet emberi")
    print("   olvasas talalja meg, es ha megvan, a ledger.json-be kell konyvelni,")
    print("   ahol a racsni elkapja. A graf nem bizonyitja a teljesseget, csak azt,")
    print("   hogy amit deklaraltunk, az konzisztens.")
    print()

    if hibak:
        print("ITELET: BUKIK -- %s" % ", ".join(hibak))
        return 1
    print("ITELET: ALL -- a deklaralt graf kormentes, es minden nevesitett audit all.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
