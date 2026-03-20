#!/usr/bin/env python3
"""Run the 12 value-changed scripts and capture key output lines."""
import subprocess, os

PYTHON = os.path.join(os.path.dirname(__file__), "..",
                       "phonon-exflation-sim", ".venv312", "Scripts", "python.exe")
CWD = os.path.join(os.path.dirname(__file__), "..")

SCRIPTS = [
    ("s40_cc_transit.py",        "E_cond",    "0.156->0.137",  "12% GL->ED"),
    ("s42_dm_profile.py",        "E_cond",    "-0.115->-0.137", "19%"),
    ("s42_fabric_wz.py",         "E_cond",    "-0.115->-0.137", "19%"),
    ("s42_fabric_wz_v2.py",      "E_cond",    "-0.115->-0.137", "19%"),
    ("s42_hauser_feshbach.py",   "E_cond",    "-0.115->-0.137", "19%"),
    ("s43_friedmann_bcs.py",     "E_cond",    "-0.115->-0.137", "19%"),
    ("s43_flat_band.py",         "E_cond",    "-0.115->-0.137", "19%"),
    ("s43_schwinger_factor36.py","E_cond",    "0.115->0.137",   "19%"),
    ("s36_cc_arithmetic.py",     "M_KK",      "1e16->7.43e16",  "7.4x"),
    ("s43_offj_jsymm.py",        "M_KK",      "1e16->7.43e16",  "7.4x"),
    ("s44_tracelog_cc.py",       "rho_obs",   "2.3e-47->2.7e-47","17%"),
    ("s43_carlip_cc.py",         "Lambda_obs","2.888e-47->2.7e-47","7%"),
]

KEYWORDS = ['e_cond', 'e_exc', 'e_bcs', 'e_total', 'm_kk', 'rho_', 'lambda',
            'verdict', 'pass', 'fail', 'gate', 'result', 'ratio', 'gap',
            'orders', 'shortfall', 'cc_', 'n_e', 'epsilon']

for script, const, change, desc in SCRIPTS:
    path = os.path.join("tier0-computation", script)
    print(f"\n{'='*70}")
    print(f"  {script}: {const} {change} ({desc})")
    print(f"{'='*70}")

    try:
        result = subprocess.run(
            [PYTHON, path],
            capture_output=True, text=True, timeout=120, cwd=CWD
        )
    except subprocess.TimeoutExpired:
        print("  TIMEOUT (>120s)")
        continue
    except Exception as e:
        print(f"  ERROR: {e}")
        continue

    if result.returncode != 0:
        stderr_lines = result.stderr.strip().split('\n') if result.stderr else []
        last_err = stderr_lines[-3:] if len(stderr_lines) >= 3 else stderr_lines
        print(f"  EXIT {result.returncode}:")
        for el in last_err:
            print(f"    {el}")
        continue

    lines = result.stdout.split('\n')
    key_lines = []
    for line in lines:
        lo = line.lower().strip()
        if lo and any(kw in lo for kw in KEYWORDS):
            key_lines.append(line)

    if key_lines:
        print(f"  OUTPUT ({len(key_lines)} key lines / {len(lines)} total):")
        for kl in key_lines[:25]:
            print(f"    {kl}")
        if len(key_lines) > 25:
            print(f"    ... ({len(key_lines)-25} more)")
    else:
        print(f"  COMPLETED ({len(lines)} lines, no keyword matches)")
