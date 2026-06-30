#!/usr/bin/env python3
"""
NPAIR2-ED-55: N_pair=2 Exact Diagonalization + Level Statistics
================================================================
Nazarewicz Nuclear Structure Theorist — Session 55, Wave 1

Physics: Exact diagonalization of the 2-pair BCS Hamiltonian on 8 modes.
The Fock space has dim = C(8,2) = 28.  We include:
  (a) Diagonal pair energies: sum_k 2*eps_k * n_k
  (b) Off-diagonal pair scattering: V_{kl} P_k^+ P_l  (Richardson-Gaudin integrable part)
  (c) Inter-pair density-density: V_{kl} n_k n_l  (integrability-BREAKING part)

The Richardson-Gaudin model (a)+(b) alone is exactly integrable with N conserved
quantities.  Adding (c) breaks integrability.  Level statistics distinguish:
  - Poisson <r> = 0.386  (integrable)
  - GOE    <r> = 0.531  (chaotic / broken integrability)

Gate: NPAIR2-ED-55
  PASS: <r> > 0.48  AND  P_vac(DE)/P_vac(GGE) < 0.5
  FAIL: <r> < 0.40

References:
  - Paper 03 (Bogoliubov, odd-even): BCS gap equation and blocking
  - Paper 08 (pairing collapse): pairing as function of interaction strength
  - Richardson, J. Math. Phys. 6, 1034 (1965): exact BCS solution
  - Oganesyan & Huse, Phys. Rev. B 75, 155111 (2007): r-statistic
"""

import sys
import numpy as np
from itertools import combinations
from math import comb as mcomb
from scipy.optimize import minimize
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

sys.path.insert(0, 'computations')
from canonical_constants import (
    tau_fold, E_cond, N_dof_BCS, E_cond_ED_8mode,
    Delta_0_GL, S_inst, omega_PV, M_KK
)

# ============================================================
# 1. Load data
# ============================================================
data_ed = np.load('computations/session-54/s54_ed_sweep.npz', allow_pickle=True)

tau_values = data_ed['tau_values']       # (50,)
E_sp_sweep = data_ed['E_sp_sweep']       # (50, 8)
V_bare = data_ed['V_bare_cont']          # (8, 8)
fold_idx = int(data_ed['fold_idx'])      # = 19

N_modes = 8  # (local)
N_pairs = 2

print("=" * 70)
print("NPAIR2-ED-55: N_pair=2 Exact Diagonalization")
print("=" * 70)
print(f"N_modes = {N_modes}, N_pairs = {N_pairs}")
print(f"Fock space dimension: C({N_modes},{N_pairs}) = {mcomb(N_modes, N_pairs)}")
print(f"fold_idx = {fold_idx}, tau_fold = {tau_values[fold_idx]:.6f}")
print()

# ============================================================
# 2. Build the 2-pair Fock basis
# ============================================================
basis = list(combinations(range(N_modes), N_pairs))
dim = len(basis)
assert dim == 28

# Occupation matrix: occ_mat[a, k] = 1 if level k occupied in state a
occ_mat = np.zeros((dim, N_modes))
for a, state in enumerate(basis):
    for k in state:
        occ_mat[a, k] = 1.0

print(f"Basis dimension: {dim}")
print()

# ============================================================
# 3. Hamiltonian construction
# ============================================================
def build_H(eps, V, alpha_dd=1.0):
    """
    H = sum_k 2*eps_k*n_k + alpha_dd*sum_{k<l} V_{kl}*n_k*n_l + sum_{k!=l} V_{kl}*P_k^+*P_l

    Part (a)+(b): Richardson-Gaudin integrable (pair energies + pair scattering)
    Part (c): density-density (monopole interaction, breaks RG integrability)
    """
    H = np.zeros((dim, dim))
    for a in range(dim):
        # (a) Pair energies
        H[a, a] = sum(2.0 * eps[k] for k in basis[a])
        # (c) Density-density
        k1, k2 = basis[a]
        H[a, a] += alpha_dd * V[k1, k2]
        # (b) Pair scattering
        for b in range(a + 1, dim):
            occ_a = set(basis[a])
            occ_b = set(basis[b])
            removed = occ_a - occ_b
            added = occ_b - occ_a
            if len(removed) == 1 and len(added) == 1:
                k = removed.pop()
                l = added.pop()
                H[a, b] = V[k, l]
                H[b, a] = V[k, l]
    return H


