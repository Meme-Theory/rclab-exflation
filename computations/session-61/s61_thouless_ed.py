#!/usr/bin/env python3
"""
s61_thouless_ed.py — THOULESS-GGE-61: Many-Body Thouless Time via Exact Diagonalization
========================================================================================

Gate: THOULESS-GGE-61
  PASS if t_Th > 10^3 * t_transit
  FAIL if t_Th < t_transit
  INFO if t_Th in [t_transit, 10^3 * t_transit]

Method:
  Construct the many-body BCS+Josephson Hamiltonian using direct Fock-state
  matrix element computation (no sparse kron). Diagonalize, extract level
  spacing at mid-spectrum, fit scaling with N_cell.

Context (Batch 1):
  PHONON-3: t_Th/t_transit = 65 from CG(24) single-particle spectral gap
  VOL-2:    t_Th/t_transit = 2625 from diffusive scaling E_Th = E_J/N^{2/3}

Session 61 | Hawking-Theorist
"""

import sys
import os
import time
import numpy as np
from scipy.linalg import eigh

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    E_cond, E_cond_ED_8mode, N_dof_BCS,
    E_B1, E_B2_mean, E_B3_mean,
    dt_transit, omega_tau, tau_fold,
    Delta_0_GL, Delta_0_OES,
)

# Load data
_dir = os.path.dirname(os.path.abspath(__file__))
s60_data = np.load(os.path.join(_dir, 's60_rg_integrals.npz'), allow_pickle=True)
E_J_fold = float(s60_data['E_J_fold'])          # 3.397 M_KK
eps_fold_8 = np.array(s60_data['eps_fold'])      # 8 single-particle energies
V_fold_8 = np.array(s60_data['V_fold'])          # 8x8 pairing matrix

s59_data = np.load(os.path.join(_dir, 's59_page_curve.npz'), allow_pickle=True)
E_GS_2cell_ref = float(s59_data['E_GS_2cell'])

t_transit = dt_transit  # 0.00113 M_KK^{-1}

print("=" * 72)
print("THOULESS-GGE-61: Many-Body Thouless Time via Exact Diagonalization")
print("=" * 72)
print(f"E_J = {E_J_fold:.4f} M_KK")
print(f"t_transit = {t_transit:.6f} M_KK^{{-1}}")
print(f"Gate: PASS if t_Th/t_tr > 10^3, FAIL if < 1, INFO if [1, 10^3]")
print()

# =============================================================================
# DIRECT FOCK-STATE HAMILTONIAN CONSTRUCTION
# =============================================================================
# For n_modes modes per cell and N_cell cells, total modes = n_modes * N_cell.
# Fock space dimension = 2^(n_modes * N_cell).
# Each Fock state = integer whose bits encode occupation numbers.
#
# This is FAR more efficient than nested kron products because we compute
# matrix elements directly from the bit representation.

def popcount(n):
    """Count number of set bits."""
    c = 0  # (local)
    while n:
        c += n & 1
        n >>= 1
    return c

def fermion_sign(state, pos):
    """
    Jordan-Wigner sign for acting on orbital 'pos' in Fock state 'state'.
    = (-1)^{number of occupied orbitals below pos}
    """
    mask = (1 << pos) - 1  # bits below pos
    return 1 - 2 * (popcount(state & mask) % 2)

