#!/usr/bin/env python3
"""
S86 W8-2 (P7) -- S86-RHO-SUBSTRATE-PREDICTION-MC
================================================

Gate: S86-RHO-SUBSTRATE-PREDICTION-MC ([VERIFY]+[SIGN])

Pre-registered threshold (plan §W8-2 line 419-423):
  PASS  iff  |rho_substrate-prediction| in [0.819, 1.001]
            (RATIO <= 1e-1 of reference 0.91, capped at 1.0 by Cauchy-Schwarz)
            under at least one (sign_convention, atlas_weighting) combination
            of the 6, AND bootstrap sigma_rho <= 0.05.
  INFO  iff  |rho| outside [0.819, 1.001] BUT consistent across >=4/6 cells
            (sign of |rho| in same direction for >=4/6) AND bootstrap sigma_rho <= 0.05.
  FAIL  iff  bootstrap sigma_rho > 0.05 OR max-min spread of |rho| over 6 cells > 0.5
            OR script crashes before producing 6-cell rho_grid.

Tolerance rule: RATIO (<= 1e-1) for PASS band; ABSOLUTE (sigma_rho <= 0.05)
                for stability checks.

Output 4-tuple:
  (value=(rho_signed_uniform, rho_signed_PV-dn, rho_signed_PV-excl,
          rho_mag_uniform, rho_mag_PV-dn, rho_mag_PV-excl),
   scheme=substrate-marginalized-observable,
   convention=W12-4-5-regulator-atlas+W13-2-forward-map+pre-pinned-6cell,
   L_max=10)

Classification: PHONONIC (LAYER-3 substrate-marginalized-observable; the MC
                samples the substrate's regulator-class predictions for
                (alpha_s, Omega_GW(f_LISA)) under the W12-4 5-regulator atlas).

METHODOLOGY (plan §6, 4 steps)
------------------------------
Step 1: Load W12-4 5-regulator atlas (a_0^k, a_2^k, a_4^k) for k in
        {zeta, Zubarev, SDW, cutoff_sqrt, anomaly} via _spectral_action_regulators
        evaluators. Map plan labels to helper evaluators by family:
          zeta   <- zeta_a_n           (F_4 family, class (a) INVARIANT)
          Zubarev <- mellin_a_n        (F_4 family, equivalence-class with zeta)
          SDW    <- heat_kernel_a_n    (F_4 family, Seeley-DeWitt dressed)
          cutoff_sqrt <- hard_cutoff_a_n  (M family, class (d) STRUCTURALLY-DIVERGENT)
          anomaly <- pauli_villars_a_n (M family, class (d) STRUCTURALLY-DIVERGENT)

Step 2: Substrate forward map per regulator k:
          alpha_s^k       = (n_s^k)^2 - 1           (W13-2 S50 O-Z identity)
          n_s^k           = planck_ns * (1 + kappa_ns * delta^k_a2)
          Omega_GW^k(f_L) = Omega_at_LISA_zeta * (1 + kappa_Omega * delta^k_a4)
        where:
          delta^k_a2 = (a_2^k - a_2^zeta) / a_2^zeta
          delta^k_a4 = (a_4^k - a_4^zeta) / a_4^zeta
          kappa_ns   = +1 (n_s tracks a_2 of D_K spectrum positively, W13-2 forward)
          kappa_Omega = +1 (Omega_GW amplitude tracks a_4 spectral norm positively)
          Omega_at_LISA_zeta is the W13-2 canonical anchor at f_LISA=3 mHz.

Step 3: Monte-Carlo sample. For each regulator k draw N_samples = 10000
        Gaussian perturbations of (n_s, Omega_GW) about (alpha_s^k, Omega_GW^k):
          n_s_sample      ~ N(n_s^k, sigma_k_ns)
          Omega_GW_sample ~ N(Omega_GW^k, sigma_k_Omega)
        sigma_k from W12-4 5-class taxonomy uncertainty envelope:
          F_4 family (zeta, Zubarev, SDW): sigma = 0.001 (class (a) INVARIANT)
          M family (cutoff_sqrt, anomaly): sigma = 0.05  (PINNED-BUT-DRIFT
                                                           PRU Class 8.1 fallback)
        Total ensemble: 5 regulators * 10000 samples = 50000 (regulator, sample) pairs.

Step 4: Pearson rho over the ensemble in 6 modes:
          sign_convention in {signed, magnitude}
          atlas_weighting in {uniform, PV-down-weighted, PV-excluded}
        50000-point covariance/std/Pearson routed through torch.std + torch.dot
        on AMD RX 9070 XT ROCm path (mandatory per plan §6).

Pre-registration pins (plan §6/§10) -- MUST appear in verdict line:
  sign_convention     = ALL_SIX_COMBINATIONS_REPORTED
  atlas_weighting     = ALL_THREE_COMBINATIONS_REPORTED
  N_samples           = 10000
  N_regulators        = 5
  ensemble_size       = 50000
  RANDOM_SEED         = 0xCFAB1771   (substrate-tag, fixed at plan-freeze)
  forward_map_version = W13-2 canonical
  uncertainty_envelope = W12-4 5-class default with +/-5% Gaussian fallback
                         (PINNED-BUT-DRIFT PRU Class 8.1)
  f_pivot_Hz          = 3.0e-3       (f_LISA canonical from canonical_constants)
  reference_rho_mag   = 0.91         (mack 9A §VI.2 R3 spot-check)

SUBSTRATE FRAMING (plan §13)
----------------------------
The 50000-point ensemble samples the SUBSTRATE'S regulator-class predictions for
(alpha_s, Omega_GW(f_LISA)). It is NOT a sampling over experimental noise
(LAYER-2 territory) and NOT over a parameter prior (LAYER-1 territory). The
substrate's CGWB-alpha_s correlation under W12-4 5-regulator marginalization
is |rho| = <value>; the value collapses onto a near-1D line because the 5
regulators agree on the substrate's directional response.
"""

