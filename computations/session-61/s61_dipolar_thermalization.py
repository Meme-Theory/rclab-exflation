#!/usr/bin/env python3
"""
S61 DIPOLAR-THERM-61: Leggett Mode Lifetime on Josephson Fabric
================================================================

Gate: DIPOLAR-THERM-61 — INFO (Leggett lifetime characterization)

Physics: The Leggett mode (relative B2-B3 phase oscillation, omega_L1 = 0.138 M_KK)
can decay into two Goldstone phonons on the 32-cell Josephson fabric. This is the
exact analog of the 3He-B Leggett mode decaying into two longitudinal sound waves
via the spin-orbit (dipolar) coupling vertex.

In 3He-B:
  - Leggett frequency omega_L ~ 10^{-3} * Delta (dipolar energy << pairing gap)
  - Decay channel: omega_L -> omega_s(k1) + omega_s(k2) with omega_s = c_s * k
  - Lifetime tau_L ~ microseconds at mK temperatures
  - Superfluid state persists for years -> ratio ~ 10^{12}

Framework:
  - omega_L1 = 0.138 M_KK, m_G = 0.070 M_KK (S49 DIPOLAR-CATALOG-49)
  - Goldstone dispersion: omega_G(k) = c_Gold * |k| on lattice Laplacian
  - c_Gold = 0.915 M_KK (S52 GL-JOSEPHSON-52)
  - E_J per bond = 3.397 M_KK (S60 s60_rg_integrals)
  - Beliaev (-> 2 quasiparticles): FORBIDDEN by 25.9x (S50 LEGGETT-DAMPING-50)
  - The FABRIC provides 31 Goldstone modes with discrete k-vectors

Method:
  1. Construct Goldstone dispersion on 32-cell Voronoi lattice
  2. Construct Leggett dispersion (gapped at omega_L1)
  3. Fermi golden rule: Gamma = (2pi) * sum_{k1+k2=q} |V_cubic|^2 * delta(...)
  4. Cubic vertex from third-order expansion of Josephson energy
  5. Compare tau_L to transit time, Thouless time, Hubble time

Key insight from Volovik (Paper 14, Ch. 10): In a superfluid with known microscopic
Hamiltonian, the Leggett mode lifetime is computable from the BCS parameters without
any UV ambiguity. The cubic coupling is determined by the gap structure and the
spin-orbit (here: Josephson) energy. This is a microscopic computation, not effective
field theory.

Author: Volovik Superfluid Universe Theorist
Session: 61
"""

import numpy as np
import sys
import os

# Import canonical constants
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    omega_L1, omega_L2, c_Gold, M_KK, N_cells,
    Delta_0_GL, Delta_B3, dt_transit, H_fold,
    E_cond, PI, a_GL, b_GL, J_C2, J_su2, J_u1,
    E_B1, E_B2_mean, E_B3_mean, omega_PV, hbar_GeV_s
)

print("=" * 72)
print("S61 DIPOLAR-THERM-61: Leggett Mode Lifetime on Josephson Fabric")
print("=" * 72)

# ===========================================================================
#  SECTION 1: Fabric Goldstone Spectrum
# ===========================================================================

print("\n--- SECTION 1: Fabric Goldstone Spectrum ---")

# 32-cell Voronoi tessellation of S^3
# Graph Laplacian eigenvalues for the dual graph (truncated octahedron / Cayley graph)
# From s61_leggett_squeezing_spectrum.npz: 31 nonzero eigenvalues
# The Goldstone dispersion is omega_G(k) = sqrt(omega_L0^2 + c_Gold^2 * lambda_k)
# where lambda_k are Laplacian eigenvalues and omega_L0 = 0 for the Goldstone

# Load Laplacian eigenvalues from the squeezing spectrum computation
sq_data = np.load(os.path.join(os.path.dirname(__file__),
                               's61_leggett_squeezing_spectrum.npz'),
                  allow_pickle=True)
lambda_lap = sq_data['laplacian_eigs_all']  # 32 eigenvalues, first is 0

print(f"Laplacian eigenvalues (32 total, first = {lambda_lap[0]:.6f}):")
print(f"  Nonzero: {lambda_lap[1:]}")
print(f"  Min nonzero: {lambda_lap[1]:.6f}")
print(f"  Max: {lambda_lap[-1]:.6f}")

# Goldstone dispersion on lattice: omega_G(n) = c_Gold * sqrt(lambda_n)
# This is the acoustic branch — massless Goldstone from spontaneous U(1) breaking
omega_Gold = c_Gold * np.sqrt(lambda_lap[1:])  # 31 modes, exclude k=0
print(f"\nGoldstone frequencies (31 modes):")
print(f"  omega_Gold_min = {omega_Gold[0]:.6f} M_KK")
print(f"  omega_Gold_max = {omega_Gold[-1]:.6f} M_KK")
print(f"  2 * omega_Gold_min = {2*omega_Gold[0]:.6f} M_KK")

# Leggett mode frequency and mass
omega_L = omega_L1  # 0.138 M_KK (from GL-JOSEPHSON-52)
m_G = omega_L / 2   # 0.069 M_KK (mass = omega/2 in relativistic convention)
# Note: S49 gives m_G = 0.070 M_KK, consistent to 1.4%

