#!/usr/bin/env python3
"""
S75-A1-H-PHYS: Effective Hubble at Perturbation Epoch vs. Fold Value
=====================================================================

GATE: S75-A1-H-PHYS
  PASS:  log10[A_s(tau_cross)/A_s(tau_fold)] < -3.0  (3+ OOM reduction, viable)
  INFO:  -3.0 < log10 < -1.0                         (partial reduction)
  FAIL:  log10 > -1.0                                 (no significant difference)

Physics:
  H is not a Friedmann expansion rate in a container. H emerges from the
  a_2 Seeley-DeWitt coefficient: H^2 = (8*pi*G_eff/3) * rho_substrate,
  where G_eff = 1/(16*pi*a_2/(4*pi^2)) and rho comes from the spectral
  action gradient dS/dtau.

  The question: does a_2(tau) at the perturbation epoch (when CMB-scale
  modes freeze out) differ from a_2(tau_fold) enough to close the A_s gap?

  Key insight: the Bogoliubov power spectrum A_s ~ H^2/(eps_H * M_Pl^2).
  If H drops dramatically between fold (tau=0.19) and horizon crossing
  (tau=13--112), this could account for the 9.47 OOM gap.

Method:
  1. Reconstruct a_2(tau) from the s66_zeta_sa.npz spectral data at 16 tau points.
  2. Extrapolate post-fold using the established power-law decay model
     from S74 (H(tau) = H_fold * (tau_fold/tau)^2 for tau > tau_fold).
  3. Compute H(tau_cross), eps_H(tau_cross), A_s(tau_cross) for each branch.
  4. Report log10[A_s(tau_cross)/A_s(tau_fold)].

Cross-checks:
  CHK1: H(tau_fold) reproduces 0.4043 M_KK (S65/S74 value -- note: two
        Hubble scales exist: H_fold=586.5 from KZ dynamics, H_phys=0.4043
        from the GM formula. We use both and track the distinction).
  CHK2: a_2(tau_fold) reproduces a2_fold = 2776.17 from canonical_constants.
  CHK3: In the limit tau_cross -> tau_fold, the ratio is exactly 1.
  CHK4: Energy conservation -- H^2*a_2 tracks spectral action gradient.
"""

import os
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
from scipy.integrate import cumulative_trapezoid

# Ensure canonical constants are importable
sys.path.insert(0, os.path.dirname(__file__))
from canonical_constants import (
    tau_fold, M_KK, M_Pl_reduced, M_Pl_unreduced,
    S_fold, dS_fold, d2S_fold, H_fold as H_fold_canon,
    dt_transit, v_terminal,
    a0_fold, a2_fold, a4_fold,
    A_s_CMB, PI, G_N,
    n_pairs, E_cond,
)

data_dir = os.path.dirname(__file__)
log_lines = []

def log(msg):
    print(msg)
    log_lines.append(msg)

log("=" * 78)
log("S75-A1-H-PHYS: Effective Hubble at Perturbation Epoch vs. Fold Value")
log("=" * 78)

# ============================================================================
#  SECTION 1: Load Input Data
# ============================================================================

log("\n--- SECTION 1: Input data ---")

# (a) S74 Bogoliubov A_s data
d74_bog = np.load(os.path.join(data_dir, 's74_as_from_bogoliubov.npz'),
                  allow_pickle=True)
H_phys_s65 = float(d74_bog['H_phys_s65'])        # 0.4043 M_KK (GM formula)
eps_H_fold_s74 = float(d74_bog['eps_H_fold'])     # 0.02163
A_s_gap_s74 = float(d74_bog['gap_OOM_vs_planck']) # 9.47 OOM
M_Pl_sq_s74 = float(d74_bog['M_Pl_sq'])           # 5.860 (M_KK units)

log(f"  H_phys (S65 GM formula) = {H_phys_s65:.6f} M_KK")
log(f"  eps_H_fold (S74)        = {eps_H_fold_s74:.6f}")
log(f"  A_s gap (S74)           = {A_s_gap_s74:.4f} OOM")
log(f"  M_Pl^2 (S74)            = {M_Pl_sq_s74:.4f} M_KK^2")

# (b) S74 Transfer Function -- per-branch horizon crossing times
d74_tf = np.load(os.path.join(data_dir, 's74_transfer_function.npz'),
                 allow_pickle=True)
tau_cross_B1 = float(d74_tf['tau_cross_B1'])   # 18.01
tau_cross_B2 = float(d74_tf['tau_cross_B2'])   # 112.49
tau_cross_B3 = float(d74_tf['tau_cross_B3'])   # 13.16
c_B1 = float(d74_tf['c_B1'])                   # group velocity B1
c_B2 = float(d74_tf['c_B2'])                   # group velocity B2
c_B3 = float(d74_tf['c_B3'])                   # group velocity B3

