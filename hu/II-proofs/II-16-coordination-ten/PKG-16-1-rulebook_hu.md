---
id: PKG-16-1
type: package
part_of: II-16
lang: hu
pair: PKG-16-1-rulebook_en.md
pair_status: missing
doc_version: "1.3"
status: jovahagyva
builds_on: [II-15, II-14, II-12, II-11, I-06]
imports: "a kiválasztási szabály (kimondott konvenció, 9. szakasz)"
---

# PKG-16-1 — A tízes koordináció szabálykönyve (levezetés-csomag)

**Számolást nem tartalmaz** — a szabályokat rögzíti minden számolás előtt; utólag nem módosítható.

## 1. Kérdés (egy mondat, előre rögzítve)

Tízes koordináción — ahol a honos fok az öt — felmegy-e a lépcső a honosig, és **hová fordul vissza a tetején**: megint a háromra, a tükör-jegy egyetlen hordozójára (itt épp a honos ötre), vagy máshová?

## 2. Bemenetek

A II/12–II/15 teljes öröksége, kiemelten: a kizárás tétele (I/6); a nyom-döntetlen (II/12); a **lyuk-tükör tétel** ([PKG-15-5](../II-15-dimension-fourth-rung/PKG-15-5-hole-mirror_hu.md)); az **irány-tétel** gépezete a rendezési, átfordítási és szendvics-lemmával ([PKG-15-6](../II-15-dimension-fourth-rung/PKG-15-6-direction_hu.md)); a tető-tétel mintája ([PKG-15-7](../II-15-dimension-fourth-rung/PKG-15-7-top_hu.md)); a visszhang-számsor (a 12-es körbeérés elégséges — [PKG-14-5](../II-14-dimension-staircase/PKG-14-5-readout-repeat_hu.md), [PKG-15-4](../II-15-dimension-fourth-rung/PKG-15-4-readout_hu.md)); és a II/15 három helyesbítés-tanulsága **szabállyá emelve**: duplázásbiztos bekötés-építés gépi elem-egyediség-állítással (H1), a páros-körbeérés követelmény csak a páros-jegyű indulókon (H2), az elsődleges számolási út hosszú-lebegős (H3).

## 3. A rögzített rendszer

- **248 832 hely** (= 12⁵); **1 244 160 egységnyi simasági szerződés, helyenként pontosan tíz.**
- Minden induló szövés-háló; minden körbezárt irány körbeérése **legalább 8 gráf-lépés, gépi bejárással igazolva**; a **páros-jegyű** indulókon a körbeérés páros is.
- Költség: a létra alulról töltése, N = 1-től 248 832-ig; **az elsődleges út hosszú-lebegős**, az azonosság-tűrés 10⁻⁸.

## 4. A mezőny

| Jelölt | Szövés | Bekötés (fél-lépések) | Legrövidebb oldal |
|---|---|---|---|
| **J1 — vonal** | 248 832-es kör | 1, 2, 3, 4, 5 | — |
| **J2 — sík** | 432×576 | (1,0), (0,1), (1,1), (1,−1), (0,2) | 432 |
| **J3 — tér** | 54×64×72 | tengelyek + (0,1,−1), (0,1,1) | 54 |
| **J4 — négykiterjedés** | 18×24×24×24 | tengelyek + (0,0,1,−1) | 18 |
| **J5 — ötkiterjedés (honos)** | 12⁵ | egységlépések | 12 |

**Kontrollok (versenyeznek, kiolvasást nem kapnak):** K1 tér-alak 48×72×72; K2 négykiterjedés nyújtva 12×24×24×36; K3 sík nyújtva 288×864; KA2/KA3/KA4 — a döntetlen-törő önkényének kontrolljai (a plusz-lépés a másik oldal-párra fektetve); **KP3 páros tér** (tengelyek + két testátló-pár); **KP4 páros négykiterjedés** (tengelyek + (0,1,1,1)-pár).

**Becsületességi pásztázás:** a vonal-család mind a 792 ötös-bekötése (1 ≤ a < b < c < d < e ≤ 12); a plafon kimondott határ, a II/14–II/15-ével azonos.

## 5. Levezetett előzetes tények

**Golyótörvények (hivatkozási sorok; a héjak r = 2-től szétválnak: 10 / 22 / 34 / 44 / 50):**

| Jelölt | Héj-növekmény | A golyó sora (r = 0..5) |
|---|---|---|
| vonal | 10 | 1, 11, 21, 31, 41, 51 |
| sík | 12r − 2 | 1, 11, 33, 67, 113, 171 |
| tér | 8r² + 2 | 1, 11, 45, 119, 249, 451 |
| négykiterjedés | 2r(2r² + 3) | 1, 11, 55, 181, 461, 991 |
| ötkiterjedés | kombinatorikus zárt alak (negyedrendű) | 1, 11, 61, 231, 681, 1683 |

**Jegy-tábla (két úton igazolva, duplázásbiztos leszámlálóval):** hármas-séták 60 / 42 / 24 / 12 / 0 — **ez az egy jegy mind a tíz fő párt szétválasztja**; négyes-séták 590 / 414 / 318 / 270 / 270 (a J4–J5 egyezés ártalmatlan). **A párosság-lelet:** tízes koordináción egyedül a honos foknak van teljes irány-szimmetriájú és egyben páros-jegyű szövése — a J2–J4 aszimmetriája és háromszögessége a koordináció kényszere; a tükör-kérdést a KP3, KP4 kontrollok és a hat csupa-páratlan lépésű családtag hordozza.

**Szétesés-tábla:** 786 ép + 6 kétpéldányos (a csupa-páros tagok); nulla-módus = példányszám; hárompéldányos tag nincs.

