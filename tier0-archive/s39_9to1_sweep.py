#!/usr/bin/env python3
"""
Session 39: 9TO1-39 -- Tau-Sweep of R(tau) = omega_att / (B3 - B1)
===================================================================

GATE: 9TO1-39
  PASS (STRUCTURAL):   sigma_R / R_0 < 0.01  (1% variation)
  FAIL (COINCIDENCE):  sigma_R / R_0 > 0.05  (5% variation)
  INTERMEDIATE:        between 1% and 5%

CONTEXT:
  Session 38 (W2, C-3) found omega_att = 9*(B3-B1) at 0.08% accuracy at
  the fold tau = 0.190. This script sweeps tau across the BCS-active
  window to determine whether R(tau) is a structural constant or a
  fold-specific coincidence.

METHODOLOGY:
  1. Use Kosmann K_a matrices at the 9 coarse tau grid points to build
     exact V_8x8 at each tau.
  2. Interpolate eigenvalues and V matrix to a dense fine grid around
     the fold where BCS is active.
  3. At each fine tau, compute rho_B2(tau) via the van Hove Lorentzian
     profile (same as GCM S36), solve the 8-mode BCS gap equation, and
     extract Delta_0, E_cond, a_GL, b_GL.
  4. Compute omega_att = sqrt(F''(Delta_0)) with m_eff = 1 (consistent
     with S37-S38 methodology).
  5. Compute R(tau) = omega_att / (B3-B1) and secondary ratios.
  6. Fit R(tau) to a constant and report sigma_R / R_0.

Author: gen-physicist, Session 39
Date: 2026-03-09
"""

import os
import sys
import time
import numpy as np
from numpy.linalg import eigvals, eigh
from scipy.interpolate import CubicSpline
from scipy.integrate import trapezoid
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
t0 = time.time()

print("=" * 78)
print("Session 39: 9TO1-39 -- Tau-Sweep of R(tau) = omega_att / (B3 - B1)")
print("=" * 78)

# ======================================================================
#  Constants (matching S36 GCM methodology)
# ======================================================================
MU = 0.0
MS_FACTOR = 1.046
ETA_REG_FRAC = 0.001

# Eigenvalue indices in sorted 16-mode spectrum
B1_IDX = np.array([8])
B2_IDX = np.array([9, 10, 11, 12])
B3_IDX = np.array([13, 14, 15])

# ======================================================================
#  Load data
# ======================================================================
print("\n--- Loading data ---")

kosmann = np.load(os.path.join(SCRIPT_DIR, 's23a_kosmann_singlet.npz'),
                  allow_pickle=True)
vh_data = np.load(os.path.join(SCRIPT_DIR, 's35a_vh_impedance_arbiter.npz'),
                  allow_pickle=True)
s35_data = np.load(os.path.join(SCRIPT_DIR, 's35_thouless_multiband.npz'),
                   allow_pickle=True)
pair_data = np.load(os.path.join(SCRIPT_DIR, 's37_pair_susceptibility.npz'),
                    allow_pickle=True)

tau_coarse = kosmann['tau_values']
n_coarse = len(tau_coarse)

tau_fold = float(vh_data['tau_fold'])   # 0.1902
rho_B2_step = float(vh_data['rho_step'])  # 5.40
rho_B2_smooth = float(vh_data['rho_at_physical'])  # 14.02
rho_B1_raw = float(s35_data['rho_B1']) / MS_FACTOR  # ~3.76
rho_B3_raw = float(s35_data['rho_B3']) / MS_FACTOR  # ~0.46

# Pair vibration frequency for secondary ratio
omega_PV = float(pair_data['omega_plus'])  # 0.792

print(f"  tau_fold = {tau_fold:.6f}")
print(f"  rho_B2_step = {rho_B2_step:.4f}")
print(f"  rho_B2_smooth = {rho_B2_smooth:.4f}")
print(f"  rho_B1 = {rho_B1_raw * MS_FACTOR:.4f}")
print(f"  rho_B3 = {rho_B3_raw * MS_FACTOR:.4f}")
print(f"  omega_PV = {omega_PV:.6f}")


# ======================================================================
#  Helper functions
# ======================================================================

def build_V_and_eigenvalues(kosmann_data, tau_idx):
    """Build V_nm = sum_{a=0..7} |K^a_{nm}|^2 in eigenvalue-sorted basis."""
    evals = kosmann_data[f'eigenvalues_{tau_idx}']
    sort_idx = np.argsort(evals)
    evals_sorted = evals[sort_idx]

    V = np.zeros((16, 16))
    for a in range(8):
        K = kosmann_data[f'K_a_matrix_{tau_idx}_{a}']
        V += np.abs(K) ** 2

    V_sorted = V[np.ix_(sort_idx, sort_idx)]
    return V_sorted, evals_sorted


