#!/usr/bin/env python3
"""
S56 BKT-TEST-56: Berezinskii-Kosterlitz-Thouless Temperature vs T_GH
=====================================================================

Physics:
  The BKT transition governs the onset of topological (vortex-antivortex)
  order in 2D systems with U(1) symmetry. On the 32-cell Voronoi graph
  of SU(3) irreps, the Cooper pair condensate has a U(1)_7 phase degree
  of freedom at each cell. Josephson coupling between cells provides
  phase stiffness. The BKT temperature sets the scale below which
  vortex-antivortex pairs are bound, and superconducting (or superfluid)
  long-range order survives.

  T_BKT = (pi/2) * rho_s, where rho_s is the superfluid stiffness.
  For a Josephson junction array: rho_s = E_J(tau), the effective
  Josephson energy.

  E_J(tau) = J_C2(tau)^2 * F_anomalous(tau)

  where F_anomalous = Sum_k Delta / (2 * E_qp_k^2) is the anomalous
  Green's function integrated over the Matsubara shell. Here:
    E_qp_k = sqrt((epsilon_k - mu)^2 + Delta^2)
  with epsilon_k the tight-binding eigenvalues of the 32-cell graph,
  mu = chemical potential (half-filling convention), and
  Delta = 0.4643 (canonical OES gap).

  The Gibbons-Hawking temperature T_GH = H(tau)/(2*pi) provides
  a geometric temperature scale. If T_GH crosses T_BKT at some tau,
  the thermal fluctuations from the expanding geometry destroy
  vortex binding -- a phase transition on the fabric.

  d_s = 2 context: The graph Laplacian spectral dimension reaches
  d_s ~ 2 at intermediate diffusion times (S54 GRAPH-LAPLACIAN-DS-54),
  making BKT the relevant universality class for phase ordering.

Gate: BKT-CROSSING-56
  INFO: If T_GH/T_BKT crossing found in tau in [0.05, 0.40], flag
  for fabric phase transition analysis.

Author: landau-condensed-matter-theorist (Session 56, Wave 0)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
from numpy import pi, sqrt, exp
from scipy.interpolate import interp1d
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import (
    tau_fold, Delta_0_OES, J_C2 as J_C2_fold,
    N_cells, T_acoustic, E_cond,
)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_NPZ = os.path.join(SCRIPT_DIR, "s56_bkt_test.npz")
OUT_PNG = os.path.join(SCRIPT_DIR, "s56_bkt_test.png")
OUT_TXT = os.path.join(SCRIPT_DIR, "s56_bkt_test_output.txt")

# ============================================================
# Output tee
# ============================================================
class Tee:
    def __init__(self, filename):
        self.file = open(filename, 'w')
        self.stdout = sys.stdout
    def write(self, data):
        self.file.write(data)
        self.stdout.write(data)
    def flush(self):
        self.file.flush()
        self.stdout.flush()

sys.stdout = Tee(OUT_TXT)

print("=" * 72)
print("S56 BKT-TEST-56: BKT Temperature vs Gibbons-Hawking Temperature")
print("=" * 72)

# ============================================================
# Section 1: Load tight-binding data
# ============================================================
print("\n--- Section 1: Load tight-binding Hamiltonian data ---")

tb_path = os.path.join(SCRIPT_DIR, "s54_tb_hamiltonian.npz")
tb_data = np.load(tb_path, allow_pickle=True)

tau_tb = tb_data['tau_values']         # (50,)
eigenvalues = tb_data['eigenvalues']   # (50, 32) -- TB eigenvalues
J_C2_tau = tb_data['J_C2_tau']         # (50,) -- Josephson coupling vs tau
N = int(tb_data['N_cells'])

print(f"  tau range: [{tau_tb[0]:.4f}, {tau_tb[-1]:.4f}], N_points = {len(tau_tb)}")
print(f"  N_cells = {N}")
print(f"  J_C2 range: [{J_C2_tau.min():.6f}, {J_C2_tau.max():.6f}] M_KK")

# ============================================================
# Section 2: Load scale factor / Hubble data
# ============================================================
print("\n--- Section 2: Load scale factor data ---")

sf_path = os.path.join(SCRIPT_DIR, "s54_scale_factor.npz")
sf_data = np.load(sf_path, allow_pickle=True)

tau_sf = sf_data['tau']   # (10,) -- sparse
H_sf = sf_data['H']       # (10,) -- Hubble parameter in M_KK units

print(f"  Scale factor tau range: [{tau_sf[0]:.4f}, {tau_sf[-1]:.4f}], N_points = {len(tau_sf)}")
print(f"  H range: [{H_sf.min():.4f}, {H_sf.max():.4f}] M_KK")

# Interpolate H(tau) to the fine 50-point tau grid
# Use cubic interpolation (R^2 = 0.997 for exponential fit, so smooth)
H_interp_func = interp1d(tau_sf, H_sf, kind='cubic', fill_value='extrapolate')
H_tau = H_interp_func(tau_tb)

print(f"  Interpolated H range: [{H_tau.min():.4f}, {H_tau.max():.4f}] M_KK")

# ============================================================
# Section 3: Compute E_J(tau) and T_BKT(tau)
# ============================================================
print("\n--- Section 3: Josephson energy and BKT temperature ---")

Delta = Delta_0_OES  # BCS gap, M_KK units (OES/pair-addition gap)
print(f"  BCS gap Delta = {Delta:.6f} M_KK")

# For each tau, compute F_anomalous = Sum_k Delta / (2 * E_qp_k^2)
# E_qp_k = sqrt((epsilon_k - mu)^2 + Delta^2)
# mu = chemical potential at half-filling: mu = (epsilon_min + epsilon_max)/2
# But we have N_pair = 1 Cooper pair on N=32 sites (very dilute limit).
# In the dilute limit, mu is at the bottom of the band.
# More precisely: for N_pair = 1 on 32 sites, filling fraction = 1/32 ~ 3%.
# The BCS state has occupation ~1 near the Fermi energy and ~0 above.
# For consistency with the BCS framework used in S35-S38 (which is at
# the gap edge of the Dirac spectrum, not the TB spectrum), we need
# to use the correct chemical potential.
#
# Physical interpretation: The TB eigenvalues are single-particle hopping
# energies on the graph. With one Cooper pair, the relevant quasiparticle
# energies are measured from the chemical potential at the lowest level.
# For the anomalous Green's function, we sum over ALL k-states.

E_J_tau = np.zeros(len(tau_tb))
F_anom_tau = np.zeros(len(tau_tb))
mu_tau = np.zeros(len(tau_tb))

for i, tau in enumerate(tau_tb):
    eps = eigenvalues[i]  # 32 eigenvalues, sorted ascending

    # Chemical potential: for dilute limit (1 pair on 32 sites),
    # mu sits at the bottom of the band. Use mu = eps[0] (ground state).
    # BCS: all states contribute to the anomalous function.
    mu = eps[0]  # (local)
    mu_tau[i] = mu

    # Quasiparticle energies
    xi_k = eps - mu  # measured from Fermi level
    E_qp = sqrt(xi_k**2 + Delta**2)

    # Anomalous Green's function kernel
    # F_anomalous = Sum_k Delta / (2 * E_qp_k^2)
    # This is the standard BCS anomalous self-energy sum (Ambegaokar-Baratoff)
    F_anom = np.sum(Delta / (2.0 * E_qp**2))
    F_anom_tau[i] = F_anom

    # E_J = J_C2^2 * F_anomalous
    # The factor of J_C2^2 comes from second-order tunneling: the Josephson
    # energy of a single junction is E_J = J^2 * chi_pair, where chi_pair
    # is the pair susceptibility (anomalous Green's function).
    E_J = J_C2_tau[i]**2 * F_anom
    E_J_tau[i] = E_J

print(f"  F_anomalous range: [{F_anom_tau.min():.6f}, {F_anom_tau.max():.6f}]")
print(f"  E_J range: [{E_J_tau.min():.6f}, {E_J_tau.max():.6f}] M_KK")

# BKT temperature: T_BKT = (pi/2) * E_J
# This is the Nelson-Kosterlitz universal jump relation for a 2D system:
# rho_s(T_BKT^-) = (2/pi) * T_BKT
# For an XY model on a lattice: T_BKT = (pi/2) * J_eff
# where J_eff = E_J for the Josephson junction array.
T_BKT_tau = (pi / 2.0) * E_J_tau

print(f"  T_BKT range: [{T_BKT_tau.min():.6f}, {T_BKT_tau.max():.6f}] M_KK")

# ============================================================
# Section 4: Compute T_GH(tau)
# ============================================================
print("\n--- Section 4: Gibbons-Hawking temperature ---")

# T_GH = H(tau) / (2*pi) -- the de Sitter horizon temperature
# In units of M_KK (H is already in M_KK units from scale factor data)
T_GH_tau = H_tau / (2.0 * pi)

print(f"  T_GH range: [{T_GH_tau.min():.4f}, {T_GH_tau.max():.4f}] M_KK")

# ============================================================
# Section 5: Find crossings and analyze
# ============================================================
print("\n--- Section 5: Crossing analysis ---")

ratio = T_GH_tau / T_BKT_tau
print(f"  T_GH/T_BKT range: [{ratio.min():.6f}, {ratio.max():.6f}]")

# Find crossings: where T_GH - T_BKT changes sign
diff = T_GH_tau - T_BKT_tau
crossings = []
for j in range(len(diff) - 1):
    if diff[j] * diff[j+1] < 0:
        # Linear interpolation for crossing tau
        tau_cross = tau_tb[j] + (tau_tb[j+1] - tau_tb[j]) * abs(diff[j]) / (abs(diff[j]) + abs(diff[j+1]))
        T_cross = np.interp(tau_cross, tau_tb, T_GH_tau)
        crossings.append((tau_cross, T_cross))
        print(f"  CROSSING at tau = {tau_cross:.6f}, T = {T_cross:.6f} M_KK")

if len(crossings) == 0:
    print("  NO CROSSINGS found in tau range [0.00, 0.50]")
    if np.all(T_GH_tau > T_BKT_tau):
        print("  T_GH > T_BKT everywhere: fabric is in the DISORDERED (vortex-unbound) phase")
        print("  Geometric temperature always exceeds vortex binding scale")
    else:
        print("  T_GH < T_BKT everywhere: fabric is in the ORDERED (vortex-bound) phase")
        print("  Geometric temperature never reaches vortex unbinding")

# Check specifically in the gate range [0.05, 0.40]
gate_crossings = [c for c in crossings if 0.05 <= c[0] <= 0.40]
if gate_crossings:
    gate_status = "FLAG"
    print(f"\n  *** CROSSINGS IN GATE RANGE [0.05, 0.40]: {len(gate_crossings)} ***")
    for tc, Tc in gate_crossings:
        print(f"      tau = {tc:.6f}, T = {Tc:.6f} M_KK")
else:
    gate_status = "NO_CROSSING"
    print(f"\n  No crossings in gate range [0.05, 0.40]")

# Ratio at fold
fold_idx = np.argmin(np.abs(tau_tb - tau_fold))
tau_at_fold = tau_tb[fold_idx]
ratio_at_fold = ratio[fold_idx]
T_BKT_at_fold = T_BKT_tau[fold_idx]
T_GH_at_fold = T_GH_tau[fold_idx]
E_J_at_fold = E_J_tau[fold_idx]

print(f"\n  At fold (tau = {tau_at_fold:.4f}):")
print(f"    E_J         = {E_J_at_fold:.6f} M_KK")
print(f"    T_BKT       = {T_BKT_at_fold:.6f} M_KK")
print(f"    T_GH        = {T_GH_at_fold:.6f} M_KK")
print(f"    T_GH/T_BKT  = {ratio_at_fold:.4f}")
print(f"    J_C2        = {J_C2_tau[fold_idx]:.6f} M_KK")
print(f"    F_anomalous = {F_anom_tau[fold_idx]:.6f}")

# Find T_BKT minimum
idx_min = np.argmin(T_BKT_tau)
print(f"\n  T_BKT minimum:")
print(f"    tau_min     = {tau_tb[idx_min]:.4f}")
print(f"    T_BKT(min)  = {T_BKT_tau[idx_min]:.6f} M_KK")
print(f"    T_GH at min = {T_GH_tau[idx_min]:.6f} M_KK")
print(f"    ratio       = {T_GH_tau[idx_min] / T_BKT_tau[idx_min]:.4f}")

# Find T_BKT maximum
idx_max = np.argmax(T_BKT_tau)
print(f"\n  T_BKT maximum:")
print(f"    tau_max     = {tau_tb[idx_max]:.4f}")
print(f"    T_BKT(max)  = {T_BKT_tau[idx_max]:.6f} M_KK")

# ============================================================
# Section 6: Separation of scales analysis
# ============================================================
print("\n--- Section 6: Scale separation ---")

# Compare T_BKT to the acoustic temperature (GGE)
print(f"  T_acoustic (GGE) = {T_acoustic:.6f} M_KK")
print(f"  T_BKT(fold)/T_acoustic = {T_BKT_at_fold/T_acoustic:.4f}")
print(f"  T_GH(fold)/T_acoustic  = {T_GH_at_fold/T_acoustic:.4f}")

# The BKT temperature should be compared to E_J and Delta
print(f"\n  Delta (BCS gap) = {Delta:.6f} M_KK")
print(f"  T_BKT(fold)/Delta = {T_BKT_at_fold/Delta:.4f}")
print(f"  T_GH(fold)/Delta  = {T_GH_at_fold/Delta:.4f}")

# Order of magnitude: if T_GH >> T_BKT, vortices always unbound
# If T_GH << T_BKT, phase order survives the expansion
# If T_GH ~ T_BKT, there IS a phase transition during transit

print(f"\n  Separation factor: T_GH/T_BKT spans [{ratio.min():.2f}, {ratio.max():.2f}]")
if ratio.max() > 1 and ratio.min() < 1:
    print("  => PHASE TRANSITION EXISTS: T_GH crosses T_BKT during transit")
elif np.all(ratio > 1):
    magnitude = np.log10(ratio.min())
    print(f"  => T_GH DOMINATES: vortices always unbound (min log10(ratio)={magnitude:.2f})")
else:
    magnitude = np.log10(ratio.max())
    print(f"  => T_BKT DOMINATES: phase order always survives (max log10(ratio)={magnitude:.2f})")

# ============================================================
# Section 7: Effective coordination number analysis
# ============================================================
print("\n--- Section 7: Graph coordination for BKT context ---")

adj = tb_data['adjacency'].astype(float)
coordination = adj.sum(axis=1)
z_mean = coordination.mean()
z_min = coordination.min()
z_max = coordination.max()
print(f"  Mean coordination z = {z_mean:.2f}")
print(f"  Coordination range: [{z_min:.0f}, {z_max:.0f}]")
print(f"  For BKT on lattice with z neighbors: T_BKT ~ (pi/2) * E_J")
print(f"  (This is the z-independent universal relation; z enters via")
print(f"   the renormalization of rho_s from the bare value)")

# Refinement: the effective stiffness on an inhomogeneous lattice
# is rho_s_eff ~ z_eff * E_J / 2 for nearest-neighbor XY model.
# For triangular lattice (z=6), T_BKT/J = pi*z/4 = 4.71.
# For square lattice (z=4), T_BKT/J = pi*z/4 = 3.14.
# The universal jump is: rho_s(T_BKT^-) = (2/pi)*T_BKT.
# For the bare XY model with z neighbors, rho_s_bare = z*J/2.
# After renormalization: T_BKT ~ 0.89 * J for z=4 (square),
# ~ 1.5 * J for z=6 (triangular). Monte Carlo gives:
#   Square:     T_BKT = 0.8929 J
#   Triangular: T_BKT = 1.498 J
#   Honeycomb:  T_BKT = 0.572 J
# We use z_eff * J * pi/4 as the estimate, with z_eff from the
# actual graph. This overestimates T_BKT slightly relative to MC.

# But the truly correct expression is just T_BKT = (pi/2)*rho_s
# where rho_s is the STIFFNESS, not the coupling. For the bare model,
# rho_s = E_J on a square lattice. On a general graph, we need the
# stiffness from linear response. For this first computation, we use
# the standard T_BKT = (pi/2)*E_J as specified in the task.

# Also compute the z-corrected version for comparison
# T_BKT_corrected = (pi/4) * z_eff * E_J (mean-field BKT with coordination)
T_BKT_z_corr = (pi / 4.0) * z_mean * E_J_tau
print(f"\n  z-corrected T_BKT at fold: {T_BKT_z_corr[fold_idx]:.6f} M_KK")
print(f"  z-corrected ratio: {T_GH_tau[fold_idx]/T_BKT_z_corr[fold_idx]:.4f}")

# ============================================================
# Section 8: Gate verdict
# ============================================================
print("\n--- Section 8: Gate verdict ---")

print(f"\n  Gate: BKT-CROSSING-56")
if gate_crossings:
    print(f"  Verdict: INFO -- CROSSING FOUND")
    print(f"  {len(gate_crossings)} crossing(s) in [0.05, 0.40]")
    for tc, Tc in gate_crossings:
        print(f"    tau = {tc:.6f}, T = {Tc:.6f} M_KK")
    print(f"  => Phase transition in fabric during transit")
else:
    print(f"  Verdict: INFO -- NO CROSSING in [0.05, 0.40]")
    if np.all(ratio > 1):
        print(f"  T_GH > T_BKT at all tau: fabric always above BKT")
        print(f"  Vortices always unbound. No phase-coherent regime")
        print(f"  Minimum T_GH/T_BKT = {ratio.min():.2f} at tau = {tau_tb[np.argmin(ratio)]:.4f}")
    elif np.all(ratio < 1):
        print(f"  T_GH < T_BKT at all tau: fabric always below BKT")
        print(f"  Phase coherence survives throughout transit")
        print(f"  Maximum T_GH/T_BKT = {ratio.max():.2f} at tau = {tau_tb[np.argmax(ratio)]:.4f}")

# ============================================================
# Section 9: Save data
# ============================================================
print("\n--- Section 9: Save results ---")

np.savez(OUT_NPZ,
    # Grid
    tau=tau_tb,
    tau_fold=tau_fold,
    fold_idx=fold_idx,
    # Physical quantities
    E_J=E_J_tau,
    F_anomalous=F_anom_tau,
    J_C2=J_C2_tau,
    mu=mu_tau,
    Delta=Delta,
    # Temperatures
    T_BKT=T_BKT_tau,
    T_GH=T_GH_tau,
    H_interp=H_tau,
    T_BKT_z_corrected=T_BKT_z_corr,
    # Ratio
    ratio_TGH_TBKT=ratio,
    # Crossings
    n_crossings=len(crossings),
    crossings_tau=np.array([c[0] for c in crossings]) if crossings else np.array([]),
    crossings_T=np.array([c[1] for c in crossings]) if crossings else np.array([]),
    n_gate_crossings=len(gate_crossings),
    # At fold
    ratio_at_fold=ratio_at_fold,
    T_BKT_at_fold=T_BKT_at_fold,
    T_GH_at_fold=T_GH_at_fold,
    E_J_at_fold=E_J_at_fold,
    # Minimum
    tau_BKT_min=tau_tb[idx_min],
    T_BKT_min=T_BKT_tau[idx_min],
    # Coordination
    z_mean=z_mean,
    # Gate
    gate_name="BKT-CROSSING-56",
    gate_verdict=gate_status,
)

print(f"  Saved: {OUT_NPZ}")

# ============================================================
# Section 10: Plot
# ============================================================
print("\n--- Section 10: Generate plot ---")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("BKT-TEST-56: BKT Temperature vs Gibbons-Hawking Temperature",
             fontsize=13, fontweight='bold')

# Panel (a): T_BKT and T_GH vs tau
ax = axes[0, 0]
ax.plot(tau_tb, T_BKT_tau, 'b-', linewidth=2, label=r'$T_{\mathrm{BKT}}(\tau) = \frac{\pi}{2} E_J(\tau)$')
ax.plot(tau_tb, T_GH_tau, 'r--', linewidth=2, label=r'$T_{\mathrm{GH}}(\tau) = H(\tau)/(2\pi)$')
ax.plot(tau_tb, T_BKT_z_corr, 'b:', linewidth=1.5, alpha=0.6,
        label=r'$T_{\mathrm{BKT}}^{(z)} = \frac{\pi}{4} \bar{z} \, E_J$')
ax.axvline(tau_fold, color='green', linestyle=':', alpha=0.5, label=r'$\tau_{\mathrm{fold}}$')
for tc, Tc in crossings:
    ax.plot(tc, Tc, 'ko', markersize=10, zorder=5)
    ax.annotate(f'crossing\n$\\tau={tc:.3f}$', xy=(tc, Tc),
                xytext=(tc+0.03, Tc*1.3), fontsize=9,
                arrowprops=dict(arrowstyle='->', color='black'))
ax.set_xlabel(r'$\tau$', fontsize=12)
ax.set_ylabel(r'Temperature ($M_{\mathrm{KK}}$)', fontsize=12)
ax.set_title('(a) Temperature scales', fontsize=11)
ax.legend(fontsize=9, loc='best')
ax.set_xlim(0, 0.5)
ax.grid(True, alpha=0.3)

# Panel (b): Ratio T_GH / T_BKT
ax = axes[0, 1]
ax.semilogy(tau_tb, ratio, 'k-', linewidth=2)
ax.axhline(1.0, color='red', linestyle='--', alpha=0.5, label='$T_{GH}/T_{BKT}=1$')
ax.axvline(tau_fold, color='green', linestyle=':', alpha=0.5, label=r'$\tau_{\mathrm{fold}}$')
ax.fill_between([0.05, 0.40], 0.01, 1000, color='yellow', alpha=0.1, label='Gate range')
ax.set_xlabel(r'$\tau$', fontsize=12)
ax.set_ylabel(r'$T_{\mathrm{GH}} / T_{\mathrm{BKT}}$', fontsize=12)
ax.set_title('(b) Temperature ratio', fontsize=11)
ax.legend(fontsize=9, loc='best')
ax.set_xlim(0, 0.5)
ax.grid(True, alpha=0.3)

# Panel (c): Josephson energy E_J and its components
ax = axes[1, 0]
ax2 = ax.twinx()
ax.plot(tau_tb, J_C2_tau, 'g-', linewidth=2, label=r'$J_{C^2}(\tau)$')
ax.plot(tau_tb, J_C2_tau**2, 'g--', linewidth=1.5, alpha=0.7, label=r'$J_{C^2}^2(\tau)$')
ax2.plot(tau_tb, F_anom_tau, 'm-', linewidth=2, label=r'$F_{\mathrm{anom}}(\tau)$')
ax.axvline(tau_fold, color='green', linestyle=':', alpha=0.5)
ax.set_xlabel(r'$\tau$', fontsize=12)
ax.set_ylabel(r'Josephson coupling ($M_{\mathrm{KK}}$)', fontsize=12, color='green')
ax2.set_ylabel(r'$F_{\mathrm{anomalous}}$', fontsize=12, color='purple')
ax.set_title('(c) E_J components', fontsize=11)
ax.legend(fontsize=9, loc='upper right')
ax2.legend(fontsize=9, loc='center right')
ax.set_xlim(0, 0.5)
ax.grid(True, alpha=0.3)

# Panel (d): E_J(tau) directly
ax = axes[1, 1]
ax.plot(tau_tb, E_J_tau, 'b-', linewidth=2, label=r'$E_J(\tau) = J_{C^2}^2 \cdot F_{\mathrm{anom}}$')
ax.axvline(tau_fold, color='green', linestyle=':', alpha=0.5, label=r'$\tau_{\mathrm{fold}}$')
ax.set_xlabel(r'$\tau$', fontsize=12)
ax.set_ylabel(r'$E_J$ ($M_{\mathrm{KK}}$)', fontsize=12)
ax.set_title('(d) Effective Josephson energy', fontsize=11)
ax.legend(fontsize=9, loc='best')
ax.set_xlim(0, 0.5)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(OUT_PNG, dpi=150, bbox_inches='tight')
print(f"  Saved: {OUT_PNG}")

# ============================================================
# Summary
# ============================================================
print("\n" + "=" * 72)
print("SUMMARY: BKT-TEST-56")
print("=" * 72)
print(f"  Delta (BCS gap)   = {Delta:.6f} M_KK")
print(f"  E_J at fold       = {E_J_at_fold:.6f} M_KK")
print(f"  T_BKT at fold     = {T_BKT_at_fold:.6f} M_KK")
print(f"  T_GH at fold      = {T_GH_at_fold:.4f} M_KK")
print(f"  T_GH/T_BKT(fold)  = {ratio_at_fold:.2f}")
print(f"  T_BKT minimum     = {T_BKT_tau[idx_min]:.6f} M_KK at tau = {tau_tb[idx_min]:.4f}")
print(f"  Crossings total   = {len(crossings)}")
print(f"  Crossings in gate = {len(gate_crossings)}")
print(f"  Gate verdict      = {gate_status}")
print("=" * 72)
