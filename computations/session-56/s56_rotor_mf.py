#!/usr/bin/env python3
"""
s56_rotor_mf.py — Quantum Rotor Mean-Field Free Energy on 32-Cell Graph

ROTOR-MF-56 (FABRIC-FREE-ENERGY-56 gate):
Compute F_fabric(tau) = F_cells + F_Josephson + F_BA on the 32-cell CG graph
using self-consistent XY mean-field theory for the Josephson phase order
parameter, combined with the Bogoliubov-Anderson phonon and BCS quasiparticle
contributions.

Gate: FABRIC-FREE-ENERGY-56
  PASS: F_fabric has minimum in [0.10, 0.30] with barrier > 1%.
  FAIL: F_fabric(tau) is monotone.

Physics (Nazarewicz decomposition):
  F_fabric(tau, T) = F_cells(tau, T) + F_Josephson(tau, T) + F_BA(tau, T)

  F_cells    = 32 * [-T_GH * ln(Prod_k (1 + exp(-E_sp_k / T_GH)))]   (BCS fermionic)
  F_Josephson = -N_bonds * E_J(tau) * <cos(phi)>(tau, T)                (Josephson stiffness)
  F_BA       = Sum_{n=1}^{31} [omega_n/2 + T * ln(1 - exp(-omega_n/T))] (BA phonons)

  Self-consistency: m = <cos(phi)> satisfies
    m = I_1(z * E_J * m / T) / I_0(z * E_J * m / T)
  where z = mean C2 coordination number, I_0/I_1 = modified Bessel functions.

Author: landau-condensed-matter-theorist
Session: S56
"""

import sys
import os
import numpy as np
from scipy.interpolate import interp1d
from scipy.special import i0, i1  # modified Bessel functions I_0, I_1
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

sys.path.insert(0, 'computations')
from canonical_constants import Delta_0_OES, tau_fold, N_cells

# =============================================================================
# 0. Load data
# =============================================================================

# W0-1 BA spectrum data (reuse for consistency)
ba = np.load('computations/session-56/s56_ba_spectrum.npz')
tau_values = ba['tau_values']       # (50,)
E_J_arr = ba['E_J']                # (50,) Josephson energy per C2 bond
E_c_arr = ba['E_c']                # (50,) charging energy
omega_BA_all = ba['omega_BA']       # (50, 31) BA phonon frequencies
T_GH = ba['T_GH']                  # (50,) Gibbons-Hawking temperature
F_BA_w0 = ba['F_BA']               # (50,) for cross-check
laplacian_eigs = ba['laplacian_eigs']  # (32,) graph Laplacian eigenvalues

# Tight-binding data
tb = np.load('computations/session-54/s54_tb_hamiltonian.npz')
adj_C2 = tb['adj_C2']              # (32, 32) C2 adjacency
eigenvalues = tb['eigenvalues']     # (50, 32) TB spectrum

# ED data for single-particle quasiparticle energies
ed = np.load('computations/session-54/s54_ed_sweep.npz')
E_sp_sweep = ed['E_sp_sweep']      # (50, 8) BCS-active single-particle energies

N_tau = len(tau_values)   # 50
Delta = Delta_0_OES       # 0.4643 M_KK

print(f"Loaded: {N_tau} tau values in [{tau_values[0]:.4f}, {tau_values[-1]:.4f}]")
print(f"N_cells = {N_cells}, Delta = {Delta:.6f} M_KK")

# =============================================================================
# 1. Graph structure
# =============================================================================

coord_C2 = np.sum(adj_C2 > 0, axis=1)  # coordination per cell
z_C2 = np.mean(coord_C2.astype(float))  # mean C2 coordination = 3.125
N_bonds = np.sum(adj_C2 > 0) // 2       # number of C2 bonds = 50

print(f"\nGraph structure:")
print(f"  N_bonds (C2) = {N_bonds}")
print(f"  z_C2 (mean coordination) = {z_C2:.4f}")
print(f"  Coordination range: [{coord_C2.min()}, {coord_C2.max()}]")

