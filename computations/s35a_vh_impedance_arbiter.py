#!/usr/bin/env python3
"""
Session 35a: VH-IMP-35a — Van Hove Integral + Impedance Arbitration
====================================================================
THE DECISIVE COMPUTATION for the 11% BCS shortfall question.

Two questions:
  (A) Van Hove DOS: What is the correct smooth-wall DOS rho_per_mode for B2?
      The W-32b step-function average v_wall = 0.059 gives rho = 5.40/mode.
      But the B2 fold at tau ~ 0.190 has v_B2 = 0 (van Hove singularity).
      A smooth wall profile captures the log-divergent DOS enhancement.

  (B) Impedance: Is the CT-4 impedance factor (1.56) physically correct?
      Tesla claims overcounting (intra-B2 mode reshuffling). We test
      via eigenvector overlap analysis: if B2 modes transmit through the
      wall with T_branch > 0.99, impedance ~ 1.0.

  (C) Combined: 2D grid of (v_min, impedance) -> M_max.

Gate VH-IMP-35a:
  PASS:  M_max >= 1.0 at the physically justified (v_min, impedance) point
  FAIL:  M_max < 1.0 at ALL defensible combinations

Author: bap (baptista-spacetime-analyst), Session 35a
Date: 2026-03-06
Source data: s23a_kosmann_singlet.npz, s32a_umklapp_vertex.npz,
             s33a_landau_sector.npz
"""

import os
import time
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.integrate import quad
from scipy.linalg import eigh
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ======================================================================
#  Paths
# ======================================================================
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = SCRIPT_DIR  # tier0-computation

SINGLET_FILE = os.path.join(DATA_DIR, "s23a_kosmann_singlet.npz")
UMKLAPP_FILE = os.path.join(DATA_DIR, "s32a_umklapp_vertex.npz")
SECTOR_FILE  = os.path.join(DATA_DIR, "s33a_landau_sector.npz")

OUTPUT_NPZ = os.path.join(DATA_DIR, "s35a_vh_impedance_arbiter.npz")
OUTPUT_PNG = os.path.join(DATA_DIR, "s35a_vh_impedance_arbiter.png")

# ======================================================================
#  Constants
# ======================================================================
TAU_VALUES = np.array([0.0, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.50])

# Branch indices in A_antisym 8x8 basis
B3_IDX = np.array([0, 1, 2])
B2_IDX = np.array([3, 4, 5, 6])
B1_IDX = np.array([7])

# Wall 2 endpoints (the tightest, highest-rho configuration)
TAU_WALL_LO = 0.15
TAU_WALL_HI = 0.25

# Multi-sector factor (from SECT-33a, conservative)
MULTI_SECTOR_FACTOR = 1.046

# Regulator
ETA_REG_FRAC = 0.001


# ======================================================================
#  PART A: Van Hove DOS Arbitration
# ======================================================================

def load_B2_eigenvalues():
    """Load B2 mean eigenvalue at each tau from the data files."""
    umk = np.load(UMKLAPP_FILE, allow_pickle=True)
    B2_evals = umk['B2_evals']  # shape (9, 4), all 4 modes degenerate
    B2_mean = np.mean(B2_evals, axis=1)  # shape (9,)
    v_B2 = umk['v_B2']  # shape (9,), group velocity of B2 mean
    tau = umk['tau_values']
    return tau, B2_mean, v_B2, B2_evals


