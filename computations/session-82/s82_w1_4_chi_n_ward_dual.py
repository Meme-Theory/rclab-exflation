#!/usr/bin/env python3
"""
S82 W1-4: CHI-N-WARD-DUAL (rank-2 fallback spectral-measure functional)
========================================================================

Gate: S82-CHI-N-WARD-DUAL [VERIFY]
Classification: PARTICLE
  - W(tau) is a selection-rule / gauge-invariant diagnostic for substrate
    U(1)_EM. Its scale is controlled by the fourth Seeley-DeWitt moment
    (gauge kinetic term).
  - chi_N(tau) is a topological Euler-characteristic readout built as the
    alternating sum of spectral-measure moments of D_K.

Owner: gen-physicist
EVOI: 0.074
S82 plan anchor: reassigned from S80 L1087-L1122 (W1-5 in S80 plan).

HYPOTHESIS
----------
A rank-2 dual functional chi_N(tau) * W(tau) is constant under
tau-variation (Ward identity, substrate U(1)_EM gauge structure) and
serves as a fallback §VII.II functional if primary Fold Transit Event
candidates are marginal.

PRE-REGISTERED GATE
-------------------
Compute chi_N(tau), W(tau) at tau in {0.15, 0.19, 0.25}.
Measure: pct_var = 100 * (max(Pi) - min(Pi)) / mean(Pi)
  PASS: pct_var < 5%   (Ward-duality confirmed)
  INFO: 5% <= pct_var < 20%
  FAIL: pct_var >= 20%

--------------------------------------------------------------------
SUBSTITUTION CHAIN [VERIFY] (mandatory per math-scripts.md)
--------------------------------------------------------------------

Step 1 - chi_N definition (rank-2 spectral-measure Euler character):
  mu_0(tau) = a_0(tau)      volume / mode count
  mu_1(tau) = a_2(tau)      scalar-curvature moment
  mu_2(tau) = a_4(tau)      Gauss-Bonnet / gauge kinetic moment
  a_k(tau)  = 0.5 * sum_{|lam|>cutoff} d_n * |lam_n|^{-k}    (S73B half-spectrum)
  chi_N(tau)  = mu_0 - mu_1 + mu_2  =  a_0 - a_2 + a_4

Step 2 - W(tau) definition (Ward functional, U(1)_EM sector):
  W(tau) = g_U1(tau)^2 * sqrt(a_4(tau) / a_2(tau))
  g_U1(tau)^2 = g_U1_fold * exp(-2*(tau - tau_fold))   (canonical S22a)

Step 3 - Product:
  Pi(tau) = chi_N(tau) * W(tau)
         = [a_0 - a_2 + a_4] * g_U1_fold * exp(-2(tau - tau_fold)) * sqrt(a_4/a_2)

Step 4 - Ward-duality hypothesis:
  Pi(tau) = constant  <=>  dPi/dtau = 0 identically

Step 5 - Direction of d(Pi)/d(tau) is an OUTPUT of the tau sweep, not
  an input claim.  Two competing sign drivers:
    (a) exp(-2(tau - tau_fold))  decreases with tau (negative driver)
    (b) chi_N = a_0 - a_2 + a_4 changes under Jensen; sign not pinned.
  The pre-registered gate tests VARIANCE, not direction.  Direction of
  the variance (increasing / decreasing Pi(tau) across {0.15, 0.19, 0.25})
  is reported as diagnostic only.

--------------------------------------------------------------------
STRUCTURAL CAVEAT
--------------------------------------------------------------------
S22c established chi(SU(3) group manifold) = 0 (Gauss-Bonnet topological
invariant).  chi_N HERE is the alternating sum of spectral-measure
moments of D_K, NOT the group-manifold Euler characteristic.  It is a
1-parameter family in tau (Jensen deformation) and is non-vanishing.
This is a "spectral Euler characteristic" in the McKean-Singer sense
applied to truncated Laplace-moment towers.

--------------------------------------------------------------------
S82 DISCIPLINE (delta from S80)
--------------------------------------------------------------------
  - First-20-stdout-line SHA-256 input pins for every file read
  - 64-char SHA closure emitted via JSON-sorted ordered input-pin map
  - 4-tuple (value=..., scheme=..., convention=..., L_max=...) final line
  - Verdict file line follows S82 canonical form:
      S82-CHI-N-WARD-DUAL: PASS|FAIL|INFO -- value=<pct_var> scheme=... ...
  - Canonical constants imported; every intermediate tagged # (local)
"""

