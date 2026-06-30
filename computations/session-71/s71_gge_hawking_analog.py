#!/usr/bin/env python3
"""
s71_gge_hawking_analog.py — BEC Analog Experiment Prediction: C_V(T_eff)
=========================================================================

Gate: GGE-HAWKING-ANALOG-71 (INFO)
Session: S71, Wave 4-A

Physics:
  The substrate transit (supersonic passage through the van Hove fold) has a
  laboratory analog in BEC experiments where a rapid interaction quench drives
  the condensate through a sonic horizon. The GGE relic — a non-thermal phonon
  distribution — produces a characteristic deviation in the specific heat C_V(T)
  from the Debye T^3 law. This computation predicts the magnitude and temperature
  range of that deviation for a ^39K BEC analog experiment.

  The BEC is a simplified projection of the substrate transit. The substrate is
  fundamental; the BEC models its acoustic sector. The chirp rate transfers
  cleanly because it is a geometric invariant (CHIRP-UNIVERSALITY-71, PASS).

  In the Volovik superfluid vacuum program (Paper 01, Section II.G), the
  zero-point energies of phonons do not contribute to the gravitating vacuum
  energy because the microscopic theory enforces thermodynamic equilibrium.
  The GGE relic is a non-equilibrium excitation ABOVE this vacuum, and its
  specific heat is a measurable departure from the equilibrium Debye law.

Inputs:
  - computations/session-69/s69_bec_analog.npz  (BEC analog parameters)
  - computations/_shared/canonical_constants.py (all constants)

Output:
  - computations/session-71/s71_gge_hawking_analog.npz
"""

import numpy as np
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    T_compound, c_fabric, n_pairs, N_dof_BCS, Delta_BCS,
    E_exc, k_B, k_B_SI, hbar_SI, M_KK, c_light,
    H_fold, v_terminal, dt_transit, omega_tau
)

# ============================================================================
#  Step 1: Load BEC analog data from S69
# ============================================================================

bec_data = np.load(os.path.join(os.path.dirname(__file__), 's69_bec_analog.npz'),
                   allow_pickle=True)

# BEC parameters (^39K, Feshbach resonance quench)
c_s_BEC    = float(bec_data['c_s_f_B'])       # m/s, post-quench sound speed
xi_f       = float(bec_data['xi_f_B'])         # m, post-quench healing length
Mach_BEC   = float(bec_data['Mach_BEC_B'])     # Mach number of quench
n_0_BEC    = float(bec_data['n_0'])            # m^{-3}, condensate density
k_phys     = bec_data['k_phys']                # 1/m, momentum array
nk_strong  = bec_data['nk_strong']             # occupation for strong quench
nk_moderate= bec_data['nk_moderate']           # occupation for moderate quench
nk_extreme = bec_data['nk_extreme']            # occupation for extreme quench
n_plat_strong = float(bec_data['n_plateau_strong'])
dt_Q       = float(bec_data['dt_Q'])           # s, quench time
T_max_BEC  = float(bec_data['T_max_B'])        # K, max temperature from quench

# Framework parameters from S69 data
Mach_framework = float(bec_data['Mach_framework'])
k_tach_framework = float(bec_data['k_tach_framework'])

print("=" * 72)
print("GGE-HAWKING-ANALOG-71: BEC Analog Specific Heat Prediction")
print("=" * 72)
print()

# ============================================================================
#  Step 2: Map framework parameters to BEC
# ============================================================================

# The substrate transit has T_compound (microcanonical temperature in M_KK units)
# The BEC analog maps this through the ratio of sound speeds and lattice spacings.
#
# Convention translation (Volovik corpus -> framework -> BEC):
#   Substrate: c_fabric = 209.97 M_KK (fabric sound speed)
#   BEC:       c_s_BEC = 0.0215 m/s (^39K post-quench)
#
# The effective temperature in the BEC is set by the quench energy injection.
# T_eff_BEC = T_compound * (c_BEC / c_fabric) * (a_BEC / a_lattice)
#
# But the BEC has its own microscopic scale: the healing length xi_f.
# The effective temperature from quench energy:
#   E_quench = (1/2) * m_atom * c_s_BEC^2 * (Mach^2 - 1) per mode
#   T_eff ~ E_quench / k_B * (n_modes_excited / n_total)

m_39K = 39 * 1.66054e-27  # kg, ^39K atomic mass

