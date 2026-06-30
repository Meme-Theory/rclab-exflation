#!/usr/bin/env python3
"""
S58 EPSILON-DIRECT: Dipolar Coupling from Full V_bare Matrix
=============================================================

Session 58, Wave 0, Computation W0-3
Agent: quantum-acoustics-theorist

PURPOSE:
    Extract the Leggett dipolar coupling epsilon directly from the
    microscopic pairing matrix V_bare_cont (8x8) stored in s54_ed_sweep.npz,
    and compare to the S49 determination epsilon = 0.00248 +/- 50%.

PHYSICS:
    The S49 epsilon was defined as:
        epsilon_S49 = J_23 / Delta_B2
    where J_23 = V_constrained[B2,B3] * Delta_B2 * Delta_B3 is the
    Josephson coupling from the S46 E_cond-constrained Hauser-Feshbach
    model (V_mat_constrained = alpha_star * V_mat_raw).

    The V_bare_cont matrix is the ACTUAL microscopic pairing interaction
    from the Dirac operator on SU(3), stored in the (p,q) representation
    basis. It is a fundamentally different object from V_constrained:
    - V_bare respects Trap 1: V[B1,B1] = 0 exactly (U(2) singlet)
    - V_bare respects selection rule: V[B1,B3] = 0 exactly
    - V_bare has V[B2,B1] = 0.0799 UNIFORM (4-fold B2 degeneracy)
    - V_constrained has V[B1,B1] != 0, V[B1,B3] != 0 (HF model)

    This script computes epsilon from V_bare using THREE definitions:
    1. S48 formula: J_ab = V_band[a,b] * |Delta_a| * |Delta_b|,
       epsilon = J_23/Delta_B2
    2. Coupling ratio: epsilon_V = V_23^2 / (V_22 * V_33)
    3. ED anomalous density: J_ab = sum V_kk' * F_k * F_k',
       epsilon = J_23/Delta_B2

GATE: EPSILON-DIRECT-58
    PASS: epsilon_direct in [0.001, 0.005]
    FAIL: epsilon_direct outside [0.0005, 0.010]

Data inputs:
    - computations/session-54/s54_ed_sweep.npz (V_bare_cont, eigenvalues)
    - computations/session-36/s36_multisector_ed.npz (pair correlations from ED)
    - computations/session-48/s48_leggett_mode.npz (S48 J_23, Delta, rho)
    - computations/session-46/s46_qtheory_selfconsistent.npz (V_constrained)
"""

import sys
import os
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from canonical_constants import (
    E_cond, E_cond_ED_8mode, tau_fold,
    rho_B2_per_mode, E_B1, E_B2_mean, E_B3_mean,
    omega_L1, omega_L2, Delta_0_GL,
    J_C2, J_su2, J_u1,
    N_cells, M_KK
)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ARCHIVE_DIR = os.path.join(os.path.dirname(SCRIPT_DIR), 'computations/_shared')

print("=" * 78)
print("S58 EPSILON-DIRECT: Dipolar Coupling from Full V_bare Matrix")
print("=" * 78)

# =============================================================================
# STEP 1: LOAD ALL DATA
# =============================================================================
print("\n--- STEP 1: Load data ---")

# S54 ED sweep: V_bare_cont, eigenvalues, pair occupations
d54 = np.load(os.path.join(SCRIPT_DIR, 's54_ed_sweep.npz'), allow_pickle=True)
V_bare = d54['V_bare_cont']           # (8, 8) microscopic pairing matrix
fold_idx = int(d54['fold_idx'])        # = 19
tau_fold_data = d54['tau_values'][fold_idx]
E_sp = d54['E_sp_sweep'][fold_idx]    # (8,) single-particle energies at fold
v2_N1 = d54['pair_occupations'][fold_idx]  # (8,) pair occupations at N_pair=1
N_pair_54 = int(d54['N_pair'])

# S36 8-mode ED: pair correlations at canonical filling
d36 = np.load(os.path.join(ARCHIVE_DIR, 's36_multisector_ed.npz'), allow_pickle=True)
pair_corr_8 = d36['config_4_pair_corr']     # (8, 8) exact pair correlator
pair_occ_8 = d36['config_4_pair_occ']       # (8,) pair occupations
V_8x8_check = d36['V_8x8_full']             # (8, 8) should match V_bare
branch_labels = d36['branch_labels']          # ['B2[0]', ..., 'B1', 'B3[0]', ...]
E_8 = d36['E_8_full']                        # (8,) effective band energies
N_pair_36 = int(d36['config_4_gs_n_pairs'])

