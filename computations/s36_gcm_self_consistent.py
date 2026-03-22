#!/usr/bin/env python3
"""
Session 36: SC-HFB-36 -- Self-Consistent GCM Kernel Integrals (MASTER GATE)
============================================================================

CONTEXT:
  The Generator Coordinate Method (GCM) is the gold standard in nuclear DFT
  for computing correlation energies beyond the mean-field approximation. It
  mixes constrained HFB solutions at different values of a collective
  coordinate (here tau) to form a correlated ground state.

  Three-way dictionary (nuclear / framework / string):
    GCM mixing of nuclear shapes -> GCM mixing of tau configs -> landscape wavefunction
    Constrained HFB at each tau  -> BCS energy at each tau     -> spectral action at each tau
    GCM eigenvalue equation      -> Hill-Wheeler equation      -> Wheeler-DeWitt analog

  The GCM eigenvalue problem is:
    sum_j (H_ij - E_alpha * N_ij) f_alpha(q_j) = 0

  This script performs the computation at TWO resolutions:
  (A) Coarse grid: original 9 tau points
  (B) Fine grid: 41 points with dense sampling near the van Hove fold

  The van Hove fold at tau_fold ~ 0.190 creates a NARROW spike in DOS
  that supports BCS pairing. The 9-point coarse grid has only ONE point
  (tau=0.20) in the pairing-active region. A fine grid is essential for
  proper resolution of the pairing pocket.

GATE SC-HFB-36 (MASTER, pre-registered):
  PASS:     M_max(GCM) > 1.0  -> mechanism chain survives self-consistency
  FAIL:     M_max(GCM) < 1.0  -> mechanism chain broken
  MARGINAL: M_max(GCM) in [0.95, 1.05] -> requires beyond-GCM

Author: nazarewicz-nuclear-structure-theorist, Session 36 Wave 2
Date: 2026-03-07
"""

import os
import sys
import time
import numpy as np
from numpy.linalg import eigh, eigvals
from scipy.linalg import eigh as scipy_eigh
from scipy.interpolate import CubicSpline
from scipy.stats import norm as normal_dist

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
t0 = time.time()

# ======================================================================
#  Constants and Parameters
# ======================================================================
MU = 0.0        # Chemical potential (PH-symmetric, forced by Session 34)
MS_FACTOR = 1.046   # Multi-sector factor (SECT-33a)
ETA_REG_FRAC = 0.001  # Regulator fraction for Thouless

# Branch indices in 16x16 sorted eigenbasis (positive sector)
B1_IDX = np.array([8])           # d=1, lowest positive
B2_IDX = np.array([9, 10, 11, 12])  # d=4
B3_IDX = np.array([13, 14, 15])     # d=3

# GCM parameters
GCM_REG_THRESHOLD = 1e-6  # Eigenvalue threshold for norm kernel


# ======================================================================
#  Data Loading
# ======================================================================
def load_data():
    """Load all prerequisite data files."""
    print("Step 1: Loading prerequisite data...")

    kosmann = np.load(os.path.join(SCRIPT_DIR, 's23a_kosmann_singlet.npz'),
                      allow_pickle=True)
    strutinsky = np.load(os.path.join(SCRIPT_DIR, 's33a_strutinsky.npz'),
                         allow_pickle=True)
    vh_data = np.load(os.path.join(SCRIPT_DIR, 's35a_vh_impedance_arbiter.npz'),
                      allow_pickle=True)
    s35_data = np.load(os.path.join(SCRIPT_DIR, 's35_thouless_multiband.npz'),
                       allow_pickle=True)
    mmax_data = np.load(os.path.join(SCRIPT_DIR, 's36_mmax_authoritative.npz'),
                        allow_pickle=True)

    tau_grid = kosmann['tau_values']  # [0, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.5]
    S_singlet = strutinsky['S_singlet']

    print(f"  tau_grid: {tau_grid}")
    print(f"  S_singlet: {S_singlet}")

    return kosmann, strutinsky, vh_data, s35_data, mmax_data, tau_grid, S_singlet


# ======================================================================
#  Build V matrix and eigenvalues at original tau points
# ======================================================================
def build_V_and_eigenvalues(kosmann, tau_idx):
    """Build V_nm = sum_{a=0..7} |K^a_{nm}|^2 in eigenvalue-sorted basis."""
    evals = kosmann[f'eigenvalues_{tau_idx}']
    sort_idx = np.argsort(evals)
    evals_sorted = evals[sort_idx]

    V = np.zeros((16, 16))
    for a in range(8):
        K = kosmann[f'K_a_matrix_{tau_idx}_{a}']
        V += np.abs(K) ** 2

    V_sorted = V[np.ix_(sort_idx, sort_idx)]
    return V_sorted, evals_sorted


# ======================================================================
#  Compute DOS via van Hove profile
# ======================================================================
def compute_dos(tau, tau_fold, rho_B2_step, rho_B2_smooth, rho_B1_raw,
                rho_B3_raw, delta_tau_wall=0.040):
    """Compute DOS at arbitrary tau using Lorentzian van Hove profile."""
    gamma = delta_tau_wall / 2.0
    vh_enh = rho_B2_smooth / rho_B2_step - 1.0
    lorentz = gamma**2 / ((tau - tau_fold)**2 + gamma**2)

    rho_B2 = rho_B2_step * (1.0 + vh_enh * lorentz) * MS_FACTOR
    rho_B1 = rho_B1_raw * MS_FACTOR
    rho_B3 = rho_B3_raw * MS_FACTOR

    return rho_B1, rho_B2, rho_B3


# ======================================================================
#  Thouless M_max
# ======================================================================
def compute_Mmax(V_sorted, evals_sorted, rho_B1, rho_B2, rho_B3,
                 mode='B2_only'):
    """Compute Thouless M_max for specified subspace."""
    if mode == 'B2_only':
        idx = B2_IDX.tolist()
        rho_list = [rho_B2] * 4
    elif mode == '8x8':
        idx = np.concatenate([B1_IDX, B2_IDX, B3_IDX]).tolist()
        rho_list = [rho_B1] + [rho_B2] * 4 + [rho_B3] * 3
    else:
        raise ValueError(f"Unknown mode: {mode}")

    E_sub = evals_sorted[np.array(idx)]
    xi = E_sub - MU
    lambda_min = np.min(np.abs(E_sub))
    eta = max(ETA_REG_FRAC * lambda_min, 1e-15)
    abs_xi = np.maximum(np.abs(xi), eta)

    V_sub = V_sorted[np.ix_(idx, idx)]
    rho = np.array(rho_list)
    n = len(idx)

    M = np.zeros((n, n))
    for m in range(n):
        M[:, m] = V_sub[:, m] * rho[m] / (2.0 * abs_xi[m])

    return np.max(np.real(eigvals(M)))


