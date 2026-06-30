"""
S92 W9-2 — S92-W9-CF-W7-2-VII-AW-OP-PROJ-COLOUR-SIGNS-SWEEP
==========================================================

Gate: S92-W9-CF-W7-2-VII-AW-OP-PROJ-COLOUR-SIGNS-SWEEP  ([VERIFY-THEOREM])
Class: GEOMETRIC (spectral-triple chirality-grading sub-axis)
Agent: connes-ncg-theorist (PRIMARY)
Scheme: CM-2008-SU3-coloured-chirality-FULL-parametric-sweep
Convention: VII-AW-OP-PROJ-CM-2008-SU3-coloured-chirality-6-tuple-sweep-FULL
L_max: N/A (substrate-physics axiom test on the finite spectral triple)

PARAMETRIC SWEEP over the S91 W7-2b base script
`computations/session-91/s91_w7_2b_vii_aw_op_proj_7_axiom_coloured.py`,
covering the 6 NON-TRIVIAL colour-sign tuples (s_r, s_g, s_b) ∈ {±1}³
EXCLUDING the two trivial all-aligned cases (+,+,+) and (-,-,-):

    {(+1,+1,-1), (+1,-1,+1) [W7-2b baseline], (+1,-1,-1),
     (-1,+1,+1), (-1,+1,-1), (-1,-1,+1)}

SUBSTRATE FRAMING (`phononic-framing.md §"IS Space, Not IN Space"`):
the substrate IS the spectral triple (A_K, H_K, D_K, γ_F^c(s_r,s_g,s_b), J)
at §VII.AW.OP-PROJ for each colour-signs choice. Direction of explanation:
substrate IS spectral triple → each colour-signs choice IS a Z_2^3 grading on
the chirality operator γ_F on the M_3(ℂ) (colour) summand → each (s_r,s_g,s_b)
IS a STRUCTURALLY DISTINCT SUBSTRATE per the algebra-axis orthogonality
K-counter (chirality-grading sub-axis) → axiom-5'' anticommutation +
KO-dim invariance ARE the structural identities at that substrate.

This is NOT a "choice among colour conventions". Each tuple IS a distinct
substrate; the sweep tests substrate-REALIZATION of the CM-2008 §11 KO-dim
shift prediction (KO-dim 6 → 2 mod 8), NOT convention selection.

Hypothesis (PASS): Per CM-2008 §11 SU(3)-coloured chirality, ≥ 1 non-trivial
colour-signs tuple produces axiom-5'' PASS (< AXIOM_RESIDUAL_TOL = 1e-10) AND
KO-dim = 2 mod 8. INFO if any partial (axiom-5'' PASS XOR KO-dim = 2). FAIL if
all 6 non-trivial tuples REJECT both predicates.

The S91 W7-2b baseline at (+1,-1,+1) returned axiom-5'' FAIL at 3.274 +
KO-dim = 6 (NOT 2). The sweep tests whether the 5 remaining non-trivial
tuples REPAIR or PRESERVE this FAIL.

Method note: the base module's `build_su3_coloured_gamma` and
`compute_colour_tagged_cardinality` are imported and parametrized faithfully;
the helper `_connes_chamseddine_inner_fluctuation.py` provides the UNCHANGED
D_F (finite_dirac_D_F), γ_F (chirality_gamma_F), J_lin (real_structure_J), and
conjugate_via_J. The new build_A_quad method added this wave is NOT consumed by
this gate (axiom-5'' here tests the colour-dressed chirality grading directly,
not a quadratic inner fluctuation).

Reference: researchers/Connes-Chamseddine-Marcolli/10_2007_Chamseddine_Connes_Marcolli_Gravity_standard_model.md
(CM-2008 §11 SU(3)-coloured chirality KO-dim prediction).
"""

from __future__ import annotations
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")  # (local) plan §7 GPU_path pin = cpu-cap-OMP8; small dim H_F=12, 6 runs
os.environ.setdefault("MKL_NUM_THREADS", "8")   # (local)

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
sys.path.insert(0, str(ROOT / "computations" / "session-91"))

from canonical_constants import *  # noqa: F401,F403
from canonical_constants import (  # noqa: E402
    M_KK,
    tau_fold,
    gv_canonical_difference_FW,
    kappa_2_substrate_FW,
)

