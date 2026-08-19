---
id: PKG-16-5
type: package
part_of: II-16
lang: hu
pair: PKG-16-5-transfer_en.md
pair_status: missing
doc_version: "1.3"
status: jovahagyva
builds_on: [PKG-16-3, PKG-15-5, PKG-15-6, PKG-15-7]
imports: nulla
---

# PKG-16-5 — Tétel-átvitel a páros készleten (összerakó csomag)

**A csomag dolga.** A [lyuk-tükör tétel](../II-15-dimension-fourth-rung/PKG-15-5-hole-mirror_hu.md) szövege változatlanul érvényes tízes koordináción (két páros-jegyű szövés, azonos helyszám és helyenkénti szerződésszám) — új bizonyítás nem kell, csak alkalmazás a páros készletre: J5 (honos), KP3, KP4 (páros kontrollok) és a csupa-páratlan lépésű családtagok. A szkript: `shared/II-16-coordination-ten/PKG-16-5-transfer.py`.

## 1. Az átvitt tételek — gépi megerősítéssel

| Pár | Tükör-eltérés | N*-gépi | Tető-szakasz (tételként) | Legkisebb előny |
|---|---|---|---|---|
| KP3 – KP4 | 1,7·10⁻¹⁰ | 17 621 | 231 211 .. 248 830 | 0,0978 |
| KP3 – J5 | 1,3·10⁻⁹ | 18 081 | 230 751 .. 248 830 | 0,2451 |
| KP4 – J5 | 1,5·10⁻⁹ | 12 024 | 236 808 .. 248 830 | 0,1473 |
| **(1,3,5,7,9) – KP3** | 6,4·10⁻¹¹ | 14 491 | 234 341 .. 248 830 | 0,0228 |

Az egy-lyukas páros holtverseny (KP3–J5) 1,3·10⁻⁹-en áll. **A tanúsított tető-szakaszokon a páros sorrend tételként a ritka sorrend tükre: vonal < tér < négykiterjedés < ötkiterjedés** — a páros vonal-tag még a páros teret is veri a tetőn.

## 2. Mezőny-konzisztencia — a törvény legélesebb alakja

A teljes mezőny **utolsó 2000 töltéséből 1999-et a páros vonal-tag, az (1, 3, 5, 7, 9) nyer** — a teli vég a ritka vég tükre, és ritkán a vonal a legolcsóbb. A teljes mezőnyben tehát a törvény így hangzik: **a tetőt a mezőny legalacsonyabb kiterjedésű tükör-jegyű tagja viszi** — a fő ötösön ez a J5 (az egyetlen páros fő jelölt), a teljes mezőnyben a páros vonal.

## 3. Hatókör — őszintén

A tételi láb a tanúsított szakaszokra szól (a tető legfelső ~12–18 ezer töltése páronként); a sávhatárok (például a J5 fő-ötös sávjának 125 564-es nyitása) mért tények maradnak. A páros kontra nem-páros felső uralom változatlanul mért (III/1, 7.) — de immár három koordináción, kivétel nélkül.

## 4. Kimenő állítás

- **T1:** az egyesített tető-törvény („a tetőt a tükör-jegyűek közül a legalacsonyabb kiterjedésű viszi") tételi fele tízes koordináción is áll, a fenti szakaszokkal és tartalékokkal; a mért fele háromszorosan megerősített. A III/1 frissítésének alapja.