# ============================================================
# 4. Level statistics
# ============================================================
def compute_r_ratio(eigenvalues):
    """Oganesyan-Huse r-statistic for nearest-neighbor spacing ratios."""
    E = np.sort(eigenvalues)
    spacings = np.diff(E)
    spacings = spacings[spacings > 1e-12]
    if len(spacings) < 3:
        return np.nan, np.array([])
    r_vals = np.array([min(spacings[i], spacings[i+1]) / max(spacings[i], spacings[i+1])
                       for i in range(len(spacings) - 1)])
    return np.mean(r_vals), r_vals


# ============================================================
# 5. GGE solver (scipy L-BFGS-B)
# ============================================================
def solve_GGE(psi_0, H_final):
    """
    Solve for the Generalized Gibbs Ensemble with mode occupations as conserved quantities.
    rho_GGE = (1/Z) exp(-sum_k lambda_k n_k), diagonal in Fock basis.
    Lagrange multipliers determined by <n_k>_GGE = <n_k>_initial.
    """
    # Target occupations
    n_k_target = occ_mat.T @ (np.abs(psi_0)**2)

    def objective(lam):
        log_w = -(occ_mat @ lam)
        log_w -= np.max(log_w)
        w = np.exp(log_w)
        Z = np.sum(w)
        p = w / Z
        n_k_gge = occ_mat.T @ p
        return np.sum((n_k_gge - n_k_target)**2)

    def jac(lam):
        log_w = -(occ_mat @ lam)
        log_w -= np.max(log_w)
        w = np.exp(log_w)
        Z = np.sum(w)
        p = w / Z
        n_k_gge = occ_mat.T @ p
        diff = n_k_gge - n_k_target
        cov = occ_mat.T @ np.diag(p) @ occ_mat - np.outer(n_k_gge, n_k_gge)
        return -2.0 * cov @ diff

    result = minimize(objective, np.zeros(N_modes), jac=jac,
                      method='L-BFGS-B', options={'maxiter': 10000, 'ftol': 1e-25})

    # Final GGE distribution
    lam = result.x
    log_w = -(occ_mat @ lam)
    log_w -= np.max(log_w)
    w = np.exp(log_w)
    Z = np.sum(w)
    p = w / Z
    n_k_gge = occ_mat.T @ p

    # GGE energy: Tr[rho_GGE * H] = sum_a p(a) * H[a,a]  (rho_GGE diagonal in Fock basis)
    E_GGE = np.sum(p * np.diag(H_final))

    return E_GGE, p, n_k_gge, n_k_target, result.fun


# ============================================================
# 6. Finite-size reference distributions
# ============================================================
print("Computing finite-size reference distributions (N=28 levels)...")
np.random.seed(42)
N_MC = 5000  # (local)

r_poisson_mc = []
for _ in range(N_MC):
    E = np.sort(np.random.uniform(0, 10, dim))
    r_val, _ = compute_r_ratio(E)
    r_poisson_mc.append(r_val)
r_poisson_mc = np.array(r_poisson_mc)

r_goe_mc = []
for _ in range(N_MC):
    M = np.random.randn(dim, dim)
    M = (M + M.T) / 2
    E = np.linalg.eigvalsh(M)
    r_val, _ = compute_r_ratio(E)
    r_goe_mc.append(r_val)
r_goe_mc = np.array(r_goe_mc)

r_poisson_ref = np.mean(r_poisson_mc)
r_goe_ref = np.mean(r_goe_mc)
sigma_poisson = np.std(r_poisson_mc)
sigma_goe = np.std(r_goe_mc)

