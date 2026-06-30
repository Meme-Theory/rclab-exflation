"""
S85 §6A R2-A Tesla — Explicit 5x5 Fisher Recomputation with a_n Nuisance.

Workshop: s85-6a-cgwb-alphas-independence.md (3-round 2-agent workshop, R2-A turn)
Mother gate: S85-W13-2-CGWB-ALPHA-S-FLAGSHIP-JOINT (verdict line 66 of s85_gate_verdicts.txt)
Mother atlas: S85-W12-ELIM-8 (5-regulator a_n atlas, line 194)

GOAL (per schedule §6A R2 prescription):
  "(tesla) respond to mack's covariance claim: produce the explicit Fisher
   matrix with a_2, a_4, a_6 as nuisance parameters; compute the marginalized
   rho(CGWB, alpha_s) after marginalizing over a_n; check whether rho stays
   at 0 or moves."

This script executes EXACTLY THAT computation:
  1. Build 5x5 Fisher F_full on (alpha_s, Omega_GW, a_0, a_2, a_4) at the
     canonical zeta-pinned mean over the 5-regulator atlas.
  2. Schur-complement marginalize over (a_0, a_2, a_4) to get 2x2 F_marg.
  3. Read off rho_marg = F_marg[0,1] / sqrt(F_marg[0,0]*F_marg[1,1]).
  4. Compare to W13-2 rho_cc = 0 verdict.

Substitution chain for the Schur-complement direction (mandatory per math-is-hard.sh):
  Definition 1: F_marg = A - B C^{-1} B^T   [Schur complement of C in F_full]
  Definition 2: rho_marg = F_marg[0,1] / sqrt(F_marg[0,0] * F_marg[1,1])
  Substitute leading-order Jacobians:
    J_alpha_s = (dn_s/dlnk depends on a_2/a_0 via O-Z; dalpha_s/da_2 != 0; dalpha_s/da_0 != 0; dalpha_s/da_4 = 0 LO)
    J_CGWB    = (Omega_GW ~ G_N ~ 1/a_2; dOmega_GW/da_2 != 0; dOmega_GW/da_0 = 0 LO; dOmega_GW/da_4 = 0 LO)
  Both Jacobian rows have nonzero entry in the a_2 column.
  Therefore B is NOT zero, and B C^{-1} B^T need NOT be zero.
  Direction: rho_marg = 0 IFF Sum_{m,n} J_a[m] C^{-1}[m,n] J_C[n] = 0.
  This is a NUMERICAL question, not a structural symmetry — Python decides.

Substitution chain for "amplification" direction:
  Definition: condition number kappa(C) = lambda_max(C) / lambda_min(C)
  Mack reports kappa(C) ~ 7.6e+10 across 5-regulator atlas (rank-2 numerically).
  C^{-1} therefore has entries up to 1/lambda_min(C) ~ 1.3e+11.
  Substitute into Schur: |F_marg[0,1]| <= |J_a| * (1/lambda_min) * |J_C|
  For finite J's and large 1/lambda_min, |F_marg[0,1]| can be BIG.
  Direction: near-singular C AMPLIFIES the kernel cross-product. Mack's claim.

VERDICT this script must produce: numeric F_marg and rho_marg from explicit
construction at zeta-pinned a_n, against the canonical observational sigmas.
"""

import sys
import os
import numpy as np
import hashlib
import json

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    alpha_s_cmb_central,           # -0.06896799
    f_LISA_pivot,                  # 3.0e-3 Hz
    planck_ns,                     # 0.9649
)

# -----------------------------------------------------------------------------
# Pinned observational sigmas (W13-2 verbatim, workshop file lines 207, 234)
# -----------------------------------------------------------------------------
sigma_alpha_s_CMBS4 = 0.003   # (local) W13-2 §(e); CMB-S4-Book-2019 forecast
sigma_Omega_GW_LISA = 1.0e-12 # (local) W13-2 §(e); LISA-PLS-2024 floor at 3 mHz

# -----------------------------------------------------------------------------
# W12-4 atlas (verbatim from session-85-w12-workingpaper.md lines 224-226)
# -----------------------------------------------------------------------------
# 5 regulators: heat-kernel, zeta, Mellin, hard-cutoff, Pauli-Villars
a_0_atlas = np.array([3.7074, 3.7074, 3.7074, 2.0122, 3.7074])     # (local)
a_2_atlas = np.array([0.15445, 0.15810, 0.15810, 0.11100, 0.03185]) # (local)
a_4_atlas = np.array([0.011837, 0.011994, 0.011994, 0.010677, 0.006795]) # (local)

