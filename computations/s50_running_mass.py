#!/usr/bin/env python3
"""
s50_running_mass.py — Running Mass from Anomalous Dimension (RUNNING-MASS-50)
================================================================================

Physics:
  S49 proved alpha_s = n_s^2 - 1 = -0.069 is EXACT for the O-Z propagator with
  CONSTANT mass. This script asks: if the Goldstone mass runs with wavevector
  m(K)^2 = m_0^2 + Sigma(K) - Sigma(0), does the correction to alpha_s bring it
  within 2-sigma of Planck?

  The GL free energy for the Goldstone field phi on the 32-cell lattice:
    F[phi] = sum_<ij> J_ij/2 (phi_i - phi_j)^2 + sum_i m^2/2 phi_i^2
             + sum_i lambda/4! phi_i^4

  The 1-loop self-energy on the anisotropic lattice:
    Sigma(K) = (lambda * T) / (2*N) sum_q G(q)
             + (lambda^2 * T^2) / (6*N^2) sum_{q1,q2} G(q1)*G(q2)*G(K-q1-q2)

  where G(q) = 1/[epsilon(q) + m^2] and epsilon(q) is the lattice dispersion.

  The running mass modifies the O-Z propagator:
    P(K) = T / [J*epsilon(K) + m(K)^2]

  The spectral tilt is:
    n_s(K) = 1 + d ln P / d ln K

  The running of the running:
    alpha_s = d n_s / d ln K

  The CORRECTION from running mass:
    delta_alpha = alpha_s(running) - (n_s^2 - 1)

  The anomalous dimension:
    gamma = d ln m(K)^2 / d ln K   (evaluated at K_pivot)

Gate: RUNNING-MASS-50
  PASS: gamma > 1.7 AND alpha_s shifts within 2-sigma of Planck (+0.061 from -0.069)
  FAIL: gamma < 0.5 (negligible running)
  INFO: 0.5 < gamma < 1.7 (partial but insufficient running)

Session: S50 W1-F
Author: landau-condensed-matter-theorist
"""

import sys
import os
import time
import numpy as np
from scipy.optimize import brentq
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

t0 = time.time()

# --- Import canonical constants ---
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    E_cond, tau_fold, N_cells, M_KK, PI,
    Delta_0_GL, Delta_0_OES, xi_BCS, xi_GL,
    T_compound, a_GL, b_GL
)

# --- Load upstream data ---
data_dir = os.path.dirname(os.path.abspath(__file__))

d_oz = np.load(os.path.join(data_dir, 's48_aniso_oz.npz'), allow_pickle=True)
d_tex = np.load(os.path.join(data_dir, 's47_texture_corr.npz'), allow_pickle=True)
d_dipolar = np.load(os.path.join(data_dir, 's49_dipolar_catalog.npz'), allow_pickle=True)
d_bayes = np.load(os.path.join(data_dir, 's49_alpha_s_bayes.npz'), allow_pickle=True)

# Central coupling constants (M_KK units)
J_C2 = float(d_tex['J_C2'])          # = 0.9325
J_su2 = float(d_tex['J_su2'])        # = 0.0591
J_u1 = float(d_tex['J_u1'])          # = 0.0383
J_xy = float(d_oz['J_xy'])           # = J_C2
J_z = float(d_oz['J_z'])             # = J_su2

# Temperatures
T_acoustic = float(d_oz['T_acoustic'])  # = 0.1122

# Goldstone mass (Leggett dipolar, S49)
omega_L1 = float(d_dipolar['omega_L1'])   # = 0.06955 M_KK
omega_L2 = float(d_dipolar['omega_L2'])   # = 0.10737 M_KK
m_0 = omega_L1                             # Bare Goldstone mass

# Pivot scale
K_pivot = float(d_oz['K_pivot_lattice'])  # = 1.979
L_eff = float(d_oz['L_eff'])             # = 3.175

# Cell geometry
l_cell = float(d_tex['l_cell'])           # = 0.152 M_KK^{-1}
rho_s_eigs = np.array(d_tex['rho_s_eigs'])

# Lattice dimensions
nx, ny, nz = 4, 4, 2
N_lat = nx * ny * nz  # = 32

# S49 Bayes results for comparison
alpha_s_central = float(d_bayes['alpha_s_central'])  # = -0.0688

# V-matrix coupling (from S34: V(B2,B2) = 0.1557)
V_B2B2 = 0.1557  # Casimir, irreducible (S34 Schur)

print("=" * 78)
print("RUNNING-MASS-50: Running Mass from Anomalous Dimension")
print("       Ginzburg-Landau 1-loop Self-Energy on the 32-Cell Lattice")
print("=" * 78)

# ============================================================================
# SECTION 1: Lattice Dispersion and Brillouin Zone
# ============================================================================
print("\n--- Section 1: Anisotropic Lattice Dispersion ---")

# The lattice dispersion for the anisotropic 4x4x2 Josephson network:
#   epsilon(q) = 2*J_xy*(2 - cos(q_x) - cos(q_y)) + 2*J_z*(1 - cos(q_z))
#
# This is the standard tight-binding dispersion on a simple cubic lattice
# with anisotropic hopping. The lattice constants are absorbed into J_ij.
#
# Momentum quantization on the 4x4x2 lattice:
#   q_x = 2*pi*n_x/4, n_x = 0,1,2,3
#   q_y = 2*pi*n_y/4, n_y = 0,1,2,3
#   q_z = 2*pi*n_z/2, n_z = 0,1

# Generate all lattice momenta
qx_vals = 2 * PI * np.arange(nx) / nx
qy_vals = 2 * PI * np.arange(ny) / ny
qz_vals = 2 * PI * np.arange(nz) / nz

# Create momentum grid
QX, QY, QZ = np.meshgrid(qx_vals, qy_vals, qz_vals, indexing='ij')
Q_grid = np.stack([QX.ravel(), QY.ravel(), QZ.ravel()], axis=1)  # (32, 3)

print(f"  Lattice: {nx} x {ny} x {nz} = {N_lat} sites")
print(f"  J_xy (C2 direction) = {J_xy:.6f} M_KK")
print(f"  J_z  (su2 direction) = {J_z:.6f} M_KK")
print(f"  Anisotropy ratio J_xy/J_z = {J_xy/J_z:.2f}")
print(f"  Bare Goldstone mass m_0 = omega_L1 = {m_0:.6f} M_KK")
print(f"  T_acoustic = {T_acoustic:.6f} M_KK")
print(f"  K_pivot = {K_pivot:.6f}")


def epsilon_lattice(qx, qy, qz):
    """Lattice dispersion: epsilon(q) for the anisotropic Josephson network."""
    return (2 * J_xy * (2 - np.cos(qx) - np.cos(qy))
            + 2 * J_z * (1 - np.cos(qz)))


# Compute epsilon at all lattice momenta
eps_grid = epsilon_lattice(Q_grid[:, 0], Q_grid[:, 1], Q_grid[:, 2])

print(f"\n  Lattice dispersion epsilon(q):")
print(f"    min = {eps_grid.min():.6f} (q=0)")
print(f"    max = {eps_grid.max():.6f}")
print(f"    bandwidth W = {eps_grid.max() - eps_grid.min():.6f}")
print(f"    mean = {np.mean(eps_grid):.6f}")

# Effective isotropic coupling for comparison
J_eff = (2 * J_xy + J_z) / 3
print(f"  J_eff (isotropic avg) = {J_eff:.6f}")

# ============================================================================
# SECTION 2: 1-Loop Self-Energy on the Lattice
# ============================================================================
print("\n--- Section 2: 1-Loop Self-Energy Sigma(K) ---")

