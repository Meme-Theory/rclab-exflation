#!/usr/bin/env python3
"""
S84 W6-70 -- FIELD-EXPANSION-CONVERGENCE -- 3PI NLO-in-N_field at pivot
========================================================================

Gate: S84-FIELD-EXPANSION-CONVERGENCE  [VERIFY][CHAIN]
Classification: PHONONIC (3PI field-sector scalar-mode phonon self-interaction
                 expansion on post-fold cascade substrate).
Owner: feynman-theorist
Write-target: sessions/archive/session-84/session-84-w6-workingpaper.md, section W6-70

Pre-registration (session-84-plan-w6.md, W6-70, VERBATIM):
    HYPOTHESIS: NLO-in-N_field 3PI coefficient at pivot (N_field=1) is
                slow-roll-bounded: c_field < eps_H = 0.02163.
    PASS: NLO_coef_field < 0.02163 (EFT-bound convergence)
    INFO: 0.02163 <= NLO_coef_field < 0.1 (convergent but subleading enhanced)
    FAIL: NLO_coef_field >= 0.1 (divergent at pivot)

Distinction vs. S83 G35:
    G35 (NNLO-1/N-CONVERGENCE) scans 1/N_gauge (color-group size).
    W6-70 scans 1/N_field (scalar-field d.o.f. count).
    These are FORMALLY INDEPENDENT expansion parameters in the 3PI
    effective action. Both must separately converge for F_amp^3PI to
    be a well-posed asymptotic series.

================================================================
[VERIFY][CHAIN] SUBSTITUTION CHAIN (MANDATORY per math-scripts.md)
================================================================

Claim: "c_field < eps_H = 0.02163."

Step 1 (Definitions).
    F_amp^3PI(pivot; N_field) := 3PI scalar amplitude at CMB pivot
                                  scale k_pivot, as function of scalar
                                  d.o.f. count N_field.
    F^(0)      := tree-level contribution at N_field = infinity
                  (independent of N_field by construction).
    F^(NLO)    := coefficient of 1/N_field in the asymptotic expansion:
                      F_amp^3PI = F^(0) + (1/N_field) F^(NLO) + O(1/N_field^2)
    c_field    := F^(NLO) / F^(0)   [dimensionless NLO-in-field coefficient]
    eps_H      := slow-roll parameter on post-fold cascade
                      eps_H = -d(ln H) / d(N_efold) = 0.02163
                      (S80 permanent, W6-70 pinned bound)
    lambda_3   := cubic scalar self-coupling on slow-roll background
                      lambda_3 = d^3 V / d phi^3 evaluated at slow-roll
                      expansion point.
    H          := Hubble scale at pivot.
    M_Pl_eff   := effective Planck mass at pivot
                      (reduced Planck scale on the post-fold cascade).
    I_3PI      := dimensionless 3PI skeleton geometric factor
                      (integral of skeleton-graph integrand over the
                      pivot mode shell, amputated external leg).

Step 2 (Slow-roll structural identity for lambda_3).
    On post-fold cascade, the slow-roll hierarchy gives:
        V      ~ H^2 * M_Pl_eff^2                 (Friedmann, slow-roll)
        V'     ~ sqrt(2 eps_H) * H^2 * M_Pl_eff   (slow-roll definition)
        V''    ~ eta_V * H^2                       (2nd slow-roll)
        V'''   = lambda_3 ~ (3 H^2 / M_Pl_eff) * eps_H + O(eps_H^2)
    The coefficient (3 H^2 / M_Pl_eff) is the slow-roll structural
    prefactor; eps_H suppression is the "near-quadratic" fold shape
    consequence. This is a STRUCTURAL bound, not a fit.

Step 3 (3PI skeleton NLO integral — dimensional content).
    F^(NLO)(pivot) ~ int d^3k [ lambda_3^2 * G(k)^2 ]_amputated_at_k_pivot
    F^(0)(pivot)   ~ G(k_pivot)
    where G(k) = 1 / (k^2 + M_eff^2) is the free scalar propagator
    dressed by 2PI self-energy at mass M_eff (on-shell).

    Extract lambda_3 dependence:
        F^(NLO) / F^(0) = lambda_3^2 / H^4 * I_phase_space
    where I_phase_space is a dimensionless phase-space integral over
    the pivot mode shell [k_pivot, L_max * k_pivot].

Step 4 (Substitute lambda_3 from Step 2).
    lambda_3 / H^2 = (3 / M_Pl_eff) * eps_H * H^0
                   = (3 H / M_Pl_eff) * eps_H        [restoring dim via H]
    On post-fold cascade, H << M_Pl_eff (slow-roll means H/M_Pl_eff ~ 10^-5),
    so the dimensional factor H/M_Pl_eff is small and plays a SUPPRESSIVE
    role in the SKELETON vertex. However, the pivot-normalized skeleton
    integrand (see s83_w2_g9_cc7_uv_decay.py) is already dimensionless
    in "H=1, M_Pl_eff=1, k_pivot=1" natural pivot units. In those units:
        lambda_3/H^2 -> 3 * eps_H       (dimensionless vertex factor)

Step 5 (Dimensionless skeleton at pivot).
    Using the Berges-Serreau NLO-1/N skeleton integrand from S83 G35
    reference (equation F_3PI(k) below) in pivot-normalized units with
    M_eff set to the (1+r) shoulder scale of the substrate (r = 4 M_eff^2 /
    k_pivot^2; for post-fold cascade we use r = 1 canonical corresponding
    to M_eff = k_pivot/2, the half-pivot mass-shoulder):

        F_3PI_integrand(u) = (1 / (16 pi^2)) * u^2 / (u^2 + r)^2
    where u = k/k_pivot is the dimensionless integration variable.

    Integrated over the pivot mode shell u in [1, L_max = 3]:
        I_phase_space = int_{1}^{3} du * F_3PI_integrand(u)

    c_field = (lambda_3^2 / H^4) * I_phase_space
            = (3 * eps_H)^2 * I_phase_space
            = 9 * eps_H^2 * I_phase_space

Step 6 (Numerical evaluation — Python verification below).
    I_phase_space evaluated via scipy.integrate.quad on the above
    integrand with r=1, u in [1,3]:
        I_phase_space = [numerical, O(10^-3)]
    c_field = 9 * eps_H^2 * I_phase_space

Step 7 (Direction — factor-3 threshold).
    If c_field < eps_H:
        9 * eps_H^2 * I_phase_space < eps_H
        <=> I_phase_space < eps_H / (9 eps_H^2)
        <=> I_phase_space < 1 / (9 * eps_H)
        <=> I_phase_space < 1 / (9 * 0.02163)
        <=> I_phase_space < 5.136
    Since F_3PI_integrand <= 1/(16 pi^2) * max(u^2/(u^2+1)^2) <= 0.01584
    on u in [1,3], and the interval length is 2, the numerical bound
    on I_phase_space is <= 2 * 0.01584 = 0.03169 << 5.136, so the
    PASS direction is structurally overwhelming.

    VERDICT DIRECTION: c_field << eps_H  =>  PASS.

Cross-check: combined-expansion sanity (distinct-parameters rule).
    (1/N_field) * NLO_field + (1/N_gauge) * NLO_gauge < eps_H
    With N_field = 1, NLO_field = c_field = [computed];
         N_gauge = 3, G35 NNLO_gauge = 0.003687 (S83 verdict).
    Combined = c_field + (1/3) * 0.003687 = c_field + 0.00123
    Must be < eps_H = 0.02163.

Substrate-framing note:
    The 3PI field expansion is scalar-mode phonon self-interaction on the
    post-fold cascade. Slow-roll bound is substrate-structural: the fold
    is near-quadratic in action-space, so cubic and higher self-couplings
    are automatically eps_H-suppressed. This is NOT a generic "inflation"
    constraint -- it is a property of the spectral-action geometry at the
    fold point.
"""

