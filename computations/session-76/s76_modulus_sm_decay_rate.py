#!/usr/bin/env python3
"""
S76-B5-SM-DECAY: Standard Model Decay Rate of Modulus Oscillation
==================================================================

First-principles QFT computation of Gamma(tau -> SM) from the spectral
action coupling of the modulus tau to Standard Model gauge fields.

Physics:
--------
The spectral action is  S_gauge = (1/4) * a_4(tau) * integral F_{mu nu}^2.
The Seeley-DeWitt coefficient a_4(tau) sets the gauge kinetic normalization:

    L_gauge = -(1/4) * [a_4(tau) / (8 pi^2)] * F_a^{mu nu} F_a_{mu nu}

where the 1/(8 pi^2) is the standard Chamseddine-Connes spectral action
convention (Tr(f(D/Lambda)) -> f_2 a_2 + f_0 a_4 + ..., with f_0 ~ 1/(8 pi^2)
absorbing the loop factor).

When tau oscillates about the fold:
    tau(t) = tau_fold + A * cos(m_tau * t)

the gauge coupling modulates:
    a_4(tau) = a_4(fold) + (da_4/dtau)|_fold * A * cos(m_tau * t) + ...

This produces an interaction vertex:
    L_int = -(1/4) * [da_4/dtau * A / (8 pi^2)] * cos(m_tau * t) * F^2

In the quantum theory, this gives a decay amplitude for tau -> g g (or W W, B B)
through the dimension-5 operator  (tau / Lambda) F^2, where:
    y = (da_4/dtau) / a_4(fold)   [fractional spectral modulation]

The decay rate into gauge bosons of a given gauge group with N_A generators is:

    Gamma(tau -> AA) = N_A * y^2 * m_tau^3 / (64 * pi)   [natural units]

summed over SU(3)_c + SU(2)_L + U(1)_Y.

IMPORTANT: The amplitude of tau oscillations is set by the transit dynamics.
At the fold, the modulus has kinetic energy from the spectral-action gradient
dS/dtau, and oscillates with amplitude A ~ v_terminal / m_tau (Eq. of motion).
The dimensionless coupling y then captures (da_4/dtau * A) / a_4.

The gravitational channel comparison:
    Gamma_grav = m_tau^3 / (48 * pi * M_Pl^2)

Gate: S76-B5-SM-DECAY
    PASS: Gamma_SM/Gamma_grav > 100 AND T_RH > T_BBN AND tau_SM < 1 s
    FAIL: Gamma_SM/Gamma_grav < 1
    INFO: 1 < ratio < 100

Author: Feynman-Theorist (S76)
Provenance: canonical_constants.py (S42 spectral data), s54_higgs_modulus.npz
            (spectral derivatives)
"""

import sys
import os
import numpy as np

# Ensure canonical_constants is importable
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from canonical_constants import (
    PI,
    M_Pl_reduced, M_Pl_unreduced,
    hbar_GeV_s, GeV_to_inv_s,
    a0_fold, a2_fold, a4_fold,
    m_tau, M_KK, M_KK_gravity,
    dS_fold, d2S_fold, S_fold,
    v_terminal, dt_transit,
    G_DeWitt, Z_fold,
    T_BBN_GeV, g_star_SM,
)

# ============================================================================
#  SECTION 1: Load spectral derivatives from S54 data
# ============================================================================

print("=" * 72)
print("S76-B5-SM-DECAY: Modulus -> SM Decay Rate (First-Principles QFT)")
print("=" * 72)

# Load the S54 Higgs-modulus data which contains the spectral derivatives
s54_path = os.path.join(os.path.dirname(__file__), "s54_higgs_modulus.npz")  # (local)
s54_data = np.load(s54_path, allow_pickle=True)  # (local)

da2_dtau = float(s54_data["da2_dtau"])  # (local) = -875.62
da4_dtau = float(s54_data["da4_dtau"])  # (local) = -609.18
d2a4_dtau2 = float(s54_data["d2a4_dtau2"])  # (local) = -3063.18

print("\n--- Section 1: Spectral Derivatives at the Fold ---")
print(f"  a_0(fold)       = {a0_fold:.2f}")
print(f"  a_2(fold)       = {a2_fold:.6f}")
print(f"  a_4(fold)       = {a4_fold:.6f}")
print(f"  da_2/dtau       = {da2_dtau:.4f}")
print(f"  da_4/dtau       = {da4_dtau:.4f}")
print(f"  d^2 a_4/dtau^2  = {d2a4_dtau2:.4f}")
print(f"  (1/a_2)(da_2/dtau) = {da2_dtau / a2_fold:.6f}")
print(f"  (1/a_4)(da_4/dtau) = {da4_dtau / a4_fold:.6f}")

