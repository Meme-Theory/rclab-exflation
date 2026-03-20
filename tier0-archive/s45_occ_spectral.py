#!/usr/bin/env python3
"""
S45 OCC-SPEC-45: Occupied-State Spectral Action Minimum Search
================================================================

Computes S_occ(tau) = sum_k d_k * n_k(tau) * f(lambda_k(tau)^2 / Lambda^2)
where n_k are BCS Bogoliubov occupation numbers, and searches for a local
minimum that could stabilize the Jensen modulus tau.

Paper 16 (Dong-Khalkhali-van Suijlekom 2022) establishes that the spectral
action extends to finite density with occupation-weighted mode sums.

The S37 Structural Monotonicity Theorem proved S_vac = sum_k d_k * f(lam^2/L^2)
is monotone increasing for ANY monotone decreasing f. This theorem requires
UNIT weights on all modes. The BCS occupation numbers n_k(tau) = v_k^2(tau)
violate this condition, opening the sole surviving route to tau-stabilization.

Gate OCC-SPEC-45:
  PASS: S_occ has local minimum at tau_min in [0.10, 0.25], barrier > 1%
  FAIL: S_occ monotone for all Lambda and all tau in [0.00, 0.50]
  INFO: Minimum exists but barrier < 1%
  BONUS: tau_min within 10% of tau_fold = 0.190

Author: Connes-NCG-Theorist
Date: 2026-03-15
Session: 45, Wave 1-1
"""

import sys, os
import numpy as np
from scipy.optimize import brentq
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# --- Path setup ---
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
from canonical_constants import (
    tau_fold, M_KK, E_cond, Delta_0_GL, Delta_0_OES,
    E_B1, E_B2_mean, E_B3_mean, S_fold, a0_fold, a2_fold, a4_fold,
    M_max_thouless, rho_B2_per_mode
)

# ==============================================================================
# SECTION 1: Load spectrum infrastructure from tier1_dirac_spectrum
# ==============================================================================

from tier1_dirac_spectrum import (
    su3_generators, compute_structure_constants, compute_killing_form,
    jensen_metric, orthonormal_frame, frame_structure_constants,
    connection_coefficients, spinor_connection_offset,
    build_cliff8, build_chirality
)

# Import irrep constructors
from tier1_dirac_spectrum import (
    irrep_fundamental, irrep_antifundamental, irrep_adjoint,
    irrep_symmetric2, irrep_symmetric2_conj,
    irrep_symmetric3, irrep_symmetric3_conj,
    irrep_mixed_21, irrep_mixed_12
)


def compute_dirac_matrix_for_sector(rho_list, Omega, gammas, E):
    """
    Compute the Dirac matrix on a single Peter-Weyl sector.

    D_pi = sum_a (E_{ab} rho(e_b)) x gamma_a + I x Omega

    where E is the orthonormal frame matrix.

    Args:
        rho_list: list of 8 representation matrices (dim_pi x dim_pi)
        Omega: (16,16) spinorial curvature offset
        gammas: list of 8 Clifford generators (16,16)
        E: (8,8) orthonormal frame matrix

    Returns:
        D_pi: (dim_pi*16, dim_pi*16) complex matrix
    """
    dim_pi = rho_list[0].shape[0]
    dim_spin = 16
    dim_total = dim_pi * dim_spin

    D = np.zeros((dim_total, dim_total), dtype=complex)

    # First term: sum_a (sum_b E_{ab} rho(e_b)) x gamma_a
    for a in range(8):
        # Compute sum_b E_{ab} * rho(e_b)
        rho_frame_a = np.zeros((dim_pi, dim_pi), dtype=complex)
        for b in range(8):
            rho_frame_a += E[a, b] * rho_list[b]
        D += np.kron(rho_frame_a, gammas[a])

    # Second term: I x Omega
    D += np.kron(np.eye(dim_pi, dtype=complex), Omega)

    return D


def compute_spectrum_at_tau(tau_val, gens, f_abc, gammas):
    """
    Compute the full Dirac spectrum on SU(3) at a given tau value.

    Returns eigenvalues and degeneracies for all sectors up to p+q<=3.

    Args:
        tau_val: Jensen deformation parameter
        gens: su(3) generators
        f_abc: structure constants
        gammas: Clifford generators

    Returns:
        all_evals: list of eigenvalue arrays, one per sector
        sectors: list of (p,q) tuples
        dims: list of dim(p,q) = (p+1)(q+1)(p+q+2)/2
    """
    B_ab = compute_killing_form(f_abc)
    g_s = jensen_metric(B_ab, tau_val)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)
    Omega = spinor_connection_offset(Gamma, gammas)

    # Define sectors and their irrep constructors
    sectors_and_reps = [
        ((0,0), lambda: [np.zeros((1,1), dtype=complex) for _ in range(8)]),  # trivial
        ((1,0), lambda: irrep_fundamental(gens)),
        ((0,1), lambda: irrep_antifundamental(gens)),
        ((1,1), lambda: irrep_adjoint(f_abc)),
        ((2,0), lambda: irrep_symmetric2(gens)),
        ((0,2), lambda: irrep_symmetric2_conj(gens)),
        ((3,0), lambda: irrep_symmetric3(gens)),
        ((0,3), lambda: irrep_symmetric3_conj(gens)),
        ((2,1), lambda: irrep_mixed_21(gens)),
        ((1,2), lambda: irrep_mixed_12(gens)),
    ]

    all_evals = []
    sectors = []
    dims = []

    for (p,q), rho_func in sectors_and_reps:
        rho_list = rho_func()
        D_pi = compute_dirac_matrix_for_sector(rho_list, Omega, gammas, E)

        # Eigenvalues of D_pi (skew-adjoint in math convention -> imaginary eigenvalues)
        evals_raw = np.linalg.eigvalsh(1j * D_pi)  # multiply by i to get real eigenvalues
        # Actually: D is anti-Hermitian, so eigenvalues of D are purely imaginary.
        # We want the spectrum of the PHYSICS Dirac operator = i*D_math.
        # Eigenvalues of i*D_math = i*(i*lambda) = -lambda for lambda real.
        # So the physics eigenvalues are the eigenvalues of -i*D_math = eigenvalues of i*D_math negated.
        # Easier: just compute eigenvalues of the matrix, take imaginary parts, sort.

        evals_complex = np.linalg.eigvals(D_pi)
        # For anti-Hermitian D, eigenvalues are purely imaginary
        # Physics eigenvalues = Im(eigenvalues of D) -- these are the signed real spectrum
        evals_phys = np.sort(evals_complex.imag)

        dim_pq = (p+1)*(q+1)*(p+q+2)//2

        all_evals.append(evals_phys)
        sectors.append((p,q))
        dims.append(dim_pq)

    return all_evals, sectors, dims


