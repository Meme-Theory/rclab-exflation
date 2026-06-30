#!/usr/bin/env python3
"""
Z2-BAW-ANALOG-69: Design a BAW experiment testing Z_2 selection rule
=====================================================================

Gate: Z2-BAW-69 -- INFO (design study)
Session: S69, Wave 5, Task W5-C

Physics Summary
---------------
S67 LEGGETT-GRAV-DECAY-67 proved that the Z_2 parity of the spectral
action's a_2 moment (a_2(phi) = a_2(-phi), from the cos(phi_{23})
structure of the BCS gap) forbids single-Leggett gravitational decay
EXACTLY: Gamma_single = 0 to all orders.

This script designs an acoustic analog experiment to test this selection
rule in a BAW (bulk acoustic wave) resonator. The mapping:

  Substrate Leggett mode  -->  BAW breathing mode (even, l=0 radial)
  Gravitational channel    -->  Quadratic strain coupling H ~ x_A^2 x_B
  Waveguide / bath mode   -->  BAW dipole mode (odd, l=1 radial)

The Z_2 parity of the breathing mode under x_A -> -x_A guarantees that
the coupling H_int = g * x_A^2 * x_B changes Leggett number by 0 or +-2,
never by 1. Single breathing-phonon decay is FORBIDDEN.

Platform: Chu et al. 2017 (Science 358, 199) HBAR + transmon qubit.
Sapphire substrate, AlN piezoelectric transducer.

Output: s69_z2_baw.npz
"""

import sys
import os
import numpy as np

# Add computations to path for canonical_constants
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    PI, hbar_SI, k_B_SI, c_light, G_N,
    M_Pl_reduced, M_KK, hbar_GeV_s,
    omega_L1, omega_L2, E_cond, J_C2
)

print("=" * 72)
print("Z2-BAW-ANALOG-69: Breathing-Mode Selection Rule BAW Experiment")
print("=" * 72)

# ==========================================================================
# SECTION 1: BAW Resonator Parameters (from Chu et al. 2017)
# ==========================================================================
print("\n--- SECTION 1: BAW Resonator Parameters ---")

# Sapphire substrate
h_sub = 420e-6         # m, substrate thickness (Chu 2017)
d_disk = 200e-6        # m, AlN disk diameter
v_l_sapphire = 11100   # m/s, longitudinal sound speed in sapphire (c-axis)
v_t_sapphire = 6040    # m/s, transverse sound speed
rho_sapphire = 3980    # kg/m^3, sapphire density

# AlN piezoelectric layer
h_AlN = 900e-9         # m, AlN thickness
e33_AlN = 1.55         # C/m^2, piezoelectric coefficient (c-axis)  # (local)
c33_AlN = 395e9        # Pa, elastic stiffness c_{33}
d33_AlN = e33_AlN / c33_AlN  # m/V, piezoelectric strain coefficient

# Free spectral range (longitudinal modes)
nu_FSR = v_l_sapphire / (2 * h_sub)  # Hz
omega_FSR = 2 * PI * nu_FSR

print(f"Substrate: sapphire, h = {h_sub*1e6:.0f} um, d = {d_disk*1e6:.0f} um")
print(f"v_l = {v_l_sapphire} m/s, v_t = {v_t_sapphire} m/s, rho = {rho_sapphire} kg/m^3")
print(f"FSR = {nu_FSR/1e6:.2f} MHz = {omega_FSR/(2*PI*1e6):.2f} MHz")
print(f"AlN: h = {h_AlN*1e9:.0f} nm, e33 = {e33_AlN} C/m^2, c33 = {c33_AlN/1e9:.0f} GPa")

# ==========================================================================
# SECTION 2: Mode Structure -- Breathing (even) vs Dipole (odd)
# ==========================================================================
print("\n--- SECTION 2: Mode Structure ---")

# Breathing mode: l=even longitudinal, m=0 radial (J_0 profile)
# Strain: s_breath(z,r) = sin(l*pi*z/h) * J_0(j_{0,1}*2r/d)
# This has EVEN parity under z -> h-z (for even l) and r -> r (always even)
#
# Dipole mode: l=odd longitudinal, m=1 radial (J_1 profile)
# Strain: s_dipole(z,r,phi) = sin(l*pi*z/h) * J_1(j_{1,1}*2r/d) * cos(phi)
# This has ODD parity under azimuthal reflection phi -> -phi

# Bessel zeros
j01 = 2.40483    # first zero of J_0
j11 = 3.83171    # first zero of J_1

# Choose mode numbers for near-degeneracy
# We want omega_A (breathing) ~ 2 * omega_B (dipole) for parametric down-conversion test
# or omega_A ~ omega_B for direct coupling test

# Longitudinal mode numbers
l_breath = 32   # even longitudinal number (breathing)
l_dipole = 31   # odd longitudinal number (dipole)

# Mode frequencies (Chu eq. 2)
def omega_mode(l, m_radial, j_mn):
    """BAW mode frequency: omega = sqrt( (l*pi/h)^2 * v_l^2 + (2*j_mn/d)^2 * v_t^2 )"""
    k_z = l * PI / h_sub
    k_r = 2 * j_mn / d_disk
    return np.sqrt((k_z * v_l_sapphire)**2 + (k_r * v_t_sapphire)**2)

omega_A = omega_mode(l_breath, 0, j01)   # breathing: (l=32, m=0)
omega_B = omega_mode(l_dipole, 1, j11)   # dipole: (l=31, m=1)
nu_A = omega_A / (2 * PI)
nu_B = omega_B / (2 * PI)
delta_nu = abs(nu_A - nu_B)

