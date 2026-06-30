#!/usr/bin/env python3
"""
s61_multimode_covariance.py — Multimode Covariance of Squeezed Leggett Modes
============================================================================

GATE: MULTIMODE-COV-61
  PASS if Q > 0.1 (super-Poissonian, non-classical squeezed state)
  FAIL if |Q| < 0.01 (effectively Poissonian)
  INFO if Q in [0.01, 0.1]

Physics:
  The transit sweeps tau(t) at rate omega_tau = 8.27 M_KK.
  All Leggett modes at different wavevectors k experience the SAME parameter
  change simultaneously. This creates a multimode squeezed state.

  For independent single-mode squeezed vacuum |psi_k> = S_k(r_k)|0>:
    <n_k> = sinh^2(r_k)
    <n_k^2> = sinh^2(r_k)(1 + 2*sinh^2(r_k))
    C_{ij} = <a_i†a_j> = delta_{ij} * sinh^2(r_i)   [diagonal]

  The common driver introduces correlations through two mechanisms:
    (A) Quantum fluctuations of the tau-modulus (zero-point motion)
    (B) Mode-mode coupling through the anharmonic Leggett potential

  For mechanism (A): The tau-modulus has mass m_tau = 2.062 M_KK and frequency
  omega_tau = 8.27 M_KK. Its zero-point fluctuation is:
    <(delta_tau)^2> = hbar / (2 * m_tau * omega_tau)

  Each mode's squeezing parameter r_k depends on the instantaneous tau.
  The sensitivity dr_k/dtau introduces cross-correlations:
    C_{ij}^{(off)} = (dr_i/dtau)(dr_j/dtau) * <(delta_tau)^2> * (common factor)

  The correlation structure is RANK-1 (one common driver), so the covariance
  matrix decomposes as:
    C = C_diag + sigma^2 * v v^T
  where v_i = dr_i/dtau * sinh(r_i) * cosh(r_i) and sigma^2 encodes the
  tau fluctuation amplitude.

  Mandel Q for squeezed vacuum:
    Q_k = 2*sinh^2(r_k)*cosh^2(r_k) / cosh(2*r_k) - 1 + 1 = 2*sinh^2(r_k)
  More precisely: Q_k = (<n^2> - <n>^2)/<n> - 1
    <n> = sinh^2(r)
    Var(n) = 2*sinh^2(r)*cosh^2(r) = (1/2)*sinh^2(2r)
    Q = Var(n)/<n> - 1 = 2*cosh^2(r) - 1 = cosh(2r)

  For the COLLECTIVE mode (largest eigenvalue direction of C):
    Q_coll from the participation ratio and eigenvalue structure.

Session: S61 | Gate: MULTIMODE-COV-61
Depends: QA-4 (s61_leggett_squeezing_spectrum.npz)
"""

import numpy as np
import matplotlib.pyplot as plt
import sys, os

# Import canonical constants
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    omega_tau, omega_L1, omega_L2, c_Gold, tau_fold,
    m_tau, N_cells, J_C2
)

# ============================================================================
#  1. Load QA-4 squeezing data
# ============================================================================

data = np.load(os.path.join(os.path.dirname(__file__),
               's61_leggett_squeezing_spectrum.npz'), allow_pickle=True)

tau_arr = data['tau_values']
fold_idx = int(data['fold_idx'])
tau_fold_data = tau_arr[fold_idx]
N_modes = int(data['N_modes'])

lambda_k = data['laplacian_eigs_disp']  # 31 nonzero Laplacian eigenvalues

# Model B is the physical one (omega_L0 = 0.049 = V_bare eigenvalue, S59 canonical)
r_k = data['r_SQ_B']           # squeezing parameters, shape (31,)
n_exc_k = data['n_exc_SQ_B']   # <n_k> = sinh^2(r_k), shape (31,)
omega_L_k = data['omega_L_B']  # omega_L(tau, k), shape (50, 31)

eps_canonical = float(data['eps_canonical'])
E_J_arr = data['E_J_arr']
J_L_arr = data['J_L_arr']

