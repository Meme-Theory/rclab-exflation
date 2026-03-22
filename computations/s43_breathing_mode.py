#!/usr/bin/env python3
"""
BREATHE-43: Breathing Mode of 32-Cell Tessellation
====================================================

Computes the giant monopole resonance (GMR) analog for the 32-cell SU(3) fabric.
The breathing mode is the uniform volume-scaling oscillation where all cells
expand/contract in phase, analogous to nuclear ISGMR.

Physical setup:
  - 32-cell tessellation of the SU(3) internal fiber (S41 phononic crystal)
  - Each cell parameterized by Jensen deformation tau
  - Breathing mode: tau -> alpha * tau_fold uniformly across all cells
  - alpha = 1 is equilibrium (fold point tau = 0.190)

Energy contributions:
  E_total(alpha) = S_spectral(alpha * tau_fold) + E_BCS(alpha) + E_gradient(alpha)

  where:
    S_spectral = spectral action (monotonically increasing, RESTORING for compression)
    E_BCS = BCS condensation energy (NEGATIVE, depends on DOS and gap)
    E_gradient = (1/2)*Z*(nabla tau)^2 -- for UNIFORM scaling, nabla tau = 0
                 within cells; contributes only through surface terms

Incompressibility:
  K_total = tau_fold^2 * d^2 E_total / d(alpha)^2 |_{alpha=1}

Breathing frequency:
  omega_breathe = sqrt(K_total / M_ATDHFB) / R_cell

Pre-registered gate BREATHE-43: INFO.
  If K_BCS < 0 and |K_BCS| > K_spectral, report ANOMALOUS.

Author: Quantum Acoustics Theorist (Session 43)
Date: 2026-03-14
"""

import numpy as np
from numpy.linalg import eigvalsh
from scipy.interpolate import CubicSpline
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sys
import os
import time

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
from tier1_dirac_spectrum import (
    su3_generators,
    compute_structure_constants,
    compute_killing_form,
    jensen_metric,
    orthonormal_frame,
    frame_structure_constants,
    connection_coefficients,
    validate_connection,
    build_cliff8,
    validate_clifford,
    spinor_connection_offset,
    get_irrep,
    validate_irrep,
    dirac_operator_on_irrep,
    _irrep_cache,
)
from canonical_constants import tau_fold as TAU_FOLD

# ===========================================================================
# CONFIGURATION
# ===========================================================================

# Uniform scale factors for the breathing mode
ALPHA_VALUES = np.array([0.90, 0.93, 0.95, 0.97, 0.98, 0.99,
                         1.00,
                         1.01, 1.02, 1.03, 1.05, 1.07, 1.10])

# Corresponding tau values: tau = alpha * tau_fold
TAU_BREATHE = ALPHA_VALUES * TAU_FOLD

# BCS parameters from prior sessions
G_MOD = 5.0  # Coupling constant from S40
N_CELLS = 32  # Tessellation cell count (S41)

# Sectors through KK level 3 (same as s36)
KK_LEVELS = {
    0: [(0, 0)],
    1: [(1, 0), (0, 1)],
    2: [(1, 1), (2, 0), (0, 2)],
    3: [(3, 0), (0, 3), (2, 1), (1, 2)],
}

ALL_SECTORS = []
for level in sorted(KK_LEVELS.keys()):
    ALL_SECTORS.extend(KK_LEVELS[level])

def dim_pq(p, q):
    return (p + 1) * (q + 1) * (p + q + 2) // 2

def mult_pq(p, q):
    return dim_pq(p, q) ** 2


# ===========================================================================
# STEP 0: LOAD PRIOR DATA
# ===========================================================================

print("=" * 70)
print("BREATHE-43: Breathing Mode of 32-Cell Tessellation")
print("=" * 70)

t_start = time.time()

# Load spectral action data
d36 = np.load(os.path.join(os.path.dirname(os.path.abspath(__file__)),
              's36_sfull_tau_stabilization.npz'), allow_pickle=True)
tau_s36 = d36['tau_combined']
S_full_s36 = d36['S_full']

# Load gradient stiffness data
d42 = np.load(os.path.join(os.path.dirname(os.path.abspath(__file__)),
              's42_gradient_stiffness.npz'), allow_pickle=True)
Z_fold = float(np.asarray(d42['Z_fold']).flat[0])
d2S_fold_stored = float(np.asarray(d42['d2S_fold']).flat[0])
M_ATDHFB_stored = float(np.asarray(d42['M_ATDHFB']).flat[0])

# Load BCS / instanton data
d38 = np.load(os.path.join(os.path.dirname(os.path.abspath(__file__)),
              's38_cc_instanton.npz'), allow_pickle=True)
Delta_0 = float(np.asarray(d38['Delta_0']).flat[0])
a_GL = float(np.asarray(d38['a_GL']).flat[0])
b_GL = float(np.asarray(d38['b_GL']).flat[0])
xi_fold_modes = d38['xi_fold']  # [B1, B2, B3] gap-edge eigenvalues
mult_k = d38['mult_k']         # [1, 4, 3] multiplicities

# Load collective inertia data
d40 = np.load(os.path.join(os.path.dirname(os.path.abspath(__file__)),
              's40_collective_inertia.npz'), allow_pickle=True)
M_ATDHFB = float(np.asarray(d40['M_ATDHFB_TOTAL']).flat[0])
eps_fold = d40['eps_fold']      # single-particle energies at fold
Delta_fold = d40['Delta_fold']  # BCS gaps at fold
E_fold = d40['E_fold']          # quasiparticle energies at fold
u_fold = d40['u_fold']
v_fold = d40['v_fold']
d2S_fold_s40 = float(np.asarray(d40['d2S_fold']).flat[0])
d2e1_fold = float(np.asarray(d40['d2e1_fold']).flat[0])

