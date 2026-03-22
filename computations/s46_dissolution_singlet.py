#!/usr/bin/env python3
"""
s46_dissolution_singlet.py -- DISSOLUTION-SINGLET-46
=====================================================

Compute entanglement entropy S(eps_c) restricted to singlet-singlet
partition only (16 modes, bipartition A=4, B=4).

=== PHYSICS ===

S45 DISSOLUTION-ENTROPY-45 found S/S_page ~ 0.47 for the FULL block-diagonal
spectrum at the dissolution crossover eps_c. The question: is this suppression
geometric (caused by block-diagonality across multiple sectors of different
sizes) or dynamical (intrinsic to the BCS/Dirac structure within each block)?

The singlet (0,0) sector is the simplest test case. It has:
  - Representation dimension d_rep = 1 (trivial representation of SU(3))
  - Dirac block size = 1 * 16 = 16 (16 spinor components)
  - Tensor product bipartition: 16 = 4 * 4, so d_A = 4, d_B = 4
  - S_page(4,4) = ln(4) - 4/(2*4) = 0.886 nats
  - S_max = ln(4) = 1.386 nats

At epsilon = 0: the ground state of the 16x16 singlet block is an eigenstate,
hence a product state in the 4x4 tensor decomposition only if the Dirac
structure has no off-diagonal coupling between the two halves. In general,
S(0) will be nonzero because the Dirac operator already couples the spinor
components within the block.

At epsilon = eps_c(full): the full-spectrum dissolution crossover. But for the
singlet block ALONE, the relevant eps_c may differ. We measure S at the SAME
eps_c as the full spectrum for direct comparison.

INTERPRETATION:
  - S_singlet/S_page > 0.95 => suppression is GEOMETRIC. The singlet block
    alone reaches near-full entanglement at eps_c, meaning the 0.47 in the
    full spectrum is caused by the block-diagonal structure (geometric
    frustration from mixing blocks of different sizes).

  - S_singlet/S_page ~ 0.47 => suppression is DYNAMICAL. Even within a single
    block, the BCS/Dirac structure resists full entanglement at eps_c. This
    would mean the information content of the Dirac spectrum itself limits
    dissolution.

=== METHOD ===

For each truncation level (pq 1-5), the singlet block is IDENTICAL (always
the same 16x16 matrix -- it does not depend on the truncation level since
(0,0) is the trivial representation at any pq_max). So we only need to build
it once.

We then:
  1. Build the 16x16 singlet block H_singlet = i * D_K(0,0)
  2. For each pq level's eps_c:
     a. Scale perturbation: sigma = eps_c * ||H_singlet||_F / 16
     b. Generate M random GUE perturbations
     c. Compute ground state of H_singlet + V
     d. Reshape psi (length 16) into 4x4 matrix
     e. Compute S_ent from SVD (Schmidt decomposition)
  3. Compare S_singlet(eps_c)/S_page(4,4) against full-spectrum 0.47

Additionally, we perform an independent eps scan for the singlet block to
find its OWN crossover eps_c_singlet (where <r> crosses the midpoint) and
measure S there.

=== DIMENSIONAL ANALYSIS ===
  - H_singlet: [energy] = M_KK
  - epsilon: dimensionless (perturbation amplitude / Frobenius norm)
  - S_ent: dimensionless (nats)
  - d_A, d_B: dimensionless (Hilbert space dimensions)

=== LIMITING CASES ===
  - eps = 0: S = S(eigenstate of H_singlet). May be nonzero due to Dirac coupling.
  - eps >> 1: S -> S_page(4,4) = 0.886 nats (random matrix regime).
  - d_A = d_B = 1: S = 0 always (trivial bipartition).

=== CITATION ===
  - S45 dissolution entropy: s45_dissolution_entropy.{py,npz}
  - S44 dissolution scaling: s44_dissolution_scaling.{py,npz}
  - Page entropy: Page (1993), PRL 71, 1291

=== GATE ===
DISSOLUTION-STRUCTURE-46. PASS: S_singlet/S_page > 0.95. INFO: ~ 0.47.

Author: hawking-theorist, Session 46
"""

import numpy as np
from numpy.linalg import eigvalsh, eigh
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from scipy.optimize import curve_fit
import os
import sys
import time

t_start = time.time()

# Add tier0 path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

# Import infrastructure
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
# CONSTANTS
# ============================================================
R_POISSON = 2 * np.log(2) - 1   # 0.38629
R_GOE = 0.5307                    # Atas et al. 2013
R_MIDPOINT = (R_POISSON + R_GOE) / 2.0  # ~0.459
DEGENERACY_TOL = 1e-10

