#!/usr/bin/env python3
"""
s57_bayesian_fabric.py — BAYESIAN-FABRIC-57 (W3-5)
=====================================================
Gate: INFO — Does Bayesian history-matching constrain the fabric parameters?

Method: Apply Paper 06 (Bayesian history matching) methodology to the fabric
parameter space {E_J, E_c, epsilon, N_cells}, using S57 scaling relations
and Planck observables.

The implausibility function:
    I(x) = max_i |O_pred_i(x) - O_obs_i| / sqrt(sigma_pred_i^2 + sigma_obs_i^2)

NROY region: I(x) < 3 (not ruled out yet).

Input: All W1-W2 output .npz files, canonical_constants.py
Output: s57_bayesian_fabric.npz
"""

import sys
sys.path.insert(0, 'computations')
import numpy as np
from scipy.special import comb
from canonical_constants import (
    J_C2 as J_C2_canonical, tau_fold, N_cells as N_cells_canon,
    E_cond, Omega_DM, Omega_Lambda, Omega_m, Omega_b,
    rho_Lambda_obs, rho_crit_GeV4, M_KK, PI,
    Delta_0_GL, S_inst, omega_PV, xi_BCS,
    E_exc_ratio, n_pairs,
    omega_L1, omega_L2, omega_H1, c_Gold,
    H_0_km_s_Mpc, h_planck_SI
)

# =============================================================================
# 1. Load S57 W-round results
# =============================================================================
ft = np.load('computations/session-57/s57_finite_rate_transit.npz', allow_pickle=True)
lp = np.load('computations/session-57/s57_leggett_partition.npz', allow_pickle=True)
gs = np.load('computations/session-57/s57_gap_scaling.npz', allow_pickle=True)
dm = np.load('computations/session-57/s57_fabric_dm_abundance.npz', allow_pickle=True)
cc = np.load('computations/session-57/s57_cc_sign.npz', allow_pickle=True)

print("=== S57 W-round results loaded ===")
print(f"  W1-1 P_exc (2-cell, physical rate): {float(ft['P_exc_final']):.4f}")
print(f"  W1-2 f_DM (Leggett channel):        {float(lp['f_DM_end_S49']):.4f}")
print(f"  W1-3 alpha (gap scaling exponent):   {float(gs['alpha_physical']):.4f}")
print(f"  W2-4 Omega_DM h^2 (Model A):        {float(dm['Omega_DM_h2_pred_A']):.4f}")
print(f"  W2-4 Omega_DM h^2 (Model B):        {float(dm['Omega_DM_h2_pred_B']):.4f}")
print(f"  W2-3 Lambda_eff (M_KK units):       {float(cc['Lambda_eff_MKK']):.4f}")
print(f"  W2-3 w_GGE:                         {float(cc['w_GGE']):.4f}")

# =============================================================================
# 2. Define parameter space
# =============================================================================
# Four fabric parameters:
#   E_J:     Josephson coupling (M_KK units). Canonical = 0.933
#   E_c:     Charging energy = 1/(2*N_cells*C). Related to E_J via E_J/E_c ratio
#   epsilon: BCS coupling strength = |E_cond|/E_J^2. Canonical = 0.00248
#   N_cells: Number of Voronoi cells. Canonical = 32

# Parameter ranges
E_J_range = np.linspace(0.5, 1.5, 50)      # M_KK
# E_c derived from E_J/E_c ratio, which determines Mott vs SF phase (Paper 19-22)
EJ_over_Ec_range = np.linspace(0.1, 100, 50)  # E_J/E_c ratio
epsilon_range = np.linspace(0.001, 0.005, 30)  # BCS coupling
N_cells_list = np.array([2, 4, 8, 16, 32, 64, 128])

# Canonical values
E_J_canon = J_C2_canonical  # 0.933
epsilon_canon = abs(E_cond) / E_J_canon**2  # 0.137 / 0.870 = 0.157
# Wait - epsilon is the bare coupling g, not E_cond/E_J^2
# From canonical: epsilon = dimensionless BCS coupling
# In the framework: g*N(E_F) determines BCS, and E_cond = -N(0)*Delta^2/2
# The relevant parameter is the Josephson-to-charging ratio for the fabric

# From W1-2: E_J = J_C2 * N_cells = 0.933 * 32 = 29.86 (total Josephson energy)
# From W1-2: F_Josephson = -336.64 (dominates by 1-3 orders)
# E_c ~ 1/N_cells for capacitive coupling

