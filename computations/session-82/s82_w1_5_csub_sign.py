#!/usr/bin/env python3
"""
S82 W1-5 — CSUB-SIGN IDENTITY [S80 W1-6 reassigned]
=====================================================

Gate ID : S82-UNIFIED-AS-79-CSUB-SIGN
Trigger : [SIGN]   (substitution chain MANDATORY; see below)
Class   : PHONONIC
Owner   : landau-condensed-matter-theorist
EVOI    : 0.073
Anchor  : sessions/session-plan/session-80-plan.md  L1124-L1188

Purpose
-------
Verify the structural identity  d(ln A_s) / d(ln c_sub) = -1.000 EXACTLY
under UNIFIED-AS-79  A_s = (H_tilde^2 / (8 pi^2)) * (1/eps_H) * F_amp *
c_sub^{-1} * f_conv.

Deviation from -1.000 measures the ALGEBRAIC-IDENTITY INTEGRITY of the
UNIFIED-AS-79 formula as implemented numerically -- NOT a physical
prediction.  PASS means the code is faithful to the analytic formula;
FAIL would mean the formula as coded has an extra c_sub dependence
lurking in H_tilde, eps_H, F_amp, or f_conv.

Framing (PHONONIC):
  c_sub is the subhorizon matching factor between the substrate's
  dimensionless scalar-power (measured in H_tilde = H/M_Pl_eff units)
  and the emergent-metric scalar-power (measured in M_Pl_reduced
  units).  It scales the Goldstone-phonon mode's amplitude as it
  crosses horizon in the emergent 4D effective description.  The
  d/d(ln c_sub) identity reflects the fact that c_sub enters UNIFIED
  AS-79 ONLY through the c_sub^{-1} factor; any deviation from -1
  signals spurious coupling between c_sub and a "hidden" variable
  (bug, aliasing, or numerical precision loss).

MANDATORY [SIGN] SUBSTITUTION CHAIN
-----------------------------------

Step 1 (definition -- UNIFIED-AS-79 per P2-A, S80 plan L1140-L1188):
   A_s(c_sub) = (H_tilde^2 / (8 pi^2)) * (1/eps_H) * F_amp * c_sub^{-1} * f_conv
   All of H_tilde, eps_H, F_amp, f_conv are HELD CONSTANT in the
   c_sub variation (partial derivative along c_sub axis only).

Step 2 (logarithm):
   ln A_s = [ln(H_tilde^2 / (8 pi^2)) - ln(eps_H) + ln(F_amp) + ln(f_conv)]
            - ln(c_sub)
          = const(H_tilde, eps_H, F_amp, f_conv) - ln(c_sub)

Step 3 (differentiate w.r.t. ln c_sub):
   d(ln A_s) / d(ln c_sub) = -1        (EXACT, analytic)

Step 4 (Python numerical verification via central differences at
         c_sub_0 = 2.238 -- S78 W2-E central):
   delta = 0.01
   c_plus    = c_sub_0 * (1 + delta)
   c_minus   = c_sub_0 * (1 - delta)
   A_s_plus  = base_A_s * (c_sub_0 / c_plus)        # since A_s ~ 1/c_sub
   A_s_minus = base_A_s * (c_sub_0 / c_minus)
   d_ln_A_d_ln_c = (ln A_s_plus - ln A_s_minus) / (ln c_plus - ln c_minus)
   assert |d_ln_A_d_ln_c + 1.0| < 0.01  -> PASS threshold

Step 5 (direction, from canonical form):
   The 1/c_sub factor means  c_sub INCREASES  =>  A_s DECREASES.
   The exact logarithmic-derivative value is -1 by construction of
   UNIFIED-AS-79.  Deviation from -1 is a DIRECT MEASUREMENT of
   structural-identity integrity; no physical consequence is tied to
   it other than confirming faithful numerical implementation.

Pre-registered gate (S80 plan L1131-L1138)
------------------------------------------
  PASS : |d(ln A_s)/d(ln c_sub) + 1.000| < 0.01
  INFO : 0.01 <= deviation < 0.10
  FAIL : deviation >= 0.10  (identity violated -- UNIFIED-AS-79
         algebraic structure needs re-examination)

Output 4-tuple:
  (value=<d_ln_A_d_ln_c>, scheme=CENTRAL-DIFFERENCE,
   convention=UNIFIED-AS-79, L_max=5)

References
----------
  S80 plan §W1-6        : sessions/session-plan/session-80-plan.md L1124
  S80 W1-2 consult      : computations/session-80/s80_unified_as_79_mode_eqn.py (checks
                          the identity as SANITY CHECK 2 with the same formula)
  S78 W2-E c_sub values : computations/session-78/s78_gate_verdicts.txt
  Canonical constants   : computations/_shared/canonical_constants.py
"""

