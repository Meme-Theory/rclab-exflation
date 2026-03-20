#!/usr/bin/env python3
"""
S51 Strutinsky Decomposition of the Spectral Action (STRUTINSKY-51)
===================================================================
Session 51, W2-B — Nazarewicz nuclear-structure-theorist

Physics:
  The Strutinsky energy theorem (1967) decomposes the total energy of a
  finite fermion system into a smooth (Thomas-Fermi / liquid-drop) part
  and an oscillating (shell correction) part:

      E_total = E_smooth + delta_E_shell

  The smooth part captures the bulk (volume + surface) contributions,
  while the oscillating part encodes shell structure — magic numbers,
  gaps, and clustering of single-particle levels.

  Here we apply this decomposition to the spectral action:

      S(Lambda) = sum_n g_n * f(omega_n^2 / Lambda^2)

  where omega_n are eigenvalues of |D_K| on SU(3) and g_n = dim(p,q)^2.

  The smooth spectral action S_smooth(Lambda) is obtained by replacing
  the discrete level density g(E) = sum g_n delta(E - omega_n) with
  a Strutinsky-smoothed density g_smooth(E), obtained by Gaussian
  convolution with width gamma.

  The optimal gamma is determined by the Strutinsky plateau condition:
  dS_smooth / dgamma ~ 0 over a range of gamma values.

  We then extract the effective spectral tilt n_s from each part.

Gate: STRUTINSKY-51
  PASS: Smooth part gives n_s in [0.950, 0.980] at Lambda ~ 12 M_KK
        with |delta_S_shell / S_smooth| < 10%
  FAIL: Shell correction dominates or n_s insensitive to Lambda
  INFO: Both contribute comparably

Method:
  1. At each tau, compute S_exact(Lambda) for Lambda = 4, 6, 8, 10, 12, 14
  2. Compute g_smooth(E) via Gaussian convolution; optimize gamma by plateau
  3. Compute S_smooth(Lambda) = integral g_smooth(E) * f(E^2/Lambda^2) dE
  4. Shell correction delta_S = S_exact - S_smooth
  5. Extract n_s from d ln S / d ln Lambda at each Lambda

Provenance: s44_dos_tau.npz (992 eigenvalues at 5 tau values)
"""

import sys
sys.path.insert(0, r"C:\sandbox\Ainulindale Exflation\tier0-computation")
from canonical_constants import *
import numpy as np
from scipy.integrate import trapezoid
from scipy.interpolate import interp1d
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ============================================================================
#  1. Load Dirac spectrum
# ============================================================================

data = np.load(r"C:\sandbox\Ainulindale Exflation\tier0-computation\s44_dos_tau.npz",
               allow_pickle=True)

tau_values = data['tau_values']  # [0.00, 0.05, 0.10, 0.15, 0.19]
tau_labels = ['0.00', '0.05', '0.10', '0.15', '0.19']

# Cutoff function: Gaussian f(x) = exp(-x)
# This is the standard choice for the spectral action (Chamseddine-Connes)
def f_cutoff(x):
    """Gaussian cutoff: f(x) = exp(-x)"""
    return np.exp(-x)

def f_cutoff_deriv(x):
    """df/dx = -exp(-x)"""
    return -np.exp(-x)

# Lambda values in M_KK units
Lambda_values = np.array([4.0, 6.0, 8.0, 10.0, 12.0, 14.0])

# ============================================================================
#  2. Exact spectral action
# ============================================================================

def compute_S_exact(omega, dim2, Lambda):
    """
    S_exact(Lambda) = sum_n g_n * f(omega_n^2 / Lambda^2)
    where g_n = dim2[n], omega_n = omega[n].
    """
    x = omega**2 / Lambda**2
    return np.sum(dim2 * f_cutoff(x))


# ============================================================================
#  3. Strutinsky smoothing
# ============================================================================

