#!/usr/bin/env python3
"""
NPAIR3-ED-56: N_pair=3 Exact Diagonalization + Level Statistics
================================================================
Nazarewicz Nuclear Structure Theorist -- Session 56, Wave 1

Physics: Exact diagonalization of the 3-pair BCS Hamiltonian on 8 modes.
The Fock space has dim = C(8,3) = 56.  We include:
  (a) Diagonal pair energies: sum_k 2*eps_k * n_k
  (b) Off-diagonal pair scattering: V_{kl} P_k^+ P_l  (Richardson-Gaudin integrable part)
  (c) Inter-pair density-density: alpha_dd * sum_{k<l} V_{kl} * n_k * n_l  (breaks RG integrability)

For N_pair=3, density-density has C(3,2)=3 terms per basis state (vs 1 for N_pair=2).
The larger Hilbert space (56 vs 28) provides better statistics for r-ratio classification.

S55 NPAIR2-ED gave <r>_fold = 0.509 (+2.0 sigma from Poisson) but was INFO (dim=28 too small).
This computation is the pre-registered follow-up.

Gate: NPAIR3-ED-56
  PASS: <r> >= 0.53 at alpha_dd=1.0 (GOE, integrability definitively broken)
  FAIL: <r> < 0.45 (near-Poisson, integrable)
  INFO: 0.45 <= <r> < 0.53 (transition, inconclusive at dim=56)

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
N_pairs = 3

print("=" * 70)
print("NPAIR3-ED-56: N_pair=3 Exact Diagonalization")
print("=" * 70)
print(f"N_modes = {N_modes}, N_pairs = {N_pairs}")
print(f"Fock space dimension: C({N_modes},{N_pairs}) = {mcomb(N_modes, N_pairs)}")
print(f"fold_idx = {fold_idx}, tau_fold = {tau_values[fold_idx]:.6f}")
print()

# ============================================================
# 2. Build the 3-pair Fock basis
# ============================================================
basis = list(combinations(range(N_modes), N_pairs))
dim = len(basis)
assert dim == 56, f"Expected 56, got {dim}"

# Occupation matrix: occ_mat[a, k] = 1 if level k occupied in state a
occ_mat = np.zeros((dim, N_modes))
for a, state in enumerate(basis):
    for k in state:
        occ_mat[a, k] = 1.0

print(f"Basis dimension: {dim}")
print(f"First 5 basis states: {basis[:5]}")
print(f"Last 5 basis states: {basis[-5:]}")
print()

# ============================================================
# 3. Hamiltonian construction
# ============================================================
def build_H(eps, V, alpha_dd=1.0):
    """
    H = sum_k 2*eps_k*n_k
      + alpha_dd * sum_{k<l, both occupied} V_{kl} * n_k * n_l
      + sum_{k!=l} V_{kl} * P_k^+ * P_l

    Part (a): Pair energies (diagonal).
    Part (c): Density-density (diagonal, breaks RG integrability).
              For N_pair=3, each basis state has C(3,2)=3 pair interactions.
    Part (b): Pair scattering (off-diagonal, states differ by exactly 1 level swap).
    """
    H = np.zeros((dim, dim))
    for a in range(dim):
        occ_a = basis[a]  # tuple of 3 occupied levels
        # (a) Pair energies
        H[a, a] = sum(2.0 * eps[k] for k in occ_a)
        # (c) Density-density: sum over all pairs of occupied levels
        for i in range(len(occ_a)):
            for j in range(i + 1, len(occ_a)):
                H[a, a] += alpha_dd * V[occ_a[i], occ_a[j]]
        # (b) Pair scattering: connect states differing by exactly 1 level
        for b in range(a + 1, dim):
            set_a = set(occ_a)
            set_b = set(basis[b])
            removed = set_a - set_b
            added = set_b - set_a
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
# 6. Finite-size reference distributions (dim=56)
# ============================================================
print("Computing finite-size reference distributions (N=56 levels)...")
np.random.seed(42)
N_MC = 10000  # (local)

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

print(f"  Poisson (dim={dim}): <r> = {r_poisson_ref:.4f} +/- {sigma_poisson:.4f}")
print(f"  GOE    (dim={dim}): <r> = {r_goe_ref:.4f} +/- {sigma_goe:.4f}")
print()

# Cross-check: S55 used dim=28: Poisson 0.3856, GOE 0.5309
# dim=56 should be closer to thermodynamic values: Poisson 0.386, GOE 0.536


# ============================================================
# 7. Main computation: tau sweep (10 values in [0.10, 0.30])
# ============================================================
# Select 10 tau indices covering [0.10, 0.30]
tau_target = np.linspace(0.10, 0.30, 10)
tau_indices = [int(np.argmin(np.abs(tau_values - t))) for t in tau_target]
# Remove duplicates while preserving order
seen = set()
tau_indices_unique = []
for idx in tau_indices:
    if idx not in seen:
        seen.add(idx)
        tau_indices_unique.append(idx)
tau_indices = tau_indices_unique

print(f"Tau sweep: {len(tau_indices)} points")
print(f"  tau values: {[f'{tau_values[i]:.4f}' for i in tau_indices]}")
print(f"  fold at index {fold_idx} (tau={tau_values[fold_idx]:.4f})")
print()

results = {k: [] for k in ['tau_vals', 'r_full', 'r_RG', 'eigenvalues_full',
                             'eigenvalues_RG', 'Gamma_breaking',
                             'P_vac_DE', 'P_vac_GGE', 'P_ratio',
                             'comm_norm', 'sigma_from_poisson',
                             'gs_occupations', 'IPR_fold', 'E_gs']}

print("-" * 90)
print(f"{'tau':>8s} | {'<r>_full':>8s} | {'<r>_RG':>8s} | {'sig_P':>6s} | {'sig_GOE':>6s} | {'Gamma':>10s} | {'P_DE/P_GGE':>10s}")
print("-" * 90)

for idx in tau_indices:
    tau = tau_values[idx]
    eps = E_sp_sweep[idx]

    H_full = build_H(eps, V_bare, alpha_dd=1.0)
    H_RG = build_H(eps, V_bare, alpha_dd=0.0)

    evals_full, evecs_full = np.linalg.eigh(H_full)
    evals_RG, evecs_RG = np.linalg.eigh(H_RG)

    r_full, _ = compute_r_ratio(evals_full)
    r_RG, _ = compute_r_ratio(evals_RG)

    # Integrability-breaking rate (Fermi golden rule)
    H_dd = H_full - H_RG
    H_dd_eig = evecs_RG.T @ H_dd @ evecs_RG
    off_diag = np.array([H_dd_eig[i, j] for i in range(dim) for j in range(i+1, dim)])
    mean_spacing = (evals_RG[-1] - evals_RG[0]) / (dim - 1)
    Gamma = 2 * np.pi * np.mean(off_diag**2) / mean_spacing

    # Commutator norm (measure of non-commutativity between integrable and breaking parts)
    comm = H_RG @ H_dd - H_dd @ H_RG
    comm_rel = np.linalg.norm(comm, 'fro') / np.linalg.norm(H_RG, 'fro')

    # Ground state occupations
    psi_gs = evecs_full[:, 0]
    gs_occ = occ_mat.T @ (np.abs(psi_gs)**2)

    # IPR of ground state in energy eigenbasis
    IPR_gs = 1.0 / np.sum(np.abs(psi_gs)**4)  # in Fock basis

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
    sigma_GOE = (r_full - r_goe_ref) / sigma_goe

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
    results['gs_occupations'].append(gs_occ)
    results['IPR_fold'].append(IPR_gs)
    results['E_gs'].append(evals_full[0])

    print(f"{tau:8.4f} | {r_full:8.4f} | {r_RG:8.4f} | {sigma_P:+5.1f}s | {sigma_GOE:+5.1f}s | {Gamma:10.6f} | {P_ratio:10.4f}")

print("-" * 90)

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
alphas = np.linspace(0, 2, 21)  # 20 values as specified + 0
r_vs_alpha = []
E_gs_vs_alpha = []
gap_vs_alpha = []
occ_vs_alpha = []

print(f"{'alpha_dd':>8s} | {'<r>':>8s} | {'sigma_P':>7s} | {'sigma_GOE':>8s} | {'E_gs':>10s} | {'gap':>10s}")
print("-" * 70)
for alpha in alphas:
    H = build_H(eps_fold, V_bare, alpha_dd=alpha)
    evals, evecs = np.linalg.eigh(H)
    r, _ = compute_r_ratio(evals)
    sig_p = (r - r_poisson_ref) / sigma_poisson
    sig_g = (r - r_goe_ref) / sigma_goe
    r_vs_alpha.append(r)
    E_gs_vs_alpha.append(evals[0])
    gap_vs_alpha.append(evals[1] - evals[0])
    # Ground state occupations
    psi = evecs[:, 0]
    occ = occ_mat.T @ (np.abs(psi)**2)
    occ_vs_alpha.append(occ)
    print(f"{alpha:8.3f} | {r:8.4f} | {sig_p:+6.1f}s | {sig_g:+7.1f}s | {evals[0]:10.6f} | {evals[1]-evals[0]:10.6f}")

r_vs_alpha = np.array(r_vs_alpha)
E_gs_vs_alpha = np.array(E_gs_vs_alpha)
gap_vs_alpha = np.array(gap_vs_alpha)
occ_vs_alpha = np.array(occ_vs_alpha)

# Find peak
peak_alpha = alphas[np.argmax(r_vs_alpha)]
peak_r = np.max(r_vs_alpha)
# Physical value
idx_phys = np.argmin(np.abs(alphas - 1.0))
r_physical = r_vs_alpha[idx_phys]
print(f"\nPeak: alpha_dd = {peak_alpha:.3f}, <r> = {peak_r:.4f}, sigma_P = {(peak_r - r_poisson_ref)/sigma_poisson:+.1f}")
print(f"Physical alpha_dd = 1.0: <r> = {r_physical:.4f} ({(r_physical - r_poisson_ref)/sigma_poisson:+.1f} sig from Poisson)")


# ============================================================
# 9. Extended alpha sweep (wider range to find GOE regime)
# ============================================================
print()
print("Extended alpha_dd sweep (0 to 50):")
alphas_ext = np.concatenate([np.linspace(0, 2, 21), np.linspace(3, 10, 8), np.linspace(15, 50, 8)])
r_ext = []
for alpha in alphas_ext:
    H = build_H(eps_fold, V_bare, alpha_dd=alpha)
    evals = np.linalg.eigvalsh(H)
    r, _ = compute_r_ratio(evals)
    r_ext.append(r)
r_ext = np.array(r_ext)
peak_ext = alphas_ext[np.argmax(r_ext)]
print(f"Extended peak: alpha_dd = {peak_ext:.2f}, <r> = {np.max(r_ext):.4f}")


# ============================================================
# 10. Large quench analysis
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

    P_ratio_q = E_DE / E_GGE if abs(E_GGE) > 1e-15 else np.inf
    heat_fraction = (E_DE - evals_f[0]) / (E_inf - evals_f[0]) if E_inf != evals_f[0] else 0

    large_quench_results[label] = {
        'E_DE': E_DE, 'E_GGE': E_GGE, 'P_ratio': P_ratio_q,
        'IPR': IPR, 'heat_fraction': heat_fraction, 'gge_resid': gge_resid,
        'n_k_target': n_k_target, 'n_k_gge': n_k_gge
    }

    print(f"\n{label}:")
    print(f"  E_gs(final)  = {evals_f[0]:.6f}")
    print(f"  E_DE         = {E_DE:.6f}")
    print(f"  E_GGE        = {E_GGE:.6f}")
    print(f"  P_DE/P_GGE   = {P_ratio_q:.6f}")
    print(f"  IPR          = {IPR:.2f}/{dim}")
    print(f"  Heat frac    = {heat_fraction:.6f} (0=cold, 1=hot)")
    print(f"  GGE residual = {gge_resid:.2e}")
    print(f"  n_k target   = {n_k_target}")
    print(f"  n_k GGE      = {n_k_gge}")

# Primary quench for gate
primary_quench = large_quench_results['tau=0 -> fold']


# ============================================================
# 11. Vacuum pressure P_vac
# ============================================================
print()
print("=" * 70)
print("VACUUM PRESSURE AND GROUND STATE ANALYSIS AT FOLD")
print("=" * 70)

H_fold = build_H(eps_fold, V_bare, alpha_dd=1.0)
evals_fold, evecs_fold = np.linalg.eigh(H_fold)
psi_gs_fold = evecs_fold[:, 0]

# Ground state occupations
gs_occ_fold = occ_mat.T @ (np.abs(psi_gs_fold)**2)
print(f"\nGround state occupations at fold (tau={tau_values[fold_idx]:.4f}):")
for k in range(N_modes):
    print(f"  Mode {k} (eps={eps_fold[k]:.4f}): n_k = {gs_occ_fold[k]:.6f}")

# P_vac = -E_gs/V (in natural units where V=1)
P_vac = -evals_fold[0]
print(f"\nP_vac = -E_gs = {P_vac:.6f} M_KK")
print(f"E_gs = {evals_fold[0]:.6f} M_KK")
print(f"First gap = {evals_fold[1] - evals_fold[0]:.6f} M_KK")

# IPR of ground state in Fock basis
IPR_gs_fold = 1.0 / np.sum(np.abs(psi_gs_fold)**4)
print(f"IPR(gs) = {IPR_gs_fold:.4f} / {dim}")

# Compare to N_pair=2
H_fold_N2 = np.zeros((28, 28))
basis_N2 = list(combinations(range(N_modes), 2))
for a in range(28):
    H_fold_N2[a, a] = sum(2.0 * eps_fold[k] for k in basis_N2[a])
    k1, k2 = basis_N2[a]
    H_fold_N2[a, a] += V_bare[k1, k2]
    for b in range(a+1, 28):
        set_a = set(basis_N2[a])
        set_b = set(basis_N2[b])
        removed = set_a - set_b
        added = set_b - set_a
        if len(removed) == 1 and len(added) == 1:
            k = removed.pop()
            l = added.pop()
            H_fold_N2[a, b] = V_bare[k, l]
            H_fold_N2[b, a] = V_bare[k, l]
evals_N2 = np.linalg.eigvalsh(H_fold_N2)
r_N2, _ = compute_r_ratio(evals_N2)
print(f"\nComparison with N_pair=2:")
print(f"  <r>(N=2, dim=28) = {r_N2:.4f}")

# Build N=1 for comparison
H_fold_N1 = np.zeros((8, 8))
for a in range(8):
    H_fold_N1[a, a] = 2.0 * eps_fold[a]
    for b in range(a+1, 8):
        H_fold_N1[a, b] = V_bare[a, b]
        H_fold_N1[b, a] = V_bare[a, b]
evals_N1 = np.linalg.eigvalsh(H_fold_N1)
r_N1, _ = compute_r_ratio(evals_N1)
print(f"  <r>(N=1, dim=8) = {r_N1:.4f}")

# Separation energy S_3 = E(N=3) - E(N=2) - E(N=1)
# [Actually: 2-pair separation energy S_2(N) = E(N) - 2*E(N-1) + E(N-2)]
# S_3(3) = E(3) - 2*E(2) + E(1)
S3_sep = evals_fold[0] - 2*evals_N2[0] + evals_N1[0]
print(f"\nTwo-body separation energy S_3 = E(3) - 2*E(2) + E(1) = {S3_sep:.6f} M_KK")
print(f"  E(1) = {evals_N1[0]:.6f}")
print(f"  E(2) = {evals_N2[0]:.6f}")
print(f"  E(3) = {evals_fold[0]:.6f}")


# ============================================================
# 12. Gate verdict
# ============================================================
print()
print("=" * 70)
print("GATE VERDICT: NPAIR3-ED-56")
print("=" * 70)

# Find the fold index in our tau sweep
fold_pos = None
for i, idx in enumerate(tau_indices):
    if idx == fold_idx:
        fold_pos = i
        break

r_full_mean = np.mean(results['r_full'])
r_RG_mean = np.mean(results['r_RG'])
Gamma_mean = np.mean(results['Gamma_breaking'])
r_at_fold = results['r_full'][fold_pos] if fold_pos is not None else r_full_mean
P_at_fold = primary_quench['P_ratio']

print(f"<r> at fold:              {r_at_fold:.4f}  ({(r_at_fold - r_poisson_ref)/sigma_poisson:+.1f} sigma from Poisson)")
print(f"                                   ({(r_at_fold - r_goe_ref)/sigma_goe:+.1f} sigma from GOE)")
print(f"<r> mean over [0.10, 0.30]:  {r_full_mean:.4f}  ({(r_full_mean - r_poisson_ref)/sigma_poisson:+.1f} sigma from Poisson)")
print(f"<r> RG-only mean:         {r_RG_mean:.4f}")
print(f"<r> shift (full - RG):    {r_full_mean - r_RG_mean:+.4f}")
print(f"P_vac(DE)/P_vac(GGE):     {P_at_fold:.4f}  (large quench, tau=0->fold)")
print(f"IPR large quench:         {primary_quench['IPR']:.2f}/{dim}")
print(f"Gamma_breaking (mean):    {Gamma_mean:.6f} M_KK")
print(f"Gamma/Delta_0:            {Gamma_mean / Delta_0_GL:.6f}")
print(f"||[H_RG, H_dd]||/||H_RG||: {np.mean(results['comm_norm']):.6f}")
print(f"P_vac = {P_vac:.6f} M_KK")
print()

# Comparison with S55 N_pair=2
print("COMPARISON WITH S55 (N_pair=2, dim=28):")
print(f"  S55: <r>_fold = 0.509, <r>_mean = 0.447")
print(f"  S56: <r>_fold = {r_at_fold:.4f}, <r>_mean = {r_full_mean:.4f}")
print(f"  Shift: d<r>_fold = {r_at_fold - 0.509:+.4f}, d<r>_mean = {r_full_mean - 0.447:+.4f}")
print()

# Gate classification
# Pre-registered thresholds: PASS >= 0.53, FAIL < 0.45, INFO in between
# Using r_at_fold (at alpha_dd = 1.0) as the primary criterion
if r_at_fold >= 0.53:
    verdict = "PASS"
    detail = (f"<r>_fold={r_at_fold:.4f}>=0.53 (GOE). dim=56 confirms integrability breaking. "
              f"Density-density interaction drives Poisson-to-GOE transition. "
              f"<r>_mean={r_full_mean:.4f}, P_ratio={P_at_fold:.4f}.")
elif r_at_fold < 0.45:
    verdict = "FAIL"
    detail = (f"<r>_fold={r_at_fold:.4f}<0.45 (near-Poisson). System remains integrable at N_pair=3. "
              f"<r>_mean={r_full_mean:.4f}.")
else:
    verdict = "INFO"
    # Sub-classify
    sigma_P_fold = (r_at_fold - r_poisson_ref) / sigma_poisson
    sigma_GOE_fold = (r_at_fold - r_goe_ref) / sigma_goe
    if r_at_fold >= 0.50:
        detail = (f"<r>_fold={r_at_fold:.4f} in [0.45,0.53] (transition regime), "
                  f"{sigma_P_fold:+.1f}sig from Poisson, {sigma_GOE_fold:+.1f}sig from GOE. "
                  f"<r>_mean={r_full_mean:.4f}. P_ratio={P_at_fold:.4f}. "
                  f"Partial integrability breaking confirmed (dim=56 still finite-size limited). "
                  f"Peak <r>={peak_r:.4f} at alpha_dd={peak_alpha:.2f}. "
                  f"System on GOE side of transition at fold but not yet fully chaotic.")
    else:
        detail = (f"<r>_fold={r_at_fold:.4f} in [0.45,0.53] (transition regime), "
                  f"{sigma_P_fold:+.1f}sig from Poisson. "
                  f"<r>_mean={r_full_mean:.4f}. P_ratio={P_at_fold:.4f}. "
                  f"Integrability weakly broken. Insufficient for GOE classification at dim=56.")

print(f"VERDICT: {verdict}")
print(f"DETAIL:  {detail}")


# ============================================================
# 13. Save all results
# ============================================================
np.savez('computations/session-56/s56_npair3_ed.npz',
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
    gs_occupations=np.array(results['gs_occupations']),
    IPR_vals=np.array(results['IPR_fold']),
    E_gs_sweep=np.array(results['E_gs']),
    # Alpha sweep (physical range)
    alphas=alphas,
    r_vs_alpha=r_vs_alpha,
    E_gs_vs_alpha=E_gs_vs_alpha,
    gap_vs_alpha=gap_vs_alpha,
    occ_vs_alpha=occ_vs_alpha,
    peak_alpha=peak_alpha,
    peak_r=peak_r,
    r_physical=r_physical,
    # Extended alpha sweep
    alphas_ext=alphas_ext,
    r_ext=r_ext,
    peak_alpha_ext=peak_ext,
    # Large quench
    E_DE_large=primary_quench['E_DE'],
    E_GGE_large=primary_quench['E_GGE'],
    P_ratio_large=P_at_fold,
    IPR_large=primary_quench['IPR'],
    heat_fraction=primary_quench['heat_fraction'],
    # Vacuum pressure
    P_vac=P_vac,
    E_gs_fold=evals_fold[0],
    first_gap_fold=evals_fold[1] - evals_fold[0],
    gs_occ_fold=gs_occ_fold,
    IPR_gs_fold=IPR_gs_fold,
    # Separation energy
    S3_separation=S3_sep,
    E_N1=evals_N1[0],
    E_N2=evals_N2[0],
    E_N3=evals_fold[0],
    # Cross-comparisons
    r_N1=r_N1,
    r_N2=r_N2,
    # Reference distributions
    r_poisson_ref=r_poisson_ref,
    r_goe_ref=r_goe_ref,
    sigma_poisson=sigma_poisson,
    sigma_goe=sigma_goe,
    # Gate
    gate_name='NPAIR3-ED-56',
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

print(f"\nData saved to computations/session-56/s56_npair3_ed.npz")


# ============================================================
# 14. Plot (3x3 panels)
# ============================================================
fig, axes = plt.subplots(3, 3, figsize=(18, 15))
fig.suptitle(f'NPAIR3-ED-56: $N_{{pair}}=3$ Exact Diagonalization (dim={dim})\n'
             f'Gate: {verdict} | $\\langle r \\rangle_{{fold}}$={r_at_fold:.3f}, '
             f'$\\langle r \\rangle_{{mean}}$={r_full_mean:.3f}, '
             f'$P_{{DE}}/P_{{GGE}}$={P_at_fold:.3f}',
             fontsize=13, fontweight='bold')

# (a) <r> vs tau
ax = axes[0, 0]
ax.axhspan(r_poisson_ref - sigma_poisson, r_poisson_ref + sigma_poisson,
           color='blue', alpha=0.1)
ax.axhspan(r_goe_ref - sigma_goe, r_goe_ref + sigma_goe,
           color='red', alpha=0.1)
ax.axhline(r_poisson_ref, color='blue', ls='--', alpha=0.7, label=f'Poisson ({r_poisson_ref:.3f})')
ax.axhline(r_goe_ref, color='red', ls='--', alpha=0.7, label=f'GOE ({r_goe_ref:.3f})')
ax.axhline(0.53, color='orange', ls=':', alpha=0.9, lw=2, label='PASS threshold (0.53)')
ax.axhline(0.45, color='green', ls=':', alpha=0.9, lw=2, label='FAIL threshold (0.45)')
ax.plot(results['tau_vals'], results['r_full'], 'ko-', ms=7, lw=2, label='Full H (N=3)')
ax.plot(results['tau_vals'], results['r_RG'], 'b^--', ms=5, alpha=0.7, label='RG only (N=3)')
ax.axvline(tau_values[fold_idx], color='gray', ls='-.', alpha=0.5, label='fold')
ax.set_xlabel(r'$\tau$', fontsize=12)
ax.set_ylabel(r'$\langle r \rangle$', fontsize=12)
ax.set_title(r'$\langle r \rangle$ vs $\tau$ ($N_{pair}=3$, dim=56)')
ax.legend(fontsize=6.5, loc='upper left', ncol=2)
ax.set_ylim(0.25, 0.65)

# (b) Alpha_dd sweep (physical range)
ax = axes[0, 1]
ax.axhline(r_poisson_ref, color='blue', ls='--', alpha=0.7, label='Poisson')
ax.axhline(r_goe_ref, color='red', ls='--', alpha=0.7, label='GOE')
ax.axhline(0.53, color='orange', ls=':', alpha=0.7, lw=2, label='PASS')
ax.axhline(0.45, color='green', ls=':', alpha=0.7, lw=2, label='FAIL')
ax.plot(alphas, r_vs_alpha, 'ko-', ms=5, lw=1.5, label=f'$N_{{pair}}=3$')
ax.axvline(1.0, color='green', ls='-', alpha=0.8, lw=2, label=r'Physical $\alpha_{dd}=1$')
ax.set_xlabel(r'$\alpha_{dd}$ (density-density strength)', fontsize=11)
ax.set_ylabel(r'$\langle r \rangle$', fontsize=12)
ax.set_title(r'$\alpha_{dd}$ sweep at fold (dim=56)')
ax.legend(fontsize=7)

# (c) Spectrum at fold
ax = axes[0, 2]
if fold_pos is not None:
    evals_at_fold = results['eigenvalues_full'][fold_pos]
    evals_RG_fold = results['eigenvalues_RG'][fold_pos]
else:
    evals_at_fold = evals_fold
    evals_RG_fold = np.linalg.eigvalsh(build_H(eps_fold, V_bare, alpha_dd=0.0))
ax.plot(range(dim), evals_at_fold - evals_at_fold[0], 'ko', ms=3, label='Full H')
ax.plot(range(dim), evals_RG_fold - evals_RG_fold[0], 'b^', ms=2.5, alpha=0.6, label='RG only')
ax.set_xlabel('Level index', fontsize=11)
ax.set_ylabel(r'$E_n - E_0$ [$M_{KK}$]', fontsize=11)
ax.set_title(f'Spectrum at fold ($\\tau$={tau_values[fold_idx]:.3f}, dim={dim})')
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
ax.hist(s_norm, bins=12, density=True, alpha=0.7, color='steelblue', edgecolor='black', label='Data')
s_plot = np.linspace(0, 4, 200)
ax.plot(s_plot, np.exp(-s_plot), 'b--', lw=2, label='Poisson')
ax.plot(s_plot, (np.pi / 2) * s_plot * np.exp(-np.pi * s_plot**2 / 4), 'r--', lw=2, label='GOE')
ax.set_xlabel(r'$s = \delta E / \langle \delta E \rangle$', fontsize=11)
ax.set_ylabel('P(s)', fontsize=11)
ax.set_title('NNS distribution at fold (dim=56)')
ax.legend()

# (f) Ground state occupations at fold
ax = axes[1, 2]
ax.bar(range(N_modes), gs_occ_fold, color='steelblue', edgecolor='black', alpha=0.8)
ax.set_xlabel('Mode index $k$', fontsize=11)
ax.set_ylabel(r'$\langle n_k \rangle$', fontsize=11)
ax.set_title(f'Ground state occupations (N=3, fold)')
ax.set_xticks(range(N_modes))
ax.set_xticklabels([f'{k}\n({eps_fold[k]:.2f})' for k in range(N_modes)], fontsize=8)

# (g) N_pair comparison (1, 2, 3)
ax = axes[2, 0]
N_pair_list = [1, 2, 3]
r_list = [r_N1, r_N2, r_at_fold]
dims = [8, 28, 56]
colors = ['skyblue', 'steelblue', 'navy']
bars = ax.bar(N_pair_list, r_list, color=colors, edgecolor='black', alpha=0.8)
ax.axhline(r_poisson_ref, color='blue', ls='--', alpha=0.7, label='Poisson')
ax.axhline(r_goe_ref, color='red', ls='--', alpha=0.7, label='GOE')
ax.axhline(0.53, color='orange', ls=':', alpha=0.7, lw=2)
ax.axhline(0.45, color='green', ls=':', alpha=0.7, lw=2)
for i, (n, r, d) in enumerate(zip(N_pair_list, r_list, dims)):
    ax.text(n, r + 0.01, f'{r:.3f}\n(dim={d})', ha='center', fontsize=9)
ax.set_xlabel(r'$N_{pair}$', fontsize=12)
ax.set_ylabel(r'$\langle r \rangle$ at fold', fontsize=12)
ax.set_title(r'$\langle r \rangle$ vs $N_{pair}$ at fold')
ax.set_xticks(N_pair_list)
ax.set_ylim(0.2, 0.65)
ax.legend(fontsize=9)

# (h) Extended alpha sweep
ax = axes[2, 1]
ax.axhline(r_poisson_ref, color='blue', ls='--', alpha=0.7, label='Poisson')
ax.axhline(r_goe_ref, color='red', ls='--', alpha=0.7, label='GOE')
ax.axhline(0.53, color='orange', ls=':', alpha=0.7, lw=2)
ax.plot(alphas_ext, r_ext, 'ko-', ms=3, lw=1)
ax.axvline(1.0, color='green', ls='-', alpha=0.8, lw=2, label=r'$\alpha_{dd}=1$')
ax.set_xlabel(r'$\alpha_{dd}$', fontsize=11)
ax.set_ylabel(r'$\langle r \rangle$', fontsize=12)
ax.set_title(r'Extended $\alpha_{dd}$ sweep (dim=56)')
ax.set_xlim(-1, 55)
ax.legend(fontsize=8)

# (i) P_ratio and IPR vs tau
ax = axes[2, 2]
ax2 = ax.twinx()
l1, = ax.plot(results['tau_vals'], results['P_ratio'], 'go-', ms=5, lw=1.5,
              label=r'$P_{DE}/P_{GGE}$')
l2, = ax2.plot(results['tau_vals'], results['IPR_fold'], 'ms-', ms=5, lw=1.5,
               label=f'IPR/{dim}')
ax.axhline(1.0, color='gray', ls=':', alpha=0.5)
ax.axvline(tau_values[fold_idx], color='gray', ls='-.', alpha=0.5)
ax.set_xlabel(r'$\tau$', fontsize=12)
ax.set_ylabel(r'$P_{vac}(DE) / P_{vac}(GGE)$', fontsize=10, color='green')
ax2.set_ylabel(f'IPR / {dim}', fontsize=10, color='purple')
ax.set_title('Quench diagnostics vs $\\tau$')
lines = [l1, l2]
ax.legend(lines, [l.get_label() for l in lines], fontsize=8, loc='upper left')

plt.tight_layout()
plt.savefig('computations/session-56/s56_npair3_ed.png', dpi=150, bbox_inches='tight')
print(f"Plot saved to computations/session-56/s56_npair3_ed.png")
print()
print("DONE.")
