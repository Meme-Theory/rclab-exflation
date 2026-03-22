#!/usr/bin/env python3
"""
s47_ratio_correct.py -- RATIO-CORRECT-47
Corrects the S46 ratio of 2.19x (131/59.8) by constructing sector-matched
ratios where numerator and denominator come from the SAME sector.

The problem with S46's ratio:
  - Numerator 131 = ALL PW-weighted pi-phases including B1 (15) and B3 (35)
  - Denominator 59.8 = ALL quasiparticle pairs from 992-mode sudden quench
  - These are apples and oranges: B1 has V(B1,B1)=0 (Trap 1) so its 15
    pi-phase channels are topologically available but dynamically inert

Key methodological issue: how to decompose 59.8 pairs into sectors.
  - Method A (8-mode ED fractions): WRONG. The ED populates B1 at 49.4%
    through V(B1,B2) cross-channel entanglement. These are NOT BCS pairs.
  - Method B (BCS v2 fractions): CORRECT. The v2 per sector reflects the
    actual BCS pairing amplitude. B2 carries 90.7% of BCS weight.
  - Method C (v2 * absolute mode count): overshoots total (66.8 vs 59.8)
    because 8-mode v2 doesn't transfer to 992 modes with different DOS.

Selected: Method B -- use BCS v2 FRACTIONS applied to the known 59.8 total.
"""

import numpy as np
import os

# === Load all data ===
base = os.path.dirname(os.path.abspath(__file__))
s46_bcs = np.load(os.path.join(base, 's46_number_projected_bcs.npz'), allow_pickle=True)
s46_rg = np.load(os.path.join(base, 's46_rg_pair_transfer.npz'), allow_pickle=True)
s38_cc = np.load(os.path.join(base, 's38_cc_instanton.npz'), allow_pickle=True)
s44_dos = np.load(os.path.join(base, 's44_dos_tau.npz'), allow_pickle=True)
s47_pi = np.load(os.path.join(base, 's47_pi_sector.npz'), allow_pickle=True)
s47_k7 = np.load(os.path.join(base, 's47_k7_filter.npz'), allow_pickle=True)

print("=" * 72)
print("RATIO-CORRECT-47: Sector-Matched BCS Pi-Phase Ratio")
print("=" * 72)

# =====================================================================
# STEP 1: 8-mode ED pair count by sector (for comparison only)
# =====================================================================
print("\n--- STEP 1: 8-mode ED pair count by sector ---\n")

n_occ = s46_rg['n_occ']
mode_sector = s46_rg['mode_sector']
mult_k = s38_cc['mult_k']  # [1, 4, 3]

n_pairs_8_B1 = n_occ[0]
n_pairs_8_B2 = np.sum(n_occ[1:5])
n_pairs_8_B3 = np.sum(n_occ[5:8])
n_pairs_8_total = n_pairs_8_B1 + n_pairs_8_B2 + n_pairs_8_B3

print(f"  N_pairs_ED(B1) = {n_pairs_8_B1:.6f}  ({n_pairs_8_B1/n_pairs_8_total*100:.1f}%)")
print(f"  N_pairs_ED(B2) = {n_pairs_8_B2:.6f}  ({n_pairs_8_B2/n_pairs_8_total*100:.1f}%)")
print(f"  N_pairs_ED(B3) = {n_pairs_8_B3:.6f}  ({n_pairs_8_B3/n_pairs_8_total*100:.1f}%)")
print(f"  Total          = {n_pairs_8_total:.15f}")
print(f"  WARNING: B1 at 49.4% despite V(B1,B1)=0. Cross-channel artifact.")

# =====================================================================
# STEP 2: BCS v2 sector fractions -- the correct decomposition
# =====================================================================
print("\n--- STEP 2: BCS v2 sector fractions ---\n")

v2_bcs = s46_bcs['v2_bcs']  # [0.0446, 0.1220, 0.0019] per mode
# mult_k = [1, 4, 3] modes per sector in the 8-mode model
# v2*mult gives the BCS pair weight per sector

