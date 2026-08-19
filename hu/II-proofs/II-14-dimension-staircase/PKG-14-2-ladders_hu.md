---
id: PKG-14-2
type: package
part_of: II-14
lang: hu
pair: PKG-14-2-ladders_en.md
pair_status: in-sync
doc_version: "1.4"
status: jovahagyva
builds_on: [PKG-14-1]
imports: nulla
---

# PKG-14-2 — Az ütem-létrák (levezetés-csomag)

**Épít:** [PKG-14-1](PKG-14-1-rulebook_hu.md) (A1–A4, A7) · **Nem tartalmaz:** betöltési versenyt — a létrák itt csak kiszámolódnak, a verseny a PKG-14-3 dolga. · **Számoló kód:** `PKG-14-2-ladders.py`

---

## 1. Kérdés

Mi a három jelölt, a sík-kontroll és a teljes rögzített pásztázás ($a<b<c\le12$, 220 családtag) ütem-létrája, két független módszerrel ellenőrizve?

## 2. Bemenetek

PKG-14-1: A1 (rendszer), A2 (mezőny és pásztázás), A3 (költségdefiníció), A4 (előre regisztrált tények), A7 (páros-jegy önellenőrzés). Gépezet: a hálózati ütem-létra sajátfeladata ([B függelék](../../appendix/B-machinery_hu.md), 2. eszköz) és a szövések zárt Fourier-alakja mint független ellenőrzés.

## 3. A számolás

Mind a **224 háló** létrája kétszer számolódik: a szerződésháló szomszédlistás mátrixának sajátfeladataként (gépezet) és a szövések zárt képletéből (Fourier-alak).

## 4. Eredmény — a mezőny létrái (költség csatolásegységben; ×n = polcszélesség)

| Háló | A létra eleje | Polcok | Tető |
|---|---|---|---|
| **J1 — vonal** | 0; 0,0021 (×2); 0,0084 (×2); 0,0190 (×2); 0,0337 (×2); … | 255 | 8,631 |
| **J2 — sík (16×32)** | 0; 0,0769 (×2); 0,2291 (×2); 0,3045 (×6); 0,5277 (×4); … | 94 | 8,988 |
| **J3 — tér (8×8×8)** | 0; 0,5858 (×6); 1,172 (×12); 1,757 (×8); 2 (×6); 2,586 (×24); … | 25 | 12 |
| **sík-kontroll (8×64)** | 0; 0,0193 (×2); 0,0769 (×2); 0,1722 (×2); 0,3045 (×2); … | 122 | 8,945 |

**A J3 teljes létrája** (25 polc): 0; 0,5858 (×6); 1,172 (×12); 1,757 (×8); 2 (×6); 2,586 (×24); 3,172 (×24); 3,414 (×6); 4 (×39); 4,586 (×60); 5,172 (×12); 5,414 (×24); 6 (×68); 6,586 (×24); 6,828 (×12); 7,414 (×60); 8 (×39); 8,586 (×6); 8,828 (×24); 9,414 (×24); 10 (×6); 10,24 (×8); 10,83 (×12); 11,41 (×6); 12 (×1). **Fokhatárai (zárt fokok):** 1, 7, 19, 27, 33, 57, 81, 87, 126, 186, 198, 222, 290, 314, 326, 386, 425, 431, 455, 479, 485, 493, 505, 511, 512.

## 5. A pásztázás — 220 családtag, és amit fogott

- A 220 tag **216 különböző létrába** esik; a négy egybeeső pár mindegyike lépéskészlet-átszámozás (a lépések hárommal szorzása — a 3 az 512-höz relatív prím, tehát ugyanaz a szövés átcímkézve). Köztük maga a J1 is: az (1,2,3) és a (3,6,9) azonos háló.
- **A pásztázás fogása — a rögzített A4 2. pontja a családra nem áll.** A deklarált mezőnyre igen (J1, J2, J3 és a kontroll mind összefüggő, pontosan 1-1 nulla-módussal — lásd 6. pont), de a pásztázott családban **20 széteső szövés él**: pontosan azok a hármasok, amelyeknek minden lépése páros — 19 tag két komponensre, a (4,8,12) négyre esik. Az A4-be írt kiterjesztés („minden induló összefüggő") levezetési tévedés volt; a szabálykönyv nem módosul, a helyesbítés itt és a szintézisben rögzül. Következmény a versenyre: az alacsony töltésű széteső-előny (komponensenként egy ingyen nulla-módus — II/13) **mégis játszik**, a mezőny rögzített tagjaként.

## 6. Önellenőrzések

1. **Nyomösszeg:** mind a 224 hálón 3072, eltérés $10^{-12}$ alatt — a nyom-döntetlen fedezete (A4, 3.) áll.
2. **Nulla-módusok:** J1: 1, J2: 1, J3: 1, kontroll: 1 (A4, 2. a deklarált mezőnyre áll); a pásztázókon a nulla-módusok száma pontosan a lépések és az 512 közös osztója (200 tag: 1; 19 tag: 2; egy tag: 4).
3. **Gépezet kontra zárt képlet:** legnagyobb eltérés $7{,}9\cdot10^{-14}$ (gépi pontosság), mind a 224 hálón.
4. **A páros-jegy (A7):** a J3 létrája a 6 körül **egzaktul szimmetrikus** (eltérés $1{,}8\cdot10^{-15}$), a J1-é és a J2-é nem (eltérés 3,37 ill. 3,01) — a három jelölt páronként különböző háló, a II/13-as összeesési csapda itt bizonyítottan nem áll fenn.

## 7. Megfigyelések (verseny-mentesek)

- A J3 létrája a legkevesebb polcból áll (25), a legszélesebbekkel (a 6-os polcon 68 ütem) — a tér-szövés magas szimmetriájának ujjlenyomata; teteje a 12, a páros háló kötelező tükre.
- A J1 indulása kirívóan lágy (0,0021): a vastagított vonal hosszú hullámai szinte ingyen vannak — alacsony töltésen ez lesz az ereje.
- A nyújtás lágyít: a 8×64-es kontroll létrája mélyebben indul (0,0193), mint a 16×32-esé (0,0769) — a sík a nyújtott alakjában „vonalasodik".

## 8. Import-számla és ítélet

Új import: **nulla.** A csomag határa tartott: betöltési összeg nem számolódott. **Ítélet: áll** — az 5. pont fogásával együtt, amely nem a csomag hibája, hanem a pásztázás kötelezettségének hozadéka.

## 9. Kimenő állítások (a PKG-14-3 csak ezekre építhet)

- **B1:** a J1, J2, J3 és a kontroll létrái a 4. pont szerint — ezek a hivatkozási értékek.
- **B2:** a versenybe a teljes rögzített mezőny lép: a négy deklarált háló és a pásztázás mind a 216 létra-osztálya, köztük a 20 széteső taggal — az A4 2. pontjának helyesbítése (5. pont) a szintézisben kötelezően jelentendő.
- **B3:** a PKG-14-3 köteles a létrákat új kódúton függetlenül újraszámolni, és csak egyezés után versenyeztetni.
- **B4:** betöltési verseny e csomagban nem történt — a győztes-kérdés érintetlen.
- **B5:** a héj-logika ellenőrzéséhez a J3 fokhatárai a 4. pont szerint rögzítve.
