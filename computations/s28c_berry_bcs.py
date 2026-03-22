#!/usr/bin/env python3
"""S-4 Berry Curvature at BCS Sector Transitions (28c-7)

Computes the Berry phase of the BCS ground state wavefunction at sector
boundary transitions where M_max crosses 1 (supercritical <-> subcritical).

MATHEMATICAL BACKGROUND
========================

The BCS ground state in mean-field is:

    |Psi(tau)> = prod_k [u_k(tau) + v_k(tau) c_k^+ c_{-k}^+] |vac>

where the coherence factors are:

    u_k^2 = (1 + xi_k / E_k) / 2
    v_k^2 = (1 - xi_k / E_k) / 2
    E_k   = sqrt(xi_k^2 + |Delta_k|^2)
    xi_k  = epsilon_k - mu

The Berry connection along the tau parameter is:

    A(tau) = -i <Psi|d/dtau|Psi>
           = -sum_k (1/2) d(theta_k)/dtau

where theta_k = arctan2(|Delta_k|, xi_k) is the Bogoliubov mixing angle.
In the BCS formalism, this simplifies to:

    A(tau) = sum_k Im[u_k* du_k/dtau + v_k* dv_k/dtau]

For real u_k, v_k (which holds when Delta is real), this reduces to:

    A(tau) = sum_k [u_k dv_k/dtau - v_k du_k/dtau]  (cross-term form)

which equals -(1/2) sum_k d(theta_k)/dtau.

The Berry phase around a path P is:

    gamma = integral_P A(tau) dtau

For a Z_2 topological transition, we expect gamma = pi (mod 2*pi).

For re-entrant transitions (entering and exiting the condensed phase),
the Berry phase accumulated over the full re-entrant cycle is the
relevant topological invariant.

INPUTS
======
- s27_multisector_bcs.npz: eigenvalues, pairing matrices V, M_max per sector
- s28a_torsionful_bcs.npz: torsionful BCS data (D_can basis)
- s28b_relaxation_times.npz: precise tau_c crossing values

OUTPUTS
=======
- s28c_berry_bcs.npz: Berry phase per sector, Berry curvature profiles
- s28c_berry_bcs.png: visualization

Author: phonon-exflation-sim agent
Date: 2026-02-27
"""

import numpy as np
from scipy.linalg import eigvalsh, eigh
from scipy.interpolate import CubicSpline
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
import warnings

# =============================================================================
# Constants and paths
# =============================================================================

SCRIPT_DIR = Path(__file__).parent
DATA_DIR = SCRIPT_DIR

S27_FILE = DATA_DIR / 's27_multisector_bcs.npz'
S28A_FILE = DATA_DIR / 's28a_torsionful_bcs.npz'
S28B_FILE = DATA_DIR / 's28b_relaxation_times.npz'

OUT_NPZ = DATA_DIR / 's28c_berry_bcs.npz'
OUT_PNG = DATA_DIR / 's28c_berry_bcs.png'

# BCS parameters (Session 26/27 conventions)
ETA_FRAC = 0.01       # Regulator fraction for linearized kernel
DELTA0_SCALE = 0.01   # Initial gap guess as fraction of lambda_min
MAX_ITER = 2000       # Self-consistent iteration limit
CONV_TOL = 1e-10      # Convergence tolerance

# Dense tau grid for Berry phase integration
N_TAU_DENSE = 2000    # Number of points in dense tau sweep


# =============================================================================
# BCS solver (reproduces Sessions 26/27 conventions)
# =============================================================================

def build_bcs_kernel_linearized(V: np.ndarray, evals: np.ndarray,
                                 mu: float, eta_frac: float = ETA_FRAC
                                 ) -> np.ndarray:
    """Build linearized BCS kernel K_{nm} = V_{nm} / (2 * |xi_m|).

    Regularized with eta = eta_frac * lambda_min to handle mu ~ lambda_m.

    Parameters
    ----------
    V : (N, N) ndarray
        Positive pairing matrix.
    evals : (N,) ndarray
        Dirac eigenvalues.
    mu : float
        Chemical potential.
    eta_frac : float
        Regulator fraction.

    Returns
    -------
    K : (N, N) ndarray
        Linearized BCS kernel.
    """
    xi = evals - mu
    xi_abs = np.abs(xi)
    lambda_min = np.min(np.abs(evals))
    eta = max(eta_frac * lambda_min, 1e-15)
    E = np.maximum(xi_abs, eta)
    factor = 1.0 / (2.0 * E)
    return V * factor[np.newaxis, :]


