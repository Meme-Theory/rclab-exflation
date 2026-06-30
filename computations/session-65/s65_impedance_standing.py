#!/usr/bin/env python3
"""
S65 IMPEDANCE-65: BLV-BA Impedance Matching — Standing Waves and A_s
=====================================================================

The three-speed acoustic system (c_BLV = 0.485, c_BA = 0.399, c_L ~ 0.025)
creates impedance mismatches at each interface. These mismatches produce
partial reflections, forming standing waves in a multi-layer acoustic cavity.

RESONANCE STRUCTURE:
  What oscillates: Scalar (density/phase) perturbations propagating through
    the three acoustic channels.
  What is the cavity: The BA layer sandwiched between the BLV fabric channel
    (fast) and the Leggett inter-band channel (slow). Each interface partially
    reflects. The cavity "length" is set by the Hubble scale L ~ c_BA / H.
  Boundary conditions: Impedance matching at two interfaces:
    BLV|BA (Gamma_1) and BA|Leggett (Gamma_2).
  Normal modes: Standing waves satisfying round-trip phase = 2*pi*n.
    Resonance frequencies: omega_n = n * pi * c_BA / L.
  Selection mechanism: The finesse F = pi*sqrt(R1*R2)/(1-R1*R2) determines
    the sharpness and amplitude of each resonance. At resonance, the
    transmitted amplitude is enhanced by 1/(1-R1*R2).

CONDENSED MATTER ANALOG:
  This is a direct analog of a multi-layer phononic crystal. In superfluid
  He-3B, the three sound modes (first sound, second sound, spin-orbit sound)
  create exactly this kind of multi-channel acoustic cavity. The impedance
  mismatch between first and second sound at the normal-superfluid boundary
  produces Kapitza resistance (thermal boundary resistance), and standing
  waves in the superfluid gap produce Shapiro steps in Josephson junctions.

  In Tesla's work: this is the quarter-wave resonator. Tesla's Colorado
  Springs oscillator exploited the impedance mismatch between the primary
  (high Z) and secondary (low Z) coils to create standing waves at the
  quarter-wave frequency. The enhancement factor at resonance is the Q
  of the cavity.

PHYSICS:
  For a three-layer acoustic system with impedances Z_1, Z_2, Z_3
  and layer thickness d_2 (the BA cavity):

  Reflection coefficients at interfaces:
    r_12 = (Z_1 - Z_2) / (Z_1 + Z_2)     [BLV -> BA]             (1)
    r_23 = (Z_2 - Z_3) / (Z_2 + Z_3)     [BA -> Leggett]         (2)

  Transfer matrix for the BA layer:
    T = [[cos(phi), -i*sin(phi)/Z_2], [-i*Z_2*sin(phi), cos(phi)]]  (3)
    where phi = omega * d_2 / c_BA                                  (4)

  Total transmission through three-layer stack:
    |t|^2 = 1 / (1 + F_12*sin^2(phi) + F_23*sin^2(phi)
             + 2*F_12*F_23*sin^2(phi)*cos^2(phi)
             + ...)
    Exact: use full 2x2 transfer matrix product.                    (5)

  For the FULL four-speed system (mod, BLV, BA, L), we construct the
  4x4 problem as three 2x2 transfer matrices cascaded.

  A_s modulation: The scalar amplitude A_s is enhanced at frequencies
  where the Fabry-Perot transmission peaks. The modulation is:
    delta A_s / A_s = sum_n (T_n - <T>) * W_n                      (6)
  where T_n is the transmission at resonance n and W_n is the spectral
  weight (fraction of primordial power at that frequency).

Gate: IMPEDANCE-65
    INFO: Report standing wave frequencies, enhancement factors, and
          A_s modulation at CMB-relevant scales.

Input: s64_sound_speed.npz, s56_cba_sound.npz, s64_linewidth_hierarchy.npz,
       s65_leggett_rpa.npz, canonical_constants.py
Output: s65_impedance_standing.npz, s65_impedance_standing.png

Session: S65 W7-D
Author: Tesla-Resonance Agent
"""

import numpy as np
from scipy.optimize import brentq
from scipy.signal import find_peaks
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import sys
import os
import time

t_start = time.time()

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
sys.path.insert(0, SCRIPT_DIR)

from canonical_constants import (
    tau_fold, Delta_0_OES, N_dof_BCS, M_KK, PI,
    E_B1, E_B2_mean, E_B3_mean, N_cells,
    J_C2, J_su2, J_u1, E_cond, xi_BCS,
    H_fold, T_acoustic, a0_fold, a2_fold,
    G_DeWitt, Z_fold, dS_fold, d2S_fold, S_fold,
    Delta_B3, A_s_CMB, c_fabric,
)

def projpath(*parts):
    """Resolve path relative to project root."""
    return os.path.join(PROJECT_ROOT, *parts)

# =============================================================================
# Section 1: Load Input Data
# =============================================================================
print("=" * 78)
print("IMPEDANCE-65: BLV-BA Standing Wave Resonances and A_s Modulation")
print("Tesla-Resonance | S65 W7-D")
print("=" * 78)

# S64 sound speed data
d_s64 = np.load(projpath('computations', 's64_sound_speed.npz'),
                allow_pickle=True)
c_BLV = float(d_s64['c_BLV'])          # 0.485 (fabric scalar speed)
c_BA_S56 = float(d_s64['c_BA_S56'])    # 0.399 (Anderson-Bogoliubov)
c_Leggett_range = d_s64['c_Leggett_range']  # [0.019, 0.032]
c_mod = float(d_s64['c_mod'])           # 1.0 (canonical modulus)
epsilon_H = float(d_s64['epsilon_H_SA'])
c_BLV_arr = d_s64['c_BLV_arr']         # tau-dependent BLV speed
tau_grid = d_s64['tau_grid']

# S56 BA sound data
d_s56 = np.load(projpath('computations', 's56_cba_sound.npz'),
                allow_pickle=True)
c_BA_fold = float(d_s56['c_BA_fold'])   # 0.399
c_BA_tau = d_s56['c_BA_tau']            # tau-dependent
tau_BA = d_s56['tau_values']
omega_BA_modes = d_s56['omega_BA']      # (50, 31) — BA mode spectrum
J_C2_tau = d_s56['J_C2_tau']

# S64 linewidth data (for damping)
d_lw = np.load(projpath('computations', 's64_linewidth_hierarchy.npz'),
               allow_pickle=True)
Gamma_B1 = float(d_lw['Gamma_B1'])
Gamma_B2 = float(d_lw['Gamma_B2'])
Gamma_B3 = float(d_lw['Gamma_B3'])

# S65 Leggett RPA data (collective damping)
d_rpa = np.load(projpath('computations', 's65_leggett_rpa.npz'),
                allow_pickle=True)
omega_L1 = float(d_rpa['omega_L1_RPA'])   # 0.0684 M_KK
omega_L2 = float(d_rpa['omega_L2_RPA'])   # 0.0952 M_KK
Gamma_L1 = float(d_rpa['Gamma_L1_RPA'])   # 0.00486 M_KK
Gamma_L2 = float(d_rpa['Gamma_L2_RPA'])   # 0.01875 M_KK
c_Leggett_mid = np.mean(c_Leggett_range)  # 0.0255

print(f"\n{'='*40}")
print("INPUT: Four-Speed Hierarchy")
print(f"{'='*40}")
print(f"  c_mod    = {c_mod:.4f}  (canonical modulus, tensors)")
print(f"  c_BLV    = {c_BLV:.4f}  (BLV fabric, scalar perturbations)")
print(f"  c_BA     = {c_BA_fold:.4f}  (Anderson-Bogoliubov, BCS condensate)")
print(f"  c_L      = [{c_Leggett_range[0]:.3f}, {c_Leggett_range[1]:.3f}]  (Leggett, DM sector)")
print(f"  c_L_mid  = {c_Leggett_mid:.4f}  (geometric mean)")
print(f"\nINPUT: Leggett collective modes (RPA)")
print(f"  omega_L1 = {omega_L1:.5f} M_KK, Gamma_L1 = {Gamma_L1:.5e} M_KK")
print(f"  omega_L2 = {omega_L2:.5f} M_KK, Gamma_L2 = {Gamma_L2:.5e} M_KK")
print(f"\nINPUT: Hubble and transit parameters")
print(f"  H_fold   = {H_fold:.2f} M_KK")
print(f"  epsilon_H = {epsilon_H:.5f}")

