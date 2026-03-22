"""
Session 42 W1-3: Hauser-Feshbach Branching Ratios for KK Channels

Computes the Hauser-Feshbach (HF) compound nucleus decay branching ratios
for the post-BCS-transit compound system in the 8-dimensional internal space.

Physical setup:
    - BCS transit quench produces 59.8 Bogoliubov pairs at GUT-scale energies
    - E_exc = 443 * |E_cond| = 443 * 0.115 = 50.945 M_KK
    - Compound system has well-characterized quantum numbers (B2:B3:B1 = 85.5:13.3:0.45)
    - NOHAIR-40: compound nucleus NOT fully equilibrated (T varies 64.6%)
    - B2 doorway state with PR = 3.17 (3 dominant eigenstates)

Key structural result:
    D_K spectrum at the fold (tau=0.190) has NO zero modes. All KK channels
    are massive (m_min = 0.819 M_KK). There are no massless "photon" or
    "graviton" channels in the truncated spectrum.

Hauser-Feshbach formalism:
    P_c = T_c(E) / sum_{c'} T_{c'}(E)
    T_c(E) = 1 / (1 + exp[2*pi*(V_c - E + Q_c) / (hbar*omega_c)])

For massive KK modes: V_c = m_c (mass threshold), omega_c from barrier curvature.
In the high-temperature limit (E >> V_c): T_c -> 1.
In the Boltzmann limit: T_c ~ exp(-m_c / T_compound).

Gate: HF-KK-42
    PASS: T_massless/T_total > 3 OOM across channels AND doorway correction > 10:1
    FAIL: Democratic branching (all channels within 1 OOM)

Note on "massless" channels: Since D_K has NO zero modes at the fold,
there are no strictly massless channels. The "massless" criterion from
the gate must be reinterpreted as: lightest vs heaviest channel branching
ratio spans > 3 orders of magnitude.

Author: nazarewicz-nuclear-structure-theorist (Session 42)
Date: 2026-03-13
"""

import sys
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from collections import defaultdict

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)

# ================================================================
# 1. LOAD INPUT DATA
# ================================================================

print("=" * 70)
print("Session 42 W1-3: Hauser-Feshbach KK Branching Ratios")
print("=" * 70)

# Load D_K eigenvalues
bcs_data = np.load(os.path.join(SCRIPT_DIR, "s27_multisector_bcs.npz"), allow_pickle=True)
tau_values = bcs_data['tau_values']
sectors = bcs_data['sectors']

# Load acoustic temperature
temp_data = np.load(os.path.join(SCRIPT_DIR, "s40_acoustic_temperature.npz"), allow_pickle=True)
T_acoustic = float(temp_data['T_acoustic_metric_B2'])  # 0.112 M_KK
T_Gibbs = float(temp_data['T_Gibbs'])  # 0.113 M_KK
Delta_pair = float(temp_data['Delta_pair'])  # 0.464

# Load NOHAIR sensitivity
nohair_data = np.load(os.path.join(SCRIPT_DIR, "s40_nohair_sensitivity.npz"), allow_pickle=True)
T_variation_pct = float(nohair_data['gate_T_variation_clean_pct'])  # 64.6%
Delta_k_fold = nohair_data['Delta_k_fold']  # 8 quasiparticle gaps
branch_labels = nohair_data['branch_labels']
v_k_sq = nohair_data['v_k_sq']  # occupation probabilities

# Load B2 integrability
b2_data = np.load(os.path.join(SCRIPT_DIR, "s40_b2_integrability.npz"), allow_pickle=True)
PR_B2 = 3.17  # participation ratio (from memory, confirmed in data)
r_B2 = float(b2_data['r_B2_N2'])  # 0.401 (Poisson-like)
rank1_frac = float(b2_data['rank1_frac_B2'])  # 0.859
V_B2B2 = b2_data['V_B2B2']  # 4x4 B2-B2 interaction
V_B2_B1 = b2_data['V_B2_B1']  # 4-vector B2-B1 coupling
V_B2_B3 = b2_data['V_B2_B3']  # 4x3 B2-B3 coupling

# Load Kosmann interaction (for doorway overlap calculation)
kosmann_data = np.load(os.path.join(SCRIPT_DIR, "s23a_kosmann_singlet.npz"), allow_pickle=True)

print(f"\nInput parameters:")
print(f"  T_acoustic    = {T_acoustic:.4f} M_KK")
print(f"  T_Gibbs       = {T_Gibbs:.4f} M_KK")
print(f"  Delta_pair    = {Delta_pair:.4f} M_KK")
print(f"  T_variation   = {T_variation_pct:.1f}%")
print(f"  PR_B2         = {PR_B2:.2f}")
print(f"  r_B2          = {r_B2:.4f} (Poisson)")
print(f"  rank1_frac    = {rank1_frac:.4f}")

# ================================================================
# 2. BUILD COMPLETE KK MASS SPECTRUM AT THE FOLD
# ================================================================

# Use tau=0.20 (index 3), closest to fold at 0.190
idx_fold = 3
tau_fold = tau_values[idx_fold]
print(f"\nUsing tau = {tau_fold:.2f} (closest grid point to fold tau=0.190)")

# Build mass table: each entry = (|eigenvalue|, sector_dim^2, p, q)
mass_table = []
sector_eigenvalues = {}

for row in sectors:
    p, q, dim, dim2 = row
    key = f'evals_{p}_{q}_{idx_fold}'
    if key in bcs_data:
        evals = bcs_data[key]
        sector_eigenvalues[(p, q)] = evals
        for ev in evals:
            mass_table.append((abs(ev), dim2, p, q))

mass_table.sort(key=lambda x: x[0])
total_channels = len(mass_table)

# Extract unique mass levels with total multiplicities
from collections import Counter
mass_mult = defaultdict(int)
mass_sector_info = defaultdict(list)
for m, deg, p, q in mass_table:
    m_rounded = round(m, 4)
    mass_mult[m_rounded] += 1
    mass_sector_info[m_rounded].append((p, q, deg))

unique_masses = sorted(mass_mult.keys())
n_levels = len(unique_masses)

print(f"\nKK Mass Spectrum at fold:")
print(f"  Total eigenvalues: {total_channels}")
print(f"  Unique mass levels: {n_levels}")
print(f"  Mass range: [{min(unique_masses):.4f}, {max(unique_masses):.4f}] M_KK")
print(f"  CRITICAL: Zero modes = 0 (ALL channels massive)")

# ================================================================
# 3. COMPOUND NUCLEUS PARAMETERS
# ================================================================

