---
id: PROGRAM
type: rulebook
lang: hu
pair: PROGRAM_en.md
pair_status: missing
doc_version: "1.4"
status: jelolt
---

# A kutatási program — a leírónyelvtől a zárt, prediktív modellező nyelvig

**Egy mondatban.** Ez a dokumentum azt az utat rögzíti, amelyen a nyelv a visszaszámoló hasonlóság-gyűjtemény vádja alól számmal mentesül: zárt könyvelésű, formálisan tisztázott státuszú, előre jósló, folyamatokat is modellező és 10⁵ objektumig skálázó elmélet-nyelvvé válik — vagy pontosan rögzített bukásokkal kimondja, meddig ér. A programot AI-agentek hajtják végre; ezért minden mérföldkőnek gépileg eldönthető siker- és bukás-kritériuma van — ahol pedig ez elvileg lehetetlen (irodalom-audit, keresési ítélet), ott rögzített protokollú, naplózott, harmadik fél által megismételhető ítélet áll a helyén, és ez kimondva szerepel —, és minden lépés a repó saját módszertanán — csomag-módszer, import-számla, kétutas számolás — fut.

Ez a fájl terv, nem eredmény: az igazság forrása mindig a lefutott próbák fájlja lesz. A mérföldkövek sorszáma bővítésálló; új mérföldkő mindig a szakasza végére kerül.

---

## 1. A kiindulás: mi van meg, és miért támadható

**Ami megvan.** Öt törvény és egy növekvő tétel-készlet (két típusosztály, kizárás, No-Cloning, lyuk-tükör, irány-tétel, tető-tétel, összeomlási tétel — az [I/9](I-language/I-09-laws-table_hu.md) táblája); tizenhat számolt próba, köztük egy intézményesített bukás ([II/12](II-proofs/II-12-network-race/proof_hu.md)); az import-számla (jelenleg négy import, gépi nyilvántartással és racsnival) és az import/konvenció/peremadat/hatókör szétválasztás; a csomag-módszer előre rögzített szabálykönyvvel és kapu-szabállyal; 10⁻¹²–10⁻¹⁶ szintű kétutas számolások; és egy saját születésű törvény-jelölt (a tető-törvény, [III/1, 8.](III-frontier/III-01-candidate-laws_hu.md)). Ez a fegyelem ritka vagyon — a program nem nulláról indul, hanem egy proto-formális rendszert emel gépi kikényszerítésre.

**Ami támadható.** A szkeptikus fizikus hat vádja, veszélyességi sorrendben — és az a mérföldkő, amelyik az adott vádat elhallgattatja:

| # | A vád | Ami elhallgattatja |
|---|---|---|
| 1 | **Retrodikció + átcímkézés:** mind a 16 próba ismert számot ad vissza, a szerző választotta célpontokon, a standard QM gépezetén | P1.4, P1.5 (vak célpontok), P4.4, P4.5 (valódi jóslat) — addig P1.2 (prior-art audit) tartja sakkban |
| 2 | **Formális státusz tisztázatlan:** ha a nyelv ekvivalens a rácsos QM-mel, definíció szerint nem jósolhat mást; ha nem, hol tér el? | P2.6 (ekvivalencia vagy eltérési pont) |
| 3 | **Az importok a lényeget hozzák:** az 1/r **és a kimondatlanul betett kiterjedésszám együtt** adja a hidrogén négy tizedesét, a típusdeklarációk a bűvös számokat — és a PKG-15-9 óta tudjuk, hogy a kiterjedés-verseny a hármat belülről nem adja ki | P2.1, P2.2, P2.4, P2.5 (import-nullázás vagy becsületes véglegesítés) |
| 4 | **A kiterjedés-verseny önjáték:** a győztest részben a saját konvenciók definiálják; mért ellenpár nincs | **részben beismerve, számmal:** a P1.1 lezárult (a mért fél háromból hármon áll), a PKG-15-9 pedig ellenőrzött kísérletben kimutatta, hogy a fő mezőny „3, 3, 5” mintája konvenció-műtermék. Marad: a KON-01 és a KON-03 érzékenysége |
| 5 | **Kis rendszerek:** ami 12 objektumon tétel, az a határértékben lehet műtermék (a PKG-14-5 precedens ezt bizonyította is) | P4.1–P4.4, P4.6 (méret-létra, 100 → 10³ → 10⁵) |
| 6 | **Statika-katalógus:** a 16 próbából egy számol időfejlődést; nincs hőmérséklet, nincs nyitott rendszer, nincs szava a kvázirészecskére | 3. szakasz (folyamat-modellezés) |

A diagnózis kulcsa: a vádak nem cáfolandók vitában — mindegyikhez fájlban fekvő, gépileg ellenőrzött ellenbizonyíték építendő.

---

## 2. A mérce: a „high-end" hat feltétele

A „high-end" nem önminősítés, hanem hat, előre rögzített, gépileg auditálható feltétel. A program akkor ért célba, ha mind a hat áll — és minden feltételhez tartozik becsületes bukó-ág is.

- **H1 — Zárt könyvelés.** Minden állítás pontosan egy kategóriában áll: törvény / géppel ellenőrzött levezetési nyomvonalú tétel / kimondott konvenció / peremadat (a világ példány-adata, amelyet a nyelv elvileg sem vezet le). A megmagyarázatlan importok száma 0, vagy legfeljebb 1, kimondott hatókörrel. A szám nyilvános és követhető (ma: **4** — a 2026-08-20-i függőségi audit egy be nem könyvelt bemenetet, a kiterjedésszámot talált; a szám nem azért nőtt, mert új import került be, hanem mert a könyvelés rövid volt).
- **H2 — Tisztázott formális státusz.** Vagy bizonyított megfeleltetési tétel (az öt törvény + importok pontosan a véges dimenziós, rácsos kvantummechanikát adják — ekkor a nyelv értéke a levezetési út és a könyvelés, kimondva), vagy legalább egy megnevezett, számolható eltérési pont.
- **H3 — Predikció.** Gépi tanúval igazolt vak-protokoll; legalább két belső jóslat (saját, még le nem olvasott számolásokon) és legalább egy időbélyegesen regisztrált, fizikus közönség előtt is jóslatnak számító állítás.
- **H4 — Skálázás.** A nyelv saját tételeiből indokolt gépezetek (felület-törvény → tenzorháló; tanítás → neurális tanú) 100-tól 10⁵ objektumig, minden szám pecséttel (fokozat + erő).
- **H5 — Folyamat-modellezés.** A 4. törvény motor-fele valódi terjedést, tanú-ütemet (nyitott rendszert) és hőmérsékletet is számol, mért célszámokon.
- **H6 — Hatókör-térkép.** A nyelv határa (relativitás, változó példányszám, gravitáció) ugyanolyan pontosan kimondva, mint a törvényei — soronként gépileg ellenőrzött ütközés-példával.

---

## 3. A program szerkezete: öt szakasz, kapukkal

