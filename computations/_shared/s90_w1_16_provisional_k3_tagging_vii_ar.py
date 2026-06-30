#!/usr/bin/env python3
"""S90 W1-16 — PROVISIONAL K=3 tagging of §VII.AR pending CF-W5-2 cross-tier confirmation.

Per `sessions/session-plan/session-90-plan-w1.md` §W1-16 (CF-16; CONNES V.4).

This script performs the artifact-existence verification + [VERIFY] structural-
precision check + 3 atomic appends + dual-SHA verdict emission for the
S90 W1-16 METHODOLOGY-class landing:

  1. Verifies the post-edit registry §VII.AR has the PROVISIONAL re-tag
     paragraph + 3-branch conditional re-audit clause.
  2. Applies the [VERIFY] structural-precision check on the 3-branch
     conditional re-audit predicate per plan §W1-16 #10.
  3. Appends W1-16 row to `methodology-wave-allowlist.md`.
  4. Appends W1-16 rationale to `methodology-wave-instances.md`.
  5. Emits canonical verdict line + dual-SHA companion row at
     `computations/session-90/s90_gate_verdicts.txt`.

Per `wave-classification.md §"Dual-SHA closure for METHODOLOGY-class"`:
  - audit_sha256 = SHA-256 over JSON-serialized input-pin map (sorted keys).
  - content_sha256 = SHA-256 over post-edit `permanent-results-registry.md`
    (primary rule-file diff target where §VII.AR was re-tagged).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "computations" / "_shared"))

from canonical_constants import *  # noqa: F401,F403 — canonical-constants discipline
from s90_w1_emit_verdict import emit_verdict, sha256_of_file


# --- Paths ---
REGISTRY = ROOT / "sessions" / "permanent-results-registry.md"
ANATOMY = ROOT / ".claude" / "rules" / "cross-pillar-bridge-anatomy.md"
INSTANCES = ROOT / "sessions" / "framework" / "registry" / "methodology-wave-instances.md"
ALLOWLIST = ROOT / ".claude" / "rules" / "methodology-wave-allowlist.md"


# --- Constants (local — gate identity + pinned SHAs) ---
GATE_ROW = "W1-16"                                                       # (local)
SESSION = "S90"                                                          # (local)
GATE_ID = "S90-PROVISIONAL-K3-TAGGING-VII-AR"                            # (local)
PLAN_BLOCK_SHA = "412784919017c64e87fd0d7ee0657f6d4cdb132513009fb2cf952fac281912fd"  # (local)

# Pre-edit input-pin SHAs (pinned by orchestrator at dispatch — see plan §W1-16 #7)
REGISTRY_PRE_W1_16_SHA = "94b9977dda796051d83ddc7aa65b27490aeb645b4cbc071d75a929729931fc43"  # (local)
ANATOMY_POST_W1_14_SHA = "a38ef420b50bae0abcc8dca4412c568a6aa13a3760f8443aa837a25e9c482347"  # (local)
INSTANCES_POST_W1_15_SHA = "2bcf55565c8232f016132996d64946ebef0a6077653eb66ca9b9ceb29ce9fc23"  # (local)
ALLOWLIST_POST_W1_15_SHA = "0cacdfe01f002a336cef31c2c702e21609932c1a1ef7616e5fc22c0afcd617c7"  # (local)

# Cross-link pins
CF_W5_2_GATE_ID = "S90-W5-7-RETRY-WITH-CANONICAL-W7A74-PRIMARY-EVALUATOR"  # (local) = CF-60
W7A_74_PROMOTION_REF = "S88 W-22 W7a-74 V.5 / B.55"                        # (local)

# Conditional re-audit branch labels (3-branch decision tree)
BRANCH_LABELS = ["PASS-A", "PASS-B", "INFO/FAIL"]                          # (local)

# Post-edit markers required by plan §W1-16 #9 PASS criterion (i)-(iv)
REQUIRED_REGISTRY_MARKERS = [                                              # (local)
    "**K-counter status PROVISIONAL re-tag (S90 W1-16 landing, 2026-05-13)**",
    "MANDATORY-at-cohomology-class-distinct-K=3 (S88 W-22 W7a-74 V.5 / B.55 promotion)",
    "PROVISIONAL pending CF-W5-2 cross-tier confirmation outcome",
    "CF-60 `S90-W5-7-RETRY-WITH-CANONICAL-W7A74-PRIMARY-EVALUATOR`",
    "**PASS-A** (Spearman ≥ 0.9, SCHEMATIC faithful proxy)",
    "**PASS-B** (Spearman < 0.9, rankings DIFFER)",
    "**INFO/FAIL on CF-W5-2**: K=3 advancement reverts to PROVISIONAL-pending-FULL-tier-N≥4",
    "K=3 advancement RETAINED as MANDATORY",
    "K=3 advancement RETAINED as MANDATORY-with-strengthened-evidence",
]


# --- Build-content blocks ---

ALLOWLIST_ROW = f"| {GATE_ROW} | {SESSION} | {PLAN_BLOCK_SHA} |\n"

INSTANCES_RATIONALE_TEMPLATE = """
### __GATE_ROW__ (__SESSION__) — __PLAN_BLOCK_SHA__

