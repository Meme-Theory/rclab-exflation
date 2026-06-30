#!/usr/bin/env python3
"""
S86 W8 GATE C — HBW / MP-Abs-Conv at s=6 on Framework-Truncated f_6 = 0.1 Residue
================================================================================

Gate: S86-CUTOFF-SQRT-GATE-C-S82-APPLICABILITY  [VERIFY]
Classification: GEOMETRIC (Hausdorff-Bernstein-Widder positive-cone test on
                a regulator's spectral-action profile reconstructed from
                Mellin moments — a property of the regulator class, not of
                substrate excitations.)
Owner: lizzi-spectral-functional-theorist
Workshop: s86-cutoff-sqrt-gate-abc-trio.md (R1 Turn-B; lizzi response to connes)

PURPOSE
-------
GATE C of the cutoff_sqrt 3-gate joint adjudication apparatus
(`sessions/framework/registry/cutoff-sqrt-adjudication.md` §3.3). Test whether the
spectral-action profile f_residue(u) reconstructed from the framework-truncated
cutoff_AL2010 Mellin vector (f_0, f_2, f_4, f_6) = (2, 1, 0.5, 0.1) admits

  (a) ABSOLUTELY CONVERGENT Mellin moment at s = 6 (KO-dim anchor),
      i.e., M[f_residue](6) = int_0^inf u^5 f_residue(u) du < +inf;
  (b) POSITIVE-CONE membership in Hausdorff-Bernstein-Widder sense, i.e.,
      f_residue(u) is COMPLETELY MONOTONE on (0, +inf):
         f_residue(u) = int_0^inf rho(alpha) exp(-alpha u) d alpha
      with rho(alpha) >= 0 a positive measure (Widder, *The Laplace
      Transform* 1941, Ch. IV; HBW theorem).

Per W4-3 §3.3 + cutoff-sqrt-adjudication.md §3.3:
  PASS:  M[f_residue](6) absolutely convergent AND positive (in HBW cone).
  FAIL:  diverges OR oscillatory-non-positive (HBW excluded).
  INFO:  convergent but outside HBW positive cone (marginal).

This is the kernel-class admissibility test EXPLICITLY restricted to the
framework's L_max=3 numerical residue at the f_6 slot, NOT the unregulated
sharp-cutoff kernel (the latter was retracted under R2-A-CONV-(a) citation
correction during the S85 W4 workshop).

PRE-REGISTERED SUBSTITUTION CHAIN (per `.claude/rules/math-scripts.md`)
----------------------------------------------------------------------
Step 1 (definitions):
  Andrianov-Lizzi (2010) §5 spectral-action moments (sharp-cutoff convention):
    f_0    := res_{s=0} M[f](s) = sum of HBW spectral measure on (0, +inf)
    f_{2k} := M[f](k) = int_0^inf x^{k-1} f(x) dx       (k = 1, 2, 3, ...)
  Framework numerical truncation at L_max=3 (workshop §3.3 +
  cutoff-sqrt-adjudication.md §3.3 line 196): f_residue Mellin vector
    (f_0, f_2, f_4, f_6) = (2, 1, 0.5, 0.1)
  HBW positive cone (Widder Ch. IV):
    HBW := {f : (0, inf) -> R : f completely monotone}
        = {f : exists rho >= 0 measure on (0, inf) with
                 f(u) = int rho(alpha) exp(-alpha u) d alpha}

Step 2 (substitute):
  Reconstruct f_residue as 4-term sum-of-exponentials (S84 W7b-81 #2 BASELINE
  class -- the canonical CM ansatz, immediately HBW-compatible IF all weights
  c_j >= 0):
    f_residue(u) = sum_{j=1}^{4} c_j * exp(-lambda_j * u)
  Pin lambda_j = {0.5, 1.0, 2.0, 4.0} (dyadic Mellin-cone discretization,
  PRDR-fixed at plan-freeze; see Source pin file in §4 below).
  Mellin moments (closed form):
    M[exp(-lambda u)](s) = Gamma(s) * lambda^(-s)
    M[f_residue](s) = Gamma(s) * sum_j c_j * lambda_j^(-s)
    res_{s=0} M[f_residue] = sum_j c_j   (Gamma(s) ~ 1/s near s=0)
  Match the 4 prescribed moments:
    f_0  = sum_j c_j                             = 2
    f_2  = M[f](1) = sum_j c_j / lambda_j        = 1
    f_4  = M[f](2) = sum_j c_j / lambda_j^2      = 0.5
    f_6  = M[f](3) * 2 = ... = 2 sum_j c_j/L^3   = 0.1
                 i.e. sum_j c_j / lambda_j^3    = 0.05

Step 3 (simplify):
  Linear system A c = m where A_{ij} = 1/lambda_j^{i-1} (i=1..4 = exponents
  0,1,2,3), m = (2, 1, 0.5, 0.05). Solved exactly via numpy.linalg.solve
  on this 4x4 well-conditioned Vandermonde-like matrix.

  GATE C test (Step 3.a, MP-abs-conv at s=6):
    M[f_residue](6) = Gamma(6) * sum_j c_j * lambda_j^(-6) = 120 * S_6
  Convergence test: |M[f_residue](6)| < ABSOLUTE_FINITE_THRESH = 1e15
    AND R-scan saturation (R = 5, 10, 20, 50, 100, 200, 500): the
    truncated integral M_R := int_0^R u^5 f_residue(u) du is monotone
    bounded with |M_R - M_inf|/|M_inf| -> 0 within SAT_REL_TOL = 1e-3
    (per S83 G27 / S84 W7b-81 saturation-test methodology).

  GATE C test (Step 3.b, HBW positivity):
    HBW test: c_j >= 0 for all j (4-atom point-mass measure
    rho(alpha) = sum_j c_j delta(alpha - lambda_j) is positive iff all c_j
    nonnegative). If any c_j < 0, f_residue is NOT in HBW positive cone.

Step 4 (direction):
  PASS  iff Mellin moment at s=6 absolutely convergent (Step 3.a) AND
            f_residue is in HBW positive cone (all c_j >= 0, Step 3.b).
  FAIL  iff M[f_residue](6) diverges OR f_residue is oscillatory-non-positive
            (some c_j < 0 AND moment finite -- i.e., the cancellations
             that give finite Mellin do not preserve HBW positivity).
  INFO  iff M[f_residue](6) finite AND some c_j < 0 (convergent but
            outside HBW positive cone -- the S82 marginal case).
  Direction read from sign(min_j c_j) and sign(M_6 - ABS_THRESH):
    min_j c_j >= 0 AND M_6 finite  -> PASS
    min_j c_j <  0 AND M_6 finite  -> INFO  (converged but not in HBW cone)
    M_6 not finite                 -> FAIL  (regardless of sign)
    Oscillatory-non-positive       -> FAIL  (R-scan ratio not saturating)

Step 5 (cross-check):
  Two independent reconstructions:
    (A) PRIMARY    -- 4-term sum-of-exp at lambda = {0.5, 1, 2, 4}.
    (B) STENCIL    -- 4-term sum-of-exp at lambda = {1, 2, 4, 8}.
  Both must yield same SIGN pattern on min(c_j) for the gate verdict to be
  ROBUST (lambda-pin independent at the sign level). Magnitudes will
  generally differ (different inversion conditioning); only the
  PASS/INFO/FAIL classification is required to match.

ENVIRONMENT
-----------
CPU thread cap at 8 (before numpy import). Single-machine numerics; no GPU
(linear-algebra problem is 4x4; matrix inversion is O(64) flops).
"""
from __future__ import annotations

