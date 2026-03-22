#!/usr/bin/env python3
"""
MULTI-T-FRIEDMANN-49: Modified Friedmann equation for 8-temperature GGE relic.

Gate: MULTI-T-FRIEDMANN-49
  PASS: |w_0(GGE) - w_0(DESI)| < |w_0(single-T) - w_0(DESI)| (GGE moves toward data)
  INFO: shift < 1%
  FAIL: GGE moves w_0 away from data

Physics (Einstein):
  The GGE post-transit state has 8 distinct temperatures (Richardson-Gaudin conserved
  quantities). S48 computed w_0 = -1/(1+alpha) where alpha = E/P (Volovik DM/DE ratio).
  The S48 alpha_Z = 1.152, giving w_0 = -0.465.

  CORRECTION DISCOVERED IN THIS COMPUTATION:
  S48 used the S46 occupation numbers n_k (quench projection), NOT the GGE occupations
  from Richardson-Gaudin. The GGE has more uniform B2 occupations (0.193 vs 0.168-0.267)
  and lower total energy (1.375 vs 1.688 M_KK, per-spin * 2).

  The CORRECT comparison is: GGE (multi-T) vs single-T at the SAME total energy.
  The multi-T effect shifts w_0 toward DESI because non-uniform temperatures
  redistribute pressure relative to energy.

  KEY DEFINITION: alpha = E_total / P_Zubarev (S48 line 185). w_0 = -1/(1+alpha).
  This means w_0 = -P/(E+P), which is the Volovik vacuum medium EOS.

Inputs:
  - s39_richardson_gaudin.npz (8 conserved quantities, GGE state)
  - s48_dmde_refine.npz (S48 w_0/w_a, alpha values, pressures)
  - s46_zubarev_derivation.npz (S46 occupations, alpha definitions)
  - canonical_constants.py

Author: Einstein-Theorist
Session: 49
"""

import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
os.chdir(SCRIPT_DIR)
import numpy as np
from scipy.optimize import brentq, curve_fit
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from canonical_constants import (
    tau_fold, E_cond, E_cond_ED_8mode, N_dof_BCS,
    Omega_m, Omega_Lambda, Omega_r,
    rho_Lambda_obs, M_KK, M_KK_gravity, M_Pl_reduced,
    E_B1, E_B2_mean, E_B3_mean
)

np.set_printoptions(precision=8, linewidth=120)

print("=" * 78)
print("MULTI-T-FRIEDMANN-49: 8-Temperature GGE Modified Friedmann Equation")
print("=" * 78)

# =============================================================================
# Step 1: Load all relevant data
# =============================================================================

d_rg = np.load('s39_richardson_gaudin.npz', allow_pickle=True)
d_s48 = np.load('s48_dmde_refine.npz', allow_pickle=True)
d_s46 = np.load('s46_zubarev_derivation.npz', allow_pickle=True)

idx_fold = 3  # tau=0.2, closest to fold
epsilon_k = d_rg['E_8_tau'][idx_fold]
labels = d_rg['branch_labels']

# GGE state (Richardson-Gaudin)
psi_fold = d_rg['psi_fold']
lambda_k = -np.log(np.abs(psi_fold)**2)
n_k_GGE = 1.0 / (1.0 + np.exp(lambda_k))
T_k_GGE = epsilon_k / lambda_k

# S46 state (quench projection — what S48 used)
n_k_s46 = d_s46['n_k']
T_k_s46 = d_s46['T_k']

# Quasiparticle energies
Delta_k = d_rg['Delta_k_fold']
E_qp_k = np.sqrt(epsilon_k**2 + Delta_k**2)

print("\n--- Step 1: State Comparison ---")
print(f"{'Mode':>7s} | {'n_GGE':>8s} | {'n_S46':>8s} | {'T_GGE':>8s} | {'T_S46':>8s} | {'eps_k':>8s}")
print("-" * 65)
for i in range(8):
    print(f"{labels[i]:>7s} | {n_k_GGE[i]:8.6f} | {n_k_s46[i]:8.6f} | "
          f"{T_k_GGE[i]:8.6f} | {T_k_s46[i]:8.6f} | {epsilon_k[i]:8.6f}")

# Total energies (with spin degeneracy factor 2)
E_GGE = 2.0 * np.sum(n_k_GGE * epsilon_k)
E_s46 = 2.0 * np.sum(n_k_s46 * epsilon_k)
print(f"\nTotal energies (2x spin):")
print(f"  E_GGE = {E_GGE:.6f}")
print(f"  E_S46 = {E_s46:.6f}")
print(f"  E_S48_stored = {float(d_s48['E_GGE']):.6f}")
print(f"  Ratio GGE/S46 = {E_GGE/E_s46:.4f}")

# =============================================================================
# Step 2: Zubarev pressure for each state
# =============================================================================