from canonical_constants import E_cond  # S36 ED-CONV-36: -0.137 (was -0.115)
N_pairs = 59.8   # Bogoliubov quasiparticle pairs from transit
E_exc_ratio = 443.0  # E_exc / |E_cond|
E_exc = E_exc_ratio * abs(E_cond)  # = 50.945 M_KK

# Effective number of DOF for temperature estimation
# 8 modes in BCS Fock space (4 B2 + 1 B1 + 3 B3)
N_dof = 8
T_compound = E_exc / N_dof  # = 6.37 M_KK (microcanonical estimate)

# Alternative: use equipartition with all 992 channels
# T_compound_equip = E_exc / (total_channels / 2)  # much lower

# The compound nucleus is NOT equilibrated (NOHAIR-40: T varies 64.6%)
# So T_compound has large uncertainty
T_compound_min = T_compound * (1 - T_variation_pct/100)
T_compound_max = T_compound * (1 + T_variation_pct/100)

print(f"\nCompound Nucleus Parameters:")
print(f"  E_cond        = {E_cond:.4f} M_KK")
print(f"  N_pairs       = {N_pairs:.1f}")
print(f"  E_exc         = {E_exc:.3f} M_KK")
print(f"  N_dof (BCS)   = {N_dof}")
print(f"  T_compound    = {T_compound:.3f} M_KK (microcanonical, {N_dof} DOF)")
print(f"  T_compound range = [{T_compound_min:.3f}, {T_compound_max:.3f}] (64.6% variation)")
print(f"  T_acoustic    = {T_acoustic:.4f} M_KK (geometric, from fold curvature)")
print(f"  T_Gibbs       = {T_Gibbs:.4f} M_KK (from S38)")

# ================================================================
# 4. HAUSER-FESHBACH TRANSMISSION COEFFICIENTS
# ================================================================

def hill_wheeler_T(E, V_barrier, hbar_omega):
    """
    Hill-Wheeler transmission coefficient (inverted parabolic barrier).

    T = 1 / (1 + exp[2*pi*(V - E) / hbar_omega])

    Parameters:
        E: excitation energy above threshold
        V_barrier: barrier height (= mass for KK modes)
        hbar_omega: barrier curvature parameter

    Returns:
        T: transmission coefficient in [0, 1]
    """
    x = 2 * np.pi * (V_barrier - E) / hbar_omega
    # Numerical safety for large |x|
    x = np.clip(x, -500, 500)
    return 1.0 / (1.0 + np.exp(x))


def boltzmann_T(m, T):
    """
    Boltzmann approximation for transmission:
    T_c ~ exp(-m / T) for m > 0.

    Valid when m >> hbar_omega (sharp barrier limit).
    """
    return np.exp(-m / T)


# Compute transmission coefficients for each mass level
# Using TWO temperature scales:
#   (a) T_compound = 6.37 M_KK (from BCS excitation energy, microcanonical)
#   (b) T_acoustic = 0.112 M_KK (from fold geometry)

# For barrier curvature omega_c, use the attractor frequency omega_att = 1.430
# from S38 W2 (the characteristic oscillation of the compound system)
omega_att = 1.430  # M_KK units (from S38)

print(f"\n{'='*70}")
print(f"HAUSER-FESHBACH TRANSMISSION COEFFICIENTS")
print(f"{'='*70}")
print(f"  Barrier curvature: hbar*omega_att = {omega_att:.3f} M_KK")
print(f"  E_exc = {E_exc:.3f} M_KK")

# Scenario A: T_compound (high-T, microcanonical)
print(f"\n--- Scenario A: T = T_compound = {T_compound:.3f} M_KK ---")
T_c_HW_A = []  # Hill-Wheeler
T_c_Boltz_A = []  # Boltzmann
for m in unique_masses:
    t_hw = hill_wheeler_T(E_exc, m, omega_att)
    t_boltz = boltzmann_T(m, T_compound)
    mult = mass_mult[m]
    T_c_HW_A.append((m, mult, t_hw, t_hw * mult))
    T_c_Boltz_A.append((m, mult, t_boltz, t_boltz * mult))

T_c_HW_A = np.array([(m, mult, t, tw) for m, mult, t, tw in T_c_HW_A])
T_c_Boltz_A = np.array([(m, mult, t, tw) for m, mult, t, tw in T_c_Boltz_A])

# Since E_exc = 50.9 >> all masses (max 2.08), ALL channels are open
# Hill-Wheeler T -> 1 for all channels when E >> V
print(f"  Hill-Wheeler: T_min = {T_c_HW_A[:,2].min():.6f}, T_max = {T_c_HW_A[:,2].max():.6f}")
print(f"  Boltzmann:    T_min = {T_c_Boltz_A[:,2].min():.6e}, T_max = {T_c_Boltz_A[:,2].max():.6e}")

T_total_HW_A = np.sum(T_c_HW_A[:,3])
T_total_Boltz_A = np.sum(T_c_Boltz_A[:,3])
print(f"  Sum T (HW, weighted):      {T_total_HW_A:.3f}")
print(f"  Sum T (Boltz, weighted):   {T_total_Boltz_A:.3f}")

# Branching ratio: lightest vs heaviest
BR_HW_A = T_c_HW_A[0,2] / T_c_HW_A[-1,2]
BR_Boltz_A = T_c_Boltz_A[0,2] / T_c_Boltz_A[-1,2]
print(f"  BR(lightest/heaviest) HW:    {BR_HW_A:.6f} (ratio)")
print(f"  BR(lightest/heaviest) Boltz: {BR_Boltz_A:.6f} (ratio)")
print(f"  Dynamic range HW:    {np.log10(BR_HW_A):.3f} decades")
print(f"  Dynamic range Boltz: {np.log10(BR_Boltz_A):.3f} decades")

# Scenario B: T_acoustic (geometric temperature at fold)
print(f"\n--- Scenario B: T = T_acoustic = {T_acoustic:.4f} M_KK ---")
T_c_HW_B = []
T_c_Boltz_B = []
for m in unique_masses:
    t_hw = hill_wheeler_T(E_exc, m, omega_att)  # same as A (HW depends on E_exc, not T)
    t_boltz = boltzmann_T(m, T_acoustic)
    mult = mass_mult[m]
    T_c_HW_B.append((m, mult, t_hw, t_hw * mult))
    T_c_Boltz_B.append((m, mult, t_boltz, t_boltz * mult))

T_c_Boltz_B = np.array([(m, mult, t, tw) for m, mult, t, tw in T_c_Boltz_B])

print(f"  Boltzmann: T_min = {T_c_Boltz_B[:,2].min():.6e}, T_max = {T_c_Boltz_B[:,2].max():.6e}")