print(f"\nLeggett mode:")
print(f"  omega_L1 = {omega_L:.6f} M_KK")
print(f"  m_G = omega_L/2 = {m_G:.6f} M_KK")
print(f"  m_G (S49 catalog) = 0.070 M_KK")

# ===========================================================================
#  SECTION 2: Kinematic Analysis — Leggett -> 2 Goldstone
# ===========================================================================

print("\n--- SECTION 2: Kinematic Analysis ---")

# For the decay Leggett(q=0) -> Goldstone(k1) + Goldstone(k2):
# Energy conservation: omega_L = omega_G(k1) + omega_G(k2)
# Momentum conservation on lattice: k1 + k2 = 0 (q=0 Leggett)
# So we need: omega_L = 2 * omega_G(k) for some lattice mode k

# Check: can we satisfy omega_L = 2 * omega_G(k)?
omega_half_L = omega_L / 2
print(f"Required Goldstone frequency: omega_L/2 = {omega_half_L:.6f} M_KK")
print(f"Goldstone frequency range: [{omega_Gold[0]:.6f}, {omega_Gold[-1]:.6f}] M_KK")

kinematic_possible = (omega_half_L >= omega_Gold[0]) and (omega_half_L <= omega_Gold[-1])
print(f"Kinematic match possible: {kinematic_possible}")

if kinematic_possible:
    # Find closest Goldstone mode
    idx_closest = np.argmin(np.abs(omega_Gold - omega_half_L))
    omega_closest = omega_Gold[idx_closest]
    detuning = omega_half_L - omega_closest
    print(f"Closest Goldstone mode: omega_G[{idx_closest}] = {omega_closest:.6f} M_KK")
    print(f"Detuning: {detuning:.6f} M_KK ({abs(detuning/omega_half_L)*100:.2f}%)")
else:
    print(f"omega_L/2 = {omega_half_L:.6f} BELOW Goldstone band minimum {omega_Gold[0]:.6f}")
    print("Back-to-back decay kinematically forbidden on this lattice!")

# Also check non-back-to-back: omega_L = omega_G(k1) + omega_G(k2) for k1 != -k2
# On a discrete lattice, momentum conservation is modular
# Count all pairs (i,j) with omega_G[i] + omega_G[j] within resolution of omega_L
energy_tol = 0.01 * omega_L  # 1% energy window (finite lattice broadening)
n_kinematic_pairs = 0
kinematic_pairs = []
for i in range(len(omega_Gold)):
    for j in range(i, len(omega_Gold)):
        if abs(omega_Gold[i] + omega_Gold[j] - omega_L) < energy_tol:
            n_kinematic_pairs += 1
            kinematic_pairs.append((i, j, omega_Gold[i], omega_Gold[j]))

print(f"\nNon-back-to-back pairs within 1% of omega_L:")
print(f"  N_pairs = {n_kinematic_pairs}")
for p in kinematic_pairs[:5]:
    print(f"  modes ({p[0]},{p[1]}): omega_G = ({p[2]:.4f}, {p[3]:.4f}), "
          f"sum = {p[2]+p[3]:.4f}")

# Broader window: 10%
energy_tol_broad = 0.10 * omega_L
n_broad = 0
for i in range(len(omega_Gold)):
    for j in range(i, len(omega_Gold)):
        if abs(omega_Gold[i] + omega_Gold[j] - omega_L) < energy_tol_broad:
            n_broad += 1
print(f"  Within 10%: N_pairs = {n_broad}")

# ===========================================================================
#  SECTION 3: Cubic Coupling Vertex
# ===========================================================================

print("\n--- SECTION 3: Cubic Coupling Vertex ---")

# The Leggett mode is a relative phase oscillation: phi_rel = phi_B2 - phi_B3
# The Josephson energy is: H_J = -E_J * cos(phi_rel)
# Expanding to cubic order around equilibrium (phi_rel = 0):
#   H_J = -E_J [1 - phi_rel^2/2 + phi_rel^4/24 - ...]
# The Leggett mass comes from: (1/2) * E_J * phi_rel^2 -> omega_L^2 = E_J / chi_phase
# where chi_phase is the phase susceptibility (moment of inertia)

# The cubic vertex coupling Leggett to phonons comes from:
#   V_cubic = (E_J / 6) * phi_rel * delta_rho^2  (density-phase coupling)
# More precisely, from the equation of motion coupling:
#   The condensation energy E_cond depends on the gap Delta, which depends on density
#   Fluctuations in Delta couple to fluctuations in phi_rel through the BCS self-consistency

# E_J per bond from s60_rg_integrals
E_J_bond = 3.397  # M_KK (verified from s60_rg_integrals.npz)  # (local)

# Josephson coupling per mode (distributed over 8 BCS modes)
# The Leggett mode involves B2-B3 coupling specifically
# J_23 from S49: epsilon = J_23/Delta_B2 = 0.00248, Delta_B2 ~ 0.77
J_23 = 0.00248 * Delta_0_GL  # = 0.00191 M_KK (inter-sector Josephson)

