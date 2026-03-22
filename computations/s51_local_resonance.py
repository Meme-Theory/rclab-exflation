#!/usr/bin/env python3
"""
s51_local_resonance.py — Local Resonance Mass Enhancement via T-Matrix
=======================================================================

Session 51, Gate: LOCAL-RESONANCE-51

Physics:
  The Goldstone phonon (n=0 KK mode, m_G = 0.070 M_KK) propagates on the
  4D fabric. Its first-order self-energy from the T^2 condensate texture
  VANISHES because <V>_{T^2} = 0 for the zero-mode (S50 W1-H, proven).

  However, the SECOND-ORDER self-energy through intermediate KK states
  and cavity resonances does NOT vanish:

    Re[Sigma(omega)] = sum_n |V_{0n}|^2 / (omega_n^2 - omega^2)

  where V_{0n} = <Goldstone|H_int|KK_n> is the coupling matrix element
  and omega_n are the cavity mode frequencies.

  This is the acoustic metamaterial mechanism: sub-wavelength resonators
  (cavity modes at omega_0 = 0.800+ M_KK) create effective mass enhancement
  for a wave propagating at omega << omega_0 (the Goldstone at 0.070).

  The enhancement diverges as omega -> omega_0, giving arbitrarily large
  effective mass near the resonance. Below resonance, Re[Sigma] > 0 and
  Im[Sigma] = 0 (no damping), which is exactly the regime we operate in.

Key insight:
  First-order coupling (Goldstone -> KK_n) is blocked by <V> = 0.
  But the T-matrix includes ALL orders. The SECOND-order coupling is:

    g_eff^2 = sum_{n>=1} |<0|V|n>|^2 * omega_n^2 / (omega_n^2 - omega^2)

  where <0|V|n> is the coupling of the zero-mode to KK mode n through
  the texture V(x). These matrix elements are NONZERO because V(x) has
  nonzero Fourier components at all KK wavevectors.

Gate criteria:
  PASS: m_eff in [8, 16] M_KK
  FAIL: g^2_eff < 10 M_KK^4 (insufficient coupling)
  INFO: m_eff > 1 but < 8 M_KK

Outputs:
  - s51_local_resonance.npz
  - s51_local_resonance.png

Usage:
  "phonon-exflation-sim/.venv312/Scripts/python.exe" tier0-computation/s51_local_resonance.py
"""

import sys
sys.path.insert(0, 'tier0-computation')
from canonical_constants import *
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

OUT_DIR = Path('tier0-computation')

print("=" * 78)
print("LOCAL RESONANCE MASS ENHANCEMENT VIA T-MATRIX (LOCAL-RESONANCE-51)")
print("=" * 78)

# ============================================================================
#  SECTION 1: Load upstream data
# ============================================================================

print("\nSECTION 1: Loading upstream data")
print("-" * 40)

d49 = np.load(OUT_DIR / 's49_cavity_resonance.npz', allow_pickle=True)
d50 = np.load(OUT_DIR / 's50_eikonal_damping.npz', allow_pickle=True)

# Goldstone parameters
m_G = float(d50['m_G'])          # 0.0696 M_KK (Leggett mass)
c_BdG = float(d50['c_BdG'])     # 0.7507 M_KK
g_11 = float(d50['g_11'])       # metric element
L_phys = float(d50['L_phys'])   # T^2 circumference = 13.16 M_KK^{-1}

# Texture parameters (from S50 Haar sampling on T^2)
V_rms = float(d50['V_rms'])     # 3.035 (dimensionless, delta_c/c_0)
V_haar_avg = float(d50['V_haar_avg'])  # Should be ~0 for zero-mode argument
l_corr = float(d50['l_corr'])   # 0.948 M_KK^{-1} correlation length

# Cavity modes from S49 (30 modes across 5 solved cavities)
cavity_modes_all = d49['cavity_modes_all']   # omega values (M_KK)
cavity_rank_all = d49['cavity_rank_all']     # which cavity
n_subsonic = int(d49['n_subsonic_components'])  # 111 total cavities
n_cavities_solved = int(d49['n_cavities_solved'])  # 5 solved

# S_q structure function from S50 (for coupling estimate)
q_centers = d50['q_centers']
S_q = d50['S_q']

# Cavity properties
cavity_R_eff = d49['cavity_R_eff']  # Effective radii of solved cavities
barrier_width = float(d49['barrier_width'])
Q_exponent = float(d49['Q_exponent'])  # Q ~ e^23.5

print(f"  m_G           = {m_G:.6f} M_KK")
print(f"  c_BdG         = {c_BdG:.4f} M_KK")
print(f"  V_rms         = {V_rms:.4f}")
print(f"  l_corr        = {l_corr:.4f} M_KK^{{-1}}")
print(f"  L_phys (T^2)  = {L_phys:.4f} M_KK^{{-1}}")
print(f"  n_subsonic    = {n_subsonic}")
print(f"  Solved cavity modes: {len(cavity_modes_all)}")
print(f"  Lowest cavity = {cavity_modes_all.min():.5f} M_KK")
print(f"  Q_exponent    = {Q_exponent:.1f} (Q ~ e^{Q_exponent:.0f})")

# ============================================================================
#  SECTION 2: KK mode spectrum on T^2
# ============================================================================

print("\n" + "=" * 78)
print("SECTION 2: KK mode spectrum on T^2")
print("=" * 78)

# T^2 is a flat torus with circumference L_phys.
# For a FLAT torus (T^2 = R^2 / (L1 Z x L2 Z)), the KK modes are:
#   k_{n1,n2} = 2*pi * (n1/L1, n2/L2)
#   omega_{n1,n2} = c_BdG * |k_{n1,n2}|
# For a square torus with L1 = L2 = L:
#   omega_{n1,n2} = c_BdG * 2*pi/L * sqrt(n1^2 + n2^2)

# The T^2 is NOT square in general. From S49, the physical torus is
# parameterized by the SU(3) Cartan torus at the fold.
# L_phys = 13.16 is the CIRCUMFERENCE (perimeter of fundamental domain).
# For a square torus: L = L_phys / 4, but the Cartan torus is a
# HEXAGONAL torus (SU(3) root lattice is hexagonal).
#
# The hexagonal torus has fundamental frequencies:
#   omega_{m,n} = c_BdG * (4*pi / (L_hex * sqrt(3))) * sqrt(m^2 + mn + n^2)
# where L_hex = L_phys / (2*sqrt(3)) is the lattice constant.
# However, the key physics is set by omega_min = c_BdG * k_min where
# k_min = 2*pi / R_max and R_max is the largest dimension of the torus.

# For the square torus approximation (which sets the scale):
L_torus = L_phys / 4  # Side length (approximate for square torus)
k_fund = 2 * PI / L_torus  # Fundamental KK wavevector
omega_KK_fund = c_BdG * k_fund  # Fundamental KK frequency

print(f"  L_torus (side) = {L_torus:.4f} M_KK^{{-1}}")
print(f"  k_fund         = {k_fund:.4f} M_KK")
print(f"  omega_KK_fund  = {omega_KK_fund:.4f} M_KK")
print(f"  omega_KK_fund / m_G = {omega_KK_fund / m_G:.1f}x")

# Build KK mode tower (up to some cutoff)
# Modes: (n1, n2) with n1^2 + n2^2 > 0
# omega_{n1,n2} = omega_KK_fund * sqrt(n1^2 + n2^2)
# For a hexagonal torus: omega_{n1,n2} = omega_hex * sqrt(n1^2 + n1*n2 + n2^2)

n_max_KK = 10  # Include modes up to (n_max, n_max)
kk_modes = []
for n1 in range(-n_max_KK, n_max_KK + 1):
    for n2 in range(-n_max_KK, n_max_KK + 1):
        if n1 == 0 and n2 == 0:
            continue  # Skip zero mode (that's the Goldstone)
        r2 = n1**2 + n2**2  # Square torus
        omega_kk = omega_KK_fund * np.sqrt(r2)
        kk_modes.append((n1, n2, omega_kk))

kk_modes.sort(key=lambda x: x[2])
N_KK = len(kk_modes)
omega_KK = np.array([m[2] for m in kk_modes])

print(f"\n  KK modes generated: {N_KK}")
print(f"  Lowest KK mode:  omega = {omega_KK[0]:.4f} M_KK (degeneracy: "
      f"{np.sum(np.abs(omega_KK - omega_KK[0]) < 1e-10)})")
print(f"  Highest KK mode: omega = {omega_KK[-1]:.4f} M_KK")
print(f"  First 10 KK frequencies:")
shown = set()
for n1, n2, w in kk_modes:
    w_round = round(w, 6)
    if w_round not in shown:
        deg = sum(1 for _, _, ww in kk_modes if abs(ww - w) < 1e-10)
        print(f"    omega = {w:.4f} M_KK (n1^2+n2^2 = {n1**2+n2**2}, deg = {deg})")
        shown.add(w_round)
    if len(shown) >= 10:
        break

# ============================================================================
#  SECTION 3: Coupling matrix elements <0|V|n>
# ============================================================================

print("\n" + "=" * 78)
print("SECTION 3: Coupling matrix elements <0|V|n>")
print("=" * 78)

# The texture V(x) on T^2 has Fourier decomposition:
#   V(x) = sum_{m,n} V_{m,n} exp(i k_{m,n} . x)
# where V_{0,0} = <V>_{T^2} = 0 (proven in S50).
#
# The coupling of the Goldstone (zero-mode, psi_0 = 1/sqrt(A)) to
# KK mode |n1,n2> (psi_{n} = exp(ik_n.x)/sqrt(A)) is:
#   <0|V|n> = (1/A) integral V(x) exp(ik_n.x) d^2x = V_{-n1,-n2} / sqrt(A)
#
# The |V_{n1,n2}|^2 are related to the structure function S(q):
#   S(q) = (1/A) sum_{|k_{m,n}| in shell q} |V_{m,n}|^2
#
# From S50: S_q is computed on the T^2 grid.

# The total coupling squared is:
#   sum_{n!=0} |<0|V|n>|^2 = (1/A) sum_{n!=0} |V_n|^2 = (1/A) * (A * V_rms^2 - |V_0|^2)
#                          = V_rms^2  (since V_0 = 0)
#
# This gives the TOTAL coupling from zero-mode to ALL KK modes via the texture.
# The key insight: this total is LARGE (V_rms^2 = 9.2), but it is distributed
# across ALL KK modes weighted by their wavevector.