# =============================================================================
# Section 2: Acoustic Impedances
# =============================================================================
print(f"\n{'='*78}")
print("Section 2: Acoustic Impedances")
print(f"{'='*78}")

# Acoustic impedance Z = rho * c_s
# In the spectral action framework, the "density" for each channel is determined
# by the spectral weight participating in that mode.
#
# For BLV: rho_BLV = d2S/dtau2 (the spectral action curvature acts as the
#   effective inertia for modulus fluctuations)
# For BA: rho_BA comes from the BCS sector. The effective density is the
#   superfluid density n_s * m_eff = 2*|E_cond|*N_dof / c_BA^2
# For Leggett: rho_L = inter-band coupling J_23 / c_L^2
#
# However, for impedance MATCHING, what matters is the ratio of impedances,
# not their absolute values. The reflection coefficient depends only on
# Z_1/Z_2 = (rho_1 * c_1) / (rho_2 * c_2).

# Method 1: Direct ratio from sound speeds and spectral weights
# The BLV mode is driven by the spectral action S(tau). Its "impedance" is:
#   Z_BLV = sqrt(Z_spectral * d2S/dtau2)
# where Z_spectral = sum_n (dlambda_n/dtau)^2 / (4|lambda_n|) is the
# gradient stiffness. But c_BLV^2 = Z_spectral / d2S, so:
#   Z_BLV = d2S * c_BLV = d2S/dtau2 * sqrt(Z_spectral / d2S) = sqrt(Z_spectral * d2S)

Z_BLV_eff = np.sqrt(Z_fold * d2S_fold)  # sqrt(spectral stiffness * curvature)
print(f"\n  Z_BLV_eff = sqrt(Z_fold * d2S_fold) = sqrt({Z_fold:.1f} * {d2S_fold:.1f})")
print(f"           = {Z_BLV_eff:.2f} M_KK^2")

# For the BA channel, the effective impedance is:
#   Z_BA = n_s * c_BA where n_s is the superfluid density
# n_s = 2*|E_cond|*N_dof / c_BA^2 (from BCS theory)
n_s_BCS = 2.0 * abs(E_cond) * N_dof_BCS / c_BA_fold**2
Z_BA_eff = n_s_BCS * c_BA_fold
print(f"\n  n_s(BCS)  = 2*|E_cond|*N_dof / c_BA^2 = {n_s_BCS:.4f}")
print(f"  Z_BA_eff  = n_s * c_BA = {Z_BA_eff:.4f} M_KK^2")

# For the Leggett channel:
#   Z_L = rho_L * c_L where rho_L ~ J_23 / c_L^2
# J_23 is the inter-band Josephson coupling
J_23 = float(d_rpa['J_23'])
rho_L = J_23 / c_Leggett_mid**2
Z_L_eff = rho_L * c_Leggett_mid
print(f"\n  J_23      = {J_23:.6f} M_KK")
print(f"  rho_L     = J_23 / c_L^2 = {rho_L:.4f}")
print(f"  Z_L_eff   = rho_L * c_L = {Z_L_eff:.4f} M_KK^2")

# For the modulus channel:
#   Z_mod = G_DeWitt * c_mod = G_DeWitt (since c_mod = 1)
Z_mod_eff = G_DeWitt * c_mod
print(f"\n  Z_mod_eff = G_DeWitt * c_mod = {Z_mod_eff:.4f} M_KK^2")

# IMPEDANCE RATIOS (the physically meaningful quantities)
ratio_BLV_BA = Z_BLV_eff / Z_BA_eff
ratio_BA_L = Z_BA_eff / Z_L_eff
ratio_mod_BLV = Z_mod_eff / Z_BLV_eff

print(f"\n  Z_BLV / Z_BA    = {ratio_BLV_BA:.2f}")
print(f"  Z_BA  / Z_L     = {ratio_BA_L:.2f}")
print(f"  Z_mod / Z_BLV   = {ratio_mod_BLV:.4f}")

# =============================================================================
# Section 3: Reflection Coefficients at Each Interface
# =============================================================================
print(f"\n{'='*78}")
print("Section 3: Reflection Coefficients")
print(f"{'='*78}")

# Interface 1: mod -> BLV
r_mod_BLV = (Z_mod_eff - Z_BLV_eff) / (Z_mod_eff + Z_BLV_eff)
R_mod_BLV = r_mod_BLV**2

# Interface 2: BLV -> BA
r_BLV_BA = (Z_BLV_eff - Z_BA_eff) / (Z_BLV_eff + Z_BA_eff)
R_BLV_BA = r_BLV_BA**2

# Interface 3: BA -> Leggett
r_BA_L = (Z_BA_eff - Z_L_eff) / (Z_BA_eff + Z_L_eff)
R_BA_L = r_BA_L**2

print(f"\n  Interface mod|BLV:  r = {r_mod_BLV:.6f},  R = |r|^2 = {R_mod_BLV:.6f}")
print(f"  Interface BLV|BA:   r = {r_BLV_BA:.6f},  R = |r|^2 = {R_BLV_BA:.6f}")
print(f"  Interface BA|L:     r = {r_BA_L:.6f},  R = |r|^2 = {R_BA_L:.6f}")

# The BLV-BA interface is where the CMB-relevant standing waves form.
# The mod|BLV interface is nearly perfectly reflecting (Z_mod >> Z_BLV),
# and BA|L is also highly reflecting.
#
# Fresnel-like coefficients for AMPLITUDE reflection:
Gamma_BLV_BA = abs(r_BLV_BA)  # amplitude reflection coefficient
Gamma_BA_L = abs(r_BA_L)
Gamma_mod_BLV = abs(r_mod_BLV)

print(f"\n  Gamma_BLV_BA = {Gamma_BLV_BA:.6f}  (BLV -> BA amplitude reflection)")
print(f"  Gamma_BA_L   = {Gamma_BA_L:.6f}  (BA -> L amplitude reflection)")
print(f"  Gamma_mod_BLV = {Gamma_mod_BLV:.6f}  (mod -> BLV amplitude reflection)")

# =============================================================================
# Section 4: Fabry-Perot Cavity Analysis — BLV Layer as Resonator
# =============================================================================
print(f"\n{'='*78}")
print("Section 4: Fabry-Perot Cavity — BLV Layer Between mod and BA")
print(f"{'='*78}")

# The primary cavity is the BLV layer, bounded by:
#   - Left:  mod|BLV interface (nearly total reflection)
#   - Right: BLV|BA interface (partial reflection)
#
# A secondary cavity is the BA layer, bounded by:
#   - Left:  BLV|BA interface
#   - Right: BA|L interface (strong reflection)
#
# Cavity "length" in natural units: L ~ c / H
# The Hubble scale sets the largest resonant wavelength.
# For the BLV cavity: L_BLV = c_BLV / H_fold
# For the BA cavity:  L_BA = c_BA / H_fold
#
# But we also have the coherence length xi_BCS as a scale.
# And for the Josephson-coupled fabric: L_fabric = diameter * lattice_spacing
# where diameter = 6 (graph diameter of 32-cell tessellation).

L_BLV_Hubble = c_BLV / H_fold
L_BA_Hubble = c_BA_fold / H_fold
L_BLV_xi = xi_BCS  # BCS coherence length sets the sub-Hubble cavity

