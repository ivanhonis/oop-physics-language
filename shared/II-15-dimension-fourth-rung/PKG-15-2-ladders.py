# PKG-15-2 — Beat ladders (II/15)
# Builds on the outgoing claims of PKG-15-1 (A1-A8). Its business:
#   1) building the field: J1-J4, K1-K4, and all 495 members of the line family
#   2) the ladder by the closed Fourier route on all 503 networks
#   3) self-checks (A7): (i) three distinctness marks on the main four;
#      (ii) ladder classification over the full field with a fixed tolerance;
#      (iii) machine wrap-around traversal on every entrant; (iv) trace sum 165888;
#      (v) component count against the disconnection table
#   4) machine route (A8): dense eigenproblem on the 8 main/control networks +
#      24 drawn family members (seed: 20736); restartable — finished networks
#      are skipped. Memory need ~8 GB per network; runtime ~15-20 min/network.
# Usage:  python3 PKG-15-2-ladders.py [--gep N]
#   --gep N : run at most N machine eigenproblems in this run
#             (default: all remaining). --gep 0 runs only the fast part;
#             the batch can be continued later.

# Identifier glossary — the identifiers were renamed from Hungarian
# to English; the original Hungarian name stands on the right:
#   bad = rossz                         bad_v = hiba_v
#   bipartite = paros                   BIPARTITE_MAIN = PAROS_FO
#   by_digest = kulcsok                 CACHE_DIR = GYORSITO
#   ceiling = plafon                    classes = osztalyok
#   closed_ladder = zart_letra          cosines = cosok
#   counter = szamlalo                  depth = melyseg
#   dev = elt                           digest = kulcs
#   dir_target = iranycel               dirs = irany
#   done = kesz                         even_ok = paros_all
#   expected3 = vart3                   expected4 = vart4
#   fam_mark_bad = cs_jegyu_hiba        fam_min = cs_min
#   fam_odd = cs_paratlan               FAMILY = CSALAD
#   global_len = globalis               grids = racsok
#   half_steps = fel                    have = megvan
#   high = felso                        index_of = sorszam
#   J2_STEPS = J2LEP                    J3_STEPS = J3LEP
#   ladders = letrak                    low = also
#   machine_ladder = gepi_letra         machine_limit = gep_limit
#   MAIN = FO                           matches = egyezik
#   member = tag                        multiples = tobbes
#   name = nev                          needs_even = paros_kell
#   new_front = ujf                     new_reach = uj
#   ok_here = rendben                   ok_i = okI
#   ok_iii = iii_ok                     phase = fazis
#   reach = el                          remaining = hatra
#   sample = minta                      SEED = MAG
#   seen = lat                          selftest_dev = proba_elt
#   shape = alak                        shape_p = alak_p
#   shortest = legrov                   sign_variants = elojelek
#   sites = helyek                      span = hossz
#   steps = lepesek                     steps_p = fel_p
#   target = cel                        targets = celok
#   to_run = futtat                     TOL_CLASS = TURES_OSZTALY
#   TRACE_SUM = NYOM                    unit = egyseg
#   UNIT4 = EGYSEG4                     worst = legrosszabb
#   wraparound_ring = korbeeres_kor     wraparound_torus = korbeeres_torus
#   zero_modes = nullak

import numpy as np
import os, sys, time
from itertools import combinations, product
from collections import deque
from math import gcd
from functools import reduce

N = 20736
TRACE_SUM = 2 * 4 * N            # 165888 — the cover of the trace tie
TOL_CLASS = 1e-8        # ladder classification quantum (fixed)
SEED = 20736                 # random seed (fixed; numpy PCG64)
CACHE_DIR = "letrak_gepi"    # cache of the machine leg (for restarting)

# ----------------------------------------------------------------- field ---
def sign_variants(v):
    idx = [i for i, x in enumerate(v) if x]
    out = []
    for s in product([1, -1], repeat=len(idx)):
        w = list(v)
        for k, i in enumerate(idx):
            w[i] = v[i] * s[k]
        out.append(tuple(w))
    return out

UNIT4 = [(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)]
J3_STEPS = [(1,0,0),(0,1,0),(0,0,1),(1,-1,-1)]
J2_STEPS = [(1,0),(0,1),(1,1),(1,-1)]

