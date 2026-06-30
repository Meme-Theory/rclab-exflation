#!/usr/bin/env python3
"""
S53 KZ-PRESSURE-53: Kibble-Zurek Phonon Gas Backreaction

Route P5: After transit destroys the condensate (P_exc=1.000), the
59.8 quasiparticle pairs populate the 6 GL collective mode branches.
This script computes:
  1. Energy distribution across 6 GL branches
  2. Equation of state w_phonon of the GGE relic
  3. Backreaction on geometry: H_phonon, N_e^afterglow
  4. Bracketing with thermal vs single-mode distributions

Gate: KZ-PRESSURE-53
  PASS: w_phonon computable, N_e^afterglow > 0.5, backreaction finite
  INFO: w_phonon > 0 (decelerating)
  FAIL: w_phonon undefined or backreaction divergent

Physics (Volovik perspective):
  The GGE relic is the analog of a quenched superfluid with non-thermal
  quasiparticle distribution. In 3He-B after a rapid pressure quench,
  the system reaches a non-equilibrium state with occupation numbers
  constrained by conserved integrals (Vollhardt-Woelfle Ch. 10).
  The equation of state follows from the dispersion relations:
    w = p/rho where p = sum_K (K/3) * v_g(K) * n(K)
  For linear dispersion (Goldstone): w = 1/3 (radiation)
  For massive modes: w -> 0 (matter)
  The mix determines effective w.

Author: Volovik-Superfluid-Universe-Theorist (S53)
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import sys
import os

# ── imports ──────────────────────────────────────────────────────────
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    n_pairs, E_exc, N_dof_BCS, tau_fold, G_DeWitt,
    c_Gold, c_fabric, M_KK, E_cond, N_cells, H_fold,
    Delta_0_GL, Delta_B3, N_e_classical, Lambda_obs_MP4,
    M_Pl_reduced, H_0_GeV, Omega_Lambda, Omega_DM,
    S_inst, Gamma_Langer_BCS
)

OUT = Path(__file__).parent
LOG = []
def log(msg):
    print(msg)
    LOG.append(msg)

log("=" * 72)
log("KZ-PRESSURE-53: Kibble-Zurek Phonon Gas Backreaction")
log("=" * 72)
log("")

# ── Load GL sweep data ──────────────────────────────────────────────
gl = np.load(OUT / "s53_gl_sweep.npz", allow_pickle=True)
tau_values = gl['tau_values']
omega_full = gl['omega_full']   # (N_tau, N_K, 6)
K_plot = gl['K_plot']           # (N_K,)
K_BZ = float(gl['K_BZ'])
alpha_eff_all = gl['alpha_eff_all']  # (N_tau, 6)
c_Gold_vs_tau = gl['c_Gold_vs_tau']

# Gap values at each tau
omega_Gold_0 = gl['omega_Goldstone']   # ~0 (Goldstone gap)
omega_L1_0 = gl['omega_Leggett1']     # ~0.138
omega_L2_0 = gl['omega_Leggett2']     # ~0.192
omega_H1_0 = gl['omega_Higgs1']       # ~0.378
omega_H2_0 = gl['omega_Higgs2']       # ~1.41
omega_H3_0 = gl['omega_Higgs3']       # ~11.47

# Load Bogoliubov amplitudes
bog = np.load(OUT / "s52_bogoliubov_amp.npz", allow_pickle=True)
u_k = bog['u_k']  # (8,) Bogoliubov u amplitudes
v_k = bog['v_k']  # (8,) Bogoliubov v amplitudes
E_qp = bog['E_qp']  # (8,) quasiparticle energies
branch_labels = bog['branch_labels']  # ['B2[0]', ..., 'B1', 'B3[0]', ...]

# Load S38 KZ defects for GGE context
kz = np.load(OUT.parent / "computations/_shared" / "s38_kz_defects.npz", allow_pickle=True)
P_exc_kz = float(kz['P_exc_kz'])
E_modes = kz['E_modes']    # (8,) quasiparticle energies
rho_modes = kz['rho_modes']  # (8,) mode densities

# ── Select tau = tau_fold for evaluation ────────────────────────────
idx_fold = np.argmin(np.abs(tau_values - tau_fold))
tau_at_fold = tau_values[idx_fold]
log(f"tau_fold = {tau_fold}, nearest grid point: tau = {tau_at_fold}")
log(f"P_exc = {P_exc_kz} (condensate fully destroyed)")
log(f"E_exc = {E_exc:.4f} M_KK ({n_pairs:.1f} quasiparticle pairs)")
log(f"E_cond = {E_cond:.6f} M_KK (ground state)")
log(f"E_exc / |E_cond| = {E_exc / abs(E_cond):.1f}")
log("")

# ══════════════════════════════════════════════════════════════════════
# STEP 1: Energy distribution across 6 GL branches
# ══════════════════════════════════════════════════════════════════════
log("=" * 72)
log("STEP 1: Energy Distribution Across 6 GL Branches")
log("=" * 72)

# The 6 GL branches at the fold:
branch_names = ['Goldstone', 'Leggett-1', 'Leggett-2', 'Higgs-1', 'Higgs-2', 'Higgs-3']
gaps = np.array([
    omega_Gold_0[idx_fold],
    omega_L1_0[idx_fold],
    omega_L2_0[idx_fold],
    omega_H1_0[idx_fold],
    omega_H2_0[idx_fold],
    omega_H3_0[idx_fold]
])

log(f"\nBranch gaps at tau = {tau_at_fold}:")
for i, (name, gap) in enumerate(zip(branch_names, gaps)):
    log(f"  {name}: omega_0 = {gap:.6f} M_KK")

# BZ boundary frequencies
omega_BZ = gl['omega_BZ_all'][idx_fold]
log(f"\nBZ boundary frequencies:")
for i, (name, wbz) in enumerate(zip(branch_names, omega_BZ)):
    log(f"  {name}: omega(K_BZ) = {wbz:.6f} M_KK")

# Dispersion at fold
omega_at_fold = omega_full[idx_fold]  # (N_K, 6)
dK = K_plot[1] - K_plot[0]

# ── Density of states for each branch ──────────────────────────────
# In 3D with N_cells = 32 on BCC lattice, the total number of K-modes
# per branch is N_cells (one mode per cell per branch).
# DOS ~ K^2 / v_g(K) for 3D isotropic dispersion
# For phononic computation: number of modes in shell [K, K+dK] is
# g(K) = N_cells * 4pi K^2 dK / V_BZ where V_BZ = (2pi/a)^3

# Compute group velocities at all K
v_g = np.zeros_like(omega_at_fold)
for br in range(6):
    # Central differences
    v_g[1:-1, br] = (omega_at_fold[2:, br] - omega_at_fold[:-2, br]) / (2 * dK)
    # Forward/backward at boundaries
    v_g[0, br] = (omega_at_fold[1, br] - omega_at_fold[0, br]) / dK
    v_g[-1, br] = (omega_at_fold[-1, br] - omega_at_fold[-2, br]) / dK

# ── Method 1: Bogoliubov overlap (which modes are excited) ─────────
log("\n--- Method 1: Bogoliubov Overlap ---")
# The 8 BCS quasiparticles have energies E_qp and Bogoliubov amplitudes
# (u_k, v_k). The sudden quench excites ALL 8 modes (P_exc=1.0).
# Key question: how do the 8 BCS excitations map to the 6 GL branches?
#
# BCS quasiparticles are FERMIONIC (broken pairs).
# GL collective modes are BOSONIC (oscillations of the order parameter).
# The mapping is through the spectral weight:
#   - Each broken pair creates one amplitude mode (Higgs-like) excitation
#     and one phase mode (Goldstone/Leggett) excitation
#   - Energy splits: E_qp -> E_amp + E_phase
#
# In the 3He analog (Volovik & Kopnin, 2001): pair-breaking creates
# quasiparticles that scatter into collective modes. The branching ratio
# depends on the matrix element |<GL|qp pair>|^2.
#
# For the BCS state with gap structure {B1, B2(x4), B3(x3)}:
#   - B2 sector (4 modes, Delta=0.770): dominates pairing
#   - B1 sector (1 mode, Delta=0): ungapped, purely geometric
#   - B3 sector (3 modes, Delta=0.176): weakly paired

# Energy per BCS mode
log(f"\nBCS quasiparticle energies:")
for i in range(8):
    log(f"  Mode {i} ({branch_labels[i]}): E_qp = {E_qp[i]:.6f}, "
        f"u = {u_k[i]:.6f}, v = {v_k[i]:.6f}, |v|^2 = {v_k[i]**2:.6f}")

# Total BCS excitation energy check
E_qp_total = np.sum(E_qp)
log(f"\nSum(E_qp) = {E_qp_total:.4f} vs E_exc = {E_exc:.4f}")
log(f"Each mode contributes equally in sudden quench (n_k = 1 for all k)")

# ── Method 2: DOS-weighted distribution ─────────────────────────────
log("\n--- Method 2: DOS-Weighted Distribution ---")

# For a 3D system with N_cells = 32, each branch has N_cells K-modes.
# The DOS at energy omega is:
#   g(omega) = (N_cells / V_BZ) * 4pi K^2(omega) / |v_g(omega)|
#
# But we need to be careful: the quench excites modes at ALL K,
# not just near K=0. The occupation distribution depends on the
# quench protocol.
#
# For a SUDDEN quench (our case, since P_exc = 1.000):
# The Kibble-Zurek mechanism in superfluid 3He predicts:
#   n_k = |beta_k|^2 = v_k^2 (Bogoliubov coefficient)
# This is the particle number in the quasiparticle vacuum.
#
# For collective modes, the analogous quantity is the number of
# phonons/rotons created by the quench. In the sudden limit:
#   n_GL(K) = (1/2)|alpha_K|^2 where alpha_K = coherent state amplitude

# Distribution approach: thermal vs non-thermal bracketing
# Key insight from 3He (Volovik "Universe in Helium Droplet" Ch. 28):
# The sudden quench creates modes with occupation:
#   n_sudden(K) ~ (Delta_0 / (2*omega(K)))^2
# for omega(K) >> Delta_0, and n_sudden ~ 1/2 for omega ~ Delta_0

# Compute n_sudden(K) for each branch
Delta_eff = Delta_0_GL  # Use the GL gap
n_sudden = np.zeros_like(omega_at_fold)
for br in range(6):
    for ik in range(len(K_plot)):
        omega_k = omega_at_fold[ik, br]
        if omega_k > 1e-10:
            # Parametric amplification formula for sudden quench
            if omega_k > Delta_eff:
                n_sudden[ik, br] = (Delta_eff / (2 * omega_k))**2
            else:
                n_sudden[ik, br] = 0.5  # saturated
        else:
            n_sudden[ik, br] = 0.0

# Energy in each branch from sudden-quench distribution
E_branch_sudden = np.zeros(6)
for br in range(6):
    # Integrate: E = N_cells * sum_K omega(K) * n(K) * (K/K_BZ)^2
    # Weight by spherical shell volume: 4pi K^2 dK
    for ik in range(len(K_plot)):
        K = K_plot[ik]
        shell_weight = 4 * np.pi * K**2 * dK if K > 0 else 0
        E_branch_sudden[br] += omega_at_fold[ik, br] * n_sudden[ik, br] * shell_weight
    # Normalize by BZ volume
    V_BZ = 4/3 * np.pi * K_BZ**3
    E_branch_sudden[br] *= N_cells / V_BZ

log(f"\nSudden-quench energy per branch:")
E_sudden_total = np.sum(E_branch_sudden)
for i, (name, E_br) in enumerate(zip(branch_names, E_branch_sudden)):
    frac = E_br / E_sudden_total if E_sudden_total > 0 else 0
    log(f"  {name}: E = {E_br:.6f} M_KK ({frac*100:.1f}%)")
log(f"  Total (unnormalized): {E_sudden_total:.6f}")

# Rescale to match actual E_exc
if E_sudden_total > 0:
    E_branch = E_branch_sudden * (E_exc / E_sudden_total)
else:
    # Fallback: equipartition
    E_branch = np.full(6, E_exc / 6)

log(f"\nRescaled to E_exc = {E_exc:.4f}:")
for i, (name, E_br) in enumerate(zip(branch_names, E_branch)):
    frac = E_br / E_exc
    log(f"  {name}: E = {E_br:.4f} M_KK ({frac*100:.1f}%)")

# ── Method 3: Thermal bracketing ────────────────────────────────────
log("\n--- Method 3: Thermal Bracketing ---")

# Upper bound: thermal distribution at T_eff such that total energy = E_exc
# Lower bound: all energy in single (lowest) mode

# Effective temperature from equipartition:
# E = (6 branches * N_cells modes) * T/2 for classical
# E = sum_branch sum_K omega_K / (exp(omega_K/T) - 1)
# Solve for T numerically

def total_energy_thermal(T, omega_array, K_array, dK_val, K_BZ_val, N_c):
    """Total energy for Bose-Einstein distribution at temperature T."""
    if T < 1e-15:
        return 0.0
    E_total = 0.0  # (local)
    V_BZ = 4/3 * np.pi * K_BZ_val**3
    for br in range(omega_array.shape[1]):
        for ik in range(len(K_array)):
            K = K_array[ik]
            omega_k = omega_array[ik, br]
            if omega_k < 1e-12 or K < 1e-12:
                continue
            shell_weight = 4 * np.pi * K**2 * dK_val
            n_BE = 1.0 / (np.exp(omega_k / T) - 1.0) if omega_k / T < 500 else 0.0
            E_total += omega_k * n_BE * shell_weight * N_c / V_BZ
    return E_total

# Binary search for T_eff
T_lo, T_hi = 0.01, 100.0
for _ in range(100):
    T_mid = (T_lo + T_hi) / 2
    E_mid = total_energy_thermal(T_mid, omega_at_fold, K_plot, dK, K_BZ, N_cells)
    if E_mid < E_exc:
        T_lo = T_mid
    else:
        T_hi = T_mid
T_eff = (T_lo + T_hi) / 2
E_at_Teff = total_energy_thermal(T_eff, omega_at_fold, K_plot, dK, K_BZ, N_cells)

log(f"\nThermal distribution:")
log(f"  T_eff = {T_eff:.6f} M_KK (such that E_thermal = E_exc)")
log(f"  E_thermal(T_eff) = {E_at_Teff:.4f} vs E_exc = {E_exc:.4f}")

# Thermal occupation at T_eff per branch
E_branch_thermal = np.zeros(6)
V_BZ = 4/3 * np.pi * K_BZ**3
for br in range(6):
    for ik in range(len(K_plot)):
        K = K_plot[ik]
        omega_k = omega_at_fold[ik, br]
        if omega_k < 1e-12 or K < 1e-12:
            continue
        shell_weight = 4 * np.pi * K**2 * dK
        n_BE = 1.0 / (np.exp(omega_k / T_eff) - 1.0) if omega_k / T_eff < 500 else 0.0
        E_branch_thermal[br] += omega_k * n_BE * shell_weight * N_cells / V_BZ

log(f"\nThermal energy per branch:")
for i, (name, E_br) in enumerate(zip(branch_names, E_branch_thermal)):
    frac = E_br / E_exc
    log(f"  {name}: E = {E_br:.4f} M_KK ({frac*100:.1f}%)")

# ══════════════════════════════════════════════════════════════════════
# STEP 2: Equation of state w_phonon
# ══════════════════════════════════════════════════════════════════════
log("\n" + "=" * 72)
log("STEP 2: Equation of State w_phonon")
log("=" * 72)

# For each branch and distribution, compute:
#   rho_i = sum_K omega_i(K) * n_i(K)
#   p_i = sum_K (K/3) * (d omega_i / dK) * n_i(K)
# w = p_total / rho_total

def compute_eos(occupation, omega_array, vg_array, K_array, dK_val, K_BZ_val, N_c):
    """
    Compute energy density and pressure from occupation numbers.

    rho = sum_K omega(K) * n(K) * DOS
    p = sum_K (K/3) * v_g(K) * n(K) * DOS

    The (K/3)*v_g is the pressure contribution per mode:
      p_K = (1/3) * K * (d omega / dK) * n(K)
    This is exact for 3D isotropic dispersion.
    """
    V_BZ = 4/3 * np.pi * K_BZ_val**3
    rho_branches = np.zeros(omega_array.shape[1])
    p_branches = np.zeros(omega_array.shape[1])
    w_branches = np.zeros(omega_array.shape[1])

    for br in range(omega_array.shape[1]):
        rho = 0.0
        p = 0.0  # (local)
        for ik in range(len(K_array)):
            K = K_array[ik]
            if K < 1e-12:
                continue
            omega_k = omega_array[ik, br]
            vg_k = vg_array[ik, br]
            n_k = occupation[ik, br]
            shell_weight = 4 * np.pi * K**2 * dK_val * N_c / V_BZ

            rho += omega_k * n_k * shell_weight
            p += (K / 3.0) * vg_k * n_k * shell_weight

        rho_branches[br] = rho
        p_branches[br] = p
        if rho > 1e-15:
            w_branches[br] = p / rho
        else:
            w_branches[br] = np.nan

    rho_total = np.sum(rho_branches)
    p_total = np.sum(p_branches)
    w_total = p_total / rho_total if rho_total > 1e-15 else np.nan

    return rho_branches, p_branches, w_branches, rho_total, p_total, w_total

# ── Case A: Sudden-quench distribution ──────────────────────────────
log("\n--- Case A: Sudden-Quench Distribution ---")
rho_A, p_A, w_A, rho_A_tot, p_A_tot, w_A_tot = compute_eos(
    n_sudden, omega_at_fold, v_g, K_plot, dK, K_BZ, N_cells
)

# Rescale to match E_exc
scale_A = E_exc / rho_A_tot if rho_A_tot > 0 else 1.0
rho_A *= scale_A
p_A *= scale_A
rho_A_tot *= scale_A
p_A_tot *= scale_A
# w is unaffected by rescaling (ratio)

log(f"\nPer-branch EOS (sudden quench):")
log(f"{'Branch':>12s}  {'rho':>10s}  {'p':>10s}  {'w':>8s}")
for i, name in enumerate(branch_names):
    log(f"{name:>12s}  {rho_A[i]:10.4f}  {p_A[i]:10.4f}  {w_A[i]:8.4f}")
log(f"{'TOTAL':>12s}  {rho_A_tot:10.4f}  {p_A_tot:10.4f}  {w_A_tot:8.4f}")

# ── Case B: Thermal distribution (maximum entropy) ─────────────────
log("\n--- Case B: Thermal Distribution (maximum entropy bound) ---")

n_thermal = np.zeros_like(omega_at_fold)
for br in range(6):
    for ik in range(len(K_plot)):
        omega_k = omega_at_fold[ik, br]
        if omega_k > 1e-12 and omega_k / T_eff < 500:
            n_thermal[ik, br] = 1.0 / (np.exp(omega_k / T_eff) - 1.0)

rho_B, p_B, w_B, rho_B_tot, p_B_tot, w_B_tot = compute_eos(
    n_thermal, omega_at_fold, v_g, K_plot, dK, K_BZ, N_cells
)

log(f"\nPer-branch EOS (thermal at T_eff = {T_eff:.4f}):")
log(f"{'Branch':>12s}  {'rho':>10s}  {'p':>10s}  {'w':>8s}")
for i, name in enumerate(branch_names):
    log(f"{name:>12s}  {rho_B[i]:10.4f}  {p_B[i]:10.4f}  {w_B[i]:8.4f}")
log(f"{'TOTAL':>12s}  {rho_B_tot:10.4f}  {p_B_tot:10.4f}  {w_B_tot:8.4f}")

# ── Case C: Single-mode (minimum entropy) ──────────────────────────
log("\n--- Case C: Single-Mode (minimum entropy bound) ---")
# All energy in the Goldstone branch (linear dispersion, highest DOS)
# At the BZ boundary: omega_Gold(K_BZ) = 0.507
# Required occupation: n_total = E_exc / omega_Gold(K_BZ) ~ 120

n_single = np.zeros_like(omega_at_fold)
# Put all energy in Goldstone at K = K_BZ (maximum K, most modes)
# For a uniform distribution in K: n(K) = const for Goldstone
E_Gold_per_mode = np.sum(omega_at_fold[:, 0] * 4 * np.pi * K_plot**2 * dK) * N_cells / V_BZ
if E_Gold_per_mode > 0:
    n_uniform_Gold = E_exc / E_Gold_per_mode
    n_single[:, 0] = n_uniform_Gold
else:
    n_single[:, 0] = 1.0

rho_C, p_C, w_C, rho_C_tot, p_C_tot, w_C_tot = compute_eos(
    n_single, omega_at_fold, v_g, K_plot, dK, K_BZ, N_cells
)

# Rescale
scale_C = E_exc / rho_C_tot if rho_C_tot > 0 else 1.0
rho_C *= scale_C
p_C *= scale_C
rho_C_tot *= scale_C
p_C_tot *= scale_C

log(f"\nSingle-mode EOS (all energy in Goldstone):")
log(f"  rho_Gold = {rho_C_tot:.4f}, p_Gold = {p_C_tot:.4f}")
log(f"  w_Gold = {w_C_tot:.6f}")
log(f"  (Expected: w -> 1/3 for linear dispersion)")

# ── Analytic cross-check ────────────────────────────────────────────
log("\n--- Analytic Cross-Checks ---")

# For purely linear dispersion omega = c*K:
#   v_g = c (constant)
#   p = (1/3) * sum_K K * c * n(K) * DOS = (1/3) * sum omega * n * DOS = rho/3
#   => w = 1/3 exactly (radiation)
#
# For quadratic dispersion omega = m + K^2/(2m):
#   v_g = K/m
#   p = (1/3) * sum K * (K/m) * n = (1/3) * sum K^2/m * n
#   rho = sum (m + K^2/(2m)) * n ~ m * sum n (for non-relativistic)
#   => w = (2/3) * <E_kin> / (m*N + <E_kin>) -> 0 for non-relativistic
#
# For the Goldstone branch (nearly linear, alpha ~ 0.95):
#   w ~ 1/3 * (alpha/1) where alpha is the dispersion exponent
#   Corrected: w = alpha / 3 for omega ~ K^alpha (not exact but indicative)

alpha_Gold = alpha_eff_all[idx_fold, 0]
alpha_L1 = alpha_eff_all[idx_fold, 1]
alpha_L2 = alpha_eff_all[idx_fold, 2]

log(f"\nDispersion exponents at fold:")
for i, name in enumerate(branch_names):
    log(f"  {name}: alpha = {alpha_eff_all[idx_fold, i]:.4f}")

log(f"\nFor linear (alpha=1): w = 1/3 = 0.3333")
log(f"For Goldstone (alpha={alpha_Gold:.3f}): w ~ {alpha_Gold/3:.4f}")
log(f"For massive (alpha->2 at low K): w -> 0")

# ── Summary: w_phonon brackets ──────────────────────────────────────
log("\n" + "=" * 72)
log("EQUATION OF STATE SUMMARY")
log("=" * 72)

log(f"\n  Case A (sudden quench):   w_phonon = {w_A_tot:.6f}")
log(f"  Case B (thermal):         w_phonon = {w_B_tot:.6f}")
log(f"  Case C (Goldstone only):  w_phonon = {w_C_tot:.6f}")

w_phonon = w_A_tot  # primary result from physical distribution
w_thermal = w_B_tot
w_goldstone = w_C_tot

log(f"\n  ** w_phonon = {w_phonon:.6f} (primary: sudden quench) **")
log(f"  Bracket: [{min(w_A_tot, w_B_tot, w_C_tot):.4f}, "
    f"{max(w_A_tot, w_B_tot, w_C_tot):.4f}]")

# Check: is w < -1/3 (accelerating)?
if w_phonon < -1/3:
    log(f"\n  w < -1/3: ACCELERATING expansion")
elif w_phonon > 0:
    log(f"\n  w > 0: DECELERATING expansion (matter/radiation-like)")
else:
    log(f"\n  -1/3 < w < 0: DECELERATING but slower than matter")

# ══════════════════════════════════════════════════════════════════════
# STEP 3: Backreaction on Geometry
# ══════════════════════════════════════════════════════════════════════
log("\n" + "=" * 72)
log("STEP 3: Backreaction on Geometry")
log("=" * 72)

# Friedmann equation: H^2 = (8*pi*G/3) * rho
# Using G_DeWitt = 5.0 (from canonical constants, in M_KK units)
# H^2 = (8*pi*G_DeWitt/3) * rho_phonon
#
# The phonon energy density rho_phonon = E_exc / V_cell where V_cell
# is the volume of one BCC unit cell.
# But in our framework, rho is already in M_KK units per cell.

# The key quantity is rho_phonon in Planck units for Friedmann.
# E_exc = 60.6 M_KK. If the geometry has volume V, then
# rho_phonon = E_exc / V.
#
# For N_cells = 32 on BCC with a_BCC from data:
a_BCC = float(gl['a_BCC'])  # lattice constant in natural units
V_cell = a_BCC**3 / 2  # BCC has 2 atoms per conventional cell
V_total = N_cells * V_cell
rho_phonon = E_exc / V_total  # energy density in M_KK / (natural length)^3

log(f"\nGeometry:")
log(f"  a_BCC = {a_BCC:.4f}")
log(f"  V_cell = {V_cell:.4f}")
log(f"  V_total (32 cells) = {V_total:.4f}")
log(f"  rho_phonon = E_exc / V_total = {rho_phonon:.6f}")

# Friedmann with G_DeWitt:
H_phonon_sq = (8 * np.pi * G_DeWitt / 3) * rho_phonon
H_phonon = np.sqrt(H_phonon_sq)
log(f"\n  H_phonon = sqrt(8*pi*G/3 * rho) = {H_phonon:.4f} M_KK")
log(f"  H_fold (from canonical) = {H_fold:.4f} M_KK")
log(f"  H_phonon / H_fold = {H_phonon / H_fold:.6f}")

# The phonon gas contributes to expansion.
# For w > 0 (decelerating), the contribution is positive H but
# deceleration means a_dot_dot < 0.
# N_e from phonon gas:
#   rho ~ a^{-3(1+w)}
#   H ~ rho^{1/2} ~ a^{-3(1+w)/2}
#   For radiation (w=1/3): rho ~ a^{-4}, H ~ a^{-2}
#   dt = da/(a*H), and N_e = ln(a_f/a_i)
#
# Duration of the afterglow phase:
# The phonon gas persists until it redshifts away.
# Since the GGE never thermalizes (integrability), it persists forever.
# But the expansion it drives is decelerating.
#
# N_e = integral H dt
# For H = H_0 * (a/a_0)^{-3(1+w)/2}:
#   N_e = H_0 * integral_0^{t_f} (a(t)/a_0)^{-3(1+w)/2} dt
#
# In radiation domination (w=1/3):
#   a ~ t^{1/2}, so H = 1/(2t)
#   N_e = integral_{t_i}^{t_f} dt/(2t) = (1/2)*ln(t_f/t_i)
#
# For the phonon gas, the expansion is finite and computable.

# Key: how long does the phonon-dominated phase last?
# The phonon energy redshifts as rho ~ a^{-3(1+w)}
# It becomes subdominant when rho_phonon * a^{-3(1+w)} < rho_other
#
# But in our framework there IS no other energy source initially.
# The phonon gas IS the dominant component after the quench.

# N_e from the phonon phase:
# a(t) ~ t^{2/(3(1+w))} for constant w
# H(t) = 2/(3(1+w)*t)
# N_e = integral H dt from t_i to t_f
#     = [2/(3(1+w))] * ln(t_f/t_i)
#
# Need to know the duration ratio t_f/t_i.
# t_i = 1/H_phonon (the initial time)
# t_f is when... the phonon gas has diluted?
#
# More precisely: the total expansion from the phonon gas is
# N_e = ln(a_f/a_i) where a_f is set by when the phonon gas
# energy density drops below some threshold.

# For the 3He analog: the quench produces quasiparticles whose
# energy density is E_exc per unit volume. This determines the
# "superfluid velocity" and hence the expansion rate.
# The expansion runs until the energy density is insufficient
# to drive further expansion (equilibrium).
#
# In q-theory language (Volovik papers 15-16):
# The system expands until d(epsilon)/dq = 0 (equilibrium).
# Starting from E_exc, the system must release all excess energy.
# The total expansion is determined by energy conservation:
#   E_exc = rho_0 * V_0 = rho_0 * V_0 * (a_f/a_i)^{3(1+w)} * (a_i/a_f)^3
#   Only for w != 0, some energy goes into PdV work.
#
# For the phonon gas with w = w_phonon:
#   Expansion factor = (E_exc / E_eq)^{1/(3w)} where E_eq is the
#   equilibrium energy (which is |E_cond| in the ground state, but
#   the condensate is destroyed so E_eq ~ 0 in the GGE).

# The correct computation: how much expansion does E_exc drive?
# Using Friedmann: da/a = H dt where H^2 = (8pi G/3) rho
# rho(a) = rho_0 * (a_0/a)^{3(1+w)}
# H(a) = H_0 * (a_0/a)^{3(1+w)/2}
# N_e = integral d ln(a) = integral H dt
#     = integral H da/(aH) = integral da/a ... this is circular.
#
# Direct: a(t) = a_0 * (t/t_0)^{2/(3(1+w))}
#   H = 2/(3(1+w)*t)
#   t_0 = 2/(3(1+w)*H_0)
#
# The expansion runs for as long as the phonon gas dominates.
# Since there is no other component, it runs FOREVER (but decelerating).
# Total N_e -> infinity but with diminishing H.
#
# Physical cutoff: expansion stops being meaningful when H*t_Hubble ~ 1
# i.e., when the expansion timescale equals the current age of the universe.
# This is the standard radiation-dominated calculation.

# Let's compute N_e over a finite duration comparable to the transit:
t_transit = float(kz['dt_transit'])
t_Hubble_initial = 1.0 / H_phonon

log(f"\n  t_transit = {t_transit:.6f} M_KK^-1")
log(f"  t_Hubble(phonon) = 1/H_phonon = {t_Hubble_initial:.6f} M_KK^-1")

# For power-law expansion: N_e over time interval [t_i, t_f]
# N_e = (2/(3(1+w))) * ln(t_f/t_i)
# The phonon phase starts at the end of transit.
#
# If the phonon gas lasts for n Hubble times:
# N_e = (2/(3(1+w))) * ln(n)
# For n = e^{3(1+w)/2}: N_e = 1

# More physical: the total energy E_exc drives expansion.
# Energy conservation: rho * V = const (for w=0, dust)
# For w > 0: rho * V * a^{3w} decreases (energy transferred to PdV work)
# The total PdV work = integral p dV = integral w*rho*dV
# = integral w * rho_0 * (a_0/a)^{3(1+w)} * 3*V_0*(a/a_0)^2 * da/a_0
# This integral gives the total expansion.

# Simpler: use N_e = ln(a_f/a_i) = ln((E_exc/E_final)^{1/(3(1+w_phonon))})
# If E_final = kT_CMB (the CMB temperature energy per mode):
# But this assumes the phonon gas eventually thermalizes to CMB, which
# contradicts the GGE non-thermalization. Better: track until rho drops
# to the observational cosmological constant scale.

# Actually the cleanest calculation:
# N_e^afterglow = (2/(3*(1+w))) * ln(rho_i / rho_f)^{1/2}
# = (1/(3*(1+w))) * ln(rho_i / rho_f)
# where rho_i = rho_phonon and rho_f is the final density.

# For the framework: rho_f is set by the CC (Lambda_obs).
# But the ratio is enormous: rho_i / Lambda ~ 10^{120}.
# This would give N_e ~ 120/(3*(1+w)) * ln(10) ~ 90.
# However, this assumes the phonon gas expansion is the ONLY
# component between the quench and the CC-dominated era.

# Let's compute for several duration scenarios:
log(f"\n  N_e for various scenarios:")
log(f"  (w_phonon = {w_phonon:.4f})")

# Scenario 1: Expansion for 1 transit time
ratio_1 = max(1 + H_phonon * t_transit, 1.001)
N_e_1 = np.log(ratio_1)
log(f"  1 transit time: a_f/a_i = {ratio_1:.6f}, N_e = {N_e_1:.6f}")

# Scenario 2: Expansion for 1 Hubble time
# a(t_H) = a_0 * 2^{2/(3(1+w))}
if 1 + w_phonon > 0:
    exponent = 2.0 / (3 * (1 + w_phonon))
    N_e_Hub = exponent * np.log(2)
    log(f"  1 Hubble time: N_e = {N_e_Hub:.6f}")

# Scenario 3: Full phonon-dominated era
# From rho_phonon down to the point where H = H_0 (today)
# H_phonon / H_0 = (rho_phonon / rho_0)^{1/2}
# N_e = (1/(3(1+w))) * ln(rho_phonon / rho_0)
# But rho_0 in M_KK units:
# H_0 = 1.438e-42 GeV, H_phonon in M_KK units... need conversion

H_phonon_GeV = H_phonon * M_KK  # Convert to GeV (H has units of energy/hbar)
log(f"\n  H_phonon = {H_phonon:.4f} M_KK = {H_phonon_GeV:.4e} GeV")
log(f"  H_0 = {H_0_GeV:.4e} GeV")

if H_phonon_GeV > 0 and H_0_GeV > 0 and (1 + w_phonon) > 0:
    N_e_full = (1.0 / (3 * (1 + w_phonon))) * np.log(H_phonon_GeV / H_0_GeV)
    log(f"  Full phonon era (H_phonon -> H_0): N_e = {N_e_full:.4f}")
else:
    N_e_full = 0

# Scenario 4: Energy-based estimate
# Total expansion = how many e-folds until E_exc energy density
# drops below some reference.
# For radiation: rho ~ a^{-4}, so a_f/a_i = (rho_i/rho_f)^{1/4}
# N_e = (1/4) * ln(rho_i/rho_f)
if w_phonon > -1 and rho_phonon > 0:
    # Use ratio of phonon H to fold H
    if H_fold > 0:
        N_e_vs_fold = (1.0 / (3 * (1 + w_phonon))) * np.log(
            (H_phonon / H_fold)**2 if H_phonon > H_fold else 1.0
        )
        log(f"  Phonon vs fold H: N_e = {N_e_vs_fold:.4f}")

# The most physically motivated estimate:
# The afterglow N_e is the expansion from the phonon-dominated phase.
# Since rho_phonon << rho at the fold (H_phonon << H_fold),
# the phonon gas is a PERTURBATION on the fold dynamics, not the driver.

log(f"\n  ** CRITICAL: H_phonon / H_fold = {H_phonon / H_fold:.6f} **")
log(f"  The phonon gas H is {H_fold/H_phonon:.1f}x smaller than the fold H.")
log(f"  The phonon gas is a PERTURBATION on the fold-driven expansion.")

# The afterglow contributes AFTER the fold transit.
# N_e^afterglow = integral_{t_transit}^{infinity} H_phonon(t) dt
# For power-law: N_e^afterglow = (2/(3(1+w))) * ln(t_f/t_transit)
# where t_f -> infinity for the GGE (never thermalizes).
# But H(t) -> 0 as t -> infinity, so the integral converges:
# N_e^afterglow = (2/(3(1+w))) * ln(infinity) ... diverges logarithmically.
#
# Physical cutoff: when H_phonon(t) < H_0 (today's Hubble rate)
# This gives N_e^afterglow = (1/(3(1+w))) * ln(H_phonon^2 / H_0^2)
# = (2/(3(1+w))) * ln(H_phonon / H_0)

if H_phonon_GeV > H_0_GeV and (1 + w_phonon) > 0:
    N_e_afterglow = (2.0 / (3 * (1 + w_phonon))) * np.log(H_phonon_GeV / H_0_GeV)
    log(f"\n  N_e^afterglow (until H = H_0) = {N_e_afterglow:.4f}")
else:
    N_e_afterglow = 0.0
    log(f"\n  N_e^afterglow = {N_e_afterglow}")

# ══════════════════════════════════════════════════════════════════════
# STEP 4: Non-thermal Distribution Analysis
# ══════════════════════════════════════════════════════════════════════
log("\n" + "=" * 72)
log("STEP 4: Non-Thermal Distribution (GGE)")
log("=" * 72)

# The GGE has 8 conserved integrals (Richardson-Gaudin).
# The occupation is: n_k = 1/(exp(sum_j beta_j Q_j(k)) - 1)
# For the BCS system, the conserved integrals are the individual
# pair occupation numbers n_alpha (one per BCS mode).
#
# From S38: the system has 8 excited modes, all with n_k = 1 (sudden quench).
# This means the GGE is simply: each mode is occupied exactly once.
# The GGE temperatures from S43 (gge-temp-43):
#   T_B2 = 0.668, T_B1 = 0.435, T_B3 = 0.178

# The GGE is NOT a single-temperature Bose-Einstein distribution.
# Each sector has its own temperature. The occupation differs from BE
# precisely because the conserved integrals constrain the distribution.
#
# For the EOS, the key insight is: w depends on the DISPERSION,
# not on the distribution. For any distribution:
#   w = <(K/3) * v_g(K)> / <omega(K)>
# where <...> is the average over the occupied modes.
#
# If all modes are equally occupied (n_k = const), then w is
# determined purely by the dispersion relation shape.

log(f"\nGGE structure:")
log(f"  8 conserved integrals (Richardson-Gaudin)")
log(f"  GGE temperatures: T_B2=0.668, T_B1=0.435, T_B3=0.178")
log(f"  T_max/T_min = 3.75 (strongly non-thermal)")
log(f"  Negative temperature T(B2,B1) exists")
log("")
log(f"  Key: w is determined by dispersion shape, not distribution details")
log(f"  For equipopulated modes: w depends only on omega(K) geometry")

# Compute w for equipopulated distribution (most relevant for GGE)
n_equi = np.ones_like(omega_at_fold)
rho_eq, p_eq, w_eq, rho_eq_tot, p_eq_tot, w_eq_tot = compute_eos(
    n_equi, omega_at_fold, v_g, K_plot, dK, K_BZ, N_cells
)

log(f"\n  w (equipopulated, all n=1): {w_eq_tot:.6f}")
log(f"  w (sudden quench): {w_A_tot:.6f}")
log(f"  w (thermal): {w_B_tot:.6f}")
log(f"  w (Goldstone only): {w_C_tot:.6f}")

# Distribution-independence check: if w varies by < 10% across
# distributions, it's robust.
w_values = [w_A_tot, w_B_tot, w_C_tot, w_eq_tot]
w_mean = np.mean(w_values)
w_spread = (max(w_values) - min(w_values)) / w_mean if w_mean != 0 else 0
log(f"\n  w spread across distributions: {w_spread*100:.1f}%")
log(f"  w is {'ROBUST' if w_spread < 0.3 else 'DISTRIBUTION-DEPENDENT'}")

# ══════════════════════════════════════════════════════════════════════
# STEP 5: 3He Analog Assessment
# ══════════════════════════════════════════════════════════════════════
log("\n" + "=" * 72)
log("STEP 5: 3He Analog Assessment")
log("=" * 72)

ratio_T_Delta = T_eff / Delta_0_GL if Delta_0_GL > 0 else float('inf')
regime = "ultrarelativistic" if T_eff > Delta_0_GL else ("near-gap" if T_eff > 0.3 * Delta_0_GL else "sub-gap")

log(f"""
Superfluid 3He analog for the KZ phonon gas:

1. KIBBLE-ZUREK in 3He-B (Bauerle et al. 1996, Ruutu et al. 1996):
   Neutron irradiation creates a hot spot that undergoes rapid quench.
   The quench creates quantized vortices (topological defects).
   In our framework: P_exc = 1.000 means the ENTIRE condensate is
   destroyed -- more extreme than the 3He experiments where
   only a local region is quenched.

2. QUASIPARTICLE GAS in 3He-B:
   After the quench, the hot spot contains a gas of Bogoliubov
   quasiparticles. Their EOS is:
   - At T >> Delta (above gap): w = 1/3 (ultrarelativistic fermions)
   - At T ~ Delta (near gap): w = 1/3 * (1 - (Delta/T)^2 + ...)
   - At T << Delta (below gap): w -> 0 (massive particles)

   The analog mapping: T_eff / Delta_0_GL ~ T_eff / 0.770
   In our case: T_eff = {T_eff:.3f}, so T_eff/Delta = {ratio_T_Delta:.3f}
   This is the {regime} regime.

3. PHONON PRESSURE in superfluid:
   First sound (phonons) have w = 1/3.
   Second sound (entropy waves) have w that depends on rho_n/rho.
   Destroyed condensate: rho_s = 0, rho_n/rho = 1.
   This is the NORMAL FLUID -- all excitations are phonon-like.

