#!/usr/bin/env python3
"""tools/_path_existence_fix.py — apply auto-suggested fixes from the audit.

Consumes the JSON report from `_path_existence_audit.py --json` and applies
targeted line-level regex substitutions to fix dead `computations/X` path
references where the audit identified an unambiguous correct location.

Substitution rules:
  Path-form:        ROOT / "computations" / "X"  -> ROOT / "computations" / "<sub>" / "X"
  os.path.join form:  os.path.join(ROOT, "computations", "X")
                   ->  os.path.join(ROOT, "computations", "<sub>", "X")

where <sub> is "_shared" or "session-N" per the audit's suggested_fix.

Usage:
  --dry-run (default): scan + report file count and total replacements; no writes.
  --execute:           apply replacements to disk.
  --report PATH:       use a specific report file (default: tools/_path_existence_audit_report.json).

Skips findings without a suggested_fix (the 8 unresolvable refs in current corpus).
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_REPORT = PROJECT_ROOT / "tools" / "_path_existence_audit_report.json"


def build_substitution_patterns(finding: dict) -> tuple[str, str] | None:
    """Build (old_substring, new_substring) for a single finding.

    Returns None if the substitution can't be constructed unambiguously.
    """
    components = finding["components"]
    suggested_rel = finding.get("suggested_fix")
    if not suggested_rel:
        return None

    suggested_parts = suggested_rel.split("/")
    if not suggested_parts or suggested_parts[0] != "computations":
        return None
    suggested_tail = suggested_parts[1:]  # drop "computations" prefix

    raw = finding["raw"]
    is_path_form = " / " in raw and '"computations"' in raw
    is_join_form = "os.path.join" in raw

    # SHAPE A — INSERT: suggested = [<inserted>, *components]
    #   e.g., original "computations/sN_X" -> "computations/session-N/sN_X"
    #   suggested_tail = ["session-N", "sN_X"]; components = ["sN_X"]
    if (len(suggested_tail) == len(components) + 1
            and suggested_tail[1:] == components):
        sub = suggested_tail[0]
        if is_path_form:
            comp_str = " / ".join(f'"{c}"' for c in components)
            old_substr = f'"computations" / {comp_str}'
            new_substr = f'"computations" / "{sub}" / {comp_str}'
            return old_substr, new_substr
        if is_join_form:
            for quote in ['"', "'"]:
                comp_str = ", ".join(f'{quote}{c}{quote}' for c in components)
                old_substr = f'{quote}computations{quote}, {comp_str}'
                new_substr = f'{quote}computations{quote}, {quote}{sub}{quote}, {comp_str}'
                if old_substr in raw:
                    return old_substr, new_substr

    # SHAPE B — REPLACE-FIRST-COMPONENT: same component count, but
    # components[0] differs from suggested_tail[0], rest matches.
    #   e.g., original "computations/_shared/sN_X" -> "computations/session-N/sN_X"
    #   suggested_tail = ["session-N", "sN_X"]; components = ["_shared", "sN_X"]
    if (len(suggested_tail) == len(components)
            and suggested_tail[0] != components[0]
            and suggested_tail[1:] == components[1:]):
        old_first = components[0]
        new_first = suggested_tail[0]
        if is_path_form:
            comp_str_full = " / ".join(f'"{c}"' for c in components)
            new_comp_str = " / ".join(f'"{c}"' for c in [new_first] + components[1:])
            old_substr = f'"computations" / {comp_str_full}'
            new_substr = f'"computations" / {new_comp_str}'
            return old_substr, new_substr
        if is_join_form:
            for quote in ['"', "'"]:
                comp_str_full = ", ".join(f'{quote}{c}{quote}' for c in components)
                new_comp_str = ", ".join(f'{quote}{c}{quote}' for c in [new_first] + components[1:])
                old_substr = f'{quote}computations{quote}, {comp_str_full}'
                new_substr = f'{quote}computations{quote}, {new_comp_str}'
                if old_substr in raw:
                    return old_substr, new_substr

    return None


def apply_fixes_to_file(file_path: Path, findings: list[dict],
                       dry_run: bool) -> tuple[int, int]:
    """Apply fixes to a single file. Returns (applied, skipped)."""
    if not file_path.exists():
        print(f"  ERROR: file disappeared: {file_path}")
        return 0, len(findings)
    text = file_path.read_text(encoding="utf-8")
    original_text = text
    applied = 0
    skipped = 0
    for finding in findings:
        sub = build_substitution_patterns(finding)
        if sub is None:
            skipped += 1
            continue
        old_substr, new_substr = sub
        if old_substr not in text:
            print(f"  WARN: substring not found at line {finding['line']}: {old_substr[:60]}")
            skipped += 1
            continue
        # Replace ONLY ONE occurrence per finding (to handle files with multiple
        # similar-but-distinct refs). Find first occurrence and replace it.
        text = text.replace(old_substr, new_substr, 1)
        applied += 1
    if applied > 0 and not dry_run and text != original_text:
        file_path.write_text(text, encoding="utf-8")
    return applied, skipped


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT,
                        help=f"Path to audit JSON report (default: {DEFAULT_REPORT.relative_to(PROJECT_ROOT)})")
    parser.add_argument("--execute", action="store_true",
                        help="Apply fixes to disk (default: dry-run)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Explicit dry-run (default behavior)")
    args = parser.parse_args(argv)

    if not args.report.exists():
        print(f"ERROR: report not found at {args.report}")
        print("Run: python tools/_path_existence_audit.py --json")
        return 1

    report = json.loads(args.report.read_text(encoding="utf-8"))
    dead = report["dead_refs"]
    fixable = [f for f in dead if f.get("suggested_fix")]

    # Group by file
    by_file: dict[str, list[dict]] = defaultdict(list)
    for f in fixable:
        by_file[f["file"]].append(f)

    dry_run = not args.execute

    print("=" * 76)
    print(f"PATH EXISTENCE FIX — {'DRY-RUN' if dry_run else 'EXECUTE'}")
    print("=" * 76)
    print(f"Report:           {args.report.relative_to(PROJECT_ROOT)}")
    print(f"Total dead refs:  {len(dead)}")
    print(f"Fixable:          {len(fixable)}")
    print(f"Unfixable:        {len(dead) - len(fixable)}")
    print(f"Files to modify:  {len(by_file)}")
    print()

    total_applied = 0
    total_skipped = 0
    for fname, findings in sorted(by_file.items()):
        file_path = PROJECT_ROOT / fname
        applied, skipped = apply_fixes_to_file(file_path, findings, dry_run)
        total_applied += applied
        total_skipped += skipped
        status = "[DRY]" if dry_run else "[FIX]"
        print(f"  {status} {fname}: {applied} applied, {skipped} skipped")

    print()
    print(f"Total: {total_applied} applied, {total_skipped} skipped "
          f"({'no files modified — dry-run' if dry_run else 'files written to disk'})")

    if dry_run:
        print("\nRe-run with --execute to apply.")
    else:
        print("\nVerify: python tools/_path_existence_audit.py")

    return 0


if __name__ == "__main__":
    sys.exit(main())
