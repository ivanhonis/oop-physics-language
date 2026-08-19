---
id: II-05
type: proof
lang: en
pair: proof_hu.md
pair_status: in-sync
doc_version: "1.3"
status: ervenyes
builds_on: [II-01, I-07]
imports: zero
---

# II/5. The triangle — frustration

**The question.** What happens if three members conclude the contract of [II/1](../II-01-pair-bond/proof_en.md) pairwise? Because of [exclusive ownership](../../I-language/I-07-measurement_en.md) a member cannot be part of two full bonds — the three contracts together are structurally unsatisfiable. The prediction stated in advance: the cost of the minimum is not zero but a computable remainder.

**The computation.** *Instance-level:* all three members can be written with one angle each, and the closed form of II/1 holds bond by bond: $L = \tfrac{1}{2} + \tfrac{1}{2}\cos^2(\theta_i - \theta_j)$. The sum of the three angle differences, however, is necessarily zero — they cannot all stand at 90 degrees. The best distribution is the 120-degree one: $\cos^2(120^\circ) = \tfrac{1}{4}$ on every bond, in total $L = 3 \cdot (\tfrac{1}{2} + \tfrac{1}{8})$ = **15/8**. *Jointly owned:* the exact minimum of the full, eight-state space is **3/2**, fourfold degenerate.

**The result.**

| State | Cost |
|---|---|
| Best instance-level arrangement | 15/8 |
| Jointly owned minimum (fourfold) | 3/2 |
| The cost of one bond in the minimum | ½ |

Three readings. The ½ remainder per bond is exactly the entanglement advantage of II/1 — exclusive ownership taxes back on every bond what joint ownership won at the pair. The benefit of joint ownership is transformed: no single bond reaches the full bond, but all three reach the instance-level ideal (½) at once, which is impossible with genuine own states. And the minimum is fourfold: frustration leaves an **undecided choice** in the system, two "directions of rotation".

**Checking against reality.** The measured level pattern of equilateral triangular molecular magnets (copper and vanadium triangles) is exactly this: two coinciding doublets at the bottom, above them a jump of 3/2 coupling units — measured routinely by susceptibility and spectroscopy ([Appendix C](../../appendix/C-benchmarks_en.md)).

**Import ledger:** zero — the triangle is only three already vetted contracts. **What it confirmed:** frustration is a theorem: it follows from exclusive ownership, and its remainder is a derived number. The undecided choice will be the raw material of [II/9](../II-09-kagome/proof_en.md).
