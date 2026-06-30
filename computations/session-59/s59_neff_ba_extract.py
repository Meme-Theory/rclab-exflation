#!/usr/bin/env python3
"""Extract key results from s59_neff_ba.npz to text file."""
import numpy as np
import os

data_dir = os.path.dirname(__file__)
d = np.load(os.path.join(data_dir, 's59_neff_ba.npz'), allow_pickle=True)

out = os.path.join(data_dir, 's59_neff_ba_results.txt')
with open(out, 'w') as f:
    f.write("=== NEFF-BA-59 Results Extraction ===\n\n")
    f.write("All keys in npz:\n")
    for k in sorted(d.files):
        v = d[k]
        try:
            val = float(v)
            f.write(f"  {k} = {val}\n")
        except (TypeError, ValueError):
            if hasattr(v, 'shape'):
                f.write(f"  {k} = array shape {v.shape}, dtype {v.dtype}\n")
                if v.size < 50:
                    f.write(f"    values: {v}\n")
            else:
                f.write(f"  {k} = {v}\n")

    f.write("\n=== Key Gate Results ===\n")
    # Extract gate-critical values
    for key in ['Delta_Neff_conservative', 'Delta_Neff_aggressive',
                'Delta_Neff_CMB_conservative', 'Delta_Neff_CMB_aggressive',
                'Delta_Neff_BBN_conservative', 'Delta_Neff_BBN_aggressive',
                'Delta_Neff', 'gate_verdict',
                'g_BA', 'g_BA_eff', 'F_BA', 'E_matter_Volovik',
                'rho_BA_over_rho_gamma_Sh', 'rho_BA_over_rho_SM_Sh',
                'dilution_BBN', 'dilution_CMB']:
        if key in d.files:
            v = d[key]
            try:
                val = float(v)
                f.write(f"  {key} = {val:.6e}\n")
            except (TypeError, ValueError):
                f.write(f"  {key} = {v}\n")

print(f"Written to {out}")
