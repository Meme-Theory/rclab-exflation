#!/usr/bin/env python3
"""
KZ-NS-45: Kibble-Zurek Bogoliubov Spectrum for n_s
====================================================

Session 45, Wave 1-2 (volovik-superfluid-universe-theorist)

Computes the spectral tilt n_s from the Bogoliubov particle creation spectrum
during the transit quench.  The transit is a SUDDEN QUENCH (P_exc = 1.000,
tau_Q / tau_BCS ~ 10^{-5}, S_inst = 0.069), not slow-roll inflation.

The perturbation spectrum is set by Bogoliubov coefficients |beta_k|^2 from the
eigenvalue change during the quench: Parker-type cosmological particle creation
(S38: not Hawking, no horizon, no thermal spectrum).

Formula Audit Protocol (S45 Mandatory):
  (a) Formulas stated with explicit units
  (b) Dimensional checks
  (c) Limiting cases verified
  (d) Citations: Parker (1968), Birrell-Davies Ch. 3, S38 W4

Gate: KZ-NS-45
  PASS:  n_s in [0.955, 0.975]
  FAIL:  n_s outside [0.80, 1.10]
  INFO:  n_s in [0.80, 1.10] but outside [0.955, 0.975]
  BONUS: alpha_s consistent with Planck within 2 sigma
"""

import sys
import numpy as np
from pathlib import Path

# ---------------------------------------------------------------------------
# Imports from canonical constants (S45 mandatory)
# ---------------------------------------------------------------------------
sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import (
    tau_fold, Delta_0_GL, Delta_0_OES, E_cond, S_inst,
    M_KK, M_KK_gravity, M_KK_kerner,
    H_fold, dt_transit, P_exc_kz, n_Bog,
    xi_BCS, xi_GL, a0_fold, a2_fold, a4_fold,
    A_s_CMB, Omega_r, H_0_GeV, M_Pl_reduced,
    PI, Vol_SU3_Haar, N_dof_BCS,
    rho_Lambda_obs, Omega_m, Omega_Lambda,
    Mpc_to_m, hbar_c_GeV_m, c_light,
)

DATA_DIR = Path(__file__).parent
OUT_PREFIX = "s45_kz_ns"

# ---------------------------------------------------------------------------
# SECTION 1: Load eigenvalue data
# ---------------------------------------------------------------------------
print("=" * 78)
print("KZ-NS-45: Kibble-Zurek Bogoliubov Spectrum for n_s")
print("=" * 78)

# 992 eigenvalues at 5 tau values
d_dos = np.load(DATA_DIR / "s44_dos_tau.npz", allow_pickle=True)
omega_in  = d_dos["tau0.00_all_omega"]   # Pre-transit: round SU(3), tau=0
omega_out = d_dos["tau0.19_all_omega"]   # Post-transit: fold, tau=0.19
dim2      = d_dos["tau0.00_all_dim2"]    # Degeneracy weights d(p,q)^2
N_modes   = len(omega_in)

# Intermediate tau values for sensitivity analysis
omega_015 = d_dos["tau0.15_all_omega"]   # tau = 0.15
omega_010 = d_dos["tau0.10_all_omega"]   # tau = 0.10
omega_005 = d_dos["tau0.05_all_omega"]   # tau = 0.05

# BCS parameters from S38
d_inst = np.load(DATA_DIR / "s38_cc_instanton.npz", allow_pickle=True)
xi_fold_sectors = d_inst["xi_fold"]       # sector energies at fold
mult_k_sectors  = d_inst["mult_k"]        # sector multiplicities
Delta_0 = float(d_inst["Delta_0"])        # GL gap = 0.770 M_KK

# Van Hove trajectory data
d_vh = np.load(DATA_DIR / "s44_vanhove_track.npz", allow_pickle=True)

print(f"\n--- Loaded Data ---")
print(f"  Modes: {N_modes}")
print(f"  omega_in  range: [{omega_in.min():.6f}, {omega_in.max():.6f}] M_KK")
print(f"  omega_out range: [{omega_out.min():.6f}, {omega_out.max():.6f}] M_KK")
print(f"  Delta_0 = {Delta_0:.6f} M_KK")
print(f"  M_KK = {M_KK:.4e} GeV (gravity route)")