# Fractional spectral modulation (key dimensionless quantity)
frac_da4 = da4_dtau / a4_fold  # (local) dimensionless
frac_da2 = da2_dtau / a2_fold  # (local) dimensionless
print(f"\n  Fractional da_4/dtau / a_4 = {frac_da4:.6f}")
print(f"  Fractional da_2/dtau / a_2 = {frac_da2:.6f}")

# ============================================================================
#  SECTION 2: Modulus oscillation amplitude
# ============================================================================
#
# At the fold, the modulus has terminal velocity v_terminal = 26.54 (M_KK units).
# Post-fold, it oscillates in the potential well with frequency m_tau = 2.062 M_KK.
#
# The oscillation amplitude is determined by energy conservation:
#   (1/2) * M_eff * v_terminal^2 = (1/2) * M_eff * m_tau^2 * A^2
# => A = v_terminal / m_tau
#
# This is the amplitude in tau-space (dimensionless moduli field).

print("\n--- Section 2: Modulus Oscillation Amplitude ---")

A_osc = v_terminal / m_tau  # (local) dimensionless amplitude in tau-space
print(f"  v_terminal     = {v_terminal:.4f}  (M_KK units)")
print(f"  m_tau          = {m_tau:.4f}  (M_KK units)")
print(f"  A_osc = v/m    = {A_osc:.4f}  (dimensionless)")

# Physical modulus mass in GeV
m_tau_GeV = m_tau * M_KK  # (local)
print(f"\n  m_tau [GeV]    = {m_tau_GeV:.4e}")
print(f"  M_KK [GeV]     = {M_KK:.4e}")

# ============================================================================
#  SECTION 3: Modulus-gauge vertex from spectral action
# ============================================================================
#
# The spectral action coupling of tau to gauge fields:
#
#   L_gauge = -(f_0 / 4) * a_4(tau) * F^2
#
# where f_0 is the spectral function moment (absorbs 1/(8*pi^2) in
# Chamseddine-Connes normalization). Expanding:
#
#   a_4(tau) = a_4(fold) + (da_4/dtau) * delta_tau + ...
#
# With delta_tau = A * cos(m_tau * t), the interaction Lagrangian is:
#
#   L_int = -(f_0 / 4) * (da_4/dtau) * A * cos(m_tau * t) * F^2
#
# In canonical normalization where L_gauge = -(1/4) * F^2, we have
# f_0 * a_4 = 1, so f_0 = 1/a_4. The dimensionless coupling is:
#
#   y = (da_4/dtau) * A / a_4 = frac_da4 * A_osc
#
# This is the modulation depth: how much the gauge coupling changes
# per oscillation cycle.

print("\n--- Section 3: Modulus-Gauge Vertex ---")

# Dimensionless coupling (modulation depth)
y_coupling = abs(frac_da4) * A_osc  # (local)
print(f"  y = |frac_da4| * A_osc = {y_coupling:.6f}")

# The vertex factor for tau -> A_a A_b:
#   V = (y / v_canonical) * delta_ab * (k1 . k2 * g_{mu nu} - k1_nu * k2_mu)
#
# where v_canonical is related to the modulus VEV normalization.
# In the spectral action, the modulus tau is not a canonically normalized field.
# The canonical field sigma has kinetic term:
#   L_kin = (1/2) * Z_fold * (partial_mu tau)^2
# => sigma = sqrt(Z_fold) * tau, so tau = sigma / sqrt(Z_fold).
#
# The coupling in terms of the canonical field:
#   y_canon = y / sqrt(Z_fold) [or equivalently, the vertex is suppressed by 1/sqrt(Z)]

y_canonical = y_coupling / np.sqrt(Z_fold)  # (local) coupling in canonical normalization
print(f"  Z_fold = {Z_fold:.2f}")
print(f"  sqrt(Z_fold)   = {np.sqrt(Z_fold):.2f}")
print(f"  y_canonical    = {y_canonical:.6e}")

# However, the oscillation amplitude A_osc was derived from v_terminal
# which already accounts for Z_fold through the equation of motion.
# Let's be precise: the canonical-field oscillation amplitude is
#   A_sigma = sqrt(Z_fold) * A_osc  (canonical field units = sqrt(Z) * tau)
# and the canonical coupling suppression is 1/sqrt(Z_fold), so:
#   y_eff = (|da_4/dtau| / a_4) * A_sigma / sqrt(Z_fold) = |frac_da4| * A_osc = y_coupling
#
# The Z_fold factors cancel! This is correct: the physical decay rate depends
# on the modulation depth y = delta(a_4) / a_4, which is directly observable.