# Quench energy per atom (kinetic energy of the interaction quench)
E_quench_per_atom = 0.5 * m_39K * c_s_BEC**2 * (Mach_BEC**2 - 1)
T_quench_kinetic = E_quench_per_atom / k_B_SI  # K

# The GGE temperature from the occupation number plateau:
# n_plateau = 1/(exp(epsilon/T_eff) - 1) at k ~ 1/xi
# For the plateau: epsilon_char = hbar * c_s_BEC / xi_f
epsilon_char = hbar_SI * c_s_BEC / xi_f  # J
T_eff_from_plateau = epsilon_char / (k_B_SI * np.log(1 + 1/n_plat_strong))  # K

# The physical T_eff is the one consistent with the GGE distribution
T_eff_BEC = T_eff_from_plateau

# Also compute T_max from S69 data for cross-check
print(f"BEC parameters (^39K Feshbach quench):")
print(f"  c_s_BEC        = {c_s_BEC:.4e} m/s")
print(f"  xi_f (healing)  = {xi_f:.4e} m")
print(f"  Mach_BEC       = {Mach_BEC:.3f}")
print(f"  n_0            = {n_0_BEC:.4e} m^{{-3}}")
print(f"  dt_Q (quench)  = {dt_Q:.2e} s")
print(f"  n_plateau      = {n_plat_strong:.4f}")
print()
print(f"Framework mapping:")
print(f"  T_compound     = {T_compound:.4f} M_KK")
print(f"  c_fabric       = {c_fabric:.2f} M_KK")
print(f"  Mach_framework = {Mach_framework:.2f}")
print()
print(f"Effective temperatures:")
print(f"  T_quench (kinetic)   = {T_quench_kinetic:.4e} K")
print(f"  T_eff (from plateau) = {T_eff_BEC:.4e} K")
print(f"  T_max (S69)          = {T_max_BEC:.4e} K")
print()

# ============================================================================
#  Step 3: Compute C_V(T) for the GGE distribution
# ============================================================================
#
# The specific heat for a phonon gas with occupation n_k:
#   C_V(T) = sum_k (epsilon_k^2 / T^2) * n_k * (1 + n_k)
#
# For the GGE, n_k is NOT a Bose-Einstein distribution but the
# non-thermal occupation from the quench. The deviation from Debye
# is the signature of the GGE relic.

# Temperature scan range: from 0.01 * T_eff to 10 * T_eff
N_T = 200
T_scan = np.logspace(np.log10(T_eff_BEC * 0.01),
                     np.log10(T_eff_BEC * 10),
                     N_T)

# Momentum grid from BEC data
dk = k_phys[1] - k_phys[0]  # dk for integration

# Dispersion: epsilon_k = hbar * c_s * |k| (linear, Bogoliubov at low k)
epsilon_k = hbar_SI * c_s_BEC * k_phys  # J

# -- C_V from GGE distribution --
# The GGE occupation is fixed (frozen by integrability, Volovik Paper 25 Sec V).
# C_V_GGE = d<E>/dT where <E> = sum_k epsilon_k * n_k(T_eff)
# But the GGE occupation is temperature-independent (it's a non-thermal state).
# The correct comparison is:
#
# (a) C_V_thermal(T): specific heat if the same energy were in a thermal state
# (b) C_V_GGE_eff(T): specific heat measured by coupling to a weak thermometer
#
# For the GGE, the effective C_V measured by a weak probe at temperature T is:
#   C_V_eff(T) = sum_k (epsilon_k^2 / T^2) * n_k^BE(T) * (1 + n_k^BE(T))
#
# where n_k^BE(T) = 1/(exp(epsilon_k/(k_B*T)) - 1) is the thermal reference.
#
# The GGE DEPARTURE is measured by comparing:
#   E_GGE = sum_k epsilon_k * n_k_GGE    (total energy in the GGE state)
#   E_thermal(T) = sum_k epsilon_k * n_k^BE(T)  (thermal energy at temperature T)
#
# T_eff is defined by E_GGE = E_thermal(T_eff), i.e., equal total energy.
# But the DISTRIBUTION is different, so the differential response differs.

# First: compute the total GGE energy
E_GGE_total = np.sum(epsilon_k * nk_strong * dk * k_phys**2 / (2 * np.pi**2))
print(f"Total GGE energy density: {E_GGE_total:.4e} J/m^3")

