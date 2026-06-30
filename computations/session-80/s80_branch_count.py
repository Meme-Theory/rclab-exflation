#!/usr/bin/env python3
"""
S80 W0-15: Rank-Universality 5-vs-7 Branch-Count Pre-Audit
===========================================================

Gate: S80-PHONONIC-LENGTH-OFF-BY-2-BRANCH-COUNT [VERIFY]

Purpose: Resolve off-by-2 gap between
  - Rank-universality prediction (P4-A): 7 branches for SU(3)
  - Task-spec canonical count:            5 branches {c_Gold, c_BLV, c_BA, c_L, c_mod}
  - Actual s52_gl_josephson data:         ??? (to be determined)

Substrate framing: Phononic eigenvalue branches of the SU(3) fiber
spectrum. Each branch is a distinct excitation mode (relay pattern)
of the fiber's Dirac-connection operator at the fold epoch.

Method:
  1. Verify rank-universality derivation: (N^2-1) - 2(N-1) + (N-1) + 1 = 7 for N=3.
  2. Load s52_gl_josephson.npz; count branches.
  3. Classify each branch by dispersion (acoustic / massive / phase-mode).
  4. Emit verdict Scenario A (=7), Scenario B (=5 with PRU closure), INFO (=6), or FAIL.
"""

import sys
import os
import numpy as np
import matplotlib.pyplot as plt

# Canonical constants import (per computations/_shared/CLAUDE.md)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import *  # noqa: F401, F403


# =============================================================================
# STEP 1: Rank-universality substitution chain (MANDATORY [VERIFY])
# =============================================================================
# Definition of each term in P4-A rank-universality formula for SU(N):
#   (N^2 - 1):  dim(su(N))                   — total generators of the Lie algebra
#   2*(N-1):    Goldstones removed           — 2 per broken generator from Higgs-like gauging
#   (N-1):      moduli from Cartan subalgebra — rank(SU(N)) = N-1
#   1:          residual U(1) photon
# Substitution for N=3:
#   predicted = 8 - 4 + 2 + 1 = 7
# Algebraic simplification:
#   = N^2 - 1 - 2N + 2 + N - 1 + 1 = N^2 - N + 1 = 9 - 3 + 1 = 7
# Direction: if |actual - 7| = 0 -> PASS Scenario A

N_rank = 3                                # (local) SU(3) rank
total_gens = N_rank**2 - 1                # (local) dim(su(3)) = 8
goldstones_removed = 2 * (N_rank - 1)     # (local) Higgs-eaten Goldstones = 4
moduli_count = N_rank - 1                 # (local) Cartan moduli = 2
photon_count = 1                          # (local) residual U(1)
predicted_branches = total_gens - goldstones_removed + moduli_count + photon_count  # (local)

# Algebraic check (independent route)
predicted_alg = N_rank**2 - N_rank + 1    # (local) should equal predicted_branches

print("=" * 70)
print("S80 W0-15: RANK-UNIVERSALITY BRANCH-COUNT PRE-AUDIT")
print("=" * 70)
print("\n[STEP 1] Rank-universality substitution chain (MANDATORY [VERIFY])")
print(f"  N (SU(N))              = {N_rank}")
print(f"  dim(su(N)) = N^2 - 1   = {total_gens}")
print(f"  Goldstones eaten       = 2*(N-1) = {goldstones_removed}")
print(f"  Moduli (rank)          = N - 1   = {moduli_count}")
print(f"  Photon                 = {photon_count}")
print(f"  Predicted = {total_gens} - {goldstones_removed} + {moduli_count} + {photon_count} = {predicted_branches}")
print(f"  Algebraic (N^2-N+1)    = {predicted_alg}")
assert predicted_branches == predicted_alg == 7, "RANK-UNIVERSALITY DERIVATION FAILURE"
print("  PASS: Rank-universality predicts EXACTLY 7 branches for SU(3)")

# =============================================================================
# STEP 2: Load S52 GL-Josephson data — actual branch count
# =============================================================================

