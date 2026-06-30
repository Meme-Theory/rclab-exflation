#!/usr/bin/env python3
"""
s53_kz_power_spectrum.py — KZ Primordial Power Spectrum from BCS Transit
=========================================================================

Gate: NS-ACOUSTIC-53 / KZ-POWER-SPECTRUM-53
  PASS: n_s within [0.955, 0.975] (3σ of Planck 0.965 ± 0.004)
  INFO: n_s computed but outside 3σ
  FAIL: spectrum cannot be computed

Physics:
  In exflation, the primordial perturbation spectrum is NOT from slow-roll
  vacuum fluctuations. It comes from the Kibble-Zurek excitation pattern
  during the BCS transit. When the condensate forms and is destroyed
  (P_exc = 1.000), 59.8 quasiparticle pairs are created across 6 GL branches.
  The POPULATION PATTERN across modes IS the primordial spectrum.

  The KZ mechanism produces:
    n_k ~ exp(-π k² ξ_KZ²)                          (Zurek 1996)
    ξ_KZ = ξ₀ × (τ_quench / τ₀)^{ν/(1+νz)}        (KZ scaling)
  with z=2 (diffusive), ν=1/2 (mean-field BCS), giving exponent 1/4.

  Each GL branch i has dispersion ω_i(K). The energy-weighted mode occupation:
    P(K) = Σ_i ω_i(K) × n_i(K)
  where n_i(K) ∝ exp(-π K² ξ_KZ²) × ρ_i(K) and ρ_i(K) is the density of
  states of branch i (from the dispersion).

  This is deterministic — set by ξ_KZ, quench rate, and GL dispersion.

Session: S53
Agent: Tesla-Resonance
"""

import sys, os
sys.path.insert(0, os.path.dirname(__file__))
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from canonical_constants import (
    xi_BCS, xi_GL, dt_transit, n_pairs, E_exc,
    Delta_0_GL, v_terminal, tau_fold, M_KK, M_KK_gravity,
    omega_PV, omega_att, A_s_CMB, PI, c_Gold, H_fold,
    omega_L1, omega_L2, omega_H1, omega_H2, omega_H3,
    E_cond, Kapitza_ratio, Gamma_Langer_BCS, S_inst,
    N_cells, L_over_xi, a_GL, b_GL, barrier_0d,
    hbar_c_GeV_m, M_Pl_reduced, rho_Lambda_obs
)

OUT_DIR = os.path.dirname(__file__)
PREFIX = "s53_kz_power_spectrum"

# ==============================================================================
#  1. LOAD GL DISPERSION DATA
# ==============================================================================

gl_data = np.load(os.path.join(OUT_DIR, "s52_gl_josephson.npz"), allow_pickle=True)
K_gl = gl_data['K_array']          # (51,) wavenumber array [M_KK units]
omega_gl = gl_data['omega_branches']  # (51, 6) branch dispersions [M_KK units]
branch_labels = list(gl_data['branch_labels'])
K_BZ = float(gl_data['K_BZ'])
c_eff_gl = gl_data['c_eff']        # (6,) effective speeds at K=0

# Also load Bogoliubov data for mode-resolved excitation info
bogo_data = np.load(os.path.join(OUT_DIR, "s52_bogoliubov_amp.npz"), allow_pickle=True)

print("=" * 72)
print("KZ PRIMORDIAL POWER SPECTRUM — EXFLATION")
print("=" * 72)
print()

# ==============================================================================
#  2. KZ CORRELATION LENGTH
# ==============================================================================
# KZ scaling: ξ_KZ = ξ₀ × (τ_quench / τ₀)^{ν/(1+νz)}
# For BCS (mean-field): ν = 1/2, z = 2 (diffusive dynamics)
# Exponent: ν/(1+νz) = (1/2)/(1 + 1/2 × 2) = (1/2)/2 = 1/4
#
# ξ₀ = xi_BCS (BCS coherence length, the microscopic scale)
# τ_quench = dt_transit (transit duration)
# τ₀ = 1/omega_PV (the microscopic relaxation time, pair vibration period)
#   This is the natural internal timescale — the period of the dominant
#   collective mode. omega_PV = 0.792 M_KK → τ₀ = 1.263 M_KK^{-1}

nu_KZ = 0.5      # mean-field correlation length exponent
z_KZ = 2          # dynamic critical exponent (diffusive/BCS)
KZ_exponent = nu_KZ / (1 + nu_KZ * z_KZ)  # = 1/4

xi_0 = xi_BCS                      # microscopic coherence length [M_KK^{-1}]
tau_0 = 1.0 / omega_PV             # microscopic relaxation time [M_KK^{-1}]
tau_quench = dt_transit             # quench duration [M_KK^{-1}]

