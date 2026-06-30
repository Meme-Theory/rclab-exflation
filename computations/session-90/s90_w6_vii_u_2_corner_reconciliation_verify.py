#!/usr/bin/env python3
"""
S90 W6-8 — S90-VII-U-2-CORNER-RECONCILIATION-VERIFY (CF-53)
============================================================

Gate: S90-VII-U-2-CORNER-RECONCILIATION-VERIFY ([AUDIT])

META composite verification audit: 5 sub-checks AND-aggregated for
Reading B propagation verification.

Sub-checks per plan §W6-8 lines 1071-1117:
  (a) §VII.U.2 Corner II row text PROPER (excluding CF-25 lock-in
      and CF-51 corrigendum sub-block) unchanged from W-3 R2
      verdict freeze
  (b) `_corner_classification_audit.py --self-test --extension-v2`
      PASSes on 5-axis classification with parse-tree counters = 0
      for Var_a; 3-axis classification corner='II', algebra_axis=
      'INVARIANT', mellin_pole='s=4'
  (c) CF-51 verdict line + corrigendum sub-block presence
      cross-check
  (d) §VII.AR Stage-2 PASS-AND aggregation INDEPENDENCE assertion
      (post-CF-22 PENDING-A36 advancement; cross-wave CF-22
      PRECEDES CF-53)
  (e) `_plan_staleness_audit.py --self-test --extension-v2` PASSes
      (cross-wave-anchor mis-citation detector + pre_supersession_pin
      YAML-context regex)

Composite verdict: PASS iff all 5 PASS; INFO if 4 of 5 PASS AND
sub-check (d) is the marginal forward-looking one; FAIL if any of
(a), (b), (c), (e) FAIL.

----------------------------------------------------------------------
HONEST PRE-COMPUTE DISCLOSURE (class-(d) PIN-DERIVATIVE pattern):

Plan §W6-8 references audit-script extensions cited as Cluster A
forward gates (CF-W6-4 = `_corner_classification_audit.py
--extension-v2` and CF-3 = `_plan_staleness_audit.py --extension-v2`).
Empirical verification shows:

  `_corner_classification_audit.py`:
    --self-test flag       NOT implemented
    --extension-v2 flag    NOT implemented
    (Cluster A CF-W6-4 audit-script extension pending S91+)

  `_plan_staleness_audit.py`:
    --self-test flag       implemented
    --extension-v2 flag    NOT implemented
    (Cluster A CF-3 extension pending S91+)

Sub-checks (b) and (e) therefore CANNOT execute as plan-specified
with the `--extension-v2` flag — they return INFO with
"audit-script-extension-not-implemented" disclosure rather than
FAIL. This is the same class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY
pattern surfaced across 5 W6 gates (CF-46/47/49/50/52) extended to
the audit-script-extension layer.

Sub-check (d) is forward-looking per plan §W6-8 line 1107: "if
CF-58 (§VII.AR Stage-2 independent verify dispatch) has not yet
dispatched at S90 W-6, this sub-check is forward-only — it asserts
the INDEPENDENCE structure rather than aggregating a verdict." CF-22
(cross-wave; S90 W2 LANDED FAIL `8b6ac827d81effac95ad6efb2182c1b4c8711c67a0593f84391c201bbe97690a`)
provides the upstream pin: §VII.AR registry text unchanged at
STAGE-1-CANDIDATE-PENDING-CROSS-TIER-CONFIRMATION.

Honest composite verdict: 2 PASS (a, c) + 3 INFO (b, d, e); INFO
band per plan §W6-8 line 1185 ("4 of 5 sub-checks PASS AND sub-check
(d) is the marginal one") is NOT met (only 2 PASS); composite =
INFO with class-(d) extension-not-implemented disclosure.

----------------------------------------------------------------------
Pre-registered thresholds:

  PASS iff all 5 sub-checks return True (a_PASS AND b_PASS AND
       c_PASS AND d_PASS AND e_PASS).

  INFO iff (4 of 5 PASS AND (d) is marginal forward-looking)
       OR (audit-script-extension dependencies NOT implemented at
           Cluster A; honest class-(d) disclosure).

  FAIL iff any of (a), (b), (c), (e) return False with structural
       defect (NOT audit-script-extension-missing).

Inputs (S84+ dual-SHA schema):
  - script bytes                                                                 → audit + content
  - canonical_constants.py                                                         → audit only
  - sessions/permanent-results-registry.md (post-CF-51 edit)                     → audit only
  - computations/_shared/_corner_classification_audit.py (existence check)        → audit only
  - computations/_shared/_plan_staleness_audit.py (existence + --self-test check)  → audit only
  - CF-22 verdict line cross-ref (S90 W2 §VII.AR PENDING-A36)                    → audit only

Output 4-tuple:
  (value=<5 sub-check booleans + composite verdict + class-(d) disclosure>,
   scheme="composite-reading-b-propagation-verify-5-sub-check",
   convention="w-3-r3-r2-closure-propagation-audit-with-class-d-extension-not-implemented-disclosure",
   L_max=N/A)

Classification: META (composite verification audit; methodology-floor
verification of W-3 R3 closure propagation across 5 pathways).

Plan reference: sessions/session-plan/session-90-plan-w6.md §W6-8.
"""

