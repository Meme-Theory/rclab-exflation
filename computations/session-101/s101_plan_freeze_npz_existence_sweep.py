"""S101 plan-freeze npz-existence sweep (orchestrator-effected).

Closes the _plan_upstream_pin_validator.py vacuity gap: the validator's per-gate
parser missed `input_files: path:` npz entries in several wave files (it
reported NO-UPSTREAM-NPZ while the gates do pin upstream npz). This sweep
mechanically extracts EVERY quoted *.npz path from every S101 wave plan and
checks on-disk existence, classifying s101-slugged absences as forward-pinned
in-session outputs (expected absent at plan-freeze).

canonical_constants exemption: plan-freeze audit tooling, zero framework
constants consumed (paths only) — same shape as the s88 append-helper
precedent.
"""
import glob
import os
import re
import sys


def main() -> int:
    missing = []
    forward = []
    found = 0  # (local)
    pat = re.compile(r'["\'`]((?:computations|sessions)/[^"\'`]+?\.npz)["\'`]')
    for f in sorted(glob.glob("sessions/session-plan/session-101-plan-w*.md")):
        if "validation" in f:
            continue
        with open(f, encoding="utf-8") as fh:
            txt = fh.read()
        refs = set(pat.findall(txt))
        for r in sorted(refs):
            if os.path.exists(r):
                found += 1
            elif "/session-101/" in r:
                forward.append((os.path.basename(f), r))
            else:
                missing.append((os.path.basename(f), r))
    print(f"EXISTING upstream npz refs verified on disk: {found}")
    print(f"FORWARD-PINNED s101 outputs (expected absent at freeze): {len(forward)}")
    for f_, r in forward:
        print(f"  fwd  {f_}: {r}")
    print(f"GENUINELY MISSING upstream npz: {len(missing)}")
    for f_, r in missing:
        print(f"  MISS {f_}: {r}")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