npz_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "s52_gl_josephson.npz")
d = np.load(npz_path, allow_pickle=True)

K_array = d['K_array']                    # (local) quasi-momentum grid
K_BZ = float(d['K_BZ'])                   # (local) BZ radius
omega_branches = d['omega_branches']      # (local) shape (N_K, n_branches)
omega_sq = d['omega_sq']                  # (local) omega^2 to preserve sign
branch_labels = [str(x) for x in d['branch_labels']]  # (local) branch names
alpha_eff = d['alpha_eff']                # (local) dispersion exponent per branch
c_eff = d['c_eff']                        # (local) effective sound speed per branch
amp_frac_K0 = d['amp_frac_K0']            # (local) amplitude-sector weight at K=0
n_branches_s52 = omega_branches.shape[1]  # (local) ACTUAL count from data

print(f"\n[STEP 2] S52 GL-Josephson branch enumeration")
print(f"  npz path:          {os.path.basename(npz_path)}")
print(f"  omega_branches     shape = {omega_branches.shape}")
print(f"  N_K (K-grid points)      = {len(K_array)}")
print(f"  K_BZ (BZ radius)         = {K_BZ:.6f}")
print(f"  n_branches (ACTUAL)      = {n_branches_s52}")
print(f"  branch labels            = {branch_labels}")

# =============================================================================
# STEP 3: Classify each branch by dispersion signature
# =============================================================================
# Acoustic  : alpha ~ 1,   omega(K=0) ~ 0
# Massive   : alpha ~ 2,   omega(K=0) > 0 with sqrt(m^2 + c^2 K^2) shape
# Phase-mode: any alpha,   nearly flat in K (small c_eff relative to omega_0)
# Anomalous : alpha outside [0.7, 2.3] or strong amplitude mixing

def classify_branch(label, alpha, c, amp_K0, omega_0):
    """Classify one branch by dispersion + K=0 gap + amplitude mixing."""
    # (local) heuristic boundaries
    alpha_low = 0.7   # (local) below = sub-acoustic anomaly
    alpha_high = 2.3  # (local) above = super-massive anomaly
    flat_c = 0.1      # (local) |c| below = nearly flat phase-mode
    gapped_eps = 1e-4  # (local) omega_0 above = massive/gapped
    if abs(alpha - 1.0) < 0.3 and omega_0 < gapped_eps:
        return "acoustic"
    if abs(alpha - 2.0) < 0.3 and omega_0 > gapped_eps:
        return "massive"
    if abs(c) < flat_c and omega_0 > gapped_eps:
        return "phase-mode-flat"
    if alpha < alpha_low or alpha > alpha_high:
        return "anomalous"
    # (local) fallback — check K=0 gap
    if omega_0 < gapped_eps:
        return "acoustic-like"
    return "massive-like"


print(f"\n[STEP 3] Branch classification by dispersion")
header = f"  {'branch':<12} {'alpha':<8} {'c_eff':<12} {'amp_K0':<10} {'omega_0':<12} {'class':<18}"
print(header)
print("  " + "-" * (len(header) - 2))
classifications = []  # (local)
for i, lab in enumerate(branch_labels):
    omega_0 = float(np.abs(omega_branches[0, i]))                     # (local)
    cls = classify_branch(lab, float(alpha_eff[i]), float(c_eff[i]),
                          float(amp_frac_K0[i]), omega_0)
    classifications.append(cls)
    print(f"  {lab:<12} {alpha_eff[i]:<8.4f} {c_eff[i]:<12.4e} "
          f"{amp_frac_K0[i]:<10.4f} {omega_0:<12.4e} {cls:<18}")

# =============================================================================
# STEP 4: Cross-reference task-spec canonical-5 names
# =============================================================================
# Task spec claimed 5 canonical branches: c_Gold, c_BLV, c_BA, c_L, c_mod
# MCP query (in agent memory): only c_Gold is in canonical_constants; the
# other four are hypothetical labels from the rank-universality synthesis.