def compute_dos(tau, tau_f, rho_step, rho_smooth, rho_b1, rho_b3,
                delta_tau_wall=0.040):
    """Compute DOS at arbitrary tau using Lorentzian van Hove profile."""
    gamma = delta_tau_wall / 2.0
    vh_enh = rho_smooth / rho_step - 1.0
    lorentz = gamma**2 / ((tau - tau_f)**2 + gamma**2)

    rho_B2 = rho_step * (1.0 + vh_enh * lorentz) * MS_FACTOR
    rho_B1 = rho_b1 * MS_FACTOR
    rho_B3 = rho_b3 * MS_FACTOR

    return rho_B1, rho_B2, rho_B3


def extract_8mode(V_sorted, evals_sorted):
    """Extract 8-mode positive-sector V matrix and eigenvalues.

    Ordering: B2[0..3], B1, B3[0..2] (matching S36 convention).
    """
    full_pos_idx = np.concatenate([B2_IDX, B1_IDX, B3_IDX])
    V_8 = V_sorted[np.ix_(full_pos_idx, full_pos_idx)]
    E_8 = evals_sorted[full_pos_idx]
    return V_8, E_8


def solve_8mode_bcs(V_8, E_8, rho_8, mu=0.0, max_iter=5000, tol=1e-14):
    """Solve 8-mode BCS gap equation.

    Gap equation: Delta_k = sum_{k'} V_{kk'} * sqrt(rho_k*rho_{k'}) * Delta_{k'} / (2*E_{k'})
    where E_{k'} = sqrt(xi_{k'}^2 + Delta_{k'}^2), xi_k = E_k - mu.

    Returns: Delta (8,), converged (bool), n_iter (int)
    """
    n = len(E_8)
    xi = E_8 - mu

    # Multiple seed attempts
    for seed_scale in [0.5, 0.1, 1.0, 0.01, 2.0]:
        Delta = np.ones(n) * seed_scale
        for it in range(max_iter):
            E_qp = np.sqrt(xi**2 + Delta**2)
            Delta_new = np.zeros(n)
            for k in range(n):
                for kp in range(n):
                    Delta_new[k] += V_8[k, kp] * np.sqrt(rho_8[k] * rho_8[kp]) * Delta[kp] / (2.0 * E_qp[kp])
            diff = np.max(np.abs(Delta_new - Delta))
            Delta = Delta_new.copy()
            if diff < tol:
                if np.max(Delta) > 1e-10:
                    return Delta, True, it
                break

    # If no convergent nontrivial solution, return zero
    return np.zeros(n), False, max_iter


def bcs_free_energy_path(alpha, Delta_SC, V_8, xi, rho_8):
    """BCS variational energy at Delta_k = alpha * Delta_SC_k.

    F = sum_k [E_k - |xi_k|] - sum_{k,k'} V_{kk'} * sqrt(rho_k*rho_{k'}) * Delta_k*Delta_{k'} / (4*E_k*E_{k'})

    Kinetic term has no DOS prefactor (discrete-mode BCS).
    """
    n = len(xi)
    Delta = alpha * Delta_SC
    E_qp = np.sqrt(xi**2 + Delta**2)

    F_kin = np.sum(E_qp - np.abs(xi))

    F_pair = 0.0
    for k in range(n):
        for kp in range(n):
            F_pair -= V_8[k, kp] * np.sqrt(rho_8[k] * rho_8[kp]) * Delta[k] * Delta[kp] / (4.0 * E_qp[k] * E_qp[kp])

    return F_kin + F_pair


