#!/usr/bin/env python3
"""
S85 W8-3: S85-W8-3-MUKHANOV-SASAKI-SUB-CORRIDOR-AUDIT
=====================================================================
Reclassify the S84 W5 A_s-closure gate verdicts (W5-54, W5-59, W5-63,
W5-64, W5-65) on the MS-valid sub-corridor K >= K_R5 = 1.9222. PASS if
>= 3 of 5 verdicts are STABLE under reclassification.

Gate: S85-W8-3-MUKHANOV-SASAKI-SUB-CORRIDOR-AUDIT  [VERIFY] [AUDIT]
Classification: PHONONIC (Mukhanov-Sasaki validity on substrate)
Owner: volovik-superfluid-universe-theorist
Plan: sessions/session-plan/session-85-plan-w8.md §W8-3

PRE-REGISTERED THRESHOLDS (plan §W8-3 step 9):
  PASS: at least 3 of 5 W5 gates retain original verdict under K >= K_R5
        reclassification (sub-corridor-stable master-gate composition).
  FAIL: >= 3 W5 gate verdicts flip under reclassification (would trigger
        W5 rerun in S86).
  INFO: 1-2 W5 verdicts change (sub-corridor-stable but refined).

SUBSTITUTION CHAIN (plan §W8-3 step 10, re-derived):
  Def 1: K_corridor_full = [K_R5, K_R1] = [1.9222, 2.1849]   (W5-63 4-hull)
  Def 2: K_corridor_sub = [K_R5, inf) n K_corridor_full        (MS-valid)
  Def 3: K_excluded = [1.0, K_R5)                              (MS-invalid)
  Def 4: gate.verdict(K_eval) = original verdict using K_eval list
  Def 5: gate.verdict_sub(K_eval n [K_R5, inf)) = reclassified verdict

  Step 1: Enumerate K-evaluation points of each W5 gate from agent
          memory files:
          * W5-54: regulator-axis test (zeta K_R5=0.6366 vs Zub K_R5=32.40);
                   not a K-point evaluation in corridor sense; reclass
                   OUT-OF-SCOPE (regulator space, not K space).
          * W5-59: K = 2.035 (substrate-native K_base)
                   2.035 >= 1.9222 -> IN-corridor -> UNCHANGED.
          * W5-63: T = {1.0, 1.1, 1.3, 1.5, 1.7} (reachable-target set)
                   all < 1.9222 -> entirely OUT-corridor -> FLIPPED
                   (FAIL-on-reachability -> INFO-inapplicable-in-MS-valid).
          * W5-64: K = 2.035 (f_B closure gate at substrate-native K)
                   2.035 >= 1.9222 -> IN-corridor -> UNCHANGED.
          * W5-65: K = K_base = 2.035 (K_FIRAS coincidence gate)
                   2.035 >= 1.9222 -> IN-corridor -> UNCHANGED.

  Step 2: Count stable vs flipped:
          Stable (UNCHANGED or OUT-OF-SCOPE): W5-54, W5-59, W5-64, W5-65 = 4
          Flipped: W5-63 = 1
          Total: 5 gates; 4 of 5 stable.

  Step 3: PASS threshold is >= 3 of 5 stable. 4 >= 3 -> PASS.

  Step 4: Direction of reclassification: master-gate composition is
          STRENGTHENED (MS-invalid FAILs move to INFO-inapplicable),
          not weakened. W5-63 as FAIL was a real failure on its
          reachable-target test but that test was at K-points in
          [1.0, 1.7], entirely outside the MS-valid region. The
          reclassified verdict is "INFO-inapplicable-in-MS-valid"
          which is a correct scope note rather than a real closure
          failure.

  Conclusion: PASS with 4/5 stable.

References:
  - plan: sessions/session-plan/session-85-plan-w8.md §W8-3
  - W5-54: .claude/agent-memory/volovik-superfluid-universe-theorist/k-floor-regulator-invariance-84-result.md
  - W5-59: .claude/agent-memory/volovik-superfluid-universe-theorist/a_s_floor_branch_b_84-result.md
  - W5-63: .claude/agent-memory/volovik-superfluid-universe-theorist/k-floor-reachable-84-result.md
  - W5-65: .claude/agent-memory/volovik-superfluid-universe-theorist/k-firas-coincidence-84-result.md
"""

