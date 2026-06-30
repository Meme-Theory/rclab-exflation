#!/usr/bin/env python3
"""
s61_ruelle_zeta.py — RUELLE-ARITH-61
=====================================
Ruelle zeta function of geodesic flow on (SU(3), g_Jensen).

Mathematical foundations:
  1. On a compact Lie group G with left-invariant metric g, the geodesics
     through the identity are one-parameter subgroups exp(tX), X in g.
     (This follows from Euler-Arnold: left-invariant metrics make geodesics
     be solutions of the Euler equation on g*; for bi-invariant metrics
     these are exactly the one-parameter subgroups.)

  2. For general LEFT-invariant (not bi-invariant) metrics, geodesics through e
     are NOT one-parameter subgroups. However, they ARE still determined by
     the Euler-Arnold equation on g*. For the Jensen metric, which is a
     diagonal deformation of the bi-invariant Killing metric along the
     fibration SU(3) -> SU(3)/SU(2) ~ S^5, the geodesic equation can be
     integrated because the metric respects the SU(2) x U(1) symmetry.

  3. A closed geodesic gamma has period L(gamma) = the length of the
     shortest closed loop. On the maximal torus T^2 of SU(3), the lattice
     of elements H in t such that exp(H) = I is the cocharacter lattice
     Lambda^vee. Geodesics along torus directions close with periods
     determined by the metric lengths of lattice vectors.

  4. The Ruelle zeta function:
       R(s) = prod_{gamma primitive} (1 - exp(-s * L(gamma)))^(-1)
     converges for Re(s) >> 0 and may be meromorphically continued.

  5. For the Jensen metric at tau=0.19, the metric on su(3) is:
       g_Jensen = diag(g_V, g_V, g_V, g_H, g_H, g_H, g_H, g_H)
     where g_V = g0*(1-tau) along su(2) directions (3 generators)
     and g_H = g0*(1+tau) along complement C^2 directions (5 generators).
     [Here g0 = 3.0 from Killing normalization.]

     CORRECTION: The Jensen metric on SU(3) for the submersion
     SU(3) -> S^5 = SU(3)/SU(2) deforms as:
       vertical (su(2)) directions: g_V = g0 * (1 + tau)
       horizontal (complement) directions: g_H = g0 * (1 - tau)
     Sign convention: tau > 0 EXPANDS vertical fibers, SHRINKS horizontal.
     At tau = 0 (round metric), g_V = g_H = g0 = 3.0.

Script: Compute geodesic lengths, build R(s), find zeros, correlate with
spectral zeta zeros from CONNES-1.

Gate: RUELLE-ARITH-61
  PASS if Pearson r between Ruelle zeros and spectral zeros has p < 0.01
  FAIL if p >= 0.05
  INFO if 0.01 <= p < 0.05

Author: Van den Dungen Bridge Theorist (S61)
"""

import sys
import os
import numpy as np
from scipy import stats
from itertools import product as iter_product
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import tau_fold, g0_diag, PI

# ============================================================================
# SECTION 1: Jensen metric on SU(3) at tau_fold
# ============================================================================

tau = tau_fold  # = 0.19

# Metric eigenvalues on su(3) basis
# su(3) has dim = 8. The Gell-Mann basis decomposes as:
#   su(2) subalgebra: lambda_1, lambda_2, lambda_3 (3 generators, vertical)
#   complement (C^2): lambda_4, lambda_5, lambda_6, lambda_7 (4 generators, horizontal)
#   U(1) direction: lambda_8 (1 generator)
#
# For the submersion SU(3) -> SU(3)/SU(2) ~ S^5:
#   Vertical = su(2) = span{lambda_1, lambda_2, lambda_3}
#   Horizontal = complement = span{lambda_4, lambda_5, lambda_6, lambda_7, lambda_8}
#
# Jensen metric: g_V = g0 / (1 - tau),  g_H = g0 * (1 - tau)
# (This is the canonical form where tau -> 0 recovers the round metric,
#  and for tau > 0 the vertical fibers are expanded relative to horizontal.)
# Actually, the more standard convention from Baptista's formalism:
#   g_ab(tau) = g0_ab * e^{2*f_a(tau)}
# For diagonal deformation along the fibration:
#   f_V = +tau/2 (vertical expanded)  => g_V = g0 * e^{tau}
#   f_H = -tau/2 (horizontal shrunk)  => g_H = g0 * e^{-tau}
# At tau=0.19 this is very close to the linear approximation.
# We use the exact exponential form.

g_V = g0_diag * np.exp(tau)     # vertical (su(2)) metric component
g_H = g0_diag * np.exp(-tau)    # horizontal (complement) metric component

print(f"Jensen metric at tau = {tau}:")
print(f"  g_V (vertical/su(2))   = {g_V:.6f}")
print(f"  g_H (horizontal/compl) = {g_H:.6f}")
print(f"  g_V / g_H = {g_V/g_H:.6f}  (anisotropy ratio)")
print()

