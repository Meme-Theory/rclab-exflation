#!/usr/bin/env python3
"""
S58 W3-15: Free-Streaming Bound from Paper 16

Gate: FREE-STREAMING-58
  PASS: z_tr > 6.2 x 10^7
  FAIL: z_tr < 6.2 x 10^7

Physics:
  - DM candidate = B2 sector quasiparticle (BCS excitation in (1,1) rep of SU(3))
  - Produced at the fold (tau_fold = 0.19) with v_prod = c_Gold = 0.915c
  - Post-transit, tau stabilizes => mass fixed (Paper 16 eq 7.1: dm^2/ds = 0 when d_A g_K = 0)
  - Momentum redshifts as p ~ (1+z) => velocity drops
  - Non-relativistic transition: v(z_tr) = c/3

Key subtlety: The tau-to-z mapping is not directly fixed by the framework's internal
scale factor a(tau). We must use the ENERGY SCALE M_KK to infer T_prod, then
standard cosmological T-z relation to get z_prod.

References:
  - Paper 16 (Baptista 2024, arXiv:2406.09503): mass variation formula eq 7.1
  - s58_mass_variation.npz: B2 eigenvalues vs tau
  - s54_scale_factor.npz: a(tau), H(tau)
  - canonical_constants.py: M_KK, c_Gold, T_CMB, etc.
"""

import sys
import os
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    M_KK, M_KK_gravity, M_KK_kerner, OOM_diff_MKK,
    tau_fold, c_Gold, T_CMB, T_CMB_GeV,
    E_B2_mean, Delta_0_GL, Delta_B3,
    z_BBN, T_BBN_GeV,
    Omega_DM, Omega_m,
)

# ============================================================================
#  STEP 0: Load input data
# ============================================================================

script_dir = os.path.dirname(os.path.abspath(__file__))
mv_data = np.load(os.path.join(script_dir, 's58_mass_variation.npz'), allow_pickle=True)
sf_data = np.load(os.path.join(script_dir, 's54_scale_factor.npz'), allow_pickle=True)

tau_mv = mv_data['tau_values']       # (50,) tau grid
eigs = mv_data['eigenvalues']         # (50, 32) eigenvalues of D_K^2
labels = mv_data['cell_labels']       # (32, 2) = (p,q) labels
fold_idx = int(mv_data['fold_idx'])   # index of tau_fold in tau_mv

# Scale factor data
tau_sf = sf_data['tau']
a_sf = sf_data['a']
H_sf = sf_data['H']
A_exp = float(sf_data['A_exp'])
B_exp = float(sf_data['B_exp'])

print("=" * 72)
print("  S58 W3-15: Free-Streaming Bound from Paper 16")
print("  Gate: FREE-STREAMING-58")
print("=" * 72)

# ============================================================================
#  STEP 1: Extract B2 mass at the fold
# ============================================================================
# B2 = (1,1) representation of SU(3)

b2_mask = (labels[:, 0] == 1) & (labels[:, 1] == 1)
b2_idx = np.where(b2_mask)[0]
assert len(b2_idx) == 1, f"Expected exactly one B2 cell, found {len(b2_idx)}"
b2_idx = b2_idx[0]

# Eigenvalue of D_K^2 for B2 at the fold
lambda_B2_fold = eigs[fold_idx, b2_idx]
m_B2_fold_MKK = np.sqrt(lambda_B2_fold)  # mass in M_KK units

# B2 mass across the full tau range
lambda_B2_all = eigs[:, b2_idx]
m_B2_all = np.sqrt(lambda_B2_all)

# B2 mass at tau=0 and tau=0.5
m_B2_0 = np.sqrt(eigs[0, b2_idx])
m_B2_end = np.sqrt(eigs[-1, b2_idx])

print(f"\n--- Step 1: B2 Mass at Fold ---")
print(f"B2 cell index: {b2_idx} (rep (1,1), dim={int(mv_data['cell_dims'][b2_idx])})")
print(f"lambda_B2(tau=0)    = {eigs[0, b2_idx]:.6f}")
print(f"lambda_B2(tau_fold) = {lambda_B2_fold:.6f}")
print(f"lambda_B2(tau=0.5)  = {eigs[-1, b2_idx]:.6f}")
print(f"m_B2(tau=0)    = {m_B2_0:.6f} M_KK = {m_B2_0 * M_KK:.4e} GeV")
print(f"m_B2(tau_fold) = {m_B2_fold_MKK:.6f} M_KK = {m_B2_fold_MKK * M_KK:.4e} GeV")
print(f"m_B2(tau=0.5)  = {m_B2_end:.6f} M_KK = {m_B2_end * M_KK:.4e} GeV")
print(f"Mass change (0 -> fold): {(m_B2_fold_MKK - m_B2_0)/m_B2_0 * 100:.1f}%")
print(f"Mass change (0 -> 0.5):  {(m_B2_end - m_B2_0)/m_B2_0 * 100:.1f}%")

