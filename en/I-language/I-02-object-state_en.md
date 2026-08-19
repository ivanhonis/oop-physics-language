---
id: I-02
type: chapter
lang: en
pair: I-02-object-state_hu.md
pair_status: in-sync
doc_version: "1.3"
status: ervenyes
---

# I/2. The object and the state

Mathematically, an object type is a pair: $O = (S, M)$, where $S$ is the set of states (the possible values of the "fields" taken together), and $M$ is the set of the permitted operations: mappings $S \to S$ (the "methods"). An **instance** is one concrete state from this set.

**The state is not a value but a weighting.** The smallest system: one object with two possible values (0 and 1). Its state is not "0 or 1" but a weight pair $(a, b)$: how much the system is in 0 and how much in 1. On readout we get 0 with probability $a^2$ and 1 with probability $b^2$.

**The total length of the weights is fixed: $a^2 + b^2 = 1$.** This is not a separate assumption but the closure of the readout rule: the probabilities of the outcomes sum to 1. The space of the states is therefore the set of weight vectors of unit length — which is why we can speak of evolution as **rotation**. Two weight vectors that differ only by a common factor of unit magnitude say the same thing for every readout: they are the same state.

For the complete physical description the weights are complex numbers; for understanding the fundamentals it is enough in most places to take them as real. That the complex weight is not ornament but constraint is stated by the fourth law ([I/5](I-05-contract_en.md)), and its sharp experimental test is kept by the [1st open question of Part III](../III-frontier/III-02-open-questions_en.md). (Physics calls this two-valued object a qubit.)