# Singlet bipartition: 16 = 4 * 4
D_SINGLET = 16  # total dim of singlet block
D_A = 4          # subsystem A dimension
D_B = 4          # subsystem B dimension

# Page entropy for d_A=4, d_B=4
# S_page = ln(d_A) - d_A/(2*d_B) = ln(4) - 4/8 = 1.386 - 0.5 = 0.886
S_PAGE_SINGLET = np.log(D_A) - D_A / (2.0 * D_B)
S_MAX_SINGLET = np.log(min(D_A, D_B))

np.random.seed(42)

# Configuration
N_SAMPLES = 100     # Singlet is 16x16, eigh is instant. Use many samples.
N_EPS_SCAN = 30     # Fine epsilon scan
N_BINARY_STEPS = 14 # Binary search steps for singlet-own eps_c


# ============================================================
# LOAD S45 DATA
# ============================================================
print("=" * 70)
print("DISSOLUTION-SINGLET-46: Singlet-Only Entanglement Entropy")
print("=" * 70)

s45_path = os.path.join(SCRIPT_DIR, "s45_dissolution_entropy.npz")
s45 = np.load(s45_path, allow_pickle=True)

eps_c_full = s45['eps_c_values']          # [pq1, pq2, pq3, pq4, pq5]
N_full = s45['N_values']                   # [112, 432, 1232, 2912, 6048]
S_full = s45['S_at_eps_c']                 # S_ent at eps_c for full spectrum
S_page_full = s45['S_page']                # S_page for full spectrum
S_norm_full = s45['S_normalized']           # S/S_page for full spectrum
max_pq_sums = s45['max_pq_sums']

print(f"\nLoaded S45 dissolution data:")
print(f"  S_page(singlet) = {S_PAGE_SINGLET:.4f}")
print(f"  S_max(singlet)  = {S_MAX_SINGLET:.4f}")
print(f"  S/S_page(full)  = {S_norm_full}  (mean = {np.mean(S_norm_full):.4f})")
print(f"  Bipartition: d_A = {D_A}, d_B = {D_B}, N = {D_SINGLET}")
print(f"\n  Full-spectrum eps_c values:")
for i in range(len(max_pq_sums)):
    print(f"    pq={max_pq_sums[i]}: N={int(N_full[i])}, eps_c={eps_c_full[i]:.5f}, "
          f"S/S_page={S_norm_full[i]:.4f}")


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def ratio_statistic(evals):
    """Oganesyan-Huse ratio statistic <r> from eigenvalues."""
    evals = np.sort(np.real(evals))
    unique = [evals[0]]
    for e in evals[1:]:
        if abs(e - unique[-1]) > DEGENERACY_TOL:
            unique.append(e)
    evals = np.array(unique)
    if len(evals) < 4:
        return np.nan
    spacings = np.diff(evals)
    spacings = spacings[spacings > DEGENERACY_TOL]
    if len(spacings) < 3:
        return np.nan
    ratios = []
    for i in range(len(spacings) - 1):
        s1, s2 = spacings[i], spacings[i + 1]
        if max(s1, s2) > 0:
            ratios.append(min(s1, s2) / max(s1, s2))
    return np.mean(ratios) if ratios else np.nan


def page_entropy(d_A, d_B):
    """Page entropy: S_page = ln(d_A) - d_A/(2*d_B) for d_A <= d_B."""
    if d_A > d_B:
        d_A, d_B = d_B, d_A
    if d_A <= 0:
        return 0.0
    return np.log(d_A) - d_A / (2.0 * d_B)


def entanglement_entropy_4x4(psi):
    """
    Compute entanglement entropy of |psi> in C^16 via 4x4 tensor bipartition.

    Reshape psi (length 16) into a 4x4 matrix M.
    SVD: M = U * diag(sigma) * V^dag.
    Schmidt probabilities: p_i = sigma_i^2 / sum(sigma_j^2).
    S_ent = -sum(p_i * ln(p_i)).

    Returns S_ent in nats.
    """
    assert len(psi) == 16, f"Expected 16 components, got {len(psi)}"
    M = psi.reshape(D_A, D_B)
    sigma = np.linalg.svd(M, compute_uv=False)
    p = sigma**2
    p = np.real(p)
    p_sum = np.sum(p)
    if p_sum > 0:
        p = p / p_sum
    p = p[p > 1e-30]
    return -np.sum(p * np.log(p))


