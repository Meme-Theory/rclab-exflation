"""
_f2_f4_vocabulary_audit.py

F_2 vs F_4 vocabulary audit (T4-16, S86 W-9 AUDIT-3).

Purpose
-------
Knowledge-MCP-driven scan that flags any registry/script/working-paper
text using bare "F_4" without disambiguating between:

  - W4-2 P5 reading: F_2 = {zeta, SDW}                    (cardinality 2)
  - W14 plan reading: F_4 = {zeta, Zubarev, SDW}          (cardinality 3)

The W14-plan F_4 = {zeta, Zubarev, SDW} FAILS K-invariance at
9.240e-01 while F_2 = {zeta, SDW} PASSes at 0.0 (W4-2 P5 line 9
threshold pair PASS_thresh=1e-3, FAIL_thresh=1e-2). Aliasing the
two produces structurally false statements.

Audit modes
-----------
  --report      : human-readable hit list (default)
  --json        : machine-readable JSON with file/line/snippet rows
  --strict      : exit nonzero if any unresolved bare F_4 hits found
  --new-only    : only files whose mtime > S86 W-9 closure (2026-04-26)
  --include-paths PATH [PATH ...] : restrict scan to specific roots
                  (defaults to: computations/_shared/, sessions/,
                   .claude/agent-memory/)

Disambiguation acceptance criteria
----------------------------------
A bare "F_4" hit is RESOLVED (not flagged) if it appears within
  +/- 5 lines of any of the disambiguating tokens:

    W14-plan reading
    {zeta, Zubarev, SDW}
    cardinality 3
    Zubarev-included
    F_4-W14
    F_4_W14
    F_4 (W14)
    NOT F_2

OR if the file is in the protected source list (the workshop
extracts and W-9 source documents themselves), where the bare
F_4 appears as a quoted W14-plan symbol.

Source
------
S86 W-9 §D-R2.1 (lines 1014-1044) — F_2 vs F_4 vocabulary disambiguation.
S86 W-9 §T-CR2.1 (lines 1213-1247) — transit cross-correction.
S86 W-9 CANON-1 — Mellin 5-tuple at s=3.
S86 W-9 CANON-2 — K-invariance threshold pair (PASS=1e-3, FAIL=1e-2).

Provenance
----------
S86 W0c-7 housekeeping queue Tier-4 row T4-16.
Promoted from S86 W-9 AUDIT-3 (lizzi+transit, 2026-04-26).

Usage
-----
    python _f2_f4_vocabulary_audit.py
    python _f2_f4_vocabulary_audit.py --json
    python _f2_f4_vocabulary_audit.py --strict --new-only
    python _f2_f4_vocabulary_audit.py --include-paths sessions/archive/session-87
"""

from __future__ import annotations

import argparse
import datetime as _dt
import json
import os
import re
import sys
from pathlib import Path

# Project canonical constants (mandatory per .claude/rules/math-scripts.md S34+).
sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import *  # noqa: F401,F403


# ---------------------------------------------------------------------------
# Pinned audit parameters
# ---------------------------------------------------------------------------

# Bare-F_4 detector. Catches "F_4" word boundaries; ignores "F_42" etc.
BARE_F4_REGEX = re.compile(r"\bF_4\b")                    # (local)

# Lines around each hit to scan for disambiguators (+/- N lines).
DISAMBIG_WINDOW = 5                                       # (local)

# Acceptable disambiguating tokens (case-insensitive substring match
# within the +/- DISAMBIG_WINDOW context).
DISAMBIG_TOKENS = (                                       # (local)
    "w14-plan",
    "w14 plan",
    "{zeta, zubarev, sdw}",
    "{ζ, zubarev, sdw}",
    "cardinality 3",
    "zubarev-included",
    "f_4-w14",
    "f_4_w14",
    "f_4 (w14)",
    "not f_2",
    "f_4 ≠ f_2",
    "f_4 != f_2",
    "f_4 vs f_2",
    "f_2 vs f_4",
    "f_2/f_4 disambig",
    "f_4 disambig",
)