from __future__ import annotations

# -----------------------------------------------------------------------------
# Section 1 -- Canonical constants (MANDATORY first import)
# -----------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403

# -----------------------------------------------------------------------------
# Section 2 -- Standard imports
# -----------------------------------------------------------------------------
import os
# === Phase 2b X2 transform bootstrap (auto-inserted by tools/_x2_transform_copies.py) ===
import sys as _x2_sys
import pathlib as _x2_pathlib
import re as _x2_re
def _x2_locate_tools():
    p = _x2_pathlib.Path(__file__).resolve()
    for _ in range(8):
        if (p / "tools" / "computation_root.py").is_file():
            return p / "tools"
        p = p.parent
    raise RuntimeError(
        "Phase 2b bootstrap: tools/computation_root.py not found in any "
        "ancestor of " + str(__file__))
_x2_sys.path.insert(0, str(_x2_locate_tools()))
from computation_root import resolve_script, resolve_output, resolve_glob, resolve_dynamic, project_root as _x2_project_root
def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"
_x2_session_dir_match = _x2_re.match(r"^session-(\d+)$",
    _x2_pathlib.Path(__file__).resolve().parent.name)
_x2_self_session = int(_x2_session_dir_match.group(1)) if _x2_session_dir_match else None
# === End X2 bootstrap ===

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

import torch  # GPU path mandatory per plan §6

# Helper -- 5-regulator atlas evaluators
from _spectral_action_regulators import (
    zeta_a_n,
    mellin_a_n,
    heat_kernel_a_n,
    hard_cutoff_a_n,
    pauli_villars_a_n,
)

# -----------------------------------------------------------------------------
# Section 3 -- Paths + pre-registration constants
# -----------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)
ART_DIR = resolve_script(None, '_artifacts')
ART_DIR.mkdir(parents=True, exist_ok=True)

SESSION = "S86"                                                      # (local)
GATE_ID = "S86-RHO-SUBSTRATE-PREDICTION-MC"                          # (local)
SCHEME = "substrate-marginalized-observable"                          # (local)
CONVENTION = "W12-4-5-regulator-atlas+W13-2-forward-map+pre-pinned-6cell"  # (local)
L_MAX = 10                                                            # (local)

# Pre-registered MC pins (plan §6, §7)
N_SAMPLES = 10000                                                     # (local) per regulator
N_REGULATORS = 5                                                      # (local)
ENSEMBLE_SIZE = N_SAMPLES * N_REGULATORS                              # (local) = 50000
RANDOM_SEED = 0xCFAB1771                                              # (local) substrate-tag, plan-freeze pin

# W12-4 5-class uncertainty envelope (plan §6 Step 3): F_4 invariant, M divergent
SIGMA_F4 = 0.001                                                      # (local) class (a) INVARIANT
SIGMA_M = 0.05                                                        # (local) PINNED-BUT-DRIFT 8.1 fallback

# Forward-map sensitivity coefficients (plan §10 Step 3)
KAPPA_NS = 1.0                                                        # (local) n_s tracks a_2 +1
KAPPA_OMEGA = 1.0                                                     # (local) Omega_GW tracks a_4 +1

