#!/usr/bin/env python3
"""
S54 MODULUS-FLUCT-54: Modulus fluctuation spectrum from the 32-cell lattice Hamiltonian
=======================================================================================

Computes delta_tau(K) -- the modulus fluctuation power spectrum -- from the
tight-binding Hamiltonian on the 32-cell SU(3) representation graph.

Physics:
  Each cell i in the 32-cell lattice corresponds to an irreducible representation
  (p_i, q_i) of SU(3). The modulus tau controls the Jensen-deformed metric on SU(3).

  Fluctuations of tau across the lattice are sourced by quantum zero-point motion
  in the modulus potential. The effective Hamiltonian for modulus fluctuations is:

    H_tau = (1/2) sum_i pi_i^2 / M_i + (1/2) sum_{<ij>} K_{ij} (tau_i - tau_j)^2
            + (1/2) sum_i m_i^2 tau_i^2

  where K_{ij} = (dJ_{ij}/dtau)^2 / E_scale is the bond stiffness,
  and m_i^2 = d^2 epsilon_i / dtau^2 is the on-site mass-squared.

  The power spectrum P(lambda_k) in the graph Laplacian eigenbasis:
    P(lambda_k) = sum_m |<u_k|v_m>|^2 / (2 omega_m)
  where omega_m^2 are eigenvalues of the dynamical matrix, and |u_k> are
  graph Laplacian eigenvectors.

Methods:
  A. Susceptibility (quantum response): chi(i,j) = sum_{k>0} psi_k(i)psi_k(j)/(N*Delta_E_k)
  B. Dynamical matrix: M = K_stiffness + diag(m_i^2), P ~ 1/(2*omega)
  C. Thermally-weighted: rho(i) from Boltzmann weights at T = Delta_E (gap)

Gate: MODULUS-FLUCT-54
  PASS: n_s in [0.93, 0.98]
  FAIL: n_s > 1 (blue) or n_s < 0.90 (too red)

Author: quantum-foam-theorist (S54)
"""

import numpy as np
from scipy import stats
from scipy.sparse.csgraph import shortest_path
import sys
import os

# Import canonical constants
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    M_KK, tau_fold, A_s_CMB, l_Planck
)

# ============================================================================
# 0. LOAD DATA
# ============================================================================

data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         's54_tb_hamiltonian.npz')
data = np.load(data_path, allow_pickle=True)

tau_values = data['tau_values']    # (50,)
eigenvalues = data['eigenvalues']  # (50, 32)
eigenvectors = data['eigenvectors']  # (50, 32, 32)
hamiltonians = data['hamiltonians']  # (50, 32, 32)
adjacency = data['adjacency'].astype(float)  # (32, 32)
cell_labels = data['cell_labels']  # (32, 2)
cell_casimirs = data['cell_casimirs']  # (32,)
cell_dims = data['cell_dims']  # (32,)

N_cells = int(data['N_cells'])
dtau = tau_values[1] - tau_values[0]

print(f"Loaded: {N_cells} cells, {len(tau_values)} tau values")
print(f"tau range: [{tau_values[0]:.4f}, {tau_values[-1]:.4f}], dtau = {dtau:.6f}")

# ============================================================================
# 1. GRAPH LAPLACIAN (defines Fourier basis for the graph)
# ============================================================================

degree = np.diag(adjacency.sum(axis=1))
L_graph = degree - adjacency
lap_eigs, lap_vecs = np.linalg.eigh(L_graph)

print(f"\nGraph Laplacian spectrum:")
print(f"  lambda_0 = {lap_eigs[0]:.2e} (should be ~0)")
print(f"  lambda_1 = {lap_eigs[1]:.4f} (spectral gap)")
print(f"  lambda_max = {lap_eigs[-1]:.4f}")

# Graph distance matrix
dist_matrix = shortest_path(adjacency, directed=False, unweighted=True).astype(int)
max_dist = dist_matrix.max()
print(f"  Graph diameter: {max_dist}")

# ============================================================================
# 2. SELECT TAU VALUE NEAR THE FOLD
# ============================================================================

# Primary computation at tau ~ tau_fold
tau_target = tau_fold
tau_idx = np.argmin(np.abs(tau_values - tau_target))
tau_actual = tau_values[tau_idx]
print(f"\nPrimary tau = {tau_actual:.4f} (index {tau_idx}, target {tau_target})")

