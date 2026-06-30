"""
s61_gge_therm.py — GGE Thermalization via Thouless Time Scaling (GGE-THERM-61)

Gate: PASS if t_Th > 10 * t_transit at N=32. FAIL if < 0.1 * t_transit. INFO otherwise.

Physics:
    The Thouless energy E_Th(N) = D / L^2 measures how fast information diffuses
    across a disordered/coupled system of size L ~ N^{1/3} (in d=3).
    For a lattice with diffusion constant D = E_J * a^2 / hbar (a = lattice spacing = 1):
        E_Th(N) = E_J / N^{2/3}
        t_Th(N) = 1 / E_Th(N) = N^{2/3} / E_J

    E_J = 3.40 M_KK is the per-bond Josephson coupling (pair transfer amplitude).
    The total Josephson energy is E_J_total = N_bonds * E_J = 93 * 7.04 = 655 M_KK,
    but Thouless scaling uses the per-bond coupling as the diffusion hopping rate.

3He-B perspective:
    In 3He-B, the Leggett frequency omega_L plays the role of E_J.
    When omega_L >> Delta (gap), the system thermalizes rapidly.
    Here E_J/Delta = 3.40/0.77 = 4.4, which is NOT the >> limit.
    This is a genuine race between diffusion and transit.

Also computes Fermi golden rule quasiparticle scattering rate:
    Gamma_qp = 2*pi * |V_J|^2 * rho(E_F)

Author: Volovik-Superfluid-Universe-Theorist (S61)
"""

import numpy as np
import matplotlib.pyplot as plt
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    Delta_0_GL, omega_tau, dt_transit, N_cells,
    J_C2, J_su2, J_u1, rho_B2_per_mode,
    E_B1, E_B2_mean, E_B3_mean, N_dof_BCS,
    xi_BCS, omega_PV
)

# ============================================================================
# SECTION 1: Input parameters
# ============================================================================

# Per-bond Josephson coupling from s60_rg_integrals.npz
# E_J_fold = 3.397 M_KK (pair-transfer amplitude between two cells)
data_s60 = np.load(os.path.join(os.path.dirname(__file__), 's60_rg_integrals.npz'), allow_pickle=True)
E_J_bond = float(data_s60['E_J_fold'])  # 3.397 M_KK per bond

# Transit time (the competitor)
t_transit = dt_transit  # 0.00113 M_KK^{-1} (S38)

# BCS gap
Delta = Delta_0_GL  # 0.770 M_KK

# Cell counts to sweep
N_array = np.array([2, 4, 8, 16, 32])

# Coordination number for N=32 (from S42 Voronoi tessellation)
z_mean_32 = 5.81  # mean coordination number  # (local)
N_bonds_32 = int(32 * z_mean_32 / 2)  # = 93 bonds

# Total Josephson energy for cross-reference
# From S55: E_J_total = N_bonds * E_J_per_bond_directional
# where E_J_per_bond_directional = 7.042 (directional stiffness sum)
# But s60 gives E_J_bond = 3.40 (pair transfer matrix element)
# These are DIFFERENT quantities: 7.042 is the phase stiffness, 3.40 is the tunneling amplitude
E_J_per_bond_stiffness = J_C2 * 4 + J_su2 * 3 + J_u1 * 1  # = 3.732 + 0.177 + 0.038 = 3.947
# Note: 7.042 from S55 used a different normalization. The s60 value 3.40 is the
# direct pair-transfer Hamiltonian matrix element. Use THIS for Thouless.

print("=" * 70)
print("GGE-THERM-61: Thouless Time Scaling for Josephson Fabric")
print("=" * 70)
print()
print(f"E_J (per-bond, s60):         {E_J_bond:.4f} M_KK")
print(f"E_J (phase stiffness sum):   {E_J_per_bond_stiffness:.4f} M_KK")
print(f"Delta_0_GL (BCS gap):        {Delta:.4f} M_KK")
print(f"E_J/Delta:                   {E_J_bond/Delta:.3f}")
print(f"t_transit:                   {t_transit:.6e} M_KK^{{-1}}")
print(f"1/t_transit (omega_transit): {1/t_transit:.2f} M_KK")
print(f"omega_tau (transit freq):    {omega_tau:.2f} M_KK")
print()