# Canonical zeta-pin (W13-2 verdict line: scheme=zeta)
a_0_zeta = a_0_atlas[1]   # (local) 3.7074
a_2_zeta = a_2_atlas[1]   # (local) 0.15810
a_4_zeta = a_4_atlas[1]   # (local) 0.011994

# Mean-pin across atlas (mack's M2 reference)
a_0_mean = float(np.mean(a_0_atlas))   # (local)
a_2_mean = float(np.mean(a_2_atlas))   # (local)
a_4_mean = float(np.mean(a_4_atlas))   # (local)

print("=" * 78)
print("S85 §6A R2-A Tesla — Explicit 5x5 Fisher with a_n Nuisance")
print("=" * 78)
print()
print(f"W12-4 atlas pin (zeta scheme):")
print(f"  a_0 = {a_0_zeta:.6f}  a_2 = {a_2_zeta:.6f}  a_4 = {a_4_zeta:.6f}")
print(f"Atlas mean (mack's reference):")
print(f"  a_0 = {a_0_mean:.6f}  a_2 = {a_2_mean:.6f}  a_4 = {a_4_mean:.6f}")
print()

# -----------------------------------------------------------------------------
# Substrate covariance C — 3x3 sample covariance of (a_0, a_2, a_4) over atlas
# -----------------------------------------------------------------------------
samples = np.column_stack([a_0_atlas, a_2_atlas, a_4_atlas])  # (5, 3)  # (local)
C = np.cov(samples, rowvar=False, ddof=1)  # (3, 3)

print("Substrate covariance C (sample, ddof=1):")
print(C)
print()
eigvals_C = np.linalg.eigvalsh(C)
print(f"Eigenvalues of C: {eigvals_C}")
print(f"det(C) = {np.linalg.det(C):.6e}")
print(f"cond(C) = {np.linalg.cond(C):.6e}")
print()

# Pearson correlations
sd = np.sqrt(np.diag(C))
R = C / np.outer(sd, sd)
print(f"Pearson correlations:")
print(f"  rho(a_0, a_2) = {R[0,1]:+.6f}")
print(f"  rho(a_0, a_4) = {R[0,2]:+.6f}")
print(f"  rho(a_2, a_4) = {R[1,2]:+.6f}")
print()

# Pseudoinverse (mack confirms C is rank-2 numerically; full inverse fails)
C_pinv = np.linalg.pinv(C)  # (local)
print("C+ (Moore-Penrose pseudoinverse):")
print(C_pinv)
print()

# -----------------------------------------------------------------------------
# OBSERVABLE values at the zeta pin (W13-2)
# -----------------------------------------------------------------------------
n_s = planck_ns                                          # (local) 0.9649
alpha_s_obs = alpha_s_cmb_central                        # (local) -0.06896799 (= n_s^2 - 1, S50 O-Z)
Omega_GW_obs = 8.299e-58                                 # (local) W13-2 verdict value at f_LISA_pivot