v2_weighted = v2_bcs * mult_k  # [0.045, 0.488, 0.006]
v2_total = np.sum(v2_weighted)

frac_v2_B1 = v2_weighted[0] / v2_total
frac_v2_B2 = v2_weighted[1] / v2_total
frac_v2_B3 = v2_weighted[2] / v2_total

print(f"  v2_bcs per mode: B1={v2_bcs[0]:.5f}, B2={v2_bcs[1]:.5f}, B3={v2_bcs[2]:.5f}")
print(f"  Multiplicities:  B1={mult_k[0]}, B2={mult_k[1]}, B3={mult_k[2]}")
print(f"  v2*mult:         B1={v2_weighted[0]:.5f}, B2={v2_weighted[1]:.5f}, B3={v2_weighted[2]:.5f}")
print(f"  Total v2*mult:   {v2_total:.5f}")
print(f"")
print(f"  BCS pair fractions:")
print(f"    f_BCS(B1) = {frac_v2_B1:.4f}  ({frac_v2_B1*100:.1f}%)")
print(f"    f_BCS(B2) = {frac_v2_B2:.4f}  ({frac_v2_B2*100:.1f}%)")
print(f"    f_BCS(B3) = {frac_v2_B3:.4f}  ({frac_v2_B3*100:.1f}%)")
print(f"")
print(f"  WHY BCS fractions, not ED fractions:")
print(f"    ED gives B1 = 49.4% because V(B1,B2) = 0.130 creates cross-channel")
print(f"    entanglement. But V(B1,B1) = 0 EXACTLY (Trap 1, S34). B1 has zero")
print(f"    BCS self-pairing. The ED B1 occupation is entanglement, not pairing.")
print(f"    BCS v2 correctly attributes pairing: B2 carries {frac_v2_B2*100:.1f}%.")

# Decompose 59.8 total pairs into sectors using BCS fractions
N_total = 59.8  # S38 sudden quench
N_B1 = frac_v2_B1 * N_total
N_B2 = frac_v2_B2 * N_total
N_B3 = frac_v2_B3 * N_total

print(f"\n  992-mode pair decomposition (BCS fractions x 59.8):")
print(f"    N_pairs(B1) = {N_B1:.2f}")
print(f"    N_pairs(B2) = {N_B2:.2f}")
print(f"    N_pairs(B3) = {N_B3:.2f}")
print(f"    Total       = {N_B1 + N_B2 + N_B3:.2f}")

# =====================================================================
# STEP 3: Pi-phase counts (from W1-1 and W1-2)
# =====================================================================
print("\n--- STEP 3: Pi-phase counts ---\n")

pw_pi_B1 = int(s47_pi['pw_pi_B1'])   # 15
pw_pi_B2 = int(s47_pi['pw_pi_B2'])   # 81
pw_pi_B3 = int(s47_pi['pw_pi_B3'])   # 35
pw_pi_total = pw_pi_B1 + pw_pi_B2 + pw_pi_B3  # 131

pw_acc_cons = int(s47_k7['pw_accessible_conservative'])  # 81
pw_acc_mod  = int(s47_k7['pw_accessible_moderate'])      # 116

print(f"  PW-weighted pi-phases:")
print(f"    B1: {pw_pi_B1}  INERT (Trap 1: V(B1,B1) = 0)")
print(f"    B2: {pw_pi_B2}  ACTIVE (V(B2,B2) = 0.256)")
print(f"    B3: {pw_pi_B3}  MARGINAL (V(B3,B3) = 0.003)")
print(f"    Total: {pw_pi_total}")
print(f"  K7-filtered:")
print(f"    Conservative (B2 only): {pw_acc_cons}")
print(f"    Moderate (B2 + B3):     {pw_acc_mod}")

# =====================================================================
# STEP 4: Construct the ratio table
# =====================================================================
print("\n--- STEP 4: Ratio table ---\n")

