#!/usr/bin/env python3
"""path_existence.py - dead-path audit + suggested-fix applicator.

Replaces _path_existence_audit.py + _path_existence_fix.py with one entry
point. Used by /weave --update Phase 7 and /weave --audit-paths.

Subcommands:
  audit       - Scan computations/ Python files for `Path()` / `os.path.join()`
                refs that resolve to non-existent files. Outputs a stdout
                report and (with --json) tools/_path_existence_audit_report.json.
                --strict exits 1 on any dead refs (CI gating).
  fix         - Consume the audit report and apply suggested substitutions to
                disk. Default is dry-run; --execute writes.

Why this audit exists:
  The abandoned `_phase3_path_string_migration` moved file layouts:
    computations/canonical_constants.py  -> computations/_shared/canonical_constants.py
    computations/sN_<name>               -> computations/session-N/sN_<name>
    computations/_<name>                 -> computations/_shared/_<name>
    computations/<name>                  -> computations/_shared/<name>
  The migration was started but NOT FINISHED. Many session scripts still
  reference the pre-migration paths. The audit catches them; the fix
  applies the standard substitutions.

  Refs annotated `# soft prereq` / `# planned` / `# expected missing` are
  forward-pinned (legit refs to outputs from gates that haven't run yet) and
  excluded from the dead-refs list.
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

# ===========================================================================
# AUDIT - lifted from _path_existence_audit.py (main -> run_audit)
# ===========================================================================


# Pattern A: Path-form expressions
#   ROOT / "computations" / "X"  (one component)
#   ROOT / "computations" / "X" / "Y"  (two components)
# We capture the root variable name (for diagnostics) and the path components.
PATH_FORM_RE = re.compile(
    r'\b(?P<root>(?:PROJECT_)?ROOT|REPO(?:_ROOT)?|PROJ|HERE|repo_root|project_root)'
    r'\s*/\s*"computations"'
    r'(?:\s*/\s*"(?P<comp1>[^"]+)")'
    r'(?:\s*/\s*"(?P<comp2>[^"]+)")?'
    r'(?:\s*/\s*"(?P<comp3>[^"]+)")?'
)

# Pattern B: os.path.join form (single or double-quoted)
#   os.path.join(ROOT, "computations", "X")  or  (..., 'computations', 'X')
JOIN_FORM_RE = re.compile(
    r'os\.path\.join\([^)]*?["\']computations["\']\s*,\s*'
    r'["\'](?P<comp1>[^"\']+)["\']'
    r'(?:\s*,\s*["\'](?P<comp2>[^"\']+)["\'])?'
    r'(?:\s*,\s*["\'](?P<comp3>[^"\']+)["\'])?'
)


def scan_file(path: Path) -> list[dict]:
    """Return a list of {line, raw, components, resolved, exists} dicts
    for every Path/os.path.join reference in the file that points under
    `computations/`. Drops references where ALL components are wildcards
    (likely string-formatting templates)."""
    findings = []
    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return findings

    for lineno, line in enumerate(text.splitlines(), start=1):
        # Skip comments-only lines
        stripped = line.strip()
        if stripped.startswith("#"):
            continue

        for match_re in (PATH_FORM_RE, JOIN_FORM_RE):
            for m in match_re.finditer(line):
                components = []
                for key in ("comp1", "comp2", "comp3"):
                    val = m.group(key) if key in m.groupdict() else None
                    if val is not None:
                        components.append(val)
                if not components:
                    continue
                # Drop string-formatting templates: components containing { or %
                if any("{" in c or "%" in c for c in components):
                    continue
                resolved_rel = Path("computations", *components)
                resolved_abs = PROJECT_ROOT / resolved_rel
                exists = resolved_abs.exists()
                # Recognize explicit "expected missing" annotations on the same line.
                # These mark forward-pinned refs (planned outputs from gates that
                # haven't run yet, soft prereqs the script tolerates being missing,
                # or audit-acknowledged expected gaps). They are EXCLUDED from the
                # dead-refs list — the path form is correct, the file just doesn't
                # exist yet by design.
                expected_missing_markers = [
                    "# soft prereq",
                    "# planned",
                    "# expected missing",
                    "# AUDIT-EXPECTED-MISSING",
                    "expected missing",  # bare form (without # prefix)
                ]
                line_lower = line.lower()
                is_expected_missing = any(
                    marker.lower() in line_lower for marker in expected_missing_markers
                )
                findings.append({
                    "file": str(path.relative_to(PROJECT_ROOT)).replace("\\", "/"),
                    "line": lineno,
                    "raw": line.rstrip()[:200],
                    "components": components,
                    "resolved_rel": str(resolved_rel).replace("\\", "/"),
                    "exists": exists,
                    "expected_missing": is_expected_missing,
                })
    return findings


def collect_targets() -> list[Path]:
    """Return the list of source files to scan.

    Excludes self-referential audit/migration scripts whose docstrings/source
    contain example path patterns by design (would produce false positives).
    """
    SKIP = {
        # Audit/migration tooling: docstring examples match the regex but are
        # documentation, not actual code references.
        "tools/path_existence.py",
        "tools/_phase3_path_string_migration.py",
    }
    targets = []
    # Session scripts (high-leverage; the 35 files with broken refs)
    targets.extend(sorted((PROJECT_ROOT / "computations").glob("session-*/*.py")))
    # Shared infrastructure
    targets.extend(sorted((PROJECT_ROOT / "computations" / "_shared").glob("*.py")))
    # Tools
    targets.extend(sorted((PROJECT_ROOT / "tools").glob("*.py")))
    # Filter out self-referential files
    targets = [t for t in targets
               if str(t.relative_to(PROJECT_ROOT)).replace("\\", "/") not in SKIP]
    return targets


def categorize_finding(finding: dict) -> str:
    """Categorize a dead-reference finding by likely intent.

    Categories:
      - SESSION-FILE-MISLOCATED: bare `computations/sN_*` should be at
        `computations/session-N/sN_*` per migration rule #2.
      - SHARED-HELPER-MISLOCATED: bare `computations/_<helper>` should be at
        `computations/_shared/_<helper>` per migration rule #3.
      - GENERIC-MISLOCATED: bare `computations/<name>.py` should be at
        `computations/_shared/<name>.py` per migration rule #4.
      - UNKNOWN: no migration rule clearly applies.
    """
    components = finding["components"]
    if not components:
        return "UNKNOWN"
    head = components[0]
    if re.match(r"^s\d+_", head):
        return "SESSION-FILE-MISLOCATED"
    if head.startswith("_") and len(components) == 1 and head.endswith(".py"):
        return "SHARED-HELPER-MISLOCATED"
    if len(components) == 1 and (head.endswith(".py") or head.endswith(".npz") or
                                 head.endswith(".md") or head.endswith(".txt") or
                                 head.endswith(".json")):
        # bare-name; could go to _shared/ or session-N/ depending on prefix
        return "GENERIC-MISLOCATED"
    return "UNKNOWN"


def suggest_fix(finding: dict) -> str | None:
    """Return the most-likely correct path for a dead reference, or None.

    Handles three reference shapes:
      (1) <root>/computations/sN_X       -> tries session-N/sN_X then _shared/sN_X
      (2) <root>/computations/_X         -> tries _shared/_X
      (3) <root>/computations/_shared/sN_X (wrong-dir; sN_ files belong in session-N/)
                                          -> tries session-N/sN_X
      (4) <root>/computations/<bare>     -> tries _shared/<bare>
    """
    components = finding["components"]
    if not components:
        return None
    head = components[0]

    # Case (3): _shared/sN_X — wrong directory; sN_ files belong in session-N/
    if head == "_shared" and len(components) >= 2:
        second = components[1]
        sN_match = re.match(r"^s(\d+)_", second)
        if sN_match:
            session_num = int(sN_match.group(1))
            # Strip the wrong "_shared" component, replace with session-N
            tail_components = components[1:]  # drop "_shared", keep the rest
            suggested = Path("computations", f"session-{session_num}", *tail_components)
            if (PROJECT_ROOT / suggested).exists():
                return str(suggested).replace("\\", "/")

    # Case (1): bare sN_X (head starts with sN_ pattern)
    sN_match = re.match(r"^s(\d+)_", head)
    if sN_match:
        session_num = int(sN_match.group(1))
        suggested = Path("computations", f"session-{session_num}", *components)
        if (PROJECT_ROOT / suggested).exists():
            return str(suggested).replace("\\", "/")
        # Fallback: try _shared/
        suggested_shared = Path("computations", "_shared", *components)
        if (PROJECT_ROOT / suggested_shared).exists():
            return str(suggested_shared).replace("\\", "/")
        return None  # neither location has the file

    # Case (2): _X (helper module)
    if head.startswith("_") and head != "_shared":
        suggested = Path("computations", "_shared", *components)
        if (PROJECT_ROOT / suggested).exists():
            return str(suggested).replace("\\", "/")

    # Case (4): GENERIC: try _shared/
    suggested = Path("computations", "_shared", *components)
    if (PROJECT_ROOT / suggested).exists():
        return str(suggested).replace("\\", "/")

    return None


def run_audit(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    parser.add_argument("--json", action="store_true",
                        help="Emit JSON report to tools/_path_existence_audit_report.json")
    parser.add_argument("--strict", action="store_true",
                        help="Exit 1 if any dead refs found (for CI gating)")
    args = parser.parse_args(argv)

    targets = collect_targets()
    all_findings = []
    for path in targets:
        all_findings.extend(scan_file(path))

    # Split missing refs into "dead" (genuine bugs) vs "expected_missing"
    # (forward-pinned to gates that haven't run yet, marked with # soft prereq /
    # # planned / etc.).
    alive = [f for f in all_findings if f["exists"]]
    expected_missing = [f for f in all_findings
                        if not f["exists"] and f.get("expected_missing")]
    dead = [f for f in all_findings
            if not f["exists"] and not f.get("expected_missing")]

    # Categorize + suggest fixes for dead refs
    for f in dead:
        f["category"] = categorize_finding(f)
        f["suggested_fix"] = suggest_fix(f)

    # Group dead refs by file for stdout report
    by_file: dict[str, list[dict]] = {}
    for f in dead:
        by_file.setdefault(f["file"], []).append(f)

    print("=" * 76)
    print("PATH EXISTENCE AUDIT — dead-reference detection under computations/")
    print("=" * 76)
    print(f"Scanned files:                {len(targets)}")
    print(f"Total path refs:              {len(all_findings)}")
    print(f"Resolved (alive):             {len(alive)}")
    print(f"Expected-missing (annotated): {len(expected_missing)}")
    print(f"Dead references (real bugs):  {len(dead)}")
    print(f"Files with dead refs:         {len(by_file)}")
    print()
    if expected_missing:
        print(f"Expected-missing refs (forward-pinned, NOT bugs):")
        for f in expected_missing[:5]:
            print(f"  {f['file']}:{f['line']}  {f['resolved_rel']}")
        if len(expected_missing) > 5:
            print(f"  ... and {len(expected_missing) - 5} more")
        print()

    if dead:
        # Category histogram
        cat_counts: dict[str, int] = {}
        for f in dead:
            cat_counts[f["category"]] = cat_counts.get(f["category"], 0) + 1
        print("By category:")
        for cat, n in sorted(cat_counts.items(), key=lambda kv: -kv[1]):
            print(f"  {cat:35s} {n:4d}")
        print()

        # Files with most dead refs (top 20)
        file_counts = [(name, len(refs)) for name, refs in by_file.items()]
        file_counts.sort(key=lambda kv: -kv[1])
        print("Files by dead-ref count (top 20):")
        for name, n in file_counts[:20]:
            print(f"  {n:3d}  {name}")
        print()

        # Suggested-fix coverage
        with_fix = sum(1 for f in dead if f["suggested_fix"] is not None)
        print(f"Auto-suggested fix available: {with_fix}/{len(dead)} "
              f"({100.0*with_fix/len(dead):.1f}%)")
        no_fix = [f for f in dead if f["suggested_fix"] is None]
        if no_fix:
            print(f"\nUnresolvable dead refs (no fix candidate exists either):")
            for f in no_fix[:10]:
                print(f"  {f['file']}:{f['line']}  {f['resolved_rel']}")
            if len(no_fix) > 10:
                print(f"  ... and {len(no_fix) - 10} more (see --json for full list)")
        print()

    if args.json:
        out_path = PROJECT_ROOT / "tools" / "_path_existence_audit_report.json"
        out_path.write_text(json.dumps({
            "summary": {
                "scanned_files": len(targets),
                "total_refs": len(all_findings),
                "alive": len(alive),
                "expected_missing": len(expected_missing),
                "dead": len(dead),
                "files_with_dead_refs": len(by_file),
            },
            "dead_refs": dead,
            "expected_missing_refs": expected_missing,
        }, indent=2), encoding="utf-8")
        print(f"JSON report: {out_path.relative_to(PROJECT_ROOT)}")

    if args.strict and dead:
        print(f"\n[STRICT] FAIL — {len(dead)} dead path reference(s). See report above.")
        return 1

    if dead:
        print(f"\n[WARN] {len(dead)} dead path reference(s) found. "
              f"Run with --strict to exit non-zero, or --json for full list.")

    return 0


# ===========================================================================
# FIX - lifted from _path_existence_fix.py (main -> run_fix)
# ===========================================================================



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


def run_fix(argv=None):
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


# ---------------------------------------------------------------------------
# CLI dispatcher
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        prog="path_existence.py",
        description="Dead-path audit + suggested-fix applicator.",
    )
    sub = parser.add_subparsers(dest="cmd", required=True)
    audit_p = sub.add_parser("audit", help="Scan for dead path refs under computations/.")
    audit_p.add_argument("--json", action="store_true",
                         help="Emit JSON report to tools/_path_existence_audit_report.json")
    audit_p.add_argument("--strict", action="store_true",
                         help="Exit 1 if any dead refs found (for CI gating)")
    fix_p = sub.add_parser("fix", help="Apply suggested-fix substitutions to disk.")
    fix_p.add_argument("--report", type=Path, default=DEFAULT_REPORT,
                       help=f"Path to audit JSON report (default: {DEFAULT_REPORT.relative_to(PROJECT_ROOT)})")
    fix_p.add_argument("--execute", action="store_true",
                       help="Apply fixes to disk (default: dry-run)")
    fix_p.add_argument("--dry-run", action="store_true",
                       help="Explicit dry-run (default behavior)")
    args = parser.parse_args()
    if args.cmd == "audit":
        argv = []
        if args.json:
            argv.append("--json")
        if args.strict:
            argv.append("--strict")
        sys.exit(run_audit(argv))
    elif args.cmd == "fix":
        argv = ["--report", str(args.report)]
        if args.execute:
            argv.append("--execute")
        if args.dry_run:
            argv.append("--dry-run")
        sys.exit(run_fix(argv))


if __name__ == "__main__":
    main()