H = hamiltonians[tau_idx]
eigs = eigenvalues[tau_idx]
vecs = eigenvectors[tau_idx]  # vecs[:, k] = k-th eigenvector

E_gap = eigs[1] - eigs[0]
print(f"  E_0 = {eigs[0]:.6e} M_KK")
print(f"  E_1 = {eigs[1]:.6e} M_KK")
print(f"  Gap = {E_gap:.6e} M_KK")

# Check ground state uniformity (Perron-Frobenius)
psi0 = vecs[:, 0]
psi0_std = np.std(np.abs(psi0)) / np.mean(np.abs(psi0))
print(f"  Ground state uniformity: std/mean = {psi0_std:.2e}")

# ============================================================================
# 3. METHOD A: SUSCEPTIBILITY (quantum fluctuation correlation)
# ============================================================================
# chi(i,j) = (1/N) sum_{k>0} psi_k(i) * psi_k(j) / (E_k - E_0)
# This is the zero-temperature quantum fluctuation correlation function
# of the density operator n_i = |i><i|

print("\n=== METHOD A: SUSCEPTIBILITY ===")

chi = np.zeros((N_cells, N_cells))
for k in range(1, N_cells):
    dE = eigs[k] - eigs[0]
    if dE < 1e-14:
        continue
    psi_k = vecs[:, k]
    chi += np.outer(psi_k, psi_k) / dE
chi /= N_cells

# Graph Fourier transform of chi: P_A(k) = chi_hat(k,k)
chi_hat = lap_vecs.T @ chi @ lap_vecs
P_A = np.array([chi_hat[k, k] for k in range(N_cells)])

# Fit spectral index (skip zero mode)
lam_A = lap_eigs[1:]
PA_fit = P_A[1:]
mask_A = PA_fit > 0
log_lam_A = np.log(lam_A[mask_A])
log_PA = np.log(PA_fit[mask_A])
slope_A, intercept_A, r_A, pval_A, se_A = stats.linregress(log_lam_A, log_PA)
alpha_A = slope_A
ns_A = 1 + 2 * alpha_A
ns_A_err = 2 * se_A

print(f"  P_A(lambda_1) = {P_A[1]:.4e}")
print(f"  P_A(lambda_max) = {P_A[-1]:.4e}")
print(f"  Ratio P_1/P_max = {P_A[1]/P_A[-1]:.2f}")
print(f"  Fit: alpha = {alpha_A:.4f} +/- {se_A:.4f}")
print(f"  n_s = {ns_A:.4f} +/- {ns_A_err:.4f}")
print(f"  R^2 = {r_A**2:.4f}")

# ============================================================================
# 4. METHOD B: DYNAMICAL MATRIX (modulus effective Hamiltonian)
# ============================================================================
# The modulus tau is a FIELD on the graph. Its dynamics:
#   omega_k^2 = eigenvalue of dynamical matrix M
#   M = K_stiffness_laplacian + diag(m_i^2)
#
# Bond stiffness: K_{ij} = (dH_{ij}/dtau)^2 (how hopping changes with tau)
# On-site mass: m_i^2 = d^2 H_{ii}/dtau^2 (curvature of on-site potential)
#
# Power spectrum: P_B(k) = sum_m |<u_k|v_m>|^2 / (2*omega_m)

print("\n=== METHOD B: DYNAMICAL MATRIX ===")

# Numerical derivatives of H wrt tau
if tau_idx > 0 and tau_idx < len(tau_values) - 1:
    H_plus = hamiltonians[tau_idx + 1]
    H_minus = hamiltonians[tau_idx - 1]
    dH_dtau = (H_plus - H_minus) / (2 * dtau)
    d2H_dtau2 = (H_plus - 2 * H + H_minus) / dtau**2
else:
    raise ValueError(f"tau_idx={tau_idx} at boundary, cannot compute derivatives")

# On-site mass-squared
m_sq = np.diag(d2H_dtau2)
print(f"  On-site mass^2: mean={m_sq.mean():.3f}, std={np.std(m_sq):.3f}")
print(f"    range: [{m_sq.min():.3f}, {m_sq.max():.3f}]")