# Compute C_V_thermal(T) and C_V_GGE(T) for each temperature
C_V_thermal = np.zeros(N_T)
C_V_GGE = np.zeros(N_T)
E_thermal = np.zeros(N_T)

for i, T in enumerate(T_scan):
    kBT = k_B_SI * T
    x = epsilon_k / kBT

    # Thermal Bose-Einstein occupation
    # Clip to avoid overflow
    x_clip = np.clip(x, 0, 500)
    n_BE = np.where(x_clip < 500, 1.0 / (np.exp(x_clip) - 1 + 1e-300), 0.0)

    # Thermal C_V: (epsilon^2 / T^2) * n * (1+n)
    # In k-space with 3D density of states: 4*pi*k^2*dk / (2*pi)^3
    integrand_thermal = (epsilon_k**2 / (kBT**2)) * n_BE * (1 + n_BE)
    C_V_thermal[i] = np.sum(integrand_thermal * k_phys**2 / (2 * np.pi**2)) * dk

    # Thermal energy at this T
    E_thermal[i] = np.sum(epsilon_k * n_BE * k_phys**2 / (2 * np.pi**2)) * dk

    # GGE "specific heat": what a thermometer sees
    # The GGE has fixed occupation n_k_GGE. When probed at temperature T,
    # the response function is:
    #   C_V_GGE(T) = sum_k (epsilon_k^2/T^2) * n_k_GGE * (1 + n_k_GGE)
    integrand_GGE = (epsilon_k**2 / (kBT**2)) * nk_strong * (1 + nk_strong)
    C_V_GGE[i] = np.sum(integrand_GGE * k_phys**2 / (2 * np.pi**2)) * dk

# ============================================================================
#  Step 4: Debye reference
# ============================================================================

# Debye temperature: T_D = hbar * c_s * k_D / k_B
# where k_D = (6 * pi^2 * n_0)^{1/3} (Debye cutoff)
k_D = (6 * np.pi**2 * n_0_BEC)**(1.0/3)
T_D = hbar_SI * c_s_BEC * k_D / k_B_SI

print(f"Debye parameters:")
print(f"  k_D = {k_D:.4e} m^{{-1}}")
print(f"  T_D = {T_D:.4e} K")
print(f"  T_eff / T_D = {T_eff_BEC / T_D:.4f}")
print()

# Debye C_V: C_V_Debye = (12*pi^4/5) * N * (T/T_D)^3 per unit volume
# For a 3D phonon gas with n_0 atoms:
# C_V_Debye(T) = n_0 * k_B * (12*pi^4/5) * (T/T_D)^3 * (V per atom = 1/n_0)
# = k_B * (12*pi^4/5) * (T/T_D)^3  per unit volume
C_V_Debye = k_B_SI * (12 * np.pi**4 / 5) * (T_scan / T_D)**3

# ============================================================================
#  Step 5: Deviation delta_CV
# ============================================================================

# delta_CV = (C_V_GGE - C_V_Debye) / C_V_Debye
# This measures the fractional excess/deficit from the Debye law due to
# the non-thermal GGE occupation.

# Also compute deviation relative to thermal:
# delta_CV_vs_thermal = (C_V_GGE - C_V_thermal) / C_V_thermal

# Avoid division by zero at very low T
with np.errstate(divide='ignore', invalid='ignore'):
    delta_CV_vs_Debye = np.where(
        C_V_Debye > 0,
        (C_V_GGE - C_V_Debye) / C_V_Debye,
        0.0
    )
    delta_CV_vs_thermal = np.where(
        C_V_thermal > 0,
        (C_V_GGE - C_V_thermal) / C_V_thermal,
        0.0
    )

# Find temperature of maximum GGE deviation
idx_max_dev = np.argmax(np.abs(delta_CV_vs_thermal))
T_max_dev = T_scan[idx_max_dev]
delta_CV_max = delta_CV_vs_thermal[idx_max_dev]

# Find the temperature range where |delta_CV_vs_thermal| > 10% (gate threshold)
mask_detectable = np.abs(delta_CV_vs_thermal) > 0.10
if np.any(mask_detectable):
    T_detect_min = T_scan[mask_detectable].min()
    T_detect_max = T_scan[mask_detectable].max()
    detection_range = True
else:
    T_detect_min = 0.0  # (local)
    T_detect_max = 0.0  # (local)
    detection_range = False

