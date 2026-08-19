---
id: PKG-15-1
type: package
part_of: II-15
lang: hu
pair: PKG-15-1-rulebook_en.md
pair_status: in-sync
doc_version: "1.3"
status: jovahagyva
builds_on: [II-14, II-13, II-12, II-11, I-06]
imports: nulla
---

# PKG-15-1 — A negyedik fok szabálykönyve (levezetés-csomag)

**Számolást nem tartalmaz** — ez a csomag a szabályokat rögzíti, mielőtt bármi kiszámolódna, hogy utólagos szabálymódosítás ne legyen lehetséges.

---

## 1. Kérdés (egy mondat, előre rögzítve)

Folytatódik-e a lépcső: azonos helyenkénti szerződésszám (nyolc) mellett van-e olyan felső sűrűségsáv, ahol a négykiterjedésű szövés egyszerre veri a teret, a síkot és a vonalat — és alatta rendre olyan sávok, ahol a tér, majd a sík teszi ugyanezt?

## 2. Bemenetek

- **[II/12 versenyszabály-konvenció](../II-12-network-race/proof_hu.md):** rögzített szerződés-költségvetést kötelező elhelyezni; az egyensúly a legkisebb összköltségű elrendezés.
- **[III/1, 5. (helyek egyenrangúsága)](../../III-frontier/III-01-candidate-laws_hu.md):** szövés-építéssel megvalósítva, mint a II/13–II/14-ben.
- **[I/6, a kizárás tétele](../../I-language/I-06-identity_hu.md):** az ütem-létra alulról, ütemenként egy példánnyal töltendő.
- **II/12 nyom-döntetlen tétele:** teljes töltésnél minden háló ára a költségvetés kétszerese.
- **[II/11 visszarakó és golyónövekedés](../II-11-locality-readout/proof_hu.md):** a győztes kiolvasásához.
- **[II/13](../II-13-dimension-race/proof_hu.md) összeesési tanulsága:** a jelöltek különbözőségét ellenőrizni kell, nem feltételezni — itt elvből bizonyítjuk (5. pont).
- **[II/14](../II-14-dimension-staircase/proof_hu.md) örökségei:** a körbeérés-korlát **gráf-lépésben újrafogalmazva** (a tér-jelölt átlós lépése miatt a nyers oldalhossz nem elég); a két jegyzőkönyv-tanulság — előjeles ugrás és sáv-őrszem — a [PKG-14-5](../II-14-dimension-staircase/PKG-14-5-readout-repeat_hu.md)-ben bevizsgált alakban; a 12-es körbeérés elégségessége hatos koordináción a PKG-14-5 által **tétel**, nyolcas koordináción **támpont, nem garancia** — ezért marad kötelező az őrszem.
- **[III/2, 8. javított golyótörvényei](../../III-frontier/III-02-open-questions_hu.md):** a negyedik hivatkozási sor levezetett héja köbös: (8/3)·r·(r² + 2).

## 3. A rögzített rendszer

- **20736 hely**; simasági szerződések, egységnyi erővel.
- **Helyenként pontosan 8 szerződés** — a teljes költségvetés 82944 szerződés, minden jelöltnél azonosan.
- Minden jelölt **szövés-háló** (a helyek egyenrangúsága építési elv); minden körbezárt irány körbeérése **páros és legalább 8 lépés** — a páros körbeérés a páros jegyet védi a körbezáráson, és a körbeérést minden indulón **gépi bejárás igazolja**, nem kézi levezetés.
- Költség N példánynál: a háló ütem-létrájának alulról töltése, N = 1-től 20736-ig végigpásztázva.
- A természetes kisebb méret (4096, benne 8⁴) kimondva kizárt: a honos páros jelöltet pontosan arra a 8-as körbeérési padlóra tenné, ahol a II/14 kiolvasása páros győztesen részlegesen megbukott.

## 4. A mezőny

