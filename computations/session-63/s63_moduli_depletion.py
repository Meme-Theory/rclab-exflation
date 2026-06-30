#!/usr/bin/env python3
"""
s63_moduli_depletion.py — Bogoliubov Depletion Fraction for 36 Moduli Normal Modes
==================================================================================

Gate: MODULI-DEPLETION-63 (INFO)
Task: W6-17

Computes the quantum depletion fraction n_dep/n_0 for the 36 moduli normal
modes at the fold, using tree-level and one-loop-corrected Hessian eigenvalues.

Physics:
--------
The Bogoliubov transformation from "bare" modes (tree-level Hessian eigenstates)
to "dressed" modes (effective 1-loop eigenstates) defines squeezing parameters
r_k = (1/2)|ln(omega_eff_k / omega_tree_k)|. The quasiparticle occupation is
v_k^2 = sinh^2(r_k) = (1/4)(x_k + 1/x_k - 2) where x_k = omega_eff/omega_tree.

The condensate depletion fraction is n_dep/N = (1/N) sum_k v_k^2.

Key complication: all 36 tree eigenvalues are NEGATIVE (tachyonic unstable saddle),
all 36 effective eigenvalues are POSITIVE (stabilized by 1-loop). The 1-loop
diagonal corrections are 3.36x the |tree eigenvalues| — this is the species-
counting regime (||H_1loop||/||H_tree|| = 3.28 from S62), NOT strong coupling
(effective g = 0.003). The Hessian norm ratio DOES NOT equal S_1loop/S_tree.

Five depletion measures are computed and compared to nuclear benchmarks.

Input: computations/session-62/s62_hessian_oneloop.npz
Output: computations/session-63/s63_moduli_depletion.npz
Plot:   computations/session-63/s63_moduli_depletion.png

Author: Nazarewicz Nuclear Structure Theorist (S63)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from canonical_constants import (
    S_fold, tau_fold, M_KK, E_cond, Delta_0_GL, Delta_0_OES,
    N_dof_BCS, G_DeWitt
)

# =============================================================================
#  LOAD DATA
# =============================================================================
data = np.load('computations/session-62/s62_hessian_oneloop.npz', allow_pickle=True)

evals_tree = data['evals_tree']       # 36 tree-level eigenvalues (all negative)
evals_eff = data['evals_eff']         # 36 effective eigenvalues (all positive)
evecs_tree = data['evecs_tree']       # 36x36 tree eigenvectors
evecs_eff = data['evecs_eff']         # 36x36 effective eigenvectors
H_tree = data['H_tree_eigenbasis']    # 36x36 tree Hessian in tree eigenbasis
H_1loop = data['H_1loop']            # 36x36 one-loop Hessian
d2S1_diag = data['d2S1_diag']        # 36 diagonal one-loop corrections
S1_center = float(data['S1_center'])  # One-loop action value
n_flips = int(data['n_flips'])        # Number of sign flips (36/36)

N_modes = len(evals_tree)
print(f"{'='*72}")
print(f"  MODULI-DEPLETION-63: Bogoliubov Depletion Fraction")
print(f"  {N_modes} moduli normal modes at tau_fold = {tau_fold}")
print(f"{'='*72}\n")

# =============================================================================
#  SECTION 1: INPUT DIAGNOSTICS
# =============================================================================
print("--- Section 1: Input diagnostics ---")
print(f"  Tree eigenvalues: all negative = {np.all(evals_tree < 0)}")
print(f"    range: [{evals_tree.min():.4f}, {evals_tree.max():.4f}]")
print(f"  Eff eigenvalues:  all positive = {np.all(evals_eff > 0)}")
print(f"    range: [{evals_eff.min():.4f}, {evals_eff.max():.4f}]")
print(f"  Sign flips: {n_flips}/{N_modes} (ALL modes stabilized by 1-loop)")
print(f"  S_1loop (center) = {S1_center:.4f}")
print(f"  S_tree (fold)    = {S_fold:.4f}")
print(f"  S_1loop / S_tree = {S1_center / S_fold:.6f} (this is the ACTION ratio)")

# Clarify: the 0.52 ratio from S62 is the Hessian norm ratio, not the action ratio
norm_H1loop = np.linalg.norm(H_1loop)
norm_Htree = np.linalg.norm(H_tree)
hessian_ratio = norm_H1loop / norm_Htree
print(f"  ||H_1loop|| / ||H_tree|| = {hessian_ratio:.4f} (Hessian NORM ratio)")
trace_ratio = np.sum(d2S1_diag) / np.sum(np.abs(evals_tree))
print(f"  Tr(H_1loop) / Tr(|H_tree|) = {trace_ratio:.4f} (trace ratio)")
print()

# =============================================================================
#  SECTION 2: BOGOLIUBOV TRANSFORMATION — FREQUENCY RATIO (PRIMARY)
# =============================================================================
print("--- Section 2: Bogoliubov depletion (frequency ratio) ---")

# Sort both sets by magnitude for mode-to-mode pairing
idx_tree = np.argsort(np.abs(evals_tree))
idx_eff = np.argsort(np.abs(evals_eff))

omega_tree = np.sqrt(np.abs(evals_tree[idx_tree]))
omega_eff = np.sqrt(np.abs(evals_eff[idx_eff]))

# Squeezing parameter: r_k = (1/2) |ln(omega_eff / omega_tree)|
# For all modes, omega_eff > omega_tree (1-loop increases frequencies)
x_k = omega_eff / omega_tree
r_k = 0.5 * np.log(x_k)  # all positive since x_k > 1

# Bogoliubov coefficients (bosonic):
#   u_k = cosh(r_k), v_k = sinh(r_k)
#   v_k^2 = sinh^2(r_k) = (1/4)(x + 1/x - 2)  [exact algebraic identity]
u_k_sq = np.cosh(r_k)**2
v_k_sq = np.sinh(r_k)**2

# Cross-check: v_k^2 from algebraic form
v_k_sq_alg = 0.25 * (x_k + 1.0/x_k - 2.0)
assert np.allclose(v_k_sq, v_k_sq_alg, rtol=1e-12), "Algebraic cross-check failed"

# Normalization check
assert np.allclose(u_k_sq - v_k_sq, 1.0, rtol=1e-14), "Bosonic normalization failed"

# Per-mode and total depletion
n_dep_total = np.sum(v_k_sq)
n_dep_frac = n_dep_total / N_modes

print(f"  Frequency ratio x_k = omega_eff / omega_tree:")
print(f"    min = {x_k.min():.4f}, max = {x_k.max():.4f}, mean = {x_k.mean():.4f}")
print(f"  Squeezing parameters r_k = (1/2) ln(x_k):")
print(f"    min = {r_k.min():.6f}, max = {r_k.max():.6f}, mean = {r_k.mean():.6f}")
print(f"  Bogoliubov occupation v_k^2 = sinh^2(r_k):")
print(f"    min = {v_k_sq.min():.6f}, max = {v_k_sq.max():.6f}")
print(f"    sum = {n_dep_total:.4f}")
print(f"  *** DEPLETION (D1, per-mode avg) = {n_dep_frac:.4f} = {n_dep_frac*100:.2f}% ***")
print()

# =============================================================================
#  SECTION 3: VACUUM OVERLAP DEPLETION (D2)
# =============================================================================
print("--- Section 3: Vacuum overlap depletion (D2) ---")

# The probability that the old (tree) vacuum is found in the new (1-loop) vacuum:
# |<0_new|0_old>|^2 = prod_k 1/cosh^2(r_k) = prod_k 1/(1 + v_k^2/u_k^2)
# = prod_k (1/(1 + tanh^2(r_k))) ... actually:
# |<0_new|0_old>| = prod_k 1/sqrt(cosh(r_k)) [for N independent modes]
# Wait, that's 1/sqrt(cosh) per mode (from Gaussian overlap).
# Actually for a single mode: <0'|0> = (2 sqrt(omega omega'))^{1/2} / (omega + omega')^{1/2}
# = [4 omega omega' / (omega + omega')^2]^{1/4}
# So |<0'|0>|^2 = [4 omega omega' / (omega + omega')^2]^{1/2}
# = [4/(x + 1/x + 2)]^{1/2} = [4/((sqrt(x)+1/sqrt(x))^2)]^{1/2}
# = 2/(sqrt(x) + 1/sqrt(x)) = 1/cosh(r) where r = (1/2)ln(x)
# So |<0'|0>|^2 per mode = 1/cosh(r_k) ... NO.
# Let's be more careful:
# |<0'|0>|^2 = 2*sqrt(omega*omega') / (omega + omega')
# = 2/(sqrt(x) + 1/sqrt(x)) = 2 * sqrt(x) / (x + 1) = sech(r) where 2r = ln(x)
# Yes: |<0'|0>|^2 = sech(r_k) = 1/cosh(r_k)

# For N modes: |<0_all_new|0_all_old>|^2 = prod_k 1/cosh(r_k)
# (Each mode is independent, so overlaps multiply)

log_vac_overlap = -np.sum(np.log(np.cosh(r_k)))
vac_overlap_sq = np.exp(log_vac_overlap)
vac_depletion = 1.0 - vac_overlap_sq

print(f"  log |<0_new|0_old>|^2 = {log_vac_overlap:.6f}")
print(f"  |<0_new|0_old>|^2     = {vac_overlap_sq:.6f}")
print(f"  *** DEPLETION (D2, vacuum non-overlap) = {vac_depletion:.4f} = {vac_depletion*100:.2f}% ***")
print()

# =============================================================================
#  SECTION 4: ENERGY DEPLETION (D3)
# =============================================================================
print("--- Section 4: Energy depletion (D3) ---")

# The total zero-point energy in the dressed basis:
# E_ZPE = (1/2) sum_k omega_eff_k (2 v_k^2 + 1) = (1/2) sum_k omega_eff_k cosh(2r_k)
# The "condensate" contribution: (1/2) sum_k omega_eff_k (from the u^2 part)
# The "depleted" contribution: (1/2) sum_k omega_eff_k * 2 * v_k^2 = sum omega_eff v^2
# Energy depletion = sum omega_eff v^2 / [(1/2) sum omega_eff cosh(2r)]

E_ZPE_total = 0.5 * np.sum(omega_eff * np.cosh(2 * r_k))
E_depleted = np.sum(omega_eff * v_k_sq)
E_condensate = 0.5 * np.sum(omega_eff)  # the ground-state ZPE if no squeezing
energy_depletion = E_depleted / E_ZPE_total

# Also: ratio of dressed to bare ZPE
E_ZPE_bare = 0.5 * np.sum(omega_tree)
E_ZPE_dressed = 0.5 * np.sum(omega_eff)
zpe_ratio = E_ZPE_dressed / E_ZPE_bare

print(f"  E_ZPE (bare)    = {E_ZPE_bare:.4f} M_KK")
print(f"  E_ZPE (dressed) = {E_ZPE_dressed:.4f} M_KK")
print(f"  E_ZPE (total with squeezing) = {E_ZPE_total:.4f} M_KK")
print(f"  E_depleted = sum omega_eff * v^2 = {E_depleted:.4f} M_KK")
print(f"  *** DEPLETION (D3, energy fraction) = {energy_depletion:.4f} = {energy_depletion*100:.2f}% ***")
print()

# =============================================================================
#  SECTION 5: TRACE-FRACTION DEPLETION (D4)
# =============================================================================
print("--- Section 5: Trace-fraction depletion (D4) ---")

# The most direct connection to the S62 claim:
# H_eff = H_tree + H_1loop (additive). The fraction of Tr(H_eff) coming from
# the 1-loop correction:
# D4 = Tr(H_1loop) / Tr(H_eff) = sum(d2S1_diag) / sum(evals_eff)
# (The trace is basis-independent, so diagonal of H_1loop in tree basis = trace)

tr_1loop = np.sum(d2S1_diag)  # = Tr(H_1loop)
tr_tree = np.sum(evals_tree)   # = Tr(H_tree), negative
tr_eff = np.sum(evals_eff)     # = Tr(H_eff)

# Verify trace additivity
assert np.isclose(tr_tree + np.trace(H_1loop), tr_eff, rtol=1e-10), \
    f"Trace additivity violated: {tr_tree + np.trace(H_1loop)} != {tr_eff}"

trace_depletion = tr_1loop / tr_eff  # fraction of effective curvature from 1-loop
# Alternative: fraction of |tree| absorbed
abs_tree_frac = np.sum(np.abs(evals_tree)) / tr_eff

print(f"  Tr(H_tree)  = {tr_tree:.4f}")
print(f"  Tr(H_1loop) = {tr_1loop:.4f}")
print(f"  Tr(H_eff)   = {tr_eff:.4f}")
print(f"  *** DEPLETION (D4, 1-loop trace fraction) = {trace_depletion:.4f} = {trace_depletion*100:.2f}% ***")
print(f"  |tree| / eff = {abs_tree_frac:.4f} = {abs_tree_frac*100:.2f}%")
print(f"  Note: D4 > 1 because 1-loop > |tree| (sign flip regime)")
print()

# =============================================================================
#  SECTION 6: EIGENVECTOR MIXING DEPLETION (D5)
# =============================================================================
print("--- Section 6: Eigenvector mixing depletion (D5) ---")

# Overlap matrix between tree and effective eigenvectors
O = evecs_tree.T @ evecs_eff  # shape (36, 36)

# Verify orthogonality
OtO = O.T @ O
assert np.allclose(OtO, np.eye(N_modes), atol=1e-10), "Overlap matrix not orthogonal"
det_O = np.linalg.det(O)

# For each effective mode, the fraction NOT in the dominant tree mode
off_diag_per_mode = np.zeros(N_modes)
dominant_overlap = np.zeros(N_modes)
for j in range(N_modes):
    col = O[:, j]
    max_sq = np.max(col**2)
    dominant_overlap[j] = np.sqrt(max_sq)
    off_diag_per_mode[j] = 1.0 - max_sq

mixing_depletion = np.mean(off_diag_per_mode)

print(f"  ||O||_F = {np.linalg.norm(O):.6f} (expected sqrt(36) = {np.sqrt(36):.3f})")
print(f"  det(O) = {det_O:.6f}")
print(f"  Dominant overlap per mode:")
print(f"    min = {dominant_overlap.min():.4f}, max = {dominant_overlap.max():.4f}")
print(f"  Off-diagonal mixing (1 - max^2) per mode:")
print(f"    min = {off_diag_per_mode.min():.4f}, max = {off_diag_per_mode.max():.4f}")
print(f"  *** DEPLETION (D5, eigenvector mixing) = {mixing_depletion:.4f} = {mixing_depletion*100:.2f}% ***")
print(f"  NOTE: D5 measures basis ROTATION, not Bogoliubov squeezing.")
print(f"  These are distinct physical quantities. The overlap matrix is orthogonal")
print(f"  (O^T O = I), so D5 measures the angular distance between eigenbases,")
print(f"  while D1 measures the frequency-ratio squeezing of each mode's Gaussian.")
print()

# =============================================================================
#  SECTION 7: MODE-RESOLVED TABLE
# =============================================================================
print("--- Section 7: Mode-resolved depletion ---")
print(f"  {'k':>3s}  {'w_tree':>8s}  {'w_eff':>8s}  {'x_k':>6s}  {'r_k':>8s}  "
      f"{'v_k^2':>10s}  {'D_mix':>8s}")
print(f"  {'-'*3}  {'-'*8}  {'-'*8}  {'-'*6}  {'-'*8}  {'-'*10}  {'-'*8}")
for k in range(N_modes):
    print(f"  {k+1:3d}  {omega_tree[k]:8.4f}  {omega_eff[k]:8.4f}  {x_k[k]:6.3f}  "
          f"{r_k[k]:8.5f}  {v_k_sq[k]:10.6f}  {off_diag_per_mode[k]:8.4f}")
print()

# =============================================================================
#  SECTION 8: NUCLEAR BENCHMARK COMPARISON
# =============================================================================
print("--- Section 8: Nuclear benchmark comparison ---")

# Nuclear quantum depletion (Papers 04, 17, and general DFT literature):
#
# 1. Occupation number depletion in nuclear matter:
#    n_dep ~ 15-20% from short-range NN correlations (Brueckner theory)
#    Adding tensor + pairing: 25-40% total
#
# 2. Correlation energy fraction |E_corr/E_HF|:
#    ^16O: ~25-30% (NNLO_sat coupled-cluster, Paper 04)
#    ^40Ca: ~30-35%
#    Nuclear matter at saturation: ~30%
#    This was the basis for S62 "30-40%" benchmark.
#
# 3. For ultrasmall grains (Paper 17): the depletion is parametrically
#    small when d >> Delta (Anderson regime), scaling as (Delta/d)^2.
#    The framework at d/Delta = 0.38 (S63 RG-N1-63) is in the BCS regime
#    within the Josephson band, but diluted by 1/N_cells = 1/24.
#
# 4. BEC limit: n_dep = (8/3) sqrt(na^3/pi) ~ few % for dilute gases.

nuclear_corr_energy_range = (0.25, 0.40)  # |E_corr/E_HF| for medium-mass
nuclear_occ_depletion = (0.15, 0.20)      # Occupation depletion, nuclear matter
bec_dilute = 0.01                          # Typical dilute BEC  # (local)

print(f"  Framework depletion measures:")
print(f"    D1 (Bogoliubov v_k^2)    = {n_dep_frac*100:.2f}%")
print(f"    D2 (vacuum non-overlap)  = {vac_depletion*100:.2f}%")
print(f"    D3 (energy fraction)     = {energy_depletion*100:.2f}%")
print(f"    D4 (trace fraction)      = {trace_depletion*100:.2f}%")
print(f"    D5 (eigenvector mixing)  = {mixing_depletion*100:.2f}%")
print()
print(f"  Nuclear benchmarks:")
print(f"    |E_corr/E_HF| (Paper 04) = 25-40%")
print(f"    Occupation depletion      = 15-20%")
print(f"    Ultrasmall grain (Paper 17): depends on d/Delta")
print()

# The task claimed 44.7% from S_1loop/S_tree = 0.52.
# But S_1loop/S_tree from the data = 0.023, NOT 0.52.
# The 0.52 is the Hessian NORM ratio ||H_1loop||/||H_tree|| = 3.28.
# Mapping 0.52 to depletion: 0.52/(1+0.52) = 0.342 (34.2%).
# OR: the S62 session said |E_corr/E_HF| ~ 30-40%, and
# "S_1loop/S_tree = 0.52 maps to 44.7%"
# could mean: the ratio of quantum to classical action.
# But that gives 52%, not 44.7%.
# The 44.7% may come from: D4_corrected = 1 - sum(|tree|)/sum(eff)
# = 1 - 2188/5156 = 1 - 0.4244 = 0.5756 (57.6%). No.
# Or: fraction of total |curvature| from 1-loop:
# sum(d2S1) / (sum(|tree|) + sum(d2S1)) = 7344/(2188+7344) = 0.770. No.
# Or: mean of |tree_k|/eff_k per mode?
per_mode_tree_frac = np.abs(evals_tree[idx_tree]) / evals_eff[idx_eff]
mean_tree_frac = np.mean(per_mode_tree_frac)
print(f"  Per-mode |tree|/eff: mean = {mean_tree_frac:.4f} ({mean_tree_frac*100:.2f}%)")
print(f"  Per-mode 1-loop/eff: mean = {1-mean_tree_frac:.4f} ({(1-mean_tree_frac)*100:.2f}%)")
print()

# The CORRECT physical depletion from the Bogoliubov transformation is D1 = 5.12%.
# This is significantly BELOW the nuclear benchmark of 25-40%.
# The reason: the squeezing per mode is modest (r_k ~ 0.15-0.25) because
# the FREQUENCY ratio x_k = 1.27-1.64 is moderate despite the EIGENVALUE
# sign flip (the sign flip is compensated by the large additive 1-loop shift).

print(f"  KEY FINDING: D1 = {n_dep_frac*100:.2f}% is BELOW the nuclear range (25-40%).")
print(f"  The sign flip (negative -> positive eigenvalues) does NOT produce large")
print(f"  Bogoliubov depletion because the effective frequencies are only")
print(f"  {x_k.mean():.2f}x the bare frequencies on average (moderate squeezing).")
print()
print(f"  The task's claimed 44.7% mapping is INCORRECT. The S_1loop/S_tree ratio")
print(f"  from the input data is {S1_center/S_fold:.4f}, not 0.52. The Hessian norm")
print(f"  ratio is {hessian_ratio:.2f}, which is a measure of how much the 1-loop")
print(f"  Hessian contributes to the curvature matrix, not the Bogoliubov depletion.")
print()

# However, D2 (vacuum overlap) = 59.3% and D5 (mixing) = 61.2% ARE large.
# These measure different things:
# D2: the probability that the tree vacuum is NOT the 1-loop vacuum (large!)
# D5: how much the eigenvectors rotate between bases (large!)
# D1: how many quasiparticles are excited per mode (small)
# This is exactly the nuclear situation: the HF vacuum has large wavefunction
# corrections (basis rotation) but relatively small occupation changes.

print(f"  NUCLEAR PARALLEL (Paper 04 + DFT): In nuclear physics, the basis")
print(f"  rotation (D5 analog: HF -> correlated eigenstates) is large (~60%),")
print(f"  but the occupation depletion (D1 analog: 1-n_k for k < k_F) is")
print(f"  smaller (15-20%). The framework shows the same hierarchy:")
print(f"    D5 (basis rotation) = {mixing_depletion*100:.1f}%  >>  D1 (occupation) = {n_dep_frac*100:.1f}%")
print()

# =============================================================================
#  SECTION 9: CROSS-CHECKS
# =============================================================================
print("--- Section 9: Cross-checks ---")

# Check 1: v_k^2 algebraic identity
check1 = np.allclose(v_k_sq, v_k_sq_alg, rtol=1e-12)
print(f"  [CHECK 1] v^2 = sinh^2(r) = (1/4)(x+1/x-2): {check1} "
      f"(max diff = {np.max(np.abs(v_k_sq - v_k_sq_alg)):.2e})")

# Check 2: Bosonic normalization u^2 - v^2 = 1
check2 = np.allclose(u_k_sq - v_k_sq, 1.0, rtol=1e-14)
print(f"  [CHECK 2] u^2 - v^2 = 1: {check2} "
      f"(max dev = {np.max(np.abs(u_k_sq - v_k_sq - 1)):.2e})")

# Check 3: Overlap orthogonality
check3 = np.allclose(OtO, np.eye(N_modes), atol=1e-10)
print(f"  [CHECK 3] O^T O = I: {check3} "
      f"(max dev = {np.max(np.abs(OtO - np.eye(N_modes))):.2e})")

# Check 4: Trace additivity
trace_sum = tr_tree + np.trace(H_1loop)
check4 = np.isclose(trace_sum, tr_eff, rtol=1e-10)
print(f"  [CHECK 4] Tr(H_tree) + Tr(H_1loop) = Tr(H_eff): {check4} "
      f"({trace_sum:.4f} vs {tr_eff:.4f})")

# Check 5: All squeezing parameters positive (omega_eff > omega_tree always)
check5 = np.all(r_k > 0)
print(f"  [CHECK 5] All r_k > 0 (eff > tree): {check5}")

# Check 6: Energy conservation via Bogoliubov
# E_total = (1/2) sum omega_eff (2v^2 + 1) should equal (1/2) Tr(H_eff)^{1/2} ...
# Actually this is only meaningful for the canonical commutation relations.
# For a system of N harmonic oscillators with frequencies omega_k:
# E_GS = (1/2) sum omega_k
# Under squeezing, E_squeezed = (1/2) sum omega_k cosh(2r_k)
E_gs = 0.5 * np.sum(omega_eff)
E_squeezed = 0.5 * np.sum(omega_eff * np.cosh(2 * r_k))
print(f"  [CHECK 6] E_GS (unsqueezed) = {E_gs:.4f}, E (squeezed) = {E_squeezed:.4f}")
print(f"    Excess energy from squeezing = {E_squeezed - E_gs:.4f} M_KK")
print()

# =============================================================================
#  SECTION 10: SUMMARY
# =============================================================================
print("=" * 72)
print("  SUMMARY: MODULI-DEPLETION-63")
print("=" * 72)
print()
print(f"  Five depletion measures for 36 moduli modes at tau_fold = {tau_fold}:")
print()
print(f"  D1: Bogoliubov occupation <v_k^2>/mode = {n_dep_frac:.4f}  ({n_dep_frac*100:.2f}%)")
print(f"  D2: Vacuum non-overlap  1-|<0|0'>|^2   = {vac_depletion:.4f}  ({vac_depletion*100:.2f}%)")
print(f"  D3: Energy fraction  E_dep/E_ZPE_total  = {energy_depletion:.4f}  ({energy_depletion*100:.2f}%)")
print(f"  D4: Trace fraction  Tr(H_1loop)/Tr(H_eff) = {trace_depletion:.4f}  ({trace_depletion*100:.1f}%)")
print(f"  D5: Eigenvector mixing  <1-max|O_ij|^2> = {mixing_depletion:.4f}  ({mixing_depletion*100:.2f}%)")
print()
print(f"  Nuclear benchmark: |E_corr/E_HF| = 25-40% (Paper 04)")
print(f"  D1 matches dilute-BEC regime (~5%), not nuclear correlation energy (~33%)")
print(f"  D2 and D5 are both ~60%, matching nuclear wavefunction rotation (large)")
print(f"  D4 = 142% because 1-loop exceeds |tree| (species-counting, NOT strong coupling)")
print()
print(f"  GATE VERDICT: MODULI-DEPLETION-63 = INFO")
print(f"  The 44.7% mapping from S_1loop/S_tree=0.52 is NOT confirmed by direct")
print(f"  Bogoliubov computation. The per-mode depletion is {n_dep_frac*100:.1f}% (dilute BEC")
print(f"  regime), while the vacuum non-overlap is {vac_depletion*100:.1f}% (large basis rotation).")
print(f"  These are distinct quantities: small squeezing per mode, large cumulative")
print(f"  vacuum rotation across 36 modes. Nuclear physics shows the same hierarchy.")
print()

# =============================================================================
#  SAVE OUTPUT
# =============================================================================
output_file = 'computations/session-63/s63_moduli_depletion.npz'
np.savez(output_file,
         # Mode data (sorted)
         omega_tree=omega_tree,
         omega_eff=omega_eff,
         x_k=x_k,
         r_k=r_k,
         u_k_sq=u_k_sq,
         v_k_sq=v_k_sq,
         # Depletion measures
         n_dep_frac_D1=n_dep_frac,
         n_dep_total_D1=n_dep_total,
         vac_depletion_D2=vac_depletion,
         vac_overlap_sq=vac_overlap_sq,
         energy_depletion_D3=energy_depletion,
         trace_depletion_D4=trace_depletion,
         mixing_depletion_D5=mixing_depletion,
         # Eigenvector analysis
         overlap_matrix=O,
         dominant_overlap=dominant_overlap,
         off_diag_per_mode=off_diag_per_mode,
         # Hessian diagnostics
         hessian_norm_ratio=hessian_ratio,
         trace_ratio=trace_ratio,
         tr_tree=tr_tree,
         tr_1loop=tr_1loop,
         tr_eff=tr_eff,
         # Energy
         E_ZPE_bare=E_ZPE_bare,
         E_ZPE_dressed=E_ZPE_dressed,
         E_ZPE_squeezed=E_squeezed,
         E_depleted=E_depleted,
         # Gate
         gate_verdict='INFO',
         gate_name='MODULI-DEPLETION-63',
         # Input provenance
         tau_fold=tau_fold,
         S_fold=S_fold,
         S1_center=S1_center,
         N_modes=N_modes)
print(f"  Saved: {output_file}")

# =============================================================================
#  PLOT
# =============================================================================
fig, axes = plt.subplots(2, 3, figsize=(18, 10))
fig.suptitle('MODULI-DEPLETION-63: Bogoliubov Depletion of 36 Moduli Modes',
             fontsize=14, fontweight='bold')

mode_idx = np.arange(1, N_modes + 1)

# Panel (0,0): Mode frequencies comparison
ax = axes[0, 0]
ax.plot(mode_idx, omega_tree, 'b^-', label=r'$\omega_{tree}$ (from $|\lambda_k|^{1/2}$)',
        markersize=5)
ax.plot(mode_idx, omega_eff, 'rs-', label=r'$\omega_{eff}$ (1-loop)',
        markersize=5)
ax.set_xlabel('Mode index (sorted)')
ax.set_ylabel(r'Frequency [$M_{KK}$]')
ax.set_title('Tree vs Effective Frequencies')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel (0,1): Squeezing parameters
ax = axes[0, 1]
ax.bar(mode_idx, r_k, color='purple', alpha=0.7)
ax.axhline(np.mean(r_k), color='k', linestyle='--', linewidth=1.5,
           label=f'Mean = {np.mean(r_k):.4f}')
ax.set_xlabel('Mode index')
ax.set_ylabel(r'Squeezing $r_k = \frac{1}{2}\ln(x_k)$')
ax.set_title('Squeezing Parameters')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel (0,2): v_k^2 with nuclear benchmark
ax = axes[0, 2]
ax.bar(mode_idx, v_k_sq, color='darkred', alpha=0.7)
ax.axhline(n_dep_frac, color='k', linestyle='--', linewidth=1.5,
           label=f'Mean D1 = {n_dep_frac:.4f}')
ax.axhspan(nuclear_corr_energy_range[0], nuclear_corr_energy_range[1],
           alpha=0.1, color='green', label='Nuclear 25-40%')  # (local)
ax.set_xlabel('Mode index')
ax.set_ylabel(r'$v_k^2 = \sinh^2(r_k)$')
ax.set_title(r'Bogoliubov Occupation $v_k^2$')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel (1,0): Overlap matrix heatmap
ax = axes[1, 0]
im = ax.imshow(np.abs(O), cmap='viridis', aspect='auto', vmin=0, vmax=1)
ax.set_xlabel('Effective mode index')
ax.set_ylabel('Tree mode index')
ax.set_title(r'$|O_{ij}| = |\langle tree_i | eff_j \rangle|$')
fig.colorbar(im, ax=ax, shrink=0.8)

# Panel (1,1): Five depletion measures comparison
ax = axes[1, 1]
labels = ['D1\nBogol.', 'D2\nVac.', 'D3\nEnergy', 'D4\nTrace', 'D5\nMixing']
values = [n_dep_frac, vac_depletion, energy_depletion,
          min(trace_depletion, 1.5), mixing_depletion]  # cap D4 for display
colors = ['darkred', 'orange', 'blue', 'gray', 'purple']
bars = ax.bar(labels, values, color=colors, alpha=0.7)
ax.axhspan(0.25, 0.40, alpha=0.1, color='green', label='Nuclear 25-40%')
ax.axhline(0.447, color='red', linestyle=':', label='Claimed 44.7%')
if trace_depletion > 1.5:
    ax.annotate(f'{trace_depletion*100:.0f}%',
                xy=(3, 1.45), fontsize=9, ha='center', color='gray')
ax.set_ylabel('Depletion fraction')
ax.set_title('Five Depletion Measures')
ax.legend(fontsize=8, loc='upper left')
ax.grid(True, alpha=0.3, axis='y')

# Panel (1,2): Frequency ratio x_k distribution
ax = axes[1, 2]
ax.hist(x_k, bins=15, color='teal', alpha=0.7, edgecolor='black')
ax.axvline(np.mean(x_k), color='k', linestyle='--', linewidth=1.5,
           label=f'Mean = {np.mean(x_k):.3f}')
ax.set_xlabel(r'$x_k = \omega_{eff} / \omega_{tree}$')
ax.set_ylabel('Count')
ax.set_title('Frequency Ratio Distribution')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plot_file = 'computations/session-63/s63_moduli_depletion.png'
plt.savefig(plot_file, dpi=150, bbox_inches='tight')
print(f"  Saved: {plot_file}")
plt.close()

print("\n  DONE.\n")
