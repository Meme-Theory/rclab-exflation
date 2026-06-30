#!/usr/bin/env python3
"""
S52 — 12D-REDUCTION-52 Analytic Cross-Check
=============================================

Verifies the N_e saturation result and derives the analytic formula.

In the stiff-matter limit (KE >> |V|), the Friedmann-modulus system simplifies:
  H^2 = G_mod_full * tau_dot^2 / (6 * M_p^2)
  tau evolves nearly as free particle: tau(t) ~ tau_i + tau_dot_0 * t
  a(t) ~ a_i * exp(H*t) ~ a_i * (1 + tau_dot_0 * sqrt(G_mod/(6*M_p^2)) * t)

Actually for stiff matter (w=1): a(t) ~ t^{1/3}

The KEY: N_e = integral_0^{t_fold} H(t) dt

In the stiff limit:
  rho(t) = rho_0 * (a_0/a(t))^6  [w=1 => rho ~ a^{-6}]
  H^2 = rho/(3*M_p^2)
  da/dt = H*a => a ~ t^{1/3}
  H = 1/(3*t)
  N_e = integral H dt = (1/3)*ln(t_f/t_i)

The transit time: tau_fold / tau_dot_0 ~ 0.19 / tau_dot_0
The initial time: set by the Hubble rate at start
  H_0 = tau_dot_0 * sqrt(G_mod_full/(6*M_p^2))
  t_i ~ 1/(3*H_0)

For stiff matter: t_f = t_i * (a_f/a_i)^3

But here's the subtle point: tau_dot is NOT constant. The Hubble friction
3*H*tau_dot slows it down, and the potential gradient dV/dtau accelerates it.

In the pure stiff limit (V << K):
  tau_dot ~ tau_dot_0 * (a_0/a)^3  [stiff dilution]
  d(tau)/dt = tau_dot_0 * (a_0/a)^3

  integral d(tau) = tau_fold
  integral tau_dot_0 * (a_0/a)^3 dt = tau_fold

With a = a_0 * (t/t_0)^{1/3} and t_0 = 1/(3*H_0):
  dt = da * 3*t_0 / a_0 * (a/a_0)^2
  integral tau_dot_0 * (a_0/a)^3 * 3*t_0/a_0 * (a/a_0)^2 da
  = 3 * tau_dot_0 * t_0 / a_0 * integral (a_0/a) da
  = 3 * tau_dot_0 * t_0 * ln(a_f/a_0)

Wait, let me redo this more carefully.

For stiff matter (w=1):
  a(t) = a_0 * (t/t_0)^{1/3}
  tau_dot(t) = tau_dot_0 * (a_0/a(t))^3 = tau_dot_0 * (t_0/t)

  tau(t) - tau(0) = integral_t_0^t tau_dot_0 * t_0 / t' dt'
                  = tau_dot_0 * t_0 * ln(t/t_0)

  Setting tau(t_f) - tau(0) = tau_fold:
  tau_fold = tau_dot_0 * t_0 * ln(t_f/t_0)
  ln(t_f/t_0) = tau_fold / (tau_dot_0 * t_0)

  But N_e = (1/3) * ln(t_f/t_0) for a ~ t^{1/3}

  So N_e = tau_fold / (3 * tau_dot_0 * t_0)

  With t_0 = 1/(3*H_0) and H_0 = tau_dot_0 * sqrt(G_mod_full/(6*M_p^2)):
  t_0 = 1/(3 * tau_dot_0 * sqrt(G_mod_full/(6*M_p^2)))

  N_e = tau_fold / (3 * tau_dot_0 * 1/(3*tau_dot_0*sqrt(G_mod_full/(6*M_p^2))))
      = tau_fold * sqrt(G_mod_full/(6*M_p^2))

  THIS IS INDEPENDENT OF tau_dot_0!!!

  N_e = tau_fold * sqrt(G_mod_full / (6 * M_p^2))

This is the structural result. Let's compute it.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
from canonical_constants import (
    tau_fold, G_DeWitt, M_KK_kerner, M_Pl_reduced,
)

M_KK = M_KK_kerner
M_p_sq = (M_Pl_reduced / M_KK)**2
G_mod_full = M_p_sq * G_DeWitt

print("=" * 72)
print("  ANALYTIC CROSS-CHECK: N_e saturation in stiff-matter limit")
print("=" * 72)

# The EXACT stiff-matter result:
# N_e = tau_fold * sqrt(G_mod_full / (6 * M_p^2))
# = tau_fold * sqrt(G_DeWitt / 6)

N_e_analytic = tau_fold * np.sqrt(G_DeWitt / 6.0)
print(f"\n  N_e = tau_fold * sqrt(G_DeWitt / 6)")
print(f"      = {tau_fold} * sqrt({G_DeWitt}/6)")
print(f"      = {tau_fold} * {np.sqrt(G_DeWitt/6.0):.6f}")
print(f"      = {N_e_analytic:.6f}")

print(f"\n  Numerical result: N_e = 0.1734")
print(f"  Analytic result:  N_e = {N_e_analytic:.6f}")
print(f"  Agreement: {abs(N_e_analytic - 0.1734)/0.1734 * 100:.2f}%")

# This is a STRUCTURAL result:
# - N_e does NOT depend on tau_dot_0 in the stiff limit
# - N_e does NOT depend on M_KK or M_Pl individually (only through G_DeWitt)
# - N_e = tau_fold * sqrt(G_DeWitt / 6) = 0.19 * sqrt(5/6) = 0.1734

# For the gate: K_pivot = exp(-N_e)
K_pivot = np.exp(-N_e_analytic)
K_star = 0.087  # (local)
print(f"\n  K_pivot = exp(-N_e) = {K_pivot:.6f}")
print(f"  K* = {K_star}")
print(f"  K_pivot / K* = {K_pivot / K_star:.4f}")

# How many e-folds would we NEED?
# N_e >= 3.1 requires tau_fold * sqrt(G_DeWitt/6) >= 3.1
# tau_fold >= 3.1 / sqrt(5/6) = 3.1 / 0.9129 = 3.395
# That's impossible — tau_fold = 0.19 is FIXED by the van Hove singularity!

tau_fold_needed = 3.1 / np.sqrt(G_DeWitt / 6.0)
print(f"\n  For N_e = 3.1: need tau_fold = {tau_fold_needed:.3f}")
print(f"  Actual tau_fold = {tau_fold}")
print(f"  Shortfall: {tau_fold_needed / tau_fold:.1f}x")

# Alternative: how large would G_DeWitt need to be?
G_needed = 6.0 * (3.1 / tau_fold)**2
print(f"\n  For N_e = 3.1 with tau_fold = 0.19:")
print(f"  Need G_DeWitt = 6*(3.1/0.19)^2 = {G_needed:.1f}")
print(f"  Actual G_DeWitt = {G_DeWitt}")
print(f"  Shortfall: {G_needed / G_DeWitt:.1f}x")

# PHYSICAL INTERPRETATION:
print(f"\n{'='*72}")
print(f"  PHYSICAL INTERPRETATION")
print(f"{'='*72}")
print(f"""
  The e-fold count N_e = tau_fold * sqrt(G_DeWitt/6) is a STRUCTURAL result.

  In the stiff-matter limit (w=1), both the Hubble rate and the modulus
  velocity scale the same way with the initial conditions:
    - Faster tau_dot_0 => higher H => more expansion per unit time
    - BUT faster tau_dot_0 => shorter transit time (tau_fold / tau_dot_0)
    - These two effects EXACTLY CANCEL.

  The result depends ONLY on:
    1. tau_fold = 0.19 (the Jensen parameter at the van Hove singularity)
    2. G_DeWitt = 5.0 (the modulus kinetic coefficient, exact for Jensen)

  N_e = 0.19 * sqrt(5/6) = 0.1734

  This is 17.9x SHORT of the N_e = 3.1 requirement.

  Possible escape routes:
  1. SLOW-ROLL regime (w << 1): requires V_KK gradient to dominate,
     which doesn't happen because Delta_V/V ~ 0.9% over the transit.
  2. Multi-modulus: additional internal degrees of freedom could increase
     the effective G_DeWitt. Would need G_eff ~ 1595.
  3. Non-trivial Lambda_P: a 12D cosmological constant adds a constant
     to V_KK, which can create a plateau and slow-roll phase.
  4. |S|^2 contribution: The second fundamental form might contribute
     additional terms beyond the simple G_mod * tau_dot^2 kinetic term.
  5. Extended modulus range: if the BCS transition occurs at tau > 0.19,
     the additional range could help (but tau_fold is set by the DOS).

  The dominant effect: Delta_V = -0.42 M_KK^4 over 0.19 in tau,
  compared to V_KK(0) = -46.65 M_KK^4. The potential is nearly FLAT
  relative to its depth, giving a stiff equation of state.