import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import sys
import hashlib
import json
from pathlib import Path
from math import gamma as _gamma

import numpy as np
from scipy.integrate import quad
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent                       # (local)
sys.path.insert(0, str(HERE))
from canonical_constants import *  # noqa: F401,F403

# ============================================================
# SECTION 0: Input SHA-256 pins
# ============================================================

def _sha256(path: Path) -> str:
    h = hashlib.sha256()                                     # (local)
    with open(path, 'rb') as fp:
        h.update(fp.read())
    return h.hexdigest()


PROJECT_ROOT = HERE.parent                                   # (local)
INPUT_FILES = [                                              # (local)
    HERE / 'canonical_constants.py',
    HERE / 's84_w7b_81_mp_admissibility_extended.py',
    PROJECT_ROOT / 'sessions' / 'framework' / 'cutoff-sqrt-adjudication.md',
    PROJECT_ROOT / 'sessions' / 'session-86' / 'session-86-w4-workingpaper.md',
]

print("=" * 78)
print("S86 W8 GATE C — HBW / MP-Abs-Conv at s=6 on f_6=0.1 Framework-Truncated")
print("=" * 78)
print("\n[SEC 0] Input SHA-256 pins")
INPUT_SHAS = {}                                              # (local)
for _f in INPUT_FILES:
    if _f.exists():
        _h = _sha256(_f)                                     # (local)
        INPUT_SHAS[str(_f.relative_to(PROJECT_ROOT))] = _h
        print(f"  {_f.name:48s} sha256={_h[:16]}...{_h[-8:]}")
    else:
        INPUT_SHAS[str(_f.relative_to(PROJECT_ROOT))] = None
        print(f"  {_f.name:48s} MISSING")

