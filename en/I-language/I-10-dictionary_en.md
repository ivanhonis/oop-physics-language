---
id: I-10
type: chapter
lang: en
pair: I-10-dictionary_hu.md
pair_status: in-sync
doc_version: "1.3"
status: ervenyes
---

# I/10. The dictionary

This file is at the same time the terminology source of the translations (CONTRIBUTING, point 8). Relative to the Hungarian pair it carries a **third column**: the Hungarian original of the language's own technical terms. Every translation works from here — the first column fixes the English term, the third anchors it to the source language.

**State and view**

| OOP concept | Physical counterpart | Hungarian term |
|---|---|---|
| Object type (S, M) | State space + operators (Hilbert space) | Objektumtípus (S, M) |
| Instance | A concrete state | Példány |
| Field | Weight(s) on the possible values | Mező |
| Fixed total length of the weights | Normalization | Súlyok rögzített összhossza |
| View (read-only, derived state) | Mixed state (reduced density matrix) | Nézet |
| Witness rule (summing out the partner) | Partial trace | Tanú-szabály |
| The disk / ball of the views | Bloch sphere | A nézetek korongja / golyója |
| The rim distance of the view | Purity — entanglement measure | A nézet peremtávolsága |
| Violation of encapsulation | Entanglement | Enkapszuláció sérülése |
| Exclusive ownership | Monogamy of entanglement | Kizárólagos birtoklás |

**Operations and laws**

| OOP concept | Physical counterpart | Hungarian term |
|---|---|---|
| Reversible setter | Unitary time evolution | Visszafordítható setter |
| Getter (always with a side effect) | Measurement | Getter (mindig mellékhatásos) |
| Weight-preserving operation | Linearity | Súlytartó művelet |
| The fee of the getter on a bound system | The energy cost of breaking the bond | A getter díja kötött rendszeren |
| The immobility of the unconditional view | No-signaling | A feltétel nélküli nézet mozdulatlansága |
| The impossibility of clone() | No-Cloning theorem | clone() lehetetlensége |
| Move (the original is destroyed) | Teleportation | Mozgatás (move) |
| The environment as witness | Decoherence | A környezet mint tanú |
| Internal witness (the system as its own environment) | Thermalization (eigenstate thermalization) | Belső tanú |
| The stalling of witnessing under strong unevenness | Many-body localization (MBL) | A tanúsítás elakadása erős egyenetlenségnél |

**Contracts and energy**

| OOP concept | Physical counterpart | Hungarian term |
|---|---|---|
| Relation contract (loss function) | Interaction energy (Hamiltonian) | Kapcsolat-szerződés (veszteségfüggvény) |
| Total cost | Energy | Összköltség |
| The contract as engine | Schrödinger equation | A szerződés mint motor |
| Self-rotating pattern | Stationary state (energy eigenstate) | Önforgó mintázat |
| The discrete beats of the engine | Energy levels, eigenfrequencies | A motor diszkrét ütemei |
| Beat ladder in a bound system | Discrete energy spectrum | Ütem-létra kötött rendszerben |
| The disappearance of the ladder above zero cost | Ionization (continuous spectrum) | A létra eltűnése nulla költség fölött |
| Level coincidence | Degeneracy | Szint-egybeesés |
| Smoothness contract | Kinetic energy | Simasági szerződés |
| Uniformity theorem | Universality | Egyformasági tétel |
| The scale difference of the local mixings | Effective mass | A helyi keverések léptékkülönbsége |
| Locality (mixing only between neighbors) | Locality | Helyiség |
| Attractive contract (distance-inverse discount) | Coulomb potential | Vonzó szerződés |
| Repulsive contract | Coulomb repulsion | Taszítási szerződés |
| Equilibrium state | Ground state | Egyensúlyi állapot |
| Temperature-weighted equilibrium view | Thermal (Gibbs) state | Hőmérséklet-súlyozta egyensúlyi nézet |
| The yield of joint ownership | Binding energy | Közös birtoklás hozadéka |
| Training (handing off cost) | Scattering into the environment (dissipation) | Tanítás (költség leadása) |

**Multiplicity and identity**