# =============================================================================
# 2. F_cells: BCS fermionic free energy
#    F_cells(tau) = 32 * [-T_GH * Sum_{k=0}^{7} ln(1 + exp(-E_sp_k / T_GH))]
# =============================================================================

F_cells = np.zeros(N_tau)

for i in range(N_tau):
    T = T_GH[i]
    E_sp = E_sp_sweep[i]  # 8 single-particle eigenvalues
    # Fermionic free energy per cell: -T * Sum_k ln(1 + exp(-E_k / T))
    # Note: E_sp_k >= 0 (eigenvalues from zero). The argument -E_sp_k/T is always <= 0.
    # ln(1 + exp(-x)) for x = E_sp/T
    x = E_sp / T
    # Numerical stability: for large x, ln(1 + exp(-x)) ~ exp(-x)
    log_terms = np.where(x > 500, np.exp(-x), np.log1p(np.exp(-x)))
    F_cell_i = -T * np.sum(log_terms)
    F_cells[i] = N_cells * F_cell_i

print(f"\nF_cells range: [{F_cells.min():.4f}, {F_cells.max():.4f}] M_KK")

# =============================================================================
# 3. Self-consistent mean-field for <cos(phi)>
#    m = I_1(z * E_J * m / T) / I_0(z * E_J * m / T)
#
#    Physics: In the XY model mean-field on a lattice with coordination z,
#    each spin sees an effective field h_eff = z * E_J * m from its neighbors.
#    The single-spin partition function is Z_1 = 2*pi*I_0(h_eff/T), giving
#    <cos(phi)> = I_1(h_eff/T) / I_0(h_eff/T).
#
#    The C2 coordination z_C2 = 3.125 is the correct choice since E_J
#    is the C2 Josephson coupling.
# =============================================================================

m_order = np.zeros(N_tau)    # order parameter <cos(phi)>

for i in range(N_tau):
    T = T_GH[i]
    E_J = E_J_arr[i]
    z = z_C2

    # Initialize close to ordered state
    m = 0.99
    for iteration in range(10000):
        arg = z * E_J * m / T
        if arg > 700:
            # Asymptotic: I_1(x)/I_0(x) -> 1 - 1/(2x) for x >> 1
            m_new = 1.0 - 1.0 / (2.0 * arg)
        elif arg < 1e-15:
            m_new = 0.0  # (local)
            m = m_new
            break
        else:
            m_new = float(i1(arg) / i0(arg))

        if abs(m_new - m) < 1e-12:
            m = m_new
            break
        m = m_new
    else:
        print(f"  WARNING: mean-field did not converge at tau={tau_values[i]:.4f}, m={m:.6f}")

    m_order[i] = m

print(f"\n<cos(phi)> (order parameter):")
print(f"  Range: [{m_order.min():.6f}, {m_order.max():.6f}]")
idx_fold = np.argmin(np.abs(tau_values - tau_fold))
print(f"  At fold (tau={tau_values[idx_fold]:.4f}): m = {m_order[idx_fold]:.6f}")
print(f"  At tau=0: m = {m_order[0]:.6f}")
print(f"  At tau=0.5: m = {m_order[-1]:.6f}")

# Check: is the system always ordered (m > 0)?
all_ordered = np.all(m_order > 0.01)
print(f"  Ordered (m > 0.01) at all tau: {all_ordered}")

# =============================================================================
# 4. F_Josephson: Josephson phase stiffness free energy
#    F_Josephson(tau) = -N_bonds * E_J(tau) * m(tau)
# =============================================================================

F_Josephson = -N_bonds * E_J_arr * m_order

print(f"\nF_Josephson range: [{F_Josephson.min():.4f}, {F_Josephson.max():.4f}] M_KK")
print(f"  At fold: {F_Josephson[idx_fold]:.4f}")
print(f"  At tau=0: {F_Josephson[0]:.4f}")
print(f"  At tau=0.5: {F_Josephson[-1]:.4f}")

