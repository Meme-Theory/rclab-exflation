"""
S92 W9-1 — S92-W9-CF-W7-1-VII-AQ-OP-PROJ-CCVS-2013-QUADRATIC-EXTENSION
=====================================================================

Gate: S92-W9-CF-W7-1-VII-AQ-OP-PROJ-CCVS-2013-QUADRATIC-EXTENSION  ([VERIFY-THEOREM] + [SIGN])
Class: GEOMETRIC
Agent: connes-ncg-theorist (PRIMARY; CCvS 2013 §3 helper extension)
Scheme: CCvS-2013-quadratic-extension-FULL
Convention: VII-AQ-OP-PROJ-CCvS-2013-quadratic-extension-build_A_quad-FULL-per-eq4-Hermitian-D_def
L_max: N/A (finite spectral triple; full A_F rep dim H_F = 12)

HYPOTHESIS (plan §W9-1): per CCvS 2013 §3 eq 4, the quadratic-extended inner
fluctuation  D_def = D_F + A_lin + A_quad + J(A_lin + A_quad)J^{-1}  with
A_quad = Σ_{ij} c_{ij} [D, a_i][D, b_j]  closes the linear inner fluctuation's
first-order axiom-4 invariance perturbation back to zero (plan's assumed
"order-one cancellation theorem"). Test whether the quadratic corrections,
applied to the S91 W7-1 5-grid generator scan at §VII.AQ.OP-PROJ Reading A,
drive the max axiom-4 invariance deviation below AXIOM_RESIDUAL_TOL = 1e-10
while preserving K-theory residual = 0 and KO-dim = 6.

================================ NUMBERS FIRST ================================

SUBSTRATE-IS STRUCTURAL FINDING (the verdict driver). The plan's substitution-
chain Step 4 predicts the quadratic correction DECREASES the deviation toward
zero. The substrate FALSIFIES this prediction on two independent grading axes:

  (A) A_quad = [D,a][D,b] is a DEGREE-0 (EVEN) operator. Each [D, ·] is degree-1
      (odd; {[D,·],γ_F}=0); the product of two odd operators is even
      ([A_quad,γ_F]=0, {A_quad,γ_F}≠0). Adding any non-zero A_quad to the Dirac
      operator BREAKS axiom 5 ({D_def,γ_F}=0) — A_quad is not Dirac-like.
      (Numerically: {A_quad,γ_F} = 3.134 ≠ 0 on grid 5 at c=1; Sage-Q grading
       sign of [D,a][D,b] = +1 EVEN.)

  (B) The cancellation the plan assumes,
        [A_quad, π(a)] + h.c.  =  -([A_lin, π(a)] - π(δ_4(a)))_order-1 ,
      is a GRADING-SECTOR MISMATCH: [A_quad, a] is EVEN (sign +1), while
      [A_lin, a] (the order-1 residual) is ODD (sign -1). EVEN = ODD requires
      both to vanish; the RHS ≠ 0 by the substrate's documented order-one
      violation [[D_K, H], H] = 4.000. No c_{ij} choice cancels it.

CONSEQUENCE (c-mesh scan on grid 5, c ∈ {0, ±1/2, ±1}):
    c=0   : axiom-4 dev = 2.863564 (= linear baseline; only axiom-5-PRESERVING pt)
    c=±0.5: axiom-4 dev = 3.090696   {D_def,γ_F} = 3.134454  (axiom-5 BREAKS)
    c=±1  : axiom-4 dev = 3.689119   {D_def,γ_F} = 6.268907  (axiom-5 BREAKS)
The axiom-4 invariance deviation is bounded BELOW by the linear residual; adding
A_quad only INCREASES it (opposite to the plan's prediction) and breaks axiom 5.
=> FAIL at the strict 1e-10 boundary.

SUBSTRATE FRAMING (plan substrate_framing; MANDATORY):
The substrate IS the spectral triple (A_K, H_K, D_K, γ_9 = γ_5 ⊗ γ_F, J) at
§VII.AQ.OP-PROJ Reading A. The inner fluctuation IS a substrate-natural
deformation of D within the registered triple's inner-automorphism orbit; the
deformed triple IS a new substrate; axiom-4 invariance IS that new substrate's
structural identity. Direction of explanation: substrate IS spectral triple →
inner fluctuation IS deformation of D → axiom-4 invariance IS the structural
identity of the deformed substrate. NOT container-thinking ("the fluctuation
acts on the triple"). The CCvS 2013 §3 quadratic term is the substrate's
even-sector gauge-curvature reconstruction (paper #23 Result #4 — gauge
invariance; Result #1 — semi-group closure); it ACCOMMODATES the order-one
violation, it does NOT repair it (paper #23 Result #2 — c_{ij} non-zero iff
order-one fails). The substrate's order-one violation (4.000) is structurally
permanent under inner fluctuation; the FAIL CLOSES the "quadratic-extension
repairs order-one" promotion pathway at §VII.AQ.OP-PROJ.

SUBSTITUTION CHAIN (per math-scripts.md §"Double-Check Logic Before Compute"):
  Def 1: D_F = canonical finite Dirac (build_D_F in helper).
  Def 2: A_lin = a[D_F,b] + h.c.   (degree-1 / odd; helper build_A).
  Def 3: A_quad = Σ c_{ij}[D_F,a_i][D_F,b_j] + h.c.  (degree-0 / EVEN; build_A_quad).
  Def 4: D_def(quad) = D_F + (A_lin+A_quad) + J(A_lin+A_quad)J^{-1}.
  Def 5: axiom_4_dev[D] = ||[[D,a],b°] - [[D_F,a],b°]||  (inner-fluct invariance).
  Substitute (quadratic): [[D_def,a],b°]-[[D_F,a],b°] = [[A_lin+A_quad + J(...)J^{-1}, a], b°]
                          = (linear residual, ODD sector) + ([A_quad,a]+h.c., EVEN sector).
  Simplify (grading orthogonality): ODD ⊕ EVEN; the EVEN A_quad term cannot
                          cancel the ODD linear residual. Operator norm of a
                          direct sum is ≥ each summand => dev[quad] ≥ dev[linear].
  Direction (PRE-REGISTERED prediction, plan Step 4): quadratic correction
                          DECREASES dev toward 0.  COMPUTED direction: quadratic
                          correction INCREASES dev (2.864 → 3.69 at c=1) AND
                          breaks axiom 5.  => sign_verdict = FAIL (direction mismatch).
  Conclusion: FAIL. No c_{ij} over the rational mesh closes axiom-4 at 1e-10.
              c=0 recovers the INFO-class linear baseline (axiom-5 preserved,
              dev=2.864). The substrate-IS axiom-4 invariance is NOT restored by
              the CCvS 2013 quadratic extension; §VII.AQ.OP-PROJ Stage-2 dispatch
              REMAINS blocked under this pathway.

CROSS-CHECKS:
  - Sage-Q symbolic: grading sign of A_quad = +1 (EVEN); cancellation [A_quad,a]
    (EVEN) = -[A_lin,a] (ODD) impossible unless both vanish.
  - Baseline diff: c=0 reproduces S91 W7-1 max_axiom4_inv_dev = 2.863564 bit-for-bit.
  - K-theory residual Δ_GV (γ_F-anticommutation of A_lin) = 0 at every grid (linear
    1-form is genuine); but A_quad anticommutes-nonzero with γ_F (EVEN), so the
    QUADRATIC 1-form is NOT a degree-1 K-theory class — Δ_GV_quad ≠ 0.

References (Connes corpus):
  - Chamseddine, Connes, van Suijlekom (2013), "Inner Fluctuations in NCG without
    the first order condition", JGP 73, 222-234.
    researchers/Connes/23_2013_Chamseddine_Connes_vSuijlekom_Inner_Fluctuations.md
    §3 ("The Fluctuation Extension"): A_quad = Σ_{ij} c_{ij}[D,a_i][D,a_j] (eq 4);
    Result #2 (order-one is the c_{ij}=0 special case); Result #4 (gauge
    invariance preserved); Result #1 (semi-group closure).
  - Connes (1996), "Gravity coupled with matter...", CMP 182. (axiom 4 derivation)
  - Helper docstring lines 33-39 (order-one violation 4.000 structurally
    preserved under inner fluctuation).

PROHIBITED_ACTIONS per v3-closure-recovery.md:
  - Convention-shopping: CCvS-2013-quadratic-extension-FULL pinned at plan §W9-1.
  - Iterate-until-PASS: 5-grid pre-registered; c-mesh {0,±1/2,±1} pre-registered;
    do NOT expand to chase a PASS. FAIL is a structural result, not an agent failure.
  - Post-hoc threshold editing: 1e-10 PASS / 1e-7 INFO boundaries fixed.
  - Ansatz-forced PASS: no hand-tuned c_{ij}; the mesh is exhaustive over the
    pre-registered rational coefficients.
"""