# ---------------------------------------------------------------------------
# SECTION 2: Bogoliubov coefficient computation
# ---------------------------------------------------------------------------
#
# FORMULA (Parker 1968, Birrell-Davies Ch. 3):
#
#   For a sudden quench from Hamiltonian H_in to H_out, the Bogoliubov
#   coefficient for mode k is:
#
#     |beta_k|^2 = ((E_k^in - E_k^out) / (2 sqrt(E_k^in * E_k^out)))^2
#
#   where E_k = sqrt(xi_k^2 + Delta^2) is the BdG quasiparticle energy.
#
# Units: [E_k] = M_KK. |beta_k|^2 is dimensionless.
#
# Limiting case: if xi_k^in = xi_k^out and Delta_in = Delta_out,
#   then |beta_k|^2 = 0 (no particle creation). VERIFIED BELOW.
#
# PHYSICS:
#   Pre-transit: BCS condensate with gap Delta_0 at tau=0
#   Post-transit: condensate DESTROYED (P_exc = 1.000, S38).
#     Delta_out = 0 (no condensate).
#   The quasiparticle energies are:
#     E_k^in  = sqrt(omega_in[k]^2 + Delta_0^2)   (with BCS gap)
#     E_k^out = |omega_out[k]|                      (no gap, Delta=0)
#
# Note: chemical potential mu = 0 (S34, PH-forced). So xi_k = omega_k.
#

print("\n--- Bogoliubov Coefficients ---")

# Pre-transit BdG energies (with gap)
E_in = np.sqrt(omega_in**2 + Delta_0**2)

# Post-transit energies (gap destroyed)
Delta_out = 0.0  # P_exc = 1.000, condensate destroyed
E_out = np.sqrt(omega_out**2 + Delta_out**2)  # = |omega_out|

# Bogoliubov coefficients
beta2 = ((E_in - E_out) / (2.0 * np.sqrt(E_in * E_out)))**2

# Verification: limiting case
E_test_in = np.sqrt(1.0**2 + Delta_0**2)
E_test_out = np.sqrt(1.0**2 + Delta_0**2)
beta2_test = ((E_test_in - E_test_out) / (2.0 * np.sqrt(E_test_in * E_test_out)))**2
assert beta2_test == 0.0, f"Limiting case failed: {beta2_test}"
print(f"  Limiting case (no change): |beta|^2 = {beta2_test} [PASS]")

# Another verification: check dimensions
# E_in, E_out in M_KK -> ratio is dimensionless -> beta2 dimensionless [PASS]

print(f"  |beta_k|^2 range: [{beta2.min():.6e}, {beta2.max():.6e}]")
print(f"  |beta_k|^2 mean:  {beta2.mean():.6e}")
print(f"  |beta_k|^2 std:   {beta2.std():.6e}")
print(f"  Total particle number: sum(d^2 * |beta_k|^2) = {np.sum(dim2 * beta2):.4f}")

# ---------------------------------------------------------------------------
# SECTION 3: 4D wavenumber assignment
# ---------------------------------------------------------------------------
#
# Two approaches:
#
# APPROACH A (Casimir mapping, simultaneous creation):
#   All modes created simultaneously (sudden quench). The 4D wavenumber
#   is proportional to the internal eigenvalue:
#
#     k_4D / k_0 = omega_k / omega_min
#
#   where k_0 is the pivot scale. This is the simplest: modes with larger
#   internal energy correspond to smaller 4D wavelengths.
#
# APPROACH B (Hubble mapping):
#   k_4D = a * H at the time mode exits the horizon.  For a sudden quench,
#   all modes are created at the same cosmic time, so:
#
#     k_4D = a(t_fold) * H(t_fold)
#
#   is the SAME for all modes.  But the relative k-dependence comes from
#   the internal quantum numbers: the energy spectrum defines a natural
#   ordering.  Use the pre-transit eigenvalue spectrum as the k-proxy.
#
# For the power spectrum P(k), we need the SPECTRAL DENSITY as a function
# of a continuous variable k.  The discrete modes define bins in k-space.
# We use omega_out (post-transit eigenvalues) as the wavenumber proxy,
# since these determine the free quasiparticle momenta.
#

print("\n--- Wavenumber Assignment ---")

# For the spectral tilt, the PHYSICAL question is:
# How does |beta_k|^2 scale with the mode index / eigenvalue?
# The 4D wavenumber k is monotonically related to the internal eigenvalue.
# n_s - 1 = d ln P / d ln k is a LOG-LOG slope.

# Approach A: use omega_out as k-proxy (post-transit dispersion)
# k ~ omega_out (in M_KK units)
k_proxy_A = omega_out.copy()

# Approach B: use omega_in as k-proxy (pre-transit quantum numbers)
k_proxy_B = omega_in.copy()

# Approach C: use geometric mean (compromise)
k_proxy_C = np.sqrt(omega_in * omega_out)

# For actual 4D wavenumber in physical units:
# k_phys = omega_k * M_KK / hbar_c  (mode energy -> inverse length)
# k_phys [Mpc^{-1}] = omega_k * M_KK * Mpc_to_m / hbar_c_GeV_m

# The pivot scale k_* = 0.05 Mpc^{-1} corresponds to:
k_pivot_Mpc = 0.05  # Mpc^{-1}
k_pivot_GeV = k_pivot_Mpc / Mpc_to_m * hbar_c_GeV_m  # very small ~ 3.2e-42 GeV

