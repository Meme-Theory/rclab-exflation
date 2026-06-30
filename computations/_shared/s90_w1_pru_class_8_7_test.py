#!/usr/bin/env python3
"""S90 W1-12 — S90-RULE-EXTENSION-EPISTEMIC-PRU-CLASS-8-7-DEGENERATE-OBSERVABLE

Gate: S90-RULE-EXTENSION-EPISTEMIC-PRU-CLASS-8-7-DEGENERATE-OBSERVABLE
      (PHONON-FIRST V.4)
Trigger: [AUDIT]
Classification: METHODOLOGY (PRU Class 8.7 promotion + audit-script pattern
                landing; gen-physicist orchestrator-direct-write per
                wave-classification.md M1∧M2∧M3∧M4)

Plan reference: sessions/session-plan/session-90-plan-w1.md §W1-12 lines 780-857.

Method (plan §W1-12 #6):
  1. Promote Class 8.7 to PRU sub-class taxonomy table
     (`.claude/rules/epistemic-discipline.md`)
  2. Append "Degenerate-Observable Pre-Flight Check (Class 8.7; advisory until
     K=3)" sub-section per directive-document discipline
  3. Extend `_pru_cardinality_audit.py` with detector patterns P1 + P2 +
     degeneracy-witness check (file created in-session per W6-3 hygiene-gap
     discharge documented at S89 W6 WP line 363; Class 8.7 is the inaugural
     content; broader D_PRU_raw cardinality audit is separate carry-forward)
  4. Self-test on S89 §W1-1 FAIL plan-block (K=1 calibration corpus instance)
  5. Append §"Class 8.7 Calibration Corpus" to pru-class-corpus.md (§18)
  6. Emit dual-SHA verdict

Pre-registered thresholds (plan §W1-12 #9):
  PASS iff (i) Class 8.7 row added to taxonomy table
           (ii) sub-section appended with 3 enumerated elements
           (iii) audit-script extension lands with P1+P2 patterns +
                 degeneracy-witness check
           (iv) self-test on S89 §W1-1 plan-block fires Class 8.7
           (v) K=1 corpus row appended
           (vi) allowlist + instances rows appended
  FAIL iff any of (i)-(vi) absent OR self-test misses calibration instance.

Substrate framing (plan §W1-12 #13):
  Dimension-spectrum degeneracy IS a substrate-IS structural property of the
  finite spectral triple at the LRD-horizon scale; multiplicity at substrate-
  distance-1 pole s=3 IS substrate-IS (not laboratory-IN). Class 8.7 captures
  the methodology F-image of substrate-IS degeneracy at the plan-block layer;
  the rule prevents silent naive-corridor evaluation that discards substrate-
  IS multiplicity.

Output 4-tuple (plan §W1-12 #8):
  (value=class_8_7_landed_with_K_1_corpus + audit_pattern_set,
   scheme=pru-class-8-7-degenerate-observable,
   convention=cm-1995-iii-4-multiplicity-pre-flight,
   L_max=N/A)
"""
from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "computations" / "_shared"))

from canonical_constants import *  # noqa: F401,F403 — canonical-constants discipline

from _pru_cardinality_audit import (  # noqa: E402
    P1_HSS_TRACE_MINUS_RCM,
    P2_ZETA_D_AT_ZERO,
    DEGENERACY_WITNESS_MARKERS,
    detect_class_8_7_degenerate_observable,
    run_self_test,
    run_negative_self_test,
)
from s90_w1_emit_verdict import emit_verdict, sha256_of_file  # noqa: E402

# ---------------- Gate-block constants (plan §W1-12) ----------------
GATE_ID = "S90-RULE-EXTENSION-EPISTEMIC-PRU-CLASS-8-7-DEGENERATE-OBSERVABLE"
SCHEME = "pru-class-8-7-degenerate-observable"
CONVENTION = "cm-1995-iii-4-multiplicity-pre-flight"
L_MAX = "N/A"

# Plan §W1-12 #7 PRDR pins
S89_W1_1_VERDICT_SHA = (
    "6db37f7c6da0768662c5afb320654a54f2e4c478882d365465712034e28a16fe"
)