def compute_van_hove_dos(tau_arr, E_B2, v_B2_arr):
    """Compute smooth-wall DOS via cubic spline + integral.

    The B2 eigenvalue E(tau) has a minimum near tau ~ 0.190.
    At the minimum, v = dE/dtau = 0 => 1D van Hove singularity
    with rho ~ 1/(pi * |v|) diverging as 1/sqrt(|tau - tau_fold|).

    Method:
    1. Fit cubic spline cs_E(tau) to the B2 mean eigenvalue.
    2. Compute v(tau) = cs_E'(tau). Find tau_fold where v = 0.
    3. Compute d2E/dtau2 at fold.
    4. Integrate rho_smooth = integral_{tau_lo}^{tau_hi} 1/(pi * max(|v|, v_min)) dtau
       for a scan of v_min values.
    5. Normalize: rho_per_mode = rho_smooth / (tau_hi - tau_lo)

    Returns:
        results dict with tau_fold, d2E, v_min estimates, rho_smooth arrays
    """
    # Step 1: Cubic spline for E(tau)
    cs_E = CubicSpline(tau_arr, E_B2)

    # Step 2: v(tau) = dE/dtau
    tau_fine = np.linspace(0.0, 0.5, 5000)
    v_fine = cs_E(tau_fine, 1)  # first derivative

    # Find tau_fold: where v = 0 in [0.10, 0.30]
    mask = (tau_fine >= 0.10) & (tau_fine <= 0.30)
    v_masked = v_fine[mask]
    tau_masked = tau_fine[mask]

    # Find sign changes
    sign_changes = np.where(np.diff(np.sign(v_masked)))[0]
    if len(sign_changes) == 0:
        # No exact sign change; find minimum |v|
        idx_min = np.argmin(np.abs(v_masked))
        tau_fold = tau_masked[idx_min]
    else:
        # Linear interpolation for zero crossing
        i = sign_changes[0]
        tau_fold = tau_masked[i] - v_masked[i] * (tau_masked[i+1] - tau_masked[i]) / (v_masked[i+1] - v_masked[i])

    # Step 3: d2E/dtau2 at fold
    d2E_fold = cs_E(tau_fold, 2)  # second derivative
    E_fold = cs_E(tau_fold)
    v_fold = cs_E(tau_fold, 1)

    # Step 4: Scan v_min
    v_min_scan = np.logspace(-5, -1, 200)

    # Wall integration limits
    tau_lo = TAU_WALL_LO
    tau_hi = TAU_WALL_HI
    wall_width = tau_hi - tau_lo

    rho_smooth = np.zeros(len(v_min_scan))
    for j, vmin in enumerate(v_min_scan):
        # Integrand: 1/(pi * max(|v(tau)|, v_min))
        def integrand(tau):
            v = cs_E(tau, 1)
            return 1.0 / (np.pi * max(abs(v), vmin))

        result, err = quad(integrand, tau_lo, tau_hi, limit=200, epsabs=1e-12)
        rho_smooth[j] = result / wall_width  # per unit tau = per mode

    # Step 5: Physical v_min estimates
    # (a) v_min_sector: from finite sector width delta_tau ~ 0.004 (SECT-33a)
    delta_tau_sector = 0.004
    v_min_sector = abs(d2E_fold) * delta_tau_sector

    # (b) v_min_splitting: This estimate addresses whether the exact 4-fold
    #     B2 degeneracy on the Jensen curve provides a natural cutoff.
    #     ON the Jensen curve, B2 splitting = 0 exactly (U(2) symmetry).
    #     The B2 eigenvalue CHANGES with tau (bandwidth W_B2 = 0.058 over
    #     full tau range), but all 4 modes move together.
    #
    #     The relevant quantity is the B2 eigenvalue CHANGE across the wall:
    #     delta_E_wall = |E_B2(tau_hi) - E_B2(tau_lo)| = |0.8473 - 0.8462| = 0.0012
    #     This is tiny because the fold sits INSIDE the wall.
    #
    #     A more conservative estimate: the B2-B1 shell gap at the fold
    #     provides the energy scale below which the 1D van Hove picture
    #     breaks down (inter-band hybridization could regularize the singularity):
    kosmann = np.load(SINGLET_FILE, allow_pickle=True)
    E_at_fold_idx = 3  # tau = 0.20, closest to fold
    evals_fold = np.sort(kosmann[f'eigenvalues_{E_at_fold_idx}'][
        kosmann[f'eigenvalues_{E_at_fold_idx}'] > 0])
    B1_fold = evals_fold[0]
    B2_fold = evals_fold[1]  # first B2 mode
    shell_gap_fold = B2_fold - B1_fold  # = 0.026
    #     Convert to velocity: v ~ delta_E / delta_tau where delta_tau is
    #     the tau range over which E changes by shell_gap.
    #     From d2E/dtau2 = 1.176: delta_tau = sqrt(2 * shell_gap / d2E)
    #     This is ~0.21 in tau units. v at this point = d2E * delta_tau ~ 0.25
    #     But this is the INTERBAND gap, not a B2 splitting.
    #     The B2 modes have ZERO splitting, so this estimate is inapplicable.
    v_min_splitting_shell = shell_gap_fold / wall_width  # 0.026/0.10 = 0.26
    #     ^ This is NOT a valid v_min because v_min should be a GROUP VELOCITY
    #       cutoff, not an energy scale divided by a tau interval.
    #       Include for completeness but flag as INAPPLICABLE.
    #
    #     The B2 eigenvalue change across the wall is the correct "splitting":
    umk = np.load(UMKLAPP_FILE, allow_pickle=True)
    B2_bw = umk['W_B2']  # Total B2 bandwidth over [0, 0.5]
    delta_E_wall = abs(E_B2[np.argmin(np.abs(tau_arr - TAU_WALL_HI))]
                       - E_B2[np.argmin(np.abs(tau_arr - TAU_WALL_LO))])
    v_min_splitting_prompt = delta_E_wall / wall_width  # eigenvalue change / tau interval

    # (c) v_min_slope: from |dv/dtau| at fold times sector width
    d3E_fold = cs_E(tau_fold, 3)  # third derivative = dv/dtau rate of change
    v_min_slope = abs(d3E_fold) * delta_tau_sector**2 / 2.0  # Taylor: v ~ (d2E)*dt + (d3E)*dt^2/2

    # Physical v_min: report ALL candidates, choose based on physics
    physical_v_min_candidates = {
        'v_min_sector': v_min_sector,           # = d2E * delta_tau_sector = 0.0047
        'v_min_delta_E_wall': v_min_splitting_prompt,  # = delta_E_wall / wall_width = 0.012
        'v_min_slope': v_min_slope,              # = d3E * delta_tau^2 / 2 ~ 3e-6
    }
    # Also store the inapplicable shell-gap estimate for transparency
    inapplicable_candidates = {
        'v_min_shell_gap (INAPPLICABLE)': v_min_splitting_shell,
    }

    # PHYSICAL CHOICE: v_min_sector is the well-motivated estimate.
    # It represents the minimum group velocity achievable given the finite
    # sector width delta_tau = 0.004 from SECT-33a. At the fold, v = 0
    # exactly, but modes offset by delta_tau have v = d2E * delta_tau.
    # The delta_E_wall estimate (0.012) is the eigenvalue change across the
    # wall divided by the wall width -- this IS a velocity and is numerically
    # close to v_min_sector. Use the LARGER (more conservative) of these two.
    valid_candidates = {k: v for k, v in physical_v_min_candidates.items()}
    v_min_physical = max(valid_candidates.values())
    v_min_physical_name = max(valid_candidates, key=valid_candidates.get)

    # Step-function reference
    v_step = (abs(cs_E(tau_lo, 1)) + abs(cs_E(tau_hi, 1))) / 2.0
    rho_step = 1.0 / (np.pi * v_step)

    # rho at physical v_min
    def integrand_phys(tau):
        v = cs_E(tau, 1)
        return 1.0 / (np.pi * max(abs(v), v_min_physical))
    rho_at_physical, _ = quad(integrand_phys, tau_lo, tau_hi, limit=200)
    rho_at_physical /= wall_width

    results = {
        'tau_fold': tau_fold,
        'E_fold': E_fold,
        'v_fold': v_fold,
        'd2E_fold': d2E_fold,
        'd3E_fold': d3E_fold,
        'v_min_scan': v_min_scan,
        'rho_smooth': rho_smooth,
        'v_min_sector': v_min_sector,
        'v_min_delta_E_wall': v_min_splitting_prompt,
        'delta_E_wall': delta_E_wall,
        'v_min_slope': v_min_slope,
        'v_min_physical': v_min_physical,
        'v_min_physical_name': v_min_physical_name,
        'v_step': v_step,
        'rho_step': rho_step,
        'rho_at_physical': rho_at_physical,
        'cs_E': cs_E,
        'tau_fine': tau_fine,
        'v_fine': v_fine,
        'physical_v_min_candidates': physical_v_min_candidates,
        'B2_bw': float(B2_bw),
        'delta_E_wall': delta_E_wall,
        'shell_gap_fold': shell_gap_fold,
        'v_min_shell_gap': v_min_splitting_shell,
    }
    return results