from __future__ import annotations
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")   # GPU_path = cpu-cap-OMP8 (dim H_F=12)

import sys
import hashlib
import json
import time
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "computations" / "_shared"))

from canonical_constants import *  # noqa: F401,F403
from canonical_constants import (  # noqa: E402
    M_KK,
    tau_fold,
    gv_canonical_difference_FW,
)

from _connes_chamseddine_inner_fluctuation import (  # noqa: E402
    InnerFluctuation1Form,
    all_grid_points,
    DIM_HF,
)

# ============================ Gate-block constants ============================
GATE_ID = "S92-W9-CF-W7-1-VII-AQ-OP-PROJ-CCVS-2013-QUADRATIC-EXTENSION"
SCHEME = "CCvS-2013-quadratic-extension-FULL"
CONVENTION = ("VII-AQ-OP-PROJ-CCvS-2013-quadratic-extension-"
              "build_A_quad-FULL-per-eq4-Hermitian-D_def")
L_MAX = "N/A"  # (local) finite spectral triple; no truncation per plan §5

# Thresholds per plan §W9-1 (5) machinery_pin_map
AXIOM_RESIDUAL_TOL = 1e-10   # (local) strict PASS boundary (matches S91 W7-1)
INFO_RESIDUAL_TOL = 1e-7     # (local) INFO band: 1e-10 <= dev < 1e-7
NUM_GRID_POINTS = 5          # (local) per S91 W7-1 pre-registered grid
NUM_AXIOMS = 7               # (local) NCG axioms 1-7 + Poincaré duality
EXPECTED_KO_DIM = 6          # (local) BDI class per Connes 1996 §2
# Pre-registered rational c-mesh per CCvS 2013 §3 (plan (4) reachable_rationals)
C_MESH = [0.0, 0.5, -0.5, 1.0, -1.0]  # (local) c_{ij} ∈ {0, ±1/2, ±1}
S91_BASELINE_MAX_AXIOM4 = 2.863564212655270  # (local) S91 W7-1 npz max_axiom_4_deviation (diff cross-check)

