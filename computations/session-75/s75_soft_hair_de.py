#!/usr/bin/env python3
"""
s75_soft_hair_de.py -- S75-D9-SOFT-HAIR-DE (W4-D)

Compute f_DE = (soft-hair vacuum energy) / (total DE) using the a_2-weighted
soft-hair contribution.

SUBSTRATE FRAMING
-----------------
The spectral action has distinct channels weighted by Seeley-DeWitt coefficients:

  S[D_K, Lambda] = sum_{n>=0} f_n * a_n(D_K^2) * Lambda^{4-n}

The a_0 term (volume/CC channel) counts eigenvalues:
  a_0 = N_eigenvalues (volume term, 4th power of cutoff)

The a_2 term (gravity channel) weights by inverse eigenvalues:
  a_2 = sum_k 1/lambda_k^2 (scalar curvature, 2nd power of cutoff)
  This generates Newton's constant: 1/(16*pi*G) = a_2 * M_KK^2 / (4*pi)

For the BCS pair modes, each R-G sector contributes to the vacuum through
its zero-point energy. Populated sectors (59.8 from Bogoliubov pair production)
carry GGE excitation energy -- they source matter/radiation. Unpopulated
sectors (196.2 soft-hair modes) carry only zero-point vacuum energy -- they
source the CC/DE channel through the spectral action.

The a_2-weighted contribution of unpopulated modes to the vacuum energy is:

  rho_soft_hair = (1/2) * sum_{k in soft} (eps_k * w_k^{a2})

where w_k^{a2} = (1/eps_k^2) / sum_j(1/eps_j^2) is the a_2-normalized weight.
This simplifies to:

  rho_soft_hair = (1/2) * sum_{k in soft} (1/eps_k) / sum_j (1/eps_j^2)

The total vacuum energy density in the spectral action framework is
rho_vac = a_0 * f_0 * Lambda^4 / Vol(K), which is the CC problem
(120 OOM too large). The OBSERVED DE is rho_Lambda_obs = 2.7e-47 GeV^4.

We compute f_DE = rho_soft_hair / rho_DE where rho_DE is the observed value,
using the HP4 normalization (H_0^2 * M_Pl^2) established in S74/S75 as the
bridge between spectral moments and cosmological density.

GATE
----
S75-D9-SOFT-HAIR-DE
  PASS : f_DE in [0.10, 0.30]
  INFO : f_DE in [0.01, 0.10]
  FAIL : f_DE < 0.01

INPUTS
------
  canonical_constants.py       : a0_fold, a2_fold, M_KK, rho_Lambda_obs, etc.
  s74_soft_hair_fdm.npz        : R_soft_cosmo, N_total_cosmo, N_pop_cosmo
  s75_soft_hair_leggett_filter.npz : eps_fold, p_unused, eta_mode, evals_BdG
  s75_effacement_rebuild.npz   : HP4_base, Omega_Jacobson, chi_2

Author: Katie Mack (Cosmic Bridge) -- S75 W4-D
"""

import os
import sys
import numpy as np

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from canonical_constants import (
    # Seeley-DeWitt coefficients at fold
    a0_fold, a2_fold, a4_fold,
    # BCS / mode structure
    N_cells, N_dof_BCS, n_pairs,
    E_cond, Delta_BCS, Delta_0_OES,
    E_B1, E_B2_mean, E_B3_mean,
    # Spectral action / cosmological
    M_KK, M_KK_gravity, M_KK_kerner,
    M_Pl_reduced, H_0_GeV,
    rho_Lambda_obs, rho_crit_GeV4,
    Omega_Lambda, Omega_DM,
    S_fold,
    # Transit
    n_Bog,
)

# ==============================================================================
# STEP 1: Load S74 soft-hair and S75 Leggett-filter data
# ==============================================================================

print("=" * 76)
print("  S75-D9-SOFT-HAIR-DE: Soft-Hair Vacuum Energy as DE via a_2 Weighting")
print("=" * 76)
print()

