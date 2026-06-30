#!/usr/bin/env python3
"""
S87 W1b WP duplicate-section cleanup tool.

Problem: 5 of 6 W1b agents wrote canonical content at the BOTTOM of the WP
(post-W13 region) instead of replacing the orchestrator-authored shells in
the W1b block (between §W1a-Wave-Synthesis and §W2-1). The two writers that
got this right were W1b-2 (line 813) and W1b-4 (line 968); W1b-1 and W1b-5
wrote substantive content post-W13 and reduced the shell to a pointer or
left it untouched; W1b-3 has not run yet; W1b-6 wrote at line 1108 after
SendMessage-resume.

Fix: idempotent one-shot rewrite that
  (a) MOVES the post-W13 §W1b-1 substantive section to the L803 shell
      location (overwriting the W1b-1 agent's pointer)
  (b) MOVES the post-W13 §W1b-5 substantive section to the L1087 shell
      location (overwriting the NOT STARTED placeholder)
  (c) DELETES all other post-W13 §W1b-N stubs (21-line NOT STARTED templates)
  (d) PRESERVES the post-W13 §W13-2 section + global Wave Synthesis tail.

The script is content-anchored (string match by `### §W1b-N.` heading
prefix) and atomic-write (read → process → temp file → rename). Re-runnable
without harm.

Usage:
    python computations/_shared/_s87_w1b_wp_dedupe_cleanup.py [--dry-run]
"""

from __future__ import annotations

import re
import shutil
import sys
from pathlib import Path

# Compliance import per .claude/rules/math-scripts.md (no constants needed
# by this hygiene tool, but the import is mandatory for computation scripts).
sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import *  # noqa: F401, F403

WP_PATH = Path("sessions/archive/session-87/session-87-results-workingpaper.md")
BACKUP_PATH = Path("sessions/archive/session-87/session-87-results-workingpaper.md.dedupe-backup")
DRY_RUN = "--dry-run" in sys.argv

W1B_HEADER_RE = re.compile(r"^### §W1b-([1-6])\. ", re.MULTILINE)
W1B_TERMINATOR_RE = re.compile(r"^### §|^## ", re.MULTILINE)


def find_section(text: str, marker: str, occurrence: int) -> tuple[int, int] | None:
    """Find the start/end byte offsets of the Nth occurrence of a §-marker.

    Section ENDS at the next `### ` or `## ` header (NOT inclusive). Returns
    (start, end) in byte offsets, or None if not found.
    """
    matches = []
    for m in re.finditer(re.escape(marker), text):
        matches.append(m.start())
    if len(matches) < occurrence:
        return None
    start = matches[occurrence - 1]
    after = text[start + len(marker):]
    term = W1B_TERMINATOR_RE.search(after)
    if not term:
        return (start, len(text))
    end = start + len(marker) + term.start()
    return (start, end)


def section_content(text: str, span: tuple[int, int]) -> str:
    return text[span[0]: span[1]]


def is_stub(content: str) -> bool:
    """A 'stub' section is the orchestrator-authored shell template
    (Status: NOT STARTED + 3 pending blocks). Length-based heuristic:
    < 30 substantive lines AND contains 'Status**: NOT STARTED'.
    """
    nstart = content.count("\n")
    has_not_started = "Status**: NOT STARTED" in content
    return nstart < 35 and has_not_started