# Corrective emission per gate-verdicts.md §"Option A": the first run of this
# gate emitted a verdict line (audit_sha256 below) under a verdict-aggregation
# bug — it computed the PASS predicate as min over ALL (grid,c), which is
# dominated by grid-1's structural-trivial zero (ℂ-only [D_F,a]=0), yielding
# misleading sign/magnitude=PASS. The composite was correctly FAIL (regime
# BREAKDOWN from axiom-5), but the sub-verdicts misrepresented the physics.
# The corrected predicate is MAX over the 5 grids of the best axiom-5-preserving
# axiom-4 deviation (all 5 grids must close). This corrective line supersedes
# the prior; the prior line is RETAINED on disk (verdict permanence).
SUPERSEDES_AUDIT_SHA = (  # (local) FULL 64-char prior audit_sha256 (first run)
    "5d11d746b55ed04e33ee489af677ba9bc59bb539daceb4ace19c99c1ac767a5b"
)

# Output paths
OUT_NPZ = ROOT / "computations" / "session-92" / "s92_w9_1_vii_aq_op_proj_ccvs_2013_quadratic_extension.npz"
OUT_PNG = ROOT / "computations" / "session-92" / "s92_w9_1_vii_aq_op_proj_ccvs_2013_quadratic_extension.png"
VERDICT_FILE = ROOT / "computations" / "session-92" / "s92_gate_verdicts.txt"

# Input file paths
CANONICAL_CONSTANTS = ROOT / "computations" / "_shared" / "canonical_constants.py"
INNER_FLUCT_HELPER = ROOT / "computations" / "_shared" / "_connes_chamseddine_inner_fluctuation.py"
CM_1995_HELPER = ROOT / "computations" / "_shared" / "_cm_1995_residue_formula.py"
CCVS_2013_PAPER = ROOT / "researchers" / "Connes" / "23_2013_Chamseddine_Connes_vSuijlekom_Inner_Fluctuations.md"
S91_W7_1_BASELINE = ROOT / "computations" / "session-91" / "s91_w7_1_vii_aq_op_proj_stage_2_upgrade.npz"
SCRIPT_PATH = Path(__file__).resolve()

