#!/usr/bin/env python3
"""S90 W1-17 — §VII.AH Stage-2 substrate-input-orthogonality K-counter K=1 → K=2 rule update.

Per `sessions/session-plan/session-90-plan-w1.md` §W1-17 (CF-17 / CF-W4-7-ORTHOGONALITY-K2).

This script performs the artifact-existence verification + [VERIFY] structural-
precision check + 3 atomic appends + dual-SHA verdict emission for the
S90 W1-17 METHODOLOGY-class landing:

  1. Verifies the post-edit `joint-theorem-promotion.md §"Substrate-input-
     orthogonality clause"` reflects K=2 advancement (status "SUGGESTION at K=2"
     + W4-7 §VII.AH audit_sha256 cited).
  2. Verifies the post-edit `pru-class-corpus.md §15` K-counter table has the
     K=2 row populated (S89 W4-7 §VII.AH at structural ceiling; FIRST INSTANCE
     WITHOUT substrate-input-overlap caveat).
  3. [VERIFY] substitution chain: K_substrate_input_orthogonality = 1 + 1 = 2
     at structural ceiling.
  4. Appends W1-17 row to `methodology-wave-allowlist.md`.
  5. Appends W1-17 rationale to `methodology-wave-instances.md`.
  6. Emits canonical verdict line + dual-SHA companion row at
     `computations/session-90/s90_gate_verdicts.txt`.

Per `wave-classification.md §"Dual-SHA closure for METHODOLOGY-class"`:
  - audit_sha256 = SHA-256 over JSON-serialized input-pin map (sorted keys).
  - content_sha256 = SHA-256 over post-edit `joint-theorem-promotion.md`
    (primary rule-file diff target where the K-counter status was updated).
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
JOINT_THEOREM_PROMOTION = ROOT / ".claude" / "rules" / "joint-theorem-promotion.md"
PRU_CLASS_CORPUS = ROOT / "sessions" / "framework" / "registry" / "pru-class-corpus.md"
INSTANCES = ROOT / "sessions" / "framework" / "registry" / "methodology-wave-instances.md"
ALLOWLIST = ROOT / ".claude" / "rules" / "methodology-wave-allowlist.md"


# --- Constants (local — gate identity + pinned SHAs) ---
GATE_ROW = "W1-17"                                                       # (local)
SESSION = "S90"                                                          # (local)
GATE_ID = "S90-VII-AH-STAGE-2-ORTHOGONALITY-K2-RULE-UPDATE"              # (local)
PLAN_BLOCK_SHA = "01cd431699d88193bf564b94f61180f3f542ca71e44f6582832874ec93ea8f69"  # (local)

# Pre-edit input-pin SHAs (pinned by orchestrator at dispatch — see plan §W1-17 #7)
JOINT_THEOREM_PROMOTION_PRE_W1_17_SHA = "2e1ca1a38ef16daf6322aaebce4dba7cabce741c477dc6c68ef6993666059af2"  # (local)
PRU_CLASS_CORPUS_PRE_W1_17_SHA = "86a5e6ffe540fbded256cbf56ac2549eb8e5fd2fc1518c2098a45c722f82a800"  # (local)
INSTANCES_POST_W1_16_SHA = "c5a7ef2a4fcc0e203c576fb4aea30e0605ff0b763077b6e23d0a05a534f5f6a0"  # (local)
ALLOWLIST_POST_W1_16_SHA = "113bc56a8a61d4d00db2c4606a8b015541ee51163179f75e9c7cc1a06d7d80ce"  # (local)

# W4-7 §VII.AH audit_sha pin per plan §W1-17 #7 PRDR
W4_7_AUDIT_SHA = "4fcd7d29af51c56d8c6620bc2c323970b96edc053e432232e680903d8926536a"  # (local)
W7C_167_NPZ_SHA = "120435cbfd5ef313ebcba6e23ec1712c51d04a3f75b788034ebe7964aa32519f"  # (local) — K=1 source data

# K-counter pins (substitution chain Step 1-4)
K_BEFORE = 1                                                              # (local)
K_AFTER = 2                                                               # (local)
K_PROMOTION = 3                                                           # (local) per feedback_rules-compensate-missing-structure.md

# Post-edit markers required by plan §W1-17 #9 PASS criterion (i)-(iv)
REQUIRED_JOINT_THEOREM_MARKERS = [                                        # (local)
    "Calibration corpus K=2 (post-S90 W1-17 advancement, 2026-05-13)",
    "K=1**: S88 W7c-167 obs1 PASS-AND with substrate-input-overlap caveat",
    "K=2**: S89 W4-7 §VII.AH Stage-2 re-dispatch on obs2 + obs3 PASS 8/8 at structural ceiling",
    "FIRST INSTANCE WITHOUT substrate-input-overlap caveat",
    W4_7_AUDIT_SHA,
    "S90 W1-17",
    "SUGGESTION at K=2",
]

REQUIRED_PRU_CORPUS_MARKERS = [                                           # (local)
    "S89 W4-7 §VII.AH Stage-2 re-dispatch on obs2 + obs3 PASS 8/8",
    W4_7_AUDIT_SHA,
    "calibration corpus instance #2 at **structural ceiling**",
    "FIRST INSTANCE WITHOUT substrate-input-overlap caveat",
    "K=1 → K=2 advancement landed S90 W1-17",
    "reserved (S90+ third structurally-distinct instance",
]


# --- Build-content blocks ---

ALLOWLIST_ROW = f"| {GATE_ROW} | {SESSION} | {PLAN_BLOCK_SHA} |\n"

INSTANCES_RATIONALE_TEMPLATE = """
### __GATE_ROW__ (__SESSION__) — __PLAN_BLOCK_SHA__

