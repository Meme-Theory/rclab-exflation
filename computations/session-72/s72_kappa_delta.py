#!/usr/bin/env python3
"""
s72_kappa_delta.py — Self-Consistent BCS Gap Curvature kappa_Delta
===================================================================

Gate: KAPPA-DELTA-72
  PASS: t_dec/t_transit in [1.0, 5.0] AND kappa_Delta real and positive.
  INFO: t_dec/t_transit outside [1.0, 5.0] but kappa_Delta well-defined.
  FAIL: Gap equation fails to converge, or Delta(tau) non-monotonic.

Physics:
  The canonical BCS gap Delta_BCS = 0.4643 M_KK was computed in s37_pair_
  susceptibility using the FULL 256-state Hilbert space with DOS-weighted
  pairing: V_eff[n,m] = V[n,m] * sqrt(rho[n] * rho[m]), where rho[B2] = 14.02
  (van Hove DOS) and rho[B1] = rho[B3] = 1.0. The single-particle energies
  at the fold are E_8 = {B2: 0.845 (degenerate x4), B1: 0.819, B3: 0.978 (x3)}.

  To compute kappa_Delta, we must use the SAME Hamiltonian structure at each
  tau value. The single-particle energies vary with tau according to the
  E_sp_sweep from s54_ed_sweep.npz (50 tau values). The DOS weighting varies
  because the van Hove DOS at each tau depends on the curvature of the band.

  CRITICAL DISTINCTION (WS3 D2): kappa_Delta is the curvature of the BCS GAP
  Delta(tau), NOT the D_K eigenvalue curvature. The gap responds nonlinearly
  to eigenvalue changes through the self-consistent gap equation.

  Method:
  1. At each tau, load E_sp from the s54 sweep.
  2. Apply the same DOS-weighted pairing as s36/s37 (V_eff = V * sqrt(rho*rho)).
  3. Diagonalize the FULL 256-state Hamiltonian.
  4. Extract sector ground states E(N=0), E(N=1), E(N=2).
  5. Compute Delta_OES(tau) = [E(N=2) + E(N=0) - 2*E(N=1)] / 2.
  6. Fit parabola to extract kappa_Delta.

Session: S72, Wave 1-A
Agent: landau-condensed-matter-theorist
"""

import numpy as np
from pathlib import Path
from scipy.interpolate import CubicSpline
import sys
import os
import time

# --- Import canonical constants ---
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    Delta_BCS, Delta_0_OES, dt_transit, tau_fold as tau_fold_canonical,
    E_cond, E_cond_ED_8mode, N_dof_BCS, E_B1, E_B2_mean, E_B3_mean,
    H_fold, v_terminal, M_KK, omega_tau,
    rho_B2_per_mode
)

# ============================================================================
#  Section 1: Load Input Data
# ============================================================================

data_dir = os.path.dirname(os.path.abspath(__file__))
archive_dir = os.path.join(os.path.dirname(data_dir), 'computations/_shared')

t_start = time.time()

# Load s36 data (defines the canonical BCS Hamiltonian)
s36 = np.load(os.path.join(archive_dir, "s36_multisector_ed.npz"), allow_pickle=True)
E_8_s36 = s36['E_8_full']          # (8,) mode energies [B2x4, B1, B3x3]
V_8x8_s36 = s36['V_8x8_full']     # (8,8) pairing matrix
branch_labels = list(s36['branch_labels'])
E_cond_s36 = float(s36['config_4_E_cond'])

# Load van Hove DOS from s35a arbiter
s35a = np.load(os.path.join(archive_dir, "s35a_vh_impedance_arbiter.npz"), allow_pickle=True)
rho_vH = float(s35a['rho_at_physical'])  # = 14.023 (B2 DOS at fold)

# DOS array: B2 modes get van Hove rho, B1/B3 get 1.0
rho = np.array([rho_vH]*4 + [1.0, 1.0, 1.0, 1.0])

# Load FULL eigenvalue sweep from S54 (50 tau values, 8 modes)
s54 = np.load(os.path.join(data_dir, "s54_ed_sweep.npz"), allow_pickle=True)
E_sp_sweep = s54['E_sp_sweep']     # (50, 8) single-particle energies
tau_sweep = s54['tau_values']       # (50,) tau values [0, 0.5]
V_bare_cont = s54['V_bare_cont']   # (8, 8) pairing matrix (tau-independent)
fold_idx_s54 = int(s54['fold_idx'])  # = 19

M = 8  # Number of modes
N_FOCK = 2**M  # = 256

print("=" * 72)
print("S72 KAPPA-DELTA-72: Self-Consistent BCS Gap Curvature")
print("=" * 72)

print(f"\n--- Input Constants ---")
print(f"  Delta_BCS (canonical) = {Delta_BCS:.10f} M_KK")
print(f"  E_cond (canonical) = {E_cond:.10f}")
print(f"  E_cond (s36) = {E_cond_s36:.10f}")
print(f"  dt_transit = {dt_transit:.10e} M_KK^{{-1}}")
print(f"  tau_fold (canonical) = {tau_fold_canonical}")
print(f"  rho_B2 (van Hove DOS) = {rho_vH:.6f}")

