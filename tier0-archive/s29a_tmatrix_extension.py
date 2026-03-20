"""
Session 29a Computation 29a-1: T-Matrix Extension to tau=0.40, 0.50
====================================================================

Extends the KC-2 T-matrix computation (Session 28c) from tau=[0.15, 0.25, 0.35]
to include tau=[0.40, 0.50]. This tests whether phonon-phonon scattering remains
sufficient for thermalization at larger SU(3) deformation.

Gate K-29a (pre-registered):
    FAIL (KC-3 CLOSED): W/Gamma_inject < 0.1 at tau >= 0.50
    PASS: W/Gamma_inject >= 0.1 at tau=0.50

Physics:
--------
As tau increases, the SU(3) metric deformation changes two competing effects:
1. The Dirac eigenvalue spectrum compresses (gap shrinks), increasing the density
   of states and potentially enhancing scattering.
2. The Bogoliubov coefficients B_k change character -- if the deformation becomes
   more adiabatic, particle production slows and Gamma_inject could drop, but the
   modes are better defined. If it becomes less adiabatic, the injection rate grows.

The critical question: does the W/Gamma ratio remain O(1) or collapse?

From s28c results:
    tau=0.15: W/Gamma_inject = 0.52 (KC-2 PASS)
    tau=0.25: W/Gamma_inject = 0.19
    tau=0.35: W/Gamma_inject = 0.27

Input: tier0-computation/s23a_eigenvectors_extended.npz
       tier0-computation/s28a_bogoliubov_coefficients.npz
Output: tier0-computation/s29a_tmatrix_extension.npz
        tier0-computation/s29a_tmatrix_extension.png

Author: phonon-exflation-sim agent
Date: 2026-02-28
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
EIGVEC_FILE = DATA_DIR / "s23a_eigenvectors_extended.npz"
BOGO_FILE = DATA_DIR / "s28a_bogoliubov_coefficients.npz"
OUTPUT_NPZ = DATA_DIR / "s29a_tmatrix_extension.npz"
OUTPUT_PNG = DATA_DIR / "s29a_tmatrix_extension.png"

# Gate thresholds (same as KC-2 for consistency)
W_PASS_RATIO = 0.1    # W/Gamma > 0.1 = PASS
W_KILL_RATIO = 0.01   # W/Gamma < 0.01 = CLOSED

# Gate K-29a: specific test at high tau
K29A_TAU_THRESHOLD = 0.50
K29A_FAIL_RATIO = 0.1  # W/Gamma_inject < 0.1 at tau >= 0.50 = KC-3 FAIL

# Number of lowest modes to include
N_MODES = 20

# Full tau scan: original 3 + new 2
TAU_TARGETS = [0.15, 0.25, 0.35, 0.40, 0.50]

# Broadening for energy delta function
EPSILON = 0.02

# Occupation number
N_OCC = 1.0


# ==============================================================================
# Load data
# ==============================================================================

print("=" * 72)
print("29a-1: T-Matrix Extension to tau=0.40, 0.50 (Gate K-29a)")
print("=" * 72)

t_start = time.time()

print("\nLoading eigenvector data...")
evec_data = np.load(EIGVEC_FILE, allow_pickle=True)
tau_evec = evec_data['tau_values']
print(f"  Available tau values: {tau_evec}")

print("Loading Bogoliubov coefficient data...")
bogo_data = np.load(BOGO_FILE, allow_pickle=True)
tau_bogo = bogo_data['tau_values']
B_k_all = bogo_data['B_k']           # (21, 11424)
omega_all = bogo_data['omega_tracked']  # (21, 11424)
Gamma_inject_all = bogo_data['Gamma_inject']  # (21,)

# Find tau indices in both datasets
tau_idx_evec = {}
tau_idx_bogo = {}
for t_target in TAU_TARGETS:
    idx_e = np.argmin(np.abs(tau_evec - t_target))
    if abs(tau_evec[idx_e] - t_target) > 0.01:
        print(f"  WARNING: tau={t_target} not found in eigvec data. Closest: {tau_evec[idx_e]}")
    tau_idx_evec[t_target] = idx_e

    idx_b = np.argmin(np.abs(tau_bogo - t_target))
    if abs(tau_bogo[idx_b] - t_target) > 0.05:
        print(f"  WARNING: tau={t_target} not found in Bogoliubov data. Closest: {tau_bogo[idx_b]}")
    tau_idx_bogo[t_target] = idx_b

print(f"  Eigvec tau indices: {tau_idx_evec}")
print(f"  Bogo tau indices:   {tau_idx_bogo}")


# ==============================================================================
# Module 1: Extract lowest modes per tau
# ==============================================================================

def extract_lowest_modes(evec_data, tau_idx, n_modes):
    """
    Extract the n_modes lowest-|eigenvalue| modes at a given tau index.

    Returns:
        modes: list of dicts with keys:
            'eigenvalue': float (signed eigenvalue lambda)
            'omega': float (|lambda|)
            'sector_idx': int (index into sector_labels)
            'sector_pq': (p, q) tuple
            'col_idx': int (column index within sector eigenvector matrix)
            'eigvec': ndarray, shape (sector_size,), the eigenvector coefficients
        sector_labels: ndarray, shape (n_sectors, 2)
        sector_sizes: ndarray, shape (n_sectors,)
    """
    ti = tau_idx
    evals = evec_data[f'eigenvalues_{ti}']
    sector_labels = evec_data[f'sector_labels_{ti}']
    sector_sizes = evec_data[f'sector_sizes_{ti}']

    n_sectors = len(sector_labels)

    # Build cumulative offset into the flat eigenvalue array
    cum_offsets = np.zeros(n_sectors + 1, dtype=int)
    for s in range(n_sectors):
        cum_offsets[s + 1] = cum_offsets[s] + sector_sizes[s]

    # Sort by |eigenvalue|
    abs_evals = np.abs(evals)
    sort_idx = np.argsort(abs_evals)

    modes = []
    for i in range(min(n_modes, len(evals))):
        flat_idx = sort_idx[i]
        lam = evals[flat_idx]

        # Find which sector contains this flat_idx
        s_idx = None
        for s in range(n_sectors):
            if cum_offsets[s] <= flat_idx < cum_offsets[s + 1]:
                s_idx = s
                break

        assert s_idx is not None, f"Could not find sector for flat_idx={flat_idx}"

        col_idx = flat_idx - cum_offsets[s_idx]
        evec_matrix = evec_data[f'eigvec_{ti}_sector_{s_idx}']
        eigvec = evec_matrix[:, col_idx]

        modes.append({
            'eigenvalue': lam,
            'omega': abs(lam),
            'sector_idx': s_idx,
            'sector_pq': (int(sector_labels[s_idx][0]), int(sector_labels[s_idx][1])),
            'col_idx': col_idx,
            'eigvec': eigvec,
            'flat_idx': flat_idx,
        })

    return modes, sector_labels, sector_sizes


# ==============================================================================
# Module 2: Intra-sector 4-point overlap
# ==============================================================================

def overlap_4pt_intra(v_a, v_b, v_c, v_d):
    """
    Compute intra-sector 4-point overlap and Cauchy-Schwarz upper bound.

    The "diagonal" overlap sum_I conj(v_a[I]) * conj(v_b[I]) * v_c[I] * v_d[I]
    captures the delta_{IJKL} contribution. The Hadamard-product Cauchy-Schwarz
    bound provides a tight upper bound on the full 4-point integral including
    off-diagonal CG contributions.

    Parameters:
        v_a, v_b, v_c, v_d: ndarray, shape (N,), complex eigenvector coefficients

    Returns:
        V_diag: complex, diagonal contribution
        V_bound: float, Cauchy-Schwarz upper bound on |V_{abcd}|
    """
    V_diag = np.sum(np.conj(v_a) * np.conj(v_b) * v_c * v_d)

    V_bound = np.sqrt(np.sum(np.abs(v_a * v_b)**2)) * \
              np.sqrt(np.sum(np.abs(v_c * v_d)**2))

    return V_diag, V_bound


# ==============================================================================
# Module 3: Cross-sector overlap estimation
# ==============================================================================

def overlap_4pt_cross_bound(dim_a, dim_b, dim_c, dim_d):
    """
    Upper bound on cross-sector 4-point overlap: 1/sqrt(dim_max).

    Parameters:
        dim_a, dim_b, dim_c, dim_d: sector dimensions

    Returns:
        V_bound: float, upper bound on |V_{abcd}|
    """
    dim_max = max(dim_a, dim_b, dim_c, dim_d)
    return 1.0 / np.sqrt(dim_max)


def check_selection_rule(pq1, pq2, pq3, pq4):
    """
    Check SU(3) triality conservation for 4-point overlap:
        (q1-p1) + (q2-p2) + (p3-q3) + (p4-q4) = 0 mod 3

    Returns:
        bool: True if selection rule allows nonzero overlap
    """
    triality = (pq1[1] - pq1[0]) + (pq2[1] - pq2[0]) + (pq3[0] - pq3[1]) + (pq4[0] - pq4[1])
    return triality % 3 == 0


# ==============================================================================
# Module 4: Compute T-matrix elements
# ==============================================================================

def compute_tmatrix(modes, n_modes):
    """
    Compute Born + 1-loop T-matrix for phonon-phonon scattering.

    T_{12->34} = V_{1234} + sum_{m,n} V_{12mn} * G_{mn}(E1+E2) * V_{mn34}

    where G_{mn}(E) = 1/(E - omega_m - omega_n + i*epsilon).

    Returns:
        V_born, V_upper, T_full, T_upper: ndarray shape (n, n, n, n)
        omega: ndarray shape (n,)
    """
    omega = np.array([m['omega'] for m in modes[:n_modes]])

    V_born = np.zeros((n_modes, n_modes, n_modes, n_modes), dtype=complex)
    V_upper = np.zeros((n_modes, n_modes, n_modes, n_modes))

    sector_ids = [m['sector_idx'] for m in modes[:n_modes]]
    sector_pqs = [m['sector_pq'] for m in modes[:n_modes]]
    eigvecs = [m['eigvec'] for m in modes[:n_modes]]

    n_intra = 0
    n_cross_allowed = 0
    n_cross_forbidden = 0

    for a in range(n_modes):
        for b in range(a, n_modes):
            for c in range(n_modes):
                for d in range(c, n_modes):
                    sa, sb, sc, sd = sector_ids[a], sector_ids[b], sector_ids[c], sector_ids[d]

                    if sa == sb == sc == sd:
                        v_diag, v_bnd = overlap_4pt_intra(
                            eigvecs[a], eigvecs[b], eigvecs[c], eigvecs[d]
                        )
                        V_born[a, b, c, d] = v_diag
                        V_upper[a, b, c, d] = v_bnd
                        n_intra += 1
                    else:
                        pqa, pqb, pqc, pqd = sector_pqs[a], sector_pqs[b], sector_pqs[c], sector_pqs[d]

                        if check_selection_rule(pqa, pqb, pqc, pqd):
                            dim_a = len(eigvecs[a])
                            dim_b = len(eigvecs[b])
                            dim_c = len(eigvecs[c])
                            dim_d = len(eigvecs[d])
                            v_bnd = overlap_4pt_cross_bound(dim_a, dim_b, dim_c, dim_d)
                            V_born[a, b, c, d] = 0.0
                            V_upper[a, b, c, d] = v_bnd
                            n_cross_allowed += 1
                        else:
                            V_born[a, b, c, d] = 0.0
                            V_upper[a, b, c, d] = 0.0
                            n_cross_forbidden += 1

                    # Symmetries
                    V_born[b, a, d, c] = V_born[a, b, c, d]
                    V_upper[b, a, d, c] = V_upper[a, b, c, d]
                    V_born[c, d, a, b] = np.conj(V_born[a, b, c, d])
                    V_upper[c, d, a, b] = V_upper[a, b, c, d]
                    V_born[d, c, b, a] = np.conj(V_born[a, b, c, d])
                    V_upper[d, c, b, a] = V_upper[a, b, c, d]

    print(f"  4-point overlaps: {n_intra} intra, {n_cross_allowed} cross-allowed, {n_cross_forbidden} cross-forbidden")

    # T-matrix: Born + 1-loop (s-channel bubble)
    T_full = np.zeros_like(V_born)
    T_upper = np.zeros_like(V_upper)

    for a in range(n_modes):
        for b in range(n_modes):
            E_in = omega[a] + omega[b]
            for c in range(n_modes):
                for d in range(n_modes):
                    T_ab_cd = V_born[a, b, c, d]
                    T_ub_cd = V_upper[a, b, c, d]

                    loop_contrib = 0.0 + 0.0j
                    loop_ub = 0.0

                    for m in range(n_modes):
                        for n in range(n_modes):
                            E_int = omega[m] + omega[n]
                            G_mn = 1.0 / (E_in - E_int + 1j * EPSILON)

                            loop_contrib += V_born[a, b, m, n] * G_mn * V_born[m, n, c, d]
                            loop_ub += V_upper[a, b, m, n] * abs(G_mn) * V_upper[m, n, c, d]

                    T_full[a, b, c, d] = T_ab_cd + loop_contrib
                    T_upper[a, b, c, d] = T_ub_cd + loop_ub

    return V_born, V_upper, T_full, T_upper, omega


# ==============================================================================
# Module 5: Scattering rate computation
# ==============================================================================

def compute_scattering_rate(T_full, T_upper, omega, n_modes):
    """
    Compute scattering rate W_{ab} = 2*pi * sum_{c,d} |T|^2 * delta(dE) * n^2.

    Uses Lorentzian approximation for the energy delta function:
        delta(E) ~ (1/pi) * epsilon / (E^2 + epsilon^2)

    Returns:
        W, W_upper: ndarray shape (n_modes, n_modes)
    """
    W = np.zeros((n_modes, n_modes))
    W_upper = np.zeros((n_modes, n_modes))

    for a in range(n_modes):
        for b in range(n_modes):
            E_in = omega[a] + omega[b]
            rate = 0.0
            rate_ub = 0.0

            for c in range(n_modes):
                for d in range(n_modes):
                    E_out = omega[c] + omega[d]
                    dE = E_in - E_out
                    delta_L = (1.0 / np.pi) * EPSILON / (dE**2 + EPSILON**2)

                    rate += abs(T_full[a, b, c, d])**2 * delta_L * N_OCC**2
                    rate_ub += T_upper[a, b, c, d]**2 * delta_L * N_OCC**2

            W[a, b] = 2 * np.pi * rate
            W_upper[a, b] = 2 * np.pi * rate_ub

    return W, W_upper


# ==============================================================================
# Module 6: Main computation loop
# ==============================================================================

print("\n" + "=" * 72)
print("COMPUTING 4-POINT OVERLAPS AND T-MATRIX")
print(f"tau values: {TAU_TARGETS}")
print(f"N_modes: {N_MODES}, epsilon: {EPSILON}")
print("=" * 72)

results = {}

for tau_target in TAU_TARGETS:
    print(f"\n{'='*60}")
    print(f"tau = {tau_target:.2f}")
    print(f"{'='*60}")

    ti_evec = tau_idx_evec[tau_target]
    ti_bogo = tau_idx_bogo[tau_target]

    print(f"  Extracting {N_MODES} lowest modes (eigvec tau_idx={ti_evec})...")
    modes, sector_labels, sector_sizes = extract_lowest_modes(evec_data, ti_evec, N_MODES)

    print(f"  Mode summary:")
    for i, m in enumerate(modes):
        print(f"    mode {i:2d}: omega={m['omega']:.6f}, lambda={m['eigenvalue']:+.6f}, "
              f"sector=({m['sector_pq'][0]},{m['sector_pq'][1]}), col={m['col_idx']}")

    print(f"\n  Computing 4-point overlaps and T-matrix ({N_MODES}^4 = {N_MODES**4})...")
    t0 = time.time()
    V_born, V_upper, T_full, T_upper, omega = compute_tmatrix(modes, N_MODES)
    t1 = time.time()
    print(f"  Done in {t1-t0:.2f}s")

    # Born vertex statistics
    V_abs = np.abs(V_born)
    V_nonzero = V_abs[V_abs > 1e-15]
    print(f"\n  Born vertex |V|: max={V_abs.max():.4e}, mean={V_abs.mean():.4e}, "
          f"nonzero={len(V_nonzero)}/{V_abs.size}")
    print(f"  Upper bound V:   max={V_upper.max():.4e}, mean={V_upper.mean():.4e}")

    T_abs = np.abs(T_full)
    print(f"  T-matrix |T|:    max={T_abs.max():.4e}, mean={T_abs.mean():.4e}")

    # Scattering rate
    print(f"  Computing scattering rate...")
    W, W_upper = compute_scattering_rate(T_full, T_upper, omega, N_MODES)

    # Gamma_inject from Bogoliubov data
    Gamma_inject = Gamma_inject_all[ti_bogo]
    B_k_tau = B_k_all[ti_bogo]
    omega_tau = omega_all[ti_bogo]

    # Per-mode decay rate from gap-edge Bogoliubov coefficients
    mask = omega_tau > 0.01
    omega_pos = omega_tau[mask]
    B_pos = B_k_tau[mask]
    gap_sort = np.argsort(omega_pos)
    gap_edge_idx = gap_sort[:N_MODES]

    B_gap = B_pos[gap_edge_idx]
    omega_gap = omega_pos[gap_edge_idx]

    Gamma_per_mode = B_gap * omega_gap
    Gamma_decay = np.mean(Gamma_per_mode)
    Gamma_decay_max = np.max(Gamma_per_mode)

    W_max = W.max()
    W_upper_max = W_upper.max()
    W_mean_diag = np.mean(np.diag(W))

    # Compute key ratios
    ratio_born = W_max / Gamma_decay if Gamma_decay > 0 else np.inf
    ratio_upper = W_upper_max / Gamma_decay if Gamma_decay > 0 else np.inf
    ratio_vs_inject = W_max / Gamma_inject if Gamma_inject > 0 else np.inf
    ratio_vs_omega = W_max / np.mean(omega_gap)

    print(f"\n  W_max = {W_max:.6e},  W_upper_max = {W_upper_max:.6e}")
    print(f"  Gamma_decay (mean) = {Gamma_decay:.6e},  Gamma_decay (max) = {Gamma_decay_max:.6e}")
    print(f"  Gamma_inject       = {Gamma_inject:.6e}")
    print(f"  B_k gap-edge: min={B_gap.min():.4e}, max={B_gap.max():.4e}, mean={B_gap.mean():.4e}")
    print(f"\n  KEY RATIOS:")
    print(f"    W/Gamma_decay (mean)   = {ratio_born:.4e}")
    print(f"    W/Gamma_decay (max)    = {W_max/Gamma_decay_max:.4e}")
    print(f"    W/Gamma_inject         = {ratio_vs_inject:.4e}")
    print(f"    W/omega_gap (mean)     = {ratio_vs_omega:.4e}")

    results[tau_target] = {
        'modes': modes,
        'V_born': V_born,
        'V_upper': V_upper,
        'T_full': T_full,
        'T_upper': T_upper,
        'omega': omega,
        'W': W,
        'W_upper': W_upper,
        'Gamma_decay': Gamma_decay,
        'Gamma_decay_max': Gamma_decay_max,
        'Gamma_inject': Gamma_inject,
        'ratio_born': ratio_born,
        'ratio_upper': ratio_upper,
        'ratio_vs_inject': ratio_vs_inject,
        'ratio_vs_omega': ratio_vs_omega,
        'B_gap_mean': float(B_gap.mean()),
        'B_gap_max': float(B_gap.max()),
        'omega_gap_mean': float(np.mean(omega_gap)),
    }


# ==============================================================================
# Module 7: Gate K-29a verdict
# ==============================================================================

print("\n" + "=" * 72)
print("GATE K-29a: T-MATRIX EXTENSION VERDICT")
print("=" * 72)

# Summary table
print(f"\n  {'tau':>5s} | {'W_max':>12s} | {'Gamma_inj':>12s} | {'W/G_inj':>12s} | {'W/G_decay':>12s} | {'B_gap_mean':>12s}")
print(f"  {'-'*5}-+-{'-'*12}-+-{'-'*12}-+-{'-'*12}-+-{'-'*12}-+-{'-'*12}")
for tau in TAU_TARGETS:
    r = results[tau]
    print(f"  {tau:5.2f} | {r['W'].max():12.4e} | {r['Gamma_inject']:12.4e} | "
          f"{r['ratio_vs_inject']:12.4e} | {r['ratio_born']:12.4e} | {r['B_gap_mean']:12.4e}")

# Gate K-29a: W/Gamma_inject at tau >= 0.50
tau_test = K29A_TAU_THRESHOLD
r_test = results[tau_test]
ratio_at_050 = r_test['ratio_vs_inject']

print(f"\n  Gate K-29a test: W/Gamma_inject at tau={tau_test:.2f} = {ratio_at_050:.4e}")
print(f"  Threshold: W/Gamma_inject < {K29A_FAIL_RATIO} -> KC-3 FAIL")

if ratio_at_050 < K29A_FAIL_RATIO:
    k29a_verdict = "FAIL"
    k29a_detail = (f"W/Gamma_inject = {ratio_at_050:.4e} < {K29A_FAIL_RATIO} at tau={tau_test}. "
                   f"Phonon thermalization insufficient at large deformation. KC-3 CLOSED.")
else:
    k29a_verdict = "PASS"
    k29a_detail = (f"W/Gamma_inject = {ratio_at_050:.4e} >= {K29A_FAIL_RATIO} at tau={tau_test}. "
                   f"Phonon scattering remains sufficient.")

print(f"\n  K-29a VERDICT: {k29a_verdict}")
print(f"  Detail: {k29a_detail}")

# Also check the full KC-2 gate across all tau (using W/Gamma_decay as in original)
max_ratio_born = max(r['ratio_born'] for r in results.values())
max_ratio_upper = max(r['ratio_upper'] for r in results.values())
best_tau_born = max(results.keys(), key=lambda t: results[t]['ratio_born'])

if max_ratio_born >= W_PASS_RATIO:
    kc2_verdict = "PASS"
elif max_ratio_upper >= W_PASS_RATIO:
    kc2_verdict = "INCONCLUSIVE_HIGH"
elif max_ratio_upper < W_KILL_RATIO:
    kc2_verdict = "CLOSED"
else:
    kc2_verdict = "INCONCLUSIVE"

print(f"\n  KC-2 extended verdict: {kc2_verdict}")
print(f"  Best W/Gamma_decay = {max_ratio_born:.4e} at tau={best_tau_born}")

# Trend analysis: is W/Gamma_inject monotonically decreasing?
ratios_inject = [results[t]['ratio_vs_inject'] for t in TAU_TARGETS]
monotone_decrease = all(ratios_inject[i] >= ratios_inject[i+1] for i in range(len(ratios_inject)-1))
print(f"\n  Trend analysis:")
print(f"    W/Gamma_inject values: {[f'{r:.4e}' for r in ratios_inject]}")
print(f"    Monotonically decreasing: {monotone_decrease}")

if monotone_decrease and ratio_at_050 < K29A_FAIL_RATIO:
    print(f"    IMPLICATION: Scattering rate declining monotonically and below threshold.")
    print(f"    This is a ROBUST closure -- not a fluctuation.")
elif not monotone_decrease:
    print(f"    Non-monotonic behavior: the tau dependence has structure.")
    # Check if there is a minimum
    min_idx = np.argmin(ratios_inject)
    print(f"    Minimum W/Gamma_inject = {ratios_inject[min_idx]:.4e} at tau={TAU_TARGETS[min_idx]}")


# ==============================================================================
# Module 8: Diagnostics
# ==============================================================================

print("\n" + "=" * 72)
print("DIAGNOSTICS: New tau values")
print("=" * 72)

for tau_target in [0.40, 0.50]:
    r = results[tau_target]
    print(f"\n--- tau = {tau_target:.2f} ---")

    W = r['W']
    flat_idx = np.argsort(W.ravel())[::-1]
    print(f"  Top 5 scattering channels (a,b) by W_ab:")
    for rank in range(min(5, len(flat_idx))):
        idx = flat_idx[rank]
        a, b = np.unravel_index(idx, W.shape)
        ma = r['modes'][a]
        mb = r['modes'][b]
        print(f"    #{rank+1}: ({a},{b}), W={W[a,b]:.4e}, "
              f"omega=({ma['omega']:.4f},{mb['omega']:.4f}), "
              f"sectors=({ma['sector_pq']},{mb['sector_pq']})")

    # Energy-conserving channels
    omega = r['omega']
    n_conserving = 0
    for a in range(N_MODES):
        for b in range(N_MODES):
            for c in range(N_MODES):
                for d in range(N_MODES):
                    dE = abs(omega[a] + omega[b] - omega[c] - omega[d])
                    if dE < EPSILON and abs(r['T_full'][a,b,c,d]) > 1e-15:
                        n_conserving += 1
    print(f"  Energy-conserving channels (|dE| < {EPSILON}): {n_conserving}")

    # Sector composition
    V_abs = np.abs(r['V_born'])
    sector_pairs = {}
    for a in range(N_MODES):
        for b in range(N_MODES):
            for c in range(N_MODES):
                for d in range(N_MODES):
                    if V_abs[a,b,c,d] > 1e-15:
                        key = (r['modes'][a]['sector_pq'], r['modes'][b]['sector_pq'],
                               r['modes'][c]['sector_pq'], r['modes'][d]['sector_pq'])
                        if key not in sector_pairs:
                            sector_pairs[key] = []
                        sector_pairs[key].append(V_abs[a,b,c,d])

    print(f"  Born vertex sector structure:")
    for key in sorted(sector_pairs.keys(), key=lambda k: -max(sector_pairs[k]))[:5]:
        vals = sector_pairs[key]
        print(f"    {key}: {len(vals)} nonzero, max={max(vals):.4e}")


# ==============================================================================
# Module 9: Save output
# ==============================================================================

print("\n" + "=" * 72)
print("SAVING OUTPUT")
print("=" * 72)

save_dict = {
    'tau_targets': np.array(TAU_TARGETS),
    'n_modes': np.array([N_MODES]),
    'epsilon': np.array([EPSILON]),
    'k29a_verdict': np.array([k29a_verdict]),
    'kc2_extended_verdict': np.array([kc2_verdict]),
    'k29a_ratio_at_050': np.array([ratio_at_050]),
}

for i, tau_target in enumerate(TAU_TARGETS):
    r = results[tau_target]
    prefix = f'tau{i}_'
    save_dict[prefix + 'tau'] = np.array([tau_target])
    save_dict[prefix + 'omega'] = r['omega']
    save_dict[prefix + 'V_born'] = r['V_born']
    save_dict[prefix + 'V_upper'] = r['V_upper']
    save_dict[prefix + 'T_full'] = r['T_full']
    save_dict[prefix + 'T_upper'] = r['T_upper']
    save_dict[prefix + 'W'] = r['W']
    save_dict[prefix + 'W_upper'] = r['W_upper']
    save_dict[prefix + 'Gamma_decay'] = np.array([r['Gamma_decay']])
    save_dict[prefix + 'Gamma_decay_max'] = np.array([r['Gamma_decay_max']])
    save_dict[prefix + 'Gamma_inject'] = np.array([r['Gamma_inject']])
    save_dict[prefix + 'ratio_born'] = np.array([r['ratio_born']])
    save_dict[prefix + 'ratio_upper'] = np.array([r['ratio_upper']])
    save_dict[prefix + 'ratio_vs_inject'] = np.array([r['ratio_vs_inject']])
    save_dict[prefix + 'ratio_vs_omega'] = np.array([r['ratio_vs_omega']])

np.savez_compressed(OUTPUT_NPZ, **save_dict)
print(f"  Saved: {OUTPUT_NPZ}")


# ==============================================================================
# Module 10: Visualization
# ==============================================================================

print("\nGenerating plots...")

fig = plt.figure(figsize=(20, 16))
fig.suptitle(f'29a-1: T-Matrix Extension — K-29a: {k29a_verdict}', fontsize=14, fontweight='bold')

# Layout: 3 rows
# Row 1 (5 panels): W heatmaps for each tau
# Row 2 (5 panels): W/Gamma histograms for each tau
# Row 3 (2 panels): Trend plots

gs = fig.add_gridspec(3, 5, hspace=0.35, wspace=0.35,
                      height_ratios=[1, 1, 1.2])

# Row 1: W heatmaps
for i, tau_target in enumerate(TAU_TARGETS):
    r = results[tau_target]
    ax = fig.add_subplot(gs[0, i])
    im = ax.imshow(np.log10(r['W'] + 1e-30), cmap='hot', aspect='equal')
    ax.set_title(f'log10(W) tau={tau_target:.2f}', fontsize=10)
    ax.set_xlabel('Mode b', fontsize=8)
    ax.set_ylabel('Mode a', fontsize=8)
    plt.colorbar(im, ax=ax, shrink=0.8)

# Row 2: W/Gamma histograms
for i, tau_target in enumerate(TAU_TARGETS):
    r = results[tau_target]
    ax = fig.add_subplot(gs[1, i])
    W_flat = r['W'].ravel()
    W_flat_pos = W_flat[W_flat > 1e-30]
    if len(W_flat_pos) > 0 and r['Gamma_decay'] > 0:
        ratio_flat = W_flat_pos / r['Gamma_decay']
        ax.hist(np.log10(ratio_flat), bins=50, color='steelblue', alpha=0.7, edgecolor='black')
        ax.axvline(np.log10(W_PASS_RATIO), color='green', ls='--', lw=2, label='PASS')
        ax.axvline(np.log10(W_KILL_RATIO), color='red', ls='--', lw=2, label='CLOSURE')
        ax.set_xlabel('log10(W/Gamma_decay)', fontsize=8)
        ax.set_ylabel('Count', fontsize=8)
        ax.legend(fontsize=7)
    ax.set_title(f'W/G dist tau={tau_target:.2f}', fontsize=10)

# Row 3: Trend plots
# Panel 1: W/Gamma_inject vs tau
ax1 = fig.add_subplot(gs[2, 0:2])
taus = np.array(TAU_TARGETS)
ratios_inject = np.array([results[t]['ratio_vs_inject'] for t in TAU_TARGETS])
ratios_decay = np.array([results[t]['ratio_born'] for t in TAU_TARGETS])
W_max_vals = np.array([results[t]['W'].max() for t in TAU_TARGETS])
Gamma_inj_vals = np.array([results[t]['Gamma_inject'] for t in TAU_TARGETS])

ax1.semilogy(taus, ratios_inject, 'bo-', lw=2, ms=8, label='W/Gamma_inject')
ax1.axhline(K29A_FAIL_RATIO, color='red', ls='--', lw=2, label=f'K-29a threshold ({K29A_FAIL_RATIO})')
ax1.axhline(1.0, color='gray', ls=':', lw=1, label='W = Gamma_inject')
ax1.set_xlabel('tau', fontsize=12)
ax1.set_ylabel('W / Gamma_inject', fontsize=12)
ax1.set_title('K-29a: Scattering / Injection Ratio', fontsize=12)
ax1.legend(fontsize=9)
ax1.grid(True, alpha=0.3)
ax1.set_xlim(0.10, 0.55)

# Mark the K-29a test point
ax1.plot(0.50, ratios_inject[-1], 'r*', ms=15, zorder=5, label=f'K-29a: {ratios_inject[-1]:.3f}')
ax1.legend(fontsize=9)

# Panel 2: W_max and Gamma_inject vs tau (absolute values)
ax2 = fig.add_subplot(gs[2, 2:4])
ax2.semilogy(taus, W_max_vals, 'bs-', lw=2, ms=8, label='W_max')
ax2.semilogy(taus, Gamma_inj_vals, 'r^-', lw=2, ms=8, label='Gamma_inject')
ax2.semilogy(taus, [results[t]['Gamma_decay'] for t in TAU_TARGETS], 'gv-', lw=2, ms=8, label='Gamma_decay')
ax2.set_xlabel('tau', fontsize=12)
ax2.set_ylabel('Rate (natural units)', fontsize=12)
ax2.set_title('Absolute Rates vs tau', fontsize=12)
ax2.legend(fontsize=9)
ax2.grid(True, alpha=0.3)
ax2.set_xlim(0.10, 0.55)

# Panel 3: W/Gamma_decay (the KC-2 metric) vs tau
ax3 = fig.add_subplot(gs[2, 4])
ax3.semilogy(taus, ratios_decay, 'go-', lw=2, ms=8)
ax3.axhline(W_PASS_RATIO, color='green', ls='--', lw=1.5)
ax3.axhline(W_KILL_RATIO, color='red', ls='--', lw=1.5)
ax3.set_xlabel('tau', fontsize=12)
ax3.set_ylabel('W / Gamma_decay', fontsize=12)
ax3.set_title('KC-2 metric', fontsize=12)
ax3.grid(True, alpha=0.3)
ax3.set_xlim(0.10, 0.55)

plt.savefig(OUTPUT_PNG, dpi=150, bbox_inches='tight')
print(f"  Saved: {OUTPUT_PNG}")

t_end = time.time()
print(f"\nTotal runtime: {t_end - t_start:.1f}s")
print(f"\n{'='*72}")
print(f"FINAL VERDICTS:")
print(f"  K-29a = {k29a_verdict} (W/Gamma_inject = {ratio_at_050:.4e} at tau=0.50)")
print(f"  KC-2 extended = {kc2_verdict} (best W/Gamma_decay = {max_ratio_born:.4e} at tau={best_tau_born})")
print(f"{'='*72}")
