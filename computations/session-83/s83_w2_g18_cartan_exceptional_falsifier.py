"""
S83 W2-G18 -- CARTAN-EXCL-EXCEPTIONAL-FALSIFIER (G_2 CLT falsifier)
======================================================================

Gate: S83-CARTAN-EXCL-EXCEPTIONAL-FALSIFIER
Trigger: [VERIFY][SIGN]
Classification: GEOMETRIC

HYPOTHESIS: G_2 (exceptional rank-2 Lie group) drift_u1 falsifies the L2
Cartan-exclusion theorem candidate if it lies OUTSIDE the CLT prediction
band at L=6,7,8.

SUBSTITUTION CHAIN (pre-registered, [VERIFY][SIGN]):
  Step 1 (def). drift_u1^{CLT}(L) = 0.5 + 0.5/sqrt(L*(L+1))  -- pre-registered.
                (Plan Step 1, line 1418 of session-83-plan.md.)
  Step 2 (sub). Compute drift_u1^{actual}(G_2, L) for L in {6, 7, 8}.
                Definition (per P4-B, matching S78/S80 W2-C convention):
                  drift_u1(L) = |<alpha_1>^{u1} - <alpha_1>^{exact}| / |<alpha_1>^{exact}|
                where
                  <alpha_1>^{b}    = J_b^{zeta2} / J_b^{SDW}   per-branch ratio
                  <alpha_1>^{exact} = cross-branch mean over {Cartan, ShortRoots,
                                     LongRoots}  (R-protection target)
                G_2 has the root-system partition:
                  - Cartan h = H_1, H_2 (rank 2; 2 Cartan directions)
                  - 6 short roots (alpha_1, ..., fundamental 7-dim direction)
                  - 6 long roots (alpha_2, ..., orthogonal root span)
                The "u1" branch generalization for G_2: the Cartan-only branch
                (h) is the rank-2 abelian subalgebra -- the direct analog of
                SU(3)'s u1 (lambda_8 direction) at higher rank, with dim H_pi = 2.
  Step 3 (simpl). Band = CLT +/- 15% (pre-registered).
                    L=6: CLT = 0.5 + 0.5/sqrt(42)  = 0.5 + 0.07714 = 0.57714
                    L=7: CLT = 0.5 + 0.5/sqrt(56)  = 0.5 + 0.06682 = 0.56682
                    L=8: CLT = 0.5 + 0.5/sqrt(72)  = 0.5 + 0.05893 = 0.55893
                    Band_lo(L) = CLT(L) * 0.85
                    Band_hi(L) = CLT(L) * 1.15
  Step 4 (direction). PASS (confirms L2 theorem) if all 3 L in band.
                FAIL (falsifies L2 theorem) if drift outside band at any L.
  Step 5. Python computes actual drift_u1(G_2, L) via the spectral formula and
          classifies.

PRU pins:
  (1) SHA-256 content-hash of L=6,7,8 G_2 spectrum.
  (2) SHA-256 import-closure hash.
  (3) CLT formula pin: drift_u1^{CLT}(L) = 0.5 + 0.5/sqrt(L*(L+1))  (plan line 1418).
  (4) Single run per L_max -- no iteration.

METHOD ARCHITECTURE (substrate framing):
  The G_2 spectral triple (A_G2, H_G2, D_G2) on Jensen-deformed G_2 fiber is
  constructed representation-theoretically via the irrep expansion. For each
  highest-weight (a1, a2), the spectral contribution is:
    lambda_rep = sqrt(C_2^{G2}(a1,a2)) * exp(-tau * rho(a1,a2))
  with multiplicity = dim_G2(a1, a2).
  rho(a1,a2) = a1 + a2 (number of root-system steps), identical proxy to
  W1-G2 script (s83_w1_g2_epsilon_h_promotion.py).

  For the branch decomposition, G_2 has 14 adjoint generators:
    - 2 Cartan (abelian, h-branch) <-> u1 analog (dim H_pi = 2)
    - 6 short roots (s-branch)
    - 6 long roots (l-branch)
  The branch-projected perturbation G_i for each branch scales the contribution
  of that branch's generators in the irrep. For the rep-theoretic proxy, the
  per-branch J_b^{func} at leading order in the Jensen coderivative is:
    J_b^{SDW}   = (dim_b / dim_adj) * sum_rep dim_rep * lam_rep
    J_b^{zeta2} = (dim_b / dim_adj) * sum_rep dim_rep / lam_rep^2
  with (dim_h, dim_s, dim_l, dim_adj) = (2, 6, 6, 14).

  alpha_1^b := J_b^{zeta2} / J_b^{SDW}. At leading order this ratio is
  INDEPENDENT of the (dim_b/dim_adj) prefactor (it cancels). The drift comes
  from: for a rank-r branch with dim_H_pi = r, CLT predicts a residual
  O(1/sqrt(N)) in the branch-restricted Mellin ratio due to finite-L mode
  truncation. For SU(3) u1 (r=1), observed drift_u1(6)=0.8375 (S78) vs
  CLT_naive = 0.6768 => PASS-CLT at L=8 (drift=0.6732, S80).
  For G_2 h-branch (r=2), test whether drift(L=6,7,8) stays in-band at 15%
  of 0.5 + 0.5/sqrt(L*(L+1)).

  IMPORTANT DISTINCTION from S80 u1 drift: here we test the FALSIFIER
  prediction. If G_2 h-drift is WITHIN the predicted CLT band at all 3 L,
  the L2 Cartan-exclusion theorem CANDIDATE is consistent (PASS). If G_2
  h-drift DEVIATES beyond 15%, the theorem is FALSIFIED (FAIL).

OUTPUTS:
  computations/session-83/s83_w2_g18_cartan_exceptional_falsifier.py
  computations/session-83/s83_w2_g18_cartan_exceptional_falsifier.npz
  computations/session-83/s83_w2_g18_cartan_exceptional_falsifier.png
  Append verdict to computations/session-83/s83_gate_verdicts.txt
  Write section §W2-G18 to session-83-results-workingpaper.md

Session: S83 W2-G18. Agent: connes-ncg-theorist.
"""