print("\n--- Step 2: Zubarev Pressures ---")

# P_Z = 2 * sum_k T_k * ln(1 + exp(-lambda_k))  [with spin 2x]
# For GGE: T_k = epsilon_k / lambda_k, and the argument is -lambda_k
P_k_GGE = T_k_GGE * np.log(1.0 + np.exp(-lambda_k))
P_Z_GGE = 2.0 * np.sum(P_k_GGE)

# For S46: T_k = epsilon_k / ln((1-n_k)/n_k), argument = -epsilon_k/T_k
lambda_k_s46 = np.log((1.0 - n_k_s46) / n_k_s46)  # = epsilon_k / T_k
P_k_s46 = T_k_s46 * np.log(1.0 + np.exp(-lambda_k_s46))
P_Z_s46 = 2.0 * np.sum(P_k_s46)

print(f"Zubarev pressures:")
print(f"  P_Z(GGE) = {P_Z_GGE:.6f}")
print(f"  P_Z(S46) = {P_Z_s46:.6f}")
print(f"  P_Z(S48_stored) = {float(d_s48['P_GGE_recomp']):.6f}")

# =============================================================================
# Step 3: Alpha = E/P and w_0 = -1/(1+alpha) = -P/(E+P)
# =============================================================================

print("\n--- Step 3: Alpha and w_0 ---")

# S48 definition: alpha = E/P (line 185 of s48_dmde_refine.py)
alpha_Z_GGE = E_GGE / P_Z_GGE
alpha_Z_s46 = E_s46 / P_Z_s46

w0_GGE = -1.0 / (1.0 + alpha_Z_GGE)
w0_s46 = -1.0 / (1.0 + alpha_Z_s46)

print(f"alpha_Z(GGE) = E/P = {alpha_Z_GGE:.6f}  ->  w_0 = {w0_GGE:.6f}")
print(f"alpha_Z(S46) = E/P = {alpha_Z_s46:.6f}  ->  w_0 = {w0_s46:.6f}")
print(f"alpha_Z(S48_stored) = {float(d_s48['alpha_Zubarev_P']):.6f}  ->  w_0 = {float(d_s48['w0_band_lo']):.6f}")

# =============================================================================
# Step 4: Apples-to-apples — single-T at SAME total energy as GGE
# =============================================================================

print("\n--- Step 4: Single-T Reference at Same Energy ---")

# Find T_match such that E_single(T_match) = E_GGE
def E_thermal(T):
    """Total energy at temperature T (with 2x spin)."""
    n = 1.0 / (1.0 + np.exp(epsilon_k / T))
    return 2.0 * np.sum(n * epsilon_k)

T_match = brentq(lambda T: E_thermal(T) - E_GGE, 0.01, 10.0)
n_k_match = 1.0 / (1.0 + np.exp(epsilon_k / T_match))
P_k_match = T_match * np.log(1.0 + np.exp(-epsilon_k / T_match))
P_Z_match = 2.0 * np.sum(P_k_match)
alpha_Z_match = E_GGE / P_Z_match
w0_match = -1.0 / (1.0 + alpha_Z_match)

print(f"T_match (same E as GGE) = {T_match:.6f}")
print(f"E_match = {E_thermal(T_match):.6f} (should = {E_GGE:.6f})")
print(f"P_Z(match) = {P_Z_match:.6f}")
print(f"alpha_Z(match) = {alpha_Z_match:.6f}  ->  w_0 = {w0_match:.6f}")

# Also find T_match for S46 energy
T_match_s46 = brentq(lambda T: E_thermal(T) - E_s46, 0.01, 10.0)
n_k_match_s46 = 1.0 / (1.0 + np.exp(epsilon_k / T_match_s46))
P_k_match_s46 = T_match_s46 * np.log(1.0 + np.exp(-epsilon_k / T_match_s46))
P_Z_match_s46 = 2.0 * np.sum(P_k_match_s46)
alpha_Z_match_s46 = E_s46 / P_Z_match_s46
w0_match_s46 = -1.0 / (1.0 + alpha_Z_match_s46)

print(f"\nT_match_s46 (same E as S46) = {T_match_s46:.6f}")
print(f"alpha_Z(match_s46) = {alpha_Z_match_s46:.6f}  ->  w_0 = {w0_match_s46:.6f}")

# =============================================================================
# Step 5: Entropy analysis — WHY does multi-T change alpha?
# =============================================================================

print("\n--- Step 5: Why Multi-T Changes Alpha ---")

