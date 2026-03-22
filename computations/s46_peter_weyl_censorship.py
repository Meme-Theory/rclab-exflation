#!/usr/bin/env python3
"""
s46_peter_weyl_censorship.py -- PETER-WEYL-CENSORSHIP-46
=========================================================

Retry of S45 killed computation. Tests whether the 17,594x EIH singlet
suppression survives random GOE perturbations at the dissolution scale.

=== PHYSICS ===

The block-diagonal D_K decomposes by SU(3) representation (Peter-Weyl).
The (0,0) singlet contributes S_singlet/S_fold = 5.68e-5 to the full
spectral action -- a 17,594x suppression. Only this singlet fraction
couples to 4D gravity (EIH-GRAV-44).

DISSOLUTION-SCALING-44 showed epsilon_c ~ 0.236/sqrt(N) dissolves the
block structure (Poisson -> GOE). We test whether the singlet fraction
of the SPECTRAL ACTION (an integrated quantity) survives at epsilon_c.

=== METHOD ===

Fixed truncation: max_pq_sum = 2, giving N = 432 (6 sectors).
Critical epsilon: epsilon_c = 1/sqrt(432) = 0.0481.
Perturbation: GOE random Hermitian matrices (real symmetric + Hermitian).
Monte Carlo: 50 realizations per epsilon point.
Epsilon scan: 20 points from eps_c/30 to 10*eps_c (log-spaced).

For each perturbed H = H_0 + epsilon * (||H_0||_F / N) * V_GOE:
  1. Diagonalize: eigenvalues + eigenvectors
  2. Compute singlet weight w_k = sum_{i in singlet} |v_k[i]|^2
  3. Singlet spectral action = sum_k f(lambda_k^2) * w_k
  4. Three functionals: polynomial (lambda^4), curvature (lambda^2), trace-log

Gate: PETER-WEYL-CENSORSHIP-46 (INFO)
  ROBUST if suppression degrades < 2x at eps_c
  FRAGILE if suppression degrades > 10x at eps_c

Input: s44_eih_grav.npz, s44_dissolution_scaling.npz, s42_hauser_feshbach.npz,
       canonical_constants.py
Output: s46_peter_weyl_censorship.{npz,png}

Author: gen-physicist, Session 46
Date: 2026-03-15
"""

import numpy as np
from numpy.linalg import eigh
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import os
import sys
import time

t_start = time.time()

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))

from tier1_dirac_spectrum import (
    su3_generators,
    compute_structure_constants,
    compute_killing_form,
    jensen_metric,
    orthonormal_frame,
    frame_structure_constants,
    connection_coefficients,
    spinor_connection_offset,
    build_cliff8,
    validate_clifford,
    dirac_operator_on_irrep,
    get_irrep,
    validate_connection,
    validate_omega_hermitian,
)
from canonical_constants import tau_fold as TAU_FOLD

# ============================================================
# 0. LOAD PRIOR RESULTS
# ============================================================
print("=" * 72)
print("PETER-WEYL-CENSORSHIP-46")
print("Robustness of EIH singlet suppression under GOE perturbation")
print("=" * 72)

eih_data = np.load('tier0-computation/s44_eih_grav.npz', allow_pickle=True)
diss_data = np.load('tier0-computation/s44_dissolution_scaling.npz', allow_pickle=True)

S_singlet_exact = float(eih_data['S_singlet'])            # 14.23
S_fold_exact = float(eih_data['S_fold'])                   # 250360.68
ratio_exact = float(eih_data['ratio_singlet_to_full'])     # 5.684e-5
suppression_exact = 1.0 / ratio_exact                      # 17,594x
sector_S_fold = eih_data['sector_S_fold']                  # per-sector S at fold
sector_labels_eih = eih_data['sector_labels']              # (p,q) labels

fit_a = float(diss_data['fit_1_sqrtN_params'][0])          # 0.236
N_values_diss = diss_data['N_values']
eps_c_diss = diss_data['epsilon_crossover']

print(f"\n  Exact singlet ratio:    {ratio_exact:.6e}")
print(f"  Exact suppression:      {suppression_exact:.0f}x")
print(f"  Dissolution fit:        eps_c = {fit_a:.4f} / sqrt(N)")
print(f"  Tau:                    {TAU_FOLD}")

# ============================================================
# 1. BUILD SU(3) INFRASTRUCTURE
# ============================================================
print("\n--- Step 1: Build SU(3) infrastructure ---")

gens = su3_generators()
f_abc = compute_structure_constants(gens)
gammas = build_cliff8()
cliff_err = validate_clifford(gammas)
B_ab = compute_killing_form(f_abc)
g_s = jensen_metric(B_ab, TAU_FOLD)
E = orthonormal_frame(g_s)
ft = frame_structure_constants(f_abc, E)
Gamma = connection_coefficients(ft)
mc_err = validate_connection(Gamma)
Omega = spinor_connection_offset(Gamma, gammas)
_, is_ah, h_err, ah_err = validate_omega_hermitian(Omega)

