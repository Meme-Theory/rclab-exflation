#!/usr/bin/env python3
"""
DM-PAIR-DECAY-70: Leggett DM Pair Decay Rate vs FIRAS/PIXIE Spectral Distortion
================================================================================

Session 70, Wave 5-A (Mack Cosmic Bridge)

The Leggett-channel GGE quasiparticles constitute the framework's dark matter
candidate. Their stability against gravitational decay determines whether they
survive to the present epoch. This computation loads the S67 Leggett gravitational
decay results and confronts them with the FIRAS spectral distortion bound
(delta_mu < 9e-5, 95% CL) and the PIXIE forecast sensitivity (sigma_mu ~ 5e-8).

The Leggett mode is protected from single-particle decay by a Z_2 parity
selection rule (exact to machine epsilon, S67 LEGGETT-GRAV-DECAY-67 PASS).
Only pair annihilation 2L -> 2g is allowed, with rate Gamma_pair.

The spectral distortion from a decaying DM species is:
    delta_mu ~ (Gamma_DM / H_0) * (Omega_DM / Omega_rad) * (T_decay / T_CMB)^{3/2}

For pair annihilation, T_decay is irrelevant (rate is so small that no decays
occur within any cosmological epoch).

Gate: DM-PAIR-DECAY-70
    PASS: Gamma_L * t_universe < sigma_FIRAS (stable against FIRAS)
    FAIL: Gamma_L * t_universe > 1 (decays within age of universe)
    INFO: intermediate (detectable by PIXIE but not FIRAS)

Input: computations/session-67/s67_leggett_grav_decay.npz
       computations/_shared/canonical_constants.py
Output: computations/session-70/s70_dm_pair_decay.npz
        Working paper Section W5-A
"""

import sys
import os
import numpy as np

# Ensure canonical_constants is importable
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    H_0_GeV, t_universe_s, Omega_DM, Omega_r,
    T_CMB, T_CMB_GeV, M_KK_gravity, M_Pl_reduced,
    hbar_GeV_s, GeV_to_inv_s, sigma_FIRAS,
    omega_L1, omega_L2,
    H_0_km_s_Mpc, PI,
)

# ==============================================================================
#  Step 1: Load Leggett gravitational decay data from S67
# ==============================================================================

data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         "s67_leggett_grav_decay.npz")
d = np.load(data_path, allow_pickle=True)

# Extract key quantities
Gamma_single = float(d['Gamma_single'])         # Single-particle decay rate (GeV)
Gamma_pair_S59 = float(d['Gamma_pair_S59'])     # Pair annihilation rate (GeV), S59 omega_L
Gamma_pair_S52 = float(d['Gamma_pair_S52'])     # Pair annihilation rate (GeV), S52 omega_L
Gamma_pair_over_H0_S59 = float(d['Gamma_pair_over_H0_S59'])
Gamma_pair_over_H0_S52 = float(d['Gamma_pair_over_H0_S52'])
tau_pair_s_S59 = float(d['tau_pair_s_S59'])     # Pair lifetime in seconds
tau_pair_s_S52 = float(d['tau_pair_s_S52'])     # Pair lifetime in seconds
Z2_parity_blocks = bool(d['Z2_parity_blocks_single'])
Z2_asymmetry_max = float(d['Z2_asymmetry_max'])
gate_verdict_S67 = str(d['gate_verdict'])

omega_L_S52 = float(d['omega_L_S52'])           # Leggett frequency (M_KK units)
omega_L_S59 = float(d['omega_L_S59'])           # Leggett frequency (M_KK units)

print("=" * 78)
print("DM-PAIR-DECAY-70: Leggett DM Pair Decay Rate vs FIRAS/PIXIE")
print("=" * 78)

# ==============================================================================
#  Step 2: Summarize S67 decay rates
# ==============================================================================

