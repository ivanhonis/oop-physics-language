---
id: II-01
type: proof
lang: hu
pair: proof_en.md
pair_status: missing
doc_version: "1.3"
status: ervenyes
builds_on: [I-02, I-04, I-05]
imports: nulla
---

# II/1. A pár kötése — a bíró próbája

**A kérdés.** Tud-e a legegyszerűbb szerződés helyesen pontozni: kiadja-e a közös birtoklás mérhető előnyét?

**A rendszer és a szerződés.** Két kétállapotú objektum, közös súlyaik $a, b, c, d$. A szerződés három elvárás:

$$
L = a^2 + d^2 + \tfrac{1}{2}(b + c)^2 \tag{K-II1-1}
$$

— $a^2$ és $d^2$ bünteti az egyezést; $(b + c)^2$ bünteti, ha a rendszer „tudja", melyik tag a 0 és melyik az 1: a szerepek nyilvántartása tilos.

**A számolás.** *Példány-szintű (szétbontható) állapotok:* mindkét tag saját súlypárja egy-egy szöggel írható: $(\cos\theta_1, \sin\theta_1)$ és $(\cos\theta_2, \sin\theta_2)$. Behelyettesítve és a szögösszeg-azonosságokkal összevonva a költség zárt alakra hozható:

$$
L_{\text{termék}} = \tfrac{1}{2} + \tfrac{1}{2}\cos^2(\theta_1 - \theta_2) \tag{K-II1-2}
$$

A minimum tehát pontosan **½**, akkor, ha a két tag merőlegesen áll ($\theta_1 - \theta_2 = 90^\circ$) — ennél lejjebb példány-szintű állapot elvileg nem mehet. *Közösen birtokolt állapotok:* az $a = d = 0$, $b = -c = 1/\sqrt{2}$ súlynégyesre $L = \tfrac{1}{2}(b + c)^2 = 0$. Ez a szerep-mentes állapot: fele súly a $(0,1)$-en, fele az $(1,0)$-n, ellentétes előjellel — a rendszer nem tartja nyilván, ki a 0 és ki az 1. A szerződés ütem-létrája: egyetlen 0 költségű állapot, fölötte három, egyenként 1 csatolásegységnyi.

**Az eredmény.** A ½ különbség kizárólag a szerep-nyilvántartás tilalmából jön: ezt az elvárást példány-szintű állapottal nem lehet teljesíteni, csak közösen birtokolttal. **Az összefonódás ebben a nyelvben tétel, nem feltevés.** A győztes állapot tagjának nézete a korong középpontja — a legteljesebb közös birtoklás.

**Ellenőrzés a valóságon.** Ez a rendszer a fizikában két spin antiferromágneses csatolása. A kiadott minimum a szingulett állapot — a hidrogénmolekula kötésének és az antiferromágneseknek a mért alapállapota —, és a kötött–független energiakülönbség ott is a csatolás erősségének fele.

**Import-számla:** nulla. **Mit igazolt:** a [2. törvényt](../../I-language/I-04-ownership-view_hu.md) számmal; a szerződés bíróként működik; a getter díja ([I/7](../../I-language/I-07-measurement_hu.md)) innen kap számot: a kötés szakítása ½-be kerül.