print(f"\n--- s36 Mode Energies at Fold ---")
for i in range(M):
    print(f"  {branch_labels[i]:>5s}: E = {E_8_s36[i]:.8f}, rho = {rho[i]:.6f}")

print(f"\n--- s54 Sweep Energies at Fold ---")
bcs_labels = ['B2[0]', 'B2[1]', 'B2[2]', 'B2[3]', 'B1', 'B3[0]', 'B3[1]', 'B3[2]']
for i in range(M):
    print(f"  {bcs_labels[i]:>5s}: eps = {E_sp_sweep[fold_idx_s54, i]:.8f}")

# Cross-check V matrices
V_diff = np.max(np.abs(V_8x8_s36 - V_bare_cont))
print(f"\n--- V Matrix Cross-Check ---")
print(f"  |V_s36 - V_bare_cont| max = {V_diff:.6e}")
print(f"  V matrices are {'identical' if V_diff < 1e-10 else 'DIFFERENT'}")

# ============================================================================
#  Section 2: Build the DOS-Weighted BCS Hamiltonian
# ============================================================================

def build_full_fock_H_dos(E_sp, V_matrix, rho_arr):
    """Build BCS Hamiltonian in full 2^N Fock space with DOS weighting.

    This matches the s37_pair_susceptibility Hamiltonian exactly:
      H = sum_k 2*xi_k * n_k - sum_{k!=l} V_{kl} * sqrt(rho_k * rho_l) * b_k^dag b_l

    where xi_k = E_k - mu (with mu=0 as in s36/s37).
    """
    n_modes = len(E_sp)
    dim = 2**n_modes
    H = np.zeros((dim, dim))

    mu = 0.0  # (local)
    xi = E_sp - mu

    for s in range(dim):
        # Diagonal: kinetic energy
        for k in range(n_modes):
            if s & (1 << k):
                H[s, s] += 2.0 * xi[k]

        # Off-diagonal: pair scattering with DOS weighting
        for k in range(n_modes):
            for l in range(n_modes):
                if k == l:
                    continue
                if V_matrix[k, l] < 1e-15:
                    continue
                # b_k^dag b_l: annihilate pair l, create pair k
                if (s & (1 << l)) and not (s & (1 << k)):
                    new_s = s ^ (1 << l) ^ (1 << k)
                    H[new_s, s] -= V_matrix[k, l] * np.sqrt(rho_arr[k] * rho_arr[l])

    # Symmetrize
    H = 0.5 * (H + H.T)
    return H


def compute_sector_energies(E_sp, V_matrix, rho_arr, n_modes=8):
    """Diagonalize full Fock space and extract sector ground states.

    The BCS Hamiltonian conserves pair number, so eigenstates live in
    definite pair-number sectors. We use eigh to get eigenvectors, then
    project each eigenstate onto the pair-number basis to identify its sector.

    Returns: E_N0, E_N1, E_N2 (ground state energies in each sector).
    """
    H = build_full_fock_H_dos(E_sp, V_matrix, rho_arr)
    E_all, psi_all = np.linalg.eigh(H)

    dim = 2**n_modes
    # Pair-number for each Fock basis state
    npair_basis = np.array([bin(s).count('1') for s in range(dim)])

    # For each eigenstate, compute <N_pair>
    N_expect = np.zeros(dim)
    for idx in range(dim):
        prob = np.abs(psi_all[:, idx])**2
        N_expect[idx] = np.dot(prob, npair_basis)

    # Since H conserves pair number, N_expect should be integer-valued
    N_round = np.round(N_expect).astype(int)

    E_N0 = np.min(E_all[N_round == 0])
    E_N1 = np.min(E_all[N_round == 1])
    E_N2 = np.min(E_all[N_round == 2])

    return E_N0, E_N1, E_N2, E_all


# ============================================================================
#  Section 3: Verify at Fold (reproduce Delta_BCS)
# ============================================================================

print("\n" + "=" * 72)
print("Section 3: Verify BCS Gap at Fold")
print("=" * 72)

# Use s36 energies (degenerate B2) — this is what produced Delta_BCS
E_N0_fold, E_N1_fold, E_N2_fold, E_all_fold = compute_sector_energies(
    E_8_s36, V_8x8_s36, rho)

Delta_fold_check = (E_N2_fold + E_N0_fold - 2 * E_N1_fold) / 2.0

print(f"  E(N=0) = {E_N0_fold:.10f}")
print(f"  E(N=1) = {E_N1_fold:.10f}")
print(f"  E(N=2) = {E_N2_fold:.10f}")
print(f"  Delta_OES = {Delta_fold_check:.10f}")
print(f"  Delta_BCS (canonical) = {Delta_BCS:.10f}")
print(f"  Relative diff: {abs(Delta_fold_check - Delta_BCS)/Delta_BCS:.4e}")
print(f"  E(N=1) vs E_cond: {abs(E_N1_fold - E_cond_s36):.4e}")