| Jelölt | Szövés | Bekötés | Körbeérés |
|---|---|---|---|
| **J1 — vonal** | 20736-os kör | ±1, ±2, ±3, ±4 lépés | 5184 |
| **J2 — sík** | 144×144 király-szövés (négyzetrács + mindkét átló) | ±(1,0), ±(0,1), ±(1,1), ±(1,−1) | 144 |
| **J3 — tér** | 24×24×36 BCC-szövés, a saját bázisában építve | ±(1,0,0), ±(0,1,0), ±(0,0,1), ±(1,−1,−1) | 24 |
| **J4 — négykiterjedés** | 12×12×12×12 hiperkocka-rács | ±(1,0,0,0), ±(0,1,0,0), ±(0,0,1,0), ±(0,0,0,1) | 12 |

A honos fok eltolódása kimondva: nyolcas koordináción a csupasz egységlépéses bekötés a négykiterjedésé (8 = 2·4), ahogy hatoson a téré volt (6 = 2·3); az alsó fokok a többletet a maguk módján költik el (a vonal vastagszik, a sík átlósodik, a tér testátló-lépésre vált). A J3 valós mért szerkezet (térközepes rács — többek közt a vas); a [C függelékbe](../../appendix/C-benchmarks_hu.md) hivatkozásként felvehető.

**Rögzített változat-lista (kötelező kontroll):** K1 — tér másik alakban, 16×36×36; K2 — tér nyújtva, 12×36×48; K3 — négykiterjedés nyújtva, 8×8×18×18; K4 — sík nyújtva, 48×432. Kontroll versenyez és a teljes-mezőny olvasatban jelentendő; kiolvasást elvből nem kap. A K3 két iránya a 8-as padlón áll — a versenyre érvényes adat.

**Becsületességi pásztázás (kötelező, kimondott korláttal):** a vonal-család (a, b, c, d) négyes-bekötései az 1 ≤ a < b < c < d ≤ 12 tartományban mind kiszámolandók és indulnak — 495 tag. A d > 12 tagok nem pásztázottak; ez a próba kimondott határa, szándékosan a II/14 plafonjával azonos, hogy a két próba család-lelete összevethető legyen.

## 5. Levezetett előzetes tények

**Golyótörvények (a kiolvasás hivatkozási sorai).** Nyolcas koordináción minden golyó 8-cal indul; a megkülönböztető jegy a növekmény **rendje** (kiterjedésszám mínusz egy); az együtthatók a konkrét bekötés tulajdonai:

| Jelölt | Héj-növekmény | Rend | A golyó sora |
|---|---|---|---|
| vonal | 8 | állandó | 1, 9, 17, 25, 33, 41 |
| sík | 8r | lineáris | 1, 9, 25, 49, 81, 121 |
| tér | 6r² + 2 | négyzetes | 1, 9, 35, 91, 189, 341 |
| négykiterjedés | (8/3)·r·(r² + 2) | köbös | 1, 9, 41, 129, 321, 681 |

A sorok r = 2-től válnak szét (héjak: 8 / 16 / 26 / 32); az ítélethez r ≤ 3 elegendő és kötelező határ, jelentés r ≤ 5-ig (8. pont).

**Különbözőség (a II/13 összeesési csapdája elvből zárva).** Három létra-jegy — mindhárom a létra hatványösszege, tehát létra-tulajdon —, gépi leszámlálással megerősítve; mivel a legrövidebb körbeérés 12 lépés, a legfeljebb 4 lépéses zárt sétákba a körbezárás nem szól bele, a végtelen szövés egzakt értékei érvényesek:

| Jelölt | Páros-jegy | Hármas-séták (helyenként) | Négyes-séták (helyenként) |
|---|---|---|---|
| J1 | nincs | 36 | 296 |
| J2 | nincs | 48 | 1188 |
| J3 | van | 0 | 216 |
| J4 | van | 0 | 168 |

A hat pár szétválasztása: a keresztpárokat a páros-jegy, a J1–J2 párt a hármas-séták (36 ≠ 48), a J3–J4 párt a négyes-séták (216 ≠ 168) döntik. A jegyek gépi visszaigazolása a kiszámolt létrákon a PKG-15-2 kötelező önellenőrzése.