import os
# CPU thread cap (must precede numpy import). 6x6/8x8 matrices do not
# benefit from GPU; stay on CPU with conservative thread count.
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import sys
import time
import hashlib
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))             # (local)
sys.path.insert(0, SCRIPT_DIR)
os.chdir(SCRIPT_DIR)

# ============================================================
# SECTION 0: Input SHA-256 pins (MANDATORY in first 20 lines)
# ============================================================
def _sha256(path):
    """Compute SHA-256 of a file (full 64-char hexdigest)."""
    with open(path, 'rb') as h:
        return hashlib.sha256(h.read()).hexdigest()


INPUT_FILES = [                                                     # (local)
    os.path.join(SCRIPT_DIR, 'canonical_constants.py'),
    os.path.join(SCRIPT_DIR, 'dirac_spectrum.py'),
    os.path.join(SCRIPT_DIR, 's80_chi_N_ward_dual.py'),
    os.path.join(SCRIPT_DIR, 's80_chi_N_ward_dual.npz'),
]

print("=" * 78)
print("S82 W1-4: CHI-N-WARD-DUAL (rank-2 spectral-measure functional)")
print("=" * 78)
print("[SEC 0] Input SHA-256 pins")
INPUT_SHAS = {}                                                     # (local)
for _f in INPUT_FILES:
    if os.path.exists(_f):
        _h = _sha256(_f)                                            # (local)
        INPUT_SHAS[os.path.basename(_f)] = _h
        print(f"  {os.path.basename(_f):32s} sha256={_h[:16]}...{_h[-8:]}")
    else:
        INPUT_SHAS[os.path.basename(_f)] = None
        print(f"  {os.path.basename(_f):32s} MISSING")

# Now imports (verified present by SHA pins above)
from canonical_constants import (
    tau_fold,
    a0_fold,
    a2_fold,
    a4_fold,
    g_U1_fold,
)
from dirac_spectrum import (
    su3_generators,
    compute_structure_constants,
    collect_spectrum,
    build_cliff8,
)

print()
print(f"  Canonical anchors (imported):")
print(f"    tau_fold    = {tau_fold}")
print(f"    a0_fold     = {a0_fold}")
print(f"    a2_fold     = {a2_fold}")
print(f"    a4_fold     = {a4_fold}")
print(f"    g_U1_fold^2 = {g_U1_fold}")
print()

# ============================================================
# SECTION 1: Configuration (machinery pin, PRDR)
# ============================================================
# Coarse gate grid (pre-registered)
TAU_COARSE = np.array([0.15, 0.19, 0.25])                           # (local)

# Fine grid (diagnostic; van-Hove sanity check only, not a gate input)
TAU_FINE = np.arange(0.10, 0.281, 0.02)                             # (local)

# Union for computation
TAU_ALL = np.unique(np.concatenate(
    [TAU_COARSE, TAU_FINE, [tau_fold]]
))                                                                  # (local)

# Peter-Weyl truncation (canonical L_max=3)
MAX_PQ_SUM = 3                                                      # (local)
EVAL_CUTOFF = 0.01                                                  # (local)

# Gate thresholds (pre-registered, from task spec)
PASS_THRESH = 5.0                                                   # (local) percent
INFO_THRESH = 20.0                                                  # (local) percent

print("[SEC 1] Configuration (machinery pin, PRDR)")
print(f"  L_max (max_pq_sum)    = {MAX_PQ_SUM}")
print(f"  Eigenvalue cutoff     = {EVAL_CUTOFF}")
print(f"  Coarse tau grid       = {TAU_COARSE}")
print(f"  Fine tau grid         = {TAU_FINE}")
print(f"  Union grid size       = {len(TAU_ALL)}")
print(f"  PASS threshold        = {PASS_THRESH}% variation")
print(f"  INFO threshold        = {INFO_THRESH}% variation")
print()

