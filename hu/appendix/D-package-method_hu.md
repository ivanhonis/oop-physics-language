---
id: APP-D
type: appendix
lang: hu
pair: D-package-method_en.md
pair_status: needs-update
doc_version: "1.4"
status: ervenyes
---

# D) A csomag-nyomvonal

A csomag-módszer elve a nyelv saját módszertani szabálya: [I/1](../I-language/I-01-concept_hu.md); a technikai leképezése (csomag-sablon, kapu-szabály, branch- és PR-rend) a [szabálykönyvben](../../CONTRIBUTING.md) áll. Ez a fájl a lefutott csomagsorozatok **nyomvonalát** őrzi: próbánként egy szakasz, csomagonként egy sor — mi volt a csomag dolga, és mi lett a hozadéka. Új próba nyomvonala mindig új szakaszként kerül a végére. A nyomvonal a II/13-nál kezdődik, mert a csomag-módszer ott lépett életbe; a korábbi tizenkét próba a szabályrend kialakulása előtt készült, nyomvonaluk nincs.

## A II/13 nyomvonala

A [II/13 — kiterjedés-verseny](../II-proofs/II-13-dimension-race/proof_hu.md) négy csomagból épült:

- **[PKG-13-1 — szabálykönyv](../II-proofs/II-13-dimension-race/PKG-13-1-rulebook_hu.md):** a jelöltek, az ítélet-szabály és a kiolvasási jegyzőkönyv minden számolás előtt rögzítve; hozadéka az összeesési lemma (a négykiterjedésű jelölt 16 helyen azonos a síkkal).
- **[PKG-13-2 — ütem-létrák](../II-proofs/II-13-dimension-race/PKG-13-2-ladders_hu.md):** minden létra két független úton; hozadéka a második darabolt szövés felfedezése és a 7 létra-osztály.
- **[PKG-13-3 — a betöltési verseny](../II-proofs/II-13-dimension-race/PKG-13-3-race_hu.md):** a győztes-tábla és a kettős ítélet; hozadéka a héj-logika és a tükör-hatás.
- **[PKG-13-4 — a kiolvasás](../II-proofs/II-13-dimension-race/PKG-13-4-readout_hu.md):** a hurok zárása a győztesen; hozadéka a részleges bukás pontos oka (körbeérési rezonancia) és a méret-diagnózis ($+4r$ golyótörvény a 8×8-as szövésen).

## A II/14 nyomvonala

A [II/14 — kiterjedés-lépcső](../II-proofs/II-14-dimension-staircase/proof_hu.md) öt csomagból épült; a szabálykönyv rögzítése *előtt* egy előkészítő javítás történt (a III/2, 8. tér-golyótörvénye lineárisról négyzetesre — a jegyzőkönyv erre épül):

- **[PKG-14-1 — szabálykönyv](../II-proofs/II-14-dimension-staircase/PKG-14-1-rulebook_hu.md):** a hatos koordinációjú vonal–sík–tér mezőny, a kétsávos lépcső-ítélet és a golyó-jegyzőkönyv rögzítve; hozadéka a páros-jegy mint különbözőség-bizonyíték (a II/13-as összeesési csapda kizárva) és a rendre épülő golyó-olvasat (állandó/lineáris/négyzetes).
- **[PKG-14-2 — ütem-létrák](../II-proofs/II-14-dimension-staircase/PKG-14-2-ladders_hu.md):** mind a 224 háló két független úton; hozadéka a pásztázás fogása (20 széteső családtag — a szabálykönyv egy levezetési tévedésének helyesbítése) és a tér 25 polcos, egzaktul szimmetrikus létrája.
- **[PKG-14-3 — a betöltési verseny](../II-proofs/II-14-dimension-staircase/PKG-14-3-race_hu.md):** a teljes lépcső-ítélet (vonal 2–129, sík 130–255, tér 256–511); hozadéka a fél-töltési átvétel és a tükör-mechanizmus, valamint a mezőny-lelet (a kiterjedés-előny vékony és vonal-imitálható).
- **[PKG-14-4 — a kiolvasás](../II-proofs/II-14-dimension-staircase/PKG-14-4-readout_hu.md):** a hurok zárása a győztesen; hozadéka a részleges bukás új oka (átellenes tükör-visszhang — a páros-jegy kis-méretű ára), két szabály-tanulság (szűk őrszem; előjel-hézag) és a méret-diagnózis (egzakt $4r^2+2$ a 12×12×12-es szövésen).
- **[PKG-14-5 — az újrakiolvasás](../II-proofs/II-14-dimension-staircase/PKG-14-5-readout-repeat_hu.md):** a méret-diagnózis rögzített hatókörű ismétlése a 12-es szövésen; hozadéka: a méret-műtermék jelöltből tétel, a visszhang számmá vált (16%, előjeles), és a javított jegyzőkönyv (előjeles ugrás, sáv-őrszem) bevizsgált alakot kapott.

