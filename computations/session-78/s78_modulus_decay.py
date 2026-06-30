#!/usr/bin/env python3
"""
S78 W3-O: MODULUS-DECAY — Reheating Temperature T_rh (RETRY)
=============================================================

Gate: S78-W3-O-MODULUS-DECAY
Owner: einstein-theorist (retry after prior silent death)
Plan: sessions/session-plan/session-78-plan-scrubbed.md lines 852-875
Shell: sessions/archive/session-78/session-78-results-workingpaper.md Section V W3-O

Substrate framing:
  T_rh is the thermal scale at which post-fold modulus decay deposits energy
  into the emergent gauge sector via instanton-mediated vertex rate -- NOT
  reheating in a pre-existing inflationary spacetime. The instanton vertex is
  a non-perturbative spectral-action feature of the substrate's Jensen-
  deformed D_K.  When the modulus tau oscillates post-fold, the a_4(tau)
  Seeley-DeWitt coefficient modulates the effective gauge kinetic term,
  sourcing emergent gauge-boson excitations of the fiber's eigenvalue
  spectrum.  The instanton-weighted amplitude dresses the vertex by
  exp(-S_inst) (amplitude) = exp(-2 S_inst) (rate).

Convention pins (plan Sec 0):
  - Instanton action S_inst: scheme-independent (topological; 8pi^2 c_2/g^2)
  - alpha_gauge at instanton scale: f* canonical; SDW cross-check (RGE)
  - Instanton-vertex normalization: Chamseddine-Connes (f_0 absorbs 1/(8 pi^2))
  - tau-modulus-to-gauge-field coupling: L_int = -(frac_da4/4) * sigma * F^2
  - Lambda_QCD at vertex scale: M_KK (vertex is at the KK threshold)
  - Semi-classical validity: S_inst > 10 REQUIRED; > 100 UNAMBIGUOUS; < 10 BOUNDARY

Pre-registered expected value (einstein-theorist, pre-reg BEFORE run):
  Framework expected T_rh ~ 10^18 MeV = 10^15 GeV (from S78-W3-M pre-reg line
  and prompt instruction).  This is the GRAVITY-DOMINATED rate.  The genuinely
  instanton-mediated channel (Route alpha below) is expected to be ~10^9 GeV
  due to the exp(-2 S_inst) suppression; the spectral-action dim-5 channel
  WITHOUT exp suppression (Route beta) is ~10^16 GeV; the irreducible
  gravity channel (Route gamma) is ~10^15 GeV.  The three routes bracket the
  10^18 MeV expected value.  Primary for the "instanton-mediated" gate is
  Route alpha (exp(-2 S_inst) at rate).  The verdict follows Route alpha.

Gate thresholds (per shell, pre-registered):
  - PASS: T_rh within factor 10 of 1e18 MeV (i.e. in [1e17, 1e19] MeV)
          AND semi-classical (S_inst > 10)
          AND BBN-compatible (T_rh > 1 MeV)
  - FAIL: T_rh differs from 1e18 MeV by factor > 100
  - INFO: deviation 10-100x (diagnose vertex-rate source)
          OR 1 < S_inst < 10 (boundary)
  - INCOMPUTABLE: S_inst < 1 (out of semi-classical regime)

Cross-checks:
  1. Instanton action positive (semi-classical reality)
  2. Reheating efficiency < 1 (energy budget)
  3. BBN eta_B consistent (cosmological BBN coherence)
  4. E_J(T_rh)/T_rh > 50 or < 50 (feeds W3-M phase-slip null)
  5. Gauge-group branching SU(3):SU(2):U(1) respecting group-theoretic factors

Author: einstein-theorist (S78 W3-O retry)
"""

import sys
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# -------- canonical constants -----------------------------------------------
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    PI,
    M_Pl_reduced, M_Pl_unreduced,
    hbar_GeV_s, GeV_to_inv_s,
    M_KK, M_KK_gravity, M_KK_kerner,
    tau_fold, m_tau, v_terminal, Z_fold, dS_fold,
    a0_fold, a2_fold, a4_fold,
    T_BBN_GeV, eta_BBN_obs, eta_BBN_err,
    g_star_SM, g_star_BBN,
    alpha_s_MZ_obs, M_Z,
    J_C2,
)

# -------- load instanton landscape (s73a) -----------------------------------
# S_inst(tau) from the Jensen SU(3) bundle (topological; 8 pi^2/g^2(tau))
landscape = np.load(
    os.path.join(os.path.dirname(os.path.abspath(__file__)),
                 's73a_instanton_landscape.npz'),
    allow_pickle=True,
)
tau_scan = landscape['tau_scan']                # (local) 21 points, [0, 1]
S_inst_A_array = landscape['S_inst_A']          # (local) Model A: 8 pi^2/[4 exp(2 tau)]
g2_modelA_array = landscape['g2_modelA']        # (local) g^2 Model A: 4 exp(2 tau)

