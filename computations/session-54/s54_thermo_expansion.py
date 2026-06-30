#!/usr/bin/env python3
"""
THERMO-EXPANSION-GGE-54: q-Theory Vacuum Pressure from GGE
=============================================================

Computes the q-theory vacuum pressure P_vac = -epsilon + sum_k T_k S_k
using the 8 GGE sector temperatures and sector entropies.

Physics:
  Volovik Paper 05 (2005): vacuum energy in quantum liquids is zero in
  equilibrium. Perturbations (quasiparticles, curvature) induce nonzero
  vacuum energy proportional to the perturbation energy.

  Volovik Paper 15 (2008, Klinkhamer-Volovik): q-theory self-tuning.
  The vacuum variable q adjusts to nullify effective vacuum energy density.
  The generalized Gibbs-Duhem relation for a non-equilibrium system:

    P_vac = -epsilon + sum_k mu_k n_k

  For the GGE with conserved occupation numbers n_k, the chemical potentials
  mu_k = T_k (effective temperature per sector). The Gibbs-Duhem becomes:

    P_vac = -epsilon + sum_k T_k S_k

  where S_k is the Shannon entropy of sector k.

  Key insight from S45 EULER-DEFICIT-45: for canonical N=1 GGE,
    sum_k T_k S_k^{Shannon} = N_pair = 1 exactly (tautology).
  Therefore P_vac = -(epsilon - 1) in M_KK units.

  The question: does the sector-specific temperature structure produce
  cancellation that differs from naive epsilon?

Gate: THERMO-EXPANSION-GGE-54 (INFO)

Session 54, Wave 3, Task 8
Agent: volovik-superfluid-universe-theorist
"""

import numpy as np
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    E_cond, E_exc, n_pairs, N_dof_BCS, M_KK, M_KK_gravity,
    rho_Lambda_obs, M_Pl_reduced, a0_fold, tau_fold,
    E_B1, E_B2_mean, E_B3_mean, PI, d2S_fold
)

# ============================================================================
# SECTION 1: Load GGE data from S43
# ============================================================================

gge_data = np.load(
    os.path.join(os.path.dirname(__file__), "..", "_shared", 's43_gge_temperatures.npz'),
    allow_pickle=True
)

# 8-mode GGE data (1-pair canonical)
nk_exact = gge_data['nk_exact']       # Exact occupation numbers f_k (canonical N=1)
beta_k   = gge_data['beta_k']         # Inverse temperatures beta_k = -ln(f_k)
T_k      = gge_data['T_k']            # Temperatures T_k = 1/beta_k
E_8      = gge_data['E_8']            # Single-particle energies (M_KK)
rho_8    = gge_data['rho']            # Density of states per mode
branch_labels = gge_data['branch_labels']

# Branch-level data
T_B2     = float(gge_data['T_B2'])
T_B1     = float(gge_data['T_B1'])
T_B3     = float(gge_data['T_B3'])
E_GGE    = float(gge_data['E_GGE'])   # = 1.688 M_KK (1-pair)
S_GGE    = float(gge_data['S_GGE'])   # = 1.612 nats
S_max    = float(gge_data['S_max'])    # = ln(8) = 2.079 nats

# Branch energies and entropies
E_branch = gge_data['E_branch']        # [E_B2, E_B1, E_B3]
S_branch = gge_data['S_branch']        # [S_B2, S_B1, S_B3]

print("=" * 72)
print("THERMO-EXPANSION-GGE-54: q-Theory Vacuum Pressure from GGE")
print("=" * 72)

# ============================================================================
# SECTION 2: Verify Euler identity (sum T_k S_k = N_pair)
# ============================================================================

# Shannon entropy per mode: S_k = -f_k ln(f_k)
f_k = nk_exact  # occupation fractions
S_k_shannon = np.where(f_k > 0, -f_k * np.log(f_k), 0.0)

# Euler sum: sum T_k * S_k^Shannon
euler_sum = np.sum(T_k * S_k_shannon)