def measure_singlet_entropy(H_singlet, H_norm, epsilon, n_samples, compute_r=True):
    """
    Measure entanglement entropy at given epsilon for the 16x16 singlet block.

    Perturbation: V drawn from GUE scaled so ||V||_F ~ epsilon * ||H||_F.

    Returns: (S_mean, S_err, r_mean, r_err, S_all)
    """
    sigma = epsilon * H_norm / D_SINGLET
    S_values = []
    r_values = []

    for _ in range(n_samples):
        V_real = np.random.randn(D_SINGLET, D_SINGLET) * sigma
        V_imag = np.random.randn(D_SINGLET, D_SINGLET) * sigma
        V = (V_real + 1j * V_imag)
        V = (V + V.conj().T) / 2.0

        H_pert = H_singlet + V
        evals, evecs = eigh(H_pert)
        psi = evecs[:, 0]  # ground state

        S = entanglement_entropy_4x4(psi)
        S_values.append(S)

        if compute_r:
            r_val = ratio_statistic(evals)
            if not np.isnan(r_val):
                r_values.append(r_val)

    S_arr = np.array(S_values)
    S_mean = np.mean(S_arr)
    S_err = np.std(S_arr) / np.sqrt(len(S_arr)) if len(S_arr) > 1 else 0.0

    r_arr = np.array(r_values) if r_values else np.array([np.nan])
    r_mean = np.nanmean(r_arr)
    r_err = np.nanstd(r_arr) / np.sqrt(np.sum(~np.isnan(r_arr))) if np.sum(~np.isnan(r_arr)) > 1 else 0.0

    return S_mean, S_err, r_mean, r_err, S_arr


# ============================================================
# Step 1: Build SU(3) infrastructure and extract singlet block
# ============================================================
print("\n--- Step 1: Build SU(3) infrastructure ---")

gens = su3_generators()
f_abc = compute_structure_constants(gens)
gammas = build_cliff8()
cliff_err = validate_clifford(gammas)
print(f"  Clifford algebra error: {cliff_err:.2e}")

B_ab = compute_killing_form(f_abc)
g_s = jensen_metric(B_ab, TAU_FOLD)
E_frame = orthonormal_frame(g_s)
ft = frame_structure_constants(f_abc, E_frame)
Gamma = connection_coefficients(ft)
mc_err = validate_connection(Gamma)
Omega = spinor_connection_offset(Gamma, gammas)
_, is_ah, h_err, ah_err = validate_omega_hermitian(Omega)

print(f"  Connection metric-compatibility error: {mc_err:.2e}")
print(f"  Omega anti-Hermitian error: {ah_err:.2e}")

# Build singlet (0,0) Dirac block
print("\n--- Step 2: Build singlet (0,0) block ---")

rho_00, dim_00 = get_irrep(0, 0, gens, f_abc)
assert dim_00 == 1, f"Singlet dimension should be 1, got {dim_00}"

D_singlet = dirac_operator_on_irrep(rho_00, E_frame, gammas, Omega)
H_singlet = 1j * D_singlet  # Hermitian

# Verify Hermiticity
herm_err = np.max(np.abs(H_singlet - H_singlet.conj().T))
print(f"  H_singlet shape: {H_singlet.shape}")
print(f"  Hermiticity error: {herm_err:.2e}")
assert herm_err < 1e-12, f"H_singlet not Hermitian: {herm_err}"

H_norm = np.linalg.norm(H_singlet, 'fro')
print(f"  ||H_singlet||_F = {H_norm:.6f}")

# Eigenvalues of unperturbed singlet block
evals_0 = eigvalsh(H_singlet)
print(f"  Eigenvalues: {evals_0}")

# Unperturbed ground state entropy
evals_0_full, evecs_0 = eigh(H_singlet)
psi_0 = evecs_0[:, 0]
S_0 = entanglement_entropy_4x4(psi_0)
r_0 = ratio_statistic(evals_0)
print(f"  Unperturbed S_ent = {S_0:.6f}")
print(f"  Unperturbed <r> = {r_0:.4f}")

# Verify: the singlet block is the SAME for all truncation levels
# (since it depends only on the (0,0) representation, which is trivial)
print(f"\n  STRUCTURAL CHECK: Singlet block is INDEPENDENT of truncation level.")
print(f"  It is always the same 16x16 matrix at tau = {TAU_FOLD}.")