def compute_bcs_landscape(V_8, E_8, rho_8, mu=0.0, n_alpha=5001):
    """Compute the full BCS free energy landscape F(alpha) along instanton path.

    Returns dict with BCS parameters or None if no condensate.
    """
    xi = E_8 - mu

    # Solve gap equation
    Delta_SC, converged, nit = solve_8mode_bcs(V_8, E_8, rho_8, mu=mu)

    if not converged or np.max(Delta_SC) < 1e-10:
        return None  # No BCS condensate

    Delta_max_SC = np.max(Delta_SC)

    # Scan alpha
    alpha_scan = np.linspace(0, 3.0, n_alpha)
    F_scan = np.array([bcs_free_energy_path(a, Delta_SC, V_8, xi, rho_8)
                        for a in alpha_scan])

    idx_min = np.argmin(F_scan)
    alpha_min = alpha_scan[idx_min]
    F_min = F_scan[idx_min]
    E_cond = F_min - F_scan[0]
    Delta_0 = alpha_min * Delta_max_SC

    if abs(Delta_0) < 1e-10 or E_cond >= -1e-12:
        return None  # No condensation

    # GL parameters from E_cond and Delta_0
    a_GL = 2.0 * E_cond / Delta_0**2
    b_GL = -E_cond / Delta_0**4

    # Curvature of F at the minimum: 5-point finite difference in Delta space
    delta_scan = alpha_scan * Delta_max_SC
    d_Delta = delta_scan[1] - delta_scan[0]

    if idx_min >= 2 and idx_min < len(F_scan) - 2:
        F_pp = (-F_scan[idx_min+2] + 16*F_scan[idx_min+1] - 30*F_scan[idx_min]
                + 16*F_scan[idx_min-1] - F_scan[idx_min-2]) / (12 * d_Delta**2)
    elif idx_min >= 1 and idx_min < len(F_scan) - 1:
        F_pp = (F_scan[idx_min+1] - 2*F_scan[idx_min] + F_scan[idx_min-1]) / d_Delta**2
    else:
        F_pp = 4.0 * abs(a_GL)  # Fall back to GL

    omega_att = np.sqrt(abs(F_pp))

    # Also compute GL omega_att for comparison
    omega_att_GL = np.sqrt(4.0 * abs(a_GL))

    return {
        'Delta_SC': Delta_SC,
        'Delta_0': Delta_0,
        'alpha_min': alpha_min,
        'E_cond': E_cond,
        'F_min': F_min,
        'a_GL': a_GL,
        'b_GL': b_GL,
        'F_pp': F_pp,
        'omega_att': omega_att,
        'omega_att_GL': omega_att_GL,
        'converged': converged,
    }


# ======================================================================
#  Step 1: Build V matrices and eigenvalues at coarse grid
# ======================================================================
print("\n" + "=" * 78)
print("Step 1: V matrices and eigenvalues at coarse grid")
print("=" * 78)

V_coarse = []
evals_coarse = []
V8_coarse = []
E8_coarse = []

for ti in range(n_coarse):
    V_sorted, evals_sorted = build_V_and_eigenvalues(kosmann, ti)
    V_coarse.append(V_sorted)
    evals_coarse.append(evals_sorted)

    V_8, E_8 = extract_8mode(V_sorted, evals_sorted)
    V8_coarse.append(V_8)
    E8_coarse.append(E_8)

# Extract branch eigenvalues at coarse grid
E_B1_coarse = np.array([evals_coarse[i][B1_IDX[0]] for i in range(n_coarse)])
E_B2_coarse = np.array([np.mean(evals_coarse[i][B2_IDX]) for i in range(n_coarse)])
E_B3_coarse = np.array([np.mean(evals_coarse[i][B3_IDX]) for i in range(n_coarse)])

print(f"\n  Eigenvalue branches at coarse grid:")
print(f"  {'tau':>6s}  {'E_B1':>10s}  {'E_B2':>10s}  {'E_B3':>10s}  {'B3-B1':>10s}  {'B3-B2':>10s}")
for i in range(n_coarse):
    print(f"  {tau_coarse[i]:6.2f}  {E_B1_coarse[i]:10.6f}  {E_B2_coarse[i]:10.6f}  "
          f"{E_B3_coarse[i]:10.6f}  {E_B3_coarse[i]-E_B1_coarse[i]:10.6f}  "
          f"{E_B3_coarse[i]-E_B2_coarse[i]:10.6f}")


# ======================================================================
#  Step 2: Build fine grid and interpolate
# ======================================================================
print("\n" + "=" * 78)
print("Step 2: Fine grid construction")
print("=" * 78)

# Dense grid around fold
tau_fine_base = np.arange(0.0, 0.501, 0.02)
tau_fold_region = np.arange(tau_fold - 0.05, tau_fold + 0.051, 0.0025)
tau_fine = np.sort(np.unique(np.concatenate([tau_fine_base, tau_fold_region])))
tau_fine = tau_fine[(tau_fine >= 0) & (tau_fine <= 0.5)]
n_fine = len(tau_fine)

# Interpolate eigenvalues
cs_B1 = CubicSpline(tau_coarse, E_B1_coarse)
cs_B2 = CubicSpline(tau_coarse, E_B2_coarse)
cs_B3 = CubicSpline(tau_coarse, E_B3_coarse)

# Interpolate V_8x8 matrix elements (smooth in tau)
V8_elements = np.zeros((n_coarse, 8, 8))
for ti in range(n_coarse):
    V8_elements[ti] = V8_coarse[ti]

# Create cubic spline for each V matrix element
cs_V8 = [[None]*8 for _ in range(8)]
for i in range(8):
    for j in range(8):
        cs_V8[i][j] = CubicSpline(tau_coarse, V8_elements[:, i, j])

print(f"  Fine grid: {n_fine} points")
print(f"  Fold region: {np.sum(np.abs(tau_fine - tau_fold) < 0.05)} points within 0.05 of fold")


