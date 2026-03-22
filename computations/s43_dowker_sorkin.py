"""
DS-LAMBDA-43: Dowker-Sorkin Everpresent Lambda vs Framework CC Comparison
=========================================================================

Structural comparison between:
  (A) Dowker-Sorkin (Paper 19): Lambda_DS ~ 1/sqrt(V) ~ H^2, fluctuating, zero-centered Gaussian
  (B) Framework: Lambda = const (w = -1 to ~10^{-140}), determined by q-theory self-tuning

The two approaches are structurally incompatible:
  - DS: Lambda is STOCHASTIC, V-dependent, sign-reversing, with sigma ~ H_0^2
  - Framework: Lambda is DETERMINISTIC, spatially homogeneous, fixed after self-tuning

This script computes:
1. DS magnitude at current epoch vs framework CC
2. Mutual falsification criteria with DESI
3. Sigma thresholds for exclusion
4. w(z) comparison and distinguishability

Gate: DS-LAMBDA-43 (INFO)
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# =============================================================================
# Physical constants (Planck units: hbar = c = G = 1, M_P = 1)
# =============================================================================
from canonical_constants import l_Planck as l_P  # m
from canonical_constants import t_Planck as t_P  # s
from canonical_constants import M_Pl_unreduced as M_P_GeV  # 1.2209e19 GeV
M_P4_GeV4 = M_P_GeV**4  # GeV^4

# Observed cosmological parameters
H_0_GeV = 1.44e-42    # GeV (H_0 ~ 67.4 km/s/Mpc)
H_0_Planck = H_0_GeV / M_P_GeV  # in Planck units ~1.18e-61
Lambda_obs_GeV4 = 2.888e-122 * M_P4_GeV4  # ~6.44e-47 GeV^4
Lambda_obs_MP4 = 2.888e-122  # in M_P^4

# Age of universe
from canonical_constants import t_universe_s as t_0  # seconds
t_0_Planck = t_0 / t_P  # ~8.07e60

# Observable volume (4-volume of past light cone, order-of-magnitude)
# V_4 ~ (c * t_0)^4 ~ t_0^4 in Planck units
# More precisely: 4-volume ~ (4pi/3) * (c*t_0)^3 * t_0 = (4pi/3) * t_0^4
V_4_Planck = (4 * np.pi / 3) * t_0_Planck**4  # Planck 4-volumes
# In proper counting: N ~ V_4 / l_P^4 = V_4_Planck (since l_P = 1 in Planck units)
N_elements = V_4_Planck  # ~ 10^243 elements in causal set

print("=" * 72)
print("DS-LAMBDA-43: Dowker-Sorkin vs Framework CC Comparison")
print("=" * 72)

# =============================================================================
# 1. DOWKER-SORKIN PREDICTION
# =============================================================================
print("\n--- 1. DOWKER-SORKIN PREDICTION ---")

# DS central claim (Paper 19, eq 3.7): Lambda_DS ~ 1/sqrt(V)
# More precisely: rho_Lambda ~ m_P^4 / sqrt(N) where N = V / l_P^4
# In Planck units: Lambda_DS ~ 1/sqrt(N)

# Poisson fluctuation of N elements:
sigma_N = np.sqrt(N_elements)
Lambda_DS_Planck = 1.0 / np.sqrt(N_elements)  # in M_P^4 (order 1/sqrt(N))

print(f"4-volume of observable universe: V_4 = {V_4_Planck:.3e} l_P^4")
print(f"Number of causal set elements: N = {N_elements:.3e}")
print(f"sqrt(N) = {sigma_N:.3e}")

print(f"\nDS prediction: Lambda_DS ~ 1/sqrt(N) = {Lambda_DS_Planck:.3e} M_P^4")
print(f"Observed: Lambda_obs = {Lambda_obs_MP4:.3e} M_P^4")

ratio_DS_obs = Lambda_DS_Planck / Lambda_obs_MP4
log_ratio = np.log10(ratio_DS_obs)
print(f"\nRatio Lambda_DS / Lambda_obs = {ratio_DS_obs:.3e}")
print(f"log10(ratio) = {log_ratio:.2f}")

# DS also relates to H^2: Lambda ~ H^2 in natural units
# H_0^2 in Planck units:
H0_sq_Planck = H_0_Planck**2
print(f"\nH_0^2 = {H0_sq_Planck:.3e} M_P^4")
print(f"Lambda_obs / H_0^2 = {Lambda_obs_MP4 / H0_sq_Planck:.3f}")
print(f"  (should be ~3 from Friedmann: Lambda = 3 * Omega_Lambda * H^2)")
# Friedmann: H^2 = Lambda/3 * (for pure Lambda universe)
# Actually: H^2 = (8piG/3) * rho_tot. For Lambda: rho_Lambda = Lambda/(8piG)
# So Lambda = 3 * H^2 * Omega_Lambda
Lambda_from_Friedmann = 3 * H0_sq_Planck * 0.685  # Omega_Lambda ~ 0.685
print(f"3 * Omega_Lambda * H_0^2 = {Lambda_from_Friedmann:.3e} M_P^4")

# =============================================================================
# 2. FRAMEWORK PREDICTION
# =============================================================================
print("\n--- 2. FRAMEWORK PREDICTION ---")

# Load framework data
data = np.load('tier0-computation/s42_fabric_wz_v2.npz', allow_pickle=True)
tau_Sfull = data['tau_Sfull']
S_full = data['S_full']
tau_fold = float(data['tau_fold'])
m_tau = float(data['m_tau'])

# Framework CC (from W1-1 / W2-3 of session 43):
# q-theory: S(0) does not gravitate. Gravitating CC = Delta_S = S(fold) - S(0)
S_0 = S_full[0]  # S_full at tau=0
S_fold = float(data['V_fold'])  # S_full at fold (tau=0.19)
Delta_S = S_fold - S_0

# M_KK values
M_KK_gravity = 7.43e16  # GeV (gravity route, favored by FIRAS)
M_KK_Kerner = 5.0e17    # GeV (Kerner route)

# Lambda_internal = Delta_S * M_KK^4 / (16 * pi^2)
Lambda_framework_gravity = Delta_S * (M_KK_gravity / M_P_GeV)**4 / (16 * np.pi**2)
Lambda_framework_Kerner = Delta_S * (M_KK_Kerner / M_P_GeV)**4 / (16 * np.pi**2)

print(f"S(0) = {S_0:.2f} M_KK^4")
print(f"S(fold) = {S_fold:.2f} M_KK^4")
print(f"Delta_S = {Delta_S:.2f} M_KK^4")

print(f"\nM_KK (gravity route) = {M_KK_gravity:.2e} GeV")
print(f"Lambda_internal (gravity) = {Lambda_framework_gravity:.3e} M_P^4")
print(f"log10(Lambda_internal) = {np.log10(Lambda_framework_gravity):.2f}")

print(f"\nM_KK (Kerner route) = {M_KK_Kerner:.2e} GeV")
print(f"Lambda_internal (Kerner) = {Lambda_framework_Kerner:.3e} M_P^4")

# Required Carlip suppression
suppression_gravity = Lambda_framework_gravity / Lambda_obs_MP4
suppression_Kerner = Lambda_framework_Kerner / Lambda_obs_MP4
print(f"\nRequired suppression (gravity): {suppression_gravity:.3e} = 10^{{{np.log10(suppression_gravity):.1f}}}")
print(f"Required suppression (Kerner): {suppression_Kerner:.3e} = 10^{{{np.log10(suppression_Kerner):.1f}}}")

# Framework w prediction
w0_framework = -1.0
wa_framework = 0.0  # exact to ~10^{-140}
print(f"\nFramework w_0 = {w0_framework}")
print(f"Framework w_a = {wa_framework} (exact to ~10^{{-140}})")

# =============================================================================
# 3. STRUCTURAL COMPARISON
# =============================================================================
print("\n--- 3. STRUCTURAL COMPARISON ---")

comparison_table = {
    "Nature of Lambda": ("Stochastic, fluctuating", "Deterministic, constant"),
    "Lambda sign": ("Reverses on ~H^{-1} timescale", "Fixed positive (q-theory)"),
    "Lambda magnitude": ("~ 1/sqrt(V) ~ H^2", "Delta_S * M_KK^4 / (16pi^2)"),
    "CC problem solution": ("Poisson fluctuation of N elements", "Carlip foam + q-theory"),
    "Spacetime substrate": ("Causal set (poset)", "M4 x SU(3) spectral triple"),
    "Lorentz invariance": ("Preserved (causal order)", "Preserved (spectral action)"),
    "w(z) prediction": ("w != -1 (sign reversals)", "w = -1 to ~10^{-140}"),
    "Fine-tuning": ("None claimed", "None (q-theory self-tuning)"),
    "Falsifiable by": ("w = -1 exactly at all z", "w != -1 at any z"),
    "Unimodular gravity": ("Required", "Compatible but not required"),
}

for key, (ds_val, fw_val) in comparison_table.items():
    print(f"\n  {key}:")
    print(f"    DS:        {ds_val}")
    print(f"    Framework: {fw_val}")

# =============================================================================
# 4. MUTUAL FALSIFICATION ANALYSIS
# =============================================================================
print("\n--- 4. MUTUAL FALSIFICATION ---")

# DS predicts: sigma_Lambda / Lambda ~ 1 (O(1) fluctuations on Hubble timescale)
# This means w_eff != -1 generically.
# DS effective w: from Paper 19 eq 4.2 scaling relations
# During DE domination: Lambda ~ const (weak variation), but SIGN changes possible
# The variance in w from DS:
# Lambda(t) = Lambda_0 + delta_Lambda(t), delta_Lambda ~ Lambda_0
# w_eff = -1 + (2/3) * (d ln Lambda / d ln a)
# If Lambda fluctuates by order unity on Hubble timescale:
# d ln Lambda / d ln a ~ 1, so |w + 1| ~ O(1)
# But Paper 19 is more nuanced: during DE era, Lambda ~ const to first order

# DS w(z) from Poisson fluctuations:
# sigma_w(z) ~ (1/3) * sqrt(a(z)^{-4}) / sqrt(V(z)) -- rough
# More precisely: DS predicts w_eff(z) = -1 + delta_w(z)
# where |delta_w| ~ sqrt(rho_m(z) / rho_Lambda(z)) * (Delta_t / t_Hubble(z))

# The key falsification: DESI CPL parameterization
# DESI DR1 (2024): w_0 = -0.55 +/- 0.21, w_a = -1.32 +/- 0.67 (w0waCDM)
# DESI DR2 (2025): w_0 = -0.752 +/- 0.057, w_a = -0.86 +/- 0.28 (DESI+CMB+SN)

# If DS is correct: w_a != 0 is expected (Lambda varies over cosmic history)
# If Framework is correct: w_a = 0 exactly

print("DESI DR2 (2025) CPL fit: w_0 = -0.752 +/- 0.057, w_a = -0.86 +/- 0.28")
print()

# Framework prediction: w_0 = -1.0, w_a = 0.0
# Tension with DESI DR2:
sigma_w0_DESI = 0.057
sigma_wa_DESI = 0.28
w0_DESI = -0.752
wa_DESI = -0.86

tension_w0 = abs(w0_framework - w0_DESI) / sigma_w0_DESI
tension_wa = abs(wa_framework - wa_DESI) / sigma_wa_DESI

print(f"Framework vs DESI DR2:")
print(f"  w_0 tension: |{w0_framework} - ({w0_DESI})| / {sigma_w0_DESI} = {tension_w0:.1f} sigma")
print(f"  w_a tension: |{wa_framework} - ({wa_DESI})| / {sigma_wa_DESI} = {tension_wa:.1f} sigma")

# DS prediction: can accommodate w_a != 0 by construction (Lambda varies)
# DS w_a prediction is QUALITATIVE: sign reversals on Hubble timescale -> w_a < 0 expected
# (Lambda was larger in past, decaying as V grows -> effective w_a < 0)

# DS effective w(z):
# Lambda(z) ~ 1/sqrt(V(z)) where V(z) ~ t(z)^4
# For matter domination: t ~ a^{3/2}, so V ~ a^6
# Lambda(a) ~ a^{-3} during matter era
# rho_Lambda(a) = Lambda(a) / (8piG) ~ a^{-3}
# This gives w_Lambda = -1 + (d ln rho_Lambda)/(3 * d ln a) = -1 + (-3)/3 = -2!
# That's too extreme. Paper 19 is more subtle:
# During DE domination, Lambda ~ const (self-consistent)
# During matter-DE transition: Lambda decays as a^{-2} (Paper 19 eq on line 72-73)

# Let me compute the DS effective w(z) properly:
# rho_Lambda_DS(a) = rho_Lambda_0 * (a/a_0)^{-n} where n depends on era
# Paper 19: n = 4/3 (radiation), n = 2 (matter), n ~ 0 (DE)
# w_eff = -1 + n/3

z_arr = np.linspace(0, 2.5, 200)
a_arr = 1.0 / (1.0 + z_arr)

# DS effective w(z) from Lambda(a) scaling:
# Transition function between DE era (n~0) and matter era (n~2)
Omega_m0 = 0.315
Omega_Lambda0 = 0.685
# Omega_m(z) / Omega_Lambda(z) determines which era dominates
Omega_m_z = Omega_m0 * (1 + z_arr)**3 / (Omega_m0 * (1 + z_arr)**3 + Omega_Lambda0)
# DS: n(z) interpolates from ~0 (DE era) to ~2 (matter era)
n_DS = 2.0 * Omega_m_z  # simple interpolation: n = 2 * Omega_m(z)
w_DS = -1.0 + n_DS / 3.0

# Framework: w = -1 at all z
w_framework = np.full_like(z_arr, -1.0)

# DESI CPL: w(z) = w_0 + w_a * z / (1 + z)
w_DESI_central = w0_DESI + wa_DESI * z_arr / (1 + z_arr)
w_DESI_upper = (w0_DESI + sigma_w0_DESI) + (wa_DESI + sigma_wa_DESI) * z_arr / (1 + z_arr)
w_DESI_lower = (w0_DESI - sigma_w0_DESI) + (wa_DESI - sigma_wa_DESI) * z_arr / (1 + z_arr)

print(f"\nDS effective w(z=0): {w_DS[0]:.4f}")
print(f"DS effective w(z=0.5): {w_DS[np.argmin(np.abs(z_arr-0.5))]:.4f}")
print(f"DS effective w(z=1.0): {w_DS[np.argmin(np.abs(z_arr-1.0))]:.4f}")
print(f"DS effective w(z=2.0): {w_DS[np.argmin(np.abs(z_arr-2.0))]:.4f}")

# =============================================================================
# 5. DESI SIGMA THRESHOLDS FOR EXCLUSION
# =============================================================================
print("\n--- 5. EXCLUSION THRESHOLDS ---")

# Framework exclusion: If |w_a| > X sigma from 0
# Currently: |w_a|/sigma = 0.86/0.28 = 3.07 sigma from w_a = 0
# Framework needs: w_a = 0 at 5 sigma to be safe
# Framework EXCLUDED when: |w_a| / sigma > 5 (5-sigma detection of w_a != 0)

# Current status:
print(f"Current DESI DR2: |w_a| = {abs(wa_DESI):.2f}, sigma = {sigma_wa_DESI:.2f}")
print(f"  |w_a|/sigma = {abs(wa_DESI)/sigma_wa_DESI:.2f} sigma")
print(f"  Framework status: {abs(wa_DESI)/sigma_wa_DESI:.1f} sigma tension (NOT excluded)")

# Projected DESI DR3 (expected ~2026-2027):
# sigma_wa expected to shrink by ~sqrt(2) (more data)
sigma_wa_DR3_proj = sigma_wa_DESI / np.sqrt(2)
print(f"\nProjected DESI DR3 (sigma_wa ~ {sigma_wa_DR3_proj:.2f}):")
print(f"  If central value holds: |w_a|/sigma = {abs(wa_DESI)/sigma_wa_DR3_proj:.2f} sigma")

# Full DESI (DR5, ~2028):
sigma_wa_DR5_proj = sigma_wa_DESI / 2.5  # ~2.5x improvement
print(f"\nProjected DESI DR5 (sigma_wa ~ {sigma_wa_DR5_proj:.2f}):")
print(f"  If central value holds: |w_a|/sigma = {abs(wa_DESI)/sigma_wa_DR5_proj:.2f} sigma")

# Threshold for 5-sigma exclusion of framework:
# Need |w_a| / sigma_wa > 5
# If w_a stays at -0.86: sigma_wa must shrink below 0.86/5 = 0.172
sigma_wa_5sigma = abs(wa_DESI) / 5.0
print(f"\n5-sigma exclusion of framework requires sigma_wa < {sigma_wa_5sigma:.3f}")
print(f"  (reduction factor: {sigma_wa_DESI / sigma_wa_5sigma:.2f}x from current)")

# DS exclusion: harder. DS accommodates a RANGE of w(z).
# DS is excluded if:
# (1) Lambda is measured to be EXACTLY constant at all z (no fluctuations)
# (2) This would require sigma_{delta_Lambda} / Lambda < 1/sqrt(N) ~ 10^{-61}
# Operationally: DS is not excluded by any foreseeable measurement of w(z)
# DS can always accommodate w = -1 as a particular realization

print("\nDS exclusion: Lambda measured constant at all z to precision << 1/sqrt(V)")
print("  Required precision: sigma_w < ~10^{-61} (beyond any experiment)")
print("  DS is NOT falsifiable by w(z) measurements alone")
print("  DS IS falsifiable by: detecting Lorentz violation from discreteness,")
print("    or confirming spacetime is continuous (no Planck-scale granularity)")

# =============================================================================
# 6. RATIO AND STRUCTURAL NUMBERS
# =============================================================================
print("\n--- 6. KEY RATIOS ---")

# DS Lambda vs Framework Lambda (pre-Carlip)
ratio_DS_FW = Lambda_DS_Planck / Lambda_framework_gravity
print(f"Lambda_DS / Lambda_framework = {ratio_DS_FW:.3e}")
print(f"  (DS is {np.log10(ratio_DS_FW):.1f} orders below framework pre-Carlip)")

# DS Lambda vs observed
print(f"Lambda_DS / Lambda_obs = {ratio_DS_obs:.3e}")
print(f"  (DS is {log_ratio:.1f} orders {'above' if log_ratio > 0 else 'below'} observed)")

# Framework Lambda (post-Carlip) vs observed
# From F-FOAM-5-43: Lambda_eff = Lambda_obs exactly at L = 1.74 mm
print(f"Framework (post-Carlip): Lambda_eff = Lambda_obs (by construction at L = 1.74 mm)")

# Both achieve Lambda_obs but by different mechanisms
print(f"\nBoth DS and Framework+Carlip can produce Lambda ~ Lambda_obs:")
print(f"  DS: Poisson statistics, 1/sqrt(N) with N ~ 10^243 -> Lambda ~ 10^{{{-243/2:.0f}}} M_P^4")
print(f"  Framework+Carlip: Foam WDW wavefunction trapping at L = 1.74 mm")

# DS more precisely: Lambda_DS = +/- m_P^4 / sqrt(N)
# For N = V_4 in Planck units: Lambda_DS ~ 1/sqrt(V_4)
# V_4 ~ (H_0^{-1})^4 in Planck units = H_0^{-4} * M_P^4 / (l_P^4 * M_P^4)
# = (1/H_0_Planck)^4
# So Lambda_DS ~ H_0^2 (since 1/sqrt(H_0^{-4}) = H_0^2)
Lambda_DS_from_H = H0_sq_Planck
print(f"\nDS from H_0^2: Lambda_DS = H_0^2 = {Lambda_DS_from_H:.3e} M_P^4")
print(f"Lambda_obs = {Lambda_obs_MP4:.3e} M_P^4")
print(f"Ratio Lambda_DS(H_0^2) / Lambda_obs = {Lambda_DS_from_H / Lambda_obs_MP4:.2f}")
print(f"  -> O(1) agreement (the DS prediction IS that Lambda ~ H_0^2)")

# =============================================================================
# 7. SIGN REVERSAL ANALYSIS
# =============================================================================
print("\n--- 7. SIGN REVERSAL PREDICTIONS ---")

# DS: Lambda sign flips on timescale ~ H^{-1}
# Number of sign flips since Big Bang ~ t_0 / H_0^{-1} ~ O(1)
# More precisely: number ~ ln(a_0/a_eq) ~ 8 during matter+DE era
t_Hubble = 1.0 / H_0_Planck  # Planck times
print(f"Hubble time: t_H = {t_Hubble:.3e} t_P = {t_Hubble * t_P:.3e} s")
print(f"Number of sign flips since equality: ~ ln(a_0/a_eq) ~ {np.log(1/3e-4):.1f}")
print(f"Expected sign flips in observable history: O(1) to O(10)")
print()
print("Framework: ZERO sign flips. Lambda = const > 0 at all times.")
print("  (q-theory self-tunes to positive value; no mechanism for sign reversal)")

# DS probability that Lambda > 0 now (given Gaussian):
# P(Lambda > 0) = 1/2 (zero-centered Gaussian)
# But CONDITIONED on current expansion rate: P(Lambda > 0 | H > 0) ~ 1
# The observation H > 0 already selects Lambda > 0 realization
print(f"\nDS: P(Lambda > 0 now) = 1/2 a priori, ~1 conditioned on observed H > 0")
print(f"Framework: P(Lambda > 0) = 1 (deterministic)")

# =============================================================================
# 8. CMB IMPLICATIONS
# =============================================================================
print("\n--- 8. CMB/OBSERVATIONAL DISCRIMINANTS ---")

# DS predicts: ISW effect from time-varying Lambda
# Framework: no ISW from Lambda (but possible from KZ defects - ALPHA-PATTERN-43 closed)
print("DS: ISW effect from Lambda(t) variation -> low-l CMB anomalies")
print("Framework: no ISW from Lambda variation (Lambda constant)")
print()

# DS signature in BAO:
# If Lambda varied in past: BAO scale modified
# Sound horizon r_s depends on pre-recombination physics (Lambda subdominant)
# -> DS and Framework give same BAO prediction to O(10^{-6})
print("BAO: Both DS and Framework predict same r_s (Lambda subdominant at z > 1000)")
print()

# Distinctive test: cross-correlation of weak lensing with CMB lensing
# DS: additional scatter from Lambda fluctuations -> decorrelation
# Framework: no additional scatter -> clean cross-correlation
print("Weak lensing x CMB lensing:")
print("  DS: additional decorrelation from stochastic Lambda")
print("  Framework: clean cross-correlation (constant Lambda)")
print("  Discriminating power: requires sub-percent lensing precision (Euclid/LSST)")

# =============================================================================
# 9. GENERATE FIGURE
# =============================================================================
fig = plt.figure(figsize=(14, 10))
gs = GridSpec(2, 2, hspace=0.35, wspace=0.3)

# Panel (a): w(z) comparison
ax1 = fig.add_subplot(gs[0, 0])
ax1.plot(z_arr, w_framework, 'b-', linewidth=2.5, label='Framework (w = -1 exact)')
ax1.plot(z_arr, w_DS, 'r-', linewidth=2.5, label='DS everpresent $\\Lambda$')
ax1.plot(z_arr, w_DESI_central, 'k--', linewidth=1.5, label='DESI DR2 (CPL best fit)')
ax1.fill_between(z_arr, w_DESI_lower, w_DESI_upper, alpha=0.15, color='gray',
                  label='DESI DR2 $1\\sigma$')
ax1.set_xlabel('Redshift z', fontsize=12)
ax1.set_ylabel('w(z)', fontsize=12)
ax1.set_title('(a) Equation of State Comparison', fontsize=13)
ax1.set_xlim(0, 2.5)
ax1.set_ylim(-1.8, -0.2)
ax1.axhline(-1, color='gray', ls=':', alpha=0.5)
ax1.legend(fontsize=9, loc='upper left')
ax1.grid(True, alpha=0.3)

# Panel (b): Lambda magnitude comparison
ax2 = fig.add_subplot(gs[0, 1])
labels = ['$\\Lambda_{\\rm obs}$', '$\\Lambda_{\\rm DS}$\n($H_0^2$)',
          '$\\Lambda_{\\rm FW}$\n(pre-Carlip)', '$\\Lambda_{\\rm FW}$\n(post-Carlip)']
log_values = [np.log10(Lambda_obs_MP4),
              np.log10(Lambda_DS_from_H),
              np.log10(Lambda_framework_gravity),
              np.log10(Lambda_obs_MP4)]  # post-Carlip = obs by construction
colors = ['green', 'red', 'blue', 'cyan']
bars = ax2.bar(labels, log_values, color=colors, alpha=0.7, edgecolor='black')
ax2.set_ylabel('$\\log_{10}(\\Lambda / M_P^4)$', fontsize=12)
ax2.set_title('(b) CC Magnitude (log scale)', fontsize=13)
ax2.axhline(np.log10(Lambda_obs_MP4), color='green', ls='--', alpha=0.5,
            label=f'$\\Lambda_{{obs}}$')
for bar, val in zip(bars, log_values):
    ax2.text(bar.get_x() + bar.get_width()/2., val + 1,
             f'{val:.1f}', ha='center', va='bottom', fontsize=10, fontweight='bold')
ax2.set_ylim(-130, 0)
ax2.grid(True, alpha=0.3, axis='y')

# Panel (c): Exclusion sigma projection
ax3 = fig.add_subplot(gs[1, 0])
# Project sigma_wa improvement with survey progress
years = np.array([2024, 2025, 2026, 2027, 2028, 2029, 2030])
# DESI DR1 (2024): sigma_wa ~ 0.67
# DESI DR2 (2025): sigma_wa ~ 0.28
# DESI DR3 (2026-7): ~ 0.20
# DESI full (2028): ~ 0.11
# Euclid + DESI (2029+): ~ 0.05
sigma_wa_proj = np.array([0.67, 0.28, 0.20, 0.15, 0.11, 0.08, 0.05])
tension_proj = abs(wa_DESI) / sigma_wa_proj

ax3.plot(years, tension_proj, 'ko-', linewidth=2, markersize=8)
ax3.axhline(3, color='orange', ls='--', alpha=0.7, label='$3\\sigma$')
ax3.axhline(5, color='red', ls='--', alpha=0.7, label='$5\\sigma$')
ax3.fill_between([2024, 2030], [5, 5], [12, 12], alpha=0.08, color='red')
ax3.text(2025.5, 5.5, 'Framework excluded', fontsize=10, color='red', alpha=0.7)
ax3.text(2025.5, 2.5, 'Not excluded', fontsize=10, color='green', alpha=0.7)
ax3.set_xlabel('Year', fontsize=12)
ax3.set_ylabel('$|w_a| / \\sigma_{w_a}$ [sigma]', fontsize=12)
ax3.set_title('(c) Framework Exclusion Timeline', fontsize=13)
ax3.set_xlim(2023.5, 2030.5)
ax3.set_ylim(0, 10)
ax3.legend(fontsize=10)
ax3.grid(True, alpha=0.3)
# Mark current status
ax3.annotate('DR2\n(3.1$\\sigma$)', xy=(2025, tension_proj[1]),
             xytext=(2025.5, tension_proj[1]+1.5),
             arrowprops=dict(arrowstyle='->', color='black'),
             fontsize=9, ha='center')

# Panel (d): Structural feature comparison
ax4 = fig.add_subplot(gs[1, 1])
ax4.axis('off')
comparison_data = [
    ['Feature', 'Dowker-Sorkin', 'Framework'],
    ['Lambda nature', 'Stochastic', 'Deterministic'],
    ['Sign reversals', 'Yes (~H$^{-1}$)', 'No'],
    ['w(z)', 'w $\\neq$ -1', 'w = -1 (exact)'],
    ['CC mechanism', '1/$\\sqrt{V}$ Poisson', 'Carlip + q-theory'],
    ['Substrate', 'Causal set', 'M4 x SU(3)'],
    ['Fine-tuning', 'None', 'None (self-tuned)'],
    ['DESI excludes?', 'w = -1 exactly', 'w $\\neq$ -1 at 5$\\sigma$'],
    ['Lorentz inv.', 'Preserved', 'Preserved'],
]
table = ax4.table(cellText=comparison_data[1:], colLabels=comparison_data[0],
                  loc='center', cellLoc='center')
table.auto_set_font_size(False)
table.set_fontsize(9)
table.scale(1.0, 1.6)
# Color header
for j in range(3):
    table[0, j].set_facecolor('#cccccc')
    table[0, j].set_text_props(fontweight='bold')
# Alternate row coloring
for i in range(1, len(comparison_data)):
    for j in range(3):
        if i % 2 == 0:
            table[i, j].set_facecolor('#f0f0f0')
ax4.set_title('(d) Structural Comparison', fontsize=13, pad=20)

fig.suptitle('DS-LAMBDA-43: Dowker-Sorkin vs Framework CC Comparison',
             fontsize=14, fontweight='bold', y=0.98)
plt.savefig('tier0-computation/s43_dowker_sorkin.png', dpi=150, bbox_inches='tight')
print("\nFigure saved: tier0-computation/s43_dowker_sorkin.png")

# =============================================================================
# 10. SAVE RESULTS
# =============================================================================
np.savez('tier0-computation/s43_dowker_sorkin.npz',
    # Gate info
    gate_name='DS-LAMBDA-43',
    verdict='INFO',

    # DS predictions
    Lambda_DS_Planck=Lambda_DS_Planck,
    Lambda_DS_from_H=Lambda_DS_from_H,
    N_elements=N_elements,
    V_4_Planck=V_4_Planck,

    # Framework predictions
    Lambda_framework_gravity=Lambda_framework_gravity,
    Lambda_framework_Kerner=Lambda_framework_Kerner,
    Delta_S=Delta_S,
    S_0=S_0,
    S_fold=S_fold,

    # Observed
    Lambda_obs_MP4=Lambda_obs_MP4,

    # Ratios
    ratio_DS_obs=ratio_DS_obs,
    ratio_DS_FW=ratio_DS_FW,
    suppression_gravity=suppression_gravity,

    # w(z) arrays
    z_arr=z_arr,
    w_DS=w_DS,
    w_framework=w_framework,
    w_DESI_central=w_DESI_central,
    w_DESI_upper=w_DESI_upper,
    w_DESI_lower=w_DESI_lower,

    # Exclusion thresholds
    sigma_wa_DESI_DR2=sigma_wa_DESI,
    sigma_wa_5sigma_threshold=sigma_wa_5sigma,
    tension_wa_current=tension_wa,
    tension_w0_current=tension_w0,

    # Projections
    years_proj=years,
    sigma_wa_proj=sigma_wa_proj,
    tension_proj=tension_proj,

    # Structural
    DS_sign_reversals=True,
    Framework_sign_reversals=False,
    DS_w_prediction='w != -1',
    Framework_w_prediction='w = -1 exact',
)
print("Data saved: tier0-computation/s43_dowker_sorkin.npz")

# =============================================================================
# SUMMARY
# =============================================================================
print("\n" + "=" * 72)
print("DS-LAMBDA-43 SUMMARY")
print("=" * 72)
print(f"""
GATE VERDICT: INFO (structural comparison, no pass/fail applicable)

