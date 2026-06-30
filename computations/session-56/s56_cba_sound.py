#!/usr/bin/env python3
"""
s56_cba_sound.py — CBA-SOUND-56
Bogoliubov-Anderson sound velocity on the 32-cell CG fabric.

Physics:
  The 32-cell Cayley graph tessellation of SU(3) forms a Josephson junction
  array with quantum rotor Hamiltonian:
      H = -E_J sum_{<ij>} cos(phi_i - phi_j) + E_c sum_i (n_i - n_0)^2

  In the superfluid regime (E_J/E_c >> 1), small phase fluctuations give
  Bogoliubov-Anderson (BA) phonon modes. Expanding cos(delta_phi) ~ 1 - delta_phi^2/2,
  the phase dynamics become:
      E_c * d^2 phi_i / dt^2 = -E_J * sum_j L_{ij} * phi_j
  where L is the graph Laplacian of the CG graph.

  Normal modes: omega_n = sqrt(E_J * E_c * lambda_n), n = 0, 1, ..., 31
  where lambda_n are the graph Laplacian eigenvalues.
  n=0 (lambda_0=0) is the Goldstone mode (uniform phase rotation).

  The Bogoliubov-Anderson sound velocity is defined by the lowest nonzero
  mode and the graph diameter D (longest shortest path):
      c_BA = omega_1 * D / pi

  This is the INTER-CELL acoustic velocity — physically distinct from the
  INTRA-CELL Goldstone velocity c_Gold = 0.915 M_KK.

  E_J(tau) = J_C2(tau)^2 * F_anomalous(tau)  [BCS anomalous density, Method 1]
  E_c(tau) = delta_E_F(tau) / 2               [half the Fermi level spacing]

Gate: CBA-SOUND-56 (INFO)
  c_BA(tau) profile and comparison to c_Gold.
  Flag if c_BA has minimum near fold.

Output:
  s56_cba_sound.npz — full data
  s56_cba_sound.png — plots

Author: quantum-acoustics-theorist
Session: S56, Wave 0
"""

import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

sys.path.insert(0, 'computations')
from canonical_constants import (
    tau_fold, Delta_0_OES, c_Gold, M_KK, PI, N_cells as N_cells_canon
)

# ═══════════════════════════════════════════════════════════════════
#  LOAD DATA
# ═══════════════════════════════════════════════════════════════════
tb = np.load('computations/session-54/s54_tb_hamiltonian.npz', allow_pickle=True)
tau_values = tb['tau_values']       # (50,)
eigenvalues = tb['eigenvalues']     # (50, 32) — tight-binding eigenvalues
J_C2_tau = tb['J_C2_tau']           # (50,)
adj_C2 = tb['adj_C2']              # (32, 32)
bandwidths = tb['bandwidths']       # (50,)
N = int(tb['N_cells'])              # 32
D = int(tb['diameter'])             # 6
n_tau = len(tau_values)

Delta = Delta_0_OES  # BCS gap = 0.4643 M_KK (canonical)

print(f"{'='*72}")
print(f"  CBA-SOUND-56: Bogoliubov-Anderson Sound Velocity on 32-Cell CG Graph")
print(f"{'='*72}")
print(f"N_cells = {N}, Diameter = {D}")
print(f"Delta_BCS = {Delta:.6f} M_KK")
print(f"c_Gold (intra-cell) = {c_Gold:.4f} M_KK")
print(f"tau range: [{tau_values[0]:.4f}, {tau_values[-1]:.4f}], {n_tau} points")

# ═══════════════════════════════════════════════════════════════════
#  STEP 1: Graph Laplacian eigenvalues (tau-independent topology)
# ═══════════════════════════════════════════════════════════════════
deg = np.sum(adj_C2, axis=1).astype(float)
L_graph = np.diag(deg) - adj_C2.astype(float)
lambda_graph = np.sort(np.linalg.eigvalsh(L_graph))

# Verify: lambda_0 = 0 (connected graph)
assert abs(lambda_graph[0]) < 1e-10, f"Graph not connected: lambda_0 = {lambda_graph[0]}"
lambda_1 = lambda_graph[1]
lambda_max = lambda_graph[-1]