def strutinsky_smooth_density(E_grid, omega, dim2, gamma, p_order=6):
    """
    Compute Strutinsky-smoothed level density on E_grid.

    The Strutinsky prescription (with curvature corrections up to order p):

      g_smooth(E) = (1/gamma*sqrt(pi)) * sum_n g_n * exp(-(E-omega_n)^2/gamma^2)
                    * C_p((E - omega_n)/gamma)

    where C_p is the curvature correction polynomial:
      C_p(u) = sum_{k=0}^{p/2} a_k * H_{2k}(u)

    with H_{2k} the Hermite polynomials and a_k chosen to reproduce
    the first p moments of the smooth density exactly.

    For the standard Strutinsky prescription with p=6 (nuclear standard):
      C_6(u) = 1 + a_1 * H_2(u) + a_2 * H_4(u) + a_3 * H_6(u)
      a_1 = -1/2, a_2 = 1/8, a_3 = -1/48

    This ensures that a smooth polynomial density of degree <= 5 is
    reproduced exactly by the smoothing, regardless of gamma.

    Parameters
    ----------
    E_grid : array, energy grid points
    omega : array, eigenvalues
    dim2 : array, degeneracies (weights)
    gamma : float, smoothing width
    p_order : int, correction polynomial order (default 6, nuclear standard)

    Returns
    -------
    g_smooth : array, smoothed density on E_grid
    """
    g_smooth = np.zeros_like(E_grid, dtype=float)

    # Curvature correction coefficients for p=6 (Strutinsky 1967, Brack-Bhaduri)
    # C_p(u) = sum_{k=0}^{p/2} (-1)^k / (2^k * k!) * L_k^{-1/2}(u^2)
    # where L_k^{-1/2} is the generalized Laguerre polynomial
    # Equivalently: use Hermite polynomial expansion
    def correction_poly(u, p=6):
        """
        Strutinsky curvature correction polynomial C_p(u).
        For p=6: C_6(u) = 1 - (1/2)(u^2 - 1/2) + (1/8)(u^4 - 3u^2 + 3/4)
                          - (1/48)(u^6 - 15/2 u^4 + 45/4 u^2 - 15/8)
        Simplified form using Hermite polynomials.
        """
        u2 = u * u
        if p == 0:
            return np.ones_like(u)
        elif p == 2:
            return 1.0 - 0.5 * (u2 - 0.5)
        elif p == 4:
            return 1.0 - 0.5 * (u2 - 0.5) + (1.0/8.0) * (u2*u2 - 3.0*u2 + 0.75)
        elif p == 6:
            # Full p=6 curvature correction
            # a_1 H_2(u) = (-1/2)(2u^2 - 1)
            # a_2 H_4(u) = (1/8)(4u^4 - 12u^2 + 3)
            # a_3 H_6(u) = (-1/48)(8u^6 - 60u^4 + 90u^2 - 15)
            H2 = 2.0 * u2 - 1.0
            H4 = 4.0 * u2*u2 - 12.0 * u2 + 3.0
            H6 = 8.0 * u2*u2*u2 - 60.0 * u2*u2 + 90.0 * u2 - 15.0
            return 1.0 + (-0.5) * H2 / 2.0 + (0.25) * H4 / 8.0 + (-0.125) * H6 / 48.0
            # = 1 - H2/4 + H4/32 - H6/384
        else:
            raise ValueError(f"p_order={p} not implemented")

    for i_e, E in enumerate(E_grid):
        u = (E - omega) / gamma
        gauss = np.exp(-u**2) / (gamma * np.sqrt(np.pi))
        corr = correction_poly(u, p_order)
        g_smooth[i_e] = np.sum(dim2 * gauss * corr)

    return g_smooth


def compute_S_smooth(E_grid, g_smooth, Lambda):
    """
    S_smooth(Lambda) = integral g_smooth(E) * f(E^2 / Lambda^2) dE
    """
    x = E_grid**2 / Lambda**2
    integrand = g_smooth * f_cutoff(x)
    return trapezoid(integrand, E_grid)


# ============================================================================
#  4. Plateau condition for gamma optimization
# ============================================================================

def find_plateau_gamma(omega, dim2, Lambda_test, E_grid,
                       gamma_range=np.linspace(0.02, 0.40, 100)):
    """
    Find optimal gamma by the Strutinsky plateau condition:
    S_smooth(Lambda; gamma) should be approximately constant over a
    range of gamma values. The plateau gamma is where |dS_smooth/dgamma|
    is minimized.

    Returns
    -------
    gamma_opt : float, optimal smoothing width
    S_vs_gamma : array, S_smooth at each gamma
    gamma_grid : array, gamma values tested
    """
    S_vs_gamma = np.zeros(len(gamma_range))

    for i_g, gam in enumerate(gamma_range):
        g_sm = strutinsky_smooth_density(E_grid, omega, dim2, gam)
        S_vs_gamma[i_g] = compute_S_smooth(E_grid, g_sm, Lambda_test)

    # Find plateau: where |dS/dgamma| is minimized
    dS_dgamma = np.gradient(S_vs_gamma, gamma_range)

    # Look for the plateau region: where |dS/dgamma| < threshold
    # Exclude very small gamma (< 0.05) where shell structure dominates
    mask = gamma_range >= 0.05
    abs_deriv = np.abs(dS_dgamma[mask])
    gamma_masked = gamma_range[mask]

    # Find the gamma where |dS/dgamma| is smallest
    idx_min = np.argmin(abs_deriv)
    gamma_opt = gamma_masked[idx_min]

    return gamma_opt, S_vs_gamma, gamma_range, dS_dgamma


# ============================================================================
#  5. Spectral tilt extraction
# ============================================================================

def extract_n_s(S_array, Lambda_array):
    """
    Extract effective spectral tilt n_s from the spectral action.

    The spectral action S(Lambda) ~ Lambda^{n_eff} in the scaling regime.
    The spectral index of primordial perturbations is related to the
    logarithmic derivative:

      n_eff(Lambda) = d ln S / d ln Lambda

    In the Seeley-DeWitt expansion:
      S(Lambda) ~ f_0 Lambda^8 + f_2 Lambda^6 R + f_4 Lambda^4 (R^2 + ...)
    so n_eff -> 8 for large Lambda. But the DEVIATION from this controls
    the spectral tilt of fluctuations:

      n_s - 1 = d ln (dS/dLambda) / d ln Lambda - (d ln S / d ln Lambda)

    More precisely, for the spectral action generating the power spectrum
    of tau fluctuations, the tilt is:

      n_s - 1 = d ln chi_SA / d ln K

    where chi_SA(K) = d^2 S / dtau^2 evaluated at K.

    For the Strutinsky context, we compute the simpler effective exponent:
      n_eff(Lambda) = d ln S / d ln Lambda

    and the running:
      dn_eff / d ln Lambda

    which measures how the spectral action departs from pure power-law.
    """
    ln_Lambda = np.log(Lambda_array)
    ln_S = np.log(np.abs(S_array))

    # Central differences for interior points, one-sided for edges
    n_eff = np.gradient(ln_S, ln_Lambda)

    return n_eff