# The GL free energy coupling lambda is related to V(B2,B2):
#   lambda = 6 * V(B2,B2) / N_B2
# where N_B2 = 4 (number of B2 modes). The factor 6 is the combinatorial
# factor for a phi^4 vertex with 4 identical legs: 4! / 4 = 6.
#
# However, for the running mass computation, lambda is the key FREE PARAMETER.
# We scan over lambda to find the threshold value that gives gamma > 1.7.

# The tadpole diagram (1-loop, constant shift):
#   Sigma_tadpole = (lambda * T) / (2*N) * sum_q G_0(q)
#   where G_0(q) = 1/[epsilon(q) + m_0^2]
#
# This gives a K-INDEPENDENT mass shift. It does NOT contribute to running.

# The sunset diagram (2-loop, but 1-loop in phi^4 self-energy):
#   Sigma_sunset(K) = (lambda^2 * T^2) / (6*N^2) * sum_{q1,q2}
#       G_0(q1) * G_0(q2) * G_0(K-q1-q2)
#
# This IS K-dependent and gives the running mass.


def compute_G0(m_sq):
    """Bare propagator at all lattice momenta."""
    return 1.0 / (eps_grid + m_sq)


def compute_tadpole(lam, m_sq, T):
    """Tadpole self-energy (K-independent)."""
    G0 = compute_G0(m_sq)
    return lam * T / (2 * N_lat) * np.sum(G0)


def compute_sunset(K_vec, lam, m_sq, T):
    """
    Sunset self-energy at external momentum K_vec.

    Sigma_sunset(K) = (lam^2 * T^2) / (6 * N^2) * sum_{q1,q2} G0(q1)*G0(q2)*G0(K-q1-q2)

    For efficiency on the 32-site lattice, this is an O(N^2) = O(1024) double sum
    over the 32 momentum points.
    """
    G0 = compute_G0(m_sq)

    # Pre-compute epsilon at all shifted momenta K - q1 - q2
    # K_vec - q1 - q2 must be wrapped back into the BZ
    sigma_val = 0.0
    for i1 in range(N_lat):
        q1 = Q_grid[i1]
        for i2 in range(N_lat):
            q2 = Q_grid[i2]
            # K - q1 - q2, wrapped to BZ
            q3 = K_vec - q1 - q2
            # Wrap: the lattice dispersion is 2*pi periodic in each component
            eps_q3 = epsilon_lattice(q3[0], q3[1], q3[2])
            G0_q3 = 1.0 / (eps_q3 + m_sq)
            sigma_val += G0[i1] * G0[i2] * G0_q3

    prefactor = lam**2 * T**2 / (6 * N_lat**2)
    return prefactor * sigma_val


def compute_sigma_full(K_vec, lam, m_sq, T):
    """Total 1-loop self-energy: tadpole + sunset."""
    sig_tadpole = compute_tadpole(lam, m_sq, T)
    sig_sunset = compute_sunset(K_vec, lam, m_sq, T)
    return sig_tadpole + sig_sunset


# ============================================================================
# SECTION 3: Running Mass m(K)^2 = m_0^2 + Sigma(K) - Sigma(0)
# ============================================================================
print("\n--- Section 3: Running Mass Computation ---")

# The physical running mass is:
#   m(K)^2 = m_0^2 + Sigma(K) - Sigma(0)
#
# The tadpole cancels in the difference Sigma(K) - Sigma(0) because it is
# K-independent. So only the sunset diagram contributes to the running:
#   m(K)^2 - m_0^2 = Sigma_sunset(K) - Sigma_sunset(0)

# First, verify the scale of the tadpole
m_0_sq = m_0**2
print(f"  m_0^2 = {m_0_sq:.8f}")

# Compute at a reference coupling
lam_ref = V_B2B2  # Natural scale: V(B2,B2) = 0.1557

tadpole_ref = compute_tadpole(lam_ref, m_0_sq, T_acoustic)
print(f"  Tadpole at lambda={lam_ref:.4f}: Sigma_tadpole = {tadpole_ref:.8f}")
print(f"  Ratio Sigma_tadpole / m_0^2 = {tadpole_ref / m_0_sq:.6f}")

# Compute sunset at K=0
K_zero = np.array([0.0, 0.0, 0.0])
sunset_0 = compute_sunset(K_zero, lam_ref, m_0_sq, T_acoustic)
print(f"  Sunset at K=0, lambda={lam_ref:.4f}: Sigma_sunset(0) = {sunset_0:.8f}")

# Compute sunset at K_pivot (along the (1,1,0) direction, appropriate for
# the angular average; the exact direction averages out by the isotropic
# constraint on n_s)
K_pivot_vec = K_pivot * np.array([1.0, 1.0, 0.0]) / np.sqrt(2)
sunset_K = compute_sunset(K_pivot_vec, lam_ref, m_0_sq, T_acoustic)
print(f"  Sunset at K=K_pivot, lambda={lam_ref:.4f}: Sigma_sunset(K_pivot) = {sunset_K:.8f}")

delta_sigma_ref = sunset_K - sunset_0
print(f"  Delta Sigma = Sigma(K_pivot) - Sigma(0) = {delta_sigma_ref:.8e}")
print(f"  m(K_pivot)^2 - m_0^2 = {delta_sigma_ref:.8e}")
print(f"  Relative shift: {delta_sigma_ref / m_0_sq:.6e}")

# ============================================================================
# SECTION 4: Lambda Scan — Anomalous Dimension gamma(lambda)
# ============================================================================
print("\n--- Section 4: Lambda Scan for Anomalous Dimension ---")

# The anomalous dimension gamma = d ln m(K)^2 / d ln K is computed by
# evaluating m(K)^2 at two nearby K values and taking the log-derivative.
#
# gamma = [ln m(K+dK)^2 - ln m(K-dK)^2] / [2 * d(ln K)]

# Scan lambda over [0.01, 10] in log space
lambda_scan = np.logspace(-2, 1, 50)
gamma_scan = np.zeros_like(lambda_scan)
delta_alpha_scan = np.zeros_like(lambda_scan)
m_K_sq_scan = np.zeros_like(lambda_scan)  # m(K_pivot)^2
sigma_K_scan = np.zeros_like(lambda_scan)
sigma_0_scan = np.zeros_like(lambda_scan)

# For gamma, evaluate m^2 at K_pivot +/- small step
dK_frac = 0.05  # 5% step for numerical derivative
K_plus = K_pivot * (1 + dK_frac)
K_minus = K_pivot * (1 - dK_frac)

# Direction vectors
hat_110 = np.array([1.0, 1.0, 0.0]) / np.sqrt(2)
K_plus_vec = K_plus * hat_110
K_minus_vec = K_minus * hat_110

print(f"  K_pivot = {K_pivot:.6f}")
print(f"  K_plus  = {K_plus:.6f}")
print(f"  K_minus = {K_minus:.6f}")
print(f"  d(ln K) = {2 * dK_frac:.4f}")
print(f"  Lambda scan: [{lambda_scan[0]:.3f}, {lambda_scan[-1]:.3f}] ({len(lambda_scan)} points)")
print()

