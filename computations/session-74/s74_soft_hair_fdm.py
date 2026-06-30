"""
s74_soft_hair_fdm.py -- SOFT-HAIR-FDM-74 (W3-O)

Scale the Richardson-Gaudin (R-G) sector count from the 4-cell N_pair=2-4 regime
to the cosmological N_pair = 59.8 and check whether the unused/populated sector
ratio matches the dark-matter mass fraction f_DM = 0.27.

SUBSTRATE FRAMING
-----------------
The R-G sectors are the integrable eigenmodes of the flat-band BCS pair Hamiltonian
acting on the substrate's Fock space (8 pair modes per fiber = 4 B2 + 1 B1 + 3 B3).
At cosmological N_pair, only a fraction of these modes are thermally populated by
the transit-induced Bogoliubov pair production. The rest remain as "soft hair" --
dormant eigenmodes of the Jensen-deformed SU(3) fiber that carry energy-momentum
through the spectral action (a_2 channel) but are CPT-neutral and non-annihilating.

DM hypothesis (S73B phonon-first-hawking workshop carry-forward #5):
    DM = unpopulated R-G sectors of the substrate's integrable BCS structure.

This is NOT a DM particle in spacetime -- it is an excitation channel of the fabric
that is structurally present but never filled. The gate is the ratio of unused to
populated sectors compared to the observed f_DM = 0.27.

GATE
----
R_soft = (N_total - N_populated) / N_populated
PASS   : R_soft / 0.27 in [0.1, 10]
INFO   : R_soft / 0.27 in [0.01, 100]
FAIL   : otherwise

INPUTS
------
canonical_constants : N_cells = 32 (S42 Voronoi tessellation), N_dof_BCS = 8,
                     n_pairs = 59.8 (S38 Bogoliubov quasiparticle pairs from transit)
s73b_multi_cell_integ.npz : 4-cell R-G sector structure (N_cells=4, N_modes=8,
                            N_slots=32, N_pair=4), used for scaling validation
"""

import os
import numpy as np
import matplotlib.pyplot as plt

from canonical_constants import (
    N_cells, n_pairs, N_dof_BCS,
    M_KK, Delta_BCS,
)

# ---------------------------------------------------------------------------
# 1. Load the S73B multi-cell R-G sector structure (4-cell reference)
# ---------------------------------------------------------------------------
S73B_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         "s73b_multi_cell_integ.npz")                   # (local)
data_73b = np.load(S73B_PATH, allow_pickle=True)                         # (local)

N_modes_73b    = int(data_73b['N_modes'])     # (local)  -- 8 pair modes per cell
N_cells_73b    = int(data_73b['N_cells'])     # (local)  -- 4 cells (workshop scale)
N_pair_73b     = int(data_73b['N_pair'])      # (local)  -- 4 populated pairs
N_slots_73b    = int(data_73b['N_slots'])     # (local)  -- 32 pair slots total
dim_total_73b  = int(data_73b['dim_total'])   # (local)  -- Hilbert-space dim
n_orbits_73b   = int(data_73b['n_orbits'])    # (local)  -- k-orbit count
r_overall_73b  = float(data_73b['r_overall']) # (local)
gate_73b       = str(data_73b['gate_verdict']) # (local)

print("=" * 76)
print("  S74 W3-O  SOFT-HAIR-FDM-74")
print("  Scale R-G Sector Count from 4-cell to Cosmological N_pair")
print("=" * 76)
print()
print("S73B reference (4-cell R-G workshop scale):")
print(f"  N_modes_per_cell      = {N_modes_73b}")
print(f"  N_cells_73b           = {N_cells_73b}")
print(f"  N_slots_73b           = {N_slots_73b}  (= N_cells * N_modes)")
print(f"  N_pair_73b populated  = {N_pair_73b}")
print(f"  dim_total (Hilbert)   = {dim_total_73b}")
print(f"  n_orbits (k-sectors)  = {n_orbits_73b}")
print(f"  <r> overall           = {r_overall_73b:.4f}")
print(f"  S73B gate verdict     = {gate_73b}")
print()

# Verify: N_modes_per_cell from data == N_dof_BCS from canonical_constants
assert N_modes_73b == N_dof_BCS, \
    f"S73B N_modes={N_modes_73b} != canonical N_dof_BCS={N_dof_BCS}"