def extract_n_s_from_tau_variation(S_tau_array, tau_arr, Lambda_array):
    """
    Extract n_s from the tau-dependence of S at each Lambda.

    The physical observable is the power spectrum of tau fluctuations:
      P(K) ~ 1 / chi_SA(K)
    where chi_SA = d^2 S / dtau^2.

    We approximate chi_SA(Lambda) from the tau-grid:
      chi_SA(Lambda) ~ [S(tau+dtau, Lambda) - 2 S(tau, Lambda) + S(tau-dtau, Lambda)] / dtau^2

    Then n_s - 1 = d ln chi_SA / d ln Lambda.
    """
    # Compute chi_SA = d^2 S / d tau^2 at each Lambda
    # Using 5 tau points, compute second derivative at tau = 0.10 (central)
    n_tau = len(tau_arr)
    chi_SA = np.zeros(len(Lambda_array))

    for i_L in range(len(Lambda_array)):
        S_of_tau = S_tau_array[:, i_L]
        # Second derivative using central differences at tau_fold = 0.19
        # Use all 5 points for a 4th-order finite difference
        # tau = [0.00, 0.05, 0.10, 0.15, 0.19]
        # Non-uniform spacing -> use polynomial fit
        coeffs = np.polyfit(tau_arr, S_of_tau, 4)
        # d^2 S / dtau^2 = 2*c2 + 6*c1*tau + 12*c0*tau^2
        poly_2nd = np.polyder(np.poly1d(coeffs), 2)
        chi_SA[i_L] = poly_2nd(tau_fold)

    # n_s - 1 = d ln chi_SA / d ln Lambda
    ln_Lambda = np.log(Lambda_array)
    ln_chi = np.log(np.abs(chi_SA))
    n_s_minus_1 = np.gradient(ln_chi, ln_Lambda)
    n_s = 1.0 + n_s_minus_1

    return n_s, chi_SA


# ============================================================================
#  6. Main computation
# ============================================================================

print("=" * 72)
print("  STRUTINSKY-51: Strutinsky Decomposition of the Spectral Action")
print("=" * 72)

# Storage
S_exact_all = np.zeros((len(tau_values), len(Lambda_values)))
S_smooth_all = np.zeros((len(tau_values), len(Lambda_values)))
delta_S_all = np.zeros((len(tau_values), len(Lambda_values)))
gamma_opt_all = np.zeros(len(tau_values))
n_eff_exact = np.zeros((len(tau_values), len(Lambda_values)))
n_eff_smooth = np.zeros((len(tau_values), len(Lambda_values)))
n_eff_shell = np.zeros((len(tau_values), len(Lambda_values)))

# Store plateau data
plateau_data = {}