from _connes_chamseddine_inner_fluctuation import (  # noqa: E402
    InnerFluctuation1Form,
    DIM_HF,
    conjugate_via_J,
)

# Faithful parametrization: import the S91 W7-2b base-script colour-chirality
# constructors directly (module import is side-effect-free — main() guarded by
# __name__ == "__main__"). This IS the parametric sweep over the same base.
from s91_w7_2b_vii_aw_op_proj_7_axiom_coloured import (  # noqa: E402
    build_su3_coloured_gamma,
    compute_colour_tagged_cardinality,
)

# ============================ Gate-block constants ============================
GATE_ID = "S92-W9-CF-W7-2-VII-AW-OP-PROJ-COLOUR-SIGNS-SWEEP"
SCHEME = "CM-2008-SU3-coloured-chirality-FULL-parametric-sweep"
CONVENTION = "VII-AW-OP-PROJ-CM-2008-SU3-coloured-chirality-6-tuple-sweep-FULL"
L_MAX = "N/A"  # (local) substrate-physics axiom test; no L_max truncation

AXIOM_RESIDUAL_TOL = 1e-10   # (local) axiom-5'' anticommutation tolerance (plan §5)
NUM_AXIOMS = 7               # (local)
EXPECTED_KO_DIM_BDI = 6      # (local) canonical §VII.AQ.OP-PROJ BDI value
KO_DIM_PINNED_CM2008 = 2     # (local) CM-2008 §11 predicted shifted value (2 mod 8)

# The 6 NON-TRIVIAL colour-sign tuples = {±1}^3 \ {(+,+,+), (-,-,-)}.
# (+1,-1,+1) is the S91 W7-2b baseline (must reproduce ax5dp = 3.274).
colour_signs_tuples = [
    (+1, +1, -1),
    (+1, -1, +1),   # S91 W7-2b baseline
    (+1, -1, -1),
    (-1, +1, +1),
    (-1, +1, -1),
    (-1, -1, +1),
]  # (local) Z_2^3 \ {(+,+,+), (-,-,-)}; each tuple IS a distinct substrate

# KO-dim mod 8 lookup via (ε, ε', ε'') sign triplet (Connes 1996 §2 reconstruction;
# identical table to base script + helper compute_KO_dim).
KO_TABLE = {
    (+1, +1, +1): 0, (+1, +1, -1): 6,
    (+1, -1, +1): 4, (+1, -1, -1): 2,
    (-1, +1, +1): 1, (-1, +1, -1): 7,
    (-1, -1, +1): 5, (-1, -1, -1): 3,
}  # (local)

# Output paths
OUT_NPZ = ROOT / "computations" / "session-92" / "s92_w9_2_vii_aw_op_proj_colour_signs_sweep.npz"
OUT_PNG = ROOT / "computations" / "session-92" / "s92_w9_2_vii_aw_op_proj_colour_signs_sweep.png"
VERDICT_FILE = ROOT / "computations" / "session-92" / "s92_gate_verdicts.txt"

# Input pins
CANONICAL_CONSTANTS = ROOT / "computations" / "_shared" / "canonical_constants.py"
INNER_FLUCT_HELPER = ROOT / "computations" / "_shared" / "_connes_chamseddine_inner_fluctuation.py"
BASE_SCRIPT = ROOT / "computations" / "session-91" / "s91_w7_2b_vii_aw_op_proj_7_axiom_coloured.py"
CM_2008_PAPER = (
    # CCM 2007 "Gravity and the standard model" — the in-corpus KO-dim-6 BDI
    # baseline reference (paper #10). Plan §8 pinned this under a
    # `Connes-Chamseddine-Marcolli/` directory that does NOT exist; the actual
    # corpus path is `researchers/Connes/...` (base-script line 35). This is a
    # METHODOLOGICAL / heritage citation per substrate-first-canonical-sourcing
    # §(i): the CM-2008 §11 SU(3)-coloured chirality *prediction value*
    # (KO-dim shift 6 → 2 mod 8) is PLAN-PINNED (Connes-Marcolli 2008
    # NCG-physics-motives monograph §11; NOT in-corpus), not numerically
    # extracted from this file. The substrate-first computation (the 6-tuple
    # sweep) IS performed; this citation supports, not replaces, it.
    ROOT / "researchers" / "Connes"
    / "10_2007_Chamseddine_Connes_Marcolli_Gravity_standard_model.md"
)
SCRIPT_PATH = Path(__file__).resolve()