```
0. szakasz          1. szakasz         2. szakasz        3. szakasz          4. szakasz
FUNDAMENTUM   ──►   HITELESSÉG   ──►   ZÁRÁS       ──►   FOLYAMAT      ──►   SKÁLÁZÁS ÉS
(mag, pad,          (vak próbák,       (importok,        (dinamika,          ELSŐ-KIMONDÁS
széf, agent-        auditok, a         tételesítés,      tanú-ütem,          (gépezetek,
protokoll)          8-as tető)         formális          hőmérséklet,        külső jóslatok,
                                       státusz)          új típusok)         zárási audit)
```

A szakaszhatár kapu: a következő szakasz csak az előző kimondott ítéletei után nyílik — kivéve a megjelölt párhuzamos ágakat. A 3. és 4. szakasz nagyrészt párhuzamosan futhat, mert más gépezetre épülnek. Minden mérföldkő teljes csomag-nyomvonallal fut (szabálykönyv → számolás-csomagok → ítélet), és bármelyik érvényes kimenete a rögzített bukás is.

---

## 4. Mérföldkövek

### 0. szakasz — A fundamentum (mind a négy párhuzamosan indítható)

**P0.1 — A formális mag és a „levezetett" ige.**
- *Kérdés:* előállítható-e a nyelv teljes fogalom-, törvény-, tétel- és import-leltára gépileg olvasható definíció-tárként, amelyen egy ellenőrző futás eldönti minden állítás státuszát?
- *Siker:* `shared/kernel/` alatt definíció-tár + ellenőrző szkript, amely igazolja: (a) a függőségi gráf körmentes; (b) minden tétel levezetési útja törvényben, importban vagy korábbi tételben végződik; (c) a szabályrend szerinti próbák import-számlája egyezik a mag nyilvántartásával. A „levezetett" ige hármas operatív definíciója rögzül: (1) premissza csak mag-csomópont lehet; (2) az import-delta ≤ 0; (3) a regresszió zöld — az importot a tétellel helyettesítve mind a 16 próba ítélete változatlan. A nyilvántartás háromkategóriás lesz: **import / konvenció / peremadat**. Külön kimondandó tétel a magban: a **fizikai állandók** (ħ, mₑ, e — a skála-kalibráció, amellyel a nyelv dimenziótlan rács-számai mért egységekre váltanak) peremadat-rangú bemenetek; a tár próbánként nyilvántartja, melyik melyiket használja, és a zárási audit (P4.7) ellenőrzi.
- *Bukás-ág:* ha három vagy több próba nem rekonstruálható a magból be nem jelentett import nélkül, a nyelv nem zárt — előbb a lyukak pótlandók, nem a formalizálás erőltetendő.
- *Megjegyzés:* bizonyítás-asszisztens (Lean/Coq) ebben a fokban **nem** kell; a minimális hasznos alak a típusos, futtatható definíció-tár. Az asszisztens csak a zárt alakú tételekre (lyuk-tükör, irány-tétel, összeomlási tétel) mérlegelendő, később, külön döntéssel.

**P0.2 — A hitelesítő-pad.**
- *Kérdés:* gépi futtatással, emberi kéz nélkül visszaadja-e mind a négy meglévő eszköz a [B függelék](appendix/B-machinery_hu.md) összes rögzített ellenőrző számát? — az eszközök futtatható alakja a szabályrend előtti próbáknál még nem áll rendelkezésre, ezért a pad hatóköre a szabályrend szerinti próbák ellenőrző számai.
- *Siker:* egyetlen paranccsal lefutó regressziós pad, zöld/piros ítélettel minden beépített pontossági ellenőrzésre (1,2533/1,246; a 9/16; a Kagome-érték; a 132-es nyom; a II/13–II/16 kettős számolásai és pecsétjei), géppel olvasható tűrés-fájllal.
- *Bukás-ág:* ami csak kézzel reprodukálható, az reprodukálhatósági adósság — előbb ez törlesztendő, mielőtt bármi új épül.

**P0.3 — A célszám-széf és a jóslat-regiszter.**
- *Kérdés:* kikényszeríthető-e gépi tanúval, hogy egy levezetés a célszám ismerete nélkül záruljon le?
- *Siker:* minden célszám sózott hash-ben, külön széf-fájlban; a jóslat-regiszter géppel olvasható (jóslat-mondat a nyelv fogalmaiból, szám, tűrés, forrás, bukás-feltétel, commit-hash, dátum); egy teljes vak-futás egy már álló próbán (kalibráció: a II/8 mellékcsúcsai) igazolja, hogy a levezetés-lezáró commit megelőzi a széf-nyitót.
- *Bukás-ág:* ha a protokoll gépi tanúval nem kényszeríthető ki, a program nem indulhat — előbb környezetet kell váltani.

**P0.4 — Az agent-protokoll 1.0.**
- *Kérdés:* a csomag-módszer emberi fegyelme gépi kikényszerítésre emelhető-e?
- *Siker:* szabálykönyv-sablon és -generátor, kapu-ellenőr (hash-elt szabálykönyv, pecsét-ellenőrzés, tűrés-tágítás tiltása), import-könyvelő, reprodukciós futtató (az `environment-check` mintájára) és gépi állapot-mentő. A protokoll vizsgája a P1.1: az a mérföldkő legfeljebb 1 emberi érintéssel (végső elfogadás) fut végig.
- *Ítélet-sáv, hézag nélkül:* ≤ 1 érintés = áll; 2–3 érintés = részleges — a gyenge pontok néven nevezendők, a P1.2–P1.5 indulhat, de a P4.7 zárolva a javításig; > 3 érintés = a protokoll bukott, újratervezendő, mielőtt drágább kampány épülne rá.

### 1. szakasz — Hitelesség (olcsó, nagy hozamú lépések; a vádak semlegesítése)

**P1.1 — A nyolcas koordináció teljes-mezőny-teteje** *(belső vak-jóslat; az agent-protokoll vizsgája).*
- *Kérdés:* a nyolcas koordináción a teljes mezőny tetejét tükör-jegyű vonal-tag viszi-e, ahogy a tető-törvény állítja?
- *Siker:* az agent a tető-törvényből **előre** megnevezi a győztes lépés-halmazt (regiszter-commit), MAJD újrafuttatja a nyolcas versenyt a [PKG-15-2](II-proofs/II-15-dimension-fourth-rung/PKG-15-2-ladders_hu.md) mentett létra-gyorsítótárából (`shared/II-15-dimension-fourth-rung/letrak_gepi/`) — a futás a PKG-16-3 mintájára állapot-mentővé bővítve —, és a mentett állapotból végzi el ugyanazt a leolvasást, amit a [PKG-16-5](II-proofs/II-16-coordination-ten/PKG-16-5-transfer_hu.md) tízesen megcsinált. *Ténybeli helyesbítés, kimondva:* a repó (III/1, 8.a) „mentett verseny-állapot"-ot említ, de a fájlrendszeren ilyen nincs — csak a létrák gyorsítótára él; a verseny újrafuttatandó, ami a kész létrákból olcsó (a verseny maga részösszeg-számolás). A vak-feltétel így is természetes: a jóslat-commit a futtatás előtt rögzül, és a válasz ma senkinek nincs a birtokában.
- *Bukás-ág:* ha a tető nem tükör-jegyű tagé (a legtöbbet nyerő három imitátorból kettő páros lépésű, tehát az eredmény nem sejthető!), a tető-törvény mért fele teljes mezőnyön megbukott — rögzített bukás, a törvény a fő mezőnyre szűkítendő, és a P2.3 hordozó-levezetése új célt kap: megmagyarázni a kivételt.
- *Kimenet:* PKG-15-8 csomag; a [III/1, 8.](III-frontier/III-01-candidate-laws_hu.md) táblájának „nincs megnézve" cellája kitöltve, és a 8.(a) „mentett verseny-állapot" szövege helyesbítve.