def build_H_direct(n_modes, N_cell, eps, V_pair, E_J, adj):
    """
    Build the full many-body Hamiltonian by direct Fock-state matrix elements.

    Total orbitals: n_tot = n_modes * N_cell
    Fock space dim: 2^n_tot

    Orbital labeling: orbital (cell, mode) -> index = cell * n_modes + mode

    H = sum_i [ sum_k eps_k n_{k,i} + sum_{k!=k'} V_{kk'} n_{k,i} n_{k',i} ]
      + sum_{<ij>} [ -E_J sum_k (c^dag_{k,i} c_{k,j} + h.c.) ]
    """
    n_tot = n_modes * N_cell
    dim = 1 << n_tot  # 2^n_tot

    print(f"  Building H: n_modes={n_modes}, N_cell={N_cell}, n_tot={n_tot}, dim={dim}")
    sys.stdout.flush()

    # Diagonal part: kinetic + on-site interaction
    H_diag = np.zeros(dim)
    for state in range(dim):
        e = 0.0
        for cell in range(N_cell):
            for k in range(n_modes):
                orb = cell * n_modes + k
                if state & (1 << orb):
                    e += eps[k]
            # On-site pairing: V_{kk'} n_k n_{k'}
            for k in range(n_modes):
                orb_k = cell * n_modes + k
                if not (state & (1 << orb_k)):
                    continue
                for kp in range(k+1, n_modes):
                    orb_kp = cell * n_modes + kp
                    if state & (1 << orb_kp):
                        e += V_pair[k, kp] + V_pair[kp, k]
        H_diag[state] = e

    # Off-diagonal part: Josephson hopping
    # -E_J * (c^dag_{k,i} c_{k,j} + h.c.) for each bond (i,j) and mode k
    # c^dag_{k,i} c_{k,j} |state> : if orbital (j,k) occupied and (i,k) empty,
    #   result = sign * |state with (j,k)->0, (i,k)->1>

    # Collect COO data
    rows = []
    cols = []
    vals = []

    for i_cell in range(N_cell):
        for j_cell in range(i_cell + 1, N_cell):
            if adj[i_cell, j_cell] == 0:
                continue
            for k in range(n_modes):
                orb_i = i_cell * n_modes + k
                orb_j = j_cell * n_modes + k

                for state in range(dim):
                    # c^dag_{orb_i} c_{orb_j} |state>
                    # Need: orb_j occupied, orb_i empty
                    if (state & (1 << orb_j)) and not (state & (1 << orb_i)):
                        # Annihilate orb_j
                        sign_j = fermion_sign(state, orb_j)
                        state1 = state ^ (1 << orb_j)
                        # Create orb_i
                        sign_i = fermion_sign(state1, orb_i)
                        new_state = state1 | (1 << orb_i)
                        sign = sign_j * sign_i

                        rows.append(new_state)
                        cols.append(state)
                        vals.append(-E_J * sign)

                    # Hermitian conjugate: c^dag_{orb_j} c_{orb_i} |state>
                    if (state & (1 << orb_i)) and not (state & (1 << orb_j)):
                        sign_i2 = fermion_sign(state, orb_i)
                        state1 = state ^ (1 << orb_i)
                        sign_j2 = fermion_sign(state1, orb_j)
                        new_state = state1 | (1 << orb_j)
                        sign = sign_i2 * sign_j2

                        rows.append(new_state)
                        cols.append(state)
                        vals.append(-E_J * sign)

    # Build H — use sparse for large dims, dense for small
    if dim > 16384:
        from scipy.sparse import csr_matrix
        from scipy.sparse.linalg import eigsh
        # Build sparse
        diag_rows = list(range(dim))
        diag_cols = list(range(dim))
        diag_vals = list(H_diag)
        all_rows = diag_rows + rows + cols  # add transpose for symmetry
        all_cols = diag_cols + cols + rows
        all_vals = diag_vals + vals + vals
        H_sp = csr_matrix((all_vals, (all_rows, all_cols)), shape=(dim, dim))
        return H_sp, dim
    else:
        H = np.diag(H_diag)
        for r, c, v in zip(rows, cols, vals):
            H[r, c] += v
        H = 0.5 * (H + H.T)
        return H, dim


def chain_adjacency(N):
    """1D chain adjacency (open BC)."""
    adj = np.zeros((N, N), dtype=int)
    for i in range(N-1):
        adj[i, i+1] = 1
        adj[i+1, i] = 1
    return adj


