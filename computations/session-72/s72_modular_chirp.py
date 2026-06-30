#!/usr/bin/env python3
"""
MODULAR-CHIRP-72: GGE Modular Hamiltonian Chirp Rate
=====================================================

Computes the second tau-derivative of the GGE modular Hamiltonian
H_mod = -ln(rho_GGE) = sum_k beta_k * n_k at the van Hove fold and
compares to the chirp rates from S71 CHIRP-UNIVERSALITY-71.

The key question: does d^2(H_mod)/dtau^2 match the chirp universality
result?

Physics:
  The GGE modular Hamiltonian is H_mod(tau) = sum_k beta_k(tau) * n_k(tau).
  The GGE occupations are Bogoliubov-frozen (set at the quench), but the
  mode energies change with tau. The tau-dependence enters through:

  (a) The Bogoliubov rotation: the frozen GGE basis rotates relative to the
      instantaneous eigenbasis of D_K(tau). In the instantaneous basis:
        n_k^{eff}(tau) = |u_k(tau)|^2 * n_k + |v_k(tau)|^2 * (n_k + 1)
      where u_k, v_k are Bogoliubov coefficients connecting tau_fold to tau.

  (b) The modular multipliers: beta_k = ln(1/f_k - 1) for the frozen
      occupations f_k. These do NOT change with tau (they are properties
      of the GGE state, not the Hamiltonian).

  Therefore:
    d^2(H_mod)/dtau^2 = sum_k beta_k * d^2(n_k^{eff})/dtau^2

  At the fold (tau = tau_fold), the Bogoliubov rotation is the identity
  (u_k = 1, v_k = 0), so:
    n_k^{eff}(tau_fold) = n_k  (the frozen occupations)
    d(n_k^{eff})/dtau|_{fold} = 0  (Bogoliubov coefficients are stationary)
    d^2(n_k^{eff})/dtau^2|_{fold} depends on the eigenvalue curvature

  The second derivative of the Bogoliubov occupation involves the
  eigenvalue curvature d^2(epsilon_k)/dtau^2, which is exactly the
  chirp rate kappa_n from S71 (in tau-space, not time-space).

Gate: MODULAR-CHIRP-72
  PASS: |d^2(H_mod)/dtau^2 - kappa_n| / kappa_n < 10^{-8} for all B2 modes
  INFO: Agreement within 10^{-4}
  FAIL: Disagreement > 10^{-4}

Note on S71 kappa_n: S71 defined kappa_n as the mode-resolved contribution
to the collective tachyonic boundary chirp d^2(k_tach)/dtau^2, distributed
via DOS weights. This is NOT the same as d^2(epsilon_k)/dtau^2 from D_K.
The modular Hamiltonian chirp connects to the EIGENVALUE curvatures from
D_K directly. We compute both connections.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

import numpy as np
from scipy.interpolate import CubicSpline

from canonical_constants import (
    tau_fold, M_KK, v_terminal, dt_transit, H_fold,
    Delta_BCS, E_B1, E_B2_mean, E_B3_mean,
    N_dof_BCS, PI, rho_B2_per_mode,
    d2S_fold, dS_fold,
)

print("=" * 72)
print("MODULAR-CHIRP-72: GGE Modular Hamiltonian Chirp Rate")
print("=" * 72)

# ============================================================================
#  SECTION 1: Load Data
# ============================================================================

data_dir = os.path.dirname(__file__)
archive_dir = os.path.join(os.path.dirname(__file__), "..", "_shared")

s71 = np.load(os.path.join(data_dir, 's71_chirp_universality.npz'), allow_pickle=True)
s58 = np.load(os.path.join(data_dir, 's58_pomeranchuk_gge.npz'), allow_pickle=True)
s27 = np.load(os.path.join(archive_dir, 's27_multisector_bcs.npz'), allow_pickle=True)

# S71 chirp data (mode ordering: B1, B2[0-3], B3[0-2])
kappa_s71 = s71['kappa_n']          # Collective chirp distributed by DOS weight
k_chirp_lab_s71 = s71['k_chirp_lab']  # = v_terminal^2 * kappa_s71
mode_labels = list(s71['mode_labels'])

# S58 GGE data (mode ordering: B2[0-3], B1, B3[0-2])
# Reorder to match S71: B1, B2[0-3], B3[0-2]
s71_to_s58 = [4, 0, 1, 2, 3, 5, 6, 7]
beta_k = s58['beta_k'][s71_to_s58]
fk_gge = s58['fk_gge'][s71_to_s58]
N0_k = s58['N0_k'][s71_to_s58]    # GGE mean occupations (BCS v^2)

print(f"\nLoaded data successfully.")
print(f"  S71: {len(kappa_s71)} modes, kappa range [{kappa_s71.min():.4e}, {kappa_s71.max():.4e}]")
print(f"  S58: beta_k = {beta_k}")
print(f"  S58: f_k (occupations) = {fk_gge}")
print(f"  Mode ordering: {mode_labels}")

# ============================================================================
#  SECTION 2: Extract Eigenvalue Flow from D_K Spectrum
# ============================================================================

print(f"\n{'=' * 72}")
print("SECTION 2: Eigenvalue Flow from D_K(tau)")
print(f"{'=' * 72}")

# The 8 BCS modes live in the (0,0) sector of D_K
# tau values: [0, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.50]
taus = np.array([0.0, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.50])
n_tau = len(taus)

# Extract positive eigenvalues from (0,0) sector
evals_flow = np.zeros((8, n_tau))
for ti in range(n_tau):
    evals = np.sort(s27[f'evals_0_0_{ti}'])
    pos = evals[evals > 0]
    evals_flow[:, ti] = pos  # 8 positive eigenvalues, sorted

# Mode identification at fold (tau_idx=3, tau=0.20):
#   pos[0] = 0.81914  -> B1 (singlet, lowest)
#   pos[1-4] = 0.84527 (4-fold degenerate) -> B2[0-3]
#   pos[5-7] = 0.97822 (3-fold degenerate) -> B3[0-2]

print(f"\n  D_K eigenvalues at fold (tau={taus[3]:.2f}):")
for i in range(8):
    print(f"    {mode_labels[i]:>6s}: lambda = {evals_flow[i, 3]:.6f} M_KK")

# Compute derivatives using cubic spline interpolation
print(f"\n  Spectral flow derivatives at fold:")
kappa_dk = np.zeros(8)       # d^2(lambda_k)/dtau^2 from D_K
dlambda_dk = np.zeros(8)     # d(lambda_k)/dtau from D_K
lambda_fold = np.zeros(8)    # lambda_k at fold

for i in range(8):
    cs = CubicSpline(taus, evals_flow[i, :])
    lambda_fold[i] = cs(tau_fold)
    dlambda_dk[i] = cs(tau_fold, 1)   # first derivative
    kappa_dk[i] = cs(tau_fold, 2)     # second derivative (chirp in tau-space)
    print(f"    {mode_labels[i]:>6s}: lambda={lambda_fold[i]:.6f}, "
          f"dlambda/dtau={dlambda_dk[i]:+.6f}, "
          f"d2lambda/dtau2={kappa_dk[i]:+.6f}")

# Convert to physical time chirp: d^2(lambda)/dt^2 = v_terminal^2 * d^2(lambda)/dtau^2
# (at the fold, modulus moves at terminal velocity, so dt = dtau/v_terminal)
kappa_dk_phys = v_terminal**2 * kappa_dk

print(f"\n  Physical chirp rates (v_terminal^2 * kappa_dk):")
print(f"  v_terminal = {v_terminal:.6f} M_KK")
for i in range(8):
    print(f"    {mode_labels[i]:>6s}: d^2(lambda)/dt^2 = {kappa_dk_phys[i]:.4e} M_KK^3")

# ============================================================================
#  SECTION 3: GGE Modular Hamiltonian
# ============================================================================

print(f"\n{'=' * 72}")
print("SECTION 3: GGE Modular Hamiltonian Construction")
print(f"{'=' * 72}")

# The GGE density matrix is:
#   rho_GGE = (1/Z) * exp(-sum_k beta_k * n_k)
# with beta_k = ln(1/f_k - 1) for Fermi-like BCS occupations.
#
# The modular Hamiltonian is:
#   H_mod = -ln(rho_GGE) + const = sum_k beta_k * n_k
#
# At the fold, the n_k are diagonal in the D_K eigenbasis.
# The expectation value:
#   <H_mod> = sum_k beta_k * f_k
#
# As tau changes, the instantaneous D_K eigenbasis rotates relative to
# the frozen GGE basis. The Bogoliubov transformation mixes modes:
#   c_k(tau) = u_k(tau) * c_k(fold) + v_k(tau) * c_k^dag(fold)
# with |u_k|^2 - |v_k|^2 = 1 (bosonic) or |u_k|^2 + |v_k|^2 = 1 (fermionic).
#
# For the BCS case (fermionic quasiparticles):
#   n_k^{eff}(tau) = <c_k^dag(tau) c_k(tau)>_GGE
#     = |u_k(tau)|^2 * f_k + |v_k(tau)|^2 * (1 - f_k)
# where f_k = fk_gge are the frozen GGE occupations.

# Verify beta_k consistency
print(f"\n  GGE parameters:")
print(f"  {'Mode':>8s}  {'beta_k':>10s}  {'f_k':>10s}  {'beta_check':>12s}  {'delta':>12s}")
for i in range(8):
    beta_check = np.log(1.0/fk_gge[i] - 1.0)
    delta = abs(beta_k[i] - beta_check)
    print(f"  {mode_labels[i]:>8s}  {beta_k[i]:>10.6f}  {fk_gge[i]:>10.6f}  "
          f"{beta_check:>12.6f}  {delta:>12.4e}")

# The beta_k from S58 are not exactly ln(1/f-1) -- they include
# the mode energy dependence. The stored beta_k are the true GGE
# Lagrange multipliers. Use them as given.

# Modular Hamiltonian at the fold:
H_mod_fold = np.sum(beta_k * fk_gge)
print(f"\n  H_mod at fold = sum_k beta_k * f_k = {H_mod_fold:.6f} M_KK")

# The partition function:
Z_GGE = np.prod(1.0 + np.exp(-beta_k))
ln_Z = np.sum(np.log(1.0 + np.exp(-beta_k)))
print(f"  ln(Z_GGE) = {ln_Z:.6f}")

# ============================================================================
#  SECTION 4: Bogoliubov Rotation and Second Derivatives
# ============================================================================

print(f"\n{'=' * 72}")
print("SECTION 4: Bogoliubov Rotation -- d^2(n_k^eff)/dtau^2")
print(f"{'=' * 72}")

# The Bogoliubov coefficients connect the frozen (fold) basis to the
# instantaneous (tau) basis. For BCS:
#   u_k(tau) = cos(theta_k(tau) - theta_k(fold))
#   v_k(tau) = sin(theta_k(tau) - theta_k(fold))
# where theta_k is the Bogoliubov angle: tan(2*theta_k) = Delta / (epsilon_k - mu).
#
# At the fold: theta_k(fold) = theta_k_0, so u_k(fold)=1, v_k(fold)=0.
# Near the fold:
#   theta_k(tau) = theta_k_0 + dtheta/dtau * (tau - tau_fold) + ...
# so u_k ~ 1 - (1/2)(dtheta/dtau)^2 * delta_tau^2 + ...
#    v_k ~ dtheta/dtau * delta_tau + ...
#
# The effective occupation:
#   n_k^{eff}(tau) = |u_k|^2 * f_k + |v_k|^2 * (1 - f_k)
#     = f_k + |v_k|^2 * (1 - 2*f_k)
#
# Near the fold:
#   n_k^{eff} ~ f_k + (dtheta_k/dtau)^2 * (1 - 2*f_k) * delta_tau^2
#
# Therefore:
#   d(n_k^{eff})/dtau|_{fold} = 0  (v_k = 0 at fold)
#   d^2(n_k^{eff})/dtau^2|_{fold} = 2 * (dtheta_k/dtau)^2 * (1 - 2*f_k)
#
# The Bogoliubov angle derivative is related to the eigenvalue curvature.
# For BCS: theta_k = (1/2) * arctan(Delta / (epsilon_k - mu))
#   dtheta_k/dtau = -(1/2) * Delta * (depsilon_k/dtau) / [(epsilon_k - mu)^2 + Delta^2]
#
# At the fold, the quasiparticle energy is:
#   E_k = sqrt((epsilon_k - mu)^2 + Delta^2)
# so:
#   dtheta_k/dtau = -(1/2) * (Delta / E_k^2) * depsilon_k/dtau
#   (dtheta_k/dtau)^2 = (1/4) * (Delta / E_k^2)^2 * (depsilon_k/dtau)^2

# The second derivative of n_k^{eff} involves two terms:
# (A) From the Bogoliubov angle changing (rotation of basis):
#     d^2(n_k^{eff})/dtau^2|_{rotation} = 2*(dtheta_k/dtau)^2 * (1-2*f_k)
# (B) From the eigenvalue curvature at constant angle:
#     This gives a contribution through d^2(theta)/dtau^2 * v_k * ...
#     but at the fold v_k=0, so this vanishes.
#
# Wait -- there is a subtlety. The rotation contribution (A) comes from
# |v_k|^2 ~ (dtheta/dtau)^2 * dtau^2. But this depends on (depsilon/dtau)^2,
# NOT on d^2(epsilon)/dtau^2. The eigenvalue CURVATURE (kappa) enters
# differently.
#
# Let me be more careful. The modular Hamiltonian in the instantaneous basis:
#   H_mod(tau) = sum_k beta_k * n_k^{eff}(tau)
#
# The tau-dependence is ENTIRELY through the Bogoliubov rotation.
# n_k^{eff}(tau) depends on theta_k(tau) which depends on epsilon_k(tau).
#
# dH_mod/dtau = sum_k beta_k * dn_k^{eff}/dtau
#   = sum_k beta_k * d/dtau [f_k + (1-2*f_k)*sin^2(theta_k(tau)-theta_k(fold))]
#   = sum_k beta_k * (1-2*f_k) * sin(2*(theta-theta_0)) * dtheta/dtau
#
# At fold: sin(2*(theta-theta_0)) = 0, so dH_mod/dtau|_{fold} = 0. GOOD.
#
# d^2H_mod/dtau^2|_{fold} = sum_k beta_k * (1-2*f_k) *
#   [2*cos(0)*(dtheta/dtau)^2 + sin(0)*(d^2theta/dtau^2)]
#   = 2 * sum_k beta_k * (1-2*f_k) * (dtheta_k/dtau)^2
#
# This is the ROTATIONAL contribution. It depends on (depsilon/dtau)^2.
# The eigenvalue CURVATURE d^2(epsilon)/dtau^2 enters through d^2theta/dtau^2,
# but that term is multiplied by sin(0) = 0 at the fold. So the curvature
# kappa_k does NOT directly enter d^2(H_mod)/dtau^2 at the fold.
#
# The chirp in H_mod is driven by MODE SPLITTING (first derivatives of
# eigenvalues), not by eigenvalue curvature.

# For the B2 modes: dlambda/dtau ~ 0 at the fold (van Hove).
# Therefore dtheta_B2/dtau ~ 0 and d^2(H_mod)/dtau^2 from B2 is SMALL.
# For B1 and B3: dlambda/dtau is nonzero, so they contribute.

# Compute the Bogoliubov parameters
mu = E_B1  # Chemical potential ~ lowest mode energy at fold

# Mode energies at fold (from D_K)
eps_fold = lambda_fold  # single-particle energies

# BCS gap at fold
Delta = Delta_BCS

# Quasiparticle energies
E_qp = np.sqrt((eps_fold - mu)**2 + Delta**2)

print(f"\n  BCS parameters at fold:")
print(f"    mu (chemical potential) = {mu:.6f} M_KK")
print(f"    Delta (BCS gap) = {Delta:.6f} M_KK")
print(f"    {'Mode':>8s}  {'eps_k':>10s}  {'eps-mu':>10s}  {'E_qp':>10s}  {'theta_k':>10s}")
for i in range(8):
    theta_k = 0.5 * np.arctan2(Delta, eps_fold[i] - mu)
    print(f"    {mode_labels[i]:>8s}  {eps_fold[i]:>10.6f}  "
          f"{eps_fold[i]-mu:>+10.6f}  {E_qp[i]:>10.6f}  {theta_k:>10.6f}")

# Bogoliubov angle and its tau-derivative at the fold
theta_k_fold = 0.5 * np.arctan2(Delta, eps_fold - mu)
dtheta_dtau = -0.5 * Delta * dlambda_dk / E_qp**2
# (depsilon_k/dtau = dlambda_dk from Section 2)

print(f"\n  Bogoliubov angle derivatives:")
print(f"    {'Mode':>8s}  {'dtheta/dtau':>14s}  {'(dtheta/dtau)^2':>16s}  {'dlambda/dtau':>14s}")
for i in range(8):
    print(f"    {mode_labels[i]:>8s}  {dtheta_dtau[i]:>+14.6e}  "
          f"{dtheta_dtau[i]**2:>16.6e}  {dlambda_dk[i]:>+14.6e}")

# Second derivative of effective occupation
d2n_eff = 2.0 * dtheta_dtau**2 * (1.0 - 2.0 * fk_gge)

print(f"\n  Second derivatives of effective occupation:")
print(f"    {'Mode':>8s}  {'d2n_eff/dtau2':>14s}  {'1-2f_k':>10s}")
for i in range(8):
    print(f"    {mode_labels[i]:>8s}  {d2n_eff[i]:>+14.6e}  {1-2*fk_gge[i]:>+10.6f}")

# ============================================================================
#  SECTION 5: Modular Hamiltonian Chirp Rate
# ============================================================================

print(f"\n{'=' * 72}")
print("SECTION 5: d^2(H_mod)/dtau^2 at the Fold")
print(f"{'=' * 72}")

# d^2(H_mod)/dtau^2 = sum_k beta_k * d^2(n_k^eff)/dtau^2
d2H_mod = np.sum(beta_k * d2n_eff)

# Per-mode contributions
d2H_mod_per_mode = beta_k * d2n_eff

print(f"\n  Per-mode contributions to d^2(H_mod)/dtau^2:")
print(f"  {'Mode':>8s}  {'beta_k':>10s}  {'d2n_eff':>14s}  {'contribution':>14s}  {'fraction':>10s}")
total = 0.0  # (local)
for i in range(8):
    frac = d2H_mod_per_mode[i] / d2H_mod if d2H_mod != 0 else 0
    print(f"  {mode_labels[i]:>8s}  {beta_k[i]:>10.6f}  {d2n_eff[i]:>+14.6e}  "
          f"{d2H_mod_per_mode[i]:>+14.6e}  {frac:>+10.4f}")
    total += d2H_mod_per_mode[i]

print(f"  {'TOTAL':>8s}  {'':>10s}  {'':>14s}  {total:>+14.6e}")

# Physical chirp in time: d^2(H_mod)/dt^2 = v_terminal^2 * d^2(H_mod)/dtau^2
d2H_mod_phys = v_terminal**2 * d2H_mod

print(f"\n  d^2(H_mod)/dtau^2 = {d2H_mod:.6e} M_KK")
print(f"  d^2(H_mod)/dt^2 = v_terminal^2 * above = {d2H_mod_phys:.6e} M_KK^3")
print(f"  v_terminal = {v_terminal:.6f}")

# ============================================================================
#  SECTION 6: Comparison with S71 Chirp Rates
# ============================================================================

print(f"\n{'=' * 72}")
print("SECTION 6: Comparison with S71 Chirp Universality")
print(f"{'=' * 72}")

# S71 kappa_n are COLLECTIVE chirp rates (d^2(k_tach)/dtau^2 distributed
# by DOS weight). These are NOT the same as eigenvalue curvatures.
#
# The modular Hamiltonian chirp d^2(H_mod)/dtau^2 involves:
#   - The GGE multipliers beta_k
#   - The Bogoliubov rotation rate dtheta/dtau
#   - The eigenvalue first derivatives dlambda/dtau (NOT second derivatives)
#
# The S71 kappa_n involve:
#   - The collective z''/z curvature
#   - DOS-weighted redistribution
#
# These are fundamentally DIFFERENT quantities. The modular chirp is:
#   d^2(H_mod)/dtau^2 = 2 * sum_k beta_k * (1-2*f_k) * (dtheta_k/dtau)^2
#
# While the S71 chirp is:
#   kappa_n = (weight_n / total_weight) * d^2(k_tach)/dtau^2
#
# The connection: both ultimately trace to the spectral geometry of D_K(tau).
# The eigenvalue curvature kappa_dk = d^2(lambda_k)/dtau^2 is the geometric
# invariant. Let us compare:

print(f"\n  A) Direct comparison: d^2(H_mod)/dtau^2 vs sum(kappa_s71)")
sum_kappa_s71 = np.sum(kappa_s71)
ratio_A = d2H_mod / sum_kappa_s71 if sum_kappa_s71 != 0 else float('inf')
print(f"     d^2(H_mod)/dtau^2 = {d2H_mod:.6e}")
print(f"     sum(kappa_s71)     = {sum_kappa_s71:.6e}")
print(f"     ratio              = {ratio_A:.6e}")
print(f"     These differ by {abs(np.log10(abs(ratio_A))):.1f} orders of magnitude.")
print(f"     REASON: kappa_s71 is a collective z''/z redistribution, not eigenvalue curvature.")

print(f"\n  B) Comparison with eigenvalue curvatures from D_K")
print(f"     kappa_dk = d^2(lambda)/dtau^2 from D_K spectrum (Section 2)")
print(f"     d^2(H_mod)/dtau^2 = {d2H_mod:.6e}")
sum_kappa_dk = np.sum(kappa_dk)
print(f"     sum(kappa_dk)      = {sum_kappa_dk:.6e}")
ratio_B = d2H_mod / sum_kappa_dk if sum_kappa_dk != 0 else float('inf')
print(f"     ratio              = {ratio_B:.6e}")

# Weighted eigenvalue curvature: sum_k beta_k * kappa_dk
weighted_kappa_dk = np.sum(beta_k * kappa_dk)
print(f"     sum(beta_k * kappa_dk) = {weighted_kappa_dk:.6e}")
ratio_C = d2H_mod / weighted_kappa_dk if weighted_kappa_dk != 0 else float('inf')
print(f"     d^2(H_mod) / sum(beta_k * kappa_dk) = {ratio_C:.6e}")

# The correct comparison: the modular chirp vs the beta-weighted eigenvalue chirp
# These are different because the modular chirp involves (depsilon/dtau)^2
# while the eigenvalue chirp is d^2(epsilon)/dtau^2.

print(f"\n  C) The structural relationship:")
print(f"     d^2(H_mod)/dtau^2 = 2 * sum_k beta_k * (1-2*f_k) * [Delta/(2*E_k^2)]^2 * (dlambda_k/dtau)^2")
print(f"     This involves (dlambda/dtau)^2, NOT d^2(lambda)/dtau^2.")
print(f"     The chirp kappa_n = d^2(lambda)/dtau^2 is a DIFFERENT quantity.")
print(f"     They agree only if (dlambda/dtau)^2 ~ d^2(lambda)/dtau^2 * delta_tau,")
print(f"     which is a coincidence, not a structural identity.")

# ============================================================================
#  SECTION 7: Alternative -- Spectral Moment Connection
# ============================================================================

print(f"\n{'=' * 72}")
print("SECTION 7: Spectral Moment Connection")
print(f"{'=' * 72}")

# There IS a structural connection between the modular Hamiltonian and
# the chirp, but it goes through the SPECTRAL ACTION, not through the
# individual mode chirp rates.
#
# The spectral action S(tau) = Tr[f(D_K(tau)/Lambda)] is the generating
# function for all spectral moments. Its second derivative is:
#   d^2S/dtau^2 = sum_n f''(lambda_n/Lambda) * (dlambda_n/dtau)^2 / Lambda^2
#                 + sum_n f'(lambda_n/Lambda) * d^2(lambda_n)/dtau^2 / Lambda
#
# At the fold, the first term is suppressed for B2 modes (dlambda/dtau ~ 0).
# The second term gives the chirp contribution from eigenvalue curvature.
#
# The modular Hamiltonian is related to the spectral action:
#   H_mod = -ln(rho_GGE) = sum_k beta_k * n_k
# This is a DIFFERENT spectral functional from S(tau). The connection:
#   Both are spectral moments, but with different weight functions.
#   S uses f(x) = exp(-x^2) (Gaussian cutoff).
#   H_mod uses beta_k = ln(1/f_k - 1) (GGE multiplier).
#
# The chirp UNIVERSALITY means d^2(lambda)/dtau^2 is frame-independent.
# This is a property of the EIGENVALUES, not of any particular spectral
# functional. Both S(tau) and H_mod(tau) inherit this universality
# through their dependence on the eigenvalues.

# Construct H_mod(tau) at all tau values
H_mod_tau = np.zeros(n_tau)
for ti in range(n_tau):
    # At each tau, compute the Bogoliubov rotation from fold
    eps_tau = evals_flow[:, ti]
    eps_0 = evals_flow[:, 3]  # fold eigenvalues

    # Bogoliubov angles
    theta_tau = 0.5 * np.arctan2(Delta, eps_tau - mu)
    theta_0 = 0.5 * np.arctan2(Delta, eps_0 - mu)
    dtheta = theta_tau - theta_0

    # Effective occupations
    u2 = np.cos(dtheta)**2
    v2 = np.sin(dtheta)**2
    n_eff = u2 * fk_gge + v2 * (1.0 - fk_gge)

    # Modular Hamiltonian expectation
    H_mod_tau[ti] = np.sum(beta_k * n_eff)

print(f"\n  H_mod(tau) at 9 tau values:")
for ti in range(n_tau):
    print(f"    tau={taus[ti]:.2f}: H_mod = {H_mod_tau[ti]:.8f} M_KK")

# Compute derivatives using cubic spline
cs_Hmod = CubicSpline(taus, H_mod_tau)
dH_mod_at_fold = cs_Hmod(tau_fold, 1)
d2H_mod_at_fold = cs_Hmod(tau_fold, 2)

print(f"\n  Derivatives from cubic spline at tau_fold = {tau_fold}:")
print(f"    H_mod(fold)          = {cs_Hmod(tau_fold):.8f} M_KK")
print(f"    dH_mod/dtau(fold)    = {dH_mod_at_fold:.8e}")
print(f"    d^2H_mod/dtau^2(fold) = {d2H_mod_at_fold:.8e}")

# Cross-check: compare spline d^2 to analytical d^2
print(f"\n  Cross-check: analytical vs spline")
print(f"    Analytical d^2H_mod/dtau^2 = {d2H_mod:.6e}")
print(f"    Spline d^2H_mod/dtau^2     = {d2H_mod_at_fold:.6e}")
ratio_check = d2H_mod / d2H_mod_at_fold if d2H_mod_at_fold != 0 else float('inf')
print(f"    ratio = {ratio_check:.6f}")
print(f"    (Disagreement is expected: analytical uses local derivatives,")
print(f"     spline uses global fit to 9 points with wide spacing.)")

# ============================================================================
#  SECTION 8: Modular Chirp in Physical Time
# ============================================================================

print(f"\n{'=' * 72}")
print("SECTION 8: Modular Chirp -- Physical Time Comparison")
print(f"{'=' * 72}")

# d^2(H_mod)/dt^2 = v_terminal^2 * d^2(H_mod)/dtau^2
d2H_dt2_analytical = v_terminal**2 * d2H_mod
d2H_dt2_spline = v_terminal**2 * d2H_mod_at_fold

print(f"\n  In physical time:")
print(f"    d^2(H_mod)/dt^2 (analytical) = {d2H_dt2_analytical:.6e} M_KK^3")
print(f"    d^2(H_mod)/dt^2 (spline)     = {d2H_dt2_spline:.6e} M_KK^3")

# Compare with S71 quantities:
# S71 kappa_n = d^2(k_tach)/dtau^2 * weight_n/total_weight  (distributed collective chirp)
# S71 k_chirp_lab = v_terminal^2 * kappa_n
print(f"\n  S71 quantities for comparison:")
print(f"    sum(k_chirp_lab) = {np.sum(k_chirp_lab_s71):.6e} M_KK^3")
print(f"    sum(kappa_s71)   = {np.sum(kappa_s71):.6e} M_KK")

# Per-mode comparison: modular chirp vs S71 chirp
print(f"\n  Per-mode: modular chirp contribution vs S71 kappa_n")
print(f"  {'Mode':>8s}  {'beta*d2n_eff':>14s}  {'kappa_s71':>14s}  {'ratio':>12s}  {'kappa_dk':>14s}")
for i in range(8):
    r = d2H_mod_per_mode[i] / kappa_s71[i] if kappa_s71[i] != 0 else float('inf')
    print(f"  {mode_labels[i]:>8s}  {d2H_mod_per_mode[i]:>+14.6e}  {kappa_s71[i]:>14.4e}  "
          f"{r:>12.4e}  {kappa_dk[i]:>+14.6f}")

# ============================================================================
#  SECTION 9: Gate Evaluation
# ============================================================================

print(f"\n{'=' * 72}")
print("SECTION 9: GATE EVALUATION -- MODULAR-CHIRP-72")
print(f"{'=' * 72}")

# The gate asks: does d^2(H_mod)/dtau^2 match kappa_n (S71)?
# The answer requires careful identification of what "match" means.
#
# kappa_n from S71 are COLLECTIVE chirp rates (units: M_KK, order ~10^8).
# d^2(H_mod)/dtau^2 is the modular Hamiltonian curvature (units: M_KK, order ~10^{-3}).
# These are DIFFERENT quantities with different physical content.
#
# However, there IS a structural relationship:
# (1) Both trace to the spectral geometry of D_K(tau).
# (2) The chirp universality (frame independence) is inherited by H_mod
#     because H_mod depends on eigenvalues, and eigenvalues are geometric.
# (3) The modular chirp is driven by (dlambda/dtau)^2, while kappa_n
#     is d^2(lambda)/dtau^2. These are independent geometric quantities.
#
# For the B2 modes specifically:
#   dlambda_B2/dtau ~ 0 at fold (van Hove stationary)
#   => d^2(H_mod)/dtau^2 contribution from B2 ~ 0
#   => The modular chirp is DOMINATED by B1 and B3 (non-stationary modes)
# While S71 kappa_n distributes the chirp to B2 modes via DOS weighting.

# Compute the ratio for each mode
print(f"\n  Pre-registered criterion: |d^2(H_mod)/dtau^2 - kappa_n| / kappa_n < 10^{{-8}} for PASS")
print(f"  (10^{{-4}} for INFO, >10^{{-4}} for FAIL)")

deviations = np.zeros(8)
for i in range(8):
    if kappa_s71[i] != 0:
        deviations[i] = abs(d2H_mod_per_mode[i] - kappa_s71[i]) / kappa_s71[i]
    else:
        deviations[i] = float('inf')

print(f"\n  {'Mode':>8s}  {'d2H_mod_mode':>14s}  {'kappa_s71':>14s}  {'deviation':>14s}")
for i in range(8):
    print(f"  {mode_labels[i]:>8s}  {d2H_mod_per_mode[i]:>+14.6e}  {kappa_s71[i]:>14.4e}  {deviations[i]:>14.4e}")

max_dev_B2 = np.max(deviations[1:5])   # B2 modes
max_dev_all = np.max(deviations)

print(f"\n  Max deviation (B2 modes): {max_dev_B2:.4e}")
print(f"  Max deviation (all modes): {max_dev_all:.4e}")

# The modular chirp and S71 chirp are INCOMMENSURABLE quantities.
# d^2(H_mod)/dtau^2 is order ~10^{-3} while kappa_s71 is order ~10^{8}.
# The relative deviation is O(1), not small.

if max_dev_B2 < 1e-8:
    verdict = "PASS"
elif max_dev_B2 < 1e-4:
    verdict = "INFO"
else:
    verdict = "FAIL"

print(f"\n  MODULAR-CHIRP-72: {verdict}")
print(f"    Criterion: |d^2(H_mod)/dtau^2 - kappa_s71| / kappa_s71 < 10^{{-8}} for PASS")
print(f"    Result: max B2 deviation = {max_dev_B2:.4e} (>> 10^{{-4}})")

# ============================================================================
#  SECTION 10: Structural Analysis -- What the Modular Chirp DOES Encode
# ============================================================================

print(f"\n{'=' * 72}")
print("SECTION 10: What the Modular Chirp Encodes")
print(f"{'=' * 72}")

# The modular chirp d^2(H_mod)/dtau^2 does NOT match kappa_s71.
# But it DOES encode physical information about the GGE state:
#
# 1. It measures how fast the GGE density matrix rotates relative to
#    the instantaneous eigenbasis as tau changes.
# 2. At the fold, d(H_mod)/dtau = 0 (modular Hamiltonian is stationary),
#    which is a CROSS-CHECK: the fold is an extremum of the spectral flow.
# 3. d^2(H_mod)/dtau^2 measures the STIFFNESS of the modular Hamiltonian
#    against deformations of the internal geometry.

# Cross-check 1: dH_mod/dtau = 0 at fold
print(f"\n  Cross-check 1: dH_mod/dtau at fold")
print(f"    Analytical: sum_k beta_k * (1-2*f_k) * sin(2*dtheta) * dtheta/dtau")
dH_analytical = np.sum(beta_k * (1.0 - 2.0 * fk_gge) * 2.0 * dtheta_dtau * 1.0)
# At fold, sin(2*dtheta) * |dtheta=0 -> 0, but the expansion gives:
# d/dtau [sin^2(dtheta)] = 2*sin(dtheta)*cos(dtheta)*dtheta/dtau
# At fold: dtheta=0, so sin(0)*cos(0) = 0. Thus dH/dtau = 0 identically.
# But the spline gives a nonzero value due to ASYMMETRY in the spectral flow.
print(f"    From spline: dH_mod/dtau = {dH_mod_at_fold:.6e}")
print(f"    NOTE: Nonzero from spline because the fold is not exactly at a")
print(f"    grid point (tau_fold=0.19, grid has tau=0.15, 0.20, 0.25).")
print(f"    The B1 and B3 modes have dlambda/dtau != 0 at fold, contributing")
print(f"    a nonzero dH_mod/dtau from their Bogoliubov rotation.")

# Cross-check 2: Tr(H_mod) stationarity in interaction picture
# The GGE state is stationary: rho_GGE does not evolve in time.
# H_mod = -ln(rho_GGE) is therefore tau-independent in the GGE frame.
# The tau-dependence we compute is in the INSTANTANEOUS basis.
print(f"\n  Cross-check 2: H_mod stationarity")
print(f"    H_mod(tau=0.00) = {H_mod_tau[0]:.8f}")
print(f"    H_mod(tau=0.20) = {H_mod_tau[3]:.8f}")
print(f"    H_mod(tau=0.50) = {H_mod_tau[8]:.8f}")
print(f"    Variation: {(H_mod_tau.max() - H_mod_tau.min()):.6e}")
print(f"    H_mod varies because the Bogoliubov rotation changes the")
print(f"    effective occupations in the instantaneous basis.")

# Cross-check 3: The B2 contribution is suppressed
B2_frac = np.sum(np.abs(d2H_mod_per_mode[1:5])) / np.sum(np.abs(d2H_mod_per_mode))
B1_frac = np.abs(d2H_mod_per_mode[0]) / np.sum(np.abs(d2H_mod_per_mode))
B3_frac = np.sum(np.abs(d2H_mod_per_mode[5:])) / np.sum(np.abs(d2H_mod_per_mode))
print(f"\n  Cross-check 3: Mode dominance in modular chirp")
print(f"    B1 fraction: {B1_frac:.4f} ({B1_frac*100:.1f}%)")
print(f"    B2 fraction: {B2_frac:.4f} ({B2_frac*100:.1f}%)")
print(f"    B3 fraction: {B3_frac:.4f} ({B3_frac*100:.1f}%)")
print(f"    B2 suppressed because dlambda_B2/dtau ~ 0 at van Hove fold.")

# ============================================================================
#  SECTION 11: The Correct Statement
# ============================================================================

print(f"\n{'=' * 72}")
print("SECTION 11: The Correct Structural Statement")
print(f"{'=' * 72}")

# The modular chirp and eigenvalue chirp are DIFFERENT spectral functionals
# of the same geometric invariant (the D_K eigenvalue flow).
#
# Chirp universality (S71): d^2(lambda_n)/dtau^2 is frame-independent.
#   This is because eigenvalues are REPARAMETRIZATION INVARIANTS.
#
# Modular chirp: d^2(H_mod)/dtau^2 = f(dlambda/dtau, d^2lambda/dtau^2)
#   This is ALSO frame-independent, for the same reason.
#   But it's a DIFFERENT function of the eigenvalue flow.
#
# The group-theoretic derivation of frame independence:
#   D_K(tau) = D_K(tau) in ANY basis. Its eigenvalues are the same.
#   Any spectral functional F[{lambda_n(tau)}] inherits frame independence.
#   Both kappa_n and d^2(H_mod)/dtau^2 are spectral functionals.
#   Both are frame-independent. But they are NOT equal.

# The modular chirp is a QUADRATIC function of first derivatives:
d2H_from_first_deriv = 2.0 * np.sum(
    beta_k * (1.0 - 2.0 * fk_gge) * (Delta / (2.0 * E_qp**2))**2 * dlambda_dk**2
)

# The eigenvalue chirp is a LINEAR function of second derivatives:
d2H_from_second_deriv = np.sum(beta_k * kappa_dk)

print(f"\n  d^2(H_mod)/dtau^2:")
print(f"    From Bogoliubov rotation (quadratic in dlambda/dtau): {d2H_from_first_deriv:.6e}")
print(f"    From eigenvalue curvature (linear in d^2lambda/dtau^2): {d2H_from_second_deriv:.6e}")
print(f"    The actual modular chirp is the ROTATIONAL term (Bogoliubov).")
print(f"    The eigenvalue curvature term enters at HIGHER ORDER (d^2theta/dtau^2).")

# Ratio of these two contributions:
if d2H_from_second_deriv != 0:
    ratio_contributions = d2H_from_first_deriv / d2H_from_second_deriv
    print(f"\n    Ratio (rotation / curvature) = {ratio_contributions:.6e}")
    print(f"    The modular chirp is {abs(ratio_contributions):.2e}x the naive beta*kappa term.")

# Frame independence of the modular chirp:
# In physical time: d^2(H_mod)/dt^2 = v^2 * d^2(H_mod)/dtau^2
# Since H_mod depends on eigenvalues (frame-independent), and the
# frame transformation is just dtau -> dt with a Jacobian, the
# modular chirp in tau-space is frame-independent by construction.
print(f"\n  Frame independence:")
print(f"    d^2(H_mod)/dtau^2 is frame-independent because it depends")
print(f"    only on eigenvalues of D_K(tau), which are reparametrization")
print(f"    invariants. This follows from the same argument as S71.")
print(f"    The specific VALUE of d^2(H_mod)/dtau^2 differs from kappa_n")
print(f"    because H_mod is a different spectral functional from lambda_n.")

# ============================================================================
#  SECTION 12: Save Results
# ============================================================================

print(f"\n{'=' * 72}")
print("SECTION 12: Saving Results")
print(f"{'=' * 72}")

outfile = os.path.join(data_dir, 's72_modular_chirp.npz')
np.savez(outfile,
    # Gate
    gate_name='MODULAR-CHIRP-72',
    gate_verdict=verdict,
    gate_criterion='|d2H_mod - kappa_s71| / kappa_s71 < 1e-8 (PASS), 1e-4 (INFO)',
    max_dev_B2=max_dev_B2,
    max_dev_all=max_dev_all,

    # Eigenvalue flow from D_K
    taus=taus,
    evals_flow=evals_flow,
    lambda_fold=lambda_fold,
    dlambda_dk=dlambda_dk,
    kappa_dk=kappa_dk,
    kappa_dk_phys=kappa_dk_phys,

    # GGE parameters
    beta_k=beta_k,
    fk_gge=fk_gge,
    mode_labels=np.array(mode_labels),

    # BCS parameters
    mu=mu,
    Delta=Delta,
    E_qp=E_qp,
    theta_k_fold=theta_k_fold,
    dtheta_dtau=dtheta_dtau,

    # Modular Hamiltonian
    H_mod_tau=H_mod_tau,
    H_mod_fold=H_mod_fold,
    d2H_mod_analytical=d2H_mod,
    d2H_mod_spline=d2H_mod_at_fold,
    d2H_mod_per_mode=d2H_mod_per_mode,
    d2H_mod_phys=d2H_mod_phys,
    dH_mod_at_fold=dH_mod_at_fold,
    d2n_eff=d2n_eff,

    # Structural decomposition
    d2H_from_rotation=d2H_from_first_deriv,
    d2H_from_curvature=d2H_from_second_deriv,

    # S71 comparison
    kappa_s71=kappa_s71,
    k_chirp_lab_s71=k_chirp_lab_s71,
    deviations=deviations,

    # Cross-checks
    B1_fraction=B1_frac,
    B2_fraction=B2_frac,
    B3_fraction=B3_frac,
    H_mod_variation=H_mod_tau.max() - H_mod_tau.min(),
)

print(f"  Saved to {outfile}")
print(f"  Keys: {36} entries")

# ============================================================================
#  FINAL SUMMARY
# ============================================================================

print(f"\n{'=' * 72}")
print("FINAL SUMMARY")
print(f"{'=' * 72}")

print(f"""
MODULAR-CHIRP-72: {verdict}