MAIN = {  # name -> (shape, half-steps); the full step set arises with the +- pairs
    "J1": ((N,),           [(1,),(2,),(3,),(4,)]),
    "J2": ((144,144),      J2_STEPS),
    "J3": ((24,24,36),     J3_STEPS),
    "J4": ((12,12,12,12),  UNIT4),
    "K1": ((16,36,36),     J3_STEPS),
    "K2": ((12,36,48),     J3_STEPS),
    "K3": ((8,8,18,18),    UNIT4),
    "K4": ((48,432),       J2_STEPS),
}
BIPARTITE_MAIN = {"J3", "J4", "K1", "K2", "K3"}   # the main/control networks carrying the bipartite mark
FAMILY = list(combinations(range(1, 13), 4))  # 495 members

# -------------------------------------------------- closed Fourier ladder ---
def closed_ladder(shape, half_steps):
    grids = np.meshgrid(*[2*np.pi*np.arange(L)/L for L in shape], indexing="ij")
    lam = np.zeros(shape)
    for s in half_steps:
        phase = sum(si * gi for si, gi in zip(s, grids))
        lam += 2.0 - 2.0*np.cos(phase)
    return np.sort(lam.ravel())

# ------------------------------------- (iii) machine wrap-around traversal ---
def wraparound_ring(steps, Nk):
    """1D banded BFS: the shortest word length producing +-Nk.
    The band [-13, Nk+13] is enough: the steps can be rearranged so that the
    partial sum never leaves it (every step <= 12)."""
    low, high = -13, Nk + 13
    span = high - low + 1
    reach = np.zeros(span, dtype=bool)
    reach[-low] = True
    target = Nk - low
    depth = 0
    ceiling = Nk // min(steps) + 20
    while depth <= ceiling:
        if reach[target]:
            return depth
        new_reach = np.zeros(span, dtype=bool)
        for s in steps:
            new_reach[s:] |= reach[:-s]     # +s step
            new_reach[:-s] |= reach[s:]     # -s step
        reach = new_reach
        depth += 1
    return None