# ======================================================================
#  PART B: Impedance Arbitration
# ======================================================================

def compute_impedance_analysis():
    """Compute eigenvector overlaps between Wall 2 endpoints.

    Method:
    1. Load eigenvectors at tau=0.15 (idx=2) and tau=0.25 (idx=4).
    2. Compute 16x16 overlap matrix O_nm = <psi_n(0.15)|psi_m(0.25)>.
    3. Identify B2 indices (modes 9-12 in full 16, positive sector).
    4. Compute mode-diagonal transmission: T_diag_k = |O_kk|^2 for B2.
    5. Branch-resolved: T_branch_k = sum_{l in B2} |O_kl|^2 for B2.
    6. Cross-branch leakage to B1, B3.
    7. Determine whether impedance is justified.
    """
    kosmann = np.load(SINGLET_FILE, allow_pickle=True)

    # Eigenvectors at wall endpoints
    evecs_lo = kosmann['eigenvectors_2']  # tau = 0.15
    evecs_hi = kosmann['eigenvectors_4']  # tau = 0.25

    # Full 16x16 overlap matrix
    O = evecs_lo.conj().T @ evecs_hi
    # O_{nm} = <psi_n(0.15) | psi_m(0.25)>

    # Unitarity check
    O_unit = O @ O.conj().T
    unit_err = np.max(np.abs(O_unit - np.eye(16)))

    # B2 indices in the full 16 eigenvalue array:
    # Eigenvalues sorted: indices 0-7 negative (descending magnitude), 8-15 positive (ascending)
    # Positive eigenvalue ordering (ascending): B1(8), B2(9,10,11,12), B3(13,14,15)
    # But the branch_labels from umklapp are for the POSITIVE 8 eigenvalues sorted ascending:
    # branch_labels = ['B1', 'B2', 'B2', 'B2', 'B2', 'B3', 'B3', 'B3']
    # So in the full 16: positive indices 8+0=8(B1), 8+1..4=9..12(B2), 8+5..7=13..15(B3)

    B1_full_pos = [8]
    B2_full_pos = [9, 10, 11, 12]
    B3_full_pos = [13, 14, 15]

    # Negative sector mirrors (reversed): indices 0-7
    B3_full_neg = [0, 1, 2]
    B2_full_neg = [3, 4, 5, 6]
    B1_full_neg = [7]

    # Mode-diagonal transmission for B2+
    T_diag_B2 = np.array([np.abs(O[k, k])**2 for k in B2_full_pos])
    T_diag_B2_mean = np.mean(T_diag_B2)

    # Branch-resolved transmission: sum over B2+ only
    T_branch_B2 = np.zeros(4)
    for i, k in enumerate(B2_full_pos):
        T_branch_B2[i] = sum(np.abs(O[k, l])**2 for l in B2_full_pos)
    T_branch_B2_mean = np.mean(T_branch_B2)

    # Cross-branch leakage from B2+ to B1+
    leak_B1 = np.zeros(4)
    for i, k in enumerate(B2_full_pos):
        leak_B1[i] = sum(np.abs(O[k, l])**2 for l in B1_full_pos)
    leak_B1_mean = np.mean(leak_B1)

    # Cross-branch leakage from B2+ to B3+
    leak_B3 = np.zeros(4)
    for i, k in enumerate(B2_full_pos):
        leak_B3[i] = sum(np.abs(O[k, l])**2 for l in B3_full_pos)
    leak_B3_mean = np.mean(leak_B3)

    # Leakage to negative sector
    leak_neg = np.zeros(4)
    for i, k in enumerate(B2_full_pos):
        leak_neg[i] = sum(np.abs(O[k, l])**2 for l in range(8))
    leak_neg_mean = np.mean(leak_neg)

    # Full row sum check (should be 1.0 by unitarity)
    row_sums = np.array([np.sum(np.abs(O[k, :])**2) for k in B2_full_pos])

    # Also compute the B2 negative-sector transmission
    T_diag_B2_neg = np.array([np.abs(O[k, k])**2 for k in B2_full_neg])
    T_branch_B2_neg = np.zeros(4)
    for i, k in enumerate(B2_full_neg):
        T_branch_B2_neg[i] = sum(np.abs(O[k, l])**2 for l in B2_full_neg)

    # Impedance determination:
    # If T_branch > 0.99: modes pass through wall with negligible reflection
    #   => impedance ~ 1.0 (no enhancement from multiple reflections)
    # If T_branch < 0.9: significant mode mixing / reflection
    #   => impedance ~ 1/(1-R) where R = 1 - T_branch
    R_effective = 1.0 - T_branch_B2_mean
    if R_effective > 0.01:
        impedance_from_overlap = 1.0 / (1.0 - R_effective)
    else:
        impedance_from_overlap = 1.0

    # Also check the full overlap matrix B2 block
    O_B2_block = O[np.ix_(B2_full_pos, B2_full_pos)]

    results = {
        'O': O,
        'unit_err': unit_err,
        'T_diag_B2': T_diag_B2,
        'T_diag_B2_mean': T_diag_B2_mean,
        'T_branch_B2': T_branch_B2,
        'T_branch_B2_mean': T_branch_B2_mean,
        'leak_B1': leak_B1,
        'leak_B1_mean': leak_B1_mean,
        'leak_B3': leak_B3,
        'leak_B3_mean': leak_B3_mean,
        'leak_neg': leak_neg,
        'leak_neg_mean': leak_neg_mean,
        'row_sums': row_sums,
        'R_effective': R_effective,
        'impedance_from_overlap': impedance_from_overlap,
        'O_B2_block': O_B2_block,
        'T_diag_B2_neg': T_diag_B2_neg,
        'T_branch_B2_neg': T_branch_B2_neg,
    }
    return results