print(f"\n  Hubble length: H_fold^-1 = {1.0/H_fold:.6f} M_KK^-1")
print(f"  BLV Hubble cavity:  L_BLV = c_BLV / H = {L_BLV_Hubble:.6f} M_KK^-1")
print(f"  BA Hubble cavity:   L_BA  = c_BA / H = {L_BA_Hubble:.6f} M_KK^-1")
print(f"  BCS coherence:      xi_BCS = {xi_BCS:.4f} M_KK^-1")

# The physical cavity length that matters for CMB-relevant modes is
# the Hubble crossing scale at the fold. This is L ~ c / H.
# Modes with wavelength lambda > L_Hubble are super-Hubble and frozen.
# Modes with lambda < L_Hubble are sub-Hubble and can form standing waves.

# CAVITY 1: BLV layer (dominant for scalar perturbations)
# Finesse of the BLV cavity (bounded by mod|BLV and BLV|BA interfaces)
R1_BLV = R_mod_BLV  # left mirror
R2_BLV = R_BLV_BA   # right mirror
F_BLV = PI * np.sqrt(np.sqrt(R1_BLV * R2_BLV)) / (1.0 - np.sqrt(R1_BLV * R2_BLV))
Q_BLV = F_BLV / (2.0 * PI) if F_BLV > 0 else 0.0

print(f"\n  CAVITY 1: BLV layer (mod|BLV <-> BLV|BA)")
print(f"    R_left  = {R1_BLV:.6f} (mod|BLV)")
print(f"    R_right = {R2_BLV:.6f} (BLV|BA)")
print(f"    Finesse = {F_BLV:.4f}")
print(f"    Q_cav   = {Q_BLV:.4f}")

# CAVITY 2: BA layer (bounded by BLV|BA and BA|L interfaces)
R1_BA = R_BLV_BA  # left mirror (from BA side: same |r|)
R2_BA = R_BA_L    # right mirror
F_BA = PI * np.sqrt(np.sqrt(R1_BA * R2_BA)) / (1.0 - np.sqrt(R1_BA * R2_BA))
Q_BA = F_BA / (2.0 * PI) if F_BA > 0 else 0.0

print(f"\n  CAVITY 2: BA layer (BLV|BA <-> BA|L)")
print(f"    R_left  = {R1_BA:.6f} (BLV|BA from BA side)")
print(f"    R_right = {R2_BA:.6f} (BA|L)")
print(f"    Finesse = {F_BA:.4f}")
print(f"    Q_cav   = {Q_BA:.4f}")

# =============================================================================
# Section 5: Transfer Matrix for Full Three-Layer System
# =============================================================================
print(f"\n{'='*78}")
print("Section 5: Transfer Matrix — Full Three-Layer Stack")
print(f"{'='*78}")

# The transfer matrix method: for a layer of thickness d with impedance Z
# and wavenumber k = omega/c, the 2x2 transfer matrix is:
#
#   M = [[cos(kd),     (i/Z)*sin(kd)],
#        [i*Z*sin(kd), cos(kd)       ]]
#
# The total transfer matrix for the stack is M_total = M1 * M2 * M3
# (one matrix per layer).
#
# Transmission: |t|^2 = 1 / |M_total[0,0]|^2  (for matched external media)
# More generally: t = 2*Z_out / (M_11*Z_out + M_12 + M_21*Z_out^2 + M_22*Z_out)

def transfer_matrix(omega, c, Z, d):
    """2x2 transfer matrix for a single acoustic layer.

    Parameters:
        omega: angular frequency (M_KK)
        c: sound speed (dimensionless)
        Z: acoustic impedance (M_KK^2)
        d: layer thickness (M_KK^{-1})

    Returns:
        2x2 complex matrix
    """
    k = omega / c
    phi = k * d
    cos_phi = np.cos(phi)
    sin_phi = np.sin(phi)
    M = np.array([
        [cos_phi, 1j * sin_phi / Z],
        [1j * Z * sin_phi, cos_phi]
    ], dtype=complex)
    return M

def transmission_coefficient(M_total, Z_in, Z_out):
    """Compute transmission through a transfer matrix stack.

    T = |2 * Z_out / (M_11 * Z_out + M_12 + M_21 * Z_in * Z_out + M_22 * Z_in)|^2
    """
    M11, M12 = M_total[0, 0], M_total[0, 1]
    M21, M22 = M_total[1, 0], M_total[1, 1]
    denom = M11 * Z_out + M12 + M21 * Z_in * Z_out + M22 * Z_in
    t = 2.0 * np.sqrt(Z_in * Z_out) / denom
    return np.abs(t)**2

# Set cavity length scales.
# The Hubble scale at the fold determines the largest resonance.
# We use the BA layer thickness as L_BA = c_BA / H and BLV layer as L_BLV = c_BLV / H.
#
# The KEY insight: during transit, the modulus sweeps through tau = 0 to tau_fold.
# Perturbations generated at each tau have wavelengths set by the Hubble
# crossing condition: k = aH. The cavity for these perturbations is the
# co-moving Hubble volume.
#
# For the standing wave analysis, we use L as the co-moving size of each
# acoustic channel at the fold. The physical size in units of M_KK^{-1} is:
#   L_i = c_i / H_fold

L_BLV_cav = c_BLV / H_fold      # BLV cavity size
L_BA_cav = c_BA_fold / H_fold   # BA cavity size

print(f"\n  Cavity lengths (co-moving Hubble scale):")
print(f"    L_BLV = c_BLV / H = {L_BLV_cav:.6e} M_KK^-1")
print(f"    L_BA  = c_BA / H  = {L_BA_cav:.6e} M_KK^-1")

# Scan over frequency range: from H (largest scale) to 1000*H (sub-Hubble)
N_omega = 5000  # (local)
omega_min = 0.1 * H_fold
omega_max = 200.0 * H_fold
omega_scan = np.linspace(omega_min, omega_max, N_omega)

# Compute transmission through the BLV-BA two-cavity stack
# Stack: [mod medium] | BLV layer (thickness L_BLV) | BA layer (thickness L_BA) | [L medium]
T_scan = np.zeros(N_omega)

for i, omega in enumerate(omega_scan):
    M_BLV = transfer_matrix(omega, c_BLV, Z_BLV_eff, L_BLV_cav)
    M_BA = transfer_matrix(omega, c_BA_fold, Z_BA_eff, L_BA_cav)
    M_total = M_BLV @ M_BA
    T_scan[i] = transmission_coefficient(M_total, Z_mod_eff, Z_L_eff)

# Find resonance peaks
peaks_idx, properties = find_peaks(T_scan, height=0.01, prominence=0.005)
omega_resonances = omega_scan[peaks_idx]
T_resonances = T_scan[peaks_idx]

print(f"\n  Frequency scan: [{omega_min/H_fold:.1f}, {omega_max/H_fold:.1f}] * H_fold")
print(f"  Number of resonance peaks found: {len(peaks_idx)}")
print(f"  Transmission range: [{T_scan.min():.6e}, {T_scan.max():.6e}]")

if len(peaks_idx) > 0:
    print(f"\n  First 10 resonances:")
    print(f"  {'n':>4s}  {'omega/H':>10s}  {'omega (M_KK)':>14s}  {'T_peak':>10s}  {'Enhancement':>12s}")
    print(f"  {'-'*54}")
    T_baseline = np.median(T_scan)
    for j in range(min(10, len(peaks_idx))):
        idx = peaks_idx[j]
        enh = T_scan[idx] / T_baseline if T_baseline > 0 else np.inf
        print(f"  {j+1:4d}  {omega_scan[idx]/H_fold:10.3f}  "
              f"{omega_scan[idx]:14.4f}  {T_scan[idx]:10.6f}  {enh:12.4f}x")

# =============================================================================
# Section 6: Resonance Analysis — Free Spectral Range and Finesse
# =============================================================================
print(f"\n{'='*78}")
print("Section 6: Resonance Analysis — FSR, Finesse, Q-factors")
print(f"{'='*78}")