print(f"\nBreathing mode A: l={l_breath} (even), m=0 (J_0)")
print(f"  omega_A / 2pi = {nu_A/1e9:.4f} GHz")
print(f"Dipole mode B: l={l_dipole} (odd), m=1 (J_1)")
print(f"  omega_B / 2pi = {nu_B/1e9:.4f} GHz")
print(f"Detuning: |nu_A - nu_B| = {delta_nu/1e6:.2f} MHz")
print(f"FSR ratio: delta_nu / FSR = {delta_nu/nu_FSR:.3f}")

# Zero-point fluctuation amplitudes
# x_ZPF = sqrt(hbar / (2 * m_eff * omega))
# Effective mass for HBAR mode ~ rho * V_mode / 2 (standing wave average)
V_mode = PI * (d_disk/2)**2 * h_sub  # cylindrical mode volume
m_eff_A = rho_sapphire * V_mode / 2
m_eff_B = rho_sapphire * V_mode / 2

x_zpf_A = np.sqrt(hbar_SI / (2 * m_eff_A * omega_A))
x_zpf_B = np.sqrt(hbar_SI / (2 * m_eff_B * omega_B))

print(f"\nMode volume: V = {V_mode*1e18:.2f} * 10^-18 m^3 = {V_mode*1e18:.2f} um^3")
print(f"Effective mass: m_eff = {m_eff_A*1e12:.3f} pg")
print(f"x_zpf(A) = {x_zpf_A:.3e} m = {x_zpf_A*1e15:.3f} fm")
print(f"x_zpf(B) = {x_zpf_B:.3e} m = {x_zpf_B*1e15:.3f} fm")

# ==========================================================================
# SECTION 3: Parity Analysis -- The Z_2 Selection Rule
# ==========================================================================
print("\n--- SECTION 3: Z_2 Parity Analysis ---")

# The breathing mode has EVEN parity: P|n_A> = (-1)^0 |n_A> = +|n_A>
# Under parity x_A -> -x_A, the breathing mode displacement is even
# because it's a radial (J_0) mode: u(r) = J_0(k_r * r) is even under
# any reflection through the center.
#
# The dipole mode has ODD parity: P|n_B> = (-1)^1 |n_B> = -|n_B>
# because J_1(k_r * r) * cos(phi) -> -J_1(k_r * r) * cos(phi) under
# reflection phi -> phi + pi.
#
# GRAVITATIONAL ANALOG COUPLING:
# The a_2 spectral moment depends on eigenvalue magnitudes |E_n|^2, which
# depend on cos(phi_{23}). This means H_grav ~ a_2(phi) ~ sum of even
# powers of phi. The analog in the BAW system:
#
#   H_int = lambda_2 * x_A^2 * x_B + lambda_4 * x_A^4 * x_B + ...
#
# where x_A is the breathing mode amplitude and x_B is the bath/dipole
# mode. The key point: x_A appears ONLY in EVEN powers.
#
# Parity of coupling vertex:
#   x_A^2 * x_B changes phonon number by: Delta n_A = 0, +-2 and Delta n_B = +-1
#   x_A * x_B (if it existed) would change n_A by +-1 -- FORBIDDEN by Z_2.
#
# In the quantum description:
#   x_A = x_zpf_A * (a + a^dagger)
#   x_A^2 = x_zpf_A^2 * (a + a^dagger)^2 = x_zpf_A^2 * (a^2 + a^{dagger 2} + 2a^dag a + 1)
#
# The process 1_A -> 0_A + 1_B requires a LINEAR coupling in x_A.
# With Z_2 symmetry, only x_A^2 * x_B exists. This means:
#   2_A -> 0_A + 1_B (pair annihilation) -- ALLOWED
#   1_A -> 0_A + 1_B (single decay)     -- FORBIDDEN

print("Parity assignments:")
print(f"  Breathing mode A (J_0, l=even): P_A = +1  (even)")
print(f"  Dipole mode B (J_1, l=odd):     P_B = -1  (odd)")
print()
print("Coupling Hamiltonian (Z_2 symmetric):")
print("  H_int = lambda_2 * x_A^2 * x_B  (lowest allowed vertex)")
print("  => x_A^{odd} * x_B terms FORBIDDEN by Z_2 parity")
print()
print("Selection rules:")
print("  1_A -> 0_A + 1_B :  FORBIDDEN  (requires x_A^1 vertex)")
print("  2_A -> 0_A + 1_B :  ALLOWED    (uses x_A^2 vertex)")
print("  2_A -> 0_A + 2_B :  FORBIDDEN  (energy conservation: 2*omega_A != 2*omega_B)")

# ==========================================================================
# SECTION 4: Coupling Strength Estimation
# ==========================================================================
print("\n--- SECTION 4: Coupling Strength Estimation ---")

# Nonlinear elastic coupling in sapphire
# Third-order elastic constant C_{333} ~ -800 GPa for sapphire (c-axis)
# (from literature: Hearmon 1961, Brugger & Fritz 1967)
C333_sapphire = -800e9  # Pa, third-order elastic constant

# The nonlinear coupling Hamiltonian arises from anharmonicity:
# H_NL = (1/6) * C_{ijk} * s_i * s_j * s_k  integrated over volume
# For our mode coupling: H_int = lambda * x_A^2 * x_B
#
# The overlap integral determines the coupling constant:
# lambda = C_333 / (6 * V) * integral[ s_A(x)^2 * s_B(x) d^3x ]
#
# For the breathing (J_0) and dipole (J_1*cos(phi)) modes, the azimuthal
# integral of J_0^2 * J_1 * cos(phi) over phi gives:
#
# integral_0^{2pi} cos(phi) dphi = 0  if J_0^2 is azimuthally uniform
#
# THIS IS EXACTLY THE Z_2 SELECTION RULE IN ACTION!
# The overlap integral for the cubic coupling x_A^2 * x_B VANISHES
# by the azimuthal symmetry mismatch between J_0 (even, m=0) and
# J_1*cos(phi) (odd, m=1).

