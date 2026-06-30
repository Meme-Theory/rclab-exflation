#!/usr/bin/env python3
"""
S82 W2-4: PS-SUBSTRATE-MATCHED-IC — A_s under substrate-GGE initial condition
==============================================================================

Gate: S82-PS-SUBSTRATE-MATCHED-IC  [VERIFY] + [CHAIN]
Classification: PHONONIC
Owner: volovik-superfluid-universe-theorist (this run)
Pre-reg anchor: sessions/session-plan/session-80-plan.md §W2-4 L1307-L1338

Phononic framing:
  S79 P2-B closed horizon-exit tachyonic-Airy IC as kinematically inadmissible
  under the phonon-first substrate (5 IC directions closed at factor ~1.13
  agreement).  The surviving admissible IC is the substrate-GGE Wightman
  function — the two-point function of the Ordered Veil's phononic relic
  in the Volovik 3He-B correspondence.  This is NOT a Bunch-Davies vacuum on
  inflating spacetime; it is the per-mode squeezed-state occupation spectrum
  of the GGE relic formed by the diabatic fold transit (S38, n_pairs = 59.8
  over 8 Bogoliubov bands, per-band GGE temperatures T_k^GGE documented in
  agent-memory gge-temp-43-result).

Method (per S80 plan L1329-L1333, verbatim):
  1. Write substrate-GGE IC as Wightman function of the GGE-phonon relic
     W_GGE(k) = 1/2 + n_k^GGE = coth(omega_k / (2 T_k^GGE)) / 2
     where (omega_k, T_k^GGE) are PER-BAND (Volovik 3He-B non-equilibrium
     vacua formalism, paper 25; 3He-B topological BDI, paper 26).

  2. Evolve through transit using Parker pair-production mode equation:
     v_k^out = alpha_k v_k^BD + beta_k (v_k^BD)*, with
     |alpha|^2 - |beta|^2 = +1 (Wronskian pin),
     S_IC^GGE(k) = |alpha + beta|^2 = 1 + 2 n_k^GGE.
     Thouless >> transit (S61 factor 2625x) preserves GGE occupations to
     leading order through the fold.

  3. Match to post-transit mode; A_s under UNIFIED-AS-79 with substrate IC is
     A_s^substrate = A_s^BD(W1-2) * K_substrate,
     K_substrate = S_IC^GGE(k_pivot).

  4. Compare to W1-2 TD-branch A_s = 3.2994e-9 (PASS-F2 vs Planck 2.1e-9).

Pre-registered gate (S80 plan L1314-L1321):
  PASS: |log10(A_s^substrate / A_s^W1-2)| < log10(3) = 0.4771  (factor-3)
  INFO: log10(3) <= |log10 ratio| < log10(10) = 1.0000         (factor-3 to -10)
  FAIL: |log10 ratio| >= 1.0000                                (> factor-10)

Direction read-off (pre-Python substitution chain, SIGN rule):

  Step 1 (definitions):
    W_GGE(k) = <a_k^dag a_k>_GGE + 1/2 = n_k^GGE + 1/2
    |v_k|^2 = W_GGE(k) / omega_k (Mukhanov mode normalization)
    S_IC^GGE(k) = 1 + 2 n_k^GGE  (squeezing factor)
    K_substrate = S_IC^GGE(k_pivot) / S_IC^BD = S_IC^GGE(k_pivot) / 1

  Step 2 (substitution with positivity):
    n_k^GGE >= 0 for any GGE state (physical occupation number).
    Therefore S_IC^GGE >= 1, K_substrate >= 1.

  Step 3 (canonical form):
    A_s^substrate = A_s^BD * K_substrate  with K_substrate in [1, oo).

  Step 4 (direction from canonical form):
    A_s^substrate >= A_s^BD(W1-2).  Substrate IC CANNOT SUPPRESS A_s relative
    to BD; it can only equal-or-amplify.  This is a STRUCTURAL bound — a
    direct consequence of n_k >= 0.

  Conclusion: whether the gate passes depends on the MAGNITUDE of K_substrate,
  an OUTPUT computed from the GGE per-band data.  The direction (K >= 1) is
  pre-asserted by the substitution chain; the verdict is numerical.

Five reading conventions (all pre-registered; R3 is PRIMARY per S43 band
multiplicity):
  R1: B3-only (softest band, CMB pivot in long-wavelength sector)
  R2: Geometric mean over 3 bands (isotropic Haar weight)
  R3: Weighted by S43 band multiplicity 3/3/2 (canonical per gge-temp-43)
  R4: Naive n_pairs=59.8 over 8 bands (legacy total-conservation reading)
  R5: B2-only (dominant parametric-amplification band at fold)

Environment:
  Scalar arithmetic; no linear algebra. OMP thread cap per CPU rule.
"""