# Redefine epsilon as the BCS dimensionless coupling from S35:
# g*N(E_F) = 2.18 (from S37). But this is a single-cell quantity.
# For the fabric: epsilon = g*N(E_F) / N_cells (diluted coupling)
# Actually, epsilon in the prompt = 0.00248, which matches:
epsilon_canonical = 0.00248  # As specified in prompt  # (local)
print(f"\n  Canonical epsilon: {epsilon_canonical}")
print(f"  Canonical E_J: {E_J_canon:.3f}")
print(f"  E_cond/E_J^2: {abs(E_cond)/E_J_canon**2:.5f}")

# =============================================================================
# 3. Define observables and their measured values
# =============================================================================
# Observable 1: Omega_DM h^2
h = H_0_km_s_Mpc / 100  # 0.674
Omega_DM_h2_obs = Omega_DM * h**2  # 0.266 * 0.454 = 0.1208
sigma_Omega_DM_h2 = 0.001  # Planck 2018  # (local)

# Observable 2: Omega_Lambda
Omega_Lambda_obs = Omega_Lambda  # 0.685
sigma_Omega_Lambda = 0.01  # (local)

# Observable 3: f_DM = E_DM / E_matter = Omega_DM / Omega_m
f_DM_obs = Omega_DM / Omega_m  # 0.844
sigma_f_DM = 0.02  # derived uncertainty  # (local)

# Observable 4: w (equation of state)
w_obs = -1.0  # Lambda-CDM  # (local)
sigma_w = 0.05  # Planck + DESI  # (local)

print(f"\n=== Observables ===")
print(f"  Omega_DM h^2 = {Omega_DM_h2_obs:.4f} +/- {sigma_Omega_DM_h2}")
print(f"  Omega_Lambda = {Omega_Lambda_obs:.3f} +/- {sigma_Omega_Lambda}")
print(f"  f_DM = {f_DM_obs:.3f} +/- {sigma_f_DM}")
print(f"  w = {w_obs:.1f} +/- {sigma_w}")

# =============================================================================
# 4. Build the emulator: scaling relations from S57
# =============================================================================
# From W1-3 (GAP-SCALING-57):
#   Delta(N) ~ A * N^alpha where alpha = -1.84
#   P_exc(N) depends on gap through LZ formula
alpha_gap = float(gs['alpha_physical'])  # -1.84
A_gap_B = float(gs['A_fit_B_large'])   # 50.26 for Model B
gap_32B = float(gs['gap_B_N32'])        # 0.0849

# From W1-1 (FINITE-RATE-TRANSIT-57):
#   P_exc at physical rate for 2 cells = 0.081
P_exc_2cell = float(ft['P_exc_final'])  # 0.081
dtau_dt = float(ft['dtau_dt_phys'])     # 442.4

# From W1-2 (LEGGETT-PARTITION-57):
#   f_DM(Leggett channel) = 0.119
f_DM_Leggett_2cell = float(lp['f_DM_end_S49'])  # 0.119
E_matter_2cell = float(lp['E_matter'])            # 11.40
E_L_2cell = float(lp['E_L_end_S49'])             # 1.359
F_Josephson = float(lp['F_Josephson'])            # -336.64

# From W2-4 (FABRIC-DM-ABUNDANCE-57):
#   Omega_DM h^2 in [0.040, 0.142] bracket
Omega_DM_h2_A = float(dm['Omega_DM_h2_pred_A'])  # 0.0446
Omega_DM_h2_B = float(dm['Omega_DM_h2_pred_B'])  # 0.1417

# From W2-3 (CC-SIGN-57):
#   Lambda_eff > 0 (PASS), w_GGE = -0.408
Lambda_eff_MKK = float(cc['Lambda_eff_MKK'])  # 1.709
w_GGE = float(cc['w_GGE'])                     # -0.408

print(f"\n=== Scaling relations from S57 ===")
print(f"  Gap scaling: Delta(N) = {A_gap_B:.2f} * N^({alpha_gap:.2f})")
print(f"  P_exc(N=2) = {P_exc_2cell:.4f}")
print(f"  f_DM(Leggett, N=2) = {f_DM_Leggett_2cell:.4f}")
print(f"  E_matter(N=2) = {E_matter_2cell:.3f}")
print(f"  E_Leggett(N=2) = {E_L_2cell:.4f}")
print(f"  F_Josephson(N=2) = {F_Josephson:.2f}")

