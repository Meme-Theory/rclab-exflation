#!/usr/bin/env python3
"""
SKYRMION-BARYON-64: Skyrmion Physics on Jensen-Deformed SU(3) Fiber
====================================================================

Gen-Physicist — Session 64, Wave 7

PHYSICS:
--------
pi_3(SU(3)) = Z gives integer-winding topological solitons (skyrmions) on the
SU(3) fiber. These carry a conserved topological charge B in Z that is a
candidate for baryon number.

The Skyrme energy functional on the compact internal space M = SU(3):

    E = integral_M [ -(f_pi^2/16) Tr(L_mu L^mu)
                     + (1/(32 e^2)) Tr([L_mu, L_nu]^2) ] sqrt(g) d^8x

where L_mu = U^{-1} partial_mu U is the left-invariant Maurer-Cartan form,
U: M -> SU(3) is the chiral field, and g is the Jensen-deformed metric.

MAPPING TO SPECTRAL ACTION:
  f_pi^2 ~ a_2  (gravitational/scalar curvature stiffness)
  1/e^2  ~ a_4  (Yang-Mills/gauge kinetic stiffness)

Both a_2 and a_4 are Seeley-DeWitt coefficients of the Dirac operator D_K.

For SU(N) skyrmions, the hedgehog ansatz gives:
  M_skyrm = C_N * f_pi / e      (mass)
  R_skyrm = 1 / (e * f_pi)      (size)
  B = winding number in pi_3(SU(3))

where C_N is a numerical coefficient depending on the internal geometry.
For SU(2) flat space: C_2 = 12*pi^2 (Adkins-Nappi-Witten 1983).
For SU(3): the embedding SU(2) -> SU(3) gives the same pi_3 topology,
but the compact curved geometry modifies the coefficient.

KIBBLE-ZUREK PRODUCTION:
During the cosmological transit through the fold (tau: 0 -> 0.19),
the order parameter field must choose a vacuum orientation at each
spacetime point. Causally disconnected domains choose independently,
producing topological defects (skyrmions) at domain boundaries.

The KZ density:
  n_defect ~ (tau_Q / tau_0)^{-d*nu/(1+z*nu)}
where tau_Q is quench time, tau_0 relaxation time, d is effective
dimensionality for defect production, nu and z are critical exponents.

Baryon asymmetry:
  eta_B = n_skyrm * B / s
where s is entropy density. The KEY question: does the transit produce
a NET baryon number, or equal skyrmions and anti-skyrmions?
Skyrmion-antiskyrmion asymmetry requires CP violation during production.

GATE: SKYRMION-BARYON-64
  PASS: M_skyrm within 2 OOM of proton mass (0.938 GeV) AND
        eta_B within 3 OOM of 6e-10
  FAIL: M_skyrm > 5 OOM off OR eta_B > 10 OOM off
  INFO: otherwise

Author: gen-physicist
Session: S64 W7-E
"""

import os
import sys
import time
import numpy as np
from scipy.optimize import minimize_scalar
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# ---------------------------------------------------------------
# Setup
# ---------------------------------------------------------------
PROJECT_ROOT = r'C:\sandbox\Ainulindale Exflation'
SCRIPT_DIR = os.path.join(PROJECT_ROOT, 'computations')
sys.path.insert(0, SCRIPT_DIR)

_LOG_PATH = os.path.join(SCRIPT_DIR, 's64_skyrmion_baryon_output.txt')
class _Tee:
    def __init__(self, *streams):
        self.streams = streams
    def write(self, data):
        for s in self.streams:
            s.write(data)
            s.flush()
    def flush(self):
        for s in self.streams:
            s.flush()

_log_file = open(_LOG_PATH, 'w', encoding='utf-8')
sys.stdout = _Tee(sys.__stdout__, _log_file)
sys.stderr = _Tee(sys.__stderr__, _log_file)

from canonical_constants import (
    # Spectral action coefficients
    a0_fold, a2_fold, a4_fold,
    # Geometric
    tau_fold, Vol_SU3_Haar,
    g0_diag,
    # KK scale
    M_KK, M_KK_gravity, M_KK_kerner,
    # Transit
    dt_transit, v_terminal, omega_tau, H_fold,
    # BCS / quasiparticle
    n_pairs, E_cond, Delta_0_OES, N_dof_BCS,
    E_B1, E_B2_mean, E_B3_mean,
    # Fabric
    N_cells, J_C2, T_acoustic, c_fabric,
    xi_BCS, xi_GL,
    # Cosmological
    eta_BBN_obs, M_Pl_reduced, rho_Lambda_obs,
    Omega_b, Omega_m, T_CMB_GeV,
    A_s_CMB, H_0_GeV,
    # Fundamental
    PI,
    # Gauge
    g_SU2_fold, alpha2_MKK_inv,
    # IBO
    IBO_ratio,
    # CP phase
    phi_CP,
)

t0 = time.time()

print("=" * 78)
print("SKYRMION-BARYON-64: Skyrmion Physics on Jensen-Deformed SU(3) Fiber")
print("=" * 78)

# =============================================================================
# SECTION 1: SU(3) Geometry at the Fold
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 1: SU(3) Geometry with Jensen Deformation at tau_fold")
print("=" * 78)

# Jensen deformation: metric on SU(3) with anisotropy parameter tau
# The metric is left-invariant, with the Cartan subalgebra directions
# (H_3, H_8 generators) scaled by exp(tau) relative to the coset directions.
#
# For volume-preserving Jensen deformation on SU(3):
#   - dim SU(3) = 8
#   - Cartan subalgebra dim = 2 (rank 2)
#   - Root space dim = 6
#   - Volume preserved: det(g) = const
#
# The metric eigenvalues at the fold (tau = 0.19):
#   2 Cartan directions: scale factor exp(2*tau) = exp(0.38)
#   6 root directions: scale factor exp(-2*tau/3) = exp(-0.1267)
#   (Volume preservation: 2*(2*tau) + 6*(-2*tau/3) = 0)

tau = tau_fold
scale_cartan = np.exp(2 * tau)       # Cartan directions stretched
scale_root = np.exp(-2 * tau / 3)    # Root directions compressed

print(f"\ntau_fold = {tau_fold}")
print(f"Scale factor (Cartan, 2 dirs): {scale_cartan:.6f}")
print(f"Scale factor (Root, 6 dirs):   {scale_root:.6f}")
print(f"Volume check: exp(2*2*tau + 6*(-2*tau/3)) = {np.exp(2*2*tau + 6*(-2*tau/3)):.15f}")

# Effective radii in M_KK^{-1} units
# The round SU(3) has all directions with the same radius R_0
# From Vol_SU3_Haar = (8*sqrt(3)*pi^4) * R_0^8, solve for R_0
R_0 = (Vol_SU3_Haar / (8 * np.sqrt(3) * PI**4))**(1.0/8)
# This gives R_0 = 1 by construction (it's the normalization of the Killing metric)
# But we need the PHYSICAL radius in M_KK^{-1}
# M_KK = 1/R_phys, so R_phys = 1/M_KK and R_0 = 1 in M_KK^{-1} units
R_phys_MKK = 1.0  # M_KK^{-1}  # (local)

print(f"\nR_0 (Killing normalization) = {R_0:.6f}")
print(f"R_phys = 1/M_KK = {R_phys_MKK} M_KK^{{-1}}")

# Effective radii after Jensen deformation
R_cartan = R_phys_MKK * np.sqrt(scale_cartan)
R_root = R_phys_MKK * np.sqrt(scale_root)
print(f"R_cartan = {R_cartan:.6f} M_KK^{{-1}}")
print(f"R_root = {R_root:.6f} M_KK^{{-1}}")

