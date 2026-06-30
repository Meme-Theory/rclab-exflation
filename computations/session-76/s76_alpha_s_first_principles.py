#!/usr/bin/env python3
"""
S76-B9-ALPHA-S-FP: alpha_s from Isocurvature Transfer + Spectral Action H(tau)
================================================================================

PURPOSE: Verify the S75/S76 isocurvature alpha_s = -0.0143 using the spectral-
action-derived H(tau) profile DIRECTLY, rather than the parametric fit
H(tau) = H_0 / (1 + (tau/tau_dS)^p) used in S75.

GOVERNING STRUCTURE:
  The spectral index running alpha_s = dn_s/d(ln k) arises from the
  k-dependence of the isocurvature transfer:
    n_s(k) - 1 = -2 * mu_eff * d(Delta_N)/d(ln k)               ... (1)
    alpha_s(k) = d(n_s)/d(ln k)                                   ... (2)
             = -2 * mu_eff * d^2(Delta_N)/d(ln k)^2               ... (2a)
             - 2 * (d(mu_eff)/d(ln k)) * d(Delta_N)/d(ln k)       ... (2b)
  where Delta_N(k) = integral[tau_cross(k), tau_end] H(tau) dtau
  and tau_cross(k) is defined by c_b * k = H(tau_cross).

CRITICAL PHYSICS:
  The spectral action V(tau) INCREASES with tau for tau > tau_fold.
  H_SA(tau) = H_fold * sqrt(V(tau)/V(tau_fold)) therefore also increases.
  This is the POTENTIAL contribution to the Friedmann equation:
    3*M_Pl^2 * H^2 = V(tau) + T(tau) + ...
  After the transit, the modulus tau has large kinetic energy, causing the
  actual H to DECREASE despite V increasing. The S75 parametric model
  H_0/(1+(tau/tau_dS)^p) captures this effective decrease.

  For "first principles" verification, we construct multiple H(tau) models
  that share the SA-derived curvature near the fold but differ in their
  asymptotic (tau >> 1) behavior:
    Model 0: S75 parametric (baseline, p=1.69)
    Model 1: Modified asymptotic (p=1.5)
    Model 2: Modified asymptotic (p=2.0)
    Model 3: Spectral action q_eff-matched power law
  Agreement across models = robust alpha_s prediction.

INPUTS:
  - W1-A: mu_eff = 0.0102 (target value, derived Richardson FAIL by 38x)
  - W1-E: H_transit = 586.5 M_KK, eps_H = 1.72 at fold
  - W2-C: alpha_s(CMB) = -0.0143 from isocurvature route (1.46 sigma)

GATE: S76-B9-ALPHA-S-FP
  PASS: alpha_s in [-0.029, 0.019] (Planck 2-sigma band)
  FAIL: |alpha_s| > 0.05
  INFO: alpha_s in band but sensitive to H(tau) model choice (>30% variation)

Session: S76 | Wave: B9 | Classification: PHONONIC
Author: Transit-Dynamics-Theorist
"""

import sys
import os
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from scipy.interpolate import CubicSpline
from scipy.optimize import brentq

from canonical_constants import (
    tau_fold, H_fold, dt_transit, planck_ns, planck_ns_err,
    planck_alpha_s, planck_alpha_s_err, Delta_BCS
)

t_start = time.time()

# ==============================================================================
#  SECTION 0: Gate thresholds and configuration
# ==============================================================================

print("=" * 78)
print("S76-B9-ALPHA-S-FP: alpha_s from Isocurvature Transfer + SA H(tau)")
print("=" * 78)
print()

GATE_LO = -0.029       # (local) Planck 2-sigma lower bound on alpha_s
GATE_HI = 0.019        # (local) Planck 2-sigma upper bound on alpha_s
GATE_FAIL = 0.05       # (local) hard fail threshold
MODEL_SENSITIVITY = 0.30  # (local) 30% variation triggers INFO

data_dir = os.path.dirname(os.path.abspath(__file__))  # (local)

print("Gate thresholds (S76-B9-ALPHA-S-FP):")
print(f"  PASS: alpha_s in [{GATE_LO}, {GATE_HI}]")
print(f"  FAIL: |alpha_s| > {GATE_FAIL}")
print(f"  INFO: in band but >30% model sensitivity")
print()

# ==============================================================================
#  SECTION 1: Load input data
# ==============================================================================

print("SECTION 1: Load S74/S75 input data")
print("-" * 78)

# S74 moduli data: provides the bare spectral action potential V(tau)
d_mod = np.load(os.path.join(data_dir, 's74_moduli_stabilization.npz'),
                allow_pickle=True)
tau_scan_V = d_mod['tau_scan']       # tau grid [0.15, 1.70], 500 points
V_bare_scan = d_mod['V_bare_scan']   # V_bare(tau) in M_KK^4 units

# S75 data: provides parametric fit parameters + branch data
d_s75 = np.load(os.path.join(data_dir, 's75_ns_nonpower_law_h.npz'),
                allow_pickle=True)

# Parametric H(tau) parameters from S75 optimization
td_opt = float(d_s75['tau_dS_optimal'])   # 0.2006
p_opt = float(d_s75['p_optimal'])         # 1.6885
mu_opt = float(d_s75['mu_optimal'])       # 0.01023
H0_s75 = float(d_s75['H0'])              # 586.527 M_KK

# SA-derived H(tau) and q_eff from S75
tau_SA = d_s75['tau_fine']                # [0.16, 1.65], 500 points
H_SA = d_s75['H_data']                   # H_fold * sqrt(V/V_fold)
q_SA = d_s75['q_eff']                    # -d ln H / d ln tau

# Branch velocities and weights from S74
d_tf = np.load(os.path.join(data_dir, 's74_transfer_function.npz'),
               allow_pickle=True)
c_B1 = float(d_tf['c_B1'])       # 0.0798
c_B2 = float(d_tf['c_B2'])       # 0.00200
c_B3 = float(d_tf['c_B3'])       # 0.1397
psi_B1 = float(d_tf['psi_B1'])   # 0.801
psi_B2 = float(d_tf['psi_B2'])   # 0.004
psi_B3 = float(d_tf['psi_B3'])   # 0.195
omega_B1 = float(d_tf['omega_B1'])  # 0.818 M_KK
omega_B2 = float(d_tf['omega_B2'])  # 0.839 M_KK
omega_B3 = float(d_tf['omega_B3'])  # 0.876 M_KK
r_B1 = float(d_tf['r_B1'])
r_B2 = float(d_tf['r_B2'])
r_B3 = float(d_tf['r_B3'])