# =============================================================================
# 5. Emulator functions
# =============================================================================

def predict_observables(E_J, EJ_Ec, epsilon, N_cells):
    """
    Predict observables given fabric parameters.

    Returns: (Omega_DM_h2, Omega_Lambda, f_DM, w)
    """
    E_c = E_J / EJ_Ec if EJ_Ec > 0 else 1e10

    # --- Gap scaling ---
    # Delta(N) = A * N^alpha, with A calibrated to canonical
    # A depends on E_J: stronger coupling = larger gap
    A_eff = A_gap_B * (E_J / E_J_canon)**2 * (epsilon / epsilon_canonical)
    Delta_N = A_eff * N_cells**alpha_gap

    # --- P_exc from Landau-Zener ---
    # P_exc = exp(-pi * Delta^2 / (2 * hbar * |dH/dt|))
    # |dH/dt| = E_J * dtau_dt (the transit rate times the coupling)
    dH_dt = E_J * dtau_dt
    if Delta_N > 0 and dH_dt > 0:
        gamma_LZ = PI * Delta_N**2 / (2 * dH_dt)
        P_exc_N = 1 - np.exp(-gamma_LZ)  # probability to stay in ground state? No...
        # Actually, P_LZ = exp(-2*pi*gamma) is transition probability
        # P_exc = 1 means fully excited. At physical rate, P_exc ~ 0.08 for 2 cells
        # Calibrate: at canonical, P_exc(2) = 0.081
        # gamma_LZ_canon = pi * gap_2cell^2 / (2 * E_J_canon * dtau_dt)
        gap_2cell_canon = float(gs['gap_A_N2'])  # 0.370
        gamma_LZ_canon = PI * gap_2cell_canon**2 / (2 * E_J_canon * dtau_dt)

        # Use relative scaling
        gamma_ratio = (Delta_N / gap_2cell_canon)**2 * (E_J_canon / E_J) * (2 / N_cells)
        # P_exc scales inversely with gap^2/rate
        P_exc_N = P_exc_2cell * np.exp(-gamma_ratio + 1)  # normalized
        P_exc_N = np.clip(P_exc_N, 0, 1)
    else:
        P_exc_N = 1.0  # (local)

    # --- BCS condensation energy ---
    # E_BCS ~ N_cells * E_cond * (epsilon / epsilon_canonical)
    E_BCS_per_cell = abs(E_cond) * (epsilon / epsilon_canonical)
    E_BCS_total = N_cells * E_BCS_per_cell

    # --- Leggett energy ---
    # E_Leggett scales with N_cells-1 inter-cell bonds and P_exc per mode
    n_bonds = max(1, N_cells - 1)  # linear chain approximation
    n_Leggett_modes = min(N_cells - 1, 31)  # capped at 31 from W1-2
    # E_Leggett per mode ~ omega_L * P_exc (each excited Leggett mode contributes)
    omega_L_mean = (omega_L1 + omega_L2) / 2  # 0.165
    E_Leggett_total = n_Leggett_modes * omega_L_mean * P_exc_N

    # --- DM abundance ---
    # DM = BCS quasiparticle excitations + Leggett channel
    E_DM = E_BCS_total * P_exc_N + E_Leggett_total

    # Total matter energy = Josephson + BCS + kinetic
    # F_Josephson scales as N_cells * E_J (dominant term)
    E_Josephson = N_cells * E_J
    E_kinetic = N_cells * E_c  # charging energy contribution
    E_total = E_Josephson + E_BCS_total + E_kinetic + E_Leggett_total

    if E_total > 0:
        f_DM_pred = E_DM / E_total
    else:
        f_DM_pred = 0.0  # (local)

    # Omega_DM h^2
    # Scale from canonical: Omega_DM_h2 ~ f_DM * (E_total / E_total_canon)
    E_total_canon = N_cells_canon * E_J_canon + N_cells_canon * abs(E_cond) + E_L_2cell * 16
    Omega_DM_h2_pred = Omega_DM_h2_A * (f_DM_pred / 0.0446) * (E_total / E_total_canon)
    Omega_DM_h2_pred = max(0, Omega_DM_h2_pred)

    # --- Cosmological constant ---
    # Lambda = E_GGE - E_eq (the gap between GGE and thermal equilibrium)
    # From W2-3: Lambda_eff = 1.709 M_KK for canonical parameters
    # Scaling: Lambda ~ E_J * P_exc (the un-thermalized energy is Josephson-scale)
    Lambda_pred = Lambda_eff_MKK * (E_J / E_J_canon) * (P_exc_N / P_exc_2cell)

    # Omega_Lambda ~ Lambda / (3*H^2)
    # In our units, Lambda is already in M_KK. Convert to Omega_Lambda:
    # Omega_Lambda_pred = Lambda_pred / Lambda_eff_MKK * Omega_Lambda_obs
    # This is the ratio of predicted to canonical Lambda
    if Lambda_eff_MKK > 0:
        Omega_Lambda_pred = Omega_Lambda_obs * (Lambda_pred / Lambda_eff_MKK)
    else:
        Omega_Lambda_pred = 0.0  # (local)
    Omega_Lambda_pred = np.clip(Omega_Lambda_pred, 0, 1)

    # --- Equation of state ---
    # w = P/rho. For GGE: w_GGE = -0.408 (from W2-3)
    # w depends on E_J/E_c ratio (Josephson array phase diagram)
    # In the superfluid phase (E_J/E_c >> 1): w -> -1 (cosmological constant-like)
    # In the Mott phase (E_J/E_c << 1): w -> 0 (matter-like)
    # Interpolation:
    if EJ_Ec > 0:
        w_pred = -1.0 / (1.0 + 1.0/EJ_Ec)  # approaches -1 for large E_J/E_c
    else:
        w_pred = 0.0  # (local)

    return Omega_DM_h2_pred, Omega_Lambda_pred, f_DM_pred, w_pred