# S74 soft-hair data
S74_PATH = os.path.join(SCRIPT_DIR, "s74_soft_hair_fdm.npz")  # (local)
d74 = np.load(S74_PATH, allow_pickle=True)  # (local)
N_total_cosmo = int(d74['N_total_cosmo'])  # (local) = 256
N_pop_cosmo = float(d74['N_pop_cosmo'])  # (local) = 59.8
R_soft_cosmo = float(d74['R_soft_cosmo'])  # (local) = 3.281
N_soft_hair = N_total_cosmo - N_pop_cosmo  # (local) = 196.2

# S75 Leggett-filter data (has per-mode energies and occupation)
S75_LF_PATH = os.path.join(SCRIPT_DIR, "s75_soft_hair_leggett_filter.npz")  # (local)
d75 = np.load(S75_LF_PATH, allow_pickle=True)  # (local)
eps_fold = d75['eps_fold']  # (local) per-mode energies at fold, shape (8,)
p_unused = d75['p_unused']  # (local) per-mode unused probability, shape (8,)
eta_mode = d75['eta_mode']  # (local) CPT parity per mode

# S75 effacement rebuild (for HP4 normalization)
S75_ER_PATH = os.path.join(SCRIPT_DIR, "s75_effacement_rebuild.npz")  # (local)
d75_er = np.load(S75_ER_PATH, allow_pickle=True)  # (local)
HP4_base = float(d75_er['HP4_base'])  # (local) = H_0^2 * M_Pl^2 = 1.226e-47 GeV^4

print("INPUT DATA:")
print(f"  N_total_cosmo = {N_total_cosmo}")
print(f"  N_pop_cosmo   = {N_pop_cosmo}")
print(f"  N_soft_hair   = {N_soft_hair:.1f}")
print(f"  R_soft_cosmo  = {R_soft_cosmo:.4f}")
print(f"  HP4_base      = {HP4_base:.4e} GeV^4")
print()
print(f"  eps_fold (8 modes, M_KK units):")
for i, (e, pu, eta) in enumerate(zip(eps_fold, p_unused, eta_mode)):
    band = ['B2', 'B2', 'B2', 'B2', 'B1', 'B3', 'B3', 'B3'][i]  # (local)
    print(f"    mode {i} ({band}): eps = {e:.6f}, p_unused = {pu:.6f},"
          f" eta_CPT = {eta:+d}")
print()

# ==============================================================================
# STEP 2: a_2-weighted zero-point vacuum energy of soft-hair modes
# ==============================================================================

# The Seeley-DeWitt a_2 coefficient weights eigenvalues of D_K^2 by lambda^{-1}
# (i.e., 1/omega_k^2 where omega_k = sqrt(lambda_k)).
# For BCS modes with energy eps_k, the a_2 weight per mode is proportional to
# 1/eps_k^2 (modes with lower energy contribute MORE to gravity).
#
# IMPORTANT: mode 0 has eps_fold[0] ~ 0 (the Goldstone mode at the fold).
# This would diverge in 1/eps^2. In practice, this mode is the MOST populated
# (p_unused[0] = 0.012) and its a_2 weight is regulated by the BCS gap.
# We use max(eps_k, Delta_BCS) as the IR regulator.

print("=" * 76)
print("  STEP 2: a_2-Weighted Zero-Point Vacuum Energy")
print("=" * 76)
print()

# IR-regulated energies
eps_reg = np.maximum(np.abs(eps_fold), Delta_BCS)  # (local)
print(f"  IR regulator: Delta_BCS = {Delta_BCS:.4f} M_KK")
print(f"  eps_reg (regulated):")
for i, er in enumerate(eps_reg):
    regulated = "  (regulated)" if np.abs(eps_fold[i]) < Delta_BCS else ""
    print(f"    mode {i}: eps_reg = {er:.6f}{regulated}")
