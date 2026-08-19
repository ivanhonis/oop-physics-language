---
id: II-10
type: proof
lang: hu
pair: proof_en.md
pair_status: in-sync
doc_version: "1.3"
status: reszleges
builds_on: [II-01, II-06, I-07, I-08]
imports: nulla
---

# II/10. A belső tanú

**A kérdés.** A tanú eddig kívül állt ([I/5](../../I-language/I-05-contract_hu.md): a környezet; [I/7](../../I-language/I-07-measurement_hu.md): a műszer). Zárt rendszerben tanú csak belül lehet. Mikor tudja egy rendszer a saját környezete szerepét eljátszani — és mikor nem?

**A jelölt tétel.** Termalizáció a nyelven: a részek egymást tanúsítják, és egymás nézetét a hőmérséklet-súlyozta nézetbe csúsztatják. Két fél: **gyenge** egyenetlenségnél a motor ütemei a helyeken osztoznak, a tanúsítás végigterjed, a rész-nézetek a korong közepe felé csúsznak, a kezdőmintázat emléke elvész. **Erős** egyenetlenségnél a motor helyi motorok szorzatára esik szét: a tanúsítás nem terjed, a nézet a perem közelében reked — a rendszer örökre emlékszik. Az ív a [II/6](../II-06-universality/proof_hu.md)-é: ami egy objektumnál kisimult, az sok kizáró példánynál üzemmódot vált. (A fizika: termalizáció, ill. sok-test lokalizáció.)

**A rendszer.** Lánc 12 objektumból, körbezárva; az éleken a [II/1](../II-01-pair-bond/proof_hu.md) kötés-szerződése, minden objektumon véletlen erősségű érték-elfogultság ([I/8](../../I-language/I-08-contract-store_hu.md)). A hangolt paraméter az egyenetlenség erőssége ($W$, a kötés-csatolás egységében).

**Első ujjlenyomat: az ütem-létra statisztikája.** Két szomszédos fokköz arányának átlaga ($r$) két egzakt, publikált állandó közt választ: független ütemeknél $2 \ln 2 - 1 \approx 0{,}386$, egymást taszító (a helyeken osztozó) ütemeknél $\approx 0{,}531$. Számolva, sok sorsolás átlagában:

| W | 1 | 2 | 3 | 4 | 5 | 6 | 8 |
|---|---|---|---|---|---|---|---|
| r | 0,528 | 0,490 | 0,437 | 0,409 | 0,397 | 0,391 | 0,393 |

Átbillenés a taszítóból a függetlenbe, $W \approx 3$–$4$ körül. Nagyobb darabon (14 objektum) a két szél a két állandó felé élesedik: 0,5276 → 0,5284, illetve 0,3913 → 0,3874.

**Második ujjlenyomat: az emlék-próba.** Indítás befagyott, váltakozó mintázatból; mérve a megmaradó mintázat-különbség (I), a felező összefonódás (S) és a rész-nézet hossza:

| | gyenge (W = 1) | erős (W = 6) |
|---|---|---|
| emlék (I) ezerszeres időnél | 0,06 — elveszett | 0,54 — megmaradt |
| összefonódás (S) | gyorsan telítődik (2,87) | évtizedenként lépegetve kúszik, ezres idő alatt is csak 0,99 |
| nézet-hossz | 0,19 — középre csúszott | 0,62 — peremközelben rekedt |

**Ellenőrzés a valóságon.** A két állandó egzakt, ill. publikált érték; az átbillenési tartomány a publikált kis-lánc numerikával egyezik ([Pal–Huse 2010; Luitz és társai 2015](../../appendix/C-benchmarks_hu.md) — a becsült határ ezen a modellen $W \approx 3{,}5$); az emlék-megmaradást és a lassú összefonódás-kúszást mérték is: hideg atomok (Schreiber és társai, 2015), fogott ionok (Smith és társai, 2016).

**Import-számla:** nulla új tétel. **Mit igazolt:** a belső tanú tétel mindkét felét kis darabon, két független ujjlenyomattal. A végtelen-alak — éles fázis vagy drámai lassulás — a terep megoldatlan magja: [III. rész](../../III-frontier/III-02-open-questions_hu.md).