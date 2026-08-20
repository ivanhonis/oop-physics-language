---
id: PKG-16-6
type: package
lang: hu
pair: PKG-16-6-hole-ladder-transfer_en.md
pair_status: missing
doc_version: "1.4"
status: jovahagyasra-var
part_of: II-16
builds_on: [PKG-15-10, PKG-15-11, PKG-16-1, PKG-16-3, II-12]
imports: nulla
---

# PKG-16-6 — A lyuk-létra tízes koordináción (tétel-átvitel)

**Egy mondatban.** A [teli-vég](../II-15-dimension-fourth-rung/PKG-15-10-dense-end_hu.md) és a [lyuk-létra](../II-15-dimension-fourth-rung/PKG-15-11-hole-ladder_hu.md) tétel **változatlan szöveggel** áll tízes koordináción is — és mellékesen független úton visszaadta a [PKG-16-3](PKG-16-3-race_hu.md) teljes sávtábláját.

## 1. Kérdés

Átvihető-e a lyuk-létra apparátus a tízes koordinációra, új levezetés nélkül? A bizonyítások sehol nem hivatkoznak a nyolcra: csak a nyom-döntetlenre, a $4k$ plafonra és a hordozó-tételre, és mindhárom tetszőleges $k$-ra van kimondva. Az átvitelhez tehát nem levezetés kell, hanem **számok** — egy tizenkétszer nagyobb mezőnyön, egy fokkal feljebb.

## 2. A rendszer

A [PKG-16-1](PKG-16-1-rulebook_hu.md) rögzített rendszere, változatlanul: $n = 248\,832 = 12^5$ hely, $k = 5$ pár, tízes koordináció. Ebből $T = 2kn = 2\,488\,320$ és a plafon $4k = 20$. A mezőny a deklarált fő ötös. A számolás a [H4](../../appendix/B-machinery_hu.md) hordozható úton; futtatható alak: `shared/II-16-coordination-ten/PKG-16-6-hole-ladder-transfer.py`.

## 3. Előfeltétel — a nyom-döntetlen mindkét létrán

| | Eltérés a $2\,488\,320$-tól |
|---|---|
| az ütem-létrák | $0{,}000$ — **áll** |
| a **lyuk-létrák** | $0{,}000$ — **áll** |

A lyuk-létra tehát tízesen is teljes jogú létra, ugyanazzal az összsúllyal (a [K-PKG1511-2](../II-15-dimension-fourth-rung/PKG-15-11-hole-ladder_hu.md) tízesen).

## 4. Eredmények

**E1 — a lyuk-létra azonosság** ($\text{ár}(n-m) = T - 4km + D(m)$), minden indulón, minden töltésen: legnagyobb eltérés $6{,}37\cdot10^{-10}$ — **áll**. (A nyolcashoz képest nagyobb szám: az $n$ tizenkétszerese, a halmozódás vele nő; a rögzített tűrés $10^{-8}$.)

**E2 — tükör-jegy ⟺ a két létra azonos:**

| Induló | Csúcs-ütem | Tükör-jegy |
|---|---|---|
| J1 vonal | 13,45754 | nem |
| J2 sík | 14,24999 | nem |
| J3 tér | 16,00000 | nem |
| J4 négykiterjedés | 17,00000 | nem |
| **J5 ötkiterjedés (honos)** | **20,00000** | **igen** |

Egyetlen tükör-jegyű induló — ahogy a [II/16](proof_hu.md) mérte.

**TA — az egy-lyukas töltés.** Az $N = n-1$ árak: J1 2 488 306,54; J2 2 488 305,75; J3 2 488 304; J4 2 488 303; **J5 2 488 300 = $T - 20$**. A győztes egyedül a J5, és tükör-jegyű — **a tétel áll**.

> **Egy különbség a nyolcashoz képest, kimondva.** Nyolcason két tükör-jegyű induló volt (BCC és hiperkocka), ezért az egy-lyukas töltésen **holtverseny** állt elő. Tízesen csak egy van, ezért **nincs holtverseny**. A tétel mindkét esetet ugyanúgy adja ki: a győztes tükör-jegyű, és a tükör-jegyűek egymással holtversenyben — ha többen vannak.

