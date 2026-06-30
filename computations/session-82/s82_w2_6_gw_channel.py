#!/usr/bin/env python3
"""
S82 W2-6: GW-CHANNEL alpha vs gamma Discrimination
====================================================

Gate: S82-GW-CHANNEL
Owner: einstein-theorist (S82 Wave 2, S80 fragmented-recovery)
Plan: sessions/session-plan/session-80-plan.md lines 1368-1414
Shell: sessions/archive/session-82/session-82-results-workingpaper.md Section V.F

Substrate framing (PHONONIC):
  Route alpha (instanton-mediated modulus decay, T_rh = 2.46e11 MeV) and
  Route gamma (gravity-only Weinberg floor, T_rh = 1.69e18 MeV) produce
  distinct GW acoustic signatures during the post-fold modulus-oscillation
  epoch.  The modulus tau(t) is a phononic excitation of the substrate's
  tau-modulus direction; its oscillation modulates a_4(tau) (Seeley-DeWitt
  4th moment), sourcing gravitational-wave excitations of the emergent g_M.
  LISA would detect the acoustic signature of substrate reheating.

Pre-registered thresholds (S80 L1376-L1382):
  PASS: |delta_log10 Omega_GW| >= 2 at f = 1 mHz (routes distinguishable)
  INFO: 1 <= |delta_log10 Omega_GW| < 2
  FAIL: |delta_log10 Omega_GW| < 1 (channel cannot arbitrate)

Substitution chain (MANDATORY -- [VERIFY] trigger):
  Step 1: T_rh = [90/(pi^2 g*)]^(1/4) * sqrt(Gamma*M_Pl)
    => T_rh^2 = [90/(pi^2 g*)]^(1/2) * Gamma * M_Pl
    => Gamma = (pi^2 g*/90)^(1/2) * T_rh^2 / M_Pl  [NOT T_rh^4]
    => Gamma ∝ T_rh^2 at fixed M_Pl, g*
  Step 2: Omega_GW^prod = alpha_GW * (Gamma/m_tau)^2 * (m_tau/M_Pl_red)^4
    (perturbative scalar decay; Nakayama-Takahashi 2019, Ema et al. 2020)
  Step 3: Substitute Gamma ∝ T_rh^2 -> Omega_GW^prod ∝ T_rh^4
    at fixed m_tau, M_Pl, alpha_GW, g*
  Step 4: MD dilution a_ratio_MD = (H_prod/Gamma)^(2/3); H_prod is channel-
    independent (set by fold physics).  Omega_GW^decay = Omega_GW^prod /
    a_ratio_MD = Omega_GW^prod * (Gamma/H_prod)^(2/3)
    ∝ T_rh^4 * T_rh^(4/3) = T_rh^(16/3)
  Step 5: f_peak(today) scaling: a_prod/a_0 = (a_prod/a_decay)*(a_decay/a_0);
    a_prod/a_decay = 1/a_ratio_MD ∝ Gamma^(2/3) ∝ T_rh^(4/3);
    a_decay/a_0 ∝ 1/T_rh (entropy conservation). Combined: a_prod/a_0
    ∝ T_rh^(4/3 - 1) = T_rh^(1/3).  f_peak(today) = f_prod*a_prod/a_0
    ∝ T_rh^(1/3).  Parker-like spectrum:
    Omega_GW(f) = Omega_peak * (f/f_peak)^3 * exp(-(f/f_peak)^2)
  Step 6: At f = 1 mHz fixed, both routes have f << f_peak, so spectrum
    is in rising (f^3) regime: Omega_GW(1mHz) = Omega_peak * (f/f_peak)^3.
    Since Omega_peak ∝ T_rh^(16/3) and (1/f_peak)^3 ∝ T_rh^(-1):
    Omega_GW(1mHz) ∝ T_rh^(16/3) * T_rh^(-1) = T_rh^(13/3)
  Direction conclusion: T_rh^gamma > T_rh^alpha by 6.875e6 factor ->
    Omega_GW^gamma / Omega_GW^alpha = (6.875e6)^(13/3) ~ 10^29.63.
    Route gamma produces LARGER Omega_GW at 1 mHz (by many OOM).

Author: einstein-theorist (S82 W2-6)
"""
import os
import sys
import hashlib
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# -------- canonical constants -----------------------------------------------
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    PI,
    M_Pl_reduced, M_KK, M_KK_gravity,
    hbar_GeV_s,
    tau_fold, m_tau, v_terminal, Z_fold,
    T_CMB_GeV, T_BBN_GeV,
    g_star_SM, g_star_BBN,
)

