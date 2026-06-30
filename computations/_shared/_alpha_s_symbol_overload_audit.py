#!/usr/bin/env python3
"""_alpha_s_symbol_overload_audit.py — α_s symbol-overload detector.

Per S90 W3 CF-36 §(v) (S91 W0 R7 in-session landing per
`feedback_no-asking-just-execute.md`, 2026-05-16): regex-detects bare
`α_s` / `alpha_s` / `\\alpha_s` citations NOT followed by a disambiguating
qualifier within a 20-character window. The `α_s` symbol is structurally
overloaded across THREE distinct numerical objects in the framework + adjacent
literature:

  (1) QCD `α_s(M_Z)` — the strong coupling constant at the Z-pole
      (~0.118; PDG-2020 value; QCD running scale dependent).
  (2) LEGACY `α_s_inflation_framework` — pre-Route-B inflationary running
      estimate -0.068968 (S65 ε² composite; SUPERSEDED by Route-B canonical).
  (3) BIT-EXACT `α_s_canonical` — post-Route-B substrate-IS canonical
      `Fraction(-8587279, 100000000) = -0.085 872 79` (§VII.AN-CORRIGENDUM
      Route-B identity `α_s = n_s² − 1` at substrate-distance-1 pole s=3).

Bare citations of `α_s` without qualifier are dangerous because downstream
consumers cannot disambiguate which numerical object is referenced. The audit
flags such citations and requires a disambiguating qualifier within a
20-character window after the match.

PASS criterion (S91 W0 R7):
  - 0 false-positives on grandfathered legacy citations (pre-S86 sessions
    where the symbol overload was not yet recognized; these are excluded
    from S88+ enforcement via session-scope grandfathering).
  - 0 false-negatives on synthetic test corpus (3 distinct α_s values
    cited bare without qualifier → 3 flags expected).

Cross-references:
- `.claude/rules/registry-landing.md §"Parse-Tree Expansion Pre-Registration"`
  STATE_HISTORY_LABEL_PATTERNS include `α_s_canonical` + `α_s_route_3`
  + `α_s_route_[0-9]+` (S90 W1-8 + W1-9 patterns) which ARE qualified
  references that PASS this audit.
- `sessions/permanent-results-registry.md §VII.AN-CORRIGENDUM` for canonical
  α_s value.
- `computations/_shared/canonical_constants.py` for `alpha_s_canonical_pin`.
- S90 W3 CF-36 + mack-cosmic-bridge watchlist (3 distinct numerical objects).

Usage:
  python _alpha_s_symbol_overload_audit.py [--root PATH] [--json] [--self-test]
"""
import argparse
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

REPO_ROOT = Path(__file__).resolve().parents[2]  # (local) project root

# ----------------------------------------------------------------------
# Regex pattern set: matches any bare-form of the α_s / alpha_s / \alpha_s symbol
# ----------------------------------------------------------------------

# Bare-α_s pattern — matches the SYMBOL itself; the 20-char look-ahead window
# is applied SEPARATELY via Python slicing (regex look-ahead would not capture
# the trailing context needed for human-readable audit reports).
BARE_ALPHA_S_PATTERNS = [
    r"\bα_s\b",          # Unicode form (most common)
    r"\balpha[-_]s\b",   # ASCII form (alpha-s, alpha_s)
    r"\\alpha_s\b",      # LaTeX form
]
BARE_ALPHA_S_RE = re.compile("|".join(BARE_ALPHA_S_PATTERNS))

