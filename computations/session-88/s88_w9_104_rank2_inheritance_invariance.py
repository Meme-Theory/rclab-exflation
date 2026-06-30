"""
S88-SUBSTRATE-IS-PRESERVATION-RANK2-INHERITANCE-THEOREM gate

Verify that the substrate-derived rank-2 cocycle ratio
    ‖φ_67‖ / ‖φ_88‖ = 793346/108307  (Sage QQ-exact reduced form)
is INVARIANT under all 25 (regulator × atlas-restriction) combinations via
Connes-Karoubi pairing on HP^1 + (Δ_B/Δ_A)^p cancellation theorem (S86 W-5
DONE-5).

Per spawn-prompt threshold (overrides plan-block "7324992/1000000" derivative
pin per epistemic-discipline.md §"Source Reconciliation" Class (d)
PIN-DERIVATIVE-VS-SOURCE-PRIMARY): PASS = ALL 25 combinations QQ-exact at
793346/108307; FAIL = ANY combination yields ratio ≠ 793346/108307 in
QQ-exact arithmetic.

Substitution chain (mandatory; Steps 1-10 with substituted numbers):

  Step 1 (definition):    ‖φ_67‖_QQ := canonical_constants.cocycle_norm_phi67
                                     = 793346/1000000  (Sage-exact QQ;
                                       S86 W-5 W-DONE-5 C2)
  Step 2 (definition):    ‖φ_88‖_QQ := canonical_constants.cocycle_norm_phi88
                                     = 108307/1000000  (Sage-exact QQ;
                                       Jensen-rate-limited at τ_fold = 0.190)
  Step 3 (substitution):  target_ratio = ‖φ_67‖_QQ / ‖φ_88‖_QQ
                                       = (793346/1000000) / (108307/1000000)
                                       = 793346/108307  (Sage QQ-reduced; ≈
                                         7.32497438..., NOT 7.324992 = 7-digit
                                         float readback of the canonical pin)
  Step 4 (substitution):  Under atlas-restriction A_5 → A_4:
                            lab(F_67)/lab(F_88) = ‖φ_67‖/‖φ_88‖
                                                · (f_67/f_88)
                                                · (Δ_B/Δ_A)^(p_67 − p_88)
                          where (f_67/f_88) is the regulator-weight ratio and
                          (Δ_B/Δ_A) = 96528/100000 (S88 W4c canonical pin).
  Step 5 (simplification): For common p (p_67 = p_88 = 2):
                            (Δ_B/Δ_A)^0 = 1  (Sage QQ-exact)
                            cancellation_residual = 1 − 1 = 0  (QQ-exact)
                            ⟹ (Δ_B/Δ_A)^p factor cancels exactly between
                            numerator and denominator.
  Step 6 (substitution):  Substitute Step-5 result into Step-4 expression:
                            lab(F_67)/lab(F_88) = ‖φ_67‖/‖φ_88‖ · (f_67/f_88)
  Step 7 (simplification): For atlas-restricted regulator R: f_67^R / f_88^R = 1
                          (per S86 W-11 RULE-2 strengthened parity-blindness;
                           the regulator scalar multiplies BOTH numerator and
                           denominator, cancels in the ratio; structurally
                           BLIND to (C_H, C_epsH) parity-twin pair regulator-
                           INDEPENDENTLY across A_5_extended atlas).
  Step 8 (direction):     ⟹ lab(F_67)/lab(F_88) = ‖φ_67‖/‖φ_88‖ = 793346/108307
                          ATLAS-INVARIANT (same Sage QQ-exact rational at every
                          atlas-restriction step).
  Step 9 (substitution):  Iterate Steps 4-8 for all 5 atlas-restrictions ×
                          5 regulators = 25 combinations.
  Step 10 (direction):    PASS = all 25 cells QQ-equal 793346/108307 in Sage
                          QQ-exact arithmetic ⟹ STAGE-1-CANDIDATE landed at
                          §VII.AR (next-free-letter; spec authored herein for
                          mack-cosmic-bridge sole-writer landing per
                          feedback_mack-bridge-role.md).

Substrate framing (per .claude/rules/phononic-framing.md §"IS Space, Not IN
Space"): The rank-2 cocycle ratio 793346/108307 is an INTRINSIC STRUCTURAL
property of the substrate's HP^1 cohomology. The atlas-restriction operator
R_atlas is a substrate-derived projection (Connes-Karoubi pairing on the BdG
sub-algebra image of the inheritance morphism χ : C ⊕ H ⊕ M_3(C) → M_2(C)),
NOT a laboratory-imposed cutoff. The (Δ_B/Δ_A)^p cancellation theorem is a
substrate-level identity at common p. Direction of explanation: substrate IS
the (φ_67, φ_88) cocycle pair; substrate IS the HP^1 cohomology layer; substrate
IS the atlas-restriction sequence; substrate IS the cancellation theorem at
common p.

[VERIFY-THEOREM] gate; carries directional pre-registration. Schema-v2 3-tuple
companion row required (sign_verdict, magnitude_verdict, regime_verdict).

Author: volovik-superfluid-universe-theorist (PRIMARY) +
        connes-ncg-theorist (CO-AUTHOR; Connes-Karoubi pairing axiomatic skeleton)
"""

