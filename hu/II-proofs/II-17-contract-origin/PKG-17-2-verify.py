"""
PKG-17-2 — HITELESITO RESZ (a hurok elott)
Csomag-dokumentum: PKG-17-1-rulebook_hu.md, 6. szakasz (B3-elofeltetel) + 11. szakasz A3/A7

Ez a fajl NEM tartalmazza a hurkot. Csak azt ellenorzi, hogy a gepezet
ugyanazokat a szamokat adja, mint a mar lefutott fejezetek:
  - II/1  : a kotes-szerzodes zart alakja (peldany-szintu)
  - II/5  : haromszog — 15/8 peldany-szinten, 3/2 kozosen, negyszeres elfajulas
  - II/11 : teljes halo kontroll — 45/66, elfajulas 132, kozelseg-szoras 1e-16
  - II/11 : 12-es kor — 0.3011, kozelsegek 0.444 / 0.123 / 0.066 / 0.045 / 0.037
  - PKG-17-1 T1 : a lapos allapot fixpont — az F5 kivetelevel, ahol URES (nulla-proba)
"""

import numpy as np
from itertools import combinations

LN2 = np.log(2.0)


# ---------- UJ: a szerzodes felepitese a nyelv alakjabol ----------

def pair_cost_operator(n, i, j):
    """UJ metodus. A kotes-szerzodes parra vett operatora, kozvetlenul az I/8 alakjabol:
       L = a^2 + d^2 + 1/2 (b+c)^2  a (0,0),(0,1),(1,0),(1,1) sulyokon.
       Elso szamolasi ut."""
    dim = 1 << n
    M = np.zeros((dim, dim))
    bi, bj = 1 << (n - 1 - i), 1 << (n - 1 - j)
    for s in range(dim):
        vi, vj = (s & bi) != 0, (s & bj) != 0
        if vi == vj:
            M[s, s] += 1.0                    # a^2 es d^2
        else:
            M[s, s] += 0.5                    # 1/2 b^2, 1/2 c^2
            M[s, s ^ bi ^ bj] += 0.5          # a kereszttag: b*c
    return M


def pair_cost_operator_spin(n, i, j):
    """UJ metodus. Ugyanaz masodik, fuggetlen uton: 3/4 + S_i.S_j alakban.
       A ketutas szabaly (PKG-17-1, A7) elso eleme."""
    dim = 1 << n
    M = np.zeros((dim, dim))
    bi, bj = 1 << (n - 1 - i), 1 << (n - 1 - j)
    for s in range(dim):
        vi, vj = (s & bi) != 0, (s & bj) != 0
        M[s, s] += 0.75 + (0.25 if vi == vj else -0.25)
        if vi != vj:
            M[s, s ^ bi ^ bj] += 0.5
    return M


def hamiltonian(n, weights):
    """UJ metodus. A teljes koltseg-operator adott tartalom-vektorbol.
       weights: {(i,j): w} — csak a nem-nulla tartalmak."""
    dim = 1 << n
    H = np.zeros((dim, dim))
    for (i, j), w in weights.items():
        if w != 0.0:
            H += w * pair_cost_operator(n, i, j)
    return H


# ---------- UJ: alapallapot magnesezettseg-blokkokban ----------

def ground_space(n, H, tol=1e-9):
    """UJ metodus. A legkisebb koltsegu alter, blokkonkent szamolva.
       Visszaad: (minimum, allapotvektorok listaja a teljes terben)."""
    dim = 1 << n
    popc = np.array([bin(s).count("1") for s in range(dim)])
    best, vecs = np.inf, []
    for m in range(n + 1):
        idx = np.where(popc == m)[0]
        if idx.size == 0:
            continue
        w, v = np.linalg.eigh(H[np.ix_(idx, idx)])
        if w[0] < best - tol:
            best, vecs = w[0], []
        if w[0] < best + tol:
            for k in np.where(w < best + tol)[0]:
                full = np.zeros(dim)
                full[idx] = v[:, k]
                vecs.append(full)
    return best, vecs


# ---------- UJ: a kozelseg-merőszam (II/11) ----------

def reduced(vecs, n, sites):
    """UJ metodus. Reszallapot a nulla-koltsegu alter egyenletes keverekebol
       (II/11 kontroll-modszere: egzakt vetito, ha elfajult)."""
    k = len(sites)
    rest = [a for a in range(n) if a not in sites]
    d = 1 << k
    rho = np.zeros((d, d))
    for v in vecs:
        A = np.moveaxis(v.reshape([2] * n), sites + rest, range(n))
        A = A.reshape(d, -1)
        rho += A @ A.T
    return rho / len(vecs)


def entropy(rho):
    """UJ metodus. Neumann-entropia, termeszetes alapon (a II/11 0.69 = ln2 jegye)."""
    w = np.linalg.eigvalsh(rho)
    w = w[w > 1e-13]
    return float(-(w * np.log(w)).sum())


def proximity_map(n, vecs):
    """UJ metodus. Paronkenti kozelseg: mennyivel tud tobbet a kozos nezet."""
    s1 = [entropy(reduced(vecs, n, [a])) for a in range(n)]
    return {(i, j): s1[i] + s1[j] - entropy(reduced(vecs, n, [i, j]))
            for i, j in combinations(range(n), 2)}


# ---------- UJ: a generalo szabaly csaladja (PKG-17-1, 4. szakasz) ----------

FAMILY = {
    "F1": lambda x: x,
    "F2": lambda x: x ** 2,
    "F3": lambda x: np.sqrt(x),
    "F4": lambda x: x / (1.0 + x),
    "F5": lambda x: np.maximum(0.0, x - x.mean()),
    "F6": lambda x: x,                       # a felutas lepes a hurokban, nem itt
}


