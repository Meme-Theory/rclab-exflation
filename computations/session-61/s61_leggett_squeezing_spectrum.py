#!/usr/bin/env python3
"""
s61_leggett_squeezing_spectrum.py — Mode-Resolved Leggett Squeezing Spectrum
=============================================================================

Gate: LEGGETT-SPECTRUM-61
    PASS if non-thermal (chi^2/dof > 3)
    FAIL if thermal (chi^2/dof < 1)
    INFO if intermediate [1, 3]

PHYSICS:
    The Leggett modes on the 32-cell CG graph have dispersion:
        omega_L^2(n, tau) = omega_L0^2 + J_L(tau) * lambda_n

    where lambda_n are the graph Laplacian eigenvalues (n=0..31).

    During the transit (tau: 0 -> 0.5), each mode undergoes parametric
    excitation (Bogoliubov squeezing). The sudden quench formula gives:
        |beta(n)|^2 = sinh^2(r(n))

    Two methods for the squeezing parameter r(n):
    (A) Sudden quench: r(n) = (1/2)|ln(omega_i(n)/omega_f(n))|
    (B) Integral: r(n) = integral_0^{tau_fold} |d(ln omega_L)/dtau| dtau / 2

    Both give equivalent results in the deeply non-adiabatic regime
    (omega * dt << 1, confirmed S57).

    We compare the k-resolved |beta(n)|^2 spectrum against:
    1. Thermal Bose-Einstein: n_BE(omega) = 1/(exp(omega/T_eff) - 1)
    2. The residual (non-thermal structure)

    A non-thermal spectrum is a GGE relic — direct signature of the ordered veil.

INPUTS:
    - s54_tb_hamiltonian.npz (tau grid, TB eigenvalues, CG adjacency, J_C2(tau))
    - s54_scale_factor.npz (H(tau) for T_GH)
    - canonical_constants.py (omega_L1, Delta_0_OES, etc.)

OUTPUTS:
    - s61_leggett_squeezing_spectrum.npz
    - s61_leggett_squeezing_spectrum.png

Author: quantum-acoustics-theorist
Session: S61 (W4-03)
"""

import sys
import os
import numpy as np
from scipy.optimize import minimize_scalar, curve_fit
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
from canonical_constants import (
    tau_fold, E_cond, N_cells,
    omega_L1,          # 0.138 M_KK (S52 GL-Josephson, canonical gap)
    omega_L2,          # 0.192 M_KK (S52 GL-Josephson, Leggett-2)
    Delta_0_OES,       # 0.4643 M_KK (BCS gap)
    J_C2,              # 0.933 M_KK (C2 Josephson coupling)
    T_acoustic,        # 0.112 M_KK (GGE temperature)
    M_ATDHFB,          # 1.695 (collective mass)
    v_terminal,        # 26.545 (terminal velocity)
    PI,
)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

print("=" * 70)
print("S61 LEGGETT-SPECTRUM-61: Mode-Resolved Leggett Squeezing Spectrum")
print("=" * 70)

# ======================================================================
# 0. Constants
# ======================================================================

# S59 canonical epsilon (supersedes S49 eps=0.00248 and S58 eps_bare=0.00143)
# eps_canonical = 0.00374 from EPSILON-CANONICAL-59 PASS
eps_canonical = 0.00374  # (local)

# V_bare Leggett gap from S59 (3-band eigenvalue: 0.04923 M_KK)
omega_L0_Vbare = 0.04923  # (local)

# Two gap models:
#   Model A: canonical GL gap (0.138 M_KK) -- from canonical_constants
#   Model B: V_bare eigenvalue gap (0.04923 M_KK) -- from S59
omega_L0_A = omega_L1       # 0.138 M_KK
omega_L0_B = omega_L0_Vbare # 0.04923 M_KK

Delta = Delta_0_OES  # 0.4643 M_KK

print(f"\nConstants:")
print(f"  eps_canonical = {eps_canonical}")
print(f"  omega_L0 (Model A, GL)    = {omega_L0_A:.4f} M_KK")
print(f"  omega_L0 (Model B, Vbare) = {omega_L0_B:.5f} M_KK")
print(f"  Delta (OES) = {Delta:.4f} M_KK")
print(f"  tau_fold = {tau_fold}")
print(f"  N_cells = {N_cells}")

# ======================================================================
# 1. Load CG graph data
# ======================================================================

data_tb = np.load(os.path.join(SCRIPT_DIR, 's54_tb_hamiltonian.npz'), allow_pickle=True)
tau_values = data_tb['tau_values']   # (50,)
eigenvalues = data_tb['eigenvalues'] # (50, 32)
J_C2_tau = data_tb['J_C2_tau']      # (50,)
adj_C2 = data_tb['adj_C2']          # (32, 32)
diameter = int(data_tb['diameter'])

N_tau = len(tau_values)
fold_idx = np.argmin(np.abs(tau_values - tau_fold))

print(f"\nLoaded s54_tb_hamiltonian.npz:")
print(f"  tau grid: {N_tau} points, [{tau_values[0]:.3f}, {tau_values[-1]:.3f}]")
print(f"  fold_idx = {fold_idx}, tau[fold] = {tau_values[fold_idx]:.4f}")

# ======================================================================
# 2. Graph Laplacian eigenvalues
# ======================================================================

A_C2 = adj_C2.astype(float)
degree_C2 = A_C2.sum(axis=1)
L_C2 = np.diag(degree_C2) - A_C2
laplacian_eigs = np.sort(np.linalg.eigvalsh(L_C2))
laplacian_eigs[0] = 0.0  # enforce zero mode

