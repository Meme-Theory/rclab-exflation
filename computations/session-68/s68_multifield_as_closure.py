#!/usr/bin/env python3
"""
s68_multifield_as_closure.py — Combined A_s From All Channels (AS-CLOSURE-68)
=============================================================================

Session 68, Wave 2-A.  Gen-Physicist.

Purpose:
    Combine all A_s correction channels from S67 and S68 Wave 1 to determine
    the total corrected A_s and its gap from the Planck measurement.

Channels:
    1. Baseline: multifield delta-N (S67 W3-B) → A_s = 3.29e-10
    2. Acoustic transfer (W1-A): |T|^2 = 1 identically (no correction)
    3. BCS dressing (W1-B): delta_As/As = +11.2%
    4. RG a2 mode propagation (W1-D, multifield): delta_As/As = +0.87%

Pre-registered gate:
    AS-CLOSURE-68:
        PASS:  gap < 0.3 OOM
        FAIL:  gap > 1.0 OOM
        INFO:  0.3 <= gap <= 1.0 OOM

All constants from canonical_constants.py.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from canonical_constants import A_s_CMB, a2_fold, a4_fold

# =============================================================================
#  1. LOAD INPUT DATA
# =============================================================================

base_dir = os.path.dirname(__file__)

# S67 multifield delta-N baseline
d67 = np.load(os.path.join(base_dir, 's67_multifield_delta_n.npz'), allow_pickle=True)
A_s_baseline = float(d67['A_s_multi_m1'])       # 3.29e-10
gap_baseline_OOM = float(d67['gap_m1_OOM'])      # -0.805

# S68 W1-A: acoustic transfer
d_at = np.load(os.path.join(base_dir, 's68_acoustic_transfer.npz'), allow_pickle=True)
T_sq = float(d_at['T_sq'])                       # 1.0

# S68 W1-B: BCS dressing
d_bcs = np.load(os.path.join(base_dir, 's68_bcs_dressed_mode.npz'), allow_pickle=True)
delta_As_bcs_total = float(d_bcs['delta_As_total_exact'])  # +0.1117
A_s_bcs = float(d_bcs['A_s_bcs'])                          # 3.66e-10
# Individual BCS sub-channels
delta_As_A = float(d_bcs['delta_As_A'])           # mode variance: -0.0156
delta_As_B = float(d_bcs['delta_As_B'])           # eps_H correction: +0.1546
delta_As_C = float(d_bcs['delta_As_C'])           # sound speed: -0.0219

# S68 W1-D: RG correction (multifield channel)
d_rg = np.load(os.path.join(base_dir, 's68_rg_a2_mode_prop.npz'), allow_pickle=True)
delta_As_rg_mf = float(d_rg['delta_As_mf_frac'])  # +0.00866
delta_As_rg_sf = float(d_rg['delta_As_sf_frac'])  # -0.0495
# eps_H cancellation theorem verification
eps_H_cancel_dev = float(d_rg['eps_H_cancellation_max_deviation'])  # ~6e-13

# =============================================================================
#  2. CHANNEL-BY-CHANNEL COMBINATION
# =============================================================================

# Step 1: Baseline
A_s_0 = A_s_baseline
gap_0 = np.log10(A_s_CMB / A_s_0)  # positive means A_s_0 < A_s_CMB

print("=" * 72)
print("AS-CLOSURE-68: Combined A_s From All Channels")
print("=" * 72)
print()
print(f"Planck A_s (target):           {A_s_CMB:.3e}")
print()

print("--- Step 1: Baseline (multifield delta-N, S67 W3-B) ---")
print(f"  A_s_baseline = {A_s_0:.6e}")
print(f"  Gap from Planck = {gap_0:.4f} OOM")
print()

# Step 2: Acoustic transfer — multiplicative factor
A_s_1 = A_s_0 * T_sq
gap_1 = np.log10(A_s_CMB / A_s_1)
print("--- Step 2: Acoustic transfer (W1-A) ---")
print(f"  |T(k)|^2 = {T_sq:.1f} (Weinberg superhorizon conservation)")
print(f"  A_s_after_transfer = {A_s_1:.6e}")
print(f"  Gap from Planck = {gap_1:.4f} OOM  (no change)")
print()

# Step 3: BCS dressing
A_s_2 = A_s_1 * (1.0 + delta_As_bcs_total)
gap_2 = np.log10(A_s_CMB / A_s_2)
print("--- Step 3: BCS dressing (W1-B) ---")
print(f"  delta_As/As (total) = {delta_As_bcs_total:+.4f}")
print(f"    Channel A (mode variance): {delta_As_A:+.4f}")
print(f"    Channel B (eps_H):         {delta_As_B:+.4f}")
print(f"    Channel C (sound speed):   {delta_As_C:+.4f}")
print(f"  A_s_after_BCS = {A_s_2:.6e}")
print(f"  Gap from Planck = {gap_2:.4f} OOM  (closed {gap_1 - gap_2:.4f} OOM)")
print()

# Step 4: RG correction (multifield channel, since baseline is multifield)
A_s_3 = A_s_2 * (1.0 + delta_As_rg_mf)
gap_3 = np.log10(A_s_CMB / A_s_3)
print("--- Step 4: RG a2 mode propagation (W1-D, multifield) ---")
print(f"  delta_As/As (multifield) = {delta_As_rg_mf:+.6f}")
print(f"  eps_H cancellation theorem deviation: {eps_H_cancel_dev:.2e}")
print(f"  A_s_after_RG = {A_s_3:.6e}")
print(f"  Gap from Planck = {gap_3:.4f} OOM  (closed {gap_2 - gap_3:.4f} OOM)")
print()

# =============================================================================
#  3. DOUBLE-COUNTING VERIFICATION
# =============================================================================

print("--- Double-Counting Verification ---")
print()
print("  BCS enters through: eps_H modification (Bogoliubov coherence factors")
print("    shift the quasiparticle spectrum, changing the slow-roll parameter).")
print("    Also: mode variance shift and sound speed renormalization.")
print("  RG enters through: Friedmann equation H^2 ~ a_2(Lambda). The BCS")
print("    sector renormalizes a_2 at scale Lambda, changing H at fixed tau.")
print()
print("  The BCS eps_H correction modifies dH/dtau relative to H (slow-roll).")
print("  The RG a_2 correction modifies H^2 itself (absolute normalization).")
print("  These act on DIFFERENT factors in A_s ~ H^2 / (eps_H * c_s):")
print("    - BCS dressing: eps_H -> eps_H * (1 + delta_eps_H),")
print("      plus mode variance and c_s shifts")
print("    - RG correction: H^2 -> H^2 * (1 + delta_a2/a_2),")
print("      with eps_H cancellation theorem (uniform a2 shift => exact")
print("      eps_H invariance, verified to {:.1e})".format(eps_H_cancel_dev))
print()
print("  The RG a_2 correction is computed from the FULL fiber (diluted by ~5x")
print("  from BCS sector to all Peter-Weyl sectors). The BCS eps_H correction")
print("  is a local-in-sector effect on the slow-roll dynamics. These are")
print("  algebraically independent: no double-counting.")
print()

# Also verify: the BCS correction was computed in W1-B using BARE a2.
# The RG correction was computed in W1-D using the DRESSED a2.
# If W1-B had used dressed a2, there would be cross-terms. But since
# it didn't, the multiplicative combination is exact to first order.
cross_term = delta_As_bcs_total * delta_As_rg_mf
print(f"  Cross-term (BCS x RG) = {cross_term:.2e} (second-order, negligible)")
print(f"  Multiplicative vs additive discrepancy: {cross_term:.2e}")
print()

# =============================================================================
#  4. FINAL COMBINED RESULT
# =============================================================================

A_s_final = A_s_3
gap_final = gap_3
factor_needed = 10.0**gap_final  # factor by which A_s must still increase

print("=" * 72)
print("FINAL COMBINED RESULT")
print("=" * 72)
print()
print(f"  A_s (combined, all channels) = {A_s_final:.6e}")
print(f"  A_s (Planck 2018)            = {A_s_CMB:.3e}")
print(f"  Gap from Planck              = {gap_final:.4f} OOM")
print(f"  Factor needed to close gap   = {factor_needed:.2f}x")
print(f"  Total correction from baseline: {(A_s_final/A_s_baseline - 1)*100:.2f}%")
print()

# =============================================================================
#  5. GATE VERDICT
# =============================================================================

if gap_final < 0.3:
    verdict = "PASS"
    detail = f"A_s gap = {gap_final:.3f} OOM < 0.3 OOM threshold"
elif gap_final > 1.0:
    verdict = "FAIL"
    detail = f"A_s gap = {gap_final:.3f} OOM > 1.0 OOM threshold"
else:
    verdict = "INFO"
    detail = f"A_s gap = {gap_final:.3f} OOM (between 0.3 and 1.0 OOM)"

print(f"Gate AS-CLOSURE-68: {verdict}")
print(f"  Threshold: PASS < 0.3 OOM, FAIL > 1.0 OOM, INFO between")
print(f"  Computed:  {gap_final:.4f} OOM")
print(f"  Detail:    {detail}")
print()

# =============================================================================
#  6. CANDIDATE MECHANISMS FOR REMAINING GAP
# =============================================================================

print("--- Candidate Mechanisms for Remaining ~0.76 OOM Gap ---")
print()
print("  The remaining gap requires a factor {:.1f}x amplification.".format(factor_needed))
print("  Candidate channels:")
print()
print("  (a) Off-Jensen deformation: The baseline uses Jensen SU(3).")
print("      Off-Jensen tau-profiles during transit create tau-dependent")
print("      gradients that modify both eps_H and the effective potential.")
print("      Estimated range: 0.0 to ~2 OOM (direction uncertain).")
print()
print("  (b) Multi-level Landau-Zener: The transit passes through multiple")
print("      avoided crossings. Non-adiabatic level mixing enhances the")
print("      effective number of contributing modes. Could amplify sigma_sq")
print("      by O(1) factors.")
print()
print("  (c) Inter-branch correlations: The multifield delta-N sum treats")
print("      branches as uncorrelated. Cross-correlations between acoustic,")
print("      Leggett, and optical branches could add or subtract.")
print("      Need: explicit computation of C_{IJ} = <delta_phi_I delta_phi_J>.")
print()
print("  (d) Pre-transit initial state: The baseline assumes vacuum initial")
print("      conditions. If the pre-transit state has squeezed or thermal")
print("      fluctuations (from the BCS condensate), the initial power")
print("      could be enhanced.")
print()
print("  (e) Stochastic delta-N: The deterministic delta-N may undercount")
print("      fluctuations in the strongly non-equilibrium transit.")
print("      Stochastic corrections scale as H^2 / (2*pi*eps_H), which")
print("      at the fold gives a large correction for small eps_H.")
print()

# =============================================================================
#  7. CONVERGENCE HISTORY TABLE
# =============================================================================

print("--- A_s Convergence History ---")
print()
print("  Step                         A_s            Gap (OOM)  Correction")
print("  " + "-" * 68)
print(f"  Transit production (S38)     ~exp(+15)      15.09      ---")
print(f"  Multifield delta-N (S67)     {A_s_0:.3e}    {gap_0:.3f}     -14.28 OOM")
print(f"  + Acoustic transfer (W1-A)   {A_s_1:.3e}    {gap_1:.3f}      0.000 OOM")
print(f"  + BCS dressing (W1-B)        {A_s_2:.3e}    {gap_2:.3f}     -{gap_1-gap_2:.3f} OOM")
print(f"  + RG correction (W1-D)       {A_s_3:.3e}    {gap_3:.3f}     -{gap_2-gap_3:.3f} OOM")
print(f"  " + "-" * 68)
print(f"  TOTAL CLOSED                                           {15.09 - gap_final:.2f} OOM / 15.09")
print(f"  REMAINING                                              {gap_final:.3f} OOM")
print()

# =============================================================================
#  8. SAVE NPZ
# =============================================================================

out_path = os.path.join(base_dir, 's68_multifield_as_closure.npz')
np.savez(out_path,
    # Gate
    gate_name='AS-CLOSURE-68',
    gate_verdict=verdict,
    gate_detail=detail,
    # Baseline
    A_s_baseline=A_s_baseline,
    gap_baseline_OOM=gap_0,
    # Channel corrections
    T_sq_acoustic=T_sq,
    delta_As_bcs_total=delta_As_bcs_total,
    delta_As_bcs_A=delta_As_A,
    delta_As_bcs_B=delta_As_B,
    delta_As_bcs_C=delta_As_C,
    delta_As_rg_mf=delta_As_rg_mf,
    delta_As_rg_sf=delta_As_rg_sf,
    eps_H_cancellation_dev=eps_H_cancel_dev,
    cross_term_BCS_RG=cross_term,
    # Sequential A_s values
    A_s_after_transfer=A_s_1,
    A_s_after_bcs=A_s_2,
    A_s_after_rg=A_s_3,
    A_s_final=A_s_final,
    # Sequential gap values
    gap_after_transfer=gap_1,
    gap_after_bcs=gap_2,
    gap_after_rg=gap_3,
    gap_final=gap_final,
    # Derived
    factor_needed=factor_needed,
    total_correction_pct=(A_s_final / A_s_baseline - 1.0) * 100,
    A_s_CMB=A_s_CMB,
    # Source traceability
    sources=np.array([
        's67_multifield_delta_n.npz',
        's68_acoustic_transfer.npz',
        's68_bcs_dressed_mode.npz',
        's68_rg_a2_mode_prop.npz'
    ]),
)
print(f"Saved: {out_path}")

# =============================================================================
#  9. PLOT: A_s Gap Closure Waterfall
# =============================================================================

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# --- Left panel: Waterfall chart ---
ax = axes[0]
labels = [
    'Transit\nproduction',
    'Multifield\ndelta-N',
    'Acoustic\ntransfer',
    'BCS\ndressing',
    'RG\ncorrection',
    'Final\ngap'
]
# Gap values at each stage (OOM from Planck, positive = below)
gaps_history = [15.09, gap_0, gap_1, gap_2, gap_3]
# Corrections (positive = gap closure)
corrections = [
    0,                    # transit start
    -(gap_0 - 15.09),    # delta-N: negative means closed
    -(gap_1 - gap_0),    # acoustic: 0
    -(gap_2 - gap_1),    # BCS
    -(gap_3 - gap_2),    # RG
]

# Waterfall: plot the gap at each stage
x = np.arange(len(labels))
gap_vals = [15.09, gap_0, gap_1, gap_2, gap_3, gap_3]

# Color by type
colors = ['#d62728', '#2ca02c', '#7f7f7f', '#2ca02c', '#2ca02c', '#1f77b4']
bar_bottoms = [0] * len(labels)

# Simple bar chart of gap at each stage
bars = ax.bar(x, gap_vals, color=colors, edgecolor='black', linewidth=0.5, alpha=0.8)

# Planck threshold lines
ax.axhline(y=0.3, color='green', linestyle='--', linewidth=1.5, alpha=0.7, label='PASS threshold (0.3)')
ax.axhline(y=1.0, color='orange', linestyle='--', linewidth=1.5, alpha=0.7, label='FAIL threshold (1.0)')

ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=9)
ax.set_ylabel('Gap from Planck A_s (OOM)', fontsize=11)
ax.set_title('A_s Gap Closure: Channel by Channel', fontsize=12, fontweight='bold')
ax.legend(fontsize=8, loc='upper right')

# Annotate gap values
for i, v in enumerate(gap_vals):
    if v > 2:
        ax.text(i, v + 0.3, f'{v:.2f}', ha='center', fontsize=9, fontweight='bold')
    else:
        ax.text(i, v + 0.05, f'{v:.3f}', ha='center', fontsize=8)

ax.set_ylim(0, 17)

# --- Right panel: Channel decomposition pie/bar ---
ax2 = axes[1]

# Show the corrections as a horizontal bar chart
channel_names = [
    'Multifield delta-N\n(S67, 14.28 OOM)',
    'Acoustic transfer\n(W1-A, |T|^2=1)',
    'BCS dressing\n(W1-B, +11.2%)',
    'RG correction\n(W1-D, +0.87%)',
    'Remaining gap'
]
corrections_plot = [
    15.09 - gap_0,   # delta-N closed
    gap_0 - gap_1,   # acoustic
    gap_1 - gap_2,   # BCS
    gap_2 - gap_3,   # RG
    gap_3,            # remaining
]
colors2 = ['#2ca02c', '#7f7f7f', '#17becf', '#9467bd', '#d62728']

barh = ax2.barh(range(len(channel_names)), corrections_plot,
                color=colors2, edgecolor='black', linewidth=0.5, alpha=0.8)

ax2.set_yticks(range(len(channel_names)))
ax2.set_yticklabels(channel_names, fontsize=9)
ax2.set_xlabel('OOM contribution', fontsize=11)
ax2.set_title('Channel Decomposition of 15.09 OOM Gap', fontsize=12, fontweight='bold')
ax2.invert_yaxis()

# Annotate values
for i, v in enumerate(corrections_plot):
    if v > 0.01:
        ax2.text(v + 0.1, i, f'{v:.3f}', va='center', fontsize=9)

# Add total line
ax2.axvline(x=15.09, color='black', linestyle=':', linewidth=1, alpha=0.5)
ax2.text(15.09, -0.5, f'Total = {15.09:.2f}', ha='center', fontsize=8, alpha=0.7)

plt.tight_layout()
plt.savefig(os.path.join(base_dir, 's68_multifield_as_closure.png'), dpi=150, bbox_inches='tight')
print(f"Saved: {os.path.join(base_dir, 's68_multifield_as_closure.png')}")

print()
print("DONE.")