# ============================================================
# SECTION 1: Substitution chain (print for audit trail)
# ============================================================
print("\n[SEC 1] Substitution chain (5 steps, pre-registered)")
print("  Step 1: AL2010 spectral-action f_0/f_2/f_4/f_6 + HBW positive cone def")
print("  Step 2: Reconstruct f_residue = sum_j c_j exp(-lambda_j u), 4 atoms")
print("  Step 3: Solve 4x4 linear sys; compute M[f](6) = 120 * sum c_j/lam_j^6")
print("  Step 4: Direction: min(c_j) >= 0 + |M[f](6)| < ABS_THRESH")
print("  Step 5: Cross-check at second lambda-pin (PRIMARY={0.5,1,2,4} vs"
      " STENCIL={1,2,4,8})")

# ============================================================
# SECTION 2: Pre-registered framework Mellin vector + machinery pins
# ============================================================
print("\n[SEC 2] Framework Mellin vector + machinery pins")

# Pre-registered framework-truncated Mellin vector
# Source: cutoff-sqrt-adjudication.md §3.3 line 195-196:
#   "Framework numerical Mellin vector: (2, 1, 0.5, 0.1) (cutoff_AL2010
#    framework-truncated at L_max=3); the f_6 = 0.1 residue specifically."
FRAMEWORK_MELLIN_VEC = (2.0, 1.0, 0.5, 0.1)                  # (local) (f_0,f_2,f_4,f_6)
print(f"  Framework (f_0, f_2, f_4, f_6) = {FRAMEWORK_MELLIN_VEC}")
print(f"  Source: cutoff-sqrt-adjudication.md §3.3 line 195-196")

# AL2010 published vector (cross-check anchor only -- NOT the gate target)
PUBLISHED_MELLIN_VEC = (0.5, 1.0, 1.0, 0.0)                  # (local) (f_0,f_2,f_4,f_6)
print(f"  Published anchor    (1/2, 1, 1, 0) = {PUBLISHED_MELLIN_VEC} (cross-check only)")

# Lambda pins (PRIMARY + STENCIL); dyadic
LAMBDA_PRIMARY = np.array([0.5, 1.0, 2.0, 4.0])              # (local)
LAMBDA_STENCIL = np.array([1.0, 2.0, 4.0, 8.0])              # (local)
print(f"  PRIMARY lambdas   = {LAMBDA_PRIMARY.tolist()}")
print(f"  STENCIL lambdas   = {LAMBDA_STENCIL.tolist()}")

# Test parameters
S_KO = 6.0                                                   # (local) KO-dim anchor
ABSOLUTE_FINITE_THRESH = 1.0e15                              # (local) |M_6|<thresh => finite
SAT_REL_TOL = 1.0e-3                                         # (local) span-test tolerance
R_SCAN = [5.0, 10.0, 20.0, 50.0, 100.0, 200.0, 500.0]        # (local)
print(f"  S_KO = {S_KO} (KO-dim anchor for M_4 x SU(3))")
print(f"  ABSOLUTE_FINITE_THRESH = {ABSOLUTE_FINITE_THRESH}")
print(f"  SAT_REL_TOL = {SAT_REL_TOL}  (R-scan span saturation)")
print(f"  R_SCAN = {R_SCAN}")

# ============================================================
# SECTION 3: Reconstruct f_residue from prescribed Mellin moments
# ============================================================
print("\n[SEC 3] Reconstruct f_residue(u) = sum_j c_j exp(-lambda_j u)")
print("        Linear system: A c = m  (Vandermonde-like)")
print("        Row i=0: sum_j c_j           = f_0")
print("        Row i=1: sum_j c_j/lambda_j  = f_2")
print("        Row i=2: sum_j c_j/lambda_j^2 = f_4")
print("        Row i=3: sum_j c_j/lambda_j^3 = f_6 / Gamma(3) = f_6/2")


def build_moment_system(lambdas, mellin_vec):
    """A_{ij} = 1/lambda_j^i for i in {0,1,2,3}; m = (f_0, f_2, f_4, f_6/2)."""
    A = np.zeros((4, 4))                                     # (local)
    for i in range(4):
        for j in range(4):
            A[i, j] = lambdas[j] ** (-i)
    f_0, f_2, f_4, f_6 = mellin_vec                          # (local)
    # Convert AL2010 spectral-action f_n to Mellin moment form:
    #   f_0  -> sum c_j (Gamma residue at s=0)
    #   f_2  -> M[f](1) = Gamma(1)*sum c_j/lam = 1 * sum c_j/lam
    #   f_4  -> M[f](2) = Gamma(2)*sum c_j/lam^2 = 1 * sum c_j/lam^2
    #   f_6  -> M[f](3) = Gamma(3)*sum c_j/lam^3 = 2 * sum c_j/lam^3
    m = np.array([f_0, f_2, f_4, f_6 / 2.0])                 # (local)
    return A, m


