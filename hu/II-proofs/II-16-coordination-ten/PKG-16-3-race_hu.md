---
id: PKG-16-3
type: package
part_of: II-16
lang: hu
pair: PKG-16-3-race_en.md
pair_status: missing
doc_version: "1.3"
status: jovahagyva
builds_on: [PKG-16-2]
imports: nulla
---

# PKG-16-3 — A verseny (számolás-csomag)

**A csomag dolga.** A verseny N = 1-től 248 832-ig mind a 805 indulón (áramoltatott top-2 követéssel), a [szabálykönyv §7](PKG-16-1-rulebook_hu.md) négyfokú ítélete, a regisztrált kérdések. A szkript: `shared/II-16-coordination-ten/PKG-16-3-race.py` (szakaszolt, újraindítható).

## 1. Az előre regisztrált tények — mind áll

N = 1-nél mind a 805 induló nullán; N = 3-nál nulla-költségű induló nincs (a legjobb ár a széteső példány első nemnulla üteme, ~1,4·10⁻⁷ — pozitív, csak a kiírás kerekíti); a teli töltésnél a kötelező döntetlen 2 488 320-on, 1,4·10⁻⁹ hosszú-lebegős halmozási eltéréssel a tűrés alatt.

## 2. A győztes-tábla a fő ötösön — és az ítélet

| Győztes | Tartomány | Hossz |
|---|---|---|
| holtverseny (mind az öt) | 1 | 1 |
| J1 — vonal | 2 .. 42 661 | 42 660 |
| J2 — sík | 42 662 .. 85 085 | 42 424 |
| **J4 — négykiterjedés** | **85 086 .. 125 563** | 40 478 |
| **J5 — ötkiterjedés (honos)** | **125 564 .. 248 831** | **123 268** |
| holtverseny (mind az öt) | 248 832 | 1 |

**Ítélet: részleges — két néven nevezett lelettel.** **(1) A lépcső kihagyja a hármat:** a tér-jelöltnek egyetlen győztes töltése sincs — a sorrend vonal, sík, négykiterjedés, ötkiterjedés; a lépcső foka tehát ki is maradhat. **(2) A tető a honosé:** a fél-töltés fölötti tartomány szinte teljes egészében (a felső fél megoszlása: J5 — 123 268, J4 — 1147) az egyetlen tükör-jegyű fő jelölté.

## 3. K-a — a próba fő kérdésének válasza, és az egyesített olvasat

A két hipotézis szétvált, és **a „tükör uralja a tetőt" győzött; a „tető-hármas" minta megtört.** A három próba együtt olvasva: hatos koordináción a tető a téré (ott a tér az egyetlen páros fő jelölt); nyolcason a téré (ott a páros pár alacsonyabbika); tízesen az ötkiterjedésű honosé (itt az az egyetlen páros). **Az egyesített jelölt-törvény szövege: a tetőt a tükör-jegyű jelöltek közül a legalacsonyabb kiterjedésű viszi** — az „a tükör-jegyűek közül" fele a mért III/1, 7.; a „közülük a legalacsonyabb" felét a lyuk-tükör + irány-tétel adja tételként. A „miért három" korábbi tető-olvasata ezzel átminősül: a hatos és nyolcas koordináción a legalacsonyabb tükör-hordozó kiterjedés *történetesen* a három.

## 4. A többi regisztrált kérdés

**K-b (fésű):** az alsó tartományban egyedül a (2, 4, 6, 8, 10) kettőző jelenik meg holtversenyek közt — a hatos széteső-készlettel a minta alkalmazkodott alakban áll. **K-c (dominancia-hézag):** mind a tíz páron kimérve; az arány 27–61% — a ~fele-minta lazábban, de ismétlődik; a legkisebb arány (27%) a J4–J5 páron. **K-d (héj-illeszkedés):** vegyes — a J2 és J4 sávkezdete meglepően éles (1, illetve 3 töltésre a bejövő zárt foktól), a J5-é messze (5338); a héj-szabály hatóköre tovább pontosítandó.

## 5. A teljes mezőny

A fő ötös **nulla töltést nyer szigorúan** (30 227 töltés holtversenyes); a legtöbbet nyerő imitátorok: (2, 6, 9, 11, 12) — 34 430; (4, 9, 10, 11, 12) — 32 728; **(1, 3, 5, 7, 9) — 19 521, maga is páros-jegyű**: a tükör-imitáció jelensége — a vonal-család a tető tartományában is jelen van, a saját páros tagjaival. A mezőny-lelet és a gyökér-jelzés harmadszor is erősödik.

## 6. A kiolvasás előkészítése

A legmagasabb kiterjedésű álló sáv a J5-é (125 564 .. 248 831); a sáv legszélesebb rése ismét 2 − √3; a rögzített választási szabállyal a zárt fok: **N = 130 902.**

## 7. Kimenő állítások

- **V1:** a győztes-tábla a 2. szakasz szerint; a J3-nak nincs sávja.
- **V2:** az ítélet két néven nevezett lelete: „a lépcső kihagyja a hármat" és „a tető a honosé".
- **V3:** az egyesített tető-törvény jelölt-szövege (3. szakasz) — a III/1 frissítésének alapja.
- **V4:** a fő ötös szigorú győzelme nulla; a tükör-imitáció új jelenségként regisztrálva.
- **V5:** a kiolvasás rendszere: J5, 12⁵, N = 130 902, a rés 2 − √3.
- **V6:** a tíz pár dominancia-küszöbe és átbillenése (K-c tábla a futási naplóban) — a PKG-16-5 bemenete.
