---
id: EXTENSION
type: rulebook
lang: hu
pair: EXTENSION_en.md
pair_status: missing
doc_version: "1.4"
status: jelolt
---

# A hatodik törvény — nyelvbővítési terv

**Egy mondatban.** A nyelv ma szabályozza, hogy **az állapotot** ki birtokolja, de nem szabályozza, hogy **a szerződést** ki birtokolja — ezért a szerződésháló kézi bemenet marad, és ezen áll minden, ami eddig nem dőlt el. Ez a terv azt rögzíti, mit kell a nyelvhez hozzátenni, mibe kerül, és mi lesz az eddigi tizenhat próbával.

Ez **terv, nem eredmény**. A bevezetés feltétele a II/17 lefutása; addig a hatodik törvény jelölt.

---

## 1. A hiány, három irányból ugyanaz

A repó három független úton érkezett ugyanahhoz a ponthoz:

- **[II/12](II-proofs/II-12-network-race/proof_hu.md), a bukás gyökér-jelzése:** *„a szerződés a nyelvben ingyen erőforrás — a fizikában a csatolást a példányok hordozzák; a kiválasztás ott dőlhet el, ahol a szerződések maguk születnek."*
- **[PKG-15-9](II-proofs/II-15-dimension-fourth-rung/PKG-15-9-uniform-field_hu.md), a kiválasztási konvenció mérése:** a fő mezőny mintája **konvenció-műtermék** — a kézzel felsorolt hálók közt a kiválasztás nem dől el.
- **A függőségi audit (`P0.1`):** a hidrogén-egyezés **két be nem vezetett bemeneten** áll — a kiterjedésszámon (`IMP-04`) és a vonzásalakon (`IMP-02`).

Mindhárom ugyanarra mutat: **a nyelvben a szerződés szabályozatlan.** Ami szabályozatlan, az a modellezőre marad.

## 2. Mit kell hozzátenni — és mit nem

### A hatodik törvény (jelölt)

> **A szerződést a példányok hordozzák.** A szerződés tartalma nem szabad bemenet: a példányok kész állapota **generálja**. A rendszer akkor van egyensúlyban, ha az állapot a szerződés szerint a legolcsóbb **és** a szerződés az, amit ez az állapot generál.

Formálisan: a rendszer megadása ma egy **(példányok, szerződésháló $C$)** pár, és az egyensúly az az $s$ állapot, ami a $\text{költség}_C$-t minimalizálja. A javaslat szerint a rendszer megadása **(példányok, generáló szabály $g$)**, és az egyensúly egy **pár**:

$$s = \arg\min \text{költség}_{C}(s), \qquad C = g(s).\tag{K-EXT-1}$$

Vagyis **fixpont**. A bíró és a motor ([4. törvény](I-language/I-05-contract_hu.md)) ugyanaz marad; csak most a bíró maga is az állapotból származik.

### Amit NEM módosítunk

| Törvény | Érintett? |
|---|---|
| 1. nincs mellékhatás-mentes getter | nem |
| 2. az állapotot a rendszer birtokolja | nem — a 6. ennek a **párja** a szerződésre |
| 3. a fejlődés súlytartó | **nem** |
| 4. a szerződés bíró és motor | nem — kiegészül, nem cserélődik |
| 5. a példányazonosító nem adat | nem |

**Ez a döntő különbség a másik lehetséges úthoz képest.** A „közvetítő közeg" (saját állapotú mező a helyeken, amibe az objektumok belenyúlnak) matematikailag ugyanoda visz — és $d=3$-ban kiadja az 1/r-t —, de **a 3. törvénybe ütközik**: a közeg amplitúdója a forrással nő, tehát nem lehet rögzített összhosszú, és a fejlődése nem súlytartó. Ahhoz a 3. törvény hatókörét kellene szűkíteni („súlytartó *az objektumokra*"), ami a nyelv szerkezetének megbontása.

**A generáló szabály útja ezt elkerüli:** nem ad új hordozót, hanem *kiszámolja*, ami eddig ingyen volt.

## 3. Az ár, őszintén elszámolva

A hatodik törvény **nem szünteti meg a kézi beállítást — koncentrálja.**

