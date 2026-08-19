---
id: PKG-15-5
type: package
part_of: II-15
lang: hu
pair: PKG-15-5-hole-mirror_en.md
pair_status: in-sync
doc_version: "1.4"
status: jovahagyva
builds_on: [PKG-15-3, II-12, I-06]
imports: nulla
---

# PKG-15-5 — A lyuk-tükör tétel (levezetés-csomag)

**A csomag dolga.** A II/15 fő leletének — a tető-fordulásnak — a tükör-felét emeli jelöltből tétellé, tisztán a nyelv meglévő tételeiből; a gépi rész csak megerősítés. (Névjegyzet: a [szabálykönyv §8](PKG-15-1-rulebook_hu.md) a PKG-15-5 nevet a kiolvasás bukás-ágára foglalta; a bukás-ág nem aktiválódott, a név felszabadult.) A szkript: `shared/II-15-dimension-fourth-rung/PKG-15-5-hole-mirror.py`.

## 1. A tétel

**Lyuk-tükör tétel.** Legyen két szövés azonos helyszámmal és helyenként azonos szerződésszámmal, mindkettő páros-jegyű. Ekkor bármely N töltésen a költségkülönbségük egyenlő a tükörtöltésen (N′ = helyszám − N) vett költségkülönbségükkel: **ΔÁr(N) = ΔÁr(N′).**

## 2. A levezetés — négy lépés, nulla új import

1. **A teljes létra ára rögzített** (nyom-döntetlen tétel, [II/12](../II-12-network-race/proof_hu.md)): minden induló teljes létrájának összege a költségvetés kétszerese — itt 165888 —, hálófüggetlenül.
2. **Felbontás:** az alsó N ütem ára és a felső N′ ütem összege együtt a teljes összeg. Az alsó verseny N-en tehát a felső összegek versenye N′-n, fordított előjellel.
3. **A páros-jegy tükre:** páros-jegyű szövésen a létra a fokátlag (8) körül tükrös — minden λ ütem párja a 16 − λ ütem; a nulla-módus tükre a 16-os csúcs-ütem. Ezért a felső N′ ütem összege = 16·N′ − (az alsó N′ ütem ára).
4. **Összerakva:** Ár(N) = 165888 − 16·N′ + Ár(N′). Két páros háló különbségében a hálófüggetlen tagok kiesnek: ΔÁr(N) = ΔÁr(N′). ∎

## 3. Következmények — tételből

- **K1 (a tető a ritka vég tükre):** páros hálók páronkénti sorrendje N-en azonos a sorrendjükkel N′-n — a tetőn pontosan a ritka-végi sorrend érvényes. A II/15-ben mért tető-fordulás tükör-fele ezzel bizonyított.
- **K2 (egy-lyukas holtverseny):** N = 1-en minden háló nullát fizet, ezért egy lyuknál (N = helyszám − 1) minden páros háló egzakt holtversenyben áll — a mért 20735-ös pecsét tételből következik.
- **K3 (a csúcs-ütem):** minden páros-jegyű szövés csúcs-üteme pontosan 16 (kétszer a koordináció) — a nulla-módus tükre.
- **K4 (a felső sávhatár magyarázata):** a páros pár átbillenési helyei tükörpárt alkotnak — a tér felső sávjának nyitása (15997) a ritka-végi átbillenés (4740) tükörképe; összegük a helyszám + 1.

## 4. Gépi megerősítés

| Ellenőrzés | Eredmény |
|---|---|
| E1 — tükör-azonosság | a J3–J4 páron legfeljebb 3,6·10⁻¹², a J4–K3 páron 3,8·10⁻¹² — áll |
| E2 — egy-lyukas holtverseny | eltérés az N = 20735 töltésen 1,7·10⁻¹³ — áll |
| E3 — csúcs-ütem | J3, J4, K1, K2, K3 mind pontosan 16,000000000000 — áll |
| E4 — átbillenések tükörpárja | 4740 és 15997; összegük 20737 = helyszám + 1 — áll |
| E5 — negatív kontroll | a nem-páros J1–J2 páron a tükör-eltérés 3446,5 — a páros feltétel szükséges |

## 5. Hatókör — őszintén, mit nem mond ki

A tétel csak páros-jegyű hálók **között** szól; a páros kontra nem-páros összevetésről semmit — a „felső felet a tükör-pár nyeri" állítás ([III/1, 7.](../../III-frontier/III-01-candidate-laws_hu.md)) mért marad. És a fordulás **iránya** — hogy ritkán az alacsonyabb kiterjedés az olcsóbb — nem ebből a tételből jön; az mért lelet (a II/13–II/15 alsó sávjai). A tétel a tükrözést adja; az irányt a ritka vég adja.

## 6. Kimenő állítás

- **T1:** a lyuk-tükör tétel áll; a [III/1, 8.](../../III-frontier/III-01-candidate-laws_hu.md) jelölt tükör-fele tétellé lép, a mért 20735-ös holtverseny és a 16-os csúcs-ütem levezetett ténnyé.