for i_tau, (tau_val, t_str) in enumerate(zip(tau_values, tau_labels)):
    omega = data[f'tau{t_str}_all_omega']
    dim2 = data[f'tau{t_str}_all_dim2']

    print(f"\n--- tau = {tau_val:.2f} ---")
    print(f"  {len(omega)} eigenvalues, omega in [{omega.min():.4f}, {omega.max():.4f}]")
    print(f"  Total weight: {dim2.sum():.0f}")

    # Energy grid for smooth density (extend slightly beyond spectrum)
    E_min = omega.min() - 0.3
    E_max = omega.max() + 0.3
    E_grid = np.linspace(max(E_min, 0.01), E_max, 5000)
    dE = E_grid[1] - E_grid[0]

    # ----- Step 1: Exact spectral action -----
    for i_L, Lam in enumerate(Lambda_values):
        S_exact_all[i_tau, i_L] = compute_S_exact(omega, dim2, Lam)

    print(f"  S_exact(Lambda): ", end="")
    for i_L, Lam in enumerate(Lambda_values):
        print(f"  {Lam:.0f}->{S_exact_all[i_tau, i_L]:.2f}", end="")
    print()

    # ----- Step 2: Find optimal gamma via plateau condition -----
    gamma_range = np.linspace(0.02, 0.50, 200)
    Lambda_test = 12.0  # Test plateau at the target Lambda

    gamma_opt, S_vs_gamma, gamma_grid, dS_dgamma = \
        find_plateau_gamma(omega, dim2, Lambda_test, E_grid, gamma_range)

    gamma_opt_all[i_tau] = gamma_opt
    plateau_data[t_str] = {
        'gamma_grid': gamma_grid,
        'S_vs_gamma': S_vs_gamma,
        'dS_dgamma': dS_dgamma,
    }

    print(f"  Plateau gamma = {gamma_opt:.4f} M_KK (at Lambda = {Lambda_test})")

    # ----- Step 3: Smooth spectral action at optimal gamma -----
    g_smooth = strutinsky_smooth_density(E_grid, omega, dim2, gamma_opt)

    # Verify normalization: integral of g_smooth should ~ sum(dim2)
    norm_smooth = trapezoid(g_smooth, E_grid)
    print(f"  Smooth density normalization: {norm_smooth:.1f} (exact: {dim2.sum():.0f})")

    for i_L, Lam in enumerate(Lambda_values):
        S_smooth_all[i_tau, i_L] = compute_S_smooth(E_grid, g_smooth, Lam)
        delta_S_all[i_tau, i_L] = S_exact_all[i_tau, i_L] - S_smooth_all[i_tau, i_L]

    print(f"  S_smooth(Lambda):", end="")
    for i_L, Lam in enumerate(Lambda_values):
        print(f"  {Lam:.0f}->{S_smooth_all[i_tau, i_L]:.2f}", end="")
    print()

    frac_shell = delta_S_all[i_tau, :] / S_smooth_all[i_tau, :]
    print(f"  delta_S/S_smooth:", end="")
    for i_L, Lam in enumerate(Lambda_values):
        print(f"  {Lam:.0f}->{frac_shell[i_L]:.4f}", end="")
    print()

    # ----- Step 4: Effective exponents -----
    n_eff_exact[i_tau] = extract_n_s(S_exact_all[i_tau], Lambda_values)
    n_eff_smooth[i_tau] = extract_n_s(S_smooth_all[i_tau], Lambda_values)
    # For shell correction, be careful with sign
    # delta_S can change sign, so n_eff_shell is less meaningful
    for i_L in range(len(Lambda_values)):
        if abs(delta_S_all[i_tau, i_L]) > 1e-10:
            n_eff_shell[i_tau, i_L] = np.nan  # Will compute differently
        else:
            n_eff_shell[i_tau, i_L] = 0.0


# ============================================================================
#  7. Extract n_s from tau-variation (the physical observable)
# ============================================================================

print("\n" + "=" * 72)
print("  n_s from tau-variation of S(tau, Lambda)")
print("=" * 72)

n_s_exact, chi_SA_exact = extract_n_s_from_tau_variation(
    S_exact_all, tau_values, Lambda_values)
n_s_smooth, chi_SA_smooth = extract_n_s_from_tau_variation(
    S_smooth_all, tau_values, Lambda_values)
n_s_shell, chi_SA_shell = extract_n_s_from_tau_variation(
    delta_S_all, tau_values, Lambda_values)

print(f"\n  n_s from chi_SA (exact, smooth, shell) at each Lambda:")
print(f"  {'Lambda':>8s} {'n_s_exact':>10s} {'n_s_smooth':>10s} {'n_s_shell':>10s}"
      f" {'chi_exact':>12s} {'chi_smooth':>12s} {'|dS/S|':>10s}")
for i_L, Lam in enumerate(Lambda_values):
    frac = abs(chi_SA_shell[i_L]) / abs(chi_SA_smooth[i_L]) if chi_SA_smooth[i_L] != 0 else np.inf
    print(f"  {Lam:8.1f} {n_s_exact[i_L]:10.4f} {n_s_smooth[i_L]:10.4f} {n_s_shell[i_L]:10.4f}"
          f" {chi_SA_exact[i_L]:12.2f} {chi_SA_smooth[i_L]:12.2f} {frac:10.4f}")


# ============================================================================
#  8. Alternative n_s extraction: Seeley-DeWitt scaling
# ============================================================================

print("\n" + "=" * 72)
print("  Effective exponent n_eff = d ln S / d ln Lambda")
print("=" * 72)

# The Seeley-DeWitt expansion gives:
# S(Lambda) = f_0 * a_0 * Lambda^8 + f_2 * a_2 * Lambda^6 + f_4 * a_4 * Lambda^4 + ...
# (for 8-dimensional D_K: 4D spacetime + 4 internal, doubled by spinor)
# Actually for the internal D_K alone on SU(3) (dim 8):
# S = Tr f(D_K^2/Lambda^2)
# Using Seeley-DeWitt on a compact 8-dim manifold:
# S ~ f_0 Lambda^8 Vol + f_2 Lambda^6 (scalar curv) + f_4 Lambda^4 + ...
# But SU(3) is 8-dimensional, so the leading term is Lambda^8.
# However, the D_K is a finite matrix (992 x 101984 total states),
# so for Lambda >> omega_max, S -> sum(dim2) * f(0) = 101984 (constant).
# The Seeley-DeWitt scaling only applies for Lambda << omega_max.

# For our eigenvalue spectrum on SU(3) (8-dim with spinor = 16-comp):
# D_K^2 has eigenvalues omega_n^2
# Tr f(D_K^2/Lambda^2) = sum g_n exp(-omega_n^2/Lambda^2)
# For Lambda >> omega_max: S -> sum(g_n) = 101984
# For Lambda << omega_min: S -> sum(g_n) * exp(-omega_min^2/Lambda^2) -> 0

