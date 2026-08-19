---
id: II-07
type: proof
lang: en
pair: proof_hu.md
pair_status: in-sync
doc_version: "1.3"
status: ervenyes
builds_on: [I-06, II-03]
imports: "two type declarations: the electron is of the excluding class; the electron has an internal two-valued field"
---

# II/7. The bowl and the magic numbers — the proof of identity

**The question.** A computable consequence of the [5th law](../../I-language/I-06-identity_en.md): the filling order of excluding instances. The target system is the artificial atom.

**The system and the contract.** The electrons of the artificial atom (quantum dot) sit in a plane, at the bottom of an attractive contract. The shape of the bowl need not be given by hand: the bottom of every smooth attractive contract is quadratic close up — at the bottom of the well the slope is zero, the curvature is not. The lattice machinery of [II/3](../II-03-box/proof_en.md) computes the ladder of the self-rotating patterns from the contract.

**The computation and the result — the ladder.**

| | box (II/3) | bowl |
|---|---|---|
| cost ladder | 1 : 4 : 9 : 16 | 1 : 2 : 3 : 4 (even degrees) |
| patterns per degree | 1 | 1, 2, 3, 4 |

Computed: at fine subdivision the ladder is 1 : 2.000 : 2.999 : 3.997, and the levels within a degree coincide to within a thousandth; at coarse subdivision it is 1 : 1.95 : 2.84 : 3.59, and the degrees separate — the deviation disappears with refinement, just as with the box. The pattern count of 1-2-3-4 per degree is a level coincidence: an unrequested bonus — and the backbone of the prediction, because it is what gives the size of the shells.

**The proof.** The electron is of the excluding type, and it has an internal, two-valued field (physics calls it spin) — this doubles every site pattern. According to the [theorem of exclusion](../../I-language/I-06-identity_en.md) each state so obtained can be filled by at most one instance; the cold environment fills from below. The capacity of the degrees is 2, 4, 6, 8; the filling numbers are **2, 6, 12, 20** — the prediction: the fee of admitting the next instance jumps at these.

**Checking against reality.** [Tarucha et al. (1996)](../../appendix/C-benchmarks_en.md) measure exactly this on an artificial atom: the peaks of the filling energy at 2, 6 and 12 electrons (the degree at 20 is already blurred at the edge of the measurement). An outlook: the same machinery with a bowl of three extensions promises fillings of 2, 8, 20 — the measured first magic numbers of atomic nuclei.

**Import ledger:** two type declarations — (1) the electron belongs to the excluding class (one bit; the deeper derivation in physics, the spin–statistics theorem, requires relativity, which is outside the scope of the language); (2) the electron has an internal two-valued field. Structural borrowing: zero. **What it confirmed:** the 5th law and the theorem of exclusion on measured numbers.