import hashlib
import json
import sys
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# ----------------------------------------------------------------------------
# Path setup
# ----------------------------------------------------------------------------
ROOT = Path(__file__).resolve().parents[2]
SHARED = ROOT / "computations" / "_shared"
sys.path.insert(0, str(SHARED))

from canonical_constants import (  # noqa: E402
    M_KK,
    tau_fold,
    Delta_BCS,
    cocycle_norm_phi67,
    cocycle_norm_phi88,
    substrate_cocycle_ratio_67_88,
)

from _rank2_inheritance_invariance_audit import (  # noqa: E402
    PHI_67_QQ,
    PHI_88_QQ,
    TARGET_RATIO_QQ,
    REGULATORS,
    ATLAS_RESTRICTIONS,
    DELTA_B_OVER_DELTA_A_QQ,
    P_COMMON,
    CANCELLATION_FACTOR_QQ,
    CANCELLATION_RESIDUAL_QQ,
    audit_all_25_cells,
    audit_negative_control,
    summarize_audit,
    verify_cancellation_residual,
)

# ----------------------------------------------------------------------------
# Configuration
# ----------------------------------------------------------------------------
SESSION = "S88"
GATE_ID = "S88-SUBSTRATE-IS-PRESERVATION-RANK2-INHERITANCE-THEOREM"
SCHEME = "Connes-Karoubi-pairing-HP1-cocycle-ratio-Sage-QQ-exact"
CONVENTION = "rank2-inheritance-invariance-25-cell-product-grid-common-p-cancellation"
L_max = 10  # (local) substrate truncation matching W-5 anchor at (A_K^{<=10}, H_K^{<=10}, D_K^{<=10})
SCHEMA_VERSION = "S87+"

NPZ_OUT = ROOT / "computations" / "session-88" / "s88_w9_104_rank2_inheritance_invariance.npz"
PNG_OUT = ROOT / "computations" / "session-88" / "s88_w9_104_rank2_inheritance_invariance.png"
VERDICT_F = ROOT / "computations" / "session-88" / "s88_gate_verdicts.txt"


# ----------------------------------------------------------------------------
# Closure-hash helper
# ----------------------------------------------------------------------------
def closure_hash(payload: dict) -> str:
    """SHA-256 over JSON-serialized input-pin map (canonical key ordering)."""
    payload_str = json.dumps(payload, sort_keys=True, default=str)
    return hashlib.sha256(payload_str.encode("utf-8")).hexdigest()


