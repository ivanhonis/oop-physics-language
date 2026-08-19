---
id: I-04
type: chapter
lang: en
pair: I-04-ownership-view_hu.md
pair_status: in-sync
doc_version: "1.3"
status: ervenyes
---

# I/4. Ownership and the view

**Where encapsulation fails.** For two objects, classical OOP would expect this: each has its own weight pair, and the state of the system is the two of them placed side by side. Reality does something else: the state of the pair is a weighting of the **combinations** — four weights on the cases $(0,0)$, $(0,1)$, $(1,0)$, $(1,1)$. Most quadruples of weights do not arise as the product of two separate weight pairs. In that case the pair has a well-defined state while the members separately do not. (Physics calls this entanglement; it is experimentally confirmed many times over.)

**Second law: the state is owned by the system, not by the instance.** The "instance's own, fully knowing state" exists only if the joint state happens to factor into a product. (Proof with a number: [II/1](../II-proofs/II-01-pair-bond/proof_en.md) — the advantage of joint ownership over the best instance-level state is half a coupling unit.)

**The view.** What the member is always entitled to is a read-only extract from the joint state:

- **Owned state** — the weight vector. Its owner is the unit as far as the entanglement reaches.
- **View** — the read-only, derived state of the member: not stored data but an extract computed from the joint state. It gives exactly the statistics of every local readout, but the joint state cannot be restored from it: the correlations between the members are not in it. (Physics calls the view a mixed state, a reduced density matrix.)

**The witness rule.** The computation of the view is a single rule: the partner must be summed out, and of the local interference capability of the member's two branches there remains as much as the partner is identical in the two branches. The partner is a witness: wherever it differs in the two branches, it records which branch the system is travelling in, and the marked branches no longer interfere locally. (Physics calls this the partial trace.)

**The space of the views: the disk.** The pure weight pairs live on the rim of the circle ($a^2 + b^2 = 1$); the views fill the whole disk. The rim is the pure states, the interior points are the views of entangled members, the center is complete ignorance. The distance of the view from the rim is therefore a computable measure of the entanglement of the pair. (With complex weights the circle expands into a spherical surface and the disk into a ball — into the Bloch sphere of physics.)

**A check with numbers.** A pair, with weight 0.8 on the case $(0,1)$ and 0.2 on $(1,0)$. The value readout of the member is 80–20 — exactly what a lone, pure weight pair $(\sqrt{0.8};\ \sqrt{0.2})$ would also give; this readout does not distinguish them. The readout rotated halfway (to 45 degrees) does: the pure state gives 90–10, the view of the entangled member gives 50–50. The missing interference was carried off by the partner — it differs completely in the two branches, and therefore takes all of it.