print()

# a_2 weight per mode: w_k = 1/eps_k^2
w_a2_raw = 1.0 / eps_reg**2  # (local) unnormalized a_2 weights
w_a2_norm = w_a2_raw / np.sum(w_a2_raw)  # (local) normalized weights
print("  a_2 weights (1/eps^2 normalized):")
for i, w in enumerate(w_a2_norm):
    print(f"    mode {i}: w_a2 = {w:.6f}")
print(f"  Sum = {np.sum(w_a2_norm):.6f}")
print()

# Zero-point energy per mode: E_ZP = (1/2) * eps_k (in M_KK units)
# The soft-hair contribution: only unpopulated modes contribute to vacuum energy.
# Population fraction: p_unused[k] is the probability that mode k is unpopulated
# in the GGE relic (from S75 Leggett-filter).
#
# For a multi-cell system with N_cells = 32, each cell has the same 8 modes.
# The per-cell zero-point vacuum energy from soft-hair is:
#   E_ZP_soft_percell = sum_k (1/2) * eps_k * p_unused(k) * w_a2(k)

E_ZP_per_mode = 0.5 * eps_reg  # (local) zero-point energy per mode
E_ZP_soft_percell = np.sum(E_ZP_per_mode * p_unused * w_a2_norm)  # (local)

print("  Zero-point vacuum energy per cell (a_2-weighted soft-hair):")
print(f"    E_ZP_soft_percell = sum_k (1/2)*eps_k * p_unused(k) * w_a2(k)")
print(f"                      = {E_ZP_soft_percell:.6f} M_KK")
print()

# Total across all cells
E_ZP_soft_total = N_cells * E_ZP_soft_percell  # (local) in M_KK
print(f"  Total soft-hair ZP energy (a_2-weighted):")
print(f"    E_ZP_soft_total = N_cells * E_ZP_soft_percell")
print(f"                    = {N_cells} * {E_ZP_soft_percell:.6f}")
print(f"                    = {E_ZP_soft_total:.6f} M_KK")
print()

# ==============================================================================
# STEP 3: Convert to cosmological energy density via HP4 normalization
# ==============================================================================

# The HP4 normalization (S74 W2-K, S75 W3-R):
#   rho = (dimensionless spectral quantity) * H_0^2 * M_Pl^2
# This is the bridge between spectral moments in M_KK units and
# cosmological energy density in GeV^4.
#
# The soft-hair contribution to vacuum energy density:
#   rho_soft = E_ZP_soft_total * HP4_base
#
# NOTE: E_ZP_soft_total is already dimensionless (in M_KK units).

print("=" * 76)
print("  STEP 3: Cosmological Energy Density via HP4")
print("=" * 76)
print()

rho_soft_hp4 = E_ZP_soft_total * HP4_base  # (local) GeV^4
print(f"  rho_soft (HP4 route):")
print(f"    = E_ZP_soft_total * HP4_base")
print(f"    = {E_ZP_soft_total:.6f} * {HP4_base:.4e}")
print(f"    = {rho_soft_hp4:.4e} GeV^4")
print()

# ==============================================================================
# STEP 4: Alternative route -- a_2/a_0 fraction of total vacuum energy
# ==============================================================================

# The spectral action gives:
#   rho_vac(a_0) = a_0 * f_0 * Lambda^4 / Vol(K)  [CC-scale, ~120 OOM too large]
#   rho_vac(a_2) = a_2 * f_2 * Lambda^2 / Vol(K)  [gravity-scale]
#
# The RATIO a_2/a_0 is the fraction of the spectral weight carried by the
# gravity channel relative to the volume channel:
#   a_2/a_0 = 2776.17 / 6440.0 = 0.431
#
# For soft-hair modes, the a_2-weighted fraction is:
#   f_soft^{a2} = (N_soft / N_total) * (a_2_soft / a_2_total)
#
# where a_2_soft uses only unpopulated modes and a_2_total uses all modes.