# Load V_matrix information
d36m = np.load(os.path.join(os.path.dirname(os.path.abspath(__file__)),
               's36_mmax_authoritative.npz'), allow_pickle=True)
V_B2B2_diag = float(np.asarray(d36m['V_B2B2_diag_mean']).flat[0])
rho_B2_smooth = float(np.asarray(d36m['rho_B2_smooth']).flat[0])

print(f"\nInput data loaded:")
print(f"  tau_fold = {TAU_FOLD}")
print(f"  M_ATDHFB = {M_ATDHFB:.6f}")
print(f"  Z_fold = {Z_fold:.2f}")
print(f"  d2S/dtau2 (fold, s42) = {d2S_fold_stored:.2f}")
print(f"  d2S/dtau2 (fold, s40) = {d2S_fold_s40:.2f}")
print(f"  Delta_0 (GL) = {Delta_0:.6f}")
print(f"  a_GL = {a_GL:.6f}")
print(f"  b_GL = {b_GL:.6f}")
print(f"  V_B2B2_diag = {V_B2B2_diag:.6f}")
print(f"  rho_B2_smooth = {rho_B2_smooth:.4f}")
print(f"  eps_fold = {eps_fold}")
print(f"  Delta_fold = {Delta_fold}")
print(f"  E_fold = {E_fold}")
print(f"  N_cells = {N_CELLS}")


# ===========================================================================
# STEP 1: SPECTRAL ACTION AT SCALED TAU VALUES
# ===========================================================================
#
# S_spectral(alpha) = S_full(alpha * tau_fold)
#
# We need S_full at tau values that may not be on the existing grid.
# Strategy: recompute eigenvalues at each alpha * tau_fold, exactly as s36 does.
# ===========================================================================

print("\n" + "=" * 70)
print("STEP 1: SPECTRAL ACTION S_full(alpha * tau_fold)")
print("=" * 70)

# Infrastructure (tau-independent)
gens = su3_generators()
f_abc = compute_structure_constants(gens)
B_ab = compute_killing_form(f_abc)
gammas = build_cliff8()
cliff_err = validate_clifford(gammas)
print(f"\nClifford algebra error: {cliff_err:.2e}")
assert cliff_err < 1e-14

# Compute S_full at each breathing-mode tau value
S_spectral_alpha = np.zeros(len(ALPHA_VALUES))
singlet_evals_at_alpha = {}  # Store (0,0) sector eigenvalues for BCS

for ai, alpha in enumerate(ALPHA_VALUES):
    tau = alpha * TAU_FOLD
    print(f"\n--- alpha = {alpha:.3f}, tau = {tau:.4f} ---")
    t_tau = time.time()

    g_s = jensen_metric(B_ab, tau)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E)
    Gamma_conn = connection_coefficients(ft)
    conn_err = validate_connection(Gamma_conn)

    Omega = spinor_connection_offset(Gamma_conn, gammas)
    _irrep_cache.clear()

    S_total = 0.0
    for p, q in ALL_SECTORS:
        d_rho = dim_pq(p, q)
        m = mult_pq(p, q)

        rho, dim_r = get_irrep(p, q, gens, f_abc)
        assert dim_r == d_rho

        D_pi = dirac_operator_on_irrep(rho, E, gammas, Omega)
        ah_err = np.max(np.abs(D_pi + D_pi.conj().T))
        assert ah_err < 1e-12

        iD = 1j * D_pi
        evals = eigvalsh(iD)
        S_sector = np.sum(np.abs(evals))
        S_total += m * S_sector

        # Store singlet eigenvalues for BCS computation
        if p == 0 and q == 0:
            singlet_evals_at_alpha[alpha] = np.sort(np.abs(evals))

    S_spectral_alpha[ai] = S_total
    print(f"  S_full = {S_total:.4f}  [{time.time()-t_tau:.1f}s]")

# Verify against stored value at alpha=1
idx_alpha1 = np.argmin(np.abs(ALPHA_VALUES - 1.0))
print(f"\nCross-check: S_full(alpha=1) = {S_spectral_alpha[idx_alpha1]:.4f}")
S_fold_stored = float(np.asarray(d36['S_fold']).flat[0])
print(f"  Stored S_fold = {S_fold_stored:.4f}")
print(f"  Discrepancy = {abs(S_spectral_alpha[idx_alpha1] - S_fold_stored):.6f}")


# ===========================================================================
# STEP 2: BCS CONDENSATION ENERGY AT SCALED TAU
# ===========================================================================
#
# The BCS condensation energy depends on the single-particle spectrum through
# the density of states at the Fermi level and the BCS gap.
#
# At the fold, the 8 gap-edge modes have:
#   B2 (mult=4): eps = 0.8452, Delta = 2.062
#   B1 (mult=1): eps = 0.8191, Delta = 0.789
#   B3 (mult=3): eps = 0.9782, Delta = 0.176
#
# Under uniform scaling tau -> alpha * tau_fold, the eigenvalues scale as:
#   eps_k(alpha) = eigenvalue from the Dirac spectrum at alpha * tau_fold
#
# The BCS energy per mode pair is:
#   E_BCS = sum_k [ eps_k - E_k + Delta_k^2/(4*E_k) ]   (negative)
#         = sum_k [ eps_k - sqrt(eps_k^2 + Delta_k^2) + Delta_k^2/(4*E_k) ]
#
# For the mean-field BCS, the condensation energy is:
#   E_cond = -sum_k (Delta_k^2 * v_k^2) / (2*E_k)
#          = -(1/2)*Delta^2 * rho(E_F) at weak coupling
#
# More precisely, using the GL functional:
#   F_GL(Delta) = a_GL * Delta^2 + b_GL * Delta^4
#   E_cond = F_GL(Delta_0) = a_GL * Delta_0^2 + b_GL * Delta_0^4
#
# The alpha-dependence enters through:
#   (1) The DOS rho(E_F) at the Fermi level -> changes a_GL
#   (2) The single-particle energies eps_k -> changes BCS gap solution
# ===========================================================================

