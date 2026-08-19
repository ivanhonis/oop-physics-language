---
id: PKG-15-2
type: package
part_of: II-15
lang: en
pair: PKG-15-2-ladders_hu.md
pair_status: in-sync
doc_version: "1.3"
status: jovahagyva
builds_on: [PKG-15-1]
imports: zero
---

# PKG-15-2 — The beat ladders (computation package)

**The business of the package.** Building on claims A1–A8 of [PKG-15-1](PKG-15-1-rulebook_en.md), it computes the ladder of all 503 entrants, runs the five obligatory self-checks (A7), and the machine leg of the two-route rule (A8). The script: `shared/II-15-dimension-fourth-rung/PKG-15-2-ladders.py`.

## 1. The result of the self-checks

| Self-check | Result |
|---|---|
| (iv) trace sum | **165888 on all 503 networks** — holds |
| (i) three marks on the main four | **holds**, with one correction (see section 2): 3-walks 36 / 24 / 0 / 0; 4-walks 296 / 216 / 216 / 168; bipartite mark: none / none / present / present |
| (v) component count | main and control all 1; family **479 + 15 + 1**, the zero modes everywhere according to the disconnection table — holds |
| (ii) ladder classification | **502 classes on the 503 networks** — the single coincidence is the constructional identity: J1 = the family member (1, 2, 3, 4) (see section 3) |
| (iii) wrap-around, by machine traversal | main/control by direction: J1 [5184]; J2 [144, 144]; J3 **[24, 24, 36]**; J4 [12, 12, 12, 12]; K1 [16, 36, 36]; K2 [12, 36, 48]; K3 [8, 8, 18, 18]; K4 [48, 432] — all ≥ 8, and all even on the bipartite candidates; the shortest wrap-around of the family is 1728 — holds, with one correction (see section 2) |

## 2. Two corrections (following the II/14 precedent: the rulebook is not modified, the correction is recorded here)

**H1 — the J2 row of the distinctness table of §5 was wrong.** The rulebook stated 48 / 1188; the correct value is **24 / 216**. The source of the error: the enumerator used before the fixing built the diagonal steps twice (it counted a multigraph) — the ladder route, as an independent second route, caught it, and the corrected, duplication-free enumeration confirmed it. **The separation of the six pairs is complete as before:** the cross pairs are decided by the bipartite mark, the J1–J2 pair by the 3-walks (36 ≠ 24), and the J3–J4 pair by the 4-walks (216 ≠ 168); the 4-walk agreement of J2–J3 (216 = 216) is harmless, because that pair is separated by the bipartite mark.

**H2 — the literal form of the even-wrap-around condition of §3 was too broad.** The purpose of the condition is to protect the bipartite mark against the wrapping; in the family the wrap-around of 48 non-bipartite members is odd (the smallest such arises among the members with mixed step parity), and this is harmless. The correct reading: an even wrap-around is obligatory on the **bipartite** entrants — where it holds throughout (on the all-odd-step family members the parity is even as a consequence of a theorem) — while on the other entrants only the ≥ 8 requirement applies.

## 3. The finding of the ladder classification

The 503 entrants fall into **502 ladder classes**. The single coincidence is the intended constructional identity: the main candidate J1 is by definition the family member (1, 2, 3, 4) — the classifier correctly measures these as one, which is a consistency confirmation of the machinery, not a degeneracy. **There is no hidden coincidence:** the controls are all separate classes, and of the step-relabeling coincidences seen in II/14 not one is alive at this size — at a site count of 20736 a multiplier relabeling would have to satisfy four simultaneous congruences, and according to the measurement none does.

## 4. The machine leg (A8) — result

The self-test of the machine builder on three small weaves: largest deviation 2.3·10⁻¹⁴. The full batch ran (on a large machine, ~8–9 minutes per network): **all 32 targets computed by two routes** — the 8 main/control networks and the 24 drawn family members (seed: 20736, numpy PCG64). The per-network deviations are between 8.9·10⁻¹⁴ and 1.3·10⁻¹²; **the largest two-route deviation is 1.30·10⁻¹²** — four orders of magnitude below the classification quantum of 10⁻⁸.

## 5. Verdict on this package

**Stands.** All five self-checks (A7) are met — with two recorded corrections (H1, H2) — and the A8 two-route leg is complete: 32/32 targets, largest deviation 1.3·10⁻¹².

## 6. Outgoing claims (PKG-15-3 may build on these)

- **L1:** all 503 ladders computed by the closed Fourier route; trace sum 165888 everywhere.
- **L2:** the corrected table of the distinctness marks: 3-walks 36 / 24 / 0 / 0, 4-walks 296 / 216 / 216 / 168 — the separation of the six pairs is complete (H1).
- **L3:** 502 ladder classes; the single coincidence is the constructional identity J1 ≡ (1, 2, 3, 4); there is no hidden coincidence.
- **L4:** the wrap-around table verified by machine traversal; the scope of the even wrap-around refined (H2).
- **L5:** the race (PKG-15-3) may build on the closed ladders; the fixed value of the identity tolerance is 10⁻⁸ — four orders of magnitude above the measured two-route scale (1.3·10⁻¹²) and below the genuine ladder differences.