# Bond stiffness (from hopping derivative)
K_bond = np.zeros((N_cells, N_cells))
for i in range(N_cells):
    for j in range(N_cells):
        if adjacency[i, j] > 0:
            K_bond[i, j] = dH_dtau[i, j]**2

# Build stiffness Laplacian
K_lap = np.zeros((N_cells, N_cells))
for i in range(N_cells):
    for j in range(N_cells):
        if i != j and adjacency[i, j] > 0:
            K_lap[i, j] = -K_bond[i, j]
            K_lap[i, i] += K_bond[i, j]

K_avg = K_bond[adjacency > 0].mean()
print(f"  Bond stiffness: mean={K_avg:.4f}")

# Dynamical matrix: M = K_lap + diag(|m_sq|)
# Use |m_sq| since we need positive-definite matrix for omega^2
M_dyn = K_lap + np.diag(np.abs(m_sq))
dyn_eigs, dyn_vecs = np.linalg.eigh(M_dyn)

print(f"  Dynamical eigenvalues: [{dyn_eigs[0]:.4f}, ..., {dyn_eigs[-1]:.4f}]")
print(f"  omega_0 = {np.sqrt(max(dyn_eigs[0], 0)):.4f} M_KK")
print(f"  omega_max = {np.sqrt(dyn_eigs[-1]):.4f} M_KK")

# Mass-to-stiffness ratio (controls the tilt)
# If m >> K*lambda_max: nearly flat spectrum (n_s ~ 1)
# If m << K*lambda_max: steep spectrum
ratio_mK = np.mean(np.abs(m_sq)) / (K_avg * lap_eigs[-1])
print(f"  m^2 / (K * lambda_max) = {ratio_mK:.3f}")

# Power spectrum in graph Laplacian basis
overlap_B = lap_vecs.T @ dyn_vecs
P_B = np.zeros(N_cells)
for k in range(N_cells):
    for m in range(N_cells):
        if dyn_eigs[m] > 1e-14:
            P_B[k] += overlap_B[k, m]**2 / (2 * np.sqrt(dyn_eigs[m]))

# Fit (all modes)
lam_B = lap_eigs[1:]
PB_fit = P_B[1:]
mask_B = PB_fit > 0
log_lam_B = np.log(lam_B[mask_B])
log_PB = np.log(PB_fit[mask_B])
slope_B, intercept_B, r_B, pval_B, se_B = stats.linregress(log_lam_B, log_PB)
alpha_B = slope_B
ns_B = 1 + 2 * alpha_B
ns_B_err = 2 * se_B

print(f"\n  Full fit ({mask_B.sum()} modes):")
print(f"    alpha = {alpha_B:.4f} +/- {se_B:.4f}")
print(f"    n_s = {ns_B:.4f} +/- {ns_B_err:.4f}")
print(f"    R^2 = {r_B**2:.4f}")

# Fit IR modes only (first 10 non-zero)
n_IR = min(10, N_cells - 1)
lam_IR = lap_eigs[1:n_IR+1]
P_IR = P_B[1:n_IR+1]
mask_IR = P_IR > 0
if mask_IR.sum() >= 3:
    log_lam_IR = np.log(lam_IR[mask_IR])
    log_P_IR = np.log(P_IR[mask_IR])
    slope_IR, intercept_IR, r_IR, pval_IR, se_IR = stats.linregress(log_lam_IR, log_P_IR)
    alpha_IR = slope_IR
    ns_IR = 1 + 2 * alpha_IR
    ns_IR_err = 2 * se_IR
    print(f"\n  IR fit (first {mask_IR.sum()} modes, lambda < {lam_IR[mask_IR][-1]:.2f}):")
    print(f"    alpha = {alpha_IR:.4f} +/- {se_IR:.4f}")
    print(f"    n_s = {ns_IR:.4f} +/- {ns_IR_err:.4f}")
    print(f"    R^2 = {r_IR**2:.4f}")
else:
    ns_IR = ns_B
    ns_IR_err = ns_B_err
    alpha_IR = alpha_B
    r_IR = r_B

# ============================================================================
# 5. METHOD C: THERMAL FLUCTUATIONS (Boltzmann at T = gap)
# ============================================================================

print("\n=== METHOD C: THERMAL FLUCTUATIONS ===")

