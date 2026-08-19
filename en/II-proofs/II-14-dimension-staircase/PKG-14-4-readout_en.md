---
id: PKG-14-4
type: package
part_of: II-14
lang: en
pair: PKG-14-4-readout_hu.md
pair_status: in-sync
doc_version: "1.4"
status: jovahagyva
builds_on: [PKG-14-1, PKG-14-3, II-11]
imports: zero
---

# PKG-14-4 — Closing the loop: readout on the winner (derivation package)

> **Restoration note — read this before citing it.** The original, approved text of this file was lost: in its place stood a copy of the [PKG-14-1](PKG-14-1-rulebook_en.md) rulebook (in all four snapshots of `!archive` as well), and it was not preserved in the git history either. The present text is a **restoration**, from three sources: the surviving computation code (`shared/II-14-dimension-staircase/PKG-14-4-readout.py`), the fixed protocol ([PKG-14-1](PKG-14-1-rulebook_en.md), point 8) and the C4 input of [PKG-14-3](PKG-14-3-race_en.md). **Every number reported below was re-measured** — not copied from the proof file — and agrees with the values cited by [II/14](proof_en.md) and [PKG-14-5](PKG-14-5-readout-repeat_en.md). What the restoration cannot replace: the original wording. If the original turns up, this file is to be replaced.

**Builds on:** [PKG-14-3](PKG-14-3-race_en.md) (C4), [PKG-14-1](PKG-14-1-rulebook_en.md) (point 8, A6), [the rebuilder of II/11](../II-11-locality-readout/proof_en.md) · **Computation code:** `PKG-14-4-readout.py`

---

## 1. Question

With the fixed readout protocol, can the weave be read back from the winner (space, 8×8×8, $N = 290$), and does the ball give the space one among the three reference sequences?

## 2. Inputs and a note on the machinery

The run follows point 8 of PKG-14-1: pairwise closeness from the finished state; the neighbor count is singled out by the jump of the closeness list; a closed-degree filling from the space band ([PKG-14-3](PKG-14-3-race_en.md), C4: $N = 290$, the filling of the central shelf at 6). For free excluding instances the views can be computed exactly from the instance correlations — the accelerated form of [tool 4](../../appendix/B-machinery_en.md), with no new import: the closeness is the pairwise one-body map of the finished state.

**Closed-degree check:** the 290th beat is 6.000000, the 291st is 6.585786 — the gap is **exactly $2 - \sqrt{2}$**; the state is unambiguous, no projector is needed.

## 3. The result of the fixed run

**Closeness classes** (identically from every site of the weave, within-class spread below $10^{-12}$):

| Displacement class | Closeness | Displacements |
|---|---|---|
| neighbor (the 32 real directions, 1536 contracts) | **+0.164895** | ×6 |
| **antipodal mirror point (4,4,4)** | **+0.066406** | ×1 |
| body diagonal (1,1,1) | −0.054965 | ×8 |
| (1,2,2) | +0.020479 | ×24 |
| (0,0,2), (2,2,2), (2,4,4) | −0.019531 | ×6, ×8, ×6 |

- **Resonance sentinel (the form prescribed by the protocol):** other classes agreeing **exactly** with the neighbor class: **0** — the sentinel **did not signal**.
- **The jump — and here a protocol gap opened.** Point 8 of PKG-14-1 sought the jump on the closeness list, but did not state whether on the **signed** or the **absolute-value** list. On this weave the two **diverge**:

| Jump rule | Jump | k* | Classes drawn in | Edges | Real | Phantom | Missing |
|---|---|---|---|---|---|---|---|
| **signed** | after the 7th place, 3.24-fold | 7 | neighbor + antipodal | 1792 | **1536/1536** | **256** | 0 |
| absolute | after the 15th place, 2.68-fold | 15 | neighbor + antipodal + body diagonal | 3840 | **1536/1536** | 2304 | 0 |

