"""
Session 34a QA: The 11% Hunt -- Acoustic Perspective on Missing Pairing Strength
=================================================================================
M_max = 0.902 vs threshold 1.0. Shortfall = 11%.

This script systematically quantifies six acoustic enhancement mechanisms that
could close the gap, treating the domain wall in tau-space as an acoustic cavity
boundary. Each mechanism is computed independently with explicit assumptions.

ESTABLISHED FACTS (from s34a_dphys_thouless.py and s34a_tesla_validation.py):
  - V(B2,B2) max off-diag = 0.057 in spinor eigenbasis (CONFIRMED, basis-invariant to 0.094)
  - V(B1,B2) = 0.080 (uniform across all 4 B2 modes)
  - Wall 2 rho_full = 8.81 per B2 mode (with multi-sector 1.046x and impedance 1.56x)
  - B2 eigenvalues: 0.8453 (4-fold degenerate at tau=0.20)
  - B1 eigenvalue:  0.8191 (singlet)
  - Shell gap B2-B1 = 0.0261
  - M_max = V * rho / (2|xi|) where xi = lambda - mu, mu=0
  - Tesla optimization: best achievable V in any U(4) basis = 0.094 (still M_max = 0.90)

SIX MECHANISMS TESTED:
  1. Van Hove regularized peak DOS
  2. Fabry-Perot resonance (standing waves in tau-cavity)
  3. Evanescent coupling between neighboring walls
  4. Chemical potential shift
  5. BCS self-energy feedback (bootstrap)
  6. Negative-sector contribution (particle-hole coupling across spectral gap)

Author: qa (quantum-acoustics-theorist), Session 34a
Date: 2026-03-06
"""

import os
import sys
import time
import numpy as np
from scipy.linalg import eigh
from scipy.optimize import brentq, minimize_scalar
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
t0 = time.time()

# ======================================================================
#  Load all prerequisite data
# ======================================================================

print("=" * 78)
print("Session 34a QA: The 11% Hunt -- Acoustic Perspective")
print("=" * 78)

kosmann = np.load(os.path.join(SCRIPT_DIR, 's23a_kosmann_singlet.npz'),
                  allow_pickle=True)
wall_dos = np.load(os.path.join(SCRIPT_DIR, 's32b_wall_dos.npz'),
                   allow_pickle=True)
sector = np.load(os.path.join(SCRIPT_DIR, 's33a_landau_sector.npz'),
                 allow_pickle=True)
trap33b = np.load(os.path.join(SCRIPT_DIR, 's33b_trap1_wall_bcs.npz'),
                  allow_pickle=True)
tesla = np.load(os.path.join(SCRIPT_DIR, 's34a_tesla_validation.npz'),
                allow_pickle=True)
thouless_data = np.load(os.path.join(SCRIPT_DIR, 's34a_dphys_thouless.npz'),
                        allow_pickle=True)

print(f"Data loaded in {time.time()-t0:.1f}s\n")

# ======================================================================
#  Extract fundamental numbers
# ======================================================================

TAU_VALUES = np.array([0.0, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.50])
ti = 3  # tau = 0.20

evals_raw = kosmann[f'eigenvalues_{ti}']
evecs_raw = kosmann[f'eigenvectors_{ti}']
si = np.argsort(evals_raw)
evals_s = evals_raw[si]
evecs_s = evecs_raw[:, si]

pos_idx = np.where(evals_s > 0)[0]
pos_ev = evals_s[pos_idx]

# Branch eigenvalues
lambda_B1 = pos_ev[0]         # 0.8191
lambda_B2 = pos_ev[1]         # 0.8453 (4-fold degenerate)
lambda_B3 = pos_ev[5]         # 0.9782 (3-fold degenerate)
gap_B2_B1 = lambda_B2 - lambda_B1   # 0.0261
gap_B3_B2 = lambda_B3 - lambda_B2   # 0.1330

B1_idx = pos_idx[0:1]
B2_idx = pos_idx[1:5]
B3_idx = pos_idx[5:8]

# Build spinor V from K_a matrices
V_16 = np.zeros((16, 16))
for a in range(8):
    K = kosmann[f'K_a_matrix_{ti}_{a}']
    V_16 += np.abs(K)**2

V_B2B2 = V_16[np.ix_(B2_idx, B2_idx)]
V_B2B2_offdiag = V_B2B2.copy()
np.fill_diagonal(V_B2B2_offdiag, 0)
V_B2B2_max = np.max(V_B2B2_offdiag)  # 0.057

V_B1B2 = V_16[np.ix_(B1_idx, B2_idx)]  # shape (1,4)
V_B3B2 = V_16[np.ix_(B3_idx, B2_idx)]  # shape (3,4)
V_B1B1 = V_16[B1_idx[0], B1_idx[0]]     # Should be 0 (Trap 1)

# Wall 2 data (best wall)
W2_TAU_1 = float(wall_dos['wall_2_tau_1'])  # 0.15
W2_TAU_2 = float(wall_dos['wall_2_tau_2'])  # 0.25
W2_RHO_ALL = float(wall_dos['wall_2_rho_wall_all'])  # 21.60
W2_RHO_PER_MODE = W2_RHO_ALL / 4.0  # 5.40

IMPEDANCE_FACTOR = 1.56
MS_FACTOR = float(thouless_data['multi_sector_factor'])  # 1.046
RHO_FULL = W2_RHO_PER_MODE * MS_FACTOR * IMPEDANCE_FACTOR  # 8.81

# Current M_max
M_MAX_CURRENT = float(thouless_data['own_baseline_M_max'])  # 0.902

# Tesla-optimized V
V_OPT_MAX = float(tesla['V_B2B2_opt_max_offdiag'])  # 0.094

# ETA regulator
ETA_REG = 0.001

print("ESTABLISHED NUMBERS:")
print(f"  lambda_B1 = {lambda_B1:.6f}")
print(f"  lambda_B2 = {lambda_B2:.6f} (4-fold degenerate)")
print(f"  lambda_B3 = {lambda_B3:.6f} (3-fold degenerate)")
print(f"  gap B2-B1 = {gap_B2_B1:.6f}")
print(f"  gap B3-B2 = {gap_B3_B2:.6f}")
print(f"  V(B2,B2) max off-diag (eigh)  = {V_B2B2_max:.6f}")
print(f"  V(B2,B2) max off-diag (optim) = {V_OPT_MAX:.6f}")
print(f"  V(B1,B2) = {V_B1B2[0,0]:.6f} (uniform)")
print(f"  V(B1,B1) = {V_B1B1:.2e} (Trap 1 = exact zero)")
print(f"  Wall 2 rho_per_mode = {W2_RHO_PER_MODE:.4f}")
print(f"  Wall 2 rho_full = {RHO_FULL:.4f}")
print(f"  M_max (current) = {M_MAX_CURRENT:.6f}")
print(f"  Shortfall = {1.0/M_MAX_CURRENT:.4f}x ({(1.0/M_MAX_CURRENT - 1)*100:.1f}%)")
print()


# ======================================================================
#  UTILITY: Thouless criterion evaluation
# ======================================================================

