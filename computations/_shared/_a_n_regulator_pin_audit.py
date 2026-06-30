#!/usr/bin/env python3
r"""
_a_n_regulator_pin_audit.py — bare-a_n Seeley-DeWitt regulator-pin audit
==========================================================================

Per plan §W0c-7.6 step 2: greps computations/_shared/*.py and computations/_shared/*.py
for the regex `\ba_(\d+)\b(?!\^)` (bare `a_n` not immediately followed by `^`)
and reports violations.

Per plan §W0c-7.6 step 2(d) (--retrofit flag): conservative auto-tagging
inferring regulator from comments or imports; ambiguous cases logged as
MANUAL_REVIEW_REQUIRED rather than auto-tagged (no false-positive tagging).

Usage:
    python _a_n_regulator_pin_audit.py                  # report mode
    python _a_n_regulator_pin_audit.py --json           # machine-readable
    python _a_n_regulator_pin_audit.py --retrofit       # conservative auto-tag
    python _a_n_regulator_pin_audit.py --new-only       # only post-S86 files
    python _a_n_regulator_pin_audit.py --target <path>  # audit ONE explicit file (any extension)

Scan scope (S94 W6-21 extension):
    The default scan globs computations/**/*.py + "computation archive"/**/*.py for the
    bare-a_n Seeley-DeWitt regex. S94-A_N-RETROFIT-C-CAUSALITY extended the scope to also
    cover the curated framework document sessions/framework/Phononic-C-Causality.md (added
    to MD_TARGETS below) so that --new-only can VERIFY the post-retrofit count
    (n_untagged_seeley_dewitt == 0) on the .md doc, and added the --target flag to audit any
    single explicit file. The bare-a_n regex `\ba_(\d+)\b(?!\^)` requires a DIGIT subscript,
    so generic-family `a_n` (literal letter n) is never matched; per-citation semantic review
    (NOT this mechanical regex) decides Seeley-DeWitt-vs-NSDW upstream of the audit.

Exit codes:
    0  — no bare a_n violations OR --json mode
    1  — violations found
    2  — IO error / no files matched
"""
from __future__ import annotations

from canonical_constants import M_KK  # noqa: F401  # framework-import discipline

import argparse
import datetime as _dt
import glob as _glob
import json as _json
import os
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
# True repository root (one level above computations/). MD_TARGETS + --target paths are
# repo-root-relative (S94 W6-21); the legacy TARGET_DIRS *.py glob stays PROJECT_ROOT-relative.
REPO_ROOT = PROJECT_ROOT.parent

# Regex: a_<digits> word boundary not followed by ^
BARE_A_N_PATTERN = re.compile(r"\ba_(\d+)\b(?!\^)")
TARGET_DIRS = ["computations", "computation archive"]
# Explicit non-.py framework documents pulled into scan scope (S94 W6-21 extension).
# These curated docs cite Seeley-DeWitt coefficients in prose and are retrofitted with
# a_n^{regulator} tags per regulator-pin-discipline.md; the audit must cover them so that
# --new-only verifies n_untagged_seeley_dewitt == 0 on the doc.
MD_TARGETS = ["sessions/framework/Phononic-C-Causality.md"]
S86_CUTOFF = _dt.datetime(2026, 4, 26)  # post-S86-W0c-7-promotion


