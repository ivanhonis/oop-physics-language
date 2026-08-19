# PKG-16-3 — The race (II/16)
# Builds on the ladders of PKG-16-2, with streamed top-2 tracking (the full
# cost matrix does not fit in memory). Primary route: extended precision (rule H3).
# Its business: the four-rung staircase verdict on the quintuple J1-J5 (with the
# named turn-back case); Q-a where the top belongs; the full-field reading;
# Q-b the comb; Q-c dominance thresholds and gap ratios; Q-d shell fit;
# preparation of the readout.
#
# Note: the script is sectioned and restartable — it saves its state into
# verseny16_allapot.npz and must be run again until it reports the analysis.

# Identifier glossary — the identifiers were renamed from Hungarian
# to English; the original Hungarian name stands on the right:
#   above = felett              band = sav
#   bands = savok               BATCH = ADAG
#   better = jobb               candidates = jel
#   chosen = val                closed_ladder = zart_letra
#   cos_cache = cos_tar         cost = kolt
#   end_at = veg                FAMILY = CSALAD
#   five = otos                 GAP_THRESHOLD = RES_KUSZOB
#   gaps = resek                half_steps = fel
#   inside = benn               labels = cimkek
#   ladders5 = letrak5          MAIN = FO
#   main_wins = fo_nyer         member = tag
#   n_star = ng                 name = nev
#   NAMES = NEVEK               nearest = legk
#   runs = futamok              shape = alak
#   split = megoszlas           start_at = kezd
#   STATE_FILE = ALLAPOT        strict = szigoru
#   tipping = at                TOL = TURES
#   upper = felso               widest = legszel
#   winner = gy                 wins = gyoz
#   kesz is left as it is: it names a key inside verseny16_allapot.npz,
#   an on-disk name rather than a variable.

import numpy as np, time
from itertools import combinations

NH = 12**5
TOL = 1e-8
GAP_THRESHOLD = 1e-6

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
NAMES = list(MAIN.keys())
FAMILY = list(combinations(range(1, 13), 5))

def closed_ladder(shape, half_steps):
    dt = np.longdouble
    r = np.meshgrid(*[(2*np.pi*np.arange(L)).astype(dt)/L for L in shape],
                    indexing="ij")
    lam = np.zeros(shape, dtype=dt)
    for s in half_steps:
        lam += 2.0 - 2.0*np.cos(sum(si*gi for si, gi in zip(s, r)))
    return np.sort(lam.ravel())

def runs(labels):
    out = []
    for i, c in enumerate(labels):
        if out and out[-1][0] == c:
            out[-1][2] = i+1
        else:
            out.append([c, i+1, i+1])
    return out

STATE_FILE = "verseny16_allapot.npz"
BATCH = 260

