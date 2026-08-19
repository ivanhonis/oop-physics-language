---
id: II-09
type: proof
lang: hu
pair: proof_en.md
pair_status: missing
doc_version: "1.3"
status: ervenyes
builds_on: [II-01, II-05, I-05]
imports: "egy tétel: Kagome-szomszédság (a helyiség-import geometriai folytatása)"
---

# II/9. A Kagome-próba

**A kérdés.** Az első terep, ahol a nyelv nem lezárt eredményt számol vissza, hanem versenyt dönt el: a csupa sarokban érintkező háromszögből épült rács (a fizika Kagome-rácsa) két jelöltje közül melyik az egyensúly — a befagyott párosítás, ahol minden objektum fix párban ül, vagy a fedések önforgó keveréke, amelyet a motor a hatszög-körök mentén forgat.

**A sáv — számolás előtt, a nyelv fogalmaiból.** $N$ objektumra $2N$ kötés és $2N/3$ háromszög jut, és minden kötés pontosan egy háromszögé — az összköltség tehát háromszög-költségek összege. A [II/5](../II-05-triangle/proof_hu.md) tétele ezért szigorú **padlót** ad: $(2N/3) \cdot (3/2) / (2N) = \tfrac{1}{2}$ kötésenként, ez alá semmilyen állapot nem mehet. A befagyott fedés könyvelése **plafont**: a kötések negyede tökéletes (0), háromnegyede két lekötött, egymással korrelálatlan tag közt fut — a nézetük a korong középpontja, az ilyen kötés ára ¾ —, átlagban $\tfrac{1}{4} \cdot 0 + \tfrac{3}{4} \cdot \tfrac{3}{4}$ = **9/16**. És a [4. törvény](../../I-language/I-05-contract_hu.md) ítélete: a befagyott fedés nem önforgó mintázat — nem is jelölt egyensúly. A jóslat: a győztes önforgó keverék, költsége a sáv belsejében.

**A számolás.** Kis rács-darabok (12 és 18 objektum, körbezárt peremmel) teljes állapotterének pontos minimuma, a [II/1](../II-01-pair-bond/proof_hu.md) szerződésével minden élen; kontrollnak ugyanez négyzetrácson (16 objektum), ahol háromszög nincs.

**Az eredmény** (költség kötésenként, csatolásegységben):

| állapot | költség/kötés |
|---|---|
| padló (háromszög-tétel) | 0,5 |
| Kagome-darab, 12 objektum (pontos) | **0,5231** |
| Kagome-darab, 18 objektum (pontos) | **0,5264** |
| végtelen rács, folyadék (publikált numerika, 2011) | 0,5307 |
| legjobb szerkezetes szilárd jelölt (publikált, 2007) | 0,5335 |
| befagyott fedés (plafon; a darabon számolva is) | 0,5625 |
| négyzetrács-kontroll (pontos) | 0,3991 |

- A sáv tartott; a darabok méretben monoton tartanak a publikált végtelen-rács érték felé; a 12-es darab értéke (−0,4537 objektumonként) egyezik a publikált egzakt számolással (−0,453).
- A befagyott fedés a darabon pontosan 9/16-ot fizet (gépezet-ellenőrzés), és a motor tényleg kimozdítja: szórása nem nulla; az alapállapot súlyából egyetlen fedés csak 12%-ot ad — egyik fedés sem ural.
- Az eldöntetlen választás felskálázódik: a legalsó hármas-állapot alatt 7, ill. 14 szingulett ül (12, ill. 18 objektumnál); a fizika 36 objektumnál körülbelül kétszázat számol.
- A korrelációk gyorsan halnak (0,23 → 0,05 → 0,007): a rendszer nem rendeződik.
- A kontroll nem üres: a négyzetrács a padló *alá* megy (nincs háromszög-adó), korrelációi nem halnak (0,35 → 0,18, váltakozó előjellel — rendeződik), és szingulett-tömege nincs. A folyadék nem a súlyozás általános ajándéka, hanem a frusztrált geometria kényszere.

**Ellenőrzés a valóságon.** A végtelen-rács érték a fizika mérföldkő-numerikája (DMRG, [Yan–Huse–White, 2011](../../appendix/C-benchmarks_hu.md)); a szingulett-tömeg a publikált egzakt számolások visszatérő lelete (Waldtmann és társai, 1998; Läuchli és társai, 2011); a Kagome-anyag (herbertsmithite) a legalacsonyabb mért hőmérsékletig nem fagy be, és tört gerjesztések folytonos színképét mutatja (Han és társai, 2012).

**Egy becsületességi szám.** A fizika komoly szilárd jelöltje nem a befagyott karikatúra, hanem maga is önforgó, csak mintázatba rendeződött fedés-keverék — a 4. törvény ítélete ellene már nem érv. Az is a sávban ül (0,5335), és a folyadék kötésenként mindössze 0,003-mal veri. A nyelv gyors érve tehát a karikatúrát zárja ki és a sávot adja; a szerkezetes szilárd és a folyadék közti döntés numerikus munka volt, és a különbség kicsisége mutatja, miért tartott évtizedekig.

**Import-számla:** egy tétel — a Kagome-szomszédság, a helyiség-import geometriai folytatása. **Mit igazolt:** a sáv-tételt (padló a II/5-ből, plafon a nézet-árazásból); a folyadék-kontra-befagyott döntés a nyelvben tétel. A „melyik folyadék" nyitva: [III. rész](../../III-frontier/III-02-open-questions_hu.md).