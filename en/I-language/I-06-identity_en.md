---
id: I-06
type: chapter
lang: en
pair: I-06-identity_hu.md
pair_status: in-sync
doc_version: "1.3"
status: ervenyes
---

# I/6. Identity

**Fifth law: the instance identifier is not data.** Instances of the same type have no label: "which is which" is not data of the system. Exchanging them is therefore not an operation but a renaming — it rewrites the description, not the system, and it cannot leave a trace on the statistics of any readout.

**Theorem: two type classes.** The exchange may change the joint weight vector by at most a factor of unit magnitude ([I/2](I-02-object-state_en.md): such a factor does not change the state). Exchanging twice amounts to doing nothing, therefore this factor squared is 1 — that is, $+1$ or $-1$. And every state of a type lives in the same class: a mixed state would be measurably tipped by the exchange (it reverses the sign relation between the two parts), which contradicts the law. Two classes follow: **sharing** type — unchanged under exchange (physics calls it a boson); **excluding** type — changes sign under exchange (physics calls it a fermion).

**Theorem: exclusion.** If two excluding instances were to fill the same single-site state, the exchange would leave the joint weight vector in place even while reversing its sign — which works only for the null vector, and that is not a state. **A single-site state has at most one excluding owner.** (Physics calls this the Pauli principle — here it is not a separate rule but a consequence of the fifth law. Computed proofs: [II/7](../II-proofs/II-07-bowl-magic-numbers/proof_en.md), [II/8](../II-proofs/II-08-exclusion-vs-repulsion/proof_en.md).)

**Theorem: the exchange discount.** Two excluding instances with parallel internal fields necessarily take up a sign-reversing joint site pattern; its weight is zero on coinciding sites, so the two instances never stand at the same site — their repulsion bill is therefore smaller. Parallel alignment receives a repulsion discount. (Physics calls this the exchange interaction, and the rule Hund's rule. Computed proof: [II/8](../II-proofs/II-08-exclusion-vs-repulsion/proof_en.md).)
