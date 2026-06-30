#!/usr/bin/env python3
"""
S70 BELL-GGE-70: CHSH Bell Inequality for GGE Relic BCS Pairs
==============================================================

Gate: BELL-GGE-70
  PASS: S > 2 for ALL 8 BCS modes (Bell violation; GGE is quantum)
  FAIL: S <= 2 for ANY mode (classical correlations sufficient)
  INFO: S > 2 but marginal (S < 2.1) for any mode

Physics
-------
The BCS ground state |BCS> = prod_k (u_k + v_k c^dag_k c^dag_{-k})|0>
has each (k,-k) pair in a two-qubit entangled state:

    |psi_k> = u_k |0_k, 0_{-k}> + v_k |1_k, 1_{-k}>

with |u_k|^2 + |v_k|^2 = 1. This is NOT a continuous-variable two-mode
squeezed vacuum. It is a FERMIONIC two-level system with Hilbert space
dimension 4 per pair. The correct CHSH analysis uses the Horodecki
criterion for pure 2-qubit states:

    S_max = 2 * sqrt(1 + C_k^2)

where C_k = 2|u_k||v_k| is the concurrence. For ANY 0 < |v_k| < 1,
C_k > 0 and S_max > 2 (Bell violation guaranteed for all paired modes).

The S69 computation used the WRONG formula: S = 2*sqrt(2)*tanh(r) from
continuous-variable homodyne measurements. That formula:
  (a) asymptotes to 2 from below (never violates Bell)
  (b) requires <n> > 1 for violation (impossible in BCS, where n in [0,1])
  (c) treats fermions as bosons (wrong statistics)

This script corrects S69 by using the proper fermionic two-qubit CHSH.

Two sources of (u_k, v_k) amplitudes:
  1. S52 BCS ground state: exact diagonalization of HFB (pre-transit state)
  2. S56 GGE diagonal ensemble: nk_DE occupation numbers (post-transit state)

The GGE relic state after the impulsive transit has BOTH entanglement
sources. We compute CHSH for both.

Correction to S69
-----------------
S69 error: used S = 2*sqrt(2)*tanh(r)/sqrt(1+tanh^2(r)) which is the
bosonic CV homodyne CHSH formula (maximal value = 2 at r -> inf, NEVER
violates Bell). The fermionic BCS pair (k,-k) is a 2-qubit system.
Horodecki 1995 gives S_max = 2*sqrt(1 + C^2) where C = concurrence.

Author: Kitaev-Quantum-Chaos-Theorist (Session 70, W1-F)
"""

import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(SCRIPT_DIR)
sys.path.insert(0, SCRIPT_DIR)

import numpy as np
from canonical_constants import (
    n_Bog, n_pairs, tau_fold, T_acoustic,
    E_B1, E_B2_mean, E_B3_mean,
    E_cond, Delta_0_GL,
)

print("=" * 72)
print("S70 BELL-GGE-70: CHSH Bell Inequality for GGE Relic BCS Pairs")
print("=" * 72)

# ======================================================================
# 1. Load Bogoliubov amplitudes from S52 (BCS ground state)
# ======================================================================

d52 = np.load('s52_bogoliubov_amp.npz', allow_pickle=True)
u_k_bcs = d52['u_k']           # (8,) BCS coherence factors
v_k_bcs = d52['v_k']           # (8,) BCS coherence factors
labels = d52['branch_labels']  # B2[0..3], B1, B3[0..2]
Delta_per = d52['Delta_per_mode']  # Gap per mode

print("\n--- S52 BCS Ground State Amplitudes ---")
print(f"{'Mode':<8} {'u_k':>8} {'v_k':>8} {'u^2+v^2':>8} {'Delta':>8}")
for i in range(8):
    print(f"{str(labels[i]):<8} {u_k_bcs[i]:8.6f} {v_k_bcs[i]:8.6f} "
          f"{u_k_bcs[i]**2 + v_k_bcs[i]**2:8.6f} {np.abs(Delta_per[i]):8.4f}")

# ======================================================================
# 2. Load GGE diagonal ensemble occupations from S56 (post-transit)
# ======================================================================