import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import sys
import json
import hashlib
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Canonical constants (MANDATORY)
from canonical_constants import (
    M_KK_gravity,
    M_Pl_reduced,
    A_s_CMB,
    T_GGE_B2,          # B2-sector GGE temperature (S43)
    n_pairs,           # 59.8 Bogoliubov pairs from S38 transit
    Delta_0_GL,        # GL order parameter amplitude = 0.7704 M_KK
    Delta_0_OES,       # OES/pair-addition gap = 0.4643 M_KK
    Delta_B3,          # B3 sector gap = 0.176 M_KK
    tau_fold,          # 0.19 (S42 constants_snapshot)
)

# Per-band GGE temperatures (from gge-temp-43-result agent-memory;
# referenced in canonical_constants header S43 block but not all exported)
T_GGE_B1_local = 0.435            # (local) S43 gge-temp-43 result
T_GGE_B3_local = 0.178            # (local) S43 gge-temp-43 result

# Band multiplicities per S43 gge-temp-43 (3/3/2 for B2/B1/B3)
mult_B2 = 3                       # (local) S43 gge-temp-43-result
mult_B1 = 3                       # (local) S43 gge-temp-43-result
mult_B3 = 2                       # (local) S43 gge-temp-43-result

# ============================================================
# SECTION 0: Input SHA-256 pins (MANDATORY in first 20 lines)
# ============================================================
HERE = os.path.dirname(os.path.abspath(__file__))                  # (local)


def _sha256(path):
    with open(path, 'rb') as h:
        return hashlib.sha256(h.read()).hexdigest()


INPUT_FILES = [                                                    # (local)
    os.path.join(HERE, 'canonical_constants.py'),
    os.path.join(HERE, 's82_w1_2_unified_as_79_full.py'),
    os.path.join(HERE, 's82_w1_2_unified_as_79_full.npz'),
]

print("=" * 70)
print("S82 W2-4: PS-SUBSTRATE-MATCHED-IC (Volovik 3He-B Wightman / GGE)")
print("=" * 70)
print("\n[SEC 0] Input SHA-256 pins")
INPUT_SHAS = {}                                                    # (local)
for _f in INPUT_FILES:
    if os.path.exists(_f):
        _h = _sha256(_f)                                           # (local)
        INPUT_SHAS[os.path.basename(_f)] = _h
        print(f"  {os.path.basename(_f):46s} sha256={_h[:16]}...{_h[-8:]}")
    else:
        INPUT_SHAS[os.path.basename(_f)] = None
        print(f"  {os.path.basename(_f):46s} MISSING")

# ============================================================
# SECTION 1: Substrate-GGE Wightman inputs
# ============================================================
print("\n[SEC 1] Substrate-GGE parameters (Volovik 3He-B correspondence)")
print(f"  Per-band GGE temperatures (S43 gge-temp-43, M_KK units):")
print(f"    T_B2 = {T_GGE_B2:.4f}  (exported from canonical_constants)")
print(f"    T_B1 = {T_GGE_B1_local:.4f}  (S43 memory)")
print(f"    T_B3 = {T_GGE_B3_local:.4f}  (S43 memory)")
print(f"  Per-band gaps (canonical_constants, M_KK units):")
print(f"    Delta_B2 = {Delta_0_GL:.4f}  (= Delta_0_GL, GL order param)")
print(f"    Delta_B1 = {Delta_0_OES:.4f}  (= Delta_0_OES, OES/pair-addition)")
print(f"    Delta_B3 = {Delta_B3:.4f}")
print(f"  Band multiplicities (S43): 3/3/2 for B2/B1/B3")
print(f"  Total Bogoliubov pairs: n_pairs = {n_pairs:.1f} (S38 transit)")