# =============================================================================
# 5. F_BA: Bogoliubov-Anderson phonon free energy
#    F_BA(tau) = Sum_{n=1}^{31} [omega_n/2 + T * ln(1 - exp(-omega_n/T))]
#    Recomputed here for full control (also cross-checked against W0-1).
# =============================================================================

F_BA = np.zeros(N_tau)
F_ZPE = np.zeros(N_tau)
F_thermal = np.zeros(N_tau)

for i in range(N_tau):
    T = T_GH[i]
    for n in range(N_cells - 1):
        om = omega_BA_all[i, n]
        F_ZPE[i] += om / 2.0
        x = om / T
        if x > 500:
            thermal = 0.0
        else:
            thermal = T * np.log(1.0 - np.exp(-x))
        F_thermal[i] += thermal
    F_BA[i] = F_ZPE[i] + F_thermal[i]

# Cross-check against W0-1
max_ba_diff = np.max(np.abs(F_BA - F_BA_w0))
print(f"\nF_BA cross-check vs W0-1: max|diff| = {max_ba_diff:.2e}")
assert max_ba_diff < 1e-8, f"F_BA mismatch: {max_ba_diff}"

print(f"F_BA range: [{F_BA.min():.4f}, {F_BA.max():.4f}] M_KK")

# =============================================================================
# 6. F_fabric: total fabric free energy
#    F_fabric(tau) = F_cells(tau) + F_Josephson(tau) + F_BA(tau)
# =============================================================================

F_fabric = F_cells + F_Josephson + F_BA

print(f"\n{'='*72}")
print(f"FABRIC FREE ENERGY DECOMPOSITION")
print(f"{'='*72}")
print(f"{'tau':>6s}  {'F_cells':>12s}  {'F_Joseph':>12s}  {'F_BA':>12s}  {'F_fabric':>12s}")
print(f"{'-'*6}  {'-'*12}  {'-'*12}  {'-'*12}  {'-'*12}")

for idx in [0, 5, 10, 15, idx_fold, 20, 25, 30, 35, 40, 45, 49]:
    print(f"{tau_values[idx]:6.3f}  {F_cells[idx]:12.4f}  {F_Josephson[idx]:12.4f}  {F_BA[idx]:12.4f}  {F_fabric[idx]:12.4f}")

# =============================================================================
# 7. Derivatives and extrema search
# =============================================================================

dtau = tau_values[1] - tau_values[0]

# Numerical derivatives (central difference where possible)
dF_fabric = np.gradient(F_fabric, tau_values)
dF_cells = np.gradient(F_cells, tau_values)
dF_Josephson = np.gradient(F_Josephson, tau_values)
dF_BA = np.gradient(F_BA, tau_values)

# Second derivative of F_fabric
d2F_fabric = np.gradient(dF_fabric, tau_values)

# Find sign changes in dF_fabric (extrema candidates)
sign_dF = np.sign(dF_fabric)
sign_changes_fabric = []
for i in range(len(sign_dF) - 1):
    if sign_dF[i] * sign_dF[i+1] < 0:
        # Linear interpolation for zero crossing
        tau_cross = tau_values[i] - dF_fabric[i] * dtau / (dF_fabric[i+1] - dF_fabric[i])
        is_min = dF_fabric[i] < 0 and dF_fabric[i+1] > 0
        sign_changes_fabric.append((tau_cross, 'MIN' if is_min else 'MAX', i))

print(f"\n{'='*72}")
print(f"EXTREMA ANALYSIS")
print(f"{'='*72}")
print(f"dF_fabric sign changes: {len(sign_changes_fabric)}")
for tau_c, kind, idx_c in sign_changes_fabric:
    F_at_cross = np.interp(tau_c, tau_values, F_fabric)
    d2F_at_cross = np.interp(tau_c, tau_values, d2F_fabric)
    print(f"  {kind} at tau = {tau_c:.4f}, F_fabric ~ {F_at_cross:.4f}, d2F = {d2F_at_cross:.4f}")

