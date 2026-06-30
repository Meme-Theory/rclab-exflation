"""tools/_phase3_path_string_migration.py — Phase 3: literal-string path migration.

Sed-style text replacement for string-literal `computations/...` and
`computations/...` references that the AST transformer (Phase 2b) didn't
catch because they're plain string literals (e.g. `np.load("computations/X")`),
not alias-mediated.

Substitution rules (most-specific first):
  computations/canonical_constants.py  -> computations/_shared/canonical_constants.py
  computations/sN_<name>               -> computations/session-N/sN_<name>
  computations/_<name>                 -> computations/_shared/_<name>
  computations/<name>                  -> computations/_shared/<name>
  computations/                        -> computations/_shared/
  computations/<helper>.py (mirrored 7)    -> computations/_shared/<helper>.py
  computations/sN_<name>                   -> computations/session-N/sN_<name>
  computations/_<name>                     -> computations/_shared/_<name>  (if mirrored)
  Other computations/...                   -> LEAVE (historical reference)

Target trees:
  computations/                  (re-process; AST-transformed files get extra string fixes)
  .claude/{rules,agents,templates,hooks}/
  tools/*.py (excluding computation_root.py + this script + transformer scripts)
  CLAUDE.md (project root)

Modes:
  --dry-run (default): scan + report file count and total replacements; no writes
  --execute:           apply replacements to disk

Logs to tools/_phase3_string_migration_log.jsonl.
"""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys


PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent
LOG_PATH = PROJECT_ROOT / "tools" / "_phase3_string_migration_log.jsonl"

ARCHIVE_HELPERS = {
    "dirac_spectrum.py", "spectral_action.py",
    "branching_computation.py", "r20a_riemann_tensor.py",
    "l20_lichnerowicz.py", "s23a_kosmann_singlet.py",
    "s35_pfaffian_corrected_j.py",
}

# Files to NOT migrate (would corrupt the migration tooling itself).
SKIP_FILES = {
    "tools/_x2_transform_copies.py",
    "tools/_phase3_path_string_migration.py",
    "tools/_mirror_to_computations.py",
    "tools/computation_root.py",
    "tools/_install_computation_roots_table.py",
    "tools/_phase1_inertness_check.py",
    "tools/_mirror_audit.py",
}


def migrate_text(text: str) -> tuple[str, int]:
    """Apply all migration rules. Returns (new_text, n_replacements)."""
    n = 0

    # computations/sN_<name> -> computations/session-N/sN_<name>
    def _t0_session_repl(m: re.Match) -> str:
        return f"computations/session-{m.group(2)}/s{m.group(2)}{m.group(3)}"
    new_text, count = re.subn(
        r"computations/(s(\d+)([_a-zA-Z][^\"'\s)`,]*))",
        _t0_session_repl,
        text,
    )
    n += count
    text = new_text

    # computations/_X -> computations/_shared/_X
    new_text, count = re.subn(
        r"computations/(_[^\"'\s)`,]*)",
        r"computations/_shared/\1",
        text,
    )
    n += count
    text = new_text

    # computations/X.ext (other) -> computations/_shared/X.ext
    new_text, count = re.subn(
        r"computations/([A-Za-z][^\"'\s)`,]*)",
        r"computations/_shared/\1",
        text,
    )
    n += count
    text = new_text

    # computations/ (bare path; e.g., "computations/" appearing alone)
    new_text, count = re.subn(
        r"\bcomputations/",
        r"computations/_shared/",
        text,
    )
    n += count
    text = new_text

    # computations/sN_<name> -> computations/session-N/sN_<name>
    def _archive_session_repl(m: re.Match) -> str:
        return f"computations/session-{m.group(2)}/s{m.group(2)}{m.group(3)}"
    new_text, count = re.subn(
        r"computations/(s(\d+)([_a-zA-Z][^\"'\s)`,]*))",
        _archive_session_repl,
        text,
    )
    n += count
    text = new_text

    # computations/<known-helper>.py -> computations/_shared/<helper>.py
    for helper in ARCHIVE_HELPERS:
        helper_escaped = re.escape(helper)
        new_text, count = re.subn(
            rf"computations/{helper_escaped}",
            f"computations/_shared/{helper}",
            text,
        )
        n += count
        text = new_text

    # computations/_shared (bare, no slash; mention as a directory NAME)
    new_text, count = re.subn(
        r"\bcomputations/_shared\b",
        r"computations",
        text,
    )
    n += count
    text = new_text

    # NOTE: we deliberately do NOT do a sweeping `computation-archive` -> `computations`
    # rewrite, since archive contains historical refs that should remain readable
    # as historical citations.

    return (text, n)


def find_target_files() -> list[pathlib.Path]:
    """Enumerate files to migrate."""
    targets: list[pathlib.Path] = []

    # All .py in computations/ (already AST-transformed; gets string fixes)
    for p in (PROJECT_ROOT / "computations").rglob("*.py"):
        targets.append(p)

    # All .md in computations/
    for p in (PROJECT_ROOT / "computations").rglob("*.md"):
        targets.append(p)

    # .claude/ subdirs
    for sub in ("rules", "agents", "templates", "hooks"):
        for ext in ("md", "py", "yaml", "yml", "sh", "json"):
            for p in (PROJECT_ROOT / ".claude" / sub).rglob(f"*.{ext}"):
                targets.append(p)

    # tools/*.py except SKIP_FILES
    for p in (PROJECT_ROOT / "tools").glob("*.py"):
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        if rel in SKIP_FILES:
            continue
        targets.append(p)

    # Project root CLAUDE.md
    claude_md = PROJECT_ROOT / "CLAUDE.md"
    if claude_md.is_file():
        targets.append(claude_md)

    return targets


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Phase 3 path-string migration.")
    parser.add_argument("--dry-run", action="store_true", default=True)
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--show", type=int, default=0,
                        help="Show first N file diffs in dry-run output")
    args = parser.parse_args()
    do_execute = args.execute and not args.dry_run if args.dry_run else args.execute

    files = find_target_files()
    print(f"[setup] target file count: {len(files)}")

    n_changed = 0
    total_repl = 0
    log: list[dict] = []
    samples: list[tuple[pathlib.Path, str, str]] = []

    for p in files:
        try:
            text = p.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        new_text, count = migrate_text(text)
        if count == 0:
            continue
        n_changed += 1
        total_repl += count
        rel = str(p.relative_to(PROJECT_ROOT))
        log.append({"path": rel, "replacements": count})
        if len(samples) < args.show:
            samples.append((p, text, new_text))
        if args.execute:
            try:
                p.write_text(new_text, encoding="utf-8")
            except OSError as e:
                log[-1]["write_error"] = str(e)

    LOG_PATH.write_text(
        json.dumps({"total_files_changed": n_changed,
                    "total_replacements": total_repl,
                    "files": log}, indent=2),
        encoding="utf-8")
    print(f"[plan] wrote {LOG_PATH.relative_to(PROJECT_ROOT)}")
    print()
    print(f"  files changed:       {n_changed}")
    print(f"  total replacements:  {total_repl}")
    if samples:
        print()
        print(f"  Sample diffs (first {len(samples)}):")
        for p, old, new in samples:
            rel = str(p.relative_to(PROJECT_ROOT))
            print(f"  --- {rel}")
            for old_line, new_line in zip(old.splitlines(), new.splitlines()):
                if old_line != new_line:
                    print(f"      - {old_line[:120]}")
                    print(f"      + {new_line[:120]}")
                    break  # one sample per file

    if not args.execute:
        print()
        print("[dry-run] no files modified. Re-run with --execute to apply.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
