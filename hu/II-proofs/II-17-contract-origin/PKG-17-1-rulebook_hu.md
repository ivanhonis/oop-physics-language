---
id: PKG-17-1
type: package
part_of: II-17
lang: hu
pair: PKG-17-1-rulebook_en.md
pair_status: missing
doc_version: "1.4"
status: jovahagyva
builds_on: [II-12, II-11, II-05, II-01, I-06, I-04]
imports: "a generáló szabály (kimondott konvenció, 9. szakasz)"
---

# PKG-17-1 — A szerződés eredete: a lapos állapot stabilitása (levezetés-csomag)

**Számolást nem tartalmaz** — a szabályokat rögzíti minden számolás előtt; utólag nem módosítható.

## 1. Kérdés (egy mondat, előre rögzítve)

Ha a szerződés tartalmát nem kívülről adjuk meg, hanem a példányok kész állapota generálja — visszatér-e a rendszer a tökéletesen lapos szerződéshálóhoz, elomlik-e a párokba, vagy marad a kettő között valami?

**Amit ez a csomag nem kérdez:** hány kiterjedésű a kijövő háló, mekkora a koordinációszám, és mi a vonzás alakja. Ezek későbbi csomagok tárgyai; itt szándékosan egyetlen eldöntendő kérdés áll.

## 2. Bemenetek

A [II/11](../II-11-locality-readout/proof_hu.md) teljes gépezete és **kiszámolt kontrollja**: a páronkénti közelség-mérőszám a kész állapotból, az elfajult nulla-költségű altér egzakt vetítője, a vak visszarakó és a golyó-olvasat. A [II/1](../II-01-pair-bond/proof_hu.md) kötés-szerződése zárt alakban; a [II/5](../II-05-triangle/proof_hu.md) frusztráció-maradéka; a [II/12](../II-12-network-race/proof_hu.md) összeomlási tétele és a kötés-oldal kézzel eldőlt páros-fedése; a [kizárólagos birtoklás](../../I-language/I-07-measurement_hu.md) és az [5. törvény](../../I-language/I-06-identity_hu.md).

A II/15–II/16 három helyesbítés-tanulsága szabályként öröklődik, ahol értelmezhető: az elsődleges számolási út hosszú-lebegős (H3); az elemek egyedisége gépi állítással igazolt (H1).

## 3. A rögzített rendszer

- **Tizenkét objektum, mind a 66 pár közt szerződés** — a rendszer azonos a [II/11](../II-11-locality-readout/proof_hu.md) kontrolljával, azzal az egy különbséggel, hogy a szerződések **tartalma** nem egységes, hanem változó.
- A szerződés alakja a bevizsgált kötés-szerződés, páronkénti tartalommal: $w_{ij} \ge 0$ szorozza a [II/1](../II-01-pair-bond/proof_hu.md) zárt alakját. Tartalom nélküli (üres) pár megengedett — $w_{ij} = 0$.
- Az állapot a **teljes állapottér pontos minimuma** (B függelék, 4. eszköz; 4096 dimenzió, sűrű úton egzaktul). Elfajulás esetén a nulla-költségű altér egyenletes keveréke, **egzakt vetítővel** — a II/11 kontroll-módszere, változatlanul.
- Az elsődleges út hosszú-lebegős; az azonosság-tűrés $10^{-10}$, a hurok megállási tűrése $10^{-9}$ a tartalom-vektoron.

## 4. A hurok és a generáló szabály

A hurok egy köre, rögzítve:

1. adott tartalom-vektorból ($w$, 66 szám) a kész állapot,
2. a kész állapotból a páronkénti közelség ($I_{ij}$) — a II/11 mérőszáma, változatlanul,
3. a közelségből az új tartalom: $w_{ij} = f(I_{ij})$, majd normálás,
4. ismétlés megállásig vagy a rögzített körszámig (**200 kör**).

**A generáló szabály családja** (mind a hat tag kötelezően lefut):