# Also check Debye deviation
idx_max_dev_debye = np.argmax(np.abs(delta_CV_vs_Debye))
T_max_dev_debye = T_scan[idx_max_dev_debye]
delta_CV_max_debye = delta_CV_vs_Debye[idx_max_dev_debye]

mask_detectable_debye = np.abs(delta_CV_vs_Debye) > 0.10
if np.any(mask_detectable_debye):
    T_detect_min_debye = T_scan[mask_detectable_debye].min()
    T_detect_max_debye = T_scan[mask_detectable_debye].max()
    detection_range_debye = True
else:
    T_detect_min_debye = 0.0  # (local)
    T_detect_max_debye = 0.0  # (local)
    detection_range_debye = False

# ============================================================================
#  Step 5b: Structural analysis — entropy and mode counting
# ============================================================================

# Number of GGE modes contributing
n_modes_GGE = np.sum(nk_strong > 0.01)
n_modes_total = len(k_phys)
frac_populated = n_modes_GGE / n_modes_total

# Energy partition
E_GGE_low = np.sum(epsilon_k[k_phys < 1/xi_f] * nk_strong[k_phys < 1/xi_f] *
                    k_phys[k_phys < 1/xi_f]**2 / (2*np.pi**2)) * dk
E_frac_low = E_GGE_low / E_GGE_total if E_GGE_total > 0 else 0

# Entropy of the GGE vs thermal at T_eff
# S_GGE = -sum_k [ n_k ln(n_k) - (1+n_k) ln(1+n_k) ]
with np.errstate(divide='ignore', invalid='ignore'):
    nk_pos = np.where(nk_strong > 1e-10, nk_strong, 1e-10)
    S_GGE_density = np.sum(
        ((1 + nk_pos) * np.log(1 + nk_pos) - nk_pos * np.log(nk_pos)) *
        k_phys**2 / (2 * np.pi**2)
    ) * dk

# Thermal entropy at T_eff
kBT_eff = k_B_SI * T_eff_BEC
x_eff = epsilon_k / kBT_eff
x_clip_eff = np.clip(x_eff, 0, 500)
n_BE_eff = np.where(x_clip_eff < 500, 1.0 / (np.exp(x_clip_eff) - 1 + 1e-300), 0.0)
n_BE_pos = np.where(n_BE_eff > 1e-10, n_BE_eff, 1e-10)
S_thermal_density = np.sum(
    ((1 + n_BE_pos) * np.log(1 + n_BE_pos) - n_BE_pos * np.log(n_BE_pos)) *
    k_phys**2 / (2 * np.pi**2)
) * dk

S_ratio = S_GGE_density / S_thermal_density if S_thermal_density > 0 else 0

print("=" * 72)
print("RESULTS")
print("=" * 72)
print()
print(f"T_eff_BEC          = {T_eff_BEC:.4e} K")
print(f"T_Debye            = {T_D:.4e} K")
print(f"T_eff / T_D        = {T_eff_BEC / T_D:.6f}")
print()

# --- Physically meaningful deviation at T ~ T_eff ---
# The key experimental signature: at temperatures near T_eff, the GGE
# specific heat DIFFERS from what a thermal state at the same T would give.
# Below T_eff, the frozen GGE occupation produces much larger C_V than thermal
# (because thermal n_k -> 0 but GGE n_k stays finite). This is the signature.
#
# The Debye comparison diverges at low T because Debye ~ T^3 -> 0
# while the GGE maintains finite occupation. The meaningful comparison
# is the RATIO at T = T_eff itself, and the functional form C_V(T).

# Evaluate at T = T_eff
idx_Teff = np.argmin(np.abs(T_scan - T_eff_BEC))
delta_at_Teff_thermal = delta_CV_vs_thermal[idx_Teff]
delta_at_Teff_debye = delta_CV_vs_Debye[idx_Teff]

# Evaluate at T = T_D
idx_TD = np.argmin(np.abs(T_scan - T_D))
delta_at_TD_thermal = delta_CV_vs_thermal[idx_TD]
delta_at_TD_debye = delta_CV_vs_Debye[idx_TD]

# Find deviation in the EXPERIMENTAL regime: T in [0.5*T_eff, 2*T_eff]
mask_expt = (T_scan > 0.5 * T_eff_BEC) & (T_scan < 2.0 * T_eff_BEC)
if np.any(mask_expt):
    delta_expt_max_thermal = np.max(np.abs(delta_CV_vs_thermal[mask_expt]))
    delta_expt_max_debye = np.max(np.abs(delta_CV_vs_Debye[mask_expt]))
    delta_expt_mean_thermal = np.mean(np.abs(delta_CV_vs_thermal[mask_expt]))