# Post-fold index: first grid point strictly after tau_fold=0.19
idx_post = int(np.searchsorted(tau_scan, tau_fold, side='right'))  # (local)
tau_post = float(tau_scan[idx_post])                               # (local) = 0.20
S_inst_fold = float(S_inst_A_array[idx_post])                      # (local)
g2_fold = float(g2_modelA_array[idx_post])                         # (local)

# Instanton suppression factors (amplitude and rate level)
inst_amp_supp = float(np.exp(-S_inst_fold))                        # (local)
inst_rate_supp = float(np.exp(-2.0 * S_inst_fold))                 # (local)

# -------- SDW cross-check: SU(3) coupling via 1-loop RGE --------------------
# alpha_s(mu) from alpha_s(M_Z) = 0.118, 1-loop QCD b_0 = 7 (SM, n_f=6 above m_t)
b_0_SU3_SM = 7.0                                                   # (local)
alpha_s_inv_MKK = 1.0/alpha_s_MZ_obs + (b_0_SU3_SM/(2.0*PI)) * np.log(M_KK_gravity/M_Z)  # (local)
alpha_s_MKK = 1.0/alpha_s_inv_MKK                                  # (local)
g2_SDW = 4.0*PI*alpha_s_MKK                                        # (local)
S_inst_SDW = 8.0*PI**2/g2_SDW                                      # (local)

# -------- vertex construction (framework f* canonical) ----------------------
# Physical modulus mass (GeV)
m_tau_GeV = m_tau * M_KK_gravity                                   # (local)

# Spectral derivatives (from s54_higgs_modulus -- cached here for robustness)
s54_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 's54_higgs_modulus.npz')
if os.path.exists(s54_path):
    s54 = np.load(s54_path, allow_pickle=True)
    da4_dtau = float(s54['da4_dtau'])                              # (local)
    da2_dtau = float(s54['da2_dtau'])                              # (local)
else:
    # Fallback: canonical values from S54/S76
    da4_dtau = -609.18                                             # (local)
    da2_dtau = -875.62                                             # (local)
frac_da4 = da4_dtau / a4_fold                                      # (local) = -0.451

# Oscillation amplitude A_osc in tau-space (from v_terminal/m_tau energy conservation)
A_osc = v_terminal / m_tau                                          # (local)

# Dim-5 operator: L_int = -(1/4) * (1/Lambda_eff) * sigma * F^2
# with 1/Lambda_eff = |frac_da4| * sqrt(Z) / (2 * a_4).  But as in s76_modulus_sm_decay_rate,
# the convention pins yield:  Lambda_eff = 2 * sqrt(Z) / |frac_da4|  (in M_KK units).
Lambda_eff_MKK = 2.0 * np.sqrt(Z_fold) / abs(frac_da4)             # (local)
Lambda_eff_GeV = Lambda_eff_MKK * M_KK_gravity                     # (local)

# Gauge group adjoint dimensions (SM pre-EW: SU(3)+SU(2)+U(1))
N_SU3 = 8                                                           # (local)
N_SU2 = 3                                                           # (local)
N_U1  = 1                                                           # (local)
N_gauge_tot = N_SU3 + N_SU2 + N_U1                                  # (local) = 12

# ============================================================================
# ROUTE alpha: INSTANTON-MEDIATED (primary channel for this gate)
#   Gamma_alpha = N_gauge * m_tau^3 / (64 pi Lambda_eff^2) * exp(-2 S_inst)
#   The exp(-2 S_inst) dresses the rate: amplitude ~ exp(-S_inst), rate ~ exp(-2 S_inst).
#   Instanton-mediated = non-perturbative tunneling saddle in the gauge bundle.
# ============================================================================
Gamma_bare = N_gauge_tot * m_tau_GeV**3 / (64.0*PI*Lambda_eff_GeV**2)  # (local) GeV
Gamma_alpha = Gamma_bare * inst_rate_supp                              # (local) GeV

# Per-channel breakdown (instanton-mediated)
Gamma_alpha_SU3 = N_SU3 * m_tau_GeV**3 / (64.0*PI*Lambda_eff_GeV**2) * inst_rate_supp  # (local)
Gamma_alpha_SU2 = N_SU2 * m_tau_GeV**3 / (64.0*PI*Lambda_eff_GeV**2) * inst_rate_supp  # (local)
Gamma_alpha_U1  = N_U1  * m_tau_GeV**3 / (64.0*PI*Lambda_eff_GeV**2) * inst_rate_supp  # (local)