# Pre-registered PASS band
REFERENCE_RHO_MAG = 0.91                                              # (local) mack 9A §VI.2 R3 spot-check
RATIO_TOL = 1e-1                                                      # (local) PASS band tolerance
RHO_PASS_LO = REFERENCE_RHO_MAG * (1 - RATIO_TOL)                     # (local) = 0.819
RHO_PASS_HI = min(REFERENCE_RHO_MAG * (1 + RATIO_TOL), 1.0)           # (local) = 1.0 (Cauchy-Schwarz cap)
SIGMA_RHO_STABILITY = 0.05                                            # (local) bootstrap stability threshold
SPREAD_FAIL = 0.5                                                     # (local) FAIL spread threshold

# Plan-label -> helper-evaluator map (Step 1)
REGULATOR_LABELS = ("zeta", "Zubarev", "SDW", "cutoff_sqrt", "anomaly")  # (local)
REGULATOR_EVAL_MAP = {                                                # (local)
    "zeta":         zeta_a_n,
    "Zubarev":      mellin_a_n,         # F_4 equivalence-class
    "SDW":          heat_kernel_a_n,    # F_4 Seeley-DeWitt dressed
    "cutoff_sqrt":  hard_cutoff_a_n,    # M family
    "anomaly":      pauli_villars_a_n,  # M family
}
F4_FAMILY = {"zeta", "Zubarev", "SDW"}                                # (local)
M_FAMILY = {"cutoff_sqrt", "anomaly"}                                 # (local)

# Atlas weighting schemes (plan §6 Step 4)
WEIGHTINGS = {                                                        # (local)
    "uniform":     np.array([0.20, 0.20, 0.20, 0.20, 0.20]),
    "PV-dn":       np.array([0.20, 0.20, 0.20, 0.10, 0.30]),
    "PV-excl":     np.array([1/3, 1/3, 1/3, 0.0, 0.0]),
}

# Input/output paths
INPUT_FILES = [                                                       # (local)
    resolve_script(None, 'canonical_constants.py'),
    resolve_script(None, '_spectral_action_regulators.py'),
    resolve_script(85, 's85_w12_w0_regulator_taxonomy.py'),
    resolve_script(85, 's85_w13_2_cgwb_alpha_s_joint.py'),
    resolve_output(85, 's85_w13_2_cgwb_alpha_s_joint.npz'),
    resolve_output(69, 's69_transit_gw.npz'),
    PROJECT_ROOT / "sessions/permanent-results-registry.md",
]

VERDICT_TXT = resolve_output(SESSION[1:], f's{SESSION[1:]}_gate_verdicts.txt')
OUT_NPZ = ART_DIR / "s86_w8_p7_rho_mc_ensemble.npz"
OUT_PNG = ART_DIR / "s86_w8_p7_rho_mc_grid.png"


# -----------------------------------------------------------------------------
# Section 4 -- SHA-256 + dual-SHA helpers
# -----------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    try:
        return hashlib.sha256(path.read_bytes()).hexdigest()
    except OSError:
        return ""


def log_input_pins(inputs):
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins = {}                                                         # (local)
    for p in inputs:
        sha = sha256_of(p)                                            # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")     # (local)
        pins[rel] = sha
        print(f"  {rel}: {sha[:16]}...")
    return pins


def compute_dual_sha(script_path, canonical_path, pins):
    """Dual-SHA per S84+ schema (audit_sha = full-input closure; content_sha = script-only)."""
    script_bytes = script_path.read_bytes() if script_path.exists() else b""    # (local)
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"),
                             sort_keys=True).encode("utf-8")          # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                                       # (local)
    content = hashlib.sha256(script_bytes).hexdigest()                # (local)
    return audit, content


# -----------------------------------------------------------------------------
# Section 5 -- Step 1: load W12-4 5-regulator atlas
# -----------------------------------------------------------------------------
def load_atlas():
    """Return dict label -> (a_0, a_2, a_4) tuple under plan-label mapping."""
    atlas = {}                                                        # (local)
    for label in REGULATOR_LABELS:
        evaluator = REGULATOR_EVAL_MAP[label]                         # (local)
        a0 = evaluator(0, L_MAX, Vol_SU3_Haar)                        # (local)
        a2 = evaluator(1, L_MAX, Vol_SU3_Haar)                        # (local)
        a4 = evaluator(2, L_MAX, Vol_SU3_Haar)                        # (local)
        atlas[label] = (a0, a2, a4)
    return atlas