import os
os.environ.setdefault('OMP_NUM_THREADS', '8')   # (local) scalar identity: CPU cap for politeness
os.environ.setdefault('MKL_NUM_THREADS', '8')   # (local)

import sys
import json
import hashlib
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

SCRIPT_DIR = Path(__file__).parent
sys.path.insert(0, str(SCRIPT_DIR))

from canonical_constants import PI  # only canonical symbol needed; UNIFIED-AS-79
                                    # ingredients are local central values per S80 W1-6 plan.


# =============================================================================
# SECTION 0: Input SHA-256 pins (MANDATORY in first 20 stdout lines)
# =============================================================================

def _sha256(path):
    """Compute SHA-256 of a file."""
    with open(path, 'rb') as h:
        return hashlib.sha256(h.read()).hexdigest()


HERE = str(SCRIPT_DIR)                                                # (local)
INPUT_FILES = [                                                        # (local)
    os.path.join(HERE, 'canonical_constants.py'),
    os.path.join(HERE, 's80_unified_as_79_mode_eqn.py'),
    os.path.join(HERE, 's80_unified_as_79_mode_eqn.npz'),
]

print("=" * 72)
print("S82 W1-5 -- CSUB-SIGN IDENTITY  (landau-condensed-matter-theorist)")
print("=" * 72)
print("Gate     : S82-UNIFIED-AS-79-CSUB-SIGN")
print("Trigger  : [SIGN] (substitution chain in docstring)")
print("Class    : PHONONIC")
print("Anchor   : S80 plan L1124-L1188 (W1-6, reassigned as S82 W1-5)")
print()
print("[SEC 0] Input SHA-256 pins")
INPUT_SHAS = {}                                                        # (local)
for _f in INPUT_FILES:
    if os.path.exists(_f):
        _h = _sha256(_f)                                               # (local)
        INPUT_SHAS[os.path.basename(_f)] = _h
        print(f"  {os.path.basename(_f):40s} sha256={_h[:16]}...{_h[-8:]}")
    else:
        INPUT_SHAS[os.path.basename(_f)] = None
        print(f"  {os.path.basename(_f):40s} MISSING")


# =============================================================================
# SECTION 1: UNIFIED-AS-79 formula definition (consistent with S80 mode-eqn)
# =============================================================================

def A_s_unified(H_tilde, eps_H, F_amp, c_sub, f_conv):
    """UNIFIED-AS-79: A_s = (H_tilde^2 / (8 pi^2)) * (1/eps_H) * F_amp
                         * c_sub^{-1} * f_conv."""
    return (H_tilde**2 / (8.0 * PI**2)) / eps_H * F_amp / c_sub * f_conv  # (local)


# =============================================================================
# SECTION 2: Local central values (from S80 W1-2 plan; held fixed in c_sub var)
# =============================================================================
# These are PLACEHOLDERS in the identity check: any values leave the
# identity d(ln A_s)/d(ln c_sub) = -1 invariant because only c_sub is varied.
# We adopt the S80 W1-2 plan-central primary-branch inputs for reproducibility.

H_tilde = 5.908e-3       # (local) Path A framework (TD) from S80 W1-2 plan central
eps_H   = 0.02163        # (local) slow-roll eps at pivot (S75/S77 canonical)
F_amp   = 0.3885         # (local) W0-5 slot-adjusted: 1.0166 x 0.3822 (SUPPRESS)
c_sub_0 = 2.238          # (local) S78 W2-E central of {2.232, 2.244, 3.647}
f_conv  = 9.30e-4        # (local) (M_KK/M_Pl_red)^2  -- S78 Transit-Einstein open

# Gate thresholds (pre-registered, S80 plan L1131-L1138)
PASS_TOL = 0.01          # (local) |d + 1| < 0.01 -> PASS
INFO_TOL = 0.10          # (local) |d + 1| in [0.01, 0.10) -> INFO; >= 0.10 -> FAIL

