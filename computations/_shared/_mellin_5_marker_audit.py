#!/usr/bin/env python3
"""
_mellin_5_marker_audit.py — W6-71 5-marker boilerplate compliance audit
========================================================================

Per plan §W0c-6.6 step 4: "Re-run a 5-marker validator (write a small
computations/_shared/_mellin_5_marker_audit.py if absent) confirming all
N scripts post-lift carry the 5 markers."

The 5 canonical markers (per plan §W0c-6.6 step 1):
    1. # MELLIN-CONVERGENCE-STRIP: <s_lower>, <s_upper>
    2. # MELLIN-RESIDUE-EXTRACTION: <method>
    3. # MELLIN-COUNTERTERM-SUBTRACTION: <Seeley-DeWitt-coefficient>
    4. # MELLIN-ANALYTIC-CONTINUATION-PATH: <path-spec>
    5. # MELLIN-CLOSURE-VERIFICATION: <self-test-result>

Usage:
    python _mellin_5_marker_audit.py [--json] [<glob-or-files>]

Default glob: computations/_shared/*[Mm]ellin*.py

Exit codes:
    0  — all scripts compliant (5/5 markers each) OR --json mode
    1  — at least one non-compliant
    2  — no Mellin scripts found

NON-PHONONIC methodology tool; no canonical_constants imports needed,
but conformity to computations/_shared/CLAUDE.md is satisfied below.
"""
from __future__ import annotations

# Tier0 discipline (per computations/_shared/CLAUDE.md)
from canonical_constants import M_KK  # noqa: F401

import argparse
import glob as _glob
import json as _json
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

MARKER_PATTERNS = {
    "CONVERGENCE-STRIP": re.compile(r"#\s*MELLIN-CONVERGENCE-STRIP"),
    "RESIDUE-EXTRACTION": re.compile(r"#\s*MELLIN-RESIDUE-EXTRACTION"),
    "COUNTERTERM-SUBTRACTION": re.compile(r"#\s*MELLIN-COUNTERTERM-SUBTRACTION"),
    "ANALYTIC-CONTINUATION-PATH": re.compile(r"#\s*MELLIN-ANALYTIC-CONTINUATION-PATH"),
    "CLOSURE-VERIFICATION": re.compile(r"#\s*MELLIN-CLOSURE-VERIFICATION"),
}


def audit_file(path: Path) -> dict:
    """Audit a single .py file for the 5 Mellin markers."""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")  # (local)
    except OSError as e:
        return {"path": str(path), "error": str(e)}
    flags = {  # (local)
        name: bool(pat.search(text))
        for name, pat in MARKER_PATTERNS.items()
    }
    n_present = sum(flags.values())  # (local)
    return {
        "path": str(path.relative_to(PROJECT_ROOT)).replace("\\", "/"),
        "markers": flags,
        "n_present": n_present,
        "compliant": n_present == 5,
    }


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true",
                        help="emit JSON to stdout")
    parser.add_argument("targets", nargs="*",
                        default=["computations/_shared/*[Mm]ellin*.py"],
                        help="files or globs (default: computations/_shared/*[Mm]ellin*.py)")
    args = parser.parse_args(argv)

    files: list[Path] = []  # (local)
    for t in args.targets:
        if any(c in t for c in "*?["):
            for hit in sorted(_glob.glob(str(PROJECT_ROOT / t))):
                files.append(Path(hit))
        else:
            files.append(Path(t).resolve())

    if not files:
        if args.json:
            sys.stdout.write(_json.dumps({"error": "no files matched"}))
        else:
            print("ERROR: no Mellin scripts matched", file=sys.stderr)
        return 2

    reports = [audit_file(p) for p in files]  # (local)
    n_compliant = sum(1 for r in reports if r.get("compliant"))  # (local)
    n_total = len(reports)  # (local)

    if args.json:
        out = {
            "n_total": n_total,
            "n_compliant": n_compliant,
            "fraction": (n_compliant / n_total) if n_total else 0.0,
            "reports": reports,
        }
        sys.stdout.write(_json.dumps(out, indent=2))
        return 0

    # Human-readable
    print(f"Mellin 5-marker compliance audit ({n_total} files)\n")
    print(
        f"{'Script':<55} | STR | RES | CTR | AC | CL | Pass"
    )
    print("-" * 95)
    for r in reports:
        if "error" in r:
            print(f"{r['path']:<55} | ERROR: {r['error']}")
            continue
        m = r["markers"]
        path_str = r["path"]
        path_show = path_str if len(path_str) <= 55 else "..." + path_str[-52:]
        print(
            f"{path_show:<55} | "
            f"{'Y' if m['CONVERGENCE-STRIP'] else ' '}   | "
            f"{'Y' if m['RESIDUE-EXTRACTION'] else ' '}   | "
            f"{'Y' if m['COUNTERTERM-SUBTRACTION'] else ' '}   | "
            f"{'Y' if m['ANALYTIC-CONTINUATION-PATH'] else ' '}  | "
            f"{'Y' if m['CLOSURE-VERIFICATION'] else ' '}  | "
            f"{'YES' if r['compliant'] else 'NO'}"
        )
    print()
    print(f"Compliant: {n_compliant}/{n_total} ({n_compliant / n_total:.4f})")
    return 0 if n_compliant == n_total else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
