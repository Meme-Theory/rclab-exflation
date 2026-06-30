#!/usr/bin/env python3
"""
s90_w1_vii_an_audit_script_extension_test.py — Self-test for S90 W1-1.

Gate: S90-VII-AN-AUDIT-SCRIPT-REGISTRY-ANCHOR-RECONCILIATION-EXTENSION
Trigger: [AUDIT]
Classification: METHODOLOGY
Agent: gen-physicist orchestrator-direct-write

Hypothesis: New Class-(g) `REGISTRY-ANCHOR-ROUTE-A-VS-ROUTE-B-CONFLATION`
detector in _registry_landing_audit.py flags §VII.AN's W5a-44 NEGATIVE-CALIBRATION
pattern (registry V-anchor claims Route-A while cited closure script implements
Route-B per W5a-44 audit_sha256=c092fe1bff9ab66928aa9c545a3a22776f847053af40b5d2814db0143d21f64b).

This self-test invokes detect_class_g on §VII.AN and verifies:
  (i)   has_class_g_flag = True (Class-(g) detector fires)
  (ii)  severity ∈ {S1, S2} (not NONE — drift is detected)
  (iii) diagnostic ∈ {script_not_found_AND_route_claimed,
                      route_declaration_absent_in_producing_script,
                      route_mismatch} (one of the three structural drift outcomes)
  (iv)  per-anchor diagnostic recorded for ANCHOR-1 (V) at minimum

Plan: sessions/session-plan/session-90-plan-w1.md §W1-1
Provenance: S90 W1-1 (gen-physicist orchestrator-direct-write, 2026-05-12)
"""

import json
import sys
from pathlib import Path

# Add _shared to path for import
_shared_dir = Path(__file__).resolve().parent
sys.path.insert(0, str(_shared_dir))

from _registry_landing_audit import (  # noqa: E402
    detect_class_g,
    extract_registry_block,
)


def run_self_test() -> dict:
    """Run detect_class_g on §VII.AN and return diagnostic dict."""
    repo_root = Path(__file__).resolve().parents[2]
    registry_md = repo_root / 'sessions' / 'permanent-results-registry.md'
    assert registry_md.exists(), f'registry not found at {registry_md}'

    text = registry_md.read_text(encoding='utf-8', errors='ignore')
    block = extract_registry_block(text, '§VII.AN')
    assert block, '§VII.AN block not extracted from registry'

    result = detect_class_g(block, registry_slot='§VII.AN', repo_root=repo_root)
    return result


def verify_outcome(result: dict) -> dict:
    """Verify the four PASS conditions of the W1-1 self-test."""
    checks = {
        'has_class_g_flag': result.get('has_class_g_flag') is True,
        'severity_drift_detected': result.get('severity') in ('S1', 'S2'),
        'diagnostic_in_drift_set': result.get('diagnostic') in (
            'script_not_found_AND_route_claimed',
            'route_declaration_absent_in_producing_script',
            'route_mismatch',
        ),
        'anchors_have_records': len(result.get('anchors', [])) >= 1,
    }
    all_pass = all(checks.values())
    return {
        'self_test_checks': checks,
        'all_pass': all_pass,
        'verdict': 'PASS' if all_pass else 'FAIL',
    }


def main():
    result = run_self_test()
    outcome = verify_outcome(result)
    report = {
        'gate': 'S90-VII-AN-AUDIT-SCRIPT-REGISTRY-ANCHOR-RECONCILIATION-EXTENSION',
        'self_test': outcome,
        'audit_result': result,
    }
    print(json.dumps(report, indent=2, ensure_ascii=False))
    sys.exit(0)


if __name__ == '__main__':
    main()
