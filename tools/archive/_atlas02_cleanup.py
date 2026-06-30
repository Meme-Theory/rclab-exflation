"""One-shot cleanup: remove atlas-02 special-case extraction from extract_entities.py.

Per user direction 2026-05-19: closures live in per-session WPs / synthesis docs
(S91 cmap retrofit completed), so atlas-02-mechanism-lifecycle.md is no longer
a canonical-inventory source. Adds it to the Atlas blacklist and removes the
dedicated parser code (`_parse_atlas_02_table`, `_extract_closed_from_atlas_02`,
the era-header and session-gate regexes). Keeps `_ATLAS02_NUMBER_RE` because the
permanent-results-registry §V parser reuses it (legacy variable name).
"""
import ast
import pathlib
import re
import sys


def main():
    p = pathlib.Path("tools/extract_entities.py")
    orig = p.read_text(encoding="utf-8")
    text = orig

    # ----- (1) Blacklist: add atlas-02 entry, update comment, sort numerically
    old1 = (
        "    # Atlas docs that aren't atlas-02 (the canonical closure inventory)\n"
        '    "atlas/atlas-04-assumptions",\n'
        '    "atlas/atlas-05-walls-doors-windows",\n'
        '    "atlas/atlas-06-probability-trajectory",\n'
        '    "atlas/atlas-07-permanent-results",\n'
        '    "atlas/atlas-08-open-questions",\n'
        '    "atlas/atlas-09-retractions",\n'
        '    "atlas/atlas-10-breakthrough-genealogy",\n'
        '    "atlas/atlas-11-cross-pillar-bridge-corpus",\n'
        '    "atlas/atlas-12-methodology-floor",\n'
        '    "atlas/atlas-00-index",\n'
        '    "atlas/atlas-01-session-timeline",\n'
        '    "atlas/atlas-03-equation-flow",'
    )
    new1 = (
        "    # Atlas docs are closure SUMMARIES, not closure sources.\n"
        "    # Closures live in per-session WPs / synthesis docs\n"
        "    # (S91 cmap retrofit). atlas-02 was previously special-cased\n"
        "    # as the 'canonical closure inventory'; that mapping was reverted\n"
        "    # 2026-05-19 because Atlas docs are downstream summaries.\n"
        '    "atlas/atlas-00-index",\n'
        '    "atlas/atlas-01-session-timeline",\n'
        '    "atlas/atlas-02-mechanism-lifecycle",\n'
        '    "atlas/atlas-03-equation-flow",\n'
        '    "atlas/atlas-04-assumptions",\n'
        '    "atlas/atlas-05-walls-doors-windows",\n'
        '    "atlas/atlas-06-probability-trajectory",\n'
        '    "atlas/atlas-07-permanent-results",\n'
        '    "atlas/atlas-08-open-questions",\n'
        '    "atlas/atlas-09-retractions",\n'
        '    "atlas/atlas-10-breakthrough-genealogy",\n'
        '    "atlas/atlas-11-cross-pillar-bridge-corpus",\n'
        '    "atlas/atlas-12-methodology-floor",'
    )

    # ----- (2) Routing: remove atlas-02 special case
    old2 = (
        '    # Canonical-source routing\n'
        '    if "atlas/atlas-02-mechanism-lifecycle" in path_str:\n'
        '        return _extract_closed_from_atlas_02(filepath, text)\n'
        '    if path_str.endswith("/permanent-results-registry.md"):'
    )
    new2 = (
        '    # Canonical-source routing\n'
        '    if path_str.endswith("/permanent-results-registry.md"):'
    )

    # ----- (3) Docstring update — drop "currently atlas-02" mention
    old3 = (
        "    S89 cleanup: canonical-inventory sources route to dedicated parsers\n"
        "    (currently atlas-02; pending §V and closed-gw-channels). Other"
    )
    new3 = (
        "    S89 cleanup: canonical-inventory sources route to dedicated parsers\n"
        "    (permanent-results-registry §V; closed-gw-channels). Other"
    )

    # ----- (7) _CANONICAL_CLOSED_PREFIXES update
    old7 = '_CANONICAL_CLOSED_PREFIXES = ("closed_atlas02_", "closed_regv_", "closed_gwch_")'
    new7 = '_CANONICAL_CLOSED_PREFIXES = ("closed_regv_", "closed_gwch_")'

    replacements = [
        ("(1) blacklist+comment", old1, new1),
        ("(2) routing-remove", old2, new2),
        ("(3) docstring-update", old3, new3),
        ("(7) canonical-prefixes", old7, new7),
    ]
    for desc, old, new in replacements:
        n = text.count(old)
        if n != 1:
            print(f"FAIL: {desc} anchor count = {n} (expected 1)")
            sys.exit(1)
        text = text.replace(old, new, 1)
        print(f"OK: {desc}")

    # ----- (4) Remove _ATLAS02_ERA_HEADER_RE block (keep _ATLAS02_NUMBER_RE)
    pat4 = re.compile(
        r"# `## Era I:`, `## Era II:`, \.\.\. in atlas-02\n"
        r"_ATLAS02_ERA_HEADER_RE = re\.compile\(\n"
        r".*?\n\)\n\n",
        re.DOTALL,
    )
    n4 = len(pat4.findall(text))
    if n4 != 1:
        print(f"FAIL: (4) era-header regex match count = {n4} (expected 1)")
        sys.exit(1)
    text = pat4.sub("", text, count=1)
    print("OK: (4) era-header-regex-remove")

    # ----- (5) Remove _ATLAS02_SESSION_GATE_RE + _parse_atlas_02_table function
    pat5 = re.compile(
        r"# `S17a SP-4` / `S38 CC-INST-38` / `S62 W3-05` style cells in the Closed column\n"
        r"_ATLAS02_SESSION_GATE_RE = re\.compile\(\n"
        r".*?\n\)\n+"
        r"def _parse_atlas_02_table\(.*?\n    return out\n+",
        re.DOTALL,
    )
    n5 = len(pat5.findall(text))
    if n5 != 1:
        print(f"FAIL: (5) session-gate+parser regex match count = {n5} (expected 1)")
        sys.exit(1)
    text = pat5.sub("", text, count=1)
    print("OK: (5) session-gate+parser-remove")

    # ----- (6) Remove _extract_closed_from_atlas_02 function
    pat6 = re.compile(
        r"def _extract_closed_from_atlas_02\(filepath: Path, text: str\) -> list\[dict\]:"
        r".*?\n    return results\n\n+",
        re.DOTALL,
    )
    n6 = len(pat6.findall(text))
    if n6 != 1:
        print(f"FAIL: (6) extract_closed_from_atlas_02 regex match count = {n6} (expected 1)")
        sys.exit(1)
    text = pat6.sub("", text, count=1)
    print("OK: (6) extract_closed_from_atlas_02-remove")

    # ----- Validate syntax
    try:
        ast.parse(text)
    except SyntaxError as e:
        print(f"FAIL: syntax error after edits: {e}")
        sys.exit(1)
    print("OK: ast.parse passed")

    # ----- Audit: any atlas-02 references that survive (should only be
    # _ATLAS02_NUMBER_RE definition + its usage in the regv §V parser).
    remaining = []
    for i, line in enumerate(text.split("\n"), 1):
        low = line.lower()
        if "atlas-02" in low or "atlas02" in low:
            remaining.append((i, line))
    print(f"remaining atlas-02 / atlas02 mentions: {len(remaining)}")
    for i, line in remaining:
        print(f"  L{i}: {line}")

    # ----- Size report
    print(f"size:  {len(orig):>8d} -> {len(text):>8d} bytes (delta {len(text)-len(orig):+d})")
    print(f"lines: {orig.count(chr(10)):>8d} -> {text.count(chr(10)):>8d} (delta {text.count(chr(10))-orig.count(chr(10)):+d})")

    # ----- Write
    p.write_text(text, encoding="utf-8")
    print("WROTE tools/extract_entities.py")


if __name__ == "__main__":
    main()