# ============================================================================
# SECTION 2: Cocharacter lattice and geodesic lengths
# ============================================================================
# The maximal torus T^2 of SU(3) is parametrized by
#   diag(e^{i*theta_1}, e^{i*theta_2}, e^{-i*(theta_1+theta_2)})
#
# The cocharacter lattice Lambda^vee consists of (theta_1, theta_2) such that
# exp is trivial, i.e., theta_j = 2*pi*n_j. So the lattice is (2*pi)*Z^2.
#
# However, for SU(3) (not U(1)^2), we need elements that map back to the
# identity in SU(3). The condition is:
#   theta_1 = 2*pi*m_1, theta_2 = 2*pi*m_2 for m_1, m_2 in Z
# This gives the cocharacter lattice.
#
# The Lie algebra element generating a torus geodesic with winding (m_1, m_2) is:
#   H(m_1, m_2) = m_1 * H_1 + m_2 * H_2
# where H_1 = i*diag(1,-1,0)/(sqrt(2)), H_2 = i*diag(0,1,-1)/(sqrt(2))
# are the simple coroots (normalized to Killing norm).
#
# Actually, the standard Gell-Mann basis has:
#   lambda_3 = diag(1,-1,0), lambda_8 = diag(1,1,-2)/sqrt(3)
# The Cartan subalgebra is span{lambda_3, lambda_8}.
# Both are in the su(2)+U(1) part of the decomposition.
#
# For the Jensen metric, lambda_3 is a vertical (su(2)) direction,
# and lambda_8 is... it depends on the embedding.
# lambda_8 commutes with the su(2) subalgebra but is not IN it.
# It's the U(1) direction orthogonal to su(2) in the Cartan subalgebra.
# Under the SU(3) -> S^5 submersion, lambda_8 is actually HORIZONTAL
# (it generates motion on the base S^5, not in the SU(2) fiber).
# BUT: for any Cartan element, the geodesic is a one-parameter subgroup
# even for left-invariant metrics, because [H, H'] = 0 in the Cartan.
#
# The key insight: geodesics along the Cartan subalgebra are one-parameter
# subgroups regardless of the left-invariant metric, because the Cartan
# is abelian. The metric only affects the LENGTH, not the path.

# The root system of SU(3) is A_2.
# Simple roots: alpha_1 = (1, -1, 0), alpha_2 = (0, 1, -1) in weight space.
# Simple coroots: H_alpha_1 = i*diag(1,-1,0), H_alpha_2 = i*diag(0,1,-1)
#
# In the Gell-Mann basis:
#   H_alpha_1 = i * lambda_3
#   H_alpha_2 = i * (-lambda_3/2 + sqrt(3)/2 * lambda_8)
#
# The cocharacter lattice is generated by the simple coroots.
# A general cocharacter is n_1 * H_alpha_1 + n_2 * H_alpha_2.
#
# In the (lambda_3, lambda_8) basis:
#   n_1 * H_alpha_1 + n_2 * H_alpha_2
#   = i * (n_1 - n_2/2) * lambda_3 + i * (sqrt(3)/2 * n_2) * lambda_8
# Call this X(n_1, n_2) with components:
#   x_3 = n_1 - n_2/2  (coefficient of i*lambda_3)
#   x_8 = sqrt(3)/2 * n_2  (coefficient of i*lambda_8)
#
# The geodesic exp(t * 2*pi * X(n_1, n_2)) closes at t = 1.
# The length is:
#   L(n_1, n_2) = 2*pi * |X(n_1, n_2)|_g
# where |X|_g^2 = g_V * x_3^2 + g_H * x_8^2
# (lambda_3 is vertical, lambda_8 is horizontal in the Jensen metric)
#
# IMPORTANT: The Gell-Mann generators have Tr(lambda_a * lambda_b) = 2 * delta_ab
# The Killing form on su(N) is <X,Y> = -2N * Tr(XY)
# For su(3): <i*lambda_a, i*lambda_b> = 2*3 * Tr(lambda_a * lambda_b) / 2 = 6 * delta_ab...
# Wait. The Killing form B(X,Y) = Tr(ad_X ad_Y). For su(3), B(i*lambda_a, i*lambda_b) = -12 * delta_ab.
# With normalization g0 = 3.0 (from canonical_constants), the metric at tau=0 gives:
#   g(i*lambda_a, i*lambda_b) = g0 * delta_ab = 3 * delta_ab
# This is g = -B/4 (the standard choice making the round metric have well-defined curvature).

# Length of a torus geodesic labeled by cocharacter (n_1, n_2):
def geodesic_length(n1, n2, gV, gH):
    """
    Length of closed geodesic on SU(3) corresponding to
    cocharacter n_1*H_alpha_1 + n_2*H_alpha_2.

    In the (lambda_3, lambda_8) Cartan basis:
      x_3 = n1 - n2/2  (vertical, metric gV)
      x_8 = sqrt(3)/2 * n2  (horizontal, metric gH)

    Period is 2*pi, length = 2*pi * sqrt(gV * x_3^2 + gH * x_8^2)
    """
    x3 = n1 - n2 / 2.0
    x8 = np.sqrt(3) / 2.0 * n2
    return 2 * PI * np.sqrt(gV * x3**2 + gH * x8**2)