n_bonds = int(A_C2.sum()) // 2
N_modes = N_cells - 1  # 31 dispersive modes (exclude Goldstone n=0)

print(f"\nGraph Laplacian (C2 subgraph, {n_bonds} bonds):")
print(f"  lambda_0 = {laplacian_eigs[0]:.4f} (Goldstone)")
print(f"  lambda_1 = {laplacian_eigs[1]:.4f} (Fiedler)")
print(f"  lambda_31 = {laplacian_eigs[-1]:.4f} (UV)")
print(f"  N_modes = {N_modes} (excluding Goldstone)")

# Dispersive eigenvalues only
lam_disp = laplacian_eigs[1:]  # (31,)

# ======================================================================
# 3. Compute E_J(tau) from BCS coherence factors
# ======================================================================
# Same method as S56: E_J = J_C2^2 * F_anomalous
# F_anomalous = sum_k Delta / (2 * E_qp_k^2)

E_J_arr = np.zeros(N_tau)

for i in range(N_tau):
    eigs_i = eigenvalues[i]
    mu = 0.5 * (eigs_i[15] + eigs_i[16])  # (local)
    xi_k = eigs_i - mu
    E_qp_k = np.sqrt(xi_k**2 + Delta**2)
    F_anom = np.sum(Delta / (2.0 * E_qp_k**2))
    E_J_arr[i] = J_C2_tau[i]**2 * F_anom

print(f"\nE_J(tau):")
print(f"  E_J(0) = {E_J_arr[0]:.4f}")
print(f"  E_J(fold) = {E_J_arr[fold_idx]:.4f}")
print(f"  E_J(end) = {E_J_arr[-1]:.4f}")

# ======================================================================
# 4. Leggett dispersion omega_L(n, tau) for both models
# ======================================================================
# omega_L^2(n, tau) = omega_L0^2 + eps * E_J(tau) * lambda_n

J_L_arr = eps_canonical * E_J_arr  # (N_tau,)

print(f"\nJ_Leggett(tau) = eps * E_J(tau):")
print(f"  J_L(0) = {J_L_arr[0]:.6f}")
print(f"  J_L(fold) = {J_L_arr[fold_idx]:.6f}")
print(f"  J_L(end) = {J_L_arr[-1]:.6f}")

# Dispersion arrays: (N_tau, 31) for dispersive modes
omega_L_A = np.zeros((N_tau, N_modes))  # Model A (GL gap)
omega_L_B = np.zeros((N_tau, N_modes))  # Model B (Vbare gap)

for i in range(N_tau):
    for n in range(N_modes):
        lam_n = lam_disp[n]
        omega_sq_A = omega_L0_A**2 + J_L_arr[i] * lam_n
        omega_sq_B = omega_L0_B**2 + J_L_arr[i] * lam_n
        omega_L_A[i, n] = np.sqrt(max(omega_sq_A, 1e-30))
        omega_L_B[i, n] = np.sqrt(max(omega_sq_B, 1e-30))

print(f"\nLeggett dispersion at fold:")
print(f"  Model A (GL, omega_L0={omega_L0_A:.3f}):")
print(f"    omega_L(n=1) = {omega_L_A[fold_idx, 0]:.6f}")
print(f"    omega_L(n=31) = {omega_L_A[fold_idx, -1]:.6f}")
print(f"    bandwidth = {omega_L_A[fold_idx, -1] - omega_L_A[fold_idx, 0]:.6f}")
print(f"  Model B (Vbare, omega_L0={omega_L0_B:.5f}):")
print(f"    omega_L(n=1) = {omega_L_B[fold_idx, 0]:.6f}")
print(f"    omega_L(n=31) = {omega_L_B[fold_idx, -1]:.6f}")
print(f"    bandwidth = {omega_L_B[fold_idx, -1] - omega_L_B[fold_idx, 0]:.6f}")

# ======================================================================
# 5. Squeezing parameter r(n) — two methods
# ======================================================================

# Method 1: Sudden quench (exact for instantaneous switch)
# r_SQ(n) = (1/2) |ln(omega_i(n) / omega_f(n))|
# where omega_i = omega_L(n, tau=0), omega_f = omega_L(n, tau_fold)

# Method 2: Integral (continuous WKB-like accumulation)
# r_INT(n) = (1/2) integral_0^{tau_fold} |d(ln omega_L)/dtau| dtau
# Discretized: r_INT(n) = (1/2) sum_{i=0}^{fold_idx-1} |ln(omega(i+1)/omega(i))|

print(f"\n{'='*60}")
print("SQUEEZING PARAMETER COMPUTATION")
print(f"{'='*60}")

# --- Model A ---
omega_i_A = omega_L_A[0, :]        # initial (tau=0)
omega_f_A = omega_L_A[fold_idx, :] # final (tau=fold)

# Method 1: sudden quench
r_SQ_A = 0.5 * np.abs(np.log(omega_i_A / omega_f_A))

# Method 2: integral to fold
r_INT_A = np.zeros(N_modes)
for n in range(N_modes):
    cumulative = 0.0
    for i in range(fold_idx):
        if omega_L_A[i, n] > 0 and omega_L_A[i+1, n] > 0:
            cumulative += np.abs(np.log(omega_L_A[i+1, n] / omega_L_A[i, n]))
    r_INT_A[n] = 0.5 * cumulative

# --- Model B ---
omega_i_B = omega_L_B[0, :]
omega_f_B = omega_L_B[fold_idx, :]