for i, lam in enumerate(lambda_scan):
    # Compute sunset at K=0, K_pivot, K_plus, K_minus
    sig_0 = compute_sunset(K_zero, lam, m_0_sq, T_acoustic)
    sig_K = compute_sunset(K_pivot_vec, lam, m_0_sq, T_acoustic)
    sig_plus = compute_sunset(K_plus_vec, lam, m_0_sq, T_acoustic)
    sig_minus = compute_sunset(K_minus_vec, lam, m_0_sq, T_acoustic)

    # Running mass at each K
    m2_K = m_0_sq + sig_K - sig_0
    m2_plus = m_0_sq + sig_plus - sig_0
    m2_minus = m_0_sq + sig_minus - sig_0

    # Anomalous dimension: gamma = d ln m^2 / d ln K
    if m2_plus > 0 and m2_minus > 0:
        gamma_val = (np.log(m2_plus) - np.log(m2_minus)) / (2 * dK_frac)
    else:
        gamma_val = np.nan

    gamma_scan[i] = gamma_val
    m_K_sq_scan[i] = m2_K
    sigma_K_scan[i] = sig_K
    sigma_0_scan[i] = sig_0

    if i % 10 == 0:
        print(f"  lambda={lam:8.4f}: Sigma(K)={sig_K:.4e}, Sigma(0)={sig_0:.4e}, "
              f"m(K)^2={m2_K:.6f}, gamma={gamma_val:.6f}")

print(f"\n  Gamma range: [{np.nanmin(gamma_scan):.6f}, {np.nanmax(gamma_scan):.6f}]")

# ============================================================================
# SECTION 5: Corrected n_s and alpha_s with Running Mass
# ============================================================================
print("\n--- Section 5: n_s and alpha_s with Running Mass ---")

# For each lambda, compute n_s and alpha_s using the running mass.
#
# The O-Z propagator with running mass:
#   P(K) = T / [J_eff * epsilon_continuum(K) + m(K)^2]
#
# In the continuum limit: epsilon_continuum(K) ~ K^2 (small K).
# But on the lattice, we use the full dispersion.
#
# For the angular-averaged tilt:
#   n_s = 1 + d ln P / d ln K
#
# We evaluate this numerically at K_pivot.

# The correction to alpha_s from running mass:
# In the constant-mass case, alpha_s = n_s^2 - 1 (exact identity).
# With running mass m(K), there is an additional contribution:
#
# Let x = J_eff * K^2, m^2 = m(K)^2. Then:
#   P(K) = T / [x + m^2]
#   d ln P / d ln K = d ln T - d ln(x + m^2) / d ln K
#                   = -[d(x + m^2)/d ln K] / (x + m^2)
#                   = -[2x + d(m^2)/d ln K] / (x + m^2)
#
# With constant mass: d(m^2)/d ln K = 0, so n_s - 1 = -2x/(x+m^2)
# With running mass: n_s - 1 = -[2x + gamma * m^2] / (x + m^2)
#   where gamma = d ln m^2 / d ln K.
#
# alpha_s = d(n_s)/d ln K requires the second derivative.
# Let's compute it numerically.

ns_scan = np.zeros_like(lambda_scan)
alpha_s_scan = np.zeros_like(lambda_scan)
ns_constant_mass = np.zeros_like(lambda_scan)
alpha_s_constant = np.zeros_like(lambda_scan)

# For numerical differentiation, use 5 K-values around K_pivot
dK_ns = 0.02  # 2% step for n_s derivative
K_values = K_pivot * np.array([1 - 2*dK_ns, 1 - dK_ns, 1.0, 1 + dK_ns, 1 + 2*dK_ns])

for i, lam in enumerate(lambda_scan):
    # Compute P(K) at 5 points with running mass
    sig_0_val = compute_sunset(K_zero, lam, m_0_sq, T_acoustic)

    lnP_run = np.zeros(5)
    lnP_const = np.zeros(5)

    for j, K_val in enumerate(K_values):
        K_vec_j = K_val * hat_110
        sig_j = compute_sunset(K_vec_j, lam, m_0_sq, T_acoustic)
        m2_j = m_0_sq + sig_j - sig_0_val

        # Dispersion at this K (continuum approximation for angular avg)
        eps_j = J_eff * K_val**2

        # P with running mass
        P_run_j = T_acoustic / (eps_j + m2_j)
        lnP_run[j] = np.log(P_run_j) if P_run_j > 0 else -np.inf

        # P with constant mass (for comparison)
        P_const_j = T_acoustic / (eps_j + m_0_sq)
        lnP_const[j] = np.log(P_const_j) if P_const_j > 0 else -np.inf

    # Numerical derivatives using central differences
    d_lnK = dK_ns  # d(ln K) = dK/K = dK_ns

    # n_s = 1 + d(ln P)/d(ln K)
    # 4th-order central difference for first derivative:
    # f'(x) = [-f(x+2h) + 8*f(x+h) - 8*f(x-h) + f(x-2h)] / (12*h)
    ns_run_val = 1.0 + (-lnP_run[4] + 8*lnP_run[3] - 8*lnP_run[1] + lnP_run[0]) / (12 * d_lnK)
    ns_const_val = 1.0 + (-lnP_const[4] + 8*lnP_const[3] - 8*lnP_const[1] + lnP_const[0]) / (12 * d_lnK)

    # alpha_s = d(n_s)/d(ln K) = d^2(ln P)/d(ln K)^2
    # 4th-order central difference for second derivative:
    # f''(x) = [-f(x+2h) + 16*f(x+h) - 30*f(x) + 16*f(x-h) - f(x-2h)] / (12*h^2)
    alpha_run_val = (-lnP_run[4] + 16*lnP_run[3] - 30*lnP_run[2] + 16*lnP_run[1] - lnP_run[0]) / (12 * d_lnK**2)
    alpha_const_val = (-lnP_const[4] + 16*lnP_const[3] - 30*lnP_const[2] + 16*lnP_const[1] - lnP_const[0]) / (12 * d_lnK**2)

    ns_scan[i] = ns_run_val
    alpha_s_scan[i] = alpha_run_val
    ns_constant_mass[i] = ns_const_val
    alpha_s_constant[i] = alpha_const_val

# Compute delta_alpha = alpha_s(running) - (n_s^2 - 1)
delta_alpha_scan = alpha_s_scan - (ns_scan**2 - 1)

print(f"  At lambda=V_B2B2={V_B2B2:.4f}:")
idx_ref = np.argmin(np.abs(lambda_scan - V_B2B2))
print(f"    n_s (running)  = {ns_scan[idx_ref]:.8f}")
print(f"    n_s (constant) = {ns_constant_mass[idx_ref]:.8f}")
print(f"    alpha_s (running)  = {alpha_s_scan[idx_ref]:.8f}")
print(f"    alpha_s (constant) = {alpha_s_constant[idx_ref]:.8f}")
print(f"    n_s^2 - 1 (running n_s) = {ns_scan[idx_ref]**2 - 1:.8f}")
print(f"    delta_alpha = {delta_alpha_scan[idx_ref]:.8e}")
print(f"    gamma = {gamma_scan[idx_ref]:.8f}")

# ============================================================================
# SECTION 6: Analytical Cross-Check
# ============================================================================
print("\n--- Section 6: Analytical Cross-Check ---")

# In the continuum limit with running mass m(K)^2 = m_0^2 * (K/K_0)^gamma:
#
# P(K) = T / [J*K^2 + m_0^2*(K/K_0)^gamma]
#
# Define xi = m_0^2 * K_0^{-gamma} * K^{gamma-2} / J. Then:
#   P(K) = T / [J*K^2 * (1 + xi)]
#
# d ln P / d ln K = -2 - d ln(1+xi)/d ln K
#
# d ln(1+xi)/d ln K = xi/(1+xi) * d ln xi / d ln K = xi/(1+xi) * (gamma - 2)
#
# So: n_s - 1 = -2 - xi*(gamma-2)/(1+xi)
#             = [-2(1+xi) - xi*(gamma-2)] / (1+xi)
#             = [-2 - gamma*xi] / (1+xi)
#
# For constant mass (gamma=0):
#   n_s - 1 = -2/(1+xi)  with xi = m^2/(J*K^2)
# This gives the standard O-Z result.
#
# For running mass:
#   n_s - 1 = -(2 + gamma*xi) / (1 + xi)
#
# The correction to n_s:
#   delta(n_s) = -gamma * xi / (1+xi)
#
# The correction to alpha_s:
# alpha_s = d(n_s)/d ln K. With constant mass:
#   alpha_s_0 = n_s^2 - 1
#
# With running mass, the additional term:
#   delta(alpha_s) involves d(gamma*xi/(1+xi))/d ln K
#
# At leading order in gamma (which is small):
#   delta(alpha_s) ~ gamma * d[xi/(1+xi)] / d ln K
#                   = gamma * [d xi/d ln K] / (1+xi)^2
#                   = gamma * (gamma-2) * xi / (1+xi)^2
#
# For the O-Z model: xi = m_0^2 / (J*K_pivot^2).

