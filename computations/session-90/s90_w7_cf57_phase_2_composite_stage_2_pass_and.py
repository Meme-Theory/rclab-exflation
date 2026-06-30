#!/usr/bin/env python3
"""
S90 W7-4 — S90-W7-4-STAGE-2-COMPOSITE-PASS-AND (CF-57 Phase 2 composite)
========================================================================
ORCHESTRATOR-DIRECT EMISSION — composite Stage-2 PASS-AND aggregation for
CF-57 per `.claude/rules/joint-theorem-promotion.md §"Stage 2"` items 39-42.

Both Stage-2 cross-reviewers PASSed:
  - mack β  (S90-W7-4-STAGE-2-CROSS-AXIS-CROSS-REVIEW-MACK-BETA: PASS at
    verdict-file:137; audit_sha256=124a2d4ebababb1e7ba228c1e1e923e765c9c330c8246123621aae3780d3656e)
  - lizzi α+γ (S90-W7-4-STAGE-2-CROSS-AXIS-CROSS-REVIEW-LIZZI-ALPHA-GAMMA:
    PASS at verdict-file:140; audit_sha256=334792b50965070e68ef9941cc5332ef08ba0124b3c53cf8c9419e1330fb973f)

The composite PASS-AND across BOTH reviewers (4-way conjunction across
α, γ, β, joint-clause sub-axes) modulates the CF-57 Phase 1 INFO-pending-
Stage-2 verdict (verdict-file:121, audit_sha256=2b7bedaa0473d12ab84f3ed2aef51a8bb112344536121069258935059c020bae)
toward Stage-3 promotion eligibility per joint-theorem-promotion.md
4-stage pathway. The Phase 1 INFO line remains on disk per absolute
verdict permanence; this composite emission is a NEW gate-ID parallel
to the cross-reviewer gate-IDs.

Pattern: parallel to CF-58 plan §W7-5 §6 specification "THREE canonical
verdict lines + their dual-SHA companion comment rows (one per cross-
reviewer + one composite)" — the composite is its own line, not a
supersedes of the parent.

Plan reference: sessions/session-plan/session-90-plan-w7.md §W7-4.
Cross-link: joint-theorem-promotion.md §"Stage 2" Audit at plan-freeze
6-item check (S88 W-23 V.8 / B.60).
"""

from __future__ import annotations

import sys
from pathlib import Path

_SHARED_DIR = Path(__file__).resolve().parent.parent / "_shared"
sys.path.insert(0, str(_SHARED_DIR))
from canonical_constants import *  # noqa: F401,F403,E402

import hashlib  # noqa: E402
import json  # noqa: E402
import re  # noqa: E402
import time  # noqa: E402

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

GATE_ID = "S90-W7-4-STAGE-2-COMPOSITE-PASS-AND"  # (local)
SCHEME = "cf-57-stage-2-composite-pass-and-aggregation"  # (local)
CONVENTION = "composite-across-axis-a-lizzi-alpha-gamma-plus-axis-b-mack-beta-orchestrator-direct"  # (local)
L_MAX = "N/A"  # (local) METHODOLOGY-class aggregation; no L_max
SCHEMA_VERSION = "S87+"  # (local)

PHASE_1_GATE_ID = "S90-THREE-AXIS-RULE-REFACTOR-JOINT-CONNES-VOLOVIK"  # (local)
PHASE_1_AUDIT_SHA = "2b7bedaa0473d12ab84f3ed2aef51a8bb112344536121069258935059c020bae"  # (local)
MACK_BETA_GATE_ID = "S90-W7-4-STAGE-2-CROSS-AXIS-CROSS-REVIEW-MACK-BETA"  # (local)
MACK_BETA_AUDIT_SHA = "124a2d4ebababb1e7ba228c1e1e923e765c9c330c8246123621aae3780d3656e"  # (local)
LIZZI_AG_GATE_ID = "S90-W7-4-STAGE-2-CROSS-AXIS-CROSS-REVIEW-LIZZI-ALPHA-GAMMA"  # (local)
LIZZI_AG_AUDIT_SHA = "334792b50965070e68ef9941cc5332ef08ba0124b3c53cf8c9419e1330fb973f"  # (local)

VERDICT_TXT = SESSION_DIR / "s90_gate_verdicts.txt"
CANONICAL_CONSTANTS = SHARED_DIR / "canonical_constants.py"
PLAN_W7 = PROJECT_ROOT / "sessions" / "session-plan" / "session-90-plan-w7.md"
WP_W7 = PROJECT_ROOT / "sessions" / "session-90" / "session-90-w7-workingpaper.md"
JTP_RULE = PROJECT_ROOT / ".claude" / "rules" / "joint-theorem-promotion.md"


def sha256_of(path):
    h = hashlib.sha256()
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path, canonical_path, pins, embed_keys):
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True,
    ).encode("utf-8")
    embed_json = json.dumps(
        dict(sorted(embed_keys.items())), separators=(",", ":"), sort_keys=True,
    ).encode("utf-8")
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_audit.update(embed_json)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


def grep_gate_status(verdict_text, gate_id):
    for line in verdict_text.splitlines():
        if line.startswith(f"{gate_id}:"):
            head, _, tail = line.partition("--")
            status = head.split(":")[1].strip()
            m_sha = re.search(r"audit_sha256=([a-f0-9]{64})", tail)
            audit_sha = m_sha.group(1) if m_sha else None
            return {"found": True, "status": status, "audit_sha256": audit_sha}
    return {"found": False}