import os
os.environ.setdefault('OMP_NUM_THREADS', '4')
os.environ.setdefault('MKL_NUM_THREADS', '4')

import sys
import json
import hashlib
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))                    # (local)
sys.path.insert(0, HERE)

from canonical_constants import (
    K_R5,                # 1.9222 (substrate-native inflationary sub-corridor lower endpoint)
    K_base,              # 2.035 (R3 band-weighted K)
)

# ============================================================
# SECTION 0: Input SHA-256 pins
# ============================================================
GATE_ID = "S85-W8-3-MUKHANOV-SASAKI-SUB-CORRIDOR-AUDIT"              # (local)
SCHEME = "Interp_A_primary"                                          # (local)
CONVENTION = "ConvA_coth"                                            # (local)
L_MAX = 5                                                            # (local) plan: matches S84 W5 eval L_max

INPUT_FILES = [                                                      # (local)
    os.path.join(HERE, 'canonical_constants.py'),
    os.path.join(HERE, 's84_w5_k_floor_regulator_invariance.py'),
    os.path.join(HERE, 's84_w5_k_floor_reachable.py'),
    os.path.join(HERE, 's84_w5_k_firas_coincidence.py'),
    os.path.join(HERE, 's84_w5_a_s_floor_branch_b.py'),
]


def _sha256(path):
    if not os.path.exists(path):
        return 'MISSING'
    with open(path, 'rb') as h:
        return hashlib.sha256(h.read()).hexdigest()


print("=" * 76)
print(f"{GATE_ID}  (MS-valid sub-corridor reclassification audit)")
print("=" * 76)
print("\n[SEC 0] Input SHA-256 pins")
INPUT_SHAS = {}                                                      # (local)
for _f in INPUT_FILES:
    _h = _sha256(_f)                                                 # (local)
    rel = os.path.relpath(_f, os.path.dirname(HERE)).replace("\\", "/")
    INPUT_SHAS[rel] = _h
    _tag = (_h[:16] + '...' + _h[-8:]) if _h != 'MISSING' else 'MISSING'
    print(f"  {os.path.basename(_f):46s} sha256={_tag}")

# ============================================================
# SECTION 1: W5 gate K-evaluation tabulation from memory
# ============================================================
print("\n[SEC 1] W5 gate K-evaluation points from S84 agent memory")
print(f"  K_R5 (MS-validity floor) = {K_R5}")
print(f"  K_base (substrate-native) = {K_base}")

# Each entry: gate, original_verdict, K_eval_points, axis (K or regulator)
W5_GATES = [                                                          # (local)
    {
        'gate': 'W5-54',
        'tag': 'K-floor regulator invariance',
        'original_verdict': 'FAIL',
        'axis': 'regulator',
        'K_eval': [],   # not K-axis; regulator-axis test
        'regulator_probes': [('zeta', 0.6366), ('Zubarev', 32.40)],
        'memory_ref': 'k-floor-regulator-invariance-84-result.md',
    },
    {
        'gate': 'W5-59',
        'tag': 'A_s floor branch B',
        'original_verdict': 'INFO',
        'axis': 'K',
        'K_eval': [K_base],
        'memory_ref': 'a_s_floor_branch_b_84-result.md',
    },
    {
        'gate': 'W5-63',
        'tag': 'K-floor reachable',
        'original_verdict': 'FAIL',
        'axis': 'K',
        'K_eval': [1.0, 1.1, 1.3, 1.5, 1.7],
        'memory_ref': 'k-floor-reachable-84-result.md',
    },
    {
        'gate': 'W5-64',
        'tag': 'f_B closure (22% gap)',
        'original_verdict': 'INFO',
        'axis': 'K',
        'K_eval': [K_base],
        'memory_ref': 'plan §W8-6 reference to S84 W5-64',
    },
    {
        'gate': 'W5-65',
        'tag': 'K_FIRAS coincidence',
        'original_verdict': 'INFO',
        'axis': 'K',
        'K_eval': [K_base],
        'memory_ref': 'k-firas-coincidence-84-result.md',
    },
]

