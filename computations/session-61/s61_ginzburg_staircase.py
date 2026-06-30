#!/usr/bin/env python3
"""
s61_ginzburg_staircase.py -- Ginzburg Criterion for the CC Staircase
=====================================================================

Session 61, GINZBURG-CC-61 gate.

Physics
-------
The CC staircase is a mean-field construction: each cell has a BCS ground
state |Psi_N> with N condensed pairs, and the CC at step N is

    Lambda(N) = E_GS(N) - N * epsilon

where epsilon = dE_GS/dN is the chemical potential (step height).

Mean-field theory treats each cell as independent. Inter-cell Josephson
coupling introduces fluctuations in the pair number, which blur the steps.
The question is: are the steps sharp or washed out?

The Ginzburg criterion answers this by comparing the fluctuation amplitude
to the step height. Define:

    Gi = (delta_F / F_0)^2

where:
    F_0 = mean-field step height (chemical potential gap between steps)
    delta_F = inter-cell fluctuation in free energy from Josephson coupling

If Gi << 1: mean-field staircase is reliable, steps are sharp.
If Gi >> 1: fluctuations dominate, steps are washed out.

The inter-cell fluctuation is computed from the Josephson pair-transfer
amplitude:
    delta_F = E_J * |S_+(1)|^2 / N_modes

where:
    E_J = Josephson coupling energy (M_KK units)
    S_+(1) = pair-transfer spectral weight at DeltaN = 1
    N_modes = number of modes (normalization for per-mode fluctuation)

This is EXACTLY the standard Ginzburg construction: the correlation volume
is one cell (since J couples nearest cells), the fluctuation energy is
the Josephson tunnel splitting, and the mean-field scale is the step height.

For a d-dimensional lattice with z nearest neighbors, the full Ginzburg
criterion is:

    Gi = (z * E_J^2 * |S_+(1)|^2) / (N_modes * F_0^2)

but since we are comparing SINGLE-BOND fluctuation to the step, the
minimal (most conservative) estimate uses z = 1.

Additional analysis:
    - Ginzburg-corrected step height: F_corr = F_0 * sqrt(1 + Gi)
    - Fluctuation correlation length: xi_fluct = xi_BCS / Gi^{1/(2*(4-d))}
    - Thermal decoherence: for the GGE-temperature T_acoustic, also compute
      the thermal Ginzburg number Gi_T = (T_acoustic / F_0)^(d/2)

Pre-registered gate:
    PASS if Gi < 0.1
    FAIL if Gi > 10
    INFO if 0.1 <= Gi <= 10

Author: Landau Condensed-Matter Theorist (S61)
"""

import sys
import os
import numpy as np

# Add computations to path for canonical_constants
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import *

# =============================================================================
#  LOAD INPUT DATA
# =============================================================================

data_dir = os.path.dirname(os.path.abspath(__file__))

# Pair transfer data (S60)
pt = np.load(os.path.join(data_dir, 's60_pair_transfer_n4.npz'), allow_pickle=True)

# Staircase baseline (S60)
stair = np.load(os.path.join(data_dir, 's60_staircase_ext.npz'), allow_pickle=True)

# Compound staircase (S61 W1)
compound = np.load(os.path.join(data_dir, 's61_compound_staircase.npz'), allow_pickle=True)

# RG integrals (S60) -- integrability breaking
rg = np.load(os.path.join(data_dir, 's60_rg_integrals.npz'), allow_pickle=True)

# Fabric Landau params (S61)
fabric = np.load(os.path.join(data_dir, 's61_fabric_landau_params.npz'), allow_pickle=True)

print("=" * 72)
print("  GINZBURG CRITERION FOR THE CC STAIRCASE")
print("  Gate: GINZBURG-CC-61")
print("=" * 72)

# =============================================================================
#  SECTION 1: EXTRACT PHYSICAL QUANTITIES
# =============================================================================

# Josephson coupling energy
E_J_val = float(pt['E_J_fold'])  # = 3.397 M_KK
N_modes_val = int(pt['N_modes'])  # = 8

# Pair transfer spectral weights S_+(N)
# S_+(0) = single-particle transfer (N=0 -> N=1)
# S_+(1) = pair transfer from N=1 state (the relevant one for inter-step fluctuations)
S_plus_0 = float(pt['S_plus_N0'])  # = 0.500
S_plus_1 = float(pt['S_plus_N1'])  # = 0.936 (2-cell result)
S_plus_2 = float(pt['S_plus_N2'])  # = 1.307
S_plus_3 = float(pt['S_plus_N3'])  # = 1.615
S_plus_4 = float(pt['S_plus_N4'])  # = 1.861

