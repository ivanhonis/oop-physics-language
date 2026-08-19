# PKG-16-2 — Beat ladders (II/16)
# Builds on claims A1-A8 of PKG-16-1. 805 entrants (5 main + 8 controls +
# 792 family), streamed processing (the full ladder matrix does not fit in memory).
# Self-checks (A7): mark table by two routes | ladder classification (by digests) |
#   machine wrap-around on every entrant | trace sum 2488320 | component count |
#   wiring-uniqueness assertion.
# Two-route form (A8): (i) sparse residual check (64/16 modes, seed 248832)
#   (ii) moment cover of order<=4 everywhere (iii) dense certification on small
#   instances (iv) the projector seal runs in PKG-16-4.

# Identifier glossary — the identifiers were renamed from Hungarian
# to English; the original Hungarian name stands on the right:
#   bad = hiba                          basis = bazis
#   ceiling = plafon                    closed_ladder = zart_letra
#   coords = koord                      cos_cache = cos_tar
#   digest = kul                        digests = kivonat
#   dirs = iranyok                      dirs_of = ir
#   fam_min = cs_min                    FAMILY = CSALAD
#   global_len = globalis               global_of = gl
#   grid = racs                         half_steps = fel
#   hits = talalt                       idx_sets = idxek
#   keys = kulcs                        lam_j = lj
#   MAIN = FO                           mask = szur
#   max_residual = legmaradek           member = tag
#   moment_err = mom_hiba               mult = mm
#   multiples = tobbes                  name = nev
#   new_pts = uj                        ok_mask = jo
#   others = tobbi                      phase = ph
#   plus_minus = pm                     residual = maradek
#   sample = minta                      SEED = MAG
#   seen = lat                          shape = alak
#   SMALL = KIS                         small_dev = legkis
#   steps = lepesek                     target = cel
#   TOL = TURES                         totals = osszeg
#   trace_err = nyomhiba                TRACE_SUM = NYOM
#   walks_1d = setak_1d                 walks_nd = setak_nd
#   word_len = teljes                   wraparound_ring = korbeeres_kor
#   wraparound_torus = korbeeres_torus  wrapped = rac
#   zero_modes = nullak

import numpy as np, hashlib, time
from itertools import combinations, product
from math import gcd
from functools import reduce

NH = 12**5
TRACE_SUM = 2 * 5 * NH          # 2,488,320
TOL = 1e-8
SEED = 248832

MAIN = {
 "J1": ((NH,), [(1,),(2,),(3,),(4,),(5,)]),
 "J2": ((432,576), [(1,0),(0,1),(1,1),(1,-1),(0,2)]),
 "J3": ((54,64,72), [(1,0,0),(0,1,0),(0,0,1),(0,1,-1),(0,1,1)]),
 "J4": ((18,24,24,24), [(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1),(0,0,1,-1)]),
 "J5": ((12,)*5, [tuple(1 if i==j else 0 for i in range(5)) for j in range(5)]),
 "K1": ((48,72,72), [(1,0,0),(0,1,0),(0,0,1),(0,1,-1),(0,1,1)]),
 "K2": ((12,24,24,36), [(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1),(0,0,1,-1)]),
 "K3": ((288,864), [(1,0),(0,1),(1,1),(1,-1),(0,2)]),
 "KA2": ((432,576), [(1,0),(0,1),(1,1),(1,-1),(2,0)]),
 "KA3": ((54,64,72), [(1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,0,1)]),
 "KA4": ((18,24,24,24), [(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1),(1,0,0,-1)]),
 "KP3": ((54,64,72), [(1,0,0),(0,1,0),(0,0,1),(1,-1,-1),(1,-1,1)]),
 "KP4": ((18,24,24,24), [(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1),(0,1,1,1)]),
}
FAMILY = list(combinations(range(1, 13), 5))
SMALL = {"J1": (60,), "J2": (12,12), "J3": (12,12,12), "J4": (6,6,6,6),
       "J5": (6,)*5, "K1": (12,12,12), "K2": (6,6,6,6), "K3": (12,12),
       "KA2": (12,12), "KA3": (12,12,12), "KA4": (6,6,6,6),
       "KP3": (6,6,6), "KP4": (6,6,6,6)}

def plus_minus(half_steps):
    g = list(half_steps) + [tuple(-x for x in s) for s in half_steps]
    assert len(set(g)) == 10, "duplicated wiring"      # rule H1
    return g

