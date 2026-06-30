#!/usr/bin/env python3
"""
S93 W9-2 — S93-W9-2-PLAN-CORPUS-SECTION-NUMBER-DRIFT-DETECTOR (driver)
=====================================================================

Gate: S93-W9-2-PLAN-CORPUS-SECTION-NUMBER-DRIFT-DETECTOR ([AUDIT])

Pre-registered threshold (plan §W9-2 strict_PASS_boundary):
  PASS iff 2-of-2 calibration tests pass:
    (a) the S92 W6-2 instance fires PLAN-CORPUS-SECTION-NUMBER-DRIFT with
        cited=§15, correct=§17 (plan phrase "Within-cell discriminator axes"
        matches corpus §17 title, NOT the cited §15 title); AND
    (b) a correctly-cited reference (§10 "Element 3 fiducial-anchor binding")
        returns NO-DRIFT (no false-positive).
  FAIL otherwise.

This driver is METHODOLOGY-class. The PRODUCING SCRIPT (the detector subroutine
`detect_plan_corpus_section_number_drift` + its self-test
`selftest_plan_corpus_section_number_drift`) lives in the EXTENDED audit module
`computations/_shared/_source_reconciliation_audit.py`. This driver imports that
module, runs the 2 calibration tests against the LIVE corpus TOC, writes the
JSON sidecar, computes the S84+ dual-SHA, and appends the verdict line.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/_shared/_source_reconciliation_audit.py  (the producing script extended)
  - sessions/framework/registry/cross-pillar-bridge-corpus.md  (TOC authority §1-§24)
  - sessions/archive/session-92/session-92-w6-workingpaper.md  (calibration source CF-S93-W6-7)
  - canonical_constants.py  (feeds audit_sha256 only)
  - this driver's bytes  (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<2-of-2 pass bool>, scheme=PLAN-CORPUS-SECTION-NUMBER-DRIFT-TOC-PHRASE-MATCH,
   convention=plan-section-ref-phrase-vs-corpus-TOC-title-S2-advisory-on-mismatch, L_max=N/A)

Classification: NON-PHONONIC (methodology / audit-floor tooling). Per
epistemic-discipline.md §"Layer-Decomposition", a plan-block's corpus-section
citation is a methodology-floor pointer; this detector is the audit-floor
enforcement that the pointer's NUMBER stays coherent with the corpus's actual
TOC structure. It is the SECTION-number sibling of W9-1's LINE-anchor validator.

DEVIATION NOTE (substrate-first-canonical-sourcing.md §(ii.B)):
  the plan §W9-2 input_files block pins canonical_constants.py + the audit
  script + the corpus with `<computed-at-runtime>` placeholders (runtime SHA
  capture, NOT a literal pin). This driver captures the runtime SHAs into the
  pin map; there is no literal-vs-runtime drift (the plan pinned runtime
  capture by design). This is the §(ii.B) benign runtime-SHA-capture pattern,
  NOT a Class-(c) PIN-DRIFT defect.

DISCIPLINE:
  - `from canonical_constants import *`
  - every intermediate tagged `# (local)`
  - CPU-only (string/grep work, no linear algebra) — OMP capped in the imported
    audit module BEFORE numpy import
  - audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
  - atomic single-`open("a")` verdict append (NO read-modify-write / truncate)
  - [AUDIT] trigger ⇒ NO 3-tuple companion row (plan: schema_v2_3tuple_required=false)
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

# This driver lives at computations/session-93/. The audit module + canonical
# constants live at computations/_shared/. Add _shared to sys.path so both the
# canonical_constants import and the audit-module import resolve.
SESSION_DIR = Path(__file__).resolve().parent                  # (local)
COMPUTATIONS_DIR = SESSION_DIR.parent                          # (local)
SHARED_DIR = COMPUTATIONS_DIR / "_shared"                      # (local)
PROJECT_ROOT = COMPUTATIONS_DIR.parent                         # (local)
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403,E402

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib   # noqa: E402
import json      # noqa: E402
import time      # noqa: E402

# The producing-script detector + self-test (the W9-2 deliverable).
from _source_reconciliation_audit import (  # noqa: E402
    detect_plan_corpus_section_number_drift,
    selftest_plan_corpus_section_number_drift,
    parse_corpus_toc,
    DRIFT_FLAG,
)

# ---------------------------------------------------------------------------
# Section 3 — Identity + pre-registration pins (plan §W9-2)
# ---------------------------------------------------------------------------
SESSION = "S93"                                                              # (local)
GATE_ID = "S93-W9-2-PLAN-CORPUS-SECTION-NUMBER-DRIFT-DETECTOR"               # (local)
SCHEME = "PLAN-CORPUS-SECTION-NUMBER-DRIFT-TOC-PHRASE-MATCH"                 # (local)
CONVENTION = "plan-section-ref-phrase-vs-corpus-TOC-title-S2-advisory-on-mismatch"  # (local)
L_MAX = "N/A"                                                                # (local) audit-script
N_EVAL = 2                                                                   # (local) 1 TP + 1 TN

# Calibration instance (plan §W9-2 machinery_pin_map.calibration_instance)
CITED_SECTION_EXPECTED = 15   # (local) the WRONG number the plan cited
CORRECT_SECTION_EXPECTED = 17  # (local) the authority §M the phrase actually names

# Output destinations (per-session)
OUT_JSON = SESSION_DIR / "s93_w9_2_plan_corpus_section_number_drift_selftest.json"  # (local)
VERDICT_TXT = SESSION_DIR / "s93_gate_verdicts.txt"                                  # (local)

# Producing script + TOC authority + calibration source (plan §W9-2 input_files)
AUDIT_SCRIPT = SHARED_DIR / "_source_reconciliation_audit.py"                        # (local)
CORPUS_PATH = PROJECT_ROOT / "sessions/framework/registry/cross-pillar-bridge-corpus.md"  # (local)
S92_W6_WP = PROJECT_ROOT / "sessions/archive/session-92/session-92-w6-workingpaper.md"      # (local)
CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"                              # (local)

INPUT_FILES = [
    AUDIT_SCRIPT,
    CORPUS_PATH,
    S92_W6_WP,
    CANONICAL_PATH,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA schema, W9a-99)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; 'MISSING' on missing/unreadable."""
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return "MISSING"
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    """Print SHA-256 of each input; return {relpath: sha} for closure hash."""
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = str(p)  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(
    script_path: Path,
    canonical_path: Path,
    pins: dict[str, str],
) -> tuple[str, str]:
    """(audit_sha256, content_sha256) per the S84+ dual-SHA schema.

    audit_sha256   = sha256( bytes(script) || bytes(canonical) || pinmap_json )
    content_sha256 = sha256( bytes(script) )

    Matches .claude/templates/script-template.py compute_dual_sha (lines 148-191).
    """
    try:
        script_bytes = script_path.read_bytes()  # (local)
    except OSError:
        script_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""  # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")  # (local)

    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)

    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Verdict emission (atomic single-open append; S84+ dual-SHA)
