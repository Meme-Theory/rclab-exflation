#!/usr/bin/env python3
"""
S61 — PROJ-A2-61: Particle-Number Projection for the Heat Kernel
=================================================================

Gate: PROJ-A2-61
  PASS if |a_2^{PBCS} - a_2^{BCS}| / a_2^{BCS} < 5%.
  FAIL if > 20%.
  INFO if 5-20%.

Physics:
  The Seeley-DeWitt a_2(D_K^2) = (4pi)^{-4} * (20R/3) * Vol is PURELY GEOMETRIC:
  it depends only on the metric g_Jensen(tau) through R(tau) and Vol.
  This part is INDEPENDENT of the BCS state.

  However, the framework spectral action is computed on a Bogoliubov-de Gennes
  (BdG) doubled Hilbert space where the gap function Delta enters the operator:

      D_BdG = ( D_K,    Delta   )       D_BdG^2 includes Delta^dag Delta terms
              ( Delta^dag, -D_K )

  The heat kernel coefficient a_2(D_BdG^2) then acquires a correction from Delta:

      a_2(D_BdG^2) = a_2(D_K^2) + a_2^{pair}(Delta)

  where the pairing correction a_2^{pair} comes from the BCS gap function.
  For the UNPROJECTED BCS state, Delta is determined by the BCS gap equation.
  For the PROJECTED (PBCS) state, the effective gap is modified.

  Nuclear analogy (Papers 02, 03, 15, 17):
    In nuclei with A < 50, PBCS vs BCS pairing energies differ by 5-15%.
    The framework has N_dof = 8 modes — deep in the "light nucleus" regime
    where number projection matters most (Paper 17: ultrasmall systems).

  The computation:
    1. Geometric a_2: (4pi)^{-4} * (20R/3) * Vol  (state-independent)
    2. BCS pairing correction: proportional to sum_k Delta_k^2 / (2*E_k)^2
       where E_k = sqrt((eps_k - mu)^2 + Delta_k^2)
    3. PBCS pairing correction: use exact number-projection via Fomenko integral
       P_N = (1/2pi) int_0^{2pi} exp(i*phi*(N_hat-N)) dphi
       Discretized on N_phi quadrature points.
    4. Compare: |a_2^{PBCS} - a_2^{BCS}| / a_2^{BCS}

  The correction is:
    a_2^{pair}/a_2^{geom} ~ |Delta|^2 / (E_BCS * R * M_KK^2)

  For the framework: |Delta|^2 ~ 0.6 (M_KK^2), R ~ 2.0, so the correction is O(1)
  in M_KK units BUT enters with a small coefficient from the BdG trace structure.

Author: Nazarewicz Nuclear Structure Theorist (Session 61)
Date: 2026-03-28
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import numpy as np
from scipy.linalg import eigh
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import (
    tau_fold, Vol_SU3_Haar, M_KK, M_KK_gravity, M_KK_kerner,
    PI, E_cond, N_dof_BCS, Delta_0_GL, Delta_0_OES,
    a0_fold, a2_fold, a4_fold,
    E_B1, E_B2_mean, E_B3_mean,
)

np.set_printoptions(precision=8, linewidth=120)

# ==============================================================================
#  SECTION 1: Load S52 HFB Data
# ==============================================================================

print("=" * 72)
print("PROJ-A2-61: Particle-Number Projection for the Heat Kernel")
print("=" * 72)

data = np.load('s52_hfb_full.npz', allow_pickle=True)
E_sp = data['E_sp_bare']         # Single-particle energies (8 modes)
V_bare = data['V_bare']           # Bare interaction matrix (8x8)
labels = data['labels']           # Mode labels

print(f"\nLoaded S52 HFB data:")
print(f"  N_modes = {len(E_sp)}")
print(f"  Labels: {labels}")
print(f"  E_sp = {E_sp}")

# Collect BCS/PBCS data for each N
N_values = [1, 2, 3, 4]
results = {}
for N in N_values:
    results[N] = {
        'E_ed': float(data[f'N{N}_E_ed']),
        'E_hfb': float(data[f'N{N}_E_hfb']),
        'E_pbcs': float(data[f'N{N}_E_pbcs']),
        'n_k_ed': data[f'N{N}_n_k_ed'],
        'n_k_hfb': data[f'N{N}_n_k_hfb'],
        'n_k_pbcs': data[f'N{N}_n_k_pbcs'],
        'Sigma_HF': data[f'N{N}_Sigma_HF'],
    }
    if f'N{N}_hfb_E_sp_final' in data:
        results[N]['E_sp_hfb'] = data[f'N{N}_hfb_E_sp_final']

print(f"\nEnergies (M_KK units):")
print(f"  {'N':>3s} {'E_ED':>12s} {'E_HFB':>12s} {'E_PBCS':>12s} {'(PBCS-ED)/ED':>14s}")
for N in N_values:
    r = results[N]
    frac = (r['E_pbcs'] - r['E_ed']) / r['E_ed'] * 100
    print(f"  {N:3d} {r['E_ed']:12.6f} {r['E_hfb']:12.6f} {r['E_pbcs']:12.6f} {frac:13.3f}%")


# ==============================================================================
#  SECTION 2: Geometric a_2 (State-Independent)
# ==============================================================================

def R_scalar(tau):
    """Exact scalar curvature R(tau) on Jensen-deformed SU(3)."""
    return -0.25 * np.exp(-4*tau) + 2.0 * np.exp(-tau) - 0.25 + 0.5 * np.exp(2*tau)

def a2_gilkey(tau):
    """Seeley-DeWitt a_2(D_K^2) — purely geometric."""
    R = R_scalar(tau)
    Vol = Vol_SU3_Haar
    return (4*PI)**(-4) * (20.0 * R / 3.0) * Vol

R_fold = R_scalar(tau_fold)
a2_geom = a2_gilkey(tau_fold)
a0_geom = (4*PI)**(-4) * 16.0 * Vol_SU3_Haar

print(f"\n{'='*72}")
print(f"SECTION 2: Geometric a_2 (state-independent)")
print(f"{'='*72}")
print(f"  tau_fold = {tau_fold}")
print(f"  R(tau_fold) = {R_fold:.10f}")
print(f"  a_2^{{geom}} = {a2_geom:.10f}")
print(f"  a_0^{{geom}} = {a0_geom:.10f}")
print(f"  W1 reference: a_2 = 0.728235")
print(f"  Agreement: {abs(a2_geom - 0.728235)/0.728235*100:.6f}%")


# ==============================================================================
#  SECTION 3: BCS Gap Equation and Pairing Correction
# ==============================================================================
#
# In the BdG formalism, the full operator is:
#   D_BdG = (D_K      Delta)
#           (Delta^dag -D_K )
#
# D_BdG^2 = (D_K^2 + |Delta|^2,    ...)
#            (...,                D_K^2 + |Delta|^2)
#
# The heat kernel of D_BdG^2 gives:
#   a_2(D_BdG^2) = 2*a_2(D_K^2) + a_2^{pair}
#
# where the factor 2 comes from the Nambu doubling, and
#   a_2^{pair} = (4pi)^{-d/2} * integral tr_S(F_pair) dvol
#
# For a CONSTANT gap (homogeneous BCS on the homogeneous space SU(3)):
#   F_pair = |Delta|^2 * I_spinor (endomorphism correction)
#   a_2^{pair} = (4pi)^{-d/2} * 16 * |Delta_eff|^2 * Vol
#
# The normalized (non-doubled) a_2 is then:
#   a_2^{BCS} = a_2^{geom} + (a_2^{pair} / 2)
#             = a_2^{geom} * (1 + 3*|Delta_eff|^2 / (5*R/12))
#
# where Delta_eff is the gap measured in M_KK units with appropriate normalization.
#
# CRITICAL: The relevant Delta is the BCS gap from the ED/HFB solution,
# converted to the spectral action convention. From the S52 data:
#   Delta_k ~ V_{kk'} * u_k' * v_k' (gap equation)

print(f"\n{'='*72}")
print(f"SECTION 3: BCS Pairing Correction to a_2")
print(f"{'='*72}")

# Solve BCS gap equation from S52 data
# For each N, extract effective gap from occupation numbers
# BCS: v_k^2 = n_k, u_k^2 = 1-n_k, u_k*v_k = sqrt(n_k*(1-n_k))

def bcs_gap_from_occupations(n_k, E_sp, V_bare):
    """
    Extract BCS gap Delta_k from occupation numbers.

    The BCS gap equation:  Delta_k = -sum_k' V_{kk'} * Delta_k' / (2*E_k')
    where E_k = sqrt((eps_k - mu)^2 + Delta_k^2)

    Equivalently: Delta_k = -sum_k' V_{kk'} * u_k' * v_k'
    where u_k*v_k = Delta_k / (2*E_k) = sqrt(n_k*(1-n_k))

    From n_k alone: u_k*v_k = sqrt(n_k*(1-n_k))
    Delta_k = -sum_k' V_{kk'} * sqrt(n_k'*(1-n_k'))
    """
    uv = np.sqrt(n_k * (1.0 - n_k))
    Delta_k = -V_bare @ uv
    return Delta_k, uv

def bcs_quasiparticle_energy(E_sp, mu, Delta_k):
    """E_k = sqrt((eps_k - mu)^2 + Delta_k^2)"""
    return np.sqrt((E_sp - mu)**2 + Delta_k**2)

def chemical_potential(n_k, E_sp):
    """Estimate mu from occupation numbers (midpoint of partially occupied levels)."""
    # Weighted average of sp energies by occupation derivative
    # For BCS: mu is where n_k = 0.5
    # Approximate: mu ~ sum(n_k * E_sp) / sum(n_k) (center of mass)
    N_total = np.sum(n_k)
    return np.sum(n_k * E_sp) / N_total


# Compute for all N sectors
print(f"\n  BCS pairing analysis per sector:")
print(f"  {'N':>3s} {'<Delta^2>':>12s} {'Delta_rms':>10s} {'mu':>10s} {'<DN^2>':>10s} {'uv_max':>10s}")

Delta_eff_sq = {}
for N in N_values:
    n_k_ed = results[N]['n_k_ed']
    n_k_hfb = results[N]['n_k_hfb']
    n_k_pbcs = results[N]['n_k_pbcs']

    # Use ED occupations (exact, number-projected by construction)
    Delta_ed, uv_ed = bcs_gap_from_occupations(n_k_ed, E_sp, V_bare)
    Delta_hfb, uv_hfb = bcs_gap_from_occupations(n_k_hfb, E_sp, V_bare)
    Delta_pbcs, uv_pbcs = bcs_gap_from_occupations(n_k_pbcs, E_sp, V_bare)

    # Number fluctuation <DN^2> = 4 * sum u_k^2 v_k^2
    dN2_ed = 4.0 * np.sum(n_k_ed * (1.0 - n_k_ed))
    dN2_hfb = 4.0 * np.sum(n_k_hfb * (1.0 - n_k_hfb))
    dN2_pbcs = 4.0 * np.sum(n_k_pbcs * (1.0 - n_k_pbcs))

    # Mean squared gap
    Delta_sq_ed = np.mean(Delta_ed**2)
    Delta_sq_hfb = np.mean(Delta_hfb**2)
    Delta_sq_pbcs = np.mean(Delta_pbcs**2)

    Delta_eff_sq[N] = {
        'ed': Delta_sq_ed, 'hfb': Delta_sq_hfb, 'pbcs': Delta_sq_pbcs,
        'Delta_ed': Delta_ed, 'Delta_hfb': Delta_hfb, 'Delta_pbcs': Delta_pbcs,
        'dN2_ed': dN2_ed, 'dN2_hfb': dN2_hfb, 'dN2_pbcs': dN2_pbcs,
    }

    mu_ed = chemical_potential(n_k_ed, E_sp)

    print(f"  {N:3d} {Delta_sq_ed:12.6f} {np.sqrt(Delta_sq_ed):10.6f} "
          f"{mu_ed:10.6f} {dN2_ed:10.4f} {np.max(uv_ed):10.6f}")


# ==============================================================================
#  SECTION 4: Exact Number Projection via Fomenko Integral
# ==============================================================================
#
# The exact number projection operator is:
#   P_N = (1/2pi) * integral_0^{2pi} exp(i*phi*(N_hat - N)) dphi
#
# For a BCS state |BCS> with occupation amplitudes (u_k, v_k):
#   The gauge-rotated BCS state |BCS(phi)> has:
#     v_k(phi) = v_k * exp(i*phi)    (pair carries charge 2)
#     u_k(phi) = u_k
#
# The projected density matrix element:
#   <c_k^dag c_k>_PBCS = (1/Norm) * (1/2pi) * int dphi * exp(-i*N*phi) *
#                          prod_k'(u_k'^2 + v_k'^2 * exp(2i*phi)) *
#                          v_k^2 * exp(2i*phi) / (u_k^2 + v_k^2*exp(2i*phi))
#
# For the pairing tensor:
#   kappa_k^{PBCS} = (1/Norm) * (1/2pi) * int dphi * exp(-i*N*phi) *
#                     prod_k'(...) * u_k * v_k * exp(i*phi) / (...)
#
# This is the Fomenko discretization (standard in nuclear DFT, Paper 02/03).

print(f"\n{'='*72}")
print(f"SECTION 4: Exact Number Projection (Fomenko Integral)")
print(f"{'='*72}")

def fomenko_projection(n_k_bcs, N_target, N_phi=64):
    """
    Exact number projection of BCS state via Fomenko discretization.

    Given BCS occupation numbers n_k (= v_k^2), compute the PBCS
    occupation numbers n_k^{PBCS} and pairing tensor kappa_k^{PBCS}
    for the N-particle projected state.

    Parameters:
    -----------
    n_k_bcs : array (M,)
        BCS occupation numbers v_k^2 for M modes
    N_target : int
        Target particle number for projection
    N_phi : int
        Number of Fomenko quadrature points (default 64)

    Returns:
    --------
    n_k_pbcs : array (M,)
        Projected occupation numbers
    kappa_k_pbcs : array (M,)
        Projected pairing tensor (u_k * v_k equivalent)
    norm : float
        Normalization <BCS|P_N|BCS>
    dN2_pbcs : float
        Number fluctuation in projected state (should be ~0)
    """
    M = len(n_k_bcs)
    v2 = np.clip(n_k_bcs, 1e-15, 1.0 - 1e-15)  # regularize
    u2 = 1.0 - v2

    phi_arr = np.linspace(0, 2*PI, N_phi, endpoint=False)
    dphi = 2*PI / N_phi

    # Overlap kernel: <BCS|BCS(phi)> = prod_k (u_k^2 + v_k^2 * exp(2i*phi))
    # Phase factor: exp(-i*N*phi)

    norm = 0.0  # (local)
    n_k_proj = np.zeros(M)
    kappa_proj = np.zeros(M, dtype=complex)

    for phi in phi_arr:
        # exp(2i*phi) for pair rotation
        e2iphi = np.exp(2j * phi)

        # Overlap kernel for each mode
        zk = u2 + v2 * e2iphi   # complex number for each k

        # Total overlap (product over all modes)
        # Use log to avoid overflow
        log_overlap = np.sum(np.log(zk))
        overlap = np.exp(log_overlap)

        # Phase factor for projection
        phase = np.exp(-1j * N_target * phi)

        # Weight
        w = phase * overlap * dphi / (2*PI)

        # Normalization
        norm += w

        # Occupation number: n_k = v_k^2 * e^{2i*phi} / z_k
        for k in range(M):
            nk_rotated = v2[k] * e2iphi / zk[k]
            n_k_proj[k] += w * nk_rotated

            # Pairing tensor: kappa_k = sqrt(u2_k * v2_k) * e^{i*phi} / z_k
            kappa_k = np.sqrt(u2[k] * v2[k]) * np.exp(1j*phi) / zk[k]
            kappa_proj[k] += w * kappa_k

    # Normalize
    n_k_pbcs = np.real(n_k_proj / norm)
    kappa_pbcs = kappa_proj / norm

    # Number fluctuation in projected state
    dN2_pbcs = 4.0 * np.sum(n_k_pbcs * (1.0 - n_k_pbcs))

    return n_k_pbcs, np.abs(kappa_pbcs), float(np.real(norm)), dN2_pbcs


# Run projection for each N sector
print(f"\n  Fomenko projection (N_phi = 64):")
print(f"  {'N':>3s} {'||n_proj-n_ed||':>16s} {'||n_proj-n_S52||':>16s} "
      f"{'Norm':>12s} {'<DN^2>_proj':>12s}")

proj_results = {}
for N in N_values:
    # Project from HFB occupations (these break number symmetry)
    n_k_hfb = results[N]['n_k_hfb']
    n_k_ed = results[N]['n_k_ed']
    n_k_s52_pbcs = results[N]['n_k_pbcs']  # S52's PBCS result for comparison

    n_k_proj, kappa_proj, norm, dN2_proj = fomenko_projection(n_k_hfb, N, N_phi=64)

    # Also project from ED occupations (should be nearly identity)
    n_k_proj_ed, kappa_proj_ed, norm_ed, dN2_proj_ed = fomenko_projection(
        n_k_ed, N, N_phi=64)

    diff_ed = np.linalg.norm(n_k_proj - n_k_ed)
    diff_s52 = np.linalg.norm(n_k_proj - n_k_s52_pbcs)

    proj_results[N] = {
        'n_k_proj': n_k_proj,
        'kappa_proj': kappa_proj,
        'norm': norm,
        'dN2': dN2_proj,
        'n_k_proj_from_ed': n_k_proj_ed,
    }

    print(f"  {N:3d} {diff_ed:16.8f} {diff_s52:16.8f} "
          f"{norm:12.6e} {dN2_proj:12.6f}")

print(f"\n  Occupation comparison (N=2 example):")
print(f"    {'k':>3s} {'label':>6s} {'n_HFB':>10s} {'n_proj':>10s} {'n_ED':>10s} "
      f"{'n_S52_PBCS':>12s} {'|kappa_proj|':>12s}")
N = 2
for k in range(8):
    print(f"    {k:3d} {labels[k]:>6s} {results[N]['n_k_hfb'][k]:10.6f} "
          f"{proj_results[N]['n_k_proj'][k]:10.6f} "
          f"{results[N]['n_k_ed'][k]:10.6f} "
          f"{results[N]['n_k_pbcs'][k]:12.6f} "
          f"{proj_results[N]['kappa_proj'][k]:12.6f}")


# ==============================================================================
#  SECTION 5: a_2 Correction from BCS Pairing
# ==============================================================================
#
# The BdG operator on a compact Riemannian manifold K:
#   D_BdG = ( D_K      Delta_hat )
#           ( Delta_hat^dag  -D_K )
#
# acts on sections of S(K) ⊕ S(K) (Nambu spinor bundle).
#
# The squared operator:
#   D_BdG^2 = ( D_K^2 + Delta_hat^dag*Delta_hat,   [D_K, Delta_hat] )
#              ([Delta_hat^dag, D_K],   D_K^2 + Delta_hat*Delta_hat^dag)
#
# For a SPATIALLY CONSTANT gap on a homogeneous space (SU(3) with Jensen metric):
#   [D_K, Delta_hat] = 0  (Delta commutes with D_K since both are left-invariant)
#   Delta_hat^dag * Delta_hat = |Delta|^2 * I  (constant endomorphism)
#
# Therefore D_BdG^2 is block-diagonal:
#   D_BdG^2 = diag(D_K^2 + |Delta|^2, D_K^2 + |Delta|^2)
#
# The heat kernel of (D_K^2 + |Delta|^2):
#   a_0(D_K^2 + |Delta|^2) = a_0(D_K^2)  (unchanged)
#   a_2(D_K^2 + |Delta|^2) = a_2(D_K^2) + (4pi)^{-d/2} * rank_S * |Delta|^2 * Vol
#                           = a_2(D_K^2) + a_0(D_K^2) * |Delta|^2
#
# For the Nambu-doubled system:
#   a_2(D_BdG^2) = 2 * a_2(D_K^2) + 2 * a_0(D_K^2) * |Delta|^2
#
# The PHYSICAL a_2 (per Nambu component, entering the Planck mass formula):
#   a_2^{phys} = a_2(D_K^2) + a_0(D_K^2) * |Delta_eff|^2
#
# where |Delta_eff|^2 is the effective gap squared, measured in M_KK^{-2}.
#
# For BCS:  |Delta_eff|^2 = <Delta^2>_BCS
# For PBCS: |Delta_eff|^2 = <Delta^2>_PBCS  (from projected pairing tensor)
#
# The fractional correction:
#   delta = a_0 * |Delta_eff|^2 / a_2^{geom}
#         = (16*Vol / (4pi)^4) * |Delta_eff|^2 / ((4pi)^{-4} * (20R/3) * Vol)
#         = 16 * |Delta_eff|^2 / (20R/3)
#         = 48 * |Delta_eff|^2 / (20*R)
#         = 12 * |Delta_eff|^2 / (5*R)

print(f"\n{'='*72}")
print(f"SECTION 5: BCS Pairing Correction to a_2")
print(f"{'='*72}")

# The gap entering the spectral action is the BdG gap Delta_eff.
# In the framework, this is related to the BCS condensation energy:
#   E_cond = -(1/2) * sum_k Delta_k * u_k * v_k
#   |Delta_eff|^2 ~ sum_k Delta_k^2 / N_modes
#
# From S52 HFB data, we can extract Delta_k directly from the pairing tensor.
# Delta_k = -sum_k' V_{kk'} * u_k' * v_k'

def compute_gap_squared(n_k, V_bare):
    """
    Compute |Delta_eff|^2 from occupations and interaction.

    Delta_k = -sum_k' V_{kk'} * sqrt(n_k'*(1-n_k'))
    |Delta_eff|^2 = (1/N_modes) * sum_k Delta_k^2

    Returns Delta_eff^2 in M_KK^2 units.
    """
    uv = np.sqrt(np.clip(n_k * (1.0 - n_k), 0, None))
    Delta_k = -V_bare @ uv
    return np.mean(Delta_k**2), Delta_k

def compute_pairing_energy(n_k, V_bare):
    """
    Pairing energy E_pair = -(1/2) sum_{kk'} V_{kk'} kappa_k kappa_k'
    where kappa_k = u_k * v_k = sqrt(n_k*(1-n_k))
    """
    kappa = np.sqrt(np.clip(n_k * (1.0 - n_k), 0, None))
    return -0.5 * kappa @ V_bare @ kappa

# Compute for each source of occupations
print(f"\n  Gap-squared and pairing energy per sector:")
print(f"  {'N':>3s} {'Source':>8s} {'|Delta|^2':>12s} {'E_pair':>10s} {'delta_a2':>10s}")

# The BCS/PBCS correction ratios
delta_ratios = {}

for N in N_values:
    for source, key in [('ED', 'n_k_ed'), ('HFB', 'n_k_hfb'), ('PBCS', 'n_k_pbcs')]:
        n_k = results[N][key]
        D2, Dk = compute_gap_squared(n_k, V_bare)
        E_pair = compute_pairing_energy(n_k, V_bare)

        # Fractional correction to a_2:
        # delta = 12 * |Delta_eff|^2 / (5*R)
        # BUT: |Delta_eff|^2 is in M_KK^2, and R is also in M_KK^2 (curvature of K)
        # So delta is dimensionless — correct.
        delta = 12.0 * D2 / (5.0 * R_fold)

        if source not in delta_ratios:
            delta_ratios[source] = {}
        delta_ratios[source][N] = delta

        print(f"  {N:3d} {source:>8s} {D2:12.8f} {E_pair:10.6f} {delta:10.6f}")

# Also compute from projected occupations
for N in N_values:
    n_k_proj = proj_results[N]['n_k_proj']
    D2, Dk = compute_gap_squared(n_k_proj, V_bare)
    E_pair = compute_pairing_energy(n_k_proj, V_bare)
    delta = 12.0 * D2 / (5.0 * R_fold)

    if 'PROJ' not in delta_ratios:
        delta_ratios['PROJ'] = {}
    delta_ratios['PROJ'][N] = delta

    print(f"  {N:3d} {'PROJ':>8s} {D2:12.8f} {E_pair:10.6f} {delta:10.6f}")


# ==============================================================================
#  SECTION 6: Lipkin-Nogami (LN) Correction — Perturbative Number Projection
# ==============================================================================
#
# The Lipkin-Nogami method adds a lambda_2 * (N_hat - N)^2 term:
#   H_LN = H - lambda * N_hat - lambda_2 * (N_hat - N)^2
#
# The LN correction to the pairing energy:
#   delta_E_LN = lambda_2 * <(Delta N)^2>_BCS
#
# where lambda_2 = - V_pair / (4 * sum_k u_k^2 v_k^2) (Paper 03 formula)
#
# The LN correction to a_2 comes through the modified gap:
#   |Delta_LN|^2 ≈ |Delta_BCS|^2 * (1 - 2*lambda_2 * <(DN)^2> / E_cond)
#
# For our 8-mode system, this is a significant correction (Paper 17: ultrasmall).

print(f"\n{'='*72}")
print(f"SECTION 6: Lipkin-Nogami Correction")
print(f"{'='*72}")

def lipkin_nogami_lambda2(n_k, V_bare):
    """
    Compute Lipkin-Nogami lambda_2 parameter.

    lambda_2 = -<HNN>/(2*<NN>)  (approximate)

    For the pairing Hamiltonian:
      lambda_2 ≈ -V_pair_avg / (4 * sum_k u_k^2 * v_k^2)

    where V_pair_avg = average pairing matrix element.
    """
    u2v2 = n_k * (1.0 - n_k)
    sum_u2v2 = np.sum(u2v2)

    # Average pairing strength
    V_pair_avg = np.mean(V_bare[np.triu_indices(len(n_k), k=1)])

    if sum_u2v2 < 1e-15:
        return 0.0

    lambda2 = -V_pair_avg / (4.0 * sum_u2v2)
    return lambda2

print(f"\n  Lipkin-Nogami parameters:")
print(f"  {'N':>3s} {'lambda_2':>12s} {'<DN^2>_HFB':>12s} {'dE_LN':>10s} {'dDelta^2/Delta^2':>18s}")

for N in N_values:
    n_k_hfb = results[N]['n_k_hfb']
    lam2 = lipkin_nogami_lambda2(n_k_hfb, V_bare)
    dN2 = 4.0 * np.sum(n_k_hfb * (1.0 - n_k_hfb))

    dE_LN = lam2 * dN2

    # Relative change in Delta^2
    D2_hfb = Delta_eff_sq[N]['hfb']
    if D2_hfb > 1e-15:
        rel_change = 2.0 * abs(lam2) * dN2 / abs(E_cond)
    else:
        rel_change = 0.0  # (local)

    print(f"  {N:3d} {lam2:12.6f} {dN2:12.4f} {dE_LN:10.6f} {rel_change:18.6f}")


# ==============================================================================
#  SECTION 7: Exact ED Comparison — The Definitive Test
# ==============================================================================
#
# The MOST RELIABLE comparison is between:
#   (a) a_2 computed with ED occupation numbers (exact, number-projected)
#   (b) a_2 computed with HFB occupation numbers (number-broken BCS)
#
# The ED ground state IS the number-projected state. The HFB state breaks U(1)_7.
# The question is: how different are the effective gaps, and hence the effective a_2?
#
# This is the nuclear DFT analog: compare ED with HFB for the SAME observable.

print(f"\n{'='*72}")
print(f"SECTION 7: Definitive Comparison — ED vs HFB vs PBCS vs PROJ")
print(f"{'='*72}")

print(f"\n  a_2 = a_2^{{geom}} * (1 + delta)")
print(f"  delta = 12*|Delta_eff|^2 / (5*R)")
print(f"  a_2^{{geom}} = {a2_geom:.10f}")
print(f"  R(tau_fold) = {R_fold:.10f}")
print(f"  a_0^{{geom}} = {a0_geom:.10f}")

print(f"\n  {'N':>3s} {'a2_ED':>14s} {'a2_HFB':>14s} {'a2_PBCS':>14s} {'a2_PROJ':>14s} "
      f"{'|PROJ-ED|/ED':>14s}")

gate_results = {}
for N in N_values:
    delta_ed = delta_ratios['ED'][N]
    delta_hfb = delta_ratios['HFB'][N]
    delta_pbcs = delta_ratios['PBCS'][N]
    delta_proj = delta_ratios['PROJ'][N]

    a2_ed = a2_geom * (1.0 + delta_ed)
    a2_hfb = a2_geom * (1.0 + delta_hfb)
    a2_pbcs = a2_geom * (1.0 + delta_pbcs)
    a2_proj = a2_geom * (1.0 + delta_proj)

    # The gate comparison: PBCS (projected) vs BCS (unprojected HFB)
    frac_proj_vs_hfb = abs(a2_proj - a2_hfb) / a2_hfb * 100
    frac_ed_vs_hfb = abs(a2_ed - a2_hfb) / a2_hfb * 100
    frac_proj_vs_ed = abs(a2_proj - a2_ed) / a2_ed * 100

    gate_results[N] = {
        'a2_ed': a2_ed, 'a2_hfb': a2_hfb, 'a2_pbcs': a2_pbcs, 'a2_proj': a2_proj,
        'delta_ed': delta_ed, 'delta_hfb': delta_hfb, 'delta_pbcs': delta_pbcs,
        'delta_proj': delta_proj,
        'frac_proj_vs_hfb': frac_proj_vs_hfb,
        'frac_ed_vs_hfb': frac_ed_vs_hfb,
        'frac_proj_vs_ed': frac_proj_vs_ed,
    }

    print(f"  {N:3d} {a2_ed:14.10f} {a2_hfb:14.10f} {a2_pbcs:14.10f} {a2_proj:14.10f} "
          f"{frac_proj_vs_ed:13.6f}%")


# ==============================================================================
#  SECTION 8: Convergence Test — N_phi Dependence
# ==============================================================================

print(f"\n{'='*72}")
print(f"SECTION 8: Fomenko Convergence Test (N=2)")
print(f"{'='*72}")

N_test = 2
n_k_test = results[N_test]['n_k_hfb']
Nphi_values = [8, 16, 32, 64, 128, 256]

print(f"\n  N_phi convergence for N={N_test}:")
print(f"  {'N_phi':>6s} {'n_B1_proj':>12s} {'sum_n':>10s} {'delta_a2':>12s}")

for Nphi in Nphi_values:
    n_proj, kappa, norm, dN2 = fomenko_projection(n_k_test, N_test, N_phi=Nphi)
    D2, _ = compute_gap_squared(n_proj, V_bare)
    delta = 12.0 * D2 / (5.0 * R_fold)

    print(f"  {Nphi:6d} {n_proj[4]:12.8f} {np.sum(n_proj):10.6f} {delta:12.8f}")


# ==============================================================================
#  SECTION 9: Nuclear Physics Benchmark
# ==============================================================================
#
# From Papers 02, 03, 15, 17:
# - For A ~ 8-20 nuclei, PBCS/BCS energy correction is 5-15%
# - For ultrasmall (N_dof < 10), particle number fluctuation is O(1)
# - The gap itself changes by ~10-30% under projection
# - BUT: the heat kernel coefficient depends on Delta^2, not Delta^4
#
# Key scaling: the relative correction to a_2 from pairing is
#   delta ~ |Delta|^2 / R_fold
# NOT the pairing energy correction (which is different).

print(f"\n{'='*72}")
print(f"SECTION 9: Nuclear Physics Benchmark")
print(f"{'='*72}")

print(f"\n  Nuclear BCS systems comparison:")
print(f"  System       N_dof  (PBCS-BCS)/BCS%  Reference")
print(f"  ^16O (sd)       6      8-12%         Paper 03 (Duguet et al.)")
print(f"  ^18O             8      5-10%         Paper 02 (HFB continuum)")
print(f"  ^24Mg           12      3-8%          Paper 03")
print(f"  ^28Si           12      2-6%          Paper 03")
print(f"  Ultrasmall      ~8      10-30%        Paper 17 (von Delft & Ralph)")
print(f"  Framework        8      see below     This computation")

print(f"\n  Key diagnostic: <(Delta N)^2> / N for each sector")
for N in N_values:
    dN2_hfb = 4.0 * np.sum(results[N]['n_k_hfb'] * (1.0 - results[N]['n_k_hfb']))
    dN2_ed = 4.0 * np.sum(results[N]['n_k_ed'] * (1.0 - results[N]['n_k_ed']))

    print(f"  N={N}: <DN^2>_HFB/N = {dN2_hfb/N:.3f}, <DN^2>_ED/N = {dN2_ed/N:.3f}")
    print(f"         <DN^2>_HFB = {dN2_hfb:.3f} (comparable to N={N}!)")

# ==============================================================================
#  SECTION 10: Energy-Level Crossing Correction
# ==============================================================================
#
# An important additional contribution: the Strutinsky-type shell correction.
# When occupations change under projection, the SPECTRAL DENSITY seen by the
# heat kernel also changes. This is captured through the density-weighted
# trace:
#   a_2^{occ} = sum_k n_k * a_2(k)
#
# where a_2(k) is the contribution from mode k.
# For a homogeneous space, a_2(k) is the SAME for all modes (constant R).
# So: a_2^{occ} = (sum_k n_k) * a_2^{per_mode} = N * a_2^{per_mode}
# This is INDEPENDENT of the distribution of n_k (only total N matters).
#
# Therefore: the GEOMETRIC a_2 contribution is EXACTLY the same for
# BCS and PBCS states (by construction of number projection: sum n_k = N).
#
# The ONLY difference comes from the PAIRING correction |Delta|^2.

print(f"\n{'='*72}")
print(f"SECTION 10: Structural Analysis — What Changes Under Projection?")
print(f"{'='*72}")

print(f"\n  The geometric a_2 = (4pi)^{{-4}} * (20R/3) * Vol = {a2_geom:.10f}")
print(f"  This is FIXED by the metric. Projection does NOT change it.")
print(f"  Only the pairing correction delta = 12*|Delta_eff|^2/(5*R) changes.")

print(f"\n  Pairing correction comparison:")
print(f"  {'N':>3s} {'delta_HFB':>12s} {'delta_PROJ':>12s} {'delta_ED':>12s} "
      f"{'|PROJ-HFB|':>12s} {'Relative%':>10s}")

for N in N_values:
    dh = delta_ratios['HFB'][N]
    dp = delta_ratios['PROJ'][N]
    de = delta_ratios['ED'][N]

    abs_diff = abs(dp - dh)
    # Relative to TOTAL a_2 (including correction)
    a2_hfb = a2_geom * (1.0 + dh)
    rel = abs_diff * a2_geom / a2_hfb * 100

    print(f"  {N:3d} {dh:12.8f} {dp:12.8f} {de:12.8f} "
          f"{abs_diff:12.8f} {rel:10.4f}%")


# ==============================================================================
#  SECTION 11: Gate Verdict
# ==============================================================================

print(f"\n{'='*72}")
print(f"SECTION 11: GATE VERDICT — PROJ-A2-61")
print(f"{'='*72}")

# The gate comparison is: |a_2^{PBCS} - a_2^{BCS}| / a_2^{BCS}
# PBCS = exact number-projected (Fomenko from HFB, or ED directly)
# BCS = unprojected HFB

# For the gate, use N=2 (the physical pair sector from S52)
# and compare ALL methods

print(f"\n  Method 1: Direct ED vs HFB comparison (most reliable)")
print(f"    ED occupations = exact, number-conserving")
print(f"    HFB occupations = BCS, number-breaking")
print(f"    The ED state IS the number-projected state.")

# Collect all fractional differences
all_fracs = []
print(f"\n  {'N':>3s} {'|a2_ED - a2_HFB| / a2_HFB':>28s}")
for N in N_values:
    f = gate_results[N]['frac_ed_vs_hfb']
    all_fracs.append(f)
    print(f"  {N:3d} {f:27.6f}%")

max_frac = max(all_fracs)
mean_frac = np.mean(all_fracs)

print(f"\n  Maximum fractional difference (ED vs HFB): {max_frac:.4f}%")
print(f"  Mean fractional difference: {mean_frac:.4f}%")

print(f"\n  Method 2: Fomenko-projected vs HFB")
all_fracs2 = []
print(f"\n  {'N':>3s} {'|a2_PROJ - a2_HFB| / a2_HFB':>30s}")
for N in N_values:
    f = gate_results[N]['frac_proj_vs_hfb']
    all_fracs2.append(f)
    print(f"  {N:3d} {f:29.6f}%")

max_frac2 = max(all_fracs2)
mean_frac2 = np.mean(all_fracs2)

print(f"\n  Maximum fractional difference (PROJ vs HFB): {max_frac2:.4f}%")
print(f"  Mean fractional difference: {mean_frac2:.4f}%")

# Use the LARGER of the two (conservative)
gate_frac = max(max_frac, max_frac2)

print(f"\n  GATE VALUE (conservative, max over all N and methods): {gate_frac:.4f}%")

if gate_frac < 5.0:
    verdict = "PASS"
    verdict_detail = f"< 5% threshold"
elif gate_frac > 20.0:
    verdict = "FAIL"
    verdict_detail = f"> 20% threshold"
else:
    verdict = "INFO"
    verdict_detail = f"between 5-20%"

print(f"\n  *** PROJ-A2-61: {verdict} ***")
print(f"  {verdict_detail}")
print(f"  |a_2^{{PBCS}} - a_2^{{BCS}}| / a_2^{{BCS}} = {gate_frac:.4f}%")


# ==============================================================================
#  SECTION 12: Decomposition of the Correction
# ==============================================================================

print(f"\n{'='*72}")
print(f"SECTION 12: Physics Decomposition")
print(f"{'='*72}")

print(f"\n  The total a_2 has TWO components:")
print(f"    1. Geometric: a_2^{{geom}} = {a2_geom:.10f} (FIXED, state-independent)")
print(f"    2. Pairing:   delta * a_2^{{geom}} (state-dependent)")
print(f"")
print(f"  The geometric term dominates because:")
print(f"    delta ~ |Delta_eff|^2 / R ~ {delta_ratios['ED'][2]:.6f} (for N=2)")
print(f"    i.e., the pairing correction is ~ {delta_ratios['ED'][2]*100:.3f}% of geometric a_2")
print(f"")
print(f"  Number projection modifies delta by:")
max_delta_diff = max(abs(delta_ratios['PROJ'][N] - delta_ratios['HFB'][N])
                     for N in N_values)
max_delta_hfb = max(delta_ratios['HFB'][N] for N in N_values)
print(f"    |delta_PROJ - delta_HFB| <= {max_delta_diff:.8f}")
print(f"    Relative to delta_HFB: {max_delta_diff/max_delta_hfb*100:.2f}% (of the correction)")
print(f"    Relative to total a_2: {max_delta_diff * a2_geom / (a2_geom * (1.0 + max_delta_hfb)) * 100:.4f}%")
print(f"")
print(f"  Nuclear physics interpretation:")
print(f"    N_dof = 8 modes is equivalent to the sd-shell (^16O-^28Si)")
print(f"    In nuclei: PBCS/BCS energy ~ 5-15% for sd-shell")
print(f"    Here: a_2 correction ~ {gate_frac:.2f}%")
print(f"    This is SMALLER than nuclear pairing because:")
print(f"      (a) R(tau_fold) = {R_fold:.3f} >> |Delta_eff|^2 ~ {Delta_eff_sq[2]['ed']:.6f}")
print(f"      (b) a_2 depends on Delta^2 (quadratic), not Delta (linear)")
print(f"      (c) The geometric term is the O(1) contribution; pairing is a perturbation")


# ==============================================================================
#  SECTION 13: Save Results
# ==============================================================================

print(f"\n{'='*72}")
print(f"SECTION 13: Saving Results")
print(f"{'='*72}")

save_dict = {
    # Gate
    'gate_name': 'PROJ-A2-61',
    'gate_verdict': verdict,
    'gate_value_pct': gate_frac,

    # Geometric a_2
    'a2_geom': a2_geom,
    'a0_geom': a0_geom,
    'R_fold': R_fold,
    'tau_fold': tau_fold,

    # Per-sector results
    'N_values': np.array(N_values),
}

for N in N_values:
    prefix = f'N{N}_'
    save_dict[prefix + 'a2_ed'] = gate_results[N]['a2_ed']
    save_dict[prefix + 'a2_hfb'] = gate_results[N]['a2_hfb']
    save_dict[prefix + 'a2_pbcs'] = gate_results[N]['a2_pbcs']
    save_dict[prefix + 'a2_proj'] = gate_results[N]['a2_proj']
    save_dict[prefix + 'delta_ed'] = gate_results[N]['delta_ed']
    save_dict[prefix + 'delta_hfb'] = gate_results[N]['delta_hfb']
    save_dict[prefix + 'delta_pbcs'] = gate_results[N]['delta_pbcs']
    save_dict[prefix + 'delta_proj'] = gate_results[N]['delta_proj']
    save_dict[prefix + 'frac_ed_vs_hfb'] = gate_results[N]['frac_ed_vs_hfb']
    save_dict[prefix + 'frac_proj_vs_hfb'] = gate_results[N]['frac_proj_vs_hfb']
    save_dict[prefix + 'frac_proj_vs_ed'] = gate_results[N]['frac_proj_vs_ed']
    save_dict[prefix + 'n_proj'] = proj_results[N]['n_k_proj']
    save_dict[prefix + 'kappa_proj'] = proj_results[N]['kappa_proj']
    save_dict[prefix + 'dN2'] = proj_results[N]['dN2']
    save_dict[prefix + 'Delta_sq_ed'] = Delta_eff_sq[N]['ed']
    save_dict[prefix + 'Delta_sq_hfb'] = Delta_eff_sq[N]['hfb']
    save_dict[prefix + 'Delta_sq_pbcs'] = Delta_eff_sq[N]['pbcs']

np.savez('s61_proj_a2.npz', **save_dict)
print(f"  Saved: s61_proj_a2.npz")
print(f"  Keys: {sorted(save_dict.keys())}")


# ==============================================================================
#  SECTION 14: Summary Figure
# ==============================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel 1: a_2 comparison across methods
ax = axes[0, 0]
x = np.arange(len(N_values))
width = 0.2  # (local)
a2_ed = [gate_results[N]['a2_ed'] for N in N_values]
a2_hfb = [gate_results[N]['a2_hfb'] for N in N_values]
a2_proj = [gate_results[N]['a2_proj'] for N in N_values]
a2_pbcs = [gate_results[N]['a2_pbcs'] for N in N_values]

ax.bar(x - 1.5*width, a2_ed, width, label='ED (exact)', color='C0')
ax.bar(x - 0.5*width, a2_hfb, width, label='HFB (broken)', color='C1')
ax.bar(x + 0.5*width, a2_proj, width, label='Fomenko PROJ', color='C2')
ax.bar(x + 1.5*width, a2_pbcs, width, label='S52 PBCS', color='C3')
ax.axhline(a2_geom, color='k', ls='--', alpha=0.5, label=f'geometric ({a2_geom:.6f})')
ax.set_xticks(x)
ax.set_xticklabels([f'N={N}' for N in N_values])
ax.set_ylabel('$a_2$')
ax.set_title('$a_2$ by Method and Sector')
ax.legend(fontsize=8)

# Panel 2: Fractional corrections
ax = axes[0, 1]
delta_ed_arr = [delta_ratios['ED'][N]*100 for N in N_values]
delta_hfb_arr = [delta_ratios['HFB'][N]*100 for N in N_values]
delta_proj_arr = [delta_ratios['PROJ'][N]*100 for N in N_values]

ax.plot(N_values, delta_ed_arr, 'o-', label='ED', color='C0')
ax.plot(N_values, delta_hfb_arr, 's-', label='HFB', color='C1')
ax.plot(N_values, delta_proj_arr, '^-', label='Fomenko PROJ', color='C2')
ax.set_xlabel('N (particle number)')
ax.set_ylabel('Pairing correction $\\delta$ (%)')
ax.set_title('Pairing Correction to $a_2$')
ax.legend()
ax.grid(True, alpha=0.3)

# Panel 3: |a2_PROJ - a2_HFB| / a2_HFB
ax = axes[1, 0]
frac_arr = [gate_results[N]['frac_proj_vs_hfb'] for N in N_values]
frac_ed_arr = [gate_results[N]['frac_ed_vs_hfb'] for N in N_values]

ax.bar(x - 0.2, frac_arr, 0.4, label='|PROJ-HFB|/HFB', color='C2')
ax.bar(x + 0.2, frac_ed_arr, 0.4, label='|ED-HFB|/HFB', color='C0')
ax.axhline(5.0, color='g', ls='--', label='PASS threshold (5%)')
ax.axhline(20.0, color='r', ls='--', label='FAIL threshold (20%)')
ax.set_xticks(x)
ax.set_xticklabels([f'N={N}' for N in N_values])
ax.set_ylabel('Fractional difference (%)')
ax.set_title('Gate Criterion: PROJ-A2-61')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 4: Number fluctuations
ax = axes[1, 1]
dN2_hfb = [4*np.sum(results[N]['n_k_hfb']*(1-results[N]['n_k_hfb'])) for N in N_values]
dN2_ed = [4*np.sum(results[N]['n_k_ed']*(1-results[N]['n_k_ed'])) for N in N_values]
dN2_proj = [proj_results[N]['dN2'] for N in N_values]

ax.plot(N_values, dN2_hfb, 'o-', label='HFB (broken $U(1)_7$)', color='C1')
ax.plot(N_values, dN2_ed, 's-', label='ED (exact)', color='C0')
ax.plot(N_values, dN2_proj, '^-', label='Fomenko PROJ', color='C2')
ax.plot(N_values, N_values, 'k--', alpha=0.3, label='$\\langle\\Delta N^2\\rangle = N$')
ax.set_xlabel('N (particle number)')
ax.set_ylabel('$\\langle(\\Delta N)^2\\rangle$')
ax.set_title('Number Fluctuations')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

plt.suptitle(f'PROJ-A2-61: Number Projection for Heat Kernel | Verdict: {verdict} ({gate_frac:.3f}%)',
             fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('s61_proj_a2.png', dpi=150, bbox_inches='tight')
print(f"  Saved: s61_proj_a2.png")

print(f"\n{'='*72}")
print(f"COMPUTATION COMPLETE")
print(f"  Gate: PROJ-A2-61 = {verdict}")
print(f"  Value: {gate_frac:.4f}%")
print(f"{'='*72}")
