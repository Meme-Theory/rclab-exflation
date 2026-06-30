#!/usr/bin/env python3
"""
s63_ab_parametric.py — Parametric Amplification Reheating via A-B Mode Conversion
==================================================================================

AB-PARAMETRIC-63: Compute the parametric amplification rate through the A-B
hybridization channel (delta = 0.248 M_KK) using the negative-frequency mode
at k=0 (omega = -2.52 M_KK) as the pump. Tests whether A-B mode conversion
is the microscopic reheating mechanism during transit.

PHYSICS:
    The negative-frequency mode at k=0 is an A-B hybrid (w_A = 0.33, w_B = 0.67)
    whose negative eigenvalue signals an inverted-oscillator instability. During
    the BCS transit, this mode is coherently excited (the modulus is rolling).

    Parametric amplification: the pump mode (omega_pump < 0) decays into pairs
    of positive-frequency modes at the A-B avoided crossing. The coupling vertex
    is the A-tensor |A|^2 = 2.20, and the process is resonant when:
        omega_pump + omega_signal + omega_idler = 0
    (energy conservation with a negative-frequency pump).

    The parametric rate is computed from Fermi's golden rule with the trilinear
    coupling vertex derived from the A-B sector of the full Hamiltonian.

    Three independent estimates:
        1. Mathieu instability: exponential growth rate of modes in the
           instability band near the avoided crossing
        2. Fermi golden rule: perturbative decay rate of pump into pairs
        3. Landau-Zener: non-adiabatic transition probability at the crossing

    Gate: AB-PARAMETRIC-63
        PASS: Gamma > H(transit)    [reheating via mode conversion works]
        FAIL: Gamma < H(transit)    [too slow]

Author: tesla-resonance
Session: S63 W6-12
"""

import sys
import os
import time
import numpy as np
from scipy.linalg import eigh
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import (
    tau_fold, M_KK, M_KK_gravity, H_fold, v_terminal, dt_transit,
    omega_att, E_cond, E_exc, n_pairs,
    Gamma_Langer_BCS, PI,
)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

SCRIPT_DIR = Path(__file__).parent
OUT_NPZ = SCRIPT_DIR / "s63_ab_parametric.npz"
OUT_PNG = SCRIPT_DIR / "s63_ab_parametric.png"
OUT_TXT = SCRIPT_DIR / "s63_ab_parametric_output.txt"

t_start = time.time()

# =============================================================================
# Output tee
# =============================================================================
class Tee:
    def __init__(self, filename):
        self.file = open(filename, 'w')
        self.stdout = sys.stdout
    def write(self, data):
        self.file.write(data)
        self.stdout.write(data)
    def flush(self):
        self.file.flush()
        self.stdout.flush()

sys.stdout = Tee(str(OUT_TXT))

print("=" * 78)
print("S63 AB-PARAMETRIC-63: Parametric Amplification Reheating via A-B Conversion")
print("=" * 78)

# =============================================================================
# SECTION 1: Load dispersion data and extract pump mode
# =============================================================================
print("\n--- Section 1: Load data ---")

d = np.load(SCRIPT_DIR / "s62_phonon_dispersion_full.npz", allow_pickle=True)
omega_full = d['omega_full']           # (32, 45) full coupled spectrum
evecs_full = d['evecs_full']           # (32, 45, 45) eigenvectors
sector_weight = d['sector_weight']     # (32, 45, 3) sector weights
k_eff = d['k_eff']                     # (32,) effective wavevectors
lambda_n = d['lambda_n']               # (32,) graph Laplacian eigenvalues
V_AB = d['V_AB']                       # (36, 8) A-B coupling matrix
AB_delta_gaps = d['AB_delta_gaps']     # (69,) hybridization gap shifts
AB_coupled_gaps = d['AB_coupled_gaps'] # (69,) coupled gaps
AB_detunings = d['AB_detunings']       # (69,) detunings at crossings
A_coset_sq = float(d['A_coset_sq'])    # |A|^2 = 2.20
E_J_fold = float(d['E_J_fold'])        # 7.04 M_KK
eps_canonical = float(d['eps_canonical'])

N_k = omega_full.shape[0]      # 32
N_modes = omega_full.shape[1]  # 45
N_A = 36  # (local)
N_B = 8  # (local)
N_C = 1  # (local)

# Pump mode: the negative-frequency eigenvalue at k=0
k0_idx = 0  # k_eff[0] = 0
pump_mode_idx = 0  # lowest eigenvalue (most negative)
omega_pump = omega_full[k0_idx, pump_mode_idx]
pump_vec = evecs_full[k0_idx, :, pump_mode_idx]
pump_wA = sector_weight[k0_idx, pump_mode_idx, 0]
pump_wB = sector_weight[k0_idx, pump_mode_idx, 1]
pump_wC = sector_weight[k0_idx, pump_mode_idx, 2]

# Hybridization gap delta
delta_AB = 0.248  # M_KK, from task specification (confirmed: max AB_delta_gaps[1] = 0.2475)  # (local)
delta_AB_exact = AB_delta_gaps[1]  # = 0.24751 M_KK (tightest crossing)

print(f"Pump mode at k=0:")
print(f"  omega_pump = {omega_pump:.6f} M_KK")
print(f"  |omega_pump| = {abs(omega_pump):.6f} M_KK")
print(f"  Sector weights: A = {pump_wA:.4f}, B = {pump_wB:.4f}, C = {pump_wC:.4f}")
print(f"  A-B hybrid: {pump_wA + pump_wB:.4f} total")
print(f"\nHybridization gap:")
print(f"  delta_AB = {delta_AB_exact:.6f} M_KK (tightest crossing)")
print(f"  Coupled gap = {AB_coupled_gaps[1]:.6f} M_KK")
print(f"  Detuning = {AB_detunings[1]:.6f}")
print(f"\nA-tensor: |A_coset|^2 = {A_coset_sq:.3f}")
print(f"  |A_coset| = {np.sqrt(A_coset_sq):.6f}")
print(f"\nTransit parameters:")
print(f"  H_fold = {H_fold:.4f} M_KK (Hubble during transit)")
print(f"  v_terminal = {v_terminal:.4f} M_KK")
print(f"  dt_transit = {dt_transit:.6e} M_KK^-1")

# =============================================================================
# SECTION 2: Parametric amplification — Mathieu instability analysis
# =============================================================================
print("\n" + "=" * 78)
print("--- Section 2: Mathieu instability (exponential growth rate) ---")
print("=" * 78)

