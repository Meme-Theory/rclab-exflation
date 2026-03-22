"""
COHERENT-WALL-44: Multi-Wall Bragg Transfer Matrix
===================================================
Computes coherent propagation of KK quasiparticles through 32 Kibble-Zurek
domain walls. Each wall is an impedance mismatch in the BdG spectrum;
the periodic/disordered stack produces Bragg gaps and Anderson localization.

Physics:
  - BdG quasiparticles with branch-dependent mass M*_branch and gap Delta_branch
  - Domain wall = impedance step: Z = M* * v_group, where v_group = k / E(k)
  - Transfer matrix formalism: M_interface * M_propagation per cell
  - 32 domains from KZ statistics: L ~ Exp(xi_KZ), xi_KZ = 0.152 M_KK^{-1}
  - Numerically stable: rescale transfer matrices after each wall to prevent overflow

Gate: COHERENT-WALL-44
  PASS if DR > 3 decades for disordered 32-wall
  FAIL if DR < 2 for all configs
  INFO if periodic > 3 but disordered < 3

Author: quantum-acoustics-theorist
Session: S44, Wave 3-2
"""

import numpy as np
from scipy import linalg
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import time

t_start = time.time()

# ============================================================
# 1. LOAD DATA
# ============================================================

imp_data = np.load('tier0-computation/s43_impedance_mismatch.npz', allow_pickle=True)
fab_data = np.load('tier0-computation/s42_fabric_dispersion.npz', allow_pickle=True)
hf_data  = np.load('tier0-computation/s42_hauser_feshbach.npz', allow_pickle=True)

# BdG masses at fold (M_KK units)
M_B2 = float(fab_data['M_star_B2'].flat[0])   # 2.228
M_B1 = float(fab_data['M_star_B1'].flat[0])   # 1.138
M_B3 = float(fab_data['M_star_B3'].flat[0])   # 0.990

# BCS gaps at fold
Delta_B2 = float(imp_data['Delta_fold'][:4].mean())  # ~2.062 (B2 quartet)
Delta_B1 = float(imp_data['Delta_fold'][4])           # ~0.789
Delta_B3 = float(imp_data['Delta_fold'][5:].mean())   # ~0.176

# Single-particle energies at fold
eps_B2 = float(imp_data['eps_fold'][:4].mean())  # ~0.845
eps_B1 = float(imp_data['eps_fold'][4])           # ~0.820
eps_B3 = float(imp_data['eps_fold'][5:].mean())   # ~0.974

# Impedance parameters from S43
alpha_B2 = float(imp_data['alpha_B2'].flat[0])  # |M* dM*/dtau| for B2: 0.571
alpha_B1 = float(imp_data['alpha_B1'].flat[0])  # 1.754
alpha_B3 = float(imp_data['alpha_B3'].flat[0])  # 0.526

# Mass derivatives (for impedance variation across wall)
dM_B2 = float(imp_data['dM_B2'].flat[0])  # 1.272
dM_B1 = float(imp_data['dM_B1'].flat[0])  # -1.997
dM_B3 = float(imp_data['dM_B3'].flat[0])  # 0.520

# KZ domain parameters
xi_KZ = 0.152  # M_KK^{-1}, from S43 / S41
N_domains = 32  # from 32-cell tessellation
tau_fold = float(imp_data['tau_fold'].flat[0])

# Mass modulus
m_tau = float(fab_data['m_tau'].flat[0])  # 2.062 M_KK

# Hard spectral gap
gap_edge = float(hf_data['m_lightest'])  # 0.8191 M_KK

# Wall width
d_wall = float(imp_data['d_wall_natural'].flat[0])  # 0.485 M_KK^{-1}

# Representative tau step across one KZ domain wall
delta_tau_wall = 0.01

print("=" * 70)
print("COHERENT-WALL-44: Multi-Wall Bragg Transfer Matrix")
print("=" * 70)
print(f"\nInput parameters:")
print(f"  M*_B2 = {M_B2:.4f},  M*_B1 = {M_B1:.4f},  M*_B3 = {M_B3:.4f}")
print(f"  Delta_B2 = {Delta_B2:.4f},  Delta_B1 = {Delta_B1:.4f},  Delta_B3 = {Delta_B3:.4f}")
print(f"  eps_B2 = {eps_B2:.4f},  eps_B1 = {eps_B1:.4f},  eps_B3 = {eps_B3:.4f}")
print(f"  alpha_B2 = {alpha_B2:.4f},  alpha_B1 = {alpha_B1:.4f},  alpha_B3 = {alpha_B3:.4f}")
print(f"  dM_B2 = {dM_B2:.4f},  dM_B1 = {dM_B1:.4f},  dM_B3 = {dM_B3:.4f}")
print(f"  xi_KZ = {xi_KZ:.3f} M_KK^{{-1}}")
print(f"  N_domains = {N_domains}")
print(f"  gap_edge = {gap_edge:.4f} M_KK")
print(f"  d_wall = {d_wall:.4f} M_KK^{{-1}}")
print(f"  delta_tau = {delta_tau_wall}")


# ============================================================
# 2. BdG DISPERSION AND IMPEDANCE
# ============================================================

def bdg_energy(k, Delta, eps):
    """E(k) = sqrt((sqrt(k^2 + eps^2) - eps)^2 + Delta^2)"""
    xi_k = np.sqrt(k**2 + eps**2) - eps
    return np.sqrt(xi_k**2 + Delta**2)

