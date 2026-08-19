---
id: II-08
type: proof
lang: hu
pair: proof_en.md
pair_status: in-sync
doc_version: "1.3"
status: ervenyes
builds_on: [II-07, II-04, I-06]
imports: "nulla új tétel (a taszítási alak a vonzás-import előjelváltott mása)"
---

# II/8. A kizárás és a taszítás versenye

**A kérdés.** A [II/7](../II-07-bowl-magic-numbers/proof_hu.md) a példányokat egymástól függetlenül töltötte; a példányok egymás közti szerződése — a taszítás — itt lép be. Ez az első rendszer, ahol két szerződés versenyez: a kizárás rendet szab, a taszítás költséget.

**A rendszer és a szerződés.** A II/7 tála; plusz minden példánypár büntetése a távolságukkal fordítottan arányos. Új import nincs: az alak a [II/4](../II-04-hydrogen-atom/proof_hu.md) vonzás-importjának előjelváltott mása.

**A tétel, a nyelv szavaival.** Párhuzamos belső mezőknél a közös helymintázat az [5. törvény](../../I-language/I-06-identity_hu.md) miatt kötelezően előjelváltó — súlya az egybeeső helyeken nulla, a két példány sosem áll egy helyen, a taszítási számla kisebb: a párhuzamos beállás kedvezményt kap ([I/6, kicserélődési kedvezmény](../../I-language/I-06-identity_hu.md)).

**A számolás.** A rács-mintázatokon a taszítási büntetések páronkénti integráljai kiszámolva (pontossági ellenőrzés: a legalsó mintázat önmagával vett taszítása analitikusan $\sqrt{\pi/2} \approx 1{,}2533$; a rácson 1,246 — 0,6%); majd a fokon belüli összes elrendezés egzakt versenye, teljes kereséssel. A fokok közti keveredést a számolás elhanyagolja — érvényes, amíg a taszítás nem erősebb a fokköznél. A jósolt mennyiség a betöltési díj ugrása.

**Az eredmény** (a taszítás erőssége a fokköz fele; díjugrás fokköz-egységben):

| N | 2 | 4 | 6 | 9 | 12 | a többi N |
|---|---|---|---|---|---|---|
| díjugrás | 1,16 | 0,55 | 1,01 | 0,43 | 0,84 | 0,27–0,32 |

Főcsúcsok 2, 6, 12-nél (fokzárások, csökkenő sorban); mellékcsúcsok 4-nél és 9-nél — a félig telt fokok, tisztán a kicserélődési kedvezményből. A minimumok sokszorossága kirajzolja a beállási menetrendet: a 4-elektronos minimum háromszoros (két párhuzamos mező), a 9-es négyszeres; a teljes sor N = 1-től 12-ig: 2, 1, 4, 3, 4, 1, 2, 3, 4, 3, 2, 1. Kétszer erősebb taszításnál a csúcshelyek változatlanok, csak az arányok tolódnak. **Kontroll:** osztozó típussal a verseny el sem kezdődik — minden példány a legalsó mintázatba ül, a díjugrás egyenletes, csúcs nincs. A bűvös számok a kizárás ujjlenyomata.

**Ellenőrzés a valóságon.** [Tarucha és társai (1996)](../../appendix/C-benchmarks_hu.md) mérése pontosan ez: főcsúcsok 2, 6, 12-nél csökkenő sorban, mellékcsúcsok 4-nél és 9-nél — és a mellékcsúcsokat ott is a párhuzamos beállás magyarázza (a cikk címében szereplő „spin-effektusok").

**Import-számla:** nulla új tétel. **Mit igazolt:** a kicserélődési kedvezmény tételét mért számokon — és megnyitotta a kötés-szerződés levezethetőségét ([III/1](../../III-frontier/III-01-candidate-laws_hu.md)): két szomszédos gödörben ugyanez a mechanizmus ellenkező előjellel dolgozik (az ellentétes beállás nyer, mert csak az engedi a példányokat a simasági szerződésen át egymás gödrébe belógni), ami alakra a [II/1](../II-01-pair-bond/proof_hu.md) szerep-tiltó szerződése.