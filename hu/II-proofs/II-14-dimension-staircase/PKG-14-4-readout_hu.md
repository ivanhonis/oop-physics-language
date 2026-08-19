---
id: PKG-14-4
type: package
part_of: II-14
lang: hu
pair: PKG-14-4-readout_en.md
pair_status: in-sync
doc_version: "1.3"
status: jovahagyva
builds_on: [PKG-14-1, PKG-14-3, II-11]
imports: nulla
---

# PKG-14-4 — A hurok zárása: kiolvasás a győztesen (levezetés-csomag)

> **Helyreállítási jegyzet — olvasd el, mielőtt hivatkozol rá.** E fájl eredeti, jóváhagyott szövege elveszett: a helyén a [PKG-14-1](PKG-14-1-rulebook_hu.md) szabálykönyv másolata állt (a `!archive` mind a négy pillanatképében is), és a git-történetben sem őrződött meg. A jelen szöveg **helyreállítás**, három forrásból: a fennmaradt számoló kód (`shared/II-14-dimension-staircase/PKG-14-4-readout.py`), a rögzített jegyzőkönyv ([PKG-14-1](PKG-14-1-rulebook_hu.md), 8. pont) és a [PKG-14-3](PKG-14-3-race_hu.md) C4 bemenete. **Minden alább közölt szám újramérve** — nem másolat a próbafájlból —, és egyezik a [II/14](proof_hu.md) és a [PKG-14-5](PKG-14-5-readout-repeat_hu.md) által hivatkozott értékekkel. Amit a helyreállítás nem tud pótolni: az eredeti megfogalmazás. Ha az eredeti előkerül, ez a fájl cserélendő.

**Épít:** [PKG-14-3](PKG-14-3-race_hu.md) (C4), [PKG-14-1](PKG-14-1-rulebook_hu.md) (8. pont, A6), [II/11 visszarakó](../II-11-locality-readout/proof_hu.md) · **Számoló kód:** `PKG-14-4-readout.py`

---

## 1. Kérdés

A rögzített kiolvasási jegyzőkönyvvel visszaolvasható-e a győztesből (tér, 8×8×8, $N = 290$) a szövés, és a golyó a három hivatkozási sor közül a térét adja-e?

## 2. Bemenetek és gépezet-megjegyzés

A futás a PKG-14-1 8. pontja szerint: páros közelség a kész állapotból; a szomszédszámot a közelség-lista ugrása jelöli ki; zárt fokú töltés a tér-sávból ([PKG-14-3](PKG-14-3-race_hu.md), C4: $N = 290$, a középső 6-os polc betelése). Szabad kizáró példányoknál a nézetek a példány-korrelációkból egzaktul számolhatók — a [4. eszköz](../../appendix/B-machinery_hu.md) gyorsított alakja, új import nélkül: a közelség a kész állapot páronkénti egytest-térképe.

**Zárt fok ellenőrzés:** a 290. ütem 6,000000, a 291. 6,585786 — a rés **egzaktul $2 - \sqrt{2}$**; az állapot egyértelmű, vetítő nem kell.

## 3. A rögzített futás eredménye

**Közelség-osztályok** (a szövés minden helyéről azonosan, osztályon belüli szórás $10^{-12}$ alatt):

| Eltolás-osztály | Közelség | Eltolások |
|---|---|---|
| szomszéd (a 32 valódi irány, 1536 szerződés) | **+0,164895** | ×6 |
| **átellenes tükörpont (4,4,4)** | **+0,066406** | ×1 |
| testátló (1,1,1) | −0,054965 | ×8 |
| (1,2,2) | +0,020479 | ×24 |
| (0,0,2), (2,2,2), (2,4,4) | −0,019531 | ×6, ×8, ×6 |

- **Rezonancia-őrszem (a jegyzőkönyv előírt alakja):** a szomszéd-osztállyal **egzaktul** egyező másik osztály: **0 db** — az őrszem **nem jelzett**.
- **Az ugrás — és itt jegyzőkönyv-hézag nyílt.** A PKG-14-1 8. pontja az ugrást a közelség-listán kereste, de nem mondta ki, hogy az **előjeles** vagy az **abszolút értékes** listán. A kettő e szöveten **szétválik**:

| Ugrás-szabály | Ugrás | k* | Beemelt osztályok | Élek | Valódi | Fantom | Hiányzó |
|---|---|---|---|---|---|---|---|
| **előjeles** | a 7. hely után, 3,24-szeres | 7 | szomszéd + átellenes | 1792 | **1536/1536** | **256** | 0 |
| abszolút | a 15. hely után, 2,68-szeres | 15 | szomszéd + átellenes + testátló | 3840 | **1536/1536** | 2304 | 0 |

- **Golyónövekedés** (a visszarakott hálón, $r \le 3$): előjeles úton **1, 8, 32, 88**; abszolút úton 1, 16, 92, 296. A jegyzett hivatkozási sorok: vonal 1, 7, 13, 19 | sík 1, 7, 19, 37 | **tér 1, 7, 25, 63**.

