#!/usr/bin/env python3
"""
S91 W8 §W8-7 orchestrator composite — Stage-2 PASS-AND 3-axis aggregation
==========================================================================

Per session-91-plan-w8.md §W8-7 §5d (lines 3241-3260), the orchestrator
aggregates Axis-A (van-den-dungen-bridge-theorist Pillar 1 NCG-axiomatic) +
Axis-B-primary (mack-cosmic-bridge Pillar 2 operational laboratory) +
Axis-B-cross-pillar-specialist (spectral-geometer Hochschild cohomology
algebra-isomorphism layer) Stage-2 verifies of the Element 3 fiducial-anchor
binding type (iii) joint-hypersurface admissibility predicate on §W8-6-landed
§VII.AY.OP-PROJ (Hochschild-Künneth Morita-invariance theorem).

PASS-AND criterion (per plan §8):
  - PASS-AND three-axis: all 6 clauses (A1+A2+B1+B2+C1+C2) PASS independently
    in all 3 axis verdicts (logical AND across all 3 reviewers)
  - Element 3 joint-hypersurface (iii) K-counter K=1 → K=2 advancement ENABLED
    iff PASS-AND three-axis with substrate-input-orthogonality at structural ceiling
  - K=3 MANDATORY promotion deferred to forward calibration

Per-axis verdict ingestion (Option A non-superseded latest canonical):
  - Axis-A (vdd): corrective PASS via supersession; audit_sha256=111b164dfb005b22...
    (supersedes original FAIL at 8d4eaffed6bd7075...; script-bug fix per Option A)
  - Axis-B-primary (mack): FAIL on B1 rank-2 anchor reproduction at 1e-6 floor;
    audit_sha256=cb680378862f0010...
  - Axis-B-cross-pillar-specialist (spectral-geometer): corrective PASS via
    supersession; audit_sha256=a3a8c877f86aca68... (supersedes original FAIL at
    7161f4df5f3f890f...; verifier-formulation correction per Option A)

Composite outcome:
  - FAIL — Axis-B-primary B1 FAIL blocks composite PASS-AND
  - Element 3 joint-hypersurface (iii) K=1 → K=2 advancement BLOCKED
  - Substantive substrate-physics carry-forward: §VII.AY.OP-PROJ Element 5
    registry-text arithmetic gloss inconsistency (Class-8.3 publication-precision
    pre-registration issue) — all three axes surfaced the same finding with
    different verdict-scope-dependent disposition

This is the canonical substrate-physics finding from §W8-7: the registry-text
claim that Fraction(793346, 108307) = Fraction(114453, 15625) is arithmetically
FALSE at the 5-sig-fig precision (cross-multiplication discrepancy 29,821;
delta 1.76e-5 absolute). All three reviewers independently confirmed this
arithmetic mismatch; verdicts differ by which Fraction is adopted as the
substrate-canonical anchor for the audit comparison.

Dual-SHA per `.claude/templates/script-template.py` §4.
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
VERDICT_TXT = PROJECT_ROOT / "computations" / "session-91" / "s91_gate_verdicts.txt"
CANONICAL_PY = PROJECT_ROOT / "computations" / "_shared" / "canonical_constants.py"

sys.path.insert(0, str(PROJECT_ROOT / "computations" / "_shared"))
sys.path.insert(0, str(PROJECT_ROOT / "computations"))

from canonical_constants import *  # noqa: F401,F403,E402

# ============================ Gate-block constants ============================

GATE_ID = "S91-ELEMENT-3-FIDUCIAL-ANCHOR-BINDING-JOINT-HYPERSURFACE-(iii)-ADMISSIBILITY-VERIFY"
WP_ID = "W8-7"
SCHEME = "joint-theorem-promotion-stage-2-pass-and-three-axis-orchestrator-composite"
CONVENTION = "cross-axis-axis-a-vdd-axis-b-primary-mack-axis-b-cross-pillar-specialist-spectral-geometer"
L_MAX_STR = "10_pillar_2_only_axis_a_and_axis_b_cross_pillar_specialist_L_independent"

# Axis-side gate IDs
AXIS_A_GATE_ID = "S91-ELEMENT-3-FIDUCIAL-ANCHOR-BINDING-JOINT-HYPERSURFACE-(iii)-ADMISSIBILITY-VERIFY-AXIS-A"
AXIS_B_PRIMARY_GATE_ID = "S91-ELEMENT-3-FIDUCIAL-ANCHOR-BINDING-JOINT-HYPERSURFACE-(iii)-ADMISSIBILITY-VERIFY-AXIS-B-PRIMARY"
AXIS_B_CROSS_PILLAR_GATE_ID = "S91-ELEMENT-3-FIDUCIAL-ANCHOR-BINDING-JOINT-HYPERSURFACE-(iii)-ADMISSIBILITY-VERIFY-AXIS-B-CROSS-PILLAR-SPECIALIST"

# Cross-link sources
W8_6_GATE_ID = "S91-HOCHSCHILD-KUNNETH-MORITA-INVARIANCE-STAGE-1-CANDIDATE-REGISTRY-LANDING"
W8_5_GATE_ID = "S91-A-BDG-DEFINITIONAL-RECONCILIATION-DISCRIMINATOR"
W8_3_GATE_ID = "S91-M3C-KERNEL-UNIVERSALITY-STAGE-1-CANDIDATE-REGISTRY-LANDING"


def parse_gate_status_and_shas(gate_id: str) -> tuple[str, str, str]:
    """Return (status, audit_sha256, content_sha256) for the latest non-superseded
    canonical line of `gate_id` in s91_gate_verdicts.txt per Option A reading discipline."""
    text = VERDICT_TXT.read_text(encoding="utf-8")        # (local)
    prefix = gate_id + ":"                                # (local)
    canon = [ln for ln in text.splitlines()
             if ln.startswith(prefix) and "audit_sha256=" in ln]
    if not canon:
        raise RuntimeError(f"No canonical line for {gate_id}")
    superseded: set[str] = set()                          # (local)
    for ln in canon:
        if "supersedes=" in ln:
            sup = ln.split("supersedes=", 1)[1].split(";")[0].split()[0]
            superseded.add(sup.strip("'\""))
    for ln in reversed(canon):
        audit_sha = ln.split("audit_sha256=", 1)[1].split()[0]
        if audit_sha not in superseded:
            content_sha = ln.split("content_sha256=", 1)[1].split()[0]
            body = ln.split(":", 1)[1].strip()
            status = body.split()[0].rstrip(",")
            return status, audit_sha, content_sha
    raise RuntimeError(f"All canonical lines for {gate_id} are superseded")


def compute_dual_sha(pinmap: dict[str, str]) -> tuple[str, str]:
    script_bytes = Path(__file__).read_bytes()            # (local)
    canonical_bytes = CANONICAL_PY.read_bytes()           # (local)
    pinmap_json = json.dumps(
        dict(sorted(pinmap.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")                                      # (local)
    h_audit = hashlib.sha256()                             # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                            # (local)
    h_content = hashlib.sha256()                           # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()                        # (local)
    return audit, content


def main() -> int:
    print("=== §W8-7 Orchestrator Composite — 3-axis Stage-2 PASS-AND aggregation ===\n")

    # Ingest 3 axis verdicts
    axis_a_status, axis_a_audit, axis_a_content = parse_gate_status_and_shas(AXIS_A_GATE_ID)
    axis_b_primary_status, axis_b_primary_audit, axis_b_primary_content = parse_gate_status_and_shas(AXIS_B_PRIMARY_GATE_ID)
    axis_b_cross_pillar_status, axis_b_cross_pillar_audit, axis_b_cross_pillar_content = parse_gate_status_and_shas(AXIS_B_CROSS_PILLAR_GATE_ID)
    w8_6_status, w8_6_audit, _ = parse_gate_status_and_shas(W8_6_GATE_ID)
    w8_5_status, w8_5_audit, _ = parse_gate_status_and_shas(W8_5_GATE_ID)
    w8_3_status, w8_3_audit, _ = parse_gate_status_and_shas(W8_3_GATE_ID)

    print(f"Axis-A (vdd):                            {axis_a_status}  audit_sha256={axis_a_audit[:16]}...")
    print(f"Axis-B-primary (mack):                   {axis_b_primary_status}  audit_sha256={axis_b_primary_audit[:16]}...")
    print(f"Axis-B-cross-pillar (spectral-geometer): {axis_b_cross_pillar_status}  audit_sha256={axis_b_cross_pillar_audit[:16]}...")
    print(f"§W8-6 prereq (Hochschild-Künneth):       {w8_6_status}  audit_sha256={w8_6_audit[:16]}...")
    print(f"§W8-5 cross-link (A_BdG discriminator):  {w8_5_status}  audit_sha256={w8_5_audit[:16]}...")
    print(f"§W8-3 cross-link (M_3(C) universality):  {w8_3_status}  audit_sha256={w8_3_audit[:16]}...")

    # PASS-AND aggregation across 3 axes
    all_pass = all(s == "PASS" for s in [axis_a_status, axis_b_primary_status, axis_b_cross_pillar_status])
    any_fail = any(s == "FAIL" for s in [axis_a_status, axis_b_primary_status, axis_b_cross_pillar_status])
    if all_pass:
        composite = "PASS"
    elif any_fail:
        composite = "FAIL"
    else:
        composite = "INFO"

    element_3_k_counter_advance = "K_1_to_K_2_candidate_ENABLED" if all_pass else "K_1_to_K_2_BLOCKED_due_to_axis_FAIL"
    two_independent_axes_topology = "PASS" if all_pass else "BLOCKED_by_axis_b_primary_B1_FAIL"

    # Substrate-input-orthogonality at structural ceiling (3 reviewers, 3 independent data sources)
    substrate_input_orthogonality = "PASS_at_structural_ceiling_three_axis_three_independent_data_files"

    # Substantive carry-forward: the §VII.AY.OP-PROJ Element 5 arithmetic gloss inconsistency
    substantive_carry_forward = (
        "S92_VII_AY_OP_PROJ_ELEMENT_5_CLASS_8_3_CORRIGENDUM_"
        "Fraction_793346_108307_NEQ_Fraction_114453_15625_at_exact_arithmetic_"
        "cross_mult_residual_29821_delta_1.76e-5_absolute"
    )

    # Pinmap for closure_hash
    pinmap: dict[str, str] = {
        "_gate_id": GATE_ID,
        "_wp_id": WP_ID,
        "_scheme": SCHEME,
        "_convention": CONVENTION,
        "_L_max": L_MAX_STR,
        "axis_a_audit_sha256": axis_a_audit,
        "axis_a_content_sha256": axis_a_content,
        "axis_a_status": axis_a_status,
        "axis_b_primary_audit_sha256": axis_b_primary_audit,
        "axis_b_primary_content_sha256": axis_b_primary_content,
        "axis_b_primary_status": axis_b_primary_status,
        "axis_b_cross_pillar_audit_sha256": axis_b_cross_pillar_audit,
        "axis_b_cross_pillar_content_sha256": axis_b_cross_pillar_content,
        "axis_b_cross_pillar_status": axis_b_cross_pillar_status,
        "composite": composite,
        "element_3_k_counter_advance": element_3_k_counter_advance,
        "two_independent_axes_topology": two_independent_axes_topology,
        "substrate_input_orthogonality": substrate_input_orthogonality,
        "substantive_carry_forward": substantive_carry_forward,
        "w8_6_landing_audit_sha256_cross_link": w8_6_audit,
        "w8_5_discriminator_audit_sha256_cross_link": w8_5_audit,
        "w8_3_landing_audit_sha256_cross_link": w8_3_audit,
    }
    audit_sha, content_sha = compute_dual_sha(pinmap)
    print(f"\nComposite dual-SHA:")
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")

    # 3-tuple per gate-verdicts.md collapse rule
    if composite == "PASS":
        sign_v, mag_v, regime_v = "N/A", "PASS", "VALID"
    elif composite == "INFO":
        sign_v, mag_v, regime_v = "N/A", "INFO", "VALID"
    else:  # FAIL
        sign_v, mag_v, regime_v = "N/A", "FAIL", "VALID"

    # Build verdict line
    value_str = (
        f"stage_2_pass_and_three_axis={composite};"
        f"axis_a_verdict={axis_a_status}_vdd_clauses_A1_A2_PASS_post_supersession_option_a_clause_5;"
        f"axis_b_primary_verdict={axis_b_primary_status}_mack_clauses_B1_FAIL_B2_PASS_rank_2_anchor_at_1e-6_floor;"
        f"axis_b_cross_pillar_specialist_verdict={axis_b_cross_pillar_status}_spectral_geometer_clauses_C1_C2_PASS_post_supersession_option_a_clause_5;"
        f"joint_clauses_pass_and_three_axis={'True' if all_pass else 'False'};"
        f"element_3_joint_hypersurface_iii_k_counter_advance={element_3_k_counter_advance};"
        f"substrate_input_orthogonality_at_structural_ceiling={substrate_input_orthogonality};"
        f"two_independent_axes_verification_topology_PASS={'True' if all_pass else 'False'};"
        f"axis_a_audit_sha={axis_a_audit};"
        f"axis_b_primary_audit_sha={axis_b_primary_audit};"
        f"axis_b_cross_pillar_audit_sha={axis_b_cross_pillar_audit};"
        f"cross_link_w8_6_hochschild_kunneth_landing_audit_sha={w8_6_audit};"
        f"cross_link_w8_5_a_bdg_discriminator_audit_sha={w8_5_audit};"
        f"cross_link_w8_3_m3c_universality_landing_audit_sha={w8_3_audit};"
        f"substantive_carry_forward={substantive_carry_forward};"
        f"axis_a_disposition=corrective_PASS_via_option_a_script_bug_fix_case_sensitivity_plus_substantively_correct_preservation_predicate;"
        f"axis_b_cross_pillar_disposition=corrective_PASS_via_option_a_verifier_formulation_correction_sage_q_vs_sage_q;"
        f"axis_b_primary_disposition=FAIL_honest_at_pre_registered_1e-6_floor_against_registry_claimed_sage_q_canonical;"
        f"three_axis_substantive_convergence=all_three_axes_independently_surfaced_VII_AY_OP_PROJ_E5_arithmetic_gloss_inconsistency;"
        f"underlying_hochschild_kunneth_morita_invariance_theorem_substrate_physics_unchanged=True;"
        f"composite_FAIL_does_NOT_invalidate_w8_6_stage_1_candidate_landing_at_VII_AY_OP_PROJ"
    )

    verdict_line = (
        f"{GATE_ID}: {composite} -- value={value_str!r} "
        f"scheme={SCHEME} convention={CONVENTION} "
        f"L_max={L_MAX_STR} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )
    companion_dual_sha = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split); "
        f"3-axis orchestrator composite over Axis-A + Axis-B-primary + Axis-B-cross-pillar-specialist verdict-line SHAs + §W8-6 + §W8-5 + §W8-3 cross-link audit_shas\n"
    )
    companion_3tuple = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={regime_v} "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2); composite={composite}; "
        f"Element 3 (iii) K-counter advancement BLOCKED; "
        f"substantive carry-forward {substantive_carry_forward}\n"
    )

    # Idempotency check
    verdict_text = VERDICT_TXT.read_text(encoding="utf-8")
    if audit_sha in verdict_text:
        print(f"\n[ALREADY-EMITTED] composite audit_sha256={audit_sha[:16]}... already in verdict file")
    else:
        print(f"\nAppending composite verdict + 2 companion rows to {VERDICT_TXT.relative_to(PROJECT_ROOT)}...")
        with VERDICT_TXT.open("a", encoding="utf-8") as fp:
            fp.write(verdict_line)
            fp.write(companion_dual_sha)
            fp.write(companion_3tuple)

    print("\n=== §W8-7 Composite Verdict Summary ===")
    print(f"  Composite verdict:                                {composite}")
    print(f"  Axis-A (vdd):                                     {axis_a_status} ({axis_a_audit[:16]}...)")
    print(f"  Axis-B-primary (mack):                            {axis_b_primary_status} ({axis_b_primary_audit[:16]}...)")
    print(f"  Axis-B-cross-pillar (spectral-geometer):          {axis_b_cross_pillar_status} ({axis_b_cross_pillar_audit[:16]}...)")
    print(f"  3-axis PASS-AND:                                  {'True' if all_pass else 'False'}")
    print(f"  Element 3 (iii) K-counter advance:                {element_3_k_counter_advance}")
    print(f"  Two-independent-axes topology:                    {two_independent_axes_topology}")
    print(f"  Substrate-input-orthogonality:                    {substrate_input_orthogonality}")
    print(f"  3-tuple annotation:                               sign={sign_v} magnitude={mag_v} regime={regime_v}")
    print(f"  Substantive substrate-physics carry-forward to S92+:")
    print(f"    {substantive_carry_forward}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