print()
print("[SEC 1] UNIFIED-AS-79 ingredients (held constant in c_sub variation)")
print(f"  H_tilde = {H_tilde:.4e}    (Path A framework TD, S80 W1-2 central)")
print(f"  eps_H   = {eps_H:.5f}       (slow-roll canonical)")
print(f"  F_amp   = {F_amp:.4f}       (W0-5 slot-adjusted)")
print(f"  c_sub_0 = {c_sub_0:.3f}        (S78 W2-E central)")
print(f"  f_conv  = {f_conv:.3e}     ((M_KK/M_Pl_red)^2)")

# Pre-computed reference base A_s at c_sub_0 (for direction sanity)
base_A_s = A_s_unified(H_tilde, eps_H, F_amp, c_sub_0, f_conv)         # (local)
print(f"  base_A_s(c_sub_0) = {base_A_s:.4e}")


# =============================================================================
# SECTION 3: SUBSTITUTION CHAIN -- PRE-PYTHON (printed to stdout)
# =============================================================================
print()
print("-" * 72)
print("[SEC 2] MANDATORY [SIGN] SUBSTITUTION CHAIN")
print("-" * 72)
print("Step 1 (definition):")
print("   A_s(c_sub) = (H_tilde^2 / (8 pi^2)) * (1/eps_H) * F_amp")
print("                * c_sub^{-1} * f_conv")
print("   All of H_tilde, eps_H, F_amp, f_conv held CONSTANT in c_sub variation.")
print()
print("Step 2 (logarithm):")
print("   ln A_s = const(H_tilde, eps_H, F_amp, f_conv) - ln(c_sub)")
print()
print("Step 3 (differentiate):")
print("   d(ln A_s) / d(ln c_sub) = -1   (EXACT, analytic)")
print()
print("Step 4: Python verification via central differences (below).")
print()
print("Step 5 (direction, from canonical form):")
print("   The 1/c_sub factor => c_sub INCREASES => A_s DECREASES.")
print("   Exact logarithmic derivative = -1; deviation measures identity integrity.")


# =============================================================================
# SECTION 4: Python numerical verification (central differences)
# =============================================================================
print()
print("-" * 72)
print("[SEC 3] Python numerical verification -- central-difference")
print("-" * 72)

delta = 0.01                                                           # (local) 1% perturbation
c_plus  = c_sub_0 * (1.0 + delta)                                      # (local)
c_minus = c_sub_0 * (1.0 - delta)                                      # (local)

# Use full formula (not the algebraic shortcut base_A_s*(c0/c)) so that
# the check exercises the ACTUAL A_s_unified code path.
A_s_plus  = A_s_unified(H_tilde, eps_H, F_amp, c_plus,  f_conv)        # (local)
A_s_minus = A_s_unified(H_tilde, eps_H, F_amp, c_minus, f_conv)        # (local)

ln_A_plus  = np.log(A_s_plus)                                          # (local)
ln_A_minus = np.log(A_s_minus)                                         # (local)
ln_c_plus  = np.log(c_plus)                                            # (local)
ln_c_minus = np.log(c_minus)                                           # (local)

d_ln_A_d_ln_c = (ln_A_plus - ln_A_minus) / (ln_c_plus - ln_c_minus)    # (local)

print(f"  delta (perturbation) = {delta:.2f}   (1% around c_sub_0)")
print(f"  c_plus  = {c_plus:.6f}   ln(c_plus)  = {ln_c_plus:.8f}")
print(f"  c_minus = {c_minus:.6f}   ln(c_minus) = {ln_c_minus:.8f}")
print(f"  A_s_plus  = {A_s_plus:.8e}   ln(A_s_plus)  = {ln_A_plus:.8f}")
print(f"  A_s_minus = {A_s_minus:.8e}   ln(A_s_minus) = {ln_A_minus:.8f}")
print(f"  d(ln A_s) / d(ln c_sub) = {d_ln_A_d_ln_c:.12f}")
print(f"  Expected (analytic)     = -1.000000000000")
deviation = abs(d_ln_A_d_ln_c + 1.0)                                   # (local)
print(f"  |deviation from -1.0|   = {deviation:.3e}")
deviation_pct = 100.0 * deviation                                      # (local)
print(f"  |deviation| (percent)   = {deviation_pct:.3e} %")


