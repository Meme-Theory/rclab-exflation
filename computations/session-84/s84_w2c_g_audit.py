#!/usr/bin/env python3
"""
S84-G-AUDIT -- Newton Constant Observational-Pinning Audit
==========================================================

Gate: S84-G-AUDIT  [VERIFY] + [SIGN]
Classification: GEOMETRIC (second Seeley-DeWitt moment -> Einstein-Hilbert coeff)
Owner: einstein-theorist (appended to W2c by orchestrator directive)

PURPOSE
-------
Test whether G is observationally pinned at NIST-BIPM 2026 G = 6.67387(38) x
10^-11 m^3 kg^-1 s^-2 (relative precision 5.7e-5) to a single (f_2 scheme x
M_KK route) combination under the s44 Eq A master equation:

    1/(16 pi G_N) = (6 / pi^3) * f_2 * a_2 * M_KK^2
    => G_N = pi^2 / (96 * f_2 * a_2 * M_KK^2)

PRE-REGISTERED SUBSTITUTION CHAIN (mandatory [VERIFY]+[SIGN])
--------------------------------------------------------------
Step 1 (def, master eq A):
    1/(16 pi G_N) = (6 / pi^3) * f_2 * a_2 * M_KK^2  [GeV^2 dimensionful]
Step 2 (def, observation):
    G_N(observed, natural) = 1 / (8 pi M_Pl_red^2)   [GeV^-2]
    where M_Pl_red = 2.435e18 GeV (canonical).
Step 3 (def, ratio):
    R(f_2, a_2, M_KK) = G_pred(f_2, a_2, M_KK) / G_obs
                      = [pi^2 / (96 f_2 a_2 M_KK^2)] / [1 / (8 pi M_Pl_red^2)]
                      = pi^3 M_Pl_red^2 / (12 f_2 a_2 M_KK^2)
Step 4 (substitute, gravity-route by construction):
    M_KK_grav := sqrt[ pi^3 M_Pl_red^2 / (12 a_2_used) ]
    => R(f_2=1, a_2_used, M_KK_grav) = 1.0  EXACTLY (calibration).
    Hence gravity-route is CIRCULAR -- excluded from verdict.
Step 5 (substitute, Kerner-route, INDEPENDENT):
    M_KK_kern := sqrt[ alpha_2_GUT * M_Pl_red^2 * g_SU2_fold ]  (s42)
    R(f_2, a_2, M_KK_kern) is a NON-CIRCULAR pin test.
Step 6 (read directions):
    d(ln G_N) / d(ln f_2)   = -1   -> f_2 up  => G_N down  => R down
    d(ln G_N) / d(ln a_2)   = -1   -> a_2 up  => G_N down  => R down
    d(ln G_N) / d(ln M_KK)  = -2   -> M_KK up => G_N down  => R down
Step 7 (verdict):
    PASS iff exactly one Kerner combination has |R - 1| < 5.7e-5.
    INFO-promotable iff multiple combinations within 5.7e-5.
    INFO-mostly-RD iff at least one Kerner combination within 1%.
    FAIL iff no Kerner combination within 1% after L_max convergence.
    PRE-REG-INCOMPLETE iff a_2 is not L_max-converged to 5.7e-5
        (factor-23 swing L=3 -> L=10 already disqualifies, see below).

GATE LEVELS (pre-registered)
-----------------------------
PASS:                exactly one Kerner R within 5.7e-5 of 1.0
INFO-promotable:     multiple Kerner R within 5.7e-5
INFO-mostly-RD:      no Kerner R within 5.7e-5, at least one within 1%
FAIL:                no Kerner R within 1%
PRE-REG-INCOMPLETE:  a_2 L_max-convergence to 5.7e-5 not demonstrated

L_MAX CONVERGENCE TEST
----------------------
Use s60_pw_h0_conv.npz (PW^2-weighted a_2 at L=0..7), s66_cutoff_ns.npz
(MAX_PQ_SUM=3 PW^2-weighted a_2 = 64308.24 = "L_max=10" plan label).
Test: fit a_2(L) ~ A * L^alpha; require relative residual < 5.7e-5 between
adjacent L values for convergence claim.

INPUTS
------
canonical_constants.py (M_Pl_reduced, M_KK_kerner, M_KK_gravity, f_2_default,
   a2_fold, tau_fold)
s61_heat_kernel_a2.npz   (cross-check, single-PW a_2 at L_max=3 via SD)
s76_bcs_dressing_a2.npz  (BCS dressing delta_a2 = -4.5006, 0.16% correction)
s42_constants_snapshot.npz (M_KK route definitions, a_2 spectral zeta)
s82_w2_5_heat_kernel_mp.npz (continuum-limit heat-kernel MP integrability)
s83_w3_g57_pinning_audit.py (closure structure reference)
s83_gate_verdicts.txt (S83 verdict ledger)
s60_pw_h0_conv.npz (PW^2-weighted a_2 L-scan L=0..7)
s66_cutoff_ns.npz (PW^2-weighted a_2 at MAX_PQ_SUM=3 = "L_max=10")

OUTPUTS
-------
s84_w2c_g_audit.npz  : route x scheme x L_max table, R = G_pred/G_obs
s84_w2c_g_audit.png  : convergence plot + ratio matrix visualization
verdict line appended to s84_gate_verdicts.txt

ENVIRONMENT
-----------
CPU only; thread cap 8; no heavy linear algebra (a_2 already cached).
"""
from __future__ import annotations

