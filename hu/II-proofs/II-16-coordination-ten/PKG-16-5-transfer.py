# PKG-16-5 — Tetel-atvitel a paros keszleten (II/16)
# A lyuk-tukor tetel (PKG-15-5) szovege valtozatlanul ervenyes: ket paros-jegyu
# szoves, azonos helyszam es helyenkenti szerzodesszam. A paros keszlet itt:
# J5 (honos), KP3, KP4 (paros kontrollok), es a hat csupa-paratlan csaladtag.
# Ellenorzesek:
#  E1 tukor-azonossag gepi pontossaggal a negy kulcsparon
#  E2 irany-kuszobok (N*-gepi, pontonkenti dominancia) a paros parokon
#  E3 teto-kovetkezmeny: a tukrozott szakaszon a ritka-rendben alacsonyabb
#     paros szigoruan olcsobb (tartalekkal)
#  E4 mezony-konzisztencia: a teljes mezony teli-vegi gyozteseit a mentett
#     verseny-allapotbol olvassuk — a ritka-rend tukrozeset varjuk

import numpy as np
from itertools import combinations

NH = 12**5
FO = {
 "J5": ((12,)*5, [tuple(1 if i==j else 0 for i in range(5)) for j in range(5)]),
 "KP3": ((54,64,72), [(1,0,0),(0,1,0),(0,0,1),(1,-1,-1),(1,-1,1)]),
 "KP4": ((18,24,24,24), [(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1),(0,1,1,1)]),
}
def zl(alak, fel):
    dt = np.longdouble
    r = np.meshgrid(*[(2*np.pi*np.arange(L)).astype(dt)/L for L in alak],
                    indexing="ij")
    lam = np.zeros(alak, dtype=dt)
    for s in fel:
        lam += 2.0-2.0*np.cos(sum(si*gi for si,gi in zip(s,r)))
    return np.sort(lam.ravel())

print("== PKG-16-5 — tetel-atvitel a paros keszleten ==")
lad = {n: zl(*FO[n]) for n in FO}
kk = (2*np.pi*np.arange(NH)).astype(np.longdouble)/NH
lad["V"] = np.sort(sum(2.0-2.0*np.cos(s*kk) for s in (1,3,5,7,9)))
kolt = {n: np.cumsum(l) for n, l in lad.items()}

parok = [("KP3","KP4"),("KP3","J5"),("KP4","J5"),("V","KP3")]
print("E1 tukor-azonossag es E2-E3 a parokon:")
for x, y in parok:
    R = (kolt[y]-kolt[x])[:NH-1]
    e1 = float(np.max(np.abs(R - R[::-1])))
    j = np.where(lad[x][1:] > lad[y][1:] + 1e-12)[0]
    ng = int(j[0])+1 if len(j) else NH
    also, felso = NH-ng, NH-2
    tart = float(np.min((kolt[y]-kolt[x])[also-1:felso]))
    print("  %s-%s: tukor-elteres %.2e | N*-gepi %d | teto-szakasz %d..%d, "
          "legkisebb elony %.4f — %s"
          % (x, y, e1, ng, also, felso, tart,
             "ALL" if e1 < 1e-8 and tart > 1e-9 else "BUKIK"))
d = float(abs(kolt["KP3"][NH-2]-kolt["J5"][NH-2]))
print("  egy-lyukas paros holtverseny (KP3-J5): %.2e — %s"
      % (d, "ALL" if d < 1e-8 else "BUKIK"))

A = np.load("verseny16_allapot.npz")
bid, b1, b2 = A["bid"], A["best1"], A["best2"]
NEVEK = ["J1","J2","J3","J4","J5","K1","K2","K3","KA2","KA3","KA4","KP3","KP4"]
CSAL = list(combinations(range(1,13),5))
def nev(i): return NEVEK[i] if i < 13 else str(CSAL[i-13])
print("\nE4 a teljes mezony teli-vegi gyoztesei (utolso 2000 toltes):")
szel = bid[-2001:-1]
megoszlas = {}
for i in szel:
    megoszlas[nev(int(i))] = megoszlas.get(nev(int(i)), 0) + 1
print("  ", dict(sorted(megoszlas.items(), key=lambda x: -x[1])[:5]))
utolso = [nev(int(bid[NH-1-m])) for m in range(1, 9)]
print("   az utolso 8 toltes gyoztesei (teli fele): %s" % utolso)
