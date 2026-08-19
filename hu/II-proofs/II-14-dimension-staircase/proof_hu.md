---
id: II-14
type: proof
lang: hu
pair: proof_en.md
pair_status: in-sync
doc_version: "1.4"
status: ervenyes
builds_on: [II-13, II-12, II-11, I-06]
imports: "nulla új tétel (a versenyszabály és a helyek egyenrangúsága a II/12–II/13-ból örökölt, deklarált konvenciók)"
packages: [PKG-14-1, PKG-14-2, PKG-14-3, PKG-14-4, PKG-14-5]
---

# II/14. A kiterjedés-lépcső — igen, kiolvasási korláttal

**A kérdés.** A [III/2, 8.](../../III-frontier/III-02-open-questions_hu.md) célpróbája a II/13 után: azonos helyenkénti szerződésszám (hat) mellett lépcsőzik-e a kiterjedés a sűrűséggel — ritkán vonal, közepén sík, magas sűrűségen tér? A próba a csomag-módszerrel készült ([D függelék](../../appendix/D-package-method_hu.md)); a szabálykönyv rögzítése *előtt* egy hibát is javítani kellett: a III/2, 8. a tér golyótörvényét lineárisnak jegyezte ($+{\sim}6r$), holott az négyzetes ($4r^2+2$) — a javítás a jegyzőkönyv-építés előtt megtörtént, kimondva ([PKG-14-1](PKG-14-1-rulebook_hu.md)).

**A rendszer és a szerződés.** 512 hely; 1536 egységnyi simasági szerződés, helyenként pontosan hat; minden jelölt szövés-háló, minden körbezárt irány oldalhossza legalább 8 (a II/13 rezonancia-diagnózisának öröksége). Jelöltek: **vonal** (512-es kör 1-2-3 lépésű bekötéssel), **sík** (16×32-es háromszög-szövés), **tér** (8×8×8-as kockaszövés); kontroll a 8×64-es nyújtott sík; kötelező pásztázás: a vonal-család mind a 220 hármas-bekötése a 12-es lépésig (rögzített, kimondott korlát).

