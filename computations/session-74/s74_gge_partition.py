"""
S74 W1-F: GGE-PARTITION-74 -- Three-channel partition of GGE energy.

Computes (E_a2, E_Leggett, E_effacement) as three orthogonal projections of the
post-transit 8-mode GGE relic onto the spectral moments (a_2, Leggett inter-branch,
a_0/effacement-residual). The partition is an algebraic identity: the spectral
moments are orthogonal so any GGE state decomposes additively into these three
channels. Includes the BCS zero-point contribution to E_a2 (S35/S36 canonical).

Substrate framing: these are NOT three physical species. They are three orthogonal
PROJECTIONS of the GGE density matrix onto the substrate's spectral moment basis:
  - a_2 subspace  -> emergent matter  (BCS modes, block-diagonal via S22b)
  - Leggett mode  -> emergent DM      (CPT-neutral coherence, S66)
  - a_0 residual  -> emergent DE      (effacement leakage through Gamma mismatch)

Gate pre-registration (GGE-PARTITION-74):
  PASS if E_a2/E_total in [0.158, 0.630]
      AND E_Leggett/E_total in [0.135, 0.540]
      AND E_effacement/E_total in [0.343, 1.000].
  FAIL if any channel is off by > factor 10.
  INFO if consistent with S66 but outside the factor-2 bracket on a_2.

Observation targets:
  E_a2/E_total        ~ 0.315 (Omega_m / Omega_total, Planck)
  E_Leggett/E_total   ~ 0.27  (Omega_DM / Omega_total)
  E_effacement/E_total ~ 0.685 (Omega_Lambda / Omega_total)

Cross-checks:
  (1) Sum of three channels = 1 (partition identity).
  (2) E_Leggett alone reproduces S66 Omega_DM h^2 = 0.120 via calibration.
  (3) BCS ZPE dominates E_a2 excitation at the GGE relic population.
  (4) Sum E_a2 + E_Leggett + E_effacement consistency with Lambda_eff = 1.709 M_KK.

Author: einstein-theorist (S74 W1-F)
"""

import os
import sys
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

# Canonical constants
from canonical_constants import (
    M_KK, M_KK_gravity, M_Pl_reduced,
    tau_fold, Delta_BCS,
    a0_fold, a2_fold, a4_fold,
    omega_L1, omega_L2,
    N_cells, T_acoustic,
    f_2_default,
)

# ---------------------------------------------------------------------
# Paths and I/O
# ---------------------------------------------------------------------
SCRIPT_NAME = "s74_gge_partition"
OUT_NPZ = f"computations/_shared/{SCRIPT_NAME}.npz"
OUT_PNG = f"computations/_shared/{SCRIPT_NAME}.png"

BOG_NPZ = "computations/session-73/s73a_exit_horizon_bog.npz"
FP_NPZ  = "computations/session-73/s73a_fabry_perot_cavity.npz"

# ---------------------------------------------------------------------
# Load 8-mode Bogoliubov data (S73A W1-A)
# ---------------------------------------------------------------------
bog = np.load(BOG_NPZ, allow_pickle=True)
labels_8mode = bog["labels"]                    # ['B2[0..3]', 'B1', 'B3[0..2]']
r_k_bcs_8    = bog["r_k_bcs"].astype(float)     # intrinsic BCS squeeze
n_k_exit_8   = bog["n_k"].astype(float)         # mode occupations from exit horizon
mode_weights = bog["mode_weights"].astype(float)
Nmodes = int(len(labels_8mode))                                 # (local)

# Load Fabry-Perot cavity data for compound phase & per-mode omega
fp = np.load(FP_NPZ, allow_pickle=True)
omega_k_MKK     = fp["omega_k"].astype(float)          # pair-breaking frequency per mode
r_k_compound_8  = fp["r_k_compound"].astype(float)     # fully compounded squeeze
phi_23_split    = float(fp["delta_phi_B2_B3"])         # 0.552 rad (B2-B3 compound split)
phi_13_split    = float(fp["delta_phi_B1_B3"])
phi_12_split    = float(fp["delta_phi_B2_B1"])
n_bar_entry     = float(fp["n_bar_entry"])             # thermal occupation at entry (85.2)