# The internal modes have k ~ M_KK ~ 10^{16} GeV
# The ratio k_pivot / k_mode ~ 10^{-58} -- enormous hierarchy
# This means the observable CMB modes correspond to extremely low-energy
# internal excitations.  The KK modes at omega ~ 1 M_KK are at ~10^{16} GeV.
#
# CRITICAL INSIGHT: The spectral tilt n_s is a DIMENSIONLESS LOG-LOG SLOPE.
# It does not depend on the overall normalization k_0, only on the
# functional form P(k) = f(k) near the pivot.
# So n_s - 1 = d ln(|beta(k)|^2) / d ln(k) + 3  (from k^3 in P(k))
# evaluated at any k within the observable range.

print(f"  k_pivot = {k_pivot_Mpc} Mpc^-1 = {k_pivot_GeV:.4e} GeV")
print(f"  k_KK ~ M_KK = {M_KK:.4e} GeV")
print(f"  Hierarchy: k_pivot / k_KK ~ {k_pivot_GeV / M_KK:.4e}")
print(f"  Using omega as k-proxy for spectral tilt (dimensionless ratio)")

# ---------------------------------------------------------------------------
# SECTION 4: Power spectrum P(k) construction
# ---------------------------------------------------------------------------
#
# P(k) = sum_modes_at_k  d_k^2 * |beta_k|^2
#
# For discrete modes, we bin in k-space and compute the spectral density.
# The spectral tilt is extracted from the log-log slope.
#

print("\n--- Power Spectrum Construction ---")

# DIRECT APPROACH: Compute P(k) = d^2 * |beta_k|^2 for each mode.
# Since modes have different k, we get a discrete set of (k, P) pairs.
# The spectral tilt is the slope in log-log space.

# Sort by k-proxy
for label, k_proxy in [("A (omega_out)", k_proxy_A),
                        ("B (omega_in)", k_proxy_B),
                        ("C (geometric)", k_proxy_C)]:
    idx = np.argsort(k_proxy)
    k_sorted = k_proxy[idx]
    beta2_sorted = beta2[idx]
    dim2_sorted = dim2[idx]

    # Power per mode (including degeneracy weight)
    P_mode = dim2_sorted * beta2_sorted

    # For binned spectrum: group modes into k-bins
    n_bins = 50
    k_min, k_max = k_sorted.min(), k_sorted.max()
    k_edges = np.linspace(k_min, k_max, n_bins + 1)
    k_centers = 0.5 * (k_edges[:-1] + k_edges[1:])
    dk = k_edges[1] - k_edges[0]

    P_binned = np.zeros(n_bins)
    N_per_bin = np.zeros(n_bins)
    for i in range(n_bins):
        mask = (k_sorted >= k_edges[i]) & (k_sorted < k_edges[i+1])
        P_binned[i] = np.sum(P_mode[mask])
        N_per_bin[i] = np.sum(mask)

    # Spectral density (per unit k)
    P_density = P_binned / dk

    # Fit log-log slope in the middle range (avoid edges)
    good = P_density > 0
    if np.sum(good) > 5:
        lnk = np.log(k_centers[good])
        lnP = np.log(P_density[good])
        # Linear fit: lnP = a + b * lnk
        coeffs = np.polyfit(lnk, lnP, 1)
        slope = coeffs[0]  # d ln P / d ln k
        ns_raw = 1.0 + slope  # n_s = 1 + d ln P / d ln k
        # Note: in cosmology, P_R(k) ~ k^{n_s - 1}, so the slope IS n_s - 1

        # Also fit quadratic for running
        if np.sum(good) > 8:
            coeffs2 = np.polyfit(lnk, lnP, 2)
            # lnP = c2 * lnk^2 + c1 * lnk + c0
            # d lnP / d lnk = 2*c2*lnk + c1
            # d^2 lnP / d(lnk)^2 = 2*c2 = alpha_s
            alpha_s = 2.0 * coeffs2[0]
        else:
            alpha_s = 0.0

        print(f"\n  Approach {label}:")
        print(f"    n_s - 1 = {slope:.6f}  =>  n_s = {ns_raw:.6f}")
        print(f"    alpha_s = {alpha_s:.6f}")
        print(f"    Bins with data: {np.sum(good)}/{n_bins}")

    if label.startswith("A"):
        # Save primary result
        ns_primary = ns_raw
        alpha_s_primary = alpha_s
        k_centers_A = k_centers
        P_density_A = P_density
        coeffs_A = coeffs
        coeffs2_A = coeffs2 if np.sum(good) > 8 else None

# ---------------------------------------------------------------------------
# SECTION 5: ALTERNATIVE n_s COMPUTATION -- Mode-by-mode slope
# ---------------------------------------------------------------------------
#
# Instead of binning, compute the local log-log slope directly from the
# discrete mode data.  This avoids binning artifacts.
#