# ======================================================================
#  PART C: Combined M_max Grid
# ======================================================================

def build_full_V_8x8(kosmann, tau_idx):
    """Build V_nm = sum_{a=0..7} |<n|K_a|m>|^2 (A_antisym basis)."""
    V = np.zeros((8, 8))
    for a in range(8):
        A = kosmann[f'A_antisym_{tau_idx}_{a}']
        V += np.abs(A) ** 2
    return V


def get_branch_eigenvalues(kosmann, tau_idx):
    """Get eigenvalues in branch-adapted basis: B3(0-2), B2(3-6), B1(7)."""
    evals_all = kosmann[f'eigenvalues_{tau_idx}']
    pos_evals = np.sort(evals_all[evals_all > 0])
    E = np.zeros(8)
    E[0:3] = pos_evals[5:8]   # B3
    E[3:7] = pos_evals[1:5]   # B2
    E[7] = pos_evals[0]       # B1
    return E


def thouless_5x5(V_8x8, E_branch, mu, rho_B2, rho_B1=1.0):
    """Linearized BdG Thouless criterion in B2+B1 subspace.

    M_nm = V_nm * rho_m / (2 * |xi_m|)
    M_max = max Re(eigenvalue of M)
    PASS if M_max > 1.
    """
    idx = np.concatenate([B2_IDX, B1_IDX])
    V_sub = V_8x8[np.ix_(idx, idx)]
    E_sub = E_branch[idx]

    xi = E_sub - mu
    lambda_min = np.min(np.abs(E_sub))
    eta = max(ETA_REG_FRAC * lambda_min, 1e-15)
    abs_xi = np.maximum(np.abs(xi), eta)

    rho = np.array([rho_B2] * 4 + [rho_B1])

    M = np.zeros((5, 5))
    for m in range(5):
        M[:, m] = V_sub[:, m] * rho[m] / (2.0 * abs_xi[m])

    M_evals = np.linalg.eigvals(M)
    M_max = np.max(np.real(M_evals))
    return M_max, M_evals, M, V_sub, E_sub


def build_K_a_V_spinor(kosmann, tau_idx):
    """Build V_nm = sum_a |<psi_n|K_a|psi_m>|^2 in the EIGENVECTOR basis.

    Uses K_a_matrix (16x16 in eigenvector basis) not A_antisym (8x8 in
    positive-sector branch basis). The prompt requests K_a_matrix.

    Returns the 5x5 B1+B2 submatrix.
    """
    evecs = kosmann[f'eigenvectors_{tau_idx}']
    V_full = np.zeros((16, 16))
    for a in range(8):
        K = kosmann[f'K_a_matrix_{tau_idx}_{a}']
        # K is already in some basis; project into eigenbasis
        K_eig = evecs.conj().T @ K @ evecs
        V_full += np.abs(K_eig) ** 2

    # B2+B1 indices in the positive sector (8-15):
    # pos sorted ascending: 8=B1, 9-12=B2, 13-15=B3
    B1_pos = [8]
    B2_pos = [9, 10, 11, 12]
    idx_5 = B2_pos + B1_pos  # [9,10,11,12,8]
    V_5x5 = V_full[np.ix_(idx_5, idx_5)]
    return V_5x5, V_full


def compute_M_max_grid(V_8x8, E_branch, v_min_scan, rho_smooth_per_mode,
                        impedance_scan):
    """Compute M_max on a 2D grid of (v_min, impedance).

    Parameters:
        V_8x8: pairing matrix in branch basis
        E_branch: eigenvalues in branch basis
        v_min_scan: array of v_min values (same as in Part A)
        rho_smooth_per_mode: rho(v_min) array from Part A integration
        impedance_scan: array of impedance factors

    Returns:
        M_max_grid: shape (len(v_min_scan), len(impedance_scan))
    """
    n_v = len(v_min_scan)
    n_imp = len(impedance_scan)
    M_grid = np.zeros((n_v, n_imp))

    for i in range(n_v):
        for j in range(n_imp):
            rho_eff = rho_smooth_per_mode[i] * MULTI_SECTOR_FACTOR * impedance_scan[j]
            M_max, _, _, _, _ = thouless_5x5(V_8x8, E_branch, 0.0, rho_eff, 1.0)
            M_grid[i, j] = M_max

    return M_grid


# ======================================================================
#  Main
# ======================================================================