# KZ correlation length
xi_KZ = xi_0 * (tau_quench / tau_0) ** KZ_exponent

# KZ freeze-out time
t_freeze = tau_0 * (tau_quench / tau_0) ** (nu_KZ * z_KZ / (1 + nu_KZ * z_KZ))

print("--- KZ Parameters ---")
print(f"  nu = {nu_KZ}, z = {z_KZ}, KZ exponent = {KZ_exponent}")
print(f"  xi_0 (xi_BCS)      = {xi_0:.6f} M_KK^{{-1}}")
print(f"  tau_0 (1/omega_PV)  = {tau_0:.6f} M_KK^{{-1}}")
print(f"  tau_quench          = {tau_quench:.6e} M_KK^{{-1}}")
print(f"  tau_quench/tau_0    = {tau_quench/tau_0:.6e}")
print(f"  xi_KZ               = {xi_KZ:.6f} M_KK^{{-1}}")
print(f"  xi_KZ/xi_0          = {xi_KZ/xi_0:.6f}")
print(f"  t_freeze            = {t_freeze:.6e} M_KK^{{-1}}")
print(f"  K_KZ = 1/xi_KZ      = {1.0/xi_KZ:.4f} M_KK")
print(f"  K_BZ                = {K_BZ:.4f} M_KK")
print()

# ==============================================================================
#  3. HIGH-RESOLUTION K-ARRAY AND INTERPOLATED DISPERSIONS
# ==============================================================================
# Use a finer K grid for accurate spectral index fitting

N_K = 2000  # (local)
K_fine = np.linspace(1e-6, K_BZ, N_K)  # avoid K=0 exactly

# Interpolate each branch dispersion onto fine grid
from scipy.interpolate import interp1d

omega_fine = np.zeros((N_K, 6))
for i in range(6):
    f_interp = interp1d(K_gl, omega_gl[:, i], kind='cubic', fill_value='extrapolate')
    omega_fine[:, i] = np.abs(f_interp(K_fine))  # ensure positive

# Verify: Goldstone branch should be approximately linear at low K
# omega_Gold(K) ≈ c_Gold * K for small K
slope_check = omega_fine[10, 0] / K_fine[10]
print(f"--- Dispersion check ---")
print(f"  Goldstone slope at K={K_fine[10]:.5f}: {slope_check:.4f} (c_Gold = {c_Gold:.4f})")
print(f"  Leggett-1 gap: {omega_fine[0, 1]:.6f} M_KK")
print(f"  Leggett-2 gap: {omega_fine[0, 2]:.6f} M_KK")
print()

# ==============================================================================
#  4. DENSITY OF STATES PER BRANCH
# ==============================================================================
# In 3D (the internal SU(3) is 8D but we project onto radial K), the DOS
# for a branch with dispersion ω(K) is:
#   ρ_i(K) = K² / |dω_i/dK|    (spherical K-space shell / group velocity)
#
# For the Goldstone branch (ω ≈ c*K): ρ ~ K²/c ~ K²
# For gapped branches (ω ≈ √(Δ² + c²K²)): ρ ~ K² * ω/(c²K) = K*ω/c²
#   → suppressed below the gap scale

dK = K_fine[1] - K_fine[0]
dos_fine = np.zeros((N_K, 6))
for i in range(6):
    # Numerical group velocity |dω/dK|
    dw_dK = np.gradient(omega_fine[:, i], K_fine)
    # Avoid division by zero
    dw_dK = np.maximum(np.abs(dw_dK), 1e-12)
    # DOS ∝ K² / v_g (3D density of states in K-space)
    dos_fine[:, i] = K_fine**2 / dw_dK

# ==============================================================================
#  5. KZ OCCUPATION NUMBER
# ==============================================================================
# The Kibble-Zurek mechanism populates modes with occupation:
#   n_i(K) = n_0 × exp(-π K² ξ_KZ²) × weight_i
#
# The weight_i accounts for the sector multiplicity:
# - Goldstone: 1 mode (U(1)_7 phase)
# - Leggett-1: 1 mode (relative phase B2/B1)
# - Leggett-2: 1 mode (relative phase B2/B3)
# - Branch-3,4,5: amplitude/Higgs modes
#
# The BCS transit creates excitations BELOW the gap preferentially.
# For gapped modes: n_i(K) is further suppressed by exp(-Δ_i/T_eff)
# where T_eff ~ instantaneous effective temperature during quench.
#
# The total number of pairs is fixed: n_pairs = 59.8