else:
    delta_expt_max_thermal = 0.0  # (local)
    delta_expt_max_debye = 0.0  # (local)
    delta_expt_mean_thermal = 0.0  # (local)

print(f"--- Deviation at T = T_eff ({T_eff_BEC:.3e} K) ---")
print(f"  C_V_GGE / C_V_thermal  = {C_V_GGE[idx_Teff] / C_V_thermal[idx_Teff]:.4f}" if C_V_thermal[idx_Teff] > 0 else "  C_V_thermal = 0")
print(f"  delta_CV (vs thermal)  = {delta_at_Teff_thermal:.4f} ({100*delta_at_Teff_thermal:.2f}%)")
print(f"  delta_CV (vs Debye)    = {delta_at_Teff_debye:.4e}")
print()
print(f"--- Deviation at T = T_D ({T_D:.3e} K) ---")
print(f"  C_V_GGE / C_V_thermal  = {C_V_GGE[idx_TD] / C_V_thermal[idx_TD]:.4f}" if C_V_thermal[idx_TD] > 0 else "  C_V_thermal = 0")
print(f"  delta_CV (vs thermal)  = {delta_at_TD_thermal:.4f} ({100*delta_at_TD_thermal:.2f}%)")
print()
print(f"--- Experimental regime [0.5*T_eff, 2*T_eff] ---")
print(f"  max |delta_CV| (vs thermal) = {delta_expt_max_thermal:.4f} ({100*delta_expt_max_thermal:.2f}%)")
print(f"  max |delta_CV| (vs Debye)   = {delta_expt_max_debye:.4e}")
print(f"  mean |delta_CV| (vs thermal) = {delta_expt_mean_thermal:.4f} ({100*delta_expt_mean_thermal:.2f}%)")
print()

# The GGE has LOWER entropy than thermal at same energy. This means
# the C_V response function is different: the GGE has modes locked at
# occupation n_plateau, which respond to temperature differently than
# a thermal distribution. The signature is:
#
# 1. At T < T_eff: C_V_GGE >> C_V_thermal (frozen modes contribute while
#    thermal modes are exponentially suppressed)
# 2. At T ~ T_eff: C_V_GGE differs by the entropy deficit factor
# 3. At T >> T_eff: Both approach classical limit, difference vanishes
#
# This is exactly the pattern seen in superfluid 3He after a rapid
# quench (Volovik Paper 25, Sec V): the non-thermal quasiparticle
# distribution produces a specific heat anomaly at T ~ T_c.

print(f"--- Full range summary ---")
print(f"  max |delta_CV| (vs thermal, all T) = {np.max(np.abs(delta_CV_vs_thermal)):.4f}")
print(f"  at T = {T_scan[np.argmax(np.abs(delta_CV_vs_thermal))]:.4e} K")
print()
print(f"  Entropy ratio S_GGE/S_thermal at T_eff:")
print(f"  S_GGE / S_thermal = {S_ratio:.4f}")
print(f"  --> GGE has {(1-S_ratio)*100:.1f}% LESS entropy than thermal at same energy")
print(f"  --> This entropy deficit drives the C_V departure")

print()
print(f"--- Structural analysis ---")
print(f"  GGE modes populated (n_k > 0.01): {n_modes_GGE} / {n_modes_total}")
print(f"  Fraction populated:  {frac_populated:.4f}")
print(f"  E_GGE (k < 1/xi):   {E_frac_low:.4f} of total (low-k fraction)")
print(f"  S_GGE / S_thermal:   {S_ratio:.4f} (entropy ratio at T_eff)")
print()

# ============================================================================
#  Step 7: Gate verdict
# ============================================================================

gate_name = "GGE-HAWKING-ANALOG-71"

# Gate criterion: INFO. If delta_CV > 10%, experimentally accessible.
# Use the experimental regime deviation, not the low-T divergence
experimentally_accessible = delta_expt_max_thermal > 0.10