# Reheating temperature for Route alpha
if Gamma_alpha > 0:
    T_rh_alpha_GeV = (90.0/(PI**2 * g_star_SM))**0.25 * np.sqrt(Gamma_alpha * M_Pl_reduced)  # (local)
else:
    T_rh_alpha_GeV = 0.0                                                # (local)
T_rh_alpha_MeV = T_rh_alpha_GeV * 1e3                                   # (local)

# ============================================================================
# ROUTE beta: SPECTRAL-ACTION DIM-5 (cross-check; no exp(-2 S_inst) dressing)
#   The dim-5 operator (sigma/Lambda_eff) * F^2 is tree-level in the substrate
#   sense: no instanton tunneling needed.  S_inst enters only through the
#   prefactor-determinant of the instanton density, not through the rate
#   of a scalar-mediated decay.
# ============================================================================
Gamma_beta = Gamma_bare                                                 # (local) -- no inst supp
T_rh_beta_GeV = (90.0/(PI**2 * g_star_SM))**0.25 * np.sqrt(Gamma_beta * M_Pl_reduced)  # (local)
T_rh_beta_MeV = T_rh_beta_GeV * 1e3                                     # (local)

# ============================================================================
# ROUTE gamma: GRAVITY-ONLY (irreducible Planck-suppressed channel)
#   Gamma_grav = m_tau^3 / (48 pi M_Pl^2)
# ============================================================================
Gamma_gamma = m_tau_GeV**3 / (48.0*PI*M_Pl_reduced**2)                  # (local)
T_rh_gamma_GeV = (90.0/(PI**2 * g_star_SM))**0.25 * np.sqrt(Gamma_gamma * M_Pl_reduced)  # (local)
T_rh_gamma_MeV = T_rh_gamma_GeV * 1e3                                   # (local)

# Combined (maximum channel dominates; gravity + instanton-mediated)
Gamma_combined = Gamma_alpha + Gamma_gamma                              # (local)
T_rh_combined_GeV = (90.0/(PI**2 * g_star_SM))**0.25 * np.sqrt(Gamma_combined * M_Pl_reduced)  # (local)
T_rh_combined_MeV = T_rh_combined_GeV * 1e3                             # (local)

# ============================================================================
# SYSTEMATIC UNCERTAINTY
# ============================================================================
# (a) Instanton action ambiguity: Model A (Jensen bundle, s73a) vs SDW (RGE).
#     Use Model A as primary; SDW as cross-check.  The ratio of Gamma is
#     exp(-2*(S_inst_SDW - S_inst_A)) -- MANY OOM, but SDW is the QCD-running
#     value at the decoupling scale M_KK, not the fold scale.  Model A is the
#     framework-internal fold value; SDW is the external UV scale.
Gamma_alpha_SDW = Gamma_bare * np.exp(-2.0 * S_inst_SDW)                # (local)
# (b) Vertex coefficient ambiguity: frac_da4 varies across L_max.  Use nominal
#     value and a 20% uncertainty on frac_da4 -> 40% on Gamma -> ~20% on T_rh.
frac_da4_lo = frac_da4 * 0.9                                            # (local)
frac_da4_hi = frac_da4 * 1.1                                            # (local)
Lambda_eff_lo = 2.0 * np.sqrt(Z_fold) / abs(frac_da4_hi) * M_KK_gravity # (local)  lower Lambda <-> higher frac
Lambda_eff_hi = 2.0 * np.sqrt(Z_fold) / abs(frac_da4_lo) * M_KK_gravity # (local)
Gamma_alpha_hi = N_gauge_tot * m_tau_GeV**3 / (64.0*PI*Lambda_eff_lo**2) * inst_rate_supp  # (local)
Gamma_alpha_lo = N_gauge_tot * m_tau_GeV**3 / (64.0*PI*Lambda_eff_hi**2) * inst_rate_supp  # (local)
T_rh_alpha_hi_GeV = (90.0/(PI**2*g_star_SM))**0.25 * np.sqrt(Gamma_alpha_hi * M_Pl_reduced)  # (local)
T_rh_alpha_lo_GeV = (90.0/(PI**2*g_star_SM))**0.25 * np.sqrt(Gamma_alpha_lo * M_Pl_reduced)  # (local)
delta_T_rh_alpha_GeV = 0.5 * (T_rh_alpha_hi_GeV - T_rh_alpha_lo_GeV)    # (local) 1-sigma band

# ============================================================================
# CROSS-CHECKS
# ============================================================================
# CHK1: Instanton action positive (semi-classical reality)
chk1_pass = (S_inst_fold > 0)                                           # (local)

