"""
LEFSCHETZ-GAUSSIAN-74: Squeezed thermal state from one-loop moduli Hessian.

Session 74 Wave 2 Batch 1 (W2-E).
Baptista-spacetime-analyst, S73A phonon-first-hawking workshop carry-forward #13.

Governing structure:
    The Lefschetz thimble around the classical fold saddle has Gaussian
    fluctuations whose covariance is governed by the moduli Hessian H_ij.
    A squeezed thermal state reproduces these fluctuations via the identity

        < q_i q_j >_state  =  C_ij

    where C is determined from H.  For canonically normalised moduli with
    S_tree = (1/2) H_ij q_i q_j (so H_ij has units omega^2 in M_KK units),
    the Gaussian saddle-point measure gives position covariance

        C_ij = (H^{-1/2})_ij / 2

    with mode-wise variance sigma_k^2 = 1/(2 omega_k), omega_k = sqrt(H_eig_k).

    A squeezed thermal state with phase phi_k = 0 and squeeze parameter r_k
    has position variance (Walls-Milburn convention)

        sigma_k^2 = (1/(2 omega_k)) * [ cosh(2 r_k) - sinh(2 r_k) ]
                    * (1 + 2 n_k^thermal)
                  = (1/(2 omega_k)) * exp(-2 r_k) * (1 + 2 n_k^thermal)

    Equivalent convention used in the task prompt (phi_k = 0):

        sigma_k^2 = (1/(2 omega_k)) * [ cosh(2 r_k) - sinh(2 r_k) * 1
                                        + 2 n_k^thermal ]

    Both are solved here; the first (Walls-Milburn) is the standard form.

Inputs:
    computations/_shared/canonical_constants.py              -- framework constants
    computations/session-70/s70_off_jensen_hess.npz             -- 35x35 volume-preserving Hessian
    computations/session-74/s74_ns_1loop_spectral.npz           -- V_CW(fold) = -785.56 M_KK^4

Cross-checks:
    1. Covariance C is positive-definite
    2. Zero-temperature limit: squeezed vacuum (n_k = 0), r_k encodes anisotropy
    3. High-temperature limit: classical thermal (r_k = 0), n_k dominates
    4. Energy comparison: E_state vs V_CW(fold)

Pre-registered gate:
    PASS if |E_state - V_CW| / |V_CW| < 5%
    INFO if 5-15%
    FAIL if > 15% or non-positive-definite

Output:
    s74_lefschetz_gaussian.npz   -- C, r_k, n_k, E_state, V_CW, ratios
    s74_lefschetz_gaussian.png   -- r_k and n_k spectra
"""

import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import time

# Resolve data paths relative to this script's directory so it works from any cwd
_HERE = os.path.dirname(os.path.abspath(__file__))

from canonical_constants import (
    M_KK,
    tau_fold,
    Delta_BCS,
    T_acoustic,
    T_GGE_B2,
    S_fold,
    d2S_fold,
)

t0 = time.time()

# ---------------------------------------------------------------------------
# 1. Load Hessian (W2-D proxy -- use S70 OFF-JENSEN-HESS volume-preserving 35x35)
# ---------------------------------------------------------------------------
hess = np.load(os.path.join(_HERE, "s70_off_jensen_hess.npz"), allow_pickle=True)
H = np.asarray(hess["H_bcs_35"], dtype=float)   # BCS-dressed Hessian (35x35)
H_bare = np.asarray(hess["H_bare_35"], dtype=float)  # bare Hessian for sensitivity

assert H.shape == (35, 35)
assert np.allclose(H, H.T, atol=1e-10), "Hessian not symmetric"

# Diagonalise
evals, evecs = np.linalg.eigh(H)
evals_bare, evecs_bare = np.linalg.eigh(H_bare)

# Sanity: all positive
min_eval = float(evals.min())
assert min_eval > 0, f"Hessian non-positive: min eig = {min_eval}"
is_positive_definite = bool(min_eval > 0)

# ---------------------------------------------------------------------------
# 2. Construct covariance matrix C = (H^{-1/2}) / 2   (canonical Gaussian)
#    Also compute C_inv_H = H^{-1} (task-prompt literal form) for comparison
# ---------------------------------------------------------------------------
omega_k = np.sqrt(evals)                  # physical mode frequencies (M_KK units)
sigma_k_vac_sq = 0.5 / omega_k            # vacuum variance per mode

# Full covariance in q-basis:
C_qq_canonical = evecs @ np.diag(sigma_k_vac_sq) @ evecs.T
C_Hinv_literal = evecs @ np.diag(1.0 / evals) @ evecs.T  # H^{-1}

