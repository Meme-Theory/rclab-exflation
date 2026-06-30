#!/usr/bin/env python3
"""
S55 DBCS-CONNES-55: State-Dependent Connes Distance D_BCS.

Computes the Connes distance from the state-dependent spectral triple where
the Dirac operator is rescaled by the BCS occupation field:

  D_BCS_{ij} = D_{ij} / sqrt(F_i * F_j)   for i != j
  D_BCS_{ii} = D_{ii} / F_i                for diagonal

where F_i(tau) = sum_k |psi_k(i)|^2 * n_k(tau) is the local BCS occupation
at cell i.  psi_k are eigenvectors of the TB Hamiltonian and n_k are BCS
occupations from the odd-even staggering (OES) pairing model.

MATHEMATICAL STRUCTURE:
  The spectral triple (A, H, D_BCS) has:
    A = C(V) = C^32  (functions on 32 Voronoi cells)
    H = C^32
    D_BCS(tau) = occupation-rescaled Hamiltonian

  The Connes distance is:
    d_BCS(i,j) = sup{|f_i - f_j| : ||[D_BCS, diag(f)]||_op <= 1}

  Physical interpretation: BCS condensation concentrates occupation on
  low-lying modes (n_0 ~ 0.85 at tau=0).  The rescaling D -> D/sqrt(F*F)
  ENHANCES the operator norm in regions of low occupation, effectively
  making depleted regions metrically farther apart.  If occupation
  concentration at the fold is strong enough, it could create a minimum
  in <d_BCS>(tau) via competition with the geometric expansion (which
  drives <d_D>(tau) monotonically upward).

SOLVER: cvxpy with CLARABEL backend, parametric SDP.

Gate: DBCS-CONNES-55
  PASS: <d_BCS>(tau) has minimum in [0.10, 0.30]
  FAIL: monotone

Author: Connes-NCG-Theorist (Session 55)
"""

import numpy as np
import cvxpy as cp
import time
import os
import sys
import warnings
warnings.filterwarnings('ignore')

# ─── constants ───────────────────────────────────────────────────────────
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import tau_fold, N_cells

# ─── paths ───────────────────────────────────────────────────────────────
PROJ = os.path.dirname(os.path.abspath(__file__))
INPUT_TB = os.path.join(PROJ, "s54_tb_hamiltonian.npz")
INPUT_OCC = os.path.join(PROJ, "s54_sa_latt_occ.npz")
INPUT_REF = os.path.join(PROJ, "s54_connes_latt.npz")
OUTPUT_NPZ = os.path.join(PROJ, "s55_dbcs_connes.npz")
OUTPUT_PNG = os.path.join(PROJ, "s55_dbcs_connes.png")


def build_basis_matrices(D_off):
    """Build E_k basis for the commutator [D_off, diag(f)] = sum_k f_k E_k.

    E_k = e_k e_k^T @ D - D @ e_k e_k^T.
    Verification: [diag(f), D]_{ab} = (f_a - f_b) D_{ab}.
    """
    N = D_off.shape[0]
    E_list = []
    for k in range(N):
        ek = np.zeros(N)
        ek[k] = 1.0
        Ek = np.outer(ek, ek) @ D_off - D_off @ np.outer(ek, ek)
        E_list.append(Ek)
    return E_list