xi_0 = m_0_sq / (J_eff * K_pivot**2)
print(f"  xi_0 = m_0^2 / (J_eff * K_pivot^2) = {xi_0:.6f}")
print(f"  1/(1+xi_0) = {1/(1+xi_0):.6f}")

# But this is too small! xi_0 << 1, so m^2 << J*K^2.
# In the S49 framework, m_* was solved from n_s = 0.965, giving m_* >> m_0.
# The resolved m_* = 11.87 (from S49 Bayes), which gives xi = m_*^2/(J*K^2).

m_star = float(d_bayes['m_star_central'])  # = 11.865
xi_star = m_star**2 / (J_eff * K_pivot**2)
print(f"\n  With m_* from n_s constraint:")
print(f"  m_* = {m_star:.6f}")
print(f"  xi_* = m_*^2 / (J_eff * K_pivot^2) = {xi_star:.6f}")
print(f"  1/(1+xi_*) = {1/(1+xi_star):.6f}")

# CRITICAL: There is a factor-of-150 gap between m_0 = 0.070 (Leggett mass)
# and m_* = 11.87 (the mass required to fit n_s = 0.965 in the O-Z model).
# The running mass correction operates on m_0, not m_*.
# The question is whether the 1-loop sunset self-energy can bridge this gap.

print(f"\n  Scale hierarchy:")
print(f"    m_0 (Leggett)       = {m_0:.6f}")
print(f"    m_* (fit to n_s)    = {m_star:.4f}")
print(f"    Ratio m_*/m_0       = {m_star/m_0:.1f}")
print(f"    J_eff * K_pivot^2   = {J_eff * K_pivot**2:.4f}")
print(f"    Bandwidth W         = {eps_grid.max():.4f}")

# The analytical estimate for gamma from 1-loop sunset:
# The sunset contribution at 1 loop:
#   Sigma_sunset(K) - Sigma_sunset(0) ~ (lambda^2 * T^2) / (6 * N^2) *
#       [sum_{q1,q2} G0(q1)*G0(q2)*G0(K-q1-q2) - sum_{q1,q2} G0(q1)*G0(q2)*G0(-q1-q2)]
#
# The K-dependence comes from G0(K-q1-q2). For small K/BZ_edge:
#   G0(K-q) = G0(-q) + K * dG0/dq + ...
#
# The leading correction is O(K^2) (by cubic lattice symmetry, the O(K) term
# vanishes). So:
#   Sigma(K) - Sigma(0) ~ C * K^2
# where C is a constant depending on lambda, T, and the lattice propagators.
#
# This means: m(K)^2 = m_0^2 + C * K^2
# And: gamma = d ln m^2 / d ln K = 2*C*K^2 / (m_0^2 + C*K^2)
#
# For gamma to be O(1), we need C * K_pivot^2 ~ m_0^2.
# This requires lambda^2 * T^2 * (propagator sum) ~ m_0^2.

print("\n  Analytical gamma estimate (power-counting):")
# Estimate the propagator sum for the sunset
G0_ref = compute_G0(m_0_sq)
sum_G0_sq = np.sum(G0_ref**2) / N_lat  # average G0^2
print(f"    <G0^2> = {sum_G0_sq:.6f}")
print(f"    <G0>   = {np.mean(G0_ref):.6f}")

# The sunset coefficient C (rough estimate):
# C ~ lambda^2 * T^2 / (6 * N^2) * N * dG/dK^2_averaged
# dG/dK^2 ~ G0^2 * J (from expanding G(K-q) around G(-q))
# So: C ~ lambda^2 * T^2 * J * <G0^2> / (6 * N)
C_estimate = lambda lam: lam**2 * T_acoustic**2 * J_eff * sum_G0_sq / (6 * N_lat)

lam_test = V_B2B2
C_val = C_estimate(lam_test)
gamma_estimate = 2 * C_val * K_pivot**2 / (m_0_sq + C_val * K_pivot**2)
print(f"    At lambda={lam_test:.4f}:")
print(f"      C ~ {C_val:.6e}")
print(f"      C * K_pivot^2 = {C_val * K_pivot**2:.6e}")
print(f"      m_0^2 = {m_0_sq:.6e}")
print(f"      gamma_estimate ~ {gamma_estimate:.6e}")

# For gamma ~ 1.7, we need C * K^2 >> m_0^2:
# lambda^2 * T^2 * J * <G0^2> * K^2 / (6*N) ~ m_0^2
# lambda^2 ~ 6 * N * m_0^2 / (T^2 * J * <G0^2> * K^2)
lam_threshold = np.sqrt(6 * N_lat * m_0_sq / (T_acoustic**2 * J_eff * sum_G0_sq * K_pivot**2))
print(f"\n    lambda for gamma ~ 1:")
print(f"      lambda_threshold ~ {lam_threshold:.4f}")
print(f"      Compare to V(B2,B2) = {V_B2B2:.4f}")
print(f"      Ratio lambda_thresh/V_B2B2 = {lam_threshold/V_B2B2:.1f}")

# ============================================================================
# SECTION 7: Detailed Results at Key Couplings
# ============================================================================
print("\n--- Section 7: Detailed Results ---")

key_lambdas = [0.01, 0.05, V_B2B2, 0.5, 1.0, 2.0, 5.0, 10.0]
print(f"  {'lambda':>10s} {'gamma':>12s} {'m(K)^2':>12s} {'n_s(run)':>12s} "
      f"{'alpha_s(run)':>14s} {'n_s^2-1':>12s} {'delta_alpha':>14s}")
print("  " + "-" * 98)

for lam in key_lambdas:
    # Compute at this lambda
    sig_0 = compute_sunset(K_zero, lam, m_0_sq, T_acoustic)
    sig_K = compute_sunset(K_pivot_vec, lam, m_0_sq, T_acoustic)
    sig_plus = compute_sunset(K_plus_vec, lam, m_0_sq, T_acoustic)
    sig_minus = compute_sunset(K_minus_vec, lam, m_0_sq, T_acoustic)

    m2_K = m_0_sq + sig_K - sig_0
    m2_plus = m_0_sq + sig_plus - sig_0
    m2_minus = m_0_sq + sig_minus - sig_0

    gamma_val = (np.log(m2_plus) - np.log(m2_minus)) / (2 * dK_frac) if m2_plus > 0 and m2_minus > 0 else np.nan

    # n_s and alpha_s with running mass (5-point stencil)
    lnP = np.zeros(5)
    for j, K_val in enumerate(K_values):
        K_vec_j = K_val * hat_110
        sig_j = compute_sunset(K_vec_j, lam, m_0_sq, T_acoustic)
        m2_j = m_0_sq + sig_j - sig_0
        eps_j = J_eff * K_val**2
        P_j = T_acoustic / (eps_j + m2_j)
        lnP[j] = np.log(P_j) if P_j > 0 else -np.inf

    ns_val = 1.0 + (-lnP[4] + 8*lnP[3] - 8*lnP[1] + lnP[0]) / (12 * dK_ns)
    alpha_val = (-lnP[4] + 16*lnP[3] - 30*lnP[2] + 16*lnP[1] - lnP[0]) / (12 * dK_ns**2)
    d_alpha = alpha_val - (ns_val**2 - 1)

    print(f"  {lam:10.4f} {gamma_val:12.6f} {m2_K:12.6e} {ns_val:12.8f} "
          f"{alpha_val:14.8e} {ns_val**2 - 1:12.8e} {d_alpha:14.8e}")

