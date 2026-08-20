# Párhuzamos futtató

**English.** A process-pool runner for the independent items inside one package
stage, with an order-independence check, a resumable cache and a hard core cap.
The research is conducted in Hungarian; the text below is the single source of truth.

---

## Mikor szabad párhuzamosítani — és mikor nem

A [szabálykönyv](../../CONTRIBUTING.md) 7. pontja **sorrendet ír elő a csomagok
között**: szabálykönyv → létrák → verseny → kiolvasás, és csomagra csak a
jóváhagyott előzőre szabad építeni. Ezt a sorrendet **nem szabad** párhuzamosítani.

Egy szakaszon **belül** viszont a munka független tagok mezőnye — 503 induló,
495 családtag, hat páronkénti lemma —, és ott a sorrend semmit nem jelent.
**Ez a futtató kizárólag ide való.**

| Párhuzamosítható | Nem párhuzamosítható |
|---|---|
| a mezőny tagjainak létrái | szabálykönyv → létrák → verseny → kiolvasás |
| páronkénti lemmák | ami az előző csomag *kimenő állításaira* épül |
| pásztázások, sorsolt minták | a kapu-szabály minden lépése |
| független próbák egy padon | ami egy közös állapotot ír |

## Futtatás

```bash
python shared/parallel/demo.py
```

A demó a II/15 vonal-család mind a 495 tagjának létráját számolja ki a
[`H4` hordozható úton](../../hu/appendix/B-machinery_hu.md), és minden indulón
ellenőrzi a beépített egzakt nyomösszeget (165888). `--magok N` és `--tiszta`
(gyorsítótár ürítése) állítható.

## Az API

```python
from parallel.runner import Feladat, futtat, jelentes

feladatok = [Feladat(azonosito=str(lepesek),
                     fuggveny="parallel.letra_feladat:letra_es_gorbe",
                     argumentumok={"n": 20736, "lepesek": lepesek})
             for lepesek in mezony]

eredmeny = futtat(feladatok, magok=8, rendproba=8)
jelentes(eredmeny)
```

A `fuggveny` **sztring** (`"modul:fuggveny_nev"`), nem függvényobjektum: Windowson
a folyamatindítás `spawn`, tehát a dolgozónak friss értelmezőben kell
importálhatónak lennie — lambda és closure nem megy át a határon. Aki `futtat()`-ot
hív, annak kell `if __name__ == "__main__":` védőblokk.

## Négy garancia

**1. Rendfüggetlenség.** Az eredmények a **deklarálás** sorrendjében jönnek vissza,
soha nem a befejezés sorrendjében. Ezen felül a `rendproba=N` a feladatok egy
mintáját **újra lefuttatja sorosan**, ebben a folyamatban, és **bitre** összeveti a
párhuzamos eredménnyel.

> Ez a próba a párhuzamosításnak az, ami a kétutas szabály az aritmetikának.
> Nélküle a „gyorsabb lett" nem bizonyíték. Tűrés itt nincs: pont azt rejtené el,
> amit keresünk.

**2. Korlátos gép.** Legfeljebb **8 mag** — a többi a gép tulajdonosáé —, és a
gyerekfolyamatok BLAS/OpenMP szálpoolja 1-re kötve. A `memoriaigenyes=True`
feladatok külön sávban, egyedül futnak.

**3. Hibaizoláció.** Egy elszálló feladat nem viszi el a másik 502-t: a hiba
értékként jön vissza, a mezőny végigfut.

**4. Folytathatóság.** Minden kész feladat a gyorsítótárba kerül, így az újrafuttatás
ott folytatja, ahol az előző abbahagyta. A gyorsítótár a **rendszer temp
könyvtárában** él, nem a repóban — köztes munka, nem termék.

## Kötegelés

Rövid feladatoknál a folyamathatár átlépése annyiba kerülhet, mint maga a számolás.
A futtató ezért kötegel (`koteg=N`, alapból automatikus). Az eredményeken ez nem
változtat — a feladatok úgyis függetlenek —, csak azon, hányszor lépünk át a határon.

## Mért skálázás

A demó mezőnyén (495 induló, ~4,3 s soros munka), referencia-gépen:

| Magok | Idő | Gyorsulás |
|---|---|---|
| 1 | 4,6 s | 1,0× |
| 2 | 2,5 s | 1,8× |
| 4 | 1,7 s | 2,7× |
| 8 | 1,4 s | 3,3× |

Újrafuttatás a tárból: **0,0 s** (495/495 találat).

**Őszintén a korlátról:** a fixköltség (folyamatindítás, importok) ezen a gépen
~1 s, és ez a négy és fél másodperces mezőnyön elviszi a haszon nagy részét — ezért
lapos a görbe négy mag fölött. A futtató ott térül meg, ahol a valódi kutatómunka
él: **perces-órás mezőnyökön**, ahol az egyszeri másodperc nem számít, és a
skálázás közel lineáris.

**Egy megtanult lecke, rögzítve.** Az első változat feladatonként külön fájlba
mentett. Windowson 495 apró fájl visszaolvasása **13,4 s** volt — nyolcszor
annyi, mint újraszámolni az egészet: a gyorsítótár pont ott lassított, ahol
gyorsítania kellett volna. Innen az egyetlen, atomosan cserélt tár, 50 feladatonkénti
mentéspontokkal.

## Egy mellékes megerősítés

A demó mezőny-lelete: a 495 családtagból **15** tükör-jegyű (csupa-páratlan lépésű),
és köztük a legkisebb össz-lépésnégyzetű az **(1, 3, 5, 7)** — pontosan az, amit a
[`JOS-01` vak-jóslat](../register/predictions.json) levezetése megnevez. Ez a jóslat
**levezetését** erősíti meg, nem a válaszát: hogy a mezőny tetejét ki viszi, az a
`P1.1` dolga, és a demó szándékosan nem hasonlítja össze az indulókat.
