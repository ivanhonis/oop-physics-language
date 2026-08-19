---
id: I-03
type: chapter
lang: hu
pair: I-03-operations_en.md
pair_status: missing
doc_version: "1.3"
status: ervenyes
---

# I/3. A műveletek: fejlődés és mérés

Minden művelet kétféle lehet:

1. **Fejlődés** — a súlyokat forgatja, az összhosszukat megőrizve. Determinisztikus és mindig visszafordítható: olyan setter, amelynek mindig van inverze.
2. **Mérés** — a súlyokból egyetlen értéket csinál. Véletlenszerű és nem visszafordítható. Ez az egyetlen „olvasás".

**Első törvény: nincs mellékhatás-mentes getter.** Minden olvasás írás is. A kvantumfizika „furcsasága" ezen a nyelven ennyi. A törvény ára számmá tehető: kötött rendszeren a getter mellékhatásának minimális díja a kötési energia ([I/7](I-07-measurement_hu.md), számokkal: [II/1](../II-proofs/II-01-pair-bond/proof_hu.md)).

**Harmadik törvény: a fejlődés-műveletek súlytartók.** Egy súlyozott állapotot a fejlődés tagonként visz át: ha a művelet a tiszta 0-ból $X$-et, a tiszta 1-ből $Y$-t csinál, akkor az $(a, b)$ súlyozásból kötelezően $a \cdot X + b \cdot Y$ lesz. (A fizika ezt linearitásnak hívja.) Ez a törvény minden II. részbeli számolás szerkezeti alapja, és a clone()-tétel egyik pillére ([I/7](I-07-measurement_hu.md)).

A mérés első ránézésre kilóg az $S \to S$ keretből, hiszen a kimenete véletlen. A rést a nézet-fogalom zárja ([I/4](I-04-ownership-view_hu.md), [I/7](I-07-measurement_hu.md)): a nézetek terén a mérés zavaró fele már determinisztikus állapot→állapot művelet, a véletlen csak a leolvasásnál lép be — a nyelv egyetlen, jól körülhatárolt pontján.