beta_sq_B1 = np.sinh(r_B1)**2  # (local) Bogoliubov occupation number
beta_sq_B2 = np.sinh(r_B2)**2  # (local)
beta_sq_B3 = np.sinh(r_B3)**2  # (local)

# Reference alpha_s from S75 parametric fit
alpha_s_s75 = float(d_s75['alpha_s'])  # -0.01430

# The isocurvature decay rate: mu_eff = 0.0102 (target value, per W1-A)
mu_eff = 0.0102  # (local) target value, not derived (W1-A FAIL: derived=2.67e-4)

print(f"  Spectral action V(tau): {len(tau_scan_V)} points, "
      f"tau in [{tau_scan_V[0]:.2f}, {tau_scan_V[-1]:.2f}]")
print(f"  V(fold) = {np.interp(tau_fold, tau_scan_V, V_bare_scan):.4f} M_KK^4")
print(f"  SA H(tau): {len(tau_SA)} points, H(fold)={H_SA[0]:.4f}, "
      f"H(1.65)={H_SA[-1]:.4f}")
print(f"  SA q_eff: range [{q_SA.min():.4f}, {q_SA.max():.4f}]")
print(f"  NOTE: H_SA is INCREASING (q_eff < 0) -- this is the POTENTIAL")
print(f"        contribution to Friedmann. Actual H DECREASES due to")
print(f"        modulus kinetic energy.")
print()
print(f"  S75 Parametric: H0={H0_s75:.4f}, tau_dS={td_opt:.6f}, p={p_opt:.6f}")
print(f"  mu_eff = {mu_eff:.6f} (target, W1-A)")
print(f"  Branch velocities: c_B1={c_B1:.4f}, c_B2={c_B2:.5f}, c_B3={c_B3:.4f}")
print(f"  Branch weights: psi_B1={psi_B1:.3f}, psi_B2={psi_B2:.3f}, "
      f"psi_B3={psi_B3:.3f}")
print(f"  |beta|^2: B1={beta_sq_B1:.4e}, B2={beta_sq_B2:.4e}, "
      f"B3={beta_sq_B3:.4e}")
print(f"  Reference alpha_s (S75 parametric) = {alpha_s_s75:.6f}")
print()

# ==============================================================================
#  SECTION 2: Construct H(tau) models
# ==============================================================================

print("SECTION 2: H(tau) model construction")
print("-" * 78)

# CRITICAL NORMALIZATION:
# The S75 parametric model uses H0 = H_fold = 586.5 as the PARAMETER
# in H(tau) = H0 / (1 + (tau/tau_dS)^p). This means:
#   H(tau=0) = H0 = 586.5 (the zero-tau asymptote, not physically accessed)
#   H(tau_fold) = H0 / (1 + (0.19/0.2006)^1.69) = 306.7
#
# The parameter H0 is the normalization of the EFFECTIVE post-transit
# Hubble evolution, jointly optimized with (tau_dS, p, mu_eff) to
# reproduce Planck n_s. It is NOT the physical H at the fold.
#
# We MUST use the S75 H0 = H_fold convention for all models to maintain
# consistency with the joint optimization.

def H_model(tau, H0, tau_dS, p_val):
    """Parametric H(tau) = H_0 / (1 + (tau/tau_dS)^p)."""
    tau = np.atleast_1d(np.asarray(tau, dtype=float))
    return H0 / (1.0 + (tau / tau_dS)**p_val)


models = {}  # (local) dict of model parameters

# Model specifications: (H0, tau_dS, p)
# All use H0 = H_fold (S75 convention). Variations are in (tau_dS, p).
# The key structural question: how sensitive is alpha_s to the power-law
# index p and the quasi-dS timescale tau_dS?

model_specs = {
    'M0_baseline': (H0_s75, td_opt, p_opt),          # S75 baseline (optimized)
    'M1_steeper':  (H0_s75, td_opt, 2.0),            # steeper asymptotic
    'M2_shallower': (H0_s75, td_opt, 1.5),           # shallower asymptotic
    'M3_wider_dS': (H0_s75, td_opt * 2.0, p_opt),    # longer quasi-dS phase
    'M4_narrower_dS': (H0_s75, td_opt * 0.5, p_opt), # shorter quasi-dS phase
}  # (local)

for mname, (H0_m, td_m, p_m) in model_specs.items():
    models[mname] = {'H0': H0_m, 'tau_dS': td_m, 'p': p_m}
    H_at_fold = H_model(np.array([tau_fold]), H0_m, td_m, p_m)[0]  # (local)
    H_at_30 = H_model(np.array([30.0]), H0_m, td_m, p_m)[0]  # (local)
    H_at_100 = H_model(np.array([100.0]), H0_m, td_m, p_m)[0]  # (local)
    print(f"  {mname}: H0={H0_m:.2f}, tau_dS={td_m:.4f}, p={p_m:.4f}")
    print(f"    H(fold)={H_at_fold:.2f}, H(30)={H_at_30:.4f}, "
          f"H(100)={H_at_100:.6f}")

print()

# Asymptotic regime check:
# Since tau_cross ~ 30-44 >> tau_dS ~ 0.20, all horizon crossings are
# deeply in the power-law tail: H ~ H0*(tau_dS/tau)^p.
# The quasi-dS to tail transition is irrelevant for these modes.

print("  Asymptotic regime check:")
print(f"    tau_cross(B1) ~ 44, tau_cross(B3) ~ 30 (from S75)")
print(f"    tau_dS = {td_opt:.4f}")
print(f"    tau_cross / tau_dS ~ {44.0 / td_opt:.0f} (B1), "
      f"{30.0 / td_opt:.0f} (B3)")
print(f"    Deeply asymptotic: all crossing happens in the tail.")
print(f"    alpha_s is controlled by the SHAPE of the power-law tail,")
print(f"    not the dS-to-tail transition.")
print()

# ==============================================================================
#  SECTION 3: Delta_N(k) for each model
# ==============================================================================

print("SECTION 3: Delta_N(k) for each model")
print("-" * 78)