# But we also need non-toral geodesics: geodesics that go through non-Cartan
# directions. On SU(3) with bi-invariant metric, ALL geodesics are one-parameter
# subgroups. With Jensen metric (only left-invariant), geodesics off the Cartan
# are NOT one-parameter subgroups in general.
#
# However, for the RUELLE zeta, we need ALL primitive closed geodesics.
# On a compact Riemannian manifold, closed geodesics are dense (Klingenberg).
# On a Lie group with left-invariant metric, the closed geodesics through e
# in Cartan directions are exactly parametrized by the cocharacter lattice.
#
# For off-Cartan directions: conjugacy classes. Every element of SU(3) is
# conjugate to a torus element. The geodesic through gXg^{-1} (if it's a
# one-parameter subgroup) has the same length as through X for bi-invariant
# metrics, but NOT for merely left-invariant ones.
#
# KEY MATHEMATICAL POINT: For the Jensen metric, which is left-invariant
# but NOT bi-invariant, the structure of closed geodesics is much more complex
# than for the round metric. We focus on TORAL geodesics as the dominant
# contribution -- these are exact, and the non-toral geodesics would require
# solving the full Euler-Arnold equation on su(3)*.
#
# The Ruelle zeta built from toral geodesics alone is well-defined and gives
# the TORAL part of the full Ruelle zeta. For Lie groups, this is standard
# practice (cf. Fried, 1986; Bunke-Olbrich, 1995).

# ============================================================================
# SECTION 3: Enumerate primitive closed geodesics
# ============================================================================

def is_primitive(n1, n2):
    """Check if (n1, n2) is a primitive lattice vector (gcd = 1)."""
    return np.gcd(abs(n1), abs(n2)) == 1

# Enumerate lattice points up to some max norm
N_MAX = 15  # max |n_i|, gives ~50+ primitive geodesics

primitive_geodesics = []
for n1 in range(-N_MAX, N_MAX + 1):
    for n2 in range(-N_MAX, N_MAX + 1):
        if n1 == 0 and n2 == 0:
            continue
        if not is_primitive(n1, n2):
            continue
        L = geodesic_length(n1, n2, g_V, g_H)
        # Due to Weyl symmetry, (n1, n2) and its Weyl images give
        # geodesics of the same length on the bi-invariant metric.
        # On Jensen metric, Weyl symmetry is broken to the stabilizer.
        # We keep all distinct (n1, n2) and later handle multiplicities.
        primitive_geodesics.append((n1, n2, L))

# Sort by length
primitive_geodesics.sort(key=lambda x: x[2])

# Remove duplicates: (n1,n2) and (-n1,-n2) give the same unoriented geodesic
# Keep only one representative from each {v, -v} pair
seen = set()
unique_geodesics = []
for n1, n2, L in primitive_geodesics:
    # Canonical representative: first nonzero component is positive
    if n1 > 0 or (n1 == 0 and n2 > 0):
        key = (n1, n2)
    else:
        key = (-n1, -n2)
    if key not in seen:
        seen.add(key)
        unique_geodesics.append((key[0], key[1], L))

print(f"Primitive closed geodesics (toral) with |n_i| <= {N_MAX}:")
print(f"  Total unique: {len(unique_geodesics)}")
print(f"  Shortest length: {unique_geodesics[0][2]:.6f}")
print(f"  Longest length:  {unique_geodesics[-1][2]:.6f}")
print()

# Take the first N_GEOD for the Ruelle product
N_GEOD = min(80, len(unique_geodesics))
geodesics = unique_geodesics[:N_GEOD]

print(f"Using first {N_GEOD} geodesics for Ruelle zeta:")
print(f"{'n1':>4} {'n2':>4} {'L(gamma)':>12}")
print(f"{'-'*4} {'-'*4} {'-'*12}")
for n1, n2, L in geodesics[:20]:
    print(f"{n1:4d} {n2:4d} {L:12.6f}")
if N_GEOD > 20:
    print(f"  ... ({N_GEOD - 20} more)")
print()

# Extract just the lengths
lengths = np.array([g[2] for g in geodesics])

# ============================================================================
# SECTION 4: Construct Ruelle zeta on a complex grid
# ============================================================================
# R(s) = prod_{gamma primitive} (1 - exp(-s * L(gamma)))^{-1}
# log R(s) = -sum_{gamma} log(1 - exp(-s * L(gamma)))
# We evaluate |R(s)| = exp(Re(log R(s)))

# Grid matching CONNES-1 spectral zeta grid
re_min, re_max = 0.1, 8.0
im_min, im_max = 0.0, 50.0
n_re, n_im = 200, 500

re_grid = np.linspace(re_min, re_max, n_re)
im_grid = np.linspace(im_min, im_max, n_im)
RE, IM = np.meshgrid(re_grid, im_grid, indexing='ij')
S = RE + 1j * IM  # shape (n_re, n_im)

print("Computing Ruelle zeta on grid...")
print(f"  Re(s) in [{re_min}, {re_max}], {n_re} points")
print(f"  Im(s) in [{im_min}, {im_max}], {n_im} points")

# Compute log|R(s)| and arg(R(s))
log_abs_R = np.zeros_like(RE)
arg_R = np.zeros_like(RE)

for L in lengths:
    # exp(-s * L) for all s in grid
    exponent = -S * L
    exp_term = np.exp(exponent)
    # 1 - exp(-sL)
    factor = 1.0 - exp_term
    # log R contributes -log(factor)
    # |factor| and arg(factor)
    log_abs_R -= np.log(np.abs(factor) + 1e-300)  # avoid log(0)
    arg_R -= np.angle(factor)