# ============================================================
# SECTION 2: Build SU(3) algebraic infrastructure once
# ============================================================
print("[SEC 2] BUILD SU(3) INFRASTRUCTURE")
gens = su3_generators()                                             # (local)
f_abc = compute_structure_constants(gens)                           # (local)
gammas = build_cliff8()                                             # (local)
print("  8 su(3) anti-Hermitian generators, structure constants, Clifford-8 built.")
print()


# ============================================================
# SECTION 3: Spectral-moment computation
# ============================================================
def compute_moments_at_tau(tau_val):
    """Compute a_0, a_2, a_4 in S73B half-spectrum convention at tau."""
    all_evals, eval_data = collect_spectrum(
        tau_val, gens, f_abc, gammas, max_pq_sum=MAX_PQ_SUM, verbose=False
    )
    abs_vals_local = []                                             # (local)
    mults_local = []                                                # (local)
    for ev, mult in all_evals:
        aev = abs(ev)                                               # (local)
        if aev > EVAL_CUTOFF:
            abs_vals_local.append(aev)
            mults_local.append(mult)
    abs_vals_arr = np.array(abs_vals_local)                         # (local)
    mults_arr = np.array(mults_local, dtype=np.float64)             # (local)
    a0 = 0.5 * float(np.sum(mults_arr))                             # (local) S73B half
    a2 = 0.5 * float(np.sum(mults_arr / abs_vals_arr**2))           # (local)
    a4 = 0.5 * float(np.sum(mults_arr / abs_vals_arr**4))           # (local)
    return {
        'tau': tau_val,
        'a0': a0,
        'a2': a2,
        'a4': a4,
        'n_evals': len(abs_vals_arr),
        'lam_min': float(np.min(abs_vals_arr)),
        'lam_max': float(np.max(abs_vals_arr)),
    }


# ============================================================
# SECTION 4: tau sweep - compute spectral moments
# ============================================================
print("[SEC 3] TAU SWEEP: compute a_0, a_2, a_4 at each tau")
results = []                                                        # (local)
t_start = time.time()                                               # (local)
for i, tau_val in enumerate(TAU_ALL):
    t0 = time.time()                                                # (local)
    r = compute_moments_at_tau(tau_val)                             # (local)
    dt_step = time.time() - t0                                      # (local)
    results.append(r)
    print(f"  [{i+1:2d}/{len(TAU_ALL)}] tau={tau_val:.4f}: "
          f"a0={r['a0']:.1f}, a2={r['a2']:.3f}, a4={r['a4']:.4f}, "
          f"n_evals={r['n_evals']}, dt={dt_step:.1f}s")
t_total = time.time() - t_start                                     # (local)
print(f"  Total sweep time: {t_total:.1f}s")
print()

# ============================================================
# SECTION 5: Canonical anchor verification (tau=0.19)
# ============================================================
tau_arr_full = np.array([r['tau'] for r in results])                # (local)
a0_arr = np.array([r['a0'] for r in results])                       # (local)
a2_arr = np.array([r['a2'] for r in results])                       # (local)
a4_arr = np.array([r['a4'] for r in results])                       # (local)

idx_fold = int(np.argmin(np.abs(tau_arr_full - tau_fold)))          # (local)
a0_check = a0_arr[idx_fold]                                         # (local)
a2_check = a2_arr[idx_fold]                                         # (local)
a4_check = a4_arr[idx_fold]                                         # (local)

print("[SEC 4] CANONICAL ANCHOR VERIFICATION (tau=0.19)")
print(f"  a_0 computed = {a0_check:.3f}   canonical = {a0_fold:.3f}"
      f"   drift = {100*(a0_check/a0_fold - 1):+.3f}%")
print(f"  a_2 computed = {a2_check:.3f}   canonical = {a2_fold:.3f}"
      f"   drift = {100*(a2_check/a2_fold - 1):+.3f}%")