A_T2 = L_phys**2 / (2 * np.sqrt(3))  # Area of hexagonal torus
# For a square torus: A_T2 = L_torus^2

# Actually let's use the full physical area consistently
# S49 used a discretized T^2 with N_grid points. The physical area is:
# A = L1 * L2 where L1, L2 are the two periods. For the Cartan torus of SU(3),
# the area is Vol(T^2) with the induced metric from g_11.
# From S49: the grid had 200x200 points on a unit cell.
# L_phys = 13.16 is the circumference of the fundamental domain.
# For a square approximation: A_T2 = (L_phys/4)^2

A_T2_sq = L_torus**2
print(f"  Area of T^2 (square approx) = {A_T2_sq:.4f} M_KK^{{-2}}")

# The coupling of zero-mode to KK mode (n1,n2) through V(x) is:
#   |<0|V|n>|^2 = |V_{n1,n2}|^2 / A_T2
#
# From the S50 structure function S(q), we can extract |V_n|^2 at each q.
# S(q) = <|V(q)|^2> / A, so |V_n|^2 ~ S(|k_n|) * A / (shell area)
#
# More precisely, for a given KK mode at wavevector k_{n1,n2}:
#   |V_{n1,n2}|^2 ~ S(|k|) * delta_k^2
# where delta_k = k_fund is the wavevector spacing.

# Assign coupling to each KK mode via the texture power spectrum
# S(q) from S50 is defined on q_centers (80 bins from 0.21 to ~50 M_KK)
# Interpolate S(q) to get S at each KK wavevector

from scipy.interpolate import interp1d
S_interp = interp1d(q_centers, S_q, kind='linear', bounds_error=False, fill_value=0.0)

# For each KK mode, the wavevector is k_n = k_fund * sqrt(n1^2+n2^2)
# and the coupling is |<0|V|n>|^2 = S(|k_n|) * (k_fund)^2 / A_T2
# This gives units: [S] * [k^2] / [A] = (dimensionless)^2 per mode

# Actually let's think about this more carefully.
# V(x) is dimensionless (delta_c/c). V_rms^2 = <V^2> = 9.21.
# Parseval: sum_n |V_n|^2 / A = V_rms^2
# So sum_n |V_n|^2 = V_rms^2 * A
#
# The structure function S(q) = (1/A) * (sum over modes with |k| ~ q) |V_k|^2
# So |V_k|^2 at wavevector k is approximately S(|k|) * A * delta_q^2 / (2*pi*|k|)
# (isotropic average, ring area = 2*pi*|k|*delta_q)
#
# For a single KK mode at wavevector k_n:
#   |V_{k_n}|^2 = S(|k_n|) * A * (dk)^2  [where dk = k_fund, lattice spacing in k-space]
#
# But actually S(q) as defined in S50 uses binned average, so:
#   |V_n|^2 ~ S(|k_n|) * (delta_q * |k_n| * 2*pi) / N_modes_in_shell * A_T2
# This is getting circular. Let me use a cleaner approach.

# CLEAN APPROACH: Use the Parseval sum rule directly.
# We know: sum_{n!=0} |<0|V|n>|^2 = V_rms^2  (because V_0 = 0)
# The distribution across modes follows the power spectrum.
# From S50: S(q) drops sharply for q > 2/l_corr.
# q_50% = 1.055, q_90% = 1.899 (from S50)
# This means most of the spectral weight is at q < 2 M_KK.

q_50 = float(d50['q_50_percent'])   # 1.055 M_KK
q_90 = float(d50['q_90_percent'])   # 1.899 M_KK

print(f"\n  V_rms^2 (total coupling) = {V_rms**2:.4f}")
print(f"  q_50% = {q_50:.4f} M_KK")
print(f"  q_90% = {q_90:.4f} M_KK")
print(f"  k_fund (KK spacing) = {k_fund:.4f} M_KK")

# The first KK mode has wavevector k_1 = k_fund = 1.91 M_KK (for square torus)
# The texture has 50% of its power at q < 1.055 and 90% at q < 1.899.
# So the first KK mode sits at k_1 = 1.91, right at the q_90 cutoff.
# This means the texture power spectrum PEAKS at wavevectors just below
# the first KK mode -- the coupling is well-matched.

# For the T-matrix, we need the coupling of the Goldstone to each cavity
# mode THROUGH the KK intermediate states. The second-order coupling is:
#
#   g_{0,cav}^2 = | sum_n <0|V|n> * <n|V_cav|cav> / (E_n - E_0) |^2
#
# where V_cav is the coupling between KK mode n and cavity mode.
#
# CRITICAL POINT: The KK modes and cavity modes are on THE SAME T^2.
# The cavity modes ARE KK modes confined by the Mach-number potential.
# So the coupling <n|V_cav|cav> is the overlap of the delocalized KK
# mode with the localized cavity eigenfunction through the texture.
#
# For deep Anderson localization (kl = 0.0095), the cavity modes ARE
# the localized states. The "KK modes" in the absence of the texture
# would be plane waves. The texture localizes them into cavity modes.
# This means the second-order perturbation theory picture is WRONG:
# the texture is not a perturbation on top of free KK modes --
# it IS the confining potential that creates the cavities.

print("\n  IMPORTANT: KK modes and cavity modes are NOT independent.")
print("  The texture V(x) creates the cavities by Anderson-localizing")
print("  the KK modes. The 'free KK modes' are plane waves;")
print("  the 'cavity modes' are their localized version in V(x).")
print("  The T-matrix must use the FULL Green's function of the T^2")
print("  problem, not second-order perturbation theory.")

# ============================================================================
#  SECTION 4: T-matrix self-energy -- Single-resonator picture
# ============================================================================

print("\n" + "=" * 78)
print("SECTION 4: T-matrix self-energy (single-resonator picture)")
print("=" * 78)

# The T-matrix for a single resonant scatterer at frequency omega_0:
#
#   T(omega) = g^2 / (omega_0^2 - omega^2 - i*0^+)
#
# For a propagating mode at frequency omega < omega_0:
#   Re[T(omega)] = g^2 * omega_0^2 / (omega_0^2 - omega^2)  [omega << omega_0 limit]
#   Im[T(omega)] = 0  (below resonance, no damping)
#
# The self-energy from N_cav identical resonators at the SAME frequency:
#   Sigma(omega) = n_cav * T(omega)
# where n_cav = N_cav / A_T2 is the number density of resonators.
#
# The effective mass:
#   m_eff^2 = m_bare^2 + Re[Sigma(m_bare)]

# What is g? For a single resonant cavity on T^2, the coupling to the
# zero-mode is determined by the overlap integral:
#
#   g = <0|V|cav> = (1/sqrt(A)) * integral V(x) * psi_cav(x) d^2x
#
# BUT <0|V|cav> = 0 by the same zero-mode argument!
# The zero-mode is constant on T^2. If psi_cav is localized, then:
#   <0|V|cav> = (1/sqrt(A)) * integral_{cavity} V(x) * psi_cav(x) d^2x
# This is NOT zero in general, because V(x) varies WITHIN the cavity,
# and the integral is over the CAVITY region only (psi_cav is zero outside).
#
# Wait -- let me be more careful. psi_cav is an EIGENSTATE of the
# Helmholtz equation on T^2 with the texture potential. It is localized
# to a subsonic cavity, with exponential tails outside.
# The ZERO-MODE psi_0 = 1/sqrt(A) is ALSO an eigenstate (the lowest one).
#
# If both are eigenstates of the SAME Hamiltonian, they are ORTHOGONAL:
#   <0|cav> = 0
# This orthogonality is EXACT.
#
# So the DIRECT coupling g = <0|H_int|cav> requires the interaction
# H_int to be DIFFERENT from the Hamiltonian whose eigenstates these are.
#
# In the acoustic metamaterial context:
# - The STATIC texture V(x) defines the background (creates cavities)
# - The DYNAMICAL perturbation is the BCS interaction that couples
#   different phonon modes
# - The coupling g comes from the ANHARMONIC terms (3-phonon, 4-phonon)
#   NOT from the static texture

print("  KEY REALIZATION: Static texture cannot couple orthogonal eigenstates.")
print("  The zero-mode and cavity modes are BOTH eigenstates of the same")
print("  Hamiltonian (Helmholtz + texture). They are orthogonal by construction.")
print("  The coupling must come from ANHARMONIC terms (H_3, H_4) not from V(x).")

# ============================================================================
#  SECTION 5: Anharmonic coupling to cavity modes
# ============================================================================

print("\n" + "=" * 78)
print("SECTION 5: Anharmonic coupling to cavity modes")
print("=" * 78)

# The BCS interaction Hamiltonian includes terms beyond the mean-field:
#   H = H_0 + H_3 + H_4 + ...
# where H_0 is the quadratic (mean-field) Hamiltonian,
# H_3 = V_3 * phi^3 is the cubic anharmonicity,
# H_4 = V_4 * phi^4 is the quartic anharmonicity.
#
# In the BdG formalism, the anharmonic couplings arise from:
# 1. Amplitude fluctuations of the gap: delta|Delta|
# 2. Phase fluctuations coupling to amplitude: (grad phi)^2 * |Delta|
# 3. Direct 4-phonon from the BCS vertex
#
# The cubic coupling V_3 connects the Goldstone (phase) to two amplitude
# (Higgs-like) modes. But in our system, the amplitude mode IS the cavity
# modes -- the Higgs mode of the BCS condensate in the cavity is at
# 2*Delta ~ 2*0.855 = 1.71 M_KK. This is ABOVE the lowest cavity
# mode at 0.800, so there's a potential resonance.
#
# HOWEVER, the cubic coupling V_3 between one Goldstone and two Higgs
# modes vanishes by symmetry (the Goldstone is the phase Nambu-Goldstone
# mode; the cubic vertex phi * sigma^2 requires the Goldstone to carry
# zero momentum, which it does -- but the vertex also needs momentum
# conservation for the two Higgs modes).
#
# The LEADING coupling of the Goldstone to cavity modes is the
# QUARTIC VERTEX H_4 ~ (grad phi)^2 * delta_rho, where delta_rho
# is the density fluctuation within the cavity. This gives:
#
#   g_4 ~ V_4 * k_G^2 * psi_cav(x=0)
#
# where k_G is the Goldstone wavevector and psi_cav(x=0) is the
# cavity mode amplitude at the Goldstone's position.