print("\n--- S67 LEGGETT-GRAV-DECAY-67 Results (loaded) ---")
print(f"  Z_2 parity blocks single decay: {Z2_parity_blocks}")
print(f"  Z_2 asymmetry (max):            {Z2_asymmetry_max:.3e}")
print(f"  Gamma_single:                   {Gamma_single:.3e} GeV  (exact zero)")
print()
print(f"  Pair annihilation (2L -> 2g):")
print(f"    S59 omega_L = {omega_L_S59:.5f} M_KK:")
print(f"      Gamma_pair = {Gamma_pair_S59:.6e} GeV")
print(f"      Gamma/H_0  = {Gamma_pair_over_H0_S59:.6e}")
print(f"      tau_pair    = {tau_pair_s_S59:.6e} s")
print(f"    S52 omega_L = {omega_L_S52:.5f} M_KK:")
print(f"      Gamma_pair = {Gamma_pair_S52:.6e} GeV")
print(f"      Gamma/H_0  = {Gamma_pair_over_H0_S52:.6e}")
print(f"      tau_pair    = {tau_pair_s_S52:.6e} s")
print(f"  S67 gate verdict: {gate_verdict_S67}")

# ==============================================================================
#  Step 3: Compute spectral distortion delta_mu from pair decay
# ==============================================================================
# The mu distortion from a decaying DM species (Hu & Silk 1993, Chluba 2016):
#   delta_mu ~ (Gamma_DM / H_0) * (Omega_DM / Omega_rad) * f_therm
#
# where f_therm captures thermalization efficiency at the decay epoch.
# For decay at redshift z_decay, f_therm ~ (T_decay/T_mu)^{5/2} for
# T_decay > T_mu ~ 2e6 K (the mu-distortion thermalization threshold).
#
# But here the lifetime is tau ~ 10^{82} s >> t_universe ~ 4.35e17 s.
# The number of decays within the age of the universe is:
#   N_decay / N_total = 1 - exp(-t_univ / tau) ~ t_univ / tau  (for tau >> t_univ)
#
# The energy injection rate (fractional) is:
#   dE/E_DM = Gamma_pair * t_universe
#
# The mu distortion is bounded by:
#   delta_mu < 1.4 * (dE/E_rad)  (thermalization-limited)
# where dE/E_rad = (Omega_DM / Omega_rad) * (dE/E_DM) * f_efficiency
#
# With f_efficiency ~ 1 (all energy goes to photons), the upper bound is:

print("\n--- FIRAS/PIXIE Spectral Distortion Comparison ---")

# FIRAS bound on mu distortion
FIRAS_mu_bound = 9.0e-5         # 95% CL (Fixsen et al. 1996)  # (local)
PIXIE_mu_sensitivity = 5.0e-8   # PIXIE forecast (Kogut et al. 2011)  # (local)

# Fractional energy injection from pair decay within t_universe
# Using the MORE conservative (larger Gamma) S59 value
Gamma_pair = Gamma_pair_S59     # Use larger rate for conservative bound
tau_DM_s = tau_pair_s_S59       # Corresponding lifetime

# Fraction of DM that decays within t_universe
# Since tau >> t_univ by 65 OOM, f_decay = t_univ/tau to machine precision
# (1 - exp(-x) ~ x for x ~ 10^{-65}; float64 exp underflows to 1.0)
f_decay = t_universe_s / tau_DM_s  # Exact in this regime
log10_f_decay = np.log10(t_universe_s) - np.log10(tau_DM_s)

print(f"\n  Conservative rate (S59 omega_L):")
print(f"    Gamma_pair     = {Gamma_pair:.6e} GeV")
print(f"    tau_DM         = {tau_DM_s:.6e} s")
print(f"    t_universe     = {t_universe_s:.3e} s")
print(f"    t_univ / tau   = {f_decay:.6e}")
print(f"    log10(f_decay) = {log10_f_decay:.2f}")

# Energy injected per decay: each pair annihilation releases 2 * m_L
# where m_L = omega_L * M_KK. The energy density injected is:
#   Delta_rho = f_decay * rho_DM * (2 * m_L) / (2 * m_L) = f_decay * rho_DM
# (Each pair deposits its rest mass energy into gravitons/photons)