d56 = np.load('s56_gge_fabric.npz', allow_pickle=True)
nk_DE = d56['nk_DE'][:8]  # 8 distinct modes (next 8 are k,-k partners)
eps_fold = d56['eps_fold']  # single-particle energies at fold
T_k = d56['T_k_2cell'][:8]  # mode-resolved effective temperatures

print("\n--- S56 GGE Diagonal Ensemble (Post-Transit) ---")
print(f"{'Mode':<8} {'nk_DE':>8} {'eps_k':>8} {'T_eff':>10}")
for i in range(8):
    print(f"{str(labels[i]):<8} {nk_DE[i]:8.6f} {eps_fold[i]:8.4f} {T_k[i]:10.4f}")

# ======================================================================
# 3. CHSH for BCS ground state (S52 amplitudes)
#    |psi_k> = u_k|00> + v_k|11>  (pure 2-qubit state)
#    Concurrence: C_k = 2|u_k||v_k|
#    Max CHSH: S_k = 2*sqrt(1 + C_k^2)  [Horodecki 1995]
# ======================================================================

print(f"\n{'='*72}")
print("CHSH FOR BCS GROUND STATE (S52 AMPLITUDES)")
print(f"{'='*72}")
print("\nFormula: S_max = 2*sqrt(1 + C^2), C = 2|u_k||v_k| (Horodecki 1995)")
print("Bell violation: S > 2  <=>  C > 0  <=>  v_k != 0\n")

C_bcs = 2.0 * np.abs(u_k_bcs) * np.abs(v_k_bcs)
S_bcs = 2.0 * np.sqrt(1.0 + C_bcs**2)

# von Neumann entanglement entropy for |psi> = u|00> + v|11>
# S_vN = -|u|^2 log|u|^2 - |v|^2 log|v|^2
S_vN_bcs = np.zeros(8)
for i in range(8):
    p0 = u_k_bcs[i]**2
    p1 = v_k_bcs[i]**2
    if p0 > 0 and p1 > 0:
        S_vN_bcs[i] = -p0 * np.log(p0) - p1 * np.log(p1)
    else:
        S_vN_bcs[i] = 0.0

r_bcs = np.zeros(8)
for i in range(8):
    if v_k_bcs[i] > 0 and u_k_bcs[i] > 0:
        r_bcs[i] = np.arctanh(v_k_bcs[i] / u_k_bcs[i])

print(f"{'Mode':<8} {'C_k':>8} {'S_max':>8} {'S>2?':>6} {'S_vN':>8} {'r_k':>8}")
print("-" * 56)
for i in range(8):
    violation = "YES" if S_bcs[i] > 2.0 else "NO"
    print(f"{str(labels[i]):<8} {C_bcs[i]:8.6f} {S_bcs[i]:8.6f} {violation:>6} "
          f"{S_vN_bcs[i]:8.6f} {r_bcs[i]:8.6f}")

print(f"\nTotal S_vN (BCS ground state) = {np.sum(S_vN_bcs):.6f} nats")
print(f"Number of modes with S > 2: {np.sum(S_bcs > 2.0)}/8")
print(f"B1 mode: v_k = 0, Delta = 0 => NO pairing, NO entanglement, S = 2 exactly")

# ======================================================================
# 4. CHSH for GGE Diagonal Ensemble (S56 occupations)
#    Post-transit, each mode k has occupation nk_DE from the diagonal
#    ensemble. For the GGE relic, the effective pair state is:
#      |psi_k> = sqrt(1 - n_k)|0_k,0_{-k}> + sqrt(n_k)|1_k,1_{-k}>
#    This is the standard BCS form with u_k^eff = sqrt(1-n_k), v_k^eff = sqrt(n_k).
# ======================================================================

print(f"\n{'='*72}")
print("CHSH FOR GGE DIAGONAL ENSEMBLE (S56 OCCUPATIONS)")
print(f"{'='*72}")
print("\nPost-transit effective amplitudes: u_eff = sqrt(1-n_k), v_eff = sqrt(n_k)")
print("These encode the Kibble-Zurek pair creation during the fold transit.\n")

u_eff = np.sqrt(1.0 - nk_DE)
v_eff = np.sqrt(nk_DE)
C_gge = 2.0 * u_eff * v_eff
S_gge = 2.0 * np.sqrt(1.0 + C_gge**2)