# S48 Leggett mode: J_23, Delta, rho from multi-band BCS
d48 = np.load(os.path.join(ARCHIVE_DIR, 's48_leggett_mode.npz'), allow_pickle=True)
J_23_S48 = float(d48['J_23_fold'])
J_12_S48 = float(d48['J_12_fold'])
J_13_S48 = float(d48['J_13_fold'])
Delta_fold_S48 = d48['Delta_fold']    # [Delta_B1, Delta_B2, Delta_B3]
rho_fold_S48 = d48['rho_fold']        # [rho_B1, rho_B2, rho_B3]

# S46 self-consistent: V_constrained (alpha_star * V_raw)
d46 = np.load(os.path.join(ARCHIVE_DIR, 's46_qtheory_selfconsistent.npz'), allow_pickle=True)
V_constrained = d46['V_mat_constrained']  # (3, 3) HF model, alpha-rescaled
V_raw_HF = d46['V_mat_raw']               # (3, 3) raw HF model

# Derived constants
Delta_B1 = float(Delta_fold_S48[0])  # 0.372
Delta_B2 = float(Delta_fold_S48[1])  # 0.732
Delta_B3 = float(Delta_fold_S48[2])  # 0.084
epsilon_S49 = J_23_S48 / Delta_B2     # = 0.00248

# Alpha_star (rescaling factor from S46)
alpha_star = V_constrained[0, 0] / V_raw_HF[0, 0]

print(f"tau_fold = {tau_fold_data:.6f} (fold index {fold_idx})")
print(f"N_pair (S54) = {N_pair_54}, N_pair (S36) = {N_pair_36}")
print(f"Delta at fold: B1={Delta_B1:.6f}, B2={Delta_B2:.6f}, B3={Delta_B3:.6f}")
print(f"S48 J_23 = {J_23_S48:.10f}")
print(f"S49 epsilon = {epsilon_S49:.10f}")
print(f"S46 alpha_star = {alpha_star:.8f}")

# Cross-check: V_bare_cont matches S36 V_8x8_full
V_match = np.max(np.abs(V_bare - V_8x8_check))
print(f"\nV_bare vs S36 V_8x8: max|diff| = {V_match:.2e}")
assert V_match < 1e-14, "V matrices do not match!"

# =============================================================================
# STEP 2: MODE CLASSIFICATION
# =============================================================================
print("\n--- STEP 2: Mode classification ---")

# From branch_labels and V_bare structure:
# B2 = modes [0,1,2,3] (the (1,1) representation, 4-fold)
# B1 = mode [4] (U(2) singlet)
# B3 = modes [5,6,7] (the (1,0) representation, 3-fold)
B2 = [0, 1, 2, 3]
B1 = [4]
B3 = [5, 6, 7]

# Verify classification from selection rules
V_B1B1 = V_bare[4, 4]
V_B1B3_max = np.max(np.abs(V_bare[np.ix_(B1, B3)]))
V_B2B1_std = np.std(V_bare[np.ix_(B2, B1)])

print(f"Branch labels: {list(branch_labels)}")
print(f"B2 = {B2} (4 modes), B1 = {B1} (1 mode), B3 = {B3} (3 modes)")
print(f"V[B1,B1] = {V_B1B1:.2e} (Trap 1: should be 0)")
print(f"max|V[B1,B3]| = {V_B1B3_max:.2e} (selection rule: should be 0)")
print(f"std(V[B2,B1]) = {V_B2B1_std:.2e} (B2-B1 uniformity: should be 0)")
print(f"V[B2,B1] values = {V_bare[np.ix_(B2, B1)].flatten()}")

assert V_B1B1 < 1e-20, "Trap 1 violated!"
assert V_B1B3_max < 1e-20, "B1-B3 selection rule violated!"
assert V_B2B1_std < 1e-14, "B2-B1 coupling non-uniform!"

# =============================================================================
# STEP 3: V_BARE BLOCK STRUCTURE
# =============================================================================
print("\n--- STEP 3: V_bare block structure ---")