r_SQ_B = 0.5 * np.abs(np.log(omega_i_B / omega_f_B))

r_INT_B = np.zeros(N_modes)
for n in range(N_modes):
    cumulative = 0.0
    for i in range(fold_idx):
        if omega_L_B[i, n] > 0 and omega_L_B[i+1, n] > 0:
            cumulative += np.abs(np.log(omega_L_B[i+1, n] / omega_L_B[i, n]))
    r_INT_B[n] = 0.5 * cumulative

print(f"\nModel A (GL gap = {omega_L0_A:.3f}):")
print(f"  r_SQ:  [{r_SQ_A[0]:.6f}, {r_SQ_A[-1]:.6f}]")
print(f"  r_INT: [{r_INT_A[0]:.6f}, {r_INT_A[-1]:.6f}]")
print(f"  SQ/INT ratio: [{(r_SQ_A/r_INT_A)[0]:.4f}, {(r_SQ_A/r_INT_A)[-1]:.4f}]")

print(f"\nModel B (Vbare gap = {omega_L0_B:.5f}):")
print(f"  r_SQ:  [{r_SQ_B[0]:.6f}, {r_SQ_B[-1]:.6f}]")
print(f"  r_INT: [{r_INT_B[0]:.6f}, {r_INT_B[-1]:.6f}]")
print(f"  SQ/INT ratio: [{(r_SQ_B/r_INT_B)[0]:.4f}, {(r_SQ_B/r_INT_B)[-1]:.4f}]")

# Use INTEGRAL method as primary (more accurate for continuous sweep)
r_A = r_INT_A
r_B = r_INT_B

# ======================================================================
# 6. Bogoliubov coefficients |beta(n)|^2 = sinh^2(r(n))
# ======================================================================

beta_sq_A = np.sinh(r_A)**2
beta_sq_B = np.sinh(r_B)**2

# Also compute <n_exc> via direct sudden-quench formula as cross-check
# <n_exc> = (ratio + 1/ratio - 2)/4  where ratio = omega_i/omega_f
ratio_A = omega_i_A / omega_f_A
n_exc_SQ_A = (ratio_A + 1.0/ratio_A - 2.0) / 4.0

ratio_B = omega_i_B / omega_f_B
n_exc_SQ_B = (ratio_B + 1.0/ratio_B - 2.0) / 4.0

print(f"\n{'='*60}")
print("BOGOLIUBOV COEFFICIENTS |beta(n)|^2")
print(f"{'='*60}")

print(f"\nModel A (GL gap):")
print(f"  |beta|^2 range: [{beta_sq_A.min():.6f}, {beta_sq_A.max():.6f}]")
print(f"  <n_exc> SQ range: [{n_exc_SQ_A.min():.6f}, {n_exc_SQ_A.max():.6f}]")
print(f"  Total n_Bog = sum |beta|^2 = {beta_sq_A.sum():.4f}")
print(f"  Mean |beta|^2 = {beta_sq_A.mean():.6f}")

print(f"\nModel B (Vbare gap):")
print(f"  |beta|^2 range: [{beta_sq_B.min():.6f}, {beta_sq_B.max():.6f}]")
print(f"  <n_exc> SQ range: [{n_exc_SQ_B.min():.6f}, {n_exc_SQ_B.max():.6f}]")
print(f"  Total n_Bog = sum |beta|^2 = {beta_sq_B.sum():.4f}")
print(f"  Mean |beta|^2 = {beta_sq_B.mean():.6f}")

# ======================================================================
# 7. Thermal fit: Bose-Einstein distribution
# ======================================================================
# n_BE(omega) = 1 / (exp(omega/T_eff) - 1)
# Fit T_eff to minimize chi^2 between |beta(n)|^2 and n_BE(omega_f(n))

print(f"\n{'='*60}")
print("THERMAL FIT: Bose-Einstein Distribution")
print(f"{'='*60}")

def bose_einstein(omega, T):
    """Bose-Einstein distribution with temperature T."""
    x = omega / T
    # Avoid overflow
    x = np.clip(x, 0, 500)
    return 1.0 / (np.expm1(x))

def chi2_BE_bose(T, omega_f, beta_sq):
    """Chi-squared with Bose counting variance sigma^2 = n(n+1)."""
    n_BE = bose_einstein(omega_f, T)
    sigma_sq = np.maximum(beta_sq * (beta_sq + 1.0), 0.01)
    return np.sum((beta_sq - n_BE)**2 / sigma_sq)

def chi2_BE_uniform(T, omega_f, beta_sq):
    """Chi-squared with UNIFORM variance sigma^2 = <n>^2.
    Appropriate for deterministic data: every point weighted equally."""
    n_BE = bose_einstein(omega_f, T)
    sigma_sq = np.mean(beta_sq)**2  # single scale
    return np.sum((beta_sq - n_BE)**2 / sigma_sq)

def chi2_BE_fractional(T, omega_f, beta_sq):
    """Chi-squared with FRACTIONAL variance sigma^2 = max(n, floor)^2.
    Tests whether the fractional deviation from BE is uniform across modes."""
    n_BE = bose_einstein(omega_f, T)
    floor = 0.001  # 0.1% floor to avoid divergence at tiny n
    sigma_sq = np.maximum(beta_sq, floor)**2
    return np.sum((beta_sq - n_BE)**2 / sigma_sq)

