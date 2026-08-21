---
id: HANDOVER
type: note
lang: hu
pair: HANDOVER_en.md
pair_status: missing
doc_version: "1.4"
status: ervenyes
---

# Átadó jegyzet — 2026-08-20/21

**Ez a fájl azért van, hogy a repó önmagában elég legyen a folytatáshoz.** Aki innen veszi fel a fonalat — ember vagy gép —, ebből tudja meg, mi épült, mi dőlt el, mi bukott meg, mi van eldöntve de még megírva nincs, és mi a következő lépés. Az igazság forrása mindig a hivatkozott fájl; ez navigáció és állapot.

---

## 1. A legfontosabb mondat

> **A kiterjedés-program nem adja ki a hármat.** Ez bizonyítva van, nem sejtve. A „miért három" kérdés ezen a szinten lezárult; a hármat két külön import hozza kívülről (`IMP-02` vonzásalak, `IMP-04` kiterjedésszám). Cserébe lett négy új tétel, egy gépi könyvelő apparátus, és három lefutott vak jóslat.

---

## 2. Ami épült — gépezet

Mind fut, mind zöld, mind egy paranccsal indul.

| Eszköz | Mit csinál | Parancs |
|---|---|---|
| **mag** (`shared/kernel/`) | a kézi beállítások nyilvántartása + kapu (racsni) | `python shared/kernel/check.py` |
| **gráf** (`shared/kernel/graph.py`) | függőségi gráf, körmentesség, nevesített auditok | `python shared/kernel/graph.py` |
| **pad** (`shared/bench/`) | 44 ellenőrzés a közzétett számokra | `python shared/bench/bench.py` |
| **regiszter** (`shared/register/`) | pecsételt vak jóslatok + idő-horgony | `python shared/register/seal.py` |
| **futtató** (`shared/parallel/`) | párhuzamos mezőny, max 8 mag, rendfüggetlenség | `python shared/parallel/demo.py` |
| **H4 út** (`shared/summation.py`) | hordozható, blokkonként egzakt összegzés | `python shared/summation.py` |
| **környezet** (`shared/environment-check.py`) | referencia-környezet + a H4 út ellenőrzése | `python shared/environment-check.py` |

**Referencia-környezet** (a [B függelék](appendix/B-machinery_hu.md)-ben kimondva): Windows 11 Pro, Python 3.12.5, numpy 2.2.4, i9 8 mag/16 szál, 128 GB. **Legfeljebb 8 mag használható.** Köztes fájlok a temp-be, sosem a repóba.

---

## 3. Ami eldőlt — tudomány

### Négy új tétel (mind nulla importtal)

| Tétel | Hol | Mit mond |
|---|---|---|
| **hordozó-tétel** | [PKG-15-9](II-proofs/II-15-dimension-fourth-rung/PKG-15-9-uniform-field_hu.md) | egy szövés akkor tükör-jegyű, ha van olyan koordináta-részhalmaz, amelyre minden lépés összege páratlan |
| **teli-vég tétel** | [PKG-15-10](II-proofs/II-15-dimension-fourth-rung/PKG-15-10-dense-end_hu.md) | a nyom-döntetlen miatt a teli vég kivonás; ott a legmagasabb ütemek döntenek |
| **egy-lyuk tétel** | [PKG-15-10](II-proofs/II-15-dimension-fourth-rung/PKG-15-10-dense-end_hu.md) | $N=n-1$-en a győztes bizonyíthatóan tükör-jegyű (egzakt) |
| **lyuk-létra tétel** | [PKG-15-11](II-proofs/II-15-dimension-fourth-rung/PKG-15-11-hole-ladder_hu.md) | $\text{ár}(n-m) = T - 2dm + D(m)$ — azonosság, becslés nélkül |

**Hatókör, fontos:** a [PKG-15-12](II-proofs/II-15-dimension-fourth-rung/PKG-15-12-convention-scope_hu.md) igazolta, hogy ezek **minden fokszám-reguláris hálón** állnak, nem csak szövéseken (nem-Cayley gráfokon is: Petersen, Desargues). **Ezért túlélnek bármilyen nyelvbővítést, ami a hálót másképp állítja elő.**

### Három vak jóslat, pecséttel és git-időhorgonnyal