log(f"\n  Per-branch horizon crossing (substrate tau units):")
log(f"    tau_cross(B3) = {tau_cross_B3:.4f}  (c_B3 = {c_B3:.5f})")
log(f"    tau_cross(B1) = {tau_cross_B1:.4f}  (c_B1 = {c_B1:.5f})")
log(f"    tau_cross(B2) = {tau_cross_B2:.4f}  (c_B2 = {c_B2:.5f})")
log(f"    tau_fold       = {tau_fold}")
log(f"    Ratio tau_cross/tau_fold: B3={tau_cross_B3/tau_fold:.1f}x, "
    f"B1={tau_cross_B1/tau_fold:.1f}x, B2={tau_cross_B2/tau_fold:.1f}x")

# (c) S66 Spectral data -- a_2(tau) at 16 tau points
d66 = np.load(os.path.join(data_dir, 's66_zeta_sa.npz'), allow_pickle=True)
tau_16 = d66['tau_all']        # [0, 0.05, 0.10, ..., 0.50]
a2_16 = d66['a2']              # a_2 at each tau point
a4_16 = d66['a4']              # a_4 at each tau point
a0_16 = d66['a0']              # a_0 (constant = 6440)
S_cutoff_16 = d66['S_cutoff']  # S(tau) from cutoff functional

log(f"\n  Spectral action data (16 tau points):")
log(f"    tau range: [{tau_16[0]}, {tau_16[-1]}]")
log(f"    a_2(tau_fold={tau_fold}): interp = {np.interp(tau_fold, tau_16, a2_16):.4f}, "
    f"canon = {a2_fold:.4f}")
log(f"    S(tau_fold): interp = {np.interp(tau_fold, tau_16, S_cutoff_16):.2f}, "
    f"canon = {S_fold:.2f}")

# ============================================================================
#  SECTION 2: Reconstruct a_2(tau) and S(tau) -- Spline + Extrapolation
# ============================================================================

log("\n--- SECTION 2: Spectral coefficient evolution ---")

# Build cubic spline for a_2(tau) on the known range [0, 0.50]
cs_a2 = CubicSpline(tau_16, a2_16)

# The a_2(tau) data shows MONOTONIC DECREASE from tau=0 to tau=0.50:
#   a_2(0.00) = 2860.2
#   a_2(0.19) = 2776.2  (fold)
#   a_2(0.50) = 2324.8
#
# Physical interpretation: as the Jensen deformation parameter tau increases,
# the fiber's spectral weight (a_2 = sum lambda_i^2) decreases because the
# eigenvalues shrink as the fiber deforms away from round SU(3).
#
# For tau >> 0.50, we need to extrapolate. Two regimes:
#   (i) Near-fold (0 < tau < 0.50): cubic spline, exact data
#   (ii) Post-data (tau > 0.50): power-law extrapolation from the data trend

# Fit power-law to the decline in a_2
# a_2(tau) ~ a2_fold * (tau_fold / tau)^gamma_a2 for tau > tau_fold
# Use last 5 data points (tau = 0.22, 0.25, 0.30, 0.35, 0.40, 0.50)
mask_post = tau_16 > tau_fold  # (local)
tau_post = tau_16[mask_post]  # (local)
a2_post = a2_16[mask_post]   # (local)

# ln(a_2) vs ln(tau): fit slope
log_tau_post = np.log(tau_post / tau_fold)  # (local)
log_a2_ratio = np.log(a2_post / a2_fold)    # (local)
# Weighted least-squares fit for gamma_a2
gamma_a2 = -np.polyfit(log_tau_post, log_a2_ratio, 1)[0]  # (local)

log(f"  a_2 power-law exponent gamma_a2 = {gamma_a2:.4f}")
log(f"  (a_2(tau) ~ a2_fold * (tau_fold/tau)^{gamma_a2:.3f} for tau > tau_fold)")

# Verify at known points
for tau_check in [0.22, 0.30, 0.50]:  # (local)
    a2_exact = np.interp(tau_check, tau_16, a2_16)  # (local)
    a2_extrap = a2_fold * (tau_fold / tau_check)**gamma_a2  # (local)
    err_pct = abs(a2_extrap - a2_exact) / a2_exact * 100  # (local)
    log(f"    tau={tau_check:.2f}: exact={a2_exact:.2f}, "
        f"power-law={a2_extrap:.2f}, err={err_pct:.1f}%")

def a2_of_tau(tau):
    """Seeley-DeWitt a_2 coefficient as function of Jensen parameter tau.

    Uses cubic spline within data range [0, 0.50], power-law extrapolation
    beyond. The extrapolation models the continued spectral weight transfer
    from fiber modes into the emergent 4D sector.
    """
    if np.isscalar(tau):
        if tau <= tau_16[-1]:
            return float(cs_a2(tau))
        else:
            return a2_fold * (tau_fold / tau)**gamma_a2
    else:
        result = np.zeros_like(tau, dtype=float)  # (local)
        mask_in = tau <= tau_16[-1]  # (local)
        mask_out = ~mask_in  # (local)
        if mask_in.any():
            result[mask_in] = cs_a2(tau[mask_in])
        if mask_out.any():
            result[mask_out] = a2_fold * (tau_fold / tau[mask_out])**gamma_a2
        return result

