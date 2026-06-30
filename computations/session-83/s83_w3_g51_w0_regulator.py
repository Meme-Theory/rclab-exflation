#!/usr/bin/env python3
"""
S83 Wave 3 Gate G51 — W_0-REGULATOR-CANONICAL-CHOICE
=====================================================

Tests whether w_0 under the canonical IC regulator (R = Zubarev, determined
by W1-G1 PASS in Wave 1 of S83) reproduces the S58/S59 canonical prediction
w_0 = -0.918 (Volovik partition: Josephson ground state + GGE excess).

Context:
  - W1-G1 [S83-IC-SCHEME-DERIVATION] PASS: R_canonical = Zubarev
    (L_max=5, convention=substrate-native, Branch-B Zubarev Gaussian
     regulator f(lam) = exp(-lam^2 / M_KK^2) uniquely selected by
     Connes-Moscovici integrability + local-min-tau + KK-sign = +1)
  - S58 Volovik partition (unregulated baseline): w_0 = -0.9180213
  - The question here: does the Zubarev UV regulator preserve w_0 within
    the gate tolerance |w_0 - (-0.918)| < 0.02?

SUBSTITUTION CHAIN [VERIFY]:
  Step 1 (Definitions):
    w_0 := effective DE equation of state at z=0 (fold).
    Under Volovik partition:
      rho_vac_total = rho_J/cell + rho_GGE      (energy density)
      P_vac_total   = -rho_J/cell + P_GGE       (pressure)
      w_0          = P_vac_total / rho_vac_total
    rho_J = |F_Josephson| is the superfluid ground-state stiffness; it is
    a topological CPT invariant at tau=tau_fold (does not depend on R).
    rho_GGE and P_GGE are spectral sums that DO depend on R.

  Step 2 (Substitution — R dressing):
    Under regulator R with weight f_R(lam):
      rho_GGE(R) = sum_n d_n * f_R(lam_n) * epsilon_GGE(n)
      P_GGE(R)   = sum_n d_n * f_R(lam_n) * p_GGE(n)
    where epsilon_GGE(n) and p_GGE(n) are the bare per-mode energy/pressure
    (from S57 W2-3 GGE quasiparticle distribution).

    For the S58 unregulated baseline: f_zeta(lam) = 1 (all modes, zeta (0)
    convention). This gives rho_GGE_bare = 1.709 M_KK, P_GGE_bare = -0.688,
    w_GGE_bare = -0.408.

    Under Zubarev: f_Zub(lam) = exp(-lam^2 / M_KK^2). At tau_fold=0.19
    on L_max=5 filter:
      S_Zubarev = 3805.668  (W1-G1)
      S_zeta    = 159936.0  (W1-G1)
      Suppression ratio xi_Zub := S_Zubarev / S_zeta = 0.02379

    The KEY INSIGHT: w_GGE = P_GGE / rho_GGE is a RATIO. If the spectral
    weight f_R affects every term in rho_GGE and P_GGE proportionally, the
    ratio is invariant (first-order R-independence of w_GGE).

  Step 3 (Simplify):
    Let eta(lam_n) := p_GGE(n) / epsilon_GGE(n) be the per-mode "equation of
    state" (bounded in [-1, 1/3]).
    rho_GGE(R) = sum_n d_n * f_R(lam_n) * epsilon_GGE(n)
    P_GGE(R)   = sum_n d_n * f_R(lam_n) * epsilon_GGE(n) * eta(lam_n)
    w_GGE(R)   = P_GGE(R) / rho_GGE(R)
               = <eta>_f_R                          (weighted average)

    If eta is approximately uniform (isotropic GGE): w_GGE(R) ≈ <eta>_bare
    independent of R. If eta depends on lam, w_GGE(R) probes low-lam
    modes (Zubarev) vs all modes (zeta).

    For the Josephson sector:
      w_J = -1 exactly (pure CC, R-INDEPENDENT by topological stability).
      rho_J/cell = |F_J|/N_cells = 10.520 M_KK/cell (R-INDEPENDENT).

    Combined:
      w_0(R) = [-rho_J/cell + P_GGE(R)] / [rho_J/cell + rho_GGE(R)]

    Since rho_J/cell (10.520) >> rho_GGE (1.709), the w_0 is dominated by
    the Josephson contribution:
      w_0(R) = -1 + (rho_GGE(R) + P_GGE(R)) / (rho_J/cell + rho_GGE(R))

    The sensitivity to R enters via how rho_GGE(R) + P_GGE(R) scales.

  Step 4 (Direction):
    Under Zubarev: high-lam modes suppressed. Since GGE quasiparticles
    have eta(lam) approximately bounded by -1/3 <= eta <= 1/3 (acoustic
    Bogoliubov + Leggett admixture), and the Zubarev suppression is
    smooth Gaussian, the RATIO w_GGE(Zubarev) ≈ w_GGE(bare) = -0.408
    to O(1%) correction.

    The ABSOLUTE rho_GGE, P_GGE both rescale by ~xi_Zub = 0.0238, but
    this preserves the ratio and therefore w_GGE.

    In the combined w_0: rho_GGE(Zub) = xi_Zub * rho_GGE(bare) = 0.0407
    vs rho_J/cell = 10.520. The Josephson dominates EVEN MORE under
    Zubarev (since GGE is suppressed), pushing w_0(Zub) CLOSER to -1.

    PASS if |w_0(Zub) - (-0.918)| < 0.02
    INFO if 0.02 <= |w_0(Zub) - (-0.918)| < 0.05
    FAIL if |w_0(Zub) - (-0.918)| >= 0.05

  Step 5 (Python verification): See Section 4 below.

Outputs:
  - computations/session-83/s83_w3_g51_w0_regulator.npz
  - computations/session-83/s83_w3_g51_w0_regulator.png
  - Verdict line appended to computations/session-83/s83_gate_verdicts.txt
"""

