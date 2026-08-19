---
id: PKG-16-1
type: package
part_of: II-16
lang: en
pair: PKG-16-1-rulebook_hu.md
pair_status: in-sync
doc_version: "1.3"
status: jovahagyva
builds_on: [II-15, II-14, II-12, II-11, I-06]
imports: "the selection rule (a stated convention, section 9)"
---

# PKG-16-1 — The rulebook of coordination ten (derivation package)

**It contains no computation** — it fixes the rules before every computation; it cannot be modified afterwards.

## 1. Question (one sentence, fixed in advance)

At coordination ten — where the native rung is five — does the staircase climb up to the native, and **where does it turn back at its top**: to three again, to the single carrier of the mirror mark (here precisely the native five), or somewhere else?

## 2. Inputs

The complete legacy of II/12–II/15, in particular: the theorem of exclusion (I/6); the trace tie (II/12); the **hole-mirror theorem** ([PKG-15-5](../II-15-dimension-fourth-rung/PKG-15-5-hole-mirror_en.md)); the machinery of the **direction theorem** with the ordering, inversion and sandwich lemmas ([PKG-15-6](../II-15-dimension-fourth-rung/PKG-15-6-direction_en.md)); the pattern of the top theorem ([PKG-15-7](../II-15-dimension-fourth-rung/PKG-15-7-top_en.md)); the echo series (a wrap-around of 12 is sufficient — [PKG-14-5](../II-14-dimension-staircase/PKG-14-5-readout-repeat_en.md), [PKG-15-4](../II-15-dimension-fourth-rung/PKG-15-4-readout_en.md)); and the three correction lessons of II/15 **raised to rules**: duplication-safe wiring construction with a machine element-uniqueness assertion (H1), the even-wrap-around requirement only on the bipartite entrants (H2), and an extended-precision primary computation route (H3).

## 3. The fixed system

- **248,832 sites** (= 12⁵); **1,244,160 units of smoothness contract, exactly ten per site.**
- Every entrant is a weave network; the wrap-around of every wrapped direction is **at least 8 graph steps, verified by machine traversal**; on the **bipartite** entrants the wrap-around is also even.
- Cost: filling the ladder from below, N = 1 to 248,832; **the primary route is extended-precision**, and the identity tolerance is 10⁻⁸.

## 4. The field

| Candidate | Weave | Wiring (half-steps) | Shortest side |
|---|---|---|---|
| **J1 — line** | a 248,832-ring | 1, 2, 3, 4, 5 | — |
| **J2 — plane** | 432×576 | (1,0), (0,1), (1,1), (1,−1), (0,2) | 432 |
| **J3 — space** | 54×64×72 | axes + (0,1,−1), (0,1,1) | 54 |
| **J4 — four extensions** | 18×24×24×24 | axes + (0,0,1,−1) | 18 |
| **J5 — five extensions (native)** | 12⁵ | unit steps | 12 |

**Controls (they race, they receive no readout):** K1 space form 48×72×72; K2 four extensions stretched 12×24×24×36; K3 plane stretched 288×864; KA2/KA3/KA4 — controls for the arbitrariness of the tie-breaker (the extra step laid on the other side pair); **KP3 bipartite space** (axes + two body-diagonal pairs); **KP4 bipartite four extensions** (axes + the (0,1,1,1) pair).

**Honesty scan:** all 792 quintuple wirings of the line family (1 ≤ a < b < c < d < e ≤ 12); the ceiling is a stated limit, identical to that of II/14–II/15.

## 5. Derived preliminary facts

**Ball laws (reference sequences; the shells separate from r = 2 onwards: 10 / 22 / 34 / 44 / 50):**

| Candidate | Shell increment | The sequence of the ball (r = 0..5) |
|---|---|---|
| line | 10 | 1, 11, 21, 31, 41, 51 |
| plane | 12r − 2 | 1, 11, 33, 67, 113, 171 |
| space | 8r² + 2 | 1, 11, 45, 119, 249, 451 |
| four extensions | 2r(2r² + 3) | 1, 11, 55, 181, 461, 991 |
| five extensions | combinatorial closed form (fourth order) | 1, 11, 61, 231, 681, 1683 |

**Mark table (verified by two routes, with a duplication-safe enumerator):** 3-walks 60 / 42 / 24 / 12 / 0 — **this single mark separates all ten main pairs**; 4-walks 590 / 414 / 318 / 270 / 270 (the J4–J5 agreement is harmless). **The parity finding:** at coordination ten only the native rung has a weave that is both fully direction-symmetric and carrying the mirror mark — the asymmetry and triangularity of J2–J4 is a constraint of the coordination; the mirror question is carried by the controls KP3, KP4 and the six all-odd-step family members.

