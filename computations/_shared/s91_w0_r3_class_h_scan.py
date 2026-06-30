#!/usr/bin/env python3
"""S91 W0 R3 — Class-(h) MISSING-PARSE-TREE-EXPANSION scan.

Per `.claude/rules/registry-landing.md §"Parse-Tree Expansion Pre-Registration
for new §VII entries (S90 W-3 CF-R1-3)"`: NEW §VII entries citing observables
with state-historic names MUST declare the parse-tree expansion alongside the
symbolic form. Pre-S90 entries are GRANDFATHERED with mandatory retrofit at
next-session plan-freeze.

This scan:
  1. Iterates all `## §VII.X` and `### §VII.X.Y` slot headings in
     `sessions/permanent-results-registry.md`
  2. For each slot, extracts the block (heading through next-same-or-shallower
     heading)
  3. Runs `detect_class_h_missing_parse_tree_expansion()` from the audit script
  4. Reports per-slot diagnostic + identifies retrofit candidates

Output: JSON sidecar enumerating slots that need parse-tree expansion retrofit,
plus a human-readable summary.

Cross-link: `.claude/rules/registry-landing.md` §"Parse-Tree Expansion
Pre-Registration for new §VII entries (S90 W-3 CF-R1-3)"`.
"""
import json
import re
import sys
from pathlib import Path

# Canonical-constants import per `computations/_shared/CLAUDE.md` MANDATORY discipline.
_SHARED_DIR = Path(__file__).resolve().parent  # (local)
sys.path.insert(0, str(_SHARED_DIR))
try:
    from canonical_constants import *  # noqa: F401,F403,E402
except Exception as _e:
    print(f"WARNING: canonical_constants.py import failed: {_e}", file=sys.stderr)

# Import the audit detector from sibling module
from _registry_landing_audit import (
    detect_class_h_missing_parse_tree_expansion,
    STATE_HISTORY_LABEL_PATTERNS,
    PARSE_TREE_EXPANSION_RE,
)

REPO_ROOT = Path(__file__).resolve().parents[2]  # (local) project root
REGISTRY_FILE = REPO_ROOT / "sessions" / "permanent-results-registry.md"  # (local)
OUTPUT_JSON = REPO_ROOT / "computations" / "_shared" / "s91_w0_r3_class_h_scan.json"  # (local)

# Match either `## §VII.X[.suffix]` or `### §VII.X[.suffix]` heading
SLOT_HEADING_RE = re.compile(r"^(##|###|####) §VII\.[A-Z]+(?:\.[A-Z0-9-]+)*", re.MULTILINE)  # (local)


def extract_all_slots(registry_text: str) -> list[dict]:
    """Extract every §VII.X[.suffix] block (## OR ###) and return as list.

    Block boundary: heading through next heading at SAME or SHALLOWER level.
    """
    lines = registry_text.splitlines(keepends=True)
    headings = []  # (local) (line_idx, level, slot_label, heading_text)
    for i, line in enumerate(lines):
        m = SLOT_HEADING_RE.match(line)
        if m:
            level = len(m.group(1))  # (local) 2/3/4 for ##/###/####
            slot_label = m.group(0).split(" ", 1)[1].strip()  # (local) "§VII.X..."
            heading_text = line.rstrip("\n")  # (local)
            headings.append((i, level, slot_label, heading_text))

    # Build per-slot block — block extends to next heading at SAME or SHALLOWER level
    slots = []  # (local)
    for j, (start_idx, level, slot_label, heading_text) in enumerate(headings):
        end_idx = len(lines)
        for k in range(j + 1, len(headings)):
            if headings[k][1] <= level:
                end_idx = headings[k][0]
                break
        block_text = "".join(lines[start_idx:end_idx])
        slots.append({
            "slot_label": slot_label,
            "heading_text": heading_text,
            "level": level,
            "line_start": start_idx + 1,
            "line_end_exclusive": end_idx + 1,
            "byte_count": len(block_text.encode("utf-8")),
            "block_text": block_text,
        })
    return slots


def main():
    if not REGISTRY_FILE.exists():
        print(f"ERROR: registry not found at {REGISTRY_FILE}", file=sys.stderr)
        sys.exit(1)

    text = REGISTRY_FILE.read_text(encoding="utf-8")
    slots = extract_all_slots(text)

    print(f"Found {len(slots)} §VII slot blocks in registry")
    print(f"=" * 100)

    # Run Class-(h) detector on each
    results = []  # (local)
    missing_count = 0  # (local)
    state_history_count = 0  # (local)
    pass_count = 0  # (local)
    no_label_count = 0  # (local)

    for slot in slots:
        diag = detect_class_h_missing_parse_tree_expansion(slot["block_text"], slot["slot_label"])
        record = {
            "slot_label": slot["slot_label"],
            "level": slot["level"],
            "line_start": slot["line_start"],
            "byte_count": slot["byte_count"],
            "state_history_label_matches": [m["match_text"] for m in diag["state_history_label_matches"]],
            "parse_tree_expansion_present": diag["parse_tree_expansion_present"],
            "diagnostic": diag["diagnostic"],
            "severity": diag["severity"],
        }
        results.append(record)
        if diag["diagnostic"] == "MISSING-PARSE-TREE-EXPANSION":
            missing_count += 1
        elif diag["diagnostic"] == "PASS":
            pass_count += 1
            state_history_count += 1
        elif diag["diagnostic"] == "no_state_history_label_present":
            no_label_count += 1

    # Summary
    print(f"\nSummary (Class-(h) MISSING-PARSE-TREE-EXPANSION detector):")
    print(f"  Total slots scanned                       : {len(slots)}")
    print(f"  No state-history label present (N/A)      : {no_label_count}")
    print(f"  State-history label + parse-tree (PASS)   : {pass_count}")
    print(f"  State-history label + NO parse-tree (FAIL): {missing_count}")
    print()

    # Detail report — list only the MISSING ones (retrofit candidates)
    print(f"=" * 100)
    print(f"RETROFIT CANDIDATES (state-history label present, parse-tree MISSING):")
    print(f"-" * 100)
    for r in results:
        if r["diagnostic"] == "MISSING-PARSE-TREE-EXPANSION":
            labels = ", ".join(r["state_history_label_matches"][:5])
            print(f"  L{r['level']} {r['slot_label']:<60} line {r['line_start']:<6} labels=[{labels}]")
    print()

    # Also list PASS instances for completeness (these are entries that already pass)
    print(f"-" * 100)
    print(f"ALREADY-PASSING entries (state-history label + parse-tree present):")
    for r in results:
        if r["diagnostic"] == "PASS":
            labels = ", ".join(r["state_history_label_matches"][:3])
            print(f"  L{r['level']} {r['slot_label']:<60} line {r['line_start']:<6} labels=[{labels}]")

    # Emit JSON sidecar
    OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_JSON.write_text(json.dumps(results, indent=2, ensure_ascii=False))
    print(f"\nJSON sidecar: {OUTPUT_JSON}")
    print(f"\nState-history label patterns scanned ({len(STATE_HISTORY_LABEL_PATTERNS)}):")
    for p in STATE_HISTORY_LABEL_PATTERNS:
        print(f"  - {p!r}")


if __name__ == "__main__":
    main()