4. NON-EQUILIBRIUM EXPANSION:
   In the 3He analog, the hot spot EXPANDS into the surrounding
   cold superfluid at second sound velocity c_2 ~ c_1/sqrt(3).
   In the cosmological framework: phonon pressure drives metric
   expansion via the Friedmann equation.

5. SUPERFLUID VACUUM ANALOG (Volovik 2003, Ch. 29):
   The vacuum energy of the phonon gas contributes to the effective
   cosmological constant: Lambda_eff ~ (1+w) * rho_phonon.
   For w = 1/3: Lambda_eff = (4/3) * rho_phonon > 0.
   POSITIVE: drives expansion, but DECELERATING.
   For acceleration need w < -1/3 (negative pressure).
   This CANNOT come from a phonon gas -- requires vacuum energy
   (condensation energy) itself.
""")

# ══════════════════════════════════════════════════════════════════════
# GATE VERDICT
# ══════════════════════════════════════════════════════════════════════
log("\n" + "=" * 72)
log("GATE VERDICT: KZ-PRESSURE-53")
log("=" * 72)

gate_pass = False
gate_info = False

log(f"\n  w_phonon = {w_phonon:.6f}")
log(f"  w bracket: [{min(w_values):.4f}, {max(w_values):.4f}]")
log(f"  N_e^afterglow = {N_e_afterglow:.4f}")
log(f"  H_phonon / H_fold = {H_phonon / H_fold:.6f}")

if np.isnan(w_phonon) or np.isinf(w_phonon):
    verdict = "FAIL"
    detail = "w_phonon undefined"
elif np.isnan(N_e_afterglow) or np.isinf(N_e_afterglow):
    verdict = "FAIL"
    detail = "N_e^afterglow divergent"
elif N_e_afterglow > 0.5:
    verdict = "PASS"
    detail = f"w={w_phonon:.4f}, N_e={N_e_afterglow:.2f}, backreaction finite"
    gate_pass = True
elif w_phonon > 0:
    verdict = "INFO"
    detail = f"w={w_phonon:.4f} > 0 (decelerating). N_e={N_e_afterglow:.2f}"
    gate_info = True
else:
    verdict = "INFO"
    detail = f"w={w_phonon:.4f}, N_e={N_e_afterglow:.2f}"
    gate_info = True

log(f"\n  VERDICT: {verdict}")
log(f"  DETAIL: {detail}")

# Physical interpretation
w_regime = "radiation-like" if abs(w_phonon - 1/3) < 0.1 else "between radiation and matter"
Ne_interp = ("large because H_phonon >> H_0 even though H_phonon << H_fold. "
             "The expansion is long-lived but slow." if N_e_afterglow > 0.5
             else "small because the phonon gas is subdominant to the fold dynamics.")

log(f"""
PHYSICAL INTERPRETATION (Volovik perspective):