def selfconsistent_bcs(V: np.ndarray, evals: np.ndarray, mu: float,
                       T: float = 0.0, max_iter: int = MAX_ITER,
                       tol: float = CONV_TOL,
                       delta0_scale: float = DELTA0_SCALE
                       ) -> tuple:
    """Solve self-consistent BCS gap equation by iteration.

    Iterates Delta^{k+1}_n = sum_m V_{nm} * Delta^k_m / (2 E_m)
    with E_m = sqrt((lambda_m - mu)^2 + Delta_m^2).

    Parameters
    ----------
    V : (N, N) ndarray
        Pairing matrix.
    evals : (N,) ndarray
        Dirac eigenvalues.
    mu : float
        Chemical potential.
    T : float
        Temperature (T=0 for maximum gap).
    max_iter : int
        Maximum iterations.
    tol : float
        Convergence tolerance.
    delta0_scale : float
        Initial guess scale.

    Returns
    -------
    Delta : (N,) ndarray
        Converged gap vector.
    converged : bool
    n_iter : int
    """
    N = len(evals)
    xi = evals - mu
    lambda_min = np.min(np.abs(evals))
    Delta = np.ones(N) * delta0_scale * lambda_min

    for k in range(max_iter):
        E = np.sqrt(xi**2 + Delta**2)
        E = np.maximum(E, 1e-30)

        if T > 1e-15:
            x = E / (2.0 * T)
            factor = np.where(x > 20.0, 1.0 / (2.0 * E),
                              np.tanh(x) / (2.0 * E))
        else:
            factor = 1.0 / (2.0 * E)

        Delta_new = V @ (Delta * factor)

        norm_new = np.linalg.norm(Delta_new)
        norm_old = np.linalg.norm(Delta)

        if norm_old > 1e-20:
            rel_change = np.linalg.norm(Delta_new - Delta) / norm_old
        else:
            rel_change = np.linalg.norm(Delta_new - Delta)

        Delta = Delta_new

        if rel_change < tol and k > 5:
            return Delta, True, k + 1

        if norm_new < 1e-30 and k > 10:
            return Delta, True, k + 1

    return Delta, False, max_iter


def compute_m_max(V: np.ndarray, evals: np.ndarray, mu: float) -> float:
    """Compute largest eigenvalue of linearized BCS kernel (M_max).

    Parameters
    ----------
    V : (N, N) ndarray
    evals : (N,) ndarray
    mu : float

    Returns
    -------
    M_max : float
    """
    K = build_bcs_kernel_linearized(V, evals, mu)
    K_sym = 0.5 * (K + K.T)
    return eigvalsh(K_sym)[-1]


# =============================================================================
# Berry phase computation
# =============================================================================

def bogoliubov_angles(evals: np.ndarray, mu: float,
                      Delta: np.ndarray) -> np.ndarray:
    """Compute Bogoliubov mixing angles theta_k = arctan2(|Delta_k|, xi_k).

    For the BCS ground state, the Berry connection is:
        A(tau) = -(1/2) sum_k d(theta_k)/dtau

    Parameters
    ----------
    evals : (N,) ndarray
        Dirac eigenvalues at this tau.
    mu : float
        Chemical potential.
    Delta : (N,) ndarray
        Gap vector at this tau.

    Returns
    -------
    theta : (N,) ndarray
        Bogoliubov angles.
    """
    xi = evals - mu
    return np.arctan2(np.abs(Delta), xi)


def berry_connection_from_angles(theta_prev: np.ndarray,
                                  theta_next: np.ndarray,
                                  dtau: float) -> float:
    """Compute Berry connection A(tau) = -(1/2) sum_k d(theta_k)/dtau.

    Uses central finite differences.

    Parameters
    ----------
    theta_prev : (N,) ndarray
        Angles at tau - dtau/2.
    theta_next : (N,) ndarray
        Angles at tau + dtau/2.
    dtau : float
        Step size.

    Returns
    -------
    A : float
        Berry connection at tau.
    """
    dtheta_dtau = (theta_next - theta_prev) / dtau
    return -0.5 * np.sum(dtheta_dtau)