# Verify this equals N_pair = 1 (S45 tautology)
# T_k = -1/ln(f_k), S_k = -f_k ln(f_k)
# T_k * S_k = f_k / 1 = f_k (since beta_k = -ln(f_k))
# sum = sum f_k = N_pair = 1
euler_check = np.sum(f_k)

print("\n--- Section 2: Euler Identity Verification ---")
print(f"  f_k (occupations):  {f_k}")
print(f"  T_k (temperatures): {T_k}")
print(f"  S_k (Shannon):      {S_k_shannon}")
print(f"  sum T_k S_k  = {euler_sum:.15f}")
print(f"  sum f_k      = {euler_check:.15f}")
print(f"  N_pair       = 1.000000000000000")
print(f"  Deviation    = {abs(euler_sum - 1.0):.2e}")

# ============================================================================
# SECTION 3: Vacuum pressure in q-theory (1-pair canonical)
# ============================================================================

# Energy: epsilon = E_GGE = sum_k E_k * f_k (kinetic) + V_pair (pairing)
# The GGE energy after transit quench:
epsilon_1pair = E_GGE  # = 1.688 M_KK

# q-theory vacuum pressure (generalized Gibbs-Duhem):
# P_vac = -epsilon + sum_k T_k S_k = -epsilon + N_pair
P_vac_1pair = -epsilon_1pair + euler_sum

# Ground state energy (BCS condensate)
E_gs_1pair = epsilon_1pair - E_exc / n_pairs  # E_GGE - E_exc_per_pair
# Actually: E_gs = E_GGE - E_exc/n_pairs is wrong framing.
# The 1-pair GGE has E_GGE = 1.688. The 1-pair ground state has
# E_gs = sum_k E_k f_k^{gs} + V_pair^{gs}.
# From the BCS data: E_cond = -0.137 M_KK is the total condensation energy
# for the 8-mode system. The ground state energy is:
# E_gs = E_normal + E_cond where E_normal = sum_k E_k * f_k^{normal}

# For the unpaired state (normal): all weight on lowest mode (B1)
# E_normal_1pair = E_B1 = 0.819 M_KK
E_normal_1pair = E_B1  # = 0.819 M_KK
E_gs_1pair_corrected = E_normal_1pair + E_cond  # 0.819 - 0.137 = 0.682

# Excitation energy above ground state (1-pair)
E_exc_1pair = epsilon_1pair - E_gs_1pair_corrected

print("\n--- Section 3: q-Theory Vacuum Pressure (1-pair) ---")
print(f"  epsilon (E_GGE, 1-pair)      = {epsilon_1pair:.6f} M_KK")
print(f"  sum T_k S_k                  = {euler_sum:.15f} M_KK")
print(f"  P_vac = -eps + sum T_k S_k   = {P_vac_1pair:.6f} M_KK")
print(f"  E_normal (unpaired, B1)      = {E_normal_1pair:.6f} M_KK")
print(f"  E_cond                       = {E_cond:.6f} M_KK")
print(f"  E_gs (paired)                = {E_gs_1pair_corrected:.6f} M_KK")
print(f"  E_exc above gs               = {E_exc_1pair:.6f} M_KK")

# ============================================================================
# SECTION 4: Equation of state w = P/epsilon
# ============================================================================

w_1pair = P_vac_1pair / epsilon_1pair
w_threshold = -1.0/3.0  # acceleration threshold

print("\n--- Section 4: Equation of State ---")
print(f"  w = P/epsilon                = {w_1pair:.6f}")
print(f"  Acceleration threshold       = {w_threshold:.6f}")
print(f"  w < -1/3?                    = {w_1pair < w_threshold}")
print(f"  P + epsilon/3                = {P_vac_1pair + epsilon_1pair/3:.6f} M_KK")
print(f"  (negative means accelerating)")

# Strong energy condition: rho + 3P >= 0
SEC = epsilon_1pair + 3 * P_vac_1pair
print(f"  rho + 3P                     = {SEC:.6f} M_KK")
print(f"  SEC violated?                = {SEC < 0}")