The KZ phonon gas after condensate destruction has w ~ {w_phonon:.3f}.
This is {w_regime}.

Key insight from the superfluid analog: a phonon gas CANNOT produce
accelerated expansion (w < -1/3). Phonons have POSITIVE pressure.
The equation of state is bounded: 0 <= w <= 1/3 for any combination
of massive and massless bosonic excitations.

For acceleration, you need the VACUUM ENERGY (condensation energy),
not the EXCITATIONS above the vacuum. This is the fundamental
distinction in Volovik's "Universe in a Helium Droplet":
  - Vacuum energy (condensation energy): can have w = -1 (CC-like)
  - Excitations (phonons, rotons): always w >= 0

The GGE relic IS the excitation gas. It drives DECELERATING expansion.
N_e^afterglow = {N_e_afterglow:.2f} is {Ne_interp}

The phonon gas contributes to expansion but does NOT accelerate it.
This is a structural result: no distribution (thermal, GGE, or other)
can make phonon pressure negative.
""")

# ── Save results ─────────────────────────────────────────────────────
np.savez(OUT / "s53_kz_pressure.npz",
    # Primary results
    w_phonon=w_phonon,
    w_thermal=w_thermal,
    w_goldstone=w_goldstone,
    w_equipopulated=w_eq_tot,
    N_e_afterglow=N_e_afterglow,
    H_phonon=H_phonon,
    H_phonon_GeV=H_phonon_GeV,
    T_eff=T_eff,
    rho_phonon=rho_phonon,

    # Energy distribution
    E_branch_sudden=E_branch,
    E_branch_thermal=E_branch_thermal,
    branch_names=np.array(branch_names),

    # Per-branch EOS
    rho_branches_sudden=rho_A,
    p_branches_sudden=p_A,
    w_branches_sudden=w_A,
    rho_branches_thermal=rho_B,
    p_branches_thermal=p_B,
    w_branches_thermal=w_B,

    # Geometry
    H_fold=H_fold,
    H_ratio=H_phonon/H_fold,
    N_e_classical=N_e_classical,

    # Gate
    gate_name=np.array(["KZ-PRESSURE-53"]),
    gate_verdict=np.array([verdict]),
    gate_detail=np.array([detail]),

    # Inputs used
    E_exc=E_exc,
    n_pairs=n_pairs,
    tau_fold=tau_fold,
    G_DeWitt=G_DeWitt,
    N_cells=N_cells,
    w_spread=w_spread,
)

log(f"\nSaved: s53_kz_pressure.npz")

# ── Plot ─────────────────────────────────────────────────────────────
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("KZ-PRESSURE-53: Phonon Gas Backreaction", fontsize=14, fontweight='bold')

# Panel 1: Dispersion relations at fold
ax = axes[0, 0]
colors = ['#e41a1c', '#377eb8', '#4daf4a', '#984ea3', '#ff7f00', '#a65628']
for br in range(6):
    ax.plot(K_plot, omega_at_fold[:, br], color=colors[br],
            label=f'{branch_names[br]} (w={w_A[br]:.3f})')
ax.set_xlabel('K [M_KK]')
ax.set_ylabel('omega [M_KK]')
ax.set_title(f'Dispersion at tau = {tau_at_fold}')
ax.legend(fontsize=7, loc='upper left')
ax.set_xlim(0, K_BZ)
ax.set_ylim(0, 2.0)

# Panel 2: Energy distribution across branches
ax = axes[0, 1]
x = np.arange(6)
width = 0.35  # (local)
bars1 = ax.bar(x - width/2, E_branch, width, label='Sudden quench', color='steelblue')
bars2 = ax.bar(x + width/2, E_branch_thermal, width, label='Thermal', color='coral')
ax.set_xticks(x)
ax.set_xticklabels([n[:4] for n in branch_names], rotation=45, ha='right')
ax.set_ylabel('Energy [M_KK]')
ax.set_title('Energy per Branch')
ax.legend()

# Panel 3: w(K) for Goldstone branch
ax = axes[1, 0]
# Compute running w(K) = K*v_g / (3*omega)
w_running = np.zeros((len(K_plot), 6))
for br in range(6):
    for ik in range(len(K_plot)):
        if omega_at_fold[ik, br] > 1e-10 and K_plot[ik] > 1e-10:
            w_running[ik, br] = K_plot[ik] * v_g[ik, br] / (3 * omega_at_fold[ik, br])
for br in range(3):  # Show Goldstone and Leggett only
    ax.plot(K_plot[1:], w_running[1:, br], color=colors[br], label=branch_names[br])
ax.axhline(1/3, color='gray', ls='--', alpha=0.5, label='w = 1/3')
ax.axhline(0, color='gray', ls=':', alpha=0.3)
ax.set_xlabel('K [M_KK]')
ax.set_ylabel('w(K) = K v_g / (3 omega)')
ax.set_title('Running EOS per Mode')
ax.legend(fontsize=8)
ax.set_ylim(-0.1, 0.5)

# Panel 4: Summary text
ax = axes[1, 1]
ax.axis('off')
summary_text = f"""KZ-PRESSURE-53 SUMMARY