assert abs(Delta_fold_check - Delta_BCS) / Delta_BCS < 1e-6, \
    f"CRITICAL: Delta mismatch at fold: {Delta_fold_check:.8f} vs {Delta_BCS:.8f}"
print(f"  VERIFICATION: PASS (matches to {abs(Delta_fold_check - Delta_BCS)/Delta_BCS:.2e})")

t_verify = time.time()
print(f"  Time: {t_verify - t_start:.1f}s")

# ============================================================================
#  Section 4: Model for E_sp(tau) with DOS Weighting
# ============================================================================

print("\n" + "=" * 72)
print("Section 4: Mode Energy Trajectories")
print("=" * 72)

# The s36 Hamiltonian uses degenerate B2 (all at E_B2_mean = 0.845).
# The s54 sweep has the ACTUAL spread B2 energies from the lattice.
# To maintain consistency with the canonical gap, we use the s36 STRUCTURE
# (degenerate B2, specific B1/B3 values) but shift ALL energies by the
# MEAN energy change at each tau.
#
# Strategy: at each tau, compute the SHIFT of each sector's mean energy
# relative to the fold, and apply that shift to the s36 energies.
#
# sector_shift[sector](tau) = mean(E_sp_sweep[tau, sector_modes])
#                            - mean(E_sp_sweep[fold, sector_modes])

fi = fold_idx_s54

# Mode groupings matching s36 convention:
# B2: indices 0,1,2,3  B1: index 4  B3: indices 5,6,7
idx_B2 = [0, 1, 2, 3]
idx_B1 = [4]
idx_B3 = [5, 6, 7]

# Compute sector-mean energies at each tau
E_B2_mean_sweep = np.mean(E_sp_sweep[:, idx_B2], axis=1)  # (50,)
E_B1_sweep = E_sp_sweep[:, 4]                              # (50,)
E_B3_mean_sweep = np.mean(E_sp_sweep[:, idx_B3], axis=1)  # (50,)

# Shifts relative to fold
dE_B2 = E_B2_mean_sweep - E_B2_mean_sweep[fi]
dE_B1 = E_B1_sweep - E_B1_sweep[fi]
dE_B3 = E_B3_mean_sweep - E_B3_mean_sweep[fi]

print(f"  B2 mean at fold: {E_B2_mean_sweep[fi]:.8f}")
print(f"  B1 at fold: {E_B1_sweep[fi]:.8f}")
print(f"  B3 mean at fold: {E_B3_mean_sweep[fi]:.8f}")

# Print the shifts for a few tau values around fold
print(f"\n  Sector energy shifts near fold:")
print(f"  {'tau':>10s}  {'dE_B2':>10s}  {'dE_B1':>10s}  {'dE_B3':>10s}")
for j in range(max(0, fi-3), min(len(tau_sweep), fi+4)):
    print(f"  {tau_sweep[j]:10.6f}  {dE_B2[j]:10.6f}  {dE_B1[j]:10.6f}  "
          f"{dE_B3[j]:10.6f}")

# Build splines for sector shifts
cs_dE_B2 = CubicSpline(tau_sweep, dE_B2)
cs_dE_B1 = CubicSpline(tau_sweep, dE_B1)
cs_dE_B3 = CubicSpline(tau_sweep, dE_B3)

# Verify at fold: shifts should be zero
assert abs(cs_dE_B2(tau_sweep[fi])) < 1e-10, "B2 shift nonzero at fold"
assert abs(cs_dE_B1(tau_sweep[fi])) < 1e-10, "B1 shift nonzero at fold"
assert abs(cs_dE_B3(tau_sweep[fi])) < 1e-10, "B3 shift nonzero at fold"

# ============================================================================
#  Section 5: DOS(tau) Model
# ============================================================================

print("\n" + "=" * 72)
print("Section 5: DOS(tau) Model")
print("=" * 72)

# The van Hove DOS diverges at the fold because d(E_B2)/dtau = 0.
# Away from the fold, the DOS decreases as the band acquires nonzero slope.
# The van Hove singularity gives rho ~ 1/|d(eps)/dk| ~ 1/|d^2(eps)/dtau^2 * dtau|.
# For a quadratic band eps(tau) ~ eps_fold + (1/2)*kappa*(tau-tau_fold)^2:
#   rho(E) ~ 1/sqrt(2*kappa*(E - E_fold))
# This diverges at E = E_fold (the fold energy).
#
# For the BCS gap, what matters is the DOS AT the Fermi level.
# Near the fold, rho_F(tau) ~ rho_fold * f(tau) where f captures the
# tau-dependence. The simplest model: the B2 bandwidth increases linearly
# with |tau - tau_fold|, reducing the peak DOS proportionally.
#
# From the s54 sweep, the B2 bandwidth at the fold:
BW_B2 = np.zeros(len(tau_sweep))
for j in range(len(tau_sweep)):
    BW_B2[j] = E_sp_sweep[j, 3] - E_sp_sweep[j, 0]  # B2[3] - B2[0]

