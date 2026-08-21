---
id: PKG-18-1
type: package
part_of: II-18
lang: hu
pair: PKG-18-1-rulebook_en.md
pair_status: missing
doc_version: "1.4"
status: jovahagyva
builds_on: [I-02, I-05, I-08, II-06, II-08, II-11, II-12]
imports: nulla
---

# PKG-18-1 — A közvetítő közeg szabálykönyve (levezetés-csomag)

**Számolást nem tartalmaz** — a szabályokat rögzíti minden számolás előtt, hogy utólagos szabálymódosítás ne legyen lehetséges.

---

## 1. Kérdés (egy mondat, előre rögzítve)

Ha a szerződés tartalmát nem kézzel deklaráljuk, hanem egyetlen, helyeken élő közeg állítja elő a súlysűrűségből — **mi marad a bevizsgált szerződéstárból, és mi mond ellent?**

**Amit ez a csomag nem kérdez.** Honnan jön a háló (ez a II/19 tárgya, lásd 12. szakasz); hány kiterjedésű a rendszer; és **nem kérdez semmit egyetlen mért célpontról sem**. A 3. szakasz szándékosan úgy van megírva, hogy elolvasható legyen anélkül, hogy az olvasó bármely fizikai jelenséget ismerné. A mért célpontok a 8. szakaszban lépnek be, következményként — nem indokként.

## 2. Bemenetek

- **[I/2](../../I-language/I-02-object-state_hu.md):** az állapot súlyozás helyeken; a súlyok rögzített összhossza; és **az egységnyi nagyságú közös szorzó nem adat** (ez az 5. szakaszban lesz teherhordó).
- **[I/5](../../I-language/I-05-contract_hu.md), 4. törvény:** a szerződés bíró és motor — a szerződés határozza meg az állapotot. E csomag nem ezt módosítja, hanem a szerződés *eredetét* szabályozza.
- **[I/8](../../I-language/I-08-contract-store_hu.md):** a bevizsgált szerződés-alakok táblája — **ez a csomag audit-tárgya**.
- **[II/6](../II-06-universality/proof_hu.md):** az egyformasági tétel — minden helyi keverés alja ugyanaz a létra. **Ez az egyetlen primitív szerződés kimondásának engedélye** (lásd 3. szakasz, D3).
- **[II/11](../II-11-locality-readout/proof_hu.md):** a szomszédság a kész állapot nézete; a kiterjedésszám mérhető; és a kontroll (teljes gráf, tökéletesen lapos közelség-térkép).
- **[II/12](../II-12-network-race/proof_hu.md):** a nyom-döntetlen és az összeomlási tétel; a gyökér-jelzés, amely e csomagot kiváltotta.
- **[II/8](../II-08-exclusion-vs-repulsion/proof_hu.md):** a taszítási szerződés és a mért csúcsszerkezet — a 9. szakasz döntő próbája.
- **[III/1, 2. jelölt](../../III-frontier/III-01-candidate-laws_hu.md):** a kötés-szerződés levezethetősége. E csomag alatt ez nem opció, hanem **feltétel** (lásd 4. szakasz).

**Helyesbítés a bemenetek közt, kimondva.** A [hu/EXTENSION_hu.md](../../EXTENSION_hu.md) 2. és 8. szakasza a közeg útját **szándékosan elutasította**, azzal az indokkal, hogy „a közeg amplitúdója a forrással nő, tehát nem lehet rögzített összhosszú, és a fejlődése nem súlytartó" — vagyis a 3. törvénybe ütközik. **Ez az indok statikus közegre nem áll:** a statikus közegnek nincs fejlődése, a 3. törvény pedig fejlődés-műveletekről szól. Az EXTENSION elutasítása tehát nem véleményváltozás miatt esik el, hanem mert az indoka egy nem-statikus közegre vonatkozott. Az EXTENSION átírása e csomag **jóváhagyása utáni** dolog.

## 3. A rögzített definíció — hat kényszer

A közeg egy helyenkénti valós mennyiség, $\varphi_i$. Ha $L$ a szomszédságból épített simasági szerződés mátrixa és $\rho$ a súlysűrűség:

$$E[\varphi] \;=\; \tfrac12\,\varphi^{\mathsf T} L\, \varphi \;-\; \rho^{\mathsf T}\varphi \tag{K-PKG181-1}$$