# -------- input SHA-256 pins -------------------------------------------------
input_files = [                                                          # (local)
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'canonical_constants.py'),
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 's78_modulus_decay.npz'),
]
input_sha = {}                                                           # (local)
for fp in input_files:
    with open(fp, 'rb') as f:
        input_sha[os.path.basename(fp)] = hashlib.sha256(f.read()).hexdigest()

print("=" * 78)
print("S82 W2-6: GW-CHANNEL alpha vs gamma at LISA f = 1 mHz")
print("=" * 78)
print()
print("--- Input SHA-256 pins (first 20 lines of stdout) ---")
for k, v in input_sha.items():
    print(f"  {k}: {v}")
print()

# -------- load S78 W3-O T_rh values -----------------------------------------
s78 = np.load(input_files[1], allow_pickle=True)                         # (local)
T_rh_alpha_GeV = float(s78['T_rh_alpha_GeV'])                            # (local)
T_rh_gamma_GeV = float(s78['T_rh_gamma_GeV'])                            # (local)
T_rh_alpha_MeV = float(s78['T_rh_alpha_MeV'])                            # (local)
T_rh_gamma_MeV = float(s78['T_rh_gamma_MeV'])                            # (local)
Gamma_alpha = float(s78['Gamma_alpha'])                                  # (local) GeV
Gamma_gamma = float(s78['Gamma_gamma'])                                  # (local) GeV
m_tau_GeV_s78 = float(s78['m_tau_GeV'])                                  # (local) cross-check

# Plan specifies values pre-reg:
T_rh_alpha_MeV_pre_reg = 2.46e11                                         # (local) plan L1377
T_rh_gamma_MeV_pre_reg = 1.69e18                                         # (local) plan L1377

print("--- T_rh inputs (S78 W3-O) ---")
print(f"  T_rh^alpha  = {T_rh_alpha_GeV:.4e} GeV = {T_rh_alpha_MeV:.4e} MeV")
print(f"  T_rh^gamma  = {T_rh_gamma_GeV:.4e} GeV = {T_rh_gamma_MeV:.4e} MeV")
print(f"  Plan pre-reg: T_rh^alpha = {T_rh_alpha_MeV_pre_reg:.3e} MeV")
print(f"  Plan pre-reg: T_rh^gamma = {T_rh_gamma_MeV_pre_reg:.3e} MeV")
# Reconcile: plan anchors on values within factor of few of S78 W3-O output
ratio_alpha = T_rh_alpha_MeV / T_rh_alpha_MeV_pre_reg                    # (local)
ratio_gamma = T_rh_gamma_MeV / T_rh_gamma_MeV_pre_reg                    # (local)
print(f"  S78/plan_alpha ratio = {ratio_alpha:.3f}")
print(f"  S78/plan_gamma ratio = {ratio_gamma:.3f}")
print()

# -------- derived framework inputs (channel-independent) ---------------------
m_tau_GeV = m_tau * M_KK_gravity                                         # (local) GeV
phi_0_GeV = np.sqrt(Z_fold) * (v_terminal / m_tau) * M_KK_gravity        # (local) canonical field amplitude
rho_modulus = 0.5 * m_tau_GeV**2 * phi_0_GeV**2                          # (local) GeV^4
H_prod = np.sqrt(rho_modulus / (3.0 * M_Pl_reduced**2))                  # (local) GeV, channel-independent

print("--- Channel-Independent Modulus-Oscillation Inputs ---")
print(f"  m_tau = {m_tau:.3f} M_KK = {m_tau_GeV:.3e} GeV")
print(f"  phi_0 (canonical) = {phi_0_GeV:.3e} GeV")
print(f"  rho_modulus = {rho_modulus:.3e} GeV^4")
print(f"  H_prod (modulus-dominated) = {H_prod:.3e} GeV")
print()