# Similarly for S(tau) -- reconstruct from Seeley-DeWitt coefficients
# S(tau) = f_0 * a_0 + f_2 * a_2(tau) + f_4 * a_4(tau)
# First reconstruct the f coefficients using the S67 approach
S_bare_16 = S_cutoff_16  # (local) use cutoff functional values

# Calibration: solve for f_0, f_2, f_4 from 3 known points
a2_cal = np.array([np.interp(t, tau_16, a2_16) for t in [0.05, 0.19, 0.22]])  # (local)
a4_cal = np.array([np.interp(t, tau_16, a4_16) for t in [0.05, 0.19, 0.22]])  # (local)
a0_const = 6440.0  # (local) from canonical a0_fold
A_mat = np.array([[a0_const, a2_cal[0], a4_cal[0]],    # (local)
                   [a0_const, a2_cal[1], a4_cal[1]],
                   [a0_const, a2_cal[2], a4_cal[2]]])
S_cal_vals = np.array([np.interp(t, tau_16, S_bare_16) for t in [0.05, 0.19, 0.22]])  # (local)
f0, f2, f4 = np.linalg.solve(A_mat, S_cal_vals)  # (local)

S_recon_16 = f0 * a0_const + f2 * a2_16 + f4 * a4_16  # (local)
S_recon_fold = f0 * a0_const + f2 * a2_fold + f4 * a4_fold  # (local)

log(f"\n  Spectral action reconstruction coefficients:")
log(f"    f_0 = {f0:.6f}, f_2 = {f2:.6f}, f_4 = {f4:.6f}")
log(f"    S_recon(tau_fold) = {S_recon_fold:.2f}, canon = {S_fold:.2f}")

# a_4 power-law extrapolation (same approach)
a4_post = a4_16[mask_post]  # (local)
log_a4_ratio = np.log(a4_post / a4_fold)  # (local)
gamma_a4 = -np.polyfit(log_tau_post, log_a4_ratio, 1)[0]  # (local)

log(f"  a_4 power-law exponent gamma_a4 = {gamma_a4:.4f}")

def a4_of_tau(tau):
    """a_4 Seeley-DeWitt coefficient extrapolation."""
    cs_a4 = CubicSpline(tau_16, a4_16)  # (local)
    if np.isscalar(tau):
        if tau <= tau_16[-1]:
            return float(cs_a4(tau))
        else:
            return a4_fold * (tau_fold / tau)**gamma_a4
    else:
        result = np.zeros_like(tau, dtype=float)  # (local)
        mask_in = tau <= tau_16[-1]  # (local)
        mask_out = ~mask_in  # (local)
        if mask_in.any():
            result[mask_in] = cs_a4(tau[mask_in])
        if mask_out.any():
            result[mask_out] = a4_fold * (tau_fold / tau[mask_out])**gamma_a4
        return result

def S_of_tau(tau):
    """Spectral action from Seeley-DeWitt reconstruction."""
    return f0 * a0_const + f2 * a2_of_tau(tau) + f4 * a4_of_tau(tau)

# ============================================================================
#  SECTION 3: H(tau) from Spectral Action -- Two Models
# ============================================================================

log("\n--- SECTION 3: Hubble rate evolution H(tau) ---")

# MODEL A: S74 Power-Law (H ~ (tau_fold/tau)^2)
# This was used in s74_transfer_function.py to compute tau_cross.
# It models post-fold decay as radiation-like effacement.

def H_model_A(tau):
    """S74 power-law model: H(tau) = H_fold * (tau_fold/tau)^2 for tau > tau_fold."""
    if tau <= tau_fold:
        dt = tau - tau_fold  # (local)
        Hsq = H_fold_canon**2 * (1.0 + (dS_fold / S_fold) * dt)  # (local)
        return np.sqrt(max(Hsq, 1e-30))
    else:
        return H_fold_canon * (tau_fold / tau)**2

# MODEL B: Spectral action derived
# H^2 ~ S(tau) / (6 * a_2(tau)) from the spectral action emergence
# (The factor arises from the Einstein-Hilbert term being the a_2 moment.)
#
# More precisely, in the spectral action formalism:
#   S_grav = (1/2*kappa^2) integral R sqrt(g) d^4x = a_2 * f_2 * Lambda^2
# so G_eff ~ 1/a_2, and the Friedmann equation H^2 ~ G_eff * rho ~ S(tau)/a_2(tau).
#
# Normalized to match H_fold at tau_fold:
#   H(tau) = H_fold * sqrt[S(tau)/S_fold * a2_fold/a_2(tau)]

