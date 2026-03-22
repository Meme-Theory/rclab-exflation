#!/usr/bin/env python3
"""
NS-TILT-42: Primordial Power Spectrum Tilt n_s from Spectral Action Running
============================================================================

Computes the spectral tilt n_s predicted by the framework from the
tau-dependence of the spectral action during the transit through the fold.

In standard single-field inflation:
    n_s - 1 = -2*epsilon - eta
    r = 16*epsilon
    alpha_s = dn_s/d ln k

where epsilon = (1/2)(V'/V)^2/M_Pl^2 and eta = V''/V/M_Pl^2 in slow-roll.

In the phonon-exflation framework, the modulus field IS the internal geometry.
The fabric does not live IN space -- the fabric IS space. The spectral action
S(tau) = Tr|D_K(tau)| encodes the full dynamics. The analog slow-roll
parameters are:

    epsilon_eff = (1/2G_mod) * (d ln S / d tau)^2
    eta_eff     = (1/G_mod) * (d^2 ln S / d tau^2)

where G_mod = 5.0 (DeWitt supermetric on moduli space, Session 40/42 W1-1).

The fabric stiffness Z(tau) modifies this when k-dependence is included:
    epsilon_fabric = epsilon_eff * G_mod / (G_mod + Z * k_pivot^2 / M_KK^2)

Input data:
  - s41_constants_vs_tau.npz: Seeley-DeWitt coefficients a_0, a_2, a_4
  - s42_gradient_stiffness.npz: S_total, dS/dtau, d2S/dtau2, Z(tau)
  - s42_constants_snapshot.npz: M_KK values

Pre-registered gate NS-TILT-42:
  PASS:  n_s in [0.94, 0.98] (within 6 sigma of Planck central value 0.965)
  FAIL:  n_s outside [0.90, 1.00] or n_s = 1.000 exactly (Harrison-Zeldovich)
  DISTINCTIVE: r < 0.001 separates from single-field inflation

Author: Tesla-Resonance (Session 42)
Date: 2026-03-13
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

# ═══════════════════════════════════════════════════════════════════════
# CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════

from canonical_constants import tau_fold as TAU_FOLD

DATA_DIR = Path(__file__).parent
G_DEWITT = 5.0  # DeWitt supermetric normalization (Session 40/42)

# Planck pivot scale
K_PIVOT_MPC = 0.05  # Mpc^{-1}

# Convert k_pivot to GeV using 1 Mpc = 1.563e38 GeV^{-1}
MPC_IN_GEV_INV = 1.563e38
K_PIVOT_GEV = K_PIVOT_MPC / MPC_IN_GEV_INV  # GeV

# Observational targets
NS_PLANCK = 0.9649  # Planck 2018 best fit
NS_SIGMA = 0.0042   # 1 sigma
R_UPPER_BOUND = 0.036  # BICEP/Keck 2021

# Gate thresholds
NS_PASS_LOW = 0.94
NS_PASS_HIGH = 0.98
NS_FAIL_LOW = 0.90
NS_FAIL_HIGH = 1.00


# ═══════════════════════════════════════════════════════════════════════
# LOAD DATA
# ═══════════════════════════════════════════════════════════════════════

print("=" * 90)
print("NS-TILT-42: Primordial Power Spectrum Tilt from Spectral Action Running")
print("=" * 90)

# --- Load S41 Seeley-DeWitt coefficients ---
d41 = np.load(DATA_DIR / 's41_constants_vs_tau.npz', allow_pickle=True)
tau_41 = d41['tau_values']
a0_41 = d41['a0_cutoff0']  # cutoff = 0.01 (primary)
a2_41 = d41['a2_cutoff0']
a4_41 = d41['a4_cutoff0']

print(f"\nS41 data: {len(tau_41)} tau points, range [{tau_41[0]:.3f}, {tau_41[-1]:.3f}]")

# --- Load S42 gradient stiffness (full spectral action S = Tr|D|) ---
dZ = np.load(DATA_DIR / 's42_gradient_stiffness.npz', allow_pickle=True)
tau_Z = dZ['tau_grid']
S_total = dZ['S_total']       # Tr|D_K(tau)| with multiplicities
dS_dtau = dZ['dS_dtau']       # First derivative (finite difference, h=0.0001)
d2S_dtau2 = dZ['d2S_dtau2']   # Second derivative
Z_spectral = dZ['Z_spectral'] # Fabric stiffness = sum mult * sum (dlam/dtau)^2

print(f"S42 stiffness data: {len(tau_Z)} tau points, range [{tau_Z[0]:.3f}, {tau_Z[-1]:.3f}]")

# --- Load M_KK values ---
dC = np.load(DATA_DIR / 's42_constants_snapshot.npz', allow_pickle=True)
M_KK_gravity = float(dC['M_KK_from_GN'])    # 7.43e16 GeV
M_KK_gauge = float(dC['M_KK_kerner'])        # 5.04e17 GeV

print(f"\nM_KK (gravity route):  {M_KK_gravity:.3e} GeV")
print(f"M_KK (gauge route):    {M_KK_gauge:.3e} GeV")
print(f"k_pivot:               {K_PIVOT_GEV:.3e} GeV")
print(f"k_pivot / M_KK_grav:   {K_PIVOT_GEV / M_KK_gravity:.3e}")
print(f"k_pivot / M_KK_gauge:  {K_PIVOT_GEV / M_KK_gauge:.3e}")


# ═══════════════════════════════════════════════════════════════════════
# METHOD 1: SLOW-ROLL FROM Tr|D| (FULL SPECTRAL ACTION)
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "=" * 90)
print("METHOD 1: Slow-Roll Parameters from S(tau) = Tr|D_K(tau)|")
print("=" * 90)
print(f"G_mod = {G_DEWITT} (DeWitt supermetric)")
print()

# Compute effective slow-roll parameters
# epsilon_eff = (1 / 2*G_mod) * (d ln S / d tau)^2
# eta_eff     = (1 / G_mod) * (d^2 ln S / d tau^2)
#
# Note: d ln S / d tau = (1/S) * dS/dtau
#       d^2 ln S / d tau^2 = (1/S) * d2S/dtau2 - (1/S^2) * (dS/dtau)^2

dlnS = dS_dtau / S_total
d2lnS = d2S_dtau2 / S_total - (dS_dtau / S_total)**2

epsilon_eff = (1.0 / (2.0 * G_DEWITT)) * dlnS**2
eta_eff = (1.0 / G_DEWITT) * d2lnS

# n_s = 1 - 2*epsilon - eta  (in slow-roll convention)
ns_M1 = 1.0 - 2.0 * epsilon_eff - eta_eff

# r = 16 * epsilon
r_M1 = 16.0 * epsilon_eff

print(f"{'tau':>6}  {'S(tau)':>12}  {'d ln S':>12}  {'d2 ln S':>12}  "
      f"{'epsilon':>12}  {'eta':>12}  {'n_s':>8}  {'r':>12}")
print("-" * 102)
for i, tau in enumerate(tau_Z):
    marker = " <-- FOLD" if abs(tau - TAU_FOLD) < 1e-6 else ""
    print(f"{tau:6.3f}  {S_total[i]:12.2f}  {dlnS[i]:12.6f}  {d2lnS[i]:12.8f}  "
          f"{epsilon_eff[i]:12.8f}  {eta_eff[i]:12.8f}  {ns_M1[i]:8.6f}  {r_M1[i]:12.8f}{marker}")


# ═══════════════════════════════════════════════════════════════════════
# METHOD 2: SLOW-ROLL FROM a_2(tau) (GRAVITATIONAL SEELEY-DEWITT)
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "=" * 90)
print("METHOD 2: Slow-Roll Parameters from a_2(tau) (Gravitational Action)")
print("=" * 90)
print("a_2 ~ (1/G_N) * integral R * sqrt(g) -- the Einstein-Hilbert term")
print()

# Compute derivatives of a_2(tau) using finite differences on the S41 grid
# Use central differences where possible
def finite_diff_1st(x, y):
    """First derivative by central differences (forward/backward at edges)."""
    dy = np.zeros_like(y)
    for i in range(len(x)):
        if i == 0:
            dy[i] = (y[1] - y[0]) / (x[1] - x[0])
        elif i == len(x) - 1:
            dy[i] = (y[-1] - y[-2]) / (x[-1] - x[-2])
        else:
            dy[i] = (y[i+1] - y[i-1]) / (x[i+1] - x[i-1])
    return dy

def finite_diff_2nd(x, y):
    """Second derivative by central differences."""
    d2y = np.zeros_like(y)
    for i in range(1, len(x) - 1):
        h1 = x[i] - x[i-1]
        h2 = x[i+1] - x[i]
        d2y[i] = 2.0 * (y[i+1] / (h2 * (h1 + h2)) - y[i] / (h1 * h2) + y[i-1] / (h1 * (h1 + h2)))
    # Edges: use one-sided 3-point formula if possible
    if len(x) >= 3:
        h0, h1 = x[1] - x[0], x[2] - x[1]
        d2y[0] = 2.0 * (y[2] / (h1 * (h0 + h1)) - y[1] / (h0 * h1) + y[0] / (h0 * (h0 + h1)))
        hm1, hm2 = x[-1] - x[-2], x[-2] - x[-3]
        d2y[-1] = 2.0 * (y[-1] / (hm1 * (hm1 + hm2)) - y[-2] / (hm1 * hm2) + y[-3] / (hm2 * (hm1 + hm2)))
    return d2y


# --- a_2(tau) derivatives ---
da2 = finite_diff_1st(tau_41, a2_41)
d2a2 = finite_diff_2nd(tau_41, a2_41)

dlnA2 = da2 / a2_41
d2lnA2 = d2a2 / a2_41 - (da2 / a2_41)**2

eps_a2 = (1.0 / (2.0 * G_DEWITT)) * dlnA2**2
eta_a2 = (1.0 / G_DEWITT) * d2lnA2

ns_a2 = 1.0 - 2.0 * eps_a2 - eta_a2
r_a2 = 16.0 * eps_a2

print(f"{'tau':>6}  {'a_2(tau)':>12}  {'d ln a_2':>12}  {'d2 ln a_2':>12}  "
      f"{'epsilon':>12}  {'eta':>12}  {'n_s':>8}  {'r':>12}")
print("-" * 102)
for i, tau in enumerate(tau_41):
    marker = " <-- FOLD" if abs(tau - TAU_FOLD) < 0.005 else ""
    print(f"{tau:6.3f}  {a2_41[i]:12.6f}  {dlnA2[i]:12.6f}  {d2lnA2[i]:12.8f}  "
          f"{eps_a2[i]:12.8f}  {eta_a2[i]:12.8f}  {ns_a2[i]:8.6f}  {r_a2[i]:12.8f}{marker}")


# ═══════════════════════════════════════════════════════════════════════
# METHOD 3: SLOW-ROLL FROM a_4(tau) / a_2(tau) RATIO
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "=" * 90)
print("METHOD 3: Slow-Roll from a_4/a_2 ratio (gauge-to-gravity coupling)")
print("=" * 90)

ratio42 = a4_41 / a2_41
d_ratio = finite_diff_1st(tau_41, ratio42)
d2_ratio = finite_diff_2nd(tau_41, ratio42)

dlnR42 = d_ratio / ratio42
d2lnR42 = d2_ratio / ratio42 - (d_ratio / ratio42)**2

eps_r42 = (1.0 / (2.0 * G_DEWITT)) * dlnR42**2
eta_r42 = (1.0 / G_DEWITT) * d2lnR42

ns_r42 = 1.0 - 2.0 * eps_r42 - eta_r42
r_r42 = 16.0 * eps_r42

print(f"{'tau':>6}  {'a4/a2':>12}  {'d ln(a4/a2)':>14}  {'d2 ln':>12}  "
      f"{'epsilon':>12}  {'eta':>12}  {'n_s':>8}  {'r':>12}")
print("-" * 102)
for i, tau in enumerate(tau_41):
    marker = " <-- FOLD" if abs(tau - TAU_FOLD) < 0.005 else ""
    print(f"{tau:6.3f}  {ratio42[i]:12.8f}  {dlnR42[i]:+14.8f}  {d2lnR42[i]:12.8f}  "
          f"{eps_r42[i]:12.8f}  {eta_r42[i]:12.8f}  {ns_r42[i]:8.6f}  {r_r42[i]:12.8f}{marker}")


# ═══════════════════════════════════════════════════════════════════════
# METHOD 4: FABRIC STIFFNESS CORRECTION (k-dependent)
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "=" * 90)
print("METHOD 4: Fabric Stiffness Correction to epsilon")
print("=" * 90)
print("epsilon_fabric = epsilon_eff * G_mod / (G_mod + Z * (k/M_KK)^2)")
print("The fabric stiffness Z suppresses epsilon at sub-KK scales.")
print()

# k_pivot / M_KK is tiny: ~3.2e-55 / 7.4e16 ~ 4.3e-72 (gravity route)
# This means Z * (k/M_KK)^2 ~ 7.5e4 * (4.3e-72)^2 ~ 1.4e-139
# which is completely negligible compared to G_mod = 5.

# Let's compute this properly for both M_KK routes
for label, M_KK in [("gravity", M_KK_gravity), ("gauge", M_KK_gauge)]:
    k_over_M = K_PIVOT_GEV / M_KK
    print(f"\n--- M_KK = {M_KK:.3e} GeV ({label} route) ---")
    print(f"k_pivot / M_KK = {k_over_M:.3e}")
    print(f"(k_pivot / M_KK)^2 = {k_over_M**2:.3e}")

    fold_idx = np.argmin(np.abs(tau_Z - TAU_FOLD))
    Z_fold = Z_spectral[fold_idx]
    correction = Z_fold * k_over_M**2

    print(f"Z(fold) * (k/M_KK)^2 = {correction:.3e}")
    print(f"G_mod / (G_mod + Z*(k/M_KK)^2) = {G_DEWITT / (G_DEWITT + correction):.15f}")
    print(f"  => Fabric correction is NEGLIGIBLE (ratio = {correction/G_DEWITT:.3e})")

    if label == "gravity":
        # Compute epsilon_fabric at all tau_Z points for gravity route
        eps_fabric = epsilon_eff * G_DEWITT / (G_DEWITT + Z_spectral * k_over_M**2)
        ns_fabric = 1.0 - 2.0 * eps_fabric - eta_eff
        r_fabric = 16.0 * eps_fabric

print("\n** STRUCTURAL FINDING: k_pivot / M_KK ~ 10^{-55}. The fabric stiffness")
print("   correction is identically zero to all computable precision. This is")
print("   because k_pivot (cosmological scales) is 55 orders of magnitude below")
print("   M_KK (compactification scale). The fabric stiffness Z acts on internal")
print("   geometry gradients; at scales >> 1/M_KK, the fabric looks perfectly rigid.")
print("   => epsilon_fabric = epsilon_eff, n_s and r are UNCORRECTED by Z.")


# ═══════════════════════════════════════════════════════════════════════
# RUNNING alpha_s = dn_s / d ln k
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "=" * 90)
print("RUNNING OF SPECTRAL TILT: alpha_s = dn_s / d ln k")
print("=" * 90)

# In slow-roll: alpha_s = -2*xi^2 + 16*epsilon*eta - 24*epsilon^2
# where xi^2 = (V' V''') / V^2 / M_Pl^2
# We compute this from the third derivative of the spectral action.

# For Method 1 (Tr|D|): compute d3 ln S / d tau^3
# We only have 10 points on the tau_Z grid, so use central diff on d2lnS
d3lnS = finite_diff_1st(tau_Z, d2lnS)
xi2_eff = (1.0 / G_DEWITT) * dlnS * d3lnS / G_DEWITT  # analog of V'V'''/V^2

# But we can also just differentiate n_s directly
dns_dtau = finite_diff_1st(tau_Z, ns_M1)

# The running wrt ln k requires a model for how tau maps to ln k.
# In standard slow-roll: d ln k = H dt, and dphi/dt relates phi to k.
# Here: d tau / d ln k ~ tau / N_efolds (roughly).
# But we don't have a specific mapping. Instead, note that the slow-roll
# approximation gives alpha_s directly from the slow-roll parameters.

# Standard slow-roll formula:
alpha_s_sr = 16.0 * epsilon_eff * eta_eff - 24.0 * epsilon_eff**2 - 2.0 * xi2_eff

print(f"\n{'tau':>6}  {'epsilon':>12}  {'eta':>12}  {'xi^2':>12}  "
      f"{'alpha_s (SR)':>14}  {'dn_s/dtau':>12}")
print("-" * 80)
for i, tau in enumerate(tau_Z):
    marker = " <-- FOLD" if abs(tau - TAU_FOLD) < 1e-6 else ""
    print(f"{tau:6.3f}  {epsilon_eff[i]:12.8f}  {eta_eff[i]:12.8f}  {xi2_eff[i]:12.8f}  "
          f"{alpha_s_sr[i]:+14.10f}  {dns_dtau[i]:+12.8f}{marker}")


# ═══════════════════════════════════════════════════════════════════════
# CROSS-CHECK: S_full = a_0 + a_2 + a_4 SLOW-ROLL
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "=" * 90)
print("CROSS-CHECK: S_SD = a_0 + a_2 + a_4 (Seeley-DeWitt expansion)")
print("=" * 90)

S_SD = a0_41 + a2_41 + a4_41
dS_SD = finite_diff_1st(tau_41, S_SD)
d2S_SD = finite_diff_2nd(tau_41, S_SD)

dlnS_SD = dS_SD / S_SD
d2lnS_SD = d2S_SD / S_SD - (dS_SD / S_SD)**2

eps_SD = (1.0 / (2.0 * G_DEWITT)) * dlnS_SD**2
eta_SD = (1.0 / G_DEWITT) * d2lnS_SD

ns_SD = 1.0 - 2.0 * eps_SD - eta_SD
r_SD = 16.0 * eps_SD

print(f"\nNote: S_SD (= a_0+a_2+a_4) DECREASES with tau, while S_full (= Tr|D|) INCREASES.")
print(f"This is because a_0 is constant (mode count), while a_2 ~ sum lam^{-2} and")
print(f"a_4 ~ sum lam^{-4} decrease as eigenvalues grow. The full spectral action")
print(f"S = sum |lam| naturally increases with the eigenvalue scale.\n")

print(f"{'tau':>6}  {'S_SD':>12}  {'d ln S_SD':>12}  {'d2 ln S_SD':>12}  "
      f"{'epsilon':>12}  {'eta':>12}  {'n_s':>8}  {'r':>12}")
print("-" * 102)
for i, tau in enumerate(tau_41):
    marker = " <-- FOLD" if abs(tau - TAU_FOLD) < 0.005 else ""
    print(f"{tau:6.3f}  {S_SD[i]:12.3f}  {dlnS_SD[i]:+12.8f}  {d2lnS_SD[i]:12.8f}  "
          f"{eps_SD[i]:12.8f}  {eta_SD[i]:12.8f}  {ns_SD[i]:8.6f}  {r_SD[i]:12.8f}{marker}")


# ═══════════════════════════════════════════════════════════════════════
# DIAGNOSTIC: WHY epsilon IS SMALL
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "=" * 90)
print("DIAGNOSTIC: WHY epsilon IS SMALL (OR LARGE)")
print("=" * 90)

fold_idx_Z = np.argmin(np.abs(tau_Z - TAU_FOLD))
fold_idx_41 = np.argmin(np.abs(tau_41 - TAU_FOLD))

print(f"\nAt the fold (tau = {TAU_FOLD}):")
print(f"\n  Method 1 (Tr|D|):")
print(f"    S(fold)       = {S_total[fold_idx_Z]:.2f}")
print(f"    dS/dtau(fold) = {dS_dtau[fold_idx_Z]:.2f}")
print(f"    d ln S / dtau = {dlnS[fold_idx_Z]:.8f}")
print(f"    (d ln S)^2    = {dlnS[fold_idx_Z]**2:.10f}")
print(f"    epsilon_eff   = {epsilon_eff[fold_idx_Z]:.10f}")
print(f"    eta_eff       = {eta_eff[fold_idx_Z]:.10f}")
print(f"    => n_s        = {ns_M1[fold_idx_Z]:.8f}")
print(f"    => r          = {r_M1[fold_idx_Z]:.10f}")

print(f"\n  Method 2 (a_2):")
print(f"    a_2(fold)     = {a2_41[fold_idx_41]:.6f}")
print(f"    da_2/dtau     = {da2[fold_idx_41]:.6f}")
print(f"    d ln a_2      = {dlnA2[fold_idx_41]:.8f}")
print(f"    epsilon(a_2)  = {eps_a2[fold_idx_41]:.10f}")
print(f"    eta(a_2)      = {eta_a2[fold_idx_41]:.10f}")
print(f"    => n_s        = {ns_a2[fold_idx_41]:.8f}")
print(f"    => r          = {r_a2[fold_idx_41]:.10f}")

print(f"\n  Cross-check (a_0+a_2+a_4):")
print(f"    S_SD(fold)    = {S_SD[fold_idx_41]:.6f}")
print(f"    d ln S_SD     = {dlnS_SD[fold_idx_41]:.8f}")
print(f"    epsilon(SD)   = {eps_SD[fold_idx_41]:.10f}")
print(f"    eta(SD)       = {eta_SD[fold_idx_41]:.10f}")
print(f"    => n_s        = {ns_SD[fold_idx_41]:.8f}")
print(f"    => r          = {r_SD[fold_idx_41]:.10f}")


# ═══════════════════════════════════════════════════════════════════════
# KEY RESULT: COMPARISON WITH OBSERVATIONS
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "=" * 90)
print("KEY RESULTS: COMPARISON WITH PLANCK 2018")
print("=" * 90)

print(f"\nPlanck 2018: n_s = {NS_PLANCK} +/- {NS_SIGMA}")
print(f"BICEP/Keck 2021: r < {R_UPPER_BOUND}")
print(f"Planck 2018: alpha_s = -0.0045 +/- 0.0067")

# Report n_s at specific tau values
for tau_eval in [0.15, 0.19, 0.20, 0.25]:
    # Method 1 (primary)
    idx_Z = np.argmin(np.abs(tau_Z - tau_eval))
    if abs(tau_Z[idx_Z] - tau_eval) < 0.01:
        n = ns_M1[idx_Z]
        r = r_M1[idx_Z]
        e = epsilon_eff[idx_Z]
        h = eta_eff[idx_Z]
        sigma_from_planck = abs(n - NS_PLANCK) / NS_SIGMA
        print(f"\n  tau = {tau_eval:.3f} (Method 1, Tr|D|):")
        print(f"    n_s = {n:.6f}  ({sigma_from_planck:.1f} sigma from Planck)")
        print(f"    r   = {r:.8f}  ({'BELOW' if r < R_UPPER_BOUND else 'ABOVE'} BICEP bound)")
        print(f"    epsilon = {e:.8f}, eta = {h:.8f}")


# ═══════════════════════════════════════════════════════════════════════
# GATE VERDICT
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "=" * 90)
print("GATE VERDICT: NS-TILT-42")
print("=" * 90)

# Use Method 1 at the fold as the primary result
fold_idx_primary = np.argmin(np.abs(tau_Z - TAU_FOLD))
ns_primary = ns_M1[fold_idx_primary]
r_primary = r_M1[fold_idx_primary]
eps_primary = epsilon_eff[fold_idx_primary]
eta_primary = eta_eff[fold_idx_primary]
alpha_primary = alpha_s_sr[fold_idx_primary]

print(f"\nPrimary result (Method 1, Tr|D|, tau = {TAU_FOLD}):")
print(f"  n_s     = {ns_primary:.8f}")
print(f"  r       = {r_primary:.10f}")
print(f"  alpha_s = {alpha_primary:.10f}")
print(f"  epsilon = {eps_primary:.10f}")
print(f"  eta     = {eta_primary:.10f}")

# Gate classification
sigma_from_planck = abs(ns_primary - NS_PLANCK) / NS_SIGMA
print(f"\n  n_s - 0.965 = {ns_primary - NS_PLANCK:+.6f}")
print(f"  Tension with Planck: {sigma_from_planck:.1f} sigma")

if NS_PASS_LOW <= ns_primary <= NS_PASS_HIGH:
    verdict = "PASS"
    reason = f"n_s = {ns_primary:.6f} is within [{NS_PASS_LOW}, {NS_PASS_HIGH}]"
elif ns_primary < NS_FAIL_LOW or ns_primary > NS_FAIL_HIGH:
    verdict = "FAIL"
    reason = f"n_s = {ns_primary:.6f} is outside [{NS_FAIL_LOW}, {NS_FAIL_HIGH}]"
elif abs(ns_primary - 1.000) < 1e-6:
    verdict = "FAIL"
    reason = f"n_s = {ns_primary:.6f} is Harrison-Zeldovich (ruled out)"
else:
    verdict = "INTERMEDIATE"
    reason = f"n_s = {ns_primary:.6f} is between PASS and FAIL ranges"

print(f"\n  VERDICT: {verdict}")
print(f"  REASON: {reason}")

# Distinctive check
if r_primary < 0.001:
    print(f"\n  DISTINCTIVE: r = {r_primary:.3e} < 0.001")
    print(f"    This is BELOW all planned CMB-S4/LiteBIRD sensitivity.")
    print(f"    Distinguishes framework from single-field inflation (which requires r > 0.001 for n_s ~ 0.965).")
elif r_primary < R_UPPER_BOUND:
    print(f"\n  r = {r_primary:.6f} is BELOW BICEP/Keck bound ({R_UPPER_BOUND})")
    print(f"    Consistent with observations but NOT distinctive from single-field inflation.")
else:
    print(f"\n  r = {r_primary:.6f} EXCEEDS BICEP/Keck bound ({R_UPPER_BOUND}).")
    print(f"    This is a TENSION with observations.")


# ═══════════════════════════════════════════════════════════════════════
# PHYSICAL INTERPRETATION
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "=" * 90)
print("PHYSICAL INTERPRETATION")
print("=" * 90)

print(f"""
The spectral action S(tau) = Tr|D_K(tau)| is the one-parameter deformation of
the Dirac operator's absolute value spectrum, summed with Peter-Weyl
multiplicities. Its tau-dependence encodes how the internal geometry changes
during the transit.

