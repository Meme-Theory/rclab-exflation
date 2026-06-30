#!/usr/bin/env python3
"""Extract key results from s59_ricci_dw.npz to text file."""
import numpy as np
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

d = np.load('s59_ricci_dw.npz', allow_pickle=True)

with open('s59_ricci_dw_results.txt', 'w') as f:
    f.write("=== S59 RICCI-DW-59 Extracted Results ===\n\n")

    # Scalars
    f.write(f"tau_dw_geom    = {float(d['tau_dw_geom']):.8f}\n")
    f.write(f"tau_dw_arith   = {float(d['tau_dw_arith']):.8f}\n")
    f.write(f"A_crit         = {float(d['A_crit']):.10f}\n")
    f.write(f"sigma_crit     = {float(d['sigma_crit']):.10f}\n")
    f.write(f"sec_at_dw      = {float(d['sec_at_dw']):.10e}\n")
    f.write(f"tau_sec_zero   = {float(d['tau_sec_zero']):.8f}\n")
    f.write(f"tau_stab_cross = {float(d['tau_stab_cross']):.8f}\n")

    # Gate
    f.write(f"\ngate_name    = {str(d['gate_name'][0])}\n")
    f.write(f"gate_verdict = {str(d['gate_verdict'][0])}\n")
    f.write(f"gate_detail  = {str(d['gate_detail'][0])}\n")

    # Arrays at key tau values
    tau_vals = d['tau_vals']
    r1 = d['r1_arr']
    r2 = d['r2_arr']
    r3 = d['r3_arr']
    R = d['R_arr']
    A = d['A_aniso']
    smin = d['sec_min_arr']
    smax = d['sec_max_arr']
    nneg = d['n_neg_arr']
    L_eigs = d['L_eigs']
    rho = d['rho_arr']
    margin = d['margin_arr']

    f.write(f"\n=== Ricci components at tau=0 (validation) ===\n")
    f.write(f"r1(0) = {r1[0]:.10f}\n")
    f.write(f"r2(0) = {r2[0]:.10f}\n")
    f.write(f"r3(0) = {r3[0]:.10f}\n")
    f.write(f"R(0)  = {R[0]:.10f}\n")
    f.write(f"Expected: 3/(2*alpha)=0.5, R=12/alpha=4.0\n")

    f.write(f"\n=== Ricci at tau_DW (interpolated from nearest) ===\n")
    # Find nearest
    idx_dw = np.argmin(np.abs(tau_vals - float(d['tau_dw_geom'])))
    f.write(f"nearest tau = {tau_vals[idx_dw]:.6f} (idx={idx_dw})\n")
    f.write(f"r1 = {r1[idx_dw]:.10f}\n")
    f.write(f"r2 = {r2[idx_dw]:.10f}\n")
    f.write(f"r3 = {r3[idx_dw]:.10f}\n")
    f.write(f"R  = {R[idx_dw]:.10f}\n")
    f.write(f"A  = {A[idx_dw]:.10f}\n")
    f.write(f"sec_min = {smin[idx_dw]:.10e}\n")
    f.write(f"n_neg   = {nneg[idx_dw]}\n")

    f.write(f"\n=== Lichnerowicz eigenvalues at tau_DW ===\n")
    f.write(f"lam_L = {L_eigs[idx_dw]}\n")
    f.write(f"2*rho = {2*rho[idx_dw]:.10f}\n")
    f.write(f"margin = {margin[idx_dw]:.10f}\n")

    f.write(f"\n=== Sectional curvature sign change ===\n")
    n_neg_first = None
    for i in range(len(nneg)):
        if nneg[i] > 0:
            n_neg_first = i
            break
    if n_neg_first is not None:
        f.write(f"First n_neg>0 at tau={tau_vals[n_neg_first]:.6f} (idx={n_neg_first})\n")
        if n_neg_first > 0:
            f.write(f"Last n_neg=0 at tau={tau_vals[n_neg_first-1]:.6f}\n")
    else:
        f.write("n_neg=0 throughout\n")

    f.write(f"\n=== Range summaries ===\n")
    f.write(f"A_aniso range: [{np.min(A):.8f}, {np.max(A):.8f}]\n")
    f.write(f"sec_min range: [{np.min(smin):.8f}, {np.max(smax):.8f}]\n")
    f.write(f"R range:       [{np.min(R):.6f}, {np.max(R):.6f}]\n")
    f.write(f"margin range:  [{np.min(margin):.6f}, {np.max(margin):.6f}]\n")

    f.write(f"\n=== Key ratios ===\n")
    # r2/r3 at DW
    f.write(f"r2/r3 at DW = {r2[idx_dw]/r3[idx_dw]:.8f}\n")
    # r2/r1 at DW
    f.write(f"r2/r1 at DW = {r2[idx_dw]/r1[idx_dw]:.8f}\n")
    # anisotropy growth rate
    dA_dtau = np.gradient(A, tau_vals)
    f.write(f"dA/dtau at tau=0: {dA_dtau[0]:.6f}\n")
    f.write(f"dA/dtau at DW:    {dA_dtau[idx_dw]:.6f}\n")

    f.write(f"\n=== All stored keys ===\n")
    for k in sorted(d.files):
        v = d[k]
        if v.ndim == 0:
            f.write(f"  {k}: scalar = {v}\n")
        else:
            f.write(f"  {k}: shape={v.shape}, dtype={v.dtype}\n")

print("Done: s59_ricci_dw_results.txt")