# The mu-distortion from energy injection (Hu & Silk 1993):
#   delta_mu = 1.4 * (Delta_rho / rho_gamma) * f_therm
# where f_therm = 1 for injection after double-Compton thermalization freeze-out
# (z < z_DC ~ 2e6) and f_therm -> 0 for z > z_DC.
#
# For our case: the DM does NOT decay within the relevant epoch (z ~ 5e4 to 2e6).
# The fraction that decays at ANY redshift is negligible.
# But for the formal bound, we compute the MAXIMUM possible distortion by
# assuming ALL decays happen at the optimal redshift for mu production.

# Upper bound on delta_mu (all energy deposited at optimal z):
# delta_mu_max = 1.4 * f_decay * (Omega_DM / Omega_r)
# This underflows in float64 since f_decay ~ 10^{-65}. Use log10 arithmetic.
log10_delta_mu_max = np.log10(1.4) + log10_f_decay + np.log10(Omega_DM / Omega_r)
delta_mu_max_log = log10_delta_mu_max  # Keep as log10 to avoid underflow

print(f"\n  Spectral distortion upper bound:")
print(f"    Omega_DM / Omega_rad = {Omega_DM / Omega_r:.2f}")
print(f"    log10(delta_mu_max)  = {log10_delta_mu_max:.2f}")
print(f"    delta_mu (max)       ~ 10^{{{log10_delta_mu_max:.1f}}}")
print(f"    FIRAS bound          = {FIRAS_mu_bound:.1e}  (log10 = {np.log10(FIRAS_mu_bound):.2f})")
print(f"    PIXIE sensitivity    = {PIXIE_mu_sensitivity:.1e}  (log10 = {np.log10(PIXIE_mu_sensitivity):.2f})")
print(f"    log10(delta_mu/FIRAS)= {log10_delta_mu_max - np.log10(FIRAS_mu_bound):.1f}")
print(f"    log10(delta_mu/PIXIE)= {log10_delta_mu_max - np.log10(PIXIE_mu_sensitivity):.1f}")

# ==============================================================================
#  Step 4: Alternative decay channel — direct formula from prompt
# ==============================================================================
# The prompt specifies:
#   Gamma_L = (coupling)^2 * omega_L^3 / (8*pi * rho_s)
# where coupling comes from cubic vertex in BCS effective action.
#
# From S67: the Z_2 parity of a_2(phi_23) = a_2(-phi_23) means the cubic
# vertex vanishes identically. The first non-zero vertex is quartic (pair).
# So Gamma_single = 0 exactly.
#
# For the pair channel, the S67 computation already gives the full rate.
# Let's verify the scaling and compute the direct formula for completeness.

print("\n--- Direct Decay Rate Formula ---")

# Leggett mass in GeV
m_L_S59_GeV = omega_L_S59 * M_KK_gravity
m_L_S52_GeV = omega_L_S52 * M_KK_gravity

print(f"\n  Leggett mass:")
print(f"    m_L (S59) = {m_L_S59_GeV:.6e} GeV = {omega_L_S59:.5f} * M_KK")
print(f"    m_L (S52) = {m_L_S52_GeV:.6e} GeV = {omega_L_S52:.5f} * M_KK")

# Naive gravitational decay rate for a massive scalar -> 2 gravitons:
# Gamma_naive = m^3 / (160 * pi * M_Pl^2)  (standard result, e.g. Han, Willenbrock & Zhang 2005)
Gamma_naive_S59 = m_L_S59_GeV**3 / (160 * PI * M_Pl_reduced**2)
Gamma_naive_S52 = m_L_S52_GeV**3 / (160 * PI * M_Pl_reduced**2)

print(f"\n  Naive gravitational decay (single L -> 2g, no selection rule):")
print(f"    Gamma_naive (S59) = {Gamma_naive_S59:.6e} GeV")
print(f"    Gamma_naive (S52) = {Gamma_naive_S52:.6e} GeV")
print(f"    tau_naive (S59)   = {hbar_GeV_s / Gamma_naive_S59:.6e} s")
print(f"    tau_naive (S52)   = {hbar_GeV_s / Gamma_naive_S52:.6e} s")

# But Z_2 parity BLOCKS this channel exactly.
# The pair rate from S67 includes the epsilon^4 suppression from pair vertex
# and the KK volume suppression (M_KK/M_Pl)^4.