# von Neumann entropy
S_vN_gge = np.zeros(8)
for i in range(8):
    p0 = 1.0 - nk_DE[i]
    p1 = nk_DE[i]
    if p0 > 0 and p1 > 0:
        S_vN_gge[i] = -p0 * np.log(p0) - p1 * np.log(p1)

r_gge = np.arctanh(v_eff / u_eff)

print(f"{'Mode':<8} {'n_k':>8} {'C_k':>8} {'S_max':>8} {'S>2?':>6} {'S_vN':>8} {'r_k':>8}")
print("-" * 64)
for i in range(8):
    violation = "YES" if S_gge[i] > 2.0 else "NO"
    print(f"{str(labels[i]):<8} {nk_DE[i]:8.6f} {C_gge[i]:8.6f} {S_gge[i]:8.6f} "
          f"{violation:>6} {S_vN_gge[i]:8.6f} {r_gge[i]:8.6f}")

S_total_gge = np.sum(S_vN_gge)
print(f"\nTotal S_vN (GGE relic) = {S_total_gge:.6f} nats")
print(f"Number of modes with S > 2: {np.sum(S_gge > 2.0)}/8")

# ======================================================================
# 5. GGE vs Thermal Comparison
#    A thermal state at temperature T has n_k = 1/(exp(E_k/T) + 1)
#    (Fermi-Dirac). The GGE has mode-dependent effective temperatures.
#    If all T_eff_k are equal, the state is thermal. Spread measures
#    deviation from thermality.
#
#    TWO temperature diagnostics:
#    (A) Using single-particle energies eps_fold (S56 T_k_2cell): this
#        resolves modes against the ACTUAL energy levels. Authoritative.
#    (B) Using BdG quasiparticle energies E_qp: these are degenerate
#        within branches, giving artificially low CV. Supplementary.
# ======================================================================

print(f"\n{'='*72}")
print("GGE vs THERMAL STATE DIAGNOSTIC")
print(f"{'='*72}")

# --- Primary: S56 mode-resolved T_k (single-particle energies) ---
T_k_s56 = d56['T_k_2cell'][:8]
beta_k_s56 = d56['beta_k_2cell'][:8]

print(f"\n(A) S56 Mode-Resolved Temperatures (single-particle energies):")
print(f"{'Mode':<8} {'eps_k':>8} {'n_k':>8} {'T_eff':>10} {'beta':>10}")
print("-" * 54)
for i in range(8):
    print(f"{str(labels[i]):<8} {eps_fold[i]:8.4f} {nk_DE[i]:8.6f} "
          f"{T_k_s56[i]:10.4f} {beta_k_s56[i]:10.4f}")

# Exclude mode 0 (eps=0 => T_eff undefined) for CV calculation
T_k_valid = T_k_s56[1:]  # modes 1-7 (eps > 0)
CV_T_s56 = np.std(T_k_valid) / np.mean(T_k_valid)
T_B2 = d56['T_B2_2cell'].item()
T_B1 = d56['T_B1_2cell'].item()
T_B3 = d56['T_B3_2cell'].item()

print(f"\n  T_B2 = {T_B2:.4f}, T_B1 = {T_B1:.4f}, T_B3 = {T_B3:.4f} M_KK")
print(f"  T_B3/T_B2 = {T_B3/T_B2:.2f} (thermal requires ratio = 1)")
print(f"  CV(T_k, modes 1-7) = {CV_T_s56:.4f} = {CV_T_s56*100:.1f}%")
print(f"  T_acoustic (canonical) = {T_acoustic:.4f} M_KK")

# --- Secondary: BdG quasiparticle energies ---
E_qp = d52['E_qp']  # quasiparticle energies from S52 BdG
T_eff_qp = np.zeros(8)
for i in range(8):
    if nk_DE[i] > 0 and nk_DE[i] < 1:
        T_eff_qp[i] = E_qp[i] / np.log((1.0 - nk_DE[i]) / nk_DE[i])

print(f"\n(B) BdG Quasiparticle Temperatures (supplementary):")
print(f"{'Mode':<8} {'E_qp':>8} {'n_k':>8} {'T_eff':>8}")
print("-" * 40)
for i in range(8):
    print(f"{str(labels[i]):<8} {E_qp[i]:8.4f} {nk_DE[i]:8.6f} {T_eff_qp[i]:8.4f}")

