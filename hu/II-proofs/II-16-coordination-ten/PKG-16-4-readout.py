# PKG-16-4 — A kiolvasas (II/16)
# Rendszer (PKG-16-3, V5): J5 hiperkocka-szoves 12^5, 1 244 160 szerzodes;
# toltes: N = 130 902 zart fok (a res folotte vart erteke 2 - sqrt(3)).
# Jegyzokonyv a PKG-16-1 §8 szerint; itelet-feltetelek elore:
#   A1 zart fok all; A2 teljesseg 1244160/1244160, 0 fantom, 0 hianyzo;
#   A3 golyo r<=3 egzakt a negyedrendu soron (jelentes r<=5, 2r<12);
#   A4 sav-orszem >= 2. Kotelezo sor: atellenes osztaly (paros gyoztes).
# Vetito-pecset (A8/iv, mintaveteles ritka alak): 64 betoltott + 64 ures
# sorsolt modus (mag 248832) — (a) ritka maradek-proba a graf-epitesu
# szomszedsaggal; (b) a G-tabla kozvetlen (nem-FFT) osszegzesu transzformja
# a mintamodusoknal pontosan a betoltottseg-jelzot adja.

import numpy as np
import time
from collections import deque

L, DIM = 12, 5
NSITE = L**DIM              # 248832
NTOLT = 130902
NCONTRACT = 5 * NSITE       # 1 244 160
RES_VART = 2.0 - np.sqrt(3.0)
ABLAK = 30
MAG = 248832

def canon(d):
    return tuple(sorted(int(min(x % L, (-x) % L)) for x in d))