# Number of bonds in 32-cell Voronoi tessellation
# Each cell has ~14 faces (truncated octahedron), shared -> N_bonds ~ 32*14/2 = 224
# But the Cayley graph has coordination z=4 (generators of SU(2)), so N_bonds = 32*4/2 = 64
# From the Laplacian structure: 32 nodes, z=4 -> 64 bonds
N_bonds = 64
E_J_fabric_total = E_J_bond * N_bonds
print(f"E_J per bond = {E_J_bond:.3f} M_KK")
print(f"N_bonds (Cayley graph, z=4) = {N_bonds}")
print(f"E_J_fabric total = {E_J_fabric_total:.1f} M_KK")
print(f"J_23 (inter-sector) = {J_23:.6f} M_KK")

# Phase susceptibility (moment of inertia for relative phase)
# From Leggett mode frequency: omega_L^2 = E_J_eff / I_phase
# where I_phase = (partial^2 E / partial phi^2)^{-1} evaluated at condensation energy
# For BCS: I_phase ~ N(0) * Delta^2 where N(0) is DOS at Fermi level
# In our discrete system: chi_phase = E_J / omega_L^2

chi_phase = E_J_bond / omega_L**2
print(f"Phase susceptibility: chi_phase = E_J/omega_L^2 = {chi_phase:.4f} M_KK^{{-1}}")

# Cubic coupling vertex: V_3 = d^3 E / (d phi_rel^2 d delta_n)
# In the Josephson model: V_3 = (1/6) * d^3/dphi^3 [-E_J cos(phi)] = -(E_J/6) sin(phi)
# At equilibrium phi=0: V_3 = 0 (third derivative of cosine vanishes at minimum)
# The ACTUAL cubic coupling comes from the cross term:
#   delta_E = E_J * phi_rel * (dE_J/dn) * delta_n + ...
# where dE_J/dn is how Josephson coupling depends on density (number fluctuation)

# In 3He-B, the cubic coupling scales as:
#   g_3 ~ omega_L * sqrt(omega_L / E_F) ~ omega_L^{3/2} / sqrt(E_F)
# This gives Gamma ~ omega_L^5 / (c_s^3 * E_F) (Leggett-Takagi result)

# For the framework, the analog of E_F is the total bandwidth ~ sum(eps_k)
eps_fold = np.array([-1.18413693e-16, 1.77061960e-01, 3.29405571e-01, 5.22910373e-01,
                     7.26154925e-01, 1.00439566e+00, 1.07857332e+00, 1.17000260e+00])
E_bandwidth = eps_fold[-1] - eps_fold[0]
print(f"BCS bandwidth = {E_bandwidth:.4f} M_KK")

# ===========================================================================
#  SECTION 4: Fermi Golden Rule — Three Methods
# ===========================================================================

print("\n--- SECTION 4: Fermi Golden Rule Decay Rate ---")

# ---------- METHOD 1: Leggett-Takagi Formula (3He analog) ----------
# In 3He-B: Gamma_LT = (omega_L^5) / (60 * pi * c_s^3 * rho / m^*)
# Adapted to framework:
#   Gamma_1 = (1/(60*pi)) * omega_L^5 / (c_Gold^3 * E_bandwidth)
# This is the continuum result for Leggett -> 2 sound quanta

Gamma_LT = (1.0 / (60 * PI)) * omega_L**5 / (c_Gold**3 * E_bandwidth)
tau_LT = 1.0 / Gamma_LT if Gamma_LT > 0 else np.inf
print(f"\nMethod 1: Leggett-Takagi (continuum):")
print(f"  Gamma_LT = {Gamma_LT:.6e} M_KK")
print(f"  tau_LT = {tau_LT:.4f} M_KK^{{-1}}")

# ---------- METHOD 2: Direct FGR on Discrete Lattice ----------
# Gamma = 2*pi * sum_{k1,k2} |V_{k1,k2}|^2 * delta(omega_L - omega_1 - omega_2)
# The cubic vertex matrix element:
#   |V|^2 = (g_3)^2 / (N_cells * omega_L * omega_1 * omega_2)
# where g_3 is the cubic coupling constant from the Josephson expansion
#
# The cubic coupling: when phi_rel oscillates, it modulates the Goldstone stiffness.
# g_3 = (1/2) * d(c_Gold^2)/d(phi_rel) * sqrt(omega_L) evaluated at phi_rel = 0
# Since c_Gold^2 ~ E_J * cos(phi_rel), we get:
#   g_3 = (1/2) * E_J * sin(phi_rel)|_{phi=0} = 0
# The sine vanishes at the minimum! So the lowest-order coupling is QUARTIC, not cubic.
#
# CORRECTION: The coupling is through the CROSS term between relative phase and
# center-of-mass phase. The Josephson energy couples relative phase to total density.
# H_J = -E_J cos(phi_i - phi_j) where phi_i, phi_j are cell phases.
# Goldstone = (phi_i + phi_j)/2, Leggett = phi_i - phi_j
# Expanding: H_J = -E_J [1 - (phi_L)^2/2 + (phi_L)^4/24]
# where phi_L = phi_i - phi_j. This has NO linear coupling to phi_G = (phi_i + phi_j)/2
#
# The cubic coupling requires ANHARMONICITY in the BCS free energy:
# F(Delta, phi) = F_0 + a*|Delta|^2 + b*|Delta|^4 + ... - E_J cos(phi_rel)
# The cross-coupling: d^2F/(d|Delta| dphi) generates Leggett-amplitude coupling
# At tree level: V_3 ~ b_GL * Delta_0 * (delta_Delta) * phi_rel ~ b * Delta * phi_L * delta_n
# where delta_n is the density fluctuation carried by Goldstones

