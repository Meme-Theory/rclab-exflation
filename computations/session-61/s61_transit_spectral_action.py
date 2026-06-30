#!/usr/bin/env python3
"""
s61_transit_spectral_action.py — TRANSIT-SA-61

Transit spectral action from families of spectral triples (Paper 02).

The universe does not sit at the fold — it TRANSITS through it.
Paper 02 (van den Dungen, 1711.07299) proves that for a family of
spectral triples {(A_tau, H_tau, D_tau)}, the product spectral triple
has Dirac operator:

    D_transit = gamma^0 d/dtau (x) 1 + 1 (x) D_K(tau)

and the spectral action factorizes:

    SA_transit = integral_0^{tau_fold} SA_static(tau) * omega_tau dtau
                 + kinetic correction from dD_K/dtau

This script computes:
1. SA_static(tau) at 50 points in [0, tau_fold]
2. The tau-integrated transit SA via trapezoidal quadrature
3. Kinetic correction from da_2/dtau (dominant contribution)
4. Comparison: transit SA vs static SA(tau_fold)

Gate: TRANSIT-SA-61
  PASS if |transit - static|/static > 10%
  FAIL if < 1%
  INFO if 1-10%

Author: Van den Dungen Bridge Theorist (S61 W3-04)
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
import sys

# NumPy 2.x compat: trapz -> trapezoid
_trapz = getattr(np, 'trapezoid', getattr(np, 'trapz', None))

# ------------------------------------------------------------------
# 0. Import canonical constants
# ------------------------------------------------------------------
sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import (
    tau_fold, omega_tau, M_KK_gravity, M_KK_kerner,
    Vol_SU3_Haar, PI, a0_fold, a2_fold, a4_fold,
    dt_transit, S_fold, Z_fold, G_DeWitt,
)

# ------------------------------------------------------------------
# 1. Load input data
# ------------------------------------------------------------------
base = Path(__file__).parent

# Heat kernel a_2 data (100 points, tau in [0, 0.5])
d_a2 = np.load(base / 's61_heat_kernel_a2.npz')
tau_full = d_a2['tau_arr']          # shape (100,), tau in [0, 0.5]
a2_SD_full = d_a2['a2_SD_arr']     # Seeley-DeWitt a_2(tau), normalised
a0_SD = float(d_a2['a0_SD'])       # a_0 normalised constant = sqrt(3)/2
R_full = d_a2['R_arr']             # scalar curvature R(tau)

# Derivative data (50 points, tau in [0, ~0.247])
d_der = np.load(base / 's61_a2_tau_derivative.npz')
tau_der = d_der['tau']              # shape (50,)
da2_analytic = d_der['da2_analytic']  # da_2^phys/dtau, all negative
a2_phys_der = d_der['a2_physical']  # a_2 with volume weighting
Vol_der = d_der['Vol']              # Vol(tau)
R_der = d_der['R']                  # R(tau) on derivative grid
dR_dtau = d_der['dR_dtau']         # dR/dtau

# Hessian data (for gradient stiffness)
d_hess = np.load(base / 's60_hessian_3d.npz')

print("=" * 72)
print("TRANSIT-SA-61: Transit Spectral Action from Families of Spectral Triples")
print("=" * 72)

# ------------------------------------------------------------------
# 2. Cutoff function values (from task spec)
# ------------------------------------------------------------------
# f_k = integral_0^inf f(x) x^{k-1} dx  (momenta of cutoff function)
# These are the standard spectral action expansion coefficients.
f_4 = 1.0       # default (volume term)  # (local)
f_2 = 2.34      # from W1 constraint equation  # (local)
f_0 = 1.0       # default pending W3 gauge coupling test  # (local)

print(f"\nCutoff function moments: f_4={f_4}, f_2={f_2}, f_0={f_0}")
print(f"tau_fold = {tau_fold}")
print(f"omega_tau = {omega_tau} (M_KK units)")
print(f"dt_transit = {dt_transit:.6e} (M_KK^-1)")

# ------------------------------------------------------------------
# 3. Compute Seeley-DeWitt coefficients a_0(tau), a_2(tau), a_4(tau)
# ------------------------------------------------------------------
# The spectral action on the internal space SU(3) with Jensen metric
# at deformation parameter tau expands as:
#
#   SA(tau, Lambda) = f_4 Lambda^8 a_0(tau)
#                   + f_2 Lambda^6 a_2(tau)
#                   + f_0 Lambda^4 a_4(tau) + O(Lambda^2)
#
# where Lambda is the KK cutoff in M_KK units.
# The a_k are the heat kernel coefficients of D_K(tau)^2.
#
# Convention: a_0(tau) = (4*pi)^{-d/2} * Vol(tau) for dim d=8 fiber+base
# For the internal SU(3) alone (d=8 total, d_F=8):
#   a_0(tau) = (4*pi)^{-4} * 16 * Vol(tau)
# But we use the NORMALISED values from the heat kernel computation.

# Build uniform grid in [0, tau_fold] with 50 points
N_transit = 50
tau_transit = np.linspace(0, tau_fold, N_transit)
dtau_transit = tau_transit[1] - tau_transit[0]

# Interpolate a2_SD from the 100-point grid onto our transit grid
a2_interp = np.interp(tau_transit, tau_full, a2_SD_full)

# Compute Vol(tau) for the Jensen metric on SU(3)
# Jensen metric: g(tau) = g_round + tau * g_deform
# Volume scales as Vol(tau) = Vol_Haar * det(g(tau)/g_round)^{1/2}
# From the derivative data, Vol goes from 1349.74 to ~392 at fold
Vol_interp = np.interp(tau_transit, tau_der, Vol_der)

# a_0(tau) normalised: proportional to volume
# At tau=0: a0_SD = sqrt(3)/2 = 0.8660254
# Scale: a_0(tau) = a0_SD * Vol(tau) / Vol(0)
a0_transit = a0_SD * Vol_interp / Vol_SU3_Haar

# For a_4(tau), we need the curvature-squared terms.
# From the hessian data, a4 at fold = 1350.72 (unnormalised).
# We use the same volume-scaling approach as a_2:
# a_4 involves R^2, Ricci^2, Riemann^2 — all increase with deformation.
# For the transit integral, a_4 is the LEAST important term (Lambda^4 vs Lambda^8).
# We compute it by interpolating from the available curvature data.
#
# From the derivative file: R(tau) increases from 2.0 to ~2.04 over [0, 0.25]
# a_4 ~ R^2 * Vol, so a_4(tau) / a_4(0) ~ [R(tau)/R(0)]^2 * Vol(tau)/Vol(0)
R_interp = np.interp(tau_transit, tau_der, R_der)

# a_4 normalised at fold: from canonical constants
# a_4_fold = 1350.72 (unnormalised).
# We need the normalised a_4.  Use the unnormalised values from hessian grid.
# The 3D hessian has a4_3d at (tau,sigma,d1) grid. At fold (idx=2):
a4_3d = d_hess['a4_3d']
# Centre of grid = (2,2,2) is (tau=0.19, sigma=0, d1=0)
a4_at_fold_hess = a4_3d[2, 2, 2]  # negative because of sign convention in hessian

# For the transit, a_4 is subdominant. Approximate:
# a_4(tau) = a4_fold * Vol(tau)/Vol(tau_fold) * [R(tau)/R(tau_fold)]^2
R_fold_val = np.interp(tau_fold, tau_der, R_der)
Vol_fold_val = np.interp(tau_fold, tau_der, Vol_der)

# Use normalised a4_fold from canonical_constants
a4_transit = a4_fold * (Vol_interp / Vol_fold_val) * (R_interp / R_fold_val)**2

print(f"\nGrid: {N_transit} points in [0, {tau_fold}]")
print(f"a0_SD(0) = {a0_transit[0]:.6f}, a0_SD(fold) = {a0_transit[-1]:.6f}")
print(f"a2_SD(0) = {a2_interp[0]:.6f}, a2_SD(fold) = {a2_interp[-1]:.6f}")
print(f"Vol(0) = {Vol_interp[0]:.2f}, Vol(fold) = {Vol_interp[-1]:.2f}")
print(f"R(0) = {R_interp[0]:.6f}, R(fold) = {R_interp[-1]:.6f}")

# ------------------------------------------------------------------
# 4. Compute SA_static(tau) at each grid point
# ------------------------------------------------------------------
# SA_static(tau) = f_4*Lambda^8*a_0(tau) + f_2*Lambda^6*a_2(tau)
#                + f_0*Lambda^4*a_4(tau)
#
# Here Lambda is dimensionless (in M_KK units).
# The KK cutoff Lambda is set by the largest eigenvalue of D_K.
# From s60_hessian_3d.npz: Lambda^2 = 16.98 => Lambda ~ 4.12
Lambda_sq = float(d_hess['Lambda_sq'])
Lambda = np.sqrt(Lambda_sq)

print(f"\nCutoff: Lambda^2 = {Lambda_sq:.4f}, Lambda = {Lambda:.4f}")
print(f"Lambda^4 = {Lambda_sq**2:.2f}")
print(f"Lambda^6 = {Lambda_sq**3:.2f}")
print(f"Lambda^8 = {Lambda_sq**4:.2f}")

# Compute each term
term_a0 = f_4 * Lambda_sq**4 * a0_transit   # Lambda^8 * a_0
term_a2 = f_2 * Lambda_sq**3 * a2_interp    # Lambda^6 * a_2
term_a4 = f_0 * Lambda_sq**2 * a4_transit    # Lambda^4 * a_4

SA_static = term_a0 + term_a2 + term_a4

print(f"\n--- SA_static components at tau=0 ---")
print(f"  f_4*Lambda^8*a_0(0) = {term_a0[0]:.4f}")
print(f"  f_2*Lambda^6*a_2(0) = {term_a2[0]:.4f}")
print(f"  f_0*Lambda^4*a_4(0) = {term_a4[0]:.4f}")
print(f"  SA_static(0) = {SA_static[0]:.4f}")

print(f"\n--- SA_static components at tau=tau_fold ---")
print(f"  f_4*Lambda^8*a_0(fold) = {term_a0[-1]:.4f}")
print(f"  f_2*Lambda^6*a_2(fold) = {term_a2[-1]:.4f}")
print(f"  f_0*Lambda^4*a_4(fold) = {term_a4[-1]:.4f}")
print(f"  SA_static(fold) = {SA_static[-1]:.4f}")

# ------------------------------------------------------------------
# 5. Transit spectral action: integral over tau
# ------------------------------------------------------------------
# From Paper 02 (van den Dungen 1711.07299), the product spectral triple
# factorizes the spectral action as:
#
#   SA_transit = integral_0^{tau_fold} SA_static(tau) * |dtau/dt| * dt
#              = (1/omega_tau) * integral_0^{tau_fold} SA_static(tau) dtau
#
# because dtau/dt = omega_tau (the transit frequency), so dt = dtau/omega_tau.
#
# The normalisation: we integrate SA(tau) over the transit path,
# then compare to SA_static at the fold point.
#
# Physical picture: the universe sweeps through the moduli space
# from tau=0 to tau=tau_fold. The effective spectral action is the
# time-averaged value along the path, weighted by the transit speed.

# Method A: Simple time-averaged SA (Paper 02 factorization)
# SA_avg = (1/tau_fold) * integral_0^{tau_fold} SA_static(tau) dtau
SA_integrated = _trapz(SA_static, tau_transit)
SA_avg = SA_integrated / tau_fold

print(f"\n{'='*72}")
print(f"METHOD A: Time-averaged spectral action (Paper 02 factorization)")
print(f"{'='*72}")
print(f"integral SA_static dtau = {SA_integrated:.4f}")
print(f"SA_avg = integral/tau_fold = {SA_avg:.4f}")
print(f"SA_static(fold) = {SA_static[-1]:.4f}")
print(f"Ratio SA_avg / SA_static(fold) = {SA_avg / SA_static[-1]:.6f}")
print(f"Fractional difference = {(SA_avg - SA_static[-1]) / SA_static[-1]:.6f}")
print(f"  = {abs(SA_avg - SA_static[-1]) / SA_static[-1] * 100:.2f}%")

# ------------------------------------------------------------------
# 6. Kinetic correction from dD_K/dtau
# ------------------------------------------------------------------
# The transit Dirac operator is D = gamma^0 partial_tau + D_K(tau).
# When D_K depends on tau, there is a kinetic correction from:
#   (dD_K/dtau)^2 ~ (da_k/dtau)^2 in the spectral action expansion.
#
# The leading correction to the spectral action is:
#   delta_SA_kin = (f_2/2) * Lambda^4 * integral_0^{tau_fold}
#                  (1/omega_tau^2) * (da_2/dtau)^2 dtau
#
# This is the "back-reaction" of modulus dynamics on the spectral action.
# It comes from the cross-term in D_transit^2 = (partial_tau)^2 + D_K^2
# + gamma^0 [partial_tau, D_K].
#
# The commutator term [partial_tau, D_K] = dD_K/dtau contributes at O(Lambda^4)
# through the heat kernel expansion of exp(-t D_transit^2).

# Interpolate da2/dtau onto transit grid
da2_interp = np.interp(tau_transit, tau_der, da2_analytic)

# The kinetic energy density in moduli space:
# E_kin(tau) = (1/2) * Z(tau) * (dtau/dt)^2 = (1/2) * Z * omega_tau^2
# where Z is the gradient stiffness (Z_fold from canonical constants).
# This contributes to the spectral action as an additional a_2-like term.

# Method 1: Direct from da_2/dtau
# The rate of change of the spectral action along the transit:
dSA_dtau = (f_4 * Lambda_sq**4 * np.gradient(a0_transit, dtau_transit)
          + f_2 * Lambda_sq**3 * da2_interp
          + f_0 * Lambda_sq**2 * np.gradient(a4_transit, dtau_transit))

# Kinetic correction: comes from the (dtau/dt) factor in the transit operator
# The transit operator has D = gamma^0 omega_tau d/dtau + D_K(tau)
# so D^2 = omega_tau^2 (d/dtau)^2 + D_K^2 + omega_tau gamma^0 dD_K/dtau
# The cross-term contributes:
#   delta_a_2^kin = (1/(4pi)^4) * omega_tau^2 * [commutator terms]
# In the heat kernel, this shows up as a correction to a_2:
#   delta_a_2 = omega_tau^2 / (12 * Lambda^2) * d^2(a_2)/dtau^2
# (from the standard heat kernel for time-dependent operators)

# Compute d^2 a_2 / dtau^2
d2a2_dtau2 = np.gradient(da2_interp, dtau_transit)

# The kinetic correction to the spectral action (from time-dependent heat kernel):
# delta_SA_kin = (f_2/6) * Lambda^4 * (omega_tau / Lambda)^2 *
#                integral_0^{tau_fold} d^2(a_2)/dtau^2 dtau
# This uses the standard result that for D(t) = D_0 + t*V,
# the heat kernel gains a correction ~ t^2 * V^2 / (6 Lambda^2)

kinetic_prefactor = (f_2 / 6.0) * Lambda_sq**2 * (omega_tau**2 / Lambda_sq)
delta_SA_kin_integrand = kinetic_prefactor * d2a2_dtau2
delta_SA_kin = _trapz(delta_SA_kin_integrand, tau_transit)

print(f"\n{'='*72}")
print(f"KINETIC CORRECTION (from dD_K/dtau)")
print(f"{'='*72}")
print(f"omega_tau = {omega_tau:.4f}")
print(f"omega_tau^2 / Lambda^2 = {omega_tau**2 / Lambda_sq:.6f}")
print(f"Kinetic prefactor = {kinetic_prefactor:.6f}")
print(f"delta_SA_kin = {delta_SA_kin:.6f}")
print(f"delta_SA_kin / SA_static(fold) = {delta_SA_kin / SA_static[-1]:.6e}")

# ------------------------------------------------------------------
# 7. Method B: Full transit SA with gradient stiffness
# ------------------------------------------------------------------
# The DeWitt sigma-model metric on moduli space gives a kinetic term:
#   T_moduli = (1/2) * G_DeWitt * (dtau/dt)^2 * SA''(tau)
# The gradient stiffness Z_fold = d^2 S / dtau^2 at the fold.
#
# The total transit action is:
#   S_transit = integral_0^{T} [ SA_static(tau(t)) + T_moduli ] dt
#             = integral_0^{tau_fold} [ SA_static(tau) + (1/2)*G*omega_tau^2*Z(tau) ]
#               * dtau / omega_tau

# Method B.1: Moduli kinetic contribution
# The gradient stiffness from S42: Z_fold = 74730.76
# Scale Z with tau: Z(tau) ~ d^2S/dtau^2, which we compute from SA_static
d2SA_dtau2 = np.gradient(np.gradient(SA_static, dtau_transit), dtau_transit)

# Kinetic energy in moduli space per unit tau:
T_moduli = 0.5 * G_DeWitt * omega_tau**2

# Total transit integrand: SA + moduli kinetic energy (constant)
SA_transit_integrand_B = SA_static + T_moduli

# Integrated transit SA (Method B)
SA_transit_B = _trapz(SA_transit_integrand_B, tau_transit) / tau_fold

print(f"\n{'='*72}")
print(f"METHOD B: Transit SA with moduli kinetic energy")
print(f"{'='*72}")
print(f"G_DeWitt = {G_DeWitt:.4f}")
print(f"T_moduli = (1/2)*G*omega_tau^2 = {T_moduli:.4f}")
print(f"T_moduli / SA_static(fold) = {T_moduli / SA_static[-1]:.6e}")
print(f"SA_transit_B (avg) = {SA_transit_B:.4f}")
print(f"Ratio SA_transit_B / SA_static(fold) = {SA_transit_B / SA_static[-1]:.6f}")

# ------------------------------------------------------------------
# 8. Method C: Cumulative transit SA (proper-time weighting)
# ------------------------------------------------------------------
# The most physically transparent computation:
# During transit, the universe accumulates spectral action.
# The transit speed is dtau/dt = omega_tau.
# Total proper-time at the fold: T = tau_fold / omega_tau.
#
# The transit-accumulated SA is:
#   SA_cumul = integral_0^T SA_static(tau(t)) dt
#            = integral_0^{tau_fold} SA_static(tau) dtau / omega_tau
#
# Compare this to what you'd get if the universe sat at the fold:
#   SA_static_sitting = SA_static(fold) * T = SA_static(fold) * tau_fold / omega_tau
#
# The ratio reveals the transit effect:
#   R = SA_cumul / SA_static_sitting = SA_avg / SA_static(fold)

T_transit = tau_fold / omega_tau  # proper time of transit
SA_cumul = _trapz(SA_static / omega_tau, tau_transit)
SA_sitting = SA_static[-1] * T_transit

print(f"\n{'='*72}")
print(f"METHOD C: Cumulative transit SA (proper-time weighting)")
print(f"{'='*72}")
print(f"Transit proper-time T = tau_fold/omega_tau = {T_transit:.6f} M_KK^-1")
print(f"SA_cumul = integral SA(tau)/omega_tau dtau = {SA_cumul:.4f}")
print(f"SA_sitting = SA(fold)*T = {SA_sitting:.4f}")
print(f"Ratio SA_cumul / SA_sitting = {SA_cumul / SA_sitting:.6f}")
print(f"Fractional excess = {(SA_cumul - SA_sitting) / SA_sitting:.6f}")
print(f"  = {(SA_cumul - SA_sitting) / SA_sitting * 100:.2f}%")

# ------------------------------------------------------------------
# 9. Decompose the transit excess into contributions
# ------------------------------------------------------------------
# The transit excess comes from the fact that SA(tau) is NOT constant.
# Decompose: SA(tau) = SA(fold) + delta_SA(tau)
# where delta_SA(tau) = SA(tau) - SA(fold)
delta_SA = SA_static - SA_static[-1]

# Contribution from each Seeley-DeWitt term
delta_a0 = term_a0 - term_a0[-1]
delta_a2 = term_a2 - term_a2[-1]
delta_a4 = term_a4 - term_a4[-1]

excess_a0 = _trapz(delta_a0, tau_transit) / (tau_fold * SA_static[-1])
excess_a2 = _trapz(delta_a2, tau_transit) / (tau_fold * SA_static[-1])
excess_a4 = _trapz(delta_a4, tau_transit) / (tau_fold * SA_static[-1])
excess_total = _trapz(delta_SA, tau_transit) / (tau_fold * SA_static[-1])

print(f"\n{'='*72}")
print(f"DECOMPOSITION OF TRANSIT EXCESS")
print(f"{'='*72}")
print(f"Excess from a_0 (volume) term:    {excess_a0:.6f} ({excess_a0*100:.3f}%)")
print(f"Excess from a_2 (curvature) term: {excess_a2:.6f} ({excess_a2*100:.3f}%)")
print(f"Excess from a_4 (Gauss-Bonnet):   {excess_a4:.6f} ({excess_a4*100:.3f}%)")
print(f"Total excess:                      {excess_total:.6f} ({excess_total*100:.3f}%)")

# Verify sum
print(f"Sum of parts:                      {excess_a0+excess_a2+excess_a4:.6f}")
print(f"Consistency check:                 {abs(excess_a0+excess_a2+excess_a4 - excess_total):.2e}")

# ------------------------------------------------------------------
# 10. Physical transit ratio (the gate number)
# ------------------------------------------------------------------
# The gate-relevant quantity is:
# |SA_transit - SA_static(fold)| / SA_static(fold)
#
# Where SA_transit is the time-averaged SA during transit.
# This measures how much the transit dynamics shift the effective
# spectral action relative to the static fold value.

transit_ratio = abs(SA_avg - SA_static[-1]) / abs(SA_static[-1])
transit_sign = np.sign(SA_avg - SA_static[-1])

# Also compute including kinetic correction
SA_total = SA_avg + delta_SA_kin
transit_ratio_total = abs(SA_total - SA_static[-1]) / abs(SA_static[-1])

print(f"\n{'='*72}")
print(f"TRANSIT-SA-61 GATE EVALUATION")
print(f"{'='*72}")
print(f"SA_static(fold)          = {SA_static[-1]:.6f}")
print(f"SA_transit (time-avg)    = {SA_avg:.6f}")
print(f"Kinetic correction       = {delta_SA_kin:.6e}")
print(f"SA_total (avg + kinetic) = {SA_total:.6f}")
print(f"")
print(f"Transit ratio (no kin)   = {transit_ratio:.6f} ({transit_ratio*100:.3f}%)")
print(f"Transit ratio (with kin) = {transit_ratio_total:.6f} ({transit_ratio_total*100:.3f}%)")
print(f"Direction: SA_transit {'>' if transit_sign > 0 else '<'} SA_static(fold)")
print(f"  (universe sees {'MORE' if transit_sign > 0 else 'LESS'} spectral action during transit)")

# Gate logic
if transit_ratio > 0.10:
    gate_verdict = "PASS"
    gate_detail = (f"Transit SA differs from static fold by {transit_ratio*100:.1f}%. "
                   f"S38 transit paradigm validated: effective SA during transit is "
                   f"{'enhanced' if transit_sign > 0 else 'reduced'} by path-averaging.")
elif transit_ratio < 0.01:
    gate_verdict = "FAIL"
    gate_detail = (f"Transit SA differs from static fold by only {transit_ratio*100:.2f}%. "
                   f"Static fold approximation adequate.")
else:
    gate_verdict = "INFO"
    gate_detail = (f"Transit SA differs from static fold by {transit_ratio*100:.2f}%. "
                   f"Marginal transit effect.")

print(f"\n*** GATE: TRANSIT-SA-61 = {gate_verdict} ***")
print(f"    {gate_detail}")

# ------------------------------------------------------------------
# 11. G_eff amplification cross-check
# ------------------------------------------------------------------
# HAWK-9 found G_eff amplifies 2.6x at fold.
# G_eff ~ 1/a_2 (since M_Pl^2 ~ f_2 * Lambda^2 * a_2 in spectral gravity).
# The transit-averaged G_eff is:
#   <G_eff> = <1/a_2> = (1/tau_fold) * integral_0^{tau_fold} 1/a_2(tau) dtau
# Jensen's inequality: <1/a_2> >= 1/<a_2> (since 1/x is convex).
# So the transit-averaged G_eff is ALWAYS >= G_eff at the mean a_2.

inv_a2 = 1.0 / a2_interp
Geff_avg = _trapz(inv_a2, tau_transit) / tau_fold
Geff_fold = 1.0 / a2_interp[-1]
Geff_initial = 1.0 / a2_interp[0]
Geff_ratio = Geff_avg / Geff_fold

# Jensen inequality check
a2_mean = _trapz(a2_interp, tau_transit) / tau_fold
jensen_bound = 1.0 / a2_mean
jensen_excess = Geff_avg / jensen_bound - 1.0

print(f"\n{'='*72}")
print(f"G_eff AMPLIFICATION CROSS-CHECK")
print(f"{'='*72}")
print(f"G_eff(0) ~ 1/a_2(0) = {Geff_initial:.6f}")
print(f"G_eff(fold) ~ 1/a_2(fold) = {Geff_fold:.6f}")
print(f"G_eff ratio initial/fold = {Geff_initial / Geff_fold:.4f}")
print(f"<G_eff>_transit = {Geff_avg:.6f}")
print(f"<G_eff>_transit / G_eff(fold) = {Geff_ratio:.6f}")
print(f"Jensen bound: 1/<a_2> = {jensen_bound:.6f}")
print(f"Jensen excess (<1/a_2> vs 1/<a_2>): {jensen_excess*100:.4f}%")
print(f"HAWK-9 reported G_eff amplification: 2.6x (= 1 + delta_G = 1 + 0.613)")
print(f"This computation: <G_eff>/<G_eff(fold)> = {Geff_ratio:.4f}")

# ------------------------------------------------------------------
# 12. Spectral action profile and breakdown
# ------------------------------------------------------------------
# Which term dominates the transit difference?
frac_a0 = abs(excess_a0) / (abs(excess_a0) + abs(excess_a2) + abs(excess_a4))
frac_a2 = abs(excess_a2) / (abs(excess_a0) + abs(excess_a2) + abs(excess_a4))
frac_a4 = abs(excess_a4) / (abs(excess_a0) + abs(excess_a2) + abs(excess_a4))

print(f"\n{'='*72}")
print(f"TERM DOMINANCE IN TRANSIT EXCESS")
print(f"{'='*72}")
print(f"a_0 (volume, Lambda^8):      {frac_a0*100:.1f}%")
print(f"a_2 (curvature, Lambda^6):   {frac_a2*100:.1f}%")
print(f"a_4 (Gauss-Bonnet, Lambda^4):{frac_a4*100:.1f}%")

# ------------------------------------------------------------------
# 13. Save all results
# ------------------------------------------------------------------
outpath = base / 's61_transit_spectral_action.npz'
np.savez(
    outpath,
    # Grid
    tau_transit=tau_transit,
    N_transit=N_transit,
    dtau_transit=dtau_transit,
    tau_fold=tau_fold,
    # Cutoff
    Lambda_sq=Lambda_sq,
    Lambda=Lambda,
    f_4=f_4,
    f_2=f_2,
    f_0=f_0,
    # Seeley-DeWitt coefficients along transit
    a0_transit=a0_transit,
    a2_transit=a2_interp,
    a4_transit=a4_transit,
    Vol_transit=Vol_interp,
    R_transit=R_interp,
    # Spectral action terms
    term_a0=term_a0,
    term_a2=term_a2,
    term_a4=term_a4,
    SA_static=SA_static,
    SA_static_fold=SA_static[-1],
    # Transit results
    SA_integrated=SA_integrated,
    SA_avg=SA_avg,
    SA_cumul=SA_cumul,
    SA_sitting=SA_sitting,
    delta_SA_kin=delta_SA_kin,
    SA_total=SA_total,
    # Ratios
    transit_ratio=transit_ratio,
    transit_ratio_total=transit_ratio_total,
    transit_sign=transit_sign,
    # Decomposition
    excess_a0=excess_a0,
    excess_a2=excess_a2,
    excess_a4=excess_a4,
    excess_total=excess_total,
    # G_eff
    Geff_avg=Geff_avg,
    Geff_fold=Geff_fold,
    Geff_ratio=Geff_ratio,
    jensen_excess=jensen_excess,
    # Gate
    gate_name='TRANSIT-SA-61',
    gate_verdict=gate_verdict,
    gate_detail=gate_detail,
    # Profiles
    dSA_dtau=dSA_dtau,
    da2_transit=da2_interp,
    d2SA_dtau2=d2SA_dtau2,
)
print(f"\nData saved to: {outpath}")

# ------------------------------------------------------------------
# 14. Plots
# ------------------------------------------------------------------
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle(f'TRANSIT-SA-61: Transit Spectral Action from Families of Spectral Triples\n'
             f'Gate: {gate_verdict} | Transit ratio = {transit_ratio*100:.1f}%',
             fontsize=13, fontweight='bold')

# (0,0): SA_static(tau) profile
ax = axes[0, 0]
ax.plot(tau_transit, SA_static, 'b-', lw=2, label=r'$S_\mathrm{A}^\mathrm{static}(\tau)$')
ax.axhline(SA_static[-1], color='r', ls='--', alpha=0.7, label=r'$S_\mathrm{A}(\tau_\mathrm{fold})$')
ax.axhline(SA_avg, color='g', ls='--', alpha=0.7, label=r'$\langle S_\mathrm{A}\rangle_\mathrm{transit}$')
ax.axvline(tau_fold, color='grey', ls=':', alpha=0.5)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$S_\mathrm{A}(\tau)$ [M$_\mathrm{KK}$ units]')
ax.set_title('Spectral Action Profile')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# (0,1): Individual SD terms
ax = axes[0, 1]
ax.plot(tau_transit, term_a0, 'r-', lw=1.5, label=r'$f_4\Lambda^8 a_0$')
ax.plot(tau_transit, term_a2, 'b-', lw=1.5, label=r'$f_2\Lambda^6 a_2$')
ax.plot(tau_transit, term_a4, 'g-', lw=1.5, label=r'$f_0\Lambda^4 a_4$')
ax.axvline(tau_fold, color='grey', ls=':', alpha=0.5)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel('Term value')
ax.set_title('Seeley-DeWitt Term Decomposition')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# (0,2): Volume and curvature evolution
ax = axes[0, 2]
ax2 = ax.twinx()
l1 = ax.plot(tau_transit, Vol_interp, 'b-', lw=2, label='Vol(tau)')
l2 = ax2.plot(tau_transit, R_interp, 'r-', lw=2, label='R(tau)')
ax.axvline(tau_fold, color='grey', ls=':', alpha=0.5)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel('Vol(tau)', color='b')
ax2.set_ylabel('R(tau)', color='r')
ax.set_title('Volume & Curvature Evolution')
lines = l1 + l2
ax.legend(lines, [l.get_label() for l in lines], fontsize=8)
ax.grid(True, alpha=0.3)

# (1,0): Transit excess decomposition
ax = axes[1, 0]
delta_a0_profile = (term_a0 - term_a0[-1]) / abs(SA_static[-1]) * 100
delta_a2_profile = (term_a2 - term_a2[-1]) / abs(SA_static[-1]) * 100
delta_a4_profile = (term_a4 - term_a4[-1]) / abs(SA_static[-1]) * 100
delta_total_profile = delta_SA / abs(SA_static[-1]) * 100

ax.fill_between(tau_transit, 0, delta_total_profile, alpha=0.2, color='purple')
ax.plot(tau_transit, delta_a0_profile, 'r-', lw=1.5, label=r'$\delta a_0$ (volume)')
ax.plot(tau_transit, delta_a2_profile, 'b-', lw=1.5, label=r'$\delta a_2$ (curvature)')
ax.plot(tau_transit, delta_a4_profile, 'g-', lw=1.5, label=r'$\delta a_4$ (G-B)')
ax.plot(tau_transit, delta_total_profile, 'k-', lw=2, label='Total')
ax.axvline(tau_fold, color='grey', ls=':', alpha=0.5)
ax.axhline(0, color='grey', ls='-', alpha=0.3)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$\delta S_\mathrm{A} / S_\mathrm{A}(\mathrm{fold})$ [%]')
ax.set_title('Transit Excess Decomposition')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# (1,1): G_eff evolution
ax = axes[1, 1]
Geff_profile = 1.0 / a2_interp / Geff_fold
ax.plot(tau_transit, Geff_profile, 'b-', lw=2)
ax.axhline(1.0, color='r', ls='--', alpha=0.7, label=r'$G_\mathrm{eff}(\tau_\mathrm{fold})$')
ax.axhline(Geff_ratio, color='g', ls='--', alpha=0.7,
           label=rf'$\langle G_\mathrm{{eff}}\rangle / G_\mathrm{{eff}}(\mathrm{{fold}})$ = {Geff_ratio:.3f}')
ax.axvline(tau_fold, color='grey', ls=':', alpha=0.5)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$G_\mathrm{eff}(\tau) / G_\mathrm{eff}(\tau_\mathrm{fold})$')
ax.set_title(r'$G_\mathrm{eff}$ Amplification During Transit')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# (1,2): Pie chart of transit excess by term
ax = axes[1, 2]
sizes = [abs(excess_a0), abs(excess_a2), abs(excess_a4)]
labels = [f'$a_0$ (volume)\n{excess_a0*100:.2f}%',
          f'$a_2$ (curvature)\n{excess_a2*100:.2f}%',
          f'$a_4$ (G-B)\n{excess_a4*100:.2f}%']
colors = ['#ff6b6b', '#4ecdc4', '#95e1d3']
wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors,
                                    autopct='%1.1f%%', startangle=90,
                                    textprops={'fontsize': 8})
ax.set_title('Transit Excess by SD Term')

plt.tight_layout()
plotpath = base / 's61_transit_spectral_action.png'
plt.savefig(plotpath, dpi=150, bbox_inches='tight')
print(f"Plot saved to: {plotpath}")

# ------------------------------------------------------------------
# 15. Summary table
# ------------------------------------------------------------------
print(f"\n{'='*72}")
print(f"SUMMARY TABLE")
print(f"{'='*72}")
print(f"{'Quantity':<40} {'Value':>15} {'Unit':>12}")
print(f"{'-'*67}")
print(f"{'tau_fold':<40} {tau_fold:>15.4f} {'':>12}")
print(f"{'omega_tau':<40} {omega_tau:>15.4f} {'M_KK':>12}")
print(f"{'Lambda (cutoff)':<40} {Lambda:>15.4f} {'M_KK':>12}")
print(f"{'f_2':<40} {f_2:>15.4f} {'':>12}")
print(f"{'-'*67}")
print(f"{'SA_static(0)':<40} {SA_static[0]:>15.4f} {'M_KK^0':>12}")
print(f"{'SA_static(fold)':<40} {SA_static[-1]:>15.4f} {'M_KK^0':>12}")
print(f"{'SA_transit (time-avg)':<40} {SA_avg:>15.4f} {'M_KK^0':>12}")
print(f"{'-'*67}")
print(f"{'Transit ratio |delta|/SA(fold)':<40} {transit_ratio:>15.6f} {'':>12}")
print(f"{'  = percentage':<40} {transit_ratio*100:>14.2f}% {'':>12}")
print(f"{'Kinetic correction / SA(fold)':<40} {abs(delta_SA_kin/SA_static[-1]):>15.2e} {'':>12}")
print(f"{'-'*67}")
print(f"{'Excess from a_0 (volume)':<40} {excess_a0*100:>14.3f}% {'':>12}")
print(f"{'Excess from a_2 (curvature)':<40} {excess_a2*100:>14.3f}% {'':>12}")
print(f"{'Excess from a_4 (Gauss-Bonnet)':<40} {excess_a4*100:>14.3f}% {'':>12}")
print(f"{'-'*67}")
print(f"{'<G_eff>_transit / G_eff(fold)':<40} {Geff_ratio:>15.6f} {'':>12}")
print(f"{'Jensen excess':<40} {jensen_excess*100:>14.4f}% {'':>12}")
print(f"{'-'*67}")
print(f"{'GATE: TRANSIT-SA-61':<40} {gate_verdict:>15} {'':>12}")

print(f"\n{'='*72}")
print("DONE")
print(f"{'='*72}")