# The tilt n_s from the MODULUS FLUCTUATION power spectrum is:
# P(K) ~ 1 / (d^2 S/dtau^2) evaluated at some K-Lambda correspondence
# n_s - 1 = d ln(d^2S/dtau^2) / d ln Lambda

# Let's also compute the pure Lambda-scaling exponent for reference
print(f"\n  n_eff = d ln S_exact / d ln Lambda:")
print(f"  {'tau':>6s}", end="")
for Lam in Lambda_values:
    print(f" {Lam:7.0f}", end="")
print()
for i_tau in range(len(tau_values)):
    print(f"  {tau_values[i_tau]:6.2f}", end="")
    for i_L in range(len(Lambda_values)):
        print(f" {n_eff_exact[i_tau, i_L]:7.3f}", end="")
    print()

print(f"\n  n_eff = d ln S_smooth / d ln Lambda:")
print(f"  {'tau':>6s}", end="")
for Lam in Lambda_values:
    print(f" {Lam:7.0f}", end="")
print()
for i_tau in range(len(tau_values)):
    print(f"  {tau_values[i_tau]:6.2f}", end="")
    for i_L in range(len(Lambda_values)):
        print(f" {n_eff_smooth[i_tau, i_L]:7.3f}", end="")
    print()


# ============================================================================
#  9. Strutinsky shell energy analysis at the fold
# ============================================================================

print("\n" + "=" * 72)
print("  Strutinsky shell correction analysis at tau = 0.19 (fold)")
print("=" * 72)

i_fold = 4  # tau = 0.19
omega_fold = data['tau0.19_all_omega']
dim2_fold = data['tau0.19_all_dim2']

# Study plateau condition in detail
print(f"\n  Plateau condition (Lambda = 12 M_KK):")
gamma_fine = np.linspace(0.02, 0.50, 500)
E_grid_fold = np.linspace(max(omega_fold.min() - 0.3, 0.01),
                           omega_fold.max() + 0.3, 5000)

S_vs_gamma_fold = np.zeros(len(gamma_fine))
for i_g, gam in enumerate(gamma_fine):
    g_sm = strutinsky_smooth_density(E_grid_fold, omega_fold, dim2_fold, gam)
    S_vs_gamma_fold[i_g] = compute_S_smooth(E_grid_fold, g_sm, 12.0)

dS_dg_fold = np.gradient(S_vs_gamma_fold, gamma_fine)
d2S_dg2_fold = np.gradient(dS_dg_fold, gamma_fine)

# Find plateau: |dS/dgamma| < threshold for gamma > 0.05
mask = gamma_fine >= 0.05
abs_deriv = np.abs(dS_dg_fold[mask])
idx_min = np.argmin(abs_deriv)
gamma_plateau = gamma_fine[mask][idx_min]

print(f"  Optimal gamma (plateau): {gamma_plateau:.4f} M_KK")
print(f"  |dS/dgamma| at plateau: {abs_deriv[idx_min]:.2f}")
print(f"  S_smooth at plateau: {S_vs_gamma_fold[mask][idx_min]:.2f}")

# Compute at several gamma values near plateau to assess stability
print(f"\n  Stability around plateau:")
for gam_test in [0.05, 0.08, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40]:
    g_sm = strutinsky_smooth_density(E_grid_fold, omega_fold, dim2_fold, gam_test)
    S_sm = compute_S_smooth(E_grid_fold, g_sm, 12.0)
    S_ex = S_exact_all[i_fold, 4]  # Lambda = 12
    frac = (S_ex - S_sm) / S_sm
    print(f"    gamma = {gam_test:.2f}: S_smooth = {S_sm:.2f}, "
          f"delta_S = {S_ex - S_sm:.2f}, delta_S/S_smooth = {frac:.4f}")


# ============================================================================
#  10. Physical level spacing analysis
# ============================================================================

print("\n" + "=" * 72)
print("  Level spacing analysis at the fold")
print("=" * 72)

# Sort unique eigenvalues
u_omega = np.unique(omega_fold)
spacings = np.diff(u_omega)
mean_spacing = np.mean(spacings)
bandwidth = u_omega.max() - u_omega.min()

print(f"  Number of unique eigenvalues: {len(u_omega)}")
print(f"  Bandwidth: {bandwidth:.4f} M_KK")
print(f"  Mean level spacing: {mean_spacing:.6f} M_KK")
print(f"  gamma_opt / mean_spacing = {gamma_plateau / mean_spacing:.1f}")
print(f"  gamma_opt / bandwidth = {gamma_plateau / bandwidth:.4f}")

# The Strutinsky condition: gamma should be ~ several level spacings
# but << bandwidth. Typical nuclear physics: gamma ~ 1-2 * hbar*omega_0
# where omega_0 is the shell spacing (~ major shell gap)

# Identify shell-like gaps: large spacings
threshold = 3 * mean_spacing
large_gaps = [(u_omega[i], u_omega[i+1], spacings[i])
              for i in range(len(spacings)) if spacings[i] > threshold]