# Let me use a different, more concrete approach.
# The Goldstone dispersion on the fabric is:
#   omega^2 = c_BdG^2 * K^2 + m_G^2
# The self-energy correction from virtual excitation of internal modes:
#   Re[Sigma(omega)] = sum_n |g_n|^2 * omega_n^2 / (omega_n^2 - omega^2)
# where n runs over ALL internal modes of the T^2 cavity system.

# For the coupling, we use the PHYSICAL interaction: the BCS vertex V(B2,B2).
# The coupling of a 4D Goldstone mode to an internal cavity mode is
# mediated by the condensate texture. The texture provides the
# FORM FACTOR for the coupling.
#
# Since the Goldstone is constant on T^2, its coupling to internal mode |n>
# through the condensate gradient nabla Delta is:
#
#   g_n = V_BCS * <Delta> * integral_T2 psi_0^*(x) nabla_i psi_n(x) d^2x
#       = V_BCS * <Delta> * (1/sqrt(A)) * integral nabla_i psi_n(x) d^2x
#       = V_BCS * <Delta> * sqrt(A) * [psi_n(boundary) - psi_n(bulk)] / sqrt(A)
#
# For PERIODIC boundary conditions on T^2, the total derivative integral
# vanishes: integral nabla_i psi_n d^2x = 0 for any periodic psi_n.
# This is ANOTHER zero! The zero-mode cannot couple to internal modes
# through a total derivative.
#
# THE COUPLING MUST BE NON-DERIVATIVE.

# The remaining option: the coupling arises from the ENERGY DEPENDENCE
# of the BCS parameters. As the Goldstone (which is the modulus tau
# oscillation projected onto the phase sector) oscillates, it modulates
# the BCS gap Delta(tau). This modulation couples to ALL internal modes:
#
#   H_int = (d Delta / d phi_G) * phi_G * sum_n c_n^\dag c_n
#
# where c_n are the cavity mode operators and d Delta/d phi_G is the
# coupling strength. This is the PARAMETRIC coupling: the Goldstone
# modulates the medium, which modulates the cavity frequencies.

# The parametric coupling constant:
# phi_G (Goldstone) oscillates the relative phase between B2 sectors.
# This modulates J_12, the inter-sector Josephson coupling.
# J_12 sets the Leggett frequency: omega_L^2 ~ J_12 * n_s / m*
# The modulation of omega_n (cavity mode) by phi_G is:
#   d(omega_n)/d(phi_G) = d(omega_n)/d(Delta) * d(Delta)/d(phi_G)
#
# For a BCS cavity mode at omega_n, the sensitivity to Delta is:
#   d(omega_n)/d(Delta) ~ omega_n / Delta  (for modes near the gap edge)
#
# And d(Delta)/d(phi_G) ~ epsilon * Delta, where epsilon = 0.00248 (S49)
# is the Leggett inter-sector coupling fraction.

# The parametric coupling strength:
Delta_B2 = 0.855  # B2 BCS gap (M_KK) - from S45 multi-component
epsilon_Leggett = 0.00248  # Leggett coupling fraction (S49)

# For the parametric mechanism, the coupling is:
#   g_n = (d omega_n / d phi_G) * sqrt(omega_n)
#       = epsilon * Delta * (omega_n / Delta) * sqrt(omega_n)
#       = epsilon * omega_n * sqrt(omega_n)
# This assumes the cavity mode frequency scales with Delta.

# Actually, for the Leggett mode specifically, the coupling is more precise.
# The Leggett mode IS the inter-sector phase oscillation.
# Its coupling to INTERNAL cavity modes is through the Josephson energy:
#   E_J = J_12 * cos(phi_1 - phi_2)
# The cavity modes see the Josephson coupling as a boundary condition.
# Modulating phi changes the effective boundary condition for the cavity.

# Let me just compute the numbers directly.
# The coupling of the Goldstone to cavity mode n through the Josephson:
#   g_n^2 = epsilon^2 * J_12^2 * |<cav_n|cos(phi)|0>|^2
# where J_12 is the inter-sector Josephson coupling energy.
# From S49: J_12/J_23 = 19.52 (constant). J values from V matrix.

# The Josephson energy scale: omega_L^2 = 2*epsilon*J/m* where m* is pair mass
# So J ~ omega_L^2 * m* / (2*epsilon)
# With omega_L = 0.070, epsilon = 0.00248:
#   J * m* ~ omega_L^2 / (2*epsilon) = 0.070^2 / (2*0.00248) = 0.988

J_eff = m_G**2 / (2 * epsilon_Leggett)  # Effective Josephson scale
print(f"\n  Effective Josephson energy: J_eff = {J_eff:.4f} M_KK^2")
print(f"  = m_G^2 / (2*epsilon) = {m_G**2:.6f} / {2*epsilon_Leggett:.6f}")

# The parametric coupling of the Goldstone to cavity mode n:
#   g_n^2 = epsilon^2 * J_eff * omega_n
# (This follows from the modulation of the boundary condition;
#  the cavity mode sees an effective potential change of order
#  epsilon * J * phi_G at the domain wall.)
#
# For order-of-magnitude: g_n ~ epsilon * sqrt(J_eff * omega_n)

# Let's compute g_n for each cavity mode:
print("\n  Parametric coupling to cavity modes:")
print(f"  {'omega_n':>10s} {'g_n^2':>12s} {'g_n^2/(omega_n^2-m_G^2)':>25s}")
print(f"  {'-'*10} {'-'*12} {'-'*25}")

# ============================================================================
#  SECTION 6: Full T-matrix self-energy
# ============================================================================

print("\n" + "=" * 78)
print("SECTION 6: Full T-matrix self-energy computation")
print("=" * 78)

# The self-energy of the Goldstone from virtual excitation of cavity modes:
#
#   Re[Sigma(omega)] = sum_n g_n^2 / (omega_n^2 - omega^2)
#
# where n runs over ALL cavity modes and omega = m_G (on-shell Goldstone).
#
# We need to estimate g_n^2 for each cavity mode. There are three
# PHYSICALLY DISTINCT coupling mechanisms:

# MECHANISM A: Parametric (Josephson modulation)
# g_n^2 = epsilon^2 * J_eff * omega_n
# This is the coupling through the Leggett oscillation modulating cavity walls.

# MECHANISM B: Texture gradient coupling (non-zero for localized modes)
# Even though <V> = 0 for the zero-mode, the coupling through the
# GRADIENT of V (the texture) is nonzero:
#   g_n^2 = |<0| nabla V |n>|^2 / k_n^2
# For Anderson-localized modes, the gradient is enhanced by 1/xi_loc.
# |nabla V|^2 ~ V_rms^2 / l_corr^2

# MECHANISM C: BCS 4-phonon vertex
# The quartic BCS vertex couples two Goldstones to two cavity modes:
#   g_4^2 ~ V_{B2B2}^2 * (overlap integral)^2
# This is the standard 4-phonon scattering in the BCS Fock space.

# Let me compute ALL THREE and see which dominates.

V_B2B2 = 0.1557  # BCS interaction (M_KK, S34 Schur)

# --- MECHANISM A: Parametric ---
# g_A^2(n) = epsilon^2 * J_eff * omega_n
# This gives the modulation strength of cavity frequency by the Goldstone phase.

g2_A = np.array([epsilon_Leggett**2 * J_eff * w for w in cavity_modes_all])
Sigma_A = np.sum(g2_A / (cavity_modes_all**2 - m_G**2))

print("MECHANISM A: Parametric (Josephson modulation)")
print(f"  epsilon = {epsilon_Leggett:.4e}")
print(f"  J_eff = {J_eff:.4f}")
for i, (w, g2) in enumerate(zip(cavity_modes_all[:10], g2_A[:10])):
    contrib = g2 / (w**2 - m_G**2)
    print(f"  omega_{i} = {w:.4f}, g^2 = {g2:.2e}, contrib = {contrib:.2e}")
print(f"  Total Re[Sigma_A] = {Sigma_A:.6e} M_KK^2")
print(f"  m_eff_A = sqrt(m_G^2 + Sigma_A) = ", end='')
m_eff_A_sq = m_G**2 + Sigma_A
if m_eff_A_sq > 0:
    m_eff_A = np.sqrt(m_eff_A_sq)
    print(f"{m_eff_A:.6f} M_KK")
    print(f"  Enhancement: m_eff_A / m_bare = {m_eff_A / m_G:.2f}x")
else:
    print(f"NEGATIVE (tachyonic): {m_eff_A_sq:.6e}")

# Scale to 111 cavities (only 5 solved, but 111 total)
# The unsolved cavities have similar spectra (same physical torus).
# Scale assuming each cavity contributes proportionally to its size.
N_cav_total = n_subsonic  # 111
N_cav_solved = n_cavities_solved  # 5
# Modes per cavity from solved data: 30 modes / 5 cavities = 6 modes each
# But the solved cavities are the LARGEST. Smaller cavities have HIGHER
# fundamental frequencies (omega ~ 1/R).

# Average contribution per solved cavity:
Sigma_A_per_cav = Sigma_A / N_cav_solved
# Extrapolate to all 111:
Sigma_A_total = Sigma_A_per_cav * N_cav_total
print(f"\n  Scaled to {N_cav_total} cavities: Re[Sigma_A_total] = {Sigma_A_total:.6e}")
m_eff_A_total_sq = m_G**2 + Sigma_A_total
if m_eff_A_total_sq > 0:
    m_eff_A_total = np.sqrt(m_eff_A_total_sq)
    print(f"  m_eff_A (111 cavities) = {m_eff_A_total:.6f} M_KK")
else:
    print(f"  NEGATIVE: {m_eff_A_total_sq:.6e}")

# --- MECHANISM B: Texture gradient coupling ---
# g_B^2(n) = V_rms^2 * (1/l_corr^2) * (1/omega_n) * f_overlap
# where f_overlap is the overlap of the zero-mode with the gradient
# of the localized cavity mode.
# For a localized mode with localization length xi_loc:
#   f_overlap ~ xi_loc^2 / A_T2 (fraction of area occupied by mode)
# From S50: xi_loc ~ l_mfp_strong = 0.103 M_KK^{-1}

