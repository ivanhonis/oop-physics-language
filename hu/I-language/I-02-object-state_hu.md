---
id: I-02
type: chapter
lang: hu
pair: I-02-object-state_en.md
pair_status: missing
doc_version: "1.3"
status: ervenyes
---

# I/2. Az objektum és az állapot

Egy objektumtípus matematikailag egy pár: $O = (S, M)$, ahol $S$ az állapotok halmaza (a „mezők" lehetséges értékei együtt), $M$ a megengedett műveletek halmaza: $S \to S$ leképezések (a „metódusok"). Egy **példány** egy konkrét állapot ebből a halmazból.

**Az állapot nem érték, hanem súlyozás.** A legkisebb rendszer: egy objektum két lehetséges értékkel (0 és 1). Az állapota nem „0 vagy 1", hanem egy súlypár $(a, b)$: mennyire van a rendszer a 0-ban és mennyire az 1-ben. Kiolvasáskor $a^2$ valószínűséggel 0-t, $b^2$ valószínűséggel 1-et kapunk.

**A súlyok összhossza rögzített: $a^2 + b^2 = 1$.** Ez nem külön feltevés, hanem a kiolvasási szabály lezárása: a kimenetek valószínűségeinek összege 1. Az állapotok tere tehát az egységnyi hosszú súlyvektorok halmaza — ezért beszélhetünk a fejlődésről mint **forgatásról**. Két súlyvektor, amely csak egy egységnyi nagyságú közös szorzóban tér el, minden kiolvasásra ugyanazt mondja: ugyanaz az állapot.

A teljes fizikai leíráshoz a súlyok komplex számok; az alapok megértéséhez a legtöbb helyen elég valósnak venni őket. Hogy a komplex súly nem díszítés, hanem kényszer, azt a negyedik törvény mondja ki ([I/5](I-05-contract_hu.md)), éles kísérleti próbáját a [III. rész 1. nyitott kérdése](../III-frontier/III-02-open-questions_hu.md) őrzi. (A fizika ezt a kétértékű objektumot kvantumbitnek hívja.)