def k_from_omega(omega, Delta, eps):
    """
    Invert E(k) = omega for real k.
    Returns NaN if evanescent (omega < Delta).
    """
    if omega < Delta:
        return -1.0  # evanescent flag
    xi = np.sqrt(omega**2 - Delta**2)
    k_sq = (eps + xi)**2 - eps**2
    if k_sq < 0:
        return -1.0
    return np.sqrt(k_sq)

def group_velocity_scalar(k, Delta, eps):
    """v_g = dE/dk for scalar k > 0"""
    if k < 1e-14:
        return 0.0
    e_k = np.sqrt(k**2 + eps**2)
    xi_k = e_k - eps
    E_k = np.sqrt(xi_k**2 + Delta**2)
    return k * xi_k / (E_k * e_k)

def impedance_scalar(k, M_star, Delta, eps):
    """Z = M* * v_group"""
    vg = group_velocity_scalar(k, Delta, eps)
    return M_star * vg

def shifted_params(M_star, dM, Delta, eps, delta_tau):
    """Return shifted BdG parameters for a domain at tau_fold + delta_tau."""
    M_new = M_star + dM * delta_tau
    Delta_new = Delta * (M_new / M_star)  # Gap scales with M*
    eps_new = eps  # single-particle energy stable across fold
    return M_new, Delta_new, eps_new


# ============================================================
# 3. NUMERICALLY STABLE TRANSFER MATRIX
# ============================================================
#
# The key insight: instead of multiplying 2x2 matrices (which overflow for
# N=32 with large |r|), we track the CUMULATIVE Lyapunov exponent.
#
# For a stack of N layers, the transmission is:
#   T = |t_1 * t_2 * ... * t_N|^2 / |M_total[0,0]|^2
#
# We use the recursion relation for reflection/transmission amplitudes
# rather than raw matrix products.
#
# Alternative: rescale after each multiplication to prevent overflow.
# Track log(|M[0,0]|) separately.

def compute_transmission_stable(omega, branch_params, domain_lengths, tau_offsets):
    """
    Compute transmission through N-wall stack using numerically stable method.

    We use the rescaled transfer matrix approach:
    After each wall, extract the scale factor and accumulate log(scale).
    This prevents the matrix elements from overflowing.

    Returns:
    --------
    ln_T : float, natural log of transmission coefficient
    T    : float, transmission coefficient (may underflow to 0)
    """
    M_star = branch_params['M_star']
    dM = branch_params['dM']
    Delta_base = branch_params['Delta']
    eps_base = branch_params['eps']

    N = len(domain_lengths)

    # Accumulated log of scale factors
    log_scale = 0.0

    # Running 2x2 transfer matrix (kept O(1) by rescaling)
    M_run = np.eye(2, dtype=complex)

    for j in range(N):
        # Parameters in domain j
        dt_j = tau_offsets[j]
        M_j, Delta_j, eps_j = shifted_params(M_star, dM, Delta_base, eps_base, dt_j)

        # Parameters in domain j+1
        dt_jp1 = tau_offsets[j + 1] if j + 1 < len(tau_offsets) else tau_offsets[-1]
        M_jp1, Delta_jp1, eps_jp1 = shifted_params(M_star, dM, Delta_base, eps_base, dt_jp1)

        # Wavevector in domain j
        k_j = k_from_omega(omega, Delta_j, eps_j)

        if k_j < 0:
            # Evanescent mode in this domain
            # Compute decay constant
            if omega < Delta_j:
                kappa = np.sqrt(Delta_j**2 - omega**2)
                # For evanescent: use kappa * L as attenuation
                att = kappa * domain_lengths[j]
                if att > 500:  # Practically zero transmission
                    return -1000.0, 0.0
                # Evanescent propagation
                M_prop = np.array([[np.exp(att), 0],
                                   [0, np.exp(-att)]], dtype=complex)
            else:
                M_prop = np.eye(2, dtype=complex)
        else:
            # Propagating: accumulate phase
            phase = k_j * domain_lengths[j]
            M_prop = np.array([[np.exp(1j * phase), 0],
                               [0, np.exp(-1j * phase)]], dtype=complex)

        # Impedance at interface j -> j+1
        Z_j = impedance_scalar(max(k_j, 0), M_j, Delta_j, eps_j)
        k_jp1 = k_from_omega(omega, Delta_jp1, eps_jp1)
        Z_jp1 = impedance_scalar(max(k_jp1, 0), M_jp1, Delta_jp1, eps_jp1)

        # Reflection coefficient
        if Z_j + Z_jp1 > 1e-30:
            r = (Z_jp1 - Z_j) / (Z_jp1 + Z_j)
        else:
            r = 0.0

        # Interface transfer matrix: M = (1/t) [[1, r], [r, 1]]
        # where t^2 = 1 - r^2
        t = np.sqrt(max(1.0 - r**2, 1e-30))
        M_int = np.array([[1.0/t, r/t],
                          [r/t, 1.0/t]], dtype=complex)

        # Multiply: M_run = M_int @ M_prop @ M_run
        M_run = M_int @ M_prop @ M_run

        # Rescale to prevent overflow: extract |M[0,0]|
        scale = np.abs(M_run[0, 0])
        if scale > 1e10 or scale < 1e-10:
            if scale > 0:
                log_scale += np.log(scale)
                M_run = M_run / scale
            else:
                return -1000.0, 0.0

    # Final transmission: T = 1/|M_total[0,0]|^2
    # ln(T) = -2 * (log_scale + ln(|M_run[0,0]|))
    final_abs = np.abs(M_run[0, 0])
    if final_abs > 0:
        ln_T = -2.0 * (log_scale + np.log(final_abs))
    else:
        ln_T = -1000.0

    T = np.exp(min(ln_T, 0.0))  # Cap at 1
    return ln_T, T