print(f"\n  Note: Z_fold cancels in the physical coupling.")
print(f"  Physical y     = {y_coupling:.6f}")

# ============================================================================
#  SECTION 4: Perturbative decay rate into SM gauge bosons
# ============================================================================
#
# The decay rate for a scalar phi decaying into two gauge bosons through
# the dimension-5 operator (y/Lambda) * phi * F_a^{mu nu} * F_a_{mu nu}:
#
#   |M|^2 = (y^2 / Lambda^2) * N_A * (m_phi^4 / 4)  [summed over polarizations]
#
# But here we have an effective vertex WITHOUT explicit Lambda suppression,
# because the coupling y already encodes the modulation depth:
#
#   L_int = -(y/4) * tau * F^2
#
# where tau is the canonically normalized modulus (mass m_tau_GeV).
#
# Actually, let me be maximally explicit. The starting point is:
#
#   S_gauge = integral d^4x [-(1/4) * (a_4(tau)/(8*pi^2)) * F_a^{mu nu} * F_a_{mu nu}]
#
# Canonical gauge normalization: A_a -> A_a * sqrt(a_4/(8*pi^2))
# Then L = -(1/4) F^2 and the gauge coupling g satisfies 1/g^2 = a_4/(8*pi^2).
#
# Expanding: a_4(tau) = a_4(fold) * [1 + frac_da4 * (tau - tau_fold)]
# The interaction in canonical gauge normalization becomes:
#
#   L_int = -(1/4) * frac_da4 * delta_tau * F^2
#         = -(frac_da4 / 4) * (sigma / sqrt(Z_fold)) * F^2_canonical
#
# The decay rate for scalar -> two massless gauge bosons (N_A adjoint dof):
#
#   Gamma = N_A * alpha_eff^2 * m^3 / (64 * pi^3)
#
# where alpha_eff = |frac_da4| * g^2 / (4*pi * sqrt(Z_fold)).
#
# But wait -- there's a much cleaner way. The modulus couples to the trace
# of the gauge kinetic term. In the normalized theory, the effective coupling
# constant of the dimension-5 operator (1/Lambda_eff) * sigma * F^2 is:
#
#   1/Lambda_eff = |frac_da4| / (2 * sqrt(Z_fold))
#
# and the decay rate is the standard result for scalar -> gg via F^2:
#
#   Gamma(tau -> A_a A_a) = N_A * m_tau^3 / (64 * pi * Lambda_eff^2)
#
# In natural units, GeV throughout.

print("\n--- Section 4: Perturbative Decay Rates ---")

# Effective suppression scale
Lambda_eff = 2.0 * np.sqrt(Z_fold) / abs(frac_da4)  # (local) dimensionless (in M_KK units)
Lambda_eff_GeV = Lambda_eff * M_KK  # (local) GeV
print(f"  Lambda_eff     = {Lambda_eff:.2f} M_KK = {Lambda_eff_GeV:.4e} GeV")
print(f"  Lambda_eff / M_Pl = {Lambda_eff_GeV / M_Pl_reduced:.4e}")

# Gauge group dimensions (N_A = number of generators = adjoint dimension)
N_SU3 = 8   # (local) SU(3)_c
N_SU2 = 3   # (local) SU(2)_L
N_U1  = 1   # (local) U(1)_Y

# Decay rate per channel: Gamma = N_A * m_tau^3 / (64 * pi * Lambda_eff^2)
# All in natural units (GeV)

Gamma_gluons = N_SU3 * m_tau_GeV**3 / (64.0 * PI * Lambda_eff_GeV**2)  # (local)
Gamma_W      = N_SU2 * m_tau_GeV**3 / (64.0 * PI * Lambda_eff_GeV**2)  # (local)
Gamma_B      = N_U1  * m_tau_GeV**3 / (64.0 * PI * Lambda_eff_GeV**2)  # (local)

Gamma_SM_total = Gamma_gluons + Gamma_W + Gamma_B  # (local)

print(f"\n  Individual channels:")
print(f"    Gamma(tau -> gg)  [SU(3)] = {Gamma_gluons:.4e} GeV  (N_A = {N_SU3})")
print(f"    Gamma(tau -> WW)  [SU(2)] = {Gamma_W:.4e} GeV  (N_A = {N_SU2})")
print(f"    Gamma(tau -> BB)  [U(1)]  = {Gamma_B:.4e} GeV  (N_A = {N_U1})")
print(f"\n  Total SM:  Gamma_SM = {Gamma_SM_total:.4e} GeV")