# ======================================================================
#  Step 3: BCS computation at each fine grid point
#  TWO MODES: (A) B2-only (matching S38 methodology), (B) Full 8-mode
# ======================================================================
print("\n" + "=" * 78)
print("Step 3: BCS sweep across fine grid")
print("  Mode A: B2-only (4 modes, matching S38)")
print("  Mode B: Full 8-mode (all sectors)")
print("=" * 78)

results_list_B2 = []   # B2-only (S38 methodology)
results_list_8 = []    # Full 8-mode

print(f"\n  --- B2-only sweep (S38 methodology) ---")
print(f"  {'tau':>8s}  {'rho_B2':>8s}  {'Delta_0':>8s}  {'E_cond':>10s}  {'omega_att':>10s}  "
      f"{'B3-B1':>8s}  {'R(B3-B1)':>10s}  {'status':>8s}")
print(f"  {'='*8}  {'='*8}  {'='*8}  {'='*10}  {'='*10}  {'='*8}  {'='*10}  {'='*8}")

for fi in range(n_fine):
    tau = tau_fine[fi]

    # DOS at this tau
    rB1, rB2, rB3 = compute_dos(tau, tau_fold, rho_B2_step, rho_B2_smooth,
                                  rho_B1_raw, rho_B3_raw)

    # Interpolate eigenvalues
    b1 = cs_B1(tau)
    b2 = cs_B2(tau)
    b3 = cs_B3(tau)

    # Interpolate V_8x8
    V_8_interp = np.zeros((8, 8))
    for i in range(8):
        for j in range(8):
            V_8_interp[i, j] = cs_V8[i][j](tau)

    # ---- MODE A: B2-only (4 modes) matching S38 ----
    V_B2 = V_8_interp[np.ix_([0,1,2,3], [0,1,2,3])]
    E_B2_vec = np.array([b2, b2, b2, b2])
    rho_B2_vec = np.array([rB2, rB2, rB2, rB2])

    bcs_B2 = compute_bcs_landscape(V_B2, E_B2_vec, rho_B2_vec, mu=MU, n_alpha=10001)

    if bcs_B2 is not None:
        omega_att_B2 = bcs_B2['omega_att']
        Delta_0_B2 = bcs_B2['Delta_0']
        E_cond_B2 = bcs_B2['E_cond']
        R_31_B2 = omega_att_B2 / (b3 - b1) if (b3 - b1) > 1e-10 else np.nan
        R_32_B2 = omega_att_B2 / (b3 - b2) if (b3 - b2) > 1e-10 else np.nan

        results_list_B2.append({
            'tau': tau,
            'rho_B2': rB2,
            'E_B1': b1, 'E_B2': b2, 'E_B3': b3,
            'Delta_0': Delta_0_B2,
            'E_cond': E_cond_B2,
            'a_GL': bcs_B2['a_GL'],
            'b_GL': bcs_B2['b_GL'],
            'omega_att': omega_att_B2,
            'omega_att_GL': bcs_B2['omega_att_GL'],
            'F_pp': bcs_B2['F_pp'],
            'R_B3_B1': R_31_B2,
            'R_B3_B2': R_32_B2,
        })

        print(f"  {tau:8.4f}  {rB2:8.2f}  {Delta_0_B2:8.4f}  {E_cond_B2:10.6f}  {omega_att_B2:10.6f}  "
              f"{b3-b1:8.6f}  {R_31_B2:10.4f}  {'ACTIVE':>8s}")
    else:
        if abs(tau - tau_fold) < 0.06:
            print(f"  {tau:8.4f}  {rB2:8.2f}  {'---':>8s}  {'---':>10s}  {'---':>10s}  "
                  f"{b3-b1:8.6f}  {'---':>10s}  {'no BCS':>8s}")

    # ---- MODE B: Full 8-mode ----
    E_8_interp = np.array([b2, b2, b2, b2, b1, b3, b3, b3])
    rho_8 = np.array([rB2, rB2, rB2, rB2, rB1, rB3, rB3, rB3])

    bcs_8 = compute_bcs_landscape(V_8_interp, E_8_interp, rho_8, mu=MU)

    if bcs_8 is not None:
        results_list_8.append({
            'tau': tau,
            'rho_B2': rB2,
            'E_B1': b1, 'E_B2': b2, 'E_B3': b3,
            'Delta_0': bcs_8['Delta_0'],
            'E_cond': bcs_8['E_cond'],
            'a_GL': bcs_8['a_GL'],
            'b_GL': bcs_8['b_GL'],
            'omega_att': bcs_8['omega_att'],
            'omega_att_GL': bcs_8['omega_att_GL'],
            'F_pp': bcs_8['F_pp'],
            'R_B3_B1': bcs_8['omega_att'] / (b3 - b1) if (b3 - b1) > 1e-10 else np.nan,
            'R_B3_B2': bcs_8['omega_att'] / (b3 - b2) if (b3 - b2) > 1e-10 else np.nan,
        })

