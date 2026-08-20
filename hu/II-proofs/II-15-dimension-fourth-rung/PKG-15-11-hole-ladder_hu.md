---
id: PKG-15-11
type: package
lang: hu
pair: PKG-15-11-hole-ladder_en.md
pair_status: missing
doc_version: "1.4"
status: jovahagyva
part_of: II-15
builds_on: [PKG-15-10, PKG-15-9, PKG-15-5, II-12]
imports: nulla
---

# PKG-15-11 — A lyuk-létra (élesítő levezetés-csomag)

**Egy mondatban.** A [teli-vég tétel](PKG-15-10-dense-end_hu.md) egyenlőtlensége **azonosságra cserélhető**: minden induló magával hordoz egy második létrát — a **lyuk-létrát** —, és a teli végi verseny nem más, mint a szokásos, alulról töltő verseny ezen a második létrán.

## 1. Kérdés

A [PKG-15-10](PKG-15-10-dense-end_hu.md) egy gyenge láncszemet hagyott: a **TB** tétel a vesztes felső farkát a $m\lambda^Z_{\max}$ becsléssel korlátozta, ami bőkezű, ezért a tanúsított szakasz a valódinak csak alsó becslése volt. Kiváltható-e a becslés azonossággal?

## 2. A lyuk-létra

Írjuk fel minden ütemet a **plafontól mért távolságával**:

$$\delta^Y_{(i)} \;=\; 4k - \lambda^Y_{(n-i+1)}, \qquad i = 1,\dots,n\tag{K-PKG1511-1}$$

Ez ismét nemnegatív, növekvő létra — a **lyuk-létra** —, és a nyomösszege ugyanaz:

$$\sum_i \delta^Y_i \;=\; 4kn - T \;=\; 4kn - 2kn \;=\; 2kn \;=\; T.\tag{K-PKG1511-2}$$

Vagyis a lyuk-létra **teljes jogú létra**: ugyanazzal az összsúllyal, ugyanabban a családban. A hozzárendelés **involúció**: a lyuk-létra lyuk-létrája az eredeti.

## 3. A tétel

> **Lyuk-létra tétel.** Minden $Y$ indulóra és minden $m$-re
>
> $$\text{ár}_Y(n-m) \;=\; T - 4km + D_Y(m),\tag{K-PKG1511-3}$$
>
> ahol $D_Y(m)$ a **lyuk-létra** alulról töltésének költsége $m$-ig.

*Bizonyítás:* a legdrágább $m$ ütem a legolcsóbb $m$ lyuk, tehát $S_Y(m) = 4km - D_Y(m)$; ezt a [PKG-15-10](PKG-15-10-dense-end_hu.md) kiegészítési azonosságába (K-PKG1510-3) helyettesítve adódik. $\square$

**Semmilyen szimmetria-feltevés nincs benne.** A (K-PKG1511-3) minden indulóra áll, tükör-jegyűre és nem tükör-jegyűre egyaránt — ezért lép a becslés helyébe.

## 4. Következmények

**K-a — A teli vég nem másfajta feladat.** A teli végen a győztes pontosan az, akinek a **lyuk-létrája a legolcsóbb alulról töltve**. Az $m$ hely üresen hagyása ugyanaz a feladat, mint $m$ lyuk betöltése — egy másik létrán.

**K-b — A tükör-jegy létra-azonosság.** Egy induló akkor és csak akkor tükör-jegyű, ha a **lyuk-létrája megegyezik az ütem-létrájával**. Ez a [lyuk-tükör tétel](PKG-15-5-hole-mirror_hu.md) legtömörebb alakja: nem két töltés közti reláció, hanem két létra azonossága. (A név innen kap értelmet.)

**K-c — A TB élessé válik.** A [PKG-15-10](PKG-15-10-dense-end_hu.md) TB tétele helyett:

$$X \text{ olcsóbb } Z\text{-nél az } N = n-m \text{ töltésen} \iff D_X(m) < D_Z(m).\tag{K-PKG1511-4}$$

A régi elégséges feltétel **érvényes marad** — olcsó próba, amely a $Z$-ről csak a csúcsát kívánja —, de sokat ad fel.