# Scalar curvature at the fold (from S64 W1-A result)
# R(tau) = -0.25*exp(-4*tau) + 2.0*exp(-tau) - 0.25 + 0.5*exp(2*tau)
R_scalar_norm = (-0.25*np.exp(-4*tau) + 2.0*np.exp(-tau)
                 - 0.25 + 0.5*np.exp(2*tau))
print(f"R_scalar (normalized) = {R_scalar_norm:.6f}")
print(f"a_2(fold) = {a2_fold:.4f}")
print(f"a_4(fold) = {a4_fold:.4f}")

# =============================================================================
# SECTION 2: Skyrme Model Parameters from Spectral Action
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 2: Mapping Skyrme Parameters to Spectral Action")
print("=" * 78)

# The spectral action on M^4 x F (F = SU(3) fiber) gives:
#   S = f_4 * Lambda^8 * a_0 + f_2 * Lambda^6 * a_2 + f_0 * Lambda^4 * a_4 + ...
#
# The a_2 coefficient controls the Einstein-Hilbert term:
#   S_EH = (1/16*pi*G_N) * integral R sqrt(g) d^4x
# so f_pi^2 ~ a_2 provides the "pion decay constant" in Skyrme language.
#
# The a_4 coefficient controls the Yang-Mills term:
#   S_YM = (1/4*g_YM^2) * integral Tr(F^2) sqrt(g) d^4x
# so 1/e^2 ~ a_4 provides the Skyrme stabilizing term.
#
# Dimensional analysis in M_KK units:
#   [f_pi^2] = [energy/length^6] on 8D manifold
#   [1/e^2] = [1/(energy*length^2)] on 8D manifold
#
# The Skyrme energy E = integral [sigma-model + Skyrme term] d^8x
# On the compact 8D fiber, the sigma-model term scales as f_pi^2 * R^6
# and the Skyrme term scales as (1/e^2) * R^4.
# In M_KK units on the fiber:
#   f_pi^2 = a_2  (dimensionless, in M_KK^2 * M_KK^{-8} -> M_KK^{-6} volume)
#   1/e^2 = a_4   (dimensionless, similar)
#
# For the Skyrme model on a COMPACT manifold, the variational profile
# is not a hedgehog that extends to infinity -- it wraps the manifold.
# The skyrmion FILLS the manifold (or a significant fraction of it).

# The key insight for compact manifolds: the sigma-model term and Skyrme
# term compete. On a manifold of size R:
#   E_sigma ~ f_pi^2 * R^(d-2)  (sigma model kinetic energy)
#   E_skyrme ~ (1/e^2) * R^(d-4)  (Skyrme stabilizer)
# For d = 8 (SU(3) fiber):
#   E_sigma ~ f_pi^2 * R^6
#   E_skyrme ~ (1/e^2) * R^4
#
# But since the manifold is compact and the skyrmion WRAPS it,
# the variational parameter is not the skyrmion size but the
# profile function F(r) on the manifold.

# Map to spectral action parameters
f_pi_sq = a2_fold  # Gravitational stiffness (M_KK units)
inv_e_sq = a4_fold  # Yang-Mills stiffness (M_KK units)

f_pi = np.sqrt(f_pi_sq)
e_skyrme = 1.0 / np.sqrt(inv_e_sq)

print(f"\nf_pi^2 = a_2(fold) = {f_pi_sq:.4f} M_KK^2")
print(f"1/e^2 = a_4(fold) = {inv_e_sq:.4f} M_KK^{{-2}}")
print(f"f_pi = sqrt(a_2) = {f_pi:.4f} M_KK")
print(f"e = 1/sqrt(a_4) = {e_skyrme:.4f}")
print(f"f_pi / e = sqrt(a_2 * a_4) = {f_pi * e_skyrme:.4f} M_KK (NOT USED)")
print(f"f_pi * e = sqrt(a_2 / a_4) = {f_pi / e_skyrme:.4f} M_KK (NOT USED)")

# =============================================================================
# SECTION 3: Skyrmion on Compact SU(3) — Exact Topological Charge
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 3: Topological Charge and Winding Number")
print("=" * 78)

# pi_3(SU(3)) = Z
# The generator is the embedding SU(2) -> SU(3) via
#   U(x) = [[u(x), 0], [0, 1]] where u: S^3 -> SU(2)
#
# The winding number (baryon number) is:
#   B = (1/(24*pi^2)) * integral Tr(L wedge L wedge L)
#
# where L = U^{-1} dU is the Maurer-Cartan form pulled back to the
# 3-sphere embedded in SU(3).
#
# For the identity map S^3 -> SU(2) -> SU(3), B = 1 exactly.
# This is a TOPOLOGICAL INVARIANT — it does not depend on the metric.
#
# On the compact SU(3) manifold, the skyrmion wraps a 3-cycle.
# SU(3) has H_3(SU(3); Z) = Z (same pi_3), so the winding is well-defined.
# The relevant 3-cycle is the SU(2) subgroup.

B_skyrmion = 1  # Unit winding number
print(f"\nBaryon number B = {B_skyrmion} (topological, exact)")
print(f"pi_3(SU(3)) = Z")
print(f"H_3(SU(3); Z) = Z")
print(f"The 3-cycle is the embedded SU(2) subgroup.")

# =============================================================================
# SECTION 4: Skyrmion Mass — Faddeev-Bogomolny Bound and Variational
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 4: Skyrmion Mass on Compact SU(3)")
print("=" * 78)

# METHOD A: Faddeev-Bogomolny topological bound
# For any Skyrme-like model, there is a rigorous lower bound:
#   E >= C * |B| * f_pi / e
# where C depends on the manifold geometry.
#
# For SU(2) in flat R^3: C_flat = 12*pi^2 = 118.435
# The Bogomolny bound is saturated only for the BPS skyrmion
# (which requires additional terms). The hedgehog in flat space
# has E = 1.232 * 12*pi^2 * f_pi/e (23.2% above bound).

C_flat = 12 * PI**2
print(f"\nFaddeev-Bogomolny coefficient (flat R^3): C_flat = 12*pi^2 = {C_flat:.4f}")

# On compact SU(3), we need to account for:
# 1. The SU(2) submanifold has volume Vol(S^3) = 2*pi^2 * R_eff^3
# 2. The Jensen deformation stretches/compresses different directions
# 3. The skyrmion profile is constrained by the manifold size

# The SU(2) subgroup in SU(3) involves 3 generators.
# For the standard embedding SU(2) -> SU(3) (isospin subgroup),
# we take T_1, T_2, T_3 = lambda_1/2, lambda_2/2, lambda_3/2.
# These are root directions (2) + Cartan direction (1).
# Under Jensen deformation:
#   T_1, T_2: root directions, scale factor exp(-2*tau/3)
#   T_3: Cartan direction, scale factor exp(2*tau)

# The SU(2) sub-3-sphere has an effective metric that is anisotropic.
# Its volume is:
#   Vol(SU(2)_embedded) = Vol(S^3) * (R_root^2 * R_cartan)
# normalized to the round S^3 case.

Vol_S3_round = 2 * PI**2  # Volume of unit S^3

# The SU(2) isospin subgroup involves directions:
# Two root directions (e.g., e_alpha for root alpha = e_1 - e_2)
# and one Cartan direction (H_3).
# With Jensen deformation, the metric on the 3D submanifold is:
#   ds^2 = scale_root * (dx_1^2 + dx_2^2) + scale_cartan * dx_3^2
# Volume element: sqrt(scale_root^2 * scale_cartan) * d^3x