import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import sys
import math
import json
import hashlib
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from canonical_constants import (
    PI, M_Pl_reduced, M_KK_gravity, M_KK_kerner, f_2_default,
    a2_fold, tau_fold, Vol_SU3_Haar,
)

# =============================================================================
# 1. INPUT SHA-256 PINS (mandatory log in first 20 lines of stdout)
# =============================================================================
def sha256_of_file(p: Path) -> str:
    with open(p, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

INPUT_FILES = {
    'canonical_constants.py':   SCRIPT_DIR / 'canonical_constants.py',
    's61_heat_kernel_a2.npz':   SCRIPT_DIR / 's61_heat_kernel_a2.npz',
    's76_bcs_dressing_a2.npz':  SCRIPT_DIR / 's76_bcs_dressing_a2.npz',
    's42_constants_snapshot.npz': SCRIPT_DIR / 's42_constants_snapshot.npz',
    's82_w2_5_heat_kernel_mp.npz': SCRIPT_DIR / 's82_w2_5_heat_kernel_mp.npz',
    's83_w3_g57_pinning_audit.py': SCRIPT_DIR / 's83_w3_g57_pinning_audit.py',
    's83_gate_verdicts.txt':    SCRIPT_DIR / 's83_gate_verdicts.txt',
    's60_pw_h0_conv.npz':       SCRIPT_DIR / 's60_pw_h0_conv.npz',
    's66_cutoff_ns.npz':        SCRIPT_DIR / 's66_cutoff_ns.npz',
}

INPUT_SHAS = {name: sha256_of_file(p) for name, p in INPUT_FILES.items()}

print("=" * 78)
print("S84-G-AUDIT -- Newton Constant Observational-Pinning Audit")
print("=" * 78)
print("\nINPUT SHA-256 PINS:")
for name, sha in INPUT_SHAS.items():
    print(f"  {name}: {sha}")
print("=" * 78)

# Sanity-check 7 plan-pinned SHAs
PLAN_SHAS = {
    'canonical_constants.py':   'd49412402ad9e732a7a7270ee042e857e6899bdbc191de8237b7b96762fb28ec',
    's61_heat_kernel_a2.npz':   'aec4fb985e8e861675f8e4c850288f15e0d23f17f2493c31f477d6d77b8c1cae',
    's76_bcs_dressing_a2.npz':  '34b9b457a0a8f4bbba152f447c154d1ec031a9f44e128e20d5820d06a966df08',
    's42_constants_snapshot.npz': '39f613507950979327f0d9b7473bd73f7b0a7ea2d9d0c5507f6b8b939909f80b',
    's82_w2_5_heat_kernel_mp.npz': '125d57375989a15ad8c41a69b0434001f3b1e3e7073dda19f6c031d9e254cca6',
    's83_w3_g57_pinning_audit.py': 'db2958043020a8235eafcd225039defc2daca511fc44e3c140d87633feba9024',
    's83_gate_verdicts.txt':    '7bebad7da7c57b4d2706fd4e123cfbb762fa63c0244e143d597068fb7a574fb4',
}
for name, expected in PLAN_SHAS.items():
    got = INPUT_SHAS[name]
    if got != expected:
        print(f"\nSHA MISMATCH: {name}\n  expected={expected}\n  got     ={got}")
        sys.exit(1)
print("\n  All 7 plan-pinned SHAs MATCH.")

# =============================================================================
# 2. OBSERVATIONAL ANCHOR (NIST-BIPM 2026)
# =============================================================================
G_obs_SI = 6.67387e-11           # (local) m^3 kg^-1 s^-2 (NIST-BIPM 2026)
G_obs_sigma_SI = 0.38e-15        # (local) absolute uncertainty 5.7e-5 relative
G_obs_relative_precision = 5.7e-5  # (local) target tolerance for PASS

# Convert observed G_N to natural units (GeV^-2) via reduced Planck mass
# Definition: G_N = 1 / (8 pi M_Pl_red^2) in natural units; M_Pl_red is by
# definition consistent with the SI value. This gives the natural-unit anchor.
G_N_natural_obs = 1.0 / (8.0 * PI * M_Pl_reduced**2)  # (local) GeV^-2

print(f"\nObservational anchor (NIST-BIPM 2026):")
print(f"  G_obs (SI)            = {G_obs_SI:.5e} +/- {G_obs_sigma_SI:.2e} m^3 kg^-1 s^-2")
print(f"  Relative precision    = {G_obs_relative_precision:.2e}")
print(f"  G_N (natural, GeV^-2) = {G_N_natural_obs:.6e}  [via M_Pl_red={M_Pl_reduced:.4e} GeV]")

# =============================================================================
# 3. f_2 SCHEME ENUMERATION (plan §W2c-G-AUDIT machinery pin)
# =============================================================================
F2_SCHEMES = {
    'sharp':     1.0,         # f_2 for sharp cutoff
    'Gaussian':  2.34,        # f_2_default canonical (Connes-Chamseddine 2007)
    'SDW-L2':    2.0/3.0,     # SDW L^2 cutoff
    'f*':        214.97,      # f* anomaly-derived (s75)
}

# =============================================================================
# 4. M_KK ROUTES
# =============================================================================
# gravity route: by construction matches G_N (CIRCULAR)
# Kerner route: M_KK^2 = alpha_2_GUT * M_Pl_red^2 * g_SU2_fold (INDEPENDENT)
M_KK_ROUTES = {
    'gravity_CIRCULAR':  M_KK_gravity,    # 7.43e16 GeV
    'Kerner_INDEP':      M_KK_kerner,     # 5.04e17 GeV
}

# =============================================================================
# 5. a_2 NORMALIZATIONS AND L-SCAN
# =============================================================================
# The framework has TWO a_2 normalizations:
#  (A) single-PW weight d_pq:    a_2_PW1  -- canonical S42 a2_fold = 2776.17 at L=3
#  (B) double-PW weight d_pq^2:  a_2_PW2  -- s66 MAX_PQ_SUM=3 = 64308.24
# The plan describes "L_max=3" (2776) and "L_max=10" (64308) as different L_max
# but they are different PW-weight conventions. We test BOTH and treat the
# weight ambiguity as a CONVENTION-FREEDOM contributing to PRE-REG-INCOMPLETE.

a2_PW1_S42 = 2776.1653888633655  # (local) S42 single-PW d_pq weight, L_max=3
a2_PW2_S66 = 64308.2438882544    # (local) S66 double-PW d_pq^2 weight, MAX_PQ_SUM=3

# BCS dressing correction (s76)
delta_a2_BCS = -4.50060419255351 # (local) s76 single-PW dressing correction
a2_PW1_BCS = a2_PW1_S42 + delta_a2_BCS  # (local) BCS-dressed single-PW
# For PW^2 weight, scale linearly (correction is per-mode):
delta_a2_PW2_BCS = a2_PW2_S66 * (delta_a2_BCS / a2_PW1_S42)  # (local)
a2_PW2_BCS = a2_PW2_S66 + delta_a2_PW2_BCS                   # (local)

print(f"\na_2 NORMALIZATION SUMMARY:")
print(f"  S42 PW^1 (single d_pq weight):  a_2 = {a2_PW1_S42:.4f}  [canonical a2_fold]")
print(f"  S42 PW^1 + BCS dressing:        a_2 = {a2_PW1_BCS:.4f}  (delta = {delta_a2_BCS:+.4f}, {100*delta_a2_BCS/a2_PW1_S42:+.3f}%)")
print(f"  S66 PW^2 (double d_pq^2 weight): a_2 = {a2_PW2_S66:.4f}  [\"L_max=10\" plan label]")
print(f"  S66 PW^2 + BCS dressing:        a_2 = {a2_PW2_BCS:.4f}  (delta = {delta_a2_PW2_BCS:+.4f}, {100*delta_a2_PW2_BCS/a2_PW2_S66:+.3f}%)")

# L-scan from s60 (PW^2 weighting, L=0..7)
d60 = np.load(SCRIPT_DIR / 's60_pw_h0_conv.npz', allow_pickle=True)
L_arr = np.array(d60['L_arr'])           # (local) [0..7]
a2_PW2_L_scan = np.array(d60['a2_cumul'])  # (local) PW^2 cumulative a_2 vs L

print(f"\nL_max CONVERGENCE TEST (PW^2 weighting, s60 cumulative):")
for L_i, a2_i in zip(L_arr, a2_PW2_L_scan):
    print(f"  L_max = {L_i}: a_2 = {a2_i:.4e}")

# Convergence test: compute relative jump |a_2(L+1) - a_2(L)| / a_2(L)
print(f"\nRELATIVE INCREMENTS |a_2(L+1) - a_2(L)| / a_2(L):")
rel_jump = np.zeros(len(L_arr) - 1)  # (local)
for i in range(len(L_arr) - 1):
    rel_jump[i] = abs(a2_PW2_L_scan[i+1] - a2_PW2_L_scan[i]) / a2_PW2_L_scan[i]
    print(f"  L={L_arr[i]} -> L={L_arr[i+1]}: rel jump = {rel_jump[i]:.4e}")
final_jump = rel_jump[-1]  # (local) L=6 -> L=7
print(f"\n  Final increment (L=6->7) = {final_jump:.4e}")
print(f"  Required for 5.7e-5 PASS = {G_obs_relative_precision:.2e}")
print(f"  Convergence ratio        = {final_jump / G_obs_relative_precision:.2f}x  (need < 1)")

# Power-law fit a_2(L) ~ A L^alpha (use L >= 2 to avoid low-L noise)
mask_fit = L_arr >= 2
log_L = np.log(L_arr[mask_fit].astype(float))      # (local)
log_a2 = np.log(a2_PW2_L_scan[mask_fit])           # (local)
alpha_fit, log_A_fit = np.polyfit(log_L, log_a2, 1)  # (local)
A_fit = np.exp(log_A_fit)                          # (local)
print(f"\nPower-law fit a_2(L) ~ A L^alpha (L >= 2):")
print(f"  alpha = {alpha_fit:.4f}")
print(f"  A     = {A_fit:.4e}")

# Richardson extrapolation: assume a_2(L) = a_2_inf + B/L^p
# Try fitting to a divergent power law (alpha > 0 means a_2 -> infinity, NOT
# convergent)
if alpha_fit > 0:
    print(f"\n  WARNING: alpha = {alpha_fit:.3f} > 0 means PW^2 a_2(L) is DIVERGENT.")
    print(f"  No finite L_max -> infinity limit exists for this normalization.")
    print(f"  Richardson extrapolation NOT APPLICABLE -- a_2 has no convergent value.")
    a2_inf_estimate = None  # (local)
    converged_bool = False  # (local)
else:
    # Convergent case: fit a_2(L) = a_2_inf + B/L^|alpha|
    # We do not fit it here because alpha > 0 is overwhelmingly likely;
    # the framework already documents alpha ~ 6.24 (s60_pw_h0_conv).
    a2_inf_estimate = None  # (local)
    converged_bool = False  # (local)

# =============================================================================
# 6. MASTER EQUATION: G_pred = pi^2 / (96 f_2 a_2 M_KK^2)
# =============================================================================
def G_pred_natural(f_2: float, a_2: float, M_KK: float) -> float:
    """G_N predicted from spectral action master equation, natural units (GeV^-2).

    Substitution chain:
      1/(16 pi G_N) = (6 / pi^3) * f_2 * a_2 * M_KK^2     (Eq A, s44)
      => 16 pi G_N = pi^3 / (6 f_2 a_2 M_KK^2)
      => G_N = pi^2 / (96 f_2 a_2 M_KK^2)                 [GeV^-2]
    """
    return PI**2 / (96.0 * f_2 * a_2 * M_KK**2)

# =============================================================================
# 7. RATIO MATRIX: route x scheme x L_max
# =============================================================================
# We evaluate at THREE L_max levels:
#   L=3 PW^1 (canonical S42 a_2 = 2776.17)
#   L=3 PW^1 + BCS dressing
#   L=10 PW^2 plan-label (a_2 = 64308.24)
#   L=10 PW^2 + BCS dressing
#   PLUS: full L=0..7 PW^2 scan from s60 to expose divergence

a2_eval_panels = {
    'PW1_L3':          a2_PW1_S42,
    'PW1_L3_BCS':      a2_PW1_BCS,
    'PW2_L10_plan':    a2_PW2_S66,
    'PW2_L10_BCS':     a2_PW2_BCS,
}

n_routes  = len(M_KK_ROUTES)
n_schemes = len(F2_SCHEMES)
n_panels  = len(a2_eval_panels)

# Tensor: ratio[panel, route, scheme] = G_pred / G_obs
ratio_tensor = np.zeros((n_panels, n_routes, n_schemes))  # (local)

panel_names = list(a2_eval_panels.keys())  # (local)
route_names = list(M_KK_ROUTES.keys())     # (local)
scheme_names = list(F2_SCHEMES.keys())     # (local)

print(f"\n" + "=" * 78)
print(f"7. RATIO MATRIX: G_pred / G_obs across (panel, route, scheme)")
print(f"=" * 78)

for ip, panel in enumerate(panel_names):
    a2_use = a2_eval_panels[panel]  # (local)
    print(f"\nPANEL: {panel}  (a_2 = {a2_use:.4f})")
    print(f"  {'route':22s} {'scheme':10s} {'f_2':>8s} {'M_KK (GeV)':>12s} {'G_pred/G_obs':>14s}")
    for ir, route in enumerate(route_names):
        M_KK_use = M_KK_ROUTES[route]  # (local)
        for js, scheme in enumerate(scheme_names):
            f2_use = F2_SCHEMES[scheme]  # (local)
            G_p = G_pred_natural(f2_use, a2_use, M_KK_use)  # (local)
            R = G_p / G_N_natural_obs                       # (local)
            ratio_tensor[ip, ir, js] = R
            tag = ' (CIRCULAR)' if 'CIRCULAR' in route else ''  # (local)
            print(f"  {route:22s} {scheme:10s} {f2_use:8.3f} {M_KK_use:12.4e} {R:14.6e}{tag}")

# =============================================================================
# 8. SIGN-DIRECTION VERIFICATION (substitution chain numeric check)
# =============================================================================
print(f"\n" + "=" * 78)
print(f"8. SIGN/DIRECTION VERIFICATION (numerical check of d ln G / d ln *)")
print(f"=" * 78)
print("Master equation: G_N = pi^2 / (96 f_2 a_2 M_KK^2)")
print("Predicted: d(ln G)/d(ln f_2) = -1, d(ln G)/d(ln a_2) = -1, d(ln G)/d(ln M_KK) = -2")

ref_a2  = a2_PW1_S42       # (local)
ref_f2  = 1.0              # (local)
ref_MKK = M_KK_kerner      # (local)
ref_G   = G_pred_natural(ref_f2, ref_a2, ref_MKK)  # (local)

eps = 1e-3  # (local) finite-difference step
# d(ln G)/d(ln f_2)
G_up_f2 = G_pred_natural(ref_f2*(1+eps), ref_a2, ref_MKK)  # (local)
deriv_f2 = (np.log(G_up_f2) - np.log(ref_G)) / np.log(1+eps)  # (local)
# d(ln G)/d(ln a_2)
G_up_a2 = G_pred_natural(ref_f2, ref_a2*(1+eps), ref_MKK)  # (local)
deriv_a2 = (np.log(G_up_a2) - np.log(ref_G)) / np.log(1+eps)  # (local)
# d(ln G)/d(ln M_KK)
G_up_MKK = G_pred_natural(ref_f2, ref_a2, ref_MKK*(1+eps))  # (local)
deriv_MKK = (np.log(G_up_MKK) - np.log(ref_G)) / np.log(1+eps)  # (local)

print(f"\n  d(ln G)/d(ln f_2)  measured = {deriv_f2:.6f}  (predicted -1)")
print(f"  d(ln G)/d(ln a_2)  measured = {deriv_a2:.6f}  (predicted -1)")
print(f"  d(ln G)/d(ln M_KK) measured = {deriv_MKK:.6f}  (predicted -2)")

sign_check_pass = (
    abs(deriv_f2 - (-1.0)) < 1e-2
    and abs(deriv_a2 - (-1.0)) < 1e-2
    and abs(deriv_MKK - (-2.0)) < 1e-2
)
print(f"  SIGN-DIRECTION CHECK: {'PASS' if sign_check_pass else 'FAIL'}")

# =============================================================================
# 9. VERDICT DETERMINATION (pre-registered branches)
# =============================================================================
print(f"\n" + "=" * 78)
print(f"9. VERDICT DETERMINATION")
print(f"=" * 78)

# Find Kerner combinations with smallest |R - 1|
# Exclude gravity-route (CIRCULAR by construction)
ir_kerner = route_names.index('Kerner_INDEP')  # (local)

# Best Kerner R across all panels, all schemes
deviations = np.zeros((n_panels, n_schemes))  # (local) |R - 1|
for ip in range(n_panels):
    for js in range(n_schemes):
        deviations[ip, js] = abs(ratio_tensor[ip, ir_kerner, js] - 1.0)

# Find best (smallest deviation) Kerner combination
best_ip, best_js = np.unravel_index(np.argmin(deviations), deviations.shape)  # (local)
best_dev = deviations[best_ip, best_js]                                       # (local)
best_R = ratio_tensor[best_ip, ir_kerner, best_js]                            # (local)
best_panel = panel_names[best_ip]                                             # (local)
best_scheme = scheme_names[best_js]                                           # (local)
best_a2 = a2_eval_panels[best_panel]                                          # (local)
best_f2 = F2_SCHEMES[best_scheme]                                             # (local)

print(f"\nBest Kerner-route combination (smallest |R - 1|):")
print(f"  panel  = {best_panel}")
print(f"  scheme = {best_scheme}")
print(f"  a_2    = {best_a2:.4f}")
print(f"  f_2    = {best_f2:.4f}")
print(f"  R = G_pred/G_obs = {best_R:.6e}")
print(f"  |R - 1| = {best_dev:.6e}")

# Count combinations within 5.7e-5 and within 1%
n_within_5p7e5 = int(np.sum(deviations < G_obs_relative_precision))  # (local)
n_within_1pct = int(np.sum(deviations < 0.01))                       # (local)
print(f"\nKerner combinations within 5.7e-5 (PASS threshold): {n_within_5p7e5}")
print(f"Kerner combinations within 1.0%   (INFO-mostly-RD threshold): {n_within_1pct}")

# Verdict logic per plan §W2c-G-AUDIT
# Convergence prerequisite: PW^2 a_2 must be L_max-converged to 5.7e-5
# We measured rel_jump[L=6->L=7] >> 5.7e-5 -> NOT converged -> PRE-REG-INCOMPLETE
PRE_REG_INCOMPLETE = (final_jump > G_obs_relative_precision)  # (local)

if not PRE_REG_INCOMPLETE:
    if n_within_5p7e5 == 1:
        verdict = 'PASS'
        verdict_value = f"{best_R:.6e}"
        verdict_scheme = best_scheme
    elif n_within_5p7e5 > 1:
        verdict = 'INFO'
        verdict_value = f"{best_R:.6e}"
        verdict_scheme = 'multi-pin-promotable'
    elif n_within_1pct >= 1:
        verdict = 'INFO'
        verdict_value = f"{best_R:.6e}"
        verdict_scheme = 'mostly-RD'
    else:
        verdict = 'FAIL'
        verdict_value = f"{best_R:.6e}"
        verdict_scheme = best_scheme
else:
    # Plan PRU Class 8: a_2 not L_max-converged to required precision
    verdict = 'PRE-REG-INCOMPLETE'
    verdict_value = 'null'
    verdict_scheme = 'null'

print(f"\n" + "=" * 78)
print(f"VERDICT: {verdict}")
print(f"=" * 78)
print(f"Reasons:")
if PRE_REG_INCOMPLETE:
    print(f"  - PW^2 a_2 final L-increment {final_jump:.2e} >> 5.7e-5 target")
    print(f"  - alpha_fit = {alpha_fit:.3f} > 0 means a_2(L) is DIVERGENT in L")
    print(f"  - No L_max -> infinity limit exists for this normalization")
    print(f"  - PRU Class 8 (Pre-Registration Underspecification: a_2 normalization unpinned)")
print(f"  - Best Kerner R = {best_R:.4e}, deviation {best_dev:.4e}")
print(f"  - Master-equation prefactor convention spread (s42, s61, s62, s64, s65, plan)")
print(f"    documented; see working paper §W2-G-AUDIT.")

# =============================================================================
# 10. SHA CLOSURE
# =============================================================================
# Build ordered input-pin map (sorted by name); SHA over JSON-serialized form
ordered_input_map = {k: INPUT_SHAS[k] for k in sorted(INPUT_SHAS.keys())}  # (local)
input_map_json = json.dumps(ordered_input_map, sort_keys=True, separators=(',', ':'))  # (local)
closure_sha = hashlib.sha256(input_map_json.encode('utf-8')).hexdigest()  # (local)

print(f"\n" + "=" * 78)
print(f"10. CLOSURE SHA-256")
print(f"=" * 78)
print(f"  closure_sha = {closure_sha}")

# =============================================================================
# 11. SAVE NPZ
# =============================================================================
np.savez(
    SCRIPT_DIR / 's84_w2c_g_audit.npz',
    # Inputs and metadata
    panel_names=np.array(panel_names),
    route_names=np.array(route_names),
    scheme_names=np.array(scheme_names),
    f2_values=np.array([F2_SCHEMES[s] for s in scheme_names]),
    M_KK_values=np.array([M_KK_ROUTES[r] for r in route_names]),
    a2_panel_values=np.array([a2_eval_panels[p] for p in panel_names]),
    # Results
    ratio_tensor=ratio_tensor,
    deviations=deviations,
    G_obs_natural=G_N_natural_obs,
    G_obs_SI=G_obs_SI,
    G_obs_relative_precision=G_obs_relative_precision,
    # L-scan
    L_arr=L_arr,
    a2_PW2_L_scan=a2_PW2_L_scan,
    rel_jump=rel_jump,
    alpha_fit=alpha_fit,
    A_fit=A_fit,
    final_jump=final_jump,
    # Sign check
    deriv_f2_measured=deriv_f2,
    deriv_a2_measured=deriv_a2,
    deriv_MKK_measured=deriv_MKK,
    sign_check_pass=sign_check_pass,
    # Best result
    best_panel=best_panel,
    best_scheme=best_scheme,
    best_R=best_R,
    best_dev=best_dev,
    n_within_5p7e5=n_within_5p7e5,
    n_within_1pct=n_within_1pct,
    # Verdict
    verdict=verdict,
    verdict_value=verdict_value,
    verdict_scheme=verdict_scheme,
    PRE_REG_INCOMPLETE=PRE_REG_INCOMPLETE,
    # SHAs
    closure_sha=closure_sha,
    input_shas=np.array([f"{k}={v}" for k, v in ordered_input_map.items()]),
    four_tuple=f"(value={verdict_value}, scheme={verdict_scheme}, convention=Eq-A-SA-canonical, L_max=10)",
)

# =============================================================================
# 12. PLOT
# =============================================================================
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# (a) L_max convergence of PW^2 a_2
ax = axes[0]
ax.loglog(L_arr[1:], a2_PW2_L_scan[1:], 'o-', color='C0', label='PW^2 a_2 (s60)')
L_smooth = np.linspace(1.0, 8.0, 50)  # (local)
a2_smooth = A_fit * L_smooth ** alpha_fit  # (local)
ax.loglog(L_smooth, a2_smooth, '--', color='C1', alpha=0.7,
          label=f'fit: {A_fit:.2e} L^{alpha_fit:.2f}')
ax.axhline(a2_PW2_S66, color='C2', linestyle=':', label=f'S66 \"L_max=10\" = {a2_PW2_S66:.0f}')
ax.set_xlabel('L_max')
ax.set_ylabel('a_2 (PW^2 weighted)')
ax.set_title(f'a_2 L-convergence (DIVERGENT, alpha={alpha_fit:.2f} > 0)')
ax.legend(loc='best', fontsize=9)
ax.grid(True, alpha=0.3, which='both')

# (b) Ratio matrix heatmap (Kerner only, all panels x schemes)
ax = axes[1]
ratios_display = ratio_tensor[:, ir_kerner, :]  # (local)  shape (n_panels, n_schemes)
log_ratio = np.log10(ratios_display)            # (local)
vmax = max(2.0, np.max(np.abs(log_ratio)))      # (local)
im = ax.imshow(log_ratio, cmap='RdBu_r', vmin=-vmax, vmax=vmax, aspect='auto')
ax.set_xticks(range(n_schemes))
ax.set_xticklabels(scheme_names, rotation=45, ha='right')
ax.set_yticks(range(n_panels))
ax.set_yticklabels(panel_names)
for ip in range(n_panels):
    for js in range(n_schemes):
        ax.text(js, ip, f"{ratios_display[ip, js]:.2e}",
                ha='center', va='center',
                color='white' if abs(log_ratio[ip, js]) > 1.5 else 'black',
                fontsize=8)
plt.colorbar(im, ax=ax, label='log10(G_pred / G_obs)')
ax.set_title(f'Kerner-route G_pred/G_obs (target = 1.0; PASS within 5.7e-5)')

plt.tight_layout()
plt.savefig(SCRIPT_DIR / 's84_w2c_g_audit.png', dpi=150, bbox_inches='tight')
plt.close()

# =============================================================================
# 13. APPEND VERDICT LINE
# =============================================================================
verdict_line = (
    f"S84-G-AUDIT: {verdict} -- value={verdict_value} "
    f"scheme={verdict_scheme} convention=Eq-A-SA-canonical L_max=10 "
    f"sha256={closure_sha}"
)

verdict_file = SCRIPT_DIR / 's84_gate_verdicts.txt'
with open(verdict_file, 'a') as f:
    f.write(verdict_line + "\n")

print(f"\n" + "=" * 78)
print(f"VERDICT LINE APPENDED to {verdict_file.name}:")
print(f"=" * 78)
print(verdict_line)

# Final 4-tuple line
print(f"\n(value={verdict_value}, scheme={verdict_scheme}, convention=Eq-A-SA-canonical, L_max=10)")