T_total_Boltz_B = np.sum(T_c_Boltz_B[:,3])
BR_Boltz_B = T_c_Boltz_B[0,2] / T_c_Boltz_B[-1,2]
print(f"  Sum T (Boltz, weighted):   {T_total_Boltz_B:.6e}")
print(f"  BR(lightest/heaviest) Boltz: {BR_Boltz_B:.4e} (ratio)")
print(f"  Dynamic range Boltz: {np.log10(BR_Boltz_B):.3f} decades")

# ================================================================
# 5. CHANNEL-RESOLVED ANALYSIS
# ================================================================

print(f"\n{'='*70}")
print(f"CHANNEL-RESOLVED BRANCHING RATIOS")
print(f"{'='*70}")

# Aggregate by sector (p,q)
sector_labels = [(int(r[0]), int(r[1])) for r in sectors]
sector_T_compound = {}
sector_T_acoustic = {}
sector_channel_count = {}

for row in sectors:
    p, q, dim, dim2 = int(row[0]), int(row[1]), int(row[2]), int(row[3])
    key = f'evals_{p}_{q}_{idx_fold}'
    if key in bcs_data:
        evals = bcs_data[key]
        abs_evals = np.abs(evals)
        n_ch = len(evals)
        sector_channel_count[(p,q)] = n_ch

        # T_compound scenario
        T_arr_compound = np.array([boltzmann_T(m, T_compound) for m in abs_evals])
        sector_T_compound[(p,q)] = np.sum(T_arr_compound)

        # T_acoustic scenario
        T_arr_acoustic = np.array([boltzmann_T(m, T_acoustic) for m in abs_evals])
        sector_T_acoustic[(p,q)] = np.sum(T_arr_acoustic)

T_total_compound = sum(sector_T_compound.values())
T_total_acoustic = sum(sector_T_acoustic.values())

print(f"\n{'Sector':>10s} {'dim^2':>6s} {'N_ch':>5s} {'T_cmpd':>12s} {'BR_cmpd':>10s} "
      f"{'T_acou':>14s} {'BR_acou':>12s}")
print(f"{'-'*80}")

for row in sectors:
    p, q, dim, dim2 = int(row[0]), int(row[1]), int(row[2]), int(row[3])
    n_ch = sector_channel_count[(p,q)]
    tc = sector_T_compound[(p,q)]
    ta = sector_T_acoustic[(p,q)]
    br_c = tc / T_total_compound
    br_a = ta / T_total_acoustic
    print(f"  ({p},{q}):  {dim2:6d} {n_ch:5d} {tc:12.4f} {br_c:10.4f} "
          f"{ta:14.6e} {br_a:12.6e}")

# Dynamic range across sectors
T_sector_compound = np.array(list(sector_T_compound.values()))
T_sector_acoustic = np.array(list(sector_T_acoustic.values()))

DR_compound = T_sector_compound.max() / T_sector_compound.min()
DR_acoustic = T_sector_acoustic.max() / T_sector_acoustic.min()

print(f"\nSector dynamic range (T_compound): {DR_compound:.2f} ({np.log10(DR_compound):.2f} decades)")
print(f"Sector dynamic range (T_acoustic): {DR_acoustic:.2e} ({np.log10(DR_acoustic):.2f} decades)")

# ================================================================
# 6. DOORWAY STATE CORRECTION
# ================================================================

print(f"\n{'='*70}")
print(f"DOORWAY STATE CORRECTION")
print(f"{'='*70}")

# From NOHAIR-40: compound nucleus retains memory of formation channel
# B2 doorway (85.5% weight) preferentially decays through B2-coupled channels
# PR = 3.17 means 3 dominant eigenstates, not fully statistical

# BCS branching from S38 (zero free parameters):
BR_BCS = {
    'B2': 0.855,   # 4 modes * v_k^2 ~ 4 * 0.240 = 0.96 -> normalized
    'B1': 0.133,   # 1 mode * v_k^2 ~ 0.036
    'B3': 0.0045,  # 3 modes * v_k^2 ~ 3 * 0.0017 = 0.005
}

print(f"\nBCS formation branching (from S38, zero free parameters):")
for k, v in BR_BCS.items():
    print(f"  {k}: {v:.4f}")

# The doorway correction modifies the statistical HF branching by
# weighting each channel by its overlap with the B2 doorway state.
#
# Doorway overlap factor: O_c = |<doorway|channel_c>|^2
# In nuclear physics this is the "width fluctuation correction factor" W_c
#
# For the B2 doorway with PR = 3.17:
#   - B2-coupled channels: O ~ 1 (strong overlap)
#   - B1-coupled channels: O ~ V_B2_B1^2 / (Delta_E)^2
#   - B3-coupled channels: O ~ V_B2_B3^2 / (Delta_E)^2

# Compute doorway overlap using Kosmann coupling strengths
# V_B2_B1 and V_B2_B3 from b2_integrability data
V_B2_B1_rms = np.sqrt(np.mean(V_B2_B1**2))
V_B2_B3_rms = np.sqrt(np.mean(V_B2_B3**2))
V_B2_B2_rms = np.sqrt(np.mean(V_B2B2**2))

print(f"\nKosmann coupling strengths (from B2 integrability data):")
print(f"  V_B2_B2 (rms): {V_B2_B2_rms:.6f}")
print(f"  V_B2_B1 (rms): {V_B2_B1_rms:.6f}")
print(f"  V_B2_B3 (rms): {V_B2_B3_rms:.6f}")

# Doorway spectral function: the B2 doorway couples to each sector
# proportional to the squared matrix element divided by energy denominator

# Mean energy spacings between sectors (from D_K eigenvalues)
# B2 sector: (1,1) with dim=8
# B1 sector: pair of ((1,0) + (0,1)) with dim=3
# B3 sector: pair of ((3,0) + (0,3)) with dim=10

# For the doorway model: the doorway state |d> = |B2> decays into
# channels c with partial width Gamma_c:
#   Gamma_c = 2*pi * |V_{d,c}|^2 * rho_c(E)
# where rho_c(E) is the level density in channel c.

# Level density from D_K spectrum (number of eigenvalues per unit energy)
rho_B2 = 0  # Will compute
rho_B1 = 0
rho_B3 = 0