| | Ma | A 6. törvénnyel |
|---|---|---|
| Kézzel adott | a teljes szerződésháló: $\binom{n}{2}$ szám, vagy egy kézzel felsorolt jelölt-lista | **egyetlen** generáló szabály, $g$ |
| A mag rangja | `KON-02`, `KON-03` + hálónként a rendszer-leírás | egy új `KON-xx`: a generáló szabály |

Ez nagyságrendi csökkenés — de **csökkenés, nem nullázás**. És ezért kötelező mérni: ha a fixpont erősen függ $g$-től, akkor csak áthelyeztük a kézi beállítást, nem szüntettük meg. A [PKG-17-1](II-proofs/II-17-contract-origin/PKG-17-1-rulebook_hu.md) épp ezért futtat **hat különböző $g$-t és két normálást**, és az ítéletet csak az egyezésükre engedi.

## 4. Mi lesz az eddigi tizenhat próbával

Semmit nem dobunk el. Minden próba **rangot kap**: a benne deklarált szerződés fixpont-e a generáló szabály szerint?

| Rang | Mit jelent | Következmény |
|---|---|---|
| **fixpont** | a deklarált szerződés az, amit az állapot generálna | az eredmény **erősödik**: a szerződés már nem önkényes választás |
| **feltételes** | nem fixpont | az eredmény érvényes marad, de **feltételes**: „ezzel a szerződéssel ez jön ki" — nem állítás a világról |
| **nem vizsgálva** | még nem futott rá a próba | könyvelési adósság, nem hiba |

**Ami eleve érintetlen.** A [teli-vég](II-proofs/II-15-dimension-fourth-rung/PKG-15-10-dense-end_hu.md), a [lyuk-létra](II-proofs/II-15-dimension-fourth-rung/PKG-15-11-hole-ladder_hu.md), a [hordozó-](II-proofs/II-15-dimension-fourth-rung/PKG-15-9-uniform-field_hu.md) és az egy-lyuk tétel **minden fokszám-reguláris hálóról** szól ([PKG-15-12](II-proofs/II-15-dimension-fourth-rung/PKG-15-12-convention-scope_hu.md)). Nem érdekli őket, honnan jött a háló — kézzel adtuk vagy a hurok generálta. **Ezek teljes egészében túlélik.**

**Ami erősödik.** A [II/11](II-proofs/II-11-locality-readout/proof_hu.md) (a szomszédság a kész állapot nézete) és a [II/6](II-proofs/II-06-universality/proof_hu.md) (a keverés alakja nem számít) éppen azt mondják, amire a hurok épül. A [II/12](II-proofs/II-12-network-race/proof_hu.md) bukása **igazolást kap**: azért nem dőlhetett el, mert a hiányzó törvény hiányzott.

**Ami átminősül.** A [II/13–II/16](II-proofs/II-00-index_hu.md) versenyei kézzel felsorolt hálókat hasonlítottak össze. A 6. törvény alatt a helyes kérdés nem az, hogy „melyik a legolcsóbb", hanem hogy „melyik a fixpont". A versenyek ezzel **diagnosztikává** válnak — ami a [PKG-15-9](II-proofs/II-15-dimension-fourth-rung/PKG-15-9-uniform-field_hu.md) után amúgy is a helyes olvasatuk.

**Ami tétre megy.** A [II/4](II-proofs/II-04-hydrogen-atom/proof_hu.md) vonzásalakja (`IMP-02`) és a kiterjedésszám (`IMP-04`). Ha a fixpont-hálónak van kiolvasható geometriája (a II/11 gépezetével), akkor a kiterjedésszám **kimenet** lesz, nem bemenet — és a szerződés tartalma a kiolvasott távolság függvényében **maga a vonzástörvény**. Ez a két import törlesztésének útja.

## 5. A bevezetés menete — négy szakasz, kapukkal

**0. szakasz — a jelölt kimondása.** A hatodik törvény a [III/1](III-frontier/III-01-candidate-laws_hu.md) jelölt törvényei közé kerül, célpróbával: **II/17**. Törvénnyé csak lefutott próba után válik, az [I/9](I-language/I-09-laws-table_hu.md) mintája szerint.