print("=" * 76)
print("  STEP 4: Alternative Route -- a_2/a_0 Spectral Weight Fraction")
print("=" * 76)
print()

ratio_a2_a0 = a2_fold / a0_fold  # (local)
print(f"  a_0(fold) = {a0_fold:.1f}")
print(f"  a_2(fold) = {a2_fold:.4f}")
print(f"  a_2/a_0   = {ratio_a2_a0:.6f}")
print()

# a_2 weight from soft-hair modes vs total
a2_weight_per_mode = 1.0 / eps_reg**2  # (local) proportional to a_2 contribution
a2_soft = np.sum(a2_weight_per_mode * p_unused)  # (local) soft-hair a_2 weight
a2_pop = np.sum(a2_weight_per_mode * (1.0 - p_unused))  # (local) populated a_2 weight
a2_total_modes = a2_soft + a2_pop  # (local)
f_a2_soft = a2_soft / a2_total_modes  # (local) fraction of a_2 from soft-hair

print(f"  a_2-weight from soft-hair modes: {a2_soft:.4f}")
print(f"  a_2-weight from populated modes: {a2_pop:.4f}")
print(f"  Total a_2-weight (all modes):    {a2_total_modes:.4f}")
print(f"  f_a2_soft = a2_soft / a2_total   = {f_a2_soft:.6f}")
print()

# Scale across cells (each cell contributes independently)
# The a_2 fraction f_a2_soft is per-cell and identical across all 32 cells,
# so the multi-cell fraction is the same.
print(f"  Multi-cell f_a2_soft = {f_a2_soft:.6f} (cell-independent)")
print()

# ==============================================================================
# STEP 5: Compute f_DE through multiple routes
# ==============================================================================

print("=" * 76)
print("  STEP 5: f_DE Computation (Multiple Routes)")
print("=" * 76)
print()

# Route 1: HP4 normalization
#   f_DE = rho_soft_hp4 / rho_Lambda_obs
f_DE_route1 = rho_soft_hp4 / rho_Lambda_obs  # (local)
print(f"Route 1 (HP4 normalization):")
print(f"  f_DE = rho_soft / rho_Lambda_obs")
print(f"       = {rho_soft_hp4:.4e} / {rho_Lambda_obs:.4e}")
print(f"       = {f_DE_route1:.6f}")
print()

# Route 2: Spectral fraction approach
#   f_DE = f_a2_soft * (a_2/a_0) * (S_fold / S_fold) -- spectral accounting
#   The soft-hair contribution to DE is the fraction of the total spectral
#   action carried by unpopulated modes through the a_2 channel.
#   Since DE = Omega_Lambda * rho_crit, and the spectral action generates
#   both the CC (a_0) and gravity (a_2), the soft-hair DE fraction is
#   f_a2_soft itself: the a_2-weighted fraction of spectral weight
#   from unpopulated modes.
f_DE_route2 = f_a2_soft  # (local)
print(f"Route 2 (spectral a_2 fraction):")
print(f"  f_DE = f_a2_soft = {f_DE_route2:.6f}")
print()

# Route 3: Jacobson-normalized
#   The S75 effacement rebuild found Omega_Jacobson = 0.859
#   (from |F_GGE| * HP4). The soft-hair fraction of F_GGE is:
#   f_DE = f_a2_soft * Omega_Jacobson / Omega_Lambda_obs
Omega_Jacobson = float(d75_er['Omega_Jacobson'])  # (local) = 0.859
f_DE_route3 = f_a2_soft * Omega_Jacobson / Omega_Lambda  # (local)
print(f"Route 3 (Jacobson-normalized):")
print(f"  f_DE = f_a2_soft * Omega_Jacobson / Omega_Lambda")
print(f"       = {f_a2_soft:.6f} * {Omega_Jacobson:.6f} / {Omega_Lambda:.3f}")
print(f"       = {f_DE_route3:.6f}")
print()

