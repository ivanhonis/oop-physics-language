---
id: README
type: entry-point
lang: multi
doc_version: "1.4"
status: ervenyes
---

# OOP-based physical descriptive language · OOP-alapú fizikai leírónyelv

**[English](#english)** · **[Magyar](#magyar)**

---

## English

A descriptive language that models the physical world with object-oriented patterns — not as metaphor: every pattern is sharpened until it yields a computable claim, and that claim is checked against measured quantum-physics results.

> **Language status:** the research is conducted in **Hungarian** (`hu/`). We aim to keep the English mirror (`en/`) up to date, but new results appear in Hungarian first. Terminology for translations is fixed in the dictionary chapter (`I-10-dictionary`).

### Reading order

1. **`en/00-introduction_en.md`** — the idea and how it is built up
2. **`en/I-language/`** — the language: concepts, laws, theorems, contracts (only what is proven)
3. **`en/II-proofs/`** — the computed proofs; every claim receives its evidence here
4. **`en/III-frontier/`** — the frontier: candidate laws and open questions
5. **`en/appendix/`** — machinery, benchmarks, package trail

Quick entry: `en/I-language/I-00-index_en.md` and `en/II-proofs/II-00-index_en.md`.

### Repository layout

```
oop-physics-language/
├── README.md                ← this file (multilingual entry point)
├── LICENSE · CITATION.cff · .gitignore
├── CONTRIBUTING.md          ← the editing rulebook (language-independent)
├── .github/                 ← PR template (the gate checklist)
├── tools/assemble.py        ← builds the per-language dump
├── shared/                  ← language-independent attachments (computation code), per proof
│   └── environment-check.py ← run this first (checks np.longdouble precision)
├── hu/                      ← the source language of the research
│   ├── CHANGELOG_hu.md      ← the history of the versions
│   ├── 00-introduction_hu.md
│   ├── I-language/ · II-proofs/ · III-frontier/ · appendix/
├── en/                      ← English mirror tree, identical structure
└── (further languages later: de/ · fr/ · …)
```

### Ground rules (the full rulebook: `CONTRIBUTING.md`)

- **Append-only numbering:** a new proof is always appended to the end of the sequence; an existing identifier never changes.
- **One claim — one file:** the source of truth is the chapter file; indexes only link, duplication is forbidden.
- **Package method:** a larger derivation is produced in packages whose rulebook is fixed in advance and which are approved one by one; a chapter may build only on accepted packages.
- **Language pairs:** the pair always lives on the mirror path (`hu/X/…_hu.md` ↔ `en/X/…_en.md`); synchronization is tracked by the `pair_status` field of the headers.
- **Formulas:** LaTeX in Markdown (`$...$`, and `$$...$$`).

### License and citation

Text: CC BY-SA 4.0 · Code: MIT (details: `LICENSE`). For citation: `CITATION.cff`.

---

## Magyar

Leírónyelv, amely a fizikai világot objektumorientált mintákkal írja le — nem metaforaként: minden minta számolható állításig van pontosítva, és a kvantumfizika mért eredményein van ellenőrizve.

> **Nyelvi státusz:** a kutatás **magyar nyelven** folyik (`hu/`). A párhuzamos angol tükröt (`en/`) igyekszünk naprakészen tartani, de az első eredmények magyarul jelennek meg. A fordítások terminológia-forrása a szótár-fejezet (`I-10-dictionary`).

### Olvasási sorrend

1. **`hu/00-introduction_hu.md`** — az elgondolás és a felépítés
2. **`hu/I-language/`** — a nyelv: fogalmak, törvények, tételek, szerződések (csak a bizonyított)
3. **`hu/II-proofs/`** — a számolt próbák; minden állítás itt kapja a bizonyítékát
4. **`hu/III-frontier/`** — a határ: jelölt törvények és nyitott kérdések
5. **`hu/appendix/`** — gépezet, mércék, csomag-nyomvonal

Gyors belépés: `hu/I-language/I-00-index_hu.md` és `hu/II-proofs/II-00-index_hu.md`.

### A repó szerkezete

```
oop-physics-language/
├── README.md                ← ez a fájl (többnyelvű belépési pont)
├── LICENSE · CITATION.cff · .gitignore
├── CONTRIBUTING.md          ← szerkesztési szabálykönyv (nyelvfüggetlen)
├── .github/                 ← PR-sablon (a kapu-ellenőrzőlista)
├── tools/assemble.py        ← nyelvi dump előállítása
├── shared/                  ← nyelvfüggetlen mellékletek (számoló kódok), próbánként
│   └── environment-check.py ← futtasd elsőként (a np.longdouble pontosságát nézi)
├── hu/                      ← a kutatás forrásnyelve
│   ├── CHANGELOG_hu.md      ← a változatok története
│   ├── 00-introduction_hu.md
│   ├── I-language/ · II-proofs/ · III-frontier/ · appendix/
├── en/                      ← angol tükör-fa, azonos szerkezettel
└── (később további nyelvek: de/ · fr/ · …)
```

### Alapszabályok (a teljes szabálykönyv: `CONTRIBUTING.md`)

- **Bővítésálló számozás:** új próba mindig a sor végére kerül; meglévő azonosító soha nem változik.
- **Egy állítás — egy fájl:** az igazság forrása a fejezetfájl; az indexek csak linkelnek, duplikáció tilos.
- **Csomag-módszer:** nagyobb levezetés előre rögzített szabálykönyvű, egyenként jóváhagyott csomagokban készül; a fejezet csak elfogadott csomagokra épülhet.
- **Nyelvi párok:** a pár mindig a tükör-útvonalon él (`hu/X/…_hu.md` ↔ `en/X/…_en.md`); a szinkront a fejlécek `pair_status` mezője követi.
- **Képletek:** LaTeX Markdownban (`$...$`, illetve `$$...$$`).

### Licenc és idézés

Szöveg: CC BY-SA 4.0 · Kód: MIT (részletek: `LICENSE`). Idézéshez: `CITATION.cff`.