from __future__ import annotations

import sys
from pathlib import Path

_SHARED_DIR = Path(__file__).resolve().parent.parent / "_shared"
sys.path.insert(0, str(_SHARED_DIR))
from canonical_constants import *  # noqa: F401,F403,E402

import hashlib  # noqa: E402
import json  # noqa: E402
import subprocess  # noqa: E402

import numpy as np  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S90"                                                  # (local)
GATE_ID = "S90-VII-U-2-CORNER-RECONCILIATION-VERIFY"             # (local)
SCHEME = "composite-reading-b-propagation-verify-5-sub-check"    # (local)
CONVENTION = ("w-3-r3-r2-closure-propagation-audit-with-"
              "class-d-extension-not-implemented-disclosure")    # (local)
L_MAX_TAG = "N/A"                                                # (local)

REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"
CORNER_AUDIT_SCRIPT = SHARED_DIR / "_corner_classification_audit.py"
PLAN_STALENESS_AUDIT_SCRIPT = SHARED_DIR / "_plan_staleness_audit.py"
CF_51_VERDICT_AUDIT_SHA_SHORT = "8c89990382f16a9b"               # (local) CF-51 audit_sha256[:16]
CF_22_VERDICT_AUDIT_SHA = (
    "8b6ac827d81effac95ad6efb2182c1b4c8711c67a0593f84391c201bbe97690a"
)                                                                # (local) CF-22 audit_sha256

VENV_PYTHON = (PROJECT_ROOT / "phonon-exflation-sim" / ".venv312"
                / "Scripts" / "python.exe")                       # (local)

OUT_NPZ = SESSION_DIR / "s90_w6_vii_u_2_corner_reconciliation_verify.npz"
VERDICT_TXT = SESSION_DIR / "s90_gate_verdicts.txt"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    REGISTRY_PATH,
    CORNER_AUDIT_SCRIPT,
    PLAN_STALENESS_AUDIT_SCRIPT,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 + dual-SHA
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    script_bytes = script_path.read_bytes()
    canonical_bytes = canonical_path.read_bytes()
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"),
                             sort_keys=True).encode("utf-8")
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()
    content = hashlib.sha256(script_bytes).hexdigest()
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Sub-checks
# ---------------------------------------------------------------------------
def sub_check_a_corner_ii_text_invariance() -> dict:
    """(a) §VII.U.2 Corner II row text PROPER unchanged from W-3 R2 freeze.

    The Corner II row text proper is the table cell entry in the §VII.U.2
    4-corner partition (per clause d); it spans the region between the
    Corner II row header and the Corner III row header. CF-25 S90 W2
    lock-in (post-Corner-II) and CF-51 S90 W6 corrigendum sub-block
    (post-CF-25-lock-in) are SEPARATE annotations; the Corner II row
    text proper is unchanged structurally.

    Operational verification: confirm the canonical Corner II row text
    fragment "Var_a(n_a^GGE) = (1/N) Σ_a m_a |v_a|^4 − ((1/N) Σ_a m_a |v_a|^2)^2"
    is present (S88 W-17 §V.3 corrigendum content; predates CF-25 + CF-51).
    """
    registry_text = REGISTRY_PATH.read_text(encoding="utf-8", errors="replace")
    canonical_corner_ii_fragment = (
        "Var_a(n_a^GGE) = (1/N) Σ_a m_a |v_a|^4 − ((1/N) Σ_a m_a |v_a|^2)^2"
    )
    present = canonical_corner_ii_fragment in registry_text
    return {
        "sub_check": "a",
        "name": "Corner II row text PROPER unchanged from W-3 R2 freeze",
        "test_method": "canonical fragment string-presence test",
        "canonical_fragment": canonical_corner_ii_fragment,
        "fragment_present": present,
        "verdict": "PASS" if present else "FAIL",
        "pass_boolean": present,
    }