# ======================================================================
#  BCS gap equation solver
# ======================================================================
def solve_bcs_gap(V_sorted, evals_sorted, rho_B2, max_iter=500, tol=1e-10):
    """Solve BCS gap equation self-consistently for B2 modes.

    Returns: Delta (4,), E_qp (4,), E_BCS (scalar), converged (bool)
    """
    idx = B2_IDX.tolist()
    E_sub = evals_sorted[np.array(idx)]
    xi = E_sub - MU
    V_sub = V_sorted[np.ix_(idx, idx)]
    V_eff = V_sub * rho_B2
    n = len(idx)

    V_offdiag_mean = np.mean(np.abs(V_eff[np.triu_indices(n, k=1)]))
    if V_offdiag_mean < 1e-15:
        return np.zeros(n), np.abs(xi), 0.0, True

    # Try multiple seeds
    for seed_scale in [0.1, 0.3, 0.5, 1.0]:
        Delta = np.full(n, seed_scale * V_offdiag_mean)
        converged = False
        for _ in range(max_iter):
            E_qp = np.sqrt(xi**2 + Delta**2)
            Delta_new = 0.5 * V_eff @ (Delta / E_qp)
            diff = np.max(np.abs(Delta_new - Delta))
            if diff < tol:
                converged = True
                Delta = Delta_new
                break
            Delta = 0.5 * Delta + 0.5 * Delta_new

        if converged and np.max(Delta) > tol:
            break

    E_qp = np.sqrt(xi**2 + Delta**2)
    E_BCS = np.sum(np.abs(xi) - E_qp) + 0.5 * np.sum(Delta**2 / E_qp)

    return Delta, E_qp, E_BCS, converged


# ======================================================================
#  GCM Norm and Hamiltonian Kernels
# ======================================================================
def build_gcm_kernels(tau_fine, E_total_fine, sigma):
    """Build GCM norm and Hamiltonian kernels.

    Norm kernel (GOA): N_ij = exp(-(tau_i - tau_j)^2 / (4 sigma^2))

    Hamiltonian kernel (GOA, midpoint prescription):
      H_ij = E_total((tau_i + tau_j)/2) * N_ij
    This is the proper GOA form (Ring & Schuck, eq 11.57).
    """
    n = len(tau_fine)
    N_k = np.zeros((n, n))
    H_k = np.zeros((n, n))

    # Build E_total interpolator for midpoint evaluation
    cs_E = CubicSpline(tau_fine, E_total_fine)

    for i in range(n):
        for j in range(n):
            dtau = tau_fine[i] - tau_fine[j]
            N_k[i, j] = np.exp(-dtau**2 / (4.0 * sigma**2))

            # Midpoint energy (proper GOA)
            tau_mid = 0.5 * (tau_fine[i] + tau_fine[j])
            # Clamp to grid range for spline evaluation
            tau_mid = np.clip(tau_mid, tau_fine[0], tau_fine[-1])
            H_k[i, j] = cs_E(tau_mid) * N_k[i, j]

    return H_k, N_k


# ======================================================================
#  Hill-Wheeler GCM Eigenvalue Problem
# ======================================================================
def solve_hill_wheeler(H_k, N_k, reg_threshold=1e-6):
    """Solve sum_j (H_ij - E_alpha N_ij) f_alpha(j) = 0.

    Uses N^{-1/2} H N^{-1/2} transformation with regularization.
    """
    n_evals, n_evecs = eigh(N_k)
    mask = n_evals > reg_threshold
    n_kept = int(np.sum(mask))

    if n_kept == 0:
        raise ValueError("All norm eigenvalues below threshold!")

    n_evals_k = n_evals[mask]
    n_evecs_k = n_evecs[:, mask]

    N_inv_sqrt = n_evecs_k @ np.diag(1.0 / np.sqrt(n_evals_k)) @ n_evecs_k.T
    H_tilde = N_inv_sqrt @ H_k @ N_inv_sqrt

    E_alpha, g_alpha = eigh(H_tilde)
    f_alpha = N_inv_sqrt @ g_alpha

    return E_alpha, f_alpha, n_evals, n_kept