# ============================================================================
# SECTION 2: Thouless energy and time scaling
# ============================================================================

# Thouless energy: E_Th(N) = E_J / N^{2/3}
# This is the standard Anderson/Thouless scaling for diffusive transport:
#   D = E_J * a^2 (diffusion constant, a=1 in lattice units)
#   L = N^{1/3} * a (linear size of d=3 system)
#   E_Th = D / L^2 = E_J / N^{2/3}

# Also compute with alternative scaling:
# Ballistic: E_Th_bal = E_J / N^{1/3} (if coherent transport)
# 1D diffusive: E_Th_1d = E_J / N^2 (if effectively 1D chain)

E_Th_diffusive = E_J_bond / N_array**(2.0/3.0)
t_Th_diffusive = 1.0 / E_Th_diffusive

E_Th_ballistic = E_J_bond / N_array**(1.0/3.0)
t_Th_ballistic = 1.0 / E_Th_ballistic

E_Th_1d = E_J_bond / N_array**2.0
t_Th_1d = 1.0 / E_Th_1d

# Ratio to transit time
ratio_diff = t_Th_diffusive / t_transit
ratio_ball = t_Th_ballistic / t_transit
ratio_1d = t_Th_1d / t_transit

print("=" * 70)
print("THOULESS TIME SCALING (3 transport regimes)")
print("=" * 70)
print()
print(f"{'N':>4s} | {'E_Th(diff)':>10s} | {'t_Th(diff)':>12s} | {'t_Th/t_tr':>10s} | {'E_Th(ball)':>10s} | {'t_Th(ball)':>12s} | {'ball/t_tr':>10s}")
print("-" * 95)
for i, N in enumerate(N_array):
    print(f"{N:4d} | {E_Th_diffusive[i]:10.4f} | {t_Th_diffusive[i]:12.6e} | {ratio_diff[i]:10.2f} | "
          f"{E_Th_ballistic[i]:10.4f} | {t_Th_ballistic[i]:12.6e} | {ratio_ball[i]:10.2f}")
print()

print("1D diffusive (worst case):")
print(f"{'N':>4s} | {'E_Th(1D)':>10s} | {'t_Th(1D)':>12s} | {'1D/t_tr':>10s}")
print("-" * 50)
for i, N in enumerate(N_array):
    print(f"{N:4d} | {E_Th_1d[i]:10.6f} | {t_Th_1d[i]:12.6e} | {ratio_1d[i]:10.2f}")
print()

# ============================================================================
# SECTION 3: Fermi Golden Rule — quasiparticle scattering rate
# ============================================================================

# The Josephson coupling matrix element V_J connects states across cells.
# For the Fermi golden rule: Gamma = 2*pi * |V_J|^2 * rho(E)
#
# V_J = E_J_bond / N_modes_per_cell (distributed across modes)
# rho(E) from BCS DOS at the fold

# Single-cell Bogoliubov spectrum (from s60 data)
eps_fold = data_s60['eps_fold']  # 8 eigenvalues
V_fold = data_s60['V_fold']  # 8x8 interaction matrix

# DOS at Fermi level from BCS spectrum
# For discrete spectrum, rho(E) ~ 1/Delta_E where Delta_E is level spacing
# Mean level spacing
eps_sorted = np.sort(eps_fold)
level_spacings = np.diff(eps_sorted)
mean_spacing = np.mean(level_spacings)
rho_mean = 1.0 / mean_spacing  # mean DOS (states per M_KK)

# Also use rho_B2_per_mode from canonical_constants (from instanton action)
rho_B2 = rho_B2_per_mode  # 14.02 states/M_KK per mode

# Matrix element: V_J is the inter-cell coupling per mode pair
# From s60: g_eff = 0.276 is the effective coupling (SVD leading singular value)
g_eff = float(data_s60['g_eff'])

# Fermi golden rule rate (per quasiparticle)
# Using g_eff as the matrix element and rho_mean as the DOS
Gamma_FGR_mean = 2 * np.pi * g_eff**2 * rho_mean
t_FGR_mean = 1.0 / Gamma_FGR_mean

# Using full E_J_bond and rho_B2
Gamma_FGR_B2 = 2 * np.pi * (E_J_bond / N_dof_BCS)**2 * rho_B2
t_FGR_B2 = 1.0 / Gamma_FGR_B2