# Positive-definiteness of covariance
cov_evals = np.linalg.eigvalsh(C_qq_canonical)
cov_positive = bool(cov_evals.min() > 0)

# ---------------------------------------------------------------------------
# 3. Identify the squeezed thermal state parameters
# ---------------------------------------------------------------------------
#
# Walls-Milburn squeezed thermal with phi_k = 0:
#     <q_k^2> = (1/(2 omega_k)) * e^{-2 r_k} * (1 + 2 n_k^th)
#
# The Gaussian Lefschetz thimble gives <q_k^2> = 1/(2 omega_k) (isotropic).
# This corresponds to (r_k = 0, n_k^th = 0) -- pure vacuum in each mode.
# NON-TRIVIAL squeezing enters only when the state is compared to a DIFFERENT
# reference frame (e.g. the bare Hessian).  We compute r_k by taking the
# ratio of BCS-dressed vs bare mode variances.
#
# Reference frequencies omega_k^{bare}; BCS covariance sigma_k^{2,BCS}:
#     sigma_k^{2,BCS} / sigma_k^{2,bare} = exp(-2 r_k)   at T = 0
#
# so r_k = -(1/2) * log( sigma_k^{2,BCS} / sigma_k^{2,bare} )
#       = (1/2) * log( omega_k^{BCS} / omega_k^{bare} )

omega_k_bare = np.sqrt(evals_bare)
r_k = 0.5 * np.log(omega_k_bare / omega_k)  # BCS softening -> positive r_k

# Temperature input: T = T_acoustic (GGE acoustic temperature at fold, 0.112 M_KK)
# This is the physical temperature of the GGE state that emerges post-transit.
T_state = T_acoustic
beta = 1.0 / T_state

# Bose-Einstein occupation per mode:
x = beta * omega_k          # dimensionless; omega_k already in M_KK units
# Clip to avoid overflow
x_clip = np.clip(x, 0.0, 60.0)
n_k_thermal = 1.0 / (np.exp(x_clip) - 1.0)
# Floor tiny occupations to zero if exp(x) >> 1
n_k_thermal[x >= 60.0] = 0.0

# ---------------------------------------------------------------------------
# 4. Verify mode-wise variance matches the task-prompt formula at phi_k = 0
# ---------------------------------------------------------------------------
# Prompt form (phi_k = 0, cos(0) = 1):
#   sigma_k^2 = (1/(2 omega_k)) * ( cosh(2 r_k) - sinh(2 r_k) + 2 n_k^th )
sigma_k_sq_prompt = (0.5 / omega_k) * (
    np.cosh(2.0 * r_k) - np.sinh(2.0 * r_k) + 2.0 * n_k_thermal
)
# Walls-Milburn form (product of squeezing and thermal):
sigma_k_sq_WM = (0.5 / omega_k) * np.exp(-2.0 * r_k) * (1.0 + 2.0 * n_k_thermal)
# Vacuum reference:
sigma_k_sq_vac = 0.5 / omega_k

# ---------------------------------------------------------------------------
# 5. Total energy of the squeezed thermal state
# ---------------------------------------------------------------------------
# Formula from task prompt:
#   E_state = (1/2) * sum_k omega_k * ( cosh(2 r_k) * (1 + 2 n_k) - 1 )
#
# This is the excitation energy above the squeezed-vacuum ground state.
# Zero-point (bosonic CW) contribution:
#   E_zp = (1/2) * sum_k omega_k
#
# Full one-loop effective action (CW):
#   V_CW^{bosonic} = E_zp  (before renormalization subtraction)

E_state_prompt = 0.5 * np.sum(
    omega_k * (np.cosh(2.0 * r_k) * (1.0 + 2.0 * n_k_thermal) - 1.0)
)

# Zero-point energy (pure Gaussian saddle, T=0, r=0)
E_zp = 0.5 * np.sum(omega_k)
E_zp_bare = 0.5 * np.sum(omega_k_bare)

# Full squeezed-thermal expectation of H (including zero-point, in M_KK units)
#  <H> = sum_k (1/2) omega_k * cosh(2 r_k) * (1 + 2 n_k^th)
E_sqth_full = 0.5 * np.sum(
    omega_k * np.cosh(2.0 * r_k) * (1.0 + 2.0 * n_k_thermal)
)

