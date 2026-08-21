"""
PKG-17-2 — VERIFICATION PART (before the loop)
Package document: PKG-17-1-rulebook_hu.md / _en.md, section 6 (B3 precondition)
+ section 11, A3/A7

This file does NOT contain the loop. It only checks that the machinery gives
the same numbers as the chapters that have already run:
  - II/1  : the closed form of the bond contract (instance level)
  - II/5  : triangle — 15/8 at instance level, 3/2 jointly, fourfold degeneracy
  - II/11 : full-network control — 45/66, degeneracy 132, closeness spread 1e-16
  - II/11 : the 12-ring — 0.3011, closenesses 0.444 / 0.123 / 0.066 / 0.045 / 0.037
  - PKG-17-1 T1 : the flat state is a fixed point — except for F5, where it is
    EMPTY (the zero test)
"""

import numpy as np
from itertools import combinations

LN2 = np.log(2.0)


# ---------- NEW: building the contract from the form of the language ----------

def pair_cost_operator(n, i, j):
    """NEW method. The operator of the bond contract on a pair, directly from the
       form of I/8: L = a^2 + d^2 + 1/2 (b+c)^2 on the weights
       (0,0),(0,1),(1,0),(1,1). The first computation route."""
    dim = 1 << n
    M = np.zeros((dim, dim))
    bi, bj = 1 << (n - 1 - i), 1 << (n - 1 - j)
    for s in range(dim):
        vi, vj = (s & bi) != 0, (s & bj) != 0
        if vi == vj:
            M[s, s] += 1.0                    # a^2 and d^2
        else:
            M[s, s] += 0.5                    # 1/2 b^2, 1/2 c^2
            M[s, s ^ bi ^ bj] += 0.5          # the cross term: b*c
    return M


def pair_cost_operator_spin(n, i, j):
    """NEW method. The same by a second, independent route: in the form 3/4 + S_i.S_j.
       The first element of the two-route rule (PKG-17-1, A7)."""
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
    """NEW method. The full cost operator from a given content vector.
       weights: {(i,j): w} — only the nonzero contents."""
    dim = 1 << n
    H = np.zeros((dim, dim))
    for (i, j), w in weights.items():
        if w != 0.0:
            H += w * pair_cost_operator(n, i, j)
    return H


# ---------- NEW: ground state in magnetization blocks ----------

def ground_space(n, H, tol=1e-9):
    """NEW method. The subspace of smallest cost, computed block by block.
       Returns: (minimum, list of state vectors in the full space)."""
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


# ---------- NEW: the closeness measure (II/11) ----------

def reduced(vecs, n, sites):
    """NEW method. Partial state from the even mixture of the zero-cost subspace
       (the control method of II/11: an exact projector when degenerate)."""
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
    """NEW method. Von Neumann entropy, natural based (the 0.69 = ln2 mark of II/11)."""
    w = np.linalg.eigvalsh(rho)
    w = w[w > 1e-13]
    return float(-(w * np.log(w)).sum())


def proximity_map(n, vecs):
    """NEW method. Pairwise closeness: how much more the joint view knows."""
    s1 = [entropy(reduced(vecs, n, [a])) for a in range(n)]
    return {(i, j): s1[i] + s1[j] - entropy(reduced(vecs, n, [i, j]))
            for i, j in combinations(range(n), 2)}


# ---------- NEW: the family of the generating rule (PKG-17-1, section 4) ----------

FAMILY = {
    "F1": lambda x: x,
    "F2": lambda x: x ** 2,
    "F3": lambda x: np.sqrt(x),
    "F4": lambda x: x / (1.0 + x),
    "F5": lambda x: np.maximum(0.0, x - x.mean()),
    "F6": lambda x: x,                       # the halfway step lives in the loop, not here
}


def normalise(w, mode, n_pairs):
    """NEW method. Two normalization forms (N1: sum = pair count; N2: largest = 1).
       Returns None if the normalization is meaningless — which is itself a finding."""
    if mode == "N1":
        s = w.sum()
        return None if s <= 1e-14 else w * (n_pairs / s)
    m = w.max()
    return None if m <= 1e-14 else w / m


# ---------- NEW: the verification checks ----------

def check(name, got, want, tol):
    ok = abs(got - want) <= tol
    print(f"  [{'OK ' if ok else 'FAIL'}] {name}: {got:.10g}  (expected {want:.10g})")
    return ok