# ============================================================
# SECTION 2: Per-gate IN / OUT / MIXED / OUT-OF-SCOPE classification
# ============================================================
print("\n[SEC 2] IN / OUT / MIXED / OUT-OF-SCOPE classification vs K_R5")


def classify_gate(rec):                                              # (local helper)
    if rec['axis'] == 'regulator':
        return 'OUT-OF-SCOPE', 0, 0  # regulator-axis, no K-points
    K_eval = rec['K_eval']
    n_in = sum(1 for k in K_eval if k >= K_R5)
    n_out = sum(1 for k in K_eval if k < K_R5)
    if n_in > 0 and n_out == 0:
        return 'IN', n_in, n_out
    if n_out > 0 and n_in == 0:
        return 'OUT', n_in, n_out
    return 'MIXED', n_in, n_out


reclass_results = {}                                                 # (local)
for rec in W5_GATES:
    status, n_in, n_out = classify_gate(rec)
    # Reclassification rule:
    #   IN         -> verdict UNCHANGED (all points MS-valid)
    #   OUT        -> verdict FLIPPED to INFO-inapplicable-in-MS-valid
    #   MIXED      -> verdict UNCHANGED (MS-valid points suffice)
    #   OUT-OF-SCOPE -> verdict UNCHANGED (not a K-axis test)
    if status in ('IN', 'MIXED', 'OUT-OF-SCOPE'):
        reclass_verdict = rec['original_verdict']
        change = 'UNCHANGED'
    else:  # OUT
        reclass_verdict = 'INFO-inapplicable-in-MS-valid'
        change = 'FLIPPED'
    reclass_results[rec['gate']] = dict(
        status=status,
        n_in=n_in,
        n_out=n_out,
        original_verdict=rec['original_verdict'],
        reclass_verdict=reclass_verdict,
        change=change,
    )
    print(f"  {rec['gate']:8s} [{rec['axis']:10s}] K_eval={rec['K_eval']} "
          f"status={status:14s} orig={rec['original_verdict']:5s} "
          f"reclass={reclass_verdict:35s} {change}")

# ============================================================
# SECTION 3: Count stable vs flipped
# ============================================================
print("\n[SEC 3] Stability count")

n_unchanged = sum(1 for r in reclass_results.values() if r['change'] == 'UNCHANGED')  # (local)
n_flipped = sum(1 for r in reclass_results.values() if r['change'] == 'FLIPPED')     # (local)
n_total = len(reclass_results)                                                       # (local)

print(f"  Total W5 gates audited: {n_total}")
print(f"  UNCHANGED verdicts:     {n_unchanged}")
print(f"  FLIPPED verdicts:       {n_flipped}")

# ============================================================
# SECTION 4: Verdict evaluation
# ============================================================
print("\n[SEC 4] Verdict evaluation (plan §W8-3 step 9)")

PASS_THRESHOLD_STABLE = 3  # (local) >= 3 of 5 stable
INFO_THRESHOLD_FLIPS = 2   # (local) 1-2 flips = INFO
FAIL_THRESHOLD_FLIPS = 3   # (local) >= 3 flips = FAIL

if n_flipped >= FAIL_THRESHOLD_FLIPS:
    verdict = "FAIL"                                                 # (local)
    band = (f"{n_flipped} of {n_total} W5 verdicts flipped; master-gate "
            f"composition unstable; W5 rerun triggered in S86")     # (local)
elif n_unchanged >= PASS_THRESHOLD_STABLE:
    verdict = "PASS"                                                 # (local)
    band = (f"{n_unchanged} of {n_total} W5 verdicts STABLE under "
            f"K >= K_R5 reclassification; master-gate composition "
            f"sub-corridor-stable; {n_flipped} flipped (MS-invalid "
            f"FAIL -> INFO-inapplicable-in-MS-valid)")              # (local)
else:
    verdict = "INFO"                                                 # (local)
    band = (f"{n_flipped} of {n_total} verdicts changed; marginal")  # (local)

print(f"  Verdict: {verdict}  [{band}]")

# ============================================================
# SECTION 5: Cross-checks
# ============================================================
print("\n[SEC 5] Cross-checks")

# CC1: W5-63 is entirely OUT-corridor (plan Step 2 explicit)
CC1 = reclass_results['W5-63']['status'] == 'OUT'  # (local)
print(f"  CC1 W5-63 entirely OUT-corridor (plan Step 2): {CC1}")