# -------- GW computation formula (Nakayama-Takahashi-Ema) --------------------
# Perturbative scalar decay GW production efficiency:
#   Omega_GW^prod = alpha_GW * (Gamma/m_tau)^2 * (m_tau/M_Pl)^4
# alpha_GW ~ 0.01 for generic perturbative decay (s76 canonical).  Scheme-
# dependence in this prefactor cancels in the ratio Omega^gamma/Omega^alpha.
alpha_GW = 0.01                                                          # (local) s76 canonical

# Omega_rad today (photons + neutrinos)
h_Hubble = 0.674                                                         # (local) Planck 2018
Omega_rad_h2 = 4.15e-5                                                   # (local)
Omega_rad_today = Omega_rad_h2 / h_Hubble**2                             # (local)
g_star_0 = 3.36                                                          # (local) photons + nu today

def compute_channel(T_rh_GeV, Gamma, label):
    """Compute full GW spectrum and Omega_GW(f) at LISA band for one route."""
    print(f"--- Channel {label}: T_rh = {T_rh_GeV:.3e} GeV ---")
    # Step 1: Omega_GW at production
    Omega_GW_prod = alpha_GW * (Gamma/m_tau_GeV)**2 * (m_tau_GeV/M_Pl_reduced)**4  # (local)
    # Step 2: MD dilution (channel-dependent through Gamma)
    a_ratio_MD = (H_prod / Gamma)**(2.0/3.0)                             # (local)
    Omega_GW_at_decay = Omega_GW_prod / a_ratio_MD                       # (local)
    # Step 3: g_* correction and redshift to today
    g_star_RH = g_star_SM                                                # (local)
    # Omega_GW today (standard RD transport)
    Omega_GW_today = Omega_GW_at_decay * (g_star_RH/g_star_0)**(-1.0/3.0) * Omega_rad_today  # (local)
    # Step 4: Peak frequency (quadrupole at 2*m_tau, redshifted)
    f_prod_GeV = 2.0 * m_tau_GeV                                         # (local)
    a_prod_over_a_decay = 1.0 / a_ratio_MD                               # (local)
    a_decay_over_a0 = T_CMB_GeV / T_rh_GeV * (g_star_0/g_star_RH)**(1.0/3.0)  # (local)
    a_prod_over_a0 = a_prod_over_a_decay * a_decay_over_a0               # (local)
    f_peak_Hz = f_prod_GeV * a_prod_over_a0 / (2.0*PI*hbar_GeV_s)        # (local)
    print(f"  Gamma          = {Gamma:.3e} GeV")
    print(f"  Omega_GW^prod   = {Omega_GW_prod:.3e}")
    print(f"  a_ratio_MD      = {a_ratio_MD:.3e}  (N_MD = {np.log(1/a_ratio_MD):.2f})")
    print(f"  Omega_GW^decay  = {Omega_GW_at_decay:.3e}")
    print(f"  Omega_GW^today  = {Omega_GW_today:.3e}  (peak)")
    print(f"  f_peak (today)  = {f_peak_Hz:.3e} Hz (log10 = {np.log10(f_peak_Hz):.2f})")
    return {                                                              # (local)
        'T_rh_GeV': T_rh_GeV,
        'Gamma': Gamma,
        'Omega_GW_prod': Omega_GW_prod,
        'a_ratio_MD': a_ratio_MD,
        'Omega_GW_at_decay': Omega_GW_at_decay,
        'Omega_GW_today': Omega_GW_today,  # peak value today
        'f_peak_Hz': f_peak_Hz,
    }

result_alpha = compute_channel(T_rh_alpha_GeV, Gamma_alpha, "alpha (inst-mediated)")
print()
result_gamma = compute_channel(T_rh_gamma_GeV, Gamma_gamma, "gamma (gravity)")
print()