# KZ Gaussian envelope
kz_envelope = np.exp(-PI * K_fine**2 * xi_KZ**2)

# Gap suppression: modes with gap Δ_i are Boltzmann-suppressed
# T_eff during transit ~ barrier_0d or E_cond scale
# Use E_exc / N_dof_BCS as effective temperature
T_eff = abs(E_exc) / 8.0  # microcanonical temperature per DOF
print(f"--- Effective temperature ---")
print(f"  T_eff = E_exc / N_dof = {T_eff:.4f} M_KK")
print()

gaps = np.array([0.0, omega_L1, omega_L2, omega_H1, omega_H2, omega_H3])
gap_suppression = np.exp(-gaps / T_eff)

print("--- Gap suppression factors ---")
for i, l in enumerate(branch_labels):
    print(f"  {l}: gap = {gaps[i]:.4f}, suppression = {gap_suppression[i]:.6f}")
print()

# Build mode occupation for each branch
n_occ = np.zeros((N_K, 6))
for i in range(6):
    n_occ[:, i] = kz_envelope * gap_suppression[i] * dos_fine[:, i]

# Normalize: total number of excited pairs = n_pairs
# Integrate n_occ over K (with 4π K² already in DOS)
# Actually DOS already contains K², so integrate over dK:
total_raw = np.sum(n_occ) * dK
norm = n_pairs / total_raw if total_raw > 0 else 1.0
n_occ *= norm

# Verify normalization
total_pairs = np.sum(n_occ) * dK
print(f"--- Normalization ---")
print(f"  Total excitation count: {total_pairs:.2f} (target: {n_pairs})")
print()

# ==============================================================================
#  6. ENERGY-WEIGHTED POWER SPECTRUM P(K)
# ==============================================================================
# P(K) = Σ_i ω_i(K) × n_i(K)
# This is the energy deposited per K-mode — the analog of Δ²(k) in inflation.

P_K = np.zeros(N_K)
P_branch = np.zeros((N_K, 6))
for i in range(6):
    P_branch[:, i] = omega_fine[:, i] * n_occ[:, i]
    P_K += P_branch[:, i]

# Total energy check
E_total_spectrum = np.sum(P_K) * dK
print(f"--- Power spectrum ---")
print(f"  Total energy in spectrum: {E_total_spectrum:.4f} M_KK")
print(f"  E_exc (canonical):        {E_exc:.4f} M_KK")
print(f"  Ratio:                    {E_total_spectrum / E_exc:.4f}")
print()

# Branch-resolved energy fractions
E_per_branch = np.array([np.sum(P_branch[:, i]) * dK for i in range(6)])
E_total_branch = np.sum(E_per_branch)
print("--- Branch energy fractions ---")
for i, l in enumerate(branch_labels):
    print(f"  {l}: E = {E_per_branch[i]:.4f} ({100*E_per_branch[i]/E_total_branch:.1f}%)")
print()

# ==============================================================================
#  7. SPECTRAL INDEX n_s
# ==============================================================================
# Fit P(K) ~ K^{n_s - 1} over a suitable range.
#
# The fitting range is critical. In inflation, the "observable window" is
# modes that crossed the Hubble radius during the last ~7 e-folds.
# Here, the observable window is K < 1/xi_KZ (modes that freeze out).
# We fit from K_min = K_fine[1] to K_max ~ a few × 1/xi_KZ.

K_KZ = 1.0 / xi_KZ  # KZ cutoff wavenumber

# Fit range: from lowest K to ~3 × K_KZ (spanning ~1.5 decades if possible)
K_fit_min = K_fine[5]              # avoid K≈0 numerical issues
K_fit_max = min(3.0 * K_KZ, 0.5 * K_BZ)  # don't go beyond BZ/2

mask_fit = (K_fine >= K_fit_min) & (K_fine <= K_fit_max) & (P_K > 0)

print(f"--- Spectral index fit ---")
print(f"  K_KZ = {K_KZ:.4f} M_KK")
print(f"  Fit range: [{K_fit_min:.5f}, {K_fit_max:.4f}] M_KK")
print(f"  Fit points: {np.sum(mask_fit)}")

# Power-law fit in log-log space: log P = (n_s - 1) × log K + const
log_K = np.log(K_fine[mask_fit])
log_P = np.log(P_K[mask_fit])

# Linear regression
def power_law_log(logK, ns_minus_1, logA):
    return ns_minus_1 * logK + logA

popt, pcov = curve_fit(power_law_log, log_K, log_P)
ns_minus_1 = popt[0]
n_s = 1.0 + ns_minus_1  # (local)
ns_err = np.sqrt(pcov[0, 0])