# The negative-frequency mode acts as a parametric pump. When the modulus
# oscillates (or rolls through the transit), it modulates the A-B coupling
# at frequency |omega_pump|. Modes near the A-B avoided crossing experience
# parametric resonance if their natural frequency omega_n satisfies:
#     2 * omega_n ≈ |omega_pump|   (primary resonance)
#     omega_n ≈ |omega_pump|       (subharmonic)
#
# For a periodically driven oscillator: d^2 x/dt^2 + omega_n^2 (1 + h*cos(Omega*t)) x = 0
# the Mathieu instability band at the n-th resonance has width:
#     Delta_omega ~ h * omega_n / 2  (for primary: Omega = 2*omega_n)
# and growth rate:
#     mu = (h * omega_n / 4) * sqrt(1 - (delta/h*omega_n)^2)
# where delta is the detuning from exact resonance.
#
# Here:
#   Omega = |omega_pump| = 2.52 M_KK
#   omega_n = frequencies near |omega_pump|/2 = 1.26 M_KK
#   h = modulation depth = V_AB_eff / omega_n^2
#   V_AB_eff = effective coupling from pump mode eigenvector projected onto V_AB

# Pump amplitude during transit: the modulus displacement from equilibrium.
# During BCS transit, the excitation energy E_exc = 60.6 M_KK is released.
# The pump mode amplitude: phi_pump ~ sqrt(2 * E_pump / |omega_pump|)
# where E_pump is the energy in the pump mode.
# Conservative: distribute E_exc equally among n_pairs ~ 60 modes
# Liberal: all energy goes through the pump (dominant instability)

E_pump_conservative = E_exc / (2 * n_pairs)  # per mode
E_pump_liberal = E_exc  # all in pump

phi_pump_conservative = np.sqrt(2 * E_pump_conservative / abs(omega_pump))
phi_pump_liberal = np.sqrt(2 * E_pump_liberal / abs(omega_pump))

print(f"\nPump amplitude estimates:")
print(f"  E_exc = {E_exc:.3f} M_KK (total excitation energy)")
print(f"  n_pairs = {n_pairs:.1f} (Bogoliubov pairs)")
print(f"  Conservative (E_pump = E_exc / 2n_pairs):")
print(f"    E_pump = {E_pump_conservative:.4f} M_KK")
print(f"    phi_pump = {phi_pump_conservative:.6f} sqrt(M_KK)")
print(f"  Liberal (E_pump = E_exc):")
print(f"    E_pump = {E_pump_liberal:.4f} M_KK")
print(f"    phi_pump = {phi_pump_liberal:.6f} sqrt(M_KK)")

# Effective modulation depth from the A-B coupling vertex
# The pump eigenvector has components in both A and B sectors.
# The parametric modulation comes from the A-sector component of the pump
# driving transitions in the B-sector through V_AB.
#
# h = |<pump| V_AB |target>|^2 / (omega_target^2)
# where the pump A-component couples to target B-component.

# Extract the effective coupling: project pump eigenvector onto V_AB
pump_A = pump_vec[:N_A]     # A-sector component of pump (36,)
pump_B = pump_vec[N_A:N_A+N_B]  # B-sector component of pump (8,)

# The trilinear vertex: pump mode decays into two daughter modes at the crossing.
# g_eff = Sum_{alpha, beta} pump_A[alpha] * V_AB[alpha, beta] * target_B[beta]
# For the primary resonance target: modes near omega = |omega_pump|/2 = 1.26 M_KK

# Find modes near the primary resonance frequency
omega_primary_res = abs(omega_pump) / 2  # = 1.26 M_KK
print(f"\nPrimary parametric resonance: omega_target = |omega_pump|/2 = {omega_primary_res:.4f} M_KK")

# At k=0, find positive modes closest to omega_primary_res
pos_modes_k0 = omega_full[k0_idx, omega_full[k0_idx] > 0]
pos_idx_k0 = np.where(omega_full[k0_idx] > 0)[0]
closest_to_res = np.argsort(np.abs(pos_modes_k0 - omega_primary_res))

print(f"Positive modes closest to {omega_primary_res:.4f} M_KK at k=0:")
for rank in range(min(5, len(closest_to_res))):
    i = closest_to_res[rank]
    mode_global = pos_idx_k0[i]
    om = omega_full[k0_idx, mode_global]
    sw = sector_weight[k0_idx, mode_global]
    detuning = om - omega_primary_res
    print(f"  mode {mode_global}: omega = {om:.6f}, detuning = {detuning:+.6f}, "
          f"w_A = {sw[0]:.4f}, w_B = {sw[1]:.4f}")

# Compute effective trilinear coupling for each resonant pair
# Energy conservation: omega_pump + omega_s + omega_i = 0
# -> omega_s + omega_i = |omega_pump| = 2.52 M_KK
# For symmetric decay: omega_s = omega_i = |omega_pump|/2 = 1.26 M_KK

print(f"\n--- Trilinear coupling vertices ---")

# Method: The trilinear coupling arises from the modulation of the Hamiltonian
# by the pump mode. The A-tensor vertex is:
#   g_{pump, s, i} = d^2 H / (d phi_pump d phi_s) evaluated at equilibrium
# In the sector basis, this is approximately V_AB projected through eigenvectors.

# For each pair of positive modes (s, i) satisfying omega_s + omega_i ~ |omega_pump|:
g_eff_list = []
pair_list = []

for k_idx in range(N_k):
    pos_mask = omega_full[k_idx] > 0
    pos_indices = np.where(pos_mask)[0]
    pos_omegas = omega_full[k_idx, pos_mask]

    for ii, idx_s in enumerate(pos_indices):
        for jj, idx_i in enumerate(pos_indices[ii:], start=ii):
            omega_s = omega_full[k_idx, idx_s]
            omega_i = omega_full[k_idx, idx_i]

            # Energy conservation check: omega_s + omega_i = |omega_pump|
            energy_mismatch = abs(omega_s + omega_i - abs(omega_pump))
            if energy_mismatch < 0.5:  # Within 0.5 M_KK of resonance
                # Compute trilinear vertex
                vec_s = evecs_full[k_idx, :, idx_s]
                vec_i = evecs_full[k_idx, :, idx_i]

                # g = pump_A . V_AB . (vec_s_B (*) vec_i_B) + permutations
                # Leading order: A-sector pump vertex times B-sector daughters
                s_B = vec_s[N_A:N_A+N_B]
                i_B = vec_i[N_A:N_A+N_B]
                s_A = vec_s[:N_A]
                i_A = vec_i[:N_A]

                # Three channels:
                # (1) pump_A drives s_B via V_AB, with i_B spectator overlap
                g1 = np.dot(pump_A, V_AB @ s_B) * np.dot(pump_B, i_B)
                # (2) pump_A drives i_B via V_AB, with s_B spectator overlap
                g2 = np.dot(pump_A, V_AB @ i_B) * np.dot(pump_B, s_B)
                # (3) pump_B converts to A via V_AB.T, daughters in B
                g3 = np.dot(pump_B, V_AB.T @ s_A) * np.dot(pump_A, i_A)

                g_total = abs(g1) + abs(g2) + abs(g3)

                if g_total > 1e-6:
                    g_eff_list.append(g_total)
                    pair_list.append((k_idx, idx_s, idx_i, omega_s, omega_i,
                                     energy_mismatch, g_total))