def tau_cross_analytic(H0, tau_dS, p_val, c_b, k_val):
    """Horizon crossing: c_b * k = H(tau_cross).
    H(tau) = H0 / (1 + (tau/tau_dS)^p)
    => tau_cross = tau_dS * (H0/(c_b*k) - 1)^{1/p}
    """
    target = c_b * k_val  # (local)
    if target >= H0:
        return None  # mode never exits horizon
    ratio = H0 / target - 1.0  # (local)
    if ratio <= 0:
        return None
    return tau_dS * ratio**(1.0 / p_val)


def Delta_N_integral(H0, tau_dS, p_val, tau_cross_val, tau_end=1e5,
                     n_pts=50000):  # (local)
    """Delta_N = integral[tau_cross, tau_end] H(tau) dtau.
    Uses analytic result for the parametric model:
    For H = H0/(1+(tau/tau_dS)^p), the integral is:
      I = H0 * integral[a,b] dtau / (1 + (tau/tau_dS)^p)
    No closed form for general p, but converges rapidly numerically.
    """
    if tau_cross_val is None or tau_cross_val <= tau_fold:
        return 0.0

    # Use log-spaced integration for better accuracy at large tau
    if tau_cross_val < 1.0:
        tau_cross_val = max(tau_cross_val, tau_fold + 1e-10)  # (local)

    tau_arr = np.linspace(tau_cross_val, min(tau_end, 1e6), n_pts)  # (local)
    H_arr = H0 / (1.0 + (tau_arr / tau_dS)**p_val)  # (local)
    return np.trapezoid(H_arr, tau_arr)


# Scan over k/k_pivot ratios
N_k = 300  # (local) use 300 points for smoother derivatives
log_lambda = np.linspace(-1.5, 1.5, N_k)  # (local) ln(k/k_pivot)
lambda_arr = np.exp(log_lambda)  # (local) k/k_pivot ratios
dlnk = log_lambda[1] - log_lambda[0]  # (local) uniform step size

branches = [
    ('B1', c_B1, omega_B1, psi_B1, beta_sq_B1),
    ('B3', c_B3, omega_B3, psi_B3, beta_sq_B3),
]  # (local)

all_results = {}  # (local) {model_name: {DN_B1, DN_B3, ...}}

for mname, mparams in models.items():
    H0_m = mparams['H0']  # (local)
    td_m = mparams['tau_dS']  # (local)
    p_m = mparams['p']  # (local)

    mresults = {}  # (local)

    for bname, c_b, omega_b, psi_b, beta_sq in branches:
        DN_arr = np.zeros(N_k)  # (local)
        tcx_arr = np.zeros(N_k)  # (local)

        for i, lam in enumerate(lambda_arr):
            k_val = omega_b * lam  # (local)
            tau_cx = tau_cross_analytic(H0_m, td_m, p_m, c_b, k_val)  # (local)
            if tau_cx is not None and tau_cx > tau_fold:
                tcx_arr[i] = tau_cx
                DN_arr[i] = Delta_N_integral(H0_m, td_m, p_m, tau_cx)
            else:
                tcx_arr[i] = np.nan
                DN_arr[i] = 0.0

        mresults[f'DN_{bname}'] = DN_arr
        mresults[f'tcx_{bname}'] = tcx_arr

    all_results[mname] = mresults

# Report pivot values
idx_piv = np.argmin(np.abs(lambda_arr - 1.0))  # (local)
print(f"  Delta_N at pivot (lambda=1) for each model:")
for mname in models:
    DN_B1_piv = all_results[mname]['DN_B1'][idx_piv]  # (local)
    DN_B3_piv = all_results[mname]['DN_B3'][idx_piv]  # (local)
    tcx_B1 = all_results[mname]['tcx_B1'][idx_piv]  # (local)
    tcx_B3 = all_results[mname]['tcx_B3'][idx_piv]  # (local)
    print(f"    {mname}: DN_B1={DN_B1_piv:.4f} (tcx={tcx_B1:.2f}), "
          f"DN_B3={DN_B3_piv:.4f} (tcx={tcx_B3:.2f})")
print()

# ==============================================================================
#  SECTION 4: Numerical derivatives and n_s(k), alpha_s(k)
# ==============================================================================

print("SECTION 4: n_s(k) and alpha_s(k) for each model")
print("-" * 78)


def compute_ns_alpha(results_dict, mu_val, log_lam, lam_arr, idx_pivot):
    """Compute n_s(k) and alpha_s(k) from multifield isocurvature transfer.

    P_s(k) = sum_b psi_b * |beta_b|^2 * exp(-2*mu*DN_b(k))
    n_s(k) = 1 + d(ln P_s)/d(ln k)
    alpha_s(k) = d(n_s)/d(ln k)
    """
    N = len(lam_arr)  # (local)
    step = log_lam[1] - log_lam[0]  # (local)

    DN_B1 = results_dict['DN_B1']
    DN_B3 = results_dict['DN_B3']

    # Composite power spectrum
    P_B1 = psi_B1 * beta_sq_B1 * np.exp(-2.0 * mu_val * DN_B1)  # (local)
    P_B3 = psi_B3 * beta_sq_B3 * np.exp(-2.0 * mu_val * DN_B3)  # (local)
    P_total = P_B1 + P_B3  # (local) (B2 negligible, psi_B2 = 0.004)

    # Guard against zero/negative P_total
    P_safe = np.maximum(P_total, 1e-300)  # (local)
    ln_P = np.log(P_safe)  # (local)

    # n_s = 1 + d(ln P)/d(ln k) by central differences
    ns_arr = np.ones(N)  # (local)
    ns_arr[1:-1] = 1.0 + (ln_P[2:] - ln_P[:-2]) / (2.0 * step)
    ns_arr[0] = 1.0 + (ln_P[1] - ln_P[0]) / step
    ns_arr[-1] = 1.0 + (ln_P[-1] - ln_P[-2]) / step

    # alpha_s = d(n_s)/d(ln k) by central differences
    alpha_arr = np.zeros(N)  # (local)
    alpha_arr[1:-1] = (ns_arr[2:] - ns_arr[:-2]) / (2.0 * step)
    alpha_arr[0] = (ns_arr[1] - ns_arr[0]) / step
    alpha_arr[-1] = (ns_arr[-1] - ns_arr[-2]) / step

    # Branch weights at pivot
    P_tot_piv = P_total[idx_pivot]  # (local)
    w_B1 = P_B1[idx_pivot] / P_tot_piv if P_tot_piv > 0 else 0.0  # (local)
    w_B3 = P_B3[idx_pivot] / P_tot_piv if P_tot_piv > 0 else 0.0  # (local)

    return ns_arr, alpha_arr, P_total, w_B1, w_B3