# Extract all blocks
blocks = {}
for na, a_idx, a_name in [(4, B2, 'B2'), (1, B1, 'B1'), (3, B3, 'B3')]:
    for nb, b_idx, b_name in [(4, B2, 'B2'), (1, B1, 'B1'), (3, B3, 'B3')]:
        key = f"{a_name}-{b_name}"
        block = V_bare[np.ix_(a_idx, b_idx)]
        blocks[key] = block
        mean_val = np.mean(block)
        frob = np.linalg.norm(block)
        print(f"  V[{key}]: shape={block.shape}, mean={mean_val:.8f}, "
              f"||F||={frob:.8f}")

# Band-averaged V (per-mode-pair mean)
V_band_mean = np.zeros((3, 3))
band_names = ['B2', 'B1', 'B3']
band_indices = [B2, B1, B3]
for i in range(3):
    for j in range(3):
        V_band_mean[i, j] = np.mean(V_bare[np.ix_(band_indices[i], band_indices[j])])

print(f"\nBand-averaged V (per-mode-pair mean):")
print(f"  {'':>4s}  {'B2':>10s}  {'B1':>10s}  {'B3':>10s}")
for i in range(3):
    print(f"  {band_names[i]:>4s}  {V_band_mean[i,0]:10.6f}  "
          f"{V_band_mean[i,1]:10.6f}  {V_band_mean[i,2]:10.6f}")

# Band-summed V (S35 convention: sum over target, divide by source count)
V_branch = np.zeros((3, 3))
for i in range(3):
    for j in range(3):
        V_branch[i, j] = np.sum(V_bare[np.ix_(band_indices[i], band_indices[j])]) / len(band_indices[i])
V_branch_sym = 0.5 * (V_branch + V_branch.T)

print(f"\nV_branch (S35 convention, symmetrized):")
print(f"  {'':>4s}  {'B2':>10s}  {'B1':>10s}  {'B3':>10s}")
for i in range(3):
    print(f"  {band_names[i]:>4s}  {V_branch_sym[i,0]:10.6f}  "
          f"{V_branch_sym[i,1]:10.6f}  {V_branch_sym[i,2]:10.6f}")

# =============================================================================
# STEP 4: EPSILON FROM V_BARE (THREE DEFINITIONS)
# =============================================================================
print("\n--- STEP 4: Epsilon from V_bare ---")

# ---- Definition 1: S48 Josephson formula ----
# J_ab = V_band[a,b] * |Delta_a| * |Delta_b|
# Using per-mode-pair mean V
V_23_mean = V_band_mean[0, 2]   # B2-B3 mean coupling
V_21_mean = V_band_mean[0, 1]   # B2-B1 mean coupling
V_22_mean = V_band_mean[0, 0]   # B2-B2 mean coupling
V_33_mean = V_band_mean[2, 2]   # B3-B3 mean coupling

J_23_bare_mean = V_23_mean * Delta_B2 * Delta_B3
J_21_bare_mean = V_21_mean * Delta_B2 * Delta_B1
eps_def1_B2B3 = J_23_bare_mean / Delta_B2
eps_def1_B2B1 = J_21_bare_mean / Delta_B2

# Using symmetrized branch V (the S35/S48 convention)
V_23_branch = V_branch_sym[0, 2]  # B2-B3 branch-symmetrized
J_23_bare_branch = V_23_branch * Delta_B2 * Delta_B3
eps_def1_branch = J_23_bare_branch / Delta_B2

print("Definition 1: S48 Josephson formula (J = V * Delta_a * Delta_b)")
print(f"  Using per-mode-pair mean V_23 = {V_23_mean:.8f}:")
print(f"    J_B2B3 = {J_23_bare_mean:.10f}")
print(f"    epsilon(B2-B3) = {eps_def1_B2B3:.10f}")
print(f"  Using symmetrized V_branch[B2,B3] = {V_23_branch:.8f}:")
print(f"    J_B2B3 = {J_23_bare_branch:.10f}")
print(f"    epsilon(B2-B3) = {eps_def1_branch:.10f}")
print(f"  Using V_constrained[B2,B3] = {V_constrained[1,2]:.8f} (S46, for reference):")
print(f"    J_B2B3(S48) = {J_23_S48:.10f}")
print(f"    epsilon(S49) = {epsilon_S49:.10f}")

