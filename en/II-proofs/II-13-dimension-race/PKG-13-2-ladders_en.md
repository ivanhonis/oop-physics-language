---
id: PKG-13-2
type: package
part_of: II-13
lang: en
pair: PKG-13-2-ladders_hu.md
pair_status: in-sync
doc_version: "1.3"
status: jovahagyva
builds_on: [PKG-13-1]
imports: zero
---

# PKG-13-2 — The beat ladders (derivation package)

**Builds on:** [PKG-13-1](PKG-13-1-rulebook_en.md) (A1–A4) · **Does not contain:** the filling race — the ladders are only computed here, the race is the business of PKG-13-3. · **Computation code:** `PKG-13-2-ladders.py`

---

## 1. Question

What is the beat ladder of the three candidates and of the complete line-family scan, checked by two independent methods?

## 2. Inputs

PKG-13-1: A1 (system), A2 (candidates and the obligatory scan), A3 (cost definition), A4 (pre-registered facts). Machinery: the network beat-ladder computation of [II/12](../II-12-network-race/proof_en.md) ([Appendix B](../../appendix/B-machinery_en.md), tool 2), supplemented with the closed formula of the weave networks as an independent check.

## 3. The computation

The ladder of every network is computed twice: as the eigenproblem of the matrix of the contract network (machinery), and — where the weave is built from a ring — from the closed form of the weaves (analytic formula). The segmented candidate moreover in two independent constructions: as a member of the 16-site weave, and as two separate 8-rings.

## 4. Result — the ladder of the three candidates (cost, in coupling units; ×n = this many beats at this degree)

| Candidate | Ladder |
|---|---|
| **J1 — line** | 0; 0.738 (×2); 2.586 (×2); 4; 4.434 (×2); 4.649 (×2); 5.414 (×2); 6 (×2); 6.180 (×2) |
| **J2 — plane (torus)** | 0; 2 (×4); 4 (×6); 6 (×4); 8 |
| **J3 — segmented** | 0 (×2); 2.586 (×4); 4 (×2); 5.414 (×4); 6 (×4) |

## 5. The scan — all 21 members of the line family, in 7 different ladders

| Step pairs | Zero modes | The start of the ladder |
|---|---|---|
| (2,4), (4,6) — **this is J3 itself** | 2 | 0; 0; 2.586… |
| (2,6) — **a second segmented weave** | 2 | 0; 0; 4; 4… |
| (1,2), (2,7), (3,6), (5,6) — **the class of J1** | 1 | 0; 0.738; 0.738… |
| (1,7), (3,5) | 1 | 0; 1.172; 1.172; 4… |
| (1,3), (1,5), (3,7), (5,7) | 1 | 0; 1.387; 1.387; 2.918… |
| (1,6), (2,3), (2,5), (6,7) | 1 | 0; 1.820; 1.820; 2.586… |
| (1,4), (3,4), (4,5), (4,7) | 1 | 0; 2; 2; 2.152… |

## 6. Self-checks

1. **Trace sum:** exactly 64 on all 24 computed networks — the cover of the trace-tie theorem (A4, 3.) holds.
2. **Zero modes:** J1: 1, J2: 1, J3: 2 — according to the pre-registered facts of A4.
3. **Analytic versus machinery:** largest deviation $2 \cdot 10^{-15}$ (machine precision).
4. **The two independent constructions of J3** (as a weave member, and as two separate rings) give the same ladder, to within $6 \cdot 10^{-15}$.
5. **The ladder of J2 is exactly the binomial ladder of the hypercube** (0; 2×4; 4×6; 6×4; 8 — the widths of the degrees are 1-4-6-4-1), to machine precision: an independent, spectral confirmation of the coincidence lemma of [PKG-13-1](PKG-13-1-rulebook_en.md).

## 7. Observations (race-free)

- The ladder of J2 consists of the fewest degrees, with the widest shelves — the fingerprint of the high symmetry of the weave.
- The class of J1 has the softest start among the connected weaves (0.738); every other connected family member starts higher.
- The obligation to scan caught something: **two** segmented weaves live in the family, with different ladders — the (2,6) one (two 8-rings, with first+third neighbor wiring) enters the race as a new segmented candidate. The 21 members collapse into 7 ladders; these 7 go into the race of PKG-13-3.

## 8. Import ledger and verdict

New import: **zero.** The boundary of the package held: no filling sum was computed. **Verdict: stands.**

## 9. Outgoing claims (PKG-13-3 may build only on these)

- **B1:** the ladders of J1, J2, J3 according to point 4 — these are the reference values.
- **B2:** all 7 ladder classes of the scan enter the race, among them the second segmented weave (2,6).
- **B3:** PKG-13-3 is obliged to recompute the ladders independently, and to race them only after agreement.
- **B4:** no filling race took place in this package — the question of the winner is untouched.