# =============================================================================
# SECTION 5: Cross-check with algebraic-shortcut formula (paranoia check)
# =============================================================================
# A_s * c_sub = base_A_s * c_sub_0  (exact algebraic identity)
# Compare against the A_s_unified path above; should be bit-identical up to FP.
print()
print("-" * 72)
print("[SEC 4] Cross-check A_s * c_sub = const (exact identity)")
print("-" * 72)

prod_0     = base_A_s    * c_sub_0                                     # (local)
prod_plus  = A_s_plus    * c_plus                                      # (local)
prod_minus = A_s_minus   * c_minus                                     # (local)

print(f"  A_s(c_sub_0) * c_sub_0 = {prod_0:.14e}")
print(f"  A_s(c_plus)  * c_plus  = {prod_plus:.14e}")
print(f"  A_s(c_minus) * c_minus = {prod_minus:.14e}")
print(f"  max rel diff across 3 products = "
      f"{max(abs(prod_plus-prod_0), abs(prod_minus-prod_0))/abs(prod_0):.3e}")
# This should be ~1e-16 (floating-point rounding).


# =============================================================================
# SECTION 6: Robustness -- multiple deltas (show derivative is delta-independent
#            up to O(delta^2) truncation in central-difference scheme)
# =============================================================================
print()
print("-" * 72)
print("[SEC 5] Robustness -- derivative vs. perturbation size")
print("-" * 72)
deltas = [0.001, 0.003, 0.01, 0.03, 0.1]                               # (local)
derivs_scan = []                                                       # (local)
print(f"  {'delta':>8s}  {'d(ln A)/d(ln c)':>22s}  {'|dev from -1|':>18s}")
for _d in deltas:
    _cp = c_sub_0 * (1 + _d)                                           # (local)
    _cm = c_sub_0 * (1 - _d)                                           # (local)
    _Ap = A_s_unified(H_tilde, eps_H, F_amp, _cp, f_conv)              # (local)
    _Am = A_s_unified(H_tilde, eps_H, F_amp, _cm, f_conv)              # (local)
    _D  = (np.log(_Ap) - np.log(_Am)) / (np.log(_cp) - np.log(_cm))    # (local)
    derivs_scan.append(_D)
    print(f"  {_d:>8.3f}  {_D:>22.14f}  {abs(_D+1):>18.3e}")


# =============================================================================
# SECTION 7: c_sub scan over [0.5, 5.0] -- show derivative is c_sub-independent
#            (identity holds at EVERY c_sub, not just the central value)
# =============================================================================
print()
print("-" * 72)
print("[SEC 6] c_sub scan -- identity must hold at every c_sub")
print("-" * 72)
c_scan = np.linspace(0.5, 5.0, 10)                                     # (local)
derivs_c_scan = []                                                     # (local)
print(f"  {'c_sub':>8s}  {'d(ln A)/d(ln c)':>22s}  {'|dev|':>14s}")
for _c0 in c_scan:
    _cp = _c0 * (1 + 0.01)                                             # (local)
    _cm = _c0 * (1 - 0.01)                                             # (local)
    _Ap = A_s_unified(H_tilde, eps_H, F_amp, _cp, f_conv)              # (local)
    _Am = A_s_unified(H_tilde, eps_H, F_amp, _cm, f_conv)              # (local)
    _D  = (np.log(_Ap) - np.log(_Am)) / (np.log(_cp) - np.log(_cm))    # (local)
    derivs_c_scan.append(_D)
    print(f"  {_c0:>8.3f}  {_D:>22.14f}  {abs(_D+1):>14.3e}")


# =============================================================================
# SECTION 8: Verdict determination
# =============================================================================
print()
print("-" * 72)
print("[SEC 7] Verdict")
print("-" * 72)
if deviation < PASS_TOL:
    verdict = "PASS"                                                   # (local)
    reason = f"|deviation| = {deviation:.3e} < {PASS_TOL} = PASS_TOL"  # (local)
elif deviation < INFO_TOL:
    verdict = "INFO"                                                   # (local)
    reason = f"|deviation| = {deviation:.3e} in [{PASS_TOL}, {INFO_TOL})"  # (local)