| OOP concept | Physical counterpart | Hungarian term |
|---|---|---|
| The law of identity (the instance identifier is not data) | Indistinguishability of identical particles | Az azonosság törvénye |
| Sharing type (unchanged under exchange) | Boson | Osztozó típus |
| Excluding type (sign-reversing under exchange) | Fermion | Kizáró típus |
| The theorem of exclusion | Pauli principle | A kizárás tétele |
| Internal two-valued field | Spin | Belső kétértékű mező |
| Exchange discount | Exchange interaction | Kicserélődési kedvezmény |
| The discount of parallel alignment within the degree | Hund's rule (first) | A párhuzamos beállás kedvezménye a fokon belül |
| The filling numbers of the degrees | Shell structure ("magic numbers") | A fokok betelési számai |
| Filling fee, fee jump | Chemical potential, addition energy | Betöltési díj, díjugrás |

**Systems and phenomena**

| OOP concept | Physical counterpart | Hungarian term |
|---|---|---|
| Pairwise expectations that cannot be satisfied at once | Frustration | Egyszerre nem teljesíthető páros elvárások |
| The undecided choice of frustration | Chirality (degenerate ground-state doublets) | A frusztráció eldöntetlen választása |
| Frozen covering (every object in a fixed pair) | Valence-bond solid (VBS) | Befagyott fedés |
| Self-rotating mixture of coverings | Resonating valence bond — quantum spin liquid | Fedések önforgó keveréke |
| Singlet mass below the lowest triplet | Anomalous low-energy singlet manifold | Szingulett-tömeg a legalsó hármas alatt |
| The rapid death of the correlations | Short-range order | A korrelációk gyors halála |
| The two constants of the level-spacing ratio (0.531 / 0.386) | Wigner–Dyson and Poisson statistics respectively | A fokköz-arány két állandója |
| Memory test (persisting pattern difference) | Imbalance | Emlék-próba |
| Avalanche (spreading of an internal witness core) | Thermal avalanche | Lavina |

**Space, scope, pattern-object**

| OOP concept | Physical counterpart | Hungarian term |
|---|---|---|
| Pairwise closeness (the surplus of the joint view over the two separate ones) | Mutual information | Páros közelség |
| Surface law (the entanglement of the cut-out piece grows with its boundary) | Entanglement area law | Felület-törvény |
| The rate of ball growth | Spatial dimension | A golyónövekedés üteme |
| Read-back geometry | Space built from entanglement (emergent space) | Visszaolvasott geometria |
| Scope-bound view fact | Observer-relative fact (Wigner's friend) | Hatókörhöz kötött nézet-tény |
| Object born from a pattern | Quasiparticle | Mintázatból lett objektum |
| Exchange type outside the two classes | Anyon | Két osztályon kívüli cseretípus |
| Equal rank of the sites (no distinguished site) | Homogeneity of space | Helyek egyenrangúsága |
| The number of contracts per site | Coordination number | Egy helyre jutó szerződések száma |
| Empty site as an escape route ("vacuum parking") | Decoupled zero mode | Üres hely mint szökési út |
| Trace tie (at full filling every network is equal) | Spectral sum rule | Nyom-döntetlen |
| Weave network (the same wiring pattern at every site) | Cayley graph | Szövés-háló |
| Shell fit (victory at the closed degree) | Shell-closure stability | Héj-illeszkedés |
| Wrap-around resonance (the echo of the small weave) | Finite-size effect (periodic boundary) | Körbeérési rezonancia |
| Ball-increment law (+2 line, +4r plane) | Dimension-dependent volume growth | Golyónövekmény-törvény |

**Structural terms of the repository** (not in the Hungarian pair; fixed here for the translations)

| English | Hungarian |
|---|---|
| proof (a chapter of Part II) | próba |
| import ledger | import-számla |
| package method | csomag-módszer |
| rulebook | szabálykönyv |
| gate rule | kapu-szabály |
| outgoing claims | kimenő állítások |
| verdict | ítélet |
| trail | nyomvonal |
| site | hely |
| adjacency | szomszédság |
| degree (a level of a ladder, a shell) | fok |
| rung (a step of the extension staircase) | fok (a kiterjedés-lépcsőn) |
| coincidence lemma (two weaves are the same network) | összeesési lemma |
| collapse theorem (the budget collapses into a corner) | összeomlási tétel |
| extension (spatial) | kiterjedés |
| weave | szövés |
| native | honos |
| mirror mark | tükör-jegy |
| append-only numbering | bővítésálló számozás |