# W1-I value for cross-check
V_CW_fold = -785.5635327400585   # (local) M_KK^4
# Note: V_CW is from the FERMIONIC spectral action 1-loop (D_K sector), whereas
# E_zp above is the BOSONIC 1-loop contribution from the 35D moduli Hessian.
# They are different Hilbert spaces; the gate compares them as a consistency
# check on the Lefschetz thimble structural prediction.

# Fractional mismatch
delta_E_prompt = (E_state_prompt - V_CW_fold) / abs(V_CW_fold)
delta_E_zp = (E_zp - abs(V_CW_fold)) / abs(V_CW_fold)
delta_E_sqth = (E_sqth_full - abs(V_CW_fold)) / abs(V_CW_fold)

# Sign-flipped comparison (bosons contribute positive to zero-point, fermions negative)
# A PHYSICALLY meaningful comparison uses |V_CW| and tests whether the moduli
# bosonic sector magnitude matches the fermionic sector magnitude.

# ---------------------------------------------------------------------------
# 6. Cross-checks: limiting cases
# ---------------------------------------------------------------------------
# 6a. T = 0 limit (pure squeezed vacuum)
x_zero = np.zeros_like(omega_k)
n_k_T0 = np.zeros_like(omega_k)
sigma_T0 = (0.5 / omega_k) * (
    np.cosh(2.0 * r_k) - np.sinh(2.0 * r_k) + 2.0 * n_k_T0
)
E_T0 = 0.5 * np.sum(omega_k * (np.cosh(2.0 * r_k) * (1.0 + 2.0 * n_k_T0) - 1.0))
# At r_k = 0 as well, should be zero:
r_zero_check = np.zeros_like(omega_k)
E_true_vac = 0.5 * np.sum(
    omega_k * (np.cosh(2.0 * r_zero_check) * (1.0 + 2.0 * n_k_T0) - 1.0)
)
assert abs(E_true_vac) < 1e-12, f"Vacuum energy non-zero: {E_true_vac}"

# 6b. High-T limit: for T >> omega_max, n_k ~ T/omega_k, and E_thermal ~ N * T
T_high = 100.0 * omega_k.max()   # far above all modes
x_high = omega_k / T_high
n_k_high = 1.0 / (np.exp(x_high) - 1.0)
E_high_r0 = 0.5 * np.sum(
    omega_k * (np.cosh(2.0 * r_zero_check) * (1.0 + 2.0 * n_k_high) - 1.0)
)
# Should equal sum n_k omega_k ~ (N - small) * T_high
N_modes = 35  # (local)
E_high_classical_expected = N_modes * T_high - 0.5 * np.sum(omega_k)
# actually sum_k omega_k * n_k with n_k -> T/omega_k - 1/2 + O(omega/T)
#       = N * T - (1/2) sum omega_k + O(omega/T)^{-1}
# E_high ~ (1/2) sum omega_k * (2 * T/omega_k - 1) = N * T - (1/2) sum omega_k
E_high_ratio = E_high_r0 / E_high_classical_expected

# 6c. Eigenvalue spot-check against S70 stored values
evals_s70 = np.asarray(hess["evals_bcs_35"])
eval_match = np.allclose(evals, evals_s70, rtol=1e-10)

# ---------------------------------------------------------------------------
# 7. Additional structural diagnostics
# ---------------------------------------------------------------------------
# Squeeze magnitude and thermal occupation summaries
r_min, r_max = float(r_k.min()), float(r_k.max())
r_mean = float(r_k.mean())
n_min, n_max = float(n_k_thermal.min()), float(n_k_thermal.max())
n_mean = float(n_k_thermal.mean())

# Diagonal of C in q-basis
C_diag = np.diag(C_qq_canonical)

# Condition number of H
cond_H = float(evals.max() / evals.min())

# Log-determinant of H (for Z_fold = exp(-S_cl) / sqrt(det(H/2pi)))
logdet_H = float(np.sum(np.log(evals)))

# One-loop contribution to S_eff:
#   delta S_1loop = (1/2) log det (H / 2 pi)
#                 = (1/2) [ log det H - N * log(2 pi) ]
delta_S_1loop_mod = 0.5 * (logdet_H - N_modes * np.log(2.0 * np.pi))

# ---------------------------------------------------------------------------
# 8. Gate verdict
# ---------------------------------------------------------------------------
# Compare to V_CW = -785.56 from W1-I (fermion loop).
# The moduli-Hessian bosonic E_zp has the same dimensions but different sign
# and magnitude.  Report both signed and absolute-value comparisons.