def audit_file(path: Path) -> dict:
    """Audit a single file for bare a_n hits."""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")  # (local)
    except OSError as e:
        return {"path": str(path), "error": str(e)}
    hits = BARE_A_N_PATTERN.findall(text)  # (local)
    # Relativize against REPO_ROOT (covers both computations/ files and repo-root MD_TARGETS);
    # fall back to the absolute path string if the file lives outside the repo tree.
    try:
        rel = str(path.relative_to(REPO_ROOT)).replace("\\", "/")  # (local)
    except ValueError:
        rel = str(path).replace("\\", "/")  # (local)
    return {
        "path": rel,
        "n_violations": len(hits),
        "violations_by_n": dict((n, hits.count(n)) for n in set(hits)),
    }


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true",
                        help="emit JSON to stdout")
    parser.add_argument("--retrofit", action="store_true",
                        help="attempt conservative auto-tag (NOT YET IMPLEMENTED — would over-broaden")
    parser.add_argument("--new-only", action="store_true",
                        help="only audit files modified after S86 W0c-7 (2026-04-26)")
    parser.add_argument("--target", type=str, default=None,
                        help="audit ONE explicit file (any extension); bypasses the dir glob")
    args = parser.parse_args(argv)

    files: list[Path] = []  # (local)
    if args.target:
        # Single-file mode: audit exactly the named file (S94 W6-21 doc-verification path).
        # Relative paths resolve against the REPO ROOT (not computations/).
        tp = Path(args.target)  # (local)
        if not tp.is_absolute():
            tp = REPO_ROOT / args.target
        files.append(tp)
    else:
        for d in TARGET_DIRS:
            for hit in sorted(_glob.glob(str(PROJECT_ROOT / d / "**" / "*.py"),
                                         recursive=True)):
                p = Path(hit)  # (local)
                if args.new_only:
                    try:
                        mtime = _dt.datetime.fromtimestamp(p.stat().st_mtime)
                        if mtime < S86_CUTOFF:
                            continue
                    except OSError:
                        continue
                files.append(p)
        # Explicit .md framework-doc targets (S94 W6-21). Always scanned (curated docs are
        # always relevant to the regulator-pin discipline); --new-only mtime filter applies.
        # MD_TARGETS paths are repo-root-relative.
        for md in MD_TARGETS:
            p = Path(REPO_ROOT / md)  # (local)
            if not p.exists():
                continue
            if args.new_only:
                try:
                    mtime = _dt.datetime.fromtimestamp(p.stat().st_mtime)
                    if mtime < S86_CUTOFF:
                        continue
                except OSError:
                    continue
            files.append(p)

    if not files:
        if args.json:
            sys.stdout.write(_json.dumps({"error": "no files matched"}))
        else:
            print("ERROR: no files matched", file=sys.stderr)
        return 2

    reports = [audit_file(p) for p in files]  # (local)
    total_violations = sum(r.get("n_violations", 0) for r in reports)  # (local)
    files_with_violations = sum(
        1 for r in reports if r.get("n_violations", 0) > 0
    )  # (local)
    n_files = len(files)  # (local)

    if args.json:
        out = {
            "n_files_scanned": n_files,
            "files_with_violations": files_with_violations,
            "total_violations": total_violations,
            # Alias for the S94 W6-21 PASS criterion: each bare-a_n hit IS an untagged
            # Seeley-DeWitt coefficient AFTER the per-citation NSDW-annotation pass (the doc
            # has zero NSDW a_n; generic-family `a_n` with letter-n is not regex-matched).
            "n_untagged_seeley_dewitt": total_violations,
            "target": args.target,
            "new_only": args.new_only,
            "retrofit_executed": False,
            "reports": [r for r in reports if r.get("n_violations", 0) > 0],
        }
        sys.stdout.write(_json.dumps(out, indent=2))
        return 0 if total_violations == 0 else 1

    # Human-readable summary
    print(f"=== bare-a_n Seeley-DeWitt regulator-pin audit ===\n")
    print(f"Mode:                   {'NEW-ONLY (post-2026-04-26)' if args.new_only else 'ALL'}")
    print(f"Files scanned:          {n_files}")
    print(f"Files with violations:  {files_with_violations}")
    print(f"Total bare-a_n hits:    {total_violations}")
    print()
    if total_violations == 0:
        print("PASS: no bare a_n citations found.")
        return 0

    # Top 10 worst offenders
    sorted_reports = sorted(
        [r for r in reports if r.get("n_violations", 0) > 0],
        key=lambda r: r["n_violations"],
        reverse=True,
    )
    print("Top 10 files by violation count:")
    for r in sorted_reports[:10]:
        print(f"  {r['path']}: {r['n_violations']} hits")
    if len(sorted_reports) > 10:
        print(f"  ... ({len(sorted_reports) - 10} more files)")

    if args.retrofit:
        print()
        print("WARNING: --retrofit not implemented in S86 W0c-7. The regex")
        print(" `\\ba_(\\d+)\\b(?!\\^)` matches ANY a_n in code, not just")
        print(" Seeley-DeWitt coefficients (lattice spacings, plain variables,")
        print(" string literals, generic indices all match). Auto-tagging")
        print(" 20k violations would introduce semantic-mismatch false")
        print(" positives. Manual semantic review queued for S87+ as")
        print(" S87-A-N-SEELEY-DEWITT-RETROFIT.")

    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