# ============================================================
# Step 3: Measure S at each full-spectrum eps_c
# ============================================================
print("\n--- Step 3: Measure S_singlet at full-spectrum eps_c values ---")

S_at_full_epsc = np.zeros(len(eps_c_full))
S_err_at_full_epsc = np.zeros(len(eps_c_full))
r_at_full_epsc = np.zeros(len(eps_c_full))
r_err_at_full_epsc = np.zeros(len(eps_c_full))
S_norm_singlet = np.zeros(len(eps_c_full))

for i, eps_c in enumerate(eps_c_full):
    S_m, S_e, r_m, r_e, _ = measure_singlet_entropy(
        H_singlet, H_norm, eps_c, N_SAMPLES, compute_r=True
    )
    S_at_full_epsc[i] = S_m
    S_err_at_full_epsc[i] = S_e
    r_at_full_epsc[i] = r_m
    r_err_at_full_epsc[i] = r_e
    S_norm_singlet[i] = S_m / S_PAGE_SINGLET

    print(f"  pq={max_pq_sums[i]}: eps_c={eps_c:.5f}  "
          f"S_singlet={S_m:.4f}+/-{S_e:.4f}  "
          f"S/S_page={S_m/S_PAGE_SINGLET:.4f}  "
          f"<r>={r_m:.4f}  "
          f"[full S/S_page={S_norm_full[i]:.4f}]")


# ============================================================
# Step 4: Full epsilon scan for the singlet block
# ============================================================
print("\n--- Step 4: Full epsilon scan for singlet block ---")

# Use a wide range: from very small to very large perturbation
eps_scan = np.concatenate([
    [0.0],
    np.geomspace(1e-4, 2.0, N_EPS_SCAN - 1)
])

S_scan = np.zeros(len(eps_scan))
S_err_scan = np.zeros(len(eps_scan))
r_scan = np.zeros(len(eps_scan))
r_err_scan = np.zeros(len(eps_scan))

for i, eps in enumerate(eps_scan):
    if eps == 0.0:
        S_scan[i] = S_0
        S_err_scan[i] = 0.0
        r_scan[i] = r_0
        r_err_scan[i] = 0.0
    else:
        S_m, S_e, r_m, r_e, _ = measure_singlet_entropy(
            H_singlet, H_norm, eps, N_SAMPLES, compute_r=True
        )
        S_scan[i] = S_m
        S_err_scan[i] = S_e
        r_scan[i] = r_m
        r_err_scan[i] = r_e

    if i % 5 == 0 or i == len(eps_scan) - 1:
        print(f"  [{i+1}/{len(eps_scan)}] eps={eps:.5f}: "
              f"S={S_scan[i]:.4f}, <r>={r_scan[i]:.4f}, S/S_page={S_scan[i]/S_PAGE_SINGLET:.4f}")


# ============================================================
# Step 5: Find the singlet's OWN dissolution crossover
# ============================================================
print("\n--- Step 5: Find singlet-own eps_c (binary search) ---")

# Binary search for <r> crossing R_MIDPOINT
eps_lo_s = 1e-4
eps_hi_s = 2.0

# Check endpoints
r_lo, _, _, _, _ = measure_singlet_entropy(H_singlet, H_norm, eps_lo_s, 50, compute_r=True)
# r_lo is the r_mean returned third
_, _, r_lo_val, _, _ = measure_singlet_entropy(H_singlet, H_norm, eps_lo_s, 50, compute_r=True)
_, _, r_hi_val, _, _ = measure_singlet_entropy(H_singlet, H_norm, eps_hi_s, 50, compute_r=True)

print(f"  eps_lo={eps_lo_s:.5f}: <r>={r_lo_val:.4f}")
print(f"  eps_hi={eps_hi_s:.5f}: <r>={r_hi_val:.4f}")

log_lo = np.log10(eps_lo_s)
log_hi = np.log10(eps_hi_s)

for step in range(N_BINARY_STEPS):
    log_mid = (log_lo + log_hi) / 2.0
    eps_mid = 10**log_mid
    _, _, r_mid, _, _ = measure_singlet_entropy(H_singlet, H_norm, eps_mid, 50, compute_r=True)
    direction = ">" if r_mid > R_MIDPOINT else "<"
    print(f"  step {step+1}/{N_BINARY_STEPS}: eps={eps_mid:.5f}, <r>={r_mid:.4f} {direction} {R_MIDPOINT:.4f}")
    if r_mid > R_MIDPOINT:
        log_hi = log_mid
    else:
        log_lo = log_mid