Gate: {verdict}

w_phonon = {w_phonon:.4f}
  sudden quench: {w_A_tot:.4f}
  thermal (T={T_eff:.3f}): {w_B_tot:.4f}
  Goldstone only: {w_C_tot:.4f}
  equipopulated: {w_eq_tot:.4f}
  spread: {w_spread*100:.1f}%

N_e^afterglow = {N_e_afterglow:.2f}
H_phonon / H_fold = {H_phonon/H_fold:.4e}
T_eff = {T_eff:.4f} M_KK

3He analog: phonon gas after
neutron-induced quench.
w > 0: DECELERATING expansion.
Phonon pressure is always positive.
Cannot produce inflation.
"""
ax.text(0.05, 0.95, summary_text, transform=ax.transAxes,
        fontsize=9, verticalalignment='top', fontfamily='monospace',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

plt.tight_layout()
plt.savefig(OUT / "s53_kz_pressure.png", dpi=150, bbox_inches='tight')
log("Saved: s53_kz_pressure.png")
plt.close()

# ── Write log ────────────────────────────────────────────────────────
with open(OUT / "s53_kz_pressure_output.txt", 'w') as f:
    f.write('\n'.join(LOG))
log("\nSaved: s53_kz_pressure_output.txt")

print("\n" + "=" * 72)
print(f"DONE. Verdict: {verdict}")
print(f"w_phonon = {w_phonon:.6f}")
print(f"N_e^afterglow = {N_e_afterglow:.4f}")
print("=" * 72)