print(f"\nGraph Laplacian spectrum:")
print(f"  lambda_0 = {lambda_graph[0]:.2e} (Goldstone, should be 0)")
print(f"  lambda_1 = {lambda_1:.8f} (first nonzero = algebraic connectivity)")
print(f"  lambda_max = {lambda_max:.8f} (spectral radius)")
print(f"  Spectral gap = {lambda_1:.8f}")
print(f"  Bandwidth = {lambda_max - lambda_1:.8f}")

# ═══════════════════════════════════════════════════════════════════
#  STEP 2: E_J(tau) and E_c(tau) at all tau
# ═══════════════════════════════════════════════════════════════════
E_J_tau = np.zeros(n_tau)
E_c_tau = np.zeros(n_tau)
F_anom_tau = np.zeros(n_tau)
mu_tau = np.zeros(n_tau)

for i in range(n_tau):
    J_i = J_C2_tau[i]
    ev_i = eigenvalues[i]  # 32 TB eigenvalues

    # Fermi level: midpoint of two levels straddling half-filling
    mu_i = (ev_i[N // 2 - 1] + ev_i[N // 2]) / 2
    mu_tau[i] = mu_i

    # BCS quasiparticle energies
    xi_i = ev_i - mu_i
    E_k = np.sqrt(xi_i**2 + Delta**2)
    uv_k = Delta / (2.0 * E_k)  # u_k * v_k

    # Anomalous density (Ambegaokar-Baratoff kernel)
    F_anom_i = np.sum(uv_k / E_k)  # = sum Delta/(2*E_k^2)
    F_anom_tau[i] = F_anom_i

    # Josephson coupling per bond (Method 1: BCS anomalous density)
    E_J_tau[i] = J_i**2 * F_anom_i

    # Charging energy: half the Fermi level spacing
    delta_E_F = ev_i[N // 2] - ev_i[N // 2 - 1]
    E_c_tau[i] = max(delta_E_F / 2.0, 1e-15)  # protect against degeneracy

print(f"\nE_J and E_c profiles:")
print(f"  E_J range: [{E_J_tau.min():.6f}, {E_J_tau.max():.6f}] M_KK")
print(f"  E_c range: [{E_c_tau.min():.6f}, {E_c_tau.max():.6f}] M_KK")
print(f"  E_J/E_c range: [{(E_J_tau/E_c_tau).min():.2f}, {(E_J_tau/E_c_tau).max():.2f}]")

# ═══════════════════════════════════════════════════════════════════
#  STEP 3: BA phonon frequencies and sound velocity
# ═══════════════════════════════════════════════════════════════════
# omega_n(tau) = sqrt(E_J(tau) * E_c(tau) * lambda_n)
# 31 nonzero modes (n = 1, ..., 31)
n_modes = N - 1  # 31 nonzero modes
omega_BA = np.zeros((n_tau, n_modes))  # (50, 31)

for i in range(n_tau):
    for n in range(n_modes):
        omega_BA[i, n] = np.sqrt(E_J_tau[i] * E_c_tau[i] * lambda_graph[n + 1])

# BA sound velocity: c_BA = omega_1 * D / pi
omega_1_tau = omega_BA[:, 0]  # lowest nonzero mode
c_BA_tau = omega_1_tau * D / PI

print(f"\nBogoliubov-Anderson sound velocity:")
print(f"  c_BA range: [{c_BA_tau.min():.6f}, {c_BA_tau.max():.6f}] M_KK")
print(f"  c_BA/c_Gold range: [{(c_BA_tau/c_Gold).min():.6f}, {(c_BA_tau/c_Gold).max():.6f}]")

# Find minimum and maximum of c_BA
i_min_cBA = np.argmin(c_BA_tau)
i_max_cBA = np.argmax(c_BA_tau)
tau_min_cBA = tau_values[i_min_cBA]
tau_max_cBA = tau_values[i_max_cBA]

print(f"\n  c_BA minimum: {c_BA_tau[i_min_cBA]:.6f} at tau = {tau_min_cBA:.4f}")
print(f"  c_BA maximum: {c_BA_tau[i_max_cBA]:.6f} at tau = {tau_max_cBA:.4f}")
print(f"  c_BA variation: {(c_BA_tau.max() - c_BA_tau.min()) / c_BA_tau.mean() * 100:.1f}%")

# At the fold
i_fold = np.argmin(np.abs(tau_values - tau_fold))
tau_fold_actual = tau_values[i_fold]
c_BA_fold = c_BA_tau[i_fold]
omega_1_fold = omega_1_tau[i_fold]
E_J_fold = E_J_tau[i_fold]
E_c_fold = E_c_tau[i_fold]

print(f"\n  At fold (tau = {tau_fold_actual:.4f}):")
print(f"    E_J(fold) = {E_J_fold:.6f} M_KK")
print(f"    E_c(fold) = {E_c_fold:.6f} M_KK")
print(f"    E_J/E_c   = {E_J_fold / E_c_fold:.2f}")
print(f"    omega_1   = {omega_1_fold:.6f} M_KK")
print(f"    c_BA      = {c_BA_fold:.6f} M_KK")
print(f"    c_BA/c_Gold = {c_BA_fold / c_Gold:.6f}")

# ═══════════════════════════════════════════════════════════════════
#  STEP 4: Acoustic scale factor a_inter(tau) = 1 / c_BA(tau)
# ═══════════════════════════════════════════════════════════════════
a_inter_tau = 1.0 / c_BA_tau
# Normalize to a_inter(tau=0) = 1
a_inter_tau_norm = a_inter_tau / a_inter_tau[0]

# Check for maximum (natural stabilization)
i_max_a = np.argmax(a_inter_tau)
tau_max_a = tau_values[i_max_a]

print(f"\nAcoustic scale factor a_inter = 1/c_BA:")
print(f"  a_inter(tau=0) = {a_inter_tau[0]:.6f} M_KK^-1 (normalization)")
print(f"  a_inter maximum at tau = {tau_max_a:.4f}, value = {a_inter_tau_norm[i_max_a]:.6f}")
print(f"  a_inter(fold) / a_inter(0) = {a_inter_tau_norm[i_fold]:.6f}")
print(f"  a_inter(0.5) / a_inter(0) = {a_inter_tau_norm[-1]:.6f}")
print(f"  Total expansion ratio: {a_inter_tau_norm[-1] / a_inter_tau_norm[0]:.4f}")

has_max = (i_max_a > 0 and i_max_a < n_tau - 1)
if has_max:
    print(f"  ** INTERIOR MAXIMUM FOUND at tau = {tau_max_a:.4f} **")
    print(f"     This could signal natural stabilization of the fabric modulus")
else:
    print(f"  No interior maximum: a_inter is monotone")

# ═══════════════════════════════════════════════════════════════════
#  STEP 5: Full BA dispersion at fold — omega_n vs n
# ═══════════════════════════════════════════════════════════════════
omega_fold = omega_BA[i_fold, :]  # 31 modes
mode_indices = np.arange(1, n_modes + 1)

# Check for roton minimum: local minimum before zone edge
# A roton = omega_n decreasing then increasing before the last mode
d_omega = np.diff(omega_fold)
sign_changes = np.where(np.diff(np.sign(d_omega)))[0]

has_roton = False
roton_idx = None
roton_omega = None
if len(sign_changes) > 0:
    # Look for sign change from negative to positive (local min)
    for sc in sign_changes:
        if d_omega[sc] < 0 and d_omega[sc + 1] > 0:
            # Local minimum at mode sc+1
            has_roton = True
            roton_idx = sc + 1  # 0-indexed within omega_fold
            roton_omega = omega_fold[roton_idx]
            break

print(f"\nFull BA dispersion at fold (tau = {tau_fold_actual:.4f}):")
print(f"  31 nonzero modes")
print(f"  omega_1 = {omega_fold[0]:.6f} (acoustic)")
print(f"  omega_16 = {omega_fold[15]:.6f} (zone center)")
print(f"  omega_31 = {omega_fold[-1]:.6f} (zone edge)")
print(f"  Band center: {np.mean(omega_fold):.6f}")
print(f"  Bandwidth: {omega_fold[-1] - omega_fold[0]:.6f}")

if has_roton:
    print(f"  ** ROTON MINIMUM FOUND at mode n={roton_idx + 1} **")
    print(f"     omega_roton = {roton_omega:.6f} M_KK")
    print(f"     Delta_roton (from peak) = {omega_fold[:roton_idx].max() - roton_omega:.6f}")
else:
    print(f"  No roton minimum detected (dispersion is monotonically non-decreasing)")

# ═══════════════════════════════════════════════════════════════════
#  STEP 6: c_BA decomposition — what controls the tau dependence?
# ═══════════════════════════════════════════════════════════════════
# c_BA = (D/pi) * sqrt(E_J * E_c * lambda_1)
# E_J = J_C2^2 * F_anom(tau)
# E_c = delta_E_F(tau)/2
# lambda_1 is tau-independent
#
# So c_BA(tau) = (D/pi) * sqrt(lambda_1) * J_C2(tau) * sqrt(F_anom(tau) * E_c(tau))
# The dominant tau-dependence is from J_C2(tau) ~ exp(-tau)

# Compute J_C2 contribution vs the rest
J_C2_normalized = J_C2_tau / J_C2_tau[0]
c_BA_normalized = c_BA_tau / c_BA_tau[0]
rest_factor = c_BA_normalized / J_C2_normalized  # should be ~ sqrt(F_anom * E_c / F_anom_0 / E_c_0)

print(f"\nTau-dependence decomposition (all normalized to tau=0):")
print(f"  {'tau':>6} {'c_BA/c0':>10} {'J_C2/J0':>10} {'rest':>10}")
for i in range(0, n_tau, 5):
    print(f"  {tau_values[i]:6.3f} {c_BA_normalized[i]:10.6f} {J_C2_normalized[i]:10.6f} {rest_factor[i]:10.6f}")

# Correlation between c_BA and J_C2
corr = np.corrcoef(np.log(c_BA_tau), np.log(J_C2_tau))[0, 1]
print(f"\n  Correlation log(c_BA) vs log(J_C2): r = {corr:.6f}")

# ═══════════════════════════════════════════════════════════════════
#  STEP 7: Compare to S55 c_eff (intra-cell lattice sound)
# ═══════════════════════════════════════════════════════════════════
# S55 found c_eff = 0.338 M_KK at fold (PHONON-DISP-55)
c_eff_s55_fold = 0.338  # M_KK, from memory  # (local)

print(f"\n{'='*72}")
print(f"  VELOCITY HIERARCHY")
print(f"{'='*72}")
print(f"  c_Gold (intra-cell Goldstone) = {c_Gold:.4f} M_KK [S52, canonical]")
print(f"  c_eff (intra-cell lattice)    = {c_eff_s55_fold:.4f} M_KK [S55, at fold]")
print(f"  c_BA (inter-cell BA phonon)   = {c_BA_fold:.6f} M_KK [THIS COMPUTATION, at fold]")
print(f"")
print(f"  Ratios at fold:")
print(f"    c_BA / c_Gold = {c_BA_fold / c_Gold:.6f}")
print(f"    c_BA / c_eff  = {c_BA_fold / c_eff_s55_fold:.6f}")
print(f"    c_eff / c_Gold = {c_eff_s55_fold / c_Gold:.6f}")

# ═══════════════════════════════════════════════════════════════════
#  STEP 8: Detailed tau sweep table
# ═══════════════════════════════════════════════════════════════════
print(f"\n{'='*72}")
print(f"  FULL TAU SWEEP TABLE")
print(f"{'='*72}")
print(f"  {'tau':>6} {'J_C2':>8} {'E_J':>10} {'E_c':>10} {'E_J/E_c':>8} {'omega_1':>10} {'c_BA':>10} {'a_inter':>10}")
for i in range(n_tau):
    tag = " <-- fold" if i == i_fold else ""
    print(f"  {tau_values[i]:6.4f} {J_C2_tau[i]:8.4f} {E_J_tau[i]:10.6f} {E_c_tau[i]:10.6f} "
          f"{E_J_tau[i]/E_c_tau[i]:8.2f} {omega_1_tau[i]:10.6f} {c_BA_tau[i]:10.6f} {a_inter_tau_norm[i]:10.6f}{tag}")

# ═══════════════════════════════════════════════════════════════════
#  STEP 9: BA phonon free energy F_BA(tau)
# ═══════════════════════════════════════════════════════════════════
# For the Bogoliubov-Anderson phonons, the zero-point energy is:
#   E_ZP_BA(tau) = (1/2) sum_{n=1}^{31} omega_n(tau)
#
# This is the quantum zero-point contribution to the fabric free energy
# from the 31 BA phonon modes. At T=0:
#   F_BA(tau) = E_ZP_BA(tau)

E_ZP_BA = 0.5 * np.sum(omega_BA, axis=1)  # (50,)

# Check for minimum
i_min_E = np.argmin(E_ZP_BA)
tau_min_E = tau_values[i_min_E]
has_E_min = (i_min_E > 0 and i_min_E < n_tau - 1)

print(f"\n{'='*72}")
print(f"  BA PHONON ZERO-POINT ENERGY")
print(f"{'='*72}")
print(f"  E_ZP range: [{E_ZP_BA.min():.6f}, {E_ZP_BA.max():.6f}] M_KK")
print(f"  E_ZP at fold: {E_ZP_BA[i_fold]:.6f} M_KK")
print(f"  E_ZP minimum at tau = {tau_min_E:.4f} (value = {E_ZP_BA[i_min_E]:.6f})")
if has_E_min:
    barrier_E = (max(E_ZP_BA[0], E_ZP_BA[-1]) - E_ZP_BA[i_min_E]) / abs(E_ZP_BA[0]) * 100
    print(f"  ** INTERIOR MINIMUM FOUND **")
    print(f"     Barrier: {barrier_E:.2f}% of |E_ZP(0)|")
    in_range = 0.10 <= tau_min_E <= 0.30
    print(f"     In target range [0.10, 0.30]: {'YES' if in_range else 'NO'}")
else:
    print(f"  E_ZP is monotone (no interior minimum)")
    # Check if monotone increasing or decreasing
    if E_ZP_BA[-1] > E_ZP_BA[0]:
        print(f"  Direction: INCREASING with tau")
    else:
        print(f"  Direction: DECREASING with tau")

# ═══════════════════════════════════════════════════════════════════
#  STEP 10: Thermal BA partition function at T_GH
# ═══════════════════════════════════════════════════════════════════
# T_GH(tau) ~ H(tau) / (2*pi). For a rough estimate, use
# T_GH ~ something proportional to the local expansion rate.
# In our framework, H_fold = 586.5 M_KK, so T_GH ~ H/(2pi) ~ 93 M_KK.
# But BA phonon frequencies are ~ 0.1-1 M_KK, so all modes are deeply
# excited (kT >> hbar*omega). The classical limit applies.
#
# In the classical limit, F_BA_thermal = -N_modes * T * ln(T/omega_geometric_mean)
# where omega_geometric_mean = (prod omega_n)^{1/N_modes}
#
# The tau-dependent part is:
# F_BA_cl = N_modes * T * <ln omega_n(tau)> + const
# = (N_modes * T / 2) * [ln(E_J(tau)) + ln(E_c(tau))] + (T/2) * sum ln(lambda_n)
# The lambda_n sum is tau-independent, so doesn't contribute to tau-derivative.

log_omega_mean = np.zeros(n_tau)
for i in range(n_tau):
    log_omega_mean[i] = np.mean(np.log(omega_BA[i, :]))

# Geometric mean frequency
omega_geom_mean = np.exp(log_omega_mean)

print(f"\n{'='*72}")
print(f"  BA PHONON THERMAL PROPERTIES")
print(f"{'='*72}")
print(f"  Geometric mean omega at fold: {omega_geom_mean[i_fold]:.6f} M_KK")
print(f"  <ln omega>(tau) range: [{log_omega_mean.min():.4f}, {log_omega_mean.max():.4f}]")

# The classical free energy tau-dependence is dominated by
# d<ln omega>/dtau = d/dtau [ln E_J + ln E_c]/2 + const
# = [E_J'/E_J + E_c'/E_c]/2
dlog_omega = np.gradient(log_omega_mean, tau_values)
print(f"  d<ln omega>/dtau at fold: {dlog_omega[i_fold]:.4f}")

# ═══════════════════════════════════════════════════════════════════
#  GATE VERDICT
# ═══════════════════════════════════════════════════════════════════
print(f"\n{'='*72}")
print(f"  GATE VERDICT: CBA-SOUND-56 — INFO")
print(f"{'='*72}")
print(f"")
print(f"c_BA(tau) profile computed across 50 tau values.")
print(f"")
print(f"Key numbers:")
print(f"  c_BA at fold (tau={tau_fold_actual:.4f}) = {c_BA_fold:.6f} M_KK")
print(f"  c_BA minimum: {c_BA_tau.min():.6f} M_KK at tau = {tau_values[np.argmin(c_BA_tau)]:.4f}")
print(f"  c_BA maximum: {c_BA_tau.max():.6f} M_KK at tau = {tau_values[np.argmax(c_BA_tau)]:.4f}")
print(f"  c_BA / c_Gold at fold = {c_BA_fold / c_Gold:.6f}")
print(f"")
print(f"  c_BA is {'MONOTONICALLY DECREASING' if all(np.diff(c_BA_tau) < 0) else 'NON-MONOTONE'} with tau")

# Check monotonicity precisely
diffs = np.diff(c_BA_tau)
n_increase = np.sum(diffs > 0)
n_decrease = np.sum(diffs < 0)
print(f"  Steps increasing: {n_increase}, decreasing: {n_decrease}")

if has_E_min and 0.10 <= tau_min_E <= 0.30:
    print(f"\n  ** FLAG FOR W1-1: E_ZP_BA has minimum in target range [0.10, 0.30] **")
    print(f"     tau_min = {tau_min_E:.4f}, barrier = {barrier_E:.2f}%")
else:
    print(f"\n  E_ZP_BA {'has minimum outside target range' if has_E_min else 'is monotone'}.")

if has_roton:
    print(f"\n  ** FLAG: Roton minimum in BA dispersion at mode n={roton_idx + 1} **")

# ═══════════════════════════════════════════════════════════════════
#  SAVE DATA
# ═══════════════════════════════════════════════════════════════════
np.savez('computations/session-56/s56_cba_sound.npz',
    # Input parameters
    tau_values=tau_values,
    Delta_BCS=Delta,
    c_Gold=c_Gold,
    N_cells=N,
    diameter=D,
    # Graph Laplacian
    lambda_graph=lambda_graph,
    lambda_1=lambda_1,
    lambda_max=lambda_max,
    # Tau-dependent quantities
    E_J_tau=E_J_tau,
    E_c_tau=E_c_tau,
    J_C2_tau=J_C2_tau,
    F_anom_tau=F_anom_tau,
    mu_tau=mu_tau,
    # BA phonon spectrum (50 x 31)
    omega_BA=omega_BA,
    omega_1_tau=omega_1_tau,
    # Sound velocity
    c_BA_tau=c_BA_tau,
    c_BA_fold=c_BA_fold,
    # Acoustic scale factor
    a_inter_tau=a_inter_tau,
    a_inter_tau_norm=a_inter_tau_norm,
    # Zero-point energy
    E_ZP_BA=E_ZP_BA,
    # Fold values
    i_fold=i_fold,
    tau_fold_actual=tau_fold_actual,
    omega_fold=omega_fold,
    # Thermal
    log_omega_mean=log_omega_mean,
    omega_geom_mean=omega_geom_mean,
    # Gate
    gate_name=np.array(['CBA-SOUND-56']),
    gate_verdict=np.array(['INFO']),
)
print(f"\nData saved: computations/session-56/s56_cba_sound.npz")

# ═══════════════════════════════════════════════════════════════════
#  PLOTS
# ═══════════════════════════════════════════════════════════════════
fig, axes = plt.subplots(2, 3, figsize=(18, 11))
fig.suptitle('CBA-SOUND-56: Bogoliubov-Anderson Sound Velocity on 32-Cell CG Fabric',
             fontsize=14, fontweight='bold')

# --- Panel (0,0): c_BA(tau) vs c_Gold ---
ax = axes[0, 0]
ax.plot(tau_values, c_BA_tau, 'b-', linewidth=2, label=r'$c_{\mathrm{BA}}(\tau)$ (inter-cell)')
ax.axhline(c_Gold, color='r', linestyle='--', linewidth=1.5, label=f'$c_{{\\mathrm{{Gold}}}}$ = {c_Gold:.3f}')
ax.axhline(c_eff_s55_fold, color='orange', linestyle=':', linewidth=1.5, label=f'$c_{{\\mathrm{{eff}}}}$ (S55 fold) = {c_eff_s55_fold:.3f}')
ax.axvline(tau_fold, color='gray', linestyle=':', alpha=0.5, label=f'fold ($\\tau$={tau_fold})')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$c$ [M$_{\mathrm{KK}}$]')
ax.set_title(r'Sound Velocity Hierarchy')
ax.legend(fontsize=8, loc='upper right')
ax.set_xlim(0, 0.5)
ax.grid(True, alpha=0.3)

# --- Panel (0,1): E_J, E_c, E_J/E_c ---
ax = axes[0, 1]
ax2 = ax.twinx()
ax.plot(tau_values, E_J_tau, 'b-', linewidth=2, label=r'$E_J(\tau)$')
ax.plot(tau_values, E_c_tau, 'r-', linewidth=2, label=r'$E_c(\tau)$')
ax2.plot(tau_values, E_J_tau / E_c_tau, 'g--', linewidth=1.5, label=r'$E_J/E_c$')
ax.axvline(tau_fold, color='gray', linestyle=':', alpha=0.5)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'Energy [M$_{\mathrm{KK}}$]')
ax2.set_ylabel(r'$E_J / E_c$', color='g')
ax2.tick_params(axis='y', labelcolor='g')
ax.set_title(r'Josephson and Charging Energies')
lines1, labels1 = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax.legend(lines1 + lines2, labels1 + labels2, fontsize=8, loc='upper right')
ax.set_xlim(0, 0.5)
ax.grid(True, alpha=0.3)

# --- Panel (0,2): Full dispersion at fold ---
ax = axes[0, 2]
ax.plot(mode_indices, omega_fold, 'ko-', markersize=4, linewidth=1.5)
if has_roton:
    ax.axvline(roton_idx + 1, color='red', linestyle='--', alpha=0.7, label=f'Roton (n={roton_idx + 1})')
ax.axhline(omega_1_fold, color='blue', linestyle=':', alpha=0.5, label=f'$\\omega_1$ = {omega_1_fold:.4f}')
ax.set_xlabel('Mode index $n$')
ax.set_ylabel(r'$\omega_n$ [M$_{\mathrm{KK}}$]')
ax.set_title(f'BA Dispersion at Fold ($\\tau$ = {tau_fold_actual:.3f})')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# --- Panel (1,0): Acoustic scale factor ---
ax = axes[1, 0]
ax.plot(tau_values, a_inter_tau_norm, 'b-', linewidth=2)
ax.axvline(tau_fold, color='gray', linestyle=':', alpha=0.5, label=f'fold')
if has_max:
    ax.axvline(tau_max_a, color='red', linestyle='--', alpha=0.7, label=f'max at $\\tau$={tau_max_a:.3f}')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$a_{\mathrm{inter}}(\tau) / a_{\mathrm{inter}}(0)$')
ax.set_title(r'Acoustic Scale Factor $a = 1/c_{\mathrm{BA}}$')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# --- Panel (1,1): Zero-point energy ---
ax = axes[1, 1]
ax.plot(tau_values, E_ZP_BA, 'b-', linewidth=2)
ax.axvline(tau_fold, color='gray', linestyle=':', alpha=0.5, label=f'fold')
if has_E_min:
    ax.axvline(tau_min_E, color='red', linestyle='--', alpha=0.7, label=f'min at $\\tau$={tau_min_E:.3f}')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$E_{\mathrm{ZP}}^{\mathrm{BA}}$ [M$_{\mathrm{KK}}$]')
ax.set_title(r'BA Phonon Zero-Point Energy $\frac{1}{2}\sum\omega_n$')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# --- Panel (1,2): Decomposition of c_BA ---
ax = axes[1, 2]
ax.plot(tau_values, c_BA_normalized, 'b-', linewidth=2, label=r'$c_{\mathrm{BA}} / c_{\mathrm{BA}}(0)$')
ax.plot(tau_values, J_C2_normalized, 'r--', linewidth=1.5, label=r'$J_{C^2} / J_{C^2}(0)$')
ax.plot(tau_values, rest_factor, 'g:', linewidth=1.5, label='Residual factor')
ax.axvline(tau_fold, color='gray', linestyle=':', alpha=0.5)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel('Normalized')
ax.set_title(r'$c_{\mathrm{BA}}$ Decomposition: $J_{C^2}$ vs Rest')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)
ax.set_xlim(0, 0.5)

plt.tight_layout()
plt.savefig('computations/session-56/s56_cba_sound.png', dpi=150, bbox_inches='tight')
print(f"Plot saved: computations/session-56/s56_cba_sound.png")

print(f"\n{'='*72}")
print(f"  COMPUTATION COMPLETE")
print(f"{'='*72}")
