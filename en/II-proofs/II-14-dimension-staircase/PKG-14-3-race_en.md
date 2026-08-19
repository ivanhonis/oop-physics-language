---
id: PKG-14-3
type: package
part_of: II-14
lang: en
pair: PKG-14-3-race_hu.md
pair_status: in-sync
doc_version: "1.4"
status: jovahagyva
builds_on: [PKG-14-1, PKG-14-2]
imports: zero
---

# PKG-14-3 — The filling race (derivation package)

**Builds on:** [PKG-14-1](PKG-14-1-rulebook_en.md) (A4, A5), [PKG-14-2](PKG-14-2-ladders_en.md) (B1–B5) · **Computation code:** `PKG-14-3-race.py`

---

## 1. Question

Which weave wins the filling race at which instance count, according to the fixed two-band staircase rule?

## 2. The obligatory precondition (B3): independent recomputation

The ladders recomputed by a new code path (from the incidence matrix: one row per edge, $L = B^{\mathsf T} B$): on all 223 networks the trace sum is exactly 3072; the zero modes are as in PKG-14-2 (1 each for the four declared networks, and the 20 disconnected ones among the scan members); the spot-check values (0.0021; 0.0769; $2-\sqrt2$; the top of space at 12) agree with the reference values. The race could begin.

## 3. The result — the main reading: the declared triple (J1–J2–J3)

| N instances | 1 | 2–129 | 130–255 | 256–511 | 512 |
|---|---|---|---|---|---|
| winner | all (0) | **J1 line** | **J2 plane** | **J3 space** | all (3072) |

Both prescribed bands exist and are connected: the plane band is **130–255**, the space band is **256–511**. The boundaries are sharp and tight: at the line–plane switch (N = 129 → 130) the difference is below 0.2 per mil (303.512 / 303.691, then 309.400 / 308.234); the plane–space switch (N = 255 → 256) is tighter still (1022.788 / 1023.442, then 1029.616 / 1029.442). Characteristic depths: at N = 64 the line is 43.7 against 80.8 for the plane and 127.9 for space; at N = 384 space is 1903.5 against 1994.7 for the plane and 2015.7 for the line.

**Verdict according to the fixed rule 7: YES — both rungs of the staircase hold.** Sparsely the line, at medium density the plane, at high density space is the cheapest: extension steps with the density.

**Pre-registered facts:** all three hold (at N = 1 everyone pays 0; at N = 512 a tie at 3072; the zero modes according to the correction of PKG-14-2).

## 4. The structure of the band boundaries — checking the shell expectation

- **Space takes over the race exactly at half filling** (N = 256) — and this is **not a degree boundary**: the central shelf of space, of cost 6 and 68 beats wide, covers the range 223–290, and half filling is the **middle** of it (256.5). The mechanism is the **bipartite mark**: the ladder of space is exactly symmetric about 6 and is the widest (from 0 to 12) — in the upper hemisphere the winner is the one whose mirror pushes the high beats furthest away. The shell expectation of point 6 of the rulebook was therefore **not met** here: the plane–space boundary is decided not by degree filling but by mirror symmetry.
- The line–plane boundary (130) falls next to the degree boundary of the plane at 129, but the degree boundaries of the plane are dense there (…125, 129, 131…), so this is at best a weak signal — the candidate shell-fit rule ([III/1, 6.](../../III-frontier/III-01-candidate-laws_en.md)) needs refinement: on a small system (II/13) degree filling decided, here the mirror does.

## 5. The full field — the strict winners

**Nowhere in the full field are the declared weaves strict winners.** At every filling a tuned member of the line family is the cheapest; the regimes of the field:

- **Lower band (2–124): the comb.** The line class alternates with its own disconnected multiples — (2,4,6) is two and (4,8,12) is four copies of the same thickened line on a smaller ring; (4,8,12) takes the fillings N ≡ 4 (mod 8), (2,4,6) takes N ≡ 2 (mod 4), and the connected line takes the odd ones. Degree resonance in its purest form: the multiplied shelves fill exactly at the even fillings.
- **Middle band (125–236): cross-lines** — the mass version of the phenomenon of II/13: (1,5,6), (1,4,5), (2,3,5) and their companions overtake the plane everywhere.
- **Upper band (237–511): the rule of the bipartite mark.** The winners are all-odd-step lines — these are themselves bipartite networks, with a top at 12 — and their disconnected pairs; of the 22 members of the tie at N = 511, 20 are all-odd lines, plus space and (2,6,10). **The disadvantage of space against the field winner is small throughout: 0.3–2.2%** (1.7% at N = 300, 0.3% at N = 500).

The finding, stated: the staircase stands on the race of the **representatives of geometry**; in the full family the one-extension weave, given enough tuning freedom, catches up at every filling and beats the higher extension on a percentage scale — and the bipartite mark that decides the upper hemisphere can be produced on a line as well (with all-odd steps). The advantage of extension is therefore real, but thin, and its carrier is mirror symmetry.

## 6. Import ledger and verdict

New import: **zero.** No after-the-fact modification of the rules took place; the victories of the scan members are part of the fixed field; the failure of the shell expectation had been registered as a question, not as a prediction. **Verdict: stands.**

## 7. Outgoing claims (PKG-14-4 and the synthesis may build only on these)

- **C1:** the winner table of the triple according to point 3; band boundaries: 129/130 and 255/256.
- **C2:** main reading: **yes** — a complete staircase: line 2–129, plane 130–255, space 256–511, both prescribed bands connected.
- **C3:** the space band begins exactly at half filling, in the middle of the central mirror shelf — the mechanism is the bipartite mark, not degree filling; the candidate shell-fit rule is to be refined in this light.
- **C4:** PKG-14-4 (readout) runs on J3, at **N = 290**: the first closed degree of the space band (the filling of the central shelf; above it a gap of 0.586) — the state is unambiguous, no projector is needed.
- **C5:** full-field finding: nowhere are the declared weaves strict field winners; the disadvantage of space is 0.3–2.2%; the lower comb, the cross-lines and the upper rule of the bipartite mark are recorded.
