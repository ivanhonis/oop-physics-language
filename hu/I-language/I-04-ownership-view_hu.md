---
id: I-04
type: chapter
lang: hu
pair: I-04-ownership-view_en.md
pair_status: missing
doc_version: "1.3"
status: ervenyes
---

# I/4. A birtoklás és a nézet

**Ahol az enkapszuláció megbukik.** Két objektumnál a klasszikus OOP azt várná: mindkettőnek saját súlypárja van, a rendszer állapota a kettő egymás mellé téve. A valóság mást csinál: a pár állapota a **kombinációk** súlyozása — négy súly a $(0,0)$, $(0,1)$, $(1,0)$, $(1,1)$ eseteken. A legtöbb súlynégyes nem áll elő két külön súlypár szorzataként. Ilyenkor a párnak van jól meghatározott állapota, a tagoknak külön-külön nincs. (A fizika ezt összefonódásnak hívja, kísérletileg sokszorosan igazolt.)

**Második törvény: az állapotot a rendszer birtokolja, nem a példány.** A „példány saját, teljes tudású állapota" csak akkor létezik, ha a közös állapot történetesen szétesik szorzatra. (Bizonyítás számmal: [II/1](../II-proofs/II-01-pair-bond/proof_hu.md) — a közös birtoklás előnye a legjobb példány-szintű állapothoz képest fél csatolásegység.)

**A nézet.** Ami a tagnak mindig jár, az egy csak-olvasható kivonat a közös állapotból:

- **Birtokolt állapot** — a súlyvektor. Birtokosa az az egység, ameddig az összefonódás ér.
- **Nézet** — a tag csak-olvasható, származtatott állapota: nem tárolt adat, hanem a közös állapotból számolt kivonat. Minden helyi kiolvasás statisztikáját pontosan megadja, de a közös állapot nem állítható vissza belőle: a tagok közti korrelációk nincsenek benne. (A fizika a nézetet kevert állapotnak, redukált sűrűségmátrixnak hívja.)

**A tanú-szabály.** A nézet számítása egyetlen szabály: a társat ki kell összegezni, és a tag két ágának helyi interferencia-képességéből annyi marad, amennyire a társ a két ágban azonos. A társ tanú: ahol a két ágban különbözik, ott „megjegyzi", melyik ágban jár a rendszer, és a megjelölt ágak helyben már nem interferálnak. (A fizika ezt parciális nyomnak hívja.)

**A nézetek tere: a korong.** A tiszta súlypárok a kör peremén élnek ($a^2 + b^2 = 1$); a nézetek a teljes korongot kitöltik. A perem a tiszta állapotok, a belső pontok az összefonódott tagok nézetei, a középpont a teljes tudatlanság. A nézet peremtől mért távolsága ezért a pár összefonódottságának számolható mérőszáma. (Komplex súlyokkal a kör gömbfelületté, a korong golyóvá bővül — a fizika Bloch-gömbjévé.)

**Számpróba.** Pár, 0,8 súllyal a $(0,1)$ esetén, 0,2-vel az $(1,0)$-n. A tag érték-kiolvasása 80–20 — pontosan ennyit adna egy magányos, tiszta $(\sqrt{0{,}8};\ \sqrt{0{,}2})$ súlypár is; ez a kiolvasás nem különbözteti meg őket. A félútra (45 fokra) forgatott kiolvasás igen: a tiszta állapot 90–10-et ad, az összefonódott tag nézete 50–50-et. A hiányzó interferenciát a társ vitte el — a két ágban teljesen különbözik, ezért mindet.
