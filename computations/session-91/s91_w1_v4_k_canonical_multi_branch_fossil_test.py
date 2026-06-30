#!/usr/bin/env python3
"""
S91 W1-1 - CF-S91-V4-K_CANONICAL-MULTI-BRANCH-FOSSIL-TEST  (T1.3; routing oracle)
=================================================================================

Gate: CF-S91-V4-K_CANONICAL-MULTI-BRANCH-FOSSIL-TEST  ([VERIFY-THEOREM])

PLAN-VS-CANONICAL CORRECTION (user directive 2026-05-16)
--------------------------------------------------------
Plan sessions/session-plan/session-91-plan-w1.md section W1-1 Field 6 wrote
the substitution chain with the operator:

    L_FULL = d ln(Tr_{M_2(C)}(P_BdG * D_K^{-2s})) / d ln(K_window) |_{s=4}

But the CANONICAL substrate-IS observable for section VII.AV (per
S87 W2-3 + S89 W5-2 + S90 W8-3 CF-61 + W5b-47 closure) is:

    L_emp(K) := d^2 ln P_GGE / d(ln K)^2  |_{K_horizon}
    P_GGE(K) := Var_a(|v_a(K)|^2)  over the 8 canonical s52 Bogoliubov modes

Per the user directive 2026-05-16 ("If the plan used the wrong maths, then
use the right maths"), this script implements the canonical second log-
derivative of Bogoliubov variance, NOT the plan's first log-derivative of
an M_2 trace. The plan's literal formula is operator-mismatched against
the canonical L_emp = -7.046336474406761 anchor (different derivative
order; different observable family); implementing it literally would
produce a structurally-trivial FAIL with no physics content.

The V4 fossil test's substrate-physics question is preserved: under a
multi-branch s52 B-tensor configuration sweep at L_max=12, does the
canonical L_emp anchor exist in a BASIN of B-configurations, or only at
the identity-B canonical s52 anchor (isolated solution)?

PASS/FAIL/INFO threshold reconciliation
----------------------------------------
Plan Field 9 wrote:
    PASS iff n_aligned >= 1     ->  Reading B WIN  ->  T1.2 priority
    FAIL iff n_aligned == 0     ->  Reading A WIN  ->  T1.1 priority
    INFO iff n_aligned in [1,4] ->  REGIME-MARGINAL

The plan's PASS [>=1] and INFO [1,4] overlap (both fire at n=1..4). With
the canonical observable, identity-B (theta=0, b_1=b_2=1) is in the scan
and reproduces L_emp at numerical-noise level, so n_aligned >= 1 is
essentially guaranteed at the canonical operator (tautological PASS).
The substrate-physics-meaningful adjudication discriminates BASIN vs
ISOLATED:

    PASS iff n_aligned >= 5   ->  Reading B WIN   ->  T1.2 priority
                                (B-tensor BASIN reproduces L_emp)
    INFO iff n_aligned in [1,4] ->  REGIME-MARGINAL
                                (identity-B and near-neighbors only)
    FAIL iff n_aligned == 0   ->  Reading A WIN   ->  T1.1 priority
                                (even identity-B fails to align;
                                substrate-IS structural anomaly)

This resolves the plan's PASS/INFO overlap into a physically meaningful
trichotomy.

V4 MULTI-BRANCH B-TENSOR PARAMETERIZATION
-----------------------------------------
Plan Field 6 Step 3 specified:
    B = R(theta_1, theta_2, theta_3) * diag(b_1, b_2) * R(theta_1,...)^T
    scan: theta_k in {0, 2pi/8, ..., 14pi/8} x b_k in {0.5, 0.6, ..., 1.5}
    total = 8^3 * 11 * 11 = 61,952 configs; subsample uniform-random to
    N=16,384 (random_seed=20260516)

The B-tensor acts on the (Delta_B2, Delta_B3) per-branch gap-amplitude
sub-block of the canonical s52 8-mode structure. The branch B1 is
ungapped (Delta=0) and remains structurally fixed.

Concrete implementation (canonical interpretation):
    Delta_B1_perturbed = 0                                  [unchanged]
    Delta_B2_perturbed = b_1 * Delta_B2_canonical * e^{i*theta_1}
    Delta_B3_perturbed = b_2 * Delta_B3_canonical * e^{i*theta_2}
    theta_3 is the global phase (no effect on |v_a|^2 by gauge invariance;
              retained for plan-parameterization faithfulness)

At identity-B (theta=0, b=1), Delta_perturbed = Delta_canonical -> L_emp
reproduces -7.046336 to numerical-noise level by construction.

SCAN GRID
---------
theta_k in {0, 2pi/8, 4pi/8, ..., 14pi/8}  (8 angles each)
b_k in {0.5, 0.6, ..., 1.5}                (11 magnitudes each)
Total configs: 8 * 8 * 8 * 11 * 11 = 61,952
Random subsample: 16,384 (random_seed=20260516)

K-WINDOW (per S87 W2-3 / S89 W5-2 canonical pin)
-------------------------------------------------
K-grid uniform-in-ln-K over [0.95, 1.05] * K_horizon
DLNK = 0.001  ->  ~101 K-window points
5-point central finite difference of ln P_GGE at K=K_horizon

INPUT FILES
-----------
- canonical_constants.py
- s52_bogoliubov_amp.npz (canonical 8-mode Bogoliubov structure at L_max=12)
- s84_spectrum_cache_L12_tau019.npz (referenced for context only;
                                     L_emp anchor lives in section VII.AV
                                     registry; computation does not directly
                                     read this cache)
- script bytes

OUTPUT (plan Field 6 line 206-210)
-----------------------------------
- computations/session-91/s91_w1_v4_k_canonical_multi_branch_fossil_test.npz
- computations/session-91/s91_w1_v4_k_canonical_multi_branch_fossil_test.png
- computations/session-91/s91_gate_verdicts.txt  (canonical line + dual-SHA
                                                 + S87+ schema-v2 3-tuple)
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import math
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "computations" / "_shared"))

from canonical_constants import *  # noqa: F401,F403
from canonical_constants import (  # noqa: E402
    M_KK,
    tau_fold,
    Delta_BCS,
)

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# ============================ Gate-block constants ============================
GATE_ID = "CF-S91-V4-K_CANONICAL-MULTI-BRANCH-FOSSIL-TEST"
SCHEME = "substrate-IS-multi-branch-B-tensor-canonical-S87-W2-3-second-log-derivative"
CONVENTION = (
    "V4-Re-V3-Option-gamma-dispatch-routing-Cell-IV-substrate-distance-2-pole-s4-"
    "PLAN-OPERATOR-CORRECTED-PER-USER-2026-05-16"
)
L_MAX = 12  # (local) plan W1-1 Field 7 canonical anchor

# Scan-grid pins (plan Field 7)
SUBSAMPLE_N = 16384         # (local) Re:V3 Option gamma pre-reg target
SEED = 20260516             # (local) reproducibility pin
N_THETA = 8                 # (local) theta grid: 8 angles in [0, 2pi)
N_B = 11                    # (local) b grid: 11 magnitudes in [0.5, 1.5]
B_MIN = 0.5                 # (local)
B_MAX = 1.5                 # (local)

# K-window pins (per S87 W2-3 / S89 W5-2 canonical)
K_HORIZON_FRAC = (0.95, 1.05)  # (local) 5% window around horizon crossing
DLNK = 0.001                    # (local) step in ln K
N_K = int(round((math.log(K_HORIZON_FRAC[1]) - math.log(K_HORIZON_FRAC[0])) / DLNK)) + 1  # (local)

# Discriminator thresholds (plan Field 9, with PASS/INFO overlap resolution)
L_EMP_CANONICAL = -7.046336474406761  # (local) substrate-natural anchor; section VII.AV registry line 18092
REL_TOL = 1e-3                         # (local) pre-registered tolerance per plan Field 7
PASS_THRESHOLD_N_ALIGNED = 5           # (local) PASS-vs-INFO boundary (BASIN-vs-near-identity)
INFO_BAND_UPPER = 4                    # (local) INFO upper bound (marginal alignment count)

# Output paths
OUT_NPZ = ROOT / "computations" / "session-91" / "s91_w1_v4_k_canonical_multi_branch_fossil_test.npz"
OUT_PNG = ROOT / "computations" / "session-91" / "s91_w1_v4_k_canonical_multi_branch_fossil_test.png"
VERDICT_FILE = ROOT / "computations" / "session-91" / "s91_gate_verdicts.txt"

# Input file paths
CANONICAL_CONSTANTS = ROOT / "computations" / "_shared" / "canonical_constants.py"
S52_BOG_CACHE = ROOT / "computations" / "session-52" / "s52_bogoliubov_amp.npz"
L12_CACHE = ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
SCRIPT_PATH = Path(__file__).resolve()

INPUT_FILES = {
    "canonical_constants": CANONICAL_CONSTANTS,
    "s52_bogoliubov_amp": S52_BOG_CACHE,
    "L12_spectrum_cache_tau019": L12_CACHE,
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


def compute_dual_sha(pins: dict, script_path: Path) -> tuple[str, str]:
    """Audit SHA = SHA(script + canonical_constants + pinmap-JSON);
    Content SHA = SHA(script).
    """
    script_bytes = script_path.read_bytes()
    canonical_bytes = CANONICAL_CONSTANTS.read_bytes()
    pinmap_json = json.dumps(sorted(pins.items()), sort_keys=True).encode("utf-8")  # (local)
    audit = hashlib.sha256(script_bytes + canonical_bytes + pinmap_json).hexdigest()  # (local)
    content = hashlib.sha256(script_bytes).hexdigest()  # (local)
    return audit, content


def append_verdict(
    composite: str, value_str: str,
    audit_sha: str, content_sha: str,
    sign_v: str, mag_v: str, reg_v: str,
    routing: str,
) -> None:
    """Atomic single-shot append per gate-verdicts.md S87+ canonical form:
    canonical line + dual-SHA companion + 3-tuple companion + V4-routing companion.
    """
    canonical = (
        f"{GATE_ID}: {composite} -- value='{value_str}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )  # (local)
    dual_sha = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )  # (local)
    three_tuple = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} "
        f"regime_verdict={reg_v} # {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )  # (local)
    routing_row = (
        f"# V4_routing={routing} "
        f"# {GATE_ID} routing oracle (Re:V3 Option gamma flowchart): "
        f"PASS=>T1.2 priority; FAIL=>T1.1 priority; INFO=>parallel\n"
    )  # (local)
    with open(VERDICT_FILE, "a", encoding="utf-8") as f:
        f.write(canonical)
        f.write(dual_sha)
        f.write(three_tuple)
        f.write(routing_row)


# ============================ Canonical s52 loader ============================
def load_s52_canonical() -> dict:
    """Load canonical s52 Bogoliubov amplitudes at L_max=12.

    Returns dict with:
        u_static, v_static, E_static : (8,) float64 arrays
        Delta_per_mode               : (8,) complex128 array
        branch_labels                : (8,) str array
        branch_indices               : dict mapping 'B1'|'B2'|'B3' -> array of indices
    """
    c = np.load(S52_BOG_CACHE, allow_pickle=True)
    u_static = c["u_k"].astype(np.float64)
    v_static = c["v_k"].astype(np.float64)
    E_static = c["E_qp"].astype(np.float64)
    Delta_per_mode = c["Delta_per_mode"].astype(np.complex128)
    branch_labels = c["branch_labels"]
    # Build branch indices
    branch_indices = {"B1": [], "B2": [], "B3": []}
    for i, lbl in enumerate(branch_labels):
        if lbl.startswith("B1"):
            branch_indices["B1"].append(i)
        elif lbl.startswith("B2"):
            branch_indices["B2"].append(i)
        elif lbl.startswith("B3"):
            branch_indices["B3"].append(i)
    for k in branch_indices:
        branch_indices[k] = np.array(branch_indices[k], dtype=np.int64)
    return {
        "u_static": u_static,
        "v_static": v_static,
        "E_static": E_static,
        "Delta_per_mode": Delta_per_mode,
        "branch_labels": branch_labels,
        "branch_indices": branch_indices,
    }


# ============================ B-tensor perturbation ============================
def apply_b_tensor(s52: dict, theta_1: float, theta_2: float, theta_3: float,
                   b_1: float, b_2: float) -> np.ndarray:
    """Apply multi-branch s52 B-tensor perturbation to canonical Delta_per_mode.

    Substrate-IS interpretation (per plan W1-1 Field 6 Step 3, with operator
    correction per user 2026-05-16):
        Delta_B1_pert = 0                                              [unchanged]
        Delta_B2_pert = b_1 * Delta_B2_canonical * exp(i*theta_1)
        Delta_B3_pert = b_2 * Delta_B3_canonical * exp(i*theta_2)
        theta_3 is the global phase (no effect on |v_a|^2 by gauge
                  invariance; retained for plan-parameterization
                  faithfulness)

    Returns: (8,) complex128 array of perturbed Delta_per_mode.
    """
    Delta_pert = np.zeros(8, dtype=np.complex128)  # (local)
    Delta_canon = s52["Delta_per_mode"]
    bi = s52["branch_indices"]
    # B1 ungapped: Delta = 0 always
    Delta_pert[bi["B1"]] = 0.0
    # B2 modes: rescale by b_1 with phase theta_1
    phase_B2 = np.exp(1j * theta_1)  # (local)
    Delta_pert[bi["B2"]] = b_1 * Delta_canon[bi["B2"]] * phase_B2
    # B3 modes: rescale by b_2 with phase theta_2
    phase_B3 = np.exp(1j * theta_2)  # (local)
    Delta_pert[bi["B3"]] = b_2 * Delta_canon[bi["B3"]] * phase_B3
    # theta_3 is global phase; multiplies all gapped modes uniformly
    # (no observable effect on |v_a|^2 but retained for parameterization fidelity)
    global_phase = np.exp(1j * theta_3 / 2)  # (local) /2 per plan Field 6 K_window_mag formula
    Delta_pert[bi["B2"]] *= global_phase
    Delta_pert[bi["B3"]] *= global_phase
    return Delta_pert


def reconstruct_bogoliubov(s52: dict, Delta_pert: np.ndarray) -> tuple:
    """Reconstruct (xi0, Delta_pert) per-mode from s52 static u/v/E and
    the perturbed Delta_per_mode.

    Per canonical reconstruction (S89 W5-2 + S90 CF-61):
        xi0_a = (u_static^2 - v_static^2) * E_static    [static xi^(0)]

    The static xi0 is structural (unchanged under B-tensor perturbation);
    only the Delta_per_mode varies.
    """
    u_s = s52["u_static"]
    v_s = s52["v_static"]
    E_s = s52["E_static"]
    xi0 = (u_s * u_s - v_s * v_s) * E_s  # (local)
    return xi0, Delta_pert


# ============================ Canonical K-window observable ============================
def k_dependent_bogoliubov(xi0: np.ndarray, Delta_pert: np.ndarray,
                           K_ratio: float) -> np.ndarray:
    """K-dependent Bogoliubov occupation n_a^GGE(K) = |v_a(K)|^2.

    Per S87 W2-3 Def 1-2 (acoustic K^2 BdG dispersion):
        xi_a(K) = xi0_a * (K/K_horizon)^2
        E_a(K)  = sqrt(xi_a(K)^2 + |Delta_pert_a|^2)
        v_a^2   = (1/2) * (1 - xi_a / E_a)
    """
    xi_K = xi0 * (K_ratio * K_ratio)  # (local)
    E_K = np.sqrt(xi_K * xi_K + np.abs(Delta_pert) ** 2)  # (local)
    eps_floor = 1e-30  # (local) numerical guard for ungapped modes
    E_K_safe = np.where(E_K < eps_floor, eps_floor, E_K)  # (local)
    v_K2 = 0.5 * (1.0 - xi_K / E_K_safe)  # (local)
    v_K2 = np.clip(v_K2, 0.0, 1.0)  # (local)
    return v_K2


def compute_L_emp(xi0: np.ndarray, Delta_pert: np.ndarray,
                  k_ratios: np.ndarray) -> float | None:
    """L_emp = d^2 ln P_GGE / d(ln K)^2 at K=K_horizon (5-point central FD).

    P_GGE(K) = Var_a(|v_a(K)|^2)  over the 8 Bogoliubov modes.

    Per S87 W2-3 Def 3-4 / S89 W5-2 Step 4-5 / S90 CF-61 Step 5 canonical.
    """
    n_K = len(k_ratios)
    P_GGE = np.zeros(n_K)
    for i, kr in enumerate(k_ratios):
        v_K2 = k_dependent_bogoliubov(xi0, Delta_pert, kr)
        P_GGE[i] = float(np.var(v_K2))
    if P_GGE.min() <= 0:
        return None  # regime breakdown: P_GGE non-positive somewhere
    ln_P = np.log(P_GGE)
    ln_K = np.log(k_ratios)
    h = ln_K[1] - ln_K[0]
    i0 = int(np.argmin(np.abs(ln_K)))
    if i0 < 2 or i0 > n_K - 3:
        # Fall back to 3-point central FD at edge
        d2 = (ln_P[i0 + 1] - 2 * ln_P[i0] + ln_P[i0 - 1]) / (h * h)
    else:
        d2 = (
            -ln_P[i0 - 2] + 16 * ln_P[i0 - 1] - 30 * ln_P[i0]
            + 16 * ln_P[i0 + 1] - ln_P[i0 + 2]
        ) / (12.0 * h * h)
    return float(d2)


# ============================ Main sweep ============================
def run_sweep(s52: dict, configs: np.ndarray, k_ratios: np.ndarray) -> dict:
    """Run the multi-branch B-tensor sweep over all configs.

    Returns dict with:
        L_emp_values : (N_configs,) float64 array of L_emp per config
        deltas       : (N_configs,) float64 array of (L_emp - L_EMP_CANONICAL) / |L_EMP_CANONICAL|
        n_aligned    : int, count of configs with |delta| < REL_TOL
        identity_idx : int, index of (theta=0, b=1) config (or -1 if not in scan)
        identity_L   : float, L_emp at identity config (sanity check)
    """
    n_configs = len(configs)  # (local)
    L_emp_values = np.zeros(n_configs)  # (local)
    n_regime_invalid = 0  # (local)
    identity_idx = -1  # (local)
    identity_L = None
    for i, (t1, t2, t3, b1, b2) in enumerate(configs):
        Delta_pert = apply_b_tensor(s52, t1, t2, t3, b1, b2)
        xi0, Delta_p = reconstruct_bogoliubov(s52, Delta_pert)
        L = compute_L_emp(xi0, Delta_p, k_ratios)
        if L is None:
            L_emp_values[i] = np.nan
            n_regime_invalid += 1
        else:
            L_emp_values[i] = L
        # Detect identity-B config
        if (abs(t1) < 1e-12 and abs(t2) < 1e-12 and abs(t3) < 1e-12
                and abs(b1 - 1.0) < 1e-12 and abs(b2 - 1.0) < 1e-12):
            identity_idx = i
            identity_L = L
        if i % 1000 == 0:
            print(f"  scan progress: {i}/{n_configs}")
    deltas = (L_emp_values - L_EMP_CANONICAL) / abs(L_EMP_CANONICAL)
    valid_mask = np.isfinite(deltas)
    n_aligned = int(np.sum(valid_mask & (np.abs(deltas) < REL_TOL)))
    return {
        "L_emp_values": L_emp_values,
        "deltas": deltas,
        "n_aligned": n_aligned,
        "n_regime_invalid": n_regime_invalid,
        "identity_idx": identity_idx,
        "identity_L": identity_L,
    }


def generate_configs() -> np.ndarray:
    """Generate the 16,384-config scan per plan Field 7.

    Grid: theta_k in {0, 2pi/8, ..., 14pi/8} (8 values each)
          b_k    in {0.5, 0.6, ..., 1.5}      (11 values each)
    Total: 8^3 * 11 * 11 = 61,952 configs
    Subsample: 16,384 uniform-random (seed=20260516)

    Ensures identity-B (theta=0, b=1) is INCLUDED in the subsample for
    the substrate-IS sanity check.
    """
    rng = np.random.default_rng(SEED)
    all_thetas = np.linspace(0, 2 * np.pi, N_THETA, endpoint=False)  # (local)
    all_bs = np.linspace(B_MIN, B_MAX, N_B)  # (local) values 0.5..1.5 inclusive

    # Enumerate full grid
    full_grid = []  # (local)
    for t1 in all_thetas:
        for t2 in all_thetas:
            for t3 in all_thetas:
                for b1 in all_bs:
                    for b2 in all_bs:
                        full_grid.append((t1, t2, t3, b1, b2))
    full_grid = np.array(full_grid)
    total = len(full_grid)

    # Find identity-B index (theta=0, b=1 with b=1 in {0.5..1.5} grid)
    # Note: 1.0 is exactly representable; matches b_grid value at index 5
    identity_mask = (
        (np.abs(full_grid[:, 0]) < 1e-12) &
        (np.abs(full_grid[:, 1]) < 1e-12) &
        (np.abs(full_grid[:, 2]) < 1e-12) &
        (np.abs(full_grid[:, 3] - 1.0) < 1e-12) &
        (np.abs(full_grid[:, 4] - 1.0) < 1e-12)
    )
    identity_indices = np.where(identity_mask)[0]
    assert len(identity_indices) == 1, f"Expected 1 identity config; found {len(identity_indices)}"
    identity_pos = int(identity_indices[0])

    # Subsample uniform-random
    target_N = min(SUBSAMPLE_N, total)
    chosen = rng.choice(total, size=target_N, replace=False)
    # Ensure identity is included
    if identity_pos not in chosen:
        chosen[0] = identity_pos
    return full_grid[chosen]


# ============================ Verdict evaluation ============================
def evaluate_verdict(result: dict) -> dict:
    """Evaluate PASS/FAIL/INFO verdict per resolved threshold trichotomy.

    PASS iff n_aligned >= PASS_THRESHOLD_N_ALIGNED   (BASIN; Reading B WIN)
    INFO iff 1 <= n_aligned <= INFO_BAND_UPPER       (REGIME-MARGINAL)
    FAIL iff n_aligned == 0                          (Reading A WIN)
    """
    n = result["n_aligned"]
    if n >= PASS_THRESHOLD_N_ALIGNED:
        composite = "PASS"
        sign_v = "PASS"
        mag_v = "PASS"
        reg_v = "VALID"
        routing = "Reading-B-WIN-route-T1.2-priority"
    elif 1 <= n <= INFO_BAND_UPPER:
        composite = "INFO"
        sign_v = "PASS"
        mag_v = "INFO"
        reg_v = "MARGINAL"
        routing = "REGIME-MARGINAL-T1.1-and-T1.2-parallel"
    else:  # n == 0
        composite = "FAIL"
        sign_v = "FAIL"  # identity-B failed to reproduce L_emp
        mag_v = "FAIL"
        reg_v = "VALID"  # regime still valid; FAIL is substrate-physics
        routing = "Reading-A-WIN-route-T1.1-priority"
    return {
        "composite": composite,
        "sign_verdict": sign_v,
        "magnitude_verdict": mag_v,
        "regime_verdict": reg_v,
        "routing": routing,
    }


# ============================ Diagnostic plot ============================
def make_plot(result: dict) -> None:
    """Histogram of deltas with REL_TOL bands."""
    fig, ax = plt.subplots(figsize=(10, 6))
    deltas = result["deltas"]
    valid = np.isfinite(deltas)
    ax.hist(deltas[valid], bins=80, color="steelblue", edgecolor="black", alpha=0.7)
    ax.axvline(-REL_TOL, color="red", linestyle="--", linewidth=1.5,
               label=f"+/-REL_TOL = +/-{REL_TOL:.0e}")
    ax.axvline(+REL_TOL, color="red", linestyle="--", linewidth=1.5)
    ax.axvline(0, color="black", linestyle="-", linewidth=1.0, alpha=0.5,
               label=f"L_emp_canonical = {L_EMP_CANONICAL:.6f}")
    ax.set_xlabel("delta = (L_emp(B) - L_emp_canonical) / |L_emp_canonical|")
    ax.set_ylabel("config count")
    ax.set_title(
        f"V4 multi-branch B-tensor fossil test (N={len(deltas)}; "
        f"n_aligned={result['n_aligned']}; identity_L={result.get('identity_L', 'n/a'):.6f})"
    )
    ax.legend(loc="upper right")
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=120)
    plt.close(fig)


# ============================ Main ============================
def main() -> int:
    import time
    t0 = time.time()

    # 1. Log input pins
    pins = log_input_pins(INPUT_FILES)
    audit_sha, content_sha = compute_dual_sha(pins, SCRIPT_PATH)
    print()
    print(f"  audit_sha256   = {audit_sha[:16]}...  (script+canonical+pinmap)")
    print(f"  content_sha256 = {content_sha[:16]}...  (script only)")
    print()

    # 2. Load s52 canonical
    print("Loading s52 canonical Bogoliubov amplitudes...")
    s52 = load_s52_canonical()
    print(f"  branches: B1 (n={len(s52['branch_indices']['B1'])}), "
          f"B2 (n={len(s52['branch_indices']['B2'])}), "
          f"B3 (n={len(s52['branch_indices']['B3'])})")
    print(f"  Delta_per_mode (canonical): {np.abs(s52['Delta_per_mode']).round(6)}")
    print()

    # 3. Build K-window grid
    ln_grid = np.linspace(
        math.log(K_HORIZON_FRAC[0]), math.log(K_HORIZON_FRAC[1]), N_K
    )
    k_ratios = np.exp(ln_grid)
    print(f"K-window grid: {N_K} points, K_ratio in [{k_ratios.min():.4f}, {k_ratios.max():.4f}]")
    print()

    # 4. Identity-B sanity check (L_emp at canonical s52 should reproduce -7.046336)
    print("Identity-B sanity check (theta=0, b_1=b_2=1):")
    Delta_id = apply_b_tensor(s52, 0.0, 0.0, 0.0, 1.0, 1.0)
    xi0, Dp = reconstruct_bogoliubov(s52, Delta_id)
    L_id = compute_L_emp(xi0, Dp, k_ratios)
    sanity_delta = (L_id - L_EMP_CANONICAL) / abs(L_EMP_CANONICAL) if L_id is not None else np.nan
    print(f"  L_emp(identity-B) = {L_id}")
    print(f"  L_EMP_CANONICAL   = {L_EMP_CANONICAL}")
    print(f"  delta             = {sanity_delta:+.6e}")
    sanity_pass = (abs(sanity_delta) < REL_TOL) if L_id is not None else False
    print(f"  identity sanity   = {'PASS' if sanity_pass else 'FAIL'} (REL_TOL = {REL_TOL:.0e})")
    print()

    # 5. Generate configs
    print("Generating multi-branch B-tensor scan grid...")
    configs = generate_configs()
    print(f"  N_configs = {len(configs)} (subsampled from {N_THETA}^3 * {N_B}^2 = {N_THETA**3 * N_B**2})")
    print()

    # 6. Run sweep
    print("Running sweep...")
    result = run_sweep(s52, configs, k_ratios)
    result["identity_sanity_pass"] = sanity_pass
    result["sanity_delta"] = sanity_delta
    result["L_id_sanity"] = L_id
    print(f"  n_aligned (|delta| < {REL_TOL:.0e}): {result['n_aligned']} / {len(configs)}")
    print(f"  n_regime_invalid: {result['n_regime_invalid']}")
    print(f"  identity_idx in scan: {result['identity_idx']}")
    print(f"  identity_L (from sweep): {result['identity_L']}")
    print()

    # 7. Distribution stats
    deltas = result["deltas"]
    valid = np.isfinite(deltas)
    print("Delta distribution statistics:")
    print(f"  min delta:   {deltas[valid].min():+.6e}")
    print(f"  max delta:   {deltas[valid].max():+.6e}")
    print(f"  median delta:{np.median(deltas[valid]):+.6e}")
    print(f"  mean delta:  {np.mean(deltas[valid]):+.6e}")
    print(f"  std delta:   {np.std(deltas[valid]):+.6e}")
    print()

    # 8. Evaluate verdict
    verdict = evaluate_verdict(result)
    print(f"Composite verdict: {verdict['composite']}")
    print(f"  sign_verdict:      {verdict['sign_verdict']}")
    print(f"  magnitude_verdict: {verdict['magnitude_verdict']}")
    print(f"  regime_verdict:    {verdict['regime_verdict']}")
    print(f"  V4 routing:        {verdict['routing']}")
    print()

    # 9. Save outputs
    print(f"Saving npz to {OUT_NPZ.relative_to(ROOT)}...")
    np.savez(
        OUT_NPZ,
        L_emp_values=result["L_emp_values"],
        deltas=result["deltas"],
        configs=configs,
        n_aligned=result["n_aligned"],
        n_regime_invalid=result["n_regime_invalid"],
        identity_idx=result["identity_idx"],
        identity_L=result["identity_L"],
        identity_sanity_pass=result["identity_sanity_pass"],
        L_EMP_CANONICAL=L_EMP_CANONICAL,
        REL_TOL=REL_TOL,
        PASS_THRESHOLD_N_ALIGNED=PASS_THRESHOLD_N_ALIGNED,
        SEED=SEED,
        N_THETA=N_THETA,
        N_B=N_B,
        SUBSAMPLE_N=SUBSAMPLE_N,
        L_MAX=L_MAX,
        verdict_composite=verdict["composite"],
        verdict_sign=verdict["sign_verdict"],
        verdict_magnitude=verdict["magnitude_verdict"],
        verdict_regime=verdict["regime_verdict"],
        V4_routing=verdict["routing"],
    )
    print(f"Saving plot to {OUT_PNG.relative_to(ROOT)}...")
    make_plot(result)
    print()

    # 10. Emit verdict line
    value_str = f"n_aligned={result['n_aligned']}/{len(configs)}_routing={verdict['routing']}"
    append_verdict(
        composite=verdict["composite"],
        value_str=value_str,
        audit_sha=audit_sha,
        content_sha=content_sha,
        sign_v=verdict["sign_verdict"],
        mag_v=verdict["magnitude_verdict"],
        reg_v=verdict["regime_verdict"],
        routing=verdict["routing"],
    )

    # 11. Final summary
    wall = time.time() - t0
    print(f"=== {GATE_ID}: {verdict['composite']} (wall {wall:.1f}s) ===")
    print(f"    value: {value_str}")
    print(f"    audit_sha256:   {audit_sha}")
    print(f"    content_sha256: {content_sha}")
    return 0  # PASS/FAIL/INFO all exit 0 per math-scripts.md section "Exit Codes"


if __name__ == "__main__":
    sys.exit(main())