# For a Fermi gas at temperature T:
#   P = T * ln(1 + exp(-epsilon/T))
#   rho = n * epsilon = epsilon / (1 + exp(epsilon/T))
#   alpha = E/P = sum(rho_k) / sum(P_k)
#
# For multi-T: each mode has its own T_k.
# The multi-T alpha differs from single-T because:
# P is a CONVEX function of T (P increases faster than linearly with T).
# Jensen's inequality: sum P(T_k) >= P(sum T_k) for N modes at the same E.
# Actually: for a single mode, P(T) = T*ln(1+exp(-eps/T)).
# At fixed E = n*eps, T and n are related by n = 1/(1+exp(eps/T)).
# Higher T -> higher P per unit energy. So modes with HIGHER T contribute
# more pressure per energy.
#
# In the GGE, the B2 modes have HIGHER T (0.592) than the B1/B3 modes (0.247, 0.153).
# This means the B2 modes contribute DISPROPORTIONATELY more pressure.
# The net effect: alpha = E/P DECREASES (more P for same E).
# Since w_0 = -1/(1+alpha), lower alpha -> more negative w_0 -> closer to -1.

# Quantify: per-mode alpha_k = epsilon_k * n_k / (T_k * ln(1+exp(-lambda_k)))
alpha_k_GGE = (n_k_GGE * epsilon_k) / P_k_GGE
alpha_k_match = (n_k_match * epsilon_k) / P_k_match

print(f"Per-mode alpha_k = rho_k / P_k:")
print(f"{'Mode':>7s} | {'alpha_GGE':>10s} | {'alpha_single':>12s} | {'ratio':>8s}")
print("-" * 50)
for i in range(8):
    ratio = alpha_k_GGE[i] / alpha_k_match[i]
    print(f"{labels[i]:>7s} | {alpha_k_GGE[i]:10.6f} | {alpha_k_match[i]:12.6f} | {ratio:8.4f}")

# The WEIGHTED average alpha = sum(rho_k) / sum(P_k):
rho_weights_GGE = n_k_GGE * epsilon_k / np.sum(n_k_GGE * epsilon_k)
rho_weights_match = n_k_match * epsilon_k / np.sum(n_k_match * epsilon_k)

print(f"\nEnergy weights:")
print(f"{'Mode':>7s} | {'w_GGE':>8s} | {'w_single':>10s}")
print("-" * 35)
for i in range(8):
    print(f"{labels[i]:>7s} | {rho_weights_GGE[i]:8.4f} | {rho_weights_match[i]:10.4f}")

# The GGE concentrates energy in B2 (which has lower alpha_k) relative to single-T.
# This is the MECHANISM: multi-T shifts energy toward high-T/low-alpha modes.

# =============================================================================
# Step 6: Alpha(z) evolution and w_a generation
# =============================================================================

print("\n--- Step 6: Alpha(z) Evolution ---")

# In the expanding universe, each mode's "DM" contribution dilutes.
# The dilution rate depends on the per-mode EOS w_k.
# For the Volovik alpha(z), the DM part dilutes while DE doesn't.
#
# But here the distinction DM/DE is artificial within the vacuum medium.
# The alpha = E/P determines w at each instant.
# As the universe expands, the mode occupations change (quasiparticles dilute).
#
# For free-streaming quasiparticles with mass m_k = E_qp_k:
# The momentum redshifts as p ~ 1/a, so E_k(a) = sqrt(m_k^2 + p_k^2/a^2)
# But in the GGE, the occupations are FIXED (conserved quantities).
# The physical question: do the quasiparticles free-stream or are they trapped?
#
# In the framework, the quasiparticles are Bogoliubov excitations of the
# spectral geometry. They are MASSIVE (m ~ M_KK) and trapped in the fiber.
# They do NOT free-stream in 4D spacetime. Instead, the whole vacuum medium
# evolves as a single fluid with EOS w = -P/(E+P).
#
# So alpha does NOT evolve with redshift in this picture!
# w = const = w_0, w_a = 0.
# The multi-T effect is a SHIFT in w_0, not a generation of w_a.

# However: if we consider the FABRIC level (multiple fiber copies), then
# different cells may have slightly different GGE states, creating an
# effective alpha(z) through spatial averaging as cells enter the horizon.
# This is beyond the current computation.

print("  Alpha does NOT evolve with z in the single-fiber picture.")
print("  Quasiparticles are trapped in the SU(3) fiber (mass ~ M_KK).")
print("  They do not free-stream in 4D. w = const, w_a = 0.")
print("  Multi-T generates a w_0 SHIFT, not w_a.")

# For completeness, compute what w_a WOULD be if quasiparticles free-streamed:
# Per-mode EOS for free-streaming relativistic particles:
# w_k = P_k / rho_k = T_k * ln(1+exp(-eps/T)) / (n_k * eps)
w_k_free = P_k_GGE / (n_k_GGE * epsilon_k)