# To create a non-zero quadratic coupling x_A^2 * x_B, we need the
# B mode to also be m=0 (azimuthally symmetric). Use a second
# breathing-type mode (B': J_0, odd longitudinal) as the bath.
# Then x_A^2 * x_{B'} has non-zero overlap.

# DESIGN CHOICE: Two-channel experiment
# Channel 1 (Z_2-forbidden): A (breathing) -> B (dipole)
# Channel 2 (Z_2-allowed):   A (breathing) -> B' (breathing, different l)
# Measure both rates. Z_2 predicts ratio = 0.

# Mode B': another breathing mode at half-frequency for parametric process
l_bath = 16  # l=16 breathing mode (m=0, J_0)
omega_Bp = omega_mode(l_bath, 0, j01)
nu_Bp = omega_Bp / (2 * PI)
print(f"Bath mode B' (allowed channel): l={l_bath}, m=0 (J_0)")
print(f"  omega_B' / 2pi = {nu_Bp/1e9:.4f} GHz")
print(f"  Energy conservation: 2*omega_A vs omega_A + omega_B'")
print(f"    2*nu_A = {2*nu_A/1e9:.4f} GHz")
print(f"    nu_A + nu_B' = {(nu_A + nu_Bp)/1e9:.4f} GHz")

# Anharmonic coupling constant lambda (dimensional analysis)
# lambda ~ C_333 * V_overlap / V_mode^2 * x_zpf^2
# The strain overlap integral for same-symmetry modes:
# I_overlap = integral[ sin(l_A * pi*z/h)^2 * sin(l_B' * pi*z/h) * J_0^3(k_r*r) ] d^3x
#
# Longitudinal part: I_z = integral_0^h sin^2(l_A*pi*z/h) * sin(l_B'*pi*z/h) dz
# This is nonzero when 2*l_A +/- l_B' is even (selection rule on longitudinal harmonics)
# For l_A=32, l_B'=16: 2*32 - 16 = 48 (even) => NONZERO

# Evaluate the longitudinal overlap
z = np.linspace(0, h_sub, 10000)
dz = z[1] - z[0]
I_z_allowed = np.sum(
    np.sin(l_breath * PI * z / h_sub)**2 *
    np.sin(l_bath * PI * z / h_sub)
) * dz

I_z_forbidden = np.sum(
    np.sin(l_breath * PI * z / h_sub)**2 *
    np.sin(l_dipole * PI * z / h_sub)
) * dz

# Radial overlap (azimuthal integral kills the dipole term)
# For allowed channel (J_0^3): integral_0^{d/2} J_0(j01*2r/d)^3 * r dr * 2*pi
from scipy.special import j0 as J0_func, j1 as J1_func

r_pts = np.linspace(0, d_disk/2, 5000)
dr = r_pts[1] - r_pts[0]

I_r_allowed = 2 * PI * np.sum(
    J0_func(j01 * 2 * r_pts / d_disk)**3 * r_pts
) * dr

# For forbidden channel (J_0^2 * J_1 * cos(phi)):
# Azimuthal integral: integral_0^{2pi} cos(phi) dphi = 0  EXACTLY
# Even without computing the radial part, the coupling vanishes.
I_azimuthal_forbidden = 0.0  # EXACT by symmetry  # (local)

I_r_forbidden = I_azimuthal_forbidden  # zero regardless of radial part

print(f"\nOverlap integrals:")
print(f"  I_z (allowed, B'):   {I_z_allowed:.6e} m")
print(f"  I_z (forbidden, B):  {I_z_forbidden:.6e} m")
print(f"  I_r (allowed, J_0^3): {I_r_allowed:.6e} m^2")
print(f"  I_r (forbidden, J_0^2*J_1*cos): {I_r_forbidden:.6e} m^2  [ZERO by Z_2]")

# Total overlap
I_total_allowed = I_z_allowed * I_r_allowed / V_mode
I_total_forbidden = I_z_forbidden * I_r_forbidden / V_mode

# Coupling constant for allowed channel
# lambda = |C_333| / 6 * I_total / (m_eff^{3/2} * (omega_A * omega_A * omega_Bp)^{1/2})
# In second-quantized form: g_3 = lambda * x_zpf_A^2 * x_zpf_Bp
g_allowed = abs(C333_sapphire) / 6 * abs(I_total_allowed) * x_zpf_A**2 * x_zpf_B
g_forbidden = 0.0  # EXACTLY ZERO by Z_2  # (local)

print(f"\nCoupling constants:")
print(f"  g_allowed  = {g_allowed:.3e} J = {g_allowed/hbar_SI:.3e} rad/s")
print(f"             = {g_allowed/(hbar_SI * 2 * PI):.3e} Hz")
print(f"  g_forbidden = {g_forbidden:.3e} Hz  [EXACTLY ZERO by Z_2 parity]")

g_allowed_Hz = g_allowed / (hbar_SI * 2 * PI)

# ==========================================================================
# SECTION 5: Decay Rates -- Fermi's Golden Rule
# ==========================================================================
print("\n--- SECTION 5: Decay Rates ---")

# Single-phonon decay (FORBIDDEN channel):
# Gamma_single = (2*pi/hbar) * |<0_A, 1_B | H_int | 1_A, 0_B>|^2 * rho(omega_B)
# The matrix element <0_A, 1_B | x_A^2 * x_B | 1_A, 0_B> = 0
# because x_A^2 acting on |1_A> gives components in |3_A>, |1_A>, not |0_A>.
# Wait -- let me be more careful:
# x_A^2 |1_A> = x_zpf^2 (a + a^dag)^2 |1> = x_zpf^2 (a^2 + a^dag^2 + 2 a^dag a + 1) |1>
#             = x_zpf^2 (sqrt(2)*0 |n=... > + ...)
# Actually: (a + a^dag)^2 |1> = (a^2 + (a^dag)^2 + 2N + 1)|1>
#                                = 0 + sqrt(2*3)|3> + 2*1|1> + |1>
#                                = sqrt(6)|3> + 3|1>
# So <0| x_A^2 |1> = x_zpf^2 * <0| (sqrt(6)|3> + 3|1>) = 0  !!
# The matrix element <0_A | x_A^2 | 1_A> = 0 EXACTLY.
# This is the Z_2 selection rule: x_A^2 changes n_A by 0 or +-2, not by +-1.
# The overlap <0| (a+a^dag)^2 |1> = 0 because (a+a^dag)^2 preserves n mod 2.

