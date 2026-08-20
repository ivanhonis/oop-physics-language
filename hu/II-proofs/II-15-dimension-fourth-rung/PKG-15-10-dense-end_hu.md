---
id: PKG-15-10
type: package
lang: hu
pair: PKG-15-10-dense-end_en.md
pair_status: missing
doc_version: "1.4"
status: jovahagyva
part_of: II-15
builds_on: [II-12, PKG-15-5, PKG-15-6, PKG-15-9]
imports: nulla
---

# PKG-15-10 — A teli-vég tétel (levezetés-csomag)

**Egy mondatban.** A tető-törvény **hordozó-fele eddig mérés volt; innentől tétel**: mivel minden induló létrájának összsúlya azonos, a teli vég felől a legolcsóbb induló az, amelyiknek a **legmagasabb** ütemei a legnagyobbak — és a csúcs-ütem pontosan a tükör-jegyűeknél maximális.

## 1. Kérdés

A [III/1, 8.b](../../III-frontier/III-01-candidate-laws_hu.md) hiányzó tétele: **miért a tükör választ?** A [PKG-15-9](PKG-15-9-uniform-field_hu.md) megmondta, *mely* szövés tükör-jegyű (hordozó-tétel); ez a csomag azt mondja meg, *miért nyer* a tükör-jegyű a teli végen.

## 2. Jelölés

Rögzített $n$ hely és $k$ darab $\pm$ lépéspár (koordináció $2k$). Egy $X$ induló ütem-létrája növekvő sorrendben $\lambda^X_{(1)} \le \dots \le \lambda^X_{(n)}$. Az **ár** az alulról töltés költsége, a **felső farok** a legdrágább ütemek összege:

$$\text{ár}_X(N) = \sum_{i=1}^{N} \lambda^X_{(i)}, \qquad S_X(m) = \sum_{i=n-m+1}^{n} \lambda^X_{(i)}.\tag{K-PKG1510-1}$$

## 3. A levezetés — négy lemma, nulla import

**L1 — Nyom-döntetlen.** Minden induló összsúlya azonos:

$$T \;=\; \sum_{j} \lambda^X_j \;=\; 2kn \qquad \text{minden } X\text{-re.}\tag{K-PKG1510-2}$$

*Bizonyítás:* egy $s$ lépés járuléka $\sum_j \bigl(2 - 2\cos(2\pi\langle j,s\rangle/n)\bigr) = 2n$, mert egy nemtriviális karakter összege a csoporton nulla. $k$ lépéssel $2kn$. $\square$ (Ez a [II/12](../II-12-network-race/proof_hu.md) nyom-döntetlen tétele, a szövés-családra kimondva.)

**L2 — Kiegészítés.** Az L1-ből azonnal:

$$\text{ár}_X(N) \;=\; T - S_X(n-N).\tag{K-PKG1510-3}$$

> **Ez a csomag fordulópontja.** A teli vég felől nézve az alulról töltés nem versenyzés, hanem **kivonás**: adott $N$-nél a legolcsóbb induló pontosan az, amelyik a **legtöbbet hagyja ki**. A teli végen tehát nem az számít, kinek olcsóbbak az alsó ütemei, hanem kinek **drágábbak a felsők**.

**L3 — Csúcs-korlát.** Minden indulóra $\lambda^X_{\max} \le 4k$, és **egyenlőség pontosan akkor, ha $X$ tükör-jegyű**.

*Bizonyítás:* minden tag $2 - 2\cos\theta \le 4$, tehát $\lambda \le 4k$. Egyenlőség egy $j$-nél akkor és csak akkor, ha $\cos(2\pi\langle j,s\rangle/n) = -1$ minden $s$ lépésre, azaz $\langle j,s\rangle \equiv n/2 \pmod n$ mindenütt. Ilyen $j$ pontosan akkor létezik, ha van olyan másodrendű karakter, amely minden generátoron $-1$ — és ez szó szerint a [hordozó-tétel](PKG-15-9-uniform-field_hu.md) kétszínezése. $\square$ (Feltétel: $n$ páros; minden rögzített rendszerünkben az.)