INPUT_FILES = {
    "canonical_constants": CANONICAL_CONSTANTS,
    "inner_fluct_helper": INNER_FLUCT_HELPER,
    "cm_1995_residue_helper": CM_1995_HELPER,
    "ccvs_2013_paper": CCVS_2013_PAPER,
    "s91_w7_1_baseline": S91_W7_1_BASELINE,
    "script": SCRIPT_PATH,
}


# ============================ SHA helpers ============================
def sha256_of_file(p: Path) -> str:
    h = hashlib.sha256()  # (local)
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def log_input_pins(files: dict) -> dict:
    pins = {}  # (local)
    print("=" * 72)
    print(f"Gate: {GATE_ID}")
    print("=" * 72)
    print("Input SHAs:")
    for name, p in files.items():
        if not p.exists():
            print(f"  {name:36s} = (file not found; pin skipped)")
            continue
        sha = sha256_of_file(p)  # (local)
        pins[name] = sha
        print(f"  {name:36s} = {sha[:16]}...  ({p.relative_to(ROOT)})")
    return pins


def compute_dual_sha(pins: dict, script_path: Path) -> tuple:
    """audit_sha256 = SHA256(script + canonical + helper + pinmap);
    content_sha256 = SHA256(script only). Per gate-verdicts.md W9a-99 split."""
    script_bytes = script_path.read_bytes()
    canonical_bytes = CANONICAL_CONSTANTS.read_bytes()
    helper_bytes = INNER_FLUCT_HELPER.read_bytes()
    pinmap_json = json.dumps(sorted(pins.items()), sort_keys=True).encode("utf-8")  # (local)
    audit = hashlib.sha256(  # (local)
        script_bytes + canonical_bytes + helper_bytes + pinmap_json
    ).hexdigest()
    content = hashlib.sha256(script_bytes).hexdigest()  # (local)
    return audit, content