**Szétesés-tábla (a II/14 szabálykönyv-tévedésének helyén a helyes állítás).** Egy családtag akkor összefüggő, ha lépéseinek és a helyszámnak nincs közös osztója; 20736 = 2⁸·3⁴ miatt csak a 2 és a 3 játszik: **479 tag ép; 15 csupa-páros tag két példányra esik; a (3, 6, 9, 12) három példányra** (az (1, 2, 3, 4) három másolata). A nulla-módusok száma a példányszám. A levezetés a II/14-en visszapróbálva: ott pontosan a talált 20 széteső tagot adja (19 két- és egy négypéldányos).

## 6. Előre regisztrált, tételekből következő tények — és a regisztrált kérdések

1. N = 1-nél minden ép induló 0-t fizet.
2. N = 2-nél 16-os holtverseny nullán (a széteső tagok); N = 3-nál a hárompéldányos tag egyedül áll nullán.
3. N = 20736-nál kötelező döntetlen **165888**-on (nyom-döntetlen tétel).

**Jóslat a köztes tartományra tudatosan nincs.** Három várakozás rögzül, kérdésként: **(K-a)** héj-illeszkedés — a győzelmek a győztes fokhatárain sűrűsödnek-e ([III/1, 6.](../../III-frontier/III-01-candidate-laws_hu.md)); **(K-b)** tükör-kérdés — a J3–J4 határon, ahol a tükör-jegy mindkét oldalon ott van, a létra szélessége/alakja dönt-e — ez a [III/1, 7.](../../III-frontier/III-01-candidate-laws_hu.md) első éles próbája; **(K-c)** fésű-minta — az alsó tartomány vonal/széteső váltakozása követi-e a II/14 maradékosztály-mintáját.

## 7. Ítélet-szabály (rögzítve)

- Minden N-re a szigorúan legkisebb költségű induló nyer; az azonosság-tűrés a létra-egyezési skálából származtatott, a PKG-15-2-ben számmal rögzítendő küszöb; holtverseny holtversenyként jelentendő.
- **A fő kérdés a J1–J4 négyesen dől — háromfokú lépcső-ítélet:** a próba akkor mond **teljes igent**, ha létezik három összefüggő, érdemi sáv növekvő sűrűséggel úgy, hogy az elsőn a J2, a másodikon a J3, a harmadikon a J4 egyszerre veri a másik hármat. **Kiemelt részleges eset, néven nevezve: „a lépcső megáll a háromnál"** — van sík- és tér-sáv, de négykiterjedés-sáv nincs; ez nem kudarc, hanem a „három mint plafon" olvasat, és így jelentendő. Egyéb részleges kimenet a meglévő sávok megnevezésével; **nem**, ha a sávszerkezet nem áll össze; foltos kimenet foltokkal együtt rögzítendő.
- A pásztázók és a kontrollok győzelmei a teljes-mezőny olvasatban jelentendők (mint a II/13–II/14-ben).
- Utólag új jelölt, új töltésszűrés vagy új költségdefiníció nem vezethető be; bővítés csak új csomagban, e csomag módosítása nélkül.

## 8. A kiolvasási jegyzőkönyv (a PKG-15-4 számára rögzítve)