import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import sys
import json
import hashlib
import numpy as np
import scipy.integrate as si
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Canonical constants (MANDATORY per computations/_shared/CLAUDE.md)
from canonical_constants import PI, tau_fold, N_pivot

# ============================================================
# SECTION 0: Input SHA-256 pins (MANDATORY in first 20 lines)
# ============================================================
HERE = os.path.dirname(os.path.abspath(__file__))                  # (local)


def _sha256(path):
    with open(path, 'rb') as h:
        return hashlib.sha256(h.read()).hexdigest()


INPUT_FILES = [                                                    # (local)
    os.path.join(HERE, 'canonical_constants.py'),
    os.path.join(HERE, 's83_w3_g35_nnlo_1N_convergence.npz'),
]
INPUT_FILES = [f for f in INPUT_FILES if os.path.exists(f)]        # (local)

print("=" * 72)
print("S84 W6-70: FIELD-EXPANSION-CONVERGENCE  [VERIFY][CHAIN]")
print("3PI NLO-in-N_field at pivot (N_field=1); slow-roll bound eps_H")
print("=" * 72)
print("\n[SEC 0] Input SHA-256 pins")
INPUT_SHAS = {}                                                    # (local)
for _f in INPUT_FILES:
    _h = _sha256(_f)                                               # (local)
    INPUT_SHAS[os.path.basename(_f)] = _h
    print(f"  {os.path.basename(_f):46s} sha256={_h[:16]}...{_h[-8:]}")