# ============================================================================
#  STEP 2: Production velocity and Lorentz factor
# ============================================================================
# v_prod = c_Gold = 0.915c (Goldstone mode group velocity from GL-Josephson spectrum)
# This is the phononic DM velocity at the fold: quasiparticles propagate
# at the sound speed of the condensate's Goldstone mode.

v_prod = c_Gold  # in units of c (natural units)
gamma_prod = 1.0 / np.sqrt(1.0 - v_prod**2)
p_prod_over_m = gamma_prod * v_prod  # p_prod / m_B2

print(f"\n--- Step 2: Production Kinematics ---")
print(f"v_prod = c_Gold = {v_prod:.4f} c")
print(f"gamma_prod = {gamma_prod:.4f}")
print(f"p_prod / m = gamma * v = {p_prod_over_m:.4f}")
print(f"  => DM is RELATIVISTIC at production (v/c = {v_prod:.3f})")

# ============================================================================
#  STEP 3: Tau-to-Redshift Mapping
# ============================================================================
# The framework's internal a(tau) is NOT the cosmological scale factor.
# a(tau) describes the RELATIVE expansion during the transit (a(0)=1).
#
# To get the PHYSICAL redshift z_prod, we use the energy scale:
#   T_prod ~ M_KK  (the transit occurs at the KK compactification scale)
#   1 + z_prod = T_prod / T_CMB * (g_{*S,0} / g_{*S}(T_prod))^{1/3}
#
# Standard cosmology: T(z) = T_CMB * (1+z) * (g_{*S,0}/g_{*S})^{1/3}
# with g_{*S,0} = 3.938 (photons + neutrinos today),
#      g_{*S}(T > mt) = 106.75 (full SM).
#
# NOTE: At M_KK ~ 7.4e16 GeV, we are ABOVE the SM energy range.
# The framework predicts NO new d.o.f. between M_KK and the SM
# (the internal spectrum IS the SM). So g_{*S} = 106.75 is the
# appropriate value. If BSM physics exists (e.g., SUSY), g_{*S}
# could be higher, which would INCREASE z_prod and make the gate
# easier to pass. We use g_{*S} = 106.75 as the CONSERVATIVE choice.

g_star_S_today = 3.938      # photons (2) + 3 nu species at T_nu < T_gamma  # (local)
g_star_S_SM = 106.75        # full SM above top mass  # (local)
g_star_S_ratio = (g_star_S_today / g_star_S_SM)**(1.0/3.0)

# Production temperature = M_KK (the transit energy scale)
# Conservative: M_KK_gravity = 7.43e16 GeV
# Aggressive: M_KK_kerner = 5.04e17 GeV
T_prod_grav = M_KK_gravity  # GeV
T_prod_kern = M_KK_kerner   # GeV

z_prod_grav = (T_prod_grav / T_CMB_GeV) * g_star_S_ratio - 1.0
z_prod_kern = (T_prod_kern / T_CMB_GeV) * g_star_S_ratio - 1.0

print(f"\n--- Step 3: Tau-to-Redshift Mapping ---")
print(f"T_CMB = {T_CMB_GeV:.4e} GeV")
print(f"g_{{*S,0}} = {g_star_S_today}")
print(f"g_{{*S}}(SM) = {g_star_S_SM}")
print(f"(g_{{*S,0}}/g_{{*S}})^{{1/3}} = {g_star_S_ratio:.6f}")
print(f"")
print(f"CONSERVATIVE (gravity route, M_KK = {M_KK_gravity:.3e} GeV):")
print(f"  T_prod = {T_prod_grav:.3e} GeV")
print(f"  z_prod = {z_prod_grav:.4e}")
print(f"")
print(f"AGGRESSIVE (Kerner route, M_KK = {M_KK_kerner:.3e} GeV):")
print(f"  T_prod = {T_prod_kern:.3e} GeV")
print(f"  z_prod = {z_prod_kern:.4e}")

