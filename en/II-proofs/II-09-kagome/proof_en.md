---
id: II-09
type: proof
lang: en
pair: proof_hu.md
pair_status: in-sync
doc_version: "1.3"
status: ervenyes
builds_on: [II-01, II-05, I-05]
imports: "one item: Kagome adjacency (the geometric continuation of the locality import)"
---

# II/9. The Kagome proof

**The question.** The first terrain where the language does not recompute a closed result but decides a race: on the lattice built from triangles touching only at corners (the Kagome lattice of physics), which of two candidates is the equilibrium — the frozen pairing, in which every object sits in a fixed pair, or the self-rotating mixture of coverings, which the engine turns along the hexagon loops.

**The band — before the computation, from the concepts of the language.** For $N$ objects there are $2N$ bonds and $2N/3$ triangles, and every bond belongs to exactly one triangle — the total cost is therefore a sum of triangle costs. The theorem of [II/5](../II-05-triangle/proof_en.md) thus gives a strict **floor**: $(2N/3) \cdot (3/2) / (2N) = \tfrac{1}{2}$ per bond, below which no state can go. The accounting of the frozen covering gives a **ceiling**: a quarter of the bonds is perfect (0), three quarters run between two bound members uncorrelated with each other — their view is the center of the disk, the price of such a bond is ¾ — on average $\tfrac{1}{4} \cdot 0 + \tfrac{3}{4} \cdot \tfrac{3}{4}$ = **9/16**. And the verdict of the [4th law](../../I-language/I-05-contract_en.md): the frozen covering is not a self-rotating pattern — so it is not even a candidate equilibrium. The prediction: the winner is the self-rotating mixture, its cost inside the band.

**The computation.** The exact minimum of the full state space of small lattice pieces (12 and 18 objects, with periodic boundary), with the contract of [II/1](../II-01-pair-bond/proof_en.md) on every edge; as a control, the same on a square lattice (16 objects), where there is no triangle.

**The result** (cost per bond, in coupling units):

| state | cost/bond |
|---|---|
| floor (triangle theorem) | 0.5 |
| Kagome piece, 12 objects (exact) | **0.5231** |
| Kagome piece, 18 objects (exact) | **0.5264** |
| infinite lattice, liquid (published numerics, 2011) | 0.5307 |
| best structured solid candidate (published, 2007) | 0.5335 |
| frozen covering (ceiling; computed on the piece as well) | 0.5625 |
| square-lattice control (exact) | 0.3991 |

- The band held; the pieces tend monotonically in size towards the published infinite-lattice value; the value of the 12-object piece (−0.4537 per object) agrees with the published exact computation (−0.453).
- On the piece the frozen covering pays exactly 9/16 (machinery check), and the engine really does dislodge it: its spread is not zero; a single covering contributes only 12% of the weight of the ground state — no covering dominates.
- The undecided choice scales up: below the lowest triplet state sit 7 and 14 singlets respectively (at 12 and at 18 objects); at 36 objects physics computes roughly two hundred.
- The correlations die quickly (0.23 → 0.05 → 0.007): the system does not order.
- The control is not empty: the square lattice goes *below* the floor (there is no triangle tax), its correlations do not die (0.35 → 0.18, with alternating sign — it orders), and it has no singlet mass. The liquid is not a general gift of weighting but the constraint of the frustrated geometry.

**Checking against reality.** The infinite-lattice value is a milestone of numerical physics (DMRG, [Yan–Huse–White, 2011](../../appendix/C-benchmarks_en.md)); the singlet mass is a recurring finding of the published exact computations (Waldtmann et al., 1998; Läuchli et al., 2011); the Kagome material (herbertsmithite) does not freeze down to the lowest measured temperature, and shows a continuous spectrum of fractionalized excitations (Han et al., 2012).

**A number in fairness.** The serious solid candidate of physics is not the frozen caricature but is itself self-rotating, only a mixture of coverings arranged into a pattern — the verdict of the 4th law is no longer an argument against it. That too sits in the band (0.5335), and the liquid beats it by a mere 0.003 per bond. The quick argument of the language therefore excludes the caricature and gives the band; the decision between the structured solid and the liquid was numerical work, and the smallness of the difference shows why it took decades.

**Import ledger:** one item — Kagome adjacency, the geometric continuation of the locality import. **What it confirmed:** the band theorem (floor from II/5, ceiling from the pricing of the view); the liquid-versus-frozen decision is a theorem in the language. "Which liquid" remains open: [Part III](../../III-frontier/III-02-open-questions_en.md).