import os
# CPU fallback cap (prior to numpy import)
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import sys
import json
import hashlib
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from canonical_constants import (
    M_KK, tau_fold, Delta_BCS, N_cells, PI,
    w0_FW,  # Framework w_0 = -0.918 canonical reference
)

# =============================================================================
# Section 1. Input pin map + SHA-256 closure helper
# =============================================================================
def _sha256_file(path):
    if not Path(path).exists():
        return "FILE_MISSING"
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

INPUT_PINS = {
    "W1_G1_verdict":     SCRIPT_DIR / "s83_w1_g1_ic_scheme_derivation.npz",
    "S58_volovik":       SCRIPT_DIR / "s58_volovik_partition.npz",
    "S58_w_desi":        SCRIPT_DIR / "s58_w_desi.npz",
    "S57_cc_sign":       SCRIPT_DIR / "s57_cc_sign.npz",
    "S57_channel_budget":SCRIPT_DIR / "s57_channel_energy_budget.npz",
    "spectrum_cache":    SCRIPT_DIR / "s74_spectrum_cache_L9_tau019.npz",
    "canonical_const":   SCRIPT_DIR / "canonical_constants.py",
    "self_script":       SCRIPT_DIR / "s83_w3_g51_w0_regulator.py",
}

print("=" * 78)
print("S83 W3-G51 — W_0-REGULATOR-CANONICAL-CHOICE")
print("=" * 78)
print("\nInput pins:")
pin_hashes = {}
for name, path in INPUT_PINS.items():
    h = _sha256_file(path)
    pin_hashes[name] = h
    rel = str(path).replace(str(SCRIPT_DIR) + os.sep, '')
    print(f"  {name:22s} = {rel:45s}  sha256={h[:16]}...")

# =============================================================================
# Section 2. Load W1-G1 verdict — CANONICAL R
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 2: Load W1-G1 verdict — canonical IC regulator")
print("=" * 78)

w1g1 = np.load(INPUT_PINS["W1_G1_verdict"], allow_pickle=True)
R_canonical = str(w1g1['R_canonical'])           # (local) Zubarev
w1g1_verdict = str(w1g1['verdict'])              # (local) PASS
S_zeta     = float(w1g1['S_zeta'])               # (local) 159936.0
S_Zubarev  = float(w1g1['S_Zubarev'])            # (local) 3805.668
S_SDW      = float(w1g1['S_SDW'])                # (local) 304975
L_max_w1g1 = int(w1g1['L_max'])                  # (local) 5
N_modes    = float(w1g1['N_modes_mult'])         # (local) 159936