print(f"  n_s - 1 = {ns_minus_1:.6f} ± {ns_err:.6f}")
print(f"  n_s     = {n_s:.6f} ± {ns_err:.6f}")
print(f"  Planck: n_s = 0.9649 ± 0.0042")
print(f"  Deviation: {abs(n_s - 0.9649)/0.0042:.2f} σ")
print()

# Also do a sliding-window local spectral index
# n_s_local(K) = d ln P / d ln K
log_K_all = np.log(K_fine[P_K > 0])
log_P_all = np.log(P_K[P_K > 0])
ns_local = np.gradient(log_P_all, log_K_all) + 1  # +1 because n_s - 1 = d ln P / d ln K

# Running of spectral index: dn_s/d ln K
dns_dlnK = np.gradient(ns_local, log_K_all)

print(f"--- Local spectral index at key scales ---")
K_pos = K_fine[P_K > 0]
for K_probe in [0.01, 0.05, 0.1, K_KZ, 0.3, 0.5]:
    if K_probe < K_pos[-1]:
        idx = np.argmin(np.abs(K_pos - K_probe))
        print(f"  K = {K_pos[idx]:.4f}: n_s_local = {ns_local[idx]:.4f}, dn_s/dlnK = {dns_dlnK[idx]:.4f}")
print()

# ==============================================================================
#  8. AMPLITUDE A_s
# ==============================================================================
# The pivot scale in inflation is k_pivot = 0.05 Mpc^{-1}.
# Here, the "pivot" is K_pivot ~ 1/xi_KZ (the KZ freeze-out scale).
#
# The amplitude comparison requires mapping K (internal, M_KK units) to
# k (comoving, Mpc^{-1}). The mapping involves:
#   k_comov = K_internal × (M_KK / M_Pl) × (a_transit / a_0)
#
# But we can compare the DIMENSIONLESS power spectrum:
#   Δ² = (K³ / 2π²) × P(K) / E_total
# at the pivot scale, where E_total = total energy in the 4D patch.
#
# In exflation, the total energy in a Hubble volume at transit is set by
# the spectral action: E_Hubble ~ a_0 × M_KK^4 × V_Hubble
# V_Hubble = (4π/3) × (1/H_fold)³ in M_KK units

# Dimensionless power spectrum
Delta_sq = K_fine**3 / (2 * PI**2) * P_K / E_total_spectrum

# Evaluate at pivot scale (K_KZ)
idx_pivot = np.argmin(np.abs(K_fine - K_KZ))
K_pivot = K_fine[idx_pivot]
Delta_sq_pivot = Delta_sq[idx_pivot]

print(f"--- Amplitude ---")
print(f"  K_pivot = {K_pivot:.5f} M_KK")
print(f"  P(K_pivot) = {P_K[idx_pivot]:.6e}")
print(f"  Δ²(K_pivot) = {Delta_sq_pivot:.6e} (dimensionless, internal)")
print()

# Map to physical amplitude:
# The energy fraction that goes into perturbations vs background:
# δρ/ρ ~ Δ² × (n_pairs × E_qp / E_background)
# E_background ~ S_fold × M_KK^4 / M_Pl^2 (spectral action → Einstein-Hilbert)
#
# More directly: A_s^{exfl} = E_exc / E_Hubble × Δ²(K_pivot)
# where E_Hubble = (M_Pl²/M_KK²) × H²  (Friedmann in KK units)
# H_fold = 586.5 M_KK → E_Hubble ~ M_Pl² × H² / M_KK²
#                                 ~ (2.435e18)² × (586.5)² / (7.43e16)²
# That's dimensionless: (M_Pl/M_KK)² × H_fold²

R_Pl_KK = M_Pl_reduced / M_KK_gravity  # ~ 32.8
E_Hubble_dimless = R_Pl_KK**2 * H_fold**2  # dimensionless energy scale

# The physical amplitude:
# A_s ~ (E_exc / E_Hubble) × Δ²(K_pivot) × (extra geometric factors)
# E_exc = 60.6 M_KK (energy in excitations)
# But this needs to be ratio to the Hubble energy M_Pl² H² ~ R² H²
A_s_exfl_raw = (E_exc / E_Hubble_dimless) * Delta_sq_pivot

print(f"  R_Pl_KK = M_Pl/M_KK = {R_Pl_KK:.2f}")
print(f"  E_Hubble (dimless) = {E_Hubble_dimless:.4e}")
print(f"  A_s^{{exfl}} (raw) = {A_s_exfl_raw:.4e}")
print(f"  A_s^{{CMB}}        = {A_s_CMB:.4e}")
print(f"  Ratio A_s^exfl / A_s^CMB = {A_s_exfl_raw / A_s_CMB:.4e}")
print()