import os
os.environ.setdefault('OMP_NUM_THREADS', '8')            # (local)
os.environ.setdefault('MKL_NUM_THREADS', '8')            # (local)

import sys
import hashlib
import json
import time
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

SCRIPT_DIR = Path(__file__).parent
sys.path.insert(0, str(SCRIPT_DIR))
os.chdir(SCRIPT_DIR)

from canonical_constants import (
    tau_fold, M_KK, PI,
)

# ============================================================
# PRU PINS: Import-closure SHA-256
# ============================================================
IMPORT_CLOSURE_FILES = [                                 # (local)
    "s83_w2_g18_cartan_exceptional_falsifier.py",
    "canonical_constants.py",
]

def sha256_of_file(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()

def sha256_of_array(arr):
    a = np.ascontiguousarray(np.asarray(arr, dtype=np.float64))
    return hashlib.sha256(a.tobytes()).hexdigest()

def sha256_of(obj):
    s = json.dumps(obj, sort_keys=True, default=str).encode()
    return hashlib.sha256(s).hexdigest()

import_hashes = {f: sha256_of_file(os.path.join(SCRIPT_DIR, f))
                 for f in IMPORT_CLOSURE_FILES}                                  # (local)
closure_concat = "".join(sorted(import_hashes.values())).encode()                # (local)
IMPORT_CLOSURE_SHA = hashlib.sha256(closure_concat).hexdigest()                  # (local)

# ============================================================
# CONFIGURATION (PRU-pinned)
# ============================================================
TAU = tau_fold                                           # (local) 0.190
L_LIST = [6, 7, 8]                                       # (local) gate L range
BAND_FRAC = 0.15                                         # (local) pre-registered +/- 15%

# G_2 branch decomposition:
#   h-branch (Cartan, rank 2)  dim_h = 2
#   s-branch (short roots)     dim_s = 6
#   l-branch (long roots)      dim_l = 6
#   adjoint                    dim_adj = 14
DIM_H = 2                                                # (local)
DIM_S = 6                                                # (local)
DIM_L = 6                                                # (local)
DIM_ADJ = 14                                             # (local)

# Scheme / convention
SCHEME_TAG = "zeta2_over_SDW_G2_h_branch"                # (local)
CONVENTION_TAG = "G2-irrep-representation-theoretic, rho=a1+a2, lambda=sqrt(C2)*exp(-tau*rho)"  # (local)

# ============================================================
# G_2 REPRESENTATION THEORY
# ============================================================

def dim_g2_irrep(a1, a2):
    """
    Weyl dimension formula for G_2 irrep (a1, a2) with Dynkin labels.
    dim(a1,a2) = (a1+1)(a2+1)(a1+a2+2)(a1+2*a2+3)(2*a1+3*a2+5)(a1+3*a2+4)/120
    (0,0)=1; (1,0)=7; (0,1)=14; (2,0)=27; (1,1)=64; (0,2)=77; (3,0)=77.
    """
    n1 = a1 + 1
    n2 = a2 + 1
    n3 = a1 + a2 + 2
    n4 = a1 + 2*a2 + 3
    n5 = 2*a1 + 3*a2 + 5
    n6 = a1 + 3*a2 + 4
    return n1 * n2 * n3 * n4 * n5 * n6 // 120

def quadratic_casimir_g2(a1, a2):
    """
    G_2 quadratic Casimir for highest weight lambda = a1*w_1 + a2*w_2,
    with standard normalization |alpha_long|^2 = 2.
    C_2 = (2/3)*a1^2 + 2*a1*a2 + 2*a2^2 + (10/3)*a1 + 6*a2
    (See s72_g2_constancy.py lines 565-645 for derivation.)
    """
    return (2.0/3.0)*a1**2 + 2.0*a1*a2 + 2.0*a2**2 + (10.0/3.0)*a1 + 6.0*a2

def g2_irrep_list(L_max):
    """Enumerate (a1, a2) with a1 + a2 <= L_max, excluding trivial."""
    out = []
    for a1 in range(L_max + 1):
        for a2 in range(L_max + 1 - a1):
            if a1 == 0 and a2 == 0:
                continue
            out.append((a1, a2))
    return out

# ============================================================
# SUBSTITUTION CHAIN VERIFICATION -- CLT prediction
# ============================================================
# Step 1 definition:
#   drift_u1^{CLT}(L) = 0.5 + 0.5 / sqrt(L*(L+1))
# Step 2 substitute L=6,7,8:
#   L=6: sqrt(42) = 6.4807407...   => 0.5/sqrt(42) = 0.077152...
#        drift_CLT(6) = 0.5 + 0.077152 = 0.577152
#   L=7: sqrt(56) = 7.4833148...   => 0.5/sqrt(56) = 0.066815...
#        drift_CLT(7) = 0.5 + 0.066815 = 0.566815
#   L=8: sqrt(72) = 8.4852814...   => 0.5/sqrt(72) = 0.058926...
#        drift_CLT(8) = 0.5 + 0.058926 = 0.558926
# Step 3 direction:
#   CLT decreases monotonically with L (1/sqrt(L(L+1)) is a positive
#   decreasing function of L for L >= 1). Band_hi - Band_lo = 0.30*CLT(L)
#   decreases monotonically, so at fixed 15% frac the band narrows
#   slightly. Stated numerically:
#     L=6: band = [0.49058, 0.66373]
#     L=7: band = [0.48179, 0.65184]
#     L=8: band = [0.47508, 0.64277]

def clt_prediction(L):
    """Pre-registered CLT formula: drift_u1^{CLT}(L) = 0.5 + 0.5/sqrt(L(L+1))."""
    return 0.5 + 0.5 / np.sqrt(L * (L + 1))

# ============================================================
# DRIFT COMPUTATION FOR G_2 (analog of S80 u1 on SU(3))
# ============================================================
# Definition (per P4-B / S78 W2-C / S80 W2-C-REMED):
#   drift_b(L) = |<alpha_1>^b - <alpha_1>^exact| / |<alpha_1>^exact|
#   <alpha_1>^b = J_b^{zeta2} / J_b^{SDW}
#   <alpha_1>^exact = cross-branch mean.
#
# For the rep-theoretic approximation of the spectral moments on Jensen-
# deformed G_2 (same approach as W1-G2 script):
#   lambda_{a1,a2} = sqrt(C_2^{G2}(a1,a2)) * exp(-tau * rho(a1,a2)),  rho = a1+a2
#   mult_{a1,a2}   = dim_G2(a1, a2)
#
# Branch-projected Josephson integrals (leading-order in perturbation phi):
# The zeta-Josephson J_b^{func}(L) is the 2nd derivative in phi of the
# spectral functional, weighted by the branch projector pi_b.
# For rank-r branch acting on the rep (a1, a2), the induced eigenvalue
# perturbation scales as:
#   delta lambda(phi; b) ~ phi * w_b(a1, a2) * lambda_{a1, a2}
# where w_b(a1,a2) is the "branch overlap" for the rep.
#
# For the rep-theoretic proxy, the simplest consistent choice is:
#   w_h(a1,a2) = r_h(a1,a2) / (2 * d_G2(a1,a2))    -- Cartan-trace projector
#   w_s(a1,a2) = (a1)      / (a1 + a2)  * (6/14)   -- short-root weight
#   w_l(a1,a2) = (a2)      / (a1 + a2)  * (6/14)   -- long-root weight
# where r_h(a1,a2) = rank of the h-image in the rep (= rank of the Cartan
# subalgebra image, = 2 for faithful reps, = 0 for trivial rep).
#
# For (a1,a2) = (0,0): r_h = 0, trivial rep excluded.
# For all nontrivial irreps with a1+a2 > 0 (which is what L_max enumerates):
#   r_h = 2 (Cartan faithfully represented).
#
# The per-branch Josephson at leading order (phi^2 expansion):
#   J_b^{SDW}(L)   = sum_{irreps} mult * w_b * |lambda|
#   J_b^{zeta2}(L) = sum_{irreps} mult * w_b * 1/|lambda|^2
#
# The per-branch ratio:
#   alpha_1^b(L) = J_b^{zeta2}/J_b^{SDW}
#                = [sum mult * w_b * |lambda|^{-2}] / [sum mult * w_b * |lambda|]
# When w_b(a1,a2) depends on (a1,a2), this ratio DIFFERS across branches,
# producing the drift.
#
# For the G_2 h-branch: w_h is a constant (r_h = 2 for all nontrivial reps,
# divided by a dim_G2-dependent factor). So:
#   w_h(a1,a2) = 2 / (2 * dim_G2) * (2/14) = 1/(7*dim_G2)
# The constant factor 1/7 cancels in the ratio, leaving:
#   alpha_1^h(L) = [sum mult/dim_G2 * |lambda|^{-2}] / [sum mult/dim_G2 * |lambda|]
# But mult = dim_G2, so mult/dim_G2 = 1 -- the h-branch ratio is
# SCHEME-INDEPENDENT of the irrep multiplicity weighting:
#   alpha_1^h(L) = [sum |lambda|^{-2}] / [sum |lambda|]
#
# By contrast the s-branch and l-branch have weight
#   w_s = a1/(a1+a2) * (6/14) * mult
#   w_l = a2/(a1+a2) * (6/14) * mult
# so their ratios pick up the (a1, a2) projections in the numerator.
#
# This is the structural reason the h-branch (Cartan) is the "u1 analog" --
# it is the branch whose J-weighting is MOMENT-INDEPENDENT of the branch
# projector. The S80 SU(3) u1 drift comes from the rank-1 analogue of this
# structure: for SU(3), dim_H_pi = 1 on the u1 direction (lambda_8 only).

def compute_drift_u1_G2(L_max):
    """
    Compute drift_h(G_2, L) per P4-B definition, using the rep-theoretic
    leading-order spectral-moment formula.

    Returns dict with per-branch alpha_1, drift per branch, and the
    cross-branch-mean exact value.
    """
    irreps = g2_irrep_list(L_max)
    if not irreps:
        return None

    # Spectrum, multiplicity
    lam = np.array([np.sqrt(quadratic_casimir_g2(a1, a2)) * np.exp(-TAU * (a1 + a2))
                    for (a1, a2) in irreps])                                # (local)
    mult = np.array([dim_g2_irrep(a1, a2) for (a1, a2) in irreps],
                    dtype=np.float64)                                       # (local)
    a1_arr = np.array([a1 for (a1, a2) in irreps], dtype=np.float64)        # (local)
    a2_arr = np.array([a2 for (a1, a2) in irreps], dtype=np.float64)        # (local)
    step_sum = a1_arr + a2_arr                                              # (local) >= 1 on nontrivial reps

    # Branch weights per irrep (pre-sum):
    # h-branch: constant per rep (Cartan faithfully embedded) -> w_h ~ 1 * mult
    # s-branch: w_s ~ mult * (a1 / step_sum) * (6/14)
    # l-branch: w_l ~ mult * (a2 / step_sum) * (6/14)
    # Overall scalar factors (6/14) cancel in the ratio alpha_1 = zeta2/SDW,
    # so we omit them.
    w_h = mult                                                              # (local)
    w_s = mult * (a1_arr / step_sum)                                        # (local)
    w_l = mult * (a2_arr / step_sum)                                        # (local)

    # J^{SDW}_b = sum w_b * |lambda|
    # J^{zeta2}_b = sum w_b * 1/|lambda|^2
    J_SDW_h = float(np.sum(w_h * lam))                                      # (local)
    J_SDW_s = float(np.sum(w_s * lam))                                      # (local)
    J_SDW_l = float(np.sum(w_l * lam))                                      # (local)
    J_zeta2_h = float(np.sum(w_h / (lam ** 2)))                             # (local)
    J_zeta2_s = float(np.sum(w_s / (lam ** 2)))                             # (local)
    J_zeta2_l = float(np.sum(w_l / (lam ** 2)))                             # (local)

    alpha1_h = J_zeta2_h / J_SDW_h                                          # (local)
    alpha1_s = J_zeta2_s / J_SDW_s                                          # (local)
    alpha1_l = J_zeta2_l / J_SDW_l                                          # (local)
    alpha1_exact = float(np.mean([alpha1_h, alpha1_s, alpha1_l]))           # (local)

    drift_h = abs(alpha1_h - alpha1_exact) / abs(alpha1_exact)              # (local)
    drift_s = abs(alpha1_s - alpha1_exact) / abs(alpha1_exact)              # (local)
    drift_l = abs(alpha1_l - alpha1_exact) / abs(alpha1_exact)              # (local)

    spectrum_sha = sha256_of_array(np.sort(lam))                            # (local)

    return {
        "L": L_max,
        "n_irreps": len(irreps),
        "lam_min": float(lam.min()),
        "lam_max": float(lam.max()),
        "J_SDW": {"h": J_SDW_h, "s": J_SDW_s, "l": J_SDW_l},
        "J_zeta2": {"h": J_zeta2_h, "s": J_zeta2_s, "l": J_zeta2_l},
        "alpha1": {"h": alpha1_h, "s": alpha1_s, "l": alpha1_l},
        "alpha1_exact": alpha1_exact,
        "drift": {"h": drift_h, "s": drift_s, "l": drift_l},
        "drift_h": drift_h,  # Cartan-branch = analog of SU(3) u1
        "spectrum_sha": spectrum_sha,
        "irreps": irreps,
    }

# ============================================================
# PRINT HEADER (20-line SHA log per §4.5)
# ============================================================
print("=" * 78, flush=True)
print("S83 W2-G18: CARTAN-EXCL-EXCEPTIONAL-FALSIFIER (G_2 CLT falsifier)", flush=True)
print("=" * 78, flush=True)
print(f"  Gate ID           : S83-CARTAN-EXCL-EXCEPTIONAL-FALSIFIER", flush=True)
print(f"  Trigger           : [VERIFY][SIGN]", flush=True)
print(f"  Classification    : GEOMETRIC", flush=True)
print(f"  Import closure SHA: {IMPORT_CLOSURE_SHA}", flush=True)
print(f"  Files in closure  : {IMPORT_CLOSURE_FILES}", flush=True)
print(f"  tau_fold          : {TAU}", flush=True)
print(f"  L_LIST            : {L_LIST}", flush=True)
print(f"  Band fraction     : {BAND_FRAC} (+/- 15%)", flush=True)
print(f"  Scheme tag        : {SCHEME_TAG}", flush=True)
print(f"  Convention tag    : {CONVENTION_TAG}", flush=True)
print(f"  G_2 dim_h / dim_s / dim_l / dim_adj = {DIM_H} / {DIM_S} / {DIM_L} / {DIM_ADJ}", flush=True)
print(f"""
  SUBSTITUTION CHAIN ([VERIFY][SIGN]):
    Step 1: drift_u1^CLT(L) = 0.5 + 0.5/sqrt(L*(L+1))
    Step 2: L=6 -> CLT = 0.5 + 0.5/sqrt(42)  = {clt_prediction(6):.6f}
            L=7 -> CLT = 0.5 + 0.5/sqrt(56)  = {clt_prediction(7):.6f}
            L=8 -> CLT = 0.5 + 0.5/sqrt(72)  = {clt_prediction(8):.6f}
    Step 3: Band(L) = CLT(L) +/- 15%
            L=6 band = [{clt_prediction(6)*(1-BAND_FRAC):.5f}, {clt_prediction(6)*(1+BAND_FRAC):.5f}]
            L=7 band = [{clt_prediction(7)*(1-BAND_FRAC):.5f}, {clt_prediction(7)*(1+BAND_FRAC):.5f}]
            L=8 band = [{clt_prediction(8)*(1-BAND_FRAC):.5f}, {clt_prediction(8)*(1+BAND_FRAC):.5f}]
    Step 4: PASS (confirms theorem) if all 3 L in band
            FAIL (falsifies theorem)  if any L outside band
    Step 5: Python computes drift_u1^{{actual}}(G_2, L) below -> classify.
""", flush=True)

# ============================================================
# STEP 5: Python -- per-L drift computation
# ============================================================
print("=" * 78, flush=True)
print("STEP 5: per-L drift_h computation on Jensen-deformed G_2", flush=True)
print("=" * 78, flush=True)

t0 = time.time()                                         # (local)
results_by_L = {}                                        # (local)
for L in L_LIST:
    r = compute_drift_u1_G2(L)
    results_by_L[L] = r
    print(f"  L={L}: n_irreps={r['n_irreps']:4d}, "
          f"alpha_1(h/s/l) = ({r['alpha1']['h']:.4e}, "
          f"{r['alpha1']['s']:.4e}, {r['alpha1']['l']:.4e}), "
          f"alpha_exact = {r['alpha1_exact']:.4e}, "
          f"drift_h = {r['drift_h']:.4%}, "
          f"spec_sha={r['spectrum_sha'][:16]}", flush=True)
print(f"  compute time: {time.time()-t0:.2f}s", flush=True)

# ============================================================
# STEP 6: CLT comparison and in-band test
# ============================================================
print("\n" + "=" * 78, flush=True)
print("STEP 6: CLT comparison and in-band test", flush=True)
print("=" * 78, flush=True)

# Substitution chain verification -- compute in-band explicitly:
#   in_band(L) := |drift(L) - CLT(L)| / CLT(L) < BAND_FRAC
# NOTE: The plan's pre-registered test is the relative deviation, per line 1426:
#   `in_band = {L: abs(results[L] - clt_preds[L])/clt_preds[L] < 0.15 for L in [6,7,8]}`

drift_actual = {L: results_by_L[L]['drift_h'] for L in L_LIST}              # (local)
clt_preds = {L: clt_prediction(L) for L in L_LIST}                          # (local)
rel_dev = {L: abs(drift_actual[L] - clt_preds[L]) / clt_preds[L]
           for L in L_LIST}                                                  # (local)
in_band = {L: rel_dev[L] < BAND_FRAC for L in L_LIST}                       # (local)
all_in_band = all(in_band.values())                                         # (local)

print(f"  {'L':<4} {'drift_h^actual':>16} {'CLT pred':>14} {'rel dev':>12} {'in band?':>10}",
      flush=True)
for L in L_LIST:
    print(f"  {L:<4} {drift_actual[L]:>16.4%} {clt_preds[L]:>14.4f} "
          f"{rel_dev[L]:>11.2%} {str(in_band[L]):>10}", flush=True)
print(f"  all_in_band = {all_in_band}", flush=True)

# ============================================================
# STEP 7: Verdict classification
# ============================================================
print("\n" + "=" * 78, flush=True)
print("STEP 7: Gate verdict -- S83-CARTAN-EXCL-EXCEPTIONAL-FALSIFIER", flush=True)
print("=" * 78, flush=True)

if all_in_band:
    verdict = "PASS"
    verdict_reason = (f"G_2 Cartan drift in CLT band at all 3 L -- confirms Level-2 "
                      f"Cartan-exclusion theorem candidate for exceptional rank-2 simple groups.")
else:
    verdict = "FAIL"
    out_list = [L for L in L_LIST if not in_band[L]]                        # (local)
    verdict_reason = (f"G_2 Cartan drift OUTSIDE CLT band at L={out_list} -- "
                      f"falsifies Level-2 Cartan-exclusion theorem candidate; "
                      f"exceptional rank-2 is an exception (non-generic CLT scaling).")

print(f"  VERDICT: {verdict}", flush=True)
print(f"  reason : {verdict_reason}", flush=True)

# ============================================================
# STEP 8: 4-tuple tag and closure SHA
# ============================================================
OUTPUT_PINS = {                                                              # (local)
    "tau_fold": TAU,
    "L_LIST": L_LIST,
    "drift_h_L6": drift_actual[6],
    "drift_h_L7": drift_actual[7],
    "drift_h_L8": drift_actual[8],
    "clt_L6": clt_preds[6],
    "clt_L7": clt_preds[7],
    "clt_L8": clt_preds[8],
    "in_band_L6": in_band[6],
    "in_band_L7": in_band[7],
    "in_band_L8": in_band[8],
    "all_in_band": all_in_band,
    "verdict": verdict,
    "gate": "S83-CARTAN-EXCL-EXCEPTIONAL-FALSIFIER",
    "plan_section": "W2-G18",
    "import_closure_sha256": IMPORT_CLOSURE_SHA,
    "spec_sha_L6": results_by_L[6]['spectrum_sha'],
    "spec_sha_L7": results_by_L[7]['spectrum_sha'],
    "spec_sha_L8": results_by_L[8]['spectrum_sha'],
}
closure_sha = sha256_of(OUTPUT_PINS)                                         # (local)

# Headline value = drift_h at L=8 (largest L in range)
headline_value = drift_actual[8]                                             # (local)
L_MAX_TAG = 8                                                                # (local)

print(f"\n  4-tuple tag: (value={headline_value:.6f}, scheme={SCHEME_TAG}, "
      f"convention={CONVENTION_TAG}, L_max={L_MAX_TAG})", flush=True)
print(f"  CLOSURE_SHA256 = {closure_sha}", flush=True)

# ============================================================
# STEP 9: Save NPZ
# ============================================================
npz_path = SCRIPT_DIR / "s83_w2_g18_cartan_exceptional_falsifier.npz"
np.savez_compressed(
    npz_path,
    L_list=np.array(L_LIST, dtype=np.int64),
    drift_h_vs_L=np.array([drift_actual[L] for L in L_LIST]),
    drift_s_vs_L=np.array([results_by_L[L]['drift']['s'] for L in L_LIST]),
    drift_l_vs_L=np.array([results_by_L[L]['drift']['l'] for L in L_LIST]),
    alpha1_h_vs_L=np.array([results_by_L[L]['alpha1']['h'] for L in L_LIST]),
    alpha1_s_vs_L=np.array([results_by_L[L]['alpha1']['s'] for L in L_LIST]),
    alpha1_l_vs_L=np.array([results_by_L[L]['alpha1']['l'] for L in L_LIST]),
    alpha1_exact_vs_L=np.array([results_by_L[L]['alpha1_exact'] for L in L_LIST]),
    n_irreps_vs_L=np.array([results_by_L[L]['n_irreps'] for L in L_LIST]),
    clt_preds=np.array([clt_preds[L] for L in L_LIST]),
    rel_dev=np.array([rel_dev[L] for L in L_LIST]),
    in_band=np.array([in_band[L] for L in L_LIST]),
    all_in_band=np.bool_(all_in_band),
    band_frac=np.float64(BAND_FRAC),
    verdict=np.array(verdict),
    verdict_reason=np.array(verdict_reason),
    headline_drift_h_L8=np.float64(headline_value),
    closure_sha=np.array(closure_sha),
    import_closure_sha=np.array(IMPORT_CLOSURE_SHA),
    spec_sha_L6=np.array(results_by_L[6]['spectrum_sha']),
    spec_sha_L7=np.array(results_by_L[7]['spectrum_sha']),
    spec_sha_L8=np.array(results_by_L[8]['spectrum_sha']),
    tau_fold_used=np.float64(TAU),
    scheme_tag=np.array(SCHEME_TAG),
    convention_tag=np.array(CONVENTION_TAG),
    L_max_tag=np.int64(L_MAX_TAG),
)
print(f"\n  NPZ saved: {npz_path}", flush=True)

# ============================================================
# STEP 10: Plot
# ============================================================
fig, axs = plt.subplots(1, 2, figsize=(13, 5.5))
fig.suptitle(f"S83 W2-G18 CARTAN-EXCL-EXCEPTIONAL-FALSIFIER (G_2) -- VERDICT: {verdict}",
             fontsize=13)

# Left: drift_h (Cartan) vs L with CLT band
ax = axs[0]
Ls_arr = np.array(L_LIST)
drifts_h = np.array([drift_actual[L] for L in L_LIST])
drifts_s = np.array([results_by_L[L]['drift']['s'] for L in L_LIST])
drifts_l = np.array([results_by_L[L]['drift']['l'] for L in L_LIST])
clt_vals = np.array([clt_preds[L] for L in L_LIST])
band_lo = clt_vals * (1 - BAND_FRAC)
band_hi = clt_vals * (1 + BAND_FRAC)

ax.fill_between(Ls_arr, band_lo, band_hi, alpha=0.25, color='green',
                label=f'CLT band +/-{int(BAND_FRAC*100)}%')
ax.plot(Ls_arr, clt_vals, 'k--', label='CLT: 0.5 + 0.5/sqrt(L(L+1))', lw=1.5)
ax.plot(Ls_arr, drifts_h, 'o-', color='tab:green', label='G_2 Cartan (h) drift',
        lw=2, ms=10)
ax.plot(Ls_arr, drifts_s, 's--', color='tab:blue', label='G_2 short-roots drift',
        ms=6, alpha=0.6)
ax.plot(Ls_arr, drifts_l, '^--', color='tab:orange', label='G_2 long-roots drift',
        ms=6, alpha=0.6)
ax.set_xlabel('L_max')
ax.set_ylabel('drift_b = |<alpha_1>^b - <alpha_1>^exact| / |<alpha_1>^exact|')
ax.set_title('G_2 Cartan drift vs CLT')
ax.legend(fontsize=8, loc='best')
ax.grid(alpha=0.3)

# Right: relative deviation bar chart
ax = axs[1]
rels = np.array([rel_dev[L] for L in L_LIST]) * 100
bars = ax.bar([str(L) for L in L_LIST], rels,
              color=['green' if in_band[L] else 'red' for L in L_LIST])
ax.axhline(BAND_FRAC * 100, color='k', linestyle='--',
           label=f'pre-reg {int(BAND_FRAC*100)}% threshold')
ax.set_xlabel('L_max')
ax.set_ylabel('|drift - CLT| / CLT  (%)')
ax.set_title(f'Relative deviation -- {verdict}')
ax.legend(fontsize=9)
ax.grid(alpha=0.3, axis='y')
for L, v in zip(L_LIST, rels):
    ax.text(str(L), v + 1, f'{v:.1f}%', ha='center', fontsize=9)

plt.tight_layout()
png_path = SCRIPT_DIR / "s83_w2_g18_cartan_exceptional_falsifier.png"
plt.savefig(png_path, dpi=120)
plt.close()
print(f"  PNG saved: {png_path}", flush=True)

# ============================================================
# STEP 11: Verdict line (S81+ canonical form)
# ============================================================
verdict_path = SCRIPT_DIR / "s83_gate_verdicts.txt"
verdict_line = (f"S83-CARTAN-EXCL-EXCEPTIONAL-FALSIFIER: {verdict} -- "
                f"value={headline_value:.6f} scheme={SCHEME_TAG} "
                f"convention={CONVENTION_TAG} L_max={L_MAX_TAG} "
                f"sha256={closure_sha}")
with open(verdict_path, "a") as fh:
    fh.write(verdict_line + "\n")
print(f"\n  Verdict appended: {verdict_path}", flush=True)
print(f"    {verdict_line[:120]}...", flush=True)

print("\n" + "=" * 78, flush=True)
print(f"DONE. Verdict: {verdict}  |  drift_h(L=6,7,8) = "
      f"{drifts_h[0]:.4%}, {drifts_h[1]:.4%}, {drifts_h[2]:.4%}", flush=True)
print(f"     CLT predictions = {clt_vals[0]:.4f}, {clt_vals[1]:.4f}, {clt_vals[2]:.4f}",
      flush=True)
print(f"     relative deviations = {rels[0]:.1f}%, {rels[1]:.1f}%, {rels[2]:.1f}%",
      flush=True)
print("=" * 78, flush=True)
