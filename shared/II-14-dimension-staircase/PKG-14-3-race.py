# PKG-14-3 — A betöltési verseny (II/14, kiterjedés-lépcső)
# B3 szerint: a létrák ÚJ kódúton számolódnak újra (illeszkedési mátrix:
# L = B^T B, élenként egy sor), és csak a hivatkozási értékekkel való
# egyezés után indul a verseny.
# Verseny: alulról töltés — költség(N) = a létra N legkisebb ütemének összege.

import numpy as np
from itertools import combinations
from math import gcd

N = 512
TOL = 1e-9


# ---------- új kódút: illeszkedési mátrix ----------

def laplacian_incidence(n, edges):
    B = np.zeros((len(edges), n))
    for r, (i, j) in enumerate(edges):
        B[r, i] = 1.0
        B[r, j] = -1.0
    return B.T @ B

def ring_edges(n, steps):
    E = set()
    for i in range(n):
        for s in steps:
            E.add((min(i, (i + s) % n), max(i, (i + s) % n)))
    return sorted(E)

def torus2_tri_edges(L1, L2):
    idx = lambda x, y: (x % L1) * L2 + (y % L2)
    E = set()
    for x in range(L1):
        for y in range(L2):
            a = idx(x, y)
            for dx, dy in [(1, 0), (0, 1), (1, 1)]:
                b = idx(x + dx, y + dy)
                E.add((min(a, b), max(a, b)))
    return sorted(E)

def torus3_edges(L):
    idx = lambda x, y, z: ((x % L) * L + (y % L)) * L + (z % L)
    E = set()
    for x in range(L):
        for y in range(L):
            for z in range(L):
                a = idx(x, y, z)
                for d in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]:
                    b = idx(x + d[0], y + d[1], z + d[2])
                    E.add((min(a, b), max(a, b)))
    return sorted(E)


# ---------- a mezőny felépítése az új úton ----------

field = {}
field["J2 sik 16x32"] = np.sort(np.linalg.eigvalsh(
    laplacian_incidence(N, torus2_tri_edges(16, 32))))
field["J3 ter 8x8x8"] = np.sort(np.linalg.eigvalsh(
    laplacian_incidence(N, torus3_edges(8))))
field["kontroll sik 8x64"] = np.sort(np.linalg.eigvalsh(
    laplacian_incidence(N, torus2_tri_edges(8, 64))))
for trip in combinations(range(1, 13), 3):
    field["vonal %s" % (trip,)] = np.sort(np.linalg.eigvalsh(
        laplacian_incidence(N, ring_edges(N, trip))))

J1 = "vonal (1, 2, 3)"
J2 = "J2 sik 16x32"
J3 = "J3 ter 8x8x8"

# ---------- B3: egyezés a hivatkozási értékekkel ----------

print("== B3 elofeltetel: fuggetlen ujraszamolas ==")
traces = {k: float(v.sum()) for k, v in field.items()}
print("nyomosszeg min/max: %.10f / %.10f (eloirt 3072)"
      % (min(traces.values()), max(traces.values())))
zeros = {k: int((v < TOL).sum()) for k, v in field.items()}
print("nulla-modusok: J1=%d J2=%d J3=%d kontroll=%d; szeteso pasztazok: %d db"
      % (zeros[J1], zeros[J2], zeros[J3], zeros["kontroll sik 8x64"],
         sum(1 for k, z in zeros.items() if k.startswith("vonal") and z > 1)))
spot = [
    ("J1 2. utem", field[J1][1], 0.002108),
    ("J2 2. utem", field[J2][1], 0.076864),
    ("J3 2. utem", field[J3][1], 2.0 - np.sqrt(2.0)),
    ("J3 teto",    field[J3][-1], 12.0),
]
for name, got, ref in spot:
    print("  %-12s %.6f (hivatkozas %.6f, elteres %.1e)"
          % (name, got, ref, abs(got - ref)))

# ---------- a verseny ----------

cost = {k: np.concatenate([[0.0], np.cumsum(v)]) for k, v in field.items()}
# cost[k][n] = koltseg n peldanynal