# ============================================================================
# SECTION 5: Breakdown by branch (B2, B1, B3)
# ============================================================================

# Branch occupations
f_B2 = np.sum(f_k[:4])  # 4 B2 modes
f_B1 = f_k[4]            # 1 B1 mode
f_B3 = np.sum(f_k[5:])  # 3 B3 modes

# Branch Shannon entropies
S_B2_modes = S_k_shannon[:4]
S_B1_modes = S_k_shannon[4:5]
S_B3_modes = S_k_shannon[5:]

TS_B2 = np.sum(T_k[:4] * S_B2_modes)
TS_B1 = np.sum(T_k[4:5] * S_B1_modes)
TS_B3 = np.sum(T_k[5:] * S_B3_modes)

# Branch energies from GGE
E_B2_gge = np.sum(E_8[:4] * f_k[:4])
E_B1_gge = E_8[4] * f_k[4]
E_B3_gge = np.sum(E_8[5:] * f_k[5:])

# Branch pressures
P_B2 = -E_B2_gge + TS_B2
P_B1 = -E_B1_gge + TS_B1
P_B3 = -E_B3_gge + TS_B3

print("\n--- Section 5: Branch Decomposition ---")
print(f"  {'Branch':>8} {'f_k':>10} {'E_k':>12} {'T_k S_k':>12} {'P_k':>12} {'w_k':>10}")
print(f"  {'B2':>8} {f_B2:10.6f} {E_B2_gge:12.6f} {TS_B2:12.6f} {P_B2:12.6f} {P_B2/E_B2_gge if E_B2_gge!=0 else 0:10.6f}")
print(f"  {'B1':>8} {f_B1:10.6f} {E_B1_gge:12.6f} {TS_B1:12.6f} {P_B1:12.6f} {P_B1/E_B1_gge if E_B1_gge!=0 else 0:10.6f}")
print(f"  {'B3':>8} {f_B3:10.6f} {E_B3_gge:12.6f} {TS_B3:12.6f} {P_B3:12.6f} {P_B3/E_B3_gge if E_B3_gge!=0 else 0:10.6f}")
print(f"  {'Total':>8} {f_B2+f_B1+f_B3:10.6f} {E_B2_gge+E_B1_gge+E_B3_gge:12.6f} {TS_B2+TS_B1+TS_B3:12.6f} {P_B2+P_B1+P_B3:12.6f} {w_1pair:10.6f}")

# ============================================================================
# SECTION 6: FD entropy comparison (wrong ensemble, for reference)
# ============================================================================

# FD entropy (grand canonical, S44 formula — KNOWN WRONG for canonical N=1)
S_k_FD = np.where(f_k > 0,
    -f_k * np.log(f_k) - (1 - f_k) * np.log(np.maximum(1 - f_k, 1e-300)),
    0.0
)

TS_FD = np.sum(T_k * S_k_FD)
P_vac_FD = -epsilon_1pair + TS_FD
w_FD = P_vac_FD / epsilon_1pair

print("\n--- Section 6: FD Entropy Comparison (WRONG ensemble, for reference) ---")
print(f"  S_FD total                   = {np.sum(S_k_FD):.6f} nats")
print(f"  sum T_k S_k^FD               = {TS_FD:.6f} M_KK")
print(f"  P_vac (FD)                   = {P_vac_FD:.6f} M_KK")
print(f"  w (FD)                       = {w_FD:.6f}")
print(f"  CAUTION: FD overcounts by {TS_FD - euler_sum:.6f} M_KK (ensemble artifact)")

# ============================================================================
# SECTION 7: Physical units conversion
# ============================================================================

# The 1-pair GGE lives in a single cell. For the 32-cell fabric with 59.8 pairs:
# Total GGE energy = n_pairs * E_GGE_per_pair
# But this is NOT how to compute Lambda. The CC is energy density, not total energy.