# -----------------------------------------------------------------------------
# Section 6 -- Step 2: forward-map (a_n^k) -> (alpha_s^k, Omega_GW^k)
# -----------------------------------------------------------------------------
def omega_gw_loglog_interp(f_grid, omega_f, f_target):
    """Log-log interpolation -- inherited from W13-2."""
    omega_clip = np.maximum(omega_f, 1e-300)                          # (local)
    ln_f = np.log(f_grid)                                             # (local)
    ln_omega = np.log(omega_clip)                                     # (local)
    ln_target = np.log(f_target)                                      # (local)
    return float(np.exp(np.interp(ln_target, ln_f, ln_omega)))


def forward_map_per_regulator(atlas, omega_at_LISA_zeta):
    """For each regulator k, compute (alpha_s^k, Omega_GW^k) per plan §10 Step 3.

    Substitution chain:
      delta_a2^k = (a_2^k - a_2^zeta) / a_2^zeta
      delta_a4^k = (a_4^k - a_4^zeta) / a_4^zeta
      n_s^k     = planck_ns * (1 + kappa_ns * delta_a2^k)
      alpha_s^k = (n_s^k)^2 - 1                  (W13-2 S50 O-Z identity)
      Omega_GW^k(f_LISA) = omega_at_LISA_zeta * (1 + kappa_Omega * delta_a4^k)
    """
    a2_zeta = atlas["zeta"][1]                                        # (local)
    a4_zeta = atlas["zeta"][2]                                        # (local)
    centrals = {}                                                     # (local)
    for label in REGULATOR_LABELS:
        a0_k, a2_k, a4_k = atlas[label]
        delta_a2 = (a2_k - a2_zeta) / a2_zeta if a2_zeta != 0 else 0.0       # (local)
        delta_a4 = (a4_k - a4_zeta) / a4_zeta if a4_zeta != 0 else 0.0       # (local)
        n_s_k = planck_ns * (1.0 + KAPPA_NS * delta_a2)                # (local)
        alpha_s_k = n_s_k**2 - 1.0                                     # (local)
        omega_gw_k = omega_at_LISA_zeta * (1.0 + KAPPA_OMEGA * delta_a4)  # (local)
        centrals[label] = {
            "a_0": a0_k, "a_2": a2_k, "a_4": a4_k,
            "delta_a2": delta_a2, "delta_a4": delta_a4,
            "n_s_k": n_s_k,
            "alpha_s_k": alpha_s_k,
            "Omega_GW_k": omega_gw_k,
        }
    return centrals


# -----------------------------------------------------------------------------
# Section 7 -- Step 3: Monte-Carlo perturbations
# -----------------------------------------------------------------------------
def mc_sample_per_regulator(centrals, device, gen):
    """Draw N_SAMPLES per regulator; return ensemble_alpha_s, ensemble_omega_gw
    arrays of shape (5, N_SAMPLES). MC done on GPU per plan §6 GPU path."""
    ens_alpha = torch.zeros((N_REGULATORS, N_SAMPLES),
                            dtype=torch.float64, device=device)        # (local)
    ens_omega = torch.zeros((N_REGULATORS, N_SAMPLES),
                            dtype=torch.float64, device=device)        # (local)
    for k_idx, label in enumerate(REGULATOR_LABELS):
        c = centrals[label]
        n_s_k = c["n_s_k"]                                            # (local)
        omega_k = c["Omega_GW_k"]                                     # (local)
        sigma_ns = SIGMA_F4 if label in F4_FAMILY else SIGMA_M        # (local)
        sigma_om = SIGMA_F4 if label in F4_FAMILY else SIGMA_M        # (local)
        # n_s perturbation in units of n_s_k
        eps_ns = torch.randn(N_SAMPLES, dtype=torch.float64,
                             device=device, generator=gen) * sigma_ns  # (local)
        eps_om = torch.randn(N_SAMPLES, dtype=torch.float64,
                             device=device, generator=gen) * sigma_om  # (local)
        n_s_samples = n_s_k * (1.0 + eps_ns)                          # (local)
        # alpha_s = n_s^2 - 1 evaluated at perturbed n_s
        alpha_samples = n_s_samples * n_s_samples - 1.0               # (local)
        omega_samples = omega_k * (1.0 + eps_om)                      # (local)
        ens_alpha[k_idx, :] = alpha_samples
        ens_omega[k_idx, :] = omega_samples
    return ens_alpha, ens_omega