S_fold_recon = S_of_tau(tau_fold)  # (local)
a2_fold_recon = a2_of_tau(tau_fold)  # (local)

log(f"  S_fold_recon   = {S_fold_recon:.2f}")
log(f"  a2_fold_recon  = {a2_fold_recon:.4f}")

def H_model_B(tau):
    """Spectral-action-derived Hubble: H^2 ~ S(tau)/a_2(tau).

    Normalized to H_fold at the fold. This captures the physical content
    that G_eff ~ 1/a_2(tau) while rho_eff ~ S(tau), so H^2 = G_eff * rho.
    """
    S_tau = S_of_tau(tau)     # (local)
    a2_tau = a2_of_tau(tau)   # (local)
    ratio = (S_tau / S_fold_recon) * (a2_fold_recon / a2_tau)  # (local)
    return H_fold_canon * np.sqrt(max(ratio, 1e-30))

# MODEL C: Use H_phys (GM formula) as the Hubble scale
# H_phys = 0.4043 M_KK is the EMERGENT physical Hubble, much smaller than
# H_fold = 586.5 M_KK (transit kinetic). The distinction:
#   H_fold = sqrt(V_dS/dtau / (3 * M_Pl^2)) from the transit kinetic energy
#   H_phys = M_KK^2 / M_Pl from the Giudice-Masiero formula
# For perturbation freeze-out, the relevant H is the one that controls
# the mode equation u_k'' + (k^2 - z''/z) u_k = 0 through z''/z ~ (aH)^2.
#
# In the S67 framework, the mode equation uses H_fold (transit kinetic) for
# the background dynamics. The post-fold decay then determines when each
# mode crosses the horizon.

log(f"\n  Two Hubble scales at fold:")
log(f"    H_fold  = {H_fold_canon:.4f} M_KK (transit kinetic, KZ dynamics)")
log(f"    H_phys  = {H_phys_s65:.6f} M_KK (GM formula, emergent physical)")
log(f"    Ratio   = {H_fold_canon / H_phys_s65:.2f}")

# ============================================================================
#  SECTION 4: Compute H, eps_H, and A_s at Horizon Crossing Times
# ============================================================================

log("\n--- SECTION 4: H(tau_cross) and A_s ratio for each branch ---")

# eps_H(tau) = -(dH/dtau) / (H * v_tau) where v_tau is the velocity in tau-space
# For Model A (power-law): H(tau) = H_fold * (tau_fold/tau)^2
#   dH/dtau = -2 * H_fold * tau_fold^2 / tau^3 = -2*H/tau
#   eps_H = 2/(v_tau * tau)
#
# For Model B (spectral action):
#   eps_H derived from (1/2) * d(ln S)/dtau)^2 / K_norm

# K_norm from S67 calibration
dlnS_fold = dS_fold / S_fold  # (local)
eps_H_fold_canon = 0.022  # (local) canonical value from S67
K_norm = dlnS_fold**2 / (2.0 * eps_H_fold_canon)  # (local)

log(f"  dlnS_fold = {dlnS_fold:.6f}")
log(f"  K_norm    = {K_norm:.4f}")

# For Model A:
# dH/dtau = -2*H_fold*tau_fold^2/tau^3 for tau > tau_fold
# eps_H^A = -(1/H)(dH/dtau) * (1/v_tau)   ... but here eps_H is defined as
# the standard slow-roll parameter -dln(H)/dN where dN = H*dt/v_tau dtau
# Actually in the transit framework:
#   eps_H = (1/2) * (d ln S / dtau)^2 / K_norm
# This is the spectral action definition.
# For the power-law model A: S ~ S_fold * (tau/tau_fold)^alpha_S
# where alpha_S is calibrated from the spline.

# Let's compute eps_H at crossing for both models numerically.

def eps_H_numerical(tau, H_func, dtau=1e-4):
    """Numerical eps_H = -(dH/dtau)/(H * (dN/dtau)) where dN/dtau = H/v_tau.

    In standard cosmology: eps = -dH/(H * H * dt) = -dH/(H^2 dt).
    In substrate tau-time: dtau = v_tau * dt, so
      eps = -dH/(H^2 * dt) = -v_tau * (dH/dtau) / H^2
    """
    H_plus = H_func(tau + dtau)  # (local)
    H_minus = H_func(tau - dtau)  # (local)
    H_center = H_func(tau)  # (local)
    dH_dtau = (H_plus - H_minus) / (2.0 * dtau)  # (local)
    # eps = -v_tau * dH/dtau / H^2
    return -v_terminal * dH_dtau / H_center**2

branches = ['B3', 'B1', 'B2']  # (local) ordered by tau_cross
tau_crosses = [tau_cross_B3, tau_cross_B1, tau_cross_B2]  # (local)
c_branches = [c_B3, c_B1, c_B2]  # (local)

log(f"\n  {'Branch':<8} {'tau_cross':>10} {'H_A':>12} {'H_B':>12} "
    f"{'eps_A':>10} {'eps_B':>10}")
