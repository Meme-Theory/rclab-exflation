#!/usr/bin/env python3
"""
_s93_w9_1_wp_patch.py — single-shot WP §W9-1 section patcher (parallel-writer-safe).

The §W9-1 WP section must be filled in `session-93-w9-workingpaper.md`, a file
under concurrent multi-agent write. The Edit tool is mtime-conditional and fails
under concurrent writers (per epistemic-discipline.md §"Registry-Write Hygiene
under Parallel-Writer Race"). This patcher does a tight read-modify-write in ONE
operation, replacing the §W9-1 stub block (from the section header through its
trailing `---`) with the completed section text from _s93_w9_1_wp_section.txt.

Idempotent: if §W9-1 already shows `**Status**: COMPLETED`, the patcher no-ops
(safe to re-run if a write races).

NON-PHONONIC tooling. No framework constants.
"""
from __future__ import annotations

import sys
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent  # (local) computations/session-93
PROJECT_ROOT = SESSION_DIR.parent.parent       # (local)
WP = PROJECT_ROOT / "sessions" / "session-93" / "session-93-w9-workingpaper.md"  # (local)
SECTION_TXT = SESSION_DIR / "_s93_w9_1_wp_section.txt"  # (local)

SECTION_HEADER = "### §W9-1. S93-W9-1-PLAN-LINE-ANCHOR-VALIDATOR (gen-physicist)"  # (local)


def main() -> int:
    text = WP.read_text(encoding="utf-8")  # (local)
    new_body = SECTION_TXT.read_text(encoding="utf-8").rstrip("\n")  # (local)

    h_idx = text.find(SECTION_HEADER)  # (local)
    if h_idx == -1:
        print(f"ERROR: section header not found: {SECTION_HEADER!r}")
        return 2

    # Region to replace: everything AFTER the header line (and its blank line)
    # up to (but not including) the trailing `---` that closes the section.
    after_header = text.index("\n", h_idx) + 1  # (local) end of header line
    # Skip the single blank line after the header.
    body_start = after_header
    while body_start < len(text) and text[body_start] == "\n":
        body_start += 1

    # The section's body ends at the next standalone `---` line.
    sep_idx = text.find("\n---", body_start)  # (local)
    if sep_idx == -1:
        print("ERROR: section-closing '---' not found after §W9-1 header.")
        return 2
    body_end = sep_idx + 1  # (local) keep up to (not incl) the '---' line's start

    current_body = text[body_start:body_end]  # (local)
    if "**Status**: COMPLETED" in current_body and "Verdict**: **PASS**" in current_body:
        print("Already patched (Status COMPLETED + Verdict PASS present); no-op.")
        return 0

    new_text = text[:body_start] + new_body + "\n\n" + text[body_end:]  # (local)
    WP.write_text(new_text, encoding="utf-8")
    print(f"Patched §W9-1 section ({len(new_body)} chars) into {WP.name}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