T_eff = E_gap  # effective temperature = energy gap
boltz = np.exp(-(eigs - eigs[0]) / T_eff)
Z = boltz.sum()

# Thermal density at each site
rho_th = np.zeros(N_cells)
for k in range(N_cells):
    rho_th += boltz[k] * vecs[:, k]**2
rho_th /= Z

delta_rho = rho_th - rho_th.mean()

# Graph Fourier transform
delta_rho_hat = lap_vecs.T @ delta_rho
P_C = delta_rho_hat**2

# Fit
lam_C = lap_eigs[1:]
PC_fit = P_C[1:]
mask_C = PC_fit > 1e-30
if mask_C.sum() >= 3:
    log_lam_C = np.log(lam_C[mask_C])
    log_PC = np.log(PC_fit[mask_C])
    slope_C, intercept_C, r_C, pval_C, se_C = stats.linregress(log_lam_C, log_PC)
    ns_C = 1 + 2 * slope_C
    ns_C_err = 2 * se_C
    print(f"  n_s = {ns_C:.4f} +/- {ns_C_err:.4f}, R^2 = {r_C**2:.4f}")
else:
    ns_C = np.nan
    ns_C_err = np.nan
    r_C = 0
    slope_C = np.nan
    print("  Too few nonzero modes for fit")

# ============================================================================
# 6. METHOD D: DIMENSION-WEIGHTED FLUCTUATIONS
# ============================================================================
# Physical: cells with larger dim(p,q) have more degrees of freedom
# and contribute more to the modulus average. The fluctuation of the
# dimension-weighted modulus response:
# delta_tau(i) propto d_i * (H_{ii} - <H_ii>_weighted) / <d>
# This captures the representation-theoretic structure

print("\n=== METHOD D: DIMENSION-WEIGHTED ===")

# Dimension-weighted on-site energy
H_diag = np.diag(H)
d_weights = cell_dims / cell_dims.sum()  # probability weights
H_mean_weighted = np.sum(d_weights * H_diag)

# Fluctuation weighted by dimension
delta_tau_D = cell_dims * (H_diag - H_mean_weighted) / cell_dims.mean()
delta_tau_D -= delta_tau_D.mean()  # ensure zero mean

# Graph Fourier transform
dt_hat_D = lap_vecs.T @ delta_tau_D
P_D = dt_hat_D**2

lam_D = lap_eigs[1:]
PD_fit = P_D[1:]
mask_D = PD_fit > 1e-30
if mask_D.sum() >= 3:
    log_lam_D = np.log(lam_D[mask_D])
    log_PD = np.log(PD_fit[mask_D])
    slope_D, intercept_D, r_D, pval_D, se_D = stats.linregress(log_lam_D, log_PD)
    ns_D = 1 + 2 * slope_D
    ns_D_err = 2 * se_D
    print(f"  n_s = {ns_D:.4f} +/- {ns_D_err:.4f}, R^2 = {r_D**2:.4f}")
else:
    ns_D = np.nan
    ns_D_err = np.nan
    r_D = 0
    slope_D = np.nan
    print("  Too few nonzero modes for fit")

# ============================================================================
# 7. METHOD E: STRUCTURE FACTOR (direct density-density correlation)
# ============================================================================
# The modulus-modulus correlation C(d) on the graph
# C(d) = <delta_tau(i) delta_tau(j)>_{d(i,j)=d}
# Uses the susceptibility (Method A) as the correlation function

print("\n=== METHOD E: CORRELATION FUNCTION C(d) ===")

# Use susceptibility as the correlation
C_d = np.zeros(max_dist + 1)
count_d = np.zeros(max_dist + 1)
for i in range(N_cells):
    for j in range(N_cells):
        d = dist_matrix[i, j]
        C_d[d] += chi[i, j]
        count_d[d] += 1

C_d_avg = np.zeros(max_dist + 1)
for d in range(max_dist + 1):
    if count_d[d] > 0:
        C_d_avg[d] = C_d[d] / count_d[d]

# Normalize: C(d) -> C(d) - C_mean, then C(0) = 1
C_fluct = C_d_avg - np.mean(C_d_avg[1:])  # subtract off-diagonal mean
if abs(C_fluct[0]) > 1e-15:
    C_norm = C_fluct / C_fluct[0]