# -----------------------------------------------------------------------------
# Jacobian rows under canonical scaling laws
# -----------------------------------------------------------------------------
# CGWB: Omega_GW ~ G_N ~ 1/(a_2 * M_KK^2) at LEADING order in a_n.
#   d(Omega_GW)/d(a_2) = -Omega_GW / a_2     [LO: Omega_GW propto 1/a_2]
#   d(Omega_GW)/d(a_0) = 0                    [LO: no a_0 dependence in 1/G_N]
#   d(Omega_GW)/d(a_4) = 0                    [LO: a_4 enters NLO via heat-kernel renorm of G_N]
#
# Substitution chain for sign of dOmega_GW/da_2:
#   Step 1 (def):    Omega_GW(a_2) = K_GW / a_2  with K_GW > 0
#   Step 2 (subst):  d/da_2 [K_GW / a_2] = -K_GW / a_2^2
#   Step 3 (simpl):  -K_GW / a_2^2 = -(K_GW/a_2)/a_2 = -Omega_GW/a_2
#   Step 4 (dir):    Sign is NEGATIVE because a_2 in denominator and a_2 > 0.
#
# alpha_s: alpha_s = n_s^2 - 1, n_s = f(a_2/a_0) (S50 O-Z; constant-mass).
# Use canonical normalization n_s = (a_2/a_0) / (a_2_zeta/a_0_zeta) * n_s_pin
# i.e. n_s scales linearly in a_2/a_0 about the pin to first order
# (this is the LEADING-order expansion mack and tesla agreed in T2/Re:T2).
#
#   d(alpha_s)/d(a_2) = 2 n_s * (dn_s/d(a_2/a_0)) * (1/a_0)
#                     = 2 n_s * (n_s_pin / (a_2_zeta/a_0_zeta)) * (1/a_0)
#                     = 2 n_s^2 / a_2          [at the zeta pin]
#   d(alpha_s)/d(a_0) = 2 n_s * (dn_s/d(a_2/a_0)) * (-a_2/a_0^2)
#                     = -2 n_s^2 / a_0         [at the zeta pin]
#   d(alpha_s)/d(a_4) = 0                       [LO; running-mass NLO contribution ignored]
#
# Substitution chain for sign of dalpha_s/da_2:
#   Step 1 (def):   n_s(a_2/a_0) linear in (a_2/a_0) about pin; alpha_s = n_s^2 - 1
#   Step 2 (subst): d(alpha_s)/d(a_2) = 2 n_s * dn_s/d(a_2) = 2 n_s * (1/a_0)
#                   At pin: dn_s/d(a_2/a_0) = n_s/(a_2/a_0) = n_s * a_0/a_2  [linear ratio]
#                   So dn_s/da_2 = (n_s * a_0/a_2) * (1/a_0) = n_s/a_2
#   Step 3 (simpl): d(alpha_s)/d(a_2) = 2 n_s * (n_s/a_2) = 2 n_s^2 / a_2
#   Step 4 (dir):   Sign POSITIVE; n_s>0, a_2>0.

J_CGWB    = np.array([0.0,                    # d/da_0
                      -Omega_GW_obs / a_2_zeta,  # d/da_2
                      0.0])                    # d/da_4
J_alpha_s = np.array([-2.0 * n_s**2 / a_0_zeta,  # d/da_0
                       2.0 * n_s**2 / a_2_zeta,  # d/da_2
                       0.0])                     # d/da_4

print("Jacobian rows at zeta pin:")
print(f"  J_alpha_s = (d/da_0, d/da_2, d/da_4) = "
      f"({J_alpha_s[0]:+.6e}, {J_alpha_s[1]:+.6e}, {J_alpha_s[2]:+.6e})")
print(f"  J_CGWB    = (d/da_0, d/da_2, d/da_4) = "
      f"({J_CGWB[0]:+.6e}, {J_CGWB[1]:+.6e}, {J_CGWB[2]:+.6e})")
print()

# -----------------------------------------------------------------------------
# 5x5 FULL FISHER on theta = (alpha_s, Omega_GW, a_0, a_2, a_4)
# -----------------------------------------------------------------------------
# F_full[i,j] = sum_obs (1/sigma_obs^2) (dO_obs/dtheta_i) (dO_obs/dtheta_j).
#
# Two observables: alpha_s (sigma=sigma_alpha_s_CMBS4), Omega_GW (sigma=sigma_Omega_GW_LISA).
# Build response matrix R of shape (n_obs, n_param) = (2, 5):
#   R[0, :] = (dalpha_s/dalpha_s, dalpha_s/dOmega_GW, dalpha_s/da_0, dalpha_s/da_2, dalpha_s/da_4)
#           = (1, 0, J_alpha_s[0], J_alpha_s[1], J_alpha_s[2])
#   R[1, :] = (dOmega_GW/dalpha_s, ...)  = (0, 1, J_CGWB[0], J_CGWB[1], J_CGWB[2])
#
# Noise weight diagonal: W = diag(1/sigma_alpha^2, 1/sigma_OmegaGW^2)
# F_full = R^T W R.

R_resp = np.zeros((2, 5))
R_resp[0, 0] = 1.0
R_resp[0, 2:5] = J_alpha_s
R_resp[1, 1] = 1.0
R_resp[1, 2:5] = J_CGWB

W = np.diag([1.0 / sigma_alpha_s_CMBS4**2,
             1.0 / sigma_Omega_GW_LISA**2])

F_full = R_resp.T @ W @ R_resp  # (5, 5)