print(f"  Clifford algebra error: {cliff_err:.2e}")
print(f"  Connection metric error: {mc_err:.2e}")
print(f"  Omega anti-Hermitian error: {ah_err:.2e}")

# ============================================================
# 2. BUILD BLOCK-DIAGONAL D_K AT max_pq_sum = 2
# ============================================================
print("\n--- Step 2: Build block-diagonal D_K (max_pq_sum=2, N=432) ---")

MAX_PQ_SUM = 2
N_MC = 50
N_EPS_PTS = 20

np.random.seed(46_2026)

sectors = []
for p in range(MAX_PQ_SUM + 1):
    for q in range(MAX_PQ_SUM + 1 - p):
        dim_pq = (p + 1) * (q + 1) * (p + q + 2) // 2
        rho, dim_check = get_irrep(p, q, gens, f_abc)
        assert dim_check == dim_pq, f"dim mismatch for ({p},{q})"
        D_pi = dirac_operator_on_irrep(rho, E, gammas, Omega)
        H_pi = 1j * D_pi
        block_dim = dim_pq * 16
        sectors.append({
            'pq': (p, q),
            'dim_rep': dim_pq,
            'block_dim': block_dim,
            'H_block': H_pi,
            'is_singlet': (p == 0 and q == 0),
        })

total_dim = sum(s['block_dim'] for s in sectors)
N = total_dim
n_sectors = len(sectors)

H0 = np.zeros((N, N), dtype=complex)
singlet_indices = None
offset = 0
for s in sectors:
    d = s['block_dim']
    H0[offset:offset+d, offset:offset+d] = s['H_block']
    if s['is_singlet']:
        singlet_indices = np.arange(offset, offset + d)
    s['start'] = offset
    s['end'] = offset + d
    offset += d

H0_norm = np.linalg.norm(H0, 'fro')
n_singlet_block = len(singlet_indices)
frac_weyl = n_singlet_block / N

# Critical epsilon
eps_c = 1.0 / np.sqrt(N)  # = 1/sqrt(432) = 0.0481
eps_c_dissolution = fit_a / np.sqrt(N)  # from dissolution fit

# Verify Hermiticity
herm_err = np.linalg.norm(H0 - H0.conj().T, 'fro') / H0_norm
print(f"  N = {N} (total_dim)")
print(f"  n_sectors = {n_sectors}")
print(f"  n_singlet_block = {n_singlet_block}")
print(f"  ||H0||_F = {H0_norm:.4f}")
print(f"  Hermiticity error: {herm_err:.2e}")
print(f"  eps_c = 1/sqrt({N}) = {eps_c:.6f}")
print(f"  eps_c (dissolution fit) = {eps_c_dissolution:.6f}")
print(f"  Weyl fraction = {n_singlet_block}/{N} = {frac_weyl:.6f}")

# Sector summary
print(f"\n  Sector breakdown:")
for s in sectors:
    tag = " <-- SINGLET" if s['is_singlet'] else ""
    print(f"    ({s['pq'][0]},{s['pq'][1]}): dim_rep={s['dim_rep']}, "
          f"block_dim={s['block_dim']}{tag}")

# ============================================================
# 3. EXACT SINGLET FRACTION AT eps=0
# ============================================================
print("\n--- Step 3: Exact singlet fraction (eps=0) ---")

eigenvalues_0, eigenvectors_0 = eigh(H0)
singlet_weights_0 = np.sum(np.abs(eigenvectors_0[singlet_indices, :])**2, axis=0)
abs_evals_0 = np.abs(eigenvalues_0)
pos_mask_0 = abs_evals_0 > 1e-12

# Polynomial (a4-dominated): sum lambda^4
lam4_0 = abs_evals_0**4
S_total_poly_0 = np.sum(lam4_0[pos_mask_0])
S_singlet_poly_0 = np.sum(lam4_0[pos_mask_0] * singlet_weights_0[pos_mask_0])
frac0_poly = S_singlet_poly_0 / S_total_poly_0

# Curvature (a2): sum lambda^2
lam2_0 = abs_evals_0**2
S_total_a2_0 = np.sum(lam2_0[pos_mask_0])
S_singlet_a2_0 = np.sum(lam2_0[pos_mask_0] * singlet_weights_0[pos_mask_0])
frac0_a2 = S_singlet_a2_0 / S_total_a2_0

# Trace-log: sum ln|lambda|
ln_abs_0 = np.log(abs_evals_0[pos_mask_0])
S_total_log_0 = np.sum(np.abs(ln_abs_0))
S_singlet_log_0 = np.sum(np.abs(ln_abs_0) * singlet_weights_0[pos_mask_0])
frac0_log = S_singlet_log_0 / S_total_log_0

