---
id: II-01
type: proof
lang: en
pair: proof_hu.md
pair_status: in-sync
doc_version: "1.3"
status: ervenyes
builds_on: [I-02, I-04, I-05]
imports: zero
---

# II/1. The bond of the pair — the proof of the judge

**The question.** Can the simplest contract score correctly: does it yield the measurable advantage of joint ownership?

**The system and the contract.** Two two-state objects, their joint weights $a, b, c, d$. The contract is three expectations:

$$
L = a^2 + d^2 + \tfrac{1}{2}(b + c)^2 \tag{K-II1-1}
$$

— $a^2$ and $d^2$ penalize agreement; $(b + c)^2$ penalizes the system for "knowing" which member is the 0 and which is the 1: the bookkeeping of roles is forbidden.

**The computation.** *Instance-level (separable) states:* the own weight pair of each member can be written with one angle each: $(\cos\theta_1, \sin\theta_1)$ and $(\cos\theta_2, \sin\theta_2)$. Substituting and collecting with the angle-sum identities, the cost can be brought to closed form:

$$
L_{\text{product}} = \tfrac{1}{2} + \tfrac{1}{2}\cos^2(\theta_1 - \theta_2) \tag{K-II1-2}
$$

The minimum is therefore exactly **½**, attained when the two members stand perpendicular ($\theta_1 - \theta_2 = 90^\circ$) — in principle no instance-level state can go below this. *Jointly owned states:* for the weight quadruple $a = d = 0$, $b = -c = 1/\sqrt{2}$ we get $L = \tfrac{1}{2}(b + c)^2 = 0$. This is the role-free state: half the weight on $(0,1)$, half on $(1,0)$, with opposite signs — the system does not keep a record of who is the 0 and who is the 1. The beat ladder of the contract: a single state of cost 0, and above it three, each of one coupling unit.

**The result.** The ½ difference comes exclusively from the prohibition on the bookkeeping of roles: this expectation cannot be satisfied by an instance-level state, only by a jointly owned one. **In this language entanglement is a theorem, not an assumption.** The view of a member of the winning state is the center of the disk — the fullest joint ownership.

**Checking against reality.** In physics this system is the antiferromagnetic coupling of two spins. The minimum it yields is the singlet state — the measured ground state of the bond of the hydrogen molecule and of antiferromagnets — and there too the bound–independent energy difference is half the strength of the coupling.

**Import ledger:** zero. **What it confirmed:** the [2nd law](../../I-language/I-04-ownership-view_en.md) with a number; the contract works as a judge; the fee of the getter ([I/7](../../I-language/I-07-measurement_en.md)) receives its number from here: tearing the bond costs ½.
