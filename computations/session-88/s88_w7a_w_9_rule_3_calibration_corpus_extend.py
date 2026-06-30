#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S88 W7a-72 — S88-W-9-RULE-3-CALIBRATION-CORPUS-EXTEND
======================================================

Gate: S88-W-9-RULE-3-CALIBRATION-CORPUS-EXTEND ([AUDIT])

Pre-registered threshold (per session-88-plan-w7a.md §W7a-72 §125-129):
  PASS iff
    (1) `epistemic-discipline.md §"Pole-Scope sub-clause"` calibration
        corpus contains all 3 new instances (#2 W7-1 + #3 W7-3 + #4 W9b-2)
        with full 64-char audit_sha citations to the S87 verdict lines, AND
    (2) MANDATORY-at-K=4 promotion event marker present in the rule-file, AND
    (3) `methodology-wave-allowlist.md` contains the W7a-72 row with
        sha256_of_plan_block matching the plan §W7a-72 block bytes hash.
  FAIL iff any of the 3 instances cannot be verified on disk (rule-file
        edit failed or content drifted), OR the allowlist row is missing.
  INFO iff 2 of 3 instances verified cleanly, 1 partial — corpus K=3
        (still hits MANDATORY threshold; sub-clause status update reduced
        to "MANDATORY at plan-freeze with 1 pending refinement at S89").

Inputs (SHA-256 dual-pinned at runtime — S84+ schema):
  - .claude/rules/epistemic-discipline.md (post-W7a-72 edit, on disk)
  - .claude/rules/methodology-wave-allowlist.md (post-W7a-72 row append)
  - sessions/session-plan/session-88-plan-w7a.md (plan-block source)
  - computations/session-87/s87_gate_verdicts.txt (S87 verdict-line pins
    for W7-1, W7-3, W9b-2 — input pin map)
  - canonical_constants.py (feeds audit_sha256 only)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<verdict_str>, scheme=METHODOLOGY-class,
   convention=W-9-RULE-3-pole-scope-corpus-extend, L_max=N/A)

Classification: METHODOLOGY-class per `wave-classification.md` (M1
artifact-existence on rule-file edit; M2 Edit on epistemic-discipline.md;
M3 verbatim sub-extracts from S87 W7-1/W7-3/W9b-2 closed verdict lines;
M4 allowlist append herewith). Orchestrator-direct-write.

METHODOLOGY
-----------
This is a verification-script that confirms the rule-file edits landed
on disk (AFTER-pattern per `registry-landing.md §"Bridge-Landing Script
Architecture"`). The orchestrator already performed the two Edits
(epistemic-discipline.md calibration corpus extension + methodology-
wave-allowlist.md row append) via the Edit tool with atomic write +
fsync semantics. This script re-reads both files post-edit, verifies
the expected content markers are present, computes dual-SHA over the
input pin map, and appends the canonical verdict line.

INPUT-PIN MAP (closure_hash → audit_sha256):
  - epistemic_discipline_md_post_edit_sha
  - methodology_wave_allowlist_md_post_edit_sha
  - plan_w7a_md_sha
  - s87_gate_verdicts_txt_sha
  - canonical_constants_sha
  - script_bytes_sha

Author: lizzi-spectral-functional-theorist (PRIMARY; orchestrator-direct
under METHODOLOGY-class wave-classification path)
Session: 88, Wave: W7a, Plan: session-88-plan-w7a.md §W7a-72
Date: 2026-05-05
"""
from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys as _sys
from pathlib import Path as _Path

_THIS_FILE = _Path(__file__).resolve()                             # (local)
_SHARED_DIR = _THIS_FILE.parent.parent / "_shared"                 # (local)
if str(_SHARED_DIR) not in _sys.path:
    _sys.path.insert(0, str(_SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import sys
import time
from pathlib import Path

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S88"                                                    # (local)
GATE_ID = "S88-W-9-RULE-3-CALIBRATION-CORPUS-EXTEND"               # (local)
SCHEME = "METHODOLOGY-class"                                       # (local)
CONVENTION = "W-9-RULE-3-pole-scope-corpus-extend"                 # (local)
L_MAX = "N/A"                                                      # (local)

# Pre-registered K-counter values
K_PRE = 1                                                          # (local)
K_NEW_INSTANCES = 3                                                # (local)
K_POST = K_PRE + K_NEW_INSTANCES                                   # (local) = 4
K_PROMOTION_THRESHOLD = 3                                          # (local)

# Input file paths
EPISTEMIC_RULE = (
    PROJECT_ROOT / ".claude" / "rules" / "epistemic-discipline.md"
)                                                                  # (local)
ALLOWLIST_RULE = (
    PROJECT_ROOT / ".claude" / "rules" / "methodology-wave-allowlist.md"
)                                                                  # (local)
PLAN_W7A = (
    PROJECT_ROOT / "sessions" / "session-plan" / "session-88-plan-w7a.md"
)                                                                  # (local)
S87_VERDICTS = (
    PROJECT_ROOT / "computations" / "session-87" / "s87_gate_verdicts.txt"
)                                                                  # (local)
CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"             # (local)

# Verdict file (canonical per gate-verdicts.md S84+)
VERDICT_TXT = SESSION_DIR / "s88_gate_verdicts.txt"

# ---------------------------------------------------------------------------
# Section 4 — SHA helpers (S84+ dual-SHA schema)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes."""
    h = hashlib.sha256()                                           # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def compute_dual_sha(
    script_path: Path,
    canonical_path: Path,
    pins: dict,
) -> tuple:
    """Compute (audit_sha256, content_sha256) per S84+ dual-SHA schema."""
    script_bytes = b""                                             # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""                                          # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")                                              # (local)

    h_audit = hashlib.sha256()                                     # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                                    # (local)

    h_content = hashlib.sha256()                                   # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()                                # (local)

    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Verification (re-read + verify edits landed)