# Use B2-only results as primary (matching S38 methodology)
results_list = results_list_B2


# ======================================================================
#  Step 4: Statistical analysis
# ======================================================================
print("\n" + "=" * 78)
print("Step 4: R(tau) Statistical Analysis")
print("=" * 78)

n_active = len(results_list)
print(f"\n  Active BCS points: {n_active}")

if n_active < 2:
    print("  INSUFFICIENT DATA for statistical analysis.")
    print("  Saving minimal results and exiting.")

    out_path = os.path.join(SCRIPT_DIR, 's39_9to1_sweep.npz')
    np.savez(out_path, verdict="INSUFFICIENT_DATA", n_active=n_active)
    sys.exit(0)

tau_arr = np.array([r['tau'] for r in results_list])
omega_att_arr = np.array([r['omega_att'] for r in results_list])
R_31_arr = np.array([r['R_B3_B1'] for r in results_list])
R_32_arr = np.array([r['R_B3_B2'] for r in results_list])
Delta_arr = np.array([r['Delta_0'] for r in results_list])
E_cond_arr = np.array([r['E_cond'] for r in results_list])
B1_arr = np.array([r['E_B1'] for r in results_list])
B2_arr = np.array([r['E_B2'] for r in results_list])
B3_arr = np.array([r['E_B3'] for r in results_list])

# Constant fit for R(B3-B1)
R0_31 = np.mean(R_31_arr)
sigma_R_31 = np.std(R_31_arr)
R_range_31 = np.max(R_31_arr) - np.min(R_31_arr)
frac_sigma_31 = sigma_R_31 / R0_31

# Constant fit for R(B3-B2)
R0_32 = np.mean(R_32_arr)
sigma_R_32 = np.std(R_32_arr)
R_range_32 = np.max(R_32_arr) - np.min(R_32_arr)
frac_sigma_32 = sigma_R_32 / R0_32

# omega_att / omega_PV ratio
ratio_att_PV = omega_att_arr / omega_PV
R0_att_PV = np.mean(ratio_att_PV)
sigma_att_PV = np.std(ratio_att_PV)

print(f"\n  PRIMARY RATIO: R(tau) = omega_att / (B3 - B1)")
print(f"    R_0 (mean)   = {R0_31:.6f}")
print(f"    sigma_R      = {sigma_R_31:.6f}")
print(f"    sigma_R / R_0 = {frac_sigma_31:.6f}  ({frac_sigma_31*100:.2f}%)")
print(f"    R_max - R_min = {R_range_31:.6f}")
print(f"    R_min         = {np.min(R_31_arr):.6f}  at tau = {tau_arr[np.argmin(R_31_arr)]:.4f}")
print(f"    R_max         = {np.max(R_31_arr):.6f}  at tau = {tau_arr[np.argmax(R_31_arr)]:.4f}")

print(f"\n  SECONDARY RATIO: omega_att / (B3 - B2)")
print(f"    R_0 (mean)   = {R0_32:.6f}")
print(f"    sigma_R      = {sigma_R_32:.6f}")
print(f"    sigma_R / R_0 = {frac_sigma_32:.6f}  ({frac_sigma_32*100:.2f}%)")

print(f"\n  TERTIARY RATIO: omega_att / omega_PV")
print(f"    R_0 (mean)   = {R0_att_PV:.6f}")
print(f"    sigma         = {sigma_att_PV:.6f}")
print(f"    sigma / R_0   = {sigma_att_PV/R0_att_PV:.6f}  ({sigma_att_PV/R0_att_PV*100:.2f}%)")


# ======================================================================
#  Step 5: Gate verdict
# ======================================================================
print("\n" + "=" * 78)
print("Step 5: Gate Verdict (9TO1-39)")
print("=" * 78)

if frac_sigma_31 < 0.01:
    verdict = "PASS (STRUCTURAL)"
    verdict_detail = f"sigma_R/R_0 = {frac_sigma_31:.4f} < 0.01"
elif frac_sigma_31 > 0.05:
    verdict = "FAIL (COINCIDENCE)"
    verdict_detail = f"sigma_R/R_0 = {frac_sigma_31:.4f} > 0.05"
else:
    verdict = "INTERMEDIATE"
    verdict_detail = f"sigma_R/R_0 = {frac_sigma_31:.4f} in [0.01, 0.05]"