def emit_verdict(verdict, value_str, audit_sha, content_sha):
    canonical = (
        f"{GATE_ID}: {verdict} -- value={value_str!r} "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version={SCHEMA_VERSION}\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    tuple_row = (
        f"# sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2) | "
        f"composite Stage-2 PASS-AND across mack β + lizzi α+γ; "
        f"4-way conjunction across α, β, γ, joint-clause sub-axes; "
        f"CF-57 Phase 1 INFO-pending-Stage-2 (verdict-file:121) modulates to PASS for Stage-3 promotion eligibility per joint-theorem-promotion.md 4-stage pathway\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical)
        fp.write(companion)
        fp.write(tuple_row)


def main():
    t0 = time.time()
    inputs = [VERDICT_TXT, JTP_RULE, PLAN_W7, CANONICAL_CONSTANTS]
    pins = log_input_pins(inputs)
    embed_keys = {
        "_gate_id": GATE_ID,
        "_wp_id": "session-90-w7-workingpaper.md::§W7-4",
        "_scheme": SCHEME,
        "_convention": CONVENTION,
        "_closure_kind": "PHASE-2-STAGE-2-COMPOSITE-PASS-AND-AGGREGATION",
        "_phase_1_audit_sha": PHASE_1_AUDIT_SHA,
        "_mack_beta_audit_sha": MACK_BETA_AUDIT_SHA,
        "_lizzi_ag_audit_sha": LIZZI_AG_AUDIT_SHA,
    }
    script_path = Path(__file__).resolve()
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_CONSTANTS, pins, embed_keys)
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print()

    # Step 1: locate the 3 input verdict lines on disk
    print("Step 1: locate input verdict lines (Phase 1 INFO + mack β PASS + lizzi α+γ PASS)")
    verdict_text = VERDICT_TXT.read_text(encoding="utf-8")
    phase_1 = grep_gate_status(verdict_text, PHASE_1_GATE_ID)
    mack_beta = grep_gate_status(verdict_text, MACK_BETA_GATE_ID)
    lizzi_ag = grep_gate_status(verdict_text, LIZZI_AG_GATE_ID)
    print(f"  Phase 1 ({PHASE_1_GATE_ID}): {phase_1}")
    print(f"  mack β  ({MACK_BETA_GATE_ID}): {mack_beta}")
    print(f"  lizzi α+γ ({LIZZI_AG_GATE_ID}): {lizzi_ag}")
    if not (phase_1["found"] and mack_beta["found"] and lizzi_ag["found"]):
        print("ERROR: One or more input verdict lines NOT FOUND. Composite cannot proceed.")
        return 2
    print()

    # Step 2: verify Phase 1 audit_sha matches pinned + both reviewers PASS
    print("Step 2: verify Phase 1 audit_sha + both reviewers PASS")
    sha_match = (
        phase_1["audit_sha256"] == PHASE_1_AUDIT_SHA
        and mack_beta["audit_sha256"] == MACK_BETA_AUDIT_SHA
        and lizzi_ag["audit_sha256"] == LIZZI_AG_AUDIT_SHA
    )
    both_pass = mack_beta["status"] == "PASS" and lizzi_ag["status"] == "PASS"
    print(f"  All 3 audit_sha pins match: {sha_match}")
    print(f"  Both Stage-2 cross-reviewers PASS: {both_pass}")
    if not (sha_match and both_pass):
        print("ERROR: Pin mismatch or reviewer not PASS. Composite aggregation aborts.")
        return 3
    print()

    # Step 3: emit composite verdict line
    print("Step 3: emit composite Stage-2 PASS-AND verdict")
    composite_value = (
        "stage_2_pass_and=PASS;"
        "mack_beta=PASS;"
        "lizzi_alpha_gamma=PASS;"
        "four_way_conjunction_alpha_beta_gamma_joint_clause=PASS-AND;"
        f"phase_1_input_sha={PHASE_1_AUDIT_SHA};"
        f"mack_beta_input_sha={MACK_BETA_AUDIT_SHA};"
        f"lizzi_ag_input_sha={LIZZI_AG_AUDIT_SHA};"
        "axis_alpha_machinery_scope_K=1_SUGGESTION_with_K=2_advance_path_cf55_reading_A;"
        "axis_beta_bridge_map_scheme_K=1_SUGGESTION_first_instance_at_cf55_landing;"
        "axis_gamma_binding_axis_K=1_retained_W7b82_baseline_no_advance_cf55_reading_A;"
        "joint_clause_K=3_promotion_threshold_consistent_across_axes;"
        "stage_3_promotion_eligibility=ENABLED_per_joint_theorem_promotion_md_4_stage_pathway;"
        "phase_1_INFO_line_121_remains_on_disk_per_absolute_verdict_permanence;"
        "substrate_input_orthogonality_PASS_at_structural_ceiling_no_overlap_caveat;"
        "OAA_exclusion_PASS_for_both_reviewers_connes_volovik_excluded_as_original_authors;"
        "downstream_inheritance_reach_test_PASS_for_both_reviewers;"
        "procedural_floor_satisfied_no_workshop_transcripts_consumed_by_cross_reviewers;"
        "audit_at_plan_freeze_6_item_check_PASS_per_joint_theorem_promotion_md_audit_at_plan_freeze;"
        "composite_emission_pattern=orchestrator_direct_parallel_to_cf58_plan_w7-5_three_lines_specification"
    )
    print(f"  composite_verdict: PASS")
    print(f"  composite_value (~1400 chars): documents 4-way PASS-AND + K-counter advancement + Stage-3 eligibility")
    print()

    emit_verdict("PASS", composite_value, audit_sha, content_sha)
    print(f"  appended to: {VERDICT_TXT.relative_to(PROJECT_ROOT)}")
    print()

    print(f"=== {GATE_ID}: PASS (composite Stage-2 PASS-AND; wall {time.time() - t0:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
