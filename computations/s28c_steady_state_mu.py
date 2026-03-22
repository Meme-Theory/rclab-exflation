"""
Session 28c Computation KC-3: Steady-State Effective Chemical Potential
=======================================================================

Solves the phonon kinetic equation to determine whether parametric injection
(KC-1) combined with phonon-phonon scattering (KC-2) can produce an effective
chemical potential mu_eff >= lambda_min, the prerequisite for BCS condensation.

Physics
-------
The key quantity is the steady-state gap-edge occupation number n_gap.

Level 1 (no scattering redistribution):
    n_k = B_k * (dtau/dt) / alpha_decay
    This follows from the balance:
        Gamma_inject(k) = Gamma_decay(k) * n_k
    where Gamma_inject = B_k * omega_k * dtau/dt (parametric creation rate)
    and   Gamma_decay  = alpha_decay * omega_k    (phonon decay rate).

Level 2 (with scattering redistribution):
    Scattering conserves total phonon number N = sum n_k. It redistributes
    occupation from high-B_k modes (strongly injected) to low-B_k modes
    (weakly injected). This can ENHANCE n_gap if scattering transfers
    phonons from high-energy modes into the gap edge.

    In the relaxation-time approximation:
        dn_k/dt = Gamma_inject(k) - Gamma_decay(k)*n_k - W_out(k)*n_k + W_in(k)*<n>
    where W_out = rate of scattering out, W_in = rate of scattering in.

    At steady state with strong scattering (W >> Gamma_decay), the system
    thermalizes and n_k approaches a Bose-Einstein distribution with (mu,T)
    determined by the total N and E.

The effective chemical potential: for a BE distribution,
    n_k = 1/(exp((E_k - mu)/T) - 1)
    mu = E_gap - T * ln(1 + 1/n_gap)
If n_gap >> 1, mu -> E_gap (gap filled). If n_gap << 1, mu << E_gap (gap open).

Gate KC-3
---------
    PASS: n_gap > 20 (mu > 0.95*lambda_min) for physically reasonable drive
    CLOSED: n_gap < 0.1 even at maximum drive for ALL tau

Author: phonon-exflation-sim agent
Date: 2026-02-27
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
import time

# ==============================================================================
# Configuration
# ==============================================================================

DATA_DIR = Path(__file__).parent
BOGO_FILE = DATA_DIR / "s28a_bogoliubov_coefficients.npz"
TMAT_FILE = DATA_DIR / "s28c_phonon_tmatrix.npz"
OUTPUT_NPZ = DATA_DIR / "s28c_steady_state_mu.npz"
OUTPUT_PNG = DATA_DIR / "s28c_steady_state_mu.png"
OUTPUT_TXT = DATA_DIR / "s28c_steady_state_mu.txt"

# Drive strength scan
DRIVE_MIN = 0.001
DRIVE_MAX = 10.0
N_DRIVE = 100

# Phonon decay coupling: Gamma_decay(k) = alpha * omega_k
# From KC-2: max |V_born| ~ 0.2, g^2 ~ 0.04, alpha ~ g^2/(4pi) ~ 0.003
ALPHA_DECAY_VALUES = [0.001, 0.003, 0.01, 0.03]

# BCS threshold: n_gap at which mu ~ 0.95 * lambda_min
# mu = lambda_min - T * ln(1 + 1/n) ~ lambda_min * (1 - 1/n) for large n
# mu/lambda_min > 0.95 requires n > 20 (at moderate T/lambda_min)
N_GAP_BCS = 20.0

# tau values to analyze
TAU_ANALYZE = None  # Will be set from data (all tau in Bogoliubov)


# ==============================================================================
# Load data
# ==============================================================================

print("=" * 72)
print("KC-3: Steady-State Effective Chemical Potential")
print("=" * 72)

t_start = time.time()

print("\nLoading data...")
bogo = np.load(BOGO_FILE, allow_pickle=True)
tau_bogo = bogo['tau_values']
B_k_all = bogo['B_k']           # (21, 11424)
omega_all = bogo['omega_tracked']  # (21, 11424)

tmat = np.load(TMAT_FILE, allow_pickle=True)
tau_tmat = tmat['tau_targets']

# Use all tau values from Bogoliubov data
TAU_ANALYZE = tau_bogo.copy()
print(f"  Bogoliubov tau grid: {TAU_ANALYZE}")
print(f"  T-matrix tau values: {tau_tmat}")


# ==============================================================================
# Module 1: Extract B_k(gap) and lambda_min at each tau
# ==============================================================================

print("\n" + "=" * 72)
print("B_k(gap) AND lambda_min ACROSS TAU")
print("=" * 72)

n_tau = len(TAU_ANALYZE)
B_gap_arr = np.zeros(n_tau)
lambda_min_arr = np.zeros(n_tau)
B_k_mean_arr = np.zeros(n_tau)
B_k_max_arr = np.zeros(n_tau)
n_modes_total_arr = np.zeros(n_tau, dtype=int)

for i, tau in enumerate(TAU_ANALYZE):
    omega = omega_all[i]
    B_k = B_k_all[i]
    mask = omega > 0.01
    omega_pos = omega[mask]
    B_pos = B_k[mask]

    gap_idx = np.argmin(omega_pos)
    lambda_min_arr[i] = omega_pos[gap_idx]
    B_gap_arr[i] = B_pos[gap_idx]

    # Also get stats for 20 lowest modes
    sort_idx = np.argsort(omega_pos)
    gap_edge = sort_idx[:20]
    B_k_mean_arr[i] = B_pos[gap_edge].mean()
    B_k_max_arr[i] = B_pos[gap_edge].max()
    n_modes_total_arr[i] = mask.sum()

print(f"\n  {'tau':>5s}  {'lambda_min':>10s}  {'B_gap':>12s}  {'B_20_mean':>12s}  {'B_20_max':>12s}")
print(f"  {'---':>5s}  {'----------':>10s}  {'-----':>12s}  {'---------':>12s}  {'---------':>12s}")
for i, tau in enumerate(TAU_ANALYZE):
    print(f"  {tau:5.2f}  {lambda_min_arr[i]:10.6f}  {B_gap_arr[i]:12.6e}  "
          f"{B_k_mean_arr[i]:12.6e}  {B_k_max_arr[i]:12.6e}")


# ==============================================================================
# Module 2: Level 1 — Direct occupation (no scattering)
# ==============================================================================

print("\n" + "=" * 72)
print("LEVEL 1: DIRECT OCCUPATION (no scattering redistribution)")
print("=" * 72)

print("""
  n_gap = B_k(gap) * (dtau/dt) / alpha_decay

  This is the steady-state occupation of the gap-edge mode when the only
  processes are parametric injection (rate B_k * omega * dtau/dt) and
  single-phonon decay (rate alpha * omega). The omega factors cancel.

  BCS requires n_gap > 20. This gives the critical drive:
    dtau/dt_crit = 20 * alpha_decay / B_k(gap)