# ============================================================
# SECTION 2: Per-band Wightman W_GGE(k) and squeezing factor S_IC^GGE
# ============================================================
print("\n[SEC 2] Per-band GGE occupations n_k and squeezing S_IC = 1 + 2n_k")

# omega_k/T_k ratio (dimensionless argument of coth)
x_B2 = Delta_0_GL / T_GGE_B2                      # (local) omega/T for B2
x_B1 = Delta_0_OES / T_GGE_B1_local               # (local) omega/T for B1
x_B3 = Delta_B3 / T_GGE_B3_local                  # (local) omega/T for B3

# GGE occupation per band: n_k = 1 / (exp(omega/T) - 1)
# This is the GGE Lagrange multiplier form (NOT a single thermal beta)
n_B2 = 1.0 / (np.exp(x_B2) - 1.0)                 # (local)
n_B1 = 1.0 / (np.exp(x_B1) - 1.0)                 # (local)
n_B3 = 1.0 / (np.exp(x_B3) - 1.0)                 # (local)

# Wightman squeezing per band
S_IC_B2 = 1.0 + 2.0 * n_B2                        # (local)
S_IC_B1 = 1.0 + 2.0 * n_B1                        # (local)
S_IC_B3 = 1.0 + 2.0 * n_B3                        # (local)

print(f"  B2: omega/T = {x_B2:.4f}, n_B2 = {n_B2:.4e}, S_IC^GGE(B2) = {S_IC_B2:.4f}")
print(f"  B1: omega/T = {x_B1:.4f}, n_B1 = {n_B1:.4e}, S_IC^GGE(B1) = {S_IC_B1:.4f}")
print(f"  B3: omega/T = {x_B3:.4f}, n_B3 = {n_B3:.4e}, S_IC^GGE(B3) = {S_IC_B3:.4f}")

# Cross-check structural bound: S_IC >= 1 (required by n_k >= 0)
assert S_IC_B2 >= 1.0 and S_IC_B1 >= 1.0 and S_IC_B3 >= 1.0, \
    "STRUCTURAL VIOLATION: S_IC < 1 — substitution chain step 4 fails"
print(f"  [structural bound verified: all S_IC >= 1]")

# ============================================================
# SECTION 3: Five K_substrate reading conventions
# ============================================================
print("\n[SEC 3] K_substrate under five pre-registered reading conventions")

# R1: B3-only (softest band, CMB pivot in long-wavelength sector)
K_R1 = S_IC_B3                                    # (local)

# R2: Geometric mean (isotropic Haar weight over 3 bands)
K_R2 = (S_IC_B2 * S_IC_B1 * S_IC_B3) ** (1.0/3.0)  # (local)

# R3: Weighted by S43 band multiplicity (PRIMARY)
K_R3 = (mult_B2 * S_IC_B2 + mult_B1 * S_IC_B1 + mult_B3 * S_IC_B3) \
       / (mult_B2 + mult_B1 + mult_B3)            # (local)

# R4: Legacy naive n_pairs=59.8 over 8 bands (average occupation)
n_avg_naive = n_pairs / 8.0                       # (local)
K_R4 = 1.0 + 2.0 * n_avg_naive                    # (local)

# R5: B2-only (dominant parametric amplification band at fold)
K_R5 = S_IC_B2                                    # (local)