def main():
    ok = True
    print("\n=== 0. Two-route seal: two independent constructions of the contract ===")
    d = max(np.abs(pair_cost_operator(4, 0, 2) - pair_cost_operator_spin(4, 0, 2)).max(),
            np.abs(pair_cost_operator(3, 1, 2) - pair_cost_operator_spin(3, 1, 2)).max())
    ok &= check("deviation between the two routes", d, 0.0, 1e-14)

    print("\n=== 1. II/1 — the closed form at instance level ===")
    worst = 0.0
    for t1, t2 in [(0.3, 1.1), (0.0, 0.7), (2.0, 2.0), (0.5, -1.3)]:
        v = np.kron([np.cos(t1), np.sin(t1)], [np.cos(t2), np.sin(t2)])
        got = v @ pair_cost_operator(2, 0, 1) @ v
        worst = max(worst, abs(got - (0.5 + 0.5 * np.cos(t1 - t2) ** 2)))
    ok &= check("largest deviation from L = 1/2 + 1/2 cos^2(d)", worst, 0.0, 1e-13)

    print("\n=== 2. II/5 — the triangle ===")
    n = 3
    H = hamiltonian(n, {(i, j): 1.0 for i, j in combinations(range(n), 2)})
    e, vs = ground_space(n, H)
    ok &= check("jointly owned minimum", e, 1.5, 1e-10)
    ok &= check("degeneracy", len(vs), 4, 0)
    th = 2 * np.pi / 3
    v = np.kron(np.kron([1, 0], [np.cos(th), np.sin(th)]),
                [np.cos(2 * th), np.sin(2 * th)])
    ok &= check("best instance-level arrangement (15/8)", v @ H @ v, 1.875, 1e-12)

    print("\n=== 3. II/11 control — twelve objects, all 66 pairs ===")
    n = 12
    pairs = list(combinations(range(n), 2))
    H = hamiltonian(n, {p: 1.0 for p in pairs})
    e, vs = ground_space(n, H)
    ok &= check("bond price (exactly 45/66)", e / 66, 45 / 66, 1e-10)
    ok &= check("degeneracy / trace of the projector", len(vs), 132, 0)
    I = np.array(list(proximity_map(n, vs).values()))
    ok &= check("closeness on every pair", I.mean(), 0.012, 5e-4)
    ok &= check("spread of the closeness", I.std(), 0.0, 1e-14)

    print("\n=== 4. II/11 — the 12-ring ===")
    ring = {(i, (i + 1) % n) if i < (i + 1) % n else ((i + 1) % n, i): 1.0
            for i in range(n)}
    e, vs = ground_space(n, hamiltonian(n, ring))
    ok &= check("bond price", e / 12, 0.3011, 5e-4)
    P = proximity_map(n, vs)
    dist = {}
    for (i, j), val in P.items():
        dist.setdefault(min((j - i) % n, (i - j) % n), []).append(val)
    want = [0.444, 0.123, 0.066, 0.045, 0.037]
    for r in range(1, 6):
        ok &= check(f"closeness r={r}", float(np.mean(dist[r])), want[r - 1], 5e-4)
    print(f"   (r=6, antipodal: {np.mean(dist[6]):.4f} — a note, no reference value)")
    ball = [1 + 2 * r for r in range(6)]
    print(f"   ball on the ring: {ball} — +2 per step, one extension")

    print("\n=== 5. ZERO TEST (PKG-17-1, T1): does the flat state stay in place ===")
    n = 12
    pairs = list(combinations(range(n), 2))
    w0 = np.ones(len(pairs))
    _, vs = ground_space(n, hamiltonian(n, dict(zip(pairs, w0))))
    Iv = np.array([proximity_map(n, vs)[p] for p in pairs])
    for fname, f in FAMILY.items():
        # PKG-17-1 T1: from the flat start F5 goes to EMPTY in one round, the rest are fixed points
        expect = "EMPTY" if fname == "F5" else "FIX"
        for mode in ("N1", "N2"):
            w1 = normalise(f(Iv), mode, len(pairs))
            if w1 is None:
                got, detail = "EMPTY", "every content is exactly zero — the network has ceased"
            else:
                drift = np.abs(w1 - normalise(w0, mode, len(pairs))).max()
                got = "FIX" if drift < 1e-12 else "MOVED"
                detail = f"drift {drift:.3e}"
            good = got == expect
            print(f"  [{'OK ' if good else 'FAIL'}] {fname}/{mode}: {got} "
                  f"(expected {expect}) — {detail}")
            ok &= good

    print("\n" + "=" * 62)
    print("THE GATE: " + ("CLEAN — the rulebook can be frozen."
                          if ok else "NOT CLEAN — the rulebook must be corrected before freezing."))
    print("=" * 62 + "\n")


if __name__ == "__main__":
    main()