# Mode-resolved pair transfer amplitudes P_+(N)
P_plus_N1 = pt['P_plus_N1']  # shape (8,), per-mode amplitudes

# Step heights
# Baseline: epsilon from S60 staircase
eps_baseline = float(stair['eps_canonical'])  # = 0.00374 M_KK (N=4 canonical)

# Compound corrected: from S61 W1
eps_corrected = float(compound['epsilon_corrected'])  # = 0.182 M_KK

# Also extract the full chemical potential sequence
mu_baseline = stair['mu_forward_A']  # mu(N) = E_GS(N) - E_GS(N-1)
mu_compound = compound['mu_compound']

# Integrability breaking parameter
delta_k_mean = float(rg['mean_delta_full'])  # = 0.328

# Effective coupling
g_eff_val = float(rg['g_eff'])  # = 0.276

# BCS coherence length and GL coherence length from canonical constants
xi_BCS_val = xi_BCS  # = 0.808 M_KK^{-1}

# GGE acoustic temperature
T_ac = T_acoustic  # = 0.112 M_KK

# Number of cells in the tessellation
N_cells_val = N_cells  # = 32

print("\n--- Physical inputs ---")
print(f"E_J           = {E_J_val:.4f} M_KK")
print(f"N_modes       = {N_modes_val}")
print(f"S_+(0)        = {S_plus_0:.6f}")
print(f"S_+(1)        = {S_plus_1:.6f}")
print(f"S_+(2)        = {S_plus_2:.6f}")
print(f"xi_BCS        = {xi_BCS_val:.4f} M_KK^{{-1}}")
print(f"T_acoustic    = {T_ac:.4f} M_KK")
print(f"delta_k (RG)  = {delta_k_mean:.4f}")
print(f"g_eff         = {g_eff_val:.4f}")
print(f"N_cells       = {N_cells_val}")

print(f"\n--- Step heights (F_0) ---")
print(f"eps_baseline  = {eps_baseline:.6f} M_KK  (S60 canonical)")
print(f"eps_corrected = {eps_corrected:.6f} M_KK  (S61 compound)")

# =============================================================================
#  SECTION 2: INTER-CELL FLUCTUATION delta_F
# =============================================================================
#
# The Josephson Hamiltonian between cells i, j is:
#     H_J = -E_J * sum_k P^+_{ik} P^-_{jk}
#
# where P^+_{ik} creates a pair in mode k of cell i.
#
# The fluctuation in the pair number per cell due to Josephson tunneling:
#     <(Delta N)^2>_J = sum_k |<N+1| P^+_k |N>|^2 * (E_J / Delta_E_k)^2
#
# In the standard BCS treatment, the pair-transfer spectral weight
#     S_+(N) = sum_k |<N+1| P^+_k |N>|^2
# is ALREADY the sum over all modes of the squared matrix elements.
#
# The free energy fluctuation from one Josephson bond:
#     delta_F_bond = E_J * S_+(1)^2 / S_+(1) = E_J * S_+(1)
#
# Wait -- let me be more precise. The second-order energy shift from
# Josephson coupling between cell 1 (in state |N>) and cell 2 (in |N>) is:
#
#     delta_E^(2) = -E_J^2 * sum_k |<N+1,N-1| P^+_{1k} P^-_{2k} |N,N>|^2
#                         / (E_{N+1} + E_{N-1} - 2*E_N)
#
# The numerator is E_J^2 * sum_k |P_k(N)|^2 * |P_k(N)|^2
# where P_k(N) = <N+1|P^+_k|N> are the per-mode amplitudes.
#
# But S_+(N) = sqrt(sum_k |P_k(N)|^2), so the numerator contains
# the FOURTH moment of the P_k distribution, not the second moment squared.
#
# For the denominator, the relevant excitation energy is the PAIR-ADDITION
# energy: E_{N+1} + E_{N-1} - 2*E_N = d^2 E_GS / dN^2 (pairing stiffness).
#
# More carefully:
# S_+(N) as given in the data is defined as:
#     S_+(N) = || P^+ |GS_N> ||  (norm of the pair-addition vector)
# So S_+(N)^2 = sum_k |<GS_{N+1}| P^+_k |GS_N>|^2 summed with overlaps.
#
# Actually from the data: S_plus_N0 = 0.5, S_plus_N1 = 0.936.
# These are total spectral weights (already squared and summed).
#
# The Josephson fluctuation energy for a single bond connecting two cells
# in the N-pair ground state is:
#
#     delta_F = E_J^2 * S_+(N)^2 / Delta_pair
#
# where Delta_pair = E_{N+1} + E_{N-1} - 2*E_N is the pair stiffness.
# This is standard second-order perturbation theory in E_J.