n_singlet_dom_0 = int(np.sum(singlet_weights_0 > 0.5))

print(f"  Exact singlet fraction (polynomial/a4): {frac0_poly:.8f}  "
      f"(suppression: {1/frac0_poly:.0f}x)")
print(f"  Exact singlet fraction (curvature/a2):  {frac0_a2:.8f}  "
      f"(suppression: {1/frac0_a2:.0f}x)")
print(f"  Exact singlet fraction (trace-log):     {frac0_log:.8f}  "
      f"(suppression: {1/frac0_log:.0f}x)")
print(f"  Eigenvectors with >50% singlet weight:  {n_singlet_dom_0}/{N}")
print(f"  Weyl equipartition fraction:            {frac_weyl:.8f}  "
      f"(suppression: {1/frac_weyl:.0f}x)")

# Cross-check: the 6-sector truncation frac should differ from the
# 10-sector S44 result because we have fewer sectors
print(f"\n  Cross-check vs S44 (10 sectors): S44 ratio = {ratio_exact:.6e}")
print(f"  6-sector poly ratio (this computation): {frac0_poly:.6e}")
print(f"  Difference expected: 6-sector has fewer non-singlet modes")

# ============================================================
# 4. MONTE CARLO SWEEP: singlet fraction vs epsilon
# ============================================================
print(f"\n--- Step 4: Monte Carlo sweep ({N_MC} realizations, {N_EPS_PTS} eps points) ---")

# Epsilon grid: log-spaced from eps_c/30 to 10*eps_c, plus key points
eps_grid = np.sort(np.unique(np.concatenate([
    [0.0],
    np.geomspace(eps_c / 30, eps_c * 10, N_EPS_PTS),
    [eps_c / 10, eps_c / 3, eps_c, 3 * eps_c, 10 * eps_c],
])))

n_eps = len(eps_grid)
print(f"  eps_grid: {n_eps} points, range [{eps_grid[1]:.6f}, {eps_grid[-1]:.6f}]")
print(f"  eps_c = {eps_c:.6f}")

# Storage
frac_poly_arr = np.zeros((n_eps, N_MC))
frac_a2_arr = np.zeros((n_eps, N_MC))
frac_log_arr = np.zeros((n_eps, N_MC))
n_sing_dom_arr = np.zeros((n_eps, N_MC), dtype=int)
max_singlet_w_arr = np.zeros((n_eps, N_MC))
r_stat_arr = np.zeros((n_eps, N_MC))  # level statistics <r>


def ratio_statistic(evals, tol=1e-10):
    """Oganesyan-Huse <r> from eigenvalues."""
    ev = np.sort(np.real(evals))
    unique = [ev[0]]
    for e in ev[1:]:
        if abs(e - unique[-1]) > tol:
            unique.append(e)
    ev = np.array(unique)
    if len(ev) < 4:
        return np.nan
    spacings = np.diff(ev)
    spacings = spacings[spacings > tol]
    if len(spacings) < 3:
        return np.nan
    ratios = []
    for j in range(len(spacings) - 1):
        s1, s2 = spacings[j], spacings[j+1]
        if max(s1, s2) > 0:
            ratios.append(min(s1, s2) / max(s1, s2))
    return np.mean(ratios) if ratios else np.nan


for i_eps, eps in enumerate(eps_grid):
    sigma = eps * H0_norm / N

    for i_mc in range(N_MC):
        if eps == 0.0:
            H_pert = H0
        else:
            # GOE perturbation: real symmetric part + Hermitian
            V_real = np.random.randn(N, N) * sigma
            V_imag = np.random.randn(N, N) * sigma
            V = (V_real + 1j * V_imag)
            V = (V + V.conj().T) / 2.0
            H_pert = H0 + V

        eigenvalues, eigenvectors = eigh(H_pert)

        # Singlet weight per eigenvector
        sw = np.sum(np.abs(eigenvectors[singlet_indices, :])**2, axis=0)
        abs_ev = np.abs(eigenvalues)
        pm = abs_ev > 1e-12

        # Polynomial (a4)
        l4 = abs_ev**4
        st_poly = np.sum(l4[pm])
        ss_poly = np.sum(l4[pm] * sw[pm])
        frac_poly_arr[i_eps, i_mc] = ss_poly / st_poly if st_poly > 0 else 0.0

        # Curvature (a2)
        l2 = abs_ev**2
        st_a2 = np.sum(l2[pm])
        ss_a2 = np.sum(l2[pm] * sw[pm])
        frac_a2_arr[i_eps, i_mc] = ss_a2 / st_a2 if st_a2 > 0 else 0.0

        # Trace-log
        ln_abs = np.log(abs_ev[pm])
        st_log = np.sum(np.abs(ln_abs))
        ss_log = np.sum(np.abs(ln_abs) * sw[pm])
        frac_log_arr[i_eps, i_mc] = ss_log / st_log if st_log > 0 else 0.0

        n_sing_dom_arr[i_eps, i_mc] = int(np.sum(sw > 0.5))
        max_singlet_w_arr[i_eps, i_mc] = np.max(sw)
        r_stat_arr[i_eps, i_mc] = ratio_statistic(eigenvalues)

    # Progress
    mp = np.mean(frac_poly_arr[i_eps])
    sp = np.std(frac_poly_arr[i_eps]) / np.sqrt(N_MC)
    mr = np.nanmean(r_stat_arr[i_eps])
    label = ""
    if eps == 0:
        label = " [EXACT]"
    elif abs(eps - eps_c) / eps_c < 0.05:
        label = " [eps_c]"
    print(f"  eps={eps:.6f}: frac_poly={mp:.8f} +/- {sp:.2e}  "
          f"<r>={mr:.4f}  n_dom={np.mean(n_sing_dom_arr[i_eps]):.1f}/{n_singlet_block}"
          f"{label}")