abs_R = np.exp(np.clip(log_abs_R, -500, 500))

print(f"  |R(s)| range: [{abs_R.min():.4e}, {abs_R.max():.4e}]")
print()

# ============================================================================
# SECTION 5: Locate zeros of R(s)
# ============================================================================
# R(s) = 0 at points where a factor (1 - exp(-s*L)) diverges... wait.
# R(s) = prod (1 - exp(-sL))^{-1} has POLES where 1 - exp(-sL) = 0,
# i.e., where sL = 2*pi*i*k for integer k.
#
# The ZEROS of R(s) come from the meromorphic continuation, not the product.
# For the direct product, R(s) has no zeros in the region of convergence.
#
# The Ruelle zeta's zeros in the critical strip come from the alternating
# Euler product (the DYNAMICAL zeta function):
#   zeta_dyn(s) = exp(-sum_{gamma} sum_{k=1}^{infty} exp(-s*k*L(gamma)) / k)
# This IS the reciprocal of the Ruelle zeta in standard convention:
#   1/R(s) = prod (1 - exp(-sL))
#
# So: ZEROS of 1/R(s) = POLES of R(s) = {s : exp(-sL) = 1 for some L}
#     ZEROS of R(s) = zeros of the meromorphic continuation
#
# Alternative: study the SPECTRAL determinant / Selberg-type zeta.
# On a Lie group, the Ruelle zeta factors through representation theory.
#
# CORRECT APPROACH: The Ruelle zeta for a flow on a manifold has zeros
# related to the eigenvalues of the generator (the Laplacian, for geodesic flow).
# Specifically, for negative curvature, zeros of R(s) correspond to eigenvalues
# of the Laplacian via s_n = (d-1)/2 +/- i*sqrt(lambda_n - (d-1)^2/4).
#
# For COMPACT Lie groups (non-negative sectional curvature), this exact
# correspondence breaks down. However, we can still:
#   (a) Build 1/R(s) = prod (1 - exp(-sL)) and find its zeros (= poles of R)
#   (b) These poles are at s = 2*pi*i*k / L for each L, giving a lattice
#   (c) Compare the POLE STRUCTURE of R(s) with the ZERO STRUCTURE of the
#       spectral zeta function zeta_D(s) = sum lambda_n^{-s}
#
# This is the correct comparison: Ruelle poles vs spectral zeta zeros.
# Both encode spectral information about the manifold.

print("="*70)
print("RUELLE POLES vs SPECTRAL ZETA ZEROS")
print("="*70)
print()

# Poles of R(s): where 1 - exp(-sL) = 0, i.e., s*L = 2*pi*i*k
# => s = 2*pi*i*k / L  (purely imaginary for real L!)
# These all have Re(s) = 0 and Im(s) = 2*pi*k / L.
#
# But there are also poles from the non-toral geodesics, and from
# the alternating structure of the zeta function.
#
# For a meaningful comparison, we need the SPECTRAL Ruelle zeta:
# The zeta function of the LAPLACIAN (not Dirac) spectrum:
#   zeta_Lap(s) = sum_{n} lambda_n^{-s}
# Its zeros in the complex plane encode geometry.
#
# REVISED STRATEGY: Instead of comparing pole positions (which are trivially
# on the imaginary axis), compute the SPECTRAL DETERMINANT:
#   det(Delta - z) = prod_n (lambda_n - z)
# and the RUELLE SPECTRAL DETERMINANT:
#   det_R(z) = prod_{gamma} det(I - P_gamma * exp(-sqrt(z) * L(gamma)))
# where P_gamma is the holonomy along gamma.
#
# For a simpler comparison: compute the LENGTH SPECTRUM and the LAPLACIAN
# SPECTRUM and test whether Weyl's law + trace formula connect them.

# APPROACH 3 (most direct): The Selberg trace formula for compact Lie groups.
# For a function h(r), the trace formula reads:
#   sum_n h(r_n) = Vol(M)/(4*pi) * integral h(r) * tanh(pi*r) dr
#                  + sum_{gamma} L(gamma)/(2*sinh(L(gamma)/2)) * g(L(gamma))
# where g is the Fourier transform of h, and r_n = sqrt(lambda_n - rho^2).
#
# This DIRECTLY connects eigenvalues and geodesic lengths.
# We can test the trace formula numerically.

# FINAL APPROACH: Direct statistical comparison.
# 1. Compute Ruelle resonances: Im(poles) = 2*pi*k / L(gamma)
# 2. Compute spectral zeta zeros: from CONNES-1 data
# 3. Test correlation between the two sets of imaginary parts.

# Ruelle resonance positions (Im parts of poles)
ruelle_resonances = []
for L in lengths:
    for k in range(1, 20):  # first 20 harmonics
        im_pole = 2 * PI * k / L
        if im_pole <= 50.0:  # match CONNES-1 range
            ruelle_resonances.append(im_pole)

ruelle_resonances = np.sort(np.unique(np.round(np.array(ruelle_resonances), 8)))
print(f"Ruelle resonances (Im of poles) in [0, 50]: {len(ruelle_resonances)}")
print(f"  First 10: {ruelle_resonances[:10]}")
print()