**K-d — Az egész gépezet átvihető.** A nyom-döntetlen és a kiegészítés a lyuk-létrára is áll (K-PKG1511-2), tehát minden, amit a ritka végről tudunk, alkalmazható a teli végre — a lyuk-létrán.

## 5. Gépi megerősítés

Futtatható alak: `shared/II-15-dimension-fourth-rung/PKG-15-11-hole-ladder.py`. A II/15 rögzített rendszerén, a H4 hordozható úton.

| Ellenőrzés | Eredmény |
|---|---|
| **E1** a (K-PKG1511-3) azonosság minden indulón, minden $m$-re | legnagyobb eltérés $3{,}96\cdot10^{-11}$ — **áll** |
| **E2** tükör-jegy ⟺ a két létra azonos | mind az 5 indulón áll (J3 BCC és J4 igen; J1, J2, J3′ nem) |
| **E3** a teli végi győztes = a legolcsóbb lyuk-létra | 12 mintavett töltésen kivétel nélkül **áll** |

**E4 — mennyit adott fel az egyenlőtlenség.** A `PKG-15-10` tanúsított határa és a valódi határ:

| Tükör-jegyű $X$ | Nem tükör-jegyű $Z$ | Tanúsított $m$ | **Pontos $m$** | Feladott |
|---|---|---|---|---|
| J3 (BCC) | J1 vonal | 6648 | **13609** | 6961 |
| J3 (BCC) | J2 sík | 4250 | **10451** | 6201 |
| J3 (BCC) | J3′ lapátlós tér | 2485 | **6993** | 4508 |
| J4 hiperkocka | J1 vonal | 7227 | **14552** | 7325 |
| J4 hiperkocka | J2 sík | 4083 | **12771** | 8688 |
| J4 hiperkocka | J3′ lapátlós tér | 1883 | **10936** | 9053 |

A becslés két-hatszoros tartalékkal dolgozott. Például a J3 a J2-t nem az $N \ge 16486$ szakaszon veri, hanem **$N \ge 10285$-től** — vagyis már fél-töltés alatt.

## 6. Import-számla

Új import: **nulla.** A (K-PKG1511-1) definíció, a (K-PKG1511-2) egysoros számolás, a (K-PKG1511-3) a PKG-15-10 kiegészítési azonosságának átírása.

## 7. Ítélet erről a csomagról

**Áll.** Egy tétel, négy következmény, mind gépileg megerősítve; a `PKG-15-10` egyetlen becslése azonossággal kiváltva.

## 8. Kimenő állítások

- **K1:** **Lyuk-létra tétel** (K-PKG1511-3): minden indulóra $\text{ár}(n-m) = T - 4km + D(m)$, ahol $D$ a lyuk-létra alulról töltése. Szimmetria-feltevés nélkül.
- **K2:** A lyuk-létra nyomösszege ugyanaz ($T$), és a hozzárendelés involúció — a lyuk-létra teljes jogú létra ugyanabban a családban.
- **K3:** **Tükör-jegy ⟺ a lyuk-létra azonos az ütem-létrával.** A lyuk-tükör tétel legtömörebb alakja.
- **K4:** A [PKG-15-10](PKG-15-10-dense-end_hu.md) TB tétele **élessé vált** (K-PKG1511-4); a régi elégséges feltétel érvényes marad olcsó próbaként, de 4500–9000 töltést ad fel a hat vizsgált páron.
- **K5:** A teli végről szóló minden állítás visszavezethető a ritka végre — a lyuk-létrán. A gépezet nem bővül, csak kétszer használjuk.

**Bővítési irány, óvatosan kimondva.** A lyuk itt **saját költséglétrával rendelkező, származtatott objektumként** viselkedik, és a hozzárendelés involúció. Ez formai rokonságot mutat a [III/2, 7. nyitott kérdésével](../../III-frontier/III-02-open-questions_hu.md) (a mintázatból lett objektum) — de **csak rokonság**: itt a lyuk-létra levezetett átírás, nem új típusosztály. Állításnak nem vesszük, iránynak igen.

> A K1–K5 csak e csomag **jóváhagyása után** vezethető át a fejezetekbe.
