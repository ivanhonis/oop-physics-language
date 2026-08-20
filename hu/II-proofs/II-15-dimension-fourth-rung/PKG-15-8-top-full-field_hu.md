---
id: PKG-15-8
type: package
lang: hu
pair: PKG-15-8-top-full-field_en.md
pair_status: missing
doc_version: "1.4"
status: jovahagyasra-var
part_of: II-15
builds_on: [PKG-15-1, PKG-15-2, PKG-15-3, PKG-16-5]
imports: nulla
---

# PKG-15-8 — A teljes mezőny teteje nyolcas koordináción (vak-jóslat csomag)

**Egy mondatban.** A [tető-törvény](../../III-frontier/III-01-candidate-laws_hu.md) mért felének hiányzó harmadik támpontja: nyolcas koordináción a teljes mezőny teli végét mind a 2000 töltésen a **tükör-jegyű (1, 3, 5, 7) vonal-tag** viszi — pontosan az az induló, amelyet a jóslat a számolás előtt megnevezett.

## 1. Kérdés (a számolás előtt rögzítve)

Nyolcas koordináción a **teljes mezőny** tetejét tükör-jegyű vonal-tag viszi-e, ahogy a tető-törvény állítja — és melyik?

Ez a `P1.1` mérföldkő. A kérdés azért nyitott, mert a [PKG-15-3](PKG-15-3-race_hu.md) csak annyit mondott ki, hogy ott a fő négyes egyetlen töltést sem nyer szigorúan; a tetőn álló vonal-imitátort nem nevezte meg, és a legtöbbet nyerő háromból kettő — a (3, 5, 6, 10) és a (3, 7, 8, 9) — páros lépést is tartalmaz, tehát **nem** tükör-jegyű. Az eredmény ezért nem volt sejthető.

## 2. A vak-protokoll — a csomag lényege

A jóslat a számolás **létezése előtt** rögzült, pecséttel és idő-horgonnyal:

| | |
|---|---|
| bejegyzés | `JOS-01` (`shared/register/predictions.json`) |
| pecsét | `4332b12717f2c30b…` (SHA-256 a rögzített mezőkön) |
| idő-horgony | commit `751fbab`, 2026-08-20 13:56:34 +02:00 |
| ellenőrzés | `python shared/register/seal.py` |

A pecsét a jóslat-mondatot, a megnevezett győztest, a levezetést, az ablakot és a siker/bukás-feltételeket fedi; ezek a futás óta bizonyíthatóan nem változtak. A számolást végző szkript a pecsételő commit **után** készült.

**A jóslat levezetése** (a `JOS-01`-ben, változatlanul): (i) a tetőt tükör-jegyű tag viszi — mért, hatoson és tízesen; (ii) a vonal-családon a tükör-jegy csupa-páratlan lépést jelent; (iii) a „legalacsonyabb kiterjedésű" kitétel a vonalra mutat; (iv) egyenlő kiterjedésen a törvény nem dönt, ezért döntetlen-törőnek a repó saját [kiválasztási szabályát](../II-16-coordination-ten/PKG-16-1-rulebook_hu.md) alkalmaztuk: legkisebb össz-lépésnégyzet. A 15 csupa-páratlan négyes közül az **(1, 3, 5, 7)** a minimum (84).

## 3. Bemenetek

- **[PKG-15-1](PKG-15-1-rulebook_hu.md)**: a rögzített rendszer (20736 hely, nyolcas koordináció) és a mezőny — 495 négylépéses családtag, 4 fő jelölt, 4 kontroll.
- **[PKG-15-2](PKG-15-2-ladders_hu.md)**: a mentett létrák a fő és kontroll indulókhoz, valamint 24 családtaghoz.
- **[PKG-16-5](../II-16-coordination-ten/PKG-16-5-transfer_hu.md)**: a leolvasás mintája — a teli vég 2000 töltése tízes koordináción; az ablak abszolút mérete innen öröklődik, hogy a két eredmény közvetlenül összevethető legyen.
- **H4** ([B függelék](../../appendix/B-machinery_hu.md)): a hordozható összegzési út, `shared/summation.py`.

## 4. Kötelező előfeltétel — független újraszámolás

A létrákat itt **zárt Fourier-alakból** építjük, nem a gépezetből. A kettő egyezése a kétutas szabály új, algoritmus-alapú alakja:

> A 24 mentett családtag-létra és a zárt alakú újraszámolás legnagyobb eltérése **$1{,}293\cdot10^{-12}$** (tűrés $10^{-8}$) — **áll**.

Ez egyben a [PKG-15-2](PKG-15-2-ladders_hu.md) közzétett $1{,}30\cdot10^{-12}$-jének független megerősítése, **más algoritmussal**.

## 5. A számolás