# ============================================================================
#  STEP 4: Non-Relativistic Transition Redshift
# ============================================================================
# Post-transit, tau stabilizes => g_K is covariantly constant =>
# dm^2/ds = 0 by Paper 16 eq 7.1. Mass is FROZEN at m_B2(fold).
#
# Momentum redshifts as p(z) = p_prod * (1+z_prod)/(1+z) for matter.
#
# Velocity:
#   v(z) = p(z) / E(z) = p(z) / sqrt(p(z)^2 + m^2)
#
# Transition criterion: v(z_tr) = c/3
#   p_tr / sqrt(p_tr^2 + m^2) = 1/3
#   => 9 p_tr^2 = p_tr^2 + m^2
#   => p_tr = m / (2*sqrt(2))
#
# So: p_prod * (1+z_prod)/(1+z_tr) = m / (2*sqrt(2))
#     (1+z_tr) = p_prod/m * 2*sqrt(2) * (1+z_prod)
#              = gamma_prod * v_prod * 2*sqrt(2) * (1+z_prod)

p_tr_over_m = 1.0 / (2.0 * np.sqrt(2.0))  # = 0.3536
kinematic_factor = p_prod_over_m / p_tr_over_m  # = gamma*v * 2*sqrt(2)
# Equivalently: kinematic_factor = gamma*v * 2*sqrt(2)

z_tr_grav = kinematic_factor * (1.0 + z_prod_grav) - 1.0
z_tr_kern = kinematic_factor * (1.0 + z_prod_kern) - 1.0

print(f"\n--- Step 4: Non-Relativistic Transition ---")
print(f"Transition criterion: v(z_tr) = c/3")
print(f"  => p_tr / m = 1/(2*sqrt(2)) = {p_tr_over_m:.6f}")
print(f"  p_prod / m = gamma * v = {p_prod_over_m:.6f}")
print(f"  kinematic factor = (p_prod/m) / (p_tr/m) = {kinematic_factor:.4f}")
print(f"  => (1+z_tr) = {kinematic_factor:.4f} * (1+z_prod)")
print(f"")
print(f"CONSERVATIVE:")
print(f"  z_tr = {z_tr_grav:.4e}")
print(f"  log10(z_tr) = {np.log10(z_tr_grav):.2f}")
print(f"")
print(f"AGGRESSIVE:")
print(f"  z_tr = {z_tr_kern:.4e}")
print(f"  log10(z_tr) = {np.log10(z_tr_kern):.2f}")

# ============================================================================
#  STEP 5: Gate Evaluation
# ============================================================================
z_tr_threshold = 6.2e7  # (local)

gate_pass_grav = z_tr_grav > z_tr_threshold
gate_pass_kern = z_tr_kern > z_tr_threshold

# How many orders of magnitude of margin?
margin_grav = np.log10(z_tr_grav / z_tr_threshold)
margin_kern = np.log10(z_tr_kern / z_tr_threshold)

print(f"\n--- Step 5: Gate Evaluation ---")
print(f"Threshold: z_tr > {z_tr_threshold:.1e}")
print(f"")
print(f"CONSERVATIVE (M_KK = {M_KK_gravity:.3e} GeV):")
print(f"  z_tr = {z_tr_grav:.4e}")
print(f"  z_tr / z_threshold = {z_tr_grav/z_tr_threshold:.4e}")
print(f"  Margin: {margin_grav:.1f} orders of magnitude")
print(f"  Gate: {'PASS' if gate_pass_grav else 'FAIL'}")
print(f"")
print(f"AGGRESSIVE (M_KK = {M_KK_kerner:.3e} GeV):")
print(f"  z_tr = {z_tr_kern:.4e}")
print(f"  z_tr / z_threshold = {z_tr_kern/z_tr_threshold:.4e}")
print(f"  Margin: {margin_kern:.1f} orders of magnitude")
print(f"  Gate: {'PASS' if gate_pass_kern else 'FAIL'}")

# Overall verdict
overall_pass = gate_pass_grav  # conservative is binding
print(f"\n  OVERALL VERDICT: {'PASS' if overall_pass else 'FAIL'}")

# ============================================================================
#  STEP 6: Critical Analysis — What Could Invalidate This?
# ============================================================================
# The gate passes by ~22 orders of magnitude. This seems robust, but
# let's identify what assumptions go into this and where they could break.