# ---------------------------------------------------------------------
# SANITY: log source provenance
# ---------------------------------------------------------------------
print("=" * 72)
print("S74 W1-F: GGE-PARTITION-74 -- Three-channel partition with BCS ZPE")
print("=" * 72)
print(f"Loaded 8-mode BCS data from: {BOG_NPZ}")
print(f"Labels: {list(labels_8mode)}")
print(f"omega_k (M_KK): {omega_k_MKK}")
print(f"r_k_bcs: {r_k_bcs_8}")
print(f"r_k_compound: {r_k_compound_8}")
print(f"n_k_exit (Bogoliubov production): {n_k_exit_8}")
print(f"mode_weights (dim/32): {mode_weights}")
print()
print(f"Compound inter-branch phase splits [rad]:")
print(f"  delta_phi_B2_B3 = {phi_23_split:.6f}  (PRIMARY Leggett-channel split)")
print(f"  delta_phi_B1_B3 = {phi_13_split:.6f}")
print(f"  delta_phi_B2_B1 = {phi_12_split:.6f}")
print(f"  n_bar_entry     = {n_bar_entry:.4f}")
print()
print(f"Canonical omega_L1 = {omega_L1} M_KK (Anderson-Bogoliubov, S52/S66)")
print(f"  [task-prompt value 0.0492 is from S48/S59 superseded inertia convention]")
print()

# ---------------------------------------------------------------------
# Channel 1: E_a2 -- a_2 spectral moment projection (emergent matter)
# ---------------------------------------------------------------------
# By the S22b block-diagonal theorem, every BCS mode's D_K block sits inside the
# a_2 moment (matter sector: positive Seeley-DeWitt scalar-curvature term). The
# projection weight w_k^{a2} = 1 for all 8 BCS modes.
#
# The per-mode squeezed-vacuum energy at relic population is:
#   E_k = omega_k * (sinh^2(r_k_bcs) + 1/2)
# where sinh^2(r_k) is the squeezed-vacuum excitation and 1/2 is the BCS ZPE.
# The total E_a2 is sum_k E_k weighted by mode multiplicity (mode_weights * N_base)
# where N_base = 32 (by dimension block multiplicities the 8 "distinct" labels
# carry mode_weights that sum to 1.0 over the 32-cell tessellation).
# ---------------------------------------------------------------------
w_a2 = np.ones(Nmodes)                                 # (local)  full a_2 projection

# Per-mode BCS vacuum expectation
sinh_sq_bcs   = np.sinh(r_k_bcs_8) ** 2                # (local)
cosh_sq_bcs   = np.cosh(r_k_bcs_8) ** 2                # (local)
E_k_excit_bcs = omega_k_MKK * sinh_sq_bcs * w_a2       # (local) excitation at BCS relic
E_k_zpe       = 0.5 * omega_k_MKK * w_a2               # (local) BCS zero point
E_k_total_bcs = E_k_excit_bcs + E_k_zpe                # (local) per-mode channel-1

# Mode-weighted totals (per tessellation cell)
E_a2_excit_per_cell = float(np.sum(mode_weights * E_k_excit_bcs))    # (local) M_KK
E_a2_zpe_per_cell   = float(np.sum(mode_weights * E_k_zpe))          # (local) M_KK
E_a2_per_cell       = float(np.sum(mode_weights * E_k_total_bcs))    # (local) M_KK

# Total over N_cells = 32
E_a2_total_MKK = N_cells * E_a2_per_cell               # (local) M_KK

print("Channel 1: E_a2 (emergent matter, a_2 subspace)")
print("-" * 60)
print(f"  Per mode breakdown (r_bcs only):")
for k, lab in enumerate(labels_8mode):
    print(f"    {lab:7s} omega={omega_k_MKK[k]:.5f}  r_bcs={r_k_bcs_8[k]:.4f}  "
          f"sinh^2={sinh_sq_bcs[k]:7.3f}  E_k={E_k_total_bcs[k]:.4f}  w={mode_weights[k]:.5f}")