else:
    C_norm = C_fluct

print(f"  Graph distances: 0 to {max_dist}")
for d in range(max_dist + 1):
    print(f"    C(d={d}) = {C_d_avg[d]:.6e}  (normalized: {C_norm[d]:.6f}, {int(count_d[d])} pairs)")

# ============================================================================
# 8. TAU SWEEP: n_s vs tau
# ============================================================================

print("\n=== TAU SWEEP ===")

ns_tau_B = np.zeros(len(tau_values))
ns_tau_B_err = np.zeros(len(tau_values))
P_B_all = np.zeros((len(tau_values), N_cells))

for tidx in range(1, len(tau_values) - 1):  # skip boundaries for derivative
    H_t = hamiltonians[tidx]
    H_tp = hamiltonians[tidx + 1]
    H_tm = hamiltonians[tidx - 1]

    dH_t = (H_tp - H_tm) / (2 * dtau)
    d2H_t = (H_tp - 2 * H_t + H_tm) / dtau**2

    m_sq_t = np.diag(d2H_t)

    K_lap_t = np.zeros((N_cells, N_cells))
    for i in range(N_cells):
        for j in range(N_cells):
            if i != j and adjacency[i, j] > 0:
                k_ij = dH_t[i, j]**2
                K_lap_t[i, j] = -k_ij
                K_lap_t[i, i] += k_ij

    M_dyn_t = K_lap_t + np.diag(np.abs(m_sq_t))
    de, dv = np.linalg.eigh(M_dyn_t)

    ov = lap_vecs.T @ dv
    P_t = np.zeros(N_cells)
    for k in range(N_cells):
        for m in range(N_cells):
            if de[m] > 1e-14:
                P_t[k] += ov[k, m]**2 / (2 * np.sqrt(de[m]))
    P_B_all[tidx] = P_t

    lam_fit = lap_eigs[1:]
    P_fit = P_t[1:]
    mask = P_fit > 0
    if mask.sum() >= 3:
        log_l = np.log(lam_fit[mask])
        log_p = np.log(P_fit[mask])
        sl, _, rv, _, srv = stats.linregress(log_l, log_p)
        ns_tau_B[tidx] = 1 + 2 * sl
        ns_tau_B_err[tidx] = 2 * srv

# Report n_s at key tau values
print(f"{'tau':>8s} {'n_s':>8s} {'n_s_err':>8s}")
for tidx in [5, 10, 15, 19, 25, 30, 35, 40, 45]:
    if tidx < len(tau_values) - 1 and tidx > 0:
        print(f"  {tau_values[tidx]:.4f}  {ns_tau_B[tidx]:.4f}  {ns_tau_B_err[tidx]:.4f}")

# ============================================================================
# 9. ALTERNATIVE: BROKEN GROUND STATE (Casimir-induced)
# ============================================================================
# The ground state is uniform due to Perron-Frobenius, BUT the physical
# modulus fluctuation isn't about the ground state wavefunction --
# it's about the ENERGY LANDSCAPE across cells.
#
# The Casimir C_2(i) sets the energy scale for each cell.
# The modulus variation: delta_tau(i) ~ dE_i/dtau ~ d C_2(i) J(tau) / dtau
# This is a DETERMINISTIC field on the graph, not quantum.
# Its power spectrum tells us the spatial structure of the modulus landscape.

print("\n=== METHOD F: CASIMIR-GRADIENT FIELD ===")

# The Casimir field on the graph
cas_mean = cell_casimirs.mean()
delta_cas = cell_casimirs - cas_mean

# Graph Fourier transform
dc_hat = lap_vecs.T @ delta_cas
P_F = dc_hat**2

lam_F = lap_eigs[1:]
PF_fit = P_F[1:]
mask_F = PF_fit > 1e-30
if mask_F.sum() >= 3:
    log_lam_F = np.log(lam_F[mask_F])
    log_PF = np.log(PF_fit[mask_F])
    slope_F, intercept_F, r_F, pval_F, se_F = stats.linregress(log_lam_F, log_PF)
    ns_F = 1 + 2 * slope_F
    ns_F_err = 2 * se_F
    print(f"  Casimir field n_s = {ns_F:.4f} +/- {ns_F_err:.4f}, R^2 = {r_F**2:.4f}")