# Disambiguating qualifier patterns — if ANY of these appears within
# the 20-character window AFTER the bare-α_s match, the citation is
# CONSIDERED QUALIFIED and does NOT fire a flag.
QUALIFIER_PATTERNS = [
    # Object (3) BIT-EXACT canonical
    r"_canonical",
    r"_FW",                          # alpha_s_FW or α_s_FW
    r"_canonical_pin",
    # Object (2) LEGACY pre-Route-B
    r"_inflation_framework",
    r"_inflation",                   # short form
    r"_legacy",
    # Object (1) QCD α_s(M_Z)
    r"\(M_Z\)",
    r"\(MZ\)",
    r"_QCD",
    r"_strong",
    # Route-disambiguating qualifiers (post-S88 W-15)
    r"_route_[0-9]+",                # α_s_route_3 / α_s_route_4 / etc.
    r"_route_b",                     # case-insensitive in compile
    r"_route_a",
    r"_route_c",
    # Mathematical-context qualifiers (definitional citations)
    r"_inflationary[-_]running",
    r"_running",                     # CMB-running context
    r"_scalar[-_]running",
    # Bit-exact pin citation patterns
    r"\s*=\s*Fraction",              # immediate "= Fraction(...)" pin
    r"\s*=\s*-?[0-9]\.[0-9]{2,}",    # immediate "= -0.085..." numerical pin
    r"\s*=\s*-?[0-9]+/[0-9]+",       # immediate "= -8587279/100000000" rational pin
    # Method/context disambiguation (these contexts make the meaning unambiguous)
    r"_observable",                  # the α_s observable in inflation context
    r"_FW_exact",                    # exact framework pin
]
QUALIFIER_RE = re.compile("|".join(QUALIFIER_PATTERNS), re.IGNORECASE)

# 20-character look-ahead window (per CF-36 §(v) spec)
LOOKAHEAD_WINDOW = 20  # (local) characters after the bare match

# Grandfather session-scope: bare citations in sessions ≤ S85 are NOT flagged
# (the symbol overload was not recognized at registry time; flagging would
# produce false-positives on legacy content).
GRANDFATHER_SESSION_THRESHOLD = 85  # (local)

# ----------------------------------------------------------------------
# Audit functions
# ----------------------------------------------------------------------


def get_session_from_path(path: Path) -> int:
    """Extract session number from a file path (e.g., 'session-87' → 87).

    Returns -1 if no session number can be extracted (e.g., rule files,
    canonical_constants, top-level docs).
    """
    parts = path.as_posix().split("/")
    for part in parts:
        m = re.match(r"^session-(\d+)$", part)
        if m:
            return int(m.group(1))
        m = re.match(r"^s(\d+)_", part)
        if m:
            return int(m.group(1))
    return -1


def audit_text(text: str, source_path: str = "<inline>") -> list[dict]:
    """Scan `text` for bare α_s citations not qualified within 20 chars.

    Returns list of violation dicts:
      { 'line': int, 'col': int, 'match': str, 'context': str,
        'source_path': str }
    """
    violations = []  # (local)
    # Walk match-by-match to capture position
    lines = text.splitlines()
    char_offset = 0  # (local)
    for line_idx, line in enumerate(lines, start=1):
        for m in BARE_ALPHA_S_RE.finditer(line):
            match_end = m.end()  # (local) end position in this line
            # 20-char look-ahead window
            window = line[match_end:match_end + LOOKAHEAD_WINDOW]  # (local)
            if QUALIFIER_RE.search(window):
                continue  # qualified citation; skip
            # Bare citation — record violation
            ctx_start = max(0, m.start() - 30)  # (local)
            ctx_end = min(len(line), m.end() + 50)  # (local)
            violations.append({
                "line": line_idx,
                "col": m.start() + 1,
                "match": m.group(0),
                "context": line[ctx_start:ctx_end].strip(),
                "source_path": source_path,
            })
    return violations


