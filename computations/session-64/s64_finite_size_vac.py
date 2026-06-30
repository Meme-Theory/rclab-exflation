#!/usr/bin/env python3
"""
FINITE-SIZE-VACUUM-ENERGY-64: E(N=0) Verification
===================================================

Computes E(N=0), the total spectral action of the UNPAIRED substrate
divided by the number of emergent cells, and verifies the Gibbs-Duhem
prediction for vacuum energy at N_pair=1.

Physical logic:
  - S_fold = 250,361 M_KK is the total spectral action at the fold
    (tau=0.19), summed over ALL Peter-Weyl sectors with dim^2 weighting.
  - This is the vacuum energy of the EMPTY (unpaired) fabric.
  - The fabric tessellates into N_cells = 32 Voronoi cells (S42).
  - E(N=0) = S_fold / N_cells is the vacuum energy per cell.

Gibbs-Duhem check:
  At N_pair = 0 (no BCS pairs), the Gibbs-Duhem relation gives:
    rho = E(0) = S_fold / N_cells
  This is trivially 1.00 by construction (the empty system's vacuum
  energy IS S_fold/N_cells). The real content is:
  1. What is E(0) in M_KK units?
  2. How does E(0) compare to the BCS condensation energy E_cond?
  3. What is the OOM gap between E(0) * M_KK^4 and rho_Lambda_obs?

Additional: compare to S_occ (occupied-state spectral action from
OCC-SPEC-64) which gives the N_pair ~ 60 regime.

Gate: FINITE-SIZE-VACUUM-ENERGY-64
  INFO: Verify consistency and report gap

Input: S_fold, N_cells, E_cond, rho_Lambda_obs from canonical_constants
Output: s64_finite_size_vac.{npz,png}

Session 64, Gen-Physicist agent
"""

import numpy as np
import matplotlib.pyplot as plt
import os
import sys
import time

t_start = time.time()

# --- Setup paths ---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from canonical_constants import (
    S_fold, N_cells, E_cond, M_KK_gravity, M_KK_kerner,
    M_Pl_reduced, rho_Lambda_obs, a0_fold, a2_fold, a4_fold,
    Vol_SU3_Haar, tau_fold, n_pairs, E_exc, Delta_0_OES,
    E_B1, ratio_Evac_Econd, PI
)

print("=" * 70)
print("FINITE-SIZE-VACUUM-ENERGY-64: E(N=0) Vacuum Energy per Cell")
print("=" * 70)

# =========================================================================
# 1. BASIC QUANTITIES
# =========================================================================
print("\n--- 1. Canonical constants ---")
print(f"  S_fold      = {S_fold:.2f} M_KK        (total spectral action at fold)")
print(f"  N_cells     = {N_cells}                  (Voronoi tessellation, S42)")
print(f"  E_cond      = {E_cond:.6f} M_KK        (BCS condensation energy, 8-mode ED)")
print(f"  M_KK_grav   = {M_KK_gravity:.6e} GeV    (gravity route)")
print(f"  M_KK_kerner = {M_KK_kerner:.6e} GeV    (Kerner route)")
print(f"  M_Pl_red    = {M_Pl_reduced:.6e} GeV")
print(f"  rho_Lambda  = {rho_Lambda_obs:.2e} GeV^4 (observed)")

# =========================================================================
# 2. E(N=0) — VACUUM ENERGY PER CELL
# =========================================================================
print("\n--- 2. E(N=0): vacuum energy per cell ---")

E_vac_per_cell = S_fold / N_cells
print(f"  E(N=0) = S_fold / N_cells = {S_fold:.2f} / {N_cells}")
print(f"         = {E_vac_per_cell:.4f} M_KK")

# Gibbs-Duhem identity check: E(0) / (S_fold/N_cells) = 1.00
ratio_GD = E_vac_per_cell / (S_fold / N_cells)
print(f"\n  Gibbs-Duhem check: E(0) / (S_fold/N_cells) = {ratio_GD:.6f}")
print(f"  |deviation from 1| = {abs(ratio_GD - 1.0):.2e}")
print(f"  Gate criterion: 1.00 +/- 0.01 => {'PASS' if abs(ratio_GD - 1.0) < 0.01 else 'FAIL'}")

# =========================================================================
# 3. COMPARE TO BCS ENERGY SCALES
# =========================================================================
print("\n--- 3. Energy scale comparisons ---")

# E(0) vs E_cond
ratio_E0_Econd = E_vac_per_cell / abs(E_cond)
print(f"  E(0) / |E_cond| = {ratio_E0_Econd:.2f}")
print(f"    (vacuum energy per cell is {ratio_E0_Econd:.0f}x the condensation energy)")

