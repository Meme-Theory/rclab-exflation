"""
One-shot repair: recompute assessments from existing phase2b_sensitivity.json
data (which has complete results but truncated assessments due to numpy.bool_
serialization bug), rewrite the file, and update phase2b_summary.json.
"""

import json
import math
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

# --- Step 1: Parse the truncated sensitivity JSON ---
# The file is valid JSON up to the results section; assessments are truncated.
# We'll read the raw text and extract the valid portion.

sens_path = os.path.join(DATA_DIR, 'phase2b_sensitivity.json')
with open(sens_path, 'r') as f:
    raw = f.read()

# Find where assessments section starts and truncate before it
assess_idx = raw.find('"assessments"')
if assess_idx > 0:
    # Cut everything from "assessments" onward, strip trailing comma/whitespace
    truncated = raw[:assess_idx].rstrip()
    # Remove trailing comma if present
    if truncated.endswith(','):
        truncated = truncated[:-1]
    # Close the outer JSON object
    truncated += '\n}'
    partial = json.loads(truncated)
else:
    # File might already be valid
    partial = json.loads(raw)

config = partial['config']
results = partial['results']
breakthrough = config['breakthrough']

print("Loaded existing sensitivity data:")
for param, points in results.items():
    print(f"  {param}: {len(points)} scan points")

# --- Step 2: Recompute assessments ---

assessments = {}
for param_name, param_results in results.items():
    dh_values = [r['mean_d_over_h'] for r in param_results if r['mean_d_over_h'] > 0]

    if len(dh_values) < 2:
        assessments[param_name] = {'pass': False, 'reason': 'insufficient data'}
        continue

    log_dh = [math.log10(v) for v in dh_values]
    dh_range_oom = max(log_dh) - min(log_dh)

    bt_val = breakthrough[param_name]
    bt_dh = None
    for r in param_results:
        if r['param_value'] == bt_val and r['mean_d_over_h'] > 0:
            bt_dh = r['mean_d_over_h']
            break

    max_change_for_2x = 0.0
    if bt_dh is not None and bt_dh > 0:
        bt_log = math.log10(bt_dh)
        for r in param_results:
            if r['mean_d_over_h'] > 0 and r['param_value'] != bt_val:
                ratio = r['param_value'] / bt_val if bt_val != 0 else float('inf')
                if 0.5 <= ratio <= 2.0:
                    change = abs(math.log10(r['mean_d_over_h']) - bt_log)
                    max_change_for_2x = max(max_change_for_2x, change)

    pass_sensitivity = max_change_for_2x < 1.0
    fail_sensitivity = max_change_for_2x > 2.0

    assessments[param_name] = {
        'pass': pass_sensitivity,
        'fail_hard': fail_sensitivity,
        'dh_range_oom': dh_range_oom,
        'max_change_for_2x': max_change_for_2x,
    }

    status = 'PASS' if pass_sensitivity else 'FAIL'
    print(f"\n  {param_name}: {status}")
    print(f"    D/H range: {dh_range_oom:.2f} OOM")
    print(f"    Max change for 2x param: {max_change_for_2x:.2f} OOM")

all_pass = all(a['pass'] for a in assessments.values())
print(f"\n  Phase 2B.2 overall: {'PASS' if all_pass else 'FAIL'}")

# --- Step 3: Write repaired sensitivity JSON ---

output = {
    'config': config,
    'results': results,
    'assessments': assessments,
    'phase2b2_pass': all_pass,
}

with open(sens_path, 'w') as f:
    json.dump(output, f, indent=2)
print(f"\n  Repaired: {os.path.abspath(sens_path)}")

# --- Step 4: Update phase2b_summary.json ---

summary_path = os.path.join(DATA_DIR, 'phase2b_summary.json')
with open(summary_path, 'r') as f:
    summary = json.load(f)

# Fix subtask 2
summary['subtasks']['2']['passed'] = all_pass
summary['subtasks']['2']['error'] = None

# Recompute gate
blocking_pass = all(
    v['passed']
    for v in summary['subtasks'].values()
    if v['blocking'] and not v['skipped']
)
summary['gate_pass'] = blocking_pass
summary['blocking_pass'] = blocking_pass

with open(summary_path, 'w') as f:
    json.dump(summary, f, indent=2)
print(f"  Updated:  {os.path.abspath(summary_path)}")

# --- Final gate status ---
print(f"\n{'=' * 60}")
print(f"  PHASE 2B GATE: {'PASS' if blocking_pass else 'FAIL'}")
for k, v in sorted(summary['subtasks'].items()):
    block = '[BLOCKING]' if v['blocking'] else '[optional]'
    status = 'PASS' if v['passed'] else ('SKIP' if v['skipped'] else 'FAIL')
    err = f" ({v['error'][:40]})" if v.get('error') else ''
    print(f"    {block:11s} {v['name']:50s} {status}{err}")
print(f"{'=' * 60}")
