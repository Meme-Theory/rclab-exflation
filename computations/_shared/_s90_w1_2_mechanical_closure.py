#!/usr/bin/env python3
"""
_s90_w1_2_mechanical_closure.py — Mechanical PRE-REG-INC closure for W1-2.

Gate: S90-CORNER-CLASSIFICATION-AUDIT-VII-U-2-EXTENSION
Reason: cross-wave prerequisite W2 CF-25 `S90-VII-U-2-CORNER-RECONCILIATION-READING-B-LOCK-IN`
has NOT landed PASS in `computations/session-90/s90_gate_verdicts.txt` at W1
dispatch time (user invoked /rclab-solo on W1 only; W2 is a separate dispatch).

Per `.claude/rules/mechanical-closure-discipline.md`:
  - upstream-block topology IS the cause (W2 CF-25 verdict ≠ PASS — verdict absent)
  - plan §W1-2 #9 threshold pre-registered: "INFO iff W2 CF-25 has not landed PASS"
  - verdict honesty: emit INFO with PRE-REG-INC value string (NEVER PASS)
  - per-gate-distinct audit_sha256 (computed over W1-2-specific input-pin map)
  - audit-trail signature naming blocking prereq

Per `.claude/rules/gate-verdicts.md`:
  - canonical line at `computations/session-90/s90_gate_verdicts.txt`
  - dual-SHA closure with full 64-char SHAs (never truncated in canonical row)
"""
import json
import sys
from pathlib import Path

_shared_dir = Path(__file__).resolve().parent  # (local) — script dir resolver
sys.path.insert(0, str(_shared_dir))

from s90_w1_emit_verdict import emit_verdict, sha256_of_text  # noqa: E402
from _s90_w1_invoke_emit import extract_registry_block_sha  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[2]  # (local) — repo-root resolver


def main():
    """Emit mechanical PRE-REG-INC verdict for §W1-2."""
    # Even though W2 CF-25 has NOT landed, we pin the inputs that WOULD have been read
    plan_w1 = REPO_ROOT / 'sessions' / 'session-plan' / 'session-90-plan-w1.md'

    # The "content target" for METHODOLOGY-class mechanical closure is this script
    # itself (the closure script body), since no audit-script extension was produced.
    content_target = Path(__file__).resolve()

    input_pin_map = {
        'pin_01_plan_W1_2_block_sha_runtime': sha256_of_text(
            extract_w1_2_plan_block_text(plan_w1)
        ),
        'pin_02_registry_VII_U_2_block_sha_runtime': extract_registry_block_sha('§VII.U.2'),
        'pin_03_W2_CF_25_verdict_status': 'NOT_LANDED_at_W1_dispatch',
        'pin_04_blocking_prereq_gate_id': 'S90-VII-U-2-CORNER-RECONCILIATION-READING-B-LOCK-IN',
        'pin_05_solo_mode_w1_only': True,
        'pin_06_mechanical_closure_script_sha': sha256_of_text(
            content_target.read_text(encoding='utf-8', errors='ignore')
        ),
        'pin_07_plan_gate_id': 'S90-CORNER-CLASSIFICATION-AUDIT-VII-U-2-EXTENSION',
        'pin_08_threshold_reference': 'plan_W1_2_pre_registered_INFO_threshold_iff_W2_CF_25_NOT_PASS',
    }

    result = emit_verdict(
        gate_id='S90-CORNER-CLASSIFICATION-AUDIT-VII-U-2-EXTENSION',
        verdict='INFO',
        value_str=(
            'PRE-REG-INC_blocked_by_S90-VII-U-2-CORNER-RECONCILIATION-READING-B-LOCK-IN_NOT_LANDED;'
            'reason=cross_wave_prerequisite_absent_at_W1_dispatch_time;'
            'solo_mode=W1_only_per_user_rclab_solo_dispatch;'
            'remediation=deferred_to_S91_after_W2_CF-25_PASS_OR_W2_dispatch_in_parallel_session;'
            'closure_type=mechanical_per_mechanical-closure-discipline.md;'
            'M1_M2_M3_M4_conjunction_satisfied_at_plan_freeze=True'
        ),
        scheme='corner-classification-audit-vii-u-2-extension',
        convention='wedderburn-4-corner-mandatory-k-3',
        L_max='N/A',
        input_pin_map=input_pin_map,
        content_target=content_target,
    )
    print(json.dumps(result, indent=2, ensure_ascii=False))


def extract_w1_2_plan_block_text(plan_path: Path) -> str:
    """Extract §W1-2 block from session-90-plan-w1.md."""
    import re
    text = plan_path.read_text(encoding='utf-8', errors='ignore')
    m = re.search(r'(## §W1-2\.[\s\S]*?)(?=\n## §W1-3\.)', text)
    return m.group(1) if m else ''


if __name__ == '__main__':
    main()