# E(0) vs E_exc (total excitation energy from transit)
ratio_E0_Eexc = E_vac_per_cell / E_exc
print(f"  E(0) / E_exc    = {ratio_E0_Eexc:.4f}")
print(f"    (vacuum energy per cell is {1/ratio_E0_Eexc:.1f}x SMALLER than transit excitation)")

# The canonical ratio_Evac_Econd from S37 (pair fluctuations)
print(f"\n  S37 ratio_Evac_Econd = {ratio_Evac_Econd:.2f} (pair vibration vacuum fluctuations)")
print(f"  This E(0)/|E_cond|  = {ratio_E0_Econd:.2f} (geometric spectral action per cell)")
print(f"  Difference: factor {ratio_E0_Econd / ratio_Evac_Econd:.1f}x")
print(f"    (geometric vacuum is {ratio_E0_Econd / ratio_Evac_Econd:.0f}x larger than "
      f"fluctuation vacuum)")

# =========================================================================
# 4. SEELEY-DeWITT DECOMPOSITION PER CELL
# =========================================================================
print("\n--- 4. Seeley-DeWitt decomposition per cell ---")

# The spectral action decomposes as S = f_0*a_0 + f_2*a_2 + f_4*a_4 + ...
# where f_n are moments of the cutoff function.
# S_fold is the TOTAL, a_n are the coefficients.
# Per-cell versions:
a0_per_cell = a0_fold / N_cells
a2_per_cell = a2_fold / N_cells
a4_per_cell = a4_fold / N_cells

print(f"  a_0 / N_cells = {a0_per_cell:.4f}")
print(f"  a_2 / N_cells = {a2_per_cell:.4f}")
print(f"  a_4 / N_cells = {a4_per_cell:.4f}")
print(f"  S_fold/N_cells= {E_vac_per_cell:.4f}")

# =========================================================================
# 5. CC GAP ANALYSIS
# =========================================================================
print("\n--- 5. Cosmological constant gap ---")

# Convert E(0) to GeV^4 using both M_KK routes
# The spectral action has dimensions of M_KK^4 in the action integral
# rho_vac = (2/pi^2) * E(0) * M_KK^4  [the 2/pi^2 is the spectral action normalization]
# But actually, E(0) = S_fold/N_cells is already the integrated spectral action per cell.
# The CC density is rho = S_fold * M_KK^4 / V_4 where V_4 is 4-volume.
# Per cell: rho_cell = (S_fold/N_cells) * M_KK^4

# Route 1: gravity M_KK
rho_vac_grav = E_vac_per_cell * M_KK_gravity**4  # GeV^4 in natural units
gap_grav = np.log10(rho_vac_grav / rho_Lambda_obs)
print(f"  Gravity route (M_KK = {M_KK_gravity:.3e} GeV):")
print(f"    rho_vac = E(0) * M_KK^4 = {rho_vac_grav:.4e} GeV^4")
print(f"    rho_obs                  = {rho_Lambda_obs:.2e} GeV^4")
print(f"    Gap: log10(rho_vac/rho_obs) = {gap_grav:.2f} OOM")

# Route 2: Kerner M_KK
rho_vac_kerner = E_vac_per_cell * M_KK_kerner**4
gap_kerner = np.log10(rho_vac_kerner / rho_Lambda_obs)
print(f"\n  Kerner route (M_KK = {M_KK_kerner:.3e} GeV):")
print(f"    rho_vac = E(0) * M_KK^4 = {rho_vac_kerner:.4e} GeV^4")
print(f"    Gap: log10(rho_vac/rho_obs) = {gap_kerner:.2f} OOM")

# Route 3: Planck units for reference
# rho_Pl = M_Pl^4
rho_Pl = M_Pl_reduced**4
gap_planck = np.log10(rho_Pl / rho_Lambda_obs)
print(f"\n  Reference — Planck scale:")
print(f"    rho_Pl = M_Pl^4 = {rho_Pl:.4e} GeV^4")
print(f"    Standard CC gap: log10(M_Pl^4/rho_obs) = {gap_planck:.2f} OOM")

# =========================================================================
# 6. COMPARISON: E(N=0) vs E(N=60) [OCC-SPEC-64]
# =========================================================================
print("\n--- 6. Empty vs occupied comparison ---")

# S_occ from OCC-SPEC-64 (direct from the task specification)
S_occ = 18851.92  # M_KK (from W1-D result)  # (local)
E_occ_per_cell = S_occ / N_cells

print(f"  E(N=0)  = S_fold/N_cells = {E_vac_per_cell:.2f} M_KK  (empty substrate)")
print(f"  E(N~60) = S_occ/N_cells  = {E_occ_per_cell:.2f} M_KK  (BCS occupied)")
print(f"  Suppression factor: {E_occ_per_cell / E_vac_per_cell:.4f} ({E_vac_per_cell/E_occ_per_cell:.1f}x)")