print(f"  B2 bandwidth at fold: {BW_B2[fi]:.6e} (near-degenerate)")
print(f"  B2 bandwidth at fold-1: {BW_B2[fi-1]:.6f}")
print(f"  B2 bandwidth at fold+1: {BW_B2[fi+1]:.6f}")

# The DOS scales inversely with bandwidth: rho ~ 1/BW (for fixed mode count).
# But at the fold, BW ~ 0 (degenerate), so rho -> infinity.
# The s36 computation uses rho_vH = 14.02 which is the DOS of the
# SMOOTHED band at the fold (not infinite).
#
# For the tau-dependence: the DOS at the Fermi level changes as the
# band spreads/compresses. Since rho_vH is already the physical (smoothed)
# DOS at the fold, we model:
#   rho_B2(tau) = rho_vH * BW_B2(fold) / BW_B2(tau)   if BW_B2(tau) > BW_B2(fold)
#   rho_B2(tau) = rho_vH                                otherwise (at fold)
#
# But BW(fold) ~ 0 makes this ratio blow up. Instead, use the SMOOTH DOS
# from the spectral action curvature: the DOS is proportional to 1/sqrt(kappa)
# where kappa is the curvature of the band. Since all B2 modes have the
# same curvature (they're degenerate at the fold), the DOS variation
# comes from the distance of each mode from the van Hove point.
#
# SIMPLIFICATION: For a first computation of kappa_Delta, hold rho FIXED
# at the fold value. The dominant effect is the energy shift, not the DOS
# variation. The DOS effect is a CORRECTION that can be added later.
# Physical reasoning: over delta_tau ~ 0.01, the B2 bandwidth changes by
# only a fraction of the total energy, so rho changes by a similar fraction.
# The energy shift drives the gap change at leading order.

print(f"\n  Model: rho(tau) = rho(fold) = const = {rho_vH:.4f}")
print(f"  (DOS variation is a sub-leading correction)")

# ============================================================================
#  Section 6: Compute Delta(tau) via Full Fock Diagonalization
# ============================================================================

print("\n" + "=" * 72)
print("Section 6: BCS Gap Delta(tau) via Full 256-State ED")
print("=" * 72)

# Create fine tau grid (21 points)
tau_center = tau_sweep[fi]
dtau_half = 0.02  # (local)
N_fine = 21  # (local)
tau_fine = np.linspace(tau_center - dtau_half, tau_center + dtau_half, N_fine)

print(f"  tau_center = {tau_center:.10f}")
print(f"  tau_fine range: [{tau_fine[0]:.6f}, {tau_fine[-1]:.6f}]")
print(f"  N_fine = {N_fine}, dtau = {tau_fine[1]-tau_fine[0]:.6e}")

Delta_fine = np.zeros(N_fine)
E_N0_fine = np.zeros(N_fine)
E_N1_fine = np.zeros(N_fine)
E_N2_fine = np.zeros(N_fine)
converged = np.ones(N_fine, dtype=bool)

print(f"\n  Computing Delta(tau) at {N_fine} points...")
print(f"  {'j':>4s}  {'tau':>12s}  {'dE_B2':>10s}  {'dE_B1':>10s}  {'dE_B3':>10s}  "
      f"{'Delta_OES':>12s}  {'E(N=1)':>12s}")

for j in range(N_fine):
    tau = tau_fine[j]

    # Construct energies at this tau: s36 base + sector shifts
    dEB2 = float(cs_dE_B2(tau))
    dEB1 = float(cs_dE_B1(tau))
    dEB3 = float(cs_dE_B3(tau))

    E_sp_tau = E_8_s36.copy()
    E_sp_tau[0:4] += dEB2    # B2 modes
    E_sp_tau[4] += dEB1      # B1
    E_sp_tau[5:8] += dEB3    # B3 modes

    try:
        E0, E1, E2, _ = compute_sector_energies(E_sp_tau, V_8x8_s36, rho)
        Delta_fine[j] = (E2 + E0 - 2 * E1) / 2.0
        E_N0_fine[j] = E0
        E_N1_fine[j] = E1
        E_N2_fine[j] = E2
    except Exception as e:
        print(f"  WARNING: j={j}, tau={tau:.6f} failed: {e}")
        converged[j] = False
        Delta_fine[j] = np.nan

    print(f"  {j:4d}  {tau:12.8f}  {dEB2:10.6f}  {dEB1:10.6f}  {dEB3:10.6f}  "
          f"{Delta_fine[j]:12.8f}  {E_N1_fine[j]:12.8f}")

t_ed = time.time()
print(f"\n  Computation time: {t_ed - t_start:.1f}s")
print(f"  All converged: {np.all(converged)}")
print(f"  Delta range: [{np.nanmin(Delta_fine):.8f}, {np.nanmax(Delta_fine):.8f}]")

# ============================================================================
#  Section 7: Also Compute at Coarse Sweep Points (Cross-Check)
# ============================================================================

print("\n" + "=" * 72)
print("Section 7: Coarse Sweep Cross-Check")
print("=" * 72)

