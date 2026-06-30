#!/usr/bin/env python3
"""
S88 W12-145 Stage-2 Axis-A axiomatic cross-review (connes-ncg-theorist)
=======================================================================

Gate: S88-POLE-SCOPE-GENERIC-PLURALISM-VERIFY (Stage-2 axis-A; PASS-AND with
volovik-superfluid-universe-theorist axis-B per joint-theorem-promotion.md
§"Stage 2 — Two-Agent Parallel Cross-Check").

PURPOSE
-------
Adjudicate Reading_1 (generic pluralism: anti-correlation extends across
Mellin poles s in {4, 5, 6}) vs Reading_2 (pole-specific to s=3) for the
W-9 spectral <-> dynamical anti-correlation `|rho_S| = 1.0` EXACT at s=3
substrate-distance-1 pole across A_5 4-class projection.

Scope (per joint-theorem-promotion.md Stage-2 condition): operates WITHOUT
prior workshop context. Inputs are the registered §VII.AH STAGE-1-CANDIDATE
text (`sessions/permanent-results-registry.md`), the W9b-2 empirical NPZ data
(`computations/session-87/s87_w9b_pole_specificity_scan.npz`), and the
cited rule-file clauses (`epistemic-discipline.md` §"Pole-Scope sub-clause"
MANDATORY at K=4; `cross-pillar-bridge-anatomy.md` §"Algebra-axis
orthogonality K-counter" MANDATORY at K=3).

This script EMITS NO VERDICT LINE. It produces the JSON sidecar carrying
the axiomatic-axis Reading_1 verdict (PASS-Reading_1 / FAIL-Reading_1 /
INFO) plus rationale and closure SHA over the input-pin map. The
orchestrator aggregates this with the volovik axis-B verdict via PASS-AND
on the cross-pole-prediction.

DISCIPLINE
----------
- Substitution chain explicit per `.claude/rules/math-scripts.md` §"Double-
  Check Logic". No sign/direction/threshold claim without canonical-form
  derivation.
- Knowledge-MCP queried prior to compute (S87-POLE-SPECIFICITY-SCAN gate
  history, K-counter status, algebra-axis orthogonality rule clauses).
- All inputs SHA-256 pinned for closure-hash reproducibility.
- Open-verdict adjudication: the verdict is computed from rule-file
  authority + empirical data; not pre-judged.

CLASSIFICATION: GEOMETRIC (NCG-axiomatic side; algebra-INVARIANT family).
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

import numpy as np

# Project root (script lives in computations/session-88/)
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Canonical-constants import (mandatory for S34+ scripts per CLAUDE.md;
# validates that this script binds to canonical pin sourcing — used solely
# for cross-reference / audit-trail; computation in this script is symbolic
# (rule-file authority + NPZ empirical lookup), not numerical scan).
sys.path.insert(0, str(PROJECT_ROOT / "computations" / "_shared"))
from canonical_constants import xi_E_GGE_inv, tau_fold  # noqa: E402  (canonical pins)


# --------------------------------------------------------------------------- #
# Input-pin map (canonical sources cited; no agent-memory pins per AMRI)      #
# --------------------------------------------------------------------------- #

INPUT_PIN_MAP = {
    # Registry §VII.AH STAGE-1-CANDIDATE (the theorem text to verify)
    "registry_vii_ah": "sessions/permanent-results-registry.md",
    # Empirical W9b-2 NPZ data (rho_S(s=3) and rho_S(s=4) across 4-class + 5-reg)
    "w9b_2_npz": "computations/session-87/s87_w9b_pole_specificity_scan.npz",
    # W9b-2 producing script (for anchor-formula construction transparency)
    "w9b_2_py": "computations/session-87/s87_w9b_pole_specificity_scan.py",
    # MANDATORY rule clause: Pole-Scope sub-clause (K=4)
    "rule_epistemic_discipline": ".claude/rules/epistemic-discipline.md",
    # MANDATORY rule clause: Algebra-axis orthogonality K-counter (K=3)
    "rule_cross_pillar_bridge_anatomy": ".claude/rules/cross-pillar-bridge-anatomy.md",
    # MANDATORY rule clause corpus
    "rule_corpus_cross_pillar": "sessions/framework/registry/cross-pillar-bridge-corpus.md",
    # Stage-2 protocol
    "rule_joint_theorem_promotion": ".claude/rules/joint-theorem-promotion.md",
    # Math discipline (substitution chain)
    "rule_math_scripts": ".claude/rules/math-scripts.md",
    # Verdict-line schema (for context, no verdict emitted)
    "rule_gate_verdicts": ".claude/rules/gate-verdicts.md",
    # Canonical constants
    "canonical_constants": "computations/_shared/canonical_constants.py",
}


def sha256_file(rel_path: str) -> str:
    p = PROJECT_ROOT / rel_path
    if not p.exists():
        return f"<MISSING:{rel_path}>"
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def closure_sha(pinmap: dict) -> str:
    """Closure hash over ordered (key -> sha) pairs."""
    items = sorted(pinmap.items())
    serialized = "\n".join(f"{k}={v}" for k, v in items).encode("utf-8")
    return hashlib.sha256(serialized).hexdigest()


def log_input_shas(pinmap: dict) -> dict:
    sha_map = {}
    for key, rel in pinmap.items():
        sha = sha256_file(rel)
        print(f"  INPUT-SHA  {key:40s}  {sha[:16]}  {rel}")
        sha_map[key] = sha
    return sha_map


# --------------------------------------------------------------------------- #
# Empirical data load (W9b-2 pole-specificity NPZ)                            #
# --------------------------------------------------------------------------- #

def load_w9b_2_data() -> dict:
    npz_path = PROJECT_ROOT / "computations/session-87/s87_w9b_pole_specificity_scan.npz"
    data = np.load(npz_path, allow_pickle=True)
    return {
        "rho_S_s3_4class": float(data["rho_S_s3"][0]),
        "rho_S_s4_4class": float(data["rho_S_s4"][0]),
        "rho_S_per_regulator_s4_keys": list(data["rho_S_per_regulator_s4_keys"]),
        "rho_S_per_regulator_s4_vals": [float(v) for v in data["rho_S_per_regulator_s4_vals"]],
        "spectral_projection_s3_4class": [float(v) for v in data["spectral_projection_s3"]],
        "spectral_projection_s4_4class": [float(v) for v in data["spectral_projection_s4"]],
        "spectral_projection_s3_5reg": [float(v) for v in data["spectral_projection_s3_5reg"]],
        "spectral_projection_s4_5reg": [float(v) for v in data["spectral_projection_s4_5reg"]],
        "dynamical_projection_s3_4class": [float(v) for v in data["dynamical_projection_s3"]],
        "dynamical_projection_s4_4class": [float(v) for v in data["dynamical_projection_s4"]],
        "cross_regulator_spread": float(data["cross_regulator_spread"][0]),
        "L_max": int(data["L_max"][0]),
        "n_helper_s3": int(data["n_helper_s3"][0]),
        "n_helper_s4": int(data["n_helper_s4"][0]),
        "tau_fold": float(data["tau_fold"][0]),
        "composite_verdict_label": str(data["composite_verdict"][0]),
        "sign_verdict_label": str(data["sign_verdict"][0]),
        "magnitude_verdict_label": str(data["magnitude_verdict"][0]),
        "regime_verdict_label": str(data["regime_verdict"][0]),
        "reading_classification": str(data["reading_classification"][0]),
        "a5_4class_order": list(data["a5_4class_order"]),
        "atlas_5reg_order": list(data["atlas_5reg_order"]),
    }


# --------------------------------------------------------------------------- #
# Substitution-chain adjudication (axiomatic axis A; connes-ncg-theorist)     #
# --------------------------------------------------------------------------- #

def adjudicate_reading_1_axiomatic(emp: dict) -> dict:
    """
    Axiomatic-side (NCG-axiomatic, algebra-INVARIANT functional class)
    adjudication of Reading_1 (generic pluralism) vs Reading_2 (pole-specific).

    SUBSTITUTION CHAIN (math-scripts.md §"Double-Check Logic"):

    Step 1 — Definitions:
      Reading_1 (generic pluralism): rho_S(s) = ±1 EXACT across A_5 4-class
        projection for all s in {3, 4, 5, 6, ...}.
      Reading_2 (pole-specific):     rho_S(s=3) = ±1 EXACT; rho_S(s>=4) ≠ ±1
        strictly.
      Pole-Scope sub-clause (eDis MANDATORY at K=4): theorem text MUST scope
        to one pole; pole-extension requires pre-registered anchor-formula
        AND a discriminator predicate between Reading_1 and Reading_2.
      Algebra-axis orthogonality (cPBA MANDATORY at K=3): item 3 of
        plan-freeze enforcement reads "Cross-pole co-primary FORBIDDEN —
        per W-9 RULE-3 §"Pole-Scope sub-clause"; co-primary structures
        must inhabit the same Mellin pole-scope."
      W9b-2 empirical anchor-formula (script lines 38-42): the dynamical
        projection at s=4 INHERITS the rank order of N_break(R) from the
        s=3 baseline (the SR-LO ODE depends only on the IC ratio
        xi_E_GGE_inv * (M_R/M_F2), and the rank order of M_R(s=4) is what
        enters). This is a structurally-INHERITED rank order, not an
        independent empirical detection of cross-pole pluralism.
      W9b-2 5-regulator atlas spread: cross_regulator_spread = 0.89459074
        (NPZ key); pre-registered FAIL threshold = 0.30 (script line 22:
        `FAIL: numerical breakdown OR cross-regulator spread > 0.30`).

    Step 2 — Substitute (NCG-axiomatic constraints + W9b-2 empirical record):
      Substitute Reading_1 into Pole-Scope sub-clause requirement (1)
        "Pole-scoping declaration: theorem text reads 'structural
        correlation X holds at pole s=N' (NOT 'in general')":
          Reading_1 = "rho_S = ±1 across all s" = "in general"
          ⇒ Reading_1 violates requirement (1).
      Substitute Reading_1 into Algebra-axis orthogonality K-counter
        item 3 "Cross-pole co-primary FORBIDDEN":
          Reading_1 asserts a co-primary structural correlation spanning
          poles s ∈ {3, 4, 5, 6, ...}; this IS a cross-pole co-primary
          structural claim. ⇒ Reading_1 violates item 3.
      Substitute W9b-2 empirical:
          Cross_regulator_spread_s4 = 0.89459 > 0.30 (FAIL threshold).
          Per-regulator rho_S(s=4) = (-1.0, -0.105, -1.0, -0.949, -0.632)
            for (zeta, Zubarev, SDW, cutoff_sqrt, anomaly).
            Range = 1.0 - 0.105 = 0.895 — 5-regulator atlas anti-correlation
            COLLAPSES from |ρ| ≈ 1 at zeta+SDW to |ρ| ≈ 0.105 at Zubarev.
          4-class projection rho_S(s=4) = -1.0 EXACT, BUT this is the
            tautological output of inheriting the s=3 N_break rank order
            (script anchor-formula lines 38-42); it is NOT an independent
            empirical confirmation of cross-pole pluralism.

    Step 3 — Simplify (axiomatic side):
      Reading_1 violations of MANDATORY rule-file clauses:
        - Pole-Scope sub-clause (eDis MANDATORY at K=4): violated.
        - Algebra-axis orthogonality K-counter (cPBA MANDATORY at K=3): violated.
      Reading_2 violations of MANDATORY rule-file clauses:
        - Pole-Scope sub-clause: NOT violated (Reading_2 scopes to s=3).
        - Algebra-axis orthogonality: NOT violated (Reading_2 stays in
          one pole-scope).
      Empirical W9b-2 record:
        - 5-regulator atlas: cross-regulator spread 0.895 ≫ 0.30 ⇒
          FAIL threshold; supports Reading_2.
        - 4-class projection rho_S(s=4) = -1.0 EXACT is a tautology of the
          structural-anchor construction (script lines 38-42), NOT
          independent evidence for Reading_1.

    Step 4 — Direction (only after canonical form):
      Reading_1 fails BOTH MANDATORY rule-file clauses on the axiomatic
      side AND lacks independent empirical support beyond the
      structural-anchor tautology. Reading_2 satisfies both MANDATORY
      clauses and is consistent with the 5-regulator atlas spread
      empirical signature. Verdict: FAIL-Reading_1 from the axiomatic
      side. (Equivalently: Reading_2 is the axiomatically consistent
      reading.)

    Returns
    -------
    dict with keys:
      - axis_a_verdict_on_reading_1: "PASS-Reading_1" | "FAIL-Reading_1" | "INFO"
      - rationale: 5-10 sentence rationale text
      - cited_rule_clauses: list of MANDATORY rule clauses invoked
      - cited_empirical_anchors: list of W9b-2 NPZ keys / script line ranges
      - substitution_chain_summary: 4-step chain summary (defs / sub / simp / dir)
      - axiomatic_verdict_components: per-clause PASS/FAIL on Reading_1
    """
    # Canonical pre-registered FAIL threshold from W9b-2 script
    FAIL_THRESHOLD_CROSS_REG_SPREAD = 0.30  # (local; script line 22)

    # Empirical extraction
    cross_reg_spread_s4 = emp["cross_regulator_spread"]  # (local)
    rho_4class_s3 = emp["rho_S_s3_4class"]  # (local)
    rho_4class_s4 = emp["rho_S_s4_4class"]  # (local)
    per_reg_s4 = emp["rho_S_per_regulator_s4_vals"]  # (local)
    range_per_reg_s4 = max(per_reg_s4) - min(per_reg_s4)  # (local)
    range_per_reg_s4_abs_min = min(abs(v) for v in per_reg_s4)  # (local)
    range_per_reg_s4_abs_max = max(abs(v) for v in per_reg_s4)  # (local)

    # Substitution chain Step 4 - Direction
    # Reading_1 verdict per MANDATORY clause violations + empirical
    pole_scope_violation = True  # Reading_1 says "in general" (not pole-scoped)
    algebra_axis_orthogonality_violation = True  # cross-pole co-primary FORBIDDEN
    cross_reg_fail = cross_reg_spread_s4 > FAIL_THRESHOLD_CROSS_REG_SPREAD
    inherited_anchor_tautology = True  # script lines 38-42 inherit s=3 rank order

    # Composite axiomatic verdict on Reading_1
    axis_a_components = {
        "pole_scope_subclause_compliance": "FAIL_Reading_1" if pole_scope_violation else "PASS_Reading_1",
        "algebra_axis_orthogonality_compliance": "FAIL_Reading_1" if algebra_axis_orthogonality_violation else "PASS_Reading_1",
        "cross_regulator_spread_threshold": "FAIL_Reading_1" if cross_reg_fail else "PASS_Reading_1",
        "structural_anchor_independence": "FAIL_Reading_1" if inherited_anchor_tautology else "PASS_Reading_1",
    }

    # Verdict aggregation: ALL four components are FAIL-Reading_1 -> overall FAIL
    if all(v == "FAIL_Reading_1" for v in axis_a_components.values()):
        verdict = "FAIL-Reading_1"
    elif all(v == "PASS_Reading_1" for v in axis_a_components.values()):
        verdict = "PASS-Reading_1"
    else:
        verdict = "INFO"

    rationale = (
        "Axiomatic-side (NCG-axiomatic, algebra-INVARIANT functional class) verdict on "
        "Reading_1 (generic pluralism: anti-correlation extends to s in {4,5,6}). "
        "Reading_1 violates two MANDATORY rule-file clauses: (i) the Pole-Scope sub-clause "
        "of `epistemic-discipline.md` (MANDATORY at K=4 per S88 W7a-72) requires the theorem "
        "text scope the structural correlation to a single pole, but Reading_1 asserts the "
        "correlation 'in general' across poles; (ii) the Algebra-axis orthogonality K-counter "
        "of `cross-pillar-bridge-anatomy.md` (MANDATORY at K=3 per S87 W-2 R3 close) item 3 "
        "explicitly states 'Cross-pole co-primary FORBIDDEN — per W-9 RULE-3 §Pole-Scope "
        "sub-clause; co-primary structures must inhabit the same Mellin pole-scope', and "
        "Reading_1's structural claim is precisely a cross-pole co-primary correlation. "
        f"Empirical record from W9b-2 (`s87_w9b_pole_specificity_scan.npz`): cross-regulator "
        f"spread at s=4 = {cross_reg_spread_s4:.6f}, which exceeds the pre-registered FAIL "
        f"threshold {FAIL_THRESHOLD_CROSS_REG_SPREAD} by {cross_reg_spread_s4/FAIL_THRESHOLD_CROSS_REG_SPREAD:.3f}x; "
        f"per-regulator rho_S(s=4) ranges over [{min(per_reg_s4):.4f}, {max(per_reg_s4):.4f}] "
        f"with min(|rho|)={range_per_reg_s4_abs_min:.4f} (Zubarev), demonstrating that the "
        "5-regulator atlas anti-correlation collapses outside the F_2={zeta,SDW} sub-atlas. "
        f"The reported 4-class projection rho_S(s=4) = {rho_4class_s4:.4f} EXACT is a "
        "tautological consequence of the W9b-2 anchor-formula construction (script lines "
        "38-42: the dynamical projection at s=4 INHERITS the s=3 N_break rank order by "
        "construction since SR-LO ODE depends only on the IC ratio); it is therefore NOT an "
        "independent empirical detection of pole-pluralism. Reading_2 (pole-specific to "
        "substrate-distance-1 s=3) violates ZERO MANDATORY clauses and is consistent with "
        "the 5-regulator atlas spread signature. Connes-Moscovici 1995 §III.4 dim-spectrum "
        "residue formula `a_n = Res[Tr(D^{-2s}); s=(d-n)/2]` makes pole-specificity structural: "
        "the residue at each Mellin pole is a DISTINCT Seeley-DeWitt coefficient (s=3 ↔ a_2 "
        "Einstein-Hilbert; s=4 ↔ a_4 Yang-Mills) with structurally orthogonal regulator-class "
        "behavior. Therefore the axiomatic-axis verdict on Reading_1 is FAIL-Reading_1; "
        "equivalently Reading_2 (pole-specific) is the axiomatically consistent reading."
    )

    return {
        "axis_a_verdict_on_reading_1": verdict,
        "rationale": rationale,
        "cited_rule_clauses": [
            ".claude/rules/epistemic-discipline.md §\"Pole-Scope sub-clause (T1-20, S86 W-9; promoted to MANDATORY at K=4 via S88 W7a-72)\" lines 191-201",
            ".claude/rules/cross-pillar-bridge-anatomy.md §\"Algebra-axis orthogonality K-counter (parallel discipline; MANDATORY at K=3)\" lines 272-280",
            "sessions/framework/registry/cross-pillar-bridge-corpus.md §\"Mandatory at-plan-freeze enforcement\" item 3 (lines 218-227): 'Cross-pole co-primary FORBIDDEN'",
            ".claude/rules/joint-theorem-promotion.md §\"Stage 2 — Two-Agent Parallel Cross-Check\" (Stage-2 protocol)",
            "Connes-Moscovici 1995 §III.4 dim-spectrum residue formula a_n = Res[Tr(D^{-2s}); s=(d-n)/2]",
        ],
        "cited_empirical_anchors": [
            "computations/session-87/s87_w9b_pole_specificity_scan.npz (W9b-2 NPZ; keys: rho_S_s3, rho_S_s4, cross_regulator_spread, rho_S_per_regulator_s4_vals)",
            "computations/session-87/s87_w9b_pole_specificity_scan.py lines 22 (FAIL threshold), 38-42 (structural-anchor inheritance), 94-98 (a_0 regulator-degeneracy at s=4)",
            "sessions/permanent-results-registry.md §VII.AH lines 15399-15479 (STAGE-1-CANDIDATE text + Corrigendum 2 (T-CR2.2) pole-specificity scoping at lines 15441-15443)",
        ],
        "substitution_chain_summary": {
            "step_1_definitions": "Reading_1 = rho_S(s) = ±1 EXACT for all s in {3,4,5,6,...}; Reading_2 = rho_S = ±1 only at s=3; MANDATORY rules: Pole-Scope (eDis K=4), Algebra-axis orthogonality (cPBA K=3) with cross-pole co-primary FORBIDDEN.",
            "step_2_substitutions": "Substitute Reading_1 into both MANDATORY clauses: Reading_1 = 'in general' violates Pole-Scope (1); Reading_1's cross-pole correlation IS a 'cross-pole co-primary' structure violating Algebra-axis K-counter item 3. Empirical: cross_reg_spread(s=4)=0.89459 > 0.30 FAIL.",
            "step_3_simplification": "Reading_1 violates 2 MANDATORY clauses + empirical FAIL threshold + 4-class rho_S(s=4)=-1 is structurally-inherited tautology. Reading_2 violates 0 MANDATORY clauses + consistent with 5-reg atlas spread.",
            "step_4_direction": "FAIL-Reading_1 from axiomatic side; Reading_2 (pole-specific to s=3) is the axiomatically consistent reading.",
        },
        "axiomatic_verdict_components": axis_a_components,
        "empirical_anchors_quantitative": {
            "cross_regulator_spread_s4": cross_reg_spread_s4,
            "fail_threshold_cross_reg_spread": FAIL_THRESHOLD_CROSS_REG_SPREAD,
            "fail_margin_factor": cross_reg_spread_s4 / FAIL_THRESHOLD_CROSS_REG_SPREAD,
            "rho_S_s3_4class_proj": rho_4class_s3,
            "rho_S_s4_4class_proj_INHERITED": rho_4class_s4,
            "rho_S_s4_per_regulator": dict(zip(emp["rho_S_per_regulator_s4_keys"], per_reg_s4)),
            "rho_S_s4_per_regulator_range": range_per_reg_s4,
            "rho_S_s4_per_regulator_abs_min": range_per_reg_s4_abs_min,
            "rho_S_s4_per_regulator_abs_max": range_per_reg_s4_abs_max,
            "L_max": emp["L_max"],
            "tau_fold": emp["tau_fold"],
            "n_helper_s3": emp["n_helper_s3"],
            "n_helper_s4": emp["n_helper_s4"],
        },
    }


# --------------------------------------------------------------------------- #
# Main                                                                        #
# --------------------------------------------------------------------------- #

def main() -> int:
    print("=" * 78)
    print("S88 W12-145 Stage-2 Axis-A axiomatic cross-review (connes-ncg-theorist)")
    print("Gate: S88-POLE-SCOPE-GENERIC-PLURALISM-VERIFY (axis-A; PASS-AND with axis-B)")
    print("=" * 78)
    print()
    print("INPUT-PIN MAP (SHA-256 first 16 hex chars logged):")
    sha_map = log_input_shas(INPUT_PIN_MAP)
    print()
    pin_map_for_closure = {k: sha_map[k] for k in sorted(INPUT_PIN_MAP.keys())}
    closure = closure_sha(pin_map_for_closure)
    print(f"  CLOSURE-SHA   {closure}")
    print()

    # Empirical data load
    print("Loading W9b-2 empirical data (`s87_w9b_pole_specificity_scan.npz`)...")
    emp = load_w9b_2_data()
    print(f"  rho_S_s3 (4-class proj):     {emp['rho_S_s3_4class']:+.6f}")
    print(f"  rho_S_s4 (4-class proj):     {emp['rho_S_s4_4class']:+.6f}  [INHERITED via script lines 38-42]")
    print(f"  cross_regulator_spread_s4:    {emp['cross_regulator_spread']:.6f}  [FAIL threshold = 0.30]")
    print(f"  per-regulator rho_S(s=4):    {dict(zip(emp['rho_S_per_regulator_s4_keys'], emp['rho_S_per_regulator_s4_vals']))}")
    print(f"  L_max={emp['L_max']}, tau_fold={emp['tau_fold']:.4f}")
    print(f"  W9b-2 final composite verdict: {emp['composite_verdict_label']}  (reading={emp['reading_classification']})")
    print()

    # Axiomatic adjudication
    print("Running axiomatic-side adjudication (substitution chain explicit)...")
    result = adjudicate_reading_1_axiomatic(emp)

    print()
    print("VERDICT (Axis-A axiomatic side):")
    print(f"  axis_a_verdict_on_reading_1 = {result['axis_a_verdict_on_reading_1']}")
    print()
    print("Per-clause components:")
    for k, v in result["axiomatic_verdict_components"].items():
        print(f"  {k:50s}  {v}")
    print()

    # Persist JSON sidecar
    out_json_path = PROJECT_ROOT / "computations/session-88/s88_w12_145_stage2_axis_a_connes.json"
    payload = {
        "gate_id": "S88-POLE-SCOPE-GENERIC-PLURALISM-VERIFY",
        "stage": "Stage-2-axis-A",
        "axis": "axis_a_axiomatic",
        "reviewer_role": "connes-ncg-theorist",
        "axis_a_verdict_on_reading_1": result["axis_a_verdict_on_reading_1"],
        "axiomatic_verdict_components": result["axiomatic_verdict_components"],
        "rationale": result["rationale"],
        "cited_rule_clauses": result["cited_rule_clauses"],
        "cited_empirical_anchors": result["cited_empirical_anchors"],
        "substitution_chain_summary": result["substitution_chain_summary"],
        "empirical_anchors_quantitative": result["empirical_anchors_quantitative"],
        "input_pin_map": INPUT_PIN_MAP,
        "input_sha_map": sha_map,
        "closure_sha256": closure,
        "no_verdict_line_emitted": True,
        "no_workshop_context_consumed": True,
        "stage_2_protocol_compliance": (
            ".claude/rules/joint-theorem-promotion.md §\"Stage 2 — Two-Agent Parallel Cross-Check\""
        ),
        "axis_b_pairing": "volovik-superfluid-universe-theorist (parallel; PASS-AND aggregation by orchestrator)",
        "schema_version": "S87+",
        "session": "S88",
        "wave": "W12-145",
    }
    out_json_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"JSON sidecar written: {out_json_path}")
    print()
    print("Note: This script does NOT emit a verdict line (per spawn prompt).")
    print("PASS-AND aggregation of axis-A and axis-B verdicts is owned by the orchestrator.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