| Tag | $f$ | Miért van benne |
|---|---|---|
| F1 | $x$ | egyenes arány |
| F2 | $x^2$ | erősített visszacsatolás |
| F3 | $\sqrt{x}$ | tompított visszacsatolás |
| F4 | $x/(1+x)$ | telítődő |
| F5 | $\max(0,\, x - \bar{x})$ | átlag fölötti rész (küszöbös) |
| F6 | $x$, de körönként félúton lépve | lassított hurok (a körbe-ugrálás kiszűrésére) |

**Normálás — két alak, mindkettő kötelező:** (N1) a tartalmak összege 66 egység; (N2) a legnagyobb tartalom 1. A normálás az a hely, ahol a II/12 költségvetés-konvenciója visszaszivároghatna; ezért két, egymással nem rokon alakon fut, és az ítélet csak a **kettő egyezésén** áll.

**Indulás — négy induló, mindegyik minden családtaggal és mindkét normálással:**

| Induló | Leírás | Mit próbál |
|---|---|---|
| I1 | lapos + sorsolt zaj, $10^{-3}$ | stabil-e a lapos állapot |
| I2 | lapos + egyetlen pár megemelve | vonzza-e a pár-sarok |
| I3 | lapos + egy párosítás (6 diszjunkt pár) megemelve | a II/12 páros-fedése mint medence |
| I4 | lapos + a 12-es kör élei megemelve | a geometria mint medence |

Sorsolási mag mindenütt: **1166** (= 66 · 17 + 44; kimondott, rögzített szám). A zaj nagysága és a megemelés mértéke ($1{,}1\times$) rögzített.

## 5. Levezetett előzetes tények

**(T1) A lapos állapot fixpont — egy kivétellel.** Teljes hálón, egységes tartalommal a rendszer minden párja egyenrangú; a kész állapotból számolt közelség ezért minden páron azonos, tehát az új tartalom is egységes. Ez nem várakozás, hanem szimmetria-következmény — a kérdés emiatt **nem** az, hogy létezik-e lapos fixpont, hanem hogy **stabil-e**.

**A kivétel az F5** (küszöbös tag): a lapos ponton minden közelség egyenlő az átlagával, tehát az átlag fölötti rész mindenütt pontosan nulla. Az F5 a lapos indulóból **egyetlen körben az ÜRES állapotba visz** — nem fixpont, hanem azonnali szétesés. A küszöbös generálás tehát önmagában szimmetriatörő; ez az F5 érdemi tartalma a családban, és ezért marad benne.

**(T2) Az üres szerződés ára ebben a csomagban nem hat.** Kötelező szerződés mellett a párok száma rögzített (66), a folytonos generálás pedig általános helyzetben sehol nem ad pontos nullát; az üres ára így minden elrendezésre azonos állandó, a szimmetriát nem tudja megtörni. **Kimondva: az üres ára ezért nincs benne ebben a csomagban** — a helye a koordinációszám kérdése, ahol a párok aktív/üres választása maga a tét; a folytatás neve **PKG-17-4**-re foglalva. Ez a sorrend nem kényelem: ha a lapos állapot stabil, akkor nincs olyan távolság, amit az üres ára árazhatna.

**Az egy kivétel itt is az F5:** nála az üres szerződés ténylegesen megjelenik — mégpedig azonnal és mindenütt (T1). Az F5 tehát a híd az ár kérdéséhez: megmutatja, hogy ár nélkül az üres eset nem egyensúlyt hoz, hanem elviszi az egész hálót. Az F5 viselkedése minden futásban **külön jelentendő**.

**(T3) Két ismert sarok, mindkettő kiszámolt számokkal.** A lapos sarok a II/11 kontrollja: kötésár egzaktul $45/66 = 0{,}6818$, elfajulás 132, mind a 66 közelség 0,012, szórás $10^{-16}$. A pár-sarok a II/12 kötés-oldali győztese: hat diszjunkt pár, **nulla költség**. A pár-sarok tehát költségben verhetetlen — a hurok nem költséget minimalizál, de ezt a vonzást a jegyzőkönyvnek látnia kell.

**(T4) Az elfajulás a hurok érzékeny pontja.** A lapos állapot alapállapota 132-szeresen elfajult; a hurok első lépése ezért csak az egzakt vetítővel értelmes. Ha a zaj feloldja az elfajulást, az egyértelmű alapállapot használandó; ha nem oldja fel, a vetítő. A kettő közti váltás körönként jelentendő — **a váltások száma a jegyzőkönyv része**, mert egy ugráló hurok nem ugyanaz, mint egy sima.

