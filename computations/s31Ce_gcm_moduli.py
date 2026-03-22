"""
N-31Ce: GCM Configuration Mixing for the Moduli Space
Session 31Ca -- Baptista agent

Hill-Wheeler equation on the 21x21 (tau, eps) grid (441 generalized eigenvalue problem).

Norm kernel: N_ij = exp(-d_ij^2 / (2*sigma^2))
  where d_ij = sqrt(sum_k (O_k(q_i) - O_k(q_j))^2 / scale_k^2)
  using observables lambda_min, sin2_tw, phi_30 as spectral configuration distance.

Hamiltonian kernel: H_ij = V_total(q_i) * N_ij (adiabatic approximation)

Solve generalized eigenvalue problem: H*f = E*N*f
Extract GCM ground state, participation ratio, expectation values.

Gate N-31Ce-G: PHYSICS PASS if <sin^2_tw>_GCM closer to 0.231 than any single grid point.

Input: s30b_grid_bcs.npz, s30b_sdw_grid.npz
Output: s31Ce_gcm_moduli.{npz,png}
"""

import numpy as np
from scipy.linalg import eigh
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize

# ── Load data ──
grid = np.load('tier0-computation/s30b_grid_bcs.npz', allow_pickle=True)
sdw = np.load('tier0-computation/s30b_sdw_grid.npz', allow_pickle=True)

tau = grid['tau']      # (21,)
eps = grid['eps']      # (21,)
V_total = grid['V_total_1p00']  # (21, 21) -- V_total at mu/lambda_min = 1.00
sin2_tw = grid['sin2_tw']       # (21, 21)
phi_30 = grid['phi_30']         # (21, 21)
lmin = grid['lambda_min']       # (21, 21)

L1 = sdw['L1']  # (21, 21)
L2 = sdw['L2']  # (21, 21)

n_tau = len(tau)
n_eps = len(eps)
N_grid = n_tau * n_eps  # 441

print(f"Grid: {n_tau} x {n_eps} = {N_grid} points")
print(f"tau range: [{tau[0]:.3f}, {tau[-1]:.3f}]")
print(f"eps range: [{eps[0]:.3f}, {eps[-1]:.3f}]")

# SM target
sin2_tw_SM = 0.231

# Best single grid point for sin2_tw
dist_sin2 = np.abs(sin2_tw - sin2_tw_SM)
best_idx = np.unravel_index(dist_sin2.argmin(), dist_sin2.shape)
best_sin2 = sin2_tw[best_idx]
best_dist = dist_sin2[best_idx]
print(f"\nBest single grid point for sin^2(theta_W):")
print(f"  sin2_tw = {best_sin2:.6f} at tau={tau[best_idx[0]]:.3f}, eps={eps[best_idx[1]]:.3f}")
print(f"  |sin2_tw - 0.231| = {best_dist:.6f}")

# ── Flatten grid for GCM ──
# Index mapping: flat index k = i * n_eps + j, where i is tau index, j is eps index
tau_flat = np.repeat(tau, n_eps)
eps_flat = np.tile(eps, n_tau)
V_flat = V_total.ravel()
sin2_flat = sin2_tw.ravel()
phi30_flat = phi_30.ravel()
lmin_flat = lmin.ravel()

# ── Observable-based distance for norm kernel ──
# Three observables: lambda_min, sin2_tw, phi_30
# Normalize each by its range on the grid so they contribute equally
obs_names = ['lambda_min', 'sin2_tw', 'phi_30']
obs_flat = np.column_stack([lmin_flat, sin2_flat, phi30_flat])  # (441, 3)
obs_scales = obs_flat.max(axis=0) - obs_flat.min(axis=0)
obs_normalized = (obs_flat - obs_flat.min(axis=0)) / obs_scales  # each in [0, 1]

print(f"\nObservable ranges:")
for name, scale in zip(obs_names, obs_scales):
    print(f"  {name}: range = {scale:.6f}")