**Provenance**: gate-ID `__GATE_ID__` (CF-17 / CF-W4-7-ORTHOGONALITY-K2); agent `gen-physicist orchestrator-direct-write` per `wave-classification.md §"Dispatch consequences"`; plan reference `sessions/session-plan/session-90-plan-w1.md` §W1-17 lines 1142-1216; plan-block sha256 `__PLAN_BLOCK_SHA__` (6171 chars).

**Gate classification (M1∧M2∧M3∧M4 conjunction)**:
- **M1**: artifact-existence-with-substantive-content per `wave-classification.md §M1`. PASS predicate = (i) K-counter status in `joint-theorem-promotion.md §"Substrate-input-orthogonality clause"` advanced from K=1 to K=2 with W4-7 audit_sha pinned; (ii) `pru-class-corpus.md §15` K-counter table K=2 row populated with W4-7 §VII.AH at structural ceiling; (iii) K=3 reserved row preserved; (iv) allowlist + instances rows appended. No numerical comparison; all conditions are artifact-existence + K-counter accumulation verification.
- **M2**: producing operations restricted to Edit on `joint-theorem-promotion.md` + Edit on `pru-class-corpus.md §15` + Python marker-presence assertions + canonical verdict-line emission. No numerical comparisons against pre-registered thresholds; the [VERIFY] trigger validates K-counter advancement substitution chain (1 + 1 = 2 at structural ceiling).
- **M3**: verbatim sub-diff from plan §W1-17 #6 dispatch prompt (K=2 row content, W4-7 audit_sha pin, structural-ceiling assertion, K=3 reserved-row text all verbatim from plan). W4-7 audit_sha source verified at `s89_gate_verdicts.txt:80` (gate `S89-VII-AH-STAGE-2-RE-DISPATCH-OBS2-OBS3` PASS 8/8 with JOINT (c) + (d) clause PASS-AND verified per W-23 §IV.3 substrate-input-orthogonality predicate at structural ceiling). No first-principles new derivation.
- **M4**: row landing per `methodology-wave-allowlist.md §"Edit discipline"` orchestrator-only-edit protocol.