# ============================================================
# 4. FREQUENCY GRID
# ============================================================

N_omega = 2000
omega_grid = np.linspace(0.05, 3.0, N_omega)


# ============================================================
# 5. BRANCH PARAMETERS
# ============================================================

branches = {
    'B2': {'M_star': M_B2, 'dM': dM_B2, 'Delta': Delta_B2, 'eps': eps_B2,
           'alpha': alpha_B2, 'label': 'B2 (quartet, 4 modes)'},
    'B1': {'M_star': M_B1, 'dM': dM_B1, 'Delta': Delta_B1, 'eps': eps_B1,
           'alpha': alpha_B1, 'label': 'B1 (singlet, 1 mode)'},
    'B3': {'M_star': M_B3, 'dM': dM_B3, 'Delta': Delta_B3, 'eps': eps_B3,
           'alpha': alpha_B3, 'label': 'B3 (triplet, 3 modes)'},
}

print(f"\nBranch dispersions at k=0:")
for bname, bp in branches.items():
    E0 = bdg_energy(0, bp['Delta'], bp['eps'])
    print(f"  {bname}: E(k=0) = Delta = {bp['Delta']:.4f} M_KK, M* = {bp['M_star']:.4f}")


# ============================================================
# 6. SINGLE-WALL TRANSMISSION
# ============================================================

print("\n" + "=" * 70)
print("SINGLE-WALL TRANSMISSION")
print("=" * 70)

single_wall_T = {}
single_wall_lnT = {}

for bname, bp in branches.items():
    domain_lengths = np.array([xi_KZ])
    tau_offsets = np.array([-delta_tau_wall/2, delta_tau_wall/2])

    T_arr = np.zeros(N_omega)
    lnT_arr = np.full(N_omega, -1000.0)

    for i, omega in enumerate(omega_grid):
        lnT, T = compute_transmission_stable(omega, bp, domain_lengths, tau_offsets)
        T_arr[i] = T
        lnT_arr[i] = lnT

    single_wall_T[bname] = T_arr
    single_wall_lnT[bname] = lnT_arr

    # DR from propagating modes
    prop_mask = T_arr > 1e-15
    if prop_mask.any():
        T_max = T_arr[prop_mask].max()
        T_min = T_arr[prop_mask].min()
        DR = np.log10(T_max / (T_min + 1e-30))
        print(f"  {bname}: T_max = {T_max:.6f}, T_min = {T_min:.6e}, DR = {DR:.3f} dec")
    else:
        # Use lnT for modes that might all be evanescent
        valid = lnT_arr > -999
        if valid.any():
            lnT_max = lnT_arr[valid].max()
            lnT_min = lnT_arr[valid].min()
            DR = (lnT_max - lnT_min) / np.log(10)
            print(f"  {bname}: lnT range [{lnT_min:.2f}, {lnT_max:.2f}], DR = {DR:.3f} dec")
        else:
            print(f"  {bname}: Fully evanescent")


# ============================================================
# 7. 32-WALL PERIODIC CASE
# ============================================================

print("\n" + "=" * 70)
print("32-WALL PERIODIC CASE")
print("=" * 70)

periodic_T = {}
periodic_lnT = {}
bloch_bands = {}

for bname, bp in branches.items():
    # Alternating tau offsets: +/-delta_tau/2
    domain_lengths = np.ones(N_domains) * xi_KZ
    tau_offsets = np.array([(-1)**j * delta_tau_wall/2 for j in range(N_domains + 1)])

    T_arr = np.zeros(N_omega)
    lnT_arr = np.full(N_omega, -1000.0)
    cosK_arr = np.zeros(N_omega)

    for i, omega in enumerate(omega_grid):
        lnT, T = compute_transmission_stable(omega, bp, domain_lengths, tau_offsets)
        T_arr[i] = T
        lnT_arr[i] = lnT

        # Bloch condition: unit cell = 2 domains (high-low impedance pair)
        domain_unit = np.array([xi_KZ, xi_KZ])
        tau_unit = np.array([-delta_tau_wall/2, delta_tau_wall/2, -delta_tau_wall/2])

        # For Bloch: need the UNSCALED unit cell matrix
        # Build it carefully
        M_star = bp['M_star']
        dM = bp['dM']
        Delta_base = bp['Delta']
        eps_base = bp['eps']

        M_unit = np.eye(2, dtype=complex)
        for jj in range(2):
            dt_j = tau_unit[jj]
            M_j, Delta_j, eps_j = shifted_params(M_star, dM, Delta_base, eps_base, dt_j)
            dt_jp1 = tau_unit[jj+1]
            M_jp1, Delta_jp1, eps_jp1 = shifted_params(M_star, dM, Delta_base, eps_base, dt_jp1)

            k_j = k_from_omega(omega, Delta_j, eps_j)
            if k_j < 0:
                if omega < Delta_j:
                    kappa = np.sqrt(Delta_j**2 - omega**2)
                    att = kappa * xi_KZ
                    M_prop = np.array([[np.exp(att), 0], [0, np.exp(-att)]], dtype=complex)
                else:
                    M_prop = np.eye(2, dtype=complex)
            else:
                phase = k_j * xi_KZ
                M_prop = np.array([[np.exp(1j*phase), 0], [0, np.exp(-1j*phase)]], dtype=complex)

            Z_j = impedance_scalar(max(k_j, 0), M_j, Delta_j, eps_j)
            k_jp1 = k_from_omega(omega, Delta_jp1, eps_jp1)
            Z_jp1 = impedance_scalar(max(k_jp1, 0), M_jp1, Delta_jp1, eps_jp1)

            if Z_j + Z_jp1 > 1e-30:
                r = (Z_jp1 - Z_j) / (Z_jp1 + Z_j)
            else:
                r = 0.0

            t = np.sqrt(max(1.0 - r**2, 1e-30))
            M_int = np.array([[1.0/t, r/t], [r/t, 1.0/t]], dtype=complex)
            M_unit = M_int @ M_prop @ M_unit

        cosK_arr[i] = np.real(np.trace(M_unit)) / 2.0

    periodic_T[bname] = T_arr
    periodic_lnT[bname] = lnT_arr
    bloch_bands[bname] = cosK_arr

    # Band gap analysis
    in_gap = np.abs(cosK_arr) > 1.0
    gap_frac = np.sum(in_gap) / N_omega

    valid = lnT_arr > -999
    if valid.any():
        lnT_max = lnT_arr[valid].max()
        lnT_min = lnT_arr[valid].min()
        DR = (lnT_max - lnT_min) / np.log(10)
        print(f"  {bname}: DR = {DR:.3f} dec, gap_frac = {gap_frac:.3f}, "
              f"lnT range [{lnT_min:.2f}, {lnT_max:.2f}]")
    else:
        print(f"  {bname}: Fully evanescent, gap_frac = {gap_frac:.3f}")


