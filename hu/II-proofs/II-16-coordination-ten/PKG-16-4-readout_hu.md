---
id: PKG-16-4
type: package
part_of: II-16
lang: hu
pair: PKG-16-4-readout_en.md
pair_status: in-sync
doc_version: "1.3"
status: jovahagyva
builds_on: [PKG-16-3, PKG-15-4, II-11]
imports: nulla
---

# PKG-16-4 — A kiolvasás (számolás-csomag)

**A csomag dolga.** A hurok zárása a legmagasabb kiterjedésű álló sáv győztesén ([PKG-16-3, V5](PKG-16-3-race_hu.md)): a J5 honos szövésen, az N = 130 902 zárt fokon, a [szabálykönyv §8](PKG-16-1-rulebook_hu.md) jegyzőkönyvével és az új, mintavételes vetítő-pecséttel. A szkript: `shared/II-16-coordination-ten/PKG-16-4-readout.py`.

## 1. Eredmények

| Mérés | Érték |
|---|---|
| zárt fok | a rés a 130 902. fok fölött **0,267949192 = 2 − √3**, egzaktul |
| szomszéd-közelség | +0,127554 |
| **átellenes visszhang** (kötelező sor) | **−0,010955** — negatív, a szomszéd **8,6%-a** |
| ugrás (előjeles listán) | a **10. hely** után, 8,2-szeres — pontosan a tíz egységlépés |
| régi abszolút szabály | szintén a 10. hely után, 7,3-szeres |
| sáv-őrszem | **S = 7,29** (küszöb 2); legerősebb elutasított: a (0,0,1,1,1) hármas-átló osztály (−0,0175) |
| teljesség-számla | **1 244 160 / 1 244 160; fantom 0; hiányzó 0** |
| golyó (r = 0..5) | **1, 11, 61, 231, 681, 1683** — egzaktul a negyedrendű sor |
| vetítő-pecsét (64+64 módus, mag 248 832) | maradék-ág **5,1·10⁻¹⁴**; transzform-ág **9,4·10⁻¹⁶** — áll |

## 2. Ítélet

**Áll — mind a négy feltétel és a pecsét mindkét ága.** A honos győztes belülről ötkiterjedésűnek olvassa magát: a kiterjedésszám kívülről (verseny) és belülről (golyó) ugyanaz — öt.

## 3. Jegyzetek

- **A visszhang-számsor bővült és gyengül:** 12-es körbeérésen 3D −16%, 4D +17,4%, **5D −8,6%** — mind ártalmatlan; a méret-döntés harmadszor is igazolódott.
- **Az ismétlődő mintázat harmadszor:** a legerősebb elutasított megint egy közeli átló-osztály, nem a tükör-visszhang.
- **Az új pecsét-forma működik:** a maradék-ág a gráf-építésű szomszédsággal, a transzform-ág a G-tábla közvetlen (nem-FFT) összegzésével — mindkettő gépi pontosságon.

## 4. Kimenő állítások

- **R1:** az ötödik fok győztese belülről negyedrendű golyójú — a honos fok kívül-belül öt.
- **R2:** a visszhang-számsor háromelemű, mind a 12-es körbeérésen, mind ártalmatlan.
- **R3:** a mintavételes vetítő-pecsét bevizsgált, működő forma — a sűrű pecsét kiváltása nagy rendszeren áll.