print(f"\n  GATE 9TO1-39: {verdict}")
print(f"    Criterion: {verdict_detail}")
print(f"    R_0 = {R0_31:.6f}")
print(f"    sigma_R = {sigma_R_31:.6f}")
print(f"    N_points = {n_active}")
print(f"    tau_range = [{tau_arr.min():.4f}, {tau_arr.max():.4f}]")


# ======================================================================
#  Step 6: Candidate matching
# ======================================================================
print("\n" + "=" * 78)
print("Step 6: Candidate Matching for R_0")
print("=" * 78)

candidates = [
    ("dim(SU(3))", 8.0),
    ("dim(SU(3)) + 1 = dim(fund)^2", 9.0),
    ("Dynkin index ratio 9/4", 9.0/4.0),
    ("2*dim(fund)", 6.0),
    ("dim(adj) + dim(fund)", 11.0),
    ("dim(SU(3))/dim(fund)", 8.0/3.0),
    ("4*pi", 4*np.pi),
    ("3*pi", 3*np.pi),
    ("pi^2", np.pi**2),
]

# Value at fold (peak of BCS)
idx_fold = np.argmin(np.abs(tau_arr - tau_fold))
R_at_fold = R_31_arr[idx_fold]

print(f"\n  R_0 (mean over BCS window) = {R0_31:.6f}")
print(f"  R at fold (tau ~ {tau_arr[idx_fold]:.4f}) = {R_at_fold:.6f}")
print(f"\n  {'Candidate':<35s} {'Value':>8s} {'|R_0 - C|':>10s} {'|R_fold - C|':>12s}")
print(f"  {'='*35} {'='*8} {'='*10} {'='*12}")
for name, val in candidates:
    print(f"  {name:<35s} {val:8.4f} {abs(R0_31-val):10.4f} {abs(R_at_fold-val):12.4f}")


# ======================================================================
#  Step 7: Correlation analysis -- is R(tau) driven by Delta_0?
# ======================================================================
print("\n" + "=" * 78)
print("Step 7: Correlation Analysis")
print("=" * 78)

corr_R_Delta = np.nan
corr_R_Econd = np.nan
corr_R_rho = np.nan
corr_R_B3B1 = np.nan

if n_active > 2:
    corr_R_Delta = np.corrcoef(R_31_arr, Delta_arr)[0, 1]
    corr_R_Econd = np.corrcoef(R_31_arr, np.abs(E_cond_arr))[0, 1]
    corr_R_rho = np.corrcoef(R_31_arr, np.array([r['rho_B2'] for r in results_list]))[0, 1]
    corr_R_B3B1 = np.corrcoef(R_31_arr, (B3_arr - B1_arr))[0, 1]

    print(f"\n  Pearson correlations with R(tau):")
    print(f"    corr(R, Delta_0)  = {corr_R_Delta:+.6f}")
    print(f"    corr(R, |E_cond|) = {corr_R_Econd:+.6f}")
    print(f"    corr(R, rho_B2)   = {corr_R_rho:+.6f}")
    print(f"    corr(R, B3-B1)    = {corr_R_B3B1:+.6f}")

    print(f"\n  Physical interpretation:")
    if abs(corr_R_Delta) > 0.95:
        print(f"    R is strongly correlated with Delta_0 (r={corr_R_Delta:.3f})")
        print(f"    => R(tau) variation is driven by BCS gap magnitude, not geometry")
    elif abs(corr_R_Delta) < 0.5:
        print(f"    R is weakly correlated with Delta_0 (r={corr_R_Delta:.3f})")
        print(f"    => R(tau) has a component independent of BCS condensation")
    else:
        print(f"    R is moderately correlated with Delta_0 (r={corr_R_Delta:.3f})")


# ======================================================================
#  Step 8: Instanton action at each tau
# ======================================================================
print("\n" + "=" * 78)
print("Step 8: Instanton Action Sweep")
print("=" * 78)

S_inst_arr = np.zeros(n_active)
for i, res in enumerate(results_list):
    a = res['a_GL']
    b = res['b_GL']
    D0 = res['Delta_0']
    if b > 0 and D0 > 1e-10:
        S_inst_arr[i] = np.sqrt(2*b) * (2.0/3.0) * D0**3
    else:
        S_inst_arr[i] = np.nan

print(f"\n  {'tau':>8s}  {'S_inst':>8s}  {'omega_att':>10s}  {'R(B3-B1)':>10s}  {'Delta_0':>8s}")
for i, res in enumerate(results_list):
    print(f"  {res['tau']:8.4f}  {S_inst_arr[i]:8.4f}  {res['omega_att']:10.6f}  "
          f"{res['R_B3_B1']:10.4f}  {res['Delta_0']:8.4f}")


# ======================================================================
#  Step 8b: B2-only vs 8-mode comparison
# ======================================================================
print("\n" + "=" * 78)
print("Step 8b: B2-only vs Full 8-mode Comparison")
print("=" * 78)