# Let me verify explicitly:
# (a + a^dag)^2 = a^2 + (a^dag)^2 + a*a^dag + a^dag*a = a^2 + (a^dag)^2 + 2N + 1
# Acting on |1>: a^2|1> = a*sqrt(1)|0> = 0*... wait:
# a|1> = sqrt(1)|0> = |0>, so a^2|1> = a|0> = 0
# (a^dag)^2|1> = a^dag * sqrt(2)|2> = sqrt(2)*sqrt(3)|3> = sqrt(6)|3>
# (2N+1)|1> = (2*1+1)|1> = 3|1>
# So (a+a^dag)^2 |1> = 0 + sqrt(6)|3> + 3|1>
# <0|(a+a^dag)^2|1> = 0*sqrt(6) + 0*3 = 0. CONFIRMED.

# More generally: <m| (a+a^dag)^2 |n> = 0 unless m-n is even.
# This is the EXACT analog of the Z_2 parity: (-1)^{n_A} is conserved.

print("VERIFICATION: Matrix element <0_A | x_A^2 | 1_A> = 0")
print("  (a+a^dag)^2 |1> = sqrt(6)|3> + 3|1>")
print("  <0| [sqrt(6)|3> + 3|1>] = 0  [QED]")
print()
print("Z_2 SELECTION RULE: (-1)^{n_A} is conserved by H_int = g * x_A^2 * x_B")
print("  Single decay 1_A -> 0_A : changes (-1)^{n_A} from -1 to +1  => FORBIDDEN")
print("  Pair decay   2_A -> 0_A : changes (-1)^{n_A} from +1 to +1  => ALLOWED")

# Pair decay rate (ALLOWED channel):
# 2_A -> 0_A + 1_{B'}
# Matrix element: <0_A, 1_{B'} | x_A^2 * x_{B'} | 2_A, 0_{B'}>
# = x_zpf_A^2 * x_zpf_Bp * <0| (a+a^dag)^2 |2> * <1| (b+b^dag) |0>
# <0|(a+a^dag)^2|2> = <0| [a^2 + (a^dag)^2 + 2N+1] |2>
#                    = <0| [sqrt(2)|0> + sqrt(2*3)|4> + 5|2>]
#                    = sqrt(2)
# <1|(b+b^dag)|0> = <1|b^dag|0> = 1

ME_pair = np.sqrt(2)  # <0|(a+a^dag)^2|2> = sqrt(2)
ME_bath = 1.0         # <1|(b+b^dag)|0> = 1  # (local)

print(f"\nPair decay matrix elements:")
print(f"  <0_A|(a+a^dag)^2|2_A> = sqrt(2) = {ME_pair:.4f}")
print(f"  <1_B|(b+b^dag)|0_B>   = 1")

# Energy conservation for pair decay: 2*omega_A = omega_A + omega_{B'}
# This requires omega_A = omega_Bp, or more generally the energy difference
# goes into the bath phonon.
# Process: |2_A, 0_B'> -> |0_A, 1_B'> with energy 2*hbar*omega_A -> hbar*omega_Bp
# Energy released = hbar*(2*omega_A - omega_Bp) (into B' phonon recoil or other modes)

E_release = hbar_SI * (2 * omega_A - omega_Bp)
print(f"\nEnergy budget:")
print(f"  2 * hbar * omega_A = {2*hbar_SI*omega_A:.4e} J = {2*hbar_SI*omega_A/(hbar_SI*2*PI)/1e9:.4f} GHz")
print(f"  hbar * omega_B'   = {hbar_SI*omega_Bp:.4e} J = {hbar_SI*omega_Bp/(hbar_SI*2*PI)/1e9:.4f} GHz")
print(f"  Energy released    = {E_release:.4e} J = {E_release/(hbar_SI*2*PI)/1e9:.4f} GHz")

# Fermi's golden rule for pair decay:
# Gamma_pair = (2*pi/hbar) * |g_eff|^2 * rho(E_final)
# g_eff = g_allowed * ME_pair * ME_bath (with the ZPF already folded into g_allowed)
# rho(E_final) = density of final states at the released energy
# For a discrete mode: rho = 1/(hbar * kappa_B') where kappa_B' is the linewidth of mode B'

# Q factor scan
Q_values = np.array([1e3, 1e4, 1e5, 1e6, 1e7, 1e8, 1e9, 1e10])
kappa_B_values = omega_Bp / Q_values  # linewidths in rad/s

# For allowed channel: pair decay 2_A -> 0_A + 1_{B'}
# Using FGR with discrete final state (Lorentzian broadening)
g_eff_pair = g_allowed_Hz * 2 * PI * ME_pair * ME_bath  # rad/s

# Gamma_pair = g_eff^2 / kappa_B (on-resonance, discrete mode)
# More precisely, for detuned case:
# Gamma_pair = g_eff^2 * kappa_B / ((2*omega_A - omega_Bp)^2 + (kappa_B/2)^2)
detuning_pair = 2 * omega_A - omega_Bp  # rad/s

print(f"\nEffective coupling: g_eff(pair) = {g_eff_pair/(2*PI):.3e} Hz")
print(f"Detuning: delta = {detuning_pair/(2*PI)/1e6:.3f} MHz")