print("\n" + "=" * 70)
print("STEP 2: BCS CONDENSATION ENERGY E_BCS(alpha)")
print("=" * 70)

# Approach: Compute BCS gap equation at each alpha value
# using the singlet-sector eigenvalues.
#
# The singlet (0,0) has 16 eigenvalues: 8 positive, 8 negative (paired by PH).
# The 8 positive eigenvalues are the single-particle energies.
# BCS gap equation: 1/G = sum_k 1/(2*E_k) where E_k = sqrt(eps_k^2 + Delta^2)
# with uniform gap approximation (Delta_k = Delta for modes near E_F).

def solve_bcs_gap(eps_positive, G, tol=1e-12, max_iter=500):
    """Solve the BCS gap equation for uniform gap Delta.

    Gap equation: 1/G = sum_k 1/(2*sqrt(eps_k^2 + Delta^2))

    Parameters:
        eps_positive: array of positive single-particle energies
        G: pairing interaction strength (dimensionless, includes DOS)

    Returns:
        Delta: BCS gap (0 if no solution)
        E_cond: condensation energy
        u_k, v_k: BdG coherence factors
    """
    n_modes = len(eps_positive)

    # Check if pairing instability exists
    # Thouless criterion: M = G * sum_k 1/(2*eps_k) > 1
    M_thouless = G * np.sum(1.0 / (2.0 * eps_positive))
    if M_thouless <= 1.0:
        return 0.0, 0.0, np.ones(n_modes), np.zeros(n_modes), M_thouless

    # Solve iteratively (bisection on Delta)
    Delta_min = 1e-15
    Delta_max = 10.0 * np.max(eps_positive)

    def gap_residual(Delta):
        E_k = np.sqrt(eps_positive**2 + Delta**2)
        return G * np.sum(1.0 / (2.0 * E_k)) - 1.0

    # Bisection
    for _ in range(200):
        Delta_mid = 0.5 * (Delta_min + Delta_max)
        if gap_residual(Delta_mid) > 0:
            Delta_min = Delta_mid
        else:
            Delta_max = Delta_mid
        if Delta_max - Delta_min < tol * Delta_mid:
            break

    Delta = 0.5 * (Delta_min + Delta_max)
    E_k = np.sqrt(eps_positive**2 + Delta**2)
    v_k2 = 0.5 * (1.0 - eps_positive / E_k)
    u_k2 = 0.5 * (1.0 + eps_positive / E_k)
    u_k = np.sqrt(u_k2)
    v_k = np.sqrt(v_k2)

    # BCS condensation energy:
    # E_cond = 2*sum_k [eps_k*v_k^2 - E_k*u_k*v_k] + Delta^2/G
    # (the factor of 2 for time-reversal partners is already in the gap eq)
    #
    # Standard BCS result:
    # E_cond = sum_k [eps_k - E_k + Delta^2/(2*E_k)] - Delta^2/G
    #        = sum_k [eps_k - E_k] + Delta^2 * [sum_k 1/(2*E_k) - 1/G]
    #        = sum_k [eps_k - E_k]   (by the gap equation, the second term = 0)
    #
    # Wait -- that's not right. The standard formula:
    # E_BCS = 2*sum_k (eps_k * v_k^2) - G * (sum_k u_k*v_k)^2
    #       = 2*sum_k eps_k * v_k^2 - Delta^2/G
    # E_normal = 0 (all levels below Fermi occupied)
    # But here mu = 0 (forced by PH symmetry), so E_normal = 0
    # E_cond = E_BCS - E_normal = sum_k [2*eps_k*v_k^2] - Delta^2/G

    E_cond = np.sum(2.0 * eps_positive * v_k2) - Delta**2 / G

    return Delta, E_cond, u_k, v_k, M_thouless


# The pairing interaction G includes the DOS factor.
# From prior sessions: G_mod = 5.0 is the dimensionless coupling
# G = G_mod / N_modes where N_modes is the number of active modes
# Actually, from the s40 computation: G_mod = 5.0 is used directly
# in the BCS gap equation as the coupling constant.
#
# The gap equation at fold gives Delta ~ 2.06 for B2 modes,
# which is achieved with G_mod = 5.0 and 8 gap-edge modes.

# Compute BCS at each alpha
E_BCS_alpha = np.zeros(len(ALPHA_VALUES))
Delta_BCS_alpha = np.zeros(len(ALPHA_VALUES))
M_thouless_alpha = np.zeros(len(ALPHA_VALUES))

for ai, alpha in enumerate(ALPHA_VALUES):
    # Get positive eigenvalues from singlet sector
    evals = singlet_evals_at_alpha[alpha]  # already sorted |lambda|
    eps_pos = evals[evals > 0]  # positive eigenvalues

    # Solve BCS gap equation
    Delta, E_cond, u_k, v_k, M_th = solve_bcs_gap(eps_pos, G_MOD)

    E_BCS_alpha[ai] = E_cond
    Delta_BCS_alpha[ai] = Delta
    M_thouless_alpha[ai] = M_th

    print(f"  alpha={alpha:.3f}: Delta={Delta:.6f}, E_cond={E_cond:.6f}, "
          f"M_th={M_th:.4f}")

