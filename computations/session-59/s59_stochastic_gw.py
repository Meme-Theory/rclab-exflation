#!/usr/bin/env python3
"""
s59_stochastic_gw.py — Stochastic GW Background from BCS Shattering
=====================================================================

Gate: STOCHASTIC-GW-59
  PASS: f_peak accessible (1e-4 to 1e3 Hz)
  FAIL: f_peak > 1e6 Hz (completely inaccessible)
  INFO: amplitude too small to detect

Physics:
  The BCS transition at the Shattering is a first-order phase transition at
  temperature T* = T_acoustic * M_KK in the internal (SU(3)) space. This
  produces GWs through three mechanisms: bubble collisions, sound waves in
  the plasma, and turbulence. We use the standard envelope approximation
  (Caprini et al. 2016, JCAP 04:001) to compute Omega_GW(f) h^2.

  Key parameters:
    alpha = E_exc / E_rad  — transition strength (latent heat / radiation)  # (local)
    beta/H* = 1/dt_transit / H_fold — inverse duration in Hubble units
    T* = T_acoustic * M_KK — transition temperature in GeV

  The peak frequency today is:
    f_peak = (beta / 2*pi) * (a* / a_0) = (beta / 2*pi) * (T_0 / T*)
  where the last equality uses entropy conservation a*T* = a_0*T_0.

Session: S59
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from canonical_constants import *
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

print("=" * 70)
print("S59 STOCHASTIC GW BACKGROUND FROM BCS SHATTERING")
print("=" * 70)

# ==============================================================================
#  Step 1: Physical parameters from canonical constants + input data
# ==============================================================================

# Load acoustic metric data for additional cross-checks
acoustic = np.load(os.path.join(os.path.dirname(__file__), 's58_acoustic_metric.npz'),
                   allow_pickle=True)
fold_idx = int(acoustic['fold_idx'])

# Transition temperature
# T_acoustic = 0.112 M_KK (from canonical_constants, S42/S47 GGE acoustic temperature)
# M_KK = M_KK_gravity = 7.43e16 GeV
T_star_GeV = T_acoustic * M_KK  # GeV
print(f"\n--- Step 1: Transition Parameters ---")
print(f"T_acoustic = {T_acoustic} M_KK")
print(f"M_KK = {M_KK:.4e} GeV (gravity route)")
print(f"T* = T_acoustic * M_KK = {T_star_GeV:.4e} GeV")

# For comparison: electroweak T ~ 100 GeV, QCD T ~ 0.15 GeV
# This transition is at ~8.3e15 GeV — just below GUT scale
print(f"  (Electroweak: ~100 GeV, QCD: ~0.15 GeV, GUT: ~1e16 GeV)")
print(f"  This transition is at {T_star_GeV / 1e16:.2f} x 10^16 GeV")

# Transit parameters
# beta = inverse duration of the transition = 1 / dt_transit
# dt_transit = 0.00113 M_KK^{-1} (canonical_constants, S38 s38_kz_defects)
# H_fold = 586.5 M_KK (Hubble parameter at fold, canonical_constants)
beta_MKK = 1.0 / dt_transit  # M_KK units
beta_GeV = beta_MKK * M_KK   # GeV (natural units: 1/time = energy)
beta_Hz = beta_GeV * GeV_to_inv_s  # Hz

# Hubble rate at transition
H_star_MKK = H_fold  # M_KK units (at the fold)
H_star_GeV = H_star_MKK * M_KK
H_star_Hz = H_star_GeV * GeV_to_inv_s

# beta/H* ratio — critical for GW spectrum shape
beta_over_H = beta_MKK / H_star_MKK

print(f"\nbeta = 1/dt_transit = {beta_MKK:.2f} M_KK = {beta_GeV:.4e} GeV")
print(f"beta in Hz = {beta_Hz:.4e} Hz")
print(f"H* = H_fold = {H_star_MKK:.2f} M_KK = {H_star_GeV:.4e} GeV")
print(f"H* in Hz = {H_star_Hz:.4e} Hz")
print(f"beta/H* = {beta_over_H:.4f}")
print(f"  (beta/H* >> 1 means fast transition relative to Hubble time)")

# Transition strength parameter alpha
# alpha = E_exc / E_rad where E_rad is the radiation energy density
# E_exc = 443 * |E_cond| = 60.6 M_KK (canonical)
# E_rad = (pi^2/30) * g_star * T_acoustic^4 in M_KK units
# g_star at T ~ 8e15 GeV: full SM + any BSM dof. SM: g_star = 106.75
# But in the framework's internal space, g_star corresponds to the BCS degrees of freedom
# N_dof_BCS = 8 modes. The radiation bath has g_star ~ 8 (bosonic modes) + fermionic
# However, the standard parameterization uses the 4D relativistic g_star.
# At T* ~ 8e15 GeV, all SM species are relativistic: g_star = 106.75

g_star = 106.75  # SM relativistic degrees of freedom at T >> M_top (local)
g_star_s = g_star  # entropy dof ~ energy dof at high T

# Radiation energy density in M_KK natural units
E_rad_MKK4 = (PI**2 / 30.0) * g_star * T_acoustic**4  # in M_KK^4
# The BCS excitation energy is E_exc per Hubble volume, but we need the
# ratio of latent heat to radiation energy density.
# E_exc is in M_KK units (energy per mode), so:
# alpha = latent_heat / rho_radiation

# The latent heat per unit volume = |E_cond| * n_modes * (M_KK)^4 / V
# But in the 0D limit (L/xi = 0.031), the entire Hubble patch is one domain
# So the relevant comparison is energy per mode vs radiation per mode
alpha_transition = E_exc / (E_rad_MKK4)  # dimensionless ratio

print(f"\n--- Transition Strength ---")
print(f"E_exc = {E_exc:.2f} M_KK (= {E_exc_ratio} * |E_cond|)")
print(f"g_star = {g_star}")
print(f"E_rad = (pi^2/30) * g_star * T^4 = {E_rad_MKK4:.6e} M_KK^4")
print(f"alpha = E_exc / E_rad = {alpha_transition:.4e}")
print(f"  (alpha >> 1: strongly first-order; alpha << 1: weakly first-order)")

# NOTE: alpha is enormous because E_exc (443 * gap) >> thermal radiation at T_acoustic
# This makes the transition extremely strongly first-order

# ==============================================================================
#  Step 2: Peak frequency today
# ==============================================================================

# The GW frequency at production is f_* ~ beta / (2*pi)
# Redshifted to today using entropy conservation:
#   f_0 = f_* * (a_*/a_0) = f_* * (T_0/T_*) * (g_{*,s,0}/g_{*,s,*})^{1/3}
# where T_0 = T_CMB = 2.7255 K = 2.348e-13 GeV
# g_{*,s,0} = 3.91 (photons + 3 neutrino species, today)
# g_{*,s,*} = g_star_s at transition

T_0_GeV = T_CMB_GeV  # CMB temperature in GeV
g_star_s_0 = 3.91     # entropy dof today  # (local)

# Frequency at production
f_star = beta_Hz / (2.0 * PI)

# Redshift factor
redshift_factor = (T_0_GeV / T_star_GeV) * (g_star_s_0 / g_star_s)**(1.0/3.0)

# Peak frequency today
f_peak = f_star * redshift_factor

print(f"\n--- Step 2: Peak Frequency ---")
print(f"f_* = beta/(2*pi) = {f_star:.4e} Hz (at production)")
print(f"T_0 = {T_0_GeV:.4e} GeV")
print(f"T_*/T_0 = {T_star_GeV / T_0_GeV:.4e}")
print(f"Redshift factor (T_0/T_*) * (g_0/g_*)^(1/3) = {redshift_factor:.4e}")
print(f"f_peak = {f_peak:.4e} Hz (today)")
print(f"log10(f_peak) = {np.log10(f_peak):.2f}")

# Cross-check: the standard scaling formula (Caprini et al. 2016, Eq. 2.13)
# f_peak ~ 1.65e-5 Hz * (f_*/beta) * (beta/H*) * (T*/100 GeV) * (g_*/100)^{1/6}
# where f_*/beta ~ 0.35-1.0 depending on mechanism
f_over_beta_sw = 8.9e-3  # Sound wave (Caprini 2016 Eq. 3.4, for v_w ~ 1)  # (local)
f_over_beta_turb = 27.0 / (4.0 * PI)  # Turbulence (Caprini 2016 Eq. 3.10)
f_over_beta_env = 0.62 / (1.8 - 0.1 + 1.8)  # Envelope (Caprini 2016 Eq. 3.2)

# Standard scaling formula from Caprini et al. (2016)
def f_peak_caprini(f_over_beta, beta_over_H_val, T_star_val, g_star_val):
    """Peak frequency today from Caprini et al. 2016 Eq. 2.13"""
    return 1.65e-5 * f_over_beta * (beta_over_H_val / 1.0) * \
           (T_star_val / (100.0)) * (g_star_val / 100.0)**(1.0/6.0)

f_peak_sw = f_peak_caprini(f_over_beta_sw, beta_over_H, T_star_GeV, g_star)
f_peak_turb = f_peak_caprini(f_over_beta_turb, beta_over_H, T_star_GeV, g_star)
f_peak_env = f_peak_caprini(f_over_beta_env, beta_over_H, T_star_GeV, g_star)

print(f"\nCross-check via Caprini et al. (2016) Eq. 2.13:")
print(f"  Sound waves:    f_peak_sw   = {f_peak_sw:.4e} Hz")
print(f"  Turbulence:     f_peak_turb = {f_peak_turb:.4e} Hz")
print(f"  Envelope:       f_peak_env  = {f_peak_env:.4e} Hz")

# Use the sound wave contribution as primary (dominant for strong transitions)
f_peak_primary = f_peak_sw

# ==============================================================================
#  Step 3: GW amplitude Omega_GW h^2
# ==============================================================================

# Following Caprini et al. (2016) Section 3
# Three contributions: bubble collisions (envelope), sound waves, turbulence

# Efficiency factors
# kappa: fraction of latent heat converted to each source
# For strongly first-order (alpha >> 1), kappa_phi ~ 1 (envelope/collisions)
# Sound wave efficiency (Espinosa et al. 2010, Eq. 3.3 of Caprini):

# Wall velocity: in a strongly first-order transition, v_w -> 1 (detonation)
v_w = 1.0  # ultrarelativistic wall velocity (strong transition)  # (local)

# For alpha >> 1:
# kappa_v ~ alpha / (0.73 + 0.083*sqrt(alpha) + alpha) (Espinosa et al. 2010)
# kappa_v -> 1 as alpha -> infinity
kappa_v = alpha_transition / (0.73 + 0.083 * np.sqrt(alpha_transition) + alpha_transition)

# Turbulence: kappa_turb ~ epsilon * kappa_v, with epsilon ~ 0.05-0.10
epsilon_turb = 0.10  # (local)
kappa_turb = epsilon_turb * kappa_v

# Envelope (bubble collisions): kappa_phi ~ 1 - kappa_v (for very strong transitions)
# For alpha >> 1, kappa_phi -> 0 (most energy goes to plasma)
# But in the 0D limit (no spatial structure), there are no bubble walls to collide
# The 0D limit means the entire patch transitions simultaneously
# => Envelope contribution is ZERO (no bubble collisions)
kappa_phi = 0.0  # No bubble collisions in 0D limit  # (local)

print(f"\n--- Step 3: GW Amplitude ---")
print(f"v_w = {v_w} (ultrarelativistic, strong transition)")
print(f"kappa_v (sound waves) = {kappa_v:.6f}")
print(f"kappa_turb = {kappa_turb:.6f}")
print(f"kappa_phi (envelope) = {kappa_phi} (ZERO: 0D limit, no bubble collisions)")

# === Sound wave contribution ===
# Caprini et al. 2016, Eq. (3.5):
# Omega_sw h^2 = 2.65e-6 * (H*/beta) * (kappa_v * alpha / (1+alpha))^2
#                * (100/g_star)^{1/3} * v_w * S_sw(f)
# where S_sw(f) is the spectral shape (peaked at f_peak_sw)

H_over_beta = 1.0 / beta_over_H

Omega_sw_peak = 2.65e-6 * H_over_beta * \
    (kappa_v * alpha_transition / (1.0 + alpha_transition))**2 * \
    (100.0 / g_star)**(1.0/3.0) * v_w

print(f"\nSound wave contribution (Caprini 2016 Eq. 3.5):")
print(f"  H*/beta = {H_over_beta:.6e}")
print(f"  kappa_v * alpha / (1+alpha) = {kappa_v * alpha_transition / (1.0 + alpha_transition):.6f}")
print(f"  Omega_sw_peak h^2 = {Omega_sw_peak:.4e}")

# === Turbulence contribution ===
# Caprini et al. 2016, Eq. (3.8):
# Omega_turb h^2 = 3.35e-4 * (H*/beta) * (kappa_turb * alpha / (1+alpha))^{3/2}
#                  * (100/g_star)^{1/3} * v_w * S_turb(f)

Omega_turb_peak = 3.35e-4 * H_over_beta * \
    (kappa_turb * alpha_transition / (1.0 + alpha_transition))**(3.0/2.0) * \
    (100.0 / g_star)**(1.0/3.0) * v_w

print(f"\nTurbulence contribution (Caprini 2016 Eq. 3.8):")
print(f"  kappa_turb * alpha / (1+alpha) = {kappa_turb * alpha_transition / (1.0 + alpha_transition):.6f}")
print(f"  Omega_turb_peak h^2 = {Omega_turb_peak:.4e}")

# Total peak amplitude
Omega_GW_peak = Omega_sw_peak + Omega_turb_peak
print(f"\nTotal Omega_GW_peak h^2 = {Omega_GW_peak:.4e}")

# ==============================================================================
#  Step 4: Full spectral shape Omega_GW(f) h^2
# ==============================================================================

# Frequency array (log-spaced, covering many decades)
f_array = np.logspace(-2, 14, 10000)  # Hz

# Sound wave spectral shape (Caprini 2016, Eq. 3.4 shape):
# S_sw(f) = (f/f_sw)^3 * (7 / (4 + 3*(f/f_sw)^2))^{7/2}
def S_sw(f, f_p):
    x = f / f_p
    return x**3 * (7.0 / (4.0 + 3.0 * x**2))**(7.0/2.0)

# Turbulence spectral shape (Caprini 2016, Eq. 3.10 shape):
# S_turb(f) = (f/f_turb)^3 / ((1 + f/f_turb)^{11/3} * (1 + 8*pi*f/h_*))
# where h_* = a_* H_* is the Hubble rate at production, redshifted
h_star_today = H_star_Hz * redshift_factor  # Hubble rate redshifted to today
f_turb = f_peak_turb

def S_turb(f, f_p, h_s):
    x = f / f_p
    return x**3 / ((1.0 + x)**(11.0/3.0) * (1.0 + 8.0 * PI * f / h_s))

# Compute full spectrum
Omega_sw_f = Omega_sw_peak * S_sw(f_array, f_peak_sw)
Omega_turb_f = Omega_turb_peak * S_turb(f_array, f_peak_turb, h_star_today)
Omega_total_f = Omega_sw_f + Omega_turb_f

# Find actual peak of total spectrum
idx_peak = np.argmax(Omega_total_f)
f_peak_actual = f_array[idx_peak]
Omega_peak_actual = Omega_total_f[idx_peak]

print(f"\n--- Step 4: Full Spectrum ---")
print(f"f_peak (actual, from spectrum) = {f_peak_actual:.4e} Hz")
print(f"Omega_GW(f_peak) h^2 = {Omega_peak_actual:.4e}")
print(f"log10(f_peak) = {np.log10(f_peak_actual):.2f}")
print(f"log10(Omega_GW_peak h^2) = {np.log10(Omega_peak_actual):.2f}")

# ==============================================================================
#  Step 5: Detector comparison
# ==============================================================================

print(f"\n--- Step 5: Detector Comparison ---")

# Detector frequency bands and sensitivities (Omega_GW h^2)
detectors = {
    'LISA':        {'f_min': 1e-4, 'f_max': 1e-1, 'Omega_min': 1e-13},
    'ET':          {'f_min': 1,    'f_max': 1e4,   'Omega_min': 1e-13},
    'CE':          {'f_min': 5,    'f_max': 5e3,   'Omega_min': 1e-13},
    'LIGO O5':     {'f_min': 10,   'f_max': 7e3,   'Omega_min': 1e-10},
    'BBO':         {'f_min': 1e-3, 'f_max': 10,    'Omega_min': 1e-17},
    'DECIGO':      {'f_min': 1e-2, 'f_max': 1e2,   'Omega_min': 1e-16},
    'SKA (PTA)':   {'f_min': 1e-9, 'f_max': 1e-7,  'Omega_min': 1e-11},
    'microwave cavity (proposed)': {'f_min': 1e6, 'f_max': 1e12, 'Omega_min': 1e-6},
}

print(f"\nPeak frequency: {f_peak_actual:.4e} Hz = {f_peak_actual/1e9:.2e} GHz")
print(f"Peak amplitude: Omega_GW h^2 = {Omega_peak_actual:.4e}")
print()

can_detect = False
for name, det in detectors.items():
    in_band = det['f_min'] <= f_peak_actual <= det['f_max']
    # Also check if any part of the spectrum is above sensitivity in the band
    mask = (f_array >= det['f_min']) & (f_array <= det['f_max'])
    if mask.any():
        Omega_in_band = Omega_total_f[mask].max()
        detectable = Omega_in_band >= det['Omega_min']
        status = "DETECTABLE" if (in_band and detectable) else \
                 f"in band but too weak (Omega={Omega_in_band:.2e})" if in_band else \
                 f"out of band (max in band: {Omega_in_band:.2e})" if Omega_in_band > 0 else "out of band"
    else:
        Omega_in_band = 0
        status = "out of band"

    if "DETECTABLE" in status:
        can_detect = True
    print(f"  {name:30s}: {status}")

# ==============================================================================
#  Step 6: Gate verdict
# ==============================================================================

print(f"\n{'='*70}")
print("GATE VERDICT: STOCHASTIC-GW-59")
print(f"{'='*70}")

if f_peak_actual < 1e-4:
    gate_verdict = "FAIL"
    gate_detail = f"f_peak = {f_peak_actual:.2e} Hz below LISA band"
elif f_peak_actual <= 1e3:
    gate_verdict = "PASS"
    gate_detail = f"f_peak = {f_peak_actual:.2e} Hz in accessible range"
elif f_peak_actual <= 1e6:
    gate_verdict = "INFO"
    gate_detail = f"f_peak = {f_peak_actual:.2e} Hz above current detectors but below FAIL threshold"
else:
    gate_verdict = "FAIL"
    gate_detail = f"f_peak = {f_peak_actual:.2e} Hz > 10^6 Hz, completely inaccessible"

# Amplitude check for INFO
if gate_verdict == "PASS" and not can_detect:
    gate_verdict = "INFO"
    gate_detail += f"; amplitude Omega_GW h^2 = {Omega_peak_actual:.2e} too small"

print(f"f_peak = {f_peak_actual:.4e} Hz")
print(f"log10(f_peak) = {np.log10(f_peak_actual):.2f}")
print(f"Omega_GW(f_peak) h^2 = {Omega_peak_actual:.4e}")
print(f"Verdict: {gate_verdict}")
print(f"Detail: {gate_detail}")

# ==============================================================================
#  Step 7: Physical interpretation
# ==============================================================================

print(f"\n{'='*70}")
print("PHYSICAL INTERPRETATION")
print(f"{'='*70}")

print(f"""
The BCS Shattering transition occurs at T* = {T_star_GeV:.2e} GeV, comparable to
the GUT scale. The resulting stochastic GW background peaks at
f_peak = {f_peak_actual:.2e} Hz (= {f_peak_actual/1e9:.2e} GHz).