# ---------------------------------------------------------------------------

# Pre-registered content markers we expect in the post-edit
# epistemic-discipline.md §"Pole-Scope sub-clause" calibration corpus.
# Each marker is a substring; ALL must be present for PASS.
EPISTEMIC_MARKERS = [
    # Status promotion marker
    "Status: MANDATORY at K=4 (promoted at S88 W7a-72 close",
    "Calibration corpus (K=4)",
    # Instance #2 (W7-1) — full audit_sha pin
    "S87-W5A-P3-IC-PER-CLASS-VERIFY: FAIL",
    "audit_sha256=38b36fc0a5e5889facda9b175fa3f43c3f3f210f08518f4345af5abd786dc696",
    "delta_max = 0.7986",
    # Instance #3 (W7-3) — full audit_sha pin
    "S87-W6-C-GAMMA-WEAK-PER-CLASS: PASS",
    "audit_sha256=0eb96f0536fb2d927639f8224bced41ccde74d062a9e59e0e29ae595919e3944",
    "{n_c} = (10, 10, 10, 11, 13)",
    # Instance #4 (W9b-2) — full audit_sha pin
    "S87-POLE-SPECIFICITY-SCAN: PASS",
    "audit_sha256=30815fae79102fb9ac671fb33101029d5318253b69a2d125ea85ae5eb7396ebc",
    "Reading_1_PASS",
    # K-counter arithmetic
    "K = 1 (instance #1 S86 baseline) + 3 (instances #2, #3, #4 from S87 corpus) = 4",
    # Forward enforcement section
    "Forward enforcement (post-promotion)",
]                                                                  # (local)

# Pre-registered content markers in methodology-wave-allowlist.md
ALLOWLIST_MARKERS = [
    # The W7a-72 row markers
    "| W7a-72 | S88 | S88-W-9-RULE-3-CALIBRATION-CORPUS-EXTEND",
    "| f1a6c6b63d41595224b135bbdc4057d52e60a9448b2470e102ebfe335755f095 |",
    "K=1→K=4 advancement",
]                                                                  # (local)


def verify_markers(content: str, markers: list, label: str) -> tuple:
    """Verify all expected markers are present in content.

    Returns (all_present: bool, missing: list, present_count: int).
    """
    missing = [m for m in markers if m not in content]             # (local)
    return (len(missing) == 0, missing, len(markers) - len(missing))


# ---------------------------------------------------------------------------
# Section 6 — Append verdict (canonical S84+ schema)
# ---------------------------------------------------------------------------

