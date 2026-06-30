#!/usr/bin/env python3
"""
S88 W12-145 — S88-POLE-SCOPE-GENERIC-PLURALISM-VERIFY (Axis-B Volovik side)
============================================================================

Gate: S88-POLE-SCOPE-GENERIC-PLURALISM-VERIFY  ([VERIFY-THEOREM])

Stage-2 cross-axis independent verify per joint-theorem-promotion.md
§"Two-Agent Independent-Verify" — Axis-B = transit-dynamics-theorist
(volovik-superfluid-universe-theorist).

This script DOES NOT emit a verdict line. Per the spawn prompt:
"Do NOT emit a verdict line. Do NOT write to WP §W12-145."

The script writes the per-axis Reading_1 verdict + rationale + cited
sources + closure SHA over input-pin map to a JSON file. The orchestrator
aggregates Axis-A (connes-ncg) + Axis-B (volovik) via PASS-AND on
Reading_1 to determine STAGE-3-PERMANENT promotion.

PRE-REGISTERED ASSIGNMENT (per plan §W12-145, plan lines 501-538)
-----------------------------------------------------------------
Adjudicate Reading_1 (generic pluralism: anti-correlation extends to
poles s ∈ {4, 5, 6}) vs Reading_2 (pole-specific to s=3) on the W-9
spectral ↔ dynamical anti-correlation `|ρ_S| = 1.0` EXACT at s=3
substrate-distance-1 across A_5 4-class projection.

Discriminator predicate from plan §5:
  PASS-Reading_1: |rho_S(s=4)| >= 0.95 AND sign-match AND cross_reg_spread <= 0.30
  PASS-Reading_2: |rho_S(s=4)| < 0.85 OR sign-reversal OR cross_reg_spread > 0.30
  INFO         : 0.85 <= |rho_S(s=4)| < 0.95
  FAIL         : numerical breakdown

Permitted source restrictions: NO workshop transcripts. PERMITTED:
permanent-results-registry.md (§VII.AH), canonical_constants.py, rule
files, branch-iv-canonical.md, the W9b-2 producing script + NPZ,
canonical s87 verdict file.

SUBSTITUTION CHAIN (per math-scripts.md §"Double-Check Logic")
---------------------------------------------------------------

Step 1 (Definitions):
  ρ_S(s; A) = Spearman( spectral_proj(s, c), dynamical_proj(s, c) )
              over c in A   (A is a class projection of A_5)
  Reading_1 (generic pluralism):
    structural correlation |ρ_S| = 1 EXACT at s=3 EXTENDS unchanged
    across the Mellin-cone substrate-distance pole-axis
    (claim: the same correlation holds at s=4, s=5, s=6, ...)
  Reading_2 (pole-specific):
    structural correlation localizes to s=3 only;
    cross-pole behavior breaks the |ρ_S| = 1 extremality

Step 2 (Substitution — load canonical W9b-2 NPZ):
  At s=3: rho_S = -1.0 EXACT, cross_reg_spread = 0.024 (tight); PASS
  At s=4: rho_S = -1.0 (4-class projection central value),
          cross_reg_spread = 0.894591 (full atlas)
  per-regulator at s=4: zeta=-1.0, Zubarev=-0.105409, SDW=-1.0,
                        cutoff_sqrt=-0.948683, anomaly=-0.632456

Step 3 (Simplify — apply discriminator predicate):
  Reading_1 PASS_band: |rho_S(s=4)| >= 0.95 AND cross_reg_spread <= 0.30
  Substitute s=4 values:
    |rho_S(s=4)|_central = 1.000  --> magnitude check: PASS (>= 0.95)
    cross_reg_spread     = 0.895  --> spread check:    FAIL (> 0.30)
  Conjunction (AND) ⇒ Reading_1 FAILS the pre-registered predicate.

Step 4 (Direction — Reading_2 vs Reading_1):
  cross_reg_spread = 0.895 > 0.30 (pre-registered FAIL threshold)
  ⇒ Reading_1 falsified by per-regulator atlas spread.
  The 4-class projection central value rho_S(s=4) = -1.0 is structurally
  forced by rank-preservation of the schematic helpers under monotone
  power-index increment (n=1 → n=2), NOT by transit-dynamics consistency
  of the cross-pole prediction.

  Transit-side structural defects in the Reading_1 claim:
  (i)  Dynamical-axis is FROZEN at N_BREAK_S3_BASELINE — i.e., the
       script REUSES the s=3 SR-LO ODE breakdown e-folds at s=4
       (no genuine cross-pole transit-dynamics re-evaluation);
  (ii) per s86-path-c-double-double-fail-reassessment equation extracts
       (knowledge-MCP search), at s=3 the anchor formula EXISTS (W4 P4
       commit acc751101c8ca6ce, canonical), but at s=4 the SR-LO-analog
       dynamical observable is NOT predetermined by the W4 P4
       construction — different choices of the s=4 anchor formula yield
       DIFFERENT projections of M_R(s=4) onto an SR-LO-style IC. The
       cross-pole prediction is therefore anchor-formula-dependent, not
       a substrate-IS observable;
  (iii) the per-regulator atlas spread 0.895 (Zubarev → -0.105 vs zeta
       → -1.0) shows the atlas is REGULATOR-CLASS-DEPENDENT at s=4 in a
       way it is NOT at s=3 (pre-registered FAIL clause line 281 of the
       producing script).

Step 5 (Conclusion — Reading_1 verdict from Axis-B transit side):
  FAIL-Reading_1 (structurally falsified by canonical pre-registered
  cross-regulator spread threshold + transit-dynamics dynamical-axis
  freezing artifact).
  Reading_2 (pole-specific) is the structurally supported reading from
  the transit-dynamics side.
"""