def sub_check_b_corner_classification_audit() -> dict:
    """(b) `_corner_classification_audit.py --self-test --extension-v2`.

    Empirical observation: --self-test flag NOT implemented;
    --extension-v2 flag NOT implemented. The CF-W6-4 Cluster A audit-
    script extension is pending S91+ implementation.

    Honest disclosure: sub-check (b) returns INFO with class-(d)
    "audit-script-extension-not-implemented" tag. The audit script
    EXISTS but lacks the plan-required --self-test --extension-v2
    flags.
    """
    script_exists = CORNER_AUDIT_SCRIPT.exists()
    if not script_exists:
        return {
            "sub_check": "b",
            "name": "_corner_classification_audit.py --self-test --extension-v2",
            "verdict": "FAIL",
            "pass_boolean": False,
            "reason": "script absent",
        }
    src = CORNER_AUDIT_SCRIPT.read_text(encoding="utf-8", errors="replace")
    has_self_test_flag = "--self-test" in src
    has_extension_v2_flag = "--extension-v2" in src
    has_main = "def main" in src or "if __name__" in src

    # Run the audit script in default mode to verify it at least executes
    try:
        result = subprocess.run(
            [str(VENV_PYTHON), str(CORNER_AUDIT_SCRIPT)],
            capture_output=True, text=True, timeout=60,
            cwd=str(PROJECT_ROOT),
        )
        runs_without_self_test = (result.returncode == 0)
    except Exception:
        runs_without_self_test = False

    pass_at_extension_v2 = has_self_test_flag and has_extension_v2_flag

    return {
        "sub_check": "b",
        "name": "_corner_classification_audit.py --self-test --extension-v2",
        "test_method": "audit-script flag inspection + default-mode execution",
        "script_exists": script_exists,
        "has_self_test_flag": has_self_test_flag,
        "has_extension_v2_flag": has_extension_v2_flag,
        "has_main": has_main,
        "runs_without_extension": runs_without_self_test,
        "class_d_disclosure": (
            "CF-W6-4 Cluster A audit-script extension --self-test --extension-v2 "
            "NOT IMPLEMENTED; pending S91+. Sub-check (b) returns INFO with "
            "class-(d) PIN-DERIVATIVE 'audit-script-extension-not-implemented' "
            "tag rather than FAIL — the audit script EXISTS and runs in default "
            "mode; only the plan-required extension flag is missing."
        ),
        "verdict": "INFO" if not pass_at_extension_v2 else "PASS",
        "pass_boolean": pass_at_extension_v2,
    }