# ---------------------------------------------------------------------------

def append_verdict(verdict: str, value: str, audit_sha: str, content_sha: str) -> None:
    """Append the canonical verdict line + dual-SHA companion row.

    Atomic append: ONE `open("a")` write per call (canonical line written in a
    single call; companion row in a second single call). No read-modify-write,
    no truncate-and-rewrite (the S84 W1 race pattern). [AUDIT] trigger ⇒ NO
    3-tuple companion row (plan §W9-2 schema_v2_3tuple_required=false).
    """
    canonical_line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )  # (local)
    companion_row = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical_line)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(companion_row)


# ---------------------------------------------------------------------------
# Section 6 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    # 1. Log input pins (S84+ dual-SHA schema; runtime SHA capture per §(ii.B))
    pins = log_input_pins(INPUT_FILES)  # (local)
    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_PATH, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (driver script only)")
    print()

    # 2. Parse corpus TOC + run the 2 calibration tests against the LIVE corpus.
    toc = parse_corpus_toc(CORPUS_PATH)  # (local)
    print(f"corpus TOC parsed: {len(toc)} top-level §N sections "
          f"(range §{min(toc) if toc else '?'}-§{max(toc) if toc else '?'})")
    print(f"  §{CITED_SECTION_EXPECTED} = {toc.get(CITED_SECTION_EXPECTED)}")
    print(f"  §{CORRECT_SECTION_EXPECTED} = {toc.get(CORRECT_SECTION_EXPECTED)}")
    print(f"  §10 = {toc.get(10)}")
    print()

    selftest = selftest_plan_corpus_section_number_drift(CORPUS_PATH)  # (local)
    tp = selftest["test_1_true_positive"]   # (local)
    tn = selftest["test_2_true_negative"]   # (local)

    print("TEST 1 (true-positive — S92 W6-2 §15-vs-§17 drift):")
    print(f"  plan fragment: {tp['plan_fragment']}")
    print(f"  expected: cited=§{tp['expected']['cited_section']}, "
          f"correct=§{tp['expected']['correct_section']}, verdict={tp['expected']['verdict']}")
    finding = tp["observed_finding"]  # (local)
    if finding:
        print(f"  observed: cited=§{finding['cited_section']}, "
              f"correct=§{finding['correct_section']}, flag={finding['flag']}")
        print(f"            cited_title='{finding['cited_title']}'")
        print(f"            correct_title='{finding['correct_title']}'")
        print(f"            severity={finding['severity']} (S2 ADVISORY)")
    print(f"  TEST 1 PASS: {tp['pass']}")
    print()
    print("TEST 2 (true-negative — §10 correctly cited):")
    print(f"  plan fragment: {tn['plan_fragment']}")
    print(f"  observed: verdict={tn['observed_verdict']}, n_findings={tn['observed_n_findings']}")
    print(f"  TEST 2 PASS: {tn['pass']}")
    print()

    # 3. Evaluate gate: PASS iff 2-of-2 calibration tests pass.
    #    Strict re-check of the cited/correct pair against the pre-registered
    #    calibration instance (defense against a self-test that PASSes for the
    #    wrong reason).
    tp_pair_ok = bool(
        finding is not None
        and finding["cited_section"] == CITED_SECTION_EXPECTED
        and finding["correct_section"] == CORRECT_SECTION_EXPECTED
        and finding["flag"] == DRIFT_FLAG
    )  # (local)
    two_of_two = bool(tp["pass"] and tn["pass"] and tp_pair_ok)  # (local)
    verdict = "PASS" if two_of_two else "FAIL"  # (local)
    value = (
        f"2-of-2_calibration={selftest['n_pass']}/2"
        f"_TP-cited=§{CITED_SECTION_EXPECTED}-correct=§{CORRECT_SECTION_EXPECTED}"
        f"_TN-NO-DRIFT={tn['observed_verdict']}"
    )  # (local)

    # 4. Write the JSON sidecar (the 2 calibration tests, full record).
    out_payload = {
        "gate_id": GATE_ID,
        "mode": "plan-corpus-section-number-drift-selftest",
        "verdict": verdict,
        "value": value,
        "two_of_two_pass": two_of_two,
        "n_eval": N_EVAL,
        "n_pass": selftest["n_pass"],
        "calibration_instance": {
            "cited_section": CITED_SECTION_EXPECTED,
            "correct_section": CORRECT_SECTION_EXPECTED,
            "drift_flag": DRIFT_FLAG,
            "source": "session-92-w6-workingpaper.md:672-677 (CF-S93-W6-7)",
        },
        "corpus_toc": {str(n): t for n, t in sorted(toc.items())},
        "corpus_toc_count": len(toc),
        "selftest": selftest,
        "input_pin_map": pins,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "fourtuple": {
            "value": value,
            "scheme": SCHEME,
            "convention": CONVENTION,
            "L_max": L_MAX,
        },
        "severity": "S2",
        "audit_method": "S93-W9-2-detect-plan-corpus-section-number-drift",
        "deviation_note": (
            "canonical_constants.py runtime SHA captured into pin map per "
            "substrate-first-canonical-sourcing.md §(ii.B); plan pinned "
            "<computed-at-runtime> by design — no literal-vs-runtime drift."
        ),
    }
    OUT_JSON.write_text(json.dumps(out_payload, indent=2, default=str), encoding="utf-8")
    print(f"JSON sidecar written: {OUT_JSON.relative_to(PROJECT_ROOT)}")

    # 5. Emit 4-tuple + append verdict (dual-SHA, S84+; NO 3-tuple for [AUDIT]).
    print(f"(value={value!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    print(f"content_sha256: {content_sha}")
    print(f"audit_sha256:   {audit_sha}")
    append_verdict(verdict, value, audit_sha, content_sha)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    # Exit 0 regardless of PASS/FAIL — verdict is data, not exit code
    # (math-scripts.md §"Exit Codes and Verdict Semantics"). Nonzero is
    # reserved for script breakage only.
    return 0


if __name__ == "__main__":
    sys.exit(main())