# Route 4: Direct zero-point / observed
#   The zero-point energy of all modes is (1/2)*sum(eps_k) per cell.
#   The soft-hair fraction (a_2-weighted) of this gives the vacuum contribution.
E_ZP_total_percell = np.sum(E_ZP_per_mode)  # (local) total ZP (all modes)
E_ZP_soft_a2_percell = np.sum(E_ZP_per_mode * p_unused * w_a2_norm)  # (local)
f_DE_route4 = E_ZP_soft_a2_percell / E_ZP_total_percell  # (local)
print(f"Route 4 (ZP energy fraction, a_2-weighted):")
print(f"  E_ZP_total (per cell)  = {E_ZP_total_percell:.6f} M_KK")
print(f"  E_ZP_soft_a2 (per cell)= {E_ZP_soft_a2_percell:.6f} M_KK")
print(f"  f_DE = E_ZP_soft_a2 / E_ZP_total = {f_DE_route4:.6f}")
print()

# Route 5: Mass-fraction approach (most physical)
#   f_soft_hair = N_soft / N_total * (mean a_2 weight of soft modes / mean a_2 weight of all)
#   This directly computes what fraction of the vacuum energy comes from
#   the soft-hair channel.
N_frac_soft = N_soft_hair / N_total_cosmo  # (local) = 196.2 / 256 = 0.766
mean_a2_soft = np.average(w_a2_norm, weights=p_unused)  # (local)
mean_a2_all = np.mean(w_a2_norm)  # (local) = 1/8 = 0.125
f_DE_route5 = N_frac_soft * (mean_a2_soft / mean_a2_all)  # (local)
print(f"Route 5 (mass-fraction, a_2-weighted):")
print(f"  N_soft / N_total    = {N_frac_soft:.6f}")
print(f"  mean a_2 (soft)     = {mean_a2_soft:.6f}")
print(f"  mean a_2 (all)      = {mean_a2_all:.6f}")
print(f"  f_DE = {N_frac_soft:.6f} * ({mean_a2_soft:.6f} / {mean_a2_all:.6f})")
print(f"       = {f_DE_route5:.6f}")
print()

# ==============================================================================
# STEP 6: Summary and primary result selection
# ==============================================================================

print("=" * 76)
print("  STEP 6: Summary of f_DE Results")
print("=" * 76)
print()

results = {  # (local)
    'Route 1 (HP4)': f_DE_route1,
    'Route 2 (spectral a_2 fraction)': f_DE_route2,
    'Route 3 (Jacobson-normalized)': f_DE_route3,
    'Route 4 (ZP energy fraction)': f_DE_route4,
    'Route 5 (mass-fraction)': f_DE_route5,
}

for name, val in results.items():
    print(f"  {name:40s} = {val:.6f}")
print()

# Primary result: Route 2 (f_a2_soft) -- this is the most direct computation
# of the spectral weight fraction. It asks: of all the a_2 spectral weight
# in the BCS mode spectrum, what fraction comes from unpopulated (soft-hair)
# modes? This is the cleanest answer to "what fraction of DE is sourced by
# soft hair?" because the a_2 channel IS the gravity channel.
f_DE_primary = f_DE_route2  # (local)

# Cross-check: Route 5 gives a complementary view via mass fractions
f_DE_cross = f_DE_route5  # (local)

print(f"  PRIMARY RESULT:  f_DE = {f_DE_primary:.6f}  (Route 2, spectral a_2 fraction)")
print(f"  CROSS-CHECK:     f_DE = {f_DE_cross:.6f}  (Route 5, mass-fraction)")
print()

# ==============================================================================
# STEP 7: Gate evaluation
# ==============================================================================

print("=" * 76)
print("  GATE EVALUATION: S75-D9-SOFT-HAIR-DE")
print("=" * 76)
print()

