---
id: PKG-15-7
type: package
part_of: II-15
lang: hu
pair: PKG-15-7-top_en.md
pair_status: in-sync
doc_version: "1.4"
status: jovahagyva
builds_on: [PKG-15-6, PKG-15-5]
imports: nulla
---

# PKG-15-7 — A tető-tétel (összerakó csomag)

**A csomag dolga.** Az irány-tétel ([PKG-15-6](PKG-15-6-direction_hu.md)) és a lyuk-tükör tétel ([PKG-15-5](PKG-15-5-hole-mirror_hu.md)) összefűzése — új bizonyítás nélkül — a II/15 fő leletének tételi alakjává. A szkript: `shared/II-15-dimension-fourth-rung/PKG-15-7-top.py`.

## 1. A tétel

**Tető-tétel.** A rögzített rendszeren a 18649 ≤ N ≤ 20734 szakaszon a tér ára szigorúan kisebb a négykiterjedésénél; az N = 20735 töltésen egzakt holtverseny áll.

*Bizonyítás.* Az irány-tétel a tér–négykiterjedés páron a 2 ≤ N ≤ 2087 szakaszra adja a tér szigorú olcsóbbságát (PKG-15-6, I2). A lyuk-tükör tétel szerint két páros-jegyű háló költségkülönbsége bármely N töltésen egyenlő a tükörtöltésen (20736 − N) vett különbséggel (PKG-15-5). A 18649..20734 szakasz tükre pontosan a 2..2087 szakasz, ezért az előjel — a szigorúsággal együtt — egy az egyben áttükröződik; az N = 20735 tükre az N = 1, ahol mindkét háló nullát fizet. ∎

## 2. Gépi ellenőrzés

| Ellenőrzés | Eredmény |
|---|---|
| E1 — szigorú dominancia a tétel-szakaszon | a tér legkisebb előnye a 18649..20734 szakaszon **0,2072** — áll |
| E2 — egy-lyukas holtverseny | eltérés 1,7·10⁻¹³ — áll |
| E3 — a tükör-átvitel egzaktsága a szakaszon | legnagyobb eltérés 2,2·10⁻¹² — áll |
| E4 — lefedettség | a tanúsított 2086 töltés a mért páronkénti felső tartomány (15997..20734) **44,0%-a** |
| konzisztencia | a tanúsított szakasz teljes egészében a mért tér-sávban ül — áll |

## 3. Őszinte összevetés a méréssel

A tétel a tető **legfelső ~2100 töltésén** mondja ki, amit a II/15 mért: ott a tér veri a négykiterjedést — ez immár következmény, nem mérés. A mért tartomány maradéka (15997..18648) mért tény marad: ott az ár-sorrend áll, de az ütemenkénti dominancia már nem (ez a PKG-15-6-ban regisztrált dominancia-hézag). És a tétel páron belüli: azt, hogy a tetőn a páros pár **mindenki mást** is ver (a vonalat és a síkot), változatlanul a mérés mondja ([III/1, 7.](../../III-frontier/III-01-candidate-laws_hu.md)).

## 4. Ítélet

**Áll.** A tető-fordulás mindkét fele tételi lábon áll: a tükör-fele teljes egészében (PKG-15-5), az irány-fele a legfelső szakaszon (e csomag) — „a tetőn a három veri a négyet" a 18649..20734 szakaszon levezetett tény.

## 5. Kimenő állítások

- **F1:** a tető-tétel az 1. szakasz szerint, a 0,2072-es szigorúsági tartalékkal.
- **F2:** a mért tér-sáv kétrétegű olvasata: 18649-től tétel, alatta (15997-től) mérés — a határ maga a dominancia-hézag tükörképe.
- **F3:** a bizonyítási minta újrahasznosítható: irány-tétel + lyuk-tükör = tető-állítás, bármely jövőbeli páros páron (koordináció-pásztázásnál készen áll).