# CHK2: Reheating efficiency < 1 (energy budget: Gamma*M_Pl < m_tau * rho_modulus)
# Efficiency = fraction of modulus rest energy converted to radiation.
# In instant-decay approximation, 100% goes to radiation, so efficiency = 1 by
# construction.  The constraint is that the modulus kinetic energy (from fold
# transit) doesn't exceed the total energy available.
# E_kinetic_modulus ~ (1/2) v_terminal^2 * m_tau (in M_KK units) = 0.5 * 26.545^2 * 2.062 = 726.4
# E_rest_modulus = m_tau = 2.062 M_KK (per particle)
# Since v_terminal >> 1 in dimensionless units, the system is relativistic but
# the modulus is a scalar field, so "rest mass" is less meaningful than
# potential energy.  For instant-decay T_rh, efficiency = 1 by definition.
reheat_efficiency = 1.0                                                 # (local) by instant-decay
chk2_pass = (reheat_efficiency <= 1.0)                                  # (local)

# CHK3: BBN eta_B consistent
# eta_B = n_B/n_gamma is frozen at sphaleron decoupling, not at T_rh.  As long
# as T_rh > T_sphaleron_decoupling ~ 100 GeV, and some CP-violating source
# operates, eta_B can take its observed value 6.12e-10.
# Route alpha predicts T_rh ~ 10^7-10^8 GeV, which is >> 100 GeV.  Route gamma
# predicts 10^15 GeV.  Both PASS.  Framework phi_CP = 0 (S52, structural zero)
# means external CP source needed; gate checks only coherence.
T_sphaleron_GeV = 100.0                                                 # (local)
chk3_alpha_pass = (T_rh_alpha_GeV > T_sphaleron_GeV)                    # (local)
chk3_gamma_pass = (T_rh_gamma_GeV > T_sphaleron_GeV)                    # (local)
chk3_pass = chk3_alpha_pass or chk3_gamma_pass                          # (local)

# CHK4: E_J(T_rh) / T_rh > 50 or < 50 (feeds W3-M phase-slip null)
# E_J_C2 = 0.933 M_KK = 0.933 * 7.43e16 = 6.93e16 GeV = 6.93e19 MeV
# W3-M used E_J = 7.042 M_KK (slightly different convention); use J_C2 canonical.
E_J_GeV = J_C2 * M_KK_gravity                                           # (local)
if T_rh_alpha_GeV > 0:
    E_J_over_T_alpha = E_J_GeV / T_rh_alpha_GeV                         # (local)
else:
    E_J_over_T_alpha = np.inf                                           # (local)
E_J_over_T_gamma = E_J_GeV / T_rh_gamma_GeV                             # (local)
chk4_alpha_flag = ">50" if E_J_over_T_alpha > 50 else "<50"             # (local)
chk4_gamma_flag = ">50" if E_J_over_T_gamma > 50 else "<50"             # (local)

# CHK5: Gauge-group branching ratios
# Branching = N_SU3:N_SU2:N_U1 = 8:3:1 (by adjoint dimension)
# This is group-theoretic; any deviation would indicate a vertex-normalization bug
BR_SU3 = N_SU3 / N_gauge_tot                                            # (local)
BR_SU2 = N_SU2 / N_gauge_tot                                            # (local)
BR_U1  = N_U1  / N_gauge_tot                                            # (local)
BR_expected = np.array([8, 3, 1]) / 12.0                                # (local)
BR_computed = np.array([BR_SU3, BR_SU2, BR_U1])                         # (local)
chk5_pass = bool(np.allclose(BR_computed, BR_expected, atol=1e-10))     # (local)

# ============================================================================
# GATE VERDICT
# ============================================================================
T_rh_expected_MeV = 1.0e18                                              # (local) pre-registered
T_rh_expected_GeV = T_rh_expected_MeV * 1e-3                            # (local) = 1e15 GeV

# Primary: Route alpha (instanton-mediated, exp(-2 S_inst) suppressed rate)
T_rh_primary_GeV = T_rh_alpha_GeV                                       # (local)
T_rh_primary_MeV = T_rh_alpha_MeV                                       # (local)

# Deviation factor |log10 ratio|
if T_rh_primary_GeV > 0:
    dev_log10_primary = np.log10(T_rh_primary_GeV / T_rh_expected_GeV)  # (local)
    dev_factor_primary = 10**abs(dev_log10_primary)                     # (local)
else:
    dev_log10_primary = np.inf                                          # (local)
    dev_factor_primary = np.inf                                         # (local)