# ============================================================
# 8. 32-WALL DISORDERED (1000 REALIZATIONS)
# ============================================================

print("\n" + "=" * 70)
print("32-WALL DISORDERED (1000 REALIZATIONS)")
print("=" * 70)

N_realizations = 1000
rng = np.random.default_rng(seed=44)

disordered_lnT_mean = {}
disordered_lnT_std = {}
disordered_T_mean = {}
disordered_T_std = {}

for bname, bp in branches.items():
    t_branch = time.time()
    print(f"\n  Computing {bname} ({N_realizations} realizations)...", flush=True)

    all_lnT = np.zeros((N_realizations, N_omega))

    for r in range(N_realizations):
        # Random domain lengths from exponential distribution
        domain_lengths = rng.exponential(scale=xi_KZ, size=N_domains)
        # Random tau offsets
        tau_offsets = rng.uniform(-delta_tau_wall, delta_tau_wall, size=N_domains + 1)

        for i, omega in enumerate(omega_grid):
            lnT, _ = compute_transmission_stable(omega, bp, domain_lengths, tau_offsets)
            all_lnT[r, i] = lnT

        if (r + 1) % 200 == 0:
            elapsed = time.time() - t_branch
            print(f"    {r+1}/{N_realizations} done ({elapsed:.1f}s)", flush=True)

    # Statistics over realizations
    # Arithmetic mean of T = mean of exp(lnT) -- use log-sum-exp for stability
    lnT_mean = np.mean(all_lnT, axis=0)  # <ln T> = typical (geometric mean)
    lnT_std = np.std(all_lnT, axis=0)

    # Arithmetic mean of T using log-sum-exp
    max_lnT = np.max(all_lnT, axis=0)
    log_mean_T = max_lnT + np.log(np.mean(np.exp(all_lnT - max_lnT[np.newaxis, :]), axis=0))

    disordered_lnT_mean[bname] = lnT_mean
    disordered_lnT_std[bname] = lnT_std
    disordered_T_mean[bname] = np.exp(np.clip(log_mean_T, -500, 0))
    disordered_T_std[bname] = lnT_std  # store std of lnT

    # DR from geometric mean (typical transmission)
    valid = lnT_mean > -999
    if valid.any():
        lnT_max = lnT_mean[valid].max()
        lnT_min = lnT_mean[valid].min()
        DR_geom = (lnT_max - lnT_min) / np.log(10)

        # DR from arithmetic mean
        logT_arith = log_mean_T[valid]
        logT_arith_valid = logT_arith[logT_arith > -999]
        if len(logT_arith_valid) > 0:
            DR_arith = (logT_arith_valid.max() - logT_arith_valid.min()) / np.log(10)
        else:
            DR_arith = 0.0

        print(f"  {bname}: DR(typical/geom) = {DR_geom:.3f} dec")
        print(f"          DR(arith mean) = {DR_arith:.3f} dec")
        print(f"          <lnT> range [{lnT_min:.2f}, {lnT_max:.2f}]")
    else:
        print(f"  {bname}: Fully evanescent")

    elapsed = time.time() - t_branch
    print(f"  {bname} completed in {elapsed:.1f}s")


# ============================================================
# 9. CROSS-BRANCH DYNAMIC RANGE
# ============================================================

print("\n" + "=" * 70)
print("CROSS-BRANCH DYNAMIC RANGE")
print("=" * 70)

def cross_branch_DR_from_lnT(lnT_dict, label):
    """Compute DR across all branches from lnT arrays."""
    all_lnT = []
    for bname in ['B2', 'B1', 'B3']:
        lnT = lnT_dict[bname]
        valid = lnT > -999
        if valid.any():
            all_lnT.extend(lnT[valid].tolist())
    if len(all_lnT) > 0:
        DR = (max(all_lnT) - min(all_lnT)) / np.log(10)
        print(f"  {label}: DR = {DR:.3f} dec")
        return DR
    print(f"  {label}: No valid data")
    return 0.0