# Suppression ratios (local)
xi_Zubarev = S_Zubarev / S_zeta                  # (local) ~0.02379
xi_SDW     = S_SDW     / S_zeta                  # (local) ~1.907 (actually amplifies)

print(f"\n  W1-G1 verdict:     {w1g1_verdict}")
print(f"  R_canonical:       {R_canonical}")
print(f"  branch_selected:   {str(w1g1['branch_selected'])}")
print(f"  L_max (W1-G1):     {L_max_w1g1}")
print(f"  S_zeta:            {S_zeta:.3f}   (bare / zeta (0) scheme)")
print(f"  S_Zubarev:         {S_Zubarev:.3f}    <-- CANONICAL")
print(f"  S_SDW:             {S_SDW:.3f}")
print(f"  xi_Zubarev:        {xi_Zubarev:.6f} (Zubarev mode-weight ratio vs zeta)")
print(f"  xi_SDW:            {xi_SDW:.6f}")

assert R_canonical == "Zubarev", "W1-G1 did not select Zubarev as canonical"

# =============================================================================
# Section 3. Load S58 Volovik partition (unregulated baseline)
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 3: Load S58 Volovik partition (unregulated / zeta baseline)")
print("=" * 78)

s58v = np.load(INPUT_PINS["S58_volovik"], allow_pickle=True)
s58w = np.load(INPUT_PINS["S58_w_desi"], allow_pickle=True)
s57c = np.load(INPUT_PINS["S57_cc_sign"], allow_pickle=True)

# S57 GGE sector (regulator-independent reference)
Lambda_eff = float(s57c['Lambda_eff_MKK'])       # (local) 1.709 M_KK
w_GGE_bare = float(s57c['w_GGE'])                # (local) -0.408
E_GGE_bare = float(s57c['E_GGE'])                # (local) 1.688 M_KK
P_GGE_bare = float(s57c['P_vac_GGE'])            # (local) -0.688

# S58 Volovik partition outputs (already computed at Josephson + GGE)
F_Josephson = float(s58v['F_Josephson'])         # (local) -336.641 M_KK
rho_J_per_cell_s58 = abs(F_Josephson) / N_cells  # (local) 10.520 M_KK/cell
w_combined_s58 = float(s58v['w_combined'])       # (local) -0.917 (S58 baseline)
w_eff_Volovik_s58 = float(s58v['w_eff_Volovik']) # (local) -0.917
w0_A_s58 = float(s58w['w_0_A'])                  # (local) -0.9180875 (S58 canonical w_0)

print(f"\n  From S57 cc_sign (GGE spectral sector):")
print(f"    Lambda_eff (rho_GGE): {Lambda_eff:.6f} M_KK")
print(f"    P_GGE:                {P_GGE_bare:.6f} M_KK")
print(f"    w_GGE_bare:           {w_GGE_bare:.6f}")
print(f"    E_GGE_bare:           {E_GGE_bare:.6f} M_KK")
print(f"\n  From S58 volovik_partition:")
print(f"    F_Josephson:          {F_Josephson:.3f} M_KK (topological CPT invariant)")
print(f"    rho_J/cell:           {rho_J_per_cell_s58:.6f} M_KK")
print(f"    w_combined (S58):     {w_combined_s58:.6f}")
print(f"\n  From S58 w_desi (canonical w_0):")
print(f"    w_0 (interp. A):      {w0_A_s58:.6f}  <-- baseline reference")
print(f"    w0_FW (constant):     {w0_FW:.6f}")

# =============================================================================
# Section 4. Compute w_0 under canonical R = Zubarev
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 4: w_0 under canonical R = Zubarev")
print("=" * 78)

# -------------------------------------------------------------------------
# (i) Josephson sector — R-INDEPENDENT
# -------------------------------------------------------------------------
# F_Josephson is a topological CPT invariant: the condensation free energy
# of the superfluid ground state, independent of UV regulator choice.
# (It is computed from the BCS gap Delta_BCS squared integrated over the
# fermion pocket, which is exponentially suppressed at large lam and thus
# INDEPENDENT of f_R(lam) at leading order.)
rho_J_R = rho_J_per_cell_s58                       # (local) R-independent
P_J_R   = -rho_J_per_cell_s58                      # (local) w_J = -1