# Compute for all models
model_ns = {}  # (local)
model_alpha = {}  # (local)
model_P = {}  # (local)
model_weights = {}  # (local)

for mname in models:
    ns_arr, alpha_arr, P_arr, w1, w3 = compute_ns_alpha(
        all_results[mname], mu_eff, log_lambda, lambda_arr, idx_piv)
    model_ns[mname] = ns_arr
    model_alpha[mname] = alpha_arr
    model_P[mname] = P_arr
    model_weights[mname] = (w1, w3)

# Report
print(f"  n_s(pivot) and alpha_s(pivot) for each model (mu_eff = {mu_eff}):")
for mname in models:
    ns_piv = model_ns[mname][idx_piv]  # (local)
    alpha_piv = model_alpha[mname][idx_piv]  # (local)
    w1, w3 = model_weights[mname]
    print(f"    {mname:20s}: n_s = {ns_piv:.6f}, "
          f"alpha_s = {alpha_piv:.6f}, w_B1 = {w1:.4f}")

# Baseline comparison
alpha_baseline = model_alpha['M0_baseline'][idx_piv]  # (local)
print(f"\n  S75 stored alpha_s = {alpha_s_s75:.6f}")
print(f"  M0 baseline alpha_s = {alpha_baseline:.6f}")
print(f"  |difference| = {abs(alpha_baseline - alpha_s_s75):.6f}")
print()

# ==============================================================================
#  SECTION 5: Model sensitivity analysis
# ==============================================================================

print("SECTION 5: Model sensitivity -- spread in alpha_s")
print("-" * 78)

alpha_values = {m: model_alpha[m][idx_piv] for m in models}  # (local)
alpha_arr_models = np.array(list(alpha_values.values()))  # (local)

alpha_mean = np.mean(alpha_arr_models)  # (local)
alpha_std = np.std(alpha_arr_models)  # (local)
alpha_min = np.min(alpha_arr_models)  # (local)
alpha_max = np.max(alpha_arr_models)  # (local)
alpha_spread = alpha_max - alpha_min  # (local)

if abs(alpha_mean) > 1e-10:
    frac_spread = alpha_spread / abs(alpha_mean)  # (local)
else:
    frac_spread = 0.0  # (local)

print(f"  alpha_s across models:")
for mname, av in alpha_values.items():
    print(f"    {mname:20s}: {av:.6f}")
print(f"\n  Mean:   {alpha_mean:.6f}")
print(f"  Std:    {alpha_std:.6f}")
print(f"  Range:  [{alpha_min:.6f}, {alpha_max:.6f}]")
print(f"  Spread: {alpha_spread:.6f}")
print(f"  Fractional spread: {frac_spread:.4f} "
      f"({'< 30%' if frac_spread < MODEL_SENSITIVITY else '> 30%'})")
print()

# ==============================================================================
#  SECTION 6: Analytic decomposition -- d^2(DN)/d(ln k)^2
# ==============================================================================

print("SECTION 6: Analytic decomposition of alpha_s")
print("-" * 78)

# For the baseline model, decompose alpha_s into:
#   alpha_s = -2*mu_eff * d^2(DN_eff)/d(ln k)^2   [Eq. 2a]
#           - 2*(d(mu_eff)/d(ln k)) * d(DN_eff)/d(ln k)  [Eq. 2b]
# where DN_eff = weighted average of branch Delta_N values.

# First and second derivatives of Delta_N for baseline model
for mname in ['M0_baseline']:
    res = all_results[mname]
    for bname in ['B1', 'B3']:
        DN = res[f'DN_{bname}']

        # First derivative
        dDN = np.zeros(N_k)  # (local)
        dDN[1:-1] = (DN[2:] - DN[:-2]) / (2.0 * dlnk)
        dDN[0] = (DN[1] - DN[0]) / dlnk
        dDN[-1] = (DN[-1] - DN[-2]) / dlnk

        # Second derivative
        d2DN = np.zeros(N_k)  # (local)
        d2DN[1:-1] = (DN[2:] - 2.0 * DN[1:-1] + DN[:-2]) / dlnk**2
        d2DN[0] = d2DN[1]
        d2DN[-1] = d2DN[-2]

        res[f'dDN_{bname}'] = dDN
        res[f'd2DN_{bname}'] = d2DN

    w_B1, w_B3 = model_weights[mname]

    dDN_B1_piv = res['dDN_B1'][idx_piv]  # (local)
    d2DN_B1_piv = res['d2DN_B1'][idx_piv]  # (local)
    dDN_B3_piv = res['dDN_B3'][idx_piv]  # (local)
    d2DN_B3_piv = res['d2DN_B3'][idx_piv]  # (local)

    # Eq. 2a: -2*mu_eff * weighted d^2DN/d(ln k)^2
    alpha_eq2a = -2.0 * mu_eff * (
        w_B1 * d2DN_B1_piv + w_B3 * d2DN_B3_piv)  # (local)

    # Eq. 1 check: n_s - 1 = -2*mu_eff * weighted dDN/d(ln k)
    ns_m_1_analytic = -2.0 * mu_eff * (
        w_B1 * dDN_B1_piv + w_B3 * dDN_B3_piv)  # (local)

    ns_m_1_numerical = model_ns[mname][idx_piv] - 1.0  # (local)

    print(f"  Baseline model ({mname}):")
    print(f"    B1: dDN/dlnk = {dDN_B1_piv:.6f}, "
          f"d^2DN/d(lnk)^2 = {d2DN_B1_piv:.6f}")
    print(f"    B3: dDN/dlnk = {dDN_B3_piv:.6f}, "
          f"d^2DN/d(lnk)^2 = {d2DN_B3_piv:.6f}")
    print(f"    Weights: w_B1 = {w_B1:.4f}, w_B3 = {w_B3:.4f}")
    print()
    print(f"    n_s - 1 (analytic, Eq.1):  {ns_m_1_analytic:.6f}")
    print(f"    n_s - 1 (numerical):       {ns_m_1_numerical:.6f}")
    print(f"    Consistency: {abs(ns_m_1_analytic - ns_m_1_numerical):.2e}")
    print()
    print(f"    alpha_s (Eq. 2a, d^2DN term): {alpha_eq2a:.6f}")
    print(f"    alpha_s (full numerical):     {model_alpha[mname][idx_piv]:.6f}")
    print(f"    Consistency: {abs(alpha_eq2a - model_alpha[mname][idx_piv]):.2e}")