t_mc_end = time.time()
print(f"\n  MC sweep time: {t_mc_end - t_start:.1f}s")

# ============================================================
# 5. ANALYSIS
# ============================================================
print("\n--- Step 5: Analysis ---")

mean_poly = np.mean(frac_poly_arr, axis=1)
std_poly = np.std(frac_poly_arr, axis=1) / np.sqrt(N_MC)
mean_a2 = np.mean(frac_a2_arr, axis=1)
std_a2 = np.std(frac_a2_arr, axis=1) / np.sqrt(N_MC)
mean_log = np.mean(frac_log_arr, axis=1)
std_log = np.std(frac_log_arr, axis=1) / np.sqrt(N_MC)
mean_n_dom = np.mean(n_sing_dom_arr, axis=1)
mean_max_sw = np.mean(max_singlet_w_arr, axis=1)
mean_r_stat = np.nanmean(r_stat_arr, axis=1)

# Suppression factor at each epsilon
supp_poly = 1.0 / mean_poly
supp_a2 = 1.0 / mean_a2

# Find key epsilon indices
idx_c = np.argmin(np.abs(eps_grid - eps_c))
idx_third = np.argmin(np.abs(eps_grid - eps_c / 3))
idx_3c = np.argmin(np.abs(eps_grid - 3 * eps_c))
idx_10c = np.argmin(np.abs(eps_grid - 10 * eps_c))

frac_at_epsc = mean_poly[idx_c]
supp_at_epsc = 1.0 / frac_at_epsc
frac_at_10epsc = mean_poly[idx_10c]
supp_at_10epsc = 1.0 / frac_at_10epsc

degradation_at_c = frac_at_epsc / frac0_poly
degradation_at_10c = frac_at_10epsc / frac0_poly

# Where does suppression drop below 100x?
below_100 = np.where(supp_poly < 100)[0]
eps_100x = eps_grid[below_100[0]] if len(below_100) > 0 else None

# Where does <r> cross the Poisson-GOE midpoint?
R_POISSON = 2 * np.log(2) - 1
R_GOE = 0.5307
R_MIDPOINT = (R_POISSON + R_GOE) / 2.0
r_cross_idx = np.where(mean_r_stat > R_MIDPOINT)[0]
eps_r_cross = eps_grid[r_cross_idx[0]] if len(r_cross_idx) > 0 else None

print(f"\n  === KEY RESULTS ===")
print(f"  eps=0 (exact):   frac_poly = {frac0_poly:.8f}  supp = {1/frac0_poly:.0f}x")
print(f"  eps=eps_c/3:     frac_poly = {mean_poly[idx_third]:.8f}  supp = {supp_poly[idx_third]:.0f}x  "
      f"degradation = {mean_poly[idx_third]/frac0_poly:.2f}x")
print(f"  eps=eps_c:       frac_poly = {frac_at_epsc:.8f}  supp = {supp_at_epsc:.0f}x  "
      f"degradation = {degradation_at_c:.2f}x")
print(f"  eps=3*eps_c:     frac_poly = {mean_poly[idx_3c]:.8f}  supp = {supp_poly[idx_3c]:.0f}x  "
      f"degradation = {mean_poly[idx_3c]/frac0_poly:.2f}x")
print(f"  eps=10*eps_c:    frac_poly = {frac_at_10epsc:.8f}  supp = {supp_at_10epsc:.0f}x  "
      f"degradation = {degradation_at_10c:.2f}x")