print("\n" + "=" * 72)
print("  SECTION 2: INTER-CELL FLUCTUATION")
print("=" * 72)

# Pair stiffness from the compound staircase
E_GS_compound = compound['E_GS_compound']  # E_GS(N) for N = 0, 1, 2, 3, 4
E_GS_baseline = stair['E_GS_A']

# d^2 E / dN^2 = E(N+1) + E(N-1) - 2*E(N)
# Compute at each available N
print("\n--- Pair stiffness d^2E/dN^2 (compound staircase) ---")
for N in range(1, len(E_GS_compound) - 1):
    stiff = E_GS_compound[N+1] + E_GS_compound[N-1] - 2 * E_GS_compound[N]
    print(f"  N={N}: Delta_pair = {stiff:.6f} M_KK")

print("\n--- Pair stiffness d^2E/dN^2 (baseline staircase) ---")
for N in range(1, len(E_GS_baseline) - 1):
    stiff = E_GS_baseline[N+1] + E_GS_baseline[N-1] - 2 * E_GS_baseline[N]
    print(f"  N={N}: Delta_pair = {stiff:.6f} M_KK")

# Use N=1 stiffness (the step most relevant for the CC)
Delta_pair_compound_N1 = (E_GS_compound[2] + E_GS_compound[0]
                          - 2 * E_GS_compound[1])
Delta_pair_baseline_N1 = (E_GS_baseline[2] + E_GS_baseline[0]
                          - 2 * E_GS_baseline[1])

print(f"\nDelta_pair (compound, N=1) = {Delta_pair_compound_N1:.6f} M_KK")
print(f"Delta_pair (baseline, N=1) = {Delta_pair_baseline_N1:.6f} M_KK")

# Josephson fluctuation (second-order perturbation theory):
#     delta_F = E_J^2 * S_+(1)^2 / Delta_pair
#
# BUT we must be careful: S_+(1)^2 is already the total spectral weight.
# The second-order shift uses the MATRIX ELEMENT squared, which is S_+(1)^2
# (since S_+(1) itself is the norm of P^+|GS_1>).
#
# No -- S_+(1) is defined as the NORM:
#     S_+(N) = || P^+ |GS_N> ||
# So S_+(1)^2 = sum_k |<k,N+1| P^+_k |GS_N>|^2
# This IS the sum of squared matrix elements.

# For a single Josephson bond:
delta_F_compound = E_J_val**2 * S_plus_1**2 / abs(Delta_pair_compound_N1)
delta_F_baseline = E_J_val**2 * S_plus_1**2 / abs(Delta_pair_baseline_N1)

print(f"\ndelta_F (compound) = E_J^2 * S_+(1)^2 / |Delta_pair|")
print(f"  = {E_J_val:.4f}^2 * {S_plus_1:.6f}^2 / {abs(Delta_pair_compound_N1):.6f}")
print(f"  = {delta_F_compound:.6f} M_KK")

print(f"\ndelta_F (baseline) = E_J^2 * S_+(1)^2 / |Delta_pair|")
print(f"  = {E_J_val:.4f}^2 * {S_plus_1:.6f}^2 / {abs(Delta_pair_baseline_N1):.6f}")
print(f"  = {delta_F_baseline:.6f} M_KK")

# =============================================================================
#  SECTION 3: GINZBURG NUMBER
# =============================================================================
#
# Gi = (delta_F / F_0)^2
# where F_0 is the step height.
#
# The step height F_0 is the chemical potential = first difference of E_GS.
# For the CC staircase, what matters is the FIRST step:
#     F_0 = |mu(1)| = |E_GS(1) - E_GS(0)|

print("\n" + "=" * 72)
print("  SECTION 3: GINZBURG NUMBER")
print("=" * 72)

# Step heights
F_0_compound = abs(eps_corrected)  # = 0.182 M_KK
F_0_baseline_canonical = abs(eps_baseline)  # = 0.00374 M_KK (staircase canonical)

