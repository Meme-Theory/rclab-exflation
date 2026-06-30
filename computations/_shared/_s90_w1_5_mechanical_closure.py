#!/usr/bin/env python3
"""
_s90_w1_5_mechanical_closure.py — Mechanical PRE-REG-INC closure for W1-5.

Gate: S90-FI-RD-MIXED-AXIS-FIELD-EXTENSION-CF-W6-4-DICT (CF-LZ-2)

Reason: in-session prerequisite W1-2 `S90-CORNER-CLASSIFICATION-AUDIT-VII-U-2-EXTENSION`
landed verdict=INFO (PRE-REG-INC) at W1-2 dispatch (audit_sha256=
`526a38d0baca18998d37aff5bd7512616efda575dabf8adb6d7d4854a99541a8`).  Plan §W1-5
#6 declares "PREREQUISITE: CF-2 (§W1-2 above) must land PASS before dispatch";
plan §W1-5 #9 pre-registers: "INFO iff CF-2 has not landed PASS (PRE-REG-INC
blocked)".  CF-2 (= §W1-2) did NOT land PASS — it landed INFO — so the §9
INFO clause fires by pre-registration.

Transitive root cause: §W1-2 itself was INFO-closed because cross-wave
prerequisite W2 CF-25 `S90-VII-U-2-CORNER-RECONCILIATION-READING-B-LOCK-IN`
had NOT landed PASS at W1 dispatch time.

Per `.claude/rules/mechanical-closure-discipline.md`:
  - upstream-block topology IS the cause (§W1-2 verdict = INFO, not PASS)
  - plan §W1-5 #9 threshold pre-registered: INFO iff CF-2 NOT PASS
  - verdict honesty: emit INFO with PRE-REG-INC value string (NEVER PASS)
  - per-gate-distinct audit_sha256 (computed over W1-5-specific input-pin map)
  - audit-trail signature naming blocking prereq verbatim

Per `.claude/rules/gate-verdicts.md`:
  - canonical line at `computations/session-90/s90_gate_verdicts.txt`
  - dual-SHA closure with full 64-char SHAs (never truncated in canonical row)
"""
import json
import sys
from pathlib import Path

_shared_dir = Path(__file__).resolve().parent  # (local) — script dir resolver
sys.path.insert(0, str(_shared_dir))

# Canonical-constants import per math-scripts.md (S34+ scripts MANDATORY).
# No framework constants are USED in this mechanical closure (the upstream
# block prevents substantive computation); the import satisfies the
# `computations/_shared/CLAUDE.md` discipline that ALL scripts import.
try:
    from canonical_constants import *  # noqa: F401,F403,E402
except Exception as e:
    print(f"ERROR: canonical_constants.py import failed: {e}", file=sys.stderr)
    raise

from s90_w1_emit_verdict import emit_verdict, sha256_of_text  # noqa: E402
from _s90_w1_invoke_emit import extract_registry_block_sha  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[2]  # (local) — repo-root resolver


def main():
    """Emit mechanical PRE-REG-INC verdict for §W1-5."""
    plan_w1 = REPO_ROOT / 'sessions' / 'session-plan' / 'session-90-plan-w1.md'

    # The "content target" for METHODOLOGY-class mechanical closure is this
    # script itself (the closure script body), since no audit-script extension
    # was produced (the upstream block prevented `_corner_classification_audit.py`
    # extension from being computable).
    content_target = Path(__file__).resolve()

    input_pin_map = {
        'pin_01_plan_W1_5_block_sha_runtime': sha256_of_text(
            extract_w1_5_plan_block_text(plan_w1)
        ),
        'pin_02_registry_VII_K_DUAL_LEVEL_DRESSED_block_sha_runtime': (
            extract_registry_block_sha('§VII.K-DUAL.LEVEL-DRESSED')
        ),
        'pin_03_W1_2_verdict_status': 'INFO_PRE_REG_INC_at_audit_sha256_526a38d0',
        'pin_04_direct_blocking_prereq_gate_id': (
            'S90-CORNER-CLASSIFICATION-AUDIT-VII-U-2-EXTENSION'
        ),
        'pin_05_transitive_blocking_prereq_gate_id': (
            'S90-VII-U-2-CORNER-RECONCILIATION-READING-B-LOCK-IN'
        ),
        'pin_06_mechanical_closure_script_sha': sha256_of_text(
            content_target.read_text(encoding='utf-8', errors='ignore')
        ),
        'pin_07_plan_gate_id': 'S90-FI-RD-MIXED-AXIS-FIELD-EXTENSION-CF-W6-4-DICT',
        'pin_08_threshold_reference': (
            'plan_W1_5_pre_registered_INFO_threshold_iff_CF_2_NOT_PASS'
        ),
    }

    result = emit_verdict(
        gate_id='S90-FI-RD-MIXED-AXIS-FIELD-EXTENSION-CF-W6-4-DICT',
        verdict='INFO',
        value_str=(
            'PRE-REG-INC_blocked_by_S90-CORNER-CLASSIFICATION-AUDIT-VII-U-2-EXTENSION_INFO_NOT_PASS;'
            'direct_blocker=W1_2_landed_INFO_audit_sha256_526a38d0baca18998d37aff5bd7512616efda575dabf8adb6d7d4854a99541a8;'
            'transitive_root=W2_CF_25_S90-VII-U-2-CORNER-RECONCILIATION-READING-B-LOCK-IN_NOT_LANDED;'
            'reason=in_session_prerequisite_W1_2_landed_INFO_not_PASS_per_plan_W1_5_section_9_INFO_clause;'
            'solo_mode=W1_only_per_user_rclab_solo_dispatch;'
            'remediation=deferred_to_S91_after_W2_CF-25_PASS_drives_W1_2_to_PASS_OR_parallel_W2_dispatch;'
            'closure_type=mechanical_per_mechanical-closure-discipline.md;'
            'M1_M2_M3_M4_conjunction_satisfied_at_plan_freeze=True'
        ),
        scheme='corner-classification-axis-extension',
        convention='fi-rd-mixed-trichotomy-plus-f-traj-dressing-factors',
        L_max='N/A',
        input_pin_map=input_pin_map,
        content_target=content_target,
    )
    print(json.dumps(result, indent=2, ensure_ascii=False))


def extract_w1_5_plan_block_text(plan_path: Path) -> str:
    """Extract §W1-5 block from session-90-plan-w1.md."""
    import re
    text = plan_path.read_text(encoding='utf-8', errors='ignore')
    m = re.search(r'(## §W1-5\.[\s\S]*?)(?=\n## §W1-6\.)', text)
    return m.group(1) if m else ''


if __name__ == '__main__':
    main()
