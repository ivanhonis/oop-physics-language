# summation.py -- the portable exact-summation route (correction H4)
#
# Why this exists. Filling a ladder from below means one long running sum over
# tens of thousands of beats, and a naive running sum drifts: on the II/15
# ladder (20736 beats, exact trace 165888) plain np.cumsum lands 1.9e-08 away
# from the exact value -- above the fixed identity tolerance of 1e-08.
#
# Correction H3 of II/15 answered this by switching the primary route to
# np.longdouble. That answer is platform-dependent: np.longdouble is the 80-bit
# extended type only where the C toolchain provides it (Linux/glibc with gcc or
# clang). On Windows with MSVC it is an ALIAS of float64, so the correction is
# silently inoperative -- and worse, any check that compares "the two routes"
# then compares a type with itself and reports a deviation of exactly zero: a
# green light covering nothing.
#
# H4 replaces the type-based fix with an algorithmic one. The drift comes from
# accumulating n terms in sequence, so the cure is to stop accumulating in
# sequence: cut the sorted ladder into short blocks, sum each block exactly with
# math.fsum (which is correctly rounded), chain the block totals exactly, and
# only inside a block let a short cumulative sum run. The error then scales with
# the block length, not with n.
#
# Measured on the 32 saved II/15 ladders, deviation of the full end from the
# exact trace:
#
#     np.cumsum, float64        1.930e-08     above the 1e-08 tolerance
#     np.cumsum, longdouble     1.930e-08     identical -- the alias, on Windows
#     this module               see self-test  far below the tolerance
#
# This route needs no extended type, so it holds on every platform, and it lets
# the two-way rule be restated the way it should always have read: two
# ALGORITHMS, not two float widths (see appendix B).
#
# Self-test:  python shared/summation.py

import math

import numpy as np

BLOKK = 64          # block length; the error scales with this, not with n
TURES = 1e-8        # the fixed identity tolerance of the rulebook-era proofs


def pontos_osszeg(x):
    """The exact sum, correctly rounded. math.fsum keeps the partial remainders
    instead of discarding them, so the result is the nearest float to the true
    total regardless of ordering."""
    return math.fsum(np.asarray(x, dtype=np.float64).ravel().tolist())


def pontos_cumsum(x, blokk=BLOKK):
    """Cumulative sum with exact block offsets.

    Every entry is (exact prefix of all whole blocks before it) + (a short local
    cumulative sum inside its own block). The long chain is exact; only the last
    few additions are ordinary float64, so the drift cannot build up over n.
    """
    x = np.asarray(x, dtype=np.float64).ravel()
    n = x.size
    if n == 0:
        return np.empty(0, dtype=np.float64)

    ki = np.empty(n, dtype=np.float64)
    blokkok = [x[i:i + blokk] for i in range(0, n, blokk)]

    # exact total of each block, then the exact running offset before each block
    osszegek = [math.fsum(b.tolist()) for b in blokkok]
    eltolas, futo = [], []
    for o in osszegek:
        eltolas.append(math.fsum(futo))
        futo.append(o)

    for i, (b, e) in enumerate(zip(blokkok, eltolas)):
        kezd = i * blokk
        ki[kezd:kezd + b.size] = np.cumsum(b) + e
    return ki


def ar(letra_rendezett, n):
    """The price of filling n: the n cheapest beats, exactly. For a single
    filling there is no reason to settle for anything less than fsum."""
    return math.fsum(np.asarray(letra_rendezett,
                                dtype=np.float64).ravel()[:n].tolist())


def argorbe(letra):
    """The whole cost curve of a ladder, filled from below."""
    return pontos_cumsum(np.sort(np.asarray(letra, dtype=np.float64).ravel()))


# --------------------------------------------------------------------- onproba

def _letra_II15():
    """The II/15 J4 hypercube ladder, built here so the self-test needs no cache:
    12^4 = 20736 beats, exact trace 2 * 4 * 20736 = 165888."""
    k = 2 * np.pi * np.arange(12) / 12
    egy = 2.0 - 2.0 * np.cos(k)
    lam = (egy[:, None, None, None] + egy[None, :, None, None]
           + egy[None, None, :, None] + egy[None, None, None, :])
    return np.sort(lam.ravel())


def onproba():
    print("== summation.py -- onproba (H4 hordozhato ut) ==")
    print()
    letra = _letra_II15()
    egzakt = 165888.0
    print("bemenet: a II/15 J4 letraja, %d utem, egzakt nyomosszeg %d"
          % (letra.size, egzakt))
    print()

    naiv = abs(float(np.cumsum(letra)[-1]) - egzakt)
    ld = abs(float(np.cumsum(letra.astype(np.longdouble))[-1]) - egzakt)
    h4 = abs(float(pontos_cumsum(letra)[-1]) - egzakt)
    fs = abs(pontos_osszeg(letra) - egzakt)

    print("  %-34s %10s  %s" % ("ut", "elteres", "a 1e-08 tures ellen"))
    print("  " + "-" * 62)
    for nev, ertek in (("np.cumsum, float64", naiv),
                       ("np.cumsum, longdouble (H3)", ld),
                       ("math.fsum (egyetlen pont)", fs),
                       ("pontos_cumsum (H4, blokk=%d)" % BLOKK, h4)):
        print("  %-34s %10.3e  %s"
              % (nev, ertek, "ALL" if ertek <= TURES else "BUKIK"))
    print()

    # the curve as a whole, not only its end: the race compares curves
    gorbe_h4 = pontos_cumsum(letra)
    gorbe_naiv = np.cumsum(letra)
    print("  a ket ut legnagyobb elterese a teljes gorben: %.3e"
          % float(np.max(np.abs(gorbe_h4 - gorbe_naiv))))

    # spot check against fsum at a few fillings, the readout's own quantity
    legrosszabb = 0.0
    for n in (1, 2, 17, 1000, 10368, 20735, 20736):
        legrosszabb = max(legrosszabb, abs(gorbe_h4[n - 1] - ar(letra, n)))
    print("  pontos_cumsum kontra fsum het toltesen, legnagyobb elteres: %.3e"
          % legrosszabb)
    print()

    jo = h4 <= TURES and fs <= TURES
    print("ITELET: %s" % ("ALL -- a hordozhato ut a rogzitett tures alatt marad."
                          if jo else "BUKIK -- a hordozhato ut sem eri el a turest."))
    return 0 if jo else 1


if __name__ == "__main__":
    raise SystemExit(onproba())
