#!/usr/bin/env python3
"""
s56_ba_spectrum.py — Bogoliubov-Anderson Phonon Spectrum on 32-Cell Graph

BA-SPECTRUM-56: Compute the collective phase-fluctuation normal modes
of the superfluid fabric modeled as a Josephson junction array on the
32-cell CG graph.

Physics:
  H_rotor = -E_J * Sum_{<ij>} cos(phi_i - phi_j) + E_c * Sum_i n_i^2
  Expanded to quadratic order:
    omega_n(tau) = sqrt(E_c(tau) * E_J(tau) * lambda_n)
  where lambda_n are the graph Laplacian eigenvalues.

Gate: BA-SPECTRUM-56
  INFO: characterize F_BA(tau). If minimum in [0.10, 0.30], flag.

Author: quantum-acoustics-theorist
Session: S56
"""

import sys
import os
import numpy as np
from scipy.interpolate import interp1d
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

sys.path.insert(0, 'computations')
from canonical_constants import Delta_0_OES, E_cond, tau_fold, N_cells

# =============================================================================
# 0. Load data
# =============================================================================

data_tb = np.load('computations/session-54/s54_tb_hamiltonian.npz')
tau_values = data_tb['tau_values']   # (50,)
eigenvalues = data_tb['eigenvalues'] # (50, 32) — TB eigenvalues at each tau
J_C2_tau = data_tb['J_C2_tau']      # (50,) — C2 hopping strength vs tau
adj_C2 = data_tb['adj_C2']          # (32, 32) — adjacency for C2 bonds

data_sf = np.load('computations/session-54/s54_scale_factor.npz')
tau_sf = data_sf['tau']  # (10,)
H_sf = data_sf['H']     # (10,) — Hubble parameter at these tau values

N_tau = len(tau_values)  # 50
Delta = Delta_0_OES  # 0.4643 M_KK — the OES/pair-addition gap

print(f"Loaded: {N_tau} tau values in [{tau_values[0]:.4f}, {tau_values[-1]:.4f}]")
print(f"N_cells = {N_cells}, Delta = {Delta:.4f} M_KK")
print(f"J_C2 range: [{J_C2_tau.min():.4f}, {J_C2_tau.max():.4f}]")

# =============================================================================
# 1. Graph Laplacian eigenvalues
# =============================================================================
# The graph Laplacian L = D - A, where D = diag(degree), A = adjacency.
# For the Josephson array, the relevant Laplacian is for C2 bonds only,
# since E_J is derived from C2 hopping.

A_C2 = adj_C2.astype(float)
degree_C2 = A_C2.sum(axis=1)
L_C2 = np.diag(degree_C2) - A_C2

# Eigenvalues of graph Laplacian (tau-independent topology)
laplacian_eigs = np.linalg.eigvalsh(L_C2)
laplacian_eigs = np.sort(laplacian_eigs)
# Zero mode
laplacian_eigs[0] = 0.0  # enforce exactly zero

print(f"\nGraph Laplacian eigenvalues (C2 bonds):")
print(f"  lambda_0 = {laplacian_eigs[0]:.6f} (Goldstone zero mode)")
print(f"  lambda_1 = {laplacian_eigs[1]:.6f} (lowest nonzero = Fiedler)")
print(f"  lambda_max = {laplacian_eigs[-1]:.6f}")
print(f"  Spectral gap: {laplacian_eigs[1]:.6f}")
print(f"  Number of nonzero modes: {np.sum(laplacian_eigs > 1e-10)}")

# =============================================================================
# 2. BCS coherence factors and E_J, E_c at each tau
# =============================================================================

E_J_arr = np.zeros(N_tau)
E_c_arr = np.zeros(N_tau)
F_anom_arr = np.zeros(N_tau)