def fit_thermal(omega_f, beta_sq, label):
    """Fit BE temperature with THREE variance models and report all."""
    results_dict = {}
    for vname, chi2fn in [("Bose", chi2_BE_bose),
                           ("Uniform", chi2_BE_uniform),
                           ("Fractional", chi2_BE_fractional)]:
        result = minimize_scalar(lambda T: chi2fn(T, omega_f, beta_sq),
                                bounds=(1e-4, 100.0), method='bounded')
        T_eff = result.x
        chi2_min = result.fun
        dof = len(beta_sq) - 1  # 31 data points, 1 parameter
        chi2_dof = chi2_min / dof
        results_dict[vname] = (T_eff, chi2_min, chi2_dof)

    # Primary: use UNIFORM variance (most appropriate for deterministic spectrum)
    T_eff = results_dict["Uniform"][0]
    n_BE_fit = bose_einstein(omega_f, T_eff)
    residuals = beta_sq - n_BE_fit
    chi2_min_uni = results_dict["Uniform"][1]
    chi2_dof_uni = results_dict["Uniform"][2]

    print(f"\n  {label}:")
    print(f"    Variance model comparison:")
    for vname in ["Bose", "Uniform", "Fractional"]:
        T_v, c2_v, c2dof_v = results_dict[vname]
        print(f"      {vname:12s}: T_eff={T_v:.6f}, chi^2/dof={c2dof_v:.4f}")
    print(f"    PRIMARY (Uniform variance):")
    print(f"      T_eff = {T_eff:.6f} M_KK")
    print(f"      T_acoustic (GGE) = {T_acoustic:.4f} M_KK")
    print(f"      T_eff / T_acoustic = {T_eff / T_acoustic:.4f}")
    print(f"      chi^2/dof = {chi2_dof_uni:.4f}")
    print(f"      max |residual| = {np.max(np.abs(residuals)):.6f}")
    print(f"      rms residual = {np.sqrt(np.mean(residuals**2)):.6f}")
    print(f"      rms / mean(n) = {np.sqrt(np.mean(residuals**2)) / np.mean(beta_sq):.4f}")

    if chi2_dof_uni > 3:
        verdict = "NON-THERMAL (chi^2/dof > 3)"
    elif chi2_dof_uni < 1:
        verdict = "THERMAL (chi^2/dof < 1)"
    else:
        verdict = f"INTERMEDIATE (chi^2/dof = {chi2_dof_uni:.2f} in [1,3])"
    print(f"    VERDICT: {verdict}")

    return T_eff, chi2_min_uni, chi2_dof_uni, n_BE_fit, residuals, results_dict

# Fit Model A
T_A, chi2_A, chi2dof_A, nBE_A, res_A, fits_A = fit_thermal(omega_f_A, beta_sq_A, "Model A (GL gap)")

# Fit Model B
T_B, chi2_B, chi2dof_B, nBE_B, res_B, fits_B = fit_thermal(omega_f_B, beta_sq_B, "Model B (Vbare gap)")

# ======================================================================
# 8. Discriminating functional form tests
# ======================================================================
# The key question: does |beta(n)|^2 = sinh^2(r(n)) have the same
# functional form as n_BE(omega) = 1/(exp(omega/T) - 1)?
#
# Three discriminants:
# (a) Kolmogorov-Smirnov test on CDF
# (b) Log-log slope: BE gives specific curvature, squeezing gives different
# (c) Two-parameter fit: BE with chemical potential mu
#     n_gen(omega) = 1/(exp((omega-mu)/T) - 1)
#     If mu != 0 improves fit significantly, spectrum is non-thermal
#     (thermal equilibrium of conserved bosons has mu=0 for phonons)

print(f"\n{'='*60}")
print("DISCRIMINATING FUNCTIONAL FORM TESTS")
print(f"{'='*60}")

# --- (a) Normalized residual shape: is it structured or random? ---
# For thermal fit, residuals should be structureless.
# Compute runs test: count sign changes in residuals.
# Too few sign changes = systematic structure = non-thermal.

from scipy.stats import mannwhitneyu

def runs_test(residuals):
    """Count runs (sign changes) in residuals. Thermal: ~N/2. Structured: << N/2."""
    signs = np.sign(residuals)
    signs[signs == 0] = 1  # treat zero as positive
    runs = 1 + np.sum(np.abs(np.diff(signs)) > 0)
    n_pos = np.sum(signs > 0)
    n_neg = np.sum(signs < 0)
    n = len(signs)
    # Expected runs for random sequence
    if n_pos > 0 and n_neg > 0:
        E_runs = 1 + 2*n_pos*n_neg / n
        var_runs = 2*n_pos*n_neg*(2*n_pos*n_neg - n) / (n**2 * (n-1))
        z_runs = (runs - E_runs) / np.sqrt(max(var_runs, 1e-10))
    else:
        E_runs = 1
        z_runs = 0
    return runs, E_runs, z_runs

for label, res in [("Model A", res_A), ("Model B", res_B)]:
    runs, E_runs, z_runs = runs_test(res)
    print(f"  {label} runs test: runs={runs}, expected={E_runs:.1f}, z={z_runs:.2f}")
    if abs(z_runs) > 1.96:
        print(f"    SIGNIFICANT (|z|>1.96): residuals are STRUCTURED (non-random)")
    else:
        print(f"    Not significant (|z|<1.96): residuals consistent with random")

# --- (b) BE with chemical potential (2-parameter fit) ---
print(f"\n  Two-parameter BE fit (T, mu):")

def n_gen_BE(omega, T, mu):
    x = (omega - mu) / T
    x = np.clip(x, -500, 500)
    return 1.0 / (np.expm1(x))

