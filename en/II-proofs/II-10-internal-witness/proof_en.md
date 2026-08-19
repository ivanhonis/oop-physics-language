---
id: II-10
type: proof
lang: en
pair: proof_hu.md
pair_status: in-sync
doc_version: "1.3"
status: reszleges
builds_on: [II-01, II-06, I-07, I-08]
imports: zero
---

# II/10. The internal witness

**The question.** So far the witness stood outside ([I/5](../../I-language/I-05-contract_en.md): the environment; [I/7](../../I-language/I-07-measurement_en.md): the instrument). In a closed system a witness can only be inside. When can a system play the role of its own environment — and when can it not?

**The candidate theorem.** Thermalization in the language: the parts witness each other, and slide each other's view into the temperature-weighted view. Two halves: at **weak** unevenness the beats of the engine are shared across the sites, the witnessing spreads all the way through, the part-views slide towards the center of the disk, the memory of the initial pattern is lost. At **strong** unevenness the engine falls apart into a product of local engines: the witnessing does not spread, the view is stranded near the rim — the system remembers forever. The arc belongs to [II/6](../II-06-universality/proof_en.md): what smoothed out for a single object switches mode for many excluding instances. (Physics: thermalization, and many-body localization respectively.)

**The system.** A chain of 12 objects, closed into a ring; on the edges the bond contract of [II/1](../II-01-pair-bond/proof_en.md), on every object a value bias of random strength ([I/8](../../I-language/I-08-contract-store_en.md)). The tuned parameter is the strength of the unevenness ($W$, in units of the bond coupling).

**First fingerprint: the statistics of the beat ladder.** The mean of the ratio of two neighboring degree gaps ($r$) chooses between two exact, published constants: for independent beats $2 \ln 2 - 1 \approx 0.386$, for mutually repelling beats (those shared across the sites) $\approx 0.531$. Computed, averaged over many draws:

| W | 1 | 2 | 3 | 4 | 5 | 6 | 8 |
|---|---|---|---|---|---|---|---|
| r | 0.528 | 0.490 | 0.437 | 0.409 | 0.397 | 0.391 | 0.393 |

The tip-over from the repelling to the independent is around $W \approx 3$–$4$. On a larger piece (14 objects) the two ends sharpen towards the two constants: 0.5276 → 0.5284, and 0.3913 → 0.3874 respectively.

**Second fingerprint: the memory test.** Starting from a frozen, alternating pattern; measuring the persisting pattern difference (I), the half-cut entanglement (S) and the length of the part-view:

| | weak (W = 1) | strong (W = 6) |
|---|---|---|
| memory (I) at a thousandfold time | 0.06 — lost | 0.54 — persisted |
| entanglement (S) | saturates quickly (2.87) | creeps, stepping decade by decade, reaching only 0.99 even over a thousandfold time |
| view length | 0.19 — slid to the center | 0.62 — stranded near the rim |

**Checking against reality.** The two constants are exact and published values respectively; the tip-over range agrees with the published small-chain numerics ([Pal–Huse 2010; Luitz et al. 2015](../../appendix/C-benchmarks_en.md) — the estimated boundary on this model is $W \approx 3.5$); the persistence of memory and the slow creep of entanglement have also been measured: cold atoms (Schreiber et al., 2015), trapped ions (Smith et al., 2016).

**Import ledger:** zero new item. **What it confirmed:** both halves of the internal-witness theorem on a small piece, with two independent fingerprints. The infinite form — a sharp phase or a dramatic slowdown — is the unsolved core of the terrain: [Part III](../../III-frontier/III-02-open-questions_en.md).