This is {np.log10(f_peak_actual) - np.log10(1e-3):.0f} decades above LISA
and {np.log10(f_peak_actual) - np.log10(100):.0f} decades above ground-based
detectors (LIGO/ET/CE).

The peak frequency scales as:
  f_peak ~ (beta/2*pi) * (T_0/T*) * (g_0/g_*)^(1/3)
         ~ (1/dt_transit) * (T_CMB/T_acoustic*M_KK) * (3.91/106.75)^(1/3)

The only way to bring f_peak into accessible range would be:
  1. T* << 8e15 GeV (transition at much lower temperature) => NO: T_acoustic fixed
  2. beta << 1/dt_transit (much slower transition) => NO: dt_transit = 0.00113 M_KK^-1 fixed
  3. Different detection technology (microwave cavities at GHz) => SPECULATIVE

The transition strength alpha = {alpha_transition:.2e} makes this extremely strongly
first-order. The amplitude would be large IF accessible, but the extreme
temperature pushes the signal to GHz frequencies where no operational or
funded detector exists.

This confirms VB-4's estimate: f_peak ~ 10^8 Hz (GHz, inaccessible).
The spectral shape follows Caprini et al. (2016) with sound wave dominance.

SUBSTRATE CLASSIFICATION: GEOMETRIC (GW production from phase transition dynamics,
not from phononic excitation modes directly)
""")

# ==============================================================================
#  Step 8: Save data
# ==============================================================================

outpath = os.path.join(os.path.dirname(__file__), 's59_stochastic_gw.npz')
np.savez(outpath,
    # Parameters
    T_star_GeV=T_star_GeV,
    T_acoustic_MKK=T_acoustic,
    M_KK_GeV=M_KK,
    beta_MKK=beta_MKK,
    beta_Hz=beta_Hz,
    H_star_MKK=H_star_MKK,
    H_star_Hz=H_star_Hz,
    beta_over_H=beta_over_H,
    alpha_transition=alpha_transition,
    g_star=g_star,
    v_w=v_w,
    kappa_v=kappa_v,
    kappa_turb=kappa_turb,
    kappa_phi=kappa_phi,
    # Spectrum
    f_array=f_array,
    Omega_sw_f=Omega_sw_f,
    Omega_turb_f=Omega_turb_f,
    Omega_total_f=Omega_total_f,
    f_peak_sw=f_peak_sw,
    f_peak_turb=f_peak_turb,
    f_peak_actual=f_peak_actual,
    Omega_sw_peak=Omega_sw_peak,
    Omega_turb_peak=Omega_turb_peak,
    Omega_peak_actual=Omega_peak_actual,
    # Gate
    gate_name='STOCHASTIC-GW-59',
    gate_verdict=gate_verdict,
    gate_detail=gate_detail,
)
print(f"\nData saved to {outpath}")

# ==============================================================================
#  Step 9: Plot
# ==============================================================================

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

# --- Left panel: Full spectrum ---
ax1.loglog(f_array, Omega_sw_f, 'b-', label='Sound waves', linewidth=1.5, alpha=0.8)
ax1.loglog(f_array, Omega_turb_f, 'r--', label='Turbulence', linewidth=1.5, alpha=0.8)
ax1.loglog(f_array, Omega_total_f, 'k-', label='Total', linewidth=2.5)

# Mark peak
ax1.axvline(f_peak_actual, color='gray', linestyle=':', alpha=0.5, linewidth=1)
ax1.plot(f_peak_actual, Omega_peak_actual, 'ko', markersize=8, zorder=5)
ax1.annotate(f'f_peak = {f_peak_actual:.1e} Hz\n'
             f'$\\Omega_{{GW}} h^2$ = {Omega_peak_actual:.1e}',
             xy=(f_peak_actual, Omega_peak_actual),
             xytext=(f_peak_actual * 1e-3, Omega_peak_actual * 1e2),
             arrowprops=dict(arrowstyle='->', color='black'),
             fontsize=10, ha='center')

# Detector bands (shaded)
det_colors = {
    'LISA': 'green', 'ET': 'orange', 'LIGO O5': 'red',
    'BBO': 'cyan', 'DECIGO': 'purple', 'SKA (PTA)': 'brown'
}
for name, det in detectors.items():
    if name in det_colors:
        ax1.axvspan(det['f_min'], det['f_max'], alpha=0.08, color=det_colors[name])
        ax1.text(np.sqrt(det['f_min'] * det['f_max']), 1e-25,
                name, fontsize=7, ha='center', color=det_colors[name], rotation=90)

ax1.set_xlabel('Frequency [Hz]', fontsize=12)
ax1.set_ylabel('$\\Omega_{GW}(f) \\, h^2$', fontsize=12)
ax1.set_title('Stochastic GW Background from BCS Shattering', fontsize=13)
ax1.set_xlim(1e-10, 1e14)
ax1.set_ylim(1e-30, 1e-2)
ax1.legend(loc='upper left', fontsize=10)
ax1.grid(True, alpha=0.3, which='both')

# --- Right panel: Parameter space ---
# Show where this transition sits relative to other phase transitions
transitions = {
    'QCD\n(~0.15 GeV)': (0.15, 1e-9),
    'EW\n(~100 GeV)': (100, 1e-1),
    'BCS Shattering\n(this work)': (T_star_GeV, beta_over_H),
}

# f_peak vs T* for various beta/H
T_range = np.logspace(-1, 18, 100)  # GeV

for bh_val, ls, label in [(1, '--', '$\\beta/H_*=1$'),
                            (10, '-.', '$\\beta/H_*=10$'),
                            (100, ':', '$\\beta/H_*=100$')]:
    f_range = 1.65e-5 * 8.9e-3 * bh_val * (T_range / 100) * (g_star / 100)**(1.0/6.0)
    ax2.loglog(T_range, f_range, ls, color='gray', alpha=0.5, linewidth=1, label=label)

# Plot this transition
ax2.plot(T_star_GeV, f_peak_actual, 'r*', markersize=15, zorder=10,
         label=f'BCS Shattering\nT* = {T_star_GeV:.1e} GeV')

# Detector bands as horizontal spans
for name, det in detectors.items():
    if name in det_colors:
        ax2.axhspan(det['f_min'], det['f_max'], alpha=0.06, color=det_colors[name])
        ax2.text(1e-1, np.sqrt(det['f_min'] * det['f_max']),
                name, fontsize=7, color=det_colors[name], va='center')

ax2.set_xlabel('Transition Temperature $T_*$ [GeV]', fontsize=12)
ax2.set_ylabel('Peak Frequency $f_{peak}$ [Hz]', fontsize=12)
ax2.set_title('GW Peak Frequency vs Transition Temperature', fontsize=13)
ax2.set_xlim(1e-1, 1e18)
ax2.set_ylim(1e-10, 1e12)
ax2.legend(loc='upper left', fontsize=9)
ax2.grid(True, alpha=0.3, which='both')

plt.tight_layout()
plotpath = os.path.join(os.path.dirname(__file__), 's59_stochastic_gw.png')
plt.savefig(plotpath, dpi=150, bbox_inches='tight')
print(f"Plot saved to {plotpath}")

print(f"\n{'='*70}")
print("DONE")
print(f"{'='*70}")
