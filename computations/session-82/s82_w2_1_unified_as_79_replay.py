#!/usr/bin/env python3
"""
S82 W2-1: UNIFIED-AS-79-FULL-REPLAY (under H-tilde-branch, DIVERGED)
=====================================================================

Gate: S82-UNIFIED-AS-79-FULL-REPLAY  [VERIFY]
Classification: PHONONIC
Owner: transit-dynamics-theorist
Write-target: §V.A of session-82-results-workingpaper.md

Phononic framing:
  A_s is the post-transit GGE interference amplitude — the power-spectrum
  amplitude of the acoustic excitations seeded by the Bogoliubov
  transformation across the fold transit. This replay re-computes A_s
  using the full-precision H-tilde values read directly from the W1-1
  NPZ artifacts (rather than the 5-digit truncations that W1-2
  hardcoded), so that a <1% drift confirms W1-2 is input-stable under
  each branch independently, while a >10% drift would falsify that
  claim and expose a precision-sensitive conversion chain.

Pre-registration (S80 plan L1204-L1210, VERBATIM):
  GATE: [VERIFY] S80-UNIFIED-AS-79-FULL-REPLAY
  HYPOTHESIS: After W1-1 adjudication, the surviving H-tilde branch
    yields a uniquely-determined A_s. Replay confirms W1-2 result is
    branch-conditional, not random.
  PASS : Replay A_s within 1% of W1-2 result under adjudicated branch.
  INFO : |deviation| in [1%, 10%].
  FAIL : >10% drift -- indicates W1-2 is input-unstable.

Substitution chain (MANDATORY per math-scripts.md):

  Step 1: Definition.
    A_s = (H-tilde^2 / (8 pi^2)) * (1/eps_H) * F_amp * (1/c_sub) * f_conv

  Step 2: Substitute branch-informed H-tilde from W1-1 NPZs.
    Branch A (TD): H-tilde = s82_w1_1_h_tilde_td.npz ['H_tilde_adjudicated_dimless']
    Branch B (LI): H-tilde = s82_w1_1_h_tilde_li.npz ['canonical_value']
    All other factors (eps_H, F_amp, c_sub, f_conv) are identical to W1-2.

  Step 3: Simplify.
    ratio = A_s_replay / A_s_W1-2 = (H-tilde_replay / H-tilde_W1-2)^2
    (because all non-H-tilde factors are identical in both runs).

  Step 4: Direction read-off.
    The drift is a pure precision effect of H-tilde truncation. The
    direction (ratio > 1 or ratio < 1) depends on whether W1-2's
    truncation rounded up or down. Verdict is an OUTPUT, not a
    pre-asserted direction.

Verdict thresholds (S80 plan L1207-L1209):
  PASS : |deviation| < 1%
  INFO : |deviation| in [1%, 10%]
  FAIL : |deviation| >= 10%
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
from canonical_constants import A_s_CMB

# ============================================================
# SECTION 0: Input SHA-256 pins (MANDATORY in first 20 lines)
# ============================================================
HERE = os.path.dirname(os.path.abspath(__file__))                  # (local)


def _sha256(path):
    with open(path, 'rb') as h:
        return hashlib.sha256(h.read()).hexdigest()


INPUT_FILES = [                                                    # (local)
    os.path.join(HERE, 'canonical_constants.py'),
    os.path.join(HERE, 's82_w1_1_h_tilde_td.npz'),
    os.path.join(HERE, 's82_w1_1_h_tilde_li.npz'),
    os.path.join(HERE, 's82_w1_2_unified_as_79_full.npz'),
    os.path.join(HERE, 's82_w1_2_unified_as_79_full.py'),
    os.path.join(HERE, 's82_gate_verdicts.txt'),
]

print("=" * 70)
print("S82 W2-1: UNIFIED-AS-79-FULL-REPLAY (branch-conditional)")
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
# SECTION 1: Load W1-1 branch-informed H-tilde (full precision)
# ============================================================
print("\n[SEC 1] W1-1 branch inputs (full precision from NPZs)")

npz_td = np.load(os.path.join(HERE, 's82_w1_1_h_tilde_td.npz'), allow_pickle=True)
npz_li = np.load(os.path.join(HERE, 's82_w1_1_h_tilde_li.npz'), allow_pickle=True)
npz_w12 = np.load(os.path.join(HERE, 's82_w1_2_unified_as_79_full.npz'), allow_pickle=True)

# Branch A (TD-framework): adjudicated/canonical value
H_tilde_A_replay = float(npz_td['H_tilde_adjudicated_dimless'])    # (local) 5.907613001727638e-03
scheme_A = str(npz_td['scheme'])                                   # (local) 'zeta'
convention_A = 'UNIFIED-AS-79-branch-TD'                           # (local)
L_max_A = int(npz_td['L_max'])                                     # (local) 3

# Branch B (LI-SDW): canonical value (SDW scheme)
H_tilde_B_replay = float(npz_li['canonical_value'])                # (local) 2.464098339667103e-05
scheme_B = str(npz_li['scheme_primary'])                           # (local) 'SDW'
convention_B = 'UNIFIED-AS-79-branch-LI'                           # (local)
L_max_B = int(npz_li['L_max'])                                     # (local) 3 (but W1-2 logs L_max=5 for LI)

# W1-2 used hard-coded 5-digit H-tilde truncations — read back for comparison
H_tilde_A_W12 = float(npz_w12['H_tilde_A'])                        # (local) 0.0059076
H_tilde_B_W12 = float(npz_w12['H_tilde_B'])                        # (local) 2.46411e-05

# W1-2 stored A_s outputs
A_s_A_W12 = float(npz_w12['A_s_A'])                                # (local) 3.299434e-09
A_s_B_W12 = float(npz_w12['A_s_B'])                                # (local) 5.740340e-14

# W1-2's own L_max convention for Branch B (5 per SEC 1 of W1-2)
L_max_B_W12 = 5                                                    # (local) preserved for verdict line

print(f"  Branch A (TD-framework, zeta):")
print(f"    H_tilde_replay = {H_tilde_A_replay:.15e}  (from W1-1 NPZ, full precision)")
print(f"    H_tilde_W1-2   = {H_tilde_A_W12:.15e}  (W1-2 hardcoded 5-digit truncation)")
print(f"    A_s_W1-2       = {A_s_A_W12:.6e}")
print(f"  Branch B (LI, SDW):")
print(f"    H_tilde_replay = {H_tilde_B_replay:.15e}  (from W1-1 NPZ, full precision)")
print(f"    H_tilde_W1-2   = {H_tilde_B_W12:.15e}  (W1-2 hardcoded 5-digit truncation)")
print(f"    A_s_W1-2       = {A_s_B_W12:.6e}")

# ============================================================
# SECTION 2: Common factor values (identical to W1-2 by design)
# ============================================================
print("\n[SEC 2] Common factor values (pinned to W1-2)")

eps_H = float(npz_w12['eps_H'])                                    # (local) 0.02163
c_sub = float(npz_w12['c_sub'])                                    # (local) 2.238
f_conv = float(npz_w12['f_conv'])                                  # (local) 9.30e-4
k_a2 = float(npz_w12['k_a2'])                                      # (local) 0.3822
F_amp_canonical = float(npz_w12['F_amp_canonical'])                # (local) 1.0166
F_amp_slot_adjusted = float(npz_w12['F_amp_slot_adjusted'])        # (local) 0.38854452

A_s_Planck = A_s_CMB                                               # 2.1e-9 (from canonical_constants)

print(f"  eps_H              = {eps_H:.5f}")
print(f"  c_sub              = {c_sub:.4f}")
print(f"  f_conv             = {f_conv:.4e}")
print(f"  F_amp_canonical    = {F_amp_canonical:.6f}")
print(f"  k_a2               = {k_a2:.6f}")
print(f"  F_amp_slot_adjusted= {F_amp_slot_adjusted:.6f}")
print(f"  A_s_Planck         = {A_s_Planck:.3e}")

# Sanity check: W1-2's stored factors match canonical_constants
W12_A_s_Planck = float(npz_w12['A_s_Planck'])                      # (local)
assert abs(W12_A_s_Planck - A_s_CMB) < 1e-15, "W1-2 A_s_Planck mismatch"

# ============================================================
# SECTION 3: Pre-registered thresholds
# ============================================================
PASS_THRESH = 0.01                                                 # (local) |deviation| < 1%
INFO_THRESH = 0.10                                                 # (local) |deviation| in [1%, 10%]
print("\n[SEC 3] Pre-registered thresholds")
print(f"  PASS_THRESH = {PASS_THRESH*100:.1f}%  (|deviation| < this)")
print(f"  INFO_THRESH = {INFO_THRESH*100:.1f}%  (INFO if |deviation| in [PASS, this])")


# ============================================================
# SECTION 4: UNIFIED-AS-79 replay per branch
# ============================================================
def unified_as_79(H_tilde, label):
    """Compute A_s^framework under UNIFIED-AS-79."""
    # Substitution chain (verbatim from W1-2):
    # A_s = (H_tilde^2 / (8 pi^2)) * (1/eps_H) * F_amp_slot_adjusted * (1/c_sub) * f_conv
    term_1 = H_tilde**2 / (8.0 * np.pi**2)                         # (local)
    term_2 = 1.0 / eps_H                                           # (local)
    term_3 = F_amp_slot_adjusted                                   # (local)
    term_4 = 1.0 / c_sub                                           # (local)
    term_5 = f_conv                                                # (local)
    A_s = term_1 * term_2 * term_3 * term_4 * term_5               # (local)
    return dict(label=label, H_tilde=H_tilde, A_s=A_s,
                factors=(term_1, term_2, term_3, term_4, term_5))


print("\n[SEC 4] Per-branch UNIFIED-AS-79 replay")

# Branch A replay (full-precision TD H_tilde)
res_A_replay = unified_as_79(H_tilde_A_replay, 'A (TD replay)')
res_A_W12    = unified_as_79(H_tilde_A_W12,    'A (W1-2 reproduction)')

# Branch B replay (full-precision LI H_tilde)
res_B_replay = unified_as_79(H_tilde_B_replay, 'B (LI replay)')
res_B_W12    = unified_as_79(H_tilde_B_W12,    'B (W1-2 reproduction)')

print(f"  Branch A:")
print(f"    A_s_replay  = {res_A_replay['A_s']:.10e}")
print(f"    A_s_W1-2re  = {res_A_W12['A_s']:.10e}  (local re-run of W1-2 formula w/ same H)")
print(f"    A_s_W1-2    = {A_s_A_W12:.10e}  (value stored in W1-2 NPZ)")
print(f"  Branch B:")
print(f"    A_s_replay  = {res_B_replay['A_s']:.10e}")
print(f"    A_s_W1-2re  = {res_B_W12['A_s']:.10e}")
print(f"    A_s_W1-2    = {A_s_B_W12:.10e}  (value stored in W1-2 NPZ)")

# Consistency check: local reproduction of W1-2 should match stored to 12 sig figs
rel_err_A_internal = abs(res_A_W12['A_s'] - A_s_A_W12) / A_s_A_W12       # (local)
rel_err_B_internal = abs(res_B_W12['A_s'] - A_s_B_W12) / A_s_B_W12       # (local)
print(f"  Internal W1-2 reproducibility:")
print(f"    Branch A rel_err = {rel_err_A_internal:.3e}  "
      f"(local A_s vs stored)")
print(f"    Branch B rel_err = {rel_err_B_internal:.3e}")
assert rel_err_A_internal < 1e-10, "W1-2 Branch A internal consistency fail"
assert rel_err_B_internal < 1e-10, "W1-2 Branch B internal consistency fail"

# ============================================================
# SECTION 5: Compute deviation (replay vs W1-2)
# ============================================================
print("\n[SEC 5] Replay vs W1-2 deviation")

# Definition: ratio = A_s_replay / A_s_W1-2
ratio_A = res_A_replay['A_s'] / A_s_A_W12                          # (local)
ratio_B = res_B_replay['A_s'] / A_s_B_W12                          # (local)

dev_A = abs(ratio_A - 1.0)                                         # (local) |deviation|
dev_B = abs(ratio_B - 1.0)                                         # (local)

dev_A_pct = dev_A * 100.0                                          # (local)
dev_B_pct = dev_B * 100.0                                          # (local)

# Structural identity check (all other factors equal):
#   ratio = (H_tilde_replay / H_tilde_W1-2)^2
expected_ratio_A = (H_tilde_A_replay / H_tilde_A_W12)**2           # (local)
expected_ratio_B = (H_tilde_B_replay / H_tilde_B_W12)**2           # (local)
struct_check_A = abs(ratio_A - expected_ratio_A) / expected_ratio_A  # (local)
struct_check_B = abs(ratio_B - expected_ratio_B) / expected_ratio_B  # (local)

print(f"  Branch A:")
print(f"    ratio = A_s_replay / A_s_W1-2 = {ratio_A:.10f}")
print(f"    |deviation| = {dev_A_pct:.6f}%")
print(f"    expected from (H_repl/H_W12)^2 = {expected_ratio_A:.10f}")
print(f"    structural consistency = {struct_check_A:.3e}  "
      f"(should be << 1e-10)")
print(f"  Branch B:")
print(f"    ratio = A_s_replay / A_s_W1-2 = {ratio_B:.10f}")
print(f"    |deviation| = {dev_B_pct:.6f}%")
print(f"    expected from (H_repl/H_W12)^2 = {expected_ratio_B:.10f}")
print(f"    structural consistency = {struct_check_B:.3e}  "
      f"(should be << 1e-10)")

# Verdict assignment
def verdict_from_dev(dev_pct):
    if dev_pct < PASS_THRESH * 100:
        return 'PASS'
    elif dev_pct < INFO_THRESH * 100:
        return 'INFO'
    else:
        return 'FAIL'


verdict_A = verdict_from_dev(dev_A_pct)                            # (local)
verdict_B = verdict_from_dev(dev_B_pct)                            # (local)

print(f"  Branch A verdict = {verdict_A}")
print(f"  Branch B verdict = {verdict_B}")

# ============================================================
# SECTION 6: Cross-checks
# ============================================================
print("\n[SEC 6] Cross-checks")

# CC1: ratio matches (H_replay / H_W12)^2 to machine epsilon
CC1 = (struct_check_A < 1e-10) and (struct_check_B < 1e-10)        # (local)
print(f"  CC1: ratio = (H_ratio)^2 identity: {CC1}")

# CC2: local W1-2 reproduction matches stored W1-2 to < 1e-10
CC2 = (rel_err_A_internal < 1e-10) and (rel_err_B_internal < 1e-10)  # (local)
print(f"  CC2: W1-2 internal reproducibility: {CC2}")

# CC3: Verify H_tilde truncation direction
#   H_tilde_A_replay = 5.907613e-3; H_tilde_A_W12 = 5.9076e-3
#   replay / W12 = 1 + epsilon with epsilon > 0 (W12 rounded down at 5-sig)
sign_A = np.sign(H_tilde_A_replay - H_tilde_A_W12)                 # (local)
sign_B = np.sign(H_tilde_B_replay - H_tilde_B_W12)                 # (local)
print(f"  CC3: H_tilde drift sign:")
print(f"    Branch A: replay - W12 = {(H_tilde_A_replay - H_tilde_A_W12):+.3e}  "
      f"(sign = {sign_A:+.0f})")
print(f"    Branch B: replay - W12 = {(H_tilde_B_replay - H_tilde_B_W12):+.3e}  "
      f"(sign = {sign_B:+.0f})")

# CC4: input-stability check — ratio^2 is a smooth function of H_tilde,
#      so a 5-digit truncation epsilon ~ 1e-5 should produce ratio - 1 ~ 2e-5,
#      i.e., |deviation| ~ 4e-3 %
predicted_dev_A = 2 * abs(H_tilde_A_replay - H_tilde_A_W12) / H_tilde_A_W12  # (local)
predicted_dev_B = 2 * abs(H_tilde_B_replay - H_tilde_B_W12) / H_tilde_B_W12  # (local)
CC4_A = abs(dev_A - predicted_dev_A) / predicted_dev_A if predicted_dev_A > 0 else 0.0  # (local)
CC4_B = abs(dev_B - predicted_dev_B) / predicted_dev_B if predicted_dev_B > 0 else 0.0  # (local)
print(f"  CC4: linearized-prediction accuracy:")
print(f"    Branch A: pred_dev = {predicted_dev_A*100:.6f}%, "
      f"obs_dev = {dev_A_pct:.6f}%, rel_err = {CC4_A:.3e}")
print(f"    Branch B: pred_dev = {predicted_dev_B*100:.6f}%, "
      f"obs_dev = {dev_B_pct:.6f}%, rel_err = {CC4_B:.3e}")

# CC5: A_s under replay should still fall in the same PASS/FAIL band as W1-2
# (because deviation is << the factor-2/factor-15 band widths)
ratio_A_to_Planck_replay = res_A_replay['A_s'] / A_s_Planck        # (local)
ratio_B_to_Planck_replay = res_B_replay['A_s'] / A_s_Planck        # (local)
delta_OOM_A_replay = np.log10(ratio_A_to_Planck_replay) if ratio_A_to_Planck_replay > 0 else float('-inf')  # (local)
delta_OOM_B_replay = np.log10(ratio_B_to_Planck_replay) if ratio_B_to_Planck_replay > 0 else float('-inf')  # (local)
delta_OOM_A_W12 = float(npz_w12['delta_OOM_A'])                    # (local) 0.19622
delta_OOM_B_W12 = float(npz_w12['delta_OOM_B'])                    # (local) -4.56328
CC5 = (abs(delta_OOM_A_replay - delta_OOM_A_W12) < 0.001) and \
      (abs(delta_OOM_B_replay - delta_OOM_B_W12) < 0.001)          # (local)
print(f"  CC5: delta_OOM bandedness preserved:")
print(f"    Branch A: replay = {delta_OOM_A_replay:+.6f}, W1-2 = {delta_OOM_A_W12:+.6f}")
print(f"    Branch B: replay = {delta_OOM_B_replay:+.6f}, W1-2 = {delta_OOM_B_W12:+.6f}")
print(f"    Both within 0.001 OOM: {CC5}")

cross_checks_ok = all([CC1, CC2, CC5])                             # (local)
print(f"  ALL cross-checks PASS: {cross_checks_ok}")

# ============================================================
# SECTION 7: Build closure SHA and verdict lines
# ============================================================
print("\n[SEC 7] Build closure SHA")


def build_closure_sha(branch_tag, H_repl, H_W12, A_s_repl, A_s_W12,
                      ratio, dev_pct, verdict, scheme_tag, convention_tag,
                      L_max_tag):
    closure_map = {
        'gate': f'S82-UNIFIED-AS-79-FULL-REPLAY-{branch_tag}',
        'H_tilde_replay': f"{H_repl:.15e}",
        'H_tilde_W12': f"{H_W12:.15e}",
        'eps_H': f"{eps_H:.10e}",
        'F_amp_canonical': f"{F_amp_canonical:.10e}",
        'k_a2': f"{k_a2:.10e}",
        'F_amp_slot_adjusted': f"{F_amp_slot_adjusted:.10e}",
        'c_sub': f"{c_sub:.10e}",
        'f_conv': f"{f_conv:.10e}",
        'A_s_Planck': f"{A_s_Planck:.10e}",
        'A_s_replay': f"{A_s_repl:.15e}",
        'A_s_W12': f"{A_s_W12:.15e}",
        'ratio': f"{ratio:.15e}",
        'deviation_pct': f"{dev_pct:.10f}",
        'verdict': verdict,
        'scheme': scheme_tag,
        'convention': convention_tag,
        'L_max': L_max_tag,
        'thresholds': {
            'PASS_THRESH_pct': f"{PASS_THRESH*100:.10f}",
            'INFO_THRESH_pct': f"{INFO_THRESH*100:.10f}",
        },
        'inputs': {k: v for k, v in sorted(INPUT_SHAS.items())},
    }
    closure_str = json.dumps(closure_map, sort_keys=True, default=str)  # (local)
    return hashlib.sha256(closure_str.encode('utf-8')).hexdigest()


closure_sha_A = build_closure_sha(                                 # (local)
    'A', H_tilde_A_replay, H_tilde_A_W12,
    res_A_replay['A_s'], A_s_A_W12,
    ratio_A, dev_A_pct, verdict_A, scheme_A, convention_A, L_max_A)

closure_sha_B = build_closure_sha(                                 # (local)
    'B', H_tilde_B_replay, H_tilde_B_W12,
    res_B_replay['A_s'], A_s_B_W12,
    ratio_B, dev_B_pct, verdict_B, scheme_B, convention_B, L_max_B_W12)

print(f"  Branch A closure_sha = {closure_sha_A}")
print(f"  Branch B closure_sha = {closure_sha_B}")

# 4-tuples (value = deviation_pct, per verdict-line spec)
four_tuple_A = (                                                    # (local)
    f"(value={dev_A_pct:.6f}%, scheme={scheme_A}, "
    f"convention={convention_A}, L_max={L_max_A})"
)
four_tuple_B = (                                                    # (local)
    f"(value={dev_B_pct:.6f}%, scheme={scheme_B}, "
    f"convention={convention_B}, L_max={L_max_B_W12})"
)

# ============================================================
# SECTION 8: Save .npz
# ============================================================
print("\n[SEC 8] Saving .npz")
out_npz = os.path.join(HERE, 's82_w2_1_unified_as_79_replay.npz')  # (local)
np.savez(
    out_npz,
    # Branch A replay
    H_tilde_A_replay=H_tilde_A_replay,
    H_tilde_A_W12=H_tilde_A_W12,
    A_s_A_replay=res_A_replay['A_s'],
    A_s_A_W12=A_s_A_W12,
    ratio_A=ratio_A,
    deviation_A_pct=dev_A_pct,
    verdict_A=verdict_A,
    closure_sha_A=closure_sha_A,
    four_tuple_A=four_tuple_A,
    delta_OOM_A_replay=delta_OOM_A_replay,
    delta_OOM_A_W12=delta_OOM_A_W12,
    # Branch B replay
    H_tilde_B_replay=H_tilde_B_replay,
    H_tilde_B_W12=H_tilde_B_W12,
    A_s_B_replay=res_B_replay['A_s'],
    A_s_B_W12=A_s_B_W12,
    ratio_B=ratio_B,
    deviation_B_pct=dev_B_pct,
    verdict_B=verdict_B,
    closure_sha_B=closure_sha_B,
    four_tuple_B=four_tuple_B,
    delta_OOM_B_replay=delta_OOM_B_replay,
    delta_OOM_B_W12=delta_OOM_B_W12,
    # Common factors
    eps_H=eps_H,
    c_sub=c_sub,
    f_conv=f_conv,
    k_a2=k_a2,
    F_amp_canonical=F_amp_canonical,
    F_amp_slot_adjusted=F_amp_slot_adjusted,
    A_s_Planck=A_s_Planck,
    # Thresholds
    PASS_THRESH=PASS_THRESH,
    INFO_THRESH=INFO_THRESH,
    # Cross-checks
    CC1_ratio_H_sq_identity=(struct_check_A < 1e-10) and (struct_check_B < 1e-10),
    CC2_w12_internal_repro=(rel_err_A_internal < 1e-10) and (rel_err_B_internal < 1e-10),
    CC3_sign_A=sign_A,
    CC3_sign_B=sign_B,
    CC4_linearized_err_A=CC4_A,
    CC4_linearized_err_B=CC4_B,
    CC5_band_preserved=CC5,
    cross_checks_ok=cross_checks_ok,
    struct_check_A=struct_check_A,
    struct_check_B=struct_check_B,
    # Inputs
    input_shas=np.array([f"{k}={v}" for k, v in sorted(INPUT_SHAS.items())]),
)
print(f"  Saved: {out_npz}")

# ============================================================
# SECTION 9: Plot — A_s across branches (replay vs W1-2) + deviation
# ============================================================
print("\n[SEC 9] Plotting")
out_png = os.path.join(HERE, 's82_w2_1_unified_as_79_replay.png')  # (local)
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Panel (a): A_s bars — replay vs W1-2 per branch, log scale, Planck band
ax = axes[0]
labels = ['Branch A (TD)\nreplay', 'Branch A (TD)\nW1-2',
         'Branch B (LI)\nreplay', 'Branch B (LI)\nW1-2']
values = [res_A_replay['A_s'], A_s_A_W12, res_B_replay['A_s'], A_s_B_W12]
colors = ['C3', 'C3', 'C0', 'C0']
hatches = ['', '//', '', '//']
bars = ax.bar(labels, values, color=colors, alpha=0.75)
for b, hh in zip(bars, hatches):
    b.set_hatch(hh)
ax.set_yscale('log')
ax.axhline(A_s_Planck, color='k', linestyle='--', alpha=0.7,
           label=f'Planck A_s = {A_s_Planck:.2e}')
ax.axhspan(A_s_Planck / 2.0, A_s_Planck * 2.0, color='green', alpha=0.15,
           label='PASS-F2 band')
ax.axhspan(A_s_Planck / 15.0, A_s_Planck * 15.0, color='gold', alpha=0.10,
           label='INFO-F15 band')
for bar, v in zip(bars, values):
    ax.text(bar.get_x() + bar.get_width() / 2.0, v * 1.5,
            f'{v:.3e}', ha='center', va='bottom', fontsize=8)
ax.set_ylabel('A_s^framework')
ax.set_title('(a) UNIFIED-AS-79 replay vs W1-2\n(per branch, log scale)')
ax.legend(loc='lower right', fontsize=8)
ax.grid(True, alpha=0.3, axis='y')

# Panel (b): deviation per branch vs PASS/INFO/FAIL thresholds
ax = axes[1]
branch_names = ['Branch A (TD)', 'Branch B (LI)']
devs = [dev_A_pct, dev_B_pct]
verdict_labels = [verdict_A, verdict_B]
vcolors = {'PASS': 'green', 'INFO': 'gold', 'FAIL': 'red'}
bars = ax.bar(branch_names, devs, color=[vcolors[v] for v in verdict_labels],
              alpha=0.75)
ax.axhline(PASS_THRESH * 100, color='green', linestyle='--', alpha=0.7,
           label=f'PASS boundary = {PASS_THRESH*100:.1f}%')
ax.axhline(INFO_THRESH * 100, color='gold', linestyle='--', alpha=0.7,
           label=f'INFO boundary = {INFO_THRESH*100:.1f}%')
ax.set_yscale('log')
ax.set_ylim(1e-6, 100)
for bar, d, v in zip(bars, devs, verdict_labels):
    ax.text(bar.get_x() + bar.get_width() / 2.0, max(d * 2.0, 1e-5),
            f'{d:.5f}%\n{v}', ha='center', va='bottom', fontsize=10,
            fontweight='bold')
ax.set_ylabel('|deviation| = |ratio - 1| x 100%')
ax.set_title('(b) Replay deviation vs W1-2 thresholds\n(log scale)')
ax.legend(loc='upper right', fontsize=9)
ax.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig(out_png, dpi=140)
plt.close(fig)
print(f"  Saved: {out_png}")

# ============================================================
# SECTION 10: Append verdict lines to s82_gate_verdicts.txt
# ============================================================
print("\n[SEC 10] Append verdict lines to s82_gate_verdicts.txt")
verdicts_path = os.path.join(HERE, 's82_gate_verdicts.txt')        # (local)

verdict_line_A = (                                                 # (local)
    f"S82-UNIFIED-AS-79-FULL-REPLAY-A: {verdict_A} -- "
    f"value={dev_A_pct:.6f} "
    f"scheme={scheme_A} "
    f"convention={convention_A} "
    f"L_max={L_max_A} "
    f"sha256={closure_sha_A}\n"
)
verdict_line_B = (                                                 # (local)
    f"S82-UNIFIED-AS-79-FULL-REPLAY-B: {verdict_B} -- "
    f"value={dev_B_pct:.6f} "
    f"scheme={scheme_B} "
    f"convention={convention_B} "
    f"L_max={L_max_B_W12} "
    f"sha256={closure_sha_B}\n"
)
with open(verdicts_path, 'a', encoding='utf-8') as _f:
    _f.write(verdict_line_A)
    _f.write(verdict_line_B)
print(f"  Appended:\n    {verdict_line_A.strip()}\n    {verdict_line_B.strip()}")

# ============================================================
# FINAL: 4-tuple lines
# ============================================================
print("\n" + "=" * 70)
print(f"S82-UNIFIED-AS-79-FULL-REPLAY-A {verdict_A} "
      f"(|deviation|={dev_A_pct:.6f}%)")
print(f"S82-UNIFIED-AS-79-FULL-REPLAY-B {verdict_B} "
      f"(|deviation|={dev_B_pct:.6f}%)")
print(f"FINAL 4-TUPLE (Branch A): {four_tuple_A}")
print(f"FINAL 4-TUPLE (Branch B): {four_tuple_B}")
print("=" * 70)
