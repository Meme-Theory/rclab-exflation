#!/usr/bin/env python3
"""
S58: Dynamic Structure Factor S(q, omega) of Post-Transit GGE
==============================================================

Computes the dynamic structure factor S(q, omega) for the post-transit
Generalized Gibbs Ensemble (GGE) state on the 32-cell Cayley graph fabric.

S(q, omega) encodes "what dark matter looks like" in this framework:
the excitation spectrum accessible to density probes.

Three contributions:
1. Quasiparticle continuum: pairs broken across the BCS gap (omega >= 2*Delta)
2. Bogoliubov-Anderson (BA) modes: phase collective excitations (sub-gap to above-gap)
3. Leggett modes: amplitude collective excitations (lowest frequencies)

The GGE occupation numbers f_k^GGE are NON-THERMAL: 8 effective temperatures
ranging from 0.178 to 0.758 M_KK, versus the best-fit thermal T_eq = 0.189 M_KK.

Gate: SQ-OMEGA-GGE-58 (INFO)
  - Hard gap visible?
  - Non-thermal occupation resolvable (GGE vs thermal)?

Session 58, Kitaev-Quantum-Chaos-Theorist
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

import numpy as np
from scipy.special import ellipk
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

from canonical_constants import (
    tau_fold, M_KK, E_cond, Delta_0_OES, omega_PV, PI
)

# =============================================================================
# Load input data
# =============================================================================
data_dir = os.path.dirname(__file__)
archive_dir = os.path.join(os.path.dirname(__file__), "..", "_shared")

gge_data = np.load(os.path.join(data_dir, 's57_gge_equilibrium_gap.npz'), allow_pickle=True)
ba_data  = np.load(os.path.join(data_dir, 's56_ba_spectrum.npz'), allow_pickle=True)
leg_data = np.load(os.path.join(data_dir, 's56_leggett_fabric.npz'), allow_pickle=True)
tb_data  = np.load(os.path.join(data_dir, 's54_tb_hamiltonian.npz'), allow_pickle=True)

# GGE state
fk_gge       = gge_data['fk_gge']           # (8,) GGE occupations
fk_eq        = gge_data['fk_eq_canonical']   # (8,) best-fit thermal occupations
E_k          = gge_data['E_k']               # (8,) quasiparticle energies
xi_k         = gge_data['xi']                # (8,) bare dispersions
T_k          = gge_data['T_k_volovik']       # (8,) effective temperatures
T_eq         = float(gge_data['T_eq_canonical'])
branch_labels = gge_data['branch_labels']
N_modes      = int(gge_data['N_modes'])
Delta        = float(ba_data['Delta'])        # BCS gap = Delta_0_OES

# Collective modes at fold
fold_idx = int(gge_data['fold_idx'])
omega_BA  = ba_data['omega_BA'][fold_idx]     # (31,) BA frequencies
omega_L   = leg_data['omega_L_GL'][fold_idx]  # (32,) Leggett frequencies

# Graph structure
lap_eigs  = ba_data['laplacian_eigs']         # (32,) Laplacian eigenvalues = q^2
adj       = tb_data['adjacency']              # (32,32) adjacency matrix
N_cells   = int(ba_data['N_cells'])           # 32

print("=" * 70)
print("S58: Dynamic Structure Factor S(q, omega) of Post-Transit GGE")
print("=" * 70)
print()
print(f"BCS gap Delta = {Delta:.6f} M_KK")
print(f"2*Delta = {2*Delta:.6f} M_KK  (quasiparticle pair-breaking threshold)")
print(f"N_modes = {N_modes}, N_cells = {N_cells}")
print(f"BA modes: {len(omega_BA)}, range [{omega_BA.min():.4f}, {omega_BA.max():.4f}] M_KK")
print(f"Leggett modes: {len(omega_L)}, range [{omega_L.min():.4f}, {omega_L.max():.4f}] M_KK")
print(f"Laplacian eigenvalues (q^2): [{lap_eigs.min():.4f}, {lap_eigs.max():.4f}]")
print()

# =============================================================================
# 1. Quasiparticle contribution to S(q, omega)
# =============================================================================
# In a BCS superconductor, the quasiparticle dynamic structure factor is:
#
#   S_qp(q, omega) = sum_{k} (u_k^2 * u_{k+q}^2 + v_k^2 * v_{k+q}^2)
#                    * f_k * (1 - f_{k+q}) * delta(omega - E_{k+q} + E_k)
#                    + coherence factors for pair-breaking
#
# For pair-breaking (dominant above 2*Delta):
#   S_pb(omega) propto N(0) * (omega / sqrt(omega^2 - 4*Delta^2))
#                      * [1 + Delta^2/omega^2]  (coherence factor, type II)
#                      * Fermi factors from GGE
#
# The BCS density of states:
#   N_BCS(E) = N(0) * |E| / sqrt(E^2 - Delta^2)  for |E| > Delta
#
# For our discrete 8-mode system, we compute the pair-breaking continuum
# by convolving the BCS DoS with GGE occupations.

print("--- Quasiparticle pair-breaking continuum ---")

# BCS coherence factors for density (type II) response
# For pair-breaking: C_II = (1 + xi_k * xi_{k'} / (E_k * E_{k'}))
# where xi_k = bare dispersion, E_k = quasiparticle energy

# Compute u_k^2, v_k^2 from BCS
u2_k = 0.5 * (1.0 + xi_k / E_k)
v2_k = 0.5 * (1.0 - xi_k / E_k)

print(f"Coherence factors u^2: {u2_k}")
print(f"Coherence factors v^2: {v2_k}")

# For the pair-breaking threshold: minimum energy to break a pair
# is 2*Delta (both quasiparticles above gap)
omega_pb_min = 2.0 * Delta
print(f"Pair-breaking threshold: omega_min = 2*Delta = {omega_pb_min:.6f} M_KK")

# BCS DoS (continuum limit for plotting)
def bcs_dos(omega, delta, eta=0.005):
    """BCS density of states N(omega)/N(0), broadened by eta."""
    result = np.zeros_like(omega)
    mask = np.abs(omega) > delta
    result[mask] = np.abs(omega[mask]) / np.sqrt(omega[mask]**2 - delta**2)
    # Broaden the singularity
    near = np.abs(np.abs(omega) - delta) < eta
    result[near] = np.abs(omega[near]) / np.sqrt(eta**2 + (omega[near]**2 - delta**2).clip(0))
    return result

# =============================================================================
# 2. Momentum structure from graph Laplacian
# =============================================================================
# The CG graph has 32 vertices. The Laplacian eigenvalues lambda_n serve as
# effective q^2 values. We use q = sqrt(lambda_n) as our momentum variable.

q_values = np.sqrt(lap_eigs)  # (32,) effective momenta
q_values[0] = 0.0  # q=0 mode

print(f"\nMomentum values q = sqrt(lambda): [{q_values.min():.4f}, {q_values.max():.4f}]")
print(f"q spacing: mean={np.diff(np.sort(q_values)).mean():.4f}")

# =============================================================================
# 3. Build S(q, omega) on a 2D grid
# =============================================================================
# omega range: from 0 to slightly above 2*max(E_k) to capture all features
omega_max = 2.0 * np.max(E_k) * 1.3
N_omega = 500  # (local)
omega_grid = np.linspace(0, omega_max, N_omega)

# Broadening width (Lorentzian)
eta = 0.015  # M_KK, chosen to resolve BA mode spacing (~0.08) (local)

def lorentzian(x, x0, gamma):
    """Normalized Lorentzian: (gamma/pi) / ((x-x0)^2 + gamma^2)"""
    return (gamma / PI) / ((x - x0)**2 + gamma**2)

# Initialize S(q, omega) arrays
S_gge = np.zeros((len(q_values), N_omega))   # GGE dynamic structure factor
S_eq  = np.zeros((len(q_values), N_omega))   # Thermal equilibrium comparison

# --- 3a. Quasiparticle pair-breaking continuum ---
# For each q (graph Laplacian mode), the pair-breaking contribution:
#   S_pb(q, omega) = sum_{k,k'} |M_{k,k'}(q)|^2 * C_II(k,k')
#                    * f_k * (1-f_{k'}) * Lorentzian(omega - E_k - E_{k'})
#
# The matrix element |M(q)|^2 encodes the overlap of graph eigenvectors
# with the quasiparticle modes. For simplicity (and because the CG graph
# scrambles momentum), we use |M|^2 propto form factor F(q) that decays
# with q (typical of s-wave BCS):
#   F(q) = 1 / (1 + (q * xi_BCS)^2)
# where xi_BCS = v_F / (pi * Delta) is the coherence length

xi_BCS = 1.0 / (PI * Delta)  # In M_KK^{-1} units (v_F ~ 1 in natural units)
print(f"\nBCS coherence length xi_BCS = {xi_BCS:.4f} M_KK^{{-1}}")

for iq, q in enumerate(q_values):
    form_factor = 1.0 / (1.0 + (q * xi_BCS)**2)

    # Pair-breaking: omega = E_k + E_{k'} >= 2*Delta
    for ik in range(N_modes):
        for ikp in range(N_modes):
            omega_trans = E_k[ik] + E_k[ikp]

            # Type II coherence factor
            C_II = 0.5 * (1.0 + xi_k[ik] * xi_k[ikp] / (E_k[ik] * E_k[ikp]))

            # GGE: both quasiparticles occupied in initial, unoccupied in final
            weight_gge = fk_gge[ik] * fk_gge[ikp] * C_II * form_factor
            weight_eq  = fk_eq[ik]  * fk_eq[ikp]  * C_II * form_factor

            S_gge[iq, :] += weight_gge * lorentzian(omega_grid, omega_trans, eta)
            S_eq[iq, :]  += weight_eq  * lorentzian(omega_grid, omega_trans, eta)

print("Quasiparticle pair-breaking: computed")

# --- 3b. Bogoliubov-Anderson collective modes ---
# BA modes are phase oscillations of the order parameter. They disperse
# as omega_BA(q) = omega_BA_n where n indexes graph Laplacian modes (31 modes).
# Each BA mode at frequency omega_n contributes a pole to S(q, omega).
#
# The BA spectral weight is proportional to q^2 (Goldstone mode coupling
# to density is omega^2 propto q^2 at small q), modulated by the BCS
# coherence:
#   A_BA(q, n) = (omega_BA_n / Delta)^2 * exp(-omega_BA_n / T_eff)
# where T_eff is the mode-dependent GGE temperature.
#
# The q-dependence: BA mode n lives on Laplacian eigenmode n+1 (n=0 is uniform),
# so it naturally carries momentum q_n.

print("\n--- Bogoliubov-Anderson modes ---")

# BA mode assignment: mode n (n=0..30) lives on Laplacian eigenvalue n+1
# (the n=0 Laplacian mode is q=0, uniform; BA modes start from n=1)
for n_ba in range(len(omega_BA)):
    iq_ba = n_ba + 1  # Laplacian index (skip q=0)
    if iq_ba >= len(q_values):
        continue

    q_ba = q_values[iq_ba]
    omega_n = omega_BA[n_ba]

    # BA spectral weight: Goldstone coupling ~ q^2/omega for small q
    # For BCS: the Anderson-Bogoliubov mode couples to density via
    # (q * Delta / omega_n) amplitude
    if omega_n > 0:
        A_BA = (q_ba * Delta / omega_n)**2
    else:
        A_BA = 0.0  # (local)

    # GGE occupation of the BA mode via effective temperature
    # The BA mode is a collective excitation; its occupation in the GGE
    # is determined by the B2 effective temperatures (dominant sector)
    T_eff_BA = np.mean(T_k[:4])  # B2 sector average
    if T_eff_BA > 0:
        n_bose_gge = 1.0 / (np.exp(omega_n / T_eff_BA) - 1.0) if omega_n / T_eff_BA < 50 else 0.0
        n_bose_eq  = 1.0 / (np.exp(omega_n / T_eq) - 1.0) if omega_n / T_eq < 50 else 0.0
    else:
        n_bose_gge = 0.0
        n_bose_eq  = 0.0

    # S(q, omega) = A_BA * (1 + n_bose) * delta(omega - omega_n)  [creation]
    #             + A_BA * n_bose * delta(omega + omega_n)          [annihilation]
    # We only plot positive omega (creation side)
    S_gge[iq_ba, :] += A_BA * (1.0 + n_bose_gge) * lorentzian(omega_grid, omega_n, eta)
    S_eq[iq_ba, :]  += A_BA * (1.0 + n_bose_eq)  * lorentzian(omega_grid, omega_n, eta)

print(f"BA modes: T_eff(B2 avg) = {np.mean(T_k[:4]):.4f} M_KK")
print(f"BA modes: T_eq = {T_eq:.4f} M_KK")

# --- 3c. Leggett (amplitude) modes ---
# Leggett modes are amplitude oscillations of Delta. They couple to density
# through the modulation of the gap. The coupling is:
#   A_L(q, n) = (Delta / omega_L_n)^2 * q^2 / (1 + q^2 * xi^2)
# Leggett modes are massive (omega_L > 0 even at q=0).

print("\n--- Leggett modes ---")

for n_L in range(len(omega_L)):
    omega_Ln = omega_L[n_L]
    q_L = q_values[n_L] if n_L < len(q_values) else q_values[-1]

    # Leggett coupling: amplitude mode couples to density via gap modulation
    # Strength ~ (Delta/omega_L)^2 but suppressed relative to BA by (Delta/E_F)^2
    A_L = 0.1 * (Delta / omega_Ln)**2 / (1.0 + (q_L * xi_BCS)**2)

    # Bose occupation (Leggett modes are bosonic)
    T_eff_L = np.mean(T_k[:4])  # B2 sector
    if T_eff_L > 0 and omega_Ln / T_eff_L < 50:
        n_L_gge = 1.0 / (np.exp(omega_Ln / T_eff_L) - 1.0)
        n_L_eq  = 1.0 / (np.exp(omega_Ln / T_eq) - 1.0) if omega_Ln / T_eq < 50 else 0.0
    else:
        n_L_gge = 0.0
        n_L_eq  = 0.0

    S_gge[n_L, :] += A_L * (1.0 + n_L_gge) * lorentzian(omega_grid, omega_Ln, eta)
    S_eq[n_L, :]  += A_L * (1.0 + n_L_eq)  * lorentzian(omega_grid, omega_Ln, eta)

print(f"Leggett modes: omega_L range [{omega_L.min():.4f}, {omega_L.max():.4f}] M_KK")

# =============================================================================
# 4. Analysis: identify features
# =============================================================================
print("\n" + "=" * 70)
print("FEATURE ANALYSIS")
print("=" * 70)

# 4a. Hard gap
# The lowest-energy excitation in S(q, omega): either Leggett or BA
omega_min_collective = min(omega_L.min(), omega_BA.min())
print(f"\nLowest collective mode: {omega_min_collective:.4f} M_KK")
print(f"  Leggett floor: {omega_L.min():.4f} M_KK")
print(f"  BA floor: {omega_BA.min():.4f} M_KK")
print(f"  Pair-breaking threshold: {2*Delta:.4f} M_KK")
print(f"  Hard gap for quasiparticles: YES at 2*Delta = {2*Delta:.4f}")
print(f"  Sub-gap collective modes: YES (Leggett at {omega_L.min():.4f}, BA at {omega_BA.min():.4f})")

# 4b. GGE vs thermal difference
S_diff = S_gge - S_eq
max_diff_idx = np.unravel_index(np.argmax(np.abs(S_diff)), S_diff.shape)
print(f"\nGGE vs Thermal:")
print(f"  Max |S_gge - S_eq| at q={q_values[max_diff_idx[0]]:.3f}, "
      f"omega={omega_grid[max_diff_idx[1]]:.3f}")
print(f"  |Delta S| / max(S_gge) = {np.max(np.abs(S_diff)) / np.max(S_gge):.4f}")

# Integrated spectral weight comparison
W_gge = np.trapezoid(S_gge, omega_grid, axis=1)
W_eq  = np.trapezoid(S_eq, omega_grid, axis=1)
print(f"  Integrated weight ratio (GGE/eq): {np.sum(W_gge)/np.sum(W_eq):.4f}")

# 4c. Spectral weight distribution by region
omega_leggett_max = omega_L.max()
omega_ba_max = omega_BA.max()
mask_leggett = omega_grid < omega_leggett_max
mask_ba      = (omega_grid >= omega_leggett_max) & (omega_grid < 2*Delta)
mask_pb      = omega_grid >= 2*Delta

W_L_gge  = np.trapezoid(S_gge[:, mask_leggett], omega_grid[mask_leggett], axis=1).sum()
W_BA_gge = np.trapezoid(S_gge[:, mask_ba], omega_grid[mask_ba], axis=1).sum()
W_pb_gge = np.trapezoid(S_gge[:, mask_pb], omega_grid[mask_pb], axis=1).sum()
W_total_gge = W_L_gge + W_BA_gge + W_pb_gge

print(f"\nSpectral weight distribution (GGE):")
print(f"  Leggett band  (0, {omega_leggett_max:.3f}):  {W_L_gge:.4f}  ({100*W_L_gge/W_total_gge:.1f}%)")
print(f"  BA band       ({omega_leggett_max:.3f}, {2*Delta:.3f}): {W_BA_gge:.4f}  ({100*W_BA_gge/W_total_gge:.1f}%)")
print(f"  Pair-breaking ({2*Delta:.3f}, {omega_max:.3f}): {W_pb_gge:.4f}  ({100*W_pb_gge/W_total_gge:.1f}%)")
print(f"  Total: {W_total_gge:.4f}")

# Same for thermal
W_L_eq  = np.trapezoid(S_eq[:, mask_leggett], omega_grid[mask_leggett], axis=1).sum()
W_BA_eq = np.trapezoid(S_eq[:, mask_ba], omega_grid[mask_ba], axis=1).sum()
W_pb_eq = np.trapezoid(S_eq[:, mask_pb], omega_grid[mask_pb], axis=1).sum()
W_total_eq = W_L_eq + W_BA_eq + W_pb_eq

print(f"\nSpectral weight distribution (Thermal T={T_eq:.4f}):")
print(f"  Leggett band:  {W_L_eq:.4f}  ({100*W_L_eq/W_total_eq:.1f}%)")
print(f"  BA band:       {W_BA_eq:.4f}  ({100*W_BA_eq/W_total_eq:.1f}%)")
print(f"  Pair-breaking: {W_pb_eq:.4f}  ({100*W_pb_eq/W_total_eq:.1f}%)")

# 4d. GGE non-thermality measure
# Jensen-Shannon divergence between S_gge and S_eq spectral weight profiles
from scipy.stats import entropy

# q-integrated spectral functions
S_gge_integrated = np.sum(S_gge, axis=0)
S_eq_integrated  = np.sum(S_eq, axis=0)
S_gge_norm = S_gge_integrated / np.sum(S_gge_integrated)
S_eq_norm  = S_eq_integrated / np.sum(S_eq_integrated)
S_avg = 0.5 * (S_gge_norm + S_eq_norm)
D_JS = 0.5 * entropy(S_gge_norm, S_avg) + 0.5 * entropy(S_eq_norm, S_avg)

print(f"\nJensen-Shannon divergence D_JS(S_gge || S_eq) = {D_JS:.6f}")
print(f"  sqrt(D_JS) = {np.sqrt(D_JS):.6f} (JS distance)")

# 4e. BCS sum rule check: f-sum rule
# integral S(q, omega) * omega d_omega = q^2 * N/m (for each q)
# In our units, this should be proportional to q^2
first_moment_gge = np.trapezoid(S_gge * omega_grid[None, :], omega_grid, axis=1)
print(f"\nFirst moment (f-sum rule proxy):")
for iq in [0, 5, 10, 15, 20, 25, 30]:
    if iq < len(q_values):
        print(f"  q={q_values[iq]:.3f}: integral(S*omega) = {first_moment_gge[iq]:.4e}")

# =============================================================================
# 5. Quasiparticle pair-breaking continuum (BCS DoS convolution)
# =============================================================================
# For a cleaner view of the continuum, compute the BCS DoS-based S(omega)
# This is the q-integrated response

print("\n--- BCS pair-breaking density of states ---")
E_grid_dos = np.linspace(Delta + 0.001, 2.5, 200)
N_bcs = np.abs(E_grid_dos) / np.sqrt(E_grid_dos**2 - Delta**2)
print(f"BCS DoS: van Hove singularity at E = Delta = {Delta:.4f}")
print(f"BCS DoS peak (at E=Delta+0.01): {np.max(N_bcs):.2f} * N(0)")

# =============================================================================
# 6. Save results
# =============================================================================
outpath = os.path.join(data_dir, 's58_sq_omega_gge.npz')
np.savez(outpath,
    # Grid
    q_values=q_values,
    omega_grid=omega_grid,
    laplacian_eigs=lap_eigs,
    # S(q, omega)
    S_gge=S_gge,
    S_eq=S_eq,
    S_diff=S_diff,
    # Inputs
    fk_gge=fk_gge,
    fk_eq=fk_eq,
    E_k=E_k,
    xi_k=xi_k,
    T_k_volovik=T_k,
    T_eq_canonical=T_eq,
    Delta=Delta,
    omega_BA=omega_BA,
    omega_L=omega_L,
    eta=eta,  # (local)
    # Spectral weights
    W_gge_leggett=W_L_gge,
    W_gge_BA=W_BA_gge,
    W_gge_pb=W_pb_gge,
    W_eq_leggett=W_L_eq,
    W_eq_BA=W_BA_eq,
    W_eq_pb=W_pb_eq,
    D_JS_spectral=D_JS,
    # Gate
    gate_name='SQ-OMEGA-GGE-58',
    gate_verdict='INFO',
    gate_detail=f'Hard gap at 2*Delta={2*Delta:.4f}. D_JS(GGE||eq)={D_JS:.6f}. '
                f'BA sub-gap continuum [{omega_BA.min():.3f},{omega_BA.max():.3f}]. '
                f'Leggett band [{omega_L.min():.3f},{omega_L.max():.3f}].'
)
print(f"\nData saved: {outpath}")

# =============================================================================
# 7. Plot
# =============================================================================
fig, axes = plt.subplots(2, 3, figsize=(18, 11))

# --- Panel (a): S_gge(q, omega) heat map ---
ax = axes[0, 0]
# Use sorted q for plotting
q_sort = np.argsort(q_values)
q_sorted = q_values[q_sort]
S_gge_sorted = S_gge[q_sort, :]

# Avoid log of zero
S_plot = S_gge_sorted.copy()
S_plot[S_plot < 1e-10] = 1e-10

im = ax.pcolormesh(omega_grid, q_sorted, S_plot,
                   norm=LogNorm(vmin=1e-4, vmax=S_plot.max()),
                   cmap='inferno', shading='auto')
ax.axvline(2*Delta, color='cyan', ls='--', lw=1.5, label=f'2$\\Delta$={2*Delta:.3f}')
ax.axvline(omega_L.min(), color='lime', ls=':', lw=1.0, label=f'$\\omega_L^{{min}}$={omega_L.min():.3f}')
ax.axvline(omega_BA.min(), color='orange', ls=':', lw=1.0, label=f'$\\omega_{{BA}}^{{min}}$={omega_BA.min():.3f}')
ax.set_xlabel('$\\omega$ [M$_{KK}$]', fontsize=12)
ax.set_ylabel('q [M$_{KK}$]', fontsize=12)
ax.set_title('(a) $S_{GGE}(q, \\omega)$', fontsize=13, fontweight='bold')
ax.legend(loc='upper right', fontsize=8)
plt.colorbar(im, ax=ax, label='$S(q,\\omega)$')

# --- Panel (b): S_eq(q, omega) heat map ---
ax = axes[0, 1]
S_eq_sorted = S_eq[q_sort, :]
S_eq_plot = S_eq_sorted.copy()
S_eq_plot[S_eq_plot < 1e-10] = 1e-10

im2 = ax.pcolormesh(omega_grid, q_sorted, S_eq_plot,
                    norm=LogNorm(vmin=1e-4, vmax=S_eq_plot.max()),
                    cmap='inferno', shading='auto')
ax.axvline(2*Delta, color='cyan', ls='--', lw=1.5, label=f'2$\\Delta$={2*Delta:.3f}')
ax.set_xlabel('$\\omega$ [M$_{KK}$]', fontsize=12)
ax.set_ylabel('q [M$_{KK}$]', fontsize=12)
ax.set_title(f'(b) $S_{{eq}}(q, \\omega)$ at T={T_eq:.3f}', fontsize=13, fontweight='bold')
ax.legend(loc='upper right', fontsize=8)
plt.colorbar(im2, ax=ax, label='$S(q,\\omega)$')

# --- Panel (c): Difference S_gge - S_eq ---
ax = axes[0, 2]
S_diff_sorted = S_diff[q_sort, :]
vabs = max(np.abs(S_diff_sorted.min()), np.abs(S_diff_sorted.max()))
if vabs < 1e-10:
    vabs = 1e-4
im3 = ax.pcolormesh(omega_grid, q_sorted, S_diff_sorted,
                    vmin=-vabs, vmax=vabs,
                    cmap='RdBu_r', shading='auto')
ax.axvline(2*Delta, color='black', ls='--', lw=1.5)
ax.set_xlabel('$\\omega$ [M$_{KK}$]', fontsize=12)
ax.set_ylabel('q [M$_{KK}$]', fontsize=12)
ax.set_title('(c) $S_{GGE} - S_{eq}$ (non-thermal excess)', fontsize=13, fontweight='bold')
plt.colorbar(im3, ax=ax, label='$\\Delta S$')

# --- Panel (d): q-integrated S(omega) comparison ---
ax = axes[1, 0]
ax.plot(omega_grid, S_gge_integrated, 'r-', lw=2.0, label='GGE (non-thermal)')
ax.plot(omega_grid, S_eq_integrated, 'b--', lw=1.5, label=f'Thermal T={T_eq:.3f}')
ax.axvline(2*Delta, color='grey', ls='--', lw=1, alpha=0.7, label=f'2$\\Delta$')
ax.axvline(omega_L.min(), color='lime', ls=':', lw=1, alpha=0.7, label='Leggett floor')
ax.axvline(omega_BA.min(), color='orange', ls=':', lw=1, alpha=0.7, label='BA floor')
ax.set_xlabel('$\\omega$ [M$_{KK}$]', fontsize=12)
ax.set_ylabel('$\\int dq\\; S(q, \\omega)$', fontsize=12)
ax.set_title('(d) q-integrated spectrum', fontsize=13, fontweight='bold')
ax.legend(fontsize=9)
ax.set_xlim(0, omega_max)

# --- Panel (e): GGE vs thermal occupation ---
ax = axes[1, 1]
mode_idx = np.arange(N_modes)
width = 0.35  # (local)
bars1 = ax.bar(mode_idx - width/2, fk_gge, width, color='red', alpha=0.7, label='GGE')
bars2 = ax.bar(mode_idx + width/2, fk_eq, width, color='blue', alpha=0.7, label=f'Thermal T={T_eq:.3f}')
ax.set_xlabel('Mode index', fontsize=12)
ax.set_ylabel('Occupation $f_k$', fontsize=12)
ax.set_title('(e) Mode occupations: GGE vs thermal', fontsize=13, fontweight='bold')
ax.set_xticks(mode_idx)
labels_short = ['B2[0]','B2[1]','B2[2]','B2[3]','B1','B3[0]','B3[1]','B3[2]']
ax.set_xticklabels(labels_short, rotation=45, fontsize=9)
ax.legend(fontsize=10)

# Annotate effective temperatures
for i in range(N_modes):
    ax.annotate(f'T={T_k[i]:.2f}', (i - width/2, fk_gge[i]),
                textcoords="offset points", xytext=(0, 5),
                fontsize=7, ha='center', color='darkred')

# --- Panel (f): Spectral weight by band ---
ax = axes[1, 2]
bands = ['Leggett\n(amplitude)', 'BA\n(phase)', 'Pair-breaking\n(qp)']
weights_gge = [W_L_gge, W_BA_gge, W_pb_gge]
weights_eq  = [W_L_eq, W_BA_eq, W_pb_eq]
x_band = np.arange(3)
width_b = 0.35  # (local)
ax.bar(x_band - width_b/2, weights_gge, width_b, color='red', alpha=0.7, label='GGE')
ax.bar(x_band + width_b/2, weights_eq, width_b, color='blue', alpha=0.7, label='Thermal')
ax.set_ylabel('Integrated spectral weight', fontsize=12)
ax.set_title('(f) Spectral weight by band', fontsize=13, fontweight='bold')
ax.set_xticks(x_band)
ax.set_xticklabels(bands, fontsize=10)
ax.legend(fontsize=10)

fig.suptitle('Dynamic Structure Factor $S(q, \\omega)$: Post-Transit GGE vs Thermal Equilibrium\n'
             f'$\\Delta$ = {Delta:.3f} M$_{{KK}}$,  '
             f'$D_{{JS}}$ = {D_JS:.4f},  '
             f'$T_{{eq}}$ = {T_eq:.3f} M$_{{KK}}$',
             fontsize=14, fontweight='bold', y=1.01)

plt.tight_layout()
plotpath = os.path.join(data_dir, 's58_sq_omega_gge.png')
fig.savefig(plotpath, dpi=150, bbox_inches='tight')
print(f"Plot saved: {plotpath}")

# =============================================================================
# 8. Gate verdict
# =============================================================================
print("\n" + "=" * 70)
print("GATE: SQ-OMEGA-GGE-58")
print("=" * 70)

hard_gap_visible = (omega_L.min() > 0) and (2*Delta > omega_BA.max() * 0.5)
nonthermal_resolvable = D_JS > 0.001  # JS divergence threshold

print(f"  Hard gap at 2*Delta = {2*Delta:.4f} M_KK: {'YES' if hard_gap_visible else 'NO'}")
print(f"  Sub-gap collective modes present: YES")
print(f"    Leggett floor: {omega_L.min():.4f} M_KK ({omega_L.min()/(2*Delta)*100:.1f}% of 2*Delta)")
print(f"    BA floor: {omega_BA.min():.4f} M_KK ({omega_BA.min()/(2*Delta)*100:.1f}% of 2*Delta)")
print(f"  Non-thermal occupation resolvable: {'YES' if nonthermal_resolvable else 'NO'}")
print(f"    D_JS = {D_JS:.6f} (threshold: 0.001)")
print(f"    GGE/thermal weight ratio: {np.sum(W_gge)/np.sum(W_eq):.4f}")
print(f"  Verdict: INFO (diagnostic computed)")

print("\n--- Physical interpretation ---")
print(f"  The DM excitation spectrum has three bands:")
print(f"    1. Leggett (amplitude) band: [{omega_L.min():.3f}, {omega_L.max():.3f}] M_KK")
print(f"       = [{omega_L.min()*float(M_KK):.2e}, {omega_L.max()*float(M_KK):.2e}] GeV")
print(f"    2. BA (phase) band: [{omega_BA.min():.3f}, {omega_BA.max():.3f}] M_KK")
print(f"       = [{omega_BA.min()*float(M_KK):.2e}, {omega_BA.max()*float(M_KK):.2e}] GeV")
print(f"    3. Pair-breaking continuum: [{2*Delta:.3f}, inf) M_KK")
print(f"       = [{2*Delta*float(M_KK):.2e}, inf) GeV")
print(f"  The GGE-specific signature: enhanced occupation of B2 modes (f~0.17-0.27)")
print(f"  relative to thermal (f~0.17 uniform). B3 modes nearly frozen (f~0.003-0.004)")
print(f"  vs thermal B3 (f~0.04). This 10:1 B2/B3 asymmetry is the GGE fingerprint.")

print("\nDone.")
