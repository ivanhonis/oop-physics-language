---
id: I-03
type: chapter
lang: en
pair: I-03-operations_hu.md
pair_status: in-sync
doc_version: "1.3"
status: ervenyes
---

# I/3. The operations: evolution and measurement

Every operation can be of two kinds:

1. **Evolution** — it rotates the weights, preserving their total length. Deterministic and always reversible: a setter that always has an inverse.
2. **Measurement** — it makes a single value out of the weights. Random and irreversible. This is the only "read".

**First law: there is no side-effect-free getter.** Every read is also a write. In this language, that is all there is to the "strangeness" of quantum physics. The price of the law can be turned into a number: on a bound system the minimal fee of the getter's side effect is the binding energy ([I/7](I-07-measurement_en.md), with numbers: [II/1](../II-proofs/II-01-pair-bond/proof_en.md)).

**Third law: the evolution operations are weight-preserving.** Evolution carries a weighted state term by term: if the operation makes $X$ out of pure 0 and $Y$ out of pure 1, then out of the weighting $(a, b)$ it necessarily makes $a \cdot X + b \cdot Y$. (Physics calls this linearity.) This law is the structural basis of every computation in Part II, and one of the pillars of the clone() theorem ([I/7](I-07-measurement_en.md)).

At first sight measurement falls outside the $S \to S$ frame, since its output is random. The gap is closed by the notion of the view ([I/4](I-04-ownership-view_en.md), [I/7](I-07-measurement_en.md)): on the space of the views the disturbing half of measurement is already a deterministic state→state operation, and the randomness enters only at the reading off — at a single, well-delimited point of the language.