else:
    ns_F = np.nan
    ns_F_err = np.nan
    slope_F = np.nan
    r_F = 0
    print("  Too few nonzero modes")

# ============================================================================
# 10. PRIMARY RESULT: best-fit n_s and uncertainty
# ============================================================================

print("\n" + "="*70)
print("SUMMARY OF SPECTRAL INDICES")
print("="*70)

methods = {
    'A (susceptibility)':    (ns_A, ns_A_err, r_A**2),
    'B (dyn. matrix, full)': (ns_B, ns_B_err, r_B**2),
    'B (dyn. matrix, IR)':   (ns_IR, ns_IR_err, r_IR**2 if isinstance(r_IR, float) else r_IR),
    'C (thermal)':           (ns_C, ns_C_err, r_C**2 if not np.isnan(ns_C) else 0),
    'D (dim-weighted)':      (ns_D, ns_D_err, r_D**2 if not np.isnan(ns_D) else 0),
    'F (Casimir gradient)':  (ns_F, ns_F_err, r_F**2 if not np.isnan(ns_F) else 0),
}

print(f"\n{'Method':<25s} {'n_s':>8s} {'err':>8s} {'R^2':>8s}")
print("-" * 55)
for name, (ns, err, r2) in methods.items():
    print(f"  {name:<23s} {ns:8.4f} {err:8.4f} {r2:8.4f}")

# The PRIMARY result is Method B (dynamical matrix) -- it captures the
# correct physics of a massive scalar field on the graph.
# Full fit is the honest number; IR fit is more relevant for cosmology.
ns_primary = ns_B
ns_primary_err = ns_B_err

print(f"\n*** PRIMARY: n_s = {ns_primary:.4f} +/- {ns_primary_err:.4f} (Method B, full)")
print(f"*** IR fit:  n_s = {ns_IR:.4f} +/- {ns_IR_err:.4f} (Method B, first 10 modes)")

# ============================================================================
# 11. GATE VERDICT
# ============================================================================

gate_pass_lo, gate_pass_hi = 0.93, 0.98
gate_fail_blue = 1.0  # (local)
gate_fail_too_red = 0.90  # (local)

# Check both full and IR fits
all_ns = [ns_B, ns_IR]
all_labels = ['B_full', 'B_IR']

best_ns = ns_B  # primary result

if gate_pass_lo <= best_ns <= gate_pass_hi:
    verdict = "PASS"
    detail = f"n_s = {best_ns:.4f} in [{gate_pass_lo}, {gate_pass_hi}]"
elif best_ns > gate_fail_blue:
    verdict = "FAIL"
    detail = f"n_s = {best_ns:.4f} > 1.0 (blue tilt)"
elif best_ns < gate_fail_too_red:
    verdict = "FAIL"
    detail = f"n_s = {best_ns:.4f} < 0.90 (too red)"
else:
    # Between 0.90 and 0.93, or between 0.98 and 1.0
    verdict = "FAIL"
    detail = f"n_s = {best_ns:.4f} outside [{gate_pass_lo}, {gate_pass_hi}]"

print(f"\n*** GATE VERDICT: {verdict}")
print(f"*** Detail: {detail}")

# ============================================================================
# 12. SAVE DATA
# ============================================================================

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        's54_modulus_fluct.npz')

