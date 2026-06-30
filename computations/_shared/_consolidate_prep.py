#!/usr/bin/env python3
"""
Consolidate per-anchor re-run prep blocks into the master prep document.

Reads every `computations/_shared/t3-intake/prep_T3-*.md` and appends to
`computations/_shared/_review_prep.md` under a new
consolidation section. Skips any gate already present in the master.

Usage:
    python _consolidate_prep.py           # append new prep blocks only
    python _consolidate_prep.py --dry     # preview what would be added

NON-PHONONIC; no substitution-chain trigger.
"""
from __future__ import annotations

from canonical_constants import *  # noqa: F401,F403

import argparse
import re
from pathlib import Path
# === Phase 2b X2 transform bootstrap (auto-inserted by tools/_x2_transform_copies.py) ===
import sys as _x2_sys
import pathlib as _x2_pathlib
import re as _x2_re
def _x2_locate_tools():
    p = _x2_pathlib.Path(__file__).resolve()
    for _ in range(8):
        if (p / "tools" / "computation_root.py").is_file():
            return p / "tools"
        p = p.parent
    raise RuntimeError(
        "Phase 2b bootstrap: tools/computation_root.py not found in any "
        "ancestor of " + str(__file__))
_x2_sys.path.insert(0, str(_x2_locate_tools()))
from computation_root import resolve_script, resolve_output, resolve_glob, project_root as _x2_project_root
def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"
_x2_session_dir_match = _x2_re.match(r"^session-(\d+)$",
    _x2_pathlib.Path(__file__).resolve().parent.name)
_x2_self_session = int(_x2_session_dir_match.group(1)) if _x2_session_dir_match else None
# === End X2 bootstrap ===


PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'COMPUTATIONS_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)
INTAKE_DIR = resolve_script(None, 't3-intake')
MASTER_PREP = resolve_script(None, '_review_prep.md')


def _master_gate_ids() -> set[str]:
    if not MASTER_PREP.exists():
        return set()
    text = MASTER_PREP.read_text(encoding="utf-8")
    return set(re.findall(r"T3-[A-Z][A-Z0-9\-]+", text))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry", action="store_true",
                    help="Preview appends without writing")
    args = ap.parse_args()

    if not INTAKE_DIR.is_dir():
        print(f"ERROR: intake dir missing: {INTAKE_DIR}")
        return 2
    if not MASTER_PREP.exists():
        print(f"ERROR: master prep missing: {MASTER_PREP}")
        return 2

    existing = _master_gate_ids()
    prep_files = sorted(INTAKE_DIR.glob("prep_T3-*.md"))
    if not prep_files:
        print("No prep_T3-*.md files in intake.")
        return 0

    to_append: list[tuple[Path, str, str]] = []
    skipped: list[tuple[Path, str]] = []

    for f in prep_files:
        m = re.search(r"prep_(T3-[A-Z][A-Z0-9\-]+)\.md$", f.name)
        if not m:
            continue
        gate_id = m.group(1)
        if gate_id in existing:
            skipped.append((f, gate_id))
            continue
        body = f.read_text(encoding="utf-8").strip()
        to_append.append((f, gate_id, body))

    print(f"Prep files scanned: {len(prep_files)}")
    print(f"  new (will append):  {len(to_append)}")
    print(f"  already in master:  {len(skipped)}")
    for f, gid in skipped:
        print(f"    [SKIP]   {gid}")
    for f, gid, _ in to_append:
        print(f"    [APPEND] {gid}")

    if args.dry or not to_append:
        return 0

    append = [
        "\n\n## S81 Extended Anchor Prep Blocks (added during Level 3 batch "
        "re-runs)\n\n",
        "These entries extend the master prep doc from the top-40 snapshot "
        "to a complete per-anchor index. Each prep block was written "
        "alongside the corresponding Level 3 verdict.\n",
    ]
    for _, gid, body in to_append:
        append.append(f"\n---\n\n{body}\n")
    with MASTER_PREP.open("a", encoding="utf-8") as out:
        out.write("".join(append))
    print(f"\nAppended {len(to_append)} prep block(s) to {MASTER_PREP}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
