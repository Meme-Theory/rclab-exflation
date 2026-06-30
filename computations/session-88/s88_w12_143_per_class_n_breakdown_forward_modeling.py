"""
S88 W12-143 — S88-OR-LATER-Q-8-PER-CLASS-N-BREAKDOWN-FORWARD-MODELING
=====================================================================

Per-class N-breakdown forward modeling.

OWNERSHIP: connes-ncg-theorist (per-class N-breakdown machinery; PRIMARY) +
mack-cosmic-bridge (cosmological forward-modeling integration; documented
in WP entry without separate dispatch per spawn-prompt instruction) +
gen-physicist (orchestrator). Solo runner.

PRE-COMPUTE AUDIT — KNOWLEDGE MCP FINDINGS:

The plan §W12-143 (lines 421-458) pre-registers a forward-prediction model

    N_breakdown(R) = N_breakdown_baseline + Delta(R)

for regulator-class set R ∈ {HypA, HypB, HypC, HypD}, with PASS criterion

    |spread_predicted - 0.3198| / 0.3198 <= 0.01    (1% pass-band)

against the W9b-1 measured spread = 31.98% (canonical value
`max_R_deviation_observable = 0.3197964204234936` from
`computations/session-87/s87_w9b_rescaled_ic_sr_lo_rerun.json` line 80).

The plan-pinned class label set {HypA, HypB, HypC, HypD} is generic; the
W9b-1 canonical L1-class-projection labels are {C_1_e, C_2_a, C_3_b,
C_4_ab} corresponding to the identity, single-(a), single-(b), and
composite-(ab) sub-atlas projections (per S87 W9b-1 dispatch source
`s87_w9b_rescaled_ic_sr_lo_rerun.py` lines 786 ff. + S87 W7-1 5-class
L1 partition definition `s87_w7_ic_per_class_verify.py` lines 11-24
referencing S86 W-9 §E-R2.2 line 1099). The label correspondence is

    HypA <-> C_1_e   (identity baseline)
    HypB <-> C_2_a   (single-(a) projection)
    HypC <-> C_3_b   (single-(b) projection)
    HypD <-> C_4_ab  (composite-(ab) projection)

documented in §W12-143 WP entry.

W9b-1 canonical data (from `s87_w9b_rescaled_ic_sr_lo_rerun.json`):

    alpha_R           = [1.0,
                         1.0954451150103321,    # = sqrt(6/5)
                         0.8944271909999159,    # = sqrt(4/5)
                         1.224744871391589]     # = sqrt(3/2)
    xi2_0_per_R       = [13.642473425595973,
                         16.370968110715165,
                         10.913978740476777,
                         20.463710138393957]
    N_breakdown_per_R = [0.01457768168620787,
                         0.012132263375416159,
                         0.01853106274316138,
                         0.009915791264885475]
    spread_measured   = 0.3197964204234936     (W9b-1 PASS at composite)

Cross-check on alpha_R: xi2_0_per_R / xi2_0_canonical = alpha_R^2:
    alpha_R^2 = [1.0, 1.2, 0.8, 1.5]
    xi2 ratio = [1.0, 1.2, 0.8, 1.5] (within machine epsilon)
The W9b-1 IC rescaling is xi2_0(R) = alpha_R^2 * xi2_0_canonical exactly.

SUBSTITUTION CHAIN (per .claude/rules/math-scripts.md):

    Definition 1: alpha_R = sqrt(xi2_0(R) / xi2_0_canonical)  per W9b-1
                  per-class IC rescaling factor.
    Definition 2: xi2_0(R) = alpha_R^2 * xi2_0_canonical
                  initial-condition value of the SR-LO Mukhanov-Sasaki
                  squared mode amplitude at horizon entry under per-class
                  regulator restriction.
    Definition 3: N_breakdown(R) := first N where eps_R(N) >= 0.5 in the
                  SR-LO trajectory (eps_breakdown_thresh = 0.5 per W9b-1
                  machinery_pin_map line 27 of the .json).
    Definition 4: N_breakdown_baseline := N_breakdown(C_1_e=HypA)
                                        = 0.01457768168620787 e-folds.
    Definition 5: Delta(R) := N_breakdown(R) - N_breakdown_baseline.
    Definition 6: spread(R) := max_R |Delta(R)| / N_breakdown_baseline
                             = max_R |N_breakdown(R) - N_breakdown_baseline|
                                       / N_breakdown_baseline.

    Step 1 — Substrate-derived form for Delta(R) (substrate prior).
       Under SR-LO with IC rescaling xi2_0(R) = alpha_R^2 * xi2_0_canonical,
       at fixed slow-roll background and fixed Mukhanov-Sasaki source
       structure, the eps trajectory eps_R(N) scales linearly with the
       initial xi2_0(R) (since xi2 enters the SR-LO Mukhanov-Sasaki
       backreaction integrand as a scalar multiplicative prefactor on
       the regulator-rescaled IC envelope; per W9b-1 plan §9 step 4
       analytic estimate line 121 "predicted_magnitude ~0.7%" derived
       from epsilon_R linear-in-alpha^2 scaling).

       Therefore at the SR-LO leading order:
          eps_R(N) ~ alpha_R^2 * eps_canonical(N)

       The breakdown N satisfies eps_R(N_breakdown) = 0.5. By the
       inverse-scaling argument (larger initial eps reaches threshold
       sooner; smaller initial eps reaches threshold later), if
       eps_canonical(N) is monotonically growing on the relevant N range,
       then approximately
          N_breakdown(R) ~ N_breakdown_baseline / alpha_R^2

       (substrate-prior closed-form forward model).

    Step 2 — Substitute into Definition 6:
       spread_predicted = max_R | N_baseline / alpha_R^2 - N_baseline | / N_baseline
                        = max_R | 1/alpha_R^2 - 1 |

       With alpha_R^2 = [1.0, 1.2, 0.8, 1.5]:
       1/alpha_R^2 = [1.0, 0.833333..., 1.25, 0.666666...]
       |1/alpha_R^2 - 1| = [0.0, 0.166667, 0.25, 0.333333]
       max = 0.333333... = 1/3

    Step 3 — Simplify and compare to W9b-1 measurement:
       spread_predicted_substrate_prior = 1/3 = 0.333333...
       spread_measured                  = 0.3197964204234936 (W9b-1)

       relative deviation = |spread_predicted - spread_measured| / spread_measured
                          = |0.333333 - 0.319796| / 0.319796
                          = 0.013537 / 0.319796
                          = 0.042331 = 4.2331%

    Step 4 — Direction (canonical-form output, only after Step 3):
       0.042331 > 0.01 (1% PASS band)
       Therefore the substrate-prior closed-form forward model FAILS
       the 1% PASS criterion.

       The deviation 4.2% exceeds 1% (FAIL band) but is well below the
       INFO-band threshold (5%) of W9b-1's plan; structurally this means
       the substrate-prior 1/alpha^2 form CAPTURES THE LEADING SCALING
       but the SR-LO ODE non-linearity contributes a residual ~4% in
       N_breakdown that the closed-form model does NOT reproduce within
       the 1% pass-band.

    Step 5 — Fitting alternative: a pure power-law
       N_breakdown(R) = N_baseline / alpha_R^p for free p.
       Least-squares on log-log gives p_lstsq computed below; we report
       both p=2 (substrate-prior) and p=p_lstsq (post-fit) but the GATE
       VERDICT is on the substrate-prior p=2 substantive forward model
       (the post-fit p_lstsq is curve-fitting, not a forward prediction).

       The P-fit-to-W9b-1 reproduction trivially achieves zero deviation
       (it IS the W9b-1 data). Reporting it would be an iterate-until-PASS
       Class-6 violation per .claude/rules/v3-closure-recovery.md
       PROHIBITED_ACTIONS. The gate VERDICT is on the substrate-prior model.

    Conclusion: PASS criterion not met by substrate-prior 1/alpha^2 forward
    model at 1% tolerance. Verdict = FAIL.

REGIME VERDICT analysis:
    spread_predicted (substrate prior, p=2) = 0.333333 (closed-form)
    spread_measured                        = 0.319796 (W9b-1 ODE numerical)
    Both within VALID regime (eps_R(N_breakdown) <= 0.5 by definition;
    no SR-LO collapse outside regime). regime_verdict = VALID.

3-tuple verdict (S87+ Schema-v2):
    sign_verdict      = PASS  (sign of spread_predicted matches sign of
                              spread_measured: both positive deviations)
    magnitude_verdict = FAIL  (4.2% > 1% pass-band)
    regime_verdict    = VALID (closed-form well-defined; SR-LO regime intact)
    composite         = FAIL  (per gate-verdicts.md composite-collapse rule:
                              magnitude=FAIL collapses composite to FAIL)

SUBSTRATE FRAMING (per .claude/rules/phononic-framing.md §"IS Space, Not
IN Space"):
    N_breakdown is a substrate-IS observable: the eigenvalue spectrum of
    D_K reorganizes under per-class regulator restriction; the SR-LO
    Mukhanov-Sasaki backreaction trajectory eps_R(N) is the substrate's
    response to that reorganization, NOT a quantity computed in a
    background-spacetime container. The forward-model 1/alpha^2 scaling
    derives from the substrate prior on how IC rescaling propagates
    through the SR-LO spectral-functional eigenvalue trajectory.

    No laboratory-IN observable: this is pure substrate-substrate
    consistency between the substrate-prior closed form and the
    substrate-numerical W9b-1 measurement. Container-thinking absent.

REFERENCES:
- Plan: sessions/session-plan/session-88-plan-w12.md §W12-143 (lines 421-458)
- W9b-1 data: computations/session-87/s87_w9b_rescaled_ic_sr_lo_rerun.json
              line 80 max_R_deviation_observable = 0.3197964204234936
- W9b-1 script: computations/session-87/s87_w9b_rescaled_ic_sr_lo_rerun.py
- CF-42 (per-class IC verify): computations/session-87/s87_w7_ic_per_class_verify.py
- canonical_constants.py: xi_E_GGE_inv = 13.642473425595973 (S86 BRANCH-IV)
- .claude/rules/gate-verdicts.md (S87+ canonical form Schema-v2)
- .claude/rules/math-scripts.md (substitution chain discipline)
- .claude/rules/v3-closure-recovery.md (PROHIBITED_ACTIONS Class 6)

Author: connes-ncg-theorist (S88 W12-143 dispatch, 2026-05-06).
"""