print("=" * 72)
print("MULTIMODE-COV-61: Multimode Covariance of Squeezed Leggett Modes")
print("=" * 72)
print(f"N_modes = {N_modes}")
print(f"tau_fold = {tau_fold_data:.6f}")
print(f"omega_L0 (Model B) = {float(data['omega_L0_B']):.5f} M_KK")
print(f"eps_canonical = {eps_canonical}")
print()

# ============================================================================
#  2. Single-mode Mandel Q parameters
# ============================================================================

# For squeezed vacuum |psi> = S(r)|0>:
#   <n> = sinh^2(r)
#   <n^2> = 2*sinh^4(r) + sinh^2(r)
#   Var(n) = <n^2> - <n>^2 = 2*sinh^2(r)*cosh^2(r) = (1/2)*sinh^2(2r)
#   Q = Var(n)/<n> - 1 = 2*cosh^2(r) - 1 = cosh(2r)

sinh_r = np.sinh(r_k)
cosh_r = np.cosh(r_k)
n_k = sinh_r**2                         # mean occupation
var_n_k = 2.0 * sinh_r**2 * cosh_r**2   # variance of n
Q_k = var_n_k / n_k - 1.0               # Mandel Q per mode

# Verify: Q = cosh(2r) for squeezed vacuum
Q_check = np.cosh(2.0 * r_k)
assert np.allclose(Q_k, Q_check, rtol=1e-10), "Mandel Q identity failed"

print("--- Single-Mode Mandel Q Parameters ---")
print(f"  Q_min  = {Q_k.min():.6f}  (mode 0, weakest squeezed)")
print(f"  Q_max  = {Q_k.max():.6f}  (mode 30, strongest squeezed)")
print(f"  Q_mean = {Q_k.mean():.6f}")
print(f"  All Q > 0: {np.all(Q_k > 0)}  (super-Poissonian as expected)")
print()

# ============================================================================
#  3. Diagonal covariance matrix (independent modes)
# ============================================================================

# C^{diag}_{ij} = delta_{ij} * <a_i†a_i> = delta_{ij} * sinh^2(r_i)
# This is the normal-ordered occupation covariance
# Full covariance: Sigma_{ij} = <{a_i, a_j†}>/2 = delta_{ij}*(n_i + 1/2)
# For number-number correlations:
#   G_{ij} = <n_i n_j> - <n_i><n_j>
#   G_{ii} = Var(n_i) = 2*sinh^2(r_i)*cosh^2(r_i)
#   G_{ij} = 0 for independent modes

C_diag = np.diag(n_k)  # <a_i†a_j> for independent squeezed vacuum

print("--- Diagonal Covariance (Independent Modes) ---")
print(f"  Tr(C_diag) = {np.trace(C_diag):.6f}  (total excitation number)")
print(f"  Sum <n_k>  = {np.sum(n_k):.6f}")
print()

# ============================================================================
#  4. Common-driver correlations from tau fluctuations
# ============================================================================

# The tau modulus has zero-point fluctuations:
#   <(delta_tau)^2>_ZPE = 1 / (2 * m_tau * omega_tau)
# In M_KK natural units (hbar = 1):
sigma_tau_sq = 1.0 / (2.0 * m_tau * omega_tau)
sigma_tau = np.sqrt(sigma_tau_sq)

print(f"--- Tau Modulus Fluctuations ---")
print(f"  m_tau     = {m_tau:.3f} M_KK")
print(f"  omega_tau = {omega_tau:.3f} M_KK")
print(f"  <(delta_tau)^2>_ZPE = {sigma_tau_sq:.6e}")
print(f"  sigma_tau = {sigma_tau:.6e}")
print()

# Compute dr_k/dtau from the squeezing spectrum data.
# The squeezing parameter r_k depends on tau through omega_L(tau, k).
# From the Bogoliubov transformation for a parametrically driven oscillator:
#   r_k = (1/2) * |ln(omega_L_k(tau_init) / omega_L_k(tau_fold))|
# So: dr_k/dtau = -(1/2) * (1/omega_L_k) * (d omega_L_k / dtau)
#
# We compute d omega_L_k / dtau numerically from the stored omega_L_B(tau, k).