def get_mode_subset(n_modes):
    """Select n_modes from the 8-mode spectrum."""
    if n_modes == 2:
        idx = [0, 7]  # 1 B2 (lowest) + 1 B3 (highest)
        label = "1B2+1B3"
    elif n_modes == 3:
        idx = [0, 1, 4]  # 2 B2 + 1 B1
        label = "2B2+1B1"
    elif n_modes == 4:
        idx = [0, 1, 4, 7]  # 2 B2 + 1 B1 + 1 B3
        label = "2B2+1B1+1B3"
    elif n_modes == 5:
        idx = [0, 1, 2, 4, 7]
        label = "3B2+1B1+1B3"
    elif n_modes == 8:
        idx = list(range(8))
        label = "4B2+1B1+3B3"
    else:
        idx = list(range(n_modes))
        label = f"lowest-{n_modes}"

    eps = eps_fold_8[idx]
    V = V_fold_8[np.ix_(idx, idx)]
    return eps, V, label


def extract_level_spacing(eigenvalues, fraction=0.4):
    """Extract mean/median level spacing near spectrum center."""
    N = len(eigenvalues)
    center = N // 2
    window = max(int(N * fraction / 2), 2)
    lo = max(center - window, 0)
    hi = min(center + window, N)

    central = eigenvalues[lo:hi]
    spacings = np.diff(central)
    # Remove any zero spacings (exact degeneracies)
    spacings_nz = spacings[spacings > 1e-14]

    if len(spacings_nz) == 0:
        return np.nan, np.nan, spacings

    return np.mean(spacings_nz), np.median(spacings_nz), spacings_nz


def wigner_dyson_r(spacings):
    """Compute <r> ratio for level statistics."""
    s = spacings[spacings > 1e-14]
    if len(s) < 3:
        return np.nan
    r_vals = np.minimum(s[:-1], s[1:]) / np.maximum(s[:-1], s[1:])
    return np.mean(r_vals)


# =============================================================================
# MAIN COMPUTATION
# =============================================================================

results = {}

print("=" * 72)
print("PHASE 1: Systematic scaling — n_modes = 2, 3, 4")
print("=" * 72)

# Maximum total orbital count for dense diag: 2^n_tot <= max_dim
# n_tot <= 16 => dim <= 65536 (comfortable for dense eigh)
# n_tot <= 18 => dim <= 262144 (about 512 MB for dense matrix, pushing it)
MAX_DIM = 65536

for n_modes in [2, 3, 4]:
    eps_sub, V_sub, mode_label = get_mode_subset(n_modes)
    dim_cell = 2**n_modes

    print(f"\n--- n_modes = {n_modes} ({mode_label}), dim_cell = {dim_cell} ---")
    print(f"  eps = {eps_sub}")

    # Find max N_cell
    max_N = 1
    while 2**(n_modes * (max_N + 1)) <= MAX_DIM:
        max_N += 1

    N_cells_list = list(range(2, max_N + 1))
    print(f"  N_cell range: {N_cells_list}")

    spacing_data = []

    for N_cell in N_cells_list:
        n_tot = n_modes * N_cell
        dim_total = 1 << n_tot
        adj = chain_adjacency(N_cell)

        t0 = time.time()
        H, dim = build_H_direct(n_modes, N_cell, eps_sub, V_sub, E_J_fold, adj)
        t_build = time.time() - t0

        t0 = time.time()
        if hasattr(H, 'toarray'):  # sparse
            from scipy.sparse.linalg import eigsh
            # Get eigenvalues near center of spectrum for level spacing
            # First get spectral bounds from a few extreme eigenvalues
            e_lo = eigsh(H, k=1, which='SA', return_eigenvectors=False)[0]
            e_hi = eigsh(H, k=1, which='LA', return_eigenvectors=False)[0]
            sigma = (e_lo + e_hi) / 2
            n_eigs = min(2000, dim - 2)
            evals = eigsh(H, k=n_eigs, sigma=sigma, return_eigenvectors=False)
            evals = np.sort(evals)
        else:
            evals = eigh(H, eigvals_only=True)
        t_diag = time.time() - t0

        delta_mean, delta_median, spacings = extract_level_spacing(evals)
        t_Th_mean = 1.0 / delta_mean if delta_mean > 0 and not np.isnan(delta_mean) else np.inf
        t_Th_median = 1.0 / delta_median if delta_median > 0 and not np.isnan(delta_median) else np.inf
        ratio_mean = t_Th_mean / t_transit
        ratio_median = t_Th_median / t_transit

        r_stat = wigner_dyson_r(spacings)

        print(f"  N={N_cell}: dim={dim}, delta_E={delta_mean:.6e}, "
              f"t_Th/t_tr={ratio_mean:.1f}, <r>={r_stat:.3f}, "
              f"build={t_build:.1f}s, diag={t_diag:.1f}s")
        sys.stdout.flush()

        spacing_data.append({
            'N_cell': N_cell,
            'dim': dim,
            'delta_mean': delta_mean,
            'delta_median': delta_median,
            't_Th_mean': t_Th_mean,
            't_Th_median': t_Th_median,
            'ratio_mean': ratio_mean,
            'ratio_median': ratio_median,
            'r_mean': r_stat,
            'E_GS': evals[0],
            'bandwidth': evals[-1] - evals[0],
        })

    results[f'n{n_modes}'] = {
        'n_modes': n_modes,
        'mode_label': mode_label,
        'eps': eps_sub,
        'V_diag': np.diag(V_sub),
        'data': spacing_data,
    }