# Minimum z_prod for gate to pass:
# z_tr > 6.2e7 requires (1+z_prod) > 6.2e7 / kinematic_factor
z_prod_min = z_tr_threshold / kinematic_factor
# And the corresponding T_prod_min:
T_prod_min_GeV = z_prod_min * T_CMB_GeV / g_star_S_ratio

print(f"\n--- Step 6: Critical Analysis ---")
print(f"Minimum z_prod for gate PASS: {z_prod_min:.4e}")
print(f"Corresponding T_prod_min: {T_prod_min_GeV:.4e} GeV = {T_prod_min_GeV*1e3:.4e} MeV")
print(f"")
print(f"For comparison:")
print(f"  T_BBN = {T_BBN_GeV:.0e} GeV (z_BBN ~ {z_BBN:.0e})")
print(f"  T_EW  ~ 100 GeV (z_EW ~ 10^15)")
print(f"  T_QCD ~ 0.2 GeV (z_QCD ~ 10^12)")
print(f"  T_prod(framework) = {M_KK:.3e} GeV (z_prod ~ {z_prod_grav:.1e})")
print(f"")
print(f"The gate passes EVEN IF the transit occurs as late as T ~ {T_prod_min_GeV:.0e} GeV.")
if T_prod_min_GeV > T_BBN_GeV:
    print(f"This is {T_prod_min_GeV/T_BBN_GeV:.0f}x above BBN.")
else:
    print(f"This is {T_BBN_GeV/T_prod_min_GeV:.0f}x BELOW BBN — gate passes for ANY pre-BBN transit.")
print(f"The transit would need to occur BELOW {T_prod_min_GeV:.0e} GeV to fail.")
print(f"Since the framework's M_KK is {M_KK:.0e} GeV, the margin is")
print(f"{M_KK/T_prod_min_GeV:.1e}x above the minimum.")

# What if v_prod is different?
# v_prod = c_Gold = 0.915c is for the Goldstone mode. If DM has a
# different production velocity (e.g., Leggett modes with omega_L1 = 0.138 M_KK):
# v_Leggett = group velocity of massive mode ~ sqrt(1 - (m_L/E)^2)
# For a massive mode at threshold, v ~ 0 and it's already non-relativistic.
# For c_Gold < v_prod < c, the kinematic factor changes modestly.

v_test = np.array([0.5, 0.7, 0.9, 0.915, 0.95, 0.99, 0.999])
gamma_test = 1.0 / np.sqrt(1.0 - v_test**2)
p_over_m_test = gamma_test * v_test
kf_test = p_over_m_test / p_tr_over_m

print(f"\n--- Sensitivity to v_prod ---")
print(f"{'v_prod/c':>10s} {'gamma':>8s} {'p/m':>10s} {'kin_factor':>12s} {'z_tr (grav)':>14s}")
for i, v in enumerate(v_test):
    z_tr_i = kf_test[i] * (1.0 + z_prod_grav) - 1.0
    print(f"{v:10.3f} {gamma_test[i]:8.3f} {p_over_m_test[i]:10.4f} {kf_test[i]:12.4f} {z_tr_i:14.4e}")

# ============================================================================
#  STEP 7: Post-Transit Mass Stability (Paper 16 Connection)
# ============================================================================
# Paper 16 eq 7.1: c^2 d(m^2)/ds = -(d_A g_K)(p_V, p_V)
# Mass is conserved IFF g_K is covariantly constant along the worldline.
# Post-transit: tau stabilizes (the modulus field reaches its minimum),
# so d_A g_K vanishes in the 4D sense (no spacetime variation of g_K).
#
# During the transit: mass DOES change (W3-10 found 55.6% variation over [0, 0.5]).
# But the transit completes in dt ~ 1.13e-3 M_KK^{-1} (canonical_constants),
# which is dt_phys ~ 1.13e-3 / M_KK ~ 1.5e-20 / (7.4e16 GeV) ~ 2e-37 GeV^{-1}
# ~ 1.3e-62 s. This is ~ 10^{-19} Planck times.
#
# The mass variation is a TRANSIT EFFECT, confined to the transit timescale.
# After transit, dm/ds = 0 and the free-streaming analysis applies.

# Verify mass is FIXED post-transit
# The eigenvalue at the fold gives the asymptotic mass (tau stabilizes at fold)
# Actually, the mass eigenvalue at the fold is the PRODUCTION mass
# The mass at tau > tau_fold may continue to evolve, but this is during transit
# Post-transit, the internal metric reaches its equilibrium and mass is fixed

