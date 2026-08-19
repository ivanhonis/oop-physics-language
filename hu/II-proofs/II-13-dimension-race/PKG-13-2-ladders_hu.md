---
id: PKG-13-2
type: package
part_of: II-13
lang: hu
pair: PKG-13-2-ladders_en.md
pair_status: in-sync
doc_version: "1.3"
status: jovahagyva
builds_on: [PKG-13-1]
imports: nulla
---

# PKG-13-2 — Az ütem-létrák (levezetés-csomag)

**Épít:** [PKG-13-1](PKG-13-1-rulebook_hu.md) (A1–A4) · **Nem tartalmaz:** betöltési versenyt — a létrák itt csak kiszámolódnak, a verseny a PKG-13-3 dolga. · **Számoló kód:** `PKG-13-2-ladders.py`

---

## 1. Kérdés

Mi a három jelölt és a teljes vonal-családi pásztázás ütem-létrája, két független módszerrel ellenőrizve?

## 2. Bemenetek

PKG-13-1: A1 (rendszer), A2 (jelöltek és kötelező pásztázás), A3 (költségdefiníció), A4 (előre regisztrált tények). Gépezet: a [II/12](../II-12-network-race/proof_hu.md) hálózati ütem-létra számolása ([B függelék](../../appendix/B-machinery_hu.md), 2. eszköz), kiegészítve a szövés-hálók zárt képletével mint független ellenőrzéssel.

## 3. A számolás

Minden háló létrája kétszer számolódik: a szerződésháló mátrixának sajátfeladataként (gépezet), és — ahol a szövés körből épül — a szövések zárt alakjából (analitikus képlet). A darabolt jelölt ráadásul két független felépítésben: a 16-os szövés tagjaként és két különálló 8-as körként.

## 4. Eredmény — a három jelölt létrája (költség, csatolásegységben; ×n = ennyi ütem ezen a fokon)

| Jelölt | Létra |
|---|---|
| **J1 — vonal** | 0; 0,738 (×2); 2,586 (×2); 4; 4,434 (×2); 4,649 (×2); 5,414 (×2); 6 (×2); 6,180 (×2) |
| **J2 — sík (tórusz)** | 0; 2 (×4); 4 (×6); 6 (×4); 8 |
| **J3 — darabolt** | 0 (×2); 2,586 (×4); 4 (×2); 5,414 (×4); 6 (×4) |

## 5. A pásztázás — a vonal-család mind a 21 tagja, 7 különböző létrában

| Lépéspárok | Nulla-módusok | A létra eleje |
|---|---|---|
| (2,4), (4,6) — **ez maga a J3** | 2 | 0; 0; 2,586… |
| (2,6) — **második darabolt szövés** | 2 | 0; 0; 4; 4… |
| (1,2), (2,7), (3,6), (5,6) — **a J1 osztálya** | 1 | 0; 0,738; 0,738… |
| (1,7), (3,5) | 1 | 0; 1,172; 1,172; 4… |
| (1,3), (1,5), (3,7), (5,7) | 1 | 0; 1,387; 1,387; 2,918… |
| (1,6), (2,3), (2,5), (6,7) | 1 | 0; 1,820; 1,820; 2,586… |
| (1,4), (3,4), (4,5), (4,7) | 1 | 0; 2; 2; 2,152… |

## 6. Önellenőrzések

1. **Nyomösszeg:** mind a 24 kiszámolt hálón pontosan 64 — a nyom-döntetlen tétel fedezete (A4, 3.) áll.
2. **Nulla-módusok:** J1: 1, J2: 1, J3: 2 — az A4 előre regisztrált tényei szerint.
3. **Analitikus kontra gépezet:** legnagyobb eltérés $2 \cdot 10^{-15}$ (gépi pontosság).
4. **A J3 két független felépítése** (szövés-tag, ill. két külön kör) azonos létrát ad, $6 \cdot 10^{-15}$-ön belül.
5. **A J2 létrája pontosan a hiperkocka binomiális létrája** (0; 2×4; 4×6; 6×4; 8 — a fokok szélessége 1-4-6-4-1), gépi pontossággal: a [PKG-13-1](PKG-13-1-rulebook_hu.md) összeesési lemmájának független, spektrális megerősítése.

## 7. Megfigyelések (verseny-mentesek)

- A J2 létrája a legkevesebb fokból áll, a legszélesebb polcokkal — a szövés magas szimmetriájának ujjlenyomata.
- A J1 osztályáé a leglágyabb indulás az összefüggő szövések közt (0,738); minden más összefüggő családtag magasabban kezd.
- A pásztázás kötelezettsége fogott egyet: a családban **két** darabolt szövés él, különböző létrával — a (2,6)-os (két 8-as kör, első+harmadik szomszéd bekötéssel) a versenybe új darabolt jelöltként lép be. A 21 tag 7 létrába esik össze; a PKG-13-3 versenyébe ez a 7 megy.

## 8. Import-számla és ítélet

Új import: **nulla.** A csomag határa tartott: betöltési összeg nem számolódott. **Ítélet: áll.**

## 9. Kimenő állítások (a PKG-13-3 csak ezekre építhet)

- **B1:** a J1, J2, J3 létrái a 4. pont szerint — ezek a hivatkozási értékek.
- **B2:** a versenybe a pásztázás mind a 7 létra-osztálya belép, köztük a második darabolt szövés (2,6).
- **B3:** a PKG-13-3 köteles a létrákat függetlenül újraszámolni, és csak egyezés után versenyeztetni.
- **B4:** betöltési verseny e csomagban nem történt — a győztes-kérdés érintetlen.
