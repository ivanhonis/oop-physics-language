---
id: II-15
type: proof
lang: hu
pair: proof_en.md
pair_status: outdated
doc_version: "1.4"
status: reszleges
builds_on: [II-14, II-13, II-12, II-11, I-06]
imports: nulla
packages: [PKG-15-1, PKG-15-2, PKG-15-3, PKG-15-4, PKG-15-5, PKG-15-6, PKG-15-7, PKG-15-8, PKG-15-9, PKG-15-10]
---

# II/15. A negyedik fok — az ítélet: részleges („a negyedik fok áll, a tető a háromé")

**Egy mondatban.** Nyolcas koordináción a kiterjedés-lépcső felmegy négyig — a négykiterjedésű szövés nyeri a mezőny legnagyobb, középső sűrűségsávját, benne a fél-töltéssel, és győztese belülről is négykiterjedésűnek olvassa magát —, de a lépcső a tetején visszafordul: a legsűrűbb tartomány a téré.

## A kérdés és a rendszer

A [II/14](../II-14-dimension-staircase/proof_hu.md) után a kérdés: folytatódik-e a lépcső — azonos helyenkénti szerződésszám (nyolc) mellett van-e sáv, ahol a négykiterjedésű szövés veri a teret, a síkot és a vonalat. A rögzített rendszer ([PKG-15-1](PKG-15-1-rulebook_hu.md)): 20736 hely, 82944 egységnyi simasági szerződés, helyenként pontosan nyolc; a mezőny a négy természetes jelölt — vonal (1-2-3-4 lépésű kör), sík (király-szövés), tér (BCC-szövés, a saját bázisában építve), négykiterjedés (hiperkocka) —, négy kontroll, és a vonal-család mind a 495 négyes-bekötése 12-es lépés-plafonig. A honos fok eltolódása kimondva: nyolcas koordináción a csupasz egységlépéses bekötés a négykiterjedésé (8 = 2·4), ahogy hatoson a téré volt. A szabálykönyv minden számolás előtt rögzült; három utólagos helyesbítés a csomagokban áll (a §5 séta-táblájának J2-sora; a páros-körbeérés hatóköre; az elsődleges számolási út hosszú-lebegőssé tétele — [PKG-15-2](PKG-15-2-ladders_hu.md), [PKG-15-3](PKG-15-3-race_hu.md)).

## Az eredmény — a verseny

A sávszerkezet teljes és folt-mentes ([PKG-15-3](PKG-15-3-race_hu.md)): **vonal 2–4217, sík 4218–7964, négykiterjedés 7965–15996, tér 15997–20734**; N = 20735-nél egzakt tér–négykiterjedés holtverseny, a teli töltésnél kötelező döntetlen. A négykiterjedés sávja a legnagyobb mind közül, és a fél-töltés benne ül — a negyedik fok tehát áll. De a sorrend nem monoton: a tető a háromé. A mechanizmus a tükör-logikából olvasható: a teli vég a ritka vég tükörképe — ott a betöltetlen ütemek (a lyukak) versenyeznek a tükrözött létrán, és ritkán az alacsonyabb kiterjedés az olcsóbb; az N = 20735-ös egzakt holtverseny (egyetlen lyuknál mindkét páros jelölt a 16-os csúcs-ütemét adja fel) ennek a pecsétje. A három regisztrált kérdés válasza: a héj-illeszkedés nem áll élesen (a sávhatárok a legközelebbi zárt foktól 2, 3, illetve 112 töltésre esnek — a sávhatár a költséggörbék metszéspontja, nem polc-határ); a tükör-szabály az eddigi legélesebb alakban megerősítve — **a felső felet kizárólag a tükör-jegyű pár nyeri**, minden egyes felső töltés az övék —, de a páron belül nem a szélesség dönt (az azonos: 16 = 16), hanem a létra alakja, és a tetőn a sorrend fordul; az alsó fésű-minta a II/14 maradékosztály-rendje szerint áll.

## Az eredmény — a kiolvasás

A hurok a negyedik fok győztesén zárul ([PKG-15-4](PKG-15-4-readout_hu.md)): N = 11075 zárt fokon (a rés fölötte egzaktul 2 − √3) a vak visszarakó ugrása pontosan a nyolc egységlépést jelöli ki (5,7-szeres), az őrszem 5,37 a kettes küszöb fölött, a teljesség-számla **82944/82944, nulla fantom, nulla hiányzó**, a golyó pedig az érvényességi tartomány végéig **egzaktul köbös: 1, 9, 41, 129, 321, 681**. A kiterjedésszám így kívülről (verseny) és belülről (golyó) ugyanaz: négy. Az átellenes visszhang jelen van (+17,4%, ezúttal pozitív előjellel), de a kritikus zónán kívül — a méret-döntés, amely a [PKG-14-5](../II-14-dimension-staircase/PKG-14-5-readout-repeat_hu.md) 12-es támpontjára épült, igazolódott. A kétutas pecsét: a vetítő zárt és gépi útja 1,7·10⁻¹⁵-ön belül egyezik.

## A mezőny-lelet

A teljes 503-as mezőnyben a fő négyes **egyetlen töltést sem nyer szigorúan**: minden töltésen a vonal-család egy hangolt tagja a legolcsóbb vagy holtversenyben áll (a legtöbbet nyerő imitátorok: (3, 5, 6, 10), (3, 7, 8, 9), (1, 3, 5, 7)). A II/14 mezőny-lelete tehát megismétlődik és élesedik: a kiválasztás szabad, kézzel felsorolt hálók közt nem dől el — a gyökér-jelzés ([III/2, 7.](../../III-frontier/III-02-open-questions_hu.md)) súlya nő.

## Mit igazolt, és mit nem

Igazolta: a negyedik fok **létezik** — a lépcső nem áll meg a háromnál, és a negyedik fok győztese belülről is annak olvassa magát; a tükör-szabály élesített alakját ([III/1, 7.](../../III-frontier/III-01-candidate-laws_hu.md)); és új törvényt szült: a tető-fordulás tükör-fele a próba zárása után tétellé emelkedett ([PKG-15-5](PKG-15-5-hole-mirror_hu.md); [III/1, 8.](../../III-frontier/III-01-candidate-laws_hu.md)) — a mért 20735-ös holtverseny és a 16-os csúcs-ütem levezetett ténnyé vált; az irány-tétel ([PKG-15-6](PKG-15-6-direction_hu.md)) és a belőle összerakott tető-tétel ([PKG-15-7](PKG-15-7-top_hu.md)) pedig a fordulást a tető legfelső szakaszán (18649-től) is tételi lábra állította. Amit nem igazolt, őszintén: a „miért három" változatlanul nincs levezetve — az 1/r-vonzás-import érintetlen; a lelet a rögzített négyesen és ezen a méreten áll, a koordináció-függés nyitott; és a sűrűség-kérdés átfogalmazódott, nem megoldódott: ha a lépcső a tetőn visszafordul, a „három" a tető olvasata — ez regisztrált kérdés, nem állítás.

## Bővítési irány

Három út nyílik: a tető-fordulás mindkét fele tételi lábon (PKG-15-5, PKG-15-6, PKG-15-7) — nyitva a dominancia-hézag kérdése (a mért sáv köztes része); a koordináció-pásztázás (10-es koordináción a honos fok az öt — fordul-e ott is a tető, és hol); és a kiválasztás gyökere — a verseny ott dől el, ahol a szerződések születnek ([III/2, 7.](../../III-frontier/III-02-open-questions_hu.md)).