**P1.2 — Az átcímkézés-audit (prior-art minden tételre).**
- *Kérdés:* van-e a nyelv tételei közt legalább kettő, amely nem egy ismert standard eredmény átnevezése?
- *Siker:* tétel-per-tétel megfeleltetés-tábla rögzített keresési protokollal, háromértékű ítélettel: „ismert eredmény fordítása" / „ismert eredmény új levezetési úton" / „nincs publikált megfelelő" — legalább 2 tétel a harmadik kategóriában. *Kimondva:* ez a mérföldkő a bevezető gépi-eldönthetőség ígéretének kivétele — a hiány kereséssel nem bizonyítható; az ítélet protokoll-audit: rögzített keresési lépések, naplózott találatok, harmadik fél által megismételhető.
- *Bukás-ág:* ha minden tétel az első kategória, és a levezetési út is lépésről lépésre a standardot követi: a „tétel" szó „fordítás"-ra cserélendő, és a program a pedagógiai irányra szűkítendő. Ez is kimondható, becsületes végállapot.

**P1.3 — A konvenció-robusztussági próba.**
- *Kérdés:* túléli-e a tető-törvény a saját konvencióinak perturbálását?
- *Siker:* a versenyszabály és a kiválasztási szabály legalább 3 előre regisztrált, független variánsán (más költségvetés-normálás, más mezőny-kiválasztás) a tető-győztes változatlan mindhárom koordináción. Melléje: legalább egy publikált mért vagy numerikus rendszer megnevezése, ahol sűrűségfüggő effektív dimenzió-váltás látszik — vagy ennek hiánya őszintén rögzítve.
- *Bukás-ág:* ha a győztes a három előre regisztrált variáns bármelyikén megfordul, a tető-törvény konvenció-műtermék — a III/1, 8. törlendő, és a II/13–II/16 ítélete „saját szabálykönyvön belül érvényes"-re szűkítendő.

**P1.4 — Vak célpont-sorsolás.**
- *Kérdés:* áll-e a nyelv olyan célpontokon is, amelyeket nem a szerző választott?
- *Siker:* legalább 20 célpont sorsolva rögzített szabállyal publikált benchmark-táblákból (egzakt diagonalizációs értékek, tankönyvi zárt alakok); a jóslat-csomag hash-elve a számolás előtt; minden bukás néven nevezve az indexbe kerül.
- *Ítélet-sáv, hézag nélkül:* ≥ 80% találat = áll; 50–79% = részleges — a bukott célpontok import-számlája kötelezően elemzendő, a P4.4/P4.5 zárolva a tisztázásig; < 50% = a 16 próba célpont-választási torzítás terméke, a II. rész „áll" ítéletei „áll, választott célponton"-ra minősítendők át.

**P1.5 — A vak-retrodikciós létra: öt publikált, be nem épített célszám.**
- *Kérdés:* ad-e a nyelv vakon helyes számot olyan mért vagy egzakt eredményekre, amelyekre még sosem számolt rá?
- *Az öt cél, egyenként ítélve:* (1) a hidrogénmolekula kötéserőssége a [III/1, 2.](III-frontier/III-01-candidate-laws_hu.md) levezetésből — **kimondottan párhuzamos ág a P2.2-vel, a szakasz-kapu alól kivéve**: ez a cél a P2.2 vak-futása, ítélete a P2.2-vel együtt születik, a P2.2 kétlépcsős kritériuma szerint; a P1.5 a maradék négy célon lezárható. Célszám csak forrás-auditáltan kerülhet a széfbe: a **mért** szám D₀ = 4,4781 eV (Herzberg); a De ≈ 4,7477 eV (38 292,9 cm⁻¹) **számított referencia**, nem közvetlen mérés — a széf-bejegyzés e státuszt is rögzíti. (2) a háromkiterjedésű tál betelése — 2, 8, 20, tűrés nulla; *nem vak cél, kimondva:* a választ a [II/7](II-proofs/II-07-bowl-magic-numbers/proof_hu.md) kitekintője nyíltan tartalmazza, ez a kitekintő beváltása — a széf-zár rá nem értelmezhető. (3) a hálózatos Bell-sértés — Renou 2021 kvantum-értéke, és kötelezően a valós-súlyú korlát **fölött**; (4) a Heisenberg-gyűrű kötésenkénti alapenergiájának termodinamikai határa — Bethe/Hulthén publikált egzakt értéke (¼ − ln 2), méret-extrapolációval, előre rögzített extrapolációs szabálykönyvvel (a repó a 12-es gyűrűig jutott — a határérték új számolás); (5) az egymásba ágyazott tanú — Bong és társai 2020 publikált sértése.
- *Siker:* legalább 4 az 5-ből áll. *Bukás-ág:* célonként — tűrésen kívüli szám, vagy ha a lezáráshoz új import kell (akkor az ítélet „lyukas", nem „áll"). Ha 5-ből 2+ bukik: a külső jóslatok (P4.4, P4.5) zárolva; a bukott célok import-számlája jelöli ki, mit kell előbb a nyelvbe beépíteni.
- *A vak-protokoll korlátja, kimondva:* a végrehajtó AI-agent nem vak — a publikált célszámok a tanítóadatában lehetnek; a széf a leolvasás ellen véd, a betanult előzetes tudás ellen nem. Publikált célszámon a vak-protokoll ezért **„fegyelmezett retrodikciót"** tanúsít, nem jóslatot; a „jóslat" cím kizárólag a valóban ismeretlen kimenetű célokat illeti (P1.1, P2.3, P4.4, P4.5). Ellenszer a szabálykönyvben: minden numerikus szabad választás (felosztás, extrapolációs alak, konvergencia-kritérium) célszám-független indoklással, előre rögzítve; kötelező érzékenységi vizsgálat — a választások perturbálása nem tolhatja a számot a cél felé.
- *Kimenet:* öt új próbafejezet a II. részben; a [C függelék](appendix/C-benchmarks_hu.md) bővítése.

### 2. szakasz — Zárás (import-nullázás és tételesítés)

**P2.1 — A helyiség-zárás: a helyek egyenrangúsága tétel vagy negyedik import.**
- *Kérdés:* levezethető-e a helyek egyenrangúsága az 5. törvény hely-kiterjesztéseként (a [II/11](II-proofs/II-11-locality-readout/proof_hu.md) átnevezés-próbájának irányán), nulla új importtal — és élesíthető-e a kiválasztási törvény (a fok-rezonanciás kivételek megértése)?
- *Siker:* csomag-módszeres levezetés kizárólag mag-premisszákból; import-delta 0; a II/12 regressziója zöld (a vákuum-parkoló zárása tételből következik). A mag státusza „jelölt" → „tétel".
- *Bukás-ág:* ha be nem jelentett feltevés kell, a jelölt — az [I/1](I-language/I-01-concept_hu.md)-ben előre bejelentett módon — **negyedik importtá válik.** Ez is lezárás: az importszám nő, de a kettős állású elem eltűnik. Kettős állású elem a magban nem maradhat.