print(f"  Weyl limit:      frac_weyl = {frac_weyl:.8f}  supp = {1/frac_weyl:.0f}x")
print(f"\n  Level statistics:")
print(f"    <r>(eps=0) = {mean_r_stat[0]:.4f}  (Poisson = {R_POISSON:.4f})")
print(f"    <r>(eps_c) = {mean_r_stat[idx_c]:.4f}  (midpoint = {R_MIDPOINT:.4f})")
print(f"    <r>(10c)   = {mean_r_stat[idx_10c]:.4f}  (GOE = {R_GOE:.4f})")
if eps_r_cross is not None:
    print(f"    <r> crosses midpoint at eps = {eps_r_cross:.6f} = {eps_r_cross/eps_c:.2f} * eps_c")

if eps_100x is not None:
    print(f"\n  Suppression < 100x at eps = {eps_100x:.6f} = {eps_100x/eps_c:.2f} * eps_c")
else:
    print(f"\n  Suppression stays > 100x for all eps tested")

# ============================================================
# 6. THREE-FUNCTIONAL COMPARISON
# ============================================================
print(f"\n--- Step 6: Three-functional comparison at eps_c ---")
print(f"  {'Functional':<20s} {'frac(0)':<14s} {'frac(eps_c)':<14s} "
      f"{'degradation':<14s} {'supp(eps_c)':<14s}")
print(f"  {'-'*72}")
for name, f0, fc in [
    ('Polynomial (a4)', frac0_poly, mean_poly[idx_c]),
    ('Curvature (a2)', frac0_a2, mean_a2[idx_c]),
    ('Trace-log', frac0_log, mean_log[idx_c]),
]:
    deg = fc / f0
    sup = 1.0 / fc
    print(f"  {name:<20s} {f0:<14.8f} {fc:<14.8f} {deg:<14.2f}x {sup:<14.0f}x")

# ============================================================
# 7. REGIME CLASSIFICATION
# ============================================================
print(f"\n--- Step 7: Regime classification ---")

if degradation_at_c < 1.1:
    regime = "ROBUST"
    regime_detail = ("Singlet fraction changes < 10% at eps_c. "
                     "Spectral action censorship is protected by a sum-rule "
                     "mechanism beyond block-diagonality.")
elif degradation_at_c < 2.0:
    regime = "SLIGHTLY DEGRADED"
    regime_detail = ("Singlet fraction changes < 2x at eps_c. "
                     "Spectral action is more robust than level statistics. "
                     "Integrated quantity averages over local mixing.")
elif degradation_at_c < 10.0:
    regime = "MODERATELY DEGRADED"
    regime_detail = ("Singlet fraction changes 2-10x at eps_c. "
                     "Partial censorship survives. "
                     "Analogous to Bondi mass loss with bounded leakage.")
else:
    regime = "FRAGILE"
    regime_detail = ("Singlet fraction changes > 10x at eps_c. "
                     "Censorship depends entirely on block-diagonality. "
                     "Analogous to Cauchy horizon mass inflation.")

print(f"  Regime: {regime}")
print(f"  Detail: {regime_detail}")
print(f"  Degradation at eps_c: {degradation_at_c:.2f}x")
print(f"  Degradation at 10*eps_c: {degradation_at_10c:.2f}x")

# ============================================================
# 8. HAUSER-FESHBACH CONTEXT
# ============================================================
print(f"\n--- Step 8: Hauser-Feshbach context ---")

# Load HF data for context
try:
    hf_data = np.load('tier0-computation/s42_hauser_feshbach.npz', allow_pickle=True)
    doorway_BR_B2 = float(hf_data['doorway_BR_B2'])
    rho_B2 = float(hf_data['rho_B2'])
    print(f"  HF doorway BR(B2) = {doorway_BR_B2:.4f}")
    print(f"  HF level density rho_B2 = {rho_B2:.1f} / M_KK")
    print(f"  Relevance: the Hauser-Feshbach branching determines how")
    print(f"  compound decay populates different KK channels. If Peter-Weyl")
    print(f"  censorship is robust, the 4D gravitational sector is protected")
    print(f"  regardless of the HF branching details.")
    hf_loaded = True
except Exception as e:
    print(f"  HF data not loaded: {e}")
    hf_loaded = False

# ============================================================
# 9. GATE VERDICT
# ============================================================
print(f"\n{'='*72}")
print(f"GATE: PETER-WEYL-CENSORSHIP-46")
print(f"{'='*72}")

verdict = "INFO"

print(f"\n  N = {N} (max_pq_sum = {MAX_PQ_SUM})")
print(f"  eps_c = 1/sqrt({N}) = {eps_c:.6f}")
print(f"  Monte Carlo: {N_MC} realizations per epsilon point")
print(f"  Epsilon grid: {n_eps} points")

print(f"\n  Exact singlet suppression (eps=0): {1/frac0_poly:.0f}x")
print(f"  Suppression at eps_c:              {supp_at_epsc:.0f}x "
      f"(degradation: {degradation_at_c:.2f}x)")
print(f"  Suppression at 10*eps_c:           {supp_at_10epsc:.0f}x "
      f"(degradation: {degradation_at_10c:.2f}x)")