# =============================================================================
# 6. Compute implausibility on grid
# =============================================================================
print("\n=== Computing implausibility grid ===")

# Model uncertainty (accounts for emulator approximation)
sigma_model_DM = 0.03    # 3% model uncertainty on Omega_DM h^2  # (local)
sigma_model_Lambda = 0.1  # 10% on Omega_Lambda  # (local)
sigma_model_fDM = 0.1     # 10% on f_DM  # (local)
sigma_model_w = 0.2       # 20% on w  # (local)

# Build 4D grid (use coarser for tractability, then refine NROY)
n_EJ = 40  # (local)
n_EJEc = 40  # (local)
n_eps = 25  # (local)
n_Ncells = len(N_cells_list)

EJ_grid = np.linspace(0.5, 1.5, n_EJ)
EJEc_grid = np.logspace(-1, 2, n_EJEc)  # 0.1 to 100
eps_grid = np.linspace(0.001, 0.005, n_eps)

# Store results
I_max_all = np.full((n_EJ, n_EJEc, n_eps, n_Ncells), np.inf)
I_DM_all = np.full((n_EJ, n_EJEc, n_eps, n_Ncells), np.inf)
I_Lambda_all = np.full((n_EJ, n_EJEc, n_eps, n_Ncells), np.inf)
I_fDM_all = np.full((n_EJ, n_EJEc, n_eps, n_Ncells), np.inf)
I_w_all = np.full((n_EJ, n_EJEc, n_eps, n_Ncells), np.inf)

O_DM_pred = np.zeros((n_EJ, n_EJEc, n_eps, n_Ncells))
O_Lambda_pred = np.zeros((n_EJ, n_EJEc, n_eps, n_Ncells))
O_fDM_pred = np.zeros((n_EJ, n_EJEc, n_eps, n_Ncells))
O_w_pred = np.zeros((n_EJ, n_EJEc, n_eps, n_Ncells))

