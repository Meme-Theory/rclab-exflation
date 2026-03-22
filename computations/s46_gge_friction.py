#!/usr/bin/env python3
"""
s46_gge_friction.py — GGE Caldeira-Leggett Friction on Tau Modulus
===================================================================
Gate: GGE-FRICTION-46 (diagnostic)
Agent: hawking-theorist

Physics: The 8 Richardson-Gaudin modes act as a finite heat bath
providing Caldeira-Leggett dissipative friction on the tau modulus.
The bath spectral density J(omega) determines the friction coefficient.
The cranking inertia (ATDHFB) gives the many-body mass enhancement.

The question: can combined friction + cranking reduce epsilon_H from 3
toward < 0.1, enabling quasi-static n_s?

Caldeira-Leggett (1983): gamma_CL = pi * J(omega_0) / (2 * M * omega_0)
Inglis-Belyaev cranking: M_crank = M_bare + 2 sum |<k|dH/dtau|l>|^2 / (E_k - E_l)^2 * (n_k - n_l)

Input:
  s45_gge_beating.npz  — GGE mode frequencies, couplings
  s44_multi_t_jacobson.npz — mode-resolved thermodynamics, G_kl
  s44_friedmann_bcs_audit.npz — Friedmann dynamics, epsilon_H
  s42_gge_energy.npz — GGE occupations
  s42_gradient_stiffness.npz — Z_fold, dS/dtau at multiple tau
  canonical_constants.py

Output:
  s46_gge_friction.npz
  s46_gge_friction.png
"""

import sys
sys.path.insert(0, "tier0-computation")

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from canonical_constants import (
    H_fold, v_terminal, G_DeWitt, M_ATDHFB, tau_fold,
    omega_PV, omega_att, E_cond, E_B1, E_B2_mean, E_B3_mean,
    S_fold, dS_fold, d2S_fold, Z_fold, dt_transit, m_tau,
    Delta_0_GL, Delta_B3, Gamma_Langer_BCS, xi_BCS,
    PI,
)

# ============================================================
# 1. LOAD DATA
# ============================================================
d_beat = np.load("tier0-computation/s45_gge_beating.npz", allow_pickle=True)
d_tj = np.load("tier0-computation/s44_multi_t_jacobson.npz", allow_pickle=True)
d_fried = np.load("tier0-computation/s44_friedmann_bcs_audit.npz", allow_pickle=True)
d_gge = np.load("tier0-computation/s42_gge_energy.npz", allow_pickle=True)
d_grad = np.load("tier0-computation/s42_gradient_stiffness.npz", allow_pickle=True)

labels = d_beat["labels"]
E_k = d_beat["E_k"]          # 8 mode energies at fold (M_KK)
n_k = d_tj["n_k"]            # GGE occupation numbers
lambda_k = d_beat["lambda_k"] # GGE Lagrange multipliers
u_k = d_beat["u_k"]          # BCS u coherence factors
v_k = d_beat["v_k"]          # BCS v coherence factors
Delta_k = d_beat["Delta_k"]  # BCS gaps per mode

omega_beats = d_beat["omega_beats"]  # [B2-B1, B2-B3, B1-B3]
omega_kl = d_beat["omega_kl"]        # 8x8 frequency matrix

# Friedmann dynamics
epsilon_H = float(d_fried["epsilon_H_S43"])
vel_reduction_needed = float(d_fried["velocity_reduction_needed"])

print("=" * 72)
print("GGE-FRICTION-46: Caldeira-Leggett Friction on Tau Modulus")
print("=" * 72)

# ============================================================
# 2. COUPLING CONSTANTS g_k = dE_k / dtau
# ============================================================
# The BCS quasiparticle energies are E_qp_k = sqrt(epsilon_k^2 + Delta_k^2)
# where epsilon_k = E_k (single-particle energies from Dirac spectrum).
#
# The coupling of mode k to the modulus is:
#   g_k = dE_qp_k / dtau = (epsilon_k / E_qp_k) * (d epsilon_k / dtau)
#                         + (Delta_k / E_qp_k) * (d Delta_k / dtau)
#
# For the leading-order estimate, use d epsilon_k / dtau from finite differences
# on the gradient stiffness tau grid. The Delta_k dependence on tau is through
# the self-consistent gap equation, which is secondary.
#
# From the gradient stiffness data, we can extract the TOTAL dS/dtau.
# The per-mode coupling is estimated from the spectral action structure:
# dE_k/dtau ~ E_k * (d ln E_k / dtau)
#
# The Jensen deformation affects the metric as:
#   g_{root} = g_0 * e^{-2*tau}   (root directions)
#   g_{Cartan} = g_0               (Cartan directions)
#
# For the BCS-active modes (low-lying spectrum):
# B2 modes: (1,1) representation, coupled to root directions
# B1 mode: (1,0) representation
# B3 modes: (0,3)/(3,0) representation
#
# The Dirac eigenvalue dependence on tau can be estimated from the
# known spectral structure. At the fold, the mode velocities are:
#   v_k = dE_k/dtau

# Method 1: From the spectral action gradient stiffness data
# The tau grid spans [0.05, 0.30] with 10 points
tau_grid = d_grad["tau_grid"]
S_total_arr = d_grad["S_total"]
dS_dtau_arr = d_grad["dS_dtau"]

# The spectral action is S = sum_k f(E_k^2/Lambda^2)
# So dS/dtau = sum_k f' * 2*E_k * dE_k/dtau / Lambda^2
# This is the TOTAL gradient, distributed across all 992 modes

# For the 8 BCS-active modes, the coupling to the modulus is through
# their position in the spectrum. The key insight: at the van Hove
# singularity (fold), the B2 modes have dE_B2/dtau = 0 (by definition
# of the singularity). The B1 and B3 modes have nonzero velocities.