# ============================================================================
# SECTION 8: The Fundamental Obstruction
# ============================================================================
print("\n--- Section 8: Structural Analysis of the Running Mass Correction ---")

# There is a fundamental issue: the O-Z identity alpha_s = n_s^2 - 1
# is an ALGEBRAIC identity for ANY single-pole propagator P(K) = T/(A*K^2 + B).
# Running mass makes B -> B(K), so P(K) = T/(A*K^2 + B(K)).
#
# The identity alpha_s = n_s^2 - 1 breaks ONLY if d^2(m^2)/d(ln K)^2 != 0,
# i.e., if the running has curvature (non-power-law).
#
# For a power-law running m^2(K) = m_0^2 * (K/K_0)^gamma with CONSTANT gamma,
# the propagator P(K) = T / [A*K^2 + B*(K/K_0)^gamma] is NOT a single-pole
# O-Z form unless gamma = 0 or gamma = 2 (in which case it maps back to O-Z
# with renormalized parameters).
#
# So the identity alpha_s = n_s^2 - 1 IS violated by running mass with 0 < gamma < 2.
# The question is how large the violation is.

# The exact formulas for n_s and alpha_s with power-law running:
# P(K) = T / [J*K^2 + m_0^2*(K/K_0)^gamma]
#
# Let u = m_0^2 * K_0^{-gamma} * K^{gamma-2} / J. Then:
#   P = T / [J * K^2 * (1 + u)]
#   ln P = ln T - ln J - 2*ln K - ln(1+u)
#   d(ln P)/d(ln K) = -2 - u*(gamma-2)/(1+u)
#   => n_s - 1 = -2 - u*(gamma-2)/(1+u) = -(2 + gamma*u)/(1+u)
#
# Second derivative:
#   d^2(ln P)/d(ln K)^2 = -d/d(ln K)[u*(gamma-2)/(1+u)]
#   d[u/(1+u)]/d(ln K) = [du/d(ln K)] / (1+u)^2 = (gamma-2)*u / (1+u)^2
#   => d^2(ln P)/d(ln K)^2 = -(gamma-2)^2 * u / (1+u)^2
#
# So: alpha_s = -(gamma-2)^2 * u / (1+u)^2
#
# The O-Z identity: n_s^2 - 1 = [(2+gamma*u)/(1+u)]^2 - 1
#                              = [(2+gamma*u)^2 - (1+u)^2] / (1+u)^2
#                              = [4 + 4*gamma*u + gamma^2*u^2 - 1 - 2*u - u^2] / (1+u)^2
#                              = [3 + (4*gamma-2)*u + (gamma^2-1)*u^2] / (1+u)^2
#
# delta_alpha = alpha_s - (n_s^2 - 1)
#             = -(gamma-2)^2 * u/(1+u)^2 - [3 + (4*gamma-2)*u + (gamma^2-1)*u^2]/(1+u)^2
#             = [-((gamma-2)^2*u) - 3 - (4*gamma-2)*u - (gamma^2-1)*u^2] / (1+u)^2
#
# Numerator: -3 - [(gamma-2)^2 + 4*gamma - 2]*u - (gamma^2-1)*u^2
#          = -3 - [gamma^2 - 4*gamma + 4 + 4*gamma - 2]*u - (gamma^2-1)*u^2
#          = -3 - [gamma^2 + 2]*u - (gamma^2-1)*u^2
#
# Hmm, this gives a CONSTANT -3/(1+u)^2 term even for gamma=0. Let me recheck.
#
# For gamma=0 (constant mass):
#   n_s - 1 = -2/(1+u) where u = m^2/(J*K^2)
#   n_s^2 - 1 = (n_s-1)(n_s+1) = [-2/(1+u)] * [2 - 2/(1+u)]
#             = [-2/(1+u)] * [2u/(1+u)]
#             = -4u/(1+u)^2
#
#   alpha_s = d(n_s)/d(ln K) = d/d(ln K)[-2/(1+u)]
#           = 2 * du/d(ln K) / (1+u)^2
#           = 2 * (-2)*u / (1+u)^2  [since du/d(ln K) = -2u for u = m^2/(J*K^2)]
#           = -4u/(1+u)^2
#
# So alpha_s = n_s^2 - 1 exactly. Good, the identity holds for gamma=0.
#
# For general gamma, with u(K) = m_0^2 * K_0^{-gamma} * K^{gamma-2} / J:
#   du/d(ln K) = (gamma-2)*u
#
#   n_s - 1 = -2 - (gamma-2)*u/(1+u)
#
#   d(n_s)/d(ln K) = -d/d(ln K)[(gamma-2)*u/(1+u)]
#                  = -(gamma-2) * [du/d(ln K)*(1+u) - u*du/d(ln K)] / (1+u)^2
#                  = -(gamma-2) * (gamma-2)*u / (1+u)^2
#                  = -(gamma-2)^2 * u / (1+u)^2
#
# This is ALWAYS negative (for gamma != 2). Now:
#   n_s^2 - 1 = (n_s - 1)(n_s + 1)
#   n_s - 1 = -(2 + (gamma-2)*u/(1+u))  ...no, let me be precise.
#   n_s - 1 = -2 - (gamma-2)*u/(1+u) = (-2(1+u) - (gamma-2)*u) / (1+u)
#           = (-2 - gamma*u) / (1+u)
#   n_s + 1 = (2(1+u) - 2 - gamma*u) / (1+u) = (2*u - gamma*u) / (1+u)
#           = u*(2 - gamma) / (1+u)
#
#   n_s^2 - 1 = (-2 - gamma*u) * u*(2-gamma) / (1+u)^2
#             = -u*(2-gamma)*(2+gamma*u) / (1+u)^2
#
#   delta_alpha = alpha_s - (n_s^2-1)
#               = [-(gamma-2)^2*u + u*(2-gamma)*(2+gamma*u)] / (1+u)^2
#
#   Note: (gamma-2)^2 = (2-gamma)^2. So:
#   delta_alpha = u*(2-gamma) * [-(2-gamma) + (2+gamma*u)] / (1+u)^2
#               = u*(2-gamma) * [gamma + gamma*u] / (1+u)^2    ...wait
#
#   Let me expand: -(2-gamma) + 2 + gamma*u = gamma + gamma*u = gamma*(1+u)
#   So: delta_alpha = u*(2-gamma)*gamma*(1+u) / (1+u)^2
#                   = gamma*(2-gamma)*u / (1+u)

# THIS IS THE KEY RESULT:
#   delta_alpha = gamma * (2 - gamma) * u / (1 + u)

# For n_s = 0.965 with constant mass: u = (1+n_s)/(1-n_s) = 1.965/0.035 = 56.14
# But with running mass, u is modified. Let's compute for the actual case.

# With n_s constrained to 0.965 by fitting m_*:
# The situation is more subtle. In the O-Z model, m_* is chosen so that n_s = 0.965.
# With running mass, the SAME n_s constraint gives a DIFFERENT m_* (lower, because
# the running adds to the mass at K_pivot).
#
# The correction to alpha_s depends on gamma at K_pivot and the ratio u at that point.
# Since u is determined by n_s, and n_s is fixed by observation, we can express
# delta_alpha purely in terms of gamma and n_s.