vol_factor = scale_root * np.sqrt(scale_cartan)
# vol_factor^{3/2} gives the full volume scaling for the 3-sphere
R_eff_SU2 = (scale_root**(2/3) * scale_cartan**(1/3))  # Effective radius scaling
Vol_SU2_embedded = Vol_S3_round * R_eff_SU2**3
print(f"\nSU(2) embedding (isospin):")
print(f"  2 root dirs: scale = {scale_root:.6f}")
print(f"  1 Cartan dir: scale = {scale_cartan:.6f}")
print(f"  Volume factor: {vol_factor:.6f}")
print(f"  R_eff = {R_eff_SU2:.6f} R_0")
print(f"  Vol(SU(2)) = {Vol_SU2_embedded:.4f} (in M_KK^{{-3}} units)")

# METHOD B: Skyrme energy on compact manifold
#
# On a 3-sphere of radius R (embedded in 8D), the B=1 hedgehog profile is:
#   U(chi) = exp(i * F(chi) * sigma_r)
# where chi is the polar angle (0 to pi) and F(chi) = pi - chi (identity map).
#
# The sigma-model energy density:
#   T_2 = -(f_pi^2/16) Tr(L_i L^i)
#       = (f_pi^2/2) * [(dF/dchi)^2 + 2*sin^2(F)/sin^2(chi)]
# integrated over the 3-sphere with measure sin^2(chi) * dchi * dOmega_2
#
# The Skyrme term energy density:
#   T_4 = (1/(32*e^2)) Tr([L_i, L_j]^2)
#       = (1/(2*e^2)) * sin^2(F)/sin^2(chi) *
#         [(dF/dchi)^2 + sin^2(F)/(2*sin^2(chi))]
#
# For F(chi) = pi - chi (identity map = B=1 skyrmion on S^3):
#   sin(F) = sin(chi), dF/dchi = -1
#
# The integrals become:
#   E_sigma = f_pi^2 * pi * integral_0^pi [1 + 2] * sin^2(chi) dchi
#           = 3 * f_pi^2 * pi * (pi/2)
#           = (3/2) * pi^2 * f_pi^2
#
#   E_skyrme = (1/e^2) * pi * integral_0^pi [1 + 1/2] * sin^2(chi)/(sin^2(chi)) dchi
#            = (3/(2*e^2)) * pi * pi
#            = (3/2) * pi^2 / e^2
#
# Wait — let me be more careful. The hedgehog on S^3 of radius R:
#
# For F(chi) = pi - chi on S^3 of radius R:
#   E_2 = (f_pi^2/(2*R)) * 4*pi * integral_0^pi [F'^2 + 2*sin^2(F)/sin^2(chi)]
#         * sin^2(chi) * R^3 * dchi / R^2
#       ... let me just compute this numerically.

# Numerical integration of the Skyrme energy on S^3
# Using dimensionless variable chi in [0, pi]
# F(chi) = pi - chi (identity map)

N_grid = 10000  # (local)
chi = np.linspace(1e-10, PI - 1e-10, N_grid)
dchi = chi[1] - chi[0]

F_profile = PI - chi  # Identity map
dF = -np.ones_like(chi)  # dF/dchi = -1
sinF = np.sin(F_profile)  # = sin(chi)
sinChi = np.sin(chi)

# Energy densities (dimensionless integrands)
# Sigma-model term: (f_pi^2/2) * R^3 * [F'^2 + 2*sin^2(F)/sin^2(chi)]
#   * sin^2(chi) * 4*pi * dchi / R
# On S^3 of radius R, the energy is:
# E_2 = (f_pi^2/2) * (4*pi) * R * integral [F'^2 + 2*sin^2F/sin^2chi] sin^2chi dchi
#
# But on the compact fiber, R = R_eff * R_phys_MKK, and R_phys = 1/M_KK
# So R is O(1) in M_KK^{-1} units.

# For the anisotropic metric, we introduce effective radii along each direction.
# The SU(2) sub-3-sphere has two root directions (R_root) and one Cartan (R_cartan).
# The hedgehog wraps all three directions, so we need the anisotropic energy.
#
# For an anisotropic S^3 with radii (a, a, b):
# The sigma-model term becomes:
#   E_2 = (f_pi^2/2) * 4*pi * integral_0^pi [
#     (1/b^2) * F'^2 + (1/a^2 + 1/(a*b)) * sin^2(F)/sin^2(chi)
#   ] * a^2 * b * sin^2(chi) dchi
#
# But let us first compute the ISOTROPIC case on S^3 of radius R=1 (M_KK^{-1}),
# then account for the anisotropy as a correction.

# ISOTROPIC S^3, radius R (in M_KK^{-1}):
# E_2[isotropic] = (f_pi^2 / (2*R)) * 4*pi * integral_0^pi [F'^2 + 2*sin^2F/sin^2chi]
#                   * sin^2(chi) * dchi
#
# Wait, let me get the dimensions right. On S^3 of radius R:
# ds^2 = R^2 * [dchi^2 + sin^2(chi) * dOmega_2^2]
# Vol(S^3) = 2*pi^2 * R^3
# The Skyrme field U(chi, theta, phi): S^3 -> SU(2)
# L_i = U^{-1} partial_i U (i = 1,2,3 are coordinates on S^3)
#
# In the hedgehog ansatz: U = exp(i*F(chi)*sigma_r)
# L_chi = i*F'*sigma_r, L_theta = ..., L_phi = ...
#
# The energy functional:
# E = integral d^3x sqrt(g) [-(f_pi^2/16) Tr(L_i L^i) + (1/(32 e^2)) Tr([L_i,L_j]^2)]
#
# For hedgehog on S^3 of radius R:
# -(f_pi^2/16) * Tr(L_i L^i) = (f_pi^2/2) * [F'^2/R^2 + 2*sin^2(F)/(R^2*sin^2(chi))]
# (1/(32*e^2)) * Tr([L_i,L_j]^2) = (1/e^2) * sin^2(F)/(R^4*sin^2(chi)) *
#                                     [F'^2 + sin^2(F)/(2*sin^2(chi))]
#
# sqrt(g) d^3x = R^3 * sin^2(chi) * sin(theta) * dchi * dtheta * dphi
# = R^3 * sin^2(chi) * 4*pi * dchi (after theta, phi integration)
#
# So:
# E = 4*pi * integral_0^pi {
#     (f_pi^2/2) * R * [F'^2 + 2*sin^2F/sin^2chi]
#   + (1/e^2) * (1/R) * sin^2F/sin^2chi * [F'^2 + sin^2F/(2*sin^2chi)]
# } * sin^2(chi) * dchi

# For F(chi) = pi - chi:
integrand_sigma = (dF**2 + 2 * sinF**2 / sinChi**2) * sinChi**2
integrand_skyrme = (sinF**2 / sinChi**2) * (
    dF**2 + sinF**2 / (2 * sinChi**2)
) * sinChi**2

# Since sin(F) = sin(pi-chi) = sin(chi) for F = pi - chi:
# sinF/sinChi = 1, so integrand_sigma = (1 + 2) * sin^2(chi) = 3*sin^2(chi)
# integrand_skyrme = 1 * (1 + 1/2) = 3/2

I_sigma = np.trapezoid(integrand_sigma, chi)
I_skyrme = np.trapezoid(integrand_skyrme, chi)

# Analytic values:
I_sigma_exact = 3 * PI / 2  # integral_0^pi 3*sin^2(chi) dchi = 3*pi/2
I_skyrme_exact = 3 * PI / 4  # integral_0^pi (3/2)*sin^2(chi) dchi = 3*pi/4

print(f"\n--- Isotropic S^3 hedgehog (F = pi - chi) ---")
print(f"I_sigma  = {I_sigma:.6f}  (exact: {I_sigma_exact:.6f}, err: {abs(I_sigma-I_sigma_exact)/I_sigma_exact:.2e})")
print(f"I_skyrme = {I_skyrme:.6f}  (exact: {I_skyrme_exact:.6f}, err: {abs(I_skyrme-I_skyrme_exact)/I_skyrme_exact:.2e})")