for label, omega_f, beta_sq in [("Model A", omega_f_A, beta_sq_A),
                                  ("Model B", omega_f_B, beta_sq_B)]:
    try:
        popt, pcov = curve_fit(n_gen_BE, omega_f, beta_sq,
                               p0=[0.05, 0.0],
                               bounds=([1e-6, -10], [10, np.min(omega_f)-1e-6]),
                               maxfev=10000)
        T_2p, mu_2p = popt
        n_fit_2p = n_gen_BE(omega_f, T_2p, mu_2p)
        ss_res_2p = np.sum((beta_sq - n_fit_2p)**2)
        ss_res_1p = np.sum((beta_sq - bose_einstein(omega_f,
                            fits_A["Uniform"][0] if "A" in label else fits_B["Uniform"][0]))**2)
        # F-test: does the extra parameter improve fit?
        dof_1p = len(beta_sq) - 1
        dof_2p = len(beta_sq) - 2
        if ss_res_2p > 0:
            F_stat = ((ss_res_1p - ss_res_2p) / 1) / (ss_res_2p / dof_2p)
        else:
            F_stat = np.inf
        from scipy.stats import f as f_dist
        p_val_F = 1 - f_dist.cdf(F_stat, 1, dof_2p)
        print(f"    {label}: T={T_2p:.6f}, mu={mu_2p:.6f}")
        print(f"      SS_res(1p)={ss_res_1p:.6e}, SS_res(2p)={ss_res_2p:.6e}")
        print(f"      F-statistic={F_stat:.2f}, p-value={p_val_F:.4e}")
        if p_val_F < 0.05:
            print(f"      mu != 0 is SIGNIFICANT: non-thermal (mu carries transit information)")
        else:
            print(f"      mu = 0 adequate: consistent with zero chemical potential")
    except Exception as e:
        print(f"    {label}: 2-param fit failed: {e}")

# --- (c) Direct analytical comparison ---
# sinh^2(r) vs 1/(exp(omega/T)-1) where r = (1/2)|ln(omega_i/omega_f)|
# For omega_i/omega_f = rho, r = (1/2)|ln(rho)|
# sinh^2(r) = (rho + 1/rho - 2)/4 = (rho - 1)^2/(4*rho)
# BE: n = 1/(exp(omega_f/T) - 1)
# These are DIFFERENT functions of omega_f unless rho(omega_f) has a specific form.
# The squeezing formula is (rho-1)^2/(4*rho) where rho = omega_i/omega_f.
# Since omega^2 = omega_L0^2 + J_L*lambda, and lambda ~ omega_f^2,
# rho = sqrt((omega_L0^2 + J_L_i*lambda) / (omega_L0^2 + J_L_f*lambda))
# This is NOT of the form exp(omega/T) in general.

print(f"\n  Analytical comparison (sinh^2 vs BE functional form):")
# Compute the exact theoretical form and compare
for label, omega_f, omega_i, beta_sq, T_eff, nBE in [
    ("Model A", omega_f_A, omega_i_A, beta_sq_A, T_A, nBE_A),
    ("Model B", omega_f_B, omega_i_B, beta_sq_B, T_B, nBE_B)]:

    # The squeezing result is exact: |beta|^2 = (rho - 1)^2 / (4*rho)
    rho = omega_i / omega_f
    beta_exact = (rho - 1.0)**2 / (4.0 * rho)

    # Verify this matches sinh^2(r)
    r_check = 0.5 * np.abs(np.log(rho))
    beta_sinh = np.sinh(r_check)**2
    match = np.allclose(beta_exact, beta_sinh, rtol=1e-10)
    print(f"    {label}: sinh^2 == (rho-1)^2/(4rho)? {match}")

    # Now compare the CURVATURE of log(|beta|^2) vs log(n_BE)
    # d^2(log n)/d(omega)^2 — different for parametric vs thermal
    log_beta = np.log(np.maximum(beta_sq, 1e-30))
    log_nBE = np.log(np.maximum(nBE, 1e-30))

    # Numerical second derivative
    d2_log_beta = np.gradient(np.gradient(log_beta, omega_f), omega_f)
    d2_log_nBE = np.gradient(np.gradient(log_nBE, omega_f), omega_f)

    curvature_ratio = np.mean(np.abs(d2_log_beta)) / np.mean(np.abs(d2_log_nBE))
    print(f"    Curvature ratio <|d^2 log beta|>/<|d^2 log nBE|> = {curvature_ratio:.4f}")
    print(f"    (1.0 = same shape, !=1 = different functional form)")

# ======================================================================
# 9. Non-thermal structure analysis
# ======================================================================

print(f"\n{'='*60}")
print("NON-THERMAL STRUCTURE ANALYSIS")
print(f"{'='*60}")

# Check for van Hove singularity imprint
# The CG graph Laplacian has a specific eigenvalue distribution.
# If the spectrum is non-thermal, the non-thermal structure should correlate
# with features of the graph spectrum (eigenvalue clustering, gaps).

# Compute d(|beta|^2)/d(lambda) — derivative of occupation vs eigenvalue
# Non-thermal structure = features in this derivative beyond smooth BE