xi_loc = float(d50['l_mfp_strong'])  # 0.103 M_KK^{-1}
f_overlap = xi_loc**2 / A_T2_sq

print(f"\n\nMECHANISM B: Texture gradient coupling")
print(f"  V_rms = {V_rms:.4f}")
print(f"  l_corr = {l_corr:.4f} M_KK^{{-1}}")
print(f"  xi_loc = {xi_loc:.4f} M_KK^{{-1}}")
print(f"  f_overlap = xi_loc^2 / A_T2 = {f_overlap:.2e}")

# For Anderson-localized modes, the coupling through texture gradients:
# The key matrix element is:
#   <0|(-nabla^2 V)|n> = (k_n^2) * <0|V|n>
# But <0|V|n> = 0 for orthogonal eigenstates.
#
# HOWEVER, the NON-ORTHOGONAL coupling arises when we consider
# the Goldstone as a 4D mode and the cavity as an internal mode.
# They live in DIFFERENT Hilbert spaces. The coupling is through
# the cross-term in the Hamiltonian:
#
#   H_cross = integral_{T^2} phi_G(x_4D) * V(x_T2) * phi_cav(x_T2) d^2x_T2
#
# Since phi_G has a flat profile on T^2 (zero mode), this is:
#   H_cross = phi_G * integral V(x) psi_cav(x) d^2x / sqrt(A)
#           = phi_G * V_{cav} / sqrt(A)
# where V_{cav} = integral V(x) psi_cav(x) d^2x.
#
# For an eigenstate of H_0 = -nabla^2 + V, psi_cav satisfies:
#   (-nabla^2 + V) psi_cav = omega_n^2 psi_cav
# So integral V(x) psi_cav(x) d^2x = omega_n^2 * integral psi_cav d^2x
#                                     + integral nabla^2 psi_cav d^2x
#                                   = omega_n^2 * <0|n> * sqrt(A) + (surface terms)
# For orthogonal eigenstates <0|n> = 0, so V_{cav} = 0.
#
# THIS IS THE SAME ZERO. The orthogonality kills the gradient coupling too.

# The coupling between the zero-mode and ANY internal eigenstate
# through the SAME Hamiltonian is exactly zero. This is a theorem,
# not an approximation.

# HOWEVER: the Goldstone on the FABRIC is NOT an eigenstate of the
# INTERNAL Hamiltonian. The fabric Goldstone is a DIFFERENT quantum
# number (it carries 4D momentum K_mu). The coupling we need is:
#
#   g_n(K) = <Goldstone, K | H_BCS | cavity_n, 0>
#
# where the Goldstone has 4D momentum K and the cavity mode has zero
# 4D momentum (it's localized internally). The BCS interaction H_BCS
# is the FULL interaction, not the mean-field Hamiltonian.

# The relevant interaction is the fluctuation term beyond mean-field:
#   delta_H = V_{B2B2} * (Delta^* Delta - <Delta^* Delta>)
#           = V_{B2B2} * (2 <Delta> delta_Delta + delta_Delta^2)
# where delta_Delta is the gap fluctuation.
#
# The Goldstone IS the phase of delta_Delta: delta_Delta = i <Delta> phi_G
# The cavity modes are density fluctuations: delta_n ~ delta_Delta^2 / Delta
#
# The coupling of one Goldstone to one cavity mode is:
#   g_n = V_{B2B2} * <Delta> * <n|phi_G|0>  [wrong: phi_G is 4D, |0> internal]
#
# Let me think about this differently. The proper way is through the
# BOGOLIUBOV-de GENNES formalism.

# In BdG: the Goldstone mode and the cavity modes are BOTH quasiparticles
# of the BdG Hamiltonian. Their interaction comes from the residual
# interaction beyond BdG (the terms that BdG mean-field doesn't capture).
#
# The residual interaction is of order V_{B2B2}^2 / E_gap (second order).
# The coupling of a 4D Goldstone (momentum K) to a localized internal
# cavity mode (with wave function psi_n) is:
#
#   g_n(K) = V_{B2B2} * integral psi_0(x) * psi_n(x) * e^{iK.x_4D} d^8x
#          = V_{B2B2} * delta_{n,0}  [by orthogonality on T^2]
#          = 0 for n >= 1
#
# THE SAME ZERO AGAIN.
# The orthogonality of internal eigenstates kills EVERY coupling that
# goes through a single insertion of V.

print("\n  STRUCTURAL OBSTACLE: All single-insertion couplings vanish.")
print("  <0|V|n> = 0 for ANY operator V diagonal in position, because")
print("  the zero-mode psi_0 and cavity mode psi_n are orthogonal.")
print("  This blocks Mechanisms A and B at leading order.")

# --- MECHANISM C: Double insertion (T-matrix) ---
# The FIRST non-vanishing coupling requires TWO insertions of V.
# This is the T-matrix itself:
#
#   T_{0n}(omega) = <0|V|m> G_m(omega) <m|V|n>  [summed over m]
#
# But <0|V|m> = 0 for ALL eigenstates m (same orthogonality).
# So the T-matrix ALSO vanishes at second order.
#
# At THIRD order:
#   T_{0n}^{(3)} = <0|V|m> G_m <m|V|p> G_p <p|V|n>
# Same problem: <0|V|m> = 0.
#
# THIS VANISHES TO ALL ORDERS IN PERTURBATION THEORY.
# The zero-mode projection kills every term in the Born series
# because the first vertex is always <0|V|m> = 0.

# Wait. This is only true if V is the SAME operator at every vertex.
# In reality, the perturbation expansion involves DIFFERENT operators:
#   H' = H_3 + H_4 where H_3 ~ phi^3, H_4 ~ phi^4
# The cubic term H_3 can connect the zero mode to a pair of modes:
#   <0|H_3|m,n> = V_3 * integral psi_0 psi_m psi_n d^2x  [nonzero!]
# This is NOT killed by orthogonality because it involves THREE wavefunctions.

print("\n  ESCAPE: The CUBIC anharmonic coupling H_3 is NOT killed by")
print("  orthogonality. <0|H_3|m,n> involves a triple overlap integral")
print("  integral psi_0(x) psi_m(x) psi_n(x) d^2x, which is generically")
print("  nonzero when psi_0 is constant (= 1/sqrt(A)).")
print("  This gives: <0|H_3|m,n> = V_3 * <psi_m psi_n>_{T^2}")

# ============================================================================
#  SECTION 7: Cubic anharmonic self-energy
# ============================================================================

print("\n" + "=" * 78)
print("SECTION 7: Cubic anharmonic self-energy")
print("=" * 78)

# The cubic interaction in the BCS system:
# H_3 = lambda_3 * sum_{k,k',q} phi_k phi_{k'} phi_q * delta(k+k'+q, 0)
#
# In our system, the relevant cubic coupling arises from the anharmonicity
# of the BCS energy functional:
#   E[Delta] = a|Delta|^2 + b|Delta|^4 + ...
# Expanding around the mean-field:
#   Delta = Delta_0 + sigma + i * Delta_0 * phi
# where sigma = amplitude mode, phi = phase mode (Goldstone).
#
# The cubic terms are:
#   H_3 = b * Delta_0 * (4 sigma phi^2 + 4 sigma^3 + ...)
# The term sigma * phi^2 couples ONE amplitude mode to TWO Goldstones.
# For the self-energy of the Goldstone, we need the ONE-LOOP diagram:
#   Goldstone -> (sigma + Goldstone virtual pair) -> Goldstone
# This has coupling vertex V_3 = 4 * b_GL * Delta_0.

V_3 = 4 * b_GL * Delta_0_GL  # Cubic coupling (M_KK units)

print(f"  Cubic coupling: V_3 = 4 * b_GL * Delta_0")
print(f"    b_GL = {b_GL:.6f}")
print(f"    Delta_0 = {Delta_0_GL:.6f}")
print(f"    V_3 = {V_3:.6f} M_KK")

# The sigma mode (amplitude/Higgs) has mass 2*Delta_0 in BCS theory.
m_sigma = 2 * Delta_0_GL
print(f"  Higgs mass: m_sigma = 2*Delta_0 = {m_sigma:.4f} M_KK")

# The one-loop self-energy of the Goldstone from the cubic vertex:
#
#   Sigma_cubic(omega) = V_3^2 * integral d^2k / (2pi)^2 *
#                         G_sigma(k) * G_phi(k-q)
#
# where G_sigma(k) = 1/(omega_sigma^2(k) - (omega_k)^2)
# and G_phi(k) = 1/(c^2 k^2 - (omega-omega_k)^2).
#
# For the ON-SHELL Goldstone at omega = m_G << m_sigma:
# The sigma propagator is approximately constant: G_sigma ~ 1/m_sigma^2
# The Goldstone propagator in the loop gives a phase-space integral.
#
# In 2D (the internal T^2), the loop integral is:
#   I_2D = integral_0^{Lambda} dk k / (2pi) * 1/(m_sigma^2)
#        = Lambda^2 / (4pi * m_sigma^2)
# where Lambda is the UV cutoff (~ k_max on T^2).

# On T^2 with finite size, Lambda ~ N_max * k_fund where N_max is the
# maximum mode number before hitting the lattice cutoff.
# For the SU(3) Cartan torus, the lattice cutoff is at pi/a where a
# is the lattice spacing. In the continuum limit, the cutoff is set
# by the physical torus:
k_max_T2 = PI / (L_torus / 20)  # Rough UV cutoff (20 modes per side)
Lambda_UV = min(k_max_T2, 20 * k_fund)

print(f"\n  UV cutoff: Lambda = {Lambda_UV:.4f} M_KK")
print(f"  k_fund = {k_fund:.4f} M_KK")

# The one-loop self-energy:
#   Sigma_cubic = V_3^2 * Lambda^2 / (4*pi * m_sigma^2)
# This is a MASS RENORMALIZATION of the Goldstone.

Sigma_cubic_naive = V_3**2 * Lambda_UV**2 / (4 * PI * m_sigma**2)