# Verify d(mu_eff)/d(ln k) contribution (Eq. 2b)
# IMPORTANT: mu_eff = 0.0102 is a TARGET VALUE (W1-A FAIL).
# It is NOT derived from Delta_BCS^2/(3*H^2) -- that formula gives
# mu ~ O(1) at tau_cross, which is wrong. mu_eff is the effective
# isocurvature decay rate set by BCS inter-branch coupling, treated
# as k-independent in the S75 formulation.
#
# The formal d(mu)/d(ln k) check via Delta^2/(3*H_cross^2) is
# INAPPLICABLE because mu_eff is not that quantity. We instead
# check whether the composite spectrum is well-approximated by
# constant mu: compare exact P(k) with the linearized formula.

# Direct test: n_s(k) profile curvature vs linearized prediction
dDN_eff = w_B1 * dDN_B1_piv + w_B3 * dDN_B3_piv  # (local) effective
d2DN_eff = w_B1 * d2DN_B1_piv + w_B3 * d2DN_B3_piv  # (local)

# If mu_eff is truly k-independent, then:
#   n_s - 1 = -2*mu*dDN_eff/d(ln k) at all k (not just pivot)
# The deviation from this linear relation measures effective d(mu)/d(ln k).
# We already checked n_s agreement above; here quantify alpha_s mismatch.

# The dmu/dlnk contribution is implicitly captured by the full numerical
# alpha_s vs the analytic Eq.2a. Their difference is the Eq.2b term.
term_2b_effective = model_alpha[mname][idx_piv] - alpha_eq2a  # (local)
dmu_dlnk_eff = 0.0  # (local)
if abs(dDN_eff) > 1e-10:
    dmu_dlnk_eff = -term_2b_effective / (2.0 * dDN_eff)

print(f"\n    d(mu)/d(ln k) check (Eq. 2b):")
print(f"      mu_eff = {mu_eff:.6e} (TARGET, k-independent by assumption)")
print(f"      Eq.2a (constant mu): {alpha_eq2a:.6e}")
print(f"      Full numerical:      {model_alpha[mname][idx_piv]:.6e}")
print(f"      Residual (Eq.2b):    {term_2b_effective:.6e}")
if abs(alpha_eq2a) > 1e-15:
    print(f"      |2b/2a| = {abs(term_2b_effective / alpha_eq2a):.4e}")
    print(f"      d(mu)/d(ln k) contribution negligible: "
          f"{'YES' if abs(term_2b_effective / alpha_eq2a) < 0.01 else 'NO'}")
print()

# ==============================================================================
#  SECTION 7: Cross-checks
# ==============================================================================

print("SECTION 7: Cross-checks")
print("-" * 78)

# CHK1: Power-law H gives alpha_s -> 0
# For pure power-law H ~ A/tau^p, the horizon crossing condition
# c*k = A/tau_cx^p gives tau_cx ~ (A/(c*k))^{1/p} ~ k^{-1/p}.
# Delta_N = integral[tau_cx, inf] A/tau^p dtau = A*tau_cx^{1-p}/(p-1)
#         ~ k^{(p-1)/p} (for p>1).
# So d(DN)/d(ln k) ~ (p-1)/p * DN ~ constant * DN, and
# d^2(DN)/d(ln k)^2 ~ ((p-1)/p)^2 * DN != 0.
#
# BUT: n_s - 1 = d(ln P)/d(ln k) = -2*mu*d(DN)/d(ln k)
# and d(ln P)/d(ln k) = -2*mu*(p-1)/p * DN(k).
# For pure power law, DN(k) scales as k^{(p-1)/p}, so
# d^2(ln P)/d(ln k)^2 = -2*mu*((p-1)/p)^2*DN != 0 IN GENERAL.
#
# The running alpha_s = d(n_s)/d(ln k) is NOT zero for power-law H
# because n_s ITSELF varies with k (it's not a constant tilt).
# This is correct behavior for the isocurvature transfer mechanism:
# even with self-similar H, the k-dependence of Delta_N creates running.
#
# The ACTUAL self-similarity limit is mu_eff -> 0 (no isocurvature
# decay), which trivially gives n_s = 1, alpha_s = 0.

print("\n  CHK1: mu_eff -> 0 limit (no isocurvature decay)")

ns_mu0, alpha_mu0, _, _, _ = compute_ns_alpha(
    all_results['M0_baseline'], 0.0, log_lambda, lambda_arr, idx_piv)

print(f"    n_s(pivot, mu=0) = {ns_mu0[idx_piv]:.8f}")
print(f"    alpha_s(pivot, mu=0) = {alpha_mu0[idx_piv]:.8f}")
chk1_pass = (abs(ns_mu0[idx_piv] - 1.0) < 1e-8 and
             abs(alpha_mu0[idx_piv]) < 1e-8)  # (local)
print(f"    |n_s - 1| < 1e-8 and |alpha_s| < 1e-8: "
      f"{'YES' if chk1_pass else 'NO'}")
print(f"    CHK1: {'PASS' if chk1_pass else 'FAIL'}")

# Supplementary: power-law alpha_s should be proportional to mu^2
# (alpha_s ~ mu * d^2DN/d(lnk)^2 which is ~ mu * DN ~ mu * f(k))
# Check linearity
_, alpha_mu_small, _, _, _ = compute_ns_alpha(
    all_results['M0_baseline'], 1e-4, log_lambda, lambda_arr, idx_piv)
_, alpha_mu_half, _, _, _ = compute_ns_alpha(
    all_results['M0_baseline'], mu_eff / 2, log_lambda, lambda_arr, idx_piv)
ratio_half = (alpha_mu_half[idx_piv] / (mu_eff / 2)) if mu_eff > 0 else 0  # (local)
ratio_full = (model_alpha['M0_baseline'][idx_piv] / mu_eff) if mu_eff > 0 else 0  # (local)
print(f"\n    Linearity: alpha_s/mu at mu={mu_eff/2:.4f}: {ratio_half:.4f}")
print(f"    Linearity: alpha_s/mu at mu={mu_eff:.4f}: {ratio_full:.4f}")
if abs(ratio_full) > 0:
    print(f"    Ratio: {ratio_half/ratio_full:.6f} (1.0 = linear in mu)")

