---
id: PKG-13-1
type: package
part_of: II-13
lang: hu
pair: PKG-13-1-rulebook_en.md
pair_status: missing
doc_version: "1.3"
status: jovahagyva
builds_on: [II-12, II-11, I-06]
imports: nulla
---

# PKG-13-1 — A kiterjedés-verseny szabálykönyve (levezetés-csomag)

**Számolást nem tartalmaz** — ez a csomag a szabályokat rögzíti, mielőtt bármi kiszámolódna, hogy utólagos szabálymódosítás ne legyen lehetséges.

---

## 1. Kérdés (egy mondat, előre rögzítve)

Azonos helyenkénti szerződésszám mellett kedveli-e a költségszerkezet a magasabb kiterjedésű szövést — vagy a vonalat, vagy a darabolást?

## 2. Bemenetek

- **[II/12 versenyszabály-konvenció](../II-12-network-race/proof_hu.md):** rögzített szerződés-költségvetést kötelező elhelyezni; az egyensúly a legkisebb összköltségű elrendezés.
- **[III/1, 5. (helyek egyenrangúsága)](../../III-frontier/III-01-candidate-laws_hu.md):** nincs kitüntetett hely — e nélkül a II/12 összeomlási tétele érvényes, a verseny értelmetlen.
- **[I/6, a kizárás tétele](../../I-language/I-06-identity_hu.md):** az ütem-létrát alulról, ütemenként egy példánnyal kell tölteni.
- **II/12 nyom-döntetlen tétele:** teljes töltésnél minden háló ára a költségvetés kétszerese.
- **[II/11 visszarakó és golyónövekedés](../../II-11-locality-readout/proof_hu.md):** a győztes kiolvasásához.
- **II/12 gépezet:** hálózati ütem-létra sajátfeladatként ([B függelék](../../../appendix/B-machinery_hu.md)).

## 3. A rögzített rendszer

- **16 hely**; simasági szerződések, egységnyi erővel.
- **Helyenként pontosan 4 szerződés** — a teljes költségvetés így 32 szerződés, minden jelöltnél azonosan.
- A helyek egyenrangúsága nem utólagos ellenőrzés, hanem építési elv: minden jelölt **szövés-háló** — egy csoportszerkezet minden helyre ugyanazt a bekötési mintát írja elő, így a háló garantáltan minden helyről ugyanúgy néz ki.
- Költség $N$ példánynál: a háló ütem-létrájának alulról töltése, $N = 1$-től 16-ig végigpásztázva.

## 4. A jelöltek

| Jelölt | Szövés | Szerkezet |
|---|---|---|
| **J1 — vonal** | 16-os kör, első- és másodszomszéd szerződésekkel | vastagított vonal |
| **J2 — sík** | 4×4-es körbezárt rács (tórusz) | valódi kétkiterjedésű szövés |
| **J3 — darabolt** | két különálló, vastagított 8-as kör | a J1 kettétörve |

**Becsületességi pásztázás (kötelező):** a vonal-család összes 4 szerződés/helyes változata (a 16-os kör minden kétlépcsős bekötése) is kiszámolandó, hogy a családból ne maradjon ki a deklaráltnál jobb jelölt.

## 5. Levezetett lemma — a jelölt-készlet összeesése

A tervezett negyedik jelölt a négykiterjedésű szövés volt (2×2×2×2 hiperkocka: helyenként négy szerződés, mind más irányba). A rögzítés közben derült ki, hogy **16 helyen ez ugyanaz a háló, mint a J2 tórusz**. A levezetés két lépés: egy kétkiterjedésű, 2 oldalhosszú szövés pontosan egy 4-es kör; a szövések iránypáronként összerakhatók — így a 2×2×2×2 négykiterjedésű szövés azonos a (4-es kör) × (4-es kör) összerakással, ami a 4×4-es tórusz.

