---
id: PKG-13-4
type: package
part_of: II-13
lang: en
pair: PKG-13-4-readout_hu.md
pair_status: in-sync
doc_version: "1.3"
status: jovahagyva
builds_on: [PKG-13-1, PKG-13-3, II-11]
imports: zero
---

# PKG-13-4 — Closing the loop: readout on the winner (derivation package)

**Builds on:** [PKG-13-3](PKG-13-3-race_en.md) (C4), [PKG-13-1](PKG-13-1-rulebook_en.md) (point 8, A6), [the rebuilder of II/11](../II-11-locality-readout/proof_en.md) · **Computation code:** `PKG-13-4-readout.py`

---

## 1. Question

With the fixed readout protocol, can the weave be read back from the winner (plane, $N = 11$)?

## 2. Inputs and a note on the machinery

The run follows point 8 of PKG-13-1: pairwise closeness from the finished state; the neighbor count is singled out by the jump of the closeness list; a filling at a closed degree ($N = 11$, degree gap 2 — the state is unambiguous). For free excluding instances the views can be computed exactly from the instance correlations — this is the accelerated form of [tool 4](../../appendix/B-machinery_en.md) for this case, with no new import.

## 3. The result of the fixed run

**Closeness classes** (identically from every site of the weave, spread $10^{-16}$):

| Displacement class | Correlation |
|---|---|
| neighbor (the 32 real contracts) | **+0.1875** |
| antipodal diagonal (2,2) | **+0.1875 — exactly identical** |
| everything else | −0.0625 |

- **The jump:** the ordered closeness list falls from 0.1723 to 0.0183 (ninefold) — but only after the **fifth** place: the protocol singles out $k = 5$.
- **Rebuilding:** all 32 real edges are present, none missing — but beside them **8 phantom edges** (all antipodal diagonals), with closeness **indistinguishable** from the real ones.
- **Ball growth:** measured 1, 6, 16 — instead of the recorded torus sequence (1, 5, 11, 15, 16).

## 4. Verdict according to the protocol: partial failure

The weave can be read back without gaps, but it **cannot be separated from its own wrap-around echo**: at this size, at the closed degree of the winner, the network and its echo coincide exactly on the closeness map. The caution of PKG-13-1 (A6: the two-or-four question may not be claimed at this size) must be extended: at this size the **clean** weave reading may not be claimed either. The failure is not destructive: no false geometry was written in place of the real one — an exact resonance pairing was written above the real one.

## 5. Diagnosis — outside the verdict, with a separate label

A check of the cause of the failure on a larger weave (8×8 torus, closed degree $N = 43$, filling 0.672 — the counterpart of the 0.688 of the fixed run). This falls **outside** the fixed 16-site scope, and is therefore not part of the verdict but its explanation:

- here the neighbor closeness is **strictly** dominant (2.07-fold relative to the next class);
- the jump singles out $k = 4$; the rebuilding is **128/128 edges, zero phantoms**;
- ball growth: 1, 5, 13, 25, 39, … — the increment is 4, 8, 12: **$+4r$ per step**, the measured law of two extensions (against the constant $+2$ of the line), until the weave wraps around.

**Candidate conclusion:** the 16-site resonance is a size artifact; on a larger weave the loop closes and the extension reading is sharp.

## 6. Import ledger and verdict on the package

New import: **zero.** The fixed run was carried out with the prescribed protocol, without modification; the failure is recorded exactly, according to the rule; the diagnosis stands with a separate label. **The package stands.**

## 7. Outgoing claims (the synthesis may build only on these)

- **D1:** the fixed run failed partially: 32/32 real edges + 8 phantom edges, with exactly identical closeness; the measured ball is not the recorded sequence.
- **D2:** the cause of the failure is identified: wrap-around resonance at the closed degree of the winner — a size-dependent phenomenon.
- **D3:** diagnosis (outside the scope, a candidate): clean rebuilding and the $+4r$ ball law on 8×8.
- **D4:** the synthesis should record [II/13](proof_en.md) as a partial result: race verdict (C2, C3) + readout limit (D1–D2) + size diagnosis (D3).
- **D5:** direction of extension: repeating the race and the readout on a larger system that already separates two and four extensions — a new package series, without modifying this one.
