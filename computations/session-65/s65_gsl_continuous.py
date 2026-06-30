#!/usr/bin/env python3
"""
GSL-CONTINUOUS-65 — Continuous dS/dtau Through Transit
======================================================

Gate: GSL-CONTINUOUS-65
Pre-registered criterion:
    PASS: dS/dtau >= 0 at all 20 tau values.
    FAIL: dS/dtau < 0 at any tau value.

Physics:
    S64 verified the generalized second law at 4 discrete stages
    (BCS -> transit -> GGE -> Gibbs). This computation extends to
    a continuous trajectory: S_spec(tau) at 20 tau values from 0 to 0.50.

    The spectral entropy arises from Bogoliubov particle creation during
    the transit through the van Hove fold. As tau increases from 0 toward
    the fold at tau=0.19 and beyond, the D_K eigenvalue spectrum reorganizes.
    This spectral reorganization acts as a parametric drive on the BCS
    quasiparticle modes, creating excitations via the Parker mechanism
    (Parker 1969, Paper 15; Hawking 1975, Paper 05).

    The Bogoliubov occupation number at each tau determines the entropy:
        f_n(tau) = |beta_n(tau)|^2 / (1 + |beta_n(tau)|^2)
    for the fermionic (BCS) quasiparticle modes.

    The spectral entropy (von Neumann entropy of the reduced state):
        S_spec(tau) = sum_n [-f_n ln f_n - (1-f_n) ln(1-f_n)]

    The Parker pair creation rate:
        dN/dtau = sum_n d|beta_n|^2/dtau
    should be proportional to dS/dtau with coefficient ~ln(2) per pair
    (each new pair adds approximately ln(2) of entropy when f ~ 1/2).

    S57 data provides |beta_k|^2 at 9 tau checkpoints (0.10 to 0.50)
    for 31 modes. We interpolate to 20 uniformly-spaced tau values
    and compute the continuous entropy trajectory.

    CRITICAL: The 8 BCS modes are FERMIONIC Bogoliubov quasiparticles.
    The occupation satisfies 0 <= f_n <= 1. The entropy per mode is
    the binary (fermionic) entropy. |beta_k|^2 uses the BOSONIC
    convention (|alpha|^2 - |beta|^2 = 1), so the fermionic occupation is
    f_n = |beta_n|^2 / (1 + |beta_n|^2).

References:
    - Parker 1969 (Paper 15): Quantized fields and particle creation
    - Hawking 1975 (Paper 05): Particle creation by black holes
    - Bekenstein 1973 (Paper 11): Black holes and entropy
    - Wall 2009 (Paper 40): Ten proofs of the generalized second law
    - S57 s57_parker_ba.npz: Parker Bogoliubov at 9 tau checkpoints
    - S61 BACKREACTION-PARKER-61: |beta_k|^2 = 1.015 universal
    - S64 POST-TRANSIT-THERMODYNAMICS-64: GSL at 4 discrete stages

Author: Hawking-Theorist (S65)
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
from scipy.interpolate import PchipInterpolator
import sys
import os

# Import canonical constants
sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import (
    tau_fold, n_Bog, N_dof_BCS, n_pairs,
    E_B1, E_B2_mean, E_B3_mean, T_acoustic,
    dt_transit, PI, M_ATDHFB, Z_fold, dS_fold, d2S_fold,
    S_fold, c_fabric, v_terminal, H_fold
)

print("=" * 72)
print("GSL-CONTINUOUS-65: Continuous dS/dtau Through Transit")
print("=" * 72)

# ===========================================================================
# Section 1: Load Input Data
# ===========================================================================

data_dir = Path(__file__).parent

# S57 Parker Bogoliubov data: |beta_k|^2 at 9 tau checkpoints for 31 modes
d57 = np.load(data_dir / 's57_parker_ba.npz', allow_pickle=True)
tau_57 = d57['tau_checkpoints']       # shape (9,): [0.1, 0.15, 0.19, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5]
beta_sq_57 = d57['beta_sq']           # shape (31, 9)
alpha_sq_57 = d57['alpha_sq']         # shape (31, 9)
v_tau_57 = float(d57['v_tau'])        # transit velocity dtau/dt

# S64 GSL entropy data (for cross-check against discrete stages)
d64 = np.load(data_dir / 's64_gsl_entropy.npz', allow_pickle=True)
S_GGE_S64 = float(d64['S_GGE_total'])
S_Gibbs_S64 = float(d64['S_Gibbs_exact'])
beta_sq_univ = float(d64['beta_sq_universal'])

# S64 epsilon profile (spectral action as function of tau)
d64_eps = np.load(data_dir / 's64_epsilon_profile.npz', allow_pickle=True)
tau_dense = d64_eps['tau_dense']       # shape (500,)
S_dense = d64_eps['S_dense']           # spectral action S(tau), shape (500,)
dS_dense = d64_eps['dS_dense']         # dS/dtau, shape (500,)
d2S_dense = d64_eps['d2S_dense']       # d2S/dtau2, shape (500,)

print("\n--- Input data loaded ---")
print(f"  S57 tau checkpoints: {tau_57}")
print(f"  S57 beta_sq shape:   {beta_sq_57.shape} (31 modes x 9 tau)")
print(f"  S64 S_GGE = {S_GGE_S64:.4f} nats")
print(f"  S64 S_Gibbs = {S_Gibbs_S64:.4f} nats")
print(f"  S64 |beta|^2 (universal) = {beta_sq_univ}")

# ===========================================================================
# Section 2: Construct |beta_k|^2(tau) at 20 Evaluation Points
# ===========================================================================

print("\n" + "=" * 72)
print("SECTION 2: BOGOLIUBOV COEFFICIENT INTERPOLATION")
print("=" * 72)

# The 20 evaluation points span [0, 0.50].
# At tau = 0: BCS ground state, no excitations, |beta_k|^2 = 0.
N_eval = 20
tau_eval = np.linspace(0.0, 0.50, N_eval)

print(f"  Evaluation points: {N_eval}")
print(f"  tau range: [{tau_eval[0]:.3f}, {tau_eval[-1]:.3f}]")
print(f"  tau spacing: {tau_eval[1] - tau_eval[0]:.4f}")

# S57 provides |beta_k|^2 at tau = [0.10, 0.15, 0.19, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5].
# We need to extend to tau = 0 where |beta_k|^2 = 0 (no excitation in BCS ground state).
# The mode-averaged |beta_k|^2 is universal to < 0.001% across 31 modes (S57).
# Use the mode-averaged value for the 8 BCS modes.

beta_sq_avg_57 = np.mean(beta_sq_57, axis=0)  # mean over 31 modes at each tau
alpha_sq_avg_57 = np.mean(alpha_sq_57, axis=0)

# Verify bosonic normalization: |alpha|^2 - |beta|^2 = 1
norm_check = alpha_sq_avg_57 - beta_sq_avg_57
print(f"\n  Bosonic normalization |alpha|^2 - |beta|^2:")
for i, t in enumerate(tau_57):
    print(f"    tau={t:.2f}: |alpha|^2={alpha_sq_avg_57[i]:.6f}, "
          f"|beta|^2={beta_sq_avg_57[i]:.6f}, "
          f"diff={norm_check[i]:.6f}")

# Prepend tau=0 with |beta|^2=0 (BCS ground state, pure, no excitations).
# Also prepend a small value near tau=0 to anchor the interpolation.
tau_extended = np.concatenate([[0.0, 0.05], tau_57])
beta_sq_extended = np.concatenate([[0.0, 0.0], beta_sq_avg_57])

# The S57 data shows beta_sq oscillates at tau=0.35 and 0.45 — this is real
# parametric amplification physics (Bogoliubov coefficients oscillate with
# the relative phase between in/out modes). However, these oscillations are
# artifacts of evaluating at intermediate tau values during an ongoing transit.
# The PHYSICAL observable is the FINAL |beta|^2 after the transit completes.
#
# For GSL purposes, what matters is the ADIABATIC particle number at each tau,
# computed as if the modulus stopped at that tau. The S57 computation does
# exactly this: at each tau checkpoint, it computes the Bogoliubov
# transformation from the initial state to that tau.
#
# The oscillations at intermediate tau are REAL and physical — they reflect
# the coherent quantum oscillations of the squeezed state. The entropy
# computed from these oscillating |beta|^2 values will itself oscillate,
# but must remain non-negative (it always is, by construction of binary entropy).
# The question for GSL is whether dS/dtau >= 0 at all points.

# Use PCHIP (monotone Hermite) interpolation to get smooth curve.
# PCHIP preserves monotonicity in monotone regions and doesn't
# introduce spurious oscillations.
interp_beta_sq = PchipInterpolator(tau_extended, beta_sq_extended)
beta_sq_at_eval = interp_beta_sq(tau_eval)

# Enforce physicality: |beta|^2 >= 0
beta_sq_at_eval = np.maximum(beta_sq_at_eval, 0.0)

print(f"\n  |beta_k|^2 at 20 evaluation points:")
for i, t in enumerate(tau_eval):
    print(f"    tau={t:.4f}: |beta|^2 = {beta_sq_at_eval[i]:.6f}")

# ===========================================================================
# Section 3: Fermionic Occupation and Spectral Entropy
# ===========================================================================

print("\n" + "=" * 72)
print("SECTION 3: SPECTRAL ENTROPY S_spec(tau)")
print("=" * 72)

# Fermionic occupation from bosonic Bogoliubov coefficient:
#   f_n(tau) = |beta_n(tau)|^2 / (1 + |beta_n(tau)|^2)
# This maps |beta|^2 in [0, inf) to f in [0, 1).
# At |beta|^2 = 0: f = 0 (ground state).
# At |beta|^2 = 1: f = 0.5 (maximum entropy per mode).
# At |beta|^2 = 1.015 (S61): f = 0.5037 (near-maximal entropy).

f_at_eval = beta_sq_at_eval / (1.0 + beta_sq_at_eval)

# Binary (fermionic) entropy per mode:
#   s(f) = -[f ln f + (1-f) ln(1-f)]
def binary_entropy_vec(f):
    """Vectorized binary entropy. Safe for f=0 and f=1."""
    result = np.zeros_like(f)
    mask = (f > 1e-15) & (f < 1.0 - 1e-15)
    p = f[mask]
    result[mask] = -(p * np.log(p) + (1.0 - p) * np.log(1.0 - p))
    return result

s_per_mode = binary_entropy_vec(f_at_eval)

# Total spectral entropy: 8 modes, all with same |beta|^2 (universality).
N_modes = 8  # 4 B2 + 1 B1 + 3 B3 (local)
S_spec = N_modes * s_per_mode

print(f"  N_modes = {N_modes} (4 B2 + 1 B1 + 3 B3)")
print(f"  S_max = {N_modes} * ln(2) = {N_modes * np.log(2):.6f} nats\n")

print(f"  {'tau':>8}  {'|beta|^2':>10}  {'f_n':>10}  {'s(f_n)':>10}  {'S_spec':>10}")
print(f"  {'-'*8}  {'-'*10}  {'-'*10}  {'-'*10}  {'-'*10}")
for i in range(N_eval):
    print(f"  {tau_eval[i]:8.4f}  {beta_sq_at_eval[i]:10.6f}  "
          f"{f_at_eval[i]:10.6f}  {s_per_mode[i]:10.6f}  {S_spec[i]:10.6f}")

# ===========================================================================
# Section 4: Compute dS/dtau by Centered Finite Differences
# ===========================================================================

print("\n" + "=" * 72)
print("SECTION 4: dS/dtau BY CENTERED FINITE DIFFERENCES")
print("=" * 72)

# Centered differences for interior points, one-sided at boundaries.
dtau = tau_eval[1] - tau_eval[0]
dS_dtau = np.zeros(N_eval)

# Forward difference at tau=0
dS_dtau[0] = (S_spec[1] - S_spec[0]) / dtau
# Centered differences for interior
for i in range(1, N_eval - 1):
    dS_dtau[i] = (S_spec[i+1] - S_spec[i-1]) / (2.0 * dtau)
# Backward difference at tau=0.5
dS_dtau[-1] = (S_spec[-1] - S_spec[-2]) / dtau

print(f"  dtau = {dtau:.6f}")
print(f"\n  {'tau':>8}  {'S_spec':>10}  {'dS/dtau':>10}  {'dS/dtau >= 0?':>15}")
print(f"  {'-'*8}  {'-'*10}  {'-'*10}  {'-'*15}")

n_violations = 0
for i in range(N_eval):
    ok = dS_dtau[i] >= -1e-12
    flag = "YES" if ok else "*** NO ***"
    if not ok:
        n_violations += 1
    print(f"  {tau_eval[i]:8.4f}  {S_spec[i]:10.6f}  {dS_dtau[i]:10.4f}  {flag:>15}")

# ===========================================================================
# Section 5: Parker Pair Creation Rate dN/dtau
# ===========================================================================

print("\n" + "=" * 72)
print("SECTION 5: PARKER PAIR CREATION RATE dN/dtau")
print("=" * 72)

# Total pair number: N(tau) = sum_n |beta_n(tau)|^2 = N_modes * |beta|^2(tau)
# (universal across modes).
N_pairs_at_eval = N_modes * beta_sq_at_eval

# dN/dtau by centered finite differences
dN_dtau = np.zeros(N_eval)
dN_dtau[0] = (N_pairs_at_eval[1] - N_pairs_at_eval[0]) / dtau
for i in range(1, N_eval - 1):
    dN_dtau[i] = (N_pairs_at_eval[i+1] - N_pairs_at_eval[i-1]) / (2.0 * dtau)
dN_dtau[-1] = (N_pairs_at_eval[-1] - N_pairs_at_eval[-2]) / dtau

# Cross-check: dS/dtau should be approximately dN/dtau * ln(2) when f ~ 1/2.
# More precisely: dS/dtau = sum_n ds(f_n)/dtau = sum_n s'(f_n) * df_n/dtau
# where s'(f) = ln((1-f)/f) and df_n/dtau = d|beta_n|^2/dtau / (1+|beta_n|^2)^2.
#
# For the ratio:
#   dS/dtau / dN/dtau = <s'(f)> * <df/dtau> / <d|beta|^2/dtau>
# When f ~ 1/2 (|beta|^2 ~ 1): s'(1/2) = 0, so the ratio goes through zero!
# When f << 1 (early transit): s'(f) ~ -ln(f) ~ ln(1/f), large.
# When f >> 1/2: s'(f) ~ ln(1/f - 1), negative if f > 1/2.
#
# The correct comparison: at early times (f << 1),
#   dS/dN ~ s(f)/f ~ -ln(f) -> infinity (each new pair contributes lots of entropy).
# At late times near f = 1/2:
#   dS/dN ~ 0 (entropy saturated, new pairs don't add entropy).
# The ~ln(2) per pair estimate is only valid at f = 1/2 for a single jump.

# Instead compute the analytic derivative ds/df and the chain rule:
# ds/dtau = ds/df * df/d(beta^2) * d(beta^2)/dtau
# where df/d(beta^2) = 1/(1+beta^2)^2

# Derivative of binary entropy: s'(f) = ln((1-f)/f)
s_prime = np.zeros(N_eval)
mask = (f_at_eval > 1e-15) & (f_at_eval < 1.0 - 1e-15)
s_prime[mask] = np.log((1.0 - f_at_eval[mask]) / f_at_eval[mask])

# df/d(beta^2) = 1/(1+beta^2)^2
df_dbeta2 = 1.0 / (1.0 + beta_sq_at_eval)**2

# d(beta^2)/dtau from finite differences of the interpolated curve
dbeta2_dtau = np.zeros(N_eval)
dbeta2_dtau[0] = (beta_sq_at_eval[1] - beta_sq_at_eval[0]) / dtau
for i in range(1, N_eval - 1):
    dbeta2_dtau[i] = (beta_sq_at_eval[i+1] - beta_sq_at_eval[i-1]) / (2.0 * dtau)
dbeta2_dtau[-1] = (beta_sq_at_eval[-1] - beta_sq_at_eval[-2]) / dtau

# Analytic dS/dtau (chain rule): should match numerical dS/dtau
dS_dtau_analytic = N_modes * s_prime * df_dbeta2 * dbeta2_dtau

print(f"  Pair creation comparison:")
print(f"  {'tau':>8}  {'N_pairs':>10}  {'dN/dtau':>10}  {'dS/dtau_num':>12}  "
      f"{'dS/dtau_ana':>12}  {'ratio':>8}")
print(f"  {'-'*8}  {'-'*10}  {'-'*10}  {'-'*12}  {'-'*12}  {'-'*8}")
for i in range(N_eval):
    ratio = dS_dtau[i] / dN_dtau[i] if abs(dN_dtau[i]) > 1e-15 else np.nan
    print(f"  {tau_eval[i]:8.4f}  {N_pairs_at_eval[i]:10.4f}  {dN_dtau[i]:10.4f}  "
          f"{dS_dtau[i]:12.4f}  {dS_dtau_analytic[i]:12.4f}  {ratio:8.4f}")

# Check consistency between numerical and analytic dS/dtau
mask_nz = np.abs(dS_dtau) > 1e-10
if np.any(mask_nz):
    rel_err = np.abs(dS_dtau[mask_nz] - dS_dtau_analytic[mask_nz]) / np.abs(dS_dtau[mask_nz])
    print(f"\n  Numerical vs analytic dS/dtau agreement:")
    print(f"    Max relative error: {np.max(rel_err):.2e}")
    print(f"    Mean relative error: {np.mean(rel_err):.2e}")

# ===========================================================================
# Section 6: Cross-Check Against S64 Discrete Stages
# ===========================================================================

print("\n" + "=" * 72)
print("SECTION 6: CROSS-CHECK AGAINST S64 DISCRETE STAGES")
print("=" * 72)

# S64 values:
#   BCS (tau < fold): S = 0
#   Transit (at fold): S_transit = 5.545 nats (entanglement; N_modes * s(0.5037))
#   GGE: S_GGE = 2.212 nats
#   Gibbs: S_Gibbs = 4.645 nats

# Our continuous trajectory at key points:
# tau=0 -> S should be 0 (BCS)
# tau=0.19 (fold) -> S should match transit occupation
# tau=0.50 (final) -> S should match transit at |beta|^2=1.015

# Find nearest tau to fold
idx_fold = np.argmin(np.abs(tau_eval - tau_fold))
idx_final = N_eval - 1

# S64 transit entropy (universal p_transit = 0.5037)
p_transit_s64 = beta_sq_univ / (1.0 + beta_sq_univ)
s_transit_s64 = -(p_transit_s64 * np.log(p_transit_s64) +
                  (1.0 - p_transit_s64) * np.log(1.0 - p_transit_s64))
S_transit_s64 = N_modes * s_transit_s64

print(f"  tau = 0.00: S_spec = {S_spec[0]:.6f} nats (should be 0)")
print(f"  tau = {tau_eval[idx_fold]:.2f} (near fold): S_spec = {S_spec[idx_fold]:.6f} nats")
print(f"  tau = 0.50 (final):  S_spec = {S_spec[idx_final]:.6f} nats")
print(f"\n  S64 transit entropy (at |beta|^2=1.015): {S_transit_s64:.6f} nats")
print(f"  S64 S_GGE (diagonal ensemble):            {S_GGE_S64:.6f} nats")
print(f"\n  Note: S_spec at tau=0.50 uses interpolated |beta|^2 = {beta_sq_at_eval[-1]:.6f}")
print(f"  S57 final |beta|^2 = {float(np.mean(beta_sq_57[:,-1])):.6f}")

# The S64 S_GGE is computed from the GGE Lagrange multipliers (lambda_k),
# NOT from |beta_k|^2. The two are distinct: the Bogoliubov entropy counts
# entanglement across the transit, while the GGE entropy counts the diagonal
# ensemble entropy. For a single mode, they coincide, but for the
# multi-mode system with different lambda_k per sector, the GGE entropy
# is LOWER than the transit entropy because conservation laws constrain
# the ensemble.

# ===========================================================================
# Section 7: GSL Gate Verdict
# ===========================================================================

print("\n" + "=" * 72)
print("SECTION 7: GATE VERDICT — GSL-CONTINUOUS-65")
print("=" * 72)

# Pre-registered criterion: dS/dtau >= 0 at all 20 tau values.
# Use a small negative threshold to account for numerical noise.
threshold = -1e-10  # (local)
violations = np.where(dS_dtau < threshold)[0]

gate_pass = len(violations) == 0

print(f"  Gate: GSL-CONTINUOUS-65")
print(f"  Criterion: dS/dtau >= 0 at all {N_eval} tau values")
print(f"  Threshold for violation: dS/dtau < {threshold:.1e}")
print(f"  Number of violations: {len(violations)}")

if len(violations) > 0:
    print(f"  Violations at tau values:")
    for v in violations:
        print(f"    tau = {tau_eval[v]:.4f}: dS/dtau = {dS_dtau[v]:.6e}")
    print(f"\n  VERDICT: FAIL")
    print(f"  GSL violated at {len(violations)} of {N_eval} evaluation points.")
else:
    print(f"\n  VERDICT: PASS")
    print(f"  dS/dtau >= 0 at all {N_eval} evaluation points.")
    print(f"  The generalized second law is satisfied continuously through the transit.")

# Additional diagnostics
print(f"\n  Entropy trajectory summary:")
print(f"    S_spec(tau=0)    = {S_spec[0]:.6f} nats (BCS ground state)")
print(f"    S_spec(tau=0.19) = {S_spec[idx_fold]:.6f} nats (at fold)")
print(f"    S_spec(tau=0.50) = {S_spec[-1]:.6f} nats (full transit)")
print(f"    S_max            = {N_modes * np.log(2):.6f} nats (= 8*ln(2))")
print(f"    Saturation at final: {S_spec[-1] / (N_modes * np.log(2)) * 100:.2f}%")
print(f"\n  dS/dtau range: [{np.min(dS_dtau):.4f}, {np.max(dS_dtau):.4f}] nats/tau")
print(f"  Peak dS/dtau at tau = {tau_eval[np.argmax(dS_dtau)]:.4f}")

# Consistency check: S monotone
S_monotone = all(S_spec[i+1] >= S_spec[i] - 1e-12 for i in range(N_eval - 1))
print(f"\n  S_spec monotonically non-decreasing: {S_monotone}")

# ===========================================================================
# Section 8: Save Data
# ===========================================================================

print("\n" + "=" * 72)
print("SECTION 8: SAVE DATA")
print("=" * 72)

output_path = data_dir / 's65_gsl_continuous.npz'
np.savez(output_path,
    # Evaluation grid
    tau_eval=tau_eval,
    N_eval=N_eval,
    # Bogoliubov coefficients
    beta_sq_at_eval=beta_sq_at_eval,
    f_at_eval=f_at_eval,
    # Entropy
    S_spec=S_spec,
    s_per_mode=s_per_mode,
    S_max=N_modes * np.log(2),
    # Derivatives
    dS_dtau=dS_dtau,
    dS_dtau_analytic=dS_dtau_analytic,
    # Parker pair creation
    N_pairs_at_eval=N_pairs_at_eval,
    dN_dtau=dN_dtau,
    # Chain rule components
    s_prime=s_prime,
    df_dbeta2=df_dbeta2,
    dbeta2_dtau=dbeta2_dtau,
    # Cross-checks
    S_transit_s64=S_transit_s64,
    S_GGE_s64=S_GGE_S64,
    beta_sq_univ=beta_sq_univ,
    # Gate
    gate_name='GSL-CONTINUOUS-65',
    gate_pass=gate_pass,
    n_violations=len(violations),
    S_monotone=S_monotone,
    # Input provenance
    tau_57=tau_57,
    beta_sq_avg_57=beta_sq_avg_57,
)
print(f"  Data saved to: {output_path}")

# ===========================================================================
# Section 9: Plot
# ===========================================================================

print("\n" + "=" * 72)
print("SECTION 9: PLOT")
print("=" * 72)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('GSL-CONTINUOUS-65: Continuous Entropy Through Transit\n'
             r'$S_{\rm spec}(\tau) = 8 \times [-f\ln f - (1-f)\ln(1-f)]$, '
             r'$f = |\beta|^2/(1+|\beta|^2)$',
             fontsize=12, fontweight='bold')

# Colors
C_BLUE = '#2166ac'
C_RED = '#b2182b'
C_GREEN = '#1b7837'
C_ORANGE = '#e08214'
C_GRAY = '#666666'

# --- Panel (a): S_spec(tau) continuous trajectory ---
ax = axes[0, 0]
ax.plot(tau_eval, S_spec, 'o-', color=C_BLUE, linewidth=2, markersize=5,
        label=r'$S_{\rm spec}(\tau)$')

# Mark key points
ax.axvline(x=tau_fold, color=C_RED, linestyle='--', alpha=0.5,
           label=f'Fold ($\\tau={tau_fold}$)')
ax.axhline(y=N_modes * np.log(2), color=C_GRAY, linestyle=':', alpha=0.5,
           label=r'$S_{\rm max} = 8\ln 2$')
ax.axhline(y=S_GGE_S64, color=C_GREEN, linestyle=':', alpha=0.5,
           label=f'$S_{{GGE}}$ = {S_GGE_S64:.2f}')

# S57 data points for comparison
f_57 = beta_sq_avg_57 / (1.0 + beta_sq_avg_57)
s_57 = binary_entropy_vec(f_57)
S_57 = N_modes * s_57
ax.scatter(tau_57, S_57, marker='x', s=60, color=C_ORANGE, zorder=5,
           label='S57 data (direct)')

ax.set_xlabel(r'$\tau$', fontsize=12)
ax.set_ylabel(r'$S_{\rm spec}$ (nats)', fontsize=12)
ax.set_title('(a) Spectral Entropy Trajectory', fontsize=11)
ax.legend(fontsize=8, loc='upper left')
ax.set_xlim(-0.02, 0.52)
ax.set_ylim(-0.2, N_modes * np.log(2) * 1.15)

verdict_text = 'PASS' if gate_pass else 'FAIL'
verdict_color = 'lightgreen' if gate_pass else '#ffcccc'
ax.text(0.97, 0.03, f'Gate: {verdict_text}',
        transform=ax.transAxes, fontsize=10, ha='right', va='bottom',
        bbox=dict(boxstyle='round', facecolor=verdict_color, alpha=0.8))

# --- Panel (b): dS/dtau ---
ax = axes[0, 1]
ax.plot(tau_eval, dS_dtau, 's-', color=C_RED, linewidth=2, markersize=5,
        label=r'$dS/d\tau$ (numerical)')
ax.plot(tau_eval, dS_dtau_analytic, '--', color=C_ORANGE, linewidth=1.5,
        label=r'$dS/d\tau$ (chain rule)')
ax.axhline(y=0, color='black', linewidth=0.5)
ax.axvline(x=tau_fold, color=C_RED, linestyle='--', alpha=0.3)

ax.set_xlabel(r'$\tau$', fontsize=12)
ax.set_ylabel(r'$dS/d\tau$ (nats)', fontsize=12)
ax.set_title('(b) Entropy Production Rate', fontsize=11)
ax.legend(fontsize=9)
ax.set_xlim(-0.02, 0.52)

# Highlight any violations
if len(violations) > 0:
    ax.scatter(tau_eval[violations], dS_dtau[violations],
               marker='X', s=100, c='red', zorder=10, label='VIOLATION')
    ax.legend(fontsize=9)

gsl_label = r'$dS/d\tau \geq 0$: ' + ('YES' if gate_pass else 'NO')
ax.text(0.97, 0.97, gsl_label, transform=ax.transAxes, fontsize=10,
        ha='right', va='top',
        bbox=dict(boxstyle='round',
                  facecolor='lightgreen' if gate_pass else '#ffcccc', alpha=0.8))

# --- Panel (c): |beta|^2 and f_n ---
ax = axes[1, 0]
ax2 = ax.twinx()

l1, = ax.plot(tau_eval, beta_sq_at_eval, 'o-', color=C_BLUE, linewidth=2,
              markersize=5, label=r'$|\beta|^2(\tau)$')
l2, = ax2.plot(tau_eval, f_at_eval, 's-', color=C_GREEN, linewidth=2,
               markersize=4, label=r'$f_n(\tau)$')

# S57 raw data
ax.scatter(tau_57, beta_sq_avg_57, marker='x', s=60, color=C_ORANGE, zorder=5,
           label='S57 data')
ax.axvline(x=tau_fold, color=C_RED, linestyle='--', alpha=0.3)
ax.axhline(y=1.0, color=C_GRAY, linestyle=':', alpha=0.3)
ax2.axhline(y=0.5, color=C_GRAY, linestyle=':', alpha=0.3)

ax.set_xlabel(r'$\tau$', fontsize=12)
ax.set_ylabel(r'$|\beta|^2$', fontsize=12, color=C_BLUE)
ax2.set_ylabel(r'$f_n = |\beta|^2/(1+|\beta|^2)$', fontsize=12, color=C_GREEN)
ax.set_title('(c) Bogoliubov Coefficients', fontsize=11)

lines = [l1, l2]
labels = [l.get_label() for l in lines]
ax.legend(lines, labels, fontsize=9, loc='upper left')

# --- Panel (d): dN/dtau vs dS/dtau ---
ax = axes[1, 1]
ax.plot(tau_eval, dN_dtau, 'D-', color=C_BLUE, linewidth=2, markersize=4,
        label=r'$dN/d\tau$ (pair creation rate)')
ax.plot(tau_eval, dS_dtau, 's-', color=C_RED, linewidth=2, markersize=4,
        label=r'$dS/d\tau$ (entropy rate)')
ax.axhline(y=0, color='black', linewidth=0.5)
ax.axvline(x=tau_fold, color=C_RED, linestyle='--', alpha=0.3)

ax.set_xlabel(r'$\tau$', fontsize=12)
ax.set_ylabel('Rate', fontsize=12)
ax.set_title('(d) Parker Rate vs Entropy Rate', fontsize=11)
ax.legend(fontsize=9)

plt.tight_layout(rect=[0, 0, 1, 0.92])
plot_path = data_dir / 's65_gsl_continuous.png'
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
print(f"  Plot saved to: {plot_path}")

print("\n" + "=" * 72)
print("COMPUTATION COMPLETE")
print("=" * 72)