# Also use the first chemical potential directly
F_0_baseline_mu1 = abs(mu_baseline[0])  # = 0.0464 M_KK
F_0_compound_mu1 = abs(mu_compound[0])  # = 0.182 M_KK

print(f"\n--- Step heights F_0 ---")
print(f"F_0 (compound, eps_corrected)   = {F_0_compound:.6f} M_KK")
print(f"F_0 (compound, mu_1)            = {F_0_compound_mu1:.6f} M_KK")
print(f"F_0 (baseline, eps_canonical)   = {F_0_baseline_canonical:.6f} M_KK")
print(f"F_0 (baseline, mu_1)            = {F_0_baseline_mu1:.6f} M_KK")

# Primary Ginzburg numbers
# Use the compound epsilon as the primary case (from task specification)
Gi_compound = (delta_F_compound / F_0_compound)**2
Gi_compound_mu1 = (delta_F_compound / F_0_compound_mu1)**2

# Baseline checks
Gi_baseline_canonical = (delta_F_baseline / F_0_baseline_canonical)**2
Gi_baseline_mu1 = (delta_F_baseline / F_0_baseline_mu1)**2

print(f"\n--- Ginzburg numbers ---")
print(f"Gi (compound, eps=0.182)  = ({delta_F_compound:.4f} / {F_0_compound:.4f})^2")
print(f"                          = {Gi_compound:.6e}")
print(f"Gi (compound, mu_1)       = ({delta_F_compound:.4f} / {F_0_compound_mu1:.4f})^2")
print(f"                          = {Gi_compound_mu1:.6e}")
print(f"Gi (baseline, eps=0.0037) = ({delta_F_baseline:.4f} / {F_0_baseline_canonical:.4f})^2")
print(f"                          = {Gi_baseline_canonical:.6e}")
print(f"Gi (baseline, mu_1=0.046) = ({delta_F_baseline:.4f} / {F_0_baseline_mu1:.4f})^2")
print(f"                          = {Gi_baseline_mu1:.6e}")

# =============================================================================
#  SECTION 4: ALTERNATIVE FLUCTUATION ESTIMATES
# =============================================================================
#
# Estimate 1 (above): Standard 2nd-order perturbation theory in E_J.
#
# Estimate 2: Direct E_J * amplitude (first-order, overestimates).
#     delta_F_direct = E_J * S_+(1) / sqrt(N_modes)
#
# Estimate 3: Per-mode estimate using the P_+(1) amplitudes directly.
#     delta_F_mode = E_J * sqrt(sum_k P_k^4) (fourth moment)
#
# Estimate 4: Thermal fluctuation from GGE temperature.
#     delta_F_thermal = T_acoustic * sqrt(N_modes)

print("\n" + "=" * 72)
print("  SECTION 4: ALTERNATIVE FLUCTUATION ESTIMATES")
print("=" * 72)

# Estimate 2: First-order (tunnel splitting)
delta_F_direct = E_J_val * S_plus_1 / np.sqrt(N_modes_val)
Gi_direct_compound = (delta_F_direct / F_0_compound)**2
Gi_direct_baseline = (delta_F_direct / F_0_baseline_mu1)**2

print(f"\nEstimate 2 (first-order tunnel splitting):")
print(f"  delta_F = E_J * S_+(1) / sqrt(N_modes)")
print(f"         = {E_J_val:.4f} * {S_plus_1:.4f} / {np.sqrt(N_modes_val):.4f}")
print(f"         = {delta_F_direct:.6f} M_KK")
print(f"  Gi (compound) = {Gi_direct_compound:.6e}")
print(f"  Gi (baseline) = {Gi_direct_baseline:.6e}")

# Estimate 3: Fourth-moment of P_+(1)
P_4th_moment = np.sqrt(np.sum(P_plus_N1**4))
delta_F_4th = E_J_val * P_4th_moment
Gi_4th_compound = (delta_F_4th / F_0_compound)**2
Gi_4th_baseline = (delta_F_4th / F_0_baseline_mu1)**2

print(f"\nEstimate 3 (fourth-moment of P_+(1)):")
print(f"  sqrt(sum P_k^4) = {P_4th_moment:.6f}")
print(f"  delta_F = E_J * sqrt(sum P_k^4)")
print(f"         = {E_J_val:.4f} * {P_4th_moment:.6f}")
print(f"         = {delta_F_4th:.6f} M_KK")
print(f"  Gi (compound) = {Gi_4th_compound:.6e}")
print(f"  Gi (baseline) = {Gi_4th_baseline:.6e}")