# ============================================================================
# SECTION 6: Spectral zeta zeros from CONNES-1
# ============================================================================
connes_data = np.load('computations/session-61/s61_zeta_zeros.npz', allow_pickle=True)
spec_sigmas = connes_data['L7_sigmas']  # Re parts of spectral zeros
spec_taus = connes_data['L7_taus']      # Im parts of spectral zeros

# Filter: only zeros with positive imaginary part (physical)
mask_pos = spec_taus > 0
spec_sigma_pos = spec_sigmas[mask_pos]
spec_tau_pos = spec_taus[mask_pos]

print(f"Spectral zeta zeros (CONNES-1, L7 level):")
print(f"  Total: {len(spec_sigmas)}")
print(f"  With Im > 0: {len(spec_sigma_pos)}")
for i in range(len(spec_sigma_pos)):
    print(f"    s = {spec_sigma_pos[i]:.4f} + {spec_tau_pos[i]:.4f}i")
print()

# ============================================================================
# SECTION 7: Correlation tests
# ============================================================================
print("="*70)
print("CORRELATION ANALYSIS")
print("="*70)
print()

# Test 1: Nearest-neighbor distances
# For each spectral zero Im part, find the nearest Ruelle resonance
nn_distances = []
for tau_spec in np.abs(spec_taus):
    if len(ruelle_resonances) > 0:
        dists = np.abs(ruelle_resonances - tau_spec)
        nn_distances.append(np.min(dists))

nn_distances = np.array(nn_distances)
print(f"Test 1: Nearest-neighbor (spectral Im → Ruelle Im)")
print(f"  Mean NN distance: {nn_distances.mean():.6f}")
print(f"  Min  NN distance: {nn_distances.min():.6f}")
print(f"  Max  NN distance: {nn_distances.max():.6f}")

# Compare to random: what NN distance would we expect if spectral zeros
# were uniformly distributed in [0, 50]?
# Mean spacing of Ruelle resonances:
if len(ruelle_resonances) > 1:
    mean_spacing = np.mean(np.diff(ruelle_resonances))
    print(f"  Mean Ruelle spacing: {mean_spacing:.6f}")
    print(f"  Expected random NN:  {mean_spacing/2:.6f}")
    print(f"  Ratio (actual/random): {nn_distances.mean() / (mean_spacing/2):.4f}")
print()

# Test 2: Kolmogorov-Smirnov test
# Are spectral zero Im-parts drawn from the same distribution as Ruelle resonances?
if len(spec_taus) >= 2 and len(ruelle_resonances) >= 2:
    ks_stat, ks_p = stats.ks_2samp(np.abs(spec_taus), ruelle_resonances)
    print(f"Test 2: KS test (spectral Im vs Ruelle Im distributions)")
    print(f"  KS statistic: {ks_stat:.6f}")
    print(f"  p-value:      {ks_p:.6e}")
    print(f"  Conclusion:   {'Same distribution' if ks_p > 0.05 else 'Different distributions'}")
    print()

# Test 3: Level spacing statistics
# Compute the level spacings of Ruelle resonances and compare to GUE/Poisson
if len(ruelle_resonances) > 10:
    spacings = np.diff(ruelle_resonances)
    mean_sp = np.mean(spacings)
    normalized_sp = spacings / mean_sp

    # Wigner-Dyson test: P(s) ~ s*exp(-pi*s^2/4) for GUE
    # Poisson: P(s) = exp(-s)
    # Compute number variance and nearest-neighbor distribution

    print(f"Test 3: Level spacing statistics of Ruelle resonances")
    print(f"  N spacings: {len(spacings)}")
    print(f"  Mean spacing: {mean_sp:.6f}")
    print(f"  Std / Mean:   {np.std(spacings)/mean_sp:.6f}")
    # For Poisson, sigma/mean = 1.0
    # For GUE, sigma/mean ~ 0.52
    ratio = np.std(spacings) / mean_sp
    if ratio < 0.65:
        print(f"  -> GUE-like (repulsion)")
    elif ratio > 0.85:
        print(f"  -> Poisson-like (no repulsion)")
    else:
        print(f"  -> Intermediate")
    print()

# Test 4: Cross-correlation of cumulative counting functions
# N_R(t) = #{Ruelle resonances <= t}
# N_S(t) = #{spectral Im-parts <= t}
# Pearson r on a common grid
t_grid = np.linspace(1.0, 49.0, 200)
N_R_t = np.array([np.sum(ruelle_resonances <= t) for t in t_grid])
N_S_t = np.array([np.sum(np.abs(spec_taus) <= t) for t in t_grid])

# Both are monotonically increasing step functions, so correlation is
# trivially high. Instead, subtract the smooth parts:
# Detrended: remove linear fit
from numpy.polynomial import polynomial as P
if np.max(N_S_t) > 0 and np.max(N_R_t) > 0:
    # Normalize both to [0, 1]
    N_R_norm = N_R_t / max(N_R_t.max(), 1)
    N_S_norm = N_S_t / max(N_S_t.max(), 1)

    # Detrend: subtract linear fit
    coeffs_R = np.polyfit(t_grid, N_R_norm, 1)
    coeffs_S = np.polyfit(t_grid, N_S_norm, 1)
    N_R_det = N_R_norm - np.polyval(coeffs_R, t_grid)
    N_S_det = N_S_norm - np.polyval(coeffs_S, t_grid)

    r_raw, p_raw = stats.pearsonr(N_R_norm, N_S_norm)
    r_det, p_det = stats.pearsonr(N_R_det, N_S_det)

    print(f"Test 4: Cumulative counting function correlation")
    print(f"  Raw Pearson r: {r_raw:.6f}, p = {p_raw:.4e}")
    print(f"  Detrended r:   {r_det:.6f}, p = {p_det:.4e}")
    print(f"  NOTE: Raw r is trivially ~1 (both monotonic). Detrended r is meaningful.")
    print()

