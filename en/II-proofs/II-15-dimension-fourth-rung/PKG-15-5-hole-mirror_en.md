---
id: PKG-15-5
type: package
part_of: II-15
lang: en
pair: PKG-15-5-hole-mirror_hu.md
pair_status: in-sync
doc_version: "1.4"
status: jovahagyva
builds_on: [PKG-15-3, II-12, I-06]
imports: zero
---

# PKG-15-5 — The hole-mirror theorem (derivation package)

**The business of the package.** It raises the mirror half of the main finding of II/15 — the top turn — from candidate to theorem, purely from the existing theorems of the language; the machine part is only confirmation. (A note on the name: [§8 of the rulebook](PKG-15-1-rulebook_en.md) reserved the name PKG-15-5 for the failure branch of the readout; the failure branch was not activated, so the name became free.) The script: `shared/II-15-dimension-fourth-rung/PKG-15-5-hole-mirror.py`.

## 1. The theorem

**Hole-mirror theorem.** Let two weaves have the same site count and the same number of contracts per site, both carrying the bipartite mark. Then at any filling N their cost difference equals their cost difference at the mirror filling (N′ = site count − N): **ΔPrice(N) = ΔPrice(N′).**

## 2. The derivation — four steps, zero new import

1. **The price of the whole ladder is fixed** (the trace-tie theorem, [II/12](../II-12-network-race/proof_en.md)): the sum of the whole ladder of every entrant is twice the budget — here 165888 — independently of the network.
2. **Decomposition:** the price of the lower N beats and the sum of the upper N′ beats together give the total sum. The lower race at N is therefore the race of the upper sums at N′, with reversed sign.
3. **The mirror of the bipartite mark:** on a weave carrying the bipartite mark the ladder is mirror-symmetric about the degree average (8) — the partner of every beat λ is the beat 16 − λ; the mirror of the zero mode is the peak beat at 16. Therefore the sum of the upper N′ beats = 16·N′ − (the price of the lower N′ beats).
4. **Assembled:** Price(N) = 165888 − 16·N′ + Price(N′). In the difference of two bipartite networks the network-independent terms cancel: ΔPrice(N) = ΔPrice(N′). ∎

## 3. Consequences — from the theorem

- **C1 (the top is the mirror of the sparse end):** the pairwise order of bipartite networks at N is identical to their order at N′ — at the top precisely the sparse-end order holds. The mirror half of the top turn measured in II/15 is thereby proved.
- **C2 (single-hole tie):** at N = 1 every network pays zero, therefore at a single hole (N = site count − 1) every bipartite network stands in an exact tie — the measured seal at 20735 follows from the theorem.
- **C3 (the peak beat):** the peak beat of every weave carrying the bipartite mark is exactly 16 (twice the coordination) — the mirror of the zero mode.
- **C4 (the explanation of the upper band boundary):** the tipping points of the bipartite pair form a mirror pair — the opening of the upper band of space (15997) is the mirror image of the sparse-end tipping (4740); their sum is the site count + 1.

## 4. Machine confirmation

| Check | Result |
|---|---|
| E1 — mirror identity | at most 3.6·10⁻¹² on the J3–J4 pair, 3.8·10⁻¹² on the J4–K3 pair — holds |
| E2 — single-hole tie | the deviation at the filling N = 20735 is 1.7·10⁻¹³ — holds |
| E3 — peak beat | J3, J4, K1, K2, K3 all exactly 16.000000000000 — holds |
| E4 — mirror pair of the tippings | 4740 and 15997; their sum is 20737 = site count + 1 — holds |
| E5 — negative control | on the non-bipartite J1–J2 pair the mirror deviation is 3446.5 — the bipartite condition is necessary |

## 5. Scope — honestly, what it does not claim

The theorem speaks only **between** networks carrying the bipartite mark; it says nothing about the bipartite versus non-bipartite comparison — the claim that "the upper half is won by the mirror pair" ([III/1, 7.](../../III-frontier/III-01-candidate-laws_en.md)) remains measured. And the **direction** of the turn — that when sparse the lower extension is the cheaper one — does not come from this theorem; that is a measured finding (the lower bands of II/13–II/15). The theorem gives the mirroring; the direction is given by the sparse end.

## 6. Outgoing claim

- **T1:** the hole-mirror theorem stands; the candidate mirror half of [III/1, 8.](../../III-frontier/III-01-candidate-laws_en.md) steps up to a theorem, and the measured tie at 20735 and the peak beat at 16 become derived facts.
