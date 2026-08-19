---
id: PKG-15-6
type: package
part_of: II-15
lang: en
pair: PKG-15-6-direction_hu.md
pair_status: in-sync
doc_version: "1.4"
status: jovahagyva
builds_on: [PKG-15-5, PKG-15-2, II-12, I-06]
imports: zero
---

# PKG-15-6 — The direction theorem (derivation and computation package)

**The business of the package.** Proving that on a sufficiently sparse stretch the weave of lower extension is the cheaper one — with an explicit threshold, on all six ordered candidate pairs. The script: `shared/II-15-dimension-fourth-rung/PKG-15-6-direction.py`.

## 1. Scope (fixed before the derivation)

**S1:** the theorem speaks about the stretch 2 ≤ N ≤ N*; about nothing outside it. **S2:** there are two thresholds, both of theorem strength — N*-analytic (the formulaic certificate of the lemma chain) and N*-machine (the maximum exactly certified on the fixed, finite system); by construction the first is at most as large as the second, and their distance must be reported. **S3:** the theorem does not, on principle, yield the boundary positions — the tippings sit in the nonlinear range of the ladders; the theorem proves the direction. **S4:** beat-by-beat dominance is stricter than the price order, so N*-machine too lies below the measured price tipping; the dominance gap is a number to be reported. **S5:** the theorem speaks about all six ordered pairs; the top theorem (PKG-15-7) mirrors the bipartite pair across from this. **S6:** it does not touch the full field, the bipartite versus non-bipartite upper rule, or the attraction import.

## 2. The three lemmas

**L5 — ordering lemma.** If every i-th beat of the ladder X is at most as large as the i-th beat of the ladder Y over the stretch 1..N, then the price of X is at most the price of Y at every filling 1..N; and if it is strictly smaller at some beat, the price is strictly smaller from that filling onwards. *Proof:* the price is a partial sum of the beats; a sum of term-by-term inequalities. ∎

**L6 — inversion lemma.** The beat order and the degree-counter order are the same statement: the i-th beat is the smallest price level below which there are already i degrees — the ordered sequence and the counting function are inverses of each other. The sparse race is thus a counter race. ∎

**L7 — sandwich lemma.** On every weave and at every wave number (4/π²)·Q(k) ≤ λ(k) ≤ Q(k), where Q is the stiffness form with folded-back phases (the phases folded onto the interval [−π, π), summed quadratically). *Proof:* term by term from the elementary inequalities 2(1 − cos θ) ≤ θ² (for every θ) and 2(1 − cos θ) ≥ (4/π²)·θ² (for |θ| ≤ π, with equality at the edge); summation preserves both sides. *Machine certification:* on the full lattice of the four candidates the violation is zero. ∎

## 3. The two layers

**Analytic certificate (L8):** from the lemma chain, if for the ordered Q sequences Q_X(i) ≤ (4/π²)·Q_Y(i), then λ_X(i) ≤ λ_Y(i) — N*-analytic is the index before the first violation. **Machine layer:** N*-machine is the longest stretch on which λ_X(i) ≤ λ_Y(i) holds exactly; from there L5 closes the price dominance. Both layers are of theorem strength on the fixed system; the machine one is the sharp one.

## 4. The direction theorem — the result

**Direction theorem.** On all six ordered pairs: the price of the candidate of lower extension is strictly smaller over the whole stretch 2..N*-machine.

| Pair | N*-analytic | **N*-machine** | Price tipping | Coverage | Strict |
|---|---|---|---|---|---|
| line–plane | 1065 | **2599** | 4218 | 61.6% | holds |
| line–space | 1609 | **3057** | 7127 | 42.9% | holds |
| line–four ext. | 1705 | **2981** | 6184 | 48.2% | holds |
| plane–space | 349 | **4645** | 10285 | 45.2% | holds |
| plane–four ext. | 741 | **3677** | 7965 | 46.2% | holds |
| **space–four ext.** | 7 | **2087** | 4740 | 44.0% | holds |

Counter-check: on the certified stretches the price dominance also holds by direct comparison, on all six pairs.

## 5. Findings

- **The pairwise tipping table is complete.** Three numbers are new (line–space 7127, line–four extensions 6184, plane–space 10285); three agree with the earlier measurements (4218 and 7965 with the band boundaries, 4740 with the mirror pair of PKG-15-5) — a consistency seal.
- **The dominance gap is systematic:** the beat-by-beat condition holds up to 43–62% of the price tipping, regardless of the pair. A registered question: why this ratio is so stable.
- **On the upper pair the continuous picture is almost empty** (N*-analytic = 7 on the space–four-extension pair): there — as the preparation had signalled in advance — the discrete first-degree structure carries it (at a fixed site count the side length shrinks with the extension, so even the first degrees already sit in extension order: 2.75·10⁻⁶ / 5.71·10⁻³ / 6.08·10⁻² / 2−√3). The two mechanisms — the exponent of the counter and the side shrinkage — point in the same direction.

## 6. Verdict

**Stands.** The direction theorem is proved on all six pairs, strictly, with a machine certificate of theorem strength; the sandwich lemma is stated and certified as a general tool.

## 7. Outgoing claims

- **I1:** the direction theorem with the six N*-machine values (the table of section 4).
- **I2:** on the space–four-extension pair **N* = 2087** — the input of the top theorem (PKG-15-7).
- **I3:** the sandwich lemma (L7) is a general tool, valid for every weave.
- **I4:** the complete pairwise tipping table, with three new numbers.
