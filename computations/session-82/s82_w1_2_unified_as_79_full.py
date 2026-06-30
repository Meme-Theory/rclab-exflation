#!/usr/bin/env python3
"""
S82 W1-2: UNIFIED-AS-79-FULL (CF-4) — A_s^framework five-factor decomposition.
==============================================================================

Gate: S82-UNIFIED-AS-79-FULL  [VERIFY] + [CHAIN]
Classification: PHONONIC
Owner: transit-dynamics-theorist
Critical to S82-MASTER: YES

Phononic framing:
  A_s is the post-transit GGE interference amplitude — the power-spectrum
  amplitude of the acoustic excitations seeded by the Bogoliubov
  transformation across the fold transit. This is NOT a vacuum fluctuation
  in inflating spacetime; it is the squeezed-state occupation spectrum of
  the Ordered Veil's phononic excitations. UNIFIED-AS-79 is the canonical
  A_s-ledger installed by S79 P2-A, replacing the earlier Mukhanov-style
  accounting that failed at 3.36 OOM.

S82 execution notes:
  * W1-1 H̃-EPOCH verdict has NOT landed in S82 at the time of this run.
    Per S82 task spec, this agent executes in BRANCH-CONDITIONAL MODE,
    using the S80 W1-1 dual-owner outputs as authoritative inputs:
      - Branch TD-framework: H_tilde = 5.90760e-03 (zeta, substrate-native,
        L_max=3, at N_pivot=55; source: s80_h_tilde_epoch_td.npz)
      - Branch LI:           H_tilde = 2.46411e-05 (SDW, epoch-resolved-a_2,
        L_max=5; source: s80_h_tilde_epoch_lizzi.npz)
    The S80 convergence-note pinned these as DIVERGED (rel_diff 99.6% at
    Path A). The dual-branch verdict is emitted here as -A (TD Path A-equiv)
    and -B (LI).
  * If W1-1 lands in S82 later (convergent within 20%), this file's
    verdict lines remain authoritative for the S82 branch-conditional pass;
    a convergent single-line -CONV verdict requires a W2-1 REPLAY.

Pre-registered substitution chain (per S80 plan L886-L933, VERBATIM):
  Factor 1: H_tilde   — from W1-1 4-tuple (dual-branch, DIVERGED).
  Factor 2: eps_H     = 0.02163  (one-loop slow-roll, S75/S77 canonical).
  Factor 3: F_amp     = F_amp_canonical * k_a2 = 1.0166 * 0.3822
                      (S78 W1-A after W0-5 slot-audit; a_2 slot SUPPRESSES).
  Factor 4: c_sub     = 2.238    (central of S78 W2-E three-scheme range
                                   {2.232, 2.244, 3.647}).
  Factor 5: f_conv    = 9.30e-4  (single (M_KK/M_Pl_red)^2 KK hierarchy
                                   factor; do NOT double-count per S78
                                   Transit-Einstein open item).

  Substitution step:
    A_s^framework = (H_tilde^2 / (8 pi^2)) * (1/eps_H) * F_amp * (1/c_sub) * f_conv

  Simplification (regime-of-validity check):
    Under UNIFIED-AS-79, H_tilde^2 carries the substrate-Friedmann
    prefactor, 1/eps_H is the canonical slow-roll mapping, F_amp carries
    the a_2-slot amplification/suppression from the Seeley-DeWitt ledger,
    c_sub^{-1} is the Mellin-weight subhorizon matching (S78 W2-E), and
    f_conv rescales substrate-internal units (M_KK^2) to physical A_s
    units (M_Pl_red^{-2}). All five factors are multiplicative; there is
    no cross-correlation under the P2-A ledger replacement.

  Direction read-off (this script is the mechanism for the direction claim,
  not the rhetoric):
    See Python substitution verification at runtime. The verdict is an
    OUTPUT, not a pre-asserted direction, per .claude/rules/math-scripts.md
    §"When the chain is NOT required".

Pre-registered thresholds (S80 plan L880-L882):
  PASS (factor-2): |A_s^framework - 2.1e-9| / 2.1e-9 < 1.0,
                   equivalently |delta_OOM| < log10(2) = 0.30103.
  INFO (factor-15): |delta_OOM| in [log10(2), log10(15)] = [0.301, 1.176].
  FAIL (> factor-15): |delta_OOM| >= log10(15) = 1.17609.

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

# Canonical constants (MANDATORY import per project rules)
from canonical_constants import (
    M_KK_gravity,
    M_Pl_reduced,
    a0_fold,
    A_s_CMB,
)

# ============================================================
# SECTION 0: Input SHA-256 pins (MANDATORY in first 20 lines)
# ============================================================
HERE = os.path.dirname(os.path.abspath(__file__))                  # (local)


def _sha256(path):
    """Compute SHA-256 of a file."""
    with open(path, 'rb') as h:
        return hashlib.sha256(h.read()).hexdigest()


INPUT_FILES = [                                                    # (local)
    os.path.join(HERE, 'canonical_constants.py'),
    os.path.join(HERE, 's80_unified_as_79_full.py'),
    os.path.join(HERE, 's80_unified_as_79_full.npz'),
    os.path.join(HERE, 's80_h_tilde_epoch_td.npz'),
    os.path.join(HERE, 's80_h_tilde_epoch_lizzi.npz'),
    os.path.join(HERE, 's80_h_tilde_epoch_lizzi_convergence_note.txt'),
]

print("=" * 70)
print("S82 W1-2: UNIFIED-AS-79-FULL (CF-4, branch-conditional)")
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
# SECTION 1: BRANCH INPUTS (from W1-1 dual-owner, DIVERGED)
# ============================================================
print("\n[SEC 1] W1-1 dual-branch inputs (DIVERGED per s80 convergence note)")

# Branch A := TD-framework (zeta / substrate-native / L_max=3, at N_pivot=55)
H_tilde_A = 5.90760e-03              # (local) TD-framework, from s80_h_tilde_epoch_td.npz
scheme_A = 'zeta'                    # (local)
convention_A = 'substrate-native'    # (local)
L_max_A = 3                          # (local)

# Branch B := LI (SDW / epoch-resolved-a_2 / L_max=5)
H_tilde_B = 2.46411e-05              # (local) LI verdict, from s80_h_tilde_epoch_lizzi.npz
scheme_B = 'SDW'                     # (local)
convention_B = 'epoch-resolved-a2'   # (local)
L_max_B = 5                          # (local)

# Reference diagnostics (NOT verdict branches)
H_tilde_TD_pathB_ref = 1.941e-02     # (local) TD Path B fold-epoch (diagnostic)
H_tilde_LI_obsinv_ref = 5.989e-05    # (local) LI obs-inverse calibration (tautological)

print(f"  Branch A (TD-framework, zeta):  H_tilde = {H_tilde_A:.6e}")
print(f"    (scheme={scheme_A}, convention={convention_A}, L_max={L_max_A})")
print(f"  Branch B (LI, SDW):             H_tilde = {H_tilde_B:.6e}")
print(f"    (scheme={scheme_B}, convention={convention_B}, L_max={L_max_B})")
print(f"  OOM gap (log10 A/B) = {np.log10(H_tilde_A/H_tilde_B):+.4f}")

# ============================================================
# SECTION 2: COMMON FACTOR VALUES (S80 plan L895-L918)
# ============================================================
print("\n[SEC 2] Common factor inputs (per S80 plan L895-L918)")

eps_H = 0.02163                      # (local) one-loop slow-roll, S75/S77 canonical (S80 plan L906)
c_sub = 2.238                        # (local) S78 W2-E three-scheme central (2.232/2.244/3.647)
f_conv = 9.30e-4                     # (local) (M_KK/M_Pl_red)^2 single KK hierarchy
k_a2 = 0.3822                        # (local) W0-5 a_2-slot factor (SUPPRESS; 0.382 per plan L908)
F_amp_canonical = 1.0166             # (local) S80 W1-B-REMED Method B pinned value
F_amp_slot_adjusted = F_amp_canonical * k_a2    # (local) F_amp after W0-5 slot-audit

A_s_Planck = A_s_CMB                 # 2.1e-9 from canonical_constants

print(f"  eps_H              = {eps_H:.5f}")
print(f"  c_sub              = {c_sub:.4f}  (central of 2.232/2.244/3.647)")
print(f"  f_conv             = {f_conv:.4e}  (M_KK/M_Pl_red)^2, single KK hierarchy")
print(f"  F_amp_canonical    = {F_amp_canonical:.6f}")
print(f"  k_a2 (W0-5 slot)   = {k_a2:.6f}  (a_2 slot SUPPRESSES)")
print(f"  F_amp_slot_adjusted= {F_amp_slot_adjusted:.6f} = {F_amp_canonical:.4f} * {k_a2:.4f}")
print(f"  A_s_Planck         = {A_s_Planck:.3e}  (Planck 2018, canonical_constants)")

# ============================================================
# SECTION 3: PRE-REGISTERED THRESHOLDS
# ============================================================
DELTA_F2 = np.log10(2.0)             # (local) = 0.30103; PASS if |delta_OOM| < 0.30103
DELTA_F15 = np.log10(15.0)           # (local) = 1.17609; INFO if |delta_OOM| in [0.30103, 1.17609]
print("\n[SEC 3] Pre-registered thresholds")
print(f"  DELTA_F2  = {DELTA_F2:.5f} OOM (PASS boundary; |delta_OOM| < this)")
print(f"  DELTA_F15 = {DELTA_F15:.5f} OOM (INFO/FAIL boundary; |delta_OOM| < this)")

# ============================================================
# SECTION 4: UNIFIED-AS-79 per-branch computation
# ============================================================


def unified_as_79(H_tilde, label, scheme_tag, convention_tag, L_max_tag):
    """Compute A_s^framework under UNIFIED-AS-79 with substitution chain printed.

    Returns a dict with all factor values, cumulative product, delta_OOM,
    and verdict.
    """
    print(f"\n--- BRANCH {label} ---")
    print(f"  Factor 1: H_tilde = {H_tilde:.6e}  (from W1-1 4-tuple)")
    print(f"  Factor 2: eps_H   = {eps_H:.5f}")
    print(f"  Factor 3: F_amp   = {F_amp_slot_adjusted:.6f}  "
          f"(= {F_amp_canonical:.4f} x {k_a2:.4f})")
    print(f"  Factor 4: c_sub   = {c_sub:.4f}")
    print(f"  Factor 5: f_conv  = {f_conv:.4e}")

    # Canonical form:
    # A_s = (H_tilde^2 / (8*pi^2)) * (1/eps_H) * F_amp * (1/c_sub) * f_conv
    term_1 = H_tilde**2 / (8.0 * np.pi**2)                         # (local) H^2/(8 pi^2)
    term_2 = 1.0 / eps_H                                            # (local) inverse slow-roll
    term_3 = F_amp_slot_adjusted                                    # (local) slot-adjusted F_amp
    term_4 = 1.0 / c_sub                                            # (local) subhorizon damping
    term_5 = f_conv                                                 # (local) physical conversion

    # Cumulative product at each step
    acc_a = term_1                                                  # (local)
    acc_b = acc_a * term_2                                          # (local)
    acc_c = acc_b * term_3                                          # (local)
    acc_d = acc_c * term_4                                          # (local)
    acc_e = acc_d * term_5                                          # (local)

    A_s = acc_e                                                     # (local)
    ratio = A_s / A_s_Planck                                        # (local)
    delta_OOM = np.log10(abs(ratio)) if ratio > 0 else float('-inf')  # (local)

    print(f"  Step-a: H_tilde^2/(8 pi^2)       = {acc_a:.6e}")
    print(f"  Step-b: * 1/eps_H               -> {acc_b:.6e}")
    print(f"  Step-c: * F_amp (slot-adjusted) -> {acc_c:.6e}")
    print(f"  Step-d: * 1/c_sub               -> {acc_d:.6e}")
    print(f"  Step-e: * f_conv                -> {acc_e:.6e}")
    print(f"  A_s^framework            = {A_s:.6e}")
    print(f"  A_s^framework / A_s_Planck = {ratio:.6e}")
    print(f"  delta_OOM (log10)          = {delta_OOM:+.4f}")

    # Verdict from pre-registered thresholds
    abs_delta = abs(delta_OOM)                                      # (local)
    if abs_delta < DELTA_F2:
        verdict = 'PASS-F2'
    elif abs_delta < DELTA_F15:
        verdict = 'INFO-F15'
    else:
        verdict = 'FAIL-GT15'
    print(f"  Verdict: {verdict}  (|delta_OOM|={abs_delta:.4f} vs thresholds "
          f"[{DELTA_F2:.4f}, {DELTA_F15:.4f}])")

    return dict(
        label=label,
        scheme=scheme_tag, convention=convention_tag, L_max=L_max_tag,
        H_tilde=H_tilde,
        term_1=term_1, term_2=term_2, term_3=term_3, term_4=term_4, term_5=term_5,
        acc_a=acc_a, acc_b=acc_b, acc_c=acc_c, acc_d=acc_d, acc_e=acc_e,
        A_s=A_s, ratio=ratio, delta_OOM=delta_OOM,
        abs_delta=abs_delta, verdict=verdict,
    )


print("\n[SEC 4] Per-branch UNIFIED-AS-79 computation")

res_A = unified_as_79(H_tilde_A, 'A (TD-framework / zeta / N_pivot=55 / L_max=3)',
                      scheme_A, 'UNIFIED-AS-79-branch-TD', L_max_A)
res_B = unified_as_79(H_tilde_B, 'B (LI / SDW / epoch-resolved-a_2 / L_max=5)',
                      scheme_B, 'UNIFIED-AS-79-branch-LI', L_max_B)

# Diagnostic references (NOT verdict branches)
print("\n[SEC 4.1] Diagnostic references (NOT verdict branches)")
res_TD_pathB = unified_as_79(H_tilde_TD_pathB_ref,
                             'REF: TD-Path-B (fold-epoch diagnostic, zeta)',
                             'zeta', 'REFERENCE-fold-epoch', 3)
res_LI_obsinv = unified_as_79(H_tilde_LI_obsinv_ref,
                              'REF: LI obs-inverse (tautological)',
                              'SDW', 'REFERENCE-tautology', 5)

# ============================================================
# SECTION 5: CROSS-CHECKS
# ============================================================
print("\n[SEC 5] Cross-checks (machine-precision identities)")

# Cross-check 1: d(ln A_s)/d(ln c_sub) = -1 identity
# Substitution chain:
#   A_s = C * c_sub^{-1}   where C = (H^2/(8 pi^2)) * (1/eps) * F_amp * f_conv
#   ln A_s = ln C - ln c_sub
#   d(ln A_s)/d(ln c_sub) = -1  (exact, analytic)
c_sub_pert = c_sub * 1.01                                          # (local) 1% perturbation
A_s_base_A = res_A['A_s']                                          # (local)
A_s_pert_A = (H_tilde_A**2 / (8*np.pi**2)) * (1.0/eps_H) * \
             F_amp_slot_adjusted / c_sub_pert * f_conv             # (local)
d_ln_As = np.log(A_s_pert_A / A_s_base_A)                          # (local)
d_ln_csub = np.log(c_sub_pert / c_sub)                             # (local)
logdiff_csub = d_ln_As / d_ln_csub                                 # (local)
CC1_match = abs(logdiff_csub + 1.0) < 1e-10                        # (local)
print(f"  CC1: d(ln A_s)/d(ln c_sub) = {logdiff_csub:.10f}  (expected: -1.0)  "
      f"match={CC1_match}")

# Cross-check 2: d(ln A_s)/d(ln F_amp) = +1 identity
F_amp_pert = F_amp_slot_adjusted * 1.01                            # (local)
A_s_pert_F = (H_tilde_A**2 / (8*np.pi**2)) * (1.0/eps_H) * \
             F_amp_pert / c_sub * f_conv                           # (local)
d_ln_As_F = np.log(A_s_pert_F / A_s_base_A)                        # (local)
d_ln_F = np.log(F_amp_pert / F_amp_slot_adjusted)                  # (local)
logdiff_Famp = d_ln_As_F / d_ln_F                                  # (local)
CC2_match = abs(logdiff_Famp - 1.0) < 1e-10                        # (local)
print(f"  CC2: d(ln A_s)/d(ln F_amp) = {logdiff_Famp:.10f}  (expected: +1.0)  "
      f"match={CC2_match}")

# Cross-check 3: d(ln A_s)/d(ln H_tilde) = +2 identity
H_pert = H_tilde_A * 1.01                                          # (local)
A_s_pert_H = (H_pert**2 / (8*np.pi**2)) * (1.0/eps_H) * \
             F_amp_slot_adjusted / c_sub * f_conv                  # (local)
d_ln_As_H = np.log(A_s_pert_H / A_s_base_A)                        # (local)
d_ln_H = np.log(H_pert / H_tilde_A)                                # (local)
logdiff_H = d_ln_As_H / d_ln_H                                     # (local)
CC3_match = abs(logdiff_H - 2.0) < 1e-10                           # (local)
print(f"  CC3: d(ln A_s)/d(ln H_tilde) = {logdiff_H:.10f}  (expected: +2.0)  "
      f"match={CC3_match}")

# Cross-check 4: d(ln A_s)/d(ln eps_H) = -1 identity
eps_pert = eps_H * 1.01                                            # (local)
A_s_pert_e = (H_tilde_A**2 / (8*np.pi**2)) * (1.0/eps_pert) * \
             F_amp_slot_adjusted / c_sub * f_conv                  # (local)
d_ln_As_e = np.log(A_s_pert_e / A_s_base_A)                        # (local)
d_ln_e = np.log(eps_pert / eps_H)                                  # (local)
logdiff_e = d_ln_As_e / d_ln_e                                     # (local)
CC4_match = abs(logdiff_e + 1.0) < 1e-10                           # (local)
print(f"  CC4: d(ln A_s)/d(ln eps_H) = {logdiff_e:.10f}  (expected: -1.0)  "
      f"match={CC4_match}")

# Cross-check 5: Reproduce S80 W1-2 A_s values (prior session concordance)
S80_A_s_TD_ref = 3.30e-9                                           # (local) S80 memory note
S80_delta_OOM_TD_ref = 0.196                                       # (local) S80 memory note
S80_rel_err = abs(res_A['A_s'] - S80_A_s_TD_ref) / S80_A_s_TD_ref  # (local)
CC5_match = S80_rel_err < 0.02                                     # (local)  1% re-agreement
print(f"  CC5: S80 branch-TD A_s={S80_A_s_TD_ref:.2e} vs S82={res_A['A_s']:.4e}  "
      f"rel_err={S80_rel_err:.4%}  match<2%={CC5_match}")

cross_checks_ok = all([CC1_match, CC2_match, CC3_match, CC4_match, CC5_match])  # (local)
print(f"  ALL cross-checks PASS: {cross_checks_ok}")

# ============================================================
# SECTION 6: BRANCH-CONDITIONAL VERDICT LINES
# ============================================================
print("\n[SEC 6] Branch-conditional verdicts")

# Build closure SHA for each branch
def build_closure_sha(res, label_tag):
    """Build ordered SHA over inputs + factor values for a branch."""
    closure_map = {
        'label': label_tag,
        'H_tilde': f"{res['H_tilde']:.10e}",
        'eps_H': f"{eps_H:.10e}",
        'F_amp_canonical': f"{F_amp_canonical:.10e}",
        'k_a2': f"{k_a2:.10e}",
        'F_amp_slot_adjusted': f"{F_amp_slot_adjusted:.10e}",
        'c_sub': f"{c_sub:.10e}",
        'f_conv': f"{f_conv:.10e}",
        'A_s_Planck': f"{A_s_Planck:.10e}",
        'A_s_framework': f"{res['A_s']:.10e}",
        'delta_OOM': f"{res['delta_OOM']:.10f}",
        'verdict': res['verdict'],
        'scheme': res['scheme'],
        'convention': res['convention'],
        'L_max': res['L_max'],
        'thresholds': {
            'DELTA_F2': f"{DELTA_F2:.10e}",
            'DELTA_F15': f"{DELTA_F15:.10e}",
        },
        'inputs': {k: v for k, v in sorted(INPUT_SHAS.items())},
    }
    closure_str = json.dumps(closure_map, sort_keys=True, default=str)  # (local)
    return hashlib.sha256(closure_str.encode('utf-8')).hexdigest()


closure_sha_A = build_closure_sha(res_A, 'A')                      # (local)
closure_sha_B = build_closure_sha(res_B, 'B')                      # (local)

# 4-tuples
four_tuple_A = (                                                    # (local)
    f"(value={res_A['A_s']:.4e}, scheme={res_A['scheme']}, "
    f"convention={res_A['convention']}, L_max={res_A['L_max']})"
)
four_tuple_B = (                                                    # (local)
    f"(value={res_B['A_s']:.4e}, scheme={res_B['scheme']}, "
    f"convention={res_B['convention']}, L_max={res_B['L_max']})"
)

print(f"  Branch A: 4-tuple = {four_tuple_A}")
print(f"            closure_sha = {closure_sha_A}")
print(f"            verdict = {res_A['verdict']}")
print(f"  Branch B: 4-tuple = {four_tuple_B}")
print(f"            closure_sha = {closure_sha_B}")
print(f"            verdict = {res_B['verdict']}")

# ============================================================
# SECTION 7: Save .npz (data artifacts)
# ============================================================
print("\n[SEC 7] Saving .npz")
out_npz = os.path.join(HERE, 's82_w1_2_unified_as_79_full.npz')    # (local)
np.savez(
    out_npz,
    # Branch inputs
    H_tilde_A=H_tilde_A,
    H_tilde_B=H_tilde_B,
    H_tilde_TD_pathB_ref=H_tilde_TD_pathB_ref,
    H_tilde_LI_obsinv_ref=H_tilde_LI_obsinv_ref,
    # Common factors
    eps_H=eps_H,
    c_sub=c_sub,
    f_conv=f_conv,
    k_a2=k_a2,
    F_amp_canonical=F_amp_canonical,
    F_amp_slot_adjusted=F_amp_slot_adjusted,
    A_s_Planck=A_s_Planck,
    # Thresholds
    DELTA_F2=DELTA_F2,
    DELTA_F15=DELTA_F15,
    # Branch A results
    A_s_A=res_A['A_s'],
    delta_OOM_A=res_A['delta_OOM'],
    verdict_A=res_A['verdict'],
    closure_sha_A=closure_sha_A,
    four_tuple_A=four_tuple_A,
    factors_A=np.array([res_A['term_1'], res_A['term_2'], res_A['term_3'],
                        res_A['term_4'], res_A['term_5']]),
    cumulative_A=np.array([res_A['acc_a'], res_A['acc_b'], res_A['acc_c'],
                           res_A['acc_d'], res_A['acc_e']]),
    # Branch B results
    A_s_B=res_B['A_s'],
    delta_OOM_B=res_B['delta_OOM'],
    verdict_B=res_B['verdict'],
    closure_sha_B=closure_sha_B,
    four_tuple_B=four_tuple_B,
    factors_B=np.array([res_B['term_1'], res_B['term_2'], res_B['term_3'],
                        res_B['term_4'], res_B['term_5']]),
    cumulative_B=np.array([res_B['acc_a'], res_B['acc_b'], res_B['acc_c'],
                           res_B['acc_d'], res_B['acc_e']]),
    # Diagnostic references
    A_s_TD_pathB_ref=res_TD_pathB['A_s'],
    A_s_LI_obsinv_ref=res_LI_obsinv['A_s'],
    # Cross-checks
    CC1_logdiff_csub=logdiff_csub,
    CC2_logdiff_Famp=logdiff_Famp,
    CC3_logdiff_H=logdiff_H,
    CC4_logdiff_eps=logdiff_e,
    CC5_rel_err_vs_s80=S80_rel_err,
    cross_checks_ok=cross_checks_ok,
    # Inputs
    input_shas=np.array([f"{k}={v}" for k, v in sorted(INPUT_SHAS.items())]),
)
print(f"  Saved: {out_npz}")

# ============================================================
# SECTION 8: Plot — factor contribution bar chart + Planck band overlay
# ============================================================
print("\n[SEC 8] Plotting")
out_png = os.path.join(HERE, 's82_w1_2_unified_as_79_full.png')    # (local)
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Panel (a): cumulative product by factor (log scale)
ax = axes[0]
labels_step = ['H^2/(8pi^2)', '* 1/eps_H', '* F_amp', '* 1/c_sub', '* f_conv']
cum_A = [res_A['acc_a'], res_A['acc_b'], res_A['acc_c'], res_A['acc_d'], res_A['acc_e']]
cum_B = [res_B['acc_a'], res_B['acc_b'], res_B['acc_c'], res_B['acc_d'], res_B['acc_e']]
x = np.arange(len(labels_step))                                    # (local)
ax.semilogy(x, np.abs(cum_A), 'o-', color='C3', linewidth=2, markersize=8,
            label=f'Branch A (TD, zeta): verdict={res_A["verdict"]}')
ax.semilogy(x, np.abs(cum_B), 's-', color='C0', linewidth=2, markersize=8,
            label=f'Branch B (LI, SDW): verdict={res_B["verdict"]}')
ax.axhline(A_s_Planck, color='k', linestyle='--', alpha=0.7,
           label=f'Planck A_s = {A_s_Planck:.2e}')
ax.axhspan(A_s_Planck / 2.0, A_s_Planck * 2.0, color='green', alpha=0.15,
           label='PASS-F2 band')
ax.axhspan(A_s_Planck / 15.0, A_s_Planck * 15.0, color='gold', alpha=0.10,
           label='INFO-F15 band')
ax.set_xticks(x)
ax.set_xticklabels(labels_step, rotation=30, ha='right')
ax.set_ylabel('Cumulative product')
ax.set_title('(a) UNIFIED-AS-79: factor-by-factor accumulation\n(log scale)')
ax.legend(loc='best', fontsize=8)
ax.grid(True, alpha=0.3)

# Panel (b): A_s bars by branch with Planck band
ax = axes[1]
branch_labels = [
    'A: TD-fw\n(zeta,N=55)',
    'B: LI\n(SDW)',
    'REF: TD-Path-B\n(fold)',
    'REF: LI-obs-inv\n(tautology)',
]
A_s_values = [res_A['A_s'], res_B['A_s'], res_TD_pathB['A_s'], res_LI_obsinv['A_s']]
delta_OOMs = [res_A['delta_OOM'], res_B['delta_OOM'],
              res_TD_pathB['delta_OOM'], res_LI_obsinv['delta_OOM']]
verdicts = [res_A['verdict'], res_B['verdict'],
            res_TD_pathB['verdict'], res_LI_obsinv['verdict']]
bar_colors = ['C3', 'C0', 'C1', 'gray']
bars = ax.bar(branch_labels, A_s_values, color=bar_colors, alpha=0.75)
ax.set_yscale('log')
ax.axhline(A_s_Planck, color='k', linestyle='--', alpha=0.7,
           label=f'Planck A_s = {A_s_Planck:.2e}')
ax.axhspan(A_s_Planck / 2.0, A_s_Planck * 2.0, color='green', alpha=0.15,
           label='PASS-F2')
ax.axhspan(A_s_Planck / 15.0, A_s_Planck * 15.0, color='gold', alpha=0.10,
           label='INFO-F15')
for bar, val, d, v in zip(bars, A_s_values, delta_OOMs, verdicts):
    h = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2.0, max(h * 2.0, 1e-30),
            f'{val:.2e}\n' + r'$\Delta$=' + f'{d:+.2f}\n{v}',
            ha='center', va='bottom', fontsize=8)
ax.set_ylabel('A_s^framework')
ax.set_title('(b) A_s per branch — dual-branch (W1-1 DIVERGED)')
ax.legend(loc='lower right', fontsize=8)
ax.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig(out_png, dpi=140)
plt.close(fig)
print(f"  Saved: {out_png}")

# ============================================================
# SECTION 9: Append verdict lines to s82_gate_verdicts.txt
# ============================================================
print("\n[SEC 9] Append verdict lines to s82_gate_verdicts.txt")
verdicts_path = os.path.join(HERE, 's82_gate_verdicts.txt')        # (local)

verdict_line_A = (                                                 # (local)
    f"S82-UNIFIED-AS-79-FULL-A: {res_A['verdict']} -- "
    f"value={res_A['A_s']:.4e} "
    f"scheme={res_A['scheme']} "
    f"convention={res_A['convention']} "
    f"L_max={res_A['L_max']} "
    f"sha256={closure_sha_A}\n"
)
verdict_line_B = (                                                 # (local)
    f"S82-UNIFIED-AS-79-FULL-B: {res_B['verdict']} -- "
    f"value={res_B['A_s']:.4e} "
    f"scheme={res_B['scheme']} "
    f"convention={res_B['convention']} "
    f"L_max={res_B['L_max']} "
    f"sha256={closure_sha_B}\n"
)
with open(verdicts_path, 'a', encoding='utf-8') as _f:
    _f.write(verdict_line_A)
    _f.write(verdict_line_B)
print(f"  Appended:\n    {verdict_line_A.strip()}\n    {verdict_line_B.strip()}")

# ============================================================
# FINAL: 4-tuple line (final non-verdict line per protocol)
# ============================================================
print("\n" + "=" * 70)
print(f"S82-UNIFIED-AS-79-FULL-A {res_A['verdict']} (delta_OOM={res_A['delta_OOM']:+.4f})")
print(f"S82-UNIFIED-AS-79-FULL-B {res_B['verdict']} (delta_OOM={res_B['delta_OOM']:+.4f})")
print(f"FINAL 4-TUPLE (Branch A): {four_tuple_A}")
print(f"FINAL 4-TUPLE (Branch B): {four_tuple_B}")
print("=" * 70)
