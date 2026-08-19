---
id: II-02
type: proof
lang: en
pair: proof_hu.md
pair_status: in-sync
doc_version: "1.3"
status: ervenyes
builds_on: [II-01, I-05]
imports: zero
---

# II/2. The exchange oscillation — the proof of the engine

**The question.** The [4th law](../../I-language/I-05-contract_en.md) claims more than scoring: the same contract also drives the evolution. This demands a separate proof — one that can be carried out on the same contract, with no new mathematics.

**The computation.** Let us start the pair from the state $(0,1)$. This is a half-and-half weighting of two cost levels of this contract — the role-free minimum of cost 0 and its symmetric partner of cost 1 unit. The engine turns the phase of the two components at a rate proportional to their cost, so their difference pulsates: the system oscillates between $(0,1)$ and $(1,0)$. The frequency of the oscillation is necessarily the difference of the two cost levels divided by the Planck constant; the return follows a $\cos^2$ curve; the time of a complete exchange is $h/(2 \cdot \text{coupling})$. **There is no free parameter:** the rate is given by the same number that [II/1](../II-01-pair-bond/proof_en.md) has already computed statically.

**Checking against reality.** On electron pairs confined in a double quantum dot this is measured directly (a routine experiment since [Petta et al., 2005](../../appendix/C-benchmarks_en.md)): at microelectronvolt coupling a gigahertz oscillation (4.1 μeV ↔ 1 GHz, since h ≈ 4.14 μeV/GHz), and the frequency moves together with the coupling, exactly as the formula says.

**Import ledger:** zero. **What it confirmed:** the 4th law. A single cost function gave back, as a judge, the bond of the hydrogen molecule (statics), and as an engine, the oscillation of the spin exchange (dynamics). With this the language is **closed**: to specify a system it is enough to list the objects and the contracts — the run is a consequence.