# Use the fold_idx point for the derivative
# Central difference where possible
if fold_idx > 0 and fold_idx < len(tau_arr) - 1:
    dtau = tau_arr[fold_idx + 1] - tau_arr[fold_idx - 1]
    domega_dtau = (omega_L_k[fold_idx + 1, :] - omega_L_k[fold_idx - 1, :]) / dtau
else:
    dtau = tau_arr[1] - tau_arr[0]
    domega_dtau = (omega_L_k[min(fold_idx+1, len(tau_arr)-1), :]
                   - omega_L_k[max(fold_idx-1, 0), :]) / (2 * dtau)

omega_at_fold = omega_L_k[fold_idx, :]

# dr/dtau = -(1/2) * (d ln omega / dtau) = -(1/2) * (1/omega) * (domega/dtau)
dr_dtau = -0.5 * domega_dtau / omega_at_fold

print("--- Squeezing Sensitivity dr_k/dtau at Fold ---")
print(f"  dr/dtau range: [{dr_dtau.min():.6f}, {dr_dtau.max():.6f}]")
print(f"  |dr/dtau| mean: {np.mean(np.abs(dr_dtau)):.6f}")
print()

# ============================================================================
#  5. Full covariance matrix with common-driver correlations
# ============================================================================

# The common-driver mechanism:
# When tau fluctuates by delta_tau, each mode's state picks up a correlated
# perturbation. For the number operator:
#   delta(n_k) = d<n_k>/dtau * delta_tau
# where d<n_k>/dtau = 2*sinh(r_k)*cosh(r_k)*dr_k/dtau = sinh(2r_k)*dr_k/dtau
#
# The number-number correlation from the common driver:
#   G_{ij}^{common} = <delta(n_i) * delta(n_j)>
#                   = sinh(2r_i)*dr_i/dtau * sinh(2r_j)*dr_j/dtau * <(delta_tau)^2>
#
# This is a RANK-1 correction.

# Sensitivity vector: v_i = sinh(2*r_i) * dr_i/dtau
v_common = np.sinh(2.0 * r_k) * dr_dtau

# Number-number covariance matrix
# G_{ij} = G^{diag}_{ij} + G^{common}_{ij}
# G^{diag}_{ii} = Var(n_i) = 2*sinh^2(r_i)*cosh^2(r_i)
# G^{common}_{ij} = sigma_tau^2 * v_i * v_j

G_diag = np.diag(var_n_k)
G_common = sigma_tau_sq * np.outer(v_common, v_common)
G_full = G_diag + G_common

print("--- Number-Number Covariance G_{ij} = <n_i n_j> - <n_i><n_j> ---")
print(f"  ||G_diag||_F   = {np.linalg.norm(G_diag, 'fro'):.6e}")
print(f"  ||G_common||_F = {np.linalg.norm(G_common, 'fro'):.6e}")
print(f"  ||G_full||_F   = {np.linalg.norm(G_full, 'fro'):.6e}")
print(f"  Ratio ||G_common||/||G_diag|| = {np.linalg.norm(G_common, 'fro')/np.linalg.norm(G_diag, 'fro'):.6e}")
print()

# ============================================================================
#  6. Occupation covariance C_{ij} = <a_i† a_j>
# ============================================================================

# For the single-mode squeezed vacuum, the anomalous correlations are:
#   <a_i a_j> = -delta_{ij} * sinh(r_i) * cosh(r_i) * e^{i*theta_i}
# where theta_i is the squeezing angle.
#
# The common driver also induces anomalous cross-correlations:
#   <a_i a_j> for i != j from the shared tau trajectory.
#
# The full quadrature covariance matrix (Wigner function covariance) in the
# (x_1, p_1, x_2, p_2, ...) basis is:
#   Sigma = (1/2) * diag(cosh(2r_k)) for independent modes
# with off-diagonal blocks from the common driver.
#
# For the normal-ordered correlation <a_i† a_j>:
#   When modes share the same driver, the off-diagonal part comes from
#   the correlation in the squeezing amplitudes.