# Free spectral range (FSR) = c / (2*L) for each cavity
FSR_BLV = PI * c_BLV / L_BLV_cav  # = pi * H_fold
FSR_BA = PI * c_BA_fold / L_BA_cav   # = pi * H_fold
# Both FSR = pi * H because L = c/H, so c/(2L) = H/2, FSR = pi * H

print(f"\n  Free spectral range:")
print(f"    FSR_BLV = pi * c_BLV / L_BLV = {FSR_BLV:.4f} M_KK = {FSR_BLV/H_fold:.4f} * H")
print(f"    FSR_BA  = pi * c_BA / L_BA   = {FSR_BA:.4f} M_KK  = {FSR_BA/H_fold:.4f} * H")
print(f"    (Both equal pi*H because L = c/H)")

# Compute per-resonance Q factors from the peak widths
Q_resonances = np.zeros(len(peaks_idx))
gamma_resonances = np.zeros(len(peaks_idx))

for j in range(len(peaks_idx)):
    idx = peaks_idx[j]
    omega_r = omega_scan[idx]
    T_peak = T_scan[idx]
    T_half = T_peak / 2.0

    # Find half-maximum width by searching left and right
    # Left side
    left_bound = max(0, idx - 500)
    left_idx = idx
    for k in range(idx - 1, left_bound, -1):
        if T_scan[k] < T_half:
            left_idx = k
            break

    # Right side
    right_bound = min(N_omega - 1, idx + 500)
    right_idx = idx
    for k in range(idx + 1, right_bound):
        if T_scan[k] < T_half:
            right_idx = k
            break

    if left_idx < idx and right_idx > idx:
        delta_omega = omega_scan[right_idx] - omega_scan[left_idx]
        gamma_resonances[j] = delta_omega / 2.0
        Q_resonances[j] = omega_r / delta_omega if delta_omega > 0 else 0
    else:
        gamma_resonances[j] = omega_scan[1] - omega_scan[0]  # resolution-limited
        Q_resonances[j] = omega_r / (2 * gamma_resonances[j])

if len(peaks_idx) > 0:
    print(f"\n  Resonance Q-factors (first 10):")
    print(f"  {'n':>4s}  {'omega/H':>10s}  {'Q':>10s}  {'gamma/H':>10s}")
    print(f"  {'-'*38}")
    for j in range(min(10, len(peaks_idx))):
        print(f"  {j+1:4d}  {omega_resonances[j]/H_fold:10.3f}  "
              f"{Q_resonances[j]:10.3f}  {gamma_resonances[j]/H_fold:10.4f}")

# =============================================================================
# Section 7: A_s Modulation from Standing Waves
# =============================================================================
print(f"\n{'='*78}")
print("Section 7: A_s Modulation from Standing Wave Resonances")
print(f"{'='*78}")

# The primordial power spectrum is modified by the transmission function.
# In standard slow-roll, A_s is uniform. Standing waves modulate it:
#   P(k) = A_s * (k/k_*)^{n_s - 1} * T_FP(k)
# where T_FP(k) is the Fabry-Perot transmission evaluated at omega = c_s * k.
#
# The CMB-relevant wavenumber range is k ~ [0.001, 0.3] Mpc^{-1}.
# At the fold, the physical wavenumber in M_KK units is:
#   k_phys = k_CMB * (M_KK / H_fold) ~ extremely large
# But what matters is the ratio k/k_* where k_* = a*H at Hubble crossing.
#
# The standing wave pattern is periodic with period FSR in omega.
# The CMB observes a finite number of oscillation periods within its window.

# Method: compute the AVERAGE and VARIANCE of T(omega) across the scan
T_mean = np.mean(T_scan)
T_var = np.var(T_scan)
T_rms = np.sqrt(T_var)

# The A_s modulation is the fractional variation in transmission:
delta_As_over_As = T_rms / T_mean if T_mean > 0 else 0

print(f"\n  Transmission statistics:")
print(f"    <T>         = {T_mean:.6e}")
print(f"    Var(T)      = {T_var:.6e}")
print(f"    sigma(T)    = {T_rms:.6e}")
print(f"    delta A_s / A_s = sigma(T) / <T> = {delta_As_over_As:.6f}")

# For specific CMB multipoles: ell ~ k * D_A where D_A is angular diameter distance
# The ratio omega/H determines the multipole moment:
#   ell ~ omega / H * (pi / theta_*) where theta_* ~ 1 degree
# So omega/H ~ 1 corresponds to the acoustic horizon (ell ~ 200)
# omega/H ~ 100 corresponds to damping tail (ell ~ 20000)

# Compute A_s modulation in the CMB-relevant band
# ell ~ 2 to 2500 corresponds to omega/H ~ 0.01 to 12.5
omega_CMB_min = 0.5 * H_fold    # ell ~ 100
omega_CMB_max = 15.0 * H_fold   # ell ~ 3000
CMB_mask = (omega_scan >= omega_CMB_min) & (omega_scan <= omega_CMB_max)

if np.sum(CMB_mask) > 10:
    T_CMB_band = T_scan[CMB_mask]
    T_CMB_mean = np.mean(T_CMB_band)
    T_CMB_rms = np.std(T_CMB_band)
    delta_As_CMB = T_CMB_rms / T_CMB_mean if T_CMB_mean > 0 else 0

    print(f"\n  CMB-relevant band (omega/H in [{omega_CMB_min/H_fold:.1f}, {omega_CMB_max/H_fold:.1f}]):")
    print(f"    <T>_CMB       = {T_CMB_mean:.6e}")
    print(f"    sigma(T)_CMB  = {T_CMB_rms:.6e}")
    print(f"    delta A_s / A_s (CMB) = {delta_As_CMB:.6f}")

    # Count resonances in CMB band
    n_res_CMB = np.sum((omega_resonances >= omega_CMB_min) & (omega_resonances <= omega_CMB_max))
    print(f"    Resonances in CMB band: {n_res_CMB}")
else:
    delta_As_CMB = 0
    n_res_CMB = 0
    T_CMB_mean = T_mean
    print(f"\n  WARNING: Too few points in CMB band. Using full-range statistics.")

# =============================================================================
# Section 8: Also compute with BCS coherence length as cavity scale
# =============================================================================
print(f"\n{'='*78}")
print("Section 8: Alternative Cavity Scale — BCS Coherence Length")
print(f"{'='*78}")

# The Hubble scale gives L ~ 10^{-3} M_KK^{-1}, which is very small.
# The BCS coherence length xi_BCS = 0.808 M_KK^{-1} is much larger and
# represents the scale over which the condensate is coherent.
# Perturbations with lambda < xi_BCS see the condensate structure.

L_alt_BLV = xi_BCS * c_BLV / c_BA_fold  # scaled by speed ratio
L_alt_BA = xi_BCS

print(f"\n  BCS coherence length: xi_BCS = {xi_BCS:.4f} M_KK^-1")
print(f"  Alternative BLV cavity: L = {L_alt_BLV:.4f} M_KK^-1")
print(f"  Alternative BA cavity:  L = {L_alt_BA:.4f} M_KK^-1")

# Scan at this scale
omega_alt_min = 0.01  # (local)
omega_alt_max = 20.0   # up to 20 M_KK  # (local)
N_alt = 5000
omega_alt = np.linspace(omega_alt_min, omega_alt_max, N_alt)
T_alt = np.zeros(N_alt)

for i, omega in enumerate(omega_alt):
    M_BLV = transfer_matrix(omega, c_BLV, Z_BLV_eff, L_alt_BLV)
    M_BA = transfer_matrix(omega, c_BA_fold, Z_BA_eff, L_alt_BA)
    M_total = M_BLV @ M_BA
    T_alt[i] = transmission_coefficient(M_total, Z_mod_eff, Z_L_eff)

peaks_alt, _ = find_peaks(T_alt, height=0.01, prominence=0.005)
omega_alt_res = omega_alt[peaks_alt]
T_alt_res = T_alt[peaks_alt]