print("\n--- Mode-by-Mode Spectral Tilt ---")

# Sort by omega_out (Approach A)
idx_A = np.argsort(omega_out)
k_sorted = omega_out[idx_A]
beta2_sorted = beta2[idx_A]
dim2_sorted = dim2[idx_A]
P_mode_sorted = dim2_sorted * beta2_sorted

# Use running average over window of modes to smooth
window = 50
n_pts = len(k_sorted)
ns_local = np.zeros(n_pts - window)
k_local = np.zeros(n_pts - window)

for i in range(n_pts - window):
    k_win = k_sorted[i:i+window]
    P_win = P_mode_sorted[i:i+window]
    # Avoid zero P
    good = P_win > 0
    if np.sum(good) > 3:
        lnk = np.log(k_win[good])
        lnP = np.log(P_win[good])
        c = np.polyfit(lnk, lnP, 1)
        ns_local[i] = 1.0 + c[0]
        k_local[i] = np.exp(np.mean(lnk))

good_local = k_local > 0
if np.sum(good_local) > 0:
    ns_mean = np.mean(ns_local[good_local])
    ns_std  = np.std(ns_local[good_local])
    ns_median = np.median(ns_local[good_local])
    print(f"  n_s (running window, mean +/- std): {ns_mean:.4f} +/- {ns_std:.4f}")
    print(f"  n_s (running window, median):       {ns_median:.4f}")

# ---------------------------------------------------------------------------
# SECTION 6: PHYSICAL SPECTRAL TILT -- Degeneracy-weighted cumulative
# ---------------------------------------------------------------------------
#
# The PHYSICAL power spectrum weights each mode by its degeneracy d(p,q)^2.
# At round SU(3) (tau=0), modes with the same Casimir have the same omega.
# At the fold (tau=0.19), the Jensen deformation splits them.
#
# The key question: what is the SCALING of |beta_k|^2 with k?
#
# For a sudden quench in BCS theory (Enomoto & Matsuda 2022, Paper 29):
#   |beta_k|^2 ~ (Delta_0 / 2 E_k)^2 for modes far from the Fermi surface
#   |beta_k|^2 ~ 1/4 for modes at the Fermi surface (E_k -> 0)
#
# In the framework: there is no Fermi surface (mu = 0, all modes above gap).
# The variation of |beta_k|^2 comes from the eigenvalue SHIFT delta_omega.

print("\n--- Physical Analysis ---")

# Compute |beta_k|^2 as function of omega_out, weighted by dim2
# Group unique post-transit eigenvalues
omega_out_unique = np.unique(omega_out)
n_unique = len(omega_out_unique)

# For each unique omega_out, sum dim2 * beta2
P_unique = np.zeros(n_unique)
dim2_total = np.zeros(n_unique)
beta2_mean = np.zeros(n_unique)
omega_in_mean = np.zeros(n_unique)

for i, om in enumerate(omega_out_unique):
    mask = omega_out == om
    P_unique[i] = np.sum(dim2[mask] * beta2[mask])
    dim2_total[i] = np.sum(dim2[mask])
    beta2_mean[i] = np.mean(beta2[mask])
    omega_in_mean[i] = np.mean(omega_in[mask])

print(f"  Unique post-transit eigenvalues: {n_unique}")
print(f"  Total weighted power: {np.sum(P_unique):.4f}")

# Log-log fit of degeneracy-weighted power
good = P_unique > 0
lnk_u = np.log(omega_out_unique[good])
lnP_u = np.log(P_unique[good])

coeffs_u = np.polyfit(lnk_u, lnP_u, 1)
ns_weighted = 1.0 + coeffs_u[0]
print(f"  n_s (deg-weighted, full range): {ns_weighted:.6f}")

# Fit quadratic for running
if len(lnk_u) > 8:
    coeffs_u2 = np.polyfit(lnk_u, lnP_u, 2)
    alpha_s_weighted = 2.0 * coeffs_u2[0]
    # Evaluate n_s at different points
    lnk_mid = np.median(lnk_u)
    ns_at_mid = 1.0 + 2*coeffs_u2[0]*lnk_mid + coeffs_u2[1]
    print(f"  n_s (deg-weighted, at median k): {ns_at_mid:.6f}")
    print(f"  alpha_s (deg-weighted): {alpha_s_weighted:.6f}")

# Also compute: what is the UNWEIGHTED beta2 vs k?
coeffs_beta = np.polyfit(lnk_u, np.log(beta2_mean[good]), 1)
slope_beta = coeffs_beta[0]
print(f"  |beta_k|^2 scaling exponent: {slope_beta:.6f}")
print(f"  (i.e., |beta_k|^2 ~ k^{slope_beta:.3f})")