R_raw = pw_pi_total / N_total
R_B2_only = pw_pi_B2 / N_B2
R_B2_B3 = pw_acc_mod / (N_B2 + N_B3)

# Cross-check with ED-fraction decomposition (Method A -- for comparison)
N_B2_edA = n_pairs_8_B2 / n_pairs_8_total * N_total
R_B2_edA = pw_pi_B2 / N_B2_edA

print(f"  {'Label':<30s} {'Numerator':>12s} {'Denominator':>14s} {'Ratio':>8s}  Base")
print(f"  {'-'*30} {'-'*12} {'-'*14} {'-'*8}  {'-'*40}")
print(f"  {'R_raw (S46)':<30s} {pw_pi_total:>12d} {N_total:>14.2f} {R_raw:>8.3f}  All sectors, mismatched")
print(f"  {'R_B2 (BCS fractions)':<30s} {pw_pi_B2:>12d} {N_B2:>14.2f} {R_B2_only:>8.3f}  B2-only, sector-matched")
print(f"  {'R_B2+B3 (moderate)':<30s} {pw_acc_mod:>12d} {N_B2+N_B3:>14.2f} {R_B2_B3:>8.3f}  Active sectors")
print(f"  {'R_B2 (ED fractions)':<30s} {pw_pi_B2:>12d} {N_B2_edA:>14.2f} {R_B2_edA:>8.3f}  WRONG: ED inflates B1")

print(f"\n  The BCS-fraction ratio R_B2 = {R_B2_only:.3f} is the primary result.")
print(f"  It says: {R_B2_only:.1f} topological channels (pi-phases) per Cooper pair in B2.")

# =====================================================================
# STEP 5: Interpretation
# =====================================================================
print("\n--- STEP 5: Interpretation ---\n")

if 0.5 <= R_B2_only <= 2.0:
    interp = "RESOLVED"
    interp_detail = (
        f"R_B2 = {R_B2_only:.3f} is within a factor of 2 of unity. "
        f"The S46 discrepancy (2.19x) was base-mixing, not a structural excess."
    )
elif R_B2_only > 2.0:
    interp = "REDUCED but not unity"
    interp_detail = (
        f"R_B2 = {R_B2_only:.3f} > 2. Sector matching reduced the discrepancy "
        f"from 2.19x to {R_B2_only:.2f}x (a {(1 - R_B2_only/R_raw)*100:.0f}% reduction), "
        f"but a moderate topological excess persists within B2."
    )
else:
    interp = "INVERTED"
    interp_detail = (
        f"R_B2 = {R_B2_only:.3f} < 0.5. More pairs than topology predicts. "
        f"Non-topological pairing dominates."
    )

print(f"  Status: {interp}")
print(f"  {interp_detail}")

print(f"\n  Decomposition of the correction:")
print(f"    Numerator:   131 -> 81   (factor {81/131:.3f}, removing B1 inert + B3 marginal)")
print(f"    Denominator: 59.8 -> {N_B2:.2f} (factor {N_B2/59.8:.3f}, BCS fraction)")
print(f"    Net ratio:   {R_raw:.3f} -> {R_B2_only:.3f} (factor {R_B2_only/R_raw:.3f})")
print(f"")
print(f"    The numerator shrinks by {(1-81/131)*100:.0f}% (removing 50 inert/marginal channels).")
print(f"    The denominator shrinks by {(1-N_B2/59.8)*100:.0f}% (B2 carries {frac_v2_B2*100:.0f}% of BCS weight).")
print(f"    The numerator shrinks MORE than the denominator because B1 contributes")
print(f"    11.5% of pi-phases but only {frac_v2_B1*100:.1f}% of BCS pairs.")

# =====================================================================
# STEP 6: B1 occupation paradox
# =====================================================================
print("\n--- STEP 6: B1 occupation paradox ---\n")