pct_match_prompt = 100.0 * abs(E_state_prompt - V_CW_fold) / abs(V_CW_fold)
pct_match_Ezp_abs = 100.0 * abs(E_zp - abs(V_CW_fold)) / abs(V_CW_fold)
pct_match_Ezp_signed = 100.0 * abs(E_zp + V_CW_fold) / abs(V_CW_fold)  # bosonic + fermionic

# Pre-registered gate uses the prompt-formula energy E_state_prompt against V_CW_fold.
# PASS: < 5%, INFO: 5-15%, FAIL: > 15% or non-PD.
if not (is_positive_definite and cov_positive):
    verdict = "FAIL"
    verdict_reason = "Covariance matrix non-positive-definite"
elif pct_match_prompt < 5.0:
    verdict = "PASS"
    verdict_reason = f"E_state matches V_CW to {pct_match_prompt:.2f}%"
elif pct_match_prompt < 15.0:
    verdict = "INFO"
    verdict_reason = f"E_state matches V_CW to {pct_match_prompt:.2f}% (5-15% band)"
else:
    verdict = "FAIL"
    verdict_reason = (
        f"E_state-V_CW mismatch {pct_match_prompt:.2f}% > 15%. "
        f"Moduli bosonic zero-point (165.79) vs fermion V_CW (|-785.56|) "
        f"differ in magnitude (ratio {E_zp / abs(V_CW_fold):.3f}) "
        f"and sign (bosons positive, fermions negative). "
        f"Sectors are disjoint Hilbert spaces; direct numerical match not expected."
    )

print("=" * 72)
print("LEFSCHETZ-GAUSSIAN-74")
print("=" * 72)
print(f"H shape: {H.shape}")
print(f"Eigenvalues positive: {is_positive_definite} (min = {min_eval:.4f})")
print(f"Covariance C positive: {cov_positive}")
print(f"Condition number H: {cond_H:.2f}")
print()
print(f"Mode frequencies omega_k (M_KK units):")
print(f"  min = {omega_k.min():.4f}")
print(f"  max = {omega_k.max():.4f}")
print(f"  mean = {omega_k.mean():.4f}")
print(f"  sum = {omega_k.sum():.4f}")
print()
print(f"Squeeze parameters r_k:")
print(f"  min = {r_min:.6f}")
print(f"  max = {r_max:.6f}")
print(f"  mean = {r_mean:.6f}")
print()
print(f"Thermal occupations n_k (T = {T_state:.4f} M_KK):")
print(f"  min = {n_min:.2e}")
print(f"  max = {n_max:.2e}")
print(f"  mean = {n_mean:.2e}")
print()
print(f"Energy decomposition (M_KK^4):")
print(f"  E_state (prompt formula) = {E_state_prompt:.4f}")
print(f"  E_zp   (bosonic 1-loop)  = {E_zp:.4f}")
print(f"  E_zp_bare                = {E_zp_bare:.4f}")
print(f"  E_sqth_full              = {E_sqth_full:.4f}")
print(f"  V_CW (W1-I, fermionic)   = {V_CW_fold:.4f}")
print()
print(f"Cross-checks:")
print(f"  True vacuum (r=0, n=0) energy: {E_true_vac:.2e} (should be 0)")
print(f"  High-T ratio: {E_high_ratio:.6f} (should be ~1)")
print(f"  S70 eigenvalue match: {eval_match}")
print()
print(f"One-loop log det H: {logdet_H:.4f}")
print(f"delta S_1loop (moduli): {delta_S_1loop_mod:.4f}")
print()
print(f"GATE: {verdict}")
print(f"  {verdict_reason}")
print(f"  Fractional mismatch (signed, prompt): {100*delta_E_prompt:+.2f}%")
print(f"  Fractional mismatch (|E_zp| vs |V_CW|): {pct_match_Ezp_abs:.2f}%")
print(f"  Fractional mismatch (E_zp+V_CW, total B+F): {pct_match_Ezp_signed:.2f}%")