T_mean_qp = np.mean(T_eff_qp)
T_std_qp = np.std(T_eff_qp)
CV_T_qp = T_std_qp / T_mean_qp

print(f"\n  CV(T_eff, BdG) = {CV_T_qp:.4f} = {CV_T_qp*100:.1f}%")
print(f"  WARNING: BdG energies are degenerate within branches.")
print(f"  This deflates CV artificially. Use S56 T_k as primary diagnostic.")

# Use S56 CV as the authoritative diagnostic
CV_T = CV_T_s56
T_eff_mode = T_k_s56  # for saving and plotting

if CV_T > 0.10:
    print(f"\nVERDICT: GGE is NOT thermal (CV = {CV_T*100:.1f}% >> 10% threshold)")
    print("  Each mode has a distinct effective temperature.")
    print("  Branch hierarchy: T_B2 < T_B1 < T_B3 (4x range).")
    print("  This is the signature of the Ordered Veil (integrable dynamics).")
    thermal_verdict = "NON-THERMAL"
else:
    print(f"\nVERDICT: GGE is approximately thermal (CV = {CV_T*100:.1f}%)")
    thermal_verdict = "THERMAL"

# ======================================================================
# 6. S_vN spread across modes (per prompt spec)
# ======================================================================

print(f"\n{'='*72}")
print("ENTANGLEMENT ENTROPY SPREAD")
print(f"{'='*72}")

S_vN_mean = np.mean(S_vN_gge)
S_vN_std = np.std(S_vN_gge)
CV_SvN = S_vN_std / S_vN_mean

print(f"\nS_vN per mode: min = {np.min(S_vN_gge):.6f}, max = {np.max(S_vN_gge):.6f}")
print(f"Mean = {S_vN_mean:.6f} nats, Std = {S_vN_std:.6f} nats")
print(f"sigma(S_vN)/mean(S_vN) = {CV_SvN:.4f} = {CV_SvN*100:.1f}%")
print(f"Total entanglement entropy (sum over 8 modes) = {S_total_gge:.4f} nats")

# Per-pair total (k and -k contribute identically)
S_total_all_pairs = 2.0 * S_total_gge  # factor 2 for (k,-k) symmetry
print(f"Total including (k,-k) partners (16 half-modes) = {S_total_all_pairs:.4f} nats")
print(f"log(2) per mode = {np.log(2):.4f} nats (maximally entangled)")
print(f"Fraction of max entanglement: {S_vN_mean / np.log(2):.3f}")

# ======================================================================
# 7. Cross-check with n_Bog from canonical_constants
# ======================================================================

print(f"\n{'='*72}")
print("CROSS-CHECK: n_Bog CONSISTENCY")
print(f"{'='*72}")

# n_Bog = 0.9986 is the Bogoliubov fraction (overlap with BCS vacuum)
# This is |<BCS_post|BCS_pre>|^2, not a per-mode occupation
# Mean nk_DE ~ 0.12, consistent with near-ground-state occupation
# n_Bog ~ 1 means the transit barely excites the system (GGE near BCS ground)
print(f"\nn_Bog (canonical) = {n_Bog:.7f}")
print(f"Mean nk_DE = {np.mean(nk_DE):.7f}")
print(f"Max nk_DE = {np.max(nk_DE):.7f}")
print(f"Min nk_DE = {np.min(nk_DE):.7f}")
print(f"\nn_Bog measures |<BCS_post|BCS_pre>|^2 (Bogoliubov overlap),")
print(f"NOT individual mode occupation. n_Bog ~ 1 is consistent with")
print(f"nk_DE ~ 0.12-0.15 (low but nonzero occupation per mode).")

# ======================================================================
# 8. Comparison: S69 (wrong) vs S70 (correct)
# ======================================================================

print(f"\n{'='*72}")
print("COMPARISON: S69 (WRONG CV FORMULA) vs S70 (CORRECT 2-QUBIT)")
print(f"{'='*72}")