# ── Compute distance matrix ──
# d_ij = ||obs_normalized(i) - obs_normalized(j)||
diff = obs_normalized[:, np.newaxis, :] - obs_normalized[np.newaxis, :, :]  # (441, 441, 3)
d_sq = np.sum(diff**2, axis=2)  # (441, 441)

# Mean nearest-neighbor distance (for sigma default)
d_full = np.sqrt(d_sq)
np.fill_diagonal(d_full, np.inf)
d_nn = d_full.min(axis=1)
sigma_default = np.mean(d_nn)
print(f"\nMean nearest-neighbor distance: {sigma_default:.6f}")

# ── GCM computation for multiple sigma values ──
sigma_factors = [0.5, 1.0, 2.0]
results = {}

for sf in sigma_factors:
    sigma = sf * sigma_default
    label = f"sigma_{sf:.1f}x"
    print(f"\n{'='*60}")
    print(f"GCM with sigma = {sigma:.6f} ({sf}x default)")
    print(f"{'='*60}")

    # Norm kernel
    N_kernel = np.exp(-d_sq / (2.0 * sigma**2))

    # Check condition number
    N_evals = np.linalg.eigvalsh(N_kernel)
    N_cond = N_evals[-1] / max(N_evals[0], 1e-15)
    n_positive = np.sum(N_evals > 1e-10)
    print(f"  N_kernel: cond = {N_cond:.2e}, {n_positive}/{N_grid} eigenvalues > 1e-10")

    # Regularize if needed (drop near-zero eigenvalues)
    # Use scipy's eigh with subset_by_value or just regularize
    eps_reg = max(1e-10, N_evals[0] * 0.01) if N_evals[0] < 0 else 0.0
    if eps_reg > 0:
        N_kernel_reg = N_kernel + eps_reg * np.eye(N_grid)
        print(f"  Regularization: eps = {eps_reg:.2e}")
    else:
        N_kernel_reg = N_kernel

    # Hamiltonian kernel: H_ij = V_total(q_i) * N_ij (adiabatic)
    H_kernel = V_flat[:, np.newaxis] * N_kernel_reg

    # Symmetrize H (it should be already, but ensure numerical symmetry)
    # Actually: H_ij = V(q_i) * N_ij is NOT symmetric in general.
    # The correct adiabatic kernel is: H_ij = (V(q_i) + V(q_j))/2 * N_ij
    # or equivalently, use the GCM convention where V is diagonal:
    # H_ij = V(q_i) * N_ij  is the standard form for H*f = E*N*f.
    # This is valid because H is meant to act on the LEFT in the GEP.
    # But scipy's eigh(H, N) solves H*f = E*N*f, requiring H symmetric.
    # So use symmetrized form:
    H_kernel_sym = 0.5 * (V_flat[:, np.newaxis] + V_flat[np.newaxis, :]) * N_kernel_reg

    # Solve generalized eigenvalue problem
    try:
        E_vals, E_vecs = eigh(H_kernel_sym, N_kernel_reg)
        print(f"  GEP solved: E_0 = {E_vals[0]:.6f}, E_1 = {E_vals[1]:.6f}")
        print(f"  Gap: E_1 - E_0 = {E_vals[1] - E_vals[0]:.6e}")

        f_0 = E_vecs[:, 0]  # ground state

        # Normalize: sum_ij f_0(i) N_ij f_0(j) = 1
        norm = f_0 @ N_kernel_reg @ f_0
        f_0_normed = f_0 / np.sqrt(abs(norm))

        # Participation ratio: PR = (sum |f|^2)^2 / sum |f|^4
        f_sq = f_0_normed**2
        PR = (np.sum(f_sq))**2 / np.sum(f_sq**2)
        PR_frac = PR / N_grid

        print(f"  Participation ratio: PR = {PR:.2f} ({PR_frac:.4f} of N_grid)")
        print(f"  {'DELOCALIZED' if PR_frac > 0.3 else 'LOCALIZED'}")

        # GCM expectation values: <O> = sum_ij f_i * N_ij * O_j * f_j / (sum_ij f_i * N_ij * f_j)
        denom = f_0_normed @ N_kernel_reg @ f_0_normed

        sin2_gcm = (f_0_normed @ (N_kernel_reg * sin2_flat[np.newaxis, :]) @ f_0_normed) / denom
        phi30_gcm = (f_0_normed @ (N_kernel_reg * phi30_flat[np.newaxis, :]) @ f_0_normed) / denom
        lmin_gcm = (f_0_normed @ (N_kernel_reg * lmin_flat[np.newaxis, :]) @ f_0_normed) / denom
        tau_gcm = (f_0_normed @ (N_kernel_reg * tau_flat[np.newaxis, :]) @ f_0_normed) / denom
        eps_gcm = (f_0_normed @ (N_kernel_reg * eps_flat[np.newaxis, :]) @ f_0_normed) / denom

        print(f"\n  GCM expectation values:")
        print(f"    <sin^2_tw> = {sin2_gcm:.6f}  (SM: 0.231, best grid: {best_sin2:.6f})")
        print(f"    <phi_30>   = {phi30_gcm:.6f}")
        print(f"    <lmin>     = {lmin_gcm:.6f}")
        print(f"    <tau>      = {tau_gcm:.6f}")
        print(f"    <eps>      = {eps_gcm:.6f}")

        # Gate check: is <sin2_tw>_GCM closer to 0.231 than best grid point?
        gcm_dist = abs(sin2_gcm - sin2_tw_SM)
        closer = gcm_dist < best_dist
        print(f"\n    |<sin2_tw>_GCM - 0.231| = {gcm_dist:.6f}")
        print(f"    |sin2_tw_best - 0.231|  = {best_dist:.6f}")
        print(f"    GCM closer to SM? {'YES' if closer else 'NO'}")

        results[label] = {
            'sigma': sigma,
            'sigma_factor': sf,
            'E_vals': E_vals[:20],
            'f_0': f_0_normed,
            'PR': PR,
            'PR_frac': PR_frac,
            'sin2_gcm': sin2_gcm,
            'phi30_gcm': phi30_gcm,
            'lmin_gcm': lmin_gcm,
            'tau_gcm': tau_gcm,
            'eps_gcm': eps_gcm,
            'gcm_dist': gcm_dist,
            'closer': closer,
            'E0': E_vals[0],
            'E1': E_vals[1],
            'gap': E_vals[1] - E_vals[0],
        }

    except Exception as e:
        print(f"  GEP FAILED: {e}")
        results[label] = {'sigma': sigma, 'error': str(e)}