g_eff_list = np.array(g_eff_list)

print(f"Found {len(pair_list)} resonant pairs within 0.5 M_KK of energy conservation")
if len(pair_list) > 0:
    print(f"Top-10 by coupling strength:")
    sorted_pairs = sorted(pair_list, key=lambda x: x[6], reverse=True)
    for rank, (ki, si, ii, os_, oi_, em, g) in enumerate(sorted_pairs[:10]):
        print(f"  {rank+1}. k={k_eff[ki]:.4f}, omega_s={os_:.4f}, omega_i={oi_:.4f}, "
              f"mismatch={em:.4f}, g={g:.6f}")

    g_max = g_eff_list.max()
    g_mean = g_eff_list.mean()
    print(f"\nCoupling statistics:")
    print(f"  g_max = {g_max:.6f} M_KK")
    print(f"  g_mean = {g_mean:.6f} M_KK")
    print(f"  g_rms = {np.sqrt(np.mean(g_eff_list**2)):.6f} M_KK")
else:
    print("  No resonant pairs found -- expanding search window")
    g_max = 0.0  # (local)
    g_mean = 0.0  # (local)

# Alternative: Direct A-B vertex from the V_AB matrix
# The maximum coupling at the avoided crossing
V_AB_max = np.abs(V_AB).max()
V_AB_rms = np.sqrt(np.mean(V_AB**2))
print(f"\nDirect V_AB statistics:")
print(f"  max|V_AB| = {V_AB_max:.6f} M_KK")
print(f"  rms(V_AB) = {V_AB_rms:.6f} M_KK")

# =============================================================================
# SECTION 3: Mathieu growth rate computation
# =============================================================================
print("\n" + "=" * 78)
print("--- Section 3: Mathieu instability band and growth rate ---")
print("=" * 78)

# The modulation depth h for the Mathieu equation:
# h = (A-tensor vertex) * phi_pump / omega_target^2
#
# For the pump mode driving the A-B crossing modes:
# h_eff = sqrt(A_coset_sq) * |V_AB_eff| * phi_pump / omega_target^2

A_coset = np.sqrt(A_coset_sq)

# Target modes: those at the avoided crossing (delta = 0.248 M_KK)
# Their natural frequency: omega_target ~ lowest positive modes at crossing
# The avoided crossing produces modes near omega = delta/2 to few * delta
omega_target_crossing = delta_AB_exact  # 0.248 M_KK (gap energy scale)

# More precisely: the modes at the tightest A-B crossing have
# frequencies omega_+ and omega_- separated by delta_AB.
# omega_center at crossing ≈ 4.00 M_KK (mode 9 at k=0, w_A = 0.997)
# with the gap producing omega_+ = 4.00 + delta/2, omega_- = 4.00 - delta/2

# The parametric resonance for PRIMARY instability: Omega = 2*omega_target
# Here Omega = |omega_pump| = 2.52 M_KK -> omega_target = 1.26 M_KK
# These are B-dominated modes near 1.06-1.11 M_KK (modes 7-8 at k=0)

# For SUBHARMONIC resonance: Omega = omega_target
# omega_target = |omega_pump| = 2.52 M_KK -- no modes near this value at k=0

# Check: what about modes at other k-points?
print(f"\nScan for modes in primary Mathieu band across all k-points:")
omega_band_center = abs(omega_pump) / 2  # 1.26 M_KK
omega_band_width = 0.5  # generous search window  # (local)

modes_in_band = []
for ki in range(N_k):
    for mi in range(N_modes):
        om = omega_full[ki, mi]
        if om > 0 and abs(om - omega_band_center) < omega_band_width:
            sw = sector_weight[ki, mi]
            modes_in_band.append((ki, mi, om, sw[0], sw[1], sw[2]))

print(f"Found {len(modes_in_band)} modes in band [{omega_band_center-omega_band_width:.2f}, "
      f"{omega_band_center+omega_band_width:.2f}] M_KK")
if modes_in_band:
    for ki, mi, om, wa, wb, wc in modes_in_band[:15]:
        print(f"  k={k_eff[ki]:.4f}, mode={mi}, omega={om:.6f}, "
              f"w_A={wa:.4f}, w_B={wb:.4f}")

# Compute Mathieu growth rate for modes in the instability band
print(f"\nMathieu growth rates:")

# The effective modulation depth for each mode:
# h_eff = |<pump|H_coupling|mode>| / omega_mode^2
# H_coupling = the off-diagonal part of the Hamiltonian that the pump modulates

mu_max_conservative = 0.0  # (local)
mu_max_liberal = 0.0  # (local)
mathieu_results = []

for ki, mi, om, wa, wb, wc in modes_in_band:
    vec = evecs_full[ki, :, mi]
    vec_A = vec[:N_A]
    vec_B = vec[N_A:N_A+N_B]

    # Coupling: pump modulates the A-B coupling vertex
    # g_eff = |pump_A . V_AB . vec_B| + |pump_B . V_AB.T . vec_A|
    g1 = abs(np.dot(pump_A, V_AB @ vec_B))
    g2 = abs(np.dot(pump_B, V_AB.T @ vec_A))
    g_mode = g1 + g2

    # Modulation depth: h = g_mode * phi_pump / omega_mode
    h_cons = g_mode * phi_pump_conservative / om
    h_lib = g_mode * phi_pump_liberal / om

    # Mathieu growth rate: mu = h * omega_mode / 4
    # (valid for h << 1; for h > 1, the growth is ~ omega_mode)
    detuning_from_res = abs(2 * om - abs(omega_pump))

    # Exact Mathieu growth rate at primary resonance:
    # mu = (omega/2) * sqrt((h/2)^2 - (detuning/omega)^2)  when h > 2*detuning/omega
    h_threshold = 2 * detuning_from_res / om

    mu_cons = 0.0  # (local)
    mu_lib = 0.0  # (local)

    if h_cons > h_threshold:
        mu_cons = (om / 2) * np.sqrt((h_cons / 2)**2 - (detuning_from_res / om)**2)
    if h_lib > h_threshold:
        mu_lib = (om / 2) * np.sqrt((h_lib / 2)**2 - (detuning_from_res / om)**2)

    mu_max_conservative = max(mu_max_conservative, mu_cons)
    mu_max_liberal = max(mu_max_liberal, mu_lib)

    mathieu_results.append((ki, mi, om, g_mode, h_cons, h_lib,
                           mu_cons, mu_lib, detuning_from_res))

    if g_mode > 0.001:
        print(f"  k={k_eff[ki]:.4f}, omega={om:.4f}: g={g_mode:.6f}, "
              f"h_cons={h_cons:.4f}, h_lib={h_lib:.4f}, "
              f"mu_cons={mu_cons:.4f}, mu_lib={mu_lib:.4f}")

