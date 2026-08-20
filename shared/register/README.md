# A jóslat-regiszter

**English.** A register of claims fixed *before* the computation that decides
them, each frozen by a SHA-256 seal. The research is conducted in Hungarian; the
text below is the single source of truth.

---

## Mire való

A repó tizenhat próbája mind **ismert számot** adott vissza. A szkeptikus első
vádja pontosan ez: *retrodikció + átcímkézés.* A jóslat-regiszter az első eszköz,
amellyel egy állítás úgy zárul le, hogy **a válasz a lezáráskor senkinek nincs a
birtokában** — a [PROGRAM](../../hu/PROGRAM_hu.md) `P0.3` mérföldköve.

## Futtatás

```bash
python shared/register/seal.py
```

`--pecsetel` lepecsételi a még pecsét nélküli bejegyzéseket. Függősége nincs.

## A két mechanizmus

| | Mit bizonyít |
|---|---|
| **pecsét** (SHA-256) | a bejegyzés a pecsételés óta **nem változott** — az állítás, az ablak és a siker/bukás-feltétel utólag nem igazítható |
| **commit** | **mikor** rögzült — a git-történet az idő-horgony |

**A kettő külön-külön semmit sem ér.** Commit nélküli pecsét nem bizonyít
vakságot: a fájl egy mozdulattal átírható és újrapecsételhető. A `seal.py` ezért
külön sorban jelenti a commit-állapotot, és figyelmeztet, ha hiányzik.

Ami **nem** része: a titkosítás. A célszám-széf sózott hashe olyan értéket rejt,
amit a szerzőnek nem szabad megnéznie; ez a regiszter fordítva dolgozik —
**közzéteszi és befagyasztja** az állítást. A pecsét bárki által újraszámolható.

## Pecsételt és szabad mezők

Pecsételt (utólag nem mozdítható): `id`, `merfoldko`, `datum`, `kerdes`,
`joslat`, `megnevezett_gyoztes`, `levezetes`, `ablak`, `siker_felteteI`,
`siker`, `bukas_felteteI`, `ismert_feszultseg`.

Szabad (a munka haladtával frissül): `allapot`, `commit`, `pecset`, `forras`,
`vegrehajtas`, `kornyezeti_felteteI`.

## A mai állás

**`JOS-01` — a `P1.1` vak-jóslata.** Pecsét: `4332b12717f2c30b…`, állapot:
`regisztralt`.

A tető-törvényből előre megnevezve: nyolcas koordináción a teljes mezőny teli
végét a tükör-jegyű vonal-tagok viszik, és köztük a legtöbb töltést az
**(1, 3, 5, 7)** bekötés nyeri. Ablak: a teli vég 2000 töltése (N = 18737…20736),
ugyanakkora, mint amekkorát a [PKG-16-5](../../hu/II-proofs/II-16-coordination-ten/PKG-16-5-transfer_hu.md)
tízesen leolvasott. Siker: S1 (≥ 1900/2000 tükör-jegyűé) **és** S2 (a legtöbbet
nyerő az (1,3,5,7)).

**Miért vak ma:** a futtatás hosszú-lebegős utat kíván, ami ezen a gépen nem
létezik — a válasz fizikailag senkinél nincs meg.

**Egy feszültség előre kimondva:** a `PKG-15-3` szerint a fő négyes a teljes
mezőnyben pontosan 2 töltésen nyer szigorúan, és a futás nem nevezi meg, melyik
kettőn. Ha ez a teli végre esik, az S1-et még nem dönti el, de a legfelső töltés
akkor nem vonal-tagé — ezt a jegyzőkönyv külön sorban jelenti, hogy utólag ne
lehessen belemagyarázni.

> **Kötelező következő lépés: a bejegyzést commitolni kell, mielőtt bárhol
> lefut.** Enélkül a `P1.1` később nem jóslat lesz, hanem fegyelmezett
> retrodikció — és a különbség pontosan az, amit a program bizonyítani akar.