# Cross-check at alpha = 1
print(f"\nCross-check at alpha=1:")
print(f"  Delta = {Delta_BCS_alpha[idx_alpha1]:.6f}")
print(f"  E_cond = {E_BCS_alpha[idx_alpha1]:.6f}")
print(f"  Stored Delta_fold(B2) = {Delta_fold[0]:.6f}")


# ===========================================================================
# STEP 3: GRADIENT ENERGY CONTRIBUTION
# ===========================================================================
#
# For uniform breathing (all cells scale identically), nabla tau = 0
# WITHIN each cell. The gradient energy is purely from inter-cell
# boundaries.
#
# E_gradient(alpha) = N_cells * (1/2) * Z(alpha*tau_fold) * |grad tau|^2_boundary
#
# For uniform scaling, grad tau = 0 everywhere. The gradient stiffness
# Z contributes only if there are spatial variations (non-breathing modes).
# For the pure breathing mode, E_gradient = 0.
#
# However, Z(tau) itself depends on alpha through the metric, which
# affects the kinetic energy of the field. In the effective potential
# formulation, Z enters the mass/inertia, not the potential.
# ===========================================================================

print("\n" + "=" * 70)
print("STEP 3: GRADIENT ENERGY CONTRIBUTION")
print("=" * 70)

print(f"\nFor UNIFORM breathing mode (all cells scale identically):")
print(f"  nabla tau = 0 within each cell")
print(f"  Inter-cell gradient = 0 (all cells at same tau)")
print(f"  E_gradient(alpha) = 0 for the breathing mode")
print(f"  Z(tau) enters through the KINETIC ENERGY (mass), not potential")
print(f"  Z_fold = {Z_fold:.2f}")


# ===========================================================================
# STEP 4: TOTAL ENERGY AND INCOMPRESSIBILITY
# ===========================================================================

print("\n" + "=" * 70)
print("STEP 4: TOTAL ENERGY AND INCOMPRESSIBILITY")
print("=" * 70)

# Total energy per cell
# S_spectral is the spectral action (per unit volume of SU(3))
# E_BCS is the condensation energy (per set of 8 gap-edge modes)
# For the 32-cell tessellation, each cell contributes independently

E_total_alpha = S_spectral_alpha + E_BCS_alpha

print(f"\n{'alpha':>7} {'tau':>8} {'S_spec':>14} {'E_BCS':>12} "
      f"{'E_total':>14} {'Delta':>10} {'M_th':>8}")
print("-" * 80)
for ai, alpha in enumerate(ALPHA_VALUES):
    tau = alpha * TAU_FOLD
    print(f"{alpha:7.3f} {tau:8.4f} {S_spectral_alpha[ai]:14.4f} "
          f"{E_BCS_alpha[ai]:12.6f} {E_total_alpha[ai]:14.4f} "
          f"{Delta_BCS_alpha[ai]:10.6f} {M_thouless_alpha[ai]:8.4f}")

# Compute d^2 E / d(alpha)^2 using finite differences
# We use the alpha grid directly. Note d/d(alpha) = tau_fold * d/d(tau)

# Cubic spline interpolation for smooth derivatives
cs_Espec = CubicSpline(ALPHA_VALUES, S_spectral_alpha)
cs_EBCS = CubicSpline(ALPHA_VALUES, E_BCS_alpha)
cs_Etotal = CubicSpline(ALPHA_VALUES, E_total_alpha)

# Second derivatives at alpha = 1
K_spectral = float(cs_Espec(1.0, 2))  # d^2 S_spec / d(alpha)^2
K_BCS = float(cs_EBCS(1.0, 2))        # d^2 E_BCS / d(alpha)^2
K_total = float(cs_Etotal(1.0, 2))     # d^2 E_total / d(alpha)^2

# Also compute first derivatives (should be nonzero since fold is not minimum)
dE_spec_dalpha = float(cs_Espec(1.0, 1))
dE_BCS_dalpha = float(cs_EBCS(1.0, 1))
dE_total_dalpha = float(cs_Etotal(1.0, 1))

print(f"\n{'DERIVATIVE ANALYSIS AT alpha = 1':}")
print(f"  dS_spec/d(alpha)  = {dE_spec_dalpha:.4f}")
print(f"  dE_BCS/d(alpha)   = {dE_BCS_dalpha:.6f}")
print(f"  dE_total/d(alpha) = {dE_total_dalpha:.4f}")
print()
print(f"  K_spectral = d^2 S_spec / d(alpha)^2 = {K_spectral:.4f}")
print(f"  K_BCS      = d^2 E_BCS  / d(alpha)^2 = {K_BCS:.6f}")
print(f"  K_total    = d^2 E_total/ d(alpha)^2 = {K_total:.4f}")
print()

# Cross-check: K_spectral should equal tau_fold^2 * d2S/dtau2
K_spectral_check = TAU_FOLD**2 * d2S_fold_stored
print(f"  Cross-check: tau_fold^2 * d2S/dtau2 = {K_spectral_check:.4f}")
print(f"  Ratio K_spectral / (tau_fold^2 * d2S_dtau2) = "
      f"{K_spectral / K_spectral_check:.6f}")

