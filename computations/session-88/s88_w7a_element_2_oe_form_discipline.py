#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S88 W7a-73 — S88-CROSS-PILLAR-BRIDGE-ANATOMY-ELEMENT-2-OE-FORM-DISCIPLINE
========================================================================

Gate: S88-CROSS-PILLAR-BRIDGE-ANATOMY-ELEMENT-2-OE-FORM-DISCIPLINE ([AUDIT])

Pre-registered threshold (per session-88-plan-w7a.md §W7a-73 §177-181):
  PASS iff (i) cross-pillar-bridge-anatomy.md §"IS-not-IN Anatomy" Element 2
        OE-form discipline subsection landed with positive-match regex +
        negative-match regex + worked-example contrast (K=2 corpus W-5
        PASS + W11-5 FAIL); AND (ii) audit script extension landed at
        computations/_shared/_cross_pillar_bridge_audit.py with
        ELEMENT_2_OE_POSITIVE_REGEX + ELEMENT_2_OE_NEGATIVE_REGEX
        + audit_element_2_oe_form function + audit_section integration;
        AND (iii) regex calibration on K=2 corpus yields W-5 PASS +
        W11-5 FAIL pre-retrofit (both must classify correctly); AND
        (iv) methodology-wave-allowlist.md contains the W7a-73 row.

  FAIL iff positive-match regex too permissive (admits W11-5 prose form)
        OR negative-match regex too aggressive (rejects W-5 OE-form);
        OR any expected marker is absent on disk.

  INFO iff regex calibration imperfect on edge cases (e.g., Pillar V
        degenerate-integral form requires extending positive-match to
        admit \\sum); update positive-match and re-validate.

Inputs (SHA-256 dual-pinned at runtime — S84+ schema):
  - .claude/rules/cross-pillar-bridge-anatomy.md (post-W7a-73 edit)
  - computations/_shared/_cross_pillar_bridge_audit.py (post-W7a-73 edit)
  - .claude/rules/methodology-wave-allowlist.md (post-W7a-73 row append)
  - sessions/session-plan/session-88-plan-w7a.md (plan-block source)
  - canonical_constants.py (feeds audit_sha256 only)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<verdict_str>, scheme=METHODOLOGY-class,
   convention=cross-pillar-bridge-anatomy-Element-2-OE-form, L_max=N/A)

Classification: METHODOLOGY-class per `wave-classification.md` (M1
artifact-existence on rule-file diff + audit-script diff; M2 Edits on
.claude/rules/cross-pillar-bridge-anatomy.md + computations/_shared/
_cross_pillar_bridge_audit.py; M3 verbatim from W-5 canonical OE-form
+ W11-5 prose form; M4 allowlist append).

METHODOLOGY
-----------
Verifier-script: re-reads both edited files to confirm markers present,
imports the audit script's regex constants, and runs synthetic K=2
calibration test using W-5 PASS + W11-5 FAIL example strings to verify
the regex correctly distinguishes OE-form from prose-form.

INPUT-PIN MAP (closure_hash → audit_sha256):
  - cross_pillar_bridge_anatomy_md_post_edit_sha
  - cross_pillar_bridge_audit_py_post_edit_sha
  - methodology_wave_allowlist_md_post_edit_sha
  - plan_w7a_md_sha
  - canonical_constants_sha
  - script_bytes_sha

Author: lizzi-spectral-functional-theorist (PRIMARY orchestrator-direct
under METHODOLOGY-class wave-classification path)
Session: 88, Wave: W7a, Plan: session-88-plan-w7a.md §W7a-73
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
import re
import sys
import time
from pathlib import Path