print(f"  Poisson: <r> = {r_poisson_ref:.4f} +/- {sigma_poisson:.4f}")
print(f"  GOE:     <r> = {r_goe_ref:.4f} +/- {sigma_goe:.4f}")
print()


# ============================================================
# 7. Main computation: tau sweep near fold
# ============================================================
tau_indices = [fold_idx + di for di in range(-5, 5) if 0 <= fold_idx + di < 50][:10]

results = {k: [] for k in ['tau_vals', 'r_full', 'r_RG', 'eigenvalues_full',
                             'eigenvalues_RG', 'Gamma_breaking',
                             'P_vac_DE', 'P_vac_GGE', 'P_ratio',
                             'comm_norm', 'sigma_from_poisson']}

print("-" * 80)
print(f"{'tau':>8s} | {'<r>_full':>8s} | {'<r>_RG':>8s} | {'sig_P':>6s} | {'Gamma':>10s} | {'P_DE/P_GGE':>10s}")
print("-" * 80)

for idx in tau_indices:
    tau = tau_values[idx]
    eps = E_sp_sweep[idx]

    H_full = build_H(eps, V_bare, alpha_dd=1.0)
    H_RG = build_H(eps, V_bare, alpha_dd=0.0)

    evals_full, evecs_full = np.linalg.eigh(H_full)
    evals_RG, evecs_RG = np.linalg.eigh(H_RG)

    r_full, _ = compute_r_ratio(evals_full)
    r_RG, _ = compute_r_ratio(evals_RG)

    # Integrability-breaking rate
    H_dd = H_full - H_RG
    H_dd_eig = evecs_RG.T @ H_dd @ evecs_RG
    off_diag = np.array([H_dd_eig[i, j] for i in range(dim) for j in range(i+1, dim)])
    mean_spacing = (evals_RG[-1] - evals_RG[0]) / (dim - 1)
    Gamma = 2 * np.pi * np.mean(off_diag**2) / mean_spacing

    # Commutator norm
    comm = H_RG @ H_dd - H_dd @ H_RG
    comm_rel = np.linalg.norm(comm, 'fro') / np.linalg.norm(H_RG, 'fro')

    # Quench: ground state from previous tau to current
    prev_idx = tau_indices[max(0, tau_indices.index(idx) - 1)]
    if idx == tau_indices[0]:
        prev_idx = max(0, idx - 1)
    H_prev = build_H(E_sp_sweep[prev_idx], V_bare)
    _, evecs_prev = np.linalg.eigh(H_prev)
    psi_0 = evecs_prev[:, 0]

    overlaps = np.abs(evecs_full.T @ psi_0)**2
    E_DE = np.sum(overlaps * evals_full)
    E_GGE, _, _, _, _ = solve_GGE(psi_0, H_full)
    P_ratio = E_DE / E_GGE if abs(E_GGE) > 1e-15 else np.inf

    sigma_P = (r_full - r_poisson_ref) / sigma_poisson

    results['tau_vals'].append(tau)
    results['r_full'].append(r_full)
    results['r_RG'].append(r_RG)
    results['eigenvalues_full'].append(evals_full)
    results['eigenvalues_RG'].append(evals_RG)
    results['Gamma_breaking'].append(Gamma)
    results['P_vac_DE'].append(E_DE)
    results['P_vac_GGE'].append(E_GGE)
    results['P_ratio'].append(P_ratio)
    results['comm_norm'].append(comm_rel)
    results['sigma_from_poisson'].append(sigma_P)

    print(f"{tau:8.4f} | {r_full:8.4f} | {r_RG:8.4f} | {sigma_P:+5.1f}s | {Gamma:10.6f} | {P_ratio:10.4f}")

print("-" * 80)

for key in results:
    results[key] = np.array(results[key])


# ============================================================
# 8. Alpha_dd sweep at fold (integrable->chaotic transition)
# ============================================================
print()
print("=" * 70)
print("ALPHA_DD SWEEP AT FOLD (integrability-breaking transition)")
print("=" * 70)