# Also compute the TOTAL scattering rate from all mode pairs
# This is the inclusive rate: sum over all final states
# Gamma_total = N_modes * Gamma_per_mode
Gamma_total = N_dof_BCS * Gamma_FGR_B2
t_total = 1.0 / Gamma_total

print("=" * 70)
print("FERMI GOLDEN RULE — Quasiparticle Scattering")
print("=" * 70)
print()
print(f"Bogoliubov spectrum at fold: {eps_fold}")
print(f"Level spacings: {level_spacings}")
print(f"Mean level spacing: {mean_spacing:.4f} M_KK")
print(f"Mean DOS (1/spacing): {rho_mean:.4f} states/M_KK")
print(f"B2 DOS (canonical): {rho_B2:.4f} states/M_KK per mode")
print(f"g_eff (SVD, s60): {g_eff:.4f} M_KK")
print(f"E_J_bond / N_modes: {E_J_bond/N_dof_BCS:.4f} M_KK")
print()
print(f"Gamma_FGR (g_eff, mean DOS): {Gamma_FGR_mean:.4f} M_KK")
print(f"  t_FGR = {t_FGR_mean:.6e} M_KK^{{-1}}")
print(f"  t_FGR / t_transit = {t_FGR_mean/t_transit:.4f}")
print()
print(f"Gamma_FGR (E_J/N, B2 DOS): {Gamma_FGR_B2:.4f} M_KK")
print(f"  t_FGR = {t_FGR_B2:.6e} M_KK^{{-1}}")
print(f"  t_FGR / t_transit = {t_FGR_B2/t_transit:.4f}")
print()
print(f"Gamma_total (inclusive, x{N_dof_BCS}): {Gamma_total:.4f} M_KK")
print(f"  t_total = {t_total:.6e} M_KK^{{-1}}")
print(f"  t_total / t_transit = {t_total/t_transit:.4f}")
print()

# ============================================================================
# SECTION 4: 3He-B Comparison
# ============================================================================

# In 3He-B:
# - Leggett frequency omega_L plays role of E_J (couples spin-orbit sectors)
# - omega_L / Delta ~ 0.01 in 3He-B (weak coupling, slow thermalization)
# - In framework: E_J/Delta = 3.40/0.77 = 4.4 (STRONG coupling, fast thermalization)
# - This is a key difference: framework is in the STRONG Josephson limit
#
# 3He-B Thouless analogy:
# - D_spin ~ (omega_L)^2 * tau_qp (spin diffusion constant)
# - tau_qp ~ 1/(Delta^2 * T) (quasiparticle lifetime at T << Delta)
# - In framework: D ~ E_J * a^2, no temperature dependence (GGE is non-thermal)

ratio_EJ_Delta = E_J_bond / Delta

# Josephson plasma frequency (analogous to Leggett frequency)
# omega_J = sqrt(E_J * E_C) where E_C = charging energy
# For the framework: E_C ~ 1/(2*N_pair) = 0.5 for N_pair = 1
E_C = 0.5  # charging energy for single pair  # (local)
omega_J_plasma = np.sqrt(E_J_bond * E_C)
t_J_plasma = 2 * np.pi / omega_J_plasma

print("=" * 70)
print("3He-B COMPARISON")
print("=" * 70)
print()
print(f"E_J / Delta = {ratio_EJ_Delta:.3f}  (>> 1 is strong Josephson limit)")
print(f"  3He-B: omega_L/Delta ~ 0.01 (WEAK)")
print(f"  Framework: E_J/Delta = {ratio_EJ_Delta:.1f} (STRONG)")
print()
print(f"Josephson plasma frequency: omega_J = sqrt(E_J * E_C) = {omega_J_plasma:.4f} M_KK")
print(f"Josephson plasma period: T_J = 2*pi/omega_J = {t_J_plasma:.4f} M_KK^{{-1}}")
print(f"T_J / t_transit = {t_J_plasma/t_transit:.2f}")
print()
print(f"omega_PV (pair vibration): {omega_PV:.4f} M_KK")
print(f"E_J / omega_PV = {E_J_bond/omega_PV:.3f} (Josephson vs internal dynamics)")
print()

# ============================================================================
# SECTION 5: Heisenberg time (ergodic limit)
# ============================================================================

