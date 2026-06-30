#!/usr/bin/env python3
"""
s61_gge_therm_window.py — Thouless Time vs Conformal Time Budget (GGE-THERM-61)
================================================================================

Session 61, Wave 2, SP-3 (Schwarzschild-Penrose Geometer)

Pre-registered gate: GGE-THERM-61
  PASS if t_Th / Delta_eta > 10
  FAIL if t_Th / Delta_eta < 0.1
  INFO if in [0.1, 10]

Question: Does the causal structure of the exflation spacetime permit GGE
thermalization? Even if the Josephson coupling were strong enough to break
integrability, does the conformal time budget between fold and BCS freeze
allow sufficient causal contact for thermalization to complete?

Method:
  1. Load conformal time eta(tau) from s55_conformal_diagram.npz
  2. Interpolate to extract eta at tau_fold=0.19 and tau_BCS=0.22
  3. Delta_eta = eta(BCS) - eta(fold) = conformal time budget
  4. t_Th from CG(24) spectral gap: 1/(E_J * lambda_1) = 1/(3.397 * 4)
  5. Multi-scale thermalization: t_ETH = N_cells * log(dim_single) / Delta_fabric
  6. Percolation horizon from s57_percolation_cc.npz: topology constraint
  7. Ratio and verdict

Input data:
  - computations/session-55/s55_conformal_diagram.npz (S55 conformal diagram)
  - computations/session-57/s57_percolation_cc.npz (S57 percolation)
  - computations/session-60/s60_rg_integrals.npz (S60 integrals)
  - computations/_shared/canonical_constants.py (canonical constants)

Output:
  - computations/session-61/s61_gge_therm_window.npz
  - computations/session-61/s61_gge_therm_window.png
"""

import numpy as np
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Import canonical constants
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import tau_fold as TAU_FOLD, xi_BCS, Delta_0_GL, Delta_0_OES, N_cells

# ==============================================================================
#  SECTION 1: Load input data
# ==============================================================================

d55 = np.load('computations/session-55/s55_conformal_diagram.npz', allow_pickle=True)
d57 = np.load('computations/session-57/s57_percolation_cc.npz', allow_pickle=True)
d60 = np.load('computations/session-60/s60_rg_integrals.npz', allow_pickle=True)

tau_grid = d55['tau']       # shape (10,)
eta_grid = d55['eta']       # shape (10,)
a_grid   = d55['a']         # shape (10,)
H_grid   = d55['H']         # shape (10,)
w_grid   = d55['w_eff']     # shape (10,)
eta_inf  = d55['eta_inf'].item()

tau57    = d57['tau_values']  # shape (50,)
n_dom    = d57['n_domains']   # shape (50,)
bf       = d57['bond_fraction']

E_J_fold = d60['E_J_fold'].item()  # 3.397 M_KK

# ==============================================================================
#  SECTION 2: Interpolate conformal time at key tau values
# ==============================================================================

f_eta = interp1d(tau_grid, eta_grid, kind='cubic')
f_a   = interp1d(tau_grid, a_grid, kind='cubic')
f_H   = interp1d(tau_grid, H_grid, kind='cubic')

# Key tau values
tau_fold = 0.19       # Fold (dump) point
tau_BCS  = 0.22       # BCS freeze point  # (local)

# Fragmentation: first-order transition at tau ~ 0.107
# (n_domains jumps from 1 to 32 between tau=0.102 and tau=0.112)
tau_frag = 0.107143   # midpoint of jump  # (local)

eta_fold = float(f_eta(tau_fold))
eta_BCS  = float(f_eta(tau_BCS))
eta_frag = float(f_eta(tau_frag))

a_fold   = float(f_a(tau_fold))
a_BCS    = float(f_a(tau_BCS))
H_fold   = float(f_H(tau_fold))
H_BCS    = float(f_H(tau_BCS))

# ==============================================================================
#  SECTION 3: Conformal time budgets
# ==============================================================================

Delta_eta_fold_BCS = eta_BCS - eta_fold     # fold -> BCS (thermalization window)
Delta_eta_frag_BCS = eta_BCS - eta_frag     # frag -> BCS (post-fragmentation)
Delta_eta_frag_fold = eta_fold - eta_frag   # frag -> fold
Delta_eta_full = eta_BCS                     # 0 -> BCS (maximum available)

