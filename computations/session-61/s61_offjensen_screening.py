#!/usr/bin/env python3
"""
S61 Off-Jensen Screening Ratio on 2D Volume-Preserving Surface
===============================================================

Gate: OFFJ-SCREEN-61
  PASS if max R_screen > 10^4
  FAIL if max R_screen < 100
  INFO if in [100, 10^4]

Physics:
  The Jensen line parametrizes left-invariant metrics on SU(3) with
  lambda_1 = lambda_2 (the u(2) block scales uniformly relative to the
  C^2 complement). The S60 screening ratio on the Jensen line is 16.1.

  Off-Jensen, we allow lambda_1 != lambda_2 while maintaining
  vol(SU(3)) = const (the 8D determinant constraint). This opens a 2D
  surface in the 3-parameter space (lambda_1, lambda_2, lambda_3).

  At each point on this surface we compute:
    R_screen = |d(alpha)/d(n_hat)| / |da_2/d(n_hat)|
  along the steepest direction, using the Hessian data from S60.

Mathematical setup:
  The general Ad(U(2))-invariant metric on su(3) is
    beta_tilde = lambda_1 * <,>|_{u(1)} + lambda_2 * <,>|_{su(2)} + lambda_3 * <,>|_{C^2}
  (Baptista paper 13, eq 5.4).

  Dimensions: u(1) has dim 1, su(2) has dim 3, C^2 has dim 4.
  Total dim = 8.

  Volume: Vol(SU(3), beta_tilde) propto lambda_1^{1/2} * lambda_2^{3/2} * lambda_3^{4/2}
  so the volume-preserving constraint is:
    lambda_1^{1/2} * lambda_2^{3/2} * lambda_3^2 = const

  Jensen line: lambda_1 = lambda_2 = lambda, lambda_3 = lambda * e^{-2*tau}
  (the exponential parametrization used in the project).

  The Seeley-DeWitt coefficients a_k depend on the metric through the
  Dirac spectrum. The S60 Hessian data gives d^2 a_k / d(moduli)^2
  in the (tau, sigma, delta_1) coordinate system, where:
    tau = Jensen parameter (overall u(2)/C^2 ratio)
    sigma = off-Jensen anisotropy (lambda_1/lambda_2 ratio)
    delta_1 = additional off-diagonal deformation

  The spectral action is S = Phi_0 * a_0 + Phi_1 * Lambda^2 * a_2 + Phi_2 * a_4 + ...
  and alpha = (Phi_1/Phi_2) * Lambda^2 controls the a_2/a_4 balance.

  The screening ratio R_screen = |d(S)/d(n)| / |da_2/d(n)| along the
  direction n that maximises this ratio on the volume-preserving surface.

Approach:
  1. Map the (lambda_1, lambda_2, lambda_3) space to the (tau, sigma, delta_1)
     Hessian coordinates used in S60.
  2. The volume constraint lambda_1^{1/2} * lambda_2^{3/2} * lambda_3^2 = const
     defines a 2D surface. Its normal in the 3D moduli space is known analytically.
  3. Project the Hessian onto this surface.
  4. Compute R_screen on a grid of directions within the surface.
  5. Find the maximum.

Author: baptista-spacetime-analyst
Session: S61, Wave 3
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
import sys
import time

sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import (
    tau_fold, a0_fold, a2_fold, a4_fold, Vol_SU3_Haar,
    M_KK_gravity, M_KK_kerner, clock_coeff, PI
)

t0 = time.time()

# =============================================================================
# 1. Load S60 Hessian data
# =============================================================================
data_dir = Path(__file__).parent
hess_data = np.load(data_dir / 's60_hessian_3d.npz', allow_pickle=True)
dim_data = np.load(data_dir / 's60_sector_dim_reduct.npz', allow_pickle=True)

# Extract Hessians of Seeley-DeWitt coefficients
H_a0 = hess_data['H_a0']  # shape (3,3)
H_a2 = hess_data['H_a2']  # shape (3,3)
H_a4 = hess_data['H_a4']  # shape (3,3)

# Extract a_k values at fold
a0_3d = hess_data['a0_3d']
a2_3d = hess_data['a2_3d']
a4_3d = hess_data['a4_3d']
S_heat_3d = hess_data['S_heat_3d']

# Grid parameters
tau_arr = hess_data['tau_arr']
sig_arr = hess_data['sig_arr']
d1_arr = hess_data['d1_arr']
dtau = float(hess_data['dtau'])
dsig = float(hess_data['dsig'])
dd1 = float(hess_data['dd1'])

c = 2  # center index
Lambda_sq = float(hess_data['Lambda_sq'])

# Values at fold
a0_at_fold = a0_3d[c, c, c]
a2_at_fold = a2_3d[c, c, c]
a4_at_fold = a4_3d[c, c, c]
S_heat_at_fold = S_heat_3d[c, c, c]

print("=" * 70)
print("S61 Off-Jensen Screening Ratio — Volume-Preserving Surface")
print("=" * 70)
print(f"\nFold point: tau = {tau_fold}")
print(f"a0 at fold = {a0_at_fold:.4f}")
print(f"a2 at fold = {a2_at_fold:.4f}")
print(f"a4 at fold = {a4_at_fold:.4f}")
print(f"S_heat at fold = {S_heat_at_fold:.4f}")
print(f"Lambda^2 (from S60) = {Lambda_sq:.4f}")

# =============================================================================
# 2. Compute gradients of a_k at fold (central differences)
# =============================================================================
grad_a0 = np.array([
    (a0_3d[c+1, c, c] - a0_3d[c-1, c, c]) / (2 * dtau),
    (a0_3d[c, c+1, c] - a0_3d[c, c-1, c]) / (2 * dsig),
    (a0_3d[c, c, c+1] - a0_3d[c, c, c-1]) / (2 * dd1),
])
grad_a2 = np.array([
    (a2_3d[c+1, c, c] - a2_3d[c-1, c, c]) / (2 * dtau),
    (a2_3d[c, c+1, c] - a2_3d[c, c-1, c]) / (2 * dsig),
    (a2_3d[c, c, c+1] - a2_3d[c, c, c-1]) / (2 * dd1),
])
grad_a4 = np.array([
    (a4_3d[c+1, c, c] - a4_3d[c-1, c, c]) / (2 * dtau),
    (a4_3d[c, c+1, c] - a4_3d[c, c-1, c]) / (2 * dsig),
    (a4_3d[c, c, c+1] - a4_3d[c, c, c-1]) / (2 * dd1),
])
grad_Sheat = np.array([
    (S_heat_3d[c+1, c, c] - S_heat_3d[c-1, c, c]) / (2 * dtau),
    (S_heat_3d[c, c+1, c] - S_heat_3d[c, c-1, c]) / (2 * dsig),
    (S_heat_3d[c, c, c+1] - S_heat_3d[c, c, c-1]) / (2 * dd1),
])

print(f"\nGradients at fold (tau, sigma, delta_1 coordinates):")
print(f"  grad(a0) = [{grad_a0[0]:.2f}, {grad_a0[1]:.2f}, {grad_a0[2]:.2f}]")
print(f"  grad(a2) = [{grad_a2[0]:.2f}, {grad_a2[1]:.2f}, {grad_a2[2]:.2f}]")
print(f"  grad(a4) = [{grad_a4[0]:.2f}, {grad_a4[1]:.2f}, {grad_a4[2]:.2f}]")
print(f"  grad(S_heat) = [{grad_Sheat[0]:.2f}, {grad_Sheat[1]:.2f}, {grad_Sheat[2]:.2f}]")

# =============================================================================
# 3. Volume-preserving constraint
# =============================================================================
# The volume of SU(3) with the Ad(U(2))-invariant metric is:
#   Vol propto lambda_1^{1/2} * lambda_2^{3/2} * lambda_3^2
# In the moduli coordinates (tau, sigma, delta_1):
#   tau parametrizes the Jensen line: lambda_1 = lambda_2 = lam, lambda_3 = lam * e^{-2*tau}
#   sigma parametrizes lambda_1/lambda_2 anisotropy: lambda_1 = lam*(1+sigma), lambda_2 = lam*(1-sigma/3)
#     (preserving tr(h) = 0 in the u(2) block to leading order)
#   delta_1 parametrizes off-diagonal deformation
#
# The volume constraint to leading order around the fold:
#   d(log Vol)/dtau = d/dtau[1/2 log(lambda_1) + 3/2 log(lambda_2) + 2 log(lambda_3)]
#
# On the Jensen line (lambda_1 = lambda_2 = lam, lambda_3 = lam * e^{-2*tau}):
#   log Vol = 1/2 * log(lam) + 3/2 * log(lam) + 2*(log(lam) - 2*tau) = 4*log(lam) - 4*tau
#   d(log Vol)/dtau = -4  (at fixed lam)
#
# For sigma perturbation (lambda_1 = lam*(1+sigma), lambda_2 = lam*(1-sigma/3)):
#   d(log Vol)/dsigma = 1/2 * 1/(1+sigma) + 3/2 * (-1/3)/(1-sigma/3)
#                     = 1/2 - 1/2 = 0  at sigma = 0
# This is by construction: sigma is a trace-free perturbation in the u(2) block,
# so it preserves volume to first order.
#
# For delta_1: this is already a TT deformation, so d(log Vol)/ddelta_1 = 0.
#
# The volume-preserving surface at the fold is thus the (sigma, delta_1) plane
# to first order, with the tau direction being the normal.
#
# However, the SECOND-order correction matters for the Hessian analysis.
# The constraint surface is:
#   lambda_1^{1/2} * lambda_2^{3/2} * lambda_3^2 = const
# Parametrize: lambda_1 = lam*(1 + sigma), lambda_2 = lam*(1 - sigma/3),
#              lambda_3 = lam * e^{-2*tau} * (1 + delta_1)
# Volume constraint to second order:
#   1/2*log(1+sigma) + 3/2*log(1-sigma/3) + 2*log(1+delta_1) - 4*tau = const
#   [1/2*sigma - sigma^2/4] + [3/2*(-sigma/3) - 3/2*sigma^2/18] + [2*delta_1 - delta_1^2] - 4*tau = const
#   [-sigma^2/4 - sigma^2/12] + [2*delta_1 - delta_1^2] - 4*tau = const
#   -sigma^2/3 + 2*delta_1 - delta_1^2 - 4*tau = const
#
# WAIT: The sigma coordinate is already designed so that the linear volume change is zero.
# And delta_1 is a TT perturbation, NOT a volume mode. Let me re-examine this.
#
# Actually, in the S60 data, the three coordinates (tau, sigma, delta_1) are:
#   tau: Jensen parameter (rescales u(2) relative to C^2)
#   sigma: off-Jensen within u(2) (breaks lambda_1 = lambda_2)
#   delta_1: off-Jensen within C^2 (internal C^2 anisotropy)
#
# The volume constraint normal in the 3D space (tau, sigma, delta_1) at the fold is:
#   n_vol = grad(log Vol) = (-4, 0, 0) + higher order
# i.e., the tau direction is the volume direction.
# The volume-preserving surface is spanned by sigma and delta_1 to first order.
#
# For the Hessian analysis, we need to project onto the (sigma, delta_1) subspace.

# Volume gradient at fold (in (tau, sigma, delta_1) coordinates)
# tau changes volume: d(log Vol)/dtau = -4 on Jensen line
# sigma, delta_1 are volume-preserving to first order by construction
n_vol = np.array([-4.0, 0.0, 0.0])
n_vol_hat = n_vol / np.linalg.norm(n_vol)

print(f"\nVolume constraint normal: n_vol = {n_vol}")
print(f"Volume-preserving surface is (sigma, delta_1) plane to first order")

# =============================================================================
# 4. Project Hessians onto the volume-preserving surface
# =============================================================================
# The volume-preserving surface at the fold is the (sigma, delta_1) plane.
# Projection operator: P = I - n_hat n_hat^T
P = np.eye(3) - np.outer(n_vol_hat, n_vol_hat)  # Projects out tau

# Project Hessians
H_a2_proj = P @ H_a2 @ P  # Projected a2 Hessian
H_a4_proj = P @ H_a4 @ P  # Projected a4 Hessian
H_a0_proj = P @ H_a0 @ P  # Projected a0 Hessian

# The projected gradients on the surface
grad_a2_surf = P @ grad_a2
grad_a4_surf = P @ grad_a4
grad_a0_surf = P @ grad_a0
grad_Sheat_surf = P @ grad_Sheat

print(f"\nProjected gradients (volume-preserving surface):")
print(f"  grad(a2)|_surf = [{grad_a2_surf[0]:.2f}, {grad_a2_surf[1]:.2f}, {grad_a2_surf[2]:.2f}]")
print(f"  grad(a4)|_surf = [{grad_a4_surf[0]:.2f}, {grad_a4_surf[1]:.2f}, {grad_a4_surf[2]:.2f}]")
print(f"  grad(S_heat)|_surf = [{grad_Sheat_surf[0]:.2f}, {grad_Sheat_surf[1]:.2f}, {grad_Sheat_surf[2]:.2f}]")

# =============================================================================
# 5. Screening ratio analysis
# =============================================================================
# The spectral action at physical cutoff Lambda = M_KK (Lambda^2 = 1 in M_KK units):
#   S = f_0 * a_0 + f_2 * a_2 + f_4 * a_4
# where f_k = Phi_{4-k/2} * Lambda^{4-k} are the moments of the cutoff function.
#
# For the heat kernel cutoff: f_0 = 2, f_2 = 2, f_4 = 1 at Lambda^2 = 1
# The key alpha parameter: alpha = f_2/f_4 * Lambda^2 = 2 for heat kernel
#
# The spectral action is: S = f_0 * a_0 + alpha * a_2 + a_4 (dropping f_4 overall)
# And from S60: the SCREENING is about how alpha_EM changes vs clock variance.
#
# From the S60 dimensional reduction analysis:
#   The screening ratio is R_screen = |d(alpha_phys)/d(modulus)| / |da_2/d(modulus)|
# where alpha_phys is the fine-structure constant (NOT the spectral action parameter).
#
# Let me use the S60 framework more precisely. The S60 result:
#   screening_naive = 16.1 along the Jensen line
#   This came from: R_screen = |fractional d(alpha)| / |fractional da2|
#     = |clock_coeff * dtau| / |(1/a2) * da2/dtau * dtau|
#     = |clock_coeff| / |(da2/dtau) / a2|
#
# So R_screen = |clock_coeff * a2| / |da2/dtau|  along Jensen.
#
# For off-Jensen directions, we generalize:
#   R_screen(n) = |d(alpha_phys)/dn| / |d(a2)/dn|
#
# The physical fine-structure constant depends on the metric through the
# gauge coupling formula from Baptista paper 13, eq (5.21):
#   e = 2*sqrt(3) / sqrt(lambda_1 + 3*lambda_2)
#   alpha_phys = e^2 / (4*pi) = 12 / [4*pi * (lambda_1 + 3*lambda_2)]
#               = 3 / [pi * (lambda_1 + 3*lambda_2)]
#
# So d(alpha_phys)/d(modulus) depends on how (lambda_1 + 3*lambda_2) changes.
#
# On the Jensen line: lambda_1 = lambda_2 = lam, so lambda_1 + 3*lambda_2 = 4*lam
#   d(alpha_phys)/dtau = -alpha_phys * d(log(4*lam))/dtau = -alpha_phys * dlam/dtau / lam
#
# Off-Jensen: lambda_1 = lam*(1+sigma), lambda_2 = lam*(1-sigma/3)
#   lambda_1 + 3*lambda_2 = lam*(1+sigma) + 3*lam*(1-sigma/3) = 4*lam
#   so d(lambda_1 + 3*lambda_2)/dsigma = lam - lam = 0 at sigma=0
#
# CRITICAL FINDING: The combination (lambda_1 + 3*lambda_2) is INDEPENDENT of sigma
# to first order! This means d(alpha_phys)/dsigma = 0 on the Jensen line.
#
# But da_2/dsigma != 0. So R_screen = 0 in the pure sigma direction.
# This is the OPPOSITE of what we want.
#
# Let me reconsider. The issue is that sigma changes a_2 (through the eigenvalue
# spectrum) but does NOT change alpha_phys. So the screening gets WORSE off-Jensen.
#
# However, there's a subtlety: the PHYSICAL alpha also depends on the spectral action
# through threshold corrections. The full physical coupling runs as:
#   1/alpha(mu) = 1/alpha_tree + b*log(mu/M_KK) + (spectral action corrections)
#
# The spectral action corrections involve the a_4 coefficient and higher.
# So the EFFECTIVE alpha depends on a_4, which DOES have off-Jensen dependence.
#
# MORE PRECISELY: In the Chamseddine-Connes spectral action framework:
#   The gauge coupling is: 1/g^2 = f_4 * a_4^{gauge} / (48*pi^2)
# where a_4^{gauge} is the gauge-field-dependent part of a_4.
#
# But a_4 has BOTH curvature and gauge contributions. The gauge part scales
# differently from the gravitational part under metric deformations.
#
# Let me take a more direct approach using the S60 data structure.

# The S60 screening ratio was defined as:
#   R_screen = |fractional change in alpha| / |fractional change in a2|
# For a general direction n_hat on the volume-preserving surface:
#   delta_alpha / alpha = clock_coeff * delta_tau_eff(n_hat)
#   delta_a2 / a2 = (grad(a2) . n_hat) * delta / a2

# The key question: what is the effective tau change for off-Jensen directions?
# On the Jensen line, delta_tau_eff = delta_tau.
# Off-Jensen, the clock variance comes from the FIBER VOLUME change, which is
# controlled by tau (the volume mode), not by sigma or delta_1 (which are
# volume-preserving to first order).

# ALTERNATIVE APPROACH: Use the SPECTRAL ACTION directly.
# The spectral action S encodes ALL the physics. The screening question is:
#   Can S change by a large amount while a_2 changes by a small amount?
# If so, the spectral action landscape has a direction that decouples from a_2.
#
# This is a Hessian eigenvector problem. We need the ratio:
#   R_screen(n) = |n^T H_S n| / |n^T H_a2 n|
# maximized over n in the volume-preserving surface.
#
# But more precisely, the clock variance comes from the FULL spectral action
# (which determines the effective gravitational constant and hence clocks),
# while a_2 enters the lapse function. So:
#   R_screen(n) = |n^T H_S n + n^T grad_S * grad_S^T n| / |n^T H_a2 n + ...|

# Let me use the most direct and honest approach.
# For the heat kernel cutoff at Lambda^2 = 1:
#   S = 2*a_0 + 2*a_2 + a_4
# This gives:
#   grad(S) = 2*grad(a0) + 2*grad(a2) + grad(a4)
#   H_S = 2*H_a0 + 2*H_a2 + H_a4

# =============================================================================
# 6. Construct full spectral action Hessian and gradient
# =============================================================================
# Physical alpha values for different cutoffs (from W3-01 results):
# Heat kernel: alpha = Phi_1/Phi_2 * Lambda^2 = 2.0 at Lambda = M_KK
cutoff_configs = {
    'heat_kernel': {'alpha': 2.0, 'f0_f4': 2.0, 'label': r'Heat kernel $e^{-u}$'},
    'gaussian': {'alpha': 1.253, 'f0_f4': 0.886, 'label': r'Gaussian $e^{-u^2/2}$'},
    'sharp': {'alpha': 0.667, 'f0_f4': 0.5, 'label': r'Sharp $\theta(1-u)$'},
    'chi8': {'alpha': 0.182, 'f0_f4': 0.111, 'label': r'$\chi_8\;(1-u)^8$'},
}

print("\n" + "=" * 70)
print("SCREENING RATIO ANALYSIS")
print("=" * 70)

# For each cutoff, the spectral action is:
#   S/f_4 = beta * a_0 + alpha * a_2 + a_4
# where beta = f_0/f_4, alpha = f_2/f_4 * Lambda^2

# The CLOCK constraint (from S22d): delta_alpha_EM / alpha_EM = clock_coeff * delta_tau
# This gives the physical coupling change per unit tau change.
# The physical coupling change along a general direction n in moduli space:
#   d(alpha_EM) / d(n) = clock_coeff * (e_tau . n)
# where e_tau is the unit vector in the tau direction.
# (Because alpha_EM depends on the metric through the gauge coupling formula,
# and on the Jensen line the gauge coupling depends only on the overall lam.)
#
# HOWEVER: off-Jensen, the gauge coupling formula DOES change.
# From Baptista eq (5.21): g'^2/4 = 3/lambda_1, g^2/4 = 1/lambda_2
# The Weinberg angle: sin^2(theta_W) = g'^2/(g'^2 + g^2) = 3*lambda_2/(3*lambda_2 + lambda_1)
# So alpha_EM = alpha_2 * sin^2(theta_W) where alpha_2 = g^2/(4*pi) = 1/(pi*lambda_2)
#
# alpha_EM = sin^2(theta_W) / (pi * lambda_2) = 3/(pi * (3*lambda_2 + lambda_1))
#
# At fold on Jensen: lambda_1 = lambda_2 = lam, so alpha_EM = 3/(4*pi*lam)
# d(alpha_EM)/d(sigma) at sigma=0:
#   lambda_1 = lam*(1+sigma), lambda_2 = lam*(1-sigma/3)
#   3*lambda_2 + lambda_1 = 3*lam*(1-sigma/3) + lam*(1+sigma) = 4*lam
#   This is EXACTLY constant! Independent of sigma!
#
# So d(alpha_EM)/d(sigma) = 0 identically (to all orders in sigma), because
# the combination 3*lambda_2 + lambda_1 is invariant under the sigma deformation.
# This is a structural result: the sigma direction preserves alpha_EM exactly.

# For delta_1 (C^2 anisotropy):
# alpha_EM depends on lambda_1 and lambda_2, not on lambda_3 or its internal structure.
# So d(alpha_EM)/d(delta_1) = 0 as well.

# CONCLUSION: On the volume-preserving surface, d(alpha_EM) = 0 in all directions.
# The physical fine-structure constant is completely insensitive to off-Jensen deformations.
# Only the tau direction (volume mode) changes alpha_EM.

# This means R_screen = |d(alpha_EM)| / |da_2| = 0 for all volume-preserving directions.
# The screening ratio CANNOT be improved by going off-Jensen.

# BUT WAIT: the timescape mechanism doesn't just need alpha_EM to change.
# It needs the CLOCK RATE to change. The clock rate depends on the LAPSE function,
# which comes from the full spectral action, not just alpha_EM.
#
# In the Chamseddine-Connes framework, the effective Newton's constant is:
#   1/(16*pi*G) = f_2 * a_2 / (48*pi^2)
# So G propto 1/a_2, and the clock rate goes as sqrt(G) propto 1/sqrt(a_2).
#
# MORE GENERAL: the lapse N^2 in the ADM decomposition depends on the
# conformal factor relating the Jordan and Einstein frames. This factor is
# determined by a_2 (the coefficient of the Ricci scalar in the spectral action).
#
# So the clock rate IS controlled by a_2. The question is then:
# Can the SPECTRAL ACTION change (driving dynamics) while a_2 stays nearly constant
# (keeping clocks synchronized)?
#
# R_screen_revised = |d(S)/dn| / |da_2/dn|
# where S is the full spectral action.

# =============================================================================
# 7. Compute R_screen on 2D volume-preserving surface — angular scan
# =============================================================================
# The volume-preserving surface is the (sigma, delta_1) plane.
# A direction on this surface is: n = cos(theta) * e_sigma + sin(theta) * e_delta
# where e_sigma = (0, 1, 0), e_delta = (0, 0, 1) in the (tau, sigma, delta_1) basis.

N_theta = 3600  # high resolution angular scan
theta_arr = np.linspace(0, 2*np.pi, N_theta, endpoint=False)

# Results storage
results = {}

for cutoff_name, cfg in cutoff_configs.items():
    alpha_param = cfg['alpha']
    beta_param = cfg['f0_f4']

    # Full spectral action gradient (in (tau, sigma, delta_1) space):
    # S/f_4 = beta * a_0 + alpha * a_2 + a_4
    grad_S = beta_param * grad_a0 + alpha_param * grad_a2 + grad_a4

    # Full spectral action Hessian:
    H_S = beta_param * H_a0 + alpha_param * H_a2 + H_a4

    # Project onto volume-preserving surface
    grad_S_surf = P @ grad_S
    H_S_surf = P @ H_S @ P

    # Now scan directions on the (sigma, delta_1) plane
    R_screen_arr = np.zeros(N_theta)
    dS_arr = np.zeros(N_theta)
    da2_arr = np.zeros(N_theta)

    for i, theta in enumerate(theta_arr):
        # Direction in 3D space (tau=0 component, sigma=cos, delta=sin)
        n = np.array([0.0, np.cos(theta), np.sin(theta)])

        # First-order: directional derivatives
        dS_dn = np.dot(grad_S, n)
        da2_dn = np.dot(grad_a2, n)

        # Second-order: curvature along direction
        d2S_dn2 = n @ H_S @ n
        d2a2_dn2 = n @ H_a2 @ n

        # The screening ratio uses BOTH gradient and curvature.
        # For a finite displacement epsilon along n:
        #   delta_S = dS_dn * epsilon + (1/2) * d2S_dn2 * epsilon^2
        #   delta_a2 = da2_dn * epsilon + (1/2) * d2a2_dn2 * epsilon^2
        # At small epsilon, R_screen = |dS_dn| / |da2_dn| (gradient ratio)
        # At the fold, we also need the curvature ratio for steepness.

        dS_arr[i] = dS_dn
        da2_arr[i] = da2_dn

        if abs(da2_dn) > 1e-10:
            R_screen_arr[i] = abs(dS_dn) / abs(da2_dn)
        else:
            # da2 nearly zero — screening is formally infinite
            R_screen_arr[i] = abs(dS_dn) / 1e-10 if abs(dS_dn) > 1e-10 else 0.0

    results[cutoff_name] = {
        'R_screen': R_screen_arr,
        'dS': dS_arr,
        'da2': da2_arr,
        'max_R': np.max(R_screen_arr),
        'theta_max': theta_arr[np.argmax(R_screen_arr)],
        'grad_S_surf': grad_S_surf,
        'H_S_surf': H_S_surf,
    }

    print(f"\n--- {cfg['label']} (alpha={alpha_param:.3f}, beta={beta_param:.3f}) ---")
    print(f"  grad(S)|_surf = [{grad_S_surf[0]:.2f}, {grad_S_surf[1]:.2f}, {grad_S_surf[2]:.2f}]")
    print(f"  |grad(S)|_surf| = {np.linalg.norm(grad_S_surf):.2f}")
    print(f"  |grad(a2)|_surf| = {np.linalg.norm(grad_a2_surf):.2f}")
    print(f"  max R_screen = {results[cutoff_name]['max_R']:.4f}")
    print(f"  theta(max) = {np.degrees(results[cutoff_name]['theta_max']):.1f} deg")
    print(f"  min |da2| on surface = {np.min(np.abs(da2_arr)):.4f}")

# =============================================================================
# 8. Generalized eigenvalue problem — exact optimization
# =============================================================================
# The maximum of R_screen = |n^T g_S n| / |n^T g_a2 n| over the surface
# is a generalized eigenvalue problem.
# On the (sigma, delta_1) subspace (indices 1,2 of the 3D space):
print("\n" + "=" * 70)
print("GENERALIZED EIGENVALUE ANALYSIS")
print("=" * 70)

for cutoff_name, cfg in cutoff_configs.items():
    alpha_param = cfg['alpha']
    beta_param = cfg['f0_f4']

    # Extract 2x2 blocks on the (sigma, delta_1) subspace
    H_S_2d = beta_param * H_a0[1:3, 1:3] + alpha_param * H_a2[1:3, 1:3] + H_a4[1:3, 1:3]
    H_a2_2d = H_a2[1:3, 1:3]
    grad_S_2d = beta_param * grad_a0[1:3] + alpha_param * grad_a2[1:3] + grad_a4[1:3]
    grad_a2_2d = grad_a2[1:3]

    # For gradient-based R_screen: max |v^T g_S| / |v^T g_a2| over unit vectors v
    # This is: max |grad_S_2d . n| / |grad_a2_2d . n|
    # The gradient vectors determine this completely.

    # Angle of grad_S in (sigma, delta_1) plane
    theta_gradS = np.arctan2(grad_S_2d[1], grad_S_2d[0])
    theta_grada2 = np.arctan2(grad_a2_2d[1], grad_a2_2d[0])

    # The ratio |grad_S . n| / |grad_a2 . n| is maximized when n is perpendicular
    # to grad_a2 (making the denominator zero) — but that makes it infinite or
    # zero depending on whether grad_S has a component there too.

    # More precisely: if grad_a2 and grad_S are NOT parallel, then there exists
    # a direction where da2/dn = 0 but dS/dn != 0, giving R_screen = infinity.
    # If they ARE parallel, R_screen = |grad_S|/|grad_a2| everywhere.

    cos_angle = np.dot(grad_S_2d, grad_a2_2d) / (
        np.linalg.norm(grad_S_2d) * np.linalg.norm(grad_a2_2d) + 1e-30)
    angle_deg = np.degrees(np.arccos(np.clip(cos_angle, -1, 1)))

    print(f"\n--- {cfg['label']} ---")
    print(f"  grad(S)|_2d = [{grad_S_2d[0]:.2f}, {grad_S_2d[1]:.2f}]")
    print(f"  grad(a2)|_2d = [{grad_a2_2d[0]:.2f}, {grad_a2_2d[1]:.2f}]")
    print(f"  |grad(S)|_2d| = {np.linalg.norm(grad_S_2d):.2f}")
    print(f"  |grad(a2)|_2d| = {np.linalg.norm(grad_a2_2d):.2f}")
    print(f"  angle between grad(S) and grad(a2) = {angle_deg:.4f} deg")
    print(f"  cos(angle) = {cos_angle:.8f}")

    # The direction perpendicular to grad_a2 on the surface:
    n_perp_a2 = np.array([-grad_a2_2d[1], grad_a2_2d[0]])
    n_perp_a2 = n_perp_a2 / np.linalg.norm(n_perp_a2)
    dS_perp = np.dot(grad_S_2d, n_perp_a2)
    da2_perp = np.dot(grad_a2_2d, n_perp_a2)  # should be ~0

    print(f"  n_perp(a2) = [{n_perp_a2[0]:.6f}, {n_perp_a2[1]:.6f}]")
    print(f"  dS along n_perp = {dS_perp:.4f}")
    print(f"  da2 along n_perp = {da2_perp:.4e}")

    # Effective R_screen at finite epsilon along n_perp:
    # delta_a2 = da2_perp * epsilon + (1/2) * n_perp^T H_a2 n_perp * epsilon^2
    # delta_S = dS_perp * epsilon + (1/2) * n_perp^T H_S n_perp * epsilon^2
    n_perp_3d = np.array([0.0, n_perp_a2[0], n_perp_a2[1]])
    curv_a2_perp = n_perp_3d @ H_a2 @ n_perp_3d
    curv_S_perp = n_perp_3d @ (beta_param * H_a0 + alpha_param * H_a2 + H_a4) @ n_perp_3d

    print(f"  d2(a2)/dn_perp^2 = {curv_a2_perp:.2f}")
    print(f"  d2(S)/dn_perp^2 = {curv_S_perp:.2f}")

    # R_screen at displacement epsilon along n_perp:
    # R = |dS_perp * eps + 0.5 * curv_S * eps^2| / |da2_perp * eps + 0.5 * curv_a2 * eps^2|
    # Since da2_perp ~ 0, the denominator ~ 0.5 * |curv_a2| * eps^2
    # and numerator ~ |dS_perp| * eps
    # So R_screen ~ |dS_perp| / (0.5 * |curv_a2| * eps) -> infinity as eps -> 0
    # This is formally infinite but physically meaningless at eps=0.

    # For a PHYSICAL screening ratio, we need to ask: over what range epsilon
    # does the FRACTIONAL change in a2 remain below some threshold delta?
    # |delta_a2/a2| < delta requires:
    # 0.5 * |curv_a2| * eps^2 / |a2| < delta (since linear term vanishes)
    # eps < sqrt(2 * delta * |a2| / |curv_a2|)
    # At that eps, the S change is: |dS_perp| * eps / (f_4 * |S_at_fold|)

    for delta_target in [1e-3, 1e-5, 1e-7]:
        if abs(curv_a2_perp) > 0:
            eps_max = np.sqrt(2 * delta_target * abs(a2_at_fold) / abs(curv_a2_perp))
            frac_dS = abs(dS_perp) * eps_max / abs(S_heat_at_fold)
            R_eff = frac_dS / delta_target if delta_target > 0 else 0
            print(f"  At |da2/a2| = {delta_target:.0e}: eps = {eps_max:.6f}, |dS/S| = {frac_dS:.6e}, R_eff = {R_eff:.2f}")

# =============================================================================
# 9. Full 2D grid scan on volume-preserving surface
# =============================================================================
print("\n" + "=" * 70)
print("2D GRID SCAN ON VOLUME-PRESERVING SURFACE")
print("=" * 70)

# Grid in (sigma, delta_1) centered at fold
N_grid = 100  # (local)
sig_range = 0.02  # +/- 0.02 around fold  # (local)
d1_range = 0.02  # (local)
sig_grid = np.linspace(-sig_range, sig_range, N_grid)
d1_grid = np.linspace(-d1_range, d1_range, N_grid)
SIG, D1 = np.meshgrid(sig_grid, d1_grid)

# For each point (sigma, delta_1), compute the a_k values using Taylor expansion:
# a_k(0, sigma, delta_1) = a_k(fold) + grad_a_k[1]*sigma + grad_a_k[2]*delta_1
#   + 0.5 * [H_a_k[1,1]*sigma^2 + 2*H_a_k[1,2]*sigma*delta_1 + H_a_k[2,2]*delta_1^2]
# (The tau component is zero because we're on the volume-preserving surface)

a2_surface = (a2_at_fold
    + grad_a2[1] * SIG + grad_a2[2] * D1
    + 0.5 * (H_a2[1,1] * SIG**2 + 2*H_a2[1,2] * SIG * D1 + H_a2[2,2] * D1**2))

a4_surface = (a4_at_fold
    + grad_a4[1] * SIG + grad_a4[2] * D1
    + 0.5 * (H_a4[1,1] * SIG**2 + 2*H_a4[1,2] * SIG * D1 + H_a4[2,2] * D1**2))

a0_surface = (a0_at_fold
    + grad_a0[1] * SIG + grad_a0[2] * D1
    + 0.5 * (H_a0[1,1] * SIG**2 + 2*H_a0[1,2] * SIG * D1 + H_a0[2,2] * D1**2))

# Compute spectral action on surface for heat kernel cutoff
alpha_hk = 2.0  # (local)
beta_hk = 2.0  # (local)
S_surface = beta_hk * a0_surface + alpha_hk * a2_surface + a4_surface

# Fractional changes from fold
frac_da2 = (a2_surface - a2_at_fold) / abs(a2_at_fold)
frac_dS = (S_surface - S_heat_at_fold) / abs(S_heat_at_fold)

# Local screening ratio at each grid point
# R_screen(x) = |frac_dS(x)| / |frac_da2(x)|
with np.errstate(divide='ignore', invalid='ignore'):
    R_screen_grid = np.abs(frac_dS) / np.abs(frac_da2)
    R_screen_grid[~np.isfinite(R_screen_grid)] = 0

# Mask out the very center where both are ~0
center_mask = (np.abs(frac_da2) < 1e-10) & (np.abs(frac_dS) < 1e-10)
R_screen_grid[center_mask] = 0

# Find maximum
max_idx = np.unravel_index(np.argmax(R_screen_grid), R_screen_grid.shape)
max_R = R_screen_grid[max_idx]
max_sig = sig_grid[max_idx[1]]
max_d1 = d1_grid[max_idx[0]]

print(f"\nHeat kernel cutoff results:")
print(f"  Grid: {N_grid}x{N_grid} on [{-sig_range},{sig_range}] x [{-d1_range},{d1_range}]")
print(f"  max R_screen on grid = {max_R:.4f}")
print(f"  at (sigma, delta_1) = ({max_sig:.4f}, {max_d1:.4f})")
print(f"  frac_da2 at max = {frac_da2[max_idx]:.6e}")
print(f"  frac_dS at max = {frac_dS[max_idx]:.6e}")

# Statistics
valid = R_screen_grid > 0
print(f"  median R_screen = {np.median(R_screen_grid[valid]):.4f}")
print(f"  mean R_screen = {np.mean(R_screen_grid[valid]):.4f}")
print(f"  R_screen > 100: {np.sum(R_screen_grid > 100)} points")
print(f"  R_screen > 10^4: {np.sum(R_screen_grid > 1e4)} points")

# =============================================================================
# 10. Jensen-line comparison
# =============================================================================
print("\n" + "=" * 70)
print("JENSEN LINE COMPARISON")
print("=" * 70)

# On Jensen line: direction = (1, 0, 0) in (tau, sigma, delta_1)
n_jensen = np.array([1.0, 0.0, 0.0])
for cutoff_name, cfg in cutoff_configs.items():
    alpha_param = cfg['alpha']
    beta_param = cfg['f0_f4']
    grad_S_full = beta_param * grad_a0 + alpha_param * grad_a2 + grad_a4
    dS_jensen = np.dot(grad_S_full, n_jensen)
    da2_jensen = np.dot(grad_a2, n_jensen)
    R_jensen = abs(dS_jensen) / abs(da2_jensen) if abs(da2_jensen) > 0 else 0

    # Also compute using the clock constraint formula
    # R_screen_clock = |clock_coeff| / |(da2/dtau)/a2|
    frac_da2_dtau = da2_jensen / a2_at_fold
    R_clock = abs(clock_coeff) / abs(frac_da2_dtau)

    print(f"  {cfg['label']:30s}: R_jensen = {R_jensen:.4f}, R_clock = {R_clock:.4f}")
    print(f"    dS/dtau = {dS_jensen:.2f}, da2/dtau = {da2_jensen:.2f}")

# =============================================================================
# 11. The structural theorem
# =============================================================================
print("\n" + "=" * 70)
print("STRUCTURAL THEOREM: GRADIENT ALIGNMENT")
print("=" * 70)

# The key finding: on the volume-preserving surface, grad(S) and grad(a2)
# are nearly parallel because a_2 dominates the spectral action at physical alpha.
# The alignment angle determines whether R_screen can ever be large.

# Compute alignment for each cutoff
for cutoff_name, cfg in cutoff_configs.items():
    alpha_param = cfg['alpha']
    beta_param = cfg['f0_f4']

    grad_S_2d = beta_param * grad_a0[1:3] + alpha_param * grad_a2[1:3] + grad_a4[1:3]
    grad_a2_2d = grad_a2[1:3]

    # Decompose grad_S into parallel and perpendicular to grad_a2
    cos_angle = np.dot(grad_S_2d, grad_a2_2d) / (
        np.linalg.norm(grad_S_2d) * np.linalg.norm(grad_a2_2d))
    sin_angle = np.sqrt(1 - cos_angle**2)

    # Parallel component: drives a_2 changes
    S_parallel = np.linalg.norm(grad_S_2d) * abs(cos_angle)
    # Perpendicular component: drives S changes WITHOUT a_2 changes
    S_perp = np.linalg.norm(grad_S_2d) * sin_angle

    # The contribution of each a_k to the gradient
    grad_a0_2d = grad_a0[1:3]
    grad_a4_2d = grad_a4[1:3]
    norm_a0_2d = np.linalg.norm(grad_a0_2d)
    norm_a2_2d = np.linalg.norm(grad_a2_2d)
    norm_a4_2d = np.linalg.norm(grad_a4_2d)

    # Maximum possible R_screen on the surface:
    # R_max = S_perp / (0.5 * |curv_a2_perp| * eps)
    # This diverges as eps -> 0, so the physical R is set by the
    # displacement scale. For eps ~ dsig (grid spacing):
    n_perp_a2_2d = np.array([-grad_a2_2d[1], grad_a2_2d[0]])
    n_perp_a2_2d = n_perp_a2_2d / np.linalg.norm(n_perp_a2_2d)
    n_perp_3d = np.array([0.0, n_perp_a2_2d[0], n_perp_a2_2d[1]])
    curv_a2_perp = n_perp_3d @ H_a2 @ n_perp_3d

    # The gradient-based R_screen at finite displacement eps:
    # In the perpendicular direction: da2 ~ 0.5*curv_a2*eps^2, dS ~ S_perp*eps
    # R_screen ~ S_perp / (0.5 * |curv_a2| * eps) at displacement eps
    # This grows as 1/eps. But physically, eps must be > some minimum scale.
    # The relevant scale is the moduli displacement that gives O(1) effects.

    print(f"\n--- {cfg['label']} ---")
    print(f"  |grad(a0)|_surf| = {norm_a0_2d:.2f}")
    print(f"  |grad(a2)|_surf| = {norm_a2_2d:.2f}")
    print(f"  |grad(a4)|_surf| = {norm_a4_2d:.2f}")
    print(f"  alpha * |grad(a2)| = {alpha_param * norm_a2_2d:.2f}")
    print(f"  Ratio alpha*|grad(a2)| / |grad(a4)| = {alpha_param * norm_a2_2d / norm_a4_2d:.4f}")
    print(f"  cos(angle) = {cos_angle:.8f}")
    print(f"  Misalignment angle = {np.degrees(np.arcsin(sin_angle)):.4f} deg")
    print(f"  |grad(S)_perp| (screening component) = {S_perp:.4f}")
    print(f"  |grad(S)_parallel| = {S_parallel:.2f}")
    print(f"  S_perp / S_parallel = {S_perp / S_parallel:.6f}")
    print(f"  curv(a2) along perp = {curv_a2_perp:.2f}")

# =============================================================================
# 12. Final gate verdict
# =============================================================================
print("\n" + "=" * 70)
print("GATE VERDICT: OFFJ-SCREEN-61")
print("=" * 70)

# The maximum R_screen on the grid
max_R_all_cutoffs = max(results[cn]['max_R'] for cn in results)
print(f"\n  Maximum R_screen across all cutoffs (angular scan): {max_R_all_cutoffs:.4f}")
print(f"  Maximum R_screen on 2D grid (heat kernel): {max_R:.4f}")

# However, the angular scan used the gradient ratio which can be infinite
# at the zero-crossing of da2. The physically meaningful quantity is the
# grid-based R_screen which includes the full Taylor expansion.

# The STRUCTURAL finding: grad(S) and grad(a2) are nearly parallel on the
# volume-preserving surface. The misalignment is tiny (< 0.05 degrees for
# all cutoffs). This means there is NO direction on the surface where
# S changes much faster than a2.

# Compute the definitive R_screen: along the direction of maximum
# gradient of S on the surface
for cutoff_name, cfg in cutoff_configs.items():
    alpha_param = cfg['alpha']
    beta_param = cfg['f0_f4']
    grad_S_2d = beta_param * grad_a0[1:3] + alpha_param * grad_a2[1:3] + grad_a4[1:3]
    grad_a2_2d = grad_a2[1:3]
    n_max = grad_S_2d / np.linalg.norm(grad_S_2d)
    dS_max = np.dot(grad_S_2d, n_max)
    da2_max = np.dot(grad_a2_2d, n_max)
    R_max_dir = abs(dS_max) / abs(da2_max)
    print(f"  {cfg['label']:30s}: R_along_gradS = {R_max_dir:.4f}")

# Compare with Jensen line value
R_jensen_s60 = float(dim_data['screening_ratio_final'])
print(f"\n  S60 Jensen-line R_screen = {R_jensen_s60:.4f}")
print(f"  Maximum off-Jensen R_screen (gradient-based) = {max_R_all_cutoffs:.4f}")

# Determine verdict
if max_R_all_cutoffs > 1e4:
    verdict = "PASS"
    detail = f"max R_screen = {max_R_all_cutoffs:.1f} > 10^4"
elif max_R_all_cutoffs < 100:
    verdict = "FAIL"
    detail = f"max R_screen = {max_R_all_cutoffs:.1f} < 100"
else:
    verdict = "INFO"
    detail = f"max R_screen = {max_R_all_cutoffs:.1f} in [100, 10^4]"

# BUT: the angular scan's "max" is misleading because it occurs at the
# zero-crossing of da2. The physical R_screen at any finite displacement
# is bounded by the gradient alignment.
# The REAL verdict should use the gradient alignment angle.

# Recompute using the most optimistic cutoff
best_cutoff = max(cutoff_configs.keys(),
                  key=lambda cn: results[cn]['max_R'])
R_best = results[best_cutoff]['max_R']

# Physical R_screen: at the zero-crossing, R diverges but the absolute
# change |da2| also goes to zero. The ratio |dS|/|da2| is unbounded
# but meaningless at eps=0. At finite displacement eps=dsig=0.005:
alpha_hk = cutoff_configs['heat_kernel']['alpha']
beta_hk = cutoff_configs['heat_kernel']['f0_f4']
grad_S_full_hk = beta_hk * grad_a0 + alpha_hk * grad_a2 + grad_a4

# Find direction where da2 = 0 on surface (exactly perpendicular to grad_a2)
grad_a2_2d = grad_a2[1:3]
n_perp = np.array([-grad_a2_2d[1], grad_a2_2d[0]])
n_perp = n_perp / np.linalg.norm(n_perp)
n_perp_3d = np.array([0.0, n_perp[0], n_perp[1]])

# At eps=0.005 along this direction:
eps_test = 0.005
delta_a2_perp = (np.dot(grad_a2, n_perp_3d) * eps_test +
                 0.5 * (n_perp_3d @ H_a2 @ n_perp_3d) * eps_test**2)
delta_S_perp = (np.dot(grad_S_full_hk, n_perp_3d) * eps_test +
                0.5 * (n_perp_3d @ (beta_hk*H_a0 + alpha_hk*H_a2 + H_a4) @ n_perp_3d) * eps_test**2)

R_physical = abs(delta_S_perp / S_heat_at_fold) / abs(delta_a2_perp / a2_at_fold)
print(f"\n  Physical R_screen at eps=0.005 along grad(a2)-perp direction:")
print(f"    |delta_a2/a2| = {abs(delta_a2_perp/a2_at_fold):.6e}")
print(f"    |delta_S/S| = {abs(delta_S_perp/S_heat_at_fold):.6e}")
print(f"    R_physical = {R_physical:.4f}")

# The definitive answer: along the steepest gradient direction on the surface
# (which is approximately the sigma direction since |da2/dsig| >> |da2/dd1|):
grad_S_2d_hk = beta_hk * grad_a0[1:3] + alpha_hk * grad_a2[1:3] + grad_a4[1:3]
R_along_gradS = np.linalg.norm(grad_S_2d_hk) / np.linalg.norm(grad_a2_2d)
print(f"\n  R_screen along grad(S) direction on surface = {R_along_gradS:.4f}")

# The gradient ratio gives the screening at infinitesimal displacement.
# This is the meaningful physical quantity.
R_definitive = R_along_gradS

if R_definitive > 1e4:
    verdict = "PASS"
    detail = f"R_screen = {R_definitive:.1f} > 10^4 along steepest direction"
elif R_definitive < 100:
    verdict = "FAIL"
    detail = f"R_screen = {R_definitive:.1f} < 100 along steepest direction"
else:
    verdict = "INFO"
    detail = f"R_screen = {R_definitive:.1f} in [100, 10^4] along steepest direction"

print(f"\n  *** VERDICT: {verdict} ***")
print(f"  *** {detail} ***")

# =============================================================================
# 13. Save results
# =============================================================================
np.savez(data_dir / 's61_offjensen_screening.npz',
    # Grid data
    sig_grid=sig_grid, d1_grid=d1_grid,
    a2_surface=a2_surface, a4_surface=a4_surface, a0_surface=a0_surface,
    S_surface=S_surface,
    frac_da2=frac_da2, frac_dS=frac_dS,
    R_screen_grid=R_screen_grid,
    # Angular scan data
    theta_arr=theta_arr,
    R_screen_heat=results['heat_kernel']['R_screen'],
    R_screen_chi8=results['chi8']['R_screen'],
    # Fold values
    a0_fold=a0_at_fold, a2_fold=a2_at_fold, a4_fold=a4_at_fold,
    S_fold=S_heat_at_fold,
    # Gradients on surface
    grad_a0_surf=grad_a0_surf, grad_a2_surf=grad_a2_surf,
    grad_a4_surf=grad_a4_surf, grad_Sheat_surf=grad_Sheat_surf,
    # Hessians (projected)
    H_a2_proj=H_a2_proj, H_a4_proj=H_a4_proj,
    # Key results
    R_definitive=R_definitive,
    R_jensen_s60=R_jensen_s60,
    R_physical_perp=R_physical,
    max_R_angular=max_R_all_cutoffs,
    max_R_grid=max_R,
    # Gate
    gate_name='OFFJ-SCREEN-61',
    gate_verdict=verdict,
    gate_detail=detail,
)
print(f"\nSaved: {data_dir / 's61_offjensen_screening.npz'}")

# =============================================================================
# 14. Plots
# =============================================================================
fig, axes = plt.subplots(2, 2, figsize=(14, 12))
fig.suptitle('S61: Off-Jensen Screening Ratio on Volume-Preserving Surface',
             fontsize=14, fontweight='bold')

# Panel 1: R_screen grid (heat kernel)
ax = axes[0, 0]
# Clip for visualization
R_plot = np.clip(R_screen_grid, 0, 200)
im = ax.pcolormesh(sig_grid, d1_grid, R_plot, cmap='hot_r', shading='auto')
plt.colorbar(im, ax=ax, label=r'$R_{\rm screen}$')
ax.set_xlabel(r'$\sigma$ (off-Jensen, u(2) anisotropy)')
ax.set_ylabel(r'$\delta_1$ (C$^2$ anisotropy)')
ax.set_title(f'Heat kernel: max $R_{{\\rm screen}}$ = {max_R:.1f}')
ax.plot(0, 0, 'w+', ms=10, mew=2)  # fold point
# Draw the grad(a2) direction
scale = 0.005
ax.arrow(0, 0, scale*grad_a2[1]/np.linalg.norm(grad_a2[1:3]),
         scale*grad_a2[2]/np.linalg.norm(grad_a2[1:3]),
         color='cyan', width=0.0002, head_width=0.001, label=r'$\nabla a_2$')
# Draw the grad(S) direction
grad_S_hk = beta_hk * grad_a0 + alpha_hk * grad_a2 + grad_a4
ax.arrow(0, 0, scale*grad_S_hk[1]/np.linalg.norm(grad_S_hk[1:3]),
         scale*grad_S_hk[2]/np.linalg.norm(grad_S_hk[1:3]),
         color='lime', width=0.0002, head_width=0.001, label=r'$\nabla S$')
ax.legend(fontsize=8, loc='upper right')

# Panel 2: Angular scan
ax = axes[0, 1]
for cutoff_name, cfg in cutoff_configs.items():
    R_ang = results[cutoff_name]['R_screen']
    ax.semilogy(np.degrees(theta_arr), R_ang, label=cfg['label'], alpha=0.8)
ax.set_xlabel(r'Angle $\theta$ on volume-preserving surface (deg)')
ax.set_ylabel(r'$R_{\rm screen}(\theta)$')
ax.set_title('Angular scan of screening ratio')
ax.axhline(100, color='orange', linestyle='--', alpha=0.5, label='FAIL threshold')
ax.axhline(1e4, color='red', linestyle='--', alpha=0.5, label='PASS threshold')
ax.axhline(R_jensen_s60, color='blue', linestyle=':', alpha=0.5, label=f'Jensen = {R_jensen_s60:.1f}')
ax.legend(fontsize=7, loc='upper right')
ax.set_xlim(0, 360)

# Panel 3: Fractional changes on surface
ax = axes[1, 0]
levels_a2 = np.linspace(-0.1, 0.1, 21)
cs = ax.contour(sig_grid, d1_grid, frac_da2, levels=levels_a2, cmap='RdBu_r')
ax.clabel(cs, fontsize=6)
ax.set_xlabel(r'$\sigma$')
ax.set_ylabel(r'$\delta_1$')
ax.set_title(r'$\Delta a_2 / a_2$ on volume-preserving surface')
ax.plot(0, 0, 'k+', ms=10, mew=2)

# Panel 4: Gradient alignment analysis
ax = axes[1, 1]
cutoff_labels = []
angles = []
R_along = []
for cutoff_name, cfg in cutoff_configs.items():
    alpha_param = cfg['alpha']
    beta_param = cfg['f0_f4']
    grad_S_2d = beta_param * grad_a0[1:3] + alpha_param * grad_a2[1:3] + grad_a4[1:3]
    grad_a2_2d = grad_a2[1:3]
    cos_a = np.dot(grad_S_2d, grad_a2_2d) / (
        np.linalg.norm(grad_S_2d) * np.linalg.norm(grad_a2_2d))
    sin_a = np.sqrt(1 - cos_a**2)
    angle = np.degrees(np.arcsin(sin_a))
    R_ratio = np.linalg.norm(grad_S_2d) / np.linalg.norm(grad_a2_2d)
    cutoff_labels.append(cfg['label'])
    angles.append(angle)
    R_along.append(R_ratio)

x_pos = np.arange(len(cutoff_labels))
width = 0.35  # (local)
bars1 = ax.bar(x_pos - width/2, angles, width, label='Misalignment (deg)', color='steelblue')
ax2 = ax.twinx()
bars2 = ax2.bar(x_pos + width/2, R_along, width, label=r'$R_{\rm screen}$', color='coral')
ax.set_xlabel('Cutoff function')
ax.set_ylabel('Misalignment angle (deg)', color='steelblue')
ax2.set_ylabel(r'$R_{\rm screen} = |\nabla S|/|\nabla a_2|$', color='coral')
ax.set_xticks(x_pos)
ax.set_xticklabels([l.replace('$', '').replace('\\', '') for l in cutoff_labels],
                   fontsize=7, rotation=15)
ax.set_title('Gradient alignment & screening ratio')
lines1, labels1 = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax.legend(lines1 + lines2, labels1 + labels2, fontsize=8, loc='upper left')

plt.tight_layout()
plt.savefig(data_dir / 's61_offjensen_screening.png', dpi=150, bbox_inches='tight')
print(f"Saved: {data_dir / 's61_offjensen_screening.png'}")

elapsed = time.time() - t0
print(f"\nTotal computation time: {elapsed:.1f}s")
print("\nDone.")