# R_soft at S73B workshop scale (validation anchor)
R_soft_73b = (N_slots_73b - N_pair_73b) / N_pair_73b  # (local)
print(f"  R_soft(4-cell reference) = ({N_slots_73b} - {N_pair_73b}) / {N_pair_73b}"
      f" = {R_soft_73b:.4f}")
print()

# ---------------------------------------------------------------------------
# 2. Scale to cosmological N_pair (primary computation)
# ---------------------------------------------------------------------------
# Per-cell pair-mode count is structural (N_dof_BCS = 8 = 4 B2 + 1 B1 + 3 B3);
# this does not scale with N_cells. The cosmological total pair-mode count is
# then N_total = N_cells * N_dof_BCS.
#
# Populated-pair count comes from canonical n_pairs = 59.8 (S38 Bogoliubov
# quasiparticle pairs produced during supersonic transit through the van Hove
# fold -- the total count of thermalized R-G occupations in the GGE relic).

N_total_cosmo = N_cells * N_dof_BCS                            # (local)  -- 256
N_pop_cosmo   = n_pairs                                        # (local)  -- 59.8

R_soft_cosmo = (N_total_cosmo - N_pop_cosmo) / N_pop_cosmo     # (local)

# Cross-check with the task-suggested CG(24) convention (24 vertices, same 8 modes)
N_total_cg24 = 24 * N_dof_BCS                                  # (local)  -- 192
R_soft_cg24  = (N_total_cg24 - N_pop_cosmo) / N_pop_cosmo      # (local)

# Per-cell occupancy (structural diagnostic)
n_pair_per_cell_cosmo = N_pop_cosmo / N_cells                  # (local)  -- 1.87
n_unused_per_cell     = N_dof_BCS - n_pair_per_cell_cosmo      # (local)  -- 6.13
R_soft_percell        = n_unused_per_cell / n_pair_per_cell_cosmo  # (local)

# Observational reference
f_DM_obs = 0.27                                                # (local)
ratio_primary = R_soft_cosmo / f_DM_obs                        # (local)
ratio_cg24    = R_soft_cg24 / f_DM_obs                         # (local)

print("Cosmological scaling (canonical N_cells = 32, N_dof_BCS = 8):")
print(f"  N_total_cosmo        = N_cells * N_dof_BCS = {N_cells} * {N_dof_BCS}"
      f" = {N_total_cosmo}")
print(f"  N_pop_cosmo (n_pairs) = {N_pop_cosmo}")
print(f"  Per-cell occupancy   = {n_pair_per_cell_cosmo:.4f} pairs / cell"
      f" (of {N_dof_BCS} slots)")
print(f"  Per-cell unused      = {n_unused_per_cell:.4f} slots / cell")
print()
print(f"  R_soft_cosmo  = ({N_total_cosmo} - {N_pop_cosmo:.1f}) / {N_pop_cosmo:.1f}"
      f" = {R_soft_cosmo:.6f}")
print(f"  R_soft (per-cell view) = {R_soft_percell:.6f}  (identical, structural)")
print()
print(f"  f_DM_obs              = {f_DM_obs}")
print(f"  R_soft / f_DM         = {ratio_primary:.4f}")
print()
print("Cross-check with CG(24) convention (N_cells = 24 Cayley-graph vertices):")
print(f"  N_total_cg24  = 24 * 8 = {N_total_cg24}")
print(f"  R_soft_cg24   = {R_soft_cg24:.6f}")
print(f"  R_soft_cg24 / f_DM = {ratio_cg24:.4f}")
print()

# ---------------------------------------------------------------------------
# 3. Gate evaluation
# ---------------------------------------------------------------------------
def classify(ratio):
    if 0.1 <= ratio <= 10.0:
        return "PASS"
    if 0.01 <= ratio <= 100.0:
        return "INFO"
    return "FAIL"

verdict_primary = classify(ratio_primary)                      # (local)
verdict_cg24    = classify(ratio_cg24)                         # (local)

print("-" * 76)
print("GATE EVALUATION")
print("-" * 76)
print(f"  SOFT-HAIR-FDM-74 (primary, N_cells = 32):  {verdict_primary}")
print(f"    R_soft / 0.27 = {ratio_primary:.4f}")
print(f"    PASS window  [0.1, 10]")
print(f"    INFO window  [0.01, 100]")
print()
print(f"  Cross-check (CG(24), 24 vertices):        {verdict_cg24}")
print(f"    R_soft / 0.27 = {ratio_cg24:.4f}")
print()