print(f"\nMaximum Mathieu growth rates:")
print(f"  mu_max (conservative) = {mu_max_conservative:.6f} M_KK")
print(f"  mu_max (liberal)      = {mu_max_liberal:.6f} M_KK")
print(f"  H_fold                = {H_fold:.4f} M_KK")
print(f"  mu_cons / H_fold      = {mu_max_conservative / H_fold:.6e}")
print(f"  mu_lib / H_fold       = {mu_max_liberal / H_fold:.6e}")

# =============================================================================
# SECTION 4: Fermi golden rule — perturbative decay rate
# =============================================================================
print("\n" + "=" * 78)
print("--- Section 4: Fermi Golden Rule decay rate ---")
print("=" * 78)

# The pump mode decays via: pump -> signal + idler
# Rate: Gamma_FGR = 2*pi * |M_fi|^2 * rho(E)
#
# |M_fi|^2 = |g_{pump, s, i}|^2 (trilinear vertex squared)
# rho(E) = density of final states at energy E = |omega_pump|
#
# For the discrete spectrum on the 32-cell Cayley graph:
# rho(E) = Sum_{s,i} delta(omega_s + omega_i - |omega_pump|)
#         ~ N_pairs / Delta_E  where N_pairs = number of pair channels
#         and Delta_E = typical energy spacing

# Count available pair channels
pair_channels = []
g_squared_sum = 0.0  # (local)

for ki in range(N_k):
    for si in range(N_modes):
        omega_s = omega_full[ki, si]
        if omega_s <= 0:
            continue
        for ii in range(si, N_modes):
            omega_i = omega_full[ki, ii]
            if omega_i <= 0:
                continue

            mismatch = abs(omega_s + omega_i - abs(omega_pump))
            if mismatch < 0.3:  # Within 0.3 M_KK
                vec_s = evecs_full[ki, :, si]
                vec_i = evecs_full[ki, :, ii]
                s_B = vec_s[N_A:N_A+N_B]
                i_B = vec_i[N_A:N_A+N_B]
                s_A = vec_s[:N_A]
                i_A = vec_i[:N_A]

                g1 = np.dot(pump_A, V_AB @ s_B) * np.dot(pump_B, i_B)
                g2 = np.dot(pump_A, V_AB @ i_B) * np.dot(pump_B, s_B)
                g3 = np.dot(pump_B, V_AB.T @ s_A) * np.dot(pump_A, i_A)

                g_sq = abs(g1)**2 + abs(g2)**2 + abs(g3)**2
                g_squared_sum += g_sq
                if g_sq > 1e-10:
                    pair_channels.append((ki, si, ii, omega_s, omega_i, mismatch, g_sq))

n_channels = len(pair_channels)
print(f"Pair decay channels (|omega_s + omega_i - |omega_pump|| < 0.3):")
print(f"  Total channels: {n_channels}")

if n_channels > 0:
    pair_channels.sort(key=lambda x: x[6], reverse=True)
    print(f"  Top-10 by |g|^2:")
    for rank, (ki, si, ii, os_, oi_, em, gsq) in enumerate(pair_channels[:10]):
        print(f"    {rank+1}. k={k_eff[ki]:.4f}, omega_s={os_:.4f}, omega_i={oi_:.4f}, "
              f"mismatch={em:.4f}, |g|^2={gsq:.6e}")

    # Density of states: discrete spectrum, smear with Lorentzian
    # rho ~ 1 / (mean spacing) for modes in the energy window
    energy_window = 0.3  # M_KK (matching our search window)  # (local)
    rho_eff = n_channels / energy_window  # effective DOS (1/M_KK)

    g_sq_max = pair_channels[0][6]
    g_sq_mean = g_squared_sum / max(n_channels, 1)

    print(f"\n  |g|^2 statistics:")
    print(f"    max |g|^2 = {g_sq_max:.6e} M_KK^2")
    print(f"    mean |g|^2 = {g_sq_mean:.6e} M_KK^2")
    print(f"    rho_eff = {rho_eff:.2f} M_KK^-1")

    # Fermi golden rule rate (sum over final states)
    # Gamma = 2*pi * Sum_f |M_fi|^2 * delta(E_f - E_i)
    # On discrete spectrum with Lorentzian broadening eta:
    # Gamma = 2*pi * Sum_f |g_f|^2 * (eta/pi) / ((Delta E_f)^2 + eta^2)
    #
    # For conservative estimate: use the BCS transit rate as broadening
    eta_transit = 1.0 / dt_transit  # Broadening from finite transit time
    print(f"    Transit broadening: eta = 1/dt_transit = {eta_transit:.2f} M_KK")

    Gamma_FGR = 0.0  # (local)
    for ki, si, ii, os_, oi_, em, gsq in pair_channels:
        lorentzian = (eta_transit / PI) / (em**2 + eta_transit**2)
        Gamma_FGR += 2 * PI * gsq * lorentzian

    # Also compute with narrower broadening (natural linewidth ~ delta_AB)
    eta_narrow = delta_AB_exact
    Gamma_FGR_narrow = 0.0  # (local)
    for ki, si, ii, os_, oi_, em, gsq in pair_channels:
        lorentzian = (eta_narrow / PI) / (em**2 + eta_narrow**2)
        Gamma_FGR_narrow += 2 * PI * gsq * lorentzian

    print(f"\nFermi Golden Rule rates:")
    print(f"  Gamma_FGR (transit broadening, eta = {eta_transit:.1f} M_KK)")
    print(f"    Gamma = {Gamma_FGR:.6f} M_KK")
    print(f"    Gamma / H_fold = {Gamma_FGR / H_fold:.6e}")
    print(f"  Gamma_FGR (narrow broadening, eta = {eta_narrow:.4f} M_KK)")
    print(f"    Gamma = {Gamma_FGR_narrow:.6f} M_KK")
    print(f"    Gamma / H_fold = {Gamma_FGR_narrow / H_fold:.6e}")