| | Tárgy | Ítélet |
|---|---|---|
| **`JOS-01`** | a nyolcas koordináció teljes-mezőny-teteje | **beállt** — (1,3,5,7), mind a 2000 töltésen |
| **`JOS-02`** | egységes kiválasztási szabály → eltűnik-e a tető-fordulás | **részleges** — a lényeg beállt, egy feltétel hibásan volt megfogalmazva |
| **`JOS-03`** | a II/17 hurok szétválik-e a generáló szabály szerint | **bukott** — nem válik szét; és ez jobb hír |

### A két deflációs lelet

1. **A „3, 3, 5" minta konvenció-műtermék** ([PKG-15-9](II-proofs/II-15-dimension-fourth-rung/PKG-15-9-uniform-field_hu.md)). Ellenőrzött kísérlet: a nyolcas tér-jelölt **egyetlen lépését** cserélve (kristálytani testátló → a `KON-02` adta lapátló) a tér elveszti a tükör-jegyet, és a tető-fordulás eltűnik. Egységes konvenció mellett a térkép mindig a honos fokot adja: 6→3, 8→**4**, 10→5, 12→6.

2. **Egy be nem könyvelt import** (`IMP-04`, a `P0.1` audit lelete). A II/3 és a II/4 sehol nem mondja ki a kiterjedésszámát, pedig a közzétett létrák elárulják (II/4: az 1:1/4:1/9:1/16 és a szint-egybeesés a **háromkiterjedésű** Coulomb sajátja). Az importszám 3-ról **4**-re nőtt — nem mert új import jött, hanem mert a könyvelés rövid volt.

### Amit az audit tisztázott

**`P2.4(a)`: nincs kör.** A kiterjedés-program (II/13–II/16) **sehol** nem támaszkodik az 1/r importra. 66 csomópont, 136 él, körmentes.

---

## 4. A könyvelés mai állása

```
aktiv import        : 4 / plafon 4      (IMP-01..04)
kimondott konvencio : 5                 (KON-01..05)
peremadat           : 1                 (PER-01)
hatokor-hatar       : 6                 (HAT-01..06)
jelolt import       : 1                 (JEL-01, kettos allasu)
erzekenysegi fedes  : 5 / 9 = 56%
```

**Megméretlen még:** `IMP-01` (helyiség), `IMP-02` (1/r), `IMP-03` (típusdeklarációk), `KON-05` (generáló szabály).

A pad: **44 ellenőrzés — 38 zöld, 0 bukik, 6 `H4-VAR`** (a visszavont H3 útra írt szkriptek; nem rossz szám, hanem hiányzó előfeltétel).

---

## 5. A nyitott döntés — és ami belőle még nincs megírva

**A tulajdonos döntése: bevezetjük a közvetítő közeget**, teljes értékű, kiegészítő tételként. A terv: [hu/EXTENSION_hu.md](EXTENSION_hu.md).

> ⚠️ **A terv fájlja a *generáló szabály* útját írja le, mert a döntés utána született. A közeg részletes tervezése CSAK ebben a jegyzetben van meg — a következő lépés a `PKG-18-1` szabálykönyv, ami ezt fájlba viszi.**

### A közeg megtervezett alakja

| Döntés | Az indok (kizárólag nyelvi, a mért céloktól függetlenül) |
|---|---|
| helyenkénti mennyiség | a nyelv minden állapota helyeken él |
| **nem normált** | ha normált volna, példány-állapot lenne, nem új kategória |
| törvénye a **meglévő simasági szerződés** | nem adunk új törvényt, ha meglévő elem elég |
| **lineáris** csatolás a súlysűrűséghez | egy példánynak egy helyen egyetlen mennyisége van |
| **nincs tömeg-tag** | tömeg = szabad paraméter; a nyelv nem tűr szabad paramétert |
| **statikus** | egy nem normált hordozó *fejlődési* törvényére a nyelvnek nincs alapja |

**Hatókör-szűkítés a 3. törvényhez:** *a **példányok** fejlődése súlytartó.* A közeg nem példány.

**Miért statikus a legfontosabb döntés:** a statikus közeg **kiintegrálható** ($\min_\varphi \tfrac12\varphi^{\mathsf T}L\varphi - \rho^{\mathsf T}\varphi = -\tfrac12\rho^{\mathsf T}L^{+}\rho$), ezért minden régi próba felülvizsgálata **zárt alakú számolás**: „a deklarált szerződés az-e, amit a közeg adna?" — nem újratervezés.