- **Mezőny:** 495 családtag zárt alakból + 8 mentett fő/kontroll létra = **503 induló**.
- **Költséggörbék:** a H4 hordozható úton, mind az 503 indulóra.
- **Beépített ellenőrzés:** az egzakt nyomösszeg ($2\cdot4\cdot20736 = 165888$) mind az 503 indulón — legnagyobb eltérés $2{,}910\cdot10^{-11}$, **áll**.
- **Tükör-jegy létrából:** a $d$-reguláris háló akkor páros, ha a színképe a $d$ körül szimmetrikus, azaz a létra és a $2d - \text{létra}$ ugyanaz a halmaz. Így a jegy a **mentett** fő és kontroll létrákon is eldönthető, ahol a lépéslista nincs meg. Eredmény: **20 tükör-jegyű induló** az 503-ból.
- **Rendfüggetlenség:** a párhuzamos futtató 6 mintafeladata sorosan újraszámolva **bitre azonos**.
- **A verseny:** az ablak minden töltésén a legolcsóbb induló(k), a rögzített $10^{-8}$ tűréssel.

Futtatható alak: `shared/II-15-dimension-fourth-rung/PKG-15-8-top-full-field.py`.

## 6. Eredmény

Az ablak: $N = 18737 \ldots 20736$, 2000 töltés. Egyértelmű győztes 1998 töltésen, holtverseny 2-n.

| Induló | Nyert töltés | Tükör-jegyű |
|---|---|---|
| **(1, 3, 5, 7)** | **2000** | igen |
| K3, K1, K2, (3,7,9,11), (3,5,9,11), (3,5,7,9), (5,7,9,11) | 2 (holtversenyben) | igen |

A fő négyes — vonal, sík, tér, négykiterjedés — az ablakban **egyetlen töltést sem nyer**.

## 7. Ítélet a `JOS-01` rögzített feltételei szerint

| Feltétel | Eredmény |
|---|---|
| **S1** — a 2000 töltésből ≥ 1900 tükör-jegyűé | **áll**: megengedő olvasat 2000/2000, szigorú olvasat 1999/2000 |
| **S2** — a legtöbbet nyerő az (1, 3, 5, 7) | **áll** — mind a 2000 töltésen |
| **B3** — a holtverseny uralja az ablakot | **nem vált ki** (2000-ból 2) |

**A jóslat beállt.**

**Utólagos jegyzet, kimondva, nem elsimítva.** A `JOS-01` rögzítette az ablakot és a küszöböket, de **nem rögzítette a holtverseny beszámítását**. Ezért mindkét olvasat jelentve áll; a különbség egyetlen töltés, tehát az ítéletet nem érinti. A holtverseny-szabály előzetes rögzítése a következő regisztráció tanulsága — nem most, a képernyőn álló számok ismeretében eldöntendő kérdés.

## 8. Import-számla

Új import: **nulla.** A rendszer, a mezőny és a lépés-plafon a PKG-15-1-ből örökölt; az ablak mérete a PKG-16-5-ből; a döntetlen-törő a kiválasztási szabály (kimondott konvenció, `KON-02`). A tükör-jegy létrából való eldöntése levezetett spektrális tény, nem új feltevés.

## 9. Ítélet erről a csomagról

**Áll.** Az előfeltétel teljesült, a beépített ellenőrzés áll, a rendfüggetlenség igazolt, és a vak-jóslat mindkét feltétele beállt.

## 10. Kimenő állítások

- **K1:** Nyolcas koordináción a teljes mezőny (503 induló) teli végét — $N = 18737\ldots20736$ — az **(1, 3, 5, 7)** tükör-jegyű vonal-tag viszi, mind a 2000 töltésen.
- **K2:** Az ablakban minden minimális induló tükör-jegyű, egyetlen töltés kivételével (1999/2000 a szigorú olvasatban).
- **K3:** A fő négyes az ablakban egyetlen töltést sem nyer — a [PKG-15-3](PKG-15-3-race_hu.md) mezőny-lelete a teli végen is megerősítve.
- **K4:** A tető-törvény **mért fele** ezzel a teljes mezőnyön **háromból háromra** áll (hatos, nyolcas, tízes koordináció). A [III/1, 8.](../../III-frontier/III-01-candidate-laws_hu.md) táblájának „nincs megnézve" cellája kitölthető, és a 8.(a) hiányzó tétel törölhető.
- **K5:** A nyolcas koordináción a legalacsonyabb tükör-hordozó a **vonal** (egy kiterjedés) — nem a három. A „miért három" kérdés alakváltása ezzel a harmadik koordináción is megerősítve: a hordozó-kérdés (III/1, 8.b) a nyitott.

> A K1–K5 csak e csomag **jóváhagyása után** építhető be a fejezetekbe; addig a [III/1](../../III-frontier/III-01-candidate-laws_hu.md) és [III/2](../../III-frontier/III-02-open-questions_hu.md) szövege változatlan.