eps_c_singlet = 10**((log_lo + log_hi) / 2.0)

# Measure at singlet's own eps_c
S_own_m, S_own_e, r_own_m, r_own_e, _ = measure_singlet_entropy(
    H_singlet, H_norm, eps_c_singlet, 200, compute_r=True
)

print(f"\n  SINGLET OWN eps_c = {eps_c_singlet:.5f}")
print(f"  S_ent(eps_c_singlet) = {S_own_m:.4f} +/- {S_own_e:.4f}")
print(f"  S/S_page = {S_own_m/S_PAGE_SINGLET:.4f}")
print(f"  <r>(eps_c_singlet) = {r_own_m:.4f}")


# ============================================================
# Step 6: Analytical cross-check -- random 16x16 GUE at strong perturbation
# ============================================================
print("\n--- Step 6: Verification at strong perturbation (eps >> 1) ---")

S_strong_m, S_strong_e, r_strong_m, r_strong_e, S_strong_all = measure_singlet_entropy(
    H_singlet, H_norm, 10.0, 200, compute_r=True
)

print(f"  eps = 10.0 (strong perturbation limit):")
print(f"  S_ent = {S_strong_m:.4f} +/- {S_strong_e:.4f}")
print(f"  S_page(4,4) = {S_PAGE_SINGLET:.4f}")
print(f"  S/S_page = {S_strong_m/S_PAGE_SINGLET:.4f}")
print(f"  <r> = {r_strong_m:.4f}  (GOE = {R_GOE:.4f})")

# For GUE random matrices, the ground state entropy should approach S_page
# This verifies our entropy computation is correct.
print(f"\n  Verification: at eps >> 1, S/S_page should be ~1.0")
print(f"  Measured: {S_strong_m/S_PAGE_SINGLET:.4f}")
if abs(S_strong_m/S_PAGE_SINGLET - 1.0) < 0.15:
    print(f"  VERIFIED: Strong perturbation limit matches Page value within 15%.")
else:
    print(f"  WARNING: Strong perturbation limit deviates from Page by "
          f"{abs(S_strong_m/S_PAGE_SINGLET - 1.0)*100:.1f}%")


# ============================================================
# Step 7: Gate verdict
# ============================================================
print("\n" + "=" * 70)
print("DISSOLUTION-SINGLET-46: GATE VERDICT")
print("=" * 70)

# Use the MEAN S/S_page across all eps_c values for the gate
mean_S_norm_singlet = np.mean(S_norm_singlet)
std_S_norm_singlet = np.std(S_norm_singlet)
mean_S_norm_full = np.mean(S_norm_full)

print(f"\n  Mean S_singlet/S_page = {mean_S_norm_singlet:.4f} +/- {std_S_norm_singlet:.4f}")
print(f"  Mean S_full/S_page    = {mean_S_norm_full:.4f}")
print(f"  Ratio: singlet/full   = {mean_S_norm_singlet/mean_S_norm_full:.4f}")
print(f"  Singlet own eps_c: S/S_page = {S_own_m/S_PAGE_SINGLET:.4f}")

# Comparison at singlet's own crossover
print(f"\n  Per-eps_c comparison:")
print(f"  {'pq':>5s}  {'eps_c':>10s}  {'S_singlet':>10s}  {'S/S_p(sing)':>12s}  {'S/S_p(full)':>12s}")
print(f"  {'-'*60}")
for i in range(len(eps_c_full)):
    print(f"  {max_pq_sums[i]:>5d}  {eps_c_full[i]:>10.5f}  "
          f"{S_at_full_epsc[i]:>10.4f}  "
          f"{S_norm_singlet[i]:>12.4f}  "
          f"{S_norm_full[i]:>12.4f}")

# Gate decision
if mean_S_norm_singlet > 0.95:
    verdict = "PASS"
    interpretation = "GEOMETRIC"
    print(f"\n  VERDICT: PASS")
    print(f"  S_singlet/S_page = {mean_S_norm_singlet:.4f} > 0.95")
    print(f"  Suppression is GEOMETRIC: the singlet block reaches near-full Page")
    print(f"  entropy at eps_c. The 0.47 suppression in the full spectrum is caused")
    print(f"  by block-diagonal geometry (different sector sizes frustrate full")
    print(f"  entanglement across the global bipartition).")
