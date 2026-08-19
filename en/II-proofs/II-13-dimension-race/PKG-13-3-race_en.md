---
id: PKG-13-3
type: package
part_of: II-13
lang: en
pair: PKG-13-3-race_hu.md
pair_status: in-sync
doc_version: "1.3"
status: jovahagyva
builds_on: [PKG-13-1, PKG-13-2]
imports: zero
---

# PKG-13-3 — The filling race (derivation package)

**Builds on:** [PKG-13-1](PKG-13-1-rulebook_en.md) (A4, A5), [PKG-13-2](PKG-13-2-ladders_en.md) (B1–B4) · **Computation code:** `PKG-13-3-race.py`

---

## 1. Question

Which weave wins the filling race at which instance count, according to the fixed verdict rule?

## 2. The obligatory precondition (B3): independent recomputation

The ladders recomputed by a new code path (with an adjacency-list construction): on all eight networks the trace sum is exactly 64; the zero modes are as in PKG-13-2 (J1: 1, J2: 1, J3: 2, second segmented: 2); the spot-check values (0.738; 2.5858; the torus ladder; the level at 4 of the segmented one) agree with the published reference values. The race could begin.

## 3. The result — winner table (strict winner; ties marked)

| N instances | Winner | Cost | J1 line | J2 plane | J3 segmented |
|---|---|---|---|---|---|
| 1 | all (tie) | 0 | 0 | 0 | 0 |
| 2 | J3 and the second segmented | 0 | 0.738 | 2 | **0** |
| 3 | **J1** | 1.476 | **1.476** | 4 | 2.586 |
| 4 | **J1** | 4.062 | **4.062** | 6 | 5.172 |
| 5 | **J1** | 6.648 | **6.648** | 8 | 7.757 |
| 6 | **J3** | 10.343 | 10.648 | 12 | **10.343** |
| 7 | **J3** | 14.343 | 15.081 | 16 | **14.343** |
| 8 | **J3** | 18.343 | 19.515 | 20 | **18.343** |
| 9 | scan member (1,6) | 22.648 | 24.164 | 24 | 23.757 |
| 10 | scan member (1,6) | 26.648 | 28.812 | 28 | 29.172 |
| 11 | **J2 — its only strict victory** | 32 | 34.227 | **32** | 34.586 |
| 12 | scan members (1,6) and (1,4) | 37.476 | 39.641 | 38 | 40 |
| 13 | scan member (1,7) | 42.343 | 45.641 | 44 | 46 |
| 14 | second segmented (2,6) | 48 | 51.641 | 50 | 52 |
| 15 | fourfold tie at 56 | 56 | 57.820 | **56** | 58 |
| 16 | all (trace tie) | 64 | 64 | 64 | 64 |

**Pre-registered facts:** all three hold — the one at $N = 2$ with the transparent addition that the strict victory is shared with the second segmented weave discovered in the meantime (the content of the fact — the segmented one zeroes out, the connected one pays — is unchanged).

## 4. Verdict according to the fixed rule 7 — two readings, both exactly

**Main reading (the letter of the rule: does J2 beat J1 and J3 at the same time?):** yes, over the connected range **10–15** — the upper half of the substantive band 3–15. **The proof says a partial yes to extension: at high density the plane beats the line and the segmented line.**

**Full field (strict winner against every entrant):** the race falls into regimes — sparsely the line (3–5), below-and-middle the segmented one (6–8), above it the cross-lines (9–10, 12–13), and the mirror effects of the full end (14–15) — and the only strict victory of the plane is **N = 11**.

## 5. Observations

- **The shell logic returns — at the level of the networks.** The degree boundaries (closed degrees) of the plane are 1, 5, 11, 15 — and it wins exactly at 11, and stands in a tie at 15. The degree boundaries of the segmented one are 2, 6, 8 — its winning band is 6–8. The winner wins where one degree of its own ladder is just filling up: the magic-number logic of [II/7](../II-07-bowl-magic-numbers/proof_en.md) repeats at the level of space selection.
- **Mirror effect at the full end** (a corollary of the trace tie): at nearly full filling the cost = 64 minus the sum of the unfilled upper beats — there the winner is the one who compresses its cost into few, high beats; this is why 14 is taken by the second segmented weave (with the peak beats of its two 8-rings).
- **Extension is a density-dependent equilibrium property:** the same budget would weave a line when sparse, pieces in the middle, and a plane at high density — extension belongs not to the network but to the network+filling pair.

## 6. Import ledger and verdict

New import: **zero.** No after-the-fact modification of the rules took place; the victories of the scan members are part of the fixed field. **Verdict: stands** — the result is partial, and is recorded exactly that way, patches included, as the rulebook prescribed.

## 7. Outgoing claims (PKG-13-4 and the synthesis may build only on these)

- **C1:** the winner table according to point 3.
- **C2:** main reading: a partial yes — the plane beats J1 and J3 over the connected range 10–15.
- **C3:** the only strict victory of the plane is $N = 11$ — its own closed degree.
- **C4:** PKG-13-4 (readout) runs on J2, at $N = 11$: a strict winner and a closed degree — the state is unambiguous, no projector is needed.
- **C5:** the shell logic and the mirror effect are recorded as observations; raising them to theorems is not the business of this package.