print(f"\n  Naive one-loop Sigma_cubic:")
print(f"    = V_3^2 * Lambda^2 / (4*pi*m_sigma^2)")
print(f"    = {V_3**2:.6f} * {Lambda_UV**2:.4f} / ({4*PI:.4f} * {m_sigma**2:.6f})")
print(f"    = {Sigma_cubic_naive:.6f} M_KK^2")
m_eff_cubic_naive = np.sqrt(m_G**2 + Sigma_cubic_naive)
print(f"    m_eff = sqrt({m_G**2:.6f} + {Sigma_cubic_naive:.6f})")
print(f"    m_eff = {m_eff_cubic_naive:.6f} M_KK")
print(f"    Enhancement: {m_eff_cubic_naive / m_G:.2f}x")

# BUT WAIT: In a Nambu-Goldstone system, the self-energy of the Goldstone
# is PROTECTED by the Ward identity. The Goldstone theorem requires that
# the self-energy satisfies:
#   Sigma(omega=0, K=0) = 0
# This means the mass renormalization is EXACTLY CANCELLED by the
# tadpole diagram (the sigma field gets a VEV shift that exactly
# compensates the loop correction).
#
# The Ward identity forces:
#   m_eff^2 = 0 + O(explicit breaking)
# The explicit breaking in our system is the Josephson coupling (epsilon).
# So: m_eff^2 = m_G^2 = epsilon * J, which is ALREADY the physical mass.
# The cubic self-energy is ALREADY INCLUDED in the definition of m_G.

print("\n  WARD IDENTITY OBSTRUCTION:")
print("  The Goldstone theorem requires Sigma(0,0) = 0 for the NG mode.")
print("  Any self-energy correction is exactly cancelled by the tadpole")
print("  diagram (Goldstone-Higgs mixing shift of <sigma>).")
print("  The physical Goldstone mass m_G = 0.070 ALREADY includes all")
print("  perturbative self-energy corrections from the BCS system.")
print("  Additional enhancement requires EXPLICIT symmetry breaking")
print("  beyond the Josephson term that gives m_G.")

# ============================================================================
#  SECTION 8: What CAN enhance the mass?
# ============================================================================

print("\n" + "=" * 78)
print("SECTION 8: Sources of mass beyond Ward identity")
print("=" * 78)

# The Ward identity protects the Goldstone mass at m_G = sqrt(epsilon * J).
# To get m_eff >> m_G, we need sources of EXPLICIT U(1)_7 breaking
# beyond the Josephson coupling.
#
# Potential sources:
# 1. ADDITIONAL Josephson couplings from higher-order tunneling paths
#    (multiple domain wall crossings on the fabric)
# 2. GRAVITATIONAL corrections (the graviton couples to all modes)
# 3. FABRIC-SCALE effects (multiple cells coupling through domain walls)
# 4. ANOMALOUS breaking (topological terms that break U(1)_7)
#
# Of these, (3) is the most promising: the Goldstone mass on the FABRIC
# can differ from the single-cell Leggett mass because the fabric provides
# additional coupling pathways.
#
# On the fabric, the Goldstone propagates through N_cells = 32 cells.
# Each cell boundary is a Z_3 domain wall with impedance eta = 1/2 (S49).
# The inter-cell Josephson coupling J_fabric provides additional explicit breaking:
#   m_fabric^2 = m_single^2 + z * J_fabric
# where z is the coordination number (~ 6 for a Voronoi tessellation).

# From S49: J_12/J_23 = 19.52, epsilon = 0.00248
# The inter-cell coupling through a Z_3 domain wall with transmission T = 1 - eta = 1/2:
# J_wall = T * J_internal = 0.5 * J_eff
# But this is the SAME Josephson coupling that gives m_G!

# Actually, the single-cell Leggett mass is set by the INTER-SECTOR coupling
# within one cell (J_12 between B2 sectors). The INTER-CELL coupling through
# domain walls adds to this.
#
# The fabric Goldstone mass:
#   m_fabric^2 = m_Leggett^2 + sum_{neighbors} J_{cell-cell}
#
# Each Z_3 domain wall transmits with T = 1-eta = 1/2.
# The coupling through one wall: J_wall = T * c_BdG^2 / L_wall
# where L_wall is the wall thickness.

# From S49: barrier_width = 3.71 M_KK^{-1}
# J_wall = T * c_BdG^2 / barrier_width
T_wall = 0.5  # Transmission through Z_3 wall (eta = 1/2)
J_wall = T_wall * c_BdG**2 / barrier_width

# Coordination number for Voronoi with 32 cells: z ~ 6
z_coord = 6

# Fabric mass from inter-cell coupling:
m_fabric_sq = m_G**2 + z_coord * J_wall
m_fabric = np.sqrt(m_fabric_sq)

print(f"  Inter-cell Josephson coupling:")
print(f"    T_wall = {T_wall:.3f} (Z_3 impedance)")
print(f"    barrier_width = {barrier_width:.4f} M_KK^{{-1}}")
print(f"    J_wall = T * c^2 / L_wall = {J_wall:.4f} M_KK^2")
print(f"    z (coordination) = {z_coord}")
print(f"  Fabric mass:")
print(f"    m_fabric^2 = m_G^2 + z * J_wall")
print(f"    = {m_G**2:.6f} + {z_coord} * {J_wall:.6f}")
print(f"    = {m_fabric_sq:.6f}")
print(f"    m_fabric = {m_fabric:.4f} M_KK")
print(f"    Enhancement: {m_fabric / m_G:.1f}x")

# --- Acoustic metamaterial: effective medium from resonant cavities ---
# Even with the Ward identity, the EFFECTIVE mass seen by a wave
# propagating through a medium of resonant scatterers IS enhanced.
# This is because the effective medium theory gives:
#   m_eff^2(omega) = rho_eff(omega) / K_eff(omega)
# where rho_eff can be VERY DIFFERENT from rho_0 near a resonance.
#
# The acoustic metamaterial mass enhancement does NOT violate the
# Goldstone theorem because it is a MEDIUM property, not a self-energy.
# The Goldstone theorem protects the pole of the propagator:
#   G^{-1}(omega, K=0) = omega^2 - m_G^2 - Sigma(omega)
# and requires Sigma(0,0) = 0. But the EFFECTIVE mass in the
# dispersion relation:
#   omega^2 = m_eff^2 * K^2 + m_G^2
# can have m_eff >> m_G because m_eff is the INERTIAL mass
# (related to the band curvature), not the gap mass.

# In acoustic metamaterials (Liu et al. 2000, Paper 13):
# The effective mass density near a resonance at omega_0 is:
#   rho_eff(omega) = rho_0 * (1 - F * omega_0^2 / (omega_0^2 - omega^2))
# where F = (m_res / m_total) * (N_res / V) is the filling fraction.
#
# The INERTIAL mass for the Goldstone propagating through the cavity array:
#   m_eff^2 = m_G^2 / (1 - F * omega_0^2 / (omega_0^2 - m_G^2))
#
# For omega_0 >> m_G (our case: 0.800 >> 0.070):
#   m_eff^2 ≈ m_G^2 / (1 - F)
# Enhancement factor: 1/(1-F).
# For m_eff = 12 M_KK: need 1/(1-F) = (12/0.070)^2 = 29,400. Need F = 0.99997.
# That requires 99.997% of the mass to be in the resonators -- unrealistic.

# Let me compute F from the actual cavity data:
# Each cavity has effective mass m_cav ~ rho_BdG * V_cav
# V_cav = pi * R_eff^2 (2D volume = area)
# Total area: A_T2

total_cav_area = np.sum(PI * cavity_R_eff**2)  # Solved cavities
# Scale to all 111
total_cav_area_all = total_cav_area * (N_cav_total / N_cav_solved)
F_filling = total_cav_area_all / A_T2_sq

print(f"\n  Metamaterial filling fraction:")
print(f"    Solved cavity area: {total_cav_area:.4f} M_KK^{{-2}}")
print(f"    Scaled to 111 cavities: {total_cav_area_all:.4f} M_KK^{{-2}}")
print(f"    T^2 total area: {A_T2_sq:.4f} M_KK^{{-2}}")
print(f"    F = {F_filling:.4f}")

# This gives the metamaterial enhancement:
if F_filling < 1.0:
    m_eff_meta_sq = m_G**2 / (1 - F_filling)
    m_eff_meta = np.sqrt(m_eff_meta_sq)
    print(f"\n  Metamaterial effective mass:")
    print(f"    m_eff^2 = m_G^2 / (1 - F) = {m_eff_meta_sq:.6f}")
    print(f"    m_eff = {m_eff_meta:.6f} M_KK")
    print(f"    Enhancement: {m_eff_meta / m_G:.2f}x")
else:
    print(f"  F > 1: metamaterial picture breaks down")
    m_eff_meta = m_G

# --- Frequency-dependent enhancement (near-resonance) ---
# The frequency-dependent rho_eff gives a DIFFERENT enhancement at
# different frequencies. Near omega_0 = 0.800:
#   rho_eff(omega) = rho_0 * (1 - F * omega_0^2 / (omega_0^2 - omega^2))
# At omega = m_G = 0.070:
#   rho_eff(m_G) = rho_0 * (1 - F * 0.800^2 / (0.800^2 - 0.070^2))
#                = rho_0 * (1 - F * 0.640 / 0.635)
#                = rho_0 * (1 - F * 1.008)
# So rho_eff < 0 for F > 0.992. That's the negative effective mass
# regime -- but we need F < 1 for the effective medium to make sense.

omega_eval = m_G
for i, omega_0_local in enumerate(sorted(set(np.round(cavity_modes_all, 4)))):
    ratio = omega_0_local**2 / (omega_0_local**2 - omega_eval**2)
    if i < 5:
        print(f"  Cavity at {omega_0_local:.4f}: ratio = {ratio:.4f}")

rho_ratio = 1 - F_filling * cavity_modes_all[0]**2 / (cavity_modes_all[0]**2 - m_G**2)
print(f"\n  rho_eff/rho_0 at omega=m_G: {rho_ratio:.6f}")

# ============================================================================
#  SECTION 9: The real T-matrix calculation
# ============================================================================

print("\n" + "=" * 78)
print("SECTION 9: Full T-matrix on the fabric (proper treatment)")
print("=" * 78)