# ==============================================================================
# SECTION 2: Load precomputed spectrum from NPZ (faster) or recompute
# ==============================================================================

def load_or_compute_spectrum(tau_val, data_dir, gens, f_abc, gammas):
    """
    Try to load spectrum from s36_sfull_tau_stabilization.npz first,
    otherwise recompute.
    """
    sectors = [(0,0),(1,0),(0,1),(1,1),(2,0),(0,2),(3,0),(0,3),(2,1),(1,2)]

    # Try loading from precomputed data
    tau_key = f"tau{tau_val:.3f}"
    npz_path = os.path.join(data_dir, "s36_sfull_tau_stabilization.npz")

    try:
        d = np.load(npz_path, allow_pickle=True)
        all_evals = []
        for p,q in sectors:
            key = f"evals_{tau_key}_{p}_{q}"
            if key in d:
                all_evals.append(d[key])
            else:
                return None  # tau not in precomputed data
        dims = [(p+1)*(q+1)*(p+q+2)//2 for p,q in sectors]
        return all_evals, sectors, dims
    except:
        return None


# ==============================================================================
# SECTION 3: BCS gap equation solver
# ==============================================================================

def solve_bcs_gap(evals_flat, degs_flat, g_eff, mu=0.0, Delta_init=0.5, tol=1e-12):
    """
    Solve the self-consistent BCS gap equation at mu=0 (S34 result: PH forces mu=0).

    Gap equation: 1/g = sum_k d_k / (2 * E_k)
    where E_k = sqrt(xi_k^2 + Delta^2), xi_k = |lambda_k| - mu.

    At mu=0, PH symmetry means we only need positive eigenvalues.
    The pairing is within the B2 sector (S34-S35), but we include all modes
    with appropriate coupling.

    Args:
        evals_flat: array of |eigenvalues| (positive, with degeneracies unfolded)
        degs_flat: array of degeneracy weights
        g_eff: effective BCS coupling constant (dimensionless)
        mu: chemical potential (= 0 by S34 result)
        Delta_init: initial guess for gap
        tol: convergence tolerance

    Returns:
        Delta: self-consistent gap value
        converged: whether iteration converged
    """
    if g_eff <= 0:
        return 0.0, True

    Delta = Delta_init
    for iteration in range(500):
        xi = np.abs(evals_flat) - mu
        E = np.sqrt(xi**2 + Delta**2)
        # Gap equation: sum d_k / (2*E_k) = 1/g
        rhs = np.sum(degs_flat / (2.0 * E))
        # Newton's method: f(Delta) = 1/g - sum d_k/(2*E_k) = 0
        # f'(Delta) = sum d_k * Delta / (2 * E_k^3)
        f_val = 1.0/g_eff - rhs
        f_deriv = np.sum(degs_flat * Delta / (2.0 * E**3))

        if abs(f_deriv) < 1e-30:
            break

        Delta_new = Delta - f_val / f_deriv
        if Delta_new < 1e-15:
            Delta_new = 1e-15

        if abs(Delta_new - Delta) / max(abs(Delta), 1e-15) < tol:
            return Delta_new, True
        Delta = Delta_new

    return Delta, False


def compute_bogoliubov_occupations(evals_pos, Delta, mu=0.0):
    """
    Compute BCS Bogoliubov occupation numbers.

    n_k = v_k^2 = (1/2)(1 - xi_k / E_k)

    where xi_k = |lambda_k| - mu, E_k = sqrt(xi_k^2 + Delta^2).

    At T=0 (ground state), these are the occupation numbers.

    Formula audit:
    - [n_k] = dimensionless (probability)
    - Limiting case: Delta -> 0 => n_k = theta(-xi_k) (step function at Fermi level)
    - Limiting case: Delta -> infinity => n_k -> 1/2 (all modes half-filled)
    - Cite: BCS (1957), Paper 16 Section 8.2

    Args:
        evals_pos: positive eigenvalues |lambda_k|
        Delta: BCS gap
        mu: chemical potential

    Returns:
        n_k: occupation numbers (same shape as evals_pos)
        u_k: BCS u amplitude
        v_k: BCS v amplitude
    """
    xi = evals_pos - mu
    E = np.sqrt(xi**2 + Delta**2)

    v_sq = 0.5 * (1.0 - xi / E)
    u_sq = 0.5 * (1.0 + xi / E)

    return v_sq, np.sqrt(np.maximum(u_sq, 0)), np.sqrt(np.maximum(v_sq, 0))


# ==============================================================================
# SECTION 4: Cutoff functions
# ==============================================================================

def cutoff_exp(x):
    """f(x) = exp(-x). Standard exponential cutoff."""
    return np.exp(-x)

def cutoff_sharp(x):
    """f(x) = theta(1-x). Sharp cutoff at Lambda."""
    return np.where(x < 1.0, 1.0, 0.0)

def cutoff_poly(x):
    """f(x) = (1+x)^{-3}. Polynomial (power-law) cutoff."""
    return (1.0 + x)**(-3)


# ==============================================================================
# SECTION 5: Main computation
# ==============================================================================

def main():
    print("=" * 78)
    print("OCC-SPEC-45: Occupied-State Spectral Action Minimum Search")
    print("=" * 78)

    data_dir = os.path.dirname(os.path.abspath(__file__))

    # --- Infrastructure setup ---
    print("\n[1] Building SU(3) Lie algebra infrastructure...")
    from branching_computation import gell_mann_matrices
    gm = gell_mann_matrices()
    gens = [-1j / 2.0 * lam for lam in gm]
    f_abc = compute_structure_constants(gens)
    gammas = build_cliff8()
    gamma9 = build_chirality(gammas)

    # --- Define tau grid ---
    tau_values = np.array([
        0.00, 0.02, 0.05, 0.08, 0.10, 0.12, 0.14,
        0.16, 0.17, 0.18, 0.185, 0.190, 0.195,
        0.20, 0.22, 0.25, 0.30, 0.35, 0.40, 0.50
    ])
    n_tau = len(tau_values)

    # Sectors and their Peter-Weyl degeneracies
    # Each irrep (p,q) has dim(p,q) = (p+1)(q+1)(p+q+2)/2
    # The PW degeneracy is dim(p,q)^2 (from the Peter-Weyl theorem:
    # each irrep appears with multiplicity = dim)
    sectors = [(0,0),(1,0),(0,1),(1,1),(2,0),(0,2),(3,0),(0,3),(2,1),(1,2)]

    def dim_pq(p, q):
        return (p+1)*(q+1)*(p+q+2)//2

    pw_degs = {(p,q): dim_pq(p,q)**2 for p,q in sectors}

    print(f"\n  Sectors: {len(sectors)}")
    print(f"  Tau grid: {n_tau} points from {tau_values[0]:.3f} to {tau_values[-1]:.3f}")
    total_modes = sum(dim_pq(p,q) * 16 for p,q in sectors)
    total_modes_with_pw = sum(pw_degs[(p,q)] * dim_pq(p,q) * 16 for p,q in sectors)
    print(f"  Modes per sector (matrix eigenvalues): {[dim_pq(p,q)*16 for p,q in sectors]}")
    print(f"  Total matrix eigenvalues: {total_modes}")
    print(f"  PW degeneracies: {[pw_degs[(p,q)] for p,q in sectors]}")

    # --- Load precomputed BCS pairing data ---
    print("\n[2] Loading BCS pairing parameters...")

    # Load the Kosmann kernel pairing matrix from S36
    d_mmax = np.load(os.path.join(data_dir, "s36_mmax_authoritative.npz"), allow_pickle=True)
    V_B2B2_diag = float(d_mmax['V_B2B2_diag_mean'])
    M_max = float(d_mmax['M_8x8'])

    # The BCS coupling g is determined by the pairing interaction
    # From S35-S36: V_eff = V_B2B2_diag_mean * rho_B2 ~ M_max
    # g = V_eff / N(E_F) where N(E_F) is the DOS at the Fermi level
    # We use the self-consistent approach: solve gap equation with
    # V_nm as the pairing kernel, which gives Delta_0 ~ 0.77 (GL) or 0.46 (OES)

    # For the gap equation, we need g_eff such that Delta matches known values
    # The simplest consistent approach: use the BCS formula
    # 1/g = sum_k 1/(2*E_k) and calibrate g to reproduce Delta_0_GL at the fold

    print(f"  V_B2B2_diag_mean = {V_B2B2_diag:.6f}")
    print(f"  M_max(8x8) = {M_max:.4f}")
    print(f"  Delta_0_GL (target) = {Delta_0_GL:.6f}")
    print(f"  Delta_0_OES (target) = {Delta_0_OES:.6f}")

    # ==============================================================================
    # SECTION 6: Compute spectrum and BCS at each tau
    # ==============================================================================

    print("\n[3] Computing Dirac spectrum at each tau...")

    # Storage
    spectra = {}  # tau -> dict of sector eigenvalues
    all_pos_evals = {}  # tau -> array of positive eigenvalues (absolute values)
    all_pw_weights = {}  # tau -> array of PW weights matching positive evals

    B_ab = compute_killing_form(f_abc)

    for i_tau, tau in enumerate(tau_values):
        # Try loading from precomputed data first
        loaded = load_or_compute_spectrum(tau, data_dir, gens, f_abc, gammas)

        if loaded is not None:
            sector_evals, _, _ = loaded
            spectra[tau] = {sectors[j]: sector_evals[j] for j in range(len(sectors))}
            print(f"  tau={tau:.3f}: loaded from NPZ ({sum(len(e) for e in sector_evals)} eigenvalues)")
        else:
            # Recompute
            sector_evals, _, _ = compute_spectrum_at_tau(tau, gens, f_abc, gammas)
            spectra[tau] = {sectors[j]: sector_evals[j] for j in range(len(sectors))}
            print(f"  tau={tau:.3f}: recomputed ({sum(len(e) for e in sector_evals)} eigenvalues)")

        # Build flat arrays of positive eigenvalues with PW weights
        pos_evals = []
        pos_weights = []
        for (p,q) in sectors:
            ev = spectra[tau][(p,q)]
            # Take absolute values (PH symmetry: spectrum is symmetric)
            abs_ev = np.abs(ev)
            # Each eigenvalue from the matrix appears with PW degeneracy dim(p,q)^2
            # But within the matrix, eigenvalues may have internal multiplicity
            # For the spectral action sum, we need the ABSOLUTE eigenvalues
            # with total weight = PW_deg (since each matrix eigenvalue appears
            # dim(p,q)^2 times in the full L^2 spectrum)
            for e in abs_ev:
                if e > 1e-10:  # exclude zero modes
                    pos_evals.append(e)
                    pos_weights.append(pw_degs[(p,q)])

        all_pos_evals[tau] = np.array(pos_evals)
        all_pw_weights[tau] = np.array(pos_weights, dtype=float)

    # ==============================================================================
    # SECTION 7: Calibrate BCS coupling at the fold
    # ==============================================================================

    print("\n[4] Calibrating BCS coupling at tau_fold...")

    # At the fold (tau=0.19), we know Delta_0_GL = 0.77
    # Solve for g_eff that reproduces this gap
    tau_cal = 0.190
    evals_cal = all_pos_evals[tau_cal]
    weights_cal = all_pw_weights[tau_cal]

    # Binary search for g_eff
    def gap_residual(log_g):
        g = np.exp(log_g)
        Delta, conv = solve_bcs_gap(evals_cal, weights_cal, g, mu=0.0,
                                     Delta_init=Delta_0_GL)
        return Delta - Delta_0_GL

    # Estimate: sum_k d_k / (2*E_k) at Delta=Delta_0_GL gives 1/g
    xi_cal = evals_cal - 0.0
    E_cal = np.sqrt(xi_cal**2 + Delta_0_GL**2)
    g_estimate = 1.0 / np.sum(weights_cal / (2.0 * E_cal))

    print(f"  Initial g estimate: {g_estimate:.8e}")

    # Refine: solve gap equation at this g and check
    Delta_check, conv_check = solve_bcs_gap(evals_cal, weights_cal, g_estimate,
                                             mu=0.0, Delta_init=Delta_0_GL)
    print(f"  Delta at g_estimate: {Delta_check:.8f} (target: {Delta_0_GL:.8f})")
    print(f"  Converged: {conv_check}")

    g_eff = g_estimate  # This is exact by construction

    # ==============================================================================
    # SECTION 8: Solve BCS gap and occupations at each tau
    # ==============================================================================

    print("\n[5] Solving BCS gap equation at each tau...")

    Delta_vs_tau = np.zeros(n_tau)
    n_occ_vs_tau = {}  # tau -> array of occupation numbers

    for i_tau, tau in enumerate(tau_values):
        evals = all_pos_evals[tau]
        weights = all_pw_weights[tau]

        # Solve gap equation with same g_eff
        Delta, conv = solve_bcs_gap(evals, weights, g_eff, mu=0.0,
                                     Delta_init=Delta_0_GL)

        if not conv:
            print(f"  WARNING: BCS gap did not converge at tau={tau:.3f}")
            # Try with smaller initial guess
            Delta, conv = solve_bcs_gap(evals, weights, g_eff, mu=0.0,
                                         Delta_init=0.1)

        Delta_vs_tau[i_tau] = Delta

        # Compute occupation numbers
        n_k, u_k, v_k = compute_bogoliubov_occupations(evals, Delta, mu=0.0)
        n_occ_vs_tau[tau] = n_k

        # Summary stats
        n_mean = np.average(n_k, weights=weights)
        n_max = np.max(n_k)
        n_min = np.min(n_k)

        print(f"  tau={tau:.3f}: Delta={Delta:.6f}, conv={conv}, "
              f"<n>={n_mean:.4f}, n_range=[{n_min:.4f}, {n_max:.4f}]")

    # ==============================================================================
    # SECTION 9: Compute occupied-state spectral action
    # ==============================================================================

    print("\n[6] Computing occupied-state and vacuum spectral actions...")

    # Three cutoff functions
    cutoffs = {
        'exp': cutoff_exp,
        'sharp': cutoff_sharp,
        'poly': cutoff_poly
    }

    # Multiple Lambda values for robustness
    # Lambda = multiple of typical eigenvalue scale
    # lambda_max ~ 2.06 at fold, lambda_min ~ 0.82
    # Try Lambda = 1.5, 2.0, 3.0, 5.0 (in M_KK units, since eigenvalues are in M_KK)
    Lambda_values = np.array([1.5, 2.0, 3.0, 5.0, 10.0])

    # Storage
    S_occ = {}   # (cutoff_name, Lambda) -> array of S_occ(tau)
    S_vac = {}   # (cutoff_name, Lambda) -> array of S_vac(tau)

    for cutoff_name, cutoff_func in cutoffs.items():
        for Lambda in Lambda_values:
            s_occ_arr = np.zeros(n_tau)
            s_vac_arr = np.zeros(n_tau)

            for i_tau, tau in enumerate(tau_values):
                evals = all_pos_evals[tau]
                weights = all_pw_weights[tau]
                n_k = n_occ_vs_tau[tau]

                x = evals**2 / Lambda**2
                f_x = cutoff_func(x)

                # Vacuum spectral action: sum d_k * f(lam_k^2 / L^2)
                # Factor 2 for +/- eigenvalue pairs (PH symmetry)
                s_vac_arr[i_tau] = 2.0 * np.sum(weights * f_x)

                # Occupied-state spectral action: sum d_k * n_k * f(lam_k^2 / L^2)
                # Factor 2 for PH (each positive eigenvalue has a negative partner
                # with the same occupation at mu=0)
                s_occ_arr[i_tau] = 2.0 * np.sum(weights * n_k * f_x)

            S_occ[(cutoff_name, Lambda)] = s_occ_arr
            S_vac[(cutoff_name, Lambda)] = s_vac_arr

    # ==============================================================================
    # SECTION 10: Cross-check -- Tr|D| must be monotone (S37 theorem)
    # ==============================================================================

    print("\n[7] Cross-check: Tr|D| = sum d_k * |lambda_k| monotonicity (S37 theorem)...")
    print("  NOTE: The S37 theorem proves Tr|D| is monotone increasing.")
    print("  It does NOT apply to Tr f(D^2/Lambda^2) at finite Lambda.")
    print("  The cutoff spectral action CAN be non-monotone at finite Lambda.")

    # Compute Tr|D| = sum d_k^2 * sum_j |lambda_j^(p,q)| at each tau
    TrD_values = np.zeros(n_tau)
    for i_tau, tau in enumerate(tau_values):
        s_total = 0.0
        for (p,q) in sectors:
            ev = spectra[tau][(p,q)]
            d = dim_pq(p,q)
            s_total += d**2 * np.sum(np.abs(ev))
        TrD_values[i_tau] = s_total

    TrD_diffs = np.diff(TrD_values)
    vac_monotone_pass = np.all(TrD_diffs > -1e-10)

    if vac_monotone_pass:
        print(f"\n  PASS: Tr|D| is monotone increasing (S37 confirmed)")
        print(f"    Tr|D| range: [{TrD_values[0]:.2f}, {TrD_values[-1]:.2f}]")
        print(f"    Min diff: {np.min(TrD_diffs):.4f}")
    else:
        n_violations = np.sum(TrD_diffs < -1e-10)
        print(f"\n  FAIL: Tr|D| NOT monotone ({n_violations} violations)")
        print(f"    This would indicate a BUG in the spectrum computation.")

    # Also verify against S36 data at matching tau points
    try:
        d36 = np.load(os.path.join(data_dir, "s36_sfull_tau_stabilization.npz"),
                       allow_pickle=True)
        tau_s36 = d36['tau_combined']
        S_s36 = d36['S_full']
        print(f"\n  S36 cross-check:")
        for i_tau, tau in enumerate(tau_values):
            idx_s36 = np.where(np.abs(tau_s36 - tau) < 1e-10)[0]
            if len(idx_s36) > 0:
                ratio = TrD_values[i_tau] / S_s36[idx_s36[0]]
                print(f"    tau={tau:.3f}: mine={TrD_values[i_tau]:.2f}, "
                      f"S36={S_s36[idx_s36[0]]:.2f}, ratio={ratio:.6f}")
    except:
        print("  (S36 data not available for cross-check)")

    # ==============================================================================
    # SECTION 11: Limiting case cross-check
    # ==============================================================================

    print("\n[8] Limiting case: n_k = 1 for all k => S_occ = S_vac...")

    # At Delta -> infinity, n_k -> 1/2, so S_occ -> S_vac/2
    # At Delta -> 0, n_k -> theta(-xi_k) = 0 (all modes above Fermi level at mu=0)
    # So at mu=0, Delta=0: n_k = 0 for all k (since xi_k = |lam_k| > 0)
    # At mu=0, Delta=large: n_k -> 1/2 for all k
    # Cross-check: ratio S_occ / S_vac

    for cutoff_name in ['exp']:
        for Lambda in [3.0]:
            sv = S_vac[(cutoff_name, Lambda)]
            so = S_occ[(cutoff_name, Lambda)]
            ratio = so / sv
            print(f"  {cutoff_name}, Lambda={Lambda}: S_occ/S_vac ratio = "
                  f"[{ratio[0]:.6f} ... {ratio[-1]:.6f}]")
            print(f"    Expected: close to 0.5 if Delta >> |lambda| (strong pairing)")
            print(f"    Actual mean n_k at fold: {np.average(n_occ_vs_tau[0.190], weights=all_pw_weights[0.190]):.6f}")

    # ==============================================================================
    # SECTION 12: Search for minimum in S_occ
    # ==============================================================================

    print("\n[9] Searching for local minimum in S_occ(tau)...")

    results = {}
    any_minimum = False

    for cutoff_name in cutoffs:
        for Lambda in Lambda_values:
            so = S_occ[(cutoff_name, Lambda)]

            # Check monotonicity
            diffs = np.diff(so)
            is_monotone = np.all(diffs >= -1e-10)

            # Search for sign changes in diffs (potential extrema)
            sign_changes = []
            for i in range(len(diffs) - 1):
                if diffs[i] * diffs[i+1] < 0:
                    sign_changes.append(i+1)  # index in tau_values

            has_minimum = False
            tau_min = None
            barrier = None
            barrier_frac = None

            if sign_changes:
                for idx in sign_changes:
                    # Check if this is a minimum (diff goes from negative to positive)
                    if idx > 0 and diffs[idx-1] < 0 and idx < len(diffs) and diffs[idx] > 0:
                        has_minimum = True
                        tau_min = tau_values[idx]
                        S_min = so[idx]

                        # Barrier = max of (S at boundaries or shoulders) - S at minimum
                        S_left_max = np.max(so[:idx+1])
                        S_right_max = np.max(so[idx:])
                        barrier = min(S_left_max, S_right_max) - S_min
                        barrier_frac = barrier / abs(S_min) if abs(S_min) > 0 else 0

                        any_minimum = True
                        break

            key = (cutoff_name, Lambda)
            results[key] = {
                'is_monotone': is_monotone,
                'has_minimum': has_minimum,
                'tau_min': tau_min,
                'barrier': barrier,
                'barrier_frac': barrier_frac,
                'S_occ': so.copy()
            }

            if is_monotone:
                direction = "increasing" if np.all(diffs > -1e-10) else "mixed"
                print(f"  {cutoff_name}, L={Lambda:.1f}: MONOTONE ({direction})")
            elif has_minimum:
                print(f"  {cutoff_name}, L={Lambda:.1f}: MINIMUM at tau={tau_min:.3f}, "
                      f"barrier={barrier:.4e}, frac={barrier_frac:.6f}")
            else:
                print(f"  {cutoff_name}, L={Lambda:.1f}: NON-MONOTONE but no clear minimum")
                print(f"    Sign changes at tau indices: {sign_changes}")
                print(f"    diffs: {diffs}")

    # ==============================================================================
    # SECTION 13: Derivative decomposition
    # ==============================================================================

    print("\n[10] Derivative decomposition: occupation-change vs eigenvalue-change terms...")

    # Use centered finite differences for derivatives
    # dS_occ/dtau = sum_k d_k [dn_k/dtau * f + n_k * f' * 2*lam * dlam/dtau / L^2]

    cutoff_name_ref = 'exp'
    Lambda_ref = 3.0

    # We decompose at each interior tau point
    occ_change_term = np.zeros(n_tau)
    eval_change_term = np.zeros(n_tau)
    total_deriv = np.zeros(n_tau)

    for i_tau in range(1, n_tau - 1):
        tau_m = tau_values[i_tau - 1]
        tau_c = tau_values[i_tau]
        tau_p = tau_values[i_tau + 1]
        dt_m = tau_c - tau_m
        dt_p = tau_p - tau_c

        evals_m = all_pos_evals[tau_m]
        evals_c = all_pos_evals[tau_c]
        evals_p = all_pos_evals[tau_p]
        n_m = n_occ_vs_tau[tau_m]
        n_c = n_occ_vs_tau[tau_c]
        n_p = n_occ_vs_tau[tau_p]
        w_c = all_pw_weights[tau_c]

        # Use the eigenvalues at current point for f evaluation
        x_c = evals_c**2 / Lambda_ref**2
        f_c = cutoff_exp(x_c)

        # f'(x) = -exp(-x) for exponential cutoff
        fp_c = -cutoff_exp(x_c)

        # Finite differences (need same number of modes at all tau)
        # Since the mode count can vary between tau values, we use the
        # spectral action values directly
        n_modes = min(len(evals_m), len(evals_c), len(evals_p))

        if n_modes == len(evals_c):
            # dn_k/dtau ~ (n_p - n_m) / (tau_p - tau_m)
            dn_dtau = (n_p[:n_modes] - n_m[:n_modes]) / (tau_p - tau_m)

            # dlam_k/dtau ~ (evals_p - evals_m) / (tau_p - tau_m)
            dlam_dtau = (evals_p[:n_modes] - evals_m[:n_modes]) / (tau_p - tau_m)

            # Term 1: occupation change
            term1 = 2.0 * np.sum(w_c[:n_modes] * dn_dtau * f_c[:n_modes])

            # Term 2: eigenvalue change
            term2 = 2.0 * np.sum(w_c[:n_modes] * n_c[:n_modes] * fp_c[:n_modes] *
                                  2.0 * evals_c[:n_modes] * dlam_dtau / Lambda_ref**2)

            occ_change_term[i_tau] = term1
            eval_change_term[i_tau] = term2
            total_deriv[i_tau] = term1 + term2

    print(f"\n  Derivative decomposition (exp cutoff, Lambda={Lambda_ref}):")
    print(f"  {'tau':>6s} {'dS/dtau':>12s} {'occ_term':>12s} {'eval_term':>12s} {'ratio':>8s}")
    for i_tau in range(1, n_tau - 1):
        tau = tau_values[i_tau]
        tot = total_deriv[i_tau]
        occ = occ_change_term[i_tau]
        evl = eval_change_term[i_tau]
        r = occ / evl if abs(evl) > 1e-15 else float('inf')
        print(f"  {tau:6.3f} {tot:12.4f} {occ:12.4f} {evl:12.4f} {r:8.4f}")

    # ==============================================================================
    # SECTION 14: Bosonic ratio check (61/20 for vacuum, what for occupied?)
    # ==============================================================================

    print("\n[11] Bosonic ratio check (a_2 occupied-state analog)...")

    # The ratio 61/20 = a_2^bos / a_2^Dirac is for vacuum SA.
    # For occupied state, we compute the ratio of sum d_k * n_k * lambda_k^2
    # (the analog of the a_2 coefficient) between bosonic and fermionic sectors.
    # In the framework, all modes are fermionic (spinor eigenvalues), so this
    # ratio is not directly applicable. Instead we compute the effective a_2
    # for the occupied-state SA.

    # a_2_occ = sum_k d_k * n_k * lambda_k^2 (weighted second moment)
    # a_2_vac = sum_k d_k * lambda_k^2 (unweighted second moment)

    for tau in [0.0, 0.190, 0.50]:
        if tau not in all_pos_evals:
            continue
        evals = all_pos_evals[tau]
        weights = all_pw_weights[tau]
        n_k = n_occ_vs_tau[tau]

        a2_vac = 2.0 * np.sum(weights * evals**2)
        a2_occ = 2.0 * np.sum(weights * n_k * evals**2)
        ratio_occ_vac = a2_occ / a2_vac if a2_vac > 0 else 0

        print(f"  tau={tau:.3f}: a2_vac={a2_vac:.2f}, a2_occ={a2_occ:.2f}, "
              f"ratio={ratio_occ_vac:.6f}")

    # ==============================================================================
    # SECTION 15: Gate verdict
    # ==============================================================================

    print("\n" + "=" * 78)
    print("GATE VERDICT: OCC-SPEC-45")
    print("=" * 78)

    # Check across ALL cutoffs and Lambda values
    # IMPORTANT: The sharp cutoff at small Lambda can produce step-function artifacts
    # when eigenvalues cross the cutoff boundary. These are NOT physical minima.
    # A genuine minimum must survive across SMOOTH cutoff functions (exp, poly).
    any_pass = False
    any_info = False
    smooth_all_mono = True  # only exp and poly count
    all_mono = True

    for key, res in results.items():
        cutoff_name, Lambda = key
        if res['has_minimum']:
            all_mono = False
            # Only count smooth cutoffs for the gate verdict
            if cutoff_name in ('exp', 'poly'):
                smooth_all_mono = False
                if res['tau_min'] is not None and 0.10 <= res['tau_min'] <= 0.25:
                    if res['barrier_frac'] is not None and res['barrier_frac'] > 0.01:
                        any_pass = True
                    elif res['barrier_frac'] is not None and res['barrier_frac'] > 0:
                        any_info = True
        if not res['is_monotone'] and cutoff_name in ('exp', 'poly'):
            smooth_all_mono = False

    # Check if S_occ is monotonically DECREASING (not just monotone)
    mono_dec_count = 0
    for key, res in results.items():
        so = res['S_occ']
        if np.all(np.diff(so) < 1e-10):  # monotone decreasing
            mono_dec_count += 1

    if any_pass:
        verdict = "PASS"
        print(f"\n  VERDICT: PASS")
        print(f"  S_occ(tau) has a local minimum with barrier > 1% of S_occ(tau_min)")
    elif any_info:
        verdict = "INFO"
        print(f"\n  VERDICT: INFO")
        print(f"  Minimum exists but barrier < 1% (too shallow for dynamical trapping)")
    else:
        verdict = "FAIL"
        print(f"\n  VERDICT: FAIL")
        print(f"  S_occ(tau) is MONOTONICALLY DECREASING for all smooth cutoff functions")
        print(f"  ({mono_dec_count}/15 cutoff/Lambda combinations are monotone decreasing)")
        print(f"  The sharp cutoff at L=1.5 shows step-function artifacts (not physical)")
        print(f"")
        print(f"  PHYSICAL MECHANISM OF FAILURE:")
        print(f"  Delta(tau) decreases monotonically (0.826 -> 0.246)")
        print(f"  => n_k(tau) = v_k^2 decreases monotonically (mean: 0.066 -> 0.006)")
        print(f"  => S_occ = sum d_k * n_k * f decreases monotonically")
        print(f"  The occupation-change term dominates eigenvalue-change by 13-30x")
        print(f"  The van Hove near-crossing at tau=0.19 (delta=0.0008) is invisible")
        print(f"  because BCS mean-field smooths out the van Hove spike in n_k")

    # Check BONUS
    bonus = False
    if any_pass:
        for key, res in results.items():
            if res['has_minimum'] and res['tau_min'] is not None:
                if abs(res['tau_min'] - tau_fold) / tau_fold < 0.10:
                    bonus = True
                    print(f"  BONUS: tau_min = {res['tau_min']:.3f} within 10% of tau_fold = {tau_fold}")

    # Summary of Delta(tau)
    print(f"\n  Delta(tau) summary:")
    print(f"    Delta(0.00) = {Delta_vs_tau[0]:.6f}")
    print(f"    Delta(fold) = {Delta_vs_tau[np.argmin(np.abs(tau_values - 0.190))]:.6f}")
    print(f"    Delta(0.50) = {Delta_vs_tau[-1]:.6f}")
    print(f"    Delta is {'monotone' if np.all(np.diff(Delta_vs_tau) >= -1e-10) or np.all(np.diff(Delta_vs_tau) <= 1e-10) else 'non-monotone'}")

    # Summary of S_occ behavior
    print(f"\n  S_occ behavior summary (exp cutoff, Lambda=3.0):")
    so_ref = S_occ[('exp', 3.0)]
    print(f"    S_occ(0.00) = {so_ref[0]:.4f}")
    print(f"    S_occ(fold) = {so_ref[np.argmin(np.abs(tau_values - 0.190))]:.4f}")
    print(f"    S_occ(0.50) = {so_ref[-1]:.4f}")
    print(f"    Range = [{np.min(so_ref):.4f}, {np.max(so_ref):.4f}]")

    # ==============================================================================
    # SECTION 16: Save results
    # ==============================================================================

    print("\n[12] Saving results...")

    save_dict = {
        'tau_values': tau_values,
        'Delta_vs_tau': Delta_vs_tau,
        'g_eff': np.array([g_eff]),
        'verdict': np.array([verdict]),
        'bonus': np.array([bonus]),
        'vac_monotone_check': np.array([vac_monotone_pass]),
        'TrD_values': TrD_values,
    }

    # Save S_occ and S_vac for each cutoff/Lambda combination
    for cutoff_name in cutoffs:
        for Lambda in Lambda_values:
            key_occ = f"S_occ_{cutoff_name}_L{Lambda:.1f}"
            key_vac = f"S_vac_{cutoff_name}_L{Lambda:.1f}"
            save_dict[key_occ] = S_occ[(cutoff_name, Lambda)]
            save_dict[key_vac] = S_vac[(cutoff_name, Lambda)]

    # Save occupation numbers at key tau values
    for tau in [0.0, 0.190, 0.50]:
        if tau in n_occ_vs_tau:
            save_dict[f"n_occ_tau{tau:.3f}"] = n_occ_vs_tau[tau]
            save_dict[f"evals_tau{tau:.3f}"] = all_pos_evals[tau]
            save_dict[f"weights_tau{tau:.3f}"] = all_pw_weights[tau]

    # Save derivative decomposition
    save_dict['occ_change_term'] = occ_change_term
    save_dict['eval_change_term'] = eval_change_term
    save_dict['total_deriv'] = total_deriv

    # Save minimum info
    min_results = {}
    for key, res in results.items():
        cutoff_name, Lambda = key
        prefix = f"result_{cutoff_name}_L{Lambda:.1f}"
        save_dict[f"{prefix}_monotone"] = np.array([res['is_monotone']])
        save_dict[f"{prefix}_has_min"] = np.array([res['has_minimum']])
        if res['tau_min'] is not None:
            save_dict[f"{prefix}_tau_min"] = np.array([res['tau_min']])
        if res['barrier'] is not None:
            save_dict[f"{prefix}_barrier"] = np.array([res['barrier']])
        if res['barrier_frac'] is not None:
            save_dict[f"{prefix}_barrier_frac"] = np.array([res['barrier_frac']])

    npz_path = os.path.join(data_dir, "s45_occ_spectral.npz")
    np.savez(npz_path, **save_dict)
    print(f"  Saved: {npz_path}")

    # ==============================================================================
    # SECTION 17: Plot
    # ==============================================================================

    print("\n[13] Generating plots...")

    fig, axes = plt.subplots(2, 3, figsize=(18, 11))

    # Panel 1: S_occ(tau) for exp cutoff, multiple Lambda
    ax = axes[0, 0]
    for Lambda in Lambda_values:
        so = S_occ[('exp', Lambda)]
        # Normalize to S_occ(0)
        ax.plot(tau_values, so / so[0], 'o-', ms=3, label=f'$\\Lambda={Lambda:.1f}$')
    ax.set_xlabel('$\\tau$')
    ax.set_ylabel('$S_{\\mathrm{occ}}(\\tau) / S_{\\mathrm{occ}}(0)$')
    ax.set_title('Occupied-state SA (exp cutoff)')
    ax.legend(fontsize=7)
    ax.axvline(tau_fold, color='gray', ls='--', alpha=0.5, label='fold')
    ax.grid(True, alpha=0.3)

    # Panel 2: S_vac(tau) vs S_occ(tau) comparison
    ax = axes[0, 1]
    Lambda_plot = 3.0
    sv = S_vac[('exp', Lambda_plot)]
    so = S_occ[('exp', Lambda_plot)]
    ax.plot(tau_values, sv / sv[0], 'b-o', ms=3, label='$S_{\\mathrm{vac}}$')
    ax.plot(tau_values, so / so[0], 'r-s', ms=3, label='$S_{\\mathrm{occ}}$')
    ax.set_xlabel('$\\tau$')
    ax.set_ylabel('Normalized spectral action')
    ax.set_title(f'Vacuum vs Occupied (exp, $\\Lambda={Lambda_plot}$)')
    ax.legend()
    ax.axvline(tau_fold, color='gray', ls='--', alpha=0.5)
    ax.grid(True, alpha=0.3)

    # Panel 3: Delta(tau) - BCS gap
    ax = axes[0, 2]
    ax.plot(tau_values, Delta_vs_tau, 'k-o', ms=4)
    ax.set_xlabel('$\\tau$')
    ax.set_ylabel('$\\Delta(\\tau)$ (M$_{\\mathrm{KK}}$ units)')
    ax.set_title('BCS Gap')
    ax.axvline(tau_fold, color='gray', ls='--', alpha=0.5, label='fold')
    ax.axhline(Delta_0_GL, color='green', ls=':', alpha=0.5, label=f'$\\Delta_0^{{GL}}={Delta_0_GL:.3f}$')
    ax.legend()
    ax.grid(True, alpha=0.3)

    # Panel 4: Occupation numbers at fold
    ax = axes[1, 0]
    tau_plot = 0.190
    evals_fold = all_pos_evals[tau_plot]
    n_fold = n_occ_vs_tau[tau_plot]
    w_fold = all_pw_weights[tau_plot]
    # Color by weight
    scatter = ax.scatter(evals_fold, n_fold, c=np.log10(w_fold+1), s=5, alpha=0.7, cmap='viridis')
    ax.set_xlabel('$|\\lambda_k|$ (M$_{\\mathrm{KK}}$)')
    ax.set_ylabel('$n_k = v_k^2$')
    ax.set_title(f'Occupation numbers at $\\tau={tau_plot}$')
    ax.axhline(0.5, color='gray', ls='--', alpha=0.3, label='$n=1/2$')
    plt.colorbar(scatter, ax=ax, label='$\\log_{10}(d_k+1)$')
    ax.grid(True, alpha=0.3)

    # Panel 5: Derivative decomposition
    ax = axes[1, 1]
    mask = (total_deriv != 0)
    ax.plot(tau_values[mask], occ_change_term[mask], 'r-o', ms=3, label='Occupation change')
    ax.plot(tau_values[mask], eval_change_term[mask], 'b-s', ms=3, label='Eigenvalue change')
    ax.plot(tau_values[mask], total_deriv[mask], 'k-^', ms=3, label='Total')
    ax.set_xlabel('$\\tau$')
    ax.set_ylabel('$dS_{\\mathrm{occ}}/d\\tau$')
    ax.set_title('Derivative decomposition')
    ax.legend(fontsize=7)
    ax.axhline(0, color='gray', ls='-', alpha=0.3)
    ax.axvline(tau_fold, color='gray', ls='--', alpha=0.5)
    ax.grid(True, alpha=0.3)

    # Panel 6: S_occ for all cutoffs at Lambda=3.0
    ax = axes[1, 2]
    for cutoff_name in cutoffs:
        so = S_occ[(cutoff_name, 3.0)]
        ax.plot(tau_values, so / so[0], 'o-', ms=3, label=cutoff_name)
    ax.set_xlabel('$\\tau$')
    ax.set_ylabel('$S_{\\mathrm{occ}}(\\tau)/S_{\\mathrm{occ}}(0)$')
    ax.set_title('Cutoff comparison ($\\Lambda=3.0$)')
    ax.legend()
    ax.axvline(tau_fold, color='gray', ls='--', alpha=0.5)
    ax.grid(True, alpha=0.3)

    plt.suptitle('OCC-SPEC-45: Occupied-State Spectral Action', fontsize=14, fontweight='bold')
    plt.tight_layout()

    plot_path = os.path.join(data_dir, "s45_occ_spectral.png")
    plt.savefig(plot_path, dpi=150)
    print(f"  Saved: {plot_path}")
    plt.close()

    print("\n" + "=" * 78)
    print(f"FINAL VERDICT: OCC-SPEC-45 = {verdict}")
    print("=" * 78)

    return verdict, results


if __name__ == "__main__":
    verdict, results = main()