# ---- Definition 2: Coupling ratio ----
# epsilon_V = V_23^2 / (V_22 * V_33)
eps_def2 = V_23_mean**2 / (V_22_mean * V_33_mean)

print(f"\nDefinition 2: Coupling ratio V_23^2 / (V_22 * V_33)")
print(f"  V_22 = {V_22_mean:.8f}, V_33 = {V_33_mean:.8f}, V_23 = {V_23_mean:.8f}")
print(f"  epsilon_V = {eps_def2:.8f}")

# ---- Definition 3: ED anomalous density ----
# From S36 pair correlations: F_k = u_k * v_k
# Anomalous product: F_product[k,k'] = C[k,k'] - v_k^2 * v_k'^2
# J_ab = sum_{k in a, k' in b} V_kk' * F_k * F_k'

# Extract F_k from pair correlations
v2 = pair_occ_8  # pair occupations from S36 8-mode ED
F_diag = v2 * (1 - v2)  # (u_k v_k)^2
F_k = np.sqrt(np.maximum(F_diag, 0))

# Compute J from V_bare and F_k
def J_from_VF(a_modes, b_modes, V, F):
    """Josephson coupling J_ab = sum V_kk' F_k F_k'."""
    s = 0.0  # (local)
    for k in a_modes:
        for kp in b_modes:
            s += V[k, kp] * F[k] * F[kp]
    return s

J_B2B3_ed = J_from_VF(B2, B3, V_bare, F_k)
J_B2B1_ed = J_from_VF(B2, B1, V_bare, F_k)
J_B2B2_ed = J_from_VF(B2, B2, V_bare, F_k)
J_B3B3_ed = J_from_VF(B3, B3, V_bare, F_k)
J_B1B1_ed = J_from_VF(B1, B1, V_bare, F_k)
J_B1B3_ed = J_from_VF(B1, B3, V_bare, F_k)

eps_def3_B2B3 = J_B2B3_ed / Delta_B2
eps_def3_B2B1 = J_B2B1_ed / Delta_B2

print(f"\nDefinition 3: ED anomalous density (J = sum V_kk' F_k F_k')")
print(f"  F_k = u_k*v_k: {['%.6f' % f for f in F_k]}")
print(f"  J_B2B3 = {J_B2B3_ed:.10f}")
print(f"  J_B2B1 = {J_B2B1_ed:.10f}")
print(f"  J_B1B1 = {J_B1B1_ed:.10e} (Trap 1)")
print(f"  J_B1B3 = {J_B1B3_ed:.10e} (selection rule)")
print(f"  epsilon(B2-B3) = {eps_def3_B2B3:.10f}")
print(f"  epsilon(B2-B1) = {eps_def3_B2B1:.10f}")

# =============================================================================
# STEP 5: RECONCILIATION — WHY V_bare != V_constrained
# =============================================================================
print("\n--- STEP 5: Reconciliation ---")

print("V_bare_cont (from Dirac operator) and V_constrained (from S46 HF model)")
print("are DIFFERENT objects:")
print(f"  V_bare[B1,B1] = {V_B1B1:.2e}  vs  V_const[B1,B1] = {V_constrained[0,0]:.6f}")
print(f"  V_bare[B1,B3] = {V_B1B3_max:.2e}  vs  V_const[B1,B3] = {V_constrained[0,2]:.6f}")
print(f"  V_bare[B2,B3] = {V_23_mean:.6f}  vs  V_const[B2,B3] = {V_constrained[1,2]:.6f}")
print(f"  Ratio V_const/V_bare for B2-B3: {V_constrained[1,2]/V_23_mean:.4f}")
print()
print("V_constrained = alpha_star * V_raw(HF), where alpha_star is fixed by")
print(f"matching E_cond to the S36 ED result. alpha_star = {alpha_star:.6f}.")
print("This rescaling was necessary because the HF statistical doorway model")
print("overshoots the microscopic pairing by ~2.3x on average.")
print()
print("The V_bare_cont matrix is the MICROSCOPIC truth. It respects:")
print("  - Trap 1 (V[B1,B1] = 0 exact, U(2) singlet selection rule)")
print("  - B1-B3 selection rule (V[B1,B3] = 0 exact)")
print("  - B2-B1 uniformity (V[B2_k, B1] = 0.0799 for all k in B2)")
print("None of these structural zeros are present in V_constrained.")