names = sorted(field.keys())
winners = []
for n in range(1, N + 1):
    vals = np.array([cost[k][n] for k in names])
    m = vals.min()
    w = [names[i] for i in np.flatnonzero(vals < m + TOL)]
    winners.append((n, m, w))

# --- a fo olvasat: a deklaralt harmason ---
print("\n== A fo olvasat: J1-J2-J3 paronkent ==")
trio_w = []
for n in range(1, N + 1):
    c1, c2, c3 = cost[J1][n], cost[J2][n], cost[J3][n]
    m = min(c1, c2, c3)
    w = "".join(t for t, c in [("1", c1), ("2", c2), ("3", c3)] if c < m + TOL)
    trio_w.append(w)

def bands(seq, start=1):
    out = []
    for i, w in enumerate(seq):
        n = start + i
        if out and out[-1][0] == w:
            out[-1][2] = n
        else:
            out.append([w, n, n])
    return out

print("savok (gyoztes: N-tol N-ig):")
for w, a, b in bands(trio_w):
    print("  J%s: %d..%d" % (w, a, b))

# sik-sav es ter-sav a szabaly szerint (J2 veri mindkettot / J3 veri mindkettot)
sik_sav = [n for n in range(1, N) if trio_w[n - 1] == "2"]
ter_sav = [n for n in range(1, N) if trio_w[n - 1] == "3"]
def osszefuggo(xs):
    return bool(xs) and xs[-1] - xs[0] + 1 == len(xs)
print("sik-sav: %s (osszefuggo: %s)" %
      (("%d..%d" % (sik_sav[0], sik_sav[-1])) if sik_sav else "nincs", osszefuggo(sik_sav)))
print("ter-sav: %s (osszefuggo: %s)" %
      (("%d..%d" % (ter_sav[0], ter_sav[-1])) if ter_sav else "nincs", osszefuggo(ter_sav)))

# --- a teljes mezony ---
print("\n== Teljes mezony: szigoru gyoztesek rezsimjei ==")
def short(ws):
    if len(ws) > 3:
        return "%d-es holtverseny" % len(ws)
    return " + ".join(w.replace("vonal ", "v").replace(" sik 16x32", "")
                      .replace(" ter 8x8x8", "").replace("kontroll sik 8x64", "K8x64")
                      for w in ws)
seq = [short(w) for n, m, w in winners]
for w, a, b in bands(seq):
    n_mid = (a + b) // 2
    print("  N=%3d..%3d  %-28s (pl. N=%d koltseg %.3f)"
          % (a, b, w, n_mid, winners[n_mid - 1][1]))

# --- kulcs-ellenorzesek ---
print("\n== Ellenorzesek ==")
print("N=1: minden halo 0-t fizet:", all(abs(cost[k][1]) < TOL for k in names))
v512 = [cost[k][N] for k in names]
print("N=512: dontetlen 3072-n:", max(v512) - min(v512) < 1e-8,
      " (min %.8f, max %.8f)" % (min(v512), max(v512)))

# hej-logika: a J3 savhatara vs fokhatarai
fokhatarok = [1, 7, 19, 27, 33, 57, 81, 87, 126, 186, 198, 222, 290, 314,
              326, 386, 425, 431, 455, 479, 485, 493, 505, 511, 512]
if ter_sav:
    print("a ter-sav also hatara: %d; J3 fokhatarai a kozelben: %s"
          % (ter_sav[0], [f for f in fokhatarok if abs(f - ter_sav[0]) <= 6]))

# tukor-hatas: a teli veg gyoztese a legnagyobb tetok halojae?
tops = sorted(((field[k][-1], k) for k in names), reverse=True)
print("legmagasabb teto: %.4f (%s) — a teli veg varhato gyoztese" % (tops[0][0], tops[0][1]))

# J2 kontra kontroll: a nyujtas hatasa
j2_veri_K = [n for n in range(1, N) if cost[J2][n] < cost["kontroll sik 8x64"][n] - TOL]
print("a 16x32 sik a 8x64 kontrollt %d toltesen veri" % len(j2_veri_K))
