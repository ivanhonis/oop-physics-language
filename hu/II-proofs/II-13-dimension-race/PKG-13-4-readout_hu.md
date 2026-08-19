---
id: PKG-13-4
type: package
part_of: II-13
lang: hu
pair: PKG-13-4-readout_en.md
pair_status: missing
doc_version: "1.3"
status: jovahagyva
builds_on: [PKG-13-1, PKG-13-3, II-11]
imports: nulla
---

# PKG-13-4 — A hurok zárása: kiolvasás a győztesen (levezetés-csomag)

**Épít:** [PKG-13-3](PKG-13-3-race_hu.md) (C4), [PKG-13-1](PKG-13-1-rulebook_hu.md) (8. pont, A6), [II/11 visszarakó](../II-11-locality-readout/proof_hu.md) · **Számoló kód:** `PKG-13-4-readout.py`

---

## 1. Kérdés

A rögzített kiolvasási jegyzőkönyvvel visszaolvasható-e a győztesből (sík, $N = 11$) a szövés?

## 2. Bemenetek és gépezet-megjegyzés

A futás a PKG-13-1 8. pontja szerint: páros közelség a kész állapotból; a szomszédszámot a közelség-lista ugrása jelöli ki; zárt fokú töltés ($N = 11$, fokköz 2 — az állapot egyértelmű). Szabad kizáró példányoknál a nézetek a példány-korrelációkból egzaktul számolhatók — ez a [4. eszköz](../../appendix/B-machinery_hu.md) gyorsított alakja erre az esetre, új import nélkül.

## 3. A rögzített futás eredménye

**Közelség-osztályok** (a szövés minden helyéről azonosan, szórás $10^{-16}$):

| Eltolás-osztály | Korreláció |
|---|---|
| szomszéd (a 32 valódi szerződés) | **+0,1875** |
| átellenes-átló (2,2) | **+0,1875 — egzaktul azonos** |
| minden más | −0,0625 |

- **Az ugrás:** a rendezett közelség-lista 0,1723-ról 0,0183-ra esik (kilencszeres) — de csak az **ötödik** hely után: a jegyzőkönyv $k = 5$-öt jelöl ki.
- **Visszarakás:** mind a 32 valódi él megvan, hiányzó nincs — de mellettük **8 fantom-él** (mind átellenes-átló), a valódiaktól **megkülönböztethetetlen** közelséggel.
- **Golyónövekedés:** mért 1, 6, 16 — a jegyzett tórusz-sor (1, 5, 11, 15, 16) helyett.

## 4. Ítélet a jegyzőkönyv szerint: részleges bukás

A szövés hiánytalanul visszaolvasható, de **nem választható el a saját körbeérési visszhangjától**: ezen a méreten a győztes zárt fokán a háló és a visszhangja egzaktul egybeesik a közelség-térképen. A PKG-13-1 óvatossága (A6: a kettő-vagy-négy kérdés e méreten nem állítható) kiterjesztendő: e méreten a **tiszta** szövés-olvasat sem állítható. A bukás nem romboló: hamis geometria nem íródott a valódi helyébe — a valódi fölé íródott egy egzakt rezonancia-párosítás.

## 5. Diagnózis — az ítéleten kívül, külön címkével

A bukás okának ellenőrzése nagyobb szövésen (8×8 tórusz, zárt fok $N = 43$, töltés 0,672 — a rögzített futás 0,688-ának megfelelője). Ez a rögzített 16-helyes hatókörön **kívül** esik, ezért nem az ítélet része, hanem annak magyarázata:

- a szomszéd-közelség itt **szigorúan** domináns (2,07-szeres a következő osztályhoz képest);
- az ugrás $k = 4$-et jelöl ki; a visszarakás **128/128 él, fantom nulla**;
- a golyónövekedés: 1, 5, 13, 25, 39, … — a növekmény 4, 8, 12: **lépésenként $+4r$**, a két kiterjedés mért törvénye (a vonal állandó $+2$-jével szemben), amíg a szövés körbe nem ér.

**Jelölt következtetés:** a 16-helyes rezonancia méret-műtermék; nagyobb szövésen a hurok zárul, és a kiterjedés-olvasat éles.

## 6. Import-számla és ítélet a csomagról

Új import: **nulla.** A rögzített futás az előírt jegyzőkönyvvel, módosítás nélkül futott le; a bukás a szabály szerint, pontosan van rögzítve; a diagnózis külön címkével áll. **A csomag áll.**

## 7. Kimenő állítások (a szintézis csak ezekre építhet)

- **D1:** a rögzített futás részlegesen bukott: 32/32 valódi él + 8 fantom-él, egzaktul azonos közelséggel; a mért golyó nem a jegyzett sor.
- **D2:** a bukás oka azonosítva: körbeérési rezonancia a győztes zárt fokán — méretfüggő jelenség.
- **D3:** diagnózis (hatókörön kívül, jelölt): 8×8-on tiszta visszarakás és $+4r$ golyótörvény.
- **D4:** a szintézis a [II/13](proof_hu.md)-at részleges eredményként rögzítse: verseny-ítélet (C2, C3) + kiolvasási korlát (D1–D2) + méret-diagnózis (D3).
- **D5:** bővítési irány: a verseny és a kiolvasás megismétlése nagyobb, a kettő és négy kiterjedést már szétválasztó rendszeren — új csomagsorozat, e sorozat módosítása nélkül.
