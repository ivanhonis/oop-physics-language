---
id: II-11
type: proof
lang: en
pair: proof_hu.md
pair_status: in-sync
doc_version: "1.3"
status: ervenyes
builds_on: [II-01, II-06, I-04, I-06]
imports: "zero new item; half of the locality import becomes a theorem, its remainder is selection (III/2, 2.)"
---

# II/11. The locality readout — space as a view

**The question.** The single remaining structural import of the language is locality: that the sites have neighbors, and that mixing runs only between them ([II/6](../II-06-universality/proof_en.md), [III/2](../../III-frontier/III-02-open-questions_en.md)). The question can be turned around: is adjacency stored data, or a view of the finished state? Two claims are to be tested: from the equilibrium state of a geometric contract network the adjacency can be read back without knowing the network or the labels; and there is a label-independent signature that decides whether a system is local — where there is no geometry, the readout must fail.

**The system and the contract.** Twelve objects closed into a ring, with the bond contract of [II/1](../II-01-pair-bond/proof_en.md) on every edge. Control: the same twelve objects, but everyone bonded with everyone (66 edges) — there is a contract, there is no geometry. The pairwise measure of closeness: how much more the joint view of the two members knows than the two separate views together. (Physics calls this mutual information.)

**The computation.** The exact minimum of the full state space ([Appendix B](../../appendix/B-machinery_en.md), tool 4). The ground state of the ring is unique; that of the control is 132-fold degenerate, so there the view is an even mixture of the zero-cost subspace, computed with an exact projector. From the finished state a closeness is computed for every pair; the rebuilder connects every object with its closest partners — how many such there are it does not know in advance, this is singled out by the jump of the closeness map (here: two, with a fourfold jump).

**The result.**

| | ring (12 objects) | control (everyone-with-everyone) |
|---|---|---|
| closeness by distance | 0.444 → 0.123 → 0.066 → 0.045 → 0.037 | all 66 pairs identical (0.012; spread 10⁻¹⁶) |
| rebuilding | 12/12 edges correct; gives the ring even with scrambled labels | there is no distinguished neighbor — it fails, as it should |
| ball growth (sites within r steps) | 1, 3, 5, 7, 9, 11 — +2 per step: one extension | there is nothing to measure |
| block entanglement (1→6 sites) | 0.69 → 1.18, flattens out — it follows the boundary | 0.69 → 3.89 — grows with the volume (maximum 4.16) |
| bond price | 0.3011 | 0.6818 (exactly 45/66) |

Three readings. **Adjacency can be read out:** the finished state carries its own geometry — adjacency is a view, not stored data, and renaming ([5th law](../../I-language/I-06-identity_en.md)) cannot spoil it. **The signature is label-independent:** in a local system the entanglement of a cut-out piece grows with the boundary of the piece, not with its interior (surface law); on the control this is measurably violated, and the closeness map is perfectly flat. **The extension number is measurable:** from the rate of ball growth — here one extension, computed. A side result for the question of selection ([III/2, 2.](../../III-frontier/III-02-open-questions_en.md)): the dense network pays 0.68 per bond against the 0.30 of the ring — the frustration tax favors the sparse network.

**Checking against reality.** The bond price of the ring agrees with the published exact small-ring value ($0.75 - 0.4489 = 0.3011$). The surface law in the equilibrium of local contracts is a result of physics confirmed many times over ([Eisert et al., 2010](../../appendix/C-benchmarks_en.md)); geometry read back from the state is a live program in physics (Van Raamsdonk, 2010) — here the language gave a small, exact example of it.

**Import ledger:** zero new item — and the other pan of the scale: half of the locality import has become a theorem; what remains an import is selection ([III/2, 2., reformulated](../../III-frontier/III-02-open-questions_en.md)). **What it confirmed:** adjacency is a view; locality is measurable from inside, without labels; the extension number is computable. The horizon: if distance is an extract of the entanglement pattern, then the engine of the [4th law](../../I-language/I-05-contract_en.md), which turns the entanglement, necessarily turns the geometry as well — that already belongs to Part III.