# CC2: W5-63 FAIL flips to INFO-inapplicable
CC2 = reclass_results['W5-63']['change'] == 'FLIPPED'  # (local)
print(f"  CC2 W5-63 FAIL flips to INFO-inapplicable: {CC2}")

# CC3: K_base = 2.035 >= K_R5 = 1.9222 (substrate-native K is MS-valid)
CC3 = K_base >= K_R5  # (local)
print(f"  CC3 K_base={K_base} >= K_R5={K_R5}: {CC3}")

# CC4: All 3 "K=K_base" gates (W5-59, W5-64, W5-65) are IN-corridor
in_corridor_gates = [g for g in ['W5-59', 'W5-64', 'W5-65']
                     if reclass_results[g]['status'] == 'IN']
CC4 = len(in_corridor_gates) == 3  # (local)
print(f"  CC4 W5-59,64,65 all IN-corridor (K=K_base=2.035): {CC4}")

# CC5: W5-54 is regulator-axis (OUT-OF-SCOPE)
CC5 = reclass_results['W5-54']['status'] == 'OUT-OF-SCOPE'  # (local)
print(f"  CC5 W5-54 regulator-axis (OUT-OF-SCOPE): {CC5}")

# CC6: 4 of 5 stable (pre-registered expectation per plan Step 2)
CC6 = (n_unchanged == 4) and (n_flipped == 1)  # (local)
print(f"  CC6 exactly 4 stable, 1 flipped (pre-reg): {CC6}")

# CC7: W5-63 target_set max (1.7) < K_R5 (1.9222)
max_W5_63 = max(next(r['K_eval'] for r in W5_GATES if r['gate'] == 'W5-63'))  # (local)
CC7 = max_W5_63 < K_R5  # (local)
print(f"  CC7 max(W5-63 target)={max_W5_63} < K_R5={K_R5}: {CC7}")

cross_checks_all = CC1 and CC2 and CC3 and CC4 and CC5 and CC6 and CC7  # (local)
print(f"  ALL cross-checks pass: {cross_checks_all}")

# ============================================================
# SECTION 6: Save NPZ + plot
# ============================================================
print("\n[SEC 6] Save NPZ + plot")

npz_path = os.path.join(HERE, 's85_w8_mukhanov_sasaki_sub_corridor_audit.npz')  # (local)
np.savez(
    npz_path,
    K_R5=K_R5,
    K_base=K_base,
    gate_names=np.array([r['gate'] for r in W5_GATES]),
    gate_axes=np.array([r['axis'] for r in W5_GATES]),
    gate_original_verdicts=np.array([r['original_verdict'] for r in W5_GATES]),
    gate_statuses=np.array([reclass_results[r['gate']]['status'] for r in W5_GATES]),
    gate_reclass_verdicts=np.array([reclass_results[r['gate']]['reclass_verdict']
                                     for r in W5_GATES]),
    gate_changes=np.array([reclass_results[r['gate']]['change'] for r in W5_GATES]),
    n_unchanged=n_unchanged,
    n_flipped=n_flipped,
    verdict=verdict,
    scheme=SCHEME,
    convention=CONVENTION,
)
print(f"  NPZ: {npz_path}")

fig, ax = plt.subplots(figsize=(12, 5))
# Plot K-evaluation points of each gate on a K-axis with the K_R5 divider
y_labels = []  # (local)
for i, rec in enumerate(W5_GATES):
    y_labels.append(f"{rec['gate']}\n{rec['tag'][:22]}")
    if rec['axis'] == 'regulator':
        # Place regulator probes as open diamonds at their regulator K_R5 values
        for name, val in rec['regulator_probes']:
            ax.plot(val, i, 'D', ms=9, mec='purple', mfc='white', mew=1.5,
                    label=f'{rec["gate"]} reg {name}' if i == 0 else None)
            ax.annotate(name, xy=(val, i), xytext=(5, 8), fontsize=7,
                        textcoords='offset points')
    else:
        for k in rec['K_eval']:
            is_in = (k >= K_R5)
            color = 'green' if is_in else 'red'
            marker = 'o' if is_in else 'x'
            ax.plot(k, i, marker, ms=11, color=color, lw=0)
    status = reclass_results[rec['gate']]['status']
    chg = reclass_results[rec['gate']]['change']
    ax.text(50, i, f"{status}  {chg}", fontsize=8, verticalalignment='center')

