#!/usr/bin/env python3
"""
s59_dm_recalc.py — DM Abundance Recalculation (DM-RECALC-59, W1-2)
===================================================================

S58's f_DM calculation used:
  - epsilon = 0.00248 (S49 value)
  - m_B2 = E_B2_mean ~ 0.845 M_KK (round-SU(3) spectrum)

S58 W0-3 and W2-1 established corrected values:
  - epsilon_direct = 0.00143 (42% reduction, EPSILON-DIRECT-58 PASS)
  - m_B2(fold) = 0.723 M_KK (30% reduction from geometric corrections)

This script recomputes the full energy budget, f_DM, and NROY under these
corrections, providing the updated baseline for all subsequent computations.

Context: W0-1 (f_DM-DEPLETION-59) found f_DM(z=0) = 1.000 (PASS), because
BA phonons redshift away and BCS quasiparticles annihilate. Only Leggett
survives. The transit-epoch f_DM is no longer the sole bottleneck, but the
corrected baseline is needed for consistency and for the Bayesian emulator.

Gate: DM-RECALC-59
  PASS: Updated f_DM(B) > 0.50
  FAIL: Updated f_DM(B) < 0.30
  INFO: f_DM(B) in [0.30, 0.50]

Author: Phonon-First Cosmologist
Session: 59 (2026-03-24)
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
from canonical_constants import *

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

outdir = os.path.dirname(os.path.abspath(__file__))

print("=" * 72)
print("DM-RECALC-59: DM Abundance Recalculation with Geometric Corrections")
print("=" * 72)

# =============================================================================
# 1. Load input data
# =============================================================================

ep_data = np.load(os.path.join(outdir, 's58_epsilon_direct.npz'), allow_pickle=True)
vp_data = np.load(os.path.join(outdir, 's58_volovik_partition.npz'), allow_pickle=True)
lf_data = np.load(os.path.join(outdir, 's56_leggett_fabric.npz'), allow_pickle=True)
mv_data = np.load(os.path.join(outdir, 's58_mass_variation.npz'), allow_pickle=True)

# S57 upstream data (same as S58 used)
lp_data = np.load(os.path.join(outdir, 's57_leggett_partition.npz'), allow_pickle=True)
ce_data = np.load(os.path.join(outdir, 's57_channel_energy_budget.npz'), allow_pickle=True)
cc_data = np.load(os.path.join(outdir, 's57_cc_sign.npz'), allow_pickle=True)
dm_data = np.load(os.path.join(outdir, 's57_fabric_dm_abundance.npz'), allow_pickle=True)
gs_data = np.load(os.path.join(outdir, 's57_gap_scaling.npz'), allow_pickle=True)
ft_data = np.load(os.path.join(outdir, 's57_finite_rate_transit.npz'), allow_pickle=True)

# =============================================================================
# 2. Extract old (S58) and new (corrected) parameters
# =============================================================================

# --- Epsilon ---
epsilon_old = 0.00248                                    # S49 value, used in S58  # (local)
epsilon_new = float(ep_data['epsilon_direct'])           # 0.00143
epsilon_ratio = epsilon_new / epsilon_old                # 0.577

# --- B2 mass ---
m_B2_round = float(np.sqrt(mv_data['eigenvalues'][0, 3]))   # 1.026 M_KK
m_B2_fold  = float(np.sqrt(mv_data['eigenvalues'][int(mv_data['fold_idx']), 3]))  # 0.723 M_KK
mass_ratio = m_B2_fold / m_B2_round                     # 0.705

# --- Leggett gap ---
omega_L0_old = float(ep_data['omega_L0_S49'])            # 0.0726 M_KK (at eps=0.00248)
omega_L0_new = float(ep_data['omega_L0_direct'])         # 0.0552 M_KK (at eps=0.00143)
omega_L_ratio = omega_L0_new / omega_L0_old              # 0.760

# --- S58 canonical energy budget (from Volovik partition) ---
F_Josephson = float(lp_data['F_Josephson'])               # -336.641 M_KK
F_BCS_old   = float(lp_data['F_BCS'])                     # -4.379 M_KK
F_BA_old    = float(lp_data['F_BA'])                      #  7.021 M_KK
F_Leggett_old = float(ce_data['F_Leggett'])               #  3.010 M_KK
E_matter_old  = abs(F_BCS_old) + F_BA_old + F_Leggett_old # 14.411 M_KK

Lambda_eff_MKK_val = float(cc_data['Lambda_eff_MKK'])     #  1.709 M_KK
w_GGE = float(cc_data['w_GGE'])                           # -0.408
P_vac_GGE_val = float(cc_data['P_vac_GGE'])               # -0.688 M_KK

# --- Gap scaling from S57 ---
alpha_gap  = float(gs_data['alpha_physical'])             # -1.84
A_gap_B    = float(gs_data['A_fit_B_large'])              # 50.26
gap_32B    = float(gs_data['gap_B_N32'])                  # 0.0849
P_exc_2cell = float(ft_data['P_exc_final'])               # 0.081
dtau_dt    = float(ft_data['dtau_dt_phys'])               # 442.4

# S57 calibration references
Omega_DM_h2_B_ref = float(dm_data['Omega_DM_h2_pred_B']) # 0.1417
E_DM_ref = float(dm_data['E_DM_total'])                  # 3.555 M_KK

print(f"\n{'='*60}")
print(f"  CORRECTION PARAMETERS")
print(f"{'='*60}")
print(f"  epsilon:    {epsilon_old:.5f} -> {epsilon_new:.5f}  (ratio {epsilon_ratio:.4f}, -{(1-epsilon_ratio)*100:.1f}%)")
print(f"  m_B2:       {m_B2_round:.4f} -> {m_B2_fold:.4f} M_KK  (ratio {mass_ratio:.4f}, -{(1-mass_ratio)*100:.1f}%)")
print(f"  omega_L0:   {omega_L0_old:.5f} -> {omega_L0_new:.5f} M_KK  (ratio {omega_L_ratio:.4f}, -{(1-omega_L_ratio)*100:.1f}%)")

# =============================================================================
# 3. Recompute energy budget with corrections
# =============================================================================
#
# Physics of corrections:
#
# (a) E_BCS excitation energy:
#     |F_BCS| ~ N_cells * |E_cond| * (epsilon / epsilon_canonical)
#     The BCS condensation energy per cell scales linearly with epsilon
#     (through the BCS gap: Delta ~ epsilon, E_cond ~ Delta^2 * N(E_F))
#     Actually, in the S58 partition, F_BCS = -4.379 was computed from
#     the full ED with the OLD epsilon. The correction is:
#     F_BCS_new = F_BCS_old * (epsilon_new / epsilon_old)
#     because the pairing interaction V_23 ~ epsilon, and E_cond ~ V_23.
#
# (b) E_BA Bogoliubov-Anderson excitation energy:
#     F_BA = 7.021 M_KK comes from the 31 phonon modes of the 32-cell fabric.
#     The BA phonon energy scales with E_J (Josephson coupling) which is
#     independent of epsilon (it depends on the condensate overlap, not
#     the pairing strength). The mass correction affects the dispersion
#     omega_k = c_s * k through the sound speed c_s ~ sqrt(E_J * n_s / m*).
#     With m_B2 reducing by 30%, c_s increases by sqrt(1/mass_ratio) ~ 19%.
#     But E_BA also depends on the occupation: for a sudden quench,
#     E_BA = sum_k omega_k * (n_k + 1/2), and n_k is set by the quench.
#     The primary scaling is through the Josephson coupling:
#     E_BA scales with E_J (independent of epsilon and m_B2 to leading order).
#     The mass correction enters at second order through c_s.
#     We keep E_BA unchanged for the conservative estimate, but compute
#     the correction factor for completeness.
#
# (c) E_Leggett excitation energy:
#     F_Leggett = 3.010 M_KK from the 31 Leggett modes of the 32-cell fabric.
#     The Leggett energy scales with omega_L * (n_L + 1/2) per mode.
#     omega_L scales with sqrt(epsilon) approximately (from the Josephson formula).
#     More precisely, from S58: omega_L0_direct / omega_L0_S49 = 0.760.
#     Since the Leggett excitation was computed at the OLD omega_L, we correct:
#     F_Leggett_new = F_Leggett_old * (omega_L0_new / omega_L0_old)

print(f"\n{'='*60}")
print(f"  S58 ENERGY BUDGET (OLD, at epsilon=0.00248)")
print(f"{'='*60}")
print(f"  |F_BCS|    = {abs(F_BCS_old):.3f} M_KK  (30.4%)")
print(f"  F_BA       = {F_BA_old:.3f} M_KK  (48.7%)")
print(f"  F_Leggett  = {F_Leggett_old:.3f} M_KK  (20.9%)")
print(f"  E_matter   = {E_matter_old:.3f} M_KK")
print(f"  f_DM(A)    = {F_Leggett_old / E_matter_old:.4f}  (Leggett only)")
print(f"  f_DM(B)    = {(F_Leggett_old + abs(F_BCS_old)) / E_matter_old:.4f}  (Leggett + BCS)")

# --- Apply corrections ---

# BCS: E_cond ~ V_pair ~ epsilon (linear in coupling, validated by RG-BCS-35)
E_BCS_new = abs(F_BCS_old) * epsilon_ratio
# Cross-check: E_cond_ED_8mode = -0.137 was computed at some reference epsilon;
# the scaling F_BCS ~ epsilon * N_cells * |E_cond_ref| is built into the S57
# channel energy budget. The ratio is what matters.

# BA: Leading-order independent of epsilon. Mass correction enters through
# sound speed: c_s ~ sqrt(J / m*), so E_BA ~ c_s * k ~ sqrt(1/m*).
# With m* -> m_B2_fold/m_B2_round * m*, the factor is sqrt(m_B2_round/m_B2_fold).
# But this is a small correction and E_BA is dominated by the Josephson
# coupling (J_C2 = 0.933, independent of both epsilon and m_B2).
# For maximal honesty: include the mass correction on BA.
c_s_correction = np.sqrt(m_B2_round / m_B2_fold)  # sqrt(1/mass_ratio) ~ 1.19
E_BA_new = F_BA_old * c_s_correction
# Note: this INCREASES E_BA because lighter particles have higher sound speed.
# This makes f_DM worse (more non-DM energy).

# Leggett: omega_L scales as measured (omega_L_ratio = 0.760)
E_Leggett_new = F_Leggett_old * omega_L_ratio

E_matter_new = E_BCS_new + E_BA_new + E_Leggett_new

# f_DM under corrected parameters
f_DM_A_new = E_Leggett_new / E_matter_new
f_DM_B_new = (E_Leggett_new + E_BCS_new) / E_matter_new

# S58 values for comparison
f_DM_A_old = float(vp_data['f_DM_Volovik_A'])   # 0.2089
f_DM_B_old = float(vp_data['f_DM_Volovik_B'])   # 0.5128

print(f"\n{'='*60}")
print(f"  CORRECTED ENERGY BUDGET (epsilon=0.00143, m_B2=0.723)")
print(f"{'='*60}")
print(f"  |F_BCS|_new    = {E_BCS_new:.4f} M_KK  ({E_BCS_new/E_matter_new*100:.1f}%)")
print(f"  F_BA_new       = {E_BA_new:.4f} M_KK  ({E_BA_new/E_matter_new*100:.1f}%)")
print(f"  F_Leggett_new  = {E_Leggett_new:.4f} M_KK  ({E_Leggett_new/E_matter_new*100:.1f}%)")
print(f"  E_matter_new   = {E_matter_new:.4f} M_KK")
print(f"")
print(f"  f_DM(A) old    = {f_DM_A_old:.4f}")
print(f"  f_DM(A) new    = {f_DM_A_new:.4f}  (shift: {(f_DM_A_new - f_DM_A_old)/f_DM_A_old*100:+.1f}%)")
print(f"  f_DM(B) old    = {f_DM_B_old:.4f}")
print(f"  f_DM(B) new    = {f_DM_B_new:.4f}  (shift: {(f_DM_B_new - f_DM_B_old)/f_DM_B_old*100:+.1f}%)")
print(f"  f_DM(obs)      = {Omega_DM / Omega_m:.4f}")

# =============================================================================
# 4. Sensitivity analysis: conservative vs aggressive mass corrections
# =============================================================================

# Conservative: only epsilon correction, no mass correction on BA
E_BA_conservative = F_BA_old  # unchanged
E_matter_conservative = E_BCS_new + E_BA_conservative + E_Leggett_new
f_DM_A_conservative = E_Leggett_new / E_matter_conservative
f_DM_B_conservative = (E_Leggett_new + E_BCS_new) / E_matter_conservative

# Aggressive: mass correction on all channels (BCS also feels mass)
# BCS gap Delta ~ V * N(E_F), and N(E_F) ~ m*^{d/2}, so for 0D (single cell),
# the density of states is discrete and not directly proportional to mass.
# But the excitation energy E_exc ~ n_pairs * Delta, and Delta ~ epsilon * bandwidth.
# With m_B2_fold, the bandwidth is proportional to the Casimir / m_B2, so the
# modes are compressed. The excitation per pair is E_pair ~ Delta = omega_PV ~ 0.79,
# which is set by the pairing interaction, not the mass directly.
# Keep BCS correction at the epsilon ratio only (conservative for E_BCS).
E_BCS_aggressive = E_BCS_new  # same as above (mass doesn't enter BCS directly in 0D)
E_BA_aggressive = E_BA_new     # mass correction included
E_Leggett_aggressive = E_Leggett_new  # omega_L correction included
E_matter_aggressive = E_BCS_aggressive + E_BA_aggressive + E_Leggett_aggressive
f_DM_A_aggressive = E_Leggett_aggressive / E_matter_aggressive
f_DM_B_aggressive = (E_Leggett_aggressive + E_BCS_aggressive) / E_matter_aggressive

print(f"\n{'='*60}")
print(f"  SENSITIVITY ANALYSIS")
print(f"{'='*60}")
print(f"  Conservative (epsilon only, no mass on BA):")
print(f"    E_matter    = {E_matter_conservative:.4f}")
print(f"    f_DM(A)     = {f_DM_A_conservative:.4f}")
print(f"    f_DM(B)     = {f_DM_B_conservative:.4f}")
print(f"  Full (epsilon + mass on BA):")
print(f"    E_matter    = {E_matter_new:.4f}")
print(f"    f_DM(A)     = {f_DM_A_new:.4f}")
print(f"    f_DM(B)     = {f_DM_B_new:.4f}")

# =============================================================================
# 5. Omega_DM h^2 recalculation
# =============================================================================

h_hubble = H_0_km_s_Mpc / 100.0  # 0.674
Omega_DM_h2_obs = Omega_DM * h_hubble**2  # 0.1207

# Calibration from S57: Omega_DM_h2 = 0.1417 when E_DM = 3.555 M_KK
# This calibration ratio gives us the physical conversion:
# Omega_DM_h2(new) = Omega_DM_h2_B_ref * (E_DM_new / E_DM_ref)

# For variant A: E_DM = E_Leggett
E_DM_A_new = E_Leggett_new
Omega_DM_h2_A_new = Omega_DM_h2_B_ref * (E_DM_A_new / E_DM_ref)

# For variant B: E_DM = E_Leggett + E_BCS
E_DM_B_new = E_Leggett_new + E_BCS_new
Omega_DM_h2_B_new = Omega_DM_h2_B_ref * (E_DM_B_new / E_DM_ref)

# S58 values
Omega_DM_h2_A_old = float(vp_data['canon_observables_A'][0])  # 0.1200

print(f"\n{'='*60}")
print(f"  OMEGA_DM h^2 RECALCULATION")
print(f"{'='*60}")
print(f"  Calibration: Omega_DM_h2_B = {Omega_DM_h2_B_ref:.4f} at E_DM = {E_DM_ref:.3f}")
print(f"  E_DM(A) new = {E_DM_A_new:.4f} M_KK  (was {F_Leggett_old:.4f})")
print(f"  E_DM(B) new = {E_DM_B_new:.4f} M_KK  (was {F_Leggett_old + abs(F_BCS_old):.4f})")
print(f"  Omega_DM h^2 (A) new = {Omega_DM_h2_A_new:.4f}  (was {Omega_DM_h2_A_old:.4f})")
print(f"  Omega_DM h^2 (B) new = {Omega_DM_h2_B_new:.4f}  (was {Omega_DM_h2_B_ref:.4f})")
print(f"  Omega_DM h^2 (obs)   = {Omega_DM_h2_obs:.4f}")

# =============================================================================
# 6. Bayesian Emulator (NROY) with corrected parameters
# =============================================================================
# Same structure as S58 (s58_volovik_partition.py) but with corrected central values.
# Parameter space: (E_J, E_J/E_c, epsilon, N_cells, alpha)

print(f"\n{'='*60}")
print(f"  BAYESIAN EMULATOR WITH CORRECTED BASELINE")
print(f"{'='*60}")

# Canonical parameters (corrected)
E_J_canon = J_C2       # 0.933 M_KK (unchanged)
EJEc_canon = abs(F_Josephson) / N_cells  # ~10.52 (unchanged)
epsilon_canon_new = epsilon_new  # 0.00143 (CORRECTED)

# Observational targets
obs_names = ['Omega_DM_h2', 'Omega_Lambda', 'f_DM', 'w']
obs_targets = np.array([Omega_DM_h2_obs, Omega_Lambda, Omega_DM / Omega_m, -1.0])
obs_sigma = np.array([0.001, 0.007, 0.01, 0.05])
model_sigma = np.array([0.02, 0.05, 0.05, 0.1])

# Grid
n_EJ = 40  # (local)
n_EJEc = 35  # (local)
n_eps = 25  # (local)
n_alpha = 10  # (local)
N_cells_list = np.array([2, 4, 8, 16, 32, 64, 128])
n_Nc = len(N_cells_list)

EJ_grid = np.linspace(0.5, 1.5, n_EJ)
EJEc_grid = np.logspace(-1, 2, n_EJEc)
eps_grid = np.linspace(0.001, 0.005, n_eps)
alpha_grid = np.linspace(-2.5, -1.0, n_alpha)

NROY_threshold = 3.0  # (local)
total_points = n_EJ * n_EJEc * n_eps * n_Nc * n_alpha
print(f"  Grid: {n_EJ} x {n_EJEc} x {n_eps} x {n_Nc} x {n_alpha} = {total_points:,} points")

# Precompute reference values for the emulator function
rho_J_per_cell = abs(F_Josephson) / N_cells  # 10.52 M_KK/cell
rho_GGE = Lambda_eff_MKK_val      # 1.709 M_KK
P_GGE = P_vac_GGE_val             # -0.688 M_KK

def predict_observables_corrected(E_J, EJ_Ec, epsilon, N_c, alpha_in):
    """
    Predict observables under Volovik partition with corrected masses.

    Key difference from S58: uses corrected epsilon baseline and
    includes mass correction for BA sound speed.
    """
    E_c = E_J / EJ_Ec if EJ_Ec > 0 else 1e10

    # Gap scaling: Delta(N) = A * N^alpha
    # Calibrate A to corrected epsilon
    A_eff = A_gap_B * (E_J / E_J_canon)**2 * (epsilon / epsilon_canon_new)
    Delta_N = A_eff * max(N_c, 1)**alpha_in

    # Landau-Zener P_exc
    if Delta_N > 0:
        gamma_N = PI * Delta_N**2 / (2 * E_J * dtau_dt)
        P_exc_N = np.exp(-2 * PI * gamma_N)
        P_exc_N = np.clip(P_exc_N, 0.0, 1.0)
    else:
        P_exc_N = 1.0  # (local)

    # BCS excitation: scales with epsilon (corrected baseline)
    E_BCS_per_cell = abs(E_cond) * (epsilon / epsilon_canon_new)
    E_BCS_total = N_c * E_BCS_per_cell * P_exc_N

    # BA excitation: scales with E_J and sqrt(m_round/m_fold) for mass correction
    n_bonds = max(1, N_c - 1)
    n_bonds_canon = N_cells - 1  # 31
    E_BA_total = F_BA_old * c_s_correction * (n_bonds / n_bonds_canon) * (E_J / E_J_canon)

    # Leggett excitation: scales with omega_L (corrected) and epsilon
    n_L_modes = max(1, N_c - 1)
    n_L_canon = N_cells - 1  # 31
    # omega_L ~ sqrt(J_23 * Delta) ~ sqrt(epsilon * ...), measured ratio is omega_L_ratio
    # For scanning: E_L scales with (epsilon / epsilon_canon_new) * omega_L_ratio factor
    # But omega_L_ratio is already applied at the canonical point.
    # For parameter scanning, the epsilon dependence is sqrt(epsilon) for omega_L:
    omega_L_scaling = np.sqrt(epsilon / epsilon_canon_new)
    E_L_total = E_Leggett_new * (n_L_modes / n_L_canon) * omega_L_scaling

    # Volovik partition: matter = all excitations
    E_matter = E_BCS_total + E_BA_total + E_L_total

    # f_DM = E_Leggett / E_matter (Variant A)
    f_DM_pred = E_L_total / E_matter if E_matter > 0 else 0.0

    # Omega_DM h^2: calibrated to S57 reference
    E_DM_pred = f_DM_pred * E_matter
    Omega_DM_h2_pred = Omega_DM_h2_B_ref * (E_DM_pred / E_DM_ref)

    # Omega_Lambda: scales with E_J (spectral structure)
    Lambda_pred = Lambda_eff_MKK_val * (E_J / E_J_canon)
    Lambda_pred = max(Lambda_pred, 0)
    Omega_Lambda_pred = Omega_Lambda * (Lambda_pred / Lambda_eff_MKK_val)
    Omega_Lambda_pred = np.clip(Omega_Lambda_pred, 0, 1.5)

    # w: from Volovik partition (Josephson + GGE)
    if EJ_Ec > 1:
        frac_GGE = rho_GGE / (rho_J_per_cell * (N_c / N_cells) + rho_GGE)
        w_pred = -1.0 + (1.0 + w_GGE) * frac_GGE
    elif EJ_Ec > 0.01:
        w_pred = w_GGE * (EJ_Ec / 1.0)
    else:
        w_pred = 0.0  # (local)

    return Omega_DM_h2_pred, Omega_Lambda_pred, f_DM_pred, w_pred

# --- Run the grid scan ---
print(f"  Scanning...")

NROY_count_A = 0
NROY_count_B = 0
I_max_best_A = np.inf
I_max_best_B = np.inf
best_params_A = np.zeros(5)
best_params_B = np.zeros(5)
nroy_per_obs_A = np.zeros(4)
nroy_per_obs_B = np.zeros(4)
total_checked = 0

# Track canonical point separately
canon_I_per_obs = np.zeros(4)
canon_observables = np.zeros(4)

for i_ej, E_J in enumerate(EJ_grid):
    for i_ejec, EJ_Ec in enumerate(EJEc_grid):
        for i_eps, eps_val in enumerate(eps_grid):
            for i_nc, N_c in enumerate(N_cells_list):
                for i_alpha, alpha_val in enumerate(alpha_grid):
                    total_checked += 1

                    pred = predict_observables_corrected(E_J, EJ_Ec, eps_val, N_c, alpha_val)
                    preds = np.array(pred)

                    # Implausibility per observable
                    I_per = np.abs(preds - obs_targets) / np.sqrt(obs_sigma**2 + model_sigma**2)
                    I_max = np.max(I_per)

                    # Variant A (Leggett only): uses preds as-is
                    if I_max < I_max_best_A:
                        I_max_best_A = I_max
                        best_params_A = np.array([E_J, EJ_Ec, eps_val, N_c, alpha_val])

                    if I_max < NROY_threshold:
                        NROY_count_A += 1

                    # Per-observable NROY (A)
                    for io in range(4):
                        if I_per[io] < NROY_threshold:
                            nroy_per_obs_A[io] += 1

                    # Variant B: f_DM includes BCS as DM
                    E_BCS_per_cell_b = abs(E_cond) * (eps_val / epsilon_canon_new)
                    P_exc_b = pred[2]  # proxy: use f_DM_A to estimate DM fraction with BCS
                    # For variant B, recalculate f_DM_B from components
                    # We need to back-calculate E components
                    n_bonds_b = max(1, N_c - 1)
                    n_bonds_c = N_cells - 1
                    E_BA_b = F_BA_old * c_s_correction * (n_bonds_b / n_bonds_c) * (E_J / E_J_canon)

                    omega_L_sc = np.sqrt(eps_val / epsilon_canon_new)
                    n_L_b = max(1, N_c - 1)
                    n_L_c = N_cells - 1
                    E_L_b = E_Leggett_new * (n_L_b / n_L_c) * omega_L_sc

                    # BCS excitation with LZ
                    A_eff_b = A_gap_B * (E_J / E_J_canon)**2 * (eps_val / epsilon_canon_new)
                    Delta_N_b = A_eff_b * max(N_c, 1)**alpha_val
                    if Delta_N_b > 0:
                        gamma_b = PI * Delta_N_b**2 / (2 * E_J * dtau_dt)
                        P_exc_b_val = np.exp(-2 * PI * gamma_b)
                        P_exc_b_val = np.clip(P_exc_b_val, 0.0, 1.0)
                    else:
                        P_exc_b_val = 1.0  # (local)
                    E_BCS_b = N_c * E_BCS_per_cell_b * P_exc_b_val

                    E_matter_b = E_BCS_b + E_BA_b + E_L_b
                    f_DM_B = (E_L_b + E_BCS_b) / E_matter_b if E_matter_b > 0 else 0.0

                    preds_B = preds.copy()
                    preds_B[2] = f_DM_B  # Replace f_DM with variant B
                    # Omega_DM_h2 for B: uses (E_L + E_BCS) as DM
                    E_DM_B = (E_L_b + E_BCS_b)
                    preds_B[0] = Omega_DM_h2_B_ref * (E_DM_B / E_DM_ref)

                    I_per_B = np.abs(preds_B - obs_targets) / np.sqrt(obs_sigma**2 + model_sigma**2)
                    I_max_B = np.max(I_per_B)

                    if I_max_B < I_max_best_B:
                        I_max_best_B = I_max_B
                        best_params_B = np.array([E_J, EJ_Ec, eps_val, N_c, alpha_val])

                    if I_max_B < NROY_threshold:
                        NROY_count_B += 1

                    for io in range(4):
                        if I_per_B[io] < NROY_threshold:
                            nroy_per_obs_B[io] += 1

# Evaluate canonical point
canon_pred = predict_observables_corrected(E_J_canon, EJEc_canon, epsilon_canon_new, N_cells, alpha_gap)
canon_observables = np.array(canon_pred)
canon_I_per_obs = np.abs(canon_observables - obs_targets) / np.sqrt(obs_sigma**2 + model_sigma**2)
canon_Imax = np.max(canon_I_per_obs)
canon_in_NROY = canon_Imax < NROY_threshold

NROY_frac_A = NROY_count_A / total_checked
NROY_frac_B = NROY_count_B / total_checked
nroy_per_obs_A /= total_checked
nroy_per_obs_B /= total_checked

print(f"\n{'='*60}")
print(f"  NROY RESULTS")
print(f"{'='*60}")
print(f"  Total points scanned: {total_checked:,}")
print(f"")
print(f"  Variant A (Leggett only as DM):")
print(f"    NROY count:  {NROY_count_A}")
print(f"    NROY frac:   {NROY_frac_A*100:.4f}%")
print(f"    Best I_max:  {I_max_best_A:.3f}")
print(f"    Best params: E_J={best_params_A[0]:.3f}, E_J/E_c={best_params_A[1]:.2f}, "
      f"eps={best_params_A[2]:.5f}, N={best_params_A[3]:.0f}, alpha={best_params_A[4]:.2f}")
print(f"    Per-observable NROY: ", end="")
for io in range(4):
    print(f"{obs_names[io]}={nroy_per_obs_A[io]*100:.1f}%  ", end="")
print()
print(f"")
print(f"  Variant B (Leggett + BCS as DM):")
print(f"    NROY count:  {NROY_count_B}")
print(f"    NROY frac:   {NROY_frac_B*100:.4f}%")
print(f"    Best I_max:  {I_max_best_B:.3f}")
print(f"    Best params: E_J={best_params_B[0]:.3f}, E_J/E_c={best_params_B[1]:.2f}, "
      f"eps={best_params_B[2]:.5f}, N={best_params_B[3]:.0f}, alpha={best_params_B[4]:.2f}")
print(f"    Per-observable NROY: ", end="")
for io in range(4):
    print(f"{obs_names[io]}={nroy_per_obs_B[io]*100:.1f}%  ", end="")
print()
print(f"")
print(f"  Canonical point (corrected):")
print(f"    Predictions: {canon_observables}")
print(f"    Targets:     {obs_targets}")
print(f"    I per obs:   {canon_I_per_obs}")
print(f"    I_max:       {canon_Imax:.3f}")
print(f"    In NROY:     {canon_in_NROY}")

# =============================================================================
# 7. Comparison with S58
# =============================================================================

print(f"\n{'='*60}")
print(f"  COMPARISON WITH S58 (UNCORRECTED)")
print(f"{'='*60}")

NROY_frac_A_old = float(vp_data['NROY_frac_A'])
NROY_frac_B_old = float(vp_data['NROY_frac_B'])
I_max_best_A_old = float(vp_data['I_max_best_A'])
I_max_best_B_old = float(vp_data['I_max_best_B'])
canon_Imax_old = float(vp_data['canon_Imax'])

print(f"                          S58 (old)    S59 (corrected)")
print(f"  epsilon (canonical):    {epsilon_old:.5f}     {epsilon_new:.5f}")
print(f"  m_B2:                   {m_B2_round:.4f}       {m_B2_fold:.4f}")
print(f"  E_matter (M_KK):        {E_matter_old:.3f}      {E_matter_new:.4f}")
print(f"  f_DM(A):                {f_DM_A_old:.4f}       {f_DM_A_new:.4f}")
print(f"  f_DM(B):                {f_DM_B_old:.4f}       {f_DM_B_new:.4f}")
print(f"  Omega_DM h^2 (A):       {Omega_DM_h2_A_old:.4f}       {Omega_DM_h2_A_new:.4f}")
print(f"  Omega_DM h^2 (B):       {Omega_DM_h2_B_ref:.4f}       {Omega_DM_h2_B_new:.4f}")
print(f"  NROY(A):                {NROY_frac_A_old*100:.4f}%      {NROY_frac_A*100:.4f}%")
print(f"  NROY(B):                {NROY_frac_B_old*100:.4f}%      {NROY_frac_B*100:.4f}%")
print(f"  I_max best(A):          {I_max_best_A_old:.3f}        {I_max_best_A:.3f}")
print(f"  I_max best(B):          {I_max_best_B_old:.3f}        {I_max_best_B:.3f}")
print(f"  Canon I_max:            {canon_Imax_old:.3f}       {canon_Imax:.3f}")

# =============================================================================
# 8. Gate verdict
# =============================================================================

print(f"\n{'='*60}")
print(f"  GATE VERDICT: DM-RECALC-59")
print(f"{'='*60}")

if f_DM_B_new > 0.50:
    gate_verdict = "PASS"
    gate_detail = f"f_DM(B) = {f_DM_B_new:.4f} > 0.50. Still within striking distance."
elif f_DM_B_new < 0.30:
    gate_verdict = "FAIL"
    gate_detail = f"f_DM(B) = {f_DM_B_new:.4f} < 0.30. Geometric corrections kill Variant B."
else:
    gate_verdict = "INFO"
    gate_detail = f"f_DM(B) = {f_DM_B_new:.4f} in [0.30, 0.50]. Intermediate regime."

print(f"  Verdict:  {gate_verdict}")
print(f"  f_DM(B):  {f_DM_B_new:.4f}")
print(f"  Detail:   {gate_detail}")

# Context from W0-1:
print(f"\n  CONTEXT: W0-1 found f_DM(z=0) = 1.000 (PASS).")
print(f"  BA phonons redshift away, BCS annihilates. Only Leggett survives.")
print(f"  At z=0, f_DM = 1.0 within the substrate sector regardless of transit-epoch budget.")
print(f"  This corrected transit-epoch baseline is needed for consistency but")
print(f"  is NO LONGER the binding constraint on DM abundance.")

# =============================================================================
# 9. Save data
# =============================================================================

np.savez(os.path.join(outdir, 's59_dm_recalc.npz'),
    # Corrections applied
    epsilon_old=epsilon_old,
    epsilon_new=epsilon_new,
    epsilon_ratio=epsilon_ratio,
    m_B2_round=m_B2_round,
    m_B2_fold=m_B2_fold,
    mass_ratio=mass_ratio,
    omega_L0_old=omega_L0_old,
    omega_L0_new=omega_L0_new,
    omega_L_ratio=omega_L_ratio,
    c_s_correction=c_s_correction,
    # Old energy budget
    E_BCS_old=abs(F_BCS_old),
    E_BA_old=F_BA_old,
    E_Leggett_old=F_Leggett_old,
    E_matter_old=E_matter_old,
    f_DM_A_old=f_DM_A_old,
    f_DM_B_old=f_DM_B_old,
    # New energy budget
    E_BCS_new=E_BCS_new,
    E_BA_new=E_BA_new,
    E_Leggett_new=E_Leggett_new,
    E_matter_new=E_matter_new,
    f_DM_A_new=f_DM_A_new,
    f_DM_B_new=f_DM_B_new,
    # Omega_DM h^2
    Omega_DM_h2_A_new=Omega_DM_h2_A_new,
    Omega_DM_h2_B_new=Omega_DM_h2_B_new,
    Omega_DM_h2_obs=Omega_DM_h2_obs,
    # NROY results
    NROY_frac_A=NROY_frac_A,
    NROY_count_A=NROY_count_A,
    NROY_frac_B=NROY_frac_B,
    NROY_count_B=NROY_count_B,
    I_max_best_A=I_max_best_A,
    I_max_best_B=I_max_best_B,
    best_params_A=best_params_A,
    best_params_B=best_params_B,
    nroy_per_obs_A=nroy_per_obs_A,
    nroy_per_obs_B=nroy_per_obs_B,
    canon_observables=canon_observables,
    canon_I_per_obs=canon_I_per_obs,
    canon_Imax=canon_Imax,
    canon_in_NROY=canon_in_NROY,
    # Sensitivity
    f_DM_A_conservative=f_DM_A_conservative,
    f_DM_B_conservative=f_DM_B_conservative,
    E_matter_conservative=E_matter_conservative,
    # Metadata
    obs_names=np.array(obs_names),
    obs_targets=obs_targets,
    obs_sigma=obs_sigma,
    model_sigma=model_sigma,
    total_points=total_checked,
    NROY_threshold=NROY_threshold,
    gate_name=np.array(['DM-RECALC-59']),
    gate_verdict=np.array([gate_verdict]),
    gate_detail=np.array([gate_detail]),
)
print(f"\n  Saved: s59_dm_recalc.npz")

# =============================================================================
# 10. Plot
# =============================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('DM-RECALC-59: Corrected DM Abundance Baseline', fontsize=14, fontweight='bold')

# Panel 1: Energy budget comparison (bar chart)
ax = axes[0, 0]
labels_bar = ['|E_BCS|', 'E_BA', 'E_Leggett']
old_vals = [abs(F_BCS_old), F_BA_old, F_Leggett_old]
new_vals = [E_BCS_new, E_BA_new, E_Leggett_new]
x = np.arange(len(labels_bar))
width = 0.35  # (local)
bars1 = ax.bar(x - width/2, old_vals, width, label=f'S58 (eps={epsilon_old:.5f})', color='steelblue', alpha=0.8)
bars2 = ax.bar(x + width/2, new_vals, width, label=f'S59 (eps={epsilon_new:.5f})', color='coral', alpha=0.8)
ax.set_ylabel('Energy (M_KK)')
ax.set_title('Energy Budget: S58 vs S59 Corrected')
ax.set_xticks(x)
ax.set_xticklabels(labels_bar)
ax.legend()
for b in bars1:
    ax.text(b.get_x() + b.get_width()/2, b.get_height() + 0.1, f'{b.get_height():.2f}',
            ha='center', va='bottom', fontsize=8)
for b in bars2:
    ax.text(b.get_x() + b.get_width()/2, b.get_height() + 0.1, f'{b.get_height():.2f}',
            ha='center', va='bottom', fontsize=8)

# Panel 2: f_DM comparison
ax = axes[0, 1]
categories = ['f_DM(A)\nLeggett', 'f_DM(B)\nLegg+BCS', 'f_DM(obs)']
old_fdm = [f_DM_A_old, f_DM_B_old, Omega_DM / Omega_m]
new_fdm = [f_DM_A_new, f_DM_B_new, Omega_DM / Omega_m]
x2 = np.arange(len(categories))
ax.bar(x2 - width/2, old_fdm, width, label='S58', color='steelblue', alpha=0.8)
ax.bar(x2 + width/2, new_fdm, width, label='S59 corrected', color='coral', alpha=0.8)
ax.axhline(y=0.50, color='green', linestyle='--', alpha=0.5, label='PASS threshold')
ax.axhline(y=0.30, color='red', linestyle='--', alpha=0.5, label='FAIL threshold')
ax.set_ylabel('f_DM')
ax.set_title('f_DM: S58 vs S59 Corrected')
ax.set_xticks(x2)
ax.set_xticklabels(categories)
ax.legend(fontsize=8)
for i, (v_old, v_new) in enumerate(zip(old_fdm, new_fdm)):
    ax.text(i - width/2, v_old + 0.02, f'{v_old:.3f}', ha='center', va='bottom', fontsize=8)
    ax.text(i + width/2, v_new + 0.02, f'{v_new:.3f}', ha='center', va='bottom', fontsize=8)

# Panel 3: Per-observable implausibility at canonical
ax = axes[1, 0]
# Old canonical I per obs
canon_I_old = np.array([float(x) for x in vp_data['canon_I_per_obs']])
x3 = np.arange(4)
ax.bar(x3 - width/2, canon_I_old, width, label='S58', color='steelblue', alpha=0.8)
ax.bar(x3 + width/2, canon_I_per_obs, width, label='S59 corrected', color='coral', alpha=0.8)
ax.axhline(y=NROY_threshold, color='red', linestyle='--', alpha=0.5, label=f'NROY threshold ({NROY_threshold})')
ax.set_ylabel('Implausibility I')
ax.set_title('Per-Observable Implausibility at Canonical Point')
ax.set_xticks(x3)
ax.set_xticklabels(obs_names, fontsize=9)
ax.legend(fontsize=8)
ax.set_yscale('symlog', linthresh=1)

# Panel 4: Summary text
ax = axes[1, 1]
ax.axis('off')
summary_text = (
    f"DM-RECALC-59 SUMMARY\n"
    f"{'='*40}\n"
    f"\n"
    f"Corrections applied:\n"
    f"  epsilon: {epsilon_old:.5f} -> {epsilon_new:.5f} (-{(1-epsilon_ratio)*100:.0f}%)\n"
    f"  m_B2:   {m_B2_round:.3f} -> {m_B2_fold:.3f} M_KK (-{(1-mass_ratio)*100:.0f}%)\n"
    f"  omega_L: {omega_L0_old:.4f} -> {omega_L0_new:.4f} M_KK (-{(1-omega_L_ratio)*100:.0f}%)\n"
    f"\n"
    f"Energy budget (M_KK):\n"
    f"  E_matter: {E_matter_old:.3f} -> {E_matter_new:.3f}\n"
    f"\n"
    f"f_DM results:\n"
    f"  A (Leggett):    {f_DM_A_old:.4f} -> {f_DM_A_new:.4f}\n"
    f"  B (Legg+BCS):   {f_DM_B_old:.4f} -> {f_DM_B_new:.4f}\n"
    f"  Observed:        {Omega_DM / Omega_m:.4f}\n"
    f"\n"
    f"NROY (threshold={NROY_threshold}):\n"
    f"  A: {NROY_frac_A_old*100:.3f}% -> {NROY_frac_A*100:.3f}%\n"
    f"  B: {NROY_frac_B_old*100:.3f}% -> {NROY_frac_B*100:.3f}%\n"
    f"\n"
    f"Gate: {gate_verdict}\n"
    f"\n"
    f"Context: W0-1 f_DM(z=0) = 1.000\n"
    f"Transit-epoch budget no longer\n"
    f"the binding constraint."
)
ax.text(0.05, 0.95, summary_text, transform=ax.transAxes, fontsize=9,
        verticalalignment='top', fontfamily='monospace',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

plt.tight_layout()
plt.savefig(os.path.join(outdir, 's59_dm_recalc.png'), dpi=150, bbox_inches='tight')
print(f"  Saved: s59_dm_recalc.png")

print(f"\n{'='*60}")
print(f"  COMPLETE")
print(f"{'='*60}")
