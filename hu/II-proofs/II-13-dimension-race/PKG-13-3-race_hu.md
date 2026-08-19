---
id: PKG-13-3
type: package
part_of: II-13
lang: hu
pair: PKG-13-3-race_en.md
pair_status: in-sync
doc_version: "1.3"
status: jovahagyva
builds_on: [PKG-13-1, PKG-13-2]
imports: nulla
---

# PKG-13-3 — A betöltési verseny (levezetés-csomag)

**Épít:** [PKG-13-1](PKG-13-1-rulebook_hu.md) (A4, A5), [PKG-13-2](PKG-13-2-ladders_hu.md) (B1–B4) · **Számoló kód:** `PKG-13-3-race.py`

---

## 1. Kérdés

Melyik szövés nyeri a betöltési versenyt melyik példányszámnál, a rögzített ítélet-szabály szerint?

## 2. A kötelező előfeltétel (B3): független újraszámolás

A létrák új kódúton (szomszédlistás felépítéssel) újraszámolva: mind a nyolc hálón a nyomösszeg pontosan 64; nulla-módusok a PKG-13-2 szerint (J1: 1, J2: 1, J3: 2, második darabolt: 2); szúrópróba-értékek (0,738; 2,5858; a tórusz-létra; a darabolt 4-es szintje) a közzétett hivatkozási értékekkel egyeznek. A verseny indulhatott.

## 3. Az eredmény — győztes-tábla (szigorú győztes; holtverseny jelölve)

| N példány | Győztes | Költség | J1 vonal | J2 sík | J3 darabolt |
|---|---|---|---|---|---|
| 1 | mind (holtverseny) | 0 | 0 | 0 | 0 |
| 2 | J3 és a második darabolt | 0 | 0,738 | 2 | **0** |
| 3 | **J1** | 1,476 | **1,476** | 4 | 2,586 |
| 4 | **J1** | 4,062 | **4,062** | 6 | 5,172 |
| 5 | **J1** | 6,648 | **6,648** | 8 | 7,757 |
| 6 | **J3** | 10,343 | 10,648 | 12 | **10,343** |
| 7 | **J3** | 14,343 | 15,081 | 16 | **14,343** |
| 8 | **J3** | 18,343 | 19,515 | 20 | **18,343** |
| 9 | pásztázó (1,6) | 22,648 | 24,164 | 24 | 23,757 |
| 10 | pásztázó (1,6) | 26,648 | 28,812 | 28 | 29,172 |
| 11 | **J2 — egyedüli szigorú győzelem** | 32 | 34,227 | **32** | 34,586 |
| 12 | pásztázók (1,6) és (1,4) | 37,476 | 39,641 | 38 | 40 |
| 13 | pásztázó (1,7) | 42,343 | 45,641 | 44 | 46 |
| 14 | második darabolt (2,6) | 48 | 51,641 | 50 | 52 |
| 15 | négyes holtverseny 56-on | 56 | 57,820 | **56** | 58 |
| 16 | mind (nyom-döntetlen) | 64 | 64 | 64 | 64 |

**Előre regisztrált tények:** mindhárom áll — az $N = 2$-es azzal a transzparens kiegészítéssel, hogy a szigorú győzelmen a közben felfedezett második darabolt is osztozik (a tény tartalma — a darabolt nulláz, az összefüggő fizet — változatlan).

## 4. Ítélet a rögzített 7. szabály szerint — két olvasat, mindkettő pontosan

**Fő olvasat (a szabály betűje: veri-e a J2 egyszerre a J1-et és a J3-at?):** igen, az összefüggő **10–15** tartományon — a 3–15-ös érdemi sáv felső fele. **A próba részleges igent mond a kiterjedésre: magas sűrűségen a sík veri a vonalat és a darabolt vonalat.**

**Teljes mezőny (szigorú győztes minden induló ellen):** a verseny rezsimekre esik — ritkán a vonal (3–5), alatta-középen a darabolt (6–8), fölötte kereszt-vonalak (9–10, 12–13), a teli vég tükör-hatásai (14–15) —, és a sík egyetlen szigorú győzelme **N = 11**.

## 5. Megfigyelések

- **A héj-logika visszatér — a hálók szintjén.** A sík fokhatárai (zárt fokai): 1, 5, 11, 15 — és pontosan 11-nél győz, 15-nél holtversenyben áll. A darabolt fokhatárai 2, 6, 8 — győzelmi sávja 6–8. A győztes ott nyer, ahol a saját létrájának egy foka éppen betelik: a [II/7](../II-07-bowl-magic-numbers/proof_hu.md) bűvös-szám logika a tér-kiválasztás szintjén ismétlődik.
- **Tükör-hatás a teli végen** (a nyom-döntetlen folyománya): majdnem-teli töltésnél a költség = 64 mínusz a betöltetlen felső ütemek összege — ott az nyer, aki a költségét kevés, magas ütembe tömöríti; ezért viszi a 14-et a második darabolt (két 8-as csúcsütemével).
- **A kiterjedés sűrűségfüggő egyensúlyi tulajdonság:** ugyanaz a költségvetés ritkán vonalat, közepén darabokat, magas sűrűségen síkot szőne — a kiterjedés nem a hálóé, hanem a háló+töltés párosé.

## 6. Import-számla és ítélet

Új import: **nulla.** Utólagos szabálymódosítás nem történt; a pásztázók győzelmei a rögzített mezőny részei. **Ítélet: áll** — az eredmény részleges, és pontosan úgy, foltokkal együtt van rögzítve, ahogy a szabálykönyv előírta.

## 7. Kimenő állítások (a PKG-13-4 és a szintézis csak ezekre építhet)

- **C1:** a győztes-tábla a 3. pont szerint.
- **C2:** fő olvasat: részleges igen — a sík a 10–15 összefüggő tartományon veri a J1-et és a J3-at.
- **C3:** a sík egyetlen szigorú győzelme $N = 11$ — a saját zárt foka.
- **C4:** a PKG-13-4 (kiolvasás) a J2-n, $N = 11$-nél fut: szigorú győztes és zárt fok — az állapot egyértelmű, vetítő nem kell.
- **C5:** a héj-logika és a tükör-hatás megfigyelésként rögzítve; tétellé emelésük nem e csomag dolga.