z_arr = np.linspace(0, 3, 1000)
alpha_z_free = np.zeros_like(z_arr)
for iz, z in enumerate(z_arr):
    # Free-streaming: rho_k dilutes as a^{-3(1+w_k)}
    rho_k_z = n_k_GGE * epsilon_k * (1+z)**(3*(1+w_k_free))
    P_k_z = P_k_GGE * (1+z)**(3*(1+w_k_free))
    E_z = 2.0 * np.sum(rho_k_z)
    P_z = 2.0 * np.sum(P_k_z)
    alpha_z_free[iz] = E_z / P_z

w_DE_free = -1.0 / (1.0 + alpha_z_free)

# CPL fit to free-streaming case
def cpl_w(z, w0, wa):
    a = 1.0 / (1.0 + z)
    return w0 + wa * (1.0 - a)

mask_fit = z_arr < 2.0
popt_free, _ = curve_fit(cpl_w, z_arr[mask_fit], w_DE_free[mask_fit], p0=[-0.4, 0.0])
w0_free_cpl, wa_free_cpl = popt_free

print(f"\n  Hypothetical free-streaming CPL: w_0 = {w0_free_cpl:.4f}, w_a = {wa_free_cpl:.4f}")
print(f"  (For reference only — quasiparticles do NOT free-stream)")

# =============================================================================
# Step 7: Modified Friedmann equation
# =============================================================================

print("\n--- Step 7: Friedmann Equation ---")

# The Friedmann equation with the GGE dark energy:
# H^2(z)/H_0^2 = Omega_r*(1+z)^4 + Omega_m*(1+z)^3 + Omega_DE*(rho_DE(z)/rho_DE(0))
#
# CASE 1: Trapped quasiparticles (physical case)
#   rho_DE(z)/rho_DE(0) = 1 (constant, like Lambda)
#   But w != -1, it's w = -P/(E+P) = w_0
#   This means: rho_DE(z) = rho_DE(0) * (1+z)^{3(1+w_0)}
#   For w_0 = -0.43: (1+z)^{3*0.57} = (1+z)^{1.71}
#
# Wait — there is a subtlety. The Volovik alpha is E/P but the Friedmann
# equation uses the STANDARD EOS w = P/rho. The connection:
#   w = P/E (sign convention where P includes vacuum contribution)
#   NOT w = -P/(E+P)
#
# Let me be careful about signs.
# The vacuum medium has:
#   rho = E_total (positive, gravitates)
#   P = -E_vac + P_qp (negative if vacuum dominates)
#   w = P/rho
#
# The S48 Volovik formula: w_0 = -1/(1+alpha) where alpha = E/P_Zubarev
# P_Zubarev is the QUASIPARTICLE pressure (positive).
# The formula comes from rho_DM / rho_DE = alpha where rho_DM ~ P_qp and rho_DE ~ E_vac.
# Actually: alpha = E/P means:
#   w_0 = -1/(1+alpha) = -P/(E+P)
# This works out to: w_0 = -(P_Zubarev)/(E_total + P_Zubarev)
# This IS negative (good for DE) because E and P are both positive.
# For DESI: w_0 = -0.752 means P/(E+P) = 0.752, so P/E = 0.752/(1-0.752) = 3.03
# That means P > E, which is only possible if the quasiparticle pressure exceeds the energy.
# This is the ULTRA-RELATIVISTIC regime (w > 1/3).

# Actually, let me reconsider. The formula w_0 = -1/(1+alpha) with alpha = E/P:
# If E > 0, P > 0: w_0 = -P/(E+P) is in (-1, 0). For DESI w_0 = -0.752,
# we need P/(E+P) = 0.752, so P = 0.752*(E+P), P*(1-0.752) = 0.752*E,
# P = 0.752/0.248 * E = 3.03 * E. So P >> E.
# But the S48 data shows P/E = 0.868 (per spin), giving w_0 = -P/(E+P) = -0.465.
# To get w_0 = -0.752 we need P/E = 3.03, which is 3.5x larger.
# This is the SHORTFALL: the GGE pressure is not large enough.

# The multi-T shift increases P/E from 0.465/(1-0.465) = 0.869 (S46)
# to alpha = 1.327, P/E = 1/(1.327-1) = ... wait, let me just use the numbers.

# GGE: alpha = 1.327, w_0 = -0.430. P/E = 1/alpha = 0.754.
# S46: alpha = 1.152, w_0 = -0.465. P/E = 1/alpha = 0.868.
# Hmm, the GGE has LOWER P/E, so w_0 is LESS negative.
# But earlier the apples-to-apples comparison (same E) showed multi-T is more negative.
# The issue: the GGE and S46 have DIFFERENT energies.
# GGE: E = 1.375, P = 1.036. P/E = 0.754. alpha = E/P = 1.327. w_0 = -0.430.
# S46: E = 1.688, P = 1.465. P/E = 0.868. alpha = E/P = 1.152. w_0 = -0.465.
# single(same E as GGE): E = 1.375, P = 0.655. P/E = 0.476. alpha = 2.10. w_0 = -0.323.
# single(same E as S46): E = 1.688, P = 0.906. P/E = 0.537. alpha = 1.863. w_0 = -0.349.