for label, beta_sq, omega_f, T_eff, nBE, lam in [
    ("Model A", beta_sq_A, omega_f_A, T_A, nBE_A, lam_disp),
    ("Model B", beta_sq_B, omega_f_B, T_B, nBE_B, lam_disp)]:

    # Fractional excess over thermal
    frac_excess = (beta_sq - nBE) / np.maximum(nBE, 1e-10)

    # Spearman rank correlation between excess and eigenvalue position
    from scipy.stats import spearmanr, pearsonr
    rho_sp, p_sp = spearmanr(lam, beta_sq - nBE)
    rho_pe, p_pe = pearsonr(lam, beta_sq - nBE)

    # Check for eigenvalue clustering: are residuals correlated with
    # eigenvalue density (van Hove imprint)?
    # Compute local eigenvalue density: delta_lambda between neighbors
    d_lam = np.diff(lam)
    lam_mid = 0.5 * (lam[:-1] + lam[1:])
    local_dos = 1.0 / d_lam  # inverse spacing ~ local DOS

    # Residuals at midpoints (average neighbors)
    res_mid = 0.5 * ((beta_sq - nBE)[:-1] + (beta_sq - nBE)[1:])
    rho_dos, p_dos = spearmanr(local_dos, res_mid)

    print(f"\n  {label}:")
    print(f"    Fractional excess range: [{frac_excess.min():.4f}, {frac_excess.max():.4f}]")
    print(f"    Spearman(lambda, residual): rho={rho_sp:.4f}, p={p_sp:.4e}")
    print(f"    Pearson(lambda, residual):  rho={rho_pe:.4f}, p={p_pe:.4e}")
    print(f"    Spearman(local_DOS, residual): rho={rho_dos:.4f}, p={p_dos:.4e}")

# ======================================================================
# 10. Mode-independence test (S57 theorem cross-check)
# ======================================================================
# S57 proved: for BA modes, omega_n(tau) = f(tau) * sqrt(lambda_n)
# This gives |beta|^2 IDENTICAL for all modes (conformal stretching).
#
# For Leggett modes: omega_L(n,tau) = sqrt(omega_L0^2 + J_L(tau)*lambda_n)
# The mass gap omega_L0 BREAKS conformal factorization.
# The key question: does the mass gap create enough mode-dependence
# for non-thermal structure?

print(f"\n{'='*60}")
print("MODE-INDEPENDENCE TEST (conformal breaking)")
print(f"{'='*60}")

# For BA modes (massless): all |beta|^2 identical
# For Leggett (massive): |beta|^2 varies with n
spread_A = (beta_sq_A.max() - beta_sq_A.min()) / beta_sq_A.mean()
spread_B = (beta_sq_B.max() - beta_sq_B.min()) / beta_sq_B.mean()

print(f"  Model A: |beta|^2 spread = {spread_A:.4f} (0 = conformal, >0.1 = broken)")
print(f"  Model B: |beta|^2 spread = {spread_B:.4f}")

# Compute the ratio omega_L0^2 / (J_L * lambda) — the mass-to-dispersion ratio
# When this >> 1, mass dominates and modes are near-degenerate (quasi-conformal)
# When this << 1, dispersion dominates and modes are distinct

mass_disp_A = omega_L0_A**2 / (J_L_arr[fold_idx] * lam_disp)
mass_disp_B = omega_L0_B**2 / (J_L_arr[fold_idx] * lam_disp)

print(f"\n  Mass/dispersion ratio at fold (omega_L0^2 / J_L*lambda):")
print(f"  Model A: [{mass_disp_A[0]:.4f}, {mass_disp_A[-1]:.4f}]")
print(f"  Model B: [{mass_disp_B[0]:.4f}, {mass_disp_B[-1]:.4f}]")

# ======================================================================
# 11. Final gate verdict
# ======================================================================

print(f"\n{'='*70}")
print("GATE: LEGGETT-SPECTRUM-61")
print(f"{'='*70}")

# Use Model A (canonical GL gap) as primary
chi2_primary = chi2dof_A
model_primary = "A (GL gap)"

# Also report Model B for completeness
print(f"\n  PRIMARY (Model A, omega_L0 = {omega_L0_A:.3f}):")
print(f"    chi^2/dof = {chi2dof_A:.4f}")
print(f"    T_eff = {T_A:.6f} M_KK")
print(f"    Total |beta|^2 = {beta_sq_A.sum():.4f}")

print(f"\n  CROSS-CHECK (Model B, omega_L0 = {omega_L0_B:.5f}):")
print(f"    chi^2/dof = {chi2dof_B:.4f}")
print(f"    T_eff = {T_B:.6f} M_KK")
print(f"    Total |beta|^2 = {beta_sq_B.sum():.4f}")

# Determine verdict from primary model
if chi2_primary > 3.0:
    gate_verdict = "PASS"
    gate_detail = f"NON-THERMAL. chi^2/dof={chi2_primary:.2f} > 3. GGE relic spectrum."
elif chi2_primary < 1.0:
    gate_verdict = "FAIL"
    gate_detail = f"THERMAL. chi^2/dof={chi2_primary:.2f} < 1. Consistent with equilibrium."
else:
    gate_verdict = "INFO"
    gate_detail = f"INTERMEDIATE. chi^2/dof={chi2_primary:.2f} in [1,3]. Marginal non-thermality."

print(f"\n  VERDICT: {gate_verdict}")
print(f"  DETAIL: {gate_detail}")

# Also check: do BOTH models agree?
if (chi2dof_A > 3 and chi2dof_B > 3):
    print(f"  ROBUSTNESS: Both models agree on NON-THERMAL.")
elif (chi2dof_A < 1 and chi2dof_B < 1):
    print(f"  ROBUSTNESS: Both models agree on THERMAL.")
else:
    print(f"  ROBUSTNESS: Models DISAGREE. A: chi^2/dof={chi2dof_A:.2f}, B: chi^2/dof={chi2dof_B:.2f}")