DR_single = cross_branch_DR_from_lnT(single_wall_lnT, "Single wall")
DR_periodic = cross_branch_DR_from_lnT(periodic_lnT, "32 periodic")
DR_disordered = cross_branch_DR_from_lnT(disordered_lnT_mean, "32 disordered (typical)")

# Per-branch DR table
print(f"\n  Per-branch DR (typical = geometric mean):")
print(f"  {'Branch':<8} {'Single':>10} {'Periodic':>10} {'Disordered':>12}")
DR_table = {}
for bname in ['B2', 'B1', 'B3']:
    dr_s = 0.0
    lnT = single_wall_lnT[bname]
    v = lnT[lnT > -999]
    if len(v) > 0:
        dr_s = (v.max() - v.min()) / np.log(10)

    dr_p = 0.0
    lnT = periodic_lnT[bname]
    v = lnT[lnT > -999]
    if len(v) > 0:
        dr_p = (v.max() - v.min()) / np.log(10)

    dr_d = 0.0
    lnT = disordered_lnT_mean[bname]
    v = lnT[lnT > -999]
    if len(v) > 0:
        dr_d = (v.max() - v.min()) / np.log(10)

    DR_table[bname] = [dr_s, dr_p, dr_d]
    print(f"  {bname:<8} {dr_s:>10.3f} {dr_p:>10.3f} {dr_d:>12.3f}")


# ============================================================
# 10. ANDERSON LOCALIZATION ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("ANDERSON LOCALIZATION ANALYSIS")
print("=" * 70)

# Lyapunov exponent: gamma(omega) = -<ln T(omega)> / (2 * L_total)
# Localization length: xi_loc = 1 / (2 * gamma)
# Anderson: ln(T) ~ -L / xi_loc (exponential decay)
# vs ohmic: T ~ 1/L (algebraic)

L_total_mean = N_domains * xi_KZ  # 32 * 0.152 = 4.864 M_KK^{-1}

loc_lengths = {}
lyapunov_spectra = {}

for bname in ['B2', 'B1', 'B3']:
    lnT = disordered_lnT_mean[bname]
    valid = lnT > -999

    # Lyapunov exponent
    gamma = np.zeros(N_omega)
    gamma[valid] = -lnT[valid] / (2 * L_total_mean)
    gamma[~valid] = np.nan

    lyapunov_spectra[bname] = gamma

    # Localization length
    pos_gamma = gamma[valid & (gamma > 1e-10)]
    if len(pos_gamma) > 0:
        xi_loc = 1.0 / (2.0 * pos_gamma)
        xi_med = np.median(xi_loc)
        xi_min = np.min(xi_loc)
        xi_max = np.max(xi_loc)
        ratio = L_total_mean / xi_med
        loc_lengths[bname] = {'median': xi_med, 'min': xi_min, 'max': xi_max}
        print(f"  {bname}: xi_loc = {xi_med:.3f} [{xi_min:.3f}, {xi_max:.3f}] M_KK^{{-1}}")
        print(f"    L_total/xi_loc = {ratio:.3f} (>1 = localized, <1 = extended)")
    else:
        loc_lengths[bname] = {'median': np.inf, 'min': np.inf, 'max': np.inf}
        print(f"  {bname}: No localization detected (gamma ~ 0)")


# Length scaling test
print("\n  Length scaling test:")
N_test_vals = [4, 8, 16, 32, 64, 128]
length_scaling = {}

for bname in ['B2', 'B1', 'B3']:
    bp = branches[bname]
    lnT_vs_N = []

    # Pick test frequency in propagating band
    omega_test = bp['Delta'] + 0.3
    if omega_test > 3.0:
        omega_test = bp['Delta'] + 0.05

    for N_test in N_test_vals:
        lnT_sum = 0.0
        n_valid = 0
        for _ in range(200):
            domain_lengths = rng.exponential(scale=xi_KZ, size=N_test)
            tau_offsets = rng.uniform(-delta_tau_wall, delta_tau_wall, size=N_test + 1)
            lnT, _ = compute_transmission_stable(omega_test, bp, domain_lengths, tau_offsets)
            if lnT > -999:
                lnT_sum += lnT
                n_valid += 1
        if n_valid > 0:
            lnT_vs_N.append(lnT_sum / n_valid)
        else:
            lnT_vs_N.append(-999)

    L_vals = [N * xi_KZ for N in N_test_vals]
    length_scaling[bname] = {'N': N_test_vals, 'lnT': lnT_vs_N, 'L': L_vals,
                              'omega_test': omega_test}

    # Fit: lnT = a - b*L (exponential/Anderson)
    L_arr = np.array(L_vals)
    lnT_arr = np.array(lnT_vs_N)
    valid_fit = lnT_arr > -999

    if valid_fit.sum() >= 3:
        L_fit = L_arr[valid_fit]
        lnT_fit = lnT_arr[valid_fit]

        # Linear fit: lnT = a + slope*L
        coeffs = np.polyfit(L_fit, lnT_fit, 1)
        slope = coeffs[0]
        residual_exp = np.sum((lnT_fit - np.polyval(coeffs, L_fit))**2)

        # Algebraic fit: lnT = a + c*ln(L)
        coeffs_alg = np.polyfit(np.log(L_fit), lnT_fit, 1)
        residual_alg = np.sum((lnT_fit - np.polyval(coeffs_alg, np.log(L_fit)))**2)

        if slope < 0:
            xi_loc_fit = -1.0 / slope
        else:
            xi_loc_fit = np.inf

        scaling = "Anderson (exp)" if residual_exp < residual_alg else "algebraic (1/L)"
        print(f"  {bname} at omega={omega_test:.3f}: {scaling}")
        print(f"    slope = {slope:.4f}/M_KK, xi_loc(fit) = {xi_loc_fit:.3f}")
        print(f"    residuals: exp={residual_exp:.6f}, alg={residual_alg:.6f}")
        print(f"    <lnT> at N={N_test_vals}: {['%.3f'%x if x > -999 else 'evan' for x in lnT_vs_N]}")


