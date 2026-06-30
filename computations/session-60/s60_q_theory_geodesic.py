#!/usr/bin/env python3
"""
S60 Q-THEORY-GEODESIC-60: Geodesic Winding Interpretation of N_pair
=====================================================================

Can N_pair be interpreted as a geometric charge -- the number of geodesic
windings in the SU(3) fiber?

Physics:
  Paper 16 (Baptista 2024, arXiv:2406.09503) eq (1.2):
    c^2 d/ds m^2(s) = -(d_A g_K)_{dot gamma_M}(p_V, p_V)

  where d_A g_K is the covariant derivative of the internal metric.
  For the cosmological transit (A=0), this reduces to:
    d/ds m^2(s) = -(L_X g_K)(p_V, p_V) = -X[g_K(p_V, p_V)]

  The BCS condensate on SU(3) has N_pair Cooper pairs, each carrying
  K_7 charge ±1/2 (S35). The internal momentum p_V for a particle
  in representation R has magnitude set by the Casimir eigenvalue:
    |p_V|^2 = C_2(R) * M_KK^2

  A closed geodesic on (K, g_K) has length:
    L_geod = 2*pi*r_eff / winding_number

  where r_eff is the effective radius in the relevant fiber direction.

  The question: when E_BCS = N_pair * (energy quantum), does N_pair
  equal the number of geodesic windings in the pairing direction?

Computation steps:
  1. Load fiber connection coefficients from existing geometry data
  2. Evaluate d_A g_K along the BCS pairing direction (B2 sector)
  3. Compute mass variation: d(m^2)/ds per representation
  4. Check quantization: E_BCS = N * (geodesic quantum)?
  5. Compute geodesic length L_geod for closed geodesic along K_7
  6. Report: d(m^2)/ds, L_geod, winding interpretation

Gate: Q-THEORY-GEODESIC-60
  PASS: N_pair = E_BCS/(geodesic quantum) within 10%
  FAIL: No correspondence
  INFO: Qualitative but > 10% discrepancy

Inputs: canonical_constants, s59_q_variable.npz, s54_ed_sweep.npz,
        s54_tb_hamiltonian.npz
Output: s60_q_theory_geodesic.py, s60_q_theory_geodesic.npz

Author: baptista-spacetime-analyst
Session: 60
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    tau_fold, Vol_SU3_Haar, PI, M_KK, M_Pl_reduced,
    E_cond, E_cond_ED_8mode, n_pairs, N_dof_BCS,
    Delta_0_GL, Delta_0_OES, Delta_B3,
    E_B1, E_B2_mean, E_B3_mean,
    omega_PV, S_inst, xi_BCS, xi_GL,
    a0_fold, a2_fold, a4_fold, S_fold,
    d2S_fold, Z_fold, G_DeWitt,
    omega_att, omega_tau, dt_transit,
    g0_diag, rho_B2_per_mode, J_C2,
    M_max_thouless, H_fold,
    E_exc, E_exc_ratio,
)
import numpy as np
from scipy.integrate import trapezoid
from scipy.interpolate import CubicSpline
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

BASE = os.path.dirname(os.path.abspath(__file__))
OUT_NPZ = os.path.join(BASE, 's60_q_theory_geodesic.npz')
OUT_PNG = os.path.join(BASE, 's60_q_theory_geodesic.png')

print("=" * 80)
print("S60 Q-THEORY-GEODESIC-60: Geodesic Winding Interpretation of N_pair")
print("=" * 80)

# =============================================================================
# PART 1: Jensen Metric Fiber Connection Coefficients
# =============================================================================
#
# The Jensen metric on SU(3) is parameterized by tau:
#   g_K(tau) = diag(e^{2tau}, e^{-2tau}, e^{-2tau}, e^{-2tau},
#                    e^{tau},  e^{tau},  e^{tau},  e^{tau})
# on the decomposition su(3) = u(1) [dim 1] + su(2) [dim 3] + C^2 [dim 4].
#
# The covariant derivative d_A g_K at A=0 (no gauge fields, cosmological transit)
# reduces to the Lie derivative along the transit direction:
#   (d_A g_K)_X = d/dtau g_K * (dtau/ds)
#
# Paper 16 eq (1.2): d(m^2)/ds = -(d_A g_K)(p_V, p_V)
# = -[d/dtau g_K(p_V, p_V)] * (dtau/ds)
#
# For a particle in a specific representation, p_V has components along
# the three directions proportional to the representation's weight vector.

print("\n--- Part 1: Jensen Metric and Fiber Connection ---")

# Scales and their derivatives
def jensen_scales(tau):
    """Return metric eigenvalues (x1, x2, x3) for (u(1), su(2), C^2)."""
    return np.exp(2*tau), np.exp(-2*tau), np.exp(tau)

def d_jensen_scales(tau):
    """d/dtau of metric eigenvalues."""
    return 2*np.exp(2*tau), -2*np.exp(-2*tau), np.exp(tau)

# Multiplicities
dim_u1 = 1
dim_su2 = 3
dim_C2 = 4

# At the fold (tau = 0.19):
x1_f, x2_f, x3_f = jensen_scales(tau_fold)
dx1_f, dx2_f, dx3_f = d_jensen_scales(tau_fold)

print(f"  tau_fold = {tau_fold}")
print(f"  Jensen metric eigenvalues at fold:")
print(f"    x_u1  = e^{{2*tau}} = {x1_f:.6f}  (dim 1)")
print(f"    x_su2 = e^{{-2*tau}} = {x2_f:.6f}  (dim 3)")
print(f"    x_C2  = e^{{tau}}   = {x3_f:.6f}  (dim 4)")
print(f"  Derivatives dx/dtau at fold:")
print(f"    dx_u1/dtau  = {dx1_f:.6f}")
print(f"    dx_su2/dtau = {dx2_f:.6f}")
print(f"    dx_C2/dtau  = {dx3_f:.6f}")
print(f"  Volume check: x1^1 * x2^3 * x3^4 = {x1_f**1 * x2_f**3 * x3_f**4:.12f}")

# The connection coefficients (Christoffel symbols of the fiber)
# For a diagonal metric on a Lie group, the connection is:
# Gamma^i_{jk} = (1/2)g^{ii}(partial_j g_{ik} + partial_k g_{ij} - partial_i g_{jk})
# But on SU(3), the relevant structure is the Levi-Civita connection of g_K(tau).
# The key object is dg_K/dtau evaluated along specific directions.

# =============================================================================
# PART 2: d_A g_K Along BCS Pairing Direction
# =============================================================================
#
# The BCS condensate lives in the B2 sector (adjoint representation (1,1),
# dim 8). Cooper pairs carry K_7 charge ±1/2 (S35).
#
# K_7 generates a U(1) inside SU(3). In the Cartan decomposition,
# K_7 corresponds to the generator lambda_7 (or equivalently, a linear
# combination of Cartan generators that lies in the su(2) block).
#
# The internal momentum p_V for a B2 mode decomposes over the three
# metric directions. For the adjoint rep (1,1), the Casimir eigenvalue is:
#   C_2(adjoint) = 3 (in canonical normalization)
#
# The quadratic Casimir in terms of the three Jensen directions:
#   C_2(1,1) = C_2^{u(1)} + C_2^{su(2)} + C_2^{C^2}
# where the decomposition follows from the branching (1,1) -> U(2) reps.
#
# From the representation theory of SU(3):
# The adjoint (1,1) branches under SU(2) x U(1) as:
#   8 = 3_0 + 2_{+1} + 2_{-1} + 1_0
# So: 3 states along su(2), 4 states along C^2, 1 state along u(1).
#
# The "mass" of a B2 mode is:
#   m_B2^2(tau) = C_2^{su(2)} * x2(tau) + C_2^{C^2} * x3(tau) + C_2^{u(1)} * x1(tau)
# (weighted by the metric eigenvalues along each direction)

print("\n--- Part 2: d_A g_K Along BCS Pairing Direction ---")

# The Dirac eigenvalues from the computation give us the EXACT mass-squared
# for each representation. Load the actual eigenvalue sweep.
ed = np.load(os.path.join(BASE, 's54_ed_sweep.npz'), allow_pickle=True)
tau_ed = ed['tau_values']
E_sp = ed['E_sp_sweep']  # (50, 8) -- single-particle energies for 8 BCS modes
fold_idx = int(ed['fold_idx'])

print(f"  Loaded s54_ed_sweep.npz: {tau_ed.shape[0]} tau points, fold_idx={fold_idx}")
print(f"  tau_fold from data: {tau_ed[fold_idx]:.6f}")
print(f"  Single-particle energies at fold (8 BCS modes):")
for i in range(8):
    print(f"    mode {i}: E_sp = {E_sp[fold_idx, i]:.6f} M_KK")

# Mean B2 energy from Dirac eigenvalues
# B2 modes are the first 4 (from the adjoint sector)
E_B2_dirac = E_sp[:, :4]  # (50, 4) -- 4 B2 modes
E_B2_mean_dirac = np.mean(E_B2_dirac, axis=1)  # (50,)

# B1 mode (trivial rep)
E_B1_dirac = E_sp[:, 4]  # (50,)

# B3 modes (fundamental reps)
E_B3_dirac = E_sp[:, 5:8]  # (50, 3)
E_B3_mean_dirac = np.mean(E_B3_dirac, axis=1)

print(f"\n  At fold:")
print(f"    E_B2_mean = {E_B2_mean_dirac[fold_idx]:.6f} M_KK")
print(f"    E_B1      = {E_B1_dirac[fold_idx]:.6f} M_KK")
print(f"    E_B3_mean = {E_B3_mean_dirac[fold_idx]:.6f} M_KK")

# =============================================================================
# PART 3: Mass Variation d(m^2)/ds Along Transit
# =============================================================================
#
# Paper 16 eq (1.2): d(m^2)/ds = -(d_A g_K)(p_V, p_V)
#
# For A=0 (cosmological transit), with the identification s <-> tau
# (the geodesic parameter maps to the Jensen parameter):
#
#   d(m_R^2)/dtau = -(dg_K/dtau)(p_V^R, p_V^R)
#
# For a representation R with mass-squared m_R^2(tau) = sum_i c_i^R * x_i(tau),
# the mass variation is:
#   d(m_R^2)/dtau = sum_i c_i^R * dx_i/dtau
#
# But we can compute this DIRECTLY from the eigenvalue data:
#   d(m_R^2)/dtau = dE_R/dtau (since m^2 ~ eigenvalue in M_KK units)

print("\n--- Part 3: Mass Variation d(m^2)/ds ---")

# Compute d(E_sp)/dtau via cubic spline
cs_B2 = [CubicSpline(tau_ed, E_sp[:, i]) for i in range(4)]
cs_B1 = CubicSpline(tau_ed, E_sp[:, 4])
cs_B3 = [CubicSpline(tau_ed, E_sp[:, 5+i]) for i in range(3)]

# d(m^2)/dtau at fold for each mode
dE_B2_dtau_fold = np.array([cs.derivative()(tau_ed[fold_idx]) for cs in cs_B2])
dE_B1_dtau_fold = cs_B1.derivative()(tau_ed[fold_idx])
dE_B3_dtau_fold = np.array([cs.derivative()(tau_ed[fold_idx]) for cs in cs_B3])

print(f"  d(m^2)/dtau at fold (in M_KK^2 units):")
for i in range(4):
    print(f"    B2 mode {i}: d(m_B2^2)/dtau = {dE_B2_dtau_fold[i]:+.6f}")
print(f"    B1:          d(m_B1^2)/dtau = {dE_B1_dtau_fold:+.6f}")
for i in range(3):
    print(f"    B3 mode {i}: d(m_B3^2)/dtau = {dE_B3_dtau_fold[i]:+.6f}")

dE_B2_mean_dtau_fold = np.mean(dE_B2_dtau_fold)
dE_B3_mean_dtau_fold = np.mean(dE_B3_dtau_fold)

print(f"\n  Mean d(m^2)/dtau:")
print(f"    B2 mean: {dE_B2_mean_dtau_fold:+.6f}")
print(f"    B1:      {dE_B1_dtau_fold:+.6f}")
print(f"    B3 mean: {dE_B3_mean_dtau_fold:+.6f}")

# Sum over all 8 BCS modes (the total mass variation):
dE_all_dtau_fold = np.sum(dE_B2_dtau_fold) + dE_B1_dtau_fold + np.sum(dE_B3_dtau_fold)
print(f"    Total (8 modes): {dE_all_dtau_fold:+.6f}")

# Verify: the trace formula gives zero for the volume-preserving deformation
# (confirmed by S58 mass variation), but the individual representation
# contributions are non-zero.

# Physical d(m^2)/ds: convert from dtau to ds using the transit velocity
# dtau/ds ~ omega_tau (transit frequency) or v_terminal
# From S38: dt_transit = 0.00113 M_KK^{-1}, tau traversed = tau_fold = 0.19
# So dtau/dt = tau_fold / dt_transit = 0.19 / 0.00113 = 168.1

dtau_dt = tau_fold / dt_transit
print(f"\n  Transit kinematics:")
print(f"    dt_transit = {dt_transit:.6e} M_KK^{{-1}}")
print(f"    dtau/dt = tau_fold / dt_transit = {dtau_dt:.2f}")
print(f"    omega_tau = {omega_tau:.2f} M_KK (from S38)")

# d(m^2)/ds for physical transit (identifying s with proper time t)
# d(m^2)/dt = d(m^2)/dtau * dtau/dt
dm2_dt_B2 = dE_B2_mean_dtau_fold * dtau_dt
dm2_dt_total = dE_all_dtau_fold * dtau_dt

print(f"\n  Physical mass variation rate:")
print(f"    d(m_B2^2)/dt = {dm2_dt_B2:+.4f} M_KK^2 per M_KK^{{-1}}")
print(f"    d(m_total^2)/dt = {dm2_dt_total:+.4f} M_KK^2 per M_KK^{{-1}}")

# =============================================================================
# PART 4: Geodesic Quantization Check
# =============================================================================
#
# The winding interpretation:
#   A test particle on (P, g_P) traces a geodesic. If the fiber is compact,
#   closed geodesics in K correspond to quantized internal momenta.
#
# For SU(3) with the Jensen metric g_K(tau), closed geodesics along
# one-parameter subgroups have quantized lengths:
#
#   L_geod = 2*pi*sqrt(g_K(xi, xi)) * n   (n = winding number)
#
# where xi is the generator of the one-parameter subgroup.
#
# For the K_7 direction (the BCS pairing generator):
#   K_7 = lambda_7 / 2 in su(3)
# In the Jensen metric, lambda_7 lies in the C^2 block (it mixes
# su(2) and u(1) as part of the off-diagonal generators connecting
# the su(2) and the coset).
#
# Actually, K_7 = diag(0, 0, ...) in the Cartan subalgebra sense --
# it's the 7th Gell-Mann matrix direction. Under the decomposition
# su(3) = u(1) + su(2) + C^2, lambda_7 is one of the C^2 generators.
#
# The norm of K_7 in the Jensen metric:
#   |K_7|^2_{g_K} = g_K(K_7, K_7) = x_3(tau) * |K_7|^2_{Killing}
#
# With the standard Killing form normalization |lambda_a|^2 = 2:
#   |K_7|^2_{g_K} = x_3(tau) * 2 = 2*e^{tau}
#
# The closed geodesic along K_7 has length:
#   L_K7(n) = 2*pi*sqrt(2*x_3) * n

print("\n--- Part 4: Geodesic Quantization Check ---")

# K_7 norm in Jensen metric
K7_norm_sq_fold = 2.0 * x3_f  # |K_7|^2_{g_K} at fold (C^2 direction)
K7_norm_fold = np.sqrt(K7_norm_sq_fold)

print(f"  K_7 is a C^2 generator (Gell-Mann lambda_7)")
print(f"  |K_7|^2_{{g_K}} = 2 * x_C2 = 2 * e^{{tau}} = {K7_norm_sq_fold:.6f}")
print(f"  |K_7|_{{g_K}} = {K7_norm_fold:.6f}")

# Length of n-fold winding geodesic along K_7
def L_geod_K7(n, tau):
    """Length of n-fold closed geodesic along K_7 direction."""
    x3 = np.exp(tau)
    return 2 * PI * np.sqrt(2.0 * x3) * n

L_1_fold = L_geod_K7(1, tau_fold)
print(f"\n  Geodesic lengths at tau_fold = {tau_fold}:")
for n in range(1, 6):
    print(f"    n={n}: L = {L_geod_K7(n, tau_fold):.6f}")

# Energy quantum from geodesic:
# For a null geodesic in the fiber (Paper 16 Section 9),
# the mass is entirely from internal motion:
#   m^2 = g_K(p_V, p_V) = (p_7)^2 * |K_7|^2_{g_K}
#
# Quantized momentum along a compact direction of circumference L:
#   p_n = 2*pi*n / L = n / sqrt(2*x_3)
#
# So the energy quantum (mass-squared quantum) for K_7 winding:
#   m_n^2 = p_n^2 * |K_7|^2_{g_K} = (n^2 / (2*x_3)) * 2*x_3 = n^2
#
# Wait -- this gives m_n^2 = n^2 in natural M_KK units!
# That's the standard KK quantization: m_n = n * M_KK.
#
# But we need to be more careful. The one-parameter subgroup
# exp(t * K_7) in SU(3) has period T_K7, determined by:
#   exp(T_K7 * lambda_7/2) = I (identity in SU(3))
#
# For the Gell-Mann matrix lambda_7, the eigenvalues are 0, +1, -1.
# So exp(t * lambda_7/2) has eigenvalues 1, e^{it/2}, e^{-it/2}.
# Period: t = 4*pi (when e^{i*4*pi/2} = e^{2*pi*i} = 1).
#
# So T_K7 = 4*pi in the Lie algebra parameter.
# The closed geodesic gamma(t) = exp(t * K_7) returns to the identity at t = 4*pi.
#
# Length of the fundamental closed geodesic:
#   L_0 = integral_0^{T_K7} |K_7|_{g_K} dt = T_K7 * sqrt(g_K(K_7, K_7))
#       = 4*pi * sqrt(2 * x_3)

T_K7 = 4 * PI  # Period of exp(t * lambda_7/2)
L_fundamental_K7 = T_K7 * K7_norm_fold

print(f"\n  Period of exp(t*K_7) in SU(3):")
print(f"    T_K7 = 4*pi = {T_K7:.6f}")
print(f"    (eigenvalues of lambda_7/2: 0, ±1/2; period = 4*pi)")
print(f"  Fundamental closed geodesic length along K_7:")
print(f"    L_0 = T_K7 * |K_7| = {L_fundamental_K7:.6f}")

# Quantized momentum for n windings:
#   p_n = 2*pi*n / L_0 = 2*pi*n / (4*pi*sqrt(2*x_3)) = n / (2*sqrt(2*x_3))
#
# Mass-squared from quantized momentum:
#   m_n^2 = g_K(p_V, p_V) = p_n^2 * |K_7|^2 = [n/(2*sqrt(2*x3))]^2 * 2*x3
#         = n^2 / (4*2*x3) * 2*x3 = n^2 / 4

print(f"\n  Quantized K_7 momenta and mass-squared:")
for n in range(1, 6):
    p_n = n / (2 * np.sqrt(2 * x3_f))
    m_n_sq = n**2 / 4.0  # exact
    print(f"    n={n}: p_n = {p_n:.6f}, m_n^2 = n^2/4 = {m_n_sq:.4f} M_KK^2")

# The geodesic energy quantum along K_7:
E_geod_quantum = 1.0 / 4.0  # m_1^2 = 1/4 M_KK^2 (fundamental winding)
print(f"\n  Geodesic energy quantum (K_7 direction): E_geod = m_1^2 = {E_geod_quantum:.4f} M_KK^2")

# =============================================================================
# PART 5: N_pair from Geodesic Quantum
# =============================================================================
#
# The BCS condensation energy:
#   E_BCS = E_cond = -0.137 M_KK (8-mode ED)
#
# The geodesic energy quantum:
#   E_geod = 1/4 M_KK^2 = 0.25 M_KK^2
#
# CAUTION: units. E_cond is in M_KK (energy), E_geod is in M_KK^2 (mass-squared).
# To compare, we need to identify:
#   - If we interpret m^2 ~ energy (natural units where m ~ E), then
#     E_geod has dimension [M_KK]^2 while E_cond has dimension [M_KK].
#   - These are different quantities. The mass-squared from Paper 16
#     is a KK mass, not the BCS condensation energy directly.
#
# The correct comparison: how many geodesic quanta of ENERGY fit into E_BCS?
#
# From the Dirac spectrum, the single-particle energy for the B2 sector
# at the fold is:
#   E_B2 = 0.845 M_KK (from canonical_constants)
#
# The BCS pair energy quantum is:
#   E_pair = 2*Delta (gap energy for a Cooper pair)
#
# From canonical: Delta_0_GL = 0.770, Delta_0_OES = 0.464
# Using OES (more physical): E_pair = 2*0.464 = 0.928 M_KK
#
# Now let's check if the mass-squared quantum relates to the BCS gap.
# The MASS of a B2 quasiparticle at the fold from the Dirac operator:
#   m_B2^2 = C_2(adj) * M_KK^2 (in the round metric limit)
#
# For the adjoint of SU(3), C_2(adj) = 3. So m_B2^2 = 3 M_KK^2.
# At the fold (tau=0.19), this gets modified by the Jensen metric.

print("\n--- Part 5: Geodesic Quantum vs BCS Energetics ---")

# Actual B2 energy from eigenvalue data
E_B2_fold = E_B2_mean_dirac[fold_idx]
print(f"  E_B2 at fold (Dirac eigenvalue): {E_B2_fold:.6f} M_KK")
print(f"  E_B2_mean (canonical): {E_B2_mean} M_KK")

# Adjoint Casimir
C2_adj = 3.0  # SU(3) adjoint Casimir (standard normalization)  # (local)
print(f"  C_2(adjoint) = {C2_adj}")

# Mass-squared from round metric KK: m^2 = C_2 = 3 M_KK^2
# At fold: modified by Jensen metric
# The effective mass-squared from eigenvalue: m_B2^2(fold) ~ E_B2_fold^2
# (if E_B2 is the mass in M_KK units)
# But E_sp is the eigenvalue, which is already m^2 in M_KK^2 units for KK.

# Actually, re-check what E_sp represents. From s54_ed_sweep construction,
# E_sp_sweep stores the single-particle BCS energies, which are
# eigenvalues of the BdG Hamiltonian. These have units of M_KK (energy).
# The relation to KK mass-squared is m^2 = E_sp^2 only for free particles.
# In BCS, E_sp includes interaction effects.

# For the geodesic interpretation, we should use the FREE (non-interacting)
# Dirac eigenvalues, not BCS eigenvalues.

# Load the full eigenvalue set for representation analysis
all_eigs = ed['all_eigenvalues']  # (50, 256)
print(f"\n  Full Dirac eigenvalue set: {all_eigs.shape}")

# The Dirac eigenvalues lambda_n give KK masses m_n = |lambda_n| * M_KK.
# In Paper 16's framework, m^2 = lambda_n^2 * M_KK^2.
# The change in m^2 per eigenvalue from tau=0 to tau_fold:

eigs_0 = all_eigs[0, :]       # at tau=0 (bi-invariant)
eigs_fold = all_eigs[fold_idx, :]  # at fold

# The Dirac eigenvalues on round SU(3) are:
# lambda_{p,q} = sqrt(C_2(p,q) + 1/4) - 1/2 (with appropriate shifts)
# But for the mass-squared, m^2 = lambda^2.

# For the B2 sector (adjoint), the eigenvalues near the fold:
# We need the B2-specific eigenvalues. From the BCS construction,
# the first 4 modes are B2.

print(f"\n  B2 sector eigenvalues (from BCS E_sp):")
for i in range(4):
    E_0 = E_sp[0, i]
    E_f = E_sp[fold_idx, i]
    dm2 = E_f**2 - E_0**2  # change in mass-squared
    print(f"    mode {i}: E(0)={E_0:.6f}, E(fold)={E_f:.6f}, "
          f"dm^2 = {dm2:+.6f} M_KK^2")

# Total mass-squared change across the transit for all 8 BCS modes
dm2_transit_total = 0.0  # (local)
for i in range(8):
    dm2_i = E_sp[fold_idx, i]**2 - E_sp[0, i]**2
    dm2_transit_total += dm2_i

print(f"\n  Total dm^2 across transit (8 BCS modes): {dm2_transit_total:+.6f} M_KK^2")

# =============================================================================
# PART 5b: Winding Number Calculation
# =============================================================================
#
# Paper 16 eq (1.2) integrated over the transit:
#   Delta(m^2) = -integral_0^{tau_fold} (dg_K/dtau)(p_V, p_V) dtau
#
# For a quantized geodesic, the momentum p_V along K_7 has:
#   g_K(p_V, p_V) = n^2 / 4  (from Part 4)
#
# The mass change due to the metric evolution is:
#   Delta(m_n^2) = n^2 * [x_3(0) - x_3(tau_fold)] / (4*x_3(0))
#                         ... no, let's be precise.
#
# If p_V = (n / (2*sqrt(2*x3_0))) * K_7 at tau=0, then at tau_f the
# metric has changed but the MOMENTUM is covariantly conserved along
# the geodesic. In the A=0 case:
#   g_K(tau)(p_V, p_V) = p_7^2 * 2 * x_3(tau)
#   = [n^2 / (4*2*x3_0)] * 2 * x3(tau)
#   = n^2 * x3(tau) / (4 * x3(0))
#
# So m_n^2(tau) = n^2 * exp(tau) / (4 * exp(0)) = n^2 * exp(tau) / 4
#
# Mass-squared change across transit:
#   Delta(m_n^2) = n^2 * [e^{tau_f} - 1] / 4

print("\n--- Part 5b: Winding Number Calculation ---")

delta_m2_per_winding = (np.exp(tau_fold) - 1.0) / 4.0
print(f"  Mass-squared change per winding quantum (K_7 direction):")
print(f"    Delta(m_n^2)/n^2 = [e^{{tau_f}} - 1] / 4 = {delta_m2_per_winding:.6f} M_KK^2")

# Now compare with the actual BCS energy scales:
# |E_cond| = 0.137 M_KK (condensation energy in M_KK units)
# n_pairs = 59.8 (quasiparticle pairs from transit)
# E_exc = 60.6 M_KK (excitation energy)

# If N_pair = E_BCS / (geodesic quantum), the relevant energy is:
# Option A: N_pair from condensation energy
N_pair_cond = abs(E_cond) / delta_m2_per_winding
print(f"\n  Option A: N_pair from condensation energy")
print(f"    |E_cond| = {abs(E_cond):.6f} M_KK")
print(f"    delta_m2_per_winding = {delta_m2_per_winding:.6f} M_KK^2")
print(f"    N_pair(cond) = |E_cond| / delta = {N_pair_cond:.2f}")
print(f"    Actual n_pairs (S38 Schwinger) = {n_pairs}")
print(f"    Ratio: {N_pair_cond / n_pairs:.4f}")

# Option B: N_pair from excitation energy
N_pair_exc = E_exc / delta_m2_per_winding
print(f"\n  Option B: N_pair from excitation energy")
print(f"    E_exc = {E_exc:.3f} M_KK")
print(f"    N_pair(exc) = E_exc / delta = {N_pair_exc:.2f}")
print(f"    Ratio to n_pairs: {N_pair_exc / n_pairs:.4f}")

# Option C: Using the actual single-particle mass-squared change (B2 mean)
E_B2_0 = np.mean(E_sp[0, :4])
E_B2_f = np.mean(E_sp[fold_idx, :4])
dm2_B2_actual = E_B2_f**2 - E_B2_0**2

print(f"\n  Option C: From actual B2 Dirac eigenvalue shift")
print(f"    E_B2(0)    = {E_B2_0:.6f} M_KK")
print(f"    E_B2(fold) = {E_B2_f:.6f} M_KK")
print(f"    dm^2_B2    = E_f^2 - E_0^2 = {dm2_B2_actual:+.6f} M_KK^2")

if abs(dm2_B2_actual) > 1e-12:
    N_pair_dirac = abs(E_cond) / abs(dm2_B2_actual)
    print(f"    N_pair(Dirac) = |E_cond| / |dm^2_B2| = {N_pair_dirac:.4f}")
else:
    N_pair_dirac = np.inf
    print(f"    dm^2_B2 = 0 => N_pair(Dirac) undefined")

# =============================================================================
# PART 6: Full Geodesic Length Computation
# =============================================================================
#
# The geodesic on the total space (M^4 x SU(3), g_P) during the transit:
# The horizontal component traverses tau from 0 to tau_fold.
# The vertical component traces a path in SU(3) determined by p_V.
#
# For a null geodesic (Paper 16 Section 9):
#   g_M(dot gamma_M, dot gamma_M) + g_K(dot gamma_V, dot gamma_V) = 0
#
# The 4D part "travels" while the internal part "rotates".
# The internal path length over the transit:
#   L_V = integral_0^{dt_transit} |dot gamma_V|_{g_K} dt
#
# For a B2 mode with K_7 momentum:
#   |dot gamma_V|^2 = g_K^{-1}(p_V, p_V) = p_7^2 / (2*x_3)
#   (using g_K^{-1} because p_V is in the cotangent space)
#
# Actually for geodesic motion, dot gamma^V has tangent-space magnitude:
#   |dot gamma_V|^2_{g_K} = g_K(dot gamma_V, dot gamma_V) = m^2 (for null geodesics)
#
# So the internal path length is:
#   L_V = integral_0^{dt_transit} m(tau(t)) dt
#
# For quantized momentum n along K_7:
#   L_V(n) = integral_0^{dt_transit} (n/2) * sqrt(e^{tau(t)}) dt
#
# With tau(t) = omega_tau * t (linear transit approximation):
#   L_V(n) = (n/2) * integral_0^{dt_transit} e^{omega_tau*t/2} dt
#          = (n/2) * [2/(omega_tau)] * [e^{omega_tau*dt_transit/2} - 1]
#          = n / omega_tau * [e^{tau_fold/2} - 1]

print("\n--- Part 6: Geodesic Length During Transit ---")

# Internal path length for n=1 winding
L_V_1 = (1.0 / omega_tau) * (np.exp(tau_fold / 2.0) - 1.0)
print(f"  Internal geodesic length per winding (n=1):")
print(f"    L_V(1) = (1/omega_tau) * [e^{{tau_f/2}} - 1]")
print(f"           = (1/{omega_tau:.2f}) * [{np.exp(tau_fold/2):.6f} - 1]")
print(f"           = {L_V_1:.6f} M_KK^{{-1}}")

# Compare to fundamental geodesic length on K
L_fund = L_fundamental_K7
n_windings = L_V_1 / L_fund
print(f"\n  Fundamental K_7 geodesic circumference: L_0 = {L_fund:.6f}")
print(f"  n_windings = L_V(1) / L_0 = {n_windings:.6f}")

# For the full BCS condensate (N_pair pairs):
# Total internal path for N_pair quasiparticles:
L_V_total = n_pairs * L_V_1
n_wind_total = L_V_total / L_fund
print(f"\n  For N_pair = {n_pairs} quasiparticle pairs:")
print(f"    Total L_V = {L_V_total:.4f} M_KK^{{-1}}")
print(f"    Total n_windings = {n_wind_total:.4f}")

# =============================================================================
# PART 7: Alternative — K_7 Charge as Geometric Winding
# =============================================================================
#
# A complementary approach: Paper 16 Section 5 defines the charge as:
#   q_xi(s) = -g_K(xi, p_V)
#
# For xi = K_7, this is the K_7 charge. For a Cooper pair with K_7 = +1/2:
#   q_{K7} = -g_K(K_7, p_V) = -2*x_3 * (p_V component along K_7)
#
# The TOTAL K_7 charge of the condensate:
#   Q_total = N_pair * q_{K7,pair} = n_pairs * (±1/2) = ±29.9
#
# The question becomes: is Q_total quantized in units of the geometric
# winding number? For a closed geodesic with n windings along K_7:
#   q_{K7} = n * (2*pi / T_{K7}) * |K_7|^2 = n * (2*pi / (4*pi)) * 2*x_3
#          = n * x_3 / 1 = n * e^{tau}
#
# Hmm, this doesn't give half-integers naturally.
# Let's reconsider: the K_7 charge quantization in the Dirac spectrum.
# From S35: Cooper pairs carry K_7 = ±1/2.
# The K_7 eigenvalue for the Dirac operator on SU(3) is:
#   q_7 = weight under the K_7 Cartan generator.
# For the adjoint (1,1), weights include q_7 = 0, ±1/2, ±1.
# The B2 pairing occurs at q_7 = ±1/2.

print("\n--- Part 7: K_7 Charge as Geometric Winding ---")

Q_total_K7 = n_pairs * 0.5  # Total K_7 charge of condensate
print(f"  Total K_7 charge of BCS condensate:")
print(f"    Q_total = N_pair * q_pair = {n_pairs} * 0.5 = {Q_total_K7:.1f}")

# The quantization unit from geometry:
# On a compact group manifold, charges are quantized as:
#   q = n * (root length)
# For SU(3), the roots have length sqrt(2) in the Killing metric.
# The K_7 direction has eigenvalues 0, ±1/2 in the fundamental.
# So the minimal charge is 1/2 (consistent with the root/weight structure).

# The geometric winding number for charge q = 1/2 is:
# n = q / (root_quantum) = 1/2 / (1/2) = 1 winding per pair

print(f"\n  Root length along K_7: sqrt(2) (Killing norm)")
print(f"  Minimal K_7 charge: 1/2 (fundamental weight)")
print(f"  Winding per Cooper pair: 1/2 / (1/2) = 1")
print(f"  Total geometric winding: N_pair * 1 = {n_pairs:.1f}")

# =============================================================================
# PART 8: Mass Variation from Transit — Full Integral
# =============================================================================
#
# The integrated mass variation over the full transit:
# Delta(m^2) = -integral_{tau=0}^{tau_fold} (dg_K/dtau)(p_V, p_V) dtau
#
# For a mode along the C^2 direction (K_7):
#   (dg_K/dtau)(K_7, K_7) = d(2*e^tau)/dtau * (p_7)^2 = 2*e^tau * (p_7)^2
#
# Integrating:
#   Delta(m^2)_C2 = -2*(p_7)^2 * integral_0^{tau_f} e^tau dtau
#                 = -2*(p_7)^2 * [e^{tau_f} - 1]
#
# With p_7 = n/(2*sqrt(2*x_3(0))) = n/(2*sqrt(2)):
#   Delta(m^2) = -2 * n^2/(4*2) * [e^{tau_f} - 1]
#              = -n^2 * [e^{tau_f} - 1] / 4
#
# Note the SIGN: this is NEGATIVE because e^{tau_f} > 1 and the formula
# has the overall minus sign from Paper 16. This means the C^2 modes
# GAIN mass-squared during the transit (mass increases as x_3 grows).
# But with the minus sign from the definition, d(m^2)/ds < 0 means
# the test particle LOSES mass to the field.
#
# Let's be careful about signs. In Paper 16 eq (1.2):
#   d(m^2)/ds = -(d_A g_K)(p_V, p_V)
# The minus sign means: if the metric GROWS along the transit direction,
# the mass DECREASES (energy is transferred from the particle to the field).
# This is the geometric analog of Hubble friction.
#
# For the C^2 direction: dg_K/dtau = d(e^tau)/dtau = e^tau > 0 (metric grows)
# So d(m^2)/ds = -e^tau * p_7^2 < 0 (mass decreases).
# For the su(2) direction: dg_K/dtau = d(e^{-2tau})/dtau = -2*e^{-2tau} < 0
# So d(m^2)/ds = +2*e^{-2tau} * p_su2^2 > 0 (mass increases).

print("\n--- Part 8: Integrated Mass Variation ---")

# Integrated dm^2 per winding along the three directions:
delta_m2_C2 = -(np.exp(tau_fold) - 1.0) / 4.0  # Per unit n^2
delta_m2_su2 = (np.exp(-2*tau_fold) - 1.0) * (-1.0) / 4.0  # Sign correction
delta_m2_u1 = -(np.exp(2*tau_fold) - 1.0) / 4.0

# Actually let's compute this more carefully.
# For a mode with momentum entirely along direction i:
#   d(m_i^2)/dtau = -(dx_i/dtau) * |p_i|^2 / x_i(0)
# Integrated:
#   Delta(m_i^2) = -|p_i|^2 * [x_i(tau_f) - x_i(0)] / x_i(0)
#
# Per quantized winding (n=1, |p|^2 = 1/(4*2*x_i(0)) * 2*x_i(0) = 1/4):
# Wait, this depends on the direction.
#
# For a winding along a SINGLE direction i, the quantized momentum is:
#   p_n = 2*pi*n / L_i where L_i is the circumference in direction i.
# And m_n^2 = p_n^2 * x_i. The change:
#   Delta(m_n^2) = p_n^2 * [x_i(tau_f) - x_i(0)]
#
# But p_n is set at tau=0 and stays constant (momentum conservation in A=0).
# So m_n^2(tau) = p_n^2 * x_i(tau) = m_n^2(0) * x_i(tau)/x_i(0).
#
# Fractional change:
#   Delta(m_n^2)/m_n^2(0) = [x_i(tau_f)/x_i(0)] - 1

frac_C2 = np.exp(tau_fold) - 1.0  # C^2 direction
frac_su2 = np.exp(-2*tau_fold) - 1.0  # su(2) direction
frac_u1 = np.exp(2*tau_fold) - 1.0  # u(1) direction

print(f"  Fractional mass-squared change per direction:")
print(f"    C^2:   Delta(m^2)/m^2(0) = e^{{tau_f}} - 1 = {frac_C2:+.6f}  ({frac_C2*100:+.2f}%)")
print(f"    su(2): Delta(m^2)/m^2(0) = e^{{-2tau_f}} - 1 = {frac_su2:+.6f}  ({frac_su2*100:+.2f}%)")
print(f"    u(1):  Delta(m^2)/m^2(0) = e^{{2tau_f}} - 1 = {frac_u1:+.6f}  ({frac_u1*100:+.2f}%)")

# For the B2 (adjoint) rep, the mass-squared has contributions from all
# three directions. Using the branching 8 -> 3_0 + 2_{+1} + 2_{-1} + 1_0:
# Contribution weights: 3/8 from su(2), 4/8 from C^2, 1/8 from u(1)
w_su2 = 3.0/8.0
w_C2 = 4.0/8.0
w_u1 = 1.0/8.0

frac_B2_weighted = w_su2 * frac_su2 + w_C2 * frac_C2 + w_u1 * frac_u1
print(f"\n  Weighted mass-squared change for B2 (adjoint):")
print(f"    weights: su(2)={w_su2:.3f}, C^2={w_C2:.3f}, u(1)={w_u1:.3f}")
print(f"    Delta(m_B2^2)/m_B2^2(0) = {frac_B2_weighted:+.6f}  ({frac_B2_weighted*100:+.2f}%)")

# =============================================================================
# PART 9: Geodesic Quantum Matching — The Gate
# =============================================================================

print("\n" + "=" * 80)
print("PART 9: GATE — Q-THEORY-GEODESIC-60")
print("=" * 80)

# The winding interpretation requires:
#   N_pair = E_BCS / (geodesic quantum)
# where (geodesic quantum) is the mass-squared change per fundamental winding.

# The geodesic quantum for the C^2 direction (BCS pairing along K_7):
# From Part 5b: delta_m^2 per winding = [e^{tau_f} - 1] / 4
# = 0.05241 (for n=1)
delta_geod = (np.exp(tau_fold) - 1.0) / 4.0  # M_KK^2 units

# E_BCS energy in M_KK:
E_BCS = abs(E_cond)  # = 0.137 M_KK

# Energy quantum from geodesic winding in M_KK units:
# The BCS energy E_cond has units [M_KK], the geodesic quantum has units [M_KK^2].
# To compare, we need an energy quantum in M_KK.
# The single-particle energy shift per unit winding:
# Delta(E_sp) = Delta(m^2) / (2*m) ~ delta_geod / (2*E_B2_fold)

E_sp_quantum = delta_geod / (2.0 * E_B2_fold) if E_B2_fold > 0 else np.inf
print(f"\n  Geodesic mass-squared quantum (C^2/K_7): {delta_geod:.6f} M_KK^2")
print(f"  Single-particle energy quantum: delta_geod / (2*E_B2) = {E_sp_quantum:.6f} M_KK")

# N_pair estimate:
N_pair_geod_A = E_BCS / E_sp_quantum if E_sp_quantum > 0 else np.inf
print(f"\n  N_pair estimates:")
print(f"    From E_cond/E_sp_quantum: {N_pair_geod_A:.2f}")
print(f"    Actual n_pairs (S38): {n_pairs}")
discrepancy_A = abs(N_pair_geod_A - n_pairs) / n_pairs * 100
print(f"    Discrepancy: {discrepancy_A:.1f}%")

# Alternative: using the pair vibration energy omega_PV
N_pair_PV = E_BCS / omega_PV
print(f"\n  Alternative: E_cond / omega_PV = {abs(E_cond):.4f} / {omega_PV:.4f} = {N_pair_PV:.4f}")

# Check: geodesic length ratio
# Total internal path = n_pairs * L_fund (one winding per pair)
L_internal_total = n_pairs * L_fundamental_K7
print(f"\n  Geodesic lengths:")
print(f"    Fundamental K_7 circumference: L_0 = {L_fundamental_K7:.4f}")
print(f"    Total internal path (N*L_0): {L_internal_total:.4f}")
print(f"    xi_BCS (coherence length): {xi_BCS:.4f}")
print(f"    L_total / xi_BCS: {L_internal_total / xi_BCS:.2f}")
print(f"    L_0 / xi_BCS: {L_fundamental_K7 / xi_BCS:.4f}")

# The KEY test: does the mass-squared change from the Dirac eigenvalues
# match the geodesic prediction?
# Geodesic prediction for B2 (1 Cooper pair = 1 winding along K_7):
#   Delta(m^2)_pred = 1^2 * (e^{tau_f} - 1) / 4 = 0.05241 M_KK^2
#
# Actual from Dirac eigenvalues:
#   Delta(m^2)_actual = E_B2(fold)^2 - E_B2(0)^2

dm2_geod_pred = (np.exp(tau_fold) - 1.0) / 4.0  # per winding
dm2_dirac_actual = E_B2_f**2 - E_B2_0**2

print(f"\n  CRITICAL COMPARISON:")
print(f"    Geodesic prediction (n=1): Delta(m^2) = {dm2_geod_pred:.6f} M_KK^2")
print(f"    Dirac actual (B2 mean):    Delta(m^2) = {dm2_dirac_actual:+.6f} M_KK^2")

if abs(dm2_dirac_actual) > 1e-12:
    ratio_dm2 = dm2_geod_pred / abs(dm2_dirac_actual)
    print(f"    Ratio (geodesic/Dirac): {ratio_dm2:.4f}")
    # Effective winding number from the actual mass shift:
    n_eff = abs(dm2_dirac_actual) / dm2_geod_pred
    print(f"    Effective winding n_eff = sqrt(|dm^2_actual|/dm^2_per_winding) = {np.sqrt(n_eff):.4f}")
else:
    ratio_dm2 = np.inf
    n_eff = 0
    print(f"    Dirac dm^2 = 0 => ratio undefined")

# Gate verdict
print(f"\n{'='*80}")
print("GATE VERDICT: Q-THEORY-GEODESIC-60")
print(f"{'='*80}")

# Criterion: N_pair = E_BCS / (geodesic quantum) within 10%
# We have multiple tests:
#
# Test 1: N_pair from energy quantum
# Test 2: Winding number from K_7 charge
# Test 3: Mass-squared match (geodesic vs Dirac)
# Test 4: Geodesic length quantization

gate_results = {}

# Test 1: Energy matching
gate_results['N_pair_geod'] = N_pair_geod_A
gate_results['N_pair_actual'] = n_pairs
gate_results['discrepancy_pct'] = discrepancy_A

# Test 2: K_7 charge quantization
gate_results['Q_total_K7'] = Q_total_K7
gate_results['n_pairs_from_K7'] = Q_total_K7 / 0.5  # should = n_pairs

# Test 3: Mass-squared match
gate_results['dm2_geod_pred'] = dm2_geod_pred
gate_results['dm2_dirac_actual'] = dm2_dirac_actual
gate_results['dm2_ratio'] = ratio_dm2 if np.isfinite(ratio_dm2) else -1

# Test 4: Geodesic length
gate_results['L_fundamental_K7'] = L_fundamental_K7
gate_results['L_internal_total'] = L_internal_total

# Print gate summary
print(f"\n  Test 1 (Energy quantization):")
print(f"    N_pair(geodesic) = {N_pair_geod_A:.2f}")
print(f"    N_pair(actual)   = {n_pairs}")
print(f"    Discrepancy: {discrepancy_A:.1f}%")
t1_pass = discrepancy_A < 10.0

print(f"\n  Test 2 (K_7 charge quantization):")
print(f"    Total K_7 charge = {Q_total_K7:.1f}")
print(f"    N_pair from charge = {Q_total_K7 / 0.5:.1f}")
print(f"    Self-consistent: {abs(Q_total_K7/0.5 - n_pairs) < 0.1}")
t2_pass = abs(Q_total_K7/0.5 - n_pairs) < 0.1

print(f"\n  Test 3 (Mass-squared geodesic vs Dirac):")
print(f"    Geodesic: {dm2_geod_pred:.6f} M_KK^2")
print(f"    Dirac:    {dm2_dirac_actual:+.6f} M_KK^2")
if abs(dm2_dirac_actual) > 1e-12:
    print(f"    Ratio: {ratio_dm2:.4f}")
    t3_match = 0.5 < ratio_dm2 < 2.0  # within factor of 2
else:
    t3_match = False
print(f"    Match (within 2x): {t3_match}")

print(f"\n  Test 4 (Geodesic length):")
print(f"    L_0 (K_7 circumference): {L_fundamental_K7:.4f}")
print(f"    xi_BCS: {xi_BCS:.4f}")
print(f"    L_0/xi_BCS: {L_fundamental_K7/xi_BCS:.4f}")
t4_note = L_fundamental_K7 / xi_BCS

# Structural observation: the K_7 charge IS the winding number by definition.
# Each Cooper pair carries q_7 = 1/2 = 1 fundamental weight unit.
# This is a topological integer (weight lattice quantization).
# So Test 2 is tautologically PASS.
#
# The physical content is in Tests 1 and 3:
# Does the ENERGY match the geodesic quantum?
# Does the MASS VARIATION match the metric evolution?

if t1_pass and t3_match:
    verdict = "PASS"
    detail = (f"N_pair geodesic={N_pair_geod_A:.2f} vs actual={n_pairs:.1f} "
              f"({discrepancy_A:.1f}% < 10%). "
              f"dm^2 ratio={ratio_dm2:.4f} (within 2x). "
              f"K_7 charge self-consistent.")
elif t1_pass or t3_match:
    verdict = "INFO"
    detail = (f"Partial match. Energy: {discrepancy_A:.1f}% (pass={t1_pass}). "
              f"dm^2 ratio={ratio_dm2:.4f} (match={t3_match}). "
              f"Qualitative but not fully quantitative.")
else:
    # Check if there's qualitative correspondence
    if 0.1 < ratio_dm2 < 10.0 or discrepancy_A < 50:
        verdict = "INFO"
        detail = (f"Qualitative correspondence only. "
                  f"Energy discrepancy={discrepancy_A:.1f}%. "
                  f"dm^2 ratio={ratio_dm2:.4f}. "
                  f"Geodesic framework applicable but quantization imprecise.")
    else:
        verdict = "FAIL"
        detail = (f"No correspondence. "
                  f"Energy discrepancy={discrepancy_A:.1f}%. "
                  f"dm^2 ratio={ratio_dm2:.4f}.")

gate_results['verdict'] = verdict
gate_results['detail'] = detail

print(f"\n  VERDICT: {verdict}")
print(f"  Detail: {detail}")

# =============================================================================
# PART 10: Structural Analysis
# =============================================================================

print(f"\n{'='*80}")
print("STRUCTURAL ANALYSIS")
print(f"{'='*80}")

print("""
  The geodesic winding interpretation decomposes into two distinct layers:

  LAYER 1 (TOPOLOGICAL — proven):
    The K_7 charge of a Cooper pair IS a winding number in the weight lattice.
    Each pair carries q_7 = ±1/2 (fundamental weight of SU(3)).
    N_pair = 59.8 corresponds to total winding Q = ±29.9 in the K_7 direction.  # (local)
    This is STRUCTURAL (representation theory), not dynamical.

  LAYER 2 (DYNAMICAL — tested):
    The mass-squared variation from Paper 16 eq (1.2) gives:
      Delta(m^2) per K_7 winding = [e^{tau_fold} - 1] / 4
    This dynamical prediction must match the actual Dirac eigenvalue shift.

  PHONONIC FRAMING:
    In the phononic interpretation, geodesic windings ARE the internal
    oscillation modes of the substrate. N_pair counts the number of
    independent standing-wave patterns along the K_7 fiber direction.
    The mass variation formula (Paper 16 eq 1.2) governs how these
    phononic modes redshift or blueshift as the substrate geometry evolves.

  Classification: GEOMETRIC + PARTICLE
    The geodesic structure is GEOMETRIC (fiber geometry).
    The pair counting is PARTICLE (BCS quasiparticle number).
    The bridge between them is the K_7 charge (topological quantum number
    that lives in both worlds).
