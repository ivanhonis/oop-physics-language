---
id: PKG-15-4
type: package
part_of: II-15
lang: hu
pair: PKG-15-4-readout_en.md
pair_status: in-sync
doc_version: "1.4"
status: jovahagyva
builds_on: [PKG-15-3, PKG-14-5, II-11]
imports: nulla
---

# PKG-15-4 — A kiolvasás (számolás-csomag)

**A csomag dolga.** A hurok zárása a legmagasabb kiterjedésű álló sáv győztesén ([PKG-15-3, V6](PKG-15-3-race_hu.md)): a J4 hiperkocka-szövésen, az N = 11075 zárt fokú töltésen, a [szabálykönyv §8](PKG-15-1-rulebook_hu.md) jegyzőkönyvével. A szkript: `shared/II-15-dimension-fourth-rung/PKG-15-4-readout.py`.

## 1. Eredmények

| Mérés | Érték |
|---|---|
| zárt fok | a rés a 11075. fok fölött **0,267949192 = 2 − √3**, egzaktul a várt érték |
| szomszéd-közelség | +0,142661 |
| **átellenes visszhang** (kötelező sor) | **+0,024836** — előjele ezúttal **pozitív**, nagysága a szomszéd **17,4%-a** |
| ugrás (előjeles listán) | a **8. hely** után, 5,7-szeres — pontosan a nyolc egységlépést jelöli ki |
| régi abszolút szabály (összevetésül) | szintén a 8. hely után, 5,4-szeres |
| sáv-őrszem | **S = 5,37** (küszöb: 2) — a legerősebb elutasított nem az átellenes, hanem a (0,1,1,1) hármas-átló osztály (−0,026563) |
| teljesség-számla | **82944/82944; fantom 0; hiányzó 0** |
| golyó (r = 0..5) | **1, 9, 41, 129, 321, 681** — egzaktul a köbös hivatkozási sor, az ítéleti r ≤ 3 határon és a teljes r ≤ 5 jelentési tartományban is |
| kétutas pecsét | a vetítő zárt (FFT) és gépi (dense sajátfeladat, sajátvektorokkal) útja közt a legnagyobb eltérés **1,67·10⁻¹⁵** |

## 2. Ítélet

**Áll — mind a négy előre rögzített feltétel teljesül, és a kétutas pecsét is.** A negyedik fok győztese belülről négykiterjedésűnek olvassa magát: a visszarakó vakon, hiánytalanul és fantom nélkül visszaadja mind a 82944 szerződést, a golyó pedig az érvényességi tartomány végéig egzaktul köbös. A bukás-ágra (a foglalt PKG-15-5 névre) nem volt szükség.

## 3. Jegyzetek

- **A méret-döntés igazolódott.** A 12-es körbeérésen a páros visszhang (17,4%) a kritikus zónán kívül van — a [PKG-14-5](../II-14-dimension-staircase/PKG-14-5-readout-repeat_hu.md) hármas-kiterjedésű mintája (16%) nyolcas koordináción, négy kiterjedésben is áll. A visszhang-számsor bővült: 3D-hatos, 8-as körbeérés: 100% (bukás); 3D-hatos, 12-es: −16%; 4D-nyolcas, 12-es: +17,4%.
- **Az előjeles szabály itt kevesebbet tett hozzá** (5,7 kontra 5,4), mert a visszhang előjele ezúttal pozitív — az őrszem viszont előjeltől függetlenül fog; a jegyzőkönyv mindkét esetre jó.
- **Ismétlődő mintázat:** a legerősebb elutasított osztály mindkét kiolvasásban egy közeli átló-osztály (ott az (1,1,1), itt a (0,1,1,1)), nem a tükör-visszhang — e méreteken az őrszem korlátja közönséges geometria, nem a szimmetria.

## 4. Kimenő állítások

- **R1:** a negyedik fok győztese belülről köbös golyójú — a kiterjedésszám a győztes sávban kívülről (verseny) és belülről (golyó) ugyanaz: négy.
- **R2:** a páros visszhang mérete a körbeéréssel szabályozott, koordinációtól és kiterjedéstől függetlenül ártalmatlan a 12-es körbeérésen.
- **R3:** a kétutas pecsét 1,7·10⁻¹⁵ — a zárt és a gépi út gépi pontosságon egyezik.