# Search specifically in [0.10, 0.30]
mask_gate = (tau_values >= 0.10) & (tau_values <= 0.30)
minima_in_range = [x for x in sign_changes_fabric if 0.10 <= x[0] <= 0.30 and x[1] == 'MIN']

print(f"\nMinima in [0.10, 0.30]: {len(minima_in_range)}")

# Also check: is the minimum at the boundary or interior?
F_in_range = F_fabric[mask_gate]
tau_in_range = tau_values[mask_gate]
idx_min_in_range = np.argmin(F_in_range)
tau_min_in_range = tau_in_range[idx_min_in_range]
F_min_in_range = F_in_range[idx_min_in_range]
is_interior = (idx_min_in_range > 0) and (idx_min_in_range < len(tau_in_range) - 1)

# Global minimum
idx_global_min = np.argmin(F_fabric)
tau_global_min = tau_values[idx_global_min]
F_global_min = F_fabric[idx_global_min]

print(f"\nGlobal minimum of F_fabric:")
print(f"  tau_min = {tau_global_min:.4f}")
print(f"  F_fabric(tau_min) = {F_global_min:.4f}")
print(f"  F_fabric(tau=0) = {F_fabric[0]:.4f}")
print(f"  F_fabric(tau=0.5) = {F_fabric[-1]:.4f}")

print(f"\nIn [0.10, 0.30]:")
print(f"  Minimum at tau = {tau_min_in_range:.4f}")
print(f"  F_fabric = {F_min_in_range:.4f}")
print(f"  Interior minimum: {is_interior}")

# =============================================================================
# 8. Barrier height computation
# =============================================================================

# Extended search: also look in [0.10, 0.35] since W0-1 found F_BA minimum at tau=0.306
mask_ext = (tau_values >= 0.10) & (tau_values <= 0.35)
minima_extended = [x for x in sign_changes_fabric if 0.10 <= x[0] <= 0.35 and x[1] == 'MIN']

barrier_height = 0.0  # (local)
barrier_pct = 0.0  # (local)
gate_pass = False

if len(minima_in_range) > 0:
    tau_min_gate = minima_in_range[0][0]
    F_min_gate = np.interp(tau_min_gate, tau_values, F_fabric)
    F_ref = max(F_fabric[0], F_fabric[-1])
    barrier_height = F_ref - F_min_gate
    barrier_pct = 100.0 * abs(barrier_height / F_fabric[0]) if abs(F_fabric[0]) > 1e-10 else 0.0
    gate_pass = barrier_pct > 1.0
    print(f"\n*** MINIMUM FOUND IN GATE WINDOW ***")
    print(f"  tau_min = {tau_min_gate:.4f}")
    print(f"  F_min = {F_min_gate:.4f}")
    print(f"  Barrier height: {barrier_height:.4f}")
    print(f"  Barrier %: {barrier_pct:.2f}%")
elif is_interior:
    # Interior minimum at grid point but no sign change found (flat derivative)
    F_boundary_max = max(F_in_range[0], F_in_range[-1])
    barrier_height = F_boundary_max - F_min_in_range
    barrier_pct = 100.0 * abs(barrier_height / F_fabric[0]) if abs(F_fabric[0]) > 1e-10 else 0.0
    gate_pass = barrier_pct > 1.0
    print(f"\n*** INTERIOR MINIMUM AT GRID POINT ***")
    print(f"  tau_min = {tau_min_in_range:.4f}")
    print(f"  Barrier height: {barrier_height:.4f}")
    print(f"  Barrier %: {barrier_pct:.2f}%")