| | Döntés | Az indok — **kizárólag nyelvi** | Kényszer vagy választás |
|---|---|---|---|
| **D1** | helyenkénti mennyiség | a nyelv minden állapota helyeken él ([I/2](../../I-language/I-02-object-state_hu.md)) | kényszer |
| **D2** | **nem normált** | ha normált volna, példány-állapot lenne, nem szerződés-forrás | kényszer |
| **D3** | törvénye a **meglévő simasági szerződés** | az [I/1](../../I-language/I-01-concept_hu.md) módszertani szabálya: nem adunk új törvényt, ha meglévő elem elég — és a [II/6](../II-06-universality/proof_hu.md) szerint a pontos alak nem is számít | kényszer |
| **D4** | **lineáris** csatolás a súlysűrűséghez | a nulladrend nem csatol; minden magasabb rend dimenziós együtthatót kíván, az pedig szabad paraméter | **kényszer** |
| **D5** | **nincs tömeg-tag** | a $m^2\varphi^2$ tag szabad szám volna. Kimondva: **ez a tag az, ami véges hatótávot szabna — a hosszú hatótáv nem beletett tulajdonság, hanem az, ami marad, amikor a szabad paramétert megtagadjuk** | kényszer |
| **D6** | **statikus** | egy nem normált hordozó *fejlődési* törvényére a nyelvnek nincs alapja | kényszer |

**Következmény D6-ból, rögzítve — a közeg nem új kategória.** Statikus közegnél a (K-PKG181-1) minimuma zárt alakban áll:

$$\varphi \;=\; L^{+}\rho, \qquad E_{\min} \;=\; -\tfrac12\,\rho^{\mathsf T} L^{+} \rho \tag{K-PKG181-2}$$

vagyis a közegnek **nulla szabad szabadsági foka van**: teljesen meghatározza a sűrűség. Ami kiintegrálható, az nem ötödik ontológiai kategória, hanem **szerződés-generáló szerkezet**. A nyelv kategóriái nem bővülnek.

**Következmény D6-ból, rögzítve — a 3. törvény érintetlen.** A statikus közegnek nincs fejlődése, tehát nem tárgya fejlődés-műveletnek. **A 3. törvény hatóköre NEM szűkül.** Ez nem kényelem, hanem költség-elkerülés: a 3. törvény linearitása az [I/7](../../I-language/I-07-measurement_hu.md) clone()-tételét hordozza, és egy szűkített 3. törvény a No-Cloningot is meggyengítené.

**A soktest-alak kötelező, a középtér-alak tiltott.** A (K-PKG181-2) forrása a **teljes** sűrűség-operátor, és kiintegrálva **kéttest-operátort** ad a soktest-téren:

$$\hat H_{\text{kozeg}} \;=\; -\tfrac12 \sum_{i,j} \hat n_i \,(L^{+})_{ij}\, \hat n_j \tag{K-PKG181-3}$$

Ez a soktest-téren **lineáris**, tehát a 3. törvénnyel összefér. A tiltott alak az, amelyben a közeget egyetlen példány saját középterének vesszük ($\varphi = L^{+}|\psi|^2$ visszahat $\psi$-re): az nemlineáris fejlődést ad, sérti a 3. törvényt, és jelzésre volna használható. **A két alak numerikusan is eltér; e csomag a (K-PKG181-3)-at rögzíti, és a középtér-alakot kizárja.**

## 4. Amit ez elvesz — a közeg a szerződéstár helyére lép

A csomag **elsőbbségi olvasatot** rögzít: a közeg a helyeken él, és **minden objektumok közti szerződés a közeg indukált tagja.** Kézzel deklarált szerződés nincs.

Ezzel a nyelv primitívjei ennyire csökkennek: **helyek**, **szomszédság** (`IMP-01`, egyelőre bemenet), **a simasági szerződés**, és az öt törvény. Minden más levezetendő.

**Ez a szűkítés a csomag lényege.** Az általános szabály ismérve, hogy *elvesz* a kimondási szabadságból: a közeg után **távolságfüggő szerződés kézzel nem deklarálható**, hatótáv nem választható, és azonos objektumok közti taszítás nem vehető fel.

### A szerződéstár-audit, előre rögzítve