### ⚠️ A kritikus lelet, ami csak itt van leírva: **az előjel**

A skalár közeg **azonos forrásokra vonzást** ad, ellentétesekre taszítást — **fordítva, mint az elektromosság**. Ez ismert fizikai tény (skalár közvetítő ↔ vektor közvetítő), és **a definíció következménye, nem hatókör-szűkítés.**

Következmény: a skalár közeg nem hordozhatja egyszerre a mag–elektron vonzást és az elektron–elektron taszítást (II/8). Ezt **következményként kell a szabálykönyvbe írni, ami cáfolhat** — nem védekező hatókörként.

### ⚠️ A módszertani korlát, amit a tulajdonos szúrt ki

**A közeget NEM szabad az 1/r-ből visszafelé tervezni.** A nyelv általános leírónyelv; a közeg indoka **szerkezeti** (a szerződés birtoklása szabályozatlan). A helyes sorrend:

1. a definíciót **nyelvi alapon** rögzíteni,
2. **utána** összeírni, mi következik belőle,
3. a következmények közül választani mért próbát,
4. **azt** regisztrálni vakon, és csak azután számolni.

**A törlesztés remény, nem terv.** Lehet, hogy a közeg jó nyelvi elem, bezárja a lyukat, és az `IMP-02` marad, ahol van.

### A felülvizsgálati regiszter (megtervezve, még nincs megvalósítva)

Minden próbafájl fejlécébe új mező: `kozeg: felulvizsgalva | nincs-vizsgalva | nem-erinti`, és egy kapu a `check.py`-ba, ami jelenti az állást. **Lusta felülvizsgálat:** egy régi eredményt csak akkor vizsgálunk felül, amikor tényleg támaszkodunk rá. A `graph.py` megmondja, mire támaszkodik egy próba.

**Számozás:** a II/17 már létezik (generáló szabály), ezért a közeg **II/18**, és a regiszter a II/1–II/17-et jelöli „közeg előtti"-nek.

---

## 6. A II/17 állása — lefutott, megbukott, van előre rögzített folytatás

A [PKG-17-1](II-proofs/II-17-contract-origin/PKG-17-1-rulebook_hu.md) fagyasztott szabálykönyv **2026-08-19-én keletkezett**, a `751fbab`-ban törölve, **visszaállítva**. A hurok lefutott (`shared/II-17-contract-origin/PKG-17-2-loop.py`, 48 futás, 203 s):

```
        | I1        I2        I3        I4
   F1   | PAR       KOZTES    PAR       PAR
   F2   | PAR       PAR       PAR       PAR
   F3   | PAR       KOZTES    PAR       PAR
   F4   | PAR       KOZTES    PAR       PAR
   F5   | PAR       PAR       PAR       KOZTES
   F6   | PAR       KOZTES    PAR       PAR
```

**Ítélet a 7. szakasz szerint: megbukott a lemma** — az I1-ből minden családtag `PÁR`, mindkét normáláson. Az önerősítés győz a frusztráció felett.

**Amit tudni kell a folytatáshoz:**

- **Az összeomlás robusztus** — hat generáló szabályon és két normáláson ugyanaz. Nem konvenció-műtermék, hanem szerkezeti tény.
- **Van nem-párosító fixpont:** az `I2`-ből négy családtag `KÖZTES`-be fut (46 nem-nulla pár, megállva). **De a 8. szakasz kapuja tiltja a kiolvasásukat**, mert az ítélet `PÁR` — ez utólagos keresésnek minősülne. **Ne olvasd ki őket, amíg az ítélet nem KÖZTES.**
- **Az `F3` (tompító) négy futása nem állt meg** 200 körön belül, köztük az `F3/N2/I1`. A tartalom ott is teljesen koncentrált.
- **Kettértelműség a 7. szakaszban, kimondva:** a meg nem álló futásra „nem áll össze ítélet" áll, de a `PÁR` osztályt a szabálykönyv nem köti megálláshoz. A besoroló a tartalom-kritériumot használta. Az ítéletet nem érinti (`KÖZTES` az I1-ből így sem lenne).

