"""
S88 W12-139 + W12-140 — Combined Mechanical-Closure Audit
============================================================

Two-gate combined audit for the two PRE-REG-INC mechanical-closure gates
remaining after §W12-138's plan-source-drift closure.

Gates:
  - §W12-139 S88-EE-BB-T-CROSS-CORRELATION-DIRECT-CSUB-PROBE
    Prereq: §VII.AJ.W4-1 cross-pillar 3-channel theorem PASS-conditional
  - §W12-140 S88-F-NL-EQUILATERAL-NON-GAUSSIANITY
    Prereq: W4-3 f_NL^folded language correction

Per knowledge-MCP audit:
  - §VII.AJ.W4-1 prereq → S87-CROSS-PILLAR-3-CHANNEL-THEOREM-PROOF
    closed at S87 with verdict INFO (value=1.0e-2; scheme=3-channel-x-
    3-pillar-Connes-Karoubi; convention=substrate-distance-anchored-
    Mellin). NOT a PASS-conditional landing. Plan §W12-139 condition
    "PASS-conditional landed" UNSATISFIED.
  - W4-3 prereq → S87-F-NL-FOLDED-W14-4-LANGUAGE-CORRECTION closed at
    S87 with verdict FAIL (value='byte-exact_replacement_blocked_by_
    class-c_PIN-DRIFT-FROM-STALE-SOURCE_plan-cited-locked-text-source-
    absent'). Plan §W12-140 condition "W4-3 landed" UNSATISFIED.

Both prereqs UNSATISFIED → mechanical-closure protocol fires for both
gates per `.claude/rules/mechanical-closure-discipline.md` §"When
mechanical closure IS acceptable" condition 1.

Per-gate-distinct audit_sha256 enforced via per-gate identity keys
(gate_id, wp_id, scheme, convention) in each input-pin map per
mechanical-closure-discipline.md §"When mechanical closure IS
acceptable" condition 3.

VERDICT TARGETS:
  §W12-139: FAIL value='PRE-REG-INC_blocked_by_VII-AJ-W4-1_CROSS-PILLAR-
                       3-CHANNEL-NOT-PASS-CONDITIONAL_S87_INFO_at_1e-2'
  §W12-140: FAIL value='PRE-REG-INC_blocked_by_W4-3_F-NL-FOLDED-
                       LANGUAGE-CORRECTION_NOT-LANDED_S87_FAIL_byte_
                       exact_replacement_blocked_class_c_pin_drift'
"""

import hashlib
import json
import sys
from pathlib import Path

_THIS = Path(__file__).resolve()
_REPO = _THIS.parent.parent.parent
sys.path.insert(0, str(_REPO / "computations" / "_shared"))
from canonical_constants import tau_fold, c_sub_baseline  # noqa: E402,F401


def file_sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def closure_hash(d: dict) -> str:
    return hashlib.sha256(json.dumps(d, sort_keys=True, default=str).encode()).hexdigest()


def emit_mechanical_closure(
    gate_id: str,
    wp_section: str,
    scheme: str,
    convention: str,
    blocker_label: str,
    blocker_value_phrase: str,
    s87_evidence: str,
    s89_carry_forward_id: str,
    extra_input_files: dict,
):
    verdict_file = _REPO / "computations" / "session-88" / "s88_gate_verdicts.txt"
    plan_path = _REPO / "sessions" / "session-plan" / "session-88-plan-w12.md"
    s87_verdicts_path = _REPO / "computations" / "session-87" / "s87_gate_verdicts.txt"
    mech_closure_rule_path = _REPO / ".claude" / "rules" / "mechanical-closure-discipline.md"

    sha_plan = file_sha256(plan_path)
    sha_s87_verdicts = file_sha256(s87_verdicts_path)
    sha_mech_rule = file_sha256(mech_closure_rule_path)

    input_pin_map = {
        "gate_id": gate_id,
        "wp_section": wp_section,
        "scheme": scheme,
        "convention": convention,
        "blocker_label": blocker_label,
        "s87_evidence": s87_evidence,
        "input_sha_plan": sha_plan,
        "input_sha_s87_verdicts": sha_s87_verdicts,
        "input_sha_mech_rule": sha_mech_rule,
        **extra_input_files,
    }
    audit_sha = closure_hash(input_pin_map)
    content_payload = {
        "composite_verdict": "FAIL",
        "value": blocker_value_phrase,
        "blocker_label": blocker_label,
    }
    content_sha = closure_hash(content_payload)

    canonical_line = (
        f"{gate_id}: FAIL -- "
        f"value='{blocker_value_phrase}' "
        f"scheme={scheme} convention={convention} L_max=10 "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )
    dual_sha = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} # {gate_id} "
        f"dual-SHA companion row (W9a-99 split)\n"
    )
    triple = (
        f"# sign_verdict=N/A magnitude_verdict=FAIL regime_verdict=BREAKDOWN "
        f"# {gate_id} 3-tuple annotation (S87 schema-v2)\n"
    )
    diag = (
        f"# DIAGNOSTIC: mechanical-closure protocol fires per "
        f"mechanical-closure-discipline.md §1. Prereq {blocker_label} "
        f"NOT-PASS-LANDED at session-88 dispatch — S87 evidence: {s87_evidence}. "
        f"Conditional method untestable; honest closure preserves audit trail. "
        f"S89 carry-forward `{s89_carry_forward_id}` registered.\n"
    )

    with open(verdict_file, "a", encoding="utf-8") as fh:
        fh.write(canonical_line)
        fh.write(dual_sha)
        fh.write(triple)
        fh.write(diag)

    return {
        "gate_id": gate_id,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "verdict": "FAIL",
        "value": blocker_value_phrase,
    }