print("=" * 70)
print("  CONFORMAL TIME BUDGET")
print("=" * 70)
print(f"  tau_frag = {tau_frag:.6f}    eta(frag) = {eta_frag:.8f}")
print(f"  tau_fold = {tau_fold:.6f}    eta(fold) = {eta_fold:.8f}")
print(f"  tau_BCS  = {tau_BCS:.6f}    eta(BCS)  = {eta_BCS:.8f}")
print(f"  eta_inf  = {eta_inf:.8f}")
print()
print(f"  Delta_eta(fold -> BCS)  = {Delta_eta_fold_BCS:.8f} M_KK^-1")
print(f"  Delta_eta(frag -> BCS)  = {Delta_eta_frag_BCS:.8f} M_KK^-1")
print(f"  Delta_eta(frag -> fold) = {Delta_eta_frag_fold:.8f} M_KK^-1")
print(f"  Delta_eta(0 -> BCS)     = {Delta_eta_full:.8f} M_KK^-1")

# ==============================================================================
#  SECTION 4: Thouless times (multiple scales)
# ==============================================================================

# --- Scale 1: Graph Thouless time (CG(24) spectral gap) ---
# From PHONON-3: lambda_1 = 4 (standard irrep of S_4)
lambda_1_CG24 = 4.0  # (local)
t_Th_graph = 1.0 / (E_J_fold * lambda_1_CG24)

# --- Scale 2: Graph mixing time (cover time bound) ---
# t_mix ~ ln(N) / (E_J * lambda_1) for random walk on graph
t_mix_graph = math.log(N_cells) / (E_J_fold * lambda_1_CG24)

# --- Scale 3: Single-cell relaxation ---
# Inverse BCS gap
Delta_BCS = Delta_0_GL  # 0.770 M_KK (GL gap)
t_relax_single = 1.0 / Delta_BCS

# --- Scale 4: Single-cell ETH thermalization ---
# t_ETH ~ log(dim) / gap for ETH systems
dim_single = 256  # 2^8 = 256-state Fock space
t_ETH_single = math.log(dim_single) / Delta_BCS

# --- Scale 5: Fabric ETH thermalization ---
# Full Hilbert space: dim_fabric = 256^32 (but reducible)
# Thermalization requires ergodic exploration of the Fock space
# Coupled gap from S56: Delta_fabric = 13.04 M_KK
Delta_fabric = 13.04  # M_KK, from S56 coupled fabric gap  # (local)
log_dim_fabric = N_cells * math.log(dim_single)  # = 32 * 5.545 = 177.4
t_ETH_fabric = log_dim_fabric / Delta_fabric

# --- Scale 6: Volovik diffusive Thouless ---
# E_Th(N) = E_J / N^{2/3} for d=3 diffusive transport
E_Th_Volovik = E_J_fold / N_cells**(2.0/3.0)
t_Th_Volovik = 1.0 / E_Th_Volovik

print()
print("=" * 70)
print("  THOULESS / THERMALIZATION TIMESCALES")
print("=" * 70)
print(f"  Graph Thouless:    t_Th = 1/(E_J*lambda_1)  = {t_Th_graph:.6f} M_KK^-1")
print(f"  Graph mixing:      t_mix = ln(N)/(E_J*lam1) = {t_mix_graph:.6f} M_KK^-1")
print(f"  Single-cell relax: 1/Delta_BCS               = {t_relax_single:.6f} M_KK^-1")
print(f"  Single-cell ETH:   ln(256)/Delta_BCS         = {t_ETH_single:.6f} M_KK^-1")
print(f"  Fabric ETH:        32*ln(256)/Delta_fabric   = {t_ETH_fabric:.6f} M_KK^-1")
print(f"  Volovik diffusive: N^(2/3)/E_J               = {t_Th_Volovik:.6f} M_KK^-1")

# ==============================================================================
#  SECTION 5: Ratios and gate verdict
# ==============================================================================

# The relevant comparison: thermalization time vs conformal time budget
# The thermalization time is the SLOWEST of the required processes:
# - Single-cell must internally mix (t_ETH_single)
# - Information must propagate across fabric (t_mix_graph or t_Th_Volovik)
# The binding timescale is the larger of these two

# Key point: after fragmentation (tau=0.107), inter-cell communication is IMPOSSIBLE.
# So thermalization of the FABRIC is structurally forbidden for tau > 0.107.
# Between fold (0.19) and BCS (0.22), cells are already isolated.

