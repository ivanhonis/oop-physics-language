---
id: I-07
type: chapter
lang: hu
pair: I-07-measurement_en.md
pair_status: missing
doc_version: "1.3"
status: ervenyes
---

# I/7. A mérés ára és a clone() hiánya

**A mérés mint tag–környezet szerződés.** A kiolvasás nem a nyelven kívüli varázslat, hanem egy szerződés bekapcsolása: a műszer egy környezet, amely a tag értékének tanújává válik — a tanú-szabály ([I/4](I-04-ownership-view_hu.md)) célzottan és teljes erővel fut: a műszer a tag két lehetséges értékéhez két megkülönböztethető saját állapotot rendel, és a tag ágai helyben többé nem interferálnak.

**A kötés felszakad.** A közös birtoklás kizárólagos: egy tag nem lehet egyszerre két kötés teljes értékű része. (A fizika: összefonódás-monogámia.) Amikor a tanú megfogja a tagot, a tag–társ kötés elszakad, és a birtoklási határ átrajzolódik: előtte a pár birtokolt, utána a tag a műszerrel közösködik, a társ kiszabadul — az eredmény ismeretében már önálló, tiszta állapota van.

**A könyvelés.** A [II/1](../II-proofs/II-01-pair-bond/proof_hu.md) szerződésén a kötött minimum költsége 0, a kiolvasás utáni állapotoké ½. A különbséget a műszer fizette be: **kötött rendszeren a getter mellékhatásának minimális díja a kötési energia.** Az első törvény ára ezzel szám — és a fizika méri is: szingulettet szakítani pontosan ennyi energiába kerül.

**Jelezni nem lehet.** A társ kiolvasása a tag feltétel nélküli nézetét nem mozdítja — a tag oldalán semmilyen helyi kiolvasás nem árulja el, hogy a társat megmérték-e. Az összefonódás nem jelzőcsatorna. (A fizika: no-signaling.)

**A véletlen helye.** A nézetek terén a mérés két lépésre esik szét: a **tanúsítás** determinisztikus, súlytartó művelet (a korong peremi pontját a tengelyére vetíti), a véletlen csak a **leolvasásnál** — az egyik ág kiválasztásánál — lép be. Ezzel az [I/3](I-03-operations_hu.md) kerete bezárult: minden művelet állapot→állapot leképezés.

**Egy mechanizmus, két üzemmód.** A lassan, gyengén érintkező hideg környezet elviszi a felesleget és leereszti a rendszert a kötött minimumba; a gyorsan, erősen rögzítő környezet (a műszer) tanúsít és szakít. A kiolvasott véletlen és a befizetett energia ugyanannak a tranzakciónak a két oldala. (Hogy a rendszer a *saját* környezete is lehet — belső tanú —, azt a [II/10](../II-proofs/II-10-internal-witness/proof_hu.md) próbálja; végtelen-alakja a III. részben nyitott.)

**Tétel: a clone() nem létezik.** Nincs olyan művelet, amely egy ismeretlen állapotról tökéletes másolatot készít — ez az első és a harmadik törvény ([I/3](I-03-operations_hu.md)) következménye, két rétegben. *Első réteg — az olvasás útja zárva:* másolni csak azt lehet, amit előbb kiolvastál; az egyetlen olvasás a mérés, ami a súlypárból egyetlen értéket csinál és az eredetit is átírja. *Második réteg — a fejlődés útja is zárva:* egy mérés nélküli, univerzális másolónak a tiszta 0-ból $(0,0)$ párt, a tiszta 1-ből $(1,1)$ párt kellene csinálnia; a súlytartás miatt az $(a, b)$ súlyozásból ekkor kötelezően $a \cdot (0,0) + b \cdot (1,1)$ lesz — nem két független másolat, hanem egy közösen birtokolt pár. **A másolási kísérlet összefonódást gyárt másolat helyett.** És a második réteg „elrontott másolója" nem selejt, hanem pontosan a fenti műszer: értéket másol és összefonódást gyárt — ez maga a tanúsítás. A clone() lehetetlensége és a getter mellékhatása egyetlen tény két olvasata. (A fizika: No-Cloning tétel.)

**Következmény: az átadási szemantika.** Érték szerinti átadás nincs. Két átadásfajta létezik: **referencia-átadás** — az objektum bekapcsolódik egy közös állapotba; ez maga az összefonódás; és **mozgatás (move)** — az állapot átvihető másik hordozóra, de az eredeti kötelezően megsemmisül közben (a fizika: teleportálás, kísérletileg pontosan így működik). A nyelv állapot-modellje tehát a modern nyelvek tulajdonlási modelljére hasonlít — egy állapotnak egy birtokosa van, másolat nincs, csak move —, de itt ez nem tervezési döntés, hanem a törvények kényszerű következménye.