# Energy density in the framework:
# rho_GGE = (1/(4 pi^2)) * a_0 * M_KK^4 * (E_GGE / E_normal_total)
# But more directly from Q-THEORY-GGE-53:
# rho_GGE = (2/pi^2) * a_0 * M_KK^4 * E_exc_fraction
# where the spectral action prefactor gives the UV cutoff.

# From S53 Q-THEORY-GGE-53: rho_GGE = 3.74e68 GeV^4
rho_GGE_GeV4 = 3.74e68  # GeV^4 (S53 result)  # (local)

# Vacuum pressure in physical units
# P_vac / epsilon = w = -0.407... (from Section 4)
P_vac_GeV4 = w_1pair * rho_GGE_GeV4

# Lambda_obs
Lambda_obs = rho_Lambda_obs  # 2.7e-47 GeV^4

# Ratio
Lambda_ratio = abs(P_vac_GeV4) / Lambda_obs

print("\n--- Section 7: Physical Units ---")
print(f"  rho_GGE                      = {rho_GGE_GeV4:.3e} GeV^4 (from S53)")
print(f"  P_vac                        = {P_vac_GeV4:.3e} GeV^4")
print(f"  |P_vac| / Lambda_obs         = {Lambda_ratio:.3e}")
print(f"  log10(|P_vac|/Lambda_obs)    = {np.log10(Lambda_ratio):.1f} orders")
print(f"  Lambda_obs                   = {Lambda_obs:.3e} GeV^4")

# ============================================================================
# SECTION 8: The Volovik equilibrium theorem
# ============================================================================

# In equilibrium (Volovik Paper 05): P_vac = 0 exactly.
# The GGE is NOT in equilibrium — it is a non-thermal relic.
# The question: does the GGE self-tune?

# q-theory self-tuning condition: d(rho_vac)/dq = 0 at equilibrium
# For GGE: the conserved integrals PREVENT q from reaching equilibrium.
# Therefore: P_vac != 0, and the residual is set by the GGE structure.

# The thermodynamic identity for the GGE:
# P + epsilon = sum_k T_k S_k = sum_k f_k = N_pair = 1
# Therefore: P = 1 - epsilon (EXACT)

# This is a CONSTRAINT, not a cancellation.
# The non-thermal fraction:
non_thermal_P = P_vac_1pair  # = 1 - E_GGE = 1 - 1.688 = -0.688

# The thermal equivalent would be:
# P_thermal = -epsilon + T_eff * S_total
T_eff_from_E = epsilon_1pair / S_GGE  # = E_GGE / S_GGE
P_thermal = -epsilon_1pair + T_eff_from_E * S_GGE  # = 0 by construction
# This is just -eps + eps = 0. Not meaningful.

# The correct thermal comparison: at T_therm (= 1.047 M_KK from data),
# all modes at same T: P_therm = -E_therm + T_therm * S_therm
# But for canonical N=1 at any single T: sum f_k = 1, so P = 1 - E(T).

print("\n--- Section 8: Volovik Equilibrium Theorem ---")
print(f"  Equilibrium P_vac            = 0 (Paper 05, exact)")
print(f"  GGE P_vac                    = {P_vac_1pair:.6f} M_KK")
print(f"  Identity: P = 1 - epsilon    = {1.0 - epsilon_1pair:.6f} M_KK")
print(f"  (Exact by Euler tautology)")
print(f"  T_eff = E/S                  = {T_eff_from_E:.6f} M_KK")
print(f"  Non-thermal P residual       = {non_thermal_P:.6f} M_KK")
print(f"  |P_vac| / epsilon            = {abs(P_vac_1pair)/epsilon_1pair:.6f}")

# ============================================================================
# SECTION 9: Cancellation analysis — does GGE structure help?
# ============================================================================

# The key question: do different T_k produce partial cancellation?
# Answer: NO. The Euler identity sum T_k S_k = 1 is EXACT regardless of T_k.
# Whether temperatures are equal or different, sum T_k S_k = sum f_k = 1.
# Therefore: P_vac = 1 - E_GGE for ANY distribution of the 1 pair.