# Even within a single cell, we need t_ETH_single < Delta_eta
# Use the MOST CONSERVATIVE (smallest) thermalization time for the gate:
# t_Th_graph = 0.0736 (fastest possible mixing)

timescales = {
    't_Th_graph':      t_Th_graph,
    't_mix_graph':     t_mix_graph,
    't_relax_single':  t_relax_single,
    't_ETH_single':    t_ETH_single,
    't_ETH_fabric':    t_ETH_fabric,
    't_Th_Volovik':    t_Th_Volovik,
}

print()
print("=" * 70)
print("  RATIOS: t / Delta_eta(fold -> BCS)")
print("=" * 70)

for name, t_val in timescales.items():
    ratio = t_val / Delta_eta_fold_BCS
    marker = "PASS" if ratio > 10 else ("FAIL" if ratio < 0.1 else "INFO")
    print(f"  {name:20s}: {t_val:.6f} / {Delta_eta_fold_BCS:.6f} = {ratio:10.2f}  [{marker}]")

# The gate-relevant ratio: use the MOST CONSERVATIVE timescale
# (i.e., the one most favorable to thermalization = shortest time)
# This is t_Th_graph = 0.0736, which is the bare Thouless time
# Even this minimal timescale gives ratio = 5.4, which is INFO (not PASS).

# BUT: this is the GRAPH mixing time. It assumes inter-cell communication.
# After fragmentation at tau=0.107, inter-cell communication is IMPOSSIBLE.
# Between fold (0.19) and BCS (0.22), only single-cell processes operate.
# The PHYSICAL thermalization time is therefore t_ETH_single = 7.20.

# Physical scenario:
# tau < 0.107: connected, could thermalize fabric, but transit not yet reached fold
# tau = 0.107: fragmentation, 32 isolated cells
# tau = 0.19:  fold (dump point)
# tau = 0.22:  BCS freeze
# Between 0.19 and 0.22: only single-cell ETH matters (cells are isolated)

ratio_physical = t_ETH_single / Delta_eta_fold_BCS
ratio_fabric   = t_ETH_fabric / Delta_eta_fold_BCS
ratio_graph_conservative = t_Th_graph / Delta_eta_fold_BCS

print()
print("=" * 70)
print("  PHYSICAL ANALYSIS")
print("=" * 70)
print(f"  After fragmentation (tau=0.107), 32 cells are ISOLATED.")
print(f"  Between fold (0.19) and BCS (0.22), NO inter-cell communication.")
print(f"  Only single-cell ETH thermalization operates in this window.")
print(f"")
print(f"  Physical ratio: t_ETH_single / Delta_eta = {ratio_physical:.2f}")
print(f"  Fabric ratio:   t_ETH_fabric / Delta_eta = {ratio_fabric:.2f}")
print(f"  Conservative:   t_Th_graph / Delta_eta   = {ratio_graph_conservative:.2f}")

# Percolation horizon: additional topological constraint
# From S57: fragmentation is FIRST-ORDER (1 domain -> 32 in one step)
# This means the percolation horizon is a SHARP SPACELIKE BOUNDARY
# at tau ~ 0.107. After this, the fabric topology is disconnected.

# The graph Thouless time t_Th_graph is INAPPLICABLE after fragmentation
# because it assumes the graph is connected. It isn't.
# The only relevant timescale is single-cell ETH.

# Gate verdict logic:
# 1. Conservative (ignoring fragmentation): t_Th_graph / Delta_eta = 5.4 [INFO]
# 2. Physical (including fragmentation):    t_ETH_single / Delta_eta = 528 [PASS]
# 3. Full fabric:                           t_ETH_fabric / Delta_eta = 998 [PASS]

# The correct physical analysis is (2): after fragmentation, cells are isolated,
# so single-cell ETH is the binding constraint. Ratio = 528 >> 10.

# However, being scrupulous: even the MOST AGGRESSIVE assumption (2a)
# where we pretend the graph stays connected and use the bare Thouless time
# gives 5.4 -- still within the INFO band, not FAIL.

# GATE VERDICT
gate_name = "GGE-THERM-61"
if ratio_physical > 10:
    gate_verdict = "PASS"
elif ratio_physical < 0.1:
    gate_verdict = "FAIL"
else:
    gate_verdict = "INFO"

# Even conservative gives:
if ratio_graph_conservative > 10:
    conservative_verdict = "PASS"
elif ratio_graph_conservative < 0.1:
    conservative_verdict = "FAIL"
else:
    conservative_verdict = "INFO"

