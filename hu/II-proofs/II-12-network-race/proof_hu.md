---
id: II-12
type: proof
lang: hu
pair: proof_en.md
pair_status: missing
doc_version: "1.3"
status: bukott
builds_on: [II-11, II-01, I-06]
imports: "konvenció: versenyszabály (rögzített, kötelező költségvetés); a mentőpróba jelölt importja: helyek egyenrangúsága (III/1, 5.)"
---

# II/12. A hálóverseny — a kiválasztási jelölt bukása

**A kérdés.** A kiválasztási kérdés ([III/2, 2.](../../III-frontier/III-02-open-questions_hu.md)) élesben: ha a szerződésháló maga a változó, milyen elrendezés győz? A jelölt előre kimondva: az összefüggést a kizárás kényszeríti ki — geometria ott születik, ahol sok kizáró példány osztozik a simasági szerződésen; a jóslat, cáfolhatóan: a geometrikus háló nyer. A versenyszabály — előre deklarált összehasonlítási konvenció: rögzített szerződés-költségvetést kötelező elhelyezni, az egyensúly a legkisebb összköltségű elrendezés.

**A rendszer és a szerződés.** Tizenkét hely; simasági költségvetés 12 csatolásegység, szabadon osztható; $N$ kizáró példány, $N = 1$-től 12-ig végigpásztázva. A költség: a szerződésháló ütem-létrájának alulról töltése — a [kizárás tétele](../../I-language/I-06-identity_hu.md) szerint minden ütemet legfeljebb egy példány. A kötés-oldal kézzel már eldőlt (a páros-fedés nulla költséggel győz — a régi III/2, 2.); a számolt verseny ezért a simasági szerződésé. Kihirdetett versenyzők: **por** (hat páros szerződés, kétszeres erővel), **sűrű** (mindenki-mindenkivel), **kör**.

**A számolás.** A rácsgépezet hálózatokon: a szerződésháló mátrixa, ütem-létra sajátfeladatként, alulról töltés, minden $N$-re.

**Az eredmény** (összköltség $N$ példánynál):

| N példány | 4 | 6 | 8 | 9 | 10 |
|---|---|---|---|---|---|
| por | 0 | 0 | 8 | 12 | 16 |
| kör | 1,54 | 4,54 | 9,54 | 12,54 | 16,27 |
| sűrű | 6,55 | 10,91 | 15,27 | 17,45 | 19,64 |
| egyetlen kövér szerződés | 0 | 0 | 0 | 0 | 0 |

**A jóslat megbukott.** A por minden töltésnél veri a kört, a sűrű mindenütt utolsó — és az igazi győztes még a pornál is durvább.

**Tétel: az összeomlási tétel.** A simasági költség sosem negatív; az az elrendezés, amely a teljes költségvetést egyetlen szerződésbe gyűjti, tizenegy példányig nullát ér el (tizenegy lecsatolt nulla-módus: tíz üres hely és a pár közös módusa) — tehát egzakt győztes. A szökési út az **üres hely**: a példányok a szerződésmentes helyekre parkolnak. A kötés-oldali párjával együtt: **egyik bevizsgált szerződés sem választ geometriát — szabad hálónál minden költségvetés sarokba omlik.**

**Tétel: a nyom-döntetlen.** Teljes töltésnél ($N = 12$) minden háló pontosan a költségvetés kétszeresét fizeti — a teljes létra összege hálófüggetlen. Teljes töltésnél a verseny elvi döntetlen.

**A mentőpróba.** A parkolót egyetlen kimondás zárja be — a **helyek egyenrangúsága** ([III/1, 5.](../../III-frontier/III-01-candidate-laws_hu.md), új jelölt import): nincs kitüntetett hely, a háló minden helyről ugyanúgy néz ki. Tizenkét egységnyi szerződéssel ez helyenként pontosan kettőt ad; a versenyzők a körfelbontások: egy 12-es kör, két hatszög, három négyzet, négy háromszög. A győztesek:

| N példány | 1–4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|
| győztes | széteső (0) | kör (2,54) | két hatszög (4) | kör (6,54) | kör (9,54) | három négyzet (12) | darabolások (16) | hármas holtverseny (20) | döntetlen (24) |

A sűrűség kényszeríti az összefüggést — négy példányig még a széteső nyer (komponensenként egy ingyen nulla-módus), öttől az egyetlen összefüggő kör az él —, de az éles törvény hiányzik: fél-töltésnél a kettéhasadás, 9–10-nél a fok-rezonanciás darabolás visszaüt.

**A hurok zárása.** A homogén győztesen (kör, 7 példány — zárt fok, egyértelmű állapot) a [II/11](../II-11-locality-readout/proof_hu.md) visszarakója a geometriát kiolvassa: a szomszéd-közelség 0,436, minden távolabbi 0,03 alatt (tizenötszörös ugrás); 12/12 él helyes; golyónövekedés lépésenként +2 — egy kiterjedés. Ahol geometria győz, ott az olvasható is.

**Ellenőrzés a valóságon.** A por-hajlam nem a gépezet hibája — a fizika méri: a fél-töltésű lánc magától páros mintázatba torzul, amint a csatolások ereje szabaddá válik ([Peierls-torzulás; a poliacetilén mért váltakozó kötéshossza](../../appendix/C-benchmarks_hu.md)), és az összefüggő rácsot ott is külön mechanizmus — a rács merevsége — menti meg. A nyelv összeomlási tétele ennek a hajlamnak a szélső, egzakt alakja.

**Import-számla:** a versenyszabály (kötelező, rögzített költségvetés) — előre deklarált konvenció; a mentőpróba új, jelölt importja a helyek egyenrangúsága ([III/1, 5.](../../III-frontier/III-01-candidate-laws_hu.md)). **Mit igazolt:** bukás-próba — a kizárás-jelölt naiv alakja megbukott, és a bukás hozadéka két tétel (összeomlás, nyom-döntetlen), egy fél-eredmény (a sűrűség kényszeríti az összefüggést a homogén osztályban) és egy gyökér-jelzés: a baj forrása, hogy a szerződés a nyelvben ingyen erőforrás — a fizikában a csatolást a példányok hordozzák; a kiválasztás ott dőlhet el, ahol a szerződések maguk születnek ([III/2, 7.](../../III-frontier/III-02-open-questions_hu.md)).