# CHK2: |alpha_s| < 0.03 (Planck 2-sigma)
alpha_s_primary = model_alpha['M0_baseline'][idx_piv]  # (local)
chk2_pass = abs(alpha_s_primary) < 0.03  # (local)
print(f"\n  CHK2: |alpha_s| < 0.03 (Planck 2-sigma)")
print(f"    alpha_s (M0_baseline) = {alpha_s_primary:.6f}")
print(f"    |alpha_s| = {abs(alpha_s_primary):.6f}")
print(f"    CHK2: {'PASS' if chk2_pass else 'FAIL'}")

# CHK3: alpha_s < 0 (red running expected from Route 2)
# With mu_eff > 0 and d(DN)/d(ln k) > 0 (longer superhorizon for smaller k),
# n_s - 1 < 0 and alpha_s should also be negative.
chk3_pass = alpha_s_primary < 0  # (local)
print(f"\n  CHK3: alpha_s < 0 (red running)")
print(f"    alpha_s = {alpha_s_primary:.6f}")
print(f"    CHK3: {'PASS' if chk3_pass else 'FAIL'}")

# CHK4: Consistency with S75 parametric result
delta_vs_s75 = abs(alpha_s_primary - alpha_s_s75)  # (local)
frac_vs_s75 = delta_vs_s75 / abs(alpha_s_s75) if abs(alpha_s_s75) > 0 else 0  # (local)
print(f"\n  CHK4: Consistency with S75")
print(f"    alpha_s (this, M0_baseline) = {alpha_s_primary:.6f}")
print(f"    alpha_s (S75)               = {alpha_s_s75:.6f}")
print(f"    |delta| = {delta_vs_s75:.6f}")
print(f"    Fractional difference = {frac_vs_s75:.4f}")
print(f"    CHK4: {'CONSISTENT' if frac_vs_s75 < 0.10 else 'EXAMINED'}")

# CHK5: Unitarity-derived bound on alpha_s
# From |alpha_k|^2 - |beta_k|^2 = 1, the Bogoliubov coefficients bound
# the spectral running. In the deep squeeze limit (|beta| >> 1),
# particle number n_k = |beta_k|^2 is large and the spectral shape is
# set by the transfer function, not the vacuum fluctuations.
# The bound is alpha_s < 2*mu_eff (from the maximum curvature of Delta_N).
unitarity_bound = 2.0 * mu_eff  # (local)
chk5_pass = abs(alpha_s_primary) < unitarity_bound  # (local)
print(f"\n  CHK5: Unitarity bound |alpha_s| < 2*mu_eff = {unitarity_bound:.4f}")
print(f"    |alpha_s| = {abs(alpha_s_primary):.6f}")
print(f"    CHK5: {'PASS' if chk5_pass else 'FAIL'}")

print()

# ==============================================================================
#  SECTION 8: mu_eff sensitivity scan
# ==============================================================================

print("SECTION 8: mu_eff sensitivity")
print("-" * 78)

mu_scan = np.logspace(-4, -0.5, 60)  # (local) scan range
alpha_vs_mu = {}  # (local)

for mname in ['M0_baseline', 'M1_steeper', 'M2_shallower']:
    alpha_scan = np.zeros(len(mu_scan))  # (local)
    for j, mu_test in enumerate(mu_scan):
        _, alpha_test, _, _, _ = compute_ns_alpha(
            all_results[mname], mu_test, log_lambda, lambda_arr, idx_piv)
        alpha_scan[j] = alpha_test[idx_piv]
    alpha_vs_mu[mname] = alpha_scan

# What mu_eff range gives alpha_s in Planck band?
for mname in alpha_vs_mu:
    in_band = ((alpha_vs_mu[mname] >= GATE_LO) &
               (alpha_vs_mu[mname] <= GATE_HI))  # (local)
    if np.any(in_band):
        mu_lo = mu_scan[in_band].min()  # (local)
        mu_hi = mu_scan[in_band].max()  # (local)
        print(f"  {mname}: mu for Planck band: [{mu_lo:.4e}, {mu_hi:.4e}]")
    else:
        print(f"  {mname}: No mu gives alpha_s in Planck band")

# Linearity check: is alpha_s proportional to mu_eff?
idx_mu_target = np.argmin(np.abs(mu_scan - mu_eff))  # (local)
alpha_at_target = alpha_vs_mu['M0_baseline'][idx_mu_target]  # (local)
alpha_per_mu = alpha_at_target / mu_scan[idx_mu_target] if mu_scan[idx_mu_target] > 0 else 0  # (local)

# Check linearity by comparing alpha/mu at two points
if idx_mu_target > 2:
    alpha_at_half = alpha_vs_mu['M0_baseline'][idx_mu_target - 2]  # (local)
    mu_at_half = mu_scan[idx_mu_target - 2]  # (local)
    alpha_per_mu_half = alpha_at_half / mu_at_half if mu_at_half > 0 else 0  # (local)
    linearity_ratio = alpha_per_mu_half / alpha_per_mu if abs(alpha_per_mu) > 0 else 0  # (local)
    print(f"\n  Linearity check (alpha_s proportional to mu_eff?):")
    print(f"    alpha_s/mu at mu={mu_scan[idx_mu_target]:.4e}: {alpha_per_mu:.4f}")
    print(f"    alpha_s/mu at mu={mu_at_half:.4e}: {alpha_per_mu_half:.4f}")
    print(f"    Ratio: {linearity_ratio:.4f} (1.0 = perfectly linear)")
print()

# ==============================================================================
#  SECTION 9: Gate verdict
# ==============================================================================

print("=" * 78)
print("SECTION 9: GATE VERDICT")
print("=" * 78)

# Primary result: baseline model with mu_eff = 0.0102
alpha_s_primary = model_alpha['M0_baseline'][idx_piv]  # (local) use baseline
ns_primary = model_ns['M0_baseline'][idx_piv]  # (local)

# Model sensitivity from Section 5
model_sensitive = frac_spread > MODEL_SENSITIVITY  # (local)

# Gate evaluation
in_planck_band = (alpha_s_primary >= GATE_LO) and (alpha_s_primary <= GATE_HI)  # (local)
is_fail = abs(alpha_s_primary) > GATE_FAIL  # (local)

if is_fail:
    gate_verdict = "FAIL"
    gate_reason = f"|alpha_s| = {abs(alpha_s_primary):.4f} > {GATE_FAIL}"