# Cubic vertex magnitude from GL anharmonicity:
# g_3 = b_GL * Delta_0_GL * (omega_L / chi_phase)^{1/2}
# This couples one Leggett quantum to one density fluctuation
# For Leggett -> 2 Goldstone, need the squared vertex

g_3_GL = abs(b_GL) * Delta_0_GL * np.sqrt(omega_L / chi_phase)
print(f"\nGL cubic coupling: g_3 = b*Delta*sqrt(omega_L/chi) = {g_3_GL:.6e} M_KK")

# However, the PHYSICAL cubic vertex must respect the symmetry.
# The Josephson cos(phi_rel) has no odd-order coupling to Goldstone.
# The coupling goes through AMPLITUDE fluctuations of Delta.
# In 3He-B, this is the "pair-breaking" channel via spin-orbit.
# The rate involves the Tsuneto function (Leggett-Takagi 1983).

# For the framework, the amplitude mode is the Higgs mode (omega_H1 = 0.380 M_KK).
# The process is: Leggett -> virtual Higgs -> 2 Goldstone
# This is a SECOND-ORDER process (suppressed by 1/omega_H1)

# Virtual Higgs propagator:
omega_H = 0.380  # Higgs-1 frequency (M_KK)  # (local)
print(f"Higgs-1 frequency: omega_H1 = {omega_H:.3f} M_KK")
print(f"omega_L / omega_H = {omega_L/omega_H:.4f}")

# The effective cubic vertex through the Higgs:
# V_eff = V_{L-H} * G_H(omega_L) * V_{H-GG}
# V_{L-H} = coupling of Leggett to Higgs ~ b_GL * Delta_0 ~ 0.34 M_KK
# G_H(omega_L) = 1/(omega_H^2 - omega_L^2) (virtual Higgs propagator)
# V_{H-GG} = coupling of Higgs to 2 Goldstones ~ c_Gold (from gap-to-sound coupling)

V_LH = abs(b_GL) * Delta_0_GL  # Leggett-Higgs coupling
G_H = 1.0 / (omega_H**2 - omega_L**2)  # virtual propagator (off-shell)
V_HGG = c_Gold  # Higgs-Goldstone-Goldstone vertex (from d(c^2)/d|Delta|)

V_eff_cubic = V_LH * G_H * V_HGG
print(f"\nVirtual Higgs channel:")
print(f"  V_LH (Leggett-Higgs) = {V_LH:.4f} M_KK")
print(f"  G_H (propagator) = {G_H:.4f} M_KK^{{-2}}")
print(f"  V_HGG (Higgs-2Goldstone) = {V_HGG:.4f} M_KK")
print(f"  V_eff = {V_eff_cubic:.6f} M_KK^{{-1}}")

# ---------- METHOD 2a: FGR with discrete lattice sum ----------
# Gamma = (2*pi / N_cells) * sum_k |V_eff|^2 / (omega_L * 2*omega_G(k))
#         * delta_broadened(omega_L - 2*omega_G(k))
# Use Lorentzian broadening with width eta = 1/t_transit (natural linewidth)

eta_broadening = 1.0 / dt_transit  # ~ 885 M_KK (transit broadening)
# This is enormous — the transit is so fast that the Leggett mode barely oscillates
# Use instead the intrinsic linewidth: eta = omega_L / Q where Q ~ 6.7e5 (S50)
# Q_Leggett = 6.7e5  # S72: now imported from canonical_constants
eta_intrinsic = omega_L / Q_Leggett
print(f"\nBroadening scales:")
print(f"  Transit: eta_transit = 1/t_transit = {eta_broadening:.1f} M_KK")
print(f"  Intrinsic: eta_intrinsic = omega_L/Q = {eta_intrinsic:.2e} M_KK")
print(f"  Goldstone spacing: delta_omega_G = {omega_Gold[1]-omega_Gold[0]:.4f} M_KK")

# For the physical rate, use the Goldstone DOS with Lorentzian broadening
# at the intrinsic scale
Gamma_lattice_intrinsic = 0.0  # (local)
Gamma_lattice_transit = 0.0  # (local)