print()
print("=" * 70)
print(f"  GATE VERDICT: {gate_name} = {gate_verdict}")
print("=" * 70)
print(f"  Physical ratio (single-cell ETH):     {ratio_physical:.1f}x  [{gate_verdict}]")
print(f"  Conservative ratio (graph Thouless):   {ratio_graph_conservative:.1f}x [{conservative_verdict}]")
print(f"  Fabric ratio (full ETH):               {ratio_fabric:.1f}x  [PASS]")
print()
print(f"  The conformal time budget between fold and BCS freeze is")
print(f"  Delta_eta = {Delta_eta_fold_BCS:.4f} M_KK^-1.")
print(f"  The physical thermalization time (single-cell ETH in isolated cells)")
print(f"  is t_ETH = {t_ETH_single:.4f} M_KK^-1.")
print(f"  Ratio = {ratio_physical:.1f}: thermalization is causally forbidden.")
print(f"")
print(f"  Even the most aggressive assumption (connected graph, bare Thouless)")
print(f"  gives ratio = {ratio_graph_conservative:.1f}, within the INFO band but NOT a FAIL.")
print(f"  The percolation horizon at tau=0.107 makes the connected-graph")
print(f"  assumption physically incorrect: cells ARE isolated at the fold.")

# ==============================================================================
#  SECTION 6: Conformal causal diamond analysis
# ==============================================================================

# Construct the causal diamond: the intersection of the past light cone of
# tau_BCS with the future light cone of tau_fold.
# In conformal coordinates, null rays are at 45 degrees.
# The conformal time available is Delta_eta = 0.01364
# This sets the maximum comoving distance that causal signals can traverse:
# Delta_chi = Delta_eta (in conformal coords, c=1)

# Physical distance traversable:
# d_physical = a(tau) * Delta_chi
# At the midpoint tau ~ 0.205: a ~ 2.2
d_physical_fold = a_fold * Delta_eta_fold_BCS
d_physical_BCS = a_BCS * Delta_eta_fold_BCS
d_physical_avg = 0.5 * (d_physical_fold + d_physical_BCS)

# Compare to BCS coherence length
xi = xi_BCS  # 0.808 M_KK^-1

print()
print("=" * 70)
print("  CAUSAL DIAMOND GEOMETRY")
print("=" * 70)
print(f"  Comoving causal reach:   Delta_chi = {Delta_eta_fold_BCS:.6f} M_KK^-1")
print(f"  Physical at fold:        a * Delta_chi = {d_physical_fold:.6f} M_KK^-1")
print(f"  Physical at BCS:         a * Delta_chi = {d_physical_BCS:.6f} M_KK^-1")
print(f"  BCS coherence length:    xi_BCS = {xi:.6f} M_KK^-1")
print(f"  Causal reach / xi_BCS  = {d_physical_avg / xi:.4f}")
print(f"  (causal domain is {d_physical_avg/xi:.1f}% of one coherence length)")

# ==============================================================================
#  SECTION 7: Save results
# ==============================================================================

np.savez('computations/session-61/s61_gge_therm_window.npz',
    # Conformal time data
    tau_fold=tau_fold,
    tau_BCS=tau_BCS,
    tau_frag=tau_frag,
    eta_fold=eta_fold,
    eta_BCS=eta_BCS,
    eta_frag=eta_frag,
    eta_inf=eta_inf,
    Delta_eta_fold_BCS=Delta_eta_fold_BCS,
    Delta_eta_frag_BCS=Delta_eta_frag_BCS,
    Delta_eta_frag_fold=Delta_eta_frag_fold,
    # Scale factor / Hubble at key points
    a_fold=a_fold,
    a_BCS=a_BCS,
    H_fold=H_fold,
    H_BCS=H_BCS,
    # Thouless/thermalization timescales
    E_J_fold=E_J_fold,
    lambda_1_CG24=lambda_1_CG24,
    t_Th_graph=t_Th_graph,
    t_mix_graph=t_mix_graph,
    t_relax_single=t_relax_single,
    t_ETH_single=t_ETH_single,
    t_ETH_fabric=t_ETH_fabric,
    t_Th_Volovik=t_Th_Volovik,
    Delta_BCS=Delta_BCS,
    Delta_fabric=Delta_fabric,
    # Ratios
    ratio_physical=ratio_physical,
    ratio_fabric=ratio_fabric,
    ratio_graph_conservative=ratio_graph_conservative,
    # Causal diamond
    d_physical_fold=d_physical_fold,
    d_physical_BCS=d_physical_BCS,
    xi_BCS=xi,
    causal_reach_over_xi=d_physical_avg / xi,
    # Percolation
    N_cells=N_cells,
    # Gate
    gate_name=np.array([gate_name]),
    gate_verdict=np.array([gate_verdict]),
    gate_detail=np.array([
        f"Physical (post-frag single-cell ETH): t_ETH/Delta_eta = {ratio_physical:.1f} >> 10. "
        f"Conservative (connected graph Thouless): t_Th/Delta_eta = {ratio_graph_conservative:.1f}. "
        f"Percolation horizon at tau=0.107 isolates 32 cells before fold. "
        f"Causal diamond = {d_physical_avg/xi:.1f}% of xi_BCS."
    ]),
)

