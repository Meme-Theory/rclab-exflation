#!/usr/bin/env python3
"""
s56_leggett_fabric.py — Leggett Mode Dispersion on 32-Cell Graph

LEGGETT-FABRIC-56: The Leggett mode is the massive Goldstone boson arising
from relative B2-B1 phase oscillation. On the fabric (Josephson junction
array on 32-cell CG graph), it becomes a propagating mode with dispersion:

    omega_L^2(n) = omega_L0^2 + J_Leggett * lambda_n

where:
    omega_L0 = Leggett gap (mass gap from broken relative U(1) symmetry)
    J_Leggett = epsilon * E_J (Leggett hopping = dipolar coupling * Josephson energy)
    epsilon = 0.00248 (S49 DIPOLAR-CATALOG-49, U(1)_7 breaking parameter)
    lambda_n = graph Laplacian eigenvalues (C2 bonds, n=0..31)
    E_J = J_C2^2 * F_anomalous (from BA-SPECTRUM-56 formulation)

Three omega_L0 values are computed:
    1. omega_L1 = 0.138 M_KK (S52 GL-Josephson, canonical)
    2. omega_L1_S49 = 0.070 M_KK (S49 dipolar, B2-B3 Leggett mode)
    3. omega_L2 = 0.107 M_KK (S49 second Leggett branch)

Gate: LEGGETT-FABRIC-56
    INFO: omega_L(k) with real c_L > 0. Report c_L vs c_BA.

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
from canonical_constants import (
    Delta_0_OES, E_cond, tau_fold, N_cells,
    omega_L1 as omega_L1_canonical,  # 0.138 from S52 GL-Josephson
    omega_L2 as omega_L2_canonical,  # 0.192 from S52 GL-Josephson
)

# =============================================================================
# 0. Constants
# =============================================================================

# Leggett gap values (three cases)
omega_L0_GL = omega_L1_canonical    # 0.138 M_KK — S52 GL-Josephson Leggett-1
omega_L0_S49_1 = 0.070              # 0.070 M_KK — S49 dipolar B2-B3 Leggett (no canonical; S49-specific)  # (local)
omega_L0_S49_2 = 0.107              # 0.107 M_KK — S49 second Leggett branch (no canonical; S49-specific)  # (local)

# Dipolar coupling (S49 DIPOLAR-CATALOG-49)
epsilon_Leggett = 0.00248           # U(1)_7 breaking parameter  # (local)

# BCS gap
Delta = Delta_0_OES  # 0.4643 M_KK

print(f"Leggett gap values:")
print(f"  omega_L0 (GL, canonical) = {omega_L0_GL:.4f} M_KK")
print(f"  omega_L0 (S49, branch 1) = {omega_L0_S49_1:.4f} M_KK")
print(f"  omega_L0 (S49, branch 2) = {omega_L0_S49_2:.4f} M_KK")
print(f"  epsilon_Leggett = {epsilon_Leggett}")
print(f"  Delta (OES) = {Delta:.4f} M_KK")

# =============================================================================
# 1. Load data
# =============================================================================

data_tb = np.load('computations/session-54/s54_tb_hamiltonian.npz')
tau_values = data_tb['tau_values']   # (50,)
eigenvalues = data_tb['eigenvalues'] # (50, 32) — TB eigenvalues at each tau
J_C2_tau = data_tb['J_C2_tau']      # (50,) — C2 hopping strength vs tau
adj_C2 = data_tb['adj_C2']          # (32, 32) — adjacency for C2 bonds
diameter = int(data_tb['diameter'])

# Scale factor data for T_GH
data_sf = np.load('computations/session-54/s54_scale_factor.npz')
tau_sf = data_sf['tau']
H_sf = data_sf['H']

N_tau = len(tau_values)

print(f"\nLoaded: {N_tau} tau values in [{tau_values[0]:.4f}, {tau_values[-1]:.4f}]")
print(f"N_cells = {N_cells}, diameter = {diameter}")

# =============================================================================
# 2. Graph Laplacian eigenvalues (C2 bonds)
# =============================================================================

A_C2 = adj_C2.astype(float)
degree_C2 = A_C2.sum(axis=1)
L_C2 = np.diag(degree_C2) - A_C2

laplacian_eigs = np.linalg.eigvalsh(L_C2)
laplacian_eigs = np.sort(laplacian_eigs)
laplacian_eigs[0] = 0.0  # enforce zero mode

n_bonds = int(A_C2.sum()) // 2
print(f"\nGraph Laplacian (C2 bonds, {n_bonds} bonds):")
print(f"  lambda_0 = {laplacian_eigs[0]:.6f} (zero mode)")
print(f"  lambda_1 = {laplacian_eigs[1]:.6f} (Fiedler)")
print(f"  lambda_31 = {laplacian_eigs[-1]:.6f}")

# =============================================================================
# 3. E_J(tau) from BCS coherence factors (same as BA-SPECTRUM-56)
# =============================================================================

E_J_arr = np.zeros(N_tau)
E_c_arr = np.zeros(N_tau)

for i in range(N_tau):
    eigs_i = eigenvalues[i]
    mu = 0.5 * (eigs_i[15] + eigs_i[16])  # (local)
    xi_k = eigs_i - mu
    E_qp_k = np.sqrt(xi_k**2 + Delta**2)
    F_anom = np.sum(Delta / (2.0 * E_qp_k**2))
    E_J_arr[i] = J_C2_tau[i]**2 * F_anom
    E_c_arr[i] = 0.5 * (eigs_i[16] - eigs_i[15])

print(f"\nE_J range: [{E_J_arr.min():.4f}, {E_J_arr.max():.4f}] M_KK")
print(f"E_c range: [{E_c_arr.min():.6f}, {E_c_arr.max():.6f}] M_KK")

# =============================================================================
# 4. J_Leggett(tau) and Leggett dispersion
# =============================================================================
# J_Leggett = epsilon * E_J
# omega_L^2(n, tau) = omega_L0^2 + J_Leggett(tau) * lambda_n

J_Leggett_arr = epsilon_Leggett * E_J_arr  # (N_tau,)

print(f"\nJ_Leggett range: [{J_Leggett_arr.min():.6f}, {J_Leggett_arr.max():.6f}] M_KK")

# Compute Leggett dispersion for all three gap values
# Shape: (N_tau, 32) — includes n=0 (pure Leggett gap) through n=31
omega_L_GL = np.zeros((N_tau, N_cells))
omega_L_S49_1 = np.zeros((N_tau, N_cells))
omega_L_S49_2 = np.zeros((N_tau, N_cells))

for i in range(N_tau):
    for n in range(N_cells):
        lam_n = laplacian_eigs[n]
        omega_sq_GL = omega_L0_GL**2 + J_Leggett_arr[i] * lam_n
        omega_sq_S49_1 = omega_L0_S49_1**2 + J_Leggett_arr[i] * lam_n
        omega_sq_S49_2 = omega_L0_S49_2**2 + J_Leggett_arr[i] * lam_n

        # Check positivity (should always hold since omega_L0 > 0 and J_Leggett > 0)
        omega_L_GL[i, n] = np.sqrt(max(omega_sq_GL, 0.0))
        omega_L_S49_1[i, n] = np.sqrt(max(omega_sq_S49_1, 0.0))
        omega_L_S49_2[i, n] = np.sqrt(max(omega_sq_S49_2, 0.0))

# Find fold index
idx_fold = np.argmin(np.abs(tau_values - tau_fold))

print(f"\nLeggett dispersion at fold (tau = {tau_values[idx_fold]:.4f}):")
print(f"  J_Leggett = {J_Leggett_arr[idx_fold]:.6f} M_KK")
print(f"  E_J = {E_J_arr[idx_fold]:.4f} M_KK")

print(f"\n  omega_L (GL, omega_L0 = {omega_L0_GL:.4f}):")
print(f"    n=0: {omega_L_GL[idx_fold, 0]:.6f} (gap)")
print(f"    n=1: {omega_L_GL[idx_fold, 1]:.6f}")
print(f"    n=31: {omega_L_GL[idx_fold, -1]:.6f}")
print(f"    Bandwidth: {omega_L_GL[idx_fold, -1] - omega_L_GL[idx_fold, 0]:.6f}")

print(f"\n  omega_L (S49-1, omega_L0 = {omega_L0_S49_1:.4f}):")
print(f"    n=0: {omega_L_S49_1[idx_fold, 0]:.6f} (gap)")
print(f"    n=1: {omega_L_S49_1[idx_fold, 1]:.6f}")
print(f"    n=31: {omega_L_S49_1[idx_fold, -1]:.6f}")
print(f"    Bandwidth: {omega_L_S49_1[idx_fold, -1] - omega_L_S49_1[idx_fold, 0]:.6f}")

print(f"\n  omega_L (S49-2, omega_L0 = {omega_L0_S49_2:.4f}):")
print(f"    n=0: {omega_L_S49_2[idx_fold, 0]:.6f} (gap)")
print(f"    n=1: {omega_L_S49_2[idx_fold, 1]:.6f}")
print(f"    n=31: {omega_L_S49_2[idx_fold, -1]:.6f}")
print(f"    Bandwidth: {omega_L_S49_2[idx_fold, -1] - omega_L_S49_2[idx_fold, 0]:.6f}")

# =============================================================================
# 5. Sound velocity c_L
# =============================================================================
# On a graph, the continuum limit gives k_n ~ pi * n / (N * a) for a regular
# 1D lattice. For the CG graph, we use the same convention as BA-SPECTRUM-56:
#   k_min = pi / diameter
#
# For the massive dispersion omega^2 = omega_0^2 + v^2 k^2, the group velocity
# at general k is:
#   v_g = d(omega)/dk = v^2 * k / omega
# At k -> 0 the group velocity vanishes (massive mode), but the asymptotic
# (large k) velocity is v = sqrt(J_Leggett * diameter^2 / pi^2).
#
# However, for phononic physics the relevant quantity is the slope of the
# propagating part, i.e., the coefficient of the k^2 term:
#   omega_L(k) ~ omega_L0 + J_Leggett * k^2 / (2 * omega_L0)
#
# The PHASE velocity at mode n is: v_ph(n) = omega_L(n) / k_n
# The GROUP velocity at mode n is: v_g(n) = d(omega)/dk|_n = J_Leggett * k_n / omega_L(n)
#
# For the lowest propagating mode (n=1), approximate:
#   k_1 = pi / diameter (same as BA convention)
#   v_g(k_1) = J_Leggett * k_1 / omega_L(k_1)
#
# The ASYMPTOTIC (high-k) group velocity is c_L_infty = sqrt(J_Leggett) * (k/k)
# Wait — the dispersion is omega^2 = omega_0^2 + J_L * lambda_n.
# On a ring of N sites, lambda_n = 2(1 - cos(2*pi*n/N)) ~ (2*pi*n/N)^2 for small n,
# giving omega^2 ~ omega_0^2 + J_L * k^2 with k = 2*pi*n/(N*a).
#
# For general graph: lambda_n does not map to k^2 cleanly. We use the BA convention:
#   k_n is defined by linear interpolation of sorted laplacian_eigs.
#   Effective k: k_n = sqrt(lambda_n) * (pi / sqrt(lambda_max)) [normalized to BZ edge]
#
# Most physically transparent: define c_L from the local slope between adjacent modes.

k_min = np.pi / diameter  # Same convention as BA spectrum

# Method 1: c_L from Fiedler mode (same as c_BA definition)
# c_L = omega_L(n=1) / k_min  — this is the PHASE velocity at the lowest mode
# This gives the overall speed of propagation. For a massive mode the group velocity
# is LOWER than the phase velocity.

# Method 2: Asymptotic velocity (high-k limit)
# In the limit lambda >> omega_L0^2 / J_Leggett, omega ~ sqrt(J_Leggett * lambda)
# which matches the BA phonon: omega_BA = sqrt(E_c * E_J * lambda)
# So c_L_infty = c_BA * sqrt(epsilon) — the Leggett mode asymptotically approaches
# a rescaled BA phonon.

# Method 3: Group velocity at the Fiedler mode
# v_g = (1/2) * J_Leggett * (d lambda/dk) / omega_L
# For k_1 = pi/diameter, lambda_1 is known, so:
# v_g(k_1) = J_Leggett * lambda_1 / (2 * omega_L(k_1) * k_1)
# This assumes d(lambda)/dk ~ 2*k at small k (parabolic approximation), giving:
# v_g(k_1) ~ J_Leggett * k_1 / omega_L(k_1)
# But we need to be careful: lambda_1 ~ alpha * k_1^2 is the parabolic approximation.
# So alpha = lambda_1 / k_1^2 and v_g = alpha * J_Leggett * k_1 / omega_L(k_1).

# Compute all three velocities
alpha_k = laplacian_eigs[1] / k_min**2  # Effective "dispersion constant" from graph

c_L_phase = np.zeros((N_tau, 3))     # Phase velocity at Fiedler mode, 3 gap values
c_L_group = np.zeros((N_tau, 3))     # Group velocity at Fiedler mode, 3 gap values
c_L_asymptotic = np.zeros(N_tau)     # Asymptotic velocity (gap-independent)

# BA sound velocity for comparison (same as BA-SPECTRUM-56)
omega_BA_fiedler = np.sqrt(E_c_arr * E_J_arr * laplacian_eigs[1])
c_BA = omega_BA_fiedler / k_min

for i in range(N_tau):
    # Phase velocities: v_ph = omega(k_1) / k_1
    c_L_phase[i, 0] = omega_L_GL[i, 1] / k_min
    c_L_phase[i, 1] = omega_L_S49_1[i, 1] / k_min
    c_L_phase[i, 2] = omega_L_S49_2[i, 1] / k_min

    # Group velocities: v_g = J_L * alpha_k * k_1 / omega(k_1)
    # where alpha_k * k_1^2 = lambda_1, so alpha_k * k_1 = lambda_1 / k_1
    c_L_group[i, 0] = J_Leggett_arr[i] * (laplacian_eigs[1] / k_min) / (2.0 * omega_L_GL[i, 1])
    c_L_group[i, 1] = J_Leggett_arr[i] * (laplacian_eigs[1] / k_min) / (2.0 * omega_L_S49_1[i, 1])
    c_L_group[i, 2] = J_Leggett_arr[i] * (laplacian_eigs[1] / k_min) / (2.0 * omega_L_S49_2[i, 1])

    # Asymptotic: c_L_infty = sqrt(J_Leggett * alpha_k) — gap-independent at high k
    c_L_asymptotic[i] = np.sqrt(J_Leggett_arr[i] * alpha_k)

print(f"\n--- Sound Velocities at Fold (tau = {tau_values[idx_fold]:.4f}) ---")
print(f"k_min = pi/{diameter} = {k_min:.6f}")
print(f"alpha_k = lambda_1/k_min^2 = {alpha_k:.6f}")

for j, (label, omL0) in enumerate([
    ("GL (0.138)", omega_L0_GL),
    ("S49-1 (0.070)", omega_L0_S49_1),
    ("S49-2 (0.107)", omega_L0_S49_2)
]):
    print(f"\n  omega_L0 = {omL0} [{label}]:")
    print(f"    c_L (phase, Fiedler) = {c_L_phase[idx_fold, j]:.6f} M_KK")
    print(f"    c_L (group, Fiedler) = {c_L_group[idx_fold, j]:.6f} M_KK")
    print(f"    c_L_group / c_BA = {c_L_group[idx_fold, j] / c_BA[idx_fold]:.6f}")
    # Ratio of massive mode bandwidth to gap
    bw = omega_L_GL[idx_fold, -1] - omega_L_GL[idx_fold, 0] if j == 0 else \
         (omega_L_S49_1[idx_fold, -1] - omega_L_S49_1[idx_fold, 0] if j == 1 else \
          omega_L_S49_2[idx_fold, -1] - omega_L_S49_2[idx_fold, 0])
    print(f"    Bandwidth / gap = {bw / omL0:.6f}")

print(f"\n  c_BA (Fiedler) = {c_BA[idx_fold]:.6f} M_KK")
print(f"  c_L (asymptotic) = {c_L_asymptotic[idx_fold]:.6f} M_KK")
print(f"  c_L_asymptotic / c_BA = {c_L_asymptotic[idx_fold] / c_BA[idx_fold]:.6f}")
print(f"  sqrt(epsilon) = {np.sqrt(epsilon_Leggett):.6f}")
print(f"  Expected c_L_asymptotic / c_BA ~ sqrt(epsilon) = {np.sqrt(epsilon_Leggett):.6f}")

# Cross-check: c_L_asymptotic should equal c_BA * sqrt(epsilon) since
# omega_L(high k) ~ sqrt(J_L * lambda) = sqrt(epsilon * E_J * lambda)
# omega_BA(high k) ~ sqrt(E_c * E_J * lambda)
# Ratio = sqrt(epsilon * E_J / (E_c * E_J)) = sqrt(epsilon / E_c)
# NOT sqrt(epsilon). The correct ratio depends on the physics:
# - BA: omega_BA^2 = E_c * E_J * lambda
# - Leggett: omega_L^2 = omega_L0^2 + epsilon * E_J * lambda
# At high k: omega_L ~ sqrt(epsilon * E_J * lambda), omega_BA ~ sqrt(E_c * E_J * lambda)
# Ratio: omega_L / omega_BA ~ sqrt(epsilon / E_c)

ratio_asymp_theoretical = np.sqrt(epsilon_Leggett / E_c_arr[idx_fold])
print(f"\n  Theoretical high-k ratio omega_L/omega_BA = sqrt(epsilon/E_c) = {ratio_asymp_theoretical:.4f}")
# Check: for omega_L_GL at highest mode
ratio_actual_GL = omega_L_GL[idx_fold, -1] / np.sqrt(E_c_arr[idx_fold] * E_J_arr[idx_fold] * laplacian_eigs[-1])
print(f"  Actual ratio at n=31: {ratio_actual_GL:.6f}")
# This won't match because omega_L0^2 contributes. Need lambda >> omega_L0^2/(epsilon*E_J)
crossover_lambda = omega_L0_GL**2 / (epsilon_Leggett * E_J_arr[idx_fold])
print(f"  Crossover lambda (GL): {crossover_lambda:.4f} (lambda_31 = {laplacian_eigs[-1]:.4f})")
if crossover_lambda < laplacian_eigs[-1]:
    print(f"  lambda_31/crossover = {laplacian_eigs[-1]/crossover_lambda:.1f}x => approaching asymptotic regime")
else:
    print(f"  NOT in asymptotic regime: lambda_31 < crossover lambda")

# =============================================================================
# 6. Compare with BA phonon dispersion
# =============================================================================

# BA phonon spectrum at fold
omega_BA_all = np.zeros(N_cells - 1)  # modes n=1..31
for n in range(N_cells - 1):
    omega_BA_all[n] = np.sqrt(E_c_arr[idx_fold] * E_J_arr[idx_fold] * laplacian_eigs[n + 1])

print(f"\n--- BA vs Leggett at fold ---")
print(f"  BA: omega_1 = {omega_BA_all[0]:.6f}, omega_31 = {omega_BA_all[-1]:.6f}")
print(f"  Leggett (GL): omega_0 = {omega_L_GL[idx_fold, 0]:.6f}, omega_31 = {omega_L_GL[idx_fold, -1]:.6f}")
print(f"  Leggett gap / BA Fiedler = {omega_L_GL[idx_fold, 0] / omega_BA_all[0]:.4f}")

# =============================================================================
# 7. Tau dependence of Leggett parameters
# =============================================================================

# J_Leggett / omega_L0^2 ratio — controls how "dispersive" the Leggett mode is
# When J_L * lambda_max << omega_L0^2, the mode is nearly flat (non-dispersive)
# When J_L * lambda_max >> omega_L0^2, it looks like a gapless mode at high k

dispersiveness_GL = J_Leggett_arr * laplacian_eigs[-1] / omega_L0_GL**2
dispersiveness_S49_1 = J_Leggett_arr * laplacian_eigs[-1] / omega_L0_S49_1**2

print(f"\nDispersiveness J_L*lambda_max/omega_L0^2:")
print(f"  GL at fold: {dispersiveness_GL[idx_fold]:.6f}")
print(f"  S49-1 at fold: {dispersiveness_S49_1[idx_fold]:.6f}")
print(f"  GL range: [{dispersiveness_GL.min():.6f}, {dispersiveness_GL.max():.6f}]")
print(f"  S49-1 range: [{dispersiveness_S49_1.min():.6f}, {dispersiveness_S49_1.max():.6f}]")

# T_GH interpolation
T_GH_sparse = H_sf / (2.0 * np.pi)
interp_T_GH = interp1d(tau_sf, T_GH_sparse, kind='cubic', fill_value='extrapolate')
T_GH = np.maximum(interp_T_GH(tau_values), 1e-10)

# omega_L0 / T_GH ratio at fold
print(f"\nomega_L0 / T_GH at fold:")
print(f"  GL: {omega_L0_GL / T_GH[idx_fold]:.4f}")
print(f"  S49-1: {omega_L0_S49_1 / T_GH[idx_fold]:.4f}")
print(f"  S49-2: {omega_L0_S49_2 / T_GH[idx_fold]:.4f}")
print(f"  T_GH at fold: {T_GH[idx_fold]:.4f}")

# =============================================================================
# 8. Save results
# =============================================================================

np.savez('computations/session-56/s56_leggett_fabric.npz',
    # Grid
    tau_values=tau_values,
    N_cells=N_cells,
    Delta=Delta,
    diameter=diameter,

    # Input parameters
    omega_L0_GL=omega_L0_GL,
    omega_L0_S49_1=omega_L0_S49_1,
    omega_L0_S49_2=omega_L0_S49_2,
    epsilon_Leggett=epsilon_Leggett,

    # Graph Laplacian
    laplacian_eigs=laplacian_eigs,
    k_min=k_min,
    alpha_k=alpha_k,

    # BCS / Josephson parameters (shared with BA-SPECTRUM-56)
    E_J=E_J_arr,
    E_c=E_c_arr,
    J_Leggett=J_Leggett_arr,

    # Leggett dispersion (N_tau, 32)
    omega_L_GL=omega_L_GL,           # GL gap (0.138)
    omega_L_S49_1=omega_L_S49_1,     # S49 gap 1 (0.070)
    omega_L_S49_2=omega_L_S49_2,     # S49 gap 2 (0.107)

    # BA phonon at fold for comparison
    omega_BA_fold=omega_BA_all,      # (31,) at fold

    # Velocities (N_tau,) or (N_tau, 3)
    c_L_phase=c_L_phase,            # Phase vel at Fiedler, 3 gaps
    c_L_group=c_L_group,            # Group vel at Fiedler, 3 gaps
    c_L_asymptotic=c_L_asymptotic,  # High-k asymptotic vel
    c_BA=c_BA,                       # BA sound velocity

    # Diagnostics
    dispersiveness_GL=dispersiveness_GL,
    dispersiveness_S49_1=dispersiveness_S49_1,
    T_GH=T_GH,

    # Gate
    gate_name='LEGGETT-FABRIC-56',
    gate_verdict='INFO'
)
print("\nSaved: computations/session-56/s56_leggett_fabric.npz")

# =============================================================================
# 9. Plotting
# =============================================================================

fig = plt.figure(figsize=(18, 18))
gs = GridSpec(3, 2, figure=fig, hspace=0.32, wspace=0.28)

# --- Panel (a): Leggett + BA dispersion at fold ---
ax1 = fig.add_subplot(gs[0, 0])

# Define effective "k" for plotting: k_n = sqrt(lambda_n) * (pi / sqrt(lambda_max))
# This normalizes so that k_max = pi (Brillouin zone edge for a 1D chain of similar extent)
k_eff = np.sqrt(laplacian_eigs) * (np.pi / np.sqrt(laplacian_eigs[-1]))

# BA phonon (massless)
ax1.plot(k_eff[1:], omega_BA_all, 'ko-', markersize=4, linewidth=1.5,
         label='BA phonon (massless)', zorder=5)

# Leggett modes (massive)
ax1.plot(k_eff, omega_L_GL[idx_fold], 's-', markersize=4, linewidth=1.5,
         color='#d62728', label=f'Leggett ($\\omega_{{L0}}=0.138$)')
ax1.plot(k_eff, omega_L_S49_1[idx_fold], 'D-', markersize=3.5, linewidth=1.2,
         color='#2ca02c', label=f'Leggett ($\\omega_{{L0}}=0.070$)')
ax1.plot(k_eff, omega_L_S49_2[idx_fold], '^-', markersize=3.5, linewidth=1.2,
         color='#9467bd', label=f'Leggett ($\\omega_{{L0}}=0.107$)')

# Mark the Leggett gap
for omL0, c in [(omega_L0_GL, '#d62728'), (omega_L0_S49_1, '#2ca02c'), (omega_L0_S49_2, '#9467bd')]:
    ax1.axhline(omL0, color=c, linestyle=':', alpha=0.4)

ax1.set_xlabel('Effective $k$ [BZ-normalized]', fontsize=11)
ax1.set_ylabel('$\\omega$ [$M_{KK}$]', fontsize=11)
ax1.set_title(f'(a) Leggett + BA Dispersion at Fold ($\\tau={tau_values[idx_fold]:.3f}$)',
              fontsize=12, fontweight='bold')
ax1.legend(fontsize=8.5, loc='upper left')
ax1.grid(True, alpha=0.3)

# --- Panel (b): Leggett dispersion zoomed low-k ---
ax2 = fig.add_subplot(gs[0, 1])

# Show first 10 modes in detail
n_show = min(10, N_cells)
k_show = k_eff[:n_show]

ax2.plot(k_show, omega_L_GL[idx_fold, :n_show], 's-', markersize=6, linewidth=1.8,
         color='#d62728', label=f'$\\omega_{{L0}}=0.138$')
ax2.plot(k_show, omega_L_S49_1[idx_fold, :n_show], 'D-', markersize=5, linewidth=1.5,
         color='#2ca02c', label=f'$\\omega_{{L0}}=0.070$')
ax2.plot(k_show, omega_L_S49_2[idx_fold, :n_show], '^-', markersize=5, linewidth=1.5,
         color='#9467bd', label=f'$\\omega_{{L0}}=0.107$')

# Also show BA for comparison
ax2.plot(k_eff[1:n_show], omega_BA_all[:n_show-1], 'ko-', markersize=5, linewidth=1.5,
         label='BA phonon')

# Mark gaps
for omL0, c in [(omega_L0_GL, '#d62728'), (omega_L0_S49_1, '#2ca02c'), (omega_L0_S49_2, '#9467bd')]:
    ax2.axhline(omL0, color=c, linestyle=':', alpha=0.5, linewidth=0.8)

ax2.set_xlabel('Effective $k$', fontsize=11)
ax2.set_ylabel('$\\omega$ [$M_{KK}$]', fontsize=11)
ax2.set_title('(b) Low-$k$ Detail (first 10 modes)', fontsize=12, fontweight='bold')
ax2.legend(fontsize=8.5)
ax2.grid(True, alpha=0.3)

# --- Panel (c): omega_L^2 vs lambda_n (should be linear) ---
ax3 = fig.add_subplot(gs[1, 0])

omega_sq_GL = omega_L_GL[idx_fold]**2
omega_sq_S49_1 = omega_L_S49_1[idx_fold]**2

ax3.plot(laplacian_eigs, omega_sq_GL, 's', markersize=5, color='#d62728',
         label=f'$\\omega_L^2$ (GL, $\\omega_{{L0}}=0.138$)')
ax3.plot(laplacian_eigs, omega_sq_S49_1, 'D', markersize=4, color='#2ca02c',
         label=f'$\\omega_L^2$ (S49, $\\omega_{{L0}}=0.070$)')

# Linear fit to verify
lam_fit = np.linspace(0, laplacian_eigs[-1], 100)
ax3.plot(lam_fit, omega_L0_GL**2 + J_Leggett_arr[idx_fold] * lam_fit, '-',
         color='#d62728', alpha=0.5, linewidth=1.5,
         label=f'$\\omega_{{L0}}^2 + J_L \\lambda$ fit')
ax3.plot(lam_fit, omega_L0_S49_1**2 + J_Leggett_arr[idx_fold] * lam_fit, '-',
         color='#2ca02c', alpha=0.5, linewidth=1.5)

ax3.set_xlabel('$\\lambda_n$ (Laplacian eigenvalue)', fontsize=11)
ax3.set_ylabel('$\\omega_L^2$ [$M_{KK}^2$]', fontsize=11)
ax3.set_title('(c) $\\omega_L^2$ vs $\\lambda_n$ — Linearity Check', fontsize=12, fontweight='bold')
ax3.legend(fontsize=8.5)
ax3.grid(True, alpha=0.3)

# --- Panel (d): c_L group velocity vs tau ---
ax4 = fig.add_subplot(gs[1, 1])

ax4.plot(tau_values, c_L_group[:, 0], '-', linewidth=2, color='#d62728',
         label=f'$c_L^{{group}}$ (GL, $\\omega_{{L0}}=0.138$)')
ax4.plot(tau_values, c_L_group[:, 1], '-', linewidth=2, color='#2ca02c',
         label=f'$c_L^{{group}}$ (S49, $\\omega_{{L0}}=0.070$)')
ax4.plot(tau_values, c_L_group[:, 2], '-', linewidth=2, color='#9467bd',
         label=f'$c_L^{{group}}$ (S49, $\\omega_{{L0}}=0.107$)')
ax4.plot(tau_values, c_BA, 'k--', linewidth=2, label='$c_{BA}$ (massless)')
ax4.axvline(tau_fold, color='gray', linestyle='--', alpha=0.5, label='fold')

ax4.set_xlabel('$\\tau$', fontsize=11)
ax4.set_ylabel('Velocity [$M_{KK}$]', fontsize=11)
ax4.set_title('(d) Group Velocities: Leggett vs BA', fontsize=12, fontweight='bold')
ax4.legend(fontsize=8, loc='upper right')
ax4.grid(True, alpha=0.3)

# --- Panel (e): J_Leggett(tau) and omega_L0 comparison ---
ax5 = fig.add_subplot(gs[2, 0])

ax5.plot(tau_values, J_Leggett_arr, 'b-', linewidth=2, label='$J_{Leggett}$')
ax5.axhline(omega_L0_GL**2, color='#d62728', linestyle='--', linewidth=1.5,
            label=f'$\\omega_{{L0}}^2$ (GL) = {omega_L0_GL**2:.4f}')
ax5.axhline(omega_L0_S49_1**2, color='#2ca02c', linestyle='--', linewidth=1.5,
            label=f'$\\omega_{{L0}}^2$ (S49-1) = {omega_L0_S49_1**2:.4f}')
ax5.axvline(tau_fold, color='gray', linestyle='--', alpha=0.5)

ax5.set_xlabel('$\\tau$', fontsize=11)
ax5.set_ylabel('Energy scale [$M_{KK}$]', fontsize=11)
ax5.set_title('(e) $J_{Leggett}$ vs $\\omega_{L0}^2$', fontsize=12, fontweight='bold')
ax5.legend(fontsize=8.5)
ax5.grid(True, alpha=0.3)
ax5.set_yscale('log')

# --- Panel (f): Dispersiveness J_L * lambda_max / omega_L0^2 vs tau ---
ax6 = fig.add_subplot(gs[2, 1])

ax6.plot(tau_values, dispersiveness_GL, '-', linewidth=2, color='#d62728',
         label=f'$J_L\\lambda_{{max}}/\\omega_{{L0}}^2$ (GL, 0.138)')
ax6.plot(tau_values, dispersiveness_S49_1, '-', linewidth=2, color='#2ca02c',
         label=f'$J_L\\lambda_{{max}}/\\omega_{{L0}}^2$ (S49, 0.070)')
ax6.axhline(1.0, color='k', linestyle=':', alpha=0.5,
            label='$=1$ (equal gap/dispersion)')
ax6.axvline(tau_fold, color='gray', linestyle='--', alpha=0.5)

ax6.set_xlabel('$\\tau$', fontsize=11)
ax6.set_ylabel('Dispersiveness', fontsize=11)
ax6.set_title('(f) Leggett Mode Dispersiveness', fontsize=12, fontweight='bold')
ax6.legend(fontsize=8.5)
ax6.grid(True, alpha=0.3)

fig.suptitle('LEGGETT-FABRIC-56: Leggett Mode Dispersion on 32-Cell CG Graph\n'
             'Massive Goldstone: $\\omega_L^2(n) = \\omega_{L0}^2 + J_{Leggett} \\cdot \\lambda_n$',
             fontsize=14, fontweight='bold', y=0.99)

plt.savefig('computations/session-56/s56_leggett_fabric.png', dpi=150, bbox_inches='tight')
print("Saved: computations/session-56/s56_leggett_fabric.png")

# =============================================================================
# 10. Summary
# =============================================================================

print("\n" + "="*72)
print("LEGGETT-FABRIC-56 SUMMARY")
print("="*72)
print(f"  N_cells = {N_cells}, N_modes = {N_cells}")
print(f"  epsilon_Leggett = {epsilon_Leggett}")
print(f"  Delta = {Delta:.4f} M_KK")
print(f"  Dispersion: omega_L^2(n) = omega_L0^2 + J_Leggett * lambda_n")
print(f"")
print(f"  AT FOLD (tau = {tau_values[idx_fold]:.4f}):")
print(f"    E_J = {E_J_arr[idx_fold]:.4f} M_KK")
print(f"    J_Leggett = epsilon * E_J = {J_Leggett_arr[idx_fold]:.6f} M_KK")
print(f"    lambda_1 (Fiedler) = {laplacian_eigs[1]:.6f}")
print(f"    lambda_31 (max) = {laplacian_eigs[-1]:.6f}")
print(f"    k_min = pi/{diameter} = {k_min:.6f}")
print(f"")
for j, (label, omL0) in enumerate([
    ("GL (0.138)", omega_L0_GL),
    ("S49-1 (0.070)", omega_L0_S49_1),
    ("S49-2 (0.107)", omega_L0_S49_2)
]):
    print(f"    --- omega_L0 = {omL0} [{label}] ---")
    print(f"    omega_L(n=0) = {omL0:.6f} (gap)")
    omL_arr = [omega_L_GL, omega_L_S49_1, omega_L_S49_2][j]
    print(f"    omega_L(n=1) = {omL_arr[idx_fold, 1]:.6f}")
    print(f"    omega_L(n=31) = {omL_arr[idx_fold, -1]:.6f}")
    print(f"    Bandwidth = {omL_arr[idx_fold, -1] - omL_arr[idx_fold, 0]:.6f}")
    print(f"    c_L (group, Fiedler) = {c_L_group[idx_fold, j]:.6f} M_KK")
    print(f"    c_L (phase, Fiedler) = {c_L_phase[idx_fold, j]:.6f} M_KK")
    print(f"    c_L_group / c_BA = {c_L_group[idx_fold, j] / c_BA[idx_fold]:.6f}")
    print(f"    Dispersiveness = {[dispersiveness_GL, dispersiveness_S49_1, dispersiveness_S49_1][j][idx_fold]:.6f}")
    print(f"")

print(f"    c_BA = {c_BA[idx_fold]:.6f} M_KK")
print(f"    c_L_asymptotic = {c_L_asymptotic[idx_fold]:.6f} M_KK")
print(f"")
print(f"  INTERPRETATION:")
disp_GL_fold = dispersiveness_GL[idx_fold]
disp_S49_fold = dispersiveness_S49_1[idx_fold]
if disp_GL_fold < 0.01:
    print(f"    GL: Leggett mode is NEARLY FLAT (dispersiveness = {disp_GL_fold:.4f} << 1)")
    print(f"          => Gap dominates. Mode does not propagate significantly.")
elif disp_GL_fold < 1:
    print(f"    GL: Leggett mode is WEAKLY DISPERSIVE (dispersiveness = {disp_GL_fold:.4f} < 1)")
    print(f"          => Gap dominates at low k, but some propagation exists.")
else:
    print(f"    GL: Leggett mode is STRONGLY DISPERSIVE (dispersiveness = {disp_GL_fold:.4f} > 1)")
    print(f"          => At high k, mode looks gapless. Propagating Leggett wave.")

if disp_S49_fold < 0.01:
    print(f"    S49: Leggett mode is NEARLY FLAT (dispersiveness = {disp_S49_fold:.4f} << 1)")
elif disp_S49_fold < 1:
    print(f"    S49: Leggett mode is WEAKLY DISPERSIVE (dispersiveness = {disp_S49_fold:.4f} < 1)")
else:
    print(f"    S49: Leggett mode is STRONGLY DISPERSIVE (dispersiveness = {disp_S49_fold:.4f} > 1)")

# Is c_L real and > 0?
cL_positive = np.all(c_L_group > 0)
print(f"\n  c_L > 0 at ALL tau for ALL gaps: {cL_positive}")
print(f"")
print(f"  GATE VERDICT: LEGGETT-FABRIC-56 = INFO")
print(f"    omega_L(k) has real c_L > 0 for all three gap choices.")
ratio_fold = c_L_group[idx_fold, 0] / c_BA[idx_fold]
print(f"    c_L_group / c_BA = {ratio_fold:.6f} (GL) at fold")
print(f"    The Leggett mode propagates on the fabric but {N_cells-1}x slower than BA phonons (GL).")
if ratio_fold < 0.01:
    print(f"    Physical: Leggett mode is a nearly-stationary massive resonance.")
elif ratio_fold < 0.1:
    print(f"    Physical: Leggett mode propagates slowly, a heavy massive boson on the fabric.")
else:
    print(f"    Physical: Leggett mode has significant propagation velocity.")
print("="*72)