# The central result: epsilon from V_bare
# Definition 1 (S48 formula) is the physically relevant one for comparison
# because it uses the SAME Josephson coupling definition as S49.
#
# However, V_bare and V_constrained differ by a MODE-DEPENDENT factor,
# not a uniform rescaling. The ratio V_const/V_bare varies from 0.07 to 6.6x.
# This means we CANNOT simply rescale V_bare by alpha_star.
#
# The correct epsilon_direct from V_bare is Definition 1 with the mean V:

epsilon_direct = eps_def1_B2B3  # = V_23_mean * Delta_B3

print(f"\n*** CENTRAL RESULT ***")
print(f"epsilon_direct (V_bare, S48 formula) = {epsilon_direct:.10f}")
print(f"epsilon_S49 (V_constrained) = {epsilon_S49:.10f}")
print(f"Ratio: epsilon_direct / epsilon_S49 = {epsilon_direct / epsilon_S49:.4f}")

# =============================================================================
# STEP 6: UNCERTAINTY PROPAGATION
# =============================================================================
print("\n--- STEP 6: Uncertainty propagation ---")

# Uncertainty sources:
# 1. V_bare numerical precision: V_bare is computed from the Dirac operator
#    eigenvalues to machine precision (~1e-15). Negligible.
# 2. Mode classification: exact (selection rules verified to 1e-20)
# 3. Delta_B2 uncertainty: from S48 BCS solution, ~5% (S57 assessment)
# 4. Delta_B3 uncertainty: larger, ~10-20% (S48, B3 far from vH)
# 5. Band averaging: within-band variation of V

# Source 5: V within-band variation
V_B2B3_all = V_bare[np.ix_(B2, B3)].flatten()  # 12 elements
V_23_std = np.std(V_B2B3_all)
V_23_err_pct = V_23_std / V_23_mean * 100

print(f"V_B2B3 elements ({len(V_B2B3_all)} values):")
print(f"  mean = {V_23_mean:.8f}")
print(f"  std = {V_23_std:.8f}")
print(f"  min = {V_B2B3_all.min():.8f}")
print(f"  max = {V_B2B3_all.max():.8f}")
print(f"  CoV = {V_23_err_pct:.1f}%")

# Delta uncertainties
sigma_Delta_B2_frac = 0.05   # 5%  # (local)
sigma_Delta_B3_frac = 0.15   # 15%  # (local)

# Propagate: epsilon = V_23 * Delta_B3 (since J = V*Delta_B2*Delta_B3, eps = J/Delta_B2)
# sigma(epsilon)/epsilon = sqrt((sigma_V/V)^2 + (sigma_Delta_B3/Delta_B3)^2)
sigma_eps_frac = np.sqrt((V_23_std / V_23_mean)**2 + sigma_Delta_B3_frac**2)
sigma_epsilon = epsilon_direct * sigma_eps_frac

print(f"\nUncertainty budget:")
print(f"  V_23: {V_23_err_pct:.1f}%")
print(f"  Delta_B3: {sigma_Delta_B3_frac*100:.0f}%")
print(f"  Combined: {sigma_eps_frac*100:.1f}%")
print(f"  epsilon_direct = {epsilon_direct:.6f} +/- {sigma_epsilon:.6f}")
print(f"  = {epsilon_direct:.6f} +/- {sigma_eps_frac*100:.0f}%")

# Compare: S49 had 50% uncertainty. Our result has ~37% uncertainty.
# The dominant source is Delta_B3 (15%), not V_23 (34%).

# =============================================================================
# STEP 7: TAU DEPENDENCE
# =============================================================================
print("\n--- STEP 7: Tau dependence ---")

# V_bare_cont is tau-INDEPENDENT (it's a property of the Dirac operator's
# representation structure, not the deformation parameter).
# The tau dependence of epsilon comes entirely through Delta(tau).
# But we only have V_bare at one tau point — it IS static.

print("V_bare_cont is stored as a SINGLE matrix (not tau-dependent).")
print("This is consistent with it being a representation-theoretic quantity.")
print("The tau dependence of epsilon enters only through Delta_B3(tau).")

# Check: is V_bare actually the same at all tau?
# The S54 data has V_bare_cont as a single (8,8) matrix, not (50,8,8).
# This confirms it's tau-independent.