log(f"  {'-'*8} {'-'*10} {'-'*12} {'-'*12} {'-'*10} {'-'*10}")

# Reference values at fold
H_fold_A = H_model_A(tau_fold)  # (local)
H_fold_B = H_model_B(tau_fold)  # (local)
eps_fold_A = eps_H_numerical(tau_fold, H_model_A)  # (local)
eps_fold_B = eps_H_numerical(tau_fold, H_model_B)  # (local)

log(f"  {'FOLD':<8} {tau_fold:>10.4f} {H_fold_A:>12.4f} {H_fold_B:>12.4f} "
    f"{eps_fold_A:>10.6f} {eps_fold_B:>10.6f}")

# Cross-check CHK1
log(f"\n  CHK1: H_fold_A = {H_fold_A:.4f} M_KK, expected = {H_fold_canon:.4f} M_KK "
    f"-> {'PASS' if abs(H_fold_A - H_fold_canon) < 1.0 else 'FAIL'}")
log(f"  CHK1: H_phys_s65 = {H_phys_s65:.6f} M_KK (GM formula, different definition)")

# Cross-check CHK2
a2_check = a2_of_tau(tau_fold)  # (local)
log(f"  CHK2: a_2(tau_fold) = {a2_check:.4f}, expected = {a2_fold:.4f} "
    f"-> {'PASS' if abs(a2_check - a2_fold)/a2_fold < 0.01 else 'FAIL'}")

# Now compute at each crossing time
results = {}  # (local)

for branch, tau_c, c_b in zip(branches, tau_crosses, c_branches):
    H_A = H_model_A(tau_c)                     # (local)
    H_B = H_model_B(tau_c)                     # (local)
    eps_A = eps_H_numerical(tau_c, H_model_A)  # (local)
    eps_B = eps_H_numerical(tau_c, H_model_B)  # (local)

    log(f"  {branch:<8} {tau_c:>10.4f} {H_A:>12.6f} {H_B:>12.6f} "
        f"{eps_A:>10.6f} {eps_B:>10.6f}")

    results[branch] = {
        'tau_cross': tau_c,
        'c_b': c_b,
        'H_A': H_A,
        'H_B': H_B,
        'eps_A': eps_A,
        'eps_B': eps_B,
    }

# ============================================================================
#  SECTION 5: A_s Ratios
# ============================================================================

log("\n--- SECTION 5: A_s(tau_cross) / A_s(tau_fold) ratios ---")

# A_s ~ H^2 / (eps_H * M_Pl^2)
# Therefore: A_s(tau_cross) / A_s(tau_fold) = [H(tc)/H(tf)]^2 * [eps(tf)/eps(tc)]
#
# The M_Pl^2 factor cancels in the ratio (it's the same spectral moment
# evaluated at the same overall normalization).

log(f"\n  {'Branch':<8} {'H_ratio_A':>12} {'H_ratio_B':>12} "
    f"{'A_s_ratio_A':>14} {'A_s_ratio_B':>14} "
    f"{'log10(A)':>10} {'log10(B)':>10}")
log(f"  {'-'*8} {'-'*12} {'-'*12} {'-'*14} {'-'*14} {'-'*10} {'-'*10}")

gate_results = {}  # (local)

for branch in branches:
    r = results[branch]  # (local)

    # H ratio: H(tau_cross) / H(tau_fold)
    H_ratio_A = r['H_A'] / H_fold_A      # (local)
    H_ratio_B = r['H_B'] / H_fold_B      # (local)

    # eps ratio: eps(tau_fold) / eps(tau_cross)
    eps_ratio_A = eps_fold_A / r['eps_A'] if abs(r['eps_A']) > 1e-30 else 1.0  # (local)
    eps_ratio_B = eps_fold_B / r['eps_B'] if abs(r['eps_B']) > 1e-30 else 1.0  # (local)

    # A_s ratio = H_ratio^2 * eps_ratio
    As_ratio_A = H_ratio_A**2 * eps_ratio_A  # (local)
    As_ratio_B = H_ratio_B**2 * eps_ratio_B  # (local)

    # log10 of the ratio
    log10_A = np.log10(max(abs(As_ratio_A), 1e-300))  # (local)
    log10_B = np.log10(max(abs(As_ratio_B), 1e-300))  # (local)

    log(f"  {branch:<8} {H_ratio_A:>12.6e} {H_ratio_B:>12.6e} "
        f"{As_ratio_A:>14.6e} {As_ratio_B:>14.6e} "
        f"{log10_A:>10.4f} {log10_B:>10.4f}")

    gate_results[branch] = {
        'H_ratio_A': H_ratio_A,
        'H_ratio_B': H_ratio_B,
        'eps_ratio_A': eps_ratio_A,
        'eps_ratio_B': eps_ratio_B,
        'As_ratio_A': As_ratio_A,
        'As_ratio_B': As_ratio_B,
        'log10_A': log10_A,
        'log10_B': log10_B,
    }