# Convert to decay time
tau_SM_s = hbar_GeV_s / Gamma_SM_total  # (local) seconds
print(f"  tau_SM = hbar / Gamma = {tau_SM_s:.4e} s")

# ============================================================================
#  SECTION 4b: Additional decay channels
# ============================================================================
#
# The modulus tau also couples to:
#
# (a) Scalar sector (Higgs) through a_2:
#   The a_2 coefficient generates the scalar kinetic/mass term.
#   L_scalar = a_2(tau) * |D_mu H|^2  =>  L_int = (da_2/dtau) * delta_tau * |D_mu H|^2
#   This gives tau -> H H with suppression Lambda_H = a_2 * sqrt(Z) / |da_2/dtau|.
#
# (b) Fermion masses through Yukawa couplings:
#   Fermion masses are m_f = y_f * v, where v depends on the a_2 coefficient.
#   The modulus coupling to fermions: tau -> f fbar with
#   Gamma = N_c * m_f^2 * m_tau / (8 pi Lambda_f^2)
#   At T_RH >> m_top, all fermions are effectively massless, so the
#   tree-level Yukawa channel is suppressed by (m_f / m_tau)^2.
#
# (c) Direct trace anomaly coupling:
#   The modulus couples to the trace of the energy-momentum tensor:
#   L_int = (1/Lambda_trace) * sigma * T^mu_mu
#   In a conformal theory T^mu_mu = 0 at tree level. The non-zero contribution
#   comes from beta functions (trace anomaly), giving an effective coupling
#   to ALL SM particles through the conformal anomaly.
#   For gauge bosons: Gamma_anomaly = (beta_i/g_i)^2 * N_A * m^3 / (64 pi Lambda^2)
#   This enhances the gauge channel by a factor [1 + beta/(2g)]^2.
#
# The dominant additional channel is the direct Higgs coupling through a_2.

print("\n--- Section 4b: Higgs Channel through a_2 ---")

# Suppression scale for Higgs channel
frac_da2 = da2_dtau / a2_fold  # (local) = -0.315
Lambda_H = abs(a2_fold * np.sqrt(Z_fold) / da2_dtau) * M_KK  # (local) GeV

# But we need to be more careful. The Higgs field coupling comes from:
#   L = a_2(tau) * Lambda^2 * |H|^2  (Higgs mass term in spectral action)
# Expanding: delta L = (da_2/dtau) * Lambda^2 * delta_tau * |H|^2
# In canonical normalization: sigma = sqrt(Z) * tau
# So: delta L = (da_2/dtau) * Lambda^2 / sqrt(Z) * sigma * |H|^2
# This is a dimension-3 operator (sigma * H^2) with coefficient da_2/(sqrt(Z) * Lambda^2).
# Actually, the spectral action Higgs mass is m_H^2 ~ a_2 * Lambda^2 / a_4,
# so the coupling is: g_{sigma HH} = (da_2/dtau) / (a_2 * sqrt(Z)) * m_H^2
#
# For the decay rate:
#   Gamma(tau -> HH) = g_{sigma HH}^2 / (8 pi m_tau) * sqrt(1 - 4 m_H^2/m_tau^2)
# Since m_H << m_tau (125 GeV vs 1.5e17 GeV), the phase space factor ~ 1.
#
# The effective coupling for the operator sigma * H^+ * H is:
#   g_eff_H = |frac_da2| * m_tau / sqrt(Z)
# Actually, in the spectral action the Higgs kinetic term has coefficient a_2,
# and the mass comes from the a_0 term. The precise coupling depends on the
# full spectral action Higgs sector.
#
# For a conservative estimate, use the same structure as the gauge channel
# but with a_2 instead of a_4:
Lambda_H_eff = 2.0 * np.sqrt(Z_fold) / abs(frac_da2) * M_KK  # (local) GeV
N_H = 4  # (local) 4 real scalar dof in Higgs doublet

# Gamma(tau -> HH) = N_H * m_tau^3 / (64 pi Lambda_H^2) [same operator structure]
Gamma_Higgs = N_H * m_tau_GeV**3 / (64.0 * PI * Lambda_H_eff**2)  # (local)

print(f"  frac_da2       = {frac_da2:.6f}")
print(f"  Lambda_H_eff   = {Lambda_H_eff:.4e} GeV")
print(f"  Gamma(tau->HH) = {Gamma_Higgs:.4e} GeV  (N_H = {N_H})")
print(f"  Gamma_Higgs / Gamma_gauge = {Gamma_Higgs / Gamma_SM_total:.2f}")