T_alt_mean = np.mean(T_alt)
T_alt_rms = np.std(T_alt)
delta_As_alt = T_alt_rms / T_alt_mean if T_alt_mean > 0 else 0

FSR_alt_BLV = PI * c_BLV / L_alt_BLV
FSR_alt_BA = PI * c_BA_fold / L_alt_BA

print(f"\n  FSR_BLV (xi scale) = {FSR_alt_BLV:.4f} M_KK")
print(f"  FSR_BA  (xi scale) = {FSR_alt_BA:.4f} M_KK")
print(f"  Resonance peaks found: {len(peaks_alt)}")
print(f"  <T>_alt = {T_alt_mean:.6e}")
print(f"  delta A_s / A_s (xi scale) = {delta_As_alt:.6f}")

if len(peaks_alt) > 0:
    print(f"\n  First 10 resonances at xi scale:")
    print(f"  {'n':>4s}  {'omega (M_KK)':>14s}  {'T_peak':>10s}")
    print(f"  {'-'*30}")
    for j in range(min(10, len(peaks_alt))):
        print(f"  {j+1:4d}  {omega_alt_res[j]:14.6f}  {T_alt_res[j]:10.6f}")

# =============================================================================
# Section 9: Damped Standing Waves — Include Leggett and BA Linewidths
# =============================================================================
print(f"\n{'='*78}")
print("Section 9: Damped Resonances — Including Collective Linewidths")
print(f"{'='*78}")

# In a real physical system, each acoustic channel has finite damping.
# This adds an imaginary part to the wavenumber: k -> k + i*gamma/(2*c)
# The transfer matrix becomes:
#   phi = (omega + i*Gamma/2) * d / c  (complex phase)
#
# BLV damping: The BLV mode is a spectral action perturbation. Its damping
# comes from the one-loop corrections (S62 Hessian showed Q_eff ~ 1.9).
# We use Gamma_BLV ~ H_fold (Hubble damping) as the dominant channel.
#
# BA damping: The Anderson-Bogoliubov mode Gamma ~ Landau 3-phonon.
# From S65 Leggett RPA: Gamma_Landau = 4.68e-3 M_KK.
#
# Leggett damping: Gamma_L1 = 4.86e-3 M_KK (RPA result).

Gamma_Landau = float(d_rpa['Gamma_Landau'])
Gamma_BLV_damp = H_fold  # Hubble damping for moduli perturbations
Gamma_BA_damp = Gamma_Landau   # Landau 3-phonon for BA mode
Gamma_L_damp = Gamma_L1        # Leggett RPA damping

print(f"\n  Damping rates:")
print(f"    Gamma_BLV   = {Gamma_BLV_damp:.4f} M_KK (Hubble friction)")
print(f"    Gamma_BA    = {Gamma_BA_damp:.6f} M_KK (Landau 3-phonon)")
print(f"    Gamma_L     = {Gamma_L_damp:.6f} M_KK (Leggett RPA)")

def transfer_matrix_damped(omega, c, Z, d, Gamma):
    """Transfer matrix with complex wavenumber (damped)."""
    k_complex = omega / c + 1j * Gamma / (2.0 * c)
    phi = k_complex * d
    cos_phi = np.cos(phi)
    sin_phi = np.sin(phi)
    M = np.array([
        [cos_phi, 1j * sin_phi / Z],
        [1j * Z * sin_phi, cos_phi]
    ], dtype=complex)
    return M

# Compute damped transmission (Hubble scale cavity)
T_damped = np.zeros(N_omega)
for i, omega in enumerate(omega_scan):
    M_BLV = transfer_matrix_damped(omega, c_BLV, Z_BLV_eff, L_BLV_cav, Gamma_BLV_damp)
    M_BA = transfer_matrix_damped(omega, c_BA_fold, Z_BA_eff, L_BA_cav, Gamma_BA_damp)
    M_total = M_BLV @ M_BA
    T_damped[i] = transmission_coefficient(M_total, Z_mod_eff, Z_L_eff)

peaks_damped, _ = find_peaks(T_damped, height=0.001, prominence=0.001)

T_damped_mean = np.mean(T_damped)
T_damped_rms = np.std(T_damped)
delta_As_damped = T_damped_rms / T_damped_mean if T_damped_mean > 0 else 0

print(f"\n  Damped transmission (Hubble cavity):")
print(f"    <T>_damped = {T_damped_mean:.6e}")
print(f"    sigma(T)_damped = {T_damped_rms:.6e}")
print(f"    delta A_s / A_s (damped) = {delta_As_damped:.6f}")
print(f"    Resonance peaks: {len(peaks_damped)}")

# =============================================================================
# Section 10: Direct Reflection Coefficient — Dimensionless
# =============================================================================
print(f"\n{'='*78}")
print("Section 10: Dimensionless Reflection Coefficients from Sound Speed Ratios")
print(f"{'='*78}")

# The fundamental dimensionless quantity is the sound speed ratio.
# For two channels with equal density (same spectral action generating both),
# the reflection coefficient depends ONLY on the speed ratio:
#   r = (c_1 - c_2) / (c_1 + c_2)
# This is the simplest and most robust estimate.

r_pure_BLV_BA = (c_BLV - c_BA_fold) / (c_BLV + c_BA_fold)
R_pure_BLV_BA = r_pure_BLV_BA**2
r_pure_BA_L = (c_BA_fold - c_Leggett_mid) / (c_BA_fold + c_Leggett_mid)
R_pure_BA_L = r_pure_BA_L**2
r_pure_mod_BLV = (c_mod - c_BLV) / (c_mod + c_BLV)
R_pure_mod_BLV = r_pure_mod_BLV**2

print(f"\n  Pure speed-ratio reflection (equal density):")
print(f"    r(BLV|BA)  = ({c_BLV:.3f} - {c_BA_fold:.3f}) / ({c_BLV:.3f} + {c_BA_fold:.3f}) = {r_pure_BLV_BA:.6f}")
print(f"    R(BLV|BA)  = {R_pure_BLV_BA:.6f}")
print(f"    r(BA|L)    = ({c_BA_fold:.3f} - {c_Leggett_mid:.3f}) / ({c_BA_fold:.3f} + {c_Leggett_mid:.3f}) = {r_pure_BA_L:.6f}")
print(f"    R(BA|L)    = {R_pure_BA_L:.6f}")
print(f"    r(mod|BLV) = ({c_mod:.3f} - {c_BLV:.3f}) / ({c_mod:.3f} + {c_BLV:.3f}) = {r_pure_mod_BLV:.6f}")
print(f"    R(mod|BLV) = {R_pure_mod_BLV:.6f}")

# Fabry-Perot finesse from pure speed ratios
# For the BA cavity between BLV and L:
r_eff_product = np.sqrt(R_pure_BLV_BA * R_pure_BA_L)
F_pure = PI * np.sqrt(r_eff_product) / (1.0 - r_eff_product)
Q_pure = F_pure / (2.0 * PI)

print(f"\n  BA cavity finesse (pure speed ratios):")
print(f"    sqrt(R1*R2) = {r_eff_product:.6f}")
print(f"    Finesse     = {F_pure:.6f}")
print(f"    Q_cavity    = {Q_pure:.6f}")

# For the BLV cavity between mod and BA:
r_eff_BLV = np.sqrt(R_pure_mod_BLV * R_pure_BLV_BA)
F_pure_BLV = PI * np.sqrt(r_eff_BLV) / (1.0 - r_eff_BLV)
Q_pure_BLV = F_pure_BLV / (2.0 * PI)

print(f"\n  BLV cavity finesse (pure speed ratios):")
print(f"    sqrt(R1*R2) = {r_eff_BLV:.6f}")
print(f"    Finesse     = {F_pure_BLV:.6f}")
print(f"    Q_cavity    = {Q_pure_BLV:.6f}")