# For forbidden channel: single decay 1_A -> 0_A + 1_B
# Gamma_single = 0 EXACTLY by Z_2
# But estimate symmetry-breaking leakage from:
# (a) Manufacturing imperfections (mode mixing)
# (b) Higher-order terms (x_A^3 * x_B, which IS allowed but suppressed)
# (c) Finite-Q bath coupling (off-diagonal in parity basis)

# Symmetry-breaking leakage estimate
# If the breathing mode has an admixture alpha of the dipole mode due to
# fabrication imperfection (surface roughness, misalignment):
# |A_phys> = |A_ideal> + alpha * |B_ideal>
# Then Gamma_single_leak = alpha^2 * Gamma_single_if_allowed

# For a well-fabricated HBAR: alpha ~ x_roughness / wavelength
# Surface roughness ~ 1 nm, wavelength ~ 2*h/l ~ 26 um
x_roughness = 1e-9  # m, typical surface roughness
lambda_A = 2 * h_sub / l_breath  # acoustic wavelength of mode A
alpha_mix = x_roughness / lambda_A

print(f"\n--- Symmetry Breaking Estimates ---")
print(f"Surface roughness: {x_roughness*1e9:.1f} nm")
print(f"Acoustic wavelength: {lambda_A*1e6:.1f} um")
print(f"Mode mixing parameter: alpha = {alpha_mix:.3e}")
print(f"Parity violation: alpha^2 = {alpha_mix**2:.3e}")

# If single decay WERE allowed (without Z_2), the rate would be:
# Gamma_single_naive = g_3^2 * x_zpf^2 / kappa * |<0|(a+a^dag)|1>|^2
# <0|(a+a^dag)|1> = 1
# This is the "control experiment" rate
g_eff_single_naive = g_allowed_Hz * 2 * PI  # single-phonon coupling if Z_2 broken
ME_single = 1.0  # <0|(a+a^dag)|1> = 1  # (local)

# ==========================================================================
# SECTION 6: Rate Predictions vs Q-Factor
# ==========================================================================
print("\n--- SECTION 6: Rate Predictions vs Q-Factor ---")

print(f"\n{'Q':>10s} | {'kappa/2pi':>12s} | {'Gamma_pair':>14s} | {'Gamma_single':>14s} | {'Gamma_leak':>14s} | {'Ratio pair/leak':>16s}")
print("-" * 100)

results_Q = []
results_Gamma_pair = []
results_Gamma_single = []
results_Gamma_leak = []

for Q in Q_values:
    kappa = omega_Bp / Q  # rad/s

    # Pair decay rate (Lorentzian profile at detuning)
    Gamma_pair = g_eff_pair**2 * kappa / (detuning_pair**2 + (kappa/2)**2)

    # Single decay: EXACTLY ZERO by Z_2
    Gamma_single = 0.0  # (local)

    # Leakage from mode mixing (manufacturing imperfection)
    # The leaked rate = alpha^2 * (what Gamma_single would be without Z_2)
    Gamma_single_if_allowed = g_eff_single_naive**2 * kappa / (
        (omega_A - omega_B)**2 + (kappa/2)**2
    )
    Gamma_leak = alpha_mix**2 * Gamma_single_if_allowed

    ratio = Gamma_pair / Gamma_leak if Gamma_leak > 0 else np.inf

    results_Q.append(Q)
    results_Gamma_pair.append(Gamma_pair / (2*PI))
    results_Gamma_single.append(0.0)
    results_Gamma_leak.append(Gamma_leak / (2*PI))

    print(f"{Q:10.0e} | {kappa/(2*PI):12.3e} Hz | {Gamma_pair/(2*PI):14.3e} Hz | {'ZERO (exact)':>14s} | {Gamma_leak/(2*PI):14.3e} Hz | {ratio:16.3e}")

results_Q = np.array(results_Q)
results_Gamma_pair = np.array(results_Gamma_pair)
results_Gamma_single = np.array(results_Gamma_single)
results_Gamma_leak = np.array(results_Gamma_leak)

# ==========================================================================
# SECTION 7: Framework Analog Mapping
# ==========================================================================
print("\n--- SECTION 7: Framework Analog Mapping ---")

# Map the BAW Z_2 to the substrate Z_2
print("ANALOG DICTIONARY:")
print()
print("  Substrate (S67)                    BAW Analog")
print("  ---------------------------------  ---------------------------------")
print("  Leggett mode phi_{23}              Breathing mode x_A (even parity)")
print("  Graviton channel (a_2 moment)      Waveguide mode x_B (output)")
print("  cos(phi_{23}) symmetry             J_0 azimuthal symmetry")
print("  Z_2: a_2(phi) = a_2(-phi)          Z_2: H_int = g * x_A^2 * x_B")
print("  (-1)^{n_L} conserved               (-1)^{n_A} conserved")
print("  Single L -> gg: FORBIDDEN          Single A -> B: FORBIDDEN")
print("  Pair 2L -> 2g: ALLOWED             Pair 2A -> B: ALLOWED")
print(f"  Gamma_pair/H_0 = 9.3e-66           Gamma_pair = {results_Gamma_pair[4]:.3e} Hz (Q=1e7)")
print(f"  epsilon = 0.00374                  alpha_mix = {alpha_mix:.3e}")

# The key experimental signature
print("\n--- EXPERIMENTAL SIGNATURE ---")
print()
print("The Z_2 selection rule predicts:")
print(f"  Gamma_single = 0  (exact, by (-1)^n_A conservation)")
print(f"  Gamma_pair > 0    (allowed by (-1)^n_A conservation)")
print()
print("Observable: prepare |2_A, 0_B> state (two breathing phonons).")
print("Measure decay to |0_A, 1_{B'}> (pair annihilation, Z_2-allowed).")
print("Then prepare |1_A, 0_B> state (one breathing phonon).")
print("Measure decay to |0_A, 1_B> (single annihilation, Z_2-forbidden).")
print("The ratio Gamma_single / Gamma_pair should be zero up to")
print(f"manufacturing imperfections (alpha^2 ~ {alpha_mix**2:.1e}).")

