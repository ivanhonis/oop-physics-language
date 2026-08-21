---
id: PKG-15-12
type: package
lang: hu
pair: PKG-15-12-convention-scope_en.md
pair_status: missing
doc_version: "1.4"
status: jovahagyva
part_of: II-15
builds_on: [PKG-15-10, PKG-15-11, PKG-15-9, II-12]
imports: nulla
---

# PKG-15-12 — A konvenciók hatóköre (érzékenységi csomag)

**Egy mondatban.** A teli-vég és a lyuk-létra tétel **sehol nem használja a szövés-szerkezetet** — elég a fokszám-regularitás —, a versenyszabály viszont **teherhordó**: ő a nyom-döntetlen előfeltétele.

## 1. Kérdés

A magban két kimondott konvenció áll megméretlenül: a **`KON-01` versenyszabály** (rögzített, azonos költségvetés) és a **`KON-03` szövés-építés** (minden induló egy csoportszerkezet ismétlése). Mennyit hordoz a kettő? Az út ugyanaz, ami a `KON-02`-nél működött: cseréld ki az egyetlen dolgot, és nézd meg, mi mozdul.

## 2. `KON-03` — a szövés-építés

**A levezetések olvasata.** Sem a [teli-vég](PKG-15-10-dense-end_hu.md), sem a [lyuk-létra](PKG-15-11-hole-ladder_hu.md) tétel nem említ szövést. Csak ezeket használják:

| Amire épül | Miért nem kell hozzá szövés |
|---|---|
| nyom-döntetlen: $\sum \lambda = dn$ | **minden** $d$-reguláris gráf Laplace-nyoma |
| plafon: $\lambda \le 2d$, egyenlőség ⟺ páros | általános spektrális tény |
| lyuk-létra: $2d - \lambda$, rendezve | definíció |

Ha ez az olvasat áll, a tételek **minden reguláris gráfon** állnak, és a szövés-konvenció **nekik** semmit nem hordoz.

**A próba.** Futtassuk a tételeket olyan hálókon, amelyeket semmi más nem ad meg, csak az élsoruk — köztük olyanokon, amelyek **bizonyítottan a szövés-családon kívül vannak**. A **Petersen-gráf** 3-reguláris és csúcstranzitív, de **nem Cayley-gráf**: egyetlen csoportszerkezet sem fektetheti ugyanazt a bekötést minden helyére. A **Desargues-gráf** (a Petersen páros duplafedése) ugyanilyen, csak páros.

| Háló | Szövés? | $d$ | $n$ | Nyom-eltérés | Csúcs / plafon | Páros | Plafon-tétel | Azonosság |
|---|---|---|---|---|---|---|---|---|
| **Petersen** | **nem** | 3 | 10 | $3{,}6\cdot10^{-15}$ | 5,000 / 6 | nem | **áll** | $3{,}6\cdot10^{-15}$ |
| **Desargues** | **nem** | 3 | 20 | $0$ | 6,000 / 6 | igen | **áll** | $1{,}8\cdot10^{-15}$ |
| kör-létra C10×K2 | igen | 3 | 20 | $0$ | 6,000 / 6 | igen | áll | $1{,}5\cdot10^{-14}$ |
| körlánc C20(1,10) | igen | 3 | 20 | $2{,}1\cdot10^{-14}$ | 5,902 / 6 | nem | áll | $1{,}4\cdot10^{-14}$ |
| körlánc C20(1,3,5) | igen | 6 | 20 | $2{,}8\cdot10^{-14}$ | 12,000 / 12 | igen | áll | $4{,}3\cdot10^{-14}$ |
| körlánc C20(1,2,3) | igen | 6 | 20 | $1{,}4\cdot10^{-14}$ | 8,618 / 12 | nem | áll | $1{,}5\cdot10^{-14}$ |

**Mind áll, kivétel nélkül** — a nem-Cayley hálókon is. És a teli-végi kritérium ([K-PKG1511-4](PKG-15-11-hole-ladder_hu.md)) azonos költségvetésű mezőnyön ($n=20$, $d=3$, a Desargues-szal együtt) **mind a 19 töltésen** ugyanazt a győztes-halmazt adja, mint a verseny.

> **Ítélet a `KON-03`-ra: a tételekre nézve nulla a hatása.** A tételek hatóköre ezzel **kitágul**: nem a szövés-családról szólnak, hanem minden fokszám-reguláris hálóról.