# ---------------------------------------------------------------------------
# 9. Save data
# ---------------------------------------------------------------------------
np.savez_compressed(
    os.path.join(_HERE, "s74_lefschetz_gaussian.npz"),
    gate_name="LEFSCHETZ-GAUSSIAN-74",
    gate_verdict=verdict,
    gate_detail=verdict_reason,
    # Hessian
    H_bcs_35=H,
    H_bare_35=H_bare,
    evals=evals,
    evals_bare=evals_bare,
    evecs=evecs,
    # Covariance
    C_canonical=C_qq_canonical,
    C_Hinv_literal=C_Hinv_literal,
    cov_evals=cov_evals,
    is_positive_definite=is_positive_definite,
    cov_positive=cov_positive,
    # Mode data
    omega_k=omega_k,
    omega_k_bare=omega_k_bare,
    sigma_k_sq_vac=sigma_k_sq_vac,
    sigma_k_sq_prompt=sigma_k_sq_prompt,
    sigma_k_sq_WM=sigma_k_sq_WM,
    r_k=r_k,
    n_k_thermal=n_k_thermal,
    T_state=T_state,
    # Energies
    E_state_prompt=E_state_prompt,
    E_zp=E_zp,
    E_zp_bare=E_zp_bare,
    E_sqth_full=E_sqth_full,
    V_CW_fold=V_CW_fold,
    delta_E_prompt=delta_E_prompt,
    delta_E_zp=delta_E_zp,
    pct_match_prompt=pct_match_prompt,
    pct_match_Ezp_abs=pct_match_Ezp_abs,
    pct_match_Ezp_signed=pct_match_Ezp_signed,
    # Cross-checks
    E_true_vac_check=E_true_vac,
    E_high_ratio=E_high_ratio,
    eval_match_S70=eval_match,
    # Structural
    cond_H=cond_H,
    logdet_H=logdet_H,
    delta_S_1loop_mod=delta_S_1loop_mod,
    tau_fold=tau_fold,
    N_modes=N_modes,
    T_acoustic=T_acoustic,
    total_time=time.time() - t0,
)

# ---------------------------------------------------------------------------
# 10. Plot r_k and n_k spectra
# ---------------------------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(12, 9))

# Panel 1: omega_k spectrum
ax = axes[0, 0]
ax.plot(np.arange(1, N_modes + 1), omega_k, "o-", color="navy", label="BCS")
ax.plot(np.arange(1, N_modes + 1), omega_k_bare, "s--", color="crimson", label="bare")
ax.set_xlabel("mode index k")
ax.set_ylabel(r"$\omega_k$ [$M_{KK}$]")
ax.set_title("Moduli mode frequencies")
ax.legend()
ax.grid(alpha=0.3)

# Panel 2: r_k
ax = axes[0, 1]
ax.plot(np.arange(1, N_modes + 1), r_k, "o-", color="darkgreen")
ax.axhline(0, color="k", lw=0.5)
ax.set_xlabel("mode index k")
ax.set_ylabel(r"$r_k$ (squeeze parameter)")
ax.set_title(f"Squeeze spectrum (BCS softening vs bare)")
ax.grid(alpha=0.3)

# Panel 3: n_k (log scale; clamp floor)
ax = axes[1, 0]
n_floor = np.where(n_k_thermal > 1e-30, n_k_thermal, 1e-30)
ax.semilogy(np.arange(1, N_modes + 1), n_floor, "o-", color="purple")
ax.set_xlabel("mode index k")
ax.set_ylabel(r"$n_k^{\mathrm{thermal}}$")
ax.set_title(f"Thermal occupation (T = {T_state:.3f} $M_{{KK}}$)")
ax.grid(alpha=0.3)

# Panel 4: mode-resolved energy contribution
ax = axes[1, 1]
E_k_prompt = 0.5 * omega_k * (
    np.cosh(2.0 * r_k) * (1.0 + 2.0 * n_k_thermal) - 1.0
)
E_k_zp = 0.5 * omega_k
ax.plot(np.arange(1, N_modes + 1), E_k_zp, "s-", color="navy",
        label=r"$E_k^{\mathrm{zp}} = \omega_k/2$")
ax.plot(np.arange(1, N_modes + 1), E_k_prompt, "o-", color="darkorange",
        label=r"$E_k$ (prompt formula)")
ax.set_xlabel("mode index k")
ax.set_ylabel(r"$E_k$ [$M_{KK}^4$]")
ax.set_title(
    f"Mode energies (total E_zp={E_zp:.2f}, prompt={E_state_prompt:.4e})"
)
ax.legend()
ax.grid(alpha=0.3)

fig.suptitle(
    f"LEFSCHETZ-GAUSSIAN-74: Squeezed Thermal State from Moduli Hessian\n"
    f"Gate: {verdict} | E_zp/|V_CW| = {E_zp/abs(V_CW_fold):.3f} | "
    f"cond(H) = {cond_H:.2f}",
    fontsize=11,
)
plt.tight_layout()
plt.savefig(os.path.join(_HERE, "s74_lefschetz_gaussian.png"), dpi=140)
plt.close()

print()
print(f"Wall time: {time.time() - t0:.2f} s")
print(f"Output: {os.path.join(_HERE, 's74_lefschetz_gaussian')}.{{npz,png}}")
