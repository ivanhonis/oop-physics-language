# letra_feladat.py -- worker functions for the parallel runner
#
# Everything here must be importable in a fresh interpreter and must be a pure
# function of its arguments: same inputs, same bits out, no shared state, no
# global RNG, no reliance on which worker got there first. That is what makes a
# field of these safe to spread across cores -- and what the runner's rendproba
# re-checks afterwards instead of taking on trust.
#
# The ladder of a weave net C_n(steps) has a closed Fourier form: every beat is a
# sum of one-dimensional contributions, so no matrix is ever built. This is the
# closed route of appendix B, and its exact trace is known in advance --
# 2 * (number of steps) * n -- which gives every task its own built-in check.

import numpy as np

import summation


def letra(n, lepesek):
    """The beat ladder of the circulant weave C_n(lepesek), sorted from cheapest.

    Each step s contributes 2 - 2cos(2*pi*j*s/n) to beat j; the +/- pair of a step
    is one contract, so a net with k steps is 2k-regular."""
    j = np.arange(n, dtype=np.float64)
    lam = np.zeros(n, dtype=np.float64)
    for s in lepesek:
        lam += 2.0 - 2.0 * np.cos(2.0 * np.pi * j * float(s) / n)
    lam.sort()
    return lam


def letra_es_gorbe(n, lepesek, toltesek=None):
    """One entrant's ladder, its exact trace, and its cost curve read at the
    requested fillings -- the H4 portable route throughout.

    Returns scalars and a short vector, never the whole curve: 500 entrants x
    20736 floats would cost more in pickling than the arithmetic saved."""
    lepesek = tuple(int(s) for s in lepesek)
    lam = letra(n, lepesek)

    nyom = summation.pontos_osszeg(lam)
    egzakt_nyom = 2.0 * len(lepesek) * n

    gorbe = summation.pontos_cumsum(lam)
    if toltesek is None:
        toltesek = (1, n // 4, n // 2, n - 1, n)
    toltesek = tuple(int(t) for t in toltesek)

    return {
        "lepesek": lepesek,
        "nyom": nyom,
        "nyom_elteres": abs(nyom - egzakt_nyom),
        "nulla_modusok": int(np.count_nonzero(lam < 1e-12)),
        "csucs_utem": float(lam[-1]),
        "polcok": int(np.unique(np.round(lam, 10)).size),
        "toltesek": toltesek,
        "arak": tuple(float(gorbe[t - 1]) for t in toltesek),
    }


def paros_jegy(lepesek):
    """Does this entrant carry the mirror mark? On a circulant of even order the
    net is bipartite exactly when every step is odd -- no odd cycle can close."""
    return all(int(s) % 2 == 1 for s in lepesek)