# -------------------------------------------------------------------------
# (ii) GGE sector — R-dependent via spectral weight
# -------------------------------------------------------------------------
# The GGE pressure/density are *bare* (zeta-scheme) spectral sums.
# Under Zubarev regulator, each mode is weighted by f_R(lam) = exp(-lam^2/M_KK^2).
# We need to convert the bare (zeta) GGE sums to the Zubarev scheme.
#
# Decomposition:
#   rho_GGE_bare = sum_n d_n * epsilon_GGE(n)           (S57 computed)
#   rho_GGE_Zub  = sum_n d_n * f_Zub(lam_n) * epsilon_GGE(n)
#
# If epsilon_GGE(n) is approximately uniform across modes (i.e., excitation
# energy per mode ~ O(M_KK)), then
#   rho_GGE_Zub ≈ <f_Zub> * rho_GGE_bare
# where <f_Zub> = S_Zubarev / S_zeta = xi_Zubarev = 0.0238.
#
# For the PRESSURE:
#   P_GGE(R) = -(1/3) sum_n d_n * f_R(lam_n) * eps_n * (group_velocity^2)
# The group velocity is mode-dependent (acoustic vs. Leggett vs. Bogoliubov).
# For a GGE dominated by acoustic Bogoliubov modes, group velocity is
# UV-suppressed (c_s at low lam, transitioning to different scaling at high lam).
# The RATIO P_GGE/rho_GGE = w_GGE is approximately MODE-INDEPENDENT (it is
# the equation-of-state of the GGE distribution), and is R-invariant to
# leading order.

# Load flat lambdas & mults for the actual dressing computation
flat_lambdas = np.asarray(w1g1['flat_lambdas'], dtype=np.float64)  # (local) shape (N,)
flat_mults   = np.asarray(w1g1['flat_mults'],   dtype=np.float64)  # (local)

# Spectral weight functions (match W1-G1 definitions)
def weight_zeta(lam):
    return np.ones_like(lam)

def weight_zubarev(lam, Lambda_Z=1.0):
    return np.exp(-(lam / Lambda_Z) ** 2)

w_zeta = weight_zeta(flat_lambdas)                 # (local)
w_zub  = weight_zubarev(flat_lambdas)              # (local)

# Verify S_R computations match W1-G1 exactly
S_zeta_check    = float((flat_mults * w_zeta).sum())
S_Zubarev_check = float((flat_mults * w_zub).sum())
assert abs(S_zeta_check    - S_zeta) < 1e-3, "S_zeta mismatch with W1-G1"
assert abs(S_Zubarev_check - S_Zubarev) < 1e-3, "S_Zubarev mismatch with W1-G1"
print(f"\n  [VERIFY] S_zeta    check:  {S_zeta_check:.3f}  vs W1-G1 {S_zeta:.3f}")
print(f"  [VERIFY] S_Zubarev check:  {S_Zubarev_check:.3f}   vs W1-G1 {S_Zubarev:.3f}")

# -------------------------------------------------------------------------
# (iii) Mode-dependent GGE weighting — refined model
# -------------------------------------------------------------------------
# Model: epsilon_GGE(lam) ~ lam (massive dispersion in acoustic branch)
# This is the standard GGE dispersion for Bogoliubov modes: eps ~ c_s * k
# at low lam, eps ~ lam at high lam (free-particle limit).
#
# For the dressed density:
#   rho_GGE(R) = sum_n d_n * f_R(lam_n) * lam_n   (up to normalization)
#   P_GGE(R)   = w_GGE * rho_GGE(R)   (first-order eta-uniform approx)
#
# Normalize so that rho_GGE(zeta) = Lambda_eff = 1.709 M_KK from S57.

# Energy-weighted spectral sums
S_zeta_E    = float((flat_mults * w_zeta * flat_lambdas).sum())  # (local)
S_Zubarev_E = float((flat_mults * w_zub  * flat_lambdas).sum())  # (local)

# Normalization: S57 computed Lambda_eff = 1.709 in zeta scheme (unregulated)
# Calibrate: Lambda_eff(zeta) = norm * S_zeta_E
norm_GGE = Lambda_eff / S_zeta_E if S_zeta_E > 0 else 0.0          # (local)