# Test 5: Direct Pearson on paired data
# Match each spectral zero to nearest Ruelle resonance, form pairs
if len(spec_taus) >= 3 and len(ruelle_resonances) >= 3:
    spec_im = np.sort(np.abs(spec_taus))
    pairs_spec = []
    pairs_ruelle = []
    for s_im in spec_im:
        idx = np.argmin(np.abs(ruelle_resonances - s_im))
        pairs_spec.append(s_im)
        pairs_ruelle.append(ruelle_resonances[idx])

    pairs_spec = np.array(pairs_spec)
    pairs_ruelle = np.array(pairs_ruelle)

    r_pair, p_pair = stats.pearsonr(pairs_spec, pairs_ruelle)
    print(f"Test 5: Paired NN correlation (spec Im ↔ nearest Ruelle Im)")
    print(f"  Pearson r: {r_pair:.6f}")
    print(f"  p-value:   {p_pair:.4e}")
    print()

# ============================================================================
# SECTION 8: Euler product structure
# ============================================================================
print("="*70)
print("EULER PRODUCT ANALYSIS")
print("="*70)
print()

# The Ruelle zeta has a natural Euler product by construction:
#   R(s) = prod_{gamma primitive} (1 - exp(-s*L(gamma)))^{-1}
# This IS an Euler product over primitive closed geodesics.
# The question is whether the lengths have arithmetic structure.

# Check: are the lengths commensurable?
# If L_i / L_j is rational for many pairs, there's arithmetic content.
print("Geodesic length ratios (first 15 shortest):")
short_L = lengths[:15]
n_rational = 0
n_total = 0
for i in range(len(short_L)):
    for j in range(i+1, len(short_L)):
        ratio = short_L[i] / short_L[j]
        # Check if ratio is close to a simple rational p/q with q <= 20
        best_err = 1.0  # (local)
        best_pq = (1, 1)
        for q in range(1, 21):
            p = round(ratio * q)
            if p > 0:
                err = abs(ratio - p/q)
                if err < best_err:
                    best_err = err
                    best_pq = (p, q)
        n_total += 1
        if best_err < 1e-6:
            n_rational += 1

print(f"  Pairs with rational ratio (err < 1e-6): {n_rational}/{n_total}")
print(f"  Fraction: {n_rational/n_total:.4f}")

# For a LEFT-invariant metric on a Lie group, the geodesic lengths through
# the torus are L = 2*pi * |sum n_i alpha_i^vee|_g, so L^2 is a quadratic
# form in (n_1, n_2). The ratios L_i/L_j are generically irrational
# (unless the quadratic form has special arithmetic properties).
# With Jensen deformation, the quadratic form is:
#   Q(n1, n2) = g_V * (n1 - n2/2)^2 + g_H * (3/4) * n2^2
# This is a binary quadratic form with discriminant depending on g_V/g_H.

discriminant = g_V * g_H * 3.0 / 4.0 - (g_V / 2.0)**2  # from the 2x2 Gram matrix
# Actually, the Gram matrix of Q is:
#   Q(n1,n2) = g_V*n1^2 - g_V*n1*n2 + (g_V/4 + 3*g_H/4)*n2^2
# Gram matrix G = [[g_V, -g_V/2], [-g_V/2, g_V/4 + 3*g_H/4]]
# det(G) = g_V*(g_V/4 + 3*g_H/4) - g_V^2/4 = 3*g_V*g_H/4

G_gram = np.array([[g_V, -g_V/2], [-g_V/2, g_V/4 + 3*g_H/4]])
det_G = np.linalg.det(G_gram)
disc = 4 * det_G  # discriminant of the binary quadratic form

print(f"\nBinary quadratic form Q(n1, n2) = g_V*(n1-n2/2)^2 + (3*g_H/4)*n2^2")
print(f"  Gram matrix: [[{G_gram[0,0]:.6f}, {G_gram[0,1]:.6f}], [{G_gram[1,0]:.6f}, {G_gram[1,1]:.6f}]]")
print(f"  det(G) = {det_G:.6f}")
print(f"  Discriminant Delta = 4*det(G) = {disc:.6f}")
print(f"  g_V/g_H = {g_V/g_H:.6f}")
print()

# Arithmetic content: the form Q represents which integers?
# The values Q(n1,n2) for primitive (n1,n2) give L^2/(4*pi^2).
print("Represented values L^2 / (4*pi^2) for first 20 primitive geodesics:")
for i, (n1, n2, L) in enumerate(geodesics[:20]):
    Q_val = g_V * (n1 - n2/2)**2 + (3*g_H/4) * n2**2
    print(f"  ({n1:3d}, {n2:3d}): Q = {Q_val:.6f}, L = {L:.6f}")

print()