# -----------------------------------------------------------------------------
# Section 8 -- Step 4: Pearson rho over weighted ensemble (GPU torch routes)
# -----------------------------------------------------------------------------
def weighted_pearson_torch(X, Y, w):
    """Weighted Pearson rho on GPU.
    X, Y: shape (5, N_SAMPLES); w: shape (5,) per-regulator weights summing to 1.

    Substitution chain (plan §10 Step 1 definitions):
      <Z>_w = sum_k sum_i w_k * Z_{k,i} / (sum_k w_k * N)
      sigma_Z^2 = <(Z - <Z>)^2>_w
      Cov(X,Y) = <(X - <X>)(Y - <Y>)>_w
      rho = Cov(X,Y) / (sigma_X sigma_Y)
    """
    # Build weight tensor matching ensemble shape
    w_t = torch.tensor(w, dtype=torch.float64, device=X.device)       # (local)
    w_t = w_t / w_t.sum()                                              # (local) renormalize
    # Per-sample weight: each (k,i) has weight w_k / N_SAMPLES (uniform within k)
    w_sample = (w_t.unsqueeze(1) / float(N_SAMPLES)).expand_as(X)     # (local)
    total_w = w_sample.sum()                                          # (local) = 1.0
    Xf = X.flatten()                                                   # (local)
    Yf = Y.flatten()                                                   # (local)
    wf = w_sample.flatten()                                            # (local)
    mu_X = torch.dot(wf, Xf) / total_w                                 # (local)
    mu_Y = torch.dot(wf, Yf) / total_w                                 # (local)
    dX = Xf - mu_X                                                     # (local)
    dY = Yf - mu_Y                                                     # (local)
    var_X = torch.dot(wf, dX * dX) / total_w                           # (local)
    var_Y = torch.dot(wf, dY * dY) / total_w                           # (local)
    sigma_X = torch.sqrt(var_X)                                        # (local)
    sigma_Y = torch.sqrt(var_Y)                                        # (local)
    cov = torch.dot(wf, dX * dY) / total_w                             # (local)
    if sigma_X.item() == 0.0 or sigma_Y.item() == 0.0:
        return 0.0
    return float(cov / (sigma_X * sigma_Y))


def compute_rho_grid(ens_alpha, ens_omega):
    """Compute 6-cell rho_grid for (sign in {signed, magnitude}) x (weighting in {uniform, PV-dn, PV-excl}).

    Plan §10 Step 1 definitions:
      rho_signed    = Cov(alpha_s, Omega_GW) / (sigma_alpha * sigma_Omega)         in [-1, +1]
      rho_magnitude = |Cov(|alpha_s|, |Omega_GW|)| / (sigma_|alpha| * sigma_|Omega|) in [0, +1]

    The outer |.| on the covariance in rho_magnitude is explicit per plan §10
    line 442-445 ("magnitude Pearson cannot be negative by construction").
    """
    # Active samples: with PV-excl, regulators 3,4 carry zero weight; we still
    # include them in the tensor but the weighting nullifies their contribution.
    rho_grid = np.zeros((2, 3), dtype=np.float64)                     # (local)
    weighting_keys = ["uniform", "PV-dn", "PV-excl"]                  # (local)
    for j, wkey in enumerate(weighting_keys):
        w = WEIGHTINGS[wkey]
        # signed Pearson over (alpha_s, Omega_GW): direct, sign-preserving
        rho_signed = weighted_pearson_torch(ens_alpha, ens_omega, w)  # (local)
        rho_grid[0, j] = rho_signed
        # magnitude Pearson over (|alpha_s|, |Omega_GW|): plan §10 wraps |Cov|
        # so the resulting rho_magnitude is non-negative by construction.
        rho_mag_raw = weighted_pearson_torch(torch.abs(ens_alpha),
                                             torch.abs(ens_omega), w) # (local)
        rho_grid[1, j] = abs(rho_mag_raw)
    return rho_grid


def bootstrap_sigma_rho(ens_alpha, ens_omega, n_boot=200):
    """Bootstrap sigma_rho across the 6 cells for stability check."""
    boot = np.zeros((n_boot, 2, 3), dtype=np.float64)                 # (local)
    rng_np = np.random.default_rng(RANDOM_SEED + 1)                   # (local) bootstrap rng
    n_per_reg = ens_alpha.shape[1]                                    # (local)
    for b in range(n_boot):
        idx = rng_np.integers(0, n_per_reg, size=n_per_reg)           # (local)
        ens_alpha_b = ens_alpha[:, idx]
        ens_omega_b = ens_omega[:, idx]
        boot[b] = compute_rho_grid(ens_alpha_b, ens_omega_b)
    sigma_grid = boot.std(axis=0)                                     # (local)
    return sigma_grid