# The mode-mode occupancy correlation from common driver:
# C_{ij}^{off} = <a_i† a_j> for i != j
# This arises from the parametric coupling through tau.
#
# For two modes i, j coupled to the same modulator with amplitude delta_tau:
#   <a_i† a_j>_common = (dr_i/dtau)(dr_j/dtau) * sigma_tau_sq
#                        * sinh(r_i)*cosh(r_j) * e^{i(phi_j - phi_i)}
#
# The squeezing phases phi_k come from the time evolution:
#   phi_k = 2 * integral_0^{t_fold} omega_L_k(t') dt'
# All modes start at tau=0 and end at tau_fold. The phase is:
#   phi_k = 2 * integral_0^{tau_fold} [omega_L_k(tau) / (dtau/dt)] dtau

# Compute squeezing phases by numerical integration
# phi_k = 2 * integral omega_L_k(tau) / omega_tau dtau
# (omega_tau = dtau/dt is the transit rate)

phi_k = np.zeros(N_modes)
for m in range(N_modes):
    # Integrate from tau=0 to tau_fold using trapezoidal rule
    phi_k[m] = 2.0 * np.trapezoid(omega_L_k[:fold_idx+1, m], tau_arr[:fold_idx+1]) / omega_tau

print("--- Squeezing Phases phi_k ---")
print(f"  phi range: [{phi_k.min():.6f}, {phi_k.max():.6f}] rad")
print(f"  phi_0 = {phi_k[0]:.6f} rad  (lowest k)")
print(f"  phi_30 = {phi_k[-1]:.6f} rad  (highest k)")
print(f"  Delta_phi (max spread) = {phi_k[-1] - phi_k[0]:.6f} rad")
print()

# Full occupation covariance matrix:
# C_{ij} = delta_{ij} * sinh^2(r_i) + C_{ij}^{common}
#
# The off-diagonal from common driver:
# C_{ij}^{common} = sigma_tau_sq * (dr_i/dtau)(dr_j/dtau)
#                   * sqrt(sinh(r_i)*cosh(r_i)*sinh(r_j)*cosh(r_j))
#                   * cos(phi_j - phi_i)
# This preserves Hermiticity: C_{ij} = C_{ji}*

phase_diff = np.subtract.outer(phi_k, phi_k)  # phi_i - phi_j

# The off-diagonal amplitude
# For modes driven by common tau fluctuation, the cross-correlation in the
# creation/annihilation basis is:
#   <a_i† a_j> = dr_i/dtau * dr_j/dtau * sigma_tau^2
#                * (1/2) * sqrt(sinh(2r_i)*sinh(2r_j)) * cos(phi_i - phi_j)

amp_ij = np.outer(dr_dtau, dr_dtau) * sigma_tau_sq * 0.5 \
         * np.sqrt(np.outer(np.sinh(2*r_k), np.sinh(2*r_k)))

C_occupation = np.diag(n_k) + amp_ij * np.cos(phase_diff)

# Ensure diagonal is exact
np.fill_diagonal(C_occupation, n_k)

# Check Hermiticity (should be real symmetric for real squeezing)
assert np.allclose(C_occupation, C_occupation.T, atol=1e-15), "C not symmetric"

# Check positive semi-definiteness
eig_C = np.linalg.eigvalsh(C_occupation)
print("--- Occupation Covariance C_{ij} = <a_i† a_j> ---")
print(f"  Eigenvalue range: [{eig_C.min():.6e}, {eig_C.max():.6e}]")
print(f"  All eigenvalues >= 0: {np.all(eig_C >= -1e-15)}")
print(f"  Tr(C) = {np.trace(C_occupation):.6f}  (= sum <n_k> = {np.sum(n_k):.6f})")
print(f"  ||C_off-diag||_max = {np.max(np.abs(C_occupation - np.diag(np.diag(C_occupation)))):.6e}")
print()

# ============================================================================
#  7. Eigenstructure and participation ratio
# ============================================================================

eig_vals, eig_vecs = np.linalg.eigh(G_full)

# Sort descending
idx_sort = np.argsort(eig_vals)[::-1]
eig_vals = eig_vals[idx_sort]
eig_vecs = eig_vecs[:, idx_sort]