elif abs(mean_S_norm_singlet - mean_S_norm_full) < 0.15:
    verdict = "INFO"
    interpretation = "DYNAMICAL"
    print(f"\n  VERDICT: INFO (~ 0.47 regime)")
    print(f"  S_singlet/S_page = {mean_S_norm_singlet:.4f} ~ {mean_S_norm_full:.4f} (full)")
    print(f"  Suppression is DYNAMICAL: even within a single block, the BCS/Dirac")
    print(f"  structure limits entanglement at the dissolution crossover.")
    print(f"  The information content of the Dirac spectrum itself resists dissolution.")
else:
    verdict = "INFO"
    interpretation = "INTERMEDIATE"
    print(f"\n  VERDICT: INFO (intermediate regime)")
    print(f"  S_singlet/S_page = {mean_S_norm_singlet:.4f}")
    print(f"  Neither purely geometric (>0.95) nor matching full ({mean_S_norm_full:.4f}).")
    print(f"  Both geometric and dynamical effects contribute to the suppression.")


# ============================================================
# Step 8: Physical interpretation
# ============================================================
print("\n" + "=" * 70)
print("Step 8: Physical Interpretation")
print("=" * 70)

print(f"""
  STRUCTURAL RESULT: Singlet-only dissolution entropy at eps_c.

  The singlet (0,0) sector has 16 Dirac eigenvalues with a 4x4 tensor
  bipartition. At the full-spectrum dissolution crossover eps_c, the
  singlet block produces:

    S_singlet / S_page = {mean_S_norm_singlet:.4f}   (vs. {mean_S_norm_full:.4f} for full spectrum)

  Interpretation: {interpretation}

  The singlet's OWN dissolution crossover occurs at:
    eps_c(singlet) = {eps_c_singlet:.5f}
    S_ent(eps_c_singlet) / S_page = {S_own_m/S_PAGE_SINGLET:.4f}

  Note: the singlet block is only 16-dimensional, so the dissolution
  crossover in <r> occurs at a DIFFERENT eps_c than the full spectrum.
  The 16x16 matrix has fewer level spacings (only ~14 usable ratios),
  so the <r> statistic has large fluctuations. The entropy measurement
  is more robust.
""")

# Connection to information theory
print(f"  CONNECTION TO INFORMATION PARADOX:")
print(f"  If suppression is geometric: block-diagonality acts as an effective")
print(f"  horizon for information -- modes in different sectors cannot communicate")
print(f"  their entanglement. The block structure creates a 'causal boundary' for")
print(f"  quantum correlations, analogous to how an event horizon prevents interior")
print(f"  modes from communicating with the exterior.")
print(f"")
print(f"  If suppression is dynamical: the Dirac operator's spectral structure")
print(f"  itself carries protected information. Even without sector boundaries,")
print(f"  the eigenvalue statistics resist full randomization -- the information")
print(f"  is encoded in the spectral gaps and degeneracy structure, similar to")
print(f"  how Hawking radiation's correlations encode information about the")
print(f"  black hole's microstate.")


# ============================================================
# Step 9: Save data
# ============================================================
print("\n--- Saving results ---")

save_data = {
    'tau': TAU_FOLD,
    'D_singlet': D_SINGLET,
    'd_A': D_A,
    'd_B': D_B,
    'S_page_singlet': S_PAGE_SINGLET,
    'S_max_singlet': S_MAX_SINGLET,
    'H_singlet_norm': H_norm,
    'H_singlet_evals': evals_0,
    'S_unperturbed': S_0,
    'r_unperturbed': r_0,

    # S at full-spectrum eps_c values
    'eps_c_full': eps_c_full,
    'S_at_full_epsc': S_at_full_epsc,
    'S_err_at_full_epsc': S_err_at_full_epsc,
    'r_at_full_epsc': r_at_full_epsc,
    'S_norm_singlet': S_norm_singlet,
    'S_norm_full': S_norm_full,
    'max_pq_sums': max_pq_sums,
    'N_full': N_full,

    # Full epsilon scan
    'eps_scan': eps_scan,
    'S_scan': S_scan,
    'S_err_scan': S_err_scan,
    'r_scan': r_scan,
    'r_err_scan': r_err_scan,

    # Singlet's own eps_c
    'eps_c_singlet': eps_c_singlet,
    'S_at_own_epsc': S_own_m,
    'S_err_at_own_epsc': S_own_e,
    'r_at_own_epsc': r_own_m,

    # Strong perturbation verification
    'S_strong': S_strong_m,
    'S_err_strong': S_strong_e,
    'r_strong': r_strong_m,

    # Gate results
    'mean_S_norm_singlet': mean_S_norm_singlet,
    'std_S_norm_singlet': std_S_norm_singlet,
    'mean_S_norm_full': mean_S_norm_full,
    'verdict': np.array([verdict]),
    'interpretation': np.array([interpretation]),
}

