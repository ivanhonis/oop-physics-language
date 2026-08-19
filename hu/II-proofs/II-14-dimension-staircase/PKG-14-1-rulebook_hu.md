---
id: PKG-14-1
type: package
part_of: II-14
lang: hu
pair: PKG-14-1-rulebook_en.md
pair_status: in-sync
doc_version: "1.4"
status: jovahagyva
builds_on: [II-13, II-12, II-11, I-06]
imports: nulla
---

# PKG-14-1 — A kiterjedés-lépcső szabálykönyve (levezetés-csomag)

**Számolást nem tartalmaz** — ez a csomag a szabályokat rögzíti, mielőtt bármi kiszámolódna, hogy utólagos szabálymódosítás ne legyen lehetséges.

---

## 1. Kérdés (egy mondat, előre rögzítve)

Lépcsőzik-e a kiterjedés a sűrűséggel: azonos helyenkénti szerződésszám (hat) mellett van-e olyan felső sűrűségsáv, ahol a tér-szövés egyszerre veri a síkot és a vonalat — és alatta olyan, ahol a sík veri a másik kettőt?

## 2. Bemenetek

- **[II/12 versenyszabály-konvenció](../II-12-network-race/proof_hu.md):** rögzített szerződés-költségvetést kötelező elhelyezni; az egyensúly a legkisebb összköltségű elrendezés.
- **[III/1, 5. (helyek egyenrangúsága)](../../III-frontier/III-01-candidate-laws_hu.md):** szövés-építéssel megvalósítva, mint a II/13-ban.
- **[I/6, a kizárás tétele](../../I-language/I-06-identity_hu.md):** az ütem-létra alulról, ütemenként egy példánnyal töltendő.
- **II/12 nyom-döntetlen tétele:** teljes töltésnél minden háló ára a költségvetés kétszerese.
- **[II/11 visszarakó és golyónövekedés](../II-11-locality-readout/proof_hu.md):** a győztes kiolvasásához.
- **[II/13](../II-13-dimension-race/proof_hu.md) három öröksége:** az összeesési lemma tanulsága (a jelöltek különbözőségét ellenőrizni kell, nem feltételezni); a körbeérési rezonancia méret-diagnózisa (a 8-as oldalhossz alsó korlát); a héj-logika és a tükör-hatás mint ellenőrzendő megfigyelések.
- **[III/2, 8. javított golyótörvényei](../../III-frontier/III-02-open-questions_hu.md):** a tér héja négyzetes ($4r^2+2$), nem lineáris.

## 3. A rögzített rendszer

- **512 hely**; simasági szerződések, egységnyi erővel.
- **Helyenként pontosan 6 szerződés** — a teljes költségvetés így 1536 szerződés, minden jelöltnél azonosan.
- Minden jelölt **szövés-háló** (a helyek egyenrangúsága építési elv, mint a II/13-ban), és minden körbezárt irány oldalhossza **legalább 8** — a II/13 rezonancia-diagnózisának öröksége.
- Költség $N$ példánynál: a háló ütem-létrájának alulról töltése, $N = 1$-től 512-ig végigpásztázva.

## 4. A jelöltek

| Jelölt | Szövés | Szerkezet |
|---|---|---|
| **J1 — vonal** | 512-es kör, 1-2-3 lépésű bekötéssel | vastagított vonal |
| **J2 — sík** | 16×32-es körbezárt rács, bekötés: ±(1,0), ±(0,1), ±(1,1) | háromszög-szövés (a hatos koordináció síkbeli szövése) |
| **J3 — tér** | 8×8×8-as körbezárt kockarács, bekötés: ±(1,0,0), ±(0,1,0), ±(0,0,1) | valódi háromkiterjedésű szövés |

**Rögzített változat-lista (kötelező kontroll):** a sík nyújtás-érzékenységére a 8×64-es háromszög-szövés is kiszámolandó és a mezőnyben indul.

**Becsületességi pásztázás (kötelező, kimondott korláttal):** a vonal-család $(a, b, c)$ hármas-bekötései a $a < b < c \le 12$ tartományban mind kiszámolandók és a mezőnyben indulnak (a szövések zárt képletével olcsó). A korlát maga is rögzített szabály: a $c > 12$ családtagok nem pásztázottak — ez a próba kimondott határa, nem utólagos döntés.

## 5. Levezetett előzetes tények — különbözőség és golyótörvények

**Különbözőség (a II/13 összeesési lemmájának tanulsága — itt ellenőrzés, nem feltevés).** Előzetes érv, számolással megerősítendő (PKG-14-2): a J1-ben és a J2-ben van hármas kör (a J1-ben az 1+2=3 lépések zárnak hármat, a J2-ben a ±(1,0), ±(0,1), ±(1,1) hármas), a J3 viszont **páros háló** — hármas köre nincs, és a létrája ezért a 6-os fok körül szimmetrikus. A három jelölt tehát páronként különböző; a szimmetria-jegy a PKG-14-2 kötelező önellenőrzése.

**Golyótörvények (levezetett, a kiolvasás hivatkozási sorai).** Hatos koordinációnál minden jelölt golyója 6-tal indul; a megkülönböztető jegy a növekmény **rendje**:

| Jelölt | Növekmény | A golyó sora |
|---|---|---|
| vonal | állandó ($+6$) | 1, 7, 13, 19, 25 |
| sík | lineáris ($6r$) | 1, 7, 19, 37, 61 |
| tér | négyzetes ($4r^2+2$) | 1, 7, 25, 63, 129 |

A sorok $r = 2$-től válnak szét (13 / 19 / 25); az olvasathoz $r \le 3$ elegendő és kötelező is a határa (8. pont).

## 6. Előre regisztrált, tételekből következő tények (nem jóslatok)

1. $N = 1$-nél minden jelölt 0-t fizet (minden hálónak van egy közös nulla-módusa).
2. Minden induló összefüggő, pontosan 1 nulla-módussal — a $N = 2$-es széteső-előny (II/13) itt nem játszik.
3. $N = 512$-nél kötelező döntetlen **3072**-n (nyom-döntetlen tétel: a teljes létra összege a költségvetés kétszerese).

**Jóslat a $2 \le N \le 511$ érdemi tartományra: tudatosan nincs.** Egyetlen várakozás rögzül, kérdésként: ha a héj-illeszkedési jelölt szabály ([III/1, 6.](../../III-frontier/III-01-candidate-laws_hu.md)) általános, a győzelmeknek a győztes saját fokhatárain kell sűrűsödniük — ez ellenőrzendő, nem jósolt.

## 7. Ítélet-szabály (rögzítve)

- Minden $N$-re a szigorúan legkisebb költségű induló nyer; a holtverseny holtversenyként jelentendő.
- **A fő kérdés eldöntése — a lépcső két foka:** a próba akkor mond **igent** a lépcsőre, ha létezik két összefüggő, érdemi sáv úgy, hogy az alacsonyabb sűrűségűn a J2 egyszerre veri a J1-et és a J3-at, a magasabb sűrűségűn pedig a J3 egyszerre veri a J1-et és a J2-t. Ha csak az egyik sáv létezik: **részleges** eredmény, a meglévő sáv megnevezésével. Ha egyik sem: **nem.** Foltos kimenet foltokkal együtt rögzítendő.
- A fő kérdés a deklarált J1–J2–J3 hármason dől el; a pásztázók és a változatok győzelmei a teljes-mezőny olvasatban jelentendők (mint a II/13-ban).
- Utólag új jelölt, új töltésszűrés vagy új költségdefiníció nem vezethető be; bővítés csak új csomagban, e csomag módosítása nélkül.

## 8. A kiolvasási jegyzőkönyv (a PKG-14-4 számára rögzítve)

- A kiolvasás a fő olvasat győztesén fut, a tér-sáv egy **zárt fokú** töltésén (egyértelmű állapot); ha minden nyerő töltés elfajult, a nulla-költségű altér egyenletes keveréke számolandó, egzakt vetítővel (II/11 kontroll-módszere).
- A II/11 visszarakója: páros közelség a kész állapotból; a szomszédszámot nem kapja meg — a közelség-lista ugrása jelöli ki.
- **Kiterjedés-olvasat a golyónövekedésből, az 5. pont három hivatkozási sora ellen, legfeljebb $r = 3$-ig** — a 8-as oldalhosszon a golyó $r = 4$-nél éri el a körbeérés felezőjét, onnan az olvasat elvből érvénytelen.
- **Rezonancia-őrszem (a II/13 tanulsága):** az átellenes eltolás-osztályok korrelációja külön jelentendő; ha bármelyik a szomszéd-osztállyal egzaktul egyezik, az olvasat részlegesnek minősítendő, az egyezés helyével együtt.

## 9. Import-számla

Új import: **nulla.** A versenyszabály, a helyek egyenrangúsága és a szövés-építés a II/12–II/13-ból örökölt, deklarált konvenciók; a golyótörvények levezetett kombinatorikai tények; a pásztázás-korlát ($c \le 12$) és az oldalhossz-korlát (≥ 8) rögzített, kimondott határok.

## 10. Ítélet erről a csomagról

**Áll.** A szabálykönyv zárt; érdemi előzetes eredménye a jelölt-különbözőség páros-jegye (a II/13 összeesési csapdája itt bizonyítottan nem áll fenn) és a javított, rendre épülő golyó-jegyzőkönyv.

## 11. Kimenő állítások (a PKG-14-2 csak ezekre építhet)

- **A1:** rendszer = 512 hely, 1536 egységnyi simasági szerződés, helyenként 6, szövés-építéssel, minden oldalhossz ≥ 8.
- **A2:** mezőny = J1 (vonal), J2 (háromszög-sík, 16×32), J3 (kocka-tér, 8×8×8), a 8×64-es sík-kontroll, és a vonal-család pásztázása $c \le 12$-ig.
- **A3:** költség = ütem-létra alulról töltése, $N = 1..512$.
- **A4:** előre regisztrált tények: $N=1$ mind 0; minden induló 1 nulla-módusú; $N=512$ döntetlen 3072-n.
- **A5:** ítélet-szabály a 7. pont szerint — kétsávos lépcső-definíció; jóslat nincs.
- **A6:** kiolvasási jegyzőkönyv a 8. pont szerint — golyó-olvasat $r \le 3$, rezonancia-őrszemmel.
- **A7:** a PKG-14-2 kötelező önellenőrzése a különbözőség: a J3 létrája a 6 körül szimmetrikus (páros háló), a J1-é és a J2-é nem.