Key finding: d ln S / d tau ~ {dlnS[fold_idx_Z]:.6f} at the fold.

This is a LARGE fractional rate of change. The spectral action changes by
~{dlnS[fold_idx_Z]*100:.2f}% per unit tau. Since the transit covers Delta_tau ~ 0.19,
the total fractional change in S is ~{(S_total[fold_idx_Z] - S_total[0])/S_total[0]*100:.2f}%.

The SIGN of the tilt depends on the sign of eta:
  - eta > 0 => the spectral action is accelerating (d2 ln S > 0) => n_s < 1 (red tilt)
  - eta < 0 => decelerating => n_s > 1 (blue tilt)

Physical picture (resonance interpretation):
  The Jensen deformation stretches eigenvalue spacings nonuniformly. Higher modes
  stretch faster than lower modes (optical branch). The d ln S / d tau measures
  the rate at which the total spectral weight shifts. The d^2 ln S / d tau^2
  measures whether this shift is accelerating or decelerating.

  In acoustic terms: the cavity (SU(3)) is being deformed, and the normal mode
  frequencies are shifting. The tilt measures whether the low-frequency modes
  are compressed or rarefied relative to the high-frequency modes during the
  deformation.

  In superfluid terms: the phonon dispersion curve is being sheared by the
  changing metric. Modes near the roton minimum (the fold in the spectral gap)
  feel the strongest differential shift.

