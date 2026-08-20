# seal.py -- the seal of the prediction register (milestone P0.3)
#
# Why this exists. Every one of the sixteen proofs so far handed back a number
# that was already known. A prediction is a different animal: it is only worth
# anything if the claim provably could not move after the answer arrived. Prose
# cannot establish that. Two mechanisms can, together:
#
#   1. the seal -- a SHA-256 fingerprint of the substantive fields of the entry,
#      so any later edit of the claim, the window, or the pass/fail conditions
#      is detectable rather than invisible;
#   2. the commit -- the entry must be committed before the run, so git history
#      time-anchors it. The seal alone proves nothing: an uncommitted file can
#      be rewritten and resealed in one breath.
#
# Note what is deliberately NOT here: secrecy. The salt of a target-number vault
# hides a value the author must not peek at. This register does the opposite job
# -- it publishes the claim and freezes it. Anyone can recompute the seal; that
# is the point.
#
# Usage:
#   python shared/register/seal.py              # verify every entry
#   python shared/register/seal.py --pecsetel   # (re)seal entries that have none
#
# Exit code: 0 if every sealed entry matches its content, 1 otherwise.

import hashlib
import json
import subprocess
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ROOT = Path(__file__).resolve().parents[2]
REGISZTER = Path(__file__).resolve().parent / "predictions.json"

# Exactly the fields a prediction may not quietly change. Anything outside this
# list (state, commit hash, notes) may be updated as the work proceeds.
PECSETELT_MEZOK = ("id", "merfoldko", "datum", "kerdes", "joslat",
                   "megnevezett_gyoztes", "levezetes", "ablak",
                   "siker_felteteI", "siker", "bukas_felteteI",
                   "ismert_feszultseg")


def lenyomat(joslat):
    """Canonical fingerprint: sorted keys, no whitespace slack, UTF-8."""
    mag = {k: joslat.get(k) for k in PECSETELT_MEZOK}
    nyers = json.dumps(mag, sort_keys=True, ensure_ascii=False,
                       separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(nyers).hexdigest()


def git(*argv):
    try:
        p = subprocess.run(["git"] + list(argv), cwd=str(ROOT),
                           capture_output=True, text=True)
    except OSError:
        return None
    return p.stdout if p.returncode == 0 else None


def horgony(pecset, ut):
    """The commit that first introduced this seal, found in git history.

    Deliberately DERIVED, never hand-entered. A hash typed into the file would
    be worth nothing -- whoever can edit the claim can edit the hash beside it.
    `git log -S<seal>` answers a different question: in which commit did this
    exact fingerprint first appear in this file? Nobody can backdate that
    without rewriting history, which is itself visible."""
    if not pecset:
        return None, None, "pecset nelkul nincs horgony"
    ki = git("log", "-S" + pecset, "--format=%H %aI", "--reverse", "--", ut)
    if ki is None:
        return None, None, "a git nem erheto el"
    sorok = [s for s in ki.splitlines() if s.strip()]
    if not sorok:
        return None, None, "NINCS COMMITOLVA -- a bejegyzes ido-horgony nelkul all"
    hash_, ido = sorok[0].split()[:2]
    return hash_, ido, "%s (%s)" % (hash_[:12], ido)


def munkapeldany(ut):
    ki = git("status", "--porcelain", "--", ut)
    if ki is None:
        return "a git allapota nem olvashato"
    sor = ki.strip()
    if not sor:
        return "tiszta"
    if sor.startswith("??"):
        return "kovetetlen"
    return "modositva a commit ota (%s)" % sor.split()[0]


def main(argv):
    pecsetel = "--pecsetel" in argv

    print("== joslat-regiszter -- pecset-ellenorzes (P0.3) ==")
    print()
    if not REGISZTER.exists():
        print("HIBA: a regiszter nem talalhato: %s" % REGISZTER)
        return 1
    tar = json.loads(REGISZTER.read_text(encoding="utf-8"))
    joslatok = tar.get("joslatok", [])

    hibak, valtozott = [], False
    for j in joslatok:
        szamolt = lenyomat(j)
        rogzitett = j.get("pecset")
        azon = j.get("id", "?")

        if rogzitett is None:
            if pecsetel:
                j["pecset"] = szamolt
                valtozott = True
                print("  [PECSETELVE] %s  %s" % (azon, szamolt[:16]))
            else:
                print("  [PECSET NELKUL] %s -- futtasd: --pecsetel" % azon)
                hibak.append(azon)
            continue

        if rogzitett == szamolt:
            print("  [ALL] %-8s %s  (%s, %s)"
                  % (azon, rogzitett[:16], j.get("merfoldko"), j.get("allapot")))
        else:
            print("  [SERULT] %s -- a tartalom a pecsetelés ota megvaltozott!" % azon)
            print("           rogzitett: %s" % rogzitett[:32])
            print("           szamolt  : %s" % szamolt[:32])
            hibak.append(azon)

    print()
    ut = REGISZTER.relative_to(ROOT).as_posix()
    horgonytalan, sorok = [], []
    for j in joslatok:
        hash_, ido, uzenet = horgony(j.get("pecset"), ut)
        sorok.append("  ido-horgony %-8s %s" % (j.get("id", "?"), uzenet))
        if hash_ is None:
            horgonytalan.append(j.get("id"))
        elif j.get("commit") != hash_:
            j["commit"] = hash_          # derived cache, refreshed on every run
            valtozott = True

    if valtozott:
        REGISZTER.write_text(json.dumps(tar, ensure_ascii=False, indent=2) + "\n",
                             encoding="utf-8")

    print("  munkapeldany: %s" % munkapeldany(ut))
    for sor in sorok:
        print(sor)

    if horgonytalan:
        print()
        print("  FIGYELEM: pecset commit nelkul nem bizonyit vaksagot. A bejegyzest")
        print("            a FUTTATAS ELOTT commitolni kell, kulonben a joslat kesobb")
        print("            nem joslat lesz, hanem fegyelmezett retrodikcio.")
    print()

    if hibak:
        print("ITELET: BUKIK -- %d bejegyzes nem all: %s" % (len(hibak), ", ".join(hibak)))
        return 1
    print("ITELET: ALL -- minden bejegyzes pecsetje egyezik a tartalmaval.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