# PRIMARY reconstruction
A_pri, m_pri = build_moment_system(LAMBDA_PRIMARY, FRAMEWORK_MELLIN_VEC)
cond_pri = np.linalg.cond(A_pri)                             # (local)
c_primary = np.linalg.solve(A_pri, m_pri)                    # (local)
residual_pri = np.linalg.norm(A_pri @ c_primary - m_pri)     # (local)
print(f"\n  PRIMARY (lambda = {LAMBDA_PRIMARY.tolist()})")
print(f"    cond(A) = {cond_pri:.3e}")
print(f"    c_primary  = [{', '.join(f'{c:+.6e}' for c in c_primary)}]")
print(f"    residual   = {residual_pri:.3e}")
print(f"    min(c_j)   = {np.min(c_primary):+.6e}  ", end="")
print(f"({'>= 0 (HBW-OK)' if np.min(c_primary) >= 0 else '<  0 (HBW-VIOLATED)'})")

# STENCIL reconstruction (cross-check)
A_sten, m_sten = build_moment_system(LAMBDA_STENCIL, FRAMEWORK_MELLIN_VEC)
cond_sten = np.linalg.cond(A_sten)                           # (local)
c_stencil = np.linalg.solve(A_sten, m_sten)                  # (local)
residual_sten = np.linalg.norm(A_sten @ c_stencil - m_sten)  # (local)
print(f"\n  STENCIL (lambda = {LAMBDA_STENCIL.tolist()})")
print(f"    cond(A) = {cond_sten:.3e}")
print(f"    c_stencil  = [{', '.join(f'{c:+.6e}' for c in c_stencil)}]")
print(f"    residual   = {residual_sten:.3e}")
print(f"    min(c_j)   = {np.min(c_stencil):+.6e}  ", end="")
print(f"({'>= 0 (HBW-OK)' if np.min(c_stencil) >= 0 else '<  0 (HBW-VIOLATED)'})")

# Verify moment match: A c == m to machine epsilon
print("\n  Verification: A c reproduces m to machine epsilon")
verify_pri = A_pri @ c_primary - m_pri                       # (local)
verify_sten = A_sten @ c_stencil - m_sten                    # (local)
print(f"    PRIMARY  max|A c - m| = {np.max(np.abs(verify_pri)):.3e}")
print(f"    STENCIL  max|A c - m| = {np.max(np.abs(verify_sten)):.3e}")

# ============================================================
# SECTION 4: Mellin moment at s = 6 (closed form + numerical quad)
# ============================================================
print("\n[SEC 4] Mellin moment M[f_residue](6) = Gamma(6) * sum c_j/lam_j^6")
print(f"        Gamma(6) = {_gamma(6.0):.6f}  (anchor: 120, exact)")


def mellin_at_s_closed(lambdas, c, s):
    """Closed form: M[f](s) = Gamma(s) * sum_j c_j * lambda_j^(-s)."""
    return _gamma(s) * float(np.sum(c * lambdas ** (-s)))


def f_residue_eval(u, lambdas, c):
    """f_residue(u) = sum_j c_j exp(-lambda_j u)."""
    if np.isscalar(u):
        return float(np.sum(c * np.exp(-lambdas * u)))
    return np.sum(
        c[:, None] * np.exp(-lambdas[:, None] * u[None, :]), axis=0)


M_6_pri_closed = mellin_at_s_closed(LAMBDA_PRIMARY, c_primary, S_KO)  # (local)
M_6_sten_closed = mellin_at_s_closed(LAMBDA_STENCIL, c_stencil, S_KO)  # (local)
print(f"\n  Closed form:")
print(f"    PRIMARY M[f_residue](6) = {M_6_pri_closed:+.6e}")
print(f"    STENCIL M[f_residue](6) = {M_6_sten_closed:+.6e}")

# Numerical quad cross-check (PRIMARY only)
def integrand_primary(u):
    return u ** (S_KO - 1.0) * f_residue_eval(u, LAMBDA_PRIMARY, c_primary)


M_6_pri_num, M_6_pri_err = quad(                            # (local)
    integrand_primary, 0.0, np.inf, limit=200)
