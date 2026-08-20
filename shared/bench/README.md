# A hitelesítő-pad

**English.** A one-command regression bench that re-runs the package scripts of
the rulebook-era proofs and checks every accuracy number they print against the
value published in the package. The research is conducted in Hungarian; the text
below is the single source of truth.

---

## Mire való

A [PROGRAM](../../hu/PROGRAM_hu.md) `P0.2` mérföldköve: *„gépi futtatással,
emberi kéz nélkül visszaadja-e mind a négy meglévő eszköz a
[B függelék](../../hu/appendix/B-machinery_hu.md) összes rögzített ellenőrző
számát?"* — bukás-ága pedig kimondja: **ami csak kézzel reprodukálható, az
reprodukálhatósági adósság, és előbb ez törlesztendő, mielőtt bármi új épül.**

## Futtatás

```bash
python shared/bench/bench.py
```

- alapból kihagyja a `lassu: true`-val jelölt szkripteket
- `--teljes` mindent futtat (a `PKG-15-4` sűrű sajátfeladata ~10–11 GB, ~17 perc)
- `--proba II-14` egyetlen próbára szűkít
- `--jobs N` a párhuzamos dolgozók száma

**Magkorlát.** A pad **legfeljebb 8 magot** használ (a gép többi része a
tulajdonosáé), és a gyerekfolyamatok BLAS/OpenMP szálpoolját 1-re köti — enélkül
8 párhuzamos szkript egyenként saját poolt nyitna, és a valódi terhelés a
nyolcszorosa lenne. A `memoriaigenyes: true`-val jelölt szkriptek (ma egy: a
`PKG-15-4`, ~10–11 GB) **sosem futnak párhuzamosan**, hogy ne fogyjon el a RAM.

Mérve: a párhuzamosítás a gyors futást ~340 s-ról **49 s**-ra vitte.

Kilépési kód: `0`, ha minden lefutott ellenőrzés zöld. Függősége a `numpy`-n túl nincs.

**Előtte futtasd a [környezet-ellenőrzőt](../environment-check.py).** A pad nem
tudja szétválasztani a környezeti korlátot a valódi hibától — az a másik szkript dolga.

## Négy ítélet

| Ítélet | Mit jelent |
|---|---|
| `ALL` | a szám visszajött a deklarált tűrésen belül |
| `BUKIK` | nem jött vissza — valódi eltérés |
| `URES` | **a próba nem fedez semmit** (lásd alább) |
| `H4-VAR` | **hiányzó előfeltétel, nem rossz szám** (lásd alább) |
| `NINCS MEG` | a minta nem talált a kimenetben — a szkript kimenete változhatott |

### Az `URES` ítélet

Kétutas ellenőrzés két, elvileg **független** számolási utat vet össze. Ha az
eltérés **pontosan nulla**, a két út nagy eséllyel egybeesett — ezen a platformon
az `np.longdouble` a `float64` álneve —, tehát a próba semmit nem fedez, mégis
zöldnek látszana.

A pad ezt bukásnak veszi. **A hamis zöld rosszabb, mint a piros:** ez a gépi
megfelelője annak a kézi beállításnak, amit soha senki nem mért meg.

### A `H4-VAR` ítélet

A [`H4` helyesbítés](../../hu/appendix/B-machinery_hu.md) visszavonta a `H3`
hosszú-lebegős útját, és hordozható, blokkonként egzakt összegzésre cserélte
(`shared/summation.py`). Néhány csomag-szkript még a régi útra van írva: a
referencia-környezetben ezek **előfeltétele hiányzik**, nem a számuk rossz.

Az ilyen ellenőrzés a tűrés-fájlban `h3_fuggo: true`, ítélete `H4-VAR`. A pad
teljes listával jelenti őket, de nem buktatja rájuk a kaput — `BUKIK`-nak
nevezni őket hamis vád volna, zöldnek hamis felmentés.

## A tűrés-fájl

A [tolerances.json](tolerances.json) minden ellenőrzésnél rögzíti a mintát, a
módot (`tures` / `egyezes` / `szoveg`), a tűrést és a **közzétett** értéket.
A tűrés utólagos tágítása tilos — a [szabálykönyv](../../CONTRIBUTING.md) 7. pontja.

Új csomag felvétele: egy blokk a `padok` tömbbe, szkriptenként. Amíg egy szkript
mintája nincs meg, a `felvetelre_var` listában álljon, kimondott okkal — a pad
így a **saját lefedettségét is jelenti**, nem hallgatja el.

## A mai állás

43 ellenőrzés 13 szkripten; további 4 szkript (a teljes II/16) felvételre vár.
Gyors futásban: **31 zöld, 0 `BUKIK`, 6 `H4-VAR`** — a kapu áll.

- **II/13 és II/14 hiánytalanul reprodukálódik** (14/14 zöld).
- **II/15 nagyrészt.** Visszajön: a `PKG-15-2` mind a három száma, a `PKG-15-4`
  minden száma a kétutas vetítő-pecséttel együtt (1,78·10⁻¹⁵), a `PKG-15-6`
  teljes irány-tétel-táblája, és a `PKG-15-7` két kulcsszáma — a szigorúsági
  tartalék **0,207180** és a lefedettség **44,0%**.

  Hat ellenőrzés `H4-VAR`, **mind ugyanabból az egy okból**: még a visszavont
  `H3` útra vannak írva (`PKG-15-3` teljes-töltési egyezés és float64
  kereszt-ellenőrzés; `PKG-15-5` E1, E2; `PKG-15-7` E2, E3). A hordozható úton
  ugyanezek a mennyiségek a tűrés alatt maradnak — `python shared/summation.py`.
- **II/16 még nincs felmérve** (248 832 hely; a futásidő ismeretlen).