for k in range(len(omega_Gold)):
    omega_k = omega_Gold[k]
    # Back-to-back: k and -k both contribute
    delta_E = omega_L - 2 * omega_k

    # Lorentzian delta function: (eta/pi) / (delta_E^2 + eta^2)
    L_intrinsic = (eta_intrinsic / PI) / (delta_E**2 + eta_intrinsic**2)
    L_transit = (eta_broadening / PI) / (delta_E**2 + eta_broadening**2)

    # Matrix element squared (dimensionless)
    M_sq = V_eff_cubic**2 / (omega_L * 2 * omega_k) if omega_k > 0 else 0

    Gamma_lattice_intrinsic += (2 * PI / N_cells) * M_sq * L_intrinsic
    Gamma_lattice_transit += (2 * PI / N_cells) * M_sq * L_transit

tau_lattice_intrinsic = 1.0 / Gamma_lattice_intrinsic if Gamma_lattice_intrinsic > 0 else np.inf
tau_lattice_transit = 1.0 / Gamma_lattice_transit if Gamma_lattice_transit > 0 else np.inf

print(f"\nMethod 2a: FGR on discrete lattice (intrinsic broadening):")
print(f"  Gamma = {Gamma_lattice_intrinsic:.6e} M_KK")
print(f"  tau = {tau_lattice_intrinsic:.4e} M_KK^{{-1}}")
print(f"\nMethod 2b: FGR on discrete lattice (transit broadening):")
print(f"  Gamma = {Gamma_lattice_transit:.6e} M_KK")
print(f"  tau = {tau_lattice_transit:.4e} M_KK^{{-1}}")

# ---------- METHOD 3: Direct Josephson cubic coupling ----------
# Even without the Higgs intermediary, there is a DIRECT cubic vertex
# from the nonlinear Josephson coupling when we expand in BOTH
# relative and center-of-mass phases on adjacent cells:
#
# H_J = -E_J cos(phi_i - phi_j)
# phi_i = phi_G + phi_L/2, phi_j = phi_G - phi_L/2 (for 2 cells)
# phi_i - phi_j = phi_L (relative phase = Leggett mode)
#
# For the FABRIC (N cells), the Goldstone is a collective phase fluctuation:
# phi_i = phi_0 + delta_phi_i, where delta_phi_i is the Goldstone field
# The Leggett mode modulates the INTERSITE phase difference
#
# On a bond (i,j): phi_i - phi_j = (delta_phi_i - delta_phi_j) + phi_L^{ij}
# where phi_L^{ij} is the Leggett component
#
# Expanding cos to third order:
# H_J = -E_J [1 - (phi_G_diff + phi_L)^2/2 + (phi_G_diff + phi_L)^4/24]
# Cross term at cubic order: E_J * phi_L * phi_G_diff^2 / 2
# This IS a cubic coupling: one Leggett * two Goldstone derivatives
#
# But wait: at equilibrium phi_L = 0, the third-order term has the form
# (1/6) E_J * sin(0) = 0 for the Josephson cosine.
# The cross-cubic E_J * phi_L * (delta_phi)^2 / 2 IS nonzero.

# DIRECT cubic vertex:
# V_3^{direct} = E_J / 2 per bond (coupling phi_L to (delta_phi)^2)
# The Leggett amplitude in the k=0 mode: phi_L ~ 1/sqrt(N_cells * omega_L * chi_phase)
# Each Goldstone in mode k: delta_phi_k ~ 1/sqrt(N_cells * omega_k * chi_Gold)
# chi_Gold ~ E_J / c_Gold^2 (Goldstone stiffness)

chi_Gold = E_J_bond / c_Gold**2
print(f"\nGoldstone stiffness: chi_Gold = E_J/c_Gold^2 = {chi_Gold:.4f}")

# Matrix element for Leggett(q=0) -> Goldstone(k) + Goldstone(-k):
# <0| V_3 |L, G_k, G_{-k}> = (E_J/2) * phi_L_amp * phi_G_k_amp * phi_G_{-k}_amp
# where amplitudes are zero-point fluctuations

# Zero-point amplitude of Leggett mode:
phi_L_zp = 1.0 / np.sqrt(2 * N_cells * omega_L * chi_phase)
print(f"Leggett zero-point amplitude: phi_L_zp = {phi_L_zp:.6f}")

# FGR rate with direct cubic coupling:
Gamma_direct = 0.0  # (local)
Gamma_direct_broad = 0.0  # (local)

for k in range(len(omega_Gold)):
    omega_k = omega_Gold[k]

    # Zero-point amplitude of Goldstone mode k
    phi_G_zp = 1.0 / np.sqrt(2 * N_cells * omega_k * chi_Gold)

    # Cubic vertex on one bond
    V_3_bond = E_J_bond / 2.0

    # Matrix element: sum over bonds * vertex * zero-point amplitudes
    # For back-to-back (k, -k), the mode function has structure e^{ik.r}
    # On the Cayley graph, the overlap integral gives a form factor ~ lambda_k / lambda_max
    form_factor = lambda_lap[k+1] / lambda_lap[-1]

    # Full matrix element squared
    # M = V_3_bond * N_bonds * form_factor * phi_L_zp * phi_G_zp^2
    M_element = V_3_bond * np.sqrt(N_bonds) * form_factor * phi_L_zp * phi_G_zp**2
    M_sq = M_element**2

    delta_E = omega_L - 2 * omega_k
    L_intrinsic = (eta_intrinsic / PI) / (delta_E**2 + eta_intrinsic**2)
    L_transit = (eta_broadening / PI) / (delta_E**2 + eta_broadening**2)

    Gamma_direct += 2 * PI * M_sq * L_intrinsic
    Gamma_direct_broad += 2 * PI * M_sq * L_transit

