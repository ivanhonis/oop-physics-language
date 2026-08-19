# PKG-14-4 — A hurok zárása: kiolvasás a győztesen (II/14)
# A rögzített jegyzőkönyv (PKG-14-1, 8. pont; PKG-14-3, C4):
#   - győztes: J3 tér (8x8x8), N = 290 (a tér-sáv első zárt foka)
#   - szabad kizáró példányok: a nézetek a példány-korrelációkból egzaktul
#     (a 4. eszköz gyorsított alakja) — közelség = a kész állapot
#     páronkénti egytest-térképe G(δ)
#   - a szomszédszámot a közelség-lista ugrása jelöli ki
#   - golyó-olvasat legfeljebb r = 3-ig, a három hivatkozási sor ellen
#   - rezonancia-őrszem: átellenes osztályok külön jelentve

import numpy as np
from collections import deque

L = 8
Nsite = L ** 3
Ninst = 290

# --- a letra es a betoltes (zart alak) ---
k = 2.0 * np.pi * np.arange(L) / L
one = 2.0 * (1.0 - np.cos(k))
lam = one[:, None, None] + one[None, :, None] + one[None, None, :]
order = np.argsort(lam.ravel(), kind="stable")
occ_flat = order[:Ninst]
lam_sorted = np.sort(lam.ravel())
print("zart fok ellenorzes: a 290. utem %.6f, a 291. utem %.6f (res %.4f)"
      % (lam_sorted[289], lam_sorted[290], lam_sorted[290] - lam_sorted[289]))
assert lam_sorted[290] - lam_sorted[289] > 0.5

# a betoltes a teljes lambda<=6 keszlet? (egyertelmuseg)
assert abs(lam_sorted[289] - 6.0) < 1e-9 and lam_sorted[290] > 6.0

# --- kozelseg-terkep: G(delta) = (1/512) sum_occ e^{i k.delta} ---
occ = np.zeros((L, L, L), dtype=bool)
occ.ravel()[occ_flat] = True
# G(delta) az elfoglaltsag-indikator inverz Fourier-transzformaltja
G = np.fft.ifftn(occ.astype(float))  # G[dx,dy,dz], G[0,0,0] = 290/512
assert np.max(np.abs(G.imag)) < 1e-12
G = G.real

# homogenitas: a szoves miatt G csak az eltolastol fugg — ez konstrukcio,
# a jegyzokonyv szerint a szorast a peldany-szintu terkepen kellene merni;
# szabad kizaro peldanyoknal a ketto egzaktul azonos (4. eszkoz).

# --- eltolas-osztalyok ---
def canon(d):
    # az oktaeder-szimmetria: elojel es tengelycsere erejeig
    v = sorted(min(x % L, (-x) % L) for x in d)
    return tuple(v)

classes = {}
for dx in range(L):
    for dy in range(L):
        for dz in range(L):
            if dx == dy == dz == 0:
                continue
            c = canon((dx, dy, dz))
            classes.setdefault(c, []).append(G[dx, dy, dz])

rows = []
for c, vals in classes.items():
    vals = np.array(vals)
    rows.append((c, float(vals.mean()), float(vals.std()), len(vals)))
    assert vals.std() < 1e-12  # osztalyon belul egzaktul azonos

rows.sort(key=lambda r: -abs(r[1]))
print()
print("== kozelseg-osztalyok (|G| szerint csokkenoen, eleje) ==")
for c, m, s, n in rows[:10]:
    print("  osztaly %-10s  G = %+.6f   (x%d eltolas)" % (str(c), m, n))

# --- rezonancia-orszem: egyezik-e nem-szomszed osztaly a szomszeddal ---
nb = rows[0]
echo = [r for r in rows[1:] if abs(abs(r[1]) - abs(nb[1])) < 1e-12]
print()
print("rezonancia-orszem: a szomszed-osztallyal egzaktul egyezo mas osztaly: %d db"
      % len(echo))
print("atellenes visszhang (4,4,4): G = %+.6f, a szomszed %.1f%%-a"
      % (G[4, 4, 4], 100 * abs(G[4, 4, 4] / G[0, 0, 1])))

# --- az ugras es a szomszedszam kijelolese, KET SZABALY SZERINT ---
# A PKG-14-1 8. pontja nem mondta ki, hogy az ugrast az elojeles vagy az
# abszolut ertekes kozelseg-listan kell keresni. E szoveten a ketto
# szetvalik, ezert a csomag mindkettot jelenti; a fo szamsor az elojeles
# olvasate. (Az elojeles alakot a PKG-14-5 emelte szabalyya.)

idx = lambda x, y, z: ((x % L) * L + (y % L)) * L + (z % L)
true_edges = set()
for x in range(L):
    for y in range(L):
        for z in range(L):
            a = idx(x, y, z)
            for d in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]:
                b = idx(x + d[0], y + d[1], z + d[2])
                true_edges.add((min(a, b), max(a, b)))

flat_off = [(dx, dy, dz) for dx in range(L) for dy in range(L) for dz in range(L)
            if not dx == dy == dz == 0]


def olvasat(mod):
    """Egy kiolvasas a megadott ugras-szabaly szerint: 'elojeles' vagy 'abszolut'."""
    kulcs = (lambda d: G[d]) if mod == "elojeles" else (lambda d: abs(G[d]))
    rend = sorted(flat_off, key=lambda d: -kulcs(d))
    vals = np.array([kulcs(d) for d in rend[:30]])
    ratios = vals[:-1] / np.maximum(np.abs(vals[1:]), 1e-300)
    kstar = int(np.argmax(ratios[:20])) + 1

    top = rend[:kstar]
    rec_edges = set()
    for x in range(L):
        for y in range(L):
            for z in range(L):
                a = idx(x, y, z)
                for d in top:
                    b = idx(x + d[0], y + d[1], z + d[2])
                    rec_edges.add((min(a, b), max(a, b)))

    adj = [[] for _ in range(Nsite)]
    for a, b in rec_edges:
        adj[a].append(b)
        adj[b].append(a)
    dist = [-1] * Nsite
    dist[0] = 0
    q = deque([0])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if dist[v] < 0:
                dist[v] = dist[u] + 1
                q.append(v)
    ball = [sum(1 for d in dist if 0 <= d <= r) for r in range(4)]

    print()
    print("== %s ugras-szabaly ==" % mod)
    print("  rendezett lista eleje:", np.round(vals[:10], 5))
    print("  a legnagyobb ugras a(z) %d. hely utan: %.6f -> %.6f (%.2f-szeres)"
          % (kstar, vals[kstar - 1], vals[kstar],
             vals[kstar - 1] / abs(vals[kstar])))
    print("  beemelt eltolas-osztalyok:", sorted({canon(d) for d in top}))
    print("  visszarakas: %d el; valodi megvan %d/%d; fantom %d; hianyzo %d"
          % (len(rec_edges), len(rec_edges & true_edges), len(true_edges),
             len(rec_edges - true_edges), len(true_edges - rec_edges)))
    print("  golyo (r=0..3):", ball,
          " novekmenyek:", [ball[i + 1] - ball[i] for i in range(3)])
    return kstar, ball


olvasat("elojeles")   # a publikalt fo szamsor: k*=7, 256 fantom, golyo 1,8,32,88
olvasat("abszolut")   # a masodik olvasat: k*=15, 2304 fantom, golyo 1,16,92,296
print()
print("hivatkozasi sorok: vonal 1,7,13,19 | sik 1,7,19,37 | ter 1,7,25,63")