print(f"  a_4 computed = {a4_check:.3f}   canonical = {a4_fold:.3f}"
      f"   drift = {100*(a4_check/a4_fold - 1):+.3f}%")
print()

# ============================================================
# SECTION 6: Form chi_N(tau) = a_0(tau) - a_2(tau) + a_4(tau)
# ============================================================
print("[SEC 5] chi_N(tau) = a_0 - a_2 + a_4 (spectral Euler-characteristic)")
chi_N_arr = a0_arr - a2_arr + a4_arr                                # (local)
chi_N_fold = float(chi_N_arr[idx_fold])                             # (local)
print(f"  chi_N at tau_fold = {chi_N_fold:.4f}")
print()

# ============================================================
# SECTION 7: Form W(tau) = g_U1(tau)^2 * sqrt(a_4/a_2)
# ============================================================
print("[SEC 6] W(tau) = g_U1(tau)^2 * sqrt(a_4/a_2)")
g_U1_sq_arr = g_U1_fold * np.exp(-2.0 * (tau_arr_full - tau_fold))  # (local)
sqrt_ratio = np.sqrt(a4_arr / a2_arr)                               # (local)
W_arr = g_U1_sq_arr * sqrt_ratio                                    # (local)
W_fold = float(W_arr[idx_fold])                                     # (local)
print(f"  W at tau_fold = {W_fold:.6f}")
print()

# ============================================================
# SECTION 8: Form product Pi(tau) = chi_N(tau) * W(tau)
# ============================================================
print("[SEC 7] Pi(tau) = chi_N(tau) * W(tau)")
Pi_arr = chi_N_arr * W_arr                                          # (local)
Pi_fold = float(Pi_arr[idx_fold])                                   # (local)
print(f"  Pi at tau_fold = {Pi_fold:.4f}")
print()

# ============================================================
# SECTION 9: tau table (coarse + all)
# ============================================================
print("[SEC 8] tau-table: chi_N, W, Pi (all grid points)")
print(f"  {'tau':>6s} | {'a_0':>10s} | {'a_2':>10s} | {'a_4':>10s} | "
      f"{'chi_N':>12s} | {'W':>11s} | {'Pi':>13s}")
print("  " + "-" * 90)
for i in range(len(tau_arr_full)):
    mark = "  <-- fold" if abs(tau_arr_full[i] - tau_fold) < 1e-4 else ""
    print(f"  {tau_arr_full[i]:>6.4f} | {a0_arr[i]:>10.3f} | {a2_arr[i]:>10.3f} | "
          f"{a4_arr[i]:>10.4f} | {chi_N_arr[i]:>12.4f} | {W_arr[i]:>11.6f} | "
          f"{Pi_arr[i]:>13.4f}{mark}")
print()

# ============================================================
# SECTION 10: PRE-REGISTERED GATE TEST (coarse grid)
# ============================================================
print("[SEC 9] PRE-REGISTERED GATE TEST (tau in {0.15, 0.19, 0.25})")
coarse_idx = []                                                     # (local)
for t_c in TAU_COARSE:
    coarse_idx.append(int(np.argmin(np.abs(tau_arr_full - t_c))))
coarse_idx = np.array(coarse_idx)                                   # (local)
tau_coarse_actual = tau_arr_full[coarse_idx]                        # (local)
chi_N_coarse = chi_N_arr[coarse_idx]                                # (local)
W_coarse = W_arr[coarse_idx]                                        # (local)
Pi_coarse = Pi_arr[coarse_idx]                                      # (local)

print(f"  {'tau':>6s} | {'chi_N':>12s} | {'W':>11s} | {'Pi':>13s}")
print("  " + "-" * 52)
for i in range(len(TAU_COARSE)):
    print(f"  {tau_coarse_actual[i]:>6.4f} | {chi_N_coarse[i]:>12.4f} | "
          f"{W_coarse[i]:>11.6f} | {Pi_coarse[i]:>13.4f}")