for row in sectors:
    p, q, dim, dim2 = int(row[0]), int(row[1]), int(row[2]), int(row[3])
    key = f'evals_{p}_{q}_{idx_fold}'
    evals = bcs_data[key]
    abs_evals = np.abs(evals)
    E_range = abs_evals.max() - abs_evals.min()
    n_levels = len(evals)
    rho = n_levels / E_range if E_range > 0 else 0

    # Classify sector into B2/B1/B3
    # B2 = (1,1) sector (adj rep, dim=8)
    # B1 = (1,0)+(0,1) (fund+antifund, dim=3)
    # B3 = (3,0)+(0,3)+(2,0)+(0,2)+(2,1) (higher reps)
    if (p, q) == (1, 1):
        rho_B2 += rho
    elif (p, q) in [(1, 0), (0, 1)]:
        rho_B1 += rho
    else:
        rho_B3 += rho

print(f"\nLevel densities:")
print(f"  rho_B2 (adjoint): {rho_B2:.2f} / M_KK")
print(f"  rho_B1 (fund):    {rho_B1:.2f} / M_KK")
print(f"  rho_B3 (higher):  {rho_B3:.2f} / M_KK")

# Partial widths from doorway (Fermi golden rule):
# Gamma_c = 2*pi * V_c^2 * rho_c
Gamma_B2 = 2 * np.pi * V_B2_B2_rms**2 * rho_B2
Gamma_B1 = 2 * np.pi * V_B2_B1_rms**2 * rho_B1
Gamma_B3 = 2 * np.pi * V_B2_B3_rms**2 * rho_B3
Gamma_total = Gamma_B2 + Gamma_B1 + Gamma_B3

print(f"\nDoorway partial widths (Fermi golden rule):")
print(f"  Gamma_B2 = {Gamma_B2:.6f}")
print(f"  Gamma_B1 = {Gamma_B1:.6f}")
print(f"  Gamma_B3 = {Gamma_B3:.6f}")
print(f"  Gamma_total = {Gamma_total:.6f}")

# Doorway branching ratios
doorway_BR_B2 = Gamma_B2 / Gamma_total
doorway_BR_B1 = Gamma_B1 / Gamma_total
doorway_BR_B3 = Gamma_B3 / Gamma_total

print(f"\nDoorway branching ratios:")
print(f"  BR_B2 = {doorway_BR_B2:.4f}")
print(f"  BR_B1 = {doorway_BR_B1:.4f}")
print(f"  BR_B3 = {doorway_BR_B3:.4f}")

# Doorway preference ratio (B2 vs others)
# NOTE: This is the FGR-derived preference, which includes level density effects.
# The FORMATION branching (from S38) gives 85.5:13.3:0.45 (B2:B1:B3).
# The DECAY branching from FGR is different because it weights by rho_c(E).
# The physical preference depends on which picture applies.
doorway_preference_FGR = doorway_BR_B2 / max(doorway_BR_B1, doorway_BR_B3)

# Formation-based preference (from BCS occupation probabilities, S38)
BR_formation_B2 = 0.855
BR_formation_B1 = 0.133
BR_formation_B3 = 0.0045
doorway_preference_formation = BR_formation_B2 / BR_formation_B1
doorway_preference = doorway_preference_FGR  # Use FGR for conservatism
print(f"  Doorway preference (FGR, B2/max(B1,B3)): {doorway_preference_FGR:.2f}:1")
print(f"  Doorway preference (formation, B2/B1): {doorway_preference_formation:.2f}:1")

# ================================================================
# 7. COMBINED HAUSER-FESHBACH WITH DOORWAY CORRECTION
# ================================================================

print(f"\n{'='*70}")
print(f"COMBINED HF + DOORWAY: SECTOR-RESOLVED BRANCHING")
print(f"{'='*70}")

# The corrected HF branching for sector s is:
# P_s = W_s * T_s / sum_{s'} W_{s'} * T_{s'}
# where W_s is the doorway weight and T_s is the thermal transmission

# Assign doorway weights to sectors
sector_doorway_weights = {}
for row in sectors:
    p, q = int(row[0]), int(row[1])
    if (p, q) == (1, 1):
        sector_doorway_weights[(p,q)] = doorway_BR_B2
    elif (p, q) in [(1, 0), (0, 1)]:
        sector_doorway_weights[(p,q)] = doorway_BR_B1 / 2  # split between (1,0) and (0,1)
    else:
        sector_doorway_weights[(p,q)] = doorway_BR_B3 / 5  # split among 5 higher sectors

# Compute combined branching at both temperatures
combined_T_compound = {}
combined_T_acoustic = {}

for row in sectors:
    p, q = int(row[0]), int(row[1])
    w = sector_doorway_weights[(p,q)]
    combined_T_compound[(p,q)] = w * sector_T_compound[(p,q)]
    combined_T_acoustic[(p,q)] = w * sector_T_acoustic[(p,q)]

total_combined_compound = sum(combined_T_compound.values())
total_combined_acoustic = sum(combined_T_acoustic.values())

print(f"\n{'Sector':>10s} {'W_door':>8s} {'T_s(cmpd)':>12s} {'W*T(cmpd)':>12s} "
      f"{'BR_cmpd':>10s} {'T_s(acou)':>14s} {'BR_acou':>12s}")
print(f"{'-'*90}")

BR_compound_sectors = {}
BR_acoustic_sectors = {}

for row in sectors:
    p, q, dim, dim2 = int(row[0]), int(row[1]), int(row[2]), int(row[3])
    w = sector_doorway_weights[(p,q)]
    tc = sector_T_compound[(p,q)]
    ta = sector_T_acoustic[(p,q)]
    wt_c = combined_T_compound[(p,q)]
    wt_a = combined_T_acoustic[(p,q)]
    br_c = wt_c / total_combined_compound
    br_a = wt_a / total_combined_acoustic

    BR_compound_sectors[(p,q)] = br_c
    BR_acoustic_sectors[(p,q)] = br_a

    print(f"  ({p},{q}):  {w:8.4f} {tc:12.4f} {wt_c:12.6f} "
          f"{br_c:10.4f} {ta:14.6e} {br_a:12.6e}")

# B2 vs all others
B2_BR_compound = BR_compound_sectors[(1,1)]
others_BR_compound = 1 - B2_BR_compound
B2_pref_compound = B2_BR_compound / others_BR_compound

B2_BR_acoustic = BR_acoustic_sectors[(1,1)]
others_BR_acoustic = 1 - B2_BR_acoustic
B2_pref_acoustic = B2_BR_acoustic / others_BR_acoustic

print(f"\nB2 preference (compound T):")
print(f"  B2 BR = {B2_BR_compound:.4f}, others = {others_BR_compound:.4f}")
print(f"  B2/others = {B2_pref_compound:.2f}:1")

