---
id: PKG-15-6
type: package
part_of: II-15
lang: hu
pair: PKG-15-6-direction_en.md
pair_status: in-sync
doc_version: "1.3"
status: jovahagyva
builds_on: [PKG-15-5, PKG-15-2, II-12, I-06]
imports: nulla
---

# PKG-15-6 — Az irány-tétel (levezetés- és számolás-csomag)

**A csomag dolga.** Annak bizonyítása, hogy elég ritka szakaszon az alacsonyabb kiterjedésű szövés az olcsóbb — explicit küszöbbel, mind a hat rendezett jelölt-páron. A szkript: `shared/II-15-dimension-fourth-rung/PKG-15-6-direction.py`.

## 1. Hatókör (a levezetés előtt rögzítve)

**H1:** a tétel a 2 ≤ N ≤ N* szakaszról szól; azon kívül semmiről. **H2:** két küszöb van, mindkettő tétel-erejű — N*-analitikus (a lemma-lánc képletes tanúsítványa) és N*-gépi (a rögzített, véges rendszeren egzaktul tanúsított maximum); építésből az első legfeljebb akkora, mint a második, a távolságuk jelentendő. **H3:** a határhelyeket a tétel elvből nem adja ki — az átbillenések a létrák nemlineáris tartományában ülnek; a tétel az irányt bizonyítja. **H4:** az ütemenkénti dominancia szigorúbb az ár-sorrendnél, ezért N*-gépi is a mért ár-átbillenés alatt van; a dominancia-hézag jelentendő szám. **H5:** a tétel mind a hat rendezett párra szól; a tető-tétel (PKG-15-7) ebből a páros párt tükrözi át. **H6:** a teljes mezőnyhöz, a páros kontra nem-páros felső uralomhoz és a vonzás-importhoz nem nyúl.

## 2. A három lemma

**L5 — rendezési lemma.** Ha az X létra minden i-edik üteme legfeljebb akkora, mint az Y létra i-edik üteme az 1..N szakaszon, akkor X ára minden 1..N töltésen legfeljebb Y ára; és ha valamelyik ütemnél szigorúan kisebb, az ár attól a töltéstől szigorúan kisebb. *Bizonyítás:* az ár az ütemek részösszege; tagonkénti egyenlőtlenségek összege. ∎

**L6 — átfordítási lemma.** Az ütem-sorrend és a fok-számláló-sorrend ugyanaz az állítás: az i-edik ütem a legkisebb árszint, amely alatt már i fok van — a rendezett sor és a számlálófüggvény egymás inverzei. A ritka verseny így számláló-verseny. ∎

**L7 — szendvics-lemma.** Minden szövésen és minden hullámszámon (4/π²)·Q(k) ≤ λ(k) ≤ Q(k), ahol Q a visszahajtott fázisú merevség-alak (a fázisok a [−π, π) szakaszra hajtva, négyzetesen összegezve). *Bizonyítás:* tagonként a 2(1 − cos θ) ≤ θ² (minden θ-ra) és a 2(1 − cos θ) ≥ (4/π²)·θ² (|θ| ≤ π, egyenlőség a szélen) elemi egyenlőtlenségekből; az összegzés mindkét oldalt megőrzi. *Gépi hitelesítés:* a négy jelölt teljes rácsán a sértés nulla. ∎

## 3. A két réteg

**Analitikus tanúsítvány (L8):** a lemma-láncból, ha a rendezett Q-sorokra Q_X(i) ≤ (4/π²)·Q_Y(i), akkor λ_X(i) ≤ λ_Y(i) — N*-analitikus az első sérülés előtti index. **Gépi réteg:** N*-gépi a leghosszabb szakasz, amelyen λ_X(i) ≤ λ_Y(i) egzaktul áll; onnan az L5 zárja az ár-dominanciát. Mindkét réteg tétel-erejű a rögzített rendszeren; a gépi az éles.

## 4. Az irány-tétel — az eredmény

**Irány-tétel.** Mind a hat rendezett páron: a kisebb kiterjedésű jelölt ára a teljes 2..N*-gépi szakaszon szigorúan kisebb.

| Pár | N*-analitikus | **N*-gépi** | Ár-átbillenés | Lefedettség | Szigorú |
|---|---|---|---|---|---|
| vonal–sík | 1065 | **2599** | 4218 | 61,6% | áll |
| vonal–tér | 1609 | **3057** | 7127 | 42,9% | áll |
| vonal–négykit. | 1705 | **2981** | 6184 | 48,2% | áll |
| sík–tér | 349 | **4645** | 10285 | 45,2% | áll |
| sík–négykit. | 741 | **3677** | 7965 | 46,2% | áll |
| **tér–négykit.** | 7 | **2087** | 4740 | 44,0% | áll |

Ellenpróba: az ár-dominancia a tanúsított szakaszokon közvetlen összevetéssel is áll, mind a hat páron.

## 5. Leletek

- **A páronkénti átbillenés-tábla teljes.** Három szám új (vonal–tér 7127, vonal–négykiterjedés 6184, sík–tér 10285); három a korábbi mérésekkel egyezik (4218 és 7965 a sávhatárokkal, 4740 a PKG-15-5 tükörpárjával) — konzisztencia-pecsét.
- **A dominancia-hézag szisztematikus:** az ütemenkénti feltétel az ár-átbillenés 43–62%-áig tart, párra való tekintet nélkül. Regisztrált kérdés: miért ilyen stabil ez az arány.
- **A felső páron a folytonos kép majdnem üres** (N*-analitikus = 7 a tér–négykiterjedés páron): ott — ahogy az előkészítés előre jelezte — a diszkrét első-fok szerkezet visz (a rögzített helyszámon az oldalhossz a kiterjedéssel zsugorodik, ezért már az első fokok is kiterjedés-sorrendben ülnek: 2,75·10⁻⁶ / 5,71·10⁻³ / 6,08·10⁻² / 2−√3). A két mechanizmus — a számláló kitevője és az oldal-zsugorodás — egy irányba mutat.

## 6. Ítélet

**Áll.** Az irány-tétel mind a hat páron bizonyított, szigorúan, tétel-erejű gépi tanúsítvánnyal; a szendvics-lemma általános eszközként kimondva és hitelesítve.

## 7. Kimenő állítások

- **I1:** az irány-tétel a hat N*-gépi értékkel (4. szakasz táblája).
- **I2:** a tér–négykiterjedés páron **N* = 2087** — a tető-tétel (PKG-15-7) bemenete.
- **I3:** a szendvics-lemma (L7) általános, minden szövésre érvényes eszköz.
- **I4:** a teljes páronkénti átbillenés-tábla, három új számmal.