rho_GGE_Zub = norm_GGE * S_Zubarev_E                               # (local)
P_GGE_Zub   = w_GGE_bare * rho_GGE_Zub                             # (local) w_GGE ratio preserved

# Also try the "flat weighting" (uniform epsilon per mode) for cross-check:
rho_GGE_Zub_flat = Lambda_eff * xi_Zubarev                         # (local) flat-mode approx
P_GGE_Zub_flat   = P_GGE_bare * xi_Zubarev                         # (local)

print(f"\n  GGE sector under Zubarev:")
print(f"    S_zeta_E (energy-wtd): {S_zeta_E:.3f}")
print(f"    S_Zubarev_E:           {S_Zubarev_E:.3f}")
print(f"    xi_E (energy ratio):   {S_Zubarev_E/S_zeta_E:.6f}")
print(f"    norm_GGE (calibration): {norm_GGE:.6e}")
print(f"\n  GGE energy-weighted (eps ~ lam) model:")
print(f"    rho_GGE_Zub:          {rho_GGE_Zub:.6f} M_KK")
print(f"    P_GGE_Zub:            {P_GGE_Zub:.6f} M_KK")
print(f"  GGE flat-weighting model (uniform eps):")
print(f"    rho_GGE_Zub_flat:     {rho_GGE_Zub_flat:.6f} M_KK")
print(f"    P_GGE_Zub_flat:       {P_GGE_Zub_flat:.6f} M_KK")

# -------------------------------------------------------------------------
# (iv) Combined w_0 under Zubarev canonical
# -------------------------------------------------------------------------
# w_0 = (P_J + P_GGE) / (rho_J + rho_GGE)

# Primary: energy-weighted Zubarev (most physically motivated)
rho_vac_Zub = rho_J_R + rho_GGE_Zub                                # (local)
P_vac_Zub   = P_J_R   + P_GGE_Zub                                  # (local)
w_0_Zubarev = P_vac_Zub / rho_vac_Zub                              # (local) PRIMARY

# Cross-check: flat weighting
rho_vac_Zub_flat = rho_J_R + rho_GGE_Zub_flat                      # (local)
P_vac_Zub_flat   = P_J_R   + P_GGE_Zub_flat                        # (local)
w_0_Zubarev_flat = P_vac_Zub_flat / rho_vac_Zub_flat               # (local)

# Cross-check: zeta baseline (should match S58)
rho_vac_zeta = rho_J_R + Lambda_eff                                # (local)
P_vac_zeta   = P_J_R   + P_GGE_bare                                # (local)
w_0_zeta     = P_vac_zeta / rho_vac_zeta                           # (local)

print(f"\n  COMBINED w_0:")
print(f"    w_0 (zeta baseline, S58):   {w_0_zeta:.6f}   [should match -0.9180875]")
print(f"    w_0 (Zubarev, E-weighted):  {w_0_Zubarev:.6f}   <-- PRIMARY")
print(f"    w_0 (Zubarev, flat):        {w_0_Zubarev_flat:.6f}")

# =============================================================================
# Section 5. Direction analysis & gate verdict
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 5: Direction analysis & gate verdict")
print("=" * 78)

# Threshold band
w_0_target = -0.918                                                # (local)
PASS_tol   = 0.02                                                  # (local)
INFO_tol   = 0.05                                                  # (local)

def verdict(w_val, target, pass_t, info_t):
    d = abs(w_val - target)
    if d < pass_t:
        return "PASS", d
    elif d < info_t:
        return "INFO", d
    else:
        return "FAIL", d

v_zeta,     d_zeta     = verdict(w_0_zeta,         w_0_target, PASS_tol, INFO_tol)
v_Zubarev,  d_Zubarev  = verdict(w_0_Zubarev,      w_0_target, PASS_tol, INFO_tol)
v_Zub_flat, d_Zub_flat = verdict(w_0_Zubarev_flat, w_0_target, PASS_tol, INFO_tol)

print(f"\n  Gate threshold:")
print(f"    target  = {w_0_target}")
print(f"    PASS if |w_0 - target| < {PASS_tol}")
print(f"    INFO if {PASS_tol} <= |w_0 - target| < {INFO_tol}")
print(f"    FAIL if |w_0 - target| >= {INFO_tol}")

