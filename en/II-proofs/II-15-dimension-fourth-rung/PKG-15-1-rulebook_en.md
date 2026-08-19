---
id: PKG-15-1
type: package
part_of: II-15
lang: en
pair: PKG-15-1-rulebook_hu.md
pair_status: in-sync
doc_version: "1.3"
status: jovahagyva
builds_on: [II-14, II-13, II-12, II-11, I-06]
imports: zero
---

# PKG-15-1 — The rulebook of the fourth rung (derivation package)

**It contains no computation** — this package fixes the rules before anything is computed, so that no after-the-fact modification of the rules is possible.

---

## 1. Question (one sentence, fixed in advance)

Does the staircase continue: at an identical number of contracts per site (eight), is there an upper density band where the four-extension weave beats space, the plane and the line at the same time — and below it, in order, bands where space and then the plane do the same?

## 2. Inputs

- **[The race-rule convention of II/12](../II-12-network-race/proof_en.md):** a fixed contract budget must be placed; the equilibrium is the arrangement with the smallest total cost.
- **[III/1, 5. (equal rank of the sites)](../../III-frontier/III-01-candidate-laws_en.md):** realized by weave construction, as in II/13–II/14.
- **[I/6, the theorem of exclusion](../../I-language/I-06-identity_en.md):** the beat ladder is to be filled from below, one instance per beat.
- **The trace-tie theorem of II/12:** at full filling the price of every network is twice the budget.
- **[The rebuilder and ball growth of II/11](../II-11-locality-readout/proof_en.md):** for the readout of the winner.
- **The coincidence lesson of [II/13](../II-13-dimension-race/proof_en.md):** the distinctness of the candidates must be checked, not assumed — here we prove it from principle (point 5).
- **The legacies of [II/14](../II-14-dimension-staircase/proof_en.md):** the wrap-around bound **reformulated in graph steps** (because of the diagonal step of the space candidate the raw side length is not enough); the two protocol lessons — the signed jump and the band sentinel — in the form vetted in [PKG-14-5](../II-14-dimension-staircase/PKG-14-5-readout-repeat_en.md); the sufficiency of a wrap-around of 12 is a **theorem** at coordination six by PKG-14-5, but at coordination eight only a **support, not a guarantee** — which is why the sentinel remains obligatory.
- **[The corrected ball laws of III/2, 8.](../../III-frontier/III-02-open-questions_en.md):** the derived shell of the fourth reference sequence is cubic: (8/3)·r·(r² + 2).

## 3. The fixed system

- **20736 sites**; smoothness contracts, of unit strength.
- **Exactly 8 contracts per site** — the total budget is 82944 contracts, identically for every candidate.
- Every candidate is a **weave network** (the equal rank of the sites as a construction principle); the wrap-around of every wrapped direction is **even and at least 8 steps** — the even wrap-around protects the bipartite mark against the wrapping, and the wrap-around is **verified by machine traversal** on every entrant, not by hand derivation.
- Cost at N instances: filling the beat ladder of the network from below, scanned from N = 1 to 20736.
- The natural smaller size (4096, containing 8⁴) is explicitly excluded: it would put the native bipartite candidate exactly on the wrap-around floor of 8, where the readout of II/14 failed partially on a bipartite winner.

## 4. The field

| Candidate | Weave | Wiring | Wrap-around |
|---|---|---|---|
| **J1 — line** | a 20736-ring | ±1, ±2, ±3, ±4 steps | 5184 |
| **J2 — plane** | 144×144 king weave (square lattice + both diagonals) | ±(1,0), ±(0,1), ±(1,1), ±(1,−1) | 144 |
| **J3 — space** | 24×24×36 BCC weave, built in its own basis | ±(1,0,0), ±(0,1,0), ±(0,0,1), ±(1,−1,−1) | 24 |
| **J4 — four extensions** | 12×12×12×12 hypercube lattice | ±(1,0,0,0), ±(0,1,0,0), ±(0,0,1,0), ±(0,0,0,1) | 12 |

The shift of the native rung is stated: at coordination eight the bare unit-step wiring belongs to four extensions (8 = 2·4), as it belonged to space at six (6 = 2·3); the lower rungs spend the surplus in their own way (the line thickens, the plane goes diagonal, space switches to a body-diagonal step). J3 is a real measured structure (the body-centered lattice — iron among others); it may be entered into [Appendix C](../../appendix/C-benchmarks_en.md) as a reference.