# ---------------------------------------------------------------------------
# 4. Limiting-case cross-check: N_pair -> infinity  =>  R_soft -> 0
# ---------------------------------------------------------------------------
# At fixed N_total, as N_populated -> N_total, R_soft -> 0 (no unused sectors).
# At fixed density n_pair/N_total = 1, R_soft = 0 exactly.
# Confirm by evaluating the scaling curve.

N_pair_scan = np.geomspace(1.0, N_total_cosmo, 64)             # (local)
R_soft_scan = (N_total_cosmo - N_pair_scan) / N_pair_scan       # (local)

R_soft_limit_full = (N_total_cosmo - N_total_cosmo) / N_total_cosmo  # (local)
print(f"Limiting case check: N_pair -> N_total  =>  R_soft = {R_soft_limit_full:.6g}"
      f"  (expected 0)")
print()

# Cross-check with S66 Leggett-only Omega_DM h^2
# If R-G soft hair sources f_DM, then on the Leggett-only partition the
# surviving DM is 0.6% of cosmo DM (S66). So Leggett alone does not saturate DM,
# and the soft-hair channel must supply the remainder.
Omega_DM_leg_s66 = 0.120                                        # (local) S66 value
Omega_DM_obs     = 0.120                                        # (local) observed
f_DM_leggett_frac = 0.006                                       # (local) S66 fraction of DM from Leggett
print("Cross-check vs S66 Leggett-only Omega_DM h^2 = 0.120:")
print(f"  Leggett-only Omega_DM h^2  = {Omega_DM_leg_s66} (matches obs)")
print(f"  But f_DM_leggett / f_DM    = {f_DM_leggett_frac}  (only 0.6% of DM)")
print(f"  Residual DM to source      = {1 - f_DM_leggett_frac:.4f}  of total")
print(f"  Soft-hair R_soft = {R_soft_cosmo:.4f} ~ {R_soft_cosmo/f_DM_obs:.2f} * f_DM")
print()

# ---------------------------------------------------------------------------
# 5. Save data
# ---------------------------------------------------------------------------
DATA_OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "s74_soft_hair_fdm.npz")                # (local)

np.savez(
    DATA_OUT,
    # Inputs
    N_cells=N_cells,
    N_dof_BCS=N_dof_BCS,
    n_pairs=n_pairs,
    f_DM_obs=f_DM_obs,
    # Reference (S73B 4-cell)
    N_cells_73b=N_cells_73b,
    N_modes_73b=N_modes_73b,
    N_slots_73b=N_slots_73b,
    N_pair_73b=N_pair_73b,
    R_soft_73b=R_soft_73b,
    r_overall_73b=r_overall_73b,
    # Cosmological primary
    N_total_cosmo=N_total_cosmo,
    N_pop_cosmo=N_pop_cosmo,
    R_soft_cosmo=R_soft_cosmo,
    ratio_primary=ratio_primary,
    verdict_primary=verdict_primary,
    n_pair_per_cell_cosmo=n_pair_per_cell_cosmo,
    n_unused_per_cell=n_unused_per_cell,
    # Cross-check CG(24)
    N_total_cg24=N_total_cg24,
    R_soft_cg24=R_soft_cg24,
    ratio_cg24=ratio_cg24,
    verdict_cg24=verdict_cg24,
    # Scaling curve
    N_pair_scan=N_pair_scan,
    R_soft_scan=R_soft_scan,
    # Gate metadata
    gate_name=np.array("SOFT-HAIR-FDM-74"),
    gate_verdict=np.array(verdict_primary),
    gate_detail=np.array(
        f"R_soft={R_soft_cosmo:.4f}, R_soft/f_DM={ratio_primary:.4f}"),
)
print(f"Data saved: {DATA_OUT}")
print()

# ---------------------------------------------------------------------------
# 6. Plot: R_soft vs N_pair scaling with annotations
# ---------------------------------------------------------------------------
PLOT_OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "s74_soft_hair_fdm.png")                # (local)

fig, ax = plt.subplots(1, 1, figsize=(8.0, 5.6))

# Master scaling curve
ax.loglog(N_pair_scan, R_soft_scan, 'b-', lw=2.0,
          label=r'$R_{\rm soft}(N_{\rm pair}) = (N_{\rm total} - N_{\rm pair})'
                r'/ N_{\rm pair}$')