**(T5) A hurok két ellentétes erőt tartalmaz.** A generálás önerősítő (a közelebbi pár erősebb szerződést kap, attól még közelebb kerül); a [frusztráció](../II-05-triangle/proof_hu.md) ellene hat (egy tag nem lehet két teljes kötés része). A kimenet e kettő versenye. Melyik győz, az **regisztrált kérdés, nem jóslat**.

## 6. Előre regisztrált tények és kérdések

**Tételből:** a lapos induló zaj nélkül minden családtaggal és mindkét normálással pontosan helyben marad (T1) — ez a hurok **kötelező nulla-próbája**, futás előtt. A II/11 kontroll-számainak visszaadása (0,6818; 132; szórás $10^{-16}$) és a 12-es kör számainak visszaadása (kötésár 0,3011; közelségek 0,444 / 0,123 / 0,066 / 0,045 / 0,037) **B3-előfeltétel**: amíg nem egyeznek, a hurok nem indul.

**Jóslat tudatosan nincs.** Regisztrált kérdések:

- **(K-a, a próba fő kérdése)** stabil-e a lapos fixpont, és ha nem, melyik irányba fut el;
- **(K-b)** függ-e a végállapot az indulótól (I1–I4) — egy medence van vagy több;
- **(K-c)** egyezik-e a hat családtag és a két normálás ítélete;
- **(K-d)** a köztes esetben mennyire tagolt a tartalom-vektor (hány elkülönülő szint), és ugrik-e a közelség-lista;
- **(K-e)** a pár-sarok elérésekor: pontos párosítás-e, vagy csak részleges.

## 7. Ítélet-szabály (rögzítve)

A végállapot **négy osztály valamelyikébe** sorolandó, minden induló–családtag–normálás hármasra külön:

- **ÜRES** — minden tartalom pontosan nulla; a háló megszűnt. A normálás ilyenkor nem elvégzendő, hanem az osztály maga az eredmény. (Elsőbbséget élvez: ha ez teljesül, nincs más besorolás.)
- **LAPOS** — a tartalmak szórása a hurok végén a kiindulási zaj alatt marad (a lapos fixpont vonzó);
- **PÁR** — a tartalom-vektor párosításba fut: legfeljebb 6 pár hordozza a tartalom legalább 95%-át;
- **KÖZTES** — a fenti három egyike sem, és a hurok megállt a rögzített tűrésen belül.

**A csomag ítélete:**

- **Áll a lemma**, ha a KÖZTES osztály **mind a hat családtagon és mindkét normáláson** megjelenik, legalább az I1 indulóból. (Az I2–I4 medence-kérdés, nem az ítélet feltétele.)
- **Megbukott a lemma**, ha az I1-ből minden családtagon LAPOS, PÁR vagy ÜRES jön ki. A bukás típusát meg kell nevezni.
- **Részleges**, ha a családtagok szétválnak — ilyenkor **az eredmény a generáló szabály alakjára érzékeny**, és ezt kell ítéletként kiírni, nem a kedvező tagot választani.
- **Nem áll össze ítélet**, ha a hurok 200 körön belül nem áll meg; ilyenkor a körbe-ugrálás ténye az eredmény, a periódus hosszával.

Utólagos családbővítés, új induló, új normálás és a tűrések utólagos hangolása kizárva.

## 8. A kiolvasási jegyzőkönyv

**Kapu:** a kiolvasás **kizárólag KÖZTES ítélet esetén fut le.** LAPOS és PÁR esetén nincs mit kiolvasni, és a kiolvasás futtatása utólagos keresésnek minősül.

KÖZTES esetén, a II/11 rendje szerint: a vak visszarakó a végállapot közelség-térképéről, a szomszédszámot nem kapja meg — a lista ugrása jelöli ki; teljesség-számla a talált kontra a tartalommal bíró párokra, fantom és hiányzó külön; golyó-olvasat **legfeljebb $r = 2$-ig**, és **kimondva: ez a méret kiterjedésszám kimondására nem elég** — csak arra felel, hogy van-e egyáltalán kitüntetett szomszédság. A kiterjedés-kérdés nagyobb rendszerre halasztva.