# Energy on isotropic S^3 of radius R:
# E_iso(R) = 4*pi * [(f_pi^2/2) * R * I_sigma + (1/e^2) * (1/R) * I_skyrme]
# E_iso(R) = 2*pi * f_pi^2 * R * I_sigma + 4*pi * I_skyrme / (e^2 * R)
#
# Minimizing over R:
# dE/dR = 2*pi * f_pi^2 * I_sigma - 4*pi * I_skyrme / (e^2 * R^2) = 0
# => R_opt^2 = 2 * I_skyrme / (f_pi^2 * e^2 * I_sigma)
# Since I_sigma = I_skyrme = 3*pi/2:
# R_opt^2 = 2 / (f_pi^2 * e^2) = 2 / (a_2 * 1/a_4) = 2*a_4 / a_2
# R_opt = sqrt(2*a_4/a_2)

# BUT: on the compact fiber, R is FIXED (it's 1/M_KK). The skyrmion cannot
# choose its size freely — it must fit on the manifold. So we evaluate at R=1:

R_S3 = 1.0  # Fiber radius in M_KK^{-1}  # (local)

def E_skyrm_isotropic(R):
    """Skyrmion energy on S^3 of radius R (M_KK^{-1}), in M_KK units."""
    return 4 * PI * (f_pi_sq / 2 * R * I_sigma_exact
                     + (1.0 / (e_skyrme**2 * R)) * I_skyrme_exact)

# Optimal size in flat space
R_opt = np.sqrt(2 * I_skyrme_exact / (f_pi_sq * e_skyrme**2 * I_sigma_exact))
print(f"\nOptimal skyrmion radius (flat space): R_opt = {R_opt:.6f} M_KK^{{-1}}")
print(f"  = {R_opt:.4f} / M_KK")

# Energy at the compact fiber radius R = 1/M_KK
E_iso_R1 = E_skyrm_isotropic(R_S3)
E_at_Ropt = E_skyrm_isotropic(R_opt)

print(f"\nE_skyrmion(R=1 M_KK^{{-1}}) = {E_iso_R1:.4f} M_KK")
print(f"E_skyrmion(R_opt) = {E_at_Ropt:.4f} M_KK  (minimum, flat-space analogue)")

# Bogomolny bound: E >= 12*pi^2 * f_pi/e * |B|
E_bogomolny = 12 * PI**2 * f_pi / e_skyrme
print(f"Bogomolny bound (flat): {E_bogomolny:.4f} M_KK")

# =============================================================================
# SECTION 5: Anisotropic Correction (Jensen Deformation)
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 5: Anisotropic Correction from Jensen Deformation")
print("=" * 78)

# The SU(2) subgroup sits in the 2 root + 1 Cartan directions.
# The anisotropy modifies the energy through the effective radii.
# The sigma-model part gets contributions from each direction weighted
# by the metric:
#   E_2^aniso = 4*pi * (f_pi^2/2) * integral [
#     (1/R_cartan) * F'^2 + (1/R_root^2) * R_cartan * 2*sin^2F/sin^2chi
#   ] * R_root^2 * R_cartan * sin^2(chi) dchi
#
# For the hedgehog on anisotropic S^3 with radii (a, a, b):
# (a = R_root = sqrt(scale_root), b = R_cartan = sqrt(scale_cartan))
# Two "transverse" (root) directions have curvature radius a
# One "longitudinal" (Cartan) direction has radius b
#
# The hedgehog wraps the longitude direction (chi) with radius b, and the
# transverse directions with radius a. The metric on the anisotropic S^3:
#   ds^2 = b^2 dchi^2 + a^2 sin^2(chi) dOmega_2^2
#
# Volume element: a^2 * b * sin^2(chi) * sin(theta) dchi dtheta dphi
# = 4*pi * a^2 * b * sin^2(chi) dchi
#
# Energy:
# E_2 = 4*pi * (f_pi^2/2) * integral [
#   (F'^2 / b^2) * (a^2 * b) + (2*sin^2F/(a^2*sin^2chi)) * (a^2 * b)
# ] * sin^2(chi) dchi
# = 4*pi * (f_pi^2/2) * integral [
#   (a^2 / b) * F'^2 + (2*b / 1) * sin^2F/sin^2chi
# ] * sin^2(chi) dchi
#
# E_4 = 4*pi * (1/e^2) * integral [
#   sin^2F/(a^2*sin^2chi) * (F'^2/b^2 + sin^2F/(2*a^2*sin^2chi))
# ] * a^2 * b * sin^2(chi) dchi
# = 4*pi * (1/e^2) * integral [
#   sin^2F/sin^2chi * (b/b^2 * F'^2 + b/(2*a^2) * sin^2F/sin^2chi)
# ] * sin^2(chi) dchi
# = 4*pi * (1/e^2) * integral [
#   sin^2F/sin^2chi * (F'^2/b + sin^2F/(2*a^2*b^{-1}))
# ] dchi ...
#
# Let me just parametrize it directly.

a_radius = R_root     # sqrt(scale_root) * R_0
b_radius = R_cartan   # sqrt(scale_cartan) * R_0

print(f"\nAnisotropic S^3 radii:")
print(f"  a (root, 2 dirs) = {a_radius:.6f} M_KK^{{-1}}")
print(f"  b (Cartan, 1 dir) = {b_radius:.6f} M_KK^{{-1}}")

# For F = pi - chi (identity map) on anisotropic S^3(a, a, b):
# Volume: 2*pi^2 * a^2 * b
Vol_SU2_aniso = 2 * PI**2 * a_radius**2 * b_radius
print(f"  Vol(SU(2)_aniso) = {Vol_SU2_aniso:.6f} M_KK^{{-3}}")

# E_sigma (sigma-model):
# = 4*pi * (f_pi^2/2) * [(a^2/b)*I_1 + 2*b*I_2]
# where I_1 = integral F'^2 sin^2(chi) dchi = pi/2
#       I_2 = integral sin^2(F)/sin^2(chi) * sin^2(chi) dchi
#           = integral sin^2(chi) dchi = pi/2  [for F = pi-chi]
I_1 = PI / 2  # integral_0^pi sin^2(chi) dchi
I_2 = PI / 2  # integral_0^pi sin^2(chi) dchi

E_sigma_aniso = 4 * PI * (f_pi_sq / 2) * (
    (a_radius**2 / b_radius) * I_1 + 2 * b_radius * I_2
)

# E_skyrme (stabilizer):
# On anisotropic S^3(a,a,b), the Skyrme term:
# E_4 = 4*pi * (1/e^2) * [(1/b) * I_3 + (b/(2*a^2)) * I_4]
# where I_3 = integral sin^2(F) * F'^2 / sin^2(chi) * sin^2(chi) dchi
#           = integral sin^2(chi) dchi = pi/2   [for F = pi - chi]
#       I_4 = integral sin^4(F) / sin^4(chi) * sin^2(chi) dchi
#           = integral sin^2(chi) dchi = pi/2   [for F = pi - chi, sin^4F/sin^4chi = 1]
# Actually wait: sin(F)=sin(chi), so sin^2(F)/sin^2(chi)=1, sin^4(F)/sin^4(chi)=1
I_3 = PI / 2
I_4 = PI / 2

E_skyrme_aniso = 4 * PI * (1.0 / e_skyrme**2) * (
    (1.0 / b_radius) * I_3 + (b_radius / (2 * a_radius**2)) * I_4
)

E_total_aniso = E_sigma_aniso + E_skyrme_aniso

print(f"\n--- Anisotropic skyrmion energy ---")
print(f"E_sigma  = {E_sigma_aniso:.4f} M_KK")
print(f"E_skyrme = {E_skyrme_aniso:.4f} M_KK")
print(f"E_total  = {E_total_aniso:.4f} M_KK")