np.savez(out_path,
    # Graph structure
    lap_eigenvalues=lap_eigs,
    lap_eigenvectors=lap_vecs,
    graph_distances=dist_matrix,

    # Method A: susceptibility
    chi_matrix=chi,
    P_susceptibility=P_A,
    ns_A=ns_A,
    ns_A_err=ns_A_err,

    # Method B: dynamical matrix (PRIMARY)
    dynamical_eigenvalues=dyn_eigs,
    dynamical_eigenvectors=dyn_vecs,
    P_dynamical=P_B,
    ns_B_full=ns_B,
    ns_B_full_err=ns_B_err,
    ns_B_IR=ns_IR,
    ns_B_IR_err=ns_IR_err,
    m_sq_onsite=m_sq,
    K_bond_mean=K_avg,
    mass_stiffness_ratio=ratio_mK,

    # Method C: thermal
    P_thermal=P_C,
    ns_C=ns_C,
    ns_C_err=ns_C_err,

    # Method D: dimension-weighted
    P_dim_weighted=P_D,
    ns_D=ns_D,
    ns_D_err=ns_D_err,

    # Method F: Casimir gradient
    P_casimir=P_F,
    ns_F=ns_F,
    ns_F_err=ns_F_err,

    # Correlation function
    C_d=C_d_avg,
    C_d_normalized=C_norm,
    pair_counts=count_d,

    # Tau sweep
    ns_vs_tau=ns_tau_B,
    ns_vs_tau_err=ns_tau_B_err,
    P_vs_tau=P_B_all,
    tau_values=tau_values,

    # Gate verdict
    gate_name=np.array(['MODULUS-FLUCT-54']),
    gate_verdict=np.array([verdict]),
    gate_detail=np.array([detail]),

    # Metadata
    tau_primary=tau_actual,
    tau_index=tau_idx,
    N_cells=N_cells,
    ns_primary=ns_B,
    ns_primary_err=ns_B_err,
)

print(f"\nData saved to: {out_path}")

# ============================================================================
# 13. PLOT
# ============================================================================

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 3, figsize=(18, 11))
fig.suptitle(f'MODULUS-FLUCT-54: Modulus Fluctuation Spectrum (tau={tau_actual:.3f})',
             fontsize=14, fontweight='bold')

# --- Panel 1: Power spectrum (all methods, log-log) ---
ax = axes[0, 0]
colors = {'A': 'blue', 'B': 'red', 'C': 'green', 'D': 'purple', 'F': 'orange'}
for label, P_data, ns_val, c in [
    ('A: suscept.', P_A, ns_A, 'blue'),
    ('B: dyn. matrix', P_B, ns_B, 'red'),
    ('C: thermal', P_C, ns_C, 'green'),
    ('D: dim-wt', P_D, ns_D, 'purple'),
    ('F: Casimir', P_F, ns_F, 'orange'),
]:
    mask = P_data[1:] > 1e-30
    if mask.any():
        ax.loglog(lap_eigs[1:][mask], P_data[1:][mask], 'o-', label=f'{label} (n_s={ns_val:.2f})',
                 color=c, markersize=3, alpha=0.7)

# Planck reference line
lam_ref = np.logspace(np.log10(lap_eigs[1]), np.log10(lap_eigs[-1]), 100)
P_ref = P_B[1] * (lam_ref / lap_eigs[1])**(-0.035/2)  # n_s=0.965 -> alpha=-0.0175
ax.loglog(lam_ref, P_ref, 'k--', alpha=0.5, label='Planck (n_s=0.965)')

ax.set_xlabel(r'$\lambda_k$ (graph Laplacian eigenvalue)')
ax.set_ylabel(r'$P(\lambda_k)$')
ax.set_title('Power Spectrum (all methods)')
ax.legend(fontsize=7, loc='upper right')
ax.grid(True, alpha=0.3)

# --- Panel 2: Method B with fit ---
ax = axes[0, 1]
ax.loglog(lap_eigs[1:], P_B[1:], 'ro-', markersize=5, label='Data')
# Show fit line
lam_plot = np.logspace(np.log10(lap_eigs[1]), np.log10(lap_eigs[-1]), 100)
P_fit_line = np.exp(intercept_B) * lam_plot**slope_B
ax.loglog(lam_plot, P_fit_line, 'r--', alpha=0.7,
          label=f'Fit: $\\alpha$={slope_B:.3f}, $n_s$={ns_B:.3f}')
# IR fit
if mask_IR.sum() >= 3:
    P_IR_line = np.exp(intercept_IR) * lam_plot**slope_IR
    ax.loglog(lam_plot, P_IR_line, 'b--', alpha=0.7,
              label=f'IR fit: $n_s$={ns_IR:.3f}')
