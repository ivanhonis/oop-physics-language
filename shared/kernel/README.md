# A kézi beállítások magja

**English.** This directory holds a machine-checkable register of every item the
language did not derive but we set by hand — borrowed concepts, our own rules of
play, raw world data, and stated scope limits — plus the gate that keeps the
register honest. The research is conducted in Hungarian; the text below is the
single source of truth.

---

## Mire való

A repó módszertani szabálya ([I/1](../../hu/I-language/I-01-concept_hu.md)) eddig
két dolgot vezetett: **mit kölcsönöztünk kívülről** (import) és **mit rögzítettünk
magunk** (kimondott konvenció). Ez a nyilvántartás ezt három ponton bővíti:

1. **Négy rangra bontja**, hogy minden kézi elem pontosan egy kategóriában álljon
   (a [PROGRAM](../../hu/PROGRAM_hu.md) H1-feltétele).
2. **Minden elem mellé érzékenységi mezőt ír elő** — ez az a szám, ami ma
   hiányzik: *mennyit hordoz az eredményből az, amit kézzel állítottunk be.*
3. **Gépi kapuval védi**: az importszám nem nőhet csendben, és a nyilvántartás
   nem csúszhat el a korpusztól.

A tár **könyvelés, nem fizika.** Semmit nem számol újra, és egyetlen ítéletet sem
dönthet meg. Az igazság forrása mindig a hivatkozott fejezetfájl.

## Futtatás

```bash
python shared/kernel/check.py
```

Kilépési kód: `0` = minden kapu áll, `1` = van hiba. Csak a Python szabvány-
könyvtárát használja, függősége nincs.

## A négy rang

| Rang | Mit jelent | Törleszthető? |
|---|---|---|
| `import` | kívülről kölcsönzött **világ-állítás** — a nyelv adóssága | igen, levezetéssel |
| `konvencio` | saját játékszabály; a világról nem állít semmit, de megszabja, mit jelent az eredmény | nem — de perturbálandó |
| `peremadat` | a világ példány-adata, amit a nyelv elvileg sem vezet le (skála-kalibráció) | nem, és ez rendben van |
| `hatokor` | kimondott méret- és pásztázási határ: a próba érvényességét szűkíti | nem — de a hatása mérendő |

Ötödik, átmeneti rang: `jelolt-import` — kettős állású elem (ma egyetlen ilyen van,
a helyek egyenrangúsága). A magban tartósan nem maradhat: vagy tétel lesz belőle,
vagy negyedik import.

## Új kézi elem felvétele — a minta

Ha egy csomag bármit kézzel rögzít, a szabálykönyv-csomag (`PKG-NN-1`)
elfogadásával **egy időben** kerüljön be ide egy bejegyzés. A minta:

```json
{
  "id": "KON-05",
  "rang": "konvencio",
  "nev": "roviden, amit beallitottunk",
  "leiras": "Pontosan mi a szabaly, es mi nem tartozik bele.",
  "bevezette": "PKG-17-1",
  "hasznaljak": ["II-17", "PKG-17-1"],
  "allapot": "aktiv",
  "torlesztes": "P1.3",
  "erzekenyseg": {
    "allapot": "nincs-merve",
    "meres": [],
    "megjegyzes": "Melyik varians perturbalna, es miert nem futott meg le."
  },
  "forras": ["hu/II-proofs/II-17-.../PKG-17-1-rulebook_hu.md"]
}
```

Szabályok:

- **Az `id` soha nem használható újra** (a [szabálykönyv](../../CONTRIBUTING.md) 2. pontja);
  visszavont elem `allapot: "visszavont"`-tal marad benn.
- A `bevezette` és a `hasznaljak` **fejezet-azonosítókat** vesz fel (`II-14`,
  `PKG-16-1`), nem útvonalakat — az ellenőrző a fejlécekből oldja fel őket.
- Az `erzekenyseg.allapot` csak akkor lehet `"merve"`, ha a `meres` megnevez egy
  csomagot. Az ellenőrző ezt kikényszeríti.
- Ha egy mérés csak részlegesen fedi az elemet, a **hatókört a `megjegyzes`
  mondja ki** — lásd a `HAT-01`-et: a méret-érzékenység a kiolvasásra megvan
  (PKG-14-5, PKG-15-4, PKG-16-4), a verseny sáv-határaira nincs.

## A kapuk

| Kód | Mit fog meg |
|---|---|
| `A1`–`A4` | séma, azonosító-stabilitás, élő hivatkozások, létező forrásfájlok |
| `B1` | minden `imports:` fejlécet deklaráló fejezet le van fedve a nyilvántartásban |
| `B2` | az I/1-ben **kimondott darabszám** egyezik azzal, amit a tár valóban tartalmaz |
| `C1` | **import-racsni** — az aktív importok száma ≤ `meta.import_plafon` |
| `C2` | **érzékenységi lefedettség** ≥ `meta.erzekenyseg_kuszob` |
| `C3` | kettős állású elem nem maradhat törlesztési mérföldkő nélkül |

A két szám a `meta`-ban a racsni: az `import_plafon` (ma **3**) nem emelhető
csendben, az `erzekenyseg_kuszob` (ma **0**) pedig a [P1.3](../../hu/PROGRAM_hu.md)
lefutása után emelendő. A küszöb emelése az egyetlen módja annak, hogy a
megméretlen kézi beállítás ne halmozódjon újra.

## A mai állás

15 bejegyzés: **3 import**, 1 jelölt import, **4 konvenció**, 1 peremadat,
6 hatókör-határ. Az érzékenységi lefedettség **1/7 = 14%** — a maradék hat
megméretlen kézi elem az az adósság, amiért a tár készült.

**Az első futás egy valós eltérést fogott (`B2`), lezárva.** Az I/1 két kimondott
konvenciót sorolt fel, a csomagok viszont négyet deklarálnak — a `PKG-13-1` /
`PKG-15-1` a **szövés-építést**, a `PKG-14-5` az **őrszem-küszöböt** is. Mivel az
elfogadott csomagok nem íródnak át, a javítás az I/1-ben történt: a darabszám
négyre állt, a két elem indoklással bekerült.

**Az első megmért kézi elem: `KON-04` (őrszem-küszöb).** Új számolás nélkül,
négy elfogadott csomag leolvasásából: a sáv-őrszem értéke a 8-as szövés bukott
esetén 1,0 (egzakt egyezés), a 12-esen 2,84, a II/15-ön 5,37, a II/16-on 7,29.
A küszöb bárhová tolható az **(1,0 ; 2,84]** intervallumon belül anélkül, hogy a
négy kiolvasási ítéletből bármelyik megfordulna — a választott 2-es érték lefelé
2,00-szeres, felfelé 1,42-szeres tartalékkal áll benne. Hatókör kimondva: ez a
**kiolvasási** ítéleteket méri, a verseny ítéletére a küszöb nem hat.