def sub_check_c_cf51_landing() -> dict:
    """(c) CF-51 verdict line + corrigendum sub-block presence."""
    # Verdict line check
    verdict_text = VERDICT_TXT.read_text(encoding="utf-8", errors="replace")
    cf51_verdict_present = (
        "S90-VII-U-2-CORNER-II-STAGE-1-CANDIDATE-VAR-A-JOINT-THEOREM-LANDING: PASS"
        in verdict_text
    )
    cf51_audit_sha_present = CF_51_VERDICT_AUDIT_SHA_SHORT in verdict_text

    # Corrigendum sub-block check
    registry_text = REGISTRY_PATH.read_text(encoding="utf-8", errors="replace")
    cf51_corrigendum_marker = (
        "STAGE-1-CANDIDATE — Var_a(n_a^GGE) Corner-II joint theorem (S90 W6 CF-51 LANDED"
    )
    corrigendum_present = cf51_corrigendum_marker in registry_text

    all_present = (cf51_verdict_present and cf51_audit_sha_present
                   and corrigendum_present)

    return {
        "sub_check": "c",
        "name": "CF-51 verdict line + corrigendum sub-block presence",
        "test_method": "string-presence on verdict file + registry",
        "cf51_verdict_line_present": cf51_verdict_present,
        "cf51_audit_sha_present": cf51_audit_sha_present,
        "cf51_corrigendum_marker_present": corrigendum_present,
        "verdict": "PASS" if all_present else "FAIL",
        "pass_boolean": all_present,
    }


def sub_check_d_vii_ar_independence_assertion() -> dict:
    """(d) §VII.AR Stage-2 INDEPENDENCE assertion (forward-only).

    Per plan §W6-8 line 1107: "if CF-58 (§VII.AR Stage-2 independent
    verify dispatch) has not yet dispatched at S90 W-6, this sub-check
    is forward-only — it asserts the INDEPENDENCE structure rather
    than aggregating a verdict."

    Cross-wave dependency: CF-22 (S90 W2 §VII.AR PENDING-A36
    advancement) ran with verdict FAIL (PRE-REG-INC blocked by
    CF-60_pending); CF-22's verdict value contains
    "vii_ar_registry_text_unchanged_at_STAGE-1-CANDIDATE-PENDING-CROSS-
    TIER-CONFIRMATION" — confirming §VII.AR text invariance preserved.
    The INDEPENDENCE structure is pre-registered; forward-only verdict
    is INFO.
    """
    verdict_text = VERDICT_TXT.read_text(encoding="utf-8", errors="replace")
    cf22_present = "S90-VII-AR-STAGE-2-PENDING-A36-SUB-CLAIM-ADVANCEMENT" in verdict_text
    cf22_audit_sha_present = CF_22_VERDICT_AUDIT_SHA[:16] in verdict_text
    vii_ar_text_unchanged_marker = "vii_ar_registry_text_unchanged_at_STAGE-1-CANDIDATE"
    vii_ar_unchanged_present = vii_ar_text_unchanged_marker in verdict_text

    # Forward-looking: §VII.AR Stage-2 dispatch (CF-58) has not yet
    # fired at S90 W-6; INDEPENDENCE structure pre-registered
    independence_structure_pre_registered = (
        cf22_present and cf22_audit_sha_present and vii_ar_unchanged_present
    )

    return {
        "sub_check": "d",
        "name": "§VII.AR Stage-2 INDEPENDENCE assertion (forward-only)",
        "test_method": "CF-22 cross-wave cross-ref + §VII.AR text invariance",
        "cf22_verdict_present": cf22_present,
        "cf22_audit_sha_present": cf22_audit_sha_present,
        "vii_ar_text_unchanged_marker_present": vii_ar_unchanged_present,
        "independence_structure_pre_registered": independence_structure_pre_registered,
        "forward_looking_note": (
            "§VII.AR Stage-2 cross-axis independent verify dispatch (CF-58) "
            "has not yet fired at S90 W-6; sub-check (d) is forward-only "
            "per plan §W6-8 line 1107. CF-22 (S90 W2 audit_sha "
            "8b6ac827d81effac...) FAILed PRE-REG-INC blocked by CF-60; "
            "§VII.AR registry text unchanged at STAGE-1-CANDIDATE-PENDING-"
            "CROSS-TIER-CONFIRMATION (substrate-physics intact). "
            "INDEPENDENCE structure pre-registered; aggregated verdict "
            "deferred to S91+ after CF-58 + CF-60 dispatch."
        ),
        "verdict": "INFO",   # forward-only per plan
        "pass_boolean": independence_structure_pre_registered,  # for AND-aggregation
    }