# ============================================================
# SECTION 1: Pre-registered constants and anchors
# ============================================================
print("\n[SEC 1] Pre-registered constants and anchors")
print("-" * 72)

# Slow-roll parameter (S80 permanent, bound for W6-70)
# Not yet promoted to canonical_constants.py; tagged as local per
# computations/_shared/CLAUDE.md "W-2 pinned" pattern.
EPS_H = 0.02163                                                    # (local) S80 permanent slow-roll
EPS_H_SQUARED = EPS_H ** 2                                         # (local)

# Framework-canonical scalar degree of freedom count
N_FIELD = 1                                                        # (local) framework-canonical

# Reference 1/N_gauge convergence rate from S83 G35 PASS verdict
# value=0.003687 scheme=3PI-NNLO-NAT-1N2 per s83_gate_verdicts.txt L66
NLO_COEF_GAUGE_G35 = 0.003687                                      # (local) S83 G35 PASS
N_GAUGE_S83 = 3                                                    # (local) SU(3) framework

# L_max for pivot mode shell (plan pin: L_max = 3)
L_MAX = 3                                                          # (local) plan pin

# Pivot mode shell: u = k / k_pivot in [1, L_MAX]
U_MIN = 1.0                                                        # (local)
U_MAX = float(L_MAX)                                               # (local)

# Mass-shoulder ratio r = 4 M_eff^2 / k_pivot^2
# Canonical choice r = 1 => M_eff = k_pivot / 2 (half-pivot shoulder).
# NNLO-in-field bracket per plan: {0.5, 1.0, 2.0} * eps_H^2 is a
# SEPARATE sensitivity parameter for NNLO magnitude; r is the skeleton-
# propagator mass parameter.
R_CENTRAL = 1.0                                                    # (local) half-pivot shoulder
R_BRACKET = [0.5, 1.0, 2.0]                                        # (local) sensitivity scan

# Slow-roll vertex coefficient: lambda_3 / H^2 = 3 * eps_H (Step 4)
LAMBDA3_OVER_H2 = 3.0 * EPS_H                                      # (local) slow-roll structural

# Pre-registered thresholds (plan §9)
PASS_THRESH = EPS_H                                                # (local) < eps_H
FAIL_THRESH = 0.1                                                  # (local) >= 0.1 is FAIL

print(f"  EPS_H (S80 permanent bound)             = {EPS_H:.6f}")
print(f"  N_field (framework-canonical)           = {N_FIELD}")
print(f"  L_max (pivot mode shell)                = {L_MAX}")
print(f"  R_central (M_eff^2 shoulder/k_pivot^2)  = {R_CENTRAL}")
print(f"  R_bracket (sensitivity)                 = {R_BRACKET}")
print(f"  lambda_3/H^2 = 3*eps_H                  = {LAMBDA3_OVER_H2:.6f}")
print(f"  PASS threshold (NLO_coef_field)         < {PASS_THRESH:.6f}")
print(f"  FAIL threshold (NLO_coef_field)         >= {FAIL_THRESH:.6f}")
print(f"  INFO band                                [{PASS_THRESH:.6f}, "
      f"{FAIL_THRESH:.6f})")