print(f"  E_a2 (ZPE only,  per cell) = {E_a2_zpe_per_cell:.6f} M_KK")
print(f"  E_a2 (excit only,per cell) = {E_a2_excit_per_cell:.6f} M_KK")
print(f"  E_a2 (total,     per cell) = {E_a2_per_cell:.6f} M_KK")
print(f"  E_a2 (total, x{N_cells} cells) = {E_a2_total_MKK:.4f} M_KK")
print(f"  ZPE / excitation ratio      = {E_a2_zpe_per_cell / max(E_a2_excit_per_cell, 1e-30):.4f}")
print()

# ---------------------------------------------------------------------
# Channel 2: E_Leggett -- inter-branch coherence mode (emergent DM)
# ---------------------------------------------------------------------
# The Leggett mode is a phase oscillation BETWEEN Bogoliubov branches (B1 vs B2,
# B2 vs B3). Its energy depends on:
#   (a) the intrinsic mode frequency omega_L1 = 0.138 M_KK (S52 Anderson-Bogoliubov)
#   (b) the thermal occupation n_L1 at T_acoustic (S52 W4-J: n_L1 = 0.41)
#   (c) the inter-branch phase split phi_{23} = 0.552 rad (S73A W3-A Fabry-Perot)
# Energy per cell:
#   E_Leggett = omega_L1 * (n_L1 + 1/2) * (1 - cos(phi_{23}^{split}))
# The (1 - cos phi) factor is the first harmonic of the inter-branch Josephson-
# coupling Hamiltonian; it quantifies how much Leggett energy the inter-branch
# phase split carries away from the a_2 projection.
# ---------------------------------------------------------------------
# Thermal occupation at T_acoustic (Bose-Einstein, S52 W4-J value 0.41)
n_L1 = 1.0 / (np.exp(omega_L1 / T_acoustic) - 1.0)     # (local) ~0.408, matches S52 W4-J
# (Thermal occupation check: using canonical T_acoustic = 0.112 gives n_L1 ~ 0.41)

phi_leg = phi_23_split                                 # (local) rad
leg_phase_factor = 1.0 - np.cos(phi_leg)               # (local) ~0.1472 at 0.552 rad

E_leggett_per_cell = omega_L1 * (n_L1 + 0.5) * leg_phase_factor  # (local) M_KK
E_leggett_total_MKK = N_cells * E_leggett_per_cell     # (local) M_KK

# Second cross-check: S66 W4-D Leggett relic (integrated over all Leggett modes,
# not just L1) gives E_Leggett^{S66,total} = 3.010 M_KK per cell, which includes
# Leggett-2 and the graph-topology summation. The pure L1 single-mode computation
# here is a LOWER BOUND on the Leggett channel energy.
E_leggett_S66_per_cell = 3.010                         # (local) M_KK (S66 W4-D canonical)
E_leggett_S66_total_MKK = N_cells * E_leggett_S66_per_cell   # (local) M_KK

print("Channel 2: E_Leggett (emergent DM, inter-branch coherence)")
print("-" * 60)
print(f"  omega_L1            = {omega_L1} M_KK  (S52 Anderson-Bogoliubov canonical)")
print(f"  n_L1 (thermal)      = {n_L1:.4f}  (T = {T_acoustic} M_KK; S52 W4-J = 0.41)")
print(f"  phi_{{23}}^{{split}}   = {phi_leg:.4f} rad  (S73A Fabry-Perot W3-A)")
print(f"  (1 - cos phi)       = {leg_phase_factor:.5f}")
print(f"  E_Leggett L1 only   = {E_leggett_per_cell:.6f} M_KK/cell  (single-mode)")
print(f"  E_Leggett (S66 W4-D canonical) = {E_leggett_S66_per_cell:.4f} M_KK/cell")
print(f"  E_Leggett (tot, x32 cells) = {E_leggett_S66_total_MKK:.4f} M_KK")
print()

# We adopt the S66 W4-D canonical value for the primary partition, because it
# includes the full Leggett-L1+L2 mode content on the CG(24) graph topology and
# is the quantity that reproduces Omega_DM h^2 = 0.120 at the 0.6% level.
# The L1-single-mode computation above is reported as a lower bound.

E_leg_primary_MKK = E_leggett_S66_total_MKK            # (local) adopted primary value

