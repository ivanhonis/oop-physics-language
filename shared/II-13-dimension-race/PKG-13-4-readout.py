# PKG-13-4 — Computation code for the readout and the size diagnosis
# Package document: PKG-13-4-readout_hu.md / _en.md (the code is language-independent)
# Part 1: the fixed run (4x4 torus, N=11, a closed degree) — the basis of the verdict
# Part 2: diagnosis (8x8 torus, N=43) — outside the fixed scope

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
    """The fixed protocol: closeness map, jump, rebuilding, ball."""
    M = n * n
    L = torus_L(n)
    w, V = np.linalg.eigh(L)
    gap = w[Nf] - w[Nf - 1]
    print(f"\n=== {label}: {n}x{n}, N={Nf}, degree gap={gap:.4f} ===")
    C = V[:, :Nf] @ V[:, :Nf].T

    # closeness classes
    cls = {}
    for i in range(M):
        for j in range(i + 1, M):
            cls.setdefault(offset(i, j, n), []).append(C[i, j])
    rank = sorted(((abs(np.mean(v)), k) for k, v in cls.items()), reverse=True)
    print("top of the closeness classes (|C|):")
    for val, k in rank[:4]:
        print(f"  displacement {k}: |C| = {val:.5f}")

    # pairwise closeness (view-based) and the jump
    def S(idx):
        return float(h(np.linalg.eigvalsh(C[np.ix_(idx, idx)])).sum())
    S1 = [S([i]) for i in range(M)]
    MI = np.zeros((M, M))
    for i in range(M):
        for j in range(i + 1, M):
            MI[i, j] = MI[j, i] = S1[i] + S1[j] - S([i, j])
    row = np.sort(MI[0][np.arange(M) != 0])[::-1]
    k = int(np.argmax(row[:-1] - row[1:])) + 1
    print("after the jump k =", k, " top of the list:", np.round(row[:6], 5))

    # rebuilding
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
    print(f"rebuilding: edges={len(edges)}, real found={len(true & edges)}/{len(true)}, "
          f"phantom={len(extra)}, missing={len(true - edges)}")
    if extra:
        print("  phantom classes:", {offset(a, b, n) for a, b in (tuple(e) for e in extra)})

    # ball growth
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
    print("ball:", sizes)

# Part 1 — the fixed run (the basis of the verdict)
readout(4, 11, "FIXED RUN")

# Part 2 — diagnosis, outside the fixed scope
readout(8, 43, "DIAGNOSIS")