print(f"\n  Shell gaps (> {threshold:.5f} M_KK = 3 x mean spacing):")
for e1, e2, gap in large_gaps[:15]:
    print(f"    [{e1:.4f}, {e2:.4f}]: gap = {gap:.5f} M_KK ({gap/mean_spacing:.1f} x mean)")


# ============================================================================
#  11. Gamma-independent Strutinsky: Thomas-Fermi from Weyl's law
# ============================================================================

print("\n" + "=" * 72)
print("  Thomas-Fermi (Weyl's law) spectral action")
print("=" * 72)

# For the Dirac operator on an 8-dimensional compact manifold,
# Weyl's law gives the integrated DOS:
#   N(E) = C_Weyl * E^8 * Vol + lower-order terms
# where C_Weyl = Vol(S^7) / (2*pi)^8 for the sphere contribution.
#
# But our D_K eigenvalues are O(1) in M_KK units and there are only
# 992 of them (finite matrix), so the Weyl limit is not fully reached.
# Instead, we fit the cumulative DOS to a polynomial.

# Cumulative DOS (weighted)
sorted_idx = np.argsort(omega_fold)
omega_sorted = omega_fold[sorted_idx]
dim2_sorted = dim2_fold[sorted_idx]
N_cum = np.cumsum(dim2_sorted)

# Fit N(E) to a polynomial in E
# N(E) = a * E^n + b * E^{n-2} + ... (Weyl form)
# For practical purposes, use a general polynomial
poly_degree = 8
coeffs_N = np.polyfit(omega_sorted, N_cum, poly_degree)
N_fit = np.polyval(coeffs_N, omega_sorted)

# Thomas-Fermi density: g_TF(E) = dN/dE
coeffs_g = np.polyder(np.poly1d(coeffs_N))

# Thomas-Fermi spectral action
g_TF = np.polyval(coeffs_g.coeffs, E_grid_fold)
# Clip negative values (unphysical)
g_TF = np.maximum(g_TF, 0.0)

S_TF_all = np.zeros(len(Lambda_values))
for i_L, Lam in enumerate(Lambda_values):
    x = E_grid_fold**2 / Lam**2
    integrand = g_TF * f_cutoff(x)
    S_TF_all[i_L] = trapezoid(integrand, E_grid_fold)

print(f"\n  Thomas-Fermi (polynomial fit, degree {poly_degree}):")
print(f"  {'Lambda':>8s} {'S_exact':>12s} {'S_TF':>12s} {'delta/S_TF':>12s}")
for i_L, Lam in enumerate(Lambda_values):
    frac = (S_exact_all[i_fold, i_L] - S_TF_all[i_L]) / S_TF_all[i_L]
    print(f"  {Lam:8.1f} {S_exact_all[i_fold, i_L]:12.2f} {S_TF_all[i_L]:12.2f} {frac:12.4f}")

# n_eff from Thomas-Fermi
n_eff_TF = extract_n_s(S_TF_all, Lambda_values)
print(f"\n  n_eff (TF): {n_eff_TF}")


# ============================================================================
#  12. Gate verdict
# ============================================================================

print("\n" + "=" * 72)
print("  GATE VERDICT: STRUTINSKY-51")
print("=" * 72)

# Key numbers at Lambda = 12 M_KK, tau = 0.19
i_L_12 = 4  # Lambda = 12
frac_shell_12 = abs(delta_S_all[i_fold, i_L_12]) / abs(S_smooth_all[i_fold, i_L_12])

print(f"\n  At Lambda = 12 M_KK, tau = 0.19:")
print(f"    S_exact     = {S_exact_all[i_fold, i_L_12]:.4f}")
print(f"    S_smooth    = {S_smooth_all[i_fold, i_L_12]:.4f}")
print(f"    delta_S     = {delta_S_all[i_fold, i_L_12]:.4f}")
print(f"    |delta_S/S| = {frac_shell_12:.4f} ({frac_shell_12*100:.2f}%)")
print(f"    gamma_opt   = {gamma_plateau:.4f} M_KK")

print(f"\n  n_s from chi_SA = d^2 S/dtau^2:")
print(f"    n_s(exact)  at Lambda=12 = {n_s_exact[i_L_12]:.4f}")
print(f"    n_s(smooth) at Lambda=12 = {n_s_smooth[i_L_12]:.4f}")
print(f"    n_s(shell)  at Lambda=12 = {n_s_shell[i_L_12]:.4f}")

print(f"\n  n_eff = d ln S / d ln Lambda:")
print(f"    n_eff(exact)  at Lambda=12 = {n_eff_exact[i_fold, i_L_12]:.4f}")
print(f"    n_eff(smooth) at Lambda=12 = {n_eff_smooth[i_fold, i_L_12]:.4f}")

# Gate criteria
gate_n_s_low, gate_n_s_high = 0.950, 0.980
gate_shell_frac = 0.10

n_s_test = n_s_smooth[i_L_12]
shell_frac_test = frac_shell_12

print(f"\n  Gate criteria:")
print(f"    n_s(smooth) in [{gate_n_s_low}, {gate_n_s_high}]? "
      f"n_s = {n_s_test:.4f} -> {'PASS' if gate_n_s_low <= n_s_test <= gate_n_s_high else 'FAIL'}")