# ---------------------------------------------------------------------
# Channel 3: E_effacement -- impedance-mismatch residual (emergent DE)
# ---------------------------------------------------------------------
# From the S66 Gamma = 0.99970 impedance-matching coefficient, the effacement
# residual is 1 - Gamma = 3e-4. This is the fraction of the a_2 channel energy
# that leaks into the a_0 (volume) spectral moment and thus appears as a
# cosmological-constant-like term in the 4D effective action.
# ---------------------------------------------------------------------
Gamma_eff = 0.99970                                    # (local) S66 impedance matching
effacement_frac = 1.0 - Gamma_eff                      # (local) 3e-4

E_effacement_per_cell = effacement_frac * E_a2_per_cell       # (local) M_KK
E_effacement_total_MKK = N_cells * E_effacement_per_cell      # (local) M_KK

print("Channel 3: E_effacement (emergent DE, impedance-mismatch residual)")
print("-" * 60)
print(f"  Gamma              = {Gamma_eff}")
print(f"  1 - Gamma          = {effacement_frac}")
print(f"  E_effacement/cell  = {E_effacement_per_cell:.4e} M_KK")
print(f"  E_effacement total = {E_effacement_total_MKK:.4e} M_KK")
print()

# ---------------------------------------------------------------------
# Three-channel totals and ratios
# ---------------------------------------------------------------------
E_total_MKK = E_a2_total_MKK + E_leg_primary_MKK + E_effacement_total_MKK  # (local)

f_a2         = E_a2_total_MKK       / E_total_MKK      # (local)
f_leggett    = E_leg_primary_MKK    / E_total_MKK      # (local)
f_effacement = E_effacement_total_MKK / E_total_MKK    # (local)
sum_check    = f_a2 + f_leggett + f_effacement         # (local) must = 1

# Ratios for observational comparison
ratio_a2_over_leg = E_a2_total_MKK / E_leg_primary_MKK # (local) target Omega_m/Omega_DM ~ 2.6
ratio_a2_over_tot = f_a2                               # target ~ 0.315
ratio_leg_over_tot = f_leggett                         # target ~ 0.27
ratio_eff_over_tot = f_effacement                      # target ~ 0.685

print("=" * 72)
print("THREE-CHANNEL PARTITION RESULTS")
print("=" * 72)
print(f"{'Channel':<22s} {'Energy [M_KK]':>16s} {'Fraction':>12s}")
print(f"{'-'*22:<22s} {'-'*16:>16s} {'-'*12:>12s}")
print(f"{'E_a2 (matter)':<22s} {E_a2_total_MKK:>16.4f} {f_a2:>12.6f}")
print(f"{'E_Leggett (DM)':<22s} {E_leg_primary_MKK:>16.4f} {f_leggett:>12.6f}")
print(f"{'E_effacement (DE)':<22s} {E_effacement_total_MKK:>16.4e} {f_effacement:>12.6e}")
print(f"{'-'*22:<22s} {'-'*16:>16s} {'-'*12:>12s}")
print(f"{'TOTAL':<22s} {E_total_MKK:>16.4f} {sum_check:>12.6f}")
print()
print("Ratios vs observational targets:")
print(f"  E_a2 / E_Leggett      = {ratio_a2_over_leg:>8.4f}   target: Omega_m/Omega_DM ~ 2.60")
print(f"  E_a2 / E_total        = {ratio_a2_over_tot:>8.6f}   target: 0.315")
print(f"  E_Leggett / E_total   = {ratio_leg_over_tot:>8.6f}   target: 0.27")
print(f"  E_effacement / E_tot  = {ratio_eff_over_tot:>8.4e}   target: 0.685")
print()

# ---------------------------------------------------------------------
# Cross-check (1): Partition sum identity (trivially 1.0 by construction)
# ---------------------------------------------------------------------
sum_identity_err = abs(sum_check - 1.0)
print("Cross-checks:")
print(f"  [1] Sum of three channels   = {sum_check:.8f}  (target 1.0, err {sum_identity_err:.2e})")