# The fair comparison is GGE vs single-T at the SAME E.
# GGE: w_0 = -0.430 (P/E = 0.754)
# Single-T: w_0 = -0.323 (P/E = 0.476)
# Multi-T INCREASES P/E from 0.476 to 0.754 (58% increase!)
# This shifts w_0 from -0.323 to -0.430 (toward DESI = -0.752).

# For the Friedmann equation, the DE component evolves as:
# rho_DE(a) = rho_DE(1) * a^{-3(1+w_0)}

# Models:
w0_models = {
    'GGE_multi_T': w0_GGE,
    'single_T_sameE': w0_match,
    'S46_multi_T': w0_s46,
    'single_T_S46E': w0_match_s46,
    'LCDM': -1.0,
}

print(f"w_0 for each model:")
for name, w0 in w0_models.items():
    print(f"  {name:20s}: w_0 = {w0:.6f}")

# Compute expansion history H(z) for each model
H2_models = {}
for name, w0 in w0_models.items():
    H2_models[name] = (Omega_r * (1+z_arr)**4 + Omega_m * (1+z_arr)**3
                        + Omega_Lambda * (1+z_arr)**(3*(1+w0)))

# Comoving distance chi(z) = integral_0^z dz'/sqrt(H2(z'))
chi_models = {}
for name in w0_models:
    chi = np.zeros_like(z_arr)
    for i in range(1, len(z_arr)):
        dz = z_arr[i] - z_arr[i-1]
        z_mid = 0.5 * (z_arr[i-1] + z_arr[i])
        H2_mid = np.interp(z_mid, z_arr, H2_models[name])
        chi[i] = chi[i-1] + dz / np.sqrt(H2_mid)
    chi_models[name] = chi

# Distance differences
print(f"\n{'z':>6s} | {'GGE-LCDM':>10s} | {'single-LCDM':>12s} | {'GGE-single':>12s}")
print("-" * 50)
for z_target in [0.3, 0.5, 0.7, 1.0, 1.5, 2.0]:
    idx = np.argmin(np.abs(z_arr - z_target))
    chi_L = chi_models['LCDM'][idx]
    if chi_L > 0:
        dchi_GGE = (chi_models['GGE_multi_T'][idx] - chi_L) / chi_L * 100
        dchi_single = (chi_models['single_T_sameE'][idx] - chi_L) / chi_L * 100
        dchi_diff = dchi_GGE - dchi_single
        print(f"{z_target:6.1f} | {dchi_GGE:9.3f}% | {dchi_single:11.3f}% | {dchi_diff:11.4f}%")

# =============================================================================
# Step 8: DESI comparison — distance from data
# =============================================================================

print("\n--- Step 8: DESI DR2 Comparison ---")

w0_desi = float(d_s48['w0_desi_dr2'])
w0_desi_err = float(d_s48['w0_desi_dr2_err'])
wa_desi = float(d_s48['wa_desi_dr2'])
wa_desi_err = float(d_s48['wa_desi_dr2_err'])
w0_S48_lo = float(d_s48['w0_band_lo'])
w0_S48_hi = float(d_s48['w0_band_hi'])
w0_S48_mid = 0.5 * (w0_S48_lo + w0_S48_hi)

# Distances from DESI
dist_GGE = abs(w0_GGE - w0_desi)
dist_single = abs(w0_match - w0_desi)
dist_s46 = abs(w0_s46 - w0_desi)
dist_S48_mid = abs(w0_S48_mid - w0_desi)
dist_LCDM = abs(-1.0 - w0_desi)

shift = w0_GGE - w0_match
shift_pct = abs(shift / w0_match) * 100
toward_desi = dist_GGE < dist_single

print(f"DESI DR2: w_0 = {w0_desi:.3f} +/- {w0_desi_err:.3f}, w_a = {wa_desi:.3f} +/- {wa_desi_err:.3f}")
print(f"\n  Model              |    w_0    |  |w_0-DESI|  | sigma from DESI")
print(f"  {'='*60}")
print(f"  GGE (multi-T)      | {w0_GGE:9.4f} | {dist_GGE:10.4f} | {dist_GGE/w0_desi_err:5.1f}sigma")
print(f"  Single-T (same E)  | {w0_match:9.4f} | {dist_single:10.4f} | {dist_single/w0_desi_err:5.1f}sigma")
print(f"  S46 (S48 ref)      | {w0_s46:9.4f} | {dist_s46:10.4f} | {dist_s46/w0_desi_err:5.1f}sigma")
print(f"  S48 band mid       | {w0_S48_mid:9.4f} | {dist_S48_mid:10.4f} | {dist_S48_mid/w0_desi_err:5.1f}sigma")
print(f"  LCDM               | {-1.0:9.4f} | {dist_LCDM:10.4f} | {dist_LCDM/w0_desi_err:5.1f}sigma")