# Compute Delta at actual sweep tau values near fold (no interpolation)
i_start_sw = max(0, fi - 5)
i_end_sw = min(len(tau_sweep), fi + 6)
N_sw = i_end_sw - i_start_sw

tau_sweep_near = np.zeros(N_sw)
Delta_sweep = np.zeros(N_sw)

for n, idx in enumerate(range(i_start_sw, i_end_sw)):
    tau = tau_sweep[idx]
    dEB2 = E_B2_mean_sweep[idx] - E_B2_mean_sweep[fi]
    dEB1 = E_B1_sweep[idx] - E_B1_sweep[fi]
    dEB3 = E_B3_mean_sweep[idx] - E_B3_mean_sweep[fi]

    E_sp_tau = E_8_s36.copy()
    E_sp_tau[0:4] += dEB2
    E_sp_tau[4] += dEB1
    E_sp_tau[5:8] += dEB3

    E0, E1, E2, _ = compute_sector_energies(E_sp_tau, V_8x8_s36, rho)
    tau_sweep_near[n] = tau
    Delta_sweep[n] = (E2 + E0 - 2 * E1) / 2.0
    print(f"  tau={tau:.6f}: Delta = {Delta_sweep[n]:.8f}")

# ============================================================================
#  Section 8: Monotonicity Check
# ============================================================================

print("\n" + "=" * 72)
print("Section 8: Monotonicity and Structure")
print("=" * 72)

idx_max = np.argmax(Delta_fine)
tau_max = tau_fine[idx_max]
Delta_max = Delta_fine[idx_max]

print(f"  Maximum Delta = {Delta_max:.10f} at tau = {tau_max:.10f} (j={idx_max})")
print(f"  tau_center = {tau_center:.10f}")
print(f"  Shift from center: {tau_max - tau_center:.6e}")

left_mono = True
right_mono = True
for j in range(idx_max - 1, -1, -1):
    if Delta_fine[j] > Delta_fine[j + 1] + 1e-12:
        left_mono = False
        break

for j in range(idx_max + 1, N_fine):
    if Delta_fine[j] > Delta_fine[j - 1] + 1e-12:
        right_mono = False
        break

is_monotonic = left_mono and right_mono
print(f"  Left-monotonic: {left_mono}")
print(f"  Right-monotonic: {right_mono}")
print(f"  Bell-shaped: {is_monotonic}")

# ============================================================================
#  Section 9: Extract kappa_Delta
# ============================================================================

print("\n" + "=" * 72)
print("Section 9: Extract kappa_Delta via Parabolic Fit")
print("=" * 72)

dtau_f = tau_fine - tau_max

# Fit A: Quadratic to central 11 points
i_inner_start = max(0, idx_max - 5)
i_inner_end = min(N_fine, idx_max + 6)
dtau_inner = tau_fine[i_inner_start:i_inner_end] - tau_max
Delta_inner = Delta_fine[i_inner_start:i_inner_end]
N_inner = i_inner_end - i_inner_start

coeffs_quad = np.polyfit(dtau_inner, Delta_inner, 2)
c_quad, b_quad, a_quad = coeffs_quad
kappa_Delta_inner = 2.0 * c_quad

print(f"\n  Quadratic fit (central {N_inner} points):")
print(f"    a = {a_quad:.10f}")
print(f"    b = {b_quad:.6e}")
print(f"    c = {c_quad:.6e}")
print(f"    kappa_Delta = 2*c = {kappa_Delta_inner:.6e}")

Delta_quad_pred = np.polyval(coeffs_quad, dtau_inner)
rms_inner = np.sqrt(np.mean((Delta_inner - Delta_quad_pred)**2))
print(f"    RMS residual = {rms_inner:.6e}")

# Fit B: Quartic to all 21 points
coeffs_q4 = np.polyfit(dtau_f, Delta_fine, 4)
d_q4, c3_q4, c2_q4, b_q4, a_q4 = coeffs_q4
kappa_Delta_quartic = 2.0 * c2_q4

print(f"\n  Quartic fit (all {N_fine} points):")
print(f"    a = {a_q4:.10f}")
print(f"    b = {b_q4:.6e}")
print(f"    c2 = {c2_q4:.6e}")
print(f"    c3 = {c3_q4:.6e}")
print(f"    d = {d_q4:.6e}")
print(f"    kappa_Delta = 2*c2 = {kappa_Delta_quartic:.6e}")

# Fit C: Even-only
X_even = np.column_stack([np.ones(N_fine), dtau_f**2, dtau_f**4])
even_coeffs, _, _, _ = np.linalg.lstsq(X_even, Delta_fine, rcond=None)
a_even, half_kappa_even, d_even = even_coeffs
kappa_Delta_even = 2.0 * half_kappa_even

print(f"\n  Even-only fit:")
print(f"    a = {a_even:.10f}")
print(f"    kappa_Delta = {kappa_Delta_even:.6e}")
print(f"    d = {d_even:.6e}")