print(f"    |delta_S/S| < {gate_shell_frac}? "
      f"|delta_S/S| = {shell_frac_test:.4f} -> {'PASS' if shell_frac_test < gate_shell_frac else 'FAIL'}")

if gate_n_s_low <= n_s_test <= gate_n_s_high and shell_frac_test < gate_shell_frac:
    verdict = "PASS"
elif shell_frac_test >= gate_shell_frac:
    verdict = "FAIL (shell correction dominates)"
else:
    n_s_check_all_Lambda = True
    for i_L in range(len(Lambda_values)):
        if gate_n_s_low <= n_s_smooth[i_L] <= gate_n_s_high:
            n_s_check_all_Lambda = False
            break
    if n_s_check_all_Lambda:
        verdict = "FAIL (n_s insensitive to Lambda or outside range)"
    else:
        verdict = "INFO (both smooth and shell contribute)"

print(f"\n  VERDICT: {verdict}")


# ============================================================================
#  13. Save data
# ============================================================================

outfile = r"C:\sandbox\Ainulindale Exflation\tier0-computation\s51_strutinsky.npz"
np.savez(outfile,
         # Input
         tau_values=tau_values,
         Lambda_values=Lambda_values,
         # Exact
         S_exact=S_exact_all,
         # Strutinsky smooth
         S_smooth=S_smooth_all,
         gamma_opt=gamma_opt_all,
         # Shell correction
         delta_S=delta_S_all,
         # Effective exponents
         n_eff_exact=n_eff_exact,
         n_eff_smooth=n_eff_smooth,
         # n_s from chi_SA
         n_s_exact_chiSA=n_s_exact,
         n_s_smooth_chiSA=n_s_smooth,
         n_s_shell_chiSA=n_s_shell,
         chi_SA_exact=chi_SA_exact,
         chi_SA_smooth=chi_SA_smooth,
         chi_SA_shell=chi_SA_shell,
         # Thomas-Fermi
         S_TF=S_TF_all,
         n_eff_TF=n_eff_TF,
         # Plateau data at fold
         gamma_plateau_fold=gamma_plateau,
         gamma_fine=gamma_fine,
         S_vs_gamma_fold=S_vs_gamma_fold,
         dS_dg_fold=dS_dg_fold,
         # Gate
         verdict=np.array(verdict))

print(f"\n  Data saved to: {outfile}")


# ============================================================================
#  14. Diagnostic plots
# ============================================================================

fig, axes = plt.subplots(3, 3, figsize=(18, 16))
fig.suptitle('STRUTINSKY-51: Strutinsky Decomposition of the Spectral Action',
             fontsize=14, fontweight='bold')

# (0,0): S_exact vs Lambda at all tau
ax = axes[0, 0]
for i_tau, tau_val in enumerate(tau_values):
    ax.semilogy(Lambda_values, S_exact_all[i_tau], 'o-',
                label=f'tau={tau_val:.2f}', markersize=5)
ax.set_xlabel('Lambda (M_KK)')
ax.set_ylabel('S_exact(Lambda)')
ax.set_title('Exact spectral action')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# (0,1): S_smooth vs Lambda at fold, with S_exact overlay
ax = axes[0, 1]
ax.semilogy(Lambda_values, S_exact_all[i_fold], 'ko-', label='S_exact', markersize=6)
ax.semilogy(Lambda_values, S_smooth_all[i_fold], 'rs--', label='S_smooth (Strut.)', markersize=6)
ax.semilogy(Lambda_values, S_TF_all, 'b^:', label='S_TF (Weyl poly)', markersize=6)
ax.set_xlabel('Lambda (M_KK)')
ax.set_ylabel('S(Lambda)')
ax.set_title(f'Exact vs Smooth at fold (tau={tau_fold})')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# (0,2): Shell correction fraction vs Lambda
ax = axes[0, 2]
for i_tau, tau_val in enumerate(tau_values):
    frac = delta_S_all[i_tau] / S_smooth_all[i_tau]
    ax.plot(Lambda_values, frac * 100, 'o-', label=f'tau={tau_val:.2f}', markersize=5)
ax.axhline(y=10, color='r', linestyle='--', alpha=0.5, label='10% threshold')
ax.axhline(y=-10, color='r', linestyle='--', alpha=0.5)
ax.set_xlabel('Lambda (M_KK)')
ax.set_ylabel('delta_S / S_smooth (%)')
ax.set_title('Shell correction fraction')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# (1,0): Plateau condition at fold
ax = axes[1, 0]
ax.plot(gamma_fine, S_vs_gamma_fold, 'b-', linewidth=1.5)
ax.axvline(x=gamma_plateau, color='r', linestyle='--', alpha=0.7,
           label=f'gamma_opt = {gamma_plateau:.3f}')
ax.set_xlabel('gamma (M_KK)')
ax.set_ylabel('S_smooth(Lambda=12)')
ax.set_title(f'Plateau condition (tau={tau_fold})')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# (1,1): dS/dgamma for plateau identification
ax = axes[1, 1]
ax.plot(gamma_fine, dS_dg_fold, 'b-', linewidth=1.5)
ax.axvline(x=gamma_plateau, color='r', linestyle='--', alpha=0.7)
ax.axhline(y=0, color='k', linestyle='-', alpha=0.3)
ax.set_xlabel('gamma (M_KK)')
ax.set_ylabel('dS_smooth / dgamma')
ax.set_title('Plateau derivative')
ax.grid(True, alpha=0.3)