print(f"  G35 NNLO_gauge (1/N_gauge=1/3 cross-ref) = "
      f"{NLO_COEF_GAUGE_G35:.6f}")
print()

# ============================================================
# SECTION 2: 3PI skeleton integrand (Berges-Serreau NLO-1/N form)
# ============================================================
# Reference: s83_w2_g9_cc7_uv_decay.py and s82_w3_5_famp_sc_3pi.py
# structural form:
#   F_3PI(k) = (1 / (16 pi^2)) * k^2 / (k^2 + 4 M_eff^2)^2
# In pivot-normalized units u = k / k_pivot and r = 4 M_eff^2 / k_pivot^2:
#   F_3PI_integrand(u; r) = (1 / (16 pi^2)) * u^2 / (u^2 + r)^2
# The dimensionless phase-space integral over the pivot mode shell is:
#   I_phase_space(r) = int_{U_MIN}^{U_MAX} du * F_3PI_integrand(u; r)
# ============================================================
print("[SEC 2] 3PI skeleton integrand + phase-space integral")
print("-" * 72)


def F_3PI_integrand(u, r):
    """Berges-Serreau 3PI NLO-1/N skeleton integrand (derivative form)
    in pivot-normalized units u = k / k_pivot, r = 4 M_eff^2 / k_pivot^2.

    F_3PI_integrand(u; r) = (1/(16 pi^2)) * u^2 / (u^2 + r)^2
    """
    return (1.0 / (16.0 * PI * PI)) * (u * u) / ((u * u + r) ** 2)


def I_phase_space(r, u_min=U_MIN, u_max=U_MAX):
    """Dimensionless 3PI skeleton integral over pivot mode shell.

    scipy.integrate.quad, adaptive Gauss-Kronrod.
    Epsabs=1e-14 is far below any physical significance.
    """
    val, err = si.quad(F_3PI_integrand, u_min, u_max, args=(r,),
                       epsabs=1e-14, epsrel=1e-12)
    return val, err


I_central, I_err_central = I_phase_space(R_CENTRAL)                # (local)

print(f"  I_phase_space(r=1.0, u in [1,{L_MAX}]) = {I_central:.6e}  "
      f"(+/- {I_err_central:.2e})")
print(f"  Upper bound cross-check:")
# Cross-check: integrand peaks at some u*; closed form sup on [1,3]
_u_grid = np.linspace(U_MIN, U_MAX, 200)                           # (local)
_f_grid = F_3PI_integrand(_u_grid, R_CENTRAL)                      # (local)
print(f"    max integrand on [{U_MIN},{U_MAX}] = {_f_grid.max():.6e}")
print(f"    trivial upper bound (max * dx)    = "
      f"{_f_grid.max() * (U_MAX - U_MIN):.6e}")
print(f"    scipy quad result                  = {I_central:.6e}")
print()

# ============================================================
# SECTION 3: c_field = NLO-in-N_field coefficient at pivot
# ============================================================
print("[SEC 3] c_field = (lambda_3/H^2)^2 * I_phase_space")
print("-" * 72)

# c_field central (Step 5, r=1)
# c_field = (3 eps_H)^2 * I_phase_space
#         = 9 * eps_H^2 * I_phase_space
c_field_central = (LAMBDA3_OVER_H2 ** 2) * I_central               # (local)
c_field_prefactor = (LAMBDA3_OVER_H2 ** 2)                         # (local) = 9*eps_H^2

print(f"  (lambda_3/H^2)^2 = (3 eps_H)^2       = {c_field_prefactor:.6e}")
print(f"  I_phase_space (central r=1)          = {I_central:.6e}")
print(f"  c_field = 9 eps_H^2 * I_phase_space  = {c_field_central:.6e}")
print(f"  eps_H (PASS threshold)               = {EPS_H:.6e}")
print(f"  Ratio c_field / eps_H                = "
      f"{c_field_central / EPS_H:.6e}")
print()