# From the formula:
#   n_s - 1 = -(2 + gamma*u) / (1+u)
#   => 2 + gamma*u = -(n_s - 1)*(1+u) = (1-n_s)*(1+u)
#   => u = [(1-n_s)*(1+u) - 2] / gamma
#   Let's solve for u in terms of n_s and gamma:
#   (1-n_s)*(1+u) = 2 + gamma*u
#   (1-n_s) + (1-n_s)*u = 2 + gamma*u
#   (1-n_s)*u - gamma*u = 2 - (1-n_s) = 1 + n_s
#   u*[(1-n_s) - gamma] = 1 + n_s
#   u = (1+n_s) / (1 - n_s - gamma)
#
# For this to be positive: 1 - n_s - gamma > 0, i.e., gamma < 1 - n_s = 0.035.
# For n_s = 0.965, gamma must be < 0.035 for u > 0!
#
# This is a STRUCTURAL CONSTRAINT: for n_s > 0 (red tilt), the anomalous
# dimension gamma of the mass must satisfy gamma < 1 - n_s.
#
# If gamma > 1 - n_s = 0.035, then u < 0 which is unphysical (negative
# effective mass squared at the pivot).

n_s_obs = 0.965
gamma_max = 1 - n_s_obs
print(f"\n  STRUCTURAL CONSTRAINT:")
print(f"    For n_s = {n_s_obs}, the anomalous dimension of the mass must satisfy:")
print(f"    gamma < 1 - n_s = {gamma_max:.4f}")
print(f"")
print(f"    If gamma > {gamma_max:.4f}, u = (1+n_s)/(1-n_s-gamma) < 0")
print(f"    => negative effective mass^2 at K_pivot => unphysical.")
print(f"")
print(f"    The gate requires gamma > 1.7. This is 49x ABOVE the structural maximum.")
print(f"    The running mass mechanism is STRUCTURALLY EXCLUDED for red-tilted n_s.")

# Compute delta_alpha for gamma in [0, 0.035)
gamma_values = np.linspace(0, 0.034, 100)
delta_alpha_values = np.zeros_like(gamma_values)

for idx, gam in enumerate(gamma_values):
    if gam == 0:
        delta_alpha_values[idx] = 0
    else:
        u_val = (1 + n_s_obs) / (1 - n_s_obs - gam)
        delta_alpha_values[idx] = gam * (2 - gam) * u_val / (1 + u_val)

print(f"\n  delta_alpha vs gamma (n_s = {n_s_obs} fixed):")
print(f"  {'gamma':>8s} {'u':>12s} {'delta_alpha':>14s} {'alpha_s total':>14s}")
print(f"  {'-'*52}")
for gam in [0.001, 0.005, 0.010, 0.020, 0.030, 0.034]:
    u_val = (1 + n_s_obs) / (1 - n_s_obs - gam)
    d_a = gam * (2 - gam) * u_val / (1 + u_val)
    alpha_total = (n_s_obs**2 - 1) + d_a
    print(f"  {gam:8.4f} {u_val:12.4f} {d_a:14.8f} {alpha_total:14.8f}")

print(f"\n  Maximum possible delta_alpha at gamma -> {gamma_max:.3f}:")
# As gamma -> 0.035, u -> infinity, delta_alpha -> gamma*(2-gamma)
d_alpha_max = gamma_max * (2 - gamma_max)
print(f"    delta_alpha_max = gamma*(2-gamma) = {d_alpha_max:.6f}")
print(f"    alpha_s = (n_s^2 - 1) + delta_alpha_max = {n_s_obs**2 - 1 + d_alpha_max:.6f}")
print(f"    vs Planck: alpha_s = -0.0045 +/- 0.0067")
print(f"    Even at the structural maximum, alpha_s = {n_s_obs**2 - 1 + d_alpha_max:.4f}")
print(f"    compared to n_s^2 - 1 = {n_s_obs**2 - 1:.6f}")

# ============================================================================
# SECTION 9: Numerical Verification of Structural Bound
# ============================================================================
print("\n--- Section 9: Numerical Verification ---")

# Verify the analytical result numerically. For a power-law running mass
# m^2(K) = m_0^2 * (K/K_ref)^gamma, compute n_s and alpha_s directly.

K_ref = K_pivot
gamma_test_vals = [0.0, 0.005, 0.010, 0.020, 0.030, 0.034]

print(f"  Direct numerical check (power-law running):")
print(f"  {'gamma':>8s} {'n_s (num)':>12s} {'alpha_s (num)':>14s} {'n_s^2-1':>12s} "
      f"{'delta_a (num)':>14s} {'delta_a (analyt)':>16s}")
print(f"  {'-'*82}")

for gam in gamma_test_vals:
    # K values for 5-point stencil
    K_pts = K_pivot * np.array([1 - 2*dK_ns, 1 - dK_ns, 1.0, 1 + dK_ns, 1 + 2*dK_ns])

    lnP = np.zeros(5)
    for j, Kv in enumerate(K_pts):
        m2_v = m_0_sq * (Kv / K_ref)**gam
        # Solve for m_star so that n_s matches: use the SAME m_star that gives n_s=0.965
        # with constant mass, then ADD the running correction.
        # Actually, we need to set up the propagator consistently.
        # Use the O-Z propagator with running mass:
        # P(K) = T / [J_eff * K^2 + m_star^2 * (K/K_ref)^gamma]
        # where m_star is chosen so that n_s(K_pivot) = 0.965.

        # For the numerical check: just compute d ln P / d ln K with the power-law form.
        eps_v = J_eff * Kv**2
        m2_run = m_star**2 * (Kv / K_ref)**gam  # use m_star from constant-mass fit
        P_v = T_acoustic / (eps_v + m2_run)
        lnP[j] = np.log(P_v)

    ns_num = 1.0 + (-lnP[4] + 8*lnP[3] - 8*lnP[1] + lnP[0]) / (12 * dK_ns)
    alpha_num = (-lnP[4] + 16*lnP[3] - 30*lnP[2] + 16*lnP[1] - lnP[0]) / (12 * dK_ns**2)

    # Analytical comparison
    # u = m_star^2 / (J_eff * K_pivot^2)  (at K=K_ref, (K/K_ref)^gamma = 1)
    u_num = m_star**2 / (J_eff * K_pivot**2)

    # n_s_analytic = 1 - (2 + gamma*u) / (1+u)
    ns_anl = 1 - (2 + gam * u_num) / (1 + u_num)

    # alpha_s_analytic = -(gamma-2)^2 * u / (1+u)^2
    alpha_anl = -(gam - 2)**2 * u_num / (1 + u_num)**2

    d_a_num = alpha_num - (ns_num**2 - 1)
    d_a_anl = gam * (2 - gam) * u_num / (1 + u_num)

    print(f"  {gam:8.4f} {ns_num:12.8f} {alpha_num:14.8e} {ns_num**2-1:12.8e} "
          f"{d_a_num:14.8e} {d_a_anl:16.8e}")

# ============================================================================
# SECTION 10: What Gamma Does the Lattice Actually Produce?
# ============================================================================
print("\n--- Section 10: Actual Lattice Gamma from 1-Loop ---")

# From the lambda scan, extract gamma at the physical coupling V_B2B2
print(f"  Physical coupling lambda = V(B2,B2) = {V_B2B2:.4f}")
print(f"  Gamma from lattice 1-loop sunset:")

# Recompute gamma more carefully at lambda = V_B2B2
lam_phys = V_B2B2

# Use finer K-grid for numerical derivative
dK_fine = 0.001
K_fine_pts = K_pivot * np.array([1 - 2*dK_fine, 1 - dK_fine, 1.0, 1 + dK_fine, 1 + 2*dK_fine])