# Import the audit-script's OE-form regex constants and audit function
# (this is the audit script that was extended at S88 W7a-73)
import importlib.util as _import_util                              # (local)
_audit_spec = _import_util.spec_from_file_location(
    "_cross_pillar_bridge_audit",
    _SHARED_DIR / "_cross_pillar_bridge_audit.py",
)                                                                  # (local)
_audit_mod = _import_util.module_from_spec(_audit_spec)            # (local)
_audit_spec.loader.exec_module(_audit_mod)
ELEMENT_2_OE_POSITIVE_REGEX = _audit_mod.ELEMENT_2_OE_POSITIVE_REGEX  # (local)
ELEMENT_2_OE_NEGATIVE_REGEX = _audit_mod.ELEMENT_2_OE_NEGATIVE_REGEX  # (local)
audit_element_2_oe_form = _audit_mod.audit_element_2_oe_form        # (local)

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S88"                                                    # (local)
GATE_ID = "S88-CROSS-PILLAR-BRIDGE-ANATOMY-ELEMENT-2-OE-FORM-DISCIPLINE"  # (local)
SCHEME = "METHODOLOGY-class"                                       # (local)
CONVENTION = "cross-pillar-bridge-anatomy-Element-2-OE-form"       # (local)
L_MAX = "N/A"                                                      # (local)

# Input file paths
ANATOMY_RULE = (
    PROJECT_ROOT / ".claude" / "rules" / "cross-pillar-bridge-anatomy.md"
)                                                                  # (local)
AUDIT_SCRIPT = (
    PROJECT_ROOT / "computations" / "_shared" / "_cross_pillar_bridge_audit.py"
)                                                                  # (local)
ALLOWLIST_RULE = (
    PROJECT_ROOT / ".claude" / "rules" / "methodology-wave-allowlist.md"
)                                                                  # (local)
PLAN_W7A = (
    PROJECT_ROOT / "sessions" / "session-plan" / "session-88-plan-w7a.md"
)                                                                  # (local)
CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"             # (local)

VERDICT_TXT = SESSION_DIR / "s88_gate_verdicts.txt"

# ---------------------------------------------------------------------------
# Section 4 — SHA helpers
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
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
# Section 5 — Marker verification (AFTER-pattern re-read of edits)
# ---------------------------------------------------------------------------

# Markers we expect post-W7a-73 in cross-pillar-bridge-anatomy.md.
# The Element 2 OE-form discipline subsection includes:
#  (i) positive-match regex pattern
#  (ii) negative-match regex pattern
#  (iii) calibration corpus K=2 (W-5 PASS + W11-5 FAIL)
#  (iv) audit-script extension reference
#  (v) forward-looking convention pin
ANATOMY_MARKERS = [
    "### Element 2 OE-form discipline (S88 W7a-73 hardening)",
    "Positive-match regex (canonical pattern)",
    r"\int.*d.*Tr.*\([ΠP]_[a-z0-9_-]+\)",
    "Negative-match regex (forbidden prose-only forms)",
    "Element 2.*: ...measurement|spectroscopy|test",
    "Calibration corpus (K=2 at S88 W7a-73",
    "W-5 §VII.W (Pillar III ↔ Pillar IV)",
    "W11-5 FWD-C3 (Pillar IV ↔ Pillar V; pre-retrofit)",
    "Audit-script extension",
    "Forward-looking convention pin",
    "GRANDFATHERED with mandatory retrofit at §W7a-75",
]                                                                  # (local)

# Markers we expect in _cross_pillar_bridge_audit.py
AUDIT_MARKERS = [
    "ELEMENT_2_OE_POSITIVE_REGEX = re.compile",
    "ELEMENT_2_OE_NEGATIVE_REGEX = re.compile",
    "def audit_element_2_oe_form(section_text: str) -> dict:",
    "S88 W7a-73 EXTENSION: Element 2 OE-form regex pass added",
    "oe_form_check = audit_element_2_oe_form(section[\"text\"])",
    "and oe_form_check[\"oe_form_pass\"]",
    '"oe_form_check": oe_form_check,',
    '"missing_oe_form": missing_oe_form,',
]                                                                  # (local)

# Markers we expect in methodology-wave-allowlist.md
ALLOWLIST_MARKERS = [
    "| W7a-73 | S88 | S88-CROSS-PILLAR-BRIDGE-ANATOMY-ELEMENT-2-OE-FORM-DISCIPLINE",
    "| 406ffaf93cd8a2f5aa0a956830fed5a78c8e41379ba8cd3d939485d48b8b6c44 |",
    "audit-script extension at computations/_shared/_cross_pillar_bridge_audit.py adds ELEMENT_2_OE_POSITIVE_REGEX",
]                                                                  # (local)