# The proper calculation:
# 1. The Goldstone propagates on the 4D fabric with dispersion
#    omega^2 = c^2 K^2 + m_G^2
# 2. At each cell, it enters the SU(3) fiber and can virtually excite
#    internal modes.
# 3. The T-matrix for a SINGLE CELL is:
#    t(omega) = sum_n |f_n|^2 / (omega_n^2 - omega^2 - i*Gamma_n*omega)
#    where f_n is the coupling of the propagating wave to internal mode n,
#    omega_n is the internal mode frequency, and Gamma_n is the damping.
#
# The coupling f_n for the propagating Goldstone to internal cavity mode n:
#
# KEY PHYSICS: The Goldstone is the U(1)_7 phase rotation. When it enters
# a cell, it rotates the phase of the BCS condensate. This phase rotation
# does NOT excite cavity modes because the cavity modes are DENSITY
# fluctuations, not phase fluctuations.
#
# In BCS theory:
#   - Phase fluctuations = Goldstone (Nambu-Goldstone boson)
#   - Amplitude fluctuations = Higgs (Anderson-Higgs boson)
#   - Cavity modes = quasiparticle excitations above the gap
#
# The Goldstone couples to the Higgs through the GRADIENT (the sigma*phi^2
# vertex). The Higgs couples to quasiparticles. So the coupling chain is:
#   Goldstone -> Higgs (virtual) -> Quasiparticle/cavity modes
#
# The effective coupling:
#   f_n = V_3 * G_Higgs(omega) * <Higgs|V|cavity_n>
#       = (4*b_GL*Delta_0) * 1/(m_sigma^2 - omega^2) * V_BCS * <Higgs|QP_n>
#
# But the Higgs-quasiparticle coupling <Higgs|QP_n> is:
#   <Higgs|QP_n> = u_n * v_n (BCS coherence factors)
# Near the gap edge: u*v ~ 1/2. For modes far from the gap: u*v -> 0.

# For the cavity modes at omega_cav = 0.800 M_KK:
# These are above the BCS gap Delta_B2 = 0.855?
# Wait: the BCS gap is Delta = 0.855, and the quasiparticle energy is:
#   E_qp = sqrt(epsilon_k^2 + Delta^2) >= Delta = 0.855
# The PAIR-BREAKING threshold is 2*Delta = 1.71 M_KK.
# The cavity modes at 0.800 are BELOW the gap.
#
# Hmm, but the cavity modes from S49 are eigenvalues of the ACOUSTIC
# Helmholtz equation on T^2, not BdG quasiparticle energies. They are
# acoustic resonances of the sound field inside subsonic cavities.
#
# These acoustic cavity modes interact with the Goldstone through
# the speed-of-sound modulation: as the Goldstone oscillates, it
# modifies c_BdG locally, which shifts the cavity frequencies.
# But this is the PARAMETRIC coupling (Mechanism A), which we already
# computed gives tiny enhancement because epsilon = 0.00248.

# Let me compute the parametric coupling MORE carefully.
# The Goldstone modulates the inter-sector phase: phi_1 - phi_2.
# The BdG sound speed depends on the gap: c_BdG ~ v_F * Delta / E_F
# The gap depends on the relative phase: Delta(phi) = Delta_0 * cos(phi/2)
# So: d(c_BdG)/d(phi) = c_BdG * (1/2) * d(ln Delta)/d(phi)
#                      = c_BdG * (-1/4) * sin(phi/2) / cos(phi/2)
# At phi = 0: d(c_BdG)/d(phi) = 0 (to first order).
# At phi = pi: diverges (gap closes).

# For SMALL phi oscillations:
#   delta_c / c_0 = -(1/8) * phi^2 + O(phi^4)
# So the LEADING coupling of phi to the sound speed is QUADRATIC in phi.
# This means the coupling of ONE Goldstone to cavity modes is:
#   H_int = (d^2 c / d phi^2) * phi_G^2 * (sum_n omega_n * n_cav_n)
# This is a SHIFT of the cavity frequency proportional to phi_G^2.
# For the self-energy, this gives a QUARTIC (phi^4) correction, not
# a mass (phi^2) correction.

# The mass correction from this mechanism:
# Sigma ~ (d^2c/dphi^2)^2 * sum_n omega_n^2 * <n_cav_n>_{T=0}
# At T=0: <n_cav_n> = 0 (no thermal population).
# But there IS zero-point motion: <n_cav_n + 1/2> = 1/2.

d2c_dphi2 = -c_BdG / 8  # Second derivative of c w.r.t. phase
Sigma_zp = (d2c_dphi2)**2 * np.sum(cavity_modes_all) / 2  # Zero-point contribution

print(f"  Parametric coupling (second order in phi):")
print(f"    d^2c/dphi^2 = -{c_BdG:.4f}/8 = {d2c_dphi2:.6f}")
print(f"    Sigma_zp = (d^2c/dphi^2)^2 * sum omega_n/2")
print(f"    = {d2c_dphi2**2:.6f} * {np.sum(cavity_modes_all)/2:.4f}")
print(f"    = {Sigma_zp:.6e} M_KK^2")
print(f"    Enhancement: sqrt((m_G^2 + Sigma_zp) / m_G^2) = "
      f"{np.sqrt((m_G**2 + Sigma_zp) / m_G**2):.4f}x")

# Scale to all 111 cavities (assume similar spectrum):
Sigma_zp_total = Sigma_zp * (N_cav_total / N_cav_solved)
m_eff_zp_sq = m_G**2 + Sigma_zp_total
m_eff_zp = np.sqrt(m_eff_zp_sq)

print(f"\n  Scaled to 111 cavities:")
print(f"    Sigma_zp_total = {Sigma_zp_total:.6e} M_KK^2")
print(f"    m_eff = {m_eff_zp:.4f} M_KK")
print(f"    Enhancement: {m_eff_zp / m_G:.1f}x")

# ============================================================================
#  SECTION 10: The CORRECT mechanism: 4D effective medium
# ============================================================================

print("\n" + "=" * 78)
print("SECTION 10: 4D effective medium theory")
print("=" * 78)

# The previous sections established that perturbative self-energy corrections
# to the Goldstone mass are either:
# (a) zero by orthogonality (Mechanisms A, B)
# (b) zero by Ward identity (cubic)
# (c) negligible (~10^{-6}) by quadratic parametric coupling
#
# But there is a NON-PERTURBATIVE mechanism: the effective medium theory
# of acoustic metamaterials.
#
# In acoustic metamaterials (Liu et al. 2000, Huang et al. 2009):
# The effective mass density rho_eff(omega) is DIFFERENT from the
# average density. It includes the resonant response of inclusions.
# Near a resonance at omega_0, rho_eff can be MUCH LARGER or even NEGATIVE.
#
# The key formula for a periodic medium with resonant inclusions:
#   rho_eff(omega) = rho_0 + N * f(omega)
# where N is the number density of resonators and f(omega) is the
# polarizability (T-matrix) of a single resonator.
#
# For a GOLDSTONE MODE on the fabric:
# The effective medium consists of 32 cells of SU(3) fibers, each containing
# internal acoustic resonances. The Goldstone is the long-wavelength
# SOUND mode propagating through this effective medium.
#
# The effective mass of the propagating mode is:
#   m_eff^2 = m_bare^2 * rho_eff(omega) / rho_0
#
# For the resonator polarizability:
#   f(omega) = sum_n g_n^2 / (omega_n^2 - omega^2 - i*Gamma_n*omega)
#
# The coupling g_n here is the SCATTERING CROSS-SECTION of the inclusion
# for the propagating wave, NOT the quantum mechanical matrix element.
# In acoustic metamaterials, this is set by the GEOMETRY of the scatterer,
# not by quantum mechanics.

# For the SU(3) fiber as an acoustic scatterer:
# The Goldstone wave propagates in 4D. When it hits a fiber, it enters
# the 6D internal space. The scattering is determined by the boundary
# conditions at the fiber entrance.
#
# The scattering strength is set by:
#   g_n ~ (L_fiber / lambda_G)^d * overlap
# where L_fiber is the size of the fiber, lambda_G is the Goldstone wavelength,
# and d is the dimensionality.
#
# For the Goldstone: lambda_G = 2*pi*c / m_G = 2*pi*0.7507/0.070 = 67.4 M_KK^{-1}
lambda_G = 2 * PI * c_BdG / m_G

# The fiber size is R_fiber ~ 1 M_KK^{-1} (internal dimensions at KK scale)
R_fiber = 1.0  # M_KK^{-1}

# The scattering parameter:
x_scatter = 2 * PI * R_fiber / lambda_G  # = R_fiber * m_G / c_BdG
print(f"  Goldstone wavelength: lambda_G = {lambda_G:.2f} M_KK^{{-1}}")
print(f"  Fiber radius: R_fiber ~ {R_fiber:.1f} M_KK^{{-1}}")
print(f"  Scattering parameter: x = 2*pi*R/lambda = {x_scatter:.4f}")
print(f"  This is the DEEP SUB-WAVELENGTH regime (x << 1).")

# In the sub-wavelength regime, the scattering cross section is:
#   sigma_scat ~ x^4 * pi * R^2  (Rayleigh scattering for d=3)
# For d dimensions: sigma ~ x^{2d} * R^{d-1} * pi
# This is VERY SMALL. The fiber is 67x smaller than the Goldstone wavelength.

sigma_Rayleigh = x_scatter**4 * PI * R_fiber**2  # 3D Rayleigh
print(f"  Rayleigh cross section (3D): sigma ~ {sigma_Rayleigh:.2e} M_KK^{{-2}}")
print(f"  Ratio sigma / A_fiber: {sigma_Rayleigh / (PI * R_fiber**2):.2e}")

# The metamaterial enhancement from N resonant scatterers:
# In the effective medium, the mass correction is:
#   delta_m^2 / m^2 = N * sigma_res / A_cell
# where sigma_res is the RESONANT scattering cross section.
# Near resonance: sigma_res >> sigma_Rayleigh by a factor of (omega_0/Gamma)^2.
# But the resonance is at omega_0 = 0.800 and we are at omega = 0.070,
# which is 11.4x BELOW resonance.
# Off-resonance: sigma_res ~ sigma_Rayleigh * omega_0^4 / (omega_0^2 - omega^2)^2
#              ~ sigma_Rayleigh * 1.005 (for omega << omega_0)
# No enhancement.

# The RESONANT enhancement mechanism requires omega ~ omega_0, which means
# the Goldstone frequency must be NEAR a cavity resonance. It is not.
# The ratio omega_G / omega_cav_min = 0.070 / 0.800 = 0.0875.
# This is 11.4x below the first resonance.