def clean_wp(text: str) -> tuple[str, dict]:
    report = {"moved": [], "deleted": [], "preserved": [], "errors": []}
    out = text

    # Process W1b-1 and W1b-5 (these have substantive content post-W13 to MOVE)
    for n in (1, 5):
        marker = f"### §W1b-{n}. "
        first = find_section(out, marker, 1)
        second = find_section(out, marker, 2)
        if first is None or second is None:
            report["errors"].append(f"W1b-{n}: missing first or second occurrence")
            continue
        first_content = section_content(out, first)
        second_content = section_content(out, second)
        # If first is stub-or-pointer and second is substantive, MOVE second → first.
        first_is_stub = is_stub(first_content) or "**Status**: COMPLETE — see canonical" in first_content
        second_is_substantive = not is_stub(second_content)
        if first_is_stub and second_is_substantive:
            # 1) Replace first (orchestrator-correct location) with second.
            new_text = out[:first[0]] + second_content + out[first[1]:]
            # 2) Delete second occurrence (now shifted by len_diff).
            len_diff = len(second_content) - len(first_content)
            second_new_start = second[0] + len_diff
            second_new_end = second[1] + len_diff
            new_text = new_text[:second_new_start] + new_text[second_new_end:]
            out = new_text
            report["moved"].append(f"W1b-{n}: post-W13→shell ({len(second_content)} bytes)")
        elif (not first_is_stub) and is_stub(second_content):
            # First is substantive, second is stub → just delete second.
            out = out[:second[0]] + out[second[1]:]
            report["deleted"].append(f"W1b-{n}: stub-only second occurrence ({len(second_content)} bytes)")
        else:
            report["errors"].append(
                f"W1b-{n}: ambiguous — first_stub={first_is_stub}, second_substantive={second_is_substantive}"
            )

    # Process W1b-2, W1b-3, W1b-4, W1b-6 (delete stub-only second occurrences)
    for n in (2, 3, 4, 6):
        marker = f"### §W1b-{n}. "
        first = find_section(out, marker, 1)
        second = find_section(out, marker, 2)
        if second is None:
            report["preserved"].append(f"W1b-{n}: no duplicate")
            continue
        if first is None:
            report["errors"].append(f"W1b-{n}: second exists but no first")
            continue
        first_content = section_content(out, first)
        second_content = section_content(out, second)
        if is_stub(first_content) and is_stub(second_content):
            # Both stubs — gate is still pending. Delete the post-W13
            # duplicate; preserve the orchestrator-correct shell at the
            # W1b block location for the agent to write into when it
            # eventually completes.
            out = out[:second[0]] + out[second[1]:]
            report["deleted"].append(
                f"W1b-{n}: post-W13 stub deleted (gate still pending; "
                f"shell at W1b block preserved; {len(second_content)} bytes)"
            )
            continue
        if is_stub(second_content):
            out = out[:second[0]] + out[second[1]:]
            report["deleted"].append(f"W1b-{n}: stub-only second occurrence ({len(second_content)} bytes)")
        elif is_stub(first_content):
            # Substantive at second, stub at first — MOVE second → first.
            new_text = out[:first[0]] + second_content + out[first[1]:]
            len_diff = len(second_content) - len(first_content)
            second_new_start = second[0] + len_diff
            second_new_end = second[1] + len_diff
            new_text = new_text[:second_new_start] + new_text[second_new_end:]
            out = new_text
            report["moved"].append(f"W1b-{n}: post-W13→shell ({len(second_content)} bytes)")
        else:
            report["errors"].append(
                f"W1b-{n}: BOTH occurrences substantive — manual review needed"
            )

    return out, report


def main() -> int:
    if not WP_PATH.exists():
        print(f"ERROR: {WP_PATH} not found", file=sys.stderr)
        return 1

    text = WP_PATH.read_text(encoding="utf-8")
    cleaned, report = clean_wp(text)

    print("=== W1b WP Dedupe Cleanup Report ===")
    for cat in ("moved", "deleted", "preserved", "errors"):
        print(f"  {cat.upper()}:")
        for entry in report[cat]:
            print(f"    {entry}")
    print()
    print(f"Original size: {len(text):,} bytes")
    print(f"Cleaned size:  {len(cleaned):,} bytes")
    print(f"Delta:         {len(text) - len(cleaned):,} bytes removed/moved")
    print()

    if report["errors"]:
        print("ERRORS PRESENT — refusing to write. Investigate manually.")
        return 2

    if DRY_RUN:
        print("DRY RUN — no file written.")
        return 0

    # Atomic write via temp + rename, with backup.
    shutil.copyfile(WP_PATH, BACKUP_PATH)
    print(f"Backup written: {BACKUP_PATH}")
    tmp = WP_PATH.with_suffix(".md.tmp")
    tmp.write_text(cleaned, encoding="utf-8")
    tmp.replace(WP_PATH)
    print(f"WP rewritten: {WP_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