# =============================================================================
# PHASE 2: Scaling Analysis
# =============================================================================

print("\n" + "=" * 72)
print("PHASE 2: Scaling Analysis")
print("=" * 72)

# Collect all data points for fitting
# For each n_modes, fit log(delta_E) vs N_cell and vs log(dim)

fits = {}
for key in ['n2', 'n3', 'n4']:
    if key not in results or len(results[key]['data']) < 2:
        continue
    r = results[key]
    N_arr = np.array([d['N_cell'] for d in r['data']])
    delta_arr = np.array([d['delta_mean'] for d in r['data']])
    dim_arr = np.array([d['dim'] for d in r['data']])
    bw_arr = np.array([d['bandwidth'] for d in r['data']])

    valid = (delta_arr > 0) & ~np.isnan(delta_arr)
    if np.sum(valid) < 2:
        continue

    # Fit: log(delta) = a + b*N
    log_delta = np.log(delta_arr[valid])
    N_v = N_arr[valid]
    coeffs_N = np.polyfit(N_v, log_delta, 1)
    alpha_exp = -coeffs_N[0]

    # Fit: log(delta) = a + b*log(dim)
    log_dim = np.log(dim_arr[valid])
    coeffs_dim = np.polyfit(log_dim, log_delta, 1)
    gamma = -coeffs_dim[0]

    # Expected from random matrix theory: delta ~ W/dim, so gamma = 1
    # Expected slope in N: -n_modes * ln(2)
    expected_slope_N = -r['n_modes'] * np.log(2)

    print(f"\n{key} (n_modes={r['n_modes']}):")
    print(f"  Exponential: delta ~ exp(-{alpha_exp:.4f}*N)")
    print(f"    Expected slope = {expected_slope_N:.4f}, measured = {coeffs_N[0]:.4f}")
    print(f"    Ratio measured/expected = {coeffs_N[0]/expected_slope_N:.4f}")
    print(f"  Power law: delta ~ dim^(-{gamma:.4f})")
    print(f"    Expected (RMT): gamma = 1.0, measured = {gamma:.4f}")
    print(f"  Bandwidth: {bw_arr}")

    # Extrapolate to N=32 (framework fabric)
    log_delta_32 = coeffs_N[0] * 32 + coeffs_N[1]
    delta_32 = np.exp(log_delta_32)
    t_Th_32 = 1.0 / delta_32
    ratio_32 = t_Th_32 / t_transit

    print(f"  Extrapolation to N=32:")
    print(f"    delta_E(32) ~ {delta_32:.2e}")
    print(f"    t_Th(32) / t_transit ~ {ratio_32:.2e}")

    fits[key] = {
        'alpha_exp': alpha_exp,
        'gamma': gamma,
        'coeffs_N': coeffs_N,
        'coeffs_dim': coeffs_dim,
        'expected_slope': expected_slope_N,
        'ratio_32': ratio_32,
        'delta_32': delta_32,
    }


