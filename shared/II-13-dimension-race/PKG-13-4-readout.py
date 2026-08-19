# PKG-13-4 — A kiolvasas es a meret-diagnozis szamolo kodja
# Csomag-dokumentum: PKG-13-4-readout_hu.md (a kod nyelvfuggetlen)
# 1. resz: a rogzitett futas (4x4 torusz, N=11, zart fok) — az itelet alapja
# 2. resz: diagnozis (8x8 torusz, N=43) — a rogzitett hatokoron kivul

import numpy as np

def torus_L(n):
    M = n * n
    L = np.zeros((M, M))
    for x in range(n):
        for y in range(n):
            i = n * x + y
            for j in (n * ((x + 1) % n) + y, n * ((x - 1) % n) + y,
                      n * x + (y + 1) % n, n * x + (y - 1) % n):
                L[i, j] -= 1
            L[i, i] = 4
    return L

def offset(i, j, n):
    xi, yi, xj, yj = i // n, i % n, j // n, j % n
    dx = min((xi - xj) % n, (xj - xi) % n)
    dy = min((yi - yj) % n, (yj - yi) % n)
    return tuple(sorted((dx, dy)))

def h(p):
    p = np.clip(p, 1e-15, 1 - 1e-15)
    return -(p * np.log(p) + (1 - p) * np.log(1 - p))

def readout(n, Nf, label):
    """A rogzitett jegyzokonyv: kozelseg-terkep, ugras, visszarakas, golyo."""
    M = n * n
    L = torus_L(n)
    w, V = np.linalg.eigh(L)
    gap = w[Nf] - w[Nf - 1]
    print(f"\n=== {label}: {n}x{n}, N={Nf}, fokkoz={gap:.4f} ===")
    C = V[:, :Nf] @ V[:, :Nf].T

    # kozelseg-osztalyok
    cls = {}
    for i in range(M):
        for j in range(i + 1, M):
            cls.setdefault(offset(i, j, n), []).append(C[i, j])
    rank = sorted(((abs(np.mean(v)), k) for k, v in cls.items()), reverse=True)
    print("kozelseg-osztalyok teteje (|C|):")
    for val, k in rank[:4]:
        print(f"  eltolas {k}: |C| = {val:.5f}")

    # paros kozelseg (nezet-alapu) es ugras
    def S(idx):
        return float(h(np.linalg.eigvalsh(C[np.ix_(idx, idx)])).sum())
    S1 = [S([i]) for i in range(M)]
    MI = np.zeros((M, M))
    for i in range(M):
        for j in range(i + 1, M):
            MI[i, j] = MI[j, i] = S1[i] + S1[j] - S([i, j])
    row = np.sort(MI[0][np.arange(M) != 0])[::-1]
    k = int(np.argmax(row[:-1] - row[1:])) + 1
    print("ugras utan k =", k, " a lista teteje:", np.round(row[:6], 5))

    # visszarakas
    edges = set()
    for i in range(M):
        for t in [j for j in np.argsort(-MI[i]) if j != i][:k]:
            edges.add(frozenset((i, t)))
    true = set()
    for x in range(n):
        for y in range(n):
            i = n * x + y
            for j in (n * ((x + 1) % n) + y, n * x + (y + 1) % n):
                true.add(frozenset((i, j)))
    extra = edges - true
    print(f"visszarakas: elek={len(edges)}, valodi megvan={len(true & edges)}/{len(true)}, "
          f"fantom={len(extra)}, hianyzo={len(true - edges)}")
    if extra:
        print("  fantom-osztalyok:", {offset(a, b, n) for a, b in (tuple(e) for e in extra)})

    # golyonovekedes
    adj = {i: set() for i in range(M)}
    for e in edges:
        a, b = tuple(e)
        adj[a].add(b)
        adj[b].add(a)
    seen, frontier, sizes = {0}, {0}, [1]
    for _ in range(2 * n):
        frontier = set(x for f in frontier for x in adj[f]) - seen
        if not frontier:
            break
        seen |= frontier
        sizes.append(len(seen))
    print("golyo:", sizes)

# 1. resz — a rogzitett futas (az itelet alapja)
readout(4, 11, "ROGZITETT FUTAS")

# 2. resz — diagnozis, a rogzitett hatokoron kivul
readout(8, 43, "DIAGNOZIS")