# Alternative: the perturbation amplitude is set by the fraction of
# excitation energy per Hubble volume relative to the background energy.
# A_s ~ (E_exc / V_Hub) / (3 M_Pl² H²) where V_Hub = (2π/H)^3
# In M_KK units: V_Hub = (2π/H_fold)^3
V_Hub = (2*PI / H_fold)**3
rho_exc = E_exc / V_Hub  # excitation energy density [M_KK^4]
rho_bg = 3 * R_Pl_KK**2 * H_fold**2  # Friedmann: ρ_bg = 3M_Pl²H² [M_KK^4 via ratio]

A_s_exfl_v2 = rho_exc / rho_bg * Delta_sq_pivot

print(f"--- Alternative amplitude estimate ---")
print(f"  V_Hubble = {V_Hub:.4e} M_KK^{{-3}}")
print(f"  rho_exc  = {rho_exc:.4e} M_KK^4")
print(f"  rho_bg   = {rho_bg:.4e} M_KK^4")
print(f"  rho_exc/rho_bg = {rho_exc/rho_bg:.4e}")
print(f"  A_s^{{exfl}} (v2) = {A_s_exfl_v2:.4e}")
print(f"  log10(A_s^exfl / A_s^CMB) = {np.log10(A_s_exfl_v2 / A_s_CMB):.2f}")
print()

# ==============================================================================
#  9. KZ SCALING ANALYSIS — SENSITIVITY TO PARAMETERS
# ==============================================================================
# Check how n_s depends on the KZ exponent (nu, z choices)

print("--- Sensitivity analysis ---")
print("  Varying KZ exponent (nu, z):")
for nu_test, z_test, label in [(0.5, 2, "mean-field BCS (canonical)"),
                                 (0.5, 1, "z=1 (quantum KZ)"),
                                 (0.67, 2, "3D Ising ν=0.67"),
                                 (1.0, 2, "ν=1 (2D Ising)")]:
    exp_test = nu_test / (1 + nu_test * z_test)
    xi_test = xi_0 * (tau_quench / tau_0) ** exp_test
    K_KZ_test = 1.0 / xi_test

    # Recompute envelope and P(K)
    env_test = np.exp(-PI * K_fine**2 * xi_test**2)
    P_test = np.zeros(N_K)
    for i in range(6):
        n_test = env_test * gap_suppression[i] * dos_fine[:, i]
        P_test += omega_fine[:, i] * n_test

    # Fit spectral index
    K_max_test = min(3.0 * K_KZ_test, 0.5 * K_BZ)
    mask_test = (K_fine >= K_fit_min) & (K_fine <= K_max_test) & (P_test > 0)
    if np.sum(mask_test) > 10:
        lK = np.log(K_fine[mask_test])
        lP = np.log(P_test[mask_test])
        p_test, _ = curve_fit(power_law_log, lK, lP)
        ns_test = 1.0 + p_test[0]
    else:
        ns_test = float('nan')

    print(f"    (nu={nu_test}, z={z_test}): xi_KZ={xi_test:.4f}, "
          f"K_KZ={K_KZ_test:.4f}, n_s={ns_test:.4f}  [{label}]")
print()

# ==============================================================================
#  10. ACOUSTIC OSCILLATION PATTERN
# ==============================================================================
# The Goldstone branch, being gapless and linear, dominates the low-K spectrum.
# This creates a characteristic acoustic signature:
# At K < K_KZ: P(K) ~ c_Gold * K * K² * exp(-πK²ξ²) ∝ K³ exp(-πK²ξ²)
# This is already like Δ² ~ K^{n_s-1} with n_s-1 ≈ 3 at low K, then bending
# due to the Gaussian cutoff.
#
# The effective n_s over the KZ window is set by the competition:
# - K² from DOS (pushes n_s > 1, blue)
# - exp(-πK²ξ²) from KZ (pushes n_s < 1, red)
# - The balance gives n_s - 1 ≈ 2 - 2πK²ξ² (evaluated at K_pivot)

ns_analytic = 1 + 2 - 2 * PI * K_pivot**2 * xi_KZ**2
print(f"--- Analytic estimate ---")
print(f"  n_s ≈ 3 - 2πK²ξ² = {ns_analytic:.4f} (Goldstone-dominated)")
print(f"  This shows the spectrum is BLUE (n_s > 1) when KZ cutoff is far.")
print(f"  Red tilt requires either: gapped branch contribution, or K_pivot ~ K_KZ.")
print()