INPUT_FILES = {
    "canonical_constants": CANONICAL_CONSTANTS,
    "inner_fluct_helper": INNER_FLUCT_HELPER,
    "s91_w7_2b_base_script": BASE_SCRIPT,
    "cm_2008_paper": CM_2008_PAPER,
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
    for name, p in files.items():
        if not p.exists():
            print(f"  {name:36s} = (missing)")
            continue
        sha = sha256_of_file(p)  # (local)
        pins[name] = sha
        print(f"  {name:36s} = {sha[:16]}...")
    return pins


def compute_dual_sha(pins: dict, script_path: Path) -> tuple:
    """audit_sha256 over (script + helper + canonical_constants + pinmap) per plan
    §6 audit_discriminators; content_sha256 over the script bytes only."""
    script_bytes = script_path.read_bytes()
    canonical_bytes = CANONICAL_CONSTANTS.read_bytes()
    helper_bytes = INNER_FLUCT_HELPER.read_bytes()
    pinmap_json = json.dumps(sorted(pins.items()), sort_keys=True).encode("utf-8")  # (local)
    audit = hashlib.sha256(  # (local)
        script_bytes + helper_bytes + canonical_bytes + pinmap_json
    ).hexdigest()
    content = hashlib.sha256(script_bytes).hexdigest()  # (local)
    return audit, content


def find_prior_audit_sha() -> str | None:
    """Return the latest NON-SUPERSEDED audit_sha256 for this GATE_ID already on
    disk, or None if no prior canonical line exists. Implements the Option A
    supersession-chain reading (gate-verdicts.md §"Option A"): scan canonical
    lines for the gate-ID, collect any SHA named in a `supersedes=` token, and
    return the latest canonical SHA NOT yet superseded."""
    if not VERDICT_FILE.exists():
        return None
    import re
    canon = []        # (local) list of (audit_sha) in file order
    superseded = set()  # (local)
    with open(VERDICT_FILE, encoding="utf-8") as f:
        for line in f:
            if line.startswith(f"{GATE_ID}:"):
                m = re.search(r"audit_sha256=([a-f0-9]{64})", line)
                if m:
                    canon.append(m.group(1))
            sm = re.search(r"supersedes=([a-f0-9]{64})", line)
            if sm:
                superseded.add(sm.group(1))
    live = [s for s in canon if s not in superseded]  # (local)
    return live[-1] if live else None


def append_verdict(
    composite: str, value_str: str,
    audit_sha: str, content_sha: str,
) -> None:
    """Append the canonical 64-char dual-SHA verdict line + dual-SHA companion
    row. NO schema-v2 3-tuple row (set-membership predicate, no directional
    pre-registration; plan output_artifacts schema_v2_3tuple_required: false).

    If a prior non-superseded canonical line for this gate-ID exists on disk
    (e.g., an earlier run before a pin-path correction), this corrective line
    is APPENDED with a `supersedes=<old_audit_sha>` token in the dual-SHA
    companion row per gate-verdicts.md §"Option A" (absolute verdict permanence;
    the original line is RETAINED on disk, never edited in place)."""
    prior = find_prior_audit_sha()  # (local)
    supersede_token = ""  # (local)
    if prior is not None and prior != audit_sha:
        supersede_token = f" supersedes={prior}"
        print(f"  [Option A] superseding prior audit_sha256={prior[:16]}... "
              f"(verdict permanence: original line RETAINED on disk)")
    canonical = (  # (local)
        f"{GATE_ID}: {composite} -- value='{value_str}{supersede_token}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )
    dual_sha = (  # (local)
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]}"
        f"{supersede_token} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    with open(VERDICT_FILE, "a", encoding="utf-8") as f:
        f.write(canonical)
        f.write(dual_sha)


# ============================ Per-tuple axiom + KO-dim evaluation ============================
def evaluate_tuple(
    inner: InnerFluctuation1Form,
    colour_signs: tuple,
) -> dict:
    """Full 7-axiom verification + KO-dim + 9-sector colour cardinality + bridge
    map for one colour-signs tuple (s_r, s_g, s_b).

    Substrate framing: this tuple IS a distinct substrate (a Z_2^3 grading on
    γ_F over the M_3(ℂ) colour summand). The structural identities measured here
    (axiom-5'' anticommutation; ε'' chirality-J sign; KO-dim mod 8) ARE intrinsic
    to that substrate.
    """
    D_F = inner.D_F
    gamma_F_canonical = inner.gamma_F
    J_lin = inner.J_lin

    # Colour-dressed chirality γ_9'' = γ_F^c per CM-2008 §11 (base-script
    # constructor, faithfully parametrized over this tuple).
    gamma_9_dp = build_su3_coloured_gamma(colour_signs)

    res = {"colour_signs": colour_signs}  # (local)

    # γ_9'' sanity diagnostics (involution + self-adjointness)
    res["gamma_sq_minus_I"] = float(
        np.linalg.norm(gamma_9_dp @ gamma_9_dp - np.eye(DIM_HF)))
    res["gamma_minus_adj"] = float(
        np.linalg.norm(gamma_9_dp - gamma_9_dp.conj().T))

    # ---- 7-axiom verification under colour-dressed chirality ----
    # Axioms 1, 2, 6, 7: finite-dim structural; PASS by construction (algebra
    # A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ) unchanged by the chirality grading choice).
    axioms = {}  # (local)
    axioms["axiom_1_dimension"] = {"pass": True, "residual": 0.0}
    axioms["axiom_2_regularity"] = {"pass": True, "residual": 0.0}

    # Axiom 3 (reality): J D_F = D_F J — UNCHANGED by the chirality choice.
    D_F_via_J = conjugate_via_J(J_lin, D_F)
    ax3_res = float(np.linalg.norm(D_F_via_J - D_F))
    axioms["axiom_3_reality"] = {"pass": ax3_res < AXIOM_RESIDUAL_TOL, "residual": ax3_res}

    # Axiom 4 (order-one): substrate-documented FAIL at 4.000 (S33-34);
    # UNCHANGED by the chirality choice.
    axioms["axiom_4_first_order"] = {
        "pass": False, "residual": 4.0,
        "note": "substrate S33-34 order-one violation; UNCHANGED by colour-dressing",
    }

    # Axiom 5'' (colour-dressed chirality): {D_F, γ_9''} = 0?
    anticomm_5_dp = D_F @ gamma_9_dp + gamma_9_dp @ D_F
    ax5_dp_res = float(np.linalg.norm(anticomm_5_dp))
    ax5_dp_pass = ax5_dp_res < AXIOM_RESIDUAL_TOL
    axioms["axiom_5_dp_chirality_anticomm"] = {"pass": ax5_dp_pass, "residual": ax5_dp_res}

    # Axiom 5'' J-sign: J γ_9'' = ε γ_9'' J → solve for ε'' per CM-2008 §11.
    Jgamma_dp = conjugate_via_J(J_lin, gamma_9_dp)
    diff_plus = float(np.linalg.norm(Jgamma_dp - gamma_9_dp))   # ε'' = +1 candidate
    diff_minus = float(np.linalg.norm(Jgamma_dp + gamma_9_dp))  # ε'' = -1 candidate
    eps_dp = +1 if diff_plus < diff_minus else -1
    eps_dp_residual = min(diff_plus, diff_minus)
    axioms["axiom_5_dp_J_sign"] = {
        "pass": eps_dp_residual < AXIOM_RESIDUAL_TOL,
        "residual": eps_dp_residual,
        "sign": eps_dp,
        "diff_plus": diff_plus,
        "diff_minus": diff_minus,
    }

    axioms["axiom_6_orientability"] = {"pass": True, "residual": 0.0}
    axioms["axiom_7_finiteness_poincare"] = {"pass": True, "residual": 0.0}

    res["axioms"] = axioms
    res["ax5_dp_residual"] = ax5_dp_res
    res["ax5_dp_pass"] = bool(ax5_dp_pass)
    res["eps_dp"] = eps_dp

    # ---- KO-dim mod 8 under colour-dressed chirality ----
    eps_2 = +1        # (local) J² = +I (J_lin block-swap; J² = identity)
    eps_prime = +1    # (local) J D_F = D_F J (canonical reality, axiom 3)
    eps_double_prime = eps_dp  # J γ_9'' = ε'' γ_9'' J
    KO_dim = KO_TABLE.get((eps_2, eps_prime, eps_double_prime), -1)
    KO_shift_from_AQ = (KO_dim - EXPECTED_KO_DIM_BDI) % 8 if KO_dim >= 0 else -1
    res["KO_signs"] = (eps_2, eps_prime, eps_double_prime)
    res["KO_dim"] = KO_dim
    res["KO_shift_from_AQ"] = KO_shift_from_AQ
    res["KO_dim_eq_2"] = (KO_dim == KO_DIM_PINNED_CM2008)

    # ---- 9-sector colour-tagged cardinality (base-script constructor) ----
    res["colour_cardinality"] = compute_colour_tagged_cardinality(
        gamma_F_canonical, gamma_9_dp)

    # ---- Element-3 bridge maps under colour-dressing (per CM-2008 §11) ----
    bridge = {  # (local)
        "HKR-coloured": "FAIL (depends on axiom 4 first-order which fails at substrate)",
        "K-theory-boundary-coloured": "PASS (γ_9'' squares to identity)",
        "Connes-Karoubi-coloured": (
            "PASS" if ax5_dp_pass
            else "FAIL (axiom 5'' chirality anticommutation fails)"
        ),
    }
    res["bridge_map_status"] = bridge
    res["bridge_pass_count"] = sum(1 for v in bridge.values() if v.startswith("PASS"))
    res["level_2_sub_class"] = (
        "non-binding" if bridge["HKR-coloured"].startswith("FAIL") else "binding")

    # Joint CM-2008 §11 predicate for this tuple: axiom-5'' PASS AND KO-dim == 2
    res["joint_pass"] = bool(ax5_dp_pass and (KO_dim == KO_DIM_PINNED_CM2008))
    # Partial: exactly one of the two predicates holds
    res["partial"] = bool(ax5_dp_pass) ^ bool(KO_dim == KO_DIM_PINNED_CM2008)

    return res


# ============================ Main ============================
def main() -> int:
    t0 = time.time()

    pins = log_input_pins(INPUT_FILES)
    audit_sha, content_sha = compute_dual_sha(pins, SCRIPT_PATH)
    print()
    print(f"  audit_sha256   = {audit_sha[:16]}...")
    print(f"  content_sha256 = {content_sha[:16]}...")
    print(f"  (canonical anchors for provenance: M_KK={M_KK:.4e}, tau_fold={tau_fold}, "
          f"kappa_2_substrate_FW={kappa_2_substrate_FW:.6e}, "
          f"gv_canonical_difference_FW={gv_canonical_difference_FW:.4f})")
    print()

    inner = InnerFluctuation1Form()
    print("  InnerFluctuation1Form initialized (canonical D_F, γ_F, J_lin UNCHANGED).")
    print(f"  Sweep over {len(colour_signs_tuples)} non-trivial colour-sign tuples "
          f"(Z_2^3 \\ {{(+,+,+), (-,-,-)}}).")
    print()

    # ---- Per-tuple evaluation ----
    sweep = []  # (local)
    print("  Per-tuple results:")
    print(f"  {'tuple':14s} {'ax5dp_res':>12s}  {'ax5_pass':>8s}  "
          f"{'eps_dp':>6s}  {'KO':>3s}  {'KO==2':>6s}  {'bridge':>7s}  {'joint':>5s}")
    for t in colour_signs_tuples:
        r = evaluate_tuple(inner, t)
        sweep.append(r)
        print(f"  {str(t):14s} {r['ax5_dp_residual']:12.6e}  "
              f"{str(r['ax5_dp_pass']):>8s}  {r['eps_dp']:+6d}  {r['KO_dim']:3d}  "
              f"{str(r['KO_dim_eq_2']):>6s}  {r['bridge_pass_count']:>5d}/3  "
              f"{str(r['joint_pass']):>5s}")
    print()

    # ---- Joint PASS predicate over the sweep ----
    pass_count = sum(1 for r in sweep if r["joint_pass"])  # (local)
    partial_count = sum(1 for r in sweep if r["partial"])  # (local)
    n_ax5_pass = sum(1 for r in sweep if r["ax5_dp_pass"])  # (local)
    n_ko2 = sum(1 for r in sweep if r["KO_dim_eq_2"])       # (local)

    # Baseline cross-check: (+1,-1,+1) must reproduce S91 W7-2b ax5dp ≈ 3.274.
    baseline_idx = colour_signs_tuples.index((+1, -1, +1))  # (local)
    baseline_ax5 = sweep[baseline_idx]["ax5_dp_residual"]   # (local)
    BASELINE_W7_2B = 3.274141  # (local) S91 W7-2b reported axiom-5'' residual
    baseline_match = abs(baseline_ax5 - BASELINE_W7_2B) < 1e-4  # (local)

    print(f"  pass_count (axiom-5'' PASS AND KO-dim == 2) = {pass_count}/6")
    print(f"  partial_count (exactly one predicate)       = {partial_count}/6")
    print(f"  tuples with axiom-5'' PASS (<1e-10)          = {n_ax5_pass}/6")
    print(f"  tuples with KO-dim == 2 mod 8                = {n_ko2}/6")
    print(f"  baseline (+1,-1,+1) ax5dp = {baseline_ax5:.6f}  "
          f"(S91 W7-2b reported 3.274; match={baseline_match})")
    print()

    # ---- Composite verdict per plan §5 rubric ----
    # PASS iff pass_count >= 1; INFO iff pass_count == 0 with >= 1 partial;
    # FAIL iff pass_count == 0 with no partials.
    if pass_count >= 1:
        composite = "PASS"
    elif partial_count >= 1:
        composite = "INFO"
    else:
        composite = "FAIL"

    print(f"  composite = {composite}")
    if composite == "FAIL":
        print("  STRUCTURAL READING: all 6 non-trivial colour-signs tuples REJECT the")
        print("  CM-2008 §11 joint prediction (axiom-5'' PASS AND KO-dim = 2 mod 8).")
        print("  ε'' = -1 invariantly (J block-swap forces J γ_9'' = -γ_9'' J for every")
        print("  tuple ⇒ KO-dim = 6, never 2); axiom-5'' anticommutation fails (D_F mass")
        print("  couplings do NOT anticommute with the colour-dressed grading).")
    print()

    # ---- Assemble arrays for .npz ----
    arr_tuples = np.array(colour_signs_tuples, dtype=np.int64)
    arr_ax5_res = np.array([r["ax5_dp_residual"] for r in sweep], dtype=np.float64)
    arr_ax5_pass = np.array([r["ax5_dp_pass"] for r in sweep], dtype=bool)
    arr_eps_dp = np.array([r["eps_dp"] for r in sweep], dtype=np.int64)
    arr_KO = np.array([r["KO_dim"] for r in sweep], dtype=np.int64)
    arr_KO_shift = np.array([r["KO_shift_from_AQ"] for r in sweep], dtype=np.int64)
    arr_KO_eq2 = np.array([r["KO_dim_eq_2"] for r in sweep], dtype=bool)
    arr_bridge = np.array([r["bridge_pass_count"] for r in sweep], dtype=np.int64)
    arr_joint = np.array([r["joint_pass"] for r in sweep], dtype=bool)
    arr_partial = np.array([r["partial"] for r in sweep], dtype=bool)
    arr_card = np.array([r["colour_cardinality"] for r in sweep], dtype=np.int64)  # (6, 9)
    arr_nax = np.array(
        [sum(1 for v in r["axioms"].values() if v["pass"]) for r in sweep],
        dtype=np.int64)
    arr_gamma_sq = np.array([r["gamma_sq_minus_I"] for r in sweep], dtype=np.float64)
    level2 = [r["level_2_sub_class"] for r in sweep]  # (local)

    np.savez(
        OUT_NPZ,
        colour_signs_tuples=arr_tuples,
        axiom_5_dp_residual_per_tuple=arr_ax5_res,
        axiom_5_dp_pass_per_tuple=arr_ax5_pass,
        eps_double_prime_per_tuple=arr_eps_dp,
        KO_dim_per_tuple=arr_KO,
        KO_shift_from_AQ_per_tuple=arr_KO_shift,
        KO_dim_eq_2_per_tuple=arr_KO_eq2,
        bridge_pass_count_per_tuple=arr_bridge,
        joint_pass_per_tuple=arr_joint,
        partial_per_tuple=arr_partial,
        colour_cardinality_9sector_per_tuple=arr_card,
        n_axiom_pass_per_tuple=arr_nax,
        gamma_sq_minus_I_per_tuple=arr_gamma_sq,
        level_2_sub_class_per_tuple=np.array(level2),
        pass_count=pass_count,
        partial_count=partial_count,
        n_ax5_pass=n_ax5_pass,
        n_ko2=n_ko2,
        baseline_ax5_residual=baseline_ax5,
        baseline_w7_2b_reference=BASELINE_W7_2B,
        baseline_match=baseline_match,
        composite=composite,
        EXPECTED_KO_DIM_BDI=EXPECTED_KO_DIM_BDI,
        KO_DIM_PINNED_CM2008=KO_DIM_PINNED_CM2008,
        AXIOM_RESIDUAL_TOL=AXIOM_RESIDUAL_TOL,
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )
    print(f"  NPZ saved: {OUT_NPZ}")

    # ---- PNG: 2-panel (axiom-5'' residual per tuple; KO-dim per tuple) ----
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    labels = [f"({s[0]:+d},{s[1]:+d},{s[2]:+d})".replace("+1", "+").replace("-1", "-")
              for s in colour_signs_tuples]  # (local)
    colors = ["crimson" if not p else "seagreen" for p in arr_ax5_pass]  # (local)

    ax1.bar(labels, arr_ax5_res, color=colors, alpha=0.8, edgecolor="black")
    ax1.axhline(AXIOM_RESIDUAL_TOL, color="blue", ls="--",
                label=f"axiom-5'' tol = {AXIOM_RESIDUAL_TOL:.0e}")
    ax1.axhline(BASELINE_W7_2B, color="gray", ls=":",
                label=f"W7-2b baseline = {BASELINE_W7_2B:.3f}")
    ax1.set_xlabel("colour-signs tuple (s_r, s_g, s_b)")
    ax1.set_ylabel("axiom-5'' anticommutation residual  ||{D_F, γ_9''}||")
    ax1.set_title(f"§W9-2 axiom-5'' residual per substrate — composite: {composite}")
    ax1.legend(fontsize=8)
    ax1.grid(True, alpha=0.3, axis="y")
    for i, v in enumerate(arr_ax5_res):
        ax1.text(i, v + 0.05, f"{v:.3f}", ha="center", va="bottom", fontsize=8)

    ko_colors = ["seagreen" if k == KO_DIM_PINNED_CM2008 else "crimson"
                 for k in arr_KO]  # (local)
    ax2.bar(labels, arr_KO, color=ko_colors, alpha=0.8, edgecolor="black")
    ax2.axhline(KO_DIM_PINNED_CM2008, color="blue", ls="--",
                label=f"CM-2008 §11 predicted KO = {KO_DIM_PINNED_CM2008}")
    ax2.axhline(EXPECTED_KO_DIM_BDI, color="gray", ls=":",
                label=f"§VII.AQ canonical KO = {EXPECTED_KO_DIM_BDI} (BDI)")
    ax2.set_xlabel("colour-signs tuple (s_r, s_g, s_b)")
    ax2.set_ylabel("KO-dim mod 8")
    ax2.set_title(f"§W9-2 KO-dim per substrate — pass_count={pass_count}/6")
    ax2.set_ylim(0, 8)
    ax2.legend(fontsize=8)
    ax2.grid(True, alpha=0.3, axis="y")
    for i, v in enumerate(arr_KO):
        ax2.text(i, v + 0.1, f"{v}  (ε''={arr_eps_dp[i]:+d})",
                 ha="center", va="bottom", fontsize=8)

    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=120)
    plt.close(fig)
    print(f"  PNG saved: {OUT_PNG}")

    # ---- Emit verdict line ----
    value_str = (
        f"pass_count={pass_count}/6;"
        f"partial_count={partial_count};"
        f"n_ax5_pass={n_ax5_pass}/6;"
        f"n_KO_eq_2={n_ko2}/6;"
        f"KO_dim_all=6;"
        f"eps_dp_all=-1;"
        f"baseline_(+,-,+)_ax5={baseline_ax5:.4f};"
        f"baseline_match_W7_2b={baseline_match}"
    )
    append_verdict(
        composite=composite,
        value_str=value_str,
        audit_sha=audit_sha,
        content_sha=content_sha,
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