freq_ratio = m_G / cavity_modes_all[0]
print(f"\n  omega_G / omega_cav_min = {freq_ratio:.4f}")
print(f"  The Goldstone sits {1/freq_ratio:.1f}x below the first cavity resonance.")
print(f"  This is far from resonance; no metamaterial enhancement.")

# ============================================================================
#  SECTION 11: Systematic assessment of g^2_eff
# ============================================================================

print("\n" + "=" * 78)
print("SECTION 11: Systematic coupling estimate")
print("=" * 78)

# Let me now compute the T-matrix self-energy using EVERY coupling estimate
# and check whether ANY mechanism gives g^2_eff >= 10 M_KK^4.

# The self-energy structure:
#   Re[Sigma(omega)] = sum_n g_n^2 * omega_n^2 / (omega_n^2 - omega^2)
# At omega = m_G = 0.070, for omega_0 = 0.800:
#   omega_0^2 / (omega_0^2 - m_G^2) = 0.640 / 0.635 = 1.008

# Denominator for each mode:
denom = cavity_modes_all**2 - m_G**2  # All positive (omega > m_G)
weight = cavity_modes_all**2 / denom  # ~ 1.008 for lowest mode

# --- Coupling estimates ---

# 1. Josephson parametric: g_n^2 = epsilon^2 * m_G^2 * omega_n
g2_param = epsilon_Leggett**2 * m_G**2 * cavity_modes_all
Sigma_param = np.sum(g2_param * weight / denom)

# 2. Texture Born (second order): g_n^2 = V_rms^2 * f_overlap / N_modes
# f_overlap = xi_loc^2 / A_T2, N_modes = 30
# BUT this is killed by orthogonality. Setting g2 = 0 (exact result).
g2_texture = 0.0
Sigma_texture = 0.0

# 3. Zero-point parametric: g_n^2 = (d^2c/dphi^2)^2 * omega_n^{-1}
g2_zp = d2c_dphi2**2 / cavity_modes_all
Sigma_zp_full = np.sum(g2_zp * weight / denom)

# 4. BCS vertex (4-phonon): g_n^2 = V_{B2B2}^2 * (u*v)^2 * f_overlap
# u*v ~ 0.5 near gap edge
g2_BCS = V_B2B2**2 * 0.25 * f_overlap * np.ones(len(cavity_modes_all))
Sigma_BCS = np.sum(g2_BCS * weight / denom)

# 5. Cubic + Ward: g_n^2 = 0 (Ward identity cancels)
g2_cubic = 0.0
Sigma_cubic = 0.0

print(f"  Coupling mechanism      |  g^2_eff (M_KK^4)  |  Re[Sigma] (M_KK^2)  |  m_eff (M_KK)")
print(f"  {'-'*24}|{'-'*20}|{'-'*22}|{'-'*15}")

results = {}
for name, g2_total, Sigma_val in [
    ("Parametric (epsilon^2)", np.sum(g2_param), Sigma_param),
    ("Texture (orthogonal=0)", g2_texture, Sigma_texture),
    ("Zero-point parametric", np.sum(g2_zp), Sigma_zp_full),
    ("BCS 4-phonon vertex", np.sum(g2_BCS), Sigma_BCS),
    ("Cubic (Ward=0)", g2_cubic, Sigma_cubic),
]:
    m_sq = m_G**2 + Sigma_val
    m_eff = np.sqrt(max(0, m_sq))
    print(f"  {name:24s}|  {g2_total:16.4e}  |  {Sigma_val:18.6e}  |  {m_eff:.6f}")
    results[name] = {'g2': g2_total, 'Sigma': Sigma_val, 'm_eff': m_eff}

# Combined (sum of all non-zero mechanisms):
Sigma_total = Sigma_param + Sigma_zp_full + Sigma_BCS
g2_total_all = np.sum(g2_param) + np.sum(g2_zp) + np.sum(g2_BCS)
m_eff_total = np.sqrt(m_G**2 + Sigma_total)
print(f"  {'COMBINED':24s}|  {g2_total_all:16.4e}  |  {Sigma_total:18.6e}  |  {m_eff_total:.6f}")

# Scale to 111 cavities:
Sigma_total_111 = Sigma_total * (N_cav_total / N_cav_solved)
g2_total_111 = g2_total_all * (N_cav_total / N_cav_solved)
m_eff_111 = np.sqrt(m_G**2 + Sigma_total_111)

print(f"\n  Scaled to 111 cavities:")
print(f"  {'COMBINED (111)':24s}|  {g2_total_111:16.4e}  |  {Sigma_total_111:18.6e}  |  {m_eff_111:.6f}")

# ============================================================================
#  SECTION 12: Physical analysis — why coupling is weak
# ============================================================================

print("\n" + "=" * 78)
print("SECTION 12: Physical analysis — why coupling is weak")
print("=" * 78)

# Three structural reasons:
# 1. ZERO-MODE PROTECTION (S50, permanent): <0|V|n> = 0 for all n.
#    Kills all single-insertion couplings to ALL ORDERS in perturbation theory.
#    The Goldstone is a uniform zero-mode; it cannot couple to ANY localized
#    internal state through any operator diagonal in position.
#
# 2. WARD IDENTITY: The Goldstone theorem forces Sigma(0,0) = 0 for the NG mode.
#    Any perturbative mass renormalization is exactly cancelled by the tadpole.
#    The physical mass m_G = 0.070 ALREADY includes all self-energy corrections.
#
# 3. SUB-WAVELENGTH RATIO: lambda_G / R_fiber = 67. The Goldstone wavelength
#    is 67x larger than the fiber. Scattering is in the deep Rayleigh regime
#    (cross-section ~ (R/lambda)^4). No resonant enhancement because the
#    Goldstone frequency (0.070) is 11x below the first cavity resonance (0.800).

print("  THREE STRUCTURAL OBSTRUCTIONS:")
print(f"  1. Zero-mode protection: <0|V|n> = 0 (kills all Born terms)")
print(f"  2. Ward identity: Sigma(0,0) = 0 (protects NG mass)")
print(f"  3. Sub-wavelength: lambda_G/R = {lambda_G/R_fiber:.0f}x, "
      f"omega_G/omega_cav = {freq_ratio:.3f}")
print(f"\n  Together these give g^2_eff = {g2_total_111:.2e} M_KK^4")
print(f"  This is {g2_total_111:.1e} / 10 = {g2_total_111/10:.1e}x the FAIL threshold.")

# --- Compute what coupling WOULD be needed ---
m_target = 12.0  # Target mass (M_KK)
Sigma_needed = m_target**2 - m_G**2  # = 143.995
# From the cavity spectrum with unit coupling:
# Sigma = g^2 * sum_n omega_n^2 / (omega_n^2 - m_G^2)
sum_weight = np.sum(weight / denom)  # Sum of 1/(omega_n^2 - m_G^2)
# Scaled to 111 cavities:
sum_weight_111 = sum_weight * (N_cav_total / N_cav_solved)

g2_needed = Sigma_needed / sum_weight_111
print(f"\n  Required coupling for m_eff = {m_target} M_KK:")
print(f"    Sigma_needed = {Sigma_needed:.4f} M_KK^2")
print(f"    sum weight (111 cav) = {sum_weight_111:.4e}")
print(f"    g^2_needed = {g2_needed:.4f} M_KK^4")
print(f"    g_needed = {np.sqrt(g2_needed):.4f} M_KK^2")
print(f"\n  Actual g^2_eff / g^2_needed = {g2_total_111 / g2_needed:.2e}")
print(f"  SHORTFALL: {g2_needed / max(g2_total_111, 1e-30):.1e}x")

# ============================================================================
#  SECTION 13: Frequency sweep — m_eff(omega)
# ============================================================================

print("\n" + "=" * 78)
print("SECTION 13: Frequency sweep of effective mass")
print("=" * 78)

# Compute m_eff(omega) across the spectrum to visualize where enhancement occurs
omega_sweep = np.linspace(0.01, 0.95 * cavity_modes_all.min(), 500)

# Using the LARGEST coupling mechanism (zero-point parametric):
g2_per_mode_zp = d2c_dphi2**2  # constant coupling for simplicity
Sigma_sweep = np.zeros_like(omega_sweep)
for w_cav in cavity_modes_all:
    Sigma_sweep += g2_per_mode_zp / (w_cav**2 - omega_sweep**2)
# Scale to 111 cavities
Sigma_sweep *= (N_cav_total / N_cav_solved)

m_eff_sweep = np.sqrt(np.maximum(m_G**2 + Sigma_sweep, 0))

print(f"  omega range: [{omega_sweep[0]:.3f}, {omega_sweep[-1]:.3f}] M_KK")
print(f"  m_eff at omega=0.01: {m_eff_sweep[0]:.6f} M_KK")
print(f"  m_eff at omega=m_G:  {m_eff_sweep[np.argmin(np.abs(omega_sweep - m_G))]:.6f} M_KK")
print(f"  m_eff at omega=0.7:  {m_eff_sweep[np.argmin(np.abs(omega_sweep - 0.7))]:.6f} M_KK")
print(f"  Maximum m_eff: {m_eff_sweep.max():.6f} M_KK at omega = {omega_sweep[np.argmax(m_eff_sweep)]:.4f}")

# ============================================================================
#  SECTION 14: Gate verdict
# ============================================================================

print("\n" + "=" * 78)
print("SECTION 14: GATE VERDICT — LOCAL-RESONANCE-51")
print("=" * 78)

# The effective mass from the T-matrix self-energy:
m_eff_final = m_eff_111
g2_eff_final = g2_total_111

# Gate criteria:
# PASS: m_eff in [8, 16] M_KK
# FAIL: g^2_eff < 10 M_KK^4
# INFO: m_eff > 1 but < 8 M_KK

if 8.0 <= m_eff_final <= 16.0:
    verdict = "PASS"
    detail = f"m_eff = {m_eff_final:.4f} M_KK in target window [8, 16]"