V_mat = s46_bcs['V_mat_constrained']
V_full = s46_rg['V_full']
Delta_bcs = s46_bcs['Delta_bcs_fold']

print(f"  In the 8-mode ED ground state (N=1 pair):")
print(f"    B1 occupation:  {n_pairs_8_B1:.4f} (49.4%)")
print(f"    B2 occupation:  {n_pairs_8_B2:.4f} (49.2%)")
print(f"    B3 occupation:  {n_pairs_8_B3:.4f} (1.4%)")
print(f"")
print(f"  But V(B1,B1) = 0 EXACTLY (Trap 1, S34, U(2) Schur lemma).")
print(f"  B1 cannot self-pair. So where do the 0.494 B1 pairs come from?")
print(f"")
print(f"  Answer: Cross-channel entanglement through V(B1,B2) = {V_mat[0,1]:.3f}.")
print(f"")
print("  The ED Hamiltonian H = sum_k eps_k n_k - sum_{kl} V_{kl} c+_k c+_k c_l c_l")
print("  includes off-diagonal V(B1,B2) = 0.130, which entangles B1 and B2 modes.")
print(f"  In the ground state, the B1 mode participates in the correlated pair")
print(f"  wavefunction |psi> = -0.307|B1> - 0.474|B2>_1 - 0.474|B2>_2 - ...")
print(f"  The B1 amplitude is large because V(B1,B2) is 50.8% of V(B2,B2).")
print(f"")
print(f"  This means the ED occupation of B1 is NOT an independent BCS pair.")
print(f"  It is entanglement leakage. In a true BCS (mean-field) treatment,")
print(f"  B1 has v2 = {v2_bcs[0]:.4f} per mode -- just 8.3% of total pairing.")
print(f"  Even this nonzero v2 arises from the PROXIMITY effect: Delta(B1) = {Delta_bcs[0]:.3f}")
print(f"  is induced entirely by V(B1,B2) coupling to the B2 condensate.")
print(f"")
print(f"  The BCS gap hierarchy confirms this picture:")
print(f"    Delta(B1) = {Delta_bcs[0]:.4f}  (proximity-induced)")
print(f"    Delta(B2) = {Delta_bcs[1]:.4f}  (self-pairing, dominant)")
print(f"    Delta(B3) = {Delta_bcs[2]:.4f}  (proximity from V(B2,B3))")

# =====================================================================
# STEP 7: S46 correction notice
# =====================================================================
print("\n--- STEP 7: S46 correction notice ---\n")

print(f"  RETRACTED:")
print(f"    The number 2.19x (131 pi-phases / 59.8 pairs) RETRACTS.")
print(f"    Error: base-mixing. Numerator includes B1 (15 PW, inert by Trap 1)")
print(f"    and B3 (35 PW, marginal V(B3,B3) = 76x weaker than V(B2,B2)).")
print(f"    Denominator includes ~{N_B1:.0f} B1 pairs that are cross-channel entanglement,")
print(f"    not BCS pairing. The ratio mixes a sector where topology is present but")
print(f"    dynamics are zero (B1) with pairs that exist dynamically but are not BCS (B1 ED).")
print(f"")
print(f"    The specific error: S46 divided a topological count (pi-phase multiplicity)")
print(f"    by a dynamical count (quasiparticle pairs) without restricting both to the")
print(f"    same dynamically active sector.")
print(f"")
print(f"  CORRECTED VALUE:")
print(f"    R_B2 = {pw_pi_B2} / {N_B2:.2f} = {R_B2_only:.3f}")
print(f"    (sector-matched B2-only, using BCS v2 fractions to decompose 59.8)")
print(f"")
print(f"  SURVIVES:")
print(f"    - 131 PW-weighted pi-phases total (topological fact, verified W1-1)")
print(f"    - 59.8 total quasiparticle pairs (S38 sudden quench)")
print(f"    - Sector-resolved V matrix: V(B1,B1)=0, V(B2,B2)=0.256, V(B3,B3)=0.003")
print(f"    - v2_bcs = [{v2_bcs[0]:.4f}, {v2_bcs[1]:.4f}, {v2_bcs[2]:.4f}]")
print(f"    - BCS gap hierarchy: Delta = [{Delta_bcs[0]:.3f}, {Delta_bcs[1]:.3f}, {Delta_bcs[2]:.3f}]")
print(f"    - B2 dominates both topology (81/131 = 62%) and dynamics (v2_B2*4 = 91%)")

