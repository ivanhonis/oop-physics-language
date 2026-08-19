# PKG-15-3 — The race (II/15)
# Builds on the outgoing claims of PKG-15-2 (L1-L5). Its business:
#   1) cost curves for N = 1..20736 on all 503 entrants (from the closed ladders)
#   2) winner table on the main four (J1-J4) — the basis of the staircase
#      verdict — and on the full field (the honest reading)
#   3) verdict by the three-rung rule of PKG-15-1 §7; tolerance: 1e-8 (L5)
#   4) checking the pre-registered facts (N = 1, 2, 3, full)
#   5) evaluating the three registered questions (Q-a, Q-b, Q-c)
#   6) independent recomputation: the J1-J4 curves on the extended-precision route too
#   7) preparing the readout: closed degrees in the winner of the highest standing band

# Identifier glossary — the identifiers were renamed from Hungarian
# to English; the original Hungarian name stands on the right:
#   above = felett              bands = savok
#   candidates = jeloltek_f     chosen = valasztott
#   closed_ladder = zart_letra  col = oszlop
#   cost = kolt                 dev = elteres
#   differs_at = elter_hol      FAMILY = CSALAD
#   full_end = teli             full_labels = telj_cimkek
#   GAP_THRESHOLD = RES_KUSZOB  gaps = resek
#   grids = racsok              half_steps = fel
#   inside = benn               J2_STEPS = J2LEP
#   J3_STEPS = J3LEP            labels = cimkek
#   labels_f = cimkek_f         ladders = letrak
#   lowest = also               MAIN = FO
#   main_band = fo_sav          main_wins = fo_nyer
#   member = tag                name = nev
#   names = nevek               nearest = legkozelebb
#   phase = fazis               runs = futamok
#   runs4 = fut4                runs_short = futamok_rov
#   seq_in = lista              shape = alak
#   start_at = kezdet           t_field = t2s
#   ties = holtversenyek        TOL = TURES
#   UNIT4 = EGYSEG4             upper = felso
#   upper_split = fj            who = kik
#   widest = legszel            win_count = gyoztes_db
#   winner = gy

import numpy as np
from itertools import combinations, product
import time

N = 20736
TOL = 1e-8          # identity tolerance (L5, fixed)
GAP_THRESHOLD = 1e-6     # threshold of a closed degree (shelf boundary) — a declared convention

# ----------------------------------------------------------------- field ---
UNIT4 = [(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)]
J3_STEPS = [(1,0,0),(0,1,0),(0,0,1),(1,-1,-1)]
J2_STEPS = [(1,0),(0,1),(1,1),(1,-1)]
MAIN = {
    "J1": ((N,),           [(1,),(2,),(3,),(4,)]),
    "J2": ((144,144),      J2_STEPS),
    "J3": ((24,24,36),     J3_STEPS),
    "J4": ((12,12,12,12),  UNIT4),
    "K1": ((16,36,36),     J3_STEPS),
    "K2": ((12,36,48),     J3_STEPS),
    "K3": ((8,8,18,18),    UNIT4),
    "K4": ((48,432),       J2_STEPS),
}
FAMILY = list(combinations(range(1, 13), 4))

def closed_ladder(shape, half_steps, dt=np.float64):
    grids = np.meshgrid(*[(2*np.pi*np.arange(L)/L).astype(dt) for L in shape],
                         indexing="ij")
    lam = np.zeros(shape, dtype=dt)
    for s in half_steps:
        phase = sum(si*gi for si, gi in zip(s, grids))
        lam += 2.0 - 2.0*np.cos(phase)
    return np.sort(lam.ravel())

def runs_short(seq_in):
    """Compressing a number sequence into intervals."""
    out = []
    for x in seq_in:
        if out and out[-1][1] == x-1:
            out[-1][1] = x
        else:
            out.append([x, x])
    return ", ".join("%d..%d" % (a, b) if a != b else str(a) for a, b in out)