**L4 — Tükör-alak.** Ha $X$ tükör-jegyű, a létrája szimmetrikus a $2k$ körül ($\lambda \leftrightarrow 4k-\lambda$), ezért $S_X(m) = 4km - \text{ár}_X(m)$, és az L2-vel:

$$\text{ár}_X(n-m) \;=\; T - 4km + \text{ár}_X(m).\tag{K-PKG1510-4}$$

> **Ez a [lyuk-tükör tétel](PKG-15-5-hole-mirror_hu.md), egy sorban.** A PKG-15-5 négy lépésben vezette le; itt az L1 és az L3 következménye. Két tükör-jegyű indulóra a különbség $\text{ár}_X(n-m) - \text{ár}_Y(n-m) = \text{ár}_X(m) - \text{ár}_Y(m)$: **a teli végi sorrend azonos a ritka végivel** — amivel az [irány-tétel](PKG-15-6-direction_hu.md) a legalacsonyabb kiterjedésű tükör-jegyűt teszi a tetőre.

## 4. A két tétel

> **TA — Egy-lyuk tétel.** Az $N = n-1$ töltésen $\text{ár}_X(n-1) = T - \lambda^X_{\max} \ge T - 4k$, és egyenlőség pontosan a tükör-jegyűeknél. **A győztes tehát bizonyíthatóan tükör-jegyű, és a tükör-jegyűek holtversenyben állnak.**