d69 = np.load('s69_bell_gge.npz', allow_pickle=True)
print(f"\nS69 used: S = 2*sqrt(2)*tanh(r)/sqrt(1+tanh^2(r))")
print(f"  This is the bosonic CV homodyne formula.")
print(f"  Maximum: S -> 2 as r -> inf (NEVER violates Bell).")
print(f"  S69 B2: S = {d69['S_B2'].item():.4f} (below 2)")
print(f"  S69 B3: S = {d69['S_B3'].item():.4f} (below 2)")
print(f"\nS70 uses: S_max = 2*sqrt(1 + C^2), C = 2|u||v| (Horodecki)")
print(f"  This is the correct fermionic 2-qubit formula.")
print(f"  S > 2 whenever C > 0 (any nonzero pairing).")

# ======================================================================
# 9. GATE VERDICT
# ======================================================================

print(f"\n{'='*72}")
print("GATE VERDICT: BELL-GGE-70")
print(f"{'='*72}")

# Gate criterion: S > 2 for ALL 8 BCS modes
# B1 has v_k = 0 => C = 0 => S = 2 exactly (boundary case)
# GGE occupations: all nk_DE > 0 => all S > 2

n_violations_bcs = np.sum(S_bcs > 2.0)
n_violations_gge = np.sum(S_gge > 2.0)

# The physically correct state is the GGE (post-transit)
# All 8 modes have nk_DE > 0, so ALL have S > 2
all_pass_gge = np.all(S_gge > 2.0)
min_S_gge = np.min(S_gge)
marginal = np.any((S_gge > 2.0) & (S_gge < 2.1))

# Determine gate verdict
if all_pass_gge:
    if marginal:
        verdict = "INFO"
        detail = (f"S > 2 for all 8 modes but marginal: "
                  f"min S = {min_S_gge:.6f}")
    else:
        verdict = "PASS"
        detail = (f"S > 2 for all 8 modes. "
                  f"min S = {min_S_gge:.6f}, max S = {np.max(S_gge):.6f}")
else:
    verdict = "FAIL"
    detail = (f"Only {n_violations_gge}/8 modes violate Bell. "
              f"min S = {min_S_gge:.6f}")

# B1 special case (pre-transit)
print(f"\n  BCS ground state (S52):")
print(f"    Modes with S > 2: {n_violations_bcs}/8")
print(f"    B1: S = {S_bcs[4]:.6f} (v_k = 0, Delta = 0, no pairing)")
print(f"    B1 is the UNPAIRED mode. S = 2 exactly (no violation).")
print(f"\n  GGE diagonal ensemble (S56, post-transit):")
print(f"    Modes with S > 2: {n_violations_gge}/8")
print(f"    ALL modes have nk_DE > 0 from Kibble-Zurek pair creation.")
print(f"    Even B1 acquires nonzero occupation (n = {nk_DE[4]:.6f}).")
print(f"    min S(GGE) = {min_S_gge:.6f} (mode {labels[np.argmin(S_gge)]})")
print(f"    max S(GGE) = {np.max(S_gge):.6f} (mode {labels[np.argmax(S_gge)]})")

print(f"\n  GGE thermality: {thermal_verdict} (CV = {CV_T*100:.1f}%)")
print(f"  sigma(S_vN)/mean(S_vN) = {CV_SvN*100:.1f}%")

print(f"\n  Gate BELL-GGE-70: {verdict}")
print(f"  Threshold: S > 2 for ALL 8 modes")
print(f"  Computed:  min S = {min_S_gge:.6f}")
print(f"  Detail:    {detail}")

# ======================================================================
# 10. Save results
# ======================================================================

np.savez('s70_bell_gge.npz',
    # BCS ground state (pre-transit)
    u_k_bcs=u_k_bcs,
    v_k_bcs=v_k_bcs,
    C_bcs=C_bcs,
    S_bcs=S_bcs,
    S_vN_bcs=S_vN_bcs,
    r_bcs=r_bcs,
    # GGE diagonal ensemble (post-transit)
    nk_DE=nk_DE,
    u_eff=u_eff,
    v_eff=v_eff,
    C_gge=C_gge,
    S_gge=S_gge,
    S_vN_gge=S_vN_gge,
    r_gge=r_gge,
    S_total_gge=S_total_gge,
    # Effective temperatures (S56 single-particle, primary)
    T_eff_mode=T_eff_mode,
    T_mean=np.mean(T_k_valid),
    T_std=np.std(T_k_valid),
    CV_T=CV_T,
    # Effective temperatures (BdG quasiparticle, supplementary)
    T_eff_qp=T_eff_qp,
    CV_T_qp=CV_T_qp,
    # Branch temperatures
    T_B2=T_B2,
    T_B1=T_B1,
    T_B3=T_B3,
    # Spread
    CV_SvN=CV_SvN,
    # Labels
    branch_labels=labels,
    eps_fold=eps_fold,
    E_qp=E_qp,
    # Gate
    gate_name=np.str_("BELL-GGE-70"),
    gate_verdict=np.str_(verdict),
    gate_detail=np.str_(detail),
    thermal_verdict=np.str_(thermal_verdict),
)