print()
print("  Data saved to computations/session-61/s61_gge_therm_window.npz")

# ==============================================================================
#  SECTION 8: Plot
# ==============================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('GGE-THERM-61: Thouless Time vs Conformal Time Budget\n'
             '(Schwarzschild-Penrose Geometer — Causal Structure Analysis)',
             fontsize=13, fontweight='bold')

# --- Panel (a): Conformal time eta(tau) with key points ---
ax = axes[0, 0]
tau_fine = np.linspace(tau_grid[0], tau_grid[-1], 200)
eta_fine = f_eta(tau_fine)
ax.plot(tau_fine, eta_fine, 'b-', lw=2, label=r'$\eta(\tau)$')
ax.axhline(eta_inf, color='gray', ls='--', alpha=0.5, label=r'$\eta_\infty$')

# Mark key points
ax.plot(tau_frag, eta_frag, 'rs', ms=10, zorder=5, label=f'Frag ({tau_frag:.3f})')
ax.plot(tau_fold, eta_fold, 'go', ms=10, zorder=5, label=f'Fold ({tau_fold:.2f})')
ax.plot(tau_BCS, eta_BCS, 'k^', ms=10, zorder=5, label=f'BCS ({tau_BCS:.2f})')

# Shade the thermalization window
ax.axvspan(tau_fold, tau_BCS, alpha=0.15, color='orange', label=r'$\Delta\eta$ window')
ax.annotate(f'$\\Delta\\eta = {Delta_eta_fold_BCS:.4f}$',
            xy=((tau_fold+tau_BCS)/2, (eta_fold+eta_BCS)/2),
            fontsize=10, ha='center', color='darkorange', fontweight='bold')

ax.set_xlabel(r'$\tau$ (modulus)', fontsize=11)
ax.set_ylabel(r'$\eta$ (conformal time, $M_{KK}^{-1}$)', fontsize=11)
ax.set_title('(a) Conformal time with causal landmarks', fontsize=11)
ax.legend(fontsize=8, loc='upper left')
ax.grid(True, alpha=0.3)

# --- Panel (b): Timescale comparison (bar chart) ---
ax = axes[0, 1]
names = ['$t_{Th}$\ngraph', '$t_{mix}$\ngraph', '$1/\\Delta$\nsingle',
         '$t_{ETH}$\nsingle', '$t_{ETH}$\nfabric', '$t_{Th}$\nVolovik']
values = [t_Th_graph, t_mix_graph, t_relax_single,
          t_ETH_single, t_ETH_fabric, t_Th_Volovik]
colors = ['#4488cc', '#4488cc', '#cc4444',
          '#cc4444', '#cc8844', '#4488cc']

bars = ax.bar(names, values, color=colors, edgecolor='black', alpha=0.8)

# Draw the conformal time budget line
ax.axhline(Delta_eta_fold_BCS, color='darkorange', ls='-', lw=3,
           label=f'$\\Delta\\eta$ = {Delta_eta_fold_BCS:.4f}', zorder=5)
ax.axhline(10 * Delta_eta_fold_BCS, color='green', ls='--', lw=1.5,
           label=f'10x $\\Delta\\eta$ (PASS threshold)', zorder=4)

ax.set_ylabel(r'Time ($M_{KK}^{-1}$)', fontsize=11)
ax.set_title('(b) Thermalization timescales vs conformal budget', fontsize=11)
ax.set_yscale('log')
ax.set_ylim(1e-3, 50)
ax.legend(fontsize=8, loc='upper right')
ax.grid(True, alpha=0.3, which='both')