eps_fold = E_sp_sweep[fold_idx]
alphas = np.concatenate([np.linspace(0, 2, 21), np.linspace(3, 10, 8), np.linspace(15, 50, 8)])
r_vs_alpha = []

print(f"{'alpha_dd':>8s} | {'<r>':>8s} | {'sigma_P':>7s} | {'E_gs':>10s} | {'gap':>10s}")
print("-" * 55)
for alpha in alphas:
    H = build_H(eps_fold, V_bare, alpha_dd=alpha)
    evals = np.linalg.eigvalsh(H)
    r, _ = compute_r_ratio(evals)
    sig = (r - r_poisson_ref) / sigma_poisson
    r_vs_alpha.append(r)
    if alpha <= 2.0 or alpha in [5.0, 10.0, 50.0] or alpha % 5 == 0:
        print(f"{alpha:8.2f} | {r:8.4f} | {sig:+6.1f}s | {evals[0]:10.6f} | {evals[1]-evals[0]:10.6f}")
r_vs_alpha = np.array(r_vs_alpha)

# Find peak
peak_alpha = alphas[np.argmax(r_vs_alpha)]
peak_r = np.max(r_vs_alpha)
print(f"\nPeak: alpha_dd = {peak_alpha:.2f}, <r> = {peak_r:.4f}, sigma_P = {(peak_r - r_poisson_ref)/sigma_poisson:+.1f}")
print(f"Physical value alpha_dd = 1.0: <r> = {r_vs_alpha[alphas.tolist().index(1.0) if 1.0 in alphas else np.argmin(np.abs(alphas-1.0))]:.4f}")


# ============================================================
# 9. Large quench analysis
# ============================================================
print()
print("=" * 70)
print("LARGE QUENCH ANALYSIS")
print("=" * 70)

quench_pairs = [
    (0, fold_idx, 'tau=0 -> fold'),
    (0, 49, 'tau=0 -> tau=0.5'),
    (fold_idx, 49, 'fold -> tau=0.5'),
]

large_quench_results = {}
for tau_i_idx, tau_f_idx, label in quench_pairs:
    H_i = build_H(E_sp_sweep[tau_i_idx], V_bare)
    H_f = build_H(E_sp_sweep[tau_f_idx], V_bare)

    evals_i, evecs_i = np.linalg.eigh(H_i)
    evals_f, evecs_f = np.linalg.eigh(H_f)

    psi_0 = evecs_i[:, 0]
    c_n = evecs_f.T @ psi_0
    overlaps_sq = np.abs(c_n)**2

    E_DE = np.sum(overlaps_sq * evals_f)
    IPR = 1.0 / np.sum(overlaps_sq**2)

    E_GGE, p_gge, n_k_gge, n_k_target, gge_resid = solve_GGE(psi_0, H_f)

    # Thermal energy at infinite temperature
    E_inf = np.sum(np.diag(H_f)) / dim

    P_ratio_q = E_DE / E_GGE
    heat_fraction = (E_DE - evals_f[0]) / (E_inf - evals_f[0]) if E_inf != evals_f[0] else 0

    large_quench_results[label] = {
        'E_DE': E_DE, 'E_GGE': E_GGE, 'P_ratio': P_ratio_q,
        'IPR': IPR, 'heat_fraction': heat_fraction, 'gge_resid': gge_resid
    }

    print(f"\n{label}:")
    print(f"  E_gs(final)  = {evals_f[0]:.6f}")
    print(f"  E_DE         = {E_DE:.6f}")
    print(f"  E_GGE        = {E_GGE:.6f}")
    print(f"  P_DE/P_GGE   = {P_ratio_q:.6f}")
    print(f"  IPR          = {IPR:.2f}/{dim}")
    print(f"  Heat frac    = {heat_fraction:.6f} (0=cold, 1=hot)")
    print(f"  GGE residual = {gge_resid:.2e}")

