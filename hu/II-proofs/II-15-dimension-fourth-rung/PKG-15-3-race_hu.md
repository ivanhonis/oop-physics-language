---
id: PKG-15-3
type: package
part_of: II-15
lang: hu
pair: PKG-15-3-race_en.md
pair_status: in-sync
doc_version: "1.4"
status: jovahagyva
builds_on: [PKG-15-2]
imports: nulla
---

# PKG-15-3 — A verseny (számolás-csomag)

**A csomag dolga.** A [PKG-15-2](PKG-15-2-ladders_hu.md) létráira építve lefuttatja a versenyt N = 1-től 20736-ig mind az 503 indulón, kimondja a [szabálykönyv §7](PKG-15-1-rulebook_hu.md) szerinti lépcső-ítéletet, ellenőrzi az előre regisztrált tényeket, és megválaszolja a három regisztrált kérdést. A szkript: `shared/II-15-dimension-fourth-rung/PKG-15-3-race.py`.

## 1. Az előre regisztrált tények — mind áll

N = 1-nél mind az 503 induló nullát fizet; N = 2-nél pontosan a 16 széteső tag áll nullán; N = 3-nál a hárompéldányos (3, 6, 9, 12) egyedül; a teli töltésnél minden induló ára 165888, az elsődleges (hosszú-lebegős) úton 8,4·10⁻¹² eltérésen belül.

## 2. A győztes-tábla a fő négyesen — és az ítélet

| Győztes | Tartomány | Hossz |
|---|---|---|
| holtverseny (mind a négy) | 1 | 1 |
| J1 — vonal | 2 .. 4217 | 4216 |
| J2 — sík | 4218 .. 7964 | 3747 |
| **J4 — négykiterjedés** | **7965 .. 15996** | **8032** |
| **J3 — tér** | **15997 .. 20734** | **4738** |
| holtverseny (J3 + J4) | 20735 | 1 |
| holtverseny (mind a négy) | 20736 | 1 |

Mindhárom felső sáv összefüggő és folt-mentes; a négykiterjedés sávja a legnagyobb mind közül, és **a fél-töltés (10368) a négykiterjedés sávjában ül**.

**Ítélet: részleges — a sávszerkezet teljes, de a sorrend nem monoton.** A §7 teljes-igen definíciója (sík → tér → négykiterjedés növekvő sűrűséggel) nem teljesül, és a néven nevezett „megáll a háromnál" eset sem áll, mert a negyedik fok igenis áll. A mért lelet, néven nevezve: **a negyedik fok áll — a középső sűrűségsávot nyeri —, de a tető a háromé: a lépcső a tetején visszafordul** (vonal, sík, négykiterjedés, tér).

## 3. A három regisztrált kérdés válasza

**K-a (héj-illeszkedés): nem áll élesen.** A sávhatárok távolsága a bejövő győztes legközelebbi zárt fokától: 1, 3, 112, illetve 2 töltés. A sávhatár a költséggörbék metszéspontja, nem a bejövő polc-határ — a héj-szabály ([III/1, 6.](../../III-frontier/III-01-candidate-laws_hu.md)) hatóköre ennek megfelelően szűkítendő.

**K-b (tükör-kérdés): a szélesség nem dönt — az alak dönt, és a tükör-szabály élesített alakban megerősítve.** A két páros jelölt létra-szélessége azonos (mindkettő legmagasabb üteme pontosan 16), mégis határozott a sorrend. A felső felet (N > 10368) **kizárólag a tükör-jegyű pár nyeri** — minden egyes felső töltés a J3-é vagy a J4-é —, ami a [III/1, 7.](../../III-frontier/III-01-candidate-laws_hu.md) eddigi legélesebb megerősítése. A páron belül viszont a tetőn a sorrend megfordul: a teli vég a ritka vég tükörképe (a verseny ott a lyukakról szól), és ritkán az alacsonyabb kiterjedés az olcsóbb — ezért a tetőn a tér veri a négykiterjedést. Ennek szép pecsétje az N = 20735-ös **egzakt** J3–J4 holtverseny: egyetlen lyuknál mindkettő a 16-os csúcs-ütemét adja fel.