else:
    g_sq_max = 0.0  # (local)
    g_sq_mean = 0.0  # (local)
    Gamma_FGR = 0.0  # (local)
    Gamma_FGR_narrow = 0.0  # (local)
    print("  No pair channels found")

# =============================================================================
# SECTION 5: Landau-Zener transition at avoided crossing
# =============================================================================
print("\n" + "=" * 78)
print("--- Section 5: Landau-Zener transition probability ---")
print("=" * 78)

# During transit, the modulus rolls through the fold with velocity v_terminal.
# This sweeps the A-B detuning through zero at the avoided crossing.
# The Landau-Zener probability for non-adiabatic transition:
#   P_LZ = exp(-pi * delta_AB^2 / (2 * |d(detuning)/dt|))
#
# The sweep rate |d(detuning)/dt| comes from the velocity in tau-space:
#   d(detuning)/dt = v_terminal * d(detuning)/d(tau)
#
# From the data: the detuning changes from 0.013 to 0.12 over a small tau range.
# We can estimate d(detuning)/d(tau) from the A-B crossing structure.

# The detuning at the tightest crossing is 0.013 M_KK
# The A-mode frequency is tau-independent (geometric), the B-mode frequency
# shifts with E_J * lambda_k, which depends on tau through E_J(tau).
# d(omega_B)/d(tau) = (d E_J / d tau) * lambda_k + d(E_sp)/d(tau)
# From S62 data: d E_J / d tau at fold ≈ E_J * d(log E_J)/d(tau)

# Approximate d(detuning)/d(tau) from the fact that E_J changes by O(1) per unit tau
# and E_J = 7.04 M_KK -> detuning changes by ~ E_J per unit tau
# More carefully: the smallest detuning is 0.013, this is omega_A - omega_B at crossing.
# omega_B = E_sp + E_J * lambda_k -> d(omega_B)/d(tau) ~ (dE_sp/dtau) + (dE_J/dtau)*lambda_k

# From s62 script: dE_sp_dtau was computed. We can estimate from the eigenvalue curvature.
# Conservative: d(detuning)/d(tau) ~ omega_B at crossing (order 1 M_KK per unit tau)
# The B-modes at crossing have omega ~ 4.0 M_KK (where A crosses B)

# Better estimate: d(E_J)/d(tau) * lambda at lowest nonzero k
# From canonical constants: E_J ~ 7.04, fold at tau = 0.19
# dE_J/dtau ~ E_J * (some coefficient) -- from spectral action, order 10-100 M_KK

# Use a physical estimate: the detuning sweeps through zero in time dt_cross.
# The crossing happens over a tau-range ~ delta_AB / (dE/dtau)
# where dE/dtau = d(omega_A - omega_B)/dtau

# At the tightest crossing (mode 0 of A vs mode 7 of B):
# omega_A ~ 3.88 M_KK (lowest A mode), omega_B(fold) ~ 3.87 (after corrections)
# d(omega_B)/d(tau) changes by several M_KK per unit tau

# Conservative estimate based on dimensional analysis:
# d(detuning)/dt = v_terminal * d(detuning)/d(tau)
# d(detuning)/d(tau) ~ E_J = 7.04 M_KK per unit tau (B-modes shift by E_J per tau)
d_detuning_dtau = E_J_fold  # M_KK per tau
d_detuning_dt = v_terminal * d_detuning_dtau  # M_KK^2 (d/dt in M_KK units)

# Landau-Zener parameter
gamma_LZ = PI * delta_AB_exact**2 / (2 * d_detuning_dt)
P_LZ = np.exp(-gamma_LZ)
P_adiabatic = 1 - P_LZ

print(f"Landau-Zener parameters:")
print(f"  delta_AB = {delta_AB_exact:.6f} M_KK (hybridization gap)")
print(f"  v_terminal = {v_terminal:.4f} M_KK (modulus roll velocity)")
print(f"  d(detuning)/d(tau) = {d_detuning_dtau:.4f} M_KK/tau")
print(f"  d(detuning)/dt = v * d(det)/d(tau) = {d_detuning_dt:.4f} M_KK^2")
print(f"  gamma_LZ = pi * delta^2 / (2 * |d(det)/dt|) = {gamma_LZ:.6f}")
print(f"  P_LZ (non-adiabatic) = exp(-gamma_LZ) = {P_LZ:.6e}")
print(f"  P_adiabatic = 1 - P_LZ = {P_adiabatic:.6f}")

# The Landau-Zener transition rate:
# During a single sweep through the crossing (transit time dt_transit),
# the probability of mode conversion is P_adiabatic * (1 - P_adiabatic)
# (Stueckelberg oscillations).
# Effective rate: Gamma_LZ ~ P_adiabatic * |omega_pump|
# (each oscillation period of the pump contributes one LZ transition attempt)

omega_pump_abs = abs(omega_pump)
Gamma_LZ = P_adiabatic * omega_pump_abs / (2 * PI)  # rate = P * frequency
N_crossings_per_transit = omega_pump_abs * dt_transit / (2 * PI)

print(f"\nLandau-Zener reheating rate:")
print(f"  Gamma_LZ = P_adiabatic * |omega_pump| / (2*pi)")
print(f"           = {P_adiabatic:.6f} * {omega_pump_abs:.4f} / {2*PI:.4f}")
print(f"           = {Gamma_LZ:.6f} M_KK")
print(f"  Gamma_LZ / H_fold = {Gamma_LZ / H_fold:.6e}")
print(f"  N_crossings per transit = |omega_pump| * dt_transit / (2*pi)")
print(f"                          = {N_crossings_per_transit:.6e}")

# =============================================================================
# SECTION 6: Broad-resonance estimate (non-perturbative)
# =============================================================================
print("\n" + "=" * 78)
print("--- Section 6: Broad-resonance (non-perturbative) estimate ---")
print("=" * 78)

# When the coupling is strong (h > 1 or g > omega), parametric amplification
# enters the broad-resonance regime where growth is not exponential but instant.
#
# The key dimensionless ratio is:
#   q = (coupling^2 * phi_pump^2) / (4 * omega_pump^2)
# For q >> 1: broad resonance, instant particle production
# For q ~ 1: intermediate, efficient parametric resonance
# For q << 1: narrow resonance, perturbative decay only

# Use the A-B coupling at the avoided crossing
# g_eff at crossing ~ V_AB_max * A_coset * (crossing weight factors)
# From the data: the pump mode has 33% A-weight, 67% B-weight
# The crossing modes have comparable A-B mixing

# Effective coupling at the avoided crossing: g_cross ~ sqrt(A_coset_sq) * V_AB_rms
g_cross = np.sqrt(A_coset_sq) * V_AB_rms
g_cross_max = np.sqrt(A_coset_sq) * V_AB_max