else:
    print(f"\n  No interior minimum in [0.10, 0.30]. F_fabric monotone in this window.")
    # Check extended range
    if len(minima_extended) > 0:
        tau_min_ext = minima_extended[0][0]
        F_min_ext = np.interp(tau_min_ext, tau_values, F_fabric)
        F_ref = max(F_fabric[0], F_fabric[-1])
        barrier_ext = F_ref - F_min_ext
        barrier_ext_pct = 100.0 * abs(barrier_ext / F_fabric[0]) if abs(F_fabric[0]) > 1e-10 else 0.0
        print(f"  Extended [0.10, 0.35]: minimum at tau = {tau_min_ext:.4f}, barrier = {barrier_ext_pct:.2f}%")

# Dominant term at the fold
print(f"\nDerivative decomposition at fold (tau={tau_values[idx_fold]:.4f}):")
print(f"  dF_cells/dtau    = {dF_cells[idx_fold]:+.4f}")
print(f"  dF_Josephson/dtau = {dF_Josephson[idx_fold]:+.4f}")
print(f"  dF_BA/dtau       = {dF_BA[idx_fold]:+.4f}")
print(f"  dF_fabric/dtau   = {dF_fabric[idx_fold]:+.4f}")
dominant = 'F_cells' if abs(dF_cells[idx_fold]) > max(abs(dF_Josephson[idx_fold]), abs(dF_BA[idx_fold])) else \
           'F_Josephson' if abs(dF_Josephson[idx_fold]) > abs(dF_BA[idx_fold]) else 'F_BA'
print(f"  Dominant term: {dominant}")

# =============================================================================
# 9. Gate verdict
# =============================================================================

gate_name = 'FABRIC-FREE-ENERGY-56'
if gate_pass:
    gate_verdict = 'PASS'
    gate_detail = f'F_fabric minimum in [0.10,0.30] with barrier {barrier_pct:.1f}%'
else:
    gate_verdict = 'FAIL'
    if is_interior and len(minima_in_range) == 0:
        gate_detail = f'Interior minimum at tau={tau_min_in_range:.4f} but barrier {barrier_pct:.2f}% < 1%'
    else:
        gate_detail = f'F_fabric monotone in [0.10,0.30]. Global min at tau={tau_global_min:.4f}'

print(f"\n{'='*72}")
print(f"GATE VERDICT: {gate_name} = {gate_verdict}")
print(f"Detail: {gate_detail}")
print(f"{'='*72}")

# =============================================================================
# 10. Save results
# =============================================================================

np.savez('computations/session-56/s56_rotor_mf.npz',
    # Grid
    tau_values=tau_values,
    N_cells=np.int64(N_cells),
    N_bonds=np.int64(N_bonds),
    z_C2=z_C2,
    Delta=Delta,

    # Components
    F_cells=F_cells,
    F_Josephson=F_Josephson,
    F_BA=F_BA,
    F_fabric=F_fabric,
    F_ZPE=F_ZPE,
    F_thermal=F_thermal,

    # Order parameter
    m_order=m_order,

    # Derivatives
    dF_fabric=dF_fabric,
    dF_cells=dF_cells,
    dF_Josephson=dF_Josephson,
    dF_BA=dF_BA,
    d2F_fabric=d2F_fabric,

    # Input parameters
    E_J=E_J_arr,
    E_c=E_c_arr,
    T_GH=T_GH,

    # Extrema
    tau_global_min=tau_global_min,
    F_global_min=F_global_min,
    barrier_height=barrier_height,
    barrier_pct=barrier_pct,

    # Gate
    gate_name=np.array([gate_name]),
    gate_verdict=np.array([gate_verdict]),
    gate_detail=np.array([gate_detail])
)
print(f"\nSaved: computations/session-56/s56_rotor_mf.npz")

# =============================================================================
# 11. Plotting
# =============================================================================

fig = plt.figure(figsize=(20, 16))
gs = GridSpec(3, 2, figure=fig, hspace=0.35, wspace=0.30)

# Color scheme
c_fabric = '#000000'
c_cells = '#2ca02c'
c_josephson = '#d62728'
c_ba = '#1f77b4'
c_fold = 'gray'

