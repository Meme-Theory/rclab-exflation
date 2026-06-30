"""Build path_existence.py from _path_existence_audit.py + _path_existence_fix.py."""
import re
from pathlib import Path

tools = Path(__file__).resolve().parent
audit_src = (tools / '_path_existence_audit.py').read_text(encoding='utf-8')
fix_src = (tools / '_path_existence_fix.py').read_text(encoding='utf-8')

# ---- audit body: strip docstring/imports, strip __main__, rename main -> run_audit ----
m = re.search(r'\nPROJECT_ROOT = Path\(__file__\)\.resolve\(\)\.parent\.parent\n', audit_src)
assert m, "audit: PROJECT_ROOT anchor not found"
audit_body = audit_src[m.end():]
m2 = re.search(r'\nif __name__ == "__main__":', audit_body)
assert m2, "audit: __main__ not found"
audit_body = audit_body[:m2.start()].rstrip() + '\n'
audit_body = re.sub(r'\ndef main\(argv=None\)', '\ndef run_audit(argv=None)', audit_body)

# ---- fix body: strip docstring/imports, strip __main__, rename main -> run_fix ----
m = re.search(r'\nDEFAULT_REPORT = PROJECT_ROOT / "tools" / "_path_existence_audit_report\.json"\n', fix_src)
assert m, "fix: DEFAULT_REPORT anchor not found"
fix_body = fix_src[m.end():]
m2 = re.search(r'\nif __name__ == "__main__":', fix_body)
assert m2, "fix: __main__ not found"
fix_body = fix_body[:m2.start()].rstrip() + '\n'
fix_body = re.sub(r'\ndef main\(argv=None\)', '\ndef run_fix(argv=None)', fix_body)

HEADER = '''#!/usr/bin/env python3
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

'''

DISPATCHER = '''

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
'''

out = (
    HEADER
    + '# ===========================================================================\n'
    + '# AUDIT - lifted from _path_existence_audit.py (main -> run_audit)\n'
    + '# ===========================================================================\n\n'
    + audit_body
    + '\n\n# ===========================================================================\n'
    + '# FIX - lifted from _path_existence_fix.py (main -> run_fix)\n'
    + '# ===========================================================================\n\n'
    + fix_body
    + DISPATCHER
)

# Also: update the SKIP set inside the audit body to include the new path_existence.py
# (replacing the two old per-file entries).
out = out.replace(
    '"tools/_path_existence_audit.py",\n        "tools/_path_existence_fix.py",',
    '"tools/path_existence.py",'
)

out_path = tools / 'path_existence.py'
out_path.write_text(out, encoding='utf-8')
print(f"Wrote {out_path}")
print(f"  Size: {out_path.stat().st_size:,} bytes")
print(f"  Lines: {out.count(chr(10))}")