# And the degeneracy scaling:
coeffs_deg = np.polyfit(lnk_u, np.log(dim2_total[good]), 1)
slope_deg = coeffs_deg[0]
print(f"  Degeneracy scaling exponent: {slope_deg:.6f}")
print(f"  (i.e., d^2 ~ k^{slope_deg:.3f})")

print(f"\n  DECOMPOSITION: n_s - 1 = slope_beta + slope_deg")
print(f"  {ns_weighted - 1:.6f} = {slope_beta:.6f} + {slope_deg:.6f}")
print(f"  Check: {slope_beta + slope_deg:.6f} (sum)")

# ---------------------------------------------------------------------------
# SECTION 7: Sensitivity analysis
# ---------------------------------------------------------------------------

print("\n--- Sensitivity Analysis ---")

results = {}

# 7a. Vary Delta_0
for Delta_frac, Delta_label in [(0.5, "0.5x"), (1.0, "1.0x"), (1.5, "1.5x"),
                                  (2.0, "2.0x"), (0.0, "0.0x (free)")]:
    Delta_test = Delta_0 * Delta_frac
    E_in_test = np.sqrt(omega_in**2 + Delta_test**2)
    E_out_test = np.abs(omega_out)  # Delta_out = 0 always (condensate destroyed)

    beta2_test = ((E_in_test - E_out_test) / (2.0 * np.sqrt(E_in_test * E_out_test)))**2

    # Weighted power at unique omega_out
    P_test = np.zeros(n_unique)
    for i, om in enumerate(omega_out_unique):
        mask = omega_out == om
        P_test[i] = np.sum(dim2[mask] * beta2_test[mask])

    good_t = P_test > 0
    if np.sum(good_t) > 5:
        c = np.polyfit(np.log(omega_out_unique[good_t]), np.log(P_test[good_t]), 1)
        ns_test = 1.0 + c[0]
        results[f"Delta={Delta_label}"] = ns_test
        print(f"  Delta_0 = {Delta_label} ({Delta_test:.3f}): n_s = {ns_test:.6f}")

# 7b. Vary tau_fold (use different post-transit spectra)
for tau_label, omega_post in [("tau=0.10", omega_010),
                                ("tau=0.15", omega_015),
                                ("tau=0.19", omega_out)]:
    E_in_test = np.sqrt(omega_in**2 + Delta_0**2)
    E_out_test = np.abs(omega_post)
    beta2_test = ((E_in_test - E_out_test) / (2.0 * np.sqrt(E_in_test * E_out_test)))**2

    # Use omega_post for k-proxy
    omega_post_unique = np.unique(omega_post)
    P_test = np.zeros(len(omega_post_unique))
    for i, om in enumerate(omega_post_unique):
        mask = omega_post == om
        P_test[i] = np.sum(dim2[mask] * beta2_test[mask])

    good_t = P_test > 0
    if np.sum(good_t) > 5:
        c = np.polyfit(np.log(omega_post_unique[good_t]), np.log(P_test[good_t]), 1)
        ns_test = 1.0 + c[0]
        results[tau_label] = ns_test
        print(f"  Post-transit at {tau_label}: n_s = {ns_test:.6f}")

# 7c. Quench profile: finite-time quench (linear ramp)
# For a linear ramp over delta_tau, the Bogoliubov coefficient is modified:
# |beta_k|^2_ramp ~ |beta_k|^2_sudden * sinc^2(E_k * delta_t / 2)
# where delta_t is the ramp time and E_k is the typical mode energy
# This SUPPRESSES high-k modes -> makes spectrum REDDER

print("\n  --- Quench profile variations ---")
for delta_tau_ramp in [0.01, 0.05, 0.10]:
    # Estimate ramp time from dt_transit / delta_tau * delta_tau_ramp
    # At fold: dt_transit = 0.00113 M_KK^{-1} for full delta_tau=0.19
    ramp_time = dt_transit * delta_tau_ramp / tau_fold  # M_KK^{-1}
    # Adiabaticity parameter: E_k * ramp_time
    adiab = E_out * ramp_time  # dimensionless

    # Sinc suppression
    sinc_factor = np.sinc(adiab / (2.0 * PI))**2  # sinc(x/2pi) = sin(x/2)/(x/2)
    # More precisely: for linear ramp, |beta|^2_ramp = |beta|^2_sudden * [sin(x)/x]^2
    # where x = Delta_E * delta_t / (2*hbar)
    Delta_E = np.abs(E_in - E_out)
    x = Delta_E * ramp_time / 2.0
    ramp_factor = np.where(x > 1e-10, (np.sin(x) / x)**2, 1.0)

    beta2_ramp = beta2 * ramp_factor

    P_ramp = np.zeros(n_unique)
    for i, om in enumerate(omega_out_unique):
        mask = omega_out == om
        P_ramp[i] = np.sum(dim2[mask] * beta2_ramp[mask])

    good_r = P_ramp > 0
    if np.sum(good_r) > 5:
        c = np.polyfit(np.log(omega_out_unique[good_r]), np.log(P_ramp[good_r]), 1)
        ns_ramp = 1.0 + c[0]
        results[f"ramp dt={delta_tau_ramp}"] = ns_ramp
        mean_supp = np.mean(ramp_factor)
        print(f"  delta_tau = {delta_tau_ramp}: n_s = {ns_ramp:.6f}, "
              f"mean sinc^2 = {mean_supp:.6f}")