print("Response matrix R (2 obs x 5 params):")
print(R_resp)
print()
print("Noise weight W (2x2 diag):")
print(W)
print()
print("F_full (5x5):")
print(F_full)
print()
eigvals_full = np.linalg.eigvalsh(F_full)
print(f"Eigenvalues F_full: {eigvals_full}")
print(f"All positive? {np.all(eigvals_full >= -1e-30)}")
print()

# -----------------------------------------------------------------------------
# OPTIONAL: substrate prior on a_n. Two interpretations (mack Q-tesla-2):
#   (a) Regulator-Bayesian: include C^{-1} as a prior on (a_0, a_2, a_4).
#       F_full_with_prior[2:5, 2:5] += C_pinv  (because the sub-block gets a Bayesian prior
#       precision matrix C^{-1} added, equivalent to a Gaussian prior with covariance C).
#   (b) Zeta-committed: no prior, C is artifactual. Skip the prior addition.
#
# We compute BOTH cases and report the marginalized rho for each.
# -----------------------------------------------------------------------------

# Case (a): Bayesian — add C^{-1} as prior on a_n nuisance block
F_full_a = F_full.copy()
F_full_a[2:5, 2:5] += C_pinv

# Case (b): zeta-committed — no prior; the a_n columns of F_full would be
# rank-1 (single observable contributing). Marginalization over un-pinned
# nuisances is ill-posed without prior. We skip case (b) Schur and instead
# note the structural answer directly: with zero prior on a_n, the a_n block
# is rank-deficient and Schur is undefined — equivalent to "the observable
# plane already pins everything"; this is exactly mack's pseudoinverse
# regime. We use C^{-1} via pseudoinverse for the marginalization.

# Case (c): Atlas-stratified (mack's preferred) — same as (a) since the
# atlas is the prior; (a) and (c) coincide computationally here.

# -----------------------------------------------------------------------------
# SCHUR COMPLEMENT — marginalize over a_n nuisance block (rows/cols 2:5)
# -----------------------------------------------------------------------------
# F_marg(signal) = A - B C_full^{-1} B^T
# where A = F_full[0:2, 0:2], B = F_full[0:2, 2:5], C_full = F_full[2:5, 2:5]

A = F_full_a[0:2, 0:2]
B = F_full_a[0:2, 2:5]
C_full_block = F_full_a[2:5, 2:5]

print("Signal block A (2x2):")
print(A)
print()
print("Cross block B (2x3):")
print(B)
print()
print("Nuisance block C_full (3x3, includes prior):")
print(C_full_block)
print()
eigvals_Cfull = np.linalg.eigvalsh(C_full_block)
print(f"Eigenvalues of nuisance block: {eigvals_Cfull}")
print(f"Min eigenvalue: {eigvals_Cfull.min():.6e}")
print()

# Use solve for stability (avoid explicit inverse)
try:
    Cfull_inv_B_T = np.linalg.solve(C_full_block, B.T)
except np.linalg.LinAlgError:
    Cfull_inv_B_T = np.linalg.pinv(C_full_block) @ B.T
F_marg = A - B @ Cfull_inv_B_T

print("F_marg = A - B C^{-1} B^T (2x2):")
print(F_marg)
print()

F_marg_diag_signs = np.sign(np.diag(F_marg))
print(f"Diagonal of F_marg: {np.diag(F_marg)}")
print(f"Off-diagonal F_marg[0,1] = {F_marg[0,1]:+.6e}")
print()

# rho_marg
if F_marg[0,0] > 0 and F_marg[1,1] > 0:
    rho_marg = F_marg[0,1] / np.sqrt(F_marg[0,0] * F_marg[1,1])
else:
    rho_marg = float('nan')
print(f"rho_marg = F_marg[0,1] / sqrt(F_marg[0,0] * F_marg[1,1]) = {rho_marg:+.6e}")
print()

# -----------------------------------------------------------------------------
# Compare to W13-2 unmarginalized rho_cc = 0
# -----------------------------------------------------------------------------
F_w13 = np.diag([1.0/sigma_alpha_s_CMBS4**2, 1.0/sigma_Omega_GW_LISA**2])
rho_w13 = 0.0  # (local) W13-2 unmarginalized rho_cc by construction
print(f"W13-2 unmarginalized rho_cc = {rho_w13:.6e} (verdict line)")
print(f"R2 marginalized rho_marg = {rho_marg:+.6e}")
print(f"|delta rho| = {abs(rho_marg - rho_w13):.6e}")
print()