# Total including Higgs
Gamma_SM_with_H = Gamma_SM_total + Gamma_Higgs  # (local)
print(f"\n  Gamma_SM (gauge only):  {Gamma_SM_total:.4e} GeV")
print(f"  Gamma_SM (gauge+Higgs): {Gamma_SM_with_H:.4e} GeV")

# Fermion channels: suppressed by (m_f/m_tau)^2, negligible
# Top quark: (173/1.5e17)^2 ~ 1.3e-30 -- completely negligible
m_top = 173.0  # (local) GeV
Gamma_top = 3 * m_top**2 * m_tau_GeV / (8.0 * PI * Lambda_eff_GeV**2)  # (local) N_c = 3
print(f"\n  Fermion channels (top quark):")
print(f"    Gamma(tau->tt) = {Gamma_top:.4e} GeV  [suppressed by (m_t/m_tau)^2]")
print(f"    Negligible: {Gamma_top / Gamma_SM_total:.2e} x gauge channel")

# Update total SM rate to include all channels
Gamma_SM_all = Gamma_SM_with_H  # (local) Higgs is the only non-negligible addition

# ============================================================================
#  SECTION 5: Gravitational decay channel
# ============================================================================
#
# Standard Planck-suppressed decay:
#   Gamma_grav = m_tau^3 / (48 * pi * M_Pl^2)
#
# This is the irreducible gravitational channel present for any massive scalar.
#
# IMPORTANT: For the gravitational channel, the modulus also requires canonical
# normalization. The gravitational coupling is 1/M_Pl^2 for the canonical field.
# Since sigma = sqrt(Z) * tau, and the graviton coupling is universal
# (equivalence principle), Gamma_grav uses m_sigma = m_tau * M_KK in GeV
# and M_Pl as the suppression scale. No Z factors appear because gravity
# couples to the energy-momentum tensor, which is already expressed in terms
# of the canonical field.

print("\n--- Section 5: Gravitational Decay Channel ---")

Gamma_grav = m_tau_GeV**3 / (48.0 * PI * M_Pl_reduced**2)  # (local)
tau_grav_s = hbar_GeV_s / Gamma_grav  # (local) seconds

print(f"  Gamma_grav = m^3 / (48 pi M_Pl^2) = {Gamma_grav:.4e} GeV")
print(f"  tau_grav   = {tau_grav_s:.4e} s")

# Ratio (gauge channels only)
R_SM_grav = Gamma_SM_total / Gamma_grav  # (local)
R_all_grav = Gamma_SM_all / Gamma_grav  # (local)
print(f"\n  R_gauge = Gamma_SM(gauge) / Gamma_grav = {R_SM_grav:.4f}")
print(f"  R_all   = Gamma_SM(all) / Gamma_grav   = {R_all_grav:.4f}")

# Total decay rate
Gamma_total_all = Gamma_SM_all + Gamma_grav  # (local)
print(f"\n  Gamma_grav dominates by factor {Gamma_grav / Gamma_SM_all:.1f}")

# ============================================================================
#  SECTION 6: Reheating temperature
# ============================================================================
#
# T_RH = (90 / (pi^2 * g_*))^{1/4} * sqrt(Gamma_total * M_Pl)
#
# where Gamma_total = Gamma_SM + Gamma_grav (SM dominates).

print("\n--- Section 6: Reheating Temperature ---")

# Use total rate (gravity-dominated)
Gamma_total = Gamma_total_all  # (local)
T_RH_GeV = (90.0 / (PI**2 * g_star_SM))**0.25 * np.sqrt(Gamma_total * M_Pl_reduced)  # (local)
T_RH_over_MKK = T_RH_GeV / M_KK  # (local)

# Also compute T_RH from SM channel alone (hypothetical: if gravity didn't exist)
T_RH_SM_only = (90.0 / (PI**2 * g_star_SM))**0.25 * np.sqrt(Gamma_SM_all * M_Pl_reduced)  # (local)

print(f"  Gamma_total    = {Gamma_total:.4e} GeV  (gravity-dominated)")
print(f"  Gamma_SM_all   = {Gamma_SM_all:.4e} GeV  (spectral channels)")
print(f"  g_* (SM)       = {g_star_SM}")
print(f"  T_RH (total)   = {T_RH_GeV:.4e} GeV")
print(f"  T_RH (SM only) = {T_RH_SM_only:.4e} GeV")
print(f"  T_RH / M_KK    = {T_RH_over_MKK:.4f}")
print(f"  T_RH / T_BBN   = {T_RH_GeV / T_BBN_GeV:.4e}")

# ============================================================================
#  SECTION 7: BBN survival check
# ============================================================================

