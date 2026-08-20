---
id: APP-B
type: appendix
lang: hu
pair: B-machinery_en.md
pair_status: outdated
doc_version: "1.4"
status: ervenyes
---

# B) A számoló gépezet

A II. rész minden száma négy, egymásra épülő eszköz valamelyikéből jön.

(1) **Zárt alakok**: ahol a rendszer kicsi, a minimum kézzel számolható ([II/1](../II-proofs/II-01-pair-bond/proof_hu.md): $L = \tfrac{1}{2} + \tfrac{1}{2}\cos^2(\theta_1 - \theta_2)$; a [II/5](../II-proofs/II-05-triangle/proof_hu.md) példány-szintű ága; a [II/12](../II-proofs/II-12-network-race/proof_hu.md) két tétele; a [II/13](../II-proofs/II-13-dimension-race/proof_hu.md) összeesési lemmája).

(2) **A rácsgépezet**: a helyek rekeszekre osztása, a szerződések mátrixa, önforgó mintázatok és költséglétra sajátfeladatként; a felosztás finomításával a folytonos válasz, durván a rácsos ([II/3](../II-proofs/II-03-box/proof_hu.md), [II/4](../II-proofs/II-04-hydrogen-atom/proof_hu.md), [II/6](../II-proofs/II-06-universality/proof_hu.md), [II/7](../II-proofs/II-07-bowl-magic-numbers/proof_hu.md); a II/12–II/16-ban ugyanez hálózatokon fut: a szerződésháló mátrixa, ütem-létra, alulról töltés).

(3) **A fok-verseny**: kiszámolt páronkénti taszítási integrálok a rács-mintázatokon, majd a fokon belüli összes elrendezés egzakt, teljes keresése ([II/8](../II-proofs/II-08-exclusion-vs-repulsion/proof_hu.md)).

(4) **A teljes állapottér pontos minimuma**: kis darabokon a teljes súlyvektor-tér kezelése kerekítésmentes elvi hibával — sajátfeladat, időfejlesztés, nézet-számítás ([II/5](../II-proofs/II-05-triangle/proof_hu.md), [II/9](../II-proofs/II-09-kagome/proof_hu.md), [II/10](../II-proofs/II-10-internal-witness/proof_hu.md), [II/11](../II-proofs/II-11-locality-readout/proof_hu.md)).

A [II/11](../II-proofs/II-11-locality-readout/proof_hu.md) a gépezetet két elemmel bővítette: a kész állapot páronkénti közelség-térképe és a belőle — címkék nélkül — dolgozó visszarakó; valamint az elfajult nulla-költségű altér egzakt vetítője. A II/13-hoz további kiegészítés: szabad kizáró példányok nézetei a példány-korrelációkból egzaktul számolódnak (a 4. eszköz gyorsított alakja). A II/14-hez: a szövés-létrák zárt Fourier-alakja mint kötelező ellenpróba a gépezet mellett, és az illeszkedési-mátrixos felépítés ($L = B^{\mathsf T} B$) mint független kódút a verseny előfeltétel-ellenőrzéséhez. A II/15-höz: a versenyt hosszú-lebegős úton kell futtatni, mert a teli vég közelében a szokásos gépi pontosság halmozási hibája a rögzített tűrés fölé nő (ez a **H3**; a **H4** ezt visszavonta és hordozható útra cserélte — lásd alább). A II/16-hoz: a mezőny akkorára nőtt, hogy a teljes kétutas ellenőrzés géppel elvégezhetetlen — helyette **ritka, négyelemű alak** áll, amely sorsolt mintákon és kis példányokon fedezi ugyanazt, kimondottan gyengébb erővel, számmal jelentett lefedettséggel; ide tartozik a kiolvasás **mintavételes vetítő-pecsétje** is, a korábbi teljes vetítő helyett.

## A referencia-környezet

A számolások **lokálisan** futnak, egy kimondott referencia-környezetben: Windows 11 Pro, Python 3.12.5, numpy 2.2.4, Intel i9 (8 mag / 16 szál), 128 GB. Az erőforrás nem korlát, ezért a méret-kérdéseket nem a költség dönti el, hanem a hatókör-határok. A környezet **rögzítve van, de nem követelmény**: azért írjuk le, hogy egy harmadik fél a környezeti különbséget meg tudja különböztetni az eredmény-különbségtől. A számolási út (lásd `H4`) platformfüggetlen, ezért más gépen is állnia kell — ha nem áll, az lelet. Az ellenőrzést a `shared/environment-check.py` végzi, a teljes reprodukciós padot a `shared/bench/bench.py`.

## H4 — a hordozható összegzési út (a H3 helyesbítése)

A **H3** (II/15) a teli vég halmozási hibájára úgy válaszolt, hogy az elsődleges számolási utat hosszú-lebegőssé tette. Ez a válasz **platformfüggő**: az `np.longdouble` csak ott a 80 bites kiterjesztett típus, ahol a C-eszközlánc adja (Linux/glibc, gcc vagy clang); Windowson, MSVC alatt a `float64` **álneve**. A referencia-környezetben tehát a H3 útja csendben hatástalan — és ami rosszabb, minden „két úton" próba, amely a két típust veti össze, ilyenkor önmagával hasonlít össze, és **pontosan nulla** eltérést jelent: zöld lámpa, amely semmit nem fedez.