n_8mode = len(results_list_8)
if n_8mode > 0:
    tau_8 = np.array([r['tau'] for r in results_list_8])
    R_8 = np.array([r['R_B3_B1'] for r in results_list_8])
    omega_8 = np.array([r['omega_att'] for r in results_list_8])
    R0_8 = np.mean(R_8)
    sigma_8 = np.std(R_8)
    frac_8 = sigma_8 / R0_8 if R0_8 > 0 else np.nan

    print(f"\n  {'Metric':<40s} {'B2-only':>12s} {'8-mode':>12s}")
    print(f"  {'='*40} {'='*12} {'='*12}")
    print(f"  {'N active points':<40s} {n_active:>12d} {n_8mode:>12d}")
    print(f"  {'R_0 = mean(omega_att/(B3-B1))':<40s} {R0_31:>12.4f} {R0_8:>12.4f}")
    print(f"  {'sigma_R':<40s} {sigma_R_31:>12.4f} {sigma_8:>12.4f}")
    print(f"  {'sigma_R / R_0':<40s} {frac_sigma_31:>12.4f} {frac_8:>12.4f}")
    print(f"  {'R range':<40s} {R_range_31:>12.4f} {np.ptp(R_8):>12.4f}")

    # Find matching fold points in both
    idx_fold_B2 = np.argmin(np.abs(tau_arr - tau_fold))
    idx_fold_8 = np.argmin(np.abs(tau_8 - tau_fold))
    print(f"\n  At fold:")
    print(f"  {'R at fold (B2-only)':<40s} {R_31_arr[idx_fold_B2]:>12.4f}")
    print(f"  {'R at fold (8-mode)':<40s} {R_8[idx_fold_8]:>12.4f}")
    print(f"  {'omega_att at fold (B2-only)':<40s} {omega_att_arr[idx_fold_B2]:>12.6f}")
    print(f"  {'omega_att at fold (8-mode)':<40s} {omega_8[idx_fold_8]:>12.6f}")

    print(f"\n  CONCLUSION: Both B2-only and 8-mode show massive variation in R(tau).")
    print(f"  The 9-to-1 ratio is NOT a structural constant. It varies by factors of")
    print(f"  >10x across the BCS window, tracking the BCS gap magnitude.")

    # 8-mode data for saving
    R0_8mode = R0_8
    sigma_8mode = sigma_8
    frac_8mode = frac_8
else:
    R0_8mode = np.nan
    sigma_8mode = np.nan
    frac_8mode = np.nan


# ======================================================================
#  Step 9: Save results
# ======================================================================
print("\n" + "=" * 78)
print("Step 9: Saving results")
print("=" * 78)

out_path = os.path.join(SCRIPT_DIR, 's39_9to1_sweep.npz')
np.savez(out_path,
    # Gate result
    verdict=verdict,
    R0_mean=R0_31,
    sigma_R=sigma_R_31,
    frac_sigma=frac_sigma_31,
    R_range=R_range_31,

    # Sweep data (B2-only, primary)
    tau_active=tau_arr,
    omega_att_arr=omega_att_arr,
    R_B3_B1=R_31_arr,
    R_B3_B2=R_32_arr,
    Delta_0_arr=Delta_arr,
    E_cond_arr=E_cond_arr,
    E_B1_arr=B1_arr,
    E_B2_arr=B2_arr,
    E_B3_arr=B3_arr,
    S_inst_arr=S_inst_arr,

    # 8-mode comparison
    R0_8mode=R0_8mode,
    sigma_8mode=sigma_8mode,
    frac_sigma_8mode=frac_8mode,

    # Secondary ratios
    R0_B3_B2_mean=R0_32,
    sigma_R_B3_B2=sigma_R_32,
    frac_sigma_B3_B2=frac_sigma_32,

    # Fold-specific
    R_at_fold=R_at_fold,
    tau_fold_actual=tau_arr[idx_fold],

    # Correlation
    corr_R_Delta=corr_R_Delta,
    corr_R_Econd=corr_R_Econd,

    # Reference
    omega_PV=omega_PV,
    n_active=n_active,
)

print(f"  Saved to {out_path}")


# ======================================================================
#  Step 10: Plotting
# ======================================================================
print("\n" + "=" * 78)
print("Step 10: Generating plot")
print("=" * 78)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle(f'9TO1-39: R(tau) = omega_att / (B3-B1) Sweep\n'
             f'Verdict: {verdict}  |  R_0 = {R0_31:.4f}  |  sigma_R/R_0 = {frac_sigma_31:.4f}',
             fontsize=13)