def runs(labels):
    """Compressing a label sequence into (label, from, to) runs."""
    out = []
    for i, c in enumerate(labels):
        if out and out[-1][0] == c:
            out[-1][2] = i+1
        else:
            out.append([c, i+1, i+1])
    return out

def main():
    t0 = time.time()
    print("== PKG-15-3 — the race ==")

    # PRIMARY ROUTE: extended precision (the float64 accumulation error near the
    # full end is ~2e-8, which would cross the fixed 1e-8 tolerance; the
    # extended-precision accumulation error is ~1e-10 — the tolerance stays
    # four orders of magnitude above it)
    names = list(MAIN.keys()) + [str(t) for t in FAMILY]
    ladders = np.empty((len(names), N), dtype=np.longdouble)
    kL = (2*np.pi*np.arange(N)).astype(np.longdouble)/N
    for i, name in enumerate(names):
        if name in MAIN:
            ladders[i] = closed_ladder(*MAIN[name], dt=np.longdouble)
        else:
            member = eval(name)
            ladders[i] = np.sort(sum(2-2*np.cos(s*kL) for s in member))
    cost = np.cumsum(ladders, axis=1)                 # kolt[i, n-1] = price at N=n
    print("cost curves (extended precision): %d networks, %.1f s"
          % (len(names), time.time()-t0))

    # -- pre-registered facts --
    t1 = np.sum(cost[:, 0] < TOL)
    t2 = np.sum(cost[:, 1] < TOL)
    t3 = [names[i] for i in np.where(cost[:, 2] < TOL)[0]]
    full_end = np.max(np.abs(cost[:, -1] - 165888.0))
    print("registered facts: N=1 at zero %d/503 | N=2 at zero %d (expected 16) | "
          "N=3 at zero %s | full-end deviation %.1e — %s"
          % (t1, t2, t3, full_end,
             "HOLDS" if (t1 == 503 and t2 == 16 and t3 == ["(3, 6, 9, 12)"]
                         and full_end < 1e-6) else "FAILS"))

    # -- winner table on the main four --
    J = cost[:4]                                     # J1..J4
    labels = []
    for n in range(N):
        col = J[:, n]
        r = np.argsort(col)
        if col[r[1]] - col[r[0]] > TOL:
            labels.append(names[r[0]])
        else:
            who = sorted(names[i] for i in range(4)
                         if col[i] - col[r[0]] <= TOL)
            labels.append("T:" + "+".join(who))
    runs4 = runs(labels)
    print("\nwinner runs on the main four (label, from, to):")
    for f in runs4:
        print("   %-14s %6d .. %6d   (%d fillings)" % (f[0], f[1], f[2], f[2]-f[1]+1))

    # -- verdict per §7 --
    bands = {}
    for f in runs4:
        if f[0] in ("J2", "J3", "J4"):
            bands.setdefault(f[0], []).append((f[1], f[2], f[2]-f[1]+1))
    print("\nbasis of the verdict: longest connected bands:")
    for j in ("J2", "J3", "J4"):
        if j in bands:
            main_band = max(bands[j], key=lambda x: x[2])
            print("   %s: %d..%d (%d fillings); further patches: %d"
                  % (j, main_band[0], main_band[1], main_band[2], len(bands[j])-1))
        else:
            print("   %s: NO winning filling" % j)

    # -- Q-b: data of the mirror question --
    print("\nQ-b (mirror question): ladder width (largest beat): "
          "J3 %.6f, J4 %.6f" % (ladders[2][-1], ladders[3][-1]))
    upper = labels[N//2:]
    upper_split = {c: upper.count(c) for c in set(upper)}
    print("   winner split on the four in the upper half (N > %d): %s"
          % (N//2, dict(sorted(upper_split.items(), key=lambda x: -x[1]))))

    # -- Q-a: shell fit at the band boundaries --
    print("\nQ-a (shell fit) — band boundary versus the shelf boundaries of the incoming winner:")
    for ix in range(1, len(runs4)):
        c, start_at = runs4[ix][0], runs4[ix][1]
        if c not in ("J1", "J2", "J3", "J4"):
            continue
        l = ladders[names.index(c)]
        gaps = np.where(np.diff(l) > GAP_THRESHOLD)[0] + 1   # closed degrees (in N)
        nearest = int(gaps[np.argmin(np.abs(gaps - start_at))])
        print("   %6d (start of the %s band): nearest closed degree %6d, distance %d"
              % (start_at, c, nearest, abs(nearest - start_at)))

    # -- full-field reading --
    t_field = time.time()
    lowest = np.min(cost, axis=0)
    win_count = {}
    ties = 0
    full_labels = []
    for n in range(N):
        who = np.where(cost[:, n] - lowest[n] <= TOL)[0]
        if len(who) == 1:
            name = names[who[0]]
            win_count[name] = win_count.get(name, 0) + 1
            full_labels.append(name)
        else:
            ties += 1
            full_labels.append("T")
    main_wins = sum(win_count.get(j, 0) for j in ("J1","J2","J3","J4"))
    top = sorted(win_count.items(), key=lambda x: -x[1])[:8]
    print("\nfull field (503 entrants): the main four win strictly at %d / %d "
          "fillings; tied fillings %d" % (main_wins, N, ties))
    print("   entrants winning the most fillings: %s" % top)
    print("   (%.0f s)" % (time.time()-t_field))

    # -- Q-c: comb pattern in the lower range --
    print("\nQ-c (comb pattern): winners of the first 24 fillings of the full field:")
    print("   " + " | ".join("%d:%s" % (n+1, full_labels[n]) for n in range(24)))

    # -- independent recomputation: float64 cross-check on the main four --
    Jf = np.empty((4, N))
    for i, name in enumerate(("J1","J2","J3","J4")):
        Jf[i] = np.cumsum(closed_ladder(*MAIN[name], dt=np.float64))
    dev = float(np.max(np.abs(Jf - J.astype(np.float64))))
    labels_f = []
    for n in range(N):
        col = Jf[:, n]
        r = np.argsort(col)
        if col[r[1]] - col[r[0]] > TOL:
            labels_f.append(names[r[0]])
        else:
            who = sorted(names[i] for i in range(4)
                         if col[i] - col[r[0]] <= TOL)
            labels_f.append("T:" + "+".join(who))
    differs_at = [n+1 for n in range(N) if labels_f[n] != labels[n]]
    print("\ncross-check (float64): largest cost deviation %.2e; "
          "the winner row differs at %d fillings%s" % (dev, len(differs_at),
          " — these: %s" % runs_short(differs_at) if differs_at else ""))

    # -- preparing the readout: closed degrees in the highest standing band --
    if "J4" in bands:
        winner = "J4"
    elif "J3" in bands:
        winner = "J3"
    else:
        winner = None
    if winner:
        main_band = max(bands[winner], key=lambda x: x[2])
        l = ladders[names.index(winner)]
        gaps = np.diff(l)
        inside = [(int(i+1), float(gaps[i])) for i in np.where(gaps > GAP_THRESHOLD)[0]
                if main_band[0] <= i+1 <= main_band[1]]
        inside.sort(key=lambda x: -x[1])
        widest = inside[0][1]
        candidates = sorted(nf for nf, r in inside if r > widest - 1e-9)
        above = [nf for nf in candidates if nf >= N//2]
        chosen = min(above, key=lambda nf: nf - N//2) if above else candidates[-1]
        print("\nreadout preparation: the winner of the highest standing rung "
              "(by extension) is %s, band %d..%d" % (winner, main_band[0], main_band[1]))
        print("   the widest gaps of the band (gap %.6f) above these closed degrees: %s"
              % (widest, candidates))
        print("   choice rule (fixed): among the widest gaps, the one nearest "
              "half filling from above -> N = %d" % chosen)

if __name__ == "__main__":
    main()