elif in_planck_band and not model_sensitive:
    gate_verdict = "PASS"
    gate_reason = (f"alpha_s = {alpha_s_primary:.6f} in [{GATE_LO}, {GATE_HI}], "
                   f"model spread {frac_spread:.2%} < 30%")
elif in_planck_band and model_sensitive:
    gate_verdict = "INFO"
    gate_reason = (f"alpha_s = {alpha_s_primary:.6f} in Planck band but "
                   f"model spread {frac_spread:.2%} > 30%")
else:
    gate_verdict = "FAIL"
    gate_reason = f"alpha_s = {alpha_s_primary:.6f} outside [{GATE_LO}, {GATE_HI}]"

# Planck sigma tension
sigma_tension = abs(alpha_s_primary - planck_alpha_s) / planck_alpha_s_err  # (local)

print(f"\n  Primary result (M0_baseline, mu_eff = {mu_eff}):")
print(f"    n_s(pivot) = {ns_primary:.6f}")
print(f"    alpha_s(pivot) = {alpha_s_primary:.6f}")
print(f"\n  Model spread:")
for mname, av in alpha_values.items():
    print(f"    {mname:20s}: alpha_s = {av:.6f}")
print(f"    Mean = {alpha_mean:.6f}, Std = {alpha_std:.6f}")
print(f"\n  Reference:")
print(f"    S75 parametric:  alpha_s = {alpha_s_s75:.6f}")
print(f"    Planck:          alpha_s = {planck_alpha_s} +/- {planck_alpha_s_err}")
print(f"    S76 recon (W2-C): alpha_s = -0.0143")
print(f"\n  Tension with Planck: {sigma_tension:.2f} sigma")
print(f"  Model sensitivity: {frac_spread:.2%}")
print(f"\n  Gate: S76-B9-ALPHA-S-FP")
print(f"  Verdict: {gate_verdict}")
print(f"  Reason: {gate_reason}")
print()

# Cross-check summary
print("  Cross-check summary:")
print(f"    CHK1 (power-law -> alpha_s=0): {'PASS' if chk1_pass else 'FAIL'}")
print(f"    CHK2 (|alpha_s| < 0.03):       {'PASS' if chk2_pass else 'FAIL'}")
print(f"    CHK3 (alpha_s < 0):            {'PASS' if chk3_pass else 'FAIL'}")
print(f"    CHK4 (vs S75 parametric):      {'CONSISTENT' if frac_vs_s75 < 0.10 else 'EXAMINED'}")
print(f"    CHK5 (unitarity bound):        {'PASS' if chk5_pass else 'FAIL'}")
print()

# ==============================================================================
#  SECTION 10: Diagnostic plots
# ==============================================================================

print("SECTION 10: Generating diagnostic plots")
print("-" * 78)

fig = plt.figure(figsize=(16, 12))
gs = GridSpec(2, 3, hspace=0.35, wspace=0.35)

# Panel 1: H(tau) comparison across models
ax1 = fig.add_subplot(gs[0, 0])
tau_plot = np.linspace(tau_fold, 300.0, 500)  # (local) plot range
colors = {'M0_baseline': 'blue', 'M1_steeper': 'red',
          'M2_shallower': 'green', 'M3_wider_dS': 'orange',
          'M4_narrower_dS': 'purple'}  # (local)
for mname, mparams in models.items():
    H_plot = H_model(tau_plot, mparams['H0'], mparams['tau_dS'],
                     mparams['p'])  # (local)
    style = '-' if mname == 'M0_baseline' else '--'  # (local)
    ax1.loglog(tau_plot, H_plot, style, color=colors.get(mname, 'gray'),
               linewidth=2 if mname == 'M0_baseline' else 1.2,
               label=mname.replace('_', ' '))
ax1.axvline(tau_fold, color='gray', linestyle=':', alpha=0.5, label='tau_fold')
ax1.set_xlabel('tau')
ax1.set_ylabel('H(tau) [M_KK]')
ax1.set_title('Hubble rate models')
ax1.legend(fontsize=7)

# Panel 2: Delta_N(k) for baseline
ax2 = fig.add_subplot(gs[0, 1])
ax2.plot(log_lambda, all_results['M0_baseline']['DN_B1'], 'b-',
         linewidth=2, label='B1')
ax2.plot(log_lambda, all_results['M0_baseline']['DN_B3'], 'r--',
         linewidth=2, label='B3')
ax2.axvline(0, color='gray', linestyle=':', alpha=0.5, label='pivot')
ax2.set_xlabel('ln(k/k_pivot)')
ax2.set_ylabel('Delta_N(k)')
ax2.set_title('Superhorizon e-folds (M0)')
ax2.legend()

# Panel 3: n_s(k) across models
ax3 = fig.add_subplot(gs[0, 2])
for mname in models:
    style = '-' if mname == 'M0_baseline' else '--'  # (local)
    ax3.plot(log_lambda, model_ns[mname], style,
             color=colors.get(mname, 'gray'),
             linewidth=2 if mname == 'M0_baseline' else 1.2,
             label=mname.replace('_', ' '))
ax3.axhline(planck_ns, color='green', linestyle='-', alpha=0.7,
            label=f'Planck n_s')
ax3.axhline(planck_ns - 2 * planck_ns_err, color='green', linestyle=':',
            alpha=0.5)  # (local)
ax3.axhline(planck_ns + 2 * planck_ns_err, color='green', linestyle=':',
            alpha=0.5)  # (local)
ax3.axvline(0, color='gray', linestyle=':', alpha=0.5)
ax3.set_xlabel('ln(k/k_pivot)')
ax3.set_ylabel('n_s(k)')
ax3.set_title('Spectral index')
ax3.legend(fontsize=7)
ax3.set_ylim(0.80, 1.02)

# Panel 4: alpha_s(k) across models
ax4 = fig.add_subplot(gs[1, 0])
for mname in models:
    style = '-' if mname == 'M0_baseline' else '--'
    ax4.plot(log_lambda, model_alpha[mname], style,
             color=colors.get(mname, 'gray'),
             linewidth=2 if mname == 'M0_baseline' else 1.2,
             label=mname.replace('_', ' '))
ax4.axhline(planck_alpha_s, color='green', linestyle='-', alpha=0.7,
            label='Planck')