# =====================================================================
# GATE VERDICT
# =====================================================================
print("\n" + "=" * 72)
print("GATE VERDICT: RATIO-CORRECT-47")
print("=" * 72)

# The gate: PASS if R_B2_only is computable and finite.
# INFO if within factor 2 of unity.
# ESCALATE if > 5 or < 0.1.
verdict = "PASS"
if R_B2_only > 5 or R_B2_only < 0.1:
    verdict = "ESCALATE"

if 0.5 <= R_B2_only <= 2.0:
    info_tag = "INFO: R ~ 1. S46 discrepancy RESOLVED as base-mixing."
else:
    info_tag = f"INFO: R = {R_B2_only:.2f}, not within factor 2 of unity."

detail = (
    f"R_B2 = {R_B2_only:.3f} (81 B2 pi-phases / {N_B2:.2f} B2 BCS pairs). "
    f"S46 raw was 2.19. Correction: {(1 - R_B2_only/R_raw)*100:.0f}% reduction. "
    f"Base-mixing error identified: B1 inert channels in numerator, "
    f"B1 cross-channel entanglement in denominator."
)

print(f"  Verdict: {verdict}")
print(f"  R_B2_only = {R_B2_only:.4f}")
print(f"  {info_tag}")
print(f"  {detail}")
print()

# =====================================================================
# SAVE
# =====================================================================
np.savez(os.path.join(base, 's47_ratio_correct.npz'),
    # Gate metadata
    gate_name='RATIO-CORRECT-47',
    gate_verdict=verdict,
    gate_detail=detail,

    # S46 raw
    R_raw_s46=R_raw,
    pw_pi_total=pw_pi_total,
    N_pairs_992_total=N_total,

    # BCS v2 sector fractions (primary method)
    v2_bcs=v2_bcs,
    v2_weighted=v2_weighted,
    v2_total=v2_total,
    frac_v2_B1=frac_v2_B1,
    frac_v2_B2=frac_v2_B2,
    frac_v2_B3=frac_v2_B3,

    # 992-mode sector decomposition
    N_pairs_B1=N_B1,
    N_pairs_B2=N_B2,
    N_pairs_B3=N_B3,

    # 8-mode ED comparison (not used for ratio, for reference)
    n_pairs_8_B1=n_pairs_8_B1,
    n_pairs_8_B2=n_pairs_8_B2,
    n_pairs_8_B3=n_pairs_8_B3,

    # Pi-phase counts
    pw_pi_B1=pw_pi_B1,
    pw_pi_B2=pw_pi_B2,
    pw_pi_B3=pw_pi_B3,
    pw_acc_conservative=pw_acc_cons,
    pw_acc_moderate=pw_acc_mod,

    # Corrected ratios
    R_B2_only=R_B2_only,
    R_B2_B3=R_B2_B3,
    R_B2_edA=R_B2_edA,

    # V matrix and gaps
    V_mat_constrained=V_mat,
    Delta_bcs_fold=Delta_bcs,

    # B1 paradox
    B1_occupation_ED=n_pairs_8_B1,
    B1_occupation_BCS=v2_bcs[0] * mult_k[0],
    B1_self_V_exact=0.0,
    B1_cross_V=V_mat[0, 1],

    # Mode counts
    N_modes_B1=124,
    N_modes_B2=496,
    N_modes_B3=372,

    # Interpretation
    interpretation=interp,
)

print(f"Data saved: tier0-computation/s47_ratio_correct.npz")
print("Done.")