print(f"\n  Numerical quad (PRIMARY, [0, inf)):")
print(f"    M[f_residue](6) = {M_6_pri_num:+.6e}  (quad err = {M_6_pri_err:.2e})")

closed_vs_quad_dev = abs(M_6_pri_num - M_6_pri_closed)       # (local)
closed_vs_quad_rel = closed_vs_quad_dev / abs(M_6_pri_closed) if abs(M_6_pri_closed) > 0 else np.inf  # (local)
print(f"    abs|closed - quad| = {closed_vs_quad_dev:.3e}")
print(f"    rel|closed - quad| = {closed_vs_quad_rel:.3e}")

# ============================================================
# SECTION 5: R-scan saturation test
# ============================================================
print("\n[SEC 5] R-scan saturation test  ")
print("        M_R := int_0^R u^5 f_residue(u) du; check span saturation")


M_scan_pri = []                                              # (local)
for R in R_SCAN:
    val, _ = quad(integrand_primary, 0.0, R, limit=200)
    M_scan_pri.append(val)
M_scan_pri = np.array(M_scan_pri)                            # (local)

print(f"  PRIMARY R-scan (M_R for R in {R_SCAN}):")
for R, M_R in zip(R_SCAN, M_scan_pri):
    print(f"    R = {R:6.1f}  M_R = {M_R:+.6e}")

# Saturation check: span of |M_R| for R in last 3 values; ratio max/min - 1
last3 = np.abs(M_scan_pri[-3:])                              # (local)
span_ratio = (last3.max() - last3.min()) / max(last3.min(), 1e-30)  # (local)
print(f"  Last-3 span ratio (max/min - 1) = {span_ratio:.3e}")
saturated = span_ratio < SAT_REL_TOL                         # (local)
print(f"  Saturation status: {'SATURATED' if saturated else 'NOT SATURATED'}"
      f"  (SAT_REL_TOL = {SAT_REL_TOL})")

abs_finite = abs(M_6_pri_closed) < ABSOLUTE_FINITE_THRESH    # (local)
print(f"  Absolute-finite check: |M_6|={abs(M_6_pri_closed):.3e} < {ABSOLUTE_FINITE_THRESH}: "
      f"{'PASS' if abs_finite else 'FAIL'}")

# ============================================================
# SECTION 6: HBW positivity test
# ============================================================
print("\n[SEC 6] HBW positivity test")
print("        f_residue in HBW positive cone iff all c_j >= 0")
print("        (4-atom point-mass measure rho = sum c_j delta(alpha-lambda_j))")

min_c_pri = float(np.min(c_primary))                         # (local)
min_c_sten = float(np.min(c_stencil))                        # (local)
print(f"  PRIMARY min(c_j) = {min_c_pri:+.6e}")
print(f"  STENCIL min(c_j) = {min_c_sten:+.6e}")

hbw_primary = min_c_pri >= 0.0                               # (local)
hbw_stencil = min_c_sten >= 0.0                              # (local)
print(f"  HBW-PRIMARY: {'IN POSITIVE CONE' if hbw_primary else 'OUTSIDE POSITIVE CONE'}")
print(f"  HBW-STENCIL: {'IN POSITIVE CONE' if hbw_stencil else 'OUTSIDE POSITIVE CONE'}")

cross_check_sign_match = (hbw_primary == hbw_stencil)        # (local)
print(f"  PRIMARY/STENCIL sign-match (HBW classification robust under "
      f"lambda-pin shift): {cross_check_sign_match}")

# Direct CM probe: evaluate f_residue at u in {0, 0.1, 0.5, 1, 2, 5, 10}
# and check sign of derivative pattern (approximate first 3 derivatives)
print("\n  CM-probe (direct f_residue evaluation):")
u_probe = np.array([0.01, 0.1, 0.5, 1.0, 2.0, 5.0, 10.0])    # (local)
f_pri = f_residue_eval(u_probe, LAMBDA_PRIMARY, c_primary)   # (local)
f_sten = f_residue_eval(u_probe, LAMBDA_STENCIL, c_stencil)  # (local)
print(f"    u                  : {[f'{u:.2f}' for u in u_probe]}")
print(f"    f_residue PRIMARY  : {[f'{v:+.3e}' for v in f_pri]}")
print(f"    f_residue STENCIL  : {[f'{v:+.3e}' for v in f_sten]}")
sign_change_pri = np.any(np.diff(np.sign(f_pri)) != 0)       # (local)
sign_change_sten = np.any(np.diff(np.sign(f_sten)) != 0)     # (local)
print(f"    PRIMARY  sign-change in u-probe: {sign_change_pri}  (CM requires NO sign-change)")
print(f"    STENCIL  sign-change in u-probe: {sign_change_sten}")