for i in range(N_tau):
    eigs_i = eigenvalues[i]  # (32,) single-particle eigenvalues

    # Chemical potential at spectral midpoint (half-filling: 16 particles in 32 levels)
    mu = 0.5 * (eigs_i[15] + eigs_i[16])  # (local)

    # BCS quasiparticle energies
    xi_k = eigs_i - mu                          # (32,)
    E_qp_k = np.sqrt(xi_k**2 + Delta**2)       # (32,)

    # Anomalous density (Josephson kernel)
    # F_anomalous = Sum_k Delta / (2 * E_qp_k^2)
    F_anom = np.sum(Delta / (2.0 * E_qp_k**2))
    F_anom_arr[i] = F_anom

    # Josephson energy per bond: E_J = J_C2(tau)^2 * F_anomalous
    E_J_arr[i] = J_C2_tau[i]**2 * F_anom

    # Charging energy: half the level spacing at Fermi surface
    E_c_arr[i] = 0.5 * (eigs_i[16] - eigs_i[15])

print(f"\nE_J range: [{E_J_arr.min():.4f}, {E_J_arr.max():.4f}] M_KK")
print(f"E_c range: [{E_c_arr.min():.6f}, {E_c_arr.max():.6f}] M_KK")
print(f"E_J/E_c range: [{(E_J_arr/E_c_arr).min():.1f}, {(E_J_arr/E_c_arr).max():.1f}]")
print(f"F_anom range: [{F_anom_arr.min():.4f}, {F_anom_arr.max():.4f}]")

# =============================================================================
# 3. BA phonon frequencies: omega_n(tau) = sqrt(E_c * E_J * lambda_n)
# =============================================================================

# omega_n for n=1,...,31 (skip zero mode n=0)
# Shape: (N_tau, 31)
omega_BA = np.zeros((N_tau, N_cells - 1))

for i in range(N_tau):
    for n in range(N_cells - 1):
        lam_n = laplacian_eigs[n + 1]  # skip zero mode
        omega_BA[i, n] = np.sqrt(E_c_arr[i] * E_J_arr[i] * lam_n)

print(f"\nBA phonon frequencies:")
print(f"  omega_1 (Fiedler) range: [{omega_BA[:, 0].min():.4f}, {omega_BA[:, 0].max():.4f}]")
print(f"  omega_31 (max) range: [{omega_BA[:, -1].min():.4f}, {omega_BA[:, -1].max():.4f}]")

# Josephson plasma frequency: omega_J = sqrt(8 * E_J * E_c) for a single junction
# For the array, the collective version: omega_1 * sqrt(N) is one measure
omega_J_single = np.sqrt(8.0 * E_J_arr * E_c_arr)
omega_J_collective = omega_BA[:, 0] * np.sqrt(N_cells)

print(f"  omega_J (single junction) range: [{omega_J_single.min():.4f}, {omega_J_single.max():.4f}]")
print(f"  omega_1*sqrt(N) range: [{omega_J_collective.min():.4f}, {omega_J_collective.max():.4f}]")

# =============================================================================
# 4. T_GH(tau) — Gibbons-Hawking temperature interpolated to 50 tau points
# =============================================================================

# T_GH = H / (2*pi)
T_GH_sparse = H_sf / (2.0 * np.pi)

# Interpolate to 50 tau values (cubic spline, extrapolate for tau > max(tau_sf))
interp_T_GH = interp1d(tau_sf, T_GH_sparse, kind='cubic', fill_value='extrapolate')
T_GH = interp_T_GH(tau_values)

# Clamp any negative T_GH from extrapolation to a small positive value
T_GH = np.maximum(T_GH, 1e-10)

print(f"\nT_GH range: [{T_GH.min():.6f}, {T_GH.max():.6f}] M_KK")
print(f"T_GH at fold (tau~0.19): {interp_T_GH(tau_fold):.6f}")

# =============================================================================
# 5. BA free energy: F_BA(tau, T_GH) = Sum_{n=1}^{31} f(omega_n/T_GH)
#    where f(x) = x/2 + T*ln(1 - exp(-x/T)) = omega/2 + T*ln(1 - exp(-omega/T))
# =============================================================================

F_BA = np.zeros(N_tau)
F_ZPE = np.zeros(N_tau)  # zero-point energy only
F_thermal = np.zeros(N_tau)  # thermal contribution only