# (1,2): Smoothed vs exact DOS at fold
ax = axes[1, 2]
E_grid_fold_fine = np.linspace(max(omega_fold.min() - 0.2, 0.01),
                                omega_fold.max() + 0.2, 5000)
g_sm_fold = strutinsky_smooth_density(E_grid_fold_fine, omega_fold, dim2_fold, gamma_plateau)
g_sm_fold_narrow = strutinsky_smooth_density(E_grid_fold_fine, omega_fold, dim2_fold, 0.03)

ax.plot(E_grid_fold_fine, g_sm_fold, 'b-', linewidth=1.5, label=f'Strutinsky (gamma={gamma_plateau:.3f})')
ax.plot(E_grid_fold_fine, g_sm_fold_narrow, 'g-', alpha=0.5, linewidth=0.8, label='gamma=0.03 (shell)')
ax.plot(E_grid_fold_fine, np.maximum(np.polyval(coeffs_g.coeffs, E_grid_fold_fine), 0),
        'r--', linewidth=1.5, label='Thomas-Fermi (poly)')
# Mark eigenvalue positions
u_omega_fold = np.unique(omega_fold)
ax.vlines(u_omega_fold, 0, 500, colors='k', alpha=0.05, linewidth=0.3)
ax.set_xlabel('E (M_KK)')
ax.set_ylabel('g(E)')
ax.set_title(f'Level density at fold')
ax.legend(fontsize=8)
ax.set_xlim(omega_fold.min() - 0.1, omega_fold.max() + 0.1)
ax.grid(True, alpha=0.3)

# (2,0): n_eff(Lambda) for exact and smooth
ax = axes[2, 0]
ax.plot(Lambda_values, n_eff_exact[i_fold], 'ko-', label='n_eff(exact)', markersize=6)
ax.plot(Lambda_values, n_eff_smooth[i_fold], 'rs--', label='n_eff(smooth)', markersize=6)
ax.plot(Lambda_values, n_eff_TF, 'b^:', label='n_eff(TF)', markersize=6)
ax.set_xlabel('Lambda (M_KK)')
ax.set_ylabel('n_eff = d ln S / d ln Lambda')
ax.set_title('Effective exponent vs Lambda')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# (2,1): n_s from chi_SA
ax = axes[2, 1]
ax.plot(Lambda_values, n_s_exact, 'ko-', label='n_s(exact)', markersize=6)
ax.plot(Lambda_values, n_s_smooth, 'rs--', label='n_s(smooth)', markersize=6)
ax.axhspan(0.950, 0.980, color='green', alpha=0.15, label='Target [0.950, 0.980]')
ax.axhline(y=0.965, color='g', linestyle=':', alpha=0.5)
ax.set_xlabel('Lambda (M_KK)')
ax.set_ylabel('n_s')
ax.set_title('Spectral tilt from chi_SA(Lambda)')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# (2,2): Summary table as text
ax = axes[2, 2]
ax.axis('off')
summary_text = (
    f"STRUTINSKY-51 GATE VERDICT: {verdict}\n\n"
    f"Lambda = 12 M_KK, tau = {tau_fold}:\n"
    f"  S_exact     = {S_exact_all[i_fold, i_L_12]:.2f}\n"
    f"  S_smooth    = {S_smooth_all[i_fold, i_L_12]:.2f}\n"
    f"  delta_S     = {delta_S_all[i_fold, i_L_12]:.2f}\n"
    f"  |dS/S|      = {frac_shell_12:.4f} ({frac_shell_12*100:.2f}%)\n"
    f"  gamma_opt   = {gamma_plateau:.4f} M_KK\n\n"
    f"  n_s(exact, chi_SA)  = {n_s_exact[i_L_12]:.4f}\n"
    f"  n_s(smooth, chi_SA) = {n_s_smooth[i_L_12]:.4f}\n"
    f"  n_s(shell, chi_SA)  = {n_s_shell[i_L_12]:.4f}\n\n"
    f"  n_eff(exact)  = {n_eff_exact[i_fold, i_L_12]:.4f}\n"
    f"  n_eff(smooth) = {n_eff_smooth[i_fold, i_L_12]:.4f}\n\n"
    f"  Gate: n_s in [0.950, 0.980]? {gate_n_s_low <= n_s_test <= gate_n_s_high}\n"
    f"  Gate: |dS/S| < 10%?         {shell_frac_test < gate_shell_frac}"
)
ax.text(0.05, 0.95, summary_text, transform=ax.transAxes,
        fontsize=9, verticalalignment='top', fontfamily='monospace',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

plt.tight_layout()
plt.savefig(r"C:\sandbox\Ainulindale Exflation\tier0-computation\s51_strutinsky.png",
            dpi=150, bbox_inches='tight')
print(f"  Plot saved to: tier0-computation/s51_strutinsky.png")

print("\n  STRUTINSKY-51 COMPLETE.")