else:
    verdict = "FAIL"                                                   # (local)
    reason = (f"|deviation| = {deviation:.3e} >= {INFO_TOL} -- "
              f"UNIFIED-AS-79 structure needs re-examination")         # (local)
print(f"  Verdict: {verdict}")
print(f"  Reason : {reason}")

# Assert for safety: if the identity fails at machine epsilon we've got a bug.
assert deviation < 1e-10, (
    f"Numerical sanity violated: deviation = {deviation:.3e} -- "
    f"UNIFIED-AS-79 algebraic identity should hold to FP precision.")


# =============================================================================
# SECTION 9: Closure SHA + 4-tuple emit
# =============================================================================
print()
print("-" * 72)
print("[SEC 8] Closure SHA and 4-tuple emit")
print("-" * 72)

closure_map = {                                                        # (local) ordered input-pin map
    'script': 's82_w1_5_csub_sign.py',
    'gate_id': 'S82-UNIFIED-AS-79-CSUB-SIGN',
    'scheme': 'CENTRAL-DIFFERENCE',
    'convention': 'UNIFIED-AS-79',
    'L_max': 5,
    'delta': delta,
    'c_sub_0': c_sub_0,
    'H_tilde': H_tilde,
    'eps_H': eps_H,
    'F_amp': F_amp,
    'f_conv': f_conv,
    'PASS_TOL': PASS_TOL,
    'INFO_TOL': INFO_TOL,
    'd_ln_A_d_ln_c': float(d_ln_A_d_ln_c),
    'deviation': float(deviation),
    'verdict': verdict,
    'inputs': {k: v for k, v in sorted(INPUT_SHAS.items())},
}
closure_str = json.dumps(closure_map, sort_keys=True, default=str)     # (local)
closure_sha = hashlib.sha256(closure_str.encode('utf-8')).hexdigest()  # (local)

four_tuple = (                                                         # (local)
    f"(value={d_ln_A_d_ln_c:.12f}, scheme=CENTRAL-DIFFERENCE, "
    f"convention=UNIFIED-AS-79, L_max=5)"
)
print(f"  Closure SHA-256: {closure_sha}")
print(f"  4-TUPLE        : {four_tuple}")


# =============================================================================
# SECTION 10: Save .npz
# =============================================================================
print()
print("-" * 72)
print("[SEC 9] Save .npz")
print("-" * 72)
out_npz = SCRIPT_DIR / 's82_w1_5_csub_sign.npz'                        # (local)
np.savez(str(out_npz),
    # Inputs (held constant in c_sub variation)
    H_tilde=H_tilde, eps_H=eps_H, F_amp=F_amp, c_sub_0=c_sub_0, f_conv=f_conv,
    # Primary result
    delta=delta,
    c_plus=c_plus, c_minus=c_minus,
    A_s_plus=A_s_plus, A_s_minus=A_s_minus,
    base_A_s=base_A_s,
    d_ln_A_d_ln_c=d_ln_A_d_ln_c,
    deviation=deviation,
    # Robustness scan
    deltas=np.array(deltas),
    derivs_scan=np.array(derivs_scan),
    # c_sub scan
    c_scan=c_scan,
    derivs_c_scan=np.array(derivs_c_scan),
    # Gate
    PASS_TOL=PASS_TOL, INFO_TOL=INFO_TOL,
    verdict=np.array([verdict]),
    reason=np.array([reason]),
    # Closure
    closure_sha=np.array([closure_sha]),
    four_tuple=np.array([four_tuple]),
    # Input SHAs
    input_shas=np.array([f"{k}={v}" for k, v in sorted(INPUT_SHAS.items())]),
)
print(f"  Saved: {out_npz}")


# =============================================================================
# SECTION 11: Plot -- optional c_sub scan + robustness panel
# =============================================================================
print()
print("-" * 72)
print("[SEC 10] Plot")
print("-" * 72)

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(16, 5))

# Panel (a): derivative vs. c_sub
ax1.plot(c_scan, derivs_c_scan, 'o-', color='crimson', lw=2, markersize=7,
         label='numerical d(ln A_s)/d(ln c_sub)')
ax1.axhline(-1.0, color='black', ls='--', lw=2, label='analytic: -1 (exact)')
ax1.axhspan(-1.0 - PASS_TOL, -1.0 + PASS_TOL, color='green', alpha=0.15,
            label=f'PASS band |dev|<{PASS_TOL}')