A **H4** a típus-alapú javítást algoritmikusra cseréli. A sodródás nem a lebegőpontos szélességből jött, hanem abból, hogy tízezernyi tagot **sorban** adunk össze. A gyógymód tehát az, hogy nem sorban adjuk össze: a rendezett létrát rövid blokkokra vágjuk, minden blokkot egzaktul összegzünk (`math.fsum`, helyesen kerekített), a blokk-összegeket egzaktul láncoljuk, és rendes lebegőpontos futó összeg csak egy blokkon belül fut. A hiba így a **blokkhosszal** skálázódik, nem $n$-nel.

Mérve a II/15 létráján (20736 ütem, egzakt nyomösszeg 165888), eltérés az egzakt értéktől:

| Út | Eltérés | Az $10^{-8}$ tűrés ellen |
|---|---|---|
| naiv futó összeg, `float64` | $1{,}93\cdot10^{-8}$ | bukik |
| `longdouble` (H3) a referencia-gépen | $1{,}93\cdot10^{-8}$ | bukik — álnév |
| **hordozható út (H4)** | **$0$** | **áll** |

A 32 mentett II/15 létrán a legrosszabb eset a naiv úton $1{,}93\cdot10^{-8}$, a H4 úton $1{,}5\cdot10^{-10}$. Az út a `shared/summation.py`-ban áll, saját önpróbával.

**Hatókör, kimondva.** A H4 az *összegzés* hibáját szünteti meg; a tárolt létra saját pontosságánál pontosabb nem lehet. A mentett gyorsítótár `float64`, ezért a visszaolvasott értékek padlója $\sim10^{-11}$ — a rögzített $10^{-8}$ tűrés alatt bőven, de a 80 bites úton született $10^{-13}$-as közzétett számoknál gyengébben. A közzétett értékek érvényesek; a referencia-környezet a rögzített tűrésen belül adja vissza őket.

**A kétutas szabály új alakja.** A H3 kiürülése megmutatta, hogy a „két út" **két lebegőpontos típusként** való értelmezése törékeny: egyetlen típus-álnév kiüti, méghozzá némán. Ezért a szabály innentől **két algoritmust** jelent — zárt alak kontra gépezet, polcos/kompenzált összegzés kontra blokkos, illeszkedési-mátrixos felépítés kontra közvetlen —, nem két számábrázolást. Az így értett fedezet minden platformon áll, és nem tud csendben elpárologni. A pad a pontosan nulla eltérést jelentő kétutas próbát külön ítélettel (`URES`) fogja meg.

**Átállási állapot.** A II/13 és II/14 csomagjai a referencia-környezetben hiánytalanul reprodukálódnak. A H3 útjára írt csomagok (`PKG-15-3`, `PKG-15-5`, `PKG-15-7`, és a II/16 érintett csomagjai) hat ellenőrzése addig `H4-VAR` státuszú a padon — **hiányzó előfeltétel, nem rossz szám** —, amíg a szkriptek át nem állnak a `shared/summation.py` útjára.

## Beépített pontossági ellenőrzések

A taszítási alapintegrál analitikus értéke ($\sqrt{\pi/2} \approx 1{,}2533$; rácson 1,246, 0,6%); a befagyott fedés analitikus 9/16-ának pontos visszaadása (II/9); a 12 objektumos Kagome-darab egyezése a publikált egzakt értékkel; a 12-es kör kötésárának egyezése a publikált egzakt értékkel, a kontroll-vetítő egzakt nyoma (132) és a kontroll közelség-szórása ($10^{-16}$) (II/11); a II/12 két tételének analitikus fedezete (a kövér-szerződés elrendezés nulla költsége és a teljes-töltési nyomösszeg egzakt); a II/13 létráinak kettős számolása (gépezet és zárt képlet, egyezés $10^{-15}$), a darabolt két független felépítése és a sík binomiális létrája mint az összeesési lemma spektrális megerősítése; a II/14 kettős számolása mind a 224 hálón ($7{,}9\cdot10^{-14}$), a 224 háló egzakt nyomösszege (3072), a tér-szövés páros-jegyének egzakt tükör-szimmetriája ($10^{-15}$) és a 12×12×12-es golyó egzakt $4r^2+2$ törvénye $r=5$-ig; a II/15 létráinak kettős számolása 32 célon ($1{,}3\cdot10^{-12}$), a teljes-töltési egyezés ($8{,}4\cdot10^{-12}$) és a vetítő zárt kontra gépi útja ($1{,}7\cdot10^{-15}$); a II/16 ritka maradék-próbája ($5{,}3\cdot10^{-14}$) és a mintavételes vetítő-pecsét két ága ($5{,}1\cdot10^{-14}$, illetve $9{,}4\cdot10^{-16}$).