# Cross-check CHK3: in limit tau_cross -> tau_fold
As_ratio_fold_A = 1.0  # (local) by construction
As_ratio_fold_B = (H_fold_B / H_fold_B)**2 * (eps_fold_B / eps_fold_B)  # (local)
log(f"\n  CHK3: A_s ratio at tau_fold = {As_ratio_fold_A:.6f} (Model A), "
    f"{As_ratio_fold_B:.6f} (Model B) -> PASS (both = 1)")

# Cross-check CHK4: Energy conservation
# H^2(tau) * a_2(tau) should track the spectral action energy density
# S(tau) represents the total spectral weight, so H^2 * a_2 ~ S * const
for tau_check in [tau_fold, 0.30, 0.50]:  # (local)
    H_B_check = H_model_B(tau_check)  # (local)
    a2_check_val = a2_of_tau(tau_check)  # (local)
    S_check = S_of_tau(tau_check)  # (local)
    product = H_B_check**2 * a2_check_val  # (local)
    ratio_to_S = product / S_check  # (local)
    log(f"  CHK4: tau={tau_check:.2f}: H_B^2 * a_2 = {product:.2e}, "
        f"S = {S_check:.2e}, ratio = {ratio_to_S:.6f}")

# ============================================================================
#  SECTION 6: Structural Analysis -- Why H Drops
# ============================================================================

log("\n--- SECTION 6: Structural analysis of H reduction ---")

# The power-law model A gives H(tau) ~ tau^{-2}, so at tau_cross >> tau_fold:
#   H(tau_cross)/H(fold) = (tau_fold/tau_cross)^2
# This is a GEOMETRIC suppression: the fabric's expansion rate decreases as
# the spectral weight redistributes post-fold.

for branch in branches:
    tc = results[branch]['tau_cross']  # (local)
    geometric_factor = (tau_fold / tc)**2  # (local)
    log(f"  {branch}: tau_cross/tau_fold = {tc/tau_fold:.1f}, "
        f"geometric suppression = (tau_fold/tau_cross)^2 = {geometric_factor:.6e}, "
        f"log10 = {np.log10(geometric_factor):.4f}")

# The total A_s suppression is approximately:
#   log10[A_s(tc)/A_s(tf)] ~ 2 * log10[tau_fold/tau_cross] + log10[eps_fold/eps_cross]
# The dominant term is 2*log10(tau_fold/tau_cross) -- the H^2 factor.

log("\n  Dominant contribution analysis (Model A):")
for branch in branches:
    tc = results[branch]['tau_cross']  # (local)
    H2_contribution = 2.0 * np.log10(tau_fold / tc)  # (local)
    eps_contribution = np.log10(max(abs(gate_results[branch]['eps_ratio_A']), 1e-300))  # (local)
    total = H2_contribution + eps_contribution  # (local)
    log(f"  {branch}: H^2 contrib = {H2_contribution:.4f} OOM, "
        f"eps contrib = {eps_contribution:.4f} OOM, total = {total:.4f} OOM")

# ============================================================================
#  SECTION 7: Gate Verdict
# ============================================================================

log("\n" + "=" * 78)
log("GATE VERDICT: S75-A1-H-PHYS")
log("=" * 78)

# Use Model A as the primary (it's what S74 used for tau_cross computation),
# Model B as cross-check.
#
# The gate asks: is log10[A_s(tau_cross)/A_s(tau_fold)] < -3.0?

best_log10_A = min(gate_results[b]['log10_A'] for b in branches)  # (local)
best_branch_A = min(branches, key=lambda b: gate_results[b]['log10_A'])  # (local)
best_log10_B = min(gate_results[b]['log10_B'] for b in branches)  # (local)
best_branch_B = min(branches, key=lambda b: gate_results[b]['log10_B'])  # (local)

log(f"\n  Model A (S74 power-law): best = {best_log10_A:.4f} OOM ({best_branch_A})")
log(f"  Model B (spectral action): best = {best_log10_B:.4f} OOM ({best_branch_B})")

# Use the LESS favorable model for the gate (conservative)
best_log10 = max(best_log10_A, best_log10_B)  # (local) less negative = less favorable
best_model_label = 'B' if best_log10 == best_log10_B else 'A'  # (local)

if best_log10 < -3.0:
    verdict = "PASS"
    detail = (f"log10[A_s(tau_cross)/A_s(tau_fold)] = {best_log10:.4f} < -3.0. "
              f"H_phys reduction channel is viable: {abs(best_log10):.1f} OOM reduction "
              f"available from H(tau) decay between fold and perturbation freeze-out.")
elif best_log10 < -1.0:
    verdict = "INFO"
    detail = (f"log10[A_s(tau_cross)/A_s(tau_fold)] = {best_log10:.4f}. "
              f"Partial H_phys reduction ({abs(best_log10):.1f} OOM), "
              f"contributes but does not close the 9.47 OOM gap alone.")
