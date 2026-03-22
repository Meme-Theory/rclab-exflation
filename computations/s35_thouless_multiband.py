#!/usr/bin/env python3
"""
Session 35: NEFF-THOULESS-35 -- Multi-Band 3x3 and Full 8x8 Thouless Eigenvalue
=================================================================================

CONTEXT:
  Session 34 found M_max = 0.902 in the B2-only (5x5) Thouless matrix with
  step-function wall DOS. With smooth-wall van Hove DOS (rho = 14.02/mode),
  VH-IMP-35a gave M_max = 1.445 (single-band B2 with van Hove).

  The beyond-mean-field (BMF) corridor requires N_eff > 5.5 for the screening
  correction to leave M_max > 1. The question: do cross-channel couplings
  V(B1,B2) and V(B3,B2) push the effective pairing dimensionality above 5.5?

COMPUTATION:
  1. Build 3x3 branch-level Thouless matrix from corrected spinor V matrix.
  2. Build full 8x8 mode-level Thouless matrix (all positive eigenvalues).
  3. Compute eigenvalues and compare with 5x5 B2-only result.
  4. Assess whether N_eff effectively exceeds 5.5.

PHYSICS:
  The Thouless criterion for BCS instability in a multi-band system:

    M_{nm} = V_{nm} * rho_m / (2 |xi_m|)

  where xi_m = E_m - mu is the distance from chemical potential.

  For the branch-level 3x3 matrix:
    M_{ij} = V_eff(B_i, B_j) * rho_j * d_j / (2 |xi_j|)
  where d_j is the degeneracy of branch j, rho_j is per-mode DOS.

  B1: d=1, E=0.81914 (AT gap edge, xi~0 => regularized)
  B2: d=4, E=0.84527, xi=0.02613
  B3: d=3, E=0.97822, xi=0.15908

  Critical subtlety: V(B1,B1) = 0 exactly (Trap 1). So B1 cannot self-pair.
  But V(B1,B2) = 0.080 is nonzero. The divergent B1 susceptibility (xi->0)
  couples to B2 pairing via the off-diagonal channel.

GATE NEFF-THOULESS-35 (pre-registered):
  PASS:  max eigenvalue of full Thouless matrix > 1.0
  FAIL:  max eigenvalue <= 1.0

Author: landau-condensed-matter-theorist, Session 35
Date: 2026-03-07
"""

import os
import sys
import time
import numpy as np
from scipy.integrate import quad
from scipy.interpolate import CubicSpline
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
t0 = time.time()

# ======================================================================
#  Constants
# ======================================================================
TAU_VALUES = np.array([0.0, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.50])
TAU_IDX_DUMP = 3   # tau = 0.20 (dump point)
MU = 0.0            # Chemical potential (PH symmetric, mu=0 forced)

# Regulator for B1 (at gap edge, xi=0)
ETA_REG_FRAC = 0.001   # As fraction of lambda_min

# Wall parameters
TAU_WALL_LO = 0.15
TAU_WALL_HI = 0.25
WALL_WIDTH = TAU_WALL_HI - TAU_WALL_LO

# Multi-sector factor (conservative, from SECT-33a)
MULTI_SECTOR_FACTOR = 1.046

# Branch indices in the 16x16 sorted eigenbasis (positive sector)
# Sorted ascending: indices 0-7 negative, 8-15 positive
# Positive (ascending eigenvalue): B1=8, B2=9-12, B3=13-15
B1_FULL = np.array([8])
B2_FULL = np.array([9, 10, 11, 12])
B3_FULL = np.array([13, 14, 15])

# Branch degeneracies
D_B1 = 1
D_B2 = 4
D_B3 = 3


# ======================================================================
#  Data Loading
# ======================================================================

def load_data():
    """Load all prerequisite data."""
    kosmann = np.load(os.path.join(SCRIPT_DIR, 's23a_kosmann_singlet.npz'),
                      allow_pickle=True)
    vh_data = np.load(os.path.join(SCRIPT_DIR, 's35a_vh_impedance_arbiter.npz'),
                      allow_pickle=True)
    umklapp = np.load(os.path.join(SCRIPT_DIR, 's32a_umklapp_vertex.npz'),
                      allow_pickle=True)
    return kosmann, vh_data, umklapp


# ======================================================================
#  V matrix construction (spinor Kosmann basis)
# ======================================================================

def build_V_full_spinor(kosmann, tau_idx):
    """Build V_nm = sum_{a=0..7} |K^a_{nm}|^2 in eigenvector-sorted basis.

    The K_a_matrix stored in s23a_kosmann_singlet.npz is already in the
    eigenvector basis. We sum over all 8 Kosmann generators.

    Returns:
        V_sorted: (16, 16) V matrix in eigenvalue-sorted basis
        evals_sorted: (16,) sorted eigenvalues
        sort_idx: permutation from original to sorted
    """
    evals = kosmann[f'eigenvalues_{tau_idx}']
    sort_idx = np.argsort(evals)
    evals_sorted = evals[sort_idx]

    V = np.zeros((16, 16))
    for a in range(8):
        K = kosmann[f'K_a_matrix_{tau_idx}_{a}']
        V += np.abs(K) ** 2

    # Reorder to sorted eigenvalue basis
    V_sorted = V[np.ix_(sort_idx, sort_idx)]
    return V_sorted, evals_sorted, sort_idx


# ======================================================================
#  DOS computation
# ======================================================================