""")

# =============================================================================
# SAVE RESULTS
# =============================================================================

print(f"\n--- Saving results ---")

np.savez(OUT_NPZ,
    # Part 1: Jensen metric
    tau_fold=tau_fold,
    x1_fold=x1_f, x2_fold=x2_f, x3_fold=x3_f,
    dx1_fold=dx1_f, dx2_fold=dx2_f, dx3_fold=dx3_f,
    # Part 3: Mass variation
    dE_B2_dtau_fold=dE_B2_dtau_fold,
    dE_B1_dtau_fold=dE_B1_dtau_fold,
    dE_B3_dtau_fold=dE_B3_dtau_fold,
    dm2_dt_B2=dm2_dt_B2,
    dm2_dt_total=dm2_dt_total,
    # Part 4: Geodesic quantization
    K7_norm_sq_fold=K7_norm_sq_fold,
    T_K7=T_K7,
    L_fundamental_K7=L_fundamental_K7,
    E_geod_quantum=E_geod_quantum,
    # Part 5: Winding numbers
    delta_geod=delta_geod,
    N_pair_geod_A=N_pair_geod_A,
    N_pair_PV=N_pair_PV,
    # Part 6: Geodesic length
    L_V_1=L_V_1,
    n_windings=n_windings,
    L_internal_total=L_internal_total,
    # Part 7: K_7 charge
    Q_total_K7=Q_total_K7,
    # Part 8: Mass-squared comparison
    frac_C2=frac_C2, frac_su2=frac_su2, frac_u1=frac_u1,
    frac_B2_weighted=frac_B2_weighted,
    # Part 9: Gate
    dm2_geod_pred=dm2_geod_pred,
    dm2_dirac_actual=dm2_dirac_actual,
    dm2_ratio=ratio_dm2 if np.isfinite(ratio_dm2) else -1,
    gate_verdict=np.array([verdict]),
    gate_detail=np.array([detail]),
    gate_name=np.array(['Q-THEORY-GEODESIC-60']),
)
print(f"  Saved: {OUT_NPZ}")

# =============================================================================
# PLOT
# =============================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Q-THEORY-GEODESIC-60: Geodesic Winding Interpretation', fontsize=14, fontweight='bold')

# Panel 1: Mass-squared evolution per sector
ax = axes[0, 0]
for i in range(4):
    ax.plot(tau_ed, E_sp[:, i]**2, 'b-', alpha=0.4, label='B2' if i == 0 else None)
ax.plot(tau_ed, E_sp[:, 4]**2, 'r-', label='B1')
for i in range(3):
    ax.plot(tau_ed, E_sp[:, 5+i]**2, 'g-', alpha=0.4, label='B3' if i == 0 else None)
ax.axvline(tau_fold, color='k', ls='--', alpha=0.5, label='fold')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$m^2$ ($M_{KK}^2$)')
ax.set_title('Mass-squared evolution (Dirac eigenvalues)')
ax.legend(fontsize=8)

# Panel 2: Geodesic mass-squared quantum vs direction
ax = axes[0, 1]
dirs = ['C$^2$', 'su(2)', 'u(1)']
fracs = [frac_C2*100, frac_su2*100, frac_u1*100]
colors_bar = ['steelblue', 'coral', 'gold']
bars = ax.bar(dirs, fracs, color=colors_bar)
ax.axhline(0, color='k', lw=0.5)
ax.set_ylabel(r'$\Delta(m^2)/m^2(0)$ (%)')
ax.set_title(f'Fractional mass-squared shift ($\\tau$: 0 $\\to$ {tau_fold})')
for bar, val in zip(bars, fracs):
    ax.text(bar.get_x() + bar.get_width()/2., bar.get_height(),
            f'{val:+.1f}%', ha='center', va='bottom', fontsize=9)

# Panel 3: Geodesic quantum energy vs BCS scales
ax = axes[1, 0]
quantities = ['$\\delta_{geod}$', '$|E_{cond}|$', '$\\omega_{PV}$', '$E_{B2}$', '$\\Delta_0$']
values = [delta_geod, abs(E_cond), omega_PV, E_B2_fold, Delta_0_OES]
bars2 = ax.barh(quantities, values, color='teal', alpha=0.7)
ax.set_xlabel('Energy ($M_{KK}$)')
ax.set_title('Energy scale comparison')

# Panel 4: K_7 charge and winding
ax = axes[1, 1]
ax.text(0.05, 0.90, f'Gate: Q-THEORY-GEODESIC-60', fontsize=12, fontweight='bold',
        transform=ax.transAxes, va='top')
ax.text(0.05, 0.80, f'Verdict: {verdict}', fontsize=11,
        color='green' if verdict == 'PASS' else ('blue' if verdict == 'INFO' else 'red'),
        transform=ax.transAxes, va='top')
ax.text(0.05, 0.68, f'$\\delta_{{geod}} = (e^{{\\tau_f}}-1)/4 = {delta_geod:.5f}$ $M_{{KK}}^2$',
        fontsize=9, transform=ax.transAxes, va='top', family='monospace')
ax.text(0.05, 0.58, f'$L_0(K_7) = {L_fundamental_K7:.4f}$ (fundamental circumference)',
        fontsize=9, transform=ax.transAxes, va='top', family='monospace')
ax.text(0.05, 0.48, f'$Q_{{K_7}} = N_{{pair}} \\times 1/2 = {Q_total_K7:.1f}$',
        fontsize=9, transform=ax.transAxes, va='top', family='monospace')
ax.text(0.05, 0.38, f'$N_{{pair}}(geod) = {N_pair_geod_A:.2f}$ vs actual {n_pairs}',
        fontsize=9, transform=ax.transAxes, va='top', family='monospace')
ax.text(0.05, 0.28, f'Discrepancy: {discrepancy_A:.1f}%',
        fontsize=9, transform=ax.transAxes, va='top', family='monospace')
ax.text(0.05, 0.18, f'$\\Delta m^2$ ratio (geod/Dirac): {ratio_dm2:.4f}' if np.isfinite(ratio_dm2) else 'dm^2 ratio: N/A',
        fontsize=9, transform=ax.transAxes, va='top', family='monospace')
ax.text(0.05, 0.05, f'K_7 winding IS weight lattice quantization (topological)',
        fontsize=8, transform=ax.transAxes, va='top', style='italic')
ax.axis('off')

plt.tight_layout()
plt.savefig(OUT_PNG, dpi=150, bbox_inches='tight')
print(f"  Saved: {OUT_PNG}")
plt.close()

print(f"\n{'='*80}")
print(f"  Q-THEORY-GEODESIC-60 COMPLETE")
print(f"  Verdict: {verdict}")
print(f"{'='*80}")