**P2.2 — A kötés-szerződés tétellé: a hidrogénmolekula-próba.** *(kimondottan párhuzamos ág a P1.5 1. céljával, a szakasz-kapu alól kivéve)*
- *Kérdés:* kiadja-e a [II/8](II-proofs/II-08-exclusion-vs-repulsion/proof_hu.md) mechanizmusa (két szomszédos gödör, ellenkező előjel) a [II/1](II-proofs/II-01-pair-bond/proof_hu.md) szerep-tiltó szerződését úgy, hogy a csatolás erőssége levezetett szám?
- *Siker, két lépcsőben — a fizikailag reális kalibrációval:* **(a) a law→theorem konverzió** — a szerep-tiltó szerződés alakja ÉS a csatolás nagyságrendje kijön a mechanizmusból, kimondott, laza tűréssel (5–10%, a szabálykönyvben előre): ezzel a nyelv első bevizsgált szerződése axiómából tétellé lép; **(b) az eV-pontos réteg, külön és opcionálisan** — csak akkor, ha teljes kételektronos számolás fut, reális tűréssel (≥ 0,005 eV), és a pontossági padló kimondva: a negyedik tizedes szintjén (~0,1 meV) már relativisztikus és adiabatikus korrekciók élnek, amelyeket a nyelv (P3.6, H6) hatókörön kívülre zár — e szint alá a siker-kritérium elvből nem mehet. Kétutas számolás, vak-protokoll mindkét lépcsőn.
- *Bukás-ág:* ha a két kódút egyezik, de az (a) lépcső száma tűrésen kívül: a szerződés axióma marad, a bukás csomagban rögzítve. A tűrés utólagos tágítása tilos; a (b) lépcső elmaradása nem bukás, hanem kimondott hatókör-határ.

**P2.3 — A hordozó-tétel, a tükör-hordozó-térkép és a 12-es koordináció jóslata.**
- *Kérdés:* levezethető-e, hogy miért a tükör választ (a [III/1, 7.](III-frontier/III-01-candidate-laws_hu.md) tételesítése), és kiadja-e a térkép, mely koordináción mely fok a legalacsonyabb tükör-jegyű szövés?
- *Siker, két lépcsőben:* (a) a hordozó-tétel mag-premisszákból, amely paraméter nélkül visszaadja mindhárom mért koordináció (6, 8, 10) tetejét; (b) **előre regisztrált jóslat a 12-es koordinációra** — a tető-hordozó neve és a lépcső kihagyott fokai. A jóslat regisztrálása e mérföldkő dolga; az ellenőrző verseny maga 10⁵-nél nagyobb rendszert kíván (a honos fok hatodrendű szövése), ezért az a P4.6 kampányában fut, a skálázott gépezettel — a jóslat addig „regisztrált, ítéletre vár" státuszú. Ráadás-cél, ha a térkép kiadja: a dominancia-hézag ~fele-mintájának előre kimondott alakja.
- *Bukás-ág:* ha a térkép a három ismert koordináció bármelyikét nem adja vissza — a levezetés bukik. Ha a térkép áll, de a 12-es jóslat bukik — a tető-törvény predikciós törvényként megbukott, mért leletté fokozandó le. P1.1 + P2.3 együttes bukása a teljes kiterjedés-program értelmezését nyitja újra.
- *Ez a program első, teljes értékű belső predikciója: a fizikának erre nincs publikált eredménye.*