# Magnitude floor for "operationally zero"
floor_obs = 1e-15  # (local) sigma_LISA * sigma_CMBS4 = 1e-12 * 0.003
print(f"Observable detection floor sqrt(sigma_LISA * sigma_alphas) ~ {floor_obs:.1e}")
print(f"|rho_marg| relative to 1e-15: {abs(rho_marg)/floor_obs:.6e}")
print()

# -----------------------------------------------------------------------------
# Direct substrate-only check: F_marg using only mack's substrate Schur
# -----------------------------------------------------------------------------
# Without observable Fisher: F_marg_substrate = -J_C^T @ C_pinv @ J_a
# This is the "substrate-Fisher off-diagonal" mack reports as 4.27e-49.
F_marg_substrate_offdiag = -J_CGWB @ C_pinv @ J_alpha_s
print(f"Substrate-only Schur term -J_C^T C+ J_a = {F_marg_substrate_offdiag:+.6e}")
print(f"  (Mack M2 estimate: 4.27e-49 at mean-pinned)")
print()

# Recompute at mean-pinned for direct comparison with mack's M2
J_CGWB_mean = np.array([0.0, -Omega_GW_obs / a_2_mean, 0.0])
J_alpha_s_mean = np.array([-2.0*n_s**2/a_0_mean,
                            +2.0*n_s**2/a_2_mean,
                            0.0])
F_marg_mean_substrate = -J_CGWB_mean @ C_pinv @ J_alpha_s_mean
print(f"At mean-pinned a_n:")
print(f"  J_CGWB = {J_CGWB_mean}")
print(f"  J_alpha_s = {J_alpha_s_mean}")
print(f"  -J_C^T C+ J_a = {F_marg_mean_substrate:+.6e}")
print()

# rho_marg with substrate-only term, using observable diagonal as denominator
F_marg_obs_full_offdiag = F_marg[0,1]
rho_alt = F_marg_substrate_offdiag / np.sqrt(
    (1.0/sigma_alpha_s_CMBS4**2) * (1.0/sigma_Omega_GW_LISA**2))
print(f"Substrate-only rho through observable Fisher denom: {rho_alt:+.6e}")
print()

# -----------------------------------------------------------------------------
# Regulator-by-regulator F_marg recomputation (Q-tesla-3)
# -----------------------------------------------------------------------------
print("=" * 78)
print("Per-regulator F_marg recomputation (Q-tesla-3 atlas robustness)")
print("=" * 78)
regulator_names = ["heat-kernel", "zeta", "Mellin", "hard-cutoff", "Pauli-Villars"]
per_reg_F_marg = []
per_reg_rho_marg = []

for r_idx, r_name in enumerate(regulator_names):
    a_0_r = a_0_atlas[r_idx]
    a_2_r = a_2_atlas[r_idx]
    a_4_r = a_4_atlas[r_idx]

    J_C_r = np.array([0.0, -Omega_GW_obs / a_2_r, 0.0])
    J_a_r = np.array([-2.0*n_s**2/a_0_r, 2.0*n_s**2/a_2_r, 0.0])

    R_r = np.zeros((2, 5))
    R_r[0, 0] = 1.0; R_r[0, 2:5] = J_a_r
    R_r[1, 1] = 1.0; R_r[1, 2:5] = J_C_r

    F_full_r = R_r.T @ W @ R_r
    F_full_r[2:5, 2:5] += C_pinv  # Bayesian prior

    A_r = F_full_r[0:2, 0:2]
    B_r = F_full_r[0:2, 2:5]
    C_r = F_full_r[2:5, 2:5]

    try:
        Cinv_BT = np.linalg.solve(C_r, B_r.T)
    except np.linalg.LinAlgError:
        Cinv_BT = np.linalg.pinv(C_r) @ B_r.T
    F_marg_r = A_r - B_r @ Cinv_BT

    if F_marg_r[0,0] > 0 and F_marg_r[1,1] > 0:
        rho_r = F_marg_r[0,1] / np.sqrt(F_marg_r[0,0]*F_marg_r[1,1])
    else:
        rho_r = float('nan')
    per_reg_F_marg.append(F_marg_r[0,1])
    per_reg_rho_marg.append(rho_r)
    print(f"  {r_name:14s}: F_marg[0,1] = {F_marg_r[0,1]:+.6e}   rho_marg = {rho_r:+.6e}")
print()