print(f"  Weyl limit:                        {1/frac_weyl:.0f}x")

print(f"\n  Does the 17,594x suppression survive at eps_c?")
if supp_at_epsc > suppression_exact * 0.5:
    survival_status = "YES"
    print(f"  ANSWER: {survival_status}")
    print(f"  Suppression at eps_c ({supp_at_epsc:.0f}x) is > 50% of exact "
          f"({suppression_exact:.0f}x).")
elif supp_at_epsc > 100:
    survival_status = "PARTIAL"
    print(f"  ANSWER: {survival_status}")
    print(f"  Suppression degrades from {suppression_exact:.0f}x to {supp_at_epsc:.0f}x "
          f"but remains > 100x.")
else:
    survival_status = "NO"
    print(f"  ANSWER: {survival_status}")
    print(f"  Suppression degrades from {suppression_exact:.0f}x to {supp_at_epsc:.0f}x "
          f"(< 100x).")

print(f"\n  Regime: {regime}")
print(f"  VERDICT: {verdict}")

# ============================================================
# 10. SAVE DATA
# ============================================================
print(f"\n--- Saving results ---")

save_dict = {
    # Gate
    'gate_verdict': np.array([verdict]),
    'gate_name': np.array(['PETER-WEYL-CENSORSHIP-46']),
    'regime': np.array([regime]),
    'survival_status': np.array([survival_status]),

    # Configuration
    'tau': TAU_FOLD,
    'max_pq_sum': MAX_PQ_SUM,
    'N': N,
    'n_sectors': n_sectors,
    'n_singlet_block': n_singlet_block,
    'n_mc': N_MC,
    'eps_c': eps_c,
    'eps_c_dissolution': eps_c_dissolution,

    # Reference values
    'S_singlet_exact': S_singlet_exact,
    'S_fold_exact': S_fold_exact,
    'ratio_exact': ratio_exact,
    'suppression_exact': suppression_exact,
    'fit_a_dissolution': fit_a,

    # Exact (eps=0) results
    'frac0_poly': frac0_poly,
    'frac0_a2': frac0_a2,
    'frac0_log': frac0_log,
    'frac_weyl': frac_weyl,

    # Epsilon scan
    'eps_grid': eps_grid,
    'mean_poly': mean_poly,
    'std_poly': std_poly,
    'mean_a2': mean_a2,
    'std_a2': std_a2,
    'mean_log': mean_log,
    'std_log': std_log,
    'mean_n_dom': mean_n_dom,
    'mean_max_sw': mean_max_sw,
    'mean_r_stat': mean_r_stat,

    # Key results
    'frac_at_epsc': frac_at_epsc,
    'supp_at_epsc': supp_at_epsc,
    'frac_at_10epsc': frac_at_10epsc,
    'supp_at_10epsc': supp_at_10epsc,
    'degradation_at_c': degradation_at_c,
    'degradation_at_10c': degradation_at_10c,

    # Level statistics
    'R_POISSON': R_POISSON,
    'R_GOE': R_GOE,
    'R_MIDPOINT': R_MIDPOINT,
}

if eps_100x is not None:
    save_dict['eps_100x'] = eps_100x
    save_dict['eps_100x_over_epsc'] = eps_100x / eps_c
if eps_r_cross is not None:
    save_dict['eps_r_cross'] = eps_r_cross
    save_dict['eps_r_cross_over_epsc'] = eps_r_cross / eps_c

np.savez('tier0-computation/s46_peter_weyl_censorship.npz', **save_dict)
print("  Saved: tier0-computation/s46_peter_weyl_censorship.npz")

# ============================================================
# 11. PLOT
# ============================================================
print("  Generating plot...")

fig = plt.figure(figsize=(18, 14))
gs = GridSpec(3, 2, hspace=0.40, wspace=0.30)

# --- Panel 1: Singlet fraction (polynomial) vs epsilon ---
ax1 = fig.add_subplot(gs[0, 0])
mask = eps_grid > 0
ax1.errorbar(eps_grid[mask], mean_poly[mask], yerr=std_poly[mask],
             fmt='o-', color='#1f77b4', markersize=4, linewidth=1.5,
             capsize=2, label=f'MC ({N_MC} realizations)')
ax1.axhline(frac0_poly, color='red', linestyle='--', alpha=0.7,
            label=f'Exact (eps=0): {frac0_poly:.2e}')
ax1.axhline(frac_weyl, color='gray', linestyle='-.', alpha=0.5,
            label=f'Weyl limit: {frac_weyl:.4f}')
ax1.axvline(eps_c, color='green', linestyle=':', alpha=0.7,
            label=f'eps_c = 1/sqrt({N}) = {eps_c:.4f}')
ax1.axvline(eps_c_dissolution, color='orange', linestyle=':', alpha=0.5,
            label=f'eps_c(diss) = {eps_c_dissolution:.4f}')