for i, ej in enumerate(EJ_grid):
    for j, ejec in enumerate(EJEc_grid):
        for k, eps in enumerate(eps_grid):
            for l, nc in enumerate(N_cells_list):
                try:
                    o_dm, o_lam, o_fdm, o_w = predict_observables(ej, ejec, eps, nc)
                except:
                    continue

                O_DM_pred[i, j, k, l] = o_dm
                O_Lambda_pred[i, j, k, l] = o_lam
                O_fDM_pred[i, j, k, l] = o_fdm
                O_w_pred[i, j, k, l] = o_w

                # Implausibility for each observable
                sigma_tot_DM = np.sqrt(sigma_Omega_DM_h2**2 + sigma_model_DM**2)
                sigma_tot_Lambda = np.sqrt(sigma_Omega_Lambda**2 + sigma_model_Lambda**2)
                sigma_tot_fDM = np.sqrt(sigma_f_DM**2 + sigma_model_fDM**2)
                sigma_tot_w = np.sqrt(sigma_w**2 + sigma_model_w**2)

                I_dm = abs(o_dm - Omega_DM_h2_obs) / sigma_tot_DM
                I_lam = abs(o_lam - Omega_Lambda_obs) / sigma_tot_Lambda
                I_fdm = abs(o_fdm - f_DM_obs) / sigma_tot_fDM
                I_w = abs(o_w - w_obs) / sigma_tot_w

                I_DM_all[i, j, k, l] = I_dm
                I_Lambda_all[i, j, k, l] = I_lam
                I_fDM_all[i, j, k, l] = I_fdm
                I_w_all[i, j, k, l] = I_w

                I_max_all[i, j, k, l] = max(I_dm, I_lam, I_fdm, I_w)

# =============================================================================
# 7. Identify NROY region
# =============================================================================
NROY_threshold = 3.0  # (local)
NROY_mask = I_max_all < NROY_threshold

total_points = I_max_all.size
NROY_count = np.sum(NROY_mask)
NROY_fraction = NROY_count / total_points

print(f"\n=== NROY Analysis ===")
print(f"Total grid points: {total_points}")
print(f"NROY points (I < 3): {NROY_count}")
print(f"NROY volume fraction: {NROY_fraction:.4f} ({NROY_fraction*100:.2f}%)")

# Which observable is most constraining?
NROY_DM = np.sum(I_DM_all < NROY_threshold) / total_points
NROY_Lambda = np.sum(I_Lambda_all < NROY_threshold) / total_points
NROY_fDM = np.sum(I_fDM_all < NROY_threshold) / total_points
NROY_w = np.sum(I_w_all < NROY_threshold) / total_points

print(f"\nNROY fractions by observable:")
print(f"  Omega_DM h^2: {NROY_DM:.4f} ({NROY_DM*100:.1f}%)")
print(f"  Omega_Lambda:  {NROY_Lambda:.4f} ({NROY_Lambda*100:.1f}%)")
print(f"  f_DM:          {NROY_fDM:.4f} ({NROY_fDM*100:.1f}%)")
print(f"  w:             {NROY_w:.4f} ({NROY_w*100:.1f}%)")

most_constraining = ['Omega_DM_h2', 'Omega_Lambda', 'f_DM', 'w'][
    np.argmin([NROY_DM, NROY_Lambda, NROY_fDM, NROY_w])]
print(f"  Most constraining: {most_constraining}")

# =============================================================================
# 8. Marginal NROY ranges for each parameter
# =============================================================================
print(f"\n=== Marginal NROY ranges ===")

# E_J
EJ_NROY = np.any(NROY_mask, axis=(1, 2, 3))
if np.any(EJ_NROY):
    EJ_min = EJ_grid[EJ_NROY].min()
    EJ_max = EJ_grid[EJ_NROY].max()
    print(f"  E_J: [{EJ_min:.3f}, {EJ_max:.3f}] M_KK (canonical: {E_J_canon:.3f})")
else:
    print(f"  E_J: EMPTY NROY")
    EJ_min = EJ_max = np.nan

# E_J/E_c
EJEc_NROY = np.any(NROY_mask, axis=(0, 2, 3))
if np.any(EJEc_NROY):
    EJEc_min = EJEc_grid[EJEc_NROY].min()
    EJEc_max = EJEc_grid[EJEc_NROY].max()
    print(f"  E_J/E_c: [{EJEc_min:.3f}, {EJEc_max:.3f}]")
else:
    print(f"  E_J/E_c: EMPTY NROY")
    EJEc_min = EJEc_max = np.nan

# epsilon
eps_NROY = np.any(NROY_mask, axis=(0, 1, 3))
if np.any(eps_NROY):
    eps_min = eps_grid[eps_NROY].min()
    eps_max = eps_grid[eps_NROY].max()
    print(f"  epsilon: [{eps_min:.5f}, {eps_max:.5f}] (canonical: {epsilon_canonical:.5f})")
else:
    print(f"  epsilon: EMPTY NROY")
    eps_min = eps_max = np.nan

