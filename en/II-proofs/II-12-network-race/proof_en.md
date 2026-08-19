---
id: II-12
type: proof
lang: en
pair: proof_hu.md
pair_status: in-sync
doc_version: "1.3"
status: bukott
builds_on: [II-11, II-01, I-06]
imports: "convention: the race rule (a fixed, obligatory budget); the candidate import of the rescue proof: equal rank of the sites (III/1, 5.)"
---

# II/12. The network race — the failure of the selection candidate

**The question.** The question of selection ([III/2, 2.](../../III-frontier/III-02-open-questions_en.md)) put to a live test: if the contract network itself is the variable, which arrangement wins? The candidate stated in advance: connectedness is enforced by exclusion — geometry is born where many excluding instances share the smoothness contract; the prediction, refutably: the geometric network wins. The race rule — a comparison convention declared in advance: a fixed contract budget must be placed, and the equilibrium is the arrangement with the smallest total cost.

**The system and the contract.** Twelve sites; a smoothness budget of 12 coupling units, freely divisible; $N$ excluding instances, scanned from $N = 1$ to 12. The cost: filling the beat ladder of the contract network from below — according to the [theorem of exclusion](../../I-language/I-06-identity_en.md) at most one instance per beat. The bond side has already been decided by hand (the pairwise covering wins with zero cost — the old III/2, 2.); the computed race is therefore that of the smoothness contract. The announced competitors: **dust** (six pairwise contracts, at double strength), **dense** (everyone-with-everyone), **ring**.

**The computation.** The lattice machinery on networks: the matrix of the contract network, the beat ladder as an eigenproblem, filling from below, for every $N$.

**The result** (total cost at $N$ instances):

| N instances | 4 | 6 | 8 | 9 | 10 |
|---|---|---|---|---|---|
| dust | 0 | 0 | 8 | 12 | 16 |
| ring | 1.54 | 4.54 | 9.54 | 12.54 | 16.27 |
| dense | 6.55 | 10.91 | 15.27 | 17.45 | 19.64 |
| a single fat contract | 0 | 0 | 0 | 0 | 0 |

**The prediction failed.** Dust beats the ring at every filling, dense is last everywhere — and the real winner is cruder even than dust.

**Theorem: the collapse theorem.** The smoothness cost is never negative; the arrangement that gathers the whole budget into a single contract reaches zero up to eleven instances (eleven decoupled zero modes: ten empty sites and the joint mode of the pair) — hence it is an exact winner. The escape route is the **empty site**: the instances park on the contract-free sites. Together with its counterpart on the bond side: **none of the vetted contracts selects a geometry — with a free network every budget collapses into a corner.**

**Theorem: the trace tie.** At full filling ($N = 12$) every network pays exactly twice the budget — the sum of the whole ladder is network-independent. At full filling the race is a tie in principle.

**The rescue proof.** The parking place is closed by a single statement — the **equal rank of the sites** ([III/1, 5.](../../III-frontier/III-01-candidate-laws_en.md), a new candidate import): there is no distinguished site, the network looks the same from every site. With twelve units of contract this gives exactly two per site; the competitors are the ring decompositions: one 12-ring, two hexagons, three squares, four triangles. The winners:

| N instances | 1–4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|
| winner | disconnected (0) | ring (2.54) | two hexagons (4) | ring (6.54) | ring (9.54) | three squares (12) | segmentations (16) | three-way tie (20) | tie (24) |

Density enforces connectedness — up to four instances the disconnected one still wins (one free zero mode per component), and from five onwards the single connected ring is alive — but the sharp law is missing: at half filling the splitting in two, and at 9–10 the degree-resonant segmentation, strike back.

**Closing the loop.** On the homogeneous winner (the ring, 7 instances — a closed degree, an unambiguous state) the rebuilder of [II/11](../II-11-locality-readout/proof_en.md) reads out the geometry: the neighbor closeness is 0.436, everything further below 0.03 (a fifteenfold jump); 12/12 edges correct; ball growth +2 per step — one extension. Where geometry wins, it is also readable.

**Checking against reality.** The tendency to dust is not a fault of the machinery — physics measures it: a half-filled chain distorts by itself into a pairwise pattern as soon as the strength of the couplings becomes free ([the Peierls distortion; the measured alternating bond length of polyacetylene](../../appendix/C-benchmarks_en.md)), and there too the connected lattice is saved by a separate mechanism — the stiffness of the lattice. The collapse theorem of the language is the extreme, exact form of this tendency.

**Import ledger:** the race rule (an obligatory, fixed budget) — a convention declared in advance; the new, candidate import of the rescue proof is the equal rank of the sites ([III/1, 5.](../../III-frontier/III-01-candidate-laws_en.md)). **What it confirmed:** a failure proof — the naive form of the exclusion candidate failed, and the yield of the failure is two theorems (collapse, trace tie), one half-result (density enforces connectedness within the homogeneous class) and one root signal: the source of the trouble is that in the language the contract is a free resource — in physics the coupling is carried by the instances; selection may be decided where the contracts themselves are born ([III/2, 7.](../../III-frontier/III-02-open-questions_en.md)).