# Default scan roots (relative to project root).
DEFAULT_SCAN_ROOTS = (                                    # (local)
    "computations",
    "sessions",
    ".claude/agent-memory",
)

# File extensions to scan.
SCAN_EXTENSIONS = (".py", ".md", ".txt", ".json")         # (local)

# Files exempt from scan (the workshop / extract sources themselves;
# bare F_4 appears as a quoted W14-plan symbol per source design).
EXEMPT_PATHS = (                                          # (local)
    "sessions/archive/session-86/_housekeeping-extract-w9.md",
    "sessions/archive/session-86/workshops/s86-w9-pathc-reassessment.md",
    "computations/_shared/_f2_f4_vocabulary_audit.py",       # (this script's own docstring)
)

# S86 W-9 closure timestamp (UTC, ISO 8601). Files modified on or
# after this date are considered "new" (post-disambiguation-rule).
S86_W9_CLOSURE_TS = _dt.datetime(2026, 4, 26, 0, 0, 0, tzinfo=_dt.timezone.utc)  # (local)


# ---------------------------------------------------------------------------
# Core audit logic
# ---------------------------------------------------------------------------

def _file_mtime_utc(path: Path) -> _dt.datetime:
    """Return file mtime as UTC datetime."""
    ts = path.stat().st_mtime                             # (local)
    return _dt.datetime.fromtimestamp(ts, tz=_dt.timezone.utc)


def _is_exempt(path: Path, project_root: Path) -> bool:
    """Check whether file is in the exempt source list."""
    try:
        rel = path.relative_to(project_root).as_posix()   # (local)
    except ValueError:
        rel = path.as_posix()
    return rel in EXEMPT_PATHS


def _has_disambiguator(lines: list[str], hit_idx: int, window: int = DISAMBIG_WINDOW) -> bool:
    """Check whether any disambiguating token appears within +/- window lines."""
    lo = max(0, hit_idx - window)                         # (local)
    hi = min(len(lines), hit_idx + window + 1)            # (local)
    context = "\n".join(lines[lo:hi]).lower()             # (local)
    return any(token in context for token in DISAMBIG_TOKENS)


def scan_file(path: Path, project_root: Path) -> list[dict]:
    """Scan a single file for unresolved bare F_4 hits.

    Returns list of hit-dicts: {line_no, snippet, resolved}.
    """
    if _is_exempt(path, project_root):
        return []
    try:
        text = path.read_text(encoding="utf-8", errors="replace")  # (local)
    except OSError:
        return []
    lines = text.splitlines()                             # (local)
    hits = []                                             # (local)
    for i, line in enumerate(lines):
        if BARE_F4_REGEX.search(line):
            resolved = _has_disambiguator(lines, i)       # (local)
            hits.append({
                "line_no": i + 1,
                "snippet": line.strip()[:200],
                "resolved": resolved,
            })
    return hits


def walk_scan_root(root: Path, project_root: Path, new_only: bool = False) -> list[Path]:
    """Yield candidate files under root with allowed extensions."""
    out = []                                              # (local)
    if not root.exists():
        return out
    for dirpath, dirnames, filenames in os.walk(root):
        # Skip generated / cache directories.
        dirnames[:] = [d for d in dirnames if d not in ("__pycache__", ".git", "node_modules")]
        for fn in filenames:
            if not fn.endswith(SCAN_EXTENSIONS):
                continue
            p = Path(dirpath) / fn                        # (local)
            if new_only and _file_mtime_utc(p) < S86_W9_CLOSURE_TS:
                continue
            out.append(p)
    return out