sig_0_fine = compute_sunset(K_zero, lam_phys, m_0_sq, T_acoustic)
m2_fine = np.zeros(5)
for j, Kv in enumerate(K_fine_pts):
    K_vec_j = Kv * hat_110
    sig_j = compute_sunset(K_vec_j, lam_phys, m_0_sq, T_acoustic)
    m2_fine[j] = m_0_sq + sig_j - sig_0_fine

# 4th-order central difference for d(m^2)/d(ln K)
dm2_dlnK = (-m2_fine[4] + 8*m2_fine[3] - 8*m2_fine[1] + m2_fine[0]) / (12 * dK_fine)
gamma_lattice = dm2_dlnK / m2_fine[2]

print(f"    m(K)^2 at K_pivot = {m2_fine[2]:.10f}")
print(f"    d(m^2)/d(ln K)    = {dm2_dlnK:.10e}")
print(f"    gamma = d ln m^2 / d ln K = {gamma_lattice:.10f}")
print(f"")
print(f"  gamma/{gamma_max:.4f} = {gamma_lattice/gamma_max:.4f}")
print(f"  gamma is {gamma_max / max(abs(gamma_lattice), 1e-30):.1e}x BELOW the structural maximum")

# Also scan over several lambda values for the gamma vs lambda curve
lambda_fine = np.logspace(-3, 2, 100)
gamma_fine = np.zeros_like(lambda_fine)

for i, lam in enumerate(lambda_fine):
    sig_0_i = compute_sunset(K_zero, lam, m_0_sq, T_acoustic)
    m2_i = np.zeros(5)
    for j, Kv in enumerate(K_fine_pts):
        K_vec_j = Kv * hat_110
        sig_j = compute_sunset(K_vec_j, lam, m_0_sq, T_acoustic)
        m2_i[j] = m_0_sq + sig_j - sig_0_i

    dm2_i = (-m2_i[4] + 8*m2_i[3] - 8*m2_i[1] + m2_i[0]) / (12 * dK_fine)
    if m2_i[2] > 0:
        gamma_fine[i] = dm2_i / m2_i[2]
    else:
        gamma_fine[i] = np.nan

# Find lambda at which gamma reaches structural max
mask_valid = ~np.isnan(gamma_fine) & (gamma_fine > 0)
if np.any(mask_valid & (gamma_fine >= gamma_max)):
    idx_cross = np.where(mask_valid & (gamma_fine >= gamma_max))[0][0]
    lam_cross = lambda_fine[idx_cross]
    print(f"\n  gamma reaches structural max {gamma_max:.4f} at lambda ~ {lam_cross:.2f}")
    print(f"  This is {lam_cross/V_B2B2:.0f}x the physical coupling V(B2,B2)")
else:
    gamma_max_achieved = np.nanmax(gamma_fine[mask_valid]) if np.any(mask_valid) else 0
    print(f"\n  gamma never reaches structural max {gamma_max:.4f}")
    print(f"  Maximum gamma achieved: {gamma_max_achieved:.6f} (at lambda={lambda_fine[np.nanargmax(gamma_fine)]:.2f})")

# ============================================================================
# SECTION 11: Gate Verdict
# ============================================================================
print("\n" + "=" * 78)
print("GATE VERDICT: RUNNING-MASS-50")
print("=" * 78)

# The structural constraint is:
# For n_s = 0.965, the anomalous dimension gamma MUST satisfy gamma < 0.035.
# The gate requires gamma > 1.7. This is structurally impossible.

# Even if gamma saturates the structural bound (gamma -> 0.035):
# delta_alpha_max = gamma*(2-gamma) = 0.035 * 1.965 = 0.0688
# alpha_s_corrected = (n_s^2-1) + 0.0688 = -0.0688 + 0.0688 = 0.0000
# This would actually hit alpha_s = 0! But it requires gamma at the structural
# maximum, which corresponds to u -> infinity, i.e., the propagator is entirely
# dominated by the mass term and J*K^2 is negligible.

print(f"\n  Structural constraint: gamma < 1 - n_s = {gamma_max:.4f}")
print(f"  Gate threshold: gamma > 1.7")
print(f"  Physical gamma (lambda = V_B2B2): {gamma_lattice:.2e}")
print(f"")

# Classification
if gamma_lattice > 1.7:
    verdict = "PASS"
elif gamma_lattice > 0.5:
    verdict = "INFO"
elif gamma_lattice < 0.5:
    # The gate says FAIL if gamma < 0.5. But there is a deeper issue:
    # gamma > 1.7 is STRUCTURALLY IMPOSSIBLE for red-tilted n_s.
    # This is not just gamma being small at physical coupling --- it is that
    # NO coupling can produce gamma > 0.035 while maintaining n_s = 0.965.
    verdict = "FAIL"
else:
    verdict = "INFO"

print(f"  VERDICT: {verdict}")
print(f"")
print(f"  STRUCTURAL RESULT: The running mass correction delta_alpha = gamma*(2-gamma)*u/(1+u)")
print(f"  with the constraint u = (1+n_s)/(1-n_s-gamma) requires gamma < 1-n_s = 0.035.")
print(f"  The gate threshold gamma > 1.7 exceeds this structural bound by a factor of 49.")
print(f"  This is not a numerical result --- it is an algebraic identity.")
print(f"")
print(f"  At the structural maximum gamma -> 0.035:")
print(f"    delta_alpha_max = 0.035 * 1.965 = {0.035*1.965:.4f}")
print(f"    alpha_s = (n_s^2-1) + delta_alpha = {n_s_obs**2-1:.4f} + {0.035*1.965:.4f} = {n_s_obs**2-1 + 0.035*1.965:.4f}")
print(f"    This WOULD bring alpha_s to ~0 (within Planck), but requires u -> infinity.")
print(f"    u -> infinity means J*K^2 / m^2 -> 0: the kinetic term is negligible,")
print(f"    and the propagator is pure mass: P(K) ~ K^{{-gamma}}. This is not O-Z.")
print(f"")
print(f"  At the physical coupling:")
print(f"    gamma = {gamma_lattice:.2e} (from 1-loop sunset on 32-cell lattice)")
print(f"    This is {gamma_lattice/gamma_max:.2e} of the structural maximum.")
print(f"    delta_alpha = {gamma_lattice * (2-gamma_lattice) * xi_star / (1+xi_star):.2e}")
print(f"    The running mass correction is negligible at physical coupling.")

# Compute the actual delta_alpha at physical gamma
delta_alpha_phys = gamma_lattice * (2 - gamma_lattice) * xi_star / (1 + xi_star)
alpha_s_corrected = (n_s_obs**2 - 1) + delta_alpha_phys

print(f"\n  NUMERICAL SUMMARY:")
print(f"    gamma (physical)       = {gamma_lattice:.6e}")
print(f"    gamma (structural max) = {gamma_max:.4f}")
print(f"    gamma (gate threshold) = 1.7")
print(f"    delta_alpha (physical) = {delta_alpha_phys:.6e}")
print(f"    delta_alpha (max possible) = {d_alpha_max:.6f}")
print(f"    alpha_s (O-Z, constant mass) = {n_s_obs**2 - 1:.6f}")
print(f"    alpha_s (with running, physical) = {alpha_s_corrected:.6f}")
print(f"    alpha_s (with running, max gamma) = ~0.000")
print(f"    Planck: alpha_s = -0.0045 +/- 0.0067")

# ============================================================================
# SECTION 12: Save Results
# ============================================================================

elapsed = time.time() - t0