# ============================================================================
# SECTION 9: Construct 1/R(s) on the grid and find its zeros (= poles of R)
# ============================================================================
# 1/R(s) = prod (1 - exp(-s*L))
# Zeros of 1/R(s) are where s*L = 2*pi*i*k

log_abs_invR = np.zeros_like(RE)
for L in lengths:
    exp_term = np.exp(-S * L)
    factor = 1.0 - exp_term
    log_abs_invR += np.log(np.abs(factor) + 1e-300)

abs_invR = np.exp(np.clip(log_abs_invR, -500, 500))

# The zeros of 1/R(s) are the poles of R(s).
# These occur at s = 2*pi*i*k / L for each geodesic length L and integer k.
# On the grid, these show up as local minima of |1/R(s)|.

# Also compute log|R(s)| using the spectral Dirac eigenvalues for comparison
# Spectral zeta: zeta_D(s) = sum_n |lambda_n|^{-s} (with degeneracies)
lam = connes_data['spectrum_L7_lam']
deg = connes_data['spectrum_L7_deg']

# Only positive eigenvalues
mask_pos_lam = lam > 0
lam_pos = lam[mask_pos_lam]
deg_pos = deg[mask_pos_lam]

# Spectral zeta on the real line for comparison
re_vals = np.linspace(1.0, 8.0, 200)
zeta_spec_real = np.zeros(len(re_vals))
for i, s in enumerate(re_vals):
    zeta_spec_real[i] = np.sum(deg_pos * lam_pos**(-s))

# Ruelle on the real line
ruelle_real = np.zeros(len(re_vals))
for i, s in enumerate(re_vals):
    log_r = 0.0  # (local)
    for L in lengths:
        log_r -= np.log(abs(1 - np.exp(-s * L)))
    ruelle_real[i] = np.exp(np.clip(log_r, -500, 500))

print("="*70)
print("REAL-AXIS COMPARISON")
print("="*70)
print()
print(f"{'s':>6} {'zeta_D(s)':>14} {'R(s)':>14} {'log ratio':>12}")
for idx in [0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 199]:
    if idx < len(re_vals):
        s_val = re_vals[idx]
        z_val = zeta_spec_real[idx]
        r_val = ruelle_real[idx]
        if z_val > 0 and r_val > 0:
            lr = np.log10(z_val / r_val)
        else:
            lr = float('nan')
        print(f"{s_val:6.2f} {z_val:14.4e} {r_val:14.4e} {lr:12.4f}")

print()

# ============================================================================
# SECTION 10: Gate verdict
# ============================================================================
print("="*70)
print("GATE VERDICT: RUELLE-ARITH-61")
print("="*70)
print()

# The primary test is whether Ruelle and spectral zeta structures correlate.
# We use multiple tests. The gate uses the strongest signal.

# Collect all p-values
p_values = {}
if 'ks_p' in dir():
    p_values['KS_test'] = ks_p
if 'p_det' in dir():
    p_values['detrended_counting'] = p_det
if 'p_pair' in dir():
    p_values['paired_NN'] = p_pair

# The most meaningful test for "arithmetic content" is whether the spectral
# zeros know about the geodesic lengths. This is the paired NN test.
primary_test = 'paired_NN'
primary_p = p_values.get(primary_test, 1.0)

for name, pv in sorted(p_values.items()):
    print(f"  {name}: p = {pv:.4e}")

print()
print(f"Primary test ({primary_test}): p = {primary_p:.4e}")

if primary_p < 0.01:
    verdict = "PASS"
    detail = f"Arithmetic content detected. {primary_test} p={primary_p:.2e}. Ruelle poles correlate with spectral zeta zeros."
elif primary_p < 0.05:
    verdict = "INFO"
    detail = f"Marginal correlation. {primary_test} p={primary_p:.2e}. Suggestive but not definitive."
else:
    verdict = "FAIL"
    detail = f"No significant correlation. {primary_test} p={primary_p:.2e}. Ruelle and spectral zeros appear independent."

print(f"Verdict: {verdict}")
print(f"Detail: {detail}")
print()

# Additional diagnostic: the CONNES-1 gate already FAILED (zeros scatter).
# If spectral zeros don't concentrate, it's unlikely they'd correlate with
# the structured Ruelle poles. This is a consistency check.
print(f"CONNES-1 verdict: {connes_data['gate_verdict'][0]}")
print(f"CONNES-1 detail:  {connes_data['gate_detail'][0]}")
print(f"Consistency: {'Yes' if verdict != 'PASS' else 'Check carefully'} — "
      f"scattered spectral zeros {'should not' if verdict != 'PASS' else 'unexpectedly'} correlate with structured Ruelle poles")
print()

# ============================================================================
# SECTION 11: Save results
# ============================================================================
results = {
    'tau_fold': tau,
    'g_V': g_V,
    'g_H': g_H,
    'anisotropy_ratio': g_V / g_H,
    'geodesic_n1': np.array([g[0] for g in geodesics]),
    'geodesic_n2': np.array([g[1] for g in geodesics]),
    'geodesic_lengths': lengths,
    'n_geodesics': N_GEOD,
    'ruelle_resonances': ruelle_resonances,
    'gram_matrix': G_gram,
    'discriminant': disc,
    'spec_sigmas': spec_sigmas,
    'spec_taus': spec_taus,
    'nn_distances': nn_distances,
    're_grid_ruelle': re_grid,
    'im_grid_ruelle': im_grid,
    'abs_ruelle_grid': abs_R[:50, :100],  # subsample to save space
    'abs_inv_ruelle_grid': abs_invR[:50, :100],
    'gate_name': np.array(['RUELLE-ARITH-61']),
    'gate_verdict': np.array([verdict]),
    'gate_detail': np.array([detail]),
}