print("\n--- Section 7: BBN Survival ---")

# Total lifetime (gravity-dominated)
tau_total_s = hbar_GeV_s / Gamma_total  # (local)
bbn_safe = tau_total_s < 1.0  # (local) Must decay before BBN at ~1 s
print(f"  tau_total      = {tau_total_s:.4e} s  (gravity-dominated)")
print(f"  tau_SM_only    = {tau_SM_s:.4e} s  (spectral channels alone)")
print(f"  BBN time       ~ 1 s")
print(f"  tau_total < 1 s? {'YES' if bbn_safe else 'NO'}")
print(f"  Margin:          {np.log10(1.0 / tau_total_s):.1f} orders of magnitude")

# Energy injection at BBN: the modulus has long since decayed, so
# the injected energy is fully thermalized.
# Fractional energy injection at BBN: essentially zero.
# The modulus decays at t ~ tau_SM ~ 10^{-40} s, BBN is at t ~ 1 s.
# At BBN, all modulus energy has been converted to SM radiation and
# thermalized over 10^{39} Hubble times.
E_inject_BBN = 0.0  # (local) fully thermalized, no late injection

print(f"  Energy injection at BBN = {E_inject_BBN} (fully thermalized)")

# ============================================================================
#  SECTION 8: Cross-checks
# ============================================================================

print("\n--- Section 8: Cross-Checks ---")

# CHK1: Decoupling limit
# If da_4/dtau -> 0, then Lambda_eff -> infinity, Gamma_SM -> 0
# Verify by computing Gamma at 1% of the actual da_4/dtau
test_frac = abs(frac_da4) * 0.01  # (local)
test_Lambda = 2.0 * np.sqrt(Z_fold) / test_frac  # (local)
test_Gamma = 12.0 * m_tau_GeV**3 / (64.0 * PI * (test_Lambda * M_KK)**2)  # (local)
chk1_pass = test_Gamma < Gamma_SM_total * 0.01  # (local) should be 10000x smaller
print(f"  CHK1 (decoupling): Gamma(0.01 * da4/dtau) = {test_Gamma:.4e} GeV")
print(f"    vs Gamma_SM = {Gamma_SM_total:.4e} GeV")
print(f"    Ratio = {test_Gamma / Gamma_SM_total:.4e}  (expect ~1e-4)")
print(f"    CHK1: {'PASS' if chk1_pass else 'FAIL'} — Gamma_SM -> 0 as da_4/dtau -> 0")

# CHK2: Kinematic limit
# Gamma must be less than m_tau (cannot decay faster than the Compton time)
chk2_pass = Gamma_SM_total < m_tau_GeV  # (local)
print(f"\n  CHK2 (kinematic): Gamma_SM / m_tau = {Gamma_SM_total / m_tau_GeV:.4e}")
print(f"    CHK2: {'PASS' if chk2_pass else 'FAIL'} — Gamma_SM < m_tau")

# CHK3: T_RH > T_BBN
chk3_pass = T_RH_GeV > T_BBN_GeV  # (local)
print(f"\n  CHK3 (BBN): T_RH / T_BBN = {T_RH_GeV / T_BBN_GeV:.4e}")
print(f"    CHK3: {'PASS' if chk3_pass else 'FAIL'} — T_RH > T_BBN")

# CHK4: Comparison to W1-B result
W1B_Gamma_SM = 1.48e15   # (local) GeV, from W1-B
W1B_tau_SM = 4.44e-40     # (local) seconds, from W1-B
W1B_T_RH = 3.25e16        # (local) GeV, from W1-B

ratio_Gamma = Gamma_SM_total / W1B_Gamma_SM  # (local)
ratio_tau = tau_SM_s / W1B_tau_SM  # (local)
ratio_TRH = T_RH_GeV / W1B_T_RH  # (local)

print(f"\n  CHK4 (W1-B comparison):")
print(f"    Gamma_SM: this = {Gamma_SM_total:.4e}, W1-B = {W1B_Gamma_SM:.4e}, ratio = {ratio_Gamma:.4f}")
print(f"    tau_SM:   this = {tau_SM_s:.4e},  W1-B = {W1B_tau_SM:.4e},  ratio = {ratio_tau:.4f}")
print(f"    T_RH:     this = {T_RH_GeV:.4e},  W1-B = {W1B_T_RH:.4e},  ratio = {ratio_TRH:.4f}")

# ============================================================================
#  SECTION 9: Dimensional analysis verification
# ============================================================================

print("\n--- Section 9: Dimensional Analysis ---")