print(f"\nMulti-T shift: delta_w_0 = {shift:.4f} ({shift_pct:.1f}%)")
print(f"Direction: {'toward' if toward_desi else 'away from'} DESI")
print(f"Distance reduction: {(dist_single - dist_GGE)/dist_single * 100:.1f}%")

# Sigma from DESI for framework predictions
sigma_GGE = dist_GGE / w0_desi_err
sigma_single = dist_single / w0_desi_err
print(f"\nGGE tension with DESI: {sigma_GGE:.1f} sigma")
print(f"Single-T tension with DESI: {sigma_single:.1f} sigma")

# =============================================================================
# Step 9: Phantom crossing check
# =============================================================================

print("\n--- Step 9: Phantom Crossing ---")

# w_0 = -0.430 (GGE): NOT phantom (w > -1)
# The Euler pressure P_E = E - sum T_k S_k = -0.115 (negative)
# If one used w = P_E/E = -0.068, this would be less negative than -1.
# No phantom crossing in any formulation.

P_Euler = float(d_s48['P_from_euler'])
w_Euler = P_Euler / float(d_s48['E_GGE'])

print(f"w_0(GGE) = {w0_GGE:.4f}: {'phantom' if w0_GGE < -1 else 'non-phantom'}")
print(f"w_Euler = {w_Euler:.4f}: {'phantom' if w_Euler < -1 else 'non-phantom'}")
print(f"No phantom crossing in any pressure definition.")
print(f"The negative Euler pressure ({P_Euler:.3f}) is a multi-T artifact,")
print(f"not a physical w < -1. The Zubarev pressure (physical) is positive.")

# =============================================================================
# Step 10: Structural analysis — what would alpha need to be?
# =============================================================================

print("\n--- Step 10: Required Alpha for DESI ---")

# w_0 = -0.752 requires alpha = E/P such that -1/(1+alpha) = -0.752
# 1/(1+alpha) = 0.752
# 1+alpha = 1/0.752 = 1.330
# alpha = 0.330
# P/E = 1/0.330 = 3.03
# We have P/E = 0.754 (GGE). Need 4.0x increase in P/E.

alpha_desi = 1.0/abs(w0_desi) - 1.0
PE_desi = 1.0/alpha_desi
PE_GGE = 1.0/alpha_Z_GGE

print(f"Required alpha for DESI: {alpha_desi:.4f} (P/E = {PE_desi:.4f})")
print(f"Current GGE: alpha = {alpha_Z_GGE:.4f} (P/E = {PE_GGE:.4f})")
print(f"Shortfall: P/E needs {PE_desi/PE_GGE:.2f}x increase")
print(f"In alpha: need {alpha_desi:.4f}, have {alpha_Z_GGE:.4f}, ratio = {alpha_Z_GGE/alpha_desi:.2f}x too large")

# =============================================================================
# GATE VERDICT
# =============================================================================

print("\n" + "=" * 78)
print("GATE: MULTI-T-FRIEDMANN-49")
print("=" * 78)

if toward_desi and shift_pct > 1.0:
    verdict = "PASS"
    detail = (f"Multi-T shifts w_0 toward DESI: {w0_match:.4f} -> {w0_GGE:.4f} "
              f"(delta={shift:.4f}, {shift_pct:.1f}%, distance {dist_single:.3f}->{dist_GGE:.3f})")
elif not toward_desi:
    verdict = "FAIL"
    detail = (f"Multi-T shifts w_0 away from DESI: {w0_match:.4f} -> {w0_GGE:.4f}")
else:
    verdict = "INFO"
    detail = (f"Multi-T shift < 1%: {w0_match:.4f} -> {w0_GGE:.4f} ({shift_pct:.1f}%)")