# Sign analysis
print(f"\n{'SIGN ANALYSIS':}")
print(f"  K_spectral = {K_spectral:.4f} ({'POSITIVE (restoring)' if K_spectral > 0 else 'NEGATIVE (unstable)'})")
print(f"  K_BCS      = {K_BCS:.6f} ({'POSITIVE (restoring)' if K_BCS > 0 else 'NEGATIVE (softening)'})")
print(f"  K_total    = {K_total:.4f} ({'POSITIVE (stable breathing)' if K_total > 0 else 'NEGATIVE (ANOMALOUS)'})")
print(f"  |K_BCS/K_spectral| = {abs(K_BCS/K_spectral):.6e}")


# ===========================================================================
# STEP 5: NUCLEAR-STYLE INCOMPRESSIBILITY
# ===========================================================================

print("\n" + "=" * 70)
print("STEP 5: NUCLEAR-STYLE INCOMPRESSIBILITY")
print("=" * 70)

# Nuclear incompressibility: K_A = 9 * <r^2> * d^2(E/A)/d(r^2)
# or equivalently K_A = alpha^2 * d^2(E/A)/d(alpha)^2 at alpha=1
#
# In nuclear physics: K_inf ~ 230 MeV (nuclear matter)
# Here we compute K_breathe in M_KK units

# The nuclear analogy:
# alpha = R/R_0 (radius scaling)
# For the internal space: alpha = tau / tau_fold (deformation scaling)
# K_nuclear = 9 * d^2(E/A) / d(alpha)^2 at alpha = 1
#
# For the fabric: E/A = E_total / N_cells
# K_fabric = 9 * d^2(E_total/N_cells) / d(alpha)^2

K_fabric_per_cell = K_total / N_CELLS
K_nuclear_analog = 9.0 * K_fabric_per_cell  # factor of 9 from nuclear convention

print(f"\n  K_total (all cells) = {K_total:.4f} M_KK^2")
print(f"  K_per_cell = K_total/N_cells = {K_fabric_per_cell:.4f} M_KK^2")
print(f"  K_nuclear_analog = 9 * K_per_cell = {K_nuclear_analog:.4f} M_KK^2")
print(f"  Nuclear K_inf ~ 230 MeV for reference")

# BCS softening ratio
if K_BCS != 0:
    softening_ratio = K_BCS / K_spectral
    print(f"\n  BCS softening ratio K_BCS/K_spectral = {softening_ratio:.6e}")
    if softening_ratio < 0:
        print(f"  BCS SOFTENS the breathing mode by "
              f"{abs(softening_ratio)*100:.4f}%")
    else:
        print(f"  BCS STIFFENS the breathing mode (unexpected)")


# ===========================================================================
# STEP 6: BREATHING MODE FREQUENCY
# ===========================================================================

print("\n" + "=" * 70)
print("STEP 6: BREATHING MODE FREQUENCY")
print("=" * 70)

# omega_breathe^2 = K_total / (M_eff * R_cell^2)
#
# M_eff = M_ATDHFB is the cranking mass (collective inertia)
# R_cell = characteristic cell size in the tessellation
#
# For the 32-cell tessellation of SU(3):
# Vol(SU(3)) = 1349.74 (Haar measure, from s42)
# Vol(cell) = Vol(SU(3)) / N_cells
# R_cell = Vol(cell)^{1/8} (8-dimensional internal space)

Vol_SU3 = float(np.asarray(d42['Vol_SU3_Haar']).flat[0])
Vol_cell = Vol_SU3 / N_CELLS
R_cell = Vol_cell**(1.0/8.0)  # 8 = dim(SU(3))

print(f"\n  Vol(SU(3)) = {Vol_SU3:.4f}")
print(f"  Vol(cell) = Vol/N_cells = {Vol_cell:.4f}")
print(f"  R_cell = Vol_cell^(1/8) = {R_cell:.6f} (in M_KK^{-1} units)")
print(f"  M_ATDHFB = {M_ATDHFB:.6f}")

if K_total > 0:
    # Standard breathing mode
    omega_breathe_sq = K_total / (M_ATDHFB * R_cell**2)
    omega_breathe = np.sqrt(omega_breathe_sq)

    # Also compute without R_cell factor (pure tau-space frequency)
    omega_tau = np.sqrt(K_total / M_ATDHFB)

    print(f"\n  omega_breathe^2 = K_total / (M_ATDHFB * R_cell^2)")
    print(f"                  = {K_total:.4f} / ({M_ATDHFB:.6f} * {R_cell:.6f}^2)")
    print(f"                  = {omega_breathe_sq:.4f}")
    print(f"  omega_breathe = {omega_breathe:.4f} M_KK")
    print(f"\n  omega_tau (tau-space) = sqrt(K_total/M_ATDHFB)")
    print(f"                       = {omega_tau:.4f} M_KK")

    # Compare to other energy scales
    print(f"\n  omega_breathe / Delta_B2 = {omega_breathe / Delta_fold[0]:.4f}")
    print(f"  omega_breathe / omega_SA_fold = {omega_breathe / float(np.asarray(d40['omega_SA_fold']).flat[0]):.6f}")
    print(f"  omega_breathe / omega_BCS_fold = {omega_breathe / float(np.asarray(d40['omega_BCS_fold']).flat[0]):.6f}")
    print(f"  omega_breathe / omega_B2_QRPA = {omega_breathe / 3.245:.4f}")

    # Nuclear GMR comparison: omega_GMR ~ 80/A^{1/3} MeV
    # For A=32: omega_GMR ~ 80/32^{1/3} ~ 25 MeV
    A_eff = N_CELLS
    omega_GMR_nuclear = 80.0 / A_eff**(1.0/3.0)
    print(f"\n  Nuclear GMR comparison:")
    print(f"    omega_GMR(A={A_eff}) ~ {omega_GMR_nuclear:.1f} MeV")
    print(f"    omega_breathe / omega_GMR = dimensionless (different units)")