def compute_M_max_5x5(V_sub, E_sub, mu, rho_vec, eta_reg=0.001):
    """Compute M_max from 5x5 Thouless matrix.

    Args:
        V_sub: (5,5) pairing kernel [B2_0,...,B2_3, B1]
        E_sub: (5,) eigenvalues
        mu: chemical potential
        rho_vec: (5,) DOS per mode
        eta_reg: regulator fraction

    Returns:
        M_max, M_eigenvalues
    """
    xi = E_sub - mu
    lam_min = np.min(np.abs(E_sub))
    eta = max(eta_reg * lam_min, 1e-15)
    abs_xi = np.maximum(np.abs(xi), eta)

    M = np.zeros((5, 5))
    for m in range(5):
        M[:, m] = V_sub[:, m] * rho_vec[m] / (2.0 * abs_xi[m])

    M_evals = np.linalg.eigvals(M)
    return np.max(np.real(M_evals)), M_evals


def build_reference_5x5():
    """Build the reference 5x5 V, E, rho from current data."""
    # V in spinor eigenspinor basis
    idx_5 = np.concatenate([B2_idx, B1_idx])
    V_sub = V_16[np.ix_(idx_5, idx_5)]
    E_sub = evals_s[idx_5]
    rho = np.array([RHO_FULL] * 4 + [1.0])
    return V_sub, E_sub, rho


# Cross-check: reproduce M_max = 0.902
V_ref, E_ref, rho_ref = build_reference_5x5()
M_check, _ = compute_M_max_5x5(V_ref, E_ref, 0.0, rho_ref)
print(f"CROSS-CHECK: M_max = {M_check:.6f} (should be {M_MAX_CURRENT:.6f})")
assert abs(M_check - M_MAX_CURRENT) < 0.001, \
    f"Cross-check FAILED: {M_check} vs {M_MAX_CURRENT}"
print(f"  PASS\n")


# ======================================================================
#  MECHANISM 1: Van Hove Regularized Peak DOS
# ======================================================================

print("=" * 78)
print("MECHANISM 1: Van Hove Regularized Peak DOS at Fold")
print("=" * 78)
print()

# The B2 fold at tau ~ 0.190 is an A_2 catastrophe (fold catastrophe).
# Near the fold minimum, the eigenvalue behaves as:
#   lambda(tau) ~ lambda_min + (1/2) d2 * (tau - tau_min)^2
#
# The 1D DOS per mode goes as:
#   rho(E) = 1 / |d lambda/d tau| = 1 / (d2 * |tau - tau_min|)
#         = 1 / sqrt(2 * d2 * (E - E_min))
#
# This gives a van Hove divergence rho ~ 1/sqrt(E - E_min).
# The divergence is regularized by two effects:
#   (a) The wall has finite width w_wall ~ tau_2 - tau_1 = 0.10
#   (b) B2 splitting under inner fluctuations (0.021 at phi=gap)
#
# The REGULARIZED peak DOS is:
#   rho_peak = 1 / sqrt(d2 * w_min)
# where w_min = max(splitting, 1/(2*pi*rho_wall)) is the effective
# resolution in tau-space.
#
# From s32b_wall_dos.py: the wall computation uses a GROUP VELOCITY
# v_B2 = 0.059 at Wall 2. The DOS per mode rho_per_mode = 1/(pi*v) = 5.40.
# This is the MEAN DOS across the wall, not the PEAK.
#
# For a fold with d2 = 1.176 (bare) or 1.226 (D_phys), the peak DOS at
# the fold is HIGHER than the mean. Let's compute both.

# d2 at fold from eigenvalue flow
# Using data at tau = 0.15, 0.20, 0.25 (centered difference)
B2_means = []
for t in range(len(TAU_VALUES)):
    ev = kosmann[f'eigenvalues_{t}']
    pos = np.sort(ev[ev > 0])
    B2_means.append(np.mean(pos[1:5]))

B2_means = np.array(B2_means)

# Central difference at tau=0.20 (index 3)
dtau = TAU_VALUES[4] - TAU_VALUES[2]  # 0.25 - 0.15 = 0.10
d2_B2 = (B2_means[4] - 2*B2_means[3] + B2_means[2]) / (dtau/2)**2
v_B2_at_fold = abs(B2_means[4] - B2_means[2]) / dtau  # first derivative ~ 0

# The fold minimum is near tau=0.190 (DPHYS-34a-1).
# At the fold center, d lambda/d tau = 0, so v_group = 0 exactly.
# The wall integral of 1/v over a finite wall width gives the total DOS.

# For a parabolic fold: lambda(tau) = lambda_min + (d2/2)(tau-tau_0)^2
# Wall from tau_1 to tau_2, fold center at tau_0.
# Integrated DOS = integral_{tau_1}^{tau_2} (1/pi) * 1/|d lambda/d tau| d tau
#                = integral (1/pi) * 1/(d2 * |tau - tau_0|) d tau
#                = (1/(pi*d2)) * [ln|tau-tau_0|]_{tau_1}^{tau_2}
# This DIVERGES logarithmically at the fold center.
# Must regularize: replace |tau - tau_0| by sqrt((tau-tau_0)^2 + delta^2)
# where delta is an effective broadening from B2 splitting or wall thickness.

# Physical regularization: the fold is NOT a mathematical point. It has
# structure on scale delta ~ splitting/d2 ~ 0.021/1.2 ~ 0.018 in tau.
# Also, the modulus field has fluctuations: delta_tau ~ sqrt(T/K) where K
# is the modulus stiffness and T is the effective temperature.
# For zero-temperature BCS, the dominant regularization is the B2 splitting.

tau_0 = 0.190  # Fold center
delta_tau = 0.018  # Regularization from B2 splitting

# Compute regularized integrated DOS per B2 mode across Wall 2
def van_hove_integrated_dos(tau_1, tau_2, tau_0, d2, delta, n_pts=10000):
    """Compute the van Hove regularized DOS integral.

    rho_int = (1/pi) integral_{tau_1}^{tau_2} 1/sqrt((d2*(tau-tau_0))^2 + delta^2) d tau
    """
    tau_grid = np.linspace(tau_1, tau_2, n_pts)
    v_grid = np.sqrt((d2 * (tau_grid - tau_0))**2 + delta**2)
    rho_grid = 1.0 / (np.pi * v_grid)
    return np.trapezoid(rho_grid, tau_grid), rho_grid, tau_grid

# Mean group velocity method (what W-32b uses):
v_B2_wall = float(wall_dos['wall_2_B2_0_v_wall'])  # 0.059

rho_vh_mean = 1.0 / (np.pi * v_B2_wall)
print(f"  Mean group velocity v_B2 = {v_B2_wall:.6f}")
print(f"  Mean DOS per mode = 1/(pi*v) = {rho_vh_mean:.4f}")

# Van Hove regularized integral
d2_fold = d2_B2
print(f"  d2(B2) at fold = {d2_fold:.6f}")

# Test multiple regularization scales
for delta_test in [0.001, 0.005, 0.010, 0.018, 0.030, 0.050]:
    rho_int, _, _ = van_hove_integrated_dos(W2_TAU_1, W2_TAU_2, tau_0, d2_fold, delta_test)
    ratio = rho_int / rho_vh_mean
    print(f"  delta={delta_test:.3f}: rho_int = {rho_int:.4f}, "
          f"ratio to mean = {ratio:.4f}")

# Use the physically motivated regularization
rho_vh, rho_grid, tau_grid = van_hove_integrated_dos(
    W2_TAU_1, W2_TAU_2, tau_0, d2_fold, delta_tau)
vh_ratio = rho_vh / rho_vh_mean

# Compute M_max with enhanced DOS
rho_vh_full = rho_vh * MS_FACTOR * IMPEDANCE_FACTOR
rho_vec_vh = np.array([rho_vh_full] * 4 + [1.0])
M_max_vh, _ = compute_M_max_5x5(V_ref, E_ref, 0.0, rho_vec_vh)