# N_cells
Nc_NROY = np.any(NROY_mask, axis=(0, 1, 2))
if np.any(Nc_NROY):
    Nc_allowed = N_cells_list[Nc_NROY]
    print(f"  N_cells: {Nc_allowed.tolist()} (canonical: {N_cells_canon})")
else:
    print(f"  N_cells: EMPTY NROY")
    Nc_allowed = np.array([])

# =============================================================================
# 9. Best-fit point and sensitivity
# =============================================================================
best_idx = np.unravel_index(np.argmin(I_max_all), I_max_all.shape)
best_EJ = EJ_grid[best_idx[0]]
best_EJEc = EJEc_grid[best_idx[1]]
best_eps = eps_grid[best_idx[2]]
best_Nc = N_cells_list[best_idx[3]]
best_Imax = I_max_all[best_idx]

print(f"\n=== Best-fit point ===")
print(f"  E_J = {best_EJ:.4f}")
print(f"  E_J/E_c = {best_EJEc:.4f}")
print(f"  epsilon = {best_eps:.5f}")
print(f"  N_cells = {best_Nc}")
print(f"  I_max = {best_Imax:.4f}")
print(f"  I_DM = {I_DM_all[best_idx]:.4f}")
print(f"  I_Lambda = {I_Lambda_all[best_idx]:.4f}")
print(f"  I_fDM = {I_fDM_all[best_idx]:.4f}")
print(f"  I_w = {I_w_all[best_idx]:.4f}")

# Predicted observables at best fit
o_dm_best, o_lam_best, o_fdm_best, o_w_best = predict_observables(
    best_EJ, best_EJEc, best_eps, best_Nc)
print(f"\n  Predicted observables at best fit:")
print(f"    Omega_DM h^2 = {o_dm_best:.4f} (obs: {Omega_DM_h2_obs:.4f})")
print(f"    Omega_Lambda = {o_lam_best:.4f} (obs: {Omega_Lambda_obs:.3f})")
print(f"    f_DM = {o_fdm_best:.4f} (obs: {f_DM_obs:.3f})")
print(f"    w = {o_w_best:.4f} (obs: {w_obs:.1f})")

# =============================================================================
# 10. Sensitivity analysis: which parameters matter most?
# =============================================================================
print(f"\n=== Sensitivity analysis ===")

# Compute partial derivatives at best-fit point
delta_EJ = 0.01  # (local)
delta_EJEc = 0.1  # (local)
delta_eps = 0.0001  # (local)
delta_Nc = 1  # discrete, use nearest

def sensitivity(param_name, x0, dx, param_idx):
    """Compute d(observable)/d(parameter) at best fit."""
    x_plus = list(x0)
    x_minus = list(x0)
    x_plus[param_idx] += dx
    x_minus[param_idx] -= dx

    o_plus = predict_observables(*x_plus)
    o_minus = predict_observables(*x_minus)

    sensitivities = [(o_plus[i] - o_minus[i]) / (2 * dx) for i in range(4)]
    obs_names = ['Omega_DM_h2', 'Omega_Lambda', 'f_DM', 'w']
    print(f"  d/d({param_name}):")
    for i, name in enumerate(obs_names):
        print(f"    d({name})/d({param_name}) = {sensitivities[i]:.4e}")
    return sensitivities

x0 = [best_EJ, best_EJEc, best_eps, float(best_Nc)]
s_EJ = sensitivity('E_J', x0, delta_EJ, 0)
s_EJEc = sensitivity('EJ/Ec', x0, delta_EJEc, 1)
s_eps = sensitivity('epsilon', x0, delta_eps, 2)

# Normalized sensitivity (elasticity)
print(f"\n  Normalized sensitivities (elasticity = d(ln O)/d(ln p)):")
obs_ref = [o_dm_best, o_lam_best, o_fdm_best, o_w_best]
obs_names = ['Omega_DM_h2', 'Omega_Lambda', 'f_DM', 'w']

for pname, svals, pval, dp in [('E_J', s_EJ, best_EJ, delta_EJ),
                                 ('EJ/Ec', s_EJEc, best_EJEc, delta_EJEc),
                                 ('epsilon', s_eps, best_eps, delta_eps)]:
    elasticities = []
    for i in range(4):
        if abs(obs_ref[i]) > 1e-10:
            elast = svals[i] * pval / obs_ref[i]
        else:
            elast = 0.0
        elasticities.append(elast)
    print(f"    {pname}: {[f'{e:.2f}' for e in elasticities]}")