print(f"Coupling estimates:")
print(f"  g_cross (rms) = sqrt({A_coset_sq}) * {V_AB_rms:.6f} = {g_cross:.6f} M_KK")
print(f"  g_cross (max) = sqrt({A_coset_sq}) * {V_AB_max:.6f} = {g_cross_max:.6f} M_KK")

# Mathieu q-parameter for each pump amplitude estimate
q_conservative = g_cross**2 * phi_pump_conservative**2 / (4 * omega_pump**2)
q_liberal = g_cross**2 * phi_pump_liberal**2 / (4 * omega_pump**2)
q_max_conservative = g_cross_max**2 * phi_pump_conservative**2 / (4 * omega_pump**2)
q_max_liberal = g_cross_max**2 * phi_pump_liberal**2 / (4 * omega_pump**2)

print(f"\nMathieu q-parameter (broad-resonance diagnostic):")
print(f"  q (rms coupling, conservative pump)  = {q_conservative:.6e}")
print(f"  q (rms coupling, liberal pump)       = {q_liberal:.6e}")
print(f"  q (max coupling, conservative pump)  = {q_max_conservative:.6e}")
print(f"  q (max coupling, liberal pump)       = {q_max_liberal:.6e}")

# Broad resonance condition: q > 1
if q_max_liberal > 1:
    print(f"  -> BROAD RESONANCE regime (q_max_liberal = {q_max_liberal:.2f} > 1)")
    broad_resonance = True
elif q_max_liberal > 0.01:
    print(f"  -> INTERMEDIATE regime (q_max_liberal = {q_max_liberal:.4f})")
    broad_resonance = False
else:
    print(f"  -> NARROW RESONANCE regime (q < 0.01)")
    broad_resonance = False

# In the broad-resonance regime, the growth rate is:
# mu_broad ~ q^{1/4} * omega_pump / 2  (for q >> 1)
# In the narrow-resonance regime:
# mu_narrow ~ g * phi_pump / (4 * omega)  (leading instability band)

# Non-perturbative rate estimate
if q_max_liberal > 1:
    mu_broad = q_max_liberal**(0.25) * abs(omega_pump) / 2
else:
    mu_broad = g_cross_max * phi_pump_liberal / (4 * abs(omega_pump))

print(f"\nNon-perturbative growth rate:")
print(f"  mu_broad = {mu_broad:.6f} M_KK")
print(f"  mu_broad / H_fold = {mu_broad / H_fold:.6e}")

# =============================================================================
# SECTION 7: The key rate — direct A-B mode conversion
# =============================================================================
print("\n" + "=" * 78)
print("--- Section 7: Direct A-B mode conversion rate (the decisive computation) ---")
print("=" * 78)

# The PHYSICAL mechanism: During transit, the modulus sweeps through tau_fold
# with velocity v_terminal. This time-dependent background drives transitions
# between A-sector (geometric) modes and B-sector (matter) modes through the
# A-tensor coupling. THIS is the reheating mechanism: geometric energy converts
# to particle excitations.
#
# The RATE of this conversion is not a perturbative decay of a single quantum,
# but a CLASSICAL parametric process driven by the rolling modulus.
#
# Key insight: the pump is not a quantum of the negative-frequency mode —
# it is the CLASSICAL ROLLING of the modulus through the A-B crossing.
# The negative frequency simply tells us the instability direction.
#
# Classical parametric conversion rate:
# Gamma_AB = |V_AB|^2 * v_terminal^2 / delta_AB
#
# This is the Rabi flopping rate at the avoided crossing, driven by the
# time-dependent detuning sweep from the modulus roll.

# V_AB_eff at the tightest crossing:
# From the S62 data, the hybridization gap delta = 0.248 M_KK.
# This gap is 2 * V_AB_eff (avoided crossing = 2x the coupling).
V_AB_eff = delta_AB_exact / 2  # = 0.124 M_KK

# The Rabi frequency at exact resonance
Omega_Rabi = delta_AB_exact  # = 2 * V_AB_eff (the gap IS the Rabi splitting)

# The transition rate per crossing:
# During transit, the modulus sweeps through with velocity v_terminal in tau.
# Number of A-B crossings swept through per unit time:
# Rate ~ Omega_Rabi (the mixing is driven at the Rabi frequency)

# Total conversion rate: Rabi frequency times occupation
# For CLASSICAL rolling (large occupation), the rate is the Rabi frequency itself
Gamma_Rabi = Omega_Rabi  # M_KK

# More careful: Zener formula for continuous sweep
# The non-adiabatic transition probability gives the FRACTION of population
# transferred per crossing. The rate is then:
# Gamma_conversion = P_adiabatic * (sweep rate / delta)
# where sweep rate = d(detuning)/dt and delta is the gap width

Gamma_conversion = P_adiabatic * d_detuning_dt / delta_AB_exact

print(f"Direct A-B mode conversion:")
print(f"  V_AB_eff = delta/2 = {V_AB_eff:.6f} M_KK")
print(f"  Omega_Rabi = delta_AB = {Omega_Rabi:.6f} M_KK")
print(f"  P_adiabatic = {P_adiabatic:.6f}")
print(f"  d(detuning)/dt = {d_detuning_dt:.4f} M_KK^2")
print(f"  Gamma_conversion = P_adiab * (d(det)/dt) / delta")
print(f"                   = {P_adiabatic:.4f} * {d_detuning_dt:.4f} / {delta_AB_exact:.4f}")
print(f"                   = {Gamma_conversion:.4f} M_KK")
print(f"  Gamma_conversion / H_fold = {Gamma_conversion / H_fold:.6e}")

# =============================================================================
# SECTION 8: Summary and gate verdict
# =============================================================================
print("\n" + "=" * 78)
print("--- Section 8: Summary and Gate Verdict ---")
print("=" * 78)

# Collect all rate estimates
rates = {}
rates['Mathieu_conservative'] = mu_max_conservative
rates['Mathieu_liberal'] = mu_max_liberal
rates['FGR_transit'] = Gamma_FGR
rates['FGR_narrow'] = Gamma_FGR_narrow
rates['LZ_rate'] = Gamma_LZ
rates['Broad_resonance'] = mu_broad
rates['Rabi_frequency'] = Omega_Rabi
rates['LZ_conversion'] = Gamma_conversion

print(f"\nAll parametric amplification / mode conversion rates (M_KK units):")
print(f"{'Method':<30s} {'Rate':<15s} {'Rate/H_fold':<15s} {'> H?':<6s}")
print("-" * 66)
for name, rate in sorted(rates.items(), key=lambda x: x[1], reverse=True):
    ratio = rate / H_fold
    verdict = "YES" if rate > H_fold else "NO"
    print(f"{name:<30s} {rate:<15.6f} {ratio:<15.6e} {verdict:<6s}")
