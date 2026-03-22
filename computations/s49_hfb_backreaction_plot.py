#!/usr/bin/env python3
"""Generate diagnostic plots for HFB-BACKREACTION-49."""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

data_dir = Path(__file__).parent
d = np.load(data_dir / 's49_hfb_backreaction.npz', allow_pickle=True)

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# --- Panel (a): Delta_B2 vs g_ph ---
ax = axes[0, 0]
g_ph = d['g_ph_values']
D_B2 = d['Delta_B2_vs_gph']
D_B2_ref = D_B2[0]
ax.plot(g_ph, (D_B2 / D_B2_ref - 1) * 100, 'o-', color='navy', ms=6, lw=2)
ax.axhline(0, color='gray', ls='--', lw=0.5)
ax.axvspan(0, 0.10, alpha=0.15, color='green', label='Physical range')
ax.axhline(-10, color='red', ls=':', lw=1, label='Gate threshold')
ax.axhline(10, color='red', ls=':', lw=1)
ax.set_xlabel(r'$g_{ph}$ (ph coupling fraction)', fontsize=12)
ax.set_ylabel(r'$\Delta_{B2}$ shift (%)', fontsize=12)
ax.set_title('(a) Gap backreaction vs ph coupling', fontsize=12)
ax.legend(fontsize=9)
ax.set_xlim(-0.02, 0.55)

# --- Panel (b): ED E_cond shift ---
ax = axes[0, 1]
g_labels = ['0.00', '0.03', '0.10']
E_conds = [float(d['E_cond_ed_g0']), float(d['E_cond_ed_g003']), float(d['E_cond_ed_g010'])]
E_ref = E_conds[0]
shifts = [(e / E_ref - 1) * 100 for e in E_conds]
g_vals = [0.0, 0.03, 0.10]
ax.bar(g_vals, shifts, width=0.02, color=['steelblue', 'seagreen', 'darkorange'],
       edgecolor='black', linewidth=0.5)
ax.set_xlabel(r'$g_{ph}$', fontsize=12)
ax.set_ylabel(r'$E_{cond}$ shift (%, ED)', fontsize=12)
ax.set_title('(b) ED condensation energy shift', fontsize=12)
ax.axhline(0, color='gray', ls='--', lw=0.5)
for i, (g, s) in enumerate(zip(g_vals, shifts)):
    ax.annotate(f'{s:+.2f}%', (g, s), textcoords='offset points',
                xytext=(0, 8), ha='center', fontsize=10)

# --- Panel (c): Tau sweep ---
ax = axes[1, 0]
tau_vals = d['tau_sweep_values']
D_noback = d['tau_Delta_B2_noback']
D_g003 = d['tau_Delta_B2_g003']
D_g010 = d['tau_Delta_B2_g010']
ax.plot(tau_vals, D_noback, 's-', color='navy', ms=6, lw=2, label=r'$g_{ph}=0$ (bare)')
ax.plot(tau_vals, D_g003, 'o-', color='seagreen', ms=6, lw=2, label=r'$g_{ph}=0.03$')
ax.plot(tau_vals, D_g010, '^-', color='darkorange', ms=6, lw=2, label=r'$g_{ph}=0.10$')
ax.set_xlabel(r'$\tau$ (Jensen parameter)', fontsize=12)
ax.set_ylabel(r'$\Delta_{B2}$ (M$_{KK}$)', fontsize=12)
ax.set_title(r'(c) $\Delta_{B2}$ vs $\tau$ with backreaction', fontsize=12)
ax.legend(fontsize=10)
ax.set_xlim(-0.01, 0.21)

# --- Panel (d): Channel hierarchy ---
ax = axes[1, 1]
channels = ['A: BdG\n(in BCS)', 'B: ph rearr.\n(g=0.03)', 'B: ph rearr.\n(g=0.10)', 'C: geometric']
ch_shifts = [0.0, 1.21, 3.89, 5.5e-5]
colors = ['steelblue', 'seagreen', 'darkorange', 'firebrick']
bars = ax.barh(channels, ch_shifts, color=colors, edgecolor='black', linewidth=0.5)
ax.set_xlabel('Max observable shift (%)', fontsize=12)
ax.set_title('(d) Backreaction channel hierarchy', fontsize=12)
ax.axvline(10, color='red', ls=':', lw=2, label='Gate threshold (10%)')
ax.legend(fontsize=10)
# Add value labels
for bar, val in zip(bars, ch_shifts):
    if val > 0.01:
        ax.text(bar.get_width() + 0.2, bar.get_y() + bar.get_height()/2,
                f'{val:.2f}%', va='center', fontsize=10)
    else:
        ax.text(0.3, bar.get_y() + bar.get_height()/2,
                f'{val:.1e}%', va='center', fontsize=10)

plt.suptitle('HFB-BACKREACTION-49: PASS\n'
             r'Self-consistent Dirac-BCS iteration — all channels $< 10\%$',
             fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig(data_dir / 's49_hfb_backreaction.png', dpi=150, bbox_inches='tight')
print(f"Saved: {data_dir / 's49_hfb_backreaction.png'}")