print(f"\n  Van Hove regularized DOS (delta={delta_tau:.3f}):")
print(f"    rho_per_mode = {rho_vh:.4f} (mean method: {W2_RHO_PER_MODE:.4f})")
print(f"    Enhancement = {vh_ratio:.4f}x")
print(f"    rho_full = {rho_vh_full:.4f} (current: {RHO_FULL:.4f})")
print(f"    M_max = {M_max_vh:.6f}")
print(f"    Verdict: {'CLOSES GAP' if M_max_vh > 1.0 else 'INSUFFICIENT'}")
print()


# ======================================================================
#  MECHANISM 2: Fabry-Perot Resonance (Standing Waves in Tau-Cavity)
# ======================================================================

print("=" * 78)
print("MECHANISM 2: Fabry-Perot Resonance in Tau-Cavity")
print("=" * 78)
print()

# The domain wall is a region in tau-space where the modulus field tau(x)
# changes rapidly. From the acoustic perspective, this is a cavity with
# impedance mismatch at the boundaries.
#
# In a 1D Fabry-Perot cavity, the transmitted intensity is enhanced by
# a factor Q ~ (1-R^2)^{-1} at resonance, where R is the reflection
# coefficient at each boundary.
#
# The "impedance" in tau-space is related to the spectral action curvature:
# Z(tau) ~ d2S/dtau^2. Different tau values give different Z, creating
# impedance mismatch at the wall boundaries.
#
# For B2 modes: the "wavelength" in tau-space is:
#   lambda_tau ~ 2*pi / k_tau
# where k_tau is determined by the modulus equation of motion.
# At the fold (tau~0.19), v_group = 0 and k -> infinity, so the mode
# is EVANESCENT beyond the fold. This is like total internal reflection.
#
# BUT: the fold is INSIDE the wall for Wall 2 (0.15 to 0.25).
# The mode can propagate on both sides but with v -> 0 at the fold.
# This creates a RESONANCE: the mode bounces back and forth between
# the fold and the wall edge, accumulating spectral weight.

# The Q factor of a Fabry-Perot cavity with one perfect mirror (R=1)
# and one partial mirror (R<1) is:
#   Q = pi * L / (lambda * (1-R))
# where L is the cavity length.

# For our system:
# - L ~ half the wall width = (tau_2 - tau_1)/2 = 0.05
# - The fold acts as a near-perfect mirror (R_fold ~ 1)
# - The wall edge has R = 0.36 (from CT-4 impedance analysis)

R_fold = 1.0  # Fold acts as perfect mirror (v=0)
R_edge = 0.36  # From impedance analysis (CT-4)
L_cavity = (W2_TAU_2 - W2_TAU_1) / 2.0  # Half-wall = 0.05

# Effective cavity round-trip phase: 2*k*L
# At resonance: 2*k*L = n*pi
# For the fundamental: k_res = pi/(2*L) = pi/0.10 = 31.4
# "Wavelength" in tau: lambda_tau = 2*pi/k_res = 0.20

# The Q of the cavity:
# Q = pi * sqrt(R_fold * R_edge) / (1 - R_fold * R_edge)
# With R_fold = 1: Q diverges. So we must use a finite R_fold.
# The fold reflection is not perfect because the fold has finite curvature.
# R_fold ~ 1 - 2*delta/L where delta is the fold width.

delta_fold = delta_tau  # 0.018
R_fold_eff = 1.0 - 2.0 * delta_fold / L_cavity  # ~ 0.64

Q_cavity = np.pi * np.sqrt(R_fold_eff * R_edge) / (1.0 - R_fold_eff * R_edge)

print(f"  Cavity parameters:")
print(f"    L (half-wall) = {L_cavity:.4f}")
print(f"    R_fold (effective) = {R_fold_eff:.4f}")
print(f"    R_edge = {R_edge:.4f}")
print(f"    Q = {Q_cavity:.4f}")
print()

# The DOS enhancement from a Fabry-Perot cavity at resonance:
# rho_FP = rho_mean * Q / (pi * n_modes)
# where n_modes is the number of resonances in the bandwidth.
# For a single resonance (fundamental): rho_FP = rho_mean * Q
# This is an UPPER BOUND; the actual enhancement depends on whether
# the B2 modes are at resonance.

# But the Fabry-Perot model assumes PROPAGATING modes. B2 has v -> 0
# at the fold, so it's not a clean propagating mode. The resonance
# picture is better described as a TRAPPED mode -- which is what
# Mechanism 1 already captures via the van Hove singularity.

# The Fabry-Perot model does however capture the IMPEDANCE MISMATCH
# effect at the wall EDGES, which the van Hove integral does not.
# The impedance correction factor is already included as
# IMPEDANCE_FACTOR = 1.56. Can we do better?

# More careful impedance analysis:
# Z_in = Z_bulk * (Z_wall + Z_bulk * tanh(gamma*L)) / (Z_bulk + Z_wall * tanh(gamma*L))
# For a lossy cavity with attenuation constant gamma.

# The key question: is the impedance factor 1.56 already optimal?
# Let's check what Z ratio gives R = 0.36.
# R = (Z2 - Z1) / (Z2 + Z1) => |R|^2 = 0.36
# |R| = 0.6 => Z2/Z1 = (1+|R|)/(1-|R|) = 4.0

Z_ratio = (1 + np.sqrt(R_edge)) / (1 - np.sqrt(R_edge))
print(f"  Impedance ratio Z_wall/Z_bulk = {Z_ratio:.4f}")
print(f"  Current impedance factor = {IMPEDANCE_FACTOR:.4f}")
print(f"  Fabry-Perot Q enhancement = {Q_cavity:.4f}")

# The impedance factor 1/(1-R) = 1/(1-0.36) = 1.5625 is for a single
# boundary. For a cavity with two boundaries (fold + edge), the
# effective enhancement is:
# At resonance: 1/(1-R1*R2)
cavity_enhancement = 1.0 / (1.0 - R_fold_eff * R_edge)

print(f"  Cavity resonance enhancement = {cavity_enhancement:.4f}")
print(f"  vs current impedance factor = {IMPEDANCE_FACTOR:.4f}")

# Replace impedance factor with cavity enhancement
rho_fp_full = W2_RHO_PER_MODE * MS_FACTOR * cavity_enhancement
rho_vec_fp = np.array([rho_fp_full] * 4 + [1.0])
M_max_fp, _ = compute_M_max_5x5(V_ref, E_ref, 0.0, rho_vec_fp)

print(f"\n  Fabry-Perot corrected M_max:")
print(f"    rho_full = {rho_fp_full:.4f} (current: {RHO_FULL:.4f})")
print(f"    M_max = {M_max_fp:.6f}")
print(f"    Verdict: {'CLOSES GAP' if M_max_fp > 1.0 else 'INSUFFICIENT'}")
print()


# ======================================================================
#  MECHANISM 3: Evanescent Coupling Between Neighboring Walls
# ======================================================================

print("=" * 78)
print("MECHANISM 3: Evanescent Coupling Between Domain Walls")
print("=" * 78)
print()