# From the known spectrum structure:
# E_k(tau) for B2 is quadratic near the fold: E_B2(tau) ~ E_B2_0 + a*(tau - tau_fold)^2
# So dE_B2/dtau = 0 at the fold (van Hove singularity)
# This is the DEFINING property of the fold

# For B1: dE_B1/dtau is nonzero (B1 is not at a van Hove point)
# For B3: dE_B3/dtau is nonzero

# Numerical estimate from finite differences on the known eigenvalues
# We use the S42 data: eigenvalue spectrum at multiple tau values

# Method 2: Analytic estimate from Jensen metric structure
# The metric deformation exp(-2*tau) affects root directions.
# For rep (p,q), eigenvalues scale as:
#   E_{(p,q)}(tau) ~ sqrt(C_2(p,q)) * g(tau)
# where g(tau) depends on the representation and the Jensen deformation.
#
# For the (1,1) adjoint = B2 sector:
# The Casimir is C_2(1,1) = 3. The eigenvalue at the fold is ~0.845 M_KK.
# The van Hove singularity means dE/dtau = 0 for B2.
#
# For B1 = (1,0): C_2(1,0) = 4/3
# For B3 = (3,0)/(0,3): C_2(3,0) = 6

# Use finite differences from the 992-mode spectrum at different tau
# The gradient stiffness gives us dS/dtau at each tau point.
# For per-mode gradients, we need the actual eigenvalue tau-derivatives.

# Estimate dE_k/dtau from the metric structure:
# The Jensen deformation is g_ab(tau) = diag(e^{-2tau}, e^{-2tau}, e^{-2tau}, 1, 1, e^{-2tau}, e^{-2tau}, e^{-2tau})
# (root directions get e^{-2tau}, Cartan directions unchanged)
# The Dirac eigenvalue squared is proportional to the Casimir computed
# with THIS metric. So:
#   E_k^2(tau) = sum_a g^{ab}(tau) * [generator contribution]_ab
#
# At the van Hove fold, the B2 BAND has dE/dtau = 0.
# But individual B2 modes within the band may still have nonzero
# coupling to tau through the gap structure.
#
# For the BdG quasiparticle spectrum:
#   E_qp_k(tau) = sqrt((E_k(tau) - mu)^2 + Delta_k(tau)^2)
# with mu = 0 (particle-hole symmetric).
#
# dE_qp_k/dtau = [E_k * dE_k/dtau + Delta_k * dDelta_k/dtau] / E_qp_k

# KEY RESULT from S40: M_ATDHFB = 1.695
# The ATDHFB mass was computed from the FULL spectrum:
#   M_ATDHFB = sum_{k,l} |<k|dD_K/dtau|l>|^2 / (E_k - E_l)^2
# This is already the cranking inertia from the SINGLE-PARTICLE spectrum.

# The BCS MANY-BODY cranking inertia adds the pairing contribution:
#   M_crank = M_ATDHFB + M_pairing
# where M_pairing = 2 * sum_{k} |dDelta_k/dtau|^2 / (2*E_qp_k)^2 * (u_k^2 - v_k^2)

# For the coupling constants, use the G_kl matrix from s44_multi_t_jacobson
# G_kl = d^2 ln Z / (d beta_k d beta_l) is the enthalpy correlator
# The diagonal G_kk = variance of mode k energy

G_kl = d_tj["G_kl"]

print("\n--- Mode Properties at Fold ---")
print(f"{'Mode':<8} {'E_k':>8} {'n_k':>8} {'Delta_k':>8} {'lambda_k':>8} {'G_kk':>8}")
for i in range(8):
    print(f"{labels[i]:<8} {E_k[i]:8.5f} {n_k[i]:8.5f} {Delta_k[i]:8.5f} "
          f"{lambda_k[i]:8.4f} {G_kl[i,i]:8.5f}")

# ============================================================
# 3. BATH SPECTRAL DENSITY J(omega)
# ============================================================
# The coupling of the GGE modes to the modulus is through
# g_k = dE_qp_k / dtau. At the van Hove fold:
#
# For B2 modes: dE_B2/dtau = 0 (van Hove singularity)
# But Delta_B2(tau) varies, so dE_qp_B2/dtau ~ Delta_B2/E_qp * dDelta/dtau
# For B1: dE_B1/dtau nonzero
# For B3: dE_B3/dtau nonzero
#
# Estimate the couplings from the gradient stiffness:
# The total spectral gradient at the fold is dS/dtau = 58,673.
# With 992 modes, the average per-mode gradient is ~59.
# But the BCS-active modes are at the BOTTOM of the spectrum,
# and their contribution is weighted by 1/E_k^2 (heat kernel).

# Compute dE_k/dtau from finite differences of the eigenvalue spectrum
# Using the Jensen metric structure for the low-lying modes:

# The key quantity is the ADIABATIC VELOCITY of each mode.
# From the spectral action Hessian (S42 gradient stiffness):
# Z_fold = sum_k (dE_k/dtau)^2 * f''(E_k^2) * 4*E_k^2 + ...
# Z_fold = 74,731. This is the total spectral stiffness.

# For the 8 BCS modes, their contribution to Z is:
# Z_BCS = sum_{k in BCS} (dE_k/dtau)^2 * w_k
# where w_k is the spectral weight.

# From the spectral structure, the low-lying modes (E ~ 0.8-1.0 M_KK)
# contribute proportionally less to Z (which is dominated by the bulk).

# DIRECT ESTIMATE of g_k:
# Use the fact that at the fold, B2 has v_group = 0.
# The spectral action S(tau) = sum_k f(E_k(tau)^2).
# Near the fold, for B2: E_B2(tau) = E_B2_fold + (1/2) E_B2'' * (tau - tau_fold)^2
#
# From the van Hove singularity:
# rho_B2 = 14.02 per mode (S37)
# This means dE_B2/dtau = 0 and d^2E_B2/dtau^2 ~ 1/(2*rho_B2) ~ 0.036 M_KK
#
# For B1 and B3, estimate dE/dtau from the band dispersion:
# E_B1(tau) varies linearly near the fold, with slope from the
# band structure. Using the gradient stiffness data:

# Method: From Z_fold and dS_fold, extract per-mode contributions
# The ratio Z_fold / N_modes = 74731 / 992 = 75.3 per mode average
# But the BCS modes are special (van Hove).

# For a RIGOROUS per-mode coupling, compute from the metric:
# d/dtau(g_root) = -2 * exp(-2*tau) = -2 * g_root
# At the fold (tau = 0.19):
# g_root(0.19) = exp(-0.38) = 0.684
# dg_root/dtau = -2 * 0.684 = -1.368

# The Dirac eigenvalue for rep (p,q) is:
# lambda_{(p,q)} = sqrt(sum_a (m_a + 1/2)^2 * g^{aa})
# where m_a are angular momentum quantum numbers and g^{aa} = 1/g_{aa}

# For the LOWEST modes in each sector:
# B2 = (1,1): 6 root directions, 2 Cartan
# B1 = (1,0): 4 root directions, 2 Cartan
# B3 = (3,0): 6 root directions, 2 Cartan

# The van Hove singularity for B2 is a BAND effect:
# multiple B2 modes converge at the fold, creating the divergent DOS.
# Individual B2 modes DO have tau-velocity through the Delta dependence.

# PHYSICALLY MOTIVATED ESTIMATE:
# g_k^2 = (dE_qp_k / dtau)^2
# For B2: dE_B2/dtau ~ 0 (van Hove), but dDelta_B2/dtau ~ Delta_B2 * d(ln Delta)/dtau
# For B1: dE_B1/dtau ~ 2 * E_B1 (from metric scaling)
# For B3: dE_B3/dtau ~ 2 * E_B3 (from metric scaling)
#
# Correction: the metric scaling d(ln g)/dtau = -2 gives dE/dtau ~ -E.
# But this is for the BARE eigenvalue. The BCS quasiparticle has:
# E_qp = sqrt(E_k^2 + Delta_k^2)
# dE_qp/dtau = (E_k * dE_k/dtau + Delta_k * dDelta_k/dtau) / E_qp

# For a more careful estimate, use the ATDHFB mass decomposition.
# M_ATDHFB = sum_k (dE_k/dtau)^2 / E_k^2 * weight_k
# With M_ATDHFB = 1.695 and sum over 992 modes, the per-mode average is 1.7e-3.
# The BCS-active modes are 8/992 = 0.8% of the spectrum.

# Two routes for the coupling:
# Route A: From the metric deformation (analytic)
# Route B: From the ATDHFB mass decomposition (data-driven)

# Route A: Analytic per-mode couplings
# For B2 modes at the van Hove fold:
# dE_B2/dtau = 0 (by definition)
# d^2E_B2/dtau^2 = 1/(rho_B2) where rho_B2 = 14.02 per mode
# So near the fold: dE_B2/dtau(tau) ~ (tau - tau_fold) / rho_B2

# For B1:
# E_B1(tau) changes with the metric. From the (1,0) representation:
# The eigenvalue goes as E ~ sqrt(C_2_eff(tau))
# dE_B1/dtau ~ -E_B1 (from root metric derivative, corrected for Cartan)
# More precisely: about 4/8 = 50% of directions are roots for (1,0) in SU(3),
# so dE_B1/dtau ~ -E_B1 * (root fraction) * 2

# For B3 = (3,0)/(0,3):
# Similar: dE_B3/dtau ~ -E_B3 * (root fraction) * 2

# Root fractions from the SU(3) structure:
# dim(SU(3)) = 8 = 6 roots + 2 Cartan
# root_frac = 6/8 = 3/4

root_frac = 6.0 / 8.0  # fraction of generators that are root directions

# For B2 at the fold: dE_B2/dtau = 0 (van Hove)
# The coupling comes ONLY from the gap derivative
# dDelta_B2/dtau is estimated from the BCS gap equation structure
# Delta(tau) = g * sum_k Delta_k / (2*E_qp_k) * tanh(beta*E_qp_k/2)
# At the fold, this is a self-consistent equation. The tau-derivative
# enters through the DOS: dDelta/dtau ~ Delta * d(ln rho) / dtau
# At the van Hove fold, d(ln rho)/dtau diverges (!) -- this is the
# van Hove singularity in the gap equation.
# However, the INTEGRATED coupling (over the BCS window) is finite.

# Conservative estimate for dDelta_B2/dtau:
# From the BCS gap equation structure, dDelta/dtau ~ Delta * d(ln N(E_F))/dtau
# where N(E_F) is the DOS at the Fermi level.
# N(E_F) ~ rho_B2 ~ 14 per mode at the fold.
# d(rho_B2)/dtau ~ d^2E/dtau^2 * rho_B2^2 ~ rho_B2 / (tau scale)
# With the fold width delta_tau ~ 0.01 (from S35),
# d(ln rho)/dtau ~ 1 / delta_tau ~ 100

# But this overestimates because the singularity is integrable.
# Use the SELF-CONSISTENT result from the gap equation:
# At the fold, Delta ~ Delta_0 * exp(-1/(g*N(E_F)))
# d(ln Delta)/dtau = (1/(g*N^2)) * dN/dtau
# This is FINITE even at the van Hove fold.

# For a robust estimate, use the ATDHFB decomposition:
# M_ATDHFB = 1.695 comes from the FULL spectrum.
# The BCS modes contribute:
# M_BCS ~ M_ATDHFB * (BCS contribution fraction)
# From S40 (M-COLL-40): B1 dominates 71% of cranking mass
# So M_B1 ~ 0.71 * 1.695 ~ 1.20
# And g_B1^2 / E_B1^2 ~ M_B1 => g_B1 ~ E_B1 * sqrt(M_B1) ~ 0.819 * 1.10 ~ 0.90

