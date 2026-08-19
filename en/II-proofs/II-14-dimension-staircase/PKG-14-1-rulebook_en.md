---
id: PKG-14-1
type: package
part_of: II-14
lang: en
pair: PKG-14-1-rulebook_hu.md
pair_status: in-sync
doc_version: "1.4"
status: jovahagyva
builds_on: [II-13, II-12, II-11, I-06]
imports: zero
---

# PKG-14-1 — The rulebook of the extension staircase (derivation package)

**It contains no computation** — this package fixes the rules before anything is computed, so that no after-the-fact modification of the rules is possible.

---

## 1. Question (one sentence, fixed in advance)

Does extension step with the density: at an identical number of contracts per site (six), is there an upper density band where the space weave beats the plane and the line at the same time — and below it one where the plane beats the other two?

## 2. Inputs

- **[The race-rule convention of II/12](../II-12-network-race/proof_en.md):** a fixed contract budget must be placed; the equilibrium is the arrangement with the smallest total cost.
- **[III/1, 5. (equal rank of the sites)](../../III-frontier/III-01-candidate-laws_en.md):** realized by weave construction, as in II/13.
- **[I/6, the theorem of exclusion](../../I-language/I-06-identity_en.md):** the beat ladder is to be filled from below, one instance per beat.
- **The trace-tie theorem of II/12:** at full filling the price of every network is twice the budget.
- **[The rebuilder and ball growth of II/11](../II-11-locality-readout/proof_en.md):** for the readout of the winner.
- **Three legacies of [II/13](../II-13-dimension-race/proof_en.md):** the lesson of the coincidence lemma (the distinctness of the candidates must be checked, not assumed); the size diagnosis of the wrap-around resonance (a side length of 8 as a lower bound); the shell logic and the mirror effect as observations to be checked.
- **[The corrected ball laws of III/2, 8.](../../III-frontier/III-02-open-questions_en.md):** the shell of space is quadratic ($4r^2+2$), not linear.

## 3. The fixed system

- **512 sites**; smoothness contracts, of unit strength.
- **Exactly 6 contracts per site** — the total budget is thus 1536 contracts, identically for every candidate.
- Every candidate is a **weave network** (the equal rank of the sites as a construction principle, as in II/13), and the side length of every wrapped direction is **at least 8** — the legacy of the resonance diagnosis of II/13.
- Cost at $N$ instances: filling the beat ladder of the network from below, scanned from $N = 1$ to 512.

## 4. The candidates

| Candidate | Weave | Structure |
|---|---|---|
| **J1 — line** | a 512-ring, with 1-2-3 step wiring | thickened line |
| **J2 — plane** | a 16×32 lattice with periodic boundary, wiring: ±(1,0), ±(0,1), ±(1,1) | triangular weave (the planar weave of coordination six) |
| **J3 — space** | an 8×8×8 cubic lattice with periodic boundary, wiring: ±(1,0,0), ±(0,1,0), ±(0,0,1) | a genuine three-extension weave |

**Fixed variant list (obligatory control):** for the stretch sensitivity of the plane, the 8×64 triangular weave must also be computed and enters the field.

**Honesty scan (obligatory, with a stated bound):** the triple wirings $(a, b, c)$ of the line family in the range $a < b < c \le 12$ must all be computed and enter the field (cheap with the closed formula of the weaves). The bound is itself a fixed rule: the family members with $c > 12$ are not scanned — this is a stated limit of this proof, not an after-the-fact decision.

## 5. Derived preliminary facts — distinctness and ball laws

**Distinctness (the lesson of the coincidence lemma of II/13 — here a check, not an assumption).** A preliminary argument, to be confirmed by computation (PKG-14-2): J1 and J2 contain a three-cycle (in J1 the steps 1+2=3 close a triangle, in J2 the triple ±(1,0), ±(0,1), ±(1,1)), whereas J3 is a **bipartite network** — it has no three-cycle, and its ladder is therefore symmetric about the degree at 6. The three candidates are thus pairwise distinct; the symmetry mark is the obligatory self-check of PKG-14-2.

**Ball laws (derived, the reference sequences of the readout).** At coordination six the ball of every candidate starts with 6; the distinguishing mark is the **order** of the increment:

| Candidate | Increment | The sequence of the ball |
|---|---|---|
| line | constant ($+6$) | 1, 7, 13, 19, 25 |
| plane | linear ($6r$) | 1, 7, 19, 37, 61 |
| space | quadratic ($4r^2+2$) | 1, 7, 25, 63, 129 |

The sequences separate from $r = 2$ onwards (13 / 19 / 25); for the reading $r \le 3$ is sufficient and is also an obligatory bound (point 8).

## 6. Pre-registered facts following from theorems (not predictions)

1. At $N = 1$ every candidate pays 0 (every network has one common zero mode).
2. Every entrant is connected, with exactly 1 zero mode — the disconnected advantage at $N = 2$ (II/13) does not play here.
3. At $N = 512$ a tie at **3072** is obligatory (the trace-tie theorem: the sum of the whole ladder is twice the budget).

**A prediction for the substantive range $2 \le N \le 511$: deliberately none.** A single expectation is fixed, as a question: if the candidate shell-fit rule ([III/1, 6.](../../III-frontier/III-01-candidate-laws_en.md)) is general, the victories should cluster on the winner's own degree boundaries — this is to be checked, not predicted.

## 7. Verdict rule (fixed)

- For every $N$ the entrant with the strictly smallest cost wins; a tie must be reported as a tie.
- **Deciding the main question — the two rungs of the staircase:** the proof says **yes** to the staircase if there exist two connected, substantive bands such that on the lower-density one J2 beats J1 and J3 at the same time, and on the higher-density one J3 beats J1 and J2 at the same time. If only one of the bands exists: a **partial** result, naming the band that exists. If neither: **no.** A patchy outcome must be recorded together with the patches.
- The main question is decided on the declared J1–J2–J3 triple; the victories of the scan members and the variants are to be reported in the full-field reading (as in II/13).
- No new candidate, new filling filter or new cost definition may be introduced afterwards; extension only in a new package, without modifying this one.

## 8. The readout protocol (fixed for PKG-14-4)

- The readout runs on the winner of the main reading, at a **closed-degree** filling of the space band (an unambiguous state); if every winning filling is degenerate, the even mixture of the zero-cost subspace must be computed, with an exact projector (the control method of II/11).
- The rebuilder of II/11: pairwise closeness from the finished state; it is not given the neighbor count — this is singled out by the jump of the closeness list.
- **Extension reading from ball growth, against the three reference sequences of point 5, up to at most $r = 3$** — at a side length of 8 the ball reaches the halfway point of the wrap-around at $r = 4$, and from there the reading is invalid in principle.
- **Resonance sentinel (the lesson of II/13):** the correlation of the antipodal displacement classes must be reported separately; if any of them agrees exactly with the neighbor class, the reading must be qualified as partial, together with the location of the agreement.

## 9. Import ledger

New import: **zero.** The race rule, the equal rank of the sites and the weave construction are declared conventions inherited from II/12–II/13; the ball laws are derived combinatorial facts; the scan bound ($c \le 12$) and the side-length bound (≥ 8) are fixed, stated limits.

## 10. Verdict on this package

**Stands.** The rulebook is closed; its substantive preliminary results are the bipartite mark of candidate distinctness (the coincidence trap of II/13 provably does not apply here) and the corrected ball protocol built on the order of growth.

## 11. Outgoing claims (PKG-14-2 may build only on these)

- **A1:** system = 512 sites, 1536 units of smoothness contract, 6 per site, by weave construction, every side length ≥ 8.
- **A2:** field = J1 (line), J2 (triangular plane, 16×32), J3 (cubic space, 8×8×8), the 8×64 plane control, and the scan of the line family up to $c \le 12$.
- **A3:** cost = filling the beat ladder from below, $N = 1..512$.
- **A4:** pre-registered facts: at $N=1$ all pay 0; every entrant has 1 zero mode; at $N=512$ a tie at 3072.
- **A5:** verdict rule according to point 7 — a two-band staircase definition; there is no prediction.
- **A6:** readout protocol according to point 8 — ball reading up to $r \le 3$, with a resonance sentinel.
- **A7:** the obligatory self-check of PKG-14-2 is distinctness: the ladder of J3 is symmetric about 6 (a bipartite network), those of J1 and J2 are not.