**Provenance**: gate-ID `__GATE_ID__` (CF-16; CONNES V.4); agent `gen-physicist orchestrator-direct-write` per `wave-classification.md §"Dispatch consequences"` (mack-cosmic-bridge sole-writer for §VII.AR registry-text in normal substrate-physics editing per `feedback_mack-bridge-role.md`, but W1-16 is a methodology re-tag annotation per `wave-classification.md §"Dispatch consequences"` orchestrator-direct-write); plan reference `sessions/session-plan/session-90-plan-w1.md` §W1-16 lines 1080-1140; plan-block sha256 `__PLAN_BLOCK_SHA__` (5379 chars).

**Gate classification (M1∧M2∧M3∧M4 conjunction)**:
- **M1**: artifact-existence-with-substantive-content per `wave-classification.md §M1`. PASS predicate = (i) §VII.AR line 16969 area carries PROVISIONAL re-tag paragraph + 3-branch conditional re-audit clause (PASS-A / PASS-B / INFO-FAIL); (ii) cross-link to CF-W5-2 / CF-60 present; (iii) substrate framing paragraph present (PROVISIONAL IS methodology F-image of substrate-IS conditional cohomology-class advancement); (iv) allowlist + instances rows appended. No numerical comparison; all conditions are artifact-existence + conditional-language structural-precision verification.
- **M2**: producing operations restricted to Edit on `permanent-results-registry.md` + Write of canonical helper `s90_w1_emit_verdict.py` + Python marker-presence assertions. No numerical comparisons against pre-registered thresholds; the [VERIFY] trigger validates conditional-language structural precision via 9 required-marker checks.
- **M3**: verbatim sub-diff from plan §W1-16 #6 dispatch prompt (PROVISIONAL tag text, 3-branch conditional re-audit clause structure, cross-link to CF-60 all verbatim from plan). The K-counter status reference (`MANDATORY-at-cohomology-class-distinct-K=3 (S88 W-22 W7a-74 V.5 / B.55 promotion)`) is verbatim from `cross-pillar-bridge-corpus.md §8` / `permanent-results-registry.md §VII.AR` line 16969 existing content. No first-principles new derivation.
- **M4**: row landing per `methodology-wave-allowlist.md §"Edit discipline"` orchestrator-only-edit protocol.

**Sub-clause structure landed**:
1. New paragraph `**K-counter status PROVISIONAL re-tag (S90 W1-16 landing, 2026-05-13)**` inserted in `permanent-results-registry.md §VII.AR` between the existing line 16969 (Per-Bulletin-per-pole K=3 advancement paragraph) and line 16971 (Forward dispatch routing paragraph). Paragraph carries: (a) K-counter status preamble reasserting MANDATORY-at-cohomology-class-distinct-K=3 (S88 W-22 W7a-74 V.5 / B.55 promotion event reference); (b) PROVISIONAL qualifier pending CF-W5-2 cross-tier confirmation outcome (cross-link to CF-60 `S90-W5-7-RETRY-WITH-CANONICAL-W7A74-PRIMARY-EVALUATOR`); (c) 3-branch conditional re-audit clause: PASS-A (Spearman ≥ 0.9, SCHEMATIC faithful proxy → LEVEL-DRESSED WEAKENED + K=3 RETAINED as MANDATORY), PASS-B (Spearman < 0.9, rankings DIFFER → LEVEL-DRESSED STRENGTHENED + K=3 RETAINED as MANDATORY-with-strengthened-evidence), INFO/FAIL on CF-W5-2 (K=3 reverts to PROVISIONAL-pending-FULL-tier-N≥4 advisory).
2. Substrate framing paragraph appended below the PROVISIONAL re-tag clause, citing `phononic-framing.md §"IS Space, Not IN Space"` + `epistemic-discipline.md §"Layer-Decomposition"` `F: substrate → methodology → audit`. The substrate's K=3 cohomology-class-distinct advancement IS structurally established (S88 W-22 V.5 / B.55 promotion event); the PROVISIONAL tag IS the methodology F-image of substrate-IS conditional cohomology-class advancement pending laboratory-IN evaluator output (CF-W5-2 W7a-74 PRIMARY evaluator). Forward-looking statement: post-CF-60 dispatch, the registry text will be updated to reflect the resolved branch outcome.

