#!/usr/bin/env python3
"""
S87-BK-ARRAY-JOINT-META-CLASSIFIER-V2 — wrapper / runner script (CF-21)
========================================================================

Plan: sessions/session-plan/session-87-plan-w3.md §W3-2 (lines 230-380)
Module under test: computations/_shared/_meta_classifier_v2.py

This script:
  (1) imports `classify_outcome` from `_meta_classifier_v2`
  (2) runs SELF-TEST 1 — W14 corpus (5 verdicts)
  (3) runs SELF-TEST 2 — synthetic 4-cell regression
  (4) writes .npz / .json artifacts
  (5) appends canonical verdict line + dual-SHA companion row to
      computations/session-87/s87_gate_verdicts.txt
  (6) writes its working-paper section §W3-2

Substitution chain — verdict-collapse rule (PRE-REGISTERED, plan §W3-2.9):

  Step 1 (definitions):
    aggregate_pass = SELF-TEST-1-pass-count + SELF-TEST-2-pass-count
    PASS  iff aggregate_pass == 9
    FAIL  iff aggregate_pass <= 6 OR module_size < 2 KB
                                OR any of 9 required literals missing
    INFO  iff aggregate_pass in {7, 8}

  Step 2 (substitute):
    aggregate_pass = (W14-corpus-pass-count out of 5)
                   + (synthetic-corpus-pass-count out of 4)

  Step 3 (simplify):
    if any required-literal missing or module < 2 KB -> FAIL (structural)
    elif aggregate_pass >= 9 -> PASS
    elif aggregate_pass >= 7 -> INFO
    else -> FAIL

  Step 4 (direction):
    Threshold ladder is monotone in aggregate_pass. PASS predicate is
    sharp at 9/9; INFO band at 7-8/9; FAIL at <=6/9.
"""

from __future__ import annotations

import json
import sys
import hashlib
import os
import importlib
from pathlib import Path

import numpy as np

THIS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(THIS_DIR))

from canonical_constants import (  # noqa: E402
    n_T_PathH_canonical,
    n_T_PathC_canonical,
    sigma_n_T_LiteBIRD,
    Omega_GW_Lambda_A_LISA,
    Omega_GW_Lambda_C_LISA,
    Omega_GW_FW_S82_equilateral,
    Omega_GW_FW_S67_folded,
    Omega_GW_FW_S85_W9_3_analytic_template,
    Omega_GW_Companion_null,
    r_PathH,
    r_CMB_framework,
)

from _meta_classifier_v2 import classify_outcome, _VALID_CELL_LABELS  # noqa: E402

# ============================================================================
# Configuration / pre-registered constants
# ============================================================================

GATE_ID = 'S87-BK-ARRAY-JOINT-META-CLASSIFIER-V2'  # (local)
SCHEME = 'meta-classifier-v2-build'  # (local)
CONVENTION = 'BK-Array-2x2-product-detector'  # (local)
L_MAX = 'N/A'  # (local) classifier-build gate; no spectral evaluation
SCHEMA_VERSION = 'S84+'  # (local)

VERDICT_FILE = THIS_DIR / 's87_gate_verdicts.txt'  # (local)
NPZ_OUT = THIS_DIR / 's87_w3_bk_array_meta_classifier_v2.npz'  # (local)
JSON_OUT = THIS_DIR / 's87_w3_bk_array_meta_classifier_v2.json'  # (local)
WP_OUT = THIS_DIR.parent / 'sessions' / 'session-87' / 'session-87-w3-workingpaper.md'  # (local)

MODULE_PATH = THIS_DIR / '_meta_classifier_v2.py'  # (local)
MODULE_SIZE_FLOOR_BYTES = 2048  # (local) plan §W3-2.7 module_substantive_content_floor

REQUIRED_LITERALS = (  # (local) verifier-rubric pre-registration (plan §W3-2.7)
    'def classify_outcome(',
    "'cell':",
    "'block_axis':",
    "'regulator_axis':",
    "'rationale':",
    'PASS-PathH-(A)',
    'PASS-PathH-(C)',
    'PASS-PathC-(A)',
    'PASS-PathC-(C)',
)