# ==========================================================================
# SECTION 8: Feasibility Assessment
# ==========================================================================
print("\n--- SECTION 8: Feasibility Assessment ---")

# Chu 2017 achieved:
# g/2pi = 260 kHz (piezoelectric coupling to qubit)
# T1_phonon = 17 us (Q ~ omega * T1)
# T2_phonon = 27 us
# T_bath ~ 20 mK (dilution fridge)
g_Chu = 2 * PI * 260e3  # rad/s, Chu's measured coupling
T1_Chu = 17e-6           # s
T2_Chu = 27e-6           # s
omega_Chu = 2 * PI * 5.4e9  # ~5.4 GHz operating frequency
Q_Chu = omega_Chu * T1_Chu
T_bath = 20e-3            # K
n_thermal = 1 / (np.exp(hbar_SI * omega_Chu / (k_B_SI * T_bath)) - 1)

print(f"Chu et al. 2017 benchmark:")
print(f"  g/2pi = 260 kHz")
print(f"  T1 = {T1_Chu*1e6:.0f} us, T2 = {T2_Chu*1e6:.0f} us")
print(f"  Q = omega * T1 = {Q_Chu:.2e}")
print(f"  n_thermal(5.4 GHz, 20 mK) = {n_thermal:.3e}")
print()

# Required Q for signal
# Need: Gamma_pair * T_measurement > 1 (at least one pair decay event)
# and: Gamma_leak * T_measurement < 1 (no spurious single decays)
T_measurement = 1.0  # s, reasonable measurement time  # (local)

print("Required conditions:")
print(f"  1. Gamma_pair * T_meas > 1  (pair decay observable)")
print(f"  2. Gamma_leak * T_meas < 1  (single decay background suppressed)")
print(f"  3. n_thermal << 1           (ground state preparation)")
print(f"  4. g_qubit >> kappa          (strong coupling for state preparation)")
print()

# For each Q, check feasibility
print(f"{'Q':>10s} | {'Gamma_pair (Hz)':>15s} | {'Events/s':>10s} | {'Leak/s':>10s} | {'Feasible?':>10s}")
print("-" * 70)
for i, Q in enumerate(results_Q):
    events_pair = results_Gamma_pair[i]
    events_leak = results_Gamma_leak[i]

    # Feasibility: need events_pair > 1/T_meas and events_leak < 1/T_meas
    feasible_signal = events_pair > 1.0 / T_measurement
    feasible_background = events_leak < 1.0 / T_measurement
    feasible_Q = Q <= 1e7  # achievable with current technology

    status = ""
    if feasible_signal and feasible_background and feasible_Q:
        status = "YES"
    elif not feasible_Q:
        status = "Q too high"
    elif not feasible_signal:
        status = "Too weak"
    else:
        status = "Bkg limit"

    print(f"{Q:10.0e} | {events_pair:15.3e} | {events_pair:10.3e} | {events_leak:10.3e} | {status:>10s}")

# ==========================================================================
# SECTION 9: Improved Design -- Parametric Pump
# ==========================================================================
print("\n--- SECTION 9: Enhanced Design with Parametric Pump ---")

# The direct anharmonic coupling is weak because C_333 * x_zpf^3 is tiny.
# A much stronger approach: use the qubit as a NONLINEAR ELEMENT to
# mediate the coupling. The transmon provides a Kerr nonlinearity
# chi ~ g^4 / (alpha * delta^2) where alpha ~ 200 MHz is the anharmonicity.

# Qubit-mediated nonlinear coupling:
# H_eff = chi_AB * n_A^2 * n_B (cross-Kerr between A and B modes)
# This naturally has the Z_2 structure because n_A = a^dag a appears
# quadratically (n_A^2), preserving (-1)^{n_A}.

# Qubit parameters (state of the art, 2024)
alpha_qubit = 2 * PI * 200e6     # Hz, transmon anharmonicity
g_qA = 2 * PI * 260e3           # Hz, qubit-A coupling (Chu value)
g_qB = 2 * PI * 200e3           # Hz, qubit-B coupling (slightly lower for different mode)
delta_qA = 2 * PI * 100e6       # Hz, qubit-A detuning
delta_qB = 2 * PI * 150e6       # Hz, qubit-B detuning

# Cross-Kerr shift (fourth-order dispersive)
# chi_AB ~ g_qA^2 * g_qB^2 / (alpha * delta_qA * delta_qB)
chi_AB = g_qA**2 * g_qB**2 / (alpha_qubit * delta_qA * delta_qB)

print(f"Qubit-mediated cross-Kerr:")
print(f"  g_qA/2pi = {g_qA/(2*PI)/1e3:.0f} kHz")
print(f"  g_qB/2pi = {g_qB/(2*PI)/1e3:.0f} kHz")
print(f"  alpha/2pi = {alpha_qubit/(2*PI)/1e6:.0f} MHz")
print(f"  delta_qA/2pi = {delta_qA/(2*PI)/1e6:.0f} MHz")
print(f"  delta_qB/2pi = {delta_qB/(2*PI)/1e6:.0f} MHz")
print(f"  chi_AB/2pi = {chi_AB/(2*PI):.3e} Hz = {chi_AB/(2*PI)*1e3:.3f} mHz")

# With the qubit-mediated coupling, the effective interaction is:
# H_eff = hbar * chi_AB * a^dag a * (a^dag a - 1) * b^dag b
# This is QUARTIC in mode A operators and preserves Z_2 by construction.
# For the pair process |2,0> -> |0,1>:
# Rate ~ chi_AB^2 / kappa_B (on resonance)

# But we can do better: use a PARAMETRIC PUMP
# Drive at frequency omega_pump = 2*omega_A - omega_B
# This activates the process a*a -> b via the Kerr nonlinearity
# Effective coupling: g_param ~ chi_AB * sqrt(n_pump)