## II/15 — A negyedik fok

- **[PKG-15-1 — szabálykönyv](../II-proofs/II-15-dimension-fourth-rung/PKG-15-1-rulebook_hu.md):** a rögzített rendszer (20736 hely, nyolcas koordináció), a háromfokú lépcső-ítélet és a bevizsgált kiolvasási jegyzőkönyv; hozadéka a különbözőség elvi, három-jegyes bizonyítása és a honos-fok eltolódás kimondása (8 = 2·4).
- **[PKG-15-2 — ütem-létrák](../II-proofs/II-15-dimension-fourth-rung/PKG-15-2-ladders_hu.md):** mind az 503 háló zárt úton, 32 cél két úton (legnagyobb eltérés 1,3·10⁻¹²); hozadéka két helyesbítés (a §5 séta-táblájának J2-sora; a páros-körbeérés hatóköre) és a tiszta osztály-lelet (502 osztály, rejtett egybeesés nélkül).
- **[PKG-15-3 — a verseny](../II-proofs/II-15-dimension-fourth-rung/PKG-15-3-race_hu.md):** a teljes sávszerkezet (vonal 2–4217, sík 4218–7964, négykiterjedés 7965–15996, tér 15997–20734); hozadéka a tető-fordulás lelete, a tükör-szabály élesített megerősítése és a mezőny-lelet élesedése (nulla szigorú győzelem a négyesnek).
- **[PKG-15-4 — a kiolvasás](../II-proofs/II-15-dimension-fourth-rung/PKG-15-4-readout_hu.md):** a hurok zárása a négykiterjedésű győztesen (N = 11075); hozadéka az egzakt köbös golyó r = 5-ig, az ártalmatlan visszhang számsora (+17,4%) és az 1,7·10⁻¹⁵-ös kétutas pecsét.
- **[PKG-15-5 — a lyuk-tükör tétel](../II-proofs/II-15-dimension-fourth-rung/PKG-15-5-hole-mirror_hu.md):** a tető-fordulás tükör-felének négy-lépéses levezetése nulla importtal; hozadéka: a 20735-ös holtverseny és a 16-os csúcs-ütem tételből, a felső sávhatár (15997) mint a ritka-végi átbillenés (4740) tükörképe, és a negatív kontroll (nem-páros páron az azonosság nem áll).
- **[PKG-15-6 — az irány-tétel](../II-proofs/II-15-dimension-fourth-rung/PKG-15-6-direction_hu.md):** a ritka szakasz iránya tétellé emelve mind a hat páron (rendezési + átfordítási + szendvics-lemma, két tétel-erejű réteggel); hozadéka a teljes páronkénti átbillenés-tábla és a dominancia-hézag lelete (az ütemenkénti feltétel az átbillenés 43–62%-áig tart, párfüggetlenül).
- **[PKG-15-7 — a tető-tétel](../II-proofs/II-15-dimension-fourth-rung/PKG-15-7-top_hu.md):** az irány-tétel és a lyuk-tükör összefűzése új bizonyítás nélkül: „a tetőn a három veri a négyet" a 18649..20734 szakaszon levezetett tény (szigorúsági tartalék 0,2072); a mért tér-sáv kétrétegű olvasatot kapott.