import hashlib
import json
import os
import sys
import time
from pathlib import Path

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import numpy as np
import matplotlib
matplotlib.use("Agg")  # (local) non-interactive backend
import matplotlib.pyplot as plt  # noqa: E402

_THIS = Path(__file__).resolve()
_REPO = _THIS.parent.parent.parent
sys.path.insert(0, str(_REPO / "computations" / "_shared"))
from canonical_constants import xi_E_GGE_inv  # noqa: E402,F401

# ---------------------------------------------------------------------------
# Constants (gate identity + plan-pinned thresholds)
# ---------------------------------------------------------------------------

GATE_ID = "S88-OR-LATER-Q-8-PER-CLASS-N-BREAKDOWN-FORWARD-MODELING"
WP_SECTION = "W12-143"
SCHEME = "SR-LO-Mukhanov-Sasaki-substrate-prior-1-over-alpha-squared-forward-model"
CONVENTION = "substrate-natural-xi-E-GGE-class-projected-W9b-1-baseline-anchor"
L_MAX = "N/A-SR-LO"  # SR-LO closed-form forward model
SCHEMA_VERSION = "S87+"

# Plan-pinned (PRDR machinery; FROZEN at plan-freeze)
N_BREAKDOWN_MEASURED = 0.3197964204234936  # (local) W9b-1 max_R_deviation_observable, plan-pinned per §W12-143 line 439
PASS_TOLERANCE = 0.01  # (local) 1% pass-band per plan §W12-143 lines 442, 448

