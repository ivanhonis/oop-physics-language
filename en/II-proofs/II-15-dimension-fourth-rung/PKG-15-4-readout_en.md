---
id: PKG-15-4
type: package
part_of: II-15
lang: en
pair: PKG-15-4-readout_hu.md
pair_status: in-sync
doc_version: "1.3"
status: jovahagyva
builds_on: [PKG-15-3, PKG-14-5, II-11]
imports: zero
---

# PKG-15-4 — The readout (computation package)

**The business of the package.** Closing the loop on the winner of the standing band of highest extension ([PKG-15-3, V6](PKG-15-3-race_en.md)): on the J4 hypercube weave, at the closed-degree filling N = 11075, with the protocol of [§8 of the rulebook](PKG-15-1-rulebook_en.md). The script: `shared/II-15-dimension-fourth-rung/PKG-15-4-readout.py`.

## 1. Results

| Measurement | Value |
|---|---|
| closed degree | the gap above the 11075th degree is **0.267949192 = 2 − √3**, exactly the expected value |
| neighbor closeness | +0.142661 |
| **antipodal echo** (obligatory row) | **+0.024836** — its sign this time is **positive**, its magnitude **17.4%** of the neighbor |
| jump (on the signed list) | after the **8th place**, 5.7-fold — it singles out exactly the eight unit steps |
| old absolute rule (for comparison) | likewise after the 8th place, 5.4-fold |
| band sentinel | **S = 5.37** (threshold: 2) — the strongest rejected is not the antipodal but the (0,1,1,1) triple-diagonal class (−0.026563) |
| completeness ledger | **82944/82944; phantom 0; missing 0** |
| ball (r = 0..5) | **1, 9, 41, 129, 321, 681** — exactly the cubic reference sequence, both at the verdict bound r ≤ 3 and over the full reporting range r ≤ 5 |
| two-route seal | between the closed (FFT) and machine (dense eigenproblem, with eigenvectors) routes of the projector the largest deviation is **1.67·10⁻¹⁵** |

## 2. Verdict

**Stands — all four conditions fixed in advance are met, and so is the two-route seal.** The winner of the fourth rung reads itself as four-extensional from the inside: the rebuilder blindly, completely and without phantoms gives back all 82944 contracts, and the ball is exactly cubic to the end of the validity range. The failure branch (the reserved name PKG-15-5) was not needed.

## 3. Notes

- **The size decision was vindicated.** At a wrap-around of 12 the bipartite echo (17.4%) is outside the critical zone — the three-extension sample of [PKG-14-5](../II-14-dimension-staircase/PKG-14-5-readout-repeat_en.md) (16%) holds at coordination eight and in four extensions as well. The echo series has grown: 3D-six, wrap-around 8: 100% (failure); 3D-six, 12: −16%; 4D-eight, 12: +17.4%.
- **The signed rule added less here** (5.7 versus 5.4), because this time the sign of the echo is positive — the sentinel, however, catches independently of the sign; the protocol is good for both cases.
- **A recurring pattern:** in both readouts the strongest rejected class is a nearby diagonal class (there (1,1,1), here (0,1,1,1)), not the mirror echo — at these sizes the limit of the sentinel is ordinary geometry, not symmetry.

## 4. Outgoing claims

- **R1:** the winner of the fourth rung has a cubic ball from the inside — in the winning band the extension number is the same from outside (the race) and from inside (the ball): four.
- **R2:** the size of the bipartite echo is governed by the wrap-around, and at a wrap-around of 12 it is harmless independently of coordination and extension.
- **R3:** the two-route seal is 1.7·10⁻¹⁵ — the closed and the machine route agree to machine precision.