def main():
    t0 = time.time()
    print("=" * 80)
    print("VH-IMP-35a: Van Hove Integral + Impedance Arbitration")
    print("=" * 80)
    print()

    # Load base data
    kosmann = np.load(SINGLET_FILE, allow_pickle=True)

    # ================================================================
    # PART A: Van Hove DOS
    # ================================================================
    print("=" * 70)
    print("PART A: Van Hove DOS — Smooth-Wall Integration")
    print("=" * 70)
    print()

    tau_arr, E_B2, v_B2_arr, B2_evals_arr = load_B2_eigenvalues()
    vh = compute_van_hove_dos(tau_arr, E_B2, v_B2_arr)

    print(f"B2 mean eigenvalue E(tau):")
    for i, t in enumerate(tau_arr):
        print(f"  tau={t:.2f}: E={E_B2[i]:.6f}, v={v_B2_arr[i]:.6f}")
    print()

    print(f"Cubic spline analysis:")
    print(f"  tau_fold (v=0): {vh['tau_fold']:.6f}")
    print(f"  E(tau_fold):    {vh['E_fold']:.6f}")
    print(f"  v(tau_fold):    {vh['v_fold']:.2e}  (should be ~0)")
    print(f"  d2E/dtau2:      {vh['d2E_fold']:.6f}")
    print(f"  d3E/dtau3:      {vh['d3E_fold']:.6f}")
    print()

    print(f"Physical v_min estimates (valid):")
    for name, val in vh['physical_v_min_candidates'].items():
        marker = " <<<" if name == vh['v_min_physical_name'] else ""
        print(f"  {name}: {val:.6f}{marker}")
    if 'inapplicable_candidates' in dir():
        print(f"Inapplicable estimates (for transparency):")
        for name, val in vh.get('inapplicable_candidates', {}).items():
            print(f"  {name}: {val:.6f}  [energy/tau, NOT a velocity cutoff]")
    print(f"  PHYSICAL v_min (most conservative valid): {vh['v_min_physical']:.6f} "
          f"({vh['v_min_physical_name']})")
    print(f"  delta_E_wall = |E_B2(0.25) - E_B2(0.15)| = {vh.get('delta_E_wall', 'N/A')}")
    print(f"  Shell gap B2-B1 at fold: {vh['shell_gap_fold']:.6f} (INAPPLICABLE as v_min)")
    print()

    print(f"Step-function reference (W-32b):")
    print(f"  v_step = (|v(0.15)| + |v(0.25)|)/2 = {vh['v_step']:.6f}")
    print(f"  rho_step = 1/(pi * v_step) = {vh['rho_step']:.4f} per mode")
    print()

    print(f"Smooth-wall van Hove integral:")
    print(f"  rho at v_min = {vh['v_min_physical']:.6f}: {vh['rho_at_physical']:.4f} per mode")
    print(f"  Enhancement over step: {vh['rho_at_physical']/vh['rho_step']:.4f}x")
    print()

    # Print rho vs v_min at key points
    v_min_checkpoints = [1e-4, 1e-3, 1e-2, 0.059, 0.1]
    print(f"  {'v_min':>10s}  {'rho/mode':>10s}  {'ratio to step':>14s}")
    print(f"  {'-'*38}")
    for vc in v_min_checkpoints:
        idx = np.argmin(np.abs(vh['v_min_scan'] - vc))
        r = vh['rho_smooth'][idx]
        print(f"  {vc:10.5f}  {r:10.4f}  {r/vh['rho_step']:14.4f}")
    print()

    # ================================================================
    # PART B: Impedance Analysis
    # ================================================================
    print("=" * 70)
    print("PART B: Impedance Arbitration — Eigenvector Overlap Analysis")
    print("=" * 70)
    print()

    imp = compute_impedance_analysis()

    print(f"Overlap matrix unitarity error: {imp['unit_err']:.2e}")
    print()

    print(f"B2+ (positive sector) mode-diagonal transmission:")
    for i, T in enumerate(imp['T_diag_B2']):
        print(f"  Mode {i}: T_diag = {T:.6f}")
    print(f"  Mean T_diag: {imp['T_diag_B2_mean']:.6f}")
    print()

    print(f"B2+ branch-resolved transmission (sum over B2+ targets):")
    for i, T in enumerate(imp['T_branch_B2']):
        print(f"  Mode {i}: T_branch = {T:.6f}")
    print(f"  Mean T_branch: {imp['T_branch_B2_mean']:.6f}")
    print()

    print(f"Cross-branch leakage from B2+:")
    print(f"  To B1+: mean = {imp['leak_B1_mean']:.6f}  (per-mode: {imp['leak_B1']})")
    print(f"  To B3+: mean = {imp['leak_B3_mean']:.6f}  (per-mode: {imp['leak_B3']})")
    print(f"  To neg sector: mean = {imp['leak_neg_mean']:.6f}")
    print(f"  Row sums (unitarity): {imp['row_sums']}")
    print()

    print(f"B2+ overlap matrix |O|:")
    O_B2 = imp['O_B2_block']
    for i in range(4):
        row = ' '.join([f'{abs(O_B2[i,j]):.4f}' for j in range(4)])
        print(f"  [{row}]")
    print()

    print(f"Impedance determination:")
    print(f"  R_effective = 1 - T_branch_mean = {imp['R_effective']:.6f}")
    print(f"  Impedance from overlap = 1/(1-R) = {imp['impedance_from_overlap']:.4f}")
    print()

    # CT-4 claimed impedance = 1.56. Compare with overlap analysis.
    CT4_impedance = 1.56
    CT4_R = 1.0 - 1.0/CT4_impedance
    print(f"CT-4 impedance analysis:")
    print(f"  CT-4 impedance: {CT4_impedance}")
    print(f"  CT-4 implied R: {CT4_R:.4f}")
    print(f"  Overlap R:      {imp['R_effective']:.4f}")
    print(f"  Overlap-based impedance: {imp['impedance_from_overlap']:.4f}")
    print()

    # Determine physically defensible impedance range
    if imp['T_branch_B2_mean'] > 0.99:
        imp_verdict = "LOW"
        imp_physical = 1.0
        imp_note = "T_branch > 0.99: modes transmit freely. Impedance ~ 1.0."
    elif imp['T_branch_B2_mean'] > 0.90:
        imp_verdict = "MODERATE"
        imp_physical = imp['impedance_from_overlap']
        imp_note = f"T_branch in [0.90, 0.99]: moderate reflection. Impedance = {imp_physical:.2f}."
    else:
        imp_verdict = "HIGH"
        imp_physical = imp['impedance_from_overlap']
        imp_note = f"T_branch < 0.90: significant scattering. Impedance = {imp_physical:.2f}."

    print(f"IMPEDANCE VERDICT: {imp_verdict}")
    print(f"  {imp_note}")
    print(f"  Defensible range: [{min(1.0, imp_physical):.2f}, {max(imp_physical, CT4_impedance):.2f}]")
    print()

    # ================================================================
    # PART C: Combined M_max Grid
    # ================================================================
    print("=" * 70)
    print("PART C: Combined M_max Grid (v_min x impedance)")
    print("=" * 70)
    print()

    # Build pairing kernel at tau = 0.20 (near fold)
    tau_idx_fold = 3  # tau = 0.20
    V_full = build_full_V_8x8(kosmann, tau_idx_fold)
    E_branch = get_branch_eigenvalues(kosmann, tau_idx_fold)

    print(f"Pairing kernel at tau = {TAU_VALUES[tau_idx_fold]:.2f}:")
    print(f"  E_branch: B3={E_branch[0]:.6f}, B2={E_branch[3]:.6f}, B1={E_branch[7]:.6f}")
    idx_5 = np.concatenate([B2_IDX, B1_IDX])
    V_5x5 = V_full[np.ix_(idx_5, idx_5)]
    print(f"  V(B1+B2) 5x5 (max off-diag): {np.max(V_5x5 - np.diag(np.diag(V_5x5))):.6f}")
    print()

    # Build grid
    v_min_grid = np.logspace(-4, -1, 100)
    impedance_grid = np.array([1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.56])

    # Compute rho at each v_min via integration
    wall_width = TAU_WALL_HI - TAU_WALL_LO
    rho_grid_per_mode = np.zeros(len(v_min_grid))
    cs_E = vh['cs_E']
    for i, vmin in enumerate(v_min_grid):
        def integrand(tau):
            v = cs_E(tau, 1)
            return 1.0 / (np.pi * max(abs(v), vmin))
        result, _ = quad(integrand, TAU_WALL_LO, TAU_WALL_HI, limit=200, epsabs=1e-12)
        rho_grid_per_mode[i] = result / wall_width

    # Compute M_max grid
    M_grid = compute_M_max_grid(V_full, E_branch, v_min_grid, rho_grid_per_mode,
                                 impedance_grid)

    print(f"M_max grid shape: {M_grid.shape}")
    print()

    # Cross-check: v_min = 0.059 (step average), impedance = 1.56
    # Should reproduce the TRAP-33b value (approximately)
    idx_step = np.argmin(np.abs(v_min_grid - vh['v_step']))
    idx_imp156 = np.argmin(np.abs(impedance_grid - 1.56))
    M_crosscheck = M_grid[idx_step, idx_imp156]
    rho_crosscheck = rho_grid_per_mode[idx_step] * MULTI_SECTOR_FACTOR * 1.56

    print(f"Cross-check (v_min={v_min_grid[idx_step]:.4f}, imp=1.56):")
    print(f"  rho_per_mode = {rho_grid_per_mode[idx_step]:.4f}")
    print(f"  rho_eff (with ms + imp) = {rho_crosscheck:.4f}")
    print(f"  M_max = {M_crosscheck:.6f}")
    print(f"  TRAP-33b reference: M_max = 2.062 at Wall 2 (rho/mode = 8.81)")
    print()

    # Find M_max = 1 contour
    print(f"M_max = 1.0 boundary:")
    print(f"  {'Impedance':>10s}  {'v_min(M=1)':>12s}  {'rho/mode(M=1)':>14s}")
    print(f"  {'-'*40}")
    v_min_at_M1 = np.zeros(len(impedance_grid))
    for j in range(len(impedance_grid)):
        col = M_grid[:, j]
        # Find where M crosses 1.0 (scanning from high v_min = low rho)
        crossings = np.where(np.diff(np.sign(col - 1.0)))[0]
        if len(crossings) > 0:
            idx_cross = crossings[-1]  # last crossing from below
            # Linear interpolation
            f = (1.0 - col[idx_cross]) / (col[idx_cross+1] - col[idx_cross])
            v_c = v_min_grid[idx_cross] * (v_min_grid[idx_cross+1]/v_min_grid[idx_cross])**f
            rho_c = rho_grid_per_mode[idx_cross] + f * (rho_grid_per_mode[idx_cross+1] - rho_grid_per_mode[idx_cross])
            v_min_at_M1[j] = v_c
            print(f"  {impedance_grid[j]:10.2f}  {v_c:12.6f}  {rho_c:14.4f}")
        elif col[0] > 1.0:  # M > 1 everywhere
            v_min_at_M1[j] = v_min_grid[-1]
            print(f"  {impedance_grid[j]:10.2f}  {'> 0.1':>12s}  {'N/A':>14s}")
        else:  # M < 1 everywhere
            v_min_at_M1[j] = 0.0
            print(f"  {impedance_grid[j]:10.2f}  {'< 1e-4':>12s}  {'N/A':>14s}")
    print()

    # ================================================================
    # M_max at physically justified point
    # ================================================================
    print("=" * 70)
    print("PHYSICAL POINT EVALUATION")
    print("=" * 70)
    print()

    # Physical v_min
    v_phys = vh['v_min_physical']
    idx_v_phys = np.argmin(np.abs(v_min_grid - v_phys))

    # Physical impedance: from overlap analysis
    imp_phys = imp['impedance_from_overlap']
    # Find closest in grid or interpolate
    if imp_phys <= impedance_grid[0]:
        idx_imp_phys = 0
        imp_phys_grid = impedance_grid[0]
    elif imp_phys >= impedance_grid[-1]:
        idx_imp_phys = len(impedance_grid) - 1
        imp_phys_grid = impedance_grid[-1]
    else:
        idx_imp_phys = np.argmin(np.abs(impedance_grid - imp_phys))
        imp_phys_grid = impedance_grid[idx_imp_phys]

    # Compute M_max at exact physical point (not grid approximation)
    rho_phys_per_mode = vh['rho_at_physical']
    rho_phys_eff = rho_phys_per_mode * MULTI_SECTOR_FACTOR * imp_phys
    M_phys, _, _, _, _ = thouless_5x5(V_full, E_branch, 0.0, rho_phys_eff, 1.0)

    print(f"Physical v_min: {v_phys:.6f} ({vh['v_min_physical_name']})")
    print(f"Physical impedance: {imp_phys:.4f} (from overlap T_branch = {imp['T_branch_B2_mean']:.4f})")
    print(f"rho_per_mode (van Hove integral): {rho_phys_per_mode:.4f}")
    print(f"rho_eff (ms={MULTI_SECTOR_FACTOR}, imp={imp_phys:.4f}): {rho_phys_eff:.4f}")
    print(f"M_max at physical point: {M_phys:.6f}")
    print()

    # Also compute at impedance = 1.0 (Tesla's claim)
    rho_imp1 = rho_phys_per_mode * MULTI_SECTOR_FACTOR * 1.0
    M_imp1, _, _, _, _ = thouless_5x5(V_full, E_branch, 0.0, rho_imp1, 1.0)
    print(f"M_max at impedance = 1.0 (Tesla claim): {M_imp1:.6f}")

    # At CT-4 impedance = 1.56
    rho_ct4 = rho_phys_per_mode * MULTI_SECTOR_FACTOR * 1.56
    M_ct4, _, _, _, _ = thouless_5x5(V_full, E_branch, 0.0, rho_ct4, 1.0)
    print(f"M_max at impedance = 1.56 (CT-4):       {M_ct4:.6f}")
    print()

    # ================================================================
    # GATE CLASSIFICATION
    # ================================================================
    print("=" * 70)
    print("GATE VH-IMP-35a CLASSIFICATION")
    print("=" * 70)
    print()

    # Check if M >= 1 at the physical point
    if M_phys >= 1.0:
        gate_verdict = "PASS"
    else:
        gate_verdict = "FAIL"

    # Check if M >= 1 at ANY defensible combination
    M_min_imp = M_imp1  # most conservative impedance
    M_max_imp = M_ct4   # most generous impedance

    # Check across the full defensible band
    imp_defensible_lo = 1.0
    imp_defensible_hi = max(imp_phys, CT4_impedance)

    M_at_lo_imp, _, _, _, _ = thouless_5x5(V_full, E_branch, 0.0,
        rho_phys_per_mode * MULTI_SECTOR_FACTOR * imp_defensible_lo, 1.0)
    M_at_hi_imp, _, _, _, _ = thouless_5x5(V_full, E_branch, 0.0,
        rho_phys_per_mode * MULTI_SECTOR_FACTOR * imp_defensible_hi, 1.0)

    print(f"GATE VH-IMP-35a: {gate_verdict}")
    print(f"  M_max at physical point ({v_phys:.4f}, {imp_phys:.2f}): {M_phys:.6f}")
    print(f"  M_max at conservative (imp=1.0):  {M_at_lo_imp:.6f}")
    print(f"  M_max at generous (imp={imp_defensible_hi:.2f}):   {M_at_hi_imp:.6f}")
    print()

    if gate_verdict == "PASS":
        print(f"  M_max >= 1.0 at the physically justified (v_min, impedance) point.")
        print(f"  The BCS instability is CONFIRMED with proper van Hove + impedance treatment.")
    else:
        # Check if any grid point passes
        any_pass = np.any(M_grid >= 1.0)
        if any_pass:
            # Find minimum impedance needed
            for j in range(len(impedance_grid)):
                if np.any(M_grid[:, j] >= 1.0):
                    # Find maximum v_min where M >= 1
                    idx_pass = np.where(M_grid[:, j] >= 1.0)[0]
                    v_max_pass = v_min_grid[idx_pass[-1]]
                    print(f"  M_max >= 1.0 possible at impedance >= {impedance_grid[j]:.2f} "
                          f"(v_min < {v_max_pass:.4f})")
                    break
            print(f"  Whether this is achieved depends on the correct impedance value.")
        else:
            print(f"  M_max < 1.0 at ALL grid points. Gate FAILS comprehensively.")

    print()

    # ================================================================
    # Summary table
    # ================================================================
    print("=" * 70)
    print("SUMMARY TABLE")
    print("=" * 70)
    print()
    print(f"{'Scenario':>25s}  {'v_min':>8s}  {'imp':>6s}  {'rho/mode':>10s}  {'M_max':>8s}  {'Verdict':>8s}")
    print(f"{'='*75}")

    scenarios = [
        ("W-32b step avg", vh['v_step'], 1.56, None),
        ("Van Hove physical", v_phys, imp_phys, None),
        ("Van Hove + imp=1.0", v_phys, 1.0, None),
        ("Van Hove + CT-4", v_phys, 1.56, None),
        ("v_min=0.01 + imp=1.0", 0.01, 1.0, None),
        ("v_min=0.01 + CT-4", 0.01, 1.56, None),
    ]

    for name, vmin, imp_val, _ in scenarios:
        def integ(tau):
            v = cs_E(tau, 1)
            return 1.0 / (np.pi * max(abs(v), vmin))
        rho_v, _ = quad(integ, TAU_WALL_LO, TAU_WALL_HI, limit=200)
        rho_v /= wall_width
        rho_eff = rho_v * MULTI_SECTOR_FACTOR * imp_val
        M, _, _, _, _ = thouless_5x5(V_full, E_branch, 0.0, rho_eff, 1.0)
        v_str = "PASS" if M >= 1.0 else "FAIL"
        print(f"{name:>25s}  {vmin:8.5f}  {imp_val:6.2f}  {rho_eff:10.4f}  {M:8.4f}  {v_str:>8s}")

    print()

    # ================================================================
    # Save
    # ================================================================
    save_dict = {
        # Part A
        'tau_fold': vh['tau_fold'],
        'E_fold': vh['E_fold'],
        'd2E_fold': vh['d2E_fold'],
        'd3E_fold': vh['d3E_fold'],
        'v_min_scan': vh['v_min_scan'],
        'rho_smooth': vh['rho_smooth'],
        'v_min_physical': vh['v_min_physical'],
        'v_step': vh['v_step'],
        'rho_step': vh['rho_step'],
        'rho_at_physical': vh['rho_at_physical'],
        'v_min_sector': vh['v_min_sector'],
        'v_min_delta_E_wall': vh['v_min_delta_E_wall'],
        'delta_E_wall_val': vh['delta_E_wall'],
        'v_min_slope': vh['v_min_slope'],
        'B2_bw': vh['B2_bw'],

        # Part B
        'O_full': imp['O'],
        'T_diag_B2': imp['T_diag_B2'],
        'T_branch_B2': imp['T_branch_B2'],
        'leak_B1': imp['leak_B1'],
        'leak_B3': imp['leak_B3'],
        'leak_neg': imp['leak_neg'],
        'R_effective': imp['R_effective'],
        'impedance_from_overlap': imp['impedance_from_overlap'],
        'O_B2_block': imp['O_B2_block'],

        # Part C
        'v_min_grid': v_min_grid,
        'impedance_grid': impedance_grid,
        'rho_grid_per_mode': rho_grid_per_mode,
        'M_grid': M_grid,
        'v_min_at_M1': v_min_at_M1,

        # Physical point
        'v_phys': v_phys,
        'imp_phys': imp_phys,
        'rho_phys_per_mode': rho_phys_per_mode,
        'rho_phys_eff': rho_phys_eff,
        'M_phys': M_phys,
        'M_imp1': M_imp1,
        'M_ct4': M_ct4,

        # Gate
        'gate_verdict': np.array([gate_verdict]),
    }
    np.savez_compressed(OUTPUT_NPZ, **save_dict)
    print(f"Saved: {OUTPUT_NPZ}")
    print(f"Size: {os.path.getsize(OUTPUT_NPZ) / 1024:.1f} KB")
    print()

    # ================================================================
    # Plot (4 panels)
    # ================================================================
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))

    # Panel 1: v_B2 profile with fold location
    ax = axes[0, 0]
    tau_plot = np.linspace(0.0, 0.5, 500)
    v_plot = cs_E(tau_plot, 1)
    ax.plot(tau_plot, v_plot, 'b-', lw=2, label='v(tau) = dE/dtau (spline)')
    ax.plot(tau_arr, v_B2_arr, 'ko', ms=8, label='v_B2 (data points)')
    ax.axhline(0, color='gray', ls='--', lw=1)
    ax.axvline(vh['tau_fold'], color='r', ls=':', lw=2, label=f'tau_fold = {vh["tau_fold"]:.4f}')
    ax.axvspan(TAU_WALL_LO, TAU_WALL_HI, alpha=0.15, color='green', label='Wall 2 [0.15, 0.25]')

    # Mark v_min cutoffs
    for name, val, col in [('sector', vh['v_min_sector'], 'purple'),
                             ('slope', vh['v_min_slope'], 'orange')]:
        ax.axhline(val, color=col, ls='-.', lw=1, alpha=0.7, label=f'v_min_{name} = {val:.4f}')
        ax.axhline(-val, color=col, ls='-.', lw=1, alpha=0.7)

    ax.set_xlabel('tau', fontsize=12)
    ax.set_ylabel('v = dE_B2/dtau', fontsize=12)
    ax.set_title('B2 Group Velocity Profile', fontsize=13)
    ax.legend(fontsize=8, loc='upper left')
    ax.set_xlim(0.05, 0.45)
    ax.grid(True, alpha=0.3)

    # Panel 2: rho vs v_min
    ax = axes[0, 1]
    ax.semilogx(vh['v_min_scan'], vh['rho_smooth'], 'b-', lw=2, label='rho(v_min) smooth integral')
    ax.axhline(vh['rho_step'], color='gray', ls='--', lw=2, label=f'Step average = {vh["rho_step"]:.2f}')
    ax.axvline(vh['v_min_physical'], color='r', ls=':', lw=2,
               label=f'Physical v_min = {vh["v_min_physical"]:.4f}')
    ax.axvline(vh['v_step'], color='gray', ls=':', lw=1,
               label=f'v_step = {vh["v_step"]:.4f}')

    # Mark physical point
    ax.plot(vh['v_min_physical'], vh['rho_at_physical'], 'ro', ms=12, zorder=5)

    ax.set_xlabel('v_min (regulator)', fontsize=12)
    ax.set_ylabel('rho per mode', fontsize=12)
    ax.set_title('Van Hove DOS vs Regulator', fontsize=13)
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Panel 3: Impedance analysis — B2 overlap matrix
    ax = axes[1, 0]
    O_show = np.abs(imp['O'])
    im = ax.imshow(O_show, cmap='hot', interpolation='nearest', vmin=0, vmax=1)
    plt.colorbar(im, ax=ax, label='|O_{nm}|')
    ax.set_xlabel('Mode at tau=0.25')
    ax.set_ylabel('Mode at tau=0.15')
    ax.set_title(f'Eigenvector Overlap |O| (T_B2={imp["T_branch_B2_mean"]:.3f})', fontsize=13)

    # Draw B2 block boundaries
    for pos in [8.5, 12.5]:
        ax.axhline(pos, color='cyan', ls='--', lw=1, alpha=0.7)
        ax.axvline(pos, color='cyan', ls='--', lw=1, alpha=0.7)
    ax.text(10.5, 10.5, 'B2+', color='cyan', fontsize=10, ha='center', va='center',
            fontweight='bold')

    # Panel 4: M_max heatmap
    ax = axes[1, 1]
    # Transpose so impedance is y-axis, v_min is x-axis
    extent = [np.log10(v_min_grid[0]), np.log10(v_min_grid[-1]),
              impedance_grid[0], impedance_grid[-1]]
    im2 = ax.imshow(M_grid.T, aspect='auto', origin='lower',
                     extent=extent, cmap='RdYlGn', vmin=0, vmax=3.0,
                     interpolation='bilinear')
    plt.colorbar(im2, ax=ax, label='M_max')

    # M = 1 contour
    # Manual contour on the grid
    from matplotlib.colors import Normalize
    ax.contour(np.log10(v_min_grid), impedance_grid, M_grid.T,
               levels=[1.0], colors='black', linewidths=2, linestyles='--')

    # Mark physical point
    ax.plot(np.log10(v_phys), imp_phys, 'k*', ms=15, mew=2, label=f'Physical ({M_phys:.2f})')
    ax.plot(np.log10(vh['v_step']), 1.56, 'ws', ms=10, mew=2, label=f'W-32b ref ({M_crosscheck:.2f})')

    ax.set_xlabel('log10(v_min)', fontsize=12)
    ax.set_ylabel('Impedance factor', fontsize=12)
    ax.set_title(f'M_max Grid — Gate: {gate_verdict}', fontsize=13)
    ax.legend(fontsize=8, loc='upper right')

    fig.suptitle(f'VH-IMP-35a: {gate_verdict} | M_phys = {M_phys:.4f}',
                 fontsize=15, fontweight='bold')
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig(OUTPUT_PNG, dpi=150)
    plt.close()
    print(f"Plot saved: {OUTPUT_PNG}")

    elapsed = time.time() - t0
    print(f"\nRuntime: {elapsed:.1f}s")
    print()
    print("=" * 80)
    print(f"VH-IMP-35a FINAL: {gate_verdict} | M_phys = {M_phys:.6f}")
    print("=" * 80)

    return vh, imp, M_grid, M_phys, gate_verdict


if __name__ == "__main__":
    vh, imp, M_grid, M_phys, verdict = main()