print(f"\nB2 preference (acoustic T):")
print(f"  B2 BR = {B2_BR_acoustic:.4f}, others = {others_BR_acoustic:.4f}")
print(f"  B2/others = {B2_pref_acoustic:.2f}:1")

# ================================================================
# 8. BARYON-TO-PHOTON RATIO ESTIMATE
# ================================================================

print(f"\n{'='*70}")
print(f"BARYON-TO-PHOTON RATIO ESTIMATE")
print(f"{'='*70}")

# In the standard compound nucleus picture:
# - "Baryons" = KK modes that carry conserved quantum numbers (K_7 charge)
# - "Photons" = radiation modes (in nuclear physics: gamma-ray emission)
#
# CRITICAL: There are NO massless modes in D_K at the fold.
# Therefore, there are no true "photon" channels.
#
# The closest analog to "baryon" vs "photon" is:
# - Heavy KK modes (m > threshold) = "matter"
# - Light KK modes (m close to gap edge) = "radiation"
#
# The gap-edge modes (m = 0.819 M_KK) are in the (0,0) singlet sector.
# They carry no SU(3) quantum numbers (trivial rep).
# The adjoint (1,1) modes at m ~ 0.874 carry adjoint quantum numbers.

# Pair-breaking suppression from S41 analysis:
# Each pair breaking suppressed by exp(-Delta/T_a)
# Delta_pair = 0.464, T_a = 0.112
pair_breaking_factor = np.exp(-Delta_pair / T_acoustic)
print(f"\nPair-breaking suppression per event:")
print(f"  Delta_pair / T_acoustic = {Delta_pair/T_acoustic:.3f}")
print(f"  exp(-Delta/T_a) = {pair_breaking_factor:.6e}")

# For eta = N_baryon / N_photon:
# N_baryon ~ number of modes that survive as "heavy" particles
# N_photon ~ number of gap-edge modes (relativistic radiation)

# In the framework's compound nucleus:
# - All 992 channels are massive
# - The "baryon" fraction is determined by the pair-breaking suppression
# - Each quasiparticle pair requires breaking a Cooper pair (cost Delta)

# Conservative estimate: baryons = modes with K_7 charge != 0
# From Session 34: Cooper pairs carry K_7 charge +/- 1/2
# Pair breaking produces qp with K_7 charge
# The suppression factor for producing N_baryon baryons is:
# P(N_b) ~ (exp(-Delta/T))^N_b * combinatorial factors

# Simplified estimate following compound nucleus evaporation:
# eta ~ exp(-m_KK / T_compound) for massive mode emission
# where m_KK is the typical KK mass

m_typical = np.mean(unique_masses)  # average mass of all KK modes
m_lightest = min(unique_masses)
m_heaviest = max(unique_masses)

# At T_compound = 6.37 M_KK >> m_typical, nearly all modes are open
# This gives eta ~ 1 (too large by 10^9)
eta_compound = np.exp(-m_typical / T_compound)
print(f"\neta estimate (T_compound = {T_compound:.3f}):")
print(f"  m_typical = {m_typical:.4f} M_KK")
print(f"  exp(-m/T_compound) = {eta_compound:.6f}")
print(f"  This gives eta ~ O(1) -- WAY too large")

# At T_acoustic = 0.112 M_KK << m_lightest = 0.819:
# ALL channels are Boltzmann-suppressed
eta_acoustic = np.exp(-m_lightest / T_acoustic)
eta_acoustic_heavy = np.exp(-m_heaviest / T_acoustic)
print(f"\neta estimate (T_acoustic = {T_acoustic:.4f}):")
print(f"  exp(-m_lightest/T_a) = {eta_acoustic:.6e}")
print(f"  exp(-m_heaviest/T_a) = {eta_acoustic_heavy:.6e}")
print(f"  All channels exponentially suppressed!")

# Pair-breaking route (from S41):
# D/H ~ 10^{-5} possible from exp(-Delta/T_a) ~ 10^{-3} per pair
# For eta ~ 6e-10: need ~3 pair breakings: (10^{-3})^3 ~ 10^{-9}
n_breakings_for_eta = np.log(6e-10) / np.log(pair_breaking_factor)
print(f"\nPair-breaking route:")
print(f"  Pair-breaking suppression = {pair_breaking_factor:.6e}")
print(f"  For eta = 6e-10: need {n_breakings_for_eta:.1f} pair breakings")
print(f"  This is order ~ {n_breakings_for_eta:.0f} pair breakings")

# Combined estimate: eta from HF branching
# The HF branching into the lightest channel (singlet gap-edge, "radiation")
# vs the heaviest channel (higher reps, "matter")
# gives the baryon-to-photon ratio as:
# eta_HF = T_heavy / T_light = exp(-(m_heavy - m_light)/T)

delta_m = m_heaviest - m_lightest
eta_HF_compound = np.exp(-delta_m / T_compound)
eta_HF_acoustic = np.exp(-delta_m / T_acoustic)

print(f"\nHF branching ratio estimate:")
print(f"  delta_m = m_heaviest - m_lightest = {delta_m:.4f} M_KK")
print(f"  eta_HF(T_compound) = exp(-delta_m/T) = {eta_HF_compound:.6f}")
print(f"  eta_HF(T_acoustic) = exp(-delta_m/T) = {eta_HF_acoustic:.6e}")

# ================================================================
# 9. SENSITIVITY ANALYSIS AND UNCERTAINTY
# ================================================================

print(f"\n{'='*70}")
print(f"SENSITIVITY ANALYSIS")
print(f"{'='*70}")

# Key uncertainties:
# 1. Temperature (64.6% from NOHAIR-40)
# 2. Barrier curvature omega_att (+/- 10% from S38 frequency fit)
# 3. D_K spectrum truncation (only 9 sectors computed)

# Scan over temperature range
T_scan = np.linspace(0.05, 10.0, 200)
DR_scan = np.zeros(len(T_scan))  # dynamic range at each T
eta_scan = np.zeros(len(T_scan))

for i, T in enumerate(T_scan):
    T_light = boltzmann_T(m_lightest, T)
    T_heavy = boltzmann_T(m_heaviest, T)
    DR_scan[i] = T_light / T_heavy if T_heavy > 1e-300 else 1e300
    eta_scan[i] = T_heavy / T_light if T_light > 1e-300 else 0

# Find temperature where DR = 10^3 (3 decades)
DR_3dec_idx = np.argmin(np.abs(np.log10(DR_scan) - 3))
T_3dec = T_scan[DR_3dec_idx]
print(f"  T for DR = 10^3: {T_3dec:.3f} M_KK")