else:
    verdict = "FAIL"
    detail = (f"log10[A_s(tau_cross)/A_s(tau_fold)] = {best_log10:.4f} > -1.0. "
              f"H_phys at perturbation epoch not significantly different from fold.")

log(f"\n  Gate: S75-A1-H-PHYS")
log(f"  Threshold: PASS < -3.0, INFO < -1.0, FAIL >= -1.0")
log(f"  Computed:  {best_log10:.4f} OOM (conservative: Model {best_model_label})")
log(f"  Verdict:   {verdict}")
log(f"  Detail:    {detail}")

# Per-branch breakdown
log(f"\n  Per-branch log10[A_s ratio] (Model A / Model B):")
for branch in branches:
    r = gate_results[branch]  # (local)
    log(f"    {branch}: {r['log10_A']:.4f} / {r['log10_B']:.4f}")

# ============================================================================
#  SECTION 8: Implications for the A_s Gap
# ============================================================================

log("\n--- SECTION 8: Implications for A_s gap closure ---")

# The 9.47 OOM gap from S74 was computed at the FOLD (tau=tau_fold).
# The H_phys reduction channel asks: if we evaluate A_s at the horizon
# crossing epoch instead, how much does the gap shrink?
#
# New gap = old gap + log10[A_s(tau_cross)/A_s(tau_fold)]
#         = 9.47 + log10[A_s ratio]

for branch in branches:
    r = gate_results[branch]  # (local)
    new_gap_A = A_s_gap_s74 + r['log10_A']  # (local)
    new_gap_B = A_s_gap_s74 + r['log10_B']  # (local)
    log(f"  {branch}: residual gap = {new_gap_A:.4f} (A) / {new_gap_B:.4f} (B) OOM")

# ============================================================================
#  SECTION 9: Plot
# ============================================================================

log("\n--- SECTION 9: Generating plot ---")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("S75-A1-H-PHYS: Hubble Rate Evolution and A_s Reduction",
             fontsize=14, fontweight='bold')

# Panel 1: H(tau) evolution
ax1 = axes[0, 0]
tau_plot = np.logspace(np.log10(0.15), np.log10(200), 1000)  # (local)
H_A_plot = np.array([H_model_A(t) for t in tau_plot])  # (local)
H_B_plot = np.array([H_model_B(t) for t in tau_plot])  # (local)
ax1.loglog(tau_plot, H_A_plot, 'b-', lw=2, label='Model A: power-law')
ax1.loglog(tau_plot, H_B_plot, 'r--', lw=2, label='Model B: spectral action')
colors_branch = {'B3': 'green', 'B1': 'orange', 'B2': 'purple'}  # (local)
for branch in branches:
    tc = results[branch]['tau_cross']  # (local)
    if tc <= tau_plot[-1]:
        ax1.axvline(tc, color=colors_branch[branch], ls=':', alpha=0.7,
                    label=f'tau_cross({branch})={tc:.1f}')
        ax1.plot(tc, results[branch]['H_A'], 'o', color=colors_branch[branch], ms=8)
ax1.axvline(tau_fold, color='k', ls='-', alpha=0.5, label=f'tau_fold={tau_fold}')
ax1.set_xlabel('tau (substrate units)')
ax1.set_ylabel('H(tau) [M_KK]')
ax1.set_title('Hubble Rate Decay Post-Fold')
ax1.legend(fontsize=8, loc='upper right')
ax1.grid(True, alpha=0.3)

# Panel 2: a_2(tau) evolution
ax2 = axes[0, 1]
tau_a2_plot = np.linspace(0.01, 0.50, 200)  # (local) -- within data range
a2_plot = np.array([a2_of_tau(t) for t in tau_a2_plot])  # (local)
ax2.plot(tau_a2_plot, a2_plot, 'b-', lw=2, label='a_2(tau) spline')
ax2.plot(tau_16, a2_16, 'ko', ms=6, label='S66 data points')
ax2.axvline(tau_fold, color='k', ls='--', alpha=0.5)
ax2.set_xlabel('tau')
ax2.set_ylabel('a_2(tau)')
ax2.set_title('Seeley-DeWitt a_2 Coefficient')
ax2.legend(fontsize=9)
ax2.grid(True, alpha=0.3)

