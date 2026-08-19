---
id: II-17-handover
type: note
part_of: II-17
lang: hu
pair: HANDOVER_en.md
pair_status: missing
doc_version: "1.0"
status: ervenyes
builds_on: [PKG-17-1]
imports: "nincs"
---

# II/17 — Átadó jegyzet (hol tartunk, mi jön)

**Ez a fájl azért van, hogy a repó dumpja önmagában elég legyen a folytatáshoz.** Aki innen veszi fel a fonalat — ember vagy gép —, ebből tudja meg, miért létezik a II/17, mi van már lezárva, és mi a következő lépés.

## 1. Miért létezik ez a fejezet

A II/12–II/16 három próbán át ugyanazt a leletet adta: **kézzel felsorolt hálók közt a kiválasztás nem dőlhet el**, mert a hangolt vonal-családtagok mindent imitálnak. A II/16 ezt lezárta: a lépcső tetejét a koordinációszám dönti el, azt pedig kézzel adjuk meg. Ebből következik, hogy a **hármas kiterjedés a nyelvben ma egyetlen helyen él: a vonzás 1/r alakjában**, amit a II/4 importként kap.

A visszakövetés a szerkezeti gyökérig: a nyelv szabályozza, hogy **az állapotot ki birtokolja** (2. törvény), de nem szabályozza, hogy **a szerződést ki birtokolja**. Ami szabályozatlan, az a modellezőre marad — ezért adjuk kézzel a hálót. A II/17 ezt a lyukat célozza. Ha a szerződés a példányok állapotából születik, akkor a háló kimenetté válik, és az 1/r alakja szerkezetileg nem lehet import.

Az összeomlási tétel szökési útja — az **üres hely** (szerződés példány nélkül) — ugyanennek a hiánynak a nyoma: ilyen csak akkor lehet, ha a szerződést nem példány hordozza.

## 2. Mi van lezárva

**`PKG-17-1-rulebook_hu.md` — fagyasztva (`jovahagyva`), nem módosítható.** Tartalma: a lemma, a rendszer (12 objektum, mind a 66 pár, változó tartalmú kötés-szerződés), a hurok, a generáló szabály hat tagja, két normálás, négy induló, 200 kör, mag 1166, négy ítélet-osztály, a kiolvasási kapu, az import-számla.

**`PKG-17-2-verify.py` — a B3-előfeltétel, lefutott, a kapu tiszta.** Amit visszaad: kötésár egzaktul 45/66, elfajulás 132, közelség-szórás 1,5·10⁻¹⁶; kör kötésára 0,30105, közelségei 0,4438 / 0,1231 / 0,0656 / 0,0448 / 0,0366; ráadásul a II/1 zárt alakja és a II/5 három száma (3/2, négyszeres elfajulás, 15/8). A nulla-próba mind a hat családtagon a várt eredményt adja.

**Amit a hitelesítés hozott, még fagyasztás előtt:** az F5 (küszöbös) családtag a lapos indulóból egyetlen körben nullára visz minden tartalmat. Ebből lett a negyedik ítélet-osztály (**ÜRES**) és a T1 kivétele. Az F5 azért marad a családban, mert ez a híd az üres szerződés ára felé.

## 3. Amit a hitelesítés menet közben rögzített (nem kell újra levezetni)

A kötés-szerződés zárt alakja két úton felépítve egyezik: a négy súly alakjából (`a² + d² + ½(b+c)²`) és operátor-alakban is. Az alapállapot magnesezettség-blokkokban számolható, az elfajult eset egzakt vetítővel — ez a II/11 kontroll-módszere. A közelség-mérőszám természetes alapú (a II/11 0,69 jegye = ln 2).

## 4. A következő lépés

**`PKG-17-2-loop.py`** — a hurok maga. 48 futás (6 családtag × 2 normálás × 4 induló), 200 kör, percek. A hitelesítőben már készen áll minden alkatrész, amit használni fog.