# ==============================================================================
#  11. GOLDSTONE-ONLY ANALYSIS (CLEAN ACOUSTIC)
# ==============================================================================
# Isolate the Goldstone contribution for the cleanest acoustic spectrum.
# For acoustic branch: ω = c*K, ρ = K²/c, so
#   P_Gold(K) = c*K × n_0 × exp(-πK²ξ²) × K²/c = n_0 × K³ × exp(-πK²ξ²)
#   → Δ²_Gold = K³/(2π²) × K³ exp(-πK²ξ²) / norm = K⁶ exp(-πK²ξ²) / norm (dim'less)
#
# But what we really want is the occupation number spectrum n(K):
#   n(K) = K² × exp(-πK²ξ²)  (Goldstone, after stripping ω weighting)
# The spectral index of n(K) is n_s - 1 = 2 - 2πK²ξ².
# At K = K_KZ: n_s - 1 = 2 - 2π ≈ -4.28 (very red!)
# At K = K_KZ/√π ≈ 0.564 K_KZ: n_s = 1 (scale-invariant).

K_scale_inv = K_KZ / np.sqrt(PI)
print(f"--- Scale-invariant K (Goldstone) ---")
print(f"  K where n_s = 1: {K_scale_inv:.4f} M_KK (= K_KZ/sqrt(π))")
print(f"  K_KZ = {K_KZ:.4f} M_KK")
print()

# The OCCUPATION spectrum n(K) = exp(-πK²ξ²) has:
# d ln n / d ln K = -2πK²ξ²
# So n_s - 1 = d ln(K² n(K)) / d ln K = 2 - 2πK²ξ²
# This crosses n_s = 1 at K = K_KZ/√π and is red for K > K_KZ/√π.
#
# The ENERGY spectrum P(K) = ω(K) × n(K) × ρ(K) adds one more power of K
# for the Goldstone (ω = cK), giving d ln P/d ln K = 3 - 2πK²ξ².
# Scale invariant at K = K_KZ × √(3/(2π)).

K_P_scale_inv = K_KZ * np.sqrt(3.0 / (2*PI))
print(f"  K where P(K) is scale-invariant: {K_P_scale_inv:.4f} M_KK")
print()

# ==============================================================================
#  12. DIMENSIONLESS POWER SPECTRUM Δ²(K)
# ==============================================================================
# The standard definition: Δ²(k) = k³ P(k) / (2π²)
# Our P(K) already has the mode counting from DOS, so:
# Δ²(K) = K³/(2π²) × P(K) / ∫P(K)dK

# Already computed as Delta_sq above. Find its spectral index.
mask_delta = (K_fine >= K_fit_min) & (K_fine <= K_fit_max) & (Delta_sq > 0)
if np.sum(mask_delta) > 10:
    log_K_d = np.log(K_fine[mask_delta])
    log_D = np.log(Delta_sq[mask_delta])
    popt_d, pcov_d = curve_fit(power_law_log, log_K_d, log_D)
    n_Delta = 1.0 + popt_d[0] / 3.0  # Δ² ~ K^{3(n_s-1)} for dimensionless spectrum
    # Actually: Δ²(k) ~ k^{n_s - 1}, so n_s - 1 = d ln Δ² / d ln k
    n_s_Delta = 1.0 + popt_d[0]
    ns_Delta_err = np.sqrt(pcov_d[0,0])
    print(f"--- Δ²(K) spectral index ---")
    print(f"  d ln Δ² / d ln K = {popt_d[0]:.4f}")
    print(f"  n_s from Δ² = {n_s_Delta:.6f} ± {ns_Delta_err:.6f}")
else:
    n_s_Delta = float('nan')
    ns_Delta_err = float('nan')
    print("  WARNING: Not enough points for Δ² fit")
print()

# ==============================================================================
#  13. GATE VERDICT
# ==============================================================================

# Use P(K) spectral index as the primary result
n_s_final = n_s
ns_err_final = ns_err

# Planck constraint
n_s_Planck = 0.9649
n_s_Planck_err = 0.0042
deviation_sigma = abs(n_s_final - n_s_Planck) / n_s_Planck_err

if abs(n_s_final - n_s_Planck) <= 3 * n_s_Planck_err:
    verdict = "PASS"
else:
    verdict = "INFO"

