#!/usr/bin/env python3
"""
s65_ep_test.py — EP Test Through Transit: delta G_N / G_N  (EP-65)
===================================================================

Einstein-Theorist computation, Session 65 Wave 8.

Physics:
  G_N = 1/(16*pi*a_2) in spectral action units (Chamseddine-Connes).
  a_2(tau) = (4*pi)^{-4} * (20/3) * R(tau) * Vol(tau)
  where Vol(tau) = Vol_SU3 * exp(-5*tau) and R(tau) from Milnor formula.

  If a_2 changes during transit, G_N changes. Post-transit must settle to
  |dG/dt / G| < 10^{-13} yr^{-1} (lunar laser ranging bound).

  Key chain:
    dG/dt / G = -(1/a_2) * (da_2/dtau) * (dtau/dt)

  Post-transit modulus dynamics:
    tau(t) = tau_final + A * exp(-Gamma*t) * cos(omega_att * t)
    where Gamma ~ (3/2)*H_phys (Hubble friction), omega_att = 1.430 M_KK.

  The enormous hierarchy M_KK ~ 10^{16} GeV -> 1/M_KK ~ 10^{-41} s
  means that even large dtau/dt in M_KK units translates to fantastically
  rapid settling in human units.

Gate: EP-65
  PASS: |dG/dt / G| < 10^{-13} yr^{-1} post-transit.
  FAIL: |dG/dt / G| > 10^{-13} yr^{-1} at late times.
  INFO: Large during transit but settles afterward (expected).

Reads: computations/session-61/s61_heat_kernel_a2.npz (R(tau), a_2(tau))
       computations/session-64/s64_epsilon_profile.npz (S(tau), H(tau))
Writes: computations/session-65/s65_ep_test.npz
        computations/session-65/s65_ep_test.png
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    PI, Vol_SU3_Haar, tau_fold, M_KK, M_KK_gravity, M_KK_kerner,
    a0_fold, a2_fold,
    v_terminal, dt_transit,
    omega_att, H_fold,
    hbar_GeV_s, GeV_to_inv_s,
    t_universe_s,
)
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

print("=" * 72)
print("  EP-65: Equivalence Principle Test Through Transit")
print("  G_N = 1/(16*pi*a_2) — does a_2(tau) settling violate EP bounds?")
print("=" * 72)

# ============================================================================
#  Step 1: Load a_2(tau) from s61_heat_kernel_a2.npz
# ============================================================================

hk_data = np.load(os.path.join(SCRIPT_DIR, 's61_heat_kernel_a2.npz'),
                  allow_pickle=True)

tau_arr = hk_data['tau_arr']       # 100 points, [0, 0.5]
R_arr   = hk_data['R_arr']        # Scalar curvature R(tau)
N_tau   = int(hk_data['N_tau'])
idx_fold_hk = int(hk_data['idx_fold'])

# Also load epsilon profile for consistency checks
eps_data = np.load(os.path.join(SCRIPT_DIR, 's64_epsilon_profile.npz'),
                   allow_pickle=True)

print(f"\nLoaded {N_tau} tau points from s61_heat_kernel_a2.npz")
print(f"tau range: [{tau_arr[0]:.4f}, {tau_arr[-1]:.4f}]")
print(f"Fold index: {idx_fold_hk}, tau_fold = {tau_arr[idx_fold_hk]:.4f}")

# ============================================================================
#  Step 2: Compute a_2(tau) and G_N(tau) = 1/(16*pi*a_2)
# ============================================================================

# Vol(tau) = Vol_SU3 * exp(-5*tau) [Jensen deformation compresses 5 directions]
Vol_tau = Vol_SU3_Haar * np.exp(-5.0 * tau_arr)

# Seeley-DeWitt prefactor for a_2 on SU(3)
prefactor_a2 = (4.0 * PI)**(-4) * (20.0 / 3.0)

# a_2(tau) = prefactor * R(tau) * Vol(tau)
a2_tau = prefactor_a2 * R_arr * Vol_tau

# Verification at fold
print(f"\n--- a_2(tau) computation ---")
print(f"a_2(0)           = {a2_tau[0]:.8f}")
print(f"a_2(fold)        = {a2_tau[idx_fold_hk]:.8f}")
print(f"a_2_fold (canon) = {a2_fold:.8f}")
print(f"NOTE: a2_fold from canonical_constants = {a2_fold} is the SPECTRAL value")
print(f"      (155,984 eigenvalues). a2_SD here = {a2_tau[idx_fold_hk]:.4f}")
print(f"      (Seeley-DeWitt asymptotic). Ratio = {a2_fold / a2_tau[idx_fold_hk]:.2f}")

# G_N(tau) = 1 / (16 * pi * a_2(tau))  [in M_KK^{-2} units]
# More precisely: G_N = pi / (2 * f_2 * a_2 * M_KK^2) from spectral action
# With f_2 = 1 (sharp cutoff): G_N = pi / (2 * a_2 * M_KK^2)
# The exact normalization cancels in the RATIO dG/G.

G_N_tau = 1.0 / (16.0 * PI * a2_tau)  # proportional to G_N(tau), normalization irrelevant for dG/G

# Fractional variation: delta G_N / G_N = -delta a_2 / a_2
delta_a2_over_a2 = (a2_tau - a2_tau[idx_fold_hk]) / a2_tau[idx_fold_hk]
delta_GN_over_GN = -delta_a2_over_a2  # since G_N ~ 1/a_2

print(f"\n--- Fractional G_N variation (static, relative to fold) ---")
for i in range(0, N_tau, 10):
    print(f"  tau={tau_arr[i]:.3f}:  delta_a2/a2 = {delta_a2_over_a2[i]:+.6f},"
          f"  delta_GN/GN = {delta_GN_over_GN[i]:+.6f}")

# ============================================================================
#  Step 3: Compute da_2/dtau and (1/a_2) * da_2/dtau at post-transit points
# ============================================================================

dtau = tau_arr[1] - tau_arr[0]

# Analytical da_2/dtau via product rule:
# da_2/dtau = prefactor * Vol(tau) * [dR/dtau - 5*R(tau)]
dR_dtau = np.gradient(R_arr, dtau)
da2_dtau = prefactor_a2 * Vol_tau * (dR_dtau - 5.0 * R_arr)

# Logarithmic derivative: d(ln a_2)/dtau
dlna2_dtau = da2_dtau / a2_tau

print(f"\n--- Logarithmic derivative d(ln a_2)/dtau ---")
print(f"d(ln a_2)/dtau at tau=0:    {dlna2_dtau[0]:+.6f}")
print(f"d(ln a_2)/dtau at fold:     {dlna2_dtau[idx_fold_hk]:+.6f}")
print(f"d(ln a_2)/dtau at tau=0.25: {dlna2_dtau[50]:+.6f}")
print(f"d(ln a_2)/dtau at tau=0.50: {dlna2_dtau[-1]:+.6f}")
print(f"Range: [{dlna2_dtau.min():+.6f}, {dlna2_dtau.max():+.6f}]")

# ============================================================================
#  Step 4: Post-transit modulus dynamics
# ============================================================================
#
# After the transit through the fold, the modulus tau settles via:
#   tau(t) = tau_final + A * exp(-Gamma*t) * cos(omega_att * t)
#
# Damping: Gamma = (3/2) * H_phys (Hubble friction on modulus in FRW)
# H_phys = sqrt(2/(3*pi^2) * a_0/a_2) * M_KK  [Friedmann from spectral action]

H_phys_MKK = np.sqrt(2.0 / (3.0 * PI**2) * a0_fold / a2_fold)
print(f"\n--- Post-transit dynamics ---")
print(f"H_phys = {H_phys_MKK:.6f} M_KK = {H_phys_MKK * M_KK:.4e} GeV")

# Physical Hubble damping rate
Gamma_Hubble = 1.5 * H_phys_MKK  # 3H/2 (Klein-Gordon in FRW with V'' << H^2)
print(f"Gamma_Hubble = (3/2)*H_phys = {Gamma_Hubble:.6f} M_KK")
print(f"omega_att = {omega_att:.6f} M_KK")
print(f"Quality factor Q = omega_att / (2*Gamma) = {omega_att / (2*Gamma_Hubble):.3f}")

# Underdamped oscillation: omega_att >> Gamma_Hubble, so modulus oscillates
# and damps exponentially.
Q_factor = omega_att / (2.0 * Gamma_Hubble)
is_underdamped = Q_factor > 0.5
print(f"Underdamped: {is_underdamped} (Q = {Q_factor:.3f})")

# Initial amplitude: transit overshoots by ~ v_terminal * dt_transit
# (order of magnitude, actual depends on potential shape)
A_initial = v_terminal * dt_transit  # dimensionless (tau units)
print(f"A_initial (estimate) = v_terminal * dt_transit = {A_initial:.6e}")

# ============================================================================
#  Step 5: Convert dG/dt/G to yr^{-1}
# ============================================================================
#
# dG/dt / G = -(d ln a_2 / dtau) * (dtau/dt)
#
# dtau/dt = -A * exp(-Gamma*t) * [Gamma*cos(omega*t) + omega*sin(omega*t)]
# Peak value: |dtau/dt|_max ~ A * sqrt(Gamma^2 + omega^2) * exp(-Gamma*t)
#           ~ A * omega * exp(-Gamma*t)  [since omega >> Gamma]
#
# All quantities in M_KK natural units (time in M_KK^{-1}).
# Convert M_KK^{-1} to seconds: t_MKK = hbar / M_KK

t_MKK_seconds = hbar_GeV_s / M_KK  # hbar / M_KK in seconds
seconds_per_year = 3.1557e7  # (local)

print(f"\n--- Unit conversions ---")
print(f"M_KK = {M_KK:.4e} GeV")
print(f"t_MKK = hbar/M_KK = {t_MKK_seconds:.4e} s")
print(f"1 yr = {seconds_per_year:.4e} s")
print(f"1 yr in M_KK units = {seconds_per_year / t_MKK_seconds:.4e}")

yr_in_MKK = seconds_per_year / t_MKK_seconds

# Now compute dG/dt/G at various post-transit times
# 10 tau values post-transit (tau > 0.190), but here "tau" means tau_modulus values
# after the fold. The actual time evolution is:
#   tau(t) = tau_fold + ... (damped oscillation)
# The "10 tau values post-transit" means 10 time points after transit completion.

# Define time grid: from t=0 (transit end) to t = 10/Gamma (several damping times)
t_damp = 1.0 / Gamma_Hubble  # damping time in M_KK^{-1}
t_grid_MKK = np.array([
    0.1 * t_damp,    # ~ 0.1 damping times
    0.5 * t_damp,    # ~ 0.5 damping times
    1.0 * t_damp,    # ~ 1 damping time
    2.0 * t_damp,    # ~ 2 damping times
    5.0 * t_damp,    # ~ 5 damping times
    10.0 * t_damp,   # ~ 10 damping times
    20.0 * t_damp,   # ~ 20 damping times
    50.0 * t_damp,   # ~ 50 damping times
    100.0 * t_damp,  # ~ 100 damping times
    1000.0 * t_damp, # ~ 1000 damping times
])

t_grid_seconds = t_grid_MKK * t_MKK_seconds
t_grid_years = t_grid_seconds / seconds_per_year

print(f"\nt_damp = 1/Gamma = {t_damp:.4f} M_KK^{{-1}} = {t_damp * t_MKK_seconds:.4e} s")
print(f"                 = {t_damp * t_MKK_seconds / seconds_per_year:.4e} yr")

# Post-transit envelope of |dtau/dt|:
# |dtau/dt|_peak(t) = A * omega * exp(-Gamma * t)  [envelope of oscillations]
dtaudt_envelope = A_initial * omega_att * np.exp(-Gamma_Hubble * t_grid_MKK)

# Logarithmic a_2 derivative at fold (representative post-transit value)
dlna2_at_fold = np.abs(dlna2_dtau[idx_fold_hk])

# |dG/dt / G| = |d(ln a_2)/dtau| * |dtau/dt|, in M_KK units
dGdt_over_G_MKK = dlna2_at_fold * dtaudt_envelope

# Convert from M_KK units to yr^{-1}: multiply by yr_in_MKK (since M_KK time -> yr time)
# Actually: dG/dt/G has units of [time^{-1}]. In M_KK units it's [M_KK].
# To convert: [M_KK] -> [s^{-1}] -> [yr^{-1}]
# [M_KK] * (M_KK / hbar) = [s^{-1}]
# Then * seconds_per_year = [yr^{-1}]
# So: dGdt_over_G [yr^{-1}] = dGdt_over_G [M_KK] * (M_KK / hbar) * seconds_per_year
#   wait, that's wrong. dG/dt/G in natural units is already [energy] = [M_KK].
#   dG/dt/G [s^{-1}] = dG/dt/G [M_KK units] * M_KK [GeV] / hbar [GeV*s]
#                     = dG/dt/G [M_KK units] * (1 / t_MKK_seconds)
#   dG/dt/G [yr^{-1}] = above * seconds_per_year

# NO. Let me be precise. In the M_KK natural unit system where hbar=c=1,
# all quantities are powers of M_KK. Time has units M_KK^{-1}.
# dG/dt has units [time^{-1}] = [M_KK].
# So dG/dt/G is dimensionless per M_KK^{-1} time, i.e., units of M_KK.
# To convert to yr^{-1}:
#   dG/dt/G [yr^{-1}] = dG/dt/G [M_KK] * (M_KK * c^2 / hbar) * (yr / 1 s) ... no.
#
# Simpler: dG/dt/G [yr^{-1}] = dG/dt/G [M_KK^{-1} time^{-1}] / (1 yr in M_KK^{-1} units)
# Wait: if time is measured in units of M_KK^{-1}, and dG/dt/G has dimensions [time^{-1}],
# then dG/dt/G in M_KK^{-1} time units = some number. To get yr^{-1}, divide by
# (1 yr expressed in M_KK^{-1} units) = yr_in_MKK.
#
# NO. That inverts. Let me think again carefully.
#
# If I have dG/dt/G = X in units where t is in M_KK^{-1}, then X has units [M_KK].
# To get yr^{-1}: X [M_KK] * (conversion factor [yr^{-1} per M_KK])
# 1 M_KK [energy] = M_KK/hbar [s^{-1}] in SI
# So X [yr^{-1}] = X * (M_KK / hbar) [s^{-1}] * (s/yr)^{-1}
# = X * (1/t_MKK_seconds) * (1/seconds_per_year)^{-1}  ... that's getting confused.
#
# Let's be completely explicit:
# dG/dt/G = X  where X is a rate. In natural units (hbar=c=1), rates have dimension [energy].
# Physical rate in s^{-1}: X_phys = X * M_KK / hbar_SI ... no.
# In natural units where M_KK=1, time is measured in M_KK^{-1}.
# So X has units of M_KK. Convert M_KK to s^{-1}:
#   M_KK [GeV] -> M_KK [GeV] * GeV_to_inv_s [s^{-1}/GeV] = rate [s^{-1}]
#   GeV_to_inv_s = 1/(hbar_GeV_s) = 1/(6.582e-25) = 1.519e24 s^{-1}/GeV

dGdt_over_G_per_s = dGdt_over_G_MKK * M_KK * GeV_to_inv_s  # s^{-1}
dGdt_over_G_per_yr = dGdt_over_G_per_s * seconds_per_year  # yr^{-1}

# EP bound
EP_bound = 1.0e-13  # yr^{-1}, lunar laser ranging  # (local)

print(f"\n--- |dG/dt/G| at 10 post-transit times ---")
print(f"{'Time (MKK^-1)':>16s}  {'Time (yr)':>14s}  {'|dG/dt/G| (MKK)':>18s}  "
      f"{'|dG/dt/G| (yr^-1)':>20s}  {'EP bound':>12s}")
print("-" * 95)
for i in range(len(t_grid_MKK)):
    ep_status = "PASS" if dGdt_over_G_per_yr[i] < EP_bound else "FAIL"
    print(f"  {t_grid_MKK[i]:14.6e}  {t_grid_years[i]:14.6e}  "
          f"{dGdt_over_G_MKK[i]:18.6e}  {dGdt_over_G_per_yr[i]:20.6e}  {ep_status:>12s}")

# ============================================================================
#  Step 6: Settling timescale — when does |dG/dt/G| drop below EP bound?
# ============================================================================

# |dG/dt/G|(t) = |d(ln a_2)/dtau| * A * omega * exp(-Gamma*t) * (M_KK * GeV_to_inv_s * sec/yr)
# Set this = EP_bound and solve for t:
# exp(-Gamma*t) = EP_bound / (|d(ln a_2)/dtau| * A * omega * M_KK * GeV_to_inv_s * sec/yr)
# t = -(1/Gamma) * ln(rhs)

peak_rate_MKK = dlna2_at_fold * A_initial * omega_att  # peak |dG/dt/G| in M_KK units
peak_rate_per_yr = peak_rate_MKK * M_KK * GeV_to_inv_s * seconds_per_year

print(f"\n--- Settling timescale ---")
print(f"|d(ln a_2)/dtau| at fold = {dlna2_at_fold:.6f}")
print(f"A_initial = {A_initial:.6e}")
print(f"omega_att = {omega_att:.6f} M_KK")
print(f"Peak |dG/dt/G| at t=0: {peak_rate_MKK:.6e} M_KK = {peak_rate_per_yr:.6e} yr^{{-1}}")

ratio_for_settling = EP_bound / peak_rate_per_yr
if ratio_for_settling > 0 and ratio_for_settling < 1:
    t_settle_MKK = -(1.0 / Gamma_Hubble) * np.log(ratio_for_settling)
    t_settle_s = t_settle_MKK * t_MKK_seconds
    t_settle_yr = t_settle_s / seconds_per_year
    n_damping = t_settle_MKK / t_damp
    print(f"Settling time: {t_settle_MKK:.6e} M_KK^{{-1}} = {t_settle_s:.6e} s = {t_settle_yr:.6e} yr")
    print(f"  = {n_damping:.2f} damping times")
    print(f"  = {t_settle_yr / (t_universe_s / seconds_per_year):.6e} Hubble times")
elif ratio_for_settling >= 1:
    t_settle_MKK = 0.0  # (local)
    t_settle_yr = 0.0  # (local)
    n_damping = 0.0
    print(f"Already below EP bound at t=0! Ratio = {ratio_for_settling:.4e}")
else:
    t_settle_MKK = np.inf
    t_settle_yr = np.inf
    n_damping = np.inf
    print(f"Never settles (unphysical)")

# ============================================================================
#  Additional: dense time grid for the plot
# ============================================================================

# Dense log-spaced time grid
N_dense = 1000
t_dense_MKK = np.logspace(-2, 6, N_dense) * t_damp  # from 0.01 to 10^6 damping times
t_dense_yr = t_dense_MKK * t_MKK_seconds / seconds_per_year

dtaudt_dense = A_initial * omega_att * np.exp(-Gamma_Hubble * t_dense_MKK)
dGdt_G_dense_MKK = dlna2_at_fold * dtaudt_dense
dGdt_G_dense_yr = dGdt_G_dense_MKK * M_KK * GeV_to_inv_s * seconds_per_year

# Also compute the actual oscillatory solution for visual interest
omega_damped = np.sqrt(omega_att**2 - Gamma_Hubble**2) if omega_att > Gamma_Hubble else 0.0
tau_of_t_dense = tau_fold + A_initial * np.exp(-Gamma_Hubble * t_dense_MKK) * np.cos(omega_damped * t_dense_MKK)

# ============================================================================
#  SECTION: Framework-specific analysis
# ============================================================================

print(f"\n{'='*72}")
print("  PRINCIPLE-THEORETIC ANALYSIS")
print(f"{'='*72}")
print(f"""
The equivalence principle demands dG/dt/G be immeasurably small today.
In the spectral action framework, G_N ~ 1/a_2(tau), and a_2 depends on
the Jensen deformation parameter tau through:
  a_2(tau) = (4pi)^{{-4}} * (20/3) * R(tau) * Vol(tau)