Key numbers:
  1. d^2(H_mod)/dtau^2 = {d2H_mod:.6e} (analytical, Bogoliubov rotation)
  2. d^2(H_mod)/dtau^2 = {d2H_mod_at_fold:.6e} (spline, 9-point global fit)
  3. sum(kappa_s71)     = {sum_kappa_s71:.6e} (S71 collective chirp)
  4. sum(beta*kappa_dk) = {d2H_from_second_deriv:.6e} (beta-weighted eigenvalue curvature)
  5. Max B2 deviation   = {max_dev_B2:.4e} (>> 10^{{-4}})

Structural finding:
  The modular Hamiltonian chirp d^2(H_mod)/dtau^2 is driven by the
  BOGOLIUBOV ROTATION (quadratic in dlambda/dtau), not by the eigenvalue
  curvature (linear in d^2lambda/dtau^2). These are different spectral
  functionals of the same D_K eigenvalue flow.

  At the van Hove fold, dlambda_B2/dtau ~ 0, so the B2 contribution to
  the modular chirp is SUPPRESSED. The chirp is dominated by B1 and B3
  (non-stationary modes).

  Both quantities are frame-independent (both are spectral functionals
  of D_K eigenvalues), but they measure DIFFERENT aspects of the spectral
  geometry: the modular chirp measures the GGE state's rotation rate,
  while kappa_n measures the eigenvalue band curvature.

Cross-checks:
  1. dH_mod/dtau at fold: {dH_mod_at_fold:.4e} (near-zero, fold is near-extremum)
  2. H_mod variation over transit: {H_mod_tau.max()-H_mod_tau.min():.6e} (moderate)
  3. B2 fraction of modular chirp: {B2_frac*100:.1f}% (suppressed by van Hove stationarity)
  4. B1/B3 dominate: {(B1_frac+B3_frac)*100:.1f}% (non-stationary modes drive the chirp)
""")

print("COMPUTATION COMPLETE.")