np.savez(os.path.join(SCRIPT_DIR, 's46_dissolution_singlet.npz'), **save_data)
print("  Saved: tier0-computation/s46_dissolution_singlet.npz")


# ============================================================
# Step 10: Plot
# ============================================================
print("  Generating plot...")

fig = plt.figure(figsize=(16, 14))
gs = GridSpec(2, 2, hspace=0.35, wspace=0.35)

# --- Panel 1: S_ent vs epsilon (full scan) with r on twin axis ---
ax1 = fig.add_subplot(gs[0, 0])
ax1r = ax1.twinx()

mask = eps_scan > 0
ax1.errorbar(eps_scan[mask], S_scan[mask], yerr=S_err_scan[mask],
             fmt='bo-', markersize=4, linewidth=1.5, capsize=2, label=r'$S_{\rm ent}$')
ax1.axhline(S_PAGE_SINGLET, color='blue', linestyle='--', linewidth=1,
            alpha=0.5, label=f'$S_{{\\rm Page}}$ = {S_PAGE_SINGLET:.3f}')
ax1.axhline(S_MAX_SINGLET, color='blue', linestyle=':', linewidth=0.8,
            alpha=0.3, label=f'$S_{{\\rm max}}$ = {S_MAX_SINGLET:.3f}')

r_finite = r_scan[mask & np.isfinite(r_scan)]
eps_finite = eps_scan[mask & np.isfinite(r_scan)]
ax1r.plot(eps_finite, r_finite, 'r-s', markersize=3, linewidth=1, alpha=0.7, label=r'$\langle r \rangle$')
ax1r.axhline(R_MIDPOINT, color='red', linestyle=':', linewidth=0.8, alpha=0.5)
ax1r.axhline(R_GOE, color='red', linestyle='--', linewidth=0.8, alpha=0.3)
ax1r.axhline(R_POISSON, color='red', linestyle='--', linewidth=0.8, alpha=0.3)

# Mark eps_c values
for i, ec in enumerate(eps_c_full):
    ax1.axvline(ec, color='gray', linestyle=':', linewidth=0.5, alpha=0.5)
ax1.axvline(eps_c_singlet, color='green', linestyle='-', linewidth=1.5, alpha=0.7,
            label=f'$\\epsilon_c$(singlet) = {eps_c_singlet:.4f}')

ax1.set_xlabel(r'$\epsilon$ (perturbation strength)', fontsize=12)
ax1.set_ylabel(r'$S_{\rm ent}$ (nats)', fontsize=12, color='blue')
ax1r.set_ylabel(r'$\langle r \rangle$', fontsize=12, color='red')
ax1.set_xscale('log')
ax1.set_title('Singlet (0,0) Block: Dissolution Diagnostics', fontsize=12)
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax1r.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, fontsize=7, loc='center right')
ax1.grid(True, alpha=0.2)

# --- Panel 2: S/S_page comparison ---
ax2 = fig.add_subplot(gs[0, 1])
x_pos = np.arange(len(eps_c_full))
width = 0.35

bars1 = ax2.bar(x_pos - width/2, S_norm_singlet, width,
                color='steelblue', alpha=0.8, label='Singlet (16 modes)')
bars2 = ax2.bar(x_pos + width/2, S_norm_full, width,
                color='coral', alpha=0.8, label='Full spectrum')

ax2.axhline(1.0, color='black', linestyle='--', linewidth=1, label='Full Page')
ax2.axhline(0.95, color='green', linestyle=':', linewidth=1, label='PASS threshold (0.95)')
ax2.axhline(0.47, color='gray', linestyle=':', linewidth=1, alpha=0.5, label='Full mean (~0.47)')

ax2.set_xlabel('Truncation level (pq)', fontsize=12)
ax2.set_ylabel(r'$S_{\rm ent} / S_{\rm Page}$', fontsize=12)
ax2.set_title('Singlet vs Full Spectrum: Normalized Entropy at $\\epsilon_c$', fontsize=12)
ax2.set_xticks(x_pos)
ax2.set_xticklabels([f'pq={pq}\nN={int(N)}' for pq, N in zip(max_pq_sums, N_full)], fontsize=8)
ax2.legend(fontsize=8)
ax2.set_ylim(0, 1.3)
ax2.grid(True, alpha=0.2, axis='y')