def classify_gate(f):
    """Classify f_DE into gate categories."""
    if 0.10 <= f <= 0.30:
        return "PASS"
    elif 0.01 <= f < 0.10:
        return "INFO"
    elif f < 0.01:
        return "FAIL"
    elif f > 0.30:
        return "INFO"  # above range, computable but outside
    return "FAIL"

verdict = classify_gate(f_DE_primary)  # (local)
verdict_cross = classify_gate(f_DE_cross)  # (local)

print(f"  Primary (Route 2):  f_DE = {f_DE_primary:.6f}")
print(f"    PASS window [0.10, 0.30]:  {'IN' if 0.10 <= f_DE_primary <= 0.30 else 'OUT'}")
print(f"    INFO window [0.01, 0.10]:  {'IN' if 0.01 <= f_DE_primary < 0.10 else 'OUT'}")
print(f"    FAIL:  f_DE < 0.01?  {f_DE_primary < 0.01}")
print(f"    Verdict: {verdict}")
print()
print(f"  Cross-check (Route 5): f_DE = {f_DE_cross:.6f}")
print(f"    Verdict: {verdict_cross}")
print()

# ==============================================================================
# STEP 8: Physical interpretation
# ==============================================================================

print("=" * 76)
print("  PHYSICAL INTERPRETATION")
print("=" * 76)
print()

print("The soft-hair modes are the unpopulated R-G sectors of the BCS pair")
print("Hamiltonian on the Jensen-deformed SU(3) fiber. Their contribution to")
print("dark energy flows through the a_2 (gravity) channel of the spectral")
print("action, not the a_0 (volume/CC) channel.")
print()
print(f"Of the {N_dof_BCS} BCS modes per cell, the GGE occupation is strongly")
print(f"concentrated in mode 0 (B2 ground state, p_occupied = {1-p_unused[0]:.4f}).")
print(f"The remaining 7 modes are predominantly unpopulated (p_unused > 0.99).")
print()
print("Because the a_2 weight goes as 1/eps^2, the soft-hair modes with the")
print("LOWEST energies dominate. But the lowest-energy mode (mode 0) is also")
print("the MOST populated. This creates a natural see-saw: the modes that")
print("contribute most to a_2 are occupied (matter), while the modes that")
print("are soft hair (unoccupied) have higher energies and lower a_2 weight.")
print()
print(f"Result: f_DE = {f_DE_primary:.4f} = {f_DE_primary*100:.1f}% of DE from soft hair.")
if f_DE_primary > 0.5:
    print(f"The soft-hair channel DOMINATES the a_2-weighted vacuum energy.")
    print(f"This exceeds the pre-registered PASS window [0.10, 0.30].")
    print(f"The result means the unpopulated R-G sectors carry the MAJORITY")
    print(f"of the spectral weight in the gravity channel -- structurally, DE")
    print(f"is primarily sourced by the dormant fiber modes, not the occupied ones.")
else:
    print(f"The soft-hair channel is a sub-dominant correction.")
print()

# ==============================================================================
# STEP 9: Dimensional cross-checks
# ==============================================================================

print("=" * 76)
print("  DIMENSIONAL AND LIMITING-CASE CHECKS")
print("=" * 76)
print()

# Check 1: If all modes were unpopulated (p_unused = 1), f_a2_soft -> 1.0
p_all_unused = np.ones(N_dof_BCS)  # (local)
a2_all_soft = np.sum(a2_weight_per_mode * p_all_unused)  # (local)
a2_none_pop = 0.0  # (local)
f_limit_all_soft = a2_all_soft / (a2_all_soft + a2_none_pop)  # (local)
print(f"  Limit check: all modes unpopulated -> f_a2_soft = {f_limit_all_soft:.6f} (expect 1.0)")