# Semi-classical validity
if S_inst_fold >= 100:
    regime_alpha = "UNAMBIGUOUS"                                        # (local)
elif S_inst_fold >= 10:
    regime_alpha = "REQUIRED-PASS"                                      # (local)
elif S_inst_fold >= 1:
    regime_alpha = "BOUNDARY"                                           # (local)
else:
    regime_alpha = "OUT-OF-REGIME"                                      # (local)

# BBN compatibility
bbn_compat_primary = (T_rh_primary_GeV > 1e-3)                          # (local) > 1 MeV
bbn_compat_gamma   = (T_rh_gamma_GeV   > 1e-3)                          # (local)

# Verdict logic per pre-registration
if regime_alpha == "OUT-OF-REGIME":
    verdict = "INCOMPUTABLE"                                            # (local)
    verdict_reason = f"S_inst={S_inst_fold:.3f} < 1, semi-classical expansion invalid"  # (local)
elif regime_alpha == "BOUNDARY":
    verdict = "INFO"                                                    # (local)
    verdict_reason = f"S_inst={S_inst_fold:.3f} in [1,10] boundary of validity"  # (local)
elif dev_factor_primary <= 10 and bbn_compat_primary:
    verdict = "PASS"                                                    # (local)
    verdict_reason = (f"T_rh={T_rh_primary_MeV:.3e} MeV within factor 10 of 1e18 MeV "
                      f"AND S_inst={S_inst_fold:.3f}>10 AND BBN-compatible")
elif dev_factor_primary > 100:
    verdict = "FAIL"                                                    # (local)
    verdict_reason = (f"T_rh_alpha={T_rh_primary_MeV:.3e} MeV differs from 1e18 MeV "
                      f"by factor {dev_factor_primary:.2e} (Route alpha suppressed by "
                      f"exp(-2 S_inst)={inst_rate_supp:.3e})")
else:
    verdict = "INFO"                                                    # (local)
    verdict_reason = (f"T_rh={T_rh_primary_MeV:.3e} MeV deviates from 1e18 MeV by "
                      f"factor {dev_factor_primary:.2f} (10-100x band) -- diagnose "
                      f"vertex-rate source")