# What WOULD produce cancellation?
# In q-theory: the variable q shifts to cancel the vacuum energy.
# But q-theory requires the system to reach thermodynamic equilibrium.
# The GGE integrability prevents this.

# The only way to reduce P_vac:
# 1. Reduce epsilon (= reduce quasiparticle energy)
# 2. Increase sum T_k S_k above 1 (impossible for canonical N=1)
# 3. Break integrability (allow thermalization toward equilibrium where P=0)

# Comparison: thermalized vs GGE
# If the system thermalized to equilibrium at T=0 (ground state):
# epsilon_eq = E_gs = 0.682, P_eq = 1 - 0.682 = 0.318
# Still P > 0 because E_gs < 1!

# The issue: for canonical N=1, the Euler sum is ALWAYS 1.
# P = 1 - E regardless of state. No cancellation is possible.
# This is the Volovik equilibrium theorem operating in reverse:
# even in equilibrium, P != 0 unless E = 1 (which requires mu = 0, T -> inf).

# At infinite temperature: f_k = 1/8, E = sum E_k/8 = 0.882
# P_inf_T = 1 - 0.882 = 0.118 M_KK (still positive!)

E_inf_T = np.sum(E_8) / 8.0
P_inf_T = 1.0 - E_inf_T

# At T=0 (ground state): all weight on lowest energy mode
# f_k = delta_{k,lowest}. E_T0 = E_B1 = 0.819.
E_T0 = E_B1
P_T0 = 1.0 - E_T0

print("\n--- Section 9: Cancellation Analysis ---")
print(f"  sum T_k S_k = 1 for ANY canonical N=1 distribution (EXACT)")
print(f"  P = 1 - E for any state. No cancellation from T_k structure.")
print()
print(f"  State-dependent pressure comparison:")
print(f"    T=0 (ground state, no pairing): P = 1 - {E_T0:.6f} = {P_T0:.6f} M_KK")
print(f"    T=inf (equipartition):           P = 1 - {E_inf_T:.6f} = {P_inf_T:.6f} M_KK")
print(f"    GGE (post-transit):              P = 1 - {epsilon_1pair:.6f} = {P_vac_1pair:.6f} M_KK")
print(f"    GS (BCS paired):                 P = 1 - {E_gs_1pair_corrected:.6f} = {1-E_gs_1pair_corrected:.6f} M_KK")
print()
print(f"  The GGE pressure is NEGATIVE (w = {w_1pair:.4f}).")
print(f"  This is because E_GGE > 1 (quasiparticle energy exceeds the Euler sum).")
print(f"  The Euler sum is FIXED at 1 by the N=1 constraint.")

# ============================================================================
# SECTION 10: Multi-pair (59.8-pair fabric) extrapolation
# ============================================================================

# For N_pair = 59.8 pairs on the fabric:
# Each pair is independent (integrability), so extensive:
# E_total = 59.8 * E_GGE = 59.8 * 1.688 = 101.0 M_KK
# sum T_k S_k = 59.8 * 1 = 59.8 M_KK (by Euler tautology, extensive)
# P_total = -E_total + sum T_k S_k = -101.0 + 59.8 = -41.2 M_KK

E_total_fabric = n_pairs * epsilon_1pair
TS_total_fabric = n_pairs * 1.0  # Euler identity, N_pair per cell
P_total_fabric = -E_total_fabric + TS_total_fabric
w_fabric = P_total_fabric / E_total_fabric

# Physical energy density (from S53):
# rho_total = n_pairs * rho_GGE_per_pair = 3.74e68 GeV^4 (already accounts for 59.8 pairs)
P_fabric_GeV4 = w_fabric * rho_GGE_GeV4
Lambda_ratio_fabric = abs(P_fabric_GeV4) / Lambda_obs