ax1.set_xlabel(r'$\epsilon$ (perturbation strength)', fontsize=11)
ax1.set_ylabel(r'Singlet fraction of $\sum \lambda^4$', fontsize=11)
ax1.set_title(r'Peter-Weyl Censorship: Singlet Fraction vs $\epsilon$', fontsize=12)
ax1.set_xscale('log')
ax1.set_yscale('log')
ax1.legend(fontsize=8)
ax1.grid(True, alpha=0.3)

# --- Panel 2: Suppression factor vs epsilon ---
ax2 = fig.add_subplot(gs[0, 1])
ax2.plot(eps_grid[mask], supp_poly[mask], 'o-', color='#1f77b4', markersize=4,
         linewidth=1.5, label='Polynomial (a4)')
ax2.plot(eps_grid[mask], supp_a2[mask], 's--', color='#ff7f0e', markersize=3,
         linewidth=1.2, alpha=0.7, label='Curvature (a2)')
ax2.axhline(suppression_exact, color='red', linestyle='--', alpha=0.5,
            label=f'S44 exact: {suppression_exact:.0f}x')
ax2.axhline(100, color='gray', linestyle=':', alpha=0.5, label='100x threshold')
ax2.axhline(1.0 / frac_weyl, color='purple', linestyle='-.', alpha=0.3,
            label=f'Weyl limit: {1/frac_weyl:.0f}x')
ax2.axvline(eps_c, color='green', linestyle=':', alpha=0.7, label=r'$\epsilon_c$')
ax2.set_xlabel(r'$\epsilon$', fontsize=11)
ax2.set_ylabel('Suppression factor (1 / singlet fraction)', fontsize=11)
ax2.set_title('EIH Suppression Factor vs Perturbation', fontsize=12)
ax2.set_xscale('log')
ax2.set_yscale('log')
ax2.legend(fontsize=8)
ax2.grid(True, alpha=0.3)

# --- Panel 3: Relative degradation vs eps/eps_c ---
ax3 = fig.add_subplot(gs[1, 0])
x_norm = eps_grid[mask] / eps_c
y_norm = mean_poly[mask] / frac0_poly
ax3.plot(x_norm, y_norm, 'o-', color='#1f77b4', markersize=4, linewidth=1.5,
         label='Polynomial (a4)')
y_norm_a2 = mean_a2[mask] / frac0_a2
ax3.plot(x_norm, y_norm_a2, 's--', color='#ff7f0e', markersize=3, linewidth=1.2,
         alpha=0.7, label='Curvature (a2)')
y_norm_log = mean_log[mask] / frac0_log
ax3.plot(x_norm, y_norm_log, '^:', color='#2ca02c', markersize=3, linewidth=1.2,
         alpha=0.7, label='Trace-log')
ax3.axhline(1.0, color='black', linestyle='-', alpha=0.3, label='No degradation')
ax3.axhline(2.0, color='red', linestyle='--', alpha=0.3, label='2x degradation')
ax3.axhline(10.0, color='darkred', linestyle='--', alpha=0.2, label='10x degradation')
ax3.axvline(1.0, color='green', linestyle=':', alpha=0.5, label=r'$\epsilon = \epsilon_c$')
ax3.set_xlabel(r'$\epsilon / \epsilon_c$', fontsize=11)
ax3.set_ylabel(r'$f(\epsilon) / f(0)$ (relative degradation)', fontsize=11)
ax3.set_title(r'Relative Censorship Degradation (normalized to $\epsilon_c$)', fontsize=12)
ax3.set_xscale('log')
ax3.set_yscale('log')
ax3.legend(fontsize=8)
ax3.grid(True, alpha=0.3)

# --- Panel 4: Level statistics <r> vs epsilon ---
ax4 = fig.add_subplot(gs[1, 1])
ax4.plot(eps_grid[mask], mean_r_stat[mask], 'ko-', markersize=4, linewidth=1.5)
ax4.axhline(R_POISSON, color='blue', linestyle='--', linewidth=1,
            label=f'Poisson ({R_POISSON:.3f})')
ax4.axhline(R_GOE, color='red', linestyle='--', linewidth=1,
            label=f'GOE ({R_GOE:.3f})')
ax4.axhline(R_MIDPOINT, color='gray', linestyle=':', linewidth=1,
            label=f'Midpoint ({R_MIDPOINT:.3f})')
ax4.axvline(eps_c, color='green', linestyle=':', alpha=0.7, label=r'$\epsilon_c$')
ax4.set_xlabel(r'$\epsilon$', fontsize=11)
ax4.set_ylabel(r'$\langle r \rangle$ (level spacing ratio)', fontsize=11)
ax4.set_title(r'Level Statistics: Poisson $\to$ GOE Transition', fontsize=12)
ax4.set_xscale('log')
ax4.set_ylim(0.30, 0.60)
ax4.legend(fontsize=9)
ax4.grid(True, alpha=0.3)