# Estimate 4: Thermal fluctuation
delta_F_thermal = T_ac * np.sqrt(N_modes_val)
Gi_thermal_compound = (delta_F_thermal / F_0_compound)**2
Gi_thermal_baseline = (delta_F_thermal / F_0_baseline_mu1)**2

print(f"\nEstimate 4 (GGE thermal fluctuation):")
print(f"  delta_F = T_acoustic * sqrt(N_modes)")
print(f"         = {T_ac:.4f} * {np.sqrt(N_modes_val):.4f}")
print(f"         = {delta_F_thermal:.6f} M_KK")
print(f"  Gi (compound) = {Gi_thermal_compound:.6e}")
print(f"  Gi (baseline) = {Gi_thermal_baseline:.6e}")

# =============================================================================
#  SECTION 5: NUMBER FLUCTUATION AND STEP RESOLUTION
# =============================================================================
#
# The pair number fluctuation induced by Josephson coupling:
#     <(Delta N)^2> = S_+(N)^2 * (E_J / Delta_pair)^2
#
# For the step to be resolved: <(Delta N)^2> << 1
# (otherwise the pair number is uncertain by more than one unit)

print("\n" + "=" * 72)
print("  SECTION 5: PAIR NUMBER FLUCTUATION")
print("=" * 72)

DN2_compound = S_plus_1**2 * (E_J_val / abs(Delta_pair_compound_N1))**2
DN2_baseline = S_plus_1**2 * (E_J_val / abs(Delta_pair_baseline_N1))**2

print(f"\n<(Delta N)^2> (compound) = S_+(1)^2 * (E_J/Delta_pair)^2")
print(f"  = {S_plus_1:.4f}^2 * ({E_J_val:.4f} / {abs(Delta_pair_compound_N1):.4f})^2")
print(f"  = {DN2_compound:.6f}")
print(f"  sqrt(<DN^2>) = {np.sqrt(DN2_compound):.6f}")

print(f"\n<(Delta N)^2> (baseline) = S_+(1)^2 * (E_J/Delta_pair)^2")
print(f"  = {S_plus_1:.4f}^2 * ({E_J_val:.4f} / {abs(Delta_pair_baseline_N1):.4f})^2")
print(f"  = {DN2_baseline:.6f}")
print(f"  sqrt(<DN^2>) = {np.sqrt(DN2_baseline):.6f}")

# =============================================================================
#  SECTION 6: GINZBURG-CORRECTED STEP HEIGHT
# =============================================================================
#
# When Gi is of order unity, the mean-field step height receives corrections.
# In standard Ginzburg-Landau theory for d dimensions:
#
#     F_corrected = F_0 * (1 + C_d * Gi^{nu_d})
#
# where C_d and nu_d depend on the universality class and dimension.
#
# For the BCS system on a graph (effectively 0+1D since L/xi << 1):
#     The "Ginzburg correction" is dominated by the Josephson coupling.
#     F_corrected = sqrt(F_0^2 + delta_F^2) (Pythagorean combination)
#
# For the 3D fabric (32-cell Voronoi tessellation):
#     Fluctuation correlation length:
#     xi_fluct = xi_BCS / Gi^{1/(2*(4-d))}   for d = 3: xi_fluct = xi_BCS / Gi^{1/2}
#
# For d = 3 (fabric embedding dimension):
#     The upper critical dimension for the pairing transition is d_uc = 4.
#     Below d_uc, fluctuations matter near the transition.

print("\n" + "=" * 72)
print("  SECTION 6: CORRECTED QUANTITIES")
print("=" * 72)

d_fabric = 3  # spatial dimensionality of the fabric