- **Ball growth** (on the rebuilt network, $r \le 3$): by the signed route **1, 8, 32, 88**; by the absolute route 1, 16, 92, 296. The recorded reference sequences: line 1, 7, 13, 19 | plane 1, 7, 19, 37 | **space 1, 7, 25, 63**.

## 4. Verdict according to the protocol: partial failure

The weave **can be read back without gaps** — all 1536 real contracts are present, none missing, under both jump rules. But the winner **cannot be separated from its own antipodal echo**: the mirror point (4,4,4) of the weave carrying the bipartite mark sits on the closeness list behind the real neighbors but ahead of every other class, and thereby wins the jump race — 256 phantom edges, a complete antipodal pairing. The measured ball is therefore **1, 8, 32, 88**, not the recorded space sequence.

The failure is **not destructive**, and it is of a **different kind** from [II/13](../II-13-dimension-race/proof_en.md): there the echo agreed *exactly* with the neighbor, here it does not (0.066406 against 0.164895 — 40.3% of the neighbor). The closing of the loop therefore **failed partially** at this size, with two lessons to be recorded separately:

1. **The form of the sentinel was narrow.** The protocol prescribed the resonance sentinel in the form of "exact agreement"; here there is no exact agreement, so the sentinel stayed silent — while the echo spoiled the ranking all the same. The correct form is not an agreement test but a **band test**: the ratio of the weakest accepted and the strongest rejected closeness.
2. **A sign gap in the protocol.** The jump rule did not state whether it runs on the signed or the absolute list. On this weave the two give different k*; the main figures above are those of the signed reading.

Both lessons are **protocol faults, not result faults** — the rulebook is not modified, and the correction is the business of the next package.

## 5. Diagnosis — outside the verdict, with a separate label

A check of the cause of the failure on a larger weave (12×12×12, the closed degree nearest half filling from above). This falls **outside** the fixed 512-site scope, and is therefore not part of the verdict but its explanation:

- closed degree $N = 934$ (half filling 864), the gap above it exactly $2 - \sqrt{3}$;
- the neighbor closeness is +0.166146, the antipodal echo **−0.026620** — it changes sign, and falls to **16.0%** of the neighbor;
- the jump singles out six sharply: after the 6th place, **8.9-fold**;
- the rebuilding is **5184/5184, zero phantom, zero missing**;
- the ball is 1, 7, 25, 63, 129, 231 — the increment is 6, 18, 38, 66, 102, **exactly $4r^2 + 2$, up to $r = 5$**: the measured growth law of three extensions.

**Candidate conclusion:** the antipodal echo of the wrap-around of 8 is a **size artifact**; the mechanism is the mirror pairing of the bipartite mark — the same symmetry that won the race for space ([PKG-14-3](PKG-14-3-race_en.md), C3) spoils its readout at small size. On a larger weave the loop closes and the extension reading is sharp.

## 6. Import ledger and verdict on the package

New import: **zero.** The fixed run was carried out with the prescribed protocol, without modification; the failure is recorded exactly, according to the rule; the diagnosis stands with a separate label; the two protocol lessons are stated. **The package stands.**

## 7. Outgoing claims (PKG-14-5 and the synthesis may build only on these)

- **D1:** the fixed run failed partially: 1536/1536 real edges, zero missing, but 256 phantom edges (a complete antipodal pairing); the measured ball is 1, 8, 32, 88 instead of the recorded 1, 7, 25, 63.
- **D2:** the cause of the failure is identified: the antipodal mirror echo is the small-size price of the bipartite mark — unlike the resonance of II/13 it is **not** an exact agreement but a precedence in the ranking.
- **D3:** two protocol lessons recorded: (i) the agreement form of the sentinel is narrow, a band form is needed; (ii) the jump rule has a sign gap.
- **D4:** diagnosis (outside the scope, a candidate): on the 12-weave a clean rebuilding (5184/5184, zero phantom) and an exact $4r^2+2$ ball law up to $r = 5$.
- **D5:** the continuation is named: the fixed-scope repetition of the diagnosis, building in the two lessons of D3 — the name is reserved as **PKG-14-5**.