print("\n--- Section 10: 59.8-Pair Fabric Extrapolation ---")
print(f"  N_pairs                      = {n_pairs}")
print(f"  E_total                      = {E_total_fabric:.3f} M_KK")
print(f"  sum T_k S_k (total)          = {TS_total_fabric:.1f} M_KK")
print(f"  P_total                      = {P_total_fabric:.3f} M_KK")
print(f"  w = P/E                      = {w_fabric:.6f}")
print(f"  w_1pair = w_fabric?          = {abs(w_1pair - w_fabric) < 1e-10} (extensive identity)")
print(f"  P_fabric (physical)          = {P_fabric_GeV4:.3e} GeV^4")
print(f"  |P_fabric| / Lambda_obs      = {Lambda_ratio_fabric:.3e}")
print(f"  log10(|P|/Lambda_obs)        = {np.log10(Lambda_ratio_fabric):.1f} orders")

# ============================================================================
# SECTION 11: q-theory susceptibility and self-tuning
# ============================================================================

# From S53 Q-THEORY-GGE-53: chi_q(SA) = 317,863 M_KK^4
chi_q_SA = d2S_fold  # = 317,863 M_KK^4 (spectral action curvature at fold)

# q-theory self-tuning: delta_q = -P_vac / chi_q
# The shift needed to cancel P_vac:
delta_q_needed = -P_vac_1pair / chi_q_SA

# But GGE prevents q from reaching this equilibrium!
# The relaxation is blocked by 8 conserved integrals.

# Residual Lambda if q could partially self-tune:
# Lambda_residual = P_vac^2 / (2 chi_q) (second-order correction)
Lambda_residual_MKK = P_vac_1pair**2 / (2 * chi_q_SA)
Lambda_residual_GeV4 = Lambda_residual_MKK * (M_KK**4 / (4 * PI**2))

# But this assumes q CAN move. For the GGE, q is FROZEN.
# The actual residual is the FULL P_vac.

print("\n--- Section 11: q-Theory Self-Tuning Analysis ---")
print(f"  chi_q (SA curvature)         = {chi_q_SA:.1f} M_KK^4")
print(f"  delta_q needed               = {delta_q_needed:.2e}")
print(f"  Lambda_residual (if q moved)  = {Lambda_residual_MKK:.2e} M_KK^4")
print(f"  Lambda_residual (GeV^4)       = {Lambda_residual_GeV4:.2e} GeV^4")
print(f"  BUT: GGE integrability BLOCKS self-tuning.")
print(f"  Actual P_vac is the FULL {P_vac_1pair:.6f} M_KK, not the residual.")

# ============================================================================
# SECTION 12: Physical interpretation
# ============================================================================

print("\n" + "=" * 72)
print("SECTION 12: PHYSICAL INTERPRETATION")
print("=" * 72)
print()
print("The q-theory vacuum pressure from the GGE is:")
print(f"  P_vac = {P_vac_1pair:.6f} M_KK (per pair)")
print(f"  w = P/rho = {w_1pair:.6f}")
print()
print("KEY STRUCTURAL RESULT:")
print("  For canonical N=1 GGE, the generalized Gibbs-Duhem gives:")
print("    P = -E + sum_k T_k S_k = -E + N_pair = -E + 1 (EXACT)")
print()
print("  This is INDEPENDENT of the temperature distribution.")
print("  The non-thermal structure of the GGE does NOT produce")
print("  partial cancellation — the Euler sum is topologically fixed")
print("  at N_pair = 1 by the canonical constraint.")
print()
print("COMPARISON TO -rho/3 THRESHOLD:")
print(f"  P_vac = {P_vac_1pair:.6f} < -rho/3 = {-epsilon_1pair/3:.6f}")
print(f"  w = {w_1pair:.4f} < -1/3 = {-1/3:.4f}")
print(f"  => ACCELERATED EXPANSION (strong energy condition violated)")
print()
print("BUT:")
print(f"  |P_vac|/Lambda_obs = {Lambda_ratio:.2e} ({np.log10(Lambda_ratio):.0f} orders)")
print(f"  This is the SAME 115-order hierarchy as S53 Q-THEORY-GGE-53.")
print(f"  The GGE pressure is negative (w < -1/3) but 115 orders too large.")
print()
print("VOLOVIK ANALOG:")
print("  In superfluid 3He after a quench, the non-thermal quasiparticles")
print("  carry energy that gravitates but cannot thermalize. The vacuum")
print("  pressure P = -E + TS is negative when E > TS. This is the")
print("  superfluid analog of dark energy — negative pressure from")
print("  non-thermal excitations. But in the 3He case, the system")
print("  eventually reaches equilibrium (P -> 0) via phonon emission")
print("  and vortex dissipation. In this framework, integrability")
print("  prevents that relaxation permanently.")