# Pump photon number (typical)
P_pump = 1e-15  # W, pump power (femtowatt level to avoid heating)
kappa_pump = 2 * PI * 1e3  # Hz, pump linewidth
omega_pump = 2 * omega_A - omega_Bp  # pump frequency
n_pump = P_pump / (hbar_SI * omega_pump * kappa_pump)

g_param = chi_AB * np.sqrt(max(n_pump, 1))

print(f"\nParametric pump enhancement:")
print(f"  omega_pump/2pi = {omega_pump/(2*PI)/1e9:.4f} GHz")
print(f"  P_pump = {P_pump*1e15:.0f} fW")
print(f"  n_pump = {n_pump:.2e}")
print(f"  g_param/2pi = {g_param/(2*PI):.3e} Hz")

# Parametric pair decay rate
# Gamma_param = 4 * g_param^2 / kappa (for on-resonance parametric process)
Q_target = 1e6  # achievable Q
kappa_target = omega_Bp / Q_target

Gamma_param = 4 * g_param**2 / kappa_target
print(f"\nParametric pair decay (Q = {Q_target:.0e}):")
print(f"  kappa/2pi = {kappa_target/(2*PI):.3e} Hz")
print(f"  Gamma_param/2pi = {Gamma_param/(2*PI):.3e} Hz")
print(f"  Events per second: {Gamma_param/(2*PI):.3e}")
print(f"  Events per hour: {Gamma_param/(2*PI)*3600:.3e}")

# Now the forbidden channel with parametric drive
# The pump at 2*omega_A - omega_B drives a*a -> b (pair, ALLOWED)
# A pump at omega_A - omega_B would drive a -> b (single, FORBIDDEN)
# With manufacturing imperfection alpha_mix, the single channel leaks:
Gamma_param_leak = alpha_mix**2 * 4 * g_param**2 / kappa_target

print(f"\nForbidden channel leakage:")
print(f"  Gamma_leak/2pi = {Gamma_param_leak/(2*PI):.3e} Hz")
print(f"  Pair/Leak ratio = {Gamma_param/Gamma_param_leak:.3e}")
print(f"  Suppression = {-np.log10(Gamma_param_leak/Gamma_param):.1f} orders of magnitude")

# ==========================================================================
# SECTION 10: Experimental Protocol
# ==========================================================================
print("\n--- SECTION 10: Experimental Protocol ---")

print("""
PROTOCOL: Z_2 SELECTION RULE TEST IN BAW RESONATOR
===================================================

Step 1: DEVICE FABRICATION
  - Sapphire substrate (420 um thickness, double-side polished)
  - AlN piezoelectric transducer (900 nm, c-axis oriented)
  - Frequency-tunable transmon qubit (Al/AlOx/Al on sapphire)
  - Design: two addressable phonon modes A (breathing, J_0) and B (dipole, J_1)
  - Achieve Q > 10^5 for both modes (Chu 2017 achieved Q ~ 5.8e5)

Step 2: MODE CHARACTERIZATION
  - Spectroscopy: identify breathing mode A and dipole mode B
  - Verify mode symmetries via coupling patterns to qubit
  - Measure individual Q-factors, T1, T2 for both modes
  - Characterize cross-Kerr chi_AB by two-tone spectroscopy

Step 3: ALLOWED CHANNEL (pair decay)
  - Prepare |2_A, 0_B> by two successive qubit->A swap operations
  - Apply parametric pump at omega_pump = 2*omega_A - omega_B'
  - Monitor B' mode population via qubit-B' swap + qubit readout
  - Measure Gamma_pair from population growth rate
  - Expected: Gamma_pair > 0 (Z_2-allowed process)

Step 4: FORBIDDEN CHANNEL (single decay)
  - Prepare |1_A, 0_B> by single qubit->A swap
  - Apply pump at omega_pump = omega_A - omega_B (single-phonon pump)
  - Monitor B mode population
  - Expected: Gamma_single = 0 (Z_2-forbidden process)
  - Measure upper bound on Gamma_single from noise floor

Step 5: CONTROL EXPERIMENT
  - Replace mode A with a dipole mode A' (ODD parity, J_1)
  - For A' mode, BOTH single and pair processes are allowed
  - Verify Gamma_single(A') > 0 as control
  - The ratio Gamma_single(A) / Gamma_single(A') tests Z_2

Step 6: DATA ANALYSIS
  - Primary observable: R = Gamma_single / Gamma_pair
  - Z_2 prediction: R = 0
  - Symmetry-breaking bound: R < alpha_mix^2
  - Systematic check: vary pump power, temperature, mode pairs
""")

# ==========================================================================
# SECTION 11: Connection to Framework Constants
# ==========================================================================
print("--- SECTION 11: Framework Constant Mapping ---")

# The ratio of pair-to-single decay in the framework
# Gamma_pair / H_0 = 9.3e-66 (S67)
# Gamma_single / H_0 = 0 (exact)
# The PAIR rate suppression is also enormous: 66 orders of magnitude below H_0

# In the BAW analog, the pair rate is measurable because:
# 1. We can PUMP the transition (parametric enhancement)
# 2. The coupling is electromagnetic, not gravitational (no M_Pl suppression)
# 3. We control the state preparation (Fock states via qubit swap)

# The RATIO Gamma_single/Gamma_pair is the universal quantity:
# Framework: 0 (exact)
# BAW analog: 0 (exact, up to alpha_mix^2)
# This ratio is independent of coupling strength and tests ONLY the Z_2 symmetry.