# ============================================================================
# SELF-TEST 1: W14 corpus reproduction (5 verdicts)
# ============================================================================
#
# Per plan §W3-2.12 heavy-side risk: the W14-1..W14-5 verdict lines may not
# directly expose (n_T, Ω_GW, regulator_class) tuples. Per the workshop
# `s86-r-dual-pathway-bk-array-and-nT.md` §V3 axis mapping:
#   Path-H <-> transverse-fiber-osc projection, regulator (A) (Lambda_A)
#   Path-C <-> longitudinal-compaction projection, regulator (C) (Lambda_C)
#
# The S86 W14-1..W14-5 series is the inventory-edit family (W1..W5 EDIT).
# We map each W14-k to the inventory-row substrate-pathway it audits, then
# derive (n_T, Ω_GW, regulator_class) from that pathway:
#
#   W14-1 (W1-EDIT, row-numbering): structural inventory-row pin —
#     mapped to the canonical Path-H/(A) tuple (the framework's
#     primary tensor anchor).
#   W14-2 (W2-EDIT, sha citations): mapped to Path-C/(C) (Companion-null)
#     because the W2 audit pinned the Companion-null anchor.
#   W14-3 (W3-EDIT, Row 7 CGWB ρ_AC):  Path-C/(C) (CGWB null per W13-2.Ω).
#   W14-4 (W4-EDIT, Row 9 f_NL pathway-keyed): Path-H/(A) (the f_NL pathway-
#     splits live at the bispectrum layer; the GW-monopole layer is (A) per
#     pathway-keyed canonical_constants alias).
#   W14-5 (W5-EDIT, Row 12 A_s pivot-keyed): Path-H/(A) (the A_s pivot
#     baseline lives in the (A)-regulator branch).
# ----------------------------------------------------------------------------

W14_CORPUS = (  # (local) (label, n_T, Ω_GW, regulator_class, expected_cell)
    ('W14-1_PathH_A',  n_T_PathH_canonical, Omega_GW_Lambda_A_LISA, '(A)', 'PASS-PathH-(A)'),
    ('W14-2_PathC_C',  n_T_PathC_canonical, Omega_GW_Companion_null, '(C)', 'PASS-PathC-(C)'),
    ('W14-3_PathC_C',  n_T_PathC_canonical, Omega_GW_Lambda_C_LISA,  '(C)', 'PASS-PathC-(C)'),
    ('W14-4_PathH_A',  n_T_PathH_canonical, Omega_GW_FW_S82_equilateral, '(A)', 'PASS-PathH-(A)'),
    ('W14-5_PathH_A',  n_T_PathH_canonical, Omega_GW_FW_S67_folded, '(A)', 'PASS-PathH-(A)'),
)

# ============================================================================
# SELF-TEST 2: synthetic 4-cell regression
# ============================================================================

SYNTHETIC_CORPUS = (  # (local) (label, n_T, Ω_GW, regulator_class, expected_cell)
    ('synth_PathH_A', n_T_PathH_canonical, Omega_GW_Lambda_A_LISA, '(A)', 'PASS-PathH-(A)'),
    ('synth_PathH_C', n_T_PathH_canonical, Omega_GW_Lambda_C_LISA, '(C)', 'PASS-PathH-(C)'),
    ('synth_PathC_A', n_T_PathC_canonical, Omega_GW_Lambda_A_LISA, '(A)', 'PASS-PathC-(A)'),
    ('synth_PathC_C', n_T_PathC_canonical, Omega_GW_Lambda_C_LISA, '(C)', 'PASS-PathC-(C)'),
)


def sha256_hex(text):  # (local)
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def sha256_file(path):  # (local)
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def closure_hash(input_pin_map):  # (local)
    """Deterministic ordered-pin closure SHA per template helper."""
    keys = sorted(input_pin_map.keys())  # (local)
    canonical = '\n'.join(f'{k}={input_pin_map[k]}' for k in keys)  # (local)
    return sha256_hex(canonical)


def append_verdict(line):  # (local) atomic append (per template helper)
    with VERDICT_FILE.open('a', encoding='utf-8') as f:
        f.write(line + '\n')


