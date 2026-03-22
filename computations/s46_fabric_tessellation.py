#!/usr/bin/env python3
"""
FABRIC-TESSELLATION-46: Domain wall modulation of pair creation spectrum
========================================================================

Gate: FABRIC-TESSELLATION-46 (diagnostic)
  Report alpha_tess from M(k) ~ k^{alpha_tess}

Physics:
  The 32-cell Voronoi tessellation from Kibble-Zurek domain formation (S42)
  imposes a geometric filter on the pair creation spectrum during transit.
  Each domain wall is an impedance mismatch (COHERENT-WALL-44: DR > 431 dec).
  A mode of wavenumber k propagating through the fabric intercepts domain
  walls at a rate proportional to k in 1D -- this is the fundamental result
  of geometric optics in a random medium.

  The modulation function M(k) = N_wall(k) / N_wall(k_max) counts the
  number of domain walls intercepted by a mode of wavenumber k, normalized
  to the maximum wavenumber. If M(k) ~ k^{alpha_tess} with alpha_tess ~ 1,
  the tessellation provides a geometric hose count alpha = 1 independent
  of BCS pair counting.

  This is the ACOUSTIC analog of X-ray scattering from a polycrystal:
  the number of Bragg planes intercepted by a beam grows linearly with
  the scattering vector |Q| = 2k sin(theta/2), giving the standard
  powder diffraction linear-in-k envelope.

Formula:
  N_wall(k) = k * L_total / pi   [1D, periodic boundary conditions]
  M(k) = N_wall(k) / N_wall(k_max) = k / k_max
  Transmission through N_wall walls: T(k) ~ T_single^{N_wall(k)}
  ln T(k) = N_wall(k) * ln(T_single) ~ k (linear in k)

  For Anderson localization (COHERENT-WALL-44):
  ln T(k) = -L / xi_loc(k) where xi_loc(k) is k-dependent

  [N_wall] = dimensionless. [k] = M_KK. [L] = M_KK^{-1}. Consistent.

Limiting cases:
  k -> 0: N_wall -> 0, T -> 1 (no wall crossings, perfect transmission)
  k -> inf: N_wall -> inf, T -> 0 (infinite wall crossings, total reflection)
  N_domains = 1: M(k) = 1 for all k (single domain, no modulation)
  alpha_tess = 1: linear regime (geometric optics valid)
  alpha_tess > 1: superlinear (coherent Bragg enhancement)
  alpha_tess < 1: sublinear (Anderson localization quenches high-k modes)

Citation:
  - COHERENT-WALL-44 (s44_coherent_wall.py): transfer matrix through 32 walls
  - VORONOI-FNL-44 (s44_voronoi_fnl.py): 32-cell tessellation on S^2
  - KZ domain formation: S42 s42_fabric_wz.py
  - Anderson localization in 1D: Phys Rev 109, 1492 (1958)

Author: Tesla-Resonance (Session 46, Wave 4-6)
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from time import time

from canonical_constants import (
    N_cells, xi_BCS, tau_fold, E_B1, E_B2_mean, E_B3_mean,
    M_KK_gravity as M_KK, PI
)

t_start = time()

print("=" * 70)
print("FABRIC-TESSELLATION-46: Domain Wall Modulation of Pair Creation")
print("=" * 70)

# ============================================================
# 1. LOAD INPUT DATA
# ============================================================

wall_data = np.load('tier0-computation/s44_coherent_wall.npz', allow_pickle=True)
vor_data  = np.load('tier0-computation/s44_voronoi_fnl.npz', allow_pickle=True)

# Coherent wall parameters
N_domains    = int(wall_data['N_domains'].item())
xi_KZ        = float(wall_data['xi_KZ'].item())
L_total      = float(wall_data['L_total_mean'].item())  # 32 * 0.152 = 4.864 M_KK^{-1}
gap_edge     = float(wall_data['gap_edge'].item())       # 0.8191 M_KK
omega_grid_w = wall_data['omega_grid']                   # (2000,) from 0.05 to 3.0

# Transmission spectra (disordered, typical = geometric mean)
lnT_B2 = wall_data['disordered_lnT_mean_B2']
lnT_B1 = wall_data['disordered_lnT_mean_B1']
lnT_B3 = wall_data['disordered_lnT_mean_B3']

# Localization lengths
xi_loc_B2 = float(wall_data['xi_loc_median_B2'].item())
xi_loc_B1 = float(wall_data['xi_loc_median_B1'].item())
xi_loc_B3 = float(wall_data['xi_loc_median_B3'].item())

# Lyapunov spectra
lyap_B2 = wall_data['lyap_B2']
lyap_B1 = wall_data['lyap_B1']
lyap_B3 = wall_data['lyap_B3']

# Length scaling data (for Anderson verification)
length_N = wall_data['length_scaling_N']          # [4, 8, 16, 32, 64, 128]
length_lnT_B2 = wall_data['length_scaling_B2_lnT']
length_lnT_B1 = wall_data['length_scaling_B1_lnT']
length_lnT_B3 = wall_data['length_scaling_B3_lnT']

# Voronoi tessellation parameters
sigma_boundary = float(vor_data['sigma_boundary'])  # 0.063 rad
l_voronoi      = int(vor_data['l_voronoi'])          # characteristic multipole ~ 20
Cl_mean        = vor_data['Cl_mean']                 # (41,)

print(f"\nInput parameters:")
print(f"  N_domains     = {N_domains}")
print(f"  xi_KZ         = {xi_KZ:.3f} M_KK^{{-1}}")
print(f"  L_total       = {L_total:.3f} M_KK^{{-1}}")
print(f"  gap_edge      = {gap_edge:.4f} M_KK")
print(f"  xi_loc_B2     = {xi_loc_B2:.3f} M_KK^{{-1}}")
print(f"  xi_loc_B1     = {xi_loc_B1:.3f} M_KK^{{-1}}")
print(f"  xi_loc_B3     = {xi_loc_B3:.3f} M_KK^{{-1}}")
print(f"  sigma_boundary = {sigma_boundary:.4f} rad")
print(f"  l_voronoi     = {l_voronoi}")

# ============================================================
# 2. WAVENUMBER GRID AND WALL-CROSSING FUNCTION
# ============================================================
#
# In 1D, a plane wave with wavenumber k propagating through a random
# medium of mean domain size <d> = xi_KZ crosses domain walls at rate:
#
#   N_wall(k, L) = L / <d> = N_domains    (independent of k!)
#
# But this is the number of PHYSICAL walls in the path. The k-dependence
# enters through the PHASE accumulated per domain:
#
#   phi(k) = k * <d> = k * xi_KZ
#
# When phi >> 1, the mode resolves individual domains and scatters
# coherently from each wall. When phi << 1, the mode sees a smooth
# average and passes through.
#
# The EFFECTIVE number of scattering events is:
#
#   N_eff(k) = N_domains * (1 - sinc(k * xi_KZ))
#
# This interpolates between:
#   k -> 0: N_eff -> 0 (long wavelength, no scattering)
#   k >> 1/xi_KZ: N_eff -> N_domains (short wavelength, full scattering)
#
# For the modulation function:
#   M(k) = N_eff(k) / N_eff(k_max) = (1 - sinc(k*xi_KZ)) / (1 - sinc(k_max*xi_KZ))
#
# The transition occurs at k_c = pi / xi_KZ (first zero of sinc).
# Below k_c: M(k) ~ (k*xi_KZ)^2 / 6  (quadratic, Rayleigh regime)
# Above k_c: M(k) ~ 1 - const/k       (saturation)
#
# For PAIR CREATION, the relevant k is the internal SU(3) wavenumber,
# not a 4D spatial wavenumber. The BdG quasiparticle dispersion
# maps omega -> k_BdG, and k_BdG ~ omega for omega >> Delta.

print("\n" + "=" * 70)
print("2. WALL-CROSSING MODULATION FUNCTION")
print("=" * 70)

# Wavenumber grid (M_KK units)
k_grid = np.linspace(0.01, 20.0, 2000)
k_max = k_grid[-1]

# Critical wavenumber
k_c = PI / xi_KZ  # = pi / 0.152 ~ 20.66 M_KK

print(f"\n  k_c = pi / xi_KZ = {k_c:.3f} M_KK  (Rayleigh-to-geometric transition)")
print(f"  k_max = {k_max:.1f} M_KK")
print(f"  k_c * xi_KZ = {k_c * xi_KZ:.4f}  (should be pi)")

# sinc function: sin(x)/x
def sinc(x):
    """sinc(x) = sin(x)/x, sinc(0) = 1"""
    out = np.ones_like(x, dtype=float)
    mask = np.abs(x) > 1e-15
    out[mask] = np.sin(x[mask]) / x[mask]
    return out

# N_eff(k): effective scattering events
phi_grid = k_grid * xi_KZ  # phase per domain
N_eff = N_domains * (1.0 - sinc(phi_grid))

# Modulation function
N_eff_max = N_domains * (1.0 - sinc(k_max * xi_KZ))
M_k = N_eff / N_eff_max

print(f"  N_eff(k_max) = {N_eff_max:.4f}")
print(f"  N_eff(k_c)   = {N_domains * (1.0 - sinc(np.array([k_c * xi_KZ]))[0]):.4f}")

# ============================================================
# 3. EXTRACT alpha_tess FROM POWER-LAW FIT
# ============================================================
#
# Fit M(k) ~ k^{alpha_tess} in the physically relevant regime.
#
# The BdG quasiparticle spectrum spans omega in [Delta, ~3] M_KK,
# which maps to k_BdG in [0, ~2] M_KK. This is BELOW k_c ~ 20.66,
# so we are in the Rayleigh regime where N_eff ~ k^2.
#
# Two fits:
# (a) Full k range [0.1, 20]: expect alpha < 2 (transition from k^2 to saturation)
# (b) Physical BdG range [0.1, 3]: expect alpha ~ 2 (Rayleigh)
# (c) From the COHERENT-WALL transmission directly: alpha from d(lnT)/d(ln k)

print("\n" + "=" * 70)
print("3. ALPHA_TESS EXTRACTION")
print("=" * 70)

# (a) Full range fit
mask_full = (k_grid > 0.1) & (k_grid < 15.0)
log_k_full = np.log(k_grid[mask_full])
log_M_full = np.log(M_k[mask_full])
# Remove any -inf or nan
valid_full = np.isfinite(log_M_full) & np.isfinite(log_k_full)
coeffs_full = np.polyfit(log_k_full[valid_full], log_M_full[valid_full], 1)
alpha_full = coeffs_full[0]
residual_full = np.sum((log_M_full[valid_full] -
                        np.polyval(coeffs_full, log_k_full[valid_full]))**2)

# (b) Physical BdG range
mask_bdg = (k_grid > 0.1) & (k_grid < 3.0)
log_k_bdg = np.log(k_grid[mask_bdg])
log_M_bdg = np.log(M_k[mask_bdg])
valid_bdg = np.isfinite(log_M_bdg) & np.isfinite(log_k_bdg)
coeffs_bdg = np.polyfit(log_k_bdg[valid_bdg], log_M_bdg[valid_bdg], 1)
alpha_bdg = coeffs_bdg[0]
residual_bdg = np.sum((log_M_bdg[valid_bdg] -
                       np.polyval(coeffs_bdg, log_k_bdg[valid_bdg]))**2)

print(f"\n  (a) Full range [0.1, 15.0] M_KK:")
print(f"      alpha_tess = {alpha_full:.4f}")
print(f"      residual   = {residual_full:.6f}")

print(f"\n  (b) Physical BdG range [0.1, 3.0] M_KK:")
print(f"      alpha_tess = {alpha_bdg:.4f}")
print(f"      residual   = {residual_bdg:.6f}")

# Analytic prediction: in Rayleigh regime, N_eff ~ (k*xi_KZ)^2 / 3
# => M(k) ~ k^2 / k_max^2 (not k^1)
# Check:
alpha_rayleigh = 2.0
print(f"\n  Analytic prediction (Rayleigh, k*xi_KZ << 1):")
print(f"      N_eff(k) ~ N_domains * (k*xi_KZ)^2 / 3")
print(f"      => alpha_tess = 2.0")
print(f"      Actual alpha in BdG range: {alpha_bdg:.4f}")
print(f"      Deviation from Rayleigh: {abs(alpha_bdg - 2.0):.4f}")

# ============================================================
# 4. TRANSMISSION-BASED MODULATION
# ============================================================
#
# The COHERENT-WALL-44 data gives ln T(omega) directly.
# The modulation of pair creation by the tessellation is
# proportional to T(omega), since modes must PROPAGATE through
# the domain walls to participate in pair creation across domains.
#
# The pair creation probability is P_pair(k) ~ |Bogoliubov coeff|^2 * T(k)
# where T(k) is the wall transmission. The k-dependence of T provides
# the modulation M_T(k).

print("\n" + "=" * 70)
print("4. TRANSMISSION-BASED MODULATION")
print("=" * 70)

# Convert omega to k_BdG for each branch
# For B2: E(k) = sqrt((sqrt(k^2 + eps^2) - eps)^2 + Delta^2)
# At high k: E ~ k, so k_BdG ~ omega
# Near gap edge: k_BdG ~ sqrt(omega^2 - Delta^2) (acoustic-like)

# Use the transmission data directly: the k-dependence is already encoded
# in the omega -> k map through the BdG dispersion.

# For the modulation analysis, what matters is:
# How does ln T scale with omega in the propagating regime?

branches = {
    'B2': {'lnT': lnT_B2, 'xi_loc': xi_loc_B2, 'lyap': lyap_B2,
           'label': 'B2 (quartet)', 'color': '#2166ac'},
    'B1': {'lnT': lnT_B1, 'xi_loc': xi_loc_B1, 'lyap': lyap_B1,
           'label': 'B1 (singlet)', 'color': '#b2182b'},
    'B3': {'lnT': lnT_B3, 'xi_loc': xi_loc_B3, 'lyap': lyap_B3,
           'label': 'B3 (triplet)', 'color': '#1b7837'},
}

# BCS gaps from canonical (approximate)
Delta_approx = {'B2': 2.062, 'B1': 0.789, 'B3': 0.176}

alpha_from_transmission = {}

for bname, bp in branches.items():
    lnT = bp['lnT']
    Delta = Delta_approx[bname]

    # Select propagating regime: omega > Delta and lnT > -500
    prop_mask = (omega_grid_w > Delta + 0.1) & (lnT > -500) & (lnT < -0.001)
    n_prop = np.sum(prop_mask)

    if n_prop < 10:
        print(f"\n  {bname}: insufficient propagating data ({n_prop} points)")
        alpha_from_transmission[bname] = np.nan
        continue

    omega_prop = omega_grid_w[prop_mask]
    lnT_prop = lnT[prop_mask]

    # Fit: ln(-lnT) = alpha * ln(omega) + const
    # This tests whether -ln T ~ omega^alpha
    neg_lnT = -lnT_prop
    valid_t = neg_lnT > 1e-15
    if np.sum(valid_t) < 10:
        print(f"\n  {bname}: insufficient valid -lnT data ({np.sum(valid_t)} points)")
        alpha_from_transmission[bname] = np.nan
        continue

    log_omega = np.log(omega_prop[valid_t])
    log_neg_lnT = np.log(neg_lnT[valid_t])

    coeffs_t = np.polyfit(log_omega, log_neg_lnT, 1)
    alpha_t = coeffs_t[0]
    alpha_from_transmission[bname] = alpha_t

    # R^2 for the fit
    ss_res = np.sum((log_neg_lnT - np.polyval(coeffs_t, log_omega))**2)
    ss_tot = np.sum((log_neg_lnT - np.mean(log_neg_lnT))**2)
    r2 = 1.0 - ss_res / (ss_tot + 1e-30)

    print(f"\n  {bname}:")
    print(f"    Propagating range: omega in [{omega_prop[0]:.3f}, {omega_prop[-1]:.3f}] M_KK")
    print(f"    N_valid = {np.sum(valid_t)}")
    print(f"    alpha_T = {alpha_t:.4f} (from -ln T ~ omega^alpha)")
    print(f"    R^2     = {r2:.6f}")
    print(f"    -lnT range: [{neg_lnT[valid_t].min():.4e}, {neg_lnT[valid_t].max():.4e}]")

# ============================================================
# 5. DIRECT WALL-CROSSING COUNT (Monte Carlo)
# ============================================================
#
# Generate random 1D Voronoi tessellations (exponential domain sizes)
# and directly count how many domain walls a mode of wavenumber k
# crosses in one wavelength lambda = 2*pi/k.
#
# N_cross(k) = number of domain walls in interval [0, lambda]
# M_MC(k) = <N_cross(k)> / <N_cross(k_max)>

print("\n" + "=" * 70)
print("5. DIRECT MONTE CARLO WALL-CROSSING COUNT")
print("=" * 70)

N_mc = 10000
rng = np.random.default_rng(seed=46)

k_mc = np.linspace(0.1, 20.0, 200)
N_cross_mean = np.zeros(len(k_mc))
N_cross_std  = np.zeros(len(k_mc))

for ik, k_val in enumerate(k_mc):
    lam = 2.0 * PI / k_val  # wavelength
    counts = np.zeros(N_mc)

    for imc in range(N_mc):
        # Generate random 1D domain walls (exponential spacing)
        # Place enough walls to cover at least lambda
        n_walls_gen = max(int(5 * lam / xi_KZ), 200)
        spacings = rng.exponential(scale=xi_KZ, size=n_walls_gen)
        wall_positions = np.cumsum(spacings)

        # Count walls in [0, lambda]
        counts[imc] = np.sum(wall_positions <= lam)

    N_cross_mean[ik] = np.mean(counts)
    N_cross_std[ik]  = np.std(counts)

# Normalize to M_MC
M_mc = N_cross_mean / N_cross_mean[-1]
M_mc_err = N_cross_std / N_cross_mean[-1]

# Fit alpha_MC
mask_mc = (k_mc > 0.3) & (M_mc > 1e-5)
log_k_mc = np.log(k_mc[mask_mc])
log_M_mc = np.log(M_mc[mask_mc])
valid_mc = np.isfinite(log_M_mc)
coeffs_mc = np.polyfit(log_k_mc[valid_mc], log_M_mc[valid_mc], 1)
alpha_mc = coeffs_mc[0]

# R^2
ss_res_mc = np.sum((log_M_mc[valid_mc] - np.polyval(coeffs_mc, log_k_mc[valid_mc]))**2)
ss_tot_mc = np.sum((log_M_mc[valid_mc] - np.mean(log_M_mc[valid_mc]))**2)
r2_mc = 1.0 - ss_res_mc / (ss_tot_mc + 1e-30)

print(f"\n  Monte Carlo wall crossings ({N_mc} realizations per k):")
print(f"    alpha_MC   = {alpha_mc:.4f}")
print(f"    R^2        = {r2_mc:.6f}")
print(f"    N_cross at k=0.1: {N_cross_mean[0]:.2f} +/- {N_cross_std[0]:.2f}")
print(f"    N_cross at k=20:  {N_cross_mean[-1]:.2f} +/- {N_cross_std[-1]:.2f}")

# Analytic prediction: for Poisson-distributed walls with density 1/xi_KZ,
# the expected number of walls in [0, lambda] is:
# <N> = lambda / xi_KZ = 2*pi*k / (k * xi_KZ) ... wait, lambda = 2*pi/k
# <N> = (2*pi/k) / xi_KZ ... this DECREASES with k!
#
# NO -- the question is about wavelength, not total path.
# The prompt says "wall crossings at wavenumber k grow as ~k in 1D."
# This must mean: for a mode of wavenumber k propagating through
# the FULL system of length L_total, the number of scattering events
# that are phase-coherent (i.e., where the phase advance per domain
# is O(1)) grows with k.
#
# Actually, the total number of physical walls is fixed at N_domains.
# But the EFFECTIVE scattering per wall depends on the phase mismatch
# between neighboring domains: Delta_phi = k * xi_KZ.
# The scattering strength per wall ~ sin^2(k * xi_KZ / 2).
# Total effective scattering: N_domains * sin^2(k * xi_KZ / 2).
#
# For small k*xi_KZ: N_eff ~ N_domains * (k*xi_KZ)^2 / 4 ~ k^2
# For large k*xi_KZ: N_eff ~ N_domains / 2 (saturated)
#
# The wall-crossing count in [0, lambda] is physically N = lambda/xi_KZ:
#   N = 2*pi / (k * xi_KZ) ~ 1/k (DECREASING with k)
# This is correct: shorter wavelength fits more periods between walls,
# not more walls per wavelength.
#
# Re-reading the prompt carefully:
# "The number of domain walls intercepted by a mode of wavenumber k
#  grows as ~k in the transit direction (1D)."
#
# This must refer to the number of walls crossed in the INTERNAL SU(3)
# direction during transit. If the transit covers a path length L_transit
# proportional to k (higher modes traverse more internal distance), then
# N_wall ~ k * L_transit / xi_KZ ~ k.
#
# More precisely: in the Peter-Weyl decomposition, a mode (p,q) has
# internal wavenumber k_int ~ sqrt(C_2(p,q)) where C_2 is the quadratic
# Casimir. Higher (p,q) modes extend further into SU(3), crossing more
# domain walls. The path length through SU(3) for mode (p,q) is
# proportional to sqrt(C_2) ~ k_int.

# Recompute: N_wall(k) = k * L_total / pi for the transit-direction
# interpretation (higher k = longer internal path)
N_wall_linear = k_mc * L_total / PI
M_linear = N_wall_linear / N_wall_linear[-1]

print(f"\n  Linear model: N_wall(k) = k * L_total / pi")
print(f"    N_wall(k=1)  = {1.0 * L_total / PI:.3f}")
print(f"    N_wall(k=10) = {10.0 * L_total / PI:.3f}")

# ============================================================
# 6. COMBINED MODULATION: GEOMETRIC + TRANSMISSION
# ============================================================
#
# The full modulation combines:
# (1) Geometric wall crossings: M_geom(k) = N_eff(k) / N_eff(k_max)
#     captures whether the mode resolves the domain structure
# (2) Transmission filtration: T(k) from COHERENT-WALL-44
#     captures how much amplitude survives the wall crossings
#
# The pair creation modulation is:
#   P_pair(k) ~ M_geom(k) * T(k)
#
# where M_geom captures the coupling strength to the domain structure
# (needed to create pairs at domain walls) and T captures the propagation
# loss.

print("\n" + "=" * 70)
print("6. COMBINED MODULATION ANALYSIS")
print("=" * 70)

# Interpolate transmission onto k_grid using omega ~ k for above-gap modes
# For simplicity, use omega = k (valid at high k) with branch B3 as the
# lightest (most modes above gap)
from scipy.interpolate import interp1d

combined_alpha = {}

for bname in ['B2', 'B1', 'B3']:
    lnT = branches[bname]['lnT']
    Delta = Delta_approx[bname]

    # Map omega -> effective k (omega ~ k at high energy)
    omega_as_k = omega_grid_w.copy()

    # Restrict to propagating regime
    prop = (omega_as_k > Delta) & (lnT > -500)
    if np.sum(prop) < 10:
        combined_alpha[bname] = np.nan
        continue

    # Interpolate lnT onto k_grid
    f_interp = interp1d(omega_as_k[prop], lnT[prop],
                        bounds_error=False, fill_value=-1000)
    lnT_on_k = f_interp(k_grid)

    # Geometric modulation (from Section 2)
    # M_geom already computed: M_k on k_grid

    # Combined: pair creation probability modulated by both
    # P(k) ~ M_geom(k) * T(k)
    # ln P(k) = ln M_geom(k) + ln T(k)
    valid_combined = (lnT_on_k > -500) & (M_k > 1e-15)
    if np.sum(valid_combined) < 10:
        combined_alpha[bname] = np.nan
        continue

    ln_P = np.log(M_k[valid_combined]) + lnT_on_k[valid_combined]

    # Fit alpha_combined
    log_k_c = np.log(k_grid[valid_combined])
    valid_c = np.isfinite(ln_P)
    if np.sum(valid_c) < 5:
        combined_alpha[bname] = np.nan
        continue

    coeffs_c = np.polyfit(log_k_c[valid_c], ln_P[valid_c], 1)
    combined_alpha[bname] = coeffs_c[0]

    print(f"  {bname}: alpha_combined = {coeffs_c[0]:.4f}")

# ============================================================
# 7. PHYSICAL INTERPRETATION: CHLADNI-VORONOI ANALOGY
# ============================================================

print("\n" + "=" * 70)
print("7. PHYSICAL INTERPRETATION")
print("=" * 70)

# The key insight (Tesla resonance perspective):
# The Voronoi tessellation is a 3D analog of a Chladni plate.
# Domain walls = nodal lines of the order parameter.
# Higher harmonics (larger k) intersect more nodal lines.
# The scaling is NOT k^1 (linear) but k^2 (Rayleigh) because
# the scattering cross-section per wall scales as k^2/k_c^2
# in the long-wavelength limit.
#
# This is exactly the phononic crystal Rayleigh regime:
# for k << k_c = pi/d (where d = lattice spacing = xi_KZ),
# scattering is ~ (k*d)^2 (Rayleigh scattering).
#
# The prompt's claim "~k in 1D" is the geometric optics limit
# (k >> k_c), but the physical BdG modes have k << k_c ~ 20.66,
# so we are in the Rayleigh regime with alpha ~ 2.

print(f"\n  KEY RESULT: The physically relevant regime is RAYLEIGH, not geometric optics.")
print(f"  The BdG quasiparticle spectrum has k < 3 M_KK.")
print(f"  The domain wall spacing gives k_c = pi / xi_KZ = {k_c:.2f} M_KK.")
print(f"  Since k_BdG << k_c, we are in the Rayleigh regime: M(k) ~ k^2.")
print(f"")
print(f"  alpha_tess values:")
print(f"    Analytic M(k) function, full range:     {alpha_full:.4f}")
print(f"    Analytic M(k) function, BdG range:      {alpha_bdg:.4f}")
print(f"    Monte Carlo wall crossings:             {alpha_mc:.4f}")
print(f"    Rayleigh prediction:                    2.0000")
print(f"")
print(f"  The geometric optics claim alpha=1 requires k >> {k_c:.1f} M_KK,")
print(f"  which is 7x above the BdG spectrum cutoff.")
print(f"")
print(f"  Condensed matter analog: phononic crystal in Rayleigh limit.")
print(f"  Just as acoustic phonons scatter as omega^4 from defects smaller")
print(f"  than lambda (Rayleigh scattering), BdG quasiparticles scatter as")
print(f"  k^2 from domain walls thinner than 1/k.")

# Cross-domain connection: Tesla coil quarter-wave resonator
# The domain walls are impedance mismatches, exactly like the
# discontinuities in a Tesla coil's helical winding. The
# transmission through N impedance steps in the sub-wavelength
# regime goes as T ~ 1 - N*(Z_mismatch/Z_0)^2 * (k*d)^2,
# which is the same k^2 Rayleigh scaling.

print(f"\n  Tesla coil analogy:")
print(f"    Domain walls = impedance mismatches in helical winding")
print(f"    Sub-wavelength regime: T ~ 1 - N*(Z_mis/Z_0)^2*(k*d)^2")
print(f"    Same k^2 Rayleigh scaling as Voronoi domain structure")

# ============================================================
# 8. DIAGNOSTIC REPORT: ALPHA_TESS VERDICT
# ============================================================

# The canonical alpha_tess for the FABRIC-TESSELLATION-46 gate
alpha_tess = alpha_bdg  # physical regime

print("\n" + "=" * 70)
print("GATE VERDICT: FABRIC-TESSELLATION-46 (Diagnostic)")
print("=" * 70)
print(f"\n  alpha_tess = {alpha_tess:.4f}")
print(f"  Regime: Rayleigh (k_BdG << k_c = pi/xi_KZ)")
print(f"")
print(f"  This is NOT alpha = 1 (geometric optics, as hypothesized in prompt).")
print(f"  The domain walls are 7x smaller than the BdG wavelengths.")
print(f"  Result: alpha_tess = {alpha_tess:.3f}, consistent with Rayleigh k^2 law.")
print(f"")
print(f"  Implication for HOSE-COUNT-46:")
print(f"    If the hose count enters through the tessellation modulation,")
print(f"    the effective alpha_eff = alpha_tess = {alpha_tess:.3f}, not 1.0.")
print(f"    This provides a STEEPER tilt than the geometric optics estimate,")
print(f"    which would give MORE red tilt (more suppression at high k).")
print(f"")
print(f"  But: the pair creation rate is NOT simply proportional to M(k).")
print(f"  The Landau-Zener probability P_k = 1 - exp(-2*pi*Q_k) depends on")
print(f"  the gap structure, not the wall crossings. The tessellation modulates")
print(f"  the SPATIAL coherence of pair creation, not the pair creation rate.")
print(f"  The relevant observable is the power spectrum of the pair density,")
print(f"  which acquires the Voronoi geometric correlation (l_voronoi ~ {l_voronoi}).")

# ============================================================
# 9. SAVE DATA
# ============================================================

t_elapsed = time() - t_start

save_dict = {
    # Gate result
    'gate_name': 'FABRIC-TESSELLATION-46',
    'alpha_tess': alpha_tess,
    'alpha_full_range': alpha_full,
    'alpha_bdg_range': alpha_bdg,
    'alpha_mc': alpha_mc,
    'alpha_rayleigh_prediction': 2.0,

    # Modulation function
    'k_grid': k_grid,
    'M_k': M_k,
    'N_eff': N_eff,

    # Monte Carlo
    'k_mc': k_mc,
    'M_mc': M_mc,
    'M_mc_err': M_mc_err,
    'N_cross_mean': N_cross_mean,
    'N_cross_std': N_cross_std,

    # Transmission-based alpha (per branch)
    'alpha_T_B2': alpha_from_transmission.get('B2', np.nan),
    'alpha_T_B1': alpha_from_transmission.get('B1', np.nan),
    'alpha_T_B3': alpha_from_transmission.get('B3', np.nan),

    # Combined alpha (per branch)
    'alpha_combined_B2': combined_alpha.get('B2', np.nan),
    'alpha_combined_B1': combined_alpha.get('B1', np.nan),
    'alpha_combined_B3': combined_alpha.get('B3', np.nan),

    # Physical parameters
    'k_c': k_c,
    'xi_KZ': xi_KZ,
    'L_total': L_total,
    'N_domains': N_domains,
    'k_max': k_max,
    'gap_edge': gap_edge,
    'l_voronoi': l_voronoi,

    # Fit quality
    'R2_mc': r2_mc,

    # Runtime
    'elapsed_s': t_elapsed,
}

np.savez('tier0-computation/s46_fabric_tessellation.npz', **save_dict)
print(f"\n  Data saved to tier0-computation/s46_fabric_tessellation.npz")

# ============================================================
# 10. PLOT
# ============================================================

fig, axes = plt.subplots(2, 3, figsize=(18, 11))
fig.suptitle('FABRIC-TESSELLATION-46: Domain Wall Modulation of Pair Creation\n'
             f'32-cell Voronoi, $\\xi_{{KZ}}$ = {xi_KZ:.3f} M$_{{KK}}^{{-1}}$, '
             f'$k_c$ = $\\pi/\\xi_{{KZ}}$ = {k_c:.1f} M$_{{KK}}$',
             fontsize=13, fontweight='bold')

# (a) Modulation function M(k) with power-law fits
ax = axes[0, 0]
ax.loglog(k_grid, M_k, 'b-', linewidth=1.5, label='$M(k) = N_{\\rm eff}(k)/N_{\\rm eff}(k_{\\rm max})$')
ax.loglog(k_mc, M_mc, 'ro', markersize=2, alpha=0.5, label='Monte Carlo')
# Power law fits
k_fit = np.logspace(np.log10(0.1), np.log10(15), 100)
ax.loglog(k_fit, np.exp(np.polyval(coeffs_bdg, np.log(k_fit))),
          'g--', linewidth=1.5, label=f'$k^{{{alpha_bdg:.2f}}}$ (BdG range)')
ax.loglog(k_fit, np.exp(np.polyval(coeffs_full, np.log(k_fit))),
          'k:', linewidth=1.2, label=f'$k^{{{alpha_full:.2f}}}$ (full range)')
ax.axvline(k_c, color='red', linestyle='--', alpha=0.5, label=f'$k_c = \\pi/\\xi_{{KZ}}$')
ax.axvspan(0.1, 3.0, alpha=0.08, color='orange', label='BdG window')
ax.set_xlabel('$k$ [M$_{\\rm KK}$]', fontsize=11)
ax.set_ylabel('$M(k)$', fontsize=11)
ax.set_title(f'(a) Modulation Function | $\\alpha_{{\\rm tess}}$ = {alpha_bdg:.3f}', fontsize=11)
ax.legend(fontsize=8, loc='lower right')
ax.set_xlim(0.08, 25)

# (b) Effective scattering events N_eff(k)
ax = axes[0, 1]
ax.plot(k_grid, N_eff, 'b-', linewidth=1.5, label='$N_{\\rm eff}(k) = N_{\\rm dom}(1 - {\\rm sinc}(k\\xi))$')
ax.axhline(N_domains, color='gray', linestyle='--', alpha=0.5, label=f'$N_{{\\rm dom}}$ = {N_domains}')
ax.axhline(N_domains / 2.0, color='gray', linestyle=':', alpha=0.3, label=f'$N_{{\\rm dom}}/2$')
ax.axvline(k_c, color='red', linestyle='--', alpha=0.5, label=f'$k_c$')
ax.axvspan(0, 3.0, alpha=0.08, color='orange', label='BdG window')
ax.set_xlabel('$k$ [M$_{\\rm KK}$]', fontsize=11)
ax.set_ylabel('$N_{\\rm eff}(k)$', fontsize=11)
ax.set_title('(b) Effective Scattering Events', fontsize=11)
ax.legend(fontsize=8)
ax.set_xlim(0, 22)
ax.set_ylim(-1, 35)

# (c) Monte Carlo wall crossings
ax = axes[0, 2]
ax.errorbar(k_mc, N_cross_mean, yerr=N_cross_std, fmt='r.', markersize=2,
            elinewidth=0.5, alpha=0.5, label='MC $\\langle N_{\\rm cross}\\rangle$')
# Analytic: N_cross = lambda / xi_KZ = 2*pi / (k * xi_KZ)
N_cross_analytic = 2 * PI / (k_mc * xi_KZ)
ax.plot(k_mc, N_cross_analytic, 'b-', linewidth=1.5, label='$2\\pi/(k \\xi_{\\rm KZ})$')
ax.set_xlabel('$k$ [M$_{\\rm KK}$]', fontsize=11)
ax.set_ylabel('$N_{\\rm cross}$ per wavelength', fontsize=11)
ax.set_title('(c) Wall Crossings per Wavelength', fontsize=11)
ax.legend(fontsize=9)
ax.set_xlim(0, 21)

# (d) Transmission ln T(omega) per branch
ax = axes[1, 0]
for bname in ['B2', 'B1', 'B3']:
    lnT = branches[bname]['lnT']
    valid = lnT > -100
    if valid.any():
        ax.plot(omega_grid_w[valid], lnT[valid], color=branches[bname]['color'],
                linewidth=0.8, label=branches[bname]['label'])
        alpha_t = alpha_from_transmission.get(bname, np.nan)
        if not np.isnan(alpha_t):
            ax.text(0.95, 0.85 - 0.12 * ['B2', 'B1', 'B3'].index(bname),
                    f'$\\alpha_T^{{{bname}}}$ = {alpha_t:.2f}',
                    transform=ax.transAxes, fontsize=9, ha='right',
                    color=branches[bname]['color'])
ax.set_xlabel('$\\omega$ [M$_{\\rm KK}$]', fontsize=11)
ax.set_ylabel('$\\langle \\ln T \\rangle$', fontsize=11)
ax.set_title('(d) Transmission (from COHERENT-WALL-44)', fontsize=11)
ax.legend(fontsize=9)
ax.set_xlim(0, 3)

# (e) Lyapunov exponent spectrum
ax = axes[1, 1]
for bname in ['B2', 'B1', 'B3']:
    gamma = branches[bname]['lyap']
    valid = (~np.isnan(gamma)) & (gamma > 1e-10)
    if valid.any():
        ax.semilogy(omega_grid_w[valid], gamma[valid], color=branches[bname]['color'],
                    linewidth=0.8, label=branches[bname]['label'])
ax.axhline(1.0 / L_total, color='gray', linestyle='--', alpha=0.5,
           label=f'$1/L_{{\\rm total}}$ = {1.0/L_total:.3f}')
ax.set_xlabel('$\\omega$ [M$_{\\rm KK}$]', fontsize=11)
ax.set_ylabel('$\\gamma(\\omega)$ [M$_{\\rm KK}$]', fontsize=11)
ax.set_title('(e) Lyapunov Exponent', fontsize=11)
ax.legend(fontsize=8)
ax.set_xlim(0, 3)

# (f) Alpha summary + Voronoi power spectrum inset
ax = axes[1, 2]
# Bar chart of alpha values
categories = ['Rayleigh\n(analytic)', 'M(k) fit\n(BdG)', 'M(k) fit\n(full)',
              'MC\ncrossings']
values = [2.0, alpha_bdg, alpha_full, alpha_mc]
colors_bar = ['#4daf4a', '#377eb8', '#984ea3', '#e41a1c']
bars = ax.bar(categories, values, color=colors_bar, alpha=0.7, edgecolor='black')
ax.axhline(1.0, color='black', linestyle='--', alpha=0.4, label='$\\alpha = 1$ (geometric optics)')
ax.axhline(2.0, color='green', linestyle='--', alpha=0.4, label='$\\alpha = 2$ (Rayleigh)')
ax.set_ylabel('$\\alpha_{\\rm tess}$', fontsize=12)
ax.set_title('(f) Alpha Summary', fontsize=11)
ax.set_ylim(0, 2.5)
ax.legend(fontsize=8)

# Add value labels on bars
for bar, val in zip(bars, values):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.05,
            f'{val:.3f}', ha='center', va='bottom', fontsize=9, fontweight='bold')

plt.tight_layout()
plt.savefig('tier0-computation/s46_fabric_tessellation.png', dpi=150, bbox_inches='tight')
print(f"  Plot saved to tier0-computation/s46_fabric_tessellation.png")

print(f"\n  Total runtime: {t_elapsed:.1f}s")
print("\n" + "=" * 70)
print("COMPUTATION COMPLETE")
print("=" * 70)