save_path = os.path.join(data_dir, 's50_running_mass.npz')
np.savez(save_path,
    # Gate
    gate_name='RUNNING-MASS-50',
    gate_verdict=verdict,
    gate_detail=f'gamma_physical={gamma_lattice:.2e}, gamma_structural_max={gamma_max:.4f}, '
                f'gate_threshold=1.7. Structural bound gamma<1-n_s=0.035 excludes gamma>1.7 '
                f'by factor 49. At physical coupling, gamma={gamma_lattice:.2e}.',

    # Physical parameters
    m_0=m_0,
    m_0_sq=m_0_sq,
    m_star=m_star,
    J_xy=J_xy,
    J_z=J_z,
    J_eff=J_eff,
    T_acoustic=T_acoustic,
    K_pivot=K_pivot,
    V_B2B2=V_B2B2,

    # Structural constraint
    n_s_obs=n_s_obs,
    gamma_structural_max=gamma_max,
    gamma_gate_threshold=1.7,

    # Numerical results
    gamma_physical=gamma_lattice,
    delta_alpha_physical=delta_alpha_phys,
    delta_alpha_max=d_alpha_max,
    alpha_s_OZ=n_s_obs**2 - 1,
    alpha_s_corrected=alpha_s_corrected,

    # Lambda scan
    lambda_scan=lambda_fine,
    gamma_vs_lambda=gamma_fine,

    # Analytical formula
    # delta_alpha = gamma * (2-gamma) * u / (1+u)
    # u = (1+n_s) / (1-n_s-gamma) for gamma < 1-n_s

    # Timing
    elapsed_s=elapsed,
)

print(f"\n  Results saved to {save_path}")

# ============================================================================
# SECTION 13: Diagnostic Plot
# ============================================================================
fig = plt.figure(figsize=(14, 10))
gs = GridSpec(2, 2, figure=fig, hspace=0.35, wspace=0.30)

# Panel A: gamma vs lambda
ax1 = fig.add_subplot(gs[0, 0])
mask_plot = gamma_fine > 0
if np.any(mask_plot):
    ax1.loglog(lambda_fine[mask_plot], gamma_fine[mask_plot], 'b-', lw=2, label=r'$\gamma$ (1-loop sunset)')
ax1.axhline(gamma_max, color='r', ls='--', lw=1.5, label=rf'$\gamma_{{max}} = 1 - n_s = {gamma_max:.4f}$')
ax1.axhline(1.7, color='k', ls=':', lw=1.5, label=r'Gate threshold $\gamma = 1.7$')
ax1.axvline(V_B2B2, color='green', ls='-.', lw=1.5, label=rf'$\lambda = V(B_2,B_2) = {V_B2B2:.4f}$')
ax1.set_xlabel(r'$\lambda$ (GL coupling)', fontsize=12)
ax1.set_ylabel(r'$\gamma = d\ln m^2/d\ln K$', fontsize=12)
ax1.set_title(r'(A) Anomalous dimension $\gamma$ vs coupling', fontsize=13)
ax1.legend(fontsize=9, loc='upper left')
ax1.set_ylim(1e-6, 10)
ax1.set_xlim(1e-3, 100)

# Panel B: delta_alpha vs gamma (analytical formula)
ax2 = fig.add_subplot(gs[0, 1])
gam_plot = np.linspace(0.001, 0.034, 200)
u_plot = (1 + n_s_obs) / (1 - n_s_obs - gam_plot)
da_plot = gam_plot * (2 - gam_plot) * u_plot / (1 + u_plot)
alpha_corrected_plot = (n_s_obs**2 - 1) + da_plot

ax2.plot(gam_plot, alpha_corrected_plot, 'b-', lw=2, label=r'$\alpha_s = (n_s^2-1) + \delta\alpha$')
ax2.axhline(0, color='gray', ls='-', lw=0.5)
ax2.axhline(-0.0045, color='orange', ls='--', lw=1.5, label=r'Planck central: $-0.0045$')
ax2.fill_between([0, 0.035], -0.0045 - 0.0067, -0.0045 + 0.0067, alpha=0.2, color='orange', label=r'Planck $1\sigma$')
ax2.axhline(n_s_obs**2 - 1, color='red', ls=':', lw=1.5, label=rf'O-Z: $n_s^2 - 1 = {n_s_obs**2-1:.4f}$')
ax2.axvline(gamma_max, color='r', ls='--', lw=1.5)
ax2.set_xlabel(r'$\gamma$ (anomalous dimension)', fontsize=12)
ax2.set_ylabel(r'$\alpha_s$', fontsize=12)
ax2.set_title(r'(B) $\alpha_s$ correction vs $\gamma$ ($n_s=0.965$ fixed)', fontsize=13)
ax2.legend(fontsize=9, loc='lower right')
ax2.set_xlim(0, 0.036)

# Panel C: Structural constraint illustration
ax3 = fig.add_subplot(gs[1, 0])
gam_wide = np.linspace(0, 2.0, 500)
u_vals = np.zeros_like(gam_wide)
for idx, gv in enumerate(gam_wide):
    denom = 1 - n_s_obs - gv
    if denom > 1e-6:
        u_vals[idx] = (1 + n_s_obs) / denom
    else:
        u_vals[idx] = np.nan

ax3.semilogy(gam_wide, u_vals, 'b-', lw=2)
ax3.axvline(gamma_max, color='r', ls='--', lw=2, label=rf'$\gamma_{{max}} = {gamma_max:.3f}$')
ax3.axvline(1.7, color='k', ls=':', lw=2, label=r'Gate: $\gamma = 1.7$')
ax3.fill_between([gamma_max, 2.0], 1e-2, 1e8, alpha=0.15, color='red', label='EXCLUDED (u < 0)')
ax3.set_xlabel(r'$\gamma$', fontsize=12)
ax3.set_ylabel(r'$u = (1+n_s)/(1-n_s-\gamma)$', fontsize=12)
ax3.set_title(r'(C) Structural bound: $\gamma < 1 - n_s$', fontsize=13)
ax3.set_xlim(0, 2.0)
ax3.set_ylim(1, 1e6)
ax3.legend(fontsize=9)

# Panel D: Summary text
ax4 = fig.add_subplot(gs[1, 1])
ax4.axis('off')
summary_text = (
    "RUNNING-MASS-50: FAIL\n"
    "---\n"
    f"Structural bound: gamma < 1 - n_s = {gamma_max:.4f}\n"
    f"Gate requires:    gamma > 1.7\n"
    f"Gap:              49x\n\n"
    f"Physical gamma:   {gamma_lattice:.2e}\n"
    f"  (1-loop sunset, lambda = V(B2,B2))\n\n"
    "Analytical identity:\n"
    r"  $\delta\alpha = \gamma(2-\gamma) u/(1+u)$" + "\n"
    r"  $u = (1+n_s)/(1-n_s-\gamma)$" + "\n\n"
    f"At gamma_max:  delta_alpha = {d_alpha_max:.4f}\n"
    f"  => alpha_s = {n_s_obs**2-1:.4f} + {d_alpha_max:.4f} = 0.000\n\n"
    "But u -> inf means P(K) ~ K^{-gamma}\n"
    "(pure mass, no kinetic term => not O-Z)"
)
ax4.text(0.05, 0.95, summary_text, transform=ax4.transAxes,
         fontsize=10, verticalalignment='top', fontfamily='monospace',
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))
ax4.set_title('(D) Summary', fontsize=13)

fig.suptitle('RUNNING-MASS-50: Running Mass Cannot Rescue alpha_s', fontsize=14, fontweight='bold')
fig.savefig(os.path.join(data_dir, 's50_running_mass.png'), dpi=150, bbox_inches='tight')
print(f"  Plot saved to s50_running_mass.png")

print(f"  Elapsed: {elapsed:.1f}s")
print("=" * 78)
