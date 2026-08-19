---
id: PKG-16-4
type: package
part_of: II-16
lang: en
pair: PKG-16-4-readout_hu.md
pair_status: in-sync
doc_version: "1.4"
status: jovahagyva
builds_on: [PKG-16-3, PKG-15-4, II-11]
imports: zero
---

# PKG-16-4 — The readout (computation package)

**The business of the package.** Closing the loop on the winner of the standing band of highest extension ([PKG-16-3, V5](PKG-16-3-race_en.md)): on the J5 native weave, at the closed degree N = 130,902, with the protocol of [§8 of the rulebook](PKG-16-1-rulebook_en.md) and the new, sampling projector seal. The script: `shared/II-16-coordination-ten/PKG-16-4-readout.py`.

## 1. Results

| Measurement | Value |
|---|---|
| closed degree | the gap above the 130,902nd degree is **0.267949192 = 2 − √3**, exactly |
| neighbor closeness | +0.127554 |
| **antipodal echo** (obligatory row) | **−0.010955** — negative, **8.6%** of the neighbor |
| jump (on the signed list) | after the **10th place**, 8.2-fold — exactly the ten unit steps |
| old absolute rule | likewise after the 10th place, 7.3-fold |
| band sentinel | **S = 7.29** (threshold 2); strongest rejected: the (0,0,1,1,1) triple-diagonal class (−0.0175) |
| completeness ledger | **1,244,160 / 1,244,160; phantom 0; missing 0** |
| ball (r = 0..5) | **1, 11, 61, 231, 681, 1683** — exactly the fourth-order sequence |
| projector seal (64+64 modes, seed 248,832) | residual branch **5.1·10⁻¹⁴**; transform branch **9.4·10⁻¹⁶** — holds |

## 2. Verdict

**Stands — all four conditions and both branches of the seal.** The native winner reads itself as five-extensional from the inside: the extension number is the same from outside (the race) and from inside (the ball) — five.

## 3. Notes

- **The echo series has grown and is weakening:** at a wrap-around of 12, 3D −16%, 4D +17.4%, **5D −8.6%** — all harmless; the size decision was vindicated for the third time.
- **The recurring pattern for the third time:** the strongest rejected is again a nearby diagonal class, not the mirror echo.
- **The new seal form works:** the residual branch with the graph-built adjacency, the transform branch with the direct (non-FFT) summation of the G table — both at machine precision.

## 4. Outgoing claims

- **R1:** the winner of the fifth rung has a fourth-order ball from the inside — the native rung is five inside and out.
- **R2:** the echo series has three elements, all at a wrap-around of 12, all harmless.
- **R3:** the sampling projector seal is a vetted, working form — a substitute for the dense seal on a large system stands.
