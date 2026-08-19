---
id: II-02
type: proof
lang: hu
pair: proof_en.md
pair_status: missing
doc_version: "1.3"
status: ervenyes
builds_on: [II-01, I-05]
imports: nulla
---

# II/2. A csere-lengés — a motor próbája

**A kérdés.** A [4. törvény](../../I-language/I-05-contract_hu.md) többet állít a pontozásnál: ugyanaz a szerződés hajtja a fejlődést is. Ez külön próbát követel — elvégezhető ugyanazon a szerződésen, új matematika nélkül.

**A számolás.** Indítsuk a párt a $(0,1)$ állapotból. Ez a szerződés két költségszintjének — a 0 költségű, szerep-mentes minimumnak és az 1 egységnyi költségű szimmetrikus párjának — fele-fele súlyozása. A motor a két összetevő fázisát a költségével arányos ütemben tekeri, ezért a különbségük lüktet: a rendszer a $(0,1)$ és az $(1,0)$ között leng. A lengés frekvenciája kötelezően a két költségszint különbsége osztva a Planck-állandóval; a visszatérés $\cos^2$-görbét követ; a teljes csere ideje $h/(2 \cdot \text{csatolás})$. **Szabad paraméter nincs:** az ütemet ugyanaz a szám adja, amelyet a [II/1](../II-01-pair-bond/proof_hu.md) statikusan már kiszámolt.

**Ellenőrzés a valóságon.** Kettős kvantumpöttybe zárt elektronpárokon ezt közvetlenül mérik ([Petta és társai, 2005](../../appendix/C-benchmarks_hu.md) óta rutinkísérlet): mikroelektronvoltos csatolásnál gigahertzes lengés (4,1 μeV ↔ 1 GHz, mert h ≈ 4,14 μeV/GHz), és a frekvencia a csatolással együtt mozog, ahogy a képlet mondja.

**Import-számla:** nulla. **Mit igazolt:** a 4. törvényt. Egyetlen költségfüggvény bíróként a hidrogénmolekula kötését adta vissza (statika), motorként a spin-csere lengését (dinamika). A nyelv ezzel **zárt**: egy rendszer megadásához elég az objektumok és a szerződések felsorolása — a futás következmény.