# A_s modulation from cavity Q:
# At resonance, enhancement = 1/(1-R1*R2)
# Off-resonance, suppression = (1-R1*R2)
# The RMS modulation is approximately:
#   delta A_s / A_s ~ (R1*R2) / (1 - R1*R2)^2 * sin^2 contribution averaged

# For BA cavity (speed ratios only):
T_max_BA = 1.0 / (1.0 - r_eff_product)**2
T_min_BA = 1.0 / (1.0 + r_eff_product / (1.0 - r_eff_product))**2 if r_eff_product < 1 else 0
delta_T_BA = (T_max_BA - T_min_BA)  # / T_mean ~ delta_As/As

print(f"\n  Enhancement at resonance (BA cavity):")
print(f"    T_max / T_min = {T_max_BA:.6f}")
print(f"    delta T = {delta_T_BA:.6f}")

# For BLV cavity:
T_max_BLV = 1.0 / (1.0 - r_eff_BLV)**2
delta_T_BLV = T_max_BLV - 1.0

print(f"\n  Enhancement at resonance (BLV cavity):")
print(f"    T_max = {T_max_BLV:.6f}")
print(f"    delta T = {delta_T_BLV:.6f}")

# =============================================================================
# Section 11: Scan with Pure Speed-Ratio Impedances
# =============================================================================
print(f"\n{'='*78}")
print("Section 11: Transfer Matrix with Pure Speed-Ratio Impedances")
print(f"{'='*78}")

# Use Z_i = c_i (impedance proportional to sound speed, equal density)
# This is the most conservative estimate — no density contrast amplification.
Z_mod_pure = c_mod
Z_BLV_pure = c_BLV
Z_BA_pure = c_BA_fold
Z_L_pure = c_Leggett_mid

T_pure_scan = np.zeros(N_omega)
for i, omega in enumerate(omega_scan):
    M_BLV = transfer_matrix(omega, c_BLV, Z_BLV_pure, L_BLV_cav)
    M_BA = transfer_matrix(omega, c_BA_fold, Z_BA_pure, L_BA_cav)
    M_total = M_BLV @ M_BA
    T_pure_scan[i] = transmission_coefficient(M_total, Z_mod_pure, Z_L_pure)

peaks_pure, _ = find_peaks(T_pure_scan, height=0.01, prominence=0.005)

T_pure_mean = np.mean(T_pure_scan)
T_pure_rms = np.std(T_pure_scan)
delta_As_pure = T_pure_rms / T_pure_mean if T_pure_mean > 0 else 0

print(f"\n  Pure speed-ratio transmission (Hubble cavity):")
print(f"    <T> = {T_pure_mean:.6e}")
print(f"    sigma(T) = {T_pure_rms:.6e}")
print(f"    delta A_s / A_s = {delta_As_pure:.6f}")
print(f"    Number of resonance peaks: {len(peaks_pure)}")

# Scan with xi_BCS cavity scale
T_pure_xi = np.zeros(N_alt)
for i, omega in enumerate(omega_alt):
    M_BLV = transfer_matrix(omega, c_BLV, Z_BLV_pure, L_alt_BLV)
    M_BA = transfer_matrix(omega, c_BA_fold, Z_BA_pure, L_alt_BA)
    M_total = M_BLV @ M_BA
    T_pure_xi[i] = transmission_coefficient(M_total, Z_mod_pure, Z_L_pure)

peaks_pure_xi, _ = find_peaks(T_pure_xi, height=0.01, prominence=0.005)

T_pure_xi_mean = np.mean(T_pure_xi)
T_pure_xi_rms = np.std(T_pure_xi)
delta_As_pure_xi = T_pure_xi_rms / T_pure_xi_mean if T_pure_xi_mean > 0 else 0

print(f"\n  Pure speed-ratio transmission (xi_BCS cavity):")
print(f"    <T> = {T_pure_xi_mean:.6e}")
print(f"    sigma(T) = {T_pure_xi_rms:.6e}")
print(f"    delta A_s / A_s = {delta_As_pure_xi:.6f}")
print(f"    Number of resonance peaks: {len(peaks_pure_xi)}")

# =============================================================================
# Section 12: CMB Imprint — Does Any Resonance Fall Within Observed Bands?
# =============================================================================
print(f"\n{'='*78}")
print("Section 12: CMB Imprint Assessment")
print(f"{'='*78}")

# The Leggett modes at omega_L1 = 0.0684, omega_L2 = 0.0952 M_KK are
# specific frequencies. Do they coincide with any cavity resonance?

# At Hubble scale (FSR = pi*H ~ 1842 M_KK): the resonances are at
# omega_n = n * pi * H, so n = omega_L / (pi * H)
n_L1_Hubble = omega_L1 / (PI * H_fold)
n_L2_Hubble = omega_L2 / (PI * H_fold)

print(f"\n  Leggett modes vs Hubble-scale resonances:")
print(f"    omega_L1 / FSR = {n_L1_Hubble:.6e}  (mode index)")
print(f"    omega_L2 / FSR = {n_L2_Hubble:.6e}  (mode index)")
print(f"    Both are << 1: Leggett modes are FAR BELOW the first Hubble-scale resonance")

# At xi_BCS scale (FSR_BA ~ 1.94 M_KK):
n_L1_xi = omega_L1 / FSR_alt_BA
n_L2_xi = omega_L2 / FSR_alt_BA

print(f"\n  Leggett modes vs xi_BCS-scale resonances:")
print(f"    omega_L1 / FSR = {n_L1_xi:.4f}  (fractional mode)")
print(f"    omega_L2 / FSR = {n_L2_xi:.4f}  (fractional mode)")

# The plasma frequency omega_J = 0.715 M_KK (from S56)
omega_J = 0.715  # (local)
n_J_xi = omega_J / FSR_alt_BA

print(f"\n  Josephson plasma frequency vs xi_BCS-scale resonances:")
print(f"    omega_J / FSR = {n_J_xi:.4f}  (mode index)")

# Key physical point: The Fabry-Perot resonances at the Hubble scale
# have FSR ~ pi*H ~ 1842 M_KK. The FIRST resonance is at ~1842 M_KK.
# All our low-energy modes (Leggett, BA, Josephson) are far below this.
#
# At the xi_BCS scale, FSR ~ 1.94 M_KK, and Leggett modes ARE within
# the first few FSR — they can overlap with xi-scale standing waves.
# But these are INTERNAL (sub-Hubble) modes, not CMB-scale perturbations.
#
# Conclusion: The standing wave resonances exist, but their effect on
# A_s at CMB scales depends on whether the cavity finesse is high enough
# to create measurable modulation within the observable window.

print(f"\n  SCALE SEPARATION ANALYSIS:")
print(f"    k_CMB ~ H_fold                  = {H_fold:.2f} M_KK")
print(f"    k_BCS ~ 1/xi_BCS               = {1.0/xi_BCS:.4f} M_KK")
print(f"    k_Leggett ~ omega_L1/c_L        = {omega_L1/c_Leggett_mid:.2f} M_KK")
print(f"    k_Josephson ~ omega_J/c_BA       = {omega_J/c_BA_fold:.4f} M_KK")
print(f"    Ratio k_CMB / k_BCS = {H_fold * xi_BCS:.2f}")
print(f"    The CMB scale is {H_fold * xi_BCS:.0f}x larger than the BCS scale.")
print(f"    Standing wave modulation at CMB frequencies is AVERAGED over")
print(f"    ~{H_fold * xi_BCS:.0f} sub-Hubble oscillations → suppressed by 1/sqrt(N).")

N_subhubble = H_fold * xi_BCS
suppression = 1.0 / np.sqrt(N_subhubble) if N_subhubble > 1 else 1.0

print(f"\n  A_s modulation suppression from averaging:")
print(f"    N_sub-Hubble oscillations ~ {N_subhubble:.1f}")
print(f"    Suppression factor ~ 1/sqrt(N) = {suppression:.4e}")
print(f"    Effective delta A_s / A_s ~ {delta_As_pure * suppression:.4e} (Hubble) or")
print(f"    {delta_As_pure_xi * suppression:.4e} (xi scale, suppressed)")