# ============================================================
# SECTION 7: Verdict mapping per pre-registered thresholds
# ============================================================
print("\n[SEC 7] Verdict mapping (pre-registered Step 4)")
print("  PASS: M[f](6) abs-finite AND HBW positive cone (all c_j >= 0)")
print("  INFO: M[f](6) abs-finite AND outside HBW (some c_j < 0, marginal)")
print("  FAIL: M[f](6) NOT finite OR oscillatory-non-positive R-scan")

# Direction read (PRIMARY is binding; STENCIL is cross-check)
if not abs_finite:
    verdict = "FAIL"                                         # (local)
    reason = "M[f_residue](6) NOT finite"                    # (local)
elif not saturated:
    verdict = "FAIL"                                         # (local)
    reason = "R-scan NOT saturated (oscillatory-non-positive)"  # (local)
elif hbw_primary:
    verdict = "PASS"                                         # (local)
    reason = "abs-finite + HBW positive cone"                # (local)
else:
    # M_6 finite, R-scan saturated, but min(c_j) < 0 -- marginal case
    verdict = "INFO"                                         # (local)
    reason = "abs-finite but OUTSIDE HBW positive cone (some c_j<0; "\
             "non-CM but Mellin-finite)"                     # (local)

print(f"\n  Final verdict: {verdict}")
print(f"  Reason: {reason}")
print(f"  Direction: PRIMARY min(c_j)={min_c_pri:+.6e}; STENCIL min(c_j)={min_c_sten:+.6e}")
print(f"  Cross-check sign-match: {cross_check_sign_match}")

# ============================================================
# SECTION 8: Closure SHA-256 (input-pin map)
# ============================================================
print("\n[SEC 8] Closure SHA-256 (audit_sha256)")

closure_map = {                                              # (local)
    'FRAMEWORK_MELLIN_VEC': list(FRAMEWORK_MELLIN_VEC),
    'PUBLISHED_MELLIN_VEC': list(PUBLISHED_MELLIN_VEC),
    'LAMBDA_PRIMARY': LAMBDA_PRIMARY.tolist(),
    'LAMBDA_STENCIL': LAMBDA_STENCIL.tolist(),
    'S_KO': S_KO,
    'ABSOLUTE_FINITE_THRESH': ABSOLUTE_FINITE_THRESH,
    'SAT_REL_TOL': SAT_REL_TOL,
    'R_SCAN': R_SCAN,
    'c_primary': [float(v) for v in c_primary],
    'c_stencil': [float(v) for v in c_stencil],
    'M_6_pri_closed': float(M_6_pri_closed),
    'M_6_sten_closed': float(M_6_sten_closed),
    'M_6_pri_num': float(M_6_pri_num),
    'min_c_pri': min_c_pri,
    'min_c_sten': min_c_sten,
    'abs_finite': abs_finite,
    'saturated': saturated,
    'hbw_primary': hbw_primary,
    'hbw_stencil': hbw_stencil,
    'cross_check_sign_match': cross_check_sign_match,
    'verdict': verdict,
    'verdict_reason': reason,
    'inputs': {k: v for k, v in sorted(INPUT_SHAS.items())
               if v is not None},
    '__script__': 's86_w8_gate_c_hbw_mp_abs_conv_s6',
    '__gate_id__': 'S86-CUTOFF-SQRT-GATE-C-S82-APPLICABILITY',
}

closure_str = json.dumps(closure_map, sort_keys=True, default=str)  # (local)
audit_sha = hashlib.sha256(closure_str.encode('utf-8')).hexdigest()  # (local)
assert len(audit_sha) == 64, "audit SHA must be full 64-char hexdigest"

# Content SHA = SHA-256 of THIS script's bytes (W9a-99 dual-SHA template)
this_script = HERE / 's86_w8_gate_c_hbw_mp_abs_conv_s6.py'   # (local)
content_sha = _sha256(this_script)                           # (local)

print(f"  audit_sha256   = {audit_sha}")
print(f"  content_sha256 = {content_sha}")

# ============================================================
# SECTION 9: Save .npz artifact
# ============================================================
print("\n[SEC 9] Saving data .npz")
out_npz = HERE / 's86_w8_gate_c_data.npz'                    # (local)