# Ratio: actual pair rate / naive single rate
ratio_S59 = Gamma_pair_S59 / Gamma_naive_S59 if Gamma_naive_S59 > 0 else 0
ratio_S52 = Gamma_pair_S52 / Gamma_naive_S52 if Gamma_naive_S52 > 0 else 0

# Ratio in log10 to handle extreme dynamic range
log10_ratio_S59 = np.log10(Gamma_pair_S59) - np.log10(Gamma_naive_S59)
log10_ratio_S52 = np.log10(Gamma_pair_S52) - np.log10(Gamma_naive_S52)

print(f"\n  Suppression from Z_2 + pair + KK volume:")
print(f"    Gamma_pair / Gamma_naive (S59) ~ 10^{{{log10_ratio_S59:.1f}}}")
print(f"    Gamma_pair / Gamma_naive (S52) ~ 10^{{{log10_ratio_S52:.1f}}}")
print(f"    log10(suppression) (S59) = {log10_ratio_S59:.1f}")
print(f"    log10(suppression) (S52) = {log10_ratio_S52:.1f}")

# ==============================================================================
#  Step 5: Lifetime comparison
# ==============================================================================

print("\n--- Lifetime Comparison ---")

# Age of universe
t_univ = t_universe_s

# Minimum lifetime for stability (> t_universe)
print(f"\n  t_universe = {t_univ:.3e} s = {t_univ / (365.25*24*3600):.3e} yr")
print(f"  tau_pair (S59) = {tau_pair_s_S59:.3e} s")
print(f"  tau_pair (S52) = {tau_pair_s_S52:.3e} s")
print(f"  tau / t_univ (S59) = {tau_pair_s_S59 / t_univ:.3e}")
print(f"  tau / t_univ (S52) = {tau_pair_s_S52 / t_univ:.3e}")
print(f"  log10(tau / t_univ) (S59) = {np.log10(tau_pair_s_S59 / t_univ):.1f}")
print(f"  log10(tau / t_univ) (S52) = {np.log10(tau_pair_s_S52 / t_univ):.1f}")

# For comparison: proton lifetime lower bound
tau_proton_lower = 1.67e34  # years (Super-K, p -> e+ pi0)  # (local)
tau_proton_lower_s = tau_proton_lower * 365.25 * 24 * 3600
print(f"\n  For reference:")
print(f"    Proton lifetime bound = {tau_proton_lower:.2e} yr = {tau_proton_lower_s:.2e} s")
print(f"    tau_Leggett / tau_proton = {tau_pair_s_S59 / tau_proton_lower_s:.2e}")
print(f"    log10(tau_L / tau_p) = {np.log10(tau_pair_s_S59 / tau_proton_lower_s):.1f}")

# ==============================================================================
#  Step 6: PIXIE forecast sensitivity
# ==============================================================================

print("\n--- PIXIE Forecast ---")
print(f"  PIXIE sigma_mu = {PIXIE_mu_sensitivity:.1e}")
print(f"  log10(delta_mu) = {log10_delta_mu_max:.2f}")
print(f"  log10(delta_mu / PIXIE) = {log10_delta_mu_max - np.log10(PIXIE_mu_sensitivity):.1f}")

# To detect with PIXIE, need delta_mu > sigma_mu ~ 5e-8
# Our log10(delta_mu) ~ -61 is many orders below both bounds
log10_margin_FIRAS = np.log10(FIRAS_mu_bound) - log10_delta_mu_max
log10_margin_PIXIE = np.log10(PIXIE_mu_sensitivity) - log10_delta_mu_max

print(f"  Safety margin vs FIRAS: {log10_margin_FIRAS:.1f} orders of magnitude")
print(f"  Safety margin vs PIXIE: {log10_margin_PIXIE:.1f} orders of magnitude")

# What decay rate WOULD be needed to produce observable distortion?
# delta_mu = FIRAS_mu_bound => f_decay = FIRAS_mu_bound / (1.4 * Omega_DM/Omega_r)
prefactor = 1.4 * Omega_DM / Omega_r
f_decay_threshold_FIRAS = FIRAS_mu_bound / prefactor
tau_threshold_FIRAS = t_universe_s / f_decay_threshold_FIRAS
Gamma_threshold_FIRAS = hbar_GeV_s / tau_threshold_FIRAS