**Az előre rögzített folytatás** (az [átadó jegyzet](II-proofs/II-17-contract-origin/II-17-HANDOVER_hu.md) elágazás-táblájából):

> **PÁR** → a kötés-szerződés rossz hordozó → **ugyanez a hurok a simasági szerződéssel, helyeken** — *ágváltás, nem kudarc*

**Ez a legolcsóbb következő lépés**, és becsületesen meg kell csinálni, mielőtt kimondanánk, hogy a generálás nem járható út.

---

## 7. A három módszertani tanulság — mostantól szabály

Mindhárom **holtverseny-kezelési hiba** volt, három különböző alakban:

1. **`JOS-01`:** a holtverseny beszámítását nem rögzítettük előre. → **Mindig rögzítendő.**
2. **`JOS-02`:** olyan küszöböt írtunk elő (`S2 = nulla`), amit egy **saját tétel** (a nyom-döntetlen) kizár. → **A feltételeket teljesíthetőségre kell ellenőrizni a már bizonyított tételek ellen.**
3. **`PKG-15-12`:** tűrés nélküli `argmin`-t hasonlítottunk össze, és a lebegőpontos zaj eltört négy holtversenyt. → **Győztes-halmazt kell összevetni tűréssel, sosem `argmin`-t.**

### És három gépezet-hiba, amit a II/17 futtatása hozott felszínre

4. **Nem érvényesített definíció:** a közelség kölcsönös információ ($\ge 0$), de numerikusan `-1e-15`-re csordul; az `F3` ezen halt meg. **Javítva: a definíció kikényszerítve.**
5. **A rendpróba rosszat mért:** a gyerekek 1 BLAS-szálon futnak, a szülő többszálon → más kerekítés, bitre eltérés. **Javítva: a minta is dolgozó-folyamatban fut.**
6. **A gyorsítótár a kódot nem vette figyelembe** — a kulcs csak (függvénynév, argumentumok) volt, tehát kódjavítás után **a régi eredményeket adta volna vissza, láthatatlanul**. **Javítva: a dolgozó-modul forrásának lenyomata is a kulcsban van.**

---

## 8. A következő lépések, sorrendben

1. **`PKG-17-2` csomagfájl megírása** — a hurok eredménye még csak a regiszterben és a szkriptben áll, csomagban nem. *(Kis munka, de a kapu-szabály kéri.)*
2. **A II/17 simasági ága** — az előre rögzített ágváltás. Ugyanaz a gépezet, helyeken.
3. **`PKG-18-1` szabálykönyv** — a közeg, az 5. szakasz doboza szerint: a definíció **cél és szám nélkül** az első felében, a következmény-lista a másodikban, az előjel-lelet következményként.
4. **A `kozeg:` regiszter-mező + kapu** a `check.py`-ba.
5. **`P1.2` — prior-art audit** a négy új tételre. *Ez dönti el, hogy a matematikai hozadék új-e — és ez a legértékesebb egyetlen nyitott kérdés.*
6. **`P2.6` — formális státusz.** A legnehezebb és a legdöntőbb; a halogatása a legnagyobb kockázat.

**Amit ne csinálj:** a `P2.4`-et (1/r levezetése) a közeg előtt; a 12-es koordináció jóslatát a kiválasztási konvenció rendezése előtt; és **a II/17 KÖZTES futásainak kiolvasását**, amíg az ítélet `PÁR`.

---

## 9. Nyitott adósságok, kimondva

- **`en/` tükrök:** a mai munkából **egyetlen** angol pár sem készült el; minden érintett `_hu` fájl `pair_status: outdated` vagy `missing`. Ez tudatos (a kutatás magyarul folyik), de adósság.
- **Hat `H4-VAR` ellenőrzés** a padon: a `PKG-15-3`, `PKG-15-5`, `PKG-15-7` még a visszavont H3 útra van írva.
- **A II/16 négy szkriptje** még nincs felvéve a padra (a `PKG-16-6` igen).
- **A `PKG-15-12` `argmin`-tanulsága** még nincs átvezetve a többi szkriptbe — csak ott van kijavítva, ahol előjött.
- **`II-17-handover` fejléce** `imports: "nincs"` — a `check.py` ezt most szinonimaként kezeli; érdemes egységesíteni.