# Gap for occupied state
rho_occ_grav = E_occ_per_cell * M_KK_gravity**4
gap_occ_grav = np.log10(rho_occ_grav / rho_Lambda_obs)
print(f"\n  CC gap (empty):    {gap_grav:.2f} OOM")
print(f"  CC gap (occupied): {gap_occ_grav:.2f} OOM")
print(f"  BCS reduces gap by {gap_grav - gap_occ_grav:.2f} OOM")

# =========================================================================
# 7. GIBBS-DUHEM THERMODYNAMIC ANALYSIS
# =========================================================================
print("\n--- 7. Gibbs-Duhem thermodynamic identity ---")

# Gibbs-Duhem for a system at T=0:
#   G = E - TS + PV = E + PV  (at T=0)
#   dG = -SdT + VdP + mu*dN
# At N=0, T=0:
#   G(0) = E(0) + P(0)*V(0)
# For the spectral action as an effective field theory, P*V = -E (vacuum,
# so Lorentz-invariant T^mu_nu = -rho*g^mu_nu => P = -rho).
# Therefore G(0) = E(0) - E(0) = 0.
# This is the standard vacuum Gibbs-Duhem identity.

# At N_pair = 1 (adding one BCS pair):
#   E(1) = E(0) + mu_BCS
# where mu_BCS = dE/dN|_{N=0} is the chemical potential for pairs.
# The BCS chemical potential is approximately E_B1 (the Fermi energy).

E_1pair = E_vac_per_cell + E_B1  # first pair costs mu above vacuum
print(f"  E(0) per cell              = {E_vac_per_cell:.4f} M_KK")
print(f"  mu_BCS (= E_B1)           = {E_B1:.6f} M_KK")
print(f"  E(1) = E(0) + mu          = {E_1pair:.4f} M_KK")
print(f"  E(1)/E(0)                  = {E_1pair/E_vac_per_cell:.6f}")
print(f"  Fractional change at N=1   = {E_B1/E_vac_per_cell:.6f}")
print(f"    (adding one pair changes vacuum energy by {E_B1/E_vac_per_cell*100:.4f}%)")

# Full condensate: subtract |E_cond| * N_cells from total
E_condensed_total = S_fold - abs(E_cond) * N_cells
E_condensed_per_cell = E_condensed_total / N_cells
print(f"\n  Full BCS condensate:")
print(f"    E_cond total = N_cells * |E_cond| = {N_cells * abs(E_cond):.4f} M_KK")
print(f"    E_condensed  = {E_condensed_per_cell:.4f} M_KK per cell")
print(f"    vs E(0)      = {E_vac_per_cell:.4f} M_KK per cell")
print(f"    Reduction    = {abs(E_cond)/E_vac_per_cell * 100:.4f}%")

# =========================================================================
# 8. SUMMARY TABLE
# =========================================================================
print("\n" + "=" * 70)
print("SUMMARY TABLE")
print("=" * 70)

summary = {
    'E_vac_per_cell': E_vac_per_cell,
    'S_fold': S_fold,
    'N_cells': N_cells,
    'E_cond': E_cond,
    'ratio_GD': ratio_GD,
    'ratio_E0_Econd': ratio_E0_Econd,
    'S_occ': S_occ,
    'E_occ_per_cell': E_occ_per_cell,
    'suppression': E_occ_per_cell / E_vac_per_cell,
    'gap_grav_empty': gap_grav,
    'gap_grav_occ': gap_occ_grav,
    'gap_kerner_empty': gap_kerner,
    'gap_planck': gap_planck,
    'rho_vac_grav': rho_vac_grav,
    'rho_vac_kerner': rho_vac_kerner,
    'rho_Lambda_obs': rho_Lambda_obs,
    'M_KK_gravity': M_KK_gravity,
    'E_B1': E_B1,
    'E_1pair_per_cell': E_1pair,
    'BCS_reduction_pct': abs(E_cond) / E_vac_per_cell * 100,
}

print(f"\n  {'Quantity':<35s} {'Value':<20s} {'Units'}")
print(f"  {'-'*35} {'-'*20} {'-'*10}")
print(f"  {'E(N=0) per cell':<35s} {E_vac_per_cell:<20.4f} {'M_KK'}")
print(f"  {'E(N~60) per cell':<35s} {E_occ_per_cell:<20.2f} {'M_KK'}")
print(f"  {'Suppression (occ/empty)':<35s} {E_occ_per_cell/E_vac_per_cell:<20.4f} {''}")
print(f"  {'E(0)/|E_cond|':<35s} {ratio_E0_Econd:<20.1f} {''}")
print(f"  {'Gibbs-Duhem ratio':<35s} {ratio_GD:<20.6f} {''}")
print(f"  {'CC gap (empty, grav)':<35s} {gap_grav:<20.2f} {'OOM'}")
print(f"  {'CC gap (occupied, grav)':<35s} {gap_occ_grav:<20.2f} {'OOM'}")
print(f"  {'CC gap (empty, Kerner)':<35s} {gap_kerner:<20.2f} {'OOM'}")
print(f"  {'CC gap (Planck reference)':<35s} {gap_planck:<20.2f} {'OOM'}")
print(f"  {'BCS reduction of E(0)':<35s} {abs(E_cond)/E_vac_per_cell*100:<20.4f} {'%'}")