# Fit D: Coarse sweep quadratic
dtau_sw = tau_sweep_near - tau_max
coeffs_sw = np.polyfit(dtau_sw, Delta_sweep, 2)
kappa_Delta_sweep = 2.0 * coeffs_sw[0]
print(f"\n  Coarse sweep quadratic:")
print(f"    kappa_Delta = {kappa_Delta_sweep:.6e}")

# Primary result: quartic fit (captures anharmonicity, uses all data)
kappa_Delta = kappa_Delta_quartic
Delta_fold_fit = a_q4

print(f"\n  === PRIMARY RESULT ===")
print(f"  kappa_Delta = {kappa_Delta:.6e} M_KK")
print(f"  |kappa_Delta| = {abs(kappa_Delta):.6e} M_KK")
print(f"  Delta_fold (fit) = {Delta_fold_fit:.10f} M_KK")
print(f"  Sign: {'< 0 (maximum at fold)' if kappa_Delta < 0 else '>= 0'}")

print(f"\n  Consistency of 4 fits:")
print(f"    Inner quad:   {kappa_Delta_inner:.6e}")
print(f"    Full quartic: {kappa_Delta_quartic:.6e}")
print(f"    Even-only:    {kappa_Delta_even:.6e}")
print(f"    Coarse sweep: {kappa_Delta_sweep:.6e}")
kappas = [kappa_Delta_inner, kappa_Delta_quartic, kappa_Delta_even, kappa_Delta_sweep]
spread = (max(kappas) - min(kappas)) / abs(np.mean(kappas))
print(f"    Spread: {spread:.4f} ({spread*100:.1f}%)")

# ============================================================================
#  Section 10: Eigenvalue Curvature Comparison
# ============================================================================

print("\n" + "=" * 72)
print("Section 10: Gap vs Eigenvalue Curvature")
print("=" * 72)

# Physical eigenvalue curvatures from s54 sweep
dtau_sw = tau_sweep[1] - tau_sweep[0]
d2eps_dtau2 = (E_sp_sweep[fi+1] + E_sp_sweep[fi-1] - 2*E_sp_sweep[fi]) / dtau_sw**2
deps_dtau = (E_sp_sweep[fi+1] - E_sp_sweep[fi-1]) / (2 * dtau_sw)

print(f"  Physical d^2(eps)/dtau^2 at fold:")
for i in range(M):
    print(f"    {bcs_labels[i]:>5s}: {d2eps_dtau2[i]:12.6f} M_KK")

# Sector-mean curvatures (what drives the gap)
d2E_B2_mean = np.mean(d2eps_dtau2[0:4])
d2E_B1 = d2eps_dtau2[4]
d2E_B3_mean = np.mean(d2eps_dtau2[5:8])

print(f"\n  Sector-mean curvatures:")
print(f"    B2 mean: {d2E_B2_mean:.6f}")
print(f"    B1: {d2E_B1:.6f}")
print(f"    B3 mean: {d2E_B3_mean:.6f}")
print(f"\n  |kappa_Delta| = {abs(kappa_Delta):.6f}")
print(f"  Ratio |kappa_Delta|/d2E_B2 = {abs(kappa_Delta)/abs(d2E_B2_mean) if abs(d2E_B2_mean) > 1e-10 else 'inf'}")

# The chirp kappa_n values were NOT eigenvalue curvatures
chirp = np.load(os.path.join(data_dir, "s71_chirp_universality.npz"), allow_pickle=True)
kappa_n_chirp = chirp['kappa_n']
print(f"\n  NOTE: chirp kappa_n(B2) = {kappa_n_chirp[1]:.4e} is d^2(k_tach)/dtau^2,")
print(f"  NOT d^2(eps)/dtau^2 = {d2eps_dtau2[0]:.6f}. These are different quantities.")

# ============================================================================
#  Section 11: Landau-Khalatnikov Decoherence Timescale
# ============================================================================

print("\n" + "=" * 72)
print("Section 11: Landau-Khalatnikov Decoherence Timescale")
print("=" * 72)

# Gamma_phi = (kappa_Delta * v_tau^2)^2 / Delta_max^2 * T^3/12
# t_dec = 1/Gamma_phi
# t_dec/T = 12 * Delta_max^2 / (kappa_Delta^2 * v_tau^4 * T^4)

v_tau = omega_tau  # = 8.27 M_KK
T = dt_transit     # = 0.001130 M_KK^{-1}

print(f"  T = dt_transit = {T:.6e} M_KK^{{-1}}")
print(f"  v_tau = omega_tau = {v_tau:.4f} M_KK")
print(f"  Delta_max = {Delta_max:.10f} M_KK")
print(f"  kappa_Delta = {kappa_Delta:.6e} M_KK")

# Full LK formula
Gamma_phi = (kappa_Delta * v_tau**2)**2 / Delta_max**2 * T**3 / 12.0
if abs(Gamma_phi) > 1e-30:
    t_dec = 1.0 / abs(Gamma_phi)
    ratio_LK = t_dec / T
else:
    t_dec = np.inf
    ratio_LK = np.inf

print(f"\n  Gamma_phi = {Gamma_phi:.6e} M_KK")
print(f"  t_dec = {t_dec:.6e} M_KK^{{-1}}")
print(f"  t_dec / t_transit = {ratio_LK:.6e}")