# =============================================================================
# PHASE 3: Cross-Checks
# =============================================================================

print("\n" + "=" * 72)
print("PHASE 3: Cross-Checks")
print("=" * 72)

# Single-particle Thouless (PHONON-3 result)
E_Th_sp = E_J_fold * 4  # spectral gap of CG(24) = 4
t_Th_sp = 1.0 / E_Th_sp
print(f"\nSingle-particle (PHONON-3): t_Th = {t_Th_sp:.6f}, ratio = {t_Th_sp/t_transit:.1f}")

# Compare with many-body at N=2
for key in ['n2', 'n3', 'n4']:
    if key in results and results[key]['data']:
        d = results[key]['data'][0]
        print(f"Many-body ({key}, N=2): t_Th = {d['t_Th_mean']:.6f}, ratio = {d['ratio_mean']:.1f}")

# Level statistics summary
print(f"\nLevel statistics:")
print(f"  GOE: <r> = 0.536 | Poisson: <r> = 0.386")
for key in ['n2', 'n3', 'n4']:
    if key in results:
        for d in results[key]['data']:
            stat = "GOE" if d['r_mean'] > 0.46 else ("Poisson" if d['r_mean'] < 0.42 else "inter")
            print(f"  {key} N={d['N_cell']}: <r>={d['r_mean']:.3f} ({stat})")


# =============================================================================
# GATE VERDICT
# =============================================================================

print("\n" + "=" * 72)
print("GATE VERDICT: THOULESS-GGE-61")
print("=" * 72)

# Use n_modes=3 as primary (best resolution per data point)
# Fall back to n_modes=2 if n3 insufficient
best_key = 'n3' if 'n3' in fits else ('n4' if 'n4' in fits else 'n2')
best_fit = fits.get(best_key, fits.get('n2', {}))

if best_fit:
    ratio_32 = best_fit['ratio_32']
    alpha_exp = best_fit['alpha_exp']
    gamma = best_fit['gamma']

    # Direct ED results at largest computed N
    best_data = results[best_key]['data']
    last = best_data[-1]
    ratio_direct = last['ratio_mean']
    N_last = last['N_cell']

    if ratio_32 > 1e3:
        verdict = "PASS"
    elif ratio_32 > 1:
        verdict = "INFO"
    else:
        verdict = "FAIL"

    # Also check: does the scaling itself make sense?
    # RMT says gamma ~ 1 (delta ~ W/dim). If we get gamma << 1, something is wrong.
    gamma_comment = ""
    if gamma < 0.5:
        gamma_comment = f" WARNING: gamma={gamma:.3f} < 0.5, scaling slower than RMT."
    elif gamma > 1.5:
        gamma_comment = f" NOTE: gamma={gamma:.3f} > 1, faster than RMT (likely conserved charges)."

    verdict_detail = (
        f"Many-body ED ({best_key}, n_modes={results[best_key]['n_modes']}): "
        f"delta_E ~ exp(-{alpha_exp:.3f}*N) ~ dim^(-{gamma:.3f}). "
        f"Direct ED at N={N_last}: t_Th/t_tr={ratio_direct:.1f}. "
        f"Extrapolated N=32: t_Th/t_tr ~ {ratio_32:.1e}.{gamma_comment}"
    )
else:
    verdict = "INFO"
    verdict_detail = "Insufficient data for scaling fit."

print(f"\nVerdict: {verdict}")
print(f"Detail: {verdict_detail}")