# =============================================================================
# Section 13: Summary and Gate Verdict
# =============================================================================
print(f"\n{'='*78}")
print("Section 13: IMPEDANCE-65 Gate Verdict")
print(f"{'='*78}")

print(f"""
IMPEDANCE MATCHING SUMMARY
{'='*50}

Four-Speed Acoustic System:
  c_mod = {c_mod:.3f}  |  c_BLV = {c_BLV:.3f}  |  c_BA = {c_BA_fold:.3f}  |  c_L = {c_Leggett_mid:.3f}

Reflection Coefficients (pure speed-ratio):
  R(mod|BLV) = {R_pure_mod_BLV:.4f}  (strong reflection)
  R(BLV|BA)  = {R_pure_BLV_BA:.6f}  (weak reflection — speeds similar)
  R(BA|L)    = {R_pure_BA_L:.4f}  (strong reflection — large speed mismatch)

Cavity Analysis:
  BLV cavity (mod|BLV <-> BLV|BA):  Q = {Q_pure_BLV:.4f}  (very low Q — weak right mirror)
  BA cavity  (BLV|BA <-> BA|L):     Q = {Q_pure:.4f}  (moderate Q — strong right mirror)

Standing Wave Frequencies:
  Hubble scale: FSR = pi*H = {PI*H_fold:.1f} M_KK (first resonance at ~1842 M_KK)
  xi_BCS scale: FSR ~ {FSR_alt_BA:.3f} M_KK (resonances at BCS scale)

A_s Modulation:
  Raw (Hubble cavity):        delta A_s / A_s = {delta_As_pure:.4e}
  Raw (xi_BCS cavity):        delta A_s / A_s = {delta_As_pure_xi:.4e}
  After sub-Hubble averaging: delta A_s / A_s ~ {delta_As_pure_xi * suppression:.4e}

KEY FINDING: The BLV-BA impedance mismatch is WEAK.
  c_BLV/c_BA = {c_BLV/c_BA_fold:.3f} — only a {100*(c_BLV - c_BA_fold)/c_BA_fold:.1f}% speed difference.
  R(BLV|BA) = {R_pure_BLV_BA:.6f} — reflectivity is {R_pure_BLV_BA*100:.2f}%.
  The BA-Leggett mismatch is STRONG (R = {R_pure_BA_L:.4f}), but the
  BLV-BA interface is nearly transparent.

  Standing waves DO form, but with very low finesse at the BLV|BA
  interface. The BA|L interface provides strong confinement of BA-scale
  perturbations, creating an effective waveguide for condensate modes.
  However, the BLV channel (which drives primordial scalar perturbations)
  passes through the BA layer with minimal reflection.

  The A_s modulation from standing waves is negligible at CMB scales.
""")

gate_detail = (
    f"IMPEDANCE-65: INFO. BLV-BA reflection R = {R_pure_BLV_BA:.6f} (weak, "
    f"c_BLV/c_BA = {c_BLV/c_BA_fold:.3f}). BA-L reflection R = {R_pure_BA_L:.4f} "
    f"(strong). BLV cavity Q = {Q_pure_BLV:.4f}, BA cavity Q = {Q_pure:.4f}. "
    f"Standing wave FSR = {PI*H_fold:.1f} M_KK (Hubble) / {FSR_alt_BA:.3f} M_KK (xi). "
    f"A_s modulation: {delta_As_pure:.4e} (Hubble raw), "
    f"{delta_As_pure_xi * suppression:.4e} (xi, averaged). "
    f"NEGLIGIBLE at CMB scales — BLV channel nearly transparent through BA layer."
)

print(f"\nGate: IMPEDANCE-65")
print(f"Verdict: INFO")
print(f"Detail: {gate_detail}")

# =============================================================================
# Section 14: Save Data
# =============================================================================
print(f"\n{'='*78}")
print("Section 14: Saving Data")
print(f"{'='*78}")

out_path = os.path.join(SCRIPT_DIR, 's65_impedance_standing.npz')
np.savez(out_path,
    # Sound speeds
    c_mod=c_mod,
    c_BLV=c_BLV,
    c_BA=c_BA_fold,
    c_L_mid=c_Leggett_mid,
    c_L_range=c_Leggett_range,

    # Impedances (effective)
    Z_mod_eff=Z_mod_eff,
    Z_BLV_eff=Z_BLV_eff,
    Z_BA_eff=Z_BA_eff,
    Z_L_eff=Z_L_eff,

    # Reflection coefficients (impedance-weighted)
    r_mod_BLV=r_mod_BLV,
    r_BLV_BA=r_BLV_BA,
    r_BA_L=r_BA_L,
    R_mod_BLV=R_mod_BLV,
    R_BLV_BA=R_BLV_BA,
    R_BA_L=R_BA_L,

    # Reflection coefficients (pure speed ratio)
    r_pure_BLV_BA=r_pure_BLV_BA,
    r_pure_BA_L=r_pure_BA_L,
    r_pure_mod_BLV=r_pure_mod_BLV,
    R_pure_BLV_BA=R_pure_BLV_BA,
    R_pure_BA_L=R_pure_BA_L,
    R_pure_mod_BLV=R_pure_mod_BLV,

    # Cavity parameters
    L_BLV_Hubble=L_BLV_cav,
    L_BA_Hubble=L_BA_cav,
    L_BLV_xi=L_alt_BLV,
    L_BA_xi=L_alt_BA,
    F_BLV=F_BLV,
    F_BA=F_BA,
    Q_BLV=Q_BLV,
    Q_BA=Q_BA,
    F_pure_BLV=F_pure_BLV,
    F_pure_BA=F_pure,
    Q_pure_BLV=Q_pure_BLV,
    Q_pure_BA=Q_pure,

    # Free spectral ranges
    FSR_Hubble=PI * H_fold,
    FSR_xi_BLV=FSR_alt_BLV,
    FSR_xi_BA=FSR_alt_BA,

    # Transmission scans
    omega_scan_Hubble=omega_scan,
    T_scan_Hubble=T_scan,
    T_damped_Hubble=T_damped,
    T_pure_Hubble=T_pure_scan,
    omega_scan_xi=omega_alt,
    T_scan_xi=T_alt,
    T_pure_xi=T_pure_xi,

    # Resonance peaks (Hubble)
    omega_resonances_Hubble=omega_resonances if len(peaks_idx) > 0 else np.array([]),
    T_resonances_Hubble=T_resonances if len(peaks_idx) > 0 else np.array([]),
    Q_resonances_Hubble=Q_resonances if len(peaks_idx) > 0 else np.array([]),

    # Resonance peaks (xi)
    omega_resonances_xi=omega_alt_res if len(peaks_alt) > 0 else np.array([]),
    T_resonances_xi=T_alt_res if len(peaks_alt) > 0 else np.array([]),

    # A_s modulation
    delta_As_Hubble=delta_As_pure,
    delta_As_xi=delta_As_pure_xi,
    delta_As_CMB=delta_As_CMB,
    delta_As_damped=delta_As_damped,
    delta_As_suppressed=delta_As_pure_xi * suppression,
    suppression_factor=suppression,
    N_subhubble=N_subhubble,

    # Damping rates
    Gamma_BLV_damp=Gamma_BLV_damp,
    Gamma_BA_damp=Gamma_BA_damp,
    Gamma_L_damp=Gamma_L_damp,

    # Gate
    gate_name='IMPEDANCE-65',
    gate_verdict='INFO',
    gate_detail=gate_detail,
)

print(f"  Saved: {out_path}")

# =============================================================================
# Section 15: Plot
# =============================================================================
print(f"\n{'='*78}")
print("Section 15: Generating Plot")
print(f"{'='*78}")