| Szerződés | Mi lesz belőle | Előre rögzített várt besorolás |
|---|---|---|
| **Simasági** | ez maga a közeg törvénye | **primitív** |
| **Vonzó** (távolság-fordított) | a közeg indukált tagja, $(L^{+})_{ij}$ | `levezetve` |
| **Tál** | a vonzó alja (ma is „levezetett alak") | `levezetve` |
| **Fal** | nem objektumok közti szerződés: rögzített forrás-elrendezés | `forras` |
| **Érték-elfogultsági** | *érték*-térben hat, nem helyen — a közeg nem látja | **nyitott (K-c)** |
| **Kötés** ([II/1](../II-01-pair-bond/proof_hu.md)) | nem indukált alak; a [III/1, 2. jelölt](../../III-frontier/III-01-candidate-laws_hu.md) útján kell előállnia | **feltétel (K-a)** |
| **Taszítási** | azonos forrásokra vonzás | **ellentmond (9. szakasz)** |

**A tábla a számolás előtt áll, és utólag nem bővíthető.** Ha egy sor a várttól eltérő besorolást kap, az eredmény, nem hiba.

## 5. A definíció kimondott fele — az él-alak

**Ez a szakasz azért van, hogy a csomag ne látsszon teljesnek.**

A primitív szerződés két részre bomlik:

$$\sum_{(i,j)\in E}\bigl|\psi_i-\psi_j\bigr|^2 \;=\; \underbrace{\sum_i d_i\,|\psi_i|^2}_{\text{hely-rész}} \;-\; \underbrace{2\sum_{(i,j)}\mathrm{Re}\bigl(\psi_i^{*}\psi_j\bigr)}_{\text{él-rész}} \tag{K-PKG181-4}$$

A D4 szerinti csatolás a súlysűrűséghez **kizárólag a hely-részt látja**. De a hely-rész önmagában nem simasági szerződés — csak helyi tag; az, amitől sok hely *egyetlen objektum* lesz, az él-részben van.

> **Kimondva: e csomag a közeg definíciójának a felét rögzíti.** A másik fél — egy éleken élő közeg, amely az él-részhez csatolódik — külön próba, előre lefoglalt névvel: **`PKG-18-4`**. A nyelv erre magától ad szerkezetet: az él-mennyiség csak **helyenkénti fázis-átdefiniálás erejéig** értelmes, mert az [I/2](../../I-language/I-02-object-state_hu.md) kimondja, hogy az egységnyi nagyságú közös szorzó nem adat.

**Mentő-tilalom (a bejelentés célja).** Ha a hely-alak bármely következménye (6. szakasz) megbukik, az **rögzített bukás**, és **nem menthető az él-alakra hivatkozva**. Az él-alak saját szabálykönyvvel futó, önálló próba; ami itt bukik, az itt bukott. Ez a kikötés azért áll a fagyasztott szövegben, hogy utólag ne lehessen mentőövvé alakítani.

## 6. Levezetett előzetes tények (nem jóslatok)

Mind a négy a (K-PKG181-2)-ből következik, számolás nélkül. **Mind cáfolható.**

| | Következmény | Levezetés |
|---|---|---|
| **C1** | Az indukált szerződés alakja **$r^{2-d}$ minden $d$-re**. | $L^{+}$ a rács Green-függvénye; kis hullámszámon $\lambda \approx k^2$. **A nyelv a hármat semmivel nem tünteti ki**; hogy ott ez $1/r$, az egy érték, nem megkülönböztetés. |
| **C2** | **Azonos forrásokra vonzás** — és mivel a súlysűrűség szerkezetéből adódóan sosem negatív, a nyelvben **nincs ellentétes forrás**: a közeg kizárólag vonzást tud. | $L^{+}$ pozitív szemidefinit; a kereszttag $-\rho_1^{\mathsf T}L^{+}\rho_2$. |
| **C3** | **Minden példánypár azonos erősséggel** vonz, típustól függetlenül. | $\sum_i \rho_i = 1$ minden példányra ([I/2](../../I-language/I-02-object-state_hu.md)), és nincs tömeg-tag (D5). |
| **C4** | **Egyenletes sűrűségen a közeg pontosan nulla.** | Állandó $\rho$ az $L$ nulla-módusa, és $L^{+}$ kiejti. |

**Két azonnali következmény a régi próbákra**, szintén levezetve:

- **egyetlen példány ⇒ a közeg tagja állandó.** A (K-PKG181-3)-ban $\hat n_i \hat n_j$ egy példánynál csak $i=j$-re nem nulla, és $(L^{+})_{ii}$ homogén rácson helyfüggetlen. Tehát a [II/3](../II-03-box/proof_hu.md) és a [II/6](../II-06-universality/proof_hu.md) létráját a közeg **nem mozdítja**.
- **egyenrangú hálón egyenletes betöltés ⇒ a közeg egzaktul nulla** (C4). Tehát a **teljes II/12–II/17** — és vele a négy új tétel — **érintetlen**.

## 7. Az erősség: nincs gomb

A (K-PKG181-1) csatolása egységnyi, a közeg merevsége a simasági szerződés saját egységnyi ereje. **Új szám nincs.**

Ez nem kényelmi választás. Egy nyelv, amely nincs egyetlen problémára szabva, **nem tarthat gombot, amellyel túléli a problémát**: ha a csatolást azért állítanánk kicsire, hogy a [II/8](../II-08-exclusion-vs-repulsion/proof_hu.md) mért csúcsai megmaradjanak, az pontosan a rászabás volna.

**Kimondva, előre:** a $\varphi \to g\varphi$ átskálázás nem tünteti el $g^2$-et — az a közeg indukált tagjának és a simasági tagnak az **arányát** rögzíti. E csomag $g = 1$-et ír elő. **Ha a mérés bármikor $g \ne 1$-et kíván, $g$ ötödik importtá válik, és a mag import-plafonja 4-ről 5-re nő.** Ez a lehetőség itt van kimondva, hogy utólag ne lehessen csendben megtenni.

## 8. Előre regisztrált tények és kérdések

**Tételből következő tények** (nem jóslatok): a C4 és a két azonnali következmény a 6. szakaszból; továbbá a **nyom-döntetlen érintetlen**, mert a közeg kéttest-tag, az ütem-létra pedig egytest-objektum.

**Jóslat tudatosan nincs.** Négy regisztrált kérdés:

- **(K-a, a csomag fő kérdése)** Levezethető-e a kötés-szerződés a közeg + kizárás + simasági szerződés együtteséből ([III/1, 2. jelölt](../../III-frontier/III-01-candidate-laws_hu.md) útján)? **Ezen áll vagy bukik hat próba** (II/1, II/2, II/5, II/9, II/10, II/11).
- **(K-b)** Mit ad a közeg a [II/4](../II-04-hydrogen-atom/proof_hu.md)-en, ha a középpont forrás-példány: a deklarált vonzó szerződés az-e, amit a közeg adna?
- **(K-c)** Mi lesz az érték-elfogultsági szerződésből, amely nem helyen, hanem értékben hat?
- **(K-d)** Mi lesz a falból mint rögzített forrás-elrendezésből?

## 9. Ítélet-szabály (rögzítve)

A döntő próba **már mért számon áll**: a [II/8](../II-08-exclusion-vs-repulsion/proof_hu.md) csúcsszerkezete (fő 2, 6, 12; mellék 4, 9). A C2 szerint a közeg két elektron közt **vonzást** ad, a mért szerkezet **taszítást** kíván.

| Ítélet | Feltétel |
|---|---|
| **ÁLL** | a szerződéstár-audit minden sora `levezetve`, `forras` vagy `nem-erinti`, **és** az érintett próbák mért célpontjai a közzétett tűrésükön belül visszajönnek |
| **RÉSZLEGES** | egyes sorok levezetődnek, mások ellentmondanak; az ellentmondók néven nevezve, és a közeg **kiegészítő** szerződés-forrásként könyvelve — vagyis az elsőbbségi olvasat elesik, a közeg egy elem a több közül |
| **MEGBUKOTT** | az előjel-ellentmondás $g = 1$-en mennyiségi és megkerülhetetlen ⇒ a közeg ebben az alakban megbukott, **rögzített bukásként**, a [II/12](../II-12-network-race/proof_hu.md) mintájára |

**Utólag tilos:** szabad erősség bevezetése; az él-alakra hivatkozó mentés (5. szakasz); a mezőny vagy a szerződéstár szűkítése; a tűrés tágítása. Bővítés csak új csomagban, e csomag módosítása nélkül.

**Kimondva, mit ér a bukás.** Ha a közeg az előjelen bukik, a bukás **általános alakú**: a nyelvben nincs előjeles forrás, ezért benne épített hely-közeg soha nem tud taszítást. Ez nem a közeg hibája, hanem a nyelv kimondott hiánya — és megnevezi a következő hiányzó fogalmat (egy előjeles, megmaradó mennyiség). Ez a II/12 mintája: a bukás megnevezi a hiányzó fogalmat.

## 10. A felülvizsgálati regiszter

Minden próbafájl fejlécébe új mező:

```
kozeg: levezetve | forras | ellentmond | nem-erinti | nincs-vizsgalva
```

és egy kapu a [`check.py`](../../../shared/kernel/check.py)-ba, amely jelenti az állást. **Számozás:** a közeg **II/18**, és a regiszter a II/1–II/17-et „közeg előtti"-nek jelöli.

**Kimondva: a lusta felülvizsgálat itt nem tartható.** Az elsőbbségi olvasat alatt minden nem-simasági szerződés azonnal tétre megy. Cserébe a felülvizsgálat **egyetlen kérdésre redukálódik** (K-a): ha a kötés-szerződés levezethető, hat próba egyszerre rendben; ha nem, hat próba egyszerre feltételes. A [`graph.py`](../../../shared/kernel/graph.py) megmondja, melyik próba mire támaszkodik.

## 11. Import-számla

**Új import: nulla** — amíg a 7. szakasz $g = 1$-e áll.

- **Örökölt, nem e csomagé:** `IMP-01` (szomszédság). **A közeg nem vezeti le a hálót, hanem használja** — ez kimondott hatókör-határ.
- **Ami törleszthető, ha a K-b áll:** az `IMP-02` **alakja**. Kimondva: a *távolság mint fogalom* eltűnik a szerződéstárból, mert a közeg csak szomszédságot használ, és a helypár-függvényt maga állítja elő. **Az elektromosságot ez nem törleszti** (C2).
- **Érintetlen:** `IMP-03`, `IMP-04`.
- **Új konvenció: nincs.** A `KON-01` és `KON-03` sorsa a II/19 dolga, nem ezé.

## 12. Hatókör-határok, kimondva

1. **A háló bemenet.** A közeg a szomszédságon él; hogy mely helyek szomszédok, azt e csomag nem dönti el. A hordozó-kérdés a **II/19** tárgya (az üres szerződés ára), amelynek két mért végpontja már áll: a [II/12](../II-12-network-race/proof_hu.md) összeomlása (ár nulla) és a [II/11](../II-11-locality-readout/proof_hu.md) lapos kontrollja (ár végtelen).
2. **A definíció fele áll** (5. szakasz).
3. **Körkörösségi kapu.** A közeg a szomszédságból épít, és nem állíthatja elő azt, amiből épül. A [`graph.py`](../../../shared/kernel/graph.py) nevesített auditot kap erre, a `P2.4(a)` mintájára: *támaszkodik-e a II/19 hordozó-levezetése a közeg indukált tagjára?* Elvárt válasz: **nem**.

## 13. Ítélet erről a csomagról

**Áll — fagyasztva.** Érdemi előzetes eredményei — mind levezetés, nem mérés:

- **a felbontási lelet** (5. szakasz): a primitív szerződésnek két része van, és a súlysűrűséghez csatolt közeg az egyiket látja — a definíció ezzel kimondottan fél;
- **az EXTENSION elutasító indokának helyesbítése** (2. szakasz): statikus közegnél a 3. törvény nem sérül;
- **a szerződéstár-audit** mint előre rögzített tábla (4. szakasz);
- **a C4 és a két azonnali következmény** (6. szakasz), amelyek a felülvizsgálatot a II/12–II/17-re nézve egy sorban lezárják.

## 14. Kimenő állítások (a PKG-18-2 csak ezekre építhet)

- **A1:** a közeg definíciója a 3. szakasz D1–D6 kényszerei szerint; a rögzített alak a (K-PKG181-1)–(K-PKG181-3); a középtér-alak kizárva.
- **A2:** a közeg **nem új kategória**, hanem szerződés-generáló szerkezet; a nyelv kategóriái nem bővülnek.
- **A3:** a **3. törvény hatóköre nem szűkül**; a statikus közeg nem tárgya fejlődés-műveletnek.
- **A4:** elsőbbségi olvasat: a primitívek a helyek, a szomszédság és a simasági szerződés; minden más szerződés levezetendő. A szerződéstár-audit táblája a 4. szakasz szerint, előre rögzítve.
- **A5:** a definíció **fele áll**; az él-alak a `PKG-18-4`-re foglalva, mentő-tilalommal.
- **A6:** a négy következmény (C1–C4) és a két azonnali következmény a 6. szakasz szerint — a `PKG-18-2` gépi megerősítésének tárgya.
- **A7:** $g = 1$, új szám nincs; $g \ne 1$ esetén ötödik import, a plafon 5-re nő.
- **A8:** ítélet-szabály a 9. szakasz szerint, három néven nevezett ággal; a döntő próba a II/8 mért csúcsszerkezete (`PKG-18-3`).
- **A9:** a `kozeg:` regiszter-mező és a `check.py` kapuja a 10. szakasz szerint; a lusta felülvizsgálat nem áll.
- **A10:** hatókör-határok a 12. szakasz szerint; a hordozó-kérdés a II/19-é, és a körkörösségi audit kötelező.

> Az A1–A10 csak e csomag **jóváhagyása után** vezethető át a fejezetekbe. Addig az [I/8](../../I-language/I-08-contract-store_hu.md), a [III/1](../../III-frontier/III-01-candidate-laws_hu.md), a [III/2](../../III-frontier/III-02-open-questions_hu.md) és az [EXTENSION](../../EXTENSION_hu.md) szövege változatlan.