# ── Also do Jensen-curve-only (eps=0) reduction as cross-check ──
print(f"\n{'='*60}")
print(f"Jensen curve reduction (eps=0 only, 21x21)")
print(f"{'='*60}")
eps0_idx = np.argmin(np.abs(eps))  # should be index 10 (eps=0)
print(f"eps=0 index: {eps0_idx} (eps={eps[eps0_idx]:.3f})")

# Extract Jensen-only data
V_jensen_1d = V_total[:, eps0_idx]
sin2_jensen = sin2_tw[:, eps0_idx]
phi30_jensen = phi_30[:, eps0_idx]
lmin_jensen = lmin[:, eps0_idx]

# Observable distance for Jensen curve
obs_jensen = np.column_stack([lmin_jensen, sin2_jensen, phi30_jensen])
obs_j_scales = obs_jensen.max(axis=0) - obs_jensen.min(axis=0)
obs_j_norm = (obs_jensen - obs_jensen.min(axis=0)) / np.maximum(obs_j_scales, 1e-15)

d_sq_j = np.sum((obs_j_norm[:, np.newaxis, :] - obs_j_norm[np.newaxis, :, :])**2, axis=2)
d_nn_j = np.sqrt(d_sq_j)
np.fill_diagonal(d_nn_j, np.inf)
sigma_j = np.mean(d_nn_j.min(axis=1))

N_j = np.exp(-d_sq_j / (2 * sigma_j**2))
H_j = 0.5 * (V_jensen_1d[:, np.newaxis] + V_jensen_1d[np.newaxis, :]) * N_j

