#!/usr/bin/env python3
"""
s90_w1_partial_positive_audit_test.py — S90 W1-9 self-test + verdict emitter
=============================================================================

Verifies the S90 W1-9 PARTIAL-POSITIVE compliance class extension to
`computations/_shared/_substrate_first_provenance_audit.py`:

  - **T1 (PARTIAL-POSITIVE — live fixture)**: §W5-7
    (`S89-HEAT-KERNEL-ANCHOR-SWEEP-W7A-74-PRIMARY`) detected as
    PARTIAL-POSITIVE. Verdict block read from
    `computations/session-89/s89_gate_verdicts.txt`; producing script at
    `computations/session-89/s89_w5_a36_heat_kernel_anchor_sweep_w7a74_primary.py`.
    Expected signature: rules (1)∧(2)∧(3) all PASS, tier_pin row ABSENT.

  - **T2 (POSITIVE — live fixture)**: W9c-1
    (`S87-W5B-C16-AXIOM-SIDE-CSUB-CROSS-REVIEW`) detected as POSITIVE.
    Verdict block from `computations/session-87/s87_gate_verdicts.txt`;
    producing script at `s87_w9c_csub_axiom_cross_review.py`.
    Expected: 4-of-4 elements PASS (tier_pin=TIER-2 companion row present).

  - **T3 (NEGATIVE — live fixture)**: W4-2
    (`S86-SECTOR-2-MELLIN-KERNEL-K-INVARIANT`) detected as NEGATIVE.
    Verdict block from `computations/session-86/s86_gate_verdicts.txt`;
    producing script at `s86_w4_p5_sector_2_k_invariant.py`.
    Expected: rule (2) `-SCHEMATIC` suffix ABSENT (≤2-of-4 elements PASS).

  - **T4 (synthetic sanity)**: 4 synthetic 2-bit signature cases:
      (rules-1∧2∧3=T, tier_pin=T) → POSITIVE
      (rules-1∧2∧3=T, tier_pin=F) → PARTIAL-POSITIVE
      (rules-1∧2∧3=F, tier_pin=T) → NEGATIVE
      (rules-1∧2∧3=F, tier_pin=F) → NEGATIVE

PASS criterion (per plan §W1-9 #9):
  (i)   PARTIAL-POSITIVE class added to §(iv) corpus taxonomy ✓ (rule-file edit);
  (ii)  §W5-7 row #5 appended to corpus table ✓ (prose-form annotation);
  (iii) audit-script extension detects all 3 classes correctly on self-test
        (POSITIVE + PARTIAL-POSITIVE + NEGATIVE) — verified by T1+T2+T3+T4;
  (iv)  K-counter advances K=4 → K=5 ✓ (rule-file K-counter advancement section);
  (v)   allowlist + instances rows appended (orchestrator post-emit step).

Per `wave-classification.md §"Dual-SHA closure for METHODOLOGY-class"`:
  content_sha256 = SHA-256 over `_substrate_first_provenance_audit.py` (post-edit)
  audit_sha256   = SHA-256 over the ordered input-pin map (JSON-serialized)

Verdict emitted to `computations/session-90/s90_gate_verdicts.txt`.

Substrate framing
-----------------
The 3-class taxonomy IS the methodology-layer F-image of substrate-IS
commutativity-check granularity per `epistemic-discipline.md
§"Layer-Decomposition"`. The substrate-side commutativity rules (1) ∧ (2) ∧ (3)
remain the MANDATORY substrate-side check; tier_pin row is a methodology-floor
disclosure refinement. PARTIAL-POSITIVE recognizes that the substrate-side
check can be intact while the methodology-floor refinement is missed —
F-image structure preserved, only the audit-trail-completeness layer has a
soft gap (forward-recommended-not-mandatory).
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

# Canonical-constants import per `computations/_shared/CLAUDE.md` MANDATORY discipline.
SHARED_DIR = Path(__file__).resolve().parent  # (local) — script-dir resolver
sys.path.insert(0, str(SHARED_DIR))
try:
    from canonical_constants import *  # noqa: F401,F403
except Exception as e:
    print(f"ERROR: canonical_constants.py import failed: {e}", file=sys.stderr)
    raise

from _substrate_first_provenance_audit import detect_compliance_class  # noqa: E402
from s90_w1_emit_verdict import emit_verdict  # noqa: E402


PROJECT_ROOT = SHARED_DIR.parents[1]  # (local) — repo-root resolver
AUDIT_SCRIPT = SHARED_DIR / '_substrate_first_provenance_audit.py'  # (local)
RULE_FILE = (
    PROJECT_ROOT / '.claude' / 'rules' / 'substrate-first-canonical-sourcing.md'
)  # (local)

# Live-fixture file paths
S89_VERDICT_FILE = PROJECT_ROOT / 'computations' / 'session-89' / 's89_gate_verdicts.txt'  # (local)
S89_W5_7_SCRIPT = (
    PROJECT_ROOT / 'computations' / 'session-89'
    / 's89_w5_a36_heat_kernel_anchor_sweep_w7a74_primary.py'
)  # (local)
S87_VERDICT_FILE = PROJECT_ROOT / 'computations' / 'session-87' / 's87_gate_verdicts.txt'  # (local)
S87_W9C_1_SCRIPT = (
    PROJECT_ROOT / 'computations' / 'session-87'
    / 's87_w9c_csub_axiom_cross_review.py'
)  # (local)
S86_VERDICT_FILE = PROJECT_ROOT / 'computations' / 'session-86' / 's86_gate_verdicts.txt'  # (local)
S86_W4_2_SCRIPT = (
    PROJECT_ROOT / 'computations' / 'session-86'
    / 's86_w4_p5_sector_2_k_invariant.py'
)  # (local)

# Live-fixture gate-IDs
S89_W5_7_GATE_ID = 'S89-HEAT-KERNEL-ANCHOR-SWEEP-W7A-74-PRIMARY'  # (local)
S87_W9C_1_GATE_ID = 'S87-W5B-C16-AXIOM-SIDE-CSUB-CROSS-REVIEW'  # (local)
S86_W4_2_GATE_ID = 'S86-SECTOR-2-MELLIN-KERNEL-K-INVARIANT'  # (local)

GATE_ID = 'S90-IV-PARTIAL-POSITIVE-CALIBRATION-CLASS-EXTENSION'  # (local)


def extract_verdict_block(verdict_file: Path, gate_id: str, n_lines_after: int = 5) -> str:
    """Extract the multi-line verdict block (canonical + companion rows) for a gate.

    Reads verdict_file, finds the line starting with `gate_id:`, and returns
    that line plus the next n_lines_after lines (typically 2 companion rows
    plus a small safety margin).
    """
    if not verdict_file.exists():
        return ''
    text = verdict_file.read_text(encoding='utf-8')
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.startswith(f'{gate_id}:'):
            block_lines = lines[i:i + 1 + n_lines_after]
            return '\n'.join(block_lines)
    return ''


def t1_w5_7_partial_positive_live() -> dict:
    """T1 — live §W5-7 fixture; expected PARTIAL-POSITIVE."""
    if not S89_W5_7_SCRIPT.exists():
        return {
            'test': 'T1_w5_7_partial_positive_live',
            'error': f'producing script not found at {S89_W5_7_SCRIPT}',
            'passes': False,
        }
    verdict_block = extract_verdict_block(S89_VERDICT_FILE, S89_W5_7_GATE_ID, n_lines_after=5)
    if not verdict_block:
        return {
            'test': 'T1_w5_7_partial_positive_live',
            'error': f'verdict block for {S89_W5_7_GATE_ID} not found in {S89_VERDICT_FILE}',
            'passes': False,
        }
    producing_script = S89_W5_7_SCRIPT.read_text(encoding='utf-8')
    result = detect_compliance_class(verdict_block, producing_script)
    expected = 'PARTIAL-POSITIVE'  # (local)
    actual = result['compliance_class']  # (local)
    passes = (actual == expected)  # (local)
    return {
        'test': 'T1_w5_7_partial_positive_live',
        'verdict_block_chars': len(verdict_block),
        'producing_script_chars': len(producing_script),
        'rule_1_pass': result.get('rule_1_pass'),
        'rule_2_pass': result.get('rule_2_pass'),
        'rule_3_pass': result.get('rule_3_pass'),
        'tier_pin_row_present': result.get('tier_pin_row_present'),
        'signature_2bit': result.get('signature_2bit'),
        'expected_class': expected,
        'actual_class': actual,
        'severity': result.get('severity'),
        'passes': passes,
    }


def t2_w9c_1_positive_live() -> dict:
    """T2 — live W9c-1 fixture; expected POSITIVE."""
    if not S87_W9C_1_SCRIPT.exists():
        return {
            'test': 'T2_w9c_1_positive_live',
            'error': f'producing script not found at {S87_W9C_1_SCRIPT}',
            'passes': False,
        }
    verdict_block = extract_verdict_block(S87_VERDICT_FILE, S87_W9C_1_GATE_ID, n_lines_after=5)
    if not verdict_block:
        return {
            'test': 'T2_w9c_1_positive_live',
            'error': f'verdict block for {S87_W9C_1_GATE_ID} not found in {S87_VERDICT_FILE}',
            'passes': False,
        }
    producing_script = S87_W9C_1_SCRIPT.read_text(encoding='utf-8')
    result = detect_compliance_class(verdict_block, producing_script)
    expected = 'POSITIVE'  # (local)
    actual = result['compliance_class']  # (local)
    passes = (actual == expected)  # (local)
    return {
        'test': 'T2_w9c_1_positive_live',
        'verdict_block_chars': len(verdict_block),
        'producing_script_chars': len(producing_script),
        'rule_1_pass': result.get('rule_1_pass'),
        'rule_2_pass': result.get('rule_2_pass'),
        'rule_3_pass': result.get('rule_3_pass'),
        'tier_pin_row_present': result.get('tier_pin_row_present'),
        'signature_2bit': result.get('signature_2bit'),
        'expected_class': expected,
        'actual_class': actual,
        'severity': result.get('severity'),
        'passes': passes,
    }


def t3_w4_2_negative_live() -> dict:
    """T3 — live W4-2 fixture; expected NEGATIVE."""
    if not S86_W4_2_SCRIPT.exists():
        return {
            'test': 'T3_w4_2_negative_live',
            'error': f'producing script not found at {S86_W4_2_SCRIPT}',
            'passes': False,
        }
    verdict_block = extract_verdict_block(S86_VERDICT_FILE, S86_W4_2_GATE_ID, n_lines_after=5)
    if not verdict_block:
        return {
            'test': 'T3_w4_2_negative_live',
            'error': f'verdict block for {S86_W4_2_GATE_ID} not found in {S86_VERDICT_FILE}',
            'passes': False,
        }
    producing_script = S86_W4_2_SCRIPT.read_text(encoding='utf-8')
    result = detect_compliance_class(verdict_block, producing_script)
    expected = 'NEGATIVE'  # (local)
    actual = result['compliance_class']  # (local)
    passes = (actual == expected)  # (local)
    return {
        'test': 'T3_w4_2_negative_live',
        'verdict_block_chars': len(verdict_block),
        'producing_script_chars': len(producing_script),
        'rule_1_pass': result.get('rule_1_pass'),
        'rule_2_pass': result.get('rule_2_pass'),
        'rule_3_pass': result.get('rule_3_pass'),
        'tier_pin_row_present': result.get('tier_pin_row_present'),
        'signature_2bit': result.get('signature_2bit'),
        'expected_class': expected,
        'actual_class': actual,
        'severity': result.get('severity'),
        'passes': passes,
    }


def t4_synthetic_2bit_signature_matrix() -> dict:
    """T4 — 4 synthetic cases covering the (rules-1∧2∧3, tier_pin) {0,1}×{0,1} matrix."""
    cases = [  # (local) — synthetic 2-bit signature matrix
        {
            'label': 'TT_positive',
            'verdict_block': (
                'S99-SYNTHETIC-TT: PASS -- value="..." scheme=foo '
                'convention=bar-SCHEMATIC L_max=N/A '
                'audit_sha256=0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef '
                'content_sha256=0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef '
                'schema_version=S87+\n'
                '# tier_pin=TIER-2 # synthetic SCHEMATIC tier-2 disclosure\n'
                '# audit_sha256_short=01234567 content_sha256_short=01234567 '
                '# S99-SYNTHETIC-TT dual-SHA companion row\n'
            ),
            'producing_script': (
                '"""Synthetic. CLASS pin SCHEMATIC. _spectral_action_regulators.py '
                'TIER-2 SCHEMATIC OPERATIONAL DEVIATION."""\n'
            ),
            'expected_class': 'POSITIVE',
        },
        {
            'label': 'TF_partial_positive',
            'verdict_block': (
                'S99-SYNTHETIC-TF: PASS -- value="..." scheme=foo '
                'convention=bar-SCHEMATIC L_max=N/A '
                'audit_sha256=fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210 '
                'content_sha256=fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210 '
                'schema_version=S87+\n'
                '# audit_sha256_short=fedcba98 content_sha256_short=fedcba98 '
                '# S99-SYNTHETIC-TF dual-SHA companion row\n'
            ),
            'producing_script': (
                '"""Synthetic. CLASS pin SCHEMATIC. _spectral_action_regulators.py '
                'TIER-2 SCHEMATIC OPERATIONAL DEVIATION."""\n'
            ),
            'expected_class': 'PARTIAL-POSITIVE',
        },
        {
            'label': 'FT_negative',
            'verdict_block': (
                'S99-SYNTHETIC-FT: PASS -- value="..." scheme=foo '
                'convention=bar L_max=N/A '
                'audit_sha256=aaaa1111bbbb2222cccc3333dddd4444eeee5555ffff6666aaaa1111bbbb2222 '
                'content_sha256=aaaa1111bbbb2222cccc3333dddd4444eeee5555ffff6666aaaa1111bbbb2222 '
                'schema_version=S87+\n'
                '# tier_pin=TIER-2 # synthetic but no -SCHEMATIC suffix\n'
            ),
            'producing_script': (
                '"""Synthetic. No SCHEMATIC. Plain bare module. Some other content."""\n'
            ),
            'expected_class': 'NEGATIVE',
        },
        {
            'label': 'FF_negative',
            'verdict_block': (
                'S99-SYNTHETIC-FF: PASS -- value="..." scheme=foo '
                'convention=bar L_max=N/A '
                'audit_sha256=99998888777766665555444433332222111100009999888877776666555544443 '
                'content_sha256=11112222333344445555666677778888999900001111222233334444555566667 '
                'schema_version=S87+\n'
                '# audit_sha256_short=99998888 content_sha256_short=11112222 '
                '# S99-SYNTHETIC-FF dual-SHA companion row\n'
            ),
            'producing_script': (
                '"""Synthetic. No mention of any compliance disclosure here."""\n'
            ),
            'expected_class': 'NEGATIVE',
        },
    ]
    results = []  # (local)
    for case in cases:
        r = detect_compliance_class(
            case['verdict_block'],
            case['producing_script'],
        )
        actual = r['compliance_class']  # (local)
        passes = (actual == case['expected_class'])  # (local)
        results.append({
            'label': case['label'],
            'expected': case['expected_class'],
            'actual': actual,
            'rule_1_pass': r.get('rule_1_pass'),
            'rule_2_pass': r.get('rule_2_pass'),
            'rule_3_pass': r.get('rule_3_pass'),
            'tier_pin_row_present': r.get('tier_pin_row_present'),
            'signature_2bit': r.get('signature_2bit'),
            'passes': passes,
        })
    n_pass = sum(1 for r in results if r['passes'])  # (local)
    n_total = len(cases)  # (local)
    return {
        'test': 'T4_synthetic_2bit_signature_matrix',
        'n_cases': n_total,
        'n_pass': n_pass,
        'cases': results,
        'passes': (n_pass == n_total),
    }