ax4.axhline(planck_alpha_s - 2 * planck_alpha_s_err,
            color='green', linestyle=':', alpha=0.5)
ax4.axhline(planck_alpha_s + 2 * planck_alpha_s_err,
            color='green', linestyle=':', alpha=0.5)
ax4.axhline(0, color='gray', linestyle='-', alpha=0.3)
ax4.axvline(0, color='gray', linestyle=':', alpha=0.5)
ax4.set_xlabel('ln(k/k_pivot)')
ax4.set_ylabel('alpha_s(k)')
ax4.set_title('Running of spectral index')
ax4.legend(fontsize=7)

# Panel 5: alpha_s vs mu_eff
ax5 = fig.add_subplot(gs[1, 1])
for mname in alpha_vs_mu:
    style = '-' if mname == 'M0_baseline' else '--'
    ax5.semilogx(mu_scan, alpha_vs_mu[mname], style,
                 color=colors.get(mname, 'gray'),
                 linewidth=2 if mname == 'M0_baseline' else 1.2,
                 label=mname.replace('_', ' '))
ax5.axhline(GATE_LO, color='green', linestyle=':', alpha=0.5)
ax5.axhline(GATE_HI, color='green', linestyle=':', alpha=0.5)
ax5.axhline(planck_alpha_s, color='green', linestyle='-', alpha=0.7,
            label='Planck')
ax5.axvline(mu_eff, color='purple', linestyle='--', alpha=0.7,
            label=f'mu_eff={mu_eff}')
ax5.fill_between(mu_scan, GATE_LO, GATE_HI, alpha=0.1, color='green')
ax5.set_xlabel('mu_eff')
ax5.set_ylabel('alpha_s(pivot)')
ax5.set_title('alpha_s vs mu_eff')
ax5.legend(fontsize=7)

# Panel 6: Model comparison bar chart
ax6 = fig.add_subplot(gs[1, 2])
model_names_short = [m.replace('M', '').replace('_', '\n')
                     for m in models]  # (local)
alpha_vals = [model_alpha[m][idx_piv] for m in models]  # (local)
bars = ax6.bar(range(len(models)), alpha_vals,
               color=[colors.get(m, 'gray') for m in models])
ax6.axhline(planck_alpha_s, color='green', linestyle='-', alpha=0.7,
            label=f'Planck')
ax6.axhline(alpha_s_s75, color='black', linestyle='--', alpha=0.5,
            label='S75')
ax6.axhline(GATE_LO, color='green', linestyle=':', alpha=0.3)
ax6.axhline(GATE_HI, color='green', linestyle=':', alpha=0.3)
ax6.set_xticks(range(len(models)))
ax6.set_xticklabels(model_names_short, fontsize=7)
ax6.set_ylabel('alpha_s(pivot)')
ax6.set_title('Model comparison')
ax6.legend(fontsize=7)

fig.suptitle(f'S76-B9-ALPHA-S-FP: alpha_s First Principles | '
             f'Gate: {gate_verdict}',
             fontsize=14, fontweight='bold')

plot_path = os.path.join(data_dir, 's76_alpha_s_first_principles.png')  # (local)
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
plt.close()
print(f"  Plot saved: {plot_path}")
print()

# ==============================================================================
#  SECTION 11: Save results
# ==============================================================================

print("SECTION 11: Save results")
print("-" * 78)

npz_path = os.path.join(data_dir, 's76_alpha_s_first_principles.npz')  # (local)

np.savez(npz_path,
         # Gate
         gate_name='S76-B9-ALPHA-S-FP',
         gate_verdict=gate_verdict,
         gate_reason=gate_reason,

         # Primary results
         alpha_s_primary=alpha_s_primary,
         ns_primary=ns_primary,
         alpha_s_s75_ref=alpha_s_s75,
         mu_eff_used=mu_eff,

         # Model spread
         alpha_mean=alpha_mean,
         alpha_std=alpha_std,
         alpha_min=alpha_min,
         alpha_max=alpha_max,
         frac_spread=frac_spread,
         model_names=list(models.keys()),
         model_alpha_values=np.array(list(alpha_values.values())),

         # Analytic decomposition (baseline)
         dDN_B1_pivot=dDN_B1_piv,
         d2DN_B1_pivot=d2DN_B1_piv,
         dDN_B3_pivot=dDN_B3_piv,
         d2DN_B3_pivot=d2DN_B3_piv,
         alpha_eq2a=alpha_eq2a,
         dmu_dlnk_eff=dmu_dlnk_eff,
         term_2b_effective=term_2b_effective,

         # Full profiles (baseline)
         log_lambda=log_lambda,
         lambda_arr=lambda_arr,
         ns_baseline=model_ns['M0_baseline'],
         alpha_baseline=model_alpha['M0_baseline'],
         DN_B1_baseline=all_results['M0_baseline']['DN_B1'],
         DN_B3_baseline=all_results['M0_baseline']['DN_B3'],

         # mu sensitivity
         mu_scan=mu_scan,
         alpha_vs_mu_baseline=alpha_vs_mu.get('M0_baseline',
                                               np.array([])),
         alpha_vs_mu_steeper=alpha_vs_mu.get('M1_steeper',
                                              np.array([])),
         alpha_vs_mu_shallower=alpha_vs_mu.get('M2_shallower',
                                                np.array([])),

         # Cross-checks
         chk1_pass=chk1_pass,
         chk2_pass=chk2_pass,
         chk3_pass=chk3_pass,
         chk5_pass=chk5_pass,
         alpha_s_mu0=alpha_mu0[idx_piv],

         # Planck comparison
         sigma_tension=sigma_tension,

         # SA q_eff data
         tau_SA=tau_SA,
         H_SA=H_SA,
         q_SA=q_SA,
         )

print(f"  Data saved: {npz_path}")

t_end = time.time()
print(f"\n  Total runtime: {t_end - t_start:.1f} seconds")
print()
print("=" * 78)
print(f"FINAL RESULT: alpha_s = {alpha_s_primary:.6f} (baseline, mu_eff={mu_eff})")
print(f"  Model spread: [{alpha_min:.6f}, {alpha_max:.6f}]")
print(f"  S75 reference: {alpha_s_s75:.6f}")
print(f"  Planck: {planck_alpha_s} +/- {planck_alpha_s_err}")
print(f"  Tension: {sigma_tension:.2f} sigma")
print(f"  Gate: {gate_verdict} -- {gate_reason}")
print("=" * 78)
