#!/usr/bin/env python3
"""Extract PENROSE-ACCESS-59 results from npz and write to txt."""
import numpy as np
import os

os.chdir("C:/sandbox/Ainulindale Exflation")
f = np.load("computations/session-59/s59_penrose_access.npz", allow_pickle=True)

out = []
out.append("PENROSE-ACCESS-59 RESULTS")
out.append("=" * 60)
out.append("")

# All keys
out.append("--- All keys ---")
for k in sorted(f.files):
    v = f[k]
    if v.ndim == 0:
        out.append(f"  {k} = {v.item()}")
    else:
        out.append(f"  {k}: shape={v.shape}, dtype={v.dtype}")
        if v.size <= 30:
            out.append(f"    values = {v}")

out.append("")
out.append("--- Key Results ---")
out.append(f"gate_verdict = {f['gate_verdict'].item()}")
out.append(f"alpha_multipair = {float(f['alpha_multipair']):.6f}")
out.append(f"alpha_Andreev = {float(f['alpha_Andreev']):.6f}")
out.append(f"alpha_total = {float(f['alpha_total']):.6f}")
out.append(f"alpha_crit = {float(f['alpha_crit']):.6f}")
out.append(f"alpha_margin = {float(f['alpha_margin']):.6f}")

out.append(f"r_npair3 = {float(f['r_npair3']):.6f}")
out.append(f"r_Andreev = {float(f['r_Andreev']):.6f}")
out.append(f"r_Poisson = {float(f['r_Poisson']):.6f}")
out.append(f"r_GOE = {float(f['r_GOE']):.6f}")

out.append(f"lambda_0 = {float(f['lambda_0']):.4f}")
out.append(f"lambda_1 = {float(f['lambda_1']):.4f}")
out.append(f"lambda_alpha = {float(f['lambda_alpha']):.4f}")

out.append(f"Gamma_Penrose = {float(f['Gamma_Penrose']):.6e}")
out.append(f"t_Penrose_MKK = {float(f['t_Penrose_MKK']):.6e}")
out.append(f"t_CC_reduction_s = {float(f['t_CC_reduction_s']):.6e}")

out.append(f"overlap_factor = {float(f['overlap_factor']):.4f}")
out.append(f"alpha_additive = {float(f['alpha_additive']):.6f}")
out.append(f"alpha_quadrature = {float(f['alpha_quadrature']):.6f}")

# Compute derived
alpha_total = float(f['alpha_total'])
alpha_crit = float(f['alpha_crit'])
ratio = alpha_total / alpha_crit
deficit = alpha_crit - alpha_total
out.append("")
out.append("--- Derived ---")
out.append(f"alpha_total / alpha_crit = {ratio:.4f}")
out.append(f"deficit = {deficit:.6f}")
out.append(f"percent_of_threshold = {ratio*100:.1f}%")

with open("computations/session-59/s59_penrose_access_results.txt", "w") as fout:
    fout.write("\n".join(out))