# If the modulus field tau(x) forms a pattern of domain walls (Turing pattern),
# the typical spacing between walls is L_wall ~ 2*pi/k_Turing.
#
# Evanescent modes from one wall can tunnel to a neighboring wall if
# L_wall is comparable to the evanescent decay length:
#   xi_ev = 1 / Im(k) ~ v_B2 / (gap_B3_B2)  at energies in the gap
#
# For B2 modes between walls, the evanescent wavefunction goes as:
#   psi ~ exp(-x/xi_ev)
# and the coupling between two walls separated by L is:
#   t ~ exp(-L/xi_ev)
#
# This coupling creates BONDING and ANTI-BONDING states, splitting the
# B2 levels and potentially pushing modes closer to the Fermi surface.
# However, this mechanism DOES NOT increase the pairing kernel V;
# it only modifies |xi| in the denominator.

# In our system, "evanescent" means the B2 mode cannot propagate in
# tau-space beyond the fold region. Between two fold regions (two domain
# walls), the mode amplitude decays exponentially.

# Decay length in tau-space:
v_B2_bulk = abs(B2_means[1] - B2_means[0]) / (TAU_VALUES[1] - TAU_VALUES[0])
# This is the B2 group velocity FAR from the fold

# Evanescent decay: Im(k) ~ sqrt(d2) for modes below the fold
# The decay length xi_ev = 1/sqrt(d2_fold) ~ 1/sqrt(1.2) ~ 0.91
# This means evanescent modes extend ~0.91 in tau, much larger than
# any realistic wall spacing.

xi_ev = 1.0 / np.sqrt(abs(d2_fold)) if abs(d2_fold) > 0 else float('inf')
print(f"  Evanescent decay length: xi_ev = 1/sqrt(d2) = {xi_ev:.4f}")
print(f"  Wall width = {W2_TAU_2 - W2_TAU_1:.4f}")
print(f"  Ratio xi_ev / wall_width = {xi_ev / (W2_TAU_2 - W2_TAU_1):.4f}")
print()

# For realistic wall spacings (from Turing pattern analysis):
# The pattern wavelength depends on the modulus equation of motion.
# Typical spacing: L_spacing ~ 5-10 * wall_width ~ 0.5-1.0

# The coupling between walls: t ~ exp(-L/xi_ev)
print("  Tunnel coupling between walls:")
for L_spacing in [0.1, 0.2, 0.5, 1.0, 2.0]:
    t_tunnel = np.exp(-L_spacing / xi_ev)
    print(f"    L={L_spacing:.1f}: |t| = {t_tunnel:.6f}")

# The evanescent coupling shifts eigenvalues by +/- t, creating
# a band of width 2*t around the B2 level. This affects |xi| in the
# Thouless denominator. For the NEAREST states to the Fermi surface:
# xi_eff = xi - t (bonding state moves closer)

# With xi = lambda_B2 = 0.845 and t ~ 0.5 (for L = 0.2):
t_typical = np.exp(-0.2 / xi_ev)
xi_eff_bonding = lambda_B2 - t_typical

print(f"\n  Evanescent coupling at L=0.2:")
print(f"    Tunnel coupling t = {t_typical:.6f}")
print(f"    xi_eff (bonding) = {xi_eff_bonding:.6f} (bare xi = {lambda_B2:.6f})")

# This mechanism is ENORMOUS -- but it's also wrong for this system.
# The "evanescent coupling" here means the B2 mode has large amplitude
# across the wall, not between walls. The fold curvature d2 ~ 1.2 is
# a SMOOTH variation, not a gap-induced exponential decay.
# The actual evanescent effect is captured by Mechanism 1 (van Hove).

# What WOULD help: if there are multiple fold regions (domain walls)
# and the B2 modes hybridize between them, creating a TIGHT-BINDING BAND.
# The bandwidth W_TB ~ 4*t would give additional states near the Fermi surface.
# But this requires multiple walls in the simulation volume, which is a
# separate question about the Turing pattern period.

# For the SINGLE-WALL analysis, evanescent coupling does not add new states.
print(f"\n  Verdict: Evanescent coupling is subsumed by Mechanism 1 for single wall.")
print(f"           Multi-wall tight-binding could contribute if wall spacing < {xi_ev:.2f}")
print(f"           This requires further Turing pattern analysis. NOT COMPUTED HERE.")
M_max_ev = M_MAX_CURRENT  # No change for single wall
print()


# ======================================================================
#  MECHANISM 4: Chemical Potential Shift
# ======================================================================

print("=" * 78)
print("MECHANISM 4: Chemical Potential Shift")
print("=" * 78)
print()

# M_nm = V_nm * rho_m / (2|lambda_m - mu|)
# At mu = 0: |xi| = |lambda| for all modes.
# If mu > 0, we move mu toward the B2 eigenvalues, reducing |xi|.
# The B1 eigenvalue is at 0.8191, B2 at 0.8453.
# The gap edge (smallest |xi|) is at B1.
#
# V(B1,B1) = 0 exactly (Trap 1), so the B1 diagonal is dead.
# But V(B1,B2) = 0.080 is nonzero, so B1 DOES participate in the
# Thouless matrix through its off-diagonal coupling to B2.
#
# As mu increases:
# - |xi_B2| = lambda_B2 - mu decreases (good for B2 pairing)
# - |xi_B1| = lambda_B1 - mu decreases even faster (good for B1-B2 coupling)
# - But V(B1,B1) = 0, so the B1 self-pairing remains zero
# - At mu = lambda_B1, the B1 mode sits exactly at the Fermi surface,
#   and |xi_B1| -> 0 (regulated). This BOOSTS the B1-B2 coupling channel.

# Scan mu from 0 to lambda_B1
mu_scan = np.linspace(0, lambda_B1, 1001)
M_max_mu = []
mu_crit = None

for mu in mu_scan:
    M, _ = compute_M_max_5x5(V_ref, E_ref, mu, rho_ref)
    M_max_mu.append(M)
    if mu_crit is None and M > 1.0:
        mu_crit = mu

M_max_mu = np.array(M_max_mu)

# Find where M_max crosses 1.0
if mu_crit is not None:
    print(f"  mu_crit (M=1.0): {mu_crit:.6f}")
    print(f"  mu_crit / lambda_B1 = {mu_crit/lambda_B1:.4f}")
    print(f"  mu_crit / lambda_B2 = {mu_crit/lambda_B2:.4f}")
else:
    # M_max > 1 for all mu or never reaches 1
    if M_max_mu[0] > 1.0:
        print(f"  M_max > 1 at mu=0 already!")
        mu_crit = 0.0
    else:
        print(f"  M_max never reaches 1 in scanned range")
        print(f"  Max M_max = {np.max(M_max_mu):.6f} at mu = {mu_scan[np.argmax(M_max_mu)]:.6f}")
        mu_crit = mu_scan[np.argmax(M_max_mu)]

# What happens at mu near lambda_B1?
# The B1 mode has V(B1,B1) = 0, so even though |xi_B1| -> 0,
# the B1 DIAGONAL contribution to M is zero. Only the B1-B2
# off-diagonal benefits. Let's check explicitly.

print(f"\n  M_max vs mu (selected values):")
print(f"  {'mu':>10s} {'|xi_B1|':>10s} {'|xi_B2|':>10s} {'M_max':>10s}")
for mu_show in [0, 0.1, 0.2, 0.4, 0.6, 0.7, 0.75, 0.80, lambda_B1*0.99, lambda_B1]:
    idx = np.argmin(np.abs(mu_scan - mu_show))
    xi_b1 = abs(lambda_B1 - mu_scan[idx])
    xi_b2 = abs(lambda_B2 - mu_scan[idx])
    print(f"  {mu_scan[idx]:10.4f} {xi_b1:10.4f} {xi_b2:10.4f} {M_max_mu[idx]:10.6f}")