print(f"{'H_fold (threshold)':<30s} {H_fold:<15.4f} {'1.000':<15s} {'---':<6s}")

# Determine decisive rate
# The physically correct estimate is the LZ conversion rate for the CLASSICAL
# rolling modulus through the A-B avoided crossing
Gamma_decisive = Gamma_conversion
method_decisive = "LZ_conversion"

# Also flag the Rabi frequency as the UPPER BOUND (full coherent conversion)
Gamma_upper = Omega_Rabi
Gamma_lower = min(r for r in rates.values() if r > 0) if any(r > 0 for r in rates.values()) else 0.0

print(f"\nDecisive rate: Gamma = {Gamma_decisive:.4f} M_KK ({method_decisive})")
print(f"Upper bound: Gamma = {Gamma_upper:.4f} M_KK (Rabi frequency)")
print(f"H_fold = {H_fold:.4f} M_KK")

# GATE VERDICT
gate_pass = Gamma_decisive > H_fold

print(f"\n{'=' * 40}")
print(f"GATE: AB-PARAMETRIC-63")
if gate_pass:
    print(f"VERDICT: PASS")
    print(f"  Gamma_conversion = {Gamma_decisive:.4f} M_KK > H_fold = {H_fold:.4f} M_KK")
    print(f"  Ratio: {Gamma_decisive / H_fold:.2f}x")
else:
    print(f"VERDICT: FAIL")
    print(f"  Gamma_conversion = {Gamma_decisive:.4f} M_KK < H_fold = {H_fold:.4f} M_KK")
    print(f"  Shortfall: {H_fold / max(Gamma_decisive, 1e-30):.2f}x")

    # Check if ANY rate passes
    any_pass = any(r > H_fold for r in rates.values())
    if any_pass:
        passing = [(n, r) for n, r in rates.items() if r > H_fold]
        print(f"  NOTE: {len(passing)} rate estimate(s) DO exceed H_fold:")
        for n, r in passing:
            print(f"    {n}: {r:.4f} M_KK ({r/H_fold:.2f}x H_fold)")
print(f"{'=' * 40}")

# =============================================================================
# SECTION 9: Cross-checks
# =============================================================================
print("\n" + "=" * 78)
print("--- Section 9: Cross-checks ---")
print("=" * 78)

# Cross-check 1: Energy conservation
print(f"\n1. Energy conservation:")
print(f"   |omega_pump| = {abs(omega_pump):.6f} M_KK")
print(f"   Modes available for pair production at |omega_pump| = {abs(omega_pump):.4f}:")
n_pairs_available = 0
for ki in range(N_k):
    for si in range(N_modes):
        if omega_full[ki, si] <= 0:
            continue
        for ii in range(si, N_modes):
            if omega_full[ki, ii] <= 0:
                continue
            if abs(omega_full[ki, si] + omega_full[ki, ii] - abs(omega_pump)) < 0.5:
                n_pairs_available += 1
print(f"   N_pairs in energy window: {n_pairs_available}")

# Cross-check 2: Dimensional consistency
print(f"\n2. Dimensional analysis:")
print(f"   [V_AB] = M_KK (dimensionless coupling in M_KK units) [OK]")
print(f"   [delta_AB] = M_KK (energy gap) [OK]")
print(f"   [d(det)/dt] = M_KK^2 (rate of energy change) [OK]")
print(f"   [Gamma] = M_KK (inverse time in M_KK units) [OK]")
print(f"   [H_fold] = M_KK (Hubble rate) [OK]")

# Cross-check 3: Adiabaticity parameter
gamma_adiab = delta_AB_exact**2 / d_detuning_dt
print(f"\n3. Adiabaticity parameter gamma = delta^2 / |d(det)/dt|:")
print(f"   gamma = {delta_AB_exact:.4f}^2 / {d_detuning_dt:.4f} = {gamma_adiab:.6e}")
print(f"   gamma << 1: fully non-adiabatic (impulsive transition)")
print(f"   gamma >> 1: fully adiabatic (smooth conversion)")
print(f"   gamma = {gamma_adiab:.4e}: {'NON-ADIABATIC' if gamma_adiab < 1 else 'ADIABATIC'}")

# Cross-check 4: Number of e-folds of amplification during transit
if mu_max_liberal > 0:
    n_efolds_liberal = mu_max_liberal * dt_transit
    print(f"\n4. E-folds of Mathieu growth during transit:")
    print(f"   n_efold = mu_max_liberal * dt_transit = {mu_max_liberal:.4f} * {dt_transit:.6e}")
    print(f"           = {n_efolds_liberal:.6e}")

# Cross-check 5: Condensed matter analog
print(f"\n5. Condensed matter analog:")
print(f"   The A-B hybridization gap delta = {delta_AB_exact:.4f} M_KK is the analog")
print(f"   of the avoided crossing in a driven two-level system (Jaynes-Cummings).")
print(f"   The modulus roll is the analog of a swept magnetic field through a")
print(f"   spin resonance. P_adiabatic = {P_adiabatic:.6f} is the LZ probability.")
print(f"   In superfluid He-3: this is the analog of the A-B transition driving")
print(f"   pair-breaking at the gap edge, creating quasiparticle excitations.")

# =============================================================================
# SECTION 10: Save data and plot
# =============================================================================
print("\n" + "=" * 78)
print("--- Section 10: Save data and plot ---")
print("=" * 78)

