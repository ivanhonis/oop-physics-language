# PKG-14-5 — Az ujrakiolvasas rogzitett hatokorrel (II/14)
# A jegyzokonyv (a futtatas elott rogzitve):
#   - rendszer: J3 ter (12x12x12), hatos koordinacio, 5184 szerzodes
#   - toltes: a fel-tolteshez legkozelebbi zart fok felulrol (determinisztikus szabaly)
#   - kozelseg: a kesz allapot paronkenti egytest-terkepe G(delta) (II/11, 4. eszkoz)
#   - UJRAKIOLVASASI JAVITAS 1 (elojeles ugras): az ugras az ELOJELES listan
#     keresendo, nem az abszolut erteken; az atellenes osztaly elojelevel
#     egyutt kulon jelentendo (a II/14 elojel-hezagjanak zarasa)
#   - UJRAKIOLVASASI JAVITAS 2 (sav-orszem): a leggyengebb elfogadott es a
#     legerosebb elutasitott kozelseg hanyadosa; 2-es tenyezo alatt az olvasat
#     reszleges (a II/14 szuk "egzakt egyezes" orszemenek tagitasa)
#   - teljesseg-szamla: megtalalt / hianyzo / fantom, mindharom szammal
#   - golyo-olvasat r <= 5-ig (ervenyesseg: 2r < 12 korbeeres), a hivatkozasi
#     sor a ter negyzetes torvenye: 1, 7, 25, 63, 129, 231 (novekmeny 4r^2+2)
#   - ketutas szabaly: a letra es a vetito zart alakban ES gepi sajatfeladattal
# Itelet-feltetelek (elore): A1 zart fok all; A2 5184/5184, 0 fantom, 0 hianyzo;
# A3 golyo egzakt; A4 orszem >= 2. Mind all -> "all"; barmelyik bukik -> reszleges.

import numpy as np
from collections import deque

L = 12
NSITE = L ** 3            # 1728 hely
NCONTRACT = 3 * NSITE     # 5184 szerzodes (helyenkent hat)
TOL = 1e-9

# --- 1) A letra ket fuggetlen uton -------------------------------------------
k = 2.0 * np.pi * np.arange(L) / L
one = 2.0 * (1.0 - np.cos(k))
lam = one[:, None, None] + one[None, :, None] + one[None, None, :]   # zart alak
lam_flat = lam.ravel()
lam_sorted = np.sort(lam_flat)

idx = lambda x, y, z: ((x % L) * L + (y % L)) * L + (z % L)
Lap = np.zeros((NSITE, NSITE))
for x in range(L):
    for y in range(L):
        for z in range(L):
            a = idx(x, y, z)
            Lap[a, a] = 6.0
            for d in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]:
                b = idx(x + d[0], y + d[1], z + d[2])
                Lap[a, b] -= 1.0
                Lap[b, a] -= 1.0
w, V = np.linalg.eigh(Lap)                                            # gepi ut
elteres_letra = float(np.max(np.abs(np.sort(w) - lam_sorted)))
print("letra ket uton: legnagyobb elteres = %.2e" % elteres_letra)
assert elteres_letra < 1e-10

# --- 2) A zart fok kijelolese (rogzitett szabaly) ----------------------------
fel = NSITE // 2                                   # 864
B = int(np.sum(lam_flat < 6.0 - TOL))              # a 6 alatti utemek
D6 = int(np.sum(np.abs(lam_flat - 6.0) < TOL))     # a 6-os polc szelessege
NINST = B + D6                                     # az elso zart fok a fel-toltes folott
res = lam_sorted[NINST] - lam_sorted[NINST - 1]
print("zart fok: N* = %d (= %d + %d); fel-toltes %d; res a fok folott %.6f"
      % (NINST, B, D6, fel, res))
assert B < fel <= NINST and res > 1e-6

# --- 3) Kozelseg-terkep ket uton ---------------------------------------------
occ = lam <= 6.0 + TOL
assert int(occ.sum()) == NINST
G = np.fft.ifftn(occ.astype(float))                # zart ut: G(delta)
assert np.max(np.abs(G.imag)) < 1e-12
G = G.real

occ_cols = w <= 6.0 + TOL                          # gepi ut: vetito a sajatvektorokbol
assert int(occ_cols.sum()) == NINST
P0 = (V[:, occ_cols] @ V[0, occ_cols])             # a vetito 0. sora
G_gepi = np.empty(NSITE)
for x in range(L):
    for y in range(L):
        for z in range(L):
            G_gepi[idx(x, y, z)] = G[x, y, z]
elteres_vetito = float(np.max(np.abs(P0 - G_gepi)))
print("vetito ket uton: legnagyobb elteres = %.2e" % elteres_vetito)
assert elteres_vetito < 1e-10

# --- 4) Eltolas-osztalyok es az atellenes visszhang --------------------------
def canon(d):
    return tuple(sorted(int(min(x % L, (-x) % L)) for x in d))

classes = {}
for dx in range(L):
    for dy in range(L):
        for dz in range(L):
            if dx == dy == dz == 0:
                continue
            classes.setdefault(canon((dx, dy, dz)), []).append(G[dx, dy, dz])
