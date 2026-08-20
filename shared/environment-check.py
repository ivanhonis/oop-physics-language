# environment-check.py -- run this BEFORE any package script in shared/
#
# What this checks, and what changed.
#
# It used to ask a platform question: "is np.longdouble genuinely the 80-bit
# extended type here?" That mattered while correction H3 of II/15 made extended
# precision the primary computation route, because on Windows with MSVC
# np.longdouble is an ALIAS of float64 and the correction was silently
# inoperative there. The answer was to move the work to Linux.
#
# Correction H4 retires that route. The drift never came from the float width;
# it came from accumulating tens of thousands of terms in sequence. Summing in
# short blocks with exact block offsets (shared/summation.py) removes it in
# plain float64, on every platform. So the question this script asks is no
# longer "is your platform good enough" but "does the portable route hold here"
# -- and the expected answer is yes, everywhere.
#
# The reference environment below is declared, not required: it records where
# the published numbers of this repository are produced, so a third party can
# tell an environment difference from a result difference. A machine that does
# not match it should still pass this check. If it does not, that is a finding.
#
# Exit code: 0 if the portable route meets the fixed identity tolerance, 1 if not.

import os
import platform
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

try:
    import numpy as np
except ImportError:
    print("numpy is missing. Install the dependencies first:")
    print("    pip install -r requirements.txt")
    raise SystemExit(2)

import summation

# The declared reference environment: the machine on which the published
# numbers of this repository are produced. Recorded for comparison, not enforced.
REFERENCIA = {
    "os": "Windows 11 Pro",
    "python": "3.12.5",
    "numpy": "2.2.4",
    "cpu": "Intel i9, 8 mag / 16 szal",
    "ram": "128 GB",
    "megjegyzes": "A tesztek lokalisan futnak; az eroforras nem korlat. "
                  "A szamolasi ut (H4) platformfuggetlen, ezert mas gepen is all.",
}

EGZAKT_NYOM = 165888.0     # the II/15 J4 ladder: 2 * 4 * 20736


def memoria_gb():
    """Best-effort physical memory, standard library only."""
    try:
        if os.name == "nt":
            import ctypes

            class MEMORYSTATUSEX(ctypes.Structure):
                _fields_ = [("dwLength", ctypes.c_ulong),
                            ("dwMemoryLoad", ctypes.c_ulong),
                            ("ullTotalPhys", ctypes.c_ulonglong),
                            ("ullAvailPhys", ctypes.c_ulonglong),
                            ("ullTotalPageFile", ctypes.c_ulonglong),
                            ("ullAvailPageFile", ctypes.c_ulonglong),
                            ("ullTotalVirtual", ctypes.c_ulonglong),
                            ("ullAvailVirtual", ctypes.c_ulonglong),
                            ("ullAvailExtendedVirtual", ctypes.c_ulonglong)]

            st = MEMORYSTATUSEX()
            st.dwLength = ctypes.sizeof(st)
            ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(st))
            return st.ullTotalPhys / 2 ** 30
        return (os.sysconf("SC_PAGE_SIZE") * os.sysconf("SC_PHYS_PAGES")) / 2 ** 30
    except Exception:
        return None


def main():
    print("== environment check for the computation code in shared/ ==")
    print()

    ram = memoria_gb()
    print("this machine")
    print("   os          : %s %s" % (platform.system(), platform.release()))
    print("   interpreter : Python %s" % sys.version.split()[0])
    print("   numpy       : %s" % np.__version__)
    print("   cores       : %s logical" % (os.cpu_count() or "?"))
    print("   memory      : %s" % ("%.0f GB" % ram if ram else "unknown"))
    print()
    print("declared reference environment (for comparison, not a requirement)")
    for kulcs in ("os", "python", "numpy", "cpu", "ram"):
        print("   %-11s : %s" % (kulcs, REFERENCIA[kulcs]))
    print()

    # Recorded, no longer a blocker: this is what H3 depended on.
    kiterjesztett = float(np.finfo(np.longdouble).eps) < float(np.finfo(np.float64).eps)
    print("np.longdouble is genuinely extended here: %s"
          % ("yes" if kiterjesztett else "NO -- it is an alias of float64"))
    print("   (recorded only. Correction H4 retired the extended-precision route,")
    print("    so this no longer decides whether the packages can be reproduced.)")
    print()

    letra = summation._letra_II15()
    naiv = abs(float(np.cumsum(letra)[-1]) - EGZAKT_NYOM)
    h4 = abs(float(summation.pontos_cumsum(letra)[-1]) - EGZAKT_NYOM)

    print("the measured consequence (II/15 ladder, %d beats, exact trace %d):"
          % (letra.size, EGZAKT_NYOM))
    print("   naive running sum, float64 : deviation %.3e" % naiv)
    print("   portable route (H4)        : deviation %.3e" % h4)
    print("   fixed identity tolerance   : %.1e" % summation.TURES)
    print()

    if h4 <= summation.TURES:
        print("VERDICT: OK -- the portable route meets the fixed tolerance on this")
        print("machine, so the computation code can reproduce its published numbers")
        print("here. No extended-precision platform is required.")
        if naiv > summation.TURES:
            print()
            print("Note: the naive route would NOT meet the tolerance here (%.3e)."
                  % naiv)
            print("Package scripts still written against the retired H3 route report")
            print("failures on this machine until they are moved to shared/summation.py;")
            print("shared/bench/bench.py marks those checks separately, as pending H4")
            print("rather than as wrong numbers.")
        return 0

    print("VERDICT: FAILS -- the portable route does not meet the fixed tolerance")
    print("here (%.3e against %.1e). This is a genuine finding, not a platform"
          % (h4, summation.TURES))
    print("limitation: report it before running anything else.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