else:
    print(f"\n  K_total < 0 => BREATHING MODE IS UNSTABLE")
    print(f"  |K_total| = {abs(K_total):.4f}")
    print(f"  Imaginary frequency: omega = i * {np.sqrt(abs(K_total)/M_ATDHFB):.4f}")
    omega_breathe = 0.0
    omega_tau = 0.0


# ===========================================================================
# STEP 7: COMPARISON OF ENERGY SCALES
# ===========================================================================

print("\n" + "=" * 70)
print("STEP 7: ENERGY SCALE HIERARCHY")
print("=" * 70)

print(f"\n  K_spectral          = {K_spectral:.4f}   (spectral action curvature)")
print(f"  K_BCS               = {K_BCS:.6f}   (BCS curvature)")
print(f"  |K_BCS/K_spectral|  = {abs(K_BCS/K_spectral):.6e}")
print(f"  S_fold              = {S_spectral_alpha[idx_alpha1]:.4f}")
print(f"  E_BCS(fold)         = {E_BCS_alpha[idx_alpha1]:.6f}")
print(f"  |E_BCS/S_fold|      = {abs(E_BCS_alpha[idx_alpha1]/S_spectral_alpha[idx_alpha1]):.6e}")

# The key ratio: is BCS energy a perturbation on the spectral action?
print(f"\n  EXTENSIVITY CHECK:")
print(f"    S_spectral involves {sum(mult_pq(p,q) for p,q in ALL_SECTORS)} "
      f"modes (L0-L3)")
print(f"    E_BCS involves 8 gap-edge modes")
print(f"    Ratio 8/{sum(mult_pq(p,q) for p,q in ALL_SECTORS)} = "
      f"{8/sum(mult_pq(p,q) for p,q in ALL_SECTORS):.6f}")
print(f"    BCS is a {abs(E_BCS_alpha[idx_alpha1]/S_spectral_alpha[idx_alpha1])*100:.6f}% "
      f"correction to S_full")


# ===========================================================================
# STEP 8: FINITE-DIFFERENCE VERIFICATION
# ===========================================================================

print("\n" + "=" * 70)
print("STEP 8: FINITE-DIFFERENCE CROSS-CHECK")
print("=" * 70)

# Use 3-point and 5-point stencils to verify the spline derivatives
# 3-point centered: f''(x) ~ [f(x+h) - 2f(x) + f(x-h)] / h^2

# Find closest alpha values to 1.0 for stencils
h_vals = [0.01, 0.02, 0.03, 0.05]
print(f"\n  Finite-difference d^2 E / d(alpha)^2 at alpha=1:")

for h in h_vals:
    # Find the alpha values nearest to 1-h, 1, 1+h
    idx_m = np.argmin(np.abs(ALPHA_VALUES - (1.0 - h)))
    idx_0 = np.argmin(np.abs(ALPHA_VALUES - 1.0))
    idx_p = np.argmin(np.abs(ALPHA_VALUES - (1.0 + h)))

    alpha_m = ALPHA_VALUES[idx_m]
    alpha_0 = ALPHA_VALUES[idx_0]
    alpha_p = ALPHA_VALUES[idx_p]

    # Only use if we have exactly the right spacing
    if (abs(alpha_m - (1.0 - h)) < 1e-6 and
        abs(alpha_0 - 1.0) < 1e-6 and
        abs(alpha_p - (1.0 + h)) < 1e-6):

        d2E_fd_spec = (S_spectral_alpha[idx_p] - 2*S_spectral_alpha[idx_0] +
                       S_spectral_alpha[idx_m]) / h**2
        d2E_fd_bcs = (E_BCS_alpha[idx_p] - 2*E_BCS_alpha[idx_0] +
                      E_BCS_alpha[idx_m]) / h**2
        d2E_fd_total = (E_total_alpha[idx_p] - 2*E_total_alpha[idx_0] +
                        E_total_alpha[idx_m]) / h**2

        print(f"  h={h:.2f}: K_spec={d2E_fd_spec:.4f} "
              f"K_BCS={d2E_fd_bcs:.6f} K_total={d2E_fd_total:.4f}")
    else:
        print(f"  h={h:.2f}: exact grid points not available (skipped)")

print(f"\n  Spline values: K_spec={K_spectral:.4f} "
      f"K_BCS={K_BCS:.6f} K_total={K_total:.4f}")


# ===========================================================================
# GATE VERDICT
# ===========================================================================

print("\n" + "=" * 70)
print("GATE VERDICT: BREATHE-43")
print("=" * 70)

is_anomalous = (K_BCS < 0) and (abs(K_BCS) > K_spectral)

if is_anomalous:
    verdict = "ANOMALOUS"
    print(f"\n  K_BCS = {K_BCS:.6f} (NEGATIVE)")
    print(f"  |K_BCS| = {abs(K_BCS):.6f} > K_spectral = {K_spectral:.4f}")
    print(f"  BCS softening EXCEEDS spectral stiffness!")
    print(f"  BREATHING MODE IS UNSTABLE (K_total < 0)")
    print(f"\n  >>> BREATHE-43: ANOMALOUS <<<")