# -------- Parker-like spectral shape -----------------------------------------
# Omega_GW(f) = Omega_peak * (f/f_peak)^3 * exp(-(f/f_peak)^2)
# (Parker-like: causal f^3 rise at low f, Gaussian fall at high f;
#  physics: coherent modulus oscillation produces narrow-band quadrupole
#  at 2m_tau, but the transit-inheritance gives a broadening profile.)
def Omega_GW_at_f(f_Hz, Omega_peak, f_peak_Hz):
    x = f_Hz / f_peak_Hz                                                 # (local)
    return Omega_peak * x**3 * np.exp(-x**2)                             # (local)

# LISA band
f_LISA = 1.0e-3                                                          # (local) Hz (1 mHz)
Omega_GW_LISA_alpha = Omega_GW_at_f(f_LISA, result_alpha['Omega_GW_today'],
                                     result_alpha['f_peak_Hz'])          # (local)
Omega_GW_LISA_gamma = Omega_GW_at_f(f_LISA, result_gamma['Omega_GW_today'],
                                     result_gamma['f_peak_Hz'])          # (local)

# Cross-check: where does f=1mHz fall relative to f_peak?
ratio_f_alpha = f_LISA / result_alpha['f_peak_Hz']                       # (local)
ratio_f_gamma = f_LISA / result_gamma['f_peak_Hz']                       # (local)

print("--- Parker-like Spectrum at LISA band (f = 1 mHz) ---")
print(f"  Shape: Omega_GW(f) = Omega_peak * (f/f_peak)^3 * exp(-(f/f_peak)^2)")
print()
print(f"  Route alpha:")
print(f"    f_LISA / f_peak    = {ratio_f_alpha:.3e}")
print(f"    Omega_GW(1mHz)     = {Omega_GW_LISA_alpha:.3e}")
print(f"  Route gamma:")
print(f"    f_LISA / f_peak    = {ratio_f_gamma:.3e}")
print(f"    Omega_GW(1mHz)     = {Omega_GW_LISA_gamma:.3e}")
print()

# -------- delta OOM computation ----------------------------------------------
# Guard against zero / inf
if Omega_GW_LISA_alpha > 0 and Omega_GW_LISA_gamma > 0:
    ratio_gamma_over_alpha = Omega_GW_LISA_gamma / Omega_GW_LISA_alpha   # (local)
    delta_OOM = np.log10(abs(ratio_gamma_over_alpha))                    # (local)
else:
    ratio_gamma_over_alpha = np.inf                                      # (local)
    delta_OOM = np.inf                                                   # (local)

abs_delta_OOM = abs(delta_OOM)                                           # (local)

print(f"  Omega_GW_gamma / Omega_GW_alpha = {ratio_gamma_over_alpha:.3e}")
print(f"  log10(ratio) = {delta_OOM:+.2f}")
print(f"  |delta_OOM|  = {abs_delta_OOM:.2f}")
print()

# -------- substitution-chain cross-check -------------------------------------
# Friedmann: T_rh = [90/(pi^2 g*)]^(1/4) * sqrt(Gamma * M_Pl)
# => Gamma ∝ T_rh^2 (at fixed M_Pl, g*)
# => Omega_GW^prod ∝ Gamma^2 ∝ T_rh^4
# => Omega_GW^peak(today) ∝ Gamma^(8/3) ∝ T_rh^(16/3)
# => f_peak(today) ∝ T_rh^(1/3) (via a_prod/a_decay and a_decay/a_0)
# => Omega_GW(f=1mHz) ∝ T_rh^(13/3) (f^3 rising regime)
T_ratio = T_rh_gamma_GeV / T_rh_alpha_GeV                                # (local)
# Peak-value OOM (no f-weighting)
ratio_peak_raw = result_gamma['Omega_GW_today'] / result_alpha['Omega_GW_today']  # (local)
# Predicted from T_rh^(16/3) scaling
ratio_peak_predicted = T_ratio**(16.0/3.0)                               # (local)
# Predicted from T_rh^4 (Omega_GW^prod only)
ratio_prod_predicted = T_ratio**4                                         # (local)
ratio_prod_actual = result_gamma['Omega_GW_prod']/result_alpha['Omega_GW_prod']  # (local)
# Predicted Omega_GW(1mHz) scaling (T^(13/3))
ratio_1mHz_predicted = T_ratio**(13.0/3.0)                               # (local)