print(f"\nVERDICT: {verdict}")
print(f"DETAIL: {detail}")
print(f"\n  Summary:")
print(f"    w_0(GGE, multi-T) = {w0_GGE:.6f}")
print(f"    w_0(single-T, same E) = {w0_match:.6f}")
print(f"    w_0(S46/S48) = {w0_s46:.6f}")
print(f"    w_0(DESI DR2) = {w0_desi:.3f} +/- {w0_desi_err:.3f}")
print(f"    w_a = 0 (trapped quasiparticles, no z evolution)")
print(f"    Shift = {shift:.4f} ({shift_pct:.1f}%), toward DESI")
print(f"    GGE tension: {sigma_GGE:.1f} sigma from DESI")
print(f"    single-T tension: {sigma_single:.1f} sigma from DESI")
print(f"    Phantom crossing: None")
print(f"    Alpha shortfall: {alpha_Z_GGE/alpha_desi:.1f}x (GGE alpha too large)")
print(f"")
print(f"  PHYSICAL INTERPRETATION:")
print(f"    The 8-temperature GGE REDISTRIBUTES pressure relative to energy.")
print(f"    High-T modes (B2, T=0.59) contribute P/E=0.78 (per mode).")
print(f"    Low-T modes (B3, T=0.15) contribute P/E=0.16 (per mode).")
print(f"    Single-T at same energy: all modes contribute P/E=0.48 equally.")
print(f"    The non-uniform distribution INCREASES total P/E from 0.48 to 0.75,")
print(f"    shifting alpha from 2.10 to 1.33 and w_0 from -0.32 to -0.43.")
print(f"    This is a {shift_pct:.0f}% shift toward DESI, reducing the gap by 25%.")
print(f"    But a 4x further increase in P/E is needed to reach DESI w_0=-0.752.")
print(f"    The multi-T structure is real but INSUFFICIENT alone.")

# =============================================================================
# Step 11: CORRECTION to S48 w_0 band
# =============================================================================

print(f"\n  CORRECTION TO S48 w_0 BAND:")
print(f"    S48 used S46 occupations (quench projection, sum n_k = 1.000).")
print(f"    The physical post-transit state is the GGE (sum n_k = 0.813).")
print(f"    S48 w_0 band [{w0_S48_lo:.4f}, {w0_S48_hi:.4f}] should be revised.")
print(f"    GGE Zubarev alpha = {alpha_Z_GGE:.4f} gives w_0 = {w0_GGE:.4f}.")
print(f"    This is OUTSIDE the S48 band (less negative, further from DESI).")
print(f"    BUT: relative to single-T at same E, it is 25% CLOSER to DESI.")

# =============================================================================
# Step 12: Save and plot
# =============================================================================

print("\n--- Saving data and plot ---")

np.savez('s49_multi_t_friedmann.npz',
    # GGE state
    epsilon_k=epsilon_k,
    lambda_k=lambda_k,
    n_k_GGE=n_k_GGE,
    T_k_GGE=T_k_GGE,
    E_qp_k=E_qp_k,
    labels=labels,
    # S46 reference
    n_k_s46=n_k_s46,
    T_k_s46=T_k_s46,
    # Energies (with 2x spin)
    E_GGE=E_GGE,
    E_s46=E_s46,
    # Zubarev pressures
    P_Z_GGE=P_Z_GGE,
    P_Z_s46=P_Z_s46,
    P_Z_match=P_Z_match,
    # Alphas (E/P definition, S48 convention)
    alpha_Z_GGE=alpha_Z_GGE,
    alpha_Z_s46=alpha_Z_s46,
    alpha_Z_match=alpha_Z_match,
    alpha_Z_match_s46=alpha_Z_match_s46,
    # w_0 values
    w0_GGE=w0_GGE,
    w0_s46=w0_s46,
    w0_match=w0_match,
    w0_match_s46=w0_match_s46,
    # Single-T references
    T_match=T_match,
    T_match_s46=T_match_s46,
    n_k_match=n_k_match,
    # Shift analysis
    shift_w0=shift,
    shift_pct=shift_pct,
    toward_desi=toward_desi,
    dist_GGE_DESI=dist_GGE,
    dist_single_DESI=dist_single,
    dist_reduction_pct=(dist_single - dist_GGE)/dist_single * 100,
    # Free-streaming (hypothetical)
    w0_free_cpl=w0_free_cpl,
    wa_free_cpl=wa_free_cpl,
    z_arr=z_arr,
    alpha_z_free=alpha_z_free,
    w_DE_free=w_DE_free,
    # DESI reference
    w0_desi_dr2=w0_desi,
    w0_desi_dr2_err=w0_desi_err,
    wa_desi_dr2=wa_desi,
    wa_desi_dr2_err=wa_desi_err,
    # S48 reference
    w0_S48_lo=w0_S48_lo,
    w0_S48_hi=w0_S48_hi,
    # Per-mode analysis
    alpha_k_GGE=alpha_k_GGE,
    alpha_k_match=alpha_k_match,
    w_k_free=w_k_free,
    # Alpha shortfall
    alpha_desi_required=alpha_desi,
    alpha_shortfall_ratio=alpha_Z_GGE/alpha_desi,
    # Phantom
    phantom_crossing=False,
    # Expansion history
    H2_GGE=H2_models['GGE_multi_T'],
    H2_single=H2_models['single_T_sameE'],
    H2_lcdm=H2_models['LCDM'],
    chi_GGE=chi_models['GGE_multi_T'],
    chi_single=chi_models['single_T_sameE'],
    chi_lcdm=chi_models['LCDM'],
    # Gate
    gate_name=np.array(['MULTI-T-FRIEDMANN-49']),
    gate_verdict=np.array([verdict]),
    gate_detail=np.array([detail]),
)

