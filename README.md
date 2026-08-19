---
id: README
type: entry-point
lang: multi
doc_version: "1.3"
status: ervenyes
---

# OOP-alapú fizikai leírónyelv · OOP-based physical descriptive language

**[Magyar](#magyar)** · **[English](#english)**

---

## English

A descriptive language that models the physical world with object-oriented patterns — not as metaphor: every pattern is sharpened until it yields a computable claim, and that claim is checked against measured quantum-physics results.

> **Language status:** the research is conducted in **Hungarian** (`hu/`). We aim to keep the English mirror (`en/`) up to date, but new results appear in Hungarian first. Terminology for translations is fixed in the dictionary chapter (`I-10-dictionary`).

Start here: `hu/00-introduction_hu.md` (English mirror coming as `en/00-introduction_en.md`).

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
descriptive-language/
├── README.md                ← ez a fájl (többnyelvű belépési pont)
├── LICENSE · CITATION.cff · .gitignore
├── .github/                 ← PR-sablon (a kapu-ellenőrzőlista)
├── tools/assemble.py        ← nyelvi dump előállítása
├── shared/                  ← nyelvfüggetlen mellékletek (számoló kódok), próbánként
├── hu/                      ← a kutatás forrásnyelve
│   ├── CONTRIBUTING_hu.md   ← szerkesztési szabálykönyv
│   ├── CHANGELOG_hu.md      ← a változatok története
│   ├── 00-introduction_hu.md
│   ├── I-language/ · II-proofs/ · III-frontier/ · appendix/
├── en/                      ← angol tükör-fa, azonos szerkezettel (készül)
└── (később további nyelvek: de/ · fr/ · …)
```

### Alapszabályok (a teljes szabálykönyv: `hu/CONTRIBUTING_hu.md`)

- **Bővítésálló számozás:** új próba mindig a sor végére kerül; meglévő azonosító soha nem változik.
- **Egy állítás — egy fájl:** az igazság forrása a fejezetfájl; az indexek csak linkelnek, duplikáció tilos.
- **Csomag-módszer:** nagyobb levezetés előre rögzített szabálykönyvű, egyenként jóváhagyott csomagokban készül; a fejezet csak elfogadott csomagokra épülhet.
- **Nyelvi párok:** a pár mindig a tükör-útvonalon él (`hu/X/…_hu.md` ↔ `en/X/…_en.md`); a szinkront a fejlécek `pair_status` mezője követi.
- **Képletek:** LaTeX Markdownban (`$...$`, illetve `$$...$$`).

### Licenc és idézés

Szöveg: CC BY-SA 4.0 · Kód: MIT (részletek: `LICENSE`). Idézéshez: `CITATION.cff`.