# Primary quench for gate
primary_quench = large_quench_results['tau=0 -> fold']


# ============================================================
# 10. Gate verdict
# ============================================================
print()
print("=" * 70)
print("GATE VERDICT: NPAIR2-ED-55")
print("=" * 70)

r_full_mean = np.mean(results['r_full'])
r_RG_mean = np.mean(results['r_RG'])
Gamma_mean = np.mean(results['Gamma_breaking'])
r_at_fold = results['r_full'][list(tau_indices).index(fold_idx)] if fold_idx in tau_indices else r_full_mean
P_at_fold = primary_quench['P_ratio']

print(f"<r> at fold:              {r_at_fold:.4f}  ({(r_at_fold - r_poisson_ref)/sigma_poisson:+.1f} sigma from Poisson)")
print(f"<r> mean near fold:       {r_full_mean:.4f}  ({(r_full_mean - r_poisson_ref)/sigma_poisson:+.1f} sigma from Poisson)")
print(f"<r> RG-only mean:         {r_RG_mean:.4f}")
print(f"<r> shift (full - RG):    {r_full_mean - r_RG_mean:+.4f}")
print(f"P_vac(DE)/P_vac(GGE):     {P_at_fold:.4f}  (large quench, tau=0->fold)")
print(f"IPR large quench:         {primary_quench['IPR']:.2f}/{dim}")
print(f"Gamma_breaking (mean):    {Gamma_mean:.6f} M_KK")
print(f"Gamma/Delta_0:            {Gamma_mean / Delta_0_GL:.6f}")
print(f"||[H_RG, H_dd]||/||H_RG||: {np.mean(results['comm_norm']):.6f}")
print()

# Gate classification
# The <r> mean is the primary criterion
if r_full_mean > 0.48 and P_at_fold < 0.5:
    verdict = "PASS"
    detail = (f"<r>={r_full_mean:.4f}>0.48 AND P_ratio={P_at_fold:.4f}<0.5. "
              f"Integrability broken, CC path viable.")
elif r_full_mean < 0.40:
    verdict = "FAIL"
    detail = (f"<r>={r_full_mean:.4f}<0.40 (Poisson). System remains integrable. "
              f"CC path through integrability breaking CLOSED.")
else:
    verdict = "INFO"
    # Determine sub-classification
    if r_at_fold > 0.48:
        detail = (f"<r>_mean={r_full_mean:.4f} in [0.40,0.48] (intermediate), "
                  f"but <r>_fold={r_at_fold:.4f}>0.48 ({(r_at_fold-r_poisson_ref)/sigma_poisson:+.1f}sigma). "
                  f"P_ratio={P_at_fold:.4f}>0.5 (GGE~DE, near-adiabatic quench). "
                  f"Density-density interaction breaks integrability LOCALLY near fold "
                  f"but Hilbert space too small (dim=28) for definitive classification. "
                  f"Need N_pair>=3 (dim=56) to resolve.")
    else:
        detail = (f"<r>={r_full_mean:.4f} in [0.40,0.48]. "
                  f"Partial integrability breaking, inconclusive at dim=28.")

print(f"VERDICT: {verdict}")
print(f"DETAIL:  {detail}")


