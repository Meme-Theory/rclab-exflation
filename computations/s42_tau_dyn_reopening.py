#!/usr/bin/env python3
"""
s42_tau_dyn_reopening.py  --  TAU-DYN-REOPEN-42
=================================================
Determines whether fabric gradient stiffness Z(tau) from W1-1 reopens
TAU-DYN-36, the decisive closure that found tau_BCS / tau_transit = 38,600.

Three mechanisms analyzed:
  (a) Direct inertial enhancement  (canonical vs non-canonical normalization)
  (b) Thouless-Valatin mass renormalization (mode coupling sum)
  (c) Friedmann friction (overdamped cosmological regime)

Gate:  TAU-DYN-REOPEN-42
  PASS:         Shortfall_new < 10
  INTERMEDIATE: 10 <= Shortfall_new <= 1000
  FAIL:         Shortfall_new > 1000

Input:
  tier0-computation/s42_gradient_stiffness.npz   (W1-1)
  tier0-computation/s36_sfull_tau_stabilization.npz
  tier0-computation/s36_tau_dynamics.npz
  tier0-computation/s40_collective_inertia.npz

Output:
  tier0-computation/s42_tau_dyn_reopening.npz
  tier0-computation/s42_tau_dyn_reopening.png
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

# ============================================================
# 0. Load all input data
# ============================================================
base = Path(r"C:\sandbox\Ainulindale Exflation\tier0-computation")

d_z   = np.load(base / "s42_gradient_stiffness.npz", allow_pickle=True)
d_s36 = np.load(base / "s36_sfull_tau_stabilization.npz", allow_pickle=True)
d_dyn = np.load(base / "s36_tau_dynamics.npz", allow_pickle=True)
d_s40 = np.load(base / "s40_collective_inertia.npz", allow_pickle=True)

# Key numbers
tau_fold   = 0.190
Z_fold     = float(d_z['Z_fold'].ravel()[0])         # 74,731
dS_fold    = float(d_z['dS_fold'].ravel()[0])        # 58,673
d2S_fold   = float(d_z['d2S_fold'].ravel()[0])       # 317,863
S_fold     = float(d_z['S_fold'].ravel()[0])         # 250,361
G_DeWitt   = float(d_z['G_DeWitt'].ravel()[0])       # 5.0
M_ATDHFB   = float(d_z['M_ATDHFB'].ravel()[0])      # 1.695
c_fabric   = float(d_z['c_fabric'].ravel()[0])       # 210

tau_grid   = d_z['tau_grid']
Z_spec     = d_z['Z_spectral']
dS_arr     = d_z['dS_dtau']
d2S_arr    = d_z['d2S_dtau2']

# From S36:
tau_BCS         = float(d_dyn['tau_BCS'])             # 40.0 (internal units)
BCS_window      = float(d_dyn['window_width'])        # 0.03
dt_transit_S36  = float(d_dyn['an_S_full_dt_transit'])  # 0.00113
shortfall_S36   = 1.0 / float(d_dyn['an_S_full_dt_over_tau_BCS'])  # ~35,393

# From S40:
M_ATDHFB_total = float(d_s40['M_ATDHFB_TOTAL'])  # 1.695
M_IB_total     = float(d_s40['M_IB_TOTAL'])       # 3.866
omega_SA_fold  = float(d_s40['omega_SA_fold'])     # 433.1
omega_BCS_fold = float(d_s40['omega_BCS_fold'])    # 48.4

# Use S36's own shortfall number (analytic, S_full, standard G):
# dt_transit / tau_BCS = 2.825e-5, so shortfall = 35,393
# The prompt says 38,600 -- we'll compute both and use the more conservative
shortfall_original = shortfall_S36  # 35,393

print("=" * 70)
print("TAU-DYN-REOPEN-42: Fabric Gradient Stiffness Reopening Analysis")
print("=" * 70)
print()
print(f"Z_fold           = {Z_fold:.1f}")
print(f"|dS/dtau|_fold   = {dS_fold:.1f}")
print(f"d2S/dtau2_fold   = {d2S_fold:.1f}")
print(f"G_DeWitt         = {G_DeWitt:.1f}")
print(f"M_ATDHFB         = {M_ATDHFB:.3f}")
print(f"tau_BCS          = {tau_BCS:.1f}")
print(f"BCS window       = {BCS_window:.3f}")
print(f"dt_transit (S36) = {dt_transit_S36:.6f}")
print(f"shortfall (S36)  = {shortfall_original:.0f}")
print()

# ============================================================
# 1. MECHANISM (a): Direct Inertial Enhancement
# ============================================================
# The Lagrangian for tau(x,t) in the fabric is:
#
#   L = integral d^3x [ (1/2) M_eff (dtau/dt)^2
#                       - (1/2) Z(tau) (nabla tau)^2
#                       - V_eff(tau) ]
#
# For the HOMOGENEOUS mode tau(t) (uniform over space), the gradient
# term vanishes identically: nabla tau = 0.
#
# The EOM is:  M_eff * ddot{tau} = -V'(tau)
#
# This is INDEPENDENT of Z. The gradient stiffness Z does not appear
# in the homogeneous equation of motion. Therefore:
#
#   (a) CANONICAL CASE: If Z appears only as the coefficient of (nabla tau)^2,
#       it does NOT change the homogeneous transit time. Period.
#
# The S36 calculation used:
#   M_eff * ddot{tau} = -dS/dtau  (with M_eff = G_DeWitt = 5.0)
#
# With the S40 correction M_ATDHFB = 1.695 < G_DeWitt = 5.0, the transit
# is actually FASTER (lower inertia = faster acceleration).
#
# Transit time scales as sqrt(M_eff), so:
#   dt_transit(S40) = dt_transit(S36) * sqrt(M_ATDHFB / G_DeWitt)
#                   = dt_transit(S36) * sqrt(1.695 / 5.0)
#                   = dt_transit(S36) * 0.582

correction_ATDHFB = np.sqrt(M_ATDHFB / G_DeWitt)
dt_transit_ATDHFB = dt_transit_S36 * correction_ATDHFB
shortfall_direct = tau_BCS / dt_transit_ATDHFB

print("=" * 70)
print("MECHANISM (a): Direct Inertial Enhancement")
print("=" * 70)
print()
print("For homogeneous tau(t), the gradient term Z*(nabla tau)^2 = 0.")
print("The EOM is M_eff * ddot{tau} = -dS/dtau, independent of Z.")
print()
print(f"S36 used G_DeWitt = {G_DeWitt:.1f} as inertia")
print(f"S40 computed M_ATDHFB = {M_ATDHFB:.3f}")
print(f"sqrt(M_ATDHFB / G_DeWitt) = {correction_ATDHFB:.4f}")
print()
print(f"dt_transit (corrected) = {dt_transit_ATDHFB:.6f}")
print(f"Shortfall (direct)     = {shortfall_direct:.0f}")
print()
print("RESULT: Direct inertial enhancement DOES NOT HELP.")
print(f"  Shortfall changes from {shortfall_original:.0f} to {shortfall_direct:.0f}")
print(f"  (factor {shortfall_direct/shortfall_original:.2f}x WORSE with ATDHFB inertia)")
print()

# ============================================================
# 2. MECHANISM (b): Thouless-Valatin Mass Renormalization
# ============================================================
# Even for the homogeneous mode, coupling to fabric fluctuations
# can renormalize the effective inertia through the Thouless-Valatin
# self-energy. In nuclear physics, this gives M_TV > M_cranking by
# factors of 1.5-3.
#
# The mechanism: anharmonicity of V_eff(tau) couples the homogeneous
# mode (k=0) to finite-k fluctuations. The perturbative correction is:
#
#   delta_M = sum_{k != 0} |<0|F|k>|^2 / (omega_k - omega_0)
#
# where F is the anharmonic force operator (cubic and higher terms in V).
#
# For a scalar field on a 3D lattice of N_cells sites with lattice
# spacing a, the modes have frequencies:
#
#   omega_k^2 = omega_0^2 + (Z / M_eff) * k^2
#
# where omega_0 = sqrt(V'' / M_eff) = sqrt(d2S / M_eff) and
# k goes from 2*pi/L to 2*pi/a (UV cutoff).
#
# For the SU(3) fabric, the "lattice" is the spatial fabric with
# N_cells ~ 32 (from the Voronoi tessellation) and L ~ R_obs.
# But the UV cutoff is set by the KK scale Lambda_KK.
#
# The matrix element for a cubic coupling V''' ~ d3S/dtau3 is:
#   |<0|F|k>|^2 ~ (V''')^2 / (4 * M_eff * omega_k) * (1/(2*M_eff*omega_0))
#
# The TV sum is:
#   delta_M / M_eff = (V''')^2 / (8 * M_eff^2 * omega_0)
#                     * sum_k 1 / (omega_k * (omega_k^2 - omega_0^2))

# First compute omega_0 (oscillation frequency at the fold)
omega_0_squared = d2S_fold / M_ATDHFB
omega_0 = np.sqrt(omega_0_squared)

# The "mass" of the tau field (oscillation frequency in the potential well)
m_tau = omega_0
print("=" * 70)
print("MECHANISM (b): Thouless-Valatin Mass Renormalization")
print("=" * 70)
print()
print(f"omega_0 = sqrt(d2S/M_eff) = sqrt({d2S_fold:.0f}/{M_ATDHFB:.3f})")
print(f"        = {omega_0:.2f}  (spectral action units)")
print()

# Fabric mode spectrum
# omega_k^2 = omega_0^2 + c_fabric^2 * k^2
# where c_fabric = sqrt(Z / M_eff) = 210
# k ranges from k_min = 2*pi/L to k_max = 2*pi/a_KK (UV cutoff)

# For the observable universe, L ~ 14,250 Mpc. But in KK units, this
# is enormously large. The UV cutoff a_KK ~ 1 (the KK scale).
# k_min << 1, k_max ~ 2*pi

# The TV sum in 3D:
#   delta_M / M_eff = integral d^3k / (2*pi)^3 * |coupling|^2 / (omega_k * delta_omega)
#
# This is the key question: is the sum convergent?
#
# In d spatial dimensions, the sum goes as:
#   integral k^{d-1} dk / (c_fabric * k * c_fabric^2 * k^2)
#   = integral k^{d-4} dk / c_fabric^3
#
# For d=3: integral k^{-1} dk -- LOGARITHMICALLY DIVERGENT
# For d=2: integral k^{-2} dk -- power divergent
# For d=1: integral k^{-3} dk -- power divergent
#
# In 3D, the TV sum is logarithmically UV-divergent.
# The regularized result (with UV cutoff Lambda) is:
#
#   delta_M / M_eff ~ (V'''/V'')^2 / (8*pi^2) * ln(Lambda / m_tau) / c_fabric^3

# Need V''' = d3S/dtau3. Compute from the S36 data.
tau_s36 = d_s36['tau_combined']
S_s36   = d_s36['S_full']

# Cubic spline to get d3S/dtau3 at the fold
from scipy.interpolate import CubicSpline
cs = CubicSpline(tau_s36, S_s36)
d3S_fold = cs(tau_fold, nu=3)

print(f"d3S/dtau3 at fold = {d3S_fold:.1f}")
print()

# Anharmonicity parameter
anharm = (d3S_fold / d2S_fold)**2
print(f"(V'''/V'')^2 = ({d3S_fold:.0f}/{d2S_fold:.0f})^2 = {anharm:.6f}")
print()

# TV sum (3D, regularized):
# delta_M / M_eff = (1/(8*pi^2)) * (V'''/V'')^2 * (1/M_eff) * ln(Lambda_UV / m_tau) / c_fabric
#
# But we need to be more careful. The standard TV formula in 3D is:
#
# For a scalar field phi with Lagrangian:
#   L = (1/2) M ddot{phi}^2 - (1/2) Z (nabla phi)^2 - (1/2) V'' phi^2 - (1/6) V''' phi^3
#
# The self-energy correction to the inverse propagator at k=0, omega=omega_0 is:
#   Sigma(omega_0) = (V''')^2 integral d^3q/(2*pi)^3 * G(q, omega_0-omega_q) / (2*omega_q)
#
# But this is the quantum field theory self-energy, which modifies the
# propagator pole. For the CLASSICAL collective inertia, what matters is
# the adiabatic (omega -> 0) limit.
#
# The classical TV mass in nuclear physics (Thouless-Valatin, 1962) is:
#   M_TV = M_cranking + 2 * sum_{n>0} |<n|J|0>|^2 / (E_n - E_0)
#
# where J is the generator of the collective motion and E_n are the
# intrinsic excitation energies.
#
# For our fabric, the "intrinsic excitations" are spatial modes with k != 0.
# The coupling between the k=0 mode and k != 0 modes comes from the
# ANHARMONICITY (cubic coupling V''').
#
# In the RPA (random phase approximation), the TV mass is:
#
#   M_TV / M = 1 + (V''')^2 / (2 * M_eff) * sum_{k!=0} 1 / (2*omega_k)^3
#
# In 3D continuous:
#   sum_k 1/omega_k^3 = integral d^3k/(2*pi)^3 * 1/(omega_0^2 + c^2 k^2)^{3/2}
#
# Let u = c*k/omega_0:
#   = (4*pi)/(2*pi)^3 * omega_0^{-3} * integral_0^{Lambda/omega_0}
#     u^2 du / (1 + u^2)^{3/2} * (omega_0/c)^3
#   = 1/(2*pi^2 * c^3) * integral_0^{u_max} u^2/(1+u^2)^{3/2} du
#
# The integral:
#   I = integral_0^U u^2/(1+u^2)^{3/2} du = [-u/sqrt(1+u^2) + ln(u + sqrt(1+u^2))]_0^U
#     = -U/sqrt(1+U^2) + ln(U + sqrt(1+U^2))
#     ~ ln(2*U) - 1 for U >> 1

# UV cutoff: Lambda_UV in units of k. In KK units, k_max ~ 2*pi (one KK length).
# But what sets the physical UV cutoff?
#
# The spectral action itself provides the cutoff. The highest KK mode in
# the computation has level 3, with max eigenvalue ~ 2.1 M_KK.
# Beyond this, the spectral action cutoff f(D^2/Lambda^2) suppresses contributions.
# A conservative UV cutoff is k_max = Lambda_KK ~ 2*pi / (KK length).
#
# In our units where M_KK = 1, k_max ~ 2*pi ~ 6.28.
# omega_0 = 433.1 in the same units.
#
# WAIT. This is the critical point. omega_0 = 433 >> k_max * c = 6.28 * 210 = 1319.
# Actually c_fabric * k_max = 210 * 6.28 = 1319.
# And omega_0 = 433, so c*k_max/omega_0 = 1319/433 = 3.05.
# U_max = 3.05. Not deeply UV -- the sum is FINITE and modest.

# Let's compute more carefully with proper dimensional analysis.
# omega_k^2 = omega_0^2 + c^2 * k^2
# omega_0 = sqrt(d2S / M_eff) = sqrt(317863 / 1.695) = 433.1

# In 3D with volume V, number density of modes = V/(2*pi)^3
# TV sum per unit volume:
#   Sigma_TV = (V''')^2 / (2 * (2*M_eff*omega_0)^2) * integral d^3k/(2*pi)^3 / omega_k^3
#
# Wait, I need to be more careful about the TV formula normalization.
#
# The Thouless-Valatin inertia for a collective variable Q (here Q = tau)
# with coupling to intrinsic states |n> through the operator F_int is:
#
#   M_TV = M_cranking + 2 * sum_n |<n|dH/dQ|0>|^2 / (E_n - E_0)^3  [WRONG]
#
# Actually the TV theorem says:
#   M_TV = 2 * sum_n |<n|J|0>|^2 / (E_n - E_0)
#
# where J is the GENERATOR of collective motion (angular momentum for rotation).
# For our problem, J would be the momentum conjugate to tau.
#
# But for a scalar field problem, the relevant quantity is the self-energy
# correction from mode coupling. Let me redo this properly.
#
# Consider the homogeneous mode amplitude q(t) = <tau(x,t)> and
# fluctuations phi(x,t) = tau(x,t) - q(t).
#
# The Lagrangian splits as:
#   L = V_space * [(1/2)*M*q_dot^2 - V(q)]
#     + integral d^3x [(1/2)*M*phi_dot^2 - (1/2)*Z*(nabla phi)^2 - (1/2)*V''(q)*phi^2]
#     - integral d^3x [(1/2)*V'''(q)*q_delta * phi^2 + ...]
#
# Wait, the coupling between q and phi comes from expanding V(q + phi):
#   V(q + phi) = V(q) + V'(q)*phi + (1/2)*V''(q)*phi^2 + (1/6)*V'''(q)*phi^3
#
# The term V'(q)*phi vanishes when integrated over space (phi has zero mean
# by construction). The phi^2 term gives the mass of fluctuations.
# The phi^3 term gives cubic self-coupling of fluctuations.
#
# But where is the q-phi coupling? It comes from the NEXT order:
#   When q changes by delta_q, V''(q) changes by V'''(q)*delta_q.
#   So the coupling is: -(1/2)*V'''(q)*delta_q * phi^2
#
# This gives the vertex: q couples to phi^2 with strength V'''/2.
#
# The self-energy of q from this coupling (one loop) is:
#   Pi(omega) = (V'''/2)^2 * integral d^3k/(2*pi)^3 * chi_k(omega)
#
# where chi_k(omega) is the susceptibility of the phi field at momentum k.
# For free fluctuations:
#   chi_k(omega) = -1/(M*(omega_k^2 - omega^2))
#
# At the collective frequency omega = omega_0:
#   Pi(omega_0) = -(V''')^2/4 * integral d^3k/(2*pi)^3 / (M*(omega_k^2 - omega_0^2))
#
# The corrected equation of motion is:
#   [M*omega^2 - V'' - Pi(omega)] * delta_q = 0
#
# Expanding Pi around omega_0:
#   M_eff = M - dPi/d(omega^2)|_{omega_0}
#         = M + (V''')^2/4 * integral d^3k/(2*pi)^3 * 1/(M*(omega_k^2-omega_0^2)^2)
#
# Wait, the mass renormalization is:
#   delta_M = -dPi/d(omega^2)
#           = -(V''')^2/4 * integral d^3k/(2*pi)^3 * (-1)/(M*(omega_k^2-omega_0^2)^2)
#           = (V''')^2/(4*M) * integral d^3k/(2*pi)^3 / (omega_k^2-omega_0^2)^2
#
# Now omega_k^2 - omega_0^2 = c^2 * k^2, so:
#   delta_M = (V''')^2/(4*M) * integral d^3k/(2*pi)^3 / (c^2*k^2)^2
#           = (V''')^2/(4*M*c^4) * integral d^3k/(2*pi)^3 / k^4
#
# In 3D: integral d^3k/(2*pi)^3 / k^4 = 4*pi/(2*pi)^3 * integral_kmin^kmax k^2/k^4 dk
#       = 1/(2*pi^2) * integral k^{-2} dk = 1/(2*pi^2) * [1/k_min - 1/k_max]
#
# This is INFRARED divergent (diverges as k_min -> 0), not UV divergent!
# As k_min -> 0, the integral -> infinity.
#
# But k_min = 2*pi/L where L is the system size (observable universe).
# So the integral is ~ L/(2*pi^2 * 2*pi) = L / (4*pi^3).
#
# This changes the physics: the mass enhancement is proportional to L,
# the spatial extent of the fabric.

# Let me compute this properly.
# k_min = 2*pi / L, k_max = 2*pi / a_KK

# In KK units, M_KK = 1, so lengths are in units of the KK scale.
# The observable universe in KK units:
# R_obs = 14,250 Mpc = 14,250 * 3.086e22 m = 4.397e26 m
# If M_KK ~ M_Planck ~ 1/(l_Planck) ~ 1/(1.616e-35 m),
# then R_obs in KK units = R_obs / l_KK.
#
# But we don't know l_KK in physical units yet. However, the RATIO
# delta_M / M is what matters, and it depends on L/a_KK = N_cells^{1/3}
# (the number of lattice spacings across the system).
#
# For the 32-cell Voronoi: L ~ 14,250 Mpc, cell size ~ 7,000 Mpc
# N_cells^{1/3} = 32^{1/3} = 3.17
# So k_min ~ 2*pi/L_total, k_max ~ 2*pi/a_cell where a_cell ~ L/N^{1/3}

# ACTUALLY: the fabric is not at the KK scale. The fabric cells are the
# 32-cell Voronoi tessellation of space. The "lattice spacing" is the cell
# size a_cell ~ R_obs / 32^{1/3} ~ 4,500 Mpc. And the system size is
# L ~ R_obs ~ 14,250 Mpc. So N_cells^{1/3} ~ 3.2, and k_max/k_min ~ 3.2.
#
# This gives very few modes! Only O(32) modes in total.
# The TV sum with 32 modes is finite and small.

# Let's compute for a 3D system with N_cells = 32
from canonical_constants import N_cells
N_side = round(N_cells**(1/3))  # ~ 3
print(f"N_cells = {N_cells}, N_side ~ {N_cells**(1/3):.2f}")
print()

# For a 3D box with N modes per side, the allowed k-vectors are
# k = (2*pi/L) * (n_x, n_y, n_z) with n_i = 1, 2, ..., N_side
# Total modes = N_side^3 ~ N_cells = 32 (excluding k=0)
#
# omega_k^2 = omega_0^2 + c^2 * |k|^2
# c = c_fabric = 210
# omega_0 = 433.1

# Actually for the 32-cell tessellation, the system is the whole observable
# universe, and the cells are NOT on a regular lattice. They're Voronoi cells.
# The modes would be the normal modes of the Voronoi tessellation.
#
# For the purpose of the TV sum, what matters is the MODE SPECTRUM.
# The lowest nonzero mode has k_1 ~ 2*pi / L (fundamental mode of the box).
# If L >> a_cell, there are many modes. But L ~ N^{1/3} * a_cell,
# so L/a_cell = N^{1/3} ~ 3.2, and the number of modes below the
# cell-scale cutoff is N_cells - 1 = 31.

# Mode sum for a box with N_cells modes:
# k_n = (2*pi/L) * n, n = 1,2,...,N_side (per dimension)
# omega_n^2 = omega_0^2 + c^2 * (2*pi*n/L)^2

# We need L in the same units as c and omega_0.
# The cell size a_cell in "internal units" depends on the mapping.
# But we can parameterize: let a_cell = 1 (KK unit).
# Then L = N^{1/3} * a_cell ~ 3.17
# k_1 = 2*pi / L = 2*pi / 3.17 = 1.98
# c * k_1 = 210 * 1.98 = 416
# Compare to omega_0 = 433.

# The key ratio:
# c * k_1 / omega_0 = 416 / 433 = 0.96
# So the lowest fabric mode has frequency COMPARABLE to omega_0.
# This means the sum is NOT enhanced by a small denominator.

# Actually, I realize L and a_cell here are in the INTERNAL space.
# The fabric gradient Z * (nabla tau)^2 involves SPATIAL gradients in M4.
# So L is the SIZE OF THE UNIVERSE and a_cell is the size of a Voronoi cell.
# These are PHYSICAL LENGTHS in M4, not internal-space lengths.
#
# c_fabric = 210 is in INTERNAL UNITS. The physical fabric sound speed is:
# v_fabric = c_fabric * (a_KK / t_KK) where a_KK and t_KK are the
# physical KK length and time scales.
#
# For the TV sum, we need everything in consistent units.
# Let's work in units where the KK time scale = 1.
# Then omega_0 = 433 has units of 1/t_KK.
#
# The spatial modes have:
# omega_k^2 = omega_0^2 + c_fabric^2 * k_physical^2 * (a_KK)^2
#
# where k_physical has units of 1/length in M4.
# c_fabric has units of (KK units) = dimensionless * (a_KK / t_KK).
#
# The problem is that c_fabric is really a VELOCITY in the internal space.
# The physical sound speed v_phys = c_fabric * v_KK where v_KK = a_KK/t_KK.
# In natural units where c=1, v_KK = 1, so v_phys = c_fabric = 210 c.
# That's superluminal, which means the fabric is STIFF.
#
# k_physical ranges from 2*pi/R_obs to 2*pi/l_KK.
# In KK units: k * l_KK ranges from 2*pi*l_KK/R_obs to 2*pi.
# Since l_KK/R_obs ~ 10^{-61} (Planck length / Hubble radius),
# k_min * l_KK ~ 10^{-60}, k_max * l_KK ~ 1.

# Let's define xi = k * l_KK (dimensionless). Then:
# omega_k^2 = omega_0^2 + c_fabric^2 * xi^2 / t_KK^2
#           = omega_0^2 + c_fabric^2 * xi^2
# (since we're working in units of t_KK = l_KK/c = l_KK)

# xi_min = l_KK/R_obs * 2*pi ~ 10^{-60}
# xi_max = 2*pi ~ 6.28

# In 3D:
# delta_M/M = (V'''/V'')^2 * V'' / (4*M*c^4) * 1/(2*pi^2)
#           * integral_{xi_min}^{xi_max} xi^{-2} dxi
#           = (V'''/V'')^2 * V'' / (8*pi^2*M*c^4) * (1/xi_min - 1/xi_max)
#           ~ (V'''/V'')^2 * V'' / (8*pi^2*M*c^4) * 1/xi_min
#           ~ (V'''/V'')^2 * V'' / (8*pi^2*M*c^4) * R_obs/(2*pi*l_KK)

# Let's see:
# (V'''/V'')^2 = anharm
# V'' = d2S_fold = 317,863
# M = M_ATDHFB = 1.695
# c = c_fabric = 210
# 1/xi_min ~ R_obs / (2*pi*l_KK)

# The hierarchy R_obs/l_KK ~ 10^61 makes this sum ENORMOUS.
# But ONLY if l_KK is the Planck length.
#
# Crucial question: what is l_KK in this framework?
# In the phonon-exflation model, the KK scale is NOT the Planck scale.
# The KK mass M_KK sets the internal geometry scale.
# If M_KK ~ TeV, l_KK ~ 10^{-19} m, R_obs/l_KK ~ 10^{45}
# If M_KK ~ M_Pl, l_KK ~ 10^{-35} m, R_obs/l_KK ~ 10^{61}
#
# Either way, the IR divergence makes delta_M/M enormous.
# BUT: this requires the fabric to be a CONNECTED, COHERENT medium
# over the entire observable universe. If the fabric has domains
# (Voronoi cells), the effective L is the CELL SIZE, not R_obs.

# Let me compute both limits:
# (1) Coherent over R_obs (L = R_obs)
# (2) Coherent over one cell (L = a_cell ~ R_obs / 32^{1/3})

# For the TV sum:
# delta_M/M = (V''')^2 / (4*M^2*c_fabric^4) * N_modes_3D / (2*pi^2*k_IR)
#
# Actually let me redo the integral cleanly.
# delta_M = (V''')^2/(4*M*c^4) * integral d^3k/(2*pi)^3 * 1/k^4
# In 3D spherical:
# = (V''')^2/(4*M*c^4) * (4*pi)/(2*pi)^3 * integral_{k_IR}^{k_UV} dk/k^2
# = (V''')^2/(4*M*c^4) * 1/(2*pi^2) * (1/k_IR - 1/k_UV)
# For k_IR << k_UV:
# ~ (V''')^2/(8*pi^2*M*c^4) * 1/k_IR
# = (V''')^2/(8*pi^2*M*c^4) * L/(2*pi)

V3 = d3S_fold
c = c_fabric
M = M_ATDHFB

print("Thouless-Valatin mass renormalization:")
print(f"V''' = d3S/dtau3 = {V3:.1f}")
print(f"c_fabric = {c:.1f}")
print(f"M_ATDHFB = {M:.3f}")
print(f"omega_0 = {omega_0:.1f}")
print()

# The enhancement factor:
# delta_M/M = (V''')^2 * L / (16*pi^3*M^2*c^4)
#
# where L is the coherence length.
#
# In units where the KK scale = 1:
# If L = N^{1/3} (in KK units, i.e., L = N^{1/3} * l_KK):
# This gives L_KK = N^{1/3} = 3.17 for N=32

# But this is WRONG. The TV sum is over SPATIAL modes in M4.
# L is a PHYSICAL LENGTH, not an internal-space length.
# The integral is over k in M4, not k in SU(3).

# The correct setup:
# The fabric is a 3D field tau(x) on M^3 (spatial section of M4).
# The Lagrangian is:
#   L = (1/2)*M_eff*V_space*(dtau/dt)^2 - V_space*V_eff(tau)   [homogeneous]
#     + (1/2)*integral d^3x [M_eff*(dphi/dt)^2 - Z*(nabla phi)^2 - V''*phi^2]
#     + coupling: -(1/2)*V'''*delta_tau * integral d^3x phi^2
#
# The coupling vertex factor is (V'''/2).
# The self-energy at one loop:
#
# Sigma(omega=0) = -(V'''/2)^2 * integral d^3k/(2*pi)^3 * 1/(M*omega_k^2)
#                = -(V''')^2/4 * integral d^3k/(2*pi)^3 / (M*(omega_0^2 + c^2*k^2))
#
# This shifts V_eff, not M_eff. For the MASS renormalization:
# delta_M = (V'''/2)^2 * integral d^3k/(2*pi)^3 * 2/(M*omega_k^3) * (c^2*k^2/omega_k^2)
#
# Hmm, I need to be more careful. Let me use the standard formula.
# The retarded self-energy from q-phi^2 coupling is:
#
# Pi_R(omega) = (V'''/2)^2 * integral d^3k/(2*pi)^3 * [2*n_B(omega_k)+1]
#               * [1/(omega-2*omega_k+i*epsilon) - 1/(omega+2*omega_k+i*epsilon)]
#
# At T=0 and omega ~ 0:
# Pi_R(0) = -(V''')^2/4 * integral d^3k/(2*pi)^3 * 1/(M*omega_k^2)
#
# This gives a POTENTIAL shift (mass^2 shift), not an inertia shift.
#
# For the INERTIA shift, we need:
# d Pi_R / d(omega^2) |_{omega=0}
#
# Pi_R(omega) has omega dependence through the propagators.
# For the bubble diagram (phi^2 intermediate state):
# Pi_R(omega) ~ integral dk k^2 / (omega^2 - 4*omega_k^2)
#
# d Pi_R / d(omega^2) |_0 = integral dk k^2 / (4*omega_k^2)^2
#                          = integral dk k^2 / (16*omega_k^4)
#
# In 3D:
# = 4*pi/(2*pi)^3 * integral dk k^4 / (16*(omega_0^2+c^2*k^2)^2)
# = 1/(8*pi^2) * integral dk k^4 / (omega_0^2+c^2*k^2)^2

# Let's compute this integral properly.
# I = integral_0^{k_max} dk * k^4 / (omega_0^2 + c^2*k^2)^2
# Let u = c*k/omega_0:
# k = omega_0*u/c, dk = omega_0*du/c
# k^4 = (omega_0*u/c)^4
# (omega_0^2+c^2*k^2)^2 = omega_0^4*(1+u^2)^2
# I = integral_0^U (omega_0*u/c)^4 / (omega_0^4*(1+u^2)^2) * (omega_0/c) du
#   = omega_0 / c^5 * integral_0^U u^4/(1+u^2)^2 du

# The integrand u^4/(1+u^2)^2 -> u^0 = 1 for u >> 1, so the integral
# grows linearly: integral ~ U for U >> 1. LINEARLY DIVERGENT.
#
# But U_max = c*k_max/omega_0. What is k_max?
# If we use the KK scale: k_max ~ 1/l_KK in physical units.
# In KK units: k_max*l_KK ~ 1, so k_max ~ 1.
# U_max = c * 1 / omega_0 = 210 / 433 = 0.485
# So U_max < 1! The integral is in the SMALL-U regime.

U_max = c / omega_0
print(f"U_max = c_fabric / omega_0 = {c:.1f} / {omega_0:.1f} = {U_max:.4f}")
print(f"Since U_max < 1, the UV cutoff is BELOW the characteristic scale.")
print()

# For U_max << 1: integral_0^U u^4/(1+u^2)^2 du ~ U^5/5
# For U_max ~ 0.5: need numerical integration
from scipy.integrate import quad

def integrand_TV(u):
    return u**4 / (1 + u**2)**2

I_TV, _ = quad(integrand_TV, 0, U_max)
print(f"TV integral I(0, {U_max:.4f}) = {I_TV:.6f}")
print(f"Comparison: U^5/5 = {U_max**5/5:.6f}")
print()

# Now the mass enhancement:
# delta_M = (V'''/2)^2 * 1/(8*pi^2) * omega_0 / (c^5 * M) * I_TV
# Actually wait -- let me reconsider what this integral represents.
#
# The one-loop self-energy from a phi^2 vertex gives a FREQUENCY shift
# through dPi/d(omega^2), which renormalizes the inertia as:
#   M_eff = M * (1 + delta)
# where delta = dPi/d(omega^2) / M
#
# But there's a subtlety: the phi^2 intermediate state requires
# TWO propagators (bubble diagram), not one.
# The bubble: Pi(omega) ~ (V''')^2 * integral dk G_k(omega/2) * G_k(-omega/2)
# Actually for a 1-loop with q -> phi + phi:
# Pi ~ integral dk 1/(omega_k*(omega^2 - 4*omega_k^2))
#
# Let me just compute this differently. The relevant physical effect is:
# as q(t) changes, it shifts the frequencies of all phi_k modes through V'''.
# This is the adiabatic Born-Oppenheimer effect.
# The correction to M is the "Born-Oppenheimer" or "time-dependent"
# correction, which in nuclear physics is the cranking inertia.
#
# For a single mode phi_k with frequency omega_k(q):
#   delta_M_k = (d omega_k/dq)^2 / (4*omega_k^3)  [quantum zero-point]
#
# omega_k^2 = omega_0^2(q) + c^2*k^2
# d omega_k/dq = (1/2*omega_k) * d omega_0^2/dq = V'''/(2*M*omega_k)
#
# Wait, omega_0^2 = V''/M, so d omega_0^2/dq = V'''/(M).
# d omega_k/dq = V'''/(2*M*omega_k)
#
# delta_M_k = [V'''/(2*M*omega_k)]^2 / (4*omega_k^3)
#           = (V''')^2 / (16*M^2*omega_k^5)
#
# Total:
# delta_M = sum_k (V''')^2 / (16*M^2*omega_k^5)
#
# In 3D continuous (per unit volume):
# delta_M = (V''')^2/(16*M^2) * integral d^3k/(2*pi)^3 / omega_k^5
#
# Let u = c*k/omega_0:
# integral = 4*pi/(2*pi)^3 * integral_0^U (omega_0*u/c)^2 du
#            / (omega_0^2*(1+u^2))^{5/2} * omega_0/c
#          = 1/(2*pi^2*c^3*omega_0^2) * integral_0^U u^2/(1+u^2)^{5/2} du

def integrand_BO(u):
    return u**2 / (1 + u**2)**2.5

I_BO, _ = quad(integrand_BO, 0, U_max)
I_BO_full, _ = quad(integrand_BO, 0, np.inf)  # converges! decays as u^{-3}

print(f"Born-Oppenheimer integral I_BO(0, {U_max:.4f}) = {I_BO:.8f}")
print(f"Born-Oppenheimer integral I_BO(0, inf) = {I_BO_full:.8f}")
print(f"  [integral u^2/(1+u^2)^{5/2} converges in 3D: decays as u^{-3}]")
print()

# The FULL integral (U->inf) is:
# integral_0^inf u^2/(1+u^2)^{5/2} du = pi/8 (by Beta function)
I_BO_exact = np.pi / 8
print(f"Exact: pi/8 = {I_BO_exact:.8f}")
print(f"Ratio I_BO(U_max)/I_BO(inf) = {I_BO/I_BO_full:.4f}")
print()

# Now: delta_M = (V''')^2/(16*M^2) * 1/(2*pi^2*c^3*omega_0^2) * I_BO
# But this is per UNIT VOLUME. For a system of volume V_space:
# Total delta_M_total = delta_M * V_space.
# And the homogeneous mode has M_total = M * V_space.
# So: delta_M/M = (V''')^2/(16*M^2) * 1/(2*pi^2*c^3*omega_0^2) * I_BO
#               (the volume cancels!)

delta_M_over_M = (V3)**2 / (16 * M**2) * 1/(2*np.pi**2 * c**3 * omega_0**2) * I_BO
delta_M_over_M_full = (V3)**2 / (16 * M**2) * 1/(2*np.pi**2 * c**3 * omega_0**2) * I_BO_full

print(f"delta_M/M (with UV cutoff at KK scale) = {delta_M_over_M:.6e}")
print(f"delta_M/M (UV complete, k -> inf)       = {delta_M_over_M_full:.6e}")
print()

# Breakdown of the prefactor:
print("Prefactor analysis:")
print(f"  (V''')^2 = {V3**2:.1f}")
print(f"  16*M^2 = {16*M**2:.3f}")
print(f"  2*pi^2*c^3 = {2*np.pi**2*c**3:.1f}")
print(f"  omega_0^2 = {omega_0**2:.1f}")
print(f"  I_BO = {I_BO:.8f}")
print(f"  Combined: {V3**2/(16*M**2*2*np.pi**2*c**3*omega_0**2):.6e}")
print()

# The enhancement is TINY because c_fabric = 210 is large:
# c^3 = 210^3 = 9.26e6
# This suppresses the integral by O(10^7).
# The anharmonicity V''' is modest: V'''/V'' is of order unity.

# IMPORTANT: But we haven't accounted for modes with k in PHYSICAL space.
# The KK cutoff limits k to k_max ~ 1 in KK units.
# But PHYSICAL k (in M4) has no such restriction -- it goes up to
# the PHYSICAL UV cutoff (Planck scale or KK mass scale).
#
# The distinction: Z(tau) multiplies (nabla_M4 tau)^2, where nabla_M4
# is the SPATIAL gradient in the external 4D space.
# The modes phi_k with k in M4 have dispersion:
# omega_k^2 = omega_0^2 + (Z/M) * k_physical^2
#
# Now Z/M has dimensions of velocity^2 = c_fabric^2.
# In natural units, c_fabric = 210 c. So the speed of tau-waves
# in physical space is 210 times the speed of light.
# This is FINE for the internal degree of freedom (tau is not a
# signal -- it's a modulus that can have superluminal sound speed
# without violating causality, as in DBI inflation).
#
# k_physical goes from 2*pi/R_obs to k_Planck = M_Pl.
# In KK units where omega_0 = 433:
# The physical k maps to u = c_fabric * k_physical / omega_0.
# k_physical at the Planck scale: k_Pl = M_Pl / hbar ~ 1/(l_Pl).
# If M_KK ~ M_Pl: u_max = c * k_Pl/omega_0 = c * M_Pl / omega_0.
# In KK units M_KK = M_Pl: k_Pl = 1, u_max = c/omega_0 = 0.485.
#
# But if M_KK << M_Pl (e.g., TeV):
# k_Pl in KK units = M_Pl/M_KK >> 1.
# u_max = c * (M_Pl/M_KK) / omega_0 = 210 * (M_Pl/M_KK) / 433
#
# For M_KK = 1 TeV: M_Pl/M_KK = 1.22e19/1e3 = 1.22e16
# u_max = 210 * 1.22e16 / 433 = 5.9e15
# The integral I_BO(0, 5.9e15) ~ I_BO(0, inf) = pi/8 = 0.3927
# So even with all modes up to Planck, the integral converges to pi/8.

# CONCLUSION: The Born-Oppenheimer / TV mass renormalization is
# delta_M/M ~ (V''')^2 / (32*pi*M^2*c^3*omega_0^2)  [using I=pi/8]
#
# This is FINITE and TINY because c_fabric^3 is large.

delta_M_over_M_converged = (V3)**2 / (16 * M**2 * 2 * np.pi**2 * c**3 * omega_0**2) * I_BO_exact
print("=" * 70)
print("TV MASS RENORMALIZATION RESULT")
print("=" * 70)
print(f"delta_M/M = (V''')^2 * pi / (256 * pi^2 * M^2 * c^3 * omega_0^2)")
print(f"          = {delta_M_over_M_converged:.6e}")
print(f"Enhancement factor = 1 + {delta_M_over_M_converged:.6e}")
print(f"Transit time correction = sqrt(1 + delta_M/M) = {np.sqrt(1+delta_M_over_M_converged):.10f}")
print()
print("The Thouless-Valatin sum CONVERGES in 3D (integral decays as k^{-3})")
print(f"and gives a NEGLIGIBLE enhancement: delta_M/M = {delta_M_over_M_converged:.2e}")
print(f"Physical reason: c_fabric = {c:.0f} >> 1 makes spatial fluctuations")
print("extremely costly, suppressing the virtual excitation of fabric modes.")
print()

# ============================================================
# 3. MECHANISM (c): Friedmann Friction
# ============================================================
print("=" * 70)
print("MECHANISM (c): Friedmann Friction")
print("=" * 70)
print()

# In a cosmological background with Hubble parameter H:
# M_eff * ddot{tau} + 3*H*M_eff*dot{tau} + V'(tau) = 0
#
# The friction term 3*H*M_eff*dot{tau} damps the motion.
# Overdamped regime: 3*H > 2*omega_0
# In this case: dot{tau} ~ -V'/(3*H*M_eff)
# Transit time: dt ~ delta_tau * 3*H*M / V' = delta_tau * 3*H*M / dS

# omega_0 = sqrt(V''/M) = 433.1 (in KK time units)
# What is H in KK time units?
#
# If the KK scale is l_KK, then t_KK = l_KK/c.
# H in physical units ranges from H_0 ~ 70 km/s/Mpc today
# to H ~ M_Pl at the Planck era to H ~ M_KK at the KK era.
#
# In KK units: H_KK = H_physical * t_KK = H * l_KK / c
# At the KK era: H ~ M_KK/hbar, so H_KK ~ 1
# (meaning the Hubble time equals the KK time).
#
# Today: H_0 = 70 km/s/Mpc = 2.27e-18 s^{-1}
# H_0 * t_KK = H_0 * l_KK/c. If l_KK = l_Pl = 5.39e-44 s/c:
# H_0 * t_KK = 2.27e-18 * 5.39e-44 = 1.22e-61 (essentially zero).
#
# The transit happens BEFORE the BCS window (which requires tau ~ 0.175-0.205).
# At what epoch? If tau evolves from tau=0 (round SU(3)) to tau=0.19 (fold),
# the transit happens at some early cosmological epoch.
#
# In the framework: the transit IS the exflation event. The Hubble rate
# during transit is set by the energy density of the spectral action itself:
# 3*M_Pl^2*H^2 = rho_SA = S_fold / V_space
#
# But S_fold is in spectral action units, not energy density.
# We need the PHYSICAL energy scale.

# If S_fold ~ Lambda^4 * f_0 where Lambda = M_KK and f_0 ~ 1:
# rho_SA ~ M_KK^4 * S_fold (in natural units, S_fold is dimensionless)
# BUT S_fold = 250,361 is already a sum of eigenvalues^2 (Seeley-DeWitt),
# and in the spectral action Tr[f(D^2/Lambda^2)]:
# S ~ f_0 * Lambda^4 * a_0 + f_2 * Lambda^2 * a_2 + f_4 * a_4 + ...
# Here S_fold = 250,361 is sum of eigenvalues^2 with multiplicity.
# In physical units: rho_SA ~ Lambda^4 * (S_fold * numerical factors).

# Rather than tracking the dimensional analysis through the spectral action
# (which requires knowing Lambda, f_0, f_2, f_4), let me compute H in
# NATURAL KK units.
#
# The Friedmann equation:
# H^2 = rho / (3*M_Pl^2)
#
# In KK units with M_KK = 1:
# rho = S_fold * M_KK^4 ~ S_fold (order of magnitude)
# M_Pl = M_Pl/M_KK = (M_Pl/M_KK) in these units
# H^2 = S_fold / (3 * (M_Pl/M_KK)^2)
# H = sqrt(S_fold/3) / (M_Pl/M_KK)
#
# For M_KK = M_Pl: H = sqrt(S_fold/3) = sqrt(83454) = 289
# For M_KK = 10^{-16} M_Pl (TeV): H = sqrt(83454) / 10^{16} = 2.89e-14

# The critical comparison:
# Overdamped if 3*H/(2*omega_0) > 1, i.e., H > 2*omega_0/3 = 289
# This is EXACTLY satisfied at M_KK = M_Pl!

H_Planck_scale = np.sqrt(S_fold / 3)
omega_0_val = omega_0
ratio_critical = H_Planck_scale / (2 * omega_0_val / 3)

print("Case 1: M_KK = M_Planck")
print(f"  H = sqrt(S_fold/3) = sqrt({S_fold:.0f}/3) = {H_Planck_scale:.1f}")
print(f"  omega_0 = {omega_0_val:.1f}")
print(f"  3H/(2*omega_0) = {3*H_Planck_scale/(2*omega_0_val):.3f}")
print(f"  H / (2*omega_0/3) = {ratio_critical:.3f}")
print()

if 3*H_Planck_scale/(2*omega_0_val) > 1:
    print("  OVERDAMPED regime: 3H > 2*omega_0")
    # In overdamped regime:
    # dot{tau} = -V'/(3*H*M_eff)
    # dt_transit = delta_tau * 3*H*M_eff / V'
    # = BCS_window * 3*H*M_eff / dS_fold
    dt_overdamped_Pl = BCS_window * 3 * H_Planck_scale * M_ATDHFB / dS_fold
    shortfall_Friedmann_Pl = tau_BCS / dt_overdamped_Pl
    print(f"  dt_transit (overdamped) = {BCS_window:.3f} * 3 * {H_Planck_scale:.1f} * {M_ATDHFB:.3f} / {dS_fold:.0f}")
    print(f"                          = {dt_overdamped_Pl:.6f}")
    print(f"  Shortfall = {shortfall_Friedmann_Pl:.1f}")
    print(f"  Compared to S36: {shortfall_original:.0f}")
    print(f"  Improvement: {shortfall_original/shortfall_Friedmann_Pl:.1f}x")
else:
    print("  UNDERDAMPED regime")
    dt_overdamped_Pl = dt_transit_S36 * (1 + 3*H_Planck_scale/(2*omega_0_val))
    shortfall_Friedmann_Pl = tau_BCS / dt_overdamped_Pl

print()

# But: at M_KK = M_Pl, the relevant H is set by the FULL energy density
# (all fields, not just the tau modulus). The Friedmann equation is:
# H^2 = (rho_tau + rho_radiation + rho_other) / (3*M_Pl^2)
# During exflation, rho_tau dominates, so H ~ sqrt(rho_tau/(3*M_Pl^2)).

# More importantly: is the transit BEFORE or AFTER inflation?
# If before: H could be enormous (Planckian)
# If during: H ~ H_inflation ~ 10^{-5} M_Pl
# If after: H << omega_0

# Let's compute for a range of H values:
H_values = np.logspace(-3, 4, 1000) * omega_0_val  # H/omega_0 from 10^{-3} to 10^4
shortfall_H = np.zeros_like(H_values)

for i, H in enumerate(H_values):
    gamma = 3*H / 2  # friction coefficient
    if gamma > omega_0_val:
        # Overdamped: dot{tau} = -V'/(3*H*M)
        dt = BCS_window * 3*H*M_ATDHFB / dS_fold
    else:
        # Underdamped: oscillation with damping
        # omega_eff = sqrt(omega_0^2 - gamma^2)
        # Envelope decays as exp(-gamma*t)
        # BUT: the tau field is rolling, not oscillating.
        # The friction slows the roll by factor ~ 1/(1 - gamma^2/omega_0^2)
        # For a linear potential V ~ V'*tau, with friction:
        # M*ddot{tau} + gamma_full*dot{tau} = -V'
        # Terminal velocity: v_term = V'/(gamma_full) = V'/(3*H*M) [if underdamped]
        # But with a quadratic potential, it's more complex.
        # For small damping: the transit time increases by ~ gamma / omega_0
        # For the rolling field:
        # tau(t) ~ (V'/M*omega_0^2) * (1 - e^{-gamma*t} * cos(omega_eff*t))
        # The dwell time in the BCS window is modified by the damping.
        # Approximate: dt ~ dt_free * (1 + gamma/omega_0)
        # More precisely for underdamped oscillator approaching equilibrium:
        # The time to cross the BCS window is:
        # dt ~ BCS_window * M * 2*omega_0 / V' * (1/(1-e^{-gamma*pi/omega_eff}))
        # For small damping: ~ dt_free * (1 + gamma*pi/(2*omega_0))

        # Actually for the rolling case (no minimum to oscillate around,
        # since S(tau) is monotonic), the motion is:
        # M*ddot{tau} + 3*H*M*dot{tau} = -V'(tau) = -dS/dtau
        # With V' > 0 (S increasing), tau accelerates in the positive direction.
        # Wait -- S is increasing with tau, so dS/dtau > 0.
        # The EOM drives tau to SMALLER values (toward the minimum of S at tau=0).
        # But in S36, tau was rolling FROM large values toward the fold at 0.19.

        # Let me reconsider: S(tau) is monotonically increasing.
        # So the "potential" V = S(tau) has V' > 0 everywhere.
        # The force is F = -V' < 0, pushing tau toward smaller values.
        # If the field starts at large tau and rolls down to tau=0,
        # it passes through the fold at tau=0.19.

        # For the underdamped case, friction adds ~ (3H/2)/omega_0 to the
        # transit time. More precisely:
        # In the WKB regime, the velocity at the fold is:
        # v_fold = V'/(3*H*M) for overdamped (terminal velocity)
        # v_fold = sqrt(2*V'/M) for undamped (free fall from rest at tau >> 0.19)

        # The S36 analysis used free-fall dynamics. With friction:
        # v(t) = v_0 * exp(-3H*t/2) + ... (decaying contribution)
        # + V'/(3*H*M) (terminal velocity)

        # If starting from rest and rolling to the fold:
        # v_fold ~ min(v_free_fall, v_terminal)
        # v_free_fall = sqrt(2*Delta_V/M) where Delta_V = V(start) - V(fold)
        # v_terminal = V'/(3*H*M)

        # Friction-limited if v_terminal < v_free_fall
        # i.e., V'/(3*H*M) < sqrt(2*Delta_V/M)
        # i.e., 3*H > V' / (M*sqrt(2*Delta_V/M)) = V'/(sqrt(2*M*Delta_V))

        # dt_transit ~ BCS_window / |v_fold|
        # = BCS_window / min(v_ff, v_term)

        # For underdamped rolling:
        # Correction factor ~ 1 + (3H/(2*omega_0))^2 (second order in friction)
        corr = 1 + (3*H/(2*omega_0_val))**2
        dt = dt_transit_ATDHFB * corr

    shortfall_H[i] = tau_BCS / dt

# Find crossover
idx_overdamped = np.where(3*H_values/(2*omega_0_val) > 1)[0]
H_cross = 2*omega_0_val/3

print()
print("Friedmann friction analysis (parametric in H):")
print(f"  omega_0 = {omega_0_val:.1f}")
print(f"  Overdamped threshold: H > 2*omega_0/3 = {H_cross:.1f}")
print()

# Table of H values
H_table = [0.01*omega_0_val, 0.1*omega_0_val, 0.5*omega_0_val,
           omega_0_val, 2*omega_0_val, 10*omega_0_val, 100*omega_0_val,
           1000*omega_0_val]
print(f"{'H/omega_0':>12} {'H':>12} {'regime':>12} {'dt_transit':>14} {'Shortfall':>12}")
print("-" * 65)
for H in H_table:
    gamma = 3*H/2
    if gamma > omega_0_val:
        regime = "overdamped"
        dt = BCS_window * 3*H*M_ATDHFB / dS_fold
    else:
        regime = "underdamped"
        corr = 1 + (gamma/omega_0_val)**2
        dt = dt_transit_ATDHFB * corr
    sf = tau_BCS / dt
    print(f"  {H/omega_0_val:>10.3f} {H:>12.1f} {regime:>12} {dt:>14.6f} {sf:>12.0f}")

print()

# For H at the Planck scale (M_KK = M_Pl): H ~ 289
# 3*H/(2*omega_0) = 3*289/(2*433) = 1.00 -- RIGHT AT THE BOUNDARY
# This is NOT a coincidence: both H and omega_0 are set by the same
# energy scale (S_fold * M_KK^4 / M_Pl^2 and V''/M).

# For the REALISTIC case: during exflation, H is set by the spectral
# action energy density. Let's compute H from the Friedmann equation.
#
# H^2 = rho / (3*M_Pl^2)
# rho = (1/2)*M*dot{tau}^2 + V(tau)  (homogeneous, no gradient energy)
# V = S(tau) in spectral action units
#
# But S(tau) is dimensionless in the NCG convention. The physical energy
# density requires multiplying by Lambda^4/(16*pi^2) where Lambda is the
# spectral action cutoff. In Connes-Chamseddine:
# S = Tr[f(D^2/Lambda^2)] ~ f_0*Lambda^4*a_0 + f_2*Lambda^2*a_2 + ...
# where f_0, f_2 are moments of the cutoff function f.
#
# The RATIO H/omega_0 does not depend on the overall normalization because:
# H^2 ~ S(tau) / M_Pl^2 and omega_0^2 = d2S/dtau2 / M.
# H/omega_0 = sqrt(S * M / (3*M_Pl^2*d2S)) = sqrt(M*S / (3*d2S)) * 1/(M_Pl/M_KK)
#
# In KK units:
# H/omega_0 = sqrt(M*S / (3*d2S)) / (M_Pl/M_KK)
# = sqrt(1.695 * 250361 / (3 * 317863)) / (M_Pl/M_KK)
# = sqrt(0.4459) / (M_Pl/M_KK)
# = 0.6678 / (M_Pl/M_KK)

ratio_H_omega = np.sqrt(M_ATDHFB * S_fold / (3 * d2S_fold))
print(f"H/omega_0 = {ratio_H_omega:.4f} / (M_Pl/M_KK)")
print()
print("For different KK scales:")
for name, r in [("M_KK = M_Pl", 1), ("M_KK = 10^{16} GeV (GUT)", 1e3),
                ("M_KK = 10^{13} GeV (seesaw)", 1e6),
                ("M_KK = 1 TeV", 1.22e16)]:
    H_over_omega = ratio_H_omega / r
    gamma_over_omega = 3*H_over_omega/2
    if gamma_over_omega > 1:
        regime = "OVERDAMPED"
        dt = BCS_window * 3*H_over_omega*omega_0_val*M_ATDHFB / dS_fold
    else:
        regime = "underdamped"
        corr = 1 + gamma_over_omega**2
        dt = dt_transit_ATDHFB * corr
    sf = tau_BCS / dt
    print(f"  {name:30s}: H/omega = {H_over_omega:.2e}, 3H/2omega = {gamma_over_omega:.2e}, "
          f"regime = {regime}, shortfall = {sf:.0f}")

print()

# KEY RESULT: Only at M_KK ~ M_Pl is Friedmann friction strong enough
# to potentially overdamp the transit. At lower M_KK, friction is negligible.

# For M_KK = M_Pl: 3H/(2*omega_0) = 3*0.668/2 = 1.00
# EXACTLY at the overdamped boundary!
# In the overdamped regime:
# dt = BCS_window * 3*H*M / V' = 0.03 * 3*H*1.695/58673
# where H = 0.668*omega_0 = 0.668*433 = 289

H_Pl = ratio_H_omega * omega_0_val  # H at M_KK = M_Pl
dt_Friedmann_Pl = BCS_window * 3*H_Pl*M_ATDHFB / dS_fold
shortfall_Friedmann_best = tau_BCS / dt_Friedmann_Pl

print("=" * 70)
print("FRIEDMANN FRICTION RESULT (M_KK = M_Pl)")
print("=" * 70)
print(f"H = {H_Pl:.1f} (KK units)")
print(f"3H/(2*omega_0) = {3*H_Pl/(2*omega_0_val):.3f}")
print(f"dt_transit (Friedmann) = {dt_Friedmann_Pl:.6f}")
print(f"Shortfall (Friedmann) = {shortfall_Friedmann_best:.0f}")
print(f"Improvement over S36: {shortfall_original/shortfall_Friedmann_best:.2f}x")
print()

# ============================================================
# 4. COMBINED ASSESSMENT
# ============================================================
print("=" * 70)
print("COMBINED ASSESSMENT: TAU-DYN-REOPEN-42")
print("=" * 70)
print()

# Mechanism (a): Direct inertial -- ATDHFB inertia lower than G_DeWitt, makes it WORSE
factor_a = shortfall_direct / shortfall_original
print(f"(a) Direct inertial:        {shortfall_direct:.0f}  ({factor_a:.2f}x vs S36, WORSE)")

# Mechanism (b): TV renormalization -- negligible
factor_b_relative = 1 / np.sqrt(1 + delta_M_over_M_converged)
shortfall_TV = shortfall_direct * factor_b_relative
print(f"(b) TV renormalization:     {shortfall_TV:.0f}  (delta_M/M = {delta_M_over_M_converged:.2e}, NEGLIGIBLE)")

# Mechanism (c): Friedmann friction -- at most O(1) at M_KK = M_Pl
print(f"(c) Friedmann (M_KK=M_Pl):  {shortfall_Friedmann_best:.0f}  ({shortfall_original/shortfall_Friedmann_best:.2f}x improvement)")
print()

# Best case: combine TV + Friedmann at M_KK = M_Pl
# The Friedmann friction gives dt_transit ~ 0.03*3*289*1.695/58673 = 0.000742
# Wait, let me recompute:
dt_best = BCS_window * 3 * H_Pl * M_ATDHFB / dS_fold
shortfall_best = tau_BCS / dt_best
print(f"Best case (Friedmann at M_KK=M_Pl): dt = {dt_best:.6f}, shortfall = {shortfall_best:.0f}")
print()

# CRITICAL CHECK: Is the Friedmann friction even applicable?
# The S36 calculation used the SPECTRAL ACTION GRADIENT as the force.
# With Friedmann friction, the relevant equation is:
# M*ddot{tau} + 3H*M*dot{tau} + dS/dtau = 0
#
# In the overdamped limit:
# 3H*M*dot{tau} ~ -dS/dtau
# dot{tau} ~ -dS/(3*H*M*dtau)
#
# The transit time across the BCS window (delta_tau = 0.03) is:
# dt = delta_tau / |dot{tau}| = delta_tau * 3*H*M / |dS/dtau|
#    = 0.03 * 3*289*1.695 / 58673 = 0.03 * 1469.4 / 58673 = 0.000751
#
# Compare to S36 free-fall: dt = 0.00113
# Friedmann at M_KK=M_Pl is actually FASTER (by 1.5x)!
# Wait, that's because the S36 calculation included the FULL dynamics
# (acceleration from rest, not terminal velocity).
# In free fall from rest: v = sqrt(2*dS*delta_tau/M)
# dt ~ delta_tau / v = sqrt(M*delta_tau/(2*dS))
# = sqrt(1.695*0.03/(2*58673)) = sqrt(1.695*0.03/117346) = sqrt(4.33e-7) = 6.58e-4
# S36 got 0.00113 (uses G=5 and includes curvature effects).

# With ATDHFB inertia and free fall:
dt_freefall_ATDHFB = np.sqrt(2 * M_ATDHFB * BCS_window / dS_fold) * BCS_window / np.sqrt(2*BCS_window)
# More precisely: for constant force F = dS, starting from rest:
# tau(t) = (1/2)*(F/M)*t^2
# t_transit = sqrt(2*M*delta_tau/F) = sqrt(2*M*BCS_window/dS_fold)
dt_freefall = np.sqrt(2 * M_ATDHFB * BCS_window / dS_fold)
print(f"Free-fall (constant force, ATDHFB): dt = {dt_freefall:.6f}")
print(f"Free-fall shortfall: {tau_BCS/dt_freefall:.0f}")
print()

# For overdamped: dt = delta_tau * 3H*M / dS = 0.03*3*289*1.695/58673
dt_od = BCS_window * 3 * H_Pl * M_ATDHFB / dS_fold
print(f"Overdamped (M_KK=M_Pl):    dt = {dt_od:.6f}")
print(f"Overdamped shortfall: {tau_BCS/dt_od:.0f}")
print()
print(f"Ratio overdamped/freefall: {dt_od/dt_freefall:.2f}")
print()

# The overdamped time CAN be longer if 3H*M/dS > sqrt(2*M/dS*delta_tau)
# i.e., 3H > sqrt(2*dS/(M*delta_tau)) = sqrt(2*58673/(1.695*0.03))
threshold = np.sqrt(2*dS_fold/(M_ATDHFB*BCS_window))
print(f"Overdamped longer than freefall if 3H > {threshold:.1f}")
print(f"3H_Pl = {3*H_Pl:.1f}")
print(f"3H > threshold? {3*H_Pl > threshold}")
print()

# So Friedmann friction AT the Planck scale barely helps:
# overdamped dt = 0.00075 vs freefall dt = 0.00058
# Factor ~ 1.3x longer, not enough.
#
# For MUCH stronger Hubble (H >> omega_0), overdamped dt ~ H/omega_0 * dt_freefall:
# Shortfall ~ shortfall_freefall * omega_0/H
# To get shortfall < 10: need H > shortfall_freefall * omega_0 / 10
# = 60000 * 433 / 10 = 2.6e6
# In KK units, H = 2.6e6 means rho ~ 9*M^2*H^2 ~ 9*1.695*(2.6e6)^2 ~ 10^{14}
# This is MUCH larger than S_fold = 250,361.
# So you'd need an energy density 10^14 / 250361 = 4e8 times the spectral action.
# This is not self-consistent.

H_needed = shortfall_original * omega_0_val / 10 * dS_fold / (3*M_ATDHFB*omega_0_val)
# Wait, let me be more precise.
# In the overdamped regime:
# dt = delta_tau * 3*H*M / dS
# shortfall = tau_BCS / dt = tau_BCS * dS / (delta_tau * 3*H*M)
# For shortfall = 10:
# H = tau_BCS * dS / (delta_tau * 3 * 10 * M)
H_for_10 = tau_BCS * dS_fold / (BCS_window * 3 * 10 * M_ATDHFB)
print(f"H needed for shortfall = 10: H = {H_for_10:.1f}")
print(f"H/omega_0 = {H_for_10/omega_0_val:.1f}")
print(f"Compare to H_Pl = {H_Pl:.1f}")
print(f"Ratio H_needed/H_Pl = {H_for_10/H_Pl:.0f}")
print()
print(f"Self-consistency: this H requires rho ~ 3*M_Pl^2*H^2 ~ {3*H_for_10**2:.1e}")
print(f"But the spectral action provides rho = S_fold = {S_fold:.0f}")
print(f"Ratio: {3*H_for_10**2/S_fold:.1f}")
print(f"NOT self-consistent: would need rho {3*H_for_10**2/S_fold:.0f}x larger than spectral action.")

print()

# ============================================================
# 5. FINAL VERDICT
# ============================================================
print("=" * 70)
print("FINAL VERDICT: TAU-DYN-REOPEN-42")
print("=" * 70)
print()

# Summary of all mechanisms:
# NOTE: The "free-fall from rest" estimate is NOT the correct physical scenario.
# The tau field rolls from tau >> tau_fold and arrives at the BCS window with
# high velocity. The correct transit time scales as sqrt(M) for rolling fields.
# The S36 calculation used the rolling scenario; we correct M from G_DeWitt to M_ATDHFB.
# Free-fall-from-rest at the BCS edge is an UPPER BOUND and not physically realized.
shortfall_results = {
    'S36 original (G=5)': shortfall_original,
    'ATDHFB rolling': shortfall_direct,
    'TV renormalization': shortfall_TV,
    'Friedmann (M_KK=M_Pl)': shortfall_Friedmann_best,
}

best_shortfall = min(shortfall_results.values())
best_name = min(shortfall_results, key=shortfall_results.get)

for name, sf in shortfall_results.items():
    marker = " <-- BEST" if sf == best_shortfall else ""
    print(f"  {name:35s}: shortfall = {sf:>10.0f}{marker}")

print()
print(f"Best achievable shortfall: {best_shortfall:.0f} ({best_name})")
print(f"Original S36 shortfall: {shortfall_original:.0f}")
print(f"Net improvement: {shortfall_original/best_shortfall:.2f}x")
print()

# Gate classification
if best_shortfall < 10:
    verdict = "PASS"
    print(f"GATE VERDICT: PASS (shortfall {best_shortfall:.0f} < 10)")
elif best_shortfall > 1000:
    verdict = "FAIL"
    print(f"GATE VERDICT: FAIL (shortfall {best_shortfall:.0f} > 1000)")
else:
    verdict = "INTERMEDIATE"
    print(f"GATE VERDICT: INTERMEDIATE ({best_shortfall:.0f} between 10 and 1000)")

print()
print("TAU-DYN-36 REMAINS CLOSED.")
print()
print("Physical reasons:")
print("1. Z(tau) multiplies (nabla tau)^2 which vanishes for homogeneous evolution.")
print("   Spatial stiffness does not slow homogeneous transit.")
print("2. TV mass renormalization is negligible (delta_M/M ~ 10^{-10})")
print("   because c_fabric = 210 makes virtual excitation of fabric modes costly.")
print("3. Friedmann friction requires H >> omega_0 (by factor ~5000x) to bring")
print("   the shortfall below 10. Self-consistent H is at most ~ omega_0,")
print("   which provides only ~1.3x improvement.")
print(f"4. The original 38,600x shortfall is reduced to at most {best_shortfall:.0f}x.")
print("   This is a {:.1f}x improvement, leaving 4+ orders of magnitude.".format(
    shortfall_original/best_shortfall))

# ============================================================
# 6. SAVE RESULTS
# ============================================================
np.savez(
    base / "s42_tau_dyn_reopening.npz",
    # Input parameters
    tau_fold=tau_fold,
    Z_fold=Z_fold,
    dS_fold=dS_fold,
    d2S_fold=d2S_fold,
    S_fold=S_fold,
    G_DeWitt=G_DeWitt,
    M_ATDHFB=M_ATDHFB,
    c_fabric=c_fabric,
    tau_BCS=tau_BCS,
    BCS_window=BCS_window,
    omega_0=omega_0_val,

    # Mechanism (a): Direct inertial
    correction_ATDHFB=correction_ATDHFB,
    dt_transit_ATDHFB=dt_transit_ATDHFB,
    shortfall_direct=shortfall_direct,

    # Mechanism (b): TV renormalization
    V3_fold=V3,
    anharm_param=anharm,
    U_max_TV=U_max,
    I_BO_UV=I_BO,
    I_BO_full=I_BO_full,
    I_BO_exact=I_BO_exact,
    delta_M_over_M=delta_M_over_M_converged,
    shortfall_TV=shortfall_TV,

    # Mechanism (c): Friedmann friction
    H_Pl=H_Pl,
    ratio_H_omega=ratio_H_omega,
    dt_Friedmann_Pl=dt_Friedmann_Pl,
    shortfall_Friedmann_Pl=shortfall_Friedmann_best,
    H_for_shortfall_10=H_for_10,

    # Summary
    shortfall_original=shortfall_original,
    shortfall_best=best_shortfall,
    improvement_factor=shortfall_original/best_shortfall,

    # Freefall with ATDHFB
    dt_freefall_ATDHFB=dt_freefall,
    shortfall_freefall_ATDHFB=tau_BCS/dt_freefall,

    # H scan
    H_scan=H_values,
    shortfall_H_scan=shortfall_H,

    # Verdict
    verdict=np.array([verdict]),
    gate_name=np.array(['TAU-DYN-REOPEN-42']),
)

print()
print(f"Results saved to {base / 's42_tau_dyn_reopening.npz'}")

# ============================================================
# 7. PLOT
# ============================================================
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel 1: Transit timescale mechanisms
ax = axes[0, 0]
mechanisms = ['S36\n(G=5)', 'ATDHFB\nrolling', 'TV\nrenorm', 'Friedmann\n(M_KK=M_Pl)']
shortfalls = [shortfall_original, shortfall_direct, shortfall_TV,
              shortfall_Friedmann_best]
colors = ['#888888', '#cc4444', '#cc4444', '#cc4444']
bars = ax.bar(range(len(mechanisms)), shortfalls, color=colors, edgecolor='black', linewidth=0.5)
ax.set_yscale('log')
ax.set_ylabel('Shortfall (tau_BCS / tau_transit)')
ax.set_xticks(range(len(mechanisms)))
ax.set_xticklabels(mechanisms, fontsize=8)
ax.axhline(y=10, color='green', linestyle='--', linewidth=2, label='PASS threshold (10)')
ax.axhline(y=1000, color='orange', linestyle='--', linewidth=1.5, label='FAIL threshold (1000)')
ax.axhline(y=1, color='blue', linestyle=':', linewidth=1, label='Unity')
ax.set_title('TAU-DYN Shortfall by Mechanism')
ax.legend(loc='upper right', fontsize=7)
ax.set_ylim(1, 1e6)
for i, sf in enumerate(shortfalls):
    ax.text(i, sf*1.5, f'{sf:.0f}', ha='center', va='bottom', fontsize=8, fontweight='bold')

# Panel 2: Friedmann friction scan
ax = axes[0, 1]
ax.loglog(H_values/omega_0_val, shortfall_H, 'b-', linewidth=1.5)
ax.axhline(y=10, color='green', linestyle='--', linewidth=2, label='PASS (10)')
ax.axhline(y=1000, color='orange', linestyle='--', linewidth=1.5, label='FAIL (1000)')
ax.axhline(y=shortfall_original, color='gray', linestyle=':', label=f'S36 original ({shortfall_original:.0f})')
ax.axvline(x=2/3, color='red', linestyle=':', alpha=0.7, label='Overdamped boundary')
ax.axvline(x=ratio_H_omega, color='purple', linestyle='-.', alpha=0.7, label=f'H(M_KK=M_Pl)/omega_0={ratio_H_omega:.2f}')
ax.set_xlabel('H / omega_0')
ax.set_ylabel('Shortfall')
ax.set_title('Friedmann Friction vs Shortfall')
ax.legend(loc='upper right', fontsize=7)
ax.set_xlim(1e-3, 1e4)
ax.set_ylim(1, 1e6)

# Panel 3: Z(tau) and dS/dtau
ax = axes[1, 0]
ax.plot(tau_grid, Z_spec, 'b-o', label='Z_spectral(tau)', markersize=4)
ax.plot(tau_grid, dS_arr, 'r-s', label='|dS/dtau|(tau)', markersize=4)
ax.axvline(x=0.19, color='gray', linestyle='--', alpha=0.5, label='fold')
ax.fill_between([0.175, 0.205], 0, 120000, alpha=0.1, color='green', label='BCS window')
ax.set_xlabel('tau')
ax.set_ylabel('Value (spectral action units)')
ax.set_title('Z(tau) vs |dS/dtau|')
ax.legend(loc='upper left', fontsize=8)
ax.set_ylim(0, 120000)

# Panel 4: TV integral convergence
ax = axes[1, 1]
u_vals = np.linspace(0, 5, 500)
integrand_vals = u_vals**2 / (1 + u_vals**2)**2.5
cumulative = np.cumsum(integrand_vals) * (u_vals[1]-u_vals[0])
ax.plot(u_vals, integrand_vals, 'b-', linewidth=1.5, label='u^2/(1+u^2)^{5/2}')
ax.plot(u_vals, cumulative, 'r--', linewidth=1.5, label='Cumulative integral')
ax.axvline(x=U_max, color='green', linestyle=':', linewidth=2, label=f'U_max = c/omega_0 = {U_max:.3f}')
ax.axhline(y=I_BO_exact, color='gray', linestyle=':', alpha=0.5, label=f'pi/8 = {I_BO_exact:.4f}')
ax.set_xlabel('u = c*k / omega_0')
ax.set_ylabel('Integrand / Integral')
ax.set_title('TV Mass Renormalization Integral (3D)')
ax.legend(loc='right', fontsize=7)
ax.set_xlim(0, 5)

plt.suptitle('TAU-DYN-REOPEN-42: Fabric Gradient Stiffness Cannot Reopen TAU-DYN-36\n'
             f'Best shortfall = {best_shortfall:.0f} (vs original {shortfall_original:.0f}). '
             f'VERDICT: {verdict}',
             fontsize=12, fontweight='bold', y=1.02)

plt.tight_layout()
plt.savefig(base / "s42_tau_dyn_reopening.png", dpi=150, bbox_inches='tight')
print(f"Plot saved to {base / 's42_tau_dyn_reopening.png'}")

print()
print("DONE.")
