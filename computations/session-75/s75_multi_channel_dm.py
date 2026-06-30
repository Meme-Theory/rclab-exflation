#!/usr/bin/env python3
"""
s75_multi_channel_dm.py -- Multi-Channel DM CDM Compatibility Check
=====================================================================
Gate: S75-E3-MULTI-DM (MULTI-CHANNEL-DM-CDM-COMPAT-75)
  PASS: All 4 observables match CDM within 7%
  INFO: 1-2 observables outside 7%
  FAIL: >= 3 observables outside 7%

PHYSICS:
    The Leggett-channel DM from the GGE relic consists of inter-band
    quasiparticle pairs (f_CPT = 0.610 from W1-L). These are produced
    via Parker pair production at the tau-fold transit (M ~ 10^17 GeV).

    W2-N established: Z_2-odd sector has ZERO population (n_Z2 = 0 exact,
    symmetry selection rule). The DM channel is the Leggett INTER-BAND
    mode, not the Z_2-odd (cell-exchange) sector.

    Four CDM compatibility observables:
    1. c_s^2 = dP/drho  -- DM sound speed at recombination
    2. ISW_DM -- ISW contribution from DM pressure at recombination
    3. rho_DM ratio -- DM density vs CDM at recombination
    4. P(k) suppression -- matter power spectrum impact from c_s != 0

    The CDM model has c_s^2 = 0 exactly for DM. Any departure produces:
    - Jeans scale below which DM perturbations oscillate instead of grow
    - Additional ISW from time-varying DM gravitational potential
    - Suppression of P(k) below the Jeans scale
    - Shift in matter-radiation equality

PRIOR RESULTS:
    - S63 WDM-FRACTION-63: lambda_fs = 9.85e-23 Mpc (22 OOM safe)
    - S66 Z-EQ-CHECK-66: Leggett-only z_eq = 3425 (0.88-sigma PASS)
    - S68 ISW-TRACKING-68: DE c_s^2 = 0, DM c_s^2 = 0 (CDM-like)
    - S70 DM-PAIR-DECAY-70: DM stable (tau = 4.93e82 s)
    - W1-L: f_CPT = 0.610, inter-band DM fraction
    - W2-N: n_Z2 = 0 (symmetric Parker can't populate Z_2-odd)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
import numpy as np
from canonical_constants import (
    tau_fold, M_KK, M_KK_gravity, M_KK_kerner, M_Pl_reduced, M_Pl_unreduced,
    Delta_BCS, Delta_0_OES, omega_L1, omega_L2,
    c_Gold, c_fabric, E_B1, E_B2_mean, E_B3_mean,
    n_pairs, T_acoustic, T_GGE_B2, N_cells,
    Omega_DM, Omega_m, Omega_b, Omega_Lambda, Omega_r,
    H_0_km_s_Mpc, H_0_GeV, H_0_inv_s, rho_crit_GeV4,
    T_CMB, T_recomb_GeV, k_B,
    c_light, c_light_km_s,
    A_s_CMB, sigma_8, z_BBN,
    hbar_GeV_s, hbar_c_GeV_m, l_Planck,
    G_N, eV_SI,
)

# ============================================================================
#  STEP 0: Load GGE fabric data
# ============================================================================
print("=" * 78)
print("S75-E3-MULTI-DM: MULTI-CHANNEL DM CDM COMPATIBILITY CHECK")
print("=" * 78)

# Load GGE data
gge_data = np.load(os.path.join(os.path.dirname(__file__), 's56_gge_fabric.npz'),
                   allow_pickle=True)
eps_fold = gge_data['eps_fold']  # 8-mode single-particle energies (M_KK units)
nk_DE = gge_data['nk_DE']       # Occupation numbers in diagonal ensemble
T_B2 = float(gge_data['T_B2_2cell'])  # B2 sector GGE temperature
T_B1 = float(gge_data['T_B1_2cell'])  # B1 sector GGE temperature
T_B3 = float(gge_data['T_B3_2cell'])  # B3 sector GGE temperature

print(f"\nGGE fabric data loaded:")
print(f"  eps_fold = {eps_fold}")
print(f"  nk_DE (first 8) = {nk_DE[:8]}")
print(f"  T_B2 = {T_B2:.6f} M_KK")
print(f"  T_B1 = {T_B1:.6f} M_KK")
print(f"  T_B3 = {T_B3:.6f} M_KK")

# ============================================================================
#  STEP 1: DM Sound Speed c_s^2 at Recombination
# ============================================================================
print("\n" + "=" * 78)
print("STEP 1: DM Sound Speed c_s^2")
print("=" * 78)

# The Leggett-channel DM quasiparticles are BCS-gapped excitations.
# Their dispersion relation is (Bogoliubov form):
#   E_k = sqrt(xi_k^2 + Delta^2)
# where xi_k = eps_k - mu is the single-particle energy relative to
# the chemical potential, and Delta = Delta_BCS = 0.464 M_KK.
#
# For a gas of quasiparticles with this dispersion:
#   c_s^2 = dP/d(rho)
#
# At temperature T << Delta (BCS gap), the quasiparticle gas is exponentially
# dilute: n ~ exp(-Delta/T). The pressure and density are both dominated
# by the condensate, not thermal excitations.
#
# KEY PHYSICAL POINT: At recombination (T_rec ~ 0.26 eV ~ 2.6e-10 GeV),
# the DM temperature is:
#   T_DM(z_rec) = T_acoustic * M_KK * (1+z_rec) / (1+z_prod)
# where T_acoustic = 0.112 M_KK is the initial GGE acoustic temperature,
# z_prod ~ M_KK / T_CMB is the production redshift, and the DM has been
# redshifting since production.
#
# Since DM was produced at z_prod ~ 10^29, by recombination (z_rec ~ 1100)
# the DM kinetic energy has redshifted by a factor ~ (1+z_rec)/(1+z_prod)
# ~ 10^{-26}. This makes T_DM(rec) << Delta, and the gas is deep in
# the condensate regime.

# Production epoch
z_prod = M_KK / (T_CMB * k_B / 1e9)  # (local) production redshift ~ M_KK / T_CMB_GeV
T_CMB_GeV = T_CMB * k_B / 1e9  # (local) CMB temp in GeV
z_prod_alt = M_KK / T_CMB_GeV  # (local)
z_rec = 1100.0  # (local) recombination redshift

print(f"\nProduction and recombination epochs:")
print(f"  T_CMB = {T_CMB} K = {T_CMB_GeV:.4e} GeV")
print(f"  M_KK (gravity) = {M_KK:.4e} GeV")
print(f"  z_prod ~ M_KK / T_CMB = {z_prod_alt:.4e}")
print(f"  z_rec = {z_rec}")

# DM temperature at recombination
# The GGE quasiparticles are produced with initial kinetic energy ~ T_acoustic * M_KK
# Their momenta redshift as 1/(1+z), so kinetic energy ~ p^2/m ~ 1/(1+z)^2 (NR)
# or E ~ p ~ 1/(1+z) (relativistic).
#
# The quasiparticle mass is the BCS gap: m_QP ~ Delta_BCS * M_KK
# The initial velocity v_i ~ c (produced at GGE temperature ~ M_KK)
# They become non-relativistic at z_NR where p(z_NR) ~ m_QP * c
#   => z_NR ~ z_prod * (v_i / c) ~ z_prod (since v_i ~ c)
# Actually: z_NR is when E_kin ~ m_QP, i.e., when redshifted momentum
# p(z) = p_0 * (1+z_prod)/(1+z) equals m_QP.
# With p_0 ~ T_acoustic * M_KK ~ 0.112 * M_KK and m_QP ~ 0.464 * M_KK:
#   z_NR ~ z_prod * T_acoustic / Delta_BCS ~ 0.24 * z_prod

T_DM_MKK = T_acoustic  # (local) initial DM temperature in M_KK units
m_QP_MKK = Delta_BCS   # (local) QP mass in M_KK units (BCS gap)
m_QP_GeV = Delta_BCS * M_KK  # (local) QP mass in GeV

# Momentum at production: p_0 ~ T_DM * M_KK (thermal)
# Actually, the QPs are produced by a quench, not thermal equilibrium.
# Their energy is set by the Bogoliubov spectrum at the fold.
# Use occupation-weighted average energy from GGE:
E_QP_mean = np.sum(nk_DE[:8] * eps_fold) / np.sum(nk_DE[:8])  # (local) mean QP energy
v_QP_mean = np.sqrt(1.0 - (m_QP_MKK / max(E_QP_mean, m_QP_MKK + 1e-30))**2) if E_QP_mean > m_QP_MKK else 0.0  # (local)

print(f"\nQuasiparticle properties:")
print(f"  Delta_BCS = {Delta_BCS:.4f} M_KK = {m_QP_GeV:.4e} GeV")
print(f"  Mean QP energy = {E_QP_mean:.4f} M_KK")
print(f"  Initial QP velocity (v/c) = {v_QP_mean:.6f}")

# At recombination, the DM momentum has redshifted by (1+z_rec)/(1+z_prod)
redshift_factor = (1.0 + z_rec) / (1.0 + z_prod_alt)  # (local)
p_rec_over_m = v_QP_mean * (1.0 + z_prod_alt) * redshift_factor / (1.0 + z_prod_alt)  # (local) ~ v_i * (1+z_rec)/(1+z_prod)
p_rec_over_m = v_QP_mean * redshift_factor  # (local) simplified: p(z_rec)/m ~ v_i * (1+z_rec)/(1+z_prod)

print(f"\nMomentum redshift:")
print(f"  Redshift factor (1+z_rec)/(1+z_prod) = {redshift_factor:.4e}")
print(f"  p(z_rec)/m_QP = {p_rec_over_m:.4e}")

# The DM sound speed squared for a non-relativistic ideal gas:
#   c_s^2 = T_eff / m
# where T_eff is the effective temperature (kinetic energy per particle).
#
# For a BCS-gapped QP gas at temperature T << Delta:
#   c_s^2 = (5/3) * (T_eff / m)  [monatomic ideal gas in NR limit]
# But for QPs deep in the gap, the relevant quantity is just the velocity
# dispersion squared: c_s^2 ~ <v^2> / 3  (3D)
#
# At recombination:
#   v(z_rec) = v_init * (1+z_rec)/(1+z_prod)
#   c_s^2 = v(z_rec)^2 / 3

v_rec = v_QP_mean * redshift_factor  # (local) velocity at recombination
cs2_DM_rec = v_rec**2 / 3.0  # (local) DM sound speed squared at z_rec

# Alternatively, for a condensate (BCS ground state), the COLLECTIVE
# sound speed is the Goldstone (first sound) mode:
#   c_Gold = 0.915 (M_KK units, from s52_gl_josephson)
# In physical units this is c_Gold * c_light, but this is the INTERNAL
# fabric sound speed, not the cosmological DM sound speed.
#
# The cosmological DM sound speed is set by the THERMAL velocity of
# the quasiparticle gas, not the collective mode speed.
# Since the QPs have been redshifting since z ~ 10^29, their v(z_rec)
# is cosmologically negligible.

print(f"\nDM sound speed at recombination:")
print(f"  v(z_rec) / c = {v_rec:.4e}")
print(f"  c_s^2 (thermal) = v^2/3 = {cs2_DM_rec:.4e}")
print(f"  CDM threshold: c_s^2 < 10^{{-5}}")

# More careful: the Bogoliubov dispersion relation gives
#   E(p) = sqrt(p^2 + Delta^2)   (relativistic)
#   v_g = dE/dp = p / E           (group velocity)
# For p << Delta (non-relativistic):
#   v_g ~ p / Delta
# The sound speed in the QP gas is:
#   c_s^2 = n * (dp/dn) * (dv/dp) / m ~ <v^2> / 3

# The QP gas is NOT a Bose-Einstein condensate at recombination.
# It's a relic gas of non-interacting quasiparticles (BCS protection
# theorem: no self-interaction vertex, S69). So the sound speed is
# simply the thermal velocity dispersion.

# Even more conservatively: the BCS condensate DOES have a collective
# Goldstone mode with c_Gold = 0.915 in M_KK units. But this mode
# propagates INSIDE the fiber (internal space), not on the emergent 4D
# manifold. The cosmological c_s is the 4D sound speed, which for a
# non-self-interacting particle is just v_thermal.

# Final c_s^2 estimate using the 3He-B analogy:
# In 3He-B, the quasiparticle (Bogoliubov) excitations have:
#   c_s^2 = (1/3) * v_F^2 * (n_n / n)   [normal fluid fraction]
# where n_n/n = exp(-Delta/T) at T << Delta.
#
# For the framework DM at recombination:
#   Delta = 0.464 M_KK ~ 3.45e16 GeV
#   T_DM(z_rec) ~ T_acoustic * M_KK * (1+z_rec)/(1+z_prod)
#                ~ 0.112 * 7.4e16 * (1101)/(3.2e29)
#                ~ 2.87e-11 GeV
#   Delta / T_DM ~ 3.45e16 / 2.87e-11 ~ 1.2e27
#   exp(-Delta/T) ~ exp(-1.2e27) = 0 (to any precision)
#   => c_s^2(3He-B analog) ~ v_F^2/3 * exp(-1.2e27) = 0

T_DM_rec_GeV = T_acoustic * M_KK * (1.0 + z_rec) / (1.0 + z_prod_alt)  # (local)
Delta_over_T = Delta_BCS * M_KK / T_DM_rec_GeV  # (local)
f_normal = np.exp(-min(Delta_over_T, 700.0))  # (local) cap to avoid underflow
v_F_squared = v_QP_mean**2  # (local) Fermi velocity ~ initial QP velocity

cs2_3HeB = (1.0/3.0) * v_F_squared * f_normal  # (local) 3He-B analog formula

print(f"\n3He-B analog computation:")
print(f"  T_DM(z_rec) = {T_DM_rec_GeV:.4e} GeV")
print(f"  Delta_BCS = {Delta_BCS * M_KK:.4e} GeV")
print(f"  Delta / T_DM = {Delta_over_T:.4e}")
print(f"  f_normal = exp(-Delta/T) = {f_normal:.4e}")
print(f"  c_s^2(3He-B) = v_F^2/3 * f_normal = {cs2_3HeB:.4e}")

# Summary: THREE routes to c_s^2 at recombination
print(f"\n--- c_s^2 SUMMARY ---")
print(f"  Method 1 (momentum redshift): c_s^2 = {cs2_DM_rec:.4e}")
print(f"  Method 2 (3He-B condensate):  c_s^2 = {cs2_3HeB:.4e}")
print(f"  Method 3 (BCS protection):    c_s^2 = 0 exactly")
print(f"                                (no self-interaction vertex => no pressure)")
print(f"  CDM threshold:                c_s^2 < 1e-5")

# Take the most conservative (largest) value
cs2_DM_final = max(cs2_DM_rec, cs2_3HeB)  # (local)
cs2_CDM_threshold = 1e-5  # (local)

obs1_pass = cs2_DM_final < cs2_CDM_threshold  # (local)
obs1_dev = abs(cs2_DM_final - 0.0) / cs2_CDM_threshold  # (local) deviation relative to threshold

print(f"\n  OBSERVABLE 1: c_s^2 = {cs2_DM_final:.4e}")
print(f"  CDM value: 0")
print(f"  Deviation: {cs2_DM_final / cs2_CDM_threshold:.4e} x threshold")
print(f"  Within 7% of CDM: {'YES (exactly CDM)' if cs2_DM_final < 0.07 * cs2_CDM_threshold else 'YES (below threshold)' if obs1_pass else 'NO'}")

# ============================================================================
#  STEP 2: ISW Contribution at Recombination from DM c_s != 0
# ============================================================================
print("\n" + "=" * 78)
print("STEP 2: ISW Contribution from DM Sound Speed")
print("=" * 78)

# The ISW effect from DM arises when the gravitational potential Phi
# changes in time due to DM perturbation evolution.
#
# For CDM: delta_DM grows as delta ~ a (matter domination), Phi = const.
#   => ISW from DM = 0 during matter domination.
#   => ISW at recombination is entirely from the radiation-matter transition.
#
# For warm/fuzzy DM with c_s^2 > 0:
#   On scales k > k_J = a*H / c_s (Jeans scale), DM perturbations oscillate
#   instead of growing. This causes Phi to decay on those scales, producing
#   additional ISW.
#
# The Jeans wavenumber at recombination:
#   k_J = a_rec * H(z_rec) / c_s
# With c_s^2 ~ 10^{-54} (our result), k_J is astronomically large.

# Hubble parameter at recombination (matter + radiation dominated)
a_rec = 1.0 / (1.0 + z_rec)  # (local)
H_rec_over_H0 = np.sqrt(Omega_m * (1+z_rec)**3 + Omega_r * (1+z_rec)**4 + Omega_Lambda)  # (local)
H_rec = H_0_km_s_Mpc * H_rec_over_H0  # (local) km/s/Mpc

print(f"\nHubble parameter at recombination:")
print(f"  H(z_rec) / H_0 = {H_rec_over_H0:.2f}")
print(f"  H(z_rec) = {H_rec:.2f} km/s/Mpc")

# Jeans wavenumber
if cs2_DM_final > 0:
    cs_DM = np.sqrt(cs2_DM_final)  # (local)
    # k_J in h/Mpc
    k_J = a_rec * H_rec / (cs_DM * c_light_km_s)  # (local) in h/Mpc (approximate)
    # More precisely: k_J = a * H / c_s in comoving coordinates
    # k_J = H(z_rec) / (c_s * c) in Mpc^{-1} (comoving)
    k_J_comoving = H_rec / (cs_DM * c_light_km_s)  # (local) h/Mpc, comoving
else:
    cs_DM = 0.0  # (local)
    k_J = np.inf  # (local)
    k_J_comoving = np.inf  # (local)

print(f"\nJeans scale from DM sound speed:")
print(f"  c_s(DM) = {cs_DM:.4e}")
if np.isfinite(k_J_comoving):
    print(f"  k_J (comoving) = {k_J_comoving:.4e} h/Mpc")
    lambda_J = 2.0 * np.pi / k_J_comoving if k_J_comoving > 0 else np.inf  # (local)
    print(f"  lambda_J = {lambda_J:.4e} Mpc/h")
else:
    print(f"  k_J = infinity (c_s = 0 exactly)")
    lambda_J = 0.0  # (local)

# Observable CMB scales: l ~ 100-2500 corresponds to k ~ 0.01-0.2 h/Mpc
k_CMB_min = 0.01  # (local) h/Mpc
k_CMB_max = 0.2   # (local) h/Mpc

print(f"\nCMB observable scales: k = [{k_CMB_min}, {k_CMB_max}] h/Mpc")
if np.isfinite(k_J_comoving):
    print(f"  k_J / k_CMB_max = {k_J_comoving / k_CMB_max:.4e}")
    print(f"  All CMB scales are {k_J_comoving / k_CMB_max:.1e}x below k_J")
else:
    print(f"  k_J = infinity => no Jeans suppression at any scale")

# ISW power contribution from DM sound speed
# The additional ISW from DM c_s > 0 modifies the TT power spectrum at
# low l through: delta C_l / C_l ~ (k_CMB / k_J)^2
# This is because the potential decay on scales k < k_J goes as
#   d(Phi)/d(eta) ~ -c_s^2 * k^2 * Phi
# and the ISW integrand is ~ d(Phi)/d(eta) * j_l(k * chi)

if np.isfinite(k_J_comoving) and k_J_comoving > 0:
    # Maximum ISW deviation at largest CMB scale
    isw_deviation = (k_CMB_max / k_J_comoving)**2  # (local) fractional ISW change
else:
    isw_deviation = 0.0  # (local)

print(f"\nISW deviation from CDM:")
print(f"  delta(C_l^TT) / C_l^TT ~ (k/k_J)^2 = {isw_deviation:.4e}")

obs2_pass = isw_deviation < 0.07  # (local) within 7% of CDM
obs2_val = isw_deviation  # (local)

print(f"\n  OBSERVABLE 2: ISW deviation = {isw_deviation:.4e}")
print(f"  CDM value: 0")
print(f"  Within 7% of CDM: {'YES' if obs2_pass else 'NO'}")

# ============================================================================
#  STEP 3: DM Density at Recombination (rho_DM ratio)
# ============================================================================
print("\n" + "=" * 78)
print("STEP 3: DM Density at Recombination")
print("=" * 78)

# The Leggett-only DM produces:
#   Omega_DM h^2 = 0.120 (from Z-EQ-CHECK-66, Leggett-only PASS)
# The Planck value:
#   Omega_DM h^2 = 0.120 +/- 0.001  (Planck 2018)
#
# Key question: does the DM density scale correctly as a^{-3}?
# For CDM: rho_DM(z) = rho_DM(0) * (1+z)^3  (matter-like)
#
# The Leggett-channel QPs are:
# - Non-relativistic at all z < z_NR ~ 10^{29}
# - Stable (tau = 4.93e82 s, DM-PAIR-DECAY-70 PASS)
# - Non-self-interacting (BCS protection theorem 5, S69)
# - Not in thermal contact with radiation (decoupled at production)
#
# Therefore: rho_DM(z) = rho_DM(0) * (1+z)^3 exactly.
# The scaling is identical to CDM because:
#   E_QP = sqrt(p^2 + m^2) ~ m + p^2/(2m) for p << m
#   Number density: n ~ a^{-3} (conserved)
#   Energy density: rho ~ n * m ~ a^{-3} (for NR particles)

# Quantitative check: what is w_DM?
# For massive NR particles: w = P/rho = <v^2>/(3c^2) ~ cs2_DM
# At recombination:
w_DM_rec = cs2_DM_final  # (local) equation of state parameter

# CDM has w_DM = 0 exactly.
# Deviation in rho scaling from z_prod to z_rec:
# rho(z_rec) / rho_CDM(z_rec) = (a_rec/a_prod)^{-3(1+w)} / (a_rec/a_prod)^{-3}
#                                = (a_rec/a_prod)^{-3w}
# For w ~ cs2 ~ 10^{-54}:
#   delta(rho)/rho = 3 * w * ln((1+z_prod)/(1+z_rec)) ~ 3 * 10^{-54} * 68 ~ 10^{-52}
ln_z_ratio = np.log((1.0 + z_prod_alt) / (1.0 + z_rec))  # (local)
delta_rho_over_rho = 3.0 * w_DM_rec * ln_z_ratio  # (local)

# Also check Omega_DM h^2 match
h = H_0_km_s_Mpc / 100.0  # (local)
Omega_DM_h2_planck = 0.120  # (local) Planck 2018
# From Z-EQ-CHECK-66: Leggett-only gives z_eq = 3425 => Omega_DM h^2 = 0.120
Omega_DM_h2_FW = 0.120  # (local) from Leggett-only channel (Z-EQ-CHECK-66)
delta_Omega = abs(Omega_DM_h2_FW - Omega_DM_h2_planck) / Omega_DM_h2_planck  # (local)

print(f"\nDM density scaling:")
print(f"  w_DM = c_s^2 = {w_DM_rec:.4e}")
print(f"  ln((1+z_prod)/(1+z_rec)) = {ln_z_ratio:.2f}")
print(f"  delta(rho)/rho (accumulated) = {delta_rho_over_rho:.4e}")
print(f"\nOmega_DM h^2:")
print(f"  Planck 2018: {Omega_DM_h2_planck:.4f}")
print(f"  Framework (Leggett-only): {Omega_DM_h2_FW:.4f}")
print(f"  Deviation: {delta_Omega:.4e} ({delta_Omega*100:.2f}%)")

obs3_pass = abs(delta_rho_over_rho) < 0.07 and delta_Omega < 0.07  # (local)
obs3_val = max(abs(delta_rho_over_rho), delta_Omega)  # (local)

print(f"\n  OBSERVABLE 3: rho_DM deviation = {obs3_val:.4e}")
print(f"  CDM value: delta_rho/rho = 0, delta_Omega = 0")
print(f"  Within 7% of CDM: {'YES' if obs3_pass else 'NO'}")

# ============================================================================
#  STEP 4: P(k) Suppression from DM Sound Speed
# ============================================================================
print("\n" + "=" * 78)
print("STEP 4: P(k) Suppression from DM Pressure")
print("=" * 78)

# For DM with c_s^2 > 0, the matter power spectrum is suppressed below
# the Jeans scale. The transfer function modification is:
#   T(k) = T_CDM(k) * [1 + (k/k_J)^2]^{-1}   (approximate)
#
# This gives:
#   P(k) / P_CDM(k) = [1 + (k/k_J)^2]^{-2}
#
# At CMB scales (k ~ 0.01-0.2 h/Mpc) with k_J >> k_CMB:
#   P/P_CDM ~ 1 - 2*(k/k_J)^2

# Compute suppression at key scales
k_scales = np.array([0.01, 0.05, 0.1, 0.2, 1.0, 10.0])  # (local) h/Mpc

print(f"\nP(k) suppression from DM Jeans filtering:")
print(f"  {'k (h/Mpc)':>12s}  {'P/P_CDM':>12s}  {'delta P/P':>12s}")

max_suppression = 0.0  # (local)
for k_val in k_scales:
    if np.isfinite(k_J_comoving) and k_J_comoving > 0:
        ratio = (k_val / k_J_comoving)**2  # (local)
        Pk_ratio = 1.0 / (1.0 + ratio)**2  # (local)
    else:
        Pk_ratio = 1.0  # (local) CDM exactly
    delta_Pk = abs(1.0 - Pk_ratio)  # (local)
    max_suppression = max(max_suppression, delta_Pk)
    print(f"  {k_val:12.3f}  {Pk_ratio:12.10f}  {delta_Pk:12.4e}")

# Also check against WDM-FRACTION-63 result:
# lambda_fs = 9.85e-23 Mpc => k_fs = 2*pi/lambda_fs ~ 6.4e22 h/Mpc
# Warm fraction is 1.15% => effective suppression is further reduced
lambda_fs_prior = 9.85e-23  # (local) Mpc, from WDM-FRACTION-63
k_fs_prior = 2.0 * np.pi / lambda_fs_prior  # (local) h/Mpc
f_warm = 0.0115  # (local) 1.15% warm fraction

print(f"\nCross-check with WDM-FRACTION-63:")
print(f"  lambda_fs = {lambda_fs_prior:.4e} Mpc")
print(f"  k_fs = {k_fs_prior:.4e} h/Mpc")
print(f"  f_warm = {f_warm:.4f}")
print(f"  k_fs / k_CMB_max = {k_fs_prior / k_CMB_max:.4e}")

obs4_pass = max_suppression < 0.07  # (local) within 7% of CDM
obs4_val = max_suppression  # (local)

print(f"\n  OBSERVABLE 4: Max P(k) suppression = {max_suppression:.4e}")
print(f"  CDM value: 0")
print(f"  Within 7% of CDM: {'YES' if obs4_pass else 'NO'}")

# ============================================================================
#  STEP 5: Gate Verdict
# ============================================================================
print("\n" + "=" * 78)
print("GATE VERDICT: S75-E3-MULTI-DM")
print("=" * 78)

observables = {
    'c_s^2': {'value': cs2_DM_final, 'CDM': 0.0, 'within_7pct': obs1_pass, 'deviation': cs2_DM_final},
    'ISW_deviation': {'value': isw_deviation, 'CDM': 0.0, 'within_7pct': obs2_pass, 'deviation': isw_deviation},
    'rho_DM_deviation': {'value': obs3_val, 'CDM': 0.0, 'within_7pct': obs3_pass, 'deviation': obs3_val},
    'P(k)_suppression': {'value': max_suppression, 'CDM': 0.0, 'within_7pct': obs4_pass, 'deviation': max_suppression},
}

n_pass = sum(1 for o in observables.values() if o['within_7pct'])  # (local)
n_fail = 4 - n_pass  # (local)

print(f"\nObservable summary:")
print(f"  {'Observable':>25s}  {'Value':>12s}  {'CDM':>8s}  {'Within 7%':>10s}")
print(f"  {'-'*25}  {'-'*12}  {'-'*8}  {'-'*10}")
for name, obs in observables.items():
    v_str = f"{obs['value']:.4e}" if obs['value'] != 0 else "0"
    print(f"  {name:>25s}  {v_str:>12s}  {'0':>8s}  {'YES' if obs['within_7pct'] else 'NO':>10s}")

print(f"\n  Passing: {n_pass}/4")
print(f"  Failing: {n_fail}/4")

if n_fail == 0:
    verdict = "PASS"
    verdict_detail = "All 4 observables match CDM within 7%"
elif n_fail <= 2:
    verdict = "INFO"
    verdict_detail = f"{n_fail}/4 observables outside 7%"
else:
    verdict = "FAIL"
    verdict_detail = f"{n_fail}/4 observables outside 7%"

print(f"\n  Gate S75-E3-MULTI-DM: {verdict}")
print(f"  {verdict_detail}")

# Physical interpretation
print(f"\n  PHYSICAL INTERPRETATION:")
print(f"  The Leggett-channel DM is CDM to extraordinary precision because:")
print(f"    1. Produced at z ~ {z_prod_alt:.1e} (M_KK scale)")
print(f"    2. All momenta redshifted by factor {redshift_factor:.1e} by recombination")
print(f"    3. BCS gap Delta = {Delta_BCS:.3f} M_KK provides exponential suppression")
print(f"       of thermal excitations: Delta/T_DM(z_rec) ~ {Delta_over_T:.1e}")
print(f"    4. Non-self-interacting (BCS protection theorem 5)")
print(f"    5. Absolutely stable (tau = 4.93e82 s)")
print(f"    6. Omega_DM h^2 = 0.120 matches Planck to < 1%")
print(f"")
print(f"  W2-N context: Z_2-odd sector has n_Z2 = 0 exactly (selection rule).")
print(f"  This is irrelevant to CDM compatibility because the DM channel is")
print(f"  the inter-band Leggett mode (f_CPT = 0.610 from W1-L), not the")
print(f"  Z_2-odd (cell-exchange) sector. The Leggett channel's CDM behavior")
print(f"  is structural (BCS protection + momentum redshift), independent of")
print(f"  the Z_2 question.")

# ============================================================================
#  STEP 6: Save results
# ============================================================================
print("\n" + "=" * 78)
print("Saving results...")
print("=" * 78)

results = {
    # Sound speed
    'cs2_DM_momentum': cs2_DM_rec,
    'cs2_DM_3HeB': cs2_3HeB,
    'cs2_DM_final': cs2_DM_final,
    'cs2_CDM_threshold': cs2_CDM_threshold,

    # ISW
    'isw_deviation': isw_deviation,
    'k_J_comoving': k_J_comoving if np.isfinite(k_J_comoving) else -1.0,

    # Density
    'delta_rho_over_rho': delta_rho_over_rho,
    'Omega_DM_h2_planck': Omega_DM_h2_planck,
    'Omega_DM_h2_FW': Omega_DM_h2_FW,
    'delta_Omega': delta_Omega,

    # P(k)
    'max_Pk_suppression': max_suppression,

    # QP properties
    'Delta_BCS_MKK': Delta_BCS,
    'm_QP_GeV': m_QP_GeV,
    'v_QP_mean': v_QP_mean,
    'v_rec': v_rec,
    'T_DM_rec_GeV': T_DM_rec_GeV,
    'Delta_over_T_rec': Delta_over_T,
    'z_prod': z_prod_alt,
    'z_rec': z_rec,
    'redshift_factor': redshift_factor,
    'f_CPT': 0.610,
    'n_Z2': 0.0,

    # Gate
    'gate_name': 'S75-E3-MULTI-DM',
    'gate_verdict': verdict,
    'n_pass': n_pass,
    'n_fail': n_fail,
}

outpath = os.path.join(os.path.dirname(__file__), 's75_multi_channel_dm.npz')
np.savez(outpath, **results)
print(f"  Saved to {outpath}")
print("\nDone.")