# ======================================================================
#  MAIN COMPUTATION
# ======================================================================
def main():
    print("=" * 78)
    print("SC-HFB-36: Self-Consistent GCM Kernel Integrals (MASTER GATE)")
    print("Nazarewicz Nuclear Structure Theorist")
    print("=" * 78)
    print()

    # ================================================================
    #  LOAD DATA
    # ================================================================
    kosmann, strutinsky, vh_data, s35_data, mmax_data, tau_grid, S_singlet = load_data()
    n_coarse = len(tau_grid)

    tau_fold = float(vh_data['tau_fold'])
    rho_B2_step = float(vh_data['rho_step'])
    rho_B2_smooth = float(vh_data['rho_at_physical'])
    rho_B1_raw = float(s35_data['rho_B1']) / MS_FACTOR
    rho_B3_raw = float(s35_data['rho_B3']) / MS_FACTOR

    # ================================================================
    #  COARSE GRID: Build V, eigenvalues, DOS, M_max, BCS at all 9 tau
    # ================================================================
    print(f"\n{'='*78}")
    print(f"Step 2: Computing at coarse grid ({n_coarse} points)")
    print(f"{'='*78}")

    V_coarse = []
    evals_coarse = []
    for ti in range(n_coarse):
        V, ev = build_V_and_eigenvalues(kosmann, ti)
        V_coarse.append(V)
        evals_coarse.append(ev)

    # Extract branch eigenvalues for interpolation
    E_B1_coarse = np.array([evals_coarse[i][B1_IDX[0]] for i in range(n_coarse)])
    E_B2_coarse = np.array([evals_coarse[i][B2_IDX[0]] for i in range(n_coarse)])
    E_B3_coarse = np.array([evals_coarse[i][B3_IDX[0]] for i in range(n_coarse)])

    # Extract V matrix elements for interpolation (key ones only)
    V_B2B2_offdiag_coarse = np.array([
        np.max(V_coarse[i][np.ix_(B2_IDX, B2_IDX)] - np.diag(np.diag(V_coarse[i][np.ix_(B2_IDX, B2_IDX)])))
        for i in range(n_coarse)])
    V_B1B2_max_coarse = np.array([
        np.max(V_coarse[i][np.ix_(B1_IDX, B2_IDX)])
        for i in range(n_coarse)])

    # Compute M_max and BCS at coarse points
    Mmax_B2_coarse = np.zeros(n_coarse)
    Mmax_8x8_coarse = np.zeros(n_coarse)
    E_BCS_coarse = np.zeros(n_coarse)
    Delta_max_coarse = np.zeros(n_coarse)

    print(f"\n  {'tau':>6s}  {'rho_B2':>8s}  {'M_B2':>8s}  {'M_8x8':>8s}  {'Delta':>8s}  {'E_BCS':>10s}")
    print(f"  {'='*6}  {'='*8}  {'='*8}  {'='*8}  {'='*8}  {'='*10}")

    for ti in range(n_coarse):
        rB1, rB2, rB3 = compute_dos(tau_grid[ti], tau_fold, rho_B2_step,
                                     rho_B2_smooth, rho_B1_raw, rho_B3_raw)
        Mmax_B2_coarse[ti] = compute_Mmax(V_coarse[ti], evals_coarse[ti], rB1, rB2, rB3, 'B2_only')
        Mmax_8x8_coarse[ti] = compute_Mmax(V_coarse[ti], evals_coarse[ti], rB1, rB2, rB3, '8x8')

        Delta, E_qp, E_BCS, conv = solve_bcs_gap(V_coarse[ti], evals_coarse[ti], rB2)
        E_BCS_coarse[ti] = E_BCS
        Delta_max_coarse[ti] = np.max(Delta)

        print(f"  {tau_grid[ti]:6.2f}  {rB2:8.2f}  {Mmax_B2_coarse[ti]:8.4f}  "
              f"{Mmax_8x8_coarse[ti]:8.4f}  {np.max(Delta):8.4f}  {E_BCS:10.6f}")

    E_total_coarse = S_singlet + E_BCS_coarse

    # ================================================================
    #  FINE GRID: Interpolate to dense grid around fold
    # ================================================================
    print(f"\n{'='*78}")
    print(f"Step 3: Building fine grid with dense fold sampling")
    print(f"{'='*78}")

    # Create fine grid: base 0.02 spacing, densified to 0.005 near fold
    tau_base = np.arange(0.0, 0.501, 0.02)
    tau_fold_region = np.arange(tau_fold - 0.05, tau_fold + 0.051, 0.005)
    tau_fine = np.sort(np.unique(np.concatenate([tau_base, tau_fold_region])))
    # Clamp to [0, 0.5]
    tau_fine = tau_fine[(tau_fine >= 0) & (tau_fine <= 0.5)]
    n_fine = len(tau_fine)

    print(f"  Fine grid: {n_fine} points")
    print(f"  Fold region [{tau_fold-0.05:.3f}, {tau_fold+0.05:.3f}]: "
          f"{np.sum((tau_fine >= tau_fold-0.05) & (tau_fine <= tau_fold+0.05))} points")

    # Interpolate eigenvalues using cubic splines
    cs_E_B1 = CubicSpline(tau_grid, E_B1_coarse)
    cs_E_B2 = CubicSpline(tau_grid, E_B2_coarse)
    cs_E_B3 = CubicSpline(tau_grid, E_B3_coarse)
    cs_S = CubicSpline(tau_grid, S_singlet)

    # Interpolate V matrix elements
    cs_V_B2B2 = CubicSpline(tau_grid, V_B2B2_offdiag_coarse)
    cs_V_B1B2 = CubicSpline(tau_grid, V_B1B2_max_coarse)

    # At each fine grid point, construct the eigenvalue and V structures
    # by interpolation and compute M_max and BCS
    Mmax_B2_fine = np.zeros(n_fine)
    Mmax_8x8_fine = np.zeros(n_fine)
    E_BCS_fine = np.zeros(n_fine)
    Delta_max_fine = np.zeros(n_fine)
    S_fine = np.zeros(n_fine)
    rho_B2_fine = np.zeros(n_fine)

    for fi in range(n_fine):
        tau = tau_fine[fi]
        rB1, rB2, rB3 = compute_dos(tau, tau_fold, rho_B2_step,
                                     rho_B2_smooth, rho_B1_raw, rho_B3_raw)
        rho_B2_fine[fi] = rB2

        # Interpolate eigenvalues
        E_b1 = cs_E_B1(tau)
        E_b2 = cs_E_B2(tau)
        E_b3 = cs_E_B3(tau)

        # Build approximate eigenvalue and V arrays for this tau
        evals_approx = np.zeros(16)
        # Negative sector (PH partners)
        evals_approx[0:3] = -E_b3  # B3- (3 modes)
        evals_approx[3:7] = -E_b2  # B2- (4 modes)
        evals_approx[7] = -E_b1    # B1- (1 mode)
        # Positive sector
        evals_approx[8] = E_b1     # B1+ (1 mode)
        evals_approx[9:13] = E_b2  # B2+ (4 modes)
        evals_approx[13:16] = E_b3 # B3+ (3 modes)

        # Interpolate V matrix: use nearest coarse point V matrix
        # (V matrix structure is smooth in tau; key variation is in eigenvalues and DOS)
        nearest_coarse = np.argmin(np.abs(tau_grid - tau))
        V_approx = V_coarse[nearest_coarse].copy()

        # Scale V off-diagonal by interpolated ratio
        if V_B2B2_offdiag_coarse[nearest_coarse] > 1e-15:
            v_ratio = cs_V_B2B2(tau) / V_B2B2_offdiag_coarse[nearest_coarse]
            V_B2_block = V_approx[np.ix_(B2_IDX, B2_IDX)]
            diag_B2 = np.diag(np.diag(V_B2_block))
            V_approx[np.ix_(B2_IDX, B2_IDX)] = diag_B2 + (V_B2_block - diag_B2) * max(v_ratio, 0)

        Mmax_B2_fine[fi] = compute_Mmax(V_approx, evals_approx, rB1, rB2, rB3, 'B2_only')
        Mmax_8x8_fine[fi] = compute_Mmax(V_approx, evals_approx, rB1, rB2, rB3, '8x8')

        Delta, E_qp, E_BCS, conv = solve_bcs_gap(V_approx, evals_approx, rB2)
        E_BCS_fine[fi] = E_BCS
        Delta_max_fine[fi] = np.max(Delta)
        S_fine[fi] = cs_S(tau)

    E_total_fine = S_fine + E_BCS_fine

    # Print fine grid around fold
    print(f"\n  Fine grid around fold:")
    print(f"  {'tau':>8s}  {'rho_B2':>8s}  {'M_B2':>8s}  {'M_8x8':>8s}  {'Delta':>8s}  {'E_BCS':>10s}  {'S':>10s}  {'E_tot':>10s}")
    print(f"  {'='*8}  {'='*8}  {'='*8}  {'='*8}  {'='*8}  {'='*10}  {'='*10}  {'='*10}")
    for fi in range(n_fine):
        if abs(tau_fine[fi] - tau_fold) < 0.08:
            marker = " *" if Mmax_B2_fine[fi] > 1.0 else ""
            print(f"  {tau_fine[fi]:8.4f}  {rho_B2_fine[fi]:8.2f}  {Mmax_B2_fine[fi]:8.4f}  "
                  f"{Mmax_8x8_fine[fi]:8.4f}  {Delta_max_fine[fi]:8.4f}  {E_BCS_fine[fi]:10.6f}  "
                  f"{S_fine[fi]:10.6f}  {E_total_fine[fi]:10.6f}{marker}")

    # Count pairing-active points
    n_paired_B2 = np.sum(Mmax_B2_fine > 1.0)
    n_paired_8x8 = np.sum(Mmax_8x8_fine > 1.0)
    tau_paired_B2 = tau_fine[Mmax_B2_fine > 1.0]
    tau_paired_8x8 = tau_fine[Mmax_8x8_fine > 1.0]

    print(f"\n  Pairing-active points (B2-only M_max > 1): {n_paired_B2}/{n_fine}")
    if n_paired_B2 > 0:
        print(f"    tau range: [{tau_paired_B2[0]:.4f}, {tau_paired_B2[-1]:.4f}]")
        print(f"    width: {tau_paired_B2[-1] - tau_paired_B2[0]:.4f}")
    print(f"  Pairing-active points (8x8 M_max > 1):    {n_paired_8x8}/{n_fine}")
    if n_paired_8x8 > 0:
        print(f"    tau range: [{tau_paired_8x8[0]:.4f}, {tau_paired_8x8[-1]:.4f}]")
        print(f"    width: {tau_paired_8x8[-1] - tau_paired_8x8[0]:.4f}")

    # ================================================================
    #  STEP 4: GCM WIDTH PARAMETER sigma
    # ================================================================
    print(f"\n{'='*78}")
    print(f"Step 4: GCM width parameter estimation")
    print(f"{'='*78}")

    # The GCM width sigma should reflect the COLLECTIVE wavefunction spread,
    # not individual mode properties.

    # Method 1: From the spectral action curvature (RPA stiffness)
    # This is the natural scale for oscillations in the tau potential
    d2S = 20.43  # RPA-32b
    sigma_rpa = 1.0 / np.sqrt(d2S)

    # Method 2: From the pairing window width
    # The BCS pairing is active over a finite range of tau.
    # sigma should be ~ half the pairing window width
    if n_paired_B2 > 0:
        sigma_pair = (tau_paired_B2[-1] - tau_paired_B2[0]) / 2.0
        if sigma_pair < 0.005:
            sigma_pair = 0.02  # minimum physical width
    else:
        sigma_pair = 0.03  # estimate from DOS spike width

    # Method 3: From the total energy curvature at the minimum
    # d2E_total/dtau2 at the minimum gives the oscillator frequency
    cs_Etot = CubicSpline(tau_fine, E_total_fine)
    idx_min = np.argmin(E_total_fine)
    tau_min = tau_fine[idx_min]
    d2E_at_min = cs_Etot(tau_min, 2)
    if d2E_at_min > 0:
        sigma_etot = 1.0 / np.sqrt(d2E_at_min)
    else:
        sigma_etot = 0.05

    print(f"  sigma estimates:")
    print(f"    Method 1 (1/sqrt(d2S)):   {sigma_rpa:.6f}")
    print(f"    Method 2 (pairing width): {sigma_pair:.6f}")
    print(f"    Method 3 (1/sqrt(d2E)):   {sigma_etot:.6f}")
    print(f"    E_total minimum at tau =  {tau_min:.4f}")
    print(f"    d2E/dtau2 at minimum:     {d2E_at_min:.4f}")

    # Physical sigma: the pairing width is the most relevant scale
    # because the GCM mixes states that differ in their pairing content
    sigma_phys = sigma_pair
    sigma_scan = np.array([sigma_pair * 0.5, sigma_pair, sigma_pair * 2.0,
                           sigma_rpa, sigma_etot])
    sigma_scan = np.sort(np.unique(np.clip(sigma_scan, 0.005, 0.5)))

    print(f"\n  Physical sigma (pairing width): {sigma_phys:.6f}")
    print(f"  Scan values: {sigma_scan}")

    # ================================================================
    #  STEP 5: SOLVE GCM FOR MULTIPLE SIGMA VALUES
    # ================================================================
    print(f"\n{'='*78}")
    print(f"Step 5: Solving Hill-Wheeler GCM at {len(sigma_scan)} sigma values")
    print(f"{'='*78}")

    gcm_results = []

    for sigma in sigma_scan:
        print(f"\n  --- sigma = {sigma:.6f} ---")

        H_k, N_k = build_gcm_kernels(tau_fine, E_total_fine, sigma)
        E_alpha, f_alpha, n_evals, n_kept = solve_hill_wheeler(
            H_k, N_k, reg_threshold=GCM_REG_THRESHOLD)

        # Ground state
        E_gs = E_alpha[0]
        f_gs = f_alpha[:, 0]

        # Probability distribution
        prob = np.abs(f_gs)**2
        prob_norm = prob / np.sum(prob)

        # Expectation values
        tau_avg = np.sum(prob_norm * tau_fine)
        tau2_avg = np.sum(prob_norm * tau_fine**2)
        tau_sigma = np.sqrt(max(tau2_avg - tau_avg**2, 0))

        # M_max at <tau>
        cs_Mmax_B2 = CubicSpline(tau_fine, Mmax_B2_fine)
        cs_Mmax_8x8 = CubicSpline(tau_fine, Mmax_8x8_fine)
        Mmax_B2_avg = float(np.clip(cs_Mmax_B2(tau_avg), 0, 5))
        Mmax_8x8_avg = float(np.clip(cs_Mmax_8x8(tau_avg), 0, 5))

        # Effective M_max (weighted average)
        Mmax_B2_eff = np.sum(prob_norm * Mmax_B2_fine)
        Mmax_8x8_eff = np.sum(prob_norm * Mmax_8x8_fine)

        # GCM correlation energy
        E_GCM_corr = E_gs - np.min(E_total_fine)

        # Fraction in paired region
        frac_paired_B2 = np.sum(prob_norm[Mmax_B2_fine > 1.0])
        frac_paired_8x8 = np.sum(prob_norm[Mmax_8x8_fine > 1.0])

        # Peak location
        peak_idx = np.argmax(prob_norm)
        peak_tau = tau_fine[peak_idx]

        result = {
            'sigma': sigma,
            'E_gs': E_gs,
            'E_GCM_corr': E_GCM_corr,
            'tau_avg': tau_avg,
            'tau_sigma': tau_sigma,
            'peak_tau': peak_tau,
            'prob_norm': prob_norm.copy(),
            'Mmax_B2_avg': Mmax_B2_avg,
            'Mmax_8x8_avg': Mmax_8x8_avg,
            'Mmax_B2_eff': Mmax_B2_eff,
            'Mmax_8x8_eff': Mmax_8x8_eff,
            'frac_paired_B2': frac_paired_B2,
            'frac_paired_8x8': frac_paired_8x8,
            'n_kept': n_kept,
            'E_alpha': E_alpha.copy(),
        }
        gcm_results.append(result)

        print(f"    States kept: {n_kept}/{len(n_evals)}")
        print(f"    E_gs = {E_gs:.6f}, E_GCM_corr = {E_GCM_corr:.6f}")
        print(f"    <tau> = {tau_avg:.6f}, sigma(tau) = {tau_sigma:.6f}, peak = {peak_tau:.4f}")
        print(f"    M_max(B2) at <tau>: {Mmax_B2_avg:.6f}")
        print(f"    M_max(8x8) at <tau>: {Mmax_8x8_avg:.6f}")
        print(f"    M_max_eff(B2): {Mmax_B2_eff:.6f}")
        print(f"    M_max_eff(8x8): {Mmax_8x8_eff:.6f}")
        print(f"    Fraction paired (B2): {frac_paired_B2:.4f}")
        print(f"    Fraction paired (8x8): {frac_paired_8x8:.4f}")

    # ================================================================
    #  STEP 6: DETERMINE AUTHORITATIVE GCM M_max
    # ================================================================
    print(f"\n{'='*78}")
    print(f"Step 6: Authoritative GCM M_max determination")
    print(f"{'='*78}")

    # The most physical sigma is the one that satisfies the self-consistency
    # condition: sigma_GCM ~ sigma(tau) from the resulting wavefunction.
    # Find the sigma where sigma_input ~ tau_sigma_output.

    print(f"\n  Self-consistency of sigma:")
    print(f"  {'sigma_in':>10s}  {'sigma_out':>10s}  {'ratio':>8s}  {'status':>15s}")
    print(f"  {'='*10}  {'='*10}  {'='*8}  {'='*15}")

    best_sc_idx = 0
    best_sc_ratio = 999

    for i, r in enumerate(gcm_results):
        ratio = r['tau_sigma'] / r['sigma']
        status = "SELF-CONSISTENT" if 0.5 < ratio < 2.0 else "INCONSISTENT"
        print(f"  {r['sigma']:10.6f}  {r['tau_sigma']:10.6f}  {ratio:8.4f}  {status:>15s}")

        if abs(ratio - 1.0) < abs(best_sc_ratio - 1.0):
            best_sc_ratio = ratio
            best_sc_idx = i

    print(f"\n  Best self-consistent sigma: {gcm_results[best_sc_idx]['sigma']:.6f}")
    print(f"    (sigma_out/sigma_in = {best_sc_ratio:.4f})")

    gcm_sc = gcm_results[best_sc_idx]

    # The GCM M_max is the EFFECTIVE (weighted) value at the self-consistent sigma
    Mmax_GCM_B2 = gcm_sc['Mmax_B2_eff']
    Mmax_GCM_8x8 = gcm_sc['Mmax_8x8_eff']

    # Also compute M_max at the PEAK of the wavefunction
    Mmax_B2_peak = float(np.clip(cs_Mmax_B2(gcm_sc['peak_tau']), 0, 5))
    Mmax_8x8_peak = float(np.clip(cs_Mmax_8x8(gcm_sc['peak_tau']), 0, 5))

    print(f"\n  GCM M_max at self-consistent sigma = {gcm_sc['sigma']:.6f}:")
    print(f"    B2 effective (weighted): {Mmax_GCM_B2:.6f}")
    print(f"    8x8 effective (weighted): {Mmax_GCM_8x8:.6f}")
    print(f"    B2 at peak tau={gcm_sc['peak_tau']:.4f}: {Mmax_B2_peak:.6f}")
    print(f"    8x8 at peak tau={gcm_sc['peak_tau']:.4f}: {Mmax_8x8_peak:.6f}")
    print(f"    B2 at <tau>={gcm_sc['tau_avg']:.4f}: {gcm_sc['Mmax_B2_avg']:.6f}")
    print(f"    8x8 at <tau>={gcm_sc['tau_avg']:.4f}: {gcm_sc['Mmax_8x8_avg']:.6f}")

    # Full range across all sigma
    Mmax_B2_all = np.array([r['Mmax_B2_eff'] for r in gcm_results])
    Mmax_8x8_all = np.array([r['Mmax_8x8_eff'] for r in gcm_results])
    Mmax_B2_interp_all = np.array([r['Mmax_B2_avg'] for r in gcm_results])
    Mmax_8x8_interp_all = np.array([r['Mmax_8x8_avg'] for r in gcm_results])

    Mmax_GCM_conservative = np.min(Mmax_B2_all)
    Mmax_GCM_upper = np.max(Mmax_8x8_all)

    print(f"\n  GCM M_max range (across all sigma):")
    print(f"    Conservative (min B2 eff):    {Mmax_GCM_conservative:.6f}")
    print(f"    Self-consistent (B2 eff):     {Mmax_GCM_B2:.6f}")
    print(f"    Upper (max 8x8 eff):          {Mmax_GCM_upper:.6f}")

    # ================================================================
    #  STEP 7: SELF-CONSISTENCY CORRECTION alpha
    # ================================================================
    print(f"\n{'='*78}")
    print(f"Step 7: Self-consistency correction alpha")
    print(f"{'='*78}")

    # Reference MF values from MMAX-AUTH-36
    Mmax_MF_B2 = float(mmax_data['M_4x4_B2only'])   # 1.351
    Mmax_MF_8x8 = float(mmax_data['M_8x8'])          # 1.674
    # But these were at the PEAK DOS (tau=0.20 with full VH DOS 14.67)
    # The fine-grid M_max at tau=0.20 uses interpolated DOS
    # For proper alpha, use the PEAK M_max from the fine grid
    Mmax_MF_B2_peak = np.max(Mmax_B2_fine)
    Mmax_MF_8x8_peak = np.max(Mmax_8x8_fine)
    tau_Mmax_peak = tau_fine[np.argmax(Mmax_B2_fine)]

    print(f"\n  MF reference values:")
    print(f"    MMAX-AUTH-36 B2-only:     {Mmax_MF_B2:.6f} (at tau=0.20, full VH DOS)")
    print(f"    MMAX-AUTH-36 8x8:         {Mmax_MF_8x8:.6f}")
    print(f"    Fine grid peak B2:        {Mmax_MF_B2_peak:.6f} (at tau={tau_Mmax_peak:.4f})")
    print(f"    Fine grid peak 8x8:       {Mmax_MF_8x8_peak:.6f}")

    # alpha = M_max(GCM) / M_max(MF)
    # Use MF peak from fine grid (self-consistent with the same DOS model)
    alpha_sc_B2 = Mmax_GCM_B2 / Mmax_MF_B2_peak
    alpha_sc_8x8 = Mmax_GCM_8x8 / Mmax_MF_8x8_peak
    alpha_cons = Mmax_GCM_conservative / Mmax_MF_B2_peak

    # Also compute alpha using MMAX-AUTH-36 values (cross-check)
    alpha_auth_B2 = Mmax_GCM_B2 / Mmax_MF_B2
    alpha_auth_8x8 = Mmax_GCM_8x8 / Mmax_MF_8x8

    print(f"\n  Self-consistency correction alpha:")
    print(f"    alpha(B2, SC, fine grid peak):  {alpha_sc_B2:.6f}")
    print(f"    alpha(8x8, SC, fine grid peak): {alpha_sc_8x8:.6f}")
    print(f"    alpha(B2, conservative):        {alpha_cons:.6f}")
    print(f"    alpha(B2, vs AUTH-36):           {alpha_auth_B2:.6f}")
    print(f"    alpha(8x8, vs AUTH-36):          {alpha_auth_8x8:.6f}")

    # ================================================================
    #  STEP 8: BAYESIAN p(M_max(SC) > 1)
    # ================================================================
    print(f"\n{'='*78}")
    print(f"Step 8: Bayesian p(M_max(SC) > 1)")
    print(f"{'='*78}")

    sigma_alpha = 0.10  # Workshop uncertainty estimate

    # Against AUTH-36 reference (the standard for the project)
    # p(alpha * M_max(MF) > 1) = p(alpha > 1/M_max(MF))
    results_bayes = {}

    for label, Mmax_GCM_val, Mmax_MF_val in [
        ("B2 conservative", Mmax_GCM_conservative, Mmax_MF_B2),
        ("B2 self-consistent", Mmax_GCM_B2, Mmax_MF_B2),
        ("8x8 self-consistent", Mmax_GCM_8x8, Mmax_MF_8x8),
        ("8x8 upper", Mmax_GCM_upper, Mmax_MF_8x8),
        ("B2 peak", Mmax_B2_peak, Mmax_MF_B2),
        ("8x8 peak", Mmax_8x8_peak, Mmax_MF_8x8),
    ]:
        alpha_val = Mmax_GCM_val / Mmax_MF_val
        threshold = 1.0 / Mmax_MF_val
        z = (alpha_val - threshold) / sigma_alpha
        p_above = 1.0 - normal_dist.cdf(threshold, loc=alpha_val, scale=sigma_alpha)
        results_bayes[label] = {'alpha': alpha_val, 'threshold': threshold,
                                'z': z, 'p': p_above}
        print(f"  {label:>25s}: alpha={alpha_val:.4f}, thresh={threshold:.4f}, "
              f"z={z:+.3f}, p(>1) = {p_above:.6f}")

    # ================================================================
    #  STEP 9: NUCLEAR DFT CROSS-CHECKS AND DIAGNOSTICS
    # ================================================================
    print(f"\n{'='*78}")
    print(f"Step 9: Cross-checks and diagnostics")
    print(f"{'='*78}")

    # Check 1: Is the pairing window width physical?
    print(f"\n  1. Pairing window analysis:")
    if n_paired_B2 > 0:
        delta_tau_pair = tau_paired_B2[-1] - tau_paired_B2[0]
        print(f"     B2 pairing window: [{tau_paired_B2[0]:.4f}, {tau_paired_B2[-1]:.4f}]")
        print(f"     Width: {delta_tau_pair:.4f}")
        print(f"     Fraction of tau range: {delta_tau_pair / 0.5:.4f}")
    else:
        print(f"     No B2 pairing on fine grid!")

    if n_paired_8x8 > 0:
        delta_tau_pair_8x8 = tau_paired_8x8[-1] - tau_paired_8x8[0]
        print(f"     8x8 pairing window: [{tau_paired_8x8[0]:.4f}, {tau_paired_8x8[-1]:.4f}]")
        print(f"     Width: {delta_tau_pair_8x8:.4f}")
    else:
        print(f"     No 8x8 pairing on fine grid!")

    # Check 2: BCS energy at the fold
    fold_idx = np.argmin(np.abs(tau_fine - tau_fold))
    print(f"\n  2. BCS at fold (tau={tau_fine[fold_idx]:.4f}):")
    print(f"     Delta_max = {Delta_max_fine[fold_idx]:.6f}")
    print(f"     E_BCS = {E_BCS_fine[fold_idx]:.6f}")
    print(f"     M_max(B2) = {Mmax_B2_fine[fold_idx]:.6f}")
    print(f"     M_max(8x8) = {Mmax_8x8_fine[fold_idx]:.6f}")

    # Check 3: GCM wavefunction at the fold
    print(f"\n  3. GCM wavefunction weight at fold:")
    for r in gcm_results:
        fold_weight = r['prob_norm'][fold_idx]
        peak_weight = np.max(r['prob_norm'])
        print(f"     sigma={r['sigma']:.4f}: |f(fold)|^2={fold_weight:.4f}, "
              f"|f(peak)|^2={peak_weight:.4f}")

    # Check 4: Is the GCM dominated by the spectral action slope?
    print(f"\n  4. Spectral action vs BCS energy competition:")
    dS_dtau_fold = float(CubicSpline(tau_fine, S_fine)(tau_fold, 1))
    print(f"     dS/dtau at fold: {dS_dtau_fold:.4f}")
    print(f"     E_BCS at fold: {E_BCS_fine[fold_idx]:.6f}")
    print(f"     E_BCS / (dS * delta_tau_pair): ", end="")
    if n_paired_B2 > 0 and abs(dS_dtau_fold) > 1e-10:
        ratio_compete = abs(E_BCS_fine[fold_idx]) / (dS_dtau_fold * delta_tau_pair)
        print(f"{ratio_compete:.4f}")
        print(f"     {'BCS CAN compete' if ratio_compete > 0.3 else 'BCS CANNOT compete'}")
    else:
        print(f"N/A")

    # Check 5: What happens if we constrain the GCM to the pairing region?
    print(f"\n  5. Constrained GCM (pairing region only):")
    if n_paired_8x8 > 0:
        mask_8x8 = Mmax_8x8_fine > 1.0
        tau_constrained = tau_fine[mask_8x8]
        E_total_constrained = E_total_fine[mask_8x8]
        n_constrained = len(tau_constrained)

        if n_constrained >= 3:
            H_c, N_c = build_gcm_kernels(tau_constrained, E_total_constrained, sigma_phys)
            E_alpha_c, f_alpha_c, _, n_kept_c = solve_hill_wheeler(H_c, N_c)

            prob_c = np.abs(f_alpha_c[:, 0])**2
            prob_c_norm = prob_c / np.sum(prob_c)
            tau_avg_c = np.sum(prob_c_norm * tau_constrained)

            Mmax_B2_constrained = np.sum(prob_c_norm * Mmax_B2_fine[mask_8x8])
            Mmax_8x8_constrained = np.sum(prob_c_norm * Mmax_8x8_fine[mask_8x8])

            print(f"     {n_constrained} points in pairing region")
            print(f"     <tau> = {tau_avg_c:.4f}")
            print(f"     M_max_eff(B2) = {Mmax_B2_constrained:.6f}")
            print(f"     M_max_eff(8x8) = {Mmax_8x8_constrained:.6f}")
        else:
            print(f"     Only {n_constrained} points -- insufficient for GCM")
    else:
        print(f"     No 8x8 pairing region!")

    # ================================================================
    #  STEP 10: GATE EVALUATION
    # ================================================================
    print(f"\n{'='*78}")
    print(f"Step 10: GATE SC-HFB-36 (MASTER)")
    print(f"{'='*78}")

    # Use self-consistent M_max (B2 effective at self-consistent sigma)
    # as the primary gate value. Report full range.

    # The self-consistent Mmax is the weighted average over the GCM wavefunction
    # at the sigma that satisfies sigma_in ~ sigma_out.
    Mmax_gate = Mmax_GCM_B2  # self-consistent B2 effective

    if Mmax_gate > 1.05:
        gate_verdict = "PASS"
    elif Mmax_gate > 1.0:
        gate_verdict = "PASS"
    elif Mmax_gate > 0.95:
        gate_verdict = "MARGINAL"
    else:
        gate_verdict = "FAIL"

    # But also evaluate the "peak" metric -- M_max at the wavefunction peak
    # This is what a system AT the GCM ground state would experience
    if Mmax_B2_peak > 1.0 and Mmax_8x8_peak > 1.0:
        peak_verdict = "PASS"
    elif Mmax_8x8_peak > 1.0:
        peak_verdict = "MARGINAL (8x8 only)"
    else:
        peak_verdict = "FAIL"

    print(f"\n  PRIMARY GATE (effective M_max at self-consistent sigma):")
    print(f"    M_max(GCM, B2 eff) = {Mmax_GCM_B2:.6f}")
    print(f"    Verdict: {gate_verdict}")

    print(f"\n  SECONDARY (M_max at wavefunction peak):")
    print(f"    M_max(B2) at peak = {Mmax_B2_peak:.6f}")
    print(f"    M_max(8x8) at peak = {Mmax_8x8_peak:.6f}")
    print(f"    Verdict: {peak_verdict}")

    print(f"\n  FULL RANGE:")
    print(f"    B2 conservative:     {Mmax_GCM_conservative:.6f}")
    print(f"    B2 self-consistent:  {Mmax_GCM_B2:.6f}")
    print(f"    8x8 self-consistent: {Mmax_GCM_8x8:.6f}")
    print(f"    8x8 upper:           {Mmax_GCM_upper:.6f}")
    print(f"    B2 at peak:          {Mmax_B2_peak:.6f}")
    print(f"    8x8 at peak:         {Mmax_8x8_peak:.6f}")

    # ================================================================
    #  SAVE
    # ================================================================
    print(f"\n{'='*78}")
    print(f"Saving results...")

    save_dict = {
        # Grids
        'tau_coarse': tau_grid,
        'tau_fine': tau_fine,
        'tau_fold': tau_fold,
        'n_fine': n_fine,

        # Energy surfaces
        'S_singlet_coarse': S_singlet,
        'S_fine': S_fine,
        'E_BCS_coarse': E_BCS_coarse,
        'E_BCS_fine': E_BCS_fine,
        'E_total_coarse': E_total_coarse,
        'E_total_fine': E_total_fine,
        'Delta_max_fine': Delta_max_fine,

        # M_max surfaces
        'Mmax_B2_coarse': Mmax_B2_coarse,
        'Mmax_B2_fine': Mmax_B2_fine,
        'Mmax_8x8_coarse': Mmax_8x8_coarse,
        'Mmax_8x8_fine': Mmax_8x8_fine,
        'rho_B2_fine': rho_B2_fine,

        # Pairing window
        'n_paired_B2': n_paired_B2,
        'n_paired_8x8': n_paired_8x8,

        # GCM parameters
        'sigma_scan': sigma_scan,
        'sigma_rpa': sigma_rpa,
        'sigma_pair': sigma_pair,
        'sigma_etot': sigma_etot,
        'sigma_phys': sigma_phys,
        'best_sc_idx': best_sc_idx,

        # GCM results (self-consistent sigma)
        'Mmax_GCM_B2': Mmax_GCM_B2,
        'Mmax_GCM_8x8': Mmax_GCM_8x8,
        'Mmax_GCM_conservative': Mmax_GCM_conservative,
        'Mmax_GCM_upper': Mmax_GCM_upper,
        'Mmax_B2_peak': Mmax_B2_peak,
        'Mmax_8x8_peak': Mmax_8x8_peak,
        'tau_avg_sc': gcm_sc['tau_avg'],
        'tau_sigma_sc': gcm_sc['tau_sigma'],
        'peak_tau_sc': gcm_sc['peak_tau'],
        'E_GCM_corr_sc': gcm_sc['E_GCM_corr'],
        'prob_norm_sc': gcm_sc['prob_norm'],

        # Self-consistency
        'alpha_sc_B2': alpha_sc_B2,
        'alpha_sc_8x8': alpha_sc_8x8,
        'alpha_cons': alpha_cons,
        'alpha_auth_B2': alpha_auth_B2,
        'alpha_auth_8x8': alpha_auth_8x8,

        # Bayesian
        'p_B2_conservative': results_bayes['B2 conservative']['p'],
        'p_B2_sc': results_bayes['B2 self-consistent']['p'],
        'p_8x8_sc': results_bayes['8x8 self-consistent']['p'],
        'p_8x8_upper': results_bayes['8x8 upper']['p'],
        'p_B2_peak': results_bayes['B2 peak']['p'],
        'p_8x8_peak': results_bayes['8x8 peak']['p'],

        # MF reference
        'Mmax_MF_B2_AUTH': Mmax_MF_B2,
        'Mmax_MF_8x8_AUTH': Mmax_MF_8x8,
        'Mmax_MF_B2_fine_peak': Mmax_MF_B2_peak,
        'Mmax_MF_8x8_fine_peak': Mmax_MF_8x8_peak,

        # Gate
        'gate_verdict': gate_verdict,
        'gate_Mmax': Mmax_gate,
        'peak_verdict': peak_verdict,
    }

    out_npz = os.path.join(SCRIPT_DIR, 's36_gcm_self_consistent.npz')
    np.savez_compressed(out_npz, **save_dict)
    print(f"  Data: {out_npz} ({os.path.getsize(out_npz) / 1024:.1f} KB)")

    # ================================================================
    #  PLOT
    # ================================================================
    print(f"  Generating plot...")
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(2, 3, figsize=(18, 10))

    # Panel 1: Energy surfaces
    ax = axes[0, 0]
    ax.plot(tau_fine, S_fine, 'b-', label='S(tau)', linewidth=1.5)
    ax.plot(tau_fine, E_total_fine, 'r-', label='E_total = S + E_BCS', linewidth=2)
    ax.plot(tau_grid, S_singlet, 'bo', ms=6)
    ax.plot(tau_grid, E_total_coarse, 'rs', ms=6)
    ax.axvline(tau_fold, color='gray', linestyle=':', alpha=0.7, label=f'tau_fold')
    ax.set_xlabel('tau')
    ax.set_ylabel('Energy')
    ax.set_title('Energy Surface E(tau)')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Panel 2: M_max vs tau (fine grid)
    ax = axes[0, 1]
    ax.plot(tau_fine, Mmax_B2_fine, 'r-', label='M_max(B2)', linewidth=2)
    ax.plot(tau_fine, Mmax_8x8_fine, 'b-', label='M_max(8x8)', linewidth=2)
    ax.axhline(1.0, color='k', linestyle='--', linewidth=1.5, label='Threshold')
    ax.axvline(tau_fold, color='gray', linestyle=':', alpha=0.7)
    # Shade pairing region
    if n_paired_B2 > 0:
        ax.axvspan(tau_paired_B2[0], tau_paired_B2[-1], alpha=0.15, color='red',
                   label=f'B2 paired [{tau_paired_B2[0]:.3f},{tau_paired_B2[-1]:.3f}]')
    if n_paired_8x8 > 0:
        ax.axvspan(tau_paired_8x8[0], tau_paired_8x8[-1], alpha=0.1, color='blue')
    ax.set_xlabel('tau')
    ax.set_ylabel('M_max')
    ax.set_title('Thouless M_max(tau) — Fine Grid')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    # Panel 3: DOS and Delta
    ax = axes[0, 2]
    ax2 = ax.twinx()
    ax.plot(tau_fine, rho_B2_fine, 'g-', linewidth=2, label='rho_B2')
    ax2.plot(tau_fine, Delta_max_fine, 'm-', linewidth=2, label='Delta_max')
    ax.axvline(tau_fold, color='gray', linestyle=':', alpha=0.7)
    ax.set_xlabel('tau')
    ax.set_ylabel('rho_B2 (DOS)', color='g')
    ax2.set_ylabel('Delta_max (BCS gap)', color='m')
    ax.set_title('DOS and BCS Gap')
    ax.legend(loc='upper left', fontsize=8)
    ax2.legend(loc='upper right', fontsize=8)
    ax.grid(True, alpha=0.3)

    # Panel 4: GCM wavefunctions
    ax = axes[1, 0]
    colors_gcm = plt.cm.viridis(np.linspace(0.2, 0.8, len(gcm_results)))
    for i, r in enumerate(gcm_results):
        lw = 3 if i == best_sc_idx else 1.5
        ls = '-' if i == best_sc_idx else '--'
        ax.plot(tau_fine, r['prob_norm'], color=colors_gcm[i], linewidth=lw,
                linestyle=ls, label=f's={r["sigma"]:.4f}'
                f'{" (SC)" if i == best_sc_idx else ""}')
    ax.axvline(tau_fold, color='gray', linestyle=':', alpha=0.7)
    ax.set_xlabel('tau')
    ax.set_ylabel('|f_0(tau)|^2')
    ax.set_title('GCM Ground State Wavefunctions')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    # Panel 5: BCS energy
    ax = axes[1, 1]
    ax.plot(tau_fine, E_BCS_fine, 'r-', linewidth=2)
    ax.plot(tau_grid, E_BCS_coarse, 'rs', ms=8, label='Coarse grid')
    ax.axvline(tau_fold, color='gray', linestyle=':', alpha=0.7)
    ax.set_xlabel('tau')
    ax.set_ylabel('E_BCS')
    ax.set_title('BCS Condensation Energy')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Panel 6: Gate summary
    ax = axes[1, 2]
    labels_bar = ['MF B2\n(AUTH)', 'MF 8x8\n(AUTH)',
                  'GCM B2\n(SC eff)', 'GCM 8x8\n(SC eff)',
                  'GCM B2\n(peak)', 'GCM 8x8\n(peak)']
    values_bar = [Mmax_MF_B2, Mmax_MF_8x8,
                  Mmax_GCM_B2, Mmax_GCM_8x8,
                  Mmax_B2_peak, Mmax_8x8_peak]
    colors_bar = ['#2196F3', '#1976D2',
                  '#FF9800', '#F57C00',
                  '#4CAF50', '#388E3C']

    bars = ax.bar(labels_bar, values_bar, color=colors_bar, edgecolor='black')
    ax.axhline(1.0, color='red', linestyle='--', linewidth=2, label='Threshold')
    ax.set_ylabel('M_max')
    ax.set_title(f'Gate SC-HFB-36: {gate_verdict}')
    for bar, val in zip(bars, values_bar):
        ax.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.02,
                f'{val:.3f}', ha='center', va='bottom', fontsize=8, fontweight='bold')
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3, axis='y')

    plt.tight_layout()
    out_png = os.path.join(SCRIPT_DIR, 's36_gcm_self_consistent.png')
    plt.savefig(out_png, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Plot: {out_png}")

    # ================================================================
    #  FINAL SUMMARY
    # ================================================================
    elapsed = time.time() - t0
    print(f"\n{'='*78}")
    print(f"SC-HFB-36 FINAL SUMMARY (MASTER GATE)")
    print(f"{'='*78}")

    print(f"\n  GATE SC-HFB-36: {gate_verdict}")
    print(f"    M_max(GCM, B2 eff, SC sigma) = {Mmax_GCM_B2:.6f}")
    print(f"    M_max(GCM, 8x8 eff, SC sigma) = {Mmax_GCM_8x8:.6f}")
    print(f"    M_max(B2 at peak) = {Mmax_B2_peak:.6f}")
    print(f"    M_max(8x8 at peak) = {Mmax_8x8_peak:.6f}")

    print(f"\n  KEY NUMBERS:")
    print(f"    alpha(B2, SC, fine peak):        {alpha_sc_B2:.6f}")
    print(f"    alpha(B2, vs AUTH-36):           {alpha_auth_B2:.6f}")
    print(f"    E_GCM_corr (SC sigma):           {gcm_sc['E_GCM_corr']:.6f}")
    print(f"    <tau> (SC sigma):                {gcm_sc['tau_avg']:.6f}")
    print(f"    peak_tau (SC sigma):             {gcm_sc['peak_tau']:.4f}")
    print(f"    Pairing window B2:               [{tau_paired_B2[0]:.4f}, {tau_paired_B2[-1]:.4f}]" if n_paired_B2 > 0 else "    No B2 pairing window!")
    print(f"    p(M_max(SC)>1 | B2 cons):        {results_bayes['B2 conservative']['p']:.6f}")
    print(f"    p(M_max(SC)>1 | B2 peak):        {results_bayes['B2 peak']['p']:.6f}")
    print(f"    p(M_max(SC)>1 | 8x8 peak):       {results_bayes['8x8 peak']['p']:.6f}")

    print(f"\n  PHYSICAL INTERPRETATION:")
    print(f"    The van Hove fold creates a NARROW pairing window")
    print(f"    in tau-space. The GCM wavefunction, which spreads")
    print(f"    over this window and beyond, samples both paired and")
    print(f"    unpaired regions. The effective M_max is the weighted")
    print(f"    average, which is reduced from the peak value by the")
    print(f"    fraction of weight outside the pairing window.")
    print(f"    The spectral action slope competes with the BCS pocket,")
    print(f"    pulling weight toward small tau (lower S) where")
    print(f"    pairing is absent.")

    print(f"\n  Runtime: {elapsed:.1f}s")
    print(f"{'='*78}")

    return gate_verdict, Mmax_GCM_B2, Mmax_GCM_8x8, alpha_sc_B2


if __name__ == '__main__':
    verdict, M_B2, M_8x8, alpha = main()