print("--- Substitution-Chain Cross-Check ---")
print(f"  T_rh^gamma / T_rh^alpha = {T_ratio:.3e}")
print(f"  Predicted Omega_GW^prod ratio (T^4): {ratio_prod_predicted:.3e}")
print(f"  Computed Omega_GW^prod ratio:        {ratio_prod_actual:.3e}")
print(f"  Chain check (should agree): {ratio_prod_actual/ratio_prod_predicted:.4f}")
print()
print(f"  Predicted Omega_peak(today) ratio (T^(16/3)): {ratio_peak_predicted:.3e}")
print(f"  Computed Omega_peak(today) ratio:             {ratio_peak_raw:.3e}")
print(f"  Chain check (should be within O(1)):    {ratio_peak_raw/ratio_peak_predicted:.4f}")
print()
print(f"  Predicted Omega_GW(1mHz) ratio (T^(13/3)): {ratio_1mHz_predicted:.3e}")
print(f"  Computed Omega_GW(1mHz) ratio:             {ratio_gamma_over_alpha:.3e}")
print(f"  Chain check (should agree within O(1)): {ratio_gamma_over_alpha/ratio_1mHz_predicted:.4f}")
print()

# -------- LISA sensitivity reference -----------------------------------------
# LISA sensitivity at f = 1 mHz is Omega_GW ~ 1e-12 (s69_transit_gw.py
# canonical).  Sources above this line are detectable.
LISA_sensitivity = 1.0e-12                                               # (local) canonical s69/s77
detectable_alpha = (Omega_GW_LISA_alpha > LISA_sensitivity)              # (local)
detectable_gamma = (Omega_GW_LISA_gamma > LISA_sensitivity)              # (local)

print("--- LISA Detectability Assessment ---")
print(f"  LISA sensitivity at 1 mHz: Omega_GW ~ {LISA_sensitivity:.0e}")
print(f"  Route alpha detectable?  {detectable_alpha}  (Omega = {Omega_GW_LISA_alpha:.3e})")
print(f"  Route gamma detectable?  {detectable_gamma}  (Omega = {Omega_GW_LISA_gamma:.3e})")
print()

# -------- build full spectrum Omega_GW(f) -----------------------------------
# Range spanning many decades for visualization
f_array_Hz = np.logspace(-20, 15, 2000)                                  # (local)
Omega_alpha_spectrum = Omega_GW_at_f(f_array_Hz, result_alpha['Omega_GW_today'],
                                      result_alpha['f_peak_Hz'])          # (local)
Omega_gamma_spectrum = Omega_GW_at_f(f_array_Hz, result_gamma['Omega_GW_today'],
                                      result_gamma['f_peak_Hz'])          # (local)

# -------- pre-registered gate verdict ----------------------------------------
PASS_THRESHOLD = 2.0                                                     # (local) OOM
INFO_THRESHOLD = 1.0                                                     # (local) OOM

if abs_delta_OOM >= PASS_THRESHOLD:
    verdict = "PASS"                                                     # (local)
    verdict_reason = (f"Routes distinguishable: |delta_OOM| = {abs_delta_OOM:.2f} "
                      f">= {PASS_THRESHOLD} OOM.")                        # (local)
elif abs_delta_OOM >= INFO_THRESHOLD:
    verdict = "INFO"                                                     # (local)
    verdict_reason = (f"|delta_OOM| = {abs_delta_OOM:.2f} in [{INFO_THRESHOLD}, "
                      f"{PASS_THRESHOLD}) OOM.")                          # (local)
else:
    verdict = "FAIL"                                                     # (local)
    verdict_reason = (f"Routes indistinguishable: |delta_OOM| = {abs_delta_OOM:.2f} "
                      f"< {INFO_THRESHOLD} OOM.")                         # (local)