fig = plt.figure(figsize=(16, 14))
gs = GridSpec(3, 2, figure=fig, hspace=0.35, wspace=0.3)

# Panel A: Speed hierarchy bar chart
ax_a = fig.add_subplot(gs[0, 0])
speeds = [c_mod, c_BLV, c_BA_fold, c_Leggett_mid]
labels_speed = ['$c_{\\rm mod}$', '$c_{\\rm BLV}$', '$c_{\\rm BA}$', '$c_L$']
colors_speed = ['#2c3e50', '#3498db', '#e74c3c', '#2ecc71']
bars = ax_a.bar(labels_speed, speeds, color=colors_speed, edgecolor='black', linewidth=0.8)
ax_a.set_ylabel('Sound speed ($c = 1$ units)')
ax_a.set_title('(A) Four-Speed Hierarchy')
ax_a.set_ylim(0, 1.15)
for bar, v in zip(bars, speeds):
    ax_a.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.02,
              f'{v:.3f}', ha='center', fontsize=9)
ax_a.axhline(y=1.0, color='gray', linestyle='--', alpha=0.5, label='$c = 1$')
ax_a.legend(fontsize=8)

# Panel B: Reflection coefficients
ax_b = fig.add_subplot(gs[0, 1])
interfaces = ['mod|BLV', 'BLV|BA', 'BA|L']
R_values = [R_pure_mod_BLV, R_pure_BLV_BA, R_pure_BA_L]
colors_R = ['#8e44ad', '#f39c12', '#1abc9c']
bars_R = ax_b.bar(interfaces, R_values, color=colors_R, edgecolor='black', linewidth=0.8)
ax_b.set_ylabel('Reflectivity $R = |r|^2$')
ax_b.set_title('(B) Interface Reflectivity (pure speed ratio)')
ax_b.set_yscale('log')
ax_b.set_ylim(1e-5, 1.5)
for bar, v in zip(bars_R, R_values):
    ax_b.text(bar.get_x() + bar.get_width()/2, v * 1.5,
              f'{v:.2e}', ha='center', fontsize=8)

# Panel C: Transmission — Hubble cavity (three methods)
ax_c = fig.add_subplot(gs[1, 0])
x_Hubble = omega_scan / H_fold
ax_c.semilogy(x_Hubble, T_pure_scan, 'b-', alpha=0.7, linewidth=0.5, label='Undamped (speed-ratio Z)')
ax_c.semilogy(x_Hubble, T_scan, 'r-', alpha=0.5, linewidth=0.5, label='Undamped (effective Z)')
ax_c.semilogy(x_Hubble, T_damped, 'k-', alpha=0.7, linewidth=0.5, label='Damped')
ax_c.axvspan(omega_CMB_min/H_fold, omega_CMB_max/H_fold, alpha=0.1, color='green', label='CMB band')
ax_c.set_xlabel('$\\omega / H_{\\rm fold}$')
ax_c.set_ylabel('Transmission $|t|^2$')
ax_c.set_title('(C) Fabry-Perot Transmission (Hubble cavity)')
ax_c.legend(fontsize=7, loc='lower right')
ax_c.set_xlim(0, 50)

# Panel D: Transmission — xi_BCS cavity
ax_d = fig.add_subplot(gs[1, 1])
ax_d.semilogy(omega_alt, T_pure_xi, 'b-', alpha=0.7, linewidth=0.5, label='Undamped (speed-ratio Z)')
ax_d.semilogy(omega_alt, T_alt, 'r-', alpha=0.5, linewidth=0.5, label='Undamped (effective Z)')
# Mark Leggett frequencies
ax_d.axvline(omega_L1, color='green', linestyle='--', alpha=0.7, label=f'$\\omega_{{L1}}$ = {omega_L1:.4f}')
ax_d.axvline(omega_L2, color='orange', linestyle='--', alpha=0.7, label=f'$\\omega_{{L2}}$ = {omega_L2:.4f}')
ax_d.axvline(omega_J, color='purple', linestyle='--', alpha=0.7, label=f'$\\omega_J$ = {omega_J:.3f}')
ax_d.set_xlabel('$\\omega$ ($M_{\\rm KK}$ units)')
ax_d.set_ylabel('Transmission $|t|^2$')
ax_d.set_title('(D) Fabry-Perot Transmission ($\\xi_{\\rm BCS}$ cavity)')
ax_d.legend(fontsize=7)

# Panel E: A_s modulation summary
ax_e = fig.add_subplot(gs[2, 0])
methods = ['Hubble\n(eff Z)', 'Hubble\n(speed Z)', 'Hubble\n(damped)',
           'xi_BCS\n(eff Z)', 'xi_BCS\n(speed Z)', 'xi_BCS\n(suppressed)']
delta_vals = [delta_As_over_As, delta_As_pure, delta_As_damped,
              delta_As_alt, delta_As_pure_xi, delta_As_pure_xi * suppression]
colors_delta = ['#e74c3c', '#3498db', '#2c3e50', '#e74c3c', '#3498db', '#2ecc71']
bars_delta = ax_e.bar(methods, delta_vals, color=colors_delta, edgecolor='black', linewidth=0.8)
ax_e.set_ylabel('$\\delta A_s / A_s$')
ax_e.set_title('(E) $A_s$ Modulation Amplitude')
ax_e.set_yscale('log')
# Set lower y-limit sensibly
valid_delta = [v for v in delta_vals if v > 0]
if valid_delta:
    ax_e.set_ylim(min(valid_delta) * 0.1, max(delta_vals) * 5)
ax_e.tick_params(axis='x', rotation=20, labelsize=7)

# Panel F: Schematic of the acoustic cavity structure
ax_f = fig.add_subplot(gs[2, 1])
ax_f.set_xlim(0, 10)
ax_f.set_ylim(0, 10)

# Draw layers
layer_colors = ['#2c3e50', '#3498db', '#e74c3c', '#2ecc71']
layer_labels = ['Modulus\n$c = 1.0$', 'BLV\n$c = 0.485$', 'BA\n$c = 0.399$', 'Leggett\n$c = 0.025$']
x_starts = [0.5, 2.5, 5.0, 7.5]
x_widths = [2.0, 2.5, 2.5, 2.0]

for x0, w, col, lab in zip(x_starts, x_widths, layer_colors, layer_labels):
    rect = plt.Rectangle((x0, 1), w, 7, facecolor=col, alpha=0.3, edgecolor=col, linewidth=2)
    ax_f.add_patch(rect)
    ax_f.text(x0 + w/2, 5, lab, ha='center', va='center', fontsize=9,
              fontweight='bold', color=col)

# Draw reflection arrows at interfaces
interface_x = [2.5, 5.0, 7.5]
R_labels = [f'R = {R_pure_mod_BLV:.3f}', f'R = {R_pure_BLV_BA:.5f}', f'R = {R_pure_BA_L:.3f}']
for x, lab in zip(interface_x, R_labels):
    ax_f.annotate('', xy=(x - 0.3, 8.5), xytext=(x + 0.3, 8.5),
                  arrowprops=dict(arrowstyle='<->', color='red', lw=2))
    ax_f.text(x, 9.2, lab, ha='center', fontsize=8, color='red', fontweight='bold')

ax_f.set_title('(F) Multi-Layer Acoustic Cavity')
ax_f.axis('off')

fig.suptitle('IMPEDANCE-65: BLV-BA Standing Wave Analysis\n'
             'Three-Layer Acoustic Cavity in Four-Speed Hierarchy',
             fontsize=13, fontweight='bold', y=0.98)

plot_path = os.path.join(SCRIPT_DIR, 's65_impedance_standing.png')
fig.savefig(plot_path, dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print(f"  Saved: {plot_path}")

elapsed = time.time() - t_start
print(f"\n  Total runtime: {elapsed:.2f}s")
print(f"\n{'='*78}")
print("IMPEDANCE-65 COMPLETE")
print(f"{'='*78}")