# ============================================================
# 11. BLOCH BAND GAP ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("BLOCH BAND STRUCTURE (PERIODIC)")
print("=" * 70)

band_gap_info = {}
for bname in ['B2', 'B1', 'B3']:
    cosK = bloch_bands[bname]
    in_gap = np.abs(cosK) > 1.0
    gap_frac = np.sum(in_gap) / N_omega

    # Find gap edges
    transitions = np.diff(in_gap.astype(int))
    gap_starts_idx = np.where(transitions == 1)[0]
    gap_ends_idx = np.where(transitions == -1)[0]

    gaps = []
    for gs_idx in gap_starts_idx:
        matching = gap_ends_idx[gap_ends_idx > gs_idx]
        if len(matching) > 0:
            ge_idx = matching[0]
            gap_lo = omega_grid[gs_idx]
            gap_hi = omega_grid[ge_idx]
            gaps.append((gap_lo, gap_hi, gap_hi - gap_lo))

    n_gaps = len(gaps)
    max_gap_width = max([g[2] for g in gaps]) if gaps else 0.0
    band_gap_info[bname] = {'n_gaps': n_gaps, 'max_gap': max_gap_width,
                             'gap_fraction': gap_frac, 'gaps': gaps}

    print(f"  {bname}: {n_gaps} Bragg gaps, max width = {max_gap_width:.4f} M_KK, "
          f"gap fraction = {gap_frac:.3f}")
    if n_gaps > 0 and n_gaps <= 10:
        for g in gaps[:5]:
            print(f"    gap: [{g[0]:.4f}, {g[1]:.4f}] width={g[2]:.4f}")


# ============================================================
# 12. GATE VERDICT
# ============================================================

print("\n" + "=" * 70)
print("GATE VERDICT: COHERENT-WALL-44")
print("=" * 70)

# The primary metric is the cross-branch DR for the disordered case
# using the TYPICAL (geometric mean) transmission, which is physically
# appropriate for disorder averaging (self-averaging of ln T).

print(f"\n  Dynamic range summary (cross-branch):")
print(f"    Single wall:      DR = {DR_single:.3f} decades")
print(f"    32 periodic:      DR = {DR_periodic:.3f} decades")
print(f"    32 disordered:    DR = {DR_disordered:.3f} decades")

# Per-branch breakdown
print(f"\n  Per-branch (disordered, typical):")
for bname in ['B2', 'B1', 'B3']:
    print(f"    {bname}: DR = {DR_table[bname][2]:.3f} dec, "
          f"xi_loc = {loc_lengths[bname]['median']:.3f} M_KK^{{-1}}")

# Gate classification
# Note: DR here is from ln(T) which includes the hard gap (omega < Delta => T = 0).
# For a fair comparison with S43's single-wall DR = 2.99,
# we should look at DR within propagating bands only.

# Compute "propagating-only" DR for disordered case:
# Restrict to omega where ALL three branches have lnT > -50 (i.e., not deeply evanescent)
DR_prop_only = {}
for bname in ['B2', 'B1', 'B3']:
    lnT = disordered_lnT_mean[bname]
    # "Propagating" = omega > Delta for this branch
    Delta = branches[bname]['Delta']
    prop = omega_grid > Delta
    valid = prop & (lnT > -500)
    if valid.any():
        lnT_v = lnT[valid]
        DR_prop_only[bname] = (lnT_v.max() - lnT_v.min()) / np.log(10)
    else:
        DR_prop_only[bname] = 0.0

print(f"\n  Propagating-only DR (disordered, per-branch):")
for bname in ['B2', 'B1', 'B3']:
    print(f"    {bname}: DR = {DR_prop_only[bname]:.3f} dec")

# Cross-branch propagating DR
all_prop_lnT = []
for bname in ['B2', 'B1', 'B3']:
    lnT = disordered_lnT_mean[bname]
    Delta = branches[bname]['Delta']
    prop = omega_grid > Delta
    valid = prop & (lnT > -500)
    if valid.any():
        all_prop_lnT.extend(lnT[valid].tolist())

if len(all_prop_lnT) > 0:
    DR_prop_cross = (max(all_prop_lnT) - min(all_prop_lnT)) / np.log(10)
else:
    DR_prop_cross = 0.0

print(f"\n  Cross-branch propagating DR (disordered): {DR_prop_cross:.3f} dec")

# The gate uses the full DR including evanescent contributions
# (evanescence IS the filtration mechanism for gapped modes)
if DR_disordered > 3.0:
    verdict = "PASS"
    verdict_reason = f"DR = {DR_disordered:.2f} > 3 decades for disordered 32-wall"
elif DR_periodic > 3.0 and DR_disordered < 3.0:
    verdict = "INFO"
    verdict_reason = (f"Periodic DR = {DR_periodic:.2f} > 3, "
                     f"disordered DR = {DR_disordered:.2f} < 3")
elif DR_disordered < 2.0 and DR_periodic < 2.0:
    verdict = "FAIL"
    verdict_reason = f"All configs DR < 2 (periodic={DR_periodic:.2f}, disordered={DR_disordered:.2f})"