# From S40: M_ATDHFB = 1.695, B1 dominates 71%
B1_frac_cranking = 0.71  # from M-COLL-40

print("\n--- Coupling Constants (Route A: Metric + ATDHFB) ---")

# Route A couplings:
# B2: dE/dtau = 0 at fold, residual coupling from gap derivative
# Use the gap equation: dDelta_B2/dtau via the BCS self-consistency
# dDelta/dtau ~ Delta * (d ln rho / dtau)_BCS_window

# The BCS window has width ~2*Delta_0 = 1.54 around E_F.
# Within this window, the DOS variation is smooth even at the fold.
# dDelta_B2/dtau ~ Delta_B2 * 2 * root_frac (from metric scaling)
# But this is the INDIRECT coupling through the gap, not the direct eigenvalue.
# The B2 eigenvalue is FLAT, so the gap coupling is the only channel.

# For the quasiparticle energy:
# E_qp_B2 = sqrt(E_B2^2 + Delta_B2^2)
E_qp_B2 = np.sqrt(E_B2_mean**2 + Delta_k[0]**2)
E_qp_B1 = np.sqrt(E_B1**2 + Delta_k[4]**2)
E_qp_B3 = np.sqrt(E_B3_mean**2 + Delta_k[5]**2)

print(f"E_qp_B2 = {E_qp_B2:.5f} M_KK")
print(f"E_qp_B1 = {E_qp_B1:.5f} M_KK")
print(f"E_qp_B3 = {E_qp_B3:.5f} M_KK")

# Direct eigenvalue velocity from metric:
# dE_k/dtau ~ -2 * root_frac * E_k (for non-van-Hove modes)
# Correction: the eigenvalue depends on sqrt(sum g^{aa} * m_a^2),
# and d/dtau(g^{aa}_root) = +2*g^{aa}_root (inverse metric goes UP).
# So dE/dtau > 0 for modes that are primarily in root directions.
# The sign doesn't matter for |g_k|^2.

dE_dtau_B2 = 0.0  # VAN HOVE: zero by definition
dE_dtau_B1 = 2.0 * root_frac * E_B1  # metric scaling
dE_dtau_B3 = 2.0 * root_frac * E_B3_mean  # metric scaling

# Gap derivatives: estimate from BCS gap equation
# dDelta/dtau ~ Delta * d(ln g*N(E_F))/dtau
# where g is the pairing coupling and N(E_F) is the DOS
# At the fold: g is tau-independent (contact interaction),
# so dDelta/dtau ~ Delta * d(ln N(E_F))/dtau
# For B2: N(E_F) diverges at fold, so d(ln N)/dtau ~ 1/(tau - tau_fold)
# This divergence is INTEGRABLE in the gap equation.
# Use the regularized estimate: dDelta_B2/dtau ~ Delta_B2 / delta_tau_BCS
# where delta_tau_BCS ~ xi_BCS * dE/dtau ~ xi_BCS * (small) ~ small
# Since B2 is at the van Hove fold, the gap is most sensitive to tau changes.
# Conservative estimate: |dDelta_B2/dtau| ~ Delta_B2 * omega_att
# (the attractor frequency sets the scale of gap oscillations)
dDelta_dtau_B2 = Delta_k[0] * omega_att  # ~ 0.43 * 1.43 = 0.61
dDelta_dtau_B1 = Delta_k[4] * omega_att * 0.1  # B1 gap is less sensitive
dDelta_dtau_B3 = Delta_k[5] * omega_att * 0.1  # B3 gap is less sensitive

# Full quasiparticle coupling:
# g_k = |dE_qp_k/dtau| = |(E_k * dE_k/dtau + Delta_k * dDelta_k/dtau) / E_qp_k|
g_B2 = np.abs(E_B2_mean * dE_dtau_B2 + Delta_k[0] * dDelta_dtau_B2) / E_qp_B2
g_B1 = np.abs(E_B1 * dE_dtau_B1 + Delta_k[4] * dDelta_dtau_B1) / E_qp_B1
g_B3 = np.abs(E_B3_mean * dE_dtau_B3 + Delta_k[5] * dDelta_dtau_B3) / E_qp_B3

# Route B: Cross-check from ATDHFB mass
# M_ATDHFB = sum_k g_k^2 / (2*E_qp_k)^2 (Inglis formula, simplified)
# With B1 = 71%:
g_B1_from_ATDHFB = np.sqrt(B1_frac_cranking * M_ATDHFB * (2 * E_qp_B1)**2)

print(f"\nRoute A couplings:")
print(f"  g_B2 = {g_B2:.5f} M_KK  (van Hove: gap-only coupling)")
print(f"  g_B1 = {g_B1:.5f} M_KK  (metric + gap)")
print(f"  g_B3 = {g_B3:.5f} M_KK  (metric + gap)")
print(f"\nRoute B cross-check (ATDHFB):")
print(f"  g_B1_ATDHFB = {g_B1_from_ATDHFB:.5f} M_KK")

# Use Route A values (more conservative for B2)
g_k_arr = np.zeros(8)
g_k_arr[0:4] = g_B2  # 4 B2 modes
g_k_arr[4] = g_B1     # 1 B1 mode
g_k_arr[5:8] = g_B3   # 3 B3 modes

print(f"\n{'Mode':<8} {'g_k':>10} {'g_k^2':>12} {'omega_k':>10}")
# Assign frequencies: within-sector modes are degenerate
# Use beat frequencies for inter-sector splitting
omega_mode = np.zeros(8)
# B2 modes: internal frequencies ~ 0 (degenerate at fold)
# The relevant frequencies are the BdG quasiparticle energies
# In the GGE, the mode frequencies are the BEAT frequencies
# omega_k = 2 * E_qp_k (BdG excitation energy)
omega_mode[0:4] = 2 * E_qp_B2  # B2 quasiparticle pair energy
omega_mode[4] = 2 * E_qp_B1    # B1 quasiparticle pair energy
omega_mode[5:8] = 2 * E_qp_B3  # B3 quasiparticle pair energy