# -----------------------------------------------------------------------------
# Section 9 -- Verdict logic
# -----------------------------------------------------------------------------
def evaluate_gate(rho_grid, sigma_grid):
    """Apply plan §9 PASS/INFO/FAIL band assignment.

    Substitution chain (plan §9):
      |rho_cell| in [RHO_PASS_LO, RHO_PASS_HI] under >=1 cell + max(sigma_grid) <= 0.05 -> PASS
      else: |rho| consistent across >=4/6 cells (sign of |rho| same direction) + sigma <= 0.05 -> INFO
      else: FAIL
    """
    abs_rho = np.abs(rho_grid)                                        # (local)
    sigma_max = float(np.max(sigma_grid))                             # (local)
    spread = float(abs_rho.max() - abs_rho.min())                     # (local) max-min spread

    if sigma_max > SIGMA_RHO_STABILITY:
        return "FAIL", f"bootstrap sigma_rho_max={sigma_max:.4f} > {SIGMA_RHO_STABILITY}"
    if spread > SPREAD_FAIL:
        return "FAIL", f"max-min spread of |rho| over 6 cells = {spread:.4f} > {SPREAD_FAIL}"

    in_band = (abs_rho >= RHO_PASS_LO) & (abs_rho <= RHO_PASS_HI)     # (local)
    if in_band.any():
        return "PASS", f"{int(in_band.sum())} cell(s) in PASS band; sigma_max={sigma_max:.4f}"

    # INFO check: |rho| consistent across >=4/6 cells
    consistent_cells = int((abs_rho > 0.5).sum())                     # (local)
    if consistent_cells >= 4:
        return "INFO", f"|rho| > 0.5 in {consistent_cells}/6 cells but none in PASS band"
    return "FAIL", f"|rho| outside PASS band and not consistent across >=4/6 cells"