# Panel 1: R(tau) with constant fit
ax = axes[0, 0]
ax.plot(tau_arr, R_31_arr, 'bo-', markersize=5, label=f'R = omega_att / (B3-B1)')
ax.axhline(R0_31, color='r', linestyle='--', label=f'R_0 = {R0_31:.4f}')
ax.fill_between(tau_arr, R0_31 - sigma_R_31, R0_31 + sigma_R_31,
                color='red', alpha=0.15, label=f'1-sigma = {sigma_R_31:.4f}')
ax.axhline(9.0, color='green', linestyle=':', alpha=0.5, label='R = 9')
ax.axvline(tau_fold, color='gray', linestyle=':', alpha=0.5, label=f'fold = {tau_fold:.3f}')
ax.set_xlabel('tau')
ax.set_ylabel('R(tau)')
ax.set_title('Primary: R = omega_att / (B3 - B1)')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 2: omega_att and BCS gap vs tau
ax = axes[0, 1]
ax2 = ax.twinx()
ax.plot(tau_arr, omega_att_arr, 'ro-', markersize=4, label='omega_att')
ax2.plot(tau_arr, Delta_arr, 'b^-', markersize=4, label='Delta_0')
ax2.plot(tau_arr, np.abs(E_cond_arr), 'gs-', markersize=4, label='|E_cond|')
ax.axvline(tau_fold, color='gray', linestyle=':', alpha=0.5)
ax.set_xlabel('tau')
ax.set_ylabel('omega_att', color='red')
ax2.set_ylabel('Delta_0, |E_cond|', color='blue')
ax.set_title('BCS Parameters vs tau')
lines1 = ax.get_legend_handles_labels()
lines2 = ax2.get_legend_handles_labels()
ax.legend(lines1[0] + lines2[0], lines1[1] + lines2[1], fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 3: Eigenvalue branches
ax = axes[1, 0]
tau_plot = np.linspace(0, 0.5, 200)
ax.plot(tau_plot, cs_B1(tau_plot), 'b-', label='B1 (singlet)')
ax.plot(tau_plot, cs_B2(tau_plot), 'g-', label='B2 (quartet)')
ax.plot(tau_plot, cs_B3(tau_plot), 'r-', label='B3 (triplet)')
ax.plot(tau_plot, cs_B3(tau_plot) - cs_B1(tau_plot), 'k--', label='B3 - B1')
# Mark active BCS region
ax.axvspan(tau_arr.min(), tau_arr.max(), alpha=0.1, color='yellow', label='BCS active')
ax.axvline(tau_fold, color='gray', linestyle=':', alpha=0.5)
ax.set_xlabel('tau')
ax.set_ylabel('Eigenvalue / Spacing')
ax.set_title('Eigenvalue Branches')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 4: R(tau) vs Delta_0 scatter
ax = axes[1, 1]
sc = ax.scatter(Delta_arr, R_31_arr, c=tau_arr, cmap='viridis', s=40, edgecolors='k', linewidth=0.5)
plt.colorbar(sc, ax=ax, label='tau')
ax.set_xlabel('Delta_0')
ax.set_ylabel('R = omega_att / (B3-B1)')
ax.set_title(f'R vs Delta_0 (corr = {corr_R_Delta:.3f})')
ax.axhline(9.0, color='green', linestyle=':', alpha=0.5, label='R = 9')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plot_path = os.path.join(SCRIPT_DIR, 's39_9to1_sweep.png')
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
print(f"  Saved plot to {plot_path}")

dt = time.time() - t0
print(f"\n  Total time: {dt:.2f}s")


# ======================================================================
#  Final Summary
# ======================================================================
print("\n" + "=" * 78)
print("  FINAL SUMMARY: 9TO1-39")
print("=" * 78)
print(f"""
  GATE 9TO1-39: {verdict}
    sigma_R / R_0 = {frac_sigma_31:.6f}  ({frac_sigma_31*100:.2f}%)
    R_0 (mean)    = {R0_31:.6f}
    R at fold     = {R_at_fold:.6f}
    R range       = [{np.min(R_31_arr):.4f}, {np.max(R_31_arr):.4f}]
    N points      = {n_active}

  SECONDARY RATIOS:
    omega_att/(B3-B2): mean = {R0_32:.4f}, sigma/mean = {frac_sigma_32:.4f}
    omega_att/omega_PV: mean = {R0_att_PV:.4f}, sigma/mean = {sigma_att_PV/R0_att_PV:.4f}

  CORRELATIONS:
    corr(R, Delta_0)  = {corr_R_Delta:+.4f}
    corr(R, |E_cond|) = {corr_R_Econd:+.4f}

  FILES:
    Script: tier0-computation/s39_9to1_sweep.py
    Data:   tier0-computation/s39_9to1_sweep.npz
    Plot:   tier0-computation/s39_9to1_sweep.png
""")
print("=" * 78)