# -------- closure SHA --------------------------------------------------------
# Canonical pre-registered 4-tuple: (value, scheme, convention, L_max)
out_value = f"{abs_delta_OOM:.3f}"                                       # (local)
out_scheme = "PARKER-SPECTRUM"                                           # (local)
out_convention = "T_RH-SCALING"                                          # (local)
out_L_max = "N/A"                                                        # (local)
closure_input = (                                                        # (local)
    f"gate=S82-GW-CHANNEL;value={out_value};scheme={out_scheme};"
    f"convention={out_convention};L_max={out_L_max};"
    f"input_sha=" + ";".join(f"{k}:{v}" for k,v in sorted(input_sha.items()))
)
closure_sha = hashlib.sha256(closure_input.encode('utf-8')).hexdigest()  # (local)

# -------- print verdict ------------------------------------------------------
print("=" * 78)
print(f"GATE VERDICT: S82-GW-CHANNEL = {verdict}")
print(f"  {verdict_reason}")
print(f"  4-tuple: (value={out_value}, scheme={out_scheme}, "
      f"convention={out_convention}, L_max={out_L_max})")
print(f"  closure SHA-256: {closure_sha}")
print("=" * 78)
print()

# -------- write verdict line -------------------------------------------------
verdict_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             's82_gate_verdicts.txt')                     # (local)
verdict_line = (                                                         # (local)
    f"S82-GW-CHANNEL: {verdict} -- value={out_value} scheme={out_scheme} "
    f"convention={out_convention} L_max={out_L_max} sha256={closure_sha}"
)
with open(verdict_file, 'a') as f:
    f.write(verdict_line + "\n")
print(f"Appended verdict line to: {verdict_file}")
print(f"  {verdict_line}")
print()

# -------- save data ----------------------------------------------------------
out_npz = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        's82_w2_6_gw_channel.npz')                        # (local)
np.savez(
    out_npz,
    # Input pins
    T_rh_alpha_GeV=T_rh_alpha_GeV,
    T_rh_gamma_GeV=T_rh_gamma_GeV,
    T_rh_alpha_MeV=T_rh_alpha_MeV,
    T_rh_gamma_MeV=T_rh_gamma_MeV,
    Gamma_alpha=Gamma_alpha,
    Gamma_gamma=Gamma_gamma,
    # Framework constants
    m_tau_GeV=m_tau_GeV,
    M_Pl_reduced=M_Pl_reduced,
    alpha_GW=alpha_GW,
    H_prod=H_prod,
    phi_0_GeV=phi_0_GeV,
    rho_modulus=rho_modulus,
    g_star_SM=g_star_SM,
    g_star_0=g_star_0,
    Omega_rad_today=Omega_rad_today,
    # Route alpha output
    Omega_GW_prod_alpha=result_alpha['Omega_GW_prod'],
    Omega_GW_decay_alpha=result_alpha['Omega_GW_at_decay'],
    Omega_GW_today_alpha=result_alpha['Omega_GW_today'],
    f_peak_alpha_Hz=result_alpha['f_peak_Hz'],
    a_ratio_MD_alpha=result_alpha['a_ratio_MD'],
    Omega_GW_LISA_alpha=Omega_GW_LISA_alpha,
    # Route gamma output
    Omega_GW_prod_gamma=result_gamma['Omega_GW_prod'],
    Omega_GW_decay_gamma=result_gamma['Omega_GW_at_decay'],
    Omega_GW_today_gamma=result_gamma['Omega_GW_today'],
    f_peak_gamma_Hz=result_gamma['f_peak_Hz'],
    a_ratio_MD_gamma=result_gamma['a_ratio_MD'],
    Omega_GW_LISA_gamma=Omega_GW_LISA_gamma,
    # Comparison
    delta_OOM=delta_OOM,
    abs_delta_OOM=abs_delta_OOM,
    ratio_gamma_over_alpha=ratio_gamma_over_alpha,
    # Substitution-chain cross-check (corrected: Gamma ∝ T_rh^2, not T_rh^4)
    T_ratio_gamma_alpha=T_ratio,
    ratio_prod_predicted_T4=ratio_prod_predicted,
    ratio_prod_actual=ratio_prod_actual,
    ratio_peak_predicted_T16over3=ratio_peak_predicted,
    ratio_peak_raw=ratio_peak_raw,
    ratio_1mHz_predicted_T13over3=ratio_1mHz_predicted,
    # LISA
    f_LISA_Hz=f_LISA,
    LISA_sensitivity=LISA_sensitivity,
    detectable_alpha=detectable_alpha,
    detectable_gamma=detectable_gamma,
    # Full spectrum
    f_array_Hz=f_array_Hz,
    Omega_alpha_spectrum=Omega_alpha_spectrum,
    Omega_gamma_spectrum=Omega_gamma_spectrum,
    # Thresholds
    PASS_THRESHOLD=PASS_THRESHOLD,
    INFO_THRESHOLD=INFO_THRESHOLD,
    # Gate
    gate_id="S82-GW-CHANNEL",
    verdict=verdict,
    verdict_reason=verdict_reason,
    # Pre-registered 4-tuple
    out_value=out_value,
    out_scheme=out_scheme,
    out_convention=out_convention,
    out_L_max=out_L_max,
    closure_sha=closure_sha,
)
print(f"Saved data to: {out_npz}")

