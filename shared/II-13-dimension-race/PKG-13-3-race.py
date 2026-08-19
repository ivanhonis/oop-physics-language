# PKG-13-3 — A betoltesi verseny szamolo kodja
# Csomag-dokumentum: PKG-13-3-race_hu.md (a kod nyelvfuggetlen)
# Lepesek: (1) fuggetlen letra-ujraszamolas szomszedlistas felepitessel (B3),
#          (2) kumulalt koltsegek N = 1..16, (3) szigoru gyoztesek,
#          (4) a 7. szabaly fo olvasata, (5) a sik fokhatarai.

import numpy as np

N = 16
reps = {
    "J1 (1,2)":  ("circ", (1, 2)),
    "J2 torusz": ("torus", None),
    "J3 (2,4)":  ("circ", (2, 4)),
    "D2 (2,6)":  ("circ", (2, 6)),
    "K (1,3)":   ("circ", (1, 3)),
    "K (1,7)":   ("circ", (1, 7)),
    "K (1,6)":   ("circ", (1, 6)),
    "K (1,4)":   ("circ", (1, 4)),
}

def build(kind, steps):
    """Fuggetlen kodut: szomszedlistas adjacencia, nem a PKG-13-2 felepitese."""
    A = np.zeros((N, N))
    if kind == "circ":
        for i in range(N):
            for s in steps:
                A[i, (i + s) % N] = 1
                A[i, (i - s) % N] = 1
    else:
        for x in range(4):
            for y in range(4):
                i = 4 * x + y
                for j in (4 * ((x + 1) % 4) + y, 4 * ((x - 1) % 4) + y,
                          4 * x + (y + 1) % 4, 4 * x + (y - 1) % 4):
                    A[i, j] = 1
    return np.diag(A.sum(1)) - A

lad, cum = {}, {}
for name, (kind, st) in reps.items():
    ev = np.sort(np.linalg.eigvalsh(build(kind, st)))
    lad[name] = ev
    cum[name] = np.cumsum(ev)

print("B3 ellenorzes — nyomosszegek es nulla-modusok:")
for n in reps:
    print(f"  {n:10s} nyom={lad[n].sum():.10f} nulla={int((lad[n] < 1e-9).sum())}")
print("szuroproba a PKG-13-2 ellen: J1[1]=%.4f (0,7380), J3[2]=%.4f (2,5858), D2[2]=%.1f (4)" %
      (lad["J1 (1,2)"][1], lad["J3 (2,4)"][2], lad["D2 (2,6)"][2]))

names = list(reps)
print("\nKUMULALT KOLTSEGEK (sorok: N = 1..16)")
print("N   | " + " | ".join(f"{n:>10s}" for n in names))
for k in range(N):
    print(f"{k+1:3d} | " + " | ".join(f"{cum[n][k]:10.3f}" for n in names))

print("\nGYOZTESEK (szigoru; holtverseny felsorolva)")
for k in range(N):
    vals = {n: cum[n][k] for n in names}
    m = min(vals.values())
    win = [n for n, v in vals.items() if v - m < 1e-9]
    print(f"  N={k+1:2d}: {win}  koltseg={m:.3f}")

print("\n7. SZABALY, fo olvasat: veri-e a J2 egyszerre a J1-et es a J3-at?")
rng = [k + 1 for k in range(N)
       if cum["J2 torusz"][k] < cum["J1 (1,2)"][k] - 1e-9
       and cum["J2 torusz"][k] < cum["J3 (2,4)"][k] - 1e-9]
print("  toltesek, ahol J2 < J1 es J2 < J3:", rng)

print("\nA J2 fokhatarai (zart fokok):",
      [i + 1 for i in range(N - 1) if lad["J2 torusz"][i + 1] - lad["J2 torusz"][i] > 1e-9])