def compute_branch_dos(umklapp, vh_data, mode='smooth'):
    """Compute per-mode DOS for each branch.

    B2: Van Hove singularity at fold => smooth-wall integral.
    B1, B3: No fold in wall region => step-function DOS.

    The van Hove integral for B2 uses v_min = 0.01174 from VH-IMP-35a.

    For B1 and B3, compute step-function DOS from the group velocities
    measured at the wall boundaries.

    Returns:
        rho_B1: per-mode DOS for B1
        rho_B2: per-mode DOS for B2
        rho_B3: per-mode DOS for B3
    """
    # B2: use van Hove result from s35a
    if mode == 'smooth':
        rho_B2 = float(vh_data['rho_at_physical'])  # 14.02 per mode
    else:
        rho_B2 = float(vh_data['rho_step'])           # 5.40 per mode

    # B1 and B3: step-function DOS
    # Load eigenvalues at wall boundaries
    tau_arr = umklapp['tau_values']  # shape (9,)
    B2_evals = umklapp['B2_evals']  # shape (9, 4)

    # For B1 and B3, we need their group velocities in the wall region.
    # B1 is a singlet: E_B1(tau). B3 is a triplet: E_B3(tau).
    # Load from kosmann singlet data.
    kosmann_data = np.load(os.path.join(SCRIPT_DIR, 's23a_kosmann_singlet.npz'),
                           allow_pickle=True)

    # Get eigenvalues at multiple tau for cubic spline
    B1_evals_tau = np.zeros(len(tau_arr))
    B3_evals_tau = np.zeros(len(tau_arr))

    for i in range(len(tau_arr)):
        evals_i = kosmann_data[f'eigenvalues_{i}']
        pos_sorted = np.sort(evals_i[evals_i > 0])
        B1_evals_tau[i] = pos_sorted[0]    # lowest positive = B1
        B3_evals_tau[i] = pos_sorted[5]    # 6th positive = first B3

    # Cubic spline for each branch
    cs_B1 = CubicSpline(tau_arr, B1_evals_tau)
    cs_B3 = CubicSpline(tau_arr, B3_evals_tau)

    # Group velocities at wall boundaries
    v_B1_lo = abs(cs_B1(TAU_WALL_LO, 1))
    v_B1_hi = abs(cs_B1(TAU_WALL_HI, 1))
    v_B3_lo = abs(cs_B3(TAU_WALL_LO, 1))
    v_B3_hi = abs(cs_B3(TAU_WALL_HI, 1))

    # Step-function average velocity
    v_B1_avg = (v_B1_lo + v_B1_hi) / 2.0
    v_B3_avg = (v_B3_lo + v_B3_hi) / 2.0

    # Step DOS: rho = 1 / (pi * v_avg)
    rho_B1 = 1.0 / (np.pi * v_B1_avg) if v_B1_avg > 1e-10 else 1.0
    rho_B3 = 1.0 / (np.pi * v_B3_avg) if v_B3_avg > 1e-10 else 1.0

    # Also compute smooth-wall integral for B1 and B3 (for completeness)
    def smooth_integral(cs, tau_lo, tau_hi, v_min=0.001):
        """Integrate 1/(pi * max(|v|, v_min)) over [tau_lo, tau_hi]."""
        def integrand(tau):
            v = cs(tau, 1)
            return 1.0 / (np.pi * max(abs(v), v_min))
        result, _ = quad(integrand, tau_lo, tau_hi, limit=200, epsabs=1e-12)
        return result / (tau_hi - tau_lo)

    rho_B1_smooth = smooth_integral(cs_B1, TAU_WALL_LO, TAU_WALL_HI, v_min=0.001)
    rho_B3_smooth = smooth_integral(cs_B3, TAU_WALL_LO, TAU_WALL_HI, v_min=0.001)

    info = {
        'v_B1_lo': v_B1_lo, 'v_B1_hi': v_B1_hi, 'v_B1_avg': v_B1_avg,
        'v_B3_lo': v_B3_lo, 'v_B3_hi': v_B3_hi, 'v_B3_avg': v_B3_avg,
        'rho_B1_step': rho_B1, 'rho_B3_step': rho_B3,
        'rho_B1_smooth': rho_B1_smooth, 'rho_B3_smooth': rho_B3_smooth,
        'rho_B2_smooth': rho_B2,
        'cs_B1': cs_B1, 'cs_B3': cs_B3,
        'B1_evals_tau': B1_evals_tau, 'B3_evals_tau': B3_evals_tau,
    }

    return rho_B1, rho_B2, rho_B3, info


# ======================================================================
#  Thouless matrix construction
# ======================================================================

def thouless_3x3_branch(V_sorted, evals_sorted, rho_B1, rho_B2, rho_B3,
                         mu=0.0, eta_frac=0.001):
    """Construct and solve the 3x3 branch-level Thouless matrix.

    The 3x3 matrix represents B1, B2, B3 as effective single channels,
    with the pairing strength summed over degenerate modes:

    M_{ij} = sum_{n in B_i, m in B_j} V_{nm} * rho_j / (2 |xi_m|)
           = V_sum(B_i, B_j) * rho_j / (2 |xi_j|)

    where V_sum(B_i, B_j) = (1/d_i) * sum_{n in B_i, m in B_j} V_{nm}
    is the average coupling from one mode in B_i to ALL modes in B_j,
    and xi_j is the representative gap-edge distance for branch j.

    Returns:
        M_max, M_evals, M_3x3, V_branch, E_branch, xi_branch
    """
    # Branch eigenvalues (representative)
    E_B1 = evals_sorted[B1_FULL[0]]
    E_B2 = np.mean(evals_sorted[B2_FULL])  # degenerate, all same
    E_B3 = np.mean(evals_sorted[B3_FULL])  # degenerate, all same
    E_branch = np.array([E_B1, E_B2, E_B3])

    # Gap-edge distances
    lambda_min = np.min(np.abs(evals_sorted[evals_sorted > 0]))
    xi_branch = E_branch - mu
    eta = max(eta_frac * lambda_min, 1e-15)
    abs_xi = np.maximum(np.abs(xi_branch), eta)

    # Branch-averaged V matrix
    # V_branch[i,j] = mean over (n in B_i) of sum over (m in B_j) of V_{nm}
    # This gives the effective coupling from one mode in B_i to the ENTIRE B_j branch
    branch_idx = [B1_FULL, B2_FULL, B3_FULL]
    deg = [D_B1, D_B2, D_B3]

    V_branch = np.zeros((3, 3))
    for i in range(3):
        for j in range(3):
            # Sum over all pairs (n in B_i, m in B_j)
            V_block = V_sorted[np.ix_(branch_idx[i], branch_idx[j])]
            # Average over source modes, sum over target modes
            # M_{ij} represents: for each mode in B_i, the total coupling to B_j
            V_branch[i, j] = np.mean(np.sum(V_block, axis=1))

    # DOS vector (per mode, but we need total branch DOS = rho * d)
    rho_per_mode = np.array([rho_B1, rho_B2, rho_B3])

    # Thouless matrix: M_{ij} = V_branch[i,j] * rho_j / (2 * |xi_j|)
    # Note: rho_j here is per-mode DOS. The sum over target modes is already
    # absorbed in V_branch (which sums over m in B_j).
    M = np.zeros((3, 3))
    for j in range(3):
        M[:, j] = V_branch[:, j] * rho_per_mode[j] / (2.0 * abs_xi[j])

    M_evals = np.linalg.eigvals(M)
    M_max = np.max(np.real(M_evals))

    return M_max, M_evals, M, V_branch, E_branch, abs_xi