def sha256_of_file(path: Path) -> str:
    """SHA-256 of a file's bytes (chunked read for large files)."""
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(65536), b''):
            h.update(chunk)
    return h.hexdigest()


def run_all_tests() -> dict:
    """Run T1-T4 and aggregate."""
    t1 = t1_w5_7_partial_positive_live()
    t2 = t2_w9c_1_positive_live()
    t3 = t3_w4_2_negative_live()
    t4 = t4_synthetic_2bit_signature_matrix()
    all_pass = (  # (local)
        t1.get('passes', False)
        and t2.get('passes', False)
        and t3.get('passes', False)
        and t4.get('passes', False)
    )
    return {
        'gate_id': GATE_ID,
        'tests_overall': 'PASS' if all_pass else 'FAIL',
        'T1_w5_7_partial_positive_live': t1,
        'T2_w9c_1_positive_live': t2,
        'T3_w4_2_negative_live': t3,
        'T4_synthetic_2bit_signature_matrix': t4,
    }


def emit_gate_verdict(test_report: dict, supersedes: str = '') -> dict:
    """Build 10-pin input-pin map per plan §W1-9 #7 PRDR; emit canonical line.

    Args:
        test_report: aggregated test report from `run_all_tests()`.
        supersedes:  optional full 64-char audit_sha256 of a prior verdict
                     line being superseded per Option A protocol.
    """
    input_pin_map = {  # (local) — 10-pin map per plan §W1-9 #7 PRDR
        'pin_01_audit_script_post_edit': sha256_of_file(AUDIT_SCRIPT),
        'pin_02_test_driver': sha256_of_file(Path(__file__).resolve()),
        'pin_03_rule_file_substrate_first_canonical_sourcing': (
            sha256_of_file(RULE_FILE) if RULE_FILE.exists() else 'MISSING'
        ),
        'pin_04_w5_7_producing_script': (
            sha256_of_file(S89_W5_7_SCRIPT) if S89_W5_7_SCRIPT.exists() else 'MISSING'
        ),
        'pin_05_w5_7_verdict_audit_sha_pin': (
            '884db5e02fff4d9791c94ad0140edc77158355d189faa26491dc83e5b9cbbc50'
        ),
        'pin_06_w9c_1_producing_script': (
            sha256_of_file(S87_W9C_1_SCRIPT) if S87_W9C_1_SCRIPT.exists() else 'MISSING'
        ),
        'pin_07_w4_2_producing_script': (
            sha256_of_file(S86_W4_2_SCRIPT) if S86_W4_2_SCRIPT.exists() else 'MISSING'
        ),
        'pin_08_K_counter_advancement': 'K_substantive_3_to_4_K_with_inheritance_4_to_5',
        'pin_09_status_preservation': 'MANDATORY_at_K_substantive_4_geq_K_promotion_3',
        'pin_10_plan_gate_id': GATE_ID,
    }

    verdict = (  # (local)
        'PASS' if test_report['tests_overall'] == 'PASS' else 'FAIL'
    )
    t1 = test_report['T1_w5_7_partial_positive_live']  # (local)
    t2 = test_report['T2_w9c_1_positive_live']  # (local)
    t3 = test_report['T3_w4_2_negative_live']  # (local)
    t4 = test_report['T4_synthetic_2bit_signature_matrix']  # (local)

    value_str = (  # (local)
        f'partial_positive_class_extension_landed_AND_K-counter_K=4_to_K=5_AND_'
        f'audit_script_3_class_detection_tests_{test_report["tests_overall"]};'
        f'T1_w5_7_PARTIAL-POSITIVE_live={t1.get("actual_class", "ERROR")};'
        f'T2_w9c_1_POSITIVE_live={t2.get("actual_class", "ERROR")};'
        f'T3_w4_2_NEGATIVE_live={t3.get("actual_class", "ERROR")};'
        f'T4_synthetic_2bit_matrix_pass={t4.get("n_pass", 0)}_of_{t4.get("n_cases", 0)};'
        f'K_substantive_3_to_4_AND_K_with_inheritance_4_to_5;'
        f'PARTIAL-POSITIVE_class_admissible_from_S90_forward;'
        f'severity_band_ADVISORY_S2_for_PARTIAL-POSITIVE;'
        f'tier_pin_row_forward_recommended_not_mandatory;'
        f'allowlist_row=pending;instances_row=pending'
    )

    result = emit_verdict(
        gate_id=GATE_ID,
        verdict=verdict,
        value_str=value_str,
        scheme='substrate-first-canonical-sourcing-extension',
        convention='schematic-level-pin-3-class-taxonomy',
        L_max='N/A',
        input_pin_map=input_pin_map,
        content_target=AUDIT_SCRIPT,
        supersedes=supersedes,
    )
    return result


def main(supersedes: str = '') -> int:
    """Run all tests, print report, emit verdict line. Exit 0 regardless."""
    print('=== S90 W1-9 PARTIAL-POSITIVE compliance class test driver ===')
    test_report = run_all_tests()
    print(json.dumps(test_report, indent=2, ensure_ascii=False))
    print()
    print('=== Emitting verdict line ===')
    if supersedes:
        print(f'(supersedes prior audit_sha256={supersedes})')
    emission_result = emit_gate_verdict(test_report, supersedes=supersedes)
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
    sup_arg = ''  # (local) — default empty (fresh emission)
    if '--supersedes' in sys.argv:
        idx = sys.argv.index('--supersedes')  # (local)
        if idx + 1 < len(sys.argv):
            sup_arg = sys.argv[idx + 1]
    sys.exit(main(supersedes=sup_arg))