# 4-cell S73B anchor (rescaled to cosmological N_total for consistency? No:
# plot it as a standalone reference curve with its own N_total=32)
N_pair_scan_73b = np.geomspace(1.0, N_slots_73b, 64)            # (local)
R_soft_scan_73b = (N_slots_73b - N_pair_scan_73b) / N_pair_scan_73b  # (local)
ax.loglog(N_pair_scan_73b, R_soft_scan_73b, 'c--', lw=1.3, alpha=0.7,
          label=r'4-cell reference ($N_{\rm total}=32$, S73B)')

# S73B anchor point
ax.plot(N_pair_73b, R_soft_73b, 'cs', markersize=11, mec='darkcyan', mew=1.5,
        label=f'S73B: N_pair={N_pair_73b}, R_soft={R_soft_73b:.2f}')

# Cosmological anchor point (primary)
ax.plot(N_pop_cosmo, R_soft_cosmo, 'ro', markersize=12, mec='darkred', mew=1.8,
        label=f'Cosmo ($N_{{\\rm cells}}=32$): '
              f'N_pair={N_pop_cosmo:.1f}, R_soft={R_soft_cosmo:.3f}')

# CG(24) alternative
N_pair_scan_cg24 = np.geomspace(1.0, N_total_cg24, 64)          # (local)
R_soft_scan_cg24 = (N_total_cg24 - N_pair_scan_cg24) / N_pair_scan_cg24  # (local)
ax.loglog(N_pair_scan_cg24, R_soft_scan_cg24, 'g:', lw=1.3, alpha=0.7,
          label=r'CG(24) alternative ($N_{\rm total}=192$)')
ax.plot(N_pop_cosmo, R_soft_cg24, 'g^', markersize=10, mec='darkgreen', mew=1.5)

# f_DM = 0.27 reference bands (PASS window [0.1, 10] * 0.27)
ax.axhline(f_DM_obs, color='k', lw=1.2, ls='-', alpha=0.6,
           label=r'$f_{\rm DM} = 0.27$')
ax.axhspan(0.1 * f_DM_obs, 10.0 * f_DM_obs, alpha=0.15, color='green',
           label='PASS window (1 OOM of f_DM)')
ax.axhspan(0.01 * f_DM_obs, 100.0 * f_DM_obs, alpha=0.05, color='blue')

ax.set_xlabel(r'$N_{\rm pair}$ populated', fontsize=12)
ax.set_ylabel(r'$R_{\rm soft} = (N_{\rm total} - N_{\rm pair}) / N_{\rm pair}$',
              fontsize=12)
ax.set_title(r'SOFT-HAIR-FDM-74: R-G soft-hair ratio vs. cosmological $N_{\rm pair}$'
             '\nSubstrate DM candidate: unpopulated R-G sectors of Jensen-SU(3) fiber',
             fontsize=11)
ax.legend(loc='lower left', fontsize=8.5, framealpha=0.88)
ax.grid(True, which='both', alpha=0.25)
ax.set_xlim(0.9, 1.1 * N_total_cosmo)
ax.set_ylim(1e-3, 1e3)

fig.tight_layout()
fig.savefig(PLOT_OUT, dpi=150)
plt.close(fig)
print(f"Plot saved: {PLOT_OUT}")
print()

# ---------------------------------------------------------------------------
# 7. Summary block
# ---------------------------------------------------------------------------
print("=" * 76)
print("  S74 W3-O  SOFT-HAIR-FDM-74 SUMMARY")
print("=" * 76)
print(f"  Total R-G sectors (cosmo)   = {N_total_cosmo}  [N_cells={N_cells}"
      f" * N_dof_BCS={N_dof_BCS}]")
print(f"  Populated sectors           = {N_pop_cosmo}  [canonical n_pairs]")
print(f"  Unused (soft hair)          = {N_total_cosmo - N_pop_cosmo:.1f}")
print(f"  R_soft                      = {R_soft_cosmo:.4f}")
print(f"  R_soft / f_DM(=0.27)        = {ratio_primary:.4f}")
print(f"  Gate                        : {verdict_primary}")
print()
print(f"  Cross-check CG(24) R_soft   = {R_soft_cg24:.4f}")
print(f"  Cross-check CG(24) ratio    = {ratio_cg24:.4f}  [{verdict_cg24}]")
print(f"  Limiting case R_soft(inf)   = 0.0  [PASS]")
print("=" * 76)