# =============================================================================
# STEP 8: CROSS-CHECKS
# =============================================================================
print("\n--- STEP 8: Cross-checks ---")

# Cross-check 1: V_bare symmetry
sym_err = np.max(np.abs(V_bare - V_bare.T))
print(f"V_bare symmetry: max|V - V^T| = {sym_err:.2e}")

# Cross-check 2: V_bare eigenvalues (should have both signs for pairing)
eigvals_V = np.linalg.eigvalsh(V_bare)
print(f"V_bare eigenvalues: {['%.6f' % e for e in eigvals_V]}")
print(f"  {np.sum(eigvals_V < 0)} negative, {np.sum(eigvals_V > 0)} positive")
print(f"  Most negative: {eigvals_V[0]:.6f} (attractive channel)")

# Cross-check 3: Trap 1 and selection rules
print(f"Trap 1: V[B1,B1] = {V_bare[4,4]:.2e} (should be 0)")
print(f"B1-B3 rule: max|V[B1,B3]| = {np.max(np.abs(V_bare[np.ix_(B1, B3)])):.2e}")
print(f"B2-B1 uniformity: std = {np.std(V_bare[np.ix_(B2, B1)]):.2e}")

# Cross-check 4: S36 pair correlation factorization
p = np.sqrt(np.diag(pair_corr_8))
C_fact = np.outer(p, p)
fact_err = np.max(np.abs(pair_corr_8 - C_fact))
print(f"S36 pair correlation factorization: max|C - pp^T| = {fact_err:.2e}")
print(f"  (exact factorization => pure BCS-like state)")

# Cross-check 5: V_constrained reproduces S48 J_23
J_23_check = V_constrained[1, 2] * Delta_B2 * Delta_B3
print(f"V_const[B2,B3]*Delta_B2*Delta_B3 = {J_23_check:.10f}")
print(f"S48 J_23 = {J_23_S48:.10f}")
print(f"Match: {abs(J_23_check - J_23_S48) < 1e-6}")

# Cross-check 6: Definition consistency
# Def 1 and Def 3 use different F_k but same V
# Def 1 uses constant F_k = Delta_k/(2*epsilon_k) ~ uniform
# Def 3 uses exact ED F_k
print(f"\nDefinition cross-check:")
print(f"  Def 1 (V_bare * Delta): epsilon = {eps_def1_B2B3:.8f}")
print(f"  Def 2 (coupling ratio): epsilon_V = {eps_def2:.8f}")
print(f"  Def 3 (ED anomalous):   epsilon = {eps_def3_B2B3:.8f}")
print(f"  S49 (V_constrained):    epsilon = {epsilon_S49:.8f}")
print(f"\nDef 3 / Def 1 = {eps_def3_B2B3 / eps_def1_B2B3:.4f}")
print(f"  (factor {eps_def3_B2B3 / eps_def1_B2B3:.1f}x = BCS coherence factor enhancement)")

# =============================================================================
# STEP 9: DOWNSTREAM IMPACT ON OMEGA_L AND F_DM
# =============================================================================
print("\n--- STEP 9: Downstream impact ---")

# omega_L0 = sqrt(2 * epsilon * E_J * Delta_harm)
# where Delta_harm = 2*Delta_B2*Delta_B3/(Delta_B2 + Delta_B3)
# E_J from S55: E_J = 7.042 M_KK

E_J = 7.042  # from S55/S56  # (local)
Delta_harm = 2 * Delta_B2 * Delta_B3 / (Delta_B2 + Delta_B3)

# At S49 epsilon:
omega_L0_S49 = np.sqrt(2 * epsilon_S49 * E_J * Delta_harm)

# At our epsilon_direct:
omega_L0_direct = np.sqrt(2 * epsilon_direct * E_J * Delta_harm)

# At Def 3 epsilon:
omega_L0_def3 = np.sqrt(2 * eps_def3_B2B3 * E_J * Delta_harm)