ax.axhspan(0, 0, alpha=0)  # dummy for spacing
ax.set_xlabel(r'$\lambda_k$')
ax.set_ylabel(r'$P(\lambda_k)$')
ax.set_title(f'Method B: Dynamical Matrix (n_s={ns_B:.3f})')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# --- Panel 3: Correlation function C(d) ---
ax = axes[0, 2]
distances = np.arange(max_dist + 1)
ax.bar(distances, C_d_avg, color='steelblue', alpha=0.7, label='C(d)')
ax2 = ax.twinx()
ax2.plot(distances, C_norm, 'ro-', label='C(d)/C(0)')
ax.set_xlabel('Graph distance d')
ax.set_ylabel('C(d) (raw)')
ax2.set_ylabel('C(d)/C(0) (normalized)')
ax.set_title('Correlation Function')
ax.legend(loc='upper left', fontsize=8)
ax2.legend(loc='upper right', fontsize=8)
ax.grid(True, alpha=0.3)

# --- Panel 4: n_s vs tau ---
ax = axes[1, 0]
valid_tau = (ns_tau_B != 0) & (ns_tau_B_err > 0)
ax.errorbar(tau_values[valid_tau], ns_tau_B[valid_tau], yerr=ns_tau_B_err[valid_tau],
           fmt='bo-', markersize=3, capsize=2, label='n_s(tau) Method B')
ax.axhline(0.965, color='green', ls='--', alpha=0.7, label='Planck n_s=0.965')
ax.axhline(0.93, color='red', ls=':', alpha=0.5, label='Gate bounds')
ax.axhline(0.98, color='red', ls=':', alpha=0.5)
ax.axhline(1.0, color='black', ls='-', alpha=0.3, label='Scale invariant')
ax.axvline(tau_fold, color='purple', ls='--', alpha=0.5, label=f'tau_fold={tau_fold}')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$n_s$')
ax.set_title(r'$n_s$ vs $\tau$ (Method B, full fit)')
ax.legend(fontsize=7, loc='best')
ax.set_ylim(-0.5, 1.5)
ax.grid(True, alpha=0.3)

# --- Panel 5: Dynamical matrix eigenvalues ---
ax = axes[1, 1]
ax.plot(np.arange(N_cells), dyn_eigs, 'ko-', markersize=4)
ax.set_xlabel('Mode index')
ax.set_ylabel(r'$\omega_k^2$ (M_KK$^2$)')
ax.set_title('Dynamical Matrix Eigenvalues')
ax.grid(True, alpha=0.3)

# --- Panel 6: Summary table ---
ax = axes[1, 2]
ax.axis('off')
summary_text = (
    f"MODULUS-FLUCT-54 SUMMARY\n"
    f"{'='*40}\n\n"
    f"tau = {tau_actual:.4f} (near fold)\n"
    f"N_cells = {N_cells}\n"
    f"Graph diameter = {max_dist}\n"
    f"E_gap = {E_gap:.4f} M_KK\n\n"
    f"On-site mass: {np.mean(np.abs(m_sq)):.2f} M_KK^2\n"
    f"Bond stiffness: {K_avg:.4f} M_KK^2\n"
    f"m^2/(K*lam_max) = {ratio_mK:.3f}\n\n"
    f"SPECTRAL INDICES:\n"
    f"  Method A (suscept.): {ns_A:.3f} +/- {ns_A_err:.3f}\n"
    f"  Method B (full):     {ns_B:.3f} +/- {ns_B_err:.3f}\n"
    f"  Method B (IR):       {ns_IR:.3f} +/- {ns_IR_err:.3f}\n"
    f"  Planck:              0.965 +/- 0.004\n\n"
    f"GATE: {verdict}\n"
    f"{detail}"
)
ax.text(0.05, 0.95, summary_text, transform=ax.transAxes,
        verticalalignment='top', fontfamily='monospace', fontsize=9)

plt.tight_layout()
plot_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         's54_modulus_fluct.png')
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
print(f"Plot saved to: {plot_path}")

# ============================================================================
# 14. RAW SPECTRUM TABLE
# ============================================================================

print("\n" + "="*70)
print("RAW POWER SPECTRUM P(lambda_k)")
print("="*70)
print(f"{'k':>3s} {'lambda_k':>10s} {'P_A':>12s} {'P_B':>12s} {'P_C':>12s} {'P_F':>12s}")
print("-" * 65)
for k in range(1, N_cells):
    print(f"  {k:2d} {lap_eigs[k]:10.4f} {P_A[k]:12.4e} {P_B[k]:12.4e} {P_C[k]:12.4e} {P_F[k]:12.4e}")

print("\n=== COMPUTATION COMPLETE ===")