else:
    verdict = "INFO"
    verdict_reason = (f"Periodic DR = {DR_periodic:.2f}, "
                     f"disordered DR = {DR_disordered:.2f}")

print(f"\n  VERDICT: {verdict}")
print(f"  Reason: {verdict_reason}")


# ============================================================
# 13. SAVE DATA
# ============================================================

save_dict = {
    # Gate results
    'verdict': np.array([verdict]),
    'verdict_reason': np.array([verdict_reason]),
    'DR_single_cross': np.array([DR_single]),
    'DR_periodic_cross': np.array([DR_periodic]),
    'DR_disordered_cross': np.array([DR_disordered]),
    'DR_prop_cross_disordered': np.array([DR_prop_cross]),
    'DR_prop_B2': np.array([DR_prop_only.get('B2', 0)]),
    'DR_prop_B1': np.array([DR_prop_only.get('B1', 0)]),
    'DR_prop_B3': np.array([DR_prop_only.get('B3', 0)]),

    # Spectra
    'omega_grid': omega_grid,
    'single_wall_lnT_B2': single_wall_lnT['B2'],
    'single_wall_lnT_B1': single_wall_lnT['B1'],
    'single_wall_lnT_B3': single_wall_lnT['B3'],
    'periodic_lnT_B2': periodic_lnT['B2'],
    'periodic_lnT_B1': periodic_lnT['B1'],
    'periodic_lnT_B3': periodic_lnT['B3'],
    'disordered_lnT_mean_B2': disordered_lnT_mean['B2'],
    'disordered_lnT_mean_B1': disordered_lnT_mean['B1'],
    'disordered_lnT_mean_B3': disordered_lnT_mean['B3'],
    'disordered_lnT_std_B2': disordered_lnT_std['B2'],
    'disordered_lnT_std_B1': disordered_lnT_std['B1'],
    'disordered_lnT_std_B3': disordered_lnT_std['B3'],

    # Bloch bands
    'bloch_cosK_B2': bloch_bands['B2'],
    'bloch_cosK_B1': bloch_bands['B1'],
    'bloch_cosK_B3': bloch_bands['B3'],

    # Band gaps
    'n_gaps_B2': np.array([band_gap_info['B2']['n_gaps']]),
    'n_gaps_B1': np.array([band_gap_info['B1']['n_gaps']]),
    'n_gaps_B3': np.array([band_gap_info['B3']['n_gaps']]),
    'max_gap_B2': np.array([band_gap_info['B2']['max_gap']]),
    'max_gap_B1': np.array([band_gap_info['B1']['max_gap']]),
    'max_gap_B3': np.array([band_gap_info['B3']['max_gap']]),

    # Localization
    'lyap_B2': lyapunov_spectra['B2'],
    'lyap_B1': lyapunov_spectra['B1'],
    'lyap_B3': lyapunov_spectra['B3'],
    'xi_loc_median_B2': np.array([loc_lengths['B2']['median']]),
    'xi_loc_median_B1': np.array([loc_lengths['B1']['median']]),
    'xi_loc_median_B3': np.array([loc_lengths['B3']['median']]),

    # Length scaling
    'length_scaling_N': np.array(N_test_vals),
    'length_scaling_B2_lnT': np.array(length_scaling['B2']['lnT']),
    'length_scaling_B1_lnT': np.array(length_scaling['B1']['lnT']),
    'length_scaling_B3_lnT': np.array(length_scaling['B3']['lnT']),

    # Parameters
    'xi_KZ': np.array([xi_KZ]),
    'N_domains': np.array([N_domains]),
    'delta_tau_wall': np.array([delta_tau_wall]),
    'N_realizations': np.array([N_realizations]),
    'gap_edge': np.array([gap_edge]),
    'L_total_mean': np.array([L_total_mean]),
}

np.savez('tier0-computation/s44_coherent_wall.npz', **save_dict)
print("\n  Data saved to tier0-computation/s44_coherent_wall.npz")


# ============================================================
# 14. PLOT
# ============================================================

fig, axes = plt.subplots(3, 2, figsize=(16, 14))
fig.suptitle('COHERENT-WALL-44: Multi-Wall Bragg Transfer Matrix\n'
             f'32 KZ domains, $\\xi_{{KZ}}$ = {xi_KZ:.3f} M$_{{KK}}^{{-1}}$, '
             f'$\\delta\\tau$ = {delta_tau_wall}', fontsize=13, fontweight='bold')

colors = {'B2': '#2166ac', 'B1': '#b2182b', 'B3': '#1b7837'}
branch_labels = {'B2': 'B2 (quartet)', 'B1': 'B1 (singlet)', 'B3': 'B3 (triplet)'}

# (a) Single-wall ln(T)
ax = axes[0, 0]
for bname in ['B2', 'B1', 'B3']:
    lnT = single_wall_lnT[bname]
    valid = lnT > -100
    if valid.any():
        T_plot = np.exp(np.clip(lnT[valid], -50, 0))
        ax.semilogy(omega_grid[valid], T_plot, color=colors[bname],
                   label=branch_labels[bname], linewidth=1.2)
ax.set_xlabel(r'$\omega$ [M$_{\rm KK}$]', fontsize=11)
ax.set_ylabel(r'$T(\omega)$', fontsize=11)
ax.set_title(f'(a) Single Wall  |  DR = {DR_single:.2f} dec', fontsize=11)
ax.legend(fontsize=9)
ax.set_ylim(1e-6, 2)
ax.axhline(1.0, color='gray', linestyle='--', alpha=0.3)
ax.set_xlim(0, 3)