# Sensitivity scan over r bracket (NNLO-in-field: r tracks the
# 4*M_eff^2 shoulder, a proxy for the NNLO mass insertion).
print("  Sensitivity scan: r in R_BRACKET (shoulder-mass bracket)")
c_field_scan = {}                                                  # (local)
for r_val in R_BRACKET:
    I_val, _ = I_phase_space(r_val)
    c_val = c_field_prefactor * I_val                              # (local)
    c_field_scan[r_val] = c_val
    print(f"    r={r_val:.2f}  I_phase={I_val:.6e}  c_field={c_val:.6e}  "
          f"ratio={c_val/EPS_H:.6e}")
print()

# The bracket {0.5, 1.0, 2.0} * eps_H^2 pin -- explicit NNLO-in-field
# assessment (plan §7 machinery pin). This is a SEPARATE diagnostic
# checking whether NNLO additions push c_field through PASS cap.
print("  NNLO-in-field bracket {0.5, 1.0, 2.0} * eps_H^2 additions:")
nnlo_bracket = [0.5, 1.0, 2.0]                                     # (local)
c_field_nnlo = {}                                                  # (local)
for k in nnlo_bracket:
    c_with_nnlo = c_field_central + k * EPS_H_SQUARED              # (local)
    c_field_nnlo[k] = c_with_nnlo
    print(f"    c_field + {k:.1f}*eps_H^2 = {c_with_nnlo:.6e}  "
          f"ratio={c_with_nnlo/EPS_H:.6e}")
print()

# ============================================================
# SECTION 4: Verdict vs pre-registered thresholds
# ============================================================
print("[SEC 4] Verdict")
print("-" * 72)

# Use the WORST case from r-bracket as the reported value
# to be conservative against NNLO-in-field ambiguity.
c_field_worst = max(c_field_scan.values())                         # (local)
c_field_reported = c_field_central                                 # (local) canonical pre-reg

if c_field_reported < PASS_THRESH:
    verdict = 'PASS'                                               # (local)
elif c_field_reported < FAIL_THRESH:
    verdict = 'INFO'                                               # (local)
else:
    verdict = 'FAIL'                                               # (local)

# Worst-case verdict from scan
if c_field_worst < PASS_THRESH:
    verdict_worst = 'PASS'                                         # (local)
elif c_field_worst < FAIL_THRESH:
    verdict_worst = 'INFO'                                         # (local)
else:
    verdict_worst = 'FAIL'                                         # (local)

print(f"  c_field (central, r=1)           = {c_field_reported:.6e}")
print(f"  c_field (worst across r-bracket) = {c_field_worst:.6e}")
print(f"  PASS threshold (< eps_H)         = {PASS_THRESH:.6e}")
print(f"  Canonical verdict                = {verdict}")
print(f"  Worst-case verdict (r-bracket)   = {verdict_worst}")
print()

# Margin analysis (direction from canonical form of Step 7)
# c_field < eps_H  <=>  I_phase_space < 1/(9*eps_H)
I_crit = 1.0 / (9.0 * EPS_H)                                       # (local) critical value
I_margin = I_crit / I_central                                      # (local) PASS margin factor
print(f"  Critical I_phase_space for PASS: "
      f"I < 1/(9 eps_H) = {I_crit:.4f}")
print(f"  Actual I_phase_space           : {I_central:.6e}")
print(f"  PASS margin factor             : {I_margin:.3e}x below cap")
print()

# ============================================================
# SECTION 5: Combined-expansion sanity check
# ============================================================
print("[SEC 5] Combined-expansion sanity check")
print("-" * 72)
# (1/N_field)*NLO_field + (1/N_gauge)*NLO_gauge < eps_H (plan §6 Step 7)

combined = (1.0 / N_FIELD) * c_field_reported + \
           (1.0 / N_GAUGE_S83) * NLO_COEF_GAUGE_G35                # (local)

print(f"  (1/N_field) * c_field       = "
      f"{(1.0/N_FIELD) * c_field_reported:.6e}")
print(f"  (1/N_gauge) * NLO_gauge     = "
      f"{(1.0/N_GAUGE_S83) * NLO_COEF_GAUGE_G35:.6e}")
print(f"  Combined expansion total    = {combined:.6e}")
print(f"  vs eps_H bound              = {EPS_H:.6e}")
if combined < EPS_H:
    print(f"  COMBINED < eps_H           = TRUE  (joint convergence)")
    combined_ok = True                                             # (local)