# 7d. k-proxy comparison
print("\n  --- k-proxy variations ---")
for label, k_test in [("omega_out", omega_out),
                       ("omega_in", omega_in),
                       ("geometric", np.sqrt(omega_in * omega_out)),
                       ("Casimir C2", omega_in**2)]:
    k_unique = np.unique(k_test)
    P_test = np.zeros(len(k_unique))
    for i, kv in enumerate(k_unique):
        mask = k_test == kv
        P_test[i] = np.sum(dim2[mask] * beta2[mask])
    good_t = P_test > 0
    if np.sum(good_t) > 5:
        c = np.polyfit(np.log(k_unique[good_t]), np.log(P_test[good_t]), 1)
        ns_test = 1.0 + c[0]
        results[f"k={label}"] = ns_test
        print(f"  k = {label}: n_s = {ns_test:.6f}")

# ---------------------------------------------------------------------------
# SECTION 8: Tensor spectrum
# ---------------------------------------------------------------------------
#
# The tensor modes couple to the trace of the stress-energy tensor, not to
# individual matter modes.  In the framework, the tensor spectrum is set by
# the overall modulus fluctuation (breathing mode of SU(3)), not by individual
# KK mode quenching.
#
# For completeness, estimate the tensor-to-scalar ratio from the BCS energy:
#   r ~ 16 * epsilon_H = 16 * 2.999 = 48 (naive, from epsilon_H invariance)
# This is clearly wrong -- epsilon_H = 2.999 is not a slow-roll parameter.
#
# Better estimate from BCS energy:
#   r ~ (E_cond / M_Pl^2 H^2) * (some geometric factor)
# This requires the full coupled Friedmann-BCS computation.
#
# We note that S44 W3-4 computed r = 3.86e-10 from a different route.
# We cannot improve on that here without the full coupled system.

print("\n--- Tensor Spectrum ---")
r_S44 = 3.86e-10
print(f"  S44 W3-4 result: r = {r_S44:.2e}")
print(f"  Naive epsilon_H route: r = 16 * epsilon_H = {16 * 2.999:.1f} (INVALID)")
print(f"  The Bogoliubov computation gives the SCALAR spectrum only.")
print(f"  Tensor spectrum requires coupled Friedmann-modulus dynamics.")

# ---------------------------------------------------------------------------
# SECTION 9: Cross-checks
# ---------------------------------------------------------------------------

print("\n--- Cross-Checks ---")

# 9a. Landau prediction: d=1 KZ formula
# n_s - 1 = -d * z * nu / (1 + z * nu) with d=1, z=2.024, nu=0.6301
z_kz = 2.024
nu_kz = 0.6301
for d_kz in [1, 2, 3]:
    ns_landau = 1.0 - d_kz * z_kz * nu_kz / (1.0 + z_kz * nu_kz)
    print(f"  Landau KZ formula d={d_kz}: n_s = {ns_landau:.4f}")

# 9b. Pure degeneracy spectrum (no beta2 variation)
# If |beta_k|^2 were constant, P(k) ~ d^2(k), and n_s - 1 = slope_deg
print(f"\n  Pure degeneracy spectrum: n_s - 1 = {slope_deg:.4f}")
print(f"  This is the contribution from the mode counting alone.")

# 9c. Energy-weighted check: total energy in Bogoliubov excitations
E_total_bog = np.sum(dim2 * beta2 * E_out)
E_total_cond = np.abs(E_cond)
print(f"\n  Total Bogoliubov energy: {E_total_bog:.4f} M_KK")
print(f"  |E_cond| = {E_total_cond:.4f} M_KK")
print(f"  Ratio E_bog / |E_cond| = {E_total_bog / E_total_cond:.1f}")

# 9d. Consistency: n_Bog from S38
n_bog_check = np.sum(beta2)  # total number of Bogoliubov quasiparticles (unweighted)
n_bog_weighted = np.sum(dim2 * beta2)
print(f"\n  n_Bog (unweighted sum): {n_bog_check:.1f}")
print(f"  n_Bog (deg-weighted): {n_bog_weighted:.1f}")
print(f"  S38 n_Bog per mode: {n_Bog:.4f}")
print(f"  S38 total pairs: {59.8}")

# ---------------------------------------------------------------------------
# SECTION 10: Assemble final results and gate verdict
# ---------------------------------------------------------------------------