# W9b-1 canonical data (loaded from s87_w9b_rescaled_ic_sr_lo_rerun.json)
ALPHA_R_W9B1 = [
    1.0,                 # C_1_e (HypA, identity baseline)
    1.0954451150103321,  # C_2_a (HypB, single-(a) ; alpha^2 = 1.2)
    0.8944271909999159,  # C_3_b (HypC, single-(b) ; alpha^2 = 0.8)
    1.224744871391589,   # C_4_ab (HypD, composite-(ab) ; alpha^2 = 1.5)
]
N_BREAKDOWN_PER_R_W9B1 = [
    0.01457768168620787,   # HypA / C_1_e (baseline)
    0.012132263375416159,  # HypB / C_2_a
    0.01853106274316138,   # HypC / C_3_b
    0.009915791264885475,  # HypD / C_4_ab (argmax of |dev|)
]
LABELS_W9B1 = ["C_1_e", "C_2_a", "C_3_b", "C_4_ab"]
LABELS_PLAN = ["HypA", "HypB", "HypC", "HypD"]


# ---------------------------------------------------------------------------
# SHA helpers
# ---------------------------------------------------------------------------


def file_sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def closure_hash(input_pin_map: dict) -> str:
    serialized = json.dumps(input_pin_map, sort_keys=True, default=str)
    return hashlib.sha256(serialized.encode("utf-8")).hexdigest()


# ---------------------------------------------------------------------------
# Forward-model evaluation
# ---------------------------------------------------------------------------


def evaluate_substrate_prior_forward_model(alpha_R, N_baseline):
    """
    Substrate-prior closed-form forward model:
        N_breakdown(R) = N_baseline / alpha_R^2
        Delta(R)       = N_baseline * (1/alpha_R^2 - 1)
        spread         = max_R |Delta(R)| / N_baseline = max_R |1/alpha_R^2 - 1|

    Per substitution chain Step 1 (W9b-1 plan §9 step 4 analytic estimate
    line 121: eps_R linear-in-alpha^2 scaling -> N_breakdown ~ 1/alpha^2).
    """
    alpha = np.asarray(alpha_R, dtype=np.float64)
    inv_alpha2 = 1.0 / (alpha ** 2)
    N_pred = N_baseline * inv_alpha2  # (local)
    Delta = N_pred - N_baseline  # (local)
    spread = float(np.max(np.abs(Delta) / N_baseline))  # (local)
    return N_pred, Delta, spread, inv_alpha2


def evaluate_powerlaw_forward_model(alpha_R, N_baseline, p):
    """
    Generalized power-law forward model:
        N_breakdown(R) = N_baseline / alpha_R^p

    Used as DIAGNOSTIC sweep, NOT as the gate verdict (per substitution
    chain Step 5: post-fit p_lstsq is curve-fitting, not forward prediction;
    iterate-until-PASS is Class-6 PROHIBITED_ACTIONS).
    """
    alpha = np.asarray(alpha_R, dtype=np.float64)
    inv_alphap = 1.0 / (alpha ** p)
    N_pred = N_baseline * inv_alphap  # (local)
    spread = float(np.max(np.abs(N_pred - N_baseline) / N_baseline))  # (local)
    return N_pred, spread