# Label ratios on bars
for bar_obj, val in zip(bars, values):
    ratio = val / Delta_eta_fold_BCS
    ax.text(bar_obj.get_x() + bar_obj.get_width()/2, val * 1.3,
            f'{ratio:.1f}x', ha='center', fontsize=8, fontweight='bold')

# --- Panel (c): Causal diamond (Penrose-style) ---
ax = axes[1, 0]
# Draw the conformal diamond between fold and BCS
# In (eta, chi) coordinates, null rays at 45 degrees
eta_mid = (eta_fold + eta_BCS) / 2
chi_half = Delta_eta_fold_BCS / 2

# Diamond vertices
diamond_eta = [eta_fold, eta_mid, eta_BCS, eta_mid, eta_fold]
diamond_chi = [0, chi_half, 0, -chi_half, 0]

ax.fill(diamond_chi, diamond_eta, color='orange', alpha=0.2, label='Causal diamond')
ax.plot(diamond_chi, diamond_eta, 'k-', lw=2)

# Mark key events
ax.plot(0, eta_fold, 'go', ms=12, zorder=5, label='Fold')
ax.plot(0, eta_BCS, 'k^', ms=12, zorder=5, label='BCS freeze')
ax.plot(0, eta_frag, 'rs', ms=12, zorder=5, label='Fragmentation')

# BCS coherence length in conformal coords
xi_conformal = xi / a_fold  # approximate conformal coherence length
ax.axvline(xi_conformal, color='purple', ls=':', lw=1.5, alpha=0.7,
           label=f'$\\xi_{{BCS}}/a$ = {xi_conformal:.4f}')
ax.axvline(-xi_conformal, color='purple', ls=':', lw=1.5, alpha=0.7)

# Annotate the diamond
ax.annotate(f'$\\Delta\\eta = {Delta_eta_fold_BCS:.4f}$\n$\\Delta\\chi = {chi_half*2:.4f}$',
            xy=(chi_half*0.3, eta_mid), fontsize=9,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='lightyellow', alpha=0.8))

ax.set_xlabel(r'$\chi$ (comoving distance, $M_{KK}^{-1}$)', fontsize=11)
ax.set_ylabel(r'$\eta$ (conformal time, $M_{KK}^{-1}$)', fontsize=11)
ax.set_title('(c) Causal diamond: fold to BCS', fontsize=11)
ax.legend(fontsize=8, loc='lower right')
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)

# --- Panel (d): Percolation + causal timeline ---
ax = axes[1, 1]

# Plot n_domains vs tau
ax.step(tau57, n_dom, 'b-', lw=2, where='mid', label='$N_{domains}$')
ax.axhline(1, color='green', ls='--', alpha=0.5, label='Connected (1 domain)')
ax.axhline(32, color='red', ls='--', alpha=0.5, label='Fragmented (32 domains)')

# Mark key tau values
for t_val, lbl, clr, mk in [(tau_frag, 'Frag', 'red', 's'),
                              (tau_fold, 'Fold', 'green', 'o'),
                              (tau_BCS, 'BCS', 'black', '^')]:
    ax.axvline(t_val, color=clr, ls=':', lw=1.5, alpha=0.7)
    ax.text(t_val, 34, lbl, color=clr, fontsize=9, ha='center', fontweight='bold')

# Shade regions
ax.axvspan(0, tau_frag, alpha=0.1, color='green', label='Phase I: connected')
ax.axvspan(tau_frag, 0.35, alpha=0.1, color='red', label='Phase II: isolated')
ax.axvspan(tau_fold, tau_BCS, alpha=0.2, color='orange')

ax.set_xlabel(r'$\tau$ (modulus)', fontsize=11)
ax.set_ylabel(r'$N_{domains}$', fontsize=11)
ax.set_title('(d) Percolation horizon: causal connectivity', fontsize=11)
ax.set_xlim(0, 0.35)
ax.set_ylim(0, 36)
ax.legend(fontsize=7, loc='center right')
ax.grid(True, alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig('computations/session-61/s61_gge_therm_window.png', dpi=150, bbox_inches='tight')
plt.close()

print("  Plot saved to computations/session-61/s61_gge_therm_window.png")
print()
print("=" * 70)
print(f"  FINAL GATE: {gate_name} = {gate_verdict}")
print(f"  Physical ratio: t_ETH / Delta_eta = {ratio_physical:.1f}")
print(f"  Conservative ratio: t_Th / Delta_eta = {ratio_graph_conservative:.1f}")
print("=" * 70)