print(f"  R1 (B3-only):          K = {K_R1:.4f}, log10 = {np.log10(K_R1):+.4f}")
print(f"  R2 (geo-mean):         K = {K_R2:.4f}, log10 = {np.log10(K_R2):+.4f}")
print(f"  R3 (weighted 3/3/2)*:  K = {K_R3:.4f}, log10 = {np.log10(K_R3):+.4f}")
print(f"  R4 (naive n_avg=7.475):K = {K_R4:.4f}, log10 = {np.log10(K_R4):+.4f}")
print(f"  R5 (B2-only):          K = {K_R5:.4f}, log10 = {np.log10(K_R5):+.4f}")
print(f"  (* PRIMARY per S43 gge-temp-43 documented band multiplicities)")

# ============================================================
# SECTION 4: Pre-registered thresholds
# ============================================================
DELTA_F3 = np.log10(3.0)         # (local) = 0.4771; PASS if |log10 ratio| < this
DELTA_F10 = np.log10(10.0)       # (local) = 1.0000; INFO if |log10 ratio| in [F3, F10]
print("\n[SEC 4] Pre-registered thresholds (S80 plan L1318-L1321)")
print(f"  DELTA_F3  = {DELTA_F3:.4f} OOM   (PASS boundary, factor-3 agreement)")
print(f"  DELTA_F10 = {DELTA_F10:.4f} OOM   (INFO/FAIL boundary, factor-10)")

# ============================================================
# SECTION 5: W1-2 reference A_s and ratio computation
# ============================================================
print("\n[SEC 5] Load W1-2 reference A_s and compute substrate-IC ratio")

W12_npz_path = os.path.join(HERE, 's82_w1_2_unified_as_79_full.npz')   # (local)
if os.path.exists(W12_npz_path):
    _d = np.load(W12_npz_path)
    A_s_W12 = float(np.atleast_1d(_d['A_s_A'])[0])                 # (local)
    H_tilde_W12 = float(np.atleast_1d(_d['H_tilde_A'])[0])         # (local)
    F_amp_W12 = float(np.atleast_1d(_d['F_amp_slot_adjusted'])[0])  # (local)
    c_sub_W12 = float(np.atleast_1d(_d['c_sub'])[0])               # (local)
    eps_H_W12 = float(np.atleast_1d(_d['eps_H'])[0])               # (local)
    f_conv_W12 = float(np.atleast_1d(_d['f_conv'])[0])             # (local)
    print(f"  A_s^W1-2 (TD-branch A) = {A_s_W12:.4e}")
    print(f"  H_tilde                = {H_tilde_W12:.5e}")
    print(f"  F_amp_slot_adjusted    = {F_amp_W12:.5e}")
    print(f"  c_sub                  = {c_sub_W12:.5e}")
    print(f"  eps_H                  = {eps_H_W12:.5e}")
    print(f"  f_conv                 = {f_conv_W12:.5e}")
else:
    # Fallback (should not happen; s82_w1_2 exists by dispatch-gate)
    A_s_W12 = 3.2994349182266295e-9       # (local) fallback
    print(f"  FALLBACK A_s^W1-2 = {A_s_W12:.4e}")

A_s_Planck = A_s_CMB                                               # 2.1e-9

# Under UNIFIED-AS-79, substrate-IC replaces the BD vacuum squeezing on F_amp:
#   A_s^substrate-IC = A_s^W1-2 * K_substrate
# The ratio to W1-2 is simply K_substrate (by construction of the pipeline).
print("\n[SEC 5.1] Substrate-IC A_s values per reading convention")


def compute_substrate_As(K, label):
    """Apply substrate-GGE K factor to W1-2 baseline and emit verdict."""
    A_s = K * A_s_W12                                              # (local)
    ratio_vs_W12 = A_s / A_s_W12                                   # (local) = K
    ratio_vs_Planck = A_s / A_s_Planck                             # (local)
    log10_ratio_W12 = np.log10(ratio_vs_W12)                       # (local)
    abs_log = abs(log10_ratio_W12)                                 # (local)
    if abs_log < DELTA_F3:
        verdict = 'PASS'
    elif abs_log < DELTA_F10:
        verdict = 'INFO'
    else:
        verdict = 'FAIL'
    print(f"  [{label}] K={K:.4f}, A_s={A_s:.4e}, "
          f"ratio_W1-2={ratio_vs_W12:.4f}, log10={log10_ratio_W12:+.4f}, "
          f"ratio_Planck={ratio_vs_Planck:.4f} -> {verdict}")
    return dict(label=label, K=K, A_s=A_s,
                ratio_vs_W12=ratio_vs_W12, ratio_vs_Planck=ratio_vs_Planck,
                log10_ratio_W12=log10_ratio_W12, abs_log=abs_log,
                verdict=verdict)