**Disconnection table:** 786 intact + 6 with two copies (the all-even members); zero modes = number of copies; there is no three-copy member.

## 6. Pre-registered facts and questions

From theorems: at N = 1 all 805 entrants at zero; at N = 2 a sixfold tie at zero; **at N = 3 — a difference from II/15 — there is no longer any zero-cost entrant**; at N = 248,832 a tie at **2,488,320** is obligatory.

**A prediction: deliberately none.** Registered questions: **(Q-a, the main question of the proof)** where the top belongs — the two readings of II/14–II/15 diverge here: if "the mirror rules the top", the top belongs to the only main candidate carrying the mirror mark, the five-extension native; if "the top belongs to the low extension", a non-bipartite rung takes it, and the scope of the mirror rule (III/1, 7.) narrows; **(Q-b)** the comb pattern in the lower range (with the sixfold disconnected set); **(Q-c)** does the ~half ratio of the dominance gap repeat; **(Q-d)** shell fit at the band boundaries.

## 7. Verdict rule (fixed)

For every N the strictly smallest cost wins (tolerance 10⁻⁸, on the extended-precision route); a tie as a tie. **The main question is decided on the quintuple J1–J5 — a four-rung staircase verdict:** a complete yes if four connected, substantive bands stand with increasing density, with J2, J3, J4, J5 winning in turn over the other four. Named partial cases: **"stops at four"**, **"stops at three"**, and — foreseen in advance following the precedent of II/15 — **"the staircase turns back at its top"**, in which case the measured order is itself the text of the verdict, naming the target rung of the turn. Any other partial case with the existing bands; no, if no band structure comes together; a patchy outcome with the patches. The scan members and the controls in the full-field reading. After-the-fact modification excluded.

## 8. The readout protocol

The order of §8 of II/15 unchanged — signed jump (window of 30), band sentinel (threshold 2), an obligatory antipodal row on a bipartite winner, completeness ledger for the 1,244,160 contracts, ball verdict up to r ≤ 3, reporting up to r ≤ 5 (on J5, just valid at a wrap-around of 12) — **with one substitution: the projector seal takes a new, sampling sparse form** (section 9), because a dense eigenproblem is excluded on principle at this size. Choice of a closed degree: among the widest gaps of the winning band, the one nearest half filling from above. Failure branch: a partial verdict naming the mechanism; the name of the continuation is reserved as PKG-16-6.

## 9. Import ledger and the new form of the two-route rule

**A new, stated convention — the selection rule:** (i) the native rung belongs to the bare unit steps; (ii) at every other rung the five ± pairs with the smallest total step-square enter, with a lexicographic tie-breaker. An honest note: projected back to coordination eight the rule gives back the line, the king plane and the hypercube, but for the space candidate of II/15 it would give axes+face-diagonal instead of the crystallographic BCC — the difference is stated; here there is no conflict, because a single-orbit alternative exists only at the native rung.

**The four-element sparse form of the two-route rule** (the dense route would be 495 GB and months): (i) **sparse residual check** — the constructed network against the closed formula, with 64 drawn modes per network on the main/control entrants and 16 modes on 24 drawn family members; (ii) **moment covers** of order ≤ 4 on every entrant (the power sums of the ladder against the combinatorial walk counts — at the same time a self-check of the mark table); (iii) **dense certification on small instances** — the 12-sided small variant of every wiring pattern by the full dense route; (iv) **sampling projector seal** at the readout (the residual of the filled and empty modes, 64 + 64 drawn modes). The random seed everywhere: **248,832**. Stated: this is weaker than the full dense seal of II/15; the coverage must be reported with a number.

## 10. Verdict on this package

**Stands.** Its substantive preliminary results: the parity finding (sharpening the mirror question into a decisive experiment), the single-mark distinctness proof, and the five ball laws.

## 11. Outgoing claims

- **A1:** system = section 3; **A2:** field = section 4 (5 + 8 + 792 entrants); **A3:** cost on the extended-precision route, tolerance 10⁻⁸; **A4:** registered facts according to section 6; **A5:** verdict rule according to section 7, with the named turn-back case; **A6:** readout protocol according to section 8; **A7:** obligatory self-checks — the mark table by two routes, ladder classification over the full field (tolerance 10⁻⁸), machine wrap-around traversal on every entrant, trace sum 2,488,320 everywhere, component count against the disconnection table, machine assertion of wiring uniqueness on every network; **A8:** the two-route rule in the four-element form of section 9, with fixed sample sizes and seed.