def normalise(w, mode, n_pairs):
    """UJ metodus. Ket normalas-alak (N1: osszeg = parszam; N2: legnagyobb = 1).
       Visszaad None-t, ha a normalas nem ertelmezheto — ez maga is lelet."""
    if mode == "N1":
        s = w.sum()
        return None if s <= 1e-14 else w * (n_pairs / s)
    m = w.max()
    return None if m <= 1e-14 else w / m


# ---------- UJ: a hitelesito probak ----------

def check(name, got, want, tol):
    ok = abs(got - want) <= tol
    print(f"  [{'OK ' if ok else 'HIBA'}] {name}: {got:.10g}  (varva {want:.10g})")
    return ok


def main():
    ok = True
    print("\n=== 0. Ketutas pecset: a szerzodes ket fuggetlen felepitese ===")
    d = max(np.abs(pair_cost_operator(4, 0, 2) - pair_cost_operator_spin(4, 0, 2)).max(),
            np.abs(pair_cost_operator(3, 1, 2) - pair_cost_operator_spin(3, 1, 2)).max())
    ok &= check("elteres a ket ut kozott", d, 0.0, 1e-14)

    print("\n=== 1. II/1 — a zart alak peldany-szinten ===")
    worst = 0.0
    for t1, t2 in [(0.3, 1.1), (0.0, 0.7), (2.0, 2.0), (0.5, -1.3)]:
        v = np.kron([np.cos(t1), np.sin(t1)], [np.cos(t2), np.sin(t2)])
        got = v @ pair_cost_operator(2, 0, 1) @ v
        worst = max(worst, abs(got - (0.5 + 0.5 * np.cos(t1 - t2) ** 2)))
    ok &= check("legnagyobb elteres L = 1/2 + 1/2 cos^2(d)-tol", worst, 0.0, 1e-13)

    print("\n=== 2. II/5 — a haromszog ===")
    n = 3
    H = hamiltonian(n, {(i, j): 1.0 for i, j in combinations(range(n), 2)})
    e, vs = ground_space(n, H)
    ok &= check("kozosen birtokolt minimum", e, 1.5, 1e-10)
    ok &= check("elfajulas", len(vs), 4, 0)
    th = 2 * np.pi / 3
    v = np.kron(np.kron([1, 0], [np.cos(th), np.sin(th)]),
                [np.cos(2 * th), np.sin(2 * th)])
    ok &= check("legjobb peldany-szintu elrendezes (15/8)", v @ H @ v, 1.875, 1e-12)

    print("\n=== 3. II/11 kontroll — tizenket objektum, mind a 66 par ===")
    n = 12
    pairs = list(combinations(range(n), 2))
    H = hamiltonian(n, {p: 1.0 for p in pairs})
    e, vs = ground_space(n, H)
    ok &= check("kotesar (egzaktul 45/66)", e / 66, 45 / 66, 1e-10)
    ok &= check("elfajulas / vetito nyoma", len(vs), 132, 0)
    I = np.array(list(proximity_map(n, vs).values()))
    ok &= check("kozelseg minden paron", I.mean(), 0.012, 5e-4)
    ok &= check("kozelseg-szorasa", I.std(), 0.0, 1e-14)

    print("\n=== 4. II/11 — a 12-es kor ===")
    ring = {(i, (i + 1) % n) if i < (i + 1) % n else ((i + 1) % n, i): 1.0
            for i in range(n)}
    e, vs = ground_space(n, hamiltonian(n, ring))
    ok &= check("kotesar", e / 12, 0.3011, 5e-4)
    P = proximity_map(n, vs)
    dist = {}
    for (i, j), val in P.items():
        dist.setdefault(min((j - i) % n, (i - j) % n), []).append(val)
    want = [0.444, 0.123, 0.066, 0.045, 0.037]
    for r in range(1, 6):
        ok &= check(f"kozelseg r={r}", float(np.mean(dist[r])), want[r - 1], 5e-4)
    print(f"   (r=6, atellenes: {np.mean(dist[6]):.4f} — jegyzetben, nincs hivatkozasi ertek)")
    ball = [1 + 2 * r for r in range(6)]
    print(f"   golyo a koron: {ball} — lepesenkent +2, egy kiterjedes")

    print("\n=== 5. NULLA-PROBA (PKG-17-1, T1): helyben marad-e a lapos allapot ===")
    n = 12
    pairs = list(combinations(range(n), 2))
    w0 = np.ones(len(pairs))
    _, vs = ground_space(n, hamiltonian(n, dict(zip(pairs, w0))))
    Iv = np.array([proximity_map(n, vs)[p] for p in pairs])
    for fname, f in FAMILY.items():
        # PKG-17-1 T1: az F5 a lapos indulobol egy korben URES-be visz, a tobbi fixpont
        expect = "URES" if fname == "F5" else "FIX"
        for mode in ("N1", "N2"):
            w1 = normalise(f(Iv), mode, len(pairs))
            if w1 is None:
                got, detail = "URES", "minden tartalom pontosan nulla — a halo megszunt"
            else:
                drift = np.abs(w1 - normalise(w0, mode, len(pairs))).max()
                got = "FIX" if drift < 1e-12 else "ELMOZDULT"
                detail = f"elmozdulas {drift:.3e}"
            good = got == expect
            print(f"  [{'OK ' if good else 'HIBA'}] {fname}/{mode}: {got} "
                  f"(varva {expect}) — {detail}")
            ok &= good

    print("\n" + "=" * 62)
    print("A KAPU: " + ("TISZTA — a szabalykonyv fagyaszthato."
                        if ok else "NEM TISZTA — a szabalykonyv javitando fagyasztas elott."))
    print("=" * 62 + "\n")


if __name__ == "__main__":
    main()