def main():
    t0 = time.time()
    print("== PKG-16-4 — a kiolvasas (J5, N = %d) ==" % NTOLT)
    k = 2*np.pi*np.arange(L)/L
    egy = 2.0 - 2.0*np.cos(k)
    lam = egy.reshape(-1,1,1,1,1)+egy.reshape(1,-1,1,1,1)+egy.reshape(1,1,-1,1,1)\
        + egy.reshape(1,1,1,-1,1)+egy.reshape(1,1,1,1,-1)
    lam_flat = np.sort(lam.ravel())
    res = lam_flat[NTOLT] - lam_flat[NTOLT-1]
    A1 = abs(res - RES_VART) < 1e-9
    print("zart fok: res a %d. fok folott %.9f (vart %.9f) — %s"
          % (NTOLT, res, RES_VART, "all" if A1 else "BUKIK"))
    kuszob = lam_flat[NTOLT-1] + 1e-9
    occ = lam <= kuszob
    assert int(occ.sum()) == NTOLT

    G = np.fft.ifftn(occ.astype(float))
    assert np.max(np.abs(G.imag)) < 1e-12
    G = G.real

    # osztaly-egzaktsag (szoves)
    oszt = {}
    Gf = G.ravel()
    koordok = np.array(np.unravel_index(np.arange(NSITE), (L,)*DIM)).T
    for i in range(NSITE):
        if i == 0:
            continue
        oszt.setdefault(canon(koordok[i]), []).append(Gf[i])
    assert max(np.std(v) for v in oszt.values()) < 1e-12

    szomszed = G[1,0,0,0,0]
    atellenes = G[(L//2,)*DIM]
    print("szomszed-kozelseg G(1,0,0,0,0) = %+.6f" % szomszed)
    print("ATELLENES VISSZHANG G(6,6,6,6,6) = %+.6f (elojel: %s; "
          "|arany| = %.4f) [kotelezo sor]"
          % (atellenes, "negativ" if atellenes < 0 else "pozitiv",
             abs(atellenes)/szomszed))

    g = Gf.copy(); g[0] = -np.inf
    rend = np.argsort(g)[::-1]
    v = g[rend]
    legjobb, kstar = -1.0, None
    for m in range(1, ABLAK+1):
        if v[m] > 0:
            r = v[m-1]/v[m]
            if r > legjobb:
                legjobb, kstar = r, m
    print("elojeles lista eleje:", np.round(v[:14], 5))
    print("ugras a(z) %d. hely utan: %.5f -> %.5f (%.1f-szeres)"
          % (kstar, v[kstar-1], v[kstar], legjobb))
    maradek = v[kstar:]; maradek = maradek[np.isfinite(maradek)]
    j = int(np.argmax(np.abs(maradek)))
    d_er = tuple(koordok[rend[kstar+j]])
    S = v[kstar-1]/abs(float(maradek[j]))
    A4 = S >= 2.0
    print("sav-orszem: S = %.4f (kuszob 2) — %s; legerosebb elutasitott: "
          "%s osztaly, G = %+.6f"
          % (S, "all" if A4 else "BUKIK", canon(d_er), float(maradek[j])))
    va = np.sort(np.abs(np.where(np.isfinite(g), g, 0)))[::-1]
    r_abs = va[:ABLAK]/np.maximum(va[1:ABLAK+1], 1e-300)
    k_abs = int(np.argmax(r_abs)) + 1
    print("regi abszolut szabaly: ugras a(z) %d. hely utan (%.1f-szeres)"
          % (k_abs, r_abs[k_abs-1]))

    # visszarakas + teljesseg
    elf = [tuple(koordok[i]) for i in rend[:kstar]]
    rc = np.arange(NSITE)
    def elek(dl):
        parok = set()
        for d in dl:
            cel = (koordok + d) % L
            b = np.ravel_multi_index(cel.T, (L,)*DIM)
            parok |= set(map(int, np.minimum(rc, b)*NSITE + np.maximum(rc, b)))
        return parok
    rec = elek(elf)
    igazd = []
    for t in range(DIM):
        for sgn in (1, -1):
            d = [0]*DIM; d[t] = sgn % L
            igazd.append(tuple(x % L for x in d))
    igaz = elek(igazd)
    megvan, fantom, hianyzo = len(rec & igaz), len(rec-igaz), len(igaz-rec)
    A2 = (megvan == NCONTRACT and fantom == 0 and hianyzo == 0)
    print("teljesseg-szamla: megtalalt %d/%d; fantom %d; hianyzo %d — %s"
          % (megvan, NCONTRACT, fantom, hianyzo, "all" if A2 else "BUKIK"))

    # golyo r<=5
    lat = {(0,)*DIM}; front = [(0,)*DIM]; golyo = [1]
    for r in range(1, 6):
        ujf = []
        for p in front:
            for d in elf:
                q = tuple((x+y) % L for x, y in zip(p, d))
                if q not in lat:
                    lat.add(q); ujf.append(q)
        golyo.append(golyo[-1]+len(ujf)); front = ujf
    hiv = [1, 11, 61, 231, 681, 1683]
    A3 = golyo[:4] == hiv[:4]
    print("golyo (r=0..5): %s — hivatkozas (negyedrendu): %s — r<=3: %s; "
          "r<=5: %s" % (golyo, hiv, "all" if A3 else "BUKIK",
                        "egyezik" if golyo == hiv else "elter"))

    # vetito-pecset: mintaveteles ritka alak
    rng = np.random.default_rng(MAG)
    idxek = [np.ravel_multi_index(((koordok + d) % L).T, (L,)*DIM)
             for d in igazd]
    occ_f = occ.ravel()
    pecset_a, pecset_b = 0.0, 0.0
    minta = []
    bet = np.where(occ_f)[0]; ur = np.where(~occ_f)[0]
    minta = list(rng.choice(bet, 64, replace=False)) \
          + list(rng.choice(ur, 64, replace=False))
    for mi in minta:
        n = koordok[mi]
        ph = sum(((n[j]*koordok[:, j]) % L)/L for j in range(DIM))
        vv = np.exp(2j*np.pi*ph)
        Av = np.zeros(NSITE, dtype=complex)
        for ix in idxek:
            Av += vv[ix]
        lj = float(sum(2-2*np.cos(2*np.pi*ni/L) for ni in n))
        pecset_a = max(pecset_a, float(np.max(np.abs(10*vv - Av - lj*vv))))
        # a G-tabla kozvetlen osszegzesu transzformja e modusnal
        val = complex(np.sum(Gf * np.conj(vv)))
        pecset_b = max(pecset_b, abs(val - (1.0 if occ_f[mi] else 0.0)))
    print("vetito-pecset (64+64 modus, mag %d): maradek-ag %.2e; "
          "transzform-ag %.2e — %s"
          % (MAG, pecset_a, pecset_b,
             "ALL" if max(pecset_a, pecset_b) < 1e-9 else "BUKIK"))

    print("\nfeltetelek: A1 %s | A2 %s | A3 %s | A4 %s"
          % tuple("all" if a else "BUKIK" for a in (A1, A2, A3, A4)))
    print("ITELET: %s  (%.0f s)"
          % ("ALL — a honos gyoztes belulrol otkiterjedesunek olvassa magat,"
             " a pecset all" if all((A1, A2, A3, A4)) else
             "RESZLEGES — a bukott feltetel fent", time.time()-t0))

if __name__ == "__main__":
    main()