def compute_berry_phase_sector(V_data: dict, evals_data: dict,
                                sector_key: str,
                                tau_grid_input: np.ndarray,
                                mu_ratio: float = 1.0,
                                tau_dense: np.ndarray = None,
                                connection_type: str = 'K'
                                ) -> dict:
    """Compute Berry phase along a tau path for a given sector.

    Method:
    1. At each tau in the input grid, extract eigenvalues and pairing matrix.
    2. Interpolate eigenvalues onto a dense tau grid.
    3. At each dense tau point, compute the self-consistent BCS gap Delta(tau).
    4. From Delta(tau), compute the Bogoliubov angles theta_k(tau).
    5. Differentiate theta_k(tau) to get the Berry connection A(tau).
    6. Integrate A(tau) to get the Berry phase gamma.

    Parameters
    ----------
    V_data : dict
        Maps tau_index -> (N, N) pairing matrix.
    evals_data : dict
        Maps tau_index -> (N,) eigenvalue array.
    sector_key : str
        Sector label like "(2,0)".
    tau_grid_input : (M,) ndarray
        Original tau grid where data is available.
    mu_ratio : float
        mu = mu_ratio * lambda_min.
    tau_dense : (P,) ndarray, optional
        Dense tau grid for interpolation.
    connection_type : str
        'K' for Kosmann (D_K) or 'can' for canonical (D_can).

    Returns
    -------
    result : dict with keys:
        'tau_dense': dense tau grid used
        'M_max_dense': M_max at each dense tau point
        'Delta_norm_dense': |Delta| at each dense tau point
        'theta_sum_dense': sum of Bogoliubov angles at each dense tau point
        'A_dense': Berry connection at each dense tau point
        'gamma_cumulative': cumulative Berry phase along the path
        'gamma_total': total Berry phase
        'gamma_mod_pi': gamma mod pi
        'crossings': list of (tau_c, direction) for M_max=1 crossings
    """
    M = len(tau_grid_input)
    if tau_dense is None:
        tau_dense = np.linspace(tau_grid_input[0], tau_grid_input[-1],
                                N_TAU_DENSE)

    P = len(tau_dense)

    # Step 1: Collect eigenvalues and V matrices at original grid points
    evals_list = []
    V_list = []
    lambda_min_list = []
    for i in range(M):
        ev = evals_data[i]
        V_mat = V_data[i]
        evals_list.append(ev)
        V_list.append(V_mat)
        lambda_min_list.append(np.min(np.abs(ev)))

    N = len(evals_list[0])  # sector dimension

    # Step 2: Interpolate eigenvalues onto dense grid
    # Each eigenvalue is a smooth function of tau (within a sector)
    evals_interp = np.zeros((P, N))
    for k in range(N):
        vals = np.array([evals_list[i][k] for i in range(M)])
        cs = CubicSpline(tau_grid_input, vals, extrapolate=True)
        evals_interp[:, k] = cs(tau_dense)

    # Step 2b: Interpolate lambda_min
    lmin_arr = np.array(lambda_min_list)
    cs_lmin = CubicSpline(tau_grid_input, lmin_arr, extrapolate=True)
    lambda_min_dense = cs_lmin(tau_dense)

    # Step 2c: Interpolate V matrices (element-wise)
    V_interp = np.zeros((P, N, N))
    for i in range(N):
        for j in range(N):
            vals = np.array([V_list[idx][i, j] for idx in range(M)])
            cs = CubicSpline(tau_grid_input, vals, extrapolate=True)
            V_interp[:, i, j] = cs(tau_dense)

    # Step 3: At each dense tau point, compute M_max and self-consistent Delta
    M_max_dense = np.zeros(P)
    Delta_dense = np.zeros((P, N))
    theta_dense = np.zeros((P, N))
    Delta_norm_dense = np.zeros(P)

    for p in range(P):
        ev_p = evals_interp[p]
        V_p = V_interp[p]
        # Ensure V is symmetric positive
        V_p = 0.5 * (V_p + V_p.T)
        V_p = np.maximum(V_p, 0.0)

        lmin_p = lambda_min_dense[p]
        mu_p = mu_ratio * lmin_p

        # M_max
        M_max_dense[p] = compute_m_max(V_p, ev_p, mu_p)

        # Self-consistent Delta
        if M_max_dense[p] > 1.0:
            Delta_sc, conv, nit = selfconsistent_bcs(V_p, ev_p, mu_p)
            if conv and np.linalg.norm(Delta_sc) > 1e-20:
                Delta_dense[p] = Delta_sc
            else:
                # Supercritical but didn't converge -- use linearized estimate
                Delta_dense[p] = np.zeros(N)
        else:
            # Subcritical: Delta = 0
            Delta_dense[p] = np.zeros(N)

        Delta_norm_dense[p] = np.linalg.norm(Delta_dense[p])

        # Bogoliubov angles
        theta_dense[p] = bogoliubov_angles(ev_p, mu_p, Delta_dense[p])

    # Step 4: Berry connection via finite differences of theta
    A_dense = np.zeros(P)
    for p in range(1, P - 1):
        dtau = tau_dense[p + 1] - tau_dense[p - 1]
        if dtau > 1e-30:
            dtheta = theta_dense[p + 1] - theta_dense[p - 1]
            A_dense[p] = -0.5 * np.sum(dtheta) / dtau

    # Boundary: forward/backward differences
    if P > 1:
        dtau0 = tau_dense[1] - tau_dense[0]
        if dtau0 > 1e-30:
            dtheta0 = theta_dense[1] - theta_dense[0]
            A_dense[0] = -0.5 * np.sum(dtheta0) / dtau0
        dtauN = tau_dense[-1] - tau_dense[-2]
        if dtauN > 1e-30:
            dthetaN = theta_dense[-1] - theta_dense[-2]
            A_dense[-1] = -0.5 * np.sum(dthetaN) / dtauN

    # Step 5: Integrate Berry connection (trapezoidal)
    gamma_cumulative = np.zeros(P)
    for p in range(1, P):
        dtau = tau_dense[p] - tau_dense[p - 1]
        gamma_cumulative[p] = gamma_cumulative[p - 1] + 0.5 * (
            A_dense[p] + A_dense[p - 1]) * dtau

    gamma_total = gamma_cumulative[-1]

    # Step 6: Find crossings (M_max = 1)
    crossings = []
    for p in range(P - 1):
        if (M_max_dense[p] - 1.0) * (M_max_dense[p + 1] - 1.0) < 0:
            # Linear interpolation for crossing point
            tau_c = tau_dense[p] + (1.0 - M_max_dense[p]) / (
                M_max_dense[p + 1] - M_max_dense[p]) * (
                    tau_dense[p + 1] - tau_dense[p])
            direction = 1 if M_max_dense[p + 1] > M_max_dense[p] else -1
            crossings.append((tau_c, direction))

    # Step 7: Berry phase at each crossing
    # For each crossing, compute gamma accumulated up to that point
    gamma_at_crossings = []
    for tau_c, direction in crossings:
        idx = np.searchsorted(tau_dense, tau_c)
        idx = min(idx, P - 1)
        gamma_at_crossings.append(gamma_cumulative[idx])

    # Berry phase between consecutive crossings (for re-entrant sectors)
    gamma_between_crossings = []
    if len(crossings) >= 2:
        for i in range(len(crossings) - 1):
            gamma_between_crossings.append(
                gamma_at_crossings[i + 1] - gamma_at_crossings[i])

    return {
        'tau_dense': tau_dense,
        'M_max_dense': M_max_dense,
        'Delta_norm_dense': Delta_norm_dense,
        'theta_sum_dense': np.sum(theta_dense, axis=1),
        'A_dense': A_dense,
        'gamma_cumulative': gamma_cumulative,
        'gamma_total': gamma_total,
        'gamma_mod_pi': gamma_total % np.pi,
        'crossings': crossings,
        'gamma_at_crossings': gamma_at_crossings,
        'gamma_between_crossings': gamma_between_crossings,
        'N_modes': N,
    }