Sorrend a szabálykönyv szerint: B3-előfeltétel → nulla-próba → elfajulás-kezelő naplózással → 48 futás → besorolás. **A kiolvasás kapuja: kizárólag KÖZTES ítélet esetén.**

## 5. Az elágazás (előre rögzítve, nem az eredmény után választandó)

| Ítélet | Mit jelent | Folytatás |
|---|---|---|
| **KÖZTES** | a lemma áll | PKG-17-3: kiolvasás; utána nagyobb rendszer, mert 12 objektumon kiterjedésszám nem mondható ki |
| **PÁR** | a kötés-szerződés rossz hordozó | ugyanez a hurok a **simasági szerződéssel**, helyeken — ágváltás, nem kudarc |
| **LAPOS** | a közelség nem az a kivonat, amiből szerkezet születhet | új kérdés: van-e más állapot-kivonat, ami szimmetriát tud törni |
| **ÜRES** | a generálás elviszi a hálót | az ár kérdése előre hozandó (PKG-17-4) |

## 6. Függő nyelv-módosítások

**Mehet bármikor** (a mai állapotot rögzíti, nem eredményt állít):

1. `I-01-concept_hu.md` — az import-számla kettébontása: *helyiség* (fél tétel, marad) és *a szerződésháló eredete* (új, teljesen nyitott sor).
2. Hiányzó `imports:` sorok a hálót kapó fejezetek fejlécébe: II/3, II/4, II/6, II/9, II/10 → szomszédság; II/12–II/16 → felsorolt mezőny és kötelező költségvetés.

**Vár a hurok eredményére** (mert a megoldásról állít valamit):

3. `I-04-ownership-view_hu.md` — a szerződés birtoklása ma szabályozatlan.
4. `I-08-contract-store_hu.md` — új sor: üres szerződés, *jelölt, ára levezetetlen*.
5. `III-01-candidate-laws_hu.md` — új 9. jelölt két lábbal: (a) a szerződés kötelező minden pár közt, levezetési jelölt az 5. törvényből; (b) az üres szerződés nem ingyenes, levezetési jelölt az 1. törvényből. Bukási feltétel vele együtt: ha a kijövő koordinációszám az üres-ár alakjára érzékeny, a jelölt megbukott.
6. `III-02-open-questions_hu.md` — a 2., a 7. és a 8. sűrűség-fele egy programmá vonva; a mérőszáma: *van-e olyan fejezet, amelynek a bemenetei közt nem szerepel háló*.
7. `I-10-dictionary_hu.md` — az üres szerződés sora; a jobb oldal **üresen hagyandó**, mert a fizikának erre nincs bevett szava.

**Amihez nem szabad nyúlni:** az I/9 törvénytáblája. Nincs hatodik törvény, amíg a próba le nem futott.

## 7. Egy elvi döntés, ami már megszületett

Verziószám (**„leíró nyelv 2.0"**) nem lesz. Az elévülés nem a fejezeteket éri, hanem a bemeneteiket, és erre a fejlécek `imports:` mezője a nyilvántartás. A verzió így nem dátum, hanem lekérdezés: **azok a fejezetek, amelyeknél az import-lista üres.** Ma három ilyen van (II/1, II/2, II/5) — a II/8 vizsgálandó, mert az már ma is minden pár közt ható, távolsággal csökkenő szerződéssel dolgozik, vagyis lehet, hogy eleve ide tartozik.

## 8. Kockázat, amit a következő ülés elején érdemes szem előtt tartani

A **II/3, II/4, II/6, II/9, II/10** öt fejezete arra épül, hogy a keverés csak szomszédok közt folyik. Kötelező szerződés mellett ez csak akkor marad igaz, ha a generált tartalmak a távolsággal csökkennek. **Az első kötelezettség tehát nem a geometria előállítása, hanem a csökkenés visszaadása** — enélkül nincs mit tovább vizsgálni.
