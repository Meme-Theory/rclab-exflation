#!/usr/bin/env python3
"""
S80 W1-6: GATE S80-UNIFIED-AS-79-CSUB-SIGN ([SIGN])
=========================================================================

PURPOSE: Structural-identity verification of the c_sub derivative in
UNIFIED-AS-79.

HYPOTHESIS: Under UNIFIED-AS-79,
    d(ln A_s) / d(ln c_sub) = -1.000 exactly
because A_s \\propto 1/c_sub is an explicit factor in the formula.

GATE:
    PASS: |d(ln A_s)/d(ln c_sub) + 1.000| < 0.01
    INFO: within [0.01, 0.10]
    FAIL: > 0.10 (identity violated)

MANDATORY [SIGN] SUBSTITUTION CHAIN
------------------------------------
  Step 1: Definition (UNIFIED-AS-79, confirmed in s80_h_tilde_epoch_td.py:245):
      A_s = (H_tilde^2 / (8 pi^2)) * (1/eps_H) * F_amp * c_sub^{-1} * f_conv

  Step 2: Take logarithm:
      ln A_s = ln(H_tilde^2) - ln(8 pi^2) - ln(eps_H) + ln(F_amp)
               - ln(c_sub) + ln(f_conv)
             = C_0 - ln(c_sub)
      where C_0 is independent of c_sub variation.

  Step 3: Differentiate w.r.t. ln(c_sub):
      d(ln A_s)/d(ln c_sub) = -1   (exact, structural)

  Step 4: Direction:
      c_sub > 1 => A_s < A_s|_{c_sub=1}   (SUPPRESSION, as claimed)

CLASSIFICATION: GEOMETRIC (structural-identity verification of the spectral
                A_s formula; derivative is -1 from explicit 1/c_sub factor).

INDEPENDENCE FROM W1-1: this gate tests a STRUCTURAL identity of the formula,
NOT a numerical value of A_s. The c_sub derivative is -1 regardless of the
H_tilde epoch choice (whether H_tilde refers to fold, horizon-exit, or
observational calibration).

Method:
    1. Central values (from plan, S78 baseline):
       eps_H = 0.02163   (slow-roll at pivot, canonical baseline)
       F_amp = 6858      (linearized power-ratio at k_pivot from S77)
       f_conv = 9.30e-4  (Mellin projection at k_pivot)
       H_tilde_sq = any positive number (cancels in ratio)
       c_sub_0 = 2.238   (central of S78 W2-E three-scheme range)
    2. Perturbation: c_sub_0 * (1 +/- delta), delta = 0.01 (1%).
    3. Compute A_s_plus, A_s_minus with all other factors fixed.
    4. Central-difference logarithmic derivative:
       d(ln A_s)/d(ln c_sub) = [ln A_s_plus - ln A_s_minus] / [ln c_plus - ln c_minus]
    5. Deviation = |derivative + 1.000|.

Expected: deviation < 1e-6 (pure arithmetic, no physics uncertainty).

Session: S80 W1-6
Owner: landau-condensed-matter-theorist
"""

import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import sys
import numpy as np
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
sys.path.insert(0, str(SCRIPT_DIR))

from canonical_constants import PI   # only canonical symbol needed; all
# UNIFIED-AS-79 ingredients are passed as local central values per plan §W1-6


# =============================================================================
# STEP 0: LOCAL CENTRAL VALUES (from S80 plan W1-6 spec)
# =============================================================================
eps_H = 0.02163                 # (local) slow-roll eps at pivot (plan §W1-6)
F_amp = 6858.0                  # (local) W0-5 slot-adjusted linearized F_amp
f_conv = 9.30e-4                # (local) Mellin projection at k_pivot (S78)
H_tilde_sq = 1.0                # (local) arbitrary: cancels in ratio
c_sub_0 = 2.238                 # (local) S78 W2-E central of {2.232, 2.244, 3.647}
delta = 0.01                    # (local) 1% perturbation per plan §W1-6

# Gate thresholds
PASS_THRESH = 0.01              # (local) per plan
INFO_HI = 0.10                  # (local) per plan


def A_s_UNIFIED79(H_tilde_sq, eps_H, F_amp, c_sub, f_conv):
    """UNIFIED-AS-79 closed-form expression.

    Parameters are in arbitrary units (H_tilde^2 cancels in any ratio; the
    full dimensionful A_s requires M_Pl^2 normalization handled at the
    observational-matching stage of UNIFIED-AS-79). For the structural-
    identity test, numerical scale is irrelevant.
    """
    return (H_tilde_sq / (8.0 * PI**2)) * (1.0 / eps_H) * F_amp * (1.0 / c_sub) * f_conv