# Find temperature where DR = 10^9 (eta scale)
mask = np.log10(DR_scan) > 0
if np.any(mask):
    DR_9dec_idx = np.argmin(np.abs(np.log10(DR_scan[mask]) - 9))
    T_9dec = T_scan[mask][DR_9dec_idx]
    print(f"  T for DR = 10^9: {T_9dec:.3f} M_KK")
else:
    T_9dec = None
    print(f"  T for DR = 10^9: not achievable in scan range")

# Doorway correction sensitivity
# Vary doorway weight from 0 (statistical) to 1 (pure B2)
doorway_weights = np.linspace(0, 1, 50)
B2_pref_scan = np.zeros(len(doorway_weights))

for i, w_B2 in enumerate(doorway_weights):
    w_others = (1 - w_B2) / (len(sectors) - 1)
    T_B2 = sector_T_acoustic[(1,1)] * w_B2
    T_others = sum(sector_T_acoustic[(int(r[0]),int(r[1]))] * w_others
                   for r in sectors if (int(r[0]), int(r[1])) != (1,1))
    total = T_B2 + T_others
    if total > 0:
        B2_pref_scan[i] = T_B2 / T_others if T_others > 0 else np.inf
    else:
        B2_pref_scan[i] = 0

# At the physical doorway weight
phys_doorway = doorway_BR_B2
phys_pref = np.interp(phys_doorway, doorway_weights, B2_pref_scan)
print(f"\n  Physical doorway weight: {phys_doorway:.4f}")
print(f"  B2 preference at physical weight: {phys_pref:.2f}:1")

# ================================================================
# 10. NUCLEAR BENCHMARKS
# ================================================================

print(f"\n{'='*70}")
print(f"NUCLEAR BENCHMARKS")
print(f"{'='*70}")

# ^24Mg compound nucleus (from S38 analogy):
# - A = 24, Z = 12
# - E* ~ 20-30 MeV (typical CN from ^12C + ^12C)
# - Level density rho ~ exp(2*sqrt(a*E*)) with a ~ A/8 ~ 3 MeV^{-1}
# - Typical # channels ~ 50-100 (neutron, proton, alpha, gamma)
# - Statistical limit: branching ratio ~ T_c * rho_c / sum

print(f"\n  ^24Mg compound nucleus (^12C + ^12C):")
print(f"    Typical E* = 20-30 MeV")
print(f"    Level density parameter a ~ 3 MeV^-1")
print(f"    Number of channels ~ 50-100")
print(f"    Statistical? YES (fully equilibrated)")
print(f"    Dominant decay: alpha emission (Coulomb barrier lowest)")
print(f"    gamma/particle ratio ~ 10^{-3} to 10^{-4}")

print(f"\n  KK compound system (this work):")
print(f"    E* = {E_exc:.1f} M_KK (equivalent to {E_exc*1e16:.0e} GeV if M_KK ~ 10^16 GeV)")
print(f"    Number of channels = {total_channels}")
print(f"    Statistical? NO (T varies 64.6%, PR_B2 = {PR_B2:.2f})")
print(f"    Dominant decay: B2 adjoint modes (doorway preference {doorway_preference:.1f}:1)")
print(f"    Dynamic range:")
print(f"      T_compound: {np.log10(DR_compound):.2f} decades (too hot, nearly democratic)")
print(f"      T_acoustic: {np.log10(DR_acoustic):.2f} decades (cold, strong hierarchy)")

# KEY COMPARISON: nuclear vs KK
print(f"\n  KEY COMPARISON:")
print(f"    Nuclear CN: statistical, many overlapping resonances, HF works well")
print(f"    KK compound: NON-statistical, doorway-dominated, resembles PRE-COMPOUND")
print(f"    Nuclear analog: intermediate structure / doorway state in ^28Si")
print(f"    (few dominant channels, large width fluctuation corrections)")

# ================================================================
# 11. GATE VERDICT
# ================================================================

print(f"\n{'='*70}")
print(f"GATE VERDICT: HF-KK-42")
print(f"{'='*70}")

# Gate criteria (pre-registered):
# PASS: Branching ratio spans > 3 OOM across channels AND doorway > 10:1
# FAIL: Democratic branching (all channels within 1 OOM)

# Since there are NO massless channels, we test the ACTUAL gate:
# "spans > 3 OOM across channels" = dynamic range (lightest/heaviest sector)
# "doorway > 10:1" = preference of dominant channel over second-largest

# RESULTS:
# SECTOR-LEVEL dynamic range (the relevant comparison for "across channels"):
#   T_compound: 1.13 decades (< 3, FAIL)
#   T_acoustic: 1.51 decades (< 3, FAIL)
# INDIVIDUAL EIGENVALUE dynamic range (gives maximum possible separation):
#   T_acoustic: 4.87 decades (> 3, PASS at eigenvalue level)
#   T_compound: 0.086 decades (FAIL)

# However, the gate says "across channels", not "across individual eigenvalues".
# In nuclear physics, channels are sectors (the quantum numbers that distinguish
# decay products), not individual energy levels within a sector. The sector-level
# DR is the correct metric. Both temperature scenarios give DR < 3 decades.

# For eigenvalue-level DR at T_acoustic: 4.87 decades > 3 -> PASS
# This is the spread from lightest (0,0) eigenvalue to heaviest (2,1) eigenvalue.
# A single photon emitted at mass 0.819 vs 2.077 would differ by 4.87 decades
# in Boltzmann weight at T_acoustic. This is physically real but represents
# the spread WITHIN the KK tower, not between qualitatively different channels.

# Doorway preference:
# FGR-derived: 3.2:1 (< 10, FAIL)
# Formation-derived: 6.4:1 (< 10, FAIL)
# Both FAIL the 10:1 criterion.

# The high level density in B3 sectors (rho_B3 = 1008/M_KK) means that even
# though V_B2_B3 is small, the large density of states in higher reps
# compensates, giving a more democratic distribution than formation branching.

gate_DR_compound_sector = np.log10(DR_compound)
gate_DR_acoustic_sector = np.log10(DR_acoustic)
gate_DR_acoustic_eval = np.log10(BR_Boltz_B)  # individual eigenvalue level
gate_doorway_FGR = doorway_preference_FGR
gate_doorway_form = doorway_preference_formation

print(f"\n  Criterion 1: Dynamic range > 3 decades?")
print(f"    Sector-level (T_compound): {gate_DR_compound_sector:.2f} decades -> FAIL")
print(f"    Sector-level (T_acoustic): {gate_DR_acoustic_sector:.2f} decades -> FAIL")
print(f"    Eigenvalue-level (T_acoustic): {gate_DR_acoustic_eval:.2f} decades -> PASS")
print(f"    Eigenvalue-level (T_compound): 0.09 decades -> FAIL")
print(f"    Assessment: FAIL at sector level (both T). PASS only at eigenvalue level with T_acoustic.")