print(f"\n  Per-scheme verdicts:")
print(f"    {'Scheme':30s} | {'w_0':>10s} | {'|w_0-(-0.918)|':>14s} | {'Verdict'}")
print(f"    {'-'*30} | {'-'*10} | {'-'*14} | {'-'*7}")
print(f"    {'zeta (bare / S58 baseline)':30s} | {w_0_zeta:>10.6f} | {d_zeta:>14.6f} | {v_zeta}")
print(f"    {'Zubarev (E-weighted, CANONICAL)':30s} | {w_0_Zubarev:>10.6f} | {d_Zubarev:>14.6f} | {v_Zubarev}")
print(f"    {'Zubarev (flat, cross-check)':30s} | {w_0_Zubarev_flat:>10.6f} | {d_Zub_flat:>14.6f} | {v_Zub_flat}")

# Canonical verdict is from Zubarev E-weighted
canonical_verdict = v_Zubarev                                      # (local)
canonical_w_0     = w_0_Zubarev                                    # (local)

# Direction commentary
print(f"\n  DIRECTION ANALYSIS:")
print(f"    Zubarev suppresses GGE density by ~xi_Zub_E = {S_Zubarev_E/S_zeta_E:.4f}")
print(f"    rho_GGE_Zub = {rho_GGE_Zub:.6f} M_KK (vs {Lambda_eff:.3f} bare)")
print(f"    Since rho_J/cell = {rho_J_per_cell_s58:.3f} dominates over GGE,")
print(f"    and GGE is SUPPRESSED under Zubarev, w_0 is pushed CLOSER to -1.")
print(f"    This is expected: UV-regulated vacuum energy density is dominated by")
print(f"    the IR-robust Josephson ground state. Zubarev preserves Volovik partition.")

# =============================================================================
# Section 6. Plot
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 6: Plot results")
print("=" * 78)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Panel 1: w_0 per scheme with threshold band
schemes = ['zeta\n(S58 baseline)', 'Zubarev\n(E-weighted,\nCANONICAL)', 'Zubarev\n(flat\ncross-check)']
w0_vals = [w_0_zeta, w_0_Zubarev, w_0_Zubarev_flat]
verdicts = [v_zeta, v_Zubarev, v_Zub_flat]
colors = ['tab:gray', 'tab:blue', 'tab:cyan']

ax1.axhspan(w_0_target - PASS_tol, w_0_target + PASS_tol, alpha=0.3, color='green', label=f'PASS ({PASS_tol})')
ax1.axhspan(w_0_target - INFO_tol, w_0_target - PASS_tol, alpha=0.2, color='orange', label=f'INFO')
ax1.axhspan(w_0_target + PASS_tol, w_0_target + INFO_tol, alpha=0.2, color='orange')
ax1.axhline(w_0_target, color='k', linestyle='--', label=f'target = {w_0_target}')
ax1.axhline(-1.0, color='r', linestyle=':', label='LCDM w_0 = -1')
ax1.axhline(-0.752, color='tab:purple', linestyle=':', label='DESI DR2 w_0 = -0.752')

for i, (sch, w, v, c) in enumerate(zip(schemes, w0_vals, verdicts, colors)):
    ax1.bar(i, w, color=c, alpha=0.7, label=f'{sch.split(chr(10))[0]}: {v}' if i == 1 else None)
    ax1.annotate(f'{w:.4f}\n[{v}]', xy=(i, w), xytext=(0, 5), textcoords='offset points',
                 ha='center', fontweight='bold')

ax1.set_xticks(range(len(schemes)))
ax1.set_xticklabels(schemes, fontsize=9)
ax1.set_ylabel('w_0')
ax1.set_title('w_0 per regulator scheme\n(canonical R = Zubarev per W1-G1)')
ax1.set_ylim(-1.0, -0.70)
ax1.legend(fontsize=8, loc='lower right')
ax1.grid(True, alpha=0.3)