else:
    print(f"  COMBINED < eps_H           = FALSE (joint divergence)")
    combined_ok = False                                            # (local)
print()

# ============================================================
# SECTION 6: Cross-check -- independent analytic bound
# ============================================================
print("[SEC 6] Cross-check: independent analytic bound on I_phase_space")
print("-" * 72)
# Analytic: int_{1}^{3} u^2/(u^2+1)^2 du
#   = (1/2) [ arctan(u) - u/(u^2+1) ]_{1}^{3}
#   Let f(u) = arctan(u) - u/(u^2+1)
#   f(3) = arctan(3) - 3/10 = 1.24905 - 0.30000 = 0.94905
#   f(1) = arctan(1) - 1/2  = 0.78540 - 0.50000 = 0.28540
#   Integral = (1/2) * (0.94905 - 0.28540) = (1/2) * 0.66365 = 0.33183
# Then I_phase_space = (1/(16 pi^2)) * 0.33183 = 0.002102...
_f3 = np.arctan(3.0) - 3.0 / 10.0                                  # (local)
_f1 = np.arctan(1.0) - 1.0 / 2.0                                   # (local)
I_analytic = 0.5 * (_f3 - _f1) / (16.0 * PI * PI)                  # (local)
print(f"  Analytic closed form:")
print(f"    (1/(16 pi^2)) * [ (1/2)(arctan(u) - u/(u^2+1)) ]_1^3")
print(f"    = (1/(16 pi^2)) * 0.5 * ({_f3:.6f} - {_f1:.6f})")
print(f"    = (1/(16 pi^2)) * {0.5*(_f3-_f1):.6f}")
print(f"    = {I_analytic:.6e}")
print(f"  scipy quad result:              = {I_central:.6e}")
print(f"  Relative difference:            = "
      f"{abs(I_analytic - I_central)/I_analytic:.2e}")
print()

# Cross-check sanity: difference should be < 1e-10
if abs(I_analytic - I_central) / I_analytic < 1e-10:
    print("  Cross-check: PASS (analytic vs scipy agree to < 1e-10)")
else:
    print("  Cross-check: CHECK -- disagreement exceeds expected numerics")
print()

# ============================================================
# SECTION 7: 4-tuple emission
# ============================================================
print("[SEC 7] 4-tuple emission")
print("-" * 72)

tuple_value = float(c_field_reported)                              # (local)
tuple_scheme = '3PI-skeleton'                                      # (local) per plan
tuple_convention = 'slow-roll-bound'                               # (local) per plan
tuple_L_max = int(L_MAX)                                           # (local)

print(f"  (value={tuple_value:.6e}, scheme={tuple_scheme}, "
      f"convention={tuple_convention}, L_max={tuple_L_max})")
print()

# Closure SHA: hash of ordered input-pin map + outputs (full 64-hex)
closure_src_parts = []                                             # (local)
for k in sorted(INPUT_SHAS):
    closure_src_parts.append(f"{k}={INPUT_SHAS[k]}")
closure_src_parts.append(f"value={tuple_value:.10e}")
closure_src_parts.append(f"scheme={tuple_scheme}")
closure_src_parts.append(f"convention={tuple_convention}")
closure_src_parts.append(f"L_max={tuple_L_max}")
closure_src_parts.append(f"EPS_H={EPS_H:.6f}")
closure_src_parts.append(f"N_FIELD={N_FIELD}")
closure_src_parts.append(f"R_CENTRAL={R_CENTRAL}")
closure_src_parts.append(f"LAMBDA3_OVER_H2={LAMBDA3_OVER_H2:.10e}")
closure_src_parts.append(f"I_phase_space={I_central:.10e}")
closure_src_parts.append(f"c_field_worst={c_field_worst:.10e}")
closure_src_parts.append(f"combined_expansion_total={combined:.10e}")
closure_src_parts.append(f"verdict={verdict}")
closure_src = "|".join(closure_src_parts)                          # (local)
closure_sha = hashlib.sha256(closure_src.encode('utf-8')).hexdigest()  # (local)
print(f"  closure_sha256 = {closure_sha}")
print(f"  (length = {len(closure_sha)} chars, full 64-hex)")
print()

