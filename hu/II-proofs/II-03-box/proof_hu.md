---
id: II-03
type: proof
lang: hu
pair: proof_en.md
pair_status: missing
doc_version: "1.3"
status: ervenyes
builds_on: [I-05, II-01]
imports: "egy tétel: szomszédság (a II/6 helyiséggé szűkíti)"
---

# II/3. A doboz — kvantáltság kötöttségből

**A kérdés.** A diszkrét értékkészlet nem a típusba írt tulajdonság, hanem a kötöttség következménye — ez itt válik ígéretből számolt tétellé.

**A rendszer és a szerződés.** Egyetlen objektum, sok lehetséges hellyel egy sorban. Két elvárás: a **fal** (a dobozon kívüli helyek büntetése) és a **simasági** szerződés (büntetés a szomszédos helyek súlykülönbségének négyzetére — alakra ugyanolyan tag, mint a [II/1](../II-01-pair-bond/proof_hu.md) $(b + c)^2$-e).

**A számolás.** A helyek rekeszekre osztva; a szerződés mátrixa a rekeszek terén felírva; az önforgó mintázatok (amiket a motor önmagukba forgat) és költségeik a mátrix sajátfeladataként számolódnak. Kötött rendszerben ilyen mintázatból csak megszámlálhatóan sok fér el.

**Az eredmény.** Az önforgó mintázatok a falaknál eltűnő állóhullámok; a költséglétrájuk aránya finom felosztásnál **1 : 4 : 9 : 16**. Ráadás: durva rekeszfelosztásnál az arányok eltérnek (1 : 3,98 : 8,87 : …) — és ez nem hiba, hanem külön jóslat (lásd ellenőrzés).

**Ellenőrzés a valóságon.** A folytonos létrát félvezető kvantumgödrökben közvetlenül mérik. A durva-felosztású, eltérő létrát a fizika kristályrácsokban méri — a nyelv kéretlenül a rácsos változat mért viselkedését is visszaadta.

**Import-számla:** egy tétel — a **szomszédság** (a helyek sorba rendezése, a „mellette" viszony). A [II/6](../II-06-universality/proof_hu.md) ezt később helyiséggé szűkíti. **Mit igazolt:** a [4. törvény](../../I-language/I-05-contract_hu.md) 2. következményét (diszkrét ütemek kötöttségből).