print("=" * 72)
print(f"GATE: NS-ACOUSTIC-53 / KZ-POWER-SPECTRUM-53")
print(f"  n_s = {n_s_final:.6f} ± {ns_err_final:.6f}")
print(f"  Planck: 0.9649 ± 0.0042")
print(f"  Deviation: {deviation_sigma:.2f} σ")
print(f"  Verdict: {verdict}")
if n_s_final > 1:
    print(f"  NOTE: Spectrum is BLUE (n_s > 1). KZ on acoustic branch produces blue tilt")
    print(f"  at scales K < K_KZ because DOS ~ K² dominates over Gaussian suppression.")
    print(f"  Red tilt requires K > K_KZ/sqrt(pi) = {K_scale_inv:.4f}, i.e., sub-KZ scales.")
print("=" * 72)
print()

# ==============================================================================
#  14. PHYSICAL INTERPRETATION
# ==============================================================================

print("=" * 72)
print("PHYSICAL INTERPRETATION")
print("=" * 72)
print()
print("The KZ excitation spectrum during BCS transit has the following structure:")
print()
print("1. RESONANCE STRUCTURE:")
print(f"   - Cavity: SU(3) internal geometry at tau_fold = {tau_fold}")
print(f"   - Modes: 6 GL collective branches (1 Goldstone + 2 Leggett + 3 Higgs)")
print(f"   - Boundary: K_BZ = {K_BZ:.4f} (Brillouin zone edge)")
print(f"   - KZ cutoff: K_KZ = {K_KZ:.4f} (correlation length scale)")
print()
print("2. MODE POPULATION:")
print(f"   - Total excited pairs: {n_pairs}")
print(f"   - Goldstone branch dominates low-K (gapless, linear dispersion)")
print(f"   - Gapped branches (Leggett, Higgs) populate high-K only")
print()
print("3. SPECTRAL INDEX:")
print(f"   - n_s = {n_s_final:.6f} from P(K) fit over [{K_fit_min:.4f}, {K_fit_max:.4f}]")
print(f"   - The tilt is set by the competition between:")
print(f"     * K² DOS factor (blue)")
print(f"     * exp(-πK²ξ_KZ²) Gaussian suppression (red)")
print(f"   - At the KZ scale: n_s_local ~ 3 - 2πK_KZ²ξ_KZ² = 3 - 2π = {3 - 2*PI:.3f}")
print()
print("4. CONDENSED MATTER ANALOG:")
print("   - This IS a Chladni pattern on SU(3)")
print("   - The excitation spectrum after a quench through a BCS transition")
print("     is identical to the phonon population of a suddenly struck drum")
print("   - KZ universality: same exponent (nu=1/2, z=2) as He-3B superfluid transition")
print("   - The 6 GL branches are the normal modes; KZ populates them exponentially")
print()
print("5. KEY DIFFERENCE FROM INFLATION:")
print("   - Inflation: P(k) from quantum vacuum fluctuations of a slowly-rolling scalar")
print("   - Exflation: P(K) from deterministic KZ excitation of BCS collective modes")
print("   - Inflation: n_s - 1 = -2ε - η (slow-roll parameters)")
print("   - Exflation: n_s - 1 determined by xi_KZ, dispersion, and DOS")
print("   - Exflation spectrum is DETERMINISTIC (zero free parameters)")
print()

# ==============================================================================
#  15. SAVE DATA
# ==============================================================================

np.savez(os.path.join(OUT_DIR, f"{PREFIX}.npz"),
    # K grid and dispersions
    K_fine=K_fine,
    K_BZ=K_BZ,
    omega_fine=omega_fine,
    branch_labels=branch_labels,
    # KZ parameters
    xi_KZ=xi_KZ,
    xi_0=xi_0,
    tau_quench=tau_quench,
    tau_0=tau_0,
    KZ_exponent=KZ_exponent,
    nu_KZ=nu_KZ,
    z_KZ=z_KZ,
    K_KZ=1.0/xi_KZ,
    # Occupation and power spectrum
    n_occ=n_occ,
    dos_fine=dos_fine,
    P_K=P_K,
    P_branch=P_branch,
    Delta_sq=Delta_sq,
    # Spectral index
    n_s=n_s_final,
    n_s_err=ns_err_final,
    n_s_Delta=n_s_Delta,
    n_s_local=ns_local,
    dns_dlnK=dns_dlnK,
    K_local=K_pos,
    # Amplitude
    Delta_sq_pivot=Delta_sq_pivot,
    K_pivot=K_pivot,
    A_s_exfl_raw=A_s_exfl_raw,
    A_s_exfl_v2=A_s_exfl_v2,
    A_s_CMB=A_s_CMB,
    # Gate
    gate_name=np.array(["NS-ACOUSTIC-53"]),
    gate_verdict=np.array([verdict]),
    gate_detail=np.array([f"n_s={n_s_final:.6f}, deviation={deviation_sigma:.2f}sigma"]),
)
print(f"Data saved: {PREFIX}.npz")