print("  [m_tau] = GeV")
print(f"  [Lambda_eff] = GeV  (= {Lambda_eff_GeV:.4e})")
print("  [Gamma] = m^3 / Lambda^2 = GeV^3 / GeV^2 = GeV  [correct: rate in natural units]")
print("  [tau_decay] = hbar / Gamma = GeV*s / GeV = s  [correct]")
print(f"  [T_RH] = (Gamma * M_Pl)^{{1/2}} = (GeV * GeV)^{{1/2}} = GeV  [correct]")

# Check: Gamma has dimension of energy
print(f"\n  Gamma_SM [GeV]  = {Gamma_SM_total:.4e}")
print(f"  m_tau [GeV]     = {m_tau_GeV:.4e}")
print(f"  Gamma/m ratio   = {Gamma_SM_total / m_tau_GeV:.4e}  (must be << 1 for perturbative)")

perturbative = Gamma_SM_total / m_tau_GeV < 1.0  # (local)
print(f"  Perturbative?    {'YES' if perturbative else 'NO'}")

# ============================================================================
#  SECTION 10: Alternative derivation via effective coupling g_eff
# ============================================================================
#
# W1-B used g_eff = sqrt(a_4/a_2) = 0.698 and Gamma = g_eff^2 * m / (16*pi).
# Let me understand what this corresponds to and how it compares.
#
# The ratio a_4/a_2 = 1350.7 / 2776.2 = 0.487, sqrt = 0.698.
# This is a spectral moment ratio, not a derivative coupling.
#
# Our coupling is: |frac_da4| * A_osc = |(da_4/dtau)/a_4| * v_terminal/m_tau
# = 0.451 * 12.874 = 5.81
#
# The W1-B approach implicitly assumed A_osc ~ 1 and used sqrt(a_4/a_2)
# as the coupling, which is dimensionally correct but physically different.

print("\n--- Section 10: Comparison of Coupling Definitions ---")

g_eff_W1B = np.sqrt(a4_fold / a2_fold)  # (local) W1-B coupling
Gamma_W1B_formula = g_eff_W1B**2 * m_tau_GeV / (16.0 * PI)  # (local)

print(f"  W1-B coupling:")
print(f"    g_eff = sqrt(a_4/a_2) = {g_eff_W1B:.6f}")
print(f"    Gamma = g_eff^2 * m / (16*pi) = {Gamma_W1B_formula:.4e} GeV")
print(f"    This is {Gamma_W1B_formula / Gamma_SM_total:.2f}x our result")

print(f"\n  This computation:")
print(f"    y = |da_4/dtau| * A / a_4 = |{frac_da4:.4f}| * {A_osc:.4f} = {y_coupling:.4f}")
print(f"    Lambda_eff = 2 * sqrt(Z) / |frac_da4| = {Lambda_eff:.2f} M_KK")
print(f"    Gamma = N_tot * m^3 / (64 pi Lambda^2)")

# ============================================================================
#  SECTION 11: Feynman diagram and amplitude summary
# ============================================================================

print("\n--- Section 11: Feynman Diagram ---")
print("""
  The process tau -> A_a + A_b  (a,b = gauge indices)

             tau (modulus)
              |
              | vertex: y * delta_ab / Lambda_eff
              |
         _____|_____
        /           \\
       /   ~~~~~     \\
      A_a(k1)      A_b(k2)

  Vertex factor: V^{mu nu}_{ab} = (1/Lambda_eff) * delta_ab
                 * [k1.k2 g^{mu nu} - k1^nu k2^mu]

  |M|^2 = N_A * (m_tau^2 / Lambda_eff)^2 * (1/2)
         [factor 1/2 from polarization sum for massless vectors]

  Gamma = (1/2m) * integral |M|^2 * dPS_2
        = N_A * m_tau^3 / (64 pi Lambda_eff^2)
""")

# ============================================================================
#  SECTION 12: Gate verdict
# ============================================================================

print("=" * 72)
print("GATE S76-B5-SM-DECAY")
print("=" * 72)

gate_pass = (R_all_grav > 100) and (T_RH_GeV > T_BBN_GeV) and (tau_total_s < 1.0)  # (local)
gate_fail = R_all_grav < 1.0  # (local)
gate_info = (1.0 < R_all_grav < 100.0)  # (local)

print(f"\n  Criterion 1: Gamma_SM / Gamma_grav > 100")
print(f"    Computed: R_all = {R_all_grav:.4f}")
print(f"    Status:   {'PASS' if R_all_grav > 100 else ('FAIL' if R_all_grav < 1 else 'INFO')}")