for i in range(N_tau):
    T = T_GH[i]
    for n in range(N_cells - 1):
        om = omega_BA[i, n]
        # Zero-point contribution
        F_ZPE[i] += om / 2.0
        # Thermal contribution: T * ln(1 - exp(-omega/T))
        x = om / T
        if x > 500:
            # Negligible thermal contribution
            thermal = 0.0
        else:
            thermal = T * np.log(1.0 - np.exp(-x))
        F_thermal[i] += thermal

    F_BA[i] = F_ZPE[i] + F_thermal[i]

print(f"\nF_BA range: [{F_BA.min():.4f}, {F_BA.max():.4f}] M_KK")
print(f"F_ZPE range: [{F_ZPE.min():.4f}, {F_ZPE.max():.4f}]")
print(f"F_thermal range: [{F_thermal.min():.6f}, {F_thermal.max():.6f}]")

# =============================================================================
# 6. Monotonicity check and minimum search
# =============================================================================

# Check if F_BA is monotonically decreasing or has a minimum
dF = np.diff(F_BA)
sign_changes = np.where(np.diff(np.sign(dF)))[0]

# Search for minimum in [0.10, 0.30]
mask = (tau_values >= 0.10) & (tau_values <= 0.30)
if np.any(mask):
    F_in_range = F_BA[mask]
    tau_in_range = tau_values[mask]
    idx_min_range = np.argmin(F_in_range)
    tau_min_range = tau_in_range[idx_min_range]
    F_min_range = F_in_range[idx_min_range]

    # Is this a local minimum (not at boundary)?
    is_interior_min = (idx_min_range > 0) and (idx_min_range < len(tau_in_range) - 1)

    # Global minimum
    idx_global_min = np.argmin(F_BA)
    tau_global_min = tau_values[idx_global_min]
    F_global_min = F_BA[idx_global_min]

print(f"\nMonotonicity analysis:")
print(f"  Sign changes in dF_BA: {len(sign_changes)}")
if len(sign_changes) > 0:
    for sc in sign_changes:
        print(f"    at tau ~ {0.5*(tau_values[sc]+tau_values[sc+1]):.4f}")

print(f"\nGlobal minimum: F_BA = {F_global_min:.4f} at tau = {tau_global_min:.4f}")
print(f"F_BA at tau=0: {F_BA[0]:.4f}")
print(f"F_BA at tau=0.5: {F_BA[-1]:.4f}")

if is_interior_min:
    # Compute depth relative to boundary
    F_boundary_max = max(F_BA[mask][0], F_BA[mask][-1])
    depth = F_boundary_max - F_min_range
    print(f"\n*** INTERIOR MINIMUM in [0.10, 0.30] ***")
    print(f"  tau_min = {tau_min_range:.4f}")
    print(f"  F_min = {F_min_range:.4f}")
    print(f"  Depth = {depth:.6f}")
    has_minimum = True
else:
    print(f"\nNo interior minimum in [0.10, 0.30].")
    print(f"  F_BA at range boundary: {F_in_range[0]:.4f} (tau={tau_in_range[0]:.3f}) to {F_in_range[-1]:.4f} (tau={tau_in_range[-1]:.3f})")
    has_minimum = False

# =============================================================================
# 7. Additional diagnostics
# =============================================================================

# Ratio E_J/E_c (superfluid parameter)
ratio_EJ_Ec = E_J_arr / E_c_arr

# Effective mode count: d_s = 2 (Weyl class for linear dispersion with N_cells - 1 = 31 modes)
# Compare to 992 single-particle modes (= 32 cells * 31 modes? No: 32 cells * 8 Dirac modes each = 256)
# Actually: 31 BA modes vs 32*8=256 SP Dirac modes per cell => ratio

# Bandwidth of BA spectrum at each tau
BW_BA = omega_BA[:, -1] - omega_BA[:, 0]

# Mean level spacing
mean_spacing = BW_BA / (N_cells - 2)  # 30 gaps between 31 modes