M_max_mu_best = np.max(M_max_mu)
mu_at_best = mu_scan[np.argmax(M_max_mu)]

print(f"\n  Best M_max over all mu = {M_max_mu_best:.6f} at mu = {mu_at_best:.6f}")
print(f"  Verdict: {'CLOSES GAP' if M_max_mu_best > 1.0 else 'INSUFFICIENT'}")
print()


# ======================================================================
#  MECHANISM 5: BCS Self-Energy Feedback (Bootstrap)
# ======================================================================

print("=" * 78)
print("MECHANISM 5: BCS Self-Energy Feedback (Bootstrap)")
print("=" * 78)
print()

# Near the Thouless instability (M_max -> 1), the BCS interaction modifies
# the quasiparticle spectrum through self-energy corrections. The self-energy
# is:
#   Sigma_n(omega) = sum_m V_nm * Delta_m / (omega^2 - E_m^2 - Delta_m^2)
#
# At the onset of instability (Delta -> 0+), the LEADING self-energy is:
#   Sigma_n ~ V_nn / (2|xi_n|)  (the Hartree-Fock shift)
#
# This shifts the quasiparticle energy: xi_eff_n = xi_n + Sigma_n
# If Sigma pushes eigenvalues TOWARD the Fermi surface (|xi_eff| < |xi|),
# the instability strengthens.
#
# For M_max = 0.902, we need an 11% boost. The self-consistent condition:
#   M_max_eff = V * rho / (2 * |xi - Sigma(Delta)|) > 1
# where Sigma(Delta) depends on Delta through the gap equation.
#
# At the ONSET (Delta=0): Sigma = 0 (no feedback), M_max = 0.902.
# The question: does the system have a FINITE-Delta solution?
#
# For M_max < 1, the linearized gap equation has no nonzero solution.
# But the FULL (nonlinear) gap equation:
#   Delta_n = sum_m V_nm * rho_m * Delta_m / (2 * sqrt(xi_m^2 + Delta_m^2))
# CAN have a nonzero solution even when M_max < 1, provided the nonlinearity
# in the denominator compensates.
#
# Let's check: for LARGE Delta, the denominator sqrt(xi^2 + Delta^2) -> Delta,
# and the gap equation becomes:
#   Delta_n = sum_m V_nm * rho_m / 2  (Delta cancels)
# This is a LINEAR equation for the Delta DIRECTION (not magnitude).
# It has a solution if sum_m V_nm * rho_m / 2 has eigenvalue > 1... but that
# matrix is DIFFERENT from the Thouless matrix (no 1/|xi| weighting).
#
# Actually, in the large-Delta limit:
#   Delta = V_eff @ (Delta / (2*Delta)) = V_eff / 2 @ ones
# This gives Delta = V_eff @ ones / 2, a fixed vector independent of Delta.
# The condition for a nonzero solution is simply that V_eff has positive entries,
# which it does. But the SELF-CONSISTENT Delta must satisfy:
#   Delta_n = sum_m V_nm * rho_m * Delta_m / (2 * sqrt(xi_m^2 + Delta_m^2))
# This equation always has Delta=0 as a solution. A nonzero solution exists
# only if the largest eigenvalue of the LINEARIZED operator exceeds 1
# (Thouless criterion). For M_max = 0.902 < 1, there is NO nonzero solution
# to the self-consistent gap equation.
#
# PROOF: the gap equation is a contraction mapping for M_max < 1.
# Define F(Delta) = V_eff @ g(Delta) where g_m(Delta) = Delta_m / (2*sqrt(xi_m^2 + Delta_m^2))
# Then ||g(Delta)|| <= ||Delta|| / (2*min|xi_m|)  [since sqrt(xi^2+D^2) >= |xi|]
# So ||F(Delta)|| <= ||V_eff|| * ||Delta|| / (2*min|xi|)
# The operator norm ||V_eff @ diag(rho/(2|xi|))|| = M_max = 0.902 < 1.
# Therefore F is a contraction: the ONLY fixed point is Delta=0.

M_bootstrap = M_MAX_CURRENT  # No change: linearized analysis is exact for M < 1

print("  The BCS gap equation Delta = V_eff * Delta / (2*sqrt(xi^2 + Delta^2))")
print(f"  has M_max = {M_MAX_CURRENT:.6f} < 1.")
print("  By the contraction mapping theorem, Delta = 0 is the UNIQUE fixed point.")
print("  There is no self-energy bootstrap: the instability either exists (M>1)")
print("  or it does not (M<1). No intermediate regime is possible in the mean-field BCS.")
print()
print("  NOTE: Beyond-mean-field fluctuation corrections (Gorkov, Nozieres-Schmitt-Rink)")
print("  could modify this conclusion. These involve Cooper pair fluctuations above T_c.")
print("  In condensed matter, fluctuation corrections to M_max are typically O(1/N)")
print("  where N is the number of modes in the pairing shell.")
print("  With N_eff = 4 (B2 modes), fluctuation corrections could be ~25%.")
print("  This is speculative and requires explicit computation of the Aslamazov-Larkin")
print("  and Maki-Thompson diagrams in the NCG setting.")
print()
print(f"  Verdict (mean-field): NO CHANGE. M_max = {M_bootstrap:.6f}")
print(f"  Verdict (fluctuation): POSSIBLY RELEVANT but uncomputed. Flag for S35.")
print()


# ======================================================================
#  MECHANISM 6: Negative-Sector Contribution (Full 16x16 Thouless)
# ======================================================================

print("=" * 78)
print("MECHANISM 6: Negative-Sector Contribution (Full Spectral Width)")
print("=" * 78)
print()

# All prior computations use only the POSITIVE eigenvalue sector (8 modes)
# or even just B1+B2 (5 modes). The FULL D_K spectrum has 16 modes:
# 8 negative eigenvalues (mirrors of the positive ones) and 8 positive.
#
# In a superconductor, BCS pairing involves BOTH particle and hole states:
# the pairing is between k and -k states. In the NCG spectral setting,
# the analog of particle-hole pairing is coupling between positive and
# negative eigenvalue sectors through the Kosmann operator K_a.
#
# Question: does V_nm have significant matrix elements coupling the
# positive and negative B2 sectors? If so, including these in the
# Thouless matrix could boost M_max.

# The spectrum is particle-hole symmetric: eigenvalues come in +/- pairs.
# The negative B2 modes have eigenvalues -0.8453 (4-fold degenerate).
# At mu = 0, |xi| = |lambda| for all modes, so positive and negative
# modes contribute equally.

# Check V coupling between positive and negative B2
neg_idx = np.where(evals_s < 0)[0]
neg_B2_idx = neg_idx[3:7]  # B2_neg (by symmetry with positive sector)

V_B2pos_B2neg = V_16[np.ix_(B2_idx, neg_B2_idx)]
V_B2pos_B2neg_max = np.max(V_B2pos_B2neg)

print(f"  V(B2+, B2-) max = {V_B2pos_B2neg_max:.6f}")
print(f"  V(B2+, B2-) matrix:")
print(f"  {V_B2pos_B2neg}")

# Full 16x16 Thouless
V_full_16 = V_16.copy()
rho_16 = np.ones(16)
# B2 modes (both positive and negative) get wall enhancement
for idx_set in [B2_idx, neg_B2_idx]:
    for i in idx_set:
        rho_16[i] = RHO_FULL