elif g2_eff_final < 10.0:
    verdict = "FAIL"
    detail = (f"g^2_eff = {g2_eff_final:.2e} M_KK^4 < 10 M_KK^4. "
              f"Three structural obstructions: (1) zero-mode protection kills all "
              f"Born-series couplings, (2) Ward identity forces Sigma(0,0)=0 for NG mode, "
              f"(3) sub-wavelength ratio lambda_G/R={lambda_G/R_fiber:.0f}x suppresses "
              f"scattering to Rayleigh regime. Largest mechanism is zero-point "
              f"parametric: Sigma_zp = {Sigma_zp_total:.2e} M_KK^2, giving "
              f"m_eff = {m_eff_zp:.4f} M_KK. Enhancement {m_eff_zp/m_G:.1f}x is "
              f"negligible versus the 170x required.")
elif m_eff_final > 1.0:
    verdict = "INFO"
    detail = f"m_eff = {m_eff_final:.4f} M_KK (partial enhancement but < 8 M_KK)"
else:
    verdict = "FAIL"
    detail = f"m_eff = {m_eff_final:.4f} M_KK < 1 M_KK (negligible enhancement)"

print(f"\n  VERDICT: {verdict}")
print(f"  DETAIL: {detail}")
print(f"\n  m_eff (5 solved cavities): {m_eff_total:.6f} M_KK")
print(f"  m_eff (111 cavities):       {m_eff_111:.6f} M_KK")
print(f"  g^2_eff (111 cavities):     {g2_total_111:.4e} M_KK^4")
print(f"  g^2_needed for m=12:        {g2_needed:.4f} M_KK^4")
print(f"  Shortfall:                   {g2_needed / max(g2_total_111, 1e-30):.1e}x")

# ============================================================================
#  SECTION 15: Generate plot
# ============================================================================

print("\n" + "=" * 78)
print("SECTION 15: Generating plot")
print("=" * 78)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel 1: Cavity mode spectrum
ax1 = axes[0, 0]
ax1.hist(cavity_modes_all, bins=20, color='steelblue', edgecolor='black', alpha=0.7)
ax1.axvline(m_G, color='red', ls='--', lw=2, label=f'$m_G = {m_G:.3f}$')
ax1.set_xlabel('$\\omega$ ($M_{KK}$)')
ax1.set_ylabel('Count')
ax1.set_title('Cavity Mode Spectrum (5 solved cavities)')
ax1.legend()

# Panel 2: T-matrix self-energy vs frequency
ax2 = axes[0, 1]
ax2.semilogy(omega_sweep, np.abs(Sigma_sweep), 'b-', lw=1.5, label='$|\\mathrm{Re}[\\Sigma(\\omega)]|$')
ax2.axvline(m_G, color='red', ls='--', lw=1.5, label=f'$m_G = {m_G:.3f}$')
ax2.axvline(cavity_modes_all.min(), color='green', ls='--', lw=1.5,
            label=f'$\\omega_{{cav,min}} = {cavity_modes_all.min():.3f}$')
ax2.axhline(Sigma_needed, color='orange', ls=':', lw=1.5, label=f'$\\Sigma_{{needed}} = {Sigma_needed:.1f}$')
ax2.set_xlabel('$\\omega$ ($M_{KK}$)')
ax2.set_ylabel('$|\\mathrm{Re}[\\Sigma]|$ ($M_{KK}^2$)')
ax2.set_title('T-matrix self-energy (zero-point parametric)')
ax2.legend(fontsize=8)

# Panel 3: Coupling comparison
ax3 = axes[1, 0]
mechanisms = ['Parametric\n($\\epsilon^2$)', 'Zero-point\nparametric',
              'BCS\n4-phonon', 'Texture\n(=0)', 'Cubic\n(Ward=0)', 'NEEDED']
g2_values = [np.sum(g2_param) * (N_cav_total / N_cav_solved),
             np.sum(g2_zp) * (N_cav_total / N_cav_solved),
             np.sum(g2_BCS) * (N_cav_total / N_cav_solved),
             1e-30, 1e-30, g2_needed]
colors = ['steelblue', 'darkorange', 'green', 'gray', 'gray', 'red']
ax3.bar(mechanisms, [max(v, 1e-30) for v in g2_values], color=colors,
        edgecolor='black', alpha=0.7)
ax3.set_yscale('log')
ax3.set_ylabel('$g^2_{eff}$ ($M_{KK}^4$)')
ax3.set_title('Coupling strength by mechanism (111 cavities)')
ax3.axhline(10.0, color='red', ls=':', lw=1.5, label='FAIL threshold')
ax3.legend()

# Panel 4: Summary text
ax4 = axes[1, 1]
ax4.axis('off')
summary = (
    f"LOCAL-RESONANCE-51: {verdict}\n"
    f"{'='*40}\n\n"
    f"Target: m_eff = 12 M_KK\n"
    f"Actual: m_eff = {m_eff_111:.6f} M_KK\n"
    f"Bare:   m_G   = {m_G:.4f} M_KK\n"
    f"Ratio:  m_eff/m_G = {m_eff_111/m_G:.4f}\n\n"
    f"g^2_eff = {g2_total_111:.2e} M_KK^4\n"
    f"g^2_needed = {g2_needed:.2f} M_KK^4\n"
    f"Shortfall: {g2_needed/max(g2_total_111, 1e-30):.1e}x\n\n"
    f"STRUCTURAL OBSTRUCTIONS:\n"
    f"1. Zero-mode: <0|V|n> = 0 (all orders)\n"
    f"2. Ward identity: Sigma(0,0) = 0\n"
    f"3. Sub-wavelength: lambda/R = {lambda_G/R_fiber:.0f}x"
)
ax4.text(0.05, 0.95, summary, transform=ax4.transAxes, fontsize=10,
         verticalalignment='top', fontfamily='monospace',
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

plt.tight_layout()
plt.savefig(str(OUT_DIR / 's51_local_resonance.png'), dpi=150, bbox_inches='tight')
print(f"  Saved: tier0-computation/s51_local_resonance.png")

# ============================================================================
#  SECTION 16: Save data
# ============================================================================

print("\n" + "=" * 78)
print("SECTION 16: Saving results")
print("=" * 78)

np.savez(str(OUT_DIR / 's51_local_resonance.npz'),
    # Gate
    gate_name='LOCAL-RESONANCE-51',
    gate_verdict=verdict,
    gate_detail=detail,
    # Input parameters
    m_G=m_G,
    c_BdG=c_BdG,
    V_rms=V_rms,
    l_corr=l_corr,
    epsilon_Leggett=epsilon_Leggett,
    L_phys=L_phys,
    R_fiber=R_fiber,
    lambda_G=lambda_G,
    # Cavity data
    cavity_modes=cavity_modes_all,
    n_cavities_solved=n_cavities_solved,
    n_cavities_total=N_cav_total,
    omega_cav_min=cavity_modes_all.min(),
    # Coupling results
    g2_parametric=np.sum(g2_param) * (N_cav_total / N_cav_solved),
    g2_zeropoint=np.sum(g2_zp) * (N_cav_total / N_cav_solved),
    g2_BCS_4phonon=np.sum(g2_BCS) * (N_cav_total / N_cav_solved),
    g2_texture=0.0,
    g2_cubic_ward=0.0,
    g2_eff_total=g2_total_111,
    g2_needed=g2_needed,
    # Self-energy results
    Sigma_parametric=Sigma_param * (N_cav_total / N_cav_solved),
    Sigma_zeropoint=Sigma_zp_total,
    Sigma_BCS=Sigma_BCS * (N_cav_total / N_cav_solved),
    Sigma_total=Sigma_total_111,
    Sigma_needed=Sigma_needed,
    # Effective mass
    m_eff_5cav=m_eff_total,
    m_eff_111cav=m_eff_111,
    m_eff_fabric=m_fabric,
    m_eff_target=m_target,
    enhancement_ratio=m_eff_111 / m_G,
    shortfall=g2_needed / max(g2_total_111, 1e-30),
    # Structural analysis
    freq_ratio=freq_ratio,
    filling_fraction=F_filling,
    scattering_param=x_scatter,
    f_overlap=f_overlap,
    # Sweep data
    omega_sweep=omega_sweep,
    Sigma_sweep=Sigma_sweep,
    m_eff_sweep=m_eff_sweep,
)

print(f"  Saved: tier0-computation/s51_local_resonance.npz")

# ============================================================================
#  SECTION 17: Summary
# ============================================================================

print("\n" + "=" * 78)
print("SUMMARY: LOCAL-RESONANCE-51")
print("=" * 78)
print(f"""
  Gate: LOCAL-RESONANCE-51
  Verdict: {verdict}

  The acoustic metamaterial mechanism (T-matrix self-energy from virtual
  excitation of internal cavity modes) CANNOT produce the required mass
  enhancement from m_G = {m_G:.4f} to m_target = {m_target:.0f} M_KK.

  Three STRUCTURAL obstructions block the coupling:

  1. ZERO-MODE PROTECTION (S50, permanent):
     The Goldstone is the n=0 KK mode with constant wavefunction on T^2.
     <0|V|n> = 0 for ALL internal eigenstates n, to ALL ORDERS in the
     Born series. This kills all T-matrix terms that begin with a
     position-diagonal operator acting on the zero-mode.

  2. WARD IDENTITY (Goldstone theorem):
     The self-energy of the Nambu-Goldstone boson satisfies Sigma(0,0) = 0.
     Any cubic self-energy correction is exactly cancelled by the tadpole
     (shift of the Higgs VEV). The physical mass m_G = {m_G:.4f} ALREADY
     includes all perturbative self-energy corrections.

  3. SUB-WAVELENGTH SUPPRESSION:
     lambda_G / R_fiber = {lambda_G/R_fiber:.0f}. The Goldstone wavelength is
     {lambda_G/R_fiber:.0f}x larger than the internal fiber. Scattering is in the
     deep Rayleigh regime (sigma ~ (R/lambda)^4 ~ {x_scatter**4:.1e}).
     The first cavity resonance at omega = {cavity_modes_all.min():.3f} is {1/freq_ratio:.1f}x
     above the Goldstone frequency — no resonant enhancement.

  Largest surviving coupling: zero-point parametric
     Sigma_zp = {Sigma_zp_total:.2e} M_KK^2
     m_eff = {m_eff_zp:.4f} M_KK ({m_eff_zp/m_G:.2f}x enhancement)

  Required for m=12: g^2 = {g2_needed:.1f} M_KK^4
  Actual g^2_eff:    {g2_total_111:.2e} M_KK^4
  Shortfall:         {g2_needed/max(g2_total_111, 1e-30):.1e}x
""")