Rezonancia-őrszem a II/13 tanulsága szerint; átellenes osztályok külön jelentve.

## 9. Import-számla és a család-követelmény

**Új, kimondott konvenció — a generáló szabály:** a szerződés tartalma a példányok kész állapotából, a II/11 közelség-mérőszámán keresztül számolódik. Ez a csomag egyetlen importja.

**A család-követelmény ennek az importnak az ára:** az [egyformasági tétel](../II-06-universality/proof_hu.md) mintájára az eredmény csak akkor áll, ha a hat családtag és a két normálás **ugyanazt az ítélet-osztályt** adja. Ha nem, az import nem szűkült, csak egy szinttel beljebb költözött — és ezt így kell megírni.

**Amit ez a csomag nem importál:** hálót (nincs, minden pár szerepel), költségvetést (nincs elosztandó mennyiség), mezőnyt (nincs jelölt-lista), koordinációszámot (nincs kimondva). **Ez az első csomag a nyomvonalon, amelynek a bemenetei közt háló nem szerepel.**

## 10. Ítélet erről a csomagról

**Áll.** Érdemi előzetes eredményei: a lapos fixpont tétele (T1) — amely a kérdést létezésről stabilitásra fordítja; az üres ár hatástalanságának levezetése ezen a rendszeren (T2), amely a csomagsorrendet is megszabja; és az elfajulás-kezelés kimondása a hurok érzékeny pontjaként (T4).

**A B3-előfeltétel fagyasztás előtt lefutott** (`PKG-17-2-verify.py`), és minden hivatkozási szám visszajött: a kötésár egzaktul 45/66, az elfajulás 132, a közelség-szórás 1,5·10⁻¹⁶, a kör kötésára 0,30105 és közelségei 0,4438 / 0,1231 / 0,0656 / 0,0448 / 0,0366; ráadásul a II/1 zárt alakja és a II/5 három száma (3/2, négyszeres elfajulás, 15/8) is. A hitelesítés **egy leletet hozott**, amely a szabálykönyv szövegét módosította fagyasztás előtt: az F5 lapos viselkedése, amiből az ÜRES osztály és a T1 kivétele lett.

## 11. Kimenő állítások (a PKG-17-2 csak ezekre építhet)

- **A1:** rendszer = 12 objektum, mind a 66 pár, változó tartalmú kötés-szerződés; állapot a teljes állapottér egzakt minimuma, elfajulás egzakt vetítővel (3. szakasz).
- **A2:** a hurok a 4. szakasz szerint: hat generáló családtag, két normálás, négy induló, 200 kör, mag 1166.
- **A3:** B3-előfeltétel a II/11 kontroll- és kör-számainak visszaadása; a nulla-próba (zaj nélküli lapos induló helyben marad) kötelező.
- **A4:** előre regisztrált tények és kérdések a 6. szakasz szerint; jóslat nincs.
- **A5:** ítélet-szabály a 7. szakasz szerint, **négy osztállyal** (ÜRES, LAPOS, PÁR, KÖZTES) és a részleges eset kötelező kiírásával; az F5 viselkedése minden futásban külön jelentendő.
- **A6:** kiolvasási jegyzőkönyv a 8. szakasz szerint, kapuval; kiterjedés-ítélet ezen a méreten nem adható.
- **A7:** kötelező önellenőrzések — a kötés-szerződés zárt alakja két úton (sűrű sajátfeladat és a II/1 képlete), a vetítő nyoma a lapos ponton egzaktul 132, a tartalom-vektor normájának körönkénti jelentése, az elfajulás-váltások számlálása.
- **A8:** bukás-ág megnevezve: **PÁR** ítélet esetén a következő csomag ugyanezt a hurkot a **simasági szerződéssel** ismétli helyeken, mert akkor a kötés-szerződés bizonyult alkalmatlan hordozónak; **LAPOS** ítélet esetén a hurok ebben az alakjában megbukott, és a generálásnak nem a közelségre, hanem más állapot-kivonatra kell épülnie.