# Check how much mass changes AFTER the fold
m_B2_fold = m_B2_all[fold_idx]
m_B2_post_fold = m_B2_all[fold_idx:]
delta_m_post = np.abs(m_B2_post_fold - m_B2_fold) / m_B2_fold

print(f"\n--- Step 7: Post-Transit Mass Stability ---")
print(f"Paper 16 eq 7.1: dm^2/ds = -(d_A g_K)(p_V, p_V)")
print(f"Mass conserved when d_A g_K = 0 (g_K covariantly constant)")
print(f"")
print(f"B2 mass at fold: {m_B2_fold:.6f} M_KK")
print(f"B2 mass continues to evolve during transit (tau > tau_fold):")
for i in range(0, len(m_B2_post_fold), 3):
    ti = fold_idx + i
    if ti < len(tau_mv):
        print(f"  tau={tau_mv[ti]:.4f}: m_B2={m_B2_all[ti]:.6f} M_KK "
              f"(delta_m/m = {delta_m_post[i]*100:.1f}%)")
print(f"")
print(f"The mass variation is a TRANSIT effect (Paper 16, Section 7).")
print(f"Post-transit, g_K stabilizes => dm/ds = 0 by eq 7.1.")
print(f"The DM mass is FROZEN at the post-transit value.")
print(f"")
print(f"KEY POINT: The exact value of the frozen mass does NOT affect z_tr.")
print(f"The kinematic factor depends on v_prod/c = {v_prod:.3f}, not on m.")
print(f"A heavier DM particle with the same v_prod has proportionally higher p_prod,")
print(f"and both p and m redshift identically, so z_tr is mass-INDEPENDENT.")

# ============================================================================
#  STEP 8: Comparison with Standard WDM Bounds
# ============================================================================
# Standard WDM: thermal relic with mass m_WDM.
# Free-streaming scale lambda_fs ~ 0.1 Mpc * (m_WDM / keV)^{-1} * (T_WDM/T_nu)
# Lyman-alpha bound: m_WDM > 5.3 keV (Irsic+ 2017)
# This corresponds to z_tr ~ 10^7 for thermal relics.
#
# Our DM is NOT a thermal relic — it's produced by Kibble-Zurek quench
# at the GUT scale with v = 0.915c. The non-thermal production at
# ultra-high z means it becomes non-relativistic MUCH earlier than
# a thermal relic of any mass.

# Effective WDM mass equivalent (for comparison):
# A thermal relic becomes NR at z_tr ~ (m_WDM / 3*T_nu(z=0))
# T_nu(z=0) = (4/11)^{1/3} * T_CMB = 1.95 K = 1.68e-4 eV
T_nu_today_eV = (4.0/11.0)**(1.0/3.0) * T_CMB * 8.617e-5  # eV
# z_tr ~ m_WDM / (3 * T_nu) for thermal relic
# => m_WDM_equiv = 3 * T_nu * z_tr
m_WDM_equiv_grav_eV = 3.0 * T_nu_today_eV * z_tr_grav
m_WDM_equiv_grav_GeV = m_WDM_equiv_grav_eV * 1e-9
m_WDM_equiv_grav_keV = m_WDM_equiv_grav_eV * 1e-3

print(f"\n--- Step 8: WDM Comparison ---")
print(f"T_nu(today) = {T_nu_today_eV:.4e} eV")
print(f"Effective WDM mass equivalent (thermal relic with same z_tr):")
print(f"  m_WDM_equiv = 3 * T_nu * z_tr = {m_WDM_equiv_grav_keV:.4e} keV")
print(f"  = {m_WDM_equiv_grav_GeV:.4e} GeV")
print(f"  Lyman-alpha bound: m_WDM > 5.3 keV")
print(f"  Ratio: m_WDM_equiv / 5.3 keV = {m_WDM_equiv_grav_keV/5.3:.4e}")
print(f"")
print(f"The phononic DM behaves like an ABSURDLY heavy thermal relic")
print(f"from the free-streaming perspective. This is because it is")
print(f"produced at the GUT scale, not at the keV scale.")

# ============================================================================
#  STEP 9: Parametric z_tr as Function of Mapping Parameter
# ============================================================================
# If the tau-to-z mapping is uncertain, express z_tr = f(z_prod).
# z_tr = kinematic_factor * (1 + z_prod) - 1
# The constraint z_tr > 6.2e7 becomes:
# z_prod > (6.2e7 + 1) / kinematic_factor - 1 ~ 6.2e7 / kinematic_factor

