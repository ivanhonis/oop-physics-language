---
id: I-07
type: chapter
lang: en
pair: I-07-measurement_hu.md
pair_status: in-sync
doc_version: "1.3"
status: ervenyes
---

# I/7. The price of measurement and the absence of clone()

**Measurement as a member–environment contract.** The readout is not magic outside the language but the switching on of a contract: the instrument is an environment that becomes the witness of the member's value — the witness rule ([I/4](I-04-ownership-view_en.md)) runs in a targeted way and at full strength: the instrument assigns two distinguishable states of its own to the two possible values of the member, and the branches of the member no longer interfere locally.

**The bond tears.** Joint ownership is exclusive: a member cannot be a full-fledged part of two bonds at once. (Physics: monogamy of entanglement.) When the witness grabs the member, the member–partner bond tears and the ownership boundary is redrawn: before it, the pair owned; after it, the member shares with the instrument and the partner is set free — knowing the outcome, it now has an independent, pure state.

**The accounting.** On the contract of [II/1](../II-proofs/II-01-pair-bond/proof_en.md) the cost of the bound minimum is 0, that of the post-readout states is ½. The difference was paid in by the instrument: **on a bound system the minimal fee of the getter's side effect is the binding energy.** The price of the first law thereby becomes a number — and physics measures it too: tearing a singlet costs exactly this much energy.

**Signalling is impossible.** The readout of the partner does not move the unconditional view of the member — on the member's side no local readout whatsoever reveals whether the partner has been measured. Entanglement is not a signalling channel. (Physics: no-signaling.)

**The place of randomness.** On the space of the views, measurement falls apart into two steps: the **witnessing** is a deterministic, weight-preserving operation (it projects the rim point of the disk onto its axis), and the randomness enters only at the **reading off** — at the selection of one of the branches. With this the frame of [I/3](I-03-operations_en.md) is closed: every operation is a state→state mapping.

**One mechanism, two modes of operation.** The slowly, weakly contacting cold environment carries off the surplus and lets the system down into the bound minimum; the quickly, strongly fixing environment (the instrument) witnesses and tears. The randomness read out and the energy paid in are the two sides of the same transaction. (That the system can also be its *own* environment — an internal witness — is put to the test by [II/10](../II-proofs/II-10-internal-witness/proof_en.md); its infinite form is open in Part III.)

**Theorem: clone() does not exist.** There is no operation that makes a perfect copy of an unknown state — this is a consequence of the first and the third law ([I/3](I-03-operations_en.md)), in two layers. *First layer — the path of reading is closed:* you can only copy what you have read out first; the only reading is measurement, which makes a single value out of the weight pair and overwrites the original as well. *Second layer — the path of evolution is closed too:* a universal copier without measurement would have to make the pair $(0,0)$ out of pure 0 and the pair $(1,1)$ out of pure 1; because of weight preservation, out of the weighting $(a, b)$ it then necessarily makes $a \cdot (0,0) + b \cdot (1,1)$ — not two independent copies but one jointly owned pair. **The attempt to copy manufactures entanglement instead of a copy.** And the botched copier of the second layer is not a reject but exactly the instrument described above: it copies a value and manufactures entanglement — this is witnessing itself. The impossibility of clone() and the side effect of the getter are two readings of a single fact. (Physics: the No-Cloning theorem.)

**Consequence: the handover semantics.** There is no pass by value. Two kinds of handover exist: **pass by reference** — the object joins a joint state; this is entanglement itself; and **move** — the state can be carried over to another carrier, but the original is necessarily destroyed in the process (physics: teleportation, which works experimentally in exactly this way). The state model of the language therefore resembles the ownership model of modern programming languages — a state has one owner, there is no copy, only move — but here this is not a design decision but a forced consequence of the laws.