# Consistency check with Batch 1
print(f"\n--- Consistency with Batch 1 ---")
print(f"PHONON-3 (CG24 spectral gap): t_Th/t_tr = 65")
print(f"VOL-2 (diffusive N^{{2/3}}):     t_Th/t_tr = 2625 (at N=32)")
print(f"HAWK-2 (many-body ED):          t_Th/t_tr = {ratio_32:.1e} (at N=32, extrapolated)")
print(f"\nKey difference: Many-body t_Th includes EXPONENTIAL Hilbert space growth.")
print(f"Single-particle estimates miss this entirely.")


# =============================================================================
# SAVE
# =============================================================================

save_path = os.path.join(_dir, 's61_thouless_ed.npz')

save_dict = {
    'gate_name': np.array(['THOULESS-GGE-61']),
    'gate_verdict': np.array([verdict]),
    'gate_detail': np.array([verdict_detail[:200]]),
    'E_J': E_J_fold,
    't_transit': t_transit,
    'eps_fold_8': eps_fold_8,
}

for key in ['n2', 'n3', 'n4']:
    if key in results:
        r = results[key]
        save_dict[f'{key}_n_modes'] = r['n_modes']
        save_dict[f'{key}_mode_label'] = np.array([r['mode_label']])
        save_dict[f'{key}_eps'] = r['eps']
        save_dict[f'{key}_N_cells'] = np.array([d['N_cell'] for d in r['data']])
        save_dict[f'{key}_dims'] = np.array([d['dim'] for d in r['data']])
        save_dict[f'{key}_delta_mean'] = np.array([d['delta_mean'] for d in r['data']])
        save_dict[f'{key}_delta_median'] = np.array([d['delta_median'] for d in r['data']])
        save_dict[f'{key}_ratio_mean'] = np.array([d['ratio_mean'] for d in r['data']])
        save_dict[f'{key}_ratio_median'] = np.array([d['ratio_median'] for d in r['data']])
        save_dict[f'{key}_r_mean'] = np.array([d['r_mean'] for d in r['data']])
        save_dict[f'{key}_E_GS'] = np.array([d['E_GS'] for d in r['data']])
        save_dict[f'{key}_bandwidth'] = np.array([d['bandwidth'] for d in r['data']])

for key in ['n2', 'n3', 'n4']:
    if key in fits:
        f = fits[key]
        save_dict[f'{key}_alpha_exp'] = f['alpha_exp']
        save_dict[f'{key}_gamma'] = f['gamma']
        save_dict[f'{key}_ratio_32'] = f['ratio_32']
        save_dict[f'{key}_delta_32'] = f['delta_32']

np.savez(save_path, **save_dict)
print(f"\nSaved: {save_path}")


# =============================================================================
# PLOT
# =============================================================================

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('THOULESS-GGE-61: Many-Body Thouless Time via Exact Diagonalization\n'
             f'Gate: {verdict}', fontsize=13, fontweight='bold')

markers = {'n2': 'o', 'n3': 's', 'n4': 'D'}
colors = {'n2': 'tab:blue', 'n3': 'tab:red', 'n4': 'tab:green'}

# Panel 1: t_Th / t_transit vs N_cell
ax = axes[0, 0]
for key in ['n2', 'n3', 'n4']:
    if key in results and results[key]['data']:
        r = results[key]
        N_v = [d['N_cell'] for d in r['data']]
        rat_v = [d['ratio_mean'] for d in r['data']]
        ax.semilogy(N_v, rat_v, markers[key] + '-', color=colors[key],
                    label=f"n={r['n_modes']} ({r['mode_label']})", markersize=8)

ax.axhline(y=1000, color='green', ls='--', alpha=0.7, label='PASS (10$^3$)')
ax.axhline(y=1, color='red', ls='--', alpha=0.7, label='FAIL (1)')
ax.set_xlabel('$N_{\\mathrm{cell}}$')
ax.set_ylabel('$t_{\\mathrm{Th}} / t_{\\mathrm{transit}}$')
ax.set_title('Many-Body Thouless Ratio')
ax.legend(fontsize=7)
ax.grid(True, alpha=0.3)

