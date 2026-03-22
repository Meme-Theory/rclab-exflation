#!/usr/bin/env python3
"""
Session 48, Wave 5-F: Volovik Superfluid Program + String Theory Connections
=============================================================================

8 sub-computations testing Volovik's superfluid-universe paradigm and
string-theory constraints applied to the phonon-exflation framework.

Gate: VOLOVIK-STRING-48 (INFO batch — individual sub-gates below)

Sub-computations:
  1. AKAMA-DIAKONOV-48: Emergent acoustic metric from condensate on T^2
  2. HAAR-QTHEORY-48:   Haar-weighted rho_vac(tau) — does tau* shift?
  3. HOMOTOPY-OP-48:    Homotopy type of order parameter manifold on T^2
  4. CONDENSATE-CC-48:   |E_cond| as residual cosmological constant
  5. SWAMPLAND-48:       de Sitter swampland conjecture c(tau)
  6. WZW-STRUTINSKY-48:  WZW partition function vs spectral action
  7. WZW-WINDING-48:     Zak phase / WZW winding mod 2 correspondence
  8. ANALOG-HAWKING-48:  Analog surface gravity and Hawking temperature

Input files:
  - s47_condensate_torus.npz
  - s47_curvature_anatomy.npz
  - s46_qtheory_selfconsistent.npz
  - s44_dos_tau.npz

Output:
  - s48_volovik_string.npz
  - s48_volovik_string.png (4-panel summary)

Author: gen-physicist (Session 48)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
from scipy import interpolate, integrate, linalg
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import (
    tau_fold, M_KK, M_KK_gravity, M_KK_kerner,
    M_Pl_reduced, M_Pl_unreduced,
    E_cond, E_cond_ED_8mode, Delta_0_GL, Delta_B3,
    Vol_SU3_Haar, rho_Lambda_obs, Lambda_obs_MP4,
    rho_crit_GeV4, Omega_Lambda,
    a0_fold, a2_fold, a4_fold, S_fold,
    H_fold, v_terminal, dt_transit,
    xi_BCS, xi_GL, S_inst,
    E_B1, E_B2_mean, E_B3_mean,
    rho_B2_per_mode, N_dof_BCS,
    omega_PV, omega_att,
    G_DeWitt, M_ATDHFB, Z_fold,
    N_cells, PI, g0_diag,
    H_0_GeV,
)

DATA_DIR = os.path.dirname(os.path.abspath(__file__))


def load_npz(name):
    """Load an npz file from the tier0-computation directory."""
    return np.load(os.path.join(DATA_DIR, name), allow_pickle=True)


# ============================================================================
#  LOAD ALL INPUT DATA
# ============================================================================

print("=" * 78)
print("SESSION 48 W5-F: VOLOVIK PROGRAM + STRING THEORY")
print("=" * 78)

d_cond = load_npz('s47_condensate_torus.npz')
d_curv = load_npz('s47_curvature_anatomy.npz')
d_qt   = load_npz('s46_qtheory_selfconsistent.npz')
d_dos  = load_npz('s44_dos_tau.npz')

# Extract condensate data on T^2
theta1 = d_cond['theta1']
theta2 = d_cond['theta2']
N_grid = int(d_cond['N_grid'])
density_haar = d_cond['density_haar_weighted']
density_bcs  = d_cond['density_bcs_weighted']
density_equal = d_cond['density_equal_weight']
haar_measure = d_cond['haar_measure']
radial_r = d_cond['radial_r']
radial_profile = d_cond['radial_profile']
haar_peak_r = float(d_cond['haar_peak_r'])

# Curvature data
K_fold = d_curv['K_fold']       # 28 sectional curvatures at fold
K_all  = d_curv['K_all']        # (26, 28) sectional curvatures vs tau
tau_curv = d_curv['tau_values']  # 26 tau values
R_scalar = d_curv['R_scalar_all']  # scalar curvature vs tau
Ric_eigs = d_curv['Ric_eigs_all']  # (26, 8) Ricci eigenvalues

# Q-theory data
tau_scan_qt = d_qt['tau_scan']       # 60 tau values
E_cond_tau  = d_qt['E_cond_tau']     # condensation energy vs tau
TL_fb       = d_qt['TL_flatband']    # total Lagrangian (flatband)
TL_sc       = d_qt['TL_selfconsistent']  # total Lagrangian (self-consistent)
Delta_B2_sc = d_qt['Delta_B2_sc']    # B2 gap vs tau
Delta_B1_sc = d_qt['Delta_B1_sc']
Delta_B3_sc = d_qt['Delta_B3_sc']
rho_gs_sc   = d_qt['rho_gs_sc']      # ground-state energy density
tau_dense_sc = d_qt['tau_dense_sc']

# DOS data
tau_dos = d_dos['tau_values']  # [0, 0.05, 0.1, 0.15, 0.19]
bin_centers = d_dos['bin_centers']

results = {}  # Collect all results for NPZ output


# ============================================================================
#  1. AKAMA-DIAKONOV-48: Emergent Acoustic Metric from Condensate
# ============================================================================
#
# In the Volovik/Akama-Diakonov framework, the low-energy quasiparticle
# propagation in a superfluid is governed by an effective acoustic metric:
#
#   g^{mu nu}_acoustic = (rho/c_s) [ -c_s^2 + v^2,  -v^j;  -v^i,  delta^{ij} ]
#
# In Painleve-Gullstrand form, for a BCS condensate on the internal space,
# the "flow velocity" v^i is determined by the gradient of the condensate
# phase, and c_BdG is the Bogoliubov speed of sound.
#
# We compute:
# (a) The condensate gradient field |grad Delta| on T^2
# (b) The BdG sound speed c_BdG = Delta_0 / sqrt(2*M_eff)
# (c) Whether |grad Delta| / c_BdG approaches or exceeds 1 (analog horizon)

print("\n" + "=" * 78)
print("1. AKAMA-DIAKONOV-48: Emergent Acoustic Metric")
print("=" * 78)

# Use density_bcs_weighted as the condensate amplitude |Delta(theta1, theta2)|^2
# The condensate density is proportional to |Delta|^2
# We interpret this on T^2 with periodicity [0, 2*pi) in each angle

# Compute |Delta| from density
Delta_field = np.sqrt(np.abs(density_bcs))  # amplitude field

# Gradient on T^2 (periodic boundary conditions)
dtheta = theta1[1] - theta1[0]  # uniform grid spacing

# Metric on T^2 embedded in SU(3): g_{ij} = diag(g_11, g_22)
# For the maximal torus of SU(3) with Killing metric normalization,
# g_{11} = g_{22} = g0_diag (from canonical_constants)
# But the physical metric depends on tau. At fold, the diagonal
# elements of the Cartan metric are modified by e^{2*tau}.
# For T^2 in SU(3), the relevant metric entries at tau_fold:
g_11 = g0_diag * np.exp(2 * tau_fold)  # ~3 * e^{0.38} ~ 4.38
g_22 = g_11  # isotropic Cartan

# Gradient using central differences with periodic BC
grad1 = np.gradient(Delta_field, dtheta, axis=0) / np.sqrt(g_11)
grad2 = np.gradient(Delta_field, dtheta, axis=1) / np.sqrt(g_22)
grad_mag = np.sqrt(grad1**2 + grad2**2)

# BdG sound speed: c_BdG = Delta_0 / sqrt(2 * m_eff)
# For BCS quasiparticles, m_eff ~ 1/(2*t) where t is the hopping
# In our framework, the effective mass is ~ 1/(2*E_B2_mean) in M_KK units
# So c_BdG = Delta_0_GL * sqrt(E_B2_mean) / sqrt(1) ~ Delta_0 * sqrt(E_B2)
# More precisely: E_k = sqrt(epsilon_k^2 + Delta^2), group velocity = d E_k / dk
# At the gap edge (epsilon ~ 0): v_g = 0 (flat dispersion)
# The sound speed is better defined from the Goldstone mode:
# c_BdG^2 = (1/3) * v_F^2 = (1/3) * (dE/dk)_F^2
# With v_F ~ sqrt(2 * E_B2_mean) in M_KK units:
v_F = np.sqrt(2 * E_B2_mean)  # Fermi velocity in M_KK units
c_BdG = v_F / np.sqrt(3)       # Anderson-Bogoliubov sound speed

# The "flow velocity" in the Akama-Diakonov picture is the gradient
# of the condensate phase. But |Delta| varies, so we also need
# the gradient of the amplitude as a proxy for the superflow.
# The ratio |grad Delta| / (Delta * c_BdG) gives the effective Mach number

# Avoid division by zero
Delta_safe = np.where(Delta_field > 1e-10, Delta_field, 1e-10)
mach_field = grad_mag / (Delta_safe * c_BdG)

mach_max = np.max(mach_field)
mach_mean = np.mean(mach_field[haar_measure > 1e-6])  # Haar-weighted region

# Painleve-Gullstrand form: ds^2 = -(c_BdG^2 - v^2)dt^2 - 2v_i dx^i dt + dx^2
# Horizon where v = c_BdG, i.e. Mach = 1
horizon_exists = mach_max >= 1.0

# Acoustic metric determinant and effective curvature
# det(g_acoustic) ~ (rho / c_BdG)^4 for 3+1D
# In our 2D internal space, det ~ (Delta^2 / c_BdG)^2
det_acoustic = (Delta_field**2 / c_BdG)**2

# Scalar curvature of the acoustic metric (2D)
# R_acoustic ~ -nabla^2(log det) / det
log_det = np.log(np.abs(det_acoustic) + 1e-30)
lap_log_det = (np.gradient(np.gradient(log_det, dtheta, axis=0), dtheta, axis=0) / g_11
             + np.gradient(np.gradient(log_det, dtheta, axis=1), dtheta, axis=1) / g_22)
R_acoustic = -lap_log_det  # 2D scalar curvature proxy

print(f"  v_F = {v_F:.4f} M_KK (Fermi velocity)")
print(f"  c_BdG = {c_BdG:.4f} M_KK (Anderson-Bogoliubov sound speed)")
print(f"  max|grad Delta|  = {np.max(grad_mag):.4e}")
print(f"  max Mach number  = {mach_max:.4f}")
print(f"  mean Mach (Haar) = {mach_mean:.4f}")
print(f"  Analog horizon exists: {horizon_exists}")
print(f"  Acoustic R: min={R_acoustic.min():.4e}, max={R_acoustic.max():.4e}")
print(f"  |grad Delta|/Delta peak at: theta1={theta1[np.unravel_index(np.argmax(mach_field), mach_field.shape)[0]]:.3f}, "
      f"theta2={theta2[np.unravel_index(np.argmax(mach_field), mach_field.shape)[1]]:.3f}")

results['akama_v_F'] = v_F
results['akama_c_BdG'] = c_BdG
results['akama_mach_max'] = mach_max
results['akama_mach_mean'] = mach_mean
results['akama_horizon'] = horizon_exists
results['akama_R_acoustic_max'] = np.max(R_acoustic)
results['akama_R_acoustic_min'] = np.min(R_acoustic)

if horizon_exists:
    # Find horizon contour (Mach = 1)
    from scipy.ndimage import binary_dilation
    horizon_mask = np.abs(mach_field - 1.0) < 0.05
    n_horizon_pts = np.sum(horizon_mask)
    print(f"  Horizon contour: {n_horizon_pts} grid points within Mach=1 +/- 0.05")
    results['akama_n_horizon_pts'] = n_horizon_pts
else:
    print(f"  No analog horizon: flow velocity everywhere sub-sonic")
    results['akama_n_horizon_pts'] = 0


# ============================================================================
#  2. HAAR-QTHEORY-48: Haar-Weighted rho_vac(tau)
# ============================================================================
#
# The q-theory vacuum energy is rho_vac = Lagrangian density integrated
# over the internal space. Previous computations (S46) used either
# flat-band or self-consistent DOS but with UNIFORM weighting on T^2.
#
# Physical correction: the Haar measure on SU(3) peaks at the shell
# (r ~ 0.85 from identity), not at identity. The condensate concentrated
# at identity is exponentially suppressed in the Haar measure.
#
# We reweight rho_vac(tau) = int d(vol) * rho(g) * |Delta(g)|^4 / integral(Haar)
# and check whether tau* shifts from the flatband value 0.210 toward 0.19.

print("\n" + "=" * 78)
print("2. HAAR-QTHEORY-48: Haar-Weighted Vacuum Energy")
print("=" * 78)

# The condensate profile |Delta|^2 ~ density_bcs_weighted
# The Haar measure is haar_measure(theta1, theta2)
# The Volovik vacuum energy density ~ Delta^4

# Compute Haar-weighted <Delta^4> as a function of tau
# We need Delta(tau, theta1, theta2). The S47 data gives Delta at tau_fold.
# The S46 data gives sector-averaged Delta_B2(tau) for the tau sweep.

# Strategy: use the T^2 profile shape from S47 as a template,
# then scale by Delta_B2(tau) from S46.

# Normalization: at tau_fold, Delta_B2 = 0.732
Delta_B2_fold_val = float(d_qt['Delta_B2_fold'])

# Template: |Delta(theta)|^2 / <|Delta|^2>_{uniform}
Delta_sq_template = density_bcs / np.mean(density_bcs)

# Delta^4 template (the Volovik vacuum energy goes as Delta^4)
Delta4_template = Delta_sq_template**2

# Compute Haar-weighted vs uniform-weighted <Delta^4>
# Uniform weight: <Delta^4>_uniform = mean(Delta4_template)
Delta4_uniform = np.mean(Delta4_template)

# Haar weight: <Delta^4>_Haar = sum(Delta4_template * haar) / sum(haar)
haar_total = np.sum(haar_measure)
if haar_total > 1e-10:
    Delta4_haar = np.sum(Delta4_template * haar_measure) / haar_total
else:
    Delta4_haar = Delta4_uniform

haar_suppression = Delta4_haar / Delta4_uniform
print(f"  <Delta^4>_uniform = {Delta4_uniform:.6e}")
print(f"  <Delta^4>_Haar    = {Delta4_haar:.6e}")
print(f"  Haar suppression factor = {haar_suppression:.6e}")

# Now compute rho_vac(tau) with Haar weighting
# rho_vac(tau) = (1/V) * E_cond(tau) * haar_suppression
# The total Lagrangian from q-theory: TL(tau) = vacuum + condensation energy

# Flatband total Lagrangian reweighted
TL_haar = TL_fb * haar_suppression

# Find the zero-crossing (vacuum equilibrium)
# tau* is where TL(tau) = 0 or has a stationary point

# Interpolate TL on the scan grid
tau_qt = tau_scan_qt

# Check: does TL_haar have a zero crossing?
TL_haar_interp = TL_fb * haar_suppression  # same shape as TL_fb (60 pts)
# Actually we should be more careful: Haar weight modifies the CONDENSATE
# contribution but the vacuum term is geometric. The total is:
# rho_vac(tau) = rho_geom(tau) + |E_cond(tau)| * haar_suppression

# The q-theory TL is: TL = rho_geom + E_cond (both in M_KK units)
# rho_geom = TL - E_cond
rho_geom = TL_fb - E_cond_tau  # vacuum geometric piece
TL_haar_corrected = rho_geom + E_cond_tau * haar_suppression

# Find tau* where TL_haar has stationary point
dTL_dtau = np.gradient(TL_haar_corrected, tau_qt)
# Find zero crossings of dTL/dtau
sign_changes = np.where(np.diff(np.sign(dTL_dtau)))[0]

tau_star_haar = None
if len(sign_changes) > 0:
    # Linear interpolation for each sign change
    for sc in sign_changes:
        t_low, t_high = tau_qt[sc], tau_qt[sc + 1]
        d_low, d_high = dTL_dtau[sc], dTL_dtau[sc + 1]
        if d_low != d_high:
            tau_star_haar = t_low - d_low * (t_high - t_low) / (d_high - d_low)
            if 0.05 < tau_star_haar < 0.35:
                break
            else:
                tau_star_haar = None

tau_star_fb = float(d_qt['tau_star_flatband_s46'])

print(f"\n  Flatband tau* (S46) = {tau_star_fb:.6f}")
if tau_star_haar is not None:
    print(f"  Haar-weighted tau*  = {tau_star_haar:.6f}")
    shift = tau_star_haar - tau_star_fb
    print(f"  Shift: {shift:+.6f} (toward fold={tau_fold}? {tau_star_haar < tau_star_fb})")
    results['haar_tau_star'] = tau_star_haar
    results['haar_tau_shift'] = shift
else:
    # Check if the TL is monotonic -- no stationary point in domain
    print(f"  Haar-weighted tau*: NO stationary point in [0.05, 0.35]")
    # Report where TL_haar_corrected is minimal
    idx_min = np.argmin(np.abs(TL_haar_corrected))
    print(f"  Closest to zero at tau = {tau_qt[idx_min]:.4f}, TL = {TL_haar_corrected[idx_min]:.6e}")
    results['haar_tau_star'] = tau_qt[idx_min]
    results['haar_tau_shift'] = tau_qt[idx_min] - tau_star_fb

results['haar_suppression'] = haar_suppression
results['haar_tau_star_fb'] = tau_star_fb
results['haar_Delta4_ratio'] = Delta4_haar / Delta4_uniform


# ============================================================================
#  3. HOMOTOPY-OP-48: Homotopy Type of Order Parameter Space
# ============================================================================
#
# The order parameter Delta lives on the internal space SU(3)/maximal torus T^2.
# On T^2, the condensate has a shell structure: |Delta| is peaked near identity
# and exponentially suppressed away from it.
#
# The order parameter MANIFOLD is M = {g in T^2 : |Delta(g)| > threshold}.
# For a shell-shaped condensate:
#   - M ~ S^1 (annulus in 2D) if shell has a hole at identity
#   - M ~ D^2 (disk) if peaked at identity with no hole
#
# Homotopy classification:
#   - D^2: pi_0 = 0 (connected), pi_1 = 0 (simply connected). No vortices.
#   - S^1 x interval (annulus): pi_0 = 0, pi_1 = Z. Vortex strings supported.
#
# The question is: does the Haar-weighted condensate have a ring (annular)
# topology supporting Z-valued vortices?

print("\n" + "=" * 78)
print("3. HOMOTOPY-OP-48: Order Parameter Topology on T^2")
print("=" * 78)

# The condensate density peaks at identity (theta1=theta2=0)
# with contrast_ratio ~ 3.1e6 (highly localized)
contrast = float(d_cond['contrast_ratio'])
density_at_id = float(d_cond['density_at_identity'])

# Radial profile from identity
r_rad = radial_r
prof_rad = radial_profile

# The Haar-weighted density: density_haar_weighted
# This shows the shell structure explicitly
dens_haar_norm = d_cond['density_haar_norm']

# Check radial profile for ring structure
# Is there a local MINIMUM at r=0 in the Haar-weighted profile?
haar_radial = d_cond['radial_haar']
prof_at_zero = prof_rad[0] if len(prof_rad) > 0 else 0.0
prof_peak_idx = np.argmax(prof_rad)
prof_peak_r = r_rad[prof_peak_idx]

# For the Haar-weighted radial profile
haar_rad_peak_idx = np.argmax(haar_radial)
haar_rad_peak_r = r_rad[haar_rad_peak_idx]
haar_at_zero = haar_radial[0]
haar_peak_val = haar_radial[haar_rad_peak_idx]

print(f"  Unweighted condensate:")
print(f"    Peak at r = {prof_peak_r:.4f}, profile(0) = {prof_rad[0]:.4e}")
print(f"    Peaked at identity -> disk topology (D^2)")
print(f"    Contrast ratio = {contrast:.4e}")

print(f"\n  Haar-weighted condensate:")
print(f"    Haar peak at r = {haar_peak_r:.4f}")
print(f"    radial_haar(0) = {haar_at_zero:.4e}")
print(f"    radial_haar(peak) = {haar_peak_val:.4e}")

# Determine topology
# Threshold: 10% of maximum (generous)
threshold_frac = 0.10

# Unweighted: check if level set M = {|Delta| > threshold * max} is disk or annulus
thresh_unw = threshold_frac * np.max(density_bcs)
M_unw = density_bcs > thresh_unw
# Count connected region around identity (theta1=0, theta2=0)
# If the identity is in M, and M is connected around it, topology is D^2
identity_in_M_unw = density_bcs[0, 0] > thresh_unw

# Haar-weighted: same analysis
thresh_haar = threshold_frac * np.max(density_haar)
if np.max(density_haar) > 0:
    M_haar = density_haar > thresh_haar
else:
    M_haar = np.zeros_like(density_haar, dtype=bool)

# Check if haar-weighted M has a hole
# The radial_haar profile: if haar_radial(0) < threshold AND there exists r > 0
# where haar_radial > threshold, we have an annulus (pi_1 = Z)
haar_has_hole = (haar_at_zero < threshold_frac * haar_peak_val) and (haar_peak_val > 0)

# Compute the fraction of T^2 covered by M
area_fraction_unw = np.sum(M_unw) / M_unw.size
area_fraction_haar = np.sum(M_haar) / M_haar.size

# For the unweighted case, compute inner and outer radii of M
# by analyzing the radial profile
if len(r_rad) > 2:
    radial_thresh_unw = threshold_frac * np.max(prof_rad)
    above_thresh = prof_rad > radial_thresh_unw
    if np.any(above_thresh):
        r_inner_unw = r_rad[np.argmax(above_thresh)]  # first r above threshold
        r_outer_unw = r_rad[len(above_thresh) - 1 - np.argmax(above_thresh[::-1])]
        print(f"    Unweighted M: r_inner={r_inner_unw:.4f}, r_outer={r_outer_unw:.4f}")
    else:
        r_inner_unw, r_outer_unw = 0.0, 0.0

    radial_thresh_haar = threshold_frac * haar_peak_val if haar_peak_val > 0 else 0
    above_thresh_h = haar_radial > radial_thresh_haar
    if np.any(above_thresh_h):
        r_inner_haar = r_rad[np.argmax(above_thresh_h)]
        r_outer_haar = r_rad[len(above_thresh_h) - 1 - np.argmax(above_thresh_h[::-1])]
        print(f"    Haar M:       r_inner={r_inner_haar:.4f}, r_outer={r_outer_haar:.4f}")
    else:
        r_inner_haar, r_outer_haar = 0.0, 0.0

# Topology determination
if identity_in_M_unw:
    topo_unw = "D^2 (disk, simply connected)"
    pi1_unw = 0
else:
    topo_unw = "Annulus (pi_1 = Z, vortex-supporting)"
    pi1_unw = 1  # Z

if haar_has_hole:
    topo_haar = "Annulus (pi_1 = Z, vortex-supporting)"
    pi1_haar = 1
else:
    topo_haar = "D^2 (disk, simply connected)"
    pi1_haar = 0

print(f"\n  Topology classification:")
print(f"    Unweighted: {topo_unw}")
print(f"      pi_0 = 0 (connected), pi_1 = {'Z' if pi1_unw else '0'}")
print(f"      Area fraction in M: {area_fraction_unw:.4f}")
print(f"    Haar-weighted: {topo_haar}")
print(f"      pi_0 = 0 (connected), pi_1 = {'Z' if pi1_haar else '0'}")
print(f"      Area fraction in M: {area_fraction_haar:.4f}")

# Physical interpretation
print(f"\n  Physical interpretation:")
if pi1_haar:
    print(f"    Haar-weighted M is an ANNULUS: pi_1(M) = Z")
    print(f"    -> Z-valued vortex strings supported in the condensate")
    print(f"    -> Volovik cosmic string analogy applicable")
    print(f"    -> Shell peak at r={haar_peak_r:.3f}, hole at identity")
else:
    print(f"    Haar-weighted M is a DISK: pi_1(M) = 0")
    print(f"    -> No topological vortex strings")
print(f"    Unweighted condensate is concentrated at identity:")
print(f"    -> {topo_unw}")

results['homotopy_unw_pi1'] = pi1_unw
results['homotopy_haar_pi1'] = pi1_haar
results['homotopy_topo_unw'] = topo_unw
results['homotopy_topo_haar'] = topo_haar
results['homotopy_area_unw'] = area_fraction_unw
results['homotopy_area_haar'] = area_fraction_haar
results['homotopy_haar_has_hole'] = haar_has_hole


# ============================================================================
#  4. CONDENSATE-CC-48: |E_cond| as Residual Cosmological Constant
# ============================================================================
#
# Volovik's key insight (The Universe in a Helium Droplet, Ch. 29):
# In a superfluid, the vacuum energy density of the ground state is
# EXACTLY ZERO by thermodynamic stability (Gibbs-Duhem at T=0).
# The residual CC after phase transition is:
#
#   Lambda ~ Delta^4 / E_F^3
#
# In our framework:
#   - Delta_B2 = 0.732 M_KK (BCS gap at fold)
#   - E_F ~ E_B2_mean = 0.845 M_KK (Fermi energy proxy)
#   - |E_cond| = 0.137 M_KK^4 * Vol(SU(3)) (condensation energy)
#
# The GGE post-transit destroys the condensate (P_exc = 1.000).
# The vacuum energy changes by |E_cond| -> this IS the residual CC.
#
# Compare: rho_Lambda_obs = 2.7e-47 GeV^4

print("\n" + "=" * 78)
print("4. CONDENSATE-CC-48: BCS Condensation Energy as Residual CC")
print("=" * 78)

# Method 1: Direct |E_cond| in physical units
# E_cond is in M_KK units (energy per mode). Physical energy density:
# rho_cond = |E_cond| * M_KK^4 / Vol(SU(3))  [GeV^4]
# The E_cond = -0.137 is the total energy, already volume-integrated.
# So rho_cond = |E_cond| * M_KK^4

rho_cond_gravity = abs(E_cond) * M_KK_gravity**4
rho_cond_kerner  = abs(E_cond) * M_KK_kerner**4

ratio_gravity = rho_cond_gravity / rho_Lambda_obs
ratio_kerner  = rho_cond_kerner  / rho_Lambda_obs

print(f"  |E_cond| = {abs(E_cond):.6f} (M_KK units)")
print(f"  M_KK (gravity) = {M_KK_gravity:.4e} GeV")
print(f"  M_KK (Kerner)  = {M_KK_kerner:.4e} GeV")

print(f"\n  rho_cond (gravity route): {rho_cond_gravity:.4e} GeV^4")
print(f"  rho_cond (Kerner route):  {rho_cond_kerner:.4e} GeV^4")
print(f"  rho_Lambda_obs:           {rho_Lambda_obs:.4e} GeV^4")

print(f"\n  Ratio rho_cond/rho_Lambda:")
print(f"    Gravity route: {ratio_gravity:.4e} (log10 = {np.log10(ratio_gravity):.2f})")
print(f"    Kerner route:  {ratio_kerner:.4e} (log10 = {np.log10(ratio_kerner):.2f})")

# Method 2: Volovik's Delta^4 formula
# rho_vac ~ Delta^4 / (hbar * c)^3 for 3He-B (Chapter 29, Volovik)
# In our units: rho_vac ~ Delta_B2^4 * M_KK^4 / (something involving E_F)
# The naive estimate is just Delta_B2^4:
Delta_B2_val = float(d_qt['Delta_B2_fold'])
rho_volovik = Delta_B2_val**4 * M_KK_gravity**4
ratio_volovik = rho_volovik / rho_Lambda_obs

print(f"\n  Volovik Delta^4 estimate:")
print(f"    Delta_B2 = {Delta_B2_val:.4f} M_KK")
print(f"    Delta_B2^4 * M_KK^4 = {rho_volovik:.4e} GeV^4")
print(f"    Ratio to observed: {ratio_volovik:.4e} (log10 = {np.log10(ratio_volovik):.2f})")

# Method 3: The CC gap = log10(rho_framework / rho_obs)
# The standard CC problem is 120 orders. How many does the condensate reduce?
cc_gap_gravity = np.log10(ratio_gravity)
cc_gap_kerner  = np.log10(ratio_kerner)
cc_gap_naive   = np.log10(M_KK_gravity**4 / rho_Lambda_obs)  # no suppression

print(f"\n  CC gap analysis:")
print(f"    Naive M_KK^4/Lambda_obs: 10^{cc_gap_naive:.1f}")
print(f"    With |E_cond| suppression (gravity): 10^{cc_gap_gravity:.1f}")
print(f"    With |E_cond| suppression (Kerner):  10^{cc_gap_kerner:.1f}")
print(f"    Orders gained by BCS: {cc_gap_naive - cc_gap_gravity:.1f} (gravity)")
print(f"    Still short by: {cc_gap_gravity:.1f} orders (gravity route)")

results['cc_rho_cond_grav'] = rho_cond_gravity
results['cc_rho_cond_kern'] = rho_cond_kerner
results['cc_ratio_grav'] = ratio_gravity
results['cc_ratio_kern'] = ratio_kerner
results['cc_gap_gravity'] = cc_gap_gravity
results['cc_gap_kerner'] = cc_gap_kerner
results['cc_gap_naive'] = cc_gap_naive
results['cc_orders_gained'] = cc_gap_naive - cc_gap_gravity


# ============================================================================
#  5. SWAMPLAND-48: de Sitter Conjecture c(tau) Along Jensen Path
# ============================================================================
#
# The de Sitter swampland conjecture (Obied-Ooguri-Spodyneiko-Vafa 2018):
#   c = |V'| / (V * M_Pl) >= O(1)
# must hold for any consistent quantum gravity potential.
#
# Our "potential" is the q-theory total Lagrangian TL(tau).
# The species scale is Lambda_sp / M_KK = 2.06 (from prior work).
# We compute c(tau) along the Jensen deformation path.
#
# Gate: PASS if c > O(1) somewhere in [0.05, 0.35].

print("\n" + "=" * 78)
print("5. SWAMPLAND-48: de Sitter Conjecture c(tau)")
print("=" * 78)

# Use TL_flatband as the potential V(tau)
V_tau = TL_fb  # dimensionless (M_KK^4 units)

# Compute V'(tau) = dTL/dtau
dV_dtau = np.gradient(V_tau, tau_qt)

# The modulus tau has a kinetic term with coefficient G_DeWitt
# so the canonically normalized field is phi = sqrt(2 * G_DeWitt) * tau
# and V'_canonical = dV/dphi = dV/dtau / sqrt(2 * G_DeWitt)

# M_Pl in M_KK units: M_Pl / M_KK
M_Pl_MKK = M_Pl_reduced / M_KK_gravity

# c = |dV/dphi| / (V * M_Pl) = |dV/dtau| / (sqrt(2*G_DeWitt) * V * M_Pl_MKK)
# Only meaningful where V > 0
V_positive = V_tau > 0
c_swamp = np.zeros_like(V_tau)
c_swamp[V_positive] = np.abs(dV_dtau[V_positive]) / (
    np.sqrt(2 * G_DeWitt) * V_tau[V_positive])
# The factor of M_Pl: in Planck units the conjecture is c >= O(1)
# Our V is in M_KK^4, so V/M_Pl^4 = V * (M_KK/M_Pl)^4
# c = |V'_phi| / V = (|dV/dtau| / sqrt(2*G)) / V (in same units)
# This is the DIMENSIONLESS gradient, which is what the conjecture constrains

# Actually, the correct form is:
# c = M_Pl * |grad V| / V  where grad is in field space with kinetic normalization
# = |dV/dtau| / (sqrt(2*G_DeWitt) * V) * M_Pl / M_KK   ... no, dimensions:
# V is in M_KK^4, dV/dtau in M_KK^4, sqrt(2*G) is dimensionless
# The conjecture in natural units: M_Pl * |nabla V| / V >= c ~ O(1)
# So c = (M_Pl_MKK * |dV/dtau|) / (sqrt(2*G_DeWitt) * V)

c_swamp_correct = np.zeros_like(V_tau)
c_swamp_correct[V_positive] = (M_Pl_MKK * np.abs(dV_dtau[V_positive])) / (
    np.sqrt(2 * G_DeWitt) * V_tau[V_positive])

# Also compute the refined conjecture: min(c, M_Pl^2 * V'' / V) >= O(1)
d2V_dtau2 = np.gradient(dV_dtau, tau_qt)
c_refined = np.zeros_like(V_tau)
c_refined[V_positive] = -(M_Pl_MKK**2 * d2V_dtau2[V_positive]) / (
    2 * G_DeWitt * V_tau[V_positive])
# The refined conjecture says min(|V'|/V, -V''/V) >= c
# If V'' < 0, this gives a positive contribution (unstable = good for swampland)

# Species scale correction
Lambda_sp_over_MKK = 2.06  # from prior session
# With species scale, M_Pl -> Lambda_sp in the constraint
c_species = c_swamp_correct * (M_KK_gravity / (Lambda_sp_over_MKK * M_KK_gravity))
# Actually Lambda_sp/M_KK = 2.06, so Lambda_sp = 2.06 * M_KK
# c_species = Lambda_sp * |dV/dtau| / (sqrt(2*G) * V) = 2.06 * |dV/dtau| / (sqrt(2*G)*V)
c_species_correct = np.zeros_like(V_tau)
c_species_correct[V_positive] = (Lambda_sp_over_MKK * np.abs(dV_dtau[V_positive])) / (
    np.sqrt(2 * G_DeWitt) * V_tau[V_positive])

# Find max c values
c_max = np.max(c_swamp_correct[V_positive]) if np.any(V_positive) else 0
c_at_fold_idx = np.argmin(np.abs(tau_qt - tau_fold))
c_at_fold = c_swamp_correct[c_at_fold_idx] if V_positive[c_at_fold_idx] else 0

c_species_max = np.max(c_species_correct[V_positive]) if np.any(V_positive) else 0

# Swampland PASS/FAIL
swampland_pass = c_max > 1.0  # O(1) means >= 1
swampland_pass_species = c_species_max > 1.0

print(f"  G_DeWitt = {G_DeWitt:.2f}")
print(f"  M_Pl / M_KK = {M_Pl_MKK:.4e}")
print(f"  Lambda_sp / M_KK = {Lambda_sp_over_MKK:.2f}")
print(f"  sqrt(2*G_DeWitt) = {np.sqrt(2*G_DeWitt):.4f}")

print(f"\n  c(tau) = M_Pl * |dV/dphi| / V:")
print(f"    max(c) = {c_max:.4e}")
print(f"    c(fold) = {c_at_fold:.4e}")
print(f"    PASS (c > 1): {swampland_pass}")

print(f"\n  c_species(tau) = Lambda_sp * |dV/dphi| / V:")
print(f"    max(c_species) = {c_species_max:.4e}")
print(f"    PASS (c_species > 1): {swampland_pass_species}")

# The refined conjecture
c_refined_max = np.max(c_refined[V_positive]) if np.any(V_positive) else 0
c_refined_at_fold = c_refined[c_at_fold_idx] if V_positive[c_at_fold_idx] else 0
print(f"\n  Refined conjecture (-M_Pl^2 * V'' / (2*G*V)):")
print(f"    max(c_refined) = {c_refined_max:.4e}")
print(f"    c_refined(fold) = {c_refined_at_fold:.4e}")
print(f"    Either c or c_refined > 1 needed: {c_max > 1 or c_refined_max > 1}")

results['swamp_c_max'] = c_max
results['swamp_c_at_fold'] = c_at_fold
results['swamp_c_species_max'] = c_species_max
results['swamp_c_refined_max'] = c_refined_max
results['swamp_pass'] = swampland_pass
results['swamp_pass_species'] = swampland_pass_species
results['swamp_c_tau'] = c_swamp_correct
results['swamp_tau'] = tau_qt


# ============================================================================
#  6. WZW-STRUTINSKY-48: WZW Partition Function vs Spectral Action
# ============================================================================
#
# The Wess-Zumino-Witten (WZW) model on SU(3) at level k has partition function:
#   Z_WZW = sum over integrable reps at level k of |chi_lambda(q)|^2
#
# The spectral action is: S = Tr[f(D^2/Lambda^2)]
#
# The Strutinsky energy theorem says the oscillating part of the DOS
# gives rise to shell corrections that should be captured by a WZW-like model.
# We compare the Strutinsky smooth + oscillating decomposition of the
# spectral action against a WZW partition function approximation.
#
# Benchmark: 95-99% agreement in the ratio S_WZW / S_spectral at fold.

print("\n" + "=" * 78)
print("6. WZW-STRUTINSKY-48: WZW vs Spectral Action")
print("=" * 78)

# Strategy: Compute the Strutinsky decomposition of the DOS at the fold
# and compare the smooth part (Weyl term) against the WZW prediction.

# Load DOS at fold (tau = 0.19)
omega_fold = d_dos['tau0.19_all_omega']
dim2_fold  = d_dos['tau0.19_all_dim2']
rho_smooth_fold = d_dos['tau0.19_rho_smooth']
rho_hist_fold   = d_dos['tau0.19_rho_w']

# The spectral action with heat kernel cutoff:
# S = sum_n f(lambda_n^2 / Lambda^2) ~ integral rho(omega) * f(omega^2 / Lambda^2) domega
# For a sharp cutoff at Lambda: S = N(Lambda) = integral_0^Lambda rho(omega) domega

# We need the eigenvalues at the fold. omega_fold contains all 992 eigenvalues.
all_omega = np.sort(omega_fold)

# Cumulative state count
N_cum = np.arange(1, len(all_omega) + 1)

# Smooth (Weyl) part: N_smooth(E) = a_0 + a_2 * E + a_4 * E^2
# where a_0, a_2, a_4 are the Seeley-DeWitt coefficients
# Actually, Weyl's law for eigenvalues of Laplacian on SU(3):
# N(Lambda) ~ Vol * Lambda^d / (4*pi)^{d/2} / Gamma(d/2+1) for d = dim(SU(3)) = 8
# In our case d = 8 (dim of SU(3)), so:
#   N_Weyl(E) = Vol_SU3 * E^4 / (4*pi)^4 / Gamma(5) = Vol * E^4 / (256*pi^4*24)
# But our eigenvalues are of D_K (Dirac), not Laplacian. D_K^2 ~ Laplacian.
# N_Weyl(Lambda) = C * Lambda^8 for Dirac on 8-manifold (SU(3) is 8D)

# Fit the smooth part with a polynomial in omega
# Use the cumulative N(omega) and fit to omega^4 (Weyl in 8D halved for Dirac)
omega_max_data = all_omega[-1]

# Weyl fitting: N(E) = c_4 * E^4 (leading term for Dirac on 8-manifold)
# Actually for a Dirac operator on a d-dimensional manifold:
# N(E) ~ Vol / (d-dim Weyl constant) * E^d
# On SU(3), d = 8 (real dim), so N(E) ~ c * E^4 (half the dimension because
# eigenvalues come in +/- pairs, and we count only positive)

# More carefully: at max_pq_sum = 6, we have a truncated spectrum.
# Let's just compare the integrated spectral density.

# Strutinsky smooth: use Gaussian averaging of rho(omega)
# rho_smooth(omega) = (1/sqrt(2*pi)*gamma) * int rho(omega') * exp(-(omega-omega')^2/(2*gamma^2)) domega'
gamma_strut = 0.05  # smoothing width in M_KK

# Build histogram of eigenvalues
omega_bins = np.linspace(0.7, 2.2, 200)
omega_bin_c = 0.5 * (omega_bins[:-1] + omega_bins[1:])
domega = omega_bins[1] - omega_bins[0]

# Weighted histogram (each eigenvalue has degeneracy from dim^2)
hist_osc, _ = np.histogram(all_omega, bins=omega_bins, weights=dim2_fold)
hist_count, _ = np.histogram(all_omega, bins=omega_bins)

# Smooth via Gaussian convolution
gauss_kernel = np.exp(-omega_bin_c**2 / (2 * gamma_strut**2))
gauss_kernel /= np.sum(gauss_kernel) * domega

rho_strutinsky_smooth = np.convolve(hist_osc, gauss_kernel, mode='same')
rho_oscillating = hist_osc - rho_strutinsky_smooth

# WZW partition function at level k
# For SU(3) at level k, the partition function is:
# Z_k = sum_{p+q <= k} |chi_{(p,q)}(q_param)|^2 * d_{(p,q)}^2
# where d_{(p,q)} = (p+1)(q+1)(p+q+2)/2 is the dimension
#
# The WZW level is related to the cutoff: k ~ Lambda / M_KK
# At the fold with max_pq_sum = 6, k_eff ~ 6

k_eff = 6  # effective WZW level (from truncation)

# Generate SU(3) representations at level k_eff
reps = []
for p in range(k_eff + 1):
    for q in range(k_eff + 1 - p):
        dim_pq = (p + 1) * (q + 1) * (p + q + 2) // 2
        # Casimir eigenvalue: C2(p,q) = (p^2 + q^2 + p*q + 3*p + 3*q)/3
        C2 = (p**2 + q**2 + p*q + 3*p + 3*q) / 3.0
        reps.append((p, q, dim_pq, C2))

# WZW energies: E_{(p,q)} = sqrt(C2 + m_0^2) where m_0 is the gap
# From our spectrum: the gap is ~0.82 M_KK
omega_gap = float(d_dos['omega_gap_vs_tau'][-1])  # at fold
reps_sorted = sorted(reps, key=lambda x: x[3])

# Compute WZW spectral action: S_WZW = sum d_{(p,q)}^2 * f(C2(p,q))
# Using heat kernel: f(x) = exp(-x / Lambda^2)
# At the fold, we use Lambda = omega_max_data as the cutoff

Lambda_wzw = omega_max_data
S_wzw_heat = sum(d**2 * np.exp(-C2 / Lambda_wzw**2) for (_, _, d, C2) in reps)
S_wzw_sharp = sum(d**2 for (_, _, d, C2) in reps if np.sqrt(C2) <= Lambda_wzw)

# Spectral action from actual eigenvalues
# S_spectral = sum f(omega_n^2 / Lambda^2) * deg_n
S_spectral_heat = np.sum(dim2_fold * np.exp(-omega_fold**2 / Lambda_wzw**2))
S_spectral_sharp = np.sum(dim2_fold[omega_fold <= Lambda_wzw])

# Agreement ratio
agreement_heat = S_wzw_heat / S_spectral_heat if S_spectral_heat > 0 else 0
agreement_sharp = S_wzw_sharp / S_spectral_sharp if S_spectral_sharp > 0 else 0

print(f"  k_eff = {k_eff} (WZW level from truncation)")
print(f"  Number of reps at level {k_eff}: {len(reps)}")
print(f"  Lambda_cutoff = {Lambda_wzw:.4f} M_KK")
print(f"  omega_gap = {omega_gap:.4f} M_KK")

print(f"\n  Heat kernel cutoff:")
print(f"    S_WZW = {S_wzw_heat:.2f}")
print(f"    S_spectral = {S_spectral_heat:.2f}")
print(f"    Ratio S_WZW/S_spectral = {agreement_heat:.4f}")
print(f"    Agreement: {100*agreement_heat:.1f}%")

print(f"\n  Sharp cutoff:")
print(f"    S_WZW = {S_wzw_sharp:.2f}")
print(f"    S_spectral = {S_spectral_sharp:.2f}")
print(f"    Ratio S_WZW/S_spectral = {agreement_sharp:.4f}")
print(f"    Agreement: {100*agreement_sharp:.1f}%")

# Strutinsky shell energy
E_shell = np.sum(rho_oscillating * omega_bin_c * domega)
E_smooth = np.sum(rho_strutinsky_smooth * omega_bin_c * domega)
shell_fraction = abs(E_shell) / abs(E_smooth) if abs(E_smooth) > 0 else 0

print(f"\n  Strutinsky decomposition:")
print(f"    E_smooth = {E_smooth:.4f}")
print(f"    E_shell  = {E_shell:.4f}")
print(f"    |E_shell/E_smooth| = {shell_fraction:.4f}")

results['wzw_k_eff'] = k_eff
results['wzw_n_reps'] = len(reps)
results['wzw_agreement_heat'] = agreement_heat
results['wzw_agreement_sharp'] = agreement_sharp
results['wzw_S_heat'] = S_wzw_heat
results['wzw_S_spectral_heat'] = S_spectral_heat
results['wzw_shell_fraction'] = shell_fraction
results['wzw_E_shell'] = E_shell
results['wzw_E_smooth'] = E_smooth


# ============================================================================
#  7. WZW-WINDING-48: Zak Phase / WZW Winding mod 2
# ============================================================================
#
# The Z_2 Zak phase (BDI class topological invariant) is:
#   gamma_Zak = pi * (number of occupied bands with phi_Berry = pi) mod 2*pi
#
# The WZW winding number for SU(3) maps to pi_5(SU(3)) = Z.
# In the BDI class, the topological invariant is Z, but the Zak phase
# gives a Z_2 reduction.
#
# From S35: sgn(Pf) = -1 at all 34 tau values. Each of the 10 sectors
# has a strict pi Zak phase. 10 mod 2 = 0.
#
# The WZW level-k winding is: W = k mod 2 (for the Z_2 reduction).
# With k_eff = 6: W = 6 mod 2 = 0.
#
# Question: Does 10 (Zak) mod 2 = 0 match W = k mod 2 = 0?

print("\n" + "=" * 78)
print("7. WZW-WINDING-48: Zak Phase vs WZW Winding mod 2")
print("=" * 78)

# From prior sessions (S35 permanent):
# - BDI class: T^2 = +1 (AZ classification)
# - sgn(Pf) = -1 at ALL 34 tau values (S35)
# - Spectral gap open: min gap = 0.819 M_KK
#
# The Zak phase decomposition:
# 16 modes total: 10 with phi_Berry = pi (4 B2 + 2*3 B3 contributions)
# and 6 with phi_Berry = 0.
# Actually, the BDI invariant is the Pfaffian sign, which is -1.
# This corresponds to a Z_2 invariant nu = 1 (nontrivial).

# The Zak phases for each sector at the fold
# B1: 1 mode, q_7 = 0 -> Zak = 0 (trivial, real, T^2=+1 singlet)
# B2: 4 modes, q_7 = +/-0.25 -> each pair contributes pi (from PH symmetry)
#     4 modes -> 2 pairs -> 2*pi -> mod 2*pi = 0? No:
#     Actually the Zak phase per band is pi if the band is inverted.
#     With PH symmetry, each mode at +E has partner at -E.
#     The BDI Pfaffian sign counts the parity of the number of negative-energy
#     states with pi Berry phase.

# S35 result: Pf = -1. This is nu_BDI = 1 (odd winding).
nu_BDI = 1  # From S35 Pfaffian

# Number of pi-phase bands (from 16-state Hilbert space)
# The 16 states decompose into 8 positive-energy and 8 negative-energy
# Under BDI, the invariant is W_BDI = number of occupied bands with
# Berry phase pi, mod 2
# From the spectral structure: 10 modes have nontrivial topology
n_pi_bands = 10  # from spectral decomposition
zak_mod2 = n_pi_bands % 2  # = 0

# WZW winding
# pi_5(SU(3)) = Z (Bott periodicity)
# The WZW winding number at level k is W_WZW = k
# Z_2 reduction: W_WZW mod 2
wzw_winding = k_eff  # = 6
wzw_mod2 = wzw_winding % 2  # = 0

# Match?
match = (zak_mod2 == wzw_mod2)

# But the Pfaffian is -1, meaning nu_BDI = 1 (ODD).
# This is a Z_2 invariant independent of the Zak phase counting.
# The CORRECT comparison is:
#   nu_BDI (Pfaffian) mod 2 vs W_WZW mod 2
# nu_BDI = 1 (odd), W_WZW = 6 mod 2 = 0 (even)
# MISMATCH!

# However, there's a subtlety: the Pfaffian sign is (-1)^nu,
# so Pf = -1 means nu = 1 (odd).
# The WZW level k = 6 gives winding 6, mod 2 = 0 (even).
# These are DIFFERENT Z_2 invariants measuring different things:
# - Pfaffian: topology of the Hilbert space (internal)
# - WZW: topology of the target space map (pi_5(SU(3)))

print(f"  BDI Pfaffian: sgn(Pf) = -1 -> nu_BDI = {nu_BDI} (ODD)")
print(f"  Number of pi-phase bands: {n_pi_bands}")
print(f"  Zak phase count mod 2: {zak_mod2}")
print(f"  WZW level: k_eff = {k_eff}")
print(f"  WZW winding mod 2: {wzw_mod2}")
print(f"\n  Comparison (Zak count mod 2 vs WZW mod 2): {'MATCH' if match else 'MISMATCH'}")
print(f"  Comparison (Pfaffian nu vs WZW mod 2): {'MATCH' if nu_BDI % 2 == wzw_mod2 else 'MISMATCH'}")

print(f"\n  Analysis:")
print(f"    The 10 pi-phases and WZW k=6 both give 0 mod 2 -> MATCH")
print(f"    But the Pfaffian nu=1 gives 1 mod 2 -> MISMATCH with WZW")
print(f"    These are INDEPENDENT invariants:")
print(f"      - Pfaffian = Hilbert space topology (BDI fiber)")
print(f"      - WZW winding = target space topology (pi_5(SU(3)))")
print(f"    The mismatch is EXPECTED: they measure different obstructions")
print(f"    The Pfaffian protects the BCS state; WZW classifies the field theory")

results['wzw_nu_BDI'] = nu_BDI
results['wzw_n_pi_bands'] = n_pi_bands
results['wzw_zak_mod2'] = zak_mod2
results['wzw_winding_mod2'] = wzw_mod2
results['wzw_zak_match'] = match
results['wzw_pfaffian_match'] = (nu_BDI % 2 == wzw_mod2)


# ============================================================================
#  8. ANALOG-HAWKING-48: Analog Surface Gravity and Hawking Temperature
# ============================================================================
#
# In the Unruh/Volovik analog gravity program, a sonic horizon in a
# flowing superfluid produces analog Hawking radiation with temperature:
#   T_H = (hbar / 2*pi*k_B) * kappa
# where kappa is the surface gravity:
#   kappa = d|v|/dr |_{horizon} = d(|grad Delta|/Delta)/dr |_{horizon}
#
# From computation 1 (AKAMA-DIAKONOV), we found whether a horizon exists.
# If yes, compute the surface gravity and T_Hawking.
# If no, compute the maximum "attempted" surface gravity.

print("\n" + "=" * 78)
print("8. ANALOG-HAWKING-48: Analog Surface Gravity + Hawking Temperature")
print("=" * 78)

# From AKAMA-DIAKONOV: mach_field = |grad Delta| / (Delta * c_BdG)
# The velocity field is v(theta) = |grad Delta(theta)| / Delta(theta) (phase gradient)
# Actually, for the BCS condensate, the superflow velocity is proportional
# to the phase gradient, not the amplitude gradient. But in the internal space,
# the "flow" is the variation of the order parameter, so we use:
# v_eff(theta) = c_BdG * mach_field(theta)

v_eff = c_BdG * mach_field  # effective velocity field

# Surface gravity = d|v|/dn at the horizon, where n is the normal direction
# Since we don't have a horizon (mach_max < 1 typically), compute the
# maximum gradient of the Mach number as a proxy

# Gradient of Mach field
dmach_d1 = np.gradient(mach_field, dtheta, axis=0) / np.sqrt(g_11)
dmach_d2 = np.gradient(mach_field, dtheta, axis=1) / np.sqrt(g_22)
grad_mach_mag = np.sqrt(dmach_d1**2 + dmach_d2**2)

# Surface gravity proxy: kappa = c_BdG * |grad(Mach)| at maximum Mach
idx_max_mach = np.unravel_index(np.argmax(mach_field), mach_field.shape)
kappa_proxy = c_BdG * grad_mach_mag[idx_max_mach]

# Maximum surface gravity over all points
kappa_max = c_BdG * np.max(grad_mach_mag)

# Hawking temperature (if horizon existed)
# T_H = kappa / (2*pi) in natural units (hbar = k_B = 1)
T_H_proxy = kappa_proxy / (2 * PI)  # in M_KK units
T_H_max = kappa_max / (2 * PI)

# Convert to physical units
T_H_proxy_GeV = T_H_proxy * M_KK_gravity  # GeV
T_H_proxy_K = T_H_proxy_GeV / (8.617333262e-14)  # K (using k_B in GeV/K)

print(f"  From AKAMA-DIAKONOV:")
print(f"    c_BdG = {c_BdG:.4f} M_KK")
print(f"    max Mach = {mach_max:.4f}")
print(f"    Horizon exists: {horizon_exists}")

print(f"\n  Surface gravity analysis:")
print(f"    kappa at max Mach = {kappa_proxy:.4e} M_KK^2")
print(f"    kappa_max (over all) = {kappa_max:.4e} M_KK^2")

print(f"\n  Analog Hawking temperature (proxy):")
print(f"    T_H = kappa/(2*pi) = {T_H_proxy:.4e} M_KK")
print(f"    T_H = {T_H_proxy_GeV:.4e} GeV")
print(f"    T_H = {T_H_proxy_K:.4e} K")

# Compare with actual transit temperature
T_compound_MKK = abs(E_cond) * 443.0 / N_dof_BCS  # E_exc / N_dof
print(f"\n  Comparison:")
print(f"    T_compound (microcanonical) = {T_compound_MKK:.4f} M_KK")
print(f"    T_H (analog) / T_compound   = {T_H_proxy / T_compound_MKK:.4e}")

# The transit IS Parker production, NOT Hawking (S38 result).
# Even if a horizon existed, the Hawking temperature would be negligible
# compared to the Kibble-Zurek excitation energy.
# The ratio T_H / T_compound quantifies this hierarchy.

# Check: does the condensate gradient speed ever exceed c_BdG during transit?
# During transit, v_terminal = 26.54 M_KK (much larger than c_BdG ~ 0.75)
# This is the MODULUS velocity, not the condensate flow velocity.
# The condensate flow is |grad Delta|/Delta, which is bounded by the
# geometry of T^2. The transit velocity is in tau-space, not internal space.
print(f"\n  Transit velocity in tau-space: v_terminal = {v_terminal:.2f} M_KK")
print(f"  v_terminal / c_BdG = {v_terminal / c_BdG:.1f}x (supersonic in tau)")
print(f"  But tau and theta are DIFFERENT directions: no horizon from transit alone")

# Gradient of Delta along the TAU direction (from S46 data)
# d Delta_B2 / d tau at the fold
dDelta_dtau = np.gradient(Delta_B2_sc, tau_scan_qt)
idx_fold_qt = np.argmin(np.abs(tau_scan_qt - tau_fold))
dDelta_dtau_fold = abs(dDelta_dtau[idx_fold_qt])

# Tau-direction Mach number during transit
v_tau_eff = v_terminal * dDelta_dtau_fold / max(Delta_B2_sc[idx_fold_qt], 1e-10)
mach_tau = v_tau_eff / c_BdG

print(f"\n  Tau-direction analysis:")
print(f"    |dDelta_B2/dtau| at fold = {dDelta_dtau_fold:.4f}")
print(f"    Effective tau-velocity = {v_tau_eff:.4f} M_KK")
print(f"    Mach_tau = {mach_tau:.4f}")
if mach_tau > 1:
    kappa_tau = c_BdG * abs(np.gradient(np.gradient(Delta_B2_sc, tau_scan_qt), tau_scan_qt)[idx_fold_qt]) / max(Delta_B2_sc[idx_fold_qt], 1e-10)
    T_H_tau = kappa_tau / (2 * PI) * M_KK_gravity
    print(f"    SUPERSONIC in tau: analog horizon in mixed (tau, theta) space")
    print(f"    kappa_tau = {kappa_tau:.4e} M_KK^2")
    print(f"    T_H_tau = {T_H_tau:.4e} GeV")
    results['hawking_mach_tau_supersonic'] = True
    results['hawking_kappa_tau'] = kappa_tau
else:
    print(f"    Subsonic in tau: no analog horizon in any direction")
    results['hawking_mach_tau_supersonic'] = False

results['hawking_mach_max'] = mach_max
results['hawking_kappa_proxy'] = kappa_proxy
results['hawking_kappa_max'] = kappa_max
results['hawking_T_H_proxy_MKK'] = T_H_proxy
results['hawking_T_H_proxy_GeV'] = T_H_proxy_GeV
results['hawking_T_H_proxy_K'] = T_H_proxy_K
results['hawking_mach_tau'] = mach_tau
results['hawking_T_compound_MKK'] = T_compound_MKK


# ============================================================================
#  SUMMARY AND GATE VERDICTS
# ============================================================================

print("\n" + "=" * 78)
print("VOLOVIK-STRING-48 SUMMARY")
print("=" * 78)

verdicts = {
    "AKAMA-DIAKONOV-48": "INFO" if not horizon_exists else "PASS",
    "HAAR-QTHEORY-48":   "INFO",
    "HOMOTOPY-OP-48":    "INFO",
    "CONDENSATE-CC-48":  "INFO",
    "SWAMPLAND-48":      "PASS" if swampland_pass else "FAIL",
    "WZW-STRUTINSKY-48": "INFO",
    "WZW-WINDING-48":    "INFO",
    "ANALOG-HAWKING-48": "INFO" if not horizon_exists else "PASS",
}

key_numbers = {
    "AKAMA-DIAKONOV-48": f"Mach_max={mach_max:.4f}, c_BdG={c_BdG:.4f}",
    "HAAR-QTHEORY-48":   f"suppression={haar_suppression:.4e}, tau*_shift={results.get('haar_tau_shift', 'N/A')}",
    "HOMOTOPY-OP-48":    f"pi_1(Haar)={'Z' if pi1_haar else '0'}, pi_1(unw)={'Z' if pi1_unw else '0'}",
    "CONDENSATE-CC-48":  f"|E_cond|/Lambda_obs=10^{cc_gap_gravity:.1f}, orders_gained={cc_gap_naive-cc_gap_gravity:.1f}",
    "SWAMPLAND-48":      f"c_max={c_max:.4e}, c_species={c_species_max:.4e}",
    "WZW-STRUTINSKY-48": f"heat_agreement={100*agreement_heat:.1f}%, shell_frac={shell_fraction:.4f}",
    "WZW-WINDING-48":    f"Zak(10 mod 2)=0, WZW(6 mod 2)=0 -> MATCH; Pf(1) vs WZW(0) -> MISMATCH",
    "ANALOG-HAWKING-48": f"kappa_max={kappa_max:.4e}, T_H={T_H_proxy:.4e} M_KK, Mach_tau={mach_tau:.4f}",
}

for name in verdicts:
    print(f"\n  {name}: {verdicts[name]}")
    print(f"    {key_numbers[name]}")

# Overall gate
n_pass = sum(1 for v in verdicts.values() if v == "PASS")
n_fail = sum(1 for v in verdicts.values() if v == "FAIL")
n_info = sum(1 for v in verdicts.values() if v == "INFO")

print(f"\n  Overall: {n_pass} PASS, {n_fail} FAIL, {n_info} INFO")
print(f"  Gate VOLOVIK-STRING-48: INFO (batch, as pre-registered)")

results['gate_name'] = 'VOLOVIK-STRING-48'
results['gate_verdict'] = 'INFO'
results['verdicts'] = str(verdicts)
results['key_numbers'] = str(key_numbers)


# ============================================================================
#  SAVE RESULTS
# ============================================================================

outfile = os.path.join(DATA_DIR, 's48_volovik_string.npz')
# Convert string values for numpy
save_dict = {}
for k, v in results.items():
    if isinstance(v, str):
        save_dict[k] = np.array(v)
    elif isinstance(v, bool):
        save_dict[k] = np.array(v)
    elif isinstance(v, np.ndarray):
        save_dict[k] = v
    else:
        save_dict[k] = np.array(v)

np.savez_compressed(outfile, **save_dict)
print(f"\n  Saved: {outfile}")


# ============================================================================
#  PLOTS: 4-panel summary
# ============================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Session 48 W5-F: Volovik Program + String Theory', fontsize=14, fontweight='bold')

# Panel 1: Acoustic Mach number on T^2
ax = axes[0, 0]
T1, T2 = np.meshgrid(theta1, theta2, indexing='ij')
im = ax.pcolormesh(T1, T2, mach_field, cmap='hot', shading='auto')
plt.colorbar(im, ax=ax, label='Mach number')
ax.set_xlabel(r'$\theta_1$')
ax.set_ylabel(r'$\theta_2$')
ax.set_title(f'AKAMA-DIAKONOV: Mach field (max={mach_max:.3f})')

# Panel 2: Swampland c(tau)
ax = axes[0, 1]
valid_c = V_positive & (c_swamp_correct > 0)
ax.semilogy(tau_qt[valid_c], c_swamp_correct[valid_c], 'b-', linewidth=2, label=r'$c = M_{Pl}|\nabla V|/V$')
ax.semilogy(tau_qt[valid_c], c_species_correct[valid_c], 'r--', linewidth=2, label=r'$c_{sp} = \Lambda_{sp}|\nabla V|/V$')
ax.axhline(1.0, color='k', linestyle=':', label='Swampland bound c=1')
ax.axvline(tau_fold, color='green', linestyle='--', alpha=0.5, label=r'$\tau_{fold}$')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$c(\tau)$')
ax.set_title(f'SWAMPLAND: c_max={c_max:.2e}')
ax.legend(fontsize=8)
ax.set_xlim(tau_qt[0], tau_qt[-1])

# Panel 3: CC gap analysis
ax = axes[1, 0]
cc_categories = ['Naive\nM_KK^4', 'With |E_cond|\n(gravity)', 'With |E_cond|\n(Kerner)', 'Volovik\nDelta^4']
cc_values = [cc_gap_naive, cc_gap_gravity, cc_gap_kerner, np.log10(ratio_volovik)]
colors = ['gray', 'blue', 'orange', 'green']
bars = ax.bar(cc_categories, cc_values, color=colors, alpha=0.7, edgecolor='black')
ax.axhline(0, color='red', linewidth=2, linestyle='-', label=r'$\Lambda_{obs}$')
ax.set_ylabel(r'$\log_{10}(\rho / \Lambda_{obs})$')
ax.set_title('CONDENSATE-CC: Orders above observed CC')
ax.legend()

# Panel 4: WZW agreement
ax = axes[1, 1]
# Show Strutinsky decomposition
ax.plot(omega_bin_c, hist_osc / max(domega, 1e-10), 'b-', alpha=0.5, label='Raw DOS')
ax.plot(omega_bin_c, rho_strutinsky_smooth / max(domega, 1e-10), 'r-', linewidth=2, label='Smooth (Strutinsky)')
ax.fill_between(omega_bin_c, 0, rho_oscillating / max(domega, 1e-10),
                alpha=0.3, color='green', label=f'Shell (|E_sh/E_sm|={shell_fraction:.3f})')
ax.set_xlabel(r'$\omega$ (M_KK)')
ax.set_ylabel(r'$\rho(\omega)$')
ax.set_title(f'WZW-STRUTINSKY: Agreement={100*agreement_heat:.0f}% (heat kernel)')
ax.legend(fontsize=8)

plt.tight_layout()
plotfile = os.path.join(DATA_DIR, 's48_volovik_string.png')
plt.savefig(plotfile, dpi=150, bbox_inches='tight')
plt.close()
print(f"  Saved: {plotfile}")

print("\n" + "=" * 78)
print("DONE: s48_volovik_string.py")
print("=" * 78)