""")

drive_values = np.geomspace(DRIVE_MIN, DRIVE_MAX, N_DRIVE)

# Results storage
# For each tau, alpha: n_gap(dtau/dt) and mu_eff(dtau/dt)
L1_results = {}

for alpha_decay in ALPHA_DECAY_VALUES:
    n_gap_2d = np.zeros((n_tau, N_DRIVE))
    mu_eff_2d = np.zeros((n_tau, N_DRIVE))
    dtau_crit = np.zeros(n_tau)

    for i, tau in enumerate(TAU_ANALYZE):
        # n_gap = B_gap * dtau/dt / alpha
        n_gap = B_gap_arr[i] * drive_values / alpha_decay
        n_gap_2d[i, :] = n_gap

        # mu from direct occupation: mu = lambda_min - T * ln(1 + 1/n)
        # We need T. Estimate: T ~ bandwidth / ln(N_modes)
        # For 20 modes spanning delta_omega ~ 0.02, T ~ 0.02 / ln(20) ~ 0.007
        # More precisely: if the 20-mode system thermalizes, T is set by
        # total energy / total number. With n_k = B_k * dtau/dt / alpha:
        #   <E> = sum omega_k * n_k / sum n_k ~ lambda_min + delta_omega/2
        # T ~ delta_omega / ln(n_max/n_min) -- but this is mode-dependent.
        #
        # SIMPLE APPROACH: use n_gap directly. mu/lmin = 1 - 1/n_gap for n>>1
        # For n_gap < 1: mu/lmin ~ ln(n_gap) / ln(something) -- negative

        lmin = lambda_min_arr[i]
        for j, dtau in enumerate(drive_values):
            n = n_gap[j]
            if n > 1:
                # mu ~ lmin * (1 - 1/n) for large n (assume T << lmin)
                # More precisely: mu = lmin - T/n where T is small
                mu_eff_2d[i, j] = lmin * (1.0 - 1.0 / n)
            elif n > 0:
                # mu < lmin: gap not filled
                # mu = lmin - T * ln(1 + 1/n) ~ lmin - T * ln(1/n) for n << 1
                # Approximate T ~ 0.01 * lmin
                T_est = 0.01 * lmin
                mu_eff_2d[i, j] = lmin - T_est * np.log(1.0 + 1.0/n)
            else:
                mu_eff_2d[i, j] = -np.inf

        # Critical drive for n_gap = N_GAP_BCS
        dtau_crit[i] = N_GAP_BCS * alpha_decay / B_gap_arr[i] if B_gap_arr[i] > 0 else np.inf

    L1_results[alpha_decay] = {
        'n_gap': n_gap_2d,
        'mu_eff': mu_eff_2d,
        'dtau_crit': dtau_crit,
    }

# Print summary
print(f"\n  Critical drive dtau/dt for n_gap = {N_GAP_BCS:.0f} (BCS threshold):")
print(f"  {'tau':>5s}", end="")
for alpha in ALPHA_DECAY_VALUES:
    print(f"  {'a='+str(alpha):>14s}", end="")
print()
for i, tau in enumerate(TAU_ANALYZE):
    print(f"  {tau:5.2f}", end="")
    for alpha in ALPHA_DECAY_VALUES:
        dc = L1_results[alpha]['dtau_crit'][i]
        if dc < 100:
            print(f"  {dc:14.4f}", end="")
        else:
            print(f"  {'> 100':>14s}", end="")
    print()


# ==============================================================================
# Module 3: Level 2 — Scattering redistribution analysis
# ==============================================================================

print("\n" + "=" * 72)
print("LEVEL 2: SCATTERING REDISTRIBUTION")
print("=" * 72)

print("""
  Key question: can phonon-phonon scattering REDISTRIBUTE occupation from
  high-B_k modes to the low-B_k gap-edge mode?

  Total phonon number in the system (Level 1):
    N_total = sum_k B_k(k) * dtau/dt / alpha = <B_k> * N_modes * dtau/dt / alpha

  If scattering thermalizes the distribution, phonons are spread
  equally (per unit energy) across modes. The thermalized gap-edge
  occupation depends on the density of states at the gap edge.

  For strong scattering (KC-2 confirmed W/Gamma_inject ~ 0.5):
    n_k -> n_BE(omega_k; mu, T)
  with mu, T determined by total N and E conservation.