# Heisenberg time: t_H = 2*pi / Delta_E (mean level spacing)
# This is the time for the system to resolve individual energy levels
# If t_Th < t_H, the system is in the "ergodic" regime (Thouless criterion)

# For N cells, the many-body Hilbert space dimension grows as dim^N
# (dim = 256 for 8 modes with occupation 0/1, but constrained to N_pair=1)
# The many-body level spacing decreases EXPONENTIALLY with N

# Single-cell dimension (N_pair=1, 8 modes): C(8,1)*2 = 16 (particle-hole pairs)
# But from s60: dim=120 for 2 cells, so single cell effective dim ~ sqrt(120) ~ 11
dim_1cell = 8  # number of single-particle levels
dim_N = np.array([dim_1cell**N for N in N_array])  # many-body dimension

# Bandwidth ~ E_J * z_mean * N (total energy scale)
# But for GGE: bandwidth = max(eps) - min(eps) ~ 1.17 M_KK (single cell)
bandwidth_1cell = eps_sorted[-1] - eps_sorted[0]
bandwidth_N = bandwidth_1cell + E_J_bond * z_mean_32 * np.sqrt(N_array)  # rough estimate

# Many-body level spacing
delta_E_N = bandwidth_N / dim_N.astype(float)

# Heisenberg time
t_H_N = 2 * np.pi / delta_E_N

print("=" * 70)
print("HEISENBERG TIME (ergodic limit)")
print("=" * 70)
print()
print(f"Single-cell bandwidth: {bandwidth_1cell:.4f} M_KK")
print(f"{'N':>4s} | {'dim(N)':>12s} | {'BW(N)':>10s} | {'delta_E':>12s} | {'t_H':>12s} | {'t_H/t_tr':>12s}")
print("-" * 75)
for i, N in enumerate(N_array):
    print(f"{N:4d} | {dim_N[i]:12.2e} | {bandwidth_N[i]:10.3f} | {delta_E_N[i]:12.4e} | {t_H_N[i]:12.4e} | {t_H_N[i]/t_transit:12.4e}")
print()

# ============================================================================
# SECTION 6: Gate verdict
# ============================================================================

# The gate uses diffusive scaling (conservative: slowest thermalization)
t_Th_32_diff = t_Th_diffusive[-1]  # N=32
ratio_32 = t_Th_32_diff / t_transit

print("=" * 70)
print("GATE VERDICT: GGE-THERM-61")
print("=" * 70)
print()
print(f"t_Th(N=32, diffusive) = {t_Th_32_diff:.6e} M_KK^{{-1}}")
print(f"t_transit             = {t_transit:.6e} M_KK^{{-1}}")
print(f"t_Th / t_transit      = {ratio_32:.4f}")
print()

if ratio_32 > 10:
    verdict = "PASS"
    detail = f"t_Th/t_transit = {ratio_32:.2f} > 10. GGE survives Thouless diffusion."
elif ratio_32 < 0.1:
    verdict = "FAIL"
    detail = f"t_Th/t_transit = {ratio_32:.4f} < 0.1. GGE thermalizes before transit completes."
else:
    verdict = "INFO"
    detail = f"t_Th/t_transit = {ratio_32:.4f} in [0.1, 10]. Race condition: thermalization and transit on comparable timescales."

print(f"VERDICT: {verdict}")
print(f"DETAIL: {detail}")
print()

# Cross-check: does FGR agree?
print("CROSS-CHECKS:")
print(f"  FGR (g_eff): t_FGR/t_transit = {t_FGR_mean/t_transit:.4f}")
print(f"  FGR (E_J/N): t_FGR/t_transit = {t_FGR_B2/t_transit:.4f}")
print(f"  Plasma period: T_J/t_transit = {t_J_plasma/t_transit:.2f}")
print(f"  Ballistic: t_Th(32,ball)/t_transit = {ratio_ball[-1]:.4f}")
print(f"  1D diffusive: t_Th(32,1d)/t_transit = {ratio_1d[-1]:.2f}")
print()

# ============================================================================
# SECTION 7: 3He-B Leggett frequency analog assessment
# ============================================================================