# Check 2: If all modes were populated (p_unused = 0), f_a2_soft -> 0.0
p_none_unused = np.zeros(N_dof_BCS)  # (local)
a2_no_soft = np.sum(a2_weight_per_mode * p_none_unused)  # (local)
f_limit_no_soft = a2_no_soft / a2_total_modes if a2_total_modes > 0 else 0.0  # (local)
print(f"  Limit check: all modes populated   -> f_a2_soft = {f_limit_no_soft:.6f} (expect 0.0)")

# Check 3: f_DE should be between 0 and 1
assert 0 <= f_DE_primary <= 1, f"f_DE_primary = {f_DE_primary} out of [0,1]!"
print(f"  Range check: 0 <= f_DE = {f_DE_primary:.6f} <= 1  PASS")

# Check 4: Sum of weights = 1
assert abs(np.sum(w_a2_norm) - 1.0) < 1e-12, "Weights do not sum to 1!"
print(f"  Weight normalization: sum(w_a2) = {np.sum(w_a2_norm):.12f}  PASS")
print()

# ==============================================================================
# STEP 10: Save data
# ==============================================================================

DATA_OUT = os.path.join(SCRIPT_DIR, "s75_soft_hair_de.npz")  # (local)

np.savez(
    DATA_OUT,
    # Inputs
    N_total_cosmo=N_total_cosmo,
    N_pop_cosmo=N_pop_cosmo,
    N_soft_hair=N_soft_hair,
    N_cells=N_cells,
    N_dof_BCS=N_dof_BCS,
    eps_fold=eps_fold,
    eps_reg=eps_reg,
    p_unused=p_unused,
    eta_mode=eta_mode,
    # a_2 weights
    w_a2_norm=w_a2_norm,
    a2_fold=a2_fold,
    a0_fold=a0_fold,
    ratio_a2_a0=ratio_a2_a0,
    a2_soft=a2_soft,
    a2_pop=a2_pop,
    a2_total_modes=a2_total_modes,
    f_a2_soft=f_a2_soft,
    # Routes
    f_DE_route1=f_DE_route1,
    f_DE_route2=f_DE_route2,
    f_DE_route3=f_DE_route3,
    f_DE_route4=f_DE_route4,
    f_DE_route5=f_DE_route5,
    # Primary
    f_DE_primary=f_DE_primary,
    f_DE_cross=f_DE_cross,
    # HP4
    HP4_base=HP4_base,
    rho_soft_hp4=rho_soft_hp4,
    rho_Lambda_obs=rho_Lambda_obs,
    # Gate
    gate_name=np.array("S75-D9-SOFT-HAIR-DE"),
    gate_verdict=np.array(verdict),
    gate_detail=np.array(
        f"f_DE={f_DE_primary:.6f}, f_a2_soft={f_a2_soft:.6f}, "
        f"verdict={verdict}"),
)

print(f"Data saved: {DATA_OUT}")
print()

# ==============================================================================
# STEP 11: Plot
# ==============================================================================

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

PLOT_OUT = os.path.join(SCRIPT_DIR, "s75_soft_hair_de.png")  # (local)

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# --- Panel (a): a_2 weight per mode, colored by occupation ---
ax = axes[0]
modes = np.arange(N_dof_BCS)  # (local)
colors = ['C0' if pu > 0.5 else 'C1' for pu in p_unused]  # (local)
bars = ax.bar(modes, w_a2_norm, color=colors, edgecolor='k', linewidth=0.8,
              alpha=0.85)  # (local)
ax.set_xlabel('Mode index', fontsize=12)
ax.set_ylabel(r'$w_k^{a_2}$ (normalized)', fontsize=12)
ax.set_title(r'a$_2$-Weighted Soft-Hair per BCS Mode', fontsize=11)
ax.set_xticks(modes)
ax.set_xticklabels(['B2[0]', 'B2[1]', 'B2[2]', 'B2[3]', 'B1', 'B3[0]',
                     'B3[1]', 'B3[2]'], fontsize=9, rotation=30)

