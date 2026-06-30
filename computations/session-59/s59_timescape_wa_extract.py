#!/usr/bin/env python3
"""Extract all key results from s59_timescape_wa.npz to text file."""
import os, sys
import numpy as np

BASEDIR = os.path.dirname(os.path.abspath(__file__))
npz = np.load(os.path.join(BASEDIR, "s59_timescape_wa.npz"), allow_pickle=True)

out = os.path.join(BASEDIR, "s59_timescape_wa_results.txt")
with open(out, "w") as f:
    f.write("=== TIMESCAPE-WA-59: All NPZ Results ===\n\n")
    for key in sorted(npz.files):
        val = npz[key]
        f.write(f"{key}: {val}\n")
    f.write("\n=== Key Results for W4H-1 ===\n\n")

    # Gate
    f.write(f"gate_name: {npz['gate_name']}\n")
    f.write(f"gate_verdict: {npz['gate_verdict']}\n")
    f.write(f"gate_detail: {npz['gate_detail']}\n\n")

    # Core numbers
    f.write(f"delta_tau_eff: {float(npz['delta_tau_eff']):.6f}\n")
    f.write(f"sigma_tau: {float(npz['sigma_tau']):.6f}\n")
    f.write(f"delta_tau_KZ: {float(npz['delta_tau_KZ']):.6f}\n")
    f.write(f"delta_tau_per_delta_route1: {float(npz['delta_tau_per_delta_route1']):.3e}\n")
    f.write(f"delta_G_over_G: {float(npz['delta_G_over_G']):.6e}\n")
    f.write(f"delta_N_over_N: {float(npz['delta_N_over_N']):.6e}\n")
    f.write(f"corr_factor: {float(npz['corr_factor']):.6e}\n\n")

    # CPL fits
    alphas = npz['alphas']
    w0s = npz['w0_apparent']
    was = npz['wa_apparent']
    for i, a in enumerate(alphas):
        f.write(f"alpha={a}: w0_app={w0s[i]:.8f}, wa_app={was[i]:.8f}\n")

    f.write(f"\nBest (alpha=0.3): w0={float(npz['w0_result']):.8f}, wa={float(npz['wa_result']):.8f}\n")
    f.write(f"|w_a_apparent| = {abs(float(npz['wa_result'])):.8f}\n\n")

    # Shortfall
    f.write(f"corr_needed: {float(npz['corr_needed']):.6f}\n")
    f.write(f"delta_N_needed: {float(npz['delta_N_needed']):.6f}\n")
    f.write(f"shortfall: {float(npz['shortfall']):.1f}x\n\n")

    # Alpha-env
    f.write(f"delta_alpha_vw: {float(npz['delta_alpha_vw']):.3e}\n")
    f.write(f"alpha_shortfall: {float(npz['alpha_shortfall']):.1f}x\n\n")

    # delta_tau_for_wa
    if 'delta_tau_for_wa' in npz.files:
        f.write(f"delta_tau_for_wa: {float(npz['delta_tau_for_wa']):.4f}\n")

    f.write("\n=== DONE ===\n")

print("Results written to:", out)
