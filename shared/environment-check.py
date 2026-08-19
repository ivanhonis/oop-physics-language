# environment-check.py — run this BEFORE any package script in shared/
#
# Why this exists. Several packages of Part II declare an extended-precision
# primary computation route (correction H3 of II/15): the cost curves are
# accumulated in np.longdouble, because the float64 accumulation error near
# the full end is larger than the fixed identity tolerance of 1e-8.
#
# np.longdouble is NOT the same width everywhere. On Linux/glibc with gcc or
# clang it is the 80-bit x87 extended type (16 bytes stored, ~18 significant
# digits). On Windows with the MSVC toolchain — and on some other platforms —
# numpy maps it onto float64. There it is silently the SAME type as float64,
# so the H3 correction has no effect and the scripts can report FAILS where
# the packages record HOLDS.
#
# This script measures the consequence instead of guessing it: it builds the
# real II/15 hypercube ladder (12^4 = 20736 beats, exact trace 165888) and
# reports how far the accumulated total lands from the exact value.
#
# Exit code: 0 if extended precision is genuinely available, 1 if not.
# Nothing here is a proof or a package result — it is an environment report.

import sys

try:
    import numpy as np
except ImportError:
    print("numpy is missing. Install the dependencies first:")
    print("    pip install -r requirements.txt")
    raise SystemExit(2)

TOLERANCE = 1e-8          # the fixed identity tolerance (PKG-15-2 L5, PKG-15-3)
EXACT_TRACE = 165888.0    # 2 * 4 * 20736 — the trace tie of II/15


def accumulation_error(dtype):
    """The II/15 J4 hypercube ladder, accumulated: how far the total lands
    from the exact trace. This is the quantity the fixed tolerance guards."""
    k = (2 * np.pi * np.arange(12)).astype(dtype) / 12
    one = 2.0 - 2.0 * np.cos(k)
    lam = (one[:, None, None, None] + one[None, :, None, None]
           + one[None, None, :, None] + one[None, None, None, :])
    total = np.cumsum(np.sort(lam.ravel()))[-1]
    return abs(float(total) - EXACT_TRACE)


def main():
    print("== environment check for the computation code in shared/ ==")
    print()
    print("interpreter : Python %s" % sys.version.split()[0])
    print("platform    : %s" % sys.platform)
    print("numpy       : %s" % np.__version__)
    print()

    ld_size = np.dtype(np.longdouble).itemsize
    f64_size = np.dtype(np.float64).itemsize
    ld_eps = float(np.finfo(np.longdouble).eps)
    f64_eps = float(np.finfo(np.float64).eps)
    extended = ld_eps < f64_eps

    print("np.longdouble : %d bytes, eps = %.3e" % (ld_size, ld_eps))
    print("np.float64    : %d bytes, eps = %.3e" % (f64_size, f64_eps))
    print("extended precision genuinely available: %s"
          % ("yes" if extended else "NO — longdouble is an alias of float64"))
    print()

    err_f64 = accumulation_error(np.float64)
    err_ld = accumulation_error(np.longdouble)
    print("measured consequence (II/15 ladder, 20736 beats, exact trace %d):"
          % EXACT_TRACE)
    print("   accumulated on float64    : deviation %.3e" % err_f64)
    print("   accumulated on longdouble : deviation %.3e" % err_ld)
    print("   fixed identity tolerance  : %.1e" % TOLERANCE)
    print()

    if extended and err_ld < TOLERANCE:
        print("VERDICT: OK — the extended-precision route works. The packages")
        print("that declare it (PKG-15-3, PKG-15-5, PKG-15-6, PKG-15-7,")
        print("PKG-16-2, PKG-16-3, PKG-16-5) will reproduce their published")
        print("numbers on this machine.")
        return 0

    print("VERDICT: DEGRADED — the extended-precision route is not available")
    print("on this machine, so the H3 correction of II/15 has no effect here.")
    print()
    print("What to expect. Near the full end the accumulated cost misses the")
    print("exact value by %.1e, which is above the fixed %.0e tolerance."
          % (err_ld, TOLERANCE))
    print("Concretely, PKG-15-7-top.py reports FAILS for its checks E2 and E3")
    print("(single-hole tie, mirror transfer) with a deviation around 2e-8,")
    print("where the package records 1.7e-13 and 2.2e-12. The same limitation")
    print("touches PKG-15-3, PKG-15-5, PKG-15-6, PKG-16-2, PKG-16-3, PKG-16-5.")
    print()
    print("This is an environment limit, not a result. The findings of the")
    print("packages are unaffected; only their reproduction on this machine is.")
    print("To reproduce them exactly, run the code on a platform where")
    print("np.longdouble is the 80-bit extended type — Linux/glibc with a gcc")
    print("or clang build of numpy is the usual choice.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