def wraparound_torus(shape, half_steps, ceiling):
    """BFS in Z^k from 0; targets: the +-w_j envelope basis vectors, and the first
    nonzero envelope point (the globally shortest wrapping loop up to the ceiling)."""
    gens = []
    for s in half_steps:
        gens += [s, tuple(-x for x in s)]
    dim = len(shape)
    start = (0,)*dim
    seen = {start}
    front = [start]
    dir_target = {}
    global_len = None
    for depth in range(1, ceiling+1):
        new_front = []
        for p in front:
            for g in gens:
                q = tuple(a+b for a, b in zip(p, g))
                if q in seen:
                    continue
                seen.add(q)
                new_front.append(q)
                if all(qi % L == 0 for qi, L in zip(q, shape)):
                    m = tuple(qi // L for qi, L in zip(q, shape))
                    if any(m):
                        if global_len is None:
                            global_len = depth
                        for j in range(dim):
                            unit = [0]*dim
                            unit[j] = 1
                            if tuple(np.abs(m)) == tuple(unit):
                                dir_target.setdefault(j, depth)
        front = new_front
        if global_len is not None and len(dir_target) == dim:
            break
    return dir_target, global_len

# ---------------------------------------------- machine route: dense builder ---
def machine_ladder(shape, half_steps):
    """Building the network and a dense eigenproblem — a route independent of the closed one."""
    Nh = int(np.prod(shape))
    Lap = np.zeros((Nh, Nh))
    sites = list(np.ndindex(*shape))
    index_of = {h: i for i, h in enumerate(sites)}
    for h in sites:
        a = index_of[h]
        Lap[a, a] = 2 * len(half_steps)
        for s in half_steps:
            b = index_of[tuple((x+y) % L for x, y, L in zip(h, s, shape))]
            Lap[a, b] -= 1.0
            Lap[b, a] -= 1.0
    return np.linalg.eigvalsh(Lap)

# =================================================================== run ---
def main():
    machine_limit = None
    if "--gep" in sys.argv:
        machine_limit = int(sys.argv[sys.argv.index("--gep")+1])

    t0 = time.time()
    print("== PKG-15-2 — ladders ==")

    # -- closed ladders: main + control --
    ladders = {}
    for name, (shape, half_steps) in MAIN.items():
        ladders[name] = closed_ladder(shape, half_steps)
    # -- closed ladders: family --
    k = 2.0*np.pi*np.arange(N)/N
    cosines = {s: 2.0 - 2.0*np.cos(s*k) for s in range(1, 13)}
    for member in FAMILY:
        ladders[str(member)] = np.sort(cosines[member[0]]+cosines[member[1]]+cosines[member[2]]+cosines[member[3]])
    print("closed ladders: %d networks, %.1f s" % (len(ladders), time.time()-t0))

    # -- (iv) trace sum --
    bad = [n for n, l in ladders.items() if abs(l.sum()-TRACE_SUM) > 1e-6]
    print("(iv) trace sum 165888 everywhere:", "HOLDS" if not bad else "FAILS: %s" % bad)

    # -- (i) three marks on the main four (from the ladder: a = 8 - lambda) --
    # CORRECTION (the II/14 precedent): the J2 row of the table of PKG-15-1 §5
    # was wrong (48 / 1188) — the source enumeration built the diagonal steps
    # twice (a multigraph). The correct values are 24 / 216. The separation of
    # the six pairs is complete as before: the cross pairs are decided by the
    # bipartite mark, the J1-J2 pair by the 3-walks (36 != 24), and the J3-J4
    # pair by the 4-walks (216 != 168); the J2-J3 4-walk agreement (216 = 216)
    # is harmless, because that pair is separated by the bipartite mark.
    expected3 = {"J1": 36, "J2": 24, "J3": 0, "J4": 0}
    expected4 = {"J1": 296, "J2": 216, "J3": 216, "J4": 168}
    ok_i = True
    for name in ("J1","J2","J3","J4"):
        a = 8.0 - ladders[name]
        m3, m4, m5 = (a**3).mean(), (a**4).mean(), (a**5).mean()
        bipartite = abs(m3) < 1e-6 and abs(m5) < 1e-6
        matches = (abs(m3-expected3[name]) < 1e-6 and abs(m4-expected4[name]) < 1e-6
                   and bipartite == (name in ("J3","J4")))
        ok_i &= matches
        print("(i) %s: 3-walks %.6f (expected %d), 4-walks %.6f (expected %d), "
              "bipartite mark %s — %s" % (name, m3, expected3[name], m4, expected4[name],
              "present" if bipartite else "none", "holds" if matches else "FAILS"))
    if ok_i:
        print("(i) CORRECTION recorded: the J2 row of PKG-15-1 §5 (48/1188) was")
        print("    wrong — diagonal steps built twice in the source enumeration;")
        print("    correctly 24/216. The separation of the six pairs still holds.")

    # -- (v) component count against the disconnection table --
    zero_modes = {n: int((l < 1e-8).sum()) for n, l in ladders.items()}
    bad_v = []
    for name in MAIN:
        if zero_modes[name] != 1:
            bad_v.append(name)
    counter = {1: 0, 2: 0, 3: 0}
    for member in FAMILY:
        g = gcd(reduce(gcd, member), N)
        if zero_modes[str(member)] != g:
            bad_v.append(str(member))
        counter[g] += 1
    print("(v) component count: main/control all 1; family %s — %s"
          % (counter, "HOLDS" if not bad_v else "FAILS: %s" % bad_v[:5]))

    # -- (ii) ladder classification over the full field --
    by_digest = {}
    for name, l in ladders.items():
        digest = np.round(l / TOL_CLASS).astype(np.int64).tobytes()
        by_digest.setdefault(digest, []).append(name)
    classes = list(by_digest.values())
    multiples = [o for o in classes if len(o) > 1]
    print("(ii) ladder classes: %d classes on %d networks; coincidences: %s"
          % (len(classes), len(ladders), multiples if multiples else "none"))

    # -- (iii) machine wrap-around traversal --
    print("(iii) wrap-around — main and control networks:")
    ok_iii = True
    for name, (shape, half_steps) in MAIN.items():
        if len(shape) == 1:
            g = wraparound_ring([s[0] for s in half_steps], shape[0])
            dirs, global_len = {0: g}, g
        else:
            dirs, global_len = wraparound_torus(shape, half_steps, max(shape)+6)
        shortest = min(min(dirs.values()), global_len)
        needs_even = name in BIPARTITE_MAIN
        even_ok = all(v % 2 == 0 for v in dirs.values()) and global_len % 2 == 0
        ok_here = shortest >= 8 and (even_ok or not needs_even)
        ok_iii &= ok_here
        print("   %s: per direction %s, global shortest %d — %s"
              % (name, sorted(dirs.values()), global_len, "holds" if ok_here else "FAILS"))
    # family: wrap-around = min word length for +-N; parity only to be noted
    t1 = time.time()
    fam_min, fam_odd, fam_mark_bad = 10**9, 0, []
    for member in FAMILY:
        g = wraparound_ring(list(member), N)
        fam_min = min(fam_min, g)
        if g % 2 == 1:
            fam_odd += 1
            if all(s % 2 == 1 for s in member):   # forbidden for a bipartite member
                fam_mark_bad.append(member)
    print("(iii) family: shortest wrap-around %d (>= 8: %s); members with odd "
          "wrap-around %d — bipartite (all-odd-step) among them: %d (%.0f s)"
          % (fam_min, "holds" if fam_min >= 8 else "FAILS", fam_odd,
             len(fam_mark_bad), time.time()-t1))
    if fam_odd:
        print("   CORRECTION (the II/14 precedent): the even-wrap-around condition")
        print("   of PKG-15-1 §3 protects the bipartite mark; its literal form was")
        print("   too broad for the non-bipartite family members — it is obligatory")
        print("   on the bipartite entrants (all hold), on the rest only the >= 8.")

    # -- (A8) machine route: dense eigenproblem, restartable --
    rng = np.random.default_rng(SEED)
    sample = [FAMILY[i] for i in sorted(rng.choice(len(FAMILY), 24, replace=False))]
    targets = list(MAIN.keys()) + [str(t) for t in sample]
    os.makedirs(CACHE_DIR, exist_ok=True)
    done = {c for c in targets if os.path.exists(os.path.join(CACHE_DIR, c+".npy"))}
    remaining = [c for c in targets if c not in done]
    print("(A8) machine leg: %d/%d done; drawn members (seed %d): %s..."
          % (len(done), len(targets), SEED, sample[:3]))
    # self-test of the machine builder on small weaves (always before starting the batch)
    selftest_dev = 0.0
    for shape_p, steps_p in [((6, 6), J2_STEPS), ((4, 4, 6), J3_STEPS),
                          ((4, 4, 4, 4), UNIT4)]:
        d = float(np.max(np.abs(machine_ladder(shape_p, steps_p)
                                - closed_ladder(shape_p, steps_p))))
        selftest_dev = max(selftest_dev, d)
    print("(A8) self-test of the machine builder on 3 small weaves: largest deviation %.2e"
          % selftest_dev)
    assert selftest_dev < 1e-10
    to_run = remaining if machine_limit is None else remaining[:machine_limit]
    worst = 0.0
    for c in to_run:
        shape, half_steps = MAIN[c] if c in MAIN else ((N,), [(s,) for s in eval(c)])
        t2 = time.time()
        w = machine_ladder(shape, half_steps)
        np.save(os.path.join(CACHE_DIR, c+".npy"), w)
        dev = float(np.max(np.abs(np.sort(w) - ladders[c])))
        worst = max(worst, dev)
        print("   %s: machine route done, deviation from the closed one %.2e (%.0f min)"
              % (c, dev, (time.time()-t2)/60))
    # summary from the cache
    have = [c for c in targets if os.path.exists(os.path.join(CACHE_DIR, c+".npy"))]
    if len(have) == len(targets):
        for c in targets:
            w = np.load(os.path.join(CACHE_DIR, c+".npy"))
            worst = max(worst, float(np.max(np.abs(np.sort(w)-ladders[c]))))
        print("(A8) COMPLETE: all %d targets by two routes; largest deviation %.2e"
              % (len(targets), worst))
        print("== PKG-15-2 VERDICT: the five self-checks above and A8 together decide ==")
    else:
        print("(A8) PENDING: %d machine eigenproblems are still missing — the verdict"
              " of the package closes after the batch finishes (re-running the"
              " script continues it)." % (len(targets)-len(have)))

if __name__ == "__main__":
    main()
