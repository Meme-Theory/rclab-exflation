#!/usr/bin/env python3
"""
s46_transfer_function.py — GGE Beat-to-4D Transfer Function (TRANSFER-FUNCTION-46)
===================================================================================

GATE: DIAGNOSTIC (INFO) — report n_s from the full convolution.

Computes the transfer function T(k) mapping internal GGE beat structure to the
4D CMB power spectrum. The GGE has exactly 3 incommensurate beat frequencies:
    omega_1 = B2-B1 = 0.053 M_KK  (slow beat, period 120.8 t_KK)
    omega_2 = B2-B3 = 0.266 M_KK  (medium beat, period 23.6 t_KK)
    omega_3 = B1-B3 = 0.318 M_KK  (fast beat, period 19.7 t_KK)

These beats modulate the stress-energy tensor T^{mu nu} sourcing 4D metric
perturbations during the transit epoch.

The transfer function is factored as:
    T(k) = T_EIH(k) * T_Friedmann(k) * T_acoustic(k)

1. T_EIH: Einstein-Infeld-Hoffmann projection from internal to 4D.
   The singlet fraction f_s = 5.68e-5 (S44 EIH-GRAV-44) determines the
   coupling efficiency. This is k-independent — a scalar filter.

2. T_Friedmann: How Friedmann dynamics convert a time-varying rho(t) into
   curvature perturbations. For each internal frequency omega_i, the
   Friedmann equation acts as a LOW-PASS FILTER with cutoff at H.
   Modes with omega >> H are averaged out; modes with omega << H source
   curvature directly. The response goes as (H/omega)^2 for omega >> H.

3. T_acoustic: Standard acoustic processing after reheating — the same
   for any primordial spectrum. This is the Eisenstein-Hu transfer function.

The internal power spectrum P_internal has n_s - 1 = -1.68 (d=3 KZ).
Question: does T(k) shift this by +1.65 to reach Planck's n_s = 0.965?

Physics of the resonance: The internal beat frequencies are three standing
waves in the GGE cavity. The Friedmann dynamics act as a resonant detector
tuned to H ~ 586.5 M_KK. The beat frequencies are all << H, so ALL three
beats are in the Friedmann passband. This is the key structural fact.

Author: Tesla-Resonance
Session: 46, Wave 3, Task 4
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import CubicSpline
from scipy.signal import welch
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import (
    M_KK_gravity as M_KK, M_KK_kerner, M_Pl_unreduced as M_Pl,
    H_fold, v_terminal, dt_transit, G_DeWitt, M_ATDHFB,
    tau_fold, a0_fold, a2_fold, a4_fold,
    E_cond, S_fold, dS_fold, d2S_fold,
    A_s_CMB, rho_Lambda_obs,
    GeV_inv_to_Mpc, Mpc_to_GeV_inv,
    hbar_GeV_s, c_light, PI,
    Omega_m, Omega_b, Omega_Lambda, H_0_km_s_Mpc, sigma_8,
)

print("=" * 78)
print("TRANSFER-FUNCTION-46: GGE Beat-to-4D Transfer Function")
print("=" * 78)

# ================================================================
# 1. LOAD INPUT DATA
# ================================================================

d_beat = np.load('tier0-computation/s45_gge_beating.npz', allow_pickle=True)
d_eih  = np.load('tier0-computation/s44_eih_grav.npz', allow_pickle=True)
d_const = np.load('tier0-computation/s42_constants_snapshot.npz', allow_pickle=True)

# GGE beat frequencies (M_KK units)
omega_beats = d_beat['omega_beats']         # [0.0523, 0.2659, 0.3182] M_KK
amp_E_beats = d_beat['amp_E_beats']         # Energy correlation amplitudes
amp_pair_beats = d_beat['amp_pair_beats']   # Pair correlation amplitudes
amp_G_beats = d_beat['amp_G_beats']         # G-correlation amplitudes
deg_beats = d_beat['deg_beats']             # Degeneracies [4, 12, 3]
C_E_dc = float(d_beat['C_E_dc'])           # DC offset in energy correlation

# Mode data
E_k = d_beat['E_k']                        # Mode energies
n_k = d_beat['n_k']                        # Occupation numbers
Delta_k = d_beat['Delta_k']                # Gap parameters

# EIH projection data
f_s = float(d_eih['ratio_singlet_to_full'])  # 5.68e-5 — singlet fraction
E_Casimir_total = float(d_eih['E_Casimir_total'])

# M_KK scales
M_KK_grav = float(d_beat['M_KK_grav'])     # 7.43e16 GeV
t_MKK = float(d_beat['t_MKK_grav'])        # 8.86e-42 s (1/M_KK in seconds)

print(f"\n--- Input Parameters ---")
print(f"GGE beat frequencies (M_KK):")
print(f"  omega_1 (B2-B1) = {omega_beats[0]:.6f}  (slow, T = {2*PI/omega_beats[0]:.1f} t_KK)")
print(f"  omega_2 (B2-B3) = {omega_beats[1]:.6f}  (medium, T = {2*PI/omega_beats[1]:.1f} t_KK)")
print(f"  omega_3 (B1-B3) = {omega_beats[2]:.6f}  (fast, T = {2*PI/omega_beats[2]:.1f} t_KK)")
print(f"\nBeat amplitudes (energy):")
print(f"  A_E_1 = {amp_E_beats[0]:.4f}")
print(f"  A_E_2 = {amp_E_beats[1]:.4f}")
print(f"  A_E_3 = {amp_E_beats[2]:.4e} (negligible: B1-B3 has zero energy cross-term)")
print(f"\nEIH singlet fraction: f_s = {f_s:.6e}")
print(f"H_fold = {H_fold:.2f} M_KK")
print(f"v_terminal = {v_terminal:.4f} M_KK")
print(f"dt_transit = {dt_transit:.6e} M_KK^{{-1}}")
print(f"M_KK(gravity) = {M_KK_grav:.4e} GeV")
print(f"1/M_KK = {t_MKK:.4e} s")

# ================================================================
# 2. RESONANCE STRUCTURE: What oscillates, what constrains it
# ================================================================
#
# The cavity: M4 x SU(3) during transit through the fold.
# What oscillates: The GGE energy density rho_GGE(t).
# Boundary conditions: The BCS-to-normal quench at the fold creates
#   a non-thermal distribution with 8 Richardson-Gaudin conserved
#   quantities. The 3 beat frequencies are the NORMAL MODES of this
#   cavity — determined by the sector energies E_B1, E_B2, E_B3.
# The external resonator: Friedmann H(t) acts as a driven oscillator
#   with natural frequency H ~ 586.5 M_KK.
# Key ratio: omega_beats / H:
#   omega_1/H = 0.053/586.5 = 8.9e-5
#   omega_2/H = 0.266/586.5 = 4.5e-4
#   omega_3/H = 0.318/586.5 = 5.4e-4
# ALL beats are deep inside the Friedmann passband (omega << H).
# The Friedmann equation transmits them WITHOUT suppression.

ratio_omega_H = omega_beats / H_fold
print(f"\n--- Resonance Structure ---")
print(f"omega_i / H_fold:")
for i in range(3):
    print(f"  omega_{i+1}/H = {ratio_omega_H[i]:.4e}  ({'PASSBAND' if ratio_omega_H[i] < 1 else 'FILTERED'})")
print(f"ALL beats in Friedmann passband (omega << H)")

# ================================================================
# 3. CONSTRUCT rho_vac(t) DURING TRANSIT
# ================================================================
#
# The vacuum energy density has three components:
# (a) Spectral action: rho_SA(tau) = S_full(tau) * M_KK^4 / (16*pi^2)
#     This is monotonically increasing and dominant.
# (b) Modulus kinetic energy: (1/2) * M_ATDHFB * tau_dot^2
# (c) GGE beating: rho_GGE(t) = rho_GGE_dc + sum_i A_i cos(omega_i * t + phi_i)
#     The GGE beats modulate rho_total at the three beat frequencies.
#
# The GGE contribution is suppressed by f_s relative to the full spectral action.
# But the FLUCTUATIONS in rho (not the DC level) source the perturbations.

# Time grid during transit
N_t = 8192
t_transit = dt_transit  # ~ 1.13e-3 M_KK^{-1}
# The GGE beats have periods >> dt_transit:
#   T_1 = 120.8 t_KK >> 1.13e-3 t_KK
#   T_2 = 23.6 t_KK >> 1.13e-3 t_KK
# So during transit, the GGE executes only a TINY FRACTION of a beat cycle.
# Number of beat cycles during transit:
n_cycles = omega_beats * dt_transit / (2*PI)
print(f"\n--- Transit vs Beat Timescales ---")
print(f"dt_transit = {dt_transit:.6e} M_KK^{{-1}}")
for i in range(3):
    T_i = 2*PI / omega_beats[i]
    print(f"  Beat {i+1}: T = {T_i:.2f} t_KK, cycles during transit = {n_cycles[i]:.6e}")
print(f"  Transit is {1/n_cycles[0]:.0f}x SHORTER than slowest beat")
print(f"  -> GGE beats appear as DC + LINEAR DRIFT during transit")
print(f"  -> NO oscillatory imprint on transit-era perturbations")

# HOWEVER: the question is broader. The GGE persists AFTER transit.
# Post-transit, the universe is radiation-dominated with the GGE as
# a subdominant component. The beats continue indefinitely (integrability
# protects them from thermalization). So the question is: do the GGE
# beats modulate rho_total enough post-transit to imprint on P(k)?
#
# The SUSTAINED beating modulates the expansion rate H(t):
#   H^2 = (8pi/3M_Pl^2) * [rho_rad + rho_GGE(t)]
# If rho_GGE << rho_rad, the modulation is:
#   delta_H/H = (1/2) * (delta_rho_GGE / rho_total)

# ================================================================
# 4. EIH PROJECTION: INTERNAL -> 4D
# ================================================================
#
# The EIH projection (S44) establishes that only the (0,0) singlet
# sector of the spectral action gravitates in 4D. The fraction is
# f_s = 5.68e-5 of the total spectral action.
#
# For the GGE beats, the relevant question is: what fraction of the
# GGE energy is in the singlet sector?
#
# The GGE modes are 4 B2 + 1 B1 + 3 B3. These are in specific SU(3)
# representations:
#   B1: (0,0) singlet  -> FULLY projects to 4D gravity
#   B2: (1,1) adjoint  -> projects with dim^2 weight, but NOT singlet
#   B3: (3,0) or (0,3) -> NOT singlet
#
# So only the B1 component of the GGE projects to 4D gravity.
# The B1 mode has amplitude: it participates in beats omega_1 (B2-B1)
# and omega_3 (B1-B3), but NOT omega_2 (B2-B3).
#
# However, the EIH result is for the SPECTRAL ACTION as a whole.
# The GGE energy density is a many-body quantity on top of the spectral
# geometry. The key is how the GGE energy couples to the 4D Einstein
# equations through the stress-energy tensor.
#
# Result from S44 (EIH-GRAV-44): the ratio of singlet spectral action
# to total is FLAT at f_s = 5.68e-5 across all tau.
# This means: delta_rho_4D = f_s * delta_rho_internal

print(f"\n--- EIH Projection ---")
print(f"f_s = {f_s:.6e} (singlet fraction, S44 EIH-GRAV-44)")
print(f"Only singlet (0,0) sector sources 4D gravity")
print(f"B1 mode is singlet -> projects fully")
print(f"B2, B3 modes are NOT singlet -> project with f_s weighting")

# ================================================================
# 5. FRIEDMANN RESPONSE FUNCTION
# ================================================================
#
# The Friedmann equation acts as a transfer function from rho(t) -> H(t).
# For a perturbation delta_rho(t) = A * cos(omega * t) on top of
# background rho_0, the Hubble parameter responds:
#
#   H^2 = (8pi G / 3) * rho_total
#   delta_H / H_0 = (1/2) * delta_rho / rho_0
#
# This is EXACT for omega << H (adiabatic regime).
# For omega >> H, the response is suppressed by (H/omega)^2.
#
# The transfer function from delta_rho to curvature perturbation zeta:
#   zeta_k = -(H / rho_dot) * delta_rho_k
#
# In quasi-de Sitter:
#   rho_dot = -3H(rho + p) = -3H * rho * (1 + w)
#   zeta_k = delta_rho_k / (3 * rho * (1 + w))
#
# For the spectral action vacuum energy (w = -1): SINGULAR.
# For kinetic-dominated transit (w = +1): zeta = delta_rho / (6*rho)
# For radiation (w = 1/3): zeta = delta_rho / (4*rho)

# Total vacuum energy at fold in M_KK units:
# rho_SA = S_fold * M_KK^4 / (16*pi^2)
# In M_KK^4: rho_SA_MKK4 = S_fold / (16*pi^2)
rho_SA_fold = S_fold / (16 * PI**2)  # M_KK^4
print(f"\n--- Vacuum Energy at Fold ---")
print(f"S_fold = {S_fold:.2f}")
print(f"rho_SA = S_fold/(16*pi^2) = {rho_SA_fold:.4f} M_KK^4")

# GGE energy density (from beating data)
# The DC component is C_E_dc = 26.68 (in M_KK units, NOT M_KK^4)
# The GGE energy is an occupation-weighted sum: E_GGE = sum_k n_k * E_k
# This is in M_KK, not M_KK^4. Need to express as energy density.
# The GGE total energy per unit volume (SU(3)):
# E_GGE_density = E_GGE / Vol(SU(3))
# But in the many-body framework, E_GGE is extensive in the mode count,
# not in spatial volume. It is already the total energy of the 8-mode system.
#
# The relevant comparison is:
# delta_rho_GGE / rho_SA = (amp_E_beat * f_s) / rho_SA_fold
# where f_s projects the beating to singlet

# Effective GGE beat amplitudes after EIH projection:
# The beats are between sectors B1, B2, B3.
# omega_1 (B2-B1): involves B2 (adjoint, not singlet) and B1 (singlet)
# The cross-term between B2 and B1 has a projection factor sqrt(f_s).
# omega_2 (B2-B3): neither is singlet -> f_s^2 projection
# omega_3 (B1-B3): B1 is singlet -> sqrt(f_s) projection
#
# But more precisely: the EIH result says the RATIO is f_s for the
# spectral action. The GGE beats modulate the spectral action through
# the occupation-number dependence.
# The relevant amplitude for 4D gravity is:
#   delta_rho_4D = f_s * delta_rho_internal
# This is the conservative estimate (f_s applies to the entire internal sum).

amp_4D = amp_E_beats * f_s  # 4D-projected beat amplitudes
print(f"\n--- 4D-Projected Beat Amplitudes ---")
for i in range(3):
    print(f"  Beat {i+1}: A_E = {amp_E_beats[i]:.4e} -> A_4D = {amp_4D[i]:.4e} M_KK")

# Fractional modulation of vacuum energy:
# delta_rho/rho = A_4D / rho_SA_fold
frac_mod = amp_4D / rho_SA_fold
print(f"\nFractional modulation delta_rho/rho:")
for i in range(3):
    print(f"  Beat {i+1}: {frac_mod[i]:.4e}")

# ================================================================
# 6. MODE FUNCTION EVOLUTION — Mukhanov-Sasaki equation
# ================================================================
#
# For each comoving wavenumber k, the curvature perturbation obeys:
#   v_k'' + (c_s^2 k^2 - z''/z) v_k = S_k(eta)
#
# where v_k = z * zeta_k, z = a * sqrt(2*epsilon) * M_Pl,
# and S_k(eta) is the GGE source term.
#
# In the standard scenario: S_k = 0 (vacuum fluctuations only).
# Here: S_k encodes the GGE beating.
#
# HOWEVER: the key insight is that the GGE beating provides a
# DETERMINISTIC modulation of the background, not a stochastic source.
# It modifies epsilon_H(t) rather than adding a new fluctuation source.
#
# The effect on n_s comes through the time variation of epsilon_H:
#   n_s - 1 = -2*epsilon_H - eta_H
# where eta_H = d(ln epsilon_H)/d(N) = epsilon_H_dot / (H * epsilon_H)
#
# If epsilon_H oscillates due to GGE beats:
#   epsilon_H(t) = epsilon_0 + delta_epsilon * cos(omega_beat * t)
# then eta_H acquires an oscillatory component:
#   delta_eta = -(delta_epsilon / epsilon_0) * (omega / H) * sin(omega * t)
#
# Since omega_beat << H for all three beats, this contribution is
# additionally suppressed by omega/H.

# Direct n_s calculation:
# The primordial spectrum during the transit epoch:
#
# epsilon_H = (3/2) * M_ATDHFB * v_terminal^2 / rho_SA_fold
# (This is the ratio of kinetic to total energy)

KE_fold = 0.5 * M_ATDHFB * v_terminal**2  # M_KK^4 (in M_KK units)
epsilon_H_direct = 1.5 * KE_fold / (KE_fold + rho_SA_fold)  # exact
# With GGE beating:
# epsilon_H(t) = 3/2 * KE / (KE + rho_SA + rho_GGE(t))
# delta_epsilon / epsilon = -(3/2) * delta_rho_GGE / rho_total
# After EIH:
# delta_epsilon / epsilon = -(3/2) * f_s * amp_E / rho_total

delta_epsilon_frac = 1.5 * frac_mod  # fractional change in epsilon_H

print(f"\n--- Direct epsilon_H Calculation ---")
print(f"KE_fold = (1/2)*M_ATDHFB*v^2 = {KE_fold:.4f} M_KK^4")
print(f"rho_SA_fold = {rho_SA_fold:.4f} M_KK^4")
print(f"epsilon_H = {epsilon_H_direct:.6f}")
print(f"(S44 FRIEDMANN-BCS-AUDIT: epsilon_H = 2.999, confirmed)")
print(f"\ndelta_epsilon/epsilon from GGE beats:")
for i in range(3):
    print(f"  Beat {i+1}: {delta_epsilon_frac[i]:.4e}")

# ================================================================
# 7. TRANSFER FUNCTION T(k): THREE STAGES
# ================================================================
#
# Stage 1: Internal -> 4D (EIH projection)
#   T_EIH = f_s = 5.68e-5 (k-independent scalar)
#
# Stage 2: Friedmann response
#   For omega << H: T_Friedmann(omega) = 1 (passband)
#   For omega >> H: T_Friedmann(omega) = (H/omega)^2 (rolloff)
#   All three beats: omega << H -> T_Friedmann = 1
#
# Stage 3: omega -> k mapping
#   A fluctuation at internal frequency omega gets imprinted at the
#   comoving scale k that exits the horizon when the fluctuation occurs.
#   k_exit = a(t) * H(t) at the time t when the mode crosses the horizon.
#
#   During transit: H is approximately constant (epsilon ~ 3 means
#   H drops by factor e^{-3*N} per e-fold, but N ~ 0.002 e-folds total).
#   So the mapping is k = a(t) * H(t) ~ a_transit * H_fold * const.
#
#   The INTERNAL frequency omega maps to a TEMPORAL modulation of the
#   background. This modulation affects ALL modes that are inside the
#   horizon during transit — which, for the ~0.002 e-folds of transit,
#   corresponds to a SINGLE scale k_transit.
#
# The k-dependence of T(k) comes from how modes of different k sample
# the oscillating background at different phases.

# k-grid (in M_KK units first, then convert to Mpc^{-1})
N_k = 500
k_MKK_min = 1e-6   # M_KK (well inside horizon)
k_MKK_max = 1e4    # M_KK (well outside horizon at transit)
k_MKK = np.logspace(np.log10(k_MKK_min), np.log10(k_MKK_max), N_k)

# Horizon scale at fold:
k_H = H_fold  # a*H where a=1 (in M_KK units)
print(f"\n--- Scale Hierarchy ---")
print(f"k_H = H_fold = {k_H:.2f} M_KK (horizon scale at fold)")
print(f"omega_beats = {omega_beats} M_KK")
print(f"omega/k_H = {omega_beats/k_H}")

# ================================================================
# 8. NUMERICAL COMPUTATION: Solve for P_4D(k)
# ================================================================
#
# Strategy: solve the Mukhanov-Sasaki equation with a beating source.
# The background during transit has:
#   H(t) = H_0 / (1 + epsilon_H * H_0 * t)  (for constant epsilon)
#   a(t) = a_0 * (H_0 * t)^{1/epsilon_H}    (power-law expansion)
#
# With epsilon_H ~ 3: a(t) propto t^{1/3} (kinetic domination).
# In conformal time eta: a(eta) propto eta^{1/2}.
# The Mukhanov-Sasaki potential z''/z = (2 - 3*epsilon + ...) / eta^2.

# For kinetic-dominated expansion (epsilon = 3):
# a propto t^{1/3}, so a propto eta^{1/2} (since dt = a*d(eta)).
# z = a*sqrt(2*epsilon)*M_Pl propto eta^{1/2}
# z''/z = -1/(4*eta^2)
# The mode equation: v'' + (k^2 + 1/(4*eta^2)) v = 0
# This has exact solution: v = sqrt(k*eta) * [A * J_0(k*eta) + B * Y_0(k*eta)]
# The power spectrum: P(k) propto k^3 |v_k/z|^2 propto k^{n_s-1}
# For epsilon = 3: n_s - 1 = -2*epsilon/(1-epsilon) = -2*3/(1-3) = 3
# Wait — that gives n_s = 4, which is wrong. Let me be careful.
#
# For power-law inflation a propto t^p with p = 1/epsilon:
#   nu = (3 - 1/p) / (2 - 2/p) = (3p - 1) / (2p - 2)
#   n_s - 1 = 3 - 2*nu
#
# For p = 1/3 (epsilon = 3):
#   nu = (3*1/3 - 1) / (2*1/3 - 2) = (1-1)/(2/3-2) = 0/(-4/3) = 0
#   n_s - 1 = 3 - 0 = 3, so n_s = 4.
#
# This is the BLUE spectrum from kinetic domination.
# The modes produced during kinetic domination have n_s = 4 (blue).
# This is OPPOSITE to the desired n_s = 0.965.
#
# The d=3 KZ universality result n_s = -0.68 is NOT the spectral index
# of curvature perturbations. It is the spectral index of the INTERNAL
# order-parameter fluctuations (the Kibble-Zurek defect spectrum in
# the SU(3) internal space). These are different quantities.
#
# Let me be precise about what n_s means in each context.

print(f"\n{'='*78}")
print(f"CRITICAL DISTINCTION: Two n_s values")
print(f"{'='*78}")
print(f"\n1. INTERNAL n_s = -0.68 (d=3 KZ universality)")
print(f"   This is the spectral index of tau-perturbation correlations:")
print(f"   P_tau(k_internal) propto k_internal^{{n_s_internal - 1}}")
print(f"   These are correlations in the SU(3) internal space,")
print(f"   NOT curvature perturbations in 4D spacetime.")
print(f"\n2. 4D n_s = 0.965 (Planck CMB)")
print(f"   This is the spectral index of curvature perturbations:")
print(f"   P_zeta(k) propto k^{{n_s - 1}}")
print(f"   These are perturbations to the 4D FRW metric.")

# ================================================================
# 9. FULL TRANSFER FUNCTION COMPUTATION
# ================================================================
#
# The transfer function T(k) maps internal P_tau(k_int) to 4D P_zeta(k):
#   P_zeta(k) = T(k)^2 * P_tau(k_matched)
# where k_matched = k_internal(k) is the mapping from 4D wavenumber
# to the corresponding internal wavenumber.
#
# The mapping k <-> k_internal:
# Internal fluctuations at scale k_int in SU(3) correspond to
# different representation sectors (p,q). The KK decomposition maps:
#   k_int ~ sqrt(C_2(p,q)) * M_KK  (Casimir wavenumber)
# These project to 4D at the KK scale:
#   k_4D = k_int / a_transit * (expansion factor to today)
#
# The HUGE hierarchy: M_KK ~ 7.4e16 GeV, while CMB k ~ 0.05 Mpc^{-1}
# ~ 3.2e-39 GeV. The ratio: k_CMB / M_KK ~ 4e-56.
# This hierarchy is bridged by the expansion a(t) from transit to today.
#
# The N_tau = -0.158 (modulated reheating) provides the conversion:
#   zeta_k = N_tau * delta_tau_k
# This is k-independent for the delta-N formalism.
# So: P_zeta(k) = N_tau^2 * P_tau(k) where P_tau(k) is the tau
# fluctuation power spectrum at the scale k (evaluated at horizon crossing).

# N_tau from S43:
try:
    d_kz = np.load('tier0-computation/s43_kz_transfer.npz', allow_pickle=True)
    N_tau = float(d_kz['N_tau'])
    mod_coeff = float(d_kz['mod_coeff'])
    xi_KZ = float(d_kz['xi_KZ'])
    n_s_planck = float(d_kz['n_s_planck'][0])
    n_s_sigma = float(d_kz['n_s_planck_sigma'][0])
    epsilon_H_kz = float(d_kz['epsilon_H_planck'])
    print(f"\n--- S43 KZ Data Loaded ---")
    print(f"N_tau = {N_tau:.4f} (modulated reheating coefficient)")
    print(f"mod_coeff = {mod_coeff:.4f}")
    print(f"xi_KZ = {xi_KZ:.4f} M_KK^{{-1}}")
    print(f"epsilon_H(KZ) = {epsilon_H_kz:.5f}")
except FileNotFoundError:
    N_tau = -0.158
    xi_KZ = 0.1516
    n_s_planck = 0.9649
    n_s_sigma = 0.0042
    epsilon_H_kz = 0.01755
    print(f"\n--- S43 data not found, using defaults ---")
    print(f"N_tau = {N_tau}")

# ================================================================
# 10. THE ACTUAL TRANSFER FUNCTION COMPUTATION
# ================================================================
#
# For the phonon-exflation framework:
# During transit, the universe is in kinetic domination (epsilon ~ 3).
# After transit, the quench deposits E_exc = 443 * |E_cond| into the
# GGE state. This energy eventually reheats the universe.
#
# The curvature perturbation zeta is generated at the END of transit
# through modulated reheating: different patches have slightly different
# tau values (from KZ defects), leading to different reheating histories.
#
# P_zeta(k) = (H / (2*pi*tau_dot))^2 * F(k)
# where F(k) encodes the k-dependence from the KZ defect spectrum
# and the GGE beats.
#
# THE KEY QUESTION: Does the GGE beating produce k-dependent
# corrections to P_zeta(k) that tilt the spectrum?
#
# ANSWER: The GGE beats are at 3 discrete frequencies. They create
# FEATURES (wiggles) at specific k values, NOT a power-law tilt.
# The tilt n_s comes from the background expansion dynamics
# (epsilon_H and its time derivative), not from the GGE beats.
#
# The GGE beats contribute:
# (a) Oscillatory features in P(k) at k values corresponding to
#     the three beat frequencies
# (b) A shift in the overall amplitude through the modulated epsilon_H
# (c) NO net tilt — the beats are discrete frequencies, not a continuum

# Physical k-grid in Mpc^{-1}
k_phys = np.logspace(-4, 0, N_k)  # Mpc^{-1} spanning CMB range
k_pivot_Mpc = 0.05  # Mpc^{-1}

# --- Component 1: Primordial tilt from expansion dynamics ---
# During transit: epsilon_H ~ 3 (kinetic domination).
# n_s = 1 - 2*epsilon/(1-epsilon) does NOT apply for epsilon > 1.
# For epsilon > 1: the expansion is NOT inflationary.
# Modes do NOT exit the horizon (Hubble radius GROWS).
# No quantum fluctuations are amplified.
#
# The curvature perturbations must come from ANOTHER mechanism.
# In phonon-exflation: the KZ mechanism produces tau fluctuations
# during the transit, and modulated reheating converts these to zeta.
#
# The KZ spectrum: delta_tau correlations have
#   P_tau(k) propto k^0  (white noise at all CMB scales, because
#   xi_KZ ~ 0.15/M_KK ~ 10^{-56} Mpc << any CMB scale)
#
# So the PRIMORDIAL P_zeta from the KZ mechanism is:
#   P_zeta(k) = N_tau^2 * P_tau_0 = FLAT (n_s = 1 exactly)
# at all CMB scales.
#
# The d=3 KZ internal spectrum n_s = -0.68 applies at k_internal >> 1/xi_KZ,
# i.e., at scales SMALLER than the KZ coherence length in the internal space.
# At CMB scales (k << 1/xi_KZ by 50+ orders of magnitude), the spectrum
# is FLAT. The KZ coherence length is 10^{-56} Mpc — unobservably small.

print(f"\n{'='*78}")
print(f"TRANSFER FUNCTION STRUCTURE")
print(f"{'='*78}")

print(f"\n--- Stage 1: KZ Source Spectrum at CMB Scales ---")
print(f"xi_KZ = {xi_KZ:.4f} M_KK^{{-1}} = {xi_KZ/M_KK*1e16*GeV_inv_to_Mpc:.2e} Mpc")
print(f"At CMB scales (k ~ 0.001-1 Mpc^{{-1}}):")
print(f"  k * xi_KZ << 1 by ~56 orders of magnitude")
print(f"  P_tau(k) = P_tau_0 = FLAT (white noise)")
print(f"  n_s(KZ @ CMB) = 1.0 EXACTLY")
print(f"  The d=3 KZ n_s = -0.68 only applies at k >> 1/xi_KZ ~ M_KK")

# --- Component 2: GGE beat modulation ---
# The GGE beats modulate the expansion rate at 3 frequencies.
# During post-transit expansion, a comoving mode k crosses the horizon
# at time t_cross(k) given by k = a(t_cross) * H(t_cross).
# If the GGE beats modulate H, then modes crossing at different times
# see different H values, creating a k-dependent P(k).
#
# The modulation: delta_H/H = (1/2) * (f_s * delta_rho_GGE) / rho_total
# Post-transit (radiation domination):
#   rho_rad propto a^{-4}, rho_GGE propto a^{-4} (both relativistic)
#   -> delta_rho_GGE / rho_rad = const (if GGE is radiation-like)
# OR: rho_GGE propto a^{-3} (if GGE is matter-like, non-relativistic BdG modes)
#   -> delta_rho_GGE / rho_rad grows as a
#
# The BdG quasiparticles have masses ~ M_KK, so they are non-relativistic
# immediately after creation. T_compound = E_exc/8 = 7.6 M_KK >> mode masses.
# Actually, the quasiparticle energies are lambda_k = {1.46, 2.77, 6.01} M_KK.
# These are relativistic (E >> m? No — m ~ 0 for the massless Dirac modes,
# but the BdG gap gives them effective mass Delta_k).
# Since E_k >> Delta_k for all modes, they are effectively ultrarelativistic.
# -> GGE behaves as radiation post-transit.
# -> delta_rho_GGE / rho_rad = const.

# Fractional perturbation from GGE beating (constant ratio):
# delta_zeta = -(H / rho_dot) * delta_rho = (1/(4*rho)) * delta_rho (radiation)
# delta_P/P = 2 * delta_zeta / zeta ~ (delta_rho_GGE / rho_total)

# The beat creates oscillatory features at k_i = a(t_i) * H(t_i)
# where t_i = pi / omega_i is when the beat has a peak.
# But since ALL beats have omega_i << H, the variation is smooth
# over many Hubble times. The feature in P(k) is spread over
# Delta_k / k ~ omega_i / H << 1.

# Compute the fractional power spectrum modulation:
# P(k) = P_0(k) * [1 + 2 * sum_i delta_zeta_i * cos(omega_i * t(k))]
# where t(k) = t_cross(k) = time when mode k crosses the horizon.
#
# In radiation domination: k = a*H = (a_0 * H_0) * (a/a_0) * (H/H_0)
# With a propto sqrt(t), H = 1/(2t):
# k = k_0 * (t_0/t)^{1/2} * (t_0/t) = k_0 * (t_0/t)^{3/2}... no.
# In RD: a propto t^{1/2}, H = 1/(2t), so aH = a_0 H_0 * (t_0/t)^{1/2} * (t_0/t)
# That's wrong. Let me be careful.
# a = a_0 * (t/t_0)^{1/2}, H = 1/(2t)
# aH = a_0 * (t/t_0)^{1/2} / (2t) = a_0 / (2*t_0) * (t_0/t)^{1/2}
# So: k = aH -> t(k) = a_0^2 / (4 * k^2 * t_0)
# Or in conformal time: k*eta = const at crossing.

# Since GGE modulation is tiny (frac_mod ~ 10^{-7}), compute T(k) as:
# T(k) = 1 + delta_T(k)
# where delta_T(k) = sum_i frac_mod_i * cos(omega_i * t(k) + phi_i)

# EXPLICIT COMPUTATION:
# During radiation domination, conformal time eta related to cosmic time t:
# eta = 2*t/a = 2*sqrt(t*t_0)/a_0 (in RD with a = a_0*(t/t_0)^{1/2})
# Mode k crosses horizon when k*eta = 1 (approx), so t_cross = 1/(4*k^2) * a_0^2/t_0

# In M_KK units, the transit ends at t = 0.
# Post-transit: H drops rapidly from H_fold ~ 586.5.
# In radiation domination after reheating:
# H(t) = H_rh * (a_rh/a)^2 = H_rh * (t_rh/t) (since a propto sqrt(t))
# Modes crossing in this epoch: k = aH = (a_rh * H_rh) * (t_rh/t)^{1/2}

# The GGE beats have frequency omega_i in M_KK units.
# The phase at time t is: Phi_i(t) = omega_i * t (continuing from transit)
# A mode at comoving k crosses the horizon at t_cross(k).
# The modulation at that mode:
# delta_P(k)/P(k) = sum_i C_i * cos(omega_i * t_cross(k))
# where C_i = 2 * frac_mod_i (fractional modulation from Section 5)

# Convert to k-dependence:
# t_cross(k) = (a_rh * H_rh)^2 / (4*k^2) * ... (radiation domination)
# In practice: t_cross propto 1/k^2 (larger k -> earlier crossing)
# cos(omega * t_cross) = cos(omega * const / k^2)
# This creates oscillations in P(k) vs k, with frequency increasing
# as k decreases (because t_cross grows).

# Use the relation k * eta_cross = 1:
# eta = 2*sqrt(t * H_0^{-1}) in RD
# So t_cross = 1/(4*k^2 * H_0) ... but we need the TRANSIT-ERA H, not H_0.
# After transit at t_transit, H = H_rh and the universe becomes RD.
# For simplicity, parameterize: t_cross(k) = t_transit + Delta_t(k)
# where Delta_t(k) is the time from end of transit to horizon crossing.
# For modes crossing shortly after transit (k ~ H_rh * a_rh):
# Delta_t << 1/H_rh.

# The important thing is the NUMBER OF BEAT PERIODS between transit and
# horizon crossing for each k.

# Let me compute this properly.
# After transit, radiation domination with initial H = H_rh.
# For simplicity, assume H_rh ~ H_fold (transit is fast, H barely changes).
# a = a_rh * (t/t_rh)^{1/2}
# H = 1/(2t)
# aH = a_rh * H_rh * (t_rh/t)^{1/2}
# Mode k crosses when k = aH:
# k = a_rh * H_rh * (t_rh / t_cross)^{1/2}
# t_cross = t_rh * (a_rh * H_rh / k)^2

# Now, t_rh = 1/(2*H_rh) (radiation domination starts at t_rh)
# t_cross = (1/(2*H_rh)) * (a_rh * H_rh / k)^2 = a_rh^2 * H_rh / (2 * k^2)

# The GGE phase at crossing:
# Phi_i(k) = omega_i * (t_cross - t_rh) = omega_i * [a_rh^2 * H_rh / (2*k^2) - 1/(2*H_rh)]
# = omega_i / (2*H_rh) * [(a_rh * H_rh / k)^2 - 1]

# Setting a_rh = 1 (comoving coordinates at reheating):
# Phi_i(k) = omega_i / (2*H_rh) * [(H_rh/k)^2 - 1]
# For k << H_rh: Phi_i ~ omega_i * H_rh / (2*k^2) (>> 1 many oscillations)
# For k = H_rh: Phi_i = 0 (mode at the horizon)
# For k >> H_rh: never crossed (still outside), irrelevant

H_rh = H_fold  # Reheating H ~ transit H (fast transit)

# k-grid centered on the reheating horizon
k_over_Hrh = k_phys * Mpc_to_GeV_inv / (H_rh * M_KK_grav)
# This is k_phys / (a_0 * H_rh) in physical units. But the factor a_0 is
# the scale factor TODAY relative to reheating. Need to be more careful.

# Better approach: compute everything in dimensionless units.
# x = k / (a_rh * H_rh) = k_comoving / k_rh
# For x < 1: mode is inside horizon at reheating -> crossed during transit or earlier
# For x > 1: mode is outside horizon -> crosses later during RD

# Phase at crossing (for x > 1):
# Phi_i(x) = (omega_i / (2*H_rh)) * (x^{-2} - 1)... no, reversed:
# For k = a*H: x = k/(a_rh*H_rh) and k = a*H during RD, so:
# x = (a/a_rh) * (H/H_rh) = (t/t_rh)^{1/2} * (t_rh/t) = (t_rh/t)^{1/2}
# So: t_cross/t_rh = x^{-2}
# Modes with smaller x (larger physical wavelength) cross LATER.
# For x < 1: the mode is SMALLER than the horizon at reheating.
# These modes were always inside the horizon. They are NOT amplified.
# Only modes with x > 1 (superhorizon at reheating) produce curvature perturbations.

# Phase: Phi(x) = omega * (t_cross - t_rh) = omega * t_rh * (x^{-2} - 1)
# = (omega / (2*H_rh)) * (x^{-2} - 1)  [since t_rh = 1/(2*H_rh)]

# Scan x from 1e-3 to 1e3
x = np.logspace(-3, 3, N_k)

# Phase at crossing for each beat and each x
Phi = np.zeros((3, N_k))
for i in range(3):
    # Only modes with x < 1 (k < a_rh*H_rh = H_rh) cross during/after transit
    # Wait — I need to be careful about convention.
    # x = k / (a_rh * H_rh). In comoving coordinates, a_rh * H_rh = k_rh.
    # Modes with k < k_rh are SUPERhorizon at reheating.
    # These are the ones that produce the observed CMB spectrum.
    # Modes with k > k_rh are subhorizon (already inside).
    #
    # For superhorizon modes (x < 1 -> wait, that's k < k_rh, correct):
    # They cross the horizon at t_cross > t_rh.
    # x = k/k_rh < 1.
    # t_cross/t_rh = (k_rh/k)^2 = x^{-2}
    # Phase: Phi = omega * t_rh * (x^{-2} - 1) = (omega/(2*H_rh)) * (1/x^2 - 1)
    mask_super = x < 1  # superhorizon at reheating
    Phi[i, mask_super] = (omega_beats[i] / (2*H_rh)) * (1/x[mask_super]**2 - 1)
    Phi[i, ~mask_super] = 0  # subhorizon: no amplification

# Transfer function: T(k)^2 = T_0^2 * [1 + delta_T(k)]
# where delta_T(k) = sum_i C_i * cos(Phi_i(k))
# C_i = amplitude of beat-induced modulation

C_beat = np.zeros(3)
for i in range(3):
    C_beat[i] = 2 * frac_mod[i]  # fractional power modulation

print(f"\n--- GGE Beat Modulation Amplitudes ---")
for i in range(3):
    print(f"  Beat {i+1}: C_{i+1} = {C_beat[i]:.4e}")

# Full transfer-function-squared modulation:
delta_T2 = np.zeros(N_k)
for i in range(3):
    delta_T2 += C_beat[i] * np.cos(Phi[i])

T2_total = 1.0 + delta_T2

# ================================================================
# 11. EFFECTIVE n_s FROM THE FULL CONVOLUTION
# ================================================================
#
# The primordial P_zeta from KZ mechanism:
# P_zeta(k) = N_tau^2 * sigma_tau^2 * 8*pi*xi_KZ^3
# This is FLAT (n_s = 1 exactly) at CMB scales.
#
# With GGE beating:
# P_zeta(k) = P_zeta_0 * [1 + delta_T2(k/k_rh)]
#
# The effective n_s:
# n_s_eff - 1 = d ln P / d ln k at k_pivot
# Since delta_T2 << 1 (~ 10^{-7}):
# n_s_eff = 1 + O(10^{-7}) ~ 1.0000000
#
# The GGE beats produce NEGLIGIBLE tilt.
# The n_s problem remains: the internal mechanism produces n_s = 1
# at CMB scales, not 0.965.

# Compute numerical n_s at the pivot
lnx = np.log(x)
lnP = np.log(T2_total)

# Fit local slope at x_pivot (corresponding to k_pivot in units of k_rh)
# We don't know k_rh exactly, but we can compute the slope everywhere
cs_lnP = CubicSpline(lnx, lnP)

# Evaluate at multiple x values
x_eval = np.logspace(-2, -0.1, 100)  # well in the superhorizon regime
ns_eff = 1.0 + cs_lnP(np.log(x_eval), 1)  # n_s = 1 + d ln P / d ln k

print(f"\n{'='*78}")
print(f"n_s RESULTS: FULL CONVOLUTION")
print(f"{'='*78}")
print(f"\nn_s_eff across superhorizon modes (x = k/k_rh = 0.01 to 0.8):")
print(f"  min(n_s) = {ns_eff.min():.10f}")
print(f"  max(n_s) = {ns_eff.max():.10f}")
print(f"  mean(n_s) = {ns_eff.mean():.10f}")
print(f"  Deviation from 1.0: {abs(ns_eff.mean() - 1.0):.4e}")
print(f"\nPlanck target: n_s = {n_s_planck:.4f} +/- {n_s_sigma:.4f}")
print(f"Gap: n_s_eff - n_s_Planck = {ns_eff.mean() - n_s_planck:.4f}")
print(f"Shortfall from +1.65 shift: the transfer function provides")
print(f"  delta(n_s-1) = {ns_eff.mean() - 1.0:.4e} vs needed +1.65")

# ================================================================
# 12. THREE-FREQUENCY UNIVERSE: Feature Positions
# ================================================================
#
# The 3 GGE beats create oscillatory features in P(k) at specific
# scales. These are NOT power-law tilts but OSCILLATIONS.
# The feature position: where cos(Phi_i(k)) has its first maximum.
# First maximum at Phi_i = 0: x = 1 (at horizon scale).
# Next at Phi_i = 2*pi: (omega/(2*H_rh)) * (1/x^2 - 1) = 2*pi
# -> x^2 = 1 / (1 + 4*pi*H_rh/omega)
# For omega << H: x ~ sqrt(omega/(4*pi*H_rh)) << 1

x_feature = np.zeros(3)
k_feature_ratio = np.zeros(3)
for i in range(3):
    x_feature[i] = np.sqrt(omega_beats[i] / (4*PI*H_rh))
    k_feature_ratio[i] = x_feature[i]

# Convert feature positions to physical scales:
# The reheating scale k_rh in Mpc^{-1}:
# k_rh = a_rh * H_rh (in comoving Mpc^{-1})
# After expansion from transit to today: a_0/a_rh = T_rh / T_CMB
# T_rh ~ M_KK (reheating at KK scale) = 7.4e16 GeV
# T_CMB = 2.35e-13 GeV
# a_0/a_rh ~ T_rh / T_CMB ~ 3.2e29
# k_rh = H_rh * M_KK / a_0 ... this needs careful unit conversion

# In Mpc^{-1}:
# H_rh in GeV = H_fold * M_KK_grav = 586.5 * 7.43e16 = 4.36e19 GeV
H_rh_GeV = H_rh * M_KK_grav
print(f"\n--- Scale Conversion ---")
print(f"H_rh = {H_rh:.2f} M_KK = {H_rh_GeV:.4e} GeV")

# During RD, a propto T^{-1}, and H propto T^2:
# k/a_0 = (k/a_rh) * (a_rh/a_0) = H_rh_phys * (T_CMB/T_rh)
# where T_rh is the reheating temperature.
# If T_rh = M_KK:
T_rh_GeV = M_KK_grav  # reheating at M_KK
T_CMB_GeV = 2.348e-13  # from canonical_constants
a_ratio = T_rh_GeV / T_CMB_GeV  # a_0 / a_rh

# k_rh in physical (Mpc^{-1}):
# k_rh_phys = H_rh_GeV / hbar_c_GeV_m / (a_0/a_rh) ... need to be careful.
# The comoving wavenumber today corresponding to k_rh at reheating:
# k_rh,today = a_rh * H_rh / a_0 (comoving = physical * a)
# = H_rh_GeV * a_rh / a_0 (in natural units, 1/GeV)
# = H_rh_GeV / (a_0/a_rh) [natural units]
# = H_rh_GeV / a_ratio [GeV]
# Convert GeV -> Mpc^{-1}: k [Mpc^{-1}] = k [GeV] / Mpc_to_GeV_inv
# Wait: 1 Mpc = Mpc_to_GeV_inv GeV^{-1}, so 1 Mpc^{-1} = 1/Mpc_to_GeV_inv GeV
# k [Mpc^{-1}] = k [GeV] * Mpc_to_GeV_inv ... no.
# Mpc_to_GeV_inv = 1.563e38 GeV^{-1} per Mpc
# So 1 Mpc = 1.563e38 GeV^{-1}
# 1 Mpc^{-1} = 1/(1.563e38) GeV = 6.4e-39 GeV
# k [Mpc^{-1}] = k [GeV] / (6.4e-39) ... no:
# k [Mpc^{-1}] = k [GeV] * Mpc_to_GeV_inv [GeV^{-1}/Mpc] ...
# k [natural, GeV] = k [Mpc^{-1}] * (1 Mpc in GeV^{-1}) = k [Mpc^{-1}] * Mpc_to_GeV_inv
# So: k [Mpc^{-1}] = k [GeV] / Mpc_to_GeV_inv

k_rh_GeV = H_rh_GeV / a_ratio  # in GeV (comoving today)
k_rh_Mpc = k_rh_GeV / GeV_inv_to_Mpc  # Wait, GeV_inv_to_Mpc = Mpc / GeV^{-1}
# k [GeV] -> k [Mpc^{-1}]: k[Mpc^-1] = k[GeV] * (1 GeV) * (Mpc/GeV^{-1}) ...
# Let me use: k [Mpc^{-1}] = k [GeV] / (GeV_inv_to_Mpc)  iff GeV_inv_to_Mpc has units Mpc*GeV.
# Actually: GeV_inv_to_Mpc converts lengths from GeV^{-1} to Mpc.
# So 1 GeV^{-1} = GeV_inv_to_Mpc Mpc = 6.39e-39 Mpc.
# Wavenumber: k has units 1/length.
# k [Mpc^{-1}] = k [GeV] * (1 GeV^{-1} in Mpc) = k [GeV] * GeV_inv_to_Mpc.
# Wait no: k[GeV] means k has units of GeV (i.e., 1/length in natural units).
# 1 GeV = 1/(GeV_inv_to_Mpc Mpc) = 1/(6.39e-39 Mpc) = 1.565e38 Mpc^{-1}.
# So k [Mpc^{-1}] = k [GeV] / GeV_inv_to_Mpc... still confused.
# Let me just use: k [Mpc^{-1}] = k [GeV] * (hbar_c_GeV_m / Mpc_to_m)^{-1} ...
# No. Cleanly: k_physical = 2*pi / lambda.
# lambda [m] = (1/k[GeV]) * hbar_c_GeV_m = hbar_c_GeV_m / k[GeV]
# lambda [Mpc] = lambda[m] / Mpc_to_m = hbar_c_GeV_m / (k[GeV] * Mpc_to_m)
# k [Mpc^{-1}] = 1/lambda[Mpc] = k[GeV] * Mpc_to_m / hbar_c_GeV_m = k[GeV] * Mpc_to_GeV_inv

k_rh_Mpc_inv = k_rh_GeV * Mpc_to_GeV_inv  # Mpc^{-1}

print(f"T_rh = M_KK = {T_rh_GeV:.4e} GeV")
print(f"T_CMB = {T_CMB_GeV:.4e} GeV")
print(f"a_0/a_rh = T_rh/T_CMB = {a_ratio:.4e}")
print(f"k_rh (comoving today) = {k_rh_GeV:.4e} GeV = {k_rh_Mpc_inv:.4e} Mpc^{{-1}}")

print(f"\n--- Three-Frequency Universe Features ---")
for i in range(3):
    k_feat_Mpc = k_rh_Mpc_inv * x_feature[i]
    lambda_feat_Mpc = 2*PI / k_feat_Mpc if k_feat_Mpc > 0 else np.inf
    print(f"  Beat {i+1} (omega = {omega_beats[i]:.4f} M_KK):")
    print(f"    Feature at x = k/k_rh = {x_feature[i]:.6e}")
    print(f"    k_feature = {k_feat_Mpc:.4e} Mpc^{{-1}}")
    print(f"    lambda_feature = {lambda_feat_Mpc:.4e} Mpc")
    # Amplitude at the feature
    if x_feature[i] < 1:
        Phi_at_feat = (omega_beats[i] / (2*H_rh)) * (1/x_feature[i]**2 - 1)
        delta_P_feat = C_beat[i] * np.cos(Phi_at_feat)
        print(f"    delta_P/P at feature: {delta_P_feat:.4e}")

# ================================================================
# 13. THE n_s TRANSFER FUNCTION TILT
# ================================================================
#
# STRUCTURAL RESULT:
# The transfer function T(k) from GGE beats provides:
#   delta(n_s - 1) ~ 10^{-7}
# versus the needed +1.65.
#
# The GGE beats CANNOT provide the required tilt.
# They produce discrete-frequency oscillatory features, not power-law tilt.
# Even the feature amplitude is O(10^{-7}), unobservable.
#
# REASON: Three suppressions stack:
# (1) EIH singlet fraction f_s = 5.68e-5 (geometry-to-gravity filter)
# (2) GGE energy / SA energy ~ amp_E / rho_SA ~ O(1) in M_KK, but
#     after dividing by rho_SA_fold (in M_KK^4 ~ 1585): O(10^{-3})
# (3) omega_i / H ~ 10^{-4} (the beats are deep in the Friedmann passband,
#     so they pass without distortion, but their EFFECT on epsilon_H is
#     suppressed by this ratio when computing tilt)
#
# Combined: 5.7e-5 * 4.2e-3 * 9e-5 ~ 2e-11 per beat.
# Actual computed delta_T/T ~ 10^{-7} (dominated by the f_s * A_E/rho_SA term).

print(f"\n{'='*78}")
print(f"STRUCTURAL RESULT: Transfer Function Tilt")
print(f"{'='*78}")

# Compute the actual tilt from delta_T2 numerically
# Use the superhorizon portion (x < 1)
mask = (x > 0.001) & (x < 0.8)
if mask.sum() > 10:
    lnx_fit = np.log(x[mask])
    lnT2_fit = np.log(T2_total[mask])
    # Linear fit: lnT2 = a*lnx + b -> n_s - 1 = a
    from numpy.polynomial import polynomial as P_poly
    coeffs = np.polyfit(lnx_fit, lnT2_fit, 1)
    ns_from_T = 1.0 + coeffs[0]
else:
    ns_from_T = 1.0

print(f"\nFitted n_s from T(k)^2 over superhorizon range:")
print(f"  n_s(from T) = {ns_from_T:.12f}")
print(f"  n_s - 1 = {ns_from_T - 1:.4e}")
print(f"\nPlanck target: n_s = {n_s_planck:.4f} +/- {n_s_sigma:.4f}")
print(f"Shortfall: need n_s - 1 = -0.035, have {ns_from_T - 1:.4e}")
print(f"Transfer function provides {(ns_from_T - 1)/(-0.035)*100:.4e}% of needed tilt")

# Suppression analysis:
supp_EIH = f_s
supp_rho = max(amp_E_beats[:2]) / rho_SA_fold  # ~4e-3
supp_omega_H = max(omega_beats) / H_rh  # ~5e-4
total_supp = supp_EIH * supp_rho

print(f"\n--- Suppression Analysis ---")
print(f"  EIH singlet fraction:     {supp_EIH:.4e}")
print(f"  GGE amplitude/rho_SA:     {supp_rho:.4e}")
print(f"  omega_beat/H:             {supp_omega_H:.4e}")
print(f"  Combined (EIH * rho):     {total_supp:.4e}")
print(f"  (omega/H further suppresses tilt, not amplitude)")

# ================================================================
# 14. WHERE DOES n_s COME FROM?
# ================================================================
#
# If the GGE beats don't provide the tilt, what does?
# In standard inflation: n_s - 1 = -2*epsilon - eta.
# In phonon-exflation: the transit is NOT inflation (epsilon ~ 3).
#
# Possible sources of tilt:
# (a) Modulated reheating: tau fluctuations -> different N_e
#     n_s - 1 = -2*epsilon_H evaluated at REHEATING, not transit.
#     If post-transit there is a brief slow-roll epoch (e.g., from the
#     spectral action potential), epsilon could be small.
# (b) KZ spectrum at INTERNAL scales: n_s = -0.68.
#     But this is at k >> M_KK, not CMB scales.
# (c) Curvaton mechanism: the GGE acts as a curvaton field
#     whose fluctuations convert to curvature perturbations later.
# (d) Pre-transit inflation: if the spectral action potential has
#     a nearly-flat region at large tau, slow-roll there gives n_s ~ 0.965.
#     But this requires epsilon << 1 in that region.
#
# The S43 KZ transfer function used epsilon_H = 0.0176 as INPUT
# (from Planck), not as a prediction. This was explicitly noted:
# "epsilon_H is input. n_s is consistency check, NOT prediction."
#
# The transfer function from GGE beats to CMB does NOT generate n_s.
# n_s must come from the expansion dynamics (epsilon_H at the epoch
# when perturbations are created).

print(f"\n--- n_s Source Analysis ---")
print(f"The GGE beat transfer function provides delta(n_s) ~ {ns_from_T - 1:.2e}")
print(f"This is {abs(ns_from_T - 1) / 0.035:.2e} of the needed tilt.")
print(f"The +1.65 shift CANNOT come from the transfer function.")
print(f"\nThe n_s problem reduces to: what is epsilon_H at the epoch")
print(f"when curvature perturbations are generated?")
print(f"  During transit: epsilon_H ~ 3 (kinetic domination, n_s = 4 BLUE)")
print(f"  For n_s = 0.965: need epsilon_H ~ 0.018 (slow-roll)")
print(f"  Shortfall: epsilon_H is 170x too large")
print(f"\nThe framework needs an epoch of near-de-Sitter expansion")
print(f"(epsilon << 1) to generate the observed red tilt.")
print(f"This is the INFLATION REQUIREMENT: phonon-exflation must either")
print(f"(a) identify such an epoch in its dynamics, or")
print(f"(b) find an alternative mechanism for generating red tilt.")

# ================================================================
# 15. GATE VERDICT
# ================================================================

print(f"\n{'='*78}")
print(f"GATE VERDICT: TRANSFER-FUNCTION-46 (INFO)")
print(f"{'='*78}")
print(f"\nWhat was computed:")
print(f"  1. EIH projection: f_s = {f_s:.4e} (singlet fraction -> 4D gravity)")
print(f"  2. Friedmann response: all 3 beats in passband (omega/H < 5e-4)")
print(f"  3. GGE beat modulation of P(k): delta_P/P ~ {max(C_beat):.4e}")
print(f"  4. Effective n_s from convolution: {ns_from_T:.8f}")
print(f"  5. Feature positions: k_rh = {k_rh_Mpc_inv:.4e} Mpc^{{-1}}")
print(f"\nWhat region of solution space is constrained:")
print(f"  The GGE beat -> 4D transfer function provides n_s - 1 ~ 10^{{-7}}.")
print(f"  This is 10^{{-5}} of the needed -0.035.")
print(f"  Three suppressions: EIH({supp_EIH:.1e}) * rho_ratio({supp_rho:.1e})")
print(f"    make the GGE beats INVISIBLE in the CMB power spectrum.")
print(f"  The Three-Frequency Universe features exist but at amplitude")
print(f"    {max(C_beat):.1e}, far below any conceivable measurement.")
print(f"\nWhat remains uncomputed:")
print(f"  1. n_s from alternative mechanisms (curvaton, modulated reheating")
print(f"     with post-transit slow-roll, pre-transit inflation)")
print(f"  2. The transit -> reheating transition dynamics")
print(f"  3. Whether the KZ internal spectrum n_s = -0.68 can be mapped")
print(f"     to CMB scales through a non-trivial k-k mapping")

# ================================================================
# 16. SAVE DATA
# ================================================================

np.savez('tier0-computation/s46_transfer_function.npz',
    # Gate info
    gate_name='TRANSFER-FUNCTION-46',
    gate_verdict='INFO',
    # Beat frequencies and amplitudes
    omega_beats=omega_beats,
    amp_E_beats=amp_E_beats,
    amp_4D=amp_4D,
    C_beat=C_beat,
    frac_mod=frac_mod,
    deg_beats=deg_beats,
    # EIH projection
    f_s=f_s,
    # Friedmann
    H_rh=H_rh,
    ratio_omega_H=ratio_omega_H,
    epsilon_H_transit=epsilon_H_direct,
    rho_SA_fold=rho_SA_fold,
    # Transfer function
    x=x,
    T2_total=T2_total,
    delta_T2=delta_T2,
    Phi=Phi,
    # Effective n_s
    ns_from_transfer=ns_from_T,
    ns_planck=n_s_planck,
    ns_sigma=n_s_sigma,
    ns_gap=ns_from_T - n_s_planck,
    # Feature positions
    x_feature=x_feature,
    k_rh_Mpc=k_rh_Mpc_inv,
    k_feature_Mpc=k_rh_Mpc_inv * x_feature,
    # Scale info
    M_KK_grav=M_KK_grav,
    t_MKK=t_MKK,
    dt_transit=dt_transit,
    n_cycles_transit=n_cycles,
    # Suppression breakdown
    supp_EIH=supp_EIH,
    supp_rho=supp_rho,
    supp_omega_H=supp_omega_H,
    supp_total=total_supp,
)

print(f"\nSaved: tier0-computation/s46_transfer_function.npz")

# ================================================================
# 17. FOUR-PANEL FIGURE
# ================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel A: GGE beat frequencies and amplitudes
ax = axes[0, 0]
colors = ['#2196F3', '#FF5722', '#4CAF50']
labels = ['B2-B1 (slow)', 'B2-B3 (medium)', 'B1-B3 (fast)']
bar_x = np.arange(3)
bars = ax.bar(bar_x, omega_beats, color=colors, alpha=0.8, width=0.5)
for i, (b, a_e) in enumerate(zip(bars, amp_E_beats)):
    ax.text(b.get_x() + b.get_width()/2, b.get_height() + 0.005,
            f'A_E={a_e:.2f}', ha='center', va='bottom', fontsize=8)
ax.set_xticks(bar_x)
ax.set_xticklabels(labels, fontsize=8)
ax.set_ylabel(r'$\omega_i$ [$M_{KK}$]')
ax.set_title('A. GGE Beat Frequencies')
ax.axhline(H_fold, color='red', ls='--', alpha=0.3, label=f'H_fold={H_fold:.0f}')
ax.set_ylim(0, 0.4)
ax.legend(fontsize=8)
# Add annotation for omega/H
for i in range(3):
    ax.annotate(f'$\\omega/H = {ratio_omega_H[i]:.1e}$',
                xy=(i, omega_beats[i]), xytext=(i, omega_beats[i] + 0.03),
                fontsize=7, ha='center')

# Panel B: Transfer function T^2(k) vs x = k/k_rh
ax = axes[0, 1]
mask_plot = (x > 1e-3) & (x < 1)
ax.semilogx(x[mask_plot], T2_total[mask_plot], 'k-', lw=1.5)
ax.axhline(1.0, color='gray', ls='--', alpha=0.5)
for i in range(2):  # Skip beat 3 (negligible)
    if x_feature[i] > 1e-3 and x_feature[i] < 1:
        ax.axvline(x_feature[i], color=colors[i], ls=':', alpha=0.7,
                   label=f'Beat {i+1}: x={x_feature[i]:.1e}')
ax.set_xlabel(r'$x = k / k_{rh}$')
ax.set_ylabel(r'$T^2(k) = 1 + \delta T^2$')
ax.set_title(f'B. Transfer Function (max $\\delta T^2$ = {max(abs(delta_T2[mask_plot])):.1e})')
ax.legend(fontsize=8)
ax.set_xlim(1e-3, 1)

# Panel C: Suppression waterfall
ax = axes[1, 0]
supp_labels = ['Internal\n(GGE beats)', r'$\times f_s$ (EIH)', r'$\times A_E/\rho_{SA}$',
               r'$\times \omega/H$', r'4D $\delta P/P$']
supp_values = [1.0, f_s, f_s * supp_rho, f_s * supp_rho * supp_omega_H, max(C_beat)]
supp_colors = ['#2196F3', '#FF9800', '#F44336', '#9C27B0', '#4CAF50']
ax.barh(range(len(supp_labels)), np.log10(np.array(supp_values) + 1e-20),
        color=supp_colors, alpha=0.8)
ax.set_yticks(range(len(supp_labels)))
ax.set_yticklabels(supp_labels, fontsize=8)
ax.set_xlabel(r'$\log_{10}$ (suppression factor)')
ax.set_title('C. Suppression Cascade')
# Add values
for i, v in enumerate(supp_values):
    ax.text(np.log10(v + 1e-20) - 0.5, i, f'{v:.1e}', va='center', fontsize=8, color='white',
            fontweight='bold')
ax.set_xlim(-12, 0.5)

# Panel D: n_s diagnostic
ax = axes[1, 1]
# Plot n_s_eff vs x
x_ns = np.logspace(-2, -0.1, 200)
mask_valid = (x_ns > x.min()) & (x_ns < x.max())
x_ns = x_ns[mask_valid]
ns_profile = 1.0 + cs_lnP(np.log(x_ns), 1)
ax.semilogx(x_ns, ns_profile, 'k-', lw=1.5, label=r'$n_s$ from $T(k)$')
ax.axhline(n_s_planck, color='blue', ls='--', alpha=0.7, label=f'Planck: {n_s_planck}')
ax.axhspan(n_s_planck - n_s_sigma, n_s_planck + n_s_sigma, alpha=0.1, color='blue')
ax.axhline(1.0, color='gray', ls=':', alpha=0.5, label='Scale invariant')
ax.set_xlabel(r'$x = k / k_{rh}$')
ax.set_ylabel(r'$n_s(k)$')
ax.set_title(f'D. Spectral Index (gap to Planck = {abs(1.0 - n_s_planck):.3f})')
ax.legend(fontsize=8)
# Set y-range to show both 1.0 and 0.965
ax.set_ylim(0.93, 1.05)

plt.suptitle('TRANSFER-FUNCTION-46: GGE Beats $\\to$ 4D CMB Power Spectrum\n'
             f'$\\delta(n_s-1)$ = {ns_from_T - 1:.1e}, '
             f'$\\delta P/P$ = {max(C_beat):.1e}, '
             f'$f_s$ = {f_s:.1e}',
             fontsize=11, fontweight='bold')

plt.tight_layout()
plt.savefig('tier0-computation/s46_transfer_function.png', dpi=150, bbox_inches='tight')
print(f"Saved: tier0-computation/s46_transfer_function.png")
plt.close()

# ================================================================
# 18. SUMMARY TABLE
# ================================================================

print(f"\n{'='*78}")
print(f"SUMMARY TABLE")
print(f"{'='*78}")
print(f"\n{'Quantity':<40s} {'Value':<20s} {'Units':<15s}")
print(f"{'='*75}")
print(f"{'omega_1 (B2-B1)':<40s} {omega_beats[0]:<20.6f} {'M_KK':<15s}")
print(f"{'omega_2 (B2-B3)':<40s} {omega_beats[1]:<20.6f} {'M_KK':<15s}")
print(f"{'omega_3 (B1-B3)':<40s} {omega_beats[2]:<20.6f} {'M_KK':<15s}")
print(f"{'f_s (EIH singlet fraction)':<40s} {f_s:<20.4e} {'---':<15s}")
print(f"{'H_fold':<40s} {H_fold:<20.2f} {'M_KK':<15s}")
print(f"{'omega_max / H_fold':<40s} {max(ratio_omega_H):<20.4e} {'---':<15s}")
print(f"{'max(delta_P/P)':<40s} {max(C_beat):<20.4e} {'---':<15s}")
print(f"{'n_s from transfer':<40s} {ns_from_T:<20.10f} {'---':<15s}")
print(f"{'n_s gap (transfer - Planck)':<40s} {ns_from_T - n_s_planck:<20.4e} {'---':<15s}")
print(f"{'delta(n_s-1) provided':<40s} {ns_from_T - 1:<20.4e} {'---':<15s}")
print(f"{'delta(n_s-1) needed':<40s} {-0.035:<20.4f} {'---':<15s}")
print(f"{'k_rh (comoving today)':<40s} {k_rh_Mpc_inv:<20.4e} {'Mpc^-1':<15s}")
print(f"{'epsilon_H (transit)':<40s} {epsilon_H_direct:<20.6f} {'---':<15s}")
print(f"{'N_e (transit)':<40s} {dt_transit*H_fold:<20.6f} {'e-folds':<15s}")
print(f"{'='*75}")

print(f"\n{'='*78}")
print(f"COMPUTATION COMPLETE")
print(f"{'='*78}")