# Panel 2: Spectral weight suppression
ax2.scatter(flat_lambdas, flat_mults * w_zeta, s=2, alpha=0.3, label='zeta (uniform weight)', color='tab:gray')
ax2.scatter(flat_lambdas, flat_mults * w_zub,  s=2, alpha=0.5, label='Zubarev (Gaussian)', color='tab:blue')
ax2.set_xlabel('lam_n (M_KK units)')
ax2.set_ylabel('d_n * f_R(lam_n)')
ax2.set_yscale('log')
ax2.set_title(f'Spectral weight distribution at tau_fold = {tau_fold}\n(L_max = {L_max_w1g1})')
ax2.legend(fontsize=9)
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plot_path = SCRIPT_DIR / "s83_w3_g51_w0_regulator.png"
plt.savefig(plot_path, dpi=120, bbox_inches='tight')
plt.close()
print(f"\n  Plot saved: {plot_path}")

# =============================================================================
# Section 7. SHA-256 closure & save output
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 7: SHA-256 closure & save")
print("=" * 78)

# Closure SHA: canonical ordered input pin map
pin_map_ordered = json.dumps(pin_hashes, sort_keys=True).encode('utf-8')
closure_sha = hashlib.sha256(pin_map_ordered).hexdigest()
print(f"\n  closure_sha = {closure_sha}")

# Save NPZ
out_npz = SCRIPT_DIR / "s83_w3_g51_w0_regulator.npz"
np.savez(out_npz,
    # W1-G1 carry-forward
    R_canonical=R_canonical,
    S_zeta=S_zeta, S_Zubarev=S_Zubarev, S_SDW=S_SDW,
    S_zeta_E=S_zeta_E, S_Zubarev_E=S_Zubarev_E,
    xi_Zubarev=xi_Zubarev, xi_SDW=xi_SDW,
    xi_Zubarev_E=S_Zubarev_E/S_zeta_E,
    L_max=L_max_w1g1,
    # S58 baseline
    F_Josephson=F_Josephson,
    rho_J_per_cell=rho_J_per_cell_s58,
    Lambda_eff=Lambda_eff,
    w_GGE_bare=w_GGE_bare,
    P_GGE_bare=P_GGE_bare,
    E_GGE_bare=E_GGE_bare,
    w_0_zeta=w_0_zeta,
    w_0_S58_A=w0_A_s58,
    # GGE under Zubarev
    rho_GGE_Zub=rho_GGE_Zub,
    P_GGE_Zub=P_GGE_Zub,
    rho_GGE_Zub_flat=rho_GGE_Zub_flat,
    P_GGE_Zub_flat=P_GGE_Zub_flat,
    # Combined w_0 (primary: E-weighted Zubarev)
    w_0_Zubarev=w_0_Zubarev,
    w_0_Zubarev_flat=w_0_Zubarev_flat,
    # Verdicts
    v_zeta=v_zeta, v_Zubarev=v_Zubarev, v_Zub_flat=v_Zub_flat,
    d_zeta=d_zeta, d_Zubarev=d_Zubarev, d_Zub_flat=d_Zub_flat,
    w_0_target=w_0_target,
    PASS_tol=PASS_tol, INFO_tol=INFO_tol,
    # Canonical verdict
    canonical_w_0=canonical_w_0,
    canonical_verdict=canonical_verdict,
    closure_sha=closure_sha,
    pin_hashes=json.dumps(pin_hashes),
)
print(f"  NPZ saved: {out_npz}")

# =============================================================================
# Section 8. Final 4-tuple + verdict line
# =============================================================================
print("\n" + "=" * 78)
print("FINAL RESULT")
print("=" * 78)
print(f"\n  Canonical R: {R_canonical}")
print(f"  Canonical w_0 (Zubarev, E-weighted): {canonical_w_0:.6f}")
print(f"  |w_0 - (-0.918)| = {d_Zubarev:.6f}")
print(f"  VERDICT: {canonical_verdict}")

# Output 4-tuple tag (last non-verdict line)
four_tuple = f"value={canonical_w_0:.6f} scheme=Zubarev-E-weighted convention=substrate-native L_max={L_max_w1g1}"
print(f"\n  4-tuple: ({four_tuple})")

# Verdict line (to be appended to s83_gate_verdicts.txt)
verdict_line = (
    f"S83-W_0-REGULATOR-CANONICAL-CHOICE: {canonical_verdict} -- "
    f"value={canonical_w_0:.6f} scheme=Zubarev-E-weighted "
    f"convention=substrate-native L_max={L_max_w1g1} sha256={closure_sha}"
)
print(f"\n  VERDICT LINE:")
print(f"  {verdict_line}")
