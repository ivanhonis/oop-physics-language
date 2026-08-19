---
id: PKG-15-7
type: package
part_of: II-15
lang: en
pair: PKG-15-7-top_hu.md
pair_status: in-sync
doc_version: "1.3"
status: jovahagyva
builds_on: [PKG-15-6, PKG-15-5]
imports: zero
---

# PKG-15-7 — The top theorem (assembly package)

**The business of the package.** Threading together the direction theorem ([PKG-15-6](PKG-15-6-direction_en.md)) and the hole-mirror theorem ([PKG-15-5](PKG-15-5-hole-mirror_en.md)) — with no new proof — into the theorem form of the main finding of II/15. The script: `shared/II-15-dimension-fourth-rung/PKG-15-7-top.py`.

## 1. The theorem

**Top theorem.** On the fixed system, over the stretch 18649 ≤ N ≤ 20734 the price of space is strictly smaller than that of four extensions; at the filling N = 20735 there is an exact tie.

*Proof.* On the space–four-extension pair the direction theorem gives the strict cheapness of space over the stretch 2 ≤ N ≤ 2087 (PKG-15-6, I2). According to the hole-mirror theorem the cost difference of two networks carrying the bipartite mark at any filling N equals the difference at the mirror filling (20736 − N) (PKG-15-5). The mirror of the stretch 18649..20734 is exactly the stretch 2..2087, so the sign — together with the strictness — mirrors across one to one; the mirror of N = 20735 is N = 1, where both networks pay zero. ∎

## 2. Machine check

| Check | Result |
|---|---|
| E1 — strict dominance on the theorem stretch | the smallest advantage of space over the stretch 18649..20734 is **0.2072** — holds |
| E2 — single-hole tie | deviation 1.7·10⁻¹³ — holds |
| E3 — exactness of the mirror transfer over the stretch | largest deviation 2.2·10⁻¹² — holds |
| E4 — coverage | the certified 2086 fillings are **44.0%** of the measured pairwise upper range (15997..20734) |
| consistency | the certified stretch sits entirely within the measured space band — holds |

## 3. An honest comparison with the measurement

The theorem states, over the **uppermost ~2100 fillings** of the top, what II/15 measured: there space beats four extensions — this is now a consequence, not a measurement. The remainder of the measured range (15997..18648) remains a measured fact: there the price order holds, but the beat-by-beat dominance no longer does (this is the dominance gap registered in PKG-15-6). And the theorem is within-pair: that at the top the bipartite pair also beats **everyone else** (the line and the plane) is still said by the measurement ([III/1, 7.](../../III-frontier/III-01-candidate-laws_en.md)).

## 4. Verdict

**Stands.** Both halves of the top turn stand on a theorem footing: the mirror half in its entirety (PKG-15-5), the direction half on the uppermost stretch (this package) — "at the top three beats four" is a derived fact over the stretch 18649..20734.

## 5. Outgoing claims

- **F1:** the top theorem according to section 1, with the strictness margin of 0.2072.
- **F2:** the two-layer reading of the measured space band: from 18649 a theorem, below it (from 15997) a measurement — the boundary is itself the mirror image of the dominance gap.
- **F3:** the proof pattern is reusable: direction theorem + hole-mirror = top claim, on any future bipartite pair (ready for the coordination scan).