# ============================================================
# 11. Save all results
# ============================================================
np.savez('computations/session-55/s55_npair2_ed.npz',
    # Tau sweep results
    tau_vals=results['tau_vals'],
    r_full=results['r_full'],
    r_RG=results['r_RG'],
    eigenvalues_full=np.array(results['eigenvalues_full']),
    eigenvalues_RG=np.array(results['eigenvalues_RG']),
    Gamma_breaking=results['Gamma_breaking'],
    P_vac_DE=results['P_vac_DE'],
    P_vac_GGE=results['P_vac_GGE'],
    P_ratio=results['P_ratio'],
    comm_norm=results['comm_norm'],
    sigma_from_poisson=results['sigma_from_poisson'],
    # Alpha sweep
    alphas=alphas,
    r_vs_alpha=r_vs_alpha,
    peak_alpha=peak_alpha,
    peak_r=peak_r,
    # Large quench
    E_DE_large=primary_quench['E_DE'],
    E_GGE_large=primary_quench['E_GGE'],
    P_ratio_large=P_at_fold,
    IPR_large=primary_quench['IPR'],
    # Reference distributions
    r_poisson_ref=r_poisson_ref,
    r_goe_ref=r_goe_ref,
    sigma_poisson=sigma_poisson,
    sigma_goe=sigma_goe,
    # Gate
    gate_name='NPAIR2-ED-55',
    gate_verdict=verdict,
    gate_detail=detail,
    r_full_mean=r_full_mean,
    r_RG_mean=r_RG_mean,
    r_at_fold=r_at_fold,
    Gamma_mean=Gamma_mean,
    # Metadata
    N_modes=N_modes,
    N_pairs=N_pairs,
    dim_fock=dim,
    fold_idx=fold_idx)

print(f"\nData saved to computations/session-55/s55_npair2_ed.npz")


# ============================================================
# 12. Plot (2x3 panels)
# ============================================================
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle('NPAIR2-ED-55: $N_{pair}=2$ Exact Diagonalization + Level Statistics\n'
             f'Gate: {verdict} | $\\langle r \\rangle_{{fold}}$={r_at_fold:.3f}, '
             f'$\\langle r \\rangle_{{mean}}$={r_full_mean:.3f}, '
             f'$P_{{DE}}/P_{{GGE}}$={P_at_fold:.3f}',
             fontsize=13, fontweight='bold')

# (a) <r> vs tau
ax = axes[0, 0]
ax.axhspan(r_poisson_ref - sigma_poisson, r_poisson_ref + sigma_poisson,
           color='blue', alpha=0.1, label=f'Poisson 1$\\sigma$')
ax.axhspan(r_goe_ref - sigma_goe, r_goe_ref + sigma_goe,
           color='red', alpha=0.1, label=f'GOE 1$\\sigma$')
ax.axhline(r_poisson_ref, color='blue', ls='--', alpha=0.7, label=f'Poisson ({r_poisson_ref:.3f})')
ax.axhline(r_goe_ref, color='red', ls='--', alpha=0.7, label=f'GOE ({r_goe_ref:.3f})')
ax.axhline(0.48, color='orange', ls=':', alpha=0.9, lw=2, label='PASS threshold')
ax.axhline(0.40, color='green', ls=':', alpha=0.9, lw=2, label='FAIL threshold')
ax.plot(results['tau_vals'], results['r_full'], 'ko-', ms=7, lw=2, label='Full H')
ax.plot(results['tau_vals'], results['r_RG'], 'b^--', ms=5, alpha=0.7, label='RG only')
ax.axvline(tau_values[fold_idx], color='gray', ls='-.', alpha=0.5)
ax.set_xlabel(r'$\tau$', fontsize=12)
ax.set_ylabel(r'$\langle r \rangle$', fontsize=12)
ax.set_title('Level spacing ratio vs $\\tau$')
ax.legend(fontsize=6.5, loc='upper left', ncol=2)
ax.set_ylim(0.25, 0.65)

# (b) Alpha_dd sweep
ax = axes[0, 1]
ax.axhline(r_poisson_ref, color='blue', ls='--', alpha=0.7, label='Poisson')
ax.axhline(r_goe_ref, color='red', ls='--', alpha=0.7, label='GOE')
ax.axhline(0.48, color='orange', ls=':', alpha=0.7)
ax.plot(alphas, r_vs_alpha, 'ko-', ms=4, lw=1.5)
ax.axvline(1.0, color='green', ls='-', alpha=0.8, lw=2, label=r'Physical $\alpha_{dd}=1$')
ax.axvline(peak_alpha, color='purple', ls=':', alpha=0.7, label=f'Peak ($\\alpha$={peak_alpha:.1f})')
ax.set_xlabel(r'$\alpha_{dd}$ (density-density strength)', fontsize=11)
ax.set_ylabel(r'$\langle r \rangle$', fontsize=12)
ax.set_title(r'Integrable $\to$ chaotic transition')
ax.set_xlim(-0.5, 12)
ax.legend(fontsize=8)