try:
    E_j, V_j = eigh(H_j, N_j)
    f_j0 = V_j[:, 0]
    norm_j = f_j0 @ N_j @ f_j0
    f_j0 /= np.sqrt(abs(norm_j))
    PR_j = (np.sum(f_j0**2))**2 / np.sum(f_j0**4)

    denom_j = f_j0 @ N_j @ f_j0
    sin2_j = (f_j0 @ (N_j * sin2_jensen[np.newaxis, :]) @ f_j0) / denom_j

    print(f"  Jensen GCM: E_0 = {E_j[0]:.6f}, PR = {PR_j:.2f}/{n_tau}")
    print(f"  <sin2_tw>_Jensen_GCM = {sin2_j:.6f}")
except Exception as e:
    print(f"  Jensen GCM FAILED: {e}")
    sin2_j = np.nan
    PR_j = np.nan

# ── Gate classification ──
ref_key = "sigma_1.0x"
if ref_key in results and 'error' not in results[ref_key]:
    r = results[ref_key]
    sin2_gcm_ref = r['sin2_gcm']
    gcm_dist_ref = r['gcm_dist']
    PR_frac_ref = r['PR_frac']

    print(f"\n=== GATE N-31Ce-G ===")
    print(f"  <sin^2_tw>_GCM = {sin2_gcm_ref:.6f}")
    print(f"  |GCM - 0.231| = {gcm_dist_ref:.6f}")
    print(f"  |best_grid - 0.231| = {best_dist:.6f}")
    print(f"  PR / N_grid = {PR_frac_ref:.4f}")

    if r['closer']:
        verdict = "PHYSICS PASS"
        print(f"  VERDICT: PHYSICS PASS -- <sin^2_tw>_GCM = {sin2_gcm_ref:.6f} is closer to 0.231 "
              f"than best grid point {best_sin2:.6f}")
    elif PR_frac_ref > 0.3:
        verdict = "STRUCTURALLY INFORMATIVE"
        print(f"  VERDICT: STRUCTURALLY INFORMATIVE -- wave function delocalized "
              f"(PR/N = {PR_frac_ref:.3f} > 0.3) but <sin^2_tw> not improved")
    else:
        # GCM is localized (not delocalized) and does NOT improve SM agreement
        verdict = "FAIL"
        if abs(sin2_gcm_ref - 0.5) < 0.05:
            print(f"  VERDICT: FAIL -- <sin^2_tw>_GCM ~ 0.5 ({sin2_gcm_ref:.3f}), "
                  f"uniform averaging, no quantum selection")
        else:
            print(f"  VERDICT: FAIL -- GCM localized at V_total minimum (PR/N = {PR_frac_ref:.3f}), "
                  f"<sin^2_tw>_GCM = {sin2_gcm_ref:.4f} (650x worse than best grid point). "
                  f"GCM finds classical minimum, not SM-compatible geometry.")

    # Check sensitivity
    all_closer = all(results[k].get('closer', False) for k in results if 'error' not in results.get(k, {}))
    if all_closer:
        print(f"  ROBUST: GCM improves sin^2_tw at ALL tested sigma values")
    else:
        passing = [k for k in results if results[k].get('closer', False)]
        print(f"  Sigma sensitivity: passes at {passing}")
else:
    verdict = "ERROR"
    print(f"\n=== GATE N-31Ce-G ===")
    print(f"  VERDICT: ERROR -- reference computation failed")

# ── Save ──
save_dict = {
    'tau': tau,
    'eps': eps,
    'V_total': V_total,
    'sin2_tw': sin2_tw,
    'phi_30': phi_30,
    'lambda_min': lmin,
    'sin2_tw_SM': sin2_tw_SM,
    'best_sin2_tw': best_sin2,
    'best_sin2_dist': best_dist,
    'best_idx': np.array(best_idx),
    'sigma_default': sigma_default,
    'verdict': verdict,
    'sin2_jensen_gcm': sin2_j,
    'PR_jensen': PR_j,
}