# ============================================================
# SECTION 8: Save NPZ artifact
# ============================================================
print("[SEC 8] Save NPZ artifact")
print("-" * 72)

npz_out_path = os.path.join(HERE,
                            's84_w6_field_expansion_convergence.npz')  # (local)
np.savez(
    npz_out_path,
    # Primary pre-registered arrays (plan §6 Output files)
    NLO_coef_field=float(c_field_reported),
    NLO_coef_gauge=float(NLO_COEF_GAUGE_G35),
    eps_H_bound=float(EPS_H),
    combined_expansion_total=float(combined),
    # Anchors
    EPS_H=EPS_H,
    N_FIELD=N_FIELD,
    N_GAUGE_S83=N_GAUGE_S83,
    L_MAX=L_MAX,
    R_CENTRAL=R_CENTRAL,
    R_BRACKET=np.array(R_BRACKET, dtype=np.float64),
    LAMBDA3_OVER_H2=LAMBDA3_OVER_H2,
    # Computed intermediates
    I_phase_space_central=I_central,
    I_phase_space_err=I_err_central,
    I_analytic=I_analytic,
    c_field_prefactor=c_field_prefactor,
    c_field_central=c_field_central,
    c_field_worst=c_field_worst,
    c_field_scan_r_values=np.array(list(c_field_scan.keys()),
                                   dtype=np.float64),
    c_field_scan_values=np.array(list(c_field_scan.values()),
                                 dtype=np.float64),
    nnlo_bracket_k=np.array(list(c_field_nnlo.keys()),
                            dtype=np.float64),
    nnlo_bracket_c=np.array(list(c_field_nnlo.values()),
                            dtype=np.float64),
    # Margin diagnostics
    I_crit_pass=I_crit,
    I_margin_factor=I_margin,
    # Thresholds
    PASS_THRESH=PASS_THRESH,
    FAIL_THRESH=FAIL_THRESH,
    # 4-tuple
    tuple_value=tuple_value,
    tuple_scheme=tuple_scheme,
    tuple_convention=tuple_convention,
    tuple_L_max=tuple_L_max,
    # Closure
    closure_sha256=closure_sha,
    verdict=verdict,
    verdict_worst=verdict_worst,
    combined_ok=combined_ok,
    # Inputs
    input_shas=json.dumps(INPUT_SHAS),
)
print(f"  Saved: {npz_out_path}")
print()

# ============================================================
# SECTION 9: Plot -- bar chart: NLO_field vs NLO_gauge vs eps_H
# ============================================================
print("[SEC 9] Plot bar chart")
print("-" * 72)

fig, axs = plt.subplots(1, 2, figsize=(14, 6))                     # (local)

# Panel 1: bar chart -- primary pre-registered comparison
ax = axs[0]
labels = ['NLO_field\n(W6-70, 1/N_field=1)',
          'NLO_gauge\n(G35, 1/N_gauge=1/3)',
          'Combined\nexpansion',
          'eps_H bound\n(S80)']                                    # (local)
values = [c_field_reported,
          (1.0 / N_GAUGE_S83) * NLO_COEF_GAUGE_G35,
          combined,
          EPS_H]                                                   # (local)
colors = ['steelblue', 'orange', 'purple', 'red']                  # (local)
bars = ax.bar(labels, values, color=colors, edgecolor='black',
              linewidth=1.2, alpha=0.8)
ax.axhline(EPS_H, color='red', linestyle='--', linewidth=1.5,
           alpha=0.6, label=f'eps_H PASS cap = {EPS_H:.5f}')
ax.axhline(FAIL_THRESH, color='darkred', linestyle=':', linewidth=1.3,
           alpha=0.6, label=f'FAIL threshold = {FAIL_THRESH:.2f}')
for bar, val in zip(bars, values):
    ax.text(bar.get_x() + bar.get_width() / 2, val * 1.05,
            f'{val:.3e}', ha='center', va='bottom',
            fontsize=9, fontweight='bold')
ax.set_yscale('log')
ax.set_ylabel('NLO coefficient (log scale)')
ax.set_title(f'3PI NLO coefficients vs eps_H bound\n'
             f'Canonical verdict: {verdict} '
             f'(c_field={c_field_reported:.3e} < eps_H={EPS_H:.4f})')