Key structural points:

1. DURING TRANSIT: |dG/dt/G| is enormous ({peak_rate_per_yr:.2e} yr^{{-1}})
   because the modulus traverses the fold at terminal velocity. This is
   expected and unproblematic — no observers exist during the transit.

2. POST-TRANSIT SETTLING: The modulus oscillates and damps via Hubble
   friction (Gamma = 3H/2 = {Gamma_Hubble:.4f} M_KK). The quality factor
   Q = {Q_factor:.3f} means the oscillation is {'underdamped' if is_underdamped else 'overdamped'}.

3. HIERARCHY PROTECTION: The hierarchy M_KK/H_0 ~ 10^{{58}} provides
   enormous suppression. Even starting from |dG/dt/G| ~ {peak_rate_per_yr:.0e} yr^{{-1}},
   exponential damping drives this below 10^{{-13}} yr^{{-1}} in
   {n_damping:.1f} damping times = {t_settle_yr:.2e} yr.

4. EIH EFFACEMENT: By the EIH theorem (S44), test body motion is
   determined by the ASYMPTOTIC field, not internal structure. Post-
   transit, G_N is the asymptotic value. Oscillatory corrections are
   O(epsilon_H) ~ O(10^{{-2}}) relative corrections that damp exponentially.
""")

# ============================================================================
#  Specific post-transit tau values (as requested: 10 values with tau > 0.190)
# ============================================================================

# The task asks for 10 tau values post-transit. In the static picture,
# these are tau values > 0.190 from the a_2(tau) curve.
print(f"\n--- Static delta G_N/G_N at 10 post-transit tau values ---")
post_transit_mask = tau_arr > tau_fold + 1e-10
post_tau = tau_arr[post_transit_mask]

# Select 10 evenly spaced points from post-transit range
if len(post_tau) >= 10:
    indices = np.linspace(0, len(post_tau)-1, 10, dtype=int)
    tau_10 = post_tau[indices]
else:
    tau_10 = post_tau

# Compute a_2 at these 10 points
a2_fold_val = a2_tau[idx_fold_hk]
print(f"a_2(fold) = {a2_fold_val:.8f}")
print(f"{'tau':>8s}  {'a_2(tau)':>14s}  {'delta_a2/a2':>14s}  {'delta_GN/GN':>14s}")
print("-" * 58)
delta_GN_10 = []
for t in tau_10:
    idx = np.argmin(np.abs(tau_arr - t))
    da2 = (a2_tau[idx] - a2_fold_val) / a2_fold_val
    dGN = -da2
    delta_GN_10.append(dGN)
    print(f"  {t:.4f}  {a2_tau[idx]:14.8f}  {da2:+14.8f}  {dGN:+14.8f}")

delta_GN_10 = np.array(delta_GN_10)
print(f"\nMax |delta GN/GN| over post-transit range: {np.max(np.abs(delta_GN_10)):.6e}")
print(f"NOTE: These are STATIC variations (different tau, same time).")
print(f"      The DYNAMICAL question is how fast the modulus reaches its final tau.")

# ============================================================================
#  Gate verdict
# ============================================================================

# The late-time value (1000 damping times)
late_time_rate = dGdt_over_G_per_yr[-1]
transit_peak_rate = peak_rate_per_yr
settling_achieved = late_time_rate < EP_bound
immediate_pass = peak_rate_per_yr < EP_bound

print(f"\n{'='*72}")
print("  GATE VERDICT: EP-65")
print(f"{'='*72}")

if immediate_pass:
    verdict = "PASS"
    detail = (f"|dG/dt/G| < {EP_bound:.0e} yr^{{-1}} at ALL times post-transit. "
              f"Peak = {peak_rate_per_yr:.2e} yr^{{-1}}.")
elif settling_achieved:
    verdict = "PASS"
    detail = (f"|dG/dt/G| settles below {EP_bound:.0e} yr^{{-1}} after "
              f"{t_settle_yr:.2e} yr ({n_damping:.1f} damping times). "
              f"Peak during transit = {peak_rate_per_yr:.2e} yr^{{-1}}, "
              f"late-time = {late_time_rate:.2e} yr^{{-1}}.")
else:
    verdict = "FAIL"
    detail = (f"|dG/dt/G| = {late_time_rate:.2e} yr^{{-1}} at 1000 damping times, "
              f"exceeding EP bound {EP_bound:.0e} yr^{{-1}}.")

print(f"\nGate EP-65: {verdict}")
print(f"  Threshold: |dG/dt/G| < {EP_bound:.0e} yr^{{-1}} post-transit")
print(f"  Computed:  Peak = {peak_rate_per_yr:.2e} yr^{{-1}} (at transit exit)")
print(f"             Late = {late_time_rate:.2e} yr^{{-1}} (at 1000 damping times)")
print(f"             Settling time = {t_settle_yr:.2e} yr")
print(f"  Verdict:   {verdict}")
print(f"  Detail:    {detail}")

# Also check: is settling time negligible compared to universe age?
t_universe_yr = t_universe_s / seconds_per_year
print(f"\n  Age of universe: {t_universe_yr:.4e} yr")
print(f"  Settling time / age: {t_settle_yr / t_universe_yr:.4e}")
print(f"  Settling time / Planck time: {t_settle_MKK * t_MKK_seconds / 5.391e-44:.2e}")

# ============================================================================
#  Step 7: Save data
# ============================================================================

outpath = os.path.join(SCRIPT_DIR, 's65_ep_test.npz')
np.savez(outpath,
    # a_2 profile
    tau_arr=tau_arr,
    a2_tau=a2_tau,
    da2_dtau=da2_dtau,
    dlna2_dtau=dlna2_dtau,
    # G_N profile
    G_N_tau=G_N_tau,
    delta_GN_over_GN=delta_GN_over_GN,
    # Post-transit dynamics
    t_grid_MKK=t_grid_MKK,
    t_grid_years=t_grid_years,
    dGdt_over_G_MKK=dGdt_over_G_MKK,
    dGdt_over_G_per_yr=dGdt_over_G_per_yr,
    # Settling
    t_settle_MKK=t_settle_MKK,
    t_settle_yr=t_settle_yr,
    n_damping_times=n_damping,
    peak_rate_per_yr=peak_rate_per_yr,
    late_time_rate_per_yr=late_time_rate,
    # Physical parameters
    H_phys_MKK=H_phys_MKK,
    Gamma_Hubble=Gamma_Hubble,
    Q_factor=Q_factor,
    A_initial=A_initial,
    dlna2_at_fold=dlna2_at_fold,
    EP_bound=EP_bound,
    # Dense grid for plotting
    t_dense_yr=t_dense_yr,
    dGdt_G_dense_yr=dGdt_G_dense_yr,
    # 10 post-transit tau points
    tau_10_posttransit=tau_10,
    delta_GN_10=delta_GN_10,
    # Gate
    gate_name='EP-65',
    gate_verdict=verdict,
    gate_detail=detail,
)
print(f"\nData saved to {outpath}")

# ============================================================================
#  Step 8: Plot
# ============================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle(r'EP-65: Equivalence Principle Test — $\dot{G}/G$ Through Transit',
             fontsize=14, fontweight='bold')

# --- Panel (a): a_2(tau) and G_N(tau) ---
ax = axes[0, 0]
ax2 = ax.twinx()
l1 = ax.plot(tau_arr, a2_tau, 'b-', linewidth=2, label=r'$a_2(\tau)$')
l2 = ax2.plot(tau_arr, G_N_tau / G_N_tau[idx_fold_hk], 'r--', linewidth=2,
              label=r'$G_N(\tau)/G_N^{\mathrm{fold}}$')
ax.axvline(tau_fold, color='gray', linestyle=':', alpha=0.7, label='fold')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$a_2(\tau)$ [SD units]', color='b')
ax2.set_ylabel(r'$G_N(\tau)/G_N^{\mathrm{fold}}$', color='r')
ax.tick_params(axis='y', labelcolor='b')
ax2.tick_params(axis='y', labelcolor='r')
lines = l1 + l2
labels = [l.get_label() for l in lines]
ax.legend(lines, labels, loc='center left', fontsize=9)
ax.set_title(r'(a) $a_2(\tau)$ and $G_N(\tau) \propto 1/a_2$')

# --- Panel (b): d(ln a_2)/dtau ---
ax = axes[0, 1]
ax.plot(tau_arr, dlna2_dtau, 'k-', linewidth=2)
ax.axvline(tau_fold, color='gray', linestyle=':', alpha=0.7)
ax.axhline(0, color='gray', linestyle='-', alpha=0.3)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$d(\ln a_2)/d\tau$')
ax.set_title(r'(b) Logarithmic derivative')
ax.annotate(f'fold: {dlna2_dtau[idx_fold_hk]:.3f}',
            xy=(tau_fold, dlna2_dtau[idx_fold_hk]),
            xytext=(tau_fold + 0.05, dlna2_dtau[idx_fold_hk] + 0.3),
            arrowprops=dict(arrowstyle='->', color='red'),
            fontsize=10, color='red')

# --- Panel (c): |dG/dt/G| vs time (log-log) ---
ax = axes[1, 0]
ax.loglog(t_dense_yr, dGdt_G_dense_yr, 'b-', linewidth=2, label='|dG/dt/G| envelope')
ax.axhline(EP_bound, color='red', linestyle='--', linewidth=2, label=f'EP bound ({EP_bound:.0e} yr$^{{-1}}$)')
if t_settle_yr > 0 and t_settle_yr < 1e30:
    ax.axvline(t_settle_yr, color='green', linestyle=':', linewidth=1.5, label=f'Settling: {t_settle_yr:.1e} yr')
# Mark the 10 sampled points
ax.scatter(t_grid_years, dGdt_over_G_per_yr, c='red', s=40, zorder=5)
ax.set_xlabel('Time post-transit (yr)')
ax.set_ylabel(r'$|\dot{G}/G|$ (yr$^{-1}$)')
ax.set_title(r'(c) $|\dot{G}/G|$ settling')
ax.legend(fontsize=9, loc='upper right')
ax.set_ylim(bottom=1e-200)

# --- Panel (d): delta G_N/G_N at static tau values ---
ax = axes[1, 1]
ax.plot(tau_arr, delta_GN_over_GN * 100, 'k-', linewidth=2)
ax.axvline(tau_fold, color='gray', linestyle=':', alpha=0.7, label='fold')
ax.scatter(tau_10, delta_GN_10 * 100, c='red', s=40, zorder=5, label='10 post-transit points')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$\Delta G_N / G_N$ (%)')
ax.set_title(r'(d) Static $\Delta G_N/G_N$ relative to fold')
ax.legend(fontsize=9)

plt.tight_layout()
plotpath = os.path.join(SCRIPT_DIR, 's65_ep_test.png')
plt.savefig(plotpath, dpi=150, bbox_inches='tight')
print(f"Plot saved to {plotpath}")

print(f"\n{'='*72}")
print(f"  DONE. Gate EP-65: {verdict}")
print(f"{'='*72}")