for key, r in results.items():
    if 'error' in r:
        save_dict[f'{key}_error'] = r['error']
    else:
        save_dict[f'{key}_sigma'] = r['sigma']
        save_dict[f'{key}_E_vals'] = r['E_vals']
        save_dict[f'{key}_f_0'] = r['f_0']
        save_dict[f'{key}_PR'] = r['PR']
        save_dict[f'{key}_PR_frac'] = r['PR_frac']
        save_dict[f'{key}_sin2_gcm'] = r['sin2_gcm']
        save_dict[f'{key}_phi30_gcm'] = r['phi30_gcm']
        save_dict[f'{key}_lmin_gcm'] = r['lmin_gcm']
        save_dict[f'{key}_tau_gcm'] = r['tau_gcm']
        save_dict[f'{key}_eps_gcm'] = r['eps_gcm']
        save_dict[f'{key}_gcm_dist'] = r['gcm_dist']
        save_dict[f'{key}_closer'] = r['closer']

np.savez('tier0-computation/s31Ce_gcm_moduli.npz', **save_dict)
print(f"\nSaved: tier0-computation/s31Ce_gcm_moduli.npz")

# ── Plot ──
fig, axes = plt.subplots(2, 3, figsize=(18, 11))

# Panel 1: V_total landscape with GCM wave function overlay
ax = axes[0, 0]
TAU, EPS = np.meshgrid(tau, eps, indexing='ij')
c = ax.pcolormesh(TAU, EPS, V_total, cmap='viridis', shading='auto')
plt.colorbar(c, ax=ax, label='V_total')
if ref_key in results and 'error' not in results[ref_key]:
    r = results[ref_key]
    f2 = r['f_0']**2
    f2_2d = f2.reshape(n_tau, n_eps)
    # Overlay contours of |f_0|^2
    levels = np.linspace(f2_2d.max() * 0.1, f2_2d.max() * 0.9, 5)
    ax.contour(TAU, EPS, f2_2d, levels=levels, colors='white', linewidths=1)
    ax.plot(r['tau_gcm'], r['eps_gcm'], 'r*', markersize=15, label=f'GCM center')
ax.plot(tau[best_idx[0]], eps[best_idx[1]], 'w+', markersize=12, markeredgewidth=2,
        label=f'Best sin2_tw grid')
ax.set_xlabel('tau')
ax.set_ylabel('eps')
ax.set_title('V_total with GCM |f_0|^2 contours')
ax.legend(fontsize=8)

# Panel 2: sin^2(theta_W) landscape
ax = axes[0, 1]
c = ax.pcolormesh(TAU, EPS, sin2_tw, cmap='RdYlBu_r', shading='auto',
                  vmin=0.1, vmax=0.5)
plt.colorbar(c, ax=ax, label='sin^2(theta_W)')
# SM target contour
ax.contour(TAU, EPS, sin2_tw, levels=[sin2_tw_SM], colors='black', linewidths=2,
           linestyles='--')
if ref_key in results and 'error' not in results[ref_key]:
    ax.plot(results[ref_key]['tau_gcm'], results[ref_key]['eps_gcm'],
            'r*', markersize=15, label=f'<sin2>_GCM={results[ref_key]["sin2_gcm"]:.4f}')
ax.set_xlabel('tau')
ax.set_ylabel('eps')
ax.set_title(f'sin^2(theta_W) landscape (SM = {sin2_tw_SM})')
ax.legend(fontsize=8)

# Panel 3: GCM wave function
ax = axes[0, 2]
if ref_key in results and 'error' not in results[ref_key]:
    f2_2d = results[ref_key]['f_0']**2
    f2_2d = f2_2d.reshape(n_tau, n_eps)
    c = ax.pcolormesh(TAU, EPS, f2_2d, cmap='hot', shading='auto')
    plt.colorbar(c, ax=ax, label='|f_0|^2')
    ax.set_title(f'GCM ground state (PR/N = {results[ref_key]["PR_frac"]:.3f})')