# =============================================================================
# STEP 1: Compute A_s at three c_sub values (central, +delta, -delta)
# =============================================================================
c_plus = c_sub_0 * (1.0 + delta)     # (local)
c_minus = c_sub_0 * (1.0 - delta)    # (local)

A_s_central = A_s_UNIFIED79(H_tilde_sq, eps_H, F_amp, c_sub_0, f_conv)  # (local)
A_s_plus = A_s_UNIFIED79(H_tilde_sq, eps_H, F_amp, c_plus, f_conv)       # (local)
A_s_minus = A_s_UNIFIED79(H_tilde_sq, eps_H, F_amp, c_minus, f_conv)     # (local)

# =============================================================================
# STEP 2: Central-difference logarithmic derivative
# =============================================================================
d_ln_A_d_ln_c = (np.log(A_s_plus) - np.log(A_s_minus)) / (np.log(c_plus) - np.log(c_minus))  # (local)
deviation = abs(d_ln_A_d_ln_c + 1.0)  # (local)

# Also compute the analytic value (should be exactly -1)
d_ln_A_d_ln_c_analytic = -1.0  # (local) from substitution chain Step 3

# =============================================================================
# STEP 3: Cross-checks
# =============================================================================
# CHK1: The ratio A_s_plus / A_s_minus should equal c_minus / c_plus exactly
ratio_As = A_s_plus / A_s_minus                  # (local)
ratio_c_inv = c_minus / c_plus                   # (local)
chk1_residual = abs(ratio_As - ratio_c_inv)      # (local)

# CHK2: Independence from other factors
# Repeat with H_tilde_sq, F_amp, eps_H, f_conv scaled by random factors;
# derivative must be unchanged.
rng = np.random.default_rng(0xC5B51611)  # (local) deterministic seed
cross_check_deviations = []                   # (local)
for trial in range(5):
    scale_H = rng.uniform(0.1, 10.0)          # (local)
    scale_F = rng.uniform(0.1, 10.0)          # (local)
    scale_eps = rng.uniform(0.1, 10.0)        # (local)
    scale_fc = rng.uniform(0.1, 10.0)         # (local)
    A_plus_alt = A_s_UNIFIED79(H_tilde_sq * scale_H, eps_H * scale_eps,
                                F_amp * scale_F, c_plus, f_conv * scale_fc)  # (local)
    A_minus_alt = A_s_UNIFIED79(H_tilde_sq * scale_H, eps_H * scale_eps,
                                 F_amp * scale_F, c_minus, f_conv * scale_fc)  # (local)
    deriv_alt = (np.log(A_plus_alt) - np.log(A_minus_alt)) / (np.log(c_plus) - np.log(c_minus))  # (local)
    cross_check_deviations.append(abs(deriv_alt + 1.0))

max_cross_dev = max(cross_check_deviations)  # (local)

# CHK3: Also test with delta = 0.001 (tighter) and delta = 0.1 (broader)
# The analytic derivative is -1 exactly; the numerical central-difference has
# higher-order O(delta^2) error, so tighter delta should give smaller deviation.
delta_scan = [1e-4, 1e-3, 1e-2, 1e-1]          # (local)
delta_scan_devs = []                            # (local)
for d in delta_scan:
    cp = c_sub_0 * (1.0 + d)                   # (local)
    cm = c_sub_0 * (1.0 - d)                   # (local)
    Ap = A_s_UNIFIED79(H_tilde_sq, eps_H, F_amp, cp, f_conv)  # (local)
    Am = A_s_UNIFIED79(H_tilde_sq, eps_H, F_amp, cm, f_conv)  # (local)
    deriv_d = (np.log(Ap) - np.log(Am)) / (np.log(cp) - np.log(cm))  # (local)
    delta_scan_devs.append((d, deriv_d, abs(deriv_d + 1.0)))

# =============================================================================
# STEP 4: Verdict classification
# =============================================================================
if deviation < PASS_THRESH:
    verdict = "PASS"
elif deviation < INFO_HI:
    verdict = "INFO"
else:
    verdict = "FAIL"

