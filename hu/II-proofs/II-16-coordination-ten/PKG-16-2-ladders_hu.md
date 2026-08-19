---
id: PKG-16-2
type: package
part_of: II-16
lang: hu
pair: PKG-16-2-ladders_en.md
pair_status: in-sync
doc_version: "1.3"
status: jovahagyva
builds_on: [PKG-16-1]
imports: nulla
---

# PKG-16-2 — Az ütem-létrák (számolás-csomag)

**A csomag dolga.** A [PKG-16-1](PKG-16-1-rulebook_hu.md) A1–A8 állításai szerint kiszámolja mind a 805 induló létráját áramoltatott feldolgozással, lefuttatja az önellenőrzéseket (A7) és a kétutas szabály három első elemét (A8; a negyedik, a vetítő-pecsét, a PKG-16-4-ben fut). A szkript: `shared/II-16-coordination-ten/PKG-16-2-ladders.py`.

## 1. Eredmények

| Ellenőrzés | Eredmény |
|---|---|
| létrák + momentum-fedezet (rend ≤ 4, **mind a 805 indulón**) | legnagyobb eltérés a kombinatorikus séta-számoktól **4,6·10⁻¹³** — áll |
| nyomösszeg 2 488 320 | legnagyobb eltérés 4,7·10⁻¹⁰ (viszonylagosan 1,9·10⁻¹⁶) — áll |
| komponensszám | mindenütt a szétesés-tábla szerint (786 + 6) — áll |
| létra-osztályozás | **804 osztály a 805 indulón** — az egyetlen egybeesés a konstrukciós azonosság: J1 = az (1, 2, 3, 4, 5) családtag; rejtett egybeesés nincs |
| körbeérés, gépi úton | mind ≥ 8; nevezetes értékek: J2 [288, 432] (a (0,2) lépés felezi az 576-os irányt), KA2 [216, 576], J5 [12⁵]; a család legrövidebbike 20736 (a széteső tagoknál a példányon mérve) — áll |
| (i) ritka maradék-próba (13×64 + 24×16 módus, mag 248 832) | a javított próbával legnagyobb maradék **5,3·10⁻¹⁴** — áll |
| (iii) kis-példányos sűrű hitelesítés (13 minta) | legnagyobb eltérés **3,4·10⁻¹³** — áll |

## 2. Két javítás a maradék-próbában (a próba hibája volt, nem a hálóké)

**Első futásán a maradék-próba 12,8-at jelzett** — miközben a másik két kétutas elem (momentum-fedezet, kis-sűrű) 10⁻¹³-on állt. A jelzés forrása a próba **saját viszonyítási képlete** volt: az ütemet a hiperkocka-különeset szerint (tengelyenkénti fázisokkal) számolta, ami a vegyes-lépésű bekötéseken hamis. A képlet a bekötés-vektoros fázisra javítva; emellett a nagy körön a fázis-felhalmozás lebegőpontos vesztesége (2,7·10⁻⁹) egzakt egész-maradékos fázisredukcióval megszűnt. **Módszertani jegyzet:** a négyelemű kétutas forma redundanciája pontosan így véd — két elem hitelesítette a létrákat, a harmadik a saját hibáját jelezte ki; szabály nem változott.

## 3. Ítélet erről a csomagról

**Áll.** Minden önellenőrzés és a kétutas forma mindhárom itteni eleme teljesül; a mezőny tiszta (804 osztály, csak a szándékolt azonossággal).

## 4. Kimenő állítások

- **L1:** mind a 805 létra zárt úton; nyomösszeg és komponensszám mindenütt rendben.
- **L2:** a jegy-tábla momentum-úton is igazolt (a hármas-séták egy jegye mind a tíz fő párt szétválasztja).
- **L3:** 804 létra-osztály; egyetlen, szándékolt egybeesés; a kontrollok mind külön osztály.
- **L4:** a körbeérés-tábla gépi úton igazolt, a (0,2)/(2,0) lépések felező hatásával együtt.
- **L5:** a verseny (PKG-16-3) a zárt létrákra építhet, hosszú-lebegős úton, 10⁻⁸ tűréssel.