np.savez(
    out_npz,
    framework_mellin_vec=np.array(FRAMEWORK_MELLIN_VEC),
    published_mellin_vec=np.array(PUBLISHED_MELLIN_VEC),
    lambda_primary=LAMBDA_PRIMARY,
    lambda_stencil=LAMBDA_STENCIL,
    s_KO=S_KO,
    R_SCAN=np.array(R_SCAN),
    c_primary=c_primary,
    c_stencil=c_stencil,
    cond_primary=cond_pri,
    cond_stencil=cond_sten,
    M_6_pri_closed=M_6_pri_closed,
    M_6_sten_closed=M_6_sten_closed,
    M_6_pri_num=M_6_pri_num,
    M_6_pri_err=M_6_pri_err,
    M_scan_pri=M_scan_pri,
    span_ratio=span_ratio,
    saturated=saturated,
    abs_finite=abs_finite,
    min_c_pri=min_c_pri,
    min_c_sten=min_c_sten,
    hbw_primary=hbw_primary,
    hbw_stencil=hbw_stencil,
    cross_check_sign_match=cross_check_sign_match,
    f_pri_at_uprobe=f_pri,
    f_sten_at_uprobe=f_sten,
    u_probe=u_probe,
    sign_change_pri=sign_change_pri,
    sign_change_sten=sign_change_sten,
    verdict=np.array([verdict]),
    reason=np.array([reason]),
    audit_sha=np.array([audit_sha]),
    content_sha=np.array([content_sha]),
    input_shas=np.array(
        [f"{k}={v}" for k, v in sorted(INPUT_SHAS.items())
         if v is not None]),
)
print(f"  Saved: {out_npz}")

# ============================================================
# SECTION 10: PNG diagnostic
# ============================================================
print("\n[SEC 10] Saving PNG diagnostic")
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Top-left: f_residue(u) on log scale
u_grid = np.linspace(0.01, 10.0, 400)                        # (local)
f_pri_grid = f_residue_eval(u_grid, LAMBDA_PRIMARY, c_primary)  # (local)
f_sten_grid = f_residue_eval(u_grid, LAMBDA_STENCIL, c_stencil)  # (local)
ax = axes[0, 0]
ax.plot(u_grid, f_pri_grid, 'b-', lw=1.5, label='PRIMARY (lam={0.5,1,2,4})')
ax.plot(u_grid, f_sten_grid, 'r--', lw=1.5,
        label='STENCIL (lam={1,2,4,8})')
ax.axhline(0, color='gray', lw=0.5, alpha=0.5)
ax.set_xlabel("u"); ax.set_ylabel("f_residue(u)")
ax.set_title(f"Reconstructed f_residue (HBW-prim={hbw_primary}, HBW-sten={hbw_stencil})")
ax.legend(loc='best', fontsize=9); ax.grid(True, alpha=0.3)

# Top-right: c_j coefficients
ax = axes[0, 1]
xs = np.arange(4)                                            # (local)
ax.bar(xs - 0.2, c_primary, width=0.4, label='PRIMARY', color='steelblue')
ax.bar(xs + 0.2, c_stencil, width=0.4, label='STENCIL', color='salmon')
ax.axhline(0, color='black', lw=0.7)
ax.set_xticks(xs)
ax.set_xticklabels([f"j={j+1}\nlamP={l:g}\nlamS={ls:g}"
                    for j, (l, ls) in enumerate(
                        zip(LAMBDA_PRIMARY, LAMBDA_STENCIL))])
ax.set_ylabel("c_j (HBW positivity weights)")
ax.set_title(f"min(c_j): PRI={min_c_pri:.2e}, STN={min_c_sten:.2e}")
ax.legend(loc='best'); ax.grid(True, alpha=0.3)

# Bottom-left: R-scan saturation
ax = axes[1, 0]
ax.semilogx(R_SCAN, M_scan_pri, 'bo-', lw=1.5, label='M_R PRIMARY')
ax.axhline(M_6_pri_closed, color='red', ls='--',
           label=f'M_inf closed = {M_6_pri_closed:.3e}')
ax.set_xlabel("R (upper integration limit)")
ax.set_ylabel("M_R = int_0^R u^5 f(u) du")
ax.set_title(f"R-scan saturation (span_ratio={span_ratio:.2e},"
             f" {'SAT' if saturated else 'NOT SAT'})")
ax.legend(loc='best', fontsize=9); ax.grid(True, alpha=0.3)