print(f"\nBA spectrum characteristics at fold (tau ~ {tau_fold:.2f}):")
idx_fold = np.argmin(np.abs(tau_values - tau_fold))
print(f"  tau_fold index: {idx_fold}, tau = {tau_values[idx_fold]:.4f}")
print(f"  E_J = {E_J_arr[idx_fold]:.4f}, E_c = {E_c_arr[idx_fold]:.6f}")
print(f"  E_J/E_c = {ratio_EJ_Ec[idx_fold]:.1f}")
print(f"  omega_1 = {omega_BA[idx_fold, 0]:.4f}")
print(f"  omega_31 = {omega_BA[idx_fold, -1]:.4f}")
print(f"  Bandwidth = {BW_BA[idx_fold]:.4f}")
print(f"  T_GH = {T_GH[idx_fold]:.6f}")
print(f"  F_BA = {F_BA[idx_fold]:.4f}")
print(f"  F_ZPE = {F_ZPE[idx_fold]:.4f}")
print(f"  F_thermal = {F_thermal[idx_fold]:.6f}")
print(f"  omega_1/T_GH = {omega_BA[idx_fold, 0]/T_GH[idx_fold]:.2f} (>>1 = quantum regime)")

# Sound velocity from lowest mode: c_BA ~ omega_1 / k_min
# On a graph, k_min ~ pi/diameter. Diameter = 6 hops.
# More precisely: c_BA = omega_1 * d_graph / pi where d_graph = diameter
diameter = int(data_tb['diameter'])
k_min = np.pi / diameter
c_BA = omega_BA[:, 0] / k_min

print(f"\nBA sound velocity (c_BA = omega_1 / k_min, k_min = pi/{diameter}):")
print(f"  c_BA range: [{c_BA.min():.4f}, {c_BA.max():.4f}]")
print(f"  c_BA at fold: {c_BA[idx_fold]:.4f}")

# =============================================================================
# 8. Save results
# =============================================================================

np.savez('computations/session-56/s56_ba_spectrum.npz',
    # Grid
    tau_values=tau_values,
    N_cells=N_cells,
    Delta=Delta,

    # Graph Laplacian
    laplacian_eigs=laplacian_eigs,

    # BCS / Josephson parameters
    E_J=E_J_arr,
    E_c=E_c_arr,
    F_anomalous=F_anom_arr,
    ratio_EJ_Ec=ratio_EJ_Ec,

    # BA phonon spectrum
    omega_BA=omega_BA,       # (50, 31)
    omega_J_single=omega_J_single,
    omega_J_collective=omega_J_collective,

    # Thermodynamics
    T_GH=T_GH,
    F_BA=F_BA,
    F_ZPE=F_ZPE,
    F_thermal=F_thermal,

    # Diagnostics
    BW_BA=BW_BA,
    c_BA=c_BA,
    k_min=k_min,
    diameter=diameter,

    # Gate
    has_minimum_in_range=has_minimum,
    tau_global_min=tau_global_min,
    F_global_min=F_global_min,
    gate_name='BA-SPECTRUM-56',
    gate_verdict='INFO'
)
print("\nSaved: computations/session-56/s56_ba_spectrum.npz")

# =============================================================================
# 9. Plotting
# =============================================================================

fig = plt.figure(figsize=(18, 14))
gs = GridSpec(3, 2, figure=fig, hspace=0.32, wspace=0.28)

# --- Panel (a): BA dispersion at 5 tau values ---
ax1 = fig.add_subplot(gs[0, 0])
tau_plot_indices = [0, 12, 24, 36, 49]  # tau ~ 0, 0.12, 0.24, 0.37, 0.50
colors_disp = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
mode_indices = np.arange(1, N_cells)  # 1..31

for j, idx in enumerate(tau_plot_indices):
    ax1.plot(mode_indices, omega_BA[idx], 'o-', markersize=3, linewidth=1.2,
             color=colors_disp[j], label=f'$\\tau={tau_values[idx]:.2f}$')

ax1.set_xlabel('Mode index $n$', fontsize=11)
ax1.set_ylabel('$\\omega_n$ [$M_{KK}$]', fontsize=11)
ax1.set_title('(a) BA Phonon Dispersion', fontsize=12, fontweight='bold')
ax1.legend(fontsize=9, loc='upper left')
ax1.grid(True, alpha=0.3)