## 4. Ítélet a jegyzőkönyv szerint: részleges bukás

A szövés **hiánytalanul visszaolvasható** — mind az 1536 valódi szerződés megvan, hiányzó nulla, mindkét ugrás-szabályon. De a győztes **nem választható el a saját átellenes visszhangjától**: a páros-jegyű szövés tükörpontja (4,4,4) a közelség-listán a valódi szomszédok mögé, de minden más osztály elé ül, és ezzel megnyeri az ugrás-versenyt — 256 fantom-él, teljes átellenes párosítás. A mért golyó ezért **1, 8, 32, 88**, nem a jegyzett tér-sor.

A bukás **nem romboló** és a [II/13](../II-13-dimension-race/proof_hu.md)-tól **eltérő fajtájú**: ott a visszhang a szomszéddal *egzaktul egyezett*, itt nem (0,066406 kontra 0,164895 — a szomszéd 40,3%-a). A hurok-zárás e méreten tehát **részlegesen bukott**, két külön rögzítendő tanulsággal:

1. **Az őrszem alakja szűk volt.** A jegyzőkönyv az „egzakt egyezés" alakjára írta elő a rezonancia-őrszemet; itt egzakt egyezés nincs, ezért az őrszem hallgatott — miközben a visszhang a rangsort mégis elrontotta. A helyes alak nem egyezés-próba, hanem **sáv-próba**: a leggyengébb elfogadott és a legerősebb elutasított közelség hányadosa.
2. **Előjel-hézag a jegyzőkönyvben.** Az ugrás-szabály nem mondta ki, előjeles vagy abszolút listán fut. E szöveten a kettő különböző k*-ot ad; a fenti fő számsor az előjeles olvasaté.

Mindkét tanulság **jegyzőkönyv-hiba, nem eredmény-hiba** — a szabálykönyv nem módosul, a helyesbítés a következő csomag dolga.

## 5. Diagnózis — az ítéleten kívül, külön címkével

A bukás okának ellenőrzése nagyobb szövésen (12×12×12, zárt fok a fél-töltéshez legközelebb felülről). Ez a rögzített 512-helyes hatókörön **kívül** esik, ezért nem az ítélet része, hanem annak magyarázata:

- zárt fok $N = 934$ (fél-töltés 864), a rés fölötte egzaktul $2 - \sqrt{3}$;
- a szomszéd-közelség +0,166146, az átellenes visszhang **−0,026620** — előjelet vált, és a szomszéd **16,0%-ára** esik;
- az ugrás élesen hatot jelöl: a 6. hely után, **8,9-szeres**;
- a visszarakás **5184/5184, fantom nulla, hiányzó nulla**;
- a golyó 1, 7, 25, 63, 129, 231 — a növekmény 6, 18, 38, 66, 102, **egzaktul $4r^2 + 2$, $r = 5$-ig**: a három kiterjedés mért növekedési törvénye.

**Jelölt következtetés:** a 8-as körbeérés átellenes visszhangja **méret-műtermék**; a mechanizmus a páros-jegy tükör-párosítása — ugyanaz a szimmetria, amely a versenyt a térnek megnyerte ([PKG-14-3](PKG-14-3-race_hu.md), C3), kis méreten a kiolvasását rontja. Nagyobb szövésen a hurok zárul, és a kiterjedés-olvasat éles.

## 6. Import-számla és ítélet a csomagról

Új import: **nulla.** A rögzített futás az előírt jegyzőkönyvvel, módosítás nélkül futott le; a bukás a szabály szerint, pontosan van rögzítve; a diagnózis külön címkével áll; a két jegyzőkönyv-tanulság kimondva. **A csomag áll.**

## 7. Kimenő állítások (a PKG-14-5 és a szintézis csak ezekre építhet)

- **D1:** a rögzített futás részlegesen bukott: 1536/1536 valódi él, hiányzó nulla, de 256 fantom-él (teljes átellenes párosítás); a mért golyó 1, 8, 32, 88 a jegyzett 1, 7, 25, 63 helyett.
- **D2:** a bukás oka azonosítva: az átellenes tükör-visszhang a páros-jegy kis-méretű ára — a II/13-as rezonanciától eltérően **nem** egzakt egyezés, hanem rangsor-elsőbbség.
- **D3:** két jegyzőkönyv-tanulság rögzítve: (i) az őrszem egyezés-alakja szűk, sáv-alak kell; (ii) az ugrás-szabály előjel-hézagos.
- **D4:** diagnózis (hatókörön kívül, jelölt): a 12-es szövésen tiszta visszarakás (5184/5184, fantom nulla) és egzakt $4r^2+2$ golyótörvény $r = 5$-ig.
- **D5:** a folytatás megnevezve: a diagnózis rögzített hatókörű ismétlése, a D3 két tanulságának beépítésével — a név **PKG-14-5**-re foglalva.