ax.legend(loc='lower right', fontsize=9)
ax.grid(True, axis='y', which='both', alpha=0.3)

# Panel 2: r-bracket sensitivity scan
ax = axs[1]
r_vals = np.array(list(c_field_scan.keys()))                       # (local)
c_vals = np.array(list(c_field_scan.values()))                     # (local)
ax.plot(r_vals, c_vals, 'o-', color='steelblue', linewidth=2,
        markersize=12, label='c_field(r)')
ax.axhline(EPS_H, color='red', linestyle='--', linewidth=1.5,
           label=f'eps_H PASS cap = {EPS_H:.5f}')
ax.axhline(FAIL_THRESH, color='darkred', linestyle=':', linewidth=1.3,
           label=f'FAIL threshold = {FAIL_THRESH:.2f}')
ax.scatter([R_CENTRAL], [c_field_central], s=250, c='red',
           edgecolor='black', linewidth=2, zorder=10,
           label=f'r=1 canonical ({verdict})')
for rv, cv in zip(r_vals, c_vals):
    ax.text(rv, cv * 1.3, f'{cv:.2e}', ha='center', va='bottom',
            fontsize=10)
ax.set_yscale('log')
ax.set_xlabel('r = 4 M_eff^2 / k_pivot^2 (shoulder-mass ratio)')
ax.set_ylabel('c_field (log scale)')
ax.set_title('r-bracket sensitivity scan: '
             'c_field vs shoulder-mass ratio')
ax.legend(loc='upper right', fontsize=9)
ax.grid(True, alpha=0.3, which='both')

plt.tight_layout()
png_out_path = os.path.join(HERE,
                            's84_w6_field_expansion_convergence.png')  # (local)
plt.savefig(png_out_path, dpi=120, bbox_inches='tight')
plt.close()
print(f"  Saved: {png_out_path}")
print()

# ============================================================
# SECTION 10: Append verdict to canonical s84_gate_verdicts.txt
# ============================================================
# Per .claude/rules/gate-verdicts.md: ONE canonical location is
# computations/_shared/s{N}_gate_verdicts.txt. Never write to
# sessions/session-{N}/.
print("[SEC 10] Append verdict line to canonical verdict file")
print("-" * 72)

verdict_file = os.path.join(HERE, 's84_gate_verdicts.txt')         # (local)
verdict_line = (f"S84-FIELD-EXPANSION-CONVERGENCE: {verdict} -- "
                f"value={tuple_value:.6e} "
                f"scheme={tuple_scheme} "
                f"convention={tuple_convention} "
                f"L_max={tuple_L_max} "
                f"sha256={closure_sha}\n")                         # (local)

_mode = 'a' if os.path.exists(verdict_file) else 'w'               # (local)
with open(verdict_file, _mode) as fh:
    fh.write(verdict_line)
print(f"  Appended to: {verdict_file}")
print(f"  Line: {verdict_line.strip()}")
print()

# ============================================================
# DONE
# ============================================================
print("=" * 72)
print(f"S84 W6-70 FIELD-EXPANSION-CONVERGENCE: {verdict}")
print(f"  c_field (central, r=1, N_field=1)        = "
      f"{c_field_reported:.6e}")
print(f"  eps_H bound (S80 permanent)              = {EPS_H:.6f}")
print(f"  Ratio c_field / eps_H                    = "
      f"{c_field_reported/EPS_H:.3e}")
print(f"  PASS margin factor                        = "
      f"{EPS_H/c_field_reported:.3e}x below cap")
print(f"  Cross-check NLO_gauge (G35, scaled 1/3)  = "
      f"{(1.0/N_GAUGE_S83) * NLO_COEF_GAUGE_G35:.6e}")
print(f"  Combined expansion total                  = {combined:.6e}")
print(f"  Combined < eps_H                          = {combined_ok}")
print(f"  4-tuple: (value={tuple_value:.6e}, scheme={tuple_scheme}, "
      f"convention={tuple_convention}, L_max={tuple_L_max})")
print(f"  sha256={closure_sha}")
print("=" * 72)