# (c) Spectrum at fold
ax = axes[0, 2]
fold_pos = list(tau_indices).index(fold_idx) if fold_idx in tau_indices else 5
evals_at_fold = results['eigenvalues_full'][fold_pos]
evals_RG_fold = results['eigenvalues_RG'][fold_pos]
ax.plot(range(dim), evals_at_fold - evals_at_fold[0], 'ko', ms=5, label='Full H')
ax.plot(range(dim), evals_RG_fold - evals_RG_fold[0], 'b^', ms=4, alpha=0.6, label='RG only')
ax.set_xlabel('Level index', fontsize=11)
ax.set_ylabel(r'$E_n - E_0$ [$M_{KK}$]', fontsize=11)
ax.set_title(f'Spectrum at fold ($\\tau$={tau_values[fold_idx]:.3f})')
ax.legend()

# (d) Gamma vs tau
ax = axes[1, 0]
ax.plot(results['tau_vals'], results['Gamma_breaking'] * 1e3, 'ro-', ms=6, lw=2)
ax.axvline(tau_values[fold_idx], color='gray', ls='-.', alpha=0.5)
ax.set_xlabel(r'$\tau$', fontsize=12)
ax.set_ylabel(r'$\Gamma \times 10^3$ [$M_{KK}$]', fontsize=11)
ax.set_title(r'Integrability-breaking rate $\Gamma$')

# (e) NNS distribution at fold
ax = axes[1, 1]
spacings = np.diff(evals_at_fold)
spacings = spacings[spacings > 1e-12]
s_norm = spacings / np.mean(spacings)
ax.hist(s_norm, bins=8, density=True, alpha=0.7, color='steelblue', edgecolor='black', label='Data')
s_plot = np.linspace(0, 4, 200)
ax.plot(s_plot, np.exp(-s_plot), 'b--', lw=2, label='Poisson')
ax.plot(s_plot, (np.pi / 2) * s_plot * np.exp(-np.pi * s_plot**2 / 4), 'r--', lw=2, label='GOE')
ax.set_xlabel(r'$s = \delta E / \langle \delta E \rangle$', fontsize=11)
ax.set_ylabel('P(s)', fontsize=11)
ax.set_title('NNS distribution at fold')
ax.legend()

# (f) Commutator and P_ratio
ax = axes[1, 2]
ax2 = ax.twinx()
l1, = ax.plot(results['tau_vals'], results['comm_norm'] * 1e3, 'ms-', ms=5, lw=1.5,
              label=r'$\|[H_{RG}, H_{dd}]\|/\|H_{RG}\| \times 10^3$')
l2, = ax2.plot(results['tau_vals'], results['P_ratio'], 'go-', ms=5, lw=1.5,
               label=r'$P_{DE}/P_{GGE}$')
ax2.axhline(0.5, color='orange', ls=':', alpha=0.7, label='PASS threshold')
ax.axvline(tau_values[fold_idx], color='gray', ls='-.', alpha=0.5)
ax.set_xlabel(r'$\tau$', fontsize=12)
ax.set_ylabel(r'$\|[H_{RG}, H_{dd}]\|/\|H_{RG}\| \times 10^3$', fontsize=10, color='purple')
ax2.set_ylabel(r'$P_{vac}(DE) / P_{vac}(GGE)$', fontsize=10, color='green')
ax.set_title('Commutator & vacuum pressure ratio')
lines = [l1, l2]
ax.legend(lines, [l.get_label() for l in lines], fontsize=8, loc='center left')

plt.tight_layout()
plt.savefig('computations/session-55/s55_npair2_ed.png', dpi=150, bbox_inches='tight')
print(f"Plot saved to computations/session-55/s55_npair2_ed.png")
print()
print("DONE.")