**1. szakasz — a II/17 lefuttatása.** A [PKG-17-1](II-proofs/II-17-contract-origin/PKG-17-1-rulebook_hu.md) szabálykönyve **fagyasztva és előre regisztrálva** áll; a B3-előfeltétel lefutott, a kapu tiszta. Hátra a hurok: 48 futás (6 családtag × 2 normálás × 4 induló), 200 kör. Négy ítélet-osztály, előre rögzített elágazással:

| Ítélet | Mit jelent a hatodik törvényre |
|---|---|
| **KÖZTES** | a fixpont létezik és nemtriviális → a törvény él, mehet a kiolvasás |
| **PÁR** | a kötés-szerződés rossz hordozó → ágváltás a simasági szerződésre, nem kudarc |
| **LAPOS** | a közelség nem elég kivonat a szimmetria töréséhez → új kivonat kell |
| **ÜRES** | a hurok kiüríti a hálót → a generáló szabály családja szűkítendő |

> **Ez lesz a harmadik vak jóslatunk** — és az első, ami nem belső technikai kérdésre megy, hanem a program legmélyebb nyitott kérdésére. A `JOS-03` a hurok lefuttatása **előtt** regisztrálandó, a `JOS-01`/`JOS-02` három tanulságával: rögzített holtverseny-szabály, teljesíthetőségre ellenőrzött küszöbök, tűréses győztes-halmaz.

**2. szakasz — az újraolvasás.** Minden próba megkapja a fixpont-rangját, géppel követve (lásd 6. szakasz). Ez könyvelés, nem kutatás — de a kapu addig nem nyílik a 3. szakaszra.

**3. szakasz — a törlesztés.** A fixpont-háló geometriája (II/11), a kiterjedésszáma, és a szerződés tartalma a távolság függvényében. Célpont: az `IMP-02` és az `IMP-04` törlesztése — és ez **mért célponton** dől el, a II/4 négy tizedesjegyén.

## 6. A gépezet, amit hozzá kell tenni

- **A magban** ([`shared/kernel/ledger.json`](../shared/kernel/ledger.json)) új rang: `generalo-szabaly`, a $g$ számára — hogy a racsni ezt is fogja.
- **Minden próbafájl fejlécébe** új mező: `fixpont: igen | nem | nincs-vizsgalva`. A [`check.py`](../shared/kernel/check.py) új kapuja jelenti, hány próba áll vizsgálatlanul.
- **A gráfba** ([`graph.py`](../shared/kernel/graph.py)) új audit: „melyik próba eredménye feltételes?"
- **A padra** a II/17 hurok ellenőrző számai, ahogy lefutnak.

## 7. Mikor mondjuk ki, hogy ez az út is megbukott

Előre rögzítve, hogy utólag ne lehessen értelmezni:

1. **Ha a hurok minden generáló szabályon és mindkét normáláson elomlik** (PÁR vagy LAPOS vagy ÜRES, KÖZTES sehol) — a hatodik törvény ebben az alakjában megbukott. Rögzített bukás, a II/12 mintájára.
2. **Ha a fixpont létezik, de erősen $g$-függő** — akkor a kézi beállítást csak áthelyeztük. A törvény megmarad, de az `IMP` szám nem csökken, és ezt ki kell mondani.
3. **Ha a fixpont-hálónak nincs kiolvasható geometriája** (a II/11 gépezete nem ad értelmes távolságot) — a 3. szakasz elesik, az `IMP-02`/`IMP-04` marad, és a törvény hozadéka a kiválasztási kérdésre szűkül.

**Egyik ág sem kudarc**, ha pontosan kimondjuk. De egyik sem hallgatható el.

## 8. Amit ez a terv nem állít

- Nem állítja, hogy a fixpont létezik. Ez a II/17 kérdése.
- Nem állítja, hogy a fixpont háromkiterjedésű. Ez 12 objektumon **nem is mondható ki** — a PKG-17-1 maga zárja ki.
- Nem állítja, hogy az 1/r ki fog jönni. Ez a 3. szakasz tétje, és elbukhat.
- **Nem módosítja a 3. törvényt.** A közvetítő közeg útját ez a terv szándékosan nem választja — a levezetés ott is működne, de a nyelv szerkezetének árán.
