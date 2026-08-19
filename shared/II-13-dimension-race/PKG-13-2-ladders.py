# PKG-13-2 — Az ütem-létrák számoló kódja
# Csomag-dokumentum: PKG-13-2-ladders_hu.md (a kód nyelvfüggetlen)
# Kimenet: a három jelölt és a teljes vonal-családi pásztázás létrái,
# a csomag 6. pontjának önellenőrzéseivel.

import math
import numpy as np
from itertools import combinations

N = 16

def circulant_L(steps):
    """A 16-os szövés (kör, adott lépéspárokkal) szerződésmátrixa."""
    L = np.zeros((N, N))
    for i in range(N):
        for s in steps:
            for j in ((i + s) % N, (i - s) % N):
                L[i, j] -= 1.0
        L[i, i] = 2 * len(steps)
    return L

def analytic_circ(steps):
    """Ugyanaz zárt képletből — független ellenőrzés."""
    ks = np.arange(N)
    lam = np.zeros(N)
    for s in steps:
        lam += 2 - 2 * np.cos(2 * np.pi * s * ks / N)
    return np.sort(lam)

def torus_L():
    """A 4x4-es körbezárt rács (sík jelölt) szerződésmátrixa."""
    L = np.zeros((N, N))
    def idx(x, y):
        return 4 * x + y
    for x in range(4):
        for y in range(4):
            i = idx(x, y)
            for j in (idx((x + 1) % 4, y), idx((x - 1) % 4, y),
                      idx(x, (y + 1) % 4), idx(x, (y - 1) % 4)):
                L[i, j] -= 1.0
            L[i, i] = 4.0
    return L

def spec(L):
    return np.sort(np.linalg.eigvalsh(L))

# --- a három jelölt ---
J1 = spec(circulant_L([1, 2]))
J2 = spec(torus_L())
J3 = spec(circulant_L([2, 4]))          # = ket kulonallo, vastagitott 8-as kor
J3_direct = np.sort(np.concatenate([    # fuggetlen felepites: 2 x C8(1,2)
    np.sort([(2 - 2 * np.cos(2 * np.pi * 1 * k / 8))
             + (2 - 2 * np.cos(2 * np.pi * 2 * k / 8)) for k in range(8)])
] * 2))

print("J1 (vonal, C16(1,2)):     ", np.round(J1, 4))
print("J2 (sik/torusz, C4xC4):   ", np.round(J2, 4))
print("J3 (darabolt, 2xC8(1,2)): ", np.round(J3, 4))

# --- onellenorzesek (csomag 6. pont) ---
print("\nONELLENORZESEK")
print("nyomosszegek (mind 64):", round(J1.sum(), 10), round(J2.sum(), 10), round(J3.sum(), 10))
print("nulla-modusok (J1,J2,J3):", int((J1 < 1e-9).sum()), int((J2 < 1e-9).sum()), int((J3 < 1e-9).sum()))
print("J1 analitikus vs gepezet, max elteres:", np.max(np.abs(J1 - analytic_circ([1, 2]))))
print("J3 ket felepitese, max elteres:", np.max(np.abs(J3 - J3_direct)))
q4 = np.sort(np.concatenate([[2 * j] * math.comb(4, j) for j in range(5)]))
print("J2 == hiperkocka binomialis letra? max elteres:", np.max(np.abs(J2 - q4)))

# --- kotelezo pasztazas: a vonal-csalad mind a 21 tagja ---
print("\nPASZTAZAS: C16(a,b), 1<=a<b<=7")
classes = {}
for a, b in combinations(range(1, 8), 2):
    lam = np.round(spec(circulant_L([a, b])), 6)
    zero = int((lam < 1e-9).sum())
    classes.setdefault(tuple(lam), []).append((a, b, zero))
print(f"tagok: {sum(len(v) for v in classes.values())}, kulonbozo letrak: {len(classes)}")
for key, members in sorted(classes.items(), key=lambda kv: kv[0]):
    lam = np.array(key)
    tags = ", ".join(f"({a},{b})" for a, b, _ in members)
    zero = members[0][2]
    print(f"  lepesek {tags}: nulla-modus={zero}, letra eleje {np.round(lam[:5], 3)}, nyom={round(lam.sum(), 6)}")
