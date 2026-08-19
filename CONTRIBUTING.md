---
id: CONTRIBUTING
type: rulebook
lang: multi
doc_version: "1.3"
status: ervenyes
---

# Szerkesztési szabálykönyv · Contribution guide

**[Magyar](#magyar)** · **English:** the research is conducted in Hungarian; this rulebook's English mirror is planned. Until then, the Hungarian text below is the single source of truth.

---

## Magyar

Ez a fájl a repó **technikai** szabályait rögzíti — ember és AI számára egyaránt kötelező, minden nyelvre. A **tartalmi** módszertan (mikor kerülhet be egy állítás a nyelvbe, import-számla, csomag-módszer elve) a nyelv saját szabálya: `hu/I-language/I-01-concept_hu.md`; ott van kimondva, itt nem ismételjük.

### 1. Az alapelv

**Egy állítás — egy címezhető egység.** Minden fejezet, próba és csomag saját fájl, stabil azonosítóval. Az igazság forrása mindig a fejezetfájl; az index-fájlok csak összefoglalnak és linkelnek. **Duplikáció tilos:** ugyanaz az állítás nem élhet két fájlban — a második előfordulás mindig link.

### 2. Számozás — bővítésálló

- Új próba mindig a sor végére kerül (`II-14-...`, `II-15-...`); meglévő azonosító **soha** nem változik és nem használható újra.
- Ugyanez érvényes a törvényekre, jelöltekre, nyitott kérdésekre és csomagokra.
- Ha egy állítás megbukik vagy elavul, a fájl megmarad, a fejléc `status` mezője jelzi — törölni nem szabad.

### 3. Fájlnevek, mappák, nyelvek

- A gyökérben a nyelvfüggetlen kellékek élnek (README, CONTRIBUTING, LICENSE, CITATION, `.github/`, `tools/`, `shared/`); a kutatás **nyelvenként külön fő-mappában** (`hu/`, `en/`, később továbbiak), azonos belső szerkezettel.
- Fájl- és mappanevek: **angolul, kisbetűvel, kötőjellel, ékezet nélkül** (a címekben az ékezet marad).
- Nyelvi utótag a kiterjesztés előtt: `_hu`, `_en` (pl. `proof_hu.md`) — a nyelvmappa mellett is, hogy a fájl önmagában is elárulja a nyelvét, és a nyelvi dump egyértelmű legyen.
- Kód és adat nyelvfüggetlen — **nincs** utótagja, és nem a nyelvmappákban, hanem a `shared/` alatt él, a próbáéval azonos nevű almappában (pl. `shared/II-13-dimension-race/PKG-13-2-ladders.py`).
- Próba-mappa: `<nyelv>/II-proofs/II-NN-short-name/`, benne `proof_<nyelv>.md`; csomag: ugyanott, `PKG-NN-M-short-name_<nyelv>.md`.

### 4. YAML-fejléc — minden md-fájl elején kötelező

```yaml
---
id: II-13              # stabil azonosító (pl. I-04, II-13, PKG-13-2, APP-B)
type: proof            # entry-point | rulebook | chapter | proof | package | index | appendix
lang: hu               # hu | en | multi (csak gyökér-kellékeknél)
pair: proof_en.md      # a másik nyelvű iker fájlneve (a tükör-útvonalon)
pair_status: missing   # missing | in-sync | outdated
doc_version: "1.3"     # melyik egységes kiadással azonos a tartalom
status: ervenyes       # ervenyes | jelolt | reszleges | bukott | elavult
                       # csomagnál: jovahagyva | jovahagyasra-var | elutasitva
builds_on: [II-01, II-12]   # mire épít (id-lista; elhagyható, ha üres)
imports: nulla         # csak proof-nál: az import-számla géppel olvasható kivonata
part_of: II-13         # csak csomagnál: melyik próbához tartozik
packages: [PKG-13-1]   # csak proof-nál, ha csomagokból épült: a nyomvonal id-listája
---
```

- **A `pair_status` szabálya:** a mező azt mondja meg, hogy **a párom naprakész-e hozzám képest**. Ha egy `_hu` fájl tartalma változik, a szerkesztő ugyanabban a módosításban átállítja a saját `pair_status`-át `outdated`-re; a fordítás frissítésekor mindkét fájlban `in-sync`-re áll vissza.
- **A `status` értelmezése proof-nál:** az ítéletet jelöli, nem a fejezet érvényességét — a `bukott` azt mondja, a próbált jelölt bukott meg (a fejezet érvényes bukás-próba), a `reszleges` részleges ítéletet.

### 5. Hivatkozások

- Mindig **relatív út**, mindig **azonos nyelvű** célfájlra: `[II/1](../II-01-pair-bond/proof_hu.md)`. Nyelvmappán belüli hivatkozás sosem lép át másik nyelvmappába.
- A `shared/` alatti kódra a csomagfájl névvel hivatkozik (a kód útvonala a `shared/` tükör-szabályából adódik).
- Szövegközi azonosító-hivatkozás (pl. „a 2. törvény", „III/2, 7.") mellé első előfordulásnál link jár.
- Fájlon belüli szakaszra horgonnyal: `proof_hu.md#az-eredmeny`.

### 6. Képletek — LaTeX Markdownban

- Soron belül: `$a^2 + b^2 = 1$`. Kiemelt képlet `$$ ... $$` blokkban, **előtte és utána üres sorral** (GitHub-követelmény).
- Csak standard LaTeX-parancsok, saját makró nélkül. A matematikán belül nincs Unicode-jel (`\psi`, nem ψ); prózában és táblázatcellában a Unicode maradhat.
- A matematikán belüli tizedesvessző `{,}` csoportosítással írandó (pl. `$\sqrt{0{,}8}$`, `$\approx 1{,}2533$`), hogy ne felsorolás-vesszőként értelmeződjön; a prózai számokban sima vessző áll.
- Prózában nyers `$` jel nem szerepelhet.
- Hivatkozott képlet azonosítót kap a blokkon belül `\tag`-gel: `\tag{K-II1-1}` — alakja `K-<fejezet>-<sorszám>`; a fejezeten belül a sorszám folytonos.

### 7. A csomag-munkamenet és a kapu-szabály (GitHub-leképezés)

- **Egy csomag = egy branch + egy pull request.** Branch-név: `pkg/13-2-ladders`; egyéb munkára `fix/...`, `translate/...`.
- A csomagfájl kötelező szerkezete: **Kérdés — Bemenetek — Levezetés/számolás — Ítélet (+ import-számla) — Kimenő állítások.** A szabálykönyv-csomag (PKG-NN-1) minden számolás előtt rögzül.
- **A kapu:** a PR-sablon ellenőrzőlistája (`.github/PULL_REQUEST_TEMPLATE.md`). A merge = jóváhagyás; a következő csomag csak a beolvasztott előzőre építhet, és csak annak **Kimenő állításait** használhatja.
- Elutasított csomag is megmarad (`status: elutasitva`) — a nyomvonal része.

### 8. Nyelvek

- **A kutatás magyar nyelven folyik**; az első eredmények magyarul jelennek meg. A párhuzamos nyelvi tükröket igyekszünk naprakészen tartani — a lemaradást a `pair_status` mezők teszik láthatóvá és géppel listázhatóvá.
- A nyelvi pár mindig a **tükör-útvonalon** él: `hu/X/…_hu.md` ↔ `en/X/…_en.md` — azonos `id`-vel, azonos belső szerkezettel.
- Fordítás előtt a terminológiát a szótár-fejezet (`I-10-dictionary`) angol oszlopa rögzíti — minden fordítás onnan dolgozik.
- Kód, számadat, táblázat-szám nem fordul; csak próza és címke.

### 9. Kiadás

- A nyelvi dumpot a `tools/assemble.py` állítja elő (a nyelvet bekéri, Enter = hu): a fa minden, az adott nyelvű fájlját `<file path="...">` tagek közé fűzi, elöl teljes fájllistával; a nem tudományos fájlokat a szkript elejei kihagyási lista szűri.
- Kiadás = git tag (`v1.3`) + release, mellékletként a dump.
- A `hu/CHANGELOG_hu.md` minden kiadásnál új bejegyzést kap; a fejlécek `doc_version` mezője a kiadással együtt lép.

### 10. Ellenőrzőlista módosítás előtt (kézzel vagy szkripttel)

- [ ] Minden érintett fájl fejléce kitöltött és érvényes értékű
- [ ] Számozás nem mozdult; új elem a sor végén
- [ ] Nincs duplikált állítás; az indexek csak linkelnek
- [ ] Linkek feloldódnak, azonos nyelvre mutatnak
- [ ] `$$` blokkok üres sorral határoltak; prózában nincs nyers `$`
- [ ] Proof-fájl import-számlával zárul; a fejléc `imports` mezője egyezik vele
- [ ] Változott `_hu` tartalomnál a `pair_status` átállítva