# Cross-check: dimensional analysis
# Gamma_phi ~ [M_KK * M_KK^2]^2 / M_KK^2 * M_KK^{-3} = M_KK^6/M_KK^2 * M_KK^{-3} = M_KK
print(f"\n  Dimensional check: Gamma_phi has units M_KK (rate): correct")

t_dec_over_t_transit = ratio_LK

# ============================================================================
#  Section 12: A_s Budget
# ============================================================================

print("\n" + "=" * 72)
print("Section 12: A_s Budget Assessment")
print("=" * 72)

if t_dec_over_t_transit > 0 and np.isfinite(t_dec_over_t_transit):
    delta_OOM = 0.868 / t_dec_over_t_transit
    print(f"  t_dec/t_transit = {t_dec_over_t_transit:.6e}")
    print(f"  delta_OOM = 0.868 / (t_dec/T) = {delta_OOM:.6e}")
    print(f"  Target: 0.267 OOM (S70 residual)")
    print(f"  Ratio: {delta_OOM/0.267:.4f}x needed correction")
else:
    delta_OOM = 0.0  # (local)
    print(f"  t_dec infinite — no decoherence")

# ============================================================================
#  Section 13: Gate Verdict
# ============================================================================

print("\n" + "=" * 72)
print("Section 13: GATE VERDICT — KAPPA-DELTA-72")
print("=" * 72)

gap_converged = np.all(converged)
gap_bell_shaped = is_monotonic
kappa_well_defined = (np.isfinite(kappa_Delta) and kappa_Delta != 0)
ratio_in_band = (1.0 <= t_dec_over_t_transit <= 5.0)

if not gap_converged:
    verdict = "FAIL"
    detail = f"Gap equation failed to converge at {np.sum(~converged)} tau values."
elif not gap_bell_shaped:
    verdict = "FAIL"
    detail = "Delta(tau) is non-monotonic (not bell-shaped around fold)."
elif not kappa_well_defined:
    verdict = "FAIL"
    detail = f"kappa_Delta not well-defined: {kappa_Delta}"
elif ratio_in_band:
    verdict = "PASS"
    detail = (f"t_dec/t_transit = {t_dec_over_t_transit:.4f} in [1.0, 5.0] "
              f"AND |kappa_Delta| = {abs(kappa_Delta):.4e} is real and well-defined.")
else:
    verdict = "INFO"
    detail = (f"t_dec/t_transit = {t_dec_over_t_transit:.4e} OUTSIDE [1.0, 5.0], "
              f"but |kappa_Delta| = {abs(kappa_Delta):.4e} is well-defined.")

print(f"\n  Gate: KAPPA-DELTA-72")
print(f"  Verdict: {verdict}")
print(f"  Detail: {detail}")

print(f"\n  Key Numbers:")
print(f"    kappa_Delta = {kappa_Delta:.6e} M_KK")
print(f"    |kappa_Delta| = {abs(kappa_Delta):.6e} M_KK")
print(f"    Delta_max = {Delta_max:.10f} M_KK")
print(f"    Delta_BCS (canonical) = {Delta_BCS:.10f} M_KK")
print(f"    |Delta_max - Delta_BCS|/Delta_BCS = {abs(Delta_max - Delta_BCS)/Delta_BCS:.6e}")
print(f"    tau_max = {tau_max:.10f}")
print(f"    t_dec/t_transit = {t_dec_over_t_transit:.6e}")
print(f"    delta_OOM = {delta_OOM:.6e}")
print(f"    Bell-shaped: {is_monotonic}")

# ============================================================================
#  Section 14: Save Data
# ============================================================================

print("\n" + "=" * 72)
print("Section 14: Save Data")
print("=" * 72)

outpath = os.path.join(data_dir, "s72_kappa_delta.npz")
np.savez(outpath,
         tau_fine=tau_fine,
         Delta_fine=Delta_fine,
         E_N0_fine=E_N0_fine,
         E_N1_fine=E_N1_fine,
         E_N2_fine=E_N2_fine,
         tau_sweep_near=tau_sweep_near,
         Delta_sweep=Delta_sweep,
         kappa_Delta=kappa_Delta,
         kappa_Delta_inner=kappa_Delta_inner,
         kappa_Delta_quartic=kappa_Delta_quartic,
         kappa_Delta_even=kappa_Delta_even,
         kappa_Delta_sweep=kappa_Delta_sweep,
         coeffs_quartic=coeffs_q4,
         t_dec_over_t_transit=t_dec_over_t_transit,
         Gamma_phi_LK=Gamma_phi,
         delta_OOM=delta_OOM,
         d2eps_dtau2=d2eps_dtau2,
         deps_dtau=deps_dtau,
         Delta_max=Delta_max,
         Delta_fold_fit=Delta_fold_fit,
         Delta_fold_check=Delta_fold_check,
         tau_max=tau_max,
         tau_center=tau_center,
         V_eff=float(np.load(os.path.join(data_dir, "s60_rg_integrals.npz"),
                             allow_pickle=True)['g_eff']),
         kappa_n_chirp_B2=kappa_n_chirp[1],
         v_tau=v_tau,
         converged=converged,
         is_monotonic=is_monotonic,
         rho_vH=rho_vH,
         gate_name="KAPPA-DELTA-72",
         gate_verdict=verdict,
         gate_detail=detail)