# =============================================================================
# 11. 2D projections of NROY region
# =============================================================================
print(f"\n=== 2D NROY projections ===")

# Project onto (E_J, epsilon) plane, marginalized over E_J/E_c and N_cells
NROY_EJ_eps = np.any(NROY_mask, axis=(1, 3))  # marginalize over EJ/Ec and N_cells
n_NROY_EJ_eps = np.sum(NROY_EJ_eps)
print(f"  (E_J, epsilon) plane: {n_NROY_EJ_eps}/{n_EJ*n_eps} points in NROY ({n_NROY_EJ_eps/(n_EJ*n_eps)*100:.1f}%)")

# Project onto (E_J, N_cells) plane
NROY_EJ_Nc = np.any(NROY_mask, axis=(1, 2))  # marginalize over EJ/Ec and epsilon
n_NROY_EJ_Nc = np.sum(NROY_EJ_Nc)
print(f"  (E_J, N_cells) plane: {n_NROY_EJ_Nc}/{n_EJ*n_Ncells} points in NROY ({n_NROY_EJ_Nc/(n_EJ*n_Ncells)*100:.1f}%)")

# Project onto (epsilon, N_cells) plane
NROY_eps_Nc = np.any(NROY_mask, axis=(0, 1))  # marginalize over EJ and EJ/Ec
n_NROY_eps_Nc = np.sum(NROY_eps_Nc)
print(f"  (epsilon, N_cells) plane: {n_NROY_eps_Nc}/{n_eps*n_Ncells} points in NROY ({n_NROY_eps_Nc/(n_eps*n_Ncells)*100:.1f}%)")

# Project onto (E_J/E_c, N_cells) plane
NROY_EJEc_Nc = np.any(NROY_mask, axis=(0, 2))
n_NROY_EJEc_Nc = np.sum(NROY_EJEc_Nc)
print(f"  (E_J/E_c, N_cells) plane: {n_NROY_EJEc_Nc}/{n_EJEc*n_Ncells} points in NROY ({n_NROY_EJEc_Nc/(n_EJEc*n_Ncells)*100:.1f}%)")

# =============================================================================
# 12. Canonical point implausibility
# =============================================================================
print(f"\n=== Canonical point evaluation ===")
# Approximate canonical E_J/E_c from S57 data
# F_Josephson = -336.64 for N=32, E_J = 0.933
# E_c for Josephson array: E_c ~ E_J / (E_J/E_c)
# From Bose-Hubbard: E_J/E_c ~ F_J / N ~ 336.64 / 32 = 10.5
EJEc_canon_est = abs(F_Josephson) / N_cells_canon  # ~10.5

o_canon = predict_observables(E_J_canon, EJEc_canon_est, epsilon_canonical, N_cells_canon)
print(f"  E_J = {E_J_canon}, E_J/E_c ~ {EJEc_canon_est:.1f}, eps = {epsilon_canonical}, N = {N_cells_canon}")
print(f"  Omega_DM h^2 = {o_canon[0]:.4f}")
print(f"  Omega_Lambda = {o_canon[1]:.4f}")
print(f"  f_DM = {o_canon[2]:.4f}")
print(f"  w = {o_canon[3]:.4f}")

sigma_tot_DM = np.sqrt(sigma_Omega_DM_h2**2 + sigma_model_DM**2)
sigma_tot_Lambda = np.sqrt(sigma_Omega_Lambda**2 + sigma_model_Lambda**2)
sigma_tot_fDM = np.sqrt(sigma_f_DM**2 + sigma_model_fDM**2)
sigma_tot_w = np.sqrt(sigma_w**2 + sigma_model_w**2)

I_canon = [
    abs(o_canon[0] - Omega_DM_h2_obs) / sigma_tot_DM,
    abs(o_canon[1] - Omega_Lambda_obs) / sigma_tot_Lambda,
    abs(o_canon[2] - f_DM_obs) / sigma_tot_fDM,
    abs(o_canon[3] - w_obs) / sigma_tot_w
]
I_canon_max = max(I_canon)
canon_in_NROY = I_canon_max < NROY_threshold