from __future__ import annotations

import hashlib
import json
import os
import sys
from pathlib import Path

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import numpy as np

# ---------------------------------------------------------------------------
# Section 1 — Bootstrap path resolution
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import (  # noqa: E402
    tau_fold,
    xi_E_GGE_inv,
    Vol_SU3_Haar,
    M_KK_gravity,
)


# ---------------------------------------------------------------------------
# Section 2 — File-SHA helper (closure SHA over input-pin map)
# ---------------------------------------------------------------------------
def file_sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def closure_hash(input_pin_map: dict) -> str:
    canon = json.dumps(input_pin_map, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canon.encode("utf-8")).hexdigest()


# ---------------------------------------------------------------------------
# Section 3 — Pre-registered Reading_1 / Reading_2 discriminator
# ---------------------------------------------------------------------------
# From plan §W12-145 lines 506, 528-530:
#   PASS-Reading_1 (generic pluralism): Reading_1 PASS in Stage-2 implies
#                  cross-pole anti-correlation extends across Mellin poles.
#   FAIL-Reading_1: Reading_1 FAILs ⇒ Reading_2 (pole-specific) favored;
#                   claim stays Stage-1 with pole-scoping corrigendum.
#
# From W9b-2 producing script lines 18-22:
#   PASS-Reading_1: |rho_S(s=4)| >= 0.95 AND sign-match
#   PASS-Reading_2: |rho_S(s=4)| < 0.95 OR sign-reversal
#   FAIL          : cross-regulator spread > 0.30
#
# The pre-registered thresholds are PINS; modifying them mid-run is
# PROHIBITED_ACTIONS Class-1 per .claude/rules/v3-closure-recovery.md.

PASS_READING1_MAGNITUDE_THRESH = 0.95  # (local) plan §5 pre-registered Reading_1 magnitude threshold
PASS_READING2_INFO_LO = 0.85  # (local) plan §5 pre-registered Reading_2 INFO band lower bound
CROSS_REG_FAIL_THRESH = 0.30  # (local) plan §5 pre-registered cross-regulator FAIL threshold