def thouless_8x8_full(V_sorted, evals_sorted, rho_B1, rho_B2, rho_B3,
                       mu=0.0, eta_frac=0.001):
    """Full 8x8 Thouless matrix for all positive modes individually.

    M_{nm} = V_{nm} * rho_m / (2 |xi_m|)

    Returns:
        M_max, M_evals, M_8x8, V_8x8, E_8, xi_8
    """
    # Positive sector indices
    all_pos = np.concatenate([B1_FULL, B2_FULL, B3_FULL])
    V_8x8 = V_sorted[np.ix_(all_pos, all_pos)]
    E_8 = evals_sorted[all_pos]

    lambda_min = np.min(np.abs(E_8))
    xi_8 = E_8 - mu
    eta = max(eta_frac * lambda_min, 1e-15)
    abs_xi = np.maximum(np.abs(xi_8), eta)

    # Per-mode DOS
    rho_8 = np.zeros(8)
    rho_8[0] = rho_B1       # B1 (mode 0)
    rho_8[1:5] = rho_B2     # B2 (modes 1-4)
    rho_8[5:8] = rho_B3     # B3 (modes 5-7)

    # Thouless matrix
    M = np.zeros((8, 8))
    for m in range(8):
        M[:, m] = V_8x8[:, m] * rho_8[m] / (2.0 * abs_xi[m])

    M_evals = np.linalg.eigvals(M)
    M_max = np.max(np.real(M_evals))

    return M_max, M_evals, M, V_8x8, E_8, abs_xi


def thouless_5x5_B2B1(V_sorted, evals_sorted, rho_B2, rho_B1=1.0,
                        mu=0.0, eta_frac=0.001):
    """5x5 Thouless matrix for B2+B1 subspace (baseline comparison).

    Matches the convention from s34a_dphys_thouless.py.
    """
    idx_5 = np.concatenate([B2_FULL, B1_FULL])  # B2 first, then B1
    V_5x5 = V_sorted[np.ix_(idx_5, idx_5)]
    E_5 = evals_sorted[idx_5]

    lambda_min = np.min(np.abs(E_5))
    xi_5 = E_5 - mu
    eta = max(eta_frac * lambda_min, 1e-15)
    abs_xi = np.maximum(np.abs(xi_5), eta)

    rho_5 = np.array([rho_B2] * 4 + [rho_B1])

    M = np.zeros((5, 5))
    for m in range(5):
        M[:, m] = V_5x5[:, m] * rho_5[m] / (2.0 * abs_xi[m])

    M_evals = np.linalg.eigvals(M)
    M_max = np.max(np.real(M_evals))

    return M_max, M_evals, M, V_5x5, E_5


# ======================================================================
#  Regulator sensitivity analysis
# ======================================================================

def regulator_scan(V_sorted, evals_sorted, rho_B1, rho_B2, rho_B3, mu=0.0):
    """Scan eta_frac to assess B1 regulator sensitivity."""
    eta_values = np.logspace(-6, -1, 50)
    M_3x3_vs_eta = np.zeros(len(eta_values))
    M_8x8_vs_eta = np.zeros(len(eta_values))
    M_5x5_vs_eta = np.zeros(len(eta_values))

    for i, eta in enumerate(eta_values):
        M_3x3_vs_eta[i], _, _, _, _, _ = thouless_3x3_branch(
            V_sorted, evals_sorted, rho_B1, rho_B2, rho_B3, mu, eta)
        M_8x8_vs_eta[i], _, _, _, _, _ = thouless_8x8_full(
            V_sorted, evals_sorted, rho_B1, rho_B2, rho_B3, mu, eta)
        M_5x5_vs_eta[i], _, _, _, _ = thouless_5x5_B2B1(
            V_sorted, evals_sorted, rho_B2, rho_B1, mu, eta)

    return eta_values, M_3x3_vs_eta, M_8x8_vs_eta, M_5x5_vs_eta


# ======================================================================
#  N_eff extraction
# ======================================================================

def compute_neff_from_multiband(M_max_5x5, M_max_8x8, M_max_3x3):
    """Estimate effective N_eff from the ratio of multi-band to single-band M_max.

    If M_max(8x8) = M_max(5x5) * f, then cross-channel couplings enhance
    pairing by factor f. The effective N_eff for beyond-mean-field is then:

    N_eff_effective = N_eff_B2_only * f^2

    where N_eff_B2_only = 4 (the B2 multiplicity in the 5x5 problem).
    The f^2 comes from the fact that M ~ V * rho, and the GMB correction
    scales as exp(-2/N_eff * ...).

    More precisely, the enhancement ratio determines whether including B1/B3
    pushes the system deeper into the BCS instability, relaxing the N_eff > 5.5
    requirement.
    """
    if M_max_5x5 > 0:
        enhancement_8x8 = M_max_8x8 / M_max_5x5
        enhancement_3x3 = M_max_3x3 / M_max_5x5
    else:
        enhancement_8x8 = 0.0
        enhancement_3x3 = 0.0

    # The beyond-mean-field corridor M_max > 1 requires:
    # M_MF * (1 - 1/N_eff) > 1  (schematic GMB)
    # So: N_eff > M_MF / (M_MF - 1)  when M_MF > 1
    # For M_MF = M_max_8x8:
    if M_max_8x8 > 1.0:
        N_eff_min_8x8 = M_max_8x8 / (M_max_8x8 - 1.0)
    else:
        N_eff_min_8x8 = float('inf')

    if M_max_3x3 > 1.0:
        N_eff_min_3x3 = M_max_3x3 / (M_max_3x3 - 1.0)
    else:
        N_eff_min_3x3 = float('inf')

    return {
        'enhancement_8x8': enhancement_8x8,
        'enhancement_3x3': enhancement_3x3,
        'N_eff_min_8x8': N_eff_min_8x8,
        'N_eff_min_3x3': N_eff_min_3x3,
    }


