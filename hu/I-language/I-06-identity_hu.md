---
id: I-06
type: chapter
lang: hu
pair: I-06-identity_en.md
pair_status: missing
doc_version: "1.3"
status: ervenyes
---

# I/6. Az azonosság

**Ötödik törvény: a példányazonosító nem adat.** Azonos típusú példányoknak nincs címkéjük: a „melyik melyik" nem a rendszer adata. A cseréjük ezért nem művelet, hanem átnevezés — a leírást írja át, a rendszert nem, és semmilyen kiolvasás statisztikáján nem hagyhat nyomot.

**Tétel: két típusosztály.** A csere a közös súlyvektort legfeljebb egy egységnyi nagyságú szorzóval változtathatja ([I/2](I-02-object-state_hu.md): az ilyen szorzó nem változtat állapotot). Kétszer cserélni annyi, mint semmit sem tenni, ezért ez a szorzó négyzetre emelve 1 — vagyis $+1$ vagy $-1$. És egy típus minden állapota ugyanabban az osztályban él: egy vegyes állapotot a csere mérhetően billentene (a két rész közti előjelviszonyt fordítja), ami a törvénnyel ellentétes. Két osztály adódik: **osztozó** típus — cserére változatlan (a fizika bozonnak hívja); **kizáró** típus — cserére előjelet vált (a fizika fermionnak hívja).

**Tétel: a kizárás.** Ha két kizáró példány ugyanazt az egyhelyes állapotot töltené, a csere az együttes súlyvektort előjelet váltva is helyben hagyná — ez csak a nullvektornak megy, az pedig nem állapot. **Egy egyhelyes állapotnak legfeljebb egy kizáró birtokosa van.** (A fizika ezt Pauli-elvnek hívja — itt nem külön szabály, hanem az ötödik törvény következménye. Számolt próbák: [II/7](../II-proofs/II-07-bowl-magic-numbers/proof_hu.md), [II/8](../II-proofs/II-08-exclusion-vs-repulsion/proof_hu.md).)

**Tétel: a kicserélődési kedvezmény.** Két kizáró példány párhuzamos belső mezővel kötelezően előjelváltó közös helymintázatot vesz fel; annak súlya az egybeeső helyeken nulla, a két példány sosem áll egy helyen — a taszítási számlájuk ezért kisebb. A párhuzamos beállás taszítás-kedvezményt kap. (A fizika ezt kicserélődési kölcsönhatásnak, a szabályt Hund-szabálynak hívja. Számolt próba: [II/8](../II-proofs/II-08-exclusion-vs-repulsion/proof_hu.md).)