# -------- plot --------------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel 1: Omega_GW(f) spectrum for both routes
ax = axes[0, 0]
ax.loglog(f_array_Hz, Omega_alpha_spectrum, 'b-', lw=2,
          label=f'Route alpha (T_rh={T_rh_alpha_GeV:.2e} GeV)')
ax.loglog(f_array_Hz, Omega_gamma_spectrum, 'r-', lw=2,
          label=f'Route gamma (T_rh={T_rh_gamma_GeV:.2e} GeV)')
# LISA band
lisa_band = (1e-4, 1e-1)                                                 # (local) Hz
ax.axvspan(lisa_band[0], lisa_band[1], alpha=0.15, color='green',
           label='LISA band')
ax.axhline(LISA_sensitivity, color='green', ls='--', lw=1.5, alpha=0.7,
           label=f'LISA sens ~ {LISA_sensitivity:.0e}')
ax.axvline(f_LISA, color='black', ls=':', lw=1.5, alpha=0.7,
           label=f'f = 1 mHz')
# Mark LISA values
ax.plot(f_LISA, Omega_GW_LISA_alpha, 'bo', ms=10, zorder=10,
        label=f'alpha: {Omega_GW_LISA_alpha:.1e}')
ax.plot(f_LISA, Omega_GW_LISA_gamma, 'r^', ms=10, zorder=10,
        label=f'gamma: {Omega_GW_LISA_gamma:.1e}')
ax.set_xlabel('Frequency f [Hz]')
ax.set_ylabel(r'$\Omega_{\rm GW}(f)$')
ax.set_title('GW Spectrum: Route alpha vs gamma')
ax.legend(fontsize=8, loc='best')
ax.set_ylim(1e-80, 1e0)
ax.grid(True, which='both', alpha=0.3)

# Panel 2: T_rh comparison + delta_OOM
ax = axes[0, 1]
labels_routes = ['alpha\n(inst-mediated)', 'gamma\n(gravity)']           # (local)
T_vals_MeV = [T_rh_alpha_MeV, T_rh_gamma_MeV]                            # (local)
Omega_vals = [Omega_GW_LISA_alpha, Omega_GW_LISA_gamma]                  # (local)
x_pos = np.arange(len(labels_routes))                                    # (local)
width = 0.35                                                             # (local)
ax_twin = ax.twinx()
bars1 = ax.bar(x_pos - width/2, T_vals_MeV, width, color='skyblue',
               edgecolor='black', label='T_rh [MeV]')
bars2 = ax_twin.bar(x_pos + width/2, Omega_vals, width, color='salmon',
                    edgecolor='black', label='Omega_GW(1mHz)')
ax.set_yscale('log')
ax_twin.set_yscale('log')
ax.set_xticks(x_pos)
ax.set_xticklabels(labels_routes)
ax.set_ylabel('T_rh [MeV]', color='steelblue')
ax_twin.set_ylabel('Omega_GW(f=1mHz)', color='red')
for bar, val in zip(bars1, T_vals_MeV):
    ax.text(bar.get_x()+bar.get_width()/2., val*2, f'{val:.2e}',
            ha='center', va='bottom', fontsize=8, color='steelblue')