M_16 = np.zeros((16, 16))
xi_16 = evals_s - 0.0  # mu = 0
lam_min = np.min(np.abs(evals_s))
eta_16 = max(0.001 * lam_min, 1e-15)
abs_xi_16 = np.maximum(np.abs(xi_16), eta_16)

for m in range(16):
    M_16[:, m] = V_full_16[:, m] * rho_16[m] / (2.0 * abs_xi_16[m])

M_evals_16 = np.linalg.eigvals(M_16)
M_max_16 = np.max(np.real(M_evals_16))

print(f"\n  Full 16x16 Thouless (both sectors, wall-enhanced B2):")
print(f"    M_max(16x16) = {M_max_16:.6f}")
print(f"    M_max(5x5)   = {M_MAX_CURRENT:.6f}")
print(f"    Enhancement  = {M_max_16/M_MAX_CURRENT:.4f}x")

# Also try 10x10: all B1+B2 modes from both sectors
B1_neg_idx = neg_idx[7:8]  # B1_neg
idx_10 = np.concatenate([B2_idx, B1_idx, neg_B2_idx, B1_neg_idx])
V_10 = V_16[np.ix_(idx_10, idx_10)]
E_10 = evals_s[idx_10]

rho_10 = np.array([RHO_FULL]*4 + [1.0] + [RHO_FULL]*4 + [1.0])
M_max_10, _ = compute_M_max_5x5.__wrapped__(V_10, E_10, 0.0, rho_10, 0.001) \
    if hasattr(compute_M_max_5x5, '__wrapped__') else (0, None)

# Rewrite for 10x10
xi_10 = E_10 - 0.0
abs_xi_10 = np.maximum(np.abs(xi_10), eta_16)
M_10 = np.zeros((10, 10))
for m in range(10):
    M_10[:, m] = V_10[:, m] * rho_10[m] / (2.0 * abs_xi_10[m])
M_evals_10 = np.linalg.eigvals(M_10)
M_max_10 = np.max(np.real(M_evals_10))

print(f"\n  10x10 Thouless (B1+B2, both sectors):")
print(f"    M_max(10x10) = {M_max_10:.6f}")

# And 8x8: all positive modes (including B3)
idx_8 = pos_idx
V_8 = V_16[np.ix_(idx_8, idx_8)]
E_8 = evals_s[idx_8]
rho_8 = np.array([1.0] + [RHO_FULL]*4 + [1.0]*3)  # B1, B2x4, B3x3
xi_8 = E_8
abs_xi_8 = np.maximum(np.abs(xi_8), eta_16)
M_8 = np.zeros((8, 8))
for m in range(8):
    M_8[:, m] = V_8[:, m] * rho_8[m] / (2.0 * abs_xi_8[m])
M_evals_8 = np.linalg.eigvals(M_8)
M_max_8 = np.max(np.real(M_evals_8))

print(f"\n  8x8 Thouless (full positive sector, wall-enhanced B2):")
print(f"    M_max(8x8)   = {M_max_8:.6f}")

print(f"\n  Verdict: {'CLOSES GAP' if max(M_max_16, M_max_10, M_max_8) > 1.0 else 'INSUFFICIENT'}")
print()


# ======================================================================
#  COMBINED ANALYSIS: Stack all mechanisms
# ======================================================================

print("=" * 78)
print("COMBINED ANALYSIS: All Enhancement Mechanisms")
print("=" * 78)
print()

# Test combinations:
# A) Van Hove DOS + optimal basis
# B) Van Hove DOS + mu shift
# C) Van Hove DOS + full 16x16
# D) Van Hove DOS + mu shift + full 16x16

# (A) Van Hove + optimal basis
# Optimal basis has V_max = 0.094 but doesn't change M_max (Tesla showed this)
# M_max depends on the EIGENVALUE of the Thouless matrix, which Tesla optimized

# (B) Van Hove + mu shift
print("  (B) Van Hove DOS (delta=0.018) + mu optimization:")
M_max_vh_mu = []
for mu in mu_scan:
    M, _ = compute_M_max_5x5(V_ref, E_ref, mu, rho_vec_vh)
    M_max_vh_mu.append(M)
M_max_vh_mu = np.array(M_max_vh_mu)
M_best_vh_mu = np.max(M_max_vh_mu)
mu_best_vh_mu = mu_scan[np.argmax(M_max_vh_mu)]
print(f"    Best M_max = {M_best_vh_mu:.6f} at mu = {mu_best_vh_mu:.6f}")
print(f"    Verdict: {'CLOSES GAP' if M_best_vh_mu > 1.0 else 'INSUFFICIENT'}")

# (C) Van Hove + 16x16
rho_16_vh = np.ones(16)
for idx_set in [B2_idx, neg_B2_idx]:
    for i in idx_set:
        rho_16_vh[i] = rho_vh_full
M_16_vh = np.zeros((16, 16))
for m in range(16):
    M_16_vh[:, m] = V_full_16[:, m] * rho_16_vh[m] / (2.0 * abs_xi_16[m])
M_max_16_vh = np.max(np.real(np.linalg.eigvals(M_16_vh)))
print(f"\n  (C) Van Hove DOS + full 16x16:")
print(f"    M_max = {M_max_16_vh:.6f}")
print(f"    Verdict: {'CLOSES GAP' if M_max_16_vh > 1.0 else 'INSUFFICIENT'}")

# (D) Van Hove + mu + 16x16
M_max_all = []
for mu in mu_scan:
    xi_16_mu = evals_s - mu
    abs_xi_16_mu = np.maximum(np.abs(xi_16_mu), eta_16)
    M_temp = np.zeros((16, 16))
    for m in range(16):
        M_temp[:, m] = V_full_16[:, m] * rho_16_vh[m] / (2.0 * abs_xi_16_mu[m])
    M_max_all.append(np.max(np.real(np.linalg.eigvals(M_temp))))
M_max_all = np.array(M_max_all)
M_best_all = np.max(M_max_all)
mu_best_all = mu_scan[np.argmax(M_max_all)]
print(f"\n  (D) Van Hove + mu optimization + full 16x16:")
print(f"    Best M_max = {M_best_all:.6f} at mu = {mu_best_all:.6f}")
print(f"    Verdict: {'CLOSES GAP' if M_best_all > 1.0 else 'INSUFFICIENT'}")
print()

# ======================================================================
#  MINIMUM EXTERNAL INPUT NEEDED
# ======================================================================

print("=" * 78)
print("MINIMUM EXTERNAL INPUT TO CLOSE THE GAP")
print("=" * 78)
print()

# Method 1: What rho_full is needed for M_max = 1.0?
# M_max ~ V * rho / (2*xi) for the dominant channel
# Current: M_max = 0.902 at rho = 8.81
# Need: rho_needed = rho_current / M_max * 1.0 (approximate)
# M_max does NOT scale exactly linearly with rho_B2 because B1 has
# fixed rho=1. Use Brent root-finding for the exact threshold.
def _M_at_rho_scalar(rho_b2):
    return compute_M_max_5x5(V_ref, E_ref, 0.0,
                              np.array([rho_b2]*4 + [1.0]))[0]
rho_needed = brentq(lambda r: _M_at_rho_scalar(r) - 1.0, 5.0, 20.0)
rho_ratio_needed = rho_needed / RHO_FULL

