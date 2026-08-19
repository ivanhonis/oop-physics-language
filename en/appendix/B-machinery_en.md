---
id: APP-B
type: appendix
lang: en
pair: B-machinery_hu.md
pair_status: in-sync
doc_version: "1.3"
status: ervenyes
---

# B) The computing machinery

Every number in Part II comes from one of four tools, each building on the previous.

(1) **Closed forms**: where the system is small, the minimum can be computed by hand ([II/1](../II-proofs/II-01-pair-bond/proof_en.md): $L = \tfrac{1}{2} + \tfrac{1}{2}\cos^2(\theta_1 - \theta_2)$; the instance-level branch of [II/5](../II-proofs/II-05-triangle/proof_en.md); the two theorems of [II/12](../II-proofs/II-12-network-race/proof_en.md); the coincidence lemma of [II/13](../II-proofs/II-13-dimension-race/proof_en.md)).

(2) **The lattice machinery**: dividing the sites into cells, the matrix of the contracts, self-rotating patterns and the cost ladder as an eigenproblem; refining the subdivision gives the continuous answer, a coarse one the lattice answer ([II/3](../II-proofs/II-03-box/proof_en.md), [II/4](../II-proofs/II-04-hydrogen-atom/proof_en.md), [II/6](../II-proofs/II-06-universality/proof_en.md), [II/7](../II-proofs/II-07-bowl-magic-numbers/proof_en.md); in II/12–II/14 the same runs on networks: the matrix of the contract network, the beat ladder, filling from below).

(3) **The degree race**: computed pairwise repulsion integrals on the lattice patterns, followed by an exact, exhaustive search of all arrangements within a degree ([II/8](../II-proofs/II-08-exclusion-vs-repulsion/proof_en.md)).

(4) **The exact minimum of the full state space**: on small pieces, handling the full weight-vector space with rounding-free error in principle — eigenproblem, time evolution, view computation ([II/5](../II-proofs/II-05-triangle/proof_en.md), [II/9](../II-proofs/II-09-kagome/proof_en.md), [II/10](../II-proofs/II-10-internal-witness/proof_en.md), [II/11](../II-proofs/II-11-locality-readout/proof_en.md)).

[II/11](../II-proofs/II-11-locality-readout/proof_en.md) extended the machinery with two elements: the pairwise closeness map of the finished state and the rebuilder working from it without labels; and the exact projector of the degenerate zero-cost subspace. A further supplement for II/13: the views of free excluding instances are computed exactly from the instance correlations (the accelerated form of tool 4). For II/14: the closed Fourier form of the weave ladders as an obligatory counter-check alongside the machinery, and the incidence-matrix construction ($L = B^{\mathsf T} B$) as an independent code path for the precondition check of the race.

Built-in accuracy checks: the analytic value of the basic repulsion integral ($\sqrt{\pi/2} \approx 1.2533$; on the lattice 1.246, 0.6%); the exact reproduction of the analytic 9/16 of the frozen covering (II/9); the agreement of the 12-object Kagome piece with the published exact value; the agreement of the bond price of the 12-ring with the published exact value, the exact trace of the control projector (132) and the closeness spread of the control ($10^{-16}$) (II/11); the analytic cover of the two theorems of II/12 (the zero cost of the fat-contract arrangement and the exact full-filling trace sum); the double computation of the ladders of II/13 (machinery and closed formula, agreeing to $10^{-15}$), the two independent constructions of the segmented one, and the binomial ladder of the plane as the spectral confirmation of the coincidence lemma; the double computation of II/14 on all 224 networks ($7.9\cdot10^{-14}$), the exact trace sum of the 224 networks (3072), the exact mirror symmetry of the bipartite mark of the space weave ($10^{-15}$), and the exact $4r^2+2$ law of the 12×12×12 ball up to $r=5$.