# ---------------------------------------------------------------------
# Cross-check (2): S66 Omega_DM h^2 calibration from Leggett channel alone
# ---------------------------------------------------------------------
# S66 W4-D: Omega_DM h^2 = 0.03985 * E_Leggett (M_KK, per cell)
calib_S66 = 0.03985                                    # (local) M_KK -> Omega_DM h^2
Omega_DM_h2_pred = calib_S66 * E_leggett_S66_per_cell  # (local)
Omega_DM_h2_Planck = 0.1207                            # (local) Planck 2018

cc2_ratio = Omega_DM_h2_pred / Omega_DM_h2_Planck
cc2_err = abs(Omega_DM_h2_pred - Omega_DM_h2_Planck) / Omega_DM_h2_Planck
print(f"  [2] Omega_DM h^2 (Leggett)  = {Omega_DM_h2_pred:.5f}  "
      f"(Planck 0.1207, err {cc2_err*100:.2f}%)")

# ---------------------------------------------------------------------
# Cross-check (3): BCS ZPE dominance in E_a2
# ---------------------------------------------------------------------
# ZPE should dominate over excitation at the GGE relic population since n_k_exit
# values are small (~0.001-0.013 from Bogoliubov production); but E_a2 here uses
# the r_k_bcs intrinsic squeeze which gives much larger excitation (sinh^2 up to
# ~180 for r=3.57). The "GGE relic" notion here is the POST-TRANSIT squeezed
# BCS vacuum, not the exit-horizon Bogoliubov fraction. So ZPE does NOT dominate;
# the excitation dominates due to the large intrinsic BCS squeeze.
zpe_dominance_ratio = E_a2_zpe_per_cell / E_a2_excit_per_cell  # (local)
print(f"  [3] ZPE / excitation ratio  = {zpe_dominance_ratio:.5f}  "
      f"(ZPE is subdominant at intrinsic BCS squeeze r ~ 2-4)")

# ---------------------------------------------------------------------
# Cross-check (4): S57 Lambda_eff = 1.709 M_KK per cell consistency
# ---------------------------------------------------------------------
# The S57 quantity Lambda_eff = E_GGE - E_BCS = +1.709 M_KK is the non-equilibrium
# GGE EXCESS above the BCS ground state, not the total E_GGE. To compare with the
# three-channel partition we use E_GGE = +1.688 M_KK per cell (S57 canonical).
# E_a2 here is the BCS-sector contribution including ZPE; E_Leggett (S66) is the
# gapped-coherence relic; E_effacement is the a_0 residual. These three should
# sum to a value consistent with the BCS + GGE excess decomposition.
Lambda_eff_S57 = 1.709                                 # (local) M_KK per cell
E_GGE_S57_per_cell = 1.688                             # (local) M_KK per cell
E_BCS_S57_per_cell = -0.021                            # (local) M_KK per cell

# Our channel-1 E_a2_per_cell is the BCS squeezed-vacuum energy (ZPE + excitation),
# which is FUNDAMENTALLY different from E_BCS_S57 (equilibrium paired ground state).
# The S57 E_BCS = -0.021 is the q-theory equilibrium reference. Our E_a2 measures
# the NON-equilibrium squeezed state. They are distinct quantities.
E_channel_sum_per_cell = E_a2_per_cell + E_leggett_S66_per_cell + E_effacement_per_cell  # (local)

print(f"  [4] Sum per cell (channels) = {E_channel_sum_per_cell:.4f} M_KK")
print(f"      S57 Lambda_eff           = {Lambda_eff_S57} M_KK  (non-eq excess)")
print(f"      S57 E_GGE                = {E_GGE_S57_per_cell} M_KK  (total)")
print(f"      ratio (chan sum / L_eff) = {E_channel_sum_per_cell / Lambda_eff_S57:.4f}")
print(f"      Note: E_a2 here is squeezed-vacuum E, NOT S57 E_BCS equilibrium ref.")
print()

# ---------------------------------------------------------------------
# Gate verdict
# ---------------------------------------------------------------------
GATE_NAME = "GGE-PARTITION-74"

# PASS brackets from pre-registered gate
PASS_A2_LO, PASS_A2_HI = 0.158, 0.630
PASS_LEG_LO, PASS_LEG_HI = 0.135, 0.540
PASS_EFF_LO, PASS_EFF_HI = 0.343, 1.000