def closed_ladder(shape, half_steps, dt=np.longdouble):
    r = np.meshgrid(*[(2*np.pi*np.arange(L)).astype(dt)/L for L in shape],
                    indexing="ij")
    lam = np.zeros(shape, dtype=dt)
    for s in half_steps:
        lam += 2.0 - 2.0*np.cos(sum(si*gi for si, gi in zip(s, r)))
    return np.sort(lam.ravel())

def walks_nd(half_steps, h):
    g = plus_minus(half_steps)
    return sum(1 for t in product(g, repeat=h)
               if all(x == 0 for x in map(sum, zip(*t))))

def walks_1d(steps, h):
    p = np.zeros(25); p[12] = 1.0
    e = np.zeros(25)
    for s in steps:
        e[12+s] += 1; e[12-s] += 1
    for _ in range(h):
        p = np.convolve(p, e)
    return int(round(p[len(p)//2]))

def wraparound_ring(steps, target):
    """Minimum word length producing the target; the non-maximal coefficients
    are bounded by an exchange argument to < 12."""
    e = steps[-1]
    others = np.array(steps[:-1])
    grid = np.array(np.meshgrid(*[np.arange(-11, 12)]*len(others),
                                indexing="ij")).reshape(len(others), -1)
    totals = others @ grid
    residual = target - totals
    ok_mask = residual % e == 0
    word_len = np.abs(grid).sum(axis=0) + np.abs(residual // e)
    return int(word_len[ok_mask].min())

def wraparound_torus(shape, half_steps, ceiling):
    gens = np.array(plus_minus(half_steps))
    dim = len(shape)
    OFF = 2*ceiling + 4
    basis = OFF**np.arange(dim)
    front = np.zeros((1, dim), dtype=np.int64)
    seen = {0}
    dirs, global_len = {}, None
    for m in range(1, ceiling+1):
        new_pts = (front[:, None, :] + gens[None, :, :]).reshape(-1, dim)
        keys = new_pts @ basis
        _, idx = np.unique(keys, return_index=True)
        new_pts = new_pts[idx]
        mask = [k not in seen for k in (new_pts @ basis)]
        new_pts = new_pts[mask]
        for k in (new_pts @ basis):
            seen.add(int(k))
        wrapped = new_pts % np.array(shape)
        hits = np.all(wrapped == 0, axis=1)
        for p in new_pts[hits]:
            mult = p // np.array(shape)
            if np.any(mult):
                if global_len is None:
                    global_len = m
                nz = np.nonzero(mult)[0]
                if len(nz) == 1:
                    dirs.setdefault(int(nz[0]), m)
        front = new_pts
        if global_len is not None and len(dirs) == dim:
            break
    return dirs, global_len

def main():
    t0 = time.time()
    print("== PKG-16-2 — ladders (805 entrants, streamed) ==")
    digests, trace_err, zero_modes = {}, 0.0, {}
    moment_err = 0.0
    for name, (shape, half_steps) in MAIN.items():
        lam = closed_ladder(shape, half_steps)
        trace_err = max(trace_err, abs(float(lam.sum()) - TRACE_SUM))
        zero_modes[name] = int((lam < TOL).sum())
        a = 10.0 - lam
        m3, m4 = float((a**3).mean()), float((a**4).mean())
        k3, k4 = walks_nd(half_steps, 3), walks_nd(half_steps, 4)
        moment_err = max(moment_err, abs(m3-k3), abs(m4-k4))
        digest = hashlib.md5(np.round(lam.astype(np.float64)/TOL)
                          .astype(np.int64).tobytes()).hexdigest()
        digests.setdefault(digest, []).append(name)
    kk = (2*np.pi*np.arange(NH)).astype(np.longdouble)/NH
    cos_cache = {s: 2.0-2.0*np.cos(s*kk) for s in range(1, 13)}
    for member in FAMILY:
        lam = np.sort(sum(cos_cache[s] for s in member))
        trace_err = max(trace_err, abs(float(lam.sum()) - TRACE_SUM))
        zero_modes[str(member)] = int((lam < TOL).sum())
        a = 10.0 - lam
        m3, m4 = float((a**3).mean()), float((a**4).mean())
        moment_err = max(moment_err, abs(m3-walks_1d(member,3)), abs(m4-walks_1d(member,4)))
        digest = hashlib.md5(np.round(lam.astype(np.float64)/TOL)
                          .astype(np.int64).tobytes()).hexdigest()
        digests.setdefault(digest, []).append(str(member))
    print("ladders + moment cover (order<=4, on all 805): largest "
          "deviation %.2e; trace-sum error %.2e  (%.0f s)"
          % (moment_err, trace_err, time.time()-t0))

    # component count against the disconnection table
    bad = [n for n in MAIN if zero_modes[n] != 1]
    for member in FAMILY:
        g = gcd(reduce(gcd, member), NH)
        if zero_modes[str(member)] != g:
            bad.append(str(member))
    print("component count: %s" % ("HOLDS" if not bad else "FAILS: %s" % bad[:5]))

    multiples = [o for o in digests.values() if len(o) > 1]
    print("ladder classes: %d classes on %d entrants; coincidences: %s"
          % (len(digests), 13+len(FAMILY), multiples if multiples else "none"))

    # machine wrap-around
    t1 = time.time()
    print("wrap-around — the named networks (per direction | global):")
    for name, (shape, half_steps) in MAIN.items():
        if len(shape) == 1:
            g = wraparound_ring([1,2,3,4,5], NH)
            print("   %-4s [%d] | %d" % (name, g, g))
        else:
            dirs_of, global_of = wraparound_torus(shape, half_steps, max(shape)+4)
            print("   %-4s %s | %d — %s" % (name, sorted(dirs_of.values()), global_of,
                  "holds" if global_of >= 8 else "FAILS"))
    fam_min = min(wraparound_ring(list(t), NH) if gcd(reduce(gcd,t),NH) == 1
                 else wraparound_ring([s//2 for s in t], NH//2)
                 for t in FAMILY)
    print("wrap-around — family: the shortest is %d (measured on the copy for the "
          "disconnected ones) — %s (%.0f s)"
          % (fam_min, "holds" if fam_min >= 8 else "FAILS", time.time()-t1))

    # (i) sparse residual check
    t2 = time.time()
    rng = np.random.default_rng(SEED)
    sample = [FAMILY[i] for i in sorted(rng.choice(len(FAMILY), 24, replace=False))]
    max_residual = 0.0
    for name, (shape, half_steps) in MAIN.items():
        Nn = int(np.prod(shape))
        coords = np.array(np.unravel_index(np.arange(Nn), shape)).T
        # the neighbour indices are the same for every mode — built once
        idx_sets = [np.ravel_multi_index(((coords + s) % np.array(shape)).T, shape)
                 for s in plus_minus(half_steps)]
        for _ in range(64):
            n = np.array([rng.integers(0, L) for L in shape])
            # exact phase: integer remainder per axis, only then floating point
            phase = sum(((n[j]*coords[:, j]) % shape[j]) / shape[j]
                     for j in range(len(shape)))
            v = np.exp(2j*np.pi*phase)
            Av = np.zeros(Nn, dtype=complex)
            for ix in idx_sets:
                Av += v[ix]
            # the correct beat formula: the phase is the product with the wiring vector
            lam_j = float(sum(2-2*np.cos(2*np.pi*sum(ni*si/L for ni, si, L
                       in zip(n, s, shape))) for s in half_steps))
            max_residual = max(max_residual,
                             float(np.max(np.abs(10*v - Av - lam_j*v))))
    x = np.arange(NH)
    for member in sample:
        idx_sets = [(x + s) % NH for s in list(member)+[-s for s in member]]
        for _ in range(16):
            n = int(rng.integers(0, NH))
            v = np.exp(2j*np.pi*((n*x) % NH)/NH)
            Av = np.zeros(NH, dtype=complex)
            for ix in idx_sets:
                Av += v[ix]
            lam_j = float(sum(2-2*np.cos(2*np.pi*n*s/NH) for s in member))
            max_residual = max(max_residual,
                             float(np.max(np.abs(10*v - Av - lam_j*v))))
    print("(i) sparse residual check (13x64 + 24x16 modes, seed %d): "
          "largest residual %.2e  (%.0f s)"
          % (SEED, max_residual, time.time()-t2))

    # (iii) dense certification on small instances
    t3 = time.time()
    small_dev = 0.0
    for name, shape in SMALL.items():
        half_steps = MAIN[name][1]
        Nk = int(np.prod(shape))
        coords = np.array(np.unravel_index(np.arange(Nk), shape)).T
        Lap = np.zeros((Nk, Nk))
        Lap[np.arange(Nk), np.arange(Nk)] = 10.0
        for s in plus_minus(half_steps):
            target = np.ravel_multi_index(((coords + s) % np.array(shape)).T, shape)
            Lap[np.arange(Nk), target] -= 1.0
        w = np.linalg.eigvalsh(Lap)
        small_dev = max(small_dev, float(np.max(np.abs(
            np.sort(w) - closed_ladder(shape, half_steps, np.float64)))))
    print("(iii) dense certification on small instances (13 patterns): largest "
          "deviation %.2e  (%.0f s)" % (small_dev, time.time()-t3))
    print("TOTAL: %.0f s" % (time.time()-t0))

if __name__ == "__main__":
    main()