""")

# SENSITIVITY ANALYSIS: What if we include the potential correction?
print(f"\n{'='*72}")
print(f"  SENSITIVITY ANALYSIS")
print(f"{'='*72}")

# Beyond pure stiff matter, the potential adds corrections:
# N_e = N_e_stiff * (1 + epsilon)
# where epsilon ~ Delta_V / (KE typical) ~ Delta_V / (G_mod_full * tau_dot_crit^2 / 2)
# This is tiny for tau_dot_0 >> tau_dot_crit but could matter near critical

# Near the critical tau_dot:
# tau_dot_crit^2 = 2 * |V(0)| / G_mod_full = 2 * 46.65 / 116.63 = 0.8
# KE_crit = G_mod_full * tau_dot_crit^2 / 2 = |V(0)| = 46.65
# Delta_V / KE = 0.42 / 46.65 = 0.009 ~ 1%
# So even at the critical velocity, the correction is ~1%.

print(f"  Potential flatness: Delta_V / |V(0)| = {0.4232 / 46.6528 * 100:.2f}%")
print(f"  This confirms: the stiff limit is an excellent approximation")
print(f"  The N_e result is robust to O(1%) corrections from V_KK")

# With 12D cosmological constant Lambda_P:
# V_KK(tau) = -(M_p^2/2) * R_K(tau) + Lambda_P * Vol_K
# If Lambda_P > 0 and Lambda_P * Vol_K > M_p^2 * R_K / 2, then V > 0
# This would give an inflationary phase (w ~ -1)

# For V > 0 at tau=0: Lambda_P > M_p^2 * R_K(0) / (2 * Vol_K) = 23.33 * 2.0 / 1349.74 = 0.0346
V_threshold = M_p_sq * 4.0 / (2.0 * 1349.74)
print(f"\n  12D Lambda_P threshold for V > 0:")
print(f"  Lambda_P > {V_threshold:.4f} M_KK^{10} (with Vol_K = 1349.74)")
print(f"  This would enable a de Sitter (inflationary) phase")
print(f"  But introduces a fine-tuning problem (CC problem in 12D)")

print(f"\n{'='*72}")
print(f"  END OF ANALYTIC CROSS-CHECK")
print(f"{'='*72}")