**P2.4 — Az 1/r zárás-kísérlete.**
- *Kérdés:* levezethető-e a vonzásalak a nyelven belülről — a kiterjedés-program három-eredményéből és a helyiség-nézetből, a győztes tér-szövés hosszútávú (Green-függvény-szerű) alakjaként — kör nélkül?
- *Siker, három rétegben:* (a) a mag gráfja gépileg igazolja, hogy a II/13–II/16 sehol nem támaszkodik az 1/r-importra (a kör kizárva — ellenőrizendő, nem feltételezendő); (b) a levezetett hosszútávú alak 1/r a rögzített korrekciós korláton belül; (c) a II/4 regressziója zöld (a négy tizedes változatlan).
- *Bukás-ág:* ha az alak csak aszimptotikusan 1/r és a korrekciók a hidrogén skáláján rontanak, VAGY a gráf kört talál: az 1/r **végleges importtá** nyilvánítandó, kimondott hatókörrel („a vonzásalak a nyelv bemenete a gyökér-program lezárásáig"). A fél-eredmény is rögzítendő: milyen kitevőt ad a nyelv magától.
- *Ez a program legnehezebb zárás-kísérlete — a 2. vád ezen áll vagy bukik véglegesen.*

**P2.5 — A peremadat-átminősítés: az elektron-típusdeklarációk.**
- *Kérdés:* szétválasztható-e gépileg, hogy a nyelv a típus-lehetőségteret vezeti le (két osztály + a származtatott típusok nyitása), a „melyik osztály az elektron" pedig peremadat — a világ példány-adata, nem a nyelv adóssága?
- *Siker:* gépi ellenőrzés igazolja, hogy egyetlen tétel sem használja a kizárólagosság **indokát**, csak az **értékét** — a deklaráció kezdőfeltételként viselkedik. Hatókör-mondat a magban: a spin–statisztika a relativisztikus szerkezetből jön, amely a nyelv hatókörén kívül áll.
- *Bukás-ág:* ha bármely levezetés az okra támaszkodik, az átminősítés érvénytelen — a deklaráció import marad, és a [III/2, 4.](III-frontier/III-02-open-questions_hu.md) (nyelven belüli út a kizáráshoz) kötelező ággá lép elő.
- *Kimondva:* ez az az import, amelyről gyanítható, hogy sosem lesz nyelven belül levezethető — a becsületes lezárás itt nem a levezetés erőltetése, hanem a peremadattá minősítés, géppel ellenőrzött feltételekkel.

**P2.6 — Ekvivalencia vagy eltérési pont: a formális státusz.**
- *Kérdés:* az öt törvény bizonyítottan ekvivalens-e a standard QM egy pontosan körülhatárolt szegmensével, vagy van legalább egy számolható eltérési pont?
- *Siker, bármelyik ágon:* (a) formális megfeleltetési tétel — az öt törvény + importok pontosan a véges dimenziós, rácsos QM-et adják; ekkor a nyelv értéke kimondottan a levezetési út és az import-könyvelés: becsületes, védhető pozíció; VAGY (b) egy megnevezett eltérési pont, számolható próbával és mérhető következménnyel — a maximális tudományos tét.
- *Bukás-ág:* ha két iterációban egyik ág sem zárul, az „elmélet" és „zárt" szavak használata felfüggesztendő; a státusz „formálisan tisztázatlan jelölt-keret", és ezt a címlap mondja ki.

**P2.7 — A kontinuum-tétel.**
- *Kérdés:* bizonyítható-e tételként, hogy a rácsgépezet létrája a felosztás finomításával rögzített rendben (hᵖ, p néven nevezve) tart a folytonos értékhez?
- *Siker:* bizonyított hibakorlát a B függelékben + gépi konvergencia-jegyzőkönyv: a II/3 és II/4 legalább 4 finomítási lépésén a mért rend a bizonyítottól 5%-nál kevesebbel tér el. A II/4 négy tizedese ettől kezdve tételes hibakorláttal áll, nem tapasztalatival — visszamenőleg is felértékelve.
- *Bukás-ág:* ha a vonzó szerződés szingularitása miatt a rend romlik és nem kezelhető: hatókör-határ kimondva — mely szerződésalakokra tételes a kontinuum, melyekre tapasztalati.

### 3. szakasz — Folyamat-modellezés (hatókör-bővítés; a P3.4 és a P2.7 bármikor párhuzamosan indítható)

**P3.1 — A hatókör sebessége (fénykúp-próba).**
- *Kérdés:* az állapot hirtelen átírása (a fizika quench-nek hívja) után a hatás véges sebességű frontban terjed-e, és a front sebessége a szerződés-ütemekből számolható-e?
- *Siker:* a gépezet időfejlesztett front-sebessége egyezik a zárt alakú maximális csoportsebességgel 1%-on belül (≥12 példányos lánc); a fronton kívüli jel exponenciálisan nyomott, kétutasan; valóság-ellenőrzés: **Jurcevic és társai 2014** mért fénykúp-terjedése fogott ionokon (spin-rendszer — a meglévő típusokkal fut) a publikált hibán belül. A Cheneau és társai 2012 Bose–Hubbard-mérés másodlagos cél, csak az osztozó deklaráció (P3.5) után — a függőség kimondva, hogy be nem jelentett import ne csússzon be.
- *Bukás-ág:* ha a kimondáshoz új fogalmat kell kölcsönözni, vagy a front nem válik el a zajtól — bukás-próbaként rögzítve, a hiányzó fogalom néven nevezve.
- *Új fogalom-jelölt:* a „hatókör-sebesség" — csak a próba átmenése után kap nevet az I. részben.

**P3.2 — A tanú üteme (nyitott rendszer).**
- *Kérdés:* a [II/10](II-proofs/II-10-internal-witness/proof_hu.md) tanú-szabályának időbeli alakja kiadja-e a mért dekoherencia-rátákat szabad paraméter nélkül?
- *Siker:* a tanú-ütem egyenlet (a Lindblad-megfelelő) a teljes állapottér egzakt időfejlesztéséből határátmenetként adódik, kétutasan; a Brune és társai 1996 mérte dekoherencia-ráták a szétválasztás négyzetes skálázásával a publikált mérési hibán belül konzisztensek (a cikk kevés ponton a konzisztenciát mutatta, illesztett kitevő-hibasávot nem publikált — a kritérium ehhez van kalibrálva); legalább egy publikált qubit T₂/T₁ arány visszaadva.
- *Bukás-ág:* ha a tanú-ütem csak a Lindblad-alak átcímkézése (az import-számla „nem segít" ítélete), bukás-próbaként rögzítendő a II/12 mintájára.
- *Ez a nyelv legpiacképesebb darabja: minden kvantumtechnológiai zajmodell erre a fogalomra épül.*

**P3.3 — A meleg létra (véges hőmérséklet).**
- *Kérdés:* ha a hőmérséklet a tanú-csere üteme (nem új import), az ütem-létra betöltési súlyaiból kijön-e a mért termikus viselkedés?
- *Siker:* (a) a Schottky-púp zárt alakban; (b) a döntő cél: a kétkiterjedésű Ising-átmenet, T_c/J = 2/ln(1+√2) = 2,2692 négy tizedesre, rögzített végesméret-szabálykönyvvel; (c) a hőmérséklet az import-számlán „levezetett" vagy pontosan egy néven nevezett új tétel.
- *Bukás-ág:* ha a termikus súlyok nem vezethetők le a tanú-cserearányból, hanem be kell hozni őket — az azonnal import, és a mérföldkő „lyukas" ítélettel zárul.
- *Sorrend-kényszer:* P3.2 után — hőmérsékletet tanú nélkül bevezetni kényszer-import volna.

**P3.4 — A származtatott típus (toric code).** *(nulla import-kockázat, bármikor indítható)*
- *Kérdés:* kimondható-e a „mintázatból lett objektum" ([III/2, 7.](III-frontier/III-02-open-questions_hu.md)): a toric code hibamintázatai önálló példányként viselkednek-e, saját típusosztállyal, amely se nem kizáró, se nem osztozó?
- *Siker, négy egzakt számmal:* alapállapoti elfajulás tóruszon = 4; a származtatott példány létrehozási ára egzakt; az e- és m-példány körbevezetési fázisa = −1 (a kétosztályos tételen kívüli, harmadik viselkedés); a topologikus tanú-jegy γ = ln 2 a nézet-számításból. Mind kétutasan, a meglévő 4. eszközzel.
- *Bukás-ág:* ha a származtatott példányra az 5. törvény (átnevezés-próba) megbukik, a „származtatott típus" nem típus — és ezt kell kimondani.
- *Két front egy mérföldkövön:* lezárja a III/2, 7.-et ÉS megnyitja a gyökér-programot (ha a csatolást mintázatok hordozzák, a kiválasztás kérdése itt válik támadhatóvá).

**P3.5 — Az osztozó osztály első próbája (BEC).**
- *Kérdés:* az osztozó deklaráció mellett (előre bejelentett import-tétel) sok példány közös legalsó ütemre gyűlése kiadja-e a mért kondenzátum-görbét?
- *Siker:* N₀/N = 1 − (T/T_c)³ a nyelv levezetésében; Ensher és társai 1996 mért görbéje és T_c-eltolódása a publikált hibán belül; az import-számlán pontosan egy új tétel (az osztozó deklaráció — a bejelentett deklaráció itt nem számít be nem jelentett importnak, ez a kivétel kimondva). Vak-kiegészítő cél a széffel: a kondenzációs küszöb ζ(3)-as együtthatója — ez ide tartozik, nem az 1. szakaszba, mert hőmérséklet-fogalom (P3.3) nélkül számolhatatlan.
- *Bukás-ág:* ha a mért egyezéshez kölcsönhatási korrekció kell, a próba „ideális-gáz határig áll" ítélettel szűkítendő, nem szépítendő.

**P3.6 — A határ-próba (kimondott bukás-próba).**
- *Kérdés:* előre bejelentett bukás-próba — a hidrogén finomszerkezete (a 2P-felhasadás, 10 969 MHz) a meglévő importokkal elérhetetlen; a cél a hiány pontos lokalizálása, nem az egyezés.
- *Siker = a pontos bukás:* (a) a számolás reprodukálhatóan NEM adja ki a felhasadást; (b) a hiányzó fogalom néven nevezve a III. részbe kerül (a példány belső forgása és a hatókör-sebesség csatolása — a relativisztikus küszöb); (c) elkészül a **hatókör-tábla** (III-03): soronként relativitás / változó példányszám / gravitáció — melyik törvénnyel ütközik, mi volna a belépő import.
- *Fordított bukás-ág:* ha a próba szabálykönyv-módosítás nélkül mégis kiadja a felhasadást, az nem bukás, hanem felfedezés — külön csomagban rögzítendő.
- *Ez a program legolcsóbb, legmaradandóbb terméke: minden bíráló első kérdésére („és a relativitás?") előre kész, számolt válasz.*

### 4. szakasz — Skálázás és első-kimondás

**P4.1 — A nézet-gépezet: tenzorháló bevizsgálása.**
- *Kérdés:* a felület-törvényből ([II/11](II-proofs/II-11-locality-readout/proof_hu.md)) natívan indokolt MPS-gépezet visszaadja-e a megoldott próbák egzakt számait, tanúsítható levágási hibával?
- *Siker:* a 12 objektumos Kagome-érték és a 12-es kör kötésára 10⁻¹⁰-en belül; a II/3 létra és a II/9 sáv-döntés reprodukálva; minden futás pecsétet ad (eldobott súly + kötésméret-extrapoláció); 100 objektumos konvergált, tanúsított futás. Az ötödik eszköz a B függelékben, hatókör-nyilatkozattal.
- *Kulcs-elv:* a felület-törvény a gépezet **tételi indoka** — kevés elmélet-nyelv tudja a saját numerikájának létjogosultságát tételből indokolni. Minden ténylegesen kölcsönzött elem tételesen könyvelendő.
- *Bukás-ág:* ha a bevizsgálás nem könyvelhető fogalmat igényel, a gépezet nem natív és nem vehető fel.

**P4.2 — A tanítás-gépezet: neurális tanú.**
- *Kérdés:* az [I/5](I-language/I-05-contract_hu.md) tanítás-fogalmának szó szerinti gépesítése (variációs tanítás a súlyvektor-téren) visszaadja-e a II/5 és II/8 rögzített számait, majd fut-e 10³ objektumon?
- *Siker:* a frusztráció-maradék és a csúcsszerkezet (2, 6, 12; 4, 9) tűrésen belül; 10³ objektumon konvergált futás; pecsét = a becslő szórása + két független magvú tanítás egyezése (a kétutas szabály tanítás-alakja). A hatodik eszköz a B függelékben.
- *Bukás-ág:* ha két független magvú tanítás a tűrésen kívül tér el, a gépezet nem pecsételhető.

**P4.3 — A pecsét-kalkulus.**
- *Kérdés:* megadható-e egyetlen fokozat-rend és számszerű pecsét-erő úgy, hogy a II/16 rögtönzött alakjai a rendszer speciális eseteiként állnak elő?
- *Siker:* kimondott fokozat-rend (teljes kétutas > ritka alak > mintavételes pecsét > szórás-pecsét), számszerű lefedettség-definícióval; a II/16 pecsétjei (5,3·10⁻¹⁴; 5,1·10⁻¹⁴; 9,4·10⁻¹⁶) a könyvtárból újraszámolva egyeznek; ettől kezdve minden futás kötelezően pecsét-mezőt hordoz, és a kapu-ellenőr pecsét nélküli ítéletet nem enged át.
- *Bukás-ág:* ha a II/16 pecsétjei nem állnak elő a rendszerből, a kalkulus rossz absztrakció — újratervezendő, mielőtt a 10⁵-ös kampány ráépül.

**P4.4 — Melyik folyadék? (külső jóslat #1).**
- *Kérdés:* réses vagy réstelen a Kagome-folyadék — és ha réses, mekkora a rés kötésegységben? *(A szakma évtizede vitatja; konszenzus nincs — a [III/2, 3.](III-frontier/III-02-open-questions_hu.md) maga mondja ki: itt már nem visszaszámolni kell, hanem elsőként kimondani.)*
- *Siker, két rétegben.* Gépi réteg: 100+ objektumos rendszeren, kötésenként 0,003-nál finomabb felbontással (a legjobb szilárd jelölt előnye) ítélet születik; **kötelező elem az előre rögzített végesméret-extrapolációs szabálykönyv legalább három méret-lépcsőn, és a hibasávba az extrapolációs bizonytalanság is beleszámít** — a kérdést a szakma nagy numerikával egy évtizede nem tudta eldönteni, a nehézség a méret-extrapoláció, nem a nyers felbontás; a méret-plafon a publikált élvonalhoz mérve rögzítendő. Ha a sáv elválasztja a réses és réstelen választ, az állásfoglalás időbélyeges, nyilvános regisztrációt kap (repó-release + jegyzet) — ez önmagában mérföldkő-siker: „regisztrált külső jóslat". Valóság-réteg (felfüggesztett ítélet): a később születő konszenzus a sávon belül esik — a bukás-feltétel előre a regiszterben.
- *Bukás-ág:* „eldöntetlen a plafonon" — érvényes, publikálható, határidővel kikényszerített lezárás, és **előre kimondva ez a legvalószínűbb kimenet**: a mérföldkő így is teljesíti a dolgát (tanúsított hibasáv egy nyitott kérdésen); ha a hibasáv átfedi mindkét választ, jóslat nem regisztrálható.
- *Függ:* P4.1 (gépezet), P1.5 (a nyelv vak-hitelessége nélkül a külső jóslatnak nincs súlya).

**P4.5 — A hálózatos Bell-jóslat (külső jóslat #2).**
- *Kérdés:* mond-e a nyelv számot egy még nem mért hálózat-topológia sértési korlátjára?
- *Siker:* egy előre rögzített, kísérlettel le nem fedett elrendezésre a teljes-súlyú és a valós-súlyú korlát külön-külön, hibasávval; a két korlát elválik (különben a jóslat üres); időbélyeges regisztráció + egyoldalas, fizikus-nyelvű jóslat-lap (mit mérjen, mit várunk, mikor buktunk) — kész recept egy kísérletező csoportnak.
- *Bukás-ág:* egyszeri, regiszterben rögzített csere engedélyezett a tartalék külső jóslatra (a dominancia-hézag külsővé érlelt alakja, vagy a herbertsmithite egy mérhető jellemzője). Második csere nincs: akkor a program ítélete „a nyelv retrodikcióra képes, predikcióra még nem" — és ez így kerül a repóba.

**P4.6 — A 10⁵-ös kampány** *(a H4 feltétel hordozója).*
- *Kérdés:* elérnek-e a bevizsgált gépezetek tanúsított futással a 10⁵ objektumos skálára — és mit mondanak ott?
- *Siker:* legalább két tanúsított 10⁵⁺ futás pecséttel (fokozat + erő a P4.3 kalkulusából): (a) a **12-es koordináció ellenőrző versenye** — a P2.3-ban regisztrált tető-jóslat ítélete itt születik meg; (b) legalább egy további nagy hálóverseny vagy nagy frusztrált rendszer a tükör-hordozó-térkép kiterjesztésére. Minden futás gépi állapot-mentéssel zárul (későbbi ingyen-leolvasásokhoz); a kis egzakt esetekkel való átfedésben a gépezetek egyezését pecsét rögzíti.
- *Bukás-ág:* ha a pecsét-erő a rögzített küszöb alá esik, a pont „nem tanúsított" jelölést kap és a térképen lyukként jelenik meg — lyukas térkép publikálható, tanúsítatlan pont állításként soha. Ha a 12-es jóslat itt bukik, a P2.3 bukás-ága lép életbe.
- *Függ:* P2.3 (a regisztrált jóslat), P4.1–P4.3 (gépezetek és pecsét-kalkulus).

**P4.7 — Az ember nélküli kampány és a zárási audit** *(a program záróköve).*
- *Kérdés, két fél:* (a) végigvihető-e egy teljesen új próba (jelölt: a [III/2, 6.](III-frontier/III-02-open-questions_hu.md) lavina-kérdése 10³ objektumon) úgy, hogy ember csak a végső kapunál nyúl hozzá? (b) kiadja-e a mag egyetlen futásban a teljes elszámolást?
- *Siker:* (a) a próba teljes csomag-nyomvonallal lezárul (áll/bukik/részleges — mindhárom érvényes), emberi érintés ≤ 1, reprodukciós futás tiszta környezetben zöld; (b) az audit minden mag-csomópontot pontosan egy kategóriába sorol, minden tételhez körmentes utat mutat, minden próbát változatlan ítélettel ellenőriz, és az importszám ≤ 1 kimondott hatókörrel (vagy 0). A kimenet a **zárt-elmélet tanúsítvány**, emberi és gépi alakban.
- *Bukás-ág:* ha az audit megmagyarázatlan függést talál, a „zárt" szó nem használható — a cím „záruló nyelv", és a hiánylista a következő programciklus bemenete.

---

## 5. Iránymutatások a végrehajtó agenteknek

1. **Csomag-módszer kivétel nélkül.** Szabálykönyv, tűrés, célszám és bukás-kritérium a számolás előtt, hash-lenyomattal rögzítve; kapu-szabály; utólagos tűrés-tágítás vagy szabálymódosítás = a futás automatikusan érvénytelen. Szabálykönyv-módosítás csak új, külön bejelentett próbában.
2. **Célszám-zár.** Minden új próba célszáma sózott hash-ben áll a széfben; a levezetés-lezáró commitnak meg kell előznie a széf-nyitót; amelyik próbán a zár nem igazolható, az retrodikciónak minősül, és az index így jelöli. Retrodikció és jóslat szigorúan külön könyvelendő: ami a regisztráció pillanatában publikált, az visszaszámolás, bármilyen pontos. A zár korlátja kimondva: a végrehajtó AI-agent betanult előzetes tudása ellen a széf nem véd — publikált célszámon ezért kötelező minden numerikus szabad választás célszám-független, előre rögzített indoklása és az érzékenységi vizsgálat (a választások perturbálása nem tolhatja a számot a cél felé); a „jóslat" cím csak valóban ismeretlen kimenetű célt illet.
3. **Pecsét nélkül nincs ítélet.** Minden szám kétutasan (ahol a mezőny nagy: a pecsét-kalkulus következő fokozatán, számmal jelentett lefedettséggel); minden futás kimenete hordozza a pecsét fokozatát és erejét; a kapu-ellenőr pecsét nélküli vagy küszöb alatti eredményt nem enged át. Az ítélet futtatható szkriptből jön — az agent szövege nem ítélet, csak jegyzőkönyv.
4. **Import-fegyelem, hármas nyilvántartással.** IMPORT (a világról szóló kölcsön — adósság) / KONVENCIÓ (a próba saját szabálya — kimondandó, de nem adósság) / PEREMADAT (a világ példány-adata — kezdőfeltétel-rangú). Összemosás tilos; minden csomag záró sora az import-delta; tétel csak delta ≤ 0 és zöld regresszió mellett fogadható el; kettős állású elem határidős döntési kötelezettség alá esik.
5. **Körmentesség gépi kényszer.** A mag függőségi gráfját minden csomag-elfogadás után az ellenőrző futtatja; kör = azonnali elutasítás. Kiemelten él a P2.4-re (kiterjedés-eredmény ↔ 1/r).
6. **A bukás rögzített eredmény.** Minden bukás-ág kimenete néven nevezett negatív tétel vagy hatókör-mondat (a II/12 a minta). Az agent a bukás-kritérium teljesülése után nem „próbálkozik tovább" — lezár, jelent, továbblép. „Eldöntetlen a plafonon" érvényes, határidővel kikényszerített ítélet. A kihagyott és bukott célpontok naplója ugyanolyan nyilvános, mint a sikereseké.
7. **Előléptetési szabály.** Jelölt → tétel csak a „levezetett" gépi kritériumával (P0.1); új törvény tételesítéséhez kötelező legalább egy előre regisztrált jóslat egy még ki nem számolt rendszerre — a visszaszámolás önmagában nem elég. Prior-art keresés (P1.2 protokollja) minden új tétel kihirdetése előtt, álló szabályként.
8. **Méret-fegyelem.** Minden dinamikus/termikus/verseny-állítás legalább két rendszerméreten (a PKG-14-5 mintájára); kulcstételek három egymást követő méret-lépcsőn, előre regisztrált extrapolációs szabállyal; ami csak kis méreten áll, az „kis darabon igazolt" címkét kap. Méret-lépcső a gépezeteknél: 100 → 10³ → 10⁵, fokot ugrani tilos — minden fok átfed a pad legnagyobb egzakt esetével.
9. **Eszköz-bevizsgálási rend.** Új gépezet előbb egy már megoldott próba rögzített számait adja vissza a padon; csak zöld után léphet új terepre. A gépezet feltevései könyvelendők (import / tételi indok / konvenció) — a gépezet nem csempészhet be világ-állítást. A gépezet mérete nem bizonyító erő: ami csak mintavételes pecséttel áll, az „mért", nem „tétel".
10. **Új fogalom csak a levezetése után kap nevet az I. részben** (az I/1 hármas szabálya, kivétel nélkül): a „hatókör-sebesség", a „tanú-ütem", a „hőmérséklet mint cserearány" és a „származtatott típus" addig a III. rész jelöltje, amíg a saját próbája át nem megy.
11. **Gépi állapot-mentés és reprodukció.** Minden verseny és nagy futás mentett állapottal zárul (a PKG-16-5 mintája: a mentett állapot később ingyen-leolvasásokat ad); minden próba elfogadás előtt tiszta környezetben reprodukálandó (az `environment-check` mintájára). Ami nem reprodukálódik, az nincs — a szabály a csomag-módszer bevezetésétől (II/13) él; a korábbi próbákra a 15. pont áll. Tárolási konvenció (a repó ma semmilyen állapotfájlt nem követ — ezt a P0.4 rögzíti): az állapotfájl helye, formátuma és méret-plafonja a szabálykönyv része; ami a git-en kívül marad, annak a rögzített szkriptből való újragenerálhatósága a reprodukciós futás ellenőrzött eleme.
12. **Üres jóslat tilalma.** Csak az a szám jóslat, amely eltérő kimeneteket választ szét; ha a hibasáv az összes versengő választ átfedi, a sor nem kerülhet a regiszterbe. Külső jóslat csak időbélyeges, nyilvános rögzítés után vethető össze későbbi méréssel.
13. **Hatókör-őszinteség.** Amíg a méret-létra (8. pont) le nem zárul egy állításon, kötelező mellé a méret-hatókör („N objektumig igazolt"); amíg a P2.6 le nem zárul, kifelé szóló szövegben az „elmélet" helyett „nyelv" vagy „jelölt-keret" használandó.
14. **Terminológia és kétnyelvűség.** Az agentek a repó saját szavait használják (próba, szerződés, ütem-létra, nézet, tanú, tükör-jegy, import-számla); új szó csak a mag definíció-tárán keresztül; minden fejezet hu/en párban, `pair_status` karbantartva. Az emberi érintések száma csomagonként naplózandó — a csökkenő görbe maga is jelentendő eredmény. Felmentés, kimondva: a 10. és a 14. szabály a nyelv (I. rész) fizikai fogalmaira vonatkozik; a program saját módszertani műszavai (célszám-széf, jóslat-regiszter, peremadat, pecsét-kalkulus) nem fizikai fogalmak — kötelező bejegyzést a P0.1 definíció-tárában kapnak, de próba-átmenés nem előfeltételük.
15. **Szabályrend előtti próbák.** A II/1–II/12 a csomag-módszer előtt készült: ítéletük érvényes, bizonyítékuk viszont nem szabályrend szerinti. Rájuk hivatkozni szabad, de az a mérföldkő, amelyik a számukat premisszaként használja, előbb megismételteti az adott próbát a mai szabályrend szerint, új sorszámon. Az ismétlés kimenete önálló ítélet: ha eltér a korábbitól, az új szám lép életbe, és a rá épülő állítások átvizsgálása a mérföldkő része.

---

## 6. A végső cél

**A program célállapota (a „high-end" tanúsítvány).** Egyetlen mondatban: *egy rendszer megadása — objektumok és szerződések felsorolása — elegendő a viselkedése kiszámolásához, és a nyelv erről szóló minden állítása vagy géppel ellenőrzött levezetési nyomvonalú tétel, vagy kimondott konvenció, vagy kimondott peremadat.* Számon kérhető alakban: a hat H-feltétel (2. szakasz) mindegyike gépi audittal áll — zárt könyvelés importszám ≤ 1-gyel (kimondott hatókörrel) vagy 0-val; tisztázott formális státusz; legalább egy igazolt (vagy becsületesen, számmal megbukott) külső jóslat; bevizsgált skálázó gépezetek 10⁵-ig; folyamat-modellezés mért célszámokon; és a hatókör-térkép. Ha a program bármely bukás-ágba fut, a végállapot ugyanilyen pontos: a repó kimondja, hogy a nyelv számolt szótár, és pontosan meddig ér — ez is lezárás, nem kudarc.

**A horizont (a program után nyíló kapu): a gyökér-program.** A II/12 óta minden mezőny-lelet ugyanoda mutat: a kiválasztás — miért olyan a világ szerződés-szerkezete, amilyen — ott dőlhet el, ahol a szerződések maguk születnek, vagyis ahol a csatolást a példányok mintázatai hordozzák ([III/2, 7–8.](III-frontier/III-02-open-questions_hu.md)). A P3.4 (származtatott típus) nyitja meg a fogalmat, a P2.3 térképe adja hozzá az adatot, a P2.4 kimenete a tétet („a vonzás alakja adja a hármat kívülről; a tükör és a sűrűség belülről; a kettő találkozása a gyökér-program dolga"). A gyökér-program — benne a „miért három kiterjedés" kérdés végső alakjával — nem e program mérföldköve: e program azt éri el, hogy a kérdés spekulációból adatvezérelt, tételekkel körülbástyázott kutatási iránnyá váljon.

---

## 7. Mire lesz jó, ha elérjük

**Tudományos többlet.**
- Az első igazolt vak találat visszamenőleg is felértékeli mind a 16 meglévő próbát: ami eddig „hasonlít-gyűjteménynek" volt leírható, az onnantól egy prediktív nyelv kalibrációs szakasza.
- Az import-levezetések (helyiség, kötés-szerződés, esetleg 1/r) a nyelv első valódi többlete a standard felett: amit a kvantummechanika **posztulál**, azt a nyelv **levezeti** — ez már nem átcímkézés.
- A Kagome-állásfoglalás és a hálózatos Bell-jóslat valódi tudományos tét: az egyik egy évtizedes nyitott kérdést dönt el számmal, a másik kész kísérleti recept egy mérőcsoportnak. A tükör-hordozó-térkép és a 12-es koordináció jóslata pedig olyan terepen bizonyít, amelyet a fizika még nem is térképezett fel.
- Az ekvivalencia-kérdés (P2.6) bármelyik ágán nyerő: vagy egy bizonyítottan hű, taníthatóbb axiomatizálást kapunk import-könyveléssel, vagy egy kísérletileg tesztelhető eltérési pontot — az utóbbi a maximális tét.

**Gyakorlati haszon.**
- A tanú-ütem (P3.2) minden kvantumtechnológiai zajmodell alapfogalma: ha a levezetés áll, a nyelv a qubit-dekoherencia natív leíró nyelve — a kvantumszámítás-mérnökség felé ez a közvetlen kapu.
- A skálázó gépezetek (tenzorháló, neurális tanú, pecsét-kalkulus) auditálható numerikus eszköztárrá érnek, amely a repón kívüli kondenzált anyag problémákra is bevethető.
- A hatókör-térkép (P3.6) után minden bíráló első kérdésére előre kész, számolt válasz van — a nyelv határa nem gyengeség, hanem kimondott eredmény.

**Módszertani export — talán a legmaradandóbb.**
- A célszám-széf, a jóslat-regiszter, a pecsét-kalkulus és az agent-protokoll együtt egy publikálható minta: **gépileg ellenőrzött, előre regisztrált, célpont-válogatás-álló elméletépítés AI-agentekkel** — a csomag-módszer természetes betetőzése. Ez a repón túl is érték: bármely AI-vezérelt kutatási program átveheti.
- A regressziós pad a meglévő tudást örökös, gépileg őrzött vagyonná teszi: a nyelv nem tud csendben megromlani — minden bővítés a teljes múlt ellenében vizsgázik.
- És a bukás-ágak is hasznot hoznak: egy becsületesen lezárt irány („az 1/r nem levezethető — végleges import") megspórolja az összes ráépülő munkát, a bukás-könyvelés kultúrája pedig — a II/12-től a zárási auditig — önmagában is minta arra, hogyan kell elméletet úgy építeni, hogy az megölhetetlen legyen: nem azért, mert nem lehet megtámadni, hanem mert minden támadáshoz fájlban fekvő, gépileg ellenőrzött válasz tartozik.

**Pedagógiai haszon.** Ha a formális státusz az ekvivalencia-ágon zárul, a nyelv a kvantummechanika taníthatóbb, programozói fogalmakra épülő, axiomatikusan könyvelt bejárata — a belépési küszöb csökkentése mérhető, önálló érték.

---

*A program mérföldkövei csomag-módszerrel futnak; ez a fájl a mérföldkövek szabálykönyveinek szabálykönyve. Módosítása a repó rendje szerint történik: a lefutott mérföldkövek szakasza nem írható át, bővítés a szakasz végére kerül.*
