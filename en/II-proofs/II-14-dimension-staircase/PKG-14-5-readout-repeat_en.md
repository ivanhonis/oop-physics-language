---
id: PKG-14-5
type: package
part_of: II-14
lang: en
pair: PKG-14-5-readout-repeat_hu.md
pair_status: in-sync
doc_version: "1.3"
status: jovahagyva
builds_on: [PKG-14-4, PKG-14-1, II-11]
imports: "zero new item (the sentinel threshold — a factor of two — is a declared convention)"
---

# PKG-14-5 — The re-readout with a fixed scope (repetition package)

**The business of the package.** The size diagnosis of [PKG-14-4](PKG-14-4-readout_en.md) — that on the 12-weave the readout is clean — was born outside the scope, as a candidate. This package repeats the same readout with a fixed scope, building in the two rule-lessons of II/14, so that the candidate may step up to a theorem — or fail explicitly.

## 1. The fixed scope (before the run)

- **System:** the J3 space weave, 12×12×12, coordination six, 5184 units of smoothness contract; wrap-around of 12 steps in every direction.
- **Filling (a deterministic rule):** the closed degree nearest to half filling, from above.
- **Correction 1 — signed jump:** the jump is to be sought on the signed closeness list, not on its absolute value; the antipodal class must be reported separately, together with its sign. (Closing the sign gap of II/14.)
- **Correction 2 — band sentinel:** the ratio of the weakest accepted and the strongest rejected closeness must be reported; below a factor of two the reading is partial. The threshold is a declared convention; for comparison: the failed case of the 8-weave would give 1.0. (Widening the narrow "exact agreement" form.)
- **Completeness ledger:** found / missing / phantom, all three with numbers.
- **Ball reading:** up to r ≤ 5 (validity: 2r < 12), against the quadratic reference sequence of space: 1, 7, 25, 63, 129, 231 (increment 4r² + 2).
- **Two-route rule:** the ladder and the projector in closed form and by machine eigenproblem as well.
- **Verdict conditions in advance:** V1 — the closed degree holds; V2 — 5184/5184, zero phantom, zero missing; V3 — the ball is exact; V4 — sentinel ≥ 2. If all hold → **stands**; if any fails → partial, naming the failed condition.

## 2. Results

| Measurement | Value |
|---|---|
| ladder by two routes | agreement to within 1.1·10⁻¹⁴ |
| closed degree | N = 934 (= 794 + a shelf of 140); half filling 864; gap above the degree 0.2679 |
| projector by two routes | agreement to within 2.8·10⁻¹⁶ |
| neighbor closeness | +0.166146 |
| **antipodal echo** | **−0.026620** — its sign is negative, its magnitude **16.0%** of the neighbor |
| jump (on the signed list) | after the 6th place, **8.9-fold** |
| band sentinel | **S = 2.84** (threshold: 2) — the strongest rejected is not the antipodal but the (1,1,1) body-diagonal class (−0.058427) |
| old absolute rule (for comparison) | the jump is likewise after the 6th place, but only 2.8-fold |
| completeness ledger | **5184/5184; phantom 0; missing 0** |
| ball (r = 0..5) | **1, 7, 25, 63, 129, 231** — increment 6, 18, 38, 66, 102, exactly 4r² + 2 |

## 3. Verdict

**Stands — all four conditions fixed in advance are met.** The size diagnosis of PKG-14-4 goes from candidate to theorem: at coordination six the antipodal echo of the 8-weave is a size artifact — on the 12-weave the loop closes without gaps, and the echo falls to 16% of the neighbor closeness (on the 8-weave it was 100%, with exact agreement).

**A bonus finding, with a number:** the benefit of the signed rule is measurable — on the signed list the jump is 8.9-fold, on the absolute-value one at the same place only 2.8-fold, because the second half of the list is led by negative classes. The correction therefore more than triples the safety band. And at this size the band sentinel is no longer limited by the antipodal echo but by an ordinary nearby class (the body diagonal) — the mirror echo has dropped out of the range in question.

## 4. What this package does not prove

It says nothing about coordination eight or about other weaves (BCC, hypercube) — there the echo question is the business of II/15's own sentinel. The threshold of two is a convention, not a derived number.

## 5. Outgoing claims

- **K1:** on the 12-weave of space the readout is complete: 5184/5184, zero phantom, and the ball is exactly quadratic up to r = 5.
- **K2:** the antipodal echo dies away with size: 100% (exact) on the 8-weave, 16% on the 12-weave, with a negative sign; at this size it is no longer the limit of the sentinel.
- **K3:** the signed jump rule is sharper than the absolute one (8.9 versus 2.8) — the reference basis of the protocol of II/15.
- **K4:** the empirical support for the size decision of II/15 — that a wrap-around of 12 is sufficient — is a fact confirmed within scope at coordination six.