def run_audit(
    project_root: Path,
    scan_roots: tuple[str, ...] = DEFAULT_SCAN_ROOTS,
    new_only: bool = False,
) -> dict:
    """Execute the F_2/F_4 vocabulary audit."""
    file_results = []                                     # (local)
    total_hits = 0                                        # (local)
    unresolved_hits = 0                                   # (local)
    files_with_unresolved = 0                             # (local)

    for root_str in scan_roots:
        root = project_root / root_str                    # (local)
        candidates = walk_scan_root(root, project_root, new_only=new_only)  # (local)
        for path in candidates:
            hits = scan_file(path, project_root)          # (local)
            if not hits:
                continue
            file_unresolved = [h for h in hits if not h["resolved"]]  # (local)
            total_hits += len(hits)
            unresolved_hits += len(file_unresolved)
            if file_unresolved:
                files_with_unresolved += 1
            try:
                rel = path.relative_to(project_root).as_posix()
            except ValueError:
                rel = path.as_posix()
            file_results.append({
                "path": rel,
                "total_hits": len(hits),
                "unresolved_count": len(file_unresolved),
                "hits": hits,
            })

    verdict = "PASS" if unresolved_hits == 0 else "FAIL"  # (local)

    return {
        "audit_id": "S86-W9-F2-F4-VOCABULARY",
        "verdict": verdict,
        "scan_roots": list(scan_roots),
        "new_only": new_only,
        "totals": {
            "files_scanned_with_hits": len(file_results),
            "total_F4_hits": total_hits,
            "unresolved_hits": unresolved_hits,
            "files_with_unresolved": files_with_unresolved,
        },
        "file_results": file_results,
        "disambiguator_tokens": list(DISAMBIG_TOKENS),
        "exempt_paths": list(EXEMPT_PATHS),
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _format_report(result: dict) -> str:
    lines = []                                             # (local)
    lines.append(f"=== {result['audit_id']} ===")
    lines.append(f"Verdict: {result['verdict']}")
    lines.append(f"Scan roots: {', '.join(result['scan_roots'])}")
    lines.append(f"New-only mode: {result['new_only']}")
    lines.append("")
    t = result["totals"]                                   # (local)
    lines.append(f"Files with F_4 hits: {t['files_scanned_with_hits']}")
    lines.append(f"Total bare-F_4 hits: {t['total_F4_hits']}")
    lines.append(f"Unresolved hits   : {t['unresolved_hits']}")
    lines.append(f"Files with unresolved hits: {t['files_with_unresolved']}")
    lines.append("")
    if t["unresolved_hits"] > 0:
        lines.append("Unresolved hit detail (first 50):")
        shown = 0                                          # (local)
        for fr in result["file_results"]:
            if fr["unresolved_count"] == 0:
                continue
            for h in fr["hits"]:
                if h["resolved"]:
                    continue
                if shown >= 50:
                    break
                lines.append(f"  {fr['path']}:{h['line_no']}: {h['snippet']}")
                shown += 1
            if shown >= 50:
                break
    else:
        lines.append("All bare-F_4 occurrences resolved by nearby disambiguators "
                     "or appear in exempt source files.")
    return "\n".join(lines)


def _project_root() -> Path:
    """Detect project root by walking up from script location."""
    p = Path(__file__).resolve().parent                   # (local)
    while p != p.parent:
        if (p / "CLAUDE.md").exists() and (p / "computations").exists():
            return p
        p = p.parent
    return Path(__file__).resolve().parent.parent


def main() -> int:
    parser = argparse.ArgumentParser(
        description="F_2 vs F_4 vocabulary audit (T4-16)"
    )
    parser.add_argument("--json", action="store_true",
                        help="emit machine-readable JSON")
    parser.add_argument("--strict", action="store_true",
                        help="exit nonzero if any unresolved hits found")
    parser.add_argument("--new-only", action="store_true",
                        help="restrict scan to files modified after S86 W-9 closure")
    parser.add_argument("--include-paths", nargs="+",
                        help="override scan roots (project-relative paths)")
    args = parser.parse_args()

    root = _project_root()                                # (local)
    scan_roots = tuple(args.include_paths) if args.include_paths else DEFAULT_SCAN_ROOTS

    result = run_audit(root, scan_roots, new_only=args.new_only)  # (local)

    if args.json:
        print(json.dumps(result, indent=2, default=str))
    else:
        print(_format_report(result))

    if args.strict and result["verdict"] == "FAIL":
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
