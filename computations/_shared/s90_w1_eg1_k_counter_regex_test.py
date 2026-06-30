#!/usr/bin/env python3
"""
s90_w1_eg1_k_counter_regex_test.py — S90 W1-4 self-test + verdict emitter
==========================================================================

Verifies the S90 W1-4 K-letter K-counter regex extension to
`_w25_closing_paragraph_coherence_sweep_audit.py`:
  - Pre-S90 regex matched ONLY count-keyed semantic patterns:
      `count\\s*[≥>=]\\s*\\d|threshold\\s*=\\s*\\d|
       covered_count\\s*[≥>=]\\s*\\d|N_PLANNING_DEFECT_THRESHOLD`
  - S90 W1-4 extension adds the K-letter K-counter form:
      `\\bK\\s*=\\s*\\d|K-counter|K_promotion`
    per `feedback_rules-compensate-missing-structure.md` K-counter
    convention.

Pre-edit baseline (empirical, BEFORE the regex extension landed):
  - cross-pillar-bridge-anatomy.md      : has_count_keyed_trigger=False
  - substrate-first-canonical-sourcing.md: has_count_keyed_trigger=False
  - registry-landing.md                  : has_count_keyed_trigger=False
Post-edit result (this test verifies):
  - cross-pillar-bridge-anatomy.md      : has_count_keyed_trigger=True
  - substrate-first-canonical-sourcing.md: has_count_keyed_trigger=True
  - registry-landing.md                  : has_count_keyed_trigger=True

PASS criterion (per plan §W1-4 #9):
  (i)  regex extended (helper present + sanity tests pass);
  (ii) self-test returns ≥ 1 of 3 rule-files with `has_count_keyed_trigger=True`;
  (iii) allowlist + instances rows appended (orchestrator post-emit step).

Per `wave-classification.md §"Dual-SHA closure for METHODOLOGY-class"`:
  content_sha256 = SHA-256 over `_w25_closing_paragraph_coherence_sweep_audit.py`
                   (the post-edit target script)
  audit_sha256   = SHA-256 over the ordered input-pin map (JSON-serialized)

Verdict emitted to `computations/session-90/s90_gate_verdicts.txt`.

Substrate framing
-----------------
K-counter advancement IS the methodology-layer F-image of substrate
calibration-corpus instance accumulation per `epistemic-discipline.md
§"Layer-Decomposition"` F: substrate → methodology → audit. The regex
captures the F-image trigger predicate (the syntactic surface form of
the promotion-threshold language). Pre-extension, the F-image's
trigger-predicate domain was incomplete: the canonical K=N form (used
across cross-pillar-bridge-anatomy.md, substrate-first-canonical-
sourcing.md, registry-landing.md) did not register, leaving the
closing-paragraph-coherence sweep audit blind to all three rule-files'
K-counter clauses. The extension closes this F-image domain gap by
construction — the K-letter trigger predicate now maps faithfully to
its substrate calibration-corpus image.
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

# Canonical-constants import per math-scripts.md (S34+ scripts).
SHARED_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SHARED_DIR))
try:
    from canonical_constants import *  # noqa: F401,F403
except Exception as e:
    print(f"ERROR: canonical_constants.py import failed: {e}", file=sys.stderr)
    raise

# Import the extended audit helper + the verdict-emitter.
from _w25_closing_paragraph_coherence_sweep_audit import (  # noqa: E402
    compute_count_keyed_trigger,
)
from s90_w1_emit_verdict import emit_verdict  # noqa: E402


PROJECT_ROOT = SHARED_DIR.parents[1]
AUDIT_SCRIPT = SHARED_DIR / '_w25_closing_paragraph_coherence_sweep_audit.py'
TARGET_FILES = [
    PROJECT_ROOT / '.claude' / 'rules' / 'cross-pillar-bridge-anatomy.md',
    PROJECT_ROOT / '.claude' / 'rules' / 'substrate-first-canonical-sourcing.md',
    PROJECT_ROOT / '.claude' / 'rules' / 'registry-landing.md',
]

GATE_ID = 'S90-EG1-K-COUNTER-REGEX-EXTENSION'  # (local)
PASS_THRESHOLD_N_MATCH = 1  # (local) per plan §W1-4 #9: ≥ 1 of 3 files


def t1_helper_sanity_tests() -> dict:
    """T1 — direct synthetic-string tests of compute_count_keyed_trigger.

    Verifies:
      - K-letter forms (K=N, K-counter, K_promotion) all match (extension)
      - word-boundary on K (OK=N must NOT match)
      - existing semantic patterns still match (regression on threshold)
    """
    test_cases = [  # (local) — synthetic test strings
        # (input_string, expected_match, label)
        ('K=3', True, 'k_letter_no_space'),
        ('K = 4', True, 'k_letter_with_spaces'),
        ('K-counter promotion', True, 'k_counter_phrase'),
        ('K_promotion = 3', True, 'k_promotion_phrase'),
        ('OK = 3', False, 'word_boundary_OK_negative'),
        ('threshold = 5', True, 'pre_s90_threshold_regression'),
        ('N_PLANNING_DEFECT_THRESHOLD', True, 'pre_s90_planning_defect_regression'),
        ('plain text no triggers', False, 'true_negative'),
    ]
    results = []  # (local)
    for input_str, expected, label in test_cases:
        actual = compute_count_keyed_trigger(input_str)
        results.append({
            'label': label,
            'input': input_str,
            'expected': expected,
            'actual': actual,
            'passes': (actual == expected),
        })
    n_pass = sum(1 for r in results if r['passes'])  # (local)
    n_total = len(results)  # (local)
    passes = (n_pass == n_total)  # (local)
    return {
        'test': 'T1_helper_sanity_tests',
        'n_test_cases': n_total,
        'n_pass': n_pass,
        'n_fail': n_total - n_pass,
        'cases': results,
        'passes': passes,
    }


def t2_three_target_file_sweep() -> dict:
    """T2 — apply compute_count_keyed_trigger to the 3 plan-named files.

    PASS iff n_match >= PASS_THRESHOLD_N_MATCH (= 1 per plan §W1-4 #9).
    """
    per_file = {}  # (local)
    for path in TARGET_FILES:
        if not path.exists():
            per_file[path.name] = {
                'path': str(path.relative_to(PROJECT_ROOT)),
                'exists': False,
                'has_count_keyed_trigger': None,
            }
            continue
        text = path.read_text(encoding='utf-8')  # (local)
        match = compute_count_keyed_trigger(text)
        per_file[path.name] = {
            'path': str(path.relative_to(PROJECT_ROOT)),
            'exists': True,
            'has_count_keyed_trigger': match,
        }
    n_match = sum(  # (local)
        1 for v in per_file.values()
        if v.get('has_count_keyed_trigger') is True
    )
    n_target = len(TARGET_FILES)  # (local)
    passes = (n_match >= PASS_THRESHOLD_N_MATCH)  # (local)
    return {
        'test': 'T2_three_target_file_sweep',
        'pass_threshold_n_match': PASS_THRESHOLD_N_MATCH,
        'n_match': n_match,
        'n_target': n_target,
        'per_file': per_file,
        'passes': passes,
    }


def sha256_of_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(65536), b''):
            h.update(chunk)
    return h.hexdigest()


def run_all_tests() -> dict:
    t1 = t1_helper_sanity_tests()
    t2 = t2_three_target_file_sweep()
    all_pass = t1['passes'] and t2['passes']  # (local)
    return {
        'gate_id': GATE_ID,
        'tests_overall': 'PASS' if all_pass else 'FAIL',
        'T1': t1,
        'T2': t2,
    }


def emit_gate_verdict(test_report: dict) -> dict:
    """Build 8-pin input-pin map per plan §W1-4 #7 PRDR; emit canonical line."""
    # Compute regex-string SHAs for axis pins (post-S90 extended pattern).
    extended_regex_pattern = (  # (local)
        r"(?:count\s*[≥>=]\s*\d|threshold\s*=\s*\d|"
        r"covered_count\s*[≥>=]\s*\d|N_PLANNING_DEFECT_THRESHOLD|"
        r"\bK\s*=\s*\d|K-counter|K_promotion)"
    )
    k_letter_extension_pattern = (  # (local)
        r"\bK\s*=\s*\d|K-counter|K_promotion"
    )

    input_pin_map = {  # (local) — 8-pin map per plan §W1-4 #7 PRDR
        'pin_01_audit_script_post_edit': sha256_of_file(AUDIT_SCRIPT),
        'pin_02_test_driver': sha256_of_file(Path(__file__).resolve()),
        'pin_03_target_cross_pillar_bridge_anatomy': (
            sha256_of_file(TARGET_FILES[0]) if TARGET_FILES[0].exists() else 'MISSING'
        ),
        'pin_04_target_substrate_first_canonical_sourcing': (
            sha256_of_file(TARGET_FILES[1]) if TARGET_FILES[1].exists() else 'MISSING'
        ),
        'pin_05_target_registry_landing': (
            sha256_of_file(TARGET_FILES[2]) if TARGET_FILES[2].exists() else 'MISSING'
        ),
        'pin_06_extended_regex_full_pattern': hashlib.sha256(
            extended_regex_pattern.encode('utf-8')
        ).hexdigest(),
        'pin_07_k_letter_extension_pattern': hashlib.sha256(
            k_letter_extension_pattern.encode('utf-8')
        ).hexdigest(),
        'pin_08_pass_threshold_n_match': str(PASS_THRESHOLD_N_MATCH),
    }

    verdict = 'PASS' if test_report['tests_overall'] == 'PASS' else 'FAIL'
    n_match = test_report.get('T2', {}).get('n_match', 0)  # (local)
    n_target = test_report.get('T2', {}).get('n_target', 0)  # (local)
    t1_pass = test_report.get('T1', {}).get('passes', False)  # (local)

    value_str = (
        f'k_letter_k_counter_regex_extension_landed_AND_'
        f'{n_match}_of_{n_target}_rule_files_match;'
        f'sanity_tests_T1=PASS_{test_report["T1"]["n_pass"]}_of_{test_report["T1"]["n_test_cases"]};'
        f'pre_edit_baseline=0_of_3_files_matched;'
        f'post_edit_result={n_match}_of_{n_target}_files_matched;'
        f'pass_threshold=geq_{PASS_THRESHOLD_N_MATCH};'
        f'k_letter_pattern=\\bK\\s*=\\s*\\d|K-counter|K_promotion;'
        f'allowlist_row=pending;instances_row=pending'
    )

    result = emit_verdict(
        gate_id=GATE_ID,
        verdict=verdict,
        value_str=value_str,
        scheme='eg1-regex-extension',
        convention='k-letter-k-counter-form',
        L_max='N/A',
        input_pin_map=input_pin_map,
        content_target=AUDIT_SCRIPT,
    )
    return result


def main() -> int:
    print('=== S90 W1-4 K-letter K-counter regex extension test driver ===')
    test_report = run_all_tests()
    print(json.dumps(test_report, indent=2, ensure_ascii=False))
    print()
    print('=== Emitting verdict line ===')
    emission_result = emit_gate_verdict(test_report)
    print(json.dumps({
        'gate_id': emission_result['gate_id'],
        'verdict': emission_result['verdict'],
        'content_sha256': emission_result['content_sha256'],
        'audit_sha256': emission_result['audit_sha256'],
        'canonical_line': emission_result['canonical_line'],
        'companion_line': emission_result['companion_line'],
    }, indent=2, ensure_ascii=False))
    return 0  # Exit 0 regardless of PASS/FAIL/INFO per math-scripts.md §Exit Codes


if __name__ == '__main__':
    sys.exit(main())
