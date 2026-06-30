"""Test harness for the patched legacy-path closed_mechanisms extractor.

Goal: empirically validate whether the S91 regex fix at
extract_entities.py:1250 (S? prefix added to inner session-finder regex)
unlocks closure extraction from session files using the S{N} convention.

Test files:
  - sessions/session-75/session-75-OOM.md
      Contains a 49-row CLOSED table under `## Summary Table`.
      Pre-fix: 0 rows extracted. Atlas-02 enumerates ~5 of these.
  - sessions/session-76/session-76-results-workingpaper.md
      Contains a closure table under `## Constraint Map Updates`,
      including the JLO route CLOSED row at line 1316.
      Pre-fix: 0 rows extracted.
  - sessions/archive/session-25/session-25-Investigation-Closing.md
      Pre-fix: 6 rows extracted. Regression check — these MUST still
      extract (the fix accepts an OPTIONAL S prefix, so bare-numeric
      sessions like 22b-22c continue to match).

Secondary diagnostic: print which sections in each file are matched by
RE_CLOSED_SECTION. If session-75-OOM has zero matched sections, then the
section-detection regex is the deeper blocker and the inner-regex fix
alone is insufficient.

Throwaway script; safe to delete once the cleanup direction is verified.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from extract_entities import (  # noqa: E402
    extract_closed_mechanisms,
    RE_CLOSED_SECTION,
    PROJECT_ROOT,
)


def banner(s: str) -> None:
    print()
    print("=" * 78)
    print(s)
    print("=" * 78)


def run_one(label: str, rel_path: str, expected_min: int) -> dict:
    """Run extract_closed_mechanisms on one file; report results.

    Returns dict with row count + matched section count + sample names.
    """
    src = PROJECT_ROOT / rel_path
    if not src.exists():
        print(f"NOT FOUND: {src}", file=sys.stderr)
        return {"rows": 0, "sections": 0, "names": [], "missing": True}
    text = src.read_text(encoding="utf-8")
    banner(f"{label}: {rel_path}")
    print(f"  size: {len(text):,} chars")

    # Count sections RE_CLOSED_SECTION matches in this file
    section_matches = list(RE_CLOSED_SECTION.finditer(text))
    print(f"  RE_CLOSED_SECTION matches: {len(section_matches)}")
    for m in section_matches[:5]:
        # Show the header line of each matched section
        start = m.start()
        end = text.find("\n", start)
        header = text[start:end].strip()
        print(f"    header: {header[:90]!r}")
    if len(section_matches) > 5:
        print(f"    ... ({len(section_matches) - 5} more)")

    # Run the legacy extractor
    rows = extract_closed_mechanisms(src, text)
    print(f"  Extracted rows: {len(rows)}  (expected >= {expected_min})")

    # Show sample rows
    if rows:
        print("  Sample (first 8):")
        for r in rows[:8]:
            print(f"    - name={r.get('name','')!r}")
            print(f"      session={r.get('session','')!r}  "
                  f"gate_id={r.get('gate_id','')!r}")
            print(f"      closed_by={(r.get('closed_by','') or '')[:60]!r}")

    return {
        "rows": len(rows),
        "sections": len(section_matches),
        "names": [r.get("name", "") for r in rows],
        "missing": False,
    }


def main() -> int:
    banner("TEST 1 — session-75-OOM.md (under `## Summary Table`)")
    print("Hypothesis: regex fix alone is insufficient because")
    print("`## Summary Table` doesn't trigger RE_CLOSED_SECTION.")
    print("Expected: 0 section matches → 0 rows (section-detection is blocker).")
    r75 = run_one(
        "session-75-OOM",
        "sessions/session-75/session-75-OOM.md",
        expected_min=0,
    )

    banner("TEST 2 — session-76-results-workingpaper.md "
           "(under `## Constraint Map Updates`)")
    print("Same hypothesis: section header is not a closure keyword.")
    r76 = run_one(
        "session-76-results-workingpaper",
        "sessions/session-76/session-76-results-workingpaper.md",
        expected_min=0,
    )

    banner("TEST 3 — session-25-Investigation-Closing.md (regression)")
    print("Hypothesis: pre-fix this file extracted 6 rows. Post-fix it")
    print("MUST still extract them — the S? prefix is OPTIONAL.")
    r25 = run_one(
        "session-25-Investigation-Closing",
        "sessions/archive/session-25/session-25-Investigation-Closing.md",
        expected_min=6,
    )

    banner("TEST 4 — session-25-Investigation-Question-Efforts.md "
           "(regression)")
    print("Pre-fix this file extracted 1 row (closed_10 in dump).")
    r25b = run_one(
        "session-25-Investigation-Question-Efforts",
        "sessions/archive/session-25/session-25-Investigation-Question-Efforts.md",
        expected_min=1,
    )

    banner("SUMMARY + VERDICT")
    print(f"  session-75-OOM:               {r75['rows']:>3} rows  "
          f"({r75['sections']:>2} sections matched)")
    print(f"  session-76-results-WP:        {r76['rows']:>3} rows  "
          f"({r76['sections']:>2} sections matched)")
    print(f"  session-25-Inv-Closing:       {r25['rows']:>3} rows  "
          f"({r25['sections']:>2} sections matched)")
    print(f"  session-25-Inv-Q-Efforts:     {r25b['rows']:>3} rows  "
          f"({r25b['sections']:>2} sections matched)")

    print()
    print("Verdict logic:")
    print(f"  - Regression (S25 files): pre-fix counts were 6 + 1 = 7.")
    print(f"    Post-fix: {r25['rows']} + {r25b['rows']} = "
          f"{r25['rows'] + r25b['rows']}.")
    if r25['rows'] + r25b['rows'] < 7:
        print("    REGRESSION — fix broke pre-S43 extraction. Revert.")
    else:
        print("    OK — pre-S43 extraction preserved.")
    print()
    print(f"  - Unlock (S75/S76 files): pre-fix counts were 0 + 0 = 0.")
    print(f"    Post-fix: {r75['rows']} + {r76['rows']} = "
          f"{r75['rows'] + r76['rows']}.")
    if r75['rows'] + r76['rows'] == 0:
        print("    REGEX FIX ALONE INSUFFICIENT — RE_CLOSED_SECTION needs")
        print("    extension to include the section headers used in")
        print("    post-S43 session files (`## Summary Table`,")
        print("    `## Constraint Map Updates`, etc.).")
    elif r75['rows'] + r76['rows'] < 10:
        print(f"    PARTIAL UNLOCK — {r75['rows'] + r76['rows']} rows but")
        print(f"    far fewer than the 49 + 14 known closures in these")
        print(f"    files. Section-detection may still be missing tables.")
    else:
        print(f"    UNLOCK — {r75['rows'] + r76['rows']} rows extracted.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