Condensed matter analog:
  This is identical to the Gruneisen parameter gamma = -d ln omega / d ln V
  measuring how phonon frequencies shift under volume change. Here, tau plays
  the role of strain, and the spectral action replaces the phonon free energy.
  The "tilt" is the frequency-dependence of the Gruneisen parameter.
""")


# ═══════════════════════════════════════════════════════════════════════
# SECOND DIAGNOSTIC: ALL METHODS COMPARISON
# ═══════════════════════════════════════════════════════════════════════

print("=" * 90)
print("ALL METHODS COMPARISON AT FOLD")
print("=" * 90)

# Collect results at fold for each method
methods = [
    ("M1: Tr|D| (primary)", ns_M1[fold_idx_Z], r_M1[fold_idx_Z],
     epsilon_eff[fold_idx_Z], eta_eff[fold_idx_Z]),
    ("M2: a_2(tau)", ns_a2[fold_idx_41], r_a2[fold_idx_41],
     eps_a2[fold_idx_41], eta_a2[fold_idx_41]),
    ("M3: a_4/a_2 ratio", ns_r42[fold_idx_41], r_r42[fold_idx_41],
     eps_r42[fold_idx_41], eta_r42[fold_idx_41]),
    ("XC: a_0+a_2+a_4", ns_SD[fold_idx_41], r_SD[fold_idx_41],
     eps_SD[fold_idx_41], eta_SD[fold_idx_41]),
]

print(f"\n{'Method':>25s}  {'n_s':>10s}  {'r':>14s}  {'epsilon':>14s}  {'eta':>14s}")
print("-" * 80)
for name, ns, r, eps, eta in methods:
    print(f"{name:>25s}  {ns:10.6f}  {r:14.8f}  {eps:14.8f}  {eta:14.8f}")

print(f"\nPlanck: n_s = {NS_PLANCK} +/- {NS_SIGMA}")


# ═══════════════════════════════════════════════════════════════════════
# SAVE DATA
# ═══════════════════════════════════════════════════════════════════════

save_dict = {
    # Grid
    'tau_Z': tau_Z,
    'tau_41': tau_41,
    'tau_fold': TAU_FOLD,
    'G_DeWitt': G_DEWITT,
    'M_KK_gravity': M_KK_gravity,
    'M_KK_gauge': M_KK_gauge,
    'k_pivot_GeV': K_PIVOT_GEV,

    # Method 1: Tr|D| (primary)
    'S_total': S_total,
    'dS_dtau': dS_dtau,
    'd2S_dtau2': d2S_dtau2,
    'dlnS': dlnS,
    'd2lnS': d2lnS,
    'epsilon_M1': epsilon_eff,
    'eta_M1': eta_eff,
    'ns_M1': ns_M1,
    'r_M1': r_M1,
    'alpha_s_M1': alpha_s_sr,

    # Method 2: a_2(tau)
    'a2_41': a2_41,
    'epsilon_a2': eps_a2,
    'eta_a2': eta_a2,
    'ns_a2': ns_a2,
    'r_a2': r_a2,

    # Method 3: a_4/a_2
    'ratio_a4_a2': ratio42,
    'epsilon_r42': eps_r42,
    'eta_r42': eta_r42,
    'ns_r42': ns_r42,
    'r_r42': r_r42,

    # Cross-check: a_0+a_2+a_4
    'S_SD': S_SD,
    'epsilon_SD': eps_SD,
    'eta_SD': eta_SD,
    'ns_SD': ns_SD,
    'r_SD': r_SD,

    # Fabric stiffness
    'Z_spectral': Z_spectral,
    'ns_fabric': ns_fabric,
    'r_fabric': r_fabric,

    # Gate
    'ns_primary': np.array([ns_primary]),
    'r_primary': np.array([r_primary]),
    'alpha_s_primary': np.array([alpha_primary]),
    'verdict': np.array([verdict]),
}

np.savez(DATA_DIR / 's42_ns_tilt.npz', **save_dict)
print(f"\nSaved: {DATA_DIR / 's42_ns_tilt.npz'}")


# ═══════════════════════════════════════════════════════════════════════
# PLOTTING
# ═══════════════════════════════════════════════════════════════════════

fig, axes = plt.subplots(2, 3, figsize=(18, 11))
fig.suptitle('NS-TILT-42: Primordial Spectral Tilt from Spectral Action Running',
             fontsize=14, fontweight='bold')

# Panel 1: S(tau) and its derivatives
ax = axes[0, 0]
ax.plot(tau_Z, S_total / 1e3, 'ko-', ms=5, label='$S(\\tau) = \\mathrm{Tr}|D_K|$ ($\\times 10^3$)')
ax.set_xlabel('$\\tau$')
ax.set_ylabel('$S(\\tau)$ ($\\times 10^3$)')
ax2 = ax.twinx()
ax2.plot(tau_Z, dlnS, 'b^-', ms=5, label='$d \\ln S / d\\tau$')
ax2.set_ylabel('$d \\ln S / d\\tau$', color='blue')
ax2.tick_params(axis='y', labelcolor='blue')
ax.axvline(TAU_FOLD, color='gray', ls='--', alpha=0.5, label='fold')
lines1, labels1 = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax.legend(lines1 + lines2, labels1 + labels2, fontsize=7, loc='upper left')
ax.set_title('Spectral action & log-derivative')

# Panel 2: epsilon and eta vs tau
ax = axes[0, 1]
ax.semilogy(tau_Z, epsilon_eff, 'ko-', ms=5, label='$\\epsilon_{\\mathrm{eff}}$')
ax.semilogy(tau_Z, np.abs(eta_eff), 'b^-', ms=5, label='$|\\eta_{\\mathrm{eff}}|$')
ax.axvline(TAU_FOLD, color='gray', ls='--', alpha=0.5)
ax.axhline(0.01, color='red', ls=':', alpha=0.3, label='$\\epsilon = 0.01$ (inflation ends)')
ax.set_xlabel('$\\tau$')
ax.set_ylabel('Slow-roll parameters')
ax.legend(fontsize=8)
ax.set_title('Slow-roll parameters (Method 1)')

# Panel 3: n_s vs tau (all methods)
ax = axes[0, 2]
ax.plot(tau_Z, ns_M1, 'ko-', ms=5, lw=2, label='M1: $\\mathrm{Tr}|D|$')
ax.plot(tau_41, ns_a2, 'b^--', ms=4, label='M2: $a_2(\\tau)$')
ax.plot(tau_41, ns_r42, 'rs--', ms=4, label='M3: $a_4/a_2$')
ax.plot(tau_41, ns_SD, 'gD--', ms=4, label='XC: $a_0+a_2+a_4$')

ax.axhspan(NS_PLANCK - NS_SIGMA, NS_PLANCK + NS_SIGMA, color='gold', alpha=0.3, label='Planck $1\\sigma$')
ax.axhspan(NS_PLANCK - 6*NS_SIGMA, NS_PLANCK + 6*NS_SIGMA, color='gold', alpha=0.1, label='Planck $6\\sigma$')
ax.axhline(NS_PLANCK, color='orange', ls='-', lw=1.5)
ax.axhline(1.0, color='red', ls='--', alpha=0.5, label='HZ ($n_s=1$)')
ax.axhline(NS_PASS_LOW, color='green', ls=':', alpha=0.5)
ax.axhline(NS_PASS_HIGH, color='green', ls=':', alpha=0.5)
ax.axvline(TAU_FOLD, color='gray', ls='--', alpha=0.5)

ax.set_xlabel('$\\tau$')
ax.set_ylabel('$n_s$')
ax.legend(fontsize=7, loc='best')
ax.set_title('Spectral tilt $n_s(\\tau)$')

# Panel 4: r vs tau
ax = axes[1, 0]
ax.semilogy(tau_Z, r_M1, 'ko-', ms=5, lw=2, label='M1: $\\mathrm{Tr}|D|$')
ax.semilogy(tau_41, r_a2, 'b^--', ms=4, label='M2: $a_2(\\tau)$')
ax.semilogy(tau_41, r_r42, 'rs--', ms=4, label='M3: $a_4/a_2$')
ax.axhline(R_UPPER_BOUND, color='red', ls='--', lw=2, label=f'BICEP/Keck ($r < {R_UPPER_BOUND}$)')
ax.axhline(0.001, color='blue', ls=':', lw=1, label='$r = 0.001$ (distinctive)')
ax.axvline(TAU_FOLD, color='gray', ls='--', alpha=0.5)
ax.set_xlabel('$\\tau$')
ax.set_ylabel('$r$ (tensor-to-scalar)')
ax.legend(fontsize=7)
ax.set_title('Tensor-to-scalar ratio $r(\\tau)$')

# Panel 5: n_s - r plane
ax = axes[1, 1]
ax.plot(ns_M1, r_M1, 'ko-', ms=5, lw=2, label='M1: $\\mathrm{Tr}|D|$')
ax.plot(ns_a2, r_a2, 'b^--', ms=4, label='M2: $a_2$')
# Mark the fold point
ax.plot(ns_primary, r_primary, 'r*', ms=15, zorder=5, label=f'Fold ($n_s={ns_primary:.3f}$)')
ax.axvspan(NS_PLANCK - NS_SIGMA, NS_PLANCK + NS_SIGMA, color='gold', alpha=0.3)
ax.axhline(R_UPPER_BOUND, color='red', ls='--', lw=1.5)
ax.axhline(0.001, color='blue', ls=':', lw=1)
ax.set_xlabel('$n_s$')
ax.set_ylabel('$r$')
ax.set_yscale('log')
ax.legend(fontsize=8)
ax.set_title('$n_s$ - $r$ plane')

# Panel 6: alpha_s (running)
ax = axes[1, 2]
ax.plot(tau_Z, alpha_s_sr, 'ko-', ms=5, label='$\\alpha_s$ (slow-roll formula)')
ax.axhline(0, color='gray', ls='-', alpha=0.3)
ax.axhline(-0.0045, color='orange', ls='--', label='Planck central ($-0.0045$)')
ax.axhspan(-0.0045 - 0.0067, -0.0045 + 0.0067, color='gold', alpha=0.2, label='Planck $1\\sigma$')
ax.axvline(TAU_FOLD, color='gray', ls='--', alpha=0.5)
ax.set_xlabel('$\\tau$')
ax.set_ylabel('$\\alpha_s = dn_s / d\\ln k$')
ax.legend(fontsize=7)
ax.set_title('Running of spectral tilt')

plt.tight_layout()
plt.savefig(DATA_DIR / 's42_ns_tilt.png', dpi=150, bbox_inches='tight')
print(f"Saved: {DATA_DIR / 's42_ns_tilt.png'}")


# ═══════════════════════════════════════════════════════════════════════
# FINAL SUMMARY
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "=" * 90)
print("FINAL SUMMARY")
print("=" * 90)

print(f"""
  NS-TILT-42 GATE VERDICT: {verdict}

  Primary result (Method 1: Tr|D_K|, tau = {TAU_FOLD}):
    n_s     = {ns_primary:.8f}
    r       = {r_primary:.10f}
    alpha_s = {alpha_primary:.10f}

  Planck 2018: n_s = {NS_PLANCK} +/- {NS_SIGMA} ({sigma_from_planck:.1f} sigma tension)
  BICEP/Keck:  r < {R_UPPER_BOUND}  ({'consistent' if r_primary < R_UPPER_BOUND else 'TENSION'})

  Method comparison at fold:
    M1 (Tr|D|):    n_s = {ns_M1[fold_idx_Z]:.6f}
    M2 (a_2):      n_s = {ns_a2[fold_idx_41]:.6f}
    M3 (a_4/a_2):  n_s = {ns_r42[fold_idx_41]:.6f}
    XC (a0+a2+a4): n_s = {ns_SD[fold_idx_41]:.6f}

  Fabric stiffness correction: IDENTICALLY ZERO (k_pivot/M_KK ~ 10^{{-55}})
""")