# Anisotropy correction factor
aniso_ratio = E_total_aniso / E_iso_R1
print(f"Anisotropy factor E_aniso/E_iso = {aniso_ratio:.6f}")
print(f"  (Jensen deformation at tau={tau_fold} gives {(aniso_ratio-1)*100:.2f}% correction)")

# =============================================================================
# SECTION 6: Physical Skyrmion Mass in GeV
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 6: Physical Skyrmion Mass")
print("=" * 78)

# M_skyrmion = E_total * M_KK (converting from M_KK units to GeV)
# Using both M_KK routes:

M_skyrm_grav = E_total_aniso * M_KK_gravity
M_skyrm_kern = E_total_aniso * M_KK_kerner

M_proton = 0.938  # GeV  # (local)

print(f"\nM_skyrmion (gravity route) = {E_total_aniso:.4f} * {M_KK_gravity:.4e} GeV")
print(f"                           = {M_skyrm_grav:.4e} GeV")
print(f"M_skyrmion (Kerner route)  = {E_total_aniso:.4f} * {M_KK_kerner:.4e} GeV")
print(f"                           = {M_skyrm_kern:.4e} GeV")
print(f"\nM_proton = {M_proton} GeV")
print(f"\nlog10(M_skyrm_grav / M_proton) = {np.log10(M_skyrm_grav / M_proton):.2f}")
print(f"log10(M_skyrm_kern / M_proton) = {np.log10(M_skyrm_kern / M_proton):.2f}")

OOM_off_proton_grav = np.log10(M_skyrm_grav / M_proton)
OOM_off_proton_kern = np.log10(M_skyrm_kern / M_proton)

# Gate criterion 1: M_skyrm within 2 OOM of proton mass
mass_pass = abs(OOM_off_proton_grav) <= 2.0
print(f"\nGate criterion 1 (mass within 2 OOM): {'PASS' if mass_pass else 'FAIL'}")
print(f"  |log10(M_skyrm/M_proton)| = {abs(OOM_off_proton_grav):.2f} (threshold: 2.0)")

# =============================================================================
# SECTION 7: Skyrmion Size
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 7: Skyrmion Size")
print("=" * 78)

# On the compact manifold, the skyrmion fills the SU(2) sub-3-sphere.
# Its "size" is the SU(2) subgroup radius ~ 1/M_KK.
R_skyrm_MKK = 1.0 / M_KK  # meters
R_skyrm_fm = R_skyrm_MKK / 1e-15  # in fm (rough)
# More precisely: 1/M_KK in GeV^{-1}, convert to fm via hbar*c = 0.197 GeV*fm
R_skyrm_fm_grav = 0.197 / M_KK_gravity * 1e15  # fm
R_skyrm_fm_kern = 0.197 / M_KK_kerner * 1e15  # fm

R_proton = 0.84  # fm (proton charge radius)  # (local)

print(f"\nSkyrmion size = SU(2) sub-3-sphere radius ~ 1/M_KK")
print(f"R_skyrm (gravity) = {R_skyrm_fm_grav:.4e} fm")
print(f"R_skyrm (Kerner)  = {R_skyrm_fm_kern:.4e} fm")
print(f"R_proton = {R_proton} fm")
print(f"\nlog10(R_skyrm/R_proton) = {np.log10(R_skyrm_fm_grav / R_proton):.2f} (gravity)")

# =============================================================================
# SECTION 8: Kibble-Zurek Skyrmion Production
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 8: Kibble-Zurek Defect Production During Transit")
print("=" * 78)

# During the cosmological transit (tau: 0 -> 0.19), the order parameter
# must choose an orientation. Causally disconnected domains choose
# independently, creating topological defects at boundaries.
#
# KZ scaling for defect density:
#   n_defect ~ (tau_Q / tau_0)^{-d_eff * nu / (1 + z * nu)}
#
# For the transit:
#   tau_Q = dt_transit = 0.00113 M_KK^{-1} (transit duration)
#   tau_0 = 1/omega_tau = 1/8.27 = 0.121 M_KK^{-1} (relaxation time ~ transit freq)
#   Or more physically: tau_0 = 1/(2*Delta) for BCS gap
#
# But wait: what is the relevant order parameter for skyrmion formation?
# Skyrmions are topological defects in the CHIRAL field U: S^3 -> SU(3).
# The "quench" here is the BCS phase transition during transit.
# The relevant gap is the BCS gap Delta = 0.464 M_KK.
# The quench rate is omega_tau = 8.27 M_KK (much faster than gap).
#
# For the BCS phase transition, the critical exponents are mean-field:
#   nu = 1/2 (correlation length exponent)
#   z = 2 (dynamic critical exponent for dissipative dynamics)
#   OR z = 1 for ballistic (relativistic) dynamics
#
# The effective dimensionality for skyrmion production:
# Skyrmions are 0-dimensional defects (point-like) in the 3D SU(2) sub-3-sphere.
# The KZ formula for 0-dimensional defects (monopole-like):
#   n_defect ~ (tau_Q/tau_0)^{-3*nu/(1+z*nu)}
#
# But we also need to consider the full 8D fiber.
# In the compact fiber, the relevant "volume" is Vol(SU(3)).
# Defect density per fiber volume:
#   n_defect = (xi_KZ)^{-d_fiber} where xi_KZ is the KZ correlation length

print(f"\n--- Transit parameters ---")
print(f"dt_transit = {dt_transit:.6e} M_KK^{{-1}}")
print(f"omega_tau = {omega_tau} M_KK")
print(f"Delta_BCS = {Delta_0_OES:.4f} M_KK")
print(f"Adiabaticity: omega_tau/Delta = {omega_tau/Delta_0_OES:.2f} (>>1 => sudden)")

# The transit is in the SUDDEN regime (omega_tau >> Delta).
# In the sudden limit, ALL modes are excited: P_exc = 1.000 (from S38).
# The correlation length at freeze-out is:
#   xi_KZ ~ xi_0 * (tau_Q/tau_0)^{nu/(1+z*nu)}
# where xi_0 = xi_BCS = 0.808 M_KK^{-1}

# KZ correlation length
xi_0 = xi_BCS  # BCS coherence length
tau_Q = dt_transit
tau_0_gap = 1.0 / (2 * Delta_0_OES)  # Relaxation time from BCS gap

# Mean-field + dissipative: nu = 1/2, z = 2
nu_mf = 0.5  # (local)
z_diss = 2.0  # (local)
z_ball = 1.0  # Ballistic/relativistic  # (local)

# KZ exponent for dissipative dynamics
kz_exp_diss = nu_mf / (1 + z_diss * nu_mf)  # = 0.5/2 = 0.25
kz_exp_ball = nu_mf / (1 + z_ball * nu_mf)  # = 0.5/1.5 = 1/3

xi_KZ_diss = xi_0 * (tau_Q / tau_0_gap)**kz_exp_diss
xi_KZ_ball = xi_0 * (tau_Q / tau_0_gap)**kz_exp_ball

print(f"\n--- Kibble-Zurek correlation lengths ---")
print(f"xi_0 = xi_BCS = {xi_0:.4f} M_KK^{{-1}}")
print(f"tau_Q = {tau_Q:.6e} M_KK^{{-1}}")
print(f"tau_0 = 1/(2*Delta) = {tau_0_gap:.4f} M_KK^{{-1}}")
print(f"tau_Q/tau_0 = {tau_Q/tau_0_gap:.6e}")
print(f"\nDissipative (z=2, nu=1/2):")
print(f"  KZ exponent = {kz_exp_diss:.4f}")
print(f"  xi_KZ = {xi_KZ_diss:.6e} M_KK^{{-1}}")
print(f"Ballistic (z=1, nu=1/2):")
print(f"  KZ exponent = {kz_exp_ball:.4f}")
print(f"  xi_KZ = {xi_KZ_ball:.6e} M_KK^{{-1}}")