# ============================================================================
# SECTION 13: Mode-by-mode pressure table
# ============================================================================

print("\n--- Section 13: Mode-by-Mode Pressure Table ---")
print(f"  {'Mode':>8} {'E_k':>10} {'f_k':>10} {'T_k':>10} {'S_k':>10} {'T_k*S_k':>10} {'E_k*f_k':>10} {'P_k':>10} {'w_k':>10}")

for i in range(8):
    Ek_fk = E_8[i] * f_k[i]
    TkSk = T_k[i] * S_k_shannon[i]
    Pk = -Ek_fk + TkSk
    wk = Pk / Ek_fk if Ek_fk != 0 else 0
    label = str(branch_labels[i])
    print(f"  {label:>8} {E_8[i]:10.6f} {f_k[i]:10.6f} {T_k[i]:10.6f} {S_k_shannon[i]:10.6f} {TkSk:10.6f} {Ek_fk:10.6f} {Pk:10.6f} {wk:10.4f}")

print(f"  {'Total':>8} {'':>10} {np.sum(f_k):10.6f} {'':>10} {np.sum(S_k_shannon):10.6f} {euler_sum:10.6f} {np.sum(E_8*f_k):10.6f} {P_vac_1pair:10.6f} {w_1pair:10.4f}")

# Note: the kinetic energy sum_k E_k * f_k is NOT the full E_GGE.
# E_GGE includes the pairing interaction energy.
E_kinetic = np.sum(E_8 * f_k)
E_pair_interaction = epsilon_1pair - E_kinetic

print(f"\n  E_kinetic = sum E_k f_k       = {E_kinetic:.6f} M_KK")
print(f"  E_pair (interaction)          = {E_pair_interaction:.6f} M_KK")
print(f"  E_GGE = E_kin + E_pair        = {E_kinetic + E_pair_interaction:.6f} M_KK")

# ============================================================================
# SECTION 14: The fundamental identity and its implications
# ============================================================================

print("\n" + "=" * 72)
print("SECTION 14: FUNDAMENTAL IDENTITY")
print("=" * 72)
print()
print("For canonical N-pair GGE with 8 modes:")
print()
print("  P_vac = N_pair - E_GGE       [EXACT, any temperature distribution]")
print()
print("  This means:")
print(f"    w = P/E = 1/E - 1 = 1/{epsilon_1pair:.4f} - 1 = {1/epsilon_1pair - 1:.6f}")
print()
print("  The equation of state depends ONLY on E_GGE.")
print("  Temperature structure is irrelevant (absorbed by Euler identity).")
print()
print("  For w < -1/3: need E > 3/2 = 1.5 M_KK")
print(f"  E_GGE = {epsilon_1pair:.4f} > 1.5: {'YES' if epsilon_1pair > 1.5 else 'NO'}")
print(f"  => Accelerating expansion condition: {'MET' if epsilon_1pair > 1.5 else 'NOT MET'}")
print()
print("  For w < -1: need E < 1 M_KK (phantom — P positive, rho < |P|)")
print(f"  E_GGE = {epsilon_1pair:.4f}: w = {w_1pair:.4f} > -1. NOT phantom.")
print(f"  The GGE is quintessence-like: -1 < w < -1/3.")
print()
print("  For negative pressure (P < 0): need E > N_pair = 1")
print(f"  E_GGE = {epsilon_1pair:.4f} > 1: YES => P < 0 (dark-energy-like)")
print(f"  The system has permanent negative pressure because E_exc >> N_pair.")
print()
print("  This is the q-theory non-equilibrium dark energy: vacuum energy")
print("  with w = -0.41 (quintessence-like). The system CANNOT relax to")
print("  equilibrium (integrability), so the equation of state is permanent.")