def main():
    print("=" * 72)
    print("S88 W12-139 + W12-140 mechanical-closure audit")
    print("=" * 72)
    print()

    # === §W12-139 ===
    print("[§W12-139] EE-BB-T cross-correlation c_sub probe ...")
    res_139 = emit_mechanical_closure(
        gate_id="S88-EE-BB-T-CROSS-CORRELATION-DIRECT-CSUB-PROBE",
        wp_section="W12-139",
        scheme="EE-BB-T-cross-correlation-mechanical-closure",
        convention="prereq-VII-AJ-W4-1-NOT-PASS-CONDITIONAL-S87-INFO",
        blocker_label="VII-AJ-W4-1_CROSS-PILLAR-3-CHANNEL_NOT-PASS-CONDITIONAL",
        blocker_value_phrase=(
            "PRE-REG-INC_blocked_by_VII-AJ-W4-1_CROSS-PILLAR-3-CHANNEL-"
            "NOT-PASS-CONDITIONAL_S87-CROSS-PILLAR-3-CHANNEL-THEOREM-PROOF_"
            "verdict_INFO_value_1e-2_NOT_PASS_required_for_conditional_method"
        ),
        s87_evidence=(
            "S87-CROSS-PILLAR-3-CHANNEL-THEOREM-PROOF: INFO value=1.0e-2 "
            "scheme=3-channel-x-3-pillar-Connes-Karoubi "
            "convention=substrate-distance-anchored-Mellin L_max=10 "
            "(s87_gate_verdicts.txt; INFO not PASS-conditional → "
            "plan §W12-139 prereq condition unsatisfied)"
        ),
        s89_carry_forward_id="S89-EE-BB-T-CSUB-PROBE-RETRY-POST-VII-AJ-W4-1-LANDING",
        extra_input_files={},
    )
    print(f"  audit_sha256:   {res_139['audit_sha256']}")
    print(f"  content_sha256: {res_139['content_sha256']}")
    print()

    # === §W12-140 ===
    print("[§W12-140] f_NL equilateral non-Gaussianity ...")
    res_140 = emit_mechanical_closure(
        gate_id="S88-F-NL-EQUILATERAL-NON-GAUSSIANITY",
        wp_section="W12-140",
        scheme="GGE-Bogoliubov-fabric-coherent-mechanical-closure",
        convention="prereq-W4-3-NOT-LANDED-S87-FAIL-byte-exact-replacement-blocked",
        blocker_label="W4-3_F-NL-FOLDED-LANGUAGE-CORRECTION_NOT-LANDED",
        blocker_value_phrase=(
            "PRE-REG-INC_blocked_by_W4-3_F-NL-FOLDED-LANGUAGE-CORRECTION_"
            "NOT-LANDED_S87-F-NL-FOLDED-W14-4-LANGUAGE-CORRECTION_verdict_FAIL_"
            "byte_exact_replacement_blocked_class_c_PIN_DRIFT_plan_cited_"
            "locked_text_source_absent"
        ),
        s87_evidence=(
            "S87-F-NL-FOLDED-W14-4-LANGUAGE-CORRECTION: FAIL "
            "value='byte-exact_replacement_blocked_by_class-c_PIN-DRIFT-FROM-"
            "STALE-SOURCE_plan-cited-locked-text-source-absent' "
            "scheme=text-replacement-byte-exact "
            "convention=phononic-framing-reframe-IS-NOT-IN "
            "(s87_gate_verdicts.txt; FAIL → plan §W12-140 prereq "
            "condition 'W4-3 landed' unsatisfied)"
        ),
        s89_carry_forward_id="S89-F-NL-EQUILATERAL-RETRY-POST-W4-3-CORRECTION-LANDING",
        extra_input_files={},
    )
    print(f"  audit_sha256:   {res_140['audit_sha256']}")
    print(f"  content_sha256: {res_140['content_sha256']}")
    print()

    # Verify per-gate-distinct audit_sha256 (sig_5 ladder)
    distinct = res_139["audit_sha256"] != res_140["audit_sha256"]
    print(f"[CC1 sig_5] per-gate-distinct audit_sha256: {distinct}")

    print("\n[done]")
    return 0


if __name__ == "__main__":
    sys.exit(main())