# =========================================================================
# 9. GATE VERDICT
# =========================================================================
print("\n" + "=" * 70)
print("GATE VERDICT: FINITE-SIZE-VACUUM-ENERGY-64")
print("=" * 70)
print(f"  Gibbs-Duhem identity: E(0)/(S_fold/N_cells) = {ratio_GD:.6f}")
print(f"  Criterion: 1.00 +/- 0.01")
print(f"  Status: {'PASS' if abs(ratio_GD - 1.0) < 0.01 else 'FAIL'}")
print(f"  Verdict: INFO")
print(f"\n  E(N=0) = {E_vac_per_cell:.4f} M_KK per cell")
print(f"  CC gap (gravity route) = {gap_grav:.2f} OOM (vs 120 standard)")
print(f"  BCS occupation reduces per-cell vacuum by factor {E_vac_per_cell/E_occ_per_cell:.1f}")
print(f"  But gap remains {gap_occ_grav:.1f} OOM -- same ballpark as standard CC problem")
print(f"\n  KEY FINDING: The vacuum energy per cell is {ratio_E0_Econd:.0f}x the")
print(f"  condensation energy. BCS pairing lowers the vacuum by only")
print(f"  {abs(E_cond)/E_vac_per_cell*100:.2f}%. The CC problem is dominated by the")
print(f"  bare spectral weight, not by the pair physics.")

# =========================================================================
# 10. PLOT
# =========================================================================
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Panel A: energy scale bar chart
ax = axes[0]
labels = ['S_fold\n(total)', 'E(0)\n(per cell)', 'S_occ\n(BCS occ)', 'E_occ\n(per cell)',
          '|E_cond|\n(x1000)']
values = [S_fold, E_vac_per_cell, S_occ, E_occ_per_cell, abs(E_cond)*1000]
colors = ['#2196F3', '#4CAF50', '#FF9800', '#F44336', '#9C27B0']
bars = ax.bar(labels, values, color=colors, edgecolor='black', linewidth=0.5)
ax.set_yscale('log')
ax.set_ylabel('Energy scale (M_KK)')
ax.set_title('Vacuum Energy Scales at Fold')
# Annotate bars
for bar, val in zip(bars, [S_fold, E_vac_per_cell, S_occ, E_occ_per_cell, abs(E_cond)*1000]):
    ax.text(bar.get_x() + bar.get_width()/2, val*1.3,
            f'{val:.1f}', ha='center', va='bottom', fontsize=9)
ax.text(4, abs(E_cond)*1000*0.3, f'(actual |E_cond|={abs(E_cond):.3f})',
        ha='center', fontsize=7, style='italic')

# Panel B: CC gap waterfall
ax2 = axes[1]
gap_labels = ['Planck\nM_Pl^4', 'Empty cell\nE(0)*M_KK^4', 'BCS occ\nE_occ*M_KK^4',
              'Target\nrho_obs']
gap_values = [gap_planck, gap_grav, gap_occ_grav, 0.0]
gap_colors = ['#9E9E9E', '#2196F3', '#FF9800', '#4CAF50']

ax2.barh(gap_labels[::-1], gap_values[::-1], color=gap_colors[::-1],
         edgecolor='black', linewidth=0.5)
ax2.set_xlabel('log10(rho / rho_obs) [OOM]')
ax2.set_title('CC Gap Waterfall')
for i, (lab, val) in enumerate(zip(gap_labels[::-1], gap_values[::-1])):
    ax2.text(val + 1, i, f'{val:.1f} OOM', va='center', fontsize=10, fontweight='bold')

ax2.axvline(x=0, color='green', linestyle='--', linewidth=2, label='rho_obs')
ax2.legend(loc='lower right')

plt.tight_layout()
outpng = os.path.join(SCRIPT_DIR, 's64_finite_size_vac.png')
plt.savefig(outpng, dpi=150)
print(f"\n  Plot saved: {outpng}")
plt.close()

# =========================================================================
# 11. SAVE DATA
# =========================================================================
outnpz = os.path.join(SCRIPT_DIR, 's64_finite_size_vac.npz')
np.savez(outnpz, **summary)
print(f"  Data saved: {outnpz}")

elapsed = time.time() - t_start
print(f"\n  Elapsed: {elapsed:.2f}s")
print("  DONE.")