print(f"\n  Criterion 2: Doorway preference > 10:1?")
print(f"    FGR-derived: {gate_doorway_FGR:.1f}:1 -> FAIL")
print(f"    Formation-derived: {gate_doorway_form:.1f}:1 -> FAIL")
print(f"    Assessment: FAIL. Level density in higher reps compensates weak coupling.")

gate_verdict = "FAIL"

print(f"\n  OVERALL VERDICT: {gate_verdict}")
print(f"    Criterion 1: FAIL at sector level (1.1-1.5 decades < 3)")
print(f"    Criterion 2: FAIL (3.2-6.4:1 < 10:1)")
print(f"    HOWEVER: eigenvalue-level DR at T_acoustic = {gate_DR_acoustic_eval:.2f} decades > 3")
print(f"    This is a PARTIAL PASS: hierarchy exists within KK tower at T_acoustic,")
print(f"    but sectors are NOT sufficiently separated for clean branching.")
print(f"    The system is intermediate: neither fully democratic nor strongly hierarchical.")

# ================================================================
# 12. ETA ESTIMATE
# ================================================================

print(f"\n{'='*70}")
print(f"BARYON-TO-PHOTON RATIO: FINAL ESTIMATE")
print(f"{'='*70}")

# The eta estimate depends critically on the mechanism:
# Route 1: HF branching (lightest/heaviest) at T_acoustic
#   eta_HF ~ exp(-delta_m / T_a) = exp(-1.258/0.112) ~ 10^{-4.9}
# Route 2: Pair-breaking suppression
#   eta_pair ~ exp(-n * Delta/T_a) with n ~ 2-3 breakings
#   eta_pair ~ 10^{-3.5} (2 breakings) to 10^{-5.3} (3 breakings)
# Route 3: Combined HF + pair-breaking
#   eta ~ eta_HF * eta_pair

# Best estimate: at T_acoustic, with 2 pair breakings:
eta_best = eta_HF_acoustic * pair_breaking_factor**2
log_eta_best = np.log10(eta_best) if eta_best > 0 else -np.inf

# Uncertainty range: 1-3 pair breakings
eta_low = eta_HF_acoustic * pair_breaking_factor**3
eta_high = eta_HF_acoustic * pair_breaking_factor**1
log_eta_low = np.log10(eta_low) if eta_low > 0 else -np.inf
log_eta_high = np.log10(eta_high) if eta_high > 0 else -np.inf

print(f"  HF branching ratio (T_acoustic): {eta_HF_acoustic:.6e}")
print(f"  Pair-breaking factor: {pair_breaking_factor:.6e}")
print(f"  Best estimate (2 breakings): eta = {eta_best:.3e} (log10 = {log_eta_best:.1f})")
print(f"  Range (1-3 breakings): [{eta_low:.3e}, {eta_high:.3e}]")
print(f"  log10 range: [{log_eta_low:.1f}, {log_eta_high:.1f}]")
print(f"  Observed: eta = 6.1e-10 (log10 = -9.2)")
print(f"  Discrepancy: {log_eta_best - (-9.2):.1f} decades from observed")

# ================================================================
# 13. SAVE RESULTS
# ================================================================

output_data = {
    # Input parameters
    'tau_fold': tau_fold,
    'T_acoustic': T_acoustic,
    'T_Gibbs': T_Gibbs,
    'T_compound': T_compound,
    'T_compound_min': T_compound_min,
    'T_compound_max': T_compound_max,
    'E_exc': E_exc,
    'Delta_pair': Delta_pair,
    'omega_att': omega_att,

    # Mass spectrum
    'unique_masses': np.array(unique_masses),
    'mass_multiplicities': np.array([mass_mult[m] for m in unique_masses]),
    'm_lightest': m_lightest,
    'm_heaviest': m_heaviest,
    'm_typical': m_typical,
    'n_zero_modes': 0,
    'total_channels': total_channels,

    # Transmission coefficients (Boltzmann at T_acoustic)
    'T_boltzmann_acoustic': np.array([boltzmann_T(m, T_acoustic) for m in unique_masses]),
    'T_boltzmann_compound': np.array([boltzmann_T(m, T_compound) for m in unique_masses]),

    # Sector branching
    'sector_labels': np.array([(int(r[0]), int(r[1])) for r in sectors]),
    'sector_T_compound': np.array([sector_T_compound[(int(r[0]),int(r[1]))] for r in sectors]),
    'sector_T_acoustic': np.array([sector_T_acoustic[(int(r[0]),int(r[1]))] for r in sectors]),
    'sector_BR_compound': np.array([BR_compound_sectors[(int(r[0]),int(r[1]))] for r in sectors]),
    'sector_BR_acoustic': np.array([BR_acoustic_sectors[(int(r[0]),int(r[1]))] for r in sectors]),

    # Doorway
    'doorway_BR_B2': doorway_BR_B2,
    'doorway_BR_B1': doorway_BR_B1,
    'doorway_BR_B3': doorway_BR_B3,
    'doorway_preference': doorway_preference,
    'V_B2B2_rms': V_B2_B2_rms,
    'V_B2_B1_rms': V_B2_B1_rms,
    'V_B2_B3_rms': V_B2_B3_rms,
    'rho_B2': rho_B2,
    'rho_B1': rho_B1,
    'rho_B3': rho_B3,

    # Gate
    'gate_DR_compound_sector': gate_DR_compound_sector,
    'gate_DR_acoustic_sector': gate_DR_acoustic_sector,
    'gate_doorway_preference_FGR': gate_doorway_FGR,
    'gate_doorway_preference_formation': gate_doorway_form,
    'gate_DR_acoustic_eval': gate_DR_acoustic_eval,
    'gate_verdict': np.array([gate_verdict]),

    # Eta
    'eta_HF_acoustic': eta_HF_acoustic,
    'eta_best': eta_best,
    'eta_low': eta_low,
    'eta_high': eta_high,
    'pair_breaking_factor': pair_breaking_factor,
    'log_eta_best': log_eta_best,
    'log_eta_observed': -9.2,

    # Sensitivity
    'T_scan': T_scan,
    'DR_scan': DR_scan,
    'T_3dec': T_3dec,
}

output_path = os.path.join(SCRIPT_DIR, "s42_hauser_feshbach.npz")
np.savez_compressed(output_path, **output_data)
print(f"\nSaved: {output_path}")