Pi_max_coarse = float(np.max(Pi_coarse))                            # (local)
Pi_min_coarse = float(np.min(Pi_coarse))                            # (local)
Pi_mean_coarse = float(np.mean(Pi_coarse))                          # (local)
pct_var_coarse = 100.0 * (Pi_max_coarse - Pi_min_coarse) / Pi_mean_coarse  # (local)

print()
print(f"  max(Pi)   = {Pi_max_coarse:.4f}")
print(f"  min(Pi)   = {Pi_min_coarse:.4f}")
print(f"  mean(Pi)  = {Pi_mean_coarse:.4f}")
print(f"  pct_var   = (max-min)/mean = {pct_var_coarse:.4f}%")
print()

# Diagnostic: direction of Pi(tau) across coarse grid (INFO only)
# Substitution chain for direction claim (computed via Python; see header):
#   Pi(0.25) - Pi(0.15) sign IS the direction across the coarse range.
Pi_slope_coarse = float(Pi_coarse[-1] - Pi_coarse[0])               # (local) Pi at 0.25 - Pi at 0.15
if Pi_slope_coarse > 0:
    direction_diag = "INCREASING"                                   # (local)
elif Pi_slope_coarse < 0:
    direction_diag = "DECREASING"                                   # (local)
else:
    direction_diag = "FLAT"                                         # (local)
print(f"  [diagnostic] Pi(0.25) - Pi(0.15) = {Pi_slope_coarse:+.4f}  "
      f"=> Pi is {direction_diag} across coarse grid")
print("  (direction is diagnostic only; gate tests variance, not sign)")
print()

# ============================================================
# SECTION 11: GATE VERDICT
# ============================================================
if pct_var_coarse < PASS_THRESH:
    verdict = "PASS"                                                # (local)
    explanation = (
        f"chi_N*W varies {pct_var_coarse:.3f}% across coarse grid "
        f"(< {PASS_THRESH}%) -- Ward duality confirmed; "
        f"rank-2 functional qualifies as VII.II fallback."
    )                                                               # (local)
elif pct_var_coarse < INFO_THRESH:
    verdict = "INFO"                                                # (local)
    explanation = (
        f"chi_N*W varies {pct_var_coarse:.3f}% across coarse grid "
        f"(in [{PASS_THRESH}%, {INFO_THRESH}%)) -- partial Ward "
        f"signature; fallback status indeterminate."
    )                                                               # (local)
else:
    verdict = "FAIL"                                                # (local)
    explanation = (
        f"chi_N*W varies {pct_var_coarse:.3f}% across coarse grid "
        f"(>= {INFO_THRESH}%) -- no Ward duality; rank-2 functional "
        f"rejected as VII.II fallback."
    )                                                               # (local)
print(f"  VERDICT: {verdict}")
print(f"  {explanation}")
print()

# ============================================================
# SECTION 12: Diagnostic (secondary) -- fine-grid van-Hove check
# ============================================================
print("[SEC 10] DIAGNOSTIC: fine-grid van-Hove check (NOT gate input)")
fine_idx = []                                                       # (local)
for t_f in TAU_FINE:
    fine_idx.append(int(np.argmin(np.abs(tau_arr_full - t_f))))
fine_idx = np.array(fine_idx)                                       # (local)
tau_fine_actual = tau_arr_full[fine_idx]                            # (local)
chi_N_fine = chi_N_arr[fine_idx]                                    # (local)

# Local extrema on fine interior
local_extrema = []                                                  # (local)
for i in range(1, len(chi_N_fine) - 1):
    if chi_N_fine[i] > chi_N_fine[i-1] and chi_N_fine[i] > chi_N_fine[i+1]:
        local_extrema.append(('MAX', float(tau_fine_actual[i]), float(chi_N_fine[i])))
    elif chi_N_fine[i] < chi_N_fine[i-1] and chi_N_fine[i] < chi_N_fine[i+1]:
        local_extrema.append(('MIN', float(tau_fine_actual[i]), float(chi_N_fine[i])))