for c, vals in classes.items():
    assert np.std(vals) < 1e-12                    # szoves: osztalyon belul egzakt

szomszed = G[1, 0, 0]
atellenes = G[L // 2, L // 2, L // 2]
print("szomszed-kozelseg G(1,0,0) = %+.6f" % szomszed)
print("atellenes visszhang G(6,6,6) = %+.6f  (elojel: %s; |arany a szomszedhoz| = %.4f)"
      % (atellenes, "negativ" if atellenes < 0 else "pozitiv",
         abs(atellenes) / szomszed))

# --- 5) Az ugras az ELOJELES listan (javitott szabaly) -----------------------
g = G.ravel().copy()
g[0] = -np.inf                                     # sajat hely kizarva
rend = np.argsort(g)[::-1]                         # elojeles, csokkeno
v = g[rend]
ablak = 30                                         # rogzitett keresesi ablak
legjobb, kstar = -1.0, None
for m in range(1, ablak + 1):
    if v[m] > 0:
        r = v[m - 1] / v[m]
        if r > legjobb:
            legjobb, kstar = r, m
print("elojeles lista eleje:", np.round(v[:10], 5))
print("ugras a(z) %d. hely utan: %.5f -> %.5f (%.1f-szeres)"
      % (kstar, v[kstar - 1], v[kstar], legjobb))

# sav-orszem: leggyengebb elfogadott / legerosebb elutasitott (nagysag szerint);
# a sajat hely helyorzoje (-inf) nem tagja a mezonynek
maradek = v[kstar:]
maradek = maradek[np.isfinite(maradek)]
j = int(np.argmax(np.abs(maradek)))
erosebb_ert = float(maradek[j])
d_erosebb = tuple(np.unravel_index(int(rend[kstar + j]), (L, L, L)))
S = v[kstar - 1] / abs(erosebb_ert)
print("sav-orszem: S = %.4f  (kuszob: 2); legerosebb elutasitott: %s osztaly, G = %+.6f"
      % (S, canon(d_erosebb), erosebb_ert))

# osszevetes a regi, abszolut-ertekes szaballyal (diagnosztika, nem itelet)
va = np.sort(np.abs(np.where(np.isfinite(g), g, 0)))[::-1]
r_abs = va[:ablak] / np.maximum(va[1:ablak + 1], 1e-300)
k_abs = int(np.argmax(r_abs)) + 1
print("regi abszolut szabaly (osszevetesul): ugras a(z) %d. hely utan (%.1f-szeres)"
      % (k_abs, r_abs[k_abs - 1]))

# --- 6) Visszarakas es teljesseg-szamla --------------------------------------
top = [tuple(np.unravel_index(int(i), (L, L, L))) for i in rend[:kstar]]
rec_edges = set()
for x in range(L):
    for y in range(L):
        for z in range(L):
            a = idx(x, y, z)
            for d in top:
                b = idx(x + d[0], y + d[1], z + d[2])
                rec_edges.add((min(a, b), max(a, b)))
true_edges = set()
for x in range(L):
    for y in range(L):
        for z in range(L):
            a = idx(x, y, z)
            for d in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]:
                b = idx(x + d[0], y + d[1], z + d[2])
                true_edges.add((min(a, b), max(a, b)))
megvan = len(rec_edges & true_edges)
fantom = len(rec_edges - true_edges)
hianyzo = len(true_edges - rec_edges)
print("teljesseg-szamla: megtalalt %d/%d; fantom %d; hianyzo %d"
      % (megvan, NCONTRACT, fantom, hianyzo))

# --- 7) Golyo-olvasat r <= 5 -------------------------------------------------
adj = [[] for _ in range(NSITE)]
for a, b in rec_edges:
    adj[a].append(b)
    adj[b].append(a)
dist = [-1] * NSITE
dist[0] = 0
q = deque([0])
while q:
    u = q.popleft()
    for x2 in adj[u]:
        if dist[x2] < 0:
            dist[x2] = dist[u] + 1
            q.append(x2)
golyo = [sum(1 for d in dist if 0 <= d <= r) for r in range(6)]
novek = [golyo[i + 1] - golyo[i] for i in range(5)]
hivatkozas = [1, 7, 25, 63, 129, 231]              # 4r^2+2 novekmennyel
print("golyo (r=0..5):", golyo, " novekmenyek:", novek)
print("hivatkozasi sor (ter, negyzetes):", hivatkozas)

# --- 8) Itelet a rogzitett feltetelek szerint --------------------------------
A1 = res > 1e-6
A2 = (megvan == NCONTRACT and fantom == 0 and hianyzo == 0)
A3 = (golyo == hivatkozas)
A4 = (S >= 2.0)
print("\nfeltetelek: A1 zart fok %s | A2 teljesseg %s | A3 golyo %s | A4 orszem %s"
      % tuple("all" if a else "BUKIK" for a in (A1, A2, A3, A4)))
print("ITELET:", "ALL — a 12-es meret-diagnozis hatokoron belul igazolva"
      if all((A1, A2, A3, A4)) else "RESZLEGES — a bukott feltetel megnevezve fent")