def main():
    t0 = time.time()
    import os
    if not os.path.exists(STATE_FILE):
        print("== PKG-16-3 — the race: the named networks ==")
        cost = {}
        for name in NAMES:
            cost[name] = np.cumsum(closed_ladder(*MAIN[name]))
        best1 = cost["J1"].copy()
        best2 = np.full(NH, np.inf, dtype=np.longdouble)
        bid = np.zeros(NH, dtype=np.int16)
        for i, name in enumerate(NAMES[1:], start=1):
            c = cost[name]
            better = c < best1
            best2 = np.where(better, best1, np.minimum(best2, c))
            best1 = np.where(better, c, best1)
            bid[better] = i
        np.savez(STATE_FILE, best1=best1, best2=best2, bid=bid, kesz=0,
                 **{"k_"+n: cost[n] for n in NAMES})
        print("the named part is done (%.0f s) — run again for the family"
              % (time.time()-t0))
        return
    A = np.load(STATE_FILE)
    kesz = int(A["kesz"])
    best1, best2, bid = A["best1"], A["best2"], A["bid"].astype(np.int16)
    cost = {n: A["k_"+n] for n in NAMES}
    if kesz < len(FAMILY):
        kk = (2*np.pi*np.arange(NH)).astype(np.longdouble)/NH
        cos_cache = {s: 2.0-2.0*np.cos(s*kk) for s in range(1, 13)}
        end_at = min(kesz + BATCH, len(FAMILY))
        for j in range(kesz, end_at):
            member = FAMILY[j]
            c = np.cumsum(np.sort(cos_cache[member[0]]+cos_cache[member[1]]
                          +cos_cache[member[2]]+cos_cache[member[3]]+cos_cache[member[4]]))
            better = c < best1
            best2 = np.where(better, best1, np.minimum(best2, c))
            best1 = np.where(better, c, best1)
            bid[better] = 13 + j
        np.savez(STATE_FILE, best1=best1, best2=best2, bid=bid, kesz=end_at,
                 **{"k_"+n: cost[n] for n in NAMES})
        print("family: %d / %d done (%.0f s) — %s"
              % (end_at, len(FAMILY), time.time()-t0,
                 "run again" if end_at < len(FAMILY) else "the analysis follows"))
        return
    ladders5 = {n: closed_ladder(*MAIN[n]) for n in ("J1","J2","J3","J4","J5")}
    print("== PKG-16-3 — analysis ==")

    # registered facts
    print("facts: N=1 lowest two prices: %.2e / %.2e | N=3 best price: %.6f (>0) | "
          "full end: |deviation| = %.2e"
          % (float(best1[0]), float(best2[0]), float(best1[2]),
             abs(float(best1[-1]) - 2488320.0)))

    # main quintuple: winner runs
    J = np.stack([cost[n] for n in ("J1","J2","J3","J4","J5")])
    labels = []
    for n in range(NH):
        o = J[:, n]
        r = np.argsort(o)
        if o[r[1]] - o[r[0]] > TOL:
            labels.append(NAMES[r[0]])
        else:
            kik = sorted("J%d" % (i+1) for i in range(5)
                         if o[i] - o[r[0]] <= TOL)
            labels.append("T:" + "+".join(kik))
    fut5 = runs(labels)
    print("\nwinner runs on the main quintuple:")
    for f in fut5:
        if f[2]-f[1]+1 >= 3 or f[0].startswith("T"):
            print("   %-18s %7d .. %7d  (%d)" % (f[0], f[1], f[2], f[2]-f[1]+1))

    # Q-a: the upper half and the top
    upper = labels[NH//2:]
    split = {}
    for c in upper:
        split[c] = split.get(c, 0) + 1
    print("\nQ-a: split of the upper half on the quintuple: %s"
          % dict(sorted(split.items(), key=lambda x: -x[1])[:6]))

    # full field
    strict = best2 - best1 > TOL
    wins = {}
    for i in np.unique(bid[strict]):
        name = NAMES[i] if i < 13 else str(FAMILY[i-13])
        wins[name] = int(np.sum((bid == i) & strict))
    main_wins = sum(wins.get(n, 0) for n in ("J1","J2","J3","J4","J5"))
    print("full field: the main quintuple wins strictly at %d / %d fillings; "
          "tied fillings %d" % (main_wins, NH, int(np.sum(~strict))))
    print("   winning the most: %s"
          % sorted(wins.items(), key=lambda x: -x[1])[:6])
    print("Q-b comb (first 24): %s"
          % " | ".join("%d:%s" % (n+1,
             (NAMES[bid[n]] if bid[n] < 13 else str(FAMILY[bid[n]-13]))
             if strict[n] else "T") for n in range(24)))

    # Q-c: pairwise tippings and dominance thresholds on the quintuple
    print("\nQ-c: pair | N*-machine | price tipping | ratio")
    five = ("J1","J2","J3","J4","J5")
    for a in range(5):
        for b in range(a+1, 5):
            la, lb = ladders5[five[a]], ladders5[five[b]]
            j = np.where(la[1:] > lb[1:] + 1e-12)[0]
            n_star = int(j[0]) + 1 if len(j) else NH
            ca, cb = cost[five[a]], cost[five[b]]
            j = np.where(ca[1:] > cb[1:] + TOL)[0]
            tipping = int(j[0]) + 2 if len(j) else None
            print("   %s-%s  %7d  %10s  %s"
                  % (five[a], five[b], n_star, tipping if tipping else "none",
                     "%.1f%%" % (100.0*n_star/tipping) if tipping else "—"))

    # Q-d: shell fit at the main band boundaries
    print("\nQ-d: band boundary versus the shelf boundaries of the incoming winner:")
    for ix in range(1, len(fut5)):
        c, start_at = fut5[ix][0], fut5[ix][1]
        if c not in five or fut5[ix][2]-start_at < 3:
            continue
        l = ladders5[c]
        gaps = np.where(np.diff(l) > GAP_THRESHOLD)[0] + 1
        nearest = int(gaps[np.argmin(np.abs(gaps - start_at))])
        print("   %8d (%s): nearest closed degree %8d, distance %d"
              % (start_at, c, nearest, abs(nearest - start_at)))

    # readout preparation: the standing band of highest extension
    bands = {}
    for f in fut5:
        if f[0] in five and f[2]-f[1]+1 >= 3:
            bands.setdefault(f[0], []).append((f[1], f[2], f[2]-f[1]+1))
    winner = None
    for name in ("J5","J4","J3","J2"):
        if name in bands:
            winner = name; break
    if winner:
        band = max(bands[winner], key=lambda x: x[2])
        l = ladders5[winner]
        gaps = np.diff(l)
        inside = [(int(i+1), float(gaps[i]))
                for i in np.where(gaps > GAP_THRESHOLD)[0]
                if band[0] <= i+1 <= band[1]]
        widest = max(r for _, r in inside)
        candidates = sorted(nf for nf, r in inside if r > widest - 1e-9)
        above = [nf for nf in candidates if nf >= NH//2]
        chosen = min(above) if above else candidates[-1]
        print("\nreadout: the standing band of highest extension is %s (%d..%d); "
              "widest gap %.6f; chosen closed degree N = %d"
              % (winner, band[0], band[1], widest, chosen))

if __name__ == "__main__":
    main()