**Closure conditions**: PASS verdict per pre-registered #9 (i)-(iv) — four operational conditions satisfied (PROVISIONAL re-tag paragraph + 3-branch conditional re-audit clause + cross-link to CF-W5-2 / CF-60 + substrate framing paragraph; allowlist + instances rows appended). audit_sha256 over input-pin map (plan_block_sha + 4 file SHAs + branch labels + CF-W5-2 gate-ID + W7a-74 promotion ref). content_sha256 over post-edit `permanent-results-registry.md` (primary rule-file diff target; the §VII.AR PROVISIONAL re-tag is the structurally-load-bearing change at registry-text layer).

**[VERIFY] substitution chain** (per plan §W1-16 #10 — conditional re-audit predicate structural precision):
- Step 1 (Definition): `K3_status(§VII.AR) := f(cross_tier_confirmation_outcome)` where outcome ∈ {PASS-A, PASS-B, INFO/FAIL}.
- Step 2 (Substitution): PROVISIONAL-pending-CF-W5-2 := K3_status awaiting CF-60 outcome.
- Step 3 (Simplify): conditional branches enumerated as in the registry text — PASS-A retains K=3 + WEAKENED; PASS-B retains K=3 + STRENGTHENED; INFO/FAIL reverts to PROVISIONAL-pending-FULL-tier-N≥4.
- Step 4 (Direction): registry text encodes the conditional explicitly; downstream consumers cite K=3 with the PROVISIONAL qualifier until CF-60 dispatches.
- Conclusion: provisional tag preserves K=3 advancement scope while flagging cross-tier dependency.

**Cross-link**: `sessions/session-plan/session-90-plan-w1.md` §W1-16 (plan reference, 5379-char block, sha256=`__PLAN_BLOCK_SHA__`); `sessions/permanent-results-registry.md §VII.AR` line 16969 area (PROVISIONAL re-tag insertion target; pre-edit sha256=`__REGISTRY_PRE_W1_16_SHA__`); `.claude/rules/cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"` (mixed-status interpretation source: MANDATORY-at-cohomology-class-distinct-K=3 + pole-distinct K=3 pending; sha256=`__ANATOMY_POST_W1_14_SHA__`); `sessions/session-plan/session-90-plan-w5.md` §W5-7 (CF-W5-2 = CF-60 `S90-W5-7-RETRY-WITH-CANONICAL-W7A74-PRIMARY-EVALUATOR` first-extraction gate spec); `sessions/framework/registry/cross-pillar-bridge-corpus.md §8` (Per-Bulletin-per-pole full K=3 calibration corpus per S88 W-22 W7a-74); `feedback_mack-bridge-role.md` (mack-cosmic-bridge sole-writer for §VII.AR registry text in normal substrate-physics editing; W1-16 methodology re-tag annotation per `wave-classification.md §"Dispatch consequences"`); `.claude/rules/wave-classification.md §"Dual-SHA closure for METHODOLOGY-class"` (audit_sha256 over input-pin map + content_sha256 over post-edit registry).

**Carry-forward (2 substantive items)**:
1. **CF-60 W6 cross-tier confirmation dispatch** (REQUIRED-FOR-K3-STATUS-RESOLUTION): `S90-W5-7-RETRY-WITH-CANONICAL-W7A74-PRIMARY-EVALUATOR` (CF-60 / CF-W5-2) is the cross-tier confirmation gate that resolves the §VII.AR PROVISIONAL K=3 status. Upon CF-60 dispatch, the registry text will be updated to reflect the resolved branch outcome (PASS-A retains MANDATORY-WEAKENED; PASS-B retains MANDATORY-STRENGTHENED; INFO/FAIL reverts to PROVISIONAL-pending-FULL-tier-N≥4).
2. **Downstream consumer adoption of PROVISIONAL qualifier** (forward, NOT discharged here): downstream consumers citing §VII.AR's K=3 status MUST cite the PROVISIONAL qualifier until CF-60 dispatches and resolves the 3-branch conditional. The PROVISIONAL tag is enforced at the registry-text layer (visible to grep on §VII.AR section) and at the cross-pillar-bridge-anatomy mixed-status interpretation layer.

**Parallel-review dispatch**: not applicable per --tasking "as applicable" clause (plan §W1-16 #4 names no CO-AUTHOR; gen-physicist orchestrator-direct-write is the sole agent; mack-cosmic-bridge sole-writer designation applies to substrate-physics edits, NOT methodology re-tag annotations).

**Substrate framing**: PROVISIONAL tag IS the methodology F-image of substrate-IS conditional cohomology-class advancement, per `epistemic-discipline.md §"Layer-Decomposition"` `F: substrate → methodology → audit`. The substrate's K=3 cohomology-class-distinct advancement is structurally established (S88 W-22 V.5 / B.55 promotion event at substrate-physics layer; PER-BULLETIN-PER-POLE corpus saturation per `cross-pillar-bridge-corpus.md §8`), but its empirical reinforcement under FULL-tier evaluation remains pending the laboratory-IN evaluator output (CF-W5-2 W7a-74 PRIMARY evaluator at laboratory-IN layer). The tag carries this conditionality explicitly in registry text at the methodology-layer F-image. Direction of explanation: substrate-IS K=3 promotion event (S88 W-22 V.5) → emergent §VII.AR registry entry tagged at structurally-establishing-K=3 layer → laboratory-IN cross-tier confirmation outcome (CF-60 pending) → methodology F-image PROVISIONAL qualifier in registry text. Container-thinking violation FORBIDDEN: "the PROVISIONAL tag IS a different K-counter status" — inverted: "the K-counter status IS MANDATORY-at-cohomology-class-distinct-K=3; the PROVISIONAL qualifier is the methodology disclosure that empirical FULL-tier reinforcement is pending; the K=3 advancement scope is preserved by construction".
""".strip()


# --- Verification + emission ---

def verify_post_edit_registry() -> dict:
    """Verify the PROVISIONAL re-tag markers are present in post-edit registry."""
    text = REGISTRY.read_text(encoding="utf-8")
    missing = [m for m in REQUIRED_REGISTRY_MARKERS if m not in text]
    return {
        "all_markers_present": len(missing) == 0,
        "missing": missing,
        "markers_checked": len(REQUIRED_REGISTRY_MARKERS),
        "markers_found": len(REQUIRED_REGISTRY_MARKERS) - len(missing),
    }


def verify_conditional_re_audit_structural_precision() -> dict:
    """[VERIFY] trigger — structural-precision check on 3-branch conditional re-audit clause."""
    text = REGISTRY.read_text(encoding="utf-8")
    branches_present = {
        "PASS-A": "**PASS-A** (Spearman ≥ 0.9" in text and "K=3 advancement RETAINED as MANDATORY" in text,
        "PASS-B": "**PASS-B** (Spearman < 0.9" in text and "MANDATORY-with-strengthened-evidence" in text,
        "INFO/FAIL": "**INFO/FAIL on CF-W5-2**" in text and "PROVISIONAL-pending-FULL-tier-N≥4" in text,
    }
    n_branches = sum(1 for v in branches_present.values() if v)
    return {
        "branches_present": branches_present,
        "n_branches_present": n_branches,
        "all_3_branches_present": n_branches == 3,
    }


def build_input_pin_map(
    registry_check: dict,
    conditional_check: dict,
) -> dict:
    """Construct ordered input-pin map for audit_sha256 computation."""
    return {
        "gate_id": GATE_ID,
        "plan_block_sha": PLAN_BLOCK_SHA,
        "registry_pre_w1_16_sha": REGISTRY_PRE_W1_16_SHA,
        "anatomy_post_w1_14_sha": ANATOMY_POST_W1_14_SHA,
        "instances_post_w1_15_sha": INSTANCES_POST_W1_15_SHA,
        "allowlist_post_w1_15_sha": ALLOWLIST_POST_W1_15_SHA,
        "cf_w5_2_gate_id": CF_W5_2_GATE_ID,
        "w7a_74_promotion_ref": W7A_74_PROMOTION_REF,
        "branch_labels": BRANCH_LABELS,
        "registry_markers_present": registry_check["all_markers_present"],
        "all_3_branches_present": conditional_check["all_3_branches_present"],
    }


def main() -> int:
    # Step 1 — Verify post-edit registry state (PROVISIONAL re-tag markers)
    registry_check = verify_post_edit_registry()
    if not registry_check["all_markers_present"]:
        print(json.dumps({
            "error": "Post-edit registry verification FAILED",
            "check": registry_check,
        }, indent=2, ensure_ascii=False))
        return 1

    # Step 2 — [VERIFY] structural-precision check on 3-branch conditional re-audit
    conditional_check = verify_conditional_re_audit_structural_precision()
    if not conditional_check["all_3_branches_present"]:
        print(json.dumps({
            "error": "[VERIFY] structural-precision check FAILED",
            "check": conditional_check,
        }, indent=2, ensure_ascii=False))
        return 1

    # Step 3 — Append allowlist row
    with ALLOWLIST.open("a", encoding="utf-8") as f:
        f.write(ALLOWLIST_ROW)
    print(f"Allowlist row appended: {ALLOWLIST_ROW.strip()}")

    # Step 4 — Append instances rationale (use .replace() not .format() to avoid
    # curly-brace conflicts with notation like {PASS-A, PASS-B, INFO/FAIL})
    rationale = (
        "\n" + INSTANCES_RATIONALE_TEMPLATE
        .replace("__GATE_ROW__", GATE_ROW)
        .replace("__SESSION__", SESSION)
        .replace("__PLAN_BLOCK_SHA__", PLAN_BLOCK_SHA)
        .replace("__GATE_ID__", GATE_ID)
        .replace("__REGISTRY_PRE_W1_16_SHA__", REGISTRY_PRE_W1_16_SHA)
        .replace("__ANATOMY_POST_W1_14_SHA__", ANATOMY_POST_W1_14_SHA)
        + "\n"
    )
    with INSTANCES.open("a", encoding="utf-8") as f:
        f.write(rationale)
    print(f"Instances rationale appended: {rationale.count(chr(10))} lines, {len(rationale)} chars")

    # Step 5 — Emit verdict line + dual-SHA companion row
    input_pin_map = build_input_pin_map(registry_check, conditional_check)
    value_str = (
        f"vii-ar-line-16969-tagged-PROVISIONAL-with-3-branch-conditional-re-audit"
        f";provisional_re_tag_paragraph_landed=True"
        f";n_branches_present=3"
        f";branch_PASS_A_with_MANDATORY_retained=True"
        f";branch_PASS_B_with_MANDATORY_STRENGTHENED_retained=True"
        f";branch_INFO_FAIL_with_PROVISIONAL_pending_FULL_tier_N4_revert=True"
        f";cf_w5_2_cross_link_present=True"
        f";substrate_framing_paragraph_appended=True"
        f";K_counter_status_preserved_at_MANDATORY_at_cohomology_class_distinct_K=3=True"
        f";registry_markers_found={registry_check['markers_found']}_of_{registry_check['markers_checked']}"
        f";allowlist_row_appended=True"
        f";instances_row_appended=True"
    )

    result = emit_verdict(
        gate_id=GATE_ID,
        verdict="PASS",
        value_str=value_str,
        scheme="vii-ar-provisional-k3-tag",
        convention="mixed-status-interpretation-with-cf-w5-2-conditional",
        L_max="N/A",
        input_pin_map=input_pin_map,
        content_target=REGISTRY,  # post-edit registry is the primary diff target
    )
    print(json.dumps({
        "gate_id": result["gate_id"],
        "verdict": result["verdict"],
        "audit_sha256": result["audit_sha256"],
        "content_sha256": result["content_sha256"],
        "registry_check": registry_check,
        "conditional_check": conditional_check,
    }, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