# ======================================================================
#  Main computation
# ======================================================================

def main():
    print("=" * 78)
    print("NEFF-THOULESS-35: Multi-Band 3x3 and 8x8 Thouless Eigenvalue")
    print("=" * 78)
    print()

    # --- Load data ---
    kosmann, vh_data, umklapp = load_data()
    print(f"Data loaded in {time.time()-t0:.1f}s")

    # --- Build V matrix ---
    V_sorted, evals_sorted, sort_idx = build_V_full_spinor(kosmann, TAU_IDX_DUMP)

    pos_evals = evals_sorted[evals_sorted > 0]
    print(f"\nEigenvalue structure at tau = {TAU_VALUES[TAU_IDX_DUMP]:.2f}:")
    print(f"  B1 (d=1): E = {evals_sorted[B1_FULL[0]]:.6f}")
    print(f"  B2 (d=4): E = {evals_sorted[B2_FULL[0]]:.6f}")
    print(f"  B3 (d=3): E = {evals_sorted[B3_FULL[0]]:.6f}")
    print(f"  Gap (lambda_min) = {np.min(pos_evals):.6f}")
    print(f"  Shell gap B2-B1 = {evals_sorted[B2_FULL[0]] - evals_sorted[B1_FULL[0]]:.6f}")
    print(f"  Shell gap B3-B2 = {evals_sorted[B3_FULL[0]] - evals_sorted[B2_FULL[-1]]:.6f}")

    # --- V matrix structure ---
    print(f"\n{'='*78}")
    print(f"V MATRIX STRUCTURE (spinor Kosmann basis, tau = 0.20)")
    print(f"{'='*78}")

    # Extract block statistics
    V_B1B1 = V_sorted[np.ix_(B1_FULL, B1_FULL)]
    V_B2B2 = V_sorted[np.ix_(B2_FULL, B2_FULL)]
    V_B3B3 = V_sorted[np.ix_(B3_FULL, B3_FULL)]
    V_B1B2 = V_sorted[np.ix_(B1_FULL, B2_FULL)]
    V_B1B3 = V_sorted[np.ix_(B1_FULL, B3_FULL)]
    V_B2B3 = V_sorted[np.ix_(B2_FULL, B3_FULL)]

    V_B2B2_offdiag = V_B2B2.copy()
    np.fill_diagonal(V_B2B2_offdiag, 0)
    V_B3B3_offdiag = V_B3B3.copy()
    np.fill_diagonal(V_B3B3_offdiag, 0)

    print(f"\n  Intra-branch:")
    print(f"    V(B1,B1) = {V_B1B1[0,0]:.6f}  (Trap 1: should be ~0)")
    print(f"    V(B2,B2) off-diag max = {np.max(V_B2B2_offdiag):.6f}")
    print(f"    V(B2,B2) diagonal mean = {np.mean(np.diag(V_B2B2)):.6f}")
    print(f"    V(B3,B3) off-diag max = {np.max(V_B3B3_offdiag):.6f}")
    print(f"    V(B3,B3) diagonal mean = {np.mean(np.diag(V_B3B3)):.6f}")

    print(f"\n  Inter-branch:")
    print(f"    V(B1,B2) max = {np.max(V_B1B2):.6f}")
    print(f"    V(B1,B2) mean = {np.mean(V_B1B2):.6f}")
    print(f"    V(B1,B3) max = {np.max(V_B1B3):.6f}")
    print(f"    V(B1,B3) mean = {np.mean(V_B1B3):.6f}")
    print(f"    V(B2,B3) max = {np.max(V_B2B3):.6f}")
    print(f"    V(B2,B3) mean = {np.mean(V_B2B3):.6f}")

    # Cross-check: V(B1,B1)=0 (Trap 1)
    print(f"\n  Trap 1 verification: V(B1,B1) = {V_B1B1[0,0]:.2e}")
    if V_B1B1[0,0] < 1e-10:
        print(f"    CONFIRMED: V(B1,B1) = 0 to machine precision")
    else:
        print(f"    WARNING: V(B1,B1) nonzero ({V_B1B1[0,0]:.2e})")

    # Cross-check against s34a stored values
    dphys = np.load(os.path.join(SCRIPT_DIR, 's34a_dphys_kosmann.npz'),
                    allow_pickle=True)
    V_B2B2_s34a = float(dphys['V_B2B2_max_vs_phi'][0])
    V_B1B2_s34a = float(dphys['V_B1B2_max_vs_phi'][0])
    V_B3B2_s34a = float(dphys['V_B3B2_max_vs_phi'][0])

    print(f"\n  Cross-check with s34a_dphys_kosmann (phi=0):")
    print(f"    V(B2,B2) offdiag max: this = {np.max(V_B2B2_offdiag):.6f}, "
          f"s34a = {V_B2B2_s34a:.6f}, "
          f"disc = {abs(np.max(V_B2B2_offdiag) - V_B2B2_s34a):.2e}")
    print(f"    V(B1,B2) max: this = {np.max(V_B1B2):.6f}, "
          f"s34a = {V_B1B2_s34a:.6f}, "
          f"disc = {abs(np.max(V_B1B2) - V_B1B2_s34a):.2e}")
    print(f"    V(B3,B2) max: this = {np.max(V_B2B3):.6f}, "
          f"s34a = {V_B3B2_s34a:.6f}, "
          f"disc = {abs(np.max(V_B2B3) - V_B3B2_s34a):.2e}")

    # --- Compute DOS ---
    print(f"\n{'='*78}")
    print(f"DOS COMPUTATION")
    print(f"{'='*78}")

    rho_B1, rho_B2, rho_B3, dos_info = compute_branch_dos(umklapp, vh_data, mode='smooth')
    rho_B1_step, _, rho_B3_step, dos_info_step = compute_branch_dos(umklapp, vh_data, mode='step')

    print(f"\n  B1 DOS:")
    print(f"    v_B1(0.15) = {dos_info['v_B1_lo']:.6f}")
    print(f"    v_B1(0.25) = {dos_info['v_B1_hi']:.6f}")
    print(f"    v_B1_avg   = {dos_info['v_B1_avg']:.6f}")
    print(f"    rho_B1 (step) = {dos_info['rho_B1_step']:.4f}")
    print(f"    rho_B1 (smooth) = {dos_info['rho_B1_smooth']:.4f}")

    print(f"\n  B2 DOS:")
    print(f"    rho_B2 (van Hove, smooth) = {rho_B2:.4f}")
    print(f"    rho_B2 (step) = {float(vh_data['rho_step']):.4f}")
    print(f"    Enhancement: {rho_B2/float(vh_data['rho_step']):.2f}x")

    print(f"\n  B3 DOS:")
    print(f"    v_B3(0.15) = {dos_info['v_B3_lo']:.6f}")
    print(f"    v_B3(0.25) = {dos_info['v_B3_hi']:.6f}")
    print(f"    v_B3_avg   = {dos_info['v_B3_avg']:.6f}")
    print(f"    rho_B3 (step) = {dos_info['rho_B3_step']:.4f}")
    print(f"    rho_B3 (smooth) = {dos_info['rho_B3_smooth']:.4f}")

    # --- Effective rho with multi-sector factor ---
    rho_B1_eff = rho_B1 * MULTI_SECTOR_FACTOR
    rho_B2_eff = rho_B2 * MULTI_SECTOR_FACTOR
    rho_B3_eff = rho_B3 * MULTI_SECTOR_FACTOR

    print(f"\n  Effective DOS (with multi-sector factor {MULTI_SECTOR_FACTOR}):")
    print(f"    rho_B1_eff = {rho_B1_eff:.4f}")
    print(f"    rho_B2_eff = {rho_B2_eff:.4f}")
    print(f"    rho_B3_eff = {rho_B3_eff:.4f}")

    # ================================================================
    # STEP 1: 5x5 BASELINE (B2+B1 only, reproduces VH-IMP-35a)
    # ================================================================
    print(f"\n{'='*78}")
    print(f"STEP 1: 5x5 BASELINE (B2+B1, smooth-wall DOS)")
    print(f"{'='*78}")

    M_5x5, evals_5x5, M_mat_5x5, V_sub_5x5, E_sub_5x5 = \
        thouless_5x5_B2B1(V_sorted, evals_sorted, rho_B2_eff, rho_B1_eff)

    print(f"\n  M_max (5x5) = {M_5x5:.6f}")
    print(f"  M eigenvalues: {np.sort(np.real(evals_5x5))[::-1]}")
    print(f"  V_5x5 matrix:")
    np.set_printoptions(precision=6, suppress=True, linewidth=120)
    print(f"  {V_sub_5x5}")

    # Cross-check with VH-IMP-35a result
    M_vh35a = float(vh_data['M_phys'])
    print(f"\n  Cross-check with VH-IMP-35a: M_phys = {M_vh35a:.6f}")
    disc_5x5 = abs(M_5x5 - M_vh35a)
    # NOTE: VH-IMP-35a used A_antisym basis, not spinor K_a basis.
    # Discrepancy expected and documented (s34a TRAP-33b retraction).
    print(f"  Discrepancy: {disc_5x5:.4f}")
    print(f"  NOTE: VH-IMP-35a used A_antisym (frame) basis, this uses")
    print(f"  K_a_matrix (spinor) basis. Discrepancy expected (documented in S34).")

    # ================================================================
    # STEP 2: 3x3 BRANCH THOULESS
    # ================================================================
    print(f"\n{'='*78}")
    print(f"STEP 2: 3x3 BRANCH THOULESS (B1, B2, B3)")
    print(f"{'='*78}")

    M_3x3, evals_3x3, M_mat_3x3, V_branch_3x3, E_branch_3x3, xi_3x3 = \
        thouless_3x3_branch(V_sorted, evals_sorted, rho_B1_eff, rho_B2_eff,
                             rho_B3_eff)

    print(f"\n  Branch eigenvalues: {E_branch_3x3}")
    print(f"  Branch |xi|: {xi_3x3}")
    print(f"  Branch V matrix (sum over target modes):")
    print(f"  {V_branch_3x3}")
    print(f"\n  3x3 Thouless matrix M:")
    print(f"  {M_mat_3x3}")
    print(f"\n  M_max (3x3) = {M_3x3:.6f}")
    print(f"  M eigenvalues: {np.sort(np.real(evals_3x3))[::-1]}")

    # ================================================================
    # STEP 3: 8x8 FULL THOULESS
    # ================================================================
    print(f"\n{'='*78}")
    print(f"STEP 3: 8x8 FULL THOULESS (all positive modes)")
    print(f"{'='*78}")

    M_8x8, evals_8x8, M_mat_8x8, V_8x8, E_8, xi_8 = \
        thouless_8x8_full(V_sorted, evals_sorted, rho_B1_eff, rho_B2_eff,
                           rho_B3_eff)

    print(f"\n  Mode eigenvalues: {E_8}")
    print(f"  Mode |xi|: {xi_8 - MU}")
    print(f"\n  8x8 V matrix:")
    print(f"  {V_8x8}")
    print(f"\n  M_max (8x8) = {M_8x8:.6f}")
    print(f"  Top 5 M eigenvalues: {np.sort(np.real(evals_8x8))[::-1][:5]}")

    # ================================================================
    # STEP 4: COMPARISON TABLE
    # ================================================================
    print(f"\n{'='*78}")
    print(f"STEP 4: COMPARISON TABLE")
    print(f"{'='*78}")

    print(f"\n  {'Matrix':>12s}  {'M_max':>10s}  {'Verdict':>10s}  {'Notes':<40s}")
    print(f"  {'='*12}  {'='*10}  {'='*10}  {'='*40}")

    for name, M_val, note in [
        ("5x5 (B2+B1)", M_5x5, "Standard B2+B1 subspace"),
        ("3x3 (branch)", M_3x3, "Branch-level with B3"),
        ("8x8 (full)", M_8x8, "All 8 positive modes"),
    ]:
        verd = "PASS" if M_val > 1.0 else "FAIL"
        print(f"  {name:>12s}  {M_val:>10.6f}  {verd:>10s}  {note:<40s}")

    # ================================================================
    # STEP 5: REGULATOR SENSITIVITY
    # ================================================================
    print(f"\n{'='*78}")
    print(f"STEP 5: REGULATOR SENSITIVITY (B1 at gap edge)")
    print(f"{'='*78}")

    eta_scan, M_3x3_scan, M_8x8_scan, M_5x5_scan = regulator_scan(
        V_sorted, evals_sorted, rho_B1_eff, rho_B2_eff, rho_B3_eff)

    print(f"\n  {'eta_frac':>12s}  {'M_5x5':>10s}  {'M_3x3':>10s}  {'M_8x8':>10s}")
    print(f"  {'='*12}  {'='*10}  {'='*10}  {'='*10}")
    for eta_val in [1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1]:
        idx = np.argmin(np.abs(eta_scan - eta_val))
        print(f"  {eta_scan[idx]:12.1e}  {M_5x5_scan[idx]:10.6f}  "
              f"{M_3x3_scan[idx]:10.6f}  {M_8x8_scan[idx]:10.6f}")

    # Plateau detection: find eta range where M_max is insensitive
    # (changes by < 1% per decade of eta)
    dM_dlneta = np.gradient(M_8x8_scan, np.log10(eta_scan))
    stable_mask = np.abs(dM_dlneta / M_8x8_scan) < 0.01
    if np.any(stable_mask):
        eta_stable_lo = eta_scan[stable_mask][0]
        eta_stable_hi = eta_scan[stable_mask][-1]
        M_plateau = np.mean(M_8x8_scan[stable_mask])
        print(f"\n  Stable plateau: eta in [{eta_stable_lo:.1e}, {eta_stable_hi:.1e}]")
        print(f"  M_max on plateau: {M_plateau:.6f}")
    else:
        print(f"\n  No stable plateau found -- M_max is regulator-sensitive")
        print(f"  (B1 at gap edge with V(B1,B1)=0 makes B1 contribution vanish)")
        M_plateau = M_8x8

    # ================================================================
    # STEP 6: N_eff ASSESSMENT
    # ================================================================
    print(f"\n{'='*78}")
    print(f"STEP 6: N_eff ASSESSMENT")
    print(f"{'='*78}")

    neff = compute_neff_from_multiband(M_5x5, M_8x8, M_3x3)

    print(f"\n  Enhancement from cross-channel couplings:")
    print(f"    M(8x8)/M(5x5) = {neff['enhancement_8x8']:.4f}")
    print(f"    M(3x3)/M(5x5) = {neff['enhancement_3x3']:.4f}")

    print(f"\n  Minimum N_eff required for BMF corridor (M_eff > 1):")
    print(f"    From 8x8: N_eff_min = {neff['N_eff_min_8x8']:.2f}")
    print(f"    From 3x3: N_eff_min = {neff['N_eff_min_3x3']:.2f}")

    print(f"\n  The actual N_eff depends on which modes participate in")
    print(f"  the dominant eigenvector of the Thouless matrix.")

    # Eigenvector analysis: which modes dominate?
    _, _, _, _, _, _ = thouless_8x8_full(V_sorted, evals_sorted,
                                          rho_B1_eff, rho_B2_eff, rho_B3_eff)
    M_8x8_mat_full = np.zeros((8, 8))
    all_pos_idx = np.concatenate([B1_FULL, B2_FULL, B3_FULL])
    E_pos = evals_sorted[all_pos_idx]
    xi_pos = E_pos - MU
    lambda_min_pos = np.min(np.abs(E_pos))
    eta_default = max(ETA_REG_FRAC * lambda_min_pos, 1e-15)
    abs_xi_pos = np.maximum(np.abs(xi_pos), eta_default)
    V_pos = V_sorted[np.ix_(all_pos_idx, all_pos_idx)]
    rho_pos = np.array([rho_B1_eff] + [rho_B2_eff]*4 + [rho_B3_eff]*3)
    for m in range(8):
        M_8x8_mat_full[:, m] = V_pos[:, m] * rho_pos[m] / (2.0 * abs_xi_pos[m])

    M_evals_full = np.linalg.eigvals(M_8x8_mat_full)
    idx_max = np.argmax(np.real(M_evals_full))
    # Get eigenvector
    M_evals_right, M_evecs_right = np.linalg.eig(M_8x8_mat_full)
    idx_dom = np.argmax(np.real(M_evals_right))
    v_dom = np.abs(M_evecs_right[:, idx_dom])
    v_dom /= np.sum(v_dom)  # normalize to probability

    print(f"\n  Dominant eigenvector weight distribution:")
    branch_labels = ['B1'] + ['B2']*4 + ['B3']*3
    for i in range(8):
        print(f"    Mode {i} ({branch_labels[i]}): weight = {v_dom[i]:.4f}")

    B1_weight = v_dom[0]
    B2_weight = np.sum(v_dom[1:5])
    B3_weight = np.sum(v_dom[5:8])
    print(f"\n  Branch weights:")
    print(f"    B1: {B1_weight:.4f}  (d=1)")
    print(f"    B2: {B2_weight:.4f}  (d=4)")
    print(f"    B3: {B3_weight:.4f}  (d=3)")

    # Participation ratio as proxy for N_eff
    PR = 1.0 / np.sum(v_dom**2)
    print(f"\n  Participation ratio (1/sum(w^2)): {PR:.2f}")
    print(f"  This is a proxy for the effective number of pairing channels.")

    # ================================================================
    # STEP 7: STEP DOS COMPARISON
    # ================================================================
    print(f"\n{'='*78}")
    print(f"STEP 7: STEP-FUNCTION DOS COMPARISON")
    print(f"{'='*78}")

    rho_step_B2 = float(vh_data['rho_step'])
    M_5x5_step, _, _, _, _ = thouless_5x5_B2B1(
        V_sorted, evals_sorted, rho_step_B2 * MULTI_SECTOR_FACTOR,
        rho_B1 * MULTI_SECTOR_FACTOR)
    M_8x8_step, _, _, _, _, _ = thouless_8x8_full(
        V_sorted, evals_sorted,
        rho_B1 * MULTI_SECTOR_FACTOR,
        rho_step_B2 * MULTI_SECTOR_FACTOR,
        rho_B3 * MULTI_SECTOR_FACTOR)
    M_3x3_step, _, _, _, _, _ = thouless_3x3_branch(
        V_sorted, evals_sorted,
        rho_B1 * MULTI_SECTOR_FACTOR,
        rho_step_B2 * MULTI_SECTOR_FACTOR,
        rho_B3 * MULTI_SECTOR_FACTOR)

    print(f"\n  {'Matrix':>12s}  {'Step DOS':>10s}  {'Smooth DOS':>10s}  {'Ratio':>8s}")
    print(f"  {'='*12}  {'='*10}  {'='*10}  {'='*8}")
    for name, Ms, Msm in [
        ("5x5", M_5x5_step, M_5x5),
        ("3x3", M_3x3_step, M_3x3),
        ("8x8", M_8x8_step, M_8x8),
    ]:
        ratio = Msm / Ms if Ms > 0 else 0
        print(f"  {name:>12s}  {Ms:10.6f}  {Msm:10.6f}  {ratio:8.2f}")

    # ================================================================
    # GATE CLASSIFICATION
    # ================================================================
    print(f"\n{'='*78}")
    print(f"NEFF-THOULESS-35: GATE CLASSIFICATION")
    print(f"{'='*78}")

    # Use the 8x8 full Thouless (most complete, includes all channels)
    M_gate = M_8x8
    gate_verdict = "PASS" if M_gate > 1.0 else "FAIL"

    print(f"\n  Pre-registered criterion: max eigenvalue of full Thouless > 1.0")
    print(f"  Result: M_max(8x8) = {M_gate:.6f}")
    print(f"  M_max(3x3) = {M_3x3:.6f}")
    print(f"  M_max(5x5) = {M_5x5:.6f}")
    print(f"\n  NEFF-THOULESS-35: *** {gate_verdict} ***")

    if gate_verdict == "PASS":
        print(f"\n  The multi-band Thouless eigenvalue exceeds 1.0.")
        print(f"  Cross-channel couplings V(B1,B2) and V(B2,B3) enhance pairing.")
        print(f"  Enhancement over B2-only: {neff['enhancement_8x8']:.2f}x")
        print(f"  Minimum N_eff for BMF: {neff['N_eff_min_8x8']:.2f}")
    else:
        print(f"\n  The multi-band Thouless eigenvalue does NOT exceed 1.0.")
        print(f"  Cross-channel couplings insufficient to open the BMF corridor.")
        print(f"  The B2-only result (M={M_5x5:.4f}) is the controlling bound.")
        if M_5x5 > 1.0:
            print(f"  However, the 5x5 M_max > 1 means B2-only BCS is present.")
            print(f"  Multi-band N_eff is NOT the bottleneck.")

    # ================================================================
    # SAVE
    # ================================================================
    save_dict = {
        # Eigenvalues
        'evals_sorted': evals_sorted,
        'E_branch': E_branch_3x3,
        'E_8': E_pos,
        'lambda_min': np.min(pos_evals),

        # V matrix
        'V_sorted_pos': V_pos,
        'V_branch_3x3': V_branch_3x3,
        'V_B1B1': V_B1B1[0, 0],
        'V_B2B2_offdiag_max': np.max(V_B2B2_offdiag),
        'V_B3B3_offdiag_max': np.max(V_B3B3_offdiag),
        'V_B1B2_max': np.max(V_B1B2),
        'V_B1B3_max': np.max(V_B1B3),
        'V_B2B3_max': np.max(V_B2B3),

        # DOS
        'rho_B1': rho_B1_eff,
        'rho_B2': rho_B2_eff,
        'rho_B3': rho_B3_eff,
        'rho_B1_step': dos_info['rho_B1_step'],
        'rho_B2_step': float(vh_data['rho_step']),
        'rho_B3_step': dos_info['rho_B3_step'],
        'rho_B1_smooth': dos_info['rho_B1_smooth'],
        'rho_B3_smooth': dos_info['rho_B3_smooth'],
        'v_B1_avg': dos_info['v_B1_avg'],
        'v_B3_avg': dos_info['v_B3_avg'],

        # Thouless results
        'M_5x5': M_5x5,
        'M_3x3': M_3x3,
        'M_8x8': M_8x8,
        'M_evals_5x5': np.real(evals_5x5),
        'M_evals_3x3': np.real(evals_3x3),
        'M_evals_8x8': np.real(evals_8x8),
        'M_mat_3x3': M_mat_3x3,

        # Step DOS comparison
        'M_5x5_step': M_5x5_step,
        'M_3x3_step': M_3x3_step,
        'M_8x8_step': M_8x8_step,

        # Regulator scan
        'eta_scan': eta_scan,
        'M_3x3_vs_eta': M_3x3_scan,
        'M_8x8_vs_eta': M_8x8_scan,
        'M_5x5_vs_eta': M_5x5_scan,

        # N_eff
        'enhancement_8x8': neff['enhancement_8x8'],
        'enhancement_3x3': neff['enhancement_3x3'],
        'N_eff_min_8x8': neff['N_eff_min_8x8'],
        'N_eff_min_3x3': neff['N_eff_min_3x3'],
        'participation_ratio': PR,
        'dominant_eigvec_weights': v_dom,
        'B1_weight': B1_weight,
        'B2_weight': B2_weight,
        'B3_weight': B3_weight,

        # Gate
        'gate_verdict': gate_verdict,
        'M_gate': M_gate,
    }

    out_npz = os.path.join(SCRIPT_DIR, 's35_thouless_multiband.npz')
    np.savez_compressed(out_npz, **save_dict)
    print(f"\nSaved: {out_npz}")
    print(f"Size: {os.path.getsize(out_npz) / 1024:.1f} KB")

    # ================================================================
    # PLOT
    # ================================================================
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Panel 1: Regulator sensitivity
    ax = axes[0, 0]
    ax.semilogx(eta_scan, M_5x5_scan, 'b-', lw=2, label='5x5 (B2+B1)')
    ax.semilogx(eta_scan, M_3x3_scan, 'g--', lw=2, label='3x3 (branch)')
    ax.semilogx(eta_scan, M_8x8_scan, 'r-', lw=2, label='8x8 (full)')
    ax.axhline(1.0, color='black', ls='--', lw=1.5, label='M=1 threshold')
    ax.axvline(ETA_REG_FRAC, color='gray', ls=':', lw=1, label=f'eta={ETA_REG_FRAC}')
    ax.set_xlabel('eta_frac (regulator)', fontsize=11)
    ax.set_ylabel('M_max', fontsize=11)
    ax.set_title('Regulator Sensitivity', fontsize=12)
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Panel 2: 8x8 V matrix heatmap
    ax = axes[0, 1]
    im = ax.imshow(V_pos, cmap='hot', interpolation='nearest')
    plt.colorbar(im, ax=ax, label='V_nm')
    ax.set_xlabel('Mode m')
    ax.set_ylabel('Mode n')
    ax.set_title('8x8 V Matrix (positive sector)', fontsize=12)
    # Draw branch boundaries
    for pos in [0.5, 4.5]:
        ax.axhline(pos, color='cyan', ls='--', lw=1)
        ax.axvline(pos, color='cyan', ls='--', lw=1)
    ax.text(0, 0, 'B1', color='cyan', fontsize=9, ha='center', va='center',
            fontweight='bold')
    ax.text(2.5, 2.5, 'B2', color='cyan', fontsize=9, ha='center', va='center',
            fontweight='bold')
    ax.text(6, 6, 'B3', color='cyan', fontsize=9, ha='center', va='center',
            fontweight='bold')

    # Panel 3: Bar chart of M_max values
    ax = axes[1, 0]
    categories = ['5x5\n(B2+B1)', '3x3\n(branch)', '8x8\n(full)']
    smooth_vals = [M_5x5, M_3x3, M_8x8]
    step_vals = [M_5x5_step, M_3x3_step, M_8x8_step]

    x = np.arange(3)
    width = 0.35
    bars1 = ax.bar(x - width/2, step_vals, width, label='Step DOS',
                    color='lightblue', edgecolor='black')
    bars2 = ax.bar(x + width/2, smooth_vals, width, label='Smooth DOS (van Hove)',
                    color='salmon', edgecolor='black')
    ax.axhline(1.0, color='black', ls='--', lw=2, label='M=1 threshold')
    ax.set_xticks(x)
    ax.set_xticklabels(categories)
    ax.set_ylabel('M_max', fontsize=11)
    ax.set_title(f'Multi-Band Thouless: {gate_verdict}', fontsize=12)
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3, axis='y')

    for bar, val in zip(bars1, step_vals):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.02,
                f'{val:.3f}', ha='center', va='bottom', fontsize=8)
    for bar, val in zip(bars2, smooth_vals):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.02,
                f'{val:.3f}', ha='center', va='bottom', fontsize=8,
                fontweight='bold')

    # Panel 4: Dominant eigenvector weights
    ax = axes[1, 1]
    labels_8 = ['B1'] + [f'B2.{i}' for i in range(4)] + [f'B3.{i}' for i in range(3)]
    colors_8 = ['green'] + ['blue']*4 + ['red']*3
    ax.bar(range(8), v_dom, color=colors_8, edgecolor='black', alpha=0.7)
    ax.set_xticks(range(8))
    ax.set_xticklabels(labels_8, fontsize=9)
    ax.set_ylabel('Weight in dominant eigenvector', fontsize=11)
    ax.set_title(f'Participation Ratio = {PR:.2f}', fontsize=12)
    ax.grid(True, alpha=0.3, axis='y')
    ax.text(0.95, 0.95,
            f'B1: {B1_weight:.3f}\nB2: {B2_weight:.3f}\nB3: {B3_weight:.3f}',
            transform=ax.transAxes, ha='right', va='top', fontsize=10,
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    fig.suptitle(
        f'NEFF-THOULESS-35: {gate_verdict} | M(8x8)={M_8x8:.4f}, '
        f'M(3x3)={M_3x3:.4f}, M(5x5)={M_5x5:.4f}',
        fontsize=13, fontweight='bold')
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plot_path = os.path.join(SCRIPT_DIR, 's35_thouless_multiband.png')
    plt.savefig(plot_path, dpi=150)
    plt.close()
    print(f"Plot saved: {plot_path}")

    elapsed = time.time() - t0
    print(f"\n{'='*78}")
    print(f"NEFF-THOULESS-35 FINAL: {gate_verdict}")
    print(f"  M(8x8) = {M_8x8:.6f}")
    print(f"  M(3x3) = {M_3x3:.6f}")
    print(f"  M(5x5) = {M_5x5:.6f}")
    print(f"  Participation ratio = {PR:.2f}")
    print(f"  Runtime: {elapsed:.1f}s")
    print(f"{'='*78}")

    return gate_verdict, M_8x8, M_3x3, M_5x5, neff


if __name__ == '__main__':
    verdict, M8, M3, M5, neff = main()