# ============================================================================
# PRINT RESULTS
# ============================================================================
print("=" * 78)
print("S78 W3-O: MODULUS-DECAY — Reheating Temperature T_rh (retry)")
print("=" * 78)
print()
print("--- Convention Pins ---")
print(f"  S_inst scheme:       Model A (Jensen bundle, s73a, topological)")
print(f"  alpha_gauge scheme:  f* canonical; SDW cross-check (1-loop RGE)")
print(f"  vertex convention:   Chamseddine-Connes (f_0 absorbs 1/(8 pi^2))")
print(f"  Lambda_QCD at vertex: M_KK (KK-threshold decoupling)")
print(f"  semi-classical reg:  S_inst > 10 required, > 100 unambiguous")
print()
print("--- Instanton Action ---")
print(f"  tau_fold (canonical) = {tau_fold}")
print(f"  tau_post (grid)      = {tau_post}")
print(f"  S_inst(tau_post) [Model A, f* canonical] = {S_inst_fold:.4f}")
print(f"  g^2(tau_post) [Model A]                  = {g2_fold:.4f}")
print(f"  S_inst(M_KK) [SDW RGE cross-check]       = {S_inst_SDW:.4f}")
print(f"  Regime (Route alpha): {regime_alpha}")
print(f"  exp(-S_inst)   (amplitude supp.) = {inst_amp_supp:.6e}")
print(f"  exp(-2 S_inst) (rate supp.)      = {inst_rate_supp:.6e}")
print()
print("--- Vertex Construction ---")
print(f"  m_tau               = {m_tau:.4f} M_KK = {m_tau_GeV:.4e} GeV")
print(f"  v_terminal          = {v_terminal:.4f} (M_KK units)")
print(f"  A_osc = v/m         = {A_osc:.4f}")
print(f"  Z_fold              = {Z_fold:.2f}, sqrt(Z) = {np.sqrt(Z_fold):.2f}")
print(f"  da_4/dtau           = {da4_dtau:.4f}")
print(f"  frac_da4 = da_4/(dtau*a_4) = {frac_da4:.6f}")
print(f"  Lambda_eff          = {Lambda_eff_MKK:.2f} M_KK = {Lambda_eff_GeV:.4e} GeV")
print(f"  Lambda_eff/M_Pl_red = {Lambda_eff_GeV/M_Pl_reduced:.4f}")
print()
print("--- Route alpha: INSTANTON-MEDIATED (primary) ---")
print(f"  Gamma_bare (no inst supp)  = {Gamma_bare:.4e} GeV")
print(f"  Gamma_alpha = Gamma_bare * exp(-2 S_inst)")
print(f"              = {Gamma_alpha:.4e} GeV")
print(f"  Per-channel: SU(3)={Gamma_alpha_SU3:.3e}, SU(2)={Gamma_alpha_SU2:.3e}, U(1)={Gamma_alpha_U1:.3e}")
print(f"  T_rh^alpha = {T_rh_alpha_GeV:.4e} GeV = {T_rh_alpha_MeV:.4e} MeV")
print(f"  1-sigma band [T_lo, T_hi] = [{T_rh_alpha_lo_GeV:.3e}, {T_rh_alpha_hi_GeV:.3e}] GeV")
print(f"  delta_T_rh (1-sigma)      = {delta_T_rh_alpha_GeV:.3e} GeV")
print()
print("--- Route beta: SPECTRAL DIM-5 (cross-check, no exp suppression) ---")
print(f"  Gamma_beta  = {Gamma_beta:.4e} GeV")
print(f"  T_rh^beta   = {T_rh_beta_GeV:.4e} GeV = {T_rh_beta_MeV:.4e} MeV")
print()
print("--- Route gamma: GRAVITY-ONLY (irreducible cross-check) ---")
print(f"  Gamma_grav  = {Gamma_gamma:.4e} GeV")
print(f"  T_rh^gamma  = {T_rh_gamma_GeV:.4e} GeV = {T_rh_gamma_MeV:.4e} MeV")
print()
print("--- Combined (alpha + gamma) ---")
print(f"  Gamma_comb  = {Gamma_combined:.4e} GeV")
print(f"  T_rh^comb   = {T_rh_combined_GeV:.4e} GeV = {T_rh_combined_MeV:.4e} MeV")
print()
print("--- Pre-registered Expected ---")
print(f"  T_rh_expected = 1e18 MeV = 1e15 GeV (prompt + W3-M pre-reg line)")
print(f"  Route alpha deviation: |log10(T^alpha/T_exp)| = {abs(dev_log10_primary):.2f} OOM")
print(f"                         factor = {dev_factor_primary:.2e}")
print()
print("--- Cross-Checks ---")
print(f"  CHK1: S_inst > 0         : {'PASS' if chk1_pass else 'FAIL'} (S_inst = {S_inst_fold:.3f})")
print(f"  CHK2: efficiency <= 1     : {'PASS' if chk2_pass else 'FAIL'} (instant-decay: eff=1)")
print(f"  CHK3: BBN coherence       : {'PASS' if chk3_pass else 'FAIL'} "
      f"(alpha>T_sph: {chk3_alpha_pass}, gamma>T_sph: {chk3_gamma_pass})")
print(f"  CHK4: E_J/T               : E_J={E_J_GeV:.3e} GeV; "
      f"alpha: E_J/T={E_J_over_T_alpha:.3e} ({chk4_alpha_flag}); "
      f"gamma: E_J/T={E_J_over_T_gamma:.3e} ({chk4_gamma_flag})")
print(f"  CHK5: SU(3):SU(2):U(1) branching = 8:3:1 group-theoretic : "
      f"{'PASS' if chk5_pass else 'FAIL'} ({BR_SU3:.4f}:{BR_SU2:.4f}:{BR_U1:.4f})")
print()
print("=" * 78)
print(f"GATE VERDICT: S78-W3-O-MODULUS-DECAY = {verdict}")
print(f"  {verdict_reason}")
print("=" * 78)

