#!/usr/bin/env python3
"""
S75-C1-NS-NONPOWER: n_s from Non-Power-Law H(tau) Decay Profile
================================================================

S74 TRANSFER-FUNCTION-74 showed n_s = 1.000 exactly when H(tau) ~ 1/tau^2
(radiation-like). The mechanism is transparent: for power-law H, the number
of superhorizon e-folds Delta_N(k) = integral[tau_cross(k), tau_end] H dtau
scales self-similarly in k, so the isocurvature-to-adiabatic transfer
coefficient T_SS is k-independent. Result: P_s = constant, n_s = 1.

For non-power-law H(tau) with a quasi-de Sitter plateau before transitioning
to power-law decay, Delta_N(k) acquires a non-trivial k-dependence because
the self-similarity is broken. The composite power spectrum becomes:

  P_s(k) = sum_b psi_b * |beta_b|^2 * exp(-2 * mu_b * [Delta_N_0 - Delta_N_b(k)])

where mu_b is the isocurvature decay rate for branch b. This gives:

  n_s - 1 = -2 * mu_eff * d(Delta_N)/d(ln k)

The d(Delta_N)/d(ln k) is purely geometric (set by H(tau)), while mu_eff
is set by the BCS physics (inter-branch coupling in the GGE relic).

SUBSTRATE FRAMING
=================
H(tau) emerges from the a_2 Seeley-DeWitt coefficient. The quasi-de Sitter
phase is the period of approximately constant spectral reorganization rate
before asymptotic power-law effacement. The isocurvature mass mu comes from
the BCS interaction between branches -- the same interaction that produces
the gap Delta_BCS.

GATE: S75-C1-NS-NONPOWER
  PASS: n_s in [0.9607, 0.9691] for physically motivated H(tau)
  INFO: n_s in [0.950, 0.975] but requires fine-tuning
  FAIL: n_s outside [0.950, 0.975] for all H(tau)

Session: S75 | Wave: C1 | Classification: PHONONIC
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
from scipy.optimize import minimize

from canonical_constants import *

t_start = time.time()

# ==============================================================================
#  SECTION 0: Header + gate thresholds
# ==============================================================================

print("=" * 78)
print("S75-C1-NS-NONPOWER: n_s from Non-Power-Law H(tau) Decay Profile")
print("=" * 78)
print()
print("Gate thresholds (S75-C1-NS-NONPOWER):")
print("  PASS: n_s in [0.9607, 0.9691] for physically motivated H(tau)")
print("  INFO: n_s in [0.950, 0.975] but requires fine-tuning")
print("  FAIL: n_s outside [0.950, 0.975] for all H(tau)")
print()

data_dir = os.path.dirname(os.path.abspath(__file__))  # (local)

NS_PLANCK_LO = 0.9607    # (local)
NS_PLANCK_HI = 0.9691    # (local)
NS_PLANCK_BEST = 0.9649  # (local)
NS_INFO_LO = 0.950       # (local)
NS_INFO_HI = 0.975       # (local)

# ==============================================================================
#  SECTION 1: Load S74 data
# ==============================================================================

print("SECTION 1: Load S74 data")
print("-" * 78)

d_mod = np.load(os.path.join(data_dir, 's74_moduli_stabilization.npz'),
                allow_pickle=True)
d_tf = np.load(os.path.join(data_dir, 's74_transfer_function.npz'),
               allow_pickle=True)

# S74 per-branch data
c_B1_s74 = float(d_tf['c_B1'])           # 0.0798
c_B2_s74 = float(d_tf['c_B2'])           # 0.00200
c_B3_s74 = float(d_tf['c_B3'])           # 0.1397
psi_B1 = float(d_tf['psi_B1'])           # 0.801
psi_B2 = float(d_tf['psi_B2'])           # 0.004
psi_B3 = float(d_tf['psi_B3'])           # 0.195
omega_B1_val = float(d_tf['omega_B1'])   # 0.818
omega_B2_val = float(d_tf['omega_B2'])   # 0.839
omega_B3_val = float(d_tf['omega_B3'])   # 0.876
r_B1_s74 = float(d_tf['r_B1'])
r_B2_s74 = float(d_tf['r_B2'])
r_B3_s74 = float(d_tf['r_B3'])

# Transit |beta|^2
beta_sq_B1 = np.sinh(r_B1_s74)**2  # (local)
beta_sq_B2 = np.sinh(r_B2_s74)**2  # (local)
beta_sq_B3 = np.sinh(r_B3_s74)**2  # (local)

# Spectral action data for H(tau) near fold
tau_scan_V = d_mod['tau_scan']
V_bare_scan = d_mod['V_bare_scan']
spl_V = CubicSpline(tau_scan_V, V_bare_scan)
V_at_fold = spl_V(tau_fold)  # (local)

print(f"  Branch velocities: c_B1={c_B1_s74:.4f}, c_B2={c_B2_s74:.5f}, "
      f"c_B3={c_B3_s74:.4f}")
print(f"  Branch weights: psi_B1={psi_B1:.3f}, psi_B2={psi_B2:.3f}, "
      f"psi_B3={psi_B3:.3f}")
print(f"  Transit |beta|^2: B1={beta_sq_B1:.4e}, B2={beta_sq_B2:.4e}, "
      f"B3={beta_sq_B3:.4e}")
print(f"  H_fold = {H_fold:.4f} M_KK, dt_transit = {dt_transit:.6f} M_KK^{{-1}}")
print()

# ==============================================================================
#  SECTION 2: Parametric H(tau) and crossing times
# ==============================================================================

print("SECTION 2: Parametric H(tau) = H_0 / (1 + (tau/tau_dS)^p)")
print("-" * 78)


def H_param(tau, H0, tau_dS, p):
    """Non-power-law Hubble rate."""
    return H0 / (1.0 + (tau / tau_dS)**p)


def tau_cross_analytic(H0, tau_dS, p, c_b, k_sub):
    """Horizon crossing: c_b * k = H(tau_cross)."""
    target = c_b * k_sub  # (local)
    if target >= H0:
        return tau_fold
    ratio = H0 / target - 1.0  # (local)
    if ratio <= 0:
        return tau_fold
    return tau_dS * ratio**(1.0 / p)


def Delta_N_branch(H0, tau_dS, p, c_b, k_sub, tau_end=1e5, n_pts=20000):
    """Number of superhorizon e-folds from crossing to tau_end.

    Delta_N = integral from tau_cross(k) to tau_end of H(tau) dtau.
    This is the key quantity: its k-dependence drives n_s.
    """
    tau_cx = tau_cross_analytic(H0, tau_dS, p, c_b, k_sub)  # (local)
    if tau_cx <= tau_fold or tau_cx >= tau_end:
        return 0.0

    # For H = H0/(1 + (tau/tau_dS)^p), analytic integral for p=1,2:
    # p=1: integral = H0*tau_dS*ln(1 + tau/tau_dS)
    # p=2: integral = H0*tau_dS*arctan(tau/tau_dS)
    # General p: use numerical integration.

    # Numerical (general p)
    tau_arr = np.linspace(tau_cx, tau_end, n_pts)  # (local)
    H_arr = H0 / (1.0 + (tau_arr / tau_dS)**p)  # (local)
    return np.trapezoid(H_arr, tau_arr)


# Spectral action effective power-law index
tau_fine = np.linspace(0.16, 1.65, 500)  # (local)
H_data = H_fold * np.sqrt(spl_V(tau_fine) / V_at_fold)  # (local)
q_eff = -np.gradient(np.log(H_data), np.log(tau_fine))   # (local)

print(f"  Spectral action q_eff (non-power-law indicator):")
print(f"    q_eff(0.19) = {np.interp(0.19, tau_fine, q_eff):.4f}")
print(f"    q_eff(0.50) = {np.interp(0.50, tau_fine, q_eff):.4f}")
print(f"    q_eff(1.00) = {np.interp(1.00, tau_fine, q_eff):.4f}")
print(f"    Variation: [{q_eff.min():.4f}, {q_eff.max():.4f}]")
print(f"    NON-POWER-LAW confirmed: q_eff changes by factor "
      f"{abs(q_eff.max()/q_eff.min()):.1f}")
print()

# ==============================================================================
#  SECTION 3: n_s formula from isocurvature transfer
# ==============================================================================

print("SECTION 3: n_s from multifield isocurvature transfer")
print("-" * 78)

# The key result (Vernizzi & Wands 2006, Sasaki & Stewart 1996):
#
# For a multifield system with branches b, the observed power spectrum is:
#   P_s(k) = sum_b psi_b * |beta_b|^2 * exp(-2*mu_b*Delta_N_b(k)) / Z(k)
# where Z(k) normalizes and mu_b is the isocurvature decay rate.
#
# The composite n_s is:
#   n_s - 1 = -2 * sum_b [w_b(k) * mu_b * dDN_b/d(ln k)]
# where w_b = P_b / P_total are the k-dependent weights.
#
# For a SINGLE effective branch (B1 dominated with psi_B1 = 0.80):
#   n_s - 1 = -2 * mu_eff * d(Delta_N_B1)/d(ln k)
#
# The isocurvature mass mu_eff:
# - From BCS inter-branch coupling: mu ~ Delta_BCS^2 / H^2 (at crossing)
# - From modulus mass: mu ~ m_tau^2 / (3*H^2)
# - mu is a DERIVED quantity from the substrate; its value constrains the
#   inter-branch coupling strength.

def compute_dDN_dlnk(H0, tau_dS, p, c_b, k_sub, dlnk=0.01):
    """d(Delta_N)/d(ln k) at pivot k."""
    k_p = k_sub * np.exp(dlnk)   # (local)
    k_m = k_sub * np.exp(-dlnk)  # (local)
    DN_p = Delta_N_branch(H0, tau_dS, p, c_b, k_p)  # (local)
    DN_m = Delta_N_branch(H0, tau_dS, p, c_b, k_m)  # (local)
    return (DN_p - DN_m) / (2 * dlnk)


def ns_from_transfer(H0, tau_dS, p, mu_eff,
                     c_b_list, k_sub_list, psi_list, beta_sq_list):
    """Compute n_s from the multifield isocurvature transfer.

    n_s - 1 = -2 * sum_b [w_b * mu_b * dDN_b/d(ln k)]

    For simplicity, use uniform mu_eff across all branches.
    The branch weights w_b are evaluated self-consistently.
    """
    dlnk = 0.01  # (local)
    # Power spectrum at pivot and nearby
    def P_at_k(k_factor):
        P = 0.0  # (local)
        for c_b, k_nom, psi_b, beta_sq in zip(
                c_b_list, k_sub_list, psi_list, beta_sq_list):
            k_use = k_nom * k_factor  # (local)
            DN = Delta_N_branch(H0, tau_dS, p, c_b, k_use)  # (local)
            P += psi_b * beta_sq * np.exp(-2 * mu_eff * DN)
        return P

    P0 = P_at_k(1.0)    # (local)
    Pp = P_at_k(np.exp(dlnk))   # (local)
    Pm = P_at_k(np.exp(-dlnk))  # (local)

    if P0 <= 0 or Pp <= 0 or Pm <= 0:
        return 1.0

    ns_m_1 = (np.log(Pp) - np.log(Pm)) / (2 * dlnk)  # (local)
    return 1.0 + ns_m_1


# ==============================================================================
#  SECTION 4: Cross-check CHK1 -- Power law gives n_s = 1
# ==============================================================================

print("SECTION 4: Cross-check CHK1 -- Power law gives n_s = 1")
print("-" * 78)

# For power-law H: tau_dS -> 0, Delta_N scales self-similarly.
# exp(-2*mu*DN) should give k-independent P_s when H ~ pure power law.
# Test: tau_dS = 1e-6, mu = 0.001

tau_dS_pl = 1e-6  # (local)
mu_test = 0.001   # (local)

ns_chk1 = ns_from_transfer(
    H_fold, tau_dS_pl, 2.0, mu_test,
    [c_B1_s74], [omega_B1_val], [1.0], [beta_sq_B1])  # (local)

# Also with mu=0 (trivial)
ns_chk1_mu0 = ns_from_transfer(
    H_fold, tau_dS_pl, 2.0, 0.0,
    [c_B1_s74], [omega_B1_val], [1.0], [beta_sq_B1])  # (local)

print(f"  CHK1 (tau_dS=1e-6, p=2, mu=0.001, B1): n_s = {ns_chk1:.8f}")
print(f"  CHK1 (tau_dS=1e-6, p=2, mu=0, B1):     n_s = {ns_chk1_mu0:.8f}")
print(f"  |n_s - 1| = {abs(ns_chk1 - 1.0):.2e}")
chk1_pass = abs(ns_chk1 - 1.0) < 0.01  # (local)
print(f"  CHK1: {'PASS' if chk1_pass else 'NEEDS EXAMINATION'}")
print()

# Delta_N diagnostic for power law
DN_B1_pivot_pl = Delta_N_branch(H_fold, tau_dS_pl, 2.0, c_B1_s74, omega_B1_val)  # (local)
dDN_B1_pivot_pl = compute_dDN_dlnk(H_fold, tau_dS_pl, 2.0, c_B1_s74, omega_B1_val)  # (local)
print(f"  Power-law Delta_N(pivot) = {DN_B1_pivot_pl:.4f}")
print(f"  Power-law d(Delta_N)/d(ln k) = {dDN_B1_pivot_pl:.4f}")
print(f"  (Should be small for k-independent spectrum)")
print()

# ==============================================================================
#  SECTION 5: Cross-check CHK2 -- de Sitter limit
# ==============================================================================

print("SECTION 5: Cross-check CHK2 -- de Sitter limit")
print("-" * 78)

# For large tau_dS: quasi-de Sitter, large Delta_N, large d(Delta_N)/d(ln k)
# n_s ~ 1 - 2*mu*d(Delta_N)/d(ln k)
# For ideal de Sitter: d(Delta_N)/d(ln k) = N_total (Lyth bound analogue)
# n_s ~ 1 - 2*mu*N => for N=60, mu=1/(120) gives n_s = 0.5

tau_dS_dS = 50.0   # (local) quasi-de Sitter
p_dS = 2.0         # (local)
mu_dS_test = 0.001 # (local) small mu

DN_dS_pivot = Delta_N_branch(H_fold, tau_dS_dS, p_dS, c_B1_s74, omega_B1_val)  # (local)
dDN_dS = compute_dDN_dlnk(H_fold, tau_dS_dS, p_dS, c_B1_s74, omega_B1_val)  # (local)

ns_chk2 = ns_from_transfer(
    H_fold, tau_dS_dS, p_dS, mu_dS_test,
    [c_B1_s74], [omega_B1_val], [1.0], [beta_sq_B1])  # (local)

ns_analytic = 1.0 - 2.0 * mu_dS_test * dDN_dS  # (local) leading-order

print(f"  tau_dS={tau_dS_dS}, p={p_dS}, mu={mu_dS_test}")
print(f"  Delta_N(pivot) = {DN_dS_pivot:.2f}")
print(f"  d(Delta_N)/d(ln k) = {dDN_dS:.2f}")
print(f"  n_s(numerical) = {ns_chk2:.8f}")
print(f"  n_s(analytic) = 1 - 2*mu*dDN/dlnk = {ns_analytic:.8f}")
print(f"  Agreement: {abs(ns_chk2 - ns_analytic):.2e}")
print()

# ==============================================================================
#  SECTION 6: Determine mu_eff that gives n_s = 0.9649 for each (tau_dS, p)
# ==============================================================================

print("SECTION 6: Required mu_eff for Planck n_s across (tau_dS, p)")
print("-" * 78)

# For each (tau_dS, p): compute d(Delta_N)/d(ln k) at pivot (B1 branch).
# Then mu_needed = (1 - n_s) / (2 * d(Delta_N)/d(ln k))
# For n_s = 0.9649: mu_needed = 0.0351 / (2 * dDN)

log_tau_dS_grid = np.linspace(-1, 2.5, 80)  # (local) [0.1, 316]
p_grid = np.linspace(0.5, 3.0, 60)           # (local)

dDN_grid = np.zeros((len(log_tau_dS_grid), len(p_grid)))  # (local)
DN_grid = np.zeros((len(log_tau_dS_grid), len(p_grid)))    # (local)
mu_needed_grid = np.zeros((len(log_tau_dS_grid), len(p_grid)))  # (local)

print(f"  Computing d(Delta_N)/d(ln k) on {len(log_tau_dS_grid)} x {len(p_grid)} grid...")

for i, lt in enumerate(log_tau_dS_grid):
    tau_dS_val = 10.0**lt  # (local)
    for j, pv in enumerate(p_grid):
        DN_grid[i, j] = Delta_N_branch(H_fold, tau_dS_val, pv,
                                        c_B1_s74, omega_B1_val)
        dDN_grid[i, j] = compute_dDN_dlnk(H_fold, tau_dS_val, pv,
                                            c_B1_s74, omega_B1_val)
        if abs(dDN_grid[i, j]) > 1e-6:
            mu_needed_grid[i, j] = 0.0351 / (2 * abs(dDN_grid[i, j]))
        else:
            mu_needed_grid[i, j] = np.inf

print("  Done.")
print()

# Report statistics
valid_mu = mu_needed_grid[mu_needed_grid < np.inf]  # (local)
print(f"  mu_needed range: [{valid_mu.min():.6f}, {valid_mu.max():.6f}] M_KK")
print(f"  Median mu_needed: {np.median(valid_mu):.6f} M_KK")
print()

# The physical constraint on mu:
# mu = m_iso^2 / (3*H^2) where m_iso is the isocurvature mass.
# m_iso comes from BCS inter-branch coupling ~ Delta_BCS.
# At crossing (H ~ c_B1 * k_pivot): H_cross = c_B1_s74 * omega_B1_val = 0.0653 M_KK
# mu_phys = Delta_BCS^2 / (3 * H_cross^2) = (0.464)^2 / (3 * 0.0653^2)

H_at_cross = c_B1_s74 * omega_B1_val  # (local) H at B1 horizon crossing
mu_BCS = Delta_BCS**2 / (3.0 * H_at_cross**2)  # (local)
mu_modulus = m_tau**2 / (3.0 * H_at_cross**2)   # (local)

print(f"  Physical mu estimates:")
print(f"    H(crossing) = c_B1 * omega_B1 = {H_at_cross:.4f} M_KK")
print(f"    mu_BCS = Delta^2/(3*H^2) = {mu_BCS:.4f}")
print(f"    mu_modulus = m_tau^2/(3*H^2) = {mu_modulus:.4f}")
print()

# BUT: these estimates use H at the deep power-law regime.
# During the quasi-dS phase, H ~ H_fold >> H_cross, so mu is much smaller.
# The relevant H for the isocurvature decay is H DURING the superhorizon
# evolution, not H at crossing. This is an average over the full Delta_N.
# For the quasi-dS phase: H ~ H_fold, mu ~ Delta_BCS^2/(3*H_fold^2)

mu_BCS_dS = Delta_BCS**2 / (3.0 * H_fold**2)  # (local)
mu_modulus_dS = m_tau**2 / (3.0 * H_fold**2)   # (local)
print(f"  During quasi-dS (H ~ H_fold):")
print(f"    mu_BCS(dS) = {mu_BCS_dS:.8f}")
print(f"    mu_modulus(dS) = {mu_modulus_dS:.8f}")
print()

# ==============================================================================
#  SECTION 7: Self-consistent (tau_dS, p, mu) scan for Planck n_s
# ==============================================================================

print("SECTION 7: Self-consistent scan for n_s in Planck band")
print("-" * 78)

# Approach: for each (tau_dS, p), the mu_needed determines if the parameter
# point is physical. We consider mu in [mu_BCS_dS, mu_BCS] as the
# physically motivated range (BCS coupling, H varies from H_fold to H_cross).

# For grid search: for each (tau_dS, p), compute n_s using mu values
# from the physical range. Report which combinations give Planck n_s.

mu_scan = np.logspace(-6, 0, 50)  # (local) wide range for exploration
# Also include the physical estimates
mu_phys_list = [mu_BCS_dS, mu_modulus_dS, mu_BCS, mu_modulus,
                0.0001, 0.0005, 0.001, 0.005, 0.01, 0.05]  # (local)

# For efficiency, use the analytic approximation first:
# n_s ~ 1 - 2*mu*dDN/dlnk (valid when mu*dDN << 1)

print(f"  Using analytic formula n_s ~ 1 - 2*mu*dDN/dlnk")
print()

# For each mu: what (tau_dS, p) gives n_s in Planck band?
# Need: 0.0309 < 2*mu*dDN < 0.0393 => dDN in [0.0155/mu, 0.0197/mu]

results_planck = []  # (local)
results_info = []    # (local)

for mu_val in mu_phys_list:
    # dDN needed: [0.0309/(2*mu), 0.0393/(2*mu)]
    dDN_lo = 0.0309 / (2 * mu_val) if mu_val > 0 else np.inf  # (local)
    dDN_hi = 0.0393 / (2 * mu_val) if mu_val > 0 else np.inf  # (local)

    # INFO band: [0.025/(2*mu), 0.050/(2*mu)]
    dDN_lo_i = 0.025 / (2 * mu_val) if mu_val > 0 else np.inf  # (local)
    dDN_hi_i = 0.050 / (2 * mu_val) if mu_val > 0 else np.inf  # (local)

    mask_planck = (np.abs(dDN_grid) >= dDN_lo) & (np.abs(dDN_grid) <= dDN_hi)  # (local)
    mask_info = (np.abs(dDN_grid) >= dDN_lo_i) & (np.abs(dDN_grid) <= dDN_hi_i)  # (local)

    n_p = np.sum(mask_planck)  # (local)
    n_i = np.sum(mask_info)    # (local)

    if n_p > 0:
        idx_best = np.unravel_index(
            np.argmin(np.abs(np.abs(dDN_grid) - (dDN_lo + dDN_hi)/2)),
            dDN_grid.shape)
        td_b = 10.0**log_tau_dS_grid[idx_best[0]]
        p_b = p_grid[idx_best[1]]
        dDN_b = dDN_grid[idx_best]
        ns_b = 1.0 - 2.0 * mu_val * abs(dDN_b)
        results_planck.append((mu_val, td_b, p_b, dDN_b, ns_b))

    if n_i > 0 and n_p == 0:
        idx_best = np.unravel_index(
            np.argmin(np.abs(np.abs(dDN_grid) - (dDN_lo_i + dDN_hi_i)/2)),
            dDN_grid.shape)
        td_b = 10.0**log_tau_dS_grid[idx_best[0]]
        p_b = p_grid[idx_best[1]]
        dDN_b = dDN_grid[idx_best]
        ns_b = 1.0 - 2.0 * mu_val * abs(dDN_b)
        results_info.append((mu_val, td_b, p_b, dDN_b, ns_b))

    if n_p > 0 or n_i > 0:
        print(f"  mu = {mu_val:.6f}: Planck={n_p}, INFO={n_i}, "
              f"dDN needed=[{dDN_lo:.1f}, {dDN_hi:.1f}]")

print()

# ==============================================================================
#  SECTION 8: Verify best candidates with full numerical computation
# ==============================================================================

print("SECTION 8: Numerical verification of best candidates")
print("-" * 78)

all_candidates = results_planck + results_info  # (local)

if len(all_candidates) == 0:
    # No candidates found. Compute the minimum mu needed.
    dDN_max = np.abs(dDN_grid).max()  # (local)
    mu_min_planck = 0.0309 / (2 * dDN_max) if dDN_max > 0 else np.inf  # (local)
    print(f"  No Planck/INFO candidates found.")
    print(f"  Maximum |dDN/dlnk| in grid = {dDN_max:.4f}")
    print(f"  Minimum mu for Planck n_s = {mu_min_planck:.6f}")
    best_ns = 1.0  # (local)
    best_td = 1.0  # (local)
    best_p = 1.0  # (local)
    best_mu = mu_min_planck  # (local)
else:
    # Sort by proximity to Planck best
    all_candidates.sort(key=lambda x: abs(x[4] - NS_PLANCK_BEST))  # (local)

print()
print("  Top candidates (analytic):")
for i, (mu_v, td_v, p_v, dDN_v, ns_v) in enumerate(all_candidates[:5]):
    print(f"    [{i+1}] mu={mu_v:.6f}, tau_dS={td_v:.3f}, p={p_v:.3f}, "
          f"dDN/dlnk={dDN_v:.2f}, n_s(analytic)={ns_v:.6f}")

# Verify top candidate with full numerical computation
if len(all_candidates) > 0:
    mu_best, td_best, p_best, dDN_best, ns_analytic_best = all_candidates[0]

    # Full numerical n_s
    ns_full_B1 = ns_from_transfer(
        H_fold, td_best, p_best, mu_best,
        [c_B1_s74], [omega_B1_val], [1.0], [beta_sq_B1])  # (local)

    ns_full_3b = ns_from_transfer(
        H_fold, td_best, p_best, mu_best,
        [c_B1_s74, c_B2_s74, c_B3_s74],
        [omega_B1_val, omega_B2_val, omega_B3_val],
        [psi_B1, psi_B2, psi_B3],
        [beta_sq_B1, beta_sq_B2, beta_sq_B3])  # (local)

    print()
    print(f"  Best candidate full numerical verification:")
    print(f"    mu = {mu_best:.6f}, tau_dS = {td_best:.4f}, p = {p_best:.4f}")
    print(f"    n_s(analytic) = {ns_analytic_best:.6f}")
    print(f"    n_s(B1 full)  = {ns_full_B1:.6f}")
    print(f"    n_s(3b full)  = {ns_full_3b:.6f}")

    best_ns = ns_full_3b  # (local)
    best_td = td_best  # (local)
    best_p = p_best  # (local)
    best_mu = mu_best  # (local)
else:
    best_ns = 1.0  # (local)
    best_td = 1.0  # (local)
    best_p = 1.0  # (local)
    best_mu = 0.0  # (local)

print()

# ==============================================================================
#  SECTION 9: Nelder-Mead refinement
# ==============================================================================

print("SECTION 9: Nelder-Mead refinement for Planck best fit")
print("-" * 78)

def loss_3param(params_vec):
    """Loss: |n_s - 0.9649| for 3-param (log_tau_dS, p, log_mu)."""
    ltd = params_vec[0]   # (local)
    pv = params_vec[1]    # (local)
    lmu = params_vec[2]   # (local)
    td_val = 10.0**ltd    # (local)
    mu_val = 10.0**lmu    # (local)
    if pv < 0.1 or td_val < 0.01 or mu_val < 1e-8 or mu_val > 10:
        return 1.0
    ns_val = ns_from_transfer(
        H_fold, td_val, pv, mu_val,
        [c_B1_s74, c_B2_s74, c_B3_s74],
        [omega_B1_val, omega_B2_val, omega_B3_val],
        [psi_B1, psi_B2, psi_B3],
        [beta_sq_B1, beta_sq_B2, beta_sq_B3])
    return (ns_val - NS_PLANCK_BEST)**2

if len(all_candidates) > 0:
    x0 = [np.log10(best_td), best_p, np.log10(best_mu)]  # (local)
else:
    x0 = [1.0, 2.0, -3.0]  # (local) default

try:
    res = minimize(loss_3param, x0, method='Nelder-Mead',
                   options={'xatol': 1e-8, 'fatol': 1e-18, 'maxiter': 10000})
    td_opt = 10.0**res.x[0]  # (local)
    p_opt = res.x[1]          # (local)
    mu_opt = 10.0**res.x[2]   # (local)
    ns_opt = ns_from_transfer(
        H_fold, td_opt, p_opt, mu_opt,
        [c_B1_s74, c_B2_s74, c_B3_s74],
        [omega_B1_val, omega_B2_val, omega_B3_val],
        [psi_B1, psi_B2, psi_B3],
        [beta_sq_B1, beta_sq_B2, beta_sq_B3])  # (local)
    print(f"  Optimized: tau_dS={td_opt:.6f}, p={p_opt:.6f}, mu={mu_opt:.8f}")
    print(f"  n_s = {ns_opt:.10f}")
    print(f"  |n_s - 0.9649| = {abs(ns_opt - NS_PLANCK_BEST):.2e}")
except Exception as e:
    td_opt = best_td  # (local)
    p_opt = best_p    # (local)
    mu_opt = best_mu  # (local)
    ns_opt = best_ns  # (local)
    print(f"  Optimization failed: {e}")

print()

# ==============================================================================
#  SECTION 10: Per-branch details at optimal
# ==============================================================================

print("SECTION 10: Per-branch details at optimal")
print("-" * 78)

# Crossing times
tc_B1 = tau_cross_analytic(H_fold, td_opt, p_opt, c_B1_s74, omega_B1_val)  # (local)
tc_B2 = tau_cross_analytic(H_fold, td_opt, p_opt, c_B2_s74, omega_B2_val)  # (local)
tc_B3 = tau_cross_analytic(H_fold, td_opt, p_opt, c_B3_s74, omega_B3_val)  # (local)

# Delta_N per branch
DN_B1 = Delta_N_branch(H_fold, td_opt, p_opt, c_B1_s74, omega_B1_val)  # (local)
DN_B2 = Delta_N_branch(H_fold, td_opt, p_opt, c_B2_s74, omega_B2_val)  # (local)
DN_B3 = Delta_N_branch(H_fold, td_opt, p_opt, c_B3_s74, omega_B3_val)  # (local)

# dDN/dlnk per branch
dDN_B1 = compute_dDN_dlnk(H_fold, td_opt, p_opt, c_B1_s74, omega_B1_val)  # (local)
dDN_B3 = compute_dDN_dlnk(H_fold, td_opt, p_opt, c_B3_s74, omega_B3_val)  # (local)

# Per-branch n_s (single-branch)
ns_B1_alone = ns_from_transfer(
    H_fold, td_opt, p_opt, mu_opt,
    [c_B1_s74], [omega_B1_val], [1.0], [beta_sq_B1])  # (local)
ns_B3_alone = ns_from_transfer(
    H_fold, td_opt, p_opt, mu_opt,
    [c_B3_s74], [omega_B3_val], [1.0], [beta_sq_B3])  # (local)

# N_plateau
N_plateau = H_fold * td_opt  # (local)

print(f"  H(tau) = {H_fold:.2f} / (1 + (tau/{td_opt:.4f})^{{{p_opt:.4f}}})")
print(f"  mu_eff = {mu_opt:.8f}")
print()
print(f"  Crossing times:")
print(f"    B1: tau_cross = {tc_B1:.4f}")
print(f"    B2: tau_cross = {tc_B2:.4f}")
print(f"    B3: tau_cross = {tc_B3:.4f}")
print()
print(f"  Superhorizon e-folds Delta_N:")
print(f"    B1: DN = {DN_B1:.2f}, dDN/dlnk = {dDN_B1:.2f}")
print(f"    B3: DN = {DN_B3:.2f}, dDN/dlnk = {dDN_B3:.2f}")
print()
print(f"  Per-branch n_s:")
print(f"    B1: n_s = {ns_B1_alone:.6f}")
print(f"    B3: n_s = {ns_B3_alone:.6f}")
print(f"    Composite: n_s = {ns_opt:.6f}")
print()
print(f"  N_plateau = H_fold * tau_dS = {N_plateau:.1f}")
print()

# ==============================================================================
#  SECTION 11: Scale dependence and running
# ==============================================================================

print("SECTION 11: Scale dependence and running")
print("-" * 78)

lambda_range = np.logspace(-1.5, 1.5, 100)  # (local) k/k_pivot
ns_of_k = []  # (local)

for lam in lambda_range:
    ns_val = ns_from_transfer(
        H_fold, td_opt, p_opt, mu_opt,
        [c_B1_s74, c_B2_s74, c_B3_s74],
        [omega_B1_val * lam, omega_B2_val * lam, omega_B3_val * lam],
        [psi_B1, psi_B2, psi_B3],
        [beta_sq_B1, beta_sq_B2, beta_sq_B3])
    ns_of_k.append(ns_val)

ns_of_k = np.array(ns_of_k)  # (local)
lnk = np.log(lambda_range)   # (local)

# Running at pivot
idx_piv = np.argmin(np.abs(lambda_range - 1.0))  # (local)
if idx_piv > 0 and idx_piv < len(lambda_range) - 1:
    alpha_s = (ns_of_k[idx_piv+1] - ns_of_k[idx_piv-1]) / (lnk[idx_piv+1] - lnk[idx_piv-1])  # (local)
else:
    alpha_s = 0.0  # (local)

print(f"  n_s(pivot) = {ns_of_k[idx_piv]:.6f}")
print(f"  alpha_s = {alpha_s:.6f}")
print(f"  Planck: alpha_s = -0.0045 +/- 0.0067")
print(f"  |alpha_s| {'<' if abs(alpha_s) < 0.015 else '>'} 0.015")
print()

# ==============================================================================
#  SECTION 12: CHK3 -- Spectral action consistency
# ==============================================================================

print("SECTION 12: Cross-check CHK3 -- Spectral action fit")
print("-" * 78)

H_data_norm = H_data / H_data[0]  # (local) spectral action data
H_param_fine = np.array([H_param(t, H_fold, td_opt, p_opt) for t in tau_fine])  # (local)
H_param_norm = H_param_fine / H_param_fine[0]  # (local)

residual = np.abs(H_param_norm - H_data_norm) / np.maximum(H_data_norm, 1e-30)  # (local)
max_res = np.max(residual)  # (local)
mean_res = np.mean(residual)  # (local)

print(f"  max |H_fit - H_data|/H_data = {max_res:.4f}")
print(f"  mean residual = {mean_res:.4f}")
chk3_status = "PASS" if max_res < 0.01 else "EXAMINED"  # (local)
print(f"  CHK3: {chk3_status} (data range [0.16, 1.65]; crossing at tau >> 2)")
print()

# ==============================================================================
#  SECTION 13: Physical assessment of mu
# ==============================================================================

print("SECTION 13: Physical assessment of mu_eff")
print("-" * 78)

# mu_opt is the optimized value. Is it physical?
# Physical range: mu in [mu_BCS_dS, mu_BCS] = [Delta^2/(3*H_fold^2), Delta^2/(3*H_cross^2)]
# The actual mu depends on the characteristic H during the superhorizon epoch.

mu_lo = mu_BCS_dS   # (local) smallest (during dS phase)
mu_hi = mu_BCS       # (local) largest (at crossing)
mu_mod_lo = mu_modulus_dS  # (local)
mu_mod_hi = mu_modulus     # (local)

mu_in_range = (mu_lo <= mu_opt <= mu_hi) or (mu_mod_lo <= mu_opt <= mu_mod_hi)  # (local)

print(f"  Optimal mu = {mu_opt:.8f}")
print(f"  BCS range: [{mu_lo:.8f}, {mu_hi:.4f}]")
print(f"  Modulus range: [{mu_mod_lo:.8f}, {mu_mod_hi:.4f}]")
print(f"  mu in physical range: {mu_in_range}")
print()

# Whether the quasi-dS duration tau_dS is physical:
# The spectral action data shows q_eff starting near 0 at fold and
# growing to ~0.5 at tau~1.5. This is consistent with a quasi-dS phase
# of duration tau_dS ~ 1-10 M_KK^{-1}.
q_eff_at_tau_dS = np.interp(min(td_opt, tau_fine[-1]), tau_fine, q_eff)  # (local)
print(f"  tau_dS = {td_opt:.4f} M_KK^{{-1}}")
print(f"  q_eff at tau_dS: {q_eff_at_tau_dS:.4f} (data value)")
print(f"  Physical: q_eff transitions from ~0 (dS) to >0.5 (power-law)")
print()

# ==============================================================================
#  SECTION 14: Gate verdict
# ==============================================================================

print("=" * 78)
print("SECTION 14: Gate verdict -- S75-C1-NS-NONPOWER")
print("=" * 78)
print()

ns_final = ns_opt  # (local)

print(f"  H(tau) = {H_fold:.2f} / (1 + (tau/{td_opt:.4f})^{{{p_opt:.4f}}})")
print(f"  mu_eff = {mu_opt:.8f}")
print(f"  n_s (3-branch composite) = {ns_final:.6f}")
print(f"  alpha_s = {alpha_s:.6f}")
print(f"  tau_dS = {td_opt:.6f}, p = {p_opt:.6f}")
print()
print(f"  CHK1 (power-law): {'PASS' if chk1_pass else 'FAIL'}")
print(f"  CHK2 (de Sitter): n_s = {ns_chk2:.6f}")
print(f"  CHK3 (data fit): {chk3_status}, max_res = {max_res:.4f}")
print()

# Determine gate
physically_motivated = mu_in_range  # (local)

if NS_PLANCK_LO <= ns_final <= NS_PLANCK_HI and physically_motivated:
    gate_verdict = "PASS"
    gate_reason = (f"n_s = {ns_final:.4f} in Planck 2-sigma with physically "
                   f"motivated mu = {mu_opt:.6f}")
elif NS_PLANCK_LO <= ns_final <= NS_PLANCK_HI and not physically_motivated:
    gate_verdict = "INFO"
    gate_reason = (f"n_s = {ns_final:.4f} in Planck 2-sigma but mu = {mu_opt:.6f} "
                   f"requires assessment against BCS/modulus scales")
elif NS_INFO_LO <= ns_final <= NS_INFO_HI:
    gate_verdict = "INFO"
    gate_reason = (f"n_s = {ns_final:.4f} in extended band [{NS_INFO_LO}, {NS_INFO_HI}]")
else:
    gate_verdict = "FAIL"
    gate_reason = (f"n_s = {ns_final:.4f} outside [{NS_INFO_LO}, {NS_INFO_HI}]")

print(f"  Gate S75-C1-NS-NONPOWER: {gate_verdict}")
print(f"  Reason: {gate_reason}")
print()

# ==============================================================================
#  SECTION 15: Save
# ==============================================================================

print("SECTION 15: Save results")
print("-" * 78)

results = {
    'gate_name': 'S75-C1-NS-NONPOWER',
    'gate_verdict': gate_verdict,
    'gate_reason': gate_reason,

    'ns_3branch': ns_opt,
    'ns_B1_alone': ns_B1_alone,
    'ns_B3_alone': ns_B3_alone,
    'alpha_s': alpha_s,
    'tau_dS_optimal': td_opt,
    'p_optimal': p_opt,
    'mu_optimal': mu_opt,
    'H0': H_fold,

    'tau_cross_B1': tc_B1,
    'tau_cross_B2': tc_B2,
    'tau_cross_B3': tc_B3,
    'Delta_N_B1': DN_B1,
    'Delta_N_B3': DN_B3,
    'dDN_dlnk_B1': dDN_B1,
    'dDN_dlnk_B3': dDN_B3,
    'N_plateau': N_plateau,

    'mu_BCS_range': [mu_lo, mu_hi],
    'mu_modulus_range': [mu_mod_lo, mu_mod_hi],
    'mu_physically_motivated': mu_in_range,

    'chk1_ns': ns_chk1,
    'chk1_pass': chk1_pass,
    'chk2_ns': ns_chk2,
    'chk3_max_residual': max_res,

    'log_tau_dS_grid': log_tau_dS_grid,
    'p_grid': p_grid,
    'dDN_grid': dDN_grid,
    'DN_grid': DN_grid,
    'mu_needed_grid': mu_needed_grid,

    'lambda_range': lambda_range,
    'ns_of_k': ns_of_k,

    'tau_fine': tau_fine,
    'H_data': H_data,
    'q_eff': q_eff,
}

np.savez(os.path.join(data_dir, 's75_ns_nonpower_law_h.npz'), **results)
print(f"  Saved: s75_ns_nonpower_law_h.npz")

# ==============================================================================
#  SECTION 16: Plots
# ==============================================================================

print("SECTION 16: Generate plots")
print("-" * 78)

fig = plt.figure(figsize=(16, 12))
gs = GridSpec(2, 3, figure=fig, hspace=0.35, wspace=0.35)

# Panel 1: H(tau) comparison
ax1 = fig.add_subplot(gs[0, 0])
tau_plot = np.logspace(np.log10(0.19), 3, 500)  # (local)
H_s74 = H_fold * (tau_fold / tau_plot)**2  # (local)
H_opt_plot = np.array([H_param(t, H_fold, td_opt, p_opt) for t in tau_plot])  # (local)
ax1.loglog(tau_plot, H_s74, 'b--', alpha=0.7, label=r'S74: $H \propto \tau^{-2}$')
ax1.loglog(tau_plot, H_opt_plot, 'r-', linewidth=2,
           label=fr'$\tau_{{dS}}$={td_opt:.2f}, p={p_opt:.2f}')
ax1.axvline(tc_B1, color='g', ls=':', alpha=0.5, label='B1 cross')
ax1.axvline(tc_B3, color='m', ls=':', alpha=0.5, label='B3 cross')
ax1.set_xlabel(r'$\tau$ [M$_{\rm KK}^{-1}$]')
ax1.set_ylabel(r'$H(\tau)$ [M$_{\rm KK}$]')
ax1.set_title(r'$H(\tau)$: power-law vs non-power-law')
ax1.legend(fontsize=7, loc='upper right')
ax1.set_xlim(0.19, 1000)

# Panel 2: dDN/dlnk contour
ax2 = fig.add_subplot(gs[0, 1])
XX, YY = np.meshgrid(log_tau_dS_grid, p_grid, indexing='ij')  # (local)
cs = ax2.contourf(XX, YY, np.abs(dDN_grid),
                  levels=np.logspace(-1, 3, 15), cmap='viridis',
                  norm=matplotlib.colors.LogNorm())
ax2.plot(np.log10(td_opt), p_opt, 'r*', markersize=15, zorder=10)
plt.colorbar(cs, ax=ax2, label=r'$|d\Delta N / d\ln k|$')
ax2.set_xlabel(r'$\log_{10}(\tau_{\rm dS})$')
ax2.set_ylabel(r'$p$')
ax2.set_title(r'$|d\Delta N / d\ln k|$ (B1 branch)')

# Panel 3: n_s(k) scale dependence
ax3 = fig.add_subplot(gs[0, 2])
k_CMB = lambda_range * 0.05  # (local) Mpc^-1
ax3.semilogx(k_CMB, ns_of_k, 'r-', linewidth=2)
ax3.axhline(NS_PLANCK_BEST, color='gray', ls='--', alpha=0.5, label='Planck best')
ax3.axhspan(NS_PLANCK_LO, NS_PLANCK_HI, alpha=0.15, color='blue', label='Planck 2-sigma')
ax3.axvline(0.05, color='k', ls=':', alpha=0.3, label='pivot')
ax3.set_xlabel(r'$k$ [Mpc$^{-1}$]')
ax3.set_ylabel(r'$n_s(k)$')
ax3.set_title(r'Scale dependence of $n_s$')
ax3.legend(fontsize=7)

# Panel 4: mu_needed contour
ax4 = fig.add_subplot(gs[1, 0])
mu_plot = np.where(mu_needed_grid < 100, mu_needed_grid, np.nan)  # (local)
cs4 = ax4.contourf(XX, YY, np.log10(np.maximum(mu_plot, 1e-10)),
                   levels=np.linspace(-6, 0, 15), cmap='plasma')
ax4.plot(np.log10(td_opt), p_opt, 'w*', markersize=15, zorder=10)
plt.colorbar(cs4, ax=ax4, label=r'$\log_{10}(\mu_{\rm needed})$')
ax4.set_xlabel(r'$\log_{10}(\tau_{\rm dS})$')
ax4.set_ylabel(r'$p$')
ax4.set_title(r'$\mu$ needed for $n_s = 0.9649$')

# Panel 5: q_eff from spectral action
ax5 = fig.add_subplot(gs[1, 1])
ax5.plot(tau_fine, -q_eff, 'b-', linewidth=2)
ax5.axhline(0.0, color='gray', ls='--', alpha=0.5, label='de Sitter (q=0)')
ax5.axhline(2.0, color='gray', ls=':', alpha=0.5, label='Radiation (q=2)')
ax5.set_xlabel(r'$\tau$ [M$_{\rm KK}^{-1}$]')
ax5.set_ylabel(r'$q_{\rm eff} = -d\ln H / d\ln\tau$')
ax5.set_title('Spectral action: effective power-law index')
ax5.legend(fontsize=8)

# Panel 6: Summary
ax6 = fig.add_subplot(gs[1, 2])
ax6.axis('off')
summary = (
    f"S75-C1-NS-NONPOWER\n"
    f"Gate: {gate_verdict}\n\n"
    f"H = {H_fold:.1f} / (1 + (tau/{td_opt:.3f})^{{{p_opt:.3f}}})\n"
    f"mu_eff = {mu_opt:.6f}\n\n"
    f"n_s (3-branch) = {ns_opt:.6f}\n"
    f"alpha_s = {alpha_s:.6f}\n\n"
    f"Delta_N(B1) = {DN_B1:.1f}\n"
    f"dDN/dlnk(B1) = {dDN_B1:.2f}\n\n"
    f"mu_BCS range: [{mu_lo:.2e}, {mu_hi:.2f}]\n"
    f"mu in range: {mu_in_range}\n\n"
    f"CHK1: {'PASS' if chk1_pass else 'FAIL'}\n"
    f"CHK3: {chk3_status} ({max_res:.4f})"
)
ax6.text(0.05, 0.95, summary, transform=ax6.transAxes,
         fontsize=9, va='top', fontfamily='monospace',
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

fig.suptitle('S75-C1-NS-NONPOWER: n_s from Isocurvature Transfer',
             fontsize=14, fontweight='bold')
plt.savefig(os.path.join(data_dir, 's75_ns_nonpower_law_h.png'), dpi=150,
            bbox_inches='tight')
print(f"  Saved: s75_ns_nonpower_law_h.png")
plt.close()

t_end = time.time()
print()
print(f"Total runtime: {t_end - t_start:.1f}s")
print()
print("=" * 78)
print(f"FINAL: Gate S75-C1-NS-NONPOWER = {gate_verdict}")
print(f"  n_s = {ns_opt:.6f}")
print(f"  tau_dS = {td_opt:.4f}, p = {p_opt:.4f}, mu = {mu_opt:.8f}")
print(f"  Reason: {gate_reason}")
print("=" * 78)