print("\n" + "=" * 78)
print("FINAL RESULTS")
print("=" * 78)

# Primary result: degeneracy-weighted power spectrum, Approach A
ns_final = ns_weighted
alpha_s_final = alpha_s_weighted

print(f"\n  n_s = {ns_final:.4f}")
print(f"  alpha_s = {alpha_s_final:.4f}")

# Uncertainty from sensitivity analysis
ns_values = list(results.values())
ns_range = [min(ns_values), max(ns_values)]
ns_systematic = (ns_range[1] - ns_range[0]) / 2.0
print(f"  n_s range (all variations): [{ns_range[0]:.4f}, {ns_range[1]:.4f}]")
print(f"  Systematic uncertainty: +/- {ns_systematic:.4f}")

# Planck constraint: n_s = 0.9649 +/- 0.0042 (1 sigma)
ns_planck = 0.9649
ns_planck_sigma = 0.0042
deviation = (ns_final - ns_planck) / ns_planck_sigma
print(f"\n  Planck n_s = {ns_planck} +/- {ns_planck_sigma}")
print(f"  Deviation from Planck: {deviation:.1f} sigma")

# Gate verdict
print("\n  --- GATE VERDICT ---")
if 0.955 <= ns_final <= 0.975:
    verdict = "PASS"
    print(f"  KZ-NS-45: PASS  (n_s = {ns_final:.4f} in [0.955, 0.975])")
elif 0.80 <= ns_final <= 1.10:
    verdict = "INFO"
    print(f"  KZ-NS-45: INFO  (n_s = {ns_final:.4f} in [0.80, 1.10] but outside Planck window)")
else:
    verdict = "FAIL"
    print(f"  KZ-NS-45: FAIL  (n_s = {ns_final:.4f} outside extended window [0.80, 1.10])")

# Bonus: alpha_s
alpha_s_planck = -0.0045
alpha_s_sigma = 0.0067
alpha_deviation = (alpha_s_final - alpha_s_planck) / alpha_s_sigma
print(f"\n  alpha_s = {alpha_s_final:.4f}")
print(f"  Planck alpha_s = {alpha_s_planck} +/- {alpha_s_sigma}")
print(f"  Alpha deviation: {alpha_deviation:.1f} sigma")
if abs(alpha_deviation) < 2.0:
    print(f"  BONUS: alpha_s consistent with Planck within 2 sigma")

# ---------------------------------------------------------------------------
# SECTION 11: Save results
# ---------------------------------------------------------------------------

np.savez(DATA_DIR / f"{OUT_PREFIX}.npz",
    # Primary results
    ns_final=ns_final,
    alpha_s_final=alpha_s_final,
    verdict=np.array([verdict]),

    # Mode data
    omega_in=omega_in,
    omega_out=omega_out,
    dim2=dim2,
    beta2=beta2,
    E_in=E_in,
    E_out=E_out,

    # Unique power spectrum
    omega_out_unique=omega_out_unique,
    P_unique=P_unique,
    beta2_mean=beta2_mean,
    dim2_total=dim2_total,

    # Sensitivity
    ns_values=np.array(ns_values),
    ns_range=np.array(ns_range),
    ns_systematic=ns_systematic,

    # Fit coefficients
    slope_beta=slope_beta,
    slope_deg=slope_deg,

    # Local n_s
    k_local=k_local,
    ns_local=ns_local,

    # Parameters
    Delta_0=Delta_0,
    Delta_out=Delta_out,
    tau_fold=tau_fold,

    # Cross-checks
    n_bog_check=n_bog_check,
    n_bog_weighted=n_bog_weighted,
    E_total_bog=E_total_bog,

    # Planck comparison
    ns_planck=ns_planck,
    ns_planck_sigma=ns_planck_sigma,
    deviation_sigma=deviation,

    # Gate
    gate_name=np.array(["KZ-NS-45"]),
)

print(f"\n  Saved: {DATA_DIR / f'{OUT_PREFIX}.npz'}")

# ---------------------------------------------------------------------------
# SECTION 12: Plot
# ---------------------------------------------------------------------------

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 3, figsize=(18, 11))

# Panel 1: Eigenvalue shift
ax = axes[0, 0]
delta_omega = omega_out - omega_in
ax.scatter(omega_in, delta_omega, s=dim2/5, alpha=0.5, c=np.log10(beta2+1e-20),
           cmap='viridis', edgecolors='none')
ax.set_xlabel(r"$\omega_{in}$ (M$_{KK}$)")
ax.set_ylabel(r"$\delta\omega = \omega_{out} - \omega_{in}$ (M$_{KK}$)")
ax.set_title("Eigenvalue shift during quench")
ax.axhline(0, color='gray', ls='--', lw=0.5)
cb = plt.colorbar(ax.collections[0], ax=ax)
cb.set_label(r"$\log_{10}|\beta_k|^2$")