# Factor-10 FAIL brackets (off by > factor 10 on ANY channel)
FAIL_A2_LO, FAIL_A2_HI = 0.0315, 1.0      # target 0.315, factor 10
FAIL_LEG_LO, FAIL_LEG_HI = 0.027, 1.0     # target 0.27
FAIL_EFF_LO, FAIL_EFF_HI = 0.0685, 1.0    # target 0.685

in_pass_a2  = PASS_A2_LO  <= f_a2         <= PASS_A2_HI
in_pass_leg = PASS_LEG_LO <= f_leggett    <= PASS_LEG_HI
in_pass_eff = PASS_EFF_LO <= f_effacement <= PASS_EFF_HI

in_fail_a2  = not (FAIL_A2_LO  <= f_a2         <= FAIL_A2_HI)
in_fail_leg = not (FAIL_LEG_LO <= f_leggett    <= FAIL_LEG_HI)
in_fail_eff = not (FAIL_EFF_LO <= f_effacement <= FAIL_EFF_HI)

if in_fail_a2 or in_fail_leg or in_fail_eff:
    gate_verdict = "FAIL"
    gate_reason = []
    if in_fail_a2:
        gate_reason.append(f"a2={f_a2:.4e} outside 10x bracket [{FAIL_A2_LO},{FAIL_A2_HI}]")
    if in_fail_leg:
        gate_reason.append(f"leg={f_leggett:.4e} outside 10x bracket [{FAIL_LEG_LO},{FAIL_LEG_HI}]")
    if in_fail_eff:
        gate_reason.append(f"eff={f_effacement:.4e} outside 10x bracket [{FAIL_EFF_LO},{FAIL_EFF_HI}]")
    gate_reason_str = "; ".join(gate_reason)
elif in_pass_a2 and in_pass_leg and in_pass_eff:
    gate_verdict = "PASS"
    gate_reason_str = "all three channels within factor-2 of observation"
else:
    gate_verdict = "INFO"
    inside = []
    outside = []
    for name, inside_flag, val, lo, hi in [
        ("a2",  in_pass_a2,  f_a2,         PASS_A2_LO,  PASS_A2_HI),
        ("leg", in_pass_leg, f_leggett,    PASS_LEG_LO, PASS_LEG_HI),
        ("eff", in_pass_eff, f_effacement, PASS_EFF_LO, PASS_EFF_HI),
    ]:
        if inside_flag:
            inside.append(f"{name}={val:.4e} in [{lo},{hi}]")
        else:
            outside.append(f"{name}={val:.4e} outside [{lo},{hi}]")
    gate_reason_str = ("INSIDE: " + "; ".join(inside)) if inside else ""
    gate_reason_str += (" | OUTSIDE: " + "; ".join(outside)) if outside else ""

print("=" * 72)
print(f"GATE: {GATE_NAME} = {gate_verdict}")
print(f"Reason: {gate_reason_str}")
print("=" * 72)
print()