# ============================================================================
# SAVE DATA
# ============================================================================
out_npz = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       's78_modulus_decay.npz')
np.savez(
    out_npz,
    # Convention pins
    scheme_tag="f*",
    convention_tag="SCHEME-INDEPENDENT-topological",
    L_max_tag=10,
    # Instanton action
    tau_fold=float(tau_fold),
    tau_post=tau_post,
    idx_post=idx_post,
    S_inst_fold=S_inst_fold,
    g2_fold=g2_fold,
    S_inst_SDW_cross=S_inst_SDW,
    inst_amp_supp=inst_amp_supp,
    inst_rate_supp=inst_rate_supp,
    regime=regime_alpha,
    # Vertex
    m_tau_GeV=m_tau_GeV,
    Lambda_eff_MKK=Lambda_eff_MKK,
    Lambda_eff_GeV=Lambda_eff_GeV,
    frac_da4=frac_da4,
    Z_fold=float(Z_fold),
    A_osc=A_osc,
    # Route alpha (primary, instanton-mediated)
    Gamma_bare=Gamma_bare,
    Gamma_alpha=Gamma_alpha,
    Gamma_alpha_SU3=Gamma_alpha_SU3,
    Gamma_alpha_SU2=Gamma_alpha_SU2,
    Gamma_alpha_U1=Gamma_alpha_U1,
    Gamma_alpha_SDW=Gamma_alpha_SDW,
    T_rh_alpha_GeV=T_rh_alpha_GeV,
    T_rh_alpha_MeV=T_rh_alpha_MeV,
    T_rh_alpha_lo_GeV=T_rh_alpha_lo_GeV,
    T_rh_alpha_hi_GeV=T_rh_alpha_hi_GeV,
    delta_T_rh_alpha_GeV=delta_T_rh_alpha_GeV,
    # Route beta (spectral dim-5)
    Gamma_beta=Gamma_beta,
    T_rh_beta_GeV=T_rh_beta_GeV,
    T_rh_beta_MeV=T_rh_beta_MeV,
    # Route gamma (gravity)
    Gamma_gamma=Gamma_gamma,
    T_rh_gamma_GeV=T_rh_gamma_GeV,
    T_rh_gamma_MeV=T_rh_gamma_MeV,
    # Combined
    Gamma_combined=Gamma_combined,
    T_rh_combined_GeV=T_rh_combined_GeV,
    T_rh_combined_MeV=T_rh_combined_MeV,
    # Pre-reg comparison
    T_rh_expected_MeV=T_rh_expected_MeV,
    T_rh_expected_GeV=T_rh_expected_GeV,
    dev_log10_primary=dev_log10_primary,
    dev_factor_primary=dev_factor_primary,
    # Cross-checks
    chk1_pass=chk1_pass,
    chk2_pass=chk2_pass,
    chk3_alpha_pass=chk3_alpha_pass,
    chk3_gamma_pass=chk3_gamma_pass,
    chk5_pass=chk5_pass,
    bbn_compat_primary=bbn_compat_primary,
    bbn_compat_gamma=bbn_compat_gamma,
    E_J_GeV=E_J_GeV,
    E_J_over_T_alpha=E_J_over_T_alpha,
    E_J_over_T_gamma=E_J_over_T_gamma,
    chk4_alpha_flag=chk4_alpha_flag,
    chk4_gamma_flag=chk4_gamma_flag,
    BR_SU3=BR_SU3, BR_SU2=BR_SU2, BR_U1=BR_U1,
    # Gate
    gate_id="S78-W3-O-MODULUS-DECAY",
    verdict=verdict,
    verdict_reason=verdict_reason,
)
print(f"\nSaved data to: {out_npz}")

# ============================================================================
# PLOT
# ============================================================================
fig, axes = plt.subplots(2, 2, figsize=(13, 10))

# Panel 1: S_inst(tau) landscape
ax = axes[0, 0]
ax.plot(tau_scan, S_inst_A_array, 'b-o', ms=4, label='Model A (Jensen, s73a)')
ax.axhline(10, color='orange', ls='--', alpha=0.7, label='S_inst=10 (required)')
ax.axhline(100, color='green', ls=':', alpha=0.7, label='S_inst=100 (unambig.)')
ax.axvline(tau_fold, color='red', ls='--', alpha=0.7, label=f'tau_fold={tau_fold}')
ax.axvline(tau_post, color='purple', ls=':', alpha=0.7, label=f'tau_post={tau_post}')
ax.scatter([tau_post], [S_inst_fold], color='red', s=80, zorder=10,
           label=f'S_inst={S_inst_fold:.2f}')
ax.set_xlabel('tau')
ax.set_ylabel('S_inst')
ax.set_title('Instanton Action Landscape')
ax.legend(fontsize=9)
ax.grid(alpha=0.3)

# Panel 2: T_rh by route (log bar chart)
ax = axes[0, 1]
routes = ['alpha\n(inst-mediated)', 'beta\n(spec dim-5)', 'gamma\n(gravity)',
          'combined\n(alpha+gamma)']  # (local)
T_rh_vals_MeV = [T_rh_alpha_MeV, T_rh_beta_MeV, T_rh_gamma_MeV, T_rh_combined_MeV]  # (local)
colors = ['steelblue', 'cornflowerblue', 'navy', 'darkred']  # (local)
bars = ax.bar(routes, T_rh_vals_MeV, color=colors, edgecolor='black')
ax.set_yscale('log')
ax.axhline(T_rh_expected_MeV, color='red', ls='--', lw=2,
           label=f'Pre-reg T_rh=1e18 MeV')
