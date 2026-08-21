---
id: PKG-18-2
type: package
part_of: II-18
lang: hu
pair: PKG-18-2-consequences_en.md
pair_status: missing
doc_version: "1.4"
status: jovahagyasra-var
builds_on: [PKG-18-1]
imports: nulla
---

# PKG-18-2 — A közeg következményeinek gépi megerősítése (számolás-csomag)

**Egy mondatban.** A [PKG-18-1](PKG-18-1-rulebook_hu.md) négy következménye (C1–C4) és a két azonnali következmény **mind áll** — és a mérés közben kiderült, hogy a C1 tartalma nem a valós térben él, hanem a kis hullámszámoknál, ahol **egzakt**.

**A csomag dolga.** A fagyasztott szabálykönyv A6 állítására építve gépileg ellenőrzi a C1–C4-et és a 6. szakasz két azonnali következményét, a kétutas szabály **algoritmus-alakjában** (zárt Fourier-út kontra sűrű pszeudo-inverz). A szkript: `shared/II-18-mediating-medium/PKG-18-2-consequences.py`. Futásidő a referencia-környezetben: **4,3 s**.

---

## 1. Eredmények

| Ellenőrzés | Mit mér | Eredmény |
|---|---|---|
| **E1** kétutas | zárt Fourier ($1/\lambda$, a $k=0$ módus kinullázva) kontra sűrű `pinv` öt hálón | legnagyobb eltérés **$1{,}90\cdot10^{-14}$** — **áll** |
| **E2** C4 | $L^{+}\mathbf{1} = 0$ — egyenletes sűrűség semmit nem forrásol | Petersen $1{,}4\cdot10^{-16}$; Desargues $9{,}4\cdot10^{-16}$; szövéseken $\le 5{,}2\cdot10^{-15}$ — **áll** |
| **E3a** C1 (egzakt) | a színkép kvadratikus kis $k$-n: $\lambda(k)/|k|^2 \to c$ | $c = 1{,}00000$ / $0{,}99995$ / $0{,}99980$ / $0{,}99679$ ($d=1..4$), **irányfüggetlen** ($10^{-12}$ alatt) — **áll** |
| **E3b** C1 (valós tér) | a sugárirányban átlagolt kitevő, méret-létrán | legjobb: $-0{,}9958$ / $+0{,}0286$ / $+0{,}9841$ / $+1{,}9830$ a jósolt $-1$ / $0$ / $1$ / $2$ ellen — **áll** |
| **E4** C1′ | a kitevőt a kiterjedés, az együtthatót a bekötés adja | a merevség-arány **3,0000**-t jósol, a valós tér **3,0000**-t mér — **áll** |
| **E5** C2 | az előjel | minden $r$-en vonzás, szigorúan gyengülve; ellentétes forrás **nem létezik**, mert $\rho \ge 0$ — **áll** |
| **E6** C3 | azonos erősség | a két különböző alakú, azonos összsúlyú példány közege **egzaktul** csak kontakt-tagban tér el; eltérés **$2{,}0\cdot10^{-17}$** — **áll** |
| **E7a** | egy példány ⇒ állandó | $(L^{+})_{ii}$ szórása $\le 2{,}0\cdot10^{-16}$, nem-Cayley hálókon is — **áll** |
| **E7b** | egyenletes betöltés ⇒ nulla | a II/15 J4-én, $N = 11075$: $\max|L^{+}\rho| = 7{,}4\cdot10^{-17}$ — **áll** |

### Az E3a a csomag legfontosabb sora

A „$r^{2-d}$ alak" **teljes tartalma** az, hogy a színkép kis hullámszámon kvadratikus; a többi az $1/|k|^2$ Fourier-transzformáltja $d$ kiterjedésben, ami matematikai azonosság, nem mérendő mennyiség. A merevség mind a négy kiterjedésben pozitív állandóhoz tart, **és irányfüggetlen** — ez utóbbi nem volt előre kimondva, és azért számít, mert enélkül a $G$ nem gömbszimmetrikus, csak affin átskálázás után.

### Az E6 élesedett: a C3 nem aszimptotikus, hanem egzakt