# ======================================================================
# 12. Save data
# ======================================================================

save_path = os.path.join(SCRIPT_DIR, 's61_leggett_squeezing_spectrum.npz')
np.savez(save_path,
    # Grid
    tau_values=tau_values,
    fold_idx=fold_idx,
    N_modes=N_modes,
    laplacian_eigs_disp=lam_disp,
    laplacian_eigs_all=laplacian_eigs,
    # Model A
    omega_L0_A=omega_L0_A,
    omega_L_A=omega_L_A,       # (N_tau, 31)
    r_SQ_A=r_SQ_A,
    r_INT_A=r_INT_A,
    beta_sq_A=beta_sq_A,
    n_exc_SQ_A=n_exc_SQ_A,
    T_eff_A=T_A,
    chi2_A=chi2_A,
    chi2_dof_A=chi2dof_A,
    nBE_fit_A=nBE_A,
    residuals_A=res_A,
    # Model B
    omega_L0_B=omega_L0_B,
    omega_L_B=omega_L_B,       # (N_tau, 31)
    r_SQ_B=r_SQ_B,
    r_INT_B=r_INT_B,
    beta_sq_B=beta_sq_B,
    n_exc_SQ_B=n_exc_SQ_B,
    T_eff_B=T_B,
    chi2_B=chi2_B,
    chi2_dof_B=chi2dof_B,
    nBE_fit_B=nBE_B,
    residuals_B=res_B,
    # Variance model comparison
    chi2dof_bose_A=fits_A["Bose"][2],
    chi2dof_uniform_A=fits_A["Uniform"][2],
    chi2dof_fractional_A=fits_A["Fractional"][2],
    chi2dof_bose_B=fits_B["Bose"][2],
    chi2dof_uniform_B=fits_B["Uniform"][2],
    chi2dof_fractional_B=fits_B["Fractional"][2],
    # Shared
    eps_canonical=eps_canonical,
    E_J_arr=E_J_arr,
    J_L_arr=J_L_arr,
    spread_A=spread_A,
    spread_B=spread_B,
    # Gate
    gate_name='LEGGETT-SPECTRUM-61',
    gate_verdict=gate_verdict,
    gate_detail=gate_detail,
)
print(f"\nSaved: {save_path}")

# ======================================================================
# 13. Plot
# ======================================================================

fig = plt.figure(figsize=(18, 14))
gs = GridSpec(3, 3, figure=fig, hspace=0.35, wspace=0.3)

# --- Panel (0,0): Dispersion at fold ---
ax00 = fig.add_subplot(gs[0, 0])
ax00.plot(lam_disp, omega_L_A[fold_idx, :], 'bo-', ms=4, label=f'Model A ($\\omega_{{L0}}$={omega_L0_A:.3f})')
ax00.plot(lam_disp, omega_L_B[fold_idx, :], 'rs-', ms=4, label=f'Model B ($\\omega_{{L0}}$={omega_L0_B:.3f})')
ax00.set_xlabel('Laplacian eigenvalue $\\lambda_n$')
ax00.set_ylabel('$\\omega_L(n)$ [$M_{KK}$]')
ax00.set_title(f'Leggett Dispersion at Fold ($\\tau$={tau_values[fold_idx]:.3f})')
ax00.legend(fontsize=8)
ax00.grid(True, alpha=0.3)

# --- Panel (0,1): Squeezing parameter r(n) ---
ax01 = fig.add_subplot(gs[0, 1])
ax01.plot(lam_disp, r_A, 'bo-', ms=4, label='Model A (integral)')
ax01.plot(lam_disp, r_SQ_A, 'b^--', ms=3, alpha=0.5, label='Model A (sudden)')
ax01.plot(lam_disp, r_B, 'rs-', ms=4, label='Model B (integral)')
ax01.plot(lam_disp, r_SQ_B, 'rv--', ms=3, alpha=0.5, label='Model B (sudden)')
ax01.set_xlabel('Laplacian eigenvalue $\\lambda_n$')
ax01.set_ylabel('Squeezing parameter $r(n)$')
ax01.set_title('Squeezing Parameter vs Mode')
ax01.legend(fontsize=7)
ax01.grid(True, alpha=0.3)

# --- Panel (0,2): |beta(n)|^2 spectrum (THE key result) ---
ax02 = fig.add_subplot(gs[0, 2])
ax02.semilogy(lam_disp, beta_sq_A, 'bo-', ms=5, lw=2, label=f'Model A: $|\\beta|^2$')
ax02.semilogy(lam_disp, nBE_A, 'b--', lw=1.5, alpha=0.7, label=f'BE fit ($T$={T_A:.4f})')
ax02.semilogy(lam_disp, beta_sq_B, 'rs-', ms=5, lw=2, label=f'Model B: $|\\beta|^2$')
ax02.semilogy(lam_disp, nBE_B, 'r--', lw=1.5, alpha=0.7, label=f'BE fit ($T$={T_B:.4f})')
ax02.set_xlabel('Laplacian eigenvalue $\\lambda_n$')
ax02.set_ylabel('$|\\beta(n)|^2$')
ax02.set_title('Bogoliubov Spectrum: Data vs Thermal Fit')
ax02.legend(fontsize=7)
ax02.grid(True, alpha=0.3)