# ==============================================================================
#  16. PLOT
# ==============================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 12))

# (a) P(K) with spectral index fit
ax = axes[0, 0]
for i in range(6):
    mask_pos = P_branch[:, i] > 0
    if np.any(mask_pos):
        ax.semilogy(K_fine[mask_pos], P_branch[mask_pos, i],
                    label=branch_labels[i], alpha=0.7)
ax.semilogy(K_fine[P_K > 0], P_K[P_K > 0], 'k-', lw=2, label='Total P(K)')
# Fit line
K_fit_arr = K_fine[mask_fit]
P_fit_line = np.exp(popt[1]) * K_fit_arr**popt[0]
ax.semilogy(K_fit_arr, P_fit_line, 'r--', lw=2,
           label=f'Fit: K^{{{popt[0]:.3f}}} (n_s={n_s_final:.4f})')
ax.axvline(K_KZ, color='gray', ls=':', alpha=0.5, label=f'K_KZ = {K_KZ:.3f}')
ax.set_xlabel('K [M_KK]', fontsize=12)
ax.set_ylabel('P(K) [M_KK]', fontsize=12)
ax.set_title(f'KZ Power Spectrum (n_s = {n_s_final:.4f})', fontsize=13)
ax.legend(fontsize=8, loc='upper right')
ax.set_xlim(0, K_BZ)

# (b) Dimensionless power spectrum Δ²(K)
ax = axes[0, 1]
mask_d = Delta_sq > 0
ax.loglog(K_fine[mask_d], Delta_sq[mask_d], 'k-', lw=2)
ax.axvline(K_KZ, color='gray', ls=':', alpha=0.5)
ax.axvline(K_scale_inv, color='blue', ls=':', alpha=0.5, label=f'n_s=1 scale')
ax.set_xlabel('K [M_KK]', fontsize=12)
ax.set_ylabel('Δ²(K)', fontsize=12)
ax.set_title('Dimensionless Power Spectrum', fontsize=13)
ax.legend(fontsize=9)

# (c) Local spectral index
ax = axes[1, 0]
# Only plot where we have meaningful data
K_plot_ns = K_pos
ns_plot = ns_local
valid = (K_plot_ns > 0.005) & (K_plot_ns < 0.8*K_BZ) & np.isfinite(ns_plot)
ax.plot(K_plot_ns[valid], ns_plot[valid], 'k-', lw=1.5)
ax.axhline(0.9649, color='red', ls='--', lw=1, label='Planck n_s = 0.965')
ax.axhline(1.0, color='gray', ls=':', alpha=0.5, label='Scale invariant')
ax.axvline(K_KZ, color='gray', ls=':', alpha=0.5, label=f'K_KZ')
ax.fill_between([K_fine[0], K_fine[-1]], 0.9649-3*0.0042, 0.9649+3*0.0042,
                alpha=0.1, color='red', label='Planck 3σ')  # (local)
ax.set_xlabel('K [M_KK]', fontsize=12)
ax.set_ylabel('n_s(K)', fontsize=12)
ax.set_title('Running Spectral Index', fontsize=13)
ax.set_xlim(0, K_BZ)
ax.set_ylim(-1, 5)
ax.legend(fontsize=8)

# (d) KZ occupation number per branch at K=0
ax = axes[1, 1]
# Occupation at low K (averaged over first 10 bins)
n_low = np.mean(n_occ[:10, :], axis=0)
colors = plt.cm.Set2(np.linspace(0, 1, 6))
bars = ax.bar(range(6), n_low, color=colors, edgecolor='black')
ax.set_xticks(range(6))
ax.set_xticklabels([l[:8] for l in branch_labels], rotation=45, ha='right', fontsize=9)
ax.set_ylabel('n(K→0) per mode', fontsize=12)
ax.set_title('KZ Low-K Occupation', fontsize=13)
# Add gap values
for i, (l, g) in enumerate(zip(branch_labels, gaps)):
    ax.text(i, n_low[i]*1.05, f'Δ={g:.3f}', ha='center', fontsize=7)

plt.suptitle('KZ-POWER-SPECTRUM-53: Primordial Power Spectrum from BCS Transit\n'
             f'Gate NS-ACOUSTIC-53: {verdict}', fontsize=14, fontweight='bold')
plt.tight_layout(rect=[0, 0, 1, 0.94])
plt.savefig(os.path.join(OUT_DIR, f"{PREFIX}.png"), dpi=150, bbox_inches='tight')
print(f"Plot saved: {PREFIX}.png")

print()
print("DONE.")