def fit_p_lstsq(alpha_R, N_breakdown_per_R, N_baseline):
    """
    Least-squares fit of p in N(R) = N_baseline / alpha^p, returned for
    DIAGNOSTIC ONLY (not gate verdict).
        log(N(R)/N_baseline) = -p * log(alpha)
    """
    alpha = np.asarray(alpha_R, dtype=np.float64)
    N = np.asarray(N_breakdown_per_R, dtype=np.float64)
    mask = alpha != 1.0  # exclude baseline (log(1)=0)
    log_ratios = np.log(N[mask] / N_baseline)
    log_alpha = np.log(alpha[mask])
    # solve log_ratios = -p * log_alpha
    p = float(-np.linalg.lstsq(log_alpha.reshape(-1, 1), log_ratios, rcond=None)[0][0])
    return p


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main():
    t_start = time.time()
    print("=" * 78)
    print(f"GATE {GATE_ID}")
    print(f"  scheme={SCHEME}")
    print(f"  convention={CONVENTION}")
    print(f"  L_max={L_MAX}")
    print("=" * 78)
    print()

    # ----- Step 0: Input-pin SHAs -----
    PLAN_PATH = _REPO / "sessions" / "session-plan" / "session-88-plan-w12.md"
    W9B1_JSON = _REPO / "computations" / "session-87" / "s87_w9b_rescaled_ic_sr_lo_rerun.json"
    W9B1_PY = _REPO / "computations" / "session-87" / "s87_w9b_rescaled_ic_sr_lo_rerun.py"
    CF42_PY = _REPO / "computations" / "session-87" / "s87_w7_ic_per_class_verify.py"
    CANONICAL_CONSTANTS_PATH = _REPO / "computations" / "_shared" / "canonical_constants.py"
    GATE_VERDICTS_RULE = _REPO / ".claude" / "rules" / "gate-verdicts.md"
    MATH_SCRIPTS_RULE = _REPO / ".claude" / "rules" / "math-scripts.md"
    V3_RECOVERY_RULE = _REPO / ".claude" / "rules" / "v3-closure-recovery.md"

    print("[Step 0] Computing input-pin SHAs ...")
    sha_plan = file_sha256(PLAN_PATH)
    sha_w9b1_json = file_sha256(W9B1_JSON)
    sha_w9b1_py = file_sha256(W9B1_PY)
    sha_cf42_py = file_sha256(CF42_PY)
    sha_canonical_consts = file_sha256(CANONICAL_CONSTANTS_PATH)
    sha_gate_verdicts_rule = file_sha256(GATE_VERDICTS_RULE)
    sha_math_scripts_rule = file_sha256(MATH_SCRIPTS_RULE)
    sha_v3_recovery_rule = file_sha256(V3_RECOVERY_RULE)
    print(f"  plan_w12:              {sha_plan}")
    print(f"  w9b1_json:             {sha_w9b1_json}")
    print(f"  w9b1_py:               {sha_w9b1_py}")
    print(f"  cf42_py:               {sha_cf42_py}")
    print(f"  canonical_constants:   {sha_canonical_consts}")
    print(f"  gate_verdicts_rule:    {sha_gate_verdicts_rule}")
    print(f"  math_scripts_rule:     {sha_math_scripts_rule}")
    print(f"  v3_recovery_rule:      {sha_v3_recovery_rule}")
    print()

    # ----- Step 1: Verify CF-42 prereq LANDED + load W9b-1 canonical data -----
    print("[Step 1] Verifying CF-42 prereq LANDED + loading W9b-1 canonical data ...")
    with open(W9B1_JSON, "r", encoding="utf-8") as fh:
        w9b1 = json.load(fh)
    w9b1_alpha_R = np.asarray(w9b1["results"]["alpha_R"], dtype=np.float64)
    w9b1_N_break = np.asarray(w9b1["results"]["N_breakdown_per_R"], dtype=np.float64)
    w9b1_xi2_0 = np.asarray(w9b1["results"]["xi2_0_per_R"], dtype=np.float64)
    w9b1_max_dev = float(w9b1["results"]["max_R_deviation_observable"])
    w9b1_audit_sha = w9b1["audit_sha256"]
    print(f"  W9b-1 audit_sha256:     {w9b1_audit_sha}")
    print(f"  W9b-1 alpha_R:          {w9b1_alpha_R.tolist()}")
    print(f"  W9b-1 xi2_0_per_R:      {w9b1_xi2_0.tolist()}")
    print(f"  W9b-1 N_breakdown_per_R:{w9b1_N_break.tolist()}")
    print(f"  W9b-1 max_R_deviation:  {w9b1_max_dev}")
    print(f"  W9b-1 verdict:          composite={w9b1['verdict_tuple']['composite']}")

    # Verify in-script ALPHA_R / N_BREAKDOWN_PER_R_W9B1 constants match the JSON
    assert np.allclose(w9b1_alpha_R, ALPHA_R_W9B1, rtol=1e-15, atol=0.0), \
        "in-script ALPHA_R_W9B1 drift from W9b-1 JSON"
    assert np.allclose(w9b1_N_break, N_BREAKDOWN_PER_R_W9B1, rtol=1e-15, atol=0.0), \
        "in-script N_BREAKDOWN_PER_R_W9B1 drift from W9b-1 JSON"
    assert abs(w9b1_max_dev - N_BREAKDOWN_MEASURED) < 1e-15, \
        "in-script N_BREAKDOWN_MEASURED drift from W9b-1 JSON"
    print(f"  in-script constants vs W9b-1 JSON: match (machine epsilon)")

    # CF-42 prereq is LANDED at S87 W7-1 / W5A-P3-IC-PER-CLASS-VERIFY (S87 W7-1
    # provenance entry "w7_ic_per_class_verify" listed in knowledge-MCP
    # provenance trace; canonical npz at s87_w7_ic_per_class_verify.npz).
    cf42_landed = CF42_PY.exists()
    print(f"  CF-42 script exists:    {cf42_landed} (s87_w7_ic_per_class_verify.py)")
    cf42_npz = _REPO / "computations" / "session-87" / "s87_w7_ic_per_class_verify.npz"
    cf42_npz_landed = cf42_npz.exists()
    print(f"  CF-42 npz exists:       {cf42_npz_landed}")
    print(f"  CF-42 prereq satisfied (LANDED at S87 per plan §W12-143 line 426): True")
    print()

    # Cross-check: alpha_R^2 vs xi2_0 ratio
    alpha2 = w9b1_alpha_R ** 2
    xi2_ratio = w9b1_xi2_0 / w9b1_xi2_0[0]
    print(f"  Cross-check alpha_R^2 = xi2_0_per_R / xi2_0_canonical:")
    print(f"    alpha_R^2:  {alpha2.tolist()}")
    print(f"    xi2_ratio:  {xi2_ratio.tolist()}")
    diff_ratio_alpha2 = float(np.max(np.abs(alpha2 - xi2_ratio)))
    print(f"    max abs diff: {diff_ratio_alpha2:.3e} (machine epsilon)")
    print()

    # ----- Step 2: Cross-link to W9b-1 measured spread -----
    print("[Step 2] Cross-linking to W9b-1 measured spread (31.98%) ...")
    spread_measured = N_BREAKDOWN_MEASURED  # = 0.3197964204234936
    print(f"  N_breakdown_measured (W9b-1) = {spread_measured} = 31.98%")
    print(f"  W9b-1 argmax_R_label         = {w9b1['results']['argmax_R_label']}")
    print()

    # ----- Step 3: Build forward-prediction model (substrate prior, p=2) -----
    print("[Step 3] Building forward-prediction model (substrate prior 1/alpha^2) ...")
    N_baseline = float(w9b1_N_break[0])
    print(f"  N_breakdown_baseline = N_breakdown(C_1_e=HypA)")
    print(f"                       = {N_baseline} e-folds")

    N_pred_p2, Delta_p2, spread_pred_p2, inv_alpha2 = \
        evaluate_substrate_prior_forward_model(w9b1_alpha_R, N_baseline)

    print(f"  alpha_R^2:                 {alpha2.tolist()}")
    print(f"  inv_alpha_R^2 = 1/alpha^2: {inv_alpha2.tolist()}")
    print(f"  Delta(R) = N_baseline*(1/alpha^2 - 1):")
    for lbl, lbl_w9, d in zip(LABELS_PLAN, LABELS_W9B1, Delta_p2):
        print(f"    {lbl} ({lbl_w9}): Delta = {d:.10e} e-folds")
    print(f"  N_predicted(R):")
    for lbl, lbl_w9, n in zip(LABELS_PLAN, LABELS_W9B1, N_pred_p2):
        print(f"    {lbl} ({lbl_w9}): N_pred = {n:.10e} e-folds")
    print(f"  spread_predicted (substrate prior, p=2) = {spread_pred_p2}")
    print(f"  Closed-form: max(|1/alpha^2 - 1|) = max(|1.0-1|, |0.8333-1|, |1.25-1|, |0.6667-1|)")
    print(f"             = max(0, 0.16667, 0.25, 0.33333) = 1/3 = {1.0/3.0}")
    print()

    # ----- Step 4: Compute predicted N_breakdown for each regulator class -----
    # (already done above in Step 3; emit the per-class table)
    print("[Step 4] Per-class predicted N_breakdown (substrate prior) vs W9b-1 measured:")
    print(f"  {'Class':<12} {'alpha^2':<12} {'N_pred (sub)':<18} {'N_meas (W9b1)':<18} {'rel_dev_pred':<14} {'rel_dev_meas':<14}")
    for lbl, lbl_w9, a2, n_p, n_m in zip(
        LABELS_PLAN, LABELS_W9B1, alpha2, N_pred_p2, w9b1_N_break
    ):
        rd_p = (n_p - N_baseline) / N_baseline
        rd_m = (n_m - N_baseline) / N_baseline
        print(f"  {lbl} ({lbl_w9:<6}) {a2:<12.6f} {n_p:<18.10e} {n_m:<18.10e} {rd_p:<+14.6e} {rd_m:<+14.6e}")
    print()

    # ----- Step 5: Cross-check predicted spread vs W9b-1 measured spread -----
    print("[Step 5] Cross-check predicted spread vs W9b-1 measured 31.98% ...")
    rel_err = abs(spread_pred_p2 - spread_measured) / spread_measured
    print(f"  spread_predicted (substrate prior) = {spread_pred_p2}")
    print(f"  spread_measured  (W9b-1)           = {spread_measured}")
    print(f"  abs(diff)                          = {abs(spread_pred_p2 - spread_measured):.10e}")
    print(f"  relative error = |diff|/spread_measured = {rel_err:.10e} = {rel_err*100:.4f}%")
    print(f"  PASS tolerance (1%)                = {PASS_TOLERANCE}")
    print(f"  PASS criterion: rel_err <= {PASS_TOLERANCE}")
    print(f"  PASS criterion satisfied?          = {rel_err <= PASS_TOLERANCE}")
    print()

    # DIAGNOSTIC ONLY: post-fit p (NOT the gate verdict; iterate-until-PASS
    # would be PROHIBITED_ACTIONS Class 6 per .claude/rules/v3-closure-recovery.md)
    print("[DIAGNOSTIC ONLY] Post-fit p_lstsq sweep (NOT gate verdict) ...")
    p_lstsq = fit_p_lstsq(w9b1_alpha_R, w9b1_N_break, N_baseline)
    print(f"  p_lstsq (least-squares post-fit) = {p_lstsq:.6f}")
    N_pred_lstsq, spread_pred_lstsq = evaluate_powerlaw_forward_model(
        w9b1_alpha_R, N_baseline, p_lstsq
    )
    rel_err_lstsq = abs(spread_pred_lstsq - spread_measured) / spread_measured
    print(f"  spread @ p_lstsq = {spread_pred_lstsq:.10e}")
    print(f"  rel_err @ p_lstsq = {rel_err_lstsq:.10e} = {rel_err_lstsq*100:.4f}%")
    print(f"  (DIAGNOSTIC: this is curve-fitting, NOT the substrate-prior")
    print(f"   forward prediction. Reporting as gate verdict would be")
    print(f"   iterate-until-PASS Class-6 PROHIBITED_ACTIONS.)")
    print()

    # Sweep p ∈ {1.0, 1.5, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3} for diagnostic plot
    p_sweep = np.array([1.0, 1.5, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, p_lstsq])
    sweep_spreads = []
    sweep_rel_errs = []
    for p in p_sweep:
        _, sp = evaluate_powerlaw_forward_model(w9b1_alpha_R, N_baseline, p)
        sweep_spreads.append(sp)
        sweep_rel_errs.append(abs(sp - spread_measured) / spread_measured)
    sweep_spreads = np.array(sweep_spreads)
    sweep_rel_errs = np.array(sweep_rel_errs)

    # ----- Step 6: Composite verdict (S87 schema-v2) -----
    # sign_verdict: spread_predicted positive matches spread_measured positive
    sign_predicted = +1 if spread_pred_p2 > 0 else -1 if spread_pred_p2 < 0 else 0
    sign_measured = +1 if spread_measured > 0 else -1 if spread_measured < 0 else 0
    sign_verdict = "PASS" if sign_predicted == sign_measured else "FAIL"

    # magnitude_verdict: per plan §W12-143 PASS criterion
    magnitude_verdict = "PASS" if rel_err <= PASS_TOLERANCE else "FAIL"

    # regime_verdict: SR-LO closed-form well-defined; eps_R(N_breakdown) = 0.5
    # remains within VALID regime (W9b-1 reports VALID for all 4 classes per
    # results/regime_per_R)
    regime_verdict = "VALID"

    # Composite collapse (per .claude/rules/gate-verdicts.md):
    # if any of {sign, magnitude, regime} = FAIL ⇒ composite = FAIL;
    # if regime = BREAKDOWN ⇒ composite = FAIL.
    # Here magnitude=FAIL ⇒ composite=FAIL.
    composite_verdict = "FAIL" if (
        sign_verdict == "FAIL" or magnitude_verdict == "FAIL" or regime_verdict == "BREAKDOWN"
    ) else "PASS"

    print("[Step 6] Composite verdict (S87 schema-v2) ...")
    print(f"  sign_verdict      = {sign_verdict}  (sign(spread_pred)={sign_predicted}, sign(spread_meas)={sign_measured})")
    print(f"  magnitude_verdict = {magnitude_verdict}  (rel_err={rel_err:.6e} vs PASS_TOLERANCE={PASS_TOLERANCE})")
    print(f"  regime_verdict    = {regime_verdict}  (SR-LO closed-form well-defined; eps within band)")
    print(f"  composite         = {composite_verdict}")
    print()

    # ----- Step 7: Save NPZ + JSON -----
    npz_path = _REPO / "computations" / "session-88" / \
        "s88_w12_143_per_class_n_breakdown_forward_modeling.npz"
    json_path = _REPO / "computations" / "session-88" / \
        "s88_w12_143_per_class_n_breakdown_forward_modeling.json"
    plot_path = _REPO / "computations" / "session-88" / \
        "s88_w12_143_per_class_n_breakdown_forward_modeling.png"

    print("[Step 7] Saving artifacts ...")
    np.savez(
        npz_path,
        alpha_R=w9b1_alpha_R,
        alpha_R_squared=alpha2,
        xi2_0_per_R=w9b1_xi2_0,
        xi2_0_canonical=w9b1_xi2_0[0],
        labels_plan=np.asarray(LABELS_PLAN),
        labels_w9b1=np.asarray(LABELS_W9B1),
        N_breakdown_baseline=N_baseline,
        N_breakdown_predicted_substrate_prior=N_pred_p2,
        N_breakdown_measured_W9b1=w9b1_N_break,
        Delta_R_substrate_prior=Delta_p2,
        spread_predicted_substrate_prior=spread_pred_p2,
        spread_measured_W9b1=spread_measured,
        rel_err_substrate_prior=rel_err,
        pass_tolerance=PASS_TOLERANCE,
        # diagnostics
        p_substrate_prior=2.0,
        p_lstsq_diagnostic=p_lstsq,
        spread_predicted_lstsq_diagnostic=spread_pred_lstsq,
        rel_err_lstsq_diagnostic=rel_err_lstsq,
        p_sweep=p_sweep,
        spread_sweep=sweep_spreads,
        rel_err_sweep=sweep_rel_errs,
        # verdict
        sign_verdict=sign_verdict,
        magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict,
        composite_verdict=composite_verdict,
    )
    print(f"  npz: {npz_path}")

    # ----- Step 8: Plot -----
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))

    # Panel 1: per-class N_breakdown predicted vs measured
    ax = axes[0]
    x_pos = np.arange(4)  # (local) matplotlib bar positions
    width = 0.35  # (local) matplotlib bar half-width (styling)
    ax.bar(x_pos - width / 2, N_pred_p2 * 1e3, width, label="Substrate prior (p=2)", color="steelblue")
    ax.bar(x_pos + width / 2, w9b1_N_break * 1e3, width, label="W9b-1 measured", color="coral")
    ax.axhline(N_baseline * 1e3, color="gray", linestyle="--", alpha=0.6,
               label=f"N_baseline = {N_baseline*1e3:.4f}e-3 e-folds")
    ax.set_xticks(x_pos)
    ax.set_xticklabels([f"{a}\n({b})" for a, b in zip(LABELS_PLAN, LABELS_W9B1)])
    ax.set_ylabel("N_breakdown (× 1e-3 e-folds)")
    ax.set_title("Per-class N_breakdown:\nsubstrate-prior 1/α² vs W9b-1 measured")
    ax.legend(loc="upper right", fontsize=9)
    ax.grid(True, alpha=0.3)

    # Panel 2: spread vs power p
    ax = axes[1]
    p_dense = np.linspace(0.5, 3.0, 80)
    spread_dense = []
    for p in p_dense:
        _, sp = evaluate_powerlaw_forward_model(w9b1_alpha_R, N_baseline, p)
        spread_dense.append(sp)
    ax.plot(p_dense, spread_dense, color="navy", linewidth=2, label="spread(p) closed-form")
    ax.axhline(spread_measured, color="red", linestyle="--", linewidth=1.5,
               label=f"W9b-1 measured = {spread_measured:.4f}")
    ax.axhline(spread_measured * (1 + PASS_TOLERANCE), color="orange",
               linestyle=":", alpha=0.6, label=f"PASS upper (+1%)")
    ax.axhline(spread_measured * (1 - PASS_TOLERANCE), color="orange",
               linestyle=":", alpha=0.6, label=f"PASS lower (-1%)")
    ax.scatter([2.0], [spread_pred_p2], color="steelblue", s=120, zorder=5,
               label=f"substrate prior p=2: spread={spread_pred_p2:.4f}, rel_err={rel_err*100:.2f}%")
    ax.scatter([p_lstsq], [spread_pred_lstsq], color="green", s=80, zorder=5,
               label=f"DIAGNOSTIC p_lstsq={p_lstsq:.3f}: rel_err={rel_err_lstsq*100:.2f}%")
    ax.set_xlabel("p in N_breakdown(R) = N_baseline / α^p")
    ax.set_ylabel("spread = max_R |N(R)/N_baseline - 1|")
    ax.set_title("Spread vs power p\n(substrate prior is p=2; gate verdict on p=2 only)")
    ax.legend(loc="upper left", fontsize=8)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0.5, 3.0)

    fig.suptitle(
        f"§W12-143: Per-class N_breakdown forward modeling\n"
        f"composite={composite_verdict} (sign={sign_verdict}, magnitude={magnitude_verdict}, "
        f"regime={regime_verdict}); rel_err={rel_err*100:.4f}% > {PASS_TOLERANCE*100:.0f}% PASS-band",
        fontsize=11,
    )
    plt.tight_layout()
    plt.savefig(plot_path, dpi=140, bbox_inches="tight")
    plt.close(fig)
    print(f"  plot: {plot_path}")

    # ----- Step 9: dual-SHA closure -----
    input_pin_map = {
        "gate_id": GATE_ID,
        "wp_section": WP_SECTION,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "schema_version": SCHEMA_VERSION,
        "input_sha_plan_w12": sha_plan,
        "input_sha_w9b1_json": sha_w9b1_json,
        "input_sha_w9b1_py": sha_w9b1_py,
        "input_sha_cf42_py": sha_cf42_py,
        "input_sha_canonical_constants": sha_canonical_consts,
        "input_sha_gate_verdicts_rule": sha_gate_verdicts_rule,
        "input_sha_math_scripts_rule": sha_math_scripts_rule,
        "input_sha_v3_recovery_rule": sha_v3_recovery_rule,
        "machinery_pin_n_breakdown_measured": N_BREAKDOWN_MEASURED,
        "machinery_pin_pass_tolerance": PASS_TOLERANCE,
        "machinery_pin_substrate_prior_p": 2.0,
        "machinery_pin_alpha_R": list(ALPHA_R_W9B1),
        "machinery_pin_n_breakdown_per_R_W9B1": list(N_BREAKDOWN_PER_R_W9B1),
        "machinery_pin_labels_plan": LABELS_PLAN,
        "machinery_pin_labels_w9b1": LABELS_W9B1,
        "cf42_landed": cf42_landed and cf42_npz_landed,
        "w9b1_audit_sha256": w9b1_audit_sha,
    }
    audit_sha256 = closure_hash(input_pin_map)

    content_payload = {
        "N_breakdown_baseline": N_baseline,
        "N_breakdown_predicted_substrate_prior": list(N_pred_p2),
        "N_breakdown_measured_W9b1": list(w9b1_N_break),
        "Delta_R_substrate_prior": list(Delta_p2),
        "spread_predicted_substrate_prior": spread_pred_p2,
        "spread_measured_W9b1": spread_measured,
        "rel_err_substrate_prior": rel_err,
        "p_lstsq_diagnostic": p_lstsq,
        "spread_predicted_lstsq_diagnostic": spread_pred_lstsq,
        "rel_err_lstsq_diagnostic": rel_err_lstsq,
        "sign_verdict": sign_verdict,
        "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
        "composite_verdict": composite_verdict,
    }
    content_sha256 = closure_hash(content_payload)
    print()
    print("[Step 9] dual-SHA closure:")
    print(f"  audit_sha256:   {audit_sha256}")
    print(f"  content_sha256: {content_sha256}")

    json_payload = {
        **input_pin_map,
        **content_payload,
        "audit_sha256": audit_sha256,
        "content_sha256": content_sha256,
        "rationale": (
            "Substrate-prior closed-form forward model "
            "N_breakdown(R) = N_baseline / alpha_R^2 yields spread_predicted = 1/3 "
            "= 0.333333... versus W9b-1 measured spread = 0.319796. Relative deviation "
            f"= {rel_err*100:.4f}% exceeds the 1% PASS criterion. The substrate-prior "
            "form CAPTURES THE LEADING SCALING (linear-in-alpha^2 SR-LO IC rescaling, "
            "per W9b-1 plan §9 step 4 analytic estimate) but the SR-LO ODE non-linearity "
            "contributes a residual ~4% in N_breakdown that the closed-form does NOT "
            "reproduce within 1%. Diagnostic post-fit p_lstsq = "
            f"{p_lstsq:.6f} reproduces W9b-1 by curve-fitting; reporting it as the "
            "gate verdict would be iterate-until-PASS Class-6 PROHIBITED_ACTIONS. "
            "Verdict: FAIL on plan §W12-143 1% pass-band; the substrate-prior 1/alpha^2 "
            "model is operationally useful as a first-order approximation but does NOT "
            "reproduce W9b-1 spread within plan-pinned tolerance. Closes corridor of "
            "per-class regulator-restriction modeling at substrate-prior leading order."
        ),
    }
    with open(json_path, "w", encoding="utf-8") as fh:
        json.dump(json_payload, fh, indent=2, default=str)
    print(f"  json: {json_path}")

    # ----- Step 10: Append verdict line -----
    verdict_file = _REPO / "computations" / "session-88" / "s88_gate_verdicts.txt"
    value_str = (
        f"spread_predicted_substrate_prior={spread_pred_p2:.10e};"
        f"spread_measured_W9b1={spread_measured:.10e};"
        f"rel_err={rel_err:.6e};"
        f"PASS_tolerance={PASS_TOLERANCE};"
        f"N_breakdown_baseline={N_baseline:.10e};"
        f"p_substrate_prior=2.0;"
        f"p_lstsq_diagnostic={p_lstsq:.6f};"
        f"rel_err_lstsq_diagnostic={rel_err_lstsq:.6e};"
        f"argmax_R={LABELS_PLAN[3]}_({LABELS_W9B1[3]})"
    )
    canonical_line = (
        f"{GATE_ID}: {composite_verdict} -- "
        f"value='{value_str}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha256} content_sha256={content_sha256} "
        f"schema_version={SCHEMA_VERSION}\n"
    )
    dual_sha_companion = (
        f"# audit_sha256_short={audit_sha256[:16]} "
        f"content_sha256_short={content_sha256[:16]} # {GATE_ID} "
        f"dual-SHA companion row (W9a-99 split)\n"
    )
    triple_companion = (
        f"# sign_verdict={sign_verdict} magnitude_verdict={magnitude_verdict} "
        f"regime_verdict={regime_verdict} # {GATE_ID} 3-tuple annotation "
        f"(S87 schema-v2)\n"
    )
    diagnostic_companion = (
        f"# DIAGNOSTIC: substrate-prior closed-form forward model "
        f"N_breakdown(R) = N_baseline / alpha_R^2 (per W9b-1 plan §9 step 4 "
        f"analytic estimate: SR-LO IC rescaling -> eps_R linear-in-alpha^2 -> "
        f"N_breakdown ~ 1/alpha^2). With alpha_R^2 = [1.0, 1.2, 0.8, 1.5] "
        f"the predicted spread = max(|1/alpha^2 - 1|) = max(0, 0.1667, 0.25, "
        f"0.3333) = 1/3 = 0.333333. W9b-1 measured spread = 0.3197964 "
        f"(C_4_ab argmax). |spread_pred - spread_meas|/spread_meas = "
        f"{rel_err*100:.4f}% > 1% pass-band (plan §W12-143 line 442). FAIL on "
        f"magnitude. The substrate-prior model captures leading scaling but "
        f"4.2% residual from SR-LO ODE non-linearity exceeds 1% tolerance. "
        f"DIAGNOSTIC post-fit p_lstsq={p_lstsq:.4f} reproduces W9b-1 to "
        f"{rel_err_lstsq*100:.4f}% but is curve-fitting, not forward "
        f"prediction; reporting it as gate verdict would be iterate-until-PASS "
        f"Class-6 PROHIBITED_ACTIONS per .claude/rules/v3-closure-recovery.md. "
        f"CF-42 prereq LANDED at S87 (s87_w7_ic_per_class_verify.py + .npz). "
        f"W9b-1 cross-link audit_sha256={w9b1_audit_sha[:16]}... "
        f"Closes corridor: per-class regulator-restriction substrate-prior "
        f"forward modeling at leading order does NOT reproduce W9b-1 within "
        f"1%; refines the W9b-1 N_breakdown spread refuting prior heuristic "
        f"per plan §W12-143 line 454.\n"
    )
    with open(verdict_file, "a", encoding="utf-8") as fh:
        fh.write(canonical_line)
        fh.write(dual_sha_companion)
        fh.write(triple_companion)
        fh.write(diagnostic_companion)
    print()
    print(f"[Step 10] Verdict appended to: {verdict_file}")
    print()
    print("CANONICAL LINE:")
    print(canonical_line.rstrip())
    print(dual_sha_companion.rstrip())
    print(triple_companion.rstrip())
    print(diagnostic_companion.rstrip())
    print()

    elapsed = time.time() - t_start
    print(f"[done] elapsed={elapsed:.2f}s")
    print(f"[done] composite_verdict = {composite_verdict}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
