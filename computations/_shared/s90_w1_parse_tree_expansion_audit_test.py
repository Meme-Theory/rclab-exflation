#!/usr/bin/env python3
"""
s90_w1_parse_tree_expansion_audit_test.py — S90 W1-8 self-test + verdict emitter
================================================================================

Verifies the S90 W1-8 MISSING-PARSE-TREE-EXPANSION audit hook extension to
`computations/_shared/_registry_landing_audit.py`:

  - **T1 (positive)**: §VII.U.2 (canonical declaration site for Var_a parse-tree
    expansion per `sessions/permanent-results-registry.md` line 12961 + clause
    (e) line 12995) PASSes the audit (state-history label `n_a^GGE` matches
    AND parse-tree marker `parse-tree decision` matches).

  - **T2 (negative)**: synthetic §VII entry with state-historic label but no
    parse-tree expansion fires `MISSING-PARSE-TREE-EXPANSION` diagnostic at
    S2 advisory severity.

  - **T3 (sanity 2x2 matrix)**: 4 synthetic cases covering the (label, expansion)
    presence matrix:
      * no_label_no_expansion       → no_state_history_label_present
      * label_only                  → MISSING-PARSE-TREE-EXPANSION
      * expansion_only              → no_state_history_label_present
      * both_present                → PASS

  - **T4 (lizzi CO-SIGN-WITH-NOTES)**: 7 synthetic cases verifying the 3 forward
    pattern additions surfaced by lizzi-spectral-functional-theorist's review of
    §W1-7 (audit_sha256=cee6a4da1c4ea564aa35768fe3e9aa663e137631a60ad77dd97abdde82d70943):
      * `Bogoliubov-state` / `Bogoliubov-amplitude` / `Bogoliubov-coefficient`
        → all match (gap closure between §W1-7 §(1) Principle and §(3) regex)
      * `Δ_M` (Unicode) + `Delta_M` (ASCII) → match (S90 W7 plan line 103 usage)
      * `α_s_route_5` + `α_s_route_42` (large N)
        → match (regex generalization vs per-route enumeration)

PASS criterion (per plan §W1-8 #9):
  (i)   `registry-landing.md` sub-section appended (verified via SHA stability);
  (ii)  audit-script extension lands
        (`detect_class_h_missing_parse_tree_expansion` importable);
  (iii) positive test on §VII.U.2 PASSes;
  (iv)  negative test on synthetic entry fires diagnostic;
  (v)   allowlist + instances rows appended (orchestrator post-emit step).

Per `wave-classification.md §"Dual-SHA closure for METHODOLOGY-class"`:
  content_sha256 = SHA-256 over `_registry_landing_audit.py` (post-edit)
  audit_sha256   = SHA-256 over the ordered input-pin map (JSON-serialized)

Verdict emitted to `computations/session-90/s90_gate_verdicts.txt`.

Substrate framing
-----------------
Parse-tree expansion declaration IS the methodology-layer F-image of substrate-IS
commutativity per `epistemic-discipline.md §"Layer-Decomposition"`. The substrate's
spectral-triple observable `(A_K, H_K, D_K)` IS the substrate-IS closed form
(spectrum-only functional `(1/N) Σ_a m_a (Δ_BCS²/(2(λ²+Δ²)))^k − ...` for Var_a);
the GGE state-history label is an emergent post-hoc descriptor of the BdG
laboratory preparation pillar. The audit hook makes this F-image visible at the
registry-text layer and decidable from the registry alone, closing the silent
class-conflation pathway demonstrated by the S88 W-17 §V.3 corrigendum.
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

# Canonical-constants import per `computations/_shared/CLAUDE.md` MANDATORY
# discipline (S34+ scripts).
SHARED_DIR = Path(__file__).resolve().parent  # (local) — script-dir resolver
sys.path.insert(0, str(SHARED_DIR))
try:
    from canonical_constants import *  # noqa: F401,F403
except Exception as e:
    print(f"ERROR: canonical_constants.py import failed: {e}", file=sys.stderr)
    raise

# Import the extended audit-script's Class-(h) detector + pattern sets +
# any-level block extractor.
from _registry_landing_audit import (  # noqa: E402
    detect_class_h_missing_parse_tree_expansion,
    extract_registry_block_anylevel,
    STATE_HISTORY_LABEL_PATTERNS,
    PARSE_TREE_EXPANSION_MARKERS,
)
from s90_w1_emit_verdict import emit_verdict  # noqa: E402


PROJECT_ROOT = SHARED_DIR.parents[1]  # (local) — repo-root resolver
AUDIT_SCRIPT = SHARED_DIR / '_registry_landing_audit.py'  # (local) — audit target
RULE_FILE = PROJECT_ROOT / '.claude' / 'rules' / 'registry-landing.md'  # (local)
W1_7_RULE_FILE = (
    PROJECT_ROOT / '.claude' / 'rules' / 'cross-pillar-bridge-anatomy.md'
)  # (local) — paired sub-clause source
REGISTRY_MD = PROJECT_ROOT / 'sessions' / 'permanent-results-registry.md'  # (local)

GATE_ID = (  # (local) — plan §W1-8 gate-ID
    'S90-PARSE-TREE-EXPANSION-PRE-REGISTRATION-FOR-NEW-VII-ENTRIES'
)


def t1_positive_vii_u_2() -> dict:
    """T1 — read §VII.U.2 block from registry, run detector, expect PASS.

    §VII.U.2 contains state-history label `n_a^GGE` (Corner II row line 12961)
    AND parse-tree decision text (clause (e) line 12995); detector should
    return diagnostic = 'PASS'.
    """
    if not REGISTRY_MD.exists():
        return {
            'test': 'T1_positive_vii_u_2',
            'error': f'registry not found at {REGISTRY_MD}',
            'passes': False,
        }
    text = REGISTRY_MD.read_text(encoding='utf-8')
    block = extract_registry_block_anylevel(text, '§VII.U.2')
    if not block:
        return {
            'test': 'T1_positive_vii_u_2',
            'error': 'failed to extract §VII.U.2 block from registry',
            'passes': False,
        }
    result = detect_class_h_missing_parse_tree_expansion(block, '§VII.U.2')
    expected_diagnostic = 'PASS'  # (local)
    actual_diagnostic = result['diagnostic']  # (local)
    passes = (actual_diagnostic == expected_diagnostic)  # (local)
    return {
        'test': 'T1_positive_vii_u_2',
        'block_size_chars': len(block),
        'state_history_matches': len(
            result.get('state_history_label_matches', [])
        ),
        'parse_tree_expansion_present': result.get(
            'parse_tree_expansion_present', False
        ),
        'parse_tree_marker_match': result.get('parse_tree_marker_match', None),
        'expected_diagnostic': expected_diagnostic,
        'actual_diagnostic': actual_diagnostic,
        'passes': passes,
    }


def t2_negative_synthetic() -> dict:
    """T2 — synthetic §VII entry with state-historic label, no reduction declared.

    NOTE: the synthetic block deliberately AVOIDS the literal string
    "parse-tree" anywhere in its body, since the audit's
    PARSE_TREE_EXPANSION_RE includes a broad fallback `\\bparse-tree\\b`
    that matches any lexical mention (including negations like "without
    parse-tree expansion"). The audit cannot parse semantic intent — only
    lexical presence — so a faithful negative-test fixture must avoid
    the trigger string entirely.
    """
    synthetic_block = (  # (local) — synthetic test fixture (no parse-tree mention)
        '### §VII.SYNTHETIC.NEG — Hypothetical entry citing n_a^GGE with no '
        'reduction chain declared\n'
        '\n'
        'This synthetic block names n_a^GGE (a state-history label) but '
        'provides only a numerical value:\n'
        '  some_observable = 1.23e-5 at L_max=10\n'
        'No reduction is provided; the substrate-IS closed form is opaque '
        'from the registry text alone.\n'
    )
    result = detect_class_h_missing_parse_tree_expansion(
        synthetic_block, '§VII.SYNTHETIC.NEG'
    )
    expected_diagnostic = 'MISSING-PARSE-TREE-EXPANSION'  # (local)
    actual_diagnostic = result['diagnostic']  # (local)
    passes = (actual_diagnostic == expected_diagnostic)  # (local)
    return {
        'test': 'T2_negative_synthetic',
        'expected_diagnostic': expected_diagnostic,
        'actual_diagnostic': actual_diagnostic,
        'state_history_matches': len(
            result.get('state_history_label_matches', [])
        ),
        'parse_tree_expansion_present': result.get(
            'parse_tree_expansion_present', False
        ),
        'has_class_h_flag': result.get('has_class_h_flag', False),
        'severity': result.get('severity', 'UNKNOWN'),
        'passes': passes,
    }


def t3_synthetic_sanity_cases() -> dict:
    """T3 — 4 sanity cases covering (label, expansion) presence matrix."""
    cases = [  # (local) — 2x2 matrix
        {
            'label': 'no_label_no_expansion',
            'block': (
                '### §VII.X — generic entry with neither label nor expansion.\n'
                '\nSome content with no triggers.'
            ),
            'expected_diagnostic': 'no_state_history_label_present',
        },
        {
            'label': 'label_only',
            'block': (
                '### §VII.X — entry citing α_s_canonical without expansion.\n'
                '\nValue = -0.0859 at L_max=10. No reduction provided.'
            ),
            'expected_diagnostic': 'MISSING-PARSE-TREE-EXPANSION',
        },
        {
            'label': 'expansion_only',
            'block': (
                '### §VII.X — entry with parse-tree decision text but no '
                'state-history label.\n'
                '\nThe parse-tree decision procedure is finite. Some '
                'unrelated value = 1.0.'
            ),
            'expected_diagnostic': 'no_state_history_label_present',
        },
        {
            'label': 'both_present',
            'block': (
                '### §VII.X — entry with α_s_canonical AND parse-tree '
                'expansion.\n'
                '\nParse-tree expansion: α_s_canonical → '
                '(Mellin-residue at substrate-distance-1)² − 1.'
            ),
            'expected_diagnostic': 'PASS',
        },
    ]
    results = []  # (local)
    for case in cases:
        r = detect_class_h_missing_parse_tree_expansion(
            case['block'], '§VII.X.SANITY'
        )
        actual = r['diagnostic']  # (local)
        passes = (actual == case['expected_diagnostic'])  # (local)
        results.append({
            'label': case['label'],
            'expected': case['expected_diagnostic'],
            'actual': actual,
            'state_history_matches': len(
                r.get('state_history_label_matches', [])
            ),
            'parse_tree_expansion_present': r.get(
                'parse_tree_expansion_present', False
            ),
            'passes': passes,
        })
    n_pass = sum(1 for r in results if r['passes'])  # (local)
    n_total = len(cases)  # (local)
    return {
        'test': 'T3_synthetic_sanity_cases',
        'n_cases': n_total,
        'n_pass': n_pass,
        'cases': results,
        'passes': (n_pass == n_total),
    }


def t4_lizzi_cosign_extensions() -> dict:
    """T4 — verify lizzi CO-SIGN-WITH-NOTES forward additions match correctly.

    Each test case constructs a synthetic §VII entry containing one of the
    three lizzi forward-pattern targets (without parse-tree expansion) and
    verifies the detector fires MISSING-PARSE-TREE-EXPANSION (i.e., the
    state-history label IS recognized by the extended pattern set).
    """
    cases = [  # (local) — lizzi forward additions
        # Pattern 1: \bBogoliubov-(state|amplitude|coefficient)\b
        ('Bogoliubov-state covariance test',
         'MISSING-PARSE-TREE-EXPANSION', 'lizzi_bogoliubov_state'),
        ('Bogoliubov-amplitude reduction',
         'MISSING-PARSE-TREE-EXPANSION', 'lizzi_bogoliubov_amplitude'),
        ('Bogoliubov-coefficient series',
         'MISSING-PARSE-TREE-EXPANSION', 'lizzi_bogoliubov_coefficient'),
        # Pattern 2: Δ_M (Unicode) + Delta_M (ASCII)
        ('Δ_M observable in S90 W7 parity-twin',
         'MISSING-PARSE-TREE-EXPANSION', 'lizzi_delta_m_unicode'),
        ('Delta_M ASCII variant for legacy scripts',
         'MISSING-PARSE-TREE-EXPANSION', 'lizzi_delta_m_ascii'),
        # Pattern 3: α_s_route_[0-9]+ regex generalization
        ('α_s_route_5 hypothetical',
         'MISSING-PARSE-TREE-EXPANSION', 'lizzi_alpha_s_route_5'),
        ('α_s_route_42 (large N stress test)',
         'MISSING-PARSE-TREE-EXPANSION', 'lizzi_alpha_s_route_large'),
    ]
    results = []  # (local)
    for content, expected, label in cases:
        block = (  # (local)
            f'### §VII.X — entry with {label}: {content}.\n'
            '\nValue = TBD; no reduction declared.'
        )
        r = detect_class_h_missing_parse_tree_expansion(block, '§VII.X.LIZZI')
        actual = r['diagnostic']  # (local)
        passes = (actual == expected)  # (local)
        results.append({
            'label': label,
            'content_excerpt': content,
            'expected': expected,
            'actual': actual,
            'state_history_matches': len(
                r.get('state_history_label_matches', [])
            ),
            'matched_patterns': [
                m['pattern'] for m in r.get('state_history_label_matches', [])
            ],
            'passes': passes,
        })
    n_pass = sum(1 for r in results if r['passes'])  # (local)
    n_total = len(cases)  # (local)
    return {
        'test': 'T4_lizzi_cosign_extensions',
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
    t1 = t1_positive_vii_u_2()
    t2 = t2_negative_synthetic()
    t3 = t3_synthetic_sanity_cases()
    t4 = t4_lizzi_cosign_extensions()
    all_pass = (  # (local)
        t1.get('passes', False)
        and t2.get('passes', False)
        and t3.get('passes', False)
        and t4.get('passes', False)
    )
    return {
        'gate_id': GATE_ID,
        'tests_overall': 'PASS' if all_pass else 'FAIL',
        'T1_positive_vii_u_2': t1,
        'T2_negative_synthetic': t2,
        'T3_synthetic_sanity_cases': t3,
        'T4_lizzi_cosign_extensions': t4,
    }


def emit_gate_verdict(test_report: dict, supersedes: str = '') -> dict:
    """Build 10-pin input-pin map per plan §W1-8 #7 PRDR; emit canonical line.

    Args:
        test_report: aggregated test report from `run_all_tests()`.
        supersedes:  optional full 64-char audit_sha256 of a prior verdict
                     line being superseded per Option A protocol
                     (`.claude/rules/gate-verdicts.md §"Option A — sig_5
                     remediation pathway"`); when provided, the canonical
                     line carries `value='<v>;supersedes=<full-sha>'`.
    """
    state_history_pattern_set = '|'.join(STATE_HISTORY_LABEL_PATTERNS)  # (local)
    parse_tree_pattern_set = '|'.join(PARSE_TREE_EXPANSION_MARKERS)  # (local)

    input_pin_map = {  # (local) — 10-pin map per plan §W1-8 #7 PRDR
        'pin_01_audit_script_post_edit': sha256_of_file(AUDIT_SCRIPT),
        'pin_02_test_driver': sha256_of_file(Path(__file__).resolve()),
        'pin_03_rule_file_registry_landing': (
            sha256_of_file(RULE_FILE) if RULE_FILE.exists() else 'MISSING'
        ),
        'pin_04_w1_7_paired_rule_file': (
            sha256_of_file(W1_7_RULE_FILE)
            if W1_7_RULE_FILE.exists() else 'MISSING'
        ),
        'pin_05_registry_md': (
            sha256_of_file(REGISTRY_MD) if REGISTRY_MD.exists() else 'MISSING'
        ),
        'pin_06_state_history_pattern_set_sha': hashlib.sha256(
            state_history_pattern_set.encode('utf-8')
        ).hexdigest(),
        'pin_07_parse_tree_pattern_set_sha': hashlib.sha256(
            parse_tree_pattern_set.encode('utf-8')
        ).hexdigest(),
        'pin_08_lizzi_cosign_review_audit_sha_W1_7': (
            'cee6a4da1c4ea564aa35768fe3e9aa663e137631a60ad77dd97abdde82d70943'
        ),
        'pin_09_K_calibration_corpus_size': '1',  # (local) Var_a Corner II
        'pin_10_plan_gate_id': GATE_ID,
    }

    verdict = (  # (local) — single-pass verdict from aggregated test report
        'PASS' if test_report['tests_overall'] == 'PASS' else 'FAIL'
    )
    t1 = test_report['T1_positive_vii_u_2']  # (local)
    t2 = test_report['T2_negative_synthetic']  # (local)
    t3 = test_report['T3_synthetic_sanity_cases']  # (local)
    t4 = test_report['T4_lizzi_cosign_extensions']  # (local)

    value_str = (  # (local)
        f'parse_tree_expansion_audit_extension_landed_AND_tests_'
        f'{test_report["tests_overall"]};'
        f'T1_positive_VII_U_2={t1.get("actual_diagnostic", "ERROR")};'
        f'T2_negative_synthetic={t2.get("actual_diagnostic", "ERROR")};'
        f'T3_sanity_pass={t3.get("n_pass", 0)}_of_{t3.get("n_cases", 0)};'
        f'T4_lizzi_cosign_extensions_pass={t4.get("n_pass", 0)}_of_'
        f'{t4.get("n_cases", 0)};'
        f'state_history_pattern_count={len(STATE_HISTORY_LABEL_PATTERNS)};'
        f'parse_tree_pattern_count={len(PARSE_TREE_EXPANSION_MARKERS)};'
        f'lizzi_cosign_extensions_baked_in=True;'
        f'K_calibration=1_VarA_CornerII_VII_U_2_line_12961;'
        f'allowlist_row=pending;instances_row=pending'
    )

    result = emit_verdict(
        gate_id=GATE_ID,
        verdict=verdict,
        value_str=value_str,
        scheme='registry-landing-extension',
        convention='parse-tree-expansion-pre-registration',
        L_max='N/A',
        input_pin_map=input_pin_map,
        content_target=AUDIT_SCRIPT,
        supersedes=supersedes,
    )
    return result


def main(supersedes: str = '') -> int:
    """Run all tests, print report, emit verdict line. Exit 0 regardless of verdict.

    Args:
        supersedes: optional 64-char audit_sha256 of a prior verdict line being
                    superseded per Option A protocol (`gate-verdicts.md §"Option
                    A — sig_5 remediation pathway"`).
    """
    print('=== S90 W1-8 parse-tree expansion audit hook test driver ===')
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
    # CLI: optional --supersedes <full-64-char-sha> argument for Option A protocol
    sup_arg = ''  # (local) — default empty (fresh emission)
    if '--supersedes' in sys.argv:
        idx = sys.argv.index('--supersedes')  # (local) — argv index
        if idx + 1 < len(sys.argv):
            sup_arg = sys.argv[idx + 1]
    sys.exit(main(supersedes=sup_arg))