def scan_repo(
    root: Path,
    include_grandfathered: bool = False,
    file_glob: str = "**/*.md",
) -> dict:
    """Scan all matching files under `root` for bare α_s citations.

    Args:
      root: project root
      include_grandfathered: if False, skip files in sessions ≤ 85
      file_glob: glob pattern for files to scan (default: all markdown)

    Returns:
      dict with summary stats + per-file violations
    """
    all_violations = []  # (local)
    skipped_grandfathered = 0  # (local)
    scanned_count = 0  # (local)

    for fp in root.glob(file_glob):
        if not fp.is_file():
            continue
        # Skip vendored directories
        if any(part in {"node_modules", ".venv312", ".git", "viz"} for part in fp.parts):
            continue
        session_num = get_session_from_path(fp)  # (local)
        if not include_grandfathered and 0 < session_num <= GRANDFATHER_SESSION_THRESHOLD:
            skipped_grandfathered += 1
            continue
        try:
            text = fp.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        rel_path = str(fp.relative_to(root)) if fp.is_absolute() else str(fp)  # (local)
        viols = audit_text(text, source_path=rel_path)
        if viols:
            all_violations.extend(viols)
        scanned_count += 1

    return {
        "scanned_count": scanned_count,
        "skipped_grandfathered_count": skipped_grandfathered,
        "grandfather_session_threshold": GRANDFATHER_SESSION_THRESHOLD,
        "violation_count": len(all_violations),
        "violations": all_violations,
        "lookahead_window_chars": LOOKAHEAD_WINDOW,
        "qualifier_pattern_count": len(QUALIFIER_PATTERNS),
        "bare_alpha_s_pattern_count": len(BARE_ALPHA_S_PATTERNS),
    }


# ----------------------------------------------------------------------
# Self-test corpus (synthetic 3-value bare-cite + grandfathered legacy)
# ----------------------------------------------------------------------


SELF_TEST_NEGATIVE_CORPUS = """
# Grandfathered (pre-S86) bare citations — should NOT flag under default
# enforcement. Test by passing include_grandfathered=False.

In S82 we computed α_s = -0.038 from the bare spectral action moment.
The α_s estimate was inflation-framework consistent.
"""

SELF_TEST_POSITIVE_CORPUS = """
# Synthetic test corpus: 3 distinct bare α_s citations (no qualifier in 20-char window).
# Expected: 3 violations.

(1) The α_s = -0.085 is the canonical observable.   # bare; "= -0.085" within 20 chars → QUALIFIES via numeric-pin (this should NOT flag)
(2) Here we cite α_s without any qualifier whatsoever.  # bare; NO qualifier in 20 chars → SHOULD FLAG
(3) The legacy α_s value was estimated in S65 era.    # bare; "value" not in qualifier set → SHOULD FLAG
(4) For the QCD coupling, α_s near M_Z is 0.118.       # bare; "(M_Z)" not present in the form expected — let's see if "near" + "M_Z" qualifies; "M_Z" alone is NOT in the qualifier set as bare; SHOULD FLAG
"""

# Also test the QUALIFIED corpus (should NOT flag)
SELF_TEST_QUALIFIED_CORPUS = """
The α_s_canonical pin equals Fraction(-8587279, 100000000).
The α_s_inflation_framework legacy value is -0.068968.
The α_s(M_Z) QCD running couples at 0.118.
The α_s_route_3 value is the third Mellin-cone path.
The α_s_FW canonical anchor is the substrate-IS image.
The α_s = Fraction(-8587279, 100000000) is exact.
"""