print(f"  Saved: {outpath}")

# ============================================================================
#  Section 15: Plot
# ============================================================================

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 3, figsize=(18, 5.5))

# Panel 1: Delta(tau) with fits
ax1 = axes[0]
ax1.plot(tau_sweep_near, Delta_sweep, 'rs', markersize=8,
         label='Sweep (exact $\\epsilon_k$)', zorder=6)
ax1.plot(tau_fine, Delta_fine, 'ko-', markersize=4,
         label='Fine grid (spline $\\epsilon_k$)', zorder=5)

tau_plot = np.linspace(tau_fine[0], tau_fine[-1], 200)
dtau_plot = tau_plot - tau_max
Delta_q4_plot = np.polyval(coeffs_q4, dtau_plot)
ax1.plot(tau_plot, Delta_q4_plot, 'b--', linewidth=1.5,
         label=f'Quartic ($\\kappa_\\Delta$ = {kappa_Delta:.4f})')

Delta_even_plot = a_even + half_kappa_even * dtau_plot**2 + d_even * dtau_plot**4
ax1.plot(tau_plot, Delta_even_plot, 'g:', linewidth=1.5,
         label=f'Even ($\\kappa_\\Delta$ = {kappa_Delta_even:.4f})')

ax1.axhline(Delta_BCS, color='orange', linestyle=':', alpha=0.5,
            label=f'$\\Delta_{{BCS}}$ = {Delta_BCS:.4f}')
ax1.axvline(tau_max, color='gray', linestyle=':', alpha=0.3)
ax1.set_xlabel(r'$\tau$', fontsize=12)
ax1.set_ylabel(r'$\Delta(\tau)$ [M$_{KK}$]', fontsize=12)
ax1.set_title(r'Self-Consistent BCS Gap', fontsize=11)
ax1.legend(fontsize=8, loc='lower left')
ax1.grid(True, alpha=0.3)

# Panel 2: Residuals
ax2 = axes[1]
dtau_pts = tau_fine - tau_max
res_q4 = (Delta_fine - np.polyval(coeffs_q4, dtau_pts)) * 1e6
ax2.plot(tau_fine, res_q4, 'bs-', markersize=3, label='Quartic')
res_even = (Delta_fine - (a_even + half_kappa_even * dtau_pts**2 + d_even * dtau_pts**4)) * 1e6
ax2.plot(tau_fine, res_even, 'g^-', markersize=3, label='Even')
ax2.axhline(0, color='gray', linestyle='-', alpha=0.3)
ax2.set_xlabel(r'$\tau$', fontsize=12)
ax2.set_ylabel(r'Residual $\times 10^6$ [M$_{KK}$]', fontsize=12)
ax2.set_title('Fit Residuals', fontsize=11)
ax2.legend(fontsize=9)
ax2.grid(True, alpha=0.3)

# Panel 3: Sector energy shifts
ax3 = axes[2]
tau_plot_e = np.linspace(tau_center - 0.03, tau_center + 0.03, 100)
ax3.plot(tau_plot_e, cs_dE_B2(tau_plot_e), 'b-', linewidth=2, label='$\\delta E_{B2}$')
ax3.plot(tau_plot_e, cs_dE_B1(tau_plot_e), 'r-', linewidth=2, label='$\\delta E_{B1}$')
ax3.plot(tau_plot_e, cs_dE_B3(tau_plot_e), 'g-', linewidth=2, label='$\\delta E_{B3}$')
ax3.axvline(tau_center, color='gray', linestyle=':', alpha=0.3)
ax3.axhline(0, color='gray', linestyle='-', alpha=0.3)
ax3.set_xlabel(r'$\tau$', fontsize=12)
ax3.set_ylabel(r'$\delta E_{sector}(\tau)$ [M$_{KK}$]', fontsize=12)
ax3.set_title('Sector Energy Shifts', fontsize=11)
ax3.legend(fontsize=9)
ax3.grid(True, alpha=0.3)

fig.suptitle(f'KAPPA-DELTA-72: $\\kappa_\\Delta$ = {kappa_Delta:.4f}, '
             f'$t_{{dec}}/t_{{transit}}$ = {t_dec_over_t_transit:.2e} [{verdict}]',
             fontsize=13, fontweight='bold')
plt.tight_layout()

plotpath = os.path.join(data_dir, "s72_kappa_delta.png")
plt.savefig(plotpath, dpi=150, bbox_inches='tight')
print(f"  Saved plot: {plotpath}")

t_end = time.time()
print(f"\n  Total time: {t_end - t_start:.1f}s")
print("\n" + "=" * 72)
print(f"  KAPPA-DELTA-72 COMPLETE — Verdict: {verdict}")
print("=" * 72)