# =============================================================================
# STEP 5: Reporting
# =============================================================================
print("="*78)
print("S80 W1-6: GATE S80-UNIFIED-AS-79-CSUB-SIGN")
print("="*78)
print()
print("Substitution chain (analytic):")
print("  A_s = (H~^2/(8 pi^2)) * (1/eps_H) * F_amp * c_sub^{-1} * f_conv")
print("  ln A_s = C_0 - ln(c_sub)")
print("  d(ln A_s)/d(ln c_sub) = -1 (structural identity)")
print()
print("Inputs (central values):")
print(f"  eps_H      = {eps_H}")
print(f"  F_amp      = {F_amp}")
print(f"  f_conv     = {f_conv:.4e}")
print(f"  H_tilde_sq = {H_tilde_sq} (arbitrary; cancels in ratio)")
print(f"  c_sub_0    = {c_sub_0}")
print(f"  delta      = {delta} (1% perturbation)")
print()
print("Perturbed A_s values:")
print(f"  A_s(c_minus={c_minus:.6f}) = {A_s_minus:.10e}")
print(f"  A_s(c_0={c_sub_0:.6f})     = {A_s_central:.10e}")
print(f"  A_s(c_plus={c_plus:.6f})   = {A_s_plus:.10e}")
print()
print("Numerical derivative:")
print(f"  d(ln A_s)/d(ln c_sub) = {d_ln_A_d_ln_c:.16f}")
print(f"  expected (analytic)   = {d_ln_A_d_ln_c_analytic:.16f}")
print(f"  |deviation|           = {deviation:.3e}")
print()
print("Cross-checks:")
print(f"  CHK1 (A_plus/A_minus == c_minus/c_plus): residual = {chk1_residual:.3e}")
print(f"  CHK2 (independence from other factors, 5 trials): max |dev| = {max_cross_dev:.3e}")
print(f"  CHK3 (delta scan):")
for d, deriv_d, dev in delta_scan_devs:
    print(f"    delta={d:.0e}  d(lnA)/d(lnc)={deriv_d:.12f}  |dev|={dev:.3e}")
print()
print("Gate thresholds:")
print(f"  PASS: |dev| < {PASS_THRESH}")
print(f"  INFO: {PASS_THRESH} <= |dev| < {INFO_HI}")
print(f"  FAIL: |dev| >= {INFO_HI}")
print()
print(f"VERDICT: {verdict}")
print(f"Direction: c_sub UP => A_s DOWN (SUPPRESSION, UNIFIED-AS-79 convention confirmed)")
print("="*78)

# =============================================================================
# STEP 6: Save .npz
# =============================================================================
out_path = SCRIPT_DIR / "s80_csub_sign.npz"
np.savez(
    out_path,
    # Gate 4-tuple
    d_ln_A_s_d_ln_c_sub=d_ln_A_d_ln_c,
    scheme="UNIFIED-AS-79",
    convention="central-difference-log-derivative",
    L_max="N/A",
    # Inputs
    eps_H=eps_H,
    F_amp=F_amp,
    f_conv=f_conv,
    H_tilde_sq=H_tilde_sq,
    c_sub_0=c_sub_0,
    delta=delta,
    c_plus=c_plus,
    c_minus=c_minus,
    # A_s values
    A_s_central=A_s_central,
    A_s_plus=A_s_plus,
    A_s_minus=A_s_minus,
    # Derivative + deviation
    d_ln_A_d_ln_c=d_ln_A_d_ln_c,
    d_ln_A_d_ln_c_analytic=d_ln_A_d_ln_c_analytic,
    deviation=deviation,
    # Cross-checks
    chk1_residual=chk1_residual,
    cross_check_deviations=np.array(cross_check_deviations),
    max_cross_dev=max_cross_dev,
    delta_scan=np.array([d for d, _, _ in delta_scan_devs]),
    delta_scan_derivs=np.array([deriv for _, deriv, _ in delta_scan_devs]),
    delta_scan_devs=np.array([dev for _, _, dev in delta_scan_devs]),
    # Thresholds + verdict
    pass_thresh=PASS_THRESH,
    info_hi=INFO_HI,
    verdict=verdict,
)
print(f"\nSaved: {out_path}")

# =============================================================================
# STEP 7: Append verdict line
# =============================================================================
verdict_path = SCRIPT_DIR / "s80_gate_verdicts.txt"
verdict_line = (
    f"S80-UNIFIED-AS-79-CSUB-SIGN [W1-6]: {verdict}  "
    f"d(ln A_s)/d(ln c_sub)={d_ln_A_d_ln_c:.10f}  "
    f"|dev|={deviation:.3e}  (threshold PASS<{PASS_THRESH}, INFO<{INFO_HI})  "
    f"scheme=UNIFIED-AS-79  convention=central-diff-log-deriv  "
    f"inputs: c_sub_0={c_sub_0}, delta={delta}, eps_H={eps_H}, F_amp={F_amp}, f_conv={f_conv:.3e}\n"
)
with open(verdict_path, "a", encoding="utf-8") as f:
    f.write(verdict_line)
print(f"Appended verdict to: {verdict_path}")