def compute_all_connes_distances(D_off, label=""):
    """Compute all N*(N-1)/2 Connes distances via parametric SDP.

    For each pair (i,j):
      maximize   f_i - f_j
      subject to [[I, M(f)], [-M(f), I]] >> 0

    where M(f) = sum_k f_k E_k and the Schur complement ensures
    sigma_max(M) <= 1, i.e. ||[D, diag(f)]||_op <= 1.
    """
    N = D_off.shape[0]
    n_pairs = N * (N - 1) // 2

    E_list = build_basis_matrices(D_off)

    # Parametric SDP: compile once, solve many times
    f_var = cp.Variable(N)
    c_param = cp.Parameter(N)

    M = sum(f_var[k] * E_list[k] for k in range(N))
    I_n = np.eye(N)
    top = cp.hstack([I_n, M])
    bot = cp.hstack([-M, I_n])
    big = cp.vstack([top, bot])

    objective = cp.Maximize(c_param @ f_var)
    constraints = [big >> 0]
    prob = cp.Problem(objective, constraints)

    # Warm compile
    c_val = np.zeros(N)
    c_val[0] = 1.0
    c_val[1] = -1.0
    c_param.value = c_val
    prob.solve(solver=cp.CLARABEL, verbose=False)

    # Solve all pairs
    pairs = [(i, j) for i in range(N) for j in range(i + 1, N)]
    dist_matrix = np.zeros((N, N))
    distances_flat = np.zeros(n_pairs)

    for idx, (i, j) in enumerate(pairs):
        c_val = np.zeros(N)
        c_val[i] = 1.0
        c_val[j] = -1.0
        c_param.value = c_val

        try:
            prob.solve(solver=cp.CLARABEL, verbose=False, warm_start=True)
            if prob.status not in ['infeasible', 'unbounded', None] and prob.value is not None:
                d = max(prob.value, 0.0)
            else:
                d = np.nan
        except Exception:
            d = np.nan

        dist_matrix[i, j] = d
        dist_matrix[j, i] = d
        distances_flat[idx] = d

        if (idx + 1) % 100 == 0:
            print(f"    {label} pair {idx+1}/{n_pairs}")

    return dist_matrix, distances_flat


def compute_occupation_field(eigvecs, occupations):
    """Compute the local BCS occupation field F_i(tau).

    F_i = sum_k |psi_k(i)|^2 * n_k

    Parameters
    ----------
    eigvecs : (N, N) array
        Eigenvectors of the TB Hamiltonian, eigvecs[:, k] = psi_k
    occupations : (N,) array
        BCS occupations n_k for each mode

    Returns
    -------
    F : (N,) array
        Local occupation at each cell
    """
    # eigvecs[i, k] = component of k-th eigenvector at cell i
    # BUT numpy convention from np.linalg.eigh: eigvecs[:, k]
    # From s54_tb_hamiltonian: eigvecs shape (32, 32), stored as [tau_idx, :, :]
    # We need |psi_k(i)|^2 = eigvecs[i, k]^2
    F = np.sum(np.abs(eigvecs)**2 * occupations[np.newaxis, :], axis=1)
    return F


def construct_D_BCS(H, F, epsilon=1e-12):
    """Construct the state-dependent Dirac operator D_BCS.

    D_BCS_{ij} = H_{ij} / sqrt(F_i * F_j)   for i != j
    D_BCS_{ii} = H_{ii} / F_i

    The rescaling by 1/sqrt(F_i F_j) has a precise NCG interpretation:
    it is the Dirac operator of the weighted spectral triple where the
    Hilbert space inner product is modified by the occupation measure.
    In the commutative limit, this corresponds to a conformal rescaling
    of the metric g -> g / F^2.

    Parameters
    ----------
    H : (N, N) array
        TB Hamiltonian (symmetric)
    F : (N,) array
        Local occupation field (positive)
    epsilon : float
        Regularization floor for F to avoid division by zero

    Returns
    -------
    D_BCS : (N, N) array
        State-dependent Dirac operator (symmetric)
    """
    N = H.shape[0]
    F_reg = np.maximum(F, epsilon)

    # Off-diagonal: divide by sqrt(F_i * F_j)
    sqrt_F = np.sqrt(F_reg)
    outer_sqrt_F = np.outer(sqrt_F, sqrt_F)
    D_BCS = H / outer_sqrt_F

    # Diagonal: divide by F_i (which is sqrt(F_i * F_i) = F_i, consistent)
    # Actually sqrt(F_i * F_i) = F_i, so the formula is unified:
    # D_BCS_{ij} = H_{ij} / sqrt(F_i * F_j) for ALL i,j
    # The diagonal case is automatically correct.

    return D_BCS