# --- Panel 5: Singlet-dominant eigenvector count ---
ax5 = fig.add_subplot(gs[2, 0])
ax5.plot(eps_grid[mask], mean_n_dom[mask], 'o-', color='#1f77b4',
         markersize=4, linewidth=1.5)
ax5.axhline(n_singlet_block, color='red', linestyle='--', alpha=0.5,
            label=f'Singlet block size: {n_singlet_block}')
ax5.axvline(eps_c, color='green', linestyle=':', alpha=0.7, label=r'$\epsilon_c$')
ax5.set_xlabel(r'$\epsilon$', fontsize=11)
ax5.set_ylabel('Eigenvectors with >50% singlet weight', fontsize=11)
ax5.set_title('Singlet-Dominant Eigenvector Count', fontsize=12)
ax5.set_xscale('log')
ax5.legend(fontsize=9)
ax5.grid(True, alpha=0.3)

# --- Panel 6: Max singlet weight ---
ax6 = fig.add_subplot(gs[2, 1])
ax6.plot(eps_grid[mask], mean_max_sw[mask], 'o-', color='#1f77b4',
         markersize=4, linewidth=1.5)
ax6.axhline(1.0, color='black', linestyle='-', alpha=0.3)
ax6.axvline(eps_c, color='green', linestyle=':', alpha=0.7, label=r'$\epsilon_c$')
ax6.set_xlabel(r'$\epsilon$', fontsize=11)
ax6.set_ylabel('Max singlet weight of any eigenvector', fontsize=11)
ax6.set_title('Eigenvector Localization in Singlet Block', fontsize=12)
ax6.set_xscale('log')
ax6.legend(fontsize=9)
ax6.grid(True, alpha=0.3)

fig.suptitle(f'PETER-WEYL-CENSORSHIP-46: Robustness of EIH Singlet Suppression\n'
             f'N={N} | Exact suppression: {1/frac0_poly:.0f}x | '
             f'eps_c = 1/sqrt({N}) = {eps_c:.4f} | {N_MC} MC | '
             f'Regime: {regime}',
             fontsize=13, fontweight='bold')

plt.savefig('tier0-computation/s46_peter_weyl_censorship.png', dpi=150, bbox_inches='tight')
print("  Saved: tier0-computation/s46_peter_weyl_censorship.png")

# ============================================================
# 12. FINAL SUMMARY
# ============================================================
t_end = time.time()
total_time = t_end - t_start

print(f"\n{'='*72}")
print(f"PETER-WEYL-CENSORSHIP-46: FINAL SUMMARY")
print(f"{'='*72}")

print(f"\n  Total runtime: {total_time:.1f}s ({total_time/60:.1f}min)")
print(f"\n  QUESTION: Does the {suppression_exact:.0f}x EIH suppression "
      f"survive at eps_c = 1/sqrt({N})?")
print(f"\n  ANSWER: {survival_status}")
print(f"    eps=0:      suppression = {1/frac0_poly:.0f}x")
print(f"    eps=eps_c:  suppression = {supp_at_epsc:.0f}x  "
      f"(degradation: {degradation_at_c:.2f}x)")
print(f"    eps=10*c:   suppression = {supp_at_10epsc:.0f}x  "
      f"(degradation: {degradation_at_10c:.2f}x)")
print(f"    Weyl limit: suppression = {1/frac_weyl:.0f}x")

print(f"\n  LEVEL STATISTICS vs SPECTRAL ACTION:")
print(f"    <r> crosses Poisson-GOE midpoint at eps ~ {eps_r_cross:.4f}" if eps_r_cross else
      f"    <r> does not cross midpoint in scan range")
print(f"    Singlet fraction degradation at eps_c: {degradation_at_c:.2f}x")
print(f"    => Spectral action is {'MORE' if degradation_at_c < 2.0 else 'LESS'} "
      f"robust than level statistics")

print(f"\n  REGIME: {regime}")
print(f"  {regime_detail}")

print(f"\n  CONSTRAINT MAP UPDATE:")
print(f"    The Peter-Weyl singlet projection provides {np.log10(1/frac0_poly):.1f} orders")
print(f"    of CC suppression at eps=0 (exact block-diagonality).")
print(f"    At the dissolution scale eps_c = {eps_c:.4f}:")
print(f"      Suppression = {supp_at_epsc:.0f}x = {np.log10(supp_at_epsc):.1f} orders")
print(f"    The censorship is {regime.lower()}: "
      f"{'structurally protected' if regime in ['ROBUST', 'SLIGHTLY DEGRADED'] else 'conditional on near-block-diagonality'}")

print(f"\n  Gate: {verdict}")
print(f"{'='*72}")