**K-c (fésű-minta): áll.** Az alsó tartományban a széteső többszörözések — a (2, 4, 6, 8) és a (3, 6, 9, 12) — váltakoznak holtversenyekkel, a II/14 maradékosztály-mintája szerint.

## 4. A teljes mezőny — a vonal-imitáció ismét, élesebben

A teljes 503-as mezőnyben **a fő négyes egyetlen töltést sem nyer szigorúan** (2346 töltés holtversenyes): minden töltésen a vonal-család egy hangolt tagja a legolcsóbb vagy holtversenyben áll. A legtöbb töltést nyerő imitátorok: (3, 5, 6, 10) — 2747; (3, 7, 8, 9) — 2042; (1, 3, 5, 7) — 2021. A II/14 mezőny-lelete tehát megismétlődik és élesedik; a gyökér-jelzés súlya nő: a kiválasztás szabad, kézzel felsorolt hálók közt nem dől el — ott dől el, ahol a szerződések születnek ([III/2, 7.](../../III-frontier/III-02-open-questions_hu.md)).

## 5. Számolási helyesbítés (H3)

A rögzített 10⁻⁸ azonosság-tűrés float64 úton nem alkalmazható a teli vég közelében: a halmozási hiba ott 1,9·10⁻⁸. **Az elsődleges út ezért hosszú-lebegős** (halmozási eltérés legfeljebb 8,4·10⁻¹², négy nagyságrenddel a tűrés alatt); a float64 keresztellenőrzés győztes-sora pontosan 2 töltésen tér el (20735–20736), ott, ahol valódi holtverseny van — az eltérés lokalizált és megértett.

## 6. A kiolvasás előkészítése — értelmezési jegyzet és a rögzített választás

A [szabálykönyv §8](PKG-15-1-rulebook_hu.md) „legmagasabb álló fok" kifejezésének zárójeles felsorolása a mért esetet nem látta előre (a negyedik fok áll, de nem a tetőn). **Értelmezési jegyzet, rögzítve:** a „fok" a lépcső foka, azaz kiterjedésszám — a kiolvasás a legmagasabb *kiterjedésű* álló sáv győztesén fut: **a J4-en, a 7965..15996 sávban.** Zárt fok választása (determinisztikus szabály, rögzítve): a sáv legszélesebb rései (mind 2 − √3 ≈ 0,267949 szélességű, e zárt fokok fölött: 8077, 9661, 11075, 12659, 13835, 14331, 15259) közül a fél-töltéshez legközelebbi felülről: **N = 11075.**

## 7. Kimenő állítások (a PKG-15-4 ezekre építhet)

- **V1:** a győztes-tábla a 2. szakasz szerint; mindhárom felső sáv folt-mentes.
- **V2:** az ítélet: részleges — „a negyedik fok áll, a tető a háromé"; se a teljes-igen, se a „megáll a háromnál" nem a mért eset.
- **V3:** a felső felet kizárólag a tükör-jegyű pár nyeri; a páron belül a tetőn a sorrend fordított (K-b).
- **V4:** a teljes mezőnyben a fő négyes szigorú győzelme nulla — a vonal-imitáció ismét áll (mezőny-lelet).
- **V5:** az elsődleges számolási út hosszú-lebegős (H3); a float64 eltérés a teli végre lokalizált.
- **V6:** a kiolvasás rendszere: J4, 12×12×12×12, a 7965..15996 sáv, zárt fok **N = 11075**, a fölötte lévő rés 2 − √3.
- **V7:** a golyó-hivatkozási sorok a szabálykönyv §5 táblája szerint; az ítélethez r ≤ 3, jelentéshez r ≤ 5 (a J4-en éppen érvényes).