# Number of skyrmions per fiber volume
# On the SU(2) sub-3-sphere (d=3), the number of defects is:
# N_skyrm ~ Vol(SU(2)) / xi_KZ^3
# (one defect per correlation volume)

N_skyrm_diss = Vol_SU2_aniso / xi_KZ_diss**3
N_skyrm_ball = Vol_SU2_aniso / xi_KZ_ball**3

print(f"\n--- Skyrmion production per fiber ---")
print(f"Vol(SU(2)_aniso) = {Vol_SU2_aniso:.4f} M_KK^{{-3}}")
print(f"Dissipative: N_skyrm/fiber = {N_skyrm_diss:.4e}")
print(f"Ballistic:   N_skyrm/fiber = {N_skyrm_ball:.4e}")

# The crucial point: the transit is so sudden (tau_Q/tau_0 ~ 10^{-3})
# that xi_KZ << 1/M_KK. Many domains form within each fiber.
# This means many skyrmion-antiskyrmion pairs are produced.

# =============================================================================
# SECTION 9: Baryon Asymmetry (eta_B)
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 9: Baryon Asymmetry Estimate")
print("=" * 78)

# The KZ mechanism produces skyrmion-ANTISKYRMION pairs equally.
# Net baryon number requires an ASYMMETRY in production.
# This asymmetry requires CP violation.
#
# From S52 ETA-B-52: phi_CP = 0.0 exactly (three independent proofs).
# From S61 TRANSIT-BARYOGEN-61: Berry CP channel CLOSED ([J, dH/dtau] = 0).
# From S60 LEPTO-CP-60: Leptogenesis CLOSED (NCG forces real Majorana mass).
#
# The ONLY remaining CP source is UV completion (E1 mechanism from S61 VOL-7):
#   delta_CP_UV ~ g_UV = 1/sqrt(IBO) = 1/sqrt(1118) ~ 0.030
#
# However, for SKYRMION baryogenesis, the relevant CP violation is the
# asymmetry in skyrmion vs antiskyrmion production during the quench.
# This requires the CHIRAL order parameter to prefer B > 0 over B < 0.
#
# In the Skyrme model, skyrmion and antiskyrmion are related by parity.
# CP violation in production requires P and CP violation in the quench dynamics.
#
# Within the framework:
# [J, D_K] = 0 (CPT hardwired) means C*P*T is exact.
# If CP is also exact (phi_CP = 0), then T is exact, and the quench dynamics
# are time-reversal invariant => equal skyrmion/antiskyrmion production.
#
# The UV completion provides the ONLY CP violation:
#   epsilon_CP = delta_CP_UV ~ g_UV = 1/sqrt(IBO_ratio)

delta_CP_UV = 1.0 / np.sqrt(IBO_ratio)
print(f"\nCP violation sources:")
print(f"  phi_CP (structural) = {phi_CP} (exact zero)")
print(f"  delta_CP_UV = 1/sqrt(IBO) = {delta_CP_UV:.6f}")
print(f"  [J, D_K] = 0 (CPT exact)")

# The baryon asymmetry:
# eta_B = (n_B - n_Bbar) / s
#       = n_skyrm * delta_CP * B / s
#
# where n_skyrm is the total skyrmion+antiskyrmion density,
# delta_CP is the fractional asymmetry,
# B = 1 is the baryon number per skyrmion.
#
# The entropy density at the transit:
# s ~ (2*pi^2/45) * g_eff * T^3
# At the GGE temperature T_acoustic:
# s_GGE = (2*pi^2/45) * N_dof * T_acoustic^3 (in M_KK units)
# But we need the ratio n_skyrm/s evaluated at the transit epoch.
#
# More precisely: in M_KK units, per fiber,
# the skyrmion density is N_skyrm / Vol(SU(3))
# and the entropy per fiber is s_fiber = N_dof * T_acoustic (order of magnitude)
#
# Actually, the relevant entropy is the 4D entropy density, not the fiber entropy.
# The 4D baryon-to-entropy ratio:
#
# n_B / s = (N_skyrm / V_4) / (s_4)
# where V_4 is the 4D volume at transit and s_4 is the 4D entropy density.
#
# In the transit epoch, the 4D horizon is:
# H_fold = 586.5 M_KK => R_H = 1/H_fold = 1.705e-3 M_KK^{-1}
# V_H ~ R_H^3 = (1/H_fold)^3
#
# N_cells Voronoi cells each produce N_skyrm skyrmions.
# Total skyrmions per Hubble volume:
# N_B_total = N_cells * N_skyrm_per_fiber * delta_CP

# Entropy per Hubble volume at transit:
# s_4 ~ g_eff * T^3 where T is the 4D "reheating" temperature
# After transit, the GGE temperature T_acoustic = 0.112 M_KK
# The total entropy is dominated by the 59.8 quasiparticle pairs:
# S_total ~ n_pairs * N_modes = 59.8 * 8 = 478.4 per fiber per cell

# The baryon-to-entropy ratio:
# eta_B ~ (N_skyrm * delta_CP * B) / (n_pairs * N_modes)
# This is the ratio PER FIBER (the 4D factors cancel in the ratio).

# Use the ballistic KZ result as the more physical one
# (the quench is supersonic = Mach 13.75, closer to ballistic)

N_skyrm = N_skyrm_ball  # Use ballistic estimate
S_per_fiber = n_pairs * N_dof_BCS  # Entropy ~ number of excited quasiparticles

# Net baryons per fiber
n_B_net = N_skyrm * delta_CP_UV * B_skyrmion

# Baryon to entropy ratio
eta_B = n_B_net / S_per_fiber

print(f"\n--- Baryon asymmetry ---")
print(f"N_skyrm (ballistic) = {N_skyrm:.4e} per fiber")
print(f"delta_CP (UV) = {delta_CP_UV:.6f}")
print(f"B = {B_skyrmion}")
print(f"S_per_fiber = n_pairs * N_dof = {S_per_fiber:.1f}")
print(f"\nNet baryons per fiber = {n_B_net:.4e}")
print(f"eta_B = n_B_net / S = {eta_B:.4e}")
print(f"\nObserved eta_B = {eta_BBN_obs:.4e}")
print(f"log10(eta_B / eta_obs) = {np.log10(abs(eta_B) / eta_BBN_obs):.2f}")

OOM_off_eta = np.log10(abs(eta_B) / eta_BBN_obs)
eta_pass = abs(OOM_off_eta) <= 3.0

# Also compute with dissipative estimate
N_skyrm_alt = N_skyrm_diss
n_B_net_alt = N_skyrm_alt * delta_CP_UV * B_skyrmion
eta_B_alt = n_B_net_alt / S_per_fiber

print(f"\n--- Alternative (dissipative z=2) ---")
print(f"N_skyrm (dissipative) = {N_skyrm_alt:.4e} per fiber")
print(f"eta_B = {eta_B_alt:.4e}")
print(f"log10(eta_B / eta_obs) = {np.log10(abs(eta_B_alt) / eta_BBN_obs):.2f}")

# =============================================================================
# SECTION 10: Stability — Can Skyrmions Survive?
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 10: Skyrmion Stability on Compact Fiber")
print("=" * 78)

# On a compact manifold, the topological charge B is strictly conserved
# (pi_3 is exact), BUT skyrmion-antiskyrmion annihilation can occur.
# The annihilation rate depends on the density and the barrier.
#
# For a skyrmion-antiskyrmion pair at separation d:
# V(d) ~ E_skyrm * exp(-M_pi * d) in the pion-mediated regime
# On the compact fiber, M_pi ~ M_KK and d ~ xi_KZ, so:
# V(d) ~ E_skyrm * exp(-M_KK * xi_KZ)
#
# If xi_KZ << 1/M_KK, the exponential suppression is ABSENT and
# annihilation is rapid. If xi_KZ >> 1/M_KK, the barrier is strong.