# ---------------------------------------------------------------------
# Save data
# ---------------------------------------------------------------------
np.savez(
    OUT_NPZ,
    # identifiers
    gate_name=GATE_NAME,
    gate_verdict=gate_verdict,
    gate_detail=gate_reason_str,
    # per-channel values (per cell and total)
    E_a2_per_cell=E_a2_per_cell,
    E_a2_zpe_per_cell=E_a2_zpe_per_cell,
    E_a2_excit_per_cell=E_a2_excit_per_cell,
    E_a2_total_MKK=E_a2_total_MKK,
    E_leggett_per_cell_L1_single=E_leggett_per_cell,
    E_leggett_per_cell_S66=E_leggett_S66_per_cell,
    E_leggett_total_MKK=E_leg_primary_MKK,
    E_effacement_per_cell=E_effacement_per_cell,
    E_effacement_total_MKK=E_effacement_total_MKK,
    E_total_MKK=E_total_MKK,
    # fractions
    f_a2=f_a2,
    f_leggett=f_leggett,
    f_effacement=f_effacement,
    sum_check=sum_check,
    # ratios
    ratio_a2_over_leg=ratio_a2_over_leg,
    ratio_a2_over_tot=ratio_a2_over_tot,
    ratio_leg_over_tot=ratio_leg_over_tot,
    ratio_eff_over_tot=ratio_eff_over_tot,
    # observational targets
    target_a2_over_tot=0.315,
    target_leg_over_tot=0.27,
    target_eff_over_tot=0.685,
    target_a2_over_leg=0.315/0.27,
    # inputs
    labels_8mode=labels_8mode,
    omega_k_MKK=omega_k_MKK,
    r_k_bcs=r_k_bcs_8,
    n_k_exit=n_k_exit_8,
    mode_weights=mode_weights,
    phi_23_split=phi_23_split,
    phi_13_split=phi_13_split,
    phi_12_split=phi_12_split,
    n_L1_thermal=n_L1,
    leg_phase_factor=leg_phase_factor,
    Gamma_eff=Gamma_eff,
    effacement_frac=effacement_frac,
    N_cells=N_cells,
    # cross-check results
    Omega_DM_h2_pred=Omega_DM_h2_pred,
    Omega_DM_h2_Planck=Omega_DM_h2_Planck,
    cc2_err=cc2_err,
    zpe_dominance_ratio=zpe_dominance_ratio,
    Lambda_eff_S57=Lambda_eff_S57,
    E_GGE_S57_per_cell=E_GGE_S57_per_cell,
    E_BCS_S57_per_cell=E_BCS_S57_per_cell,
    E_channel_sum_per_cell=E_channel_sum_per_cell,
    # PASS/FAIL brackets
    PASS_A2_LO=PASS_A2_LO, PASS_A2_HI=PASS_A2_HI,
    PASS_LEG_LO=PASS_LEG_LO, PASS_LEG_HI=PASS_LEG_HI,
    PASS_EFF_LO=PASS_EFF_LO, PASS_EFF_HI=PASS_EFF_HI,
)
print(f"Saved: {OUT_NPZ}")

# ---------------------------------------------------------------------
# Plot: two pie charts (framework vs observation)
# ---------------------------------------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Left: framework partition
colors = ['#1f77b4', '#d62728', '#2ca02c']
labels_pie = [
    f"a_2 (matter)\n{f_a2:.3f}",
    f"Leggett (DM)\n{f_leggett:.3f}",
    f"effacement (DE)\n{f_effacement:.2e}",
]
vals = [max(f_a2, 1e-3), max(f_leggett, 1e-3), max(f_effacement, 1e-3)]
axes[0].pie(vals, labels=labels_pie, colors=colors, autopct='%1.1f%%', startangle=90)
axes[0].set_title(f"Framework GGE Partition\n(E_total = {E_total_MKK:.2f} M_KK)\n"
                  f"Gate {GATE_NAME}: {gate_verdict}", fontsize=11)

# Right: observed Omega partition (Planck)
obs_labels = [
    "Omega_m (matter)\n0.315",
    "Omega_DM (DM)\n0.27",
    "Omega_Lambda (DE)\n0.685",
]
# Note: Planck Omega_m = 0.315 already INCLUDES baryons + DM, so for apples-to-
# apples we split Omega_b = 0.049 and Omega_DM = 0.266. The three-channel target
# is (Omega_b, Omega_DM, Omega_L) = (0.049, 0.266, 0.685) but the task stated
# targets (0.315, 0.27, 0.685) which double-counts matter. We use the task's
# stated targets for the gate and note the ambiguity.
obs_vals = [0.315, 0.27, 0.685]
axes[1].pie(obs_vals, labels=obs_labels, colors=colors, autopct='%1.1f%%', startangle=90)
axes[1].set_title("Observed Omega Fractions\n(Planck 2018, task targets)\n"
                  "[note: task E_a2+E_leg+E_eff > 1, see text]", fontsize=11)

fig.suptitle(
    f"S74 W1-F GGE-PARTITION-74  |  "
    f"a_2/Leg = {ratio_a2_over_leg:.2e}  |  "
    f"gate {gate_verdict}",
    fontsize=12,
)
plt.tight_layout()
plt.savefig(OUT_PNG, dpi=120, bbox_inches='tight')
print(f"Saved: {OUT_PNG}")
plt.close()

print()
print("Done.")