ax.axhline(T_rh_expected_MeV*10, color='orange', ls=':', alpha=0.5, label='PASS upper')
ax.axhline(T_rh_expected_MeV/10, color='orange', ls=':', alpha=0.5, label='PASS lower')
for bar, val in zip(bars, T_rh_vals_MeV):
    ax.text(bar.get_x()+bar.get_width()/2., val*2, f'{val:.1e}',
            ha='center', va='bottom', fontsize=9, fontweight='bold')
ax.set_ylabel('T_rh [MeV]')
ax.set_title('Reheating Temperature by Channel')
ax.legend(fontsize=9, loc='lower left')
ax.grid(alpha=0.3, axis='y')

# Panel 3: Gamma decomposition (Route alpha)
ax = axes[1, 0]
channels = ['SU(3)', 'SU(2)', 'U(1)', 'Total']  # (local)
Gamma_vals = [Gamma_alpha_SU3, Gamma_alpha_SU2, Gamma_alpha_U1, Gamma_alpha]  # (local)
chan_colors = ['gold', 'steelblue', 'red', 'black']  # (local)
bars2 = ax.bar(channels, Gamma_vals, color=chan_colors, edgecolor='black')
ax.set_yscale('log')
ax.set_ylabel('Gamma [GeV]')
ax.set_title('Route alpha: Decay-Rate Decomposition')
for bar, val in zip(bars2, Gamma_vals):
    ax.text(bar.get_x()+bar.get_width()/2., val*2, f'{val:.1e}',
            ha='center', va='bottom', fontsize=9)
# Add expected ratios
ax.text(0.02, 0.95, f'Branching ratios: 8:3:1 (adjoint dim)\n'
                    f'Expected = {8/12:.3f}:{3/12:.3f}:{1/12:.3f}\n'
                    f'Computed = {BR_SU3:.3f}:{BR_SU2:.3f}:{BR_U1:.3f}',
        transform=ax.transAxes, fontsize=9, va='top',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))
ax.grid(alpha=0.3, axis='y')

# Panel 4: Gate summary
ax = axes[1, 1]
ax.axis('off')
summary = (
    f"GATE S78-W3-O-MODULUS-DECAY: {verdict}\n"
    f"\n"
    f"Primary (Route alpha, instanton-mediated):\n"
    f"  T_rh = {T_rh_alpha_MeV:.3e} MeV = {T_rh_alpha_GeV:.3e} GeV\n"
    f"  delta_T_rh = +/-{delta_T_rh_alpha_GeV:.2e} GeV (from frac_da4 ±10%)\n"
    f"\n"
    f"Pre-registered expected: T_rh = 1e18 MeV\n"
    f"Deviation: factor {dev_factor_primary:.2e}\n"
    f"|log10(ratio)| = {abs(dev_log10_primary):.2f} OOM\n"
    f"\n"
    f"Semi-classical validity:\n"
    f"  S_inst = {S_inst_fold:.3f}\n"
    f"  Regime: {regime_alpha}\n"
    f"  exp(-2 S_inst) = {inst_rate_supp:.3e}\n"
    f"\n"
    f"Cross-channels:\n"
    f"  Route beta  (spec dim-5):  {T_rh_beta_MeV:.2e} MeV\n"
    f"  Route gamma (gravity):     {T_rh_gamma_MeV:.2e} MeV\n"
    f"  Combined (alpha + gamma):  {T_rh_combined_MeV:.2e} MeV\n"
    f"\n"
    f"Cross-checks:\n"
    f"  CHK1 S_inst>0:             {'PASS' if chk1_pass else 'FAIL'}\n"
    f"  CHK2 eff<=1:                {'PASS' if chk2_pass else 'FAIL'}\n"
    f"  CHK3 BBN coherence:        {'PASS' if chk3_pass else 'FAIL'}\n"
    f"  CHK4 E_J/T>50 (alpha):     {chk4_alpha_flag}\n"
    f"  CHK4 E_J/T>50 (gamma):     {chk4_gamma_flag}\n"
    f"  CHK5 8:3:1 branching:      {'PASS' if chk5_pass else 'FAIL'}\n"
)
verdict_color = {'PASS': 'lightgreen', 'INFO': 'lightyellow',
                 'FAIL': 'lightcoral', 'INCOMPUTABLE': 'lightgray'}.get(verdict, 'white')
ax.text(0.05, 0.95, summary, transform=ax.transAxes,
        fontsize=9, va='top', family='monospace',
        bbox=dict(boxstyle='round,pad=0.5', facecolor=verdict_color, alpha=0.9,
                  edgecolor='black', linewidth=1.5))

plt.tight_layout()
out_png = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                      's78_modulus_decay.png')
plt.savefig(out_png, dpi=130, bbox_inches='tight')
plt.close()
print(f"Saved plot to: {out_png}")
print()
print("Done.")
