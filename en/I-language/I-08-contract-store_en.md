---
id: I-08
type: chapter
lang: en
pair: I-08-contract-store_hu.md
pair_status: in-sync
doc_version: "1.3"
status: ervenyes
---

# I/8. The contract store

The vetted contract forms, with status. Notation: the joint weights of two two-state objects are $a, b, c, d$ on the cases $(0,0)$, $(0,1)$, $(1,0)$, $(1,1)$; the weights of a many-site object are, site by site, $\psi_1, \psi_2, \dots$

| Contract | Form | What it expresses | Status | Vetted by |
|---|---|---|---|---|
| Bond | $L = a^2 + d^2 + \tfrac{1}{2}(b + c)^2$ | penalizes agreement and the bookkeeping of roles | vetted; derivable candidate ([III/1](../III-frontier/III-01-candidate-laws_en.md)) | [II/1](../II-proofs/II-01-pair-bond/proof_en.md), [II/2](../II-proofs/II-02-exchange-oscillation/proof_en.md), [II/5](../II-proofs/II-05-triangle/proof_en.md), [II/9](../II-proofs/II-09-kagome/proof_en.md), [II/10](../II-proofs/II-10-internal-witness/proof_en.md), [II/11](../II-proofs/II-11-locality-readout/proof_en.md) |
| Smoothness | penalty on the square of the weight difference of neighboring sites | binds many sites into a single object | candidate definitional price, half confirmed ([III/1](../III-frontier/III-01-candidate-laws_en.md)) | [II/3](../II-proofs/II-03-box/proof_en.md), [II/4](../II-proofs/II-04-hydrogen-atom/proof_en.md), [II/6](../II-proofs/II-06-universality/proof_en.md), [II/12](../II-proofs/II-12-network-race/proof_en.md), [II/13](../II-proofs/II-13-dimension-race/proof_en.md) |
| Wall | penalty on the forbidden sites | spatial boundary | vetted | [II/3](../II-proofs/II-03-box/proof_en.md) |
| Attractive | discount for sites close to the center, inversely with the distance | attraction | imported form | [II/4](../II-proofs/II-04-hydrogen-atom/proof_en.md) |
| Bowl | cost with the square of the distance measured from the center | the bottom of every smooth attractive contract | derived form (at the bottom of the well the slope is zero, the curvature is not) | [II/7](../II-proofs/II-07-bowl-magic-numbers/proof_en.md), [II/8](../II-proofs/II-08-exclusion-vs-repulsion/proof_en.md) |
| Repulsive | penalty on instance pairs, inversely with their distance | repulsion | the sign-reversed image of the attractive form — no new import | [II/8](../II-proofs/II-08-exclusion-vs-repulsion/proof_en.md) |
| Value-bias | local penalty on one value of the object | external bias | the value variant of the wall/discount term | [II/10](../II-proofs/II-10-internal-witness/proof_en.md) |