# --- Panel (b): F_BA(tau) ---
ax2 = fig.add_subplot(gs[0, 1])
ax2.plot(tau_values, F_BA, 'k-', linewidth=2, label='$F_{BA}$ (total)')
ax2.plot(tau_values, F_ZPE, 'b--', linewidth=1.5, label='$F_{ZPE}$ (zero-point)')
ax2.plot(tau_values, F_thermal, 'r:', linewidth=1.5, label='$F_{thermal}$')
ax2.axvline(tau_fold, color='gray', linestyle='--', alpha=0.5, label=f'fold ($\\tau={tau_fold:.2f}$)')

if has_minimum:
    ax2.axvline(tau_min_range, color='green', linestyle=':', alpha=0.7,
                label=f'min at $\\tau={tau_min_range:.3f}$')

ax2.set_xlabel('$\\tau$', fontsize=11)
ax2.set_ylabel('$F$ [$M_{KK}$]', fontsize=11)
ax2.set_title('(b) BA Free Energy', fontsize=12, fontweight='bold')
ax2.legend(fontsize=9)
ax2.grid(True, alpha=0.3)

# --- Panel (c): E_J and E_c ---
ax3 = fig.add_subplot(gs[1, 0])
ax3a = ax3
ax3b = ax3.twinx()

line1, = ax3a.plot(tau_values, E_J_arr, 'b-', linewidth=2, label='$E_J$')
line2, = ax3b.plot(tau_values, E_c_arr, 'r-', linewidth=2, label='$E_c$')

ax3a.set_xlabel('$\\tau$', fontsize=11)
ax3a.set_ylabel('$E_J$ [$M_{KK}$]', fontsize=11, color='b')
ax3b.set_ylabel('$E_c$ [$M_{KK}$]', fontsize=11, color='r')
ax3a.tick_params(axis='y', labelcolor='b')
ax3b.tick_params(axis='y', labelcolor='r')
ax3.set_title('(c) Josephson and Charging Energies', fontsize=12, fontweight='bold')
lines = [line1, line2]
ax3.legend(lines, [l.get_label() for l in lines], fontsize=9, loc='center right')
ax3.grid(True, alpha=0.3)

# --- Panel (d): E_J/E_c ratio ---
ax4 = fig.add_subplot(gs[1, 1])
ax4.plot(tau_values, ratio_EJ_Ec, 'k-', linewidth=2)
ax4.axhline(1.0, color='r', linestyle='--', alpha=0.5, label='$E_J/E_c = 1$ (SF-insulator)')
ax4.axvline(tau_fold, color='gray', linestyle='--', alpha=0.5, label=f'fold')
ax4.set_xlabel('$\\tau$', fontsize=11)
ax4.set_ylabel('$E_J / E_c$', fontsize=11)
ax4.set_title('(d) Superfluid Parameter', fontsize=12, fontweight='bold')
ax4.set_yscale('log')
ax4.legend(fontsize=9)
ax4.grid(True, alpha=0.3)

# --- Panel (e): omega_J and omega_1 ---
ax5 = fig.add_subplot(gs[2, 0])
ax5.plot(tau_values, omega_J_single, 'b-', linewidth=2, label='$\\omega_J$ (single junction)')
ax5.plot(tau_values, omega_BA[:, 0], 'g-', linewidth=2, label='$\\omega_1$ (Fiedler)')
ax5.plot(tau_values, omega_BA[:, -1], 'r--', linewidth=1.5, label='$\\omega_{31}$ (max)')
ax5.plot(tau_values, T_GH, 'k:', linewidth=1.5, label='$T_{GH}$')
ax5.axvline(tau_fold, color='gray', linestyle='--', alpha=0.5)
ax5.set_xlabel('$\\tau$', fontsize=11)
ax5.set_ylabel('Energy scale [$M_{KK}$]', fontsize=11)
ax5.set_title('(e) Frequency Hierarchy', fontsize=12, fontweight='bold')
ax5.legend(fontsize=8, loc='upper right')
ax5.grid(True, alpha=0.3)