# Panel 2: delta_E vs dim
ax = axes[0, 1]
for key in ['n2', 'n3', 'n4']:
    if key in results and results[key]['data']:
        r = results[key]
        dm = [d['dim'] for d in r['data']]
        de = [d['delta_mean'] for d in r['data']]
        ax.loglog(dm, de, markers[key] + '-', color=colors[key],
                  label=f"n={r['n_modes']}", markersize=8)

# dim^{-1} reference
all_dm = []
all_de = []
for key in ['n2', 'n3', 'n4']:
    if key in results:
        for d in results[key]['data']:
            if d['delta_mean'] > 0:
                all_dm.append(d['dim'])
                all_de.append(d['delta_mean'])
if all_dm:
    d_ref = np.logspace(np.log10(min(all_dm)), np.log10(max(all_dm)), 50)
    # Normalized to first n2 point
    if results.get('n2', {}).get('data'):
        ref = results['n2']['data'][0]
        ax.loglog(d_ref, ref['delta_mean'] * (ref['dim'] / d_ref), 'k--', alpha=0.4,
                  label='$\\sim \\mathrm{dim}^{-1}$ (RMT)')

ax.set_xlabel('Hilbert space dimension')
ax.set_ylabel('$\\delta E$ (M$_{\\mathrm{KK}}$)')
ax.set_title('Level Spacing vs Dimension')
ax.legend(fontsize=7)
ax.grid(True, alpha=0.3)

# Panel 3: <r> statistic
ax = axes[1, 0]
for key in ['n2', 'n3', 'n4']:
    if key in results and results[key]['data']:
        r = results[key]
        N_v = [d['N_cell'] for d in r['data']]
        r_v = [d['r_mean'] for d in r['data']]
        ax.plot(N_v, r_v, markers[key] + '-', color=colors[key],
                label=f"n={r['n_modes']}", markersize=8)

ax.axhline(y=0.536, color='orange', ls='--', alpha=0.7, label='GOE')
ax.axhline(y=0.386, color='purple', ls='--', alpha=0.7, label='Poisson')
ax.set_xlabel('$N_{\\mathrm{cell}}$')
ax.set_ylabel('$\\langle r \\rangle$')
ax.set_title('Level Statistics')
ax.legend(fontsize=7)
ax.grid(True, alpha=0.3)
ax.set_ylim(0.25, 0.65)

# Panel 4: Extrapolation with fit
ax = axes[1, 1]
if 'n2' in fits:
    f = fits['n2']
    N_plot = np.array([d['N_cell'] for d in results['n2']['data']])
    r_plot = np.array([d['ratio_mean'] for d in results['n2']['data']])
    ax.semilogy(N_plot, r_plot, 'o-', color='tab:blue', label='ED data (n=2)', ms=8)

    N_ext = np.arange(2, 35)
    r_ext = np.exp(f['coeffs_N'][0] * N_ext + f['coeffs_N'][1]) / t_transit
    ax.semilogy(N_ext, r_ext, '--', color='gray', alpha=0.7,
                label=f'Fit: $\\exp({f["alpha_exp"]:.2f} \\cdot N)$')

    ax.axhline(y=1e3, color='green', ls='--', alpha=0.7, label='PASS')
    ax.axhline(y=1, color='red', ls='--', alpha=0.7, label='FAIL')
    ax.set_xlabel('$N_{\\mathrm{cell}}$')
    ax.set_ylabel('$t_{\\mathrm{Th}} / t_{\\mathrm{transit}}$')
    ax.set_title(f'Extrapolation: $t_{{Th}}/t_{{tr}}(32) \\sim {f["ratio_32"]:.0e}$')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(1, 34)

plt.tight_layout()
plot_path = os.path.join(_dir, 's61_thouless_ed.png')
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
print(f"Saved: {plot_path}")

print("\n" + "=" * 72)
print("COMPLETE")
print("=" * 72)