# (b) 32-wall periodic ln(T)
ax = axes[0, 1]
for bname in ['B2', 'B1', 'B3']:
    lnT = periodic_lnT[bname]
    valid = lnT > -100
    if valid.any():
        T_plot = np.exp(np.clip(lnT[valid], -50, 0))
        ax.semilogy(omega_grid[valid], T_plot, color=colors[bname],
                   label=branch_labels[bname], linewidth=0.6)
ax.set_xlabel(r'$\omega$ [M$_{\rm KK}$]', fontsize=11)
ax.set_ylabel(r'$T(\omega)$', fontsize=11)
ax.set_title(f'(b) 32 Periodic  |  DR = {DR_periodic:.2f} dec', fontsize=11)
ax.legend(fontsize=9)
ax.set_ylim(1e-20, 2)
ax.axhline(1.0, color='gray', linestyle='--', alpha=0.3)
ax.set_xlim(0, 3)

# (c) 32-wall disordered mean ln(T)
ax = axes[1, 0]
for bname in ['B2', 'B1', 'B3']:
    lnT = disordered_lnT_mean[bname]
    lnT_s = disordered_lnT_std[bname]
    valid = lnT > -100
    if valid.any():
        T_plot = np.exp(np.clip(lnT[valid], -50, 0))
        ax.semilogy(omega_grid[valid], T_plot, color=colors[bname],
                   label=branch_labels[bname], linewidth=1)
        # Error band from std of lnT
        T_upper = np.exp(np.clip(lnT[valid] + lnT_s[valid], -50, 0))
        T_lower = np.exp(np.clip(lnT[valid] - lnT_s[valid], -50, 0))
        ax.fill_between(omega_grid[valid], T_lower, T_upper,
                        color=colors[bname], alpha=0.15)
ax.set_xlabel(r'$\omega$ [M$_{\rm KK}$]', fontsize=11)
ax.set_ylabel(r'$\langle T(\omega) \rangle_{\rm typ}$', fontsize=11)
ax.set_title(f'(c) 32 Disordered (N={N_realizations})  |  DR = {DR_disordered:.2f} dec',
             fontsize=11)
ax.legend(fontsize=9)
ax.set_ylim(1e-20, 2)
ax.axhline(1.0, color='gray', linestyle='--', alpha=0.3)
ax.set_xlim(0, 3)

# (d) Bloch band structure
ax = axes[1, 1]
for bname in ['B2', 'B1', 'B3']:
    cosK = bloch_bands[bname]
    ax.plot(omega_grid, cosK, color=colors[bname], label=branch_labels[bname], linewidth=0.8)
ax.axhline(1.0, color='black', linestyle='--', alpha=0.5)
ax.axhline(-1.0, color='black', linestyle='--', alpha=0.5)
ax.set_xlabel(r'$\omega$ [M$_{\rm KK}$]', fontsize=11)
ax.set_ylabel(r'$\cos(Kd)$', fontsize=11)
ax.set_title('(d) Bloch Band Structure (Periodic)', fontsize=11)
ax.set_ylim(-5, 5)
ax.legend(fontsize=9)
ax.set_xlim(0, 3)
# Shade gap regions for B1 (most prominent)
cosK_B1 = bloch_bands['B1']
in_gap_B1 = np.abs(cosK_B1) > 1.0
ax.fill_between(omega_grid, -5, 5, where=in_gap_B1, color='red', alpha=0.06)

# (e) Anderson localization: <lnT> vs L
ax = axes[2, 0]
for bname in ['B2', 'B1', 'B3']:
    ls = length_scaling[bname]
    valid = [x > -999 for x in ls['lnT']]
    L_v = [ls['L'][i] for i in range(len(valid)) if valid[i]]
    lnT_v = [ls['lnT'][i] for i in range(len(valid)) if valid[i]]
    if len(L_v) > 0:
        ax.plot(L_v, lnT_v, 'o-', color=colors[bname],
               label=f'{bname} ($\\omega$={ls["omega_test"]:.2f})', linewidth=1.5, markersize=5)
ax.set_xlabel(r'$L$ [M$_{\rm KK}^{-1}$]', fontsize=11)
ax.set_ylabel(r'$\langle \ln T \rangle$', fontsize=11)
ax.set_title('(e) Length Scaling (Anderson Test)', fontsize=11)
ax.legend(fontsize=9)

# (f) Lyapunov exponent spectrum
ax = axes[2, 1]
for bname in ['B2', 'B1', 'B3']:
    gamma = lyapunov_spectra[bname]
    valid = ~np.isnan(gamma) & (gamma > 1e-10)
    if valid.any():
        ax.plot(omega_grid[valid], gamma[valid], color=colors[bname],
               label=branch_labels[bname], linewidth=0.8)
ax.set_xlabel(r'$\omega$ [M$_{\rm KK}$]', fontsize=11)
ax.set_ylabel(r'$\gamma(\omega)$ [M$_{\rm KK}$]', fontsize=11)
ax.set_title('(f) Lyapunov Exponent Spectrum', fontsize=11)
ax.legend(fontsize=9)

plt.tight_layout()
plt.savefig('tier0-computation/s44_coherent_wall.png', dpi=150, bbox_inches='tight')
print("  Plot saved to tier0-computation/s44_coherent_wall.png")

elapsed_total = time.time() - t_start
print(f"\n  Total runtime: {elapsed_total:.1f}s")
print("\n" + "=" * 70)
print("COMPUTATION COMPLETE")
print("=" * 70)