print(f"\nSaved: s70_bell_gge.npz")

# ======================================================================
# 11. Plot
# ======================================================================

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('BELL-GGE-70: CHSH Bell Inequality for GGE Relic',
             fontsize=14, fontweight='bold')

mode_names = [str(l) for l in labels]
x = np.arange(8)

# Panel 1: CHSH parameter
ax = axes[0, 0]
bars_bcs = ax.bar(x - 0.2, S_bcs, 0.35, label='BCS ground (S52)', color='steelblue', alpha=0.8)
bars_gge = ax.bar(x + 0.2, S_gge, 0.35, label='GGE relic (S56)', color='darkorange', alpha=0.8)
ax.axhline(y=2.0, color='red', linestyle='--', linewidth=2, label='Bell limit S=2')
ax.axhline(y=2*np.sqrt(2), color='gray', linestyle=':', linewidth=1, label='Tsirelson S=2sqrt(2)')
ax.set_xticks(x)
ax.set_xticklabels(mode_names, rotation=45)
ax.set_ylabel('S_max (CHSH)')
ax.set_title('Max CHSH Parameter per Mode')
ax.legend(fontsize=8)
ax.set_ylim(1.9, 2.9)

# Panel 2: Concurrence
ax = axes[0, 1]
ax.bar(x - 0.2, C_bcs, 0.35, label='BCS ground', color='steelblue', alpha=0.8)
ax.bar(x + 0.2, C_gge, 0.35, label='GGE relic', color='darkorange', alpha=0.8)
ax.set_xticks(x)
ax.set_xticklabels(mode_names, rotation=45)
ax.set_ylabel('Concurrence C_k')
ax.set_title('Concurrence (Entanglement Measure)')
ax.legend(fontsize=8)

# Panel 3: Entanglement entropy
ax = axes[1, 0]
ax.bar(x - 0.2, S_vN_bcs, 0.35, label='BCS ground', color='steelblue', alpha=0.8)
ax.bar(x + 0.2, S_vN_gge, 0.35, label='GGE relic', color='darkorange', alpha=0.8)
ax.axhline(y=np.log(2), color='gray', linestyle=':', linewidth=1, label='max = ln(2)')
ax.set_xticks(x)
ax.set_xticklabels(mode_names, rotation=45)
ax.set_ylabel('S_vN (nats)')
ax.set_title('von Neumann Entanglement Entropy per Mode')
ax.legend(fontsize=8)

# Panel 4: Effective temperature (S56, skip mode 0 anomaly in mean)
ax = axes[1, 1]
colors_T = ['gray'] + ['firebrick']*7  # gray for eps=0 mode
ax.bar(x, T_eff_mode, color=colors_T, alpha=0.8)
ax.axhline(y=T_acoustic, color='green', linestyle='--', linewidth=2,
           label=f'T_acoustic = {T_acoustic:.3f}')
ax.axhline(y=np.mean(T_k_valid), color='blue', linestyle=':', linewidth=2,
           label=f'T_mean(1-7) = {np.mean(T_k_valid):.3f}')
ax.set_xticks(x)
ax.set_xticklabels(mode_names, rotation=45)
ax.set_ylabel('T_eff (M_KK)')
ax.set_title(f'S56 Effective T per Mode (CV = {CV_T*100:.1f}%)')
ax.legend(fontsize=8)
ax.text(0, T_eff_mode[0] - 0.08, 'eps=0\n(anomalous)', ha='center', fontsize=6, color='gray')

plt.tight_layout()
plt.savefig('s70_bell_gge.png', dpi=150)
print("Saved: s70_bell_gge.png")

print(f"\n{'='*72}")
print(f"DONE. Gate BELL-GGE-70: {verdict}")
print(f"{'='*72}")