**Fixed variant list (obligatory control):** K1 — space in another form, 16×36×36; K2 — space stretched, 12×36×48; K3 — four extensions stretched, 8×8×18×18; K4 — plane stretched, 48×432. The controls race and are to be reported in the full-field reading; they receive no readout, on principle. Two directions of K3 stand on the floor of 8 — valid data for the race.

**Honesty scan (obligatory, with a stated bound):** the quadruple wirings (a, b, c, d) of the line family in the range 1 ≤ a < b < c < d ≤ 12 must all be computed and enter — 495 members. Members with d > 12 are not scanned; this is a stated limit of this proof, deliberately identical to the ceiling of II/14, so that the family findings of the two proofs can be compared.

## 5. Derived preliminary facts

**Ball laws (the reference sequences of the readout).** At coordination eight every ball starts with 8; the distinguishing mark is the **order** of the increment (extension number minus one); the coefficients are properties of the concrete wiring:

| Candidate | Shell increment | Order | The sequence of the ball |
|---|---|---|---|
| line | 8 | constant | 1, 9, 17, 25, 33, 41 |
| plane | 8r | linear | 1, 9, 25, 49, 81, 121 |
| space | 6r² + 2 | quadratic | 1, 9, 35, 91, 189, 341 |
| four extensions | (8/3)·r·(r² + 2) | cubic | 1, 9, 41, 129, 321, 681 |

The sequences separate from r = 2 onwards (shells: 8 / 16 / 26 / 32); for the verdict r ≤ 3 is sufficient and is an obligatory bound, with reporting up to r ≤ 5 (point 8).

**Distinctness (the coincidence trap of II/13 closed from principle).** Three ladder marks — all three power sums of the ladder, hence properties of the ladder — confirmed by machine enumeration; since the shortest wrap-around is 12 steps, the wrapping does not interfere with closed walks of at most 4 steps, so the exact values of the infinite weave are valid:

| Candidate | Bipartite mark | 3-walks (per site) | 4-walks (per site) |
|---|---|---|---|
| J1 | none | 36 | 296 |
| J2 | none | 48 | 1188 |
| J3 | present | 0 | 216 |
| J4 | present | 0 | 168 |

Separating the six pairs: the cross pairs are decided by the bipartite mark, the J1–J2 pair by the 3-walks (36 ≠ 48), and the J3–J4 pair by the 4-walks (216 ≠ 168). Machine confirmation of the marks on the computed ladders is the obligatory self-check of PKG-15-2.

**Disconnection table (the correct claim in place of the rulebook error of II/14).** A family member is connected if its steps and the site count have no common divisor; because 20736 = 2⁸·3⁴ only 2 and 3 play a role: **479 members are intact; 15 all-even members fall into two copies; and (3, 6, 9, 12) into three copies** (three copies of (1, 2, 3, 4)). The number of zero modes is the number of copies. The derivation checked back on II/14 gives exactly the 20 disconnected members found there (19 with two copies and one with four).

## 6. Pre-registered facts following from theorems — and the registered questions

1. At N = 1 every intact entrant pays 0.
2. At N = 2 there is a 16-fold tie at zero (the disconnected members); at N = 3 the three-copy member stands alone at zero.
3. At N = 20736 a tie at **165888** is obligatory (the trace-tie theorem).

**A prediction for the intermediate range: deliberately none.** Three expectations are fixed, as questions: **(Q-a)** shell fit — do the victories cluster on the winner's degree boundaries ([III/1, 6.](../../III-frontier/III-01-candidate-laws_en.md)); **(Q-b)** the mirror question — at the J3–J4 boundary, where the mirror mark is present on both sides, is it the width or the shape of the ladder that decides — this is the first sharp test of [III/1, 7.](../../III-frontier/III-01-candidate-laws_en.md); **(Q-c)** the comb pattern — does the line/disconnected alternation of the lower range follow the residue-class pattern of II/14.

## 7. Verdict rule (fixed)