# --- Panel (1,0): Residuals (Model A) ---
ax10 = fig.add_subplot(gs[1, 0])
ax10.bar(np.arange(N_modes), res_A, color='steelblue', alpha=0.7)
ax10.axhline(0, color='k', lw=0.5)
ax10.set_xlabel('Mode index $n$')
ax10.set_ylabel('$|\\beta|^2 - n_{BE}$')
ax10.set_title(f'Residuals (Model A, $\\chi^2/dof$={chi2dof_A:.2f})')
ax10.grid(True, alpha=0.3)

# --- Panel (1,1): Residuals (Model B) ---
ax11 = fig.add_subplot(gs[1, 1])
ax11.bar(np.arange(N_modes), res_B, color='indianred', alpha=0.7)
ax11.axhline(0, color='k', lw=0.5)
ax11.set_xlabel('Mode index $n$')
ax11.set_ylabel('$|\\beta|^2 - n_{BE}$')
ax11.set_title(f'Residuals (Model B, $\\chi^2/dof$={chi2dof_B:.2f})')
ax11.grid(True, alpha=0.3)

# --- Panel (1,2): omega_L vs tau (selected modes) ---
ax12 = fig.add_subplot(gs[1, 2])
mode_indices = [0, 7, 15, 23, 30]  # sample across spectrum
colors = plt.cm.viridis(np.linspace(0, 1, len(mode_indices)))
for idx, c in zip(mode_indices, colors):
    ax12.plot(tau_values, omega_L_A[:, idx], '-', color=c, lw=1.5,
              label=f'n={idx+1}, $\\lambda$={lam_disp[idx]:.2f}')
ax12.axvline(tau_values[fold_idx], color='gray', ls='--', alpha=0.5, label='fold')
ax12.set_xlabel('$\\tau$')
ax12.set_ylabel('$\\omega_L(n, \\tau)$ [$M_{KK}$]')
ax12.set_title('Leggett Frequency Evolution (Model A)')
ax12.legend(fontsize=7, loc='upper right')
ax12.grid(True, alpha=0.3)

# --- Panel (2,0): Frequency ratio omega_i/omega_f ---
ax20 = fig.add_subplot(gs[2, 0])
ax20.plot(lam_disp, ratio_A, 'bo-', ms=4, label='Model A')
ax20.plot(lam_disp, ratio_B, 'rs-', ms=4, label='Model B')
ax20.axhline(1.0, color='gray', ls='--', alpha=0.5)
ax20.set_xlabel('Laplacian eigenvalue $\\lambda_n$')
ax20.set_ylabel('$\\omega_i / \\omega_f$')
ax20.set_title('Frequency Ratio (Initial/Final)')
ax20.legend(fontsize=8)
ax20.grid(True, alpha=0.3)

# --- Panel (2,1): |beta|^2 vs omega_f (physical frequency) ---
ax21 = fig.add_subplot(gs[2, 1])
ax21.semilogy(omega_f_A, beta_sq_A, 'bo-', ms=5, lw=2, label='Model A')
ax21.semilogy(omega_f_A, nBE_A, 'b--', lw=1.5, alpha=0.7, label=f'BE ($T_A$={T_A:.4f})')
ax21.semilogy(omega_f_B, beta_sq_B, 'rs-', ms=5, lw=2, label='Model B')
ax21.semilogy(omega_f_B, nBE_B, 'r--', lw=1.5, alpha=0.7, label=f'BE ($T_B$={T_B:.4f})')
ax21.set_xlabel('$\\omega_f(n)$ [$M_{KK}$]')
ax21.set_ylabel('$|\\beta(n)|^2$')
ax21.set_title('Spectrum vs Final Frequency')
ax21.legend(fontsize=7)
ax21.grid(True, alpha=0.3)

# --- Panel (2,2): Summary text ---
ax22 = fig.add_subplot(gs[2, 2])
ax22.axis('off')
summary_text = (
    f"LEGGETT-SPECTRUM-61\n"
    f"{'='*40}\n\n"
    f"Model A (GL, $\\omega_{{L0}}$={omega_L0_A:.3f}):\n"
    f"  $T_{{eff}}$ = {T_A:.4f} $M_{{KK}}$\n"
    f"  $\\chi^2/dof$ = {chi2dof_A:.2f}\n"
    f"  $\\Sigma|\\beta|^2$ = {beta_sq_A.sum():.3f}\n"
    f"  spread = {spread_A:.3f}\n\n"
    f"Model B (Vbare, $\\omega_{{L0}}$={omega_L0_B:.4f}):\n"
    f"  $T_{{eff}}$ = {T_B:.4f} $M_{{KK}}$\n"
    f"  $\\chi^2/dof$ = {chi2dof_B:.2f}\n"
    f"  $\\Sigma|\\beta|^2$ = {beta_sq_B.sum():.3f}\n"
    f"  spread = {spread_B:.3f}\n\n"
    f"$\\epsilon_{{canon}}$ = {eps_canonical}\n"
    f"$T_{{acoustic}}$ = {T_acoustic} $M_{{KK}}$\n\n"
    f"VERDICT: {gate_verdict}\n"
    f"{gate_detail}"
)
ax22.text(0.05, 0.95, summary_text, transform=ax22.transAxes,
          fontsize=9, verticalalignment='top', fontfamily='monospace',
          bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

fig.suptitle('S61: Mode-Resolved Leggett Squeezing Spectrum', fontsize=14, fontweight='bold')

plot_path = os.path.join(SCRIPT_DIR, 's61_leggett_squeezing_spectrum.png')
fig.savefig(plot_path, dpi=150, bbox_inches='tight')
print(f"Saved: {plot_path}")
plt.close()

print(f"\n{'='*70}")
print("COMPUTATION COMPLETE")
print(f"{'='*70}")