# --- Panel (a): All free energy components ---
ax1 = fig.add_subplot(gs[0, 0])
ax1.plot(tau_values, F_fabric, c_fabric, linewidth=2.5, label=r'$F_{\rm fabric}$ (total)')
ax1.plot(tau_values, F_cells, c_cells, linewidth=1.5, linestyle='--', label=r'$F_{\rm cells}$ (BCS)')
ax1.plot(tau_values, F_Josephson, c_josephson, linewidth=1.5, linestyle='-.', label=r'$F_{\rm Josephson}$')
ax1.plot(tau_values, F_BA, c_ba, linewidth=1.5, linestyle=':', label=r'$F_{\rm BA}$')
ax1.axvline(tau_fold, color=c_fold, linestyle='--', alpha=0.5, label=f'fold ($\\tau={tau_fold:.2f}$)')

# Mark global minimum
ax1.plot(tau_global_min, F_global_min, 'ko', markersize=8, zorder=5)
ax1.annotate(f'min at $\\tau$={tau_global_min:.3f}',
             xy=(tau_global_min, F_global_min),
             xytext=(tau_global_min + 0.03, F_global_min + 20),
             arrowprops=dict(arrowstyle='->', color='black'),
             fontsize=9)

# Gate window
ax1.axvspan(0.10, 0.30, alpha=0.08, color='green', label='gate window')

ax1.set_xlabel(r'$\tau$', fontsize=12)
ax1.set_ylabel(r'$F$ [$M_{KK}$]', fontsize=12)
ax1.set_title('(a) Fabric Free Energy Components', fontsize=13, fontweight='bold')
ax1.legend(fontsize=8, loc='upper right')
ax1.grid(True, alpha=0.3)

# --- Panel (b): Order parameter <cos(phi)> ---
ax2 = fig.add_subplot(gs[0, 1])
ax2.plot(tau_values, m_order, 'k-', linewidth=2)
ax2.axvline(tau_fold, color=c_fold, linestyle='--', alpha=0.5, label='fold')
ax2.axhline(0.0, color='red', linestyle=':', alpha=0.5)
ax2.fill_between(tau_values, 0, m_order, alpha=0.15, color='blue')

ax2.set_xlabel(r'$\tau$', fontsize=12)
ax2.set_ylabel(r'$\langle \cos\phi \rangle$', fontsize=12)
ax2.set_title(r'(b) XY Order Parameter $m(\tau)$', fontsize=13, fontweight='bold')
ax2.set_ylim(-0.05, 1.05)
ax2.legend(fontsize=9)
ax2.grid(True, alpha=0.3)

# Annotate key values
ax2.annotate(f'm={m_order[idx_fold]:.4f}',
             xy=(tau_values[idx_fold], m_order[idx_fold]),
             xytext=(tau_values[idx_fold] + 0.05, m_order[idx_fold] - 0.1),
             arrowprops=dict(arrowstyle='->', color='blue'),
             fontsize=9, color='blue')

# --- Panel (c): dF/dtau for all components ---
ax3 = fig.add_subplot(gs[1, 0])
ax3.plot(tau_values, dF_fabric, c_fabric, linewidth=2.5, label=r'd$F_{\rm fabric}$/d$\tau$')
ax3.plot(tau_values, dF_cells, c_cells, linewidth=1.5, linestyle='--', label=r'd$F_{\rm cells}$/d$\tau$')
ax3.plot(tau_values, dF_Josephson, c_josephson, linewidth=1.5, linestyle='-.', label=r'd$F_{\rm Josephson}$/d$\tau$')
ax3.plot(tau_values, dF_BA, c_ba, linewidth=1.5, linestyle=':', label=r'd$F_{\rm BA}$/d$\tau$')
ax3.axhline(0.0, color='gray', linewidth=0.8)
ax3.axvline(tau_fold, color=c_fold, linestyle='--', alpha=0.5)
ax3.axvspan(0.10, 0.30, alpha=0.08, color='green')