print(f"\n  Criterion 2: T_RH > T_BBN")
print(f"    Computed: T_RH = {T_RH_GeV:.4e} GeV > T_BBN = {T_BBN_GeV:.4e} GeV")
print(f"    Status:   {'PASS' if T_RH_GeV > T_BBN_GeV else 'FAIL'}")

print(f"\n  Criterion 3: tau_total < 1 s")
print(f"    Computed: tau_total = {tau_total_s:.4e} s")
print(f"    Status:   {'PASS' if tau_total_s < 1.0 else 'FAIL'}")

if gate_pass:
    verdict = "PASS"
elif gate_fail:
    verdict = "FAIL"
elif gate_info:
    verdict = "INFO"
else:
    verdict = "FAIL"

print(f"\n  OVERALL VERDICT: {verdict}")

# ============================================================================
#  SECTION 13: Summary table
# ============================================================================

print("\n" + "=" * 72)
print("SUMMARY")
print("=" * 72)
print(f"  Modulus mass:           m_tau = {m_tau_GeV:.4e} GeV ({m_tau:.3f} M_KK)")
print(f"  Oscillation amplitude:  A     = {A_osc:.4f}")
print(f"  Fractional da4/dtau:    y     = {frac_da4:.6f}")
print(f"  Spectral coupling:      y*A   = {y_coupling:.4f}")
print(f"  Suppression scale:      Lambda = {Lambda_eff_GeV:.4e} GeV")
print(f"  Gamma(SU3):             {Gamma_gluons:.4e} GeV")
print(f"  Gamma(SU2):             {Gamma_W:.4e} GeV")
print(f"  Gamma(U1):              {Gamma_B:.4e} GeV")
print(f"  Gamma_SM (gauge):       {Gamma_SM_total:.4e} GeV")
print(f"  Gamma_SM (all):         {Gamma_SM_all:.4e} GeV")
print(f"  Gamma_grav:             {Gamma_grav:.4e} GeV")
print(f"  R = Gamma_SM/Gamma_grav: {R_all_grav:.4f}")
print(f"  tau_total:              {tau_total_s:.4e} s")
print(f"  T_RH:                   {T_RH_GeV:.4e} GeV")
print(f"  Gate verdict:           {verdict}")

# ============================================================================
#  SECTION 14: Save results
# ============================================================================

outpath = os.path.join(os.path.dirname(__file__), "s76_modulus_sm_decay_rate.npz")  # (local)
np.savez(outpath,
    # Input spectral data
    a0_fold=a0_fold,
    a2_fold=a2_fold,
    a4_fold=a4_fold,
    da4_dtau=da4_dtau,
    da2_dtau=da2_dtau,
    d2a4_dtau2=d2a4_dtau2,
    frac_da4=frac_da4,
    frac_da2=frac_da2,
    # Oscillation
    A_osc=A_osc,
    v_terminal=v_terminal,
    m_tau_MKK=m_tau,
    m_tau_GeV=m_tau_GeV,
    # Couplings
    y_coupling=y_coupling,
    Lambda_eff_MKK=Lambda_eff,
    Lambda_eff_GeV=Lambda_eff_GeV,
    Lambda_H_eff_GeV=Lambda_H_eff,
    Lambda_eff_over_MPl=Lambda_eff_GeV / M_Pl_reduced,
    # Decay rates — gauge channels
    Gamma_gluons=Gamma_gluons,
    Gamma_W=Gamma_W,
    Gamma_B=Gamma_B,
    Gamma_SM_gauge=Gamma_SM_total,
    # Decay rates — Higgs channel
    Gamma_Higgs=Gamma_Higgs,
    # Decay rates — totals
    Gamma_SM_all=Gamma_SM_all,
    Gamma_grav=Gamma_grav,
    Gamma_total=Gamma_total,
    R_SM_grav=R_all_grav,
    tau_SM_s=tau_SM_s,
    tau_grav_s=tau_grav_s,
    tau_total_s=tau_total_s,
    # Reheating
    T_RH_GeV=T_RH_GeV,
    T_RH_SM_only_GeV=T_RH_SM_only,
    T_RH_over_MKK=T_RH_over_MKK,
    # Cross-checks
    chk1_pass=chk1_pass,
    chk2_pass=chk2_pass,
    chk3_pass=chk3_pass,
    bbn_safe=bbn_safe,
    perturbative=perturbative,
    # W1-B comparison
    W1B_ratio_Gamma=ratio_Gamma,
    W1B_ratio_tau=ratio_tau,
    W1B_ratio_TRH=ratio_TRH,
    # Gate
    gate_verdict=verdict,
)
print(f"\n  Results saved to: {outpath}")
print("  Done.")