elif K_BCS < 0:
    verdict = "INFO: BCS SOFTENS"
    print(f"\n  K_BCS = {K_BCS:.6f} (NEGATIVE = BCS softening)")
    print(f"  |K_BCS| = {abs(K_BCS):.6f} << K_spectral = {K_spectral:.4f}")
    print(f"  BCS softening is a {abs(K_BCS/K_spectral)*100:.4f}% perturbation")
    print(f"  BREATHING MODE IS STABLE (K_total > 0)")
    if K_total > 0:
        print(f"  omega_breathe = {omega_breathe:.4f} M_KK")
    print(f"\n  >>> BREATHE-43: INFO (BCS softens but does not destabilize) <<<")
else:
    verdict = "INFO: ALL STIFFENING"
    print(f"\n  K_BCS = {K_BCS:.6f} (POSITIVE = BCS also stiffens)")
    print(f"  K_spectral = {K_spectral:.4f}")
    print(f"  BOTH contributions are restoring forces")
    print(f"  BREATHING MODE IS STABLE (K_total > 0)")
    if K_total > 0:
        print(f"  omega_breathe = {omega_breathe:.4f} M_KK")
    print(f"\n  >>> BREATHE-43: INFO (stable, no anomalous softening) <<<")


# ===========================================================================
# PLOT
# ===========================================================================

fig, axes = plt.subplots(2, 3, figsize=(18, 11))

# Panel 1: S_spectral(alpha)
ax = axes[0, 0]
alpha_fine = np.linspace(ALPHA_VALUES[0], ALPHA_VALUES[-1], 500)
ax.plot(alpha_fine, cs_Espec(alpha_fine), 'b-', linewidth=2, label='Spline')
ax.plot(ALPHA_VALUES, S_spectral_alpha, 'ko', markersize=6, label='Computed')
ax.axvline(x=1.0, color='red', linestyle='--', alpha=0.7, label='alpha=1 (fold)')
ax.set_xlabel('alpha (scale factor)', fontsize=11)
ax.set_ylabel('S_spectral', fontsize=11)
ax.set_title('Spectral Action vs Breathing Scale', fontsize=12)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel 2: E_BCS(alpha)
ax = axes[0, 1]
ax.plot(alpha_fine, cs_EBCS(alpha_fine), 'r-', linewidth=2, label='Spline')
ax.plot(ALPHA_VALUES, E_BCS_alpha, 'ko', markersize=6, label='Computed')
ax.axvline(x=1.0, color='red', linestyle='--', alpha=0.7)
ax.axhline(y=0, color='gray', linestyle='-', linewidth=0.5)
ax.set_xlabel('alpha', fontsize=11)
ax.set_ylabel('E_BCS', fontsize=11)
ax.set_title('BCS Condensation Energy vs Breathing Scale', fontsize=12)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel 3: Delta(alpha)
ax = axes[0, 2]
cs_Delta = CubicSpline(ALPHA_VALUES, Delta_BCS_alpha)
ax.plot(alpha_fine, cs_Delta(alpha_fine), 'g-', linewidth=2, label='Spline')
ax.plot(ALPHA_VALUES, Delta_BCS_alpha, 'ko', markersize=6, label='Computed')
ax.axvline(x=1.0, color='red', linestyle='--', alpha=0.7)
ax.set_xlabel('alpha', fontsize=11)
ax.set_ylabel('Delta (BCS gap)', fontsize=11)
ax.set_title('BCS Gap vs Breathing Scale', fontsize=12)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel 4: E_total(alpha) with breakdown
ax = axes[1, 0]
ax.plot(alpha_fine, cs_Etotal(alpha_fine), 'k-', linewidth=2.5, label='E_total')
ax.plot(alpha_fine, cs_Espec(alpha_fine), 'b--', linewidth=1.5, label='S_spectral')
# Scale E_BCS for visibility
E_BCS_scale = abs(S_spectral_alpha[idx_alpha1]) / max(abs(E_BCS_alpha.min()),
              abs(E_BCS_alpha.max())) * 0.05
ax.plot(ALPHA_VALUES, E_total_alpha, 'ko', markersize=5)
ax.axvline(x=1.0, color='red', linestyle='--', alpha=0.7)
ax.set_xlabel('alpha', fontsize=11)
ax.set_ylabel('Energy', fontsize=11)
ax.set_title('Total Energy (S_spec dominates)', fontsize=12)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel 5: Second derivatives (curvature)
ax = axes[1, 1]
d2_spec = cs_Espec(alpha_fine, 2)
d2_bcs = cs_EBCS(alpha_fine, 2)
d2_total = cs_Etotal(alpha_fine, 2)
ax.plot(alpha_fine, d2_spec, 'b-', linewidth=2, label=f'K_spec ({K_spectral:.1f})')
ax.plot(alpha_fine, d2_bcs * abs(K_spectral/K_BCS) if K_BCS != 0 else d2_bcs,
        'r-', linewidth=2,
        label=f'K_BCS x{abs(K_spectral/K_BCS):.0f} ({K_BCS:.4f})')
ax.axvline(x=1.0, color='red', linestyle='--', alpha=0.7)
ax.axhline(y=0, color='gray', linestyle='-', linewidth=0.5)
ax.set_xlabel('alpha', fontsize=11)
ax.set_ylabel('d^2E/d(alpha)^2', fontsize=11)
ax.set_title('Incompressibility Components', fontsize=12)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel 6: Summary text
ax = axes[1, 2]
ax.axis('off')
summary_text = (
    f"BREATHE-43: Breathing Mode Summary\n"
    f"{'='*40}\n\n"
    f"K_spectral = {K_spectral:.2f}\n"
    f"K_BCS      = {K_BCS:.4f}\n"
    f"|K_BCS/K_spec| = {abs(K_BCS/K_spectral):.2e}\n"
    f"K_total    = {K_total:.2f}\n\n"
    f"M_ATDHFB   = {M_ATDHFB:.4f}\n"
    f"R_cell     = {R_cell:.4f}\n\n"
)
if K_total > 0:
    summary_text += (
        f"omega_breathe = {omega_breathe:.4f} M_KK\n"
        f"omega_tau     = {omega_tau:.4f} M_KK\n\n"
        f"omega/Delta_B2 = {omega_breathe/Delta_fold[0]:.4f}\n"
        f"omega/omega_QRPA = {omega_breathe/3.245:.4f}\n\n"
        f"N_cells = {N_CELLS}\n"
        f"K_per_cell = {K_fabric_per_cell:.2f}\n\n"
        f"Verdict: {verdict}\n"
    )
