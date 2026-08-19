---
id: PKG-15-3
type: package
part_of: II-15
lang: en
pair: PKG-15-3-race_hu.md
pair_status: in-sync
doc_version: "1.3"
status: jovahagyva
builds_on: [PKG-15-2]
imports: zero
---

# PKG-15-3 — The race (computation package)

**The business of the package.** Building on the ladders of [PKG-15-2](PKG-15-2-ladders_en.md), it runs the race from N = 1 to 20736 on all 503 entrants, pronounces the staircase verdict according to [§7 of the rulebook](PKG-15-1-rulebook_en.md), checks the pre-registered facts, and answers the three registered questions. The script: `shared/II-15-dimension-fourth-rung/PKG-15-3-race.py`.

## 1. The pre-registered facts — all hold

At N = 1 all 503 entrants pay zero; at N = 2 exactly the 16 disconnected members stand at zero; at N = 3 the three-copy (3, 6, 9, 12) alone; at full filling the price of every entrant is 165888, to within a deviation of 8.4·10⁻¹² on the primary (extended-precision) route.

## 2. The winner table on the main four — and the verdict

| Winner | Range | Length |
|---|---|---|
| tie (all four) | 1 | 1 |
| J1 — line | 2 .. 4217 | 4216 |
| J2 — plane | 4218 .. 7964 | 3747 |
| **J4 — four extensions** | **7965 .. 15996** | **8032** |
| **J3 — space** | **15997 .. 20734** | **4738** |
| tie (J3 + J4) | 20735 | 1 |
| tie (all four) | 20736 | 1 |

All three upper bands are connected and patch-free; the band of four extensions is the largest of all, and **half filling (10368) sits inside the four-extension band**.

**Verdict: partial — the band structure is complete, but the order is not monotone.** The complete-yes definition of §7 (plane → space → four extensions with increasing density) is not met, and the named "stops at three" case does not hold either, because the fourth rung does stand. The measured finding, named: **the fourth rung stands — it wins the central density band — but the top belongs to three: at the top the staircase turns back** (line, plane, four extensions, space).

## 3. The answers to the three registered questions

**Q-a (shell fit): does not hold sharply.** The distance of the band boundaries from the nearest closed degree of the incoming winner: 1, 3, 112 and 2 fillings respectively. The band boundary is the intersection point of the cost curves, not the incoming shelf boundary — the scope of the shell rule ([III/1, 6.](../../III-frontier/III-01-candidate-laws_en.md)) is to be narrowed accordingly.

**Q-b (the mirror question): the width does not decide — the shape decides, and the mirror rule is confirmed in a sharpened form.** The ladder width of the two bipartite candidates is identical (the highest beat of both is exactly 16), yet the order is definite. The upper half (N > 10368) is won **exclusively by the pair carrying the mirror mark** — every single upper filling belongs to J3 or J4 — which is the sharpest confirmation so far of [III/1, 7.](../../III-frontier/III-01-candidate-laws_en.md). Within the pair, however, the order reverses at the top: the full end is the mirror image of the sparse end (there the race is about the holes), and when sparse the lower extension is the cheaper one — this is why space beats four extensions at the top. A fine seal of this is the **exact** J3–J4 tie at N = 20735: at a single hole both give up their peak beat at 16.

**Q-c (the comb pattern): holds.** In the lower range the disconnected multiples — (2, 4, 6, 8) and (3, 6, 9, 12) — alternate with ties, according to the residue-class pattern of II/14.

## 4. The full field — line imitation again, more sharply

In the full field of 503, **the main four win no filling strictly** (2346 fillings are ties): at every filling a tuned member of the line family is the cheapest or stands in a tie. The imitators winning the most fillings: (3, 5, 6, 10) — 2747; (3, 7, 8, 9) — 2042; (1, 3, 5, 7) — 2021. The field finding of II/14 therefore repeats and sharpens; the weight of the root signal grows: selection cannot be decided among free, hand-enumerated networks — it is decided where the contracts are born ([III/2, 7.](../../III-frontier/III-02-open-questions_en.md)).

## 5. Computational correction (H3)

The fixed identity tolerance of 10⁻⁸ is not applicable on the float64 route near the full end: the accumulation error there is 1.9·10⁻⁸. **The primary route is therefore extended-precision** (accumulation deviation at most 8.4·10⁻¹², four orders of magnitude below the tolerance); the winner row of the float64 cross-check differs at exactly 2 fillings (20735–20736), precisely where there is a genuine tie — the deviation is localized and understood.

## 6. Preparing the readout — an interpretation note and the fixed choice

The parenthetical enumeration of the phrase "highest standing rung" in [§8 of the rulebook](PKG-15-1-rulebook_en.md) did not foresee the measured case (the fourth rung stands, but not at the top). **Interpretation note, recorded:** "rung" means the rung of the staircase, that is, the extension number — the readout runs on the winner of the standing band of highest *extension*: **on J4, in the band 7965..15996.** The choice of a closed degree (a deterministic rule, fixed): among the widest gaps of the band (all of width 2 − √3 ≈ 0.267949, above these closed degrees: 8077, 9661, 11075, 12659, 13835, 14331, 15259), the one nearest half filling from above: **N = 11075.**

## 7. Outgoing claims (PKG-15-4 may build on these)

- **V1:** the winner table according to section 2; all three upper bands are patch-free.
- **V2:** the verdict: partial — "the fourth rung stands, the top belongs to three"; neither the complete yes nor the "stops at three" is the measured case.
- **V3:** the upper half is won exclusively by the pair carrying the mirror mark; within the pair the order is reversed at the top (Q-b).
- **V4:** in the full field the strict victories of the main four number zero — line imitation holds again (field finding).
- **V5:** the primary computation route is extended-precision (H3); the float64 deviation is localized to the full end.
- **V6:** the system of the readout: J4, 12×12×12×12, the band 7965..15996, closed degree **N = 11075**, the gap above it 2 − √3.
- **V7:** the ball reference sequences according to the table of §5 of the rulebook; r ≤ 3 for the verdict, r ≤ 5 for reporting (just valid on J4).