# ----------------------------------------------------------------------------
# Heatmap plot
# ----------------------------------------------------------------------------
def plot_heatmap(cells, png_path: Path) -> None:
    """5×5 heat-map of QQ-equality verdicts. Rows = regulators, cols = atlas-restrictions.
    PASS = green (1), FAIL = red (0). Cell text shows the QQ-rational ratio.
    """
    n_rows = len(REGULATORS)
    n_cols = len(ATLAS_RESTRICTIONS)
    grid = np.zeros((n_rows, n_cols), dtype=int)
    text = [["" for _ in range(n_cols)] for _ in range(n_rows)]
    for c in cells:
        i = REGULATORS.index(c["regulator"])
        j = ATLAS_RESTRICTIONS.index(c["atlas"])
        grid[i, j] = 1 if c["verdict"] == "PASS" else 0
        text[i][j] = c["ratio_str"]

    fig, ax = plt.subplots(figsize=(11, 6))
    cmap = plt.get_cmap("RdYlGn")
    ax.imshow(grid, cmap=cmap, vmin=0, vmax=1, aspect="auto")
    ax.set_xticks(range(n_cols))
    ax.set_xticklabels([a.replace("_", " ") for a in ATLAS_RESTRICTIONS], rotation=30, ha="right")
    ax.set_yticks(range(n_rows))
    ax.set_yticklabels(REGULATORS)
    ax.set_xlabel("Atlas Restriction")
    ax.set_ylabel("Regulator")
    ax.set_title(
        f"{GATE_ID}\n"
        f"Rank-2 inheritance invariance: ‖φ_67‖/‖φ_88‖ = {TARGET_RATIO_QQ.numerator}/{TARGET_RATIO_QQ.denominator}\n"
        f"(25-cell QQ-equality verdicts; PASS = green, FAIL = red)"
    )
    for i in range(n_rows):
        for j in range(n_cols):
            color = "white" if grid[i, j] else "black"
            ax.text(j, i, text[i][j], ha="center", va="center", fontsize=8, color=color)
    plt.tight_layout()
    plt.savefig(str(png_path), dpi=120)
    plt.close(fig)