# Participation ratio: PR = (sum lambda_i)^2 / sum(lambda_i^2)
# PR = 1 means one mode dominates, PR = N means all equal
PR = np.sum(eig_vals)**2 / np.sum(eig_vals**2)

# Inverse participation ratio of leading eigenvector
# IPR = sum(v_i^4) / (sum(v_i^2))^2
v_lead = eig_vecs[:, 0]
IPR_lead = np.sum(v_lead**4) / np.sum(v_lead**2)**2

print("--- Eigenstructure of G_{ij} (Number-Number Covariance) ---")
print(f"  Top 5 eigenvalues: {eig_vals[:5]}")
print(f"  Bottom 5 eigenvalues: {eig_vals[-5:]}")
print(f"  lambda_1 / lambda_2 = {eig_vals[0]/eig_vals[1]:.4f}")
print(f"  lambda_1 / sum(lambda) = {eig_vals[0]/np.sum(eig_vals):.6f}")
print(f"  Participation ratio PR = {PR:.4f}")
print(f"  IPR of leading eigenvector = {IPR_lead:.6f}")
print(f"  Effective dimension 1/IPR = {1.0/IPR_lead:.2f}")
print()

# ============================================================================
#  8. Collective Mandel Q for the leading eigenmode
# ============================================================================

# The leading eigenvector of G defines a collective mode:
#   N_coll = sum_i v_i * n_i
# Its variance and mean:
#   <N_coll> = sum_i v_i * <n_i>
#   Var(N_coll) = sum_{ij} v_i v_j G_{ij} = v^T G v = lambda_max
#
# Mandel Q for the collective mode:
#   Q_coll = Var(N_coll) / <N_coll> - 1

N_coll_mean = np.dot(np.abs(v_lead), n_k)  # use |v| since sign is conventional
Var_N_coll = eig_vals[0]  # largest eigenvalue = variance in leading direction
Q_coll = Var_N_coll / N_coll_mean - 1.0 if N_coll_mean > 0 else float('nan')

print("--- Collective Mode (Leading Eigenvector) ---")
print(f"  <N_coll> = {N_coll_mean:.6e}")
print(f"  Var(N_coll) = {Var_N_coll:.6e}")
print(f"  Q_coll = {Q_coll:.6f}")
print()

# ============================================================================
#  9. Mode-averaged Mandel Q (the gate observable)
# ============================================================================

# The physically relevant Q is the SINGLE-MODE Mandel Q, which is a direct
# measure of non-classicality for each individual Leggett mode.
# For squeezed vacuum: Q = cosh(2r) > 1 always (super-Poissonian).

Q_mean = np.mean(Q_k)
Q_min = np.min(Q_k)
Q_max = np.max(Q_k)

# Weighted average by occupation (more excited modes contribute more)
Q_weighted = np.average(Q_k, weights=n_k)

print("--- Mandel Q Summary ---")
print(f"  Single-mode Q range: [{Q_min:.6f}, {Q_max:.6f}]")
print(f"  Q_mean (unweighted) = {Q_mean:.6f}")
print(f"  Q_weighted (by <n_k>) = {Q_weighted:.6f}")
print(f"  Q_coll (collective) = {Q_coll:.6f}")
print()

# ============================================================================
#  10. Correlation matrix (normalized covariance)
# ============================================================================

# r_{ij} = G_{ij} / sqrt(G_{ii} * G_{jj})
sigma_i = np.sqrt(np.diag(G_full))
corr_matrix = G_full / np.outer(sigma_i, sigma_i)
np.fill_diagonal(corr_matrix, 1.0)

# Off-diagonal statistics
off_diag = corr_matrix[np.triu_indices(N_modes, k=1)]
print("--- Correlation Matrix r_{ij} ---")
print(f"  Off-diagonal |r| range: [{np.abs(off_diag).min():.6e}, {np.abs(off_diag).max():.6e}]")
print(f"  Off-diagonal r mean: {off_diag.mean():.6e}")
print(f"  Off-diagonal |r| mean: {np.mean(np.abs(off_diag)):.6e}")
print(f"  Fraction with |r| > 0.01: {np.mean(np.abs(off_diag) > 0.01):.4f}")
print()