# --- Panel (f): c_BA sound velocity ---
ax6 = fig.add_subplot(gs[2, 1])
ax6.plot(tau_values, c_BA, 'k-', linewidth=2, label='$c_{BA}$')
ax6.axvline(tau_fold, color='gray', linestyle='--', alpha=0.5, label=f'fold')
ax6.set_xlabel('$\\tau$', fontsize=11)
ax6.set_ylabel('$c_{BA}$ [$M_{KK}$]', fontsize=11)
ax6.set_title('(f) BA Sound Velocity', fontsize=12, fontweight='bold')
ax6.legend(fontsize=9)
ax6.grid(True, alpha=0.3)

fig.suptitle('BA-SPECTRUM-56: Bogoliubov-Anderson Phonon Spectrum\n32-Cell CG Graph, $\\Delta = 0.4643$ $M_{KK}$',
             fontsize=14, fontweight='bold', y=0.98)

plt.savefig('computations/session-56/s56_ba_spectrum.png', dpi=150, bbox_inches='tight')
print("Saved: computations/session-56/s56_ba_spectrum.png")

# =============================================================================
# 10. Summary for gate verdict
# =============================================================================

print("\n" + "="*72)
print("BA-SPECTRUM-56 SUMMARY")
print("="*72)
print(f"  N_cells = {N_cells}, N_BA_modes = {N_cells - 1}")
print(f"  Delta = {Delta:.4f} M_KK (OES gap)")
print(f"  Graph Laplacian: lambda_1 = {laplacian_eigs[1]:.4f}, lambda_31 = {laplacian_eigs[-1]:.4f}")
print(f"")
print(f"  AT FOLD (tau = {tau_values[idx_fold]:.4f}):")
print(f"    E_J = {E_J_arr[idx_fold]:.4f} M_KK")
print(f"    E_c = {E_c_arr[idx_fold]:.6f} M_KK")
print(f"    E_J/E_c = {ratio_EJ_Ec[idx_fold]:.1f} (SUPERFLUID)")
print(f"    omega_1 = {omega_BA[idx_fold, 0]:.4f} M_KK (Fiedler mode)")
print(f"    omega_31 = {omega_BA[idx_fold, -1]:.4f} M_KK (max mode)")
print(f"    BW_BA = {BW_BA[idx_fold]:.4f} M_KK")
print(f"    T_GH = {T_GH[idx_fold]:.4f} M_KK")
print(f"    omega_1/T_GH = {omega_BA[idx_fold, 0]/T_GH[idx_fold]:.1f}")
print(f"    c_BA = {c_BA[idx_fold]:.4f} M_KK")
print(f"    F_BA = {F_BA[idx_fold]:.4f} M_KK")
print(f"    F_ZPE = {F_ZPE[idx_fold]:.4f} M_KK")
print(f"    F_thermal = {F_thermal[idx_fold]:.6f} M_KK")
print(f"")
print(f"  GLOBAL:")
print(f"    F_BA global min = {F_global_min:.4f} at tau = {tau_global_min:.4f}")
print(f"    F_BA at tau=0: {F_BA[0]:.4f}")
print(f"    F_BA at tau=0.5: {F_BA[-1]:.4f}")
print(f"    Interior min in [0.10, 0.30]: {has_minimum}")
if has_minimum:
    print(f"    Min location: tau = {tau_min_range:.4f}, depth = {depth:.6f}")
print(f"    F_BA is {'NOT ' if len(sign_changes) > 0 else ''}monotonic")
print(f"    dF sign changes: {len(sign_changes)}")
if len(sign_changes) > 0:
    for sc in sign_changes:
        print(f"      at tau ~ {0.5*(tau_values[sc]+tau_values[sc+1]):.4f}")
print(f"")
print(f"  REGIME:")
print(f"    E_J/E_c > 1 at ALL tau: {np.all(ratio_EJ_Ec > 1)}")
print(f"    omega_1 > T_GH at ALL tau: {np.all(omega_BA[:, 0] > T_GH)}")
print(f"    => Deep quantum regime (not thermally populated)")
print(f"")
print(f"  GATE VERDICT: BA-SPECTRUM-56 = INFO")
print("="*72)