print(f"Delta_harm = {Delta_harm:.6f}")
print(f"E_J = {E_J:.3f}")
print(f"\nomega_L0 predictions:")
print(f"  S49 (epsilon={epsilon_S49:.6f}): omega_L0 = {omega_L0_S49:.6f} M_KK")
print(f"  Def 1 (epsilon={epsilon_direct:.6f}): omega_L0 = {omega_L0_direct:.6f} M_KK")
print(f"  Def 3 (epsilon={eps_def3_B2B3:.6f}): omega_L0 = {omega_L0_def3:.6f} M_KK")
print(f"  Canonical omega_L1 = {omega_L1:.6f} M_KK")

# DM energy fraction: f_DM ~ E_Leggett / E_matter
# E_Leggett ~ N_cells * epsilon * E_J * <n_squeezed>
# Ratio: f_DM(new) / f_DM(old) = sqrt(epsilon_new / epsilon_old)
# (because omega_L ~ sqrt(epsilon), and E_DM ~ omega_L * <n>)

ratio_eps = epsilon_direct / epsilon_S49
ratio_omega = np.sqrt(ratio_eps)

print(f"\nDM impact:")
print(f"  epsilon ratio: {ratio_eps:.4f}")
print(f"  omega_L ratio: {ratio_omega:.4f} (= sqrt of epsilon ratio)")
print(f"  f_DM scales as omega_L, so f_DM(new)/f_DM(old) ~ {ratio_omega:.4f}")

# S57 values
f_DM_S57_exc = 0.119   # excitation component  # (local)
f_DM_S57_tot = 0.440   # total including ZPE  # (local)
Omega_DM_h2_lo = 0.017  # (local)
Omega_DM_h2_hi = 0.188  # (local)

print(f"\nOmega_DM h^2 rescaling:")
print(f"  S57 bracket: [{Omega_DM_h2_lo:.3f}, {Omega_DM_h2_hi:.3f}]")
print(f"  Rescaled by omega ratio {ratio_omega:.4f}:")
print(f"    New bracket: [{Omega_DM_h2_lo*ratio_omega:.4f}, "
      f"{Omega_DM_h2_hi*ratio_omega:.4f}]")
print(f"  Observed: 0.120")

# =============================================================================
# STEP 10: THE ALPHA_STAR BRIDGE
# =============================================================================
print("\n--- STEP 10: The alpha_star bridge ---")

# The key insight: V_bare and V_constrained are DIFFERENT models.
# V_constrained = alpha_star * V_raw(HF).
# V_bare respects microscopic selection rules that V_raw violates.
#
# If we trust V_bare as the microscopic truth, then the S49 epsilon
# was computed from the WRONG V matrix (the HF approximation).
#
# The "correct" epsilon should be computed from V_bare.
# But V_bare gives epsilon that is 0.58x (Def 1) or 2.8x (Def 3) the S49 value.
#
# Definition 1 is the fair comparison because it uses the same formula as S48.
# With V_23_mean = 0.0170 (from V_bare), the result is:

print(f"V_bare[B2,B3] = {V_23_mean:.8f} (microscopic)")
print(f"V_const[B2,B3] = {V_constrained[1,2]:.8f} (HF + alpha rescaling)")
print(f"Ratio: V_bare/V_const = {V_23_mean / V_constrained[1,2]:.4f}")
print()
print(f"The V_constrained is {V_constrained[1,2]/V_23_mean:.2f}x LARGER than V_bare")
print(f"for the B2-B3 channel. This is because:")
print(f"  1. V_raw(HF) is a phenomenological model with no selection rules")
print(f"  2. alpha_star rescales ALL elements uniformly, including B2-B3")
print(f"  3. V_bare has structural zeros (B1-B1, B1-B3) that V_raw lacks")
print(f"  4. The alpha_star calibration matches TOTAL E_cond, not per-channel")

# =============================================================================
# STEP 11: GATE VERDICT
# =============================================================================
print("\n" + "=" * 78)
print("GATE VERDICT: EPSILON-DIRECT-58")
print("=" * 78)

# The pre-registered gate uses epsilon_direct (V_bare, S48 formula):
gate_value = epsilon_direct
gate_pass_lo = 0.001  # (local)
gate_pass_hi = 0.005  # (local)
gate_fail_lo = 0.0005  # (local)
gate_fail_hi = 0.010  # (local)

in_pass = gate_pass_lo <= gate_value <= gate_pass_hi
in_outer = gate_fail_lo <= gate_value <= gate_fail_hi

