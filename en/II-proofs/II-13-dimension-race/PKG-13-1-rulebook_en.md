---
id: PKG-13-1
type: package
part_of: II-13
lang: en
pair: PKG-13-1-rulebook_hu.md
pair_status: in-sync
doc_version: "1.3"
status: jovahagyva
builds_on: [II-12, II-11, I-06]
imports: zero
---

# PKG-13-1 — The rulebook of the extension race (derivation package)

**It contains no computation** — this package fixes the rules before anything is computed, so that no after-the-fact modification of the rules is possible.

---

## 1. Question (one sentence, fixed in advance)

At an identical number of contracts per site, does the cost structure favor the weave of higher extension — or the line, or the segmentation?

## 2. Inputs

- **[The race-rule convention of II/12](../II-12-network-race/proof_en.md):** a fixed contract budget must be placed; the equilibrium is the arrangement with the smallest total cost.
- **[III/1, 5. (equal rank of the sites)](../../III-frontier/III-01-candidate-laws_en.md):** there is no distinguished site — without this the collapse theorem of II/12 applies and the race is meaningless.
- **[I/6, the theorem of exclusion](../../I-language/I-06-identity_en.md):** the beat ladder must be filled from below, one instance per beat.
- **The trace-tie theorem of II/12:** at full filling the price of every network is twice the budget.
- **[The rebuilder and ball growth of II/11](../II-11-locality-readout/proof_en.md):** for the readout of the winner.
- **The machinery of II/12:** the network beat ladder as an eigenproblem ([Appendix B](../../appendix/B-machinery_en.md)).

## 3. The fixed system

- **16 sites**; smoothness contracts, of unit strength.
- **Exactly 4 contracts per site** — the total budget is thus 32 contracts, identically for every candidate.
- The equal rank of the sites is not an after-the-fact check but a construction principle: every candidate is a **weave network** — a group structure prescribes the same wiring pattern for every site, so the network is guaranteed to look the same from every site.
- Cost at $N$ instances: filling the beat ladder of the network from below, scanned from $N = 1$ to 16.

## 4. The candidates

| Candidate | Weave | Structure |
|---|---|---|
| **J1 — line** | a 16-ring, with first- and second-neighbor contracts | thickened line |
| **J2 — plane** | a 4×4 lattice with periodic boundary (torus) | a genuine two-extension weave |
| **J3 — segmented** | two separate, thickened 8-rings | J1 broken in two |

**Honesty scan (obligatory):** every variant of the line family with 4 contracts per site (every two-step wiring of the 16-ring) must also be computed, so that no candidate better than the declared one is left out of the family.

## 5. Derived lemma — the coincidence of the candidate set

The planned fourth candidate was the four-extension weave (the 2×2×2×2 hypercube: four contracts per site, each in a different direction). During the fixing it turned out that **on 16 sites this is the same network as the J2 torus**. The derivation is two steps: a two-extension weave of side length 2 is exactly a 4-ring; and weaves can be assembled direction-pair by direction-pair — so the 2×2×2×2 four-extension weave is identical to the (4-ring) × (4-ring) assembly, which is the 4×4 torus.

**Consequence, stated:** at this size two and four extensions cannot even be distinguished — the race decides the question *line versus non-line versus segmented*; the two-or-four question requires a larger system (a fixed direction of extension, not the subject of this proof).

## 6. Pre-registered facts following from theorems (not predictions)

1. At $N = 1$ every candidate pays 0 (every network has one common zero mode).
2. At $N = 2$ J3 wins: its two components give two zero modes, the connected candidates already pay.
3. At $N = 16$ a tie at 64 is obligatory (the trace-tie theorem).

**A prediction for the substantive range $3 \le N \le 15$: deliberately none** — after the lesson of II/12 this proof has an open outcome.

## 7. Verdict rule (fixed)

- For every $N$ the candidate with the strictly smallest cost wins; a tie must be reported as a tie.
- **Deciding the main question:** the proof says yes to extension if J2 beats J1 and J3 at the same time over a connected, substantive part of the range $3 \le N \le 15$; it says no if there is no such range. A partial outcome (winning in patches) must be recorded as a partial result, together with the location of the patches.
- No new candidate, new filling filter or new cost definition may be introduced afterwards; extension only in a new package, without modifying this one.

## 8. The readout protocol (fixed for PKG-13-4)

- On the winner the rebuilder of II/11 runs: pairwise closeness from the finished state; it is not given the neighbor count — this is singled out by the jump of the closeness list.
- A filling at a closed degree must be chosen (an unambiguous state); if every winning filling of the winner is degenerate, the even mixture of the zero-cost subspace must be computed, with an exact projector (the control method of II/11).
- The extension reading from ball growth: the line gives $+2$ per step; the recorded sequence of the torus weave is 1, 5, 11, 15, 16. The two-or-four reading is undecidable at this size (point 5) — the protocol may not even claim it.

## 9. Import ledger

New import: **zero.** The race rule and the equal rank of the sites are declared conventions inherited from II/12; the weave construction is the realization of equal rank, not a new assumption; the choice of candidates is protected from the charge of cherry-picking by the obligatory scan.

## 10. Verdict on this package

**Stands.** The rulebook is closed; it has one substantive derived result (the candidate-coincidence lemma, point 5), which sharpened the question: on 16 sites the race is about the line–plane–segmented triple.

## 11. Outgoing claims (PKG-13-2 may build only on these)

- **A1:** system = 16 sites, 32 units of smoothness contract, 4 per site, by weave construction.
- **A2:** candidates = J1 (line), J2 (torus ≡ hypercube), J3 (two pieces), plus the obligatory scan of the line family.
- **A3:** cost = filling the beat ladder from below, $N = 1..16$.
- **A4:** pre-registered facts: at $N=1$ all pay 0; at $N=2$ J3 wins; at $N=16$ a tie at 64.
- **A5:** verdict rule according to point 7; there is no prediction.
- **A6:** readout protocol according to point 8; the two-or-four question is undecidable at this size and may not be claimed.