## 6. Előre regisztrált tények és kérdések

Tételből: N = 1-nél mind a 805 induló nullán; N = 2-nél hatos holtverseny nullán; **N = 3-nál — eltérés a II/15-től — nulla-költségű induló már nincs**; N = 248 832-nél kötelező döntetlen **2 488 320**-on.

**Jóslat tudatosan nincs.** Regisztrált kérdések: **(K-a, a próba fő kérdése)** a tető hovatartozása — a II/14–II/15 két olvasata itt szétválik: ha „a tükör uralja a tetőt", a tető az egyetlen tükör-jegyű fő jelölté, az ötkiterjedésű honosé; ha „a tető az alacsony kiterjedésé", nem-páros fok viszi, és a tükör-szabály (III/1, 7.) hatóköre szűkül; **(K-b)** fésű-minta az alsó tartományban (a hatos széteső-készlettel); **(K-c)** a dominancia-hézag ~fele aránya ismétlődik-e; **(K-d)** héj-illeszkedés a sávhatárokon.

## 7. Ítélet-szabály (rögzítve)

Minden N-re a szigorúan legkisebb költségű nyer (tűrés 10⁻⁸, hosszú-lebegős úton); holtverseny holtversenyként. **A fő kérdés a J1–J5 ötösön dől — négyfokú lépcső-ítélet:** teljes igen, ha négy összefüggő, érdemi sáv áll növekvő sűrűséggel, rendre a J2, J3, J4, J5 győzelmével a másik négy fölött. Néven nevezett részleges esetek: **„megáll a négynél"**, **„megáll a háromnál"**, és — a II/15 precedense nyomán előre látva — **„a lépcső a tetején visszafordul"**, ilyenkor a mért sorrend maga az ítélet szövege, a visszafordulás célfokának megnevezésével. Egyéb részleges a meglévő sávokkal; nem, ha sávszerkezet nem áll össze; foltos kimenet foltokkal. A pásztázók és kontrollok a teljes-mezőny olvasatban. Utólagos módosítás kizárva.

## 8. A kiolvasási jegyzőkönyv

A II/15 §8 rendje változatlanul — előjeles ugrás (30-as ablak), sáv-őrszem (küszöb 2), átellenes-sor kötelező a páros győztesen, teljesség-számla az 1 244 160 szerződésre, golyó-ítélet r ≤ 3, jelentés r ≤ 5 (a J5-ön a 12-es körbeérésen éppen érvényes) — **egy cserével: a vetítő-pecsét új, mintavételes ritka alakot kap** (9. szakasz), mert a sűrű sajátfeladat e méreten elvből kizárt. Zárt fok választása: a nyerő sáv legszélesebb rései közül a fél-töltéshez legközelebbi felülről. Bukás-ág: részleges ítélet a mechanizmus megnevezésével; a folytatás neve PKG-16-6-ra foglalva.

## 9. Import-számla és a kétutas szabály új alakja

**Új, kimondott konvenció — a kiválasztási szabály:** (i) a honos fok a csupasz egységlépéseké; (ii) minden más fokon a legkisebb össz-lépésnégyzetű öt ±pár indul, lexikografikus döntetlen-törővel. Őszinte jegyzet: a szabály a nyolcas koordinációra visszavetítve a vonalat, a király-síkot és a hiperkockát visszaadja, a II/15 tér-jelöltjénél viszont a kristálytani BCC helyett tengelyek+lapátlót adna — a különbség kimondva; itt ütközés nincs, mert egy-pályás alternatíva csak a honos fokon létezik.

**A kétutas szabály négyelemű ritka alakja** (a sűrű út 495 GB és hónapok volna): (i) **ritka maradék-próba** — a felépített háló kontra a zárt képlet, hálónként 64 sorsolt módus a fő/kontroll indulókon és 16 módus 24 sorsolt családtagon; (ii) **momentum-fedezetek** rend ≤ 4 minden indulón (a létra hatványösszegei kontra a kombinatorikus séta-számok — egyben a jegy-tábla önellenőrzése); (iii) **kis-példányos sűrű hitelesítés** — minden bekötés-minta 12-oldalú kis változata teljes sűrű úton; (iv) **mintavételes vetítő-pecsét** a kiolvasásnál (betöltött és üres módusok maradéka, 64 + 64 sorsolt módus). Sorsolási mag mindenütt: **248 832**. Kimondva: ez gyengébb a II/15 teljes sűrű pecsétjénél; a lefedettség számmal jelentendő.

## 10. Ítélet erről a csomagról

**Áll.** Érdemi előzetes eredményei: a párosság-lelet (a tükör-kérdés döntő kísérletté élesítése), az egy-jegyes különbözőség-bizonyítás, és az öt golyótörvény.

## 11. Kimenő állítások

- **A1:** rendszer = 3. szakasz; **A2:** mezőny = 4. szakasz (5 + 8 + 792 induló); **A3:** költség hosszú-lebegős úton, tűrés 10⁻⁸; **A4:** regisztrált tények a 6. szakasz szerint; **A5:** ítélet-szabály a 7. szakasz szerint, a néven nevezett visszafordulás-esettel; **A6:** kiolvasási jegyzőkönyv a 8. szakasz szerint; **A7:** kötelező önellenőrzések — jegy-tábla két úton, létra-osztályozás a teljes mezőnyön (tűrés 10⁻⁸), gépi körbeérés-bejárás minden indulón, nyomösszeg 2 488 320 mindenütt, komponensszám a szétesés-tábla ellen, bekötés-egyediség gépi állítása minden hálón; **A8:** a kétutas szabály a 9. szakasz négyelemű alakjában, rögzített mintaméretekkel és maggal.