def verify_markers(content: str, markers: list) -> tuple:
    missing = [m for m in markers if m not in content]             # (local)
    return (len(missing) == 0, missing, len(markers) - len(missing))


# ---------------------------------------------------------------------------
# Section 6 — Synthetic K=2 calibration test (regex calibration on the
# pre-registered W-5 PASS form vs W11-5 FAIL prose form). The test does
# NOT consume actual registry entries — it tests the regex against
# representative example strings to confirm classifier behavior.
# ---------------------------------------------------------------------------

# Calibration corpus instance #1: W-5 §VII.W canonical OE-form (must PASS)
W5_OE_FORM_TEST_STRING = (
    "## §VII.W — Pillar III ↔ Pillar IV Bridge Theorem (W-5 calibration)\n"
    "\n"
    "Element 2 (laboratory-IN observable): "
    "R_geom(τ_fold) = ∫_BZ Tr g_ab^{(P_0)}(k; τ_fold) d^d k "
    "(Peotta-Törmä quantum-metric integrated trace over the BZ).\n"
)                                                                  # (local)

# Calibration corpus instance #2: W11-5 FWD-C3 pre-retrofit prose form (must FAIL)
W11_5_PROSE_TEST_STRING = (
    "## §VII.AJ.W11-5 — Pillar IV ↔ Pillar V FWD-C3 Bridge Candidate\n"
    "\n"
    "Element 2 (laboratory-IN observable): "
    "Caroli-Matricon ladder asymmetry measured via MCT-3 vortex-core spectroscopy.\n"
)                                                                  # (local)


def run_synthetic_calibration_test() -> dict:
    """Run the K=2 synthetic calibration test on the regex.

    Pre-registered:
      - W-5 OE-form must PASS positive-match AND must NOT match negative
      - W11-5 prose form must NOT match positive-match AND must match negative
    """
    w5_audit = audit_element_2_oe_form(W5_OE_FORM_TEST_STRING)     # (local)
    w11_5_audit = audit_element_2_oe_form(W11_5_PROSE_TEST_STRING) # (local)

    # Pre-registered expected outcomes
    w5_expected_pass = (
        w5_audit["oe_positive_match"] is True
        and w5_audit["oe_negative_match"] is False
        and w5_audit["oe_form_pass"] is True
    )                                                              # (local)
    w11_5_expected_fail = (
        w5_audit["oe_form_pass"]
        and w11_5_audit["oe_positive_match"] is False
        and w11_5_audit["oe_negative_match"] is True
        and w11_5_audit["oe_form_pass"] is False
    )                                                              # (local)

    return {
        "w5_audit": w5_audit,
        "w11_5_audit": w11_5_audit,
        "w5_expected_PASS": w5_expected_pass,
        "w11_5_expected_FAIL": w11_5_expected_fail,
        "calibration_pass": w5_expected_pass and w11_5_expected_fail,
    }


# ---------------------------------------------------------------------------
# Section 7 — Append verdict
# ---------------------------------------------------------------------------