if experimentally_accessible:
    gate_detail = (
        f"delta_CV(T_eff, vs thermal)={delta_at_Teff_thermal:.4f} ({100*np.abs(delta_at_Teff_thermal):.1f}%). "
        f"delta_CV(expt regime max, vs thermal)={delta_expt_max_thermal:.4f} ({100*delta_expt_max_thermal:.1f}%). "
        f"T_eff_BEC={T_eff_BEC:.3e} K. T_D={T_D:.3e} K. T_eff/T_D={T_eff_BEC/T_D:.3f}. "
        f"S_GGE/S_thermal={S_ratio:.4f} ({(1-S_ratio)*100:.1f}% entropy deficit). "
        f"n_plateau={n_plat_strong:.3f}. Mach={Mach_BEC:.2f}. "
        f"EXPERIMENTALLY ACCESSIBLE: GGE C_V signature exceeds 10% in [0.5,2]*T_eff."
    )
else:
    gate_detail = (
        f"delta_CV(T_eff, vs thermal)={delta_at_Teff_thermal:.4f} ({100*np.abs(delta_at_Teff_thermal):.1f}%). "
        f"delta_CV(expt regime max, vs thermal)={delta_expt_max_thermal:.4f} ({100*delta_expt_max_thermal:.1f}%). "
        f"T_eff_BEC={T_eff_BEC:.3e} K. T_D={T_D:.3e} K. T_eff/T_D={T_eff_BEC/T_D:.3f}. "
        f"S_GGE/S_thermal={S_ratio:.4f} ({(1-S_ratio)*100:.1f}% entropy deficit). "
        f"n_plateau={n_plat_strong:.3f}. Mach={Mach_BEC:.2f}. "
        f"Below 10% threshold in experimental regime. Signature exists but is challenging."
    )

gate_verdict = "INFO"

print("=" * 72)
print(f"Gate: {gate_name}")
print(f"Verdict: {gate_verdict}")
print(f"Detail: {gate_detail}")
print("=" * 72)

# ============================================================================
#  Step 8: Save results
# ============================================================================

np.savez(
    os.path.join(os.path.dirname(__file__), 's71_gge_hawking_analog.npz'),
    # Gate metadata
    gate_name=gate_name,
    gate_verdict=gate_verdict,
    gate_detail=gate_detail,
    # BEC parameters
    c_s_BEC=c_s_BEC,
    xi_f=xi_f,
    Mach_BEC=Mach_BEC,
    n_0_BEC=n_0_BEC,
    T_eff_BEC=T_eff_BEC,
    T_Debye=T_D,
    k_D=k_D,
    dt_Q=dt_Q,
    T_max_BEC=T_max_BEC,
    n_plateau_strong=n_plat_strong,
    # Temperature scan
    T_scan=T_scan,
    T_over_TD=T_scan / T_D,
    # Specific heat arrays
    C_V_thermal=C_V_thermal,
    C_V_GGE=C_V_GGE,
    C_V_Debye=C_V_Debye,
    # Deviations
    delta_CV_vs_Debye=delta_CV_vs_Debye,
    delta_CV_vs_thermal=delta_CV_vs_thermal,
    delta_CV_max_debye=delta_CV_max_debye,
    delta_CV_max_thermal=delta_CV_max,
    T_max_dev_debye=T_max_dev_debye,
    T_max_dev_thermal=T_max_dev,
    # Detection range
    experimentally_accessible=experimentally_accessible,
    T_detect_min_debye=T_detect_min_debye,
    T_detect_max_debye=T_detect_max_debye,
    T_detect_min_thermal=T_detect_min if detection_range else 0.0,
    T_detect_max_thermal=T_detect_max if detection_range else 0.0,
    # Experimental regime deviations
    delta_at_Teff_thermal=delta_at_Teff_thermal,
    delta_at_Teff_debye=delta_at_Teff_debye,
    delta_at_TD_thermal=delta_at_TD_thermal,
    delta_expt_max_thermal=delta_expt_max_thermal,
    delta_expt_max_debye=delta_expt_max_debye,
    delta_expt_mean_thermal=delta_expt_mean_thermal,
    # Structural
    S_ratio_GGE_thermal=S_ratio,
    E_GGE_total=E_GGE_total,
    E_frac_low_k=E_frac_low,
    n_modes_GGE=n_modes_GGE,
    frac_populated=frac_populated,
    # Framework parameters used
    T_compound_MKK=T_compound,
    c_fabric_MKK=c_fabric,
    Mach_framework=Mach_framework,
)

print()
print(f"Data saved: computations/session-71/s71_gge_hawking_analog.npz")
print("DONE")