- A kiolvasás a **legmagasabb álló fok** győztesén fut (teljes igen esetén a négykiterjedés-sáv, „megáll a háromnál" esetén a tér-sáv nyertesén), a nyerő sáv egy **zárt fokú** töltésén; ha minden nyerő töltés elfajult, a nulla-költségű altér egyenletes keveréke számolandó, egzakt vetítővel (II/11 kontroll-módszere). Kontroll kiolvasást nem kap.
- A visszarakó csak a páronkénti **előjeles** közelséget kapja a kész állapotból; a szomszédszámot nem — az ugrás jelöli ki.
- **Előjeles ugrás-szabály (a PKG-14-5-ben bevizsgált alak):** az ugrás az előjeles listán keresendő, rögzített 30-as keresési ablakban; az átellenes osztály előjelével együtt külön jelentendő.
- **Sáv-őrszem:** a leggyengébb elfogadott és a legerősebb elutasított közelség (nagyság szerinti) hányadosa, a legrosszabb helyi érték jelentendő; **kettes tényező alatt az olvasat részleges**. Viszonyítás: a PKG-14-5 tiszta esete 2,84-et, a II/14 bukott esete 1,0-t ad.
- Páros győztesen az átellenes-osztály korrelációja mindig külön sor, akkor is, ha az őrszem nem jelez.
- **Teljesség-számla:** megtalált / hiányzó / fantom, mindhárom számmal, a 82944 szerződésre.
- **Golyó-olvasat:** ítélet r ≤ 3-ig az 5. pont négy hivatkozási sora ellen; jelentés r ≤ 5-ig ott, ahol 2r < körbeérés — a J4-en az r = 5 éppen érvényes.
- **Bukás-ág, előre:** ha az őrszem jelez, az ítélet részleges, a mechanizmus megnevezésével; a nagyobb szövésen való ismétlés nem e csomag dolga, hanem előre megnevezett folytatásé (a PKG-15-5 név erre foglalva).

## 9. Import-számla

Új import: **nulla.** Örökölt, deklarált konvenciók: versenyszabály, helyek egyenrangúsága, szövés-építés (II/12–II/13), őrszem-küszöb (kettes tényező — PKG-14-5). Levezetett kombinatorikai tények: a golyótörvények, a séta-számok, a szétesés-tábla. Kimondott, rögzített határok: a 12-es lépés-plafon, a páros ≥ 8 körbeérés, a 20736-os méret, a 30-as keresési ablak, az r ≤ 3 / r ≤ 5 golyóhatárok, és a kétutas mintavétel (A8).

## 10. Ítélet erről a csomagról

**Áll.** A szabálykönyv zárt; érdemi előzetes eredményei: a jelölt-különbözőség három-jegyes, elvi bizonyítása (az összeesési csapda nem méret-szerencsén múlik); a honos-fok eltolódás kimondása; és a negyedik hivatkozási sorral kiegészített, rendre épülő golyó-jegyzőkönyv.

## 11. Kimenő állítások (a PKG-15-2 csak ezekre építhet)

- **A1:** rendszer = 20736 hely, 82944 egységnyi simasági szerződés, helyenként 8, szövés-építéssel; minden körbeérés páros és ≥ 8 lépés, gépi bejárással igazolva.
- **A2:** mezőny = J1–J4 (4. pont táblája), K1–K4 kontrollok, és a vonal-család pásztázása d ≤ 12-ig (495 tag, szétesőkkel együtt).
- **A3:** költség = ütem-létra alulról töltése, N = 1..20736.
- **A4:** előre regisztrált tények: N = 1 ép indulók 0-n; N = 2 16-os holtverseny; N = 3 a hárompéldányos egyedül; N = 20736 döntetlen 165888-on.
- **A5:** ítélet-szabály a 7. pont szerint — háromfokú lépcső-definíció, néven nevezett „megáll a háromnál" részleges esettel; jóslat nincs, három regisztrált kérdéssel (K-a, K-b, K-c).
- **A6:** kiolvasási jegyzőkönyv a 8. pont szerint — előjeles ugrás, sáv-őrszem (küszöb 2), golyó-ítélet r ≤ 3, jelentés r ≤ 5.
- **A7:** kötelező önellenőrzések: (i) a három különbözőség-jegy visszaigazolása a négy fő jelölt létráján; (ii) létra-osztályozás a teljes mezőnyön rögzített tűréssel; (iii) gépi körbeérés-bejárás minden indulón; (iv) nyomösszeg 165888 mindenütt; (v) komponensszám-ellenőrzés a szétesés-tábla ellen.
- **A8:** kétutas szabály rögzített mintavétellel: a fő jelöltek és a kontrollok mindkét úton (zárt Fourier-alak és gépi sajátfeladat) teljesen; a családból 24 sorsolt tag gépi keresztellenőrzése, a sorsolási mag rögzített száma: 20736.