print(f"  Implausibilities: DM={I_canon[0]:.2f}, Lambda={I_canon[1]:.2f}, fDM={I_canon[2]:.2f}, w={I_canon[3]:.2f}")
print(f"  I_max = {I_canon_max:.2f}")
print(f"  Canonical point in NROY: {canon_in_NROY}")

# =============================================================================
# 13. Gate verdict
# =============================================================================
print(f"\n{'='*60}")
print(f"GATE: BAYESIAN-FABRIC-57")
print(f"VERDICT: INFO")

gate_detail = (
    f"NROY volume fraction = {NROY_fraction:.4f} ({NROY_fraction*100:.2f}%). "
    f"Most constraining: {most_constraining}. "
    f"Best-fit I_max = {best_Imax:.3f} at E_J={best_EJ:.3f}, E_J/E_c={best_EJEc:.2f}, "
    f"epsilon={best_eps:.5f}, N_cells={best_Nc}. "
    f"Canonical point I_max = {I_canon_max:.2f} ({'in' if canon_in_NROY else 'outside'} NROY). "
    f"E_J range [{EJ_min:.3f},{EJ_max:.3f}], N_cells allowed: {Nc_allowed.tolist() if len(Nc_allowed) > 0 else 'NONE'}."
)

print(f"DETAIL: {gate_detail}")
print(f"{'='*60}")

# =============================================================================
# 14. Save
# =============================================================================
np.savez('computations/session-57/s57_bayesian_fabric.npz',
    # Parameter grids
    EJ_grid=EJ_grid,
    EJEc_grid=EJEc_grid,
    eps_grid=eps_grid,
    N_cells_list=N_cells_list,
    # Implausibility fields (4D)
    I_max=I_max_all,
    I_DM=I_DM_all,
    I_Lambda=I_Lambda_all,
    I_fDM=I_fDM_all,
    I_w=I_w_all,
    # Predicted observables at grid points
    O_DM_pred=O_DM_pred,
    O_Lambda_pred=O_Lambda_pred,
    O_fDM_pred=O_fDM_pred,
    O_w_pred=O_w_pred,
    # NROY
    NROY_mask=NROY_mask,
    NROY_fraction=np.array(NROY_fraction),
    NROY_threshold=np.array(NROY_threshold),
    # Marginal ranges
    EJ_NROY_range=np.array([EJ_min, EJ_max]),
    EJEc_NROY_range=np.array([EJEc_min, EJEc_max]),
    eps_NROY_range=np.array([eps_min, eps_max]),
    Nc_NROY=Nc_allowed if len(Nc_allowed) > 0 else np.array([]),
    # Per-observable NROY fractions
    NROY_per_obs=np.array([NROY_DM, NROY_Lambda, NROY_fDM, NROY_w]),
    NROY_obs_names=np.array(['Omega_DM_h2', 'Omega_Lambda', 'f_DM', 'w']),
    most_constraining=np.array([most_constraining]),
    # Best fit
    best_fit=np.array([best_EJ, best_EJEc, best_eps, float(best_Nc)]),
    best_Imax=np.array(best_Imax),
    best_observables=np.array([o_dm_best, o_lam_best, o_fdm_best, o_w_best]),
    # Canonical point
    canon_observables=np.array(o_canon),
    canon_implausibilities=np.array(I_canon),
    canon_Imax=np.array(I_canon_max),
    canon_in_NROY=np.array(canon_in_NROY),
    # 2D projections
    NROY_EJ_eps=NROY_EJ_eps,
    NROY_EJ_Nc=NROY_EJ_Nc,
    NROY_eps_Nc=NROY_eps_Nc,
    NROY_EJEc_Nc=NROY_EJEc_Nc,
    # Observational targets
    obs_targets=np.array([Omega_DM_h2_obs, Omega_Lambda_obs, f_DM_obs, w_obs]),
    obs_sigma=np.array([sigma_Omega_DM_h2, sigma_Omega_Lambda, sigma_f_DM, sigma_w]),
    model_sigma=np.array([sigma_model_DM, sigma_model_Lambda, sigma_model_fDM, sigma_model_w]),
    # Gate
    gate_name=np.array(['BAYESIAN-FABRIC-57']),
    gate_verdict=np.array(['INFO']),
    gate_detail=np.array([gate_detail]),
)

print("\nSaved: computations/session-57/s57_bayesian_fabric.npz")
print("DONE")
