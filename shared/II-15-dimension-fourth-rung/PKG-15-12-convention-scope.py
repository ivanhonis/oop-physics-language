# PKG-15-12-convention-scope.py -- how far do the theorems reach, and what do
# the two unmeasured conventions actually carry?
#
# The kernel still lists KON-01 (the race rule) and KON-03 (weave construction)
# as hand-set items with no measured effect. This package measures both, and the
# route is the same one that worked for KON-02: change the one thing, see what
# moves.
#
# KON-03 first, because a reading of the proofs suggests the answer. Neither the
# dense-end theorem nor the hole-ladder theorem ever mentions a weave. They use
#
#     the trace tie      sum of beats = d*n     -- true of ANY d-regular graph
#     the ceiling        beat <= 2d, equality iff bipartite -- likewise
#     the hole ladder    2d - beat, sorted      -- likewise
#
# If that reading is right, the theorems hold on every regular graph, and the
# weave convention carries nothing for THEM -- only for the field. The test is
# to run them on graphs built no other way than by their edge lists, including
# ones provably outside the weave family: the Petersen graph is 3-regular and
# vertex-transitive but is NOT a Cayley graph, so no group structure can lay the
# same wiring on each of its places. Its bipartite double cover, the Desargues
# graph, is the same but bipartite.
#
# KON-01 second. The race rule fixes an equal contract budget for every entrant.
# That is what makes the trace equal, and the trace tie is what turns the dense
# end into a subtraction. So the rule is not decorative -- it is the precondition
# of the whole apparatus, and unequal budgets should break the comparison in a
# visible way. Measuring that is the point.

import sys
import time
from pathlib import Path

import numpy as np

SHARED = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SHARED))

import summation                                             # noqa: E402

TURES = 1e-9


# ------------------------------------------------------------------ graphs
def petersen():
    """2-subsets of {0..4}, joined when disjoint. 3-regular, vertex-transitive,
    and famously NOT a Cayley graph -- the standard witness that the weave
    construction is strictly narrower than 'every place looks the same'."""
    csucsok = [frozenset(c) for c in
               [(a, b) for a in range(5) for b in range(a + 1, 5)]]
    elek = [(i, j) for i in range(10) for j in range(10)
            if i < j and not (csucsok[i] & csucsok[j])]
    return 10, elek


def desargues():
    """Bipartite double cover of the Petersen graph: 20 places, 3-regular,
    vertex-transitive, bipartite, and also not a Cayley graph."""
    _, pe = petersen()
    elek = []
    for u, v in pe:
        elek.append((u, v + 10))
        elek.append((v, u + 10))
    return 20, elek


def kor_letra():
    """C10 x K2, the circular ladder: 20 places, 3-regular, bipartite, and a
    perfectly ordinary weave -- the control."""
    elek = []
    for i in range(10):
        elek.append((i, (i + 1) % 10))
        elek.append((i + 10, (i + 1) % 10 + 10))
        elek.append((i, i + 10))
    return 20, elek


def korlanc(n, lepesek):
    """A weave (circulant) on n places -- the family the repository uses."""
    elek = set()
    for i in range(n):
        for s in lepesek:
            j = (i + s) % n
            if i != j:
                elek.add((min(i, j), max(i, j)))
    return n, sorted(elek)


def letra_grafbol(n, elek):
    """The beat ladder straight from the edge list: the Laplacian spectrum.
    No group structure is used anywhere."""
    A = np.zeros((n, n), dtype=np.float64)
    for u, v in elek:
        A[u, v] = A[v, u] = 1.0
    L = np.diag(A.sum(axis=1)) - A
    return np.sort(np.linalg.eigvalsh(L)), A


def paros_e(n, elek):
    """Two-colouring by breadth-first search -- the definition, not a criterion."""
    szin = {}
    for kezd in range(n):
        if kezd in szin:
            continue
        szin[kezd] = 0
        sor = [kezd]
        while sor:
            u = sor.pop()
            for a, b in elek:
                v = b if a == u else (a if b == u else None)
                if v is None:
                    continue
                if v not in szin:
                    szin[v] = 1 - szin[u]
                    sor.append(v)
                elif szin[v] == szin[u]:
                    return False
    return True


def probal(nev, n, elek, szoves):
    lam, A = letra_grafbol(n, elek)
    d = float(A.sum(axis=1)[0])
    assert np.allclose(A.sum(axis=1), d), "nem regularis: " + nev
    T, plafon = d * n, 2.0 * d
    nyom_elt = abs(float(lam.sum()) - T)
    csucs = float(lam[-1])
    paros = paros_e(n, elek)
    csucs_egyezik = (abs(csucs - plafon) <= TURES) == paros

    ar = np.cumsum(lam)
    D = np.cumsum(np.sort(plafon - lam))
    m = np.arange(1, n)
    azonossag = float(np.max(np.abs(ar[n - m - 1] - (T - plafon * m + D[m - 1]))))

    print("   %-22s %-7s d=%d n=%3d | nyom %8.1e | csucs %6.3f/%4.1f paros:%-3s L3:%-4s | "
          "azonossag %8.1e" % (nev, "szoves" if szoves else "NEM-szoves", d, n,
                               nyom_elt, csucs, plafon, "igen" if paros else "nem",
                               "all" if csucs_egyezik else "BUKIK", azonossag))
    return nyom_elt <= TURES and csucs_egyezik and azonossag <= 1e-8, lam, ar, D, T, plafon