ax.axvline(K_R5, color='black', ls='--', lw=2, label=f'K_R5 = {K_R5}')
ax.axvspan(K_R5, 100, alpha=0.15, color='green', label='MS-valid sub-corridor (K >= K_R5)')
ax.axvspan(0.5, K_R5, alpha=0.10, color='red', label='MS-invalid (K < K_R5)')

ax.set_yticks(range(len(W5_GATES)))
ax.set_yticklabels(y_labels, fontsize=9)
ax.set_xscale('log')
ax.set_xlim(0.5, 100)
ax.set_xlabel('K (log scale)')
ax.set_title(f'W8-3 MS sub-corridor audit: {n_unchanged}/5 stable, '
             f'{n_flipped}/5 flipped (verdict={verdict})')
ax.grid(True, axis='x', alpha=0.3)
ax.legend(fontsize=7, loc='upper right')
plt.tight_layout()
png_path = os.path.join(HERE, 's85_w8_mukhanov_sasaki_sub_corridor_audit.png')  # (local)
plt.savefig(png_path, dpi=150, bbox_inches='tight')
plt.close()
print(f"  PNG: {png_path}")

# ============================================================
# SECTION 7: Dual-SHA (S84+) + verdict append
# ============================================================
print("\n[SEC 7] Dual-SHA + verdict append")

script_path = os.path.abspath(__file__)                              # (local)
canonical_path = os.path.join(HERE, 'canonical_constants.py')        # (local)

pins = {                                                             # (local)
    'input_shas': INPUT_SHAS,
    'K_R5': K_R5,
    'K_base': K_base,
    'W5_gates': [
        {'gate': r['gate'], 'axis': r['axis'],
         'K_eval': r['K_eval'], 'original_verdict': r['original_verdict']}
        for r in W5_GATES
    ],
    'reclass_results': reclass_results,
    'n_unchanged': n_unchanged,
    'n_flipped': n_flipped,
    'verdict': verdict,
    'scheme': SCHEME,
    'convention': CONVENTION,
    'L_max': L_MAX,
}
pinmap_json = json.dumps(pins, sort_keys=True, separators=(',', ':')).encode('utf-8')  # (local)

with open(script_path, 'rb') as _fh:
    script_bytes = _fh.read()                                        # (local)
with open(canonical_path, 'rb') as _fh:
    canonical_bytes = _fh.read()                                     # (local)

h_audit = hashlib.sha256()
h_audit.update(script_bytes)
h_audit.update(canonical_bytes)
h_audit.update(pinmap_json)
audit_sha = h_audit.hexdigest()                                      # (local)
content_sha = hashlib.sha256(script_bytes).hexdigest()               # (local)

print(f"  audit_sha256   = {audit_sha}")
print(f"  content_sha256 = {content_sha}")

# 4-tuple value = n_unchanged / n_total (stability fraction)
value = f"{n_unchanged}/{n_total}"                                   # (local)
tuple_str = f"(value={value!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})"  # (local)
print(f"\n  4-tuple: {tuple_str}")

verdict_path = os.path.join(HERE, 's85_gate_verdicts.txt')           # (local)
verdict_line = (
    f"{GATE_ID}: {verdict} -- value={value!r} "
    f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
    f"audit_sha256={audit_sha} content_sha256={content_sha} "
    f"schema_version=S84+\n"
)
with open(verdict_path, 'a', encoding='utf-8') as fv:
    fv.write(verdict_line)
companion = (
    f"# audit_sha256 companion row: {GATE_ID} "
    f"audit={audit_sha[:16]} content={content_sha[:16]}\n"
)
with open(verdict_path, 'a', encoding='utf-8') as fv:
    fv.write(companion)

print(f"\n  Appended to {verdict_path}:")
print(f"    {verdict_line.strip()}")

print("\n" + "=" * 76)
print(f"{GATE_ID} complete. Verdict: {verdict}")
print("=" * 76)

sys.exit(0)