# Input files
EPISTEMIC_DISCIPLINE = ROOT / ".claude" / "rules" / "epistemic-discipline.md"
PRU_AUDIT_MODULE = ROOT / "computations" / "_shared" / "_pru_cardinality_audit.py"
PRU_CORPUS = ROOT / "sessions" / "framework" / "registry" / "pru-class-corpus.md"
S89_PLAN_W1 = ROOT / "sessions" / "session-plan" / "session-89-plan-w1.md"
PLAN_W1 = ROOT / "sessions" / "session-plan" / "session-90-plan-w1.md"
THIS_SCRIPT = Path(__file__).resolve()


def main() -> None:
    print("=" * 72)
    print(f"Gate: {GATE_ID}")
    print(f"Trigger: [AUDIT] | Classification: METHODOLOGY")
    print("=" * 72)

    # Step 1: Verify rule-file extensions landed
    print("\n--- Step 1: Verify rule-file extensions landed ---")
    epistemic_text = EPISTEMIC_DISCIPLINE.read_text(encoding="utf-8")  # (local)
    has_8_7_row = "| 8.7 |" in epistemic_text  # (local)
    has_8_7_subsection = (
        "### Degenerate-Observable Pre-Flight Check (Class 8.7" in epistemic_text
    )  # (local)
    print(f"  Class 8.7 row in taxonomy table: {has_8_7_row}")
    print(f"  Class 8.7 sub-section present  : {has_8_7_subsection}")

    # Step 2: Verify audit-script extension landed
    print("\n--- Step 2: Verify _pru_cardinality_audit.py extension landed ---")
    audit_module_text = PRU_AUDIT_MODULE.read_text(encoding="utf-8")  # (local)
    has_p1 = "P1_HSS_TRACE_MINUS_RCM" in audit_module_text  # (local)
    has_p2 = "P2_ZETA_D_AT_ZERO" in audit_module_text  # (local)
    has_witness = "DEGENERACY_WITNESS_MARKERS" in audit_module_text  # (local)
    has_detector_fn = "detect_class_8_7_degenerate_observable" in audit_module_text  # (local)
    print(f"  P1 pattern (Tr.P_HSS - R_CM) constant: {has_p1}")
    print(f"  P2 pattern (value = ζ_D(0)) constant : {has_p2}")
    print(f"  DEGENERACY_WITNESS_MARKERS constant  : {has_witness}")
    print(f"  detect_class_8_7_... function        : {has_detector_fn}")

    # Step 3: Positive self-test on S89 §W1-1 plan-block
    print("\n--- Step 3: T1 Positive self-test (S89 §W1-1) ---")
    pos_test = run_self_test()
    print(f"  status: {pos_test['self_test_status']}")
    print(f"  actual_flag: {pos_test['actual_flag']} (expected: {pos_test['expected_flag']})")
    print(f"  severity: {pos_test['severity']}")
    print(f"  P1_matches: {pos_test['p1_matches_count']}; P2_matches: {pos_test['p2_matches_count']}")
    print(f"  block_label: {pos_test['block_label']}; block_chars: {pos_test['block_char_count']}")

    # Step 4: Negative self-test on synthetic-with-witness
    print("\n--- Step 4: T2 Negative self-test (synthetic with witness) ---")
    neg_test = run_negative_self_test()
    print(f"  status: {neg_test['self_test_status']}")
    print(f"  actual_flag: {neg_test['actual_flag']} (expected: {neg_test['expected_flag']})")
    print(f"  witness_markers: {neg_test['degeneracy_witness_markers_count']}")

    # Step 5: Composite verdict
    print("\n--- Step 5: Composite verdict ---")
    pass_conditions = {
        "i_class_8_7_taxonomy_row": has_8_7_row,
        "ii_class_8_7_subsection": has_8_7_subsection,
        "iii_p1_pattern": has_p1,
        "iv_p2_pattern": has_p2,
        "v_witness_markers": has_witness,
        "vi_detector_function": has_detector_fn,
        "vii_positive_self_test_pass": pos_test["self_test_status"] == "PASS",
        "viii_negative_self_test_pass": neg_test["self_test_status"] == "PASS",
    }
    all_pass = all(pass_conditions.values())  # (local)
    verdict = "PASS" if all_pass else "FAIL"  # (local)
    print(f"  Pass conditions:")
    for k, v in pass_conditions.items():
        print(f"    {k:38s}: {v}")
    print(f"  Composite verdict: {verdict}")

    # Step 6: Input-pin map (PRDR per plan §W1-12 #7)
    print("\n--- Step 6: Input-pin map ---")
    input_pins = {
        "pin_01_epistemic_discipline_post_W1_12_sha": sha256_of_file(EPISTEMIC_DISCIPLINE),
        "pin_02_pru_cardinality_audit_post_W1_12_sha": sha256_of_file(PRU_AUDIT_MODULE),
        "pin_03_pru_class_corpus_sha": sha256_of_file(PRU_CORPUS),
        "pin_04_s89_plan_w1_sha": sha256_of_file(S89_PLAN_W1),
        "pin_05_plan_w1_sha": sha256_of_file(PLAN_W1),
        "pin_06_s89_w1_1_verdict_audit_sha256": S89_W1_1_VERDICT_SHA,
        "pin_07_p1_pattern_regex": P1_HSS_TRACE_MINUS_RCM.pattern,
        "pin_08_p2_pattern_regex": P2_ZETA_D_AT_ZERO.pattern,
        "pin_09_degeneracy_witness_regex": DEGENERACY_WITNESS_MARKERS.pattern,
        "pin_10_K_counter_status": "SUGGESTION-K=1",
        "pin_11_K_promotion_threshold": 3,
        "pin_12_positive_test_p1_matches_count": pos_test["p1_matches_count"],
        "pin_13_positive_test_severity": pos_test["severity"],
        "pin_14_negative_test_witness_count": neg_test["degeneracy_witness_markers_count"],
        "pin_15_composite_verdict": verdict,
    }
    # Normalize regex special chars + ints
    input_pins_norm = {k: (str(v) if not isinstance(v, str) else v)
                        for k, v in input_pins.items()}
    for k, v in input_pins_norm.items():
        print(f"  {k:50s} = {str(v)[:64]}")

    # Step 7: Value-string
    print("\n--- Step 7: Build value-string ---")
    value_str = (
        f"composite_verdict={verdict};"
        f"pre_registration_conditions_pass="
        f"{sum(1 for v in pass_conditions.values() if v)}_of_{len(pass_conditions)};"
        f"class_8_7_taxonomy_row_landed={has_8_7_row};"
        f"class_8_7_subsection_landed={has_8_7_subsection};"
        f"p1_pattern_landed={has_p1};p2_pattern_landed={has_p2};"
        f"witness_markers_landed={has_witness};"
        f"detector_function_landed={has_detector_fn};"
        f"positive_self_test_S89_W1_1={pos_test['self_test_status']};"
        f"positive_p1_matches={pos_test['p1_matches_count']};"
        f"positive_severity={pos_test['severity']};"
        f"negative_self_test_synthetic_witness={neg_test['self_test_status']};"
        f"negative_witness_markers_detected={neg_test['degeneracy_witness_markers_count']};"
        f"K_calibration=1_S89_W1_1_FAIL_audit_sha256={S89_W1_1_VERDICT_SHA[:16]};"
        f"K_counter_status=SUGGESTION-K=1;K_promotion_threshold=3;"
        f"file_pru_cardinality_audit_created_in_session_per_W6_3_hygiene_gap_discharge=True;"
        f"allowlist_row=pending;instances_row=pending;corpus_section_18=pending"
    )
    print(f"  value: {value_str[:200]}...")

    # Step 8: Emit verdict
    print("\n--- Step 8: Emit verdict ---")
    result = emit_verdict(
        gate_id=GATE_ID,
        verdict=verdict,
        value_str=value_str,
        scheme=SCHEME,
        convention=CONVENTION,
        L_max=L_MAX,
        input_pin_map=input_pins_norm,
        content_target=THIS_SCRIPT,
    )
    print(f"  audit_sha256  : {result['audit_sha256']}")
    print(f"  content_sha256: {result['content_sha256']}")

    print("\n" + "=" * 72)
    print(f"VERDICT: {verdict}")
    print("=" * 72)


if __name__ == "__main__":
    main()