def main():
    print("=" * 70)
    print("S55 DBCS-CONNES-55: State-Dependent Connes Distance D_BCS")
    print("=" * 70)

    # ─── Load data ────────────────────────────────────────────────────────
    print("\n--- Loading data ---")
    tb = np.load(INPUT_TB, allow_pickle=True)
    occ_data = np.load(INPUT_OCC, allow_pickle=True)
    ref_data = np.load(INPUT_REF, allow_pickle=True)

    all_tau = tb['tau_values']      # (50,)
    hamiltonians = tb['hamiltonians']  # (50, 32, 32)
    eigenvectors = tb['eigenvectors']  # (50, 32, 32)
    adjacency = tb['adjacency']     # (32, 32)

    occ_bcs = occ_data['occ_bcs_oes']  # (50, 32)

    ref_tau = ref_data['tau_values']     # (10,)
    ref_mean_d = ref_data['mean_distance']  # (10,)

    N = int(hamiltonians.shape[1])
    n_pairs = N * (N - 1) // 2
    print(f"Graph: {N} nodes, {adjacency.sum() // 2} edges")
    print(f"Tau range: [{all_tau[0]:.4f}, {all_tau[-1]:.4f}]")
    print(f"Occupation range: [{occ_bcs.min():.6f}, {occ_bcs.max():.6f}]")

    # ─── Select 10 tau values matching reference ──────────────────────────
    # Use same tau values as the reference S54 computation for direct comparison
    tau_target = np.linspace(0.0, 0.35, 10)
    tau_indices = [int(np.argmin(np.abs(all_tau - t))) for t in tau_target]
    tau_values = all_tau[np.array(tau_indices)]
    print(f"Tau values: {[f'{t:.4f}' for t in tau_values]}")

    # Verify these match reference tau values
    print(f"Ref tau values: {[f'{t:.4f}' for t in ref_tau]}")
    tau_match = np.allclose(tau_values, ref_tau, atol=0.01)
    print(f"Tau match with reference: {tau_match}")

    # ─── Diagnostics: occupation field ────────────────────────────────────
    print(f"\n{'='*70}")
    print("OCCUPATION FIELD DIAGNOSTICS")
    print(f"{'='*70}")

    all_F = np.zeros((len(tau_values), N))
    print(f"\n{'tau':>8s} | {'F_min':>10s} | {'F_max':>10s} | {'F_mean':>10s} | "
          f"{'F_std':>10s} | {'n_max':>8s} | {'n_min':>8s}")
    print("-" * 80)

    for t_idx, tau_idx in enumerate(tau_indices):
        evecs = eigenvectors[tau_idx]   # (32, 32)
        occ = occ_bcs[tau_idx]          # (32,)
        F = compute_occupation_field(evecs, occ)
        all_F[t_idx] = F

        print(f"{tau_values[t_idx]:8.4f} | {F.min():10.6f} | {F.max():10.6f} | "
              f"{F.mean():10.6f} | {F.std():10.6f} | "
              f"{occ.max():8.4f} | {occ.min():8.4f}")

    # ─── Validation ──────────────────────────────────────────────────────
    print(f"\n{'='*70}")
    print("VALIDATION CHECKS")
    print(f"{'='*70}")

    # Check 1: F_i > 0 at all tau
    F_min_global = all_F.min()
    print(f"F_i positivity: min(F) = {F_min_global:.2e} {'PASS' if F_min_global > 0 else 'FAIL'}")

    # Check 2: sum_i F_i = sum_k n_k (partition of occupation)
    for t_idx in range(len(tau_values)):
        F_sum = all_F[t_idx].sum()
        n_sum = occ_bcs[tau_indices[t_idx]].sum()
        print(f"  tau={tau_values[t_idx]:.4f}: sum(F)={F_sum:.6f}, sum(n_k)={n_sum:.6f}, "
              f"err={abs(F_sum - n_sum):.2e}")

    # Check 3: D_BCS is symmetric
    t0_idx = tau_indices[0]
    H0 = hamiltonians[t0_idx]
    F0 = all_F[0]
    D_BCS_0 = construct_D_BCS(H0, F0)
    sym_err = np.max(np.abs(D_BCS_0 - D_BCS_0.T))
    print(f"\nD_BCS symmetry at tau=0: max|D-D^T| = {sym_err:.2e} {'PASS' if sym_err < 1e-12 else 'FAIL'}")

    # Check 4: D_BCS is real
    print(f"D_BCS real: {np.isreal(D_BCS_0).all()}")

    # Check 5: D_BCS eigenvalues
    eigs_BCS = np.sort(np.linalg.eigvalsh(D_BCS_0))
    eigs_H = np.sort(np.linalg.eigvalsh(H0))
    print(f"\nEigenvalue comparison at tau=0:")
    print(f"  H:     [{eigs_H[0]:.4f}, ..., {eigs_H[-1]:.4f}], range={eigs_H[-1]-eigs_H[0]:.4f}")
    print(f"  D_BCS: [{eigs_BCS[0]:.4f}, ..., {eigs_BCS[-1]:.4f}], range={eigs_BCS[-1]-eigs_BCS[0]:.4f}")
    print(f"  D_BCS/H spectral ratio: {(eigs_BCS[-1]-eigs_BCS[0])/(eigs_H[-1]-eigs_H[0]):.4f}")

    # ─── Full computation ────────────────────────────────────────────────
    print(f"\n{'='*70}")
    print("CONNES DISTANCE COMPUTATION (D_BCS)")
    print(f"{'='*70}")

    all_dists_mat_BCS = np.zeros((len(tau_values), N, N))
    all_dists_flat_BCS = np.zeros((len(tau_values), n_pairs))
    mean_d_BCS = np.zeros(len(tau_values))
    max_d_BCS = np.zeros(len(tau_values))
    min_d_BCS = np.zeros(len(tau_values))
    std_d_BCS = np.zeros(len(tau_values))

    # Also store the occupation concentration metrics
    F_concentration = np.zeros(len(tau_values))  # std(F)/mean(F) = CV
    F_entropy = np.zeros(len(tau_values))  # Shannon entropy of F/sum(F)

    t_total = time.time()

    for t_idx, (tau_idx, tau) in enumerate(zip(tau_indices, tau_values)):
        print(f"\n--- tau = {tau:.4f} ({t_idx+1}/{len(tau_values)}) ---")

        # Construct D_BCS
        H = hamiltonians[tau_idx].copy()
        F = all_F[t_idx].copy()
        D_BCS = construct_D_BCS(H, F)

        # Extract off-diagonal for Connes distance
        D_off = D_BCS - np.diag(D_BCS.diagonal())

        # Occupation concentration metrics
        F_norm = F / F.sum()
        F_concentration[t_idx] = F.std() / F.mean()
        F_entropy[t_idx] = -np.sum(F_norm * np.log(F_norm + 1e-30))

        # Self-adjointness check
        assert np.allclose(D_BCS, D_BCS.T, atol=1e-12), f"D_BCS not symmetric at tau={tau}"

        t0 = time.time()
        dist_mat, dist_flat = compute_all_connes_distances(D_off, label=f"tau={tau:.3f}")
        elapsed = time.time() - t0

        all_dists_mat_BCS[t_idx] = dist_mat
        all_dists_flat_BCS[t_idx] = dist_flat

        nz = dist_flat[dist_flat > 1e-15]
        n_nan = np.isnan(dist_flat).sum()

        mean_d_BCS[t_idx] = np.nanmean(nz) if len(nz) > 0 else 0
        max_d_BCS[t_idx] = np.nanmax(nz) if len(nz) > 0 else 0
        min_d_BCS[t_idx] = np.nanmin(nz) if len(nz) > 0 else 0
        std_d_BCS[t_idx] = np.nanstd(nz) if len(nz) > 0 else 0

        print(f"  F: mean={F.mean():.6f}, std={F.std():.6f}, CV={F_concentration[t_idx]:.4f}")
        print(f"  D_BCS eigenrange: [{np.linalg.eigvalsh(D_BCS)[0]:.4f}, "
              f"{np.linalg.eigvalsh(D_BCS)[-1]:.4f}]")
        print(f"  <d_BCS> = {mean_d_BCS[t_idx]:.6f}, max = {max_d_BCS[t_idx]:.6f}")
        print(f"  NaN={n_nan}, Time={elapsed:.1f}s")

    t_total = time.time() - t_total
    print(f"\nTotal computation time: {t_total:.1f}s ({t_total/60:.1f} min)")

    # ─── Triangle inequality check ───────────────────────────────────────
    print(f"\n{'='*70}")
    print("METRIC AXIOM VERIFICATION (D_BCS)")
    print(f"{'='*70}")

    fold_idx_local = int(np.argmin(np.abs(tau_values - tau_fold)))
    D_fold_BCS = all_dists_mat_BCS[fold_idx_local]
    violations = 0
    max_violation = 0.0  # (local)
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                for a, b, c in [(i,j,k), (i,k,j), (j,k,i)]:
                    excess = D_fold_BCS[a,b] - D_fold_BCS[a,c] - D_fold_BCS[c,b]
                    if excess > 1e-10:
                        violations += 1
                        max_violation = max(max_violation, excess)
    print(f"Triangle inequality violations at fold: {violations}")
    print(f"Max violation: {max_violation:.2e}")
    metric_ok = (violations == 0)
    print(f"Metric status: {'TRUE METRIC' if metric_ok else 'FAILS METRIC AXIOM'}")

    # ─── Comparison with reference (unpaired) distances ──────────────────
    print(f"\n{'='*70}")
    print("COMPARISON: D_BCS vs D (unpaired)")
    print(f"{'='*70}")

    print(f"\n{'tau':>8s} | {'<d_BCS>':>10s} | {'<d_D>':>10s} | {'ratio':>8s} | "
          f"{'F_CV':>8s} | {'F_entropy':>10s}")
    print("-" * 70)
    for t_idx in range(len(tau_values)):
        # Find closest reference tau
        ref_idx = int(np.argmin(np.abs(ref_tau - tau_values[t_idx])))
        ratio = mean_d_BCS[t_idx] / ref_mean_d[ref_idx] if ref_mean_d[ref_idx] > 0 else np.nan
        print(f"{tau_values[t_idx]:8.4f} | {mean_d_BCS[t_idx]:10.6f} | "
              f"{ref_mean_d[ref_idx]:10.6f} | {ratio:8.4f} | "
              f"{F_concentration[t_idx]:8.4f} | {F_entropy[t_idx]:10.6f}")

    # ─── Monotonicity / minimum analysis ─────────────────────────────────
    print(f"\n{'='*70}")
    print("MONOTONICITY AND MINIMUM ANALYSIS")
    print(f"{'='*70}")

    diffs = np.diff(mean_d_BCS)
    mono_inc = np.all(diffs > 0)
    mono_dec = np.all(diffs < 0)

    print(f"<d_BCS> values: {[f'{v:.6f}' for v in mean_d_BCS]}")
    print(f"Differences: {[f'{v:+.6f}' for v in diffs]}")
    print(f"Monotone increasing: {mono_inc}")
    print(f"Monotone decreasing: {mono_dec}")

    has_minimum = False
    min_tau = None
    min_val = None
    min_depth = None

    if not mono_inc and not mono_dec:
        # Look for local minima
        for i in range(1, len(mean_d_BCS) - 1):
            if mean_d_BCS[i] < mean_d_BCS[i-1] and mean_d_BCS[i] < mean_d_BCS[i+1]:
                has_minimum = True
                min_tau = tau_values[i]
                min_val = mean_d_BCS[i]
                # Depth relative to endpoints
                min_depth = min(mean_d_BCS[i-1], mean_d_BCS[i+1]) - mean_d_BCS[i]
                print(f"\nLOCAL MINIMUM FOUND:")
                print(f"  tau = {min_tau:.4f}")
                print(f"  <d_BCS> = {min_val:.6f}")
                print(f"  depth = {min_depth:.6f}")
                print(f"  In gate range [0.10, 0.30]: "
                      f"{'YES' if 0.10 <= min_tau <= 0.30 else 'NO'}")

        if not has_minimum:
            # Check for a turn (sign change in differences)
            sign_changes = np.where(np.diff(np.sign(diffs)))[0]
            print(f"\nNo strict local minimum. Sign changes at indices: {sign_changes}")
            for sc in sign_changes:
                tau_sc = 0.5 * (tau_values[sc+1] + tau_values[sc+2])
                print(f"  Turn near tau ~ {tau_sc:.4f}")

    # Global minimum in the data
    global_min_idx = np.argmin(mean_d_BCS)
    print(f"\nGlobal minimum of <d_BCS>:")
    print(f"  Index: {global_min_idx}, tau = {tau_values[global_min_idx]:.4f}")
    print(f"  <d_BCS> = {mean_d_BCS[global_min_idx]:.6f}")
    if global_min_idx > 0:
        print(f"  Interior minimum: YES")
        in_gate_range = 0.10 <= tau_values[global_min_idx] <= 0.30
        print(f"  In gate range [0.10, 0.30]: {'YES' if in_gate_range else 'NO'}")
    else:
        print(f"  At boundary (tau=0): boundary minimum, not interior")

    # ─── Ratio analysis: d_BCS / d_D ─────────────────────────────────────
    print(f"\n{'='*70}")
    print("RATIO ANALYSIS: d_BCS / d_D")
    print(f"{'='*70}")

    ratios_BCS_D = np.zeros(len(tau_values))
    for t_idx in range(len(tau_values)):
        ref_idx = int(np.argmin(np.abs(ref_tau - tau_values[t_idx])))
        ratios_BCS_D[t_idx] = mean_d_BCS[t_idx] / ref_mean_d[ref_idx]

    print(f"Ratio <d_BCS>/<d_D>: {[f'{r:.4f}' for r in ratios_BCS_D]}")
    print(f"Ratio range: [{ratios_BCS_D.min():.4f}, {ratios_BCS_D.max():.4f}]")
    ratio_mono = np.all(np.diff(ratios_BCS_D) < 0) or np.all(np.diff(ratios_BCS_D) > 0)
    print(f"Ratio monotone: {ratio_mono}")

    # Check if ratio has a minimum (would indicate metric contraction relative to vacuum)
    ratio_diffs = np.diff(ratios_BCS_D)
    ratio_has_min = False
    for i in range(1, len(ratios_BCS_D) - 1):
        if ratios_BCS_D[i] < ratios_BCS_D[i-1] and ratios_BCS_D[i] < ratios_BCS_D[i+1]:
            ratio_has_min = True
            print(f"Ratio minimum at tau={tau_values[i]:.4f}: {ratios_BCS_D[i]:.4f}")

    # ─── Exponential fit ─────────────────────────────────────────────────
    from scipy.optimize import curve_fit

    def exp_model(tau, a, b):
        return a * np.exp(b * tau)

    try:
        popt_BCS, _ = curve_fit(exp_model, tau_values, mean_d_BCS, p0=[1.0, 3.0])
        fit_BCS = exp_model(tau_values, *popt_BCS)
        resid_BCS = mean_d_BCS - fit_BCS
        R2_BCS = 1 - np.sum(resid_BCS**2) / np.sum((mean_d_BCS - mean_d_BCS.mean())**2)
        print(f"\nExponential fit <d_BCS> = {popt_BCS[0]:.4f} * exp({popt_BCS[1]:.4f} * tau)")
        print(f"R^2 = {R2_BCS:.6f}")
    except Exception as e:
        print(f"Exponential fit failed: {e}")
        popt_BCS = None
        R2_BCS = None

    try:
        popt_D, _ = curve_fit(exp_model, ref_tau, ref_mean_d, p0=[1.0, 3.0])
        print(f"Reference fit <d_D> = {popt_D[0]:.4f} * exp({popt_D[1]:.4f} * tau)")
    except Exception:
        popt_D = None

    # ─── Gate verdict ────────────────────────────────────────────────────
    print(f"\n{'='*70}")
    print("GATE VERDICT: DBCS-CONNES-55")
    print(f"{'='*70}")

    gate_pass = False
    if has_minimum and min_tau is not None:
        if 0.10 <= min_tau <= 0.30:
            gate_pass = True
    elif global_min_idx > 0 and global_min_idx < len(tau_values) - 1:
        if 0.10 <= tau_values[global_min_idx] <= 0.30:
            gate_pass = True

    verdict = "PASS" if gate_pass else "FAIL"

    if gate_pass:
        detail = (f"<d_BCS>(tau) has minimum at tau={min_tau:.4f}, "
                  f"depth={min_depth:.6f}. "
                  f"<d_BCS>(0)={mean_d_BCS[0]:.4f}, "
                  f"<d_BCS>(fold)={mean_d_BCS[fold_idx_local]:.4f}, "
                  f"<d_BCS>(0.35)={mean_d_BCS[-1]:.4f}.")
    else:
        mono_str = "increasing" if mono_inc else ("decreasing" if mono_dec else "non-monotone but no interior min in [0.10,0.30]")
        detail = (f"<d_BCS>(tau) is {mono_str}. "
                  f"<d_BCS>(0)={mean_d_BCS[0]:.4f}, "
                  f"<d_BCS>(fold)={mean_d_BCS[fold_idx_local]:.4f}, "
                  f"<d_BCS>(0.35)={mean_d_BCS[-1]:.4f}. "
                  f"Global min at tau={tau_values[global_min_idx]:.4f}.")

    print(f"Verdict: {verdict}")
    print(f"Detail:  {detail}")

    # ─── Save ────────────────────────────────────────────────────────────
    print("\n--- Saving ---")
    save_dict = {
        'tau_values': tau_values,
        'tau_indices': np.array(tau_indices),
        'mean_distance_BCS': mean_d_BCS,
        'max_distance_BCS': max_d_BCS,
        'min_distance_BCS': min_d_BCS,
        'std_distance_BCS': std_d_BCS,
        'distances_BCS': all_dists_flat_BCS,
        'distance_matrix_BCS': all_dists_mat_BCS,
        'mean_distance_ref': ref_mean_d,
        'tau_ref': ref_tau,
        'ratio_BCS_D': ratios_BCS_D,
        'occupation_field': all_F,
        'F_concentration': F_concentration,
        'F_entropy': F_entropy,
        'N_cells': np.array(N),
        'n_pairs': np.array(n_pairs),
        'gate_name': np.array(['DBCS-CONNES-55']),
        'gate_verdict': np.array([verdict]),
        'gate_detail': np.array([detail]),
    }
    if has_minimum and min_tau is not None:
        save_dict['min_tau'] = np.array(min_tau)
        save_dict['min_value'] = np.array(min_val)
        save_dict['min_depth'] = np.array(min_depth)

    np.savez(OUTPUT_NPZ, **save_dict)
    print(f"Saved: {OUTPUT_NPZ}")

    # ─── Plot ────────────────────────────────────────────────────────────
    print("\n--- Plotting ---")
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle(f'DBCS-CONNES-55: State-Dependent Connes Distance  [{verdict}]',
                 fontsize=14, fontweight='bold')

    # Panel 1: Mean distances comparison
    ax = axes[0, 0]
    ax.plot(tau_values, mean_d_BCS, 'b-o', lw=2, ms=6, label=r'$\langle d_{\rm BCS} \rangle$')
    ax.fill_between(tau_values, min_d_BCS, max_d_BCS, alpha=0.1, color='blue')
    ax.plot(ref_tau, ref_mean_d, 'r-s', lw=2, ms=6, label=r'$\langle d_D \rangle$ (ref)')
    ax.axvline(tau_fold, color='gray', ls=':', alpha=0.7, label='fold')
    if has_minimum and min_tau is not None:
        ax.axvline(min_tau, color='green', ls='--', alpha=0.7, label=f'min at {min_tau:.3f}')
        ax.plot(min_tau, min_val, 'g*', ms=15, zorder=5)
    ax.set_xlabel(r'$\tau$')
    ax.set_ylabel('Mean Connes Distance')
    ax.set_title(r'$\langle d \rangle$ vs $\tau$: BCS vs Vacuum')
    ax.legend(fontsize=8, loc='best')
    ax.grid(True, alpha=0.3)

    # Panel 2: Ratio d_BCS / d_D
    ax = axes[0, 1]
    ax.plot(tau_values, ratios_BCS_D, 'g-o', lw=2, ms=6)
    ax.axhline(1.0, color='k', ls='-', alpha=0.3, label='ratio = 1')
    ax.axvline(tau_fold, color='gray', ls=':', alpha=0.7, label='fold')
    ax.set_xlabel(r'$\tau$')
    ax.set_ylabel(r'$\langle d_{\rm BCS} \rangle / \langle d_D \rangle$')
    ax.set_title('BCS / Vacuum Distance Ratio')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Panel 3: Occupation field concentration
    ax = axes[1, 0]
    ax2 = ax.twinx()
    l1 = ax.plot(tau_values, F_concentration, 'r-o', lw=2, ms=6, label='CV(F)')
    l2 = ax2.plot(tau_values, F_entropy, 'b-s', lw=2, ms=6, label=r'$S(F)$')
    ax.axvline(tau_fold, color='gray', ls=':', alpha=0.7)
    ax.set_xlabel(r'$\tau$')
    ax.set_ylabel('Concentration CV(F)', color='r')
    ax2.set_ylabel('Shannon Entropy S(F)', color='b')
    ax.set_title('Occupation Field Concentration')
    lines = l1 + l2
    labels = [l.get_label() for l in lines]
    ax.legend(lines, labels, fontsize=8, loc='best')
    ax.grid(True, alpha=0.3)

    # Panel 4: Distance matrices at tau=0 and fold
    ax = axes[1, 1]
    # Show ratio matrix at fold: d_BCS / d_D per pair
    ref_fold_idx = int(np.argmin(np.abs(ref_tau - tau_fold)))
    ref_fold_mat = ref_data['distance_matrix'][ref_fold_idx]
    bcs_fold_mat = all_dists_mat_BCS[fold_idx_local]

    # Ratio where both > 0
    ratio_mat = np.zeros_like(bcs_fold_mat)
    mask = ref_fold_mat > 1e-15
    ratio_mat[mask] = bcs_fold_mat[mask] / ref_fold_mat[mask]

    im = ax.imshow(ratio_mat, cmap='RdBu_r', aspect='equal',
                   vmin=0.5, vmax=2.0)
    plt.colorbar(im, ax=ax, label=r'$d_{\rm BCS}/d_D$ at fold')
    ax.set_xlabel('Cell index')
    ax.set_ylabel('Cell index')
    ax.set_title(rf'Per-pair BCS/Vacuum Ratio at $\tau={tau_values[fold_idx_local]:.2f}$')

    plt.tight_layout()
    plt.savefig(OUTPUT_PNG, dpi=150, bbox_inches='tight')
    print(f"Saved: {OUTPUT_PNG}")

    # ─── Final summary ───────────────────────────────────────────────────
    print(f"\n{'='*70}")
    print("SUMMARY")
    print(f"{'='*70}")
    print(f"Gate: DBCS-CONNES-55 -> {verdict}")
    print(f"<d_BCS>(tau=0.00)         = {mean_d_BCS[0]:.6f}")
    print(f"<d_BCS>(tau~{tau_values[fold_idx_local]:.2f}, fold) = {mean_d_BCS[fold_idx_local]:.6f}")
    print(f"<d_BCS>(tau=0.35)         = {mean_d_BCS[-1]:.6f}")
    print(f"<d_D>(tau=0.00)           = {ref_mean_d[0]:.6f} (ref)")
    print(f"<d_D>(tau~{ref_tau[int(np.argmin(np.abs(ref_tau - tau_fold)))]:.2f}, fold)  = "
          f"{ref_mean_d[int(np.argmin(np.abs(ref_tau - tau_fold)))]:.6f} (ref)")
    print(f"<d_D>(tau=0.35)           = {ref_mean_d[-1]:.6f} (ref)")
    print(f"BCS/D ratio range:         [{ratios_BCS_D.min():.4f}, {ratios_BCS_D.max():.4f}]")
    if has_minimum and min_tau is not None:
        print(f"Minimum at:                tau = {min_tau:.4f}")
        print(f"Minimum depth:             {min_depth:.6f}")
    else:
        print(f"No interior minimum found.")
    print(f"Monotone increasing:       {mono_inc}")
    print(f"Monotone decreasing:       {mono_dec}")
    print(f"Triangle inequality:       {'SATISFIED' if metric_ok else f'{violations} violations'}")
    if R2_BCS is not None:
        print(f"Exp fit: {popt_BCS[0]:.4f} * exp({popt_BCS[1]:.4f} * tau), R^2={R2_BCS:.6f}")
    print(f"Total time:                {t_total:.1f}s")
    print(f"\nOutputs: {OUTPUT_NPZ}, {OUTPUT_PNG}")


if __name__ == '__main__':
    main()