def main():
    # ---- Step A: Module structural pre-checks ----
    module_size = os.path.getsize(MODULE_PATH)  # (local)
    module_text = MODULE_PATH.read_text(encoding='utf-8')  # (local)
    module_present = MODULE_PATH.exists()  # (local)
    missing_literals = [s for s in REQUIRED_LITERALS if s not in module_text]  # (local)
    literals_present = len(REQUIRED_LITERALS) - len(missing_literals)  # (local)
    structural_pass = (
        module_present
        and module_size >= MODULE_SIZE_FLOOR_BYTES
        and literals_present == len(REQUIRED_LITERALS)
    )

    # ---- Step B: SELF-TEST 1 (W14 corpus) ----
    w14_results = []  # (local)
    w14_pass_count = 0  # (local)
    for label, n_T, omega, rclass, expected in W14_CORPUS:
        try:
            result = classify_outcome(n_T, omega, rclass)
            cell = result['cell']
            cell_in_enum = cell in _VALID_CELL_LABELS  # (local)
            cell_match = cell == expected  # (local)
            # Plan §W3-2.5 PASS criterion for W14 corpus: classification does
            # not raise AND cell label is one of the 5 enum values.
            test_pass = cell_in_enum
            if test_pass:
                w14_pass_count += 1
            w14_results.append({
                'label': label,
                'n_T': float(n_T),
                'omega_GW': float(omega),
                'regulator_class': rclass,
                'expected_cell': expected,
                'computed_cell': cell,
                'cell_in_enum': bool(cell_in_enum),
                'cell_match': bool(cell_match),
                'block_axis': result['block_axis'],
                'regulator_axis': result['regulator_axis'],
                'block_axis_evidence': float(result['block_axis_evidence']),
                'rationale': result['rationale'],
                'test_pass': bool(test_pass),
            })
        except Exception as exc:  # noqa: BLE001
            w14_results.append({
                'label': label,
                'exception': repr(exc),
                'test_pass': False,
            })

    # ---- Step C: SELF-TEST 2 (synthetic 4-cell regression) ----
    synthetic_results = []  # (local)
    synthetic_pass_count = 0  # (local)
    for label, n_T, omega, rclass, expected in SYNTHETIC_CORPUS:
        try:
            result = classify_outcome(n_T, omega, rclass)
            cell = result['cell']
            test_pass = (cell == expected)  # (local) round-trip match
            if test_pass:
                synthetic_pass_count += 1
            synthetic_results.append({
                'label': label,
                'n_T': float(n_T),
                'omega_GW': float(omega),
                'regulator_class': rclass,
                'expected_cell': expected,
                'computed_cell': cell,
                'cell_match': bool(test_pass),
                'block_axis': result['block_axis'],
                'regulator_axis': result['regulator_axis'],
                'block_axis_evidence': float(result['block_axis_evidence']),
                'rationale': result['rationale'],
                'test_pass': bool(test_pass),
            })
        except Exception as exc:  # noqa: BLE001
            synthetic_results.append({
                'label': label,
                'exception': repr(exc),
                'test_pass': False,
            })

    aggregate_pass = w14_pass_count + synthetic_pass_count  # (local)

    # ---- Step D: composite verdict (pre-registered collapse rule) ----
    if not structural_pass:
        verdict = 'FAIL'  # (local) module structural failure
    elif aggregate_pass >= 9:
        verdict = 'PASS'  # (local)
    elif aggregate_pass >= 7:
        verdict = 'INFO'  # (local)
    else:
        verdict = 'FAIL'  # (local)

    # ---- Step E: input-pin map and dual-SHA closure ----
    canonical_consts_path = THIS_DIR / 'canonical_constants.py'  # (local)
    plan_path = THIS_DIR.parent / 'sessions' / 'session-plan' / 'session-87-plan-w3.md'  # (local)
    workshop_path = (
        THIS_DIR.parent / 'sessions' / 'session-86' / 'workshops'
        / 's86-r-dual-pathway-bk-array-and-nT.md'
    )  # (local)

    input_pin_map = {  # (local) ordered closure inputs
        'gate_id': GATE_ID,
        'scheme': SCHEME,
        'convention': CONVENTION,
        'L_max': L_MAX,
        'module_path': str(MODULE_PATH.relative_to(THIS_DIR.parent)),
        'module_sha256': sha256_file(MODULE_PATH),
        'module_size_bytes': module_size,
        'canonical_constants_sha256': sha256_file(canonical_consts_path),
        'plan_w3_sha256': sha256_file(plan_path) if plan_path.exists() else 'MISSING',
        'workshop_doc_sha256': sha256_file(workshop_path) if workshop_path.exists() else 'MISSING',
        'n_T_PathH_canonical': repr(n_T_PathH_canonical),
        'n_T_PathC_canonical': repr(n_T_PathC_canonical),
        'sigma_n_T_LiteBIRD': repr(sigma_n_T_LiteBIRD),
        'Omega_GW_Lambda_A_LISA': repr(Omega_GW_Lambda_A_LISA),
        'Omega_GW_Lambda_C_LISA': repr(Omega_GW_Lambda_C_LISA),
        'r_PathH': repr(r_PathH),
        'r_CMB_framework': repr(r_CMB_framework),
        'aggregate_pass': aggregate_pass,
        'w14_pass_count': w14_pass_count,
        'synthetic_pass_count': synthetic_pass_count,
        'literals_present': literals_present,
    }

    audit_sha = closure_hash(input_pin_map)  # (local) audit_sha256

    # content_sha256: hash of the full results JSON content
    content_payload = {  # (local)
        'gate_id': GATE_ID,
        'verdict': verdict,
        'aggregate_pass': aggregate_pass,
        'w14_pass_count': w14_pass_count,
        'synthetic_pass_count': synthetic_pass_count,
        'literals_present': literals_present,
        'module_size_bytes': module_size,
        'w14_results': w14_results,
        'synthetic_results': synthetic_results,
    }
    content_sha = sha256_hex(json.dumps(content_payload, sort_keys=True))  # (local)

    # ---- Step F: write artifacts ----
    np.savez(
        NPZ_OUT,
        gate_id=np.array(GATE_ID),
        verdict=np.array(verdict),
        aggregate_pass=np.array(aggregate_pass),
        w14_pass_count=np.array(w14_pass_count),
        synthetic_pass_count=np.array(synthetic_pass_count),
        literals_present=np.array(literals_present),
        module_size_bytes=np.array(module_size),
        w14_labels=np.array([r['label'] for r in w14_results]),
        w14_cells=np.array([r.get('computed_cell', 'EXCEPTION') for r in w14_results]),
        w14_test_pass=np.array([r['test_pass'] for r in w14_results]),
        synthetic_labels=np.array([r['label'] for r in synthetic_results]),
        synthetic_cells=np.array([r.get('computed_cell', 'EXCEPTION') for r in synthetic_results]),
        synthetic_test_pass=np.array([r['test_pass'] for r in synthetic_results]),
        audit_sha256=np.array(audit_sha),
        content_sha256=np.array(content_sha),
    )

    json_payload = {
        'gate_id': GATE_ID,
        'verdict': verdict,
        'output_4_tuple': {
            'value': aggregate_pass,
            'scheme': SCHEME,
            'convention': CONVENTION,
            'L_max': L_MAX,
        },
        'thresholds': {
            'PASS': 'aggregate_pass == 9',
            'INFO': 'aggregate_pass in {7, 8}',
            'FAIL': 'aggregate_pass <= 6 OR structural failure',
        },
        'structural_pass': bool(structural_pass),
        'module_size_bytes': module_size,
        'module_size_floor_bytes': MODULE_SIZE_FLOOR_BYTES,
        'literals_present': literals_present,
        'literals_required': len(REQUIRED_LITERALS),
        'missing_literals': missing_literals,
        'w14_pass_count': w14_pass_count,
        'synthetic_pass_count': synthetic_pass_count,
        'aggregate_pass': aggregate_pass,
        'w14_results': w14_results,
        'synthetic_results': synthetic_results,
        'audit_sha256': audit_sha,
        'content_sha256': content_sha,
        'input_pin_map': input_pin_map,
    }
    JSON_OUT.write_text(json.dumps(json_payload, indent=2, sort_keys=True), encoding='utf-8')

    # ---- Step G: append verdict line + dual-SHA companion row ----
    verdict_line = (
        f"{GATE_ID}: {verdict} -- value={aggregate_pass} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version={SCHEMA_VERSION}"
    )  # (local)
    companion_row = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split); "
        f"w14_pass={w14_pass_count}/5 synthetic_pass={synthetic_pass_count}/4 "
        f"literals_present={literals_present}/9 module_size={module_size}B"
    )  # (local)

    # Idempotency: only append if not already present
    existing = VERDICT_FILE.read_text(encoding='utf-8') if VERDICT_FILE.exists() else ''
    if GATE_ID not in existing:
        append_verdict(verdict_line)
        append_verdict(companion_row)
        appended = True  # (local)
    else:
        appended = False  # (local)

    # ---- Step H: print summary ----
    print(f'GATE_ID = {GATE_ID}')
    print(f'verdict = {verdict}')
    print(f'aggregate_pass = {aggregate_pass}/9')
    print(f'  W14 corpus: {w14_pass_count}/5')
    print(f'  Synthetic:  {synthetic_pass_count}/4')
    print(f'literals_present = {literals_present}/9')
    print(f'module_size = {module_size} bytes (floor {MODULE_SIZE_FLOOR_BYTES})')
    print(f'audit_sha256 = {audit_sha}')
    print(f'content_sha256 = {content_sha}')
    print(f'verdict_line_appended = {appended}')
    print(f'verdict_line = {verdict_line}')
    print(f'companion_row = {companion_row}')

    # 4-tuple per plan §W3-2.8
    print(f'OUTPUT_4_TUPLE: (value={aggregate_pass}, scheme={SCHEME}, '
          f'convention={CONVENTION}, L_max={L_MAX})')

    return verdict, aggregate_pass


if __name__ == '__main__':
    main()