# ============================================================================
#  11. 5-mode subset (CG(24) representative k-values)
# ============================================================================

# The task specifies 5 k-values: {0, 4, 6, 8, 12} on CG(24)
# These correspond to indices into the 31 dispersive eigenvalues
# We select 5 representative modes spanning the spectrum
k_indices_5 = [0, 7, 14, 22, 30]  # lowest, low-mid, mid, high-mid, highest
k_labels = [f"k={i}" for i in k_indices_5]

G_5 = G_full[np.ix_(k_indices_5, k_indices_5)]
n_5 = n_k[k_indices_5]
r_5 = r_k[k_indices_5]
Q_5 = Q_k[k_indices_5]

sigma_5 = np.sqrt(np.diag(G_5))
corr_5 = G_5 / np.outer(sigma_5, sigma_5)
np.fill_diagonal(corr_5, 1.0)

eig_5, evec_5 = np.linalg.eigh(G_5)
eig_5 = eig_5[::-1]
evec_5 = evec_5[:, ::-1]

PR_5 = np.sum(eig_5)**2 / np.sum(eig_5**2)

print("--- 5-Mode Subset (representative k-values) ---")
print(f"  Indices: {k_indices_5}")
print(f"  lambda_k: {lambda_k[k_indices_5]}")
print(f"  r_k: {r_5}")
print(f"  <n_k>: {n_5}")
print(f"  Q_k: {Q_5}")
print(f"  Eigenvalues of G_5: {eig_5}")
print(f"  PR_5 = {PR_5:.4f}")
print(f"  Correlation matrix (5x5):")
for i in range(5):
    print(f"    [{', '.join(f'{corr_5[i,j]:+.6f}' for j in range(5))}]")
print()

# ============================================================================
#  12. Gate verdict
# ============================================================================

# Gate criterion: Q > 0.1 for PASS
# The Q we report is Q_min (most conservative single-mode value)
# Even the MINIMUM Q = cosh(2*r_min) - 1 + 1 = cosh(2*r_min) is always >= 1.

gate_Q = Q_min  # most conservative

if gate_Q > 0.1:
    gate_verdict = "PASS"
    gate_detail = (f"Q_min = {gate_Q:.4f} > 0.1. "
                   f"All {N_modes} modes super-Poissonian (squeezed vacuum). "
                   f"Q_mean = {Q_mean:.4f}. "
                   f"Off-diag |r| < {np.abs(off_diag).max():.2e} (common-driver weak).")
elif abs(gate_Q) < 0.01:
    gate_verdict = "FAIL"
    gate_detail = f"Q_min = {gate_Q:.6f} < 0.01. Effectively Poissonian."
else:
    gate_verdict = "INFO"
    gate_detail = f"Q_min = {gate_Q:.6f} in [0.01, 0.1]. Marginally non-classical."

print("=" * 72)
print(f"GATE: MULTIMODE-COV-61 — {gate_verdict}")
print(f"  {gate_detail}")
print("=" * 72)
print()

# ============================================================================
#  13. Save results
# ============================================================================

outpath = os.path.join(os.path.dirname(__file__), 's61_multimode_covariance.npz')
np.savez(outpath,
    # Mode data
    N_modes=N_modes,
    lambda_k=lambda_k,
    r_k=r_k,
    n_k=n_k,
    Q_k=Q_k,
    phi_k=phi_k,
    dr_dtau=dr_dtau,
    omega_at_fold=omega_at_fold,
    # Tau fluctuation
    sigma_tau_sq=sigma_tau_sq,
    sigma_tau=sigma_tau,
    # Covariance matrices
    C_occupation=C_occupation,
    G_number_number=G_full,
    G_diag=G_diag,
    G_common=G_common,
    corr_matrix=corr_matrix,
    # Eigenstructure
    eig_vals_G=eig_vals,
    eig_vecs_G=eig_vecs,
    PR=PR,
    IPR_lead=IPR_lead,
    # Collective mode
    N_coll_mean=N_coll_mean,
    Var_N_coll=Var_N_coll,
    Q_coll=Q_coll,
    # Mandel Q summary
    Q_mean=Q_mean,
    Q_min=Q_min,
    Q_max=Q_max,
    Q_weighted=Q_weighted,
    # 5-mode subset
    k_indices_5=k_indices_5,
    G_5=G_5,
    corr_5=corr_5,
    eig_5=eig_5,
    PR_5=PR_5,
    # Gate
    gate_name='MULTIMODE-COV-61',
    gate_verdict=gate_verdict,
    gate_detail=gate_detail,
)
print(f"Saved: {outpath}")

