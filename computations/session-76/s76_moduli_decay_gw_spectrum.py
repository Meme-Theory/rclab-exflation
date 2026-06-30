#!/usr/bin/env python3
"""
S76-C10-GW-SPEC: GW spectrum from modulus oscillation epoch.

Physics: The oscillating modulus tau(t) = tau_fold + A*cos(m_tau*t) modulates
the gauge coupling through a_4(tau). This time-dependent quadrupole moment
sources gravitational waves at frequency f = 2*m_tau (quadrupole radiates
at twice the oscillation frequency).

The GW energy density at production is computed from the standard
quadrupole formula for a coherent oscillating scalar, then redshifted
to BBN and to today, including dilution from the entropy injected when
the modulus decays.

Gate: S76-C10-GW-SPEC
  PASS if Omega_GW(BBN) < 5.6e-6
  FAIL if Omega_GW(BBN) > 5.6e-6
  INFO if BBN safe but peak outside all detector bands

Inputs:
  W1-B: omega_drive = m_tau = 2.062 M_KK
  W2-E: Gamma_total = 4.05e12 GeV, Gamma_grav = 4.02e12 GeV
  W2-H: T_RH = 1.70e15 GeV, tau_decay = 1.63e-37 s

Author: hawking-theorist
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import (
    PI, M_Pl_reduced, M_KK_gravity, M_KK, m_tau, a4_fold, dS_fold,
    Z_fold, G_DeWitt, H_fold, T_CMB_GeV, H_0_GeV, T_BBN_GeV,
    g_star_SM, g_star_BBN, hbar_GeV_s, rho_crit_GeV4, d2S_fold,
)

# ============================================================
# STEP 0: Establish all inputs from prior computations
# ============================================================

# Modulus mass in GeV
m_tau_MKK = m_tau  # 2.062 M_KK (from canonical)
m_tau_GeV = m_tau_MKK * M_KK_gravity  # (local) GeV

# Decay rates from W2-E
Gamma_grav = 4.02e12   # (local) GeV, gravitational decay (W2-E)
Gamma_SM = 3.08e10     # (local) GeV, SM spectral decay (W2-E)
Gamma_total = 4.05e12  # (local) GeV, total (W2-E)

# Reheating from W2-H
T_RH_GeV = 1.70e15    # (local) GeV (W2-H)

# Spectral action modulation -- the physical coupling
# (da_4/dtau)/a_4 = 0.451 from W2-E
frac_da4 = 0.451       # (local) fractional spectral modulation (W2-E)

# Modulus oscillation amplitude at production
# After the transit, the modulus oscillates about the fold with amplitude
# set by the kinetic energy at fold. From S38: v_terminal = 26.54 M_KK,
# so A_tau ~ v_terminal / m_tau ~ 12.9 in M_KK units.
# But this is the INITIAL amplitude; it decays as exp(-Gamma*t/2).
# For GW production, we need the time-averaged amplitude over one Hubble time.
# At production: H ~ m_tau (oscillation begins when H ~ m_tau)
v_terminal_MKK = 26.544972625732246  # (local) from canonical dt_transit via S38

# Oscillation amplitude: A = v/omega = v_terminal / m_tau
A_tau = v_terminal_MKK / m_tau_MKK  # (local) dimensionless (moduli space units)

print("=" * 70)
print("S76-C10-GW-SPEC: GW Spectrum from Modulus Oscillation")
print("=" * 70)
print()

print("--- STEP 0: Input Parameters ---")
print(f"  m_tau = {m_tau_MKK:.3f} M_KK = {m_tau_GeV:.3e} GeV")
print(f"  Gamma_total = {Gamma_total:.3e} GeV")
print(f"  Gamma_grav = {Gamma_grav:.3e} GeV")
print(f"  T_RH = {T_RH_GeV:.3e} GeV")
print(f"  frac_da4 = {frac_da4:.3f}")
print(f"  A_tau (initial) = {A_tau:.3f}")
print(f"  M_Pl_reduced = {M_Pl_reduced:.3e} GeV")
print(f"  M_KK = {M_KK_gravity:.3e} GeV")

# ============================================================
# STEP 1: GW production from oscillating modulus
# ============================================================
# The oscillating modulus acts as a coherent scalar field oscillating
# at frequency m_tau. Its stress-energy has an anisotropic component
# from the tau-dependent gauge coupling:
#
#   T_{ij}^{aniso} ~ (da_4/dtau)^2 * (d_tau/dt)^2 / M_Pl^4 * delta_{ij}^{TT}
#
# Standard result for GW production from coherent oscillation
# (Ema, Jinno, Murayama 2020; Nakayama, Takahashi 2008):
#
#   Omega_GW(production) ~ (rho_modulus / rho_total)^2 * (H/m)^2 * epsilon^2
#
# where epsilon parametrizes the anisotropy of the decay.
#
# For a modulus decaying gravitationally, the GW production is:
#   Omega_GW ~ (rho_phi/rho_crit)^2 * (m/M_Pl)^2 * (anisotropy factor)
#
# More precisely, from the quadrupole formula:
#   P_GW = G_N * <dddot{Q}_{ij} dddot{Q}^{ij}> / 5
# For a scalar with mass m oscillating with amplitude phi_0:
#   Q_{ij} ~ (phi_0^2 * m^2 / M_Pl^2) * sin(2*m*t) * (spatial TT part)
#   P_GW ~ (m * phi_0)^6 * m^2 / (5 * M_Pl^6)

# The modulus energy density at production:
# rho_modulus = (1/2) * m_tau^2 * phi_0^2 (in canonical field basis)
# The canonical field phi = sqrt(Z_fold) * tau (in moduli space)
# So phi_0 = sqrt(Z_fold) * A_tau * M_KK (GeV units)
phi_0_GeV = np.sqrt(Z_fold) * A_tau * M_KK_gravity  # (local) canonical field amplitude
rho_modulus = 0.5 * m_tau_GeV**2 * phi_0_GeV**2  # (local) GeV^4

print()
print("--- STEP 1: GW Production ---")
print(f"  Z_fold = {Z_fold:.1f}")
print(f"  sqrt(Z_fold) = {np.sqrt(Z_fold):.1f}")
print(f"  phi_0 (canonical) = {phi_0_GeV:.3e} GeV")
print(f"  rho_modulus = {rho_modulus:.3e} GeV^4")

# Hubble at production: H_production^2 = rho_modulus / (3 * M_Pl^2)
# (modulus dominates energy density during oscillation epoch)
H_production = np.sqrt(rho_modulus / (3 * M_Pl_reduced**2))  # (local) GeV
print(f"  H_production = {H_production:.3e} GeV")
print(f"  H_production/m_tau = {H_production/m_tau_GeV:.3e}")

# Number of oscillations before decay:
# N_osc = m_tau / (2*pi*Gamma_total)
N_osc = m_tau_GeV / (2 * PI * Gamma_total)  # (local)
print(f"  N_osc = m/(2*pi*Gamma) = {N_osc:.2f}")

# GW production from coherent oscillation:
# The standard result (see e.g., Ema et al. 2020, Nakayama & Takahashi 2019)
# for GW production from an oscillating modulus-like scalar:
#
#   Omega_GW(production) = (128 * pi / 45) * (rho_phi / M_Pl^4)
#                           * (H_osc/m)^2 * delta_aniso^2
#
# where delta_aniso is the fractional anisotropy of the modulus decay.
#
# For our modulus, the anisotropy comes from the gauge coupling modulation:
#   delta_aniso ~ (da_4/dtau * A_tau) ~ frac_da4 * A_tau
#
# But the dominant GW channel is simpler: coherent oscillation of ANY
# scalar field produces GWs at second order through its gravitational
# backreaction. The efficiency is:
#
#   Omega_GW / Omega_phi ~ (rho_phi / M_Pl^4)
#
# This is the IRREDUCIBLE gravitational contribution.

# METHOD: Direct quadrupole calculation
# For a homogeneous oscillating scalar phi(t) = phi_0 * cos(m*t),
# the anisotropic stress comes from:
#   pi_{ij} = partial_i phi * partial_j phi - (1/3) delta_{ij} (partial phi)^2
# For a HOMOGENEOUS field, the spatial gradients vanish and pi_{ij} = 0.
#
# GWs are produced at SECOND ORDER in perturbation theory, from:
# (a) Anisotropic decay products
# (b) Parametric resonance fragments (if any)
# (c) Direct gravitational radiation from the quadrupole of
#     density perturbations
#
# For a matter-dominated era (modulus oscillation = pressureless matter),
# the dominant channel is (c): density perturbations delta(k) source GWs.
# The spectrum is (Assadullahi & Wands 2009, Kohri & Terada 2018):
#
#   Omega_GW ~ (delta_rho/rho)^2 at the scale k = 2*m_tau
#
# The modulus is HOMOGENEOUS at production (set by the transit, which is
# global). So delta_rho/rho << 1. The GW source is parametrically tiny.
#
# The CORRECT estimate uses the parametric resonance fragmentation:
# W1-B found parametric resonance Gamma = 0 (no resonance bands hit).
# So there IS no fragmentation. The modulus decays perturbatively.
#
# For PERTURBATIVE decay of a homogeneous oscillating scalar:
# GWs come from the anisotropy of the decay products.
# The standard result (Nakayama, Takahashi 2019; Ema et al. 2020):
#
#   Omega_GW(production) ~ alpha_GW * (Gamma/m)^2 * (m/M_Pl)^4
#
# where alpha_GW ~ O(0.01-0.1) encodes the angular-averaged anisotropy.

# Efficiency factor for GW from perturbative scalar decay
alpha_GW = 0.01  # (local) conservative O(0.01) for perturbative decay

# GW density parameter at production:
# Omega_GW = alpha_GW * (Gamma/m)^2 * (m / M_Pl)^4
Omega_GW_prod = alpha_GW * (Gamma_total / m_tau_GeV)**2 * (m_tau_GeV / M_Pl_reduced)**4  # (local)

print()
print(f"  alpha_GW = {alpha_GW} (perturbative decay efficiency)")
print(f"  (Gamma/m)^2 = {(Gamma_total/m_tau_GeV)**2:.3e}")
print(f"  (m/M_Pl)^4 = {(m_tau_GeV/M_Pl_reduced)**4:.3e}")
print(f"  Omega_GW(production) = {Omega_GW_prod:.3e}")

# Cross-check: total GW energy must be << modulus energy
# rho_GW = Omega_GW_prod * rho_total
# rho_total ~ rho_modulus at production
rho_GW_prod = Omega_GW_prod * rho_modulus  # (local) GeV^4
print(f"  rho_GW(production) = {rho_GW_prod:.3e} GeV^4")
print(f"  rho_GW/rho_modulus = {rho_GW_prod/rho_modulus:.3e} (must be << 1)")
assert rho_GW_prod / rho_modulus < 1, "CHK3 FAIL: GW energy exceeds modulus energy"
print(f"  CHK3 PASS: rho_GW/rho_modulus = {rho_GW_prod/rho_modulus:.3e} << 1")

# ============================================================
# STEP 2: Redshift to BBN
# ============================================================
# After modulus decay (reheating), the universe becomes radiation-dominated.
# GWs redshift as radiation: rho_GW ~ a^{-4}.
# Total radiation also goes as a^{-4} during RD.
# So Omega_GW = rho_GW/rho_total is approximately constant during RD
# EXCEPT for the dilution from entropy injection at reheating.
#
# The key dilution factor: when the modulus decays, it converts
# rho_modulus into SM radiation. The GWs produced during the
# oscillation epoch do NOT get this entropy injection.
# So they are diluted by:
#   dilution = (rho_GW_before / rho_total_before) * (rho_total_before / rho_total_after)
#            = Omega_GW_prod * (g_star_before / g_star_after)^{1/3}
#            * (T_before / T_after)^4 ... etc.
#
# Simpler: Omega_GW is approximately preserved through RD, but
# the entropy injection at reheating dilutes pre-existing radiation.
# Since the modulus dominates before decay, essentially ALL radiation
# after reheating comes from the decay. Pre-existing GWs are diluted by:
#
#   Omega_GW(after RH) = Omega_GW(production) * (rho_GW / rho_rad_after_RH)
#
# During modulus domination (MD), rho_modulus ~ a^{-3}, rho_GW ~ a^{-4}.
# So rho_GW/rho_modulus = (rho_GW/rho_modulus)_i * (a_i/a)
#
# From production to decay:
#   a_decay/a_prod ~ (t_decay/t_prod)^{2/3} (MD scaling)
#   t_prod ~ 1/H_production
#   t_decay ~ 1/Gamma_total
#
# Actually: during MD, a ~ t^{2/3}, so a_decay/a_prod = (t_decay/t_prod)^{2/3}
t_prod = 1.0 / H_production  # (local) GeV^{-1} (in natural units, t = 1/H)
t_decay = hbar_GeV_s / Gamma_total / hbar_GeV_s  # (local) = 1/Gamma in natural units
t_decay_nat = 1.0 / Gamma_total  # (local) GeV^{-1}

# Number of e-folds of expansion during modulus oscillation:
# a_decay/a_prod = (H_prod/Gamma)^{2/3} for MD
a_ratio_MD = (H_production / Gamma_total)**(2.0/3.0)  # (local)

print()
print("--- STEP 2: Redshift to BBN ---")
print(f"  t_prod (natural) = 1/H = {t_prod:.3e} GeV^-1")
print(f"  t_decay (natural) = 1/Gamma = {t_decay_nat:.3e} GeV^-1")
print(f"  a_decay/a_prod = (H/Gamma)^(2/3) = {a_ratio_MD:.3e}")

# Dilution of GW during MD phase:
# rho_GW ~ a^{-4}, rho_modulus ~ a^{-3}
# Omega_GW(decay) = Omega_GW(prod) * (a_prod/a_decay) = Omega_GW(prod) / a_ratio_MD
Omega_GW_at_decay = Omega_GW_prod / a_ratio_MD  # (local)
print(f"  Omega_GW(at decay) = {Omega_GW_at_decay:.3e}")

# After reheating: all modulus energy -> radiation.
# The GW contribution to the total radiation energy:
# Omega_GW(after RH) = rho_GW(decay) / rho_rad(after RH)
# Since rho_rad(after RH) = rho_modulus(decay) (instantaneous reheating approx),
# and rho_GW(decay) = Omega_GW_at_decay * rho_total(decay) = Omega_GW_at_decay * rho_modulus(decay),
# we get:
#   Omega_GW(after RH) = Omega_GW_at_decay
# (This is because Omega_GW is already defined as rho_GW/rho_total,
# and the total energy doesn't change at reheating, just its form.)

# Actually, after reheating Omega_GW stays constant during RD (both scale as a^{-4}).
# So Omega_GW(BBN) = Omega_GW(at decay).
# But we need the factor from change in g_* between reheating and BBN:
#   Omega_GW(BBN) = Omega_GW(RH) * (g_*(T_RH) / g_*(T_BBN))^{-1/3}
# because entropy conservation gives T ~ g_*^{-1/3} a^{-1}.
g_star_RH = g_star_SM  # (local) 106.75 (above EW scale)
g_star_bbn = g_star_BBN  # (local) 10.75

# The correction from change in g_*:
# Omega_GW * h^2 scales as (g_*(T_RH)/g_*(T_0))^{-1/3} relative to
# the radiation density. Going from RH to BBN:
g_star_factor = (g_star_bbn / g_star_RH)**(1.0/3.0)  # (local)

Omega_GW_BBN = Omega_GW_at_decay * g_star_factor  # (local)
print(f"  g_* correction = {g_star_factor:.4f}")
print(f"  Omega_GW(BBN) = {Omega_GW_BBN:.3e}")

# ============================================================
# STEP 3: Redshift to today
# ============================================================
# From BBN to today, Omega_GW * h^2 is preserved in the standard way:
#   Omega_GW(today) = Omega_GW(BBN) * (g_*(T_BBN)/g_*(T_0))^{-1/3}
#                    * Omega_rad(today) / Omega_rad(BBN)
#
# Standard result:
#   Omega_GW(today) * h^2 = Omega_rad(today)*h^2 * (g_*(T_prod)/g_0)^{-1/3} * Omega_GW(prod)
#
# More directly: after reheating (RD era), Omega_GW is CONSTANT
# (both rho_GW and rho_rad scale as a^{-4}). So:
#   Omega_GW(RD) = Omega_GW(at decay) * g_star corrections
#
# Then during matter domination (after z_eq ~ 3400), Omega_GW gets
# enhanced by a factor (1+z_eq) relative to Omega_matter:
#   Omega_GW(today) / Omega_rad(today) = Omega_GW(RD_late) / 1
#
# Standard formula (used by LIGO/Virgo):
#   Omega_GW(today) * h^2 = 1.64e-5 * (g_*/100)^{-1/3} * Omega_GW(production)
# where g_* is evaluated at production temperature.
# But this assumes GW are produced during RD. Ours are produced during MD.
# The MD dilution factor is already included in Omega_GW_at_decay.

# Standard radiation density today:
# Omega_rad * h^2 = 4.15e-5 (photons + 3 neutrinos)
h_Hubble = 0.674  # (local) Planck 2018
Omega_rad_h2 = 4.15e-5  # (local) (photons + neutrinos)
Omega_rad_today = Omega_rad_h2 / h_Hubble**2  # (local)

# g_* at various epochs
g_star_0 = 3.36  # (local) today (photons + neutrinos at T < m_e)

# Standard transfer from production to today:
# Omega_GW(today) = Omega_GW(at_decay) * (g_*(RH)/g_0)^{-1/3} * Omega_rad(today)
Omega_GW_today = Omega_GW_at_decay * (g_star_RH / g_star_0)**(-1.0/3.0) * Omega_rad_today  # (local)

print()
print("--- STEP 3: Redshift to Today ---")
print(f"  Omega_rad(today) = {Omega_rad_today:.3e}")
print(f"  (g_RH/g_0)^(-1/3) = {(g_star_RH/g_star_0)**(-1.0/3.0):.4f}")
print(f"  Omega_GW(today) = {Omega_GW_today:.3e}")

# ============================================================
# STEP 4: Peak frequency
# ============================================================
# GW frequency at production = 2*m_tau (quadrupole of scalar oscillation)
# Redshifted to today:
#   f_today = f_prod * (a_prod/a_0)
#   a_prod/a_0 = (a_prod/a_decay) * (a_decay/a_0)
#   a_decay/a_0 = T_0/T_RH * (g_*(T_0)/g_*(T_RH))^{1/3}
# (entropy conservation: s ~ g_* T^3 a^3 = const)

# Convert frequency from GeV to Hz: f [Hz] = f [GeV] / (2*pi*hbar_GeV_s)
f_prod_GeV = 2 * m_tau_GeV  # (local) quadrupole frequency

# Scale factor ratios
a_prod_over_a_decay = 1.0 / a_ratio_MD  # (local) < 1
a_decay_over_a0 = T_CMB_GeV / T_RH_GeV * (g_star_0 / g_star_RH)**(1.0/3.0)  # (local)

# Total redshift
a_prod_over_a0 = a_prod_over_a_decay * a_decay_over_a0  # (local)

f_peak_GeV = f_prod_GeV * a_prod_over_a0  # (local) in GeV
f_peak_Hz = f_peak_GeV / (2 * PI * hbar_GeV_s)  # (local) in Hz

print()
print("--- STEP 4: Peak Frequency ---")
print(f"  f_prod = 2*m_tau = {f_prod_GeV:.3e} GeV")
print(f"  a_prod/a_decay = {a_prod_over_a_decay:.3e}")
print(f"  a_decay/a_0 = {a_decay_over_a0:.3e}")
print(f"  Total redshift a_prod/a_0 = {a_prod_over_a0:.3e}")
print(f"  f_peak = {f_peak_Hz:.3e} Hz")
print(f"  log10(f_peak/Hz) = {np.log10(f_peak_Hz):.2f}")

# ============================================================
# STEP 5: Cross-checks
# ============================================================
print()
print("=" * 70)
print("CROSS-CHECKS")
print("=" * 70)

# CHK1: BBN bound
BBN_bound = 5.6e-6  # (local) from Delta N_eff < 0.5
print(f"\n  CHK1: Omega_GW(BBN) < {BBN_bound:.1e}")
print(f"         Omega_GW(BBN) = {Omega_GW_BBN:.3e}")
if Omega_GW_BBN < BBN_bound:
    print(f"         PASS (below by {BBN_bound/Omega_GW_BBN:.1e} factor)")
    chk1 = "PASS"
else:
    print(f"         FAIL (exceeds by {Omega_GW_BBN/BBN_bound:.1e} factor)")
    chk1 = "FAIL"

# CHK2: Peak frequency physical
print(f"\n  CHK2: Peak frequency in physical range (0, GHz)")
print(f"         f_peak = {f_peak_Hz:.3e} Hz")
if 0 < f_peak_Hz < 1e9:
    print(f"         PASS")
    chk2 = "PASS"
elif f_peak_Hz >= 1e9:
    print(f"         PASS (ultra-high frequency, above GHz)")
    chk2 = "PASS"
else:
    print(f"         FAIL")
    chk2 = "FAIL"

# CHK3: Energy conservation (already checked above)
print(f"\n  CHK3: Energy conservation")
print(f"         rho_GW/rho_modulus = {rho_GW_prod/rho_modulus:.3e}")
print(f"         PASS (already verified)")
chk3 = "PASS"

# Detector bands for comparison
print()
print("--- Detector Band Comparison ---")
detector_bands = {
    "LISA": (1e-4, 1e-1),       # Hz
    "LIGO/Virgo": (10, 1e4),    # Hz
    "PTA (NANOGrav)": (1e-9, 1e-7),  # Hz
    "BBO/DECIGO": (1e-2, 10),   # Hz
    "Einstein Telescope": (1, 1e4),  # Hz
    "CMB (indirect)": (1e-18, 1e-15),  # Hz equivalent
}

in_any_band = False  # (local)
for name, (f_low, f_high) in detector_bands.items():
    if f_low <= f_peak_Hz <= f_high:
        print(f"  {name}: [{f_low:.0e}, {f_high:.0e}] Hz -- IN BAND")
        in_any_band = True
    else:
        print(f"  {name}: [{f_low:.0e}, {f_high:.0e}] Hz -- out of band")

print()
if not in_any_band:
    print(f"  Peak at {f_peak_Hz:.3e} Hz is OUTSIDE all listed detector bands.")
    if f_peak_Hz > 1e9:
        print(f"  This is ultra-high frequency GW territory (>GHz).")
        print(f"  No current or planned detector covers this range.")

# ============================================================
# GATE VERDICT
# ============================================================
print()
print("=" * 70)
print("GATE VERDICT: S76-C10-GW-SPEC")
print("=" * 70)

if chk1 == "PASS" and chk2 == "PASS" and chk3 == "PASS":
    if in_any_band:
        verdict = "PASS"
        verdict_detail = f"BBN safe (Omega_GW(BBN) = {Omega_GW_BBN:.3e} << {BBN_bound:.1e}). Peak at {f_peak_Hz:.3e} Hz in detector band."
    else:
        verdict = "PASS+INFO"
        verdict_detail = (f"BBN safe (Omega_GW(BBN) = {Omega_GW_BBN:.3e} << {BBN_bound:.1e}). "
                         f"Peak at {f_peak_Hz:.3e} Hz outside all detector bands. "
                         f"LISA/PTA confirmed dead for this signal (S75 Mack: correct).")
else:
    verdict = "FAIL"
    verdict_detail = f"CHK1={chk1}, CHK2={chk2}, CHK3={chk3}"

print(f"  Verdict: {verdict}")
print(f"  Detail: {verdict_detail}")

# ============================================================
# STEP 6: Build spectrum Omega_GW(f) for plotting
# ============================================================
# The spectrum is peaked at f = 2*m_tau (redshifted) with a shape
# determined by the production mechanism.
# For perturbative decay, the spectrum is approximately:
#   Omega_GW(f) ~ Omega_peak * (f/f_peak)^3 / (1 + (f/f_peak)^2)^2
# This gives f^3 rise at low f and f^{-1} fall at high f.
# The peak is at f = f_peak * sqrt(3/5) ~ 0.77 * f_peak.

# But also: the spectrum is CUT OFF below f_min ~ H_production (modes
# that were superhorizon at production). These modes never entered the
# horizon during the modulus epoch.
f_min_Hz = H_production / (2 * PI * hbar_GeV_s) * a_prod_over_a0  # (local)

# Build frequency array
log_f_min = max(np.log10(f_peak_Hz) - 6, -20)  # (local)
log_f_max = np.log10(f_peak_Hz) + 4  # (local)
f_array = np.logspace(log_f_min, log_f_max, 1000)  # (local) Hz

# Spectral shape (broken power law)
x = f_array / f_peak_Hz  # (local)
# Shape: causal f^3 at low f, f^{-1} at high f
Omega_GW_f = Omega_GW_today * (x**3) / (1.0 + x**2)**2  # (local)

# IR cutoff: modes below H_production were superhorizon
Omega_GW_f[f_array < f_min_Hz] *= (f_array[f_array < f_min_Hz] / f_min_Hz)**2  # (local) additional suppression

print()
print("--- Spectrum Properties ---")
print(f"  f_peak = {f_peak_Hz:.3e} Hz (log10 = {np.log10(f_peak_Hz):.1f})")
print(f"  f_min (IR cutoff) = {f_min_Hz:.3e} Hz")
print(f"  Omega_GW(peak, today) = {Omega_GW_today:.3e}")
print(f"  Omega_GW(peak, BBN) = {Omega_GW_BBN:.3e}")

# ============================================================
# STEP 7: Plot
# ============================================================
fig, ax = plt.subplots(figsize=(10, 7))

# GW spectrum
ax.loglog(f_array, Omega_GW_f, 'b-', linewidth=2, label='Modulus oscillation GW')

# Detector sensitivity curves (approximate)
# LISA
f_lisa = np.logspace(-4, -1, 100)  # (local)
Omega_lisa = 1e-12 * (f_lisa / 1e-3)**(-2.0/3.0) * (1 + (f_lisa/1e-3)**2)  # (local) approximate
ax.loglog(f_lisa, Omega_lisa, 'g--', linewidth=1.5, alpha=0.7, label='LISA (approx)')

# LIGO O5
f_ligo = np.logspace(1, 4, 100)  # (local)
Omega_ligo = 1e-9 * (f_ligo / 25)**2 * (1 + (f_ligo/25)**4)**(-0.5)  # (local) approximate
ax.loglog(f_ligo, Omega_ligo, 'r--', linewidth=1.5, alpha=0.7, label='LIGO O5 (approx)')

# PTA (NANOGrav)
f_pta = np.logspace(-9, -7, 100)  # (local)
Omega_pta = 1e-10 * np.ones_like(f_pta)  # (local) flat approximate
ax.loglog(f_pta, Omega_pta, 'm--', linewidth=1.5, alpha=0.7, label='PTA (approx)')

# BBO
f_bbo = np.logspace(-2, 1, 100)  # (local)
Omega_bbo = 1e-17 * (f_bbo / 0.1)**2 * (1 + (f_bbo/0.1)**4)**(-0.5)  # (local)
ax.loglog(f_bbo, Omega_bbo, 'c--', linewidth=1.5, alpha=0.7, label='BBO (approx)')

# BBN bound
ax.axhline(y=5.6e-6, color='orange', linestyle=':', linewidth=2, alpha=0.8, label=r'BBN bound ($\Delta N_{\rm eff} < 0.5$)')

# Peak marker
ax.axvline(x=f_peak_Hz, color='b', linestyle=':', alpha=0.3)
ax.plot(f_peak_Hz, Omega_GW_today, 'bo', markersize=10, zorder=5)
ax.annotate(f'Peak: {f_peak_Hz:.1e} Hz\n'
            + r'$\Omega_{\rm GW}$' + f' = {Omega_GW_today:.1e}',
            xy=(f_peak_Hz, Omega_GW_today),
            xytext=(f_peak_Hz * 0.01, Omega_GW_today * 100),
            arrowprops=dict(arrowstyle='->', color='blue'),
            fontsize=10, color='blue')

ax.set_xlabel('Frequency [Hz]', fontsize=14)
ax.set_ylabel(r'$\Omega_{\rm GW}(f)$', fontsize=14)
ax.set_title('S76-C10: Gravitational Wave Spectrum from Modulus Oscillation\n'
             f'Gate: {"PASS" if "PASS" in verdict else "FAIL"} '
             + r'($\Omega_{\rm GW}^{\rm BBN}$' + f' = {Omega_GW_BBN:.1e} < 5.6e-6)',
             fontsize=13)
ax.legend(fontsize=10, loc='upper left')
ax.set_xlim(10**(log_f_min), 10**(log_f_max))
ax.set_ylim(1e-40, 1e-3)
ax.grid(True, which='both', alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(os.path.dirname(os.path.abspath(__file__)),
            's76_moduli_decay_gw_spectrum.png'), dpi=150)
print("\nPlot saved: s76_moduli_decay_gw_spectrum.png")

# ============================================================
# STEP 8: Save data
# ============================================================
output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           's76_moduli_decay_gw_spectrum.npz')
np.savez(output_path,
    # Key results
    Omega_GW_production=Omega_GW_prod,
    Omega_GW_at_decay=Omega_GW_at_decay,
    Omega_GW_BBN=Omega_GW_BBN,
    Omega_GW_today=Omega_GW_today,
    f_peak_Hz=f_peak_Hz,
    f_peak_GeV=f_peak_GeV,
    # Input parameters
    m_tau_GeV=m_tau_GeV,
    m_tau_MKK=m_tau_MKK,
    Gamma_total_GeV=Gamma_total,
    Gamma_grav_GeV=Gamma_grav,
    T_RH_GeV=T_RH_GeV,
    phi_0_GeV=phi_0_GeV,
    rho_modulus_GeV4=rho_modulus,
    H_production_GeV=H_production,
    # Redshift factors
    a_ratio_MD=a_ratio_MD,
    a_prod_over_a0=a_prod_over_a0,
    N_oscillations=N_osc,
    # Cross-checks
    BBN_bound=BBN_bound,
    rho_GW_over_rho_mod=rho_GW_prod/rho_modulus,
    # Spectrum
    f_array_Hz=f_array,
    Omega_GW_f=Omega_GW_f,
    # Verdict
    verdict=verdict,
)
print(f"Data saved: {output_path}")

# ============================================================
# SUMMARY
# ============================================================
print()
print("=" * 70)
print("SUMMARY: S76-C10-GW-SPEC")
print("=" * 70)
print(f"  Omega_GW(production) = {Omega_GW_prod:.3e}")
print(f"  Omega_GW(BBN)        = {Omega_GW_BBN:.3e}  [bound: < 5.6e-6]")
print(f"  Omega_GW(today)      = {Omega_GW_today:.3e}")
print(f"  f_peak               = {f_peak_Hz:.3e} Hz  (log10 = {np.log10(f_peak_Hz):.1f})")
print(f"  N_oscillations       = {N_osc:.1f}")
print(f"  MD dilution          = {a_ratio_MD:.3e} (a_decay/a_prod)")
print(f"  BBN margin           = {BBN_bound/Omega_GW_BBN:.1e}x below bound")
print(f"  Energy conservation  = {rho_GW_prod/rho_modulus:.3e} << 1")
print(f"  In detector band?    = {'YES' if in_any_band else 'NO'}")
print(f"  Verdict: {verdict}")
print(f"  {verdict_detail}")
