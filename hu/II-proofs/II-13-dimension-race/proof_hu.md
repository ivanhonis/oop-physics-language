---
id: II-13
type: proof
lang: hu
pair: proof_en.md
pair_status: missing
doc_version: "1.3"
status: reszleges
builds_on: [II-11, II-12, I-06]
imports: "nulla új tétel (a versenyszabály és a helyek egyenrangúsága a II/12-ből örökölt, deklarált konvenciók)"
packages: [PKG-13-1, PKG-13-2, PKG-13-3, PKG-13-4]
---

# II/13. A kiterjedés-verseny — részleges igen

**A kérdés.** A [III/2, 8.](../../III-frontier/III-02-open-questions_hu.md) célpróbája: azonos helyenkénti szerződésszám mellett kedveli-e a költségszerkezet a magasabb kiterjedésű szövést — vagy a vonalat, vagy a darabolást? A [II/12](../II-12-network-race/proof_hu.md) tanulsága után jóslat tudatosan nem volt. A próba a csomag-módszerrel készült ([D függelék](../../appendix/D-package-method_hu.md)): a szabálykönyv — jelöltek, ítélet-szabály, kiolvasási jegyzőkönyv — minden számolás előtt rögzült ([PKG-13-1](PKG-13-1-rulebook_hu.md)).

**A rendszer és a szerződés.** Tizenhat hely; 32 egységnyi simasági szerződés, helyenként pontosan négy. A helyek egyenrangúsága itt építési elv: minden jelölt **szövés-háló** — egy csoportszerkezet minden helyre ugyanazt a bekötési mintát írja elő, így a háló garantáltan minden helyről ugyanúgy néz ki. Jelöltek: **vonal** (16-os kör első- és másodszomszéd szerződésekkel), **sík** (4×4 körbezárt rács), **darabolt** (két vastagított 8-as kör); kötelező pásztázás: a vonal-család mind a 21 bekötése.

**Összeesési lemma.** A tervezett negyedik jelöltről — a 2×2×2×2 négykiterjedésű szövésről — a rögzítés közben derült ki, hogy 16 helyen **ugyanaz a háló, mint a sík**: a 2 oldalhosszú kétkiterjedésű szövés maga a 4-es kör, és a szövések iránypáronként összerakhatók. Következmény, előre kimondva: e méreten a kettő-vagy-négy kiterjedés kérdése fel sem tehető — a verseny a vonal–sík–darabolt hármasról szól. (Spektrális megerősítés: a sík létrája pontosan a hiperkocka 1-4-6-4-1 szélességű binomiális létrája, gépi pontossággal — [PKG-13-2](PKG-13-2-ladders_hu.md).)

**A számolás.** Minden létra két független úton (a gépezet sajátfeladata és a szövések zárt képlete; a darabolt ráadásul két felépítésben), egyezés $10^{-15}$-ön belül; a nyomösszeg mind a huszonnégy hálón pontosan 64 — a nyom-döntetlen fedezete. A pásztázás fogása: a családban **két** darabolt szövés él, különböző létrával — a második új jelöltként lépett be; a 21 tag 7 létra-osztályba esik ([PKG-13-2](PKG-13-2-ladders_hu.md)). A verseny: alulról töltés $N = 1$-től 16-ig; a kiolvasás a rögzített jegyzőkönyvvel a győztesen ([PKG-13-3](PKG-13-3-race_hu.md), [PKG-13-4](PKG-13-4-readout_hu.md)).

**Az eredmény — a verseny.**

| N példány | 1 | 2 | 3–5 | 6–8 | 9–10 | 11 | 12–13 | 14 | 15 | 16 |
|---|---|---|---|---|---|---|---|---|---|---|
| győztes | mind | daraboltak | **vonal** | **darabolt** | kereszt-vonalak | **sík** | kereszt-vonalak | 2. darabolt | holtverseny (56) | mind (64) |

Két olvasat, mindkettő a rögzített szabály szerint. *Fő olvasat:* a sík az összefüggő **10–15** tartományon egyszerre veri a vonalat és a daraboltat — **a próba részleges igent mond: magas sűrűségen a kiterjedés megtérül.** *Teljes mezőny:* a verseny rezsimekre esik, és a sík egyetlen szigorú győzelme **N = 11** — pontosan a saját zárt foka (fokhatárai 1, 5, 11, 15). Két levezetett kísérőjelenség: a **héj-logika** — a győztes ott nyer, ahol a saját létrájának egy foka éppen betelik (a darabolt fokhatárai 2, 6, 8 — győzelmi sávja 6–8; jelölt szabályként rögzítve: [III/1, 6.](../../III-frontier/III-01-candidate-laws_hu.md)); és a **tükör-hatás** — majdnem-teli töltésnél a költség 64 mínusz a betöltetlen felső ütemek, ezért ott az nyer, aki a költségét kevés magas ütembe tömöríti. A kiterjedés eszerint **sűrűségfüggő egyensúlyi tulajdonság**: a háló+töltés párosé, nem a hálóé.

**Az eredmény — a kiolvasás.** A győztesen (sík, $N = 11$) a visszarakó mind a 32 valódi szerződést megtalálta, hiányzó nélkül — de a kis szövés a saját körbeérését is „hallja": 8 fantom-él íródott melléjük (mind átellenes-átló), a valódiakkal egzaktul azonos közelséggel; a mért golyó ezért nem a jegyzett tórusz-sor. **A hurok-zárás e méreten részlegesen bukott** — nem rombolón: hamis geometria nem került a valódi helyébe, csak visszhang a valódi fölé. A diagnózis (a rögzített hatókörön kívül, jelöltként): 8×8-as szövésen a rezonancia eltűnik (a szomszéd-közelség kétszeresen domináns), a visszarakás 128/128 fantom nélkül, és a golyónövekmény 4, 8, 12 — **lépésenként $+4r$: a két kiterjedés mért növekedési törvénye** (a vonal állandó $+2$-jével szemben). A 16-helyes rezonancia méret-műtermék ([PKG-13-4](PKG-13-4-readout_hu.md)).

**Ellenőrzés a valóságon.** Ez a próba — a II/12-höz hasonlóan — belső verseny, közvetlen mért célpont nélkül; két mért visszhangja van: a fokbetelés-vezérelt győzelem a [II/7](../II-07-bowl-magic-numbers/proof_hu.md) mért bűvösszám-mechanizmusának háló-szintű mása, és a sűrűség-vezérelt szerkezetváltás a fizika standard mért jelensége (anyagok nyomás alatt rácsot váltanak) — itt a legkisebb, egzakt alakban.

**Import-számla:** nulla új tétel — a versenyszabály és a helyek egyenrangúsága a II/12-ből örökölt, deklarált konvenciók; a jelölt-választást a kötelező pásztázás védte, és a pásztázás kétszer fogott (második darabolt szövés; kereszt-vonal győzelmek). **Mit igazolt:** részleges igen a kiterjedésre (10–15); a kiterjedés sűrűségfüggő; a héj-illeszkedés jelölt szabály ([III/1, 6.](../../III-frontier/III-01-candidate-laws_hu.md)); az összeesési lemma tétel; a kiolvasás korlátja kis méreten azonosított okkal, a méret-diagnózis jelöltként. Bővítési irány: a verseny és a kiolvasás nagyobb, a kettő és négy kiterjedést szétválasztó rendszeren — és a koordináció-hatos vonal–sík–tér verseny ([III/2, 8.](../../III-frontier/III-02-open-questions_hu.md)).