VAN_HOVE_DTAU = 0.02                                                # (local)
van_hove_cands = [                                                  # (local)
    (k, t, v) for (k, t, v) in local_extrema
    if abs(t - tau_fold) <= VAN_HOVE_DTAU
]
van_hove_qualify = (len(van_hove_cands) > 0)                        # (local)
print(f"  Interior extrema on fine grid: {len(local_extrema)}")
for kind, t_e, v_e in local_extrema:
    print(f"    {kind} at tau={t_e:.4f}, chi_N={v_e:.4f}, "
          f"|delta_to_fold|={abs(t_e - tau_fold):.4f}")
print(f"  Van-Hove qualification (interior extremum within "
      f"|dtau|<={VAN_HOVE_DTAU} of fold): {van_hove_qualify}")
print()

# ============================================================
# SECTION 13: Closure SHA + 4-tuple (S82 canonical emit)
# ============================================================
print("[SEC 11] Closure SHA-256 and 4-tuple emit")
closure_map = {                                                     # (local) ordered input-pin map
    'script': 's82_w1_4_chi_n_ward_dual.py',
    'MAX_PQ_SUM': MAX_PQ_SUM,
    'EVAL_CUTOFF': EVAL_CUTOFF,
    'TAU_COARSE': TAU_COARSE.tolist(),
    'TAU_FINE': TAU_FINE.tolist(),
    'PASS_THRESH': PASS_THRESH,
    'INFO_THRESH': INFO_THRESH,
    'scheme': 'WARD-DUAL',
    'convention': 'EUCLIDEAN',
    'a0_fold': a0_fold,
    'a2_fold': a2_fold,
    'a4_fold': a4_fold,
    'g_U1_fold': g_U1_fold,
    'tau_fold': tau_fold,
    'pct_var_coarse': float(pct_var_coarse),
    'Pi_coarse': Pi_coarse.tolist(),
    'chi_N_fold': chi_N_fold,
    'W_fold': W_fold,
    'inputs': {k: v for k, v in sorted(INPUT_SHAS.items())},
}
closure_str = json.dumps(closure_map, sort_keys=True, default=str)  # (local)
closure_sha = hashlib.sha256(closure_str.encode('utf-8')).hexdigest()  # (local)

four_tuple = (                                                      # (local)
    f"(value={pct_var_coarse:.4f}%, scheme=WARD-DUAL, "
    f"convention=EUCLIDEAN, L_max={MAX_PQ_SUM})"
)
print(f"  Closure SHA-256: {closure_sha}")
print(f"  4-TUPLE: {four_tuple}")
print()

# ============================================================
# SECTION 14: Save NPZ
# ============================================================
print("[SEC 12] Save outputs")
out_npz = os.path.join(SCRIPT_DIR, "s82_w1_4_chi_n_ward_dual.npz")  # (local)
np.savez(
    out_npz,
    tau_all=tau_arr_full,
    a0=a0_arr,
    a2=a2_arr,
    a4=a4_arr,
    g_U1_sq=g_U1_sq_arr,
    sqrt_a4_over_a2=sqrt_ratio,
    chi_N=chi_N_arr,
    W=W_arr,
    Pi=Pi_arr,
    tau_coarse=tau_coarse_actual,
    chi_N_coarse=chi_N_coarse,
    W_coarse=W_coarse,
    Pi_coarse=Pi_coarse,
    tau_fine=tau_fine_actual,
    chi_N_fine=chi_N_fine,
    pct_var_coarse=pct_var_coarse,
    Pi_slope_coarse=Pi_slope_coarse,
    direction_diag=np.array([direction_diag]),
    verdict=np.array([verdict]),
    explanation=np.array([explanation]),
    closure_sha=np.array([closure_sha]),
    four_tuple=np.array([four_tuple]),
    van_hove_qualify=van_hove_qualify,
    MAX_PQ_SUM=MAX_PQ_SUM,
    EVAL_CUTOFF=EVAL_CUTOFF,
    input_shas=np.array(
        [f"{k}={v}" for k, v in sorted(INPUT_SHAS.items())]
    ),
)
print(f"  Saved: {out_npz}")