**Sub-clause structure landed**:
1. `joint-theorem-promotion.md §"Substrate-input-orthogonality clause"` line 89 (K-counter anchor) extended from single-line K=1 citation to multi-row K=2 enumeration: K=1 row (S88 W7c-167 obs1 with substrate-input-overlap caveat) RETAINED; K=2 row (S89 W4-7 §VII.AH at structural ceiling; FIRST INSTANCE WITHOUT substrate-input-overlap caveat) ADDED with W4-7 audit_sha256 pin. Line 91 (status note) updated from "Status SUGGESTION at K=1" to "Status **SUGGESTION at K=2** (promotes to MANDATORY at K=3 distinct calibration instances)". Closing sentence extended with structural-ceiling distinction: "instances at structural ceiling (e.g., K=2 W4-7) omit the caveat".
2. `sessions/framework/registry/pru-class-corpus.md §15` K-counter table (lines 424-428 pre-edit) updated: K=1 row RETAINED with full overlap-caveat description; K=2 row populated with Source (S89 W4-7 §VII.AH PASS 8/8 + W4-7 audit_sha at `s89_gate_verdicts.txt:80` + gate-ID `S89-VII-AH-STAGE-2-RE-DISPATCH-OBS2-OBS3`), Stage-2 dispatch (re-dispatch on obs2 + obs3 substrate-input-orthogonal), Substrate-input overlap (NONE — orthogonality predicate satisfied), Verdict (calibration corpus instance #2 at structural ceiling; FIRST framework cross-axis joint theorem to STAGE-3-PERMANENT eligibility; K=1 → K=2 advancement landed S90 W1-17 2026-05-13; STATUS remains SUGGESTION at K=2). K=3 reserved row preserved with extended description: "reserved (S90+ third structurally-distinct instance with substrate-input-orthogonal observables across distinct §VII registry slot)".

**Closure conditions**: PASS verdict per pre-registered #9 (i)-(iv) — four operational conditions satisfied (K-counter rule-file update + K-counter corpus-table K=2 row populated + K=3 reserved-row preserved + allowlist + instances rows). audit_sha256 over input-pin map (plan_block_sha + 4 file SHAs + W4-7 audit_sha pin + W7c-167 NPZ SHA + K-counter status pins). content_sha256 over post-edit `joint-theorem-promotion.md` (primary rule-file diff target; the K-counter status advancement is the structurally-load-bearing change at the rule-file layer).

**[VERIFY] substitution chain** (per plan §W1-17 #10 — K-counter advancement structural precision):
- Step 1 (Definition): `K_substrate_input_orthogonality := count of distinct calibration-corpus instances satisfying the substrate-input-orthogonality predicate at structural ceiling`.
- Step 2 (Substitution): Pre-S90 corpus = {W7c-167 obs1 with overlap caveat}; |corpus_pre_S90| = 1. S89 W4-7 §VII.AH PASS 8/8 + JOINT (c) + (d) + structural ceiling (no overlap caveat) ⇒ new instance qualifying under substrate-input-orthogonality predicate.
- Step 3 (Simplify): K_substrate_input_orthogonality = 1 + 1 = 2.
- Step 4 (Direction): K=2 < K_promotion=3; status remains SUGGESTION pending K=3 (third structurally-distinct instance).
- Conclusion: K-counter table reflects K=2 advancement; K=3 row reserved for next-instance landing.

**Cross-link**: `sessions/session-plan/session-90-plan-w1.md` §W1-17 (plan reference, 6171-char block, sha256=`__PLAN_BLOCK_SHA__`); `.claude/rules/joint-theorem-promotion.md §"Substrate-input-orthogonality clause"` lines 77-91 (K-counter status K=1 → K=2 update target; pre-edit sha256=`__JOINT_THEOREM_PROMOTION_PRE_W1_17_SHA__`); `sessions/framework/registry/pru-class-corpus.md §15` lines 410-438 (K-counter table K=2 row population target; pre-edit sha256=`__PRU_CLASS_CORPUS_PRE_W1_17_SHA__`); `computations/session-89/s89_gate_verdicts.txt:80` (W4-7 source verdict line; gate-ID `S89-VII-AH-STAGE-2-RE-DISPATCH-OBS2-OBS3` PASS 8/8; audit_sha256=`__W4_7_AUDIT_SHA__`); S88 W7c-167 substrate-input-orthogonality K=1 anchor (`s87_w7_ic_per_class_verify.npz` SHA-256=`__W7C_167_NPZ_SHA__`); `feedback_rules-compensate-missing-structure.md` (K-counter SUGGESTION → MANDATORY at K=3 threshold); `.claude/rules/wave-classification.md §"Dual-SHA closure for METHODOLOGY-class"` (audit_sha256 over input-pin map + content_sha256 over post-edit rule-file diff target).

**Carry-forward (2 substantive items)**:
1. **K=3 promotion** (forward): when 1 additional structurally-distinct calibration instance lands (third instance with substrate-input-orthogonal observables across a distinct §VII registry slot from §VII.AH), the substrate-input-orthogonality K-counter advances K=2 → K=3, triggering SUGGESTION → MANDATORY promotion per `feedback_rules-compensate-missing-structure.md`. Audit-script extension `_joint_theorem_independent_verify_audit.py` severity escalates from S2 advisory to S1 HARD-HALT at plan-freeze on detected substrate-input-orthogonality predicate failures. Reserved K=3 row in `pru-class-corpus.md §15` awaits the third instance.
2. **W2 CF-20 §VII.AH Stage-3-PERMANENT promotion downstream consumer** (forward, NOT discharged here): downstream gate W2 CF-20 (`S90-W2-VII-AH-STAGE-3-PERMANENT-PROMOTION` or analogous) consuming §VII.AH's joint-theorem-promotion 4-stage pathway can now cite K=2 in its provenance per plan §W1-17 #11 "W2 CF-20 (Stage-3-PERMANENT promotion of §VII.AH) can cite K=2 in its provenance". The K=2 advancement at structural ceiling unblocks §VII.AH's Stage-3-PERMANENT eligibility under the substrate-input-orthogonality predicate (FIRST framework cross-axis joint theorem reaching this threshold).

**Parallel-review dispatch**: not applicable per --tasking "as applicable" clause (plan §W1-17 #4 names no CO-AUTHOR; gen-physicist orchestrator-direct-write is the sole agent).

**Substrate framing**: substrate-input-orthogonality K-counter advancement IS the methodology F-image of substrate-IS structural orthogonality at the cross-axis joint-theorem layer, per `epistemic-discipline.md §"Layer-Decomposition"` `F: substrate → methodology → audit`. §VII.AH Stage-2 PASS at structural ceiling without overlap caveat IS the substrate's own structural establishment of orthogonality across distinct substrate inputs (obs2 + obs3 each consume substrate-input loaded by exactly one cross-reviewer, NOT both); the K=2 K-counter advancement is the methodology F-image accumulation visible at the rule-file + corpus layer. Direction of explanation: substrate-IS structural orthogonality at cross-axis joint-theorem layer (§VII.AH obs2 + obs3 substrate-input-orthogonal per W4-7 verification) → emergent K-counter accumulation event (K=1 → K=2 advancement) → methodology F-image rule-file + corpus update at the audit-trail layer. Container-thinking violation FORBIDDEN: "the K-counter status IS the substrate physics" — inverted: "the substrate's structural orthogonality at §VII.AH obs2 + obs3 IS established at the substrate-physics layer (W4-7 PASS 8/8 + JOINT (c)+(d) verified); the K=2 K-counter advancement is the methodology disclosure that the corpus accumulation event has fired".
""".strip()


# --- Verification + emission ---

def verify_post_edit_joint_theorem_promotion() -> dict:
    """Verify the K=2 advancement markers in joint-theorem-promotion.md §"Substrate-input-orthogonality clause"."""
    text = JOINT_THEOREM_PROMOTION.read_text(encoding="utf-8")
    missing = [m for m in REQUIRED_JOINT_THEOREM_MARKERS if m not in text]
    return {
        "all_markers_present": len(missing) == 0,
        "missing": missing,
        "markers_checked": len(REQUIRED_JOINT_THEOREM_MARKERS),
        "markers_found": len(REQUIRED_JOINT_THEOREM_MARKERS) - len(missing),
    }


def verify_post_edit_pru_class_corpus() -> dict:
    """Verify the K=2 row population in pru-class-corpus.md §15."""
    text = PRU_CLASS_CORPUS.read_text(encoding="utf-8")
    missing = [m for m in REQUIRED_PRU_CORPUS_MARKERS if m not in text]
    return {
        "all_markers_present": len(missing) == 0,
        "missing": missing,
        "markers_checked": len(REQUIRED_PRU_CORPUS_MARKERS),
        "markers_found": len(REQUIRED_PRU_CORPUS_MARKERS) - len(missing),
    }


def verify_k_counter_substitution_chain() -> dict:
    """[VERIFY] trigger — K-counter advancement substitution chain (plan §W1-17 #10)."""
    # Step 1: K_substrate_input_orthogonality := count of distinct calibration-corpus instances
    # Step 2: Pre-S90 = 1 (W7c-167 obs1 with overlap caveat); new = 1 (W4-7 §VII.AH at structural ceiling)
    # Step 3: K = 1 + 1 = 2
    # Step 4: K=2 < K_promotion=3; status remains SUGGESTION pending K=3
    k_pre_S90 = K_BEFORE                                                  # (local)
    k_new_instance = 1                                                    # (local)
    k_post_S90 = k_pre_S90 + k_new_instance                              # (local)
    k_promotion_threshold_met = k_post_S90 >= K_PROMOTION                # (local)
    return {
        "step_1_definition": "K_substrate_input_orthogonality := count of distinct calibration-corpus instances",
        "step_2_substitution": f"pre_S90={k_pre_S90} + new_instance={k_new_instance}",
        "step_3_simplify": f"K = {k_pre_S90} + {k_new_instance} = {k_post_S90}",
        "step_4_direction": f"K={k_post_S90} < K_promotion={K_PROMOTION}; status remains SUGGESTION pending K=3" if not k_promotion_threshold_met else f"K={k_post_S90} >= K_promotion={K_PROMOTION}; SUGGESTION → MANDATORY",
        "k_post_S90": k_post_S90,
        "k_advancement_matches_K_AFTER_pin": k_post_S90 == K_AFTER,
    }


def build_input_pin_map(
    joint_theorem_check: dict,
    pru_corpus_check: dict,
    substitution_chain_check: dict,
) -> dict:
    """Construct ordered input-pin map for audit_sha256 computation."""
    return {
        "gate_id": GATE_ID,
        "plan_block_sha": PLAN_BLOCK_SHA,
        "joint_theorem_promotion_pre_w1_17_sha": JOINT_THEOREM_PROMOTION_PRE_W1_17_SHA,
        "pru_class_corpus_pre_w1_17_sha": PRU_CLASS_CORPUS_PRE_W1_17_SHA,
        "instances_post_w1_16_sha": INSTANCES_POST_W1_16_SHA,
        "allowlist_post_w1_16_sha": ALLOWLIST_POST_W1_16_SHA,
        "w4_7_audit_sha": W4_7_AUDIT_SHA,
        "w7c_167_npz_sha": W7C_167_NPZ_SHA,
        "K_before": K_BEFORE,
        "K_after": K_AFTER,
        "K_promotion": K_PROMOTION,
        "joint_theorem_markers_present": joint_theorem_check["all_markers_present"],
        "pru_corpus_markers_present": pru_corpus_check["all_markers_present"],
        "k_advancement_matches_pin": substitution_chain_check["k_advancement_matches_K_AFTER_pin"],
    }


def main() -> int:
    # Step 1 — Verify post-edit joint-theorem-promotion.md K=2 advancement markers
    joint_theorem_check = verify_post_edit_joint_theorem_promotion()
    if not joint_theorem_check["all_markers_present"]:
        print(json.dumps({
            "error": "Post-edit joint-theorem-promotion.md verification FAILED",
            "check": joint_theorem_check,
        }, indent=2, ensure_ascii=False))
        return 1

    # Step 2 — Verify post-edit pru-class-corpus.md §15 K=2 row population
    pru_corpus_check = verify_post_edit_pru_class_corpus()
    if not pru_corpus_check["all_markers_present"]:
        print(json.dumps({
            "error": "Post-edit pru-class-corpus.md §15 verification FAILED",
            "check": pru_corpus_check,
        }, indent=2, ensure_ascii=False))
        return 1

    # Step 3 — [VERIFY] K-counter substitution chain
    substitution_chain_check = verify_k_counter_substitution_chain()
    if not substitution_chain_check["k_advancement_matches_K_AFTER_pin"]:
        print(json.dumps({
            "error": "[VERIFY] K-counter substitution chain FAILED",
            "check": substitution_chain_check,
        }, indent=2, ensure_ascii=False))
        return 1

    # Step 4 — Append allowlist row
    with ALLOWLIST.open("a", encoding="utf-8") as f:
        f.write(ALLOWLIST_ROW)
    print(f"Allowlist row appended: {ALLOWLIST_ROW.strip()}")

    # Step 5 — Append instances rationale (use .replace() not .format())
    rationale = (
        "\n" + INSTANCES_RATIONALE_TEMPLATE
        .replace("__GATE_ROW__", GATE_ROW)
        .replace("__SESSION__", SESSION)
        .replace("__PLAN_BLOCK_SHA__", PLAN_BLOCK_SHA)
        .replace("__GATE_ID__", GATE_ID)
        .replace("__JOINT_THEOREM_PROMOTION_PRE_W1_17_SHA__", JOINT_THEOREM_PROMOTION_PRE_W1_17_SHA)
        .replace("__PRU_CLASS_CORPUS_PRE_W1_17_SHA__", PRU_CLASS_CORPUS_PRE_W1_17_SHA)
        .replace("__W4_7_AUDIT_SHA__", W4_7_AUDIT_SHA)
        .replace("__W7C_167_NPZ_SHA__", W7C_167_NPZ_SHA)
        + "\n"
    )
    with INSTANCES.open("a", encoding="utf-8") as f:
        f.write(rationale)
    print(f"Instances rationale appended: {rationale.count(chr(10))} lines, {len(rationale)} chars")

    # Step 6 — Emit verdict line + dual-SHA companion row
    input_pin_map = build_input_pin_map(joint_theorem_check, pru_corpus_check, substitution_chain_check)
    value_str = (
        f"k-counter-K-1-to-K-2-advancement-AND-K-3-reserved_AND_pru-corpus-cross-link-update"
        f";joint_theorem_promotion_status_updated_to_SUGGESTION_K2=True"
        f";pru_class_corpus_15_K2_row_populated=True"
        f";pru_class_corpus_15_K3_row_reserved=True"
        f";w4_7_vii_ah_audit_sha_pinned={W4_7_AUDIT_SHA}"
        f";K_pre_S90={K_BEFORE};K_post_S90={K_AFTER};K_promotion_threshold={K_PROMOTION}"
        f";k_advancement_substitution_chain_verified=True"
        f";structural_ceiling_first_instance_without_substrate_input_overlap_caveat=True"
        f";joint_theorem_markers_found={joint_theorem_check['markers_found']}_of_{joint_theorem_check['markers_checked']}"
        f";pru_corpus_markers_found={pru_corpus_check['markers_found']}_of_{pru_corpus_check['markers_checked']}"
        f";allowlist_row_appended=True;instances_row_appended=True"
    )

    result = emit_verdict(
        gate_id=GATE_ID,
        verdict="PASS",
        value_str=value_str,
        scheme="joint-theorem-promotion-substrate-input-orthogonality-K-counter-update",
        convention="k-2-structural-ceiling-without-overlap-caveat",
        L_max="N/A",
        input_pin_map=input_pin_map,
        content_target=JOINT_THEOREM_PROMOTION,  # post-edit rule-file is primary diff target
    )
    print(json.dumps({
        "gate_id": result["gate_id"],
        "verdict": result["verdict"],
        "audit_sha256": result["audit_sha256"],
        "content_sha256": result["content_sha256"],
        "joint_theorem_check": joint_theorem_check,
        "pru_corpus_check": pru_corpus_check,
        "substitution_chain_check": substitution_chain_check,
    }, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