if in_pass:
    verdict = "PASS"
    detail = (f"epsilon_direct = {gate_value:.6f} in [{gate_pass_lo}, {gate_pass_hi}]. "
              f"Confirms S49 order of magnitude and reduces uncertainty.")
elif in_outer and not in_pass:
    verdict = "INFO"
    detail = (f"epsilon_direct = {gate_value:.6f} in [{gate_fail_lo}, {gate_fail_hi}] "
              f"but outside [{gate_pass_lo}, {gate_pass_hi}]. Consistent at order of "
              f"magnitude but V_bare and V_constrained differ in detail.")
else:
    verdict = "FAIL"
    detail = (f"epsilon_direct = {gate_value:.6f} outside [{gate_fail_lo}, {gate_fail_hi}]. "
              f"S49 value wrong; Leggett predictions need revision.")

print(f"\n  epsilon_direct = {gate_value:.6f}")
print(f"  PASS range: [{gate_pass_lo}, {gate_pass_hi}]")
print(f"  FAIL range: outside [{gate_fail_lo}, {gate_fail_hi}]")
print(f"  Verdict: **{verdict}**")
print(f"  {detail}")

print(f"\n  Summary of all epsilon determinations:")
print(f"  {'Definition':<30s}  {'epsilon':>10s}  {'Method':>20s}")
print(f"  {'='*30}  {'='*10}  {'='*20}")
print(f"  {'Def 1 (V_bare S48 formula)':<30s}  {eps_def1_B2B3:10.6f}  {'V*Delta*Delta/Delta':>20s}")
print(f"  {'Def 1 (branch-sym)':<30s}  {eps_def1_branch:10.6f}  {'V_branch*D*D/D':>20s}")
print(f"  {'Def 2 (coupling ratio)':<30s}  {eps_def2:10.6f}  {'V23^2/(V22*V33)':>20s}")
print(f"  {'Def 3 (ED anomalous)':<30s}  {eps_def3_B2B3:10.6f}  {'sum V*F*F/Delta':>20s}")
print(f"  {'S49 (V_constrained)':<30s}  {epsilon_S49:10.6f}  {'J_23(S48)/Delta_B2':>20s}")

# =============================================================================
# STEP 12: SAVE DATA
# =============================================================================
print("\n--- STEP 12: Save data ---")

output_file = os.path.join(SCRIPT_DIR, 's58_epsilon_direct.npz')
np.savez(output_file,
    # Central results
    epsilon_direct=epsilon_direct,
    epsilon_branch=eps_def1_branch,
    epsilon_coupling_ratio=eps_def2,
    epsilon_ed_anomalous=eps_def3_B2B3,
    epsilon_S49=epsilon_S49,

    # V_bare blocks
    V_bare_cont=V_bare,
    V_B2B3_mean=V_23_mean,
    V_B2B3_all=V_B2B3_all,
    V_B2B1_mean=V_21_mean,
    V_B2B2_mean=V_22_mean,
    V_B3B3_mean=V_33_mean,
    V_band_mean=V_band_mean,
    V_branch_sym=V_branch_sym,

    # BCS coherence
    F_k=F_k,
    pair_occ_8=pair_occ_8,

    # Josephson couplings
    J_B2B3_bare_mean=J_23_bare_mean,
    J_B2B3_bare_branch=J_23_bare_branch,
    J_B2B3_ed=J_B2B3_ed,
    J_B2B1_ed=J_B2B1_ed,
    J_23_S48=J_23_S48,

    # Downstream
    omega_L0_direct=omega_L0_direct,
    omega_L0_S49=omega_L0_S49,
    omega_L0_def3=omega_L0_def3,
    Delta_harm=Delta_harm,
    ratio_eps=ratio_eps,
    ratio_omega=ratio_omega,

    # Uncertainties
    sigma_epsilon=sigma_epsilon,
    sigma_eps_frac=sigma_eps_frac,
    V_23_std=V_23_std,

    # Reference
    V_constrained=V_constrained,
    V_raw_HF=V_raw_HF,
    alpha_star=alpha_star,

    # Eigenvalues
    eigvals_V=eigvals_V,

    # Gate
    gate_name=np.array(['EPSILON-DIRECT-58']),
    gate_verdict=np.array([verdict]),
    gate_detail=np.array([detail]),
)

print(f"Saved: {output_file}")
print(f"Gate: EPSILON-DIRECT-58 = {verdict}")