- **[PKG-15-8 — a teljes mezőny teteje](../II-proofs/II-15-dimension-fourth-rung/PKG-15-8-top-full-field_hu.md):** a tető-törvény mért felének hiányzó harmadik támpontja, előre lepecsételt és commitolt vak jóslattal (JOS-01); hozadéka: a teli véget mind a 2000 töltésen az (1, 3, 5, 7) tükör-jegyű vonal-tag viszi, és a fő négyes ott egyetlen töltést sem nyer.
- **[PKG-15-9 — a hordozó-tétel és az egységes mezőny](../II-proofs/II-15-dimension-fourth-rung/PKG-15-9-uniform-field_hu.md):** levezetve, mitől tükör-jegyű egy szövés, és ellenőrzött kísérlettel megmérve, mennyit hordoz ebből a kézi jelölt-választás; hozadéka: a tető-fordulás **egyetlen lépésen** múlik (testátló kontra lapátló), és a „3, 3, 5” minta konvenció-műtermék.
- **[PKG-15-10 — a teli-vég tétel](../II-proofs/II-15-dimension-fourth-rung/PKG-15-10-dense-end_hu.md):** a tető-törvény hordozó-fele mérésből tétellé; hozadéka a kiegészítési azonosság, az egy-lyuk tétel (a PKG-15-5 mért holtversenye levezetve), a lyuk-tükör tétel egysoros alakja, és a tanúsított szakaszok.

- **[PKG-15-11 — a lyuk-létra](../II-proofs/II-15-dimension-fourth-rung/PKG-15-11-hole-ladder_hu.md):** a teli-vég tétel egyetlen becslése azonosságra cserélve; hozadéka a lyuk-létra (minden induló második, azonos összsúlyú létrája), a tükör-jegy létra-azonosság alakja, és a tanúsított szakaszok élesítése (a régi becslés 4500–9000 töltést adott fel).

## II/16 — Tízes koordináció: a tető törvénye

- **[PKG-16-1 — szabálykönyv](../II-proofs/II-16-coordination-ten/PKG-16-1-rulebook_hu.md):** a kiválasztási szabály (kimondott konvenció), a négyfokú ítélet a néven nevezett visszafordulás-esettel, a kétutas szabály négyelemű ritka alakja; hozadéka a párosság-lelet (a tükör-jegy egyedül a honosé) és a döntő-kísérletté élesített tető-kérdés.
- **[PKG-16-2 — ütem-létrák](../II-proofs/II-16-coordination-ten/PKG-16-2-ladders_hu.md):** 805 induló áramoltatva, 804 osztály; hozadéka a maradék-próba képlet-hibájának elfogása a négyelemű forma redundanciájával (12,8 → 5,3·10⁻¹⁴).
- **[PKG-16-3 — a verseny](../II-proofs/II-16-coordination-ten/PKG-16-3-race_hu.md):** a sávszerkezet (vonal, sík, négykiterjedés, ötkiterjedés — a három kimarad); hozadéka a két néven nevezett lelet és az egyesített tető-törvény jelölt-szövege.
- **[PKG-16-4 — a kiolvasás](../II-proofs/II-16-coordination-ten/PKG-16-4-readout_hu.md):** a honos győztes kívül-belül öt (egzakt negyedrendű golyó); hozadéka a háromelemű visszhang-számsor és a bevizsgált mintavételes vetítő-pecsét.
- **[PKG-16-5 — tétel-átvitel](../II-proofs/II-16-coordination-ten/PKG-16-5-transfer_hu.md):** a lyuk-tükör változatlan szöveggel tízesen; hozadéka a tető-törvény tételi fele a páros készleten, és a mezőny-pecsét (a teli vég 2000 töltéséből 1999 a páros vonal-tagé).