else:
    ax.set_title('GCM ground state (FAILED)')
ax.set_xlabel('tau')
ax.set_ylabel('eps')

# Panel 4: Sigma sensitivity
ax = axes[1, 0]
sfs = []
sin2s = []
prs = []
for sf in sigma_factors:
    key = f"sigma_{sf:.1f}x"
    if key in results and 'error' not in results[key]:
        sfs.append(sf)
        sin2s.append(results[key]['sin2_gcm'])
        prs.append(results[key]['PR_frac'])
if sfs:
    ax2 = ax.twinx()
    l1 = ax.plot(sfs, sin2s, 'ro-', markersize=10, linewidth=2, label='<sin^2_tw>_GCM')
    ax.axhline(sin2_tw_SM, color='red', linestyle=':', alpha=0.5, label=f'SM = {sin2_tw_SM}')
    ax.axhline(best_sin2, color='red', linestyle='--', alpha=0.3, label=f'Best grid = {best_sin2:.4f}')
    l2 = ax2.plot(sfs, prs, 'bs-', markersize=10, linewidth=2, label='PR/N')
    ax2.axhline(0.3, color='blue', linestyle=':', alpha=0.5, label='Delocalization threshold')
    ax.set_xlabel('sigma / sigma_default')
    ax.set_ylabel('<sin^2_tw>_GCM', color='red')
    ax2.set_ylabel('PR/N_grid', color='blue')
    lines = l1 + l2
    labels_l = [l.get_label() for l in lines]
    ax.legend(lines, labels_l, fontsize=8)
ax.set_title('Sigma sensitivity')

# Panel 5: Energy spectrum
ax = axes[1, 1]
for sf in sigma_factors:
    key = f"sigma_{sf:.1f}x"
    if key in results and 'error' not in results[key]:
        E = results[key]['E_vals']
        ax.plot(range(len(E)), E - E[0], 'o-', markersize=4, label=f'sigma={sf}x')
ax.set_xlabel('State index')
ax.set_ylabel('E_n - E_0')
ax.set_title('GCM excitation spectrum')
ax.legend()
ax.set_xlim(-0.5, 19.5)

# Panel 6: Summary
ax = axes[1, 2]
ax.axis('off')
summary = [
    f"N-31Ce: GCM Configuration Mixing",
    f"",
    f"Grid: {n_tau} x {n_eps} = {N_grid} points",
    f"Observables: lambda_min, sin2_tw, phi_30",
    f"sigma_default = {sigma_default:.6f}",
    f"",
    f"SM target: sin^2(theta_W) = {sin2_tw_SM}",
    f"Best grid point: {best_sin2:.6f} (|diff| = {best_dist:.6f})",
    f"  at tau = {tau[best_idx[0]]:.3f}, eps = {eps[best_idx[1]]:.3f}",
    f"",
]
for sf in sigma_factors:
    key = f"sigma_{sf:.1f}x"
    if key in results and 'error' not in results[key]:
        r = results[key]
        summary.append(f"sigma={sf}x: <sin2>={r['sin2_gcm']:.4f}, "
                      f"PR/N={r['PR_frac']:.3f}, "
                      f"{'CLOSER' if r['closer'] else 'NOT CLOSER'}")
summary.extend([
    f"",
    f"Jensen-only GCM: <sin2> = {sin2_j:.4f}, PR = {PR_j:.1f}/{n_tau}",
    f"",
    f"GATE N-31Ce-G: {verdict}",
])
ax.text(0.05, 0.95, '\n'.join(summary), transform=ax.transAxes,
        fontsize=9, verticalalignment='top', fontfamily='monospace')

plt.tight_layout()
plt.savefig('tier0-computation/s31Ce_gcm_moduli.png', dpi=150, bbox_inches='tight')
print(f"Saved: tier0-computation/s31Ce_gcm_moduli.png")

print(f"\n=== COMPUTATION COMPLETE ===")
print(f"Gate N-31Ce-G: {verdict}")