# Fluctuation correlation length
# xi_fluct = xi_BCS / Gi^{1/(2*(4-d))} = xi_BCS / Gi^{1/2} for d=3
# Only meaningful if Gi > 0
for label, Gi_val, F0_val, dF_val in [
    ("compound (eps=0.182)", Gi_compound, F_0_compound, delta_F_compound),
    ("baseline (mu_1=0.046)", Gi_baseline_mu1, F_0_baseline_mu1, delta_F_baseline),
]:
    print(f"\n--- {label} ---")
    print(f"  Gi = {Gi_val:.6e}")

    if Gi_val > 0:
        xi_fluct = xi_BCS_val / np.sqrt(Gi_val)**(1.0/(4 - d_fabric))
        print(f"  xi_fluct = xi_BCS / Gi^{{1/2}} = {xi_BCS_val:.4f} / {np.sqrt(Gi_val):.4e}")
        print(f"           = {xi_fluct:.4f} M_KK^{{-1}}")
    else:
        xi_fluct = np.inf
        print(f"  xi_fluct = infinity (no fluctuations)")

    # Pythagorean correction
    F_corr = np.sqrt(F0_val**2 + dF_val**2)
    print(f"  F_corrected = sqrt(F_0^2 + delta_F^2) = {F_corr:.6f} M_KK")
    print(f"  Correction ratio = F_corr / F_0 = {F_corr / F0_val:.6f}")

    # Second-order perturbative correction C * sqrt(Gi)
    # Standard result: C = 1/(4*pi) for d=3 Ising, but for BCS the coefficient
    # is the ratio of fluctuation DOS to mean-field DOS.
    C_pert = 1.0  # conservative O(1) coefficient  # (local)
    F_pert = F0_val * (1 + C_pert * np.sqrt(Gi_val))
    print(f"  F_pert (C=1) = F_0 * (1 + sqrt(Gi)) = {F_pert:.6f} M_KK")

# =============================================================================
#  SECTION 7: SUMMARY TABLE AND GATE VERDICT
# =============================================================================

print("\n" + "=" * 72)
print("  SECTION 7: SUMMARY AND GATE VERDICT")
print("=" * 72)

# Collect all Ginzburg numbers
results = {
    "Gi_compound_2nd_order": Gi_compound,
    "Gi_compound_mu1_2nd_order": Gi_compound_mu1,
    "Gi_baseline_canonical_2nd_order": Gi_baseline_canonical,
    "Gi_baseline_mu1_2nd_order": Gi_baseline_mu1,
    "Gi_direct_compound": Gi_direct_compound,
    "Gi_direct_baseline": Gi_direct_baseline,
    "Gi_4th_compound": Gi_4th_compound,
    "Gi_4th_baseline": Gi_4th_baseline,
    "Gi_thermal_compound": Gi_thermal_compound,
    "Gi_thermal_baseline": Gi_thermal_baseline,
}

print("\n  Estimate                        | Compound    | Baseline")
print("  " + "-" * 66)
for label_pair in [
    ("2nd-order PT", "Gi_compound_2nd_order", "Gi_baseline_mu1_2nd_order"),
    ("Direct tunnel", "Gi_direct_compound", "Gi_direct_baseline"),
    ("4th-moment", "Gi_4th_compound", "Gi_4th_baseline"),
    ("GGE thermal", "Gi_thermal_compound", "Gi_thermal_baseline"),
]:
    name, k_c, k_b = label_pair
    print(f"  {name:33s} | {results[k_c]:10.4e} | {results[k_b]:10.4e}")

# THE GATE: use the most physical estimate
# The 2nd-order PT result is the correct Ginzburg criterion.
# Use compound staircase (eps_corrected = 0.182) as primary.
Gi_primary = Gi_compound
Gi_worst = max(Gi_compound, Gi_compound_mu1, Gi_direct_compound,
               Gi_4th_compound, Gi_thermal_compound)
Gi_best = min(Gi_compound, Gi_compound_mu1, Gi_direct_compound,
              Gi_4th_compound, Gi_thermal_compound)

print(f"\n  PRIMARY Gi (compound, 2nd-order PT) = {Gi_primary:.6e}")
print(f"  WORST-CASE Gi (all estimates)       = {Gi_worst:.6e}")
print(f"  BEST-CASE Gi (all estimates)         = {Gi_best:.6e}")

# Additional: pair number fluctuation
print(f"\n  <(Delta N)^2> (compound) = {DN2_compound:.6f}")
print(f"  <(Delta N)^2> (baseline) = {DN2_baseline:.6f}")

# Gate verdict
if Gi_primary < 0.1:
    verdict = "PASS"
    reason = f"Gi = {Gi_primary:.4e} < 0.1: mean-field staircase is SHARP"
elif Gi_primary > 10.0:
    verdict = "FAIL"
    reason = f"Gi = {Gi_primary:.4e} > 10: fluctuations WASH OUT the staircase"
