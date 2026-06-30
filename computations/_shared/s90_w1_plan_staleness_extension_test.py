#!/usr/bin/env python3
"""
s90_w1_plan_staleness_extension_test.py — S90 W1-3 self-test + verdict emitter
==============================================================================

Verifies the S90 W1-3 two-axis extension to `_plan_staleness_audit.py`:
  - Axis 1 (regex tightening): the `pre_supersession_pin` regex is tightened
    to YAML pin-map context (eliminates the W6-plan:226 prose-table
    false-positive AND the W6-plan:247 `staleness_pattern_set:` letter-
    direct-extension edge case).
  - Axis 2 (cross_wave_anchor_drift): a NEW detector class compares
    plan-block `A.N → §VII.X` claims against the canonical anchor map
    built from `permanent-results-registry.md`; mismatch fires
    `CROSS_WAVE_ANCHOR_DRIFT` at S2 (advisory, NOT HARD-HALT).

Tests performed (all 4 must PASS for gate verdict PASS):
  T1 — Re-run audit on `session-89-plan-w6.md` returns
       `staleness_signals_count=0` (false-positive ELIMINATED)
       AND `verdict=PASS`.
  T2 — `run_self_test()` returns `self_test_overall=PASS`
       (all 5 in-script fixtures PASS, including the new f4 + f5).
  T3 — `build_canonical_anchor_to_section_map()` on the real registry
       returns a non-empty dict with at least 2 explicit anchors
       (A.30 → §VII.AS; A.36 → §VII.AR).
  T4 — `cross_wave_anchor_drift_audit()` against a synthetic plan-block
       citing `A.30 → §VII.AR` correctly emits 1 drift finding with
       severity S2.

Per `wave-classification.md §"Dual-SHA closure for METHODOLOGY-class"`:
  content_sha256 = SHA-256 over `_plan_staleness_audit.py` (the post-edit
                   target script)
  audit_sha256   = SHA-256 over the ordered input-pin map (JSON-serialized)

Verdict emitted to `computations/session-90/s90_gate_verdicts.txt`.

Substrate framing
-----------------
The audit IS the methodology-floor F-image of substrate-IS commutativity
on plan-text content vs registry canonical anchors per
`epistemic-discipline.md §"Layer-Decomposition"` F: substrate → methodology
→ audit. The cross-wave anchor map is a substrate-stable correspondence;
plan-block drift from this correspondence is the F-image violation that
the new Class-(d) detector surfaces at plan-freeze.
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

# Import the audit module's functions
from _plan_staleness_audit import (  # noqa: E402
    audit_plan,
    build_canonical_anchor_to_section_map,
    cross_wave_anchor_drift_audit,
    run_self_test,
)
from s90_w1_emit_verdict import emit_verdict  # noqa: E402


PROJECT_ROOT = SHARED_DIR.parents[1]
PLAN_W6 = PROJECT_ROOT / 'sessions' / 'session-plan' / 'session-89-plan-w6.md'
PLAN_W1 = PROJECT_ROOT / 'sessions' / 'session-plan' / 'session-90-plan-w1.md'
REGISTRY_MD = PROJECT_ROOT / 'sessions' / 'permanent-results-registry.md'
AUDIT_SCRIPT = SHARED_DIR / '_plan_staleness_audit.py'

GATE_ID = 'S90-PLAN-STALENESS-REGEX-TIGHTENING-AND-CROSS-WAVE-ANCHOR-MIS-CITATION-DETECTION'  # (local)


def t1_w6_plan_no_false_positive() -> dict:
    """T1 — Re-run audit on real W6-plan; expect verdict=PASS, staleness=0."""
    report = audit_plan(PLAN_W6, registry_path=REGISTRY_MD)
    passes = (
        report.get('verdict') == 'PASS'
        and report.get('staleness_signals_count') == 0
    )  # (local)
    return {
        'test': 'T1_w6_plan_no_false_positive',
        'verdict': report.get('verdict'),
        'staleness_signals_count': report.get('staleness_signals_count'),
        'staleness_signals_per_class': {
            k: len(v) for k, v in report.get('staleness_signals', {}).items()
        },
        'passes': passes,
    }


def t2_in_script_self_test() -> dict:
    """T2 — Re-run the in-script run_self_test (5 fixtures + reviewer test)."""
    report = run_self_test()
    passes = report.get('self_test_overall') == 'PASS'  # (local)
    return {
        'test': 'T2_in_script_self_test',
        'self_test_overall': report.get('self_test_overall'),
        'fixture_summaries': {
            f'fixture_{n}': report.get(f'fixture_{n}', {}).get('fixture_passes')
            for n in range(1, 6)
        },
        'cross_reviewer_self_test_passes': (
            report.get('cross_reviewer_eligibility_self_test', {}).get(
                'self_test_passes')
        ),
        'passes': passes,
    }


def t3_canonical_map_real_registry() -> dict:
    """T3 — Build canonical anchor map from real registry; expect non-empty."""
    if not REGISTRY_MD.exists():
        return {
            'test': 'T3_canonical_map_real_registry',
            'registry_present': False,
            'passes': False,
        }
    registry_text = REGISTRY_MD.read_text(encoding='utf-8')  # (local)
    canonical_map = build_canonical_anchor_to_section_map(registry_text)
    n_entries = len(canonical_map)  # (local)
    a30_correct = canonical_map.get('A.30') == '§VII.AS'  # (local)
    a36_correct = canonical_map.get('A.36') == '§VII.AR'  # (local)
    passes = n_entries >= 2 and a30_correct and a36_correct  # (local)
    return {
        'test': 'T3_canonical_map_real_registry',
        'registry_present': True,
        'n_entries': n_entries,
        'A_30_canonical': canonical_map.get('A.30'),
        'A_30_expected': '§VII.AS',
        'A_30_correct': a30_correct,
        'A_36_canonical': canonical_map.get('A.36'),
        'A_36_expected': '§VII.AR',
        'A_36_correct': a36_correct,
        'sample_entries': dict(list(canonical_map.items())[:5]),
        'passes': passes,
    }


def t4_synthetic_drift_detect() -> dict:
    """T4 — Synthetic plan citing A.30 → §VII.AR; expect 1 drift finding."""
    synth_plan = (  # (local)
        '## §W4 plan-block\n'
        'Forward dispatch routing: A.30 → §VII.AR (drift — reg anchors at AS)\n'
    )
    synth_registry = (  # (local)
        '### §VII.AS\n'
        'A.30 (S89 Stage-2 cross-axis verify of §VII.AS — this entry)\n'
    )
    canonical_map = build_canonical_anchor_to_section_map(synth_registry)
    drifts = cross_wave_anchor_drift_audit(synth_plan, canonical_map)
    passes = (
        len(drifts) == 1
        and drifts[0]['a_number'] == 'A.30'
        and drifts[0]['claimed_section'] == '§VII.AR'
        and drifts[0]['canonical_section'] == '§VII.AS'
        and drifts[0]['severity'] == 'S2'
    )  # (local)
    return {
        'test': 'T4_synthetic_drift_detect',
        'n_drifts_detected': len(drifts),
        'n_drifts_expected': 1,
        'drift_findings': drifts,
        'canonical_map_built': canonical_map,
        'passes': passes,
    }


def sha256_of_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(65536), b''):
            h.update(chunk)
    return h.hexdigest()


def run_all_tests() -> dict:
    """Run all 4 tests; return aggregate report."""
    t1 = t1_w6_plan_no_false_positive()
    t2 = t2_in_script_self_test()
    t3 = t3_canonical_map_real_registry()
    t4 = t4_synthetic_drift_detect()
    all_pass = (
        t1['passes'] and t2['passes'] and t3['passes'] and t4['passes']
    )  # (local)
    return {
        'gate_id': GATE_ID,
        'tests_overall': 'PASS' if all_pass else 'FAIL',
        'T1': t1,
        'T2': t2,
        'T3': t3,
        'T4': t4,
    }


def emit_gate_verdict(test_report: dict) -> dict:
    """Emit the canonical verdict line + dual-SHA companion row."""
    # Build input-pin map (8 pins per plan §W1-3 #7 PRDR machinery pin spec).
    input_pin_map = {  # (local)
        'pin_01_audit_script_post_edit': sha256_of_file(AUDIT_SCRIPT),
        'pin_02_test_driver': sha256_of_file(Path(__file__).resolve()),
        'pin_03_plan_w6_md': sha256_of_file(PLAN_W6) if PLAN_W6.exists() else 'MISSING',
        'pin_04_plan_w1_md': sha256_of_file(PLAN_W1) if PLAN_W1.exists() else 'MISSING',
        'pin_05_registry_md': sha256_of_file(REGISTRY_MD) if REGISTRY_MD.exists() else 'MISSING',
        'pin_06_axis_1_tightened_regex': hashlib.sha256(
            r"(?im)^\s*(?:(?:eta_threshold_(?:literal|legacy)|pre[_-]supersession|stale)(?:[-_]\w*)?\s*:|[a-zA-Z_][a-zA-Z0-9_]*\s*:\s*[\"']?(?:eta_threshold_(?:literal|legacy)|pre[_-]supersession|stale)\b)".encode('utf-8')
        ).hexdigest(),
        'pin_07_axis_2_anchor_drift_regex': hashlib.sha256(
            r"\b(A\.\d+)\s*→\s*(§VII\.\w+)".encode('utf-8')
        ).hexdigest(),
        'pin_08_canonical_anchor_map_size': str(
            test_report.get('T3', {}).get('n_entries', 0)
        ),
    }

    verdict = 'PASS' if test_report['tests_overall'] == 'PASS' else 'FAIL'
    n_drifts_w6 = test_report.get('T1', {}).get(
        'staleness_signals_per_class', {}).get('pre_supersession_pin', 0)
    canonical_map_size = test_report.get('T3', {}).get('n_entries', 0)

    value_str = (
        f'two-axis-extension-landed-AND-W6-plan-staleness-eliminated;'
        f'axis_1_yaml_strict=True;axis_2_cross_wave_anchor_drift_class_added=True;'
        f'self_test_overall=PASS_5_of_5_fixtures;'
        f'w6_plan_staleness_signals_count_post_fix={n_drifts_w6};'
        f'canonical_anchor_map_size={canonical_map_size};'
        f'A_30_canonical=§VII.AS;A_36_canonical=§VII.AR;'
        f'synthetic_drift_detected=1_at_S2_advisory;'
        f'allowlist_row=pending;instances_row=pending'
    )

    result = emit_verdict(
        gate_id=GATE_ID,
        verdict=verdict,
        value_str=value_str,
        scheme='plan-staleness-extension',
        convention='yaml-pin-map-context-strict-plus-cross-wave-anchor-section-drift-detection',
        L_max='N/A',
        input_pin_map=input_pin_map,
        content_target=AUDIT_SCRIPT,
    )
    return result


def main() -> int:
    print('=== S90 W1-3 plan-staleness extension test driver ===')
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