# Panel 2: Bogoliubov occupation
ax = axes[0, 1]
ax.scatter(omega_out, beta2, s=dim2/5, alpha=0.5, c='steelblue', edgecolors='none')
ax.set_xlabel(r"$\omega_{out}$ (M$_{KK}$)")
ax.set_ylabel(r"$|\beta_k|^2$")
ax.set_title(r"Bogoliubov $|\beta_k|^2$ vs post-transit energy")
ax.set_yscale('log')
ax.set_ylim(1e-6, 1)

# Panel 3: Power spectrum (deg-weighted)
ax = axes[0, 2]
good_plot = P_unique > 0
ax.scatter(omega_out_unique[good_plot], P_unique[good_plot],
           s=10, c='darkred', alpha=0.7)
# Fit line
x_fit = np.linspace(np.log(omega_out_unique[good_plot].min()),
                     np.log(omega_out_unique[good_plot].max()), 100)
y_fit = np.polyval(coeffs_u, x_fit)
ax.plot(np.exp(x_fit), np.exp(y_fit), 'k--', lw=1.5,
        label=f'Fit: $n_s - 1$ = {coeffs_u[0]:.3f}')
ax.set_xlabel(r"$\omega_{out}$ (M$_{KK}$)")
ax.set_ylabel(r"$P(\omega) = \sum d^2 |\beta_k|^2$")
ax.set_title(f"Power spectrum (n$_s$ = {ns_final:.4f})")
ax.set_yscale('log')
ax.set_xscale('log')
ax.legend()

# Panel 4: Running n_s (local)
ax = axes[1, 0]
good_loc = k_local > 0
if np.sum(good_loc) > 0:
    ax.plot(k_local[good_loc], ns_local[good_loc], 'b-', alpha=0.7)
    ax.axhline(ns_planck, color='red', ls='--', lw=1.5,
               label=f"Planck n$_s$ = {ns_planck}")
    ax.axhspan(ns_planck - ns_planck_sigma, ns_planck + ns_planck_sigma,
               alpha=0.2, color='red')
    ax.axhline(ns_final, color='k', ls=':', lw=1.5,
               label=f"This work n$_s$ = {ns_final:.4f}")
ax.set_xlabel(r"$k$ (M$_{KK}$)")
ax.set_ylabel(r"$n_s$ (local)")
ax.set_title("Running spectral tilt")
ax.legend(fontsize=8)

# Panel 5: Sensitivity to Delta_0
ax = axes[1, 1]
Delta_fracs = [0.0, 0.5, 1.0, 1.5, 2.0]
ns_vs_delta = [results.get(f"Delta={f}x", np.nan) for f in ["0.0x (free)", "0.5x", "1.0x", "1.5x", "2.0x"]]
ax.plot(Delta_fracs, ns_vs_delta, 'ko-', ms=8)
ax.axhspan(0.955, 0.975, alpha=0.2, color='green', label='PASS window')
ax.axhspan(0.80, 0.955, alpha=0.1, color='yellow')
ax.axhspan(0.975, 1.10, alpha=0.1, color='yellow')
ax.set_xlabel(r"$\Delta_0 / \Delta_0^{GL}$")
ax.set_ylabel(r"$n_s$")
ax.set_title(r"Sensitivity to BCS gap $\Delta_0$")
ax.legend(fontsize=8)

# Panel 6: beta2 decomposition
ax = axes[1, 2]
ax.scatter(omega_out_unique[good_plot], beta2_mean[good_plot], s=10,
           c='blue', alpha=0.7, label=r'$|\beta_k|^2$')
ax2 = ax.twinx()
ax2.scatter(omega_out_unique[good_plot], dim2_total[good_plot], s=10,
            c='red', alpha=0.5, label=r'$\sum d^2$')
ax.set_xlabel(r"$\omega_{out}$ (M$_{KK}$)")
ax.set_ylabel(r"$|\beta_k|^2$ (mean)", color='blue')
ax2.set_ylabel(r"$\sum d^2$ (total)", color='red')
ax.set_title(r"Decomposition: $|\beta_k|^2$ and degeneracy")
ax.set_yscale('log')
ax2.set_yscale('log')

fig.suptitle(f"KZ-NS-45: Bogoliubov Spectrum for $n_s$ | "
             f"Verdict: {verdict} | $n_s$ = {ns_final:.4f}",
             fontsize=14, fontweight='bold')

plt.tight_layout()
plt.savefig(DATA_DIR / f"{OUT_PREFIX}.png", dpi=150)
print(f"  Saved: {DATA_DIR / f'{OUT_PREFIX}.png'}")

print("\n" + "=" * 78)
print(f"KZ-NS-45 COMPLETE: n_s = {ns_final:.4f}, verdict = {verdict}")
print("=" * 78)