f_decay_threshold_PIXIE = PIXIE_mu_sensitivity / prefactor
tau_threshold_PIXIE = t_universe_s / f_decay_threshold_PIXIE
Gamma_threshold_PIXIE = hbar_GeV_s / tau_threshold_PIXIE

print(f"\n  Threshold for FIRAS detection:")
print(f"    tau_threshold = {tau_threshold_FIRAS:.3e} s  (log10 = {np.log10(tau_threshold_FIRAS):.1f})")
print(f"    Gamma_threshold = {Gamma_threshold_FIRAS:.3e} GeV")
print(f"  Threshold for PIXIE detection:")
print(f"    tau_threshold = {tau_threshold_PIXIE:.3e} s  (log10 = {np.log10(tau_threshold_PIXIE):.1f})")
print(f"    Gamma_threshold = {Gamma_threshold_PIXIE:.3e} GeV")
print(f"  Framework lifetime exceeds FIRAS threshold by {np.log10(tau_pair_s_S59/tau_threshold_FIRAS):.0f} OOM")
print(f"  Framework lifetime exceeds PIXIE threshold by {np.log10(tau_pair_s_S59/tau_threshold_PIXIE):.0f} OOM")

# ==============================================================================
#  Step 7: Gate verdict
# ==============================================================================

print("\n" + "=" * 78)
print("GATE VERDICT: DM-PAIR-DECAY-70")
print("=" * 78)

# Check conditions:
# PASS: Gamma_L * t_universe < sigma_FIRAS (stable against FIRAS)
# FAIL: Gamma_L * t_universe > 1 (decays within age of universe)
# INFO: intermediate

# Gamma * t_universe in natural units (dimensionless)
Gamma_t_S59 = Gamma_pair_S59 * GeV_to_inv_s * t_universe_s
Gamma_t_S52 = Gamma_pair_S52 * GeV_to_inv_s * t_universe_s

print(f"\n  Gamma_pair * t_universe (S59) = {Gamma_t_S59:.6e}")
print(f"  Gamma_pair * t_universe (S52) = {Gamma_t_S52:.6e}")
print(f"  (Both << 1, so NO decays within age of universe)")

# The gate criterion uses Gamma_L * t_universe < sigma_FIRAS as PASS
# But sigma_FIRAS is a dimensionless mu-distortion bound.
# The physically meaningful comparison is: delta_mu < FIRAS bound
# and tau_DM > t_universe.

tau_exceeds_t_univ = tau_pair_s_S59 > t_universe_s
delta_mu_below_FIRAS = log10_delta_mu_max < np.log10(FIRAS_mu_bound)
delta_mu_below_PIXIE = log10_delta_mu_max < np.log10(PIXIE_mu_sensitivity)

print(f"\n  tau_DM > t_universe?          {tau_exceeds_t_univ}  ({tau_pair_s_S59/t_universe_s:.2e}x)")
print(f"  delta_mu < FIRAS bound?       {delta_mu_below_FIRAS}  (10^{{{log10_delta_mu_max:.1f}}} vs {FIRAS_mu_bound:.1e})")
print(f"  delta_mu < PIXIE sensitivity? {delta_mu_below_PIXIE}  (10^{{{log10_delta_mu_max:.1f}}} vs {PIXIE_mu_sensitivity:.1e})")

# Determine verdict
if tau_pair_s_S59 < t_universe_s:
    verdict = "FAIL"
    detail = "Leggett DM decays within the age of the universe"
elif not delta_mu_below_FIRAS:
    verdict = "FAIL"
    detail = "Leggett DM spectral distortion exceeds FIRAS bound"
elif not delta_mu_below_PIXIE:
    verdict = "INFO"
    detail = "Detectable by PIXIE but not FIRAS (intermediate regime)"
