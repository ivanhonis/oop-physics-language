---
id: II-15
type: proof
lang: en
pair: proof_hu.md
pair_status: in-sync
doc_version: "1.3"
status: reszleges
builds_on: [II-14, II-13, II-12, II-11, I-06]
imports: zero
packages: [PKG-15-1, PKG-15-2, PKG-15-3, PKG-15-4, PKG-15-5, PKG-15-6, PKG-15-7]
---

# II/15. The fourth rung — the verdict: partial ("the fourth rung stands, the top belongs to three")

**In one sentence.** At coordination eight the extension staircase climbs to four — the four-extension weave wins the largest, central density band of the field, with half filling inside it, and its winner reads itself as four-extensional from the inside as well — but at the top the staircase turns back: the densest region belongs to space.

## The question and the system

After [II/14](../II-14-dimension-staircase/proof_en.md) the question is: does the staircase continue — at an identical number of contracts per site (eight), is there a band where the four-extension weave beats space, the plane and the line? The fixed system ([PKG-15-1](PKG-15-1-rulebook_en.md)): 20736 sites, 82944 units of smoothness contract, exactly eight per site; the field is the four natural candidates — line (a ring with 1-2-3-4 steps), plane (king weave), space (BCC weave, built in its own basis), four extensions (hypercube) — four controls, and all 495 quadruple wirings of the line family up to a step ceiling of 12. The shift of the native rung is stated: at coordination eight the bare unit-step wiring belongs to four extensions (8 = 2·4), as it belonged to space at six. The rulebook was fixed before every computation; three after-the-fact corrections stand in the packages (the J2 row of the walk table of §5; the scope of even wrap-around; making the primary computation route long-float — [PKG-15-2](PKG-15-2-ladders_en.md), [PKG-15-3](PKG-15-3-race_en.md)).

## The result — the race

The band structure is complete and patch-free ([PKG-15-3](PKG-15-3-race_en.md)): **line 2–4217, plane 4218–7964, four extensions 7965–15996, space 15997–20734**; at N = 20735 there is an exact space–four-extension tie, and at full filling the obligatory tie. The band of four extensions is the largest of all, and half filling sits inside it — the fourth rung therefore stands. But the order is not monotone: the top belongs to three. The mechanism can be read from the mirror logic: the full end is the mirror image of the sparse end — there the unfilled beats (the holes) race on the mirrored ladder, and when sparse the lower extension is the cheaper one; the exact tie at N = 20735 (at a single hole both bipartite candidates give up their peak beat at 16) is the seal of this. The answers to the three registered questions: shell fit does not hold sharply (the band boundaries fall 2, 3 and 112 fillings from the nearest closed degree — the band boundary is the intersection point of the cost curves, not a shelf boundary); the mirror rule is confirmed in its sharpest form so far — **the upper half is won exclusively by the pair carrying the mirror mark**, every single upper filling is theirs — but within the pair it is not the width that decides (that is identical: 16 = 16) but the shape of the ladder, and at the top the order reverses; the lower comb pattern follows the residue-class order of II/14.

## The result — the readout

The loop closes on the winner of the fourth rung ([PKG-15-4](PKG-15-4-readout_en.md)): at the closed degree N = 11075 (the gap above it is exactly 2 − √3) the jump of the blind rebuilder singles out exactly the eight unit steps (5.7-fold), the sentinel is 5.37, above the threshold of two, the completeness ledger is **82944/82944, zero phantom, zero missing**, and the ball is **exactly cubic to the end of the validity range: 1, 9, 41, 129, 321, 681**. The extension number is thus the same from outside (the race) and from inside (the ball): four. The antipodal echo is present (+17.4%, this time with a positive sign), but outside the critical zone — the size decision, which was built on the 12-step support of [PKG-14-5](../II-14-dimension-staircase/PKG-14-5-readout-repeat_en.md), was vindicated. The two-route seal: the closed and the machine route of the projector agree to within 1.7·10⁻¹⁵.

## The field finding

In the full field of 503, the main four **win no filling strictly**: at every filling a tuned member of the line family is the cheapest or stands in a tie (the imitators winning most often: (3, 5, 6, 10), (3, 7, 8, 9), (1, 3, 5, 7)). The field finding of II/14 therefore repeats and sharpens: selection cannot be decided among free, hand-enumerated networks — the weight of the root signal ([III/2, 7.](../../III-frontier/III-02-open-questions_en.md)) grows.

## What it confirmed, and what it did not

It confirmed: the fourth rung **exists** — the staircase does not stop at three, and the winner of the fourth rung reads itself as such from the inside; the sharpened form of the mirror rule ([III/1, 7.](../../III-frontier/III-01-candidate-laws_en.md)); and it gave birth to a new law: the mirror half of the top turn was raised to a theorem after the proof was closed ([PKG-15-5](PKG-15-5-hole-mirror_en.md); [III/1, 8.](../../III-frontier/III-01-candidate-laws_en.md)) — the measured tie at 20735 and the peak beat at 16 became derived facts; and the direction theorem ([PKG-15-6](PKG-15-6-direction_en.md)) together with the top theorem assembled from it ([PKG-15-7](PKG-15-7-top_en.md)) put the turn on a theorem footing on the uppermost stretch of the top as well (from 18649 onwards). What it did not confirm, honestly: "why three" is still not derived — the 1/r attraction import is untouched; the finding holds for the fixed four and at this size, and the coordination dependence is open; and the density question was reformulated, not solved: if the staircase turns back at the top, then "three" is the reading of the top — this is a registered question, not a claim.

## Direction of extension

Three paths open: both halves of the top turn on a theorem footing (PKG-15-5, PKG-15-6, PKG-15-7) — with the question of the dominance gap (the intermediate part of the measured band) left open; the coordination scan (at coordination 10 the native rung is five — does the top turn there too, and where); and the root of selection — the race is decided where the contracts are born ([III/2, 7.](../../III-frontier/III-02-open-questions_en.md)).
