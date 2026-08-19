---
id: PKG-15-2
type: package
part_of: II-15
lang: hu
pair: PKG-15-2-ladders_en.md
pair_status: in-sync
doc_version: "1.3"
status: jovahagyva
builds_on: [PKG-15-1]
imports: nulla
---

# PKG-15-2 — Az ütem-létrák (számolás-csomag)

**A csomag dolga.** A [PKG-15-1](PKG-15-1-rulebook_hu.md) A1–A8 állításaira építve kiszámolja mind az 503 induló létráját, lefuttatja az öt kötelező önellenőrzést (A7), és a kétutas szabály gépi ütemét (A8). A szkript: `shared/II-15-dimension-fourth-rung/PKG-15-2-ladders.py`.

## 1. Az önellenőrzések eredménye

| Önellenőrzés | Eredmény |
|---|---|
| (iv) nyomösszeg | **165888 mind az 503 hálón** — áll |
| (i) három jegy a fő négyesen | **áll**, egy helyesbítéssel (lásd 2. szakasz): hármas-séták 36 / 24 / 0 / 0; négyes-séták 296 / 216 / 216 / 168; páros-jegy: nincs / nincs / van / van |
| (v) komponensszám | fő és kontroll mind 1; család **479 + 15 + 1**, a nulla-módusok mindenütt a szétesés-tábla szerint — áll |
| (ii) létra-osztályozás | **502 osztály az 503 hálón** — az egyetlen egybeesés a konstrukciós azonosság: J1 = az (1, 2, 3, 4) családtag (lásd 3. szakasz) |
| (iii) körbeérés, gépi bejárással | fő/kontroll irányonként: J1 [5184]; J2 [144, 144]; J3 **[24, 24, 36]**; J4 [12, 12, 12, 12]; K1 [16, 36, 36]; K2 [12, 36, 48]; K3 [8, 8, 18, 18]; K4 [48, 432] — mind ≥ 8, a páros jelölteken mind páros; a család legrövidebb körbeérése 1728 — áll, egy helyesbítéssel (lásd 2. szakasz) |

## 2. Két helyesbítés (a II/14-precedens szerint: a szabálykönyv nem módosul, a helyesbítés itt rögzül)

**H1 — a §5 különbözőség-táblájának J2-sora téves volt.** A szabálykönyvben 48 / 1188 állt; a helyes érték **24 / 216**. A hiba forrása: a rögzítés előtti leszámláló az átlós lépéseket duplán építette (multigráfot számolt) — a létra-út, mint független második út, fogta, a javított duplázásmentes leszámlálás megerősítette. **A hat pár szétválasztása változatlanul teljes:** a keresztpárokat a páros-jegy, a J1–J2 párt a hármas-séták (36 ≠ 24), a J3–J4 párt a négyes-séták (216 ≠ 168) döntik; a J2–J3 négyes-egyezés (216 = 216) ártalmatlan, mert azt a párt a páros-jegy választja szét.

**H2 — a §3 páros-körbeérés feltételének szó szerinti alakja túl tág volt.** A feltétel célja a páros jegy védelme a körbezáráson; a családban 48 nem-páros tag körbeérése páratlan (a legkisebb ilyen a vegyes lépés-paritású tagoknál áll elő), és ez ártalmatlan. A helyes olvasat: a páros körbeérés a **páros-jegyű** indulókon kötelező — ott mind áll (a csupa-páratlan lépésű családtagokon a paritás tételből következően páros) —, a többi indulón csak a ≥ 8 követelmény él.

## 3. A létra-osztályozás lelete

Az 503 induló **502 létra-osztályba** esik. Az egyetlen egybeesés a szándékolt konstrukciós azonosság: a J1 fő jelölt definíció szerint maga az (1, 2, 3, 4) családtag — az osztályozó ezt helyesen egynek méri, ami a gépezet konzisztencia-megerősítése, nem elfajulás. **Rejtett egybeesés nincs:** a kontrollok mind külön osztály, és a II/14-ben látott lépés-átszámozási egybeesésekből e méreten egy sem él — a 20736-os helyszámon a szorzó-átszámozásnak négy egyidejű kongruenciát kellene teljesítenie, és a mérés szerint egy sem teljesíti.

## 4. A gépi ütem (A8) — eredmény

A gépi építő önpróbája három kis szövésen: legnagyobb eltérés 2,3·10⁻¹⁴. A teljes batch lefutott (nagy gépen, hálónként ~8–9 perc): **mind a 32 cél két úton kiszámolva** — a 8 fő/kontroll háló és a 24 sorsolt családtag (mag: 20736, numpy PCG64). A hálónkénti eltérések 8,9·10⁻¹⁴ és 1,3·10⁻¹² között; **a legnagyobb kétutas eltérés 1,30·10⁻¹²** — négy nagyságrenddel a 10⁻⁸-os osztályozási kvantum alatt.

## 5. Ítélet erről a csomagról

**Áll.** Mind az öt önellenőrzés (A7) teljesül — két rögzített helyesbítéssel (H1, H2) —, és az A8 kétutas ütem teljes: 32/32 cél, legnagyobb eltérés 1,3·10⁻¹².

## 6. Kimenő állítások (a PKG-15-3 ezekre építhet)

- **L1:** mind az 503 létra zárt Fourier-úton kiszámolva; nyomösszeg 165888 mindenütt.
- **L2:** a különbözőség-jegyek javított táblája: hármas-séták 36 / 24 / 0 / 0, négyes-séták 296 / 216 / 216 / 168 — a hat pár szétválasztása teljes (H1).
- **L3:** 502 létra-osztály; az egyetlen egybeesés a J1 ≡ (1, 2, 3, 4) konstrukciós azonosság; rejtett egybeesés nincs.
- **L4:** a körbeérés-tábla gépi bejárással igazolva; a páros-körbeérés hatóköre pontosítva (H2).
- **L5:** a verseny (PKG-15-3) a zárt létrákra építhet; az azonosság-tűrés rögzített értéke 10⁻⁸ — a mért kétutas skála (1,3·10⁻¹²) fölött négy nagyságrenddel, a valódi létra-különbségek alatt.