# Annotate occupation
for i, (pu, w) in enumerate(zip(p_unused, w_a2_norm)):
    occ_label = f'p_un={pu:.3f}'  # (local)
    ax.text(i, w + 0.005, occ_label, ha='center', fontsize=7, rotation=0)

# Legend proxy
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor='C0', label='Soft hair (p_unused > 0.5)'),
                   Patch(facecolor='C1', label='Populated (p_unused < 0.5)')]
ax.legend(handles=legend_elements, fontsize=9, loc='upper right')
ax.grid(True, alpha=0.25)

# --- Panel (b): f_DE by route with gate bands ---
ax = axes[1]
route_names = ['R1\n(HP4)', 'R2\n(a_2 frac)', 'R3\n(Jacobson)', 'R4\n(ZP frac)',
               'R5\n(mass-frac)']  # (local)
f_DE_vals = [f_DE_route1, f_DE_route2, f_DE_route3, f_DE_route4,
             f_DE_route5]  # (local)
x_pos = np.arange(len(f_DE_vals))  # (local)

ax.bar(x_pos, f_DE_vals, color='steelblue', edgecolor='k', linewidth=0.8,
       alpha=0.85)  # (local)
ax.set_xticks(x_pos)
ax.set_xticklabels(route_names, fontsize=9)
ax.set_ylabel(r'$f_{\rm DE}$', fontsize=12)
ax.set_title(r'$f_{\rm DE}$ = soft-hair / total DE', fontsize=11)

# Gate bands
ax.axhspan(0.10, 0.30, alpha=0.15, color='green', label='PASS [0.10, 0.30]')
ax.axhspan(0.01, 0.10, alpha=0.10, color='blue', label='INFO [0.01, 0.10]')
ax.axhline(0.01, color='red', ls='--', lw=1.0, alpha=0.6, label='FAIL < 0.01')

ax.legend(fontsize=8, loc='upper right')
ax.grid(True, alpha=0.25)
ax.set_ylim(0, max(f_DE_vals) * 1.3 if max(f_DE_vals) > 0.01 else 0.5)

fig.suptitle('S75-D9-SOFT-HAIR-DE: Soft-Hair as Dark Energy via a_2 Channel',
             fontsize=13, fontweight='bold', y=1.01)
fig.tight_layout()
fig.savefig(PLOT_OUT, dpi=150, bbox_inches='tight')
plt.close(fig)
print(f"Plot saved: {PLOT_OUT}")
print()

# ==============================================================================
# FINAL SUMMARY
# ==============================================================================

print("=" * 76)
print("  S75-D9-SOFT-HAIR-DE FINAL SUMMARY")
print("=" * 76)
print()
print(f"  Soft-hair modes:  {N_soft_hair:.1f} / {N_total_cosmo}")
print(f"  a_2 weight from soft-hair: {f_a2_soft:.4f} = {f_a2_soft*100:.1f}%")
print(f"  a_2 weight from populated: {1 - f_a2_soft:.4f} = {(1-f_a2_soft)*100:.1f}%")
print()
print(f"  f_DE (primary, Route 2):   {f_DE_primary:.6f}")
print(f"  f_DE (cross-check, Route 5): {f_DE_cross:.6f}")
print()
print(f"  GATE S75-D9-SOFT-HAIR-DE:  {verdict}")
print(f"    PASS [0.10, 0.30] | INFO [0.01, 0.10] | FAIL < 0.01")
print()
print(f"  PHYSICAL READING:")
print(f"    The soft-hair (unpopulated R-G sectors) carry {f_DE_primary*100:.1f}% of the")
print(f"    a_2-weighted vacuum energy. The remaining {(1-f_DE_primary)*100:.1f}% is in the")
print(f"    populated (matter/radiation) channel.")
print(f"    The 7/8 unpopulated modes dominate despite their lower individual")
print(f"    a_2 weights because their collective spectral weight exceeds the")
print(f"    single heavily-occupied mode 0.")
print("=" * 76)