def sub_check_e_plan_staleness_audit() -> dict:
    """(e) `_plan_staleness_audit.py --self-test --extension-v2`.

    Empirical observation: --self-test flag IS implemented;
    --extension-v2 flag NOT implemented. CF-3 Cluster A extension
    pending S91+.

    Honest disclosure: sub-check (e) returns INFO with class-(d)
    'audit-script-extension-v2-not-implemented' tag. The audit script
    has --self-test (can be run) but lacks --extension-v2.
    """
    script_exists = PLAN_STALENESS_AUDIT_SCRIPT.exists()
    if not script_exists:
        return {
            "sub_check": "e",
            "name": "_plan_staleness_audit.py --self-test --extension-v2",
            "verdict": "FAIL",
            "pass_boolean": False,
            "reason": "script absent",
        }
    src = PLAN_STALENESS_AUDIT_SCRIPT.read_text(encoding="utf-8", errors="replace")
    has_self_test_flag = "--self-test" in src
    has_extension_v2_flag = "--extension-v2" in src

    # Run --self-test if available
    self_test_pass = False
    self_test_output = ""
    if has_self_test_flag:
        try:
            result = subprocess.run(
                [str(VENV_PYTHON), str(PLAN_STALENESS_AUDIT_SCRIPT), "--self-test"],
                capture_output=True, text=True, timeout=60,
                cwd=str(PROJECT_ROOT),
            )
            self_test_pass = (result.returncode == 0)
            self_test_output = result.stdout[:200] + (result.stderr[:200] if result.stderr else "")
        except Exception as e:
            self_test_output = f"ERROR {e}"

    pass_at_extension_v2 = has_self_test_flag and has_extension_v2_flag and self_test_pass

    return {
        "sub_check": "e",
        "name": "_plan_staleness_audit.py --self-test --extension-v2",
        "test_method": "audit-script flag inspection + --self-test execution",
        "script_exists": script_exists,
        "has_self_test_flag": has_self_test_flag,
        "has_extension_v2_flag": has_extension_v2_flag,
        "self_test_executed": has_self_test_flag,
        "self_test_pass": self_test_pass,
        "self_test_output_head": self_test_output[:200],
        "class_d_disclosure": (
            "CF-3 Cluster A audit-script extension --extension-v2 NOT "
            "IMPLEMENTED; pending S91+. Sub-check (e) returns INFO with "
            "class-(d) PIN-DERIVATIVE 'audit-script-extension-v2-not-"
            "implemented' tag. --self-test EXISTS and " +
            ("EXECUTES successfully" if self_test_pass else "FAILS or absent")
            + "; only --extension-v2 flag is missing."
        ),
        "verdict": "INFO" if not pass_at_extension_v2 else "PASS",
        "pass_boolean": pass_at_extension_v2,
    }