else:
    verdict = "PASS"
    detail = ("Leggett DM absolutely stable against spectral distortion. "
              f"Lifetime {tau_pair_s_S59:.1e} s exceeds t_universe by "
              f"{np.log10(tau_pair_s_S59/t_universe_s):.0f} OOM. "
              f"log10(delta_mu) = {log10_delta_mu_max:.1f} is {log10_margin_FIRAS:.0f} OOM "
              f"below FIRAS and {log10_margin_PIXIE:.0f} OOM below PIXIE.")

print(f"\n  VERDICT: {verdict}")
print(f"  DETAIL:  {detail}")

# ==============================================================================
#  Step 8: Protection mechanisms summary
# ==============================================================================

print("\n--- Protection Mechanism Hierarchy ---")
print("  1. Z_2 parity: a_2(phi_23) = a_2(-phi_23)")
print("     -> Single-particle decay L -> g + g FORBIDDEN to all orders")
print(f"     -> Z_2 asymmetry max = {Z2_asymmetry_max:.2e} (machine epsilon)")
print(f"  2. Pair annihilation 2L -> 2g: ALLOWED but epsilon^4 suppressed")
print(f"     -> epsilon_canonical = {float(d['epsilon_canonical']):.6f}")
print(f"     -> epsilon^4 = {float(d['epsilon_canonical'])**4:.6e}")
print(f"  3. KK volume suppression: (M_KK / M_Pl)^4 = {(M_KK_gravity / M_Pl_reduced)**4:.6e}")
print(f"  4. Phase space: omega_L^3 instead of omega_L (pair vs single)")
print(f"  5. Combined: {log10_ratio_S59:.0f} OOM suppression vs naive gravitational decay")
print(f"     -> Lifetime {np.log10(tau_pair_s_S59):.0f} OOM vs naive {np.log10(hbar_GeV_s / Gamma_naive_S59):.0f} OOM")

# ==============================================================================
#  Step 9: Save results
# ==============================================================================

output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "s70_dm_pair_decay.npz")

np.savez(output_path,
    # Gate
    gate_name="DM-PAIR-DECAY-70",
    gate_verdict=verdict,
    gate_detail=detail,
    # Input from S67
    Gamma_single=Gamma_single,
    Gamma_pair_S59=Gamma_pair_S59,
    Gamma_pair_S52=Gamma_pair_S52,
    Gamma_pair_over_H0_S59=Gamma_pair_over_H0_S59,
    Gamma_pair_over_H0_S52=Gamma_pair_over_H0_S52,
    tau_pair_s_S59=tau_pair_s_S59,
    tau_pair_s_S52=tau_pair_s_S52,
    Z2_parity_blocks=Z2_parity_blocks,
    Z2_asymmetry_max=Z2_asymmetry_max,
    # FIRAS/PIXIE comparison
    FIRAS_mu_bound=FIRAS_mu_bound,
    PIXIE_mu_sensitivity=PIXIE_mu_sensitivity,
    log10_delta_mu_max=log10_delta_mu_max,
    log10_margin_FIRAS=log10_margin_FIRAS,
    log10_margin_PIXIE=log10_margin_PIXIE,
    # Naive comparison
    Gamma_naive_S59=Gamma_naive_S59,
    Gamma_naive_S52=Gamma_naive_S52,
    log10_pair_over_naive_S59=log10_ratio_S59,
    log10_pair_over_naive_S52=log10_ratio_S52,
    # Lifetimes
    tau_over_t_univ_S59=tau_pair_s_S59 / t_universe_s,
    tau_over_t_univ_S52=tau_pair_s_S52 / t_universe_s,
    # Thresholds
    tau_threshold_FIRAS_s=tau_threshold_FIRAS,
    Gamma_threshold_FIRAS_GeV=Gamma_threshold_FIRAS,
    tau_threshold_PIXIE_s=tau_threshold_PIXIE,
    Gamma_threshold_PIXIE_GeV=Gamma_threshold_PIXIE,
    # Leggett masses
    m_L_S59_GeV=m_L_S59_GeV,
    m_L_S52_GeV=m_L_S52_GeV,
)

print(f"\n  Data saved to: {output_path}")
print(f"\nDone.")