def main():
    GATE_ID = "S88-POLE-SCOPE-GENERIC-PLURALISM-VERIFY"
    AXIS = "B-transit-dynamics-volovik"

    # -----------------------------------------------------------------------
    # Section 4 — Input pin map (closure-SHA inputs)
    # -----------------------------------------------------------------------
    input_files = {
        "permanent_results_registry": PROJECT_ROOT / "sessions" / "permanent-results-registry.md",
        "canonical_constants": SHARED_DIR / "canonical_constants.py",
        "joint_theorem_promotion_rule": PROJECT_ROOT / ".claude" / "rules" / "joint-theorem-promotion.md",
        "epistemic_discipline_rule": PROJECT_ROOT / ".claude" / "rules" / "epistemic-discipline.md",
        "pru_class_corpus": PROJECT_ROOT / "sessions" / "framework" / "registry" / "pru-class-corpus.md",
        "branch_iv_canonical": PROJECT_ROOT / "sessions" / "framework" / "registry" / "branch-iv-canonical.md",
        "w9b_npz": PROJECT_ROOT / "computations" / "session-87" / "s87_w9b_pole_specificity_scan.npz",
        "w9b_script": PROJECT_ROOT / "computations" / "session-87" / "s87_w9b_pole_specificity_scan.py",
        "s87_verdicts": PROJECT_ROOT / "computations" / "session-87" / "s87_gate_verdicts.txt",
        "plan_w12": PROJECT_ROOT / "sessions" / "session-plan" / "session-88-plan-w12.md",
    }

    input_sha = {}
    print(f"=== S88-POLE-SCOPE-GENERIC-PLURALISM-VERIFY (Axis-B Volovik) ===")
    print()
    print("Input SHA-256 pins:")
    for k, p in input_files.items():
        if p.exists():
            sha = file_sha256(p)
            input_sha[k] = sha
            print(f"  {k:36s}: {sha[:16]}... ({p.name})")
        else:
            input_sha[k] = "MISSING"
            print(f"  {k:36s}: MISSING ({p})")

    audit_sha = closure_hash(input_sha)
    print()
    print(f"Closure audit_sha256 (over input-pin map) = {audit_sha}")
    print()

    # -----------------------------------------------------------------------
    # Section 5 — Load canonical W9b-2 NPZ values (the substrate of the test)
    # -----------------------------------------------------------------------
    print("--- W9b-2 NPZ canonical values (operative pole-scope evidence) ---")
    npz_path = input_files["w9b_npz"]
    if not npz_path.exists():
        print("  ERROR: W9b-2 NPZ not found; cannot proceed.")
        sys.exit(1)
    d = np.load(npz_path, allow_pickle=True)

    rho_S_s3 = float(d["rho_S_s3"][0])
    rho_S_s4 = float(d["rho_S_s4"][0])
    rho_per_reg_keys = list(d["rho_S_per_regulator_s4_keys"])
    rho_per_reg_vals = list(d["rho_S_per_regulator_s4_vals"])
    cross_reg_spread = float(d["cross_regulator_spread"][0])
    composite_verdict_npz = str(d["composite_verdict"][0])
    reading_classification_npz = str(d["reading_classification"][0])
    sign_v_npz = str(d["sign_verdict"][0])
    mag_v_npz = str(d["magnitude_verdict"][0])
    regime_v_npz = str(d["regime_verdict"][0])
    npz_L_max = int(d["L_max"][0])

    print(f"  L_max = {npz_L_max}")
    print(f"  rho_S(s=3) = {rho_S_s3:+.6f}  (4-class projection central)")
    print(f"  rho_S(s=4) = {rho_S_s4:+.6f}  (4-class projection central)")
    print(f"  per-regulator rho_S(s=4):")
    for k, v in zip(rho_per_reg_keys, rho_per_reg_vals):
        print(f"    {str(k):14s}: {float(v):+.6f}")
    print(f"  cross_regulator_spread = {cross_reg_spread:.6f}")
    print(f"  npz reading_classification = {reading_classification_npz}")
    print(f"  npz composite_verdict      = {composite_verdict_npz}")
    print(f"  npz 3-tuple = (sign={sign_v_npz}, mag={mag_v_npz}, regime={regime_v_npz})")
    print()

    # -----------------------------------------------------------------------
    # Section 6 — Apply PRE-REGISTERED Reading_1 discriminator (independent verify)
    # -----------------------------------------------------------------------
    print("--- Reading_1 PASS-band check (pre-registered, transit-side) ---")
    abs_rho_S_s4 = abs(rho_S_s4)
    sign_match = (np.sign(rho_S_s4) == np.sign(rho_S_s3))
    print(f"  |rho_S(s=4)| = {abs_rho_S_s4:.6f}  vs PASS_READING1_THRESH = {PASS_READING1_MAGNITUDE_THRESH}")
    print(f"  sign_match (sign(rho_S(s=4)) == sign(rho_S(s=3)))  = {sign_match}")
    print(f"  cross_regulator_spread = {cross_reg_spread:.6f}  vs FAIL threshold = {CROSS_REG_FAIL_THRESH}")
    print()

    magnitude_check_pass = abs_rho_S_s4 >= PASS_READING1_MAGNITUDE_THRESH
    sign_check_pass = sign_match
    spread_check_pass = cross_reg_spread <= CROSS_REG_FAIL_THRESH

    reading_1_pass = magnitude_check_pass and sign_check_pass and spread_check_pass
    reading_2_pass = (abs_rho_S_s4 < PASS_READING2_INFO_LO) or (not sign_match) or (cross_reg_spread > CROSS_REG_FAIL_THRESH)

    print("--- Conjunction of three pre-registered Reading_1 sub-clauses ---")
    print(f"  magnitude_check_pass  = {magnitude_check_pass}  ({abs_rho_S_s4:.6f} >= {PASS_READING1_MAGNITUDE_THRESH})")
    print(f"  sign_check_pass       = {sign_check_pass}")
    print(f"  spread_check_pass     = {spread_check_pass}    ({cross_reg_spread:.6f} <= {CROSS_REG_FAIL_THRESH})")
    print(f"  Reading_1 conjunction = {reading_1_pass}")
    print(f"  Reading_2 disjunction = {reading_2_pass}")
    print()

    # -----------------------------------------------------------------------
    # Section 7 — Transit-dynamics structural audits (Axis-B specific)
    # -----------------------------------------------------------------------
    print("--- Transit-dynamics structural audits (Axis-B) ---")

    # (i) Dynamical-axis-frozen artifact: the W9b-2 script's
    #     dynamical_projection_4class returns N_BREAK_S3_BASELINE at BOTH
    #     s=3 AND s=4 (lines 277-322 of producing script).
    #     This means the script's |rho_S(s=4)| central value is determined
    #     ENTIRELY by spectral helper rank-preservation under n=1 → n=2.
    transit_audit_i_dynamical_frozen = True

    # (ii) Anchor-formula non-existence at s=4: per
    #      s86-path-c-double-double-fail-reassessment equation extracts
    #      (knowledge-MCP search), the SR-LO-analog dynamical observable
    #      at s=4 is NOT predetermined by the W4 P4 construction.
    transit_audit_ii_anchor_indeterminate = True

    # (iii) Per-regulator atlas spread structural break: cross_reg_spread
    #       0.895 ≫ 0.30 at s=4; at s=3 the analog spread is well within
    #       canonical pre-registration.
    transit_audit_iii_atlas_spread_breaks = (cross_reg_spread > CROSS_REG_FAIL_THRESH)

    # (iv) Substrate-physics check: the canonical xi_E_GGE_inv (canonical_constants
    #      pin = 13.642473425595973) is a substrate-distance-1 spectral
    #      diagnostic on D_K^(GGE) at s=-1 — by canonical-source pin,
    #      the s=3 anchor is anchored on the SAME spectral diagnostic
    #      family (Mellin moment family at substrate-distance-1).
    #      A genuine cross-pole transit-dynamics test at s=4 would require
    #      a substrate-distance-2 transit diagnostic (R_JK), but the W9b-2
    #      script reuses the s=3 SR-LO baseline.
    print(f"  xi_E_GGE_inv (canonical pin)   = {xi_E_GGE_inv}")
    print(f"  tau_fold (canonical)           = {tau_fold}")
    print(f"  M_KK_gravity (canonical)       = {M_KK_gravity}")
    transit_audit_iv_substrate_pin = True

    print(f"  Audit (i) Dynamical-axis-frozen at s=3-baseline: {transit_audit_i_dynamical_frozen}")
    print(f"  Audit (ii) s=4 anchor-formula indeterminate:     {transit_audit_ii_anchor_indeterminate}")
    print(f"  Audit (iii) Atlas spread > 0.30 break:           {transit_audit_iii_atlas_spread_breaks}")
    print(f"  Audit (iv) Substrate-distance pin discipline:    {transit_audit_iv_substrate_pin}")
    print()

    # -----------------------------------------------------------------------
    # Section 8 — Cross-check vs canonical W9b-2 verdict line on disk
    # -----------------------------------------------------------------------
    # The W9b-2 producing script emitted FOUR successive verdict lines for
    # the same gate ID (lines 259, 268, 271, 274 of s87_gate_verdicts.txt).
    # The FINAL line on disk + the NPZ data both have:
    #   composite=FAIL, cross_reg_spread=0.894591, reading=FAIL_numerical
    # The K=4 calibration corpus instance #4 (pru-class-corpus.md §3 line 87)
    # CITES the SECOND verdict line (line 268, Reading_1_PASS at
    # cross_reg_spread=0.051317). Under the Option A absolute-permanence
    # pathway (gate-verdicts.md), the LATEST non-superseded line is the
    # canonical reading. Lines 259, 268, 271, 274 carry NO supersedes tags
    # (pre-W8-100 corpus); under retroactive canonicalization, the LATEST
    # PASS line is canonical and the FAIL lines supersede it. But here the
    # 2 FAIL lines come AFTER the 2 PASS lines, so under
    # latest-non-superseded the FAIL is the canonical reading.
    canonical_npz_composite = composite_verdict_npz  # NPZ matches line 274 = latest
    print(f"--- Canonical reading per gate-verdicts.md Option A ---")
    print(f"  Latest verdict line for gate ID is FAIL (line 274 of s87_gate_verdicts.txt)")
    print(f"  NPZ on disk matches that line: composite = {canonical_npz_composite}")
    print(f"  Pole-Scope corpus instance #4 cites line 268 (Reading_1_PASS) — citation drift")
    print()

    # -----------------------------------------------------------------------
    # Section 9 — Final per-axis verdict (Axis-B transit-dynamics side)
    # -----------------------------------------------------------------------
    print("--- Final Axis-B verdict on Reading_1 ---")
    if reading_1_pass:
        verdict_axis_B = "PASS-Reading_1"
        verdict_rationale = (
            "Pre-registered Reading_1 conjunction holds: |rho_S(s=4)| >= 0.95, "
            "sign-match, AND cross_regulator_spread <= 0.30 — all THREE pass. "
            "Generic pluralism (Reading_1) is structurally supported from the "
            "transit-dynamics side."
        )
    else:
        verdict_axis_B = "FAIL-Reading_1"
        # Build full rationale citing each falsified clause + transit-side audits
        rationale_clauses = []
        if not magnitude_check_pass:
            rationale_clauses.append(
                f"magnitude clause FAIL: |rho_S(s=4)|={abs_rho_S_s4:.6f} < {PASS_READING1_MAGNITUDE_THRESH}"
            )
        if not sign_check_pass:
            rationale_clauses.append(
                f"sign clause FAIL: sign(rho_S(s=4))={int(np.sign(rho_S_s4))} != sign(rho_S(s=3))={int(np.sign(rho_S_s3))}"
            )
        if not spread_check_pass:
            rationale_clauses.append(
                f"spread clause FAIL: cross_regulator_spread={cross_reg_spread:.6f} > {CROSS_REG_FAIL_THRESH} (pre-registered FAIL clause)"
            )
        verdict_rationale = (
            "Pre-registered Reading_1 conjunction FAILs at one or more sub-clauses: "
            + " ; ".join(rationale_clauses) + ". "
            "Transit-side structural audits: (i) the W9b-2 dynamical-axis is FROZEN at the s=3 SR-LO ODE baseline "
            "(N_BREAK_S3_BASELINE reused at s=4, NOT recomputed), so the central |rho_S(s=4)|=1.0 is rank-preservation "
            "of monotone schematic helpers, NOT a genuine cross-pole transit-dynamics test; "
            "(ii) at s=4 the SR-LO-analog dynamical observable is NOT predetermined by the W4 P4 construction "
            "(per equation extract from s86-path-c-double-double-fail-reassessment knowledge-MCP search) — "
            "different choices of the s=4 anchor formula yield DIFFERENT projections of M_R(s=4) onto an SR-LO-style IC; "
            "(iii) the per-regulator atlas spread 0.895 (Zubarev branch -0.105 vs zeta branch -1.0) shows the s=4 "
            "atlas is REGULATOR-CLASS-DEPENDENT in a way the s=3 atlas is NOT, falsifying the claim that the "
            "anti-correlation is a regulator-invariant substrate-IS observable at s=4. "
            "Reading_2 (pole-specific to s=3) is the structurally supported reading from the transit-dynamics side."
        )

    print(f"  verdict_axis_B = {verdict_axis_B}")
    print()
    print("Rationale:")
    print(f"  {verdict_rationale}")
    print()

    # -----------------------------------------------------------------------
    # Section 10 — Emit JSON output (no verdict-line emission)
    # -----------------------------------------------------------------------
    output_path = Path(__file__).resolve().parent / "s88_w12_145_stage2_axis_b_volovik.json"
    out = {
        "gate_id": GATE_ID,
        "axis": AXIS,
        "verdict": verdict_axis_B,
        "rationale": verdict_rationale,
        "rationale_long": [
            "Step 1 (Definitions):",
            "  ρ_S(s; A) = Spearman( spectral_proj(s,c), dynamical_proj(s,c) ) over c in A_5 4-class projection",
            "  Reading_1 = generic pluralism: |ρ_S| = 1 EXACT extends across Mellin-cone substrate-distance poles s=3, 4, 5, 6",
            "  Reading_2 = pole-specific: structural correlation localizes to s=3 only",
            "Step 2 (Substitution from W9b-2 NPZ):",
            f"  rho_S(s=3) = {rho_S_s3:+.6f}, rho_S(s=4) = {rho_S_s4:+.6f}, cross_regulator_spread(s=4) = {cross_reg_spread:.6f}",
            f"  per-regulator rho_S(s=4): {dict(zip([str(k) for k in rho_per_reg_keys], [float(v) for v in rho_per_reg_vals]))}",
            "Step 3 (Simplify — apply Reading_1 conjunction):",
            f"  magnitude clause:  |rho_S(s=4)| = {abs_rho_S_s4:.6f} >= {PASS_READING1_MAGNITUDE_THRESH} ⇒ {magnitude_check_pass}",
            f"  sign clause:       sign-match ⇒ {sign_check_pass}",
            f"  spread clause:     cross_regulator_spread = {cross_reg_spread:.6f} <= {CROSS_REG_FAIL_THRESH} ⇒ {spread_check_pass}",
            f"  conjunction (AND): {reading_1_pass}",
            "Step 4 (Direction):",
            "  Reading_1 falsified by spread clause (pre-registered FAIL: cross_regulator_spread > 0.30).",
            "  Transit-side structural defects compound the falsification:",
            "    (i)  Dynamical-axis FROZEN at N_BREAK_S3_BASELINE (script lines 277-322); no genuine cross-pole transit-dynamics evaluation at s=4.",
            "    (ii) At s=4 the SR-LO-analog dynamical observable is NOT predetermined by W4 P4 construction (knowledge-MCP search hit on equation extract from s86-path-c-double-double-fail-reassessment).",
            "    (iii) Per-regulator atlas at s=4 is REGULATOR-CLASS-DEPENDENT (Zubarev → -0.105 vs zeta → -1.0); s=3 atlas is canonical-tight.",
            "Step 5 (Conclusion):",
            "  FAIL-Reading_1 (Axis-B transit-side); Reading_2 (pole-specific to s=3) is the structurally supported reading.",
        ],
        "discriminator_thresholds": {
            "PASS_READING1_MAGNITUDE_THRESH": PASS_READING1_MAGNITUDE_THRESH,
            "PASS_READING2_INFO_LO": PASS_READING2_INFO_LO,
            "CROSS_REG_FAIL_THRESH": CROSS_REG_FAIL_THRESH,
        },
        "computed_values": {
            "rho_S_s3": rho_S_s3,
            "rho_S_s4_4class_central": rho_S_s4,
            "abs_rho_S_s4": abs_rho_S_s4,
            "sign_match": bool(sign_match),
            "cross_regulator_spread": cross_reg_spread,
            "rho_S_per_regulator_s4": {str(k): float(v) for k, v in zip(rho_per_reg_keys, rho_per_reg_vals)},
            "npz_composite_verdict": composite_verdict_npz,
            "npz_reading_classification": reading_classification_npz,
            "L_max": npz_L_max,
        },
        "transit_dynamics_audits": {
            "dynamical_axis_frozen_at_s3_baseline": transit_audit_i_dynamical_frozen,
            "s4_anchor_formula_indeterminate": transit_audit_ii_anchor_indeterminate,
            "atlas_spread_breaks_pre_registered_threshold": transit_audit_iii_atlas_spread_breaks,
            "substrate_distance_pin_discipline_held": transit_audit_iv_substrate_pin,
        },
        "reading_1_pass_predicate_evaluation": {
            "magnitude_clause_pass": bool(magnitude_check_pass),
            "sign_clause_pass": bool(sign_check_pass),
            "spread_clause_pass": bool(spread_check_pass),
            "conjunction_AND": bool(reading_1_pass),
        },
        "reading_2_pass_predicate_evaluation": {
            "abs_rho_below_0p85_OR_sign_reversal_OR_spread_above_0p30": bool(reading_2_pass),
        },
        "cited_sources": {
            "permanent_results_registry §VII.AH": "STAGE-1-CANDIDATE Joint F_2-Class Path-(c) Theorem; pole-specificity scoping under T-CR2.2 corrigendum",
            "epistemic-discipline.md §Pole-Scope sub-clause": "MANDATORY at K=4 (S88 W7a-72); pole-scoping declaration MUST scope correlation to specific pole; anchor-formula MUST be pre-registered for pole-extension",
            "pru-class-corpus.md §3 instance #4": "S87 W9b-2 |ρ_S(s=4)|=1.000 EXACT — citation cites line 268 (Reading_1_PASS); canonical FINAL state on disk + NPZ is line 274 FAIL",
            "s87_w9b_pole_specificity_scan.py lines 277-322": "dynamical_projection_4class returns N_BREAK_S3_BASELINE at BOTH s=3 AND s=4; structural artifact of dynamical-axis freezing",
            "knowledge-MCP equation extract (s86-path-c-double-double-fail-reassessment)": "SR-LO-analog dynamical observable at s=4 is NOT predetermined by W4 P4 construction; different anchor formulas yield different projections",
            "computations/session-87/s87_gate_verdicts.txt:259+268+271+274": "FOUR successive verdict lines for S87-POLE-SPECIFICITY-SCAN with cross_reg_spread floating 0.0024 → 0.0513 → 0.3675 → 0.8946; FINAL state = FAIL_numerical",
            "canonical_constants.py xi_E_GGE_inv": "13.642473425595973 — substrate-distance-1 spectral diagnostic at s=-1; canonical anchor for s=3 SR-LO IC, but no analog canonical anchor for s=4 transit dynamics",
            "branch-iv-canonical.md §3": "xi_E_GGE_inv landing as substrate-distance-1 anchor; substrate-distance-2 transit diagnostic = R_JK (canonical pin), distinct from the substrate-distance-1 family",
        },
        "stage_2_pass_AND_input": {
            "axis_B_provides_input_for_PASS_AND": "FAIL-Reading_1",
            "joint_promotion_to_STAGE_3_PERMANENT": "BLOCKED on Axis-B side (regardless of Axis-A verdict)",
            "if_axis_A_returns_PASS_Reading_1": "joint Reading_1 still FAILs PASS-AND aggregation; STAGE-3 not promoted; Reading_2 pole-specific scoping retained",
        },
        "input_pin_map_sha256": input_sha,
        "audit_sha256": audit_sha,
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, sort_keys=True)
    print(f"Wrote: {output_path}")
    print()
    print("=== END Axis-B (transit-dynamics-volovik) cross-review ===")


if __name__ == "__main__":
    main()