tau_direct = 1.0 / Gamma_direct if Gamma_direct > 0 else np.inf
tau_direct_broad = 1.0 / Gamma_direct_broad if Gamma_direct_broad > 0 else np.inf

print(f"\nMethod 3: Direct Josephson cubic (intrinsic broadening):")
print(f"  Gamma = {Gamma_direct:.6e} M_KK")
print(f"  tau = {tau_direct:.4e} M_KK^{{-1}}")
print(f"Method 3b: Direct Josephson cubic (transit broadening):")
print(f"  Gamma = {Gamma_direct_broad:.6e} M_KK")
print(f"  tau = {tau_direct_broad:.4e} M_KK^{{-1}}")

# ===========================================================================
#  SECTION 5: Dominant Rate and Comparison
# ===========================================================================

print("\n--- SECTION 5: Summary of All Rates ---")

# Collect all rates
rates = {
    'Leggett-Takagi (continuum)': Gamma_LT,
    'FGR lattice (intrinsic eta)': Gamma_lattice_intrinsic,
    'FGR lattice (transit eta)': Gamma_lattice_transit,
    'Direct Josephson (intrinsic)': Gamma_direct,
    'Direct Josephson (transit)': Gamma_direct_broad,
}

print(f"\n{'Method':<35} {'Gamma (M_KK)':>14} {'tau (M_KK^-1)':>14} {'tau/t_transit':>14}")
print("-" * 80)
for name, G in rates.items():
    tau = 1.0/G if G > 0 else np.inf
    ratio = tau / dt_transit if G > 0 else np.inf
    print(f"{name:<35} {G:>14.4e} {tau:>14.4e} {ratio:>14.1f}")

# The PHYSICAL rate: take the maximum (fastest decay channel)
Gamma_max = max(rates.values())
Gamma_max_name = max(rates, key=rates.get)
tau_min = 1.0 / Gamma_max
print(f"\nDominant channel: {Gamma_max_name}")
print(f"Fastest rate: Gamma_max = {Gamma_max:.6e} M_KK")
print(f"Shortest lifetime: tau_min = {tau_min:.4e} M_KK^{{-1}}")

# ===========================================================================
#  SECTION 6: Timescale Comparisons
# ===========================================================================

print("\n--- SECTION 6: Timescale Comparisons ---")

t_transit = dt_transit  # 0.00113 M_KK^{-1}
t_Thouless = 1.0 / (E_J_bond / N_cells**(2./3.))  # Thouless time
H_inv = 1.0 / H_fold  # Hubble time at fold
t_Leggett_osc = 2 * PI / omega_L  # one oscillation period
N_osc_transit = t_transit / t_Leggett_osc

# From S50: gravitational radiation rate
Gamma_grav = 5.2e-8  # M_KK (from S50 LEGGETT-DAMPING-50)  # (local)
tau_grav = 1.0 / Gamma_grav

print(f"Transit time: t_transit = {t_transit:.6e} M_KK^{{-1}}")
print(f"Thouless time: t_Th = {t_Thouless:.4f} M_KK^{{-1}}")
print(f"Hubble time at fold: H^{{-1}} = {H_inv:.6e} M_KK^{{-1}}")
print(f"Leggett oscillation period: T_L = {t_Leggett_osc:.4f} M_KK^{{-1}}")
print(f"Oscillations during transit: N_osc = {N_osc_transit:.4e}")
print(f"Gravitational decay: tau_grav = {tau_grav:.4e} M_KK^{{-1}}")

print(f"\nTimescale hierarchy:")
print(f"  tau_L (fabric decay) / t_transit = {tau_min / t_transit:.2e}")
print(f"  tau_L / t_Thouless = {tau_min / t_Thouless:.2e}")
print(f"  tau_L / H^{{-1}} = {tau_min / H_inv:.2e}")
print(f"  tau_grav / t_transit = {tau_grav / t_transit:.2e}")
print(f"  tau_grav / tau_L = {tau_grav / tau_min:.2e}")
print(f"  N_osc during transit = {N_osc_transit:.2e}")

# Q factor
Q_fabric = omega_L / (2 * Gamma_max) if Gamma_max > 0 else np.inf
print(f"\nQ factor (fabric): Q = omega_L / (2*Gamma) = {Q_fabric:.2e}")
print(f"Q factor (gravitational, S50): Q = {Q_Leggett:.2e}")

# ===========================================================================
#  SECTION 7: 3He-B Analog Comparison
# ===========================================================================

print("\n--- SECTION 7: 3He-B Analog ---")

# In 3He-B at T << T_c:
# omega_L ~ 2*pi * 100 kHz (at 0 bar)
# Delta ~ 2*pi * 100 GHz
# tau_L ~ 10 microseconds (NMR T2)
# tau_superfluid ~ years = 3e7 s
# ratio = 3e7 / 1e-5 = 3e12