**E3 — a teli végi győztes = a legolcsóbb lyuk-létra.** Hét mintavett töltésen ($m = 1 \ldots 124\,416$) kivétel nélkül **áll**.

## 5. A pontos sávhatárok — és egy egyezés

A [K-PKG1511-4](../II-15-dimension-fourth-rung/PKG-15-11-hole-ladder_hu.md) éles kritériumával, páronként:

| Tükör-jegyű | Nem tükör-jegyű | A tükör-jegyű nyer $N \ge$ |
|---|---|---|
| J5 | J1 vonal | 66 066 |
| J5 | J2 sík | 94 002 |
| J5 | J3 tér | 101 417 |
| J5 | **J4 négykiterjedés** | **125 564** |

A megelőző sávot a J4 tartotta, ezért a J5 **teljes** sávjának alsó határa a J4 elleni páros határ: **125 564**.

> **Ez pontosan az a szám, amit a [PKG-16-3](PKG-16-3-race_hu.md) mért** („J5 — ötkiterjedés (honos): 125 564 .. 248 831"). A tétel tehát nem tanúsított szakaszt ad tízesen, hanem **a sávhatárt magát**.

## 6. Független reprodukció — ráadás

A számolt sávtábla összevetve a [PKG-16-3](PKG-16-3-race_hu.md) közzétettjével:

| Győztes | PKG-16-3 (közzétett) | PKG-16-6 (itt) |
|---|---|---|
| J1 vonal | 2 .. 42 661 | 1 .. 42 661 |
| J2 sík | 42 662 .. 85 085 | egyezik |
| J4 négykiterjedés | 85 086 .. 125 563 | egyezik |
| J5 ötkiterjedés | 125 564 .. 248 831 | egyezik |

**Mind a négy sávhatár egyezik**, és a **három továbbra sem kap sávot** — a lépcső kihagyja. (Az első és utolsó töltés holtverseny; ott az itteni futás egyszerűen az első minimálisat írja ki, a PKG-16-3 holtversenyként jelenti — ugyanaz a tény, más jelentési szokás.)

Ennek külön súlya van: a `PKG-16-3` a **visszavont H3 útra** van írva, ezért a padon `H4-VAR` státuszú. Ez az újraszámolás **zárt Fourier-alakból és a H4 hordozható úton** készült, tehát a sávtáblát két független ponton is megerősíti: más algoritmus, más számolási út.

## 7. Import-számla

Új import: **nulla.** A rendszer a PKG-16-1-ből; a tételek a PKG-15-10/11-ből, változatlan szöveggel; a nyom-döntetlen a II/12-ből.

## 8. Ítélet erről a csomagról

**Áll.** Az átvitel új levezetés nélkül sikerült, mind a négy ellenőrzés áll, és a sávtábla független reprodukciója ráadás.

## 9. Kimenő állítások

- **K1:** A lyuk-létra tétel és a teli-vég tétel **tízes koordináción is áll**, változatlan szöveggel; a lyuk-létra nyomösszege ott is $T$.
- **K2:** Tízesen egyetlen tükör-jegyű fő jelölt van (a honos öt), ezért az egy-lyukas töltésen **nincs holtverseny** — szemben a nyolcassal, ahol két tükör-jegyű állt holtversenyben. A tétel mindkét esetet ugyanúgy adja.
- **K3:** Az éles kritérium tízesen **a mért sávhatárt adja vissza pontosan** (125 564), nem csak tanúsított szakaszt.
- **K4:** A [PKG-16-3](PKG-16-3-race_hu.md) sávtáblája **független úton reprodukálva** (zárt alak + H4). Ez a `H4-VAR` adósság egy részét törleszti: a II/16 verseny fő eredménye a hordozható úton is visszajön.
- **K5:** A „három kimarad" lelet megerősítve: a tér-jelöltnek tízesen egyetlen győztes töltése sincs.

> A K1–K5 csak e csomag **jóváhagyása után** vezethető át a fejezetekbe.