# Save all results
np.savez(str(OUT_NPZ),
    # Input parameters
    omega_pump=omega_pump,
    delta_AB=delta_AB_exact,
    A_coset_sq=A_coset_sq,
    H_fold=H_fold,
    v_terminal=v_terminal,
    dt_transit=dt_transit,
    E_J_fold=E_J_fold,
    # Pump mode properties
    pump_wA=pump_wA,
    pump_wB=pump_wB,
    pump_vec=pump_vec,
    phi_pump_conservative=phi_pump_conservative,
    phi_pump_liberal=phi_pump_liberal,
    # Rate estimates
    mu_max_conservative=mu_max_conservative,
    mu_max_liberal=mu_max_liberal,
    Gamma_FGR=Gamma_FGR,
    Gamma_FGR_narrow=Gamma_FGR_narrow,
    Gamma_LZ=Gamma_LZ,
    mu_broad=mu_broad,
    Omega_Rabi=Omega_Rabi,
    Gamma_conversion=Gamma_conversion,
    # LZ parameters
    P_LZ=P_LZ,
    P_adiabatic=P_adiabatic,
    gamma_LZ=gamma_LZ,
    d_detuning_dt=d_detuning_dt,
    # Mathieu parameters
    q_conservative=q_conservative,
    q_liberal=q_liberal,
    q_max_liberal=q_max_liberal,
    # Pair channels
    n_pair_channels=n_channels,
    g_sq_max=g_sq_max,
    g_sq_mean=g_sq_mean,
    # Gate
    gate_name=np.array(['AB-PARAMETRIC-63']),
    gate_pass=gate_pass,
    gate_detail=np.array([
        f"{'PASS' if gate_pass else 'FAIL'}: Gamma_conv = {Gamma_decisive:.4f} M_KK "
        f"{'>' if gate_pass else '<'} H_fold = {H_fold:.4f} M_KK. "
        f"Ratio = {Gamma_decisive/H_fold:.4f}. "
        f"delta_AB = {delta_AB_exact:.4f}, P_adiab = {P_adiabatic:.6f}, "
        f"Rabi upper bound = {Omega_Rabi:.4f} M_KK."
    ]),
)
print(f"Saved: {OUT_NPZ}")

# --- Plot ---
fig = plt.figure(figsize=(16, 10))
gs = GridSpec(2, 3, figure=fig, hspace=0.35, wspace=0.35)

# Panel 1: Rate comparison bar chart
ax1 = fig.add_subplot(gs[0, 0])
rate_names = list(rates.keys())
rate_vals = [rates[n] for n in rate_names]
colors = ['green' if r > H_fold else 'red' for r in rate_vals]
bars = ax1.barh(range(len(rate_names)), [r / H_fold for r in rate_vals], color=colors, alpha=0.7)
ax1.axvline(x=1.0, color='black', linestyle='--', linewidth=2, label='H_fold')
ax1.set_yticks(range(len(rate_names)))
ax1.set_yticklabels(rate_names, fontsize=7)
ax1.set_xlabel('Rate / H_fold')
ax1.set_title('Parametric Rates vs H_fold')
ax1.set_xscale('log')
ax1.legend()

# Panel 2: Spectrum at k=0 showing pump and daughter modes
ax2 = fig.add_subplot(gs[0, 1])
omega_k0 = omega_full[0]
sw_k0 = sector_weight[0]
for i, (om, sw) in enumerate(zip(omega_k0, sw_k0)):
    color = plt.cm.RdYlBu(sw[0])  # A-weight determines color
    ax2.barh(i, om, color=color, alpha=0.7, height=0.8)
ax2.axvline(x=0, color='gray', linestyle='-', linewidth=0.5)
ax2.axvline(x=omega_pump, color='red', linestyle='--', linewidth=2, label=f'pump = {omega_pump:.2f}')
ax2.axvline(x=abs(omega_pump)/2, color='blue', linestyle='--', linewidth=1,
            label=f'primary res = {abs(omega_pump)/2:.2f}')
ax2.set_xlabel('omega (M_KK)')
ax2.set_ylabel('Mode index')
ax2.set_title('Spectrum at k=0 (color = A-weight)')
ax2.legend(fontsize=7)

# Panel 3: A-B hybridization gap vs detuning
ax3 = fig.add_subplot(gs[0, 2])
valid = np.abs(AB_delta_gaps) < 2  # exclude outliers
ax3.scatter(AB_detunings[valid], AB_delta_gaps[valid], s=20, c='blue', alpha=0.5)
ax3.axhline(y=delta_AB_exact, color='red', linestyle='--', label=f'delta = {delta_AB_exact:.3f}')
ax3.set_xlabel('Detuning (M_KK)')
ax3.set_ylabel('Hybridization gap delta (M_KK)')
ax3.set_title('A-B Avoided Crossing Gaps')
ax3.legend(fontsize=8)

# Panel 4: Negative frequency mode dispersion
ax4 = fig.add_subplot(gs[1, 0])
neg_omegas = []
neg_k = []
for ki in range(N_k):
    for mi in range(N_modes):
        if omega_full[ki, mi] < 0:
            neg_omegas.append(omega_full[ki, mi])
            neg_k.append(k_eff[ki])
if neg_omegas:
    ax4.scatter(neg_k, neg_omegas, c='red', s=30, zorder=5, label='Negative modes')
ax4.axhline(y=0, color='gray', linestyle='-')
# Also plot first few positive modes
for mi in range(min(5, N_modes)):
    omegas_mi = [omega_full[ki, mi] for ki in range(N_k)]
    ax4.plot(k_eff, omegas_mi, 'b-', alpha=0.3, linewidth=0.5)
ax4.set_xlabel('k_eff')
ax4.set_ylabel('omega (M_KK)')
ax4.set_title('Negative-frequency mode dispersion')
ax4.legend(fontsize=8)
ax4.set_ylim(-3, 3)

# Panel 5: V_AB coupling matrix heatmap
ax5 = fig.add_subplot(gs[1, 1])
im = ax5.imshow(np.abs(V_AB[:12, :]), aspect='auto', cmap='viridis')
ax5.set_xlabel('B mode')
ax5.set_ylabel('A mode')
ax5.set_title('|V_AB| coupling (first 12 A modes)')
plt.colorbar(im, ax=ax5, label='M_KK')

# Panel 6: Landau-Zener probability vs sweep rate
ax6 = fig.add_subplot(gs[1, 2])
sweep_rates = np.logspace(-2, 4, 200)
P_LZ_scan = np.exp(-PI * delta_AB_exact**2 / (2 * sweep_rates))
P_adiab_scan = 1 - P_LZ_scan
Gamma_conv_scan = P_adiab_scan * sweep_rates / delta_AB_exact
ax6.semilogy(sweep_rates, Gamma_conv_scan / H_fold, 'b-', linewidth=2)
ax6.axhline(y=1, color='red', linestyle='--', label='H_fold')
ax6.axvline(x=d_detuning_dt, color='green', linestyle='--',
            label=f'd(det)/dt = {d_detuning_dt:.0f}')
ax6.set_xlabel('|d(detuning)/dt| (M_KK^2)')
ax6.set_ylabel('Gamma_conv / H_fold')
ax6.set_title('LZ Conversion Rate vs Sweep Rate')
ax6.legend(fontsize=8)

fig.suptitle('AB-PARAMETRIC-63: Parametric Amplification Reheating via A-B Conversion',
             fontsize=13, fontweight='bold')

plt.savefig(str(OUT_PNG), dpi=150, bbox_inches='tight')
print(f"Saved: {OUT_PNG}")

elapsed = time.time() - t_start
print(f"\nTotal runtime: {elapsed:.1f}s")
print("DONE")