# Bottom-right: verdict status
ax = axes[1, 1]
ax.axis('off')
status_text = (
    f"GATE C VERDICT: {verdict}\n"
    f"\n"
    f"Reason: {reason}\n"
    f"\n"
    f"  PRIMARY  M[f](6) = {M_6_pri_closed:+.4e}  min(c_j) = {min_c_pri:+.3e}\n"
    f"  STENCIL  M[f](6) = {M_6_sten_closed:+.4e}  min(c_j) = {min_c_sten:+.3e}\n"
    f"\n"
    f"  abs_finite     : {abs_finite}\n"
    f"  saturated      : {saturated}\n"
    f"  HBW PRIMARY    : {hbw_primary}\n"
    f"  HBW STENCIL    : {hbw_stencil}\n"
    f"  Cross-match    : {cross_check_sign_match}\n"
    f"\n"
    f"  audit_sha256[:16] = {audit_sha[:16]}\n"
    f"  content_sha256[:16] = {content_sha[:16]}\n"
)
ax.text(0.05, 0.95, status_text, transform=ax.transAxes,
        family='monospace', fontsize=9, va='top')
ax.set_title(f"S86-CUTOFF-SQRT-GATE-C: HBW/MP-abs-conv at s=6 [{verdict}]")

fig.suptitle("S86 W8 GATE C: HBW Positive-Cone & MP-Abs-Conv at s=6 on f_6=0.1 Residue",
             fontsize=12)
fig.tight_layout()
out_png = HERE / 's86_w8_gate_c_hbw_mp_abs_conv_s6.png'      # (local)
fig.savefig(out_png, dpi=120)
plt.close(fig)
print(f"  Saved: {out_png}")

# ============================================================
# SECTION 11: Append verdict line + W9a-99 dual-SHA companion row
# ============================================================
print("\n[SEC 11] Append verdict to computations/session-86/s86_gate_verdicts.txt")
verdicts_path = HERE / 's86_gate_verdicts.txt'               # (local)

value_str = (                                                # (local)
    f"min_c_pri={min_c_pri:+.4e};min_c_sten={min_c_sten:+.4e};"
    f"M_6_pri={M_6_pri_closed:+.4e};M_6_sten={M_6_sten_closed:+.4e};"
    f"abs_finite={abs_finite};saturated={saturated};"
    f"hbw_primary={hbw_primary};hbw_stencil={hbw_stencil}"
)

verdict_line = (                                             # (local)
    f"S86-CUTOFF-SQRT-GATE-C-S82-APPLICABILITY: {verdict} -- "
    f"value='{value_str}' "
    f"scheme=MP-abs-conv-s6 "
    f"convention=f_6=0.1-residue "
    f"L_max=3 "
    f"audit_sha256={audit_sha} "
    f"content_sha256={content_sha} "
    f"schema_version=S86+\n"
)
companion_row = (                                            # (local)
    f"# audit_sha256_short={audit_sha[:16]} "
    f"content_sha256_short={content_sha[:16]} "
    f"# S86-CUTOFF-SQRT-GATE-C-S82-APPLICABILITY dual-SHA companion row (W9a-99 split) "
    f"verdict_reason='{reason}' "
    f"PRIMARY_lambda={LAMBDA_PRIMARY.tolist()} "
    f"STENCIL_lambda={LAMBDA_STENCIL.tolist()} "
    f"c_primary={[round(float(c), 6) for c in c_primary]} "
    f"c_stencil={[round(float(c), 6) for c in c_stencil]} "
    f"cross_match={cross_check_sign_match}\n"
)

with open(verdicts_path, 'a', encoding='utf-8') as _fh:
    _fh.write(verdict_line)
    _fh.write(companion_row)

print(f"  Appended canonical line: {verdict_line.strip()}")
print(f"  Appended companion row : {companion_row.strip()[:120]}...")

# ============================================================
# SECTION 12: Summary
# ============================================================
print("\n" + "=" * 78)
print(f"Summary  |  S86-CUTOFF-SQRT-GATE-C-S82-APPLICABILITY  |  {verdict}")
print("=" * 78)
print(f"  Reason             : {reason}")
print(f"  PRIMARY lambdas    : {LAMBDA_PRIMARY.tolist()}")
print(f"  STENCIL lambdas    : {LAMBDA_STENCIL.tolist()}")
print(f"  PRIMARY c_j        : [{', '.join(f'{c:+.3e}' for c in c_primary)}]")
print(f"  STENCIL c_j        : [{', '.join(f'{c:+.3e}' for c in c_stencil)}]")
print(f"  PRIMARY M[f](6)    : {M_6_pri_closed:+.6e}")
print(f"  STENCIL M[f](6)    : {M_6_sten_closed:+.6e}")
print(f"  abs_finite         : {abs_finite}")
print(f"  saturated          : {saturated}")
print(f"  HBW primary        : {hbw_primary}")
print(f"  HBW stencil        : {hbw_stencil}")
print(f"  Cross-check match  : {cross_check_sign_match}")
print(f"  audit_sha256       : {audit_sha}")
print(f"  content_sha256     : {content_sha}")
print("=" * 78)