res_R1 = compute_substrate_As(K_R1, 'R1-B3-only')
res_R2 = compute_substrate_As(K_R2, 'R2-geo-mean')
res_R3 = compute_substrate_As(K_R3, 'R3-weighted-3/3/2')
res_R4 = compute_substrate_As(K_R4, 'R4-naive-59.8/8')
res_R5 = compute_substrate_As(K_R5, 'R5-B2-only')

# PRIMARY verdict = R3 (S43 gge-temp-43 documented multiplicity)
print(f"\n[SEC 5.2] PRIMARY verdict (R3 = weighted by S43 band multiplicity 3/3/2)")
primary = res_R3                                                   # (local)
print(f"  ratio = {primary['ratio_vs_W12']:.4f}")
print(f"  verdict = {primary['verdict']}")

# ============================================================
# SECTION 6: Cross-checks (machine-precision identities)
# ============================================================
print("\n[SEC 6] Cross-checks")

# CC1: structural bound — S_IC >= 1 for all bands (from n_k >= 0)
CC1 = (S_IC_B2 >= 1.0) and (S_IC_B1 >= 1.0) and (S_IC_B3 >= 1.0)    # (local)
print(f"  CC1 (structural S_IC >= 1 for all bands): {CC1}")

# CC2: per-band identity 1+2n = coth(x/2) * 1  (thermal GGE identity)
# coth(x/2) = (exp(x)+1)/(exp(x)-1) = 1 + 2/(exp(x)-1) = 1 + 2n
for label, x, S in [('B2',x_B2,S_IC_B2),('B1',x_B1,S_IC_B1),('B3',x_B3,S_IC_B3)]:
    coth_half = 1.0 / np.tanh(x/2.0)                               # (local)
    match = abs(S - coth_half) < 1e-12                             # (local)
    print(f"  CC2-{label}: 1+2n = {S:.8f} vs coth(x/2) = {coth_half:.8f} match={match}")

# CC3: R2 geometric mean >= min{S_B1,S_B2,S_B3} and <= max
CC3 = (min(S_IC_B2, S_IC_B1, S_IC_B3) <= K_R2 <= max(S_IC_B2, S_IC_B1, S_IC_B3))
print(f"  CC3 (R2 geo-mean in [min, max] of band values): {CC3}")

# CC4: R3 weighted average in [min, max]
CC4 = (min(S_IC_B2, S_IC_B1, S_IC_B3) <= K_R3 <= max(S_IC_B2, S_IC_B1, S_IC_B3))
print(f"  CC4 (R3 weighted in [min, max] of band values): {CC4}")

# CC5: Positivity of energy condition — K_substrate > 0
CC5 = (K_R1 > 0) and (K_R2 > 0) and (K_R3 > 0) and (K_R4 > 0) and (K_R5 > 0)
print(f"  CC5 (all K positive): {CC5}")

cross_checks_ok = CC1 and CC3 and CC4 and CC5                      # (local)
print(f"  ALL cross-checks pass: {cross_checks_ok}")

# ============================================================
# SECTION 7: Build closure SHA-256
# ============================================================
print("\n[SEC 7] Closure SHA-256")

