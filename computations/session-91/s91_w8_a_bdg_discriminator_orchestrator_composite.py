#!/usr/bin/env python3
"""
S91 W8 §W8-5 orchestrator composite — Δ_W5_W6 3-band classification + STRUCTURAL VERDICT
=========================================================================================

Per session-91-plan-w8.md §W8-5 §5c (lines 2309-2329), after Axis-A
(van-den-dungen-bridge-theorist) and Axis-B (mack-cosmic-bridge) both emit
their respective Var_a evaluations, the orchestrator computes:

    Δ_W5_W6 := |Var_a^{W5_full} − Var_a^{W6_image}| / max(|Var_a^{W5_full}|,
                                                          |Var_a^{W6_image}|)

and classifies per the plan §"PASS/FAIL/INFO thresholds" (lines 2398-2405,
verbatim from workshop §C5 lines 201-207):

    PASS  (verdict (a) EQUIVALENCE THEOREM):    Δ_W5_W6 < 1e-5
    FAIL  sub-branch (b) Connes canonical:       Δ_W5_W6 ≥ 1e-3 AND
                                                 |Var_a^{W5_full} − v_inf| < 1e-5
    FAIL  sub-branch (c) Volovik canonical:      Δ_W5_W6 ≥ 1e-3 AND
                                                 |Var_a^{W6_image} − v_inf| < 1e-5
    INFO  (verdict (d) DUAL-SYMBOL convention):  1e-5 ≤ Δ_W5_W6 < 1e-3

where v_inf = v_inf_extrapolated = 6.4631783294e-06 (registry §VII.U.2
line 12961, S88 W5b-47 INFO Corner-II extrapolated value).

Per `.claude/rules/epistemic-discipline.md §"Pre-Registration Completeness"`
Class 8.2 (verifier-rubric pre-registration), the plan's 4-band rubric does
NOT cover the case `Δ_W5_W6 ≥ 1e-3 AND neither reading matches v_inf within
1e-5`. This is a rubric-coverage gap surfaced empirically. The composite
verdict-class for this case is `FAIL-NEITHER-MATCHES-V-INF` — composite FAIL
with a NEW sub-class designation documenting the multiplicity-convention
discrepancy as a carry-forward to S92+ for substrate-physics workshop
adjudication.

Dual-SHA per `.claude/templates/script-template.py` §4:
    audit_sha256   = sha256(script_bytes || canonical_bytes || pinmap_json)
    content_sha256 = sha256(script_bytes)
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
VERDICT_TXT = PROJECT_ROOT / "computations" / "session-91" / "s91_gate_verdicts.txt"
CANONICAL_PY = PROJECT_ROOT / "computations" / "_shared" / "canonical_constants.py"
WP_PATH = PROJECT_ROOT / "sessions" / "session-91" / "session-91-w8-workingpaper.md"

# sys.path setup BEFORE canonical_constants import (matches S91 W1 producing-
# script pattern: e.g. s91_w1_cf70_full_cc_multipliers.py lines 130-134).
sys.path.insert(0, str(PROJECT_ROOT / "computations" / "_shared"))
sys.path.insert(0, str(PROJECT_ROOT / "computations"))

from canonical_constants import *  # noqa: F401,F403,E402

# ============================ Gate-block constants ============================

GATE_ID = "S91-A-BDG-DEFINITIONAL-RECONCILIATION-DISCRIMINATOR"
WP_ID = "W8-5"
SCHEME = "stage-2-cross-axis-discriminator-orchestrator-composite"
CONVENTION = "a-bdg-definitional-reconciliation-three-band-classification"
L_MAX = 10                          # (local) — gate-specific canonical L_max per plan §W8-5 §7

# Pre-registered thresholds per workshop §C5 lines 201-207
DELTA_PASS_THRESHOLD = 1e-5         # (local) PASS (a) EQUIVALENCE THEOREM
DELTA_FAIL_THRESHOLD = 1e-3         # (local) FAIL (b)/(c) sub-branch
V_INF_MATCH_TOL = 1e-5              # (local) Class-8.3 publication-precision floor

V_INF_EXTRAPOLATED = 6.4631783294e-06   # (local) registry §VII.U.2 line 12961 (S88 W5b-47)

# Axis npz files
AXIS_A_NPZ = (PROJECT_ROOT / "computations" / "session-91"
              / "s91_w8_a_bdg_discriminator_var_a_w5_full.npz")
AXIS_B_NPZ = (PROJECT_ROOT / "computations" / "session-91"
              / "s91_w8_a_bdg_discriminator_axis_b_mack_var_a_w6_image.npz")

# Cross-link sources
W8_6_GATE_ID = "S91-HOCHSCHILD-KUNNETH-MORITA-INVARIANCE-STAGE-1-CANDIDATE-REGISTRY-LANDING"
W8_3_GATE_ID = "S91-M3C-KERNEL-UNIVERSALITY-STAGE-1-CANDIDATE-REGISTRY-LANDING"


def load_axis_var_a(npz_path: Path, candidate_keys: list[str]) -> tuple[float, str]:
    """Load Var_a from npz; try each candidate key in order; return (value, key_used)."""
    arr = np.load(npz_path, allow_pickle=True)               # (local)
    available = list(arr.keys())                              # (local)
    for k in candidate_keys:
        if k in available:
            v = arr[k]                                        # (local)
            # arr may be 0-d ndarray; convert to float
            try:
                v_float = float(v)                            # (local)
            except (TypeError, ValueError):
                v_float = float(np.asarray(v).item())         # (local)
            return v_float, k
    raise KeyError(f"None of {candidate_keys} found in {npz_path}; available: {available}")


def parse_axis_verdict_sha(gate_id_suffix: str) -> tuple[str, str]:
    """Return (audit_sha256, content_sha256) of the latest non-superseded
    canonical line for gate {GATE_ID}-{gate_id_suffix} per Option A reading
    discipline (gate-verdicts.md §"Option A — sig_5 remediation pathway").
    """
    full_id = f"{GATE_ID}-{gate_id_suffix}"                   # (local)
    prefix = full_id + ":"                                    # (local)
    text = VERDICT_TXT.read_text(encoding="utf-8")            # (local)
    # All canonical lines for this gate (in file order)
    canon = [ln for ln in text.splitlines()
             if ln.startswith(prefix)
             and "audit_sha256=" in ln
             and "content_sha256=" in ln]                     # (local)
    if not canon:
        raise RuntimeError(f"No canonical verdict line for {full_id}")
    # Per Option A: scan supersedes= tags; exclude superseded lines
    superseded_shas: set[str] = set()                         # (local)
    for ln in canon:
        if "supersedes=" in ln:
            sup = ln.split("supersedes=", 1)[1].split(";")[0].split()[0]
            superseded_shas.add(sup.strip("'\""))
    # Latest non-superseded line wins
    for ln in reversed(canon):
        audit_sha = ln.split("audit_sha256=", 1)[1].split()[0]
        if audit_sha not in superseded_shas:
            content_sha = ln.split("content_sha256=", 1)[1].split()[0]
            return audit_sha, content_sha
    raise RuntimeError(f"All canonical lines for {full_id} are superseded")


def parse_gate_audit_sha(gate_id: str) -> str:
    """Return the canonical audit_sha256 for a gate (most-recent non-superseded)."""
    prefix = gate_id + ":"                                    # (local)
    text = VERDICT_TXT.read_text(encoding="utf-8")            # (local)
    canon = [ln for ln in text.splitlines()
             if ln.startswith(prefix)
             and "audit_sha256=" in ln]                       # (local)
    if not canon:
        return ""
    superseded_shas: set[str] = set()                         # (local)
    for ln in canon:
        if "supersedes=" in ln:
            sup = ln.split("supersedes=", 1)[1].split(";")[0].split()[0]
            superseded_shas.add(sup.strip("'\""))
    for ln in reversed(canon):
        audit_sha = ln.split("audit_sha256=", 1)[1].split()[0]
        if audit_sha not in superseded_shas:
            return audit_sha
    return ""


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def classify_3_band(delta: float, v_w5: float, v_w6: float, v_inf: float
                    ) -> tuple[str, str, str]:
    """Apply the 3-band classification per plan §W8-5 §8.

    Returns (composite_verdict, sub_branch, narrative).
    """
    abs_v5_minus_vinf = abs(v_w5 - v_inf)                     # (local)
    abs_v6_minus_vinf = abs(v_w6 - v_inf)                     # (local)

    if delta < DELTA_PASS_THRESHOLD:
        return ("PASS", "a_EQUIVALENCE_THEOREM",
                f"Δ_W5_W6 = {delta:.6e} < {DELTA_PASS_THRESHOLD:.0e} ⇒ "
                "verdict (a) EQUIVALENCE THEOREM — substrate-IS axiom-layer "
                "UNIFIED reading (dual-symbol convention COLLAPSES at axiom layer)")
    if delta >= DELTA_FAIL_THRESHOLD:
        # FAIL band — determine sub-branch (b/c/NEITHER)
        w5_matches = abs_v5_minus_vinf < V_INF_MATCH_TOL
        w6_matches = abs_v6_minus_vinf < V_INF_MATCH_TOL
        if w5_matches and not w6_matches:
            return ("FAIL", "b_CONNES_CANONICAL",
                    f"Δ_W5_W6 = {delta:.6e} ≥ {DELTA_FAIL_THRESHOLD:.0e} AND "
                    f"|Var_a^{{W5_full}} − v_inf| = {abs_v5_minus_vinf:.6e} < {V_INF_MATCH_TOL:.0e} ⇒ "
                    "verdict (b) Connes canonical — W5 tensor-product reading "
                    "is canonical; W3+W6 M_2(ℂ) reading is a sub-quotient projection losing A_F Wedderburn content")
        if w6_matches and not w5_matches:
            return ("FAIL", "c_VOLOVIK_CANONICAL",
                    f"Δ_W5_W6 = {delta:.6e} ≥ {DELTA_FAIL_THRESHOLD:.0e} AND "
                    f"|Var_a^{{W6_image}} − v_inf| = {abs_v6_minus_vinf:.6e} < {V_INF_MATCH_TOL:.0e} ⇒ "
                    "verdict (c) Volovik canonical — W3+W6 image reading is "
                    "canonical; W5 tensor-product over-sums upstream A_F content")
        # NEITHER sub-branch fires — rubric-coverage gap (PRU Class 8.2)
        return ("FAIL", "NEITHER_MATCHES_V_INF_RUBRIC_COVERAGE_GAP",
                f"Δ_W5_W6 = {delta:.6e} ≥ {DELTA_FAIL_THRESHOLD:.0e} BUT neither reading matches v_inf: "
                f"|Var_a^{{W5_full}} − v_inf|/v_inf = {abs_v5_minus_vinf/v_inf*100:.2f}%; "
                f"|Var_a^{{W6_image}} − v_inf|/v_inf = {abs_v6_minus_vinf/v_inf*100:.2f}%. "
                "PRU Class 8.2 verifier-rubric pre-registration gap — the plan's 4-band rubric "
                "does NOT cover this case. Multiplicity-convention discrepancy is the substrate-physics "
                "finding (carry-forward to S92+ for workshop adjudication of multiplicity-convention canon)")
    # INFO band (1e-5 ≤ delta < 1e-3)
    return ("INFO", "d_DUAL_SYMBOL_NAMING",
            f"{DELTA_PASS_THRESHOLD:.0e} ≤ Δ_W5_W6 = {delta:.6e} < {DELTA_FAIL_THRESHOLD:.0e} ⇒ "
            "verdict (d) DUAL-SYMBOL convention — both readings well-defined and "
            "quantitatively close-but-distinct; dual-symbol convention RETAINED at "
            "substrate-IS axiom layer; both readings preserved as F-functor-related dual structural objects")


def compute_dual_sha(pinmap: dict[str, str]) -> tuple[str, str]:
    script_bytes = Path(__file__).read_bytes()                # (local)
    canonical_bytes = CANONICAL_PY.read_bytes()               # (local)
    pinmap_json = json.dumps(
        dict(sorted(pinmap.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")                                          # (local)
    h_audit = hashlib.sha256()                                 # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                                # (local)
    h_content = hashlib.sha256()                               # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()                            # (local)
    return audit, content


def main() -> int:
    print("=== §W8-5 Orchestrator Composite — Δ_W5_W6 3-band classification ===\n")

    # ----------------------------------------------------------------------
    # 1. Load Var_a values from npz files
    # ----------------------------------------------------------------------
    print("Loading Var_a^{W5_full} from Axis-A npz...")
    print(f"  path: {AXIS_A_NPZ.relative_to(PROJECT_ROOT)}")
    var_a_w5_full, key_a = load_axis_var_a(
        AXIS_A_NPZ,
        candidate_keys=["Var_a_W5_full", "var_a_w5_full", "Var_a", "var_a"])
    print(f"  Var_a^{{W5_full}} = {var_a_w5_full:.15e}  (key='{key_a}')")

    print("\nLoading Var_a^{W6_image} from Axis-B npz...")
    print(f"  path: {AXIS_B_NPZ.relative_to(PROJECT_ROOT)}")
    var_a_w6_image, key_b = load_axis_var_a(
        AXIS_B_NPZ,
        candidate_keys=["var_a_w6_image_canonical", "Var_a_W6_image", "var_a_w6_image",
                        "Var_a_W6_image_isoscalar", "var_a_w6_image_isoscalar",
                        "var_a_w6_canonical", "Var_a"])
    print(f"  Var_a^{{W6_image}} = {var_a_w6_image:.15e}  (key='{key_b}')")

    # ----------------------------------------------------------------------
    # 2. Compute Δ_W5_W6
    # ----------------------------------------------------------------------
    delta_w5_w6 = abs(var_a_w5_full - var_a_w6_image) / max(
        abs(var_a_w5_full), abs(var_a_w6_image))                # (local)
    print(f"\nΔ_W5_W6 = |Var_a^{{W5_full}} − Var_a^{{W6_image}}| / max(|·|, |·|)")
    print(f"        = |{var_a_w5_full:.6e} − {var_a_w6_image:.6e}| / max(...)")
    print(f"        = {delta_w5_w6:.6e}")

    # ----------------------------------------------------------------------
    # 3. 3-band classification
    # ----------------------------------------------------------------------
    composite, sub_branch, narrative = classify_3_band(
        delta_w5_w6, var_a_w5_full, var_a_w6_image, V_INF_EXTRAPOLATED)
    print(f"\n3-band classification: {composite} / {sub_branch}")
    print(f"  Narrative: {narrative}\n")

    # ----------------------------------------------------------------------
    # 4. Per-axis verdict-line SHA discovery (Option A non-superseded)
    # ----------------------------------------------------------------------
    axis_a_audit_sha, axis_a_content_sha = parse_axis_verdict_sha("AXIS-A")
    axis_b_audit_sha, axis_b_content_sha = parse_axis_verdict_sha("AXIS-B")
    w8_6_audit_sha = parse_gate_audit_sha(W8_6_GATE_ID)
    w8_3_audit_sha = parse_gate_audit_sha(W8_3_GATE_ID)
    print("Per-axis canonical (non-superseded) audit_sha256 pointers:")
    print(f"  Axis-A (vdd W5_full):     {axis_a_audit_sha}")
    print(f"  Axis-B (mack W6_image):   {axis_b_audit_sha}")
    print(f"  §W8-6 (Hochschild-Künneth Morita-invariance landing): {w8_6_audit_sha}")
    print(f"  §W8-3 (M_3(ℂ)-kernel universality landing):           {w8_3_audit_sha}")

    # ----------------------------------------------------------------------
    # 5. Input-pin map for closure_hash (audit_sha256) computation
    # ----------------------------------------------------------------------
    pinmap: dict[str, str] = {
        "_gate_id": GATE_ID,
        "_wp_id": WP_ID,
        "_scheme": SCHEME,
        "_convention": CONVENTION,
        "_L_max": str(L_MAX),
        "axis_a_audit_sha256": axis_a_audit_sha,
        "axis_a_content_sha256": axis_a_content_sha,
        "axis_a_npz_sha256": file_sha256(AXIS_A_NPZ),
        "axis_a_var_a_w5_full": f"{var_a_w5_full:.15e}",
        "axis_b_audit_sha256": axis_b_audit_sha,
        "axis_b_content_sha256": axis_b_content_sha,
        "axis_b_npz_sha256": file_sha256(AXIS_B_NPZ),
        "axis_b_var_a_w6_image": f"{var_a_w6_image:.15e}",
        "delta_w5_w6": f"{delta_w5_w6:.15e}",
        "v_inf_extrapolated": f"{V_INF_EXTRAPOLATED:.10e}",
        "composite": composite,
        "sub_branch": sub_branch,
        "w8_6_landing_audit_sha256_cross_link": w8_6_audit_sha,
        "w8_3_landing_audit_sha256_cross_link": w8_3_audit_sha,
    }
    audit_sha, content_sha = compute_dual_sha(pinmap)
    print(f"\nComposite dual-SHA:")
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")

    # ----------------------------------------------------------------------
    # 6. Build verdict line + companion rows + 3-tuple
    # ----------------------------------------------------------------------
    # Sub-branch determines the structural verdict-choice mapped to the
    # 4-letter plan classification (a/b/c/d/NEITHER).
    verdict_choice_map = {
        "a_EQUIVALENCE_THEOREM":          "a_EQUIVALENCE",
        "b_CONNES_CANONICAL":             "b_CONNES",
        "c_VOLOVIK_CANONICAL":            "c_VOLOVIK",
        "d_DUAL_SYMBOL_NAMING":           "d_DUAL_SYMBOL",
        "NEITHER_MATCHES_V_INF_RUBRIC_COVERAGE_GAP": "NEITHER_RUBRIC_COVERAGE_GAP",
    }
    composite_verdict_choice = verdict_choice_map[sub_branch]   # (local)

    # Downstream consumer A_BdG canonical reading pin (per plan §W8-5 line 2321)
    if composite == "PASS":
        a_bdg_pin = "UNIFIED_axiom_layer_dual_symbol_convention_RETAINED_at_naming_layer"
    elif sub_branch == "b_CONNES_CANONICAL":
        a_bdg_pin = "W5_tensor_product_canonical_A_BdG_full_eq_A_F_otimes_M_2_C"
    elif sub_branch == "c_VOLOVIK_CANONICAL":
        a_bdg_pin = "W6_image_canonical_A_BdG_image_eq_M_2_C_sub_quotient"
    elif sub_branch == "d_DUAL_SYMBOL_NAMING":
        a_bdg_pin = "DUAL_SYMBOL_convention_RETAINED_at_substrate_IS_axiom_layer"
    else:  # NEITHER_MATCHES_V_INF_RUBRIC_COVERAGE_GAP
        a_bdg_pin = "PENDING_S92_workshop_adjudication_multiplicity_convention_carry_forward_neither_W5_nor_W6_matches_v_inf_extrapolated"

    # Retrofit-required pointer per plan §W8-5 §10
    retrofit_map = {
        "a_EQUIVALENCE_THEOREM":          "None_substrate_IS_axiom_layer_UNIFIED",
        "b_CONNES_CANONICAL":             "CF_W3_3_line_419_445_plus_CF_51_line_1552_A_BdG_image_notation_update",
        "c_VOLOVIK_CANONICAL":            "CF_42_line_69_plus_CF_43_line_218_plus_W5_line_540_A_F_otimes_M_2_upstream_clarification",
        "d_DUAL_SYMBOL_NAMING":           "None_T2_46_sub_corrigendum_RETAINED",
        "NEITHER_MATCHES_V_INF_RUBRIC_COVERAGE_GAP":
            "S92_workshop_multiplicity_convention_canon_adjudication_PRU_8_2_rubric_coverage_gap_remediation",
    }
    retrofit_required = retrofit_map[sub_branch]                # (local)

    # T2.46 sub-corrigendum status (per plan §10)
    t246_status_map = {
        "a_EQUIVALENCE_THEOREM":          "RETAINED_at_naming_layer_COLLAPSED_at_axiom_layer",
        "b_CONNES_CANONICAL":             "REVISED_to_verdict_b_Connes_canonical",
        "c_VOLOVIK_CANONICAL":            "REVISED_to_verdict_c_Volovik_canonical",
        "d_DUAL_SYMBOL_NAMING":           "RETAINED_dual_symbol_convention_at_substrate_IS_axiom_layer",
        "NEITHER_MATCHES_V_INF_RUBRIC_COVERAGE_GAP":
            "RETAINED_under_interim_DUAL_SYMBOL_pending_S92_multiplicity_convention_adjudication",
    }
    t246_status = t246_status_map[sub_branch]                   # (local)

    # 3-tuple annotation per S87+ schema-v2 + gate-verdicts.md collapse rule
    # sign_verdict: predicted direction was PASS Δ<1e-5 (verdict a); actual direction is FAIL/INFO band
    if composite == "PASS":
        sign_v, mag_v, regime_v = "PASS", "PASS", "VALID"
    elif composite == "INFO":
        sign_v, mag_v, regime_v = "FAIL", "INFO", "VALID"
    else:  # FAIL
        sign_v, mag_v, regime_v = "FAIL", "FAIL", "VALID"

    value_str = (
        f"composite_verdict={composite_verdict_choice};"
        f"var_a_w5_full={var_a_w5_full:.10e};"
        f"var_a_w6_image={var_a_w6_image:.10e};"
        f"delta_w5_w6={delta_w5_w6:.6e};"
        f"3_band_classification=PASS_lt_{DELTA_PASS_THRESHOLD:.0e}_INFO_{DELTA_PASS_THRESHOLD:.0e}_to_{DELTA_FAIL_THRESHOLD:.0e}_FAIL_ge_{DELTA_FAIL_THRESHOLD:.0e};"
        f"publication_precision_class_8_3_floor={V_INF_MATCH_TOL:.0e};"
        f"v_inf_extrapolated={V_INF_EXTRAPOLATED:.10e};"
        f"axis_a_w5_minus_v_inf_rel_dev_pct={abs(var_a_w5_full - V_INF_EXTRAPOLATED) / V_INF_EXTRAPOLATED * 100:.2f};"
        f"axis_b_w6_minus_v_inf_rel_dev_pct={abs(var_a_w6_image - V_INF_EXTRAPOLATED) / V_INF_EXTRAPOLATED * 100:.2f};"
        f"axis_a_verdict_sha={axis_a_audit_sha};"
        f"axis_b_verdict_sha={axis_b_audit_sha};"
        f"joint_clauses_pass_and=parse_tree_AND_hochschild_kunneth_AND_gge_genericity_substrate_axis_machinery_PASS_but_empirical_NOT_confirmed;"
        f"downstream_consumer_a_bdg_canonical_reading_PINNED={a_bdg_pin};"
        f"cross_link_w8_6_hochschild_kunneth_morita_landing={w8_6_audit_sha};"
        f"cross_link_w8_3_m3c_kernel_universality_landing={w8_3_audit_sha};"
        f"retrofit_required_under_FAIL_branch={retrofit_required};"
        f"vii_u_2_sub_corrigendum_t2_46_status={t246_status};"
        f"sub_branch_designation={sub_branch};"
        f"rubric_coverage_gap_flag={'True' if sub_branch == 'NEITHER_MATCHES_V_INF_RUBRIC_COVERAGE_GAP' else 'False'}"
    )

    verdict_line = (
        f"{GATE_ID}: {composite} -- value={value_str!r} "
        f"scheme={SCHEME} convention={CONVENTION} "
        f"L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )
    companion_dual_sha = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split); "
        f"orchestrator composite over Axis-A + Axis-B verdict-line SHAs + Var_a npz SHAs + §W8-6 + §W8-3 cross-link audit_shas\n"
    )
    companion_3tuple = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={regime_v} "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2); "
        f"sign_verdict={sign_v} per substrate-axis Steelman prediction at workshop §C5 line 216 (predicted Δ<1e-5 verdict (a)); "
        f"actual Δ_W5_W6 = {delta_w5_w6:.6e}; "
        f"3-band classification: {composite}; sub-branch: {sub_branch}\n"
    )

    # ----------------------------------------------------------------------
    # 7. Idempotency check + append
    # ----------------------------------------------------------------------
    verdict_text = VERDICT_TXT.read_text(encoding="utf-8")
    if audit_sha in verdict_text:
        print(f"\n[ALREADY-EMITTED] composite audit_sha256={audit_sha[:16]}... "
              "is present in s91_gate_verdicts.txt — skipping append (idempotent re-run)")
    else:
        print(f"\nAppending composite verdict line + 2 companion rows to "
              f"{VERDICT_TXT.relative_to(PROJECT_ROOT)}...")
        with VERDICT_TXT.open("a", encoding="utf-8") as fp:
            fp.write(verdict_line)
            fp.write(companion_dual_sha)
            fp.write(companion_3tuple)

    # ----------------------------------------------------------------------
    # 8. Emit summary
    # ----------------------------------------------------------------------
    print("\n=== §W8-5 Composite Verdict Summary ===")
    print(f"  Composite verdict:          {composite}")
    print(f"  Sub-branch:                 {sub_branch}")
    print(f"  Verdict choice (plan §C5):  {composite_verdict_choice}")
    print(f"  Δ_W5_W6:                    {delta_w5_w6:.6e}")
    print(f"  Var_a^{{W5_full}}:            {var_a_w5_full:.10e}  (vdd Axis-A)")
    print(f"  Var_a^{{W6_image}}:           {var_a_w6_image:.10e}  (mack Axis-B)")
    print(f"  v_inf_extrapolated:         {V_INF_EXTRAPOLATED:.10e}  (registry §VII.U.2:12961)")
    print(f"  |W5 − v_inf| / v_inf:       {abs(var_a_w5_full - V_INF_EXTRAPOLATED)/V_INF_EXTRAPOLATED*100:.2f}%")
    print(f"  |W6 − v_inf| / v_inf:       {abs(var_a_w6_image - V_INF_EXTRAPOLATED)/V_INF_EXTRAPOLATED*100:.2f}%")
    print(f"  3-tuple annotation:         sign={sign_v} magnitude={mag_v} regime={regime_v}")
    print(f"  Downstream A_BdG pin:       {a_bdg_pin}")
    print(f"  Retrofit required:          {retrofit_required}")
    print(f"  T2.46 status:               {t246_status}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