M_pi_eff = 1.0  # Effective pion mass ~ M_KK in fiber units  # (local)
d_sep_ball = xi_KZ_ball  # Typical separation = KZ correlation length

barrier_ratio_ball = M_pi_eff * d_sep_ball
barrier_ratio_diss = M_pi_eff * xi_KZ_diss

print(f"\nSkyrmion-antiskyrmion annihilation:")
print(f"  M_pi_eff * d (ballistic) = {barrier_ratio_ball:.6e}")
print(f"  M_pi_eff * d (dissipative) = {barrier_ratio_diss:.6e}")
print(f"  exp(-M*d) suppression (ball.) = {np.exp(-barrier_ratio_ball):.6e}")
print(f"  exp(-M*d) suppression (diss.) = {np.exp(-barrier_ratio_diss):.6e}")

# Since xi_KZ << 1/M_KK (the quench is extremely sudden),
# the barrier ratio is << 1, meaning NO suppression.
# Skyrmion-antiskyrmion pairs will annihilate rapidly!

print(f"\nCRITICAL: xi_KZ << 1/M_KK => barrier is negligible")
print(f"Skyrmion-antiskyrmion annihilation is UNSUPPRESSED")
print(f"The initial asymmetry eta_B will be WASHED OUT by annihilation")
print(f"unless a separation mechanism exists.")

# However, the NET baryon number (proportional to delta_CP) is conserved
# topologically. The annihilation removes equal numbers of skyrmions and
# antiskyrmions, leaving the net asymmetry INTACT.
#
# Final surviving baryons = delta_CP * N_total * B (exact by topology)
# The annihilation process removes skyrmion-antiskyrmion PAIRS,
# but cannot remove the NET topological charge.

print(f"\nTopological protection: NET B is conserved by pi_3(SU(3)) = Z")
print(f"Annihilation removes pairs, not net charge.")
print(f"Surviving eta_B = delta_CP * (N_total * B) / S_total")
print(f"This is EXACTLY what we computed: eta_B = {eta_B:.4e}")

# =============================================================================
# SECTION 11: Summary and Gate Verdict
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 11: GATE VERDICT — SKYRMION-BARYON-64")
print("=" * 78)

print(f"\n--- Gate Criteria ---")
print(f"1. M_skyrm within 2 OOM of M_proton (0.938 GeV)")
print(f"   M_skyrm = {E_total_aniso:.4f} M_KK = {M_skyrm_grav:.4e} GeV (gravity)")
print(f"   log10(M_skyrm/M_proton) = {OOM_off_proton_grav:.2f}")
print(f"   VERDICT: {'PASS' if abs(OOM_off_proton_grav) <= 2 else 'FAIL'} "
      f"(threshold: 2 OOM, actual: {abs(OOM_off_proton_grav):.2f})")

print(f"\n2. eta_B within 3 OOM of 6e-10")
print(f"   eta_B = {eta_B:.4e} (ballistic KZ)")
print(f"   eta_B = {eta_B_alt:.4e} (dissipative KZ)")
print(f"   log10(eta_B/eta_obs) = {OOM_off_eta:.2f} (ballistic)")
print(f"   VERDICT: {'PASS' if abs(OOM_off_eta) <= 3 else 'FAIL'} "
      f"(threshold: 3 OOM, actual: {abs(OOM_off_eta):.2f})")

# Overall gate
mass_pass = abs(OOM_off_proton_grav) <= 2.0
eta_pass_3oom = abs(OOM_off_eta) <= 3.0
mass_fail_hard = abs(OOM_off_proton_grav) > 5.0
eta_fail_hard = abs(OOM_off_eta) > 10.0

if mass_fail_hard or eta_fail_hard:
    gate_verdict = "FAIL"
elif mass_pass and eta_pass_3oom:
    gate_verdict = "PASS"
else:
    gate_verdict = "INFO"

print(f"\n{'='*40}")
print(f"GATE SKYRMION-BARYON-64: {gate_verdict}")
print(f"{'='*40}")

if gate_verdict == "FAIL":
    if mass_fail_hard:
        print(f"  FAIL reason: M_skyrm {abs(OOM_off_proton_grav):.1f} OOM from proton mass (> 5)")
    if eta_fail_hard:
        print(f"  FAIL reason: eta_B {abs(OOM_off_eta):.1f} OOM from observation (> 10)")
elif gate_verdict == "INFO":
    print(f"  INFO: not all criteria met, but within intermediate range")
    print(f"  M_skyrm: {abs(OOM_off_proton_grav):.2f} OOM (need < 2 for PASS)")
    print(f"  eta_B: {abs(OOM_off_eta):.2f} OOM (need < 3 for PASS)")
elif gate_verdict == "PASS":
    print(f"  Both criteria met:")
    print(f"  M_skyrm: {abs(OOM_off_proton_grav):.2f} OOM < 2")
    print(f"  eta_B: {abs(OOM_off_eta):.2f} OOM < 3")

# =============================================================================
# SECTION 12: Structural Assessment
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 12: Structural Assessment")
print("=" * 78)

print(f"""
SKYRMION BARYOGENESIS ASSESSMENT:

1. TOPOLOGY: pi_3(SU(3)) = Z provides a well-defined integer baryon number.
   This is EXACT and metric-independent. B is conserved by topology.

2. MASS: M_skyrm = {E_total_aniso:.4f} M_KK = {M_skyrm_grav:.2e} GeV.
   This is {abs(OOM_off_proton_grav):.1f} orders of magnitude ABOVE M_proton.
   The skyrmion is a GUT-scale object, not a QCD-scale baryon.
   This is EXPECTED: the fiber scale IS the KK scale ~ 10^{{16-17}} GeV.
   The Skyrme model on the FIBER gives KK-scale solitons.
   QCD baryons would require the Skyrme model on the EMERGENT 4D space,
   not on the internal fiber.

3. CP VIOLATION: phi_CP = 0 structurally (S52). UV completion provides
   delta_CP ~ 0.030 (S61 VOL-7). This is the ONLY CP source.

4. KZ PRODUCTION: The transit is extremely sudden (Mach 13.75).
   Many skyrmion-antiskyrmion pairs are produced ({N_skyrm:.1e} per fiber).
   But xi_KZ << 1/M_KK, so annihilation is unsuppressed.
   NET baryon number survives by topological protection.

5. eta_B: The baryon asymmetry eta_B = {eta_B:.2e} is {abs(OOM_off_eta):.1f} OOM
   from the observed value {eta_BBN_obs:.2e}.

6. KEY DISTINCTION: Fiber skyrmions are NOT QCD baryons.
   They are topological solitons at the KK scale.
   They could be:
   (a) DARK baryons (heavy, topologically stable, non-annihilating)
   (b) Progenitors of QCD baryons (if a decay/fragmentation channel exists)
   (c) Irrelevant (if they annihilate completely during cosmological evolution)

7. COMPARISON WITH PRIOR BARYOGENESIS ATTEMPTS:
   - S52 ETA-B-52: phi_CP = 0 exactly (structural, CLOSED)
   - S59 BARYON-DIAGNOSTIC: N_3 = 0 (BDI class, no spectral flow)
   - S60 LEPTO-CP: NCG forces real M_R (leptogenesis CLOSED)
   - S61 TRANSIT-BARYOGEN: Berry CP channel CLOSED
   - This computation: fiber skyrmions have correct topology but wrong scale
""")

# =============================================================================
# SECTION 13: Save Data
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 13: Saving data")
print("=" * 78)

