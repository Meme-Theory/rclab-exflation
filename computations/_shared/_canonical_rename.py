#!/usr/bin/env python3
"""
Batch-rename observational-constant aliases to their canonical names.

For each (alias_name, canonical_name) pair in RENAME_MAP, scans every
Computation script and:

  1. If the script assigns `alias_name = <numeric>` at top level, replaces
     with `from canonical_constants import canonical_name as alias_name`
     when canonical_name != alias_name, or simply deletes the assignment
     and adds the import when both equal.
  2. Leaves untagged assignments alone when the value doesn't match the
     canonical value (those are genuinely local scan values, already
     `# (local)` tagged).

Conservative: only touches assignments matching `alias = <numeric>` at
low indent. Scripts with multi-line assignments or loops are skipped.

Gate: S81-CANONICAL-RENAME (NON-PHONONIC).

Usage:
    python _canonical_rename.py --dry
    python _canonical_rename.py
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
# X2-removed: legacy alias replaced (replaced by tools.computation_root.resolve_*)
ARCHIVE_DIR = PROJECT_ROOT / "computation archive"

# (alias_in_scripts, canonical_name_in_canonical_constants, canonical_value)
# Values must match exactly (absolute tolerance 1e-6 on floats).
RENAME_MAP: list[tuple[str, str, float]] = [
    ("n_s_FW",    "ns_framework",      0.9595),
    ("n_s_LCDM",  "planck_ns",         0.9649),
    ("ns_planck", "planck_ns",         0.9649),
    ("k_pivot",   "k_pivot_planck",    0.05),
    ("z_eq",      "z_eq_planck",       3387.0),
    ("r_GOE",     "r_GOE_canonical",   0.5307),
]

# Assignment regex: capture `alias = <numeric>` at any indent level where
# the line is pure assignment (may have trailing comment).
def _alias_re(alias: str) -> re.Pattern:
    return re.compile(
        r"^(?P<indent>\s*)"
        r"(?P<name>" + re.escape(alias) + r")"
        r"\s*=\s*"
        r"(?P<value>-?\d+(?:\.\d*)?(?:[eE][+-]?\d+)?)"
        r"\s*"
        r"(?P<comment>#.*)?$",
        re.MULTILINE,
    )


def _value_matches(text_value: str, canonical_value: float) -> bool:
    try:
        v = float(text_value)
    except ValueError:
        return False
    return abs(v - canonical_value) < max(1e-6, abs(canonical_value) * 1e-4)


def rename_in_file(path: Path) -> tuple[int, int]:
    """Return (renamed, scanned)."""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return 0, 0
    lines = text.splitlines(keepends=True)
    renamed = 0  # (local)
    scanned = 0  # (local)
    needed_imports: set[str] = set()

    out: list[str] = []
    for raw in lines:
        line = raw.rstrip("\n\r")
        newline = "\n" if raw.endswith("\n") else ""
        matched = False
        for alias, canonical, canon_value in RENAME_MAP:
            m = _alias_re(alias).match(line)
            if not m:
                continue
            scanned += 1
            if not _value_matches(m.group("value"), canon_value):
                # Value doesn't match canonical — this is a local scan/override
                break
            existing_comment = m.group("comment") or ""
            indent = m.group("indent")
            # Replace assignment with import-as-alias
            if alias == canonical:
                new_line = (
                    f"{indent}# {alias} imported from canonical_constants "
                    f"(was: {canon_value})"
                )
            else:
                new_line = (
                    f"{indent}{alias} = {canonical}  "
                    f"# canonical alias (was: = {m.group('value')})"
                )
            needed_imports.add(canonical)
            out.append(new_line + newline)
            renamed += 1
            matched = True
            break
        if not matched:
            out.append(raw)

    if renamed > 0:
        # Ensure needed imports are present. Find existing
        # `from canonical_constants import ...` line and extend it, or
        # add a new one.
        new_text = "".join(out)
        # If wildcard import, nothing to add.
        if re.search(r"from\s+canonical_constants\s+import\s+\*", new_text):
            pass
        else:
            # Find first explicit import line and extend.
            m = re.search(
                r"^(\s*from\s+canonical_constants\s+import\s+)"
                r"([^\n]+)$",
                new_text, re.MULTILINE,
            )
            if m:
                existing = m.group(2).strip()
                existing_list = {
                    s.strip().split(" as ")[0].strip()
                    for s in existing.split(",") if s.strip()
                }
                to_add = [n for n in sorted(needed_imports)
                          if n not in existing_list]
                if to_add:
                    new_import_line = (
                        f"{m.group(1)}{existing}, {', '.join(to_add)}"
                    )
                    new_text = (
                        new_text[:m.start()] + new_import_line
                        + new_text[m.end():]
                    )
            else:
                # No import line at all — insert one near the top.
                lines2 = new_text.splitlines(keepends=True)
                insert_at = 0  # (local)
                if lines2 and lines2[0].startswith("#!"):
                    insert_at = 1  # (local)
                # Skip module docstring
                if insert_at < len(lines2) and lines2[insert_at].lstrip().startswith(
                        ('"""', "'''")):
                    q = lines2[insert_at].lstrip()[:3]
                    insert_at += 1
                    while insert_at < len(lines2):
                        if q in lines2[insert_at]:
                            insert_at += 1
                            break
                        insert_at += 1
                new_import_line = (
                    f"from canonical_constants import "
                    f"{', '.join(sorted(needed_imports))}"
                    f"  # (canonical rename)\n"
                )
                lines2.insert(insert_at, new_import_line)
                new_text = "".join(lines2)
        path.write_text(new_text, encoding="utf-8")

    return renamed, scanned


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry", action="store_true",
                    help="Count renames without writing")
    args = ap.parse_args()

    total_renamed = 0  # (local)
    total_scanned = 0  # (local)
    files_touched = 0  # (local)
    for root in (COMPUTATIONS_DIR, ARCHIVE_DIR):
        if not root.is_dir():
            continue
        for f in root.glob("s*.py"):
            if args.dry:
                text = f.read_text(encoding="utf-8", errors="replace")
                file_renamed = 0  # (local)
                for alias, canonical, canon_value in RENAME_MAP:
                    for m in _alias_re(alias).finditer(text):
                        # multiline
                        total_scanned += 1
                        if _value_matches(m.group("value"), canon_value):
                            file_renamed += 1
                            total_renamed += 1
                if file_renamed > 0:
                    files_touched += 1
                continue
            r, s = rename_in_file(f)
            total_renamed += r
            total_scanned += s
            if r > 0:
                files_touched += 1
    print(f"Scanned {total_scanned} alias occurrences; "
          f"renamed {total_renamed} in {files_touched} files "
          f"{'(dry)' if args.dry else ''}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