# -----------------------------------------------------------------------------
# Section 10 -- Main
# -----------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()                                                  # (local)
    print(f"=== {GATE_ID} (S86 W8-2 / P7) ===")
    print(f"  Classification: PHONONIC (LAYER-3 substrate-prediction MC)")
    print(f"  Convention: {CONVENTION}")
    print(f"  L_max = {L_MAX}; ensemble_size = {ENSEMBLE_SIZE}; seed = 0x{RANDOM_SEED:08X}")
    print()

    # Input pinning + dual-SHA
    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()                            # (local)
    canonical_path = resolve_script(None, 'canonical_constants.py')             # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print()

    # CHAIN warning if W0b R7+R8 entries absent (per plan dispatch policy)
    prr_path = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"
    prr_text = prr_path.read_text(encoding="utf-8")                   # (local)
    has_R7 = "R7" in prr_text and "single-name" in prr_text.lower()   # (local)
    has_R8 = ("S86-PRR-THREE-LAYER-ADJUDICATION" in prr_text or
              "three-layer adjudication" in prr_text.lower())         # (local)
    if has_R7 and has_R8:
        print("  CHAIN: permanent-results-registry W0b R7+R8 LANDED.")
    else:
        print(f"  CHAIN WARNING: R7={has_R7} R8={has_R8} (W0b methodology not yet landed)")
    print()

    # GPU selection
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"  GPU device: {device}; torch={torch.__version__}")
    if device.type == "cuda":
        gen = torch.Generator(device=device).manual_seed(RANDOM_SEED)
    else:
        gen = torch.Generator().manual_seed(RANDOM_SEED)
    print()

    # Step 1: load W12-4 5-regulator atlas
    print("=" * 78)
    print("STEP 1 -- W12-4 5-regulator atlas (a_0^k, a_2^k, a_4^k)")
    print("=" * 78)
    atlas = load_atlas()
    print(f"  {'label':12s}  {'a_0':>14s}  {'a_2':>14s}  {'a_4':>14s}  family")
    for label in REGULATOR_LABELS:
        a0, a2, a4 = atlas[label]
        fam = "F_4" if label in F4_FAMILY else "M"
        print(f"  {label:12s}  {a0:14.6e}  {a2:14.6e}  {a4:14.6e}  {fam}")
    print()

    # Inherit Omega_GW(f_LISA) anchor from W13-2 cache
    print("=" * 78)
    print("STEP 2A -- W13-2 anchor: Omega_GW(f_LISA=3 mHz)")
    print("=" * 78)
    s69 = np.load(resolve_output(69, 's69_transit_gw.npz'), allow_pickle=True)
    s69_f_grid = s69["f_grid"]                                        # (local)
    s69_Omega_f = s69["Omega_GW_f"]                                   # (local)
    omega_at_LISA_zeta = omega_gw_loglog_interp(
        s69_f_grid, s69_Omega_f, f_LISA_pivot)                        # (local)
    print(f"  f_LISA_pivot = {f_LISA_pivot} Hz (canonical_constants)")
    print(f"  Omega_GW(f_LISA, zeta-anchor) = {omega_at_LISA_zeta:.6e}")
    print()

    # Step 2: forward map per regulator
    print("=" * 78)
    print("STEP 2B -- Forward map per regulator (substitution chain)")
    print("=" * 78)
    centrals = forward_map_per_regulator(atlas, omega_at_LISA_zeta)
    print(f"  {'label':12s}  {'delta_a2':>12s}  {'delta_a4':>12s}  "
          f"{'n_s^k':>10s}  {'alpha_s^k':>14s}  {'Omega_GW^k':>14s}")
    for label in REGULATOR_LABELS:
        c = centrals[label]
        print(f"  {label:12s}  {c['delta_a2']:12.4e}  {c['delta_a4']:12.4e}  "
              f"{c['n_s_k']:10.6f}  {c['alpha_s_k']:14.6e}  {c['Omega_GW_k']:14.6e}")
    print()

    # Step 3: MC sample
    print("=" * 78)
    print(f"STEP 3 -- Monte-Carlo: {N_REGULATORS} x {N_SAMPLES} = {ENSEMBLE_SIZE} samples")
    print("=" * 78)
    ens_alpha, ens_omega = mc_sample_per_regulator(centrals, device, gen)
    print(f"  ens_alpha shape = {tuple(ens_alpha.shape)}; "
          f"ens_omega shape = {tuple(ens_omega.shape)}")
    # Ensemble means and stds (overall, uniform weighting) for substitution chain
    mu_alpha_uni = float(ens_alpha.mean())                            # (local)
    mu_omega_uni = float(ens_omega.mean())                            # (local)
    sd_alpha_uni = float(ens_alpha.std())                             # (local)
    sd_omega_uni = float(ens_omega.std())                             # (local)
    print(f"  <alpha_s> (uniform) = {mu_alpha_uni:.6e}  sigma_alpha = {sd_alpha_uni:.6e}")
    print(f"  <Omega_GW>(uniform) = {mu_omega_uni:.6e}  sigma_Omega = {sd_omega_uni:.6e}")
    print()

    # Step 4: 6-cell rho_grid via weighted Pearson on GPU
    print("=" * 78)
    print("STEP 4 -- 6-cell rho_grid (signed/magnitude x uniform/PV-dn/PV-excl)")
    print("=" * 78)
    rho_grid = compute_rho_grid(ens_alpha, ens_omega)
    print(f"  {'sign\\weight':14s}  {'uniform':>12s}  {'PV-dn':>12s}  {'PV-excl':>12s}")
    print(f"  {'signed':14s}  {rho_grid[0,0]:12.6f}  {rho_grid[0,1]:12.6f}  {rho_grid[0,2]:12.6f}")
    print(f"  {'magnitude':14s}  {rho_grid[1,0]:12.6f}  {rho_grid[1,1]:12.6f}  {rho_grid[1,2]:12.6f}")
    print()

    # Bootstrap stability
    print("=" * 78)
    print("STEP 4B -- Bootstrap sigma_rho (stability check, 200 resamples)")
    print("=" * 78)
    sigma_grid = bootstrap_sigma_rho(ens_alpha, ens_omega, n_boot=200)
    print(f"  {'sign\\weight':14s}  {'uniform':>12s}  {'PV-dn':>12s}  {'PV-excl':>12s}")
    print(f"  {'signed':14s}  {sigma_grid[0,0]:12.6f}  {sigma_grid[0,1]:12.6f}  {sigma_grid[0,2]:12.6f}")
    print(f"  {'magnitude':14s}  {sigma_grid[1,0]:12.6f}  {sigma_grid[1,1]:12.6f}  {sigma_grid[1,2]:12.6f}")
    print()

    # Verdict
    verdict, reason = evaluate_gate(rho_grid, sigma_grid)
    print("=" * 78)
    print(f"VERDICT: {verdict}  --  {reason}")
    print("=" * 78)
    print(f"  PASS band:  |rho| in [{RHO_PASS_LO:.3f}, {RHO_PASS_HI:.3f}] "
          f"(reference {REFERENCE_RHO_MAG} +/- {RATIO_TOL*100:.0f}%)")
    print(f"  Stability:  bootstrap sigma_rho <= {SIGMA_RHO_STABILITY}")
    print(f"  FAIL spread: {SPREAD_FAIL}")
    print()

    # 4-tuple report
    v1, v2, v3 = rho_grid[0]
    v4, v5, v6 = rho_grid[1]
    val_str = (f"(rho_signed_uniform={v1:.6f},"
               f"rho_signed_PV-dn={v2:.6f},"
               f"rho_signed_PV-excl={v3:.6f},"
               f"rho_mag_uniform={v4:.6f},"
               f"rho_mag_PV-dn={v5:.6f},"
               f"rho_mag_PV-excl={v6:.6f})")                          # (local)
    print(f"4-tuple: (value={val_str}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    print()

    # Save NPZ
    np.savez_compressed(
        OUT_NPZ,
        ensemble_alpha_s=ens_alpha.cpu().numpy(),
        ensemble_omega_gw=ens_omega.cpu().numpy(),
        rho_grid=rho_grid,
        sigma_grid=sigma_grid,
        regulator_labels=np.array(REGULATOR_LABELS, dtype=object),
        atlas_a0=np.array([atlas[k][0] for k in REGULATOR_LABELS]),
        atlas_a2=np.array([atlas[k][1] for k in REGULATOR_LABELS]),
        atlas_a4=np.array([atlas[k][2] for k in REGULATOR_LABELS]),
        delta_a2=np.array([centrals[k]["delta_a2"] for k in REGULATOR_LABELS]),
        delta_a4=np.array([centrals[k]["delta_a4"] for k in REGULATOR_LABELS]),
        alpha_s_central=np.array([centrals[k]["alpha_s_k"] for k in REGULATOR_LABELS]),
        omega_gw_central=np.array([centrals[k]["Omega_GW_k"] for k in REGULATOR_LABELS]),
        omega_at_LISA_zeta=omega_at_LISA_zeta,
        f_LISA_pivot=f_LISA_pivot,
        planck_ns=planck_ns,
        N_samples=N_SAMPLES,
        N_regulators=N_REGULATORS,
        ensemble_size=ENSEMBLE_SIZE,
        random_seed=RANDOM_SEED,
        reference_rho_mag=REFERENCE_RHO_MAG,
        ratio_tol=RATIO_TOL,
        verdict=verdict,
        scheme=SCHEME,
        convention=CONVENTION,
        L_max=L_MAX,
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )

    # Heatmap PNG
    fig, ax = plt.subplots(figsize=(8.5, 5.5))
    abs_rho = np.abs(rho_grid)
    im = ax.imshow(abs_rho, cmap="viridis", vmin=0.0, vmax=1.0, aspect="auto")
    ax.set_xticks([0, 1, 2])
    ax.set_xticklabels(["uniform", "PV-down-weighted", "PV-excluded"])
    ax.set_yticks([0, 1])
    ax.set_yticklabels(["signed", "magnitude"])
    for i in range(2):
        for j in range(3):
            txt = (f"{rho_grid[i,j]:.3f}\n"
                   f"|{abs_rho[i,j]:.3f}|\n"
                   f"sigma={sigma_grid[i,j]:.3f}")
            ax.text(j, i, txt, ha="center", va="center",
                    color="white" if abs_rho[i,j] < 0.5 else "black",
                    fontsize=9)
    cbar = plt.colorbar(im, ax=ax, label=r"$|\rho|$")
    ax.set_title(f"{GATE_ID}: 6-cell rho_grid (verdict={verdict}); "
                 f"reference |rho|={REFERENCE_RHO_MAG} (R3 spot-check)\n"
                 f"PASS band [{RHO_PASS_LO:.3f}, {RHO_PASS_HI:.3f}]; "
                 f"bootstrap sigma_rho threshold {SIGMA_RHO_STABILITY}")
    ax.set_xlabel("atlas_weighting")
    ax.set_ylabel("sign_convention")
    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=140, bbox_inches="tight")
    plt.close(fig)

    # Verdict-line append
    verdict_line = (
        f"{GATE_ID}: {verdict} -- value={val_str} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )                                                                 # (local)
    companion = (f"# audit_sha256 companion row: {GATE_ID} "
                 f"audit={audit_sha[:16]} content={content_sha[:16]}\n")  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(verdict_line)
        fp.write(companion)

    wall = time.time() - t0                                           # (local)
    print("=" * 78)
    print("OUTPUTS SAVED")
    print("=" * 78)
    print(f"  Script    : {__file__}")
    print(f"  Data      : {OUT_NPZ}")
    print(f"  Plot      : {OUT_PNG}")
    print(f"  Verdict   : appended to {VERDICT_TXT}")
    print()
    print(f"VERDICT LINE:")
    print(f"  {verdict_line.strip()}")
    print(f"  {companion.strip()}")
    print()
    print(f"=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