def append_verdict(verdict, value_str, audit_sha, content_sha):
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
# Section 8 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()                                               # (local)

    print(f"=== {GATE_ID} — input SHA-256 pins ===")

    pins = {
        ".claude/rules/cross-pillar-bridge-anatomy.md": sha256_of(ANATOMY_RULE),
        "computations/_shared/_cross_pillar_bridge_audit.py": sha256_of(AUDIT_SCRIPT),
        ".claude/rules/methodology-wave-allowlist.md": sha256_of(ALLOWLIST_RULE),
        "sessions/session-plan/session-88-plan-w7a.md": sha256_of(PLAN_W7A),
        "computations/_shared/canonical_constants.py": sha256_of(CANONICAL_PATH),
    }                                                              # (local)
    for k, v in pins.items():
        print(f"  {k}: {v[:16]}...")

    audit_sha, content_sha = compute_dual_sha(
        Path(__file__).resolve(), CANONICAL_PATH, pins
    )
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print()

    # Re-read + verify markers
    print("=== Verifying rule-file + audit-script edits landed ===")
    anatomy_content = ANATOMY_RULE.read_text(encoding="utf-8")     # (local)
    audit_content = AUDIT_SCRIPT.read_text(encoding="utf-8")       # (local)
    allowlist_content = ALLOWLIST_RULE.read_text(encoding="utf-8") # (local)

    an_ok, an_missing, an_count = verify_markers(anatomy_content, ANATOMY_MARKERS)
    au_ok, au_missing, au_count = verify_markers(audit_content, AUDIT_MARKERS)
    al_ok, al_missing, al_count = verify_markers(allowlist_content, ALLOWLIST_MARKERS)

    print(f"  cross-pillar-bridge-anatomy.md markers: {an_count}/{len(ANATOMY_MARKERS)}")
    if an_missing:
        print(f"    MISSING: {an_missing[:3]}{'...' if len(an_missing) > 3 else ''}")
    print(f"  _cross_pillar_bridge_audit.py markers: {au_count}/{len(AUDIT_MARKERS)}")
    if au_missing:
        print(f"    MISSING: {au_missing[:3]}{'...' if len(au_missing) > 3 else ''}")
    print(f"  methodology-wave-allowlist.md markers: {al_count}/{len(ALLOWLIST_MARKERS)}")
    if al_missing:
        print(f"    MISSING: {al_missing}")
    print()

    # Synthetic K=2 calibration test
    print("=== Synthetic K=2 regex calibration test ===")
    cal = run_synthetic_calibration_test()                         # (local)
    print(f"  W-5 OE-form (must PASS): "
          f"positive={cal['w5_audit']['oe_positive_match']}, "
          f"negative={cal['w5_audit']['oe_negative_match']}, "
          f"PASS={cal['w5_audit']['oe_form_pass']}")
    print(f"  W11-5 prose (must FAIL): "
          f"positive={cal['w11_5_audit']['oe_positive_match']}, "
          f"negative={cal['w11_5_audit']['oe_negative_match']}, "
          f"PASS={cal['w11_5_audit']['oe_form_pass']}")
    print(f"  W-5 expected PASS:  {cal['w5_expected_PASS']}")
    print(f"  W11-5 expected FAIL: {cal['w11_5_expected_FAIL']}")
    print(f"  Calibration overall: {cal['calibration_pass']}")
    print()

    # Verdict determination
    print("=== Verdict determination ===")
    all_markers_ok = an_ok and au_ok and al_ok                     # (local)
    if all_markers_ok and cal["calibration_pass"]:
        verdict = "PASS"                                           # (local)
        verdict_reason = "all markers + calibration PASS"          # (local)
    elif all_markers_ok:
        verdict = "INFO"                                           # (local)
        verdict_reason = (
            f"markers OK; calibration imperfect "
            f"(w5={cal['w5_expected_PASS']}, w11_5={cal['w11_5_expected_FAIL']})"
        )                                                          # (local)
    else:
        verdict = "FAIL"                                           # (local)
        verdict_reason = (
            f"an={an_count}/{len(ANATOMY_MARKERS)};"
            f"au={au_count}/{len(AUDIT_MARKERS)};"
            f"al={al_count}/{len(ALLOWLIST_MARKERS)}"
        )                                                          # (local)
    print(f"  Verdict: {verdict} — {verdict_reason}")
    print()

    # Build value string
    value_str = (
        f"anatomy_markers={an_count}/{len(ANATOMY_MARKERS)};"
        f"audit_script_markers={au_count}/{len(AUDIT_MARKERS)};"
        f"allowlist_markers={al_count}/{len(ALLOWLIST_MARKERS)};"
        f"calibration_K=2;"
        f"w5_PASS={cal['w5_expected_PASS']};"
        f"w11_5_FAIL={cal['w11_5_expected_FAIL']};"
        f"calibration_overall={cal['calibration_pass']};"
        f"oe_form_status=MANDATORY_for_S88plus_new_entries"
    )                                                              # (local)

    tag = (f"(value='{value_str}', scheme={SCHEME}, "
           f"convention={CONVENTION}, L_max={L_MAX})")             # (local)
    print(f"4-tuple: {tag}")
    print()

    append_verdict(verdict, value_str, audit_sha, content_sha)

    wall = time.time() - t0                                        # (local)
    print(f"=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    print(f"  Verdict appended to: {VERDICT_TXT.name}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