claimed_canonical_5 = ["c_Gold", "c_BLV", "c_BA", "c_L", "c_mod"]   # (local)
s52_label_map = {                                                    # (local)
    "Goldstone":  "c_Gold",   # canonical_constants.py has c_Gold
    "Leggett-1":  "c_L1",     # not yet canonical — S70 Leggett vacuum identifies this
    "Leggett-2":  "c_L2",     # not yet canonical
    "Branch-3":   "c_B3",     # not yet canonical — anomalous alpha=3.16
    "Branch-4":   "c_B4",     # not yet canonical
    "Higgs-1":    "c_H1",     # massive amplitude mode
}
print(f"\n[STEP 4] Cross-reference to claimed canonical-5 {claimed_canonical_5}")
for lab in branch_labels:
    print(f"  {lab:<12} -> {s52_label_map.get(lab, 'UNMAPPED')}")

# =============================================================================
# STEP 5: Gate decision
# =============================================================================
actual_count = n_branches_s52                                         # (local)
predicted_count = predicted_branches                                  # (local) = 7
claimed_count = len(claimed_canonical_5)                              # (local) = 5

print(f"\n[STEP 5] Gate decision")
print(f"  Actual branches in s52     = {actual_count}")
print(f"  Rank-universality prediction = {predicted_count}")
print(f"  Task-spec canonical claim  = {claimed_count}")
print(f"  |actual - 7|               = {abs(actual_count - 7)}")
print(f"  |actual - 5|               = {abs(actual_count - 5)}")

# Direction logic:
#   actual == 7 -> PASS Scenario A
#   actual == 5 with PRU adjustment -> PASS Scenario B
#   actual == 6 -> INFO (transitional)
#   else -> FAIL
scenario = None                                                        # (local)
verdict = None                                                         # (local)
explanation = ""                                                       # (local)

if actual_count == 7:
    scenario = "A"
    verdict = "PASS"
    explanation = ("Exactly 7 branches found; matches rank-universality "
                   "prediction. Add 2 more canonical entries to W0-14.")
elif actual_count == 5:
    # Scenario B requires framework-specific constraint reducing 7 -> 5
    #   e.g., R-protection removes 2 Goldstones; needs separate proof.
    scenario = "B-candidate"
    verdict = "PASS" if False else "INFO"  # (local) requires PRU proof
    explanation = ("5 branches found but PRU closure requires independent "
                   "R-protection proof; mark INFO pending justification.")
elif actual_count == 6:
    scenario = "INFO-6"
    verdict = "INFO"
    explanation = ("Exactly 6 branches in s52 — between canonical claim (5) "
                   "and rank-universality prediction (7). Transitional count: "
                   "one Goldstone + two Leggett + two anomalous + one Higgs amp. "
                   "Off-by-1 from both anchors. Do NOT proceed with W0-14 "
                   "canonicalization until branch taxonomy is reconciled.")
else:
    scenario = "FAIL"
    verdict = "FAIL"
    explanation = (f"Branch count {actual_count} is neither 5, 6, nor 7. "
                   "Structural inconsistency; escalate before W0-14.")

print(f"\n  Scenario label: {scenario}")
print(f"  Verdict:        {verdict}")
print(f"  Explanation:    {explanation}")

# =============================================================================
# STEP 6: Plot dispersion — all branches
# =============================================================================

fig, axs = plt.subplots(1, 2, figsize=(13, 6))

# Left panel: omega vs K (full branches)
ax0 = axs[0]
colors = plt.cm.viridis(np.linspace(0, 0.92, n_branches_s52))      # (local)
for i, lab in enumerate(branch_labels):
    omega = np.sign(omega_sq[:, i]) * np.sqrt(np.abs(omega_sq[:, i]))  # (local)
    ax0.plot(K_array, omega, color=colors[i],
             label=f"{lab} (alpha={alpha_eff[i]:.2f}, {classifications[i]})",
             linewidth=1.8)
