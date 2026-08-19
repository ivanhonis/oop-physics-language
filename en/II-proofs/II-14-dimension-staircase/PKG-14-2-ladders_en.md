---
id: PKG-14-2
type: package
part_of: II-14
lang: en
pair: PKG-14-2-ladders_hu.md
pair_status: in-sync
doc_version: "1.3"
status: jovahagyva
builds_on: [PKG-14-1]
imports: zero
---

# PKG-14-2 — The beat ladders (derivation package)

**Builds on:** [PKG-14-1](PKG-14-1-rulebook_en.md) (A1–A4, A7) · **Does not contain:** the filling race — the ladders are only computed here, the race is the business of PKG-14-3. · **Computation code:** `PKG-14-2-ladders.py`

---

## 1. Question

What is the beat ladder of the three candidates, the plane control and the complete fixed scan ($a<b<c\le12$, 220 family members), checked by two independent methods?

## 2. Inputs

PKG-14-1: A1 (system), A2 (field and scan), A3 (cost definition), A4 (pre-registered facts), A7 (bipartite-mark self-check). Machinery: the eigenproblem of the network beat ladder ([Appendix B](../../appendix/B-machinery_en.md), tool 2) and the closed Fourier form of the weaves as an independent check.

## 3. The computation

The ladder of all **224 networks** is computed twice: as the eigenproblem of the adjacency-list matrix of the contract network (machinery), and from the closed formula of the weaves (Fourier form).

## 4. Result — the ladders of the field (cost in coupling units; ×n = shelf width)

| Network | The start of the ladder | Shelves | Top |
|---|---|---|---|
| **J1 — line** | 0; 0.0021 (×2); 0.0084 (×2); 0.0190 (×2); 0.0337 (×2); … | 255 | 8.631 |
| **J2 — plane (16×32)** | 0; 0.0769 (×2); 0.2291 (×2); 0.3045 (×6); 0.5277 (×4); … | 94 | 8.988 |
| **J3 — space (8×8×8)** | 0; 0.5858 (×6); 1.172 (×12); 1.757 (×8); 2 (×6); 2.586 (×24); … | 25 | 12 |
| **plane control (8×64)** | 0; 0.0193 (×2); 0.0769 (×2); 0.1722 (×2); 0.3045 (×2); … | 122 | 8.945 |

**The complete ladder of J3** (25 shelves): 0; 0.5858 (×6); 1.172 (×12); 1.757 (×8); 2 (×6); 2.586 (×24); 3.172 (×24); 3.414 (×6); 4 (×39); 4.586 (×60); 5.172 (×12); 5.414 (×24); 6 (×68); 6.586 (×24); 6.828 (×12); 7.414 (×60); 8 (×39); 8.586 (×6); 8.828 (×24); 9.414 (×24); 10 (×6); 10.24 (×8); 10.83 (×12); 11.41 (×6); 12 (×1). **Its degree boundaries (closed degrees):** 1, 7, 19, 27, 33, 57, 81, 87, 126, 186, 198, 222, 290, 314, 326, 386, 425, 431, 455, 479, 485, 493, 505, 511, 512.

## 5. The scan — 220 family members, and what it caught

- The 220 members fall into **216 different ladders**; each of the four coinciding pairs is a relabeling of the step set (multiplying the steps by three — 3 is relatively prime to 512, so it is the same weave relabeled). Among them J1 itself: (1,2,3) and (3,6,9) are the same network.
- **What the scan caught — point 2 of the fixed A4 does not hold for the family.** For the declared field it does (J1, J2, J3 and the control are all connected, with exactly 1 zero mode each — see point 6), but in the scanned family **20 disconnected weaves live**: exactly those triples all of whose steps are even — 19 members fall into two components, and (4,8,12) into four. The extension written into A4 ("every entrant is connected") was a derivation error; the rulebook is not modified, and the correction is recorded here and in the synthesis. Consequence for the race: the low-filling disconnected advantage (one free zero mode per component — II/13) **does play after all**, as a fixed member of the field.

## 6. Self-checks

1. **Trace sum:** 3072 on all 224 networks, deviation below $10^{-12}$ — the cover of the trace tie (A4, 3.) holds.
2. **Zero modes:** J1: 1, J2: 1, J3: 1, control: 1 (A4, 2. holds for the declared field); on the scan members the number of zero modes is exactly the common divisor of the steps and 512 (200 members: 1; 19 members: 2; one member: 4).
3. **Machinery versus closed formula:** the largest deviation is $7.9\cdot10^{-14}$ (machine precision), across all 224 networks.
4. **The bipartite mark (A7):** the ladder of J3 is **exactly symmetric** about 6 (deviation $1.8\cdot10^{-15}$), those of J1 and J2 are not (deviation 3.37 and 3.01 respectively) — the three candidates are pairwise distinct networks, and the coincidence trap of II/13 provably does not apply here.

## 7. Observations (race-free)

- The ladder of J3 consists of the fewest shelves (25), and the widest ones (68 beats on the shelf at 6) — the fingerprint of the high symmetry of the space weave; its top is 12, the obligatory mirror of a bipartite network.
- The start of J1 is strikingly soft (0.0021): the long waves of the thickened line are almost free — at low filling this will be its strength.
- Stretching softens: the ladder of the 8×64 control starts deeper (0.0193) than that of the 16×32 (0.0769) — in its stretched form the plane "becomes line-like".

## 8. Import ledger and verdict

New import: **zero.** The boundary of the package held: no filling sum was computed. **Verdict: stands** — together with the catch of point 5, which is not a fault of the package but the yield of the obligation to scan.

## 9. Outgoing claims (PKG-14-3 may build only on these)

- **B1:** the ladders of J1, J2, J3 and the control according to point 4 — these are the reference values.
- **B2:** the complete fixed field enters the race: the four declared networks and all 216 ladder classes of the scan, including the 20 disconnected members — the correction to point 2 of A4 (point 5) must be reported in the synthesis.
- **B3:** PKG-14-3 is obliged to recompute the ladders independently by a new code path, and to race them only after agreement.
- **B4:** no filling race took place in this package — the question of the winner is untouched.
- **B5:** for checking the shell logic, the degree boundaries of J3 are fixed according to point 4.