**A létrák.** Mind a 224 háló létrája két független úton (a gépezet sajátfeladata és a szövések zárt Fourier-alakja), egyezés $7{,}9\cdot10^{-14}$-en belül; a nyomösszeg mindenütt pontosan 3072. A jelölt-különbözőség itt nem feltevés, hanem bizonyítás: a tér **páros háló** — létrája a 6 körül egzaktul szimmetrikus ($10^{-15}$), a vonalé és a síké nem — a II/13-as összeesési csapda nem áll fenn. A pásztázás kétszer fogott: a családban 20 széteső szövés él (minden lépésük páros — a szabálykönyv „minden induló összefüggő" levezetése tévedés volt, a helyesbítés a [PKG-14-2](PKG-14-2-ladders_hu.md)-ben áll), és a 220 tag 216 létra-osztályba esik (a négy egybeesés lépés-átszámozás, nem elfajulás).

**Az eredmény — a verseny** (független újraszámolás után, [PKG-14-3](PKG-14-3-race_hu.md)):

| N példány | 1 | 2–129 | 130–255 | 256–511 | 512 |
|---|---|---|---|---|---|
| győztes a hármason | mind (0) | **vonal** | **sík** | **tér** | mind (3072) |

**A rögzített kétsávos szabály szerint az ítélet: igen — a lépcső mindkét foka áll, összefüggően.** A kiterjedésszám a sűrűséggel lépcsőzik. És a döntő határ szerkezete kimondható: **a tér pontosan fél-töltésnél veszi át a versenyt** (N = 256) — nem fokhatáron, hanem a 68 ütem széles középső polcának a *közepén*. A mechanizmus a **páros-jegy**: a felső féltekén az nyer, akinek a létrája szimmetrikus és a legszélesebb — a tükör tolja legmagasabbra a betöltetlen ütemeket. A héj-illeszkedési jelölt szabály ezzel pontosítandó: kis rendszeren (II/13) és az alsó fésűben a fokbetelés dönt, a sík–tér határt a tükör ([III/1, 6–7.](../../III-frontier/III-01-candidate-laws_hu.md)). *Teljes mezőny, őszintén:* a deklarált szövések sehol sem szigorú mezőny-győztesek — minden töltésen a vonal-család egy hangolt tagja a legolcsóbb, a tér hátránya végig 0,3–2,2%; alacsony töltésen a vonal a saját széteső többszörözéseivel váltakozik szabályos fésűben, a teli véget a csupa-páratlan lépésű (maguk is páros-jegyű) vonalak viszik. **A kiterjedés előnye valódi, de vékony, és a hordozója a tükör-szimmetria — amely vonalon is előállítható.**

**Az eredmény — a kiolvasás** ([PKG-14-4](PKG-14-4-readout_hu.md)). A győztesen (tér, N = 290, zárt fok) a visszarakó mind az 1536 valódi szerződést megtalálta, hiányzó nélkül — de a rögzített ugrás-szabály az átellenes tükörpontot is beemelte: 256 fantom-él (teljes átellenes párosítás), a mért golyó 1, 8, 32, 88 a jegyzett 1, 7, 25, 63 helyett. **A hurok-zárás e méreten részlegesen bukott** — nem rombolón, és a II/13-tól eltérő módon: egzakt egybeesés nincs (az őrszem nem is jelzett — az „egzakt egyezés" alakja szűknek bizonyult), a visszhang az ugrás-versenyt nyerte meg; emellett jegyzőkönyv-hézag rögzült (előjeles kontra abszolút-értékes ugrás). A diagnózis (hatókörön kívül, jelöltként): 12×12×12-n az ugrás élesen hatot jelöl (8,9-szeres), a visszarakás 5184/5184 fantom nélkül, és a golyónövekmény 6, 18, 38, 66, 102 — **egzaktul $4r^2+2$, a három kiterjedés mért növekedési törvénye, $r=5$-ig**; a visszhang a mérettel elhal. A mechanizmus kimondva: az átellenes visszhang a páros-jegy tükör-párosítása — **ugyanaz a szimmetria, amely a versenyt a térnek megnyerte, kis méreten a kiolvasását rontja.** A diagnózis azóta rögzített hatókörű ismétléssel igazolva: a 12-es szövésen mind a négy előre rögzített feltétel áll, a visszhang a szomszéd-közelség 16%-ára esik — a méret-műtermék jelöltből tétel ([PKG-14-5](PKG-14-5-readout-repeat_hu.md)).

**Ellenőrzés a valóságon.** Belső verseny, közvetlen mért célpont nélkül; két mért visszhangja: a sűrűség-/nyomásvezérelt szerkezetváltások standard jelensége (itt a legkisebb, egzakt lépcső-alakban), és a fél-töltési részecske-lyuk szimmetria páros rácsokon (standard tétel) — a tükör-mechanizmus mért rokona ([C függelék](../../appendix/C-benchmarks_hu.md)).

**Import-számla:** nulla új tétel; a pásztázás kötelezettsége fogott (széteső családtagok — a szabálykönyv egy levezetési tévedése helyesbítve), a jegyzőkönyv két szabály-tanulsága rögzítve. **Mit igazolt:** teljes lépcső-ítélet — a kiterjedés sűrűségfüggő, és a sűrűséggel lépcsőzik; a tükör-szabály új jelölt ([III/1, 7.](../../III-frontier/III-01-candidate-laws_hu.md)); a héj-illeszkedés hatóköre pontosítva; a tér négyzetes olvasata nagy szövésen egzaktul mérve (a rögzített hatókörű ismétlés után tételként — [PKG-14-5](PKG-14-5-readout-repeat_hu.md)); és a mezőny-lelet gyökér-jelzése: a vékony előny és a hangolható vonal-imitáció miatt a kiválasztás szabad hálón nem dőlhet el — ott dőlhet el, ahol a szerződések születnek ([III/2, 7.](../../III-frontier/III-02-open-questions_hu.md)). Bővítési irány: a következő fok (tér kontra négykiterjedés, koordináció nyolc, elég nagy szövésen) — a kiolvasás rögzített hatókörű ismétlése a 12-es szövésen elkészült és áll ([PKG-14-5](PKG-14-5-readout-repeat_hu.md)).
