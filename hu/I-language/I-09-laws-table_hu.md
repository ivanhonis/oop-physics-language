---
id: I-09
type: chapter
lang: hu
pair: I-09-laws-table_en.md
pair_status: in-sync
doc_version: "1.3"
status: ervenyes
---

# I/9. A törvények táblája

| # | Törvény | Bizonyító / árazó próba |
|---|---|---|
| 1 | Nincs mellékhatás-mentes getter. | ára = kötési energia ([I/7](I-07-measurement_hu.md), [II/1](../II-proofs/II-01-pair-bond/proof_hu.md)) |
| 2 | Az állapotot a rendszer birtokolja, nem a példány. | [II/1](../II-proofs/II-01-pair-bond/proof_hu.md) (½ különbség), [II/5](../II-proofs/II-05-triangle/proof_hu.md), [II/11](../II-proofs/II-11-locality-readout/proof_hu.md) (a szomszédság mint nézet) |
| 3 | A fejlődés súlytartó. | minden számolás szerkezeti alapja; clone()-tétel ([I/7](I-07-measurement_hu.md)) |
| 4 | A szerződés bíró és motor. | [II/2](../II-proofs/II-02-exchange-oscillation/proof_hu.md) (statika+dinamika egy számmal); II/3–II/10 mind rá épül |
| 5 | A példányazonosító nem adat. | [II/7](../II-proofs/II-07-bowl-magic-numbers/proof_hu.md) (bűvös számok), [II/8](../II-proofs/II-08-exclusion-vs-repulsion/proof_hu.md) (Hund), [II/11](../II-proofs/II-11-locality-readout/proof_hu.md) (átnevezés-próba a helyeken) |

Tételek (levezetettek): két típusosztály és a kizárás ([I/6](I-06-identity_hu.md)); kicserélődési kedvezmény ([I/6](I-06-identity_hu.md), [II/8](../II-proofs/II-08-exclusion-vs-repulsion/proof_hu.md)); clone() lehetetlensége és az átadási szemantika ([I/7](I-07-measurement_hu.md)); a getter díja ([I/7](I-07-measurement_hu.md)); egyformasági tétel ([II/6](../II-proofs/II-06-universality/proof_hu.md)); frusztráció-maradék ([II/5](../II-proofs/II-05-triangle/proof_hu.md)); sáv-tétel a csupa-háromszög rácson ([II/9](../II-proofs/II-09-kagome/proof_hu.md)); helyiség-visszaolvasás és felület-ismertetőjel ([II/11](../II-proofs/II-11-locality-readout/proof_hu.md)); összeomlási tétel és nyom-döntetlen ([II/12](../II-proofs/II-12-network-race/proof_hu.md)); szövés-összeesési lemma ([II/13](../II-proofs/II-13-dimension-race/proof_hu.md)); méret-műtermék tétel ([PKG-14-5](../II-proofs/II-14-dimension-staircase/PKG-14-5-readout-repeat_hu.md)); lyuk-tükör tétel ([PKG-15-5](../II-proofs/II-15-dimension-fourth-rung/PKG-15-5-hole-mirror_hu.md)); irány-tétel ([PKG-15-6](../II-proofs/II-15-dimension-fourth-rung/PKG-15-6-direction_hu.md)); tető-tétel ([PKG-15-7](../II-proofs/II-15-dimension-fourth-rung/PKG-15-7-top_hu.md)). Jelölt törvények: [III/1](../III-frontier/III-01-candidate-laws_hu.md).

A II/13 utáni négy tétel egy-egy mondatban, mert a szövegük a csomagokban áll, nem fejezetben: **a méret-műtermék tétel** — a kis szövésen fellépő átellenes visszhang a méret műterméke, nagyobb szövésen a kiolvasás hiánytalanul zárul; **a lyuk-tükör tétel** — két tükör-jegyű háló költségkülönbsége bármely töltésen egyenlő a tükörtöltésen vett különbséggel, vagyis a teli vég a ritka vég tükörképe; **az irány-tétel** — a ritka szakaszon a kisebb kiterjedésű háló a szigorúan olcsóbb, tanúsított szakaszhosszal minden páron; **a tető-tétel** — az előző kettő összefűzése: a legsűrűbb szakaszon a kisebb kiterjedés veri a nagyobbat. A tető-tétel a [III/1, 8.](../III-frontier/III-01-candidate-laws_hu.md) tető-törvényének tételi lába; a törvény másik, mért fele ott áll jelöltként.