# Mark zero crossings of dF_fabric
for tau_c, kind, idx_c in sign_changes_fabric:
    marker = 'v' if kind == 'MIN' else '^'
    color = 'green' if kind == 'MIN' else 'red'
    ax3.plot(tau_c, 0, marker, markersize=10, color=color, zorder=5,
             label=f'{kind} at $\\tau$={tau_c:.3f}')

ax3.set_xlabel(r'$\tau$', fontsize=12)
ax3.set_ylabel(r'd$F$/d$\tau$ [$M_{KK}$]', fontsize=12)
ax3.set_title(r'(c) Derivatives d$F$/d$\tau$', fontsize=13, fontweight='bold')
ax3.legend(fontsize=7, loc='lower left', ncol=2)
ax3.grid(True, alpha=0.3)

# --- Panel (d): Individual dF/dtau contributions ---
ax4 = fig.add_subplot(gs[1, 1])

# Stacked area plot to show which contribution dominates
pos_stack = np.maximum(dF_cells, 0) + np.maximum(dF_Josephson, 0) + np.maximum(dF_BA, 0)
neg_stack = np.minimum(dF_cells, 0) + np.minimum(dF_Josephson, 0) + np.minimum(dF_BA, 0)

ax4.fill_between(tau_values, 0, dF_cells, alpha=0.3, color=c_cells, label=r'$F_{\rm cells}$')
ax4.fill_between(tau_values, dF_cells, dF_cells + dF_Josephson, alpha=0.3, color=c_josephson, label=r'$F_{\rm Josephson}$')
ax4.plot(tau_values, dF_fabric, c_fabric, linewidth=2, label=r'$F_{\rm fabric}$ (sum)')
ax4.axhline(0.0, color='gray', linewidth=0.8)
ax4.axvline(tau_fold, color=c_fold, linestyle='--', alpha=0.5)
ax4.axvspan(0.10, 0.30, alpha=0.08, color='green')

ax4.set_xlabel(r'$\tau$', fontsize=12)
ax4.set_ylabel(r'd$F$/d$\tau$ [$M_{KK}$]', fontsize=12)
ax4.set_title('(d) Derivative Decomposition (Stacked)', fontsize=13, fontweight='bold')
ax4.legend(fontsize=8)
ax4.grid(True, alpha=0.3)

# --- Panel (e): F_fabric zoomed on gate window ---
ax5 = fig.add_subplot(gs[2, 0])
mask_zoom = (tau_values >= 0.05) & (tau_values <= 0.40)
ax5.plot(tau_values[mask_zoom], F_fabric[mask_zoom], 'k-', linewidth=2.5, label=r'$F_{\rm fabric}$')
ax5.axvspan(0.10, 0.30, alpha=0.12, color='green', label='gate window [0.10, 0.30]')
ax5.axvline(tau_fold, color=c_fold, linestyle='--', alpha=0.5, label='fold')

# Mark minimum if found
if len(minima_in_range) > 0:
    tau_m = minima_in_range[0][0]
    F_m = np.interp(tau_m, tau_values, F_fabric)
    ax5.plot(tau_m, F_m, 'g*', markersize=15, zorder=5, label=f'min (barrier={barrier_pct:.1f}%)')
else:
    ax5.plot(tau_global_min, F_global_min, 'ko', markersize=8, zorder=5, label=f'global min at $\\tau$={tau_global_min:.3f}')

ax5.set_xlabel(r'$\tau$', fontsize=12)
ax5.set_ylabel(r'$F_{\rm fabric}$ [$M_{KK}$]', fontsize=12)
ax5.set_title('(e) Gate Window Detail', fontsize=13, fontweight='bold')
ax5.legend(fontsize=8)
ax5.grid(True, alpha=0.3)