print(f"  Method 1: rho enhancement needed")
print(f"    Current rho_full = {RHO_FULL:.4f}")
print(f"    Needed rho_full = {rho_needed:.4f}")
print(f"    Enhancement factor = {rho_ratio_needed:.4f}x ({(rho_ratio_needed-1)*100:.1f}%)")
print(f"    This translates to:")
print(f"      - Wall DOS per mode: {W2_RHO_PER_MODE:.4f} -> {W2_RHO_PER_MODE * rho_ratio_needed:.4f}")
print(f"      - OR impedance factor: {IMPEDANCE_FACTOR:.4f} -> {IMPEDANCE_FACTOR * rho_ratio_needed:.4f}")
print(f"      - OR multi-sector factor: {MS_FACTOR:.4f} -> {MS_FACTOR * rho_ratio_needed:.4f}")

# Verify linearity
rho_verify = rho_needed
M_verify, _ = compute_M_max_5x5(V_ref, E_ref, 0.0,
                                  np.array([rho_verify]*4 + [1.0]))
print(f"    Verification: M_max at rho={rho_verify:.4f} = {M_verify:.6f}")

# Method 2: What V enhancement is needed?
# M_max ~ V * rho / (2*xi). Need V *= 1/0.902 = 1.109
V_ratio_needed = 1.0 / M_MAX_CURRENT
V_needed = V_B2B2_max * V_ratio_needed
print(f"\n  Method 2: V enhancement needed")
print(f"    Current V(B2,B2) max = {V_B2B2_max:.6f}")
print(f"    Needed V(B2,B2) max = {V_needed:.6f}")
print(f"    Enhancement factor = {V_ratio_needed:.4f}x ({(V_ratio_needed-1)*100:.1f}%)")
print(f"    Tesla upper bound = {V_OPT_MAX:.6f} (ratio {V_OPT_MAX/V_B2B2_max:.4f}x)")
print(f"    Spectral bound = {float(tesla['spectral_upper_bound']):.6f}")

# Method 3: What |xi| reduction is needed?
# Need |xi_eff| = |xi| * M_max (to get M_eff = 1)
xi_current = lambda_B2  # at mu=0
xi_needed = xi_current * M_MAX_CURRENT
mu_for_xi = lambda_B2 - xi_needed

print(f"\n  Method 3: |xi| reduction needed (via mu shift)")
print(f"    Current |xi_B2| = {xi_current:.6f}")
print(f"    Needed |xi_B2| = {xi_needed:.6f}")
print(f"    Required mu = lambda_B2 - xi_needed = {mu_for_xi:.6f}")

# Direct check
M_at_mu_for_xi, _ = compute_M_max_5x5(V_ref, E_ref, mu_for_xi, rho_ref)
print(f"    M_max at mu = {mu_for_xi:.4f}: {M_at_mu_for_xi:.6f}")
print()

# Method 4: Combined small corrections
# If we can get 5% from van Hove and 6% from multi-sector...
print("  Method 4: Combined small corrections needed")
print("  Each correction factor f_i such that product > 1/M_max = 1.109:")
print(f"    f_total needed = {1.0/M_MAX_CURRENT:.4f}")
print(f"    Example: f_VH=1.04 * f_imp=1.04 * f_ms=1.03 = {1.04*1.04*1.03:.4f}")
print(f"    Or: f_VH=1.06 * f_16x16=1.02 * f_mu=1.03 = {1.06*1.02*1.03:.4f}")
print()


# ======================================================================
#  SAVE RESULTS
# ======================================================================

save_dict = {
    # Fundamental numbers
    'lambda_B1': lambda_B1,
    'lambda_B2': lambda_B2,
    'lambda_B3': lambda_B3,
    'gap_B2_B1': gap_B2_B1,
    'gap_B3_B2': gap_B3_B2,
    'V_B2B2_max': V_B2B2_max,
    'V_B1B2_max': float(np.max(V_B1B2)),
    'V_B2pos_B2neg_max': V_B2pos_B2neg_max,
    'M_max_current': M_MAX_CURRENT,
    'rho_full_current': RHO_FULL,

    # Mechanism 1: Van Hove
    'd2_fold': d2_fold,
    'delta_tau': delta_tau,
    'rho_vh_per_mode': rho_vh,
    'rho_vh_full': rho_vh_full,
    'M_max_vh': M_max_vh,
    'vh_ratio': vh_ratio,

    # Mechanism 2: Fabry-Perot
    'Q_cavity': Q_cavity,
    'R_fold_eff': R_fold_eff,
    'R_edge': R_edge,
    'cavity_enhancement': cavity_enhancement,
    'M_max_fp': M_max_fp,

    # Mechanism 3: Evanescent
    'xi_evanescent': xi_ev,

    # Mechanism 4: mu shift
    'mu_scan': mu_scan,
    'M_max_vs_mu': M_max_mu,
    'M_max_mu_best': M_max_mu_best,
    'mu_at_best': mu_at_best,

    # Mechanism 5: Bootstrap
    'M_max_bootstrap': M_bootstrap,

    # Mechanism 6: 16x16
    'M_max_16x16': M_max_16,
    'M_max_10x10': M_max_10,
    'M_max_8x8': M_max_8,

    # Combined
    'M_max_vh_mu_best': M_best_vh_mu,
    'M_max_vh_16x16': M_max_16_vh,
    'M_max_all_best': M_best_all,
    'mu_all_best': mu_best_all,

    # Minimum input
    'rho_needed': rho_needed,
    'rho_ratio_needed': rho_ratio_needed,
    'V_ratio_needed': V_ratio_needed,
    'xi_needed': xi_needed,
}

out_npz = os.path.join(SCRIPT_DIR, 's34a_qa_11pct.npz')
np.savez_compressed(out_npz, **save_dict)
print(f"Saved: {out_npz}")
print(f"File size: {os.path.getsize(out_npz) / 1024:.1f} KB")


# ======================================================================
#  PLOT
# ======================================================================

fig, axes = plt.subplots(2, 3, figsize=(18, 10))

# Panel 1: Van Hove DOS profile across wall
ax = axes[0, 0]
ax.plot(tau_grid, rho_grid, 'b-', lw=2, label='Van Hove regularized')
ax.axhline(y=1.0/(np.pi*v_B2_wall), color='r', ls='--', lw=1.5,
           label=f'Mean DOS = {1/(np.pi*v_B2_wall):.3f}')
ax.axvline(x=tau_0, color='gray', ls=':', alpha=0.5, label=f'Fold center')
ax.set_xlabel('tau')
ax.set_ylabel('Local DOS per mode')
ax.set_title('Mech 1: Van Hove DOS at Wall 2')
ax.legend(fontsize=7)
ax.grid(True, alpha=0.3)

# Panel 2: M_max vs mu
ax = axes[0, 1]
ax.plot(mu_scan, M_max_mu, 'b-', lw=2, label='5x5 Thouless')
ax.axhline(y=1.0, color='black', ls='--', lw=2, label='M=1 threshold')
ax.axvline(x=lambda_B1, color='r', ls=':', alpha=0.7,
           label=f'lambda_B1={lambda_B1:.3f}')
ax.axvline(x=lambda_B2, color='g', ls=':', alpha=0.7,
           label=f'lambda_B2={lambda_B2:.3f}')
if mu_crit is not None and M_max_mu_best > 1.0:
    ax.axvline(x=mu_crit, color='orange', ls=':', alpha=0.7,
               label=f'mu_crit={mu_crit:.3f}')
ax.set_xlabel('Chemical potential mu')
ax.set_ylabel('M_max')
ax.set_title('Mech 4: Chemical Potential Shift')
ax.legend(fontsize=7)
ax.grid(True, alpha=0.3)