**Amit viszont a `KON-03` továbbra is hordoz, kimondva:** a **mezőnyt**. Hogy a versenyen kik indulnak, azt a szövés-építés szűkíti — és ez a szűkítés **megméretlen**, mert nem-szövés indulók egyik lefutott versenyen sem indultak. A tételek szabadok tőle; a *versenyek eredménye* nem bizonyítottan az.

## 3. `KON-01` — a versenyszabály

A rögzített, azonos költségvetés az, ami miatt **minden induló nyomösszege azonos** — és a nyom-döntetlen az, ami a teli véget kivonássá alakítja. A konvenció tehát nem díszítés, hanem a teljes apparátus előfeltétele.

**Mérve.** Két indulót eresztve össze **különböző** költségvetéssel ($d=6$ és $d=3$, azonos $n=20$):

- a nyomösszegük **120** és **60** — a nyom-döntetlen nem áll;
- a teli töltésen az árkülönbség **60**, pontosan a nyomkülönbség;
- a teli-végi kritérium **2/19 töltésen téved**, míg azonos költségvetésen **0/19**-en.

> **Ítélet a `KON-01`-re: teherhordó, de elvi.** Nélküle a nyom-döntetlen és vele az egész teli-vég apparátus összeomlik. De nem önkényes: éppen az teszi értelmessé az összehasonlítást, hogy azonos költségvetést helyezünk el. A mért érték: **a konvenció megváltoztatása nem elmozdítja az eredményt, hanem megszünteti az összehasonlíthatóságot.**

*Őszinte jegyzet a mérés erejéről:* a 2/19 azért ilyen alacsony, mert a két költségvetés annyira eltér, hogy a drágább induló amúgy is veszít szinte mindenütt. Az érdemi állítás nem ez a szám, hanem a szerkezeti: eltérő $T$ mellett a „hasonlítsd össze a lyuk-létrákat" **bizonyíthatóan nem ekvivalens** a „hasonlítsd össze az árakat"-tal.

## 4. Egy módszertani lelet — harmadszor ugyanaz

A csomag első futása **négy eltérést** jelentett a teli-végi kritériumon. Egyik sem volt valódi: mindegyik **holtverseny volt, amit a lebegőpontos zaj tört el**, mert a próba tűrés nélküli `argmin`-t hasonlított össze. Mindkét végén tömeges a holtverseny: minden összefüggő hálónak van nulla üteme, és minden tükör-jegyűnek ugyanaz a csúcsa.

Ez a **harmadik** eset, amikor a holtverseny-kezelés hibázott (`JOS-01`: nem volt rögzítve; `JOS-02`: teljesíthetetlen küszöb; itt: tűrés nélküli összevetés). A tanulság mostantól szabály: **győztes-halmazt kell összevetni tűréssel, sosem `argmin`-t.**

## 5. Import-számla

Új import: **nulla.** A gráfok élsorból épülnek; a Laplace-spektrum standard; a tételek a PKG-15-10/11-ből.

## 6. Ítélet erről a csomagról

**Áll.** Mindkét konvenció megmérve, és a tételek hatóköre kitágult.

## 7. Kimenő állítások

- **K1:** A [teli-vég](PKG-15-10-dense-end_hu.md) és a [lyuk-létra](PKG-15-11-hole-ladder_hu.md) tétel **minden $d$-reguláris hálón áll**, nem csak szövéseken. Igazolva nem-Cayley csúcstranzitív hálókon (Petersen, Desargues) is. A tételekben $T = dn$ és a plafon $2d$; a szövéseknél $d = 2k$, ezért $T = 2kn$ és plafon $4k$.
- **K2:** **`KON-03` érzékenysége a tételekre: nulla.** A konvenció a *mezőnyt* szűkíti, nem a tételeket — és a mezőny-hatás **megméretlen marad**, mert nem-szövés induló egyik versenyen sem indult.
- **K3:** **`KON-01` érzékenysége: teherhordó, de elvi.** A nyom-döntetlen előfeltétele; eltérő költségvetéssel a teli-végi ekvivalencia elvész (mérve: 2/19 kontra 0/19). A konvenció megváltoztatása nem az eredményt mozdítja, hanem az összehasonlíthatóságot szünteti meg.
- **K4:** **Módszertani szabály:** győztes-halmazt kell összevetni tűréssel, sosem tűrés nélküli `argmin`-t. Ez a harmadik holtverseny-hiba a sorban.

> A K1–K4 csak e csomag **jóváhagyása után** vezethető át a fejezetekbe.