# --- Panel (f): Energy scales ---
ax6 = fig.add_subplot(gs[2, 1])
ax6.semilogy(tau_values, E_J_arr, 'b-', linewidth=2, label=r'$E_J$')
ax6.semilogy(tau_values, E_c_arr, 'r-', linewidth=2, label=r'$E_c$')
ax6.semilogy(tau_values, T_GH, 'g-', linewidth=2, label=r'$T_{GH}$')
ax6.semilogy(tau_values, np.abs(F_Josephson / N_bonds), 'm--', linewidth=1.5, label=r'$|F_J|/N_{\rm bonds}$')
ax6.axvline(tau_fold, color=c_fold, linestyle='--', alpha=0.5)

ax6.set_xlabel(r'$\tau$', fontsize=12)
ax6.set_ylabel('Energy [$M_{KK}$]', fontsize=12)
ax6.set_title('(f) Energy Scale Hierarchy', fontsize=13, fontweight='bold')
ax6.legend(fontsize=8)
ax6.grid(True, alpha=0.3, which='both')

# Title
verdict_str = f"GATE: {gate_verdict}"
fig.suptitle(f'ROTOR-MF-56: Fabric Free Energy (32-Cell CG, $z_{{C2}}$={z_C2:.2f})\n{verdict_str}',
             fontsize=14, fontweight='bold', y=0.99)

plt.savefig('computations/session-56/s56_rotor_mf.png', dpi=150, bbox_inches='tight')
print(f"Saved: computations/session-56/s56_rotor_mf.png")

# =============================================================================
# 12. Summary table
# =============================================================================

print(f"\n{'='*72}")
print(f"ROTOR-MF-56 COMPLETE SUMMARY")
print(f"{'='*72}")
print(f"  N_cells = {N_cells}, N_bonds(C2) = {N_bonds}, z_C2 = {z_C2:.4f}")
print(f"  Delta = {Delta:.6f} M_KK")
print(f"")
print(f"  ORDER PARAMETER <cos(phi)>:")
print(f"    tau = 0.00: m = {m_order[0]:.6f}")
print(f"    tau = 0.19 (fold): m = {m_order[idx_fold]:.6f}")
print(f"    tau = 0.31: m = {m_order[30]:.6f}")
print(f"    tau = 0.50: m = {m_order[-1]:.6f}")
print(f"    All ordered: {all_ordered}")
print(f"")
print(f"  FREE ENERGY COMPONENTS AT FOLD:")
print(f"    F_cells    = {F_cells[idx_fold]:+12.4f}")
print(f"    F_Josephson = {F_Josephson[idx_fold]:+12.4f}")
print(f"    F_BA       = {F_BA[idx_fold]:+12.4f}")
print(f"    F_fabric   = {F_fabric[idx_fold]:+12.4f}")
print(f"")
print(f"  FREE ENERGY AT BOUNDARIES:")
print(f"    F_fabric(tau=0)   = {F_fabric[0]:+12.4f}")
print(f"    F_fabric(tau=0.5) = {F_fabric[-1]:+12.4f}")
print(f"")
print(f"  EXTREMA:")
print(f"    Global min: tau = {tau_global_min:.4f}, F = {F_global_min:.4f}")
print(f"    Minima in [0.10, 0.30]: {len(minima_in_range)}")
print(f"    Minima in [0.10, 0.35]: {len(minima_extended)}")
if gate_pass:
    print(f"    Barrier height: {barrier_height:.4f} M_KK ({barrier_pct:.2f}%)")
print(f"")
print(f"  DERIVATIVE DECOMPOSITION AT FOLD:")
print(f"    dF_cells/dtau    = {dF_cells[idx_fold]:+.4f}")
print(f"    dF_Josephson/dtau = {dF_Josephson[idx_fold]:+.4f}")
print(f"    dF_BA/dtau       = {dF_BA[idx_fold]:+.4f}")
print(f"    dF_fabric/dtau   = {dF_fabric[idx_fold]:+.4f}")
print(f"    Dominant: {dominant}")
print(f"")
print(f"  GATE: {gate_name} = {gate_verdict}")
print(f"  DETAIL: {gate_detail}")
print(f"{'='*72}")