# The KEY 3He-B insight: in the B-phase, the Leggett frequency omega_L << Delta.
# This means spin-orbit relaxation is SLOW compared to gap dynamics.
# The GGE in 3He-B (if it were created) would persist because:
#   t_therm(spin-orbit) >> t_gap_dynamics
#
# In the framework:
#   E_J / Delta = 4.4 (STRONG coupling)
#   E_J / omega_PV = 4.3 (Josephson ~ pair vibration)
#
# This is NOT the 3He-B regime. It is closer to 3He-A where
# the orbital dynamics are fast and couple strongly to the gap.
# But the system is 3He-B CLASS (fully gapped, time-reversal).
#
# The resolution: E_J couples DIFFERENT cells, not different internal sectors.
# So even though E_J >> Delta, the Thouless time is set by DIFFUSION
# across the fabric, not by local relaxation. At N=32, the diffusion
# distance N^{1/3} ~ 3.2 lattice spacings provides the slowdown.

print("=" * 70)
print("3He-B ANALOG ASSESSMENT")
print("=" * 70)
print()
print(f"  E_J/Delta = {ratio_EJ_Delta:.1f} places the system in the STRONG Josephson limit.")
print(f"  In 3He-B: omega_L/Delta ~ 0.01 (WEAK) => slow spin-orbit relaxation.")
print(f"  Framework is NOT in the 3He-B weak-coupling regime for Josephson.")
print()
print(f"  However: Thouless scaling provides a GEOMETRIC slowdown.")
print(f"  At N=32: t_Th = N^{{2/3}} / E_J = {32**(2./3.):.2f} / {E_J_bond:.2f} = {t_Th_32_diff:.4e}")
print(f"  The factor N^{{2/3}} = {32**(2./3.):.2f} partially compensates E_J >> Delta.")
print()
print(f"  BOTTOM LINE: Strong coupling SHOULD thermalize fast (my 3He-B expectation).")
print(f"  But the ratio {ratio_32:.4f} says the transit is FASTER than thermalization.")
print(f"  Resolution: t_transit = {t_transit:.4e} is EXTREMELY short (1/omega_tau).")
print(f"  Even strong coupling cannot thermalize in {t_transit:.4e} M_KK^{{-1}}.")
print()

# ============================================================================
# SECTION 8: Save data
# ============================================================================

save_path = os.path.join(os.path.dirname(__file__), 's61_gge_therm.npz')
np.savez(save_path,
    # Input
    E_J_bond=E_J_bond,
    Delta=Delta,
    t_transit=t_transit,
    omega_tau=omega_tau,
    N_array=N_array,
    N_cells=N_cells,
    z_mean=z_mean_32,
    N_bonds=N_bonds_32,
    eps_fold=eps_fold,
    g_eff=g_eff,
    E_J_per_bond_stiffness=E_J_per_bond_stiffness,
    # Thouless scaling (3 regimes)
    E_Th_diffusive=E_Th_diffusive,
    t_Th_diffusive=t_Th_diffusive,
    E_Th_ballistic=E_Th_ballistic,
    t_Th_ballistic=t_Th_ballistic,
    E_Th_1d=E_Th_1d,
    t_Th_1d=t_Th_1d,
    ratio_diff=ratio_diff,
    ratio_ball=ratio_ball,
    ratio_1d=ratio_1d,
    # FGR
    rho_mean=rho_mean,
    rho_B2=rho_B2,
    Gamma_FGR_mean=Gamma_FGR_mean,
    Gamma_FGR_B2=Gamma_FGR_B2,
    Gamma_total=Gamma_total,
    t_FGR_mean=t_FGR_mean,
    t_FGR_B2=t_FGR_B2,
    t_total=t_total,
    # 3He comparison
    ratio_EJ_Delta=ratio_EJ_Delta,
    omega_J_plasma=omega_J_plasma,
    t_J_plasma=t_J_plasma,
    E_C=E_C,
    # Heisenberg
    dim_N=dim_N,
    bandwidth_N=bandwidth_N,
    delta_E_N=delta_E_N,
    t_H_N=t_H_N,
    # Gate
    gate_name=np.array(['GGE-THERM-61']),
    gate_verdict=np.array([verdict]),
    gate_detail=np.array([detail]),
    t_Th_32=t_Th_32_diff,
    ratio_32=ratio_32,
)
print(f"Data saved to: {save_path}")
print()

