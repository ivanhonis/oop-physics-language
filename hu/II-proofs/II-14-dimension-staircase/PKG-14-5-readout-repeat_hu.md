---
id: PKG-14-5
type: package
part_of: II-14
lang: hu
pair: PKG-14-5-readout-repeat_en.md
pair_status: in-sync
doc_version: "1.3"
status: jovahagyva
builds_on: [PKG-14-4, PKG-14-1, II-11]
imports: "nulla új tétel (az őrszem-küszöb — kettes tényező — deklarált konvenció)"
---

# PKG-14-5 — Az újrakiolvasás rögzített hatókörrel (ismétlés-csomag)

**A csomag dolga.** A [PKG-14-4](PKG-14-4-readout_hu.md) méret-diagnózisa — a 12-es szövésen a kiolvasás tiszta — hatókörön kívül, jelöltként született. Ez a csomag ugyanazt a kiolvasást rögzített hatókörrel ismétli meg, a II/14 két szabály-tanulságának beépítésével, hogy a jelölt tétellé lépjen — vagy kimondva bukjon.

## 1. A rögzített hatókör (a futtatás előtt)

- **Rendszer:** J3 tér-szövés, 12×12×12, hatos koordináció, 5184 egységnyi simasági szerződés; körbeérés minden irányban 12 lépés.
- **Töltés (determinisztikus szabály):** a fél-töltéshez legközelebbi zárt fok felülről.
- **Javítás 1 — előjeles ugrás:** az ugrás az előjeles közelség-listán keresendő, nem az abszolút értékén; az átellenes osztály előjelével együtt külön jelentendő. (A II/14 előjel-hézagjának zárása.)
- **Javítás 2 — sáv-őrszem:** a leggyengébb elfogadott és a legerősebb elutasított közelség hányadosa jelentendő; kettes tényező alatt az olvasat részleges. A küszöb deklarált konvenció; viszonyítás: a 8-as szövés bukott esete 1,0-t adna. (A szűk „egzakt egyezés"-alak tágítása.)
- **Teljesség-számla:** megtalált / hiányzó / fantom, mindhárom számmal.
- **Golyó-olvasat:** r ≤ 5-ig (érvényesség: 2r < 12), a tér négyzetes hivatkozási sora ellen: 1, 7, 25, 63, 129, 231 (növekmény 4r² + 2).
- **Kétutas szabály:** a létra és a vetítő zárt alakban és gépi sajátfeladattal is.
- **Ítélet-feltételek előre:** Á1 — a zárt fok áll; Á2 — 5184/5184, nulla fantom, nulla hiányzó; Á3 — a golyó egzakt; Á4 — őrszem ≥ 2. Mind áll → **áll**; bármelyik bukik → részleges, a bukott feltétel megnevezésével.

## 2. Eredmények

| Mérés | Érték |
|---|---|
| létra két úton | egyezés 1,1·10⁻¹⁴-en belül |
| zárt fok | N = 934 (= 794 + 140-es polc); fél-töltés 864; rés a fok fölött 0,2679 |
| vetítő két úton | egyezés 2,8·10⁻¹⁶-on belül |
| szomszéd-közelség | +0,166146 |
| **átellenes visszhang** | **−0,026620** — előjele negatív, nagysága a szomszéd **16,0%-a** |
| ugrás (előjeles listán) | a 6. hely után, **8,9-szeres** |
| sáv-őrszem | **S = 2,84** (küszöb: 2) — a legerősebb elutasított nem az átellenes, hanem az (1,1,1) testátló-osztály (−0,058427) |
| régi abszolút szabály (összevetésül) | ugrás szintén a 6. hely után, de csak 2,8-szeres |
| teljesség-számla | **5184/5184; fantom 0; hiányzó 0** |
| golyó (r = 0..5) | **1, 7, 25, 63, 129, 231** — növekmény 6, 18, 38, 66, 102, egzaktul 4r² + 2 |

## 3. Ítélet

**Áll — mind a négy előre rögzített feltétel teljesül.** A PKG-14-4 méret-diagnózisa jelöltből tétel: hatos koordináción a 8-as szövés átellenes visszhangja méret-műtermék — a 12-es szövésen a hurok hiánytalanul zárul, és a visszhang a szomszéd-közelség 16%-ára esik (a 8-ason 100% volt, egzakt egyezéssel).

**Ráadás-lelet, számmal:** az előjeles szabály haszna mérhető — az előjeles listán az ugrás 8,9-szeres, az abszolút-értékesen ugyanitt csak 2,8-szeres, mert a lista második felét negatív osztályok vezetik. A biztonsági sávot tehát a javítás több mint háromszorozza. És a sáv-őrszemet e méreten már nem az átellenes visszhang korlátozza, hanem egy közönséges közeli osztály (a testátló) — a tükör-visszhang a kérdéses tartományból kiesett.

## 4. Amit ez a csomag nem bizonyít

Nyolcas koordinációról és más szövésről (BCC, hiperkocka) nem mond semmit — ott a visszhang-kérdés a II/15 saját őrszemének dolga. A kettes küszöb konvenció, nem levezetett szám.

## 5. Kimenő állítások

- **K1:** a 12-es tér-szövésen a kiolvasás hiánytalan: 5184/5184, nulla fantom, a golyó r = 5-ig egzaktul négyzetes.
- **K2:** az átellenes visszhang a mérettel elhal: 8-as szövésen 100% (egzakt), 12-esen 16%, előjele negatív; e méreten már nem az őrszem korlátja.
- **K3:** az előjeles ugrás-szabály élesebb az abszolútnál (8,9 kontra 2,8) — a II/15 jegyzőkönyvének hivatkozási alapja.
- **K4:** a II/15 méret-döntésének tapasztalati támpontja — a 12-es körbeérés elegendő — hatos koordináción hatókörön belül igazolt tény.