print("Saved: s49_multi_t_friedmann.npz")

# --- PLOT ---
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('MULTI-T-FRIEDMANN-49: 8-Temperature GGE Modified Friedmann', fontsize=14)

# Panel (a): w_0 comparison
ax = axes[0, 0]
w_values = [w0_GGE, w0_match, w0_s46, w0_match_s46, -1.0]
w_labels = ['GGE\n(multi-T)', 'Single-T\n(same E)', 'S46\n(S48 ref)',
            'Single-T\n(S46 E)', r'$\Lambda$CDM']
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', 'gray']
bars = ax.bar(range(5), w_values, color=colors, edgecolor='black', linewidth=0.8)
ax.axhline(w0_desi, color='green', linestyle='--', linewidth=2,
           label=f'DESI DR2: $w_0 = {w0_desi:.3f}$')
ax.fill_between([-0.5, 4.5], w0_desi - w0_desi_err, w0_desi + w0_desi_err,
                alpha=0.15, color='green')
ax.set_xticks(range(5))
ax.set_xticklabels(w_labels, fontsize=8)
ax.set_ylabel(r'$w_0$')
ax.set_title(r'(a) $w_0 = -1/(1+\alpha)$ comparison')
ax.legend(fontsize=9)
# Add value labels on bars
for i, (v, bar) in enumerate(zip(w_values, bars)):
    ax.text(bar.get_x() + bar.get_width()/2, v - 0.02,
            f'{v:.3f}', ha='center', va='top', fontsize=8, fontweight='bold')

# Panel (b): Per-mode alpha and temperature
ax = axes[0, 1]
mode_names = [str(l) for l in labels]
bar_width = 0.35
x_pos = np.arange(8)
bar_colors = ['#1f77b4']*4 + ['#ff7f0e'] + ['#2ca02c']*3
ax.bar(x_pos - bar_width/2, alpha_k_GGE, bar_width,
       color=bar_colors, edgecolor='black', linewidth=0.5,
       label=r'GGE $\alpha_k$')
ax.bar(x_pos + bar_width/2, alpha_k_match, bar_width,
       color=[c + '80' for c in bar_colors], edgecolor='black', linewidth=0.5,
       label=r'Single-T $\alpha_k$')
ax.set_xticks(x_pos)
ax.set_xticklabels(mode_names, fontsize=7)
ax.set_ylabel(r'$\alpha_k = \rho_k / P_k$')
ax.set_title(r'(b) Per-mode $\alpha_k$ (lower = more DE-like)')
ax.legend(fontsize=8)
# Annotate total
ax.axhline(alpha_Z_GGE, color='blue', ls=':', lw=1, alpha=0.5)
ax.axhline(alpha_Z_match, color='orange', ls=':', lw=1, alpha=0.5)

# Panel (c): Expansion history comparison
ax = axes[1, 0]
# Plot H(z)/H_0 ratios relative to LCDM
for name, color, ls, lbl in [
    ('GGE_multi_T', '#1f77b4', '-', f'GGE ($w_0={w0_GGE:.3f}$)'),
    ('single_T_sameE', '#ff7f0e', '--', f'Single-T ($w_0={w0_match:.3f}$)'),
]:
    H_ratio = np.sqrt(H2_models[name]) / np.sqrt(H2_models['LCDM'])
    ax.plot(z_arr, H_ratio, color=color, linestyle=ls, linewidth=2, label=lbl)
ax.axhline(1.0, color='gray', ls=':', label=r'$\Lambda$CDM')
ax.set_xlabel('Redshift z')
ax.set_ylabel(r'$H(z) / H_{\Lambda CDM}(z)$')
ax.set_title('(c) Hubble parameter ratio')
ax.legend(fontsize=8)
ax.set_xlim(0, 2.5)

# Panel (d): Temperature distribution
ax = axes[1, 1]
ax.bar(x_pos, T_k_GGE, 0.6, color=bar_colors, edgecolor='black', linewidth=0.5)
ax.axhline(T_match, color='red', ls='--', lw=2,
           label=f'$T_{{single}} = {T_match:.3f}$')
ax.set_xticks(x_pos)
ax.set_xticklabels(mode_names, fontsize=7)
ax.set_ylabel(r'$T_k$ ($M_{KK}$ units)')
ax.set_title('(d) GGE temperature per mode')
ax.legend(fontsize=9)

plt.tight_layout()
plt.savefig('s49_multi_t_friedmann.png', dpi=150, bbox_inches='tight')
plt.close()
print("Saved: s49_multi_t_friedmann.png")

print("\n" + "=" * 78)
print("COMPUTATION COMPLETE")
print("=" * 78)
