---
id: I-08
type: chapter
lang: hu
pair: I-08-contract-store_en.md
pair_status: in-sync
doc_version: "1.3"
status: ervenyes
---

# I/8. A szerződéstár

A bevizsgált szerződés-alakok, státusszal. Jelölés: két kétállapotú objektum közös súlyai $a, b, c, d$ a $(0,0)$, $(0,1)$, $(1,0)$, $(1,1)$ eseteken; egy sok-helyes objektum súlyai helyenként $\psi_1, \psi_2, \dots$

| Szerződés | Alak | Mit fejez ki | Státusz | Bevizsgálva |
|---|---|---|---|---|
| Kötés | $L = a^2 + d^2 + \tfrac{1}{2}(b + c)^2$ | bünteti az egyezést és a szerep-nyilvántartást | bevizsgált; levezethető jelölt ([III/1](../III-frontier/III-01-candidate-laws_hu.md)) | [II/1](../II-proofs/II-01-pair-bond/proof_hu.md), [II/2](../II-proofs/II-02-exchange-oscillation/proof_hu.md), [II/5](../II-proofs/II-05-triangle/proof_hu.md), [II/9](../II-proofs/II-09-kagome/proof_hu.md), [II/10](../II-proofs/II-10-internal-witness/proof_hu.md), [II/11](../II-proofs/II-11-locality-readout/proof_hu.md) |
| Simasági | büntetés a szomszédos helyek súlykülönbségének négyzetére | sok helyet egyetlen objektummá köt | jelölt definíciós ár, fele igazolva ([III/1](../III-frontier/III-01-candidate-laws_hu.md)) | [II/3](../II-proofs/II-03-box/proof_hu.md), [II/4](../II-proofs/II-04-hydrogen-atom/proof_hu.md), [II/6](../II-proofs/II-06-universality/proof_hu.md), [II/12](../II-proofs/II-12-network-race/proof_hu.md), [II/13](../II-proofs/II-13-dimension-race/proof_hu.md) |
| Fal | a tiltott helyek büntetése | térbeli határ | bevizsgált | [II/3](../II-proofs/II-03-box/proof_hu.md) |
| Vonzó | kedvezmény a középponthoz közeli helyeknek, a távolsággal fordítottan | vonzás | import-alak | [II/4](../II-proofs/II-04-hydrogen-atom/proof_hu.md) |
| Tál | költség a középponttól mért távolság négyzetével | minden sima vonzó szerződés alja | levezetett alak (a gödör alján a lejtő nulla, a görbület nem) | [II/7](../II-proofs/II-07-bowl-magic-numbers/proof_hu.md), [II/8](../II-proofs/II-08-exclusion-vs-repulsion/proof_hu.md) |
| Taszítási | példánypárok büntetése a távolságukkal fordítottan | taszítás | a vonzó alak előjelváltott mása — új import nincs | [II/8](../II-proofs/II-08-exclusion-vs-repulsion/proof_hu.md) |
| Érték-elfogultsági | helyi büntetés az objektum egyik értékére | külső elfogultság | a fal/kedvezmény-tag érték-változata | [II/10](../II-proofs/II-10-internal-witness/proof_hu.md) |