# Mapping the framework's epsilon to the BAW mixing parameter
epsilon_framework = 0.00374  # S59 canonical value  # (local)
print(f"Framework epsilon (S59): {epsilon_framework:.5f}")
print(f"BAW mode mixing alpha:   {alpha_mix:.5e}")
print(f"Ratio epsilon/alpha:     {epsilon_framework/alpha_mix:.2e}")
print()
print("The Z_2 test is STRUCTURAL -- it does not require matching epsilon.")
print("What matters is the RATIO Gamma_single/Gamma_pair = 0, which tests")
print("the parity symmetry independent of coupling magnitudes.")

# Framework Leggett parameters for reference
print(f"\nFramework Leggett parameters (for reference):")
print(f"  omega_L1 (GL) = {omega_L1:.3f} M_KK = {omega_L1 * M_KK:.3e} GeV")
print(f"  omega_L2 (GL) = {omega_L2:.3f} M_KK = {omega_L2 * M_KK:.3e} GeV")
print(f"  omega_L1 (V_bare, S59) = 0.049 M_KK = {0.049 * M_KK:.3e} GeV")

# Energy scale comparison
omega_L_GeV = 0.049 * M_KK  # Leggett frequency in GeV (S59)
omega_BAW_GeV = hbar_SI * omega_A / (1.602e-19 * 1e9)  # BAW frequency in GeV
print(f"  omega_BAW = {omega_A/(2*PI)/1e9:.2f} GHz = {omega_BAW_GeV:.3e} GeV")
print(f"  Scale ratio: omega_L / omega_BAW = {omega_L_GeV / omega_BAW_GeV:.3e}")
print(f"  The BAW is {np.log10(omega_L_GeV / omega_BAW_GeV):.1f} orders below the substrate Leggett scale")
print(f"  BUT the Z_2 symmetry is SCALE-INDEPENDENT (structural, not dynamical)")

# ==========================================================================
# SECTION 12: Summary
# ==========================================================================
print("\n" + "=" * 72)
print("SUMMARY: Z2-BAW-ANALOG-69")
print("=" * 72)

print(f"""
Gate: Z2-BAW-69 -- INFO (design study, no pass/fail threshold)

RESULT: A BAW resonator experiment can test the Z_2 selection rule
        that forbids single-Leggett gravitational decay (S67 T1).

DEVICE: Sapphire HBAR (Chu et al. 2017 platform)
  Breathing mode A: l={l_breath}, m=0, nu_A = {nu_A/1e9:.3f} GHz
  Dipole mode B:    l={l_dipole}, m=1, nu_B = {nu_B/1e9:.3f} GHz
  Bath mode B':     l={l_bath}, m=0, nu_B' = {nu_Bp/1e9:.3f} GHz

Z_2 PARITY:
  (-1)^{{n_A}} is conserved by H_int = g * x_A^2 * x_B
  Single decay 1_A -> 0_A + 1_B: FORBIDDEN (exact)
  Pair decay   2_A -> 0_A + 1_B': ALLOWED

RATES (direct anharmonic, Q=1e5):
  Gamma_pair  = {results_Gamma_pair[4]:.3e} Hz
  Gamma_single = 0 Hz (exact)
  Gamma_leak   = {results_Gamma_leak[4]:.3e} Hz (manufacturing imperfection)

RATES (qubit-mediated parametric, Q=1e6):
  Gamma_param_pair  = {Gamma_param/(2*PI):.3e} Hz
  Gamma_param_leak  = {Gamma_param_leak/(2*PI):.3e} Hz
  Suppression ratio = {Gamma_param/Gamma_param_leak:.1e}

FEASIBILITY:
  - Q ~ 10^5-10^6 achievable (Chu 2017: Q = 5.8e5)
  - State preparation: Fock states via qubit-phonon swap (demonstrated)
  - Readout: qubit-phonon swap + dispersive qubit readout (demonstrated)
  - Parametric pump: standard technique in circuit QED
  - Z_2 violation bound: alpha_mix^2 ~ {alpha_mix**2:.1e} (from surface roughness)

UNIVERSAL TEST:
  The ratio R = Gamma_single / Gamma_pair = 0 is the prediction.
  This tests the SYMMETRY, not the coupling strength.
  Independent of all framework parameters except the Z_2 itself.
""")

# ==========================================================================
# Save results
# ==========================================================================
save_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         "s69_z2_baw.npz")

np.savez(save_path,
    # Device parameters
    h_sub=h_sub, d_disk=d_disk,
    v_l_sapphire=v_l_sapphire, v_t_sapphire=v_t_sapphire,
    rho_sapphire=rho_sapphire,
    nu_FSR=nu_FSR,
    # Mode parameters
    l_breath=l_breath, l_dipole=l_dipole, l_bath=l_bath,
    omega_A=omega_A, omega_B=omega_B, omega_Bp=omega_Bp,
    nu_A=nu_A, nu_B=nu_B, nu_Bp=nu_Bp,
    x_zpf_A=x_zpf_A, x_zpf_B=x_zpf_B,
    m_eff_A=m_eff_A,
    # Coupling
    g_allowed_Hz=g_allowed_Hz,
    g_eff_pair_Hz=g_eff_pair/(2*PI),
    chi_AB_Hz=chi_AB/(2*PI),
    g_param_Hz=g_param/(2*PI),
    # Rates
    Q_values=results_Q,
    Gamma_pair_Hz=results_Gamma_pair,
    Gamma_single_Hz=results_Gamma_single,
    Gamma_leak_Hz=results_Gamma_leak,
    Gamma_param_pair_Hz=Gamma_param/(2*PI),
    Gamma_param_leak_Hz=Gamma_param_leak/(2*PI),
    # Z2 parameters
    alpha_mix=alpha_mix,
    epsilon_framework=epsilon_framework,
    # Matrix elements
    ME_pair=ME_pair,
    ME_single_forbidden=0.0,
    # Framework reference
    omega_L1_MKK=0.049,
    omega_L2_MKK=0.087,
    Gamma_pair_framework_over_H0=9.3e-66,
)

print(f"\nData saved to: {save_path}")
print("DONE.")