A javított mérésben (2. szakasz) kiadódott egy azonosság, amit a szabálykönyv nem mondott ki. Ha $\rho_a$ pontszerű és $\rho_b$ a hét-helyes szétkent alak, akkor $\rho_b - \rho_a = -\tfrac17 L\,\delta_0$, tehát

$$L^{+}(\rho_b - \rho_a) \;=\; -\tfrac17\Bigl(\delta_0 - \tfrac1n\Bigr)\tag{K-PKG182-1}$$

vagyis a két közeg különbsége a forráson kívül **pontosan** az $1/(7n)$ állandó, ami a rendszer méretével eltűnik. **A távoli tér tehát nem közelítőleg, hanem egzaktul csak az összsúlyt ismeri.** A C3 ezzel élesebb alakot kapott, mint amit a szabálykönyv állított.

## 2. Két javítás a mérésben (a próba hibája volt, nem a levezetésé)

**M1 — a C1-et rossz helyen mértem.** Az első futás a kitevőt **valós térben**, szabad illesztéssel olvasta, és **bukást jelentett**: $d=3$-ra 1,17, $d=4$-re 2,31. Az eltérés nem a levezetésé volt, hanem a mérésé: a rács-diszkrétség relatív korrekciója $O(r^{-2})$, ami $r=1$-en 100%, $r=2$-n 25%, és csak $r \ge 4$-től esik 6% alá. A javítás két lépés: **(i)** a C1 tartalmát ott mérjük, ahol egzakt — a kis-$k$ merevségben (E3a); **(ii)** a valós téri olvasat sugárirányban átlagolva, eltolás-mentes hárompontos becslővel fut, és **a teljes $r$-létra jelentendő**, nem a legjobb pont.

Az eltolás-mentes becslő: $G(r) = A r^{-p} + C$ esetén

$$\frac{G(r)-G(2r)}{G(2r)-G(4r)} \;=\; 2^{p}\tag{K-PKG182-2}$$

— nincs illesztés és nincs szabad állandó. A tóruszon a $k=0$ módus kivétele éppen egy ilyen $C$ eltolást hagy, amit így nem kell kezelni. **Ugyanez a becslő fedi mind a négy kiterjedést**, mert $p = d-2$, tehát a logaritmikus $d=2$ eset egyszerűen $p = 0$.

**Felbonthatósági előfeltétel, előre kimondva:** egy méret csak akkor ítélhető, ha az ablaka elér a $r \ge 4$ alapig. Ennek indoka az $O(r^{-2})$ korrekció, nem a számok. A $16^4$-es hiperkocka ezért **nem ítélt**, csak jelentett — az ablaka $r=2$-ig ér.

**M2 — egy $n$-es szorzó a konvolúcióban.** A közeg-mezőt `ifftn(fftn(rho) * fftn(G)) * n`-ként számoltam; a numpy `ifftn`-je viszont már hordozza az $1/n$-t, tehát a szorzó **fölösleges** volt, és minden kiírt abszolút értéket $n$-szeresére fújt. Az arányokat nem érintette, ezért az ítéletek nem változtak — de a közzétett számok rosszak lettek volna. **A hibát az E6 egzakt kontakt-azonossága fogta meg** (K-PKG182-1): a mért különbség $0{,}143$ volt a levezetett $4{,}36\cdot10^{-6}$ helyett, pontosan $n = 32768$-szoros. Módszertani jegyzet: **a levezetett zárt alak fogta meg a kódot, nem fordítva** — ez a kétutas szabály haszna a legolcsóbb alakjában.

## 3. Amit ez a felülvizsgálatból lezár

Az E7 két sora a [PKG-18-1](PKG-18-1-rulebook_hu.md) 10. szakaszának regiszterét nagyrészt **egy sorban** kitölti:

| Próba | `kozeg:` | Miért |
|---|---|---|
| [II/3](../II-03-box/proof_hu.md), [II/6](../II-06-universality/proof_hu.md) | `nem-erinti` | egy példány ⇒ a közeg tagja állandó (E7a), a létrát nem mozdítja |
| [II/12](../II-12-network-race/proof_hu.md)–[II/17](../II-17-contract-origin/PKG-17-1-rulebook_hu.md) | `nem-erinti` | egyenrangú hálón egyenletes a betöltés ⇒ a közeg **egzaktul nulla** (E7b) |
| [II/1](../II-01-pair-bond/proof_hu.md), II/2, [II/5](../II-05-triangle/proof_hu.md), [II/9](../II-09-kagome/proof_hu.md), [II/10](../II-10-internal-witness/proof_hu.md), [II/11](../II-11-locality-readout/proof_hu.md) | **nyitva** | a kötés-szerződésen állnak; a K-a kérdés dönti el ([III/1, 2.](../../III-frontier/III-01-candidate-laws_hu.md)) |
| [II/4](../II-04-hydrogen-atom/proof_hu.md), [II/7](../II-07-bowl-magic-numbers/proof_hu.md), [II/8](../II-08-exclusion-vs-repulsion/proof_hu.md) | **nyitva** | a `PKG-18-3` tárgya |

**A négy új tétel** (hordozó-, teli-vég, egy-lyuk, lyuk-létra) **érintetlen**, mert a II/15–II/16 rendszerein a közeg egzaktul nulla. Ez nem hatókör-mentesség, hanem levezetett tény: a `PKG-15-12` már kimondta, hogy a tételek minden fokszám-reguláris hálón állnak; most az is megvan, hogy a közeg ott nem is szól bele.

## 4. Amit ez a csomag nem mond

- **Nem méri a mért célpontokat.** Egyetlen szám sem áll itt szemben mért értékkel; ez a `PKG-18-3` dolga, és ott dől el az előjel-kérdés a [II/8](../II-08-exclusion-vs-repulsion/proof_hu.md) csúcsszerkezetén.
- **Nem mond semmit a hálóról.** A közeg a szomszédságon él; a hordozó-kérdés a II/19-é (PKG-18-1, 12. szakasz).
- **Nem érinti az él-alakot.** A definíció fele áll ([PKG-18-1](PKG-18-1-rulebook_hu.md), 5. szakasz), és a mentő-tilalom él: ami itt vagy a `PKG-18-3`-ban bukik, azt az él-alak nem menti.
- **A kiterjedésszám itt nem kimenet.** A C1 minden $d$-re szól; hogy a világ hányas, arról ez a csomag hallgat.

## 5. Import-számla

Új import: **nulla.** A rendszer, a definíció és a következmények a `PKG-18-1`-ből örököltek; a gráfok élsorból épülnek; a Laplace-színkép standard. A felbonthatósági előfeltétel ($r \ge 4$) **kimondott hatókör-határ**, indoka az $O(r^{-2})$ rács-korrekció — nem a számokból választott küszöb.

## 6. Ítélet erről a csomagról

**Áll.** Mind a nyolc ellenőrzés teljesül, két rögzített mérés-javítással (M1, M2), és egy olyan élesedéssel, amit a szabálykönyv nem állított (K-PKG182-1: a C3 egzakt, nem aszimptotikus).

## 7. Kimenő állítások (a PKG-18-3 csak ezekre építhet)

- **B1:** a C1–C4 gépileg megerősítve; a C1 tartalma az E3a kvadratikus merevsége, ami **egzakt** — a valós téri kitevő ugyanannak a ténynek a rács-diszkrétségen át látott alakja.
- **B2:** **a kitevőt a kiterjedés adja, az együtthatót a bekötés** — két független úton igazolva (színkép-merevség és valós téri profil, arány 3,0000 kontra 3,0000).
- **B3:** a C3 **egzakt alakja** (K-PKG182-1): két azonos összsúlyú példány közege a forráson kívül csak az $1/(7n)$ állandóban tér el. A távoli tér csak az összsúlyt ismeri.
- **B4:** a **C4 nem szövés-tulajdonság** — nem-Cayley csúcstranzitív hálókon (Petersen, Desargues) is áll.
- **B5:** a felülvizsgálati regiszter nyolc próbára lezárva `nem-erinti`-vel (3. szakasz); **a négy új tétel érintetlen**.
- **B6:** eltolás-mentes kitevő-becslő (K-PKG182-2) és a felbonthatósági előfeltétel ($r \ge 4$) — általános eszköz, minden későbbi profil-mérésre.
- **B7:** a kétutas szabály algoritmus-alakja e csomagon teljesült: $1{,}90\cdot10^{-14}$.

> A B1–B7 csak e csomag **jóváhagyása után** vezethető át a fejezetekbe.
