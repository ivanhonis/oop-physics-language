---
id: II-05
type: proof
lang: hu
pair: proof_en.md
pair_status: in-sync
doc_version: "1.3"
status: ervenyes
builds_on: [II-01, I-07]
imports: nulla
---

# II/5. A háromszög — a frusztráció

**A kérdés.** Mi történik, ha három tag páronként köti meg a [II/1](../II-01-pair-bond/proof_hu.md) szerződését? A [kizárólagos birtoklás](../../I-language/I-07-measurement_hu.md) miatt egy tag nem lehet két teljes kötés része — a három szerződés együtt szerkezetileg kielégíthetetlen. A jóslat előre kimondva: a minimum költsége nem nulla, hanem számolható maradék.

**A számolás.** *Példány-szintű:* mindhárom tag egy-egy szöggel írható, és a II/1 zárt alakja kötésenként érvényes: $L = \tfrac{1}{2} + \tfrac{1}{2}\cos^2(\theta_i - \theta_j)$. A három szögkülönbség összege azonban kötelezően nulla — nem állhat mind a 90 fokon. A legjobb elosztás a 120 fokos: $\cos^2(120^\circ) = \tfrac{1}{4}$ minden kötésen, összesen $L = 3 \cdot (\tfrac{1}{2} + \tfrac{1}{8})$ = **15/8**. *Közösen birtokolt:* a teljes, nyolcállapotos tér pontos minimuma **3/2**, négyszeresen elfajult.

**Az eredmény.**

| Állapot | Költség |
|---|---|
| Legjobb példány-szintű elrendezés | 15/8 |
| Közösen birtokolt minimum (négyszeres) | 3/2 |
| A minimumban egy-egy kötés költsége | ½ |

Három olvasat. A kötésenkénti ½ maradék pontosan a II/1 összefonódási előnye — a kizárólagos birtoklás minden kötésen visszaadóztatja, amit a párnál a közös birtoklás nyert. A közös birtoklás haszna átalakul: egyetlen kötés sem éri el a teljes kötést, de mindhárom egyszerre eléri a példány-szintű ideált (½), ami valódi saját-állapotokkal lehetetlen. És a minimum négyszeres: a frusztráció **eldöntetlen választást** hagy a rendszerben, két „forgásirányt".

**Ellenőrzés a valóságon.** Az egyenlő oldalú háromszög-molekulamágnesek (réz- és vanádium-háromszögek) mért szintképe pontosan ez: alul két egybeeső kettős, fölötte 3/2 csatolásegységnyi ugrás — szuszceptibilitással és spektroszkópiával rutinszerűen mérve ([C függelék](../../appendix/C-benchmarks_hu.md)).

**Import-számla:** nulla — a háromszög csak három, már bevizsgált szerződés. **Mit igazolt:** a frusztráció tétel: a kizárólagos birtoklásból következik, maradéka levezetett szám. Az eldöntetlen választás a [II/9](../II-09-kagome/proof_hu.md) nyersanyaga lesz.