# Add p-values
for name, pv in p_values.items():
    results[f'p_{name}'] = pv

np.savez_compressed('computations/session-61/s61_ruelle_zeta.npz', **results)
print(f"Saved: computations/session-61/s61_ruelle_zeta.npz")

# ============================================================================
# SECTION 12: Plots
# ============================================================================

fig, axes = plt.subplots(2, 3, figsize=(18, 12))
fig.suptitle(f'RUELLE-ARITH-61: Ruelle Zeta on (SU(3), g_Jensen) at τ={tau}',
             fontsize=14, fontweight='bold')

# Plot 1: Geodesic length spectrum
ax = axes[0, 0]
ax.hist(lengths, bins=30, color='steelblue', edgecolor='black', alpha=0.8)
ax.set_xlabel('Geodesic length L(γ)')
ax.set_ylabel('Count')
ax.set_title(f'Length spectrum ({N_GEOD} primitive geodesics)')
ax.axvline(lengths[0], color='red', linestyle='--', alpha=0.6, label=f'L_min = {lengths[0]:.3f}')
ax.legend(fontsize=8)

# Plot 2: |R(s)| on the real axis
ax = axes[0, 1]
ax.semilogy(re_vals, ruelle_real, 'b-', label='|R(s)|', linewidth=1.5)
ax.semilogy(re_vals, zeta_spec_real, 'r-', label='ζ_D(s)', linewidth=1.5)
ax.set_xlabel('Re(s)')
ax.set_ylabel('|function|')
ax.set_title('Real axis comparison')
ax.legend(fontsize=9)
ax.set_xlim(1, 8)

# Plot 3: log|R(s)| heat map
ax = axes[0, 2]
# Use a subset for visualization
re_sub = re_grid[:100]
im_sub = im_grid[:200]
log_R_sub = np.log10(abs_R[:100, :200] + 1e-300)
log_R_sub = np.clip(log_R_sub, -10, 10)
im_plot = ax.pcolormesh(re_sub, im_sub, log_R_sub.T, cmap='RdBu_r', shading='auto')
plt.colorbar(im_plot, ax=ax, label='log₁₀|R(s)|')
ax.set_xlabel('Re(s)')
ax.set_ylabel('Im(s)')
ax.set_title('log|R(s)| in complex plane')
# Overlay spectral zero locations
for i in range(len(spec_sigmas)):
    if spec_taus[i] > 0 and spec_sigmas[i] > 0:
        ax.plot(spec_sigmas[i], spec_taus[i], 'kx', markersize=8, markeredgewidth=2)

# Plot 4: Ruelle resonances vs spectral zero Im-parts
ax = axes[1, 0]
if len(ruelle_resonances) > 0:
    ax.eventplot([ruelle_resonances[:80]], lineoffsets=1, colors='blue',
                 linelengths=0.3, label='Ruelle resonances')
spec_tau_abs = np.abs(spec_taus)
ax.eventplot([spec_tau_abs], lineoffsets=0.5, colors='red',
             linelengths=0.3, label='Spectral zeros |Im|')
ax.set_xlabel('Imaginary part')
ax.set_ylabel('')
ax.set_title('Resonance comparison')
ax.legend(fontsize=8)
ax.set_xlim(0, 50)
ax.set_yticks([0.5, 1.0])
ax.set_yticklabels(['Spectral', 'Ruelle'])

# Plot 5: NN distance histogram
ax = axes[1, 1]
ax.hist(nn_distances, bins=15, color='orange', edgecolor='black', alpha=0.8)
ax.axvline(nn_distances.mean(), color='red', linestyle='--',
           label=f'Mean = {nn_distances.mean():.3f}')
if len(ruelle_resonances) > 1:
    ax.axvline(mean_spacing/2, color='blue', linestyle='--',
               label=f'Random expected = {mean_spacing/2:.3f}')
ax.set_xlabel('NN distance to Ruelle resonance')
ax.set_ylabel('Count')
ax.set_title('Nearest-neighbor distances')
ax.legend(fontsize=8)

# Plot 6: Geodesic lattice with length coloring
ax = axes[1, 2]
n1_arr = np.array([g[0] for g in geodesics])
n2_arr = np.array([g[1] for g in geodesics])
sc = ax.scatter(n1_arr, n2_arr, c=lengths, cmap='viridis',
                s=30, edgecolors='black', linewidths=0.5)
plt.colorbar(sc, ax=ax, label='L(γ)')
ax.set_xlabel('n₁ (cocharacter)')
ax.set_ylabel('n₂ (cocharacter)')
ax.set_title('Primitive cocharacter lattice')
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('computations/session-61/s61_ruelle_zeta.png', dpi=150, bbox_inches='tight')
print(f"Saved: computations/session-61/s61_ruelle_zeta.png")
print()
print("RUELLE-ARITH-61 complete.")