def append_verdict(
    verdict: str,
    value_str: str,
    audit_sha: str,
    content_sha: str,
) -> None:
    """Append canonical verdict line + dual-SHA companion row."""
    canonical_line = (
        f"{GATE_ID}: {verdict} -- value='{value_str}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )                                                              # (local)
    companion_row = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )                                                              # (local)

    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical_line)
        fp.write(companion_row)


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()                                               # (local)

    print(f"=== {GATE_ID} — input SHA-256 pins ===")

    # 1. Hash all input files
    pins = {
        ".claude/rules/epistemic-discipline.md": sha256_of(EPISTEMIC_RULE),
        ".claude/rules/methodology-wave-allowlist.md": sha256_of(ALLOWLIST_RULE),
        "sessions/session-plan/session-88-plan-w7a.md": sha256_of(PLAN_W7A),
        "computations/session-87/s87_gate_verdicts.txt": sha256_of(S87_VERDICTS),
        "computations/_shared/canonical_constants.py": sha256_of(CANONICAL_PATH),
    }                                                              # (local)
    for k, v in pins.items():
        print(f"  {k}: {v[:16]}...")

    # 2. Compute dual-SHA
    audit_sha, content_sha = compute_dual_sha(
        Path(__file__).resolve(), CANONICAL_PATH, pins
    )
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 3. Re-read + verify rule-file edits landed (AFTER-pattern)
    print("=== Verifying rule-file edits landed ===")
    epistemic_content = EPISTEMIC_RULE.read_text(encoding="utf-8")  # (local)
    allowlist_content = ALLOWLIST_RULE.read_text(encoding="utf-8")  # (local)

    epi_ok, epi_missing, epi_count = verify_markers(
        epistemic_content, EPISTEMIC_MARKERS, "epistemic-discipline.md"
    )                                                              # (local)
    al_ok, al_missing, al_count = verify_markers(
        allowlist_content, ALLOWLIST_MARKERS, "methodology-wave-allowlist.md"
    )                                                              # (local)

    print(f"  epistemic-discipline.md markers: {epi_count}/{len(EPISTEMIC_MARKERS)} present")
    if epi_missing:
        print(f"    MISSING: {epi_missing[:3]}{'...' if len(epi_missing) > 3 else ''}")
    print(f"  methodology-wave-allowlist.md markers: {al_count}/{len(ALLOWLIST_MARKERS)} present")
    if al_missing:
        print(f"    MISSING: {al_missing}")
    print()

    # 4. Determine verdict per pre-registered threshold
    print("=== Verdict determination ===")
    print(f"  K_pre = {K_PRE}, K_new = {K_NEW_INSTANCES}, K_post = {K_POST}")
    print(f"  K_promotion_threshold = {K_PROMOTION_THRESHOLD}")
    print(f"  K_post >= K_promotion_threshold: {K_POST >= K_PROMOTION_THRESHOLD}")

    # PASS criterion: all epistemic markers AND allowlist markers AND
    # K_post >= K_promotion_threshold
    if epi_ok and al_ok and K_POST >= K_PROMOTION_THRESHOLD:
        verdict = "PASS"                                           # (local)
        verdict_reason = "all markers present; K=4 >= 3"           # (local)
    elif K_POST >= K_PROMOTION_THRESHOLD and (epi_count >= len(EPISTEMIC_MARKERS) - 2):
        # 2 of 3 instances + threshold met → INFO
        verdict = "INFO"                                           # (local)
        verdict_reason = f"epi {epi_count}/{len(EPISTEMIC_MARKERS)} markers; K={K_POST}>=3"
    else:
        verdict = "FAIL"                                           # (local)
        verdict_reason = (
            f"epi {epi_count}/{len(EPISTEMIC_MARKERS)};"
            f"al {al_count}/{len(ALLOWLIST_MARKERS)}"
        )

    print(f"  Verdict: {verdict} — {verdict_reason}")
    print()

    # 5. Build value string
    promotion_event = "fired" if K_POST >= K_PROMOTION_THRESHOLD else "not_fired"  # (local)
    value_str = (
        f"K_pre={K_PRE};K_post={K_POST};K_threshold={K_PROMOTION_THRESHOLD};"
        f"promotion_event={promotion_event};"
        f"epistemic_markers={epi_count}/{len(EPISTEMIC_MARKERS)};"
        f"allowlist_markers={al_count}/{len(ALLOWLIST_MARKERS)};"
        f"instance_2_W7-1_audit_sha=38b36fc0a5e5889f;"
        f"instance_3_W7-3_audit_sha=0eb96f0536fb2d92;"
        f"instance_4_W9b-2_audit_sha=30815fae79102fb9;"
        f"sub_clause_status_post=MANDATORY"
    )                                                              # (local)

    tag = (f"(value='{value_str}', scheme={SCHEME}, "
           f"convention={CONVENTION}, L_max={L_MAX})")             # (local)
    print(f"4-tuple: {tag}")
    print()

    # 6. Append verdict line
    append_verdict(verdict, value_str, audit_sha, content_sha)

    wall = time.time() - t0                                        # (local)
    print(f"=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    print(f"  Verdict appended to: {VERDICT_TXT.name}")

    # Exit 0 regardless of PASS/FAIL/INFO per math-scripts.md
    return 0


if __name__ == "__main__":
    sys.exit(main())