- For every N the entrant with the strictly smallest cost wins; the identity tolerance is a threshold derived from the ladder-agreement scale, to be fixed with a number in PKG-15-2; a tie must be reported as a tie.
- **The main question is decided on the quadruple J1–J4 — a three-rung staircase verdict:** the proof says a **complete yes** if there exist three connected, substantive bands with increasing density such that on the first J2, on the second J3, and on the third J4 beats the other three at the same time. **A highlighted partial case, named: "the staircase stops at three"** — there is a plane band and a space band, but no four-extension band; this is not a failure but the "three as a ceiling" reading, and is to be reported as such. Any other partial outcome with the existing bands named; **no**, if the band structure does not come together; a patchy outcome must be recorded together with the patches.
- The victories of the scan members and the controls are to be reported in the full-field reading (as in II/13–II/14).
- No new candidate, new filling filter or new cost definition may be introduced afterwards; extension only in a new package, without modifying this one.

## 8. The readout protocol (fixed for PKG-15-4)

- The readout runs on the winner of the **highest standing rung** (in the case of a complete yes, on the winner of the four-extension band; in the "stops at three" case, on the winner of the space band), at a **closed-degree** filling of the winning band; if every winning filling is degenerate, the even mixture of the zero-cost subspace must be computed, with an exact projector (the control method of II/11). Controls receive no readout.
- The rebuilder is given only the pairwise **signed** closeness from the finished state; not the neighbor count — the jump singles that out.
- **Signed jump rule (the form vetted in PKG-14-5):** the jump is to be sought on the signed list, in a fixed search window of 30; the antipodal class must be reported separately, together with its sign.
- **Band sentinel:** the ratio (by magnitude) of the weakest accepted and the strongest rejected closeness, reporting the worst local value; **below a factor of two the reading is partial**. For comparison: the clean case of PKG-14-5 gives 2.84, the failed case of II/14 gives 1.0.
- On a bipartite winner the correlation of the antipodal class is always a separate row, even if the sentinel does not signal.
- **Completeness ledger:** found / missing / phantom, all three with numbers, for the 82944 contracts.
- **Ball reading:** verdict up to r ≤ 3 against the four reference sequences of point 5; reporting up to r ≤ 5 where 2r < wrap-around — on J4, r = 5 is just valid.
- **Failure branch, in advance:** if the sentinel signals, the verdict is partial, naming the mechanism; repetition on a larger weave is not the business of this package but of a continuation named in advance (the name PKG-15-5 is reserved for this).

## 9. Import ledger

New import: **zero.** Inherited, declared conventions: the race rule, the equal rank of the sites, the weave construction (II/12–II/13), the sentinel threshold (a factor of two — PKG-14-5). Derived combinatorial facts: the ball laws, the walk counts, the disconnection table. Stated, fixed limits: the step ceiling of 12, the even ≥ 8 wrap-around, the size of 20736, the search window of 30, the r ≤ 3 / r ≤ 5 ball bounds, and the two-route sampling (A8).

## 10. Verdict on this package

**Stands.** The rulebook is closed; its substantive preliminary results are: the three-mark, principled proof of candidate distinctness (the coincidence trap does not depend on luck with the size); the statement of the native-rung shift; and the ball protocol built on the order of growth, completed with the fourth reference sequence.

## 11. Outgoing claims (PKG-15-2 may build only on these)

- **A1:** system = 20736 sites, 82944 units of smoothness contract, 8 per site, by weave construction; every wrap-around even and ≥ 8 steps, verified by machine traversal.
- **A2:** field = J1–J4 (the table of point 4), the controls K1–K4, and the scan of the line family up to d ≤ 12 (495 members, disconnected ones included).
- **A3:** cost = filling the beat ladder from below, N = 1..20736.
- **A4:** pre-registered facts: at N = 1 the intact entrants at 0; at N = 2 a 16-fold tie; at N = 3 the three-copy member alone; at N = 20736 a tie at 165888.
- **A5:** verdict rule according to point 7 — a three-rung staircase definition, with the named partial case "stops at three"; there is no prediction, but there are three registered questions (Q-a, Q-b, Q-c).
- **A6:** readout protocol according to point 8 — signed jump, band sentinel (threshold 2), ball verdict up to r ≤ 3, reporting up to r ≤ 5.
- **A7:** obligatory self-checks: (i) confirmation of the three distinctness marks on the ladders of the four main candidates; (ii) ladder classification over the full field with a fixed tolerance; (iii) machine wrap-around traversal on every entrant; (iv) trace sum 165888 everywhere; (v) component-count check against the disconnection table.
- **A8:** two-route rule with fixed sampling: the main candidates and the controls by both routes (closed Fourier form and machine eigenproblem) completely; machine cross-check of 24 drawn members from the family, with the fixed random seed: 20736.
