#!/usr/bin/env python3
"""
_s90_w1_invoke_emit.py — Orchestrator-side invoker for S90 W1 verdict-line emission.

Builds the input-pin map at runtime for each gate, then calls emit_verdict() to
append the canonical verdict + dual-SHA companion row to the verdict file.

Used during /rclab-solo execution by the orchestrator (gen-physicist) per
sessions/session-plan/session-90-plan-w1.md §"Machinery-Enumeration Pin".
"""
import hashlib
import json
import sys
from pathlib import Path

_shared_dir = Path(__file__).resolve().parent  # (local) — script dir resolver
sys.path.insert(0, str(_shared_dir))

from s90_w1_emit_verdict import (  # noqa: E402
    emit_verdict,
    sha256_of_file,
    sha256_of_text,
)

REPO_ROOT = Path(__file__).resolve().parents[2]  # (local) — repo-root resolver


def extract_registry_block_sha(slot_label: str) -> str:
    """SHA-256 over the §VII slot block text in permanent-results-registry.md."""
    import re
    registry_md = REPO_ROOT / 'sessions' / 'permanent-results-registry.md'
    text = registry_md.read_text(encoding='utf-8', errors='ignore')
    escaped = re.escape(slot_label)
    block_re = re.compile(rf'(## {escaped}\b[^\n]*\n[\s\S]*?)(?=\n##\s)', re.MULTILINE)
    m = block_re.search(text)
    if not m:
        return ''
    return sha256_of_text(m.group(1))


def invoke_w1_1():
    """Emit verdict for S90-VII-AN-AUDIT-SCRIPT-REGISTRY-ANCHOR-RECONCILIATION-EXTENSION."""
    audit_script = REPO_ROOT / 'computations' / '_shared' / '_registry_landing_audit.py'
    self_test_script = REPO_ROOT / 'computations' / '_shared' / 's90_w1_vii_an_audit_script_extension_test.py'
    substrate_first_audit = REPO_ROOT / 'computations' / '_shared' / '_substrate_first_provenance_audit.py'

    input_pin_map = {
        'pin_01_registry_landing_audit_py_sha': sha256_of_file(audit_script),
        'pin_02_self_test_script_sha': sha256_of_file(self_test_script),
        'pin_03_substrate_first_provenance_audit_py_sha': sha256_of_file(substrate_first_audit) if substrate_first_audit.exists() else 'absent_at_dispatch',
        'pin_04_registry_VII_AN_block_sha': extract_registry_block_sha('§VII.AN'),
        'pin_05_W6_2_audit_sha_fixed': '9f7a203def8301f7589501b7d73030097ceeb060cd714b1be785f0737619aa5f',
        'pin_06_W5a_44_audit_sha_fixed': 'c092fe1bff9ab66928aa9c545a3a22776f847053af40b5d2814db0143d21f64b',
        'pin_07_VII_AN_CORRIGENDUM_audit_sha_fixed': '58d870e9116b49e8bfad87759a11df3606ca977aca13c015f58dbda250e25ba8',
        'pin_08_detection_regex': r'^#\s*(Route|Derivation):\s*(.+)$',
        'pin_09_severity_band_S2_advisory_when_script_found': True,
        'pin_10_severity_band_S1_mandatory_when_script_not_found': True,
        'pin_11_plan_gate_id': 'S90-VII-AN-AUDIT-SCRIPT-REGISTRY-ANCHOR-RECONCILIATION-EXTENSION',
    }

    result = emit_verdict(
        gate_id='S90-VII-AN-AUDIT-SCRIPT-REGISTRY-ANCHOR-RECONCILIATION-EXTENSION',
        verdict='PASS',
        value_str='audit-script-extension-landed-AND-flags-§VII.AN-at-S2-advisory;class_g_flag=True;self_test_PASS=4_of_4;diagnostic=route_declaration_absent_in_producing_script;K_calibration=1;allowlist_row=pending;instances_row=pending',
        scheme='registry-anchor-class-g-extension',
        convention='route-a-vs-route-b-detection-static-string-compare',
        L_max='N/A',
        input_pin_map=input_pin_map,
        content_target=audit_script,
    )
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return result


if __name__ == '__main__':
    invoke_w1_1()
