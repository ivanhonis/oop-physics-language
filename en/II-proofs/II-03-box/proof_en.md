---
id: II-03
type: proof
lang: en
pair: proof_hu.md
pair_status: in-sync
doc_version: "1.3"
status: ervenyes
builds_on: [I-05, II-01]
imports: "one item: adjacency (II/6 narrows it to locality)"
---

# II/3. The box — quantization from boundness

**The question.** The discrete value set is not a property written into the type but a consequence of boundness — here this turns from a promise into a computed theorem.

**The system and the contract.** A single object with many possible sites in a row. Two expectations: the **wall** (penalty on the sites outside the box) and the **smoothness** contract (penalty on the square of the weight difference of neighboring sites — in form the same term as the $(b + c)^2$ of [II/1](../II-01-pair-bond/proof_en.md)).

**The computation.** The sites divided into cells; the matrix of the contract written down on the space of the cells; the self-rotating patterns (those the engine rotates into themselves) and their costs are computed as the eigenproblem of the matrix. In a bound system only countably many such patterns fit.

**The result.** The self-rotating patterns are standing waves vanishing at the walls; the ratio of their cost ladder at fine subdivision is **1 : 4 : 9 : 16**. A bonus: at coarse cell subdivision the ratios deviate (1 : 3.98 : 8.87 : …) — and this is not an error but a separate prediction (see the check).

**Checking against reality.** The continuous ladder is measured directly in semiconductor quantum wells. The coarse-subdivision, deviating ladder is measured by physics in crystal lattices — the language gave back, unrequested, the measured behavior of the lattice variant as well.

**Import ledger:** one item — **adjacency** (the arrangement of the sites in a row, the "next to" relation). [II/6](../II-06-universality/proof_en.md) later narrows this to locality. **What it confirmed:** the 2nd consequence of the [4th law](../../I-language/I-05-contract_en.md) (discrete beats from boundness).