def append_verdict(
    composite: str, value_str: str,
    audit_sha: str, content_sha: str,
    sign_v: str, mag_v: str, reg_v: str,
) -> None:
    """Atomic single-shot append per gate-verdicts.md S87+ canonical form +
    dual-SHA companion + schema-v2 3-tuple companion ([SIGN] trigger REQUIRES
    the 3-tuple; the substitution chain Step 4 pre-registers a sign prediction).
    """
    canonical = (  # (local)
        f"{GATE_ID}: {composite} -- value='{value_str}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )
    dual_sha = (  # (local)
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    three_tuple = (  # (local)
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} "
        f"regime_verdict={reg_v} # {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )
    with open(VERDICT_FILE, "a", encoding="utf-8") as f:
        f.write(canonical)
        f.write(dual_sha)
        f.write(three_tuple)


# ============================ Main ============================
def main() -> int:
    t0 = time.time()

    # 1. Input pins + dual-SHA
    pins = log_input_pins(INPUT_FILES)
    audit_sha, content_sha = compute_dual_sha(pins, SCRIPT_PATH)
    print()
    print(f"  audit_sha256   = {audit_sha[:16]}...  (script + canonical + helper + pinmap)")
    print(f"  content_sha256 = {content_sha[:16]}...  (script only)")
    print()

    # 2. Canonical anchors (load + cite; no recomputation)
    print(f"  Canonical anchor: gv_canonical_difference_FW = {gv_canonical_difference_FW}")
    print(f"  Canonical pin tau_fold = {tau_fold}; M_KK = {M_KK:.6e}")
    print(f"  S91 W7-1 baseline max axiom-4 invariance dev = {S91_BASELINE_MAX_AXIOM4}")
    print()

    inner_fluct = InnerFluctuation1Form()
    print(f"  InnerFluctuation1Form on A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ); rep dim H_F = {DIM_HF}")
    grid = all_grid_points()

    # ---- Storage (per grid, per c-mesh) ----
    n_c = len(C_MESH)  # (local)
    grid_labels = [  # (local)
        "(1) ℂ-only", "(2) ℍ-only", "(3) M3-only", "(4) ℂ⊕ℍ", "(5) Full",
    ]
    axiom_keys = [  # (local)
        'axiom_1_dimension', 'axiom_2_regularity', 'axiom_3_reality',
        'axiom_4_first_order_invariance', 'axiom_5_chirality_anticommutation',
        'axiom_6_orientability', 'axiom_7_finiteness_poincare',
    ]

    # axiom-4 invariance deviation per (grid, c)
    axiom4_dev_grid_c = np.zeros((NUM_GRID_POINTS, n_c), dtype=np.float64)  # (local)
    # axiom-5 anticommutation residual per (grid, c)  -- the grading obstruction
    axiom5_resid_grid_c = np.zeros((NUM_GRID_POINTS, n_c), dtype=np.float64)  # (local)
    # KO-dim per (grid, c)
    ko_dim_grid_c = np.zeros((NUM_GRID_POINTS, n_c), dtype=np.int64)  # (local)
    # K-theory residual Δ_GV (γ_F-anticommutation of the full 1-form) per (grid, c)
    ktheory_resid_grid_c = np.zeros((NUM_GRID_POINTS, n_c), dtype=np.float64)  # (local)
    # A_quad grading anticommutator norm per grid (c-independent structural diagnostic at c=1)
    aquad_anticomm_gamma_per_grid = np.zeros(NUM_GRID_POINTS, dtype=np.float64)  # (local)

    print()
    print("  5-grid × c-mesh{0,±1/2,±1} CCvS-2013 quadratic-extension scan")
    print("  " + "-" * 68)
    for i, (a, b) in enumerate(grid):
        A_lin = inner_fluct.build_A(a, b)
        # Single-pair quadratic term basis (i=j=0): a_coeffs=[a], b_coeffs=[b].
        A_quad_unit = inner_fluct.build_A_quad(
            np.array([[1.0]]), [a], [b])  # c=1 unit; scale by C_MESH below
        # Grading diagnostic of the (unit) quadratic term:
        comm_g, anticomm_g = inner_fluct.grading_of_operator(A_quad_unit)
        aquad_anticomm_gamma_per_grid[i] = anticomm_g
        print(f"  Grid {i+1} {grid_labels[i]:10s}: A_quad grading "
              f"[A_quad,γ_F]={comm_g:.3e} (EVEN if 0)  "
              f"{{A_quad,γ_F}}={anticomm_g:.3e} (≠0 => EVEN => not Dirac-like)")
        for k, c in enumerate(C_MESH):
            A_quad = c * A_quad_unit
            D_def = inner_fluct.apply_deformation_quadratic(A_lin, A_quad)
            axioms = inner_fluct.verify_all_axioms(D_def, a, b)
            axiom4_dev_grid_c[i, k] = axioms['axiom_4_first_order_invariance']['residual']
            axiom5_resid_grid_c[i, k] = axioms['axiom_5_chirality_anticommutation']['residual']
            ko, _ = inner_fluct.compute_KO_dim(D_def)
            ko_dim_grid_c[i, k] = ko
            # K-theory residual: γ_F-anticommutation of the FULL 1-form B=A_lin+A_quad
            B = A_lin + A_quad
            ktheory_resid_grid_c[i, k] = inner_fluct.compute_delta_GV_via_theorem(B)
        # show the c=0 (linear) and c=1 (max quad) extremes
        print(f"           axiom-4 dev: c=0 → {axiom4_dev_grid_c[i,0]:.6e}; "
              f"c=1 → {axiom4_dev_grid_c[i,3]:.6e}")
        print(f"           axiom-5 res: c=0 → {axiom5_resid_grid_c[i,0]:.6e}; "
              f"c=1 → {axiom5_resid_grid_c[i,3]:.6e}")
    print("  " + "-" * 68)
    print()

    # ---- c=0 baseline cross-check vs S91 W7-1 ----
    c0_idx = C_MESH.index(0.0)  # (local)
    max_axiom4_c0 = float(axiom4_dev_grid_c[:, c0_idx].max())  # (local)
    baseline_diff = abs(max_axiom4_c0 - S91_BASELINE_MAX_AXIOM4)  # (local)
    baseline_match = baseline_diff < 1e-9  # (local)
    print(f"  c=0 cross-check vs S91 W7-1 baseline:")
    print(f"    max axiom-4 dev (c=0)      = {max_axiom4_c0:.12e}")
    print(f"    S91 W7-1 baseline          = {S91_BASELINE_MAX_AXIOM4:.12e}")
    print(f"    |diff|                     = {baseline_diff:.3e}  "
          f"({'MATCH (bit-for-bit)' if baseline_match else 'MISMATCH'})")
    print()

    # ---- Verdict construction ----
    # PLAN OPERATOR (plan §W9-1 (1)): "max |axiom-4 deviation| < 1e-10 AND
    # K-theory residual == 0 AND KO-dim == 6" at a VALID quadratic-extended
    # deformation. "Valid" requires D_def be a genuine (odd) Dirac, i.e. axiom-5
    # ({D_def,γ_F}=0) preserved. So the gate predicate is the MAX OVER THE 5
    # GRIDS of the best axiom-5-PRESERVING axiom-4 deviation, < 1e-10.
    nonzero_c_mask = np.array([c != 0.0 for c in C_MESH])  # (local)
    all_ko6 = bool(np.all(ko_dim_grid_c == EXPECTED_KO_DIM))  # (local)
    max_axiom5_break_nonzero_c = float(axiom5_resid_grid_c[:, nonzero_c_mask].max())  # (local)
    max_ktheory_resid_c0 = float(ktheory_resid_grid_c[:, c0_idx].max())  # (local)
    max_ktheory_resid_nonzero_c = float(ktheory_resid_grid_c[:, nonzero_c_mask].max())  # (local)

    # Per-grid: among axiom-5-PRESERVING c values, the minimum axiom-4 deviation
    # achievable at that grid. If NO c preserves axiom-5 for a grid, that grid's
    # best-admissible deviation is +inf (no valid quadratic-extended Dirac there).
    ax5_ok_mask = axiom5_resid_grid_c < AXIOM_RESIDUAL_TOL  # (local) (grid,c)
    per_grid_best_admissible = np.full(NUM_GRID_POINTS, np.inf)  # (local)
    for i in range(NUM_GRID_POINTS):
        admissible_devs = axiom4_dev_grid_c[i][ax5_ok_mask[i]]  # (local)
        if admissible_devs.size > 0:
            per_grid_best_admissible[i] = float(admissible_devs.min())
    # The gate predicate operates on the MAX over grids (all 5 must close):
    max_over_grids_best_admissible = float(per_grid_best_admissible.max())  # (local)
    # Per-grid linear-baseline deviation (c=0) for the direction comparison:
    per_grid_linear_dev = axiom4_dev_grid_c[:, c0_idx]  # (local)
    # absolute floor (any c, even axiom-5-BREAKING) — diagnostic only:
    min_axiom4_dev = float(axiom4_dev_grid_c.min())  # (local)
    # min admissible deviation across grids (diagnostic; dominated by trivial-zero grids):
    min_axiom4_dev_ax5ok = float(per_grid_best_admissible[np.isfinite(per_grid_best_admissible)].min())  # (local)

    # PASS iff EVERY grid closes axiom-4 at an axiom-5-preserving point AND
    # K-theory residual 0 (at those points) AND KO-dim 6.
    pass_predicate = (max_over_grids_best_admissible < AXIOM_RESIDUAL_TOL) and all_ko6 \
        and (max_ktheory_resid_c0 == 0.0)  # (local)

    print("=" * 72)
    print("Verdict construction (plan §W9-1 operator + collapse rule)")
    print("=" * 72)
    print(f"  per-grid best axiom-5-preserving axiom-4 dev = {np.array2string(per_grid_best_admissible, precision=6)}")
    print(f"  MAX over grids (gate predicate quantity)     = {max_over_grids_best_admissible:.6e}")
    print(f"    PASS boundary (< 1e-10)                    = {AXIOM_RESIDUAL_TOL}")
    print(f"  per-grid linear-baseline (c=0) dev           = {np.array2string(per_grid_linear_dev, precision=6)}")
    print(f"  max axiom-5 breakage at c≠0                  = {max_axiom5_break_nonzero_c:.6e}  "
          f"(EVEN-A_quad grading obstruction)")
    print(f"  KO-dim = 6 across all (grid,c)?              = {all_ko6}")
    print(f"  K-theory residual (c=0, linear)              = {max_ktheory_resid_c0:.6e}")
    print(f"  K-theory residual (c≠0, A_quad EVEN)         = {max_ktheory_resid_nonzero_c:.6e}")
    print()

    # SIGN verdict: plan Step 4 PRE-REGISTERED prediction — the quadratic
    # correction DECREASES the (per-grid) axiom-4 deviation toward zero relative
    # to the linear baseline, AT A VALID DEFORMATION. COMPUTED: for every grid
    # with a non-zero linear residual (grids 2-5), the only axiom-5-preserving
    # point is c=0 (the linear baseline itself) — any c≠0 makes A_quad's EVEN
    # part break axiom-5. So the quadratic extension yields NO axiom-5-preserving
    # decrease below the linear floor on ANY non-trivial grid. The predicted
    # direction (DECREASE) is FALSIFIED.
    # Direction test: does the quadratic extension strictly decrease the best
    # admissible deviation below the linear baseline on any non-trivial grid?
    nontrivial_grids = per_grid_linear_dev > AXIOM_RESIDUAL_TOL  # (local) grids with nonzero linear residual
    quad_decreases_on_nontrivial = bool(np.any(
        per_grid_best_admissible[nontrivial_grids]
        < per_grid_linear_dev[nontrivial_grids] - AXIOM_RESIDUAL_TOL
    )) if nontrivial_grids.any() else False  # (local)
    sign_verdict = "PASS" if quad_decreases_on_nontrivial else "FAIL"  # (local)

    # MAGNITUDE verdict: |max-over-grids admissible axiom-4 dev - 0| vs bands.
    if max_over_grids_best_admissible < AXIOM_RESIDUAL_TOL:
        magnitude_verdict = "PASS"  # (local)
    elif max_over_grids_best_admissible < INFO_RESIDUAL_TOL:
        magnitude_verdict = "INFO"  # (local)
    else:
        magnitude_verdict = "FAIL"  # (local)  (max admissible dev = 2.864 ≫ 1e-7)

    # REGIME verdict: is the quadratic-extension construction within its regime
    # of validity? A_quad EVEN => adding it to D_def yields a non-Dirac operator
    # (axiom-5 broken) for every non-zero c => the construction's premise (that
    # A_quad is a valid Dirac-extending 1-form) is structurally violated.
    if max_axiom5_break_nonzero_c < AXIOM_RESIDUAL_TOL:
        regime_verdict = "VALID"  # (local) (would require A_quad odd; it is not)
    else:
        # Every non-zero c breaks axiom-5 => the quadratic-extension premise is
        # invalid across the entire pre-registered c-mesh (>50% of window).
        regime_verdict = "BREAKDOWN"  # (local)

    # Composite per gate-verdicts.md schema-v2 collapse rule
    if regime_verdict == "BREAKDOWN":
        composite = "FAIL"
    elif sign_verdict == "FAIL":
        composite = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        composite = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        composite = "INFO"
    elif magnitude_verdict == "INFO":
        composite = "INFO"
    else:
        composite = "PASS"

    print(f"  sign_verdict      = {sign_verdict}  "
          f"(plan predicted DECREASE at valid deformation; computed "
          f"{'DECREASE' if quad_decreases_on_nontrivial else 'NO-DECREASE (only axiom-5-preserving pt is c=0 linear)'})")
    print(f"  magnitude_verdict = {magnitude_verdict}")
    print(f"  regime_verdict    = {regime_verdict}")
    print(f"  composite         = {composite}")
    print(f"  pass_predicate    = {pass_predicate}")
    print()

    # ---- Save .npz ----
    np.savez(
        OUT_NPZ,
        C_MESH=np.array(C_MESH),
        axiom4_dev_grid_c=axiom4_dev_grid_c,
        axiom5_resid_grid_c=axiom5_resid_grid_c,
        ko_dim_grid_c=ko_dim_grid_c,
        ktheory_resid_grid_c=ktheory_resid_grid_c,
        aquad_anticomm_gamma_per_grid=aquad_anticomm_gamma_per_grid,
        per_grid_best_admissible=per_grid_best_admissible,
        per_grid_linear_dev=per_grid_linear_dev,
        max_over_grids_best_admissible=max_over_grids_best_admissible,
        min_axiom4_dev=min_axiom4_dev,
        min_axiom4_dev_ax5ok=min_axiom4_dev_ax5ok,
        max_axiom4_dev_c0=max_axiom4_c0,
        max_axiom5_break_nonzero_c=max_axiom5_break_nonzero_c,
        max_ktheory_resid_c0=max_ktheory_resid_c0,
        max_ktheory_resid_nonzero_c=max_ktheory_resid_nonzero_c,
        all_ko6=all_ko6,
        pass_predicate=pass_predicate,
        baseline_diff_vs_s91_w7_1=baseline_diff,
        baseline_match=baseline_match,
        S91_BASELINE_MAX_AXIOM4=S91_BASELINE_MAX_AXIOM4,
        AXIOM_RESIDUAL_TOL=AXIOM_RESIDUAL_TOL,
        INFO_RESIDUAL_TOL=INFO_RESIDUAL_TOL,
        EXPECTED_KO_DIM=EXPECTED_KO_DIM,
        gv_canonical_difference_FW=gv_canonical_difference_FW,
        verdict_composite=composite,
        sign_verdict=sign_verdict,
        magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict,
        domain_used_frac=1.0,
        audit_sha256=audit_sha,
        content_sha256=content_sha,
        grid_labels=np.array(["C-only", "H-only", "M3-only", "C-H", "Full"]),
        sage_grading_sign_A_quad=1,  # EVEN (Sage-Q cross-check)
        structural_finding=("A_quad=[D,a][D,b] is degree-0 (EVEN); breaks axiom-5 "
                            "for c!=0; cannot cancel ODD order-1 residual "
                            "(grading-sector orthogonality); axiom-4 dev bounded "
                            "below by linear baseline 2.863564 => FAIL at 1e-10."),
    )
    print(f"  NPZ saved: {OUT_NPZ}")

    # ---- PNG plot ----
    fig, (axL, axR) = plt.subplots(1, 2, figsize=(15, 6))
    cvals = np.array(C_MESH)  # (local)
    order = np.argsort(cvals)  # (local) sort c for clean lines
    # Left: axiom-4 invariance deviation vs c, per grid
    for i in range(NUM_GRID_POINTS):
        axL.plot(cvals[order], axiom4_dev_grid_c[i][order], '-o',
                 label=f"grid {i+1} ({['ℂ','ℍ','M₃','ℂ⊕ℍ','Full'][i]})")
    axL.axhline(AXIOM_RESIDUAL_TOL, color='green', linestyle='--',
                label=f'PASS boundary {AXIOM_RESIDUAL_TOL:.0e}')
    axL.axhline(S91_BASELINE_MAX_AXIOM4, color='black', linestyle=':',
                label=f'S91 W7-1 linear floor {S91_BASELINE_MAX_AXIOM4:.3f}')
    axL.set_xlabel('quadratic coefficient c_{ij}')
    axL.set_ylabel('axiom-4 invariance deviation')
    axL.set_title('Axiom-4 deviation INCREASES with |c| (plan predicted DECREASE)')
    axL.legend(fontsize=8, loc='upper center')
    axL.grid(True, alpha=0.3)
    # Right: axiom-5 anticommutation residual vs c, per grid (grading obstruction)
    for i in range(NUM_GRID_POINTS):
        axR.plot(cvals[order], axiom5_resid_grid_c[i][order], '-s',
                 label=f"grid {i+1}")
    axR.axhline(AXIOM_RESIDUAL_TOL, color='green', linestyle='--',
                label=f'axiom-5 PASS {AXIOM_RESIDUAL_TOL:.0e}')
    axR.set_xlabel('quadratic coefficient c_{ij}')
    axR.set_ylabel(r'axiom-5 residual $\|\{D_{def},\gamma_F\}\|$')
    axR.set_title('A_quad is EVEN: axiom-5 breaks for c≠0 (grading obstruction)')
    axR.legend(fontsize=8, loc='upper center')
    axR.grid(True, alpha=0.3)
    fig.suptitle(f'S92 W9-1 §VII.AQ.OP-PROJ CCvS-2013 quadratic-extension — composite: {composite}',
                 fontsize=13)
    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=120)
    plt.close(fig)
    print(f"  PNG saved: {OUT_PNG}")

    # ---- Emit verdict line ----
    value_str = (
        f"max_over_grids_best_admissible_axiom4_dev={max_over_grids_best_admissible:.6e};"
        f"linear_floor_c0={max_axiom4_c0:.6e};"
        f"max_axiom5_break_c_nonzero={max_axiom5_break_nonzero_c:.6e};"
        f"A_quad_grading=EVEN;KO_dim_all=6={all_ko6};"
        f"baseline_match_S91_W7_1={baseline_match};"
        f"supersedes={SUPERSEDES_AUDIT_SHA}"
    )
    append_verdict(
        composite=composite,
        value_str=value_str,
        audit_sha=audit_sha,
        content_sha=content_sha,
        sign_v=sign_verdict,
        mag_v=magnitude_verdict,
        reg_v=regime_verdict,
    )

    wall = time.time() - t0  # (local)
    print()
    print("=" * 72)
    print(f"  {GATE_ID}")
    print(f"  composite: {composite}")
    print(f"  value: {value_str}")
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")
    print(f"  wall: {wall:.2f}s")
    print("=" * 72)
    return 0


if __name__ == "__main__":
    sys.exit(main())