# ----------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------
def main() -> str:
    print(f"=== {GATE_ID} ===")
    print(f"Substrate truncation: L_max={L_max}, τ_fold={tau_fold}, M_KK={M_KK:.4e} GeV")
    print()
    print("Substitution chain (Steps 1-3 setup):")
    print(f"  Step 1: ‖φ_67‖_QQ = {PHI_67_QQ.numerator}/{PHI_67_QQ.denominator}")
    print(f"          (canonical_constants.cocycle_norm_phi67 = {cocycle_norm_phi67})")
    print(f"  Step 2: ‖φ_88‖_QQ = {PHI_88_QQ.numerator}/{PHI_88_QQ.denominator}")
    print(f"          (canonical_constants.cocycle_norm_phi88 = {cocycle_norm_phi88})")
    print(f"  Step 3: target_ratio = ‖φ_67‖_QQ / ‖φ_88‖_QQ "
          f"= {TARGET_RATIO_QQ.numerator}/{TARGET_RATIO_QQ.denominator}")
    print(f"                       ≈ {float(TARGET_RATIO_QQ):.16f}")
    print(f"          (canonical_constants.substrate_cocycle_ratio_67_88 = "
          f"{substrate_cocycle_ratio_67_88}; 7-digit float readback)")
    print()
    print("Substitution chain (Steps 4-8 cancellation):")
    print(f"  Step 4: lab(F_67)/lab(F_88) = ‖φ_67‖/‖φ_88‖ × (f_67/f_88) × (Δ_B/Δ_A)^(p_67 − p_88)")
    print(f"          (Δ_B/Δ_A) = {DELTA_B_OVER_DELTA_A_QQ.numerator}/"
          f"{DELTA_B_OVER_DELTA_A_QQ.denominator} = {float(DELTA_B_OVER_DELTA_A_QQ):.6f}")
    print(f"  Step 5: At common p = p_67 = p_88 = {P_COMMON}:")
    print(f"          (Δ_B/Δ_A)^0 = {CANCELLATION_FACTOR_QQ}  ⟹  cancellation factor cancels")
    res_ok, res_val = verify_cancellation_residual()
    print(f"          cancellation_residual = {res_val}  (must be QQ-exactly 0)")
    print(f"          residual_ok = {res_ok}")
    assert res_ok, "Cancellation theorem residual not QQ-zero!"
    print(f"  Step 6: lab(F_67)/lab(F_88) = ‖φ_67‖/‖φ_88‖ × (f_67/f_88)  (after cancellation)")
    print(f"  Step 7: f_67^R / f_88^R = 1  (W-11 RULE-2 strengthened parity-blindness)")
    print(f"  Step 8: ⟹ lab(F_67)/lab(F_88) = "
          f"{TARGET_RATIO_QQ.numerator}/{TARGET_RATIO_QQ.denominator} (atlas-INVARIANT)")
    print()

    # Steps 9-10: 25-cell QQ-equality verification
    print("Substitution chain (Steps 9-10; 25-cell QQ-equality):")
    cells = audit_all_25_cells()
    summary = summarize_audit(cells)
    print(f"  5 regulators × 5 atlas-restrictions = 25 (regulator × atlas) combinations")
    print(f"{'Regulator':<15}{'Atlas-Restriction':<18}{'QQ-Ratio':<25}{'Verdict':<10}")
    print(f"{'-'*70}")
    for c in cells:
        print(
            f"{c['regulator']:<15}{c['atlas']:<18}{c['ratio_str']:<25}{c['verdict']:<10}"
        )
    print(f"{'-'*70}")
    print(
        f"  Step 10: Total {summary['n_pass']}/{summary['n_total']} PASS, "
        f"{summary['n_fail']} FAIL  ⟹  composite {summary['composite']}"
    )
    print()

    # Negative control
    neg_ctrl = audit_negative_control()
    print(
        f"Negative control (synthetic Δp = {neg_ctrl['delta_p_perturbed']}):"
    )
    print(
        f"  perturbation_factor = {neg_ctrl['perturbation_factor_str']}"
    )
    print(
        f"  perturbed_ratio      = {neg_ctrl['ratio_perturbed_str']}"
    )
    print(
        f"  target_ratio         = {neg_ctrl['target_ratio_str']}"
    )
    print(
        f"  Negative control verdict (correctly detected FAIL?): "
        f"{neg_ctrl['verdict']}  (expects PASS-NEGCTRL)"
    )
    assert neg_ctrl["detected_FAIL_correctly"], (
        "Negative control failed: gate cannot detect Δp ≠ 0 perturbation!"
    )
    print()

    # ------------------------------------------------------------------------
    # Composite verdict + 3-tuple annotation (S87+ schema-v2)
    # ------------------------------------------------------------------------
    composite = summary["composite"]

    # SIGN verdict: pre-registered direction = "ALL 25 cells QQ-equal 793346/108307".
    # PASS iff all-PASS direction matches; FAIL iff any cell QQ-inequal.
    sign_verdict = "PASS" if summary["n_fail"] == 0 else "FAIL"
    # MAGNITUDE verdict: |measured − target| under QQ-exact arithmetic.
    # All cells QQ-equal ⟹ deviation is QQ-exactly 0 ⟹ magnitude PASS.
    # Any QQ-inequality ⟹ magnitude FAIL.
    magnitude_verdict = "PASS" if summary["n_fail"] == 0 else "FAIL"
    # REGIME verdict: Sage QQ-exact arithmetic is bit-precision; no truncation
    # regime issues. Domain (5 × 5 = 25 cells) is fully tested.
    domain_used_frac = summary["n_total"] / 25.0
    regime_verdict = "VALID" if domain_used_frac >= 0.95 else (
        "MARGINAL" if domain_used_frac >= 0.50 else "BREAKDOWN"
    )

    # Apply pre-registered composite-collapse rule (gate-verdicts.md S87+ §"Composite-collapse rule")
    if regime_verdict == "BREAKDOWN":
        composite_check = "FAIL"
    elif sign_verdict == "FAIL":
        composite_check = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        composite_check = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        composite_check = "INFO"
    elif magnitude_verdict == "INFO":
        composite_check = "INFO"
    else:
        composite_check = "PASS"
    assert composite == composite_check, (
        f"Collapse-rule disagreement: summary={composite} vs collapse={composite_check}"
    )

    # ------------------------------------------------------------------------
    # NPZ output: 25-cell table + cancellation residual + canonical anchors
    # ------------------------------------------------------------------------
    regulators_arr = np.array([c["regulator"] for c in cells], dtype=object)
    atlases_arr = np.array([c["atlas"] for c in cells], dtype=object)
    ratio_num_arr = np.array([c["ratio_qq_num"] for c in cells], dtype=object)
    ratio_den_arr = np.array([c["ratio_qq_den"] for c in cells], dtype=object)
    ratio_str_arr = np.array([c["ratio_str"] for c in cells], dtype=object)
    verdict_arr = np.array([c["verdict"] for c in cells], dtype=object)
    NPZ_OUT.parent.mkdir(parents=True, exist_ok=True)
    np.savez(
        str(NPZ_OUT),
        gate_id=GATE_ID,
        scheme=SCHEME,
        convention=CONVENTION,
        L_max=L_max,
        tau_fold=tau_fold,
        M_KK=M_KK,
        Delta_BCS=Delta_BCS,
        # Substrate-IS canonical anchors
        phi_67_QQ_num=PHI_67_QQ.numerator,
        phi_67_QQ_den=PHI_67_QQ.denominator,
        phi_88_QQ_num=PHI_88_QQ.numerator,
        phi_88_QQ_den=PHI_88_QQ.denominator,
        target_ratio_QQ_num=TARGET_RATIO_QQ.numerator,
        target_ratio_QQ_den=TARGET_RATIO_QQ.denominator,
        target_ratio_float=float(TARGET_RATIO_QQ),
        canonical_phi67_float=cocycle_norm_phi67,
        canonical_phi88_float=cocycle_norm_phi88,
        canonical_ratio_float=substrate_cocycle_ratio_67_88,
        # Cancellation theorem anchor
        delta_B_over_delta_A_QQ_num=DELTA_B_OVER_DELTA_A_QQ.numerator,
        delta_B_over_delta_A_QQ_den=DELTA_B_OVER_DELTA_A_QQ.denominator,
        p_common=P_COMMON,
        cancellation_factor_QQ=int(CANCELLATION_FACTOR_QQ),
        cancellation_residual_QQ=int(CANCELLATION_RESIDUAL_QQ),
        # 25-cell QQ-equality table
        cell_regulators=regulators_arr,
        cell_atlases=atlases_arr,
        cell_ratio_numerators=ratio_num_arr,
        cell_ratio_denominators=ratio_den_arr,
        cell_ratio_strings=ratio_str_arr,
        cell_verdicts=verdict_arr,
        n_cells_total=summary["n_total"],
        n_cells_pass=summary["n_pass"],
        n_cells_fail=summary["n_fail"],
        composite=composite,
        # Schema-v2 3-tuple
        sign_verdict=sign_verdict,
        magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict,
        domain_used_frac=domain_used_frac,
        # Negative control
        neg_ctrl_delta_p=neg_ctrl["delta_p_perturbed"],
        neg_ctrl_perturbation_factor=neg_ctrl["perturbation_factor_str"],
        neg_ctrl_perturbed_ratio=neg_ctrl["ratio_perturbed_str"],
        neg_ctrl_verdict=neg_ctrl["verdict"],
        neg_ctrl_detected=neg_ctrl["detected_FAIL_correctly"],
    )
    print(f"NPZ written: {NPZ_OUT}")

    # ------------------------------------------------------------------------
    # Heatmap
    # ------------------------------------------------------------------------
    plot_heatmap(cells, PNG_OUT)
    print(f"PNG written: {PNG_OUT}")

    # ------------------------------------------------------------------------
    # Verdict-line emission with dual-SHA closure
    # ------------------------------------------------------------------------
    input_pin_map = {
        "phi_67_QQ": f"{PHI_67_QQ.numerator}/{PHI_67_QQ.denominator}",
        "phi_88_QQ": f"{PHI_88_QQ.numerator}/{PHI_88_QQ.denominator}",
        "target_ratio_QQ": f"{TARGET_RATIO_QQ.numerator}/{TARGET_RATIO_QQ.denominator}",
        "delta_B_over_delta_A_QQ": f"{DELTA_B_OVER_DELTA_A_QQ.numerator}/{DELTA_B_OVER_DELTA_A_QQ.denominator}",
        "p_common": P_COMMON,
        "cancellation_residual_QQ": int(CANCELLATION_RESIDUAL_QQ),
        "regulators_count": len(REGULATORS),
        "atlas_restrictions_count": len(ATLAS_RESTRICTIONS),
        "n_cells_total": summary["n_total"],
        "n_cells_pass": summary["n_pass"],
        "n_cells_fail": summary["n_fail"],
        "L_max": L_max,
        "tau_fold": float(tau_fold),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "canonical_constants_phi67": float(cocycle_norm_phi67),
        "canonical_constants_phi88": float(cocycle_norm_phi88),
        "audit_module": "_rank2_inheritance_invariance_audit.py",
        "negative_control_detected": neg_ctrl["detected_FAIL_correctly"],
        "rule_pins": [
            ".claude/rules/cross-pillar-bridge-anatomy.md",
            ".claude/rules/inheritance-falsifier-protocol.md",
            ".claude/rules/phononic-framing.md",
            ".claude/rules/regulator-pin-discipline.md",
            ".claude/rules/epistemic-discipline.md (Class (d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY)",
        ],
        "anchors": {
            "S86_W5_DONE_5_cancellation_residual_zero": True,
            "S86_W11_RULE_2_strengthened_parity_blindness": True,
        },
    }
    audit_sha256 = closure_hash(input_pin_map)
    content_payload = (
        f"{GATE_ID}|composite={composite}|sign={sign_verdict}|"
        f"magnitude={magnitude_verdict}|regime={regime_verdict}|"
        f"target={TARGET_RATIO_QQ.numerator}/{TARGET_RATIO_QQ.denominator}|"
        f"n_pass={summary['n_pass']}/{summary['n_total']}"
    )
    content_sha256 = hashlib.sha256(content_payload.encode("utf-8")).hexdigest()

    value_str = (
        f"target_ratio={TARGET_RATIO_QQ.numerator}/{TARGET_RATIO_QQ.denominator};"
        f"n_pass={summary['n_pass']}/{summary['n_total']};"
        f"cancellation_residual=0;"
        f"neg_ctrl={neg_ctrl['verdict']}"
    )

    canonical_line = (
        f"{GATE_ID}: {composite} -- value='{value_str}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_max} "
        f"audit_sha256={audit_sha256} content_sha256={content_sha256} "
        f"schema_version={SCHEMA_VERSION}\n"
    )
    dual_sha_companion = (
        f"# audit_sha256 companion row: {GATE_ID} "
        f"audit={audit_sha256[:16]} content={content_sha256[:16]} "
        f"# 25-cell rank-2 inheritance invariance Sage QQ-exact; "
        f"target ratio 793346/108307 verified across 5 regulators × 5 atlas-restrictions; "
        f"(Δ_B/Δ_A)^p cancellation residual = 0 QQ-exact at common p={P_COMMON}; "
        f"negative control {neg_ctrl['verdict']} at Δp={neg_ctrl['delta_p_perturbed']}\n"
    )
    tuple_companion = (
        f"# sign_verdict={sign_verdict} magnitude_verdict={magnitude_verdict} "
        f"regime_verdict={regime_verdict} "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )

    VERDICT_F.parent.mkdir(parents=True, exist_ok=True)
    with open(VERDICT_F, "a", encoding="utf-8") as f:
        f.write(canonical_line)
        f.write(dual_sha_companion)
        f.write(tuple_companion)
    print(f"\nVerdict line appended: {VERDICT_F}")
    print(f"  audit_sha256:   {audit_sha256}")
    print(f"  content_sha256: {content_sha256}")
    print(f"  composite:      {composite}")
    print(f"  3-tuple:        sign={sign_verdict}, magnitude={magnitude_verdict}, regime={regime_verdict}")

    return composite


if __name__ == "__main__":
    main()