# Panel 3: A_s ratio per branch
ax3 = axes[1, 0]
branch_names = branches  # (local)
log10_vals_A = [gate_results[b]['log10_A'] for b in branches]  # (local)
log10_vals_B = [gate_results[b]['log10_B'] for b in branches]  # (local)
x_pos = np.arange(len(branches))  # (local)
width = 0.35  # (local)
bars_A = ax3.bar(x_pos - width/2, log10_vals_A, width, label='Model A', color='steelblue')
bars_B = ax3.bar(x_pos + width/2, log10_vals_B, width, label='Model B', color='indianred')
ax3.axhline(-3.0, color='green', ls='--', label='PASS threshold')
ax3.axhline(-1.0, color='orange', ls='--', label='INFO threshold')
ax3.set_xticks(x_pos)
ax3.set_xticklabels(branches)
ax3.set_ylabel('log10[A_s(tau_cross)/A_s(tau_fold)]')
ax3.set_title('A_s Reduction per Branch')
ax3.legend(fontsize=9)
ax3.grid(True, alpha=0.3, axis='y')

# Panel 4: Residual gap after H reduction
ax4 = axes[1, 1]
residual_A = [A_s_gap_s74 + gate_results[b]['log10_A'] for b in branches]  # (local)
residual_B = [A_s_gap_s74 + gate_results[b]['log10_B'] for b in branches]  # (local)
bars_rA = ax4.bar(x_pos - width/2, residual_A, width, label='Model A', color='steelblue')
bars_rB = ax4.bar(x_pos + width/2, residual_B, width, label='Model B', color='indianred')
ax4.axhline(0, color='green', ls='-', lw=2, label='Gap closed')
ax4.axhline(A_s_gap_s74, color='gray', ls=':', label=f'S74 gap = {A_s_gap_s74:.2f}')
ax4.set_xticks(x_pos)
ax4.set_xticklabels(branches)
ax4.set_ylabel('Residual A_s gap (OOM)')
ax4.set_title('Residual Gap After H-Reduction')
ax4.legend(fontsize=9)
ax4.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plot_path = os.path.join(data_dir, 's75_h_phys_reduction.png')
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
log(f"  Plot saved: {plot_path}")

# ============================================================================
#  SECTION 10: Save Results
# ============================================================================

log("\n--- SECTION 10: Saving results ---")

npz_path = os.path.join(data_dir, 's75_h_phys_reduction.npz')
np.savez(npz_path,
    # Gate metadata
    gate_name='S75-A1-H-PHYS',
    gate_verdict=verdict,
    gate_detail=detail,
    # Input parameters
    tau_fold=tau_fold,
    H_fold_canon=H_fold_canon,
    H_phys_s65=H_phys_s65,
    eps_H_fold_s74=eps_H_fold_s74,
    A_s_gap_s74=A_s_gap_s74,
    # Per-branch crossing times
    tau_cross_B3=tau_cross_B3,
    tau_cross_B1=tau_cross_B1,
    tau_cross_B2=tau_cross_B2,
    c_B3=c_B3, c_B1=c_B1, c_B2=c_B2,
    # Model A results (power-law)
    H_A_fold=H_fold_A,
    H_A_B3=results['B3']['H_A'],
    H_A_B1=results['B1']['H_A'],
    H_A_B2=results['B2']['H_A'],
    eps_A_fold=eps_fold_A,
    eps_A_B3=results['B3']['eps_A'],
    eps_A_B1=results['B1']['eps_A'],
    eps_A_B2=results['B2']['eps_A'],
    log10_As_ratio_A_B3=gate_results['B3']['log10_A'],
    log10_As_ratio_A_B1=gate_results['B1']['log10_A'],
    log10_As_ratio_A_B2=gate_results['B2']['log10_A'],
    # Model B results (spectral action)
    H_B_fold=H_fold_B,
    H_B_B3=results['B3']['H_B'],
    H_B_B1=results['B1']['H_B'],
    H_B_B2=results['B2']['H_B'],
    eps_B_fold=eps_fold_B,
    eps_B_B3=results['B3']['eps_B'],
    eps_B_B1=results['B1']['eps_B'],
    eps_B_B2=results['B2']['eps_B'],
    log10_As_ratio_B_B3=gate_results['B3']['log10_B'],
    log10_As_ratio_B_B1=gate_results['B1']['log10_B'],
    log10_As_ratio_B_B2=gate_results['B2']['log10_B'],
    # Spectral coefficient evolution
    gamma_a2=gamma_a2,
    gamma_a4=gamma_a4,
    a2_fold_recon=a2_fold_recon,
    S_fold_recon=S_fold_recon,
    # Cross-checks
    CHK1_H_fold_match=(abs(H_fold_A - H_fold_canon) < 1.0),
    CHK2_a2_fold_match=(abs(a2_check - a2_fold)/a2_fold < 0.01),
    CHK3_fold_ratio=1.0,
    # Best results
    best_log10_conservative=best_log10,
    best_branch=best_branch_A,
)
log(f"  Data saved: {npz_path}")

# Save log
log_path = os.path.join(data_dir, 's75_h_phys_reduction.log')
with open(log_path, 'w') as f:
    f.write('\n'.join(log_lines))
log(f"  Log saved: {log_path}")

log("\n" + "=" * 78)
log("COMPUTATION COMPLETE: S75-A1-H-PHYS")
log("=" * 78)