# ============================================================================
# SECTION 9: Plot
# ============================================================================

fig, axes = plt.subplots(1, 3, figsize=(16, 5))

# Panel 1: t_Th(N) for all three regimes
ax1 = axes[0]
ax1.loglog(N_array, t_Th_diffusive, 'bo-', linewidth=2, markersize=8, label=r'Diffusive ($N^{2/3}/E_J$)')
ax1.loglog(N_array, t_Th_ballistic, 'gs--', linewidth=1.5, markersize=6, label=r'Ballistic ($N^{1/3}/E_J$)')
ax1.loglog(N_array, t_Th_1d, 'r^:', linewidth=1.5, markersize=6, label=r'1D diffusive ($N^2/E_J$)')
ax1.axhline(y=t_transit, color='k', linewidth=2, linestyle='-', label=f'$t_{{transit}}$ = {t_transit:.2e}')
ax1.axhline(y=10*t_transit, color='k', linewidth=1, linestyle='--', alpha=0.5, label=r'$10 \times t_{transit}$ (PASS)')
ax1.axhline(y=0.1*t_transit, color='k', linewidth=1, linestyle=':', alpha=0.5, label=r'$0.1 \times t_{transit}$ (FAIL)')
ax1.fill_between([1.5, 40], 0.1*t_transit, 10*t_transit, alpha=0.1, color='yellow', label='INFO zone')
ax1.set_xlabel('N (cells)', fontsize=12)
ax1.set_ylabel(r'$t_{Th}$ ($M_{KK}^{-1}$)', fontsize=12)
ax1.set_title('Thouless Time vs. N', fontsize=13)
ax1.legend(fontsize=7, loc='upper left')
ax1.set_xlim(1.5, 40)
ax1.grid(True, alpha=0.3)

# Panel 2: Ratio t_Th / t_transit
ax2 = axes[1]
ax2.semilogy(N_array, ratio_diff, 'bo-', linewidth=2, markersize=8, label='Diffusive')
ax2.semilogy(N_array, ratio_ball, 'gs--', linewidth=1.5, markersize=6, label='Ballistic')
ax2.semilogy(N_array, ratio_1d, 'r^:', linewidth=1.5, markersize=6, label='1D diffusive')
ax2.axhline(y=10, color='green', linewidth=2, linestyle='--', label='PASS threshold (10)')
ax2.axhline(y=0.1, color='red', linewidth=2, linestyle='--', label='FAIL threshold (0.1)')
ax2.axhline(y=1, color='gray', linewidth=1, linestyle='-', alpha=0.5)
ax2.fill_between([1.5, 40], 0.1, 10, alpha=0.1, color='yellow')
ax2.set_xlabel('N (cells)', fontsize=12)
ax2.set_ylabel(r'$t_{Th} / t_{transit}$', fontsize=12)
ax2.set_title('Thermalization Race', fontsize=13)
ax2.legend(fontsize=8)
ax2.set_xlim(1.5, 40)
ax2.grid(True, alpha=0.3)

# Panel 3: Energy scales comparison
ax3 = axes[2]
energies = [Delta, E_J_bond, E_J_per_bond_stiffness, 1/t_transit, omega_J_plasma, omega_PV]
labels = [r'$\Delta_{BCS}$', r'$E_J$ (bond)', r'$E_J$ (stiffness)', r'$1/t_{tr}$', r'$\omega_J$', r'$\omega_{PV}$']
colors = ['blue', 'red', 'orange', 'black', 'purple', 'green']
y_pos = np.arange(len(energies))
ax3.barh(y_pos, energies, color=colors, alpha=0.7)
ax3.set_yticks(y_pos)
ax3.set_yticklabels(labels, fontsize=10)
ax3.set_xlabel('Energy (M_KK)', fontsize=12)
ax3.set_title('Energy Scale Hierarchy', fontsize=13)
ax3.set_xscale('log')
for i, v in enumerate(energies):
    ax3.text(v * 1.1, i, f'{v:.2f}', va='center', fontsize=9)
ax3.grid(True, alpha=0.3, axis='x')

plt.tight_layout()
plot_path = os.path.join(os.path.dirname(__file__), 's61_gge_therm.png')
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
print(f"Plot saved to: {plot_path}")
plt.close()

print()
print("COMPUTATION COMPLETE.")