for bar, val in zip(bars2, Omega_vals):
    if val > 0:
        ax_twin.text(bar.get_x()+bar.get_width()/2., val*2, f'{val:.2e}',
                     ha='center', va='bottom', fontsize=8, color='red')
ax.set_title(f'T_rh and Omega_GW(1mHz) by Route\n'
             f'|delta_OOM| = {abs_delta_OOM:.2f}')
ax.grid(alpha=0.3, axis='y')

# Panel 3: substitution-chain verification
ax = axes[1, 0]
quantities = ['Omega_prod\n(T^4)', 'Omega_peak(today)\n(T^(16/3))',
              'Omega(1mHz)\n(T^(13/3))']                                 # (local)
predicted = [ratio_prod_predicted, ratio_peak_predicted,
             ratio_1mHz_predicted]                                        # (local)
actual = [ratio_prod_actual, ratio_peak_raw, ratio_gamma_over_alpha]     # (local)
x_q = np.arange(len(quantities))                                         # (local)
ax.bar(x_q - 0.2, predicted, 0.4, color='gold', edgecolor='black',
       label='Predicted (T_rh scaling)')
ax.bar(x_q + 0.2, actual, 0.4, color='purple', edgecolor='black',
       label='Computed')
ax.set_yscale('log')
ax.set_xticks(x_q)
ax.set_xticklabels(quantities, fontsize=9)
ax.set_ylabel(r'$\Omega_{\rm GW}^{\gamma}/\Omega_{\rm GW}^{\alpha}$')
ax.set_title('Substitution-Chain Verification (ratio gamma/alpha)')
ax.legend(fontsize=9)
ax.grid(alpha=0.3, axis='y')

# Panel 4: Gate verdict summary
ax = axes[1, 1]
ax.axis('off')
summary = (
    f"GATE S82-GW-CHANNEL: {verdict}\n"
    f"\n"
    f"Threshold:\n"
    f"  PASS: |delta_OOM| >= {PASS_THRESHOLD}\n"
    f"  INFO: [{INFO_THRESHOLD}, {PASS_THRESHOLD}) OOM\n"
    f"  FAIL: < {INFO_THRESHOLD} OOM\n"
    f"\n"
    f"Route alpha (instanton-mediated):\n"
    f"  T_rh     = {T_rh_alpha_MeV:.3e} MeV\n"
    f"  f_peak   = {result_alpha['f_peak_Hz']:.3e} Hz\n"
    f"  Omega_peak = {result_alpha['Omega_GW_today']:.3e}\n"
    f"  Omega(1mHz) = {Omega_GW_LISA_alpha:.3e}\n"
    f"\n"
    f"Route gamma (gravity-only):\n"
    f"  T_rh     = {T_rh_gamma_MeV:.3e} MeV\n"
    f"  f_peak   = {result_gamma['f_peak_Hz']:.3e} Hz\n"
    f"  Omega_peak = {result_gamma['Omega_GW_today']:.3e}\n"
    f"  Omega(1mHz) = {Omega_GW_LISA_gamma:.3e}\n"
    f"\n"
    f"Discrimination:\n"
    f"  log10(Omega_gamma/Omega_alpha) = {delta_OOM:+.2f}\n"
    f"  |delta_OOM| = {abs_delta_OOM:.2f}\n"
    f"\n"
    f"LISA detectability (sens = 1e-12):\n"
    f"  alpha detectable? {detectable_alpha}\n"
    f"  gamma detectable? {detectable_gamma}\n"
)
verdict_color = {'PASS': 'lightgreen', 'INFO': 'lightyellow',
                 'FAIL': 'lightcoral'}.get(verdict, 'white')              # (local)
ax.text(0.05, 0.95, summary, transform=ax.transAxes,
        fontsize=9, va='top', family='monospace',
        bbox=dict(boxstyle='round,pad=0.5', facecolor=verdict_color, alpha=0.9,
                  edgecolor='black', linewidth=1.5))

plt.tight_layout()
out_png = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        's82_w2_6_gw_channel.png')                        # (local)
plt.savefig(out_png, dpi=130, bbox_inches='tight')
plt.close()
print(f"Saved plot to: {out_png}")
print()
print("Done.")