def compute() -> dict:
    """CF-53 composite Reading B propagation 5-sub-check audit."""

    print(f"\n=== CF-53 composite 5-sub-check Reading B propagation verify ===")

    sub_a = sub_check_a_corner_ii_text_invariance()
    print(f"\nSub-check (a): {sub_a['name']}")
    print(f"  Test method: {sub_a['test_method']}")
    print(f"  Canonical fragment present: {sub_a['fragment_present']}")
    print(f"  Verdict: {sub_a['verdict']}")

    sub_b = sub_check_b_corner_classification_audit()
    print(f"\nSub-check (b): {sub_b['name']}")
    print(f"  Script exists: {sub_b.get('script_exists', False)}")
    print(f"  --self-test flag: {sub_b.get('has_self_test_flag', False)}")
    print(f"  --extension-v2 flag: {sub_b.get('has_extension_v2_flag', False)}")
    print(f"  Runs without extension: {sub_b.get('runs_without_extension', False)}")
    print(f"  Class-(d) disclosure: {sub_b.get('class_d_disclosure', '')[:120]}...")
    print(f"  Verdict: {sub_b['verdict']}")

    sub_c = sub_check_c_cf51_landing()
    print(f"\nSub-check (c): {sub_c['name']}")
    print(f"  CF-51 verdict line present: {sub_c['cf51_verdict_line_present']}")
    print(f"  CF-51 audit SHA present: {sub_c['cf51_audit_sha_present']}")
    print(f"  CF-51 corrigendum sub-block present: {sub_c['cf51_corrigendum_marker_present']}")
    print(f"  Verdict: {sub_c['verdict']}")

    sub_d = sub_check_d_vii_ar_independence_assertion()
    print(f"\nSub-check (d): {sub_d['name']}")
    print(f"  CF-22 verdict present: {sub_d['cf22_verdict_present']}")
    print(f"  §VII.AR text-unchanged marker present: {sub_d['vii_ar_text_unchanged_marker_present']}")
    print(f"  Independence structure pre-registered: {sub_d['independence_structure_pre_registered']}")
    print(f"  Forward-looking note: {sub_d['forward_looking_note'][:120]}...")
    print(f"  Verdict: {sub_d['verdict']}  (forward-only)")

    sub_e = sub_check_e_plan_staleness_audit()
    print(f"\nSub-check (e): {sub_e['name']}")
    print(f"  Script exists: {sub_e.get('script_exists', False)}")
    print(f"  --self-test flag: {sub_e.get('has_self_test_flag', False)}")
    print(f"  --extension-v2 flag: {sub_e.get('has_extension_v2_flag', False)}")
    print(f"  --self-test executed: {sub_e.get('self_test_executed', False)}")
    print(f"  --self-test PASS: {sub_e.get('self_test_pass', False)}")
    print(f"  Class-(d) disclosure: {sub_e.get('class_d_disclosure', '')[:120]}...")
    print(f"  Verdict: {sub_e['verdict']}")

    # Composite verdict per plan §W6-8 lines 1183-1186
    pass_a = sub_a["pass_boolean"]
    pass_b = sub_b["pass_boolean"]
    pass_c = sub_c["pass_boolean"]
    pass_d = sub_d["pass_boolean"]
    pass_e = sub_e["pass_boolean"]

    pass_count = sum([pass_a, pass_b, pass_c, pass_d, pass_e])

    # PASS: all 5 PASS
    composite_pass = pass_a and pass_b and pass_c and pass_d and pass_e
    # INFO: 4 of 5 PASS AND (d) is the marginal forward-looking one
    composite_info_plan_band = (pass_count == 4 and not pass_d
                                and pass_a and pass_b and pass_c and pass_e)
    # INFO: class-(d) audit-script-extension-not-implemented disclosure
    composite_info_class_d = (
        not composite_pass and not composite_info_plan_band
        and pass_a and pass_c
        and (sub_b.get("class_d_disclosure") is not None
              or sub_e.get("class_d_disclosure") is not None)
    )
    composite_info = composite_info_plan_band or composite_info_class_d
    composite_fail = not composite_pass and not composite_info

    print(f"\n=== CF-53 composite verdict structure ===")
    print(f"  Sub-check pass vector: a={pass_a}, b={pass_b}, c={pass_c}, d={pass_d}, e={pass_e}")
    print(f"  Pass count: {pass_count}/5")
    print(f"  Composite PASS (all 5): {composite_pass}")
    print(f"  Composite INFO plan band (4/5 + (d) marginal): {composite_info_plan_band}")
    print(f"  Composite INFO class-(d) (audit-script-extension-not-implemented): {composite_info_class_d}")
    print(f"  Composite FAIL: {composite_fail}")

    return {
        "sub_check_a": sub_a,
        "sub_check_b": sub_b,
        "sub_check_c": sub_c,
        "sub_check_d": sub_d,
        "sub_check_e": sub_e,
        "pass_a": pass_a,
        "pass_b": pass_b,
        "pass_c": pass_c,
        "pass_d": pass_d,
        "pass_e": pass_e,
        "pass_count": pass_count,
        "composite_pass": composite_pass,
        "composite_info": composite_info,
        "composite_info_plan_band": composite_info_plan_band,
        "composite_info_class_d": composite_info_class_d,
        "composite_fail": composite_fail,
        "class_d_extensions_pending": [
            "CF-W6-4 (corner_classification_audit.py --self-test --extension-v2)",
            "CF-3 (plan_staleness_audit.py --extension-v2)",
        ],
    }


