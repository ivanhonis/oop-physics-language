---
id: PKG-14-3
type: package
part_of: II-14
lang: hu
pair: PKG-14-3-race_en.md
pair_status: missing
doc_version: "1.3"
status: jovahagyva
builds_on: [PKG-14-1, PKG-14-2]
imports: nulla
---

# PKG-14-3 — A betöltési verseny (levezetés-csomag)

**Épít:** [PKG-14-1](PKG-14-1-rulebook_hu.md) (A4, A5), [PKG-14-2](PKG-14-2-ladders_hu.md) (B1–B5) · **Számoló kód:** `PKG-14-3-race.py`

---

## 1. Kérdés

Melyik szövés nyeri a betöltési versenyt melyik példányszámnál, a rögzített kétsávos lépcső-szabály szerint?

## 2. A kötelező előfeltétel (B3): független újraszámolás

A létrák új kódúton (illeszkedési mátrixból: élenként egy sor, $L = B^{\mathsf T} B$) újraszámolva: mind a 223 hálón a nyomösszeg pontosan 3072; nulla-módusok a PKG-14-2 szerint (a négy deklarált háló 1-1, a pásztázók közt a 20 széteső); szúrópróba-értékek (0,0021; 0,0769; $2-\sqrt2$; a tér 12-es teteje) a hivatkozási értékekkel egyeznek. A verseny indulhatott.

## 3. Az eredmény — a fő olvasat: a deklarált hármas (J1–J2–J3)

| N példány | 1 | 2–129 | 130–255 | 256–511 | 512 |
|---|---|---|---|---|---|
| győztes | mind (0) | **J1 vonal** | **J2 sík** | **J3 tér** | mind (3072) |

Mindkét előírt sáv létezik és összefüggő: a sík-sáv **130–255**, a tér-sáv **256–511**. A határok élesek és szorosak: a vonal–sík váltásnál (N = 129 → 130) a különbség 0,2 ezrelék alatti (303,512 / 303,691, majd 309,400 / 308,234); a sík–tér váltás (N = 255 → 256) még szorosabb (1022,788 / 1023,442, majd 1029,616 / 1029,442). Jellemző mélységek: N = 64-nél a vonal 43,7 a sík 80,8 és a tér 127,9 ellenében; N = 384-nél a tér 1903,5 a sík 1994,7 és a vonal 2015,7 ellenében.

**Ítélet a rögzített 7. szabály szerint: IGEN — a lépcső mindkét foka áll.** Ritkán a vonal, közepes sűrűségen a sík, magas sűrűségen a tér a legolcsóbb: a kiterjedés a sűrűséggel lépcsőzik.

**Előre regisztrált tények:** mindhárom áll (N = 1 mindenki 0; N = 512 döntetlen 3072-n; a nulla-módusok a PKG-14-2 helyesbítése szerint).

## 4. A sáv-határok szerkezete — a héj-várakozás ellenőrzése

- **A tér pontosan fél-töltésnél veszi át a versenyt** (N = 256) — és ez **nem fokhatár**: a tér 6-os költségű, 68 ütem széles középső polca a 223–290 tartományt fedi, a fél-töltés ennek a **közepe** (256,5). A mechanizmus a **páros-jegy**: a tér létrája a 6 körül egzaktul szimmetrikus és a legszélesebb (0-tól 12-ig) — a felső féltekén az nyer, akinek a tükre a legtávolabb tolja a magas ütemeket. A szabálykönyv 6. pontjának héj-várakozása itt tehát **nem teljesült**: a sík–tér határt nem fokbetelés, hanem a tükör-szimmetria dönti.
- A vonal–sík határ (130) a sík 129-es fokhatára mellé esik, de a sík fokhatárai ott sűrűek (…125, 129, 131…), így ez legfeljebb gyenge jel — a héj-illeszkedési jelölt szabály ([III/1, 6.](../../III-frontier/III-01-candidate-laws_hu.md)) pontosításra szorul: kis rendszeren (II/13) a fokbetelés döntött, itt a tükör.

## 5. A teljes mezőny — a szigorú győztesek

**A deklarált szövések a teljes mezőnyben sehol sem szigorú győztesek.** Minden töltésnél a vonal-család egy hangolt tagja a legolcsóbb; a mezőny rezsimjei:

- **Alsó sáv (2–124): fésű.** A vonal-osztály a saját széteső többszörözéseivel váltakozik — a (2,4,6) két, a (4,8,12) négy példánya ugyanannak a vastagított vonalnak kisebb körön; a (4,8,12) az N ≡ 4 (mod 8), a (2,4,6) az N ≡ 2 (mod 4) töltéseket viszi, a páratlanokat az összefüggő vonal. Fok-rezonancia a legtisztább alakjában: a többszörözött polcok a páros töltéseknél telnek pontosan.
- **Középső sáv (125–236): kereszt-vonalak** — a II/13 jelenségének tömeges mása: az (1,5,6), (1,4,5), (2,3,5) és társaik a síkot mindenütt megelőzik.
- **Felső sáv (237–511): a páros-jegy uralma.** A győztesek csupa-páratlan lépésű vonalak — ezek maguk is páros hálók, 12-es tetővel — és széteső párjaik; az N = 511-es holtverseny 22 tagjából 20 csupa-páratlan vonal, plusz a tér és a (2,6,10). **A tér hátránya a mezőny-győztessel szemben végig kicsi: 0,3–2,2%** (N = 300-nál 1,7%, N = 500-nál 0,3%).

A lelet kimondva: a lépcső a **geometria-képviselők** versenyén áll; a teljes családban az egykiterjedésű szövés elegendő hangolási szabadsággal minden töltésen utoléri és százalék-skálán veri a magasabb kiterjedést — és a felső féltekét eldöntő páros-jegy vonalon is előállítható (csupa-páratlan lépéssel). A kiterjedés előnye tehát valódi, de vékony, és a hordozója a tükör-szimmetria.

## 6. Import-számla és ítélet

Új import: **nulla.** Utólagos szabálymódosítás nem történt; a pásztázók győzelmei a rögzített mezőny részei; a héj-várakozás elmaradása kérdésként volt regisztrálva, nem jóslatként. **Ítélet: áll.**

## 7. Kimenő állítások (a PKG-14-4 és a szintézis csak ezekre építhet)

- **C1:** a hármas győztes-táblája a 3. pont szerint; sáv-határok: 129/130 és 255/256.
- **C2:** fő olvasat: **igen** — teljes lépcső: vonal 2–129, sík 130–255, tér 256–511, mindkét előírt sáv összefüggő.
- **C3:** a tér-sáv pontosan fél-töltésnél kezdődik, a középső tükör-polc közepén — a mechanizmus a páros-jegy, nem fokbetelés; a héj-illeszkedési jelölt szabály ennek fényében pontosítandó.
- **C4:** a PKG-14-4 (kiolvasás) a J3-on, **N = 290**-nél fut: a tér-sáv első zárt foka (a középső polc betelése; fölötte 0,586-os rés) — az állapot egyértelmű, vetítő nem kell.
- **C5:** teljes-mezőny lelet: a deklarált szövések sehol sem szigorú mezőny-győztesek; a tér hátránya 0,3–2,2%; az alsó fésű, a kereszt-vonalak és a felső páros-jegy-uralom rögzítve.