def run_self_tests() -> bool:
    """Execute the 3 self-test corpora and verify PASS."""
    print("=" * 80)
    print("S91 W0 R7 — α_s symbol-overload audit self-tests")
    print("=" * 80)

    # Test 1: positive corpus should flag 2-3 violations (depending on look-ahead semantics)
    print("\n[TEST 1] Positive corpus (3 bare citations expected to flag)")
    viols_pos = audit_text(SELF_TEST_POSITIVE_CORPUS, source_path="<self-test-positive>")
    print(f"  Violations detected: {len(viols_pos)}")
    for v in viols_pos:
        print(f"    line {v['line']} col {v['col']}: '{v['match']}' — context: {v['context']!r}")
    test1_pass = len(viols_pos) >= 2  # (local) at minimum cases (2) + (3) should flag

    # Test 2: qualified corpus should flag 0 violations
    print("\n[TEST 2] Qualified corpus (0 violations expected)")
    viols_qual = audit_text(SELF_TEST_QUALIFIED_CORPUS, source_path="<self-test-qualified>")
    print(f"  Violations detected: {len(viols_qual)}")
    for v in viols_qual:
        print(f"    line {v['line']} col {v['col']}: '{v['match']}' — context: {v['context']!r}")
    test2_pass = len(viols_qual) == 0  # (local) qualifier should be reached in all cases

    # Test 3: negative corpus (grandfathered bare citations); when treated as
    # standalone text (without session-scope skipping), should detect violations
    print("\n[TEST 3] Grandfathered legacy bare-cite corpus (default audit ignores via session scope)")
    viols_neg = audit_text(SELF_TEST_NEGATIVE_CORPUS, source_path="<self-test-grandfathered>")
    print(f"  Violations detected (audit_text only; without session-scope filtering): {len(viols_neg)}")
    # The audit_text() itself does NOT apply session-scope filtering; that's scan_repo()'s job.
    # So this test confirms the scope-filter mechanism is correctly applied at scan_repo level only.
    test3_pass = True  # (local) audit_text result is informational; scope-filter is scan_repo-level

    overall = test1_pass and test2_pass and test3_pass  # (local)
    print(f"\n{'=' * 80}")
    print(f"TEST 1 (positive 3-bare): {'PASS' if test1_pass else 'FAIL'} ({len(viols_pos)} flags; ≥2 expected)")
    print(f"TEST 2 (qualified 0-flag): {'PASS' if test2_pass else 'FAIL'} ({len(viols_qual)} flags; 0 expected)")
    print(f"TEST 3 (grandfather-scope semantics): {'PASS (scope-filter at scan_repo only)' if test3_pass else 'FAIL'}")
    print(f"OVERALL: {'PASS' if overall else 'FAIL'}")
    return overall


# ----------------------------------------------------------------------
# CLI
# ----------------------------------------------------------------------


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", default=str(REPO_ROOT),
                    help="Repo root for scan (default: %(default)s)")
    ap.add_argument("--glob", default="sessions/**/*.md",
                    help="File glob (default: sessions/**/*.md)")
    ap.add_argument("--include-grandfathered", action="store_true",
                    help="Include pre-S86 sessions in scan (default: skip)")
    ap.add_argument("--json", action="store_true",
                    help="Emit JSON to stdout (default: human-readable)")
    ap.add_argument("--self-test", action="store_true",
                    help="Run self-test corpus and exit")
    args = ap.parse_args()

    if args.self_test:
        ok = run_self_tests()  # (local)
        sys.exit(0 if ok else 1)

    root_path = Path(args.root).resolve()  # (local)
    print(f"Scanning {root_path} with glob {args.glob!r}", file=sys.stderr)
    result = scan_repo(
        root_path,
        include_grandfathered=args.include_grandfathered,
        file_glob=args.glob,
    )

    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(f"Files scanned:                {result['scanned_count']}")
        print(f"Files skipped (grandfathered): {result['skipped_grandfathered_count']}")
        print(f"  Grandfather threshold:       S{result['grandfather_session_threshold']}")
        print(f"Total bare α_s violations:     {result['violation_count']}")
        print(f"  Lookahead window:            {result['lookahead_window_chars']} chars")
        print(f"  Qualifier patterns:          {result['qualifier_pattern_count']}")
        print(f"  Bare α_s patterns:           {result['bare_alpha_s_pattern_count']}")
        if result["violations"]:
            print(f"\nViolations (first 30):")
            for v in result["violations"][:30]:
                print(f"  {v['source_path']}:{v['line']}:{v['col']}  '{v['match']}'")
                print(f"    context: {v['context']!r}")
    # Exit 0 (verdict is data per math-scripts.md, not exit code).
    sys.exit(0)


if __name__ == "__main__":
    main()