def main():
    kezd = time.time()
    print("== PKG-15-12 -- a konvenciok hatokore ==")
    print()
    print("== KON-03: all-e a tetel a SZOVES-CSALADON KIVUL is? ==")
    print()
    mind = True
    tarolo = {}
    for nev, (n, e), szoves in [
        ("Petersen", petersen(), False),
        ("Desargues", desargues(), False),
        ("kor-letra C10xK2", kor_letra(), True),
        ("korlanc C20(1,10)", korlanc(20, [1, 10]), True),
        ("korlanc C20(1,3,5)", korlanc(20, [1, 3, 5]), True),
        ("korlanc C20(1,2,3)", korlanc(20, [1, 2, 3]), True),
    ]:
        ok, lam, ar, D, T, pl = probal(nev, n, e, szoves)
        mind = mind and ok
        tarolo[nev] = (n, lam, ar, D, T, pl)
    print()
    print("   -> %s" % ("MIND ALL. A tetelek sehol nem hasznaljak a szoves-szerkezetet: "
                        "eleg a d-regularitas." if mind else "VALAMELYIK BUKIK -- allj meg."))
    print()

    # The dense-end criterion across the weave boundary. The field MUST share n
    # and d: that is the race rule, and the first run of this script mixed d=3
    # with d=6 entrants and duly broke -- which is the KON-01 measurement below,
    # not a failure of the criterion.
    print("== A teli-veg kriterium a szoves-hataron at (kozos n=20, KOZOS d=3) ==")
    mezony = ["Desargues", "kor-letra C10xK2", "korlanc C20(1,10)"]
    n = 20
    ar_t = np.array([tarolo[k][2] for k in mezony])
    D_t = np.array([tarolo[k][3] for k in mezony])

    def gyoztesek(oszlop, tur=1e-9):
        """The winner SET, within tolerance. Comparing argmin alone would break on
        ties -- and at both ends of the filling range the entrants tie in bulk:
        every connected net has a zero beat, and every mirror-marked one has the
        same peak. The first run of this script compared argmin and reported four
        phantom discrepancies, all of them ties split by rounding noise."""
        return frozenset(i for i, v in enumerate(oszlop) if v <= oszlop.min() + tur)

    elteres = 0
    for mm in range(1, n):
        N = n - mm
        A = gyoztesek(ar_t[:, N - 1])
        B = gyoztesek(D_t[:, mm - 1])
        if A != B:
            elteres += 1
        if mm in (1, 2, 3, 5, 10, 15, 19) or A != B:
            print("   m=%3d (N=%3d): verseny {%s} lyuk-letra {%s} %s"
                  % (mm, N, ", ".join(mezony[i] for i in sorted(A)),
                     ", ".join(mezony[i] for i in sorted(B)),
                     "" if A == B else "<-- ELTER"))
    print("   -> %s" % ("mind a %d toltesen egyezik: a kriterium a NEM-szoves "
                        "indulora (Desargues) is all" % (n - 1)
                        if not elteres else "ELTERES -- allj meg"))
    print()

    # KON-01, measured: mix the budgets and watch the same criterion break.
    print("== KON-01 merese: mi tortenik, ha a koltsegvetes NEM azonos? ==")
    vegyes = ["Desargues", "korlanc C20(1,3,5)"]          # d=3 es d=6
    va = np.array([tarolo[k][2] for k in vegyes])
    vd = np.array([tarolo[k][3] for k in vegyes])
    rossz = 0
    for mm in range(1, n):
        N = n - mm
        A = frozenset(i for i, v in enumerate(va[:, N - 1]) if v <= va[:, N - 1].min() + 1e-9)
        B = frozenset(i for i, v in enumerate(vd[:, mm - 1]) if v <= vd[:, mm - 1].min() + 1e-9)
        if A != B:
            rossz += 1
    print("   d=3 es d=6 indulot osszeeresztve: a kriterium %d/%d toltesen TEVED."
          % (rossz, n - 1))
    print("   Ugyanaz a kriterium azonos koltsegvetesen 0/%d-en tevedett." % (n - 1))
    print()

    # --- KON-01 -------------------------------------------------------------
    print("== KON-01: mit hordoz a versenyszabaly (azonos koltsegvetes)? ==")
    print()
    a_n, a_lam = 20, tarolo["korlanc C20(1,3,5)"][1]          # d=6
    b_n, b_lam = tarolo["korlanc C20(1,10)"][0], tarolo["korlanc C20(1,10)"][1]  # d=3
    print("   ket indulo KULONBOZO koltsegvetessel: d=6 es d=3, azonos n=20")
    print("     nyomosszeguk: %.1f es %.1f -- %s"
          % (a_lam.sum(), b_lam.sum(), "AZONOS" if abs(a_lam.sum()-b_lam.sum()) < 1e-9
             else "KULONBOZO"))
    print()
    print("   Kovetkezmeny: a nyom-dontetlen NEM all, ezert a kiegeszitesi azonossag")
    print("   nem kozos T-vel dolgozik, es a teli veg NEM vezetheto vissza a lyuk-")
    print("   letrak osszehasonlitasara. A ket gorbe barmelyik toltesen elterhet")
    print("   annyival, amennyi a nyomkulonbseg -- a verseny ertelmetlenne valik.")
    ar_a, ar_b = np.cumsum(a_lam), np.cumsum(b_lam)
    print("     a teli toltesen az arkulonbseg: %.1f (a nyomkulonbseg)"
          % abs(ar_a[-1] - ar_b[-1]))
    print()
    print("   -> A KON-01 NEM artalmatlan konvencio: ez a nyom-dontetlen ELOFELTETELE,")
    print("      es rajta all az egesz teli-veg apparatus. De nem is onkenyes: eppen")
    print("      az teszi ertelmesse az osszehasonlitast, hogy azonos koltsegvetest")
    print("      helyezunk el. A merve ertek tehat: 'hordozo, de elvi'.")
    print()
    print("   (%.1f s)" % (time.time() - kezd))
    return 0 if mind and not elteres else 1


if __name__ == "__main__":
    raise SystemExit(main())