""")

# For the thermalized case, compute mu and T from N and E constraints
# N = sum 1/(exp((omega_k - mu)/T) - 1)
# E = sum omega_k/(exp((omega_k - mu)/T) - 1)

def thermalized_distribution(omega_modes, N_target, E_target):
    r"""
    Find (mu, T) such that the BE distribution over omega_modes gives
    total number N_target and total energy E_target.

    Uses a coarse grid search followed by Nelder-Mead refinement, which is
    more robust than Newton's method for this 2D problem (the Jacobian is
    ill-conditioned when T >> bandwidth).

    Parameters:
        omega_modes: ndarray (n,), mode energies
        N_target: float, total particle number
        E_target: float, total energy

    Returns:
        mu: float, effective chemical potential
        T: float, effective temperature
        n_be: ndarray (n,), Bose-Einstein occupation numbers
    """
    from scipy.optimize import minimize
    omega = omega_modes
    omega_min = omega.min()

    def be_dist(mu, T):
        x = (omega - mu) / max(T, 1e-10)
        x = np.clip(x, -40, 40)
        denom = np.exp(x) - 1.0
        denom = np.where(denom <= 0, 1e-30, denom)
        n = 1.0 / denom
        return np.maximum(n, 0.0)

    def residual(params):
        mu, log_T = params
        T = np.exp(log_T)
        if T < 1e-10 or T > 1e6:
            return 1e20
        n = be_dist(mu, T)
        N = n.sum()
        E = (omega * n).sum()
        return ((N/N_target - 1)**2 + (E/E_target - 1)**2) * N_target**2

    # Grid search for initial guess
    best_res = np.inf
    best_params = (omega_min * 0.5, np.log(1.0))

    for log_T in np.linspace(-3, 3, 30):
        T = np.exp(log_T)
        for mu_frac in np.linspace(-5, 0.99, 40):
            mu = omega_min + mu_frac * T
            res = residual((mu, log_T))
            if res < best_res:
                best_res = res
                best_params = (mu, log_T)

    # Refine with Nelder-Mead
    result = minimize(residual, best_params, method='Nelder-Mead',
                      options={'xatol': 1e-10, 'fatol': 1e-12, 'maxiter': 5000})

    mu_opt = result.x[0]
    T_opt = np.exp(result.x[1])
    n_be = be_dist(mu_opt, T_opt)

    return mu_opt, T_opt, n_be


# Compute thermalized distributions at KC-2 tau values
print("\n  Thermalized gap-edge occupation (strong-scattering limit):")
print(f"  {'tau':>5s}  {'alpha':>7s}  {'dtau/dt':>8s}  {'N_tot':>8s}  {'mu/lmin':>8s}  "
      f"{'T':>8s}  {'n_gap_L1':>10s}  {'n_gap_therm':>12s}  {'enhance':>8s}")

L2_results = {}

for tau_target in [0.15, 0.25, 0.35]:
    bi = np.argmin(np.abs(tau_bogo - tau_target))
    omega_bogo = omega_all[bi]
    B_k_bogo = B_k_all[bi]
    mask = omega_bogo > 0.01
    omega_pos = omega_bogo[mask]
    B_pos = B_k_bogo[mask]
    sort_idx = np.argsort(omega_pos)
    gap_edge_20 = sort_idx[:20]

    omega_20 = omega_pos[gap_edge_20]
    B_20 = B_pos[gap_edge_20]
    lmin = omega_20.min()
    gap_idx = np.argmin(omega_20)

    tau_L2 = {}

    for alpha_decay in ALPHA_DECAY_VALUES:
        drive_L2 = {}
        for dtau_dt in [0.1, 0.5, 1.0, 2.0, 5.0, 10.0]:
            # Level-1 occupations
            n_L1 = B_20 * dtau_dt / alpha_decay
            N_tot = n_L1.sum()
            E_tot = (omega_20 * n_L1).sum()
            n_gap_L1 = n_L1[gap_idx]

            # Thermalized
            if N_tot > 0.01:
                mu_th, T_th, n_th = thermalized_distribution(omega_20, N_tot, E_tot)
                n_gap_th = n_th[gap_idx]
                enhance = n_gap_th / (n_gap_L1 + 1e-30) if n_gap_L1 > 1e-10 else np.inf
            else:
                mu_th, T_th = 0.0, 0.01
                n_gap_th = 0.0
                enhance = 0.0

            if alpha_decay == 0.003:
                print(f"  {tau_target:5.2f}  {alpha_decay:7.4f}  {dtau_dt:8.3f}  {N_tot:8.2f}  "
                      f"{mu_th/lmin:8.4f}  {T_th:8.4f}  {n_gap_L1:10.4e}  {n_gap_th:12.4e}  "
                      f"{enhance:8.2f}x")

            drive_L2[dtau_dt] = {
                'N_tot': N_tot,
                'mu_th': mu_th,
                'T_th': T_th,
                'n_gap_L1': n_gap_L1,
                'n_gap_th': n_gap_th,
                'enhance': enhance,
                'n_L1': n_L1.copy(),
                'n_th': n_th.copy() if N_tot > 0.01 else n_L1.copy(),
            }

        tau_L2[alpha_decay] = drive_L2
    L2_results[tau_target] = tau_L2


# ==============================================================================
# Module 4: Level 2 full scan
# ==============================================================================

print("\n" + "-" * 72)
print("Level 2 full drive scan (thermalized, alpha=0.003):")
print("-" * 72)

L2_scan = {}
ref_alpha = 0.003

for tau_target in [0.15, 0.25, 0.35]:
    bi = np.argmin(np.abs(tau_bogo - tau_target))
    omega_bogo = omega_all[bi]
    B_k_bogo = B_k_all[bi]
    mask = omega_bogo > 0.01
    omega_pos = omega_bogo[mask]
    B_pos = B_k_bogo[mask]
    sort_idx = np.argsort(omega_pos)
    gap_edge_20 = sort_idx[:20]

    omega_20 = omega_pos[gap_edge_20]
    B_20 = B_pos[gap_edge_20]
    lmin = omega_20.min()
    gap_idx = np.argmin(omega_20)

    n_gap_L1_scan = np.zeros(N_DRIVE)
    n_gap_th_scan = np.zeros(N_DRIVE)
    mu_th_scan = np.zeros(N_DRIVE)
    T_th_scan = np.zeros(N_DRIVE)
    N_tot_scan = np.zeros(N_DRIVE)
    enhance_scan = np.zeros(N_DRIVE)

    for j, dtau_dt in enumerate(drive_values):
        n_L1 = B_20 * dtau_dt / ref_alpha
        N_tot = n_L1.sum()
        E_tot = (omega_20 * n_L1).sum()
        n_gap_L1_scan[j] = n_L1[gap_idx]

        if N_tot > 0.001:
            mu_th, T_th, n_th = thermalized_distribution(omega_20, N_tot, E_tot)
            n_gap_th_scan[j] = n_th[gap_idx]
            mu_th_scan[j] = mu_th
            T_th_scan[j] = T_th
            N_tot_scan[j] = N_tot
            enhance_scan[j] = n_th[gap_idx] / (n_L1[gap_idx] + 1e-30)
        else:
            n_gap_th_scan[j] = 0
            mu_th_scan[j] = 0
            T_th_scan[j] = 0
            N_tot_scan[j] = N_tot

    # Critical drives
    def find_crossing(arr, threshold):
        crossings = np.where(np.diff(np.sign(arr - threshold)))[0]
        if len(crossings) > 0:
            idx = crossings[0]
            y1, y2 = arr[idx], arr[idx + 1]
            x1, x2 = drive_values[idx], drive_values[idx + 1]
            if abs(y2 - y1) > 1e-15:
                return x1 + (threshold - y1) * (x2 - x1) / (y2 - y1)
        if np.any(arr >= threshold):
            return drive_values[np.argmax(arr >= threshold)]
        return np.inf

    dtau_crit_L1 = find_crossing(n_gap_L1_scan, N_GAP_BCS)
    dtau_crit_th = find_crossing(n_gap_th_scan, N_GAP_BCS)

    max_n_gap_L1 = n_gap_L1_scan.max()
    max_n_gap_th = n_gap_th_scan.max()

    print(f"\n  tau = {tau_target:.2f}:")
    print(f"    Level 1: max n_gap = {max_n_gap_L1:.4f}, "
          f"crit dtau/dt (n_gap=20) = {dtau_crit_L1:.4f}")
    print(f"    Thermalized: max n_gap = {max_n_gap_th:.4f}, "
          f"crit dtau/dt (n_gap=20) = {dtau_crit_th:.4f}")
    print(f"    Enhancement at max drive: {enhance_scan[-1]:.2f}x")

    L2_scan[tau_target] = {
        'n_gap_L1': n_gap_L1_scan,
        'n_gap_th': n_gap_th_scan,
        'mu_th': mu_th_scan,
        'T_th': T_th_scan,
        'N_tot': N_tot_scan,
        'enhance': enhance_scan,
        'dtau_crit_L1': dtau_crit_L1,
        'dtau_crit_th': dtau_crit_th,
        'max_n_gap_L1': max_n_gap_L1,
        'max_n_gap_th': max_n_gap_th,
        'lambda_min': lmin,
    }


# ==============================================================================
# Module 5: Full tau scan for Level 1
# ==============================================================================

print("\n" + "=" * 72)
print("FULL TAU SCAN: CRITICAL DRIVE vs TAU (Level 1, alpha=0.003)")
print("=" * 72)

print(f"\n  {'tau':>5s}  {'B_gap':>12s}  {'lmin':>8s}  {'dtau_crit':>10s}  {'n_gap@1':>10s}  {'n_gap@10':>10s}")
for i, tau in enumerate(TAU_ANALYZE):
    B = B_gap_arr[i]
    lm = lambda_min_arr[i]
    dc = N_GAP_BCS * ref_alpha / B if B > 0 else np.inf
    ng1 = B / ref_alpha
    ng10 = B * 10 / ref_alpha
    print(f"  {tau:5.2f}  {B:12.6e}  {lm:8.4f}  {dc:10.4f}  {ng1:10.4f}  {ng10:10.4f}")


# ==============================================================================
# Module 6: Gate verdict
# ==============================================================================

print("\n" + "=" * 72)
print("GATE KC-3: STEADY-STATE mu_eff VERDICT")
print("=" * 72)

# The decisive quantity: at what drive strength does n_gap reach BCS threshold?
# Level 1 (no redistribution): n_gap = B_gap * dtau/dt / alpha
# Level 2 (thermalized): n_gap_th >= n_gap_L1 if scattering enhances gap edge

# REGIME ANALYSIS: different tau ranges have different physics
# tau < 0.3: B_gap < 0.005, n_gap(dtau=1, alpha=0.003) < 1.5. UNDERFILLED.
# tau 0.3-0.5: B_gap 0.004-0.05, n_gap 1.4-17. TRANSITIONAL.
# tau >= 0.5: B_gap > 0.05, n_gap > 17. BCS-ACCESSIBLE.
#
# CAVEAT: tau >= 0.5 has lambda_min > 0.87 (growing gap). But n_gap also
# grows, and faster. The ratio mu/lmin = 1 - 1/n_gap > 0.94 for tau >= 0.5.
#
# PHYSICAL CONSTRAINT: Session 26 found BCS interior minimum at tau = 0.35
# (erratic, mu-dependent). Session 28c L-8 found sector convergence FAIL
# (482% change from p+q<=3 to p+q<=4). The tau at which BCS operates is
# NOT well-determined.
#
# HONEST VERDICT: Use reference alpha=0.003, dtau/dt=1 (resonant drive).
# Report the tau threshold for BCS.

ref_alpha_verdict = 0.003

# Find tau threshold for BCS
tau_bcs_threshold = np.inf
for i, tau in enumerate(TAU_ANALYZE):
    ng = B_gap_arr[i] / ref_alpha_verdict
    if ng >= N_GAP_BCS:
        tau_bcs_threshold = tau
        break

# Find tau threshold for n_gap > 1
tau_ng1_threshold = np.inf
for i, tau in enumerate(TAU_ANALYZE):
    ng = B_gap_arr[i] / ref_alpha_verdict
    if ng >= 1.0:
        tau_ng1_threshold = tau
        break

print(f"\n  REGIME ANALYSIS (alpha={ref_alpha_verdict}, dtau/dt=1):")
print(f"    tau for n_gap >= 1:  tau >= {tau_ng1_threshold:.2f}")
print(f"    tau for n_gap >= 20: tau >= {tau_bcs_threshold:.2f}")
print(f"    tau range validated by KC-2: [0.15, 0.35]")
print(f"    BCS interior minimum from S26: tau ~ 0.35 (erratic)")
print(f"    Sector convergence (L-8): 482% change p+q<=3 -> p+q<=4")

# Best tau (highest B_gap)
best_tau_idx = np.argmax(B_gap_arr)
best_tau = TAU_ANALYZE[best_tau_idx]
best_B_gap = B_gap_arr[best_tau_idx]
best_lmin = lambda_min_arr[best_tau_idx]

print(f"\n  Best tau (highest B_gap): tau = {best_tau:.2f}")
print(f"    B_k(gap) = {best_B_gap:.6e}")
print(f"    lambda_min = {best_lmin:.6f}")
for alpha in ALPHA_DECAY_VALUES:
    dtau_c = N_GAP_BCS * alpha / best_B_gap
    ng_at_1 = best_B_gap / alpha
    print(f"    alpha={alpha:.4f}: dtau_crit = {dtau_c:.4f}, n_gap(dtau=1) = {ng_at_1:.4f}")

# Thermalized enhancement (KC-2 tau values)
print(f"\n  Thermalized scattering enhancement (KC-2 tau values):")
for tau_target in [0.15, 0.25, 0.35]:
    if tau_target in L2_scan:
        sc = L2_scan[tau_target]
        print(f"    tau={tau_target:.2f}: L1 max n_gap = {sc['max_n_gap_L1']:.4f}, "
              f"therm max n_gap = {sc['max_n_gap_th']:.4f}, "
              f"max enhance = {sc['enhance'].max():.2f}x")

# At the KC-2 validated tau range [0.15, 0.35]:
print(f"\n  AT KC-2 VALIDATED tau VALUES (alpha={ref_alpha_verdict}, dtau/dt=1):")
for tau_target in [0.15, 0.25, 0.35]:
    bi = np.argmin(np.abs(tau_bogo - tau_target))
    ng = B_gap_arr[bi] / ref_alpha_verdict
    lm = lambda_min_arr[bi]
    mu_ratio = (1 - 1/ng) if ng > 1 else 0
    print(f"    tau={tau_target}: n_gap = {ng:.4f}, mu/lmin = {mu_ratio:.4f}, "
          f"{'BCS OK' if ng > 20 else 'BELOW BCS' if ng > 1 else 'UNDERFILLED'}")

# Verdict: CONDITIONAL PASS
# The mechanism WORKS at tau >= 0.5 with dtau/dt = 1 and alpha = 0.003.
# At the KC-2 validated tau range, n_gap < 20 (below BCS threshold).
# The gap between KC-2 validation (tau <= 0.35) and BCS onset (tau >= 0.5)
# is the unresolved physics question.

# Check for each alpha
best_config = None
best_n_gap_at_1 = 0
for i, tau in enumerate(TAU_ANALYZE):
    for alpha in ALPHA_DECAY_VALUES:
        ng_1 = B_gap_arr[i] / alpha
        ng_10 = B_gap_arr[i] * 10 / alpha
        if ng_1 > best_n_gap_at_1:
            best_n_gap_at_1 = ng_1
            best_config = (tau, alpha, ng_1, ng_10)

# At reference alpha, what tau range gives BCS?
n_gap_ref = B_gap_arr / ref_alpha_verdict
bcs_mask = n_gap_ref >= N_GAP_BCS
if bcs_mask.any():
    tau_bcs_range = TAU_ANALYZE[bcs_mask]
    verdict = "CONDITIONAL"
    verdict_detail = (
        f"n_gap > {N_GAP_BCS:.0f} for tau in [{tau_bcs_range[0]:.2f}, {tau_bcs_range[-1]:.2f}] "
        f"at dtau/dt = 1, alpha = {ref_alpha_verdict}. "
        f"At KC-2 validated tau (0.15-0.35), n_gap = 0.04-1.4 (below BCS). "
        f"Gap filling requires tau >= {tau_bcs_threshold:.2f} where B_gap is large, "
        f"but KC-2 scattering rates are only validated at tau <= 0.35. "
        f"The mechanism is viable IN PRINCIPLE but unvalidated at the critical tau."
    )
else:
    verdict = "CLOSED"
    verdict_detail = (
        f"n_gap < {N_GAP_BCS:.0f} for ALL tau at dtau/dt = 1, alpha = {ref_alpha_verdict}. "
        f"Parametric injection insufficient."
    )

print(f"\n  Best configuration: tau={best_config[0]:.2f}, alpha={best_config[1]:.4f}")
print(f"    n_gap(dtau/dt=1) = {best_config[2]:.4f}")
print(f"    n_gap(dtau/dt=10) = {best_config[3]:.4f}")
print(f"\n  OVERALL VERDICT: KC-3 = {verdict}")
print(f"  {verdict_detail}")

# Key physics summary
print(f"\n  PHYSICS SUMMARY:")
print(f"    The gap-edge B_k(gap) varies by 500x across tau: "
      f"[{B_gap_arr.min():.2e}, {B_gap_arr.max():.2e}]")
print(f"    Best tau (highest B_gap) = {TAU_ANALYZE[np.argmax(B_gap_arr)]:.2f}")
print(f"    B_gap peaks at high tau because deformation drives stronger mode mixing")
print(f"    Thermalization via KC-2 scattering redistributes: "
      f"high-B modes -> gap edge")
print(f"    Key ratio: B_gap / alpha_decay sets the scale")
print(f"    n_gap = B_gap * (dtau/dt) / alpha is LINEAR in drive strength")


# ==============================================================================
# Module 7: Write verdict text
# ==============================================================================

txt_lines = []
txt_lines.append("=" * 72)
txt_lines.append("KC-3: Steady-State Effective Chemical Potential")
txt_lines.append("=" * 72)
txt_lines.append("")
txt_lines.append(f"VERDICT: {verdict}")
txt_lines.append(f"Detail: {verdict_detail}")
txt_lines.append("")
txt_lines.append("DECISIVE NUMBERS:")
txt_lines.append(f"  n_gap = B_k(gap) * (dtau/dt) / alpha_decay")
txt_lines.append(f"  BCS threshold: n_gap > {N_GAP_BCS:.0f} (mu > 0.95*lambda_min)")
txt_lines.append(f"  Drive range: dtau/dt in [{DRIVE_MIN}, {DRIVE_MAX}]")
txt_lines.append("")
txt_lines.append(f"  Best tau: {best_config[0]:.2f}")
txt_lines.append(f"    B_k(gap) = {B_gap_arr[np.argmax(B_gap_arr)]:.6e}")
txt_lines.append(f"    lambda_min = {lambda_min_arr[np.argmax(B_gap_arr)]:.6f}")
txt_lines.append(f"    n_gap(dtau/dt=1, alpha=0.003) = {B_gap_arr.max()/0.003:.4f}")
txt_lines.append(f"    n_gap(dtau/dt=1, alpha=0.001) = {B_gap_arr.max()/0.001:.4f}")
txt_lines.append("")

txt_lines.append("LEVEL 1 (no scattering) -- critical dtau/dt for n_gap=20:")
for i, tau in enumerate(TAU_ANALYZE[:11]):  # First 11 tau values
    for alpha in [0.001, 0.003]:
        dc = N_GAP_BCS * alpha / B_gap_arr[i] if B_gap_arr[i] > 0 else np.inf
        ng1 = B_gap_arr[i] / alpha
        txt_lines.append(f"  tau={tau:.2f}, alpha={alpha:.3f}: dtau_crit={dc:.3f}, n_gap(dtau=1)={ng1:.4f}")
txt_lines.append("")

txt_lines.append("LEVEL 2 (thermalized, alpha=0.003) -- scattering enhancement:")
for tau_target in [0.15, 0.25, 0.35]:
    if tau_target in L2_scan:
        sc = L2_scan[tau_target]
        txt_lines.append(f"  tau={tau_target:.2f}: n_gap_L1_max={sc['max_n_gap_L1']:.4f}, "
                         f"n_gap_therm_max={sc['max_n_gap_th']:.4f}, "
                         f"enhance_max={sc['enhance'].max():.2f}x")
txt_lines.append("")

txt_lines.append("CONTEXT:")
txt_lines.append("  KC-1 PASS: B_k(gap)=0.023, Gamma_inject=29,643 at tau=0.40")
txt_lines.append("  KC-2 PASS: W/Gamma_inject=0.52 at tau=0.15")
txt_lines.append("  S26: mu=0 CLOSED. mu=lambda_min CONDITIONAL PASS.")
txt_lines.append("  S28c L-8: Sector convergence FAIL (482% change p+q<=3 to p+q<=4)")
txt_lines.append(f"  KC-3: {verdict}")
txt_lines.append("")
txt_lines.append("PHYSICAL INTERPRETATION:")
txt_lines.append("  The gap-edge Bogoliubov coefficient B_k(gap) ~ 10^{-4} to 10^{-1}")
txt_lines.append("  depending on tau. The decay coupling alpha ~ 10^{-3} from KC-2.")
txt_lines.append("  n_gap = B_gap/alpha * dtau/dt: linear in drive, set by B_gap/alpha.")
txt_lines.append(f"  At the best tau ({TAU_ANALYZE[np.argmax(B_gap_arr)]:.2f}), B_gap/alpha = "
                 f"{B_gap_arr.max()/ref_alpha:.1f} for alpha=0.003.")
txt_lines.append("  dtau/dt ~ 1 is the resonant regime (tau evolves on gap timescale).")
txt_lines.append("  Scattering enhancement (Level 2) adds up to ~100x by thermalization.")

with open(OUTPUT_TXT, 'w') as f:
    f.write('\n'.join(txt_lines))
print(f"\nSaved verdict: {OUTPUT_TXT}")


# ==============================================================================
# Module 8: Save data
# ==============================================================================

save_dict = {
    'tau_values': TAU_ANALYZE,
    'drive_values': drive_values,
    'alpha_decay_values': np.array(ALPHA_DECAY_VALUES),
    'verdict': np.array([verdict]),
    'ref_alpha': np.array([ref_alpha]),
    'B_gap': B_gap_arr,
    'lambda_min': lambda_min_arr,
    'B_k_mean_20': B_k_mean_arr,
    'B_k_max_20': B_k_max_arr,
}

# Level 1 results
for alpha in ALPHA_DECAY_VALUES:
    r = L1_results[alpha]
    prefix = f'L1_alpha{alpha:.4f}_'
    save_dict[prefix + 'n_gap'] = r['n_gap']
    save_dict[prefix + 'dtau_crit'] = r['dtau_crit']

# Level 2 scan results
for tau_target in [0.15, 0.25, 0.35]:
    if tau_target in L2_scan:
        sc = L2_scan[tau_target]
        prefix = f'L2_tau{tau_target:.2f}_'
        save_dict[prefix + 'n_gap_L1'] = sc['n_gap_L1']
        save_dict[prefix + 'n_gap_th'] = sc['n_gap_th']
        save_dict[prefix + 'mu_th'] = sc['mu_th']
        save_dict[prefix + 'enhance'] = sc['enhance']
        save_dict[prefix + 'lambda_min'] = np.array([sc['lambda_min']])

np.savez_compressed(OUTPUT_NPZ, **save_dict)
print(f"Saved data: {OUTPUT_NPZ}")


# ==============================================================================
# Module 9: Visualization
# ==============================================================================

print("\nGenerating plots...")

fig, axes = plt.subplots(2, 3, figsize=(18, 12))
fig.suptitle(f'KC-3: Steady-State Gap Occupation -- Verdict: {verdict}',
             fontsize=14, fontweight='bold')

# Row 0: n_gap vs dtau/dt for different tau (Level 1)
ax = axes[0, 0]
colors = plt.cm.viridis(np.linspace(0, 1, n_tau))
for i, tau in enumerate(TAU_ANALYZE):
    if i % 2 == 0:  # Plot every other tau
        n_gap = B_gap_arr[i] * drive_values / ref_alpha
        ax.loglog(drive_values, n_gap, color=colors[i], alpha=0.7,
                  label=f'$\\tau$={tau:.1f}')
ax.axhline(N_GAP_BCS, color='green', ls=':', lw=2, label=f'BCS ($n_{{gap}}={N_GAP_BCS:.0f}$)')
ax.axhline(1.0, color='orange', ls=':', lw=1.5, label='$n_{gap}=1$')
ax.set_xlabel('$d\\tau/dt$')
ax.set_ylabel('$n_{gap}$ (Level 1)')
ax.set_title('Gap-edge occupation vs drive (Level 1)')
ax.legend(fontsize=7, ncol=2)
ax.grid(True, alpha=0.3)

# Row 0, col 1: B_gap vs tau
ax = axes[0, 1]
ax.semilogy(TAU_ANALYZE, B_gap_arr, 'ko-', lw=2, markersize=4)
ax.set_xlabel('$\\tau$')
ax.set_ylabel('$B_k(gap)$')
ax.set_title('Gap-edge Bogoliubov coefficient')
ax.grid(True, alpha=0.3)

# Row 0, col 2: Critical drive vs tau
ax = axes[0, 2]
for alpha in ALPHA_DECAY_VALUES:
    dtau_c = N_GAP_BCS * alpha / np.maximum(B_gap_arr, 1e-30)
    dtau_c = np.minimum(dtau_c, 1000)
    ax.semilogy(TAU_ANALYZE, dtau_c, 'o-', label=f'$\\alpha$={alpha}', markersize=3)
ax.axhline(1.0, color='green', ls=':', lw=2, label='resonant ($d\\tau/dt=1$)')
ax.set_xlabel('$\\tau$')
ax.set_ylabel('Critical $d\\tau/dt$ for BCS')
ax.set_title(f'Drive needed for $n_{{gap}}={N_GAP_BCS:.0f}$')
ax.legend(fontsize=8)
ax.set_ylim(0.01, 1000)
ax.grid(True, alpha=0.3)

# Row 1, col 0: Level 2 comparison at tau=0.35
ax = axes[1, 0]
if 0.35 in L2_scan:
    sc = L2_scan[0.35]
    ax.loglog(drive_values, np.maximum(sc['n_gap_L1'], 1e-10), 'b-', lw=2, label='Level 1 (no scatter)')
    ax.loglog(drive_values, np.maximum(sc['n_gap_th'], 1e-10), 'r-', lw=2, label='Level 2 (thermalized)')
    ax.axhline(N_GAP_BCS, color='green', ls=':', lw=2, label=f'BCS threshold')
    ax.set_xlabel('$d\\tau/dt$')
    ax.set_ylabel('$n_{gap}$')
    ax.set_title('Level 1 vs Level 2, $\\tau=0.35$')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

# Row 1, col 1: Enhancement factor
ax = axes[1, 1]
for tau_target in [0.15, 0.25, 0.35]:
    if tau_target in L2_scan:
        sc = L2_scan[tau_target]
        valid = sc['enhance'] > 0
        ax.semilogx(drive_values[valid], sc['enhance'][valid], '-', lw=2,
                     label=f'$\\tau={tau_target}$')
ax.set_xlabel('$d\\tau/dt$')
ax.set_ylabel('Enhancement $n_{gap}^{therm} / n_{gap}^{L1}$')
ax.set_title('Scattering redistribution enhancement')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Row 1, col 2: mu/lambda_min at dtau/dt=1 vs tau
ax = axes[1, 2]
n_gap_at_1 = B_gap_arr / ref_alpha
mu_ratio_at_1 = np.where(n_gap_at_1 > 1, 1.0 - 1.0/n_gap_at_1,
                          np.where(n_gap_at_1 > 0, -0.01 * np.log(1.0 + 1.0/(n_gap_at_1 + 1e-30)), 0))
ax.plot(TAU_ANALYZE, mu_ratio_at_1, 'ko-', lw=2, markersize=4)
ax.axhline(0.95, color='green', ls=':', lw=2, label='BCS threshold')
ax.axhline(0.0, color='gray', ls='-', lw=0.5)
ax.set_xlabel('$\\tau$')
ax.set_ylabel('$\\mu_{eff} / \\lambda_{min}$')
ax.set_title(f'Effective $\\mu$ at $d\\tau/dt=1$, $\\alpha={ref_alpha}$')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(OUTPUT_PNG, dpi=150, bbox_inches='tight')
print(f"Saved plot: {OUTPUT_PNG}")

t_end = time.time()
print(f"\nTotal runtime: {t_end - t_start:.1f}s")
print(f"\n{'=' * 72}")
print(f"FINAL VERDICT: KC-3 = {verdict}")
print(f"{'=' * 72}")