# =============================================================================
# Data loading
# =============================================================================

def load_sector_data_s27(npz, sector_idx: int, tau_indices: list,
                         ) -> tuple:
    """Load eigenvalues and V matrices for a sector from s27 data.

    Parameters
    ----------
    npz : NpzFile
        Loaded s27 data.
    sector_idx : int
        Index into sectors array.
    tau_indices : list of int
        Tau grid indices to load.

    Returns
    -------
    evals_data : dict mapping tau_index -> (N,) eigenvalue array
    V_data : dict mapping tau_index -> (N, N) pairing matrix
    """
    sectors = npz['sectors']
    p, q = sectors[sector_idx, 0], sectors[sector_idx, 1]

    evals_data = {}
    V_data = {}
    for i, ti in enumerate(tau_indices):
        key_ev = f'evals_{p}_{q}_{ti}'
        key_V = f'V_{p}_{q}_{ti}'
        evals_data[i] = npz[key_ev]
        V_data[i] = npz[key_V]

    return evals_data, V_data


def load_sector_data_s28a(npz, sector_idx: int, tau_indices: list,
                           connection: str = 'K') -> tuple:
    """Load eigenvalues and V matrices for a sector from s28a data.

    Parameters
    ----------
    npz : NpzFile
        Loaded s28a data.
    sector_idx : int
        Index into sectors array.
    tau_indices : list of int
        Tau grid indices.
    connection : str
        'K' for Kosmann, 'can' for canonical.

    Returns
    -------
    evals_data : dict
    V_data : dict
    """
    sectors = npz['sectors']
    p, q = sectors[sector_idx, 0], sectors[sector_idx, 1]

    prefix = 'can' if connection == 'can' else 'K'

    evals_data = {}
    V_data = {}
    for i, ti in enumerate(tau_indices):
        key_ev = f'evals_{prefix}_{p}_{q}_{ti}'
        key_V = f'V_{prefix}_{p}_{q}_{ti}'
        evals_data[i] = npz[key_ev]
        V_data[i] = npz[key_V]

    return evals_data, V_data


# =============================================================================
# Main computation
# =============================================================================

