---
id: I-10
type: chapter
lang: hu
pair: I-10-dictionary_en.md
pair_status: missing
doc_version: "1.3"
status: ervenyes
---

# I/10. A szótár

Ez a fájl egyben a fordítások terminológia-forrása (CONTRIBUTING, 8. pont): a nyelv saját szakszavainak angol megfelelőit az `_en` pár rögzíti majd, harmadik oszlopként — minden fordítás onnan dolgozik.

**Állapot és nézet**

| OOP-fogalom | Fizikai megfelelő |
|---|---|
| Objektumtípus (S, M) | Állapottér + operátorok (Hilbert-tér) |
| Példány | Konkrét állapot |
| Mező | Súly(ok) a lehetséges értékeken |
| Súlyok rögzített összhossza | Normálás |
| Nézet (csak-olvasható, származtatott állapot) | Kevert állapot (redukált sűrűségmátrix) |
| Tanú-szabály (a társ kiösszegzése) | Parciális nyom |
| A nézetek korongja / golyója | Bloch-gömb |
| A nézet peremtávolsága | Tisztaság — összefonódási mérőszám |
| Enkapszuláció sérülése | Összefonódás |
| Kizárólagos birtoklás | Összefonódás-monogámia |

**Műveletek és törvények**

| OOP-fogalom | Fizikai megfelelő |
|---|---|
| Visszafordítható setter | Unitér időfejlődés |
| Getter (mindig mellékhatásos) | Mérés |
| Súlytartó művelet | Linearitás |
| A getter díja kötött rendszeren | A kötésszakítás energiaköltsége |
| A feltétel nélküli nézet mozdulatlansága | Jelzésmentesség (no-signaling) |
| clone() lehetetlensége | No-Cloning tétel |
| Mozgatás (move, az eredeti megsemmisül) | Teleportálás |
| A környezet mint tanú | Dekoherencia |
| Belső tanú (a rendszer mint saját környezete) | Termalizáció (sajátállapot-termalizáció) |
| A tanúsítás elakadása erős egyenetlenségnél | Sok-test lokalizáció (MBL) |

**Szerződések és energia**

| OOP-fogalom | Fizikai megfelelő |
|---|---|
| Kapcsolat-szerződés (veszteségfüggvény) | Kölcsönhatási energia (Hamilton-operátor) |
| Összköltség | Energia |
| A szerződés mint motor | Schrödinger-egyenlet |
| Önforgó mintázat | Stacionárius állapot (energia-sajátállapot) |
| A motor diszkrét ütemei | Energiaszintek, sajátfrekvenciák |
| Ütem-létra kötött rendszerben | Diszkrét energiaspektrum |
| A létra eltűnése nulla költség fölött | Ionizáció (folytonos spektrum) |
| Szint-egybeesés | Degeneráció |
| Simasági szerződés | Mozgási energia |
| Egyformasági tétel | Univerzalitás |
| A helyi keverések léptékkülönbsége | Effektív tömeg |
| Helyiség (keverés csak szomszédok közt) | Lokalitás |
| Vonzó szerződés (távolság-fordított kedvezmény) | Coulomb-potenciál |
| Taszítási szerződés | Coulomb-taszítás |
| Egyensúlyi állapot | Alapállapot |
| Hőmérséklet-súlyozta egyensúlyi nézet | Termikus (Gibbs-)állapot |
| Közös birtoklás hozadéka | Kötési energia |
| Tanítás (költség leadása) | Környezetbe szóródás (disszipáció) |

**Sokaság és azonosság**

| OOP-fogalom | Fizikai megfelelő |
|---|---|
| Az azonosság törvénye (a példányazonosító nem adat) | Azonos részecskék megkülönböztethetetlensége |
| Osztozó típus (cserére változatlan) | Bozon |
| Kizáró típus (cserére előjelváltó) | Fermion |
| A kizárás tétele | Pauli-elv |
| Belső kétértékű mező | Spin |
| Kicserélődési kedvezmény | Kicserélődési kölcsönhatás |
| A párhuzamos beállás kedvezménye a fokon belül | Hund-szabály (első) |
| A fokok betelési számai | Héjszerkezet („bűvös számok") |
| Betöltési díj, díjugrás | Kémiai potenciál, addíciós energia |

**Rendszerek és jelenségek**

| OOP-fogalom | Fizikai megfelelő |
|---|---|
| Egyszerre nem teljesíthető páros elvárások | Frusztráció |
| A frusztráció eldöntetlen választása | Kiralitás (elfajult alapállapoti kettősök) |
| Befagyott fedés (minden objektum fix párban) | Valenciakötés-szilárd (VBS) |
| Fedések önforgó keveréke | Rezonáló valenciakötés — kvantum-spinfolyadék |
| Szingulett-tömeg a legalsó hármas alatt | Anomális alacsonyenergiás szingulett-sokaság |
| A korrelációk gyors halála | Rövid távú rend |
| A fokköz-arány két állandója (0,531 / 0,386) | Wigner–Dyson-, ill. Poisson-statisztika |
| Emlék-próba (megmaradó mintázat-különbség) | Kiegyenlítetlenség (imbalance) |
| Lavina (belső tanú-mag terjedése) | Termikus lavina (avalanche) |

**Tér, hatókör, mintázat-objektum**

| OOP-fogalom | Fizikai megfelelő |
|---|---|
| Páros közelség (a közös nézet többlete a két különhöz képest) | Kölcsönös információ |
| Felület-törvény (a kivágott darab összefonódása a határával nő) | Összefonódási területtörvény (area law) |
| A golyónövekedés üteme | Térbeli dimenzió |
| Visszaolvasott geometria | Összefonódásból épülő (emergens) tér |
| Hatókörhöz kötött nézet-tény | Megfigyelő-viszonylagos tény (Wigner barátja) |
| Mintázatból lett objektum | Kvázirészecske |
| Két osztályon kívüli cseretípus | Anyon |
| Helyek egyenrangúsága (nincs kitüntetett hely) | A tér homogenitása |
| Egy helyre jutó szerződések száma | Koordinációs szám |
| Üres hely mint szökési út („vákuum-parkoló") | Lecsatolt nulla-módus |
| Nyom-döntetlen (teljes töltésnél minden háló egyenlő) | Spektrális összegszabály |
| Szövés-háló (minden helyre azonos bekötési minta) | Cayley-gráf |
| Héj-illeszkedés (győzelem a zárt foknál) | Héjzáródási stabilitás |
| Körbeérési rezonancia (a kis szövés visszhangja) | Véges-méret hatás (periodikus perem) |
| Golyónövekmény-törvény (+2 vonal, +4r sík) | Dimenziófüggő térfogatnövekedés |