closure_map = {
    'input_shas': INPUT_SHAS,
    'T_GGE': {'B2': T_GGE_B2, 'B1': T_GGE_B1_local, 'B3': T_GGE_B3_local},
    'Delta': {'B2': float(Delta_0_GL), 'B1': float(Delta_0_OES), 'B3': float(Delta_B3)},
    'mult': {'B2': mult_B2, 'B1': mult_B1, 'B3': mult_B3},
    'n_bands': {'B2': n_B2, 'B1': n_B1, 'B3': n_B3},
    'S_IC': {'B2': S_IC_B2, 'B1': S_IC_B1, 'B3': S_IC_B3},
    'K': {'R1': K_R1, 'R2': K_R2, 'R3': K_R3, 'R4': K_R4, 'R5': K_R5},
    'A_s_W12': A_s_W12,
    'A_s_Planck': A_s_Planck,
    'primary_K': primary['K'],
    'primary_ratio': primary['ratio_vs_W12'],
    'primary_verdict': primary['verdict'],
    'thresholds': {'F3': DELTA_F3, 'F10': DELTA_F10},
}                                                                  # (local)
closure_json = json.dumps(closure_map, sort_keys=True, default=float)  # (local)
closure_sha = hashlib.sha256(closure_json.encode('utf-8')).hexdigest()  # (local)
print(f"  closure_sha = {closure_sha}")

# ============================================================
# SECTION 8: 4-tuple tag + verdict line
# ============================================================
print("\n[SEC 8] 4-tuple tag")

four_tuple = (f"(value={primary['ratio_vs_W12']:.4f}, "
              f"scheme=GGE-WIGHTMAN, "
              f"convention=3HE-B-CORRESPONDENCE, "
              f"L_max=GGE-BAND-MULT-3/3/2)")                       # (local)
print(f"  4-tuple: {four_tuple}")

verdict_line = (f"S82-PS-SUBSTRATE-MATCHED-IC: {primary['verdict']} "
                f"-- value={primary['ratio_vs_W12']:.4f} "
                f"scheme=GGE-WIGHTMAN convention=3HE-B-CORRESPONDENCE "
                f"L_max=GGE-BAND-MULT-3-3-2 sha256={closure_sha}")  # (local)
print(f"\n[VERDICT LINE] {verdict_line}")

# ============================================================
# SECTION 9: Save NPZ + plot
# ============================================================
print("\n[SEC 9] Save outputs")

npz_path = os.path.join(HERE, 's82_w2_4_ps_substrate_matched_ic.npz')  # (local)
np.savez(npz_path,
         T_GGE_B2=T_GGE_B2, T_GGE_B1=T_GGE_B1_local, T_GGE_B3=T_GGE_B3_local,
         Delta_B2=float(Delta_0_GL), Delta_B1=float(Delta_0_OES),
         Delta_B3_val=float(Delta_B3),
         x_B2=x_B2, x_B1=x_B1, x_B3=x_B3,
         n_B2=n_B2, n_B1=n_B1, n_B3=n_B3,
         S_IC_B2=S_IC_B2, S_IC_B1=S_IC_B1, S_IC_B3=S_IC_B3,
         K_R1=K_R1, K_R2=K_R2, K_R3=K_R3, K_R4=K_R4, K_R5=K_R5,
         A_s_R1=res_R1['A_s'], A_s_R2=res_R2['A_s'],
         A_s_R3=res_R3['A_s'], A_s_R4=res_R4['A_s'],
         A_s_R5=res_R5['A_s'],
         ratio_R1=res_R1['ratio_vs_W12'], ratio_R2=res_R2['ratio_vs_W12'],
         ratio_R3=res_R3['ratio_vs_W12'], ratio_R4=res_R4['ratio_vs_W12'],
         ratio_R5=res_R5['ratio_vs_W12'],
         verdict_R1=res_R1['verdict'], verdict_R2=res_R2['verdict'],
         verdict_R3=res_R3['verdict'], verdict_R4=res_R4['verdict'],
         verdict_R5=res_R5['verdict'],
         A_s_W12=A_s_W12, A_s_Planck=A_s_Planck,
         primary_K=primary['K'], primary_ratio=primary['ratio_vs_W12'],
         primary_verdict=primary['verdict'],
         DELTA_F3=DELTA_F3, DELTA_F10=DELTA_F10,
         four_tuple=four_tuple,
         verdict_line=verdict_line,
         closure_sha=closure_sha,
         input_shas=np.array([f"{k}={v}" for k,v in INPUT_SHAS.items()]),
         mult_B2=mult_B2, mult_B1=mult_B1, mult_B3=mult_B3)
