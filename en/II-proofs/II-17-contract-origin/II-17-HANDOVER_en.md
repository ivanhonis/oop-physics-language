---
id: II-17-handover
type: note
part_of: II-17
lang: en
pair: II-17-HANDOVER_hu.md
pair_status: in-sync
doc_version: "1.0"
status: ervenyes
builds_on: [PKG-17-1]
imports: "none"
---

# II/17 — Handover note (where we stand, what comes next)

**This file exists so that the dump of the repository is by itself enough to continue.** Whoever picks up the thread from here — human or machine — learns from this why II/17 exists, what is already closed, and what the next step is.

## 1. Why this chapter exists

Across three proofs, II/12–II/16 gave the same finding: **among hand-enumerated networks selection cannot be decided**, because the tuned members of the line family imitate everything. II/16 closed this: the top of the staircase is decided by the coordination number, and that we supply by hand. It follows that **three extensions live today in a single place in the language: in the 1/r form of attraction**, which II/4 receives as an import.

Tracing back to the structural root: the language regulates **who owns the state** (2nd law), but does not regulate **who owns the contract**. What is unregulated is left to the modeler — which is why we supply the network by hand. II/17 targets this hole. If the contract is born from the state of the instances, then the network becomes an output, and the form of 1/r cannot structurally be an import.

The escape route of the collapse theorem — the **empty site** (a contract without an instance) — is a trace of the same absence: such a thing can exist only if the contract is not carried by an instance.

## 2. What is closed

**`PKG-17-1-rulebook_en.md` — frozen (`jovahagyva`), not modifiable.** Its content: the lemma, the system (12 objects, all 66 pairs, a bond contract with variable content), the loop, the six members of the generating rule, two normalizations, four starts, 200 rounds, seed 1166, four verdict classes, the readout gate, the import ledger.

**`PKG-17-2-verify.py` — the B3 precondition, it ran, and the gate is clean.** What it returns: bond price exactly 45/66, degeneracy 132, closeness spread 1.5·10⁻¹⁶; the bond price of the ring 0.30105, its closenesses 0.4438 / 0.1231 / 0.0656 / 0.0448 / 0.0366; and in addition the closed form of II/1 and the three numbers of II/5 (3/2, fourfold degeneracy, 15/8). The zero test gives the expected result on all six family members.

**What the verification brought, still before the freezing:** the F5 (thresholded) family member takes every content to zero in a single round from the flat start. From this came the fourth verdict class (**EMPTY**) and the exception to T1. F5 stays in the family because it is the bridge towards the price of the empty contract.

## 3. What the verification recorded along the way (no need to derive again)

The closed form of the bond contract agrees when built by two routes: from the form of the four weights (`a² + d² + ½(b+c)²`) and in operator form as well. The ground state can be computed in magnetization blocks, and the degenerate case with an exact projector — this is the control method of II/11. The closeness measure is natural-based (the 0.69 mark of II/11 = ln 2).

## 4. The next step

**`PKG-17-2-loop.py`** — the loop itself. 48 runs (6 family members × 2 normalizations × 4 starts), 200 rounds, minutes. Every component it will use already stands ready in the verifier.

The order according to the rulebook: B3 precondition → zero test → degeneracy handler with logging → 48 runs → classification. **The gate of the readout: only in the case of an INTERMEDIATE verdict.**

## 5. The branching (fixed in advance, not to be chosen after the result)

| Verdict | What it means | Continuation |
|---|---|---|
| **INTERMEDIATE** | the lemma stands | PKG-17-3: readout; then a larger system, because an extension number cannot be pronounced on 12 objects |
| **PAIR** | the bond contract is a bad carrier | the same loop with the **smoothness contract**, on sites — a change of branch, not a failure |
| **FLAT** | closeness is not the extract from which structure can be born | a new question: is there another extract of the state that can break symmetry |
| **EMPTY** | generation carries off the network | the question of the price is to be brought forward (PKG-17-4) |

## 6. Pending language modifications

**May go at any time** (they record the present state, they do not claim a result):

1. `I-01-concept_en.md` — splitting the import ledger in two: *locality* (half an item, remains) and *the origin of the contract network* (new, entirely open line).
2. Missing `imports:` lines in the headers of the chapters that receive a network: II/3, II/4, II/6, II/9, II/10 → adjacency; II/12–II/16 → the enumerated field and the obligatory budget.

**Waiting on the result of the loop** (because they claim something about the solution):

3. `I-04-ownership-view_en.md` — the ownership of the contract is unregulated today.
4. `I-08-contract-store_en.md` — a new line: the empty contract, *candidate, its price underived*.
5. `III-01-candidate-laws_en.md` — a new 9th candidate with two legs: (a) the contract is obligatory between every pair, a derivation candidate from the 5th law; (b) the empty contract is not free, a derivation candidate from the 1st law. Together with a failure condition: if the resulting coordination number is sensitive to the form of the empty price, the candidate has failed.
6. `III-02-open-questions_en.md` — drawing the 2nd, the 7th and the density half of the 8th into a single program; its measure: *is there a chapter among whose inputs no network appears*.
7. `I-10-dictionary_en.md` — the line for the empty contract; the right-hand side is **to be left blank**, because physics has no established word for this.

**What must not be touched:** the table of laws of I/9. There is no sixth law until the proof has run.

## 7. One decision of principle already made

There will be no version number (**"descriptive language 2.0"**). Obsolescence does not strike the chapters but their inputs, and the register for that is the `imports:` field of the headers. The version is thus not a date but a query: **those chapters whose import list is empty.** Today there are three such (II/1, II/2, II/5) — II/8 is to be examined, because it already works today with a contract acting between every pair and decreasing with distance, so it may belong here from the start.

## 8. A risk worth keeping in view at the start of the next session

The five chapters **II/3, II/4, II/6, II/9, II/10** build on mixing running only between neighbors. With obligatory contracts this remains true only if the generated contents decrease with distance. **The first obligation is therefore not to produce geometry but to recover the decrease** — without that there is nothing further to examine.