# --- Panel 3: Normalized entropy scan ---
ax3 = fig.add_subplot(gs[1, 0])

mask_s = eps_scan > 0
ax3.plot(eps_scan[mask_s], S_scan[mask_s] / S_PAGE_SINGLET,
         'ko-', markersize=4, linewidth=1.5, label=r'$S/S_{\rm Page}$ (singlet)')
ax3.axhline(1.0, color='red', linestyle='--', linewidth=1, label='Full Page')
ax3.axhline(0.95, color='green', linestyle=':', linewidth=1, label='PASS threshold')
ax3.axhline(mean_S_norm_full, color='orange', linestyle=':', linewidth=1.5,
            label=f'Full spectrum mean ({mean_S_norm_full:.3f})')
ax3.axvline(eps_c_singlet, color='green', linestyle='-', linewidth=1.5, alpha=0.7,
            label=f'$\\epsilon_c$(singlet)')

for i, ec in enumerate(eps_c_full):
    ax3.axvline(ec, color='gray', linestyle=':', linewidth=0.5, alpha=0.4)

ax3.set_xlabel(r'$\epsilon$', fontsize=12)
ax3.set_ylabel(r'$S_{\rm ent} / S_{\rm Page}$', fontsize=12)
ax3.set_title('Normalized Entropy vs Perturbation', fontsize=12)
ax3.set_xscale('log')
ax3.set_ylim(0, 1.3)
ax3.legend(fontsize=8, loc='lower right')
ax3.grid(True, alpha=0.2)

# --- Panel 4: Eigenvalue spectrum of singlet block ---
ax4 = fig.add_subplot(gs[1, 1])

# Show eigenvalues of singlet block and spacing statistics
ax4.stem(np.arange(len(evals_0)), evals_0, linefmt='b-', markerfmt='bo', basefmt='k-',
         label='Eigenvalues')
ax4.set_xlabel('Mode index', fontsize=12)
ax4.set_ylabel('Energy (M_KK)', fontsize=12)
ax4.set_title(f'Singlet (0,0) Dirac Eigenvalues at $\\tau$ = {TAU_FOLD}', fontsize=12)
ax4.legend(fontsize=9)
ax4.grid(True, alpha=0.2)

# Add text annotation with key results
text_str = (f'$S/S_{{\\rm Page}}$(singlet) = {mean_S_norm_singlet:.3f}\n'
            f'$S/S_{{\\rm Page}}$(full) = {mean_S_norm_full:.3f}\n'
            f'$\\epsilon_c$(singlet) = {eps_c_singlet:.4f}\n'
            f'Interpretation: {interpretation}')
ax4.text(0.95, 0.95, text_str, transform=ax4.transAxes, fontsize=9,
         verticalalignment='top', horizontalalignment='right',
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

fig.suptitle(f'DISSOLUTION-SINGLET-46: Singlet-Only Entanglement at Dissolution\n'
             f'Verdict: {verdict} | Interpretation: {interpretation}',
             fontsize=13, fontweight='bold')

plt.savefig(os.path.join(SCRIPT_DIR, 's46_dissolution_singlet.png'),
            dpi=150, bbox_inches='tight')
print("  Saved: tier0-computation/s46_dissolution_singlet.png")


# ============================================================
# Final timing and summary
# ============================================================
t_end = time.time()
print(f"\nTotal runtime: {t_end - t_start:.1f}s ({(t_end - t_start)/60:.1f}min)")

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)
print(f"\n  Singlet (0,0) block: 16 eigenvalues, 4x4 tensor bipartition")
print(f"  S_page(4,4) = {S_PAGE_SINGLET:.4f}")
print(f"  Unperturbed S = {S_0:.6f}")
print(f"\n  At full-spectrum eps_c values:")
print(f"    S_singlet/S_page = {mean_S_norm_singlet:.4f} +/- {std_S_norm_singlet:.4f}")
print(f"    S_full/S_page    = {mean_S_norm_full:.4f}")
print(f"\n  Singlet's own eps_c = {eps_c_singlet:.5f}")
print(f"    S(eps_c_singlet)/S_page = {S_own_m/S_PAGE_SINGLET:.4f}")
print(f"\n  Strong perturbation (eps=10):")
print(f"    S/S_page = {S_strong_m/S_PAGE_SINGLET:.4f}  (should be ~1.0)")
print(f"\n  VERDICT: {verdict}")
print(f"  INTERPRETATION: {interpretation}")