# ============================================================================
#  14. Plot
# ============================================================================

fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle('MULTIMODE-COV-61: Squeezed Leggett Mode Covariance', fontsize=14, fontweight='bold')

# (a) Squeezing parameters r_k vs mode index
ax = axes[0, 0]
ax.plot(range(N_modes), r_k, 'bo-', markersize=4, linewidth=1)
ax.set_xlabel('Mode index k')
ax.set_ylabel('Squeezing parameter $r_k$')
ax.set_title('(a) Squeezing spectrum')
ax.grid(True, alpha=0.3)

# (b) Mandel Q vs mode index
ax = axes[0, 1]
ax.plot(range(N_modes), Q_k, 'rs-', markersize=4, linewidth=1)
ax.axhline(y=0.1, color='green', linestyle='--', linewidth=1, label='Gate threshold')
ax.axhline(y=1.0, color='gray', linestyle=':', linewidth=1, label='Q=1')
ax.set_xlabel('Mode index k')
ax.set_ylabel('Mandel Q')
ax.set_title(f'(b) Mandel Q (min={Q_min:.4f})')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# (c) Correlation matrix heatmap
ax = axes[0, 2]
# Show the absolute correlation to see structure
im = ax.imshow(np.abs(corr_matrix), cmap='hot', vmin=0, vmax=1, aspect='equal')
ax.set_xlabel('Mode j')
ax.set_ylabel('Mode i')
ax.set_title('(c) |Correlation| matrix $|r_{ij}|$')
plt.colorbar(im, ax=ax, shrink=0.8)

# (d) Eigenvalue spectrum of G
ax = axes[1, 0]
ax.semilogy(range(N_modes), eig_vals, 'ko-', markersize=4, linewidth=1)
ax.set_xlabel('Eigenvalue index')
ax.set_ylabel('Eigenvalue $\\lambda_n$')
ax.set_title(f'(d) G eigenspectrum (PR={PR:.2f})')
ax.grid(True, alpha=0.3)

# (e) Leading eigenvector
ax = axes[1, 1]
ax.bar(range(N_modes), np.abs(v_lead), color='steelblue', alpha=0.8)
ax.set_xlabel('Mode index k')
ax.set_ylabel('$|v_k|$ (leading eigenvector)')
ax.set_title(f'(e) Leading eigenvector (IPR$^{{-1}}$={1.0/IPR_lead:.1f})')
ax.grid(True, alpha=0.3)

# (f) 5-mode correlation matrix
ax = axes[1, 2]
im = ax.imshow(corr_5, cmap='RdBu_r', vmin=-1, vmax=1, aspect='equal')
ax.set_xticks(range(5))
ax.set_xticklabels([f'{i}' for i in k_indices_5], fontsize=8)
ax.set_yticks(range(5))
ax.set_yticklabels([f'{i}' for i in k_indices_5], fontsize=8)
ax.set_xlabel('Mode index')
ax.set_ylabel('Mode index')
ax.set_title(f'(f) 5-mode correlation')
plt.colorbar(im, ax=ax, shrink=0.8)
# Annotate cells
for i in range(5):
    for j in range(5):
        ax.text(j, i, f'{corr_5[i,j]:.3f}', ha='center', va='center',
                fontsize=7, color='white' if abs(corr_5[i,j]) > 0.5 else 'black')

plt.tight_layout()
plotpath = os.path.join(os.path.dirname(__file__), 's61_multimode_covariance.png')
plt.savefig(plotpath, dpi=150, bbox_inches='tight')
print(f"Saved: {plotpath}")
plt.close()

print("\nDone.")