for i in range(8):
    print(f"{labels[i]:<8} {g_k_arr[i]:10.5f} {g_k_arr[i]**2:12.6f} {omega_mode[i]:10.5f}")

# ============================================================
# 4. SPECTRAL DENSITY J(omega)
# ============================================================
# J(omega) = sum_k |g_k|^2 * delta(omega - omega_k)
# Broaden delta to Lorentzian with width Gamma_k

# Natural linewidth from instanton dynamics
# Gamma ~ Gamma_Langer = 0.250 M_KK (Langer decay rate)
Gamma_mode = Gamma_Langer_BCS  # same for all modes (conservative)

omega_arr = np.linspace(0, 4.0, 2000)  # frequency grid in M_KK

def lorentzian(omega, omega_0, Gamma):
    """Normalized Lorentzian: integral = 1"""
    return (Gamma / PI) / ((omega - omega_0)**2 + Gamma**2)

J_omega = np.zeros_like(omega_arr)
for i in range(8):
    J_omega += g_k_arr[i]**2 * lorentzian(omega_arr, omega_mode[i], Gamma_mode)

print("\n--- Spectral Density J(omega) ---")
print(f"Peak J(omega) = {np.max(J_omega):.6f} M_KK")
print(f"At omega = {omega_arr[np.argmax(J_omega)]:.4f} M_KK")
print(f"Total integral = {np.trapezoid(J_omega, omega_arr):.6f} M_KK^2")
print(f"Sum |g_k|^2 = {np.sum(g_k_arr**2):.6f} M_KK^2 (should match integral)")

# ============================================================
# 5. CLASSIFY: Ohmic vs Super-Ohmic
# ============================================================
# With 8 discrete modes, J(omega) is a sum of 3 broadened lines:
# B2 at omega ~ 1.90, B1 at omega ~ 1.67, B3 at omega ~ 1.96
# This is NOT Ohmic (J ~ omega) -- it's a structured bath.

# Fit the envelope to J(omega) ~ omega^s
# Only meaningful for omega < max(omega_k)
mask = (omega_arr > 0.1) & (omega_arr < 3.0)
# Log-log fit
valid = J_omega[mask] > 1e-15
if np.sum(valid) > 10:
    log_om = np.log(omega_arr[mask][valid])
    log_J = np.log(J_omega[mask][valid])
    # Fit s from J ~ omega^s (linear in log-log)
    from numpy.polynomial import polynomial as P
    coeffs = np.polyfit(log_om, log_J, 1)
    s_bath = coeffs[0]
else:
    s_bath = np.nan

print(f"\nBath classification:")
print(f"  Effective exponent s = {s_bath:.2f}")
if s_bath < 0.5:
    print(f"  Classification: SUB-OHMIC (s < 1)")
elif s_bath < 1.5:
    print(f"  Classification: OHMIC (s ~ 1)")
else:
    print(f"  Classification: SUPER-OHMIC (s > 1)")
print(f"  Note: With 8 modes, the bath is STRUCTURED, not continuous.")
print(f"  Ohmic classification is approximate.")

# ============================================================
# 6. CALDEIRA-LEGGETT FRICTION COEFFICIENT
# ============================================================
# gamma_CL = pi * J(omega_0) / (2 * M * omega_0)
# where omega_0 is the characteristic frequency of the modulus motion
# and M is the effective mass.

# The modulus frequency: omega_tau = m_tau = 2.062 M_KK (mass of tau excitation)
# Alternatively: omega_tau = v_terminal / delta_tau where delta_tau
# is the width of the transit region.
# Using the transit time: omega_transit = 2*pi / dt_transit

omega_tau = m_tau  # modulus mass as characteristic frequency
omega_transit = 2 * PI / dt_transit  # transit frequency

# Evaluate J at the modulus frequency
J_at_omega_tau = np.interp(omega_tau, omega_arr, J_omega)
J_at_omega_transit = np.interp(min(omega_transit, omega_arr[-1]), omega_arr, J_omega)

# Also evaluate at the beat frequencies (which are where the bath IS)
J_at_B2B1_beat = np.interp(omega_beats[0], omega_arr, J_omega)
J_at_B2B3_beat = np.interp(omega_beats[1], omega_arr, J_omega)
J_at_B1B3_beat = np.interp(omega_beats[2], omega_arr, J_omega)

print(f"\n--- J(omega) at key frequencies ---")
print(f"  J(omega_tau = {omega_tau:.3f}) = {J_at_omega_tau:.6e} M_KK")
print(f"  J(omega_transit = {omega_transit:.1f}) = {J_at_omega_transit:.6e} M_KK")
print(f"  J(omega_B2B1 = {omega_beats[0]:.3f}) = {J_at_B2B1_beat:.6e} M_KK")
print(f"  J(omega_B2B3 = {omega_beats[1]:.3f}) = {J_at_B2B3_beat:.6e} M_KK")

# Caldeira-Leggett friction coefficient
# Using the modulus mass as the frequency:
M_eff = G_DeWitt  # bare modulus mass
gamma_CL_tau = PI * J_at_omega_tau / (2 * M_eff * omega_tau)

print(f"\n--- Caldeira-Leggett Friction ---")
print(f"  M_eff = G_DeWitt = {M_eff:.1f}")
print(f"  omega_0 = m_tau = {omega_tau:.3f} M_KK")
print(f"  J(omega_0) = {J_at_omega_tau:.6e} M_KK")
print(f"  gamma_CL = {gamma_CL_tau:.6e} M_KK")

# Compare to Hubble friction
gamma_H = 3 * H_fold / (2 * G_DeWitt)
ratio_CL_H = gamma_CL_tau / gamma_H

print(f"\n  gamma_H (Hubble) = {gamma_H:.4f} M_KK")
print(f"  gamma_CL / gamma_H = {ratio_CL_H:.6e}")

# ============================================================
# 7. CRANKING INERTIA
# ============================================================
# The Inglis-Belyaev cranking formula:
# M_crank = M_bare + 2 * sum_{k,l} |<k|dH/dtau|l>|^2 / (E_k - E_l)^2 * (n_k - n_l)
#
# From S40: M_ATDHFB = 1.695 (already computed from full spectrum)
# This is the SINGLE-PARTICLE cranking mass.
#
# The MANY-BODY (BCS) cranking mass adds pairing correlations:
# M_BCS_crank = M_ATDHFB + M_pair
# where M_pair = 2 * sum_k |dDelta_k/dtau|^2 / (2*E_qp_k)^3
# (Belyaev-Zelevinsky formula for superfluid)
#
# With the BCS coherence factors:
# M_pair = sum_k (u_k^2 - v_k^2)^2 * |g_k|^2 / (2*E_qp_k)^3 * Delta_k^2 / E_qp_k^2

print("\n--- Cranking Inertia ---")
print(f"  M_ATDHFB (single-particle) = {M_ATDHFB:.4f}")
print(f"  G_DeWitt (bare) = {G_DeWitt:.4f}")

# Pairing contribution to cranking mass
# For the 8 BCS modes:
M_pair = 0.0
for i in range(8):
    E_qp_i = np.sqrt(E_k[i]**2 + Delta_k[i]**2)
    uv_diff = u_k[i]**2 - v_k[i]**2
    if E_qp_i > 0:
        M_pair_i = uv_diff**2 * g_k_arr[i]**2 * Delta_k[i]**2 / (2 * E_qp_i)**3
        M_pair += M_pair_i

print(f"  M_pair (BCS enhancement) = {M_pair:.6f}")

# Total cranking mass
M_crank = M_ATDHFB + M_pair
print(f"  M_crank (total) = {M_crank:.4f}")
print(f"  Enhancement M_crank / G_DeWitt = {M_crank / G_DeWitt:.4f}")

# The effective mass including cranking affects epsilon_H:
# epsilon_H = (3/2) * M_eff * v^2 / rho
# If M_eff increases, epsilon_H INCREASES (goes wrong direction for n_s)
# UNLESS the velocity decreases more.

# ============================================================
# 8. DAMPED EQUATION OF MOTION
# ============================================================
# M_eff * ddot(tau) + (gamma_H + gamma_CL) * dot(tau) + dV/dtau = 0
#
# The spectral action gradient provides dV/dtau = dS_fold = 58,673
# (this drives the transit).
#
# In the terminal velocity regime: ddot(tau) ~ 0, so
# v_term = -dV/dtau / gamma_total
# With additional CL friction:
# v_new = -dV/dtau / (gamma_H + gamma_CL)
# v_new / v_term = gamma_H / (gamma_H + gamma_CL)

gamma_total = gamma_H + gamma_CL_tau
v_ratio = gamma_H / gamma_total

print(f"\n--- Velocity Reduction ---")
print(f"  gamma_H = {gamma_H:.4f} M_KK")
print(f"  gamma_CL = {gamma_CL_tau:.6e} M_KK")
print(f"  gamma_total = {gamma_total:.4f} M_KK")
print(f"  v(tau*) / v_terminal = {v_ratio:.10f}")
print(f"  Velocity reduction factor = {1.0/v_ratio:.10f}")

# ============================================================
# 9. SOLVE FULL EQUATION OF MOTION
# ============================================================
# Numerical integration of the damped modulus equation
# Including BOTH Hubble friction and CL friction

from scipy.integrate import solve_ivp

# The potential gradient at fold
dV_dtau = dS_fold  # spectral action gradient (drives transit)

# Equation: M * ddot(tau) + gamma * dot(tau) + dV/dtau = 0
# As first order system:
# dy/dt = [v, -(gamma/M)*v - (dV/dtau)/M]
def modulus_eom(t, y, M, gamma, dVdtau):
    tau, v = y
    dvdt = -(gamma / M) * v - dVdtau / M
    return [v, dvdt]

# Solve with bare mass
t_span = [0, 5 * dt_transit]
t_eval = np.linspace(0, 5 * dt_transit, 5000)
y0 = [tau_fold, v_terminal]

# Case 1: Hubble friction only
sol_H = solve_ivp(modulus_eom, t_span, y0, t_eval=t_eval,
                  args=(G_DeWitt, gamma_H, dV_dtau), rtol=1e-12, atol=1e-15)

# Case 2: Hubble + CL friction
sol_CL = solve_ivp(modulus_eom, t_span, y0, t_eval=t_eval,
                   args=(G_DeWitt, gamma_total, dV_dtau), rtol=1e-12, atol=1e-15)

# Case 3: Hubble + CL + cranking mass
sol_crank = solve_ivp(modulus_eom, t_span, y0, t_eval=t_eval,
                      args=(M_crank, gamma_total, dV_dtau), rtol=1e-12, atol=1e-15)

print(f"\n--- Numerical Integration Results ---")
print(f"  t_span = [0, {5*dt_transit:.6f}] M_KK^{{-1}}")
for label, sol, M_used in [("Hubble only", sol_H, G_DeWitt),
                             ("Hubble+CL", sol_CL, G_DeWitt),
                             ("Hubble+CL+crank", sol_crank, M_crank)]:
    v_final = sol.y[1, -1]
    v_mid = sol.y[1, len(sol.t)//2]
    print(f"  {label}: v_final = {v_final:.4f}, v_mid = {v_mid:.4f}, "
          f"v_mid/v_0 = {v_mid/v_terminal:.6f}")

# ============================================================
# 10. THE 829x TEST
# ============================================================
# S45: need 829x velocity reduction for n_s = 0.965
# eps_H ~ v^2, so need v_reduction = sqrt(829) for eps reduction of 829x
# Actually: need eps_H to go from 3.0 to 0.0176 (= 1 - n_s)
# Ratio: 3.0 / 0.0176 = 170.5 in eps_H
# Since eps_H ~ v^2: need v_reduction = sqrt(170.5) = 13.1x
# Or: eps_H = (3/2) * M * v^2 / rho. If we want eps_H = 0.0176:
# v_target = v_terminal * sqrt(0.0176 / 3.0) = v_terminal * 0.0766

eps_H_target = 0.0176
v_reduction_for_ns = np.sqrt(eps_H_target / epsilon_H)
v_target = v_terminal * v_reduction_for_ns

# Maximum possible CL friction with 8 modes
# Even if ALL spectral density were concentrated at omega_tau,
# J_max = sum |g_k|^2 = total coupling
g_sq_total = np.sum(g_k_arr**2)
gamma_CL_max = PI * g_sq_total / (2 * M_eff * omega_tau)

# With cranking mass enhancement
gamma_CL_max_crank = PI * g_sq_total / (2 * M_crank * omega_tau)

# Maximum velocity reduction
v_ratio_max = gamma_H / (gamma_H + gamma_CL_max)

print(f"\n--- The 829x Test ---")
print(f"  epsilon_H (current) = {epsilon_H:.4f}")
print(f"  epsilon_H (target for n_s=0.965) = {eps_H_target:.4f}")
print(f"  Velocity reduction needed = {v_reduction_for_ns:.6f} (factor {1/v_reduction_for_ns:.1f}x)")
print(f"  v_target = {v_target:.6f} M_KK (vs v_terminal = {v_terminal:.4f})")
print(f"")
print(f"  Sum |g_k|^2 (total bath coupling) = {g_sq_total:.6f} M_KK^2")
print(f"  gamma_CL_max (all J at omega_tau) = {gamma_CL_max:.6e} M_KK")
print(f"  gamma_H = {gamma_H:.4f} M_KK")
print(f"  gamma_CL_max / gamma_H = {gamma_CL_max / gamma_H:.6e}")
print(f"  Maximum velocity reduction factor = {1/v_ratio_max:.6f}")
print(f"")
print(f"  Shortfall: {v_reduction_for_ns / (1 - v_ratio_max):.1f}x")
print(f"  (factor by which CL friction falls short of the target)")

# ============================================================
# 11. STRUCTURAL ANALYSIS
# ============================================================
print("\n" + "=" * 72)
print("STRUCTURAL ANALYSIS")
print("=" * 72)

# The fundamental issue: N_bath = 8 modes vs N_system = 992 modes
# The bath is MICROSCOPICALLY FINITE
# In Caldeira-Leggett, friction requires N -> infinity (continuous bath)
# With 8 modes, the friction is bounded by the total coupling strength

# Thermal friction bound: gamma_CL <= sum |g_k|^2 / (k_B T)
# where T is the bath temperature (GGE temperatures)
T_k = d_tj["T_k"]
T_avg = np.mean(T_k)
gamma_thermal = np.sum(g_k_arr**2) / T_avg

print(f"\n  Finite bath analysis:")
print(f"  N_bath = 8 (Richardson-Gaudin modes)")
print(f"  N_system = 992 (total Dirac modes)")
print(f"  Bath fraction = {8/992:.4f}")
print(f"")
print(f"  Average GGE temperature = {T_avg:.4f} M_KK")
print(f"  Thermal friction bound = {gamma_thermal:.6f} M_KK")
print(f"  gamma_H = {gamma_H:.4f} M_KK")
print(f"  Thermal bound / gamma_H = {gamma_thermal / gamma_H:.6e}")

# The 829x (or more precisely, the ~13x velocity reduction) is impossible:
# gamma_CL / gamma_H ~ 10^{-5} at best
# Need gamma_CL / gamma_H ~ 13 for the velocity reduction
# Shortfall: ~10^6

shortfall_total = (1.0 / v_reduction_for_ns) / (gamma_CL_max / gamma_H)
print(f"\n  CONCLUSION:")
print(f"  gamma_CL_max / gamma_H = {gamma_CL_max / gamma_H:.6e}")
print(f"  Needed gamma_CL / gamma_H > {1.0/v_reduction_for_ns - 1:.1f}")
print(f"  Shortfall = {shortfall_total:.1e}x")
print(f"  8 modes CANNOT provide sufficient friction to reduce epsilon_H.")
print(f"  The GGE bath is 8/992 of the spectrum — too small by {shortfall_total:.0e}.")

# Check obstruction 1 from W2-3
print(f"\n  Obstruction 1 (no capture) status:")
print(f"  gamma_CL = {gamma_CL_tau:.6e} M_KK  << gamma_H = {gamma_H:.4f} M_KK")
print(f"  CL friction does NOT overcome obstruction 1.")
print(f"  The modulus is NOT captured by the GGE bath.")

# ============================================================
# 12. SAVE RESULTS
# ============================================================
print("\n--- Saving results ---")

np.savez("tier0-computation/s46_gge_friction.npz",
    # Gate
    gate_name="GGE-FRICTION-46",
    gate_verdict="INFO",

    # Mode properties
    labels=labels,
    E_k=E_k,
    n_k=n_k,
    lambda_k=lambda_k,
    Delta_k=Delta_k,
    u_k=u_k,
    v_k=v_k,
    g_k=g_k_arr,
    omega_mode=omega_mode,

    # Spectral density
    omega_arr=omega_arr,
    J_omega=J_omega,
    s_bath=s_bath,
    Gamma_broadening=Gamma_mode,

    # Friction coefficients
    gamma_CL=gamma_CL_tau,
    gamma_H=gamma_H,
    gamma_total=gamma_total,
    gamma_CL_max=gamma_CL_max,
    ratio_CL_H=ratio_CL_H,
    ratio_CL_max_H=gamma_CL_max / gamma_H,

    # Cranking inertia
    M_ATDHFB=M_ATDHFB,
    M_pair=M_pair,
    M_crank=M_crank,

    # Velocity analysis
    v_ratio=v_ratio,
    v_reduction_for_ns=v_reduction_for_ns,
    shortfall=shortfall_total,

    # Beat frequencies
    omega_beats=omega_beats,

    # Key numbers
    epsilon_H=epsilon_H,
    eps_H_target=eps_H_target,

    # ODE solutions
    t_ode=sol_H.t,
    v_H_only=sol_H.y[1],
    v_H_CL=sol_CL.y[1],
    v_H_CL_crank=sol_crank.y[1],

    # J at key frequencies
    J_at_omega_tau=J_at_omega_tau,
    J_at_B2B1_beat=J_at_B2B1_beat,
    J_at_B2B3_beat=J_at_B2B3_beat,
    J_at_B1B3_beat=J_at_B1B3_beat,
)

print("  Saved: tier0-computation/s46_gge_friction.npz")

# ============================================================
# 13. PLOT
# ============================================================
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("GGE-FRICTION-46: Caldeira-Leggett Friction on Tau Modulus",
             fontsize=13, fontweight="bold")

# Panel A: Spectral density J(omega)
ax = axes[0, 0]
ax.plot(omega_arr, J_omega, 'b-', linewidth=1.5, label=r"$J(\omega)$")
ax.axvline(omega_tau, color='r', ls='--', alpha=0.7, label=rf"$\omega_\tau = {omega_tau:.2f}$")
ax.axvline(omega_beats[0], color='g', ls=':', alpha=0.5, label=f"B2-B1 = {omega_beats[0]:.3f}")
ax.axvline(omega_beats[1], color='orange', ls=':', alpha=0.5, label=f"B2-B3 = {omega_beats[1]:.3f}")
# Mark the mode positions
for i in range(8):
    ax.axvline(omega_mode[i], color='gray', ls='-', alpha=0.15)
ax.set_xlabel(r"$\omega$ [M$_{\rm KK}$]")
ax.set_ylabel(r"$J(\omega)$ [M$_{\rm KK}$]")
ax.set_title("Bath Spectral Density")
ax.legend(fontsize=8, loc='upper right')
ax.set_xlim(0, 4)

# Panel B: Coupling strengths
ax = axes[0, 1]
colors = ['tab:blue']*4 + ['tab:orange'] + ['tab:green']*3
bars = ax.bar(range(8), g_k_arr**2, color=colors, edgecolor='k', linewidth=0.5)
ax.set_xticks(range(8))
ax.set_xticklabels([str(l) for l in labels], rotation=45, fontsize=8)
ax.set_ylabel(r"$|g_k|^2$ [M$_{\rm KK}^2$]")
ax.set_title("Mode-Modulus Coupling Strengths")
# Add sector labels
ax.text(1.5, max(g_k_arr**2)*0.9, "B2", color='tab:blue', fontsize=12, ha='center', fontweight='bold')
ax.text(4, max(g_k_arr**2)*0.9, "B1", color='tab:orange', fontsize=12, ha='center', fontweight='bold')
ax.text(6, max(g_k_arr**2)*0.9, "B3", color='tab:green', fontsize=12, ha='center', fontweight='bold')

# Panel C: Velocity evolution
ax = axes[1, 0]
t_norm = sol_H.t / dt_transit
ax.plot(t_norm, sol_H.y[1] / v_terminal, 'b-', linewidth=1.5, label="Hubble only")
ax.plot(t_norm, sol_CL.y[1] / v_terminal, 'r--', linewidth=1.5, label="Hubble + CL")
ax.plot(t_norm, sol_crank.y[1] / v_terminal, 'g:', linewidth=1.5, label="Hubble + CL + crank")
ax.axhline(v_reduction_for_ns, color='k', ls=':', alpha=0.5,
           label=rf"$v$ needed for $n_s = 0.965$: {v_reduction_for_ns:.4f}")
ax.set_xlabel(r"$t / t_{\rm transit}$")
ax.set_ylabel(r"$v / v_{\rm terminal}$")
ax.set_title("Modulus Velocity Evolution")
ax.legend(fontsize=8)
ax.set_ylim(0, 1.1)

# Panel D: Summary diagram
ax = axes[1, 1]
ax.axis('off')

summary_text = (
    f"GGE-FRICTION-46 SUMMARY\n"
    f"{'='*40}\n\n"
    f"Caldeira-Leggett friction:\n"
    f"  gamma_CL = {gamma_CL_tau:.2e} M_KK\n"
    f"  gamma_H  = {gamma_H:.2f} M_KK\n"
    f"  gamma_CL / gamma_H = {ratio_CL_H:.2e}\n\n"
    f"Cranking inertia:\n"
    f"  M_ATDHFB = {M_ATDHFB:.3f}\n"
    f"  M_pair   = {M_pair:.6f}\n"
    f"  M_crank  = {M_crank:.3f}\n\n"
    f"Velocity reduction:\n"
    f"  Achieved: {1/v_ratio:.6f}x\n"
    f"  Needed:   {1/v_reduction_for_ns:.1f}x\n"
    f"  Shortfall: {shortfall_total:.1e}x\n\n"
    f"Gate verdict: INFO\n"
    f"Obstruction 1 NOT overcome.\n"
    f"8 modes too few for macroscopic friction."
)
ax.text(0.05, 0.95, summary_text, transform=ax.transAxes,
        fontsize=9, verticalalignment='top', fontfamily='monospace',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

plt.tight_layout()
plt.savefig("tier0-computation/s46_gge_friction.png", dpi=150, bbox_inches='tight')
print("  Saved: tier0-computation/s46_gge_friction.png")

print("\n" + "=" * 72)
print("GATE: GGE-FRICTION-46 = INFO")
print("gamma_CL / gamma_H = {:.2e}  (negligible)".format(ratio_CL_H))
print("Obstruction 1 (no capture) SURVIVES.")
print("8-mode GGE bath cannot slow the modulus.")
print("=" * 72)