# Parametric scan
z_prod_scan = np.logspace(6, 30, 100)
z_tr_scan = kinematic_factor * (1.0 + z_prod_scan) - 1.0

# Find where z_tr crosses threshold
z_prod_critical = (z_tr_threshold + 1.0) / kinematic_factor - 1.0

print(f"\n--- Step 9: Parametric Dependence ---")
print(f"z_tr = {kinematic_factor:.4f} * (1 + z_prod) - 1")
print(f"")
print(f"Critical z_prod for gate threshold: {z_prod_critical:.4e}")
print(f"")
print(f"{'z_prod':>12s} {'z_tr':>14s} {'z_tr/threshold':>16s} {'Verdict':>8s}")
for zp in [1e6, 1e7, z_prod_critical, 1e8, 1e10, 1e15, 1e20, 1e25, z_prod_grav]:
    zt = kinematic_factor * (1.0 + zp) - 1.0
    verdict = "PASS" if zt > z_tr_threshold else "FAIL"
    print(f"{zp:12.2e} {zt:14.4e} {zt/z_tr_threshold:16.4e} {verdict:>8s}")

# ============================================================================
#  STEP 10: Summary and Gate Verdict
# ============================================================================

gate_name = "FREE-STREAMING-58"
if overall_pass:
    gate_verdict = f"PASS: z_tr = {z_tr_grav:.2e} >> {z_tr_threshold:.1e} ({margin_grav:.0f} OOM margin)"
else:
    gate_verdict = f"FAIL: z_tr = {z_tr_grav:.2e} < {z_tr_threshold:.1e}"

gate_detail = (
    f"v_prod={v_prod:.3f}c (Goldstone), "
    f"m_B2(fold)={m_B2_fold_MKK:.4f} M_KK, "
    f"z_prod={z_prod_grav:.2e} (M_KK={M_KK_gravity:.2e} GeV), "
    f"z_tr={z_tr_grav:.2e}, "
    f"threshold={z_tr_threshold:.1e}, "
    f"margin={margin_grav:.0f} OOM. "
    f"Gate passes for ANY z_prod > {z_prod_critical:.1e} "
    f"(T_prod > {T_prod_min_GeV:.0e} GeV). "
    f"Paper 16 eq 7.1: dm/ds=0 post-transit (g_K stabilizes)."
)

print(f"\n{'='*72}")
print(f"  GATE VERDICT: {gate_name}")
print(f"  {gate_verdict}")
print(f"{'='*72}")
print(f"  {gate_detail}")

# ============================================================================
#  SAVE
# ============================================================================

outpath = os.path.join(script_dir, 's58_free_streaming.npz')
np.savez(outpath,
    # Production parameters
    v_prod=v_prod,
    gamma_prod=gamma_prod,
    p_prod_over_m=p_prod_over_m,
    m_B2_fold_MKK=m_B2_fold_MKK,
    m_B2_fold_GeV=m_B2_fold_MKK * M_KK,

    # Redshift mapping
    g_star_S_today=g_star_S_today,
    g_star_S_SM=g_star_S_SM,
    z_prod_grav=z_prod_grav,
    z_prod_kern=z_prod_kern,
    T_prod_grav_GeV=T_prod_grav,
    T_prod_kern_GeV=T_prod_kern,

    # Transition
    p_tr_over_m=p_tr_over_m,
    kinematic_factor=kinematic_factor,
    z_tr_grav=z_tr_grav,
    z_tr_kern=z_tr_kern,
    z_tr_threshold=z_tr_threshold,
    margin_grav_OOM=margin_grav,
    margin_kern_OOM=margin_kern,

    # Critical analysis
    z_prod_critical=z_prod_critical,
    T_prod_min_GeV=T_prod_min_GeV,

    # Parametric scan
    z_prod_scan=z_prod_scan,
    z_tr_scan=z_tr_scan,

    # B2 mass profile
    tau_values=tau_mv,
    m_B2_all=m_B2_all,

    # WDM equivalent
    m_WDM_equiv_keV=m_WDM_equiv_grav_keV,

    # Gate
    gate_name=np.array([gate_name]),
    gate_verdict=np.array([gate_verdict]),
    gate_detail=np.array([gate_detail]),
)

print(f"\nSaved: {outpath}")
print("Done.")