# ============================================================================
# Gate verdict
# ============================================================================

print("\n" + "=" * 72)
print("GATE VERDICT: THERMO-EXPANSION-GGE-54")
print("=" * 72)
print()
print("STATUS: INFO")
print()
print("RESULT: P_vac = -0.688 M_KK, w = -0.407. Acceleration condition MET.")
print("  GGE is a phantom fluid (w < -1) — CORRECTION: w = -0.407 > -1,")
print("  NOT phantom. w is between -1 and -1/3 (quintessence-like).")
print(f"  Exact: w = 1/E_GGE - 1 = {1/epsilon_1pair - 1:.6f}")
print()

# Correct the phantom statement
is_phantom = w_1pair < -1
is_accelerating = w_1pair < -1/3
is_decelerating = w_1pair > -1/3

print(f"  w = {w_1pair:.6f}")
print(f"  Phantom (w < -1)?           {is_phantom}")
print(f"  Accelerating (w < -1/3)?    {is_accelerating}")
print(f"  Quintessence-like?          {-1 < w_1pair < -1/3}")
print()
print("  The 115-order hierarchy persists (same as S53 Q-THEORY-GGE-53).")
print("  Temperature structure does NOT produce cancellation.")
print("  P = N_pair - E is exact by Euler tautology.")
print()
print("NOT PASS: |P_vac| remains 115 orders above Lambda_obs.")
print("  The equation of state w = -0.41 is mildly interesting")
print("  (between DESI w_0 = -0.71 and cosmological constant w = -1)")
print("  but the magnitude is catastrophic.")

# ============================================================================
# Save results
# ============================================================================

np.savez(
    os.path.join(os.path.dirname(__file__), 's54_thermo_expansion.npz'),
    # 1-pair results
    epsilon_1pair=epsilon_1pair,
    P_vac_1pair=P_vac_1pair,
    w_1pair=w_1pair,
    euler_sum=euler_sum,
    # Branch decomposition
    E_B2_gge=E_B2_gge,
    E_B1_gge=E_B1_gge,
    E_B3_gge=E_B3_gge,
    P_B2=P_B2,
    P_B1=P_B1,
    P_B3=P_B3,
    TS_B2=TS_B2,
    TS_B1=TS_B1,
    TS_B3=TS_B3,
    # Mode data
    f_k=f_k,
    T_k=T_k,
    S_k_shannon=S_k_shannon,
    E_8=E_8,
    # Physical
    rho_GGE_GeV4=rho_GGE_GeV4,
    P_vac_GeV4=P_vac_GeV4,
    Lambda_ratio=Lambda_ratio,
    # Fabric
    E_total_fabric=E_total_fabric,
    P_total_fabric=P_total_fabric,
    w_fabric=w_fabric,
    # q-theory
    chi_q_SA=chi_q_SA,
    delta_q_needed=delta_q_needed,
    Lambda_residual_MKK=Lambda_residual_MKK,
    # Identity
    E_kinetic=E_kinetic,
    E_pair_interaction=E_pair_interaction,
    is_accelerating=is_accelerating,
    is_phantom=is_phantom,
    # Gate
    gate_name=np.array(['THERMO-EXPANSION-GGE-54']),
    gate_verdict=np.array(['INFO']),
    gate_detail=np.array([
        f'P_vac = {P_vac_1pair:.4f} M_KK, w = {w_1pair:.4f}. '
        f'Euler identity: sum T_k S_k = N_pair = 1 (exact). '
        f'P = 1 - E_GGE (independent of T_k distribution). '
        f'Accelerating (w < -1/3). |P|/Lambda_obs = {Lambda_ratio:.2e} (115 orders).'
    ])
)

print("\nData saved to computations/session-54/s54_thermo_expansion.npz")
print("Script complete.")
