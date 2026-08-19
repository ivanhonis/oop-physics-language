---
id: II-08
type: proof
lang: en
pair: proof_hu.md
pair_status: in-sync
doc_version: "1.3"
status: ervenyes
builds_on: [II-07, II-04, I-06]
imports: "zero new item (the repulsive form is the sign-reversed image of the attraction import)"
---

# II/8. The race of exclusion and repulsion

**The question.** [II/7](../II-07-bowl-magic-numbers/proof_en.md) filled the instances independently of each other; the contract between the instances themselves — repulsion — enters here. This is the first system in which two contracts race: exclusion sets the order, repulsion the cost.

**The system and the contract.** The bowl of II/7; plus a penalty on every instance pair, in inverse proportion to their distance. There is no new import: the form is the sign-reversed image of the attraction import of [II/4](../II-04-hydrogen-atom/proof_en.md).

**The theorem, in the words of the language.** With parallel internal fields the joint site pattern is necessarily sign-reversing because of the [5th law](../../I-language/I-06-identity_en.md) — its weight is zero on coinciding sites, the two instances never stand at the same site, the repulsion bill is smaller: parallel alignment receives a discount ([I/6, the exchange discount](../../I-language/I-06-identity_en.md)).

**The computation.** On the lattice patterns the pairwise integrals of the repulsion penalties are computed (accuracy check: the repulsion of the lowest pattern with itself is analytically $\sqrt{\pi/2} \approx 1.2533$; on the lattice 1.246 — 0.6%); then the exact race of all arrangements within a degree, by exhaustive search. The computation neglects mixing between degrees — valid as long as the repulsion is not stronger than the degree gap. The predicted quantity is the jump of the filling fee.

**The result** (the strength of the repulsion is half the degree gap; the fee jump in units of the degree gap):

| N | 2 | 4 | 6 | 9 | 12 | other N |
|---|---|---|---|---|---|---|
| fee jump | 1.16 | 0.55 | 1.01 | 0.43 | 0.84 | 0.27–0.32 |

Main peaks at 2, 6, 12 (degree closures, in decreasing order); secondary peaks at 4 and 9 — the half-filled degrees, purely from the exchange discount. The multiplicity of the minima traces out the alignment schedule: the 4-electron minimum is threefold (two parallel fields), the 9-electron one fourfold; the full sequence from N = 1 to 12: 2, 1, 4, 3, 4, 1, 2, 3, 4, 3, 2, 1. At twice the repulsion the peak positions are unchanged, only the ratios shift. **Control:** with a sharing type the race does not even begin — every instance sits into the lowest pattern, the fee jump is even, there is no peak. The magic numbers are the fingerprint of exclusion.

**Checking against reality.** The measurement of [Tarucha et al. (1996)](../../appendix/C-benchmarks_en.md) is exactly this: main peaks at 2, 6, 12 in decreasing order, secondary peaks at 4 and 9 — and there too the secondary peaks are explained by parallel alignment (the "spin effects" of the paper's title).

**Import ledger:** zero new item. **What it confirmed:** the theorem of the exchange discount on measured numbers — and it opened the derivability of the bond contract ([III/1](../../III-frontier/III-01-candidate-laws_en.md)): in two neighboring wells the same mechanism works with the opposite sign (opposite alignment wins, because only that lets the instances reach into each other's well through the smoothness contract), which in form is the role-forbidding contract of [II/1](../II-01-pair-bond/proof_en.md).