1. MAGNITUDE COMPARISON:
   Lambda_DS ~ H_0^2 ~ {Lambda_DS_from_H:.2e} M_P^4
   Lambda_framework (pre-Carlip) = {Lambda_framework_gravity:.2e} M_P^4
   Lambda_obs = {Lambda_obs_MP4:.2e} M_P^4

   DS / obs = {Lambda_DS_from_H / Lambda_obs_MP4:.2f} (O(1) -- the DS prediction)
   Framework / obs = {suppression_gravity:.2e} (needs Carlip suppression)

2. STRUCTURAL INCOMPATIBILITY:
   DS: Lambda is STOCHASTIC (Poisson fluctuation of N causal elements)
   Framework: Lambda is DETERMINISTIC (spectral action + q-theory + Carlip)
   These are mutually exclusive ontologies.

3. MUTUAL FALSIFICATION via DESI:
   If DESI confirms w_a != 0 at 5 sigma:
     -> Framework EXCLUDED (predicts w_a = 0 exactly)
     -> DS SURVIVES (accommodates w(z) != -1 naturally)
   If DESI confirms w = -1 exactly:
     -> DS NOT excluded (w = -1 is a particular realization)
     -> Framework SURVIVES

   ASYMMETRY: DS is harder to falsify than framework via w(z) alone.

4. CURRENT STATUS:
   DESI DR2: w_a = -0.86 +/- 0.28 -> {tension_wa:.1f} sigma tension with framework
   Framework NOT YET excluded (need 5 sigma)
   Projected 5-sigma exclusion if central value holds: ~2028-2029 (DESI full)

5. FALSIFICATION THRESHOLD:
   sigma_wa < {sigma_wa_5sigma:.3f} required for 5-sigma framework exclusion
   (factor {sigma_wa_DESI / sigma_wa_5sigma:.1f}x improvement from current DESI DR2)
""")