# Panel 3: Summary bar chart
ax = axes[0, 2]
mechanisms = ['Current', 'Van Hove\n(d=0.018)', 'Fabry-\nPerot',
              'mu shift', 'Full\n16x16', 'VH+mu', 'VH+16x16\n+mu']
M_values = [M_MAX_CURRENT, M_max_vh, M_max_fp, M_max_mu_best,
            M_max_16, M_best_vh_mu, M_best_all]
colors = ['green' if m > 1.0 else ('orange' if m > 0.95 else 'red') for m in M_values]
bars = ax.bar(mechanisms, M_values, color=colors, alpha=0.7, edgecolor='black')
ax.axhline(y=1.0, color='black', ls='--', lw=2)
for bar, m in zip(bars, M_values):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.005,
            f'{m:.3f}', ha='center', va='bottom', fontsize=8, fontweight='bold')
ax.set_ylabel('M_max')
ax.set_title('Mechanism Comparison')
ax.grid(True, alpha=0.3, axis='y')
ax.tick_params(axis='x', labelsize=7)

# Panel 4: V matrix heatmap (positive sector)
ax = axes[1, 0]
V_pos = V_16[np.ix_(pos_idx, pos_idx)]
im = ax.imshow(V_pos, cmap='viridis', aspect='equal')
ax.set_xticks(range(8))
ax.set_xticklabels(['B1','B2','B2','B2','B2','B3','B3','B3'], fontsize=7)
ax.set_yticks(range(8))
ax.set_yticklabels(['B1','B2','B2','B2','B2','B3','B3','B3'], fontsize=7)
ax.set_title('V(spinor) positive sector')
plt.colorbar(im, ax=ax, shrink=0.8)

# Panel 5: V matrix heatmap (full 16x16 selected)
ax = axes[1, 1]
V_sel = V_16[np.ix_(np.concatenate([B2_idx, neg_B2_idx]),
                      np.concatenate([B2_idx, neg_B2_idx]))]
im = ax.imshow(V_sel, cmap='viridis', aspect='equal')
labels = ['B2+','B2+','B2+','B2+','B2-','B2-','B2-','B2-']
ax.set_xticks(range(8))
ax.set_xticklabels(labels, fontsize=7)
ax.set_yticks(range(8))
ax.set_yticklabels(labels, fontsize=7)
ax.set_title('V(B2+,B2-) cross-sector')
plt.colorbar(im, ax=ax, shrink=0.8)

# Panel 6: Enhancement needed decomposition
ax = axes[1, 2]
factors = ['rho\n(11%)', 'V\n(11%)', '|xi|\n(10%)', 'VH+imp\n(4%+4%)',
           'VH+ms+mu\n(4%+3%+3%)']
needed = [rho_ratio_needed, V_ratio_needed, 1.0/M_MAX_CURRENT,
          1.04*1.04, 1.04*1.03*1.03]
achieved = [1.0, V_OPT_MAX/V_B2B2_max, 1.0, vh_ratio if vh_ratio > 1 else 1.0,
            vh_ratio if vh_ratio > 1 else 1.0]
ax.barh(factors, needed, color='lightcoral', alpha=0.7, label='Needed', edgecolor='black')
ax.barh(factors, achieved, color='lightgreen', alpha=0.7, label='Available', edgecolor='black')
ax.axvline(x=1.0, color='black', ls='-', lw=1)
ax.set_xlabel('Enhancement factor')
ax.set_title('Gap Closure Budget')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3, axis='x')

fig.suptitle(f'Session 34a QA: The 11% Hunt | M_max = {M_MAX_CURRENT:.3f} -> 1.000',
             fontsize=14, fontweight='bold')
plt.tight_layout(rect=[0, 0, 1, 0.96])
out_png = os.path.join(SCRIPT_DIR, 's34a_qa_11pct.png')
plt.savefig(out_png, dpi=150)
plt.close()
print(f"Plot saved: {out_png}")


# ======================================================================
#  FINAL SUMMARY
# ======================================================================

elapsed = time.time() - t0
print(f"\n{'='*78}")
print("FINAL SUMMARY: The 11% Hunt")
print(f"{'='*78}")
print(f"""
  BASELINE: M_max = {M_MAX_CURRENT:.6f} (threshold 1.0, shortfall {(1/M_MAX_CURRENT - 1)*100:.1f}%)

  MECHANISM          M_max     Enhancement   Closes Gap?
  --------           -----     -----------   -----------
  1. Van Hove DOS    {M_max_vh:.4f}    {M_max_vh/M_MAX_CURRENT:.4f}x        {'YES' if M_max_vh > 1 else 'NO'}
  2. Fabry-Perot     {M_max_fp:.4f}    {M_max_fp/M_MAX_CURRENT:.4f}x        {'YES' if M_max_fp > 1 else 'NO'}
  3. Evanescent      {M_max_ev:.4f}    1.000x         NO (single-wall)
  4. mu shift        {M_max_mu_best:.4f}    {M_max_mu_best/M_MAX_CURRENT:.4f}x        {'YES' if M_max_mu_best > 1 else 'NO'}
  5. Bootstrap       {M_bootstrap:.4f}    1.000x         NO (contraction mapping)
  6. Full 16x16      {M_max_16:.4f}    {M_max_16/M_MAX_CURRENT:.4f}x        {'YES' if M_max_16 > 1 else 'NO'}

  COMBINED:
  B. VH + mu         {M_best_vh_mu:.4f}    {M_best_vh_mu/M_MAX_CURRENT:.4f}x        {'YES' if M_best_vh_mu > 1 else 'NO'}
  D. VH + mu + 16x16 {M_best_all:.4f}    {M_best_all/M_MAX_CURRENT:.4f}x        {'YES' if M_best_all > 1 else 'NO'}

  MINIMUM INPUT:
  - Need rho x {rho_ratio_needed:.4f} (11% increase in wall DOS)
  - OR V x {V_ratio_needed:.4f} (11% increase in pairing kernel)
  - OR mu = {mu_for_xi:.4f} (shift to B2 eigenvalue neighborhood)

  STRUCTURAL CONSTRAINTS:
  - V(B2,B2) is locked at 0.057 by spinor algebra. Tesla optimization
    reaches 0.094 but M_max does not change (eigenvalue, not element).
  - V(B1,B1) = 0 exactly (Trap 1). The B1 Fermi-surface mode is inert.
  - V(B2+,B2-) = 0.000 (particle-hole channel dead for B2 self-pairing).
  - BCS bootstrap fails for M_max < 1 (contraction mapping theorem).

  REMAINING OPEN PATHS (uncomputed):
  1. Multi-wall tight-binding: if Turing pattern creates wall array,
     hybridized B2 bands could provide additional states at Fermi surface.
     Requires: wall spacing < xi_ev = {xi_ev:.2f} in tau-space.
  2. Fluctuation corrections: Aslamazov-Larkin + Maki-Thompson diagrams
     beyond mean-field. With N_eff = 4, corrections could be ~25%.
     Requires: full Gorkov theory in NCG spectral setting.
  3. Finite-density spectral action (P2b): nonzero mu from first principles.
     Requires: new NCG theory (Connes-Chamseddine at finite density).
  4. Non-singlet sector pairing: Peter-Weyl sectors with closer eigenvalues
     could pair among themselves. Requires: inter-sector V computation.

  Runtime: {elapsed:.1f}s
""")

print(f"{'='*78}")