**Következmény, kimondva:** ezen a méreten a kettő és a négy kiterjedés meg sem különböztethető — a verseny a *vonal kontra nem-vonal kontra darabolt* kérdést dönti el; a kettő-vagy-négy kérdéshez nagyobb rendszer kell (rögzített bővítési irány, nem e próba tárgya).

## 6. Előre regisztrált, tételekből következő tények (nem jóslatok)

1. $N = 1$-nél minden jelölt 0-t fizet (minden hálónak van egy közös nulla-módusa).
2. $N = 2$-nél a J3 nyer: két komponense két nulla-módust ad, az összefüggő jelöltek már fizetnek.
3. $N = 16$-nál kötelező döntetlen 64-en (nyom-döntetlen tétel).

**Jóslat a $3 \le N \le 15$ érdemi tartományra: tudatosan nincs** — a II/12 tanulsága után ez a próba nyitott kimenetelű.

## 7. Ítélet-szabály (rögzítve)

- Minden $N$-re a szigorúan legkisebb költségű jelölt nyer; a holtverseny holtversenyként jelentendő.
- **A fő kérdés eldöntése:** a próba akkor mond igent a kiterjedésre, ha a J2 a $3 \le N \le 15$ tartomány összefüggő, érdemi részén egyszerre veri a J1-et és a J3-at; akkor mond nemet, ha ilyen tartomány nincs. Részleges kimenet (foltokban nyer) részleges eredményként rögzítendő, a foltok helyével együtt.
- Utólag új jelölt, új töltésszűrés vagy új költségdefiníció nem vezethető be; bővítés csak új csomagban, e csomag módosítása nélkül.

## 8. A kiolvasási jegyzőkönyv (a PKG-13-4 számára rögzítve)

- A győztesen a II/11 visszarakója fut: páros közelség a kész állapotból; a szomszédszámot nem kapja meg — a közelség-lista ugrása jelöli ki.
- Zárt fokú töltés választandó (egyértelmű állapot); ha a győztes minden nyerő töltése elfajult, a nulla-költségű altér egyenletes keveréke számolandó, egzakt vetítővel (II/11 kontroll-módszere).
- Kiterjedés-olvasat a golyónövekedésből: a vonal lépésenként $+2$-t ad; a tórusz-szövés jegyzett sora 1, 5, 11, 15, 16. A kettő-vagy-négy olvasat e méreten eldönthetetlen (5. pont) — a jegyzőkönyv ezt nem is állíthatja.

## 9. Import-számla

Új import: **nulla.** A versenyszabály és a helyek egyenrangúsága a II/12-ből örökölt, deklarált konvenciók; a szövés-építés az egyenrangúság megvalósítása, nem új feltevés; a jelölt-választást a kötelező pásztázás védi a szemezgetés vádjától.

## 10. Ítélet erről a csomagról

**Áll.** A szabálykönyv zárt; egy érdemi levezetett eredménye van (a jelölt-összeesési lemma, 5. pont), amely a kérdést élesítette: 16 helyen a verseny a vonal–sík–darabolt hármasról szól.

## 11. Kimenő állítások (a PKG-13-2 csak ezekre építhet)

- **A1:** rendszer = 16 hely, 32 egységnyi simasági szerződés, helyenként 4, szövés-építéssel.
- **A2:** jelöltek = J1 (vonal), J2 (tórusz ≡ hiperkocka), J3 (két darab), plusz a vonal-család kötelező pásztázása.
- **A3:** költség = ütem-létra alulról töltése, $N = 1..16$.
- **A4:** előre regisztrált tények: $N=1$ mind 0; $N=2$ J3 nyer; $N=16$ döntetlen 64-en.
- **A5:** ítélet-szabály a 7. pont szerint; jóslat nincs.
- **A6:** kiolvasási jegyzőkönyv a 8. pont szerint; a kettő-vagy-négy kérdés e méreten nem eldönthető és nem is állítható.