save_path = os.path.join(SCRIPT_DIR, 's64_skyrmion_baryon.npz')
np.savez(save_path,
    # Gate result
    gate_verdict=gate_verdict,
    # Masses
    E_skyrmion_MKK=E_total_aniso,
    M_skyrm_grav=M_skyrm_grav,
    M_skyrm_kern=M_skyrm_kern,
    M_proton=M_proton,
    OOM_off_proton_grav=OOM_off_proton_grav,
    OOM_off_proton_kern=OOM_off_proton_kern,
    # Components
    E_sigma_aniso=E_sigma_aniso,
    E_skyrme_aniso=E_skyrme_aniso,
    E_iso_R1=E_iso_R1,
    aniso_ratio=aniso_ratio,
    # Geometry
    scale_cartan=scale_cartan,
    scale_root=scale_root,
    a_radius=a_radius,
    b_radius=b_radius,
    R_scalar_norm=R_scalar_norm,
    Vol_SU2_aniso=Vol_SU2_aniso,
    # Skyrme parameters
    f_pi=f_pi,
    e_skyrme=e_skyrme,
    f_pi_sq=f_pi_sq,
    inv_e_sq=inv_e_sq,
    # Topology
    B_skyrmion=B_skyrmion,
    # KZ production
    xi_KZ_ball=xi_KZ_ball,
    xi_KZ_diss=xi_KZ_diss,
    N_skyrm_ball=N_skyrm_ball,
    N_skyrm_diss=N_skyrm_diss,
    kz_exp_ball=kz_exp_ball,
    kz_exp_diss=kz_exp_diss,
    # Baryon asymmetry
    delta_CP_UV=delta_CP_UV,
    eta_B_ball=eta_B,
    eta_B_diss=eta_B_alt,
    OOM_off_eta_ball=OOM_off_eta,
    OOM_off_eta_diss=np.log10(abs(eta_B_alt)/eta_BBN_obs),
    S_per_fiber=S_per_fiber,
    # Stability
    barrier_ratio_ball=barrier_ratio_ball,
    barrier_ratio_diss=barrier_ratio_diss,
)
print(f"Saved: {save_path}")

# =============================================================================
# SECTION 14: Diagnostic Plot
# =============================================================================
print("\nGenerating diagnostic plot...")

fig = plt.figure(figsize=(16, 12))
gs = GridSpec(2, 2, figure=fig, hspace=0.35, wspace=0.3)

# Panel 1: Skyrmion energy vs radius
ax1 = fig.add_subplot(gs[0, 0])
R_range = np.linspace(0.01, 3.0, 500)
E_range = np.array([E_skyrm_isotropic(r) for r in R_range])
ax1.plot(R_range, E_range, 'b-', linewidth=2, label='E(R) isotropic')
ax1.axvline(1.0, color='r', linestyle='--', label=f'R = 1/M_KK')
ax1.axvline(R_opt, color='g', linestyle=':', label=f'R_opt = {R_opt:.3f}')
ax1.axhline(E_total_aniso, color='orange', linestyle='--',
            label=f'E_aniso = {E_total_aniso:.2f}', alpha=0.7)
ax1.axhline(E_bogomolny, color='purple', linestyle=':',
            label=f'Bogomolny = {E_bogomolny:.0f}', alpha=0.7)
ax1.set_xlabel('Radius R (M_KK$^{-1}$)', fontsize=12)
ax1.set_ylabel('E_skyrmion (M_KK)', fontsize=12)
ax1.set_title('Skyrmion Energy vs Radius', fontsize=13)
ax1.legend(fontsize=9)
ax1.set_ylim(0, min(max(E_range)*1.1, E_bogomolny*1.5))
ax1.grid(True, alpha=0.3)

# Panel 2: Mass comparison
ax2 = fig.add_subplot(gs[0, 1])
masses = {
    'Skyrmion\n(grav)': np.log10(M_skyrm_grav),
    'Skyrmion\n(Kerner)': np.log10(M_skyrm_kern),
    'M_KK\n(grav)': np.log10(M_KK_gravity),
    'M_KK\n(Kerner)': np.log10(M_KK_kerner),
    'M_Pl': np.log10(M_Pl_reduced * 1e9),
    'M_proton': np.log10(M_proton),
    'M_GUT': np.log10(2e16),
}
colors = ['blue', 'blue', 'red', 'red', 'purple', 'green', 'orange']
bars = ax2.barh(list(masses.keys()), list(masses.values()), color=colors, alpha=0.7)
ax2.set_xlabel('log10(Mass / GeV)', fontsize=12)
ax2.set_title('Mass Scale Comparison', fontsize=13)
ax2.grid(True, alpha=0.3, axis='x')
for bar, val in zip(bars, masses.values()):
    ax2.text(val + 0.3, bar.get_y() + bar.get_height()/2,
             f'{val:.1f}', va='center', fontsize=9)

# Panel 3: KZ correlation length and skyrmion density
ax3 = fig.add_subplot(gs[1, 0])
# Plot as a function of quench rate
qrate = np.logspace(-5, 0, 100)
xi_kz_b = xi_0 * qrate**kz_exp_ball
xi_kz_d = xi_0 * qrate**kz_exp_diss
ax3.loglog(qrate, xi_kz_b, 'b-', linewidth=2, label=f'Ballistic (z=1)')
ax3.loglog(qrate, xi_kz_d, 'r-', linewidth=2, label=f'Dissipative (z=2)')
ax3.axhline(1.0, color='k', linestyle='--', label='Fiber radius', alpha=0.5)
ax3.axvline(tau_Q/tau_0_gap, color='g', linestyle=':', linewidth=2,
            label=f'Transit: tau_Q/tau_0 = {tau_Q/tau_0_gap:.1e}')
ax3.set_xlabel('tau_Q / tau_0', fontsize=12)
ax3.set_ylabel('xi_KZ (M_KK$^{-1}$)', fontsize=12)
ax3.set_title('KZ Correlation Length', fontsize=13)
ax3.legend(fontsize=9)
ax3.grid(True, alpha=0.3)

# Panel 4: eta_B comparison
ax4 = fig.add_subplot(gs[1, 1])
eta_values = {
    'Observed\n(BBN)': eta_BBN_obs,
    'Skyrmion\n(ballistic)': abs(eta_B),
    'Skyrmion\n(dissipative)': abs(eta_B_alt),
    'S61\n(ATDHFB)': 1e-10,  # approximate from S61
}
bar_colors = ['green', 'blue', 'red', 'orange']
y_pos = range(len(eta_values))
ax4.barh(list(eta_values.keys()), [np.log10(v) for v in eta_values.values()],
         color=bar_colors, alpha=0.7)
ax4.set_xlabel('log10(eta_B)', fontsize=12)
ax4.set_title('Baryon Asymmetry Comparison', fontsize=13)
ax4.axvline(np.log10(eta_BBN_obs), color='green', linestyle='--', alpha=0.5)
# Shade 3 OOM window
ax4.axvspan(np.log10(eta_BBN_obs) - 3, np.log10(eta_BBN_obs) + 3,
            alpha=0.1, color='green', label='3 OOM window')  # (local)
ax4.legend(fontsize=9)
ax4.grid(True, alpha=0.3, axis='x')

fig.suptitle('SKYRMION-BARYON-64: Skyrmion Physics on SU(3) Fiber',
             fontsize=14, fontweight='bold')

plot_path = os.path.join(SCRIPT_DIR, 's64_skyrmion_baryon.png')
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
plt.close()
print(f"Saved plot: {plot_path}")

# =============================================================================
# FINISH
# =============================================================================
elapsed = time.time() - t0
print(f"\nTotal runtime: {elapsed:.2f} s")
print(f"\nDone.")

_log_file.close()