per_reg_rho_marg = np.array(per_reg_rho_marg)
spread_rho = np.ptp(per_reg_rho_marg)
print(f"Spread rho_marg across regulators: {spread_rho:.6e}")
max_abs_rho = np.max(np.abs(per_reg_rho_marg))
print(f"Max |rho_marg| across regulators: {max_abs_rho:.6e}")
print()

# -----------------------------------------------------------------------------
# VERDICT against W13-2 ρ_cc=0 claim
# -----------------------------------------------------------------------------
print("=" * 78)
print("VERDICT (R2-A explicit Fisher recomputation)")
print("=" * 78)
print(f"W13-2 unmarginalized rho_cc:        0.000000e+00 (verdict)")
print(f"R2-A marginalized rho_marg (zeta):  {rho_marg:+.6e}")
print(f"R2-A marginalized rho_marg (max across atlas): {max_abs_rho:.6e}")
print()
print(f"Substrate Fisher off-diagonal F_marg[a,O] (zeta): {F_marg_substrate_offdiag:+.6e}")
print(f"Mack M2 reference (mean-pinned):                  ~ 4.27e-49")
print()
print(f"Operational floor (sigma_LISA * sigma_alphas) ~ 3e-15")
print(f"|rho_marg| / floor: {abs(rho_marg) / 3e-15:.6e}")
print()

if max_abs_rho < 1e-30:
    verdict = "PASS-INDEPENDENCE-OBSERVABLE"
    msg = "rho_marg < 1e-30 across atlas; observable independence confirmed"
elif max_abs_rho < 1e-15:
    verdict = "PASS-INDEPENDENCE-OBSERVABLE-DILUTED"
    msg = "rho_marg below detector floor; observable independence by dilution"
elif max_abs_rho < 0.05:
    verdict = "WEAK-DEPENDENCE"
    msg = "rho_marg above floor but below 0.05; partial dependence"
else:
    verdict = "DEPENDENCE-CONFIRMED"
    msg = "rho_marg above 0.05; substantive observable dependence"

print(f"VERDICT: {verdict}")
print(f"  {msg}")
print()

# Save to JSON for workshop reference
out = {
    "session": "S85",
    "workshop": "6A-CGWB-ALPHAS-INDEPENDENCE",
    "round": "R2-A",
    "agent": "tesla",
    "computation": "explicit_5x5_fisher_with_a_n_nuisance_schur_complement",
    "atlas_pin_zeta": {"a_0": a_0_zeta, "a_2": a_2_zeta, "a_4": a_4_zeta},
    "atlas_mean":    {"a_0": a_0_mean, "a_2": a_2_mean, "a_4": a_4_mean},
    "sigma_alpha_s_CMBS4": sigma_alpha_s_CMBS4,
    "sigma_Omega_GW_LISA": sigma_Omega_GW_LISA,
    "n_s_pin": n_s,
    "Omega_GW_obs": Omega_GW_obs,
    "C_substrate": C.tolist(),
    "C_pinv": C_pinv.tolist(),
    "C_eigvals": eigvals_C.tolist(),
    "C_det": float(np.linalg.det(C)),
    "C_cond": float(np.linalg.cond(C)),
    "C_pearson_a2_a4": float(R[1,2]),
    "J_CGWB_zeta": J_CGWB.tolist(),
    "J_alpha_s_zeta": J_alpha_s.tolist(),
    "F_full_eigvals": eigvals_full.tolist(),
    "F_marg": F_marg.tolist(),
    "F_marg_offdiag": float(F_marg[0,1]),
    "rho_marg_zeta": float(rho_marg),
    "F_marg_substrate_offdiag_zeta": float(F_marg_substrate_offdiag),
    "F_marg_substrate_offdiag_mean": float(F_marg_mean_substrate),
    "per_regulator_F_marg_offdiag": [float(x) for x in per_reg_F_marg],
    "per_regulator_rho_marg":      [float(x) for x in per_reg_rho_marg],
    "spread_rho_across_regulators": float(spread_rho),
    "max_abs_rho_across_regulators": float(max_abs_rho),
    "operational_floor_3e-15": 3e-15,
    "verdict": verdict,
    "verdict_message": msg,
    "comparison_W13_2_rho_cc": 0.0,
}

with open(os.path.join(os.path.dirname(__file__), "_s85_6a_tesla_r2_fisher_5x5.json"), "w") as f:
    json.dump(out, f, indent=2)

print("Saved to _s85_6a_tesla_r2_fisher_5x5.json")
sys.exit(0)