Ez egzakt, tanúsított szakasz nélkül — és pontosan az, amit a [PKG-15-5](PKG-15-5-hole-mirror_hu.md) *mért* („a 20735-ös holtverseny és a 16-os csúcs-ütem"). Most levezetve.

> **TB — Teli-vég tétel.** Legyen $X$ tükör-jegyű, $Z$ nem az, és $\delta_Z = 4k - \lambda^Z_{\max} > 0$ a $Z$ **csúcs-hiánya**. Ha
>
> $$\text{ár}_X(m) \;<\; m\,\delta_Z,\tag{K-PKG1510-5}$$
>
> akkor $X$ szigorúan olcsóbb $Z$-nél az $N = n-m$ töltésen.

*Bizonyítás:* $S_Z(m) \le m\lambda^Z_{\max} = m(4k-\delta_Z)$, míg az L4 szerint $S_X(m) = 4km - \text{ár}_X(m)$. Ha (K-PKG1510-5) áll, akkor $S_X(m) > S_Z(m)$, és az L2 miatt $\text{ár}_X(n-m) < \text{ár}_Z(n-m)$. $\square$

**Hatókör, kimondva:** a (K-PKG1510-5) **elégséges**, nem szükséges — a tanúsított szakasz a valódi alsó becslése. Ez az [irány-tétel](PKG-15-6-direction_hu.md) mintája: tanúsított szakasz, számmal jelentve.

## 5. Gépi megerősítés

Futtatható alak: `shared/II-15-dimension-fourth-rung/PKG-15-10-dense-end.py`. Rendszer: a II/15 rögzített 20736 helye, $k=4$, $T = 165888$, $4k = 16$. A hordozható H4 úton.

| Lépés | Eredmény |
|---|---|
| **L1** nyom-döntetlen | legnagyobb eltérés $0{,}000$ — áll |
| **L2** kiegészítés, minden töltésen | $2{,}910\cdot10^{-11}$ — áll |
| **L3** csúcs-korlát és egyenlőség | mind az 5 indulón áll |
| **L4** tükör-alak, minden $m$-re | $3{,}3\cdot10^{-11}$ (BCC), $3{,}5\cdot10^{-11}$ (hiperkocka) — áll |

**Csúcsok és csúcs-hiányok:**

| Induló | Csúcs | Hiány $\delta$ | Tükör-jegy |
|---|---|---|---|
| J1 vonal | 11,03912 | 4,96088 | nem |
| J2 sík (király) | 12,00000 | 4,00000 | nem |
| J3 tér (BCC) | 16,00000 | 0 | **igen** |
| J3′ tér (lapátló) | 13,00000 | 3,00000 | nem |
| J4 hiperkocka | 16,00000 | 0 | **igen** |

**TA a mezőnyön:** az $N = 20735$ árak — J1 165876,96; J2 165876; J3′ 165875; **J3 és J4 egyaránt 165872 = $T - 16$**. A győztesek pontosan a két tükör-jegyű, holtversenyben. **A TA áll.**

**TB tanúsított szakaszai** (mindegyik gépileg visszaellenőrizve, hogy a következtetés valóban áll a szakaszon):

| Tükör-jegyű $X$ | Nem tükör-jegyű $Z$ | $\delta_Z$ | Tanúsítva $N \ge$ |
|---|---|---|---|
| J3 (BCC) | J1 vonal | 4,96 | 14088 |
| J3 (BCC) | J2 sík | 4,00 | 16486 |
| J3 (BCC) | J3′ lapátlós tér | 3,00 | 18251 |
| J4 hiperkocka | J1 vonal | 4,96 | 13509 |
| J4 hiperkocka | J2 sík | 4,00 | 16653 |
| J4 hiperkocka | J3′ lapátlós tér | 3,00 | 18853 |

**Összesítve:** a közzétett mezőnyben (BCC-vel) a J3 az $N \ge 16486$ szakaszon **tételből** veri mindkét nem tükör-jegyű indulót — 4251 töltésen. A mért sávja 15997-től nyílt, tehát a tanúsítás a valódi szakasz szolid, konzervatív alsó becslése, ahogy vártuk.

## 6. Import-számla

Új import: **nulla.** Az L1 a II/12 tétele; az L3 egyenlőség-fele a PKG-15-9 hordozó-tétele; az L2 és az L4 tiszta átrendezés. A TA és a TB ezekből következik.

## 7. Ítélet erről a csomagról

**Áll.** Négy lemma és két tétel, mind gépileg megerősítve a rögzített rendszeren.

## 8. Kimenő állítások

- **K1:** **Kiegészítési azonosság** (K-PKG1510-3): a nyom-döntetlen miatt az alulról töltés a teli vég felől kivonás; a teli végen a legdrágább ütemek döntenek.
- **K2:** **Egy-lyuk tétel (TA):** az $N = n-1$ töltésen a győztes bizonyíthatóan tükör-jegyű, és a tükör-jegyűek holtversenyben állnak. A [PKG-15-5](PKG-15-5-hole-mirror_hu.md) mért holtversenye ezzel **tétel**.
- **K3:** **A lyuk-tükör tétel egysoros alakja** (K-PKG1510-4), az L1 és L3 következményeként.
- **K4:** **Teli-vég tétel (TB):** ha $\text{ár}_X(m) < m\,\delta_Z$, akkor a tükör-jegyű $X$ veri a nem tükör-jegyű $Z$-t az $N = n-m$ töltésen. Tanúsított szakaszok a rögzített rendszeren: J3 kontra minden nem tükör-jegyű $N \ge 16486$-tól, J4 kontra ugyanazok $N \ge 18853$-tól.
- **K5:** **A tető-törvény hordozó-fele levezetve.** Ami eddig mérés volt („a tetőt tükör-jegyű tag viszi", háromból hármon mérve), az egy tanúsított szakaszon tétel, az egy-lyukas töltésen pedig egzakt. Mérés csak annyi marad, hogy a tanúsított szakasz meddig ér a valódi sávhoz képest.
- **K6:** **A III/1, 8.b hiányzó tétele lezárható.** A hordozó-kérdés két fele — *mely* szövés tükör-jegyű ([PKG-15-9](PKG-15-9-uniform-field_hu.md)) és *miért nyer* a tükör-jegyű (ez a csomag) — együtt megvan.

**Bővítési irány:** a TB átvitele tízes koordinációra (a [PKG-16-5](../II-16-coordination-ten/PKG-16-5-transfer_hu.md) mintájára, változatlan szöveggel), és a tanúsított szakasz élesítése — a $S_Z(m) \le m\lambda^Z_{\max}$ becslés a leggyengébb láncszem.

> A K1–K6 csak e csomag **jóváhagyása után** vezethető át a fejezetekbe.