else:
    summary_text += (
        f"UNSTABLE: K_total < 0\n"
        f"omega = imaginary\n\n"
        f"Verdict: {verdict}\n"
    )
ax.text(0.05, 0.95, summary_text, transform=ax.transAxes,
        fontsize=10, verticalalignment='top', fontfamily='monospace',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

plt.suptitle(f'BREATHE-43: Giant Monopole Resonance of 32-Cell Fabric -- {verdict}',
             fontsize=14, fontweight='bold')
plt.tight_layout()

outpath_png = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           's43_breathing_mode.png')
plt.savefig(outpath_png, dpi=150, bbox_inches='tight')
print(f"\nPlot saved: {outpath_png}")


# ===========================================================================
# SAVE DATA
# ===========================================================================

save_data = {
    # Grid
    'alpha_values': ALPHA_VALUES,
    'tau_breathe': TAU_BREATHE,
    'tau_fold': TAU_FOLD,
    'N_cells': N_CELLS,

    # Spectral action
    'S_spectral_alpha': S_spectral_alpha,

    # BCS
    'E_BCS_alpha': E_BCS_alpha,
    'Delta_BCS_alpha': Delta_BCS_alpha,
    'M_thouless_alpha': M_thouless_alpha,
    'G_mod': G_MOD,

    # Total energy
    'E_total_alpha': E_total_alpha,

    # Incompressibility
    'K_spectral': K_spectral,
    'K_BCS': K_BCS,
    'K_total': K_total,
    'K_fabric_per_cell': K_fabric_per_cell,
    'K_nuclear_analog': K_nuclear_analog,

    # First derivatives
    'dE_spec_dalpha': dE_spec_dalpha,
    'dE_BCS_dalpha': dE_BCS_dalpha,
    'dE_total_dalpha': dE_total_dalpha,

    # Breathing frequency
    'M_ATDHFB': M_ATDHFB,
    'R_cell': R_cell,
    'Vol_cell': Vol_cell,
    'omega_breathe': omega_breathe if K_total > 0 else 0.0,
    'omega_tau': omega_tau if K_total > 0 else 0.0,

    # Verdict
    'verdict': verdict,
    'is_anomalous': is_anomalous,
}

outpath_npz = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           's43_breathing_mode.npz')
np.savez(outpath_npz, **save_data)
print(f"Data saved: {outpath_npz}")


# ===========================================================================
# FINAL SUMMARY
# ===========================================================================

print("\n" + "=" * 70)
print("FINAL SUMMARY: BREATHE-43")
print("=" * 70)

print(f"""
COMPUTATION: Breathing mode of 32-cell SU(3) tessellation
  - Uniform scale factor alpha applied to tau_fold = {TAU_FOLD}
  - 13 alpha values from {ALPHA_VALUES[0]} to {ALPHA_VALUES[-1]}
  - Full Dirac spectrum recomputed at each alpha (11 sectors, L0-L3)
  - BCS gap equation solved at each alpha (8 gap-edge modes, G={G_MOD})

ENERGY LANDSCAPE:
  S_spectral(1) = {S_spectral_alpha[idx_alpha1]:.4f} (dominates)
  E_BCS(1)      = {E_BCS_alpha[idx_alpha1]:.6f} (tiny correction)
  |E_BCS/S|     = {abs(E_BCS_alpha[idx_alpha1]/S_spectral_alpha[idx_alpha1]):.2e}

INCOMPRESSIBILITY:
  K_spectral = {K_spectral:.4f}  ({'+' if K_spectral > 0 else '-'}restoring)
  K_BCS      = {K_BCS:.6f}  ({'+' if K_BCS >= 0 else '-'}{'stiffening' if K_BCS >= 0 else 'softening'})
  K_total    = {K_total:.4f}
  |K_BCS/K_spectral| = {abs(K_BCS/K_spectral):.2e}

BREATHING FREQUENCY:
  {'omega_breathe = ' + f'{omega_breathe:.4f} M_KK' if K_total > 0 else 'UNSTABLE (K_total < 0)'}
  {'omega_tau     = ' + f'{omega_tau:.4f} M_KK' if K_total > 0 else ''}

NUCLEAR GMR COMPARISON:
  K_per_cell = {K_fabric_per_cell:.4f}
  K_nuclear_analog (9*K/A) = {K_nuclear_analog:.4f}
  Nuclear K ~ 230 MeV (for reference, different units)

GATE VERDICT: BREATHE-43 = {verdict}
  BCS contributes {abs(K_BCS/K_spectral)*100:.6f}% of spectral curvature
  Breathing mode is {'STABLE' if K_total > 0 else 'UNSTABLE'}
  Extensivity dominance: spectral action ({sum(mult_pq(p,q) for p,q in ALL_SECTORS)} modes) >> BCS (8 modes)
""")

t_total = time.time() - t_start
print(f"Total runtime: {t_total:.1f}s")