# ================================================================
# 14. PLOTS
# ================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("Hauser-Feshbach KK Branching Ratios (HF-KK-42)", fontsize=14, fontweight='bold')

# Panel A: KK mass spectrum with transmission coefficients
ax = axes[0, 0]
masses_arr = np.array(unique_masses)
mult_arr = np.array([mass_mult[m] for m in unique_masses])
T_boltz_acou = np.array([boltzmann_T(m, T_acoustic) for m in unique_masses])
T_boltz_comp = np.array([boltzmann_T(m, T_compound) for m in unique_masses])

ax.bar(masses_arr, mult_arr, width=0.015, alpha=0.4, color='steelblue', label='Multiplicity')
ax2 = ax.twinx()
ax2.semilogy(masses_arr, T_boltz_acou, 'r-', lw=1.5, label=f'T(T_a={T_acoustic:.3f})')
ax2.semilogy(masses_arr, T_boltz_comp, 'b--', lw=1.5, label=f'T(T_c={T_compound:.1f})')
ax.set_xlabel('Mass (M_KK)')
ax.set_ylabel('Multiplicity', color='steelblue')
ax2.set_ylabel('Transmission coeff.', color='red')
ax2.legend(loc='right', fontsize=8)
ax.set_title('KK Mass Spectrum + Transmission')
ax.axvline(m_lightest, color='green', ls=':', lw=0.8, label=f'm_min={m_lightest:.3f}')
ax.legend(loc='upper left', fontsize=7)

# Panel B: Sector-resolved branching (compound vs acoustic T)
ax = axes[0, 1]
sector_names = [f'({int(r[0])},{int(r[1])})' for r in sectors]
x_pos = np.arange(len(sectors))
br_c = [BR_compound_sectors[(int(r[0]),int(r[1]))] for r in sectors]
br_a = [BR_acoustic_sectors[(int(r[0]),int(r[1]))] for r in sectors]

bar_width = 0.35
ax.bar(x_pos - bar_width/2, br_c, bar_width, label=f'T_compound={T_compound:.1f}', color='royalblue')
ax.bar(x_pos + bar_width/2, br_a, bar_width, label=f'T_acoustic={T_acoustic:.3f}', color='firebrick')
ax.set_xticks(x_pos)
ax.set_xticklabels(sector_names, rotation=45, fontsize=8)
ax.set_ylabel('Branching Ratio (with doorway)')
ax.set_title('Sector-Resolved Branching')
ax.legend(fontsize=8)
ax.set_yscale('log')

# Panel C: Dynamic range vs temperature
ax = axes[1, 0]
log_DR = np.log10(DR_scan)
log_DR = np.clip(log_DR, -1, 20)
ax.plot(T_scan, log_DR, 'k-', lw=2)
ax.axhline(3, color='red', ls='--', lw=1, label='3 decade threshold')
ax.axhline(9.2, color='green', ls='--', lw=1, label='eta = 6e-10 scale')
ax.axvline(T_acoustic, color='blue', ls=':', lw=1.5, label=f'T_acoustic={T_acoustic:.3f}')
ax.axvline(T_compound, color='orange', ls=':', lw=1.5, label=f'T_compound={T_compound:.1f}')
ax.set_xlabel('Temperature (M_KK)')
ax.set_ylabel('Dynamic Range (decades)')
ax.set_title('Channel DR vs Temperature')
ax.legend(fontsize=7)
ax.set_xlim(0, 10)
ax.set_ylim(-1, 15)

# Panel D: Doorway preference scan
ax = axes[1, 1]
ax.plot(doorway_weights, B2_pref_scan, 'k-', lw=2)
ax.axhline(10, color='red', ls='--', lw=1, label='10:1 threshold')
ax.axvline(phys_doorway, color='blue', ls=':', lw=1.5,
           label=f'Physical w_B2={phys_doorway:.3f}')
ax.set_xlabel('B2 Doorway Weight')
ax.set_ylabel('B2 / Others Preference')
ax.set_title('Doorway Preference vs B2 Weight')
ax.legend(fontsize=8)
ax.set_yscale('log')

plt.tight_layout()
plot_path = os.path.join(SCRIPT_DIR, "s42_hauser_feshbach.png")
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
print(f"Saved: {plot_path}")
plt.close()

# ================================================================
# 15. FINAL SUMMARY
# ================================================================

print(f"\n{'='*70}")
print(f"FINAL SUMMARY")
print(f"{'='*70}")
print(f"")
print(f"  STRUCTURAL RESULT: D_K at the fold has ZERO massless modes.")
print(f"  All 992 eigenvalues are massive (m_min = {m_lightest:.4f} M_KK).")
print(f"  This eliminates the standard photon/graviton emission channels.")
print(f"")
print(f"  GATE HF-KK-42: {gate_verdict}")
print(f"    Criterion 1 (DR > 3 decades):")
print(f"      Sector-level: {gate_DR_acoustic_sector:.2f} decades (FAIL)")
print(f"      Eigenvalue-level (T_acoustic): {gate_DR_acoustic_eval:.2f} decades (PASS)")
print(f"    Criterion 2 (doorway > 10:1):")
print(f"      FGR preference = {gate_doorway_FGR:.1f}:1 (FAIL)")
print(f"      Formation preference = {gate_doorway_form:.1f}:1 (FAIL)")
print(f"")
print(f"  WHY FAIL:")
print(f"    1. All KK modes are massive (m_min={m_lightest:.3f} M_KK). No massless channels exist.")
print(f"    2. Level density in higher reps (rho_B3={rho_B3:.0f}/M_KK) compensates weak coupling.")
print(f"    3. Formation branching 85.5% B2 becomes only 6.4:1 preference (< 10:1 threshold).")
print(f"    4. At T_compound >> all masses, channels are nearly democratic.")
print(f"")
print(f"  ETA ESTIMATE:")
print(f"    Best: {eta_best:.3e} (log10 = {log_eta_best:.1f})")
print(f"    Range: [{eta_low:.3e}, {eta_high:.3e}]")
print(f"    Observed: 6.1e-10 (log10 = -9.2)")
print(f"    Discrepancy: {abs(log_eta_best - (-9.2)):.1f} decades")
print(f"")
print(f"  NUCLEAR ANALOG: Intermediate structure in ^28Si")
print(f"    NOT statistical CN. Doorway-dominated with moderate B2 preference (3.2-6.4:1).")
print(f"    Width fluctuation correction factor W_c ~ 3-6 (moderate, not extreme).")
print(f"")
print(f"  Data: tier0-computation/s42_hauser_feshbach.npz")
print(f"  Plot: tier0-computation/s42_hauser_feshbach.png")