else:
    verdict = "INFO"
    reason = f"Gi = {Gi_primary:.4e} in [0.1, 10]: marginal regime"

# Check if ALL estimates agree on the verdict
verdicts_all = []
for k, v in results.items():
    if "compound" in k:
        if v < 0.1:
            verdicts_all.append("PASS")
        elif v > 10.0:
            verdicts_all.append("FAIL")
        else:
            verdicts_all.append("INFO")

unanimous = len(set(verdicts_all)) == 1

print(f"\n  GATE VERDICT: {verdict}")
print(f"  REASON: {reason}")
print(f"  All compound estimates agree: {unanimous} ({set(verdicts_all)})")

# Physical interpretation
print("\n" + "=" * 72)
print("  PHYSICAL INTERPRETATION")
print("=" * 72)

if Gi_primary < 0.1:
    print("""
  The staircase steps are WELL-DEFINED. The Josephson inter-cell coupling
  produces fluctuations that are small compared to the step height. The
  mean-field picture of discrete CC levels Lambda(N) is quantitatively
  reliable.

  The pair number is well-defined within each cell:
    sqrt(<DN^2>) << 1 confirms integer pair counting.

  The CC budget funding staircase construction is self-consistent:
  fluctuations do not redistribute the energy across steps.
""")
elif Gi_primary > 10.0:
    print("""
  The staircase steps are WASHED OUT. Josephson fluctuations between cells
  smear the pair number, making the discrete step structure meaningless.
  The CC is NOT quantized -- it is a continuous function of the average
  pair density, and the staircase picture must be abandoned.

  The pair number fluctuation sqrt(<DN^2>) >> 1 means cell-by-cell
  pair counting has no physical meaning.
""")
else:
    print("""
  The staircase is in the MARGINAL regime. Mean-field gives the qualitative
  structure but quantitative corrections are O(1). The step height receives
  Ginzburg corrections:
    F_corrected = F_0 * (1 + O(sqrt(Gi)))

  More refined analysis (RPA, large-N) may be needed to determine whether
  the steps survive as crossovers or sharp transitions.
""")

# =============================================================================
#  SAVE DATA
# =============================================================================

save_path = os.path.join(data_dir, 's61_ginzburg_staircase.npz')
np.savez(
    save_path,
    # Gate
    gate_name="GINZBURG-CC-61",
    gate_verdict=verdict,
    gate_reason=reason,
    # Primary Ginzburg number
    Gi_primary=Gi_primary,
    Gi_worst=Gi_worst,
    Gi_best=Gi_best,
    # All estimates (compound staircase)
    Gi_compound_2nd_order=Gi_compound,
    Gi_compound_mu1_2nd_order=Gi_compound_mu1,
    Gi_direct_compound=Gi_direct_compound,
    Gi_4th_compound=Gi_4th_compound,
    Gi_thermal_compound=Gi_thermal_compound,
    # All estimates (baseline staircase)
    Gi_baseline_canonical_2nd_order=Gi_baseline_canonical,
    Gi_baseline_mu1_2nd_order=Gi_baseline_mu1,
    Gi_direct_baseline=Gi_direct_baseline,
    Gi_4th_baseline=Gi_4th_baseline,
    Gi_thermal_baseline=Gi_thermal_baseline,
    # Fluctuation quantities
    delta_F_compound_2nd=delta_F_compound,
    delta_F_baseline_2nd=delta_F_baseline,
    delta_F_direct=delta_F_direct,
    delta_F_4th=delta_F_4th,
    delta_F_thermal=delta_F_thermal,
    # Step heights
    F_0_compound=F_0_compound,
    F_0_compound_mu1=F_0_compound_mu1,
    F_0_baseline_canonical=F_0_baseline_canonical,
    F_0_baseline_mu1=F_0_baseline_mu1,
    # Pair stiffness
    Delta_pair_compound_N1=Delta_pair_compound_N1,
    Delta_pair_baseline_N1=Delta_pair_baseline_N1,
    # Pair number fluctuation
    DN2_compound=DN2_compound,
    DN2_baseline=DN2_baseline,
    # Physical inputs
    E_J=E_J_val,
    S_plus_1=S_plus_1,
    N_modes=N_modes_val,
    xi_BCS=xi_BCS_val,
    T_acoustic=T_ac,
    delta_k_mean=delta_k_mean,
)

print(f"\nData saved to: {save_path}")
print("DONE.")