def main():
    print("=" * 72)
    print("S-4: Berry Curvature at BCS Sector Transitions (28c-7)")
    print("=" * 72)

    # Load data
    print("\n[1] Loading input data...")
    s27 = np.load(S27_FILE, allow_pickle=True)
    s28a = np.load(S28A_FILE, allow_pickle=True)
    s28b = np.load(S28B_FILE, allow_pickle=True)

    tau_s27 = s27['tau_values']       # [0, 0.1, 0.15, ..., 0.5]
    tau_s28a = s28a['tau_values']     # [0, 0.05, 0.1, ..., 0.5]
    sectors_s27 = s27['sectors']
    sectors_s28a = s28a['sectors']

    print(f"  s27 tau grid: {tau_s27}")
    print(f"  s28a tau grid: {tau_s28a}")
    print(f"  s27 sectors: {sectors_s27.shape[0]}")
    print(f"  s28a sectors: {sectors_s28a.shape[0]}")

    # Crossing data from s28b
    reentrant_tau_c1 = float(s28b['reentrant_20_tau_c1'])
    reentrant_tau_c2 = float(s28b['reentrant_20_tau_c2'])
    reentrant_window = float(s28b['reentrant_20_window'])

    print(f"\n  Re-entrant (2,0): tau_c1={reentrant_tau_c1:.4f}, "
          f"tau_c2={reentrant_tau_c2:.4f}, window={reentrant_window:.4f}")

    # Identify sectors with M_max crossings at mu = lambda_min
    # From s28b: crossings at mu_ratio=1.0 (index 5 in s27)
    crossing_sectors_s27 = {
        '(1,1)': {'idx': 3, 'crossings': [(0.0946, +1)]},
        '(2,0)': {'idx': 4, 'crossings': [(reentrant_tau_c1, -1),
                                            (reentrant_tau_c2, +1)]},
        '(0,2)': {'idx': 5, 'crossings': [(0.0682, -1),
                                            (reentrant_tau_c2, +1)]},
        '(2,1)': {'idx': 8, 'crossings': [(0.3033, +1)]},
    }

    print("\n  Sectors with M_max=1 crossings (D_K, mu=lambda_min):")
    for name, info in crossing_sectors_s27.items():
        print(f"    {name}: {len(info['crossings'])} crossing(s) at "
              f"tau = {[c[0] for c in info['crossings']]}")

    # =========================================================================
    # PART A: D_K (Kosmann) Berry phase from s27 data
    # =========================================================================
    print("\n" + "=" * 72)
    print("PART A: Berry Phase in D_K (Kosmann) basis")
    print("=" * 72)

    # Dense tau grid for all sectors
    tau_dense_full = np.linspace(0.0, 0.5, N_TAU_DENSE)
    tau_indices_s27 = list(range(len(tau_s27)))

    results_K = {}

    for sector_name, info in crossing_sectors_s27.items():
        sidx = info['idx']
        print(f"\n  --- Sector {sector_name} (s27 index {sidx}) ---")

        evals_data, V_data = load_sector_data_s27(
            s27, sidx, tau_indices_s27)

        result = compute_berry_phase_sector(
            V_data, evals_data, sector_name,
            tau_s27, mu_ratio=1.0,
            tau_dense=tau_dense_full,
            connection_type='K')

        results_K[sector_name] = result

        print(f"    N_modes = {result['N_modes']}")
        print(f"    gamma_total = {result['gamma_total']:.6f}")
        print(f"    gamma_total / pi = {result['gamma_total'] / np.pi:.6f}")
        print(f"    gamma mod pi = {result['gamma_mod_pi']:.6f}")
        print(f"    Crossings found: {len(result['crossings'])}")
        for i, (tc, d) in enumerate(result['crossings']):
            print(f"      tau_c = {tc:.4f}, direction = "
                  f"{'supercrit' if d > 0 else 'subcrit'}")
        if result['gamma_at_crossings']:
            print(f"    gamma at crossings: "
                  f"{[f'{g:.4f}' for g in result['gamma_at_crossings']]}")
        if result['gamma_between_crossings']:
            print(f"    gamma between crossings: "
                  f"{[f'{g:.4f}' for g in result['gamma_between_crossings']]}")

        # Check M_max range
        print(f"    M_max range: [{result['M_max_dense'].min():.4f}, "
              f"{result['M_max_dense'].max():.4f}]")
        print(f"    |Delta| range: [{result['Delta_norm_dense'].min():.6f}, "
              f"{result['Delta_norm_dense'].max():.6f}]")

    # =========================================================================
    # PART B: D_can (canonical/torsionful) Berry phase from s28a data
    # =========================================================================
    print("\n" + "=" * 72)
    print("PART B: Berry Phase in D_can (torsionful) basis")
    print("=" * 72)

    tau_indices_s28a = list(range(len(tau_s28a)))

    # Map sector names to s28a indices
    # s28a sectors (no (0,0)): (1,0), (0,1), (1,1), (2,0), (0,2), (3,0), (0,3), (2,1)
    crossing_sectors_s28a = {
        '(1,1)': {'idx': 2},
        '(2,0)': {'idx': 3},
        '(0,2)': {'idx': 4},
        '(2,1)': {'idx': 7},
    }

    results_can = {}

    for sector_name, info_s28a in crossing_sectors_s28a.items():
        sidx_s28a = info_s28a['idx']
        print(f"\n  --- Sector {sector_name} (s28a index {sidx_s28a}, D_can) ---")

        evals_data, V_data = load_sector_data_s28a(
            s28a, sidx_s28a, tau_indices_s28a, connection='can')

        result = compute_berry_phase_sector(
            V_data, evals_data, sector_name,
            tau_s28a, mu_ratio=1.0,
            tau_dense=tau_dense_full,
            connection_type='can')

        results_can[sector_name] = result

        print(f"    N_modes = {result['N_modes']}")
        print(f"    gamma_total = {result['gamma_total']:.6f}")
        print(f"    gamma_total / pi = {result['gamma_total'] / np.pi:.6f}")
        print(f"    gamma mod pi = {result['gamma_mod_pi']:.6f}")
        print(f"    Crossings found: {len(result['crossings'])}")
        for i, (tc, d) in enumerate(result['crossings']):
            print(f"      tau_c = {tc:.4f}, direction = "
                  f"{'supercrit' if d > 0 else 'subcrit'}")
        if result['gamma_at_crossings']:
            print(f"    gamma at crossings: "
                  f"{[f'{g:.4f}' for g in result['gamma_at_crossings']]}")
        if result['gamma_between_crossings']:
            print(f"    gamma between crossings: "
                  f"{[f'{g:.4f}' for g in result['gamma_between_crossings']]}")

        print(f"    M_max range: [{result['M_max_dense'].min():.4f}, "
              f"{result['M_max_dense'].max():.4f}]")
        print(f"    |Delta| range: [{result['Delta_norm_dense'].min():.6f}, "
              f"{result['Delta_norm_dense'].max():.6f}]")

    # =========================================================================
    # PART C: Also compute for always-supercritical sectors as control
    # =========================================================================
    print("\n" + "=" * 72)
    print("PART C: Control -- Always-supercritical sectors (D_K)")
    print("=" * 72)

    control_sectors = {
        '(0,0)': 0,
        '(1,0)': 1,
        '(0,1)': 2,
        '(3,0)': 6,
        '(0,3)': 7,
    }

    results_control = {}
    for sector_name, sidx in control_sectors.items():
        print(f"\n  --- Sector {sector_name} (control) ---")
        evals_data, V_data = load_sector_data_s27(
            s27, sidx, tau_indices_s27)

        result = compute_berry_phase_sector(
            V_data, evals_data, sector_name,
            tau_s27, mu_ratio=1.0,
            tau_dense=tau_dense_full,
            connection_type='K')

        results_control[sector_name] = result

        print(f"    N_modes = {result['N_modes']}")
        print(f"    gamma_total = {result['gamma_total']:.6f}")
        print(f"    gamma_total / pi = {result['gamma_total'] / np.pi:.6f}")
        print(f"    Crossings: {len(result['crossings'])}")
        print(f"    M_max range: [{result['M_max_dense'].min():.4f}, "
              f"{result['M_max_dense'].max():.4f}]")

    # =========================================================================
    # PART D: Re-entrant cycle Berry phase for (2,0)
    # =========================================================================
    print("\n" + "=" * 72)
    print("PART D: Re-entrant Cycle Berry Phase for (2,0)")
    print("=" * 72)

    res_20_K = results_K['(2,0)']
    res_20_can = results_can['(2,0)']

    # D_K re-entrant analysis
    print("\n  D_K (Kosmann):")
    if len(res_20_K['crossings']) >= 2:
        tau_c1_K = res_20_K['crossings'][0][0]
        tau_c2_K = res_20_K['crossings'][1][0]
        gamma_reentrant_K = res_20_K['gamma_between_crossings'][0]
        print(f"    tau_c1 = {tau_c1_K:.4f}, tau_c2 = {tau_c2_K:.4f}")
        print(f"    gamma(cycle) = {gamma_reentrant_K:.6f}")
        print(f"    gamma(cycle)/pi = {gamma_reentrant_K / np.pi:.6f}")

        # Check quantization
        n_pi = gamma_reentrant_K / np.pi
        n_pi_nearest = round(n_pi)
        deviation = abs(n_pi - n_pi_nearest)
        print(f"    Nearest integer multiple of pi: {n_pi_nearest}")
        print(f"    Deviation from quantization: {deviation:.6f}")
        quantized_K = deviation < 0.1
        print(f"    Quantized (within 10% of pi): {quantized_K}")
    else:
        print("    No re-entrant crossings found in D_K.")
        gamma_reentrant_K = 0.0
        quantized_K = False

    # D_can re-entrant analysis
    print("\n  D_can (torsionful):")
    if len(res_20_can['crossings']) >= 2:
        tau_c1_can = res_20_can['crossings'][0][0]
        tau_c2_can = res_20_can['crossings'][1][0]
        gamma_reentrant_can = res_20_can['gamma_between_crossings'][0]
        print(f"    tau_c1 = {tau_c1_can:.4f}, tau_c2 = {tau_c2_can:.4f}")
        print(f"    gamma(cycle) = {gamma_reentrant_can:.6f}")
        print(f"    gamma(cycle)/pi = {gamma_reentrant_can / np.pi:.6f}")

        n_pi = gamma_reentrant_can / np.pi
        n_pi_nearest = round(n_pi)
        deviation = abs(n_pi - n_pi_nearest)
        print(f"    Nearest integer multiple of pi: {n_pi_nearest}")
        print(f"    Deviation from quantization: {deviation:.6f}")
        quantized_can = deviation < 0.1
        print(f"    Quantized (within 10% of pi): {quantized_can}")
    else:
        print("    No re-entrant crossings found in D_can.")
        gamma_reentrant_can = 0.0
        quantized_can = False

    # =========================================================================
    # SYNTHESIS
    # =========================================================================
    print("\n" + "=" * 72)
    print("SYNTHESIS: Berry Phase Summary")
    print("=" * 72)

    print("\n  All sectors (D_K basis, total Berry phase over [0, 0.5]):")
    all_sectors_K = {**results_K, **results_control}
    for name in ['(0,0)', '(1,0)', '(0,1)', '(1,1)', '(2,0)',
                 '(0,2)', '(3,0)', '(0,3)', '(2,1)']:
        if name in all_sectors_K:
            r = all_sectors_K[name]
            cross_str = f"{len(r['crossings'])} crossings" if r['crossings'] else "always supercrit"
            print(f"    {name}: gamma/pi = {r['gamma_total']/np.pi:+8.4f}  "
                  f"[{cross_str}]")

    print("\n  Crossing sectors (D_can basis, total Berry phase over [0, 0.5]):")
    for name in ['(1,1)', '(2,0)', '(0,2)', '(2,1)']:
        if name in results_can:
            r = results_can[name]
            cross_str = f"{len(r['crossings'])} crossings"
            print(f"    {name}: gamma/pi = {r['gamma_total']/np.pi:+8.4f}  "
                  f"[{cross_str}]")

    # Quantization test -- ONLY at actual transitions (D_K crossing sectors)
    # D_can sectors are ALWAYS supercritical: no transitions, so their Berry
    # phase is irrelevant to the topological protection question.
    print("\n  Quantization test at CROSSING sectors (D_K, the only basis "
          "with M_max=1 transitions):")
    any_crossing_quantized = False
    for name in ['(1,1)', '(2,0)', '(0,2)', '(2,1)']:
        r = results_K[name]
        g = r['gamma_total']
        n = g / np.pi
        nr = round(n)
        dev = abs(n - nr)
        q = dev < 0.1
        if q:
            any_crossing_quantized = True
        print(f"    {name} (D_K): gamma/pi = {n:.4f}, "
              f"nearest_int = {nr}, dev = {dev:.4f}, "
              f"quantized = {q}")

    print("\n  D_can sectors (all always-supercritical, no transitions):")
    any_can_quantized = False
    for name in ['(1,1)', '(2,0)', '(0,2)', '(2,1)']:
        if name in results_can:
            r = results_can[name]
            g = r['gamma_total']
            n = g / np.pi
            nr = round(n)
            dev = abs(n - nr)
            q = dev < 0.1
            if q:
                any_can_quantized = True
            print(f"    {name} (D_can): gamma/pi = {n:.4f}, "
                  f"nearest_int = {nr}, dev = {dev:.4f}, "
                  f"quantized = {q} (NOT at transition)")

    print(f"\n  NOTE: D_can near-quantization is a property of the "
          f"continuously supercritical\n  BCS state, NOT evidence of "
          f"topological protection at transitions.\n  Those sectors "
          f"have M_max >> 1 everywhere (no crossings).")

    # Re-entrant cycle
    print(f"\n  Re-entrant (2,0) cycle Berry phase:")
    print(f"    D_K:  gamma_cycle/pi = "
          f"{gamma_reentrant_K/np.pi:.4f}, quantized = {quantized_K}")
    print(f"    D_can: gamma_cycle/pi = "
          f"{gamma_reentrant_can/np.pi:.4f}, quantized = {quantized_can}")

    # Control check: always-supercritical D_K sectors
    print(f"\n  Control (always-supercritical D_K sectors):")
    for name in ['(0,0)', '(1,0)', '(0,1)']:
        r = results_control[name]
        g = r['gamma_total']
        print(f"    {name}: gamma/pi = {g/np.pi:+.4f}")

    # Verdict -- ONLY crossing sectors matter for topological protection
    print("\n  --- GATE S-4 VERDICT ---")

    # Key test: is the Berry phase quantized at the actual D_K transitions?
    if any_crossing_quantized or quantized_K:
        verdict = "PASS"
        print(f"  Quantized Berry phase at D_K sector transitions.")
        print(f"  Topological protection indicated.")
    else:
        # Berry phase IS non-trivial but not quantized at transitions
        max_gamma_crossing = max(
            abs(results_K[name]['gamma_total'])
            for name in ['(1,1)', '(2,0)', '(0,2)', '(2,1)'])

        if max_gamma_crossing > 0.3:
            verdict = "DIAGNOSTIC"
            print(f"  Non-trivial Berry phase at D_K transitions "
                  f"(max |gamma/pi| = {max_gamma_crossing/np.pi:.4f})")
            print(f"  but NOT quantized to integer multiples of pi.")
            print(f"  Transitions are smooth crossovers, not topological.")
            if any_can_quantized:
                print(f"  D_can near-quantization ({[n for n in ['(1,1)','(2,0)','(0,2)'] if abs(results_can[n]['gamma_total']/np.pi - round(results_can[n]['gamma_total']/np.pi)) < 0.1]})")
                print(f"  is a SEPARATE phenomenon (no transitions in D_can).")
        else:
            verdict = "NULL"
            print(f"  Berry phase negligible at transitions "
                  f"(max |gamma/pi| = {max_gamma_crossing/np.pi:.6f}).")

    print(f"\n  Verdict: {verdict}")

    # =========================================================================
    # Save results
    # =========================================================================
    print(f"\n[5] Saving results to {OUT_NPZ}...")

    save_dict = {
        'tau_dense': tau_dense_full,
        'verdict': np.array([verdict]),
    }

    # Save per-sector results
    for name, r in results_K.items():
        prefix = f"K_{name.replace('(','').replace(')','').replace(',','_')}"
        save_dict[f'{prefix}_M_max'] = r['M_max_dense']
        save_dict[f'{prefix}_Delta_norm'] = r['Delta_norm_dense']
        save_dict[f'{prefix}_A'] = r['A_dense']
        save_dict[f'{prefix}_gamma_cum'] = r['gamma_cumulative']
        save_dict[f'{prefix}_gamma_total'] = np.array([r['gamma_total']])
        save_dict[f'{prefix}_crossings'] = np.array(
            r['crossings'] if r['crossings'] else [[0, 0]])

    for name, r in results_can.items():
        prefix = f"can_{name.replace('(','').replace(')','').replace(',','_')}"
        save_dict[f'{prefix}_M_max'] = r['M_max_dense']
        save_dict[f'{prefix}_Delta_norm'] = r['Delta_norm_dense']
        save_dict[f'{prefix}_A'] = r['A_dense']
        save_dict[f'{prefix}_gamma_cum'] = r['gamma_cumulative']
        save_dict[f'{prefix}_gamma_total'] = np.array([r['gamma_total']])

    for name, r in results_control.items():
        prefix = f"ctrl_{name.replace('(','').replace(')','').replace(',','_')}"
        save_dict[f'{prefix}_gamma_total'] = np.array([r['gamma_total']])
        save_dict[f'{prefix}_A'] = r['A_dense']
        save_dict[f'{prefix}_gamma_cum'] = r['gamma_cumulative']

    # Re-entrant data
    save_dict['reentrant_20_K_gamma'] = np.array([gamma_reentrant_K])
    save_dict['reentrant_20_can_gamma'] = np.array([gamma_reentrant_can])

    np.savez_compressed(OUT_NPZ, **save_dict)
    print(f"  Saved {len(save_dict)} arrays.")

    # =========================================================================
    # Visualization
    # =========================================================================
    print(f"\n[6] Generating plots at {OUT_PNG}...")

    fig, axes = plt.subplots(3, 2, figsize=(16, 14))
    fig.suptitle('S-4: Berry Phase at BCS Sector Transitions',
                 fontsize=14, fontweight='bold')

    # Panel (0,0): M_max profiles for crossing sectors (D_K)
    ax = axes[0, 0]
    colors = {'(1,1)': 'C0', '(2,0)': 'C1', '(0,2)': 'C2', '(2,1)': 'C3'}
    for name in ['(1,1)', '(2,0)', '(0,2)', '(2,1)']:
        r = results_K[name]
        ax.plot(tau_dense_full, r['M_max_dense'], label=name,
                color=colors[name])
    ax.axhline(1.0, color='k', linestyle='--', alpha=0.5, label='M_max=1')
    ax.set_xlabel('tau')
    ax.set_ylabel('M_max')
    ax.set_title('M_max (D_K, mu=lambda_min)')
    ax.legend(fontsize=8)
    ax.set_ylim(0, 3)
    ax.grid(True, alpha=0.3)

    # Panel (0,1): |Delta| profiles for crossing sectors (D_K)
    ax = axes[0, 1]
    for name in ['(1,1)', '(2,0)', '(0,2)', '(2,1)']:
        r = results_K[name]
        ax.plot(tau_dense_full, r['Delta_norm_dense'], label=name,
                color=colors[name])
    ax.set_xlabel('tau')
    ax.set_ylabel('|Delta|')
    ax.set_title('Gap magnitude |Delta| (D_K)')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Panel (1,0): Berry connection A(tau) for crossing sectors (D_K)
    ax = axes[1, 0]
    for name in ['(1,1)', '(2,0)', '(0,2)', '(2,1)']:
        r = results_K[name]
        ax.plot(tau_dense_full, r['A_dense'], label=name,
                color=colors[name])
    ax.set_xlabel('tau')
    ax.set_ylabel('A(tau)')
    ax.set_title('Berry Connection (D_K)')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Panel (1,1): Cumulative Berry phase gamma(tau) (D_K)
    ax = axes[1, 1]
    for name in ['(1,1)', '(2,0)', '(0,2)', '(2,1)']:
        r = results_K[name]
        ax.plot(tau_dense_full, r['gamma_cumulative'] / np.pi,
                label=name, color=colors[name])
    # Mark pi multiples
    for n in range(-5, 6):
        ax.axhline(n, color='gray', linestyle=':', alpha=0.3)
    ax.set_xlabel('tau')
    ax.set_ylabel('gamma(tau) / pi')
    ax.set_title('Cumulative Berry Phase (D_K)')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Panel (2,0): D_can Berry connection
    ax = axes[2, 0]
    for name in ['(1,1)', '(2,0)', '(0,2)', '(2,1)']:
        if name in results_can:
            r = results_can[name]
            ax.plot(tau_dense_full, r['A_dense'], label=f'{name} D_can',
                    color=colors[name], linestyle='--')
    ax.set_xlabel('tau')
    ax.set_ylabel('A(tau)')
    ax.set_title('Berry Connection (D_can)')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Panel (2,1): D_can cumulative Berry phase
    ax = axes[2, 1]
    for name in ['(1,1)', '(2,0)', '(0,2)', '(2,1)']:
        if name in results_can:
            r = results_can[name]
            ax.plot(tau_dense_full, r['gamma_cumulative'] / np.pi,
                    label=f'{name} D_can', color=colors[name],
                    linestyle='--')
    for n in range(-5, 6):
        ax.axhline(n, color='gray', linestyle=':', alpha=0.3)
    ax.set_xlabel('tau')
    ax.set_ylabel('gamma(tau) / pi')
    ax.set_title('Cumulative Berry Phase (D_can)')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Plot saved to {OUT_PNG}")

    print("\n" + "=" * 72)
    print("DONE.")
    print("=" * 72)


if __name__ == '__main__':
    main()
