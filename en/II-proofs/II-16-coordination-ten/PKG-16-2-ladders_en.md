---
id: PKG-16-2
type: package
part_of: II-16
lang: en
pair: PKG-16-2-ladders_hu.md
pair_status: in-sync
doc_version: "1.3"
status: jovahagyva
builds_on: [PKG-16-1]
imports: zero
---

# PKG-16-2 — The beat ladders (computation package)

**The business of the package.** According to claims A1–A8 of [PKG-16-1](PKG-16-1-rulebook_en.md), it computes the ladder of all 805 entrants with streamed processing, runs the self-checks (A7) and the first three elements of the two-route rule (A8; the fourth, the projector seal, runs in PKG-16-4). The script: `shared/II-16-coordination-ten/PKG-16-2-ladders.py`.

## 1. Results

| Check | Result |
|---|---|
| ladders + moment cover (order ≤ 4, **on all 805 entrants**) | largest deviation from the combinatorial walk counts **4.6·10⁻¹³** — holds |
| trace sum 2,488,320 | largest deviation 4.7·10⁻¹⁰ (relatively 1.9·10⁻¹⁶) — holds |
| component count | everywhere according to the disconnection table (786 + 6) — holds |
| ladder classification | **804 classes on the 805 entrants** — the single coincidence is the constructional identity: J1 = the family member (1, 2, 3, 4, 5); there is no hidden coincidence |
| wrap-around, by machine route | all ≥ 8; notable values: J2 [288, 432] (the (0,2) step halves the 576 direction), KA2 [216, 576], J5 [12⁵]; the shortest of the family is 20736 (measured on the copy for the disconnected members) — holds |
| (i) sparse residual check (13×64 + 24×16 modes, seed 248,832) | with the corrected check the largest residual is **5.3·10⁻¹⁴** — holds |
| (iii) dense certification on small instances (13 patterns) | largest deviation **3.4·10⁻¹³** — holds |

## 2. Two corrections in the residual check (the fault was the check's, not the networks')

**On its first run the residual check signalled 12.8** — while the other two two-route elements (moment cover, small-dense) stood at 10⁻¹³. The source of the signal was the check's **own reference formula**: it computed the beat according to the hypercube special case (with per-axis phases), which is false on the mixed-step wirings. The formula was corrected to the wiring-vector phase; alongside this, the floating-point loss of the phase accumulation on the large ring (2.7·10⁻⁹) was eliminated by exact integer-remainder phase reduction. **A methodological note:** the redundancy of the four-element two-route form protects in exactly this way — two elements certified the ladders, and the third signalled its own error; no rule changed.

## 3. Verdict on this package

**Stands.** Every self-check and all three of the elements of the two-route form present here are met; the field is clean (804 classes, with only the intended identity).

## 4. Outgoing claims

- **L1:** all 805 ladders by the closed route; trace sum and component count in order everywhere.
- **L2:** the mark table is confirmed by the moment route as well (the single mark of the 3-walks separates all ten main pairs).
- **L3:** 804 ladder classes; a single, intended coincidence; the controls are all separate classes.
- **L4:** the wrap-around table verified by machine route, including the halving effect of the (0,2)/(2,0) steps.
- **L5:** the race (PKG-16-3) may build on the closed ladders, on the extended-precision route, with a tolerance of 10⁻⁸.