print(f"  NPZ saved: {npz_path}")

# Plot: left panel = mode-occupation n_k (per band), right = A_s ratio bar
fig, axes = plt.subplots(1, 2, figsize=(12, 5))                    # (local)

ax0 = axes[0]
bands = ['B2\n(flat)', 'B1\n(acoustic)', 'B3\n(softest)']          # (local)
n_vals = [n_B2, n_B1, n_B3]                                        # (local)
S_vals = [S_IC_B2, S_IC_B1, S_IC_B3]                               # (local)
x_pos = np.arange(len(bands))                                      # (local)
w = 0.35                                                           # (local)
ax0.bar(x_pos - w/2, n_vals, w, label='n_k^GGE', color='steelblue')
ax0.bar(x_pos + w/2, S_vals, w, label='S_IC = 1+2n_k', color='tomato')
ax0.set_xticks(x_pos); ax0.set_xticklabels(bands)
ax0.set_ylabel('Occupation / squeezing')
ax0.set_title('Substrate-GGE per-band Wightman\n(Volovik 3He-B correspondence)')
ax0.legend(loc='best')
ax0.grid(True, alpha=0.3)
ax0.axhline(1.0, color='gray', ls=':', alpha=0.5, label='_BD vacuum_')

ax1 = axes[1]
r_labels = ['R1\nB3-only', 'R2\ngeo-mean', 'R3\nweighted*', 'R4\nnaive59.8/8', 'R5\nB2-only']  # (local)
r_vals = [K_R1, K_R2, K_R3, K_R4, K_R5]                            # (local)
colors_r = ['tomato', 'orange', 'darkred', 'gray', 'steelblue']    # (local)
ax1.bar(r_labels, r_vals, color=colors_r, alpha=0.8)
ax1.axhline(1.0, color='black', ls='-', label='W1-2 reference (K=1)')
ax1.axhline(3.0, color='green', ls='--', label='PASS-F3 boundary')
ax1.axhline(10.0, color='red', ls='--', label='FAIL-GT10 boundary')
ax1.set_yscale('log')
ax1.set_ylabel('K_substrate = A_s^GGE / A_s^W1-2')
ax1.set_title('K_substrate across reading conventions\n(* = PRIMARY per S43 band mult)')
ax1.legend(loc='best')
ax1.grid(True, alpha=0.3)

plt.tight_layout()
plot_path = os.path.join(HERE, 's82_w2_4_ps_substrate_matched_ic.png')  # (local)
plt.savefig(plot_path, dpi=150)
plt.close()
print(f"  Plot saved: {plot_path}")

# ============================================================
# SECTION 10: Append verdict line to s82_gate_verdicts.txt
# ============================================================
verdict_path = os.path.join(HERE, 's82_gate_verdicts.txt')         # (local)
with open(verdict_path, 'a', encoding='utf-8') as fh:
    fh.write(verdict_line + '\n')
print(f"\n[SEC 10] Appended verdict to: {verdict_path}")

# ============================================================
# Final summary
# ============================================================
print("\n" + "=" * 70)
print("S82 W2-4 SUMMARY")
print("=" * 70)
print(f"Primary (R3 S43-multiplicity) K_substrate = {K_R3:.4f}")
print(f"A_s^substrate-IC (R3)                    = {res_R3['A_s']:.4e}")
print(f"A_s^W1-2 (TD-branch A)                   = {A_s_W12:.4e}")
print(f"ratio (substrate/W1-2)                   = {res_R3['ratio_vs_W12']:.4f}")
print(f"|log10 ratio|                            = {res_R3['abs_log']:.4f}")
print(f"VERDICT                                  = {primary['verdict']}")
print(f"4-tuple = {four_tuple}")
print(f"closure_sha = {closure_sha}")
print("=" * 70)