# ============================================================
# SECTION 15: Plot
# ============================================================
print("[SEC 13] Plot")
fig, axes = plt.subplots(3, 1, figsize=(9, 11), sharex=True)

ax1 = axes[0]
ax1.plot(tau_arr_full, chi_N_arr, 'o-', color='steelblue',
         lw=2, ms=5, label='chi_N(tau)')
ax1.axvline(tau_fold, color='red', ls='--', alpha=0.7,
            label=f'tau_fold = {tau_fold}')
ax1.scatter(tau_coarse_actual, chi_N_coarse, color='crimson', s=80,
            zorder=5, label='coarse grid (gate)')
ax1.set_ylabel('chi_N(tau) = a_0 - a_2 + a_4')
ax1.set_title('S82 W1-4: CHI-N-WARD-DUAL (rank-2 spectral Euler-characteristic functional)')
ax1.legend(loc='best', fontsize=9)
ax1.grid(alpha=0.3)

ax2 = axes[1]
ax2.plot(tau_arr_full, W_arr, 's-', color='darkorange',
         lw=2, ms=5, label='W(tau)')
ax2.axvline(tau_fold, color='red', ls='--', alpha=0.7)
ax2.scatter(tau_coarse_actual, W_coarse, color='crimson', s=80, zorder=5)
ax2.set_ylabel('W(tau) = g_U1^2 * sqrt(a_4/a_2)')
ax2.legend(loc='best', fontsize=9)
ax2.grid(alpha=0.3)

ax3 = axes[2]
ax3.plot(tau_arr_full, Pi_arr, '^-', color='seagreen',
         lw=2, ms=6, label='Pi(tau) = chi_N*W')
ax3.axvline(tau_fold, color='red', ls='--', alpha=0.7)
ax3.scatter(tau_coarse_actual, Pi_coarse, color='crimson', s=80,
            zorder=5, label='coarse grid (gate)')
ax3.text(
    0.02, 0.95,
    f'COARSE pct_var = {pct_var_coarse:.3f}%\n'
    f'Pi direction:  {direction_diag}\n'
    f'Gate verdict:  {verdict}\n'
    f'(PASS<{PASS_THRESH}%, INFO<{INFO_THRESH}%, FAIL otherwise)',
    transform=ax3.transAxes, verticalalignment='top',
    bbox=dict(boxstyle='round', facecolor='ivory', alpha=0.9),
    fontsize=10,
)
ax3.set_xlabel('tau (Jensen deformation parameter)')
ax3.set_ylabel('Pi(tau) = chi_N(tau) * W(tau)')
ax3.legend(loc='lower left', fontsize=9)
ax3.grid(alpha=0.3)

plt.tight_layout()
out_png = os.path.join(SCRIPT_DIR, "s82_w1_4_chi_n_ward_dual.png")  # (local)
plt.savefig(out_png, dpi=150, bbox_inches='tight')
plt.close(fig)
print(f"  Saved: {out_png}")

# ============================================================
# SECTION 16: Append verdict to s82_gate_verdicts.txt
# ============================================================
print("[SEC 14] Append verdict to s82_gate_verdicts.txt")
verdicts_path = os.path.join(SCRIPT_DIR, "s82_gate_verdicts.txt")   # (local)
verdict_line = (                                                    # (local)
    f"S82-CHI-N-WARD-DUAL: {verdict} -- "
    f"value={pct_var_coarse:.4f} "
    f"scheme=WARD-DUAL "
    f"convention=EUCLIDEAN "
    f"L_max={MAX_PQ_SUM} "
    f"sha256={closure_sha}\n"
)
with open(verdicts_path, 'a', encoding='utf-8') as _fh:
    _fh.write(verdict_line)
print(f"  Appended to: {verdicts_path}")
print(f"  Line: {verdict_line.strip()}")

# ============================================================
# FINAL: 4-tuple line (MUST be final non-verdict line)
# ============================================================
print()
print("=" * 78)
print(f"S82-CHI-N-WARD-DUAL {verdict}")
print(f"FINAL 4-TUPLE: {four_tuple}")
print("=" * 78)
