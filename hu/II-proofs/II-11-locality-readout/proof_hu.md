---
id: II-11
type: proof
lang: hu
pair: proof_en.md
pair_status: missing
doc_version: "1.3"
status: ervenyes
builds_on: [II-01, II-06, I-04, I-06]
imports: "nulla új tétel; a helyiség-import fele tétellé válik, maradéka a kiválasztás (III/2, 2.)"
---

# II/11. A helyiség-visszaolvasás — a tér mint nézet

**A kérdés.** A nyelv egyetlen megmaradt szerkezeti importja a helyiség: hogy a helyeknek szomszédjuk van, és a keverés csak köztük folyik ([II/6](../II-06-universality/proof_hu.md), [III/2](../../III-frontier/III-02-open-questions_hu.md)). A kérdés megfordítható: tárolt adat-e a szomszédság, vagy a kész állapot nézete? Két állítás próbálandó: geometrikus szerződésháló egyensúlyi állapotából a szomszédság a háló és a címkék ismerete nélkül visszaolvasható; és van címke-független ismertetőjel, amely eldönti, helyi-e egy rendszer — ahol nincs geometria, ott a visszaolvasásnak el kell buknia.

**A rendszer és a szerződés.** Tizenkét objektum körbe zárva, minden élen a [II/1](../II-01-pair-bond/proof_hu.md) kötés-szerződése. Kontroll: ugyanaz a tizenkét objektum, de mindenki mindenkivel kötve (66 él) — szerződés van, geometria nincs. A közelség páronkénti mérőszáma: mennyivel tud többet a két tag közös nézete, mint a két külön nézet együtt. (A fizika ezt kölcsönös információnak hívja.)

**A számolás.** A teljes állapottér pontos minimuma ([B függelék](../../appendix/B-machinery_hu.md), 4. eszköz). A kör alapállapota egyértelmű; a kontrollé 132-szeresen elfajult, ezért ott a nézet a nulla-költségű altér egyenletes keveréke, egzakt vetítővel számolva. A kész állapotból minden párra közelség számolódik; a visszarakó minden objektumot a legközelebbi társaival köti össze — hogy hány ilyen van, azt nem tudja előre, a közelség-térkép kiugrása jelöli ki (itt: kettő, négyszeres ugrással).

**Az eredmény.**

| | kör (12 objektum) | kontroll (mindenki-mindenkivel) |
|---|---|---|
| közelség távolság szerint | 0,444 → 0,123 → 0,066 → 0,045 → 0,037 | mind a 66 pár azonos (0,012; szórás 10⁻¹⁶) |
| visszarakás | 12/12 él helyes; összekevert címkékkel is a kört adja | kitüntetett szomszéd nincs — elbukik, ahogy kell |
| golyónövekedés (r lépésen belüli helyek) | 1, 3, 5, 7, 9, 11 — lépésenként +2: egy kiterjedés | nincs mit mérni |
| blokk-összefonódás (1→6 hely) | 0,69 → 1,18, ellaposodik — a határt követi | 0,69 → 3,89 — a térfogattal nő (maximum 4,16) |
| kötésár | 0,3011 | 0,6818 (egzaktul 45/66) |

Három olvasat. **A szomszédság kiolvasható:** a kész állapot a saját geometriáját hordozza — a szomszédság nézet, nem tárolt adat, és az átnevezés ([5. törvény](../../I-language/I-06-identity_hu.md)) nem tudja elrontani. **Az ismertetőjel címke-független:** helyi rendszerben a kivágott darab összefonódása a darab határával nő, nem a belsejével (felület-törvény); a kontrollon ez mérhetően sérül, és a közelség-térkép tökéletesen lapos. **A kiterjedésszám mérhető:** a golyónövekedés üteméből — itt egy kiterjedés, számolva. Mellékeredmény a kiválasztási kérdéshez ([III/2, 2.](../../III-frontier/III-02-open-questions_hu.md)): a sűrű háló kötésenként 0,68-at fizet a kör 0,30-a ellen — a frusztráció-adó a ritka hálónak kedvez.

**Ellenőrzés a valóságon.** A kör kötésára a publikált egzakt kis-gyűrű értékkel egyezik ($0{,}75 - 0{,}4489 = 0{,}3011$). A felület-törvény helyi szerződések egyensúlyában a fizika sokszorosan ellenőrzött eredménye ([Eisert és társai, 2010](../../appendix/C-benchmarks_hu.md)); az állapotból visszaolvasott geometria a fizikában élő program (Van Raamsdonk, 2010) — a nyelv itt ennek kicsi, egzakt példáját adta.

**Import-számla:** nulla új tétel — és a mérleg másik serpenyője: a helyiség-import fele tétellé vált; ami importként megmarad, az a kiválasztás ([III/2, 2., átfogalmazva](../../III-frontier/III-02-open-questions_hu.md)). **Mit igazolt:** a szomszédság nézet; a helyiség belülről, címkék nélkül mérhető; a kiterjedésszám számolható. A horizont: ha a távolság az összefonódási mintázat kivonata, akkor a [4. törvény](../../I-language/I-05-contract_hu.md) motorja, amely az összefonódást forgatja, kényszerűen a geometriát is forgatja — ez már a III. részé.