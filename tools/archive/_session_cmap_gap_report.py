"""Per-session gap report: which sessions lack a structured Constraint-Map
section in their workingpaper?

User directive (2026-05-19): "the workingpaper IS the planned output" +
"S67 has NO Constraint-Map section. That is fine - lets get a list of
sessions that have no results - then we can do a focus look at their
actual artifacts and update at the source."

Output: per-session classification table to stdout AND to
`tools/_session_cmap_gap_report.md`. Each session is one of:

  HAS_CMAP        — at least one WP file has `## Constraint[-\\s]?Map`
                    section; lists row counts the parser extracts.
  WP_NO_CMAP      — WP file(s) exist but none have the section. THE
                    GAP — these WPs need a Constraint-Map added.
  NO_WP           — no workingpaper file at all for this session
                    (per-session-results-WP nor per-wave-WP).

Throwaway diagnostic; safe to delete once the gap is addressed.
"""
from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from extract_entities import (  # noqa: E402
    _extract_closed_from_session_workingpaper,
    _WP_CMAP_SECTION_RE,
    _WP_FILENAME_RE,
    PROJECT_ROOT,
)


# Session-N identifier extraction from any session-directory name
# (e.g., "session-25" -> 25, "session-73a" -> "73a", "session-79" -> 79)
_SESSION_DIR_RE = re.compile(r"^session-(\d+[a-z]?)$", re.IGNORECASE)


def discover_sessions() -> dict[str, Path]:
    """Walk `sessions/` and `sessions/archive/` for per-session directories.

    Returns a dict mapping session_id (e.g., "S25", "S73a") to its
    directory Path.
    """
    sessions: dict[str, Path] = {}

    def scan(root: Path):
        if not root.exists():
            return
        for entry in root.iterdir():
            if not entry.is_dir():
                continue
            m = _SESSION_DIR_RE.match(entry.name)
            if not m:
                continue
            sid = "S" + m.group(1)
            # If both `sessions/session-N` and `sessions/archive/session-N`
            # exist, prefer the non-archive copy (the live session
            # directory). Archive copy is a fallback.
            if sid not in sessions:
                sessions[sid] = entry

    scan(PROJECT_ROOT / "sessions")
    scan(PROJECT_ROOT / "sessions" / "archive")
    return sessions


def find_wps(session_dir: Path) -> list[Path]:
    """All `*workingpaper.md` files in the session directory."""
    return sorted(p for p in session_dir.rglob("*workingpaper.md")
                  if _WP_FILENAME_RE.match(p.name))


def classify_session(session_id: str, session_dir: Path) -> dict:
    """Classify one session.

    Returns a dict with keys:
      session_id, session_dir, wp_files (list of Path),
      cmap_files (list of Path with Constraint-Map),
      closure_rows (total rows extracted across all WPs),
      status (HAS_CMAP | WP_NO_CMAP | NO_WP).
    """
    wps = find_wps(session_dir)
    cmap_files: list[Path] = []
    total_rows = 0

    for wp in wps:
        try:
            text = wp.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        if _WP_CMAP_SECTION_RE.search(text):
            cmap_files.append(wp)
            rows = _extract_closed_from_session_workingpaper(wp, text)
            total_rows += len(rows)

    if not wps:
        status = "NO_WP"
    elif cmap_files:
        status = "HAS_CMAP"
    else:
        status = "WP_NO_CMAP"

    return {
        "session_id": session_id,
        "session_dir": session_dir,
        "wp_files": wps,
        "cmap_files": cmap_files,
        "closure_rows": total_rows,
        "status": status,
    }


def session_sort_key(sid: str):
    """Sort sessions numerically with letter-suffix ordering."""
    m = re.match(r"^S(\d+)([a-z]?)$", sid)
    if not m:
        return (10_000, "")
    return (int(m.group(1)), m.group(2))


def main() -> int:
    sessions = discover_sessions()
    if not sessions:
        print("ERROR: no session directories found", file=sys.stderr)
        return 1

    rows = [classify_session(sid, sessions[sid])
            for sid in sorted(sessions, key=session_sort_key)]

    # Group by status
    by_status: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        by_status[r["status"]].append(r)

    # === Console summary ===
    print(f"Sessions scanned: {len(rows)}")
    print(f"  HAS_CMAP    : {len(by_status['HAS_CMAP']):>3}  "
          f"(WP has Constraint-Map section; parser extracts closures)")
    print(f"  WP_NO_CMAP  : {len(by_status['WP_NO_CMAP']):>3}  "
          f"(WP exists but no Constraint-Map — GAP to fix at source)")
    print(f"  NO_WP       : {len(by_status['NO_WP']):>3}  "
          f"(no workingpaper file at all)")

    total_rows = sum(r["closure_rows"] for r in rows)
    print(f"\nTotal closure rows extracted (HAS_CMAP only): {total_rows}")

    # === Markdown report ===
    report_path = PROJECT_ROOT / "tools" / "_session_cmap_gap_report.md"
    lines = [
        "# Session Constraint-Map Gap Report",
        "",
        "**Generated by**: `tools/_session_cmap_gap_report.py`",
        "",
        ("**Purpose**: Identify sessions whose workingpaper lacks a "
         "structured `## Constraint[-\\s]?Map` section. Per user "
         "directive (2026-05-19): the WP IS the planned output; the "
         "Constraint-Map section is the canonical closure registry. "
         "Sessions classified as `WP_NO_CMAP` are candidates for a "
         "focused per-session retrofit (add a Constraint-Map to the "
         "WP). Sessions classified as `NO_WP` lack a workingpaper "
         "entirely (no canonical closure registry possible)."),
        "",
        "## Summary",
        "",
        f"- Sessions scanned: **{len(rows)}**",
        f"- `HAS_CMAP` (parser-extractable): **{len(by_status['HAS_CMAP'])}** "
        f"sessions, **{total_rows}** total closure rows",
        f"- `WP_NO_CMAP` (gap — needs retrofit): "
        f"**{len(by_status['WP_NO_CMAP'])}** sessions",
        f"- `NO_WP` (no workingpaper at all): "
        f"**{len(by_status['NO_WP'])}** sessions",
        "",
        "## Per-Session Status",
        "",
        "| Session | Status | WP files | CMap files | Closures | Notes |",
        "|:--------|:-------|---:|---:|---:|:------|",
    ]
    for r in rows:
        sid = r["session_id"]
        status = r["status"]
        n_wp = len(r["wp_files"])
        n_cmap = len(r["cmap_files"])
        n_rows = r["closure_rows"]
        notes = ""
        if status == "WP_NO_CMAP":
            wp_names = [p.name for p in r["wp_files"][:3]]
            notes = ", ".join(wp_names)
            if n_wp > 3:
                notes += f", ... (+{n_wp - 3} more)"
        elif status == "NO_WP":
            notes = f"dir: `{r['session_dir'].relative_to(PROJECT_ROOT)}`"
        lines.append(
            f"| {sid} | {status} | {n_wp} | {n_cmap} | {n_rows} | {notes} |"
        )

    lines.append("")
    lines.append("## WP_NO_CMAP — Gap List (focus targets)")
    lines.append("")
    if not by_status["WP_NO_CMAP"]:
        lines.append("*(none — every session with a WP has a Constraint-Map section)*")
    else:
        lines.append("Sessions with workingpapers but no Constraint-Map section:")
        lines.append("")
        for r in by_status["WP_NO_CMAP"]:
            lines.append(f"### {r['session_id']}")
            lines.append("")
            lines.append(f"Directory: `{r['session_dir'].relative_to(PROJECT_ROOT)}`")
            lines.append("")
            lines.append("WP files (none with Constraint-Map):")
            for p in r["wp_files"]:
                lines.append(f"- `{p.relative_to(PROJECT_ROOT)}`")
            lines.append("")

    lines.append("")
    lines.append("## NO_WP — Sessions without any workingpaper")
    lines.append("")
    if not by_status["NO_WP"]:
        lines.append("*(none — every session directory has at least one WP)*")
    else:
        for r in by_status["NO_WP"]:
            lines.append(
                f"- **{r['session_id']}**: `{r['session_dir'].relative_to(PROJECT_ROOT)}`"
            )

    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Methodology")
    lines.append("")
    lines.append(
        "- **Session discovery**: walks `sessions/session-*/` and "
        "`sessions/archive/session-*/` directories matching the "
        "`session-N[a-z]?` naming convention."
    )
    lines.append(
        "- **WP file detection**: matches `*workingpaper.md` files "
        "passing the `_WP_FILENAME_RE` filter from `extract_entities.py`."
    )
    lines.append(
        "- **Constraint-Map detection**: the `_WP_CMAP_SECTION_RE` "
        "regex matches `## Constraint[-\\s]?Map[-\\s]?(?:Update|Updates)?` "
        "with optional Roman-numeral prefix (e.g., `## V. Constraint Map "
        "Update` in S40)."
    )
    lines.append(
        "- **Closure extraction**: rows are emitted when any cell "
        "contains a closure marker (`CLOSED`, `LANDED`, `PINNED`, "
        "`REGISTERED`, `PROMOTED`, `STAGE-3-PERMANENT`, etc.). "
        "Schema-tolerant: works across S43/S76/S86 column orderings."
    )

    report_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nReport written to: {report_path.relative_to(PROJECT_ROOT)}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
