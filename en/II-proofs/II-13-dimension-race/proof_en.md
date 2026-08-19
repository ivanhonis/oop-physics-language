---
id: II-13
type: proof
lang: en
pair: proof_hu.md
pair_status: in-sync
doc_version: "1.3"
status: reszleges
builds_on: [II-11, II-12, I-06]
imports: "zero new item (the race rule and the equal rank of the sites are declared conventions inherited from II/12)"
packages: [PKG-13-1, PKG-13-2, PKG-13-3, PKG-13-4]
---

# II/13. The extension race — a partial yes

**The question.** The target proof of [III/2, 8.](../../III-frontier/III-02-open-questions_en.md): at an identical number of contracts per site, does the cost structure favor the weave of higher extension — or the line, or the segmentation? After the lesson of [II/12](../II-12-network-race/proof_en.md) there was deliberately no prediction. The proof was produced with the package method ([Appendix D](../../appendix/D-package-method_en.md)): the rulebook — candidates, verdict rule, readout protocol — was fixed before every computation ([PKG-13-1](PKG-13-1-rulebook_en.md)).

**The system and the contract.** Sixteen sites; 32 units of smoothness contract, exactly four per site. Here the equal rank of the sites is a construction principle: every candidate is a **weave network** — a group structure prescribes the same wiring pattern for every site, so the network is guaranteed to look the same from every site. Candidates: **line** (a 16-ring with first- and second-neighbor contracts), **plane** (a 4×4 lattice with periodic boundary), **segmented** (two thickened 8-rings); obligatory scan: all 21 wirings of the line family.

**The coincidence lemma.** About the planned fourth candidate — the 2×2×2×2 four-extension weave — it turned out during the fixing that on 16 sites it is **the same network as the plane**: the two-extension weave of side length 2 is itself the 4-ring, and weaves can be assembled direction-pair by direction-pair. A consequence, stated in advance: at this size the question of two-or-four extensions cannot even be posed — the race is about the line–plane–segmented triple. (Spectral confirmation: the ladder of the plane is exactly the binomial ladder of the hypercube with widths 1-4-6-4-1, to machine precision — [PKG-13-2](PKG-13-2-ladders_en.md).)

**The computation.** Every ladder by two independent routes (the eigenproblem of the machinery and the closed formula of the weaves; the segmented one moreover in two constructions), agreeing to within $10^{-15}$; the trace sum on all twenty-four networks is exactly 64 — the cover of the trace tie. The catch of the scan: **two** segmented weaves live in the family, with different ladders — the second entered as a new candidate; the 21 members fall into 7 ladder classes ([PKG-13-2](PKG-13-2-ladders_en.md)). The race: filling from below from $N = 1$ to 16; the readout on the winner with the fixed protocol ([PKG-13-3](PKG-13-3-race_en.md), [PKG-13-4](PKG-13-4-readout_en.md)).

**The result — the race.**

| N instances | 1 | 2 | 3–5 | 6–8 | 9–10 | 11 | 12–13 | 14 | 15 | 16 |
|---|---|---|---|---|---|---|---|---|---|---|
| winner | all | segmented ones | **line** | **segmented** | cross-lines | **plane** | cross-lines | 2nd segmented | tie (56) | all (64) |

Two readings, both according to the fixed rule. *Main reading:* the plane beats the line and the segmented one at the same time over the connected range **10–15** — **the proof says a partial yes: at high density the extension pays off.** *Full field:* the race falls into regimes, and the single strict victory of the plane is **N = 11** — exactly its own closed degree (its degree boundaries are 1, 5, 11, 15). Two derived accompanying phenomena: the **shell logic** — the winner wins where one degree of its own ladder is just filling up (the degree boundaries of the segmented one are 2, 6, 8 — its winning band is 6–8; fixed as a candidate rule: [III/1, 6.](../../III-frontier/III-01-candidate-laws_en.md)); and the **mirror effect** — at nearly full filling the cost is 64 minus the unfilled upper beats, so there the winner is the one who compresses its cost into few high beats. Extension is accordingly a **density-dependent equilibrium property**: it belongs to the network+filling pair, not to the network.

**The result — the readout.** On the winner (plane, $N = 11$) the rebuilder found all 32 real contracts, with none missing — but the small weave also "hears" its own wrap-around: 8 phantom edges were written beside them (all antipodal diagonals), with exactly the same closeness as the real ones; the measured ball is therefore not the recorded torus sequence. **The closing of the loop failed partially at this size** — not destructively: no false geometry took the place of the real one, only an echo above the real one. The diagnosis (outside the fixed scope, as a candidate): on an 8×8 weave the resonance disappears (the neighbor closeness is twofold dominant), the rebuilding is 128/128 with no phantom, and the ball increment is 4, 8, 12 — **$+4r$ per step: the measured growth law of two extensions** (against the constant $+2$ of the line). The 16-site resonance is a size artifact ([PKG-13-4](PKG-13-4-readout_en.md)).

**Checking against reality.** This proof — like II/12 — is an internal race, without a direct measured target; it has two measured echoes: the degree-filling-driven victory is the network-level image of the measured magic-number mechanism of [II/7](../II-07-bowl-magic-numbers/proof_en.md), and the density-driven structural change is a standard measured phenomenon of physics (materials change lattice under pressure) — here in its smallest, exact form.

**Import ledger:** zero new item — the race rule and the equal rank of the sites are declared conventions inherited from II/12; the choice of candidates was protected by the obligatory scan, and the scan caught something twice (a second segmented weave; cross-line victories). **What it confirmed:** a partial yes for extension (10–15); extension is density-dependent; shell fit as a candidate rule ([III/1, 6.](../../III-frontier/III-01-candidate-laws_en.md)); the coincidence lemma as a theorem; the limit of the readout at small size with an identified cause, and the size diagnosis as a candidate. Direction of extension: the race and the readout on a larger system that separates two and four extensions — and the coordination-six line–plane–space race ([III/2, 8.](../../III-frontier/III-02-open-questions_en.md)).