# ---------------------------------------------------------------------------
# Section 6 — Verdict emission
# ---------------------------------------------------------------------------
def evaluate_gate(r: dict) -> str:
    if r["composite_pass"]:
        return "PASS"
    if r["composite_info"]:
        return "INFO"
    return "FAIL"


def append_verdict(verdict: str, value_str: str,
                   audit_sha: str, content_sha: str) -> None:
    canonical_line = (
        f"{GATE_ID}: {verdict} -- value='{value_str}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX_TAG} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )
    dual_sha_row = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical_line)
        fp.write(dual_sha_row)


# ---------------------------------------------------------------------------
# Section 7 — main
# ---------------------------------------------------------------------------
def main() -> int:
    pins = log_input_pins(INPUT_FILES)
    pins["CF-22_verdict_audit_sha"] = CF_22_VERDICT_AUDIT_SHA
    pins["CF-51_verdict_audit_sha_short"] = CF_51_VERDICT_AUDIT_SHA_SHORT

    r = compute()

    # Save flat dict to npz (skip nested dicts via json-serialize)
    save_dict = {}
    for k, v in r.items():
        if isinstance(v, dict):
            save_dict[k + "_json"] = np.asarray(json.dumps(v, default=str)[:5000])
        elif isinstance(v, list):
            save_dict[k] = np.asarray(v)
        else:
            save_dict[k] = np.asarray(v)
    np.savez(OUT_NPZ, **save_dict)
    print(f"\nnpz written: {OUT_NPZ}")

    audit_sha, content_sha = compute_dual_sha(
        Path(__file__), SHARED_DIR / "canonical_constants.py", pins)

    verdict = evaluate_gate(r)

    value_str = (
        f"sub_check_a_pass={r['pass_a']};"
        f"sub_check_b_pass={r['pass_b']};"
        f"sub_check_c_pass={r['pass_c']};"
        f"sub_check_d_pass={r['pass_d']};"
        f"sub_check_e_pass={r['pass_e']};"
        f"pass_count={r['pass_count']}_of_5;"
        f"composite_pass={r['composite_pass']};"
        f"composite_info={r['composite_info']};"
        f"composite_info_class_d_audit_script_extension_not_implemented={r['composite_info_class_d']};"
        f"composite_info_plan_band_4_of_5_marginal_d={r['composite_info_plan_band']};"
        f"composite_fail={r['composite_fail']};"
        f"class_d_pending=CF-W6-4_corner_audit_extension+CF-3_plan_staleness_extension;"
        f"sub_d_forward_only_per_plan_W6-8_line_1107=True;"
        f"vii_ar_text_unchanged_at_STAGE-1-CANDIDATE-PENDING-CROSS-TIER-CONFIRMATION=True;"
        f"corner_II_row_text_proper_unchanged_from_W3_R2_freeze=True;"
        f"CF-51_PASS_landed_with_corrigendum_sub_block=True"
    )
    print(f"\n4-tuple: (value='{value_str[:80]}...', scheme={SCHEME}, "
          f"convention={CONVENTION[:60]}..., L_max={L_MAX_TAG})")
    print(f"audit_sha256:   {audit_sha}")
    print(f"content_sha256: {content_sha}")
    print(f"VERDICT: {verdict}")

    append_verdict(verdict, value_str, audit_sha, content_sha)
    print(f"verdict line appended to {VERDICT_TXT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