ax0.set_xlabel("K / (2 pi / a_BCC)", fontsize=11)
ax0.set_ylabel("omega [M_KK units]", fontsize=11)
ax0.set_title(f"S80 W0-15: S52 GL-Josephson dispersion ({n_branches_s52} branches)",
              fontsize=11)
ax0.legend(loc='upper left', fontsize=8)
ax0.grid(True, alpha=0.3)
ax0.axvline(K_BZ, linestyle='--', color='k', alpha=0.5, linewidth=0.8)

# Right panel: alpha_eff vs branch index + count comparison
ax1 = axs[1]
idx = np.arange(n_branches_s52)                                    # (local)
bars = ax1.bar(idx, alpha_eff, color=colors, edgecolor='black')
ax1.axhline(1.0, linestyle='--', color='green', alpha=0.5, label='acoustic (alpha=1)')
ax1.axhline(2.0, linestyle='--', color='red', alpha=0.5, label='massive (alpha=2)')
ax1.set_xticks(idx)
ax1.set_xticklabels(branch_labels, rotation=30, ha='right', fontsize=9)
ax1.set_ylabel("alpha_eff (dispersion exponent)", fontsize=11)
ax1.set_title(f"Branch count: s52={n_branches_s52} | rank-univ=7 | canonical claim=5",
              fontsize=11)
ax1.legend(loc='upper right', fontsize=9)
ax1.grid(True, axis='y', alpha=0.3)

# Annotate verdict
fig.suptitle(f"S80-PHONONIC-LENGTH-OFF-BY-2-BRANCH-COUNT  |  "
             f"Scenario: {scenario}  |  Verdict: {verdict}",
             fontsize=12, y=1.00)

plt.tight_layout()
png_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "s80_branch_count.png")
plt.savefig(png_path, dpi=135, bbox_inches='tight')
plt.close(fig)
print(f"\n  Plot saved: {os.path.basename(png_path)}")

# =============================================================================
# STEP 7: Save npz + append verdict to gate-verdicts
# =============================================================================

out_npz = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "s80_branch_count.npz")
np.savez(
    out_npz,
    N_rank=N_rank,
    predicted_branches=predicted_branches,
    actual_count=actual_count,
    claimed_count=claimed_count,
    branch_labels=np.array(branch_labels),
    classifications=np.array(classifications),
    alpha_eff=alpha_eff,
    c_eff=c_eff,
    amp_frac_K0=amp_frac_K0,
    omega_0=np.abs(omega_branches[0]),
    scenario=np.array([scenario]),
    verdict=np.array([verdict]),
    explanation=np.array([explanation]),
    gate_name=np.array(["S80-PHONONIC-LENGTH-OFF-BY-2-BRANCH-COUNT"]),
)
print(f"  Data saved: {os.path.basename(out_npz)}")

# Append verdict to s80_gate_verdicts.txt
verdicts_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             "s80_gate_verdicts.txt")
verdict_line = (
    f"Gate S80-PHONONIC-LENGTH-OFF-BY-2-BRANCH-COUNT (W0-15): {verdict}\n"
    f"  Scenario:    {scenario}\n"
    f"  Threshold:   actual_count == 7 (Sc.A) | == 5 with PRU (Sc.B) | == 6 (INFO)\n"
    f"  Computed:    actual={actual_count}, predicted={predicted_branches}, "
    f"claimed={claimed_count}\n"
    f"  Verdict:     {verdict} — {explanation}\n"
    f"  Agent:       phonon-first-cosmologist (S80 W0-15)\n"
    f"  Script:      s80_branch_count.py\n\n"
)
with open(verdicts_path, "a", encoding="utf-8") as f:
    f.write(verdict_line)
print(f"  Verdict appended: {os.path.basename(verdicts_path)}")

print("\n" + "=" * 70)
print(f"FINAL: Gate S80-PHONONIC-LENGTH-OFF-BY-2-BRANCH-COUNT = {verdict} "
      f"(Scenario {scenario})")
print("=" * 70)