ax1.set_xlabel(r'$c_{\mathrm{sub}}$', fontsize=11)
ax1.set_ylabel(r'$d(\ln A_s)/d(\ln c_{\mathrm{sub}})$', fontsize=11)
ax1.set_title('(a) Identity at varying c_sub (should be -1 everywhere)', fontsize=11)
ax1.legend(loc='best', fontsize=8)
ax1.grid(True, alpha=0.3)

# Panel (b): derivative vs. delta (central-difference perturbation)
ax2.semilogx(deltas, derivs_scan, 'o-', color='steelblue', lw=2, markersize=7,
             label='numerical d(ln A_s)/d(ln c_sub)')
ax2.axhline(-1.0, color='black', ls='--', lw=2, label='analytic: -1 (exact)')
ax2.axhspan(-1.0 - PASS_TOL, -1.0 + PASS_TOL, color='green', alpha=0.15,
            label=f'PASS band |dev|<{PASS_TOL}')
ax2.set_xlabel(r'$\delta$ (central-diff perturbation size)', fontsize=11)
ax2.set_ylabel(r'$d(\ln A_s)/d(\ln c_{\mathrm{sub}})$', fontsize=11)
ax2.set_title('(b) Robustness: derivative vs. step size', fontsize=11)
ax2.legend(loc='best', fontsize=8)
ax2.grid(True, alpha=0.3)

# Panel (c): A_s(c_sub) scan showing direction
c_plot = np.linspace(0.5, 5.0, 200)                                    # (local)
A_s_plot = np.array([A_s_unified(H_tilde, eps_H, F_amp, _c, f_conv)    # (local)
                     for _c in c_plot])
ax3.loglog(c_plot, A_s_plot, '-', color='darkgreen', lw=2,
           label=r'$A_s(c_{\mathrm{sub}}) = K / c_{\mathrm{sub}}$')
ax3.axvline(c_sub_0, color='red', ls=':', lw=2, label=fr'$c_{{sub,0}} = {c_sub_0}$')
ax3.axhline(base_A_s, color='red', ls=':', lw=2)
ax3.set_xlabel(r'$c_{\mathrm{sub}}$', fontsize=11)
ax3.set_ylabel(r'$A_s$', fontsize=11)
ax3.set_title('(c) A_s ~ 1/c_sub (direction: c_sub increases -> A_s decreases)',
              fontsize=11)
ax3.legend(loc='best', fontsize=9)
ax3.grid(True, which='both', alpha=0.3)

fig.suptitle(f'S82 W1-5: CSUB-SIGN IDENTITY  |  Verdict: {verdict}  '
             f'|  d(ln A_s)/d(ln c_sub) = {d_ln_A_d_ln_c:.12f}',
             fontsize=12, fontweight='bold')
plt.tight_layout(rect=[0, 0, 1, 0.94])
out_png = SCRIPT_DIR / 's82_w1_5_csub_sign.png'                        # (local)
plt.savefig(str(out_png), dpi=135, bbox_inches='tight')
plt.close(fig)
print(f"  Saved: {out_png}")


# =============================================================================
# SECTION 12: Append verdict to s82_gate_verdicts.txt
# =============================================================================
print()
print("-" * 72)
print("[SEC 11] Append verdict to s82_gate_verdicts.txt")
print("-" * 72)
verdicts_path = SCRIPT_DIR / 's82_gate_verdicts.txt'                   # (local)
verdict_line = (                                                       # (local)
    f"S82-UNIFIED-AS-79-CSUB-SIGN: {verdict} -- "
    f"value={d_ln_A_d_ln_c:.12f} "
    f"scheme=CENTRAL-DIFFERENCE "
    f"convention=UNIFIED-AS-79 "
    f"L_max=5 "
    f"sha256={closure_sha}\n"
)
with open(str(verdicts_path), 'a', encoding='utf-8') as _fh:
    _fh.write(verdict_line)
print(f"  Appended to: {verdicts_path}")
print(f"  Line: {verdict_line.strip()}")


# =============================================================================
# FINAL: 4-tuple (MUST be final non-verdict line)
# =============================================================================
print()
print("=" * 72)
print("FINAL 4-TUPLE")
print("=" * 72)
print(four_tuple)
