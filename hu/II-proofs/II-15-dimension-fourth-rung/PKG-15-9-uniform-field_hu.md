---
id: PKG-15-9
type: package
lang: hu
pair: PKG-15-9-uniform-field_en.md
pair_status: missing
doc_version: "1.4"
status: jovahagyva
part_of: II-15
builds_on: [PKG-15-1, PKG-15-3, PKG-15-5, PKG-15-6, PKG-15-8, PKG-16-1]
imports: nulla
---

# PKG-15-9 — A hordozó-tétel és az egységes mezőny döntő kísérlete

**Egy mondatban.** Levezettük, mitől tükör-jegyű egy szövés, és a tétellel megmutattuk: a II/15 tető-fordulása — a három visszatérése a legsűrűbb tartományban — **egyetlen kézzel választott lépésen múlik**; ha a tér-jelölt a repó saját kiválasztási szabályából jön, a fordulás eltűnik.

## 1. Kérdés (a számolás előtt rögzítve)

Két kérdés, egy csomagban, mert a második az elsőből következik:

1. **Miért választ a tükör?** A [III/1, 7–8.](../../III-frontier/III-01-candidate-laws_hu.md) hordozó-kérdése: levezethető-e, mely szövés tükör-jegyű, és kiadja-e a térkép a három mért koordinációt?
2. **Mennyit hordoz ebből a kézi jelölt-választás?** Ha a nyolcas koordináció tér-jelöltje egységesen a `KON-02` kiválasztási szabályból jön, túléli-e a lépcső-ítélet?

## 2. A hordozó-tétel

> **Tétel.** Egy $\mathbb{Z}^d$-beli $\pm S$ lépéskészletű szövés akkor és csak akkor tükör-jegyű (páros), ha van a koordinátáknak olyan $T$ részhalmaza, amelyre **minden** $s \in S$ lépés $T$-összege páratlan:
>
> $$\sum_{i \in T} s_i \equiv 1 \pmod 2 \qquad \text{minden } s \in S\text{-re.}\tag{K-PKG159-1}$$

**Levezetés, négy lépés, nulla import.** *(i)* A háló akkor páros, ha van kétszínezés, amelyben minden él színt vált. *(ii)* A szövés csúcsai $\mathbb{Z}^d$ pontjai, élei a $\pm S$ eltolások; egy színezés akkor konzisztens, ha $\mathbb{Z}^d \to \mathbb{Z}/2$ homomorfizmus. *(iii)* Minden ilyen homomorfizmus alakja $x \mapsto \sum_{i \in T} x_i \bmod 2$ valamely $T$ koordináta-részhalmazra. *(iv)* Az élek akkor váltanak színt, ha minden lépés képe 1 — ez a (K-PKG159-1). $\square$

**Következmény (a gyakorlati alak).** Ha a szövés tartalmazza mind a $d$ tengelyt, akkor $T$ kényszerűen az összes koordináta, és a feltétel egyszerűsödik:

> **minden többlet-lépés koordináta-összege páratlan.**

Ez adja a lépés-szintű magyarázatot: a **testátló** $(1,-1,-1)$ összege $-1$, páratlan → tükör-jegy; a **lapátló** $(0,1,-1)$ összege $0$, páros → nincs tükör-jegy.

## 3. Kétutas ellenőrzés (a kétutas szabály algoritmus-alakja)

A tükör-jegyet két **független algoritmussal** döntöttük el minden deklarált jelöltön:

- **A út:** a (K-PKG159-1) kritérium — a $2^d$ koordináta-részhalmaz átvizsgálása.
- **B út:** színkép-szimmetria — a létra és a $2\cdot\text{koordináció} - \text{létra}$ azonos halmaz-e.

**Eredmény: a két út mind a 12 deklarált fő jelöltön egyezik, kivétel nélkül.**

## 4. A tükör-hordozó-térkép

A kritérium a deklarált mezőnyökön pontosan visszaadja a mért eredményt:

| Koordináció | Tükör-jegyű fő jelöltek | Legalacsonyabb | A csomagok mérése |
|---|---|---|---|
| hatos | tér (3) | **3** | 3 ✔ |
| nyolcas | tér BCC (3), négykiterjedés (4) | **3** | 3 ✔ |
| tízes | ötkiterjedés (5) | **5** | 5 ✔ |

**A `P2.3` (a) siker-feltétele tehát betű szerint teljesül.** De a térkép egységes konvenció mellett mást ad:

| Koordináció | `KON-02` egységesen | „testátló-minta" egységesen | A csomagok ténylegesen |
|---|---|---|---|
| 6 | 3 | 3 | 3 |
| 8 | **4** | 3 | **3** |
| 10 | 5 | **3** | **5** |
| 12 | 6 | 3 | — |

**Egyik egységes konvenció sem adja ki a „3, 3, 5" mintát.** A nyolcas koordináció tér-jelöltje testátlót kapott, a tízesé lapátlót — **két különböző szabály.** A [PKG-16-1](../II-16-coordination-ten/PKG-16-1-rulebook_hu.md) §9 az eltérést már kimondta; ami eddig nem hangzott el: **ezen az egy lépésen múlik a minta.**

## 5. A döntő kísérlet — vak protokoll

A jóslat a számoló szkript **létezése előtt** rögzült:

| | |
|---|---|
| bejegyzés | `JOS-02` (`shared/register/predictions.json`) |
| pecsét | `db104804893ee3ac` |
| idő-horgony | commit `98d1b273`, 2026-08-20 14:52:52 +02:00 |

**A rendszer:** azonos a [PKG-15-1](PKG-15-1-rulebook_hu.md)-gyel — 20736 hely, nyolcas koordináció, J1 vonal, J2 király-sík, J4 hiperkocka változatlan. **Egyetlen csere:** J3′ tér = 24×24×36, bekötés ±(1,0,0), ±(0,1,0), ±(0,0,1), **±(0,1,−1)** — a `KON-02` kimenete a BCC helyett.

**Előfeltételek, mind teljesült:** nyomösszeg egzaktul 165888 minden indulón (eltérés 0,00); minden körbeérés ≥ 8; és a hordozó-tétel előrejelzése beigazolódott — **a J3′ csúcs-üteme 13,000 < 16, a tükör-jegy eltűnt.**

Futtatható alak: `shared/II-15-dimension-fourth-rung/PKG-15-9-uniform-field.py`.

## 6. Eredmény — a lépcső egységes mezőnyön

| Sáv | Közzétett (BCC-vel) | Egységes mezőny (lapátlóval) |
|---|---|---|
| vonal | 2..4217 | 1..4217 |
| sík | 4218..**7964** | 4218..**6910** |
| tér | **15997..20734** (a tetőn) | **6911..9799** (középen) |
| négykiterjedés | 7965..15996 | **9800..20735** (a tetőn) |

A lépcső **monoton** lett: vonal → sík → tér → négykiterjedés. **A három nem tér vissza a legsűrűbb tartományban.**

Az ablakban ($N = 18737\ldots20736$): a négykiterjedés **2000/2000**; holtverseny 1, és az is a teli töltés.

## 7. Ítélet a `JOS-02` rögzített feltételei szerint

| Feltétel | Eredmény |
|---|---|
| **S1** — ≥ 1900 a négykiterjedésé | **áll** — 2000/2000 |
| **S2** — a J3′ nulla töltést nyer | **nem áll betű szerint** — 1 töltést nyer |
| **B1** — a J3′ mégis viszi a tetőt | nem vált ki |
| **B3** — a holtverseny uralja az ablakot | nem vált ki |
| **K1** — kontroll: a teljes mezőny teteje (1,3,5,7) | **áll** — 2000/2000 |

**Ítélet: részleges.**

**Az S2 hibája a regisztrációé, nem a világé — kimondva.** Az az egy töltés az $N = 20736$ **teli** töltés, ahol minden induló költsége pontosan a nyomösszeg. Ez a [II/12](../II-12-network-race/proof_hu.md) **nyom-döntetlen tétele**. Az előre rögzített holtverseny-szabály mellett tehát *minden* induló „nyeri" a teli töltést, bármi legyen a mezőny: az „S2 = nulla" küszöb **tétel szerint teljesíthetetlen volt, ab initio**. A feltétel érvénytelen, nem cáfolt.

## 8. Import-számla

Új import: **nulla.** A hordozó-tétel tiszta paritás-levezetés a lépéskészletről. A rendszer a PKG-15-1-ből, az ablak a PKG-16-5-ből, a döntetlen-törő a `KON-02`-ből (kimondott konvenció) örökölt. A nyom-döntetlen a II/12 tétele.

## 9. Ítélet erről a csomagról

**Áll, részleges jóslat-ítélettel.** A hordozó-tétel levezetve és két úton igazolva; a döntő kísérlet lefutott, a kontroll áll, és a jóslat lényege beigazolódott.

## 10. Kimenő állítások

- **K1:** **Hordozó-tétel** (K-PKG159-1): egy szövés akkor és csak akkor tükör-jegyű, ha van olyan koordináta-részhalmaz, amelyre minden lépés összege páratlan. Tengelyeket tartalmazó szövésnél: minden többlet-lépés koordináta-összege páratlan. **Tétel, nulla importtal.**
- **K2:** A kritérium a három mért koordináció deklarált mezőnyén kivétel nélkül visszaadja a mért tükör-jegyeket, két független algoritmussal.
- **K3:** A tükör-hordozó-térkép **konvenció-függő**: `KON-02` egységesen mindig a honos fokot adja (6→3, 8→**4**, 10→5, 12→6); a „3, 3, 5" mintát egyik egységes konvenció sem adja ki.
- **K4:** **Ellenőrzött kísérlet:** a többlet-lépés paritásának megváltoztatása — és csak azé — megszünteti a tető-fordulást. Ez a tető-törvény **hordozó-felét erősíti**: a tükör-jegy az, ami a teli véget dönti.
- **K5:** Ugyanez **deflációs** a kiterjedés-kérdésre: „nyolcason a három viszi a tetőt" a kristálytani BCC kézi választásának következménye. A repó saját szabályával négy volna.
- **K6:** A `KON-02` érzékenységi száma megvan: **a kiválasztási szabály megváltoztatása a nyolcas tükör-hordozót 3-ról 4-re fordítja, és a tető-fordulást megszünteti.**

> A K1–K6 csak e csomag **jóváhagyása után** vezethető át a fejezetekbe. A [III/1, 8.](../../III-frontier/III-01-candidate-laws_hu.md) és a [III/2, 8.](../../III-frontier/III-02-open-questions_hu.md) átírása a jóváhagyás dolga.