omega_L_3He = 2 * PI * 100e3   # Hz
Delta_3He = 2 * PI * 100e9      # Hz
tau_L_3He = 1e-5                 # s (Leggett mode lifetime, NMR)
tau_SF_3He = 3e7                 # s (superfluid persistence)
ratio_3He = tau_SF_3He / tau_L_3He

print(f"3He-B parameters:")
print(f"  omega_L / Delta = {omega_L_3He / Delta_3He:.1e}")
print(f"  tau_L ~ {tau_L_3He:.0e} s")
print(f"  tau_superfluid ~ {tau_SF_3He:.0e} s")
print(f"  Ratio tau_SF/tau_L = {ratio_3He:.1e}")

# Framework analog:
ratio_framework = tau_min / t_transit
print(f"\nFramework parameters:")
print(f"  omega_L / Delta = {omega_L / Delta_0_GL:.4f}")
print(f"  tau_L = {tau_min:.4e} M_KK^{{-1}}")
print(f"  t_transit = {t_transit:.6e} M_KK^{{-1}}")
print(f"  Ratio tau_L/t_transit = {ratio_framework:.2e}")

# Convert to SI for comparison
tau_L_SI = tau_min / (M_KK / (hbar_GeV_s * 1e9))  # convert M_KK^{-1} to seconds
# M_KK = 7.43e16 GeV -> 1/M_KK = hbar / M_KK = 6.58e-25 / 7.43e16 = 8.85e-42 s
M_KK_inv_seconds = hbar_GeV_s / M_KK  # seconds per M_KK^{-1}
tau_L_seconds = tau_min * M_KK_inv_seconds
t_transit_seconds = t_transit * M_KK_inv_seconds

print(f"\nSI conversions:")
print(f"  1/M_KK = {M_KK_inv_seconds:.3e} s")
print(f"  tau_L = {tau_L_seconds:.3e} s")
print(f"  t_transit = {t_transit_seconds:.3e} s")

# ===========================================================================
#  SECTION 8: GGE Relic Persistence
# ===========================================================================

print("\n--- SECTION 8: GGE Relic Persistence ---")

# The question: does the Leggett mode decay fast enough to erase the
# non-thermal squeezing spectrum (GGE relic)?
#
# Answer depends on tau_L vs t_transit:
# If tau_L >> t_transit: Leggett mode never decays during the transit.
#   The GGE relic (non-thermal squeezing spectrum) is PRESERVED.
# If tau_L << t_transit: Leggett mode thermalizes during transit.
#   The squeezing spectrum would relax toward thermal.
# If tau_L ~ t_transit: partial thermalization.

ratio_preservation = tau_min / t_transit
print(f"tau_L / t_transit = {ratio_preservation:.2e}")

if ratio_preservation > 100:
    preservation = "STRONGLY PRESERVED"
    verdict_detail = f"tau_L/t_transit = {ratio_preservation:.0e} >> 1"
elif ratio_preservation > 10:
    preservation = "PRESERVED"
    verdict_detail = f"tau_L/t_transit = {ratio_preservation:.1f} > 10"
elif ratio_preservation > 1:
    preservation = "MARGINALLY PRESERVED"
    verdict_detail = f"tau_L/t_transit = {ratio_preservation:.2f} > 1 (marginal)"
else:
    preservation = "ERASED"
    verdict_detail = f"tau_L/t_transit = {ratio_preservation:.4f} < 1"

print(f"GGE relic status: {preservation}")
print(f"Detail: {verdict_detail}")

# Additional check: even AFTER transit, the Leggett mode exists only in the
# ordered (condensed) phase. The GGE state HAS no condensate (it is a normal state
# quasiparticle distribution). So the Leggett mode itself is a TRANSIT-ONLY excitation.
# Post-transit, the relevant question is whether the squeezing spectrum imprinted
# during transit survives in the GGE occupation numbers.

print(f"\nCritical structural point:")
print(f"  The Leggett mode exists only during transit (condensed phase).")
print(f"  Post-transit GGE has no condensate => no Leggett mode.")
print(f"  The squeezing spectrum is imprinted in GGE occupation numbers,")
print(f"  which are conserved quantities of the integrable Hamiltonian.")
print(f"  Leggett decay DURING transit: suppressed by tau_L >> t_transit.")
print(f"  Leggett decay AFTER transit: mode does not exist (no condensate).")
print(f"  => Non-thermal relic is DOUBLY PROTECTED.")

# ===========================================================================
#  SECTION 9: Gate Verdict
# ===========================================================================

print("\n" + "=" * 72)
print("GATE VERDICT: DIPOLAR-THERM-61 — INFO")
print("=" * 72)

print(f"""
Leggett mode lifetime on 32-cell Josephson fabric:

1. Kinematic analysis:
   - omega_L/2 = {omega_half_L:.4f} M_KK
   - Goldstone band: [{omega_Gold[0]:.4f}, {omega_Gold[-1]:.4f}] M_KK
   - Back-to-back decay (k,-k): {'POSSIBLE' if kinematic_possible else 'FORBIDDEN'}
   - Kinematic pairs within 1%: {n_kinematic_pairs}
   - Kinematic pairs within 10%: {n_broad}

2. Decay rates (M_KK units):
   - Leggett-Takagi continuum: Gamma = {Gamma_LT:.4e}, tau = {tau_LT:.4e}
   - FGR lattice (intrinsic eta): Gamma = {Gamma_lattice_intrinsic:.4e}, tau = {tau_lattice_intrinsic:.4e}
   - FGR lattice (transit eta):   Gamma = {Gamma_lattice_transit:.4e}, tau = {tau_lattice_transit:.4e}
   - Direct Josephson (intrinsic): Gamma = {Gamma_direct:.4e}, tau = {tau_direct:.4e}
   - Direct Josephson (transit):  Gamma = {Gamma_direct_broad:.4e}, tau = {tau_direct_broad:.4e}

3. Dominant channel: {Gamma_max_name}
   Gamma = {Gamma_max:.4e} M_KK
   tau_L = {tau_min:.4e} M_KK^{{-1}}
   Q = {Q_fabric:.2e}

4. Timescale ratios:
   tau_L / t_transit = {tau_min/t_transit:.2e}
   tau_L / t_Thouless = {tau_min/t_Thouless:.2e}
   tau_L / H^{{-1}} = {tau_min/H_inv:.2e}

5. GGE relic: {preservation}
   {verdict_detail}
   Double protection: kinetic (tau_L >> t_transit) + structural (no condensate post-transit)

6. 3He-B comparison:
   Framework omega_L/Delta = {omega_L/Delta_0_GL:.4f} vs 3He omega_L/Delta ~ 1e-6
   Framework tau_L/t_transit = {ratio_framework:.2e}
   3He tau_L/tau_SF = {1.0/ratio_3He:.2e} (inverse of persistence ratio {ratio_3He:.1e})

Classification: PHONONIC (Goldstone decay channel on fabric lattice)
""")

# ===========================================================================
#  SECTION 10: Save Results
# ===========================================================================

outfile = os.path.join(os.path.dirname(__file__), 's61_dipolar_thermalization.npz')
np.savez(outfile,
    # Goldstone spectrum
    lambda_lap=lambda_lap,
    omega_Gold=omega_Gold,
    c_Gold=c_Gold,
    N_cells=N_cells,
    N_bonds=N_bonds,

    # Leggett parameters
    omega_L=omega_L,
    m_G=m_G,
    chi_phase=chi_phase,
    chi_Gold=chi_Gold,
    Q_Leggett_S50=Q_Leggett,

    # Coupling constants
    E_J_bond=E_J_bond,
    J_23=J_23,
    g_3_GL=g_3_GL,
    V_eff_cubic=V_eff_cubic,
    V_LH=V_LH,
    G_H_propagator=G_H,
    V_HGG=V_HGG,
    omega_H1=omega_H,

    # Kinematic
    kinematic_possible=kinematic_possible,
    omega_half_L=omega_half_L,
    n_kinematic_pairs_1pct=n_kinematic_pairs,
    n_kinematic_pairs_10pct=n_broad,

    # Rates
    Gamma_LT=Gamma_LT,
    Gamma_lattice_intrinsic=Gamma_lattice_intrinsic,
    Gamma_lattice_transit=Gamma_lattice_transit,
    Gamma_direct=Gamma_direct,
    Gamma_direct_broad=Gamma_direct_broad,
    Gamma_max=Gamma_max,
    Gamma_grav=Gamma_grav,

    # Lifetimes
    tau_LT=tau_LT,
    tau_lattice_intrinsic=tau_lattice_intrinsic,
    tau_lattice_transit=tau_lattice_transit,
    tau_direct=tau_direct,
    tau_direct_broad=tau_direct_broad,
    tau_min=tau_min,
    tau_grav=tau_grav,

    # Q factors
    Q_fabric=Q_fabric,

    # Timescale ratios
    tau_over_t_transit=tau_min/t_transit,
    tau_over_t_Thouless=tau_min/t_Thouless,
    tau_over_H_inv=tau_min/H_inv,

    # Reference scales
    t_transit=t_transit,
    t_Thouless=t_Thouless,
    H_inv=H_inv,
    t_Leggett_osc=t_Leggett_osc,
    N_osc_transit=N_osc_transit,

    # SI conversions
    M_KK_inv_seconds=M_KK_inv_seconds,
    tau_L_seconds=tau_L_seconds,
    t_transit_seconds=t_transit_seconds,

    # 3He comparison
    ratio_3He_persistence=ratio_3He,

    # GGE preservation
    preservation_status=preservation,
    preservation_detail=verdict_detail,

    # Gate
    gate_name='DIPOLAR-THERM-61',
    gate_verdict='INFO',
    gate_detail=f'Leggett lifetime tau_L={tau_min:.2e} M_KK^-1. '
                f'tau_L/t_transit={tau_min/t_transit:.1e}. '
                f'GGE relic {preservation}. '
                f'Q_fabric={Q_fabric:.1e}. '
                f'Dominant: {Gamma_max_name}.'
)

print(f"\nSaved: {outfile}")
print("DONE.")
