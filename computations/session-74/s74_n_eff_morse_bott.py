#!/usr/bin/env python3
"""
s74_n_eff_morse_bott.py -- N-EFF-MORSE-BOTT-74
==================================================================================
Gate: N-EFF-MORSE-BOTT-74
  PASS: mapped N_eff in [2.8, 3.2]
  INFO: mapped N_eff in [2.5, 3.5]
  FAIL: mapped N_eff outside [2.5, 3.5]

Task (S74-CF-10 from S73A landau-baptista workshop):
  Map the S65 fold Hessian signature (36+, 0-, 0 zero modes) to SM relativistic
  degrees of freedom at emergence via boson/fermion partitioning under J_C2 parity,
  then compare to SM N_eff = 3.044.

Framework context (substrate picture):
  The fabric is not IN space -- space is an emergent description of how the
  fabric's spectral weight distributes itself through D_K eigenvalue reorganization.
  N_eff is the count of relativistic modes emerging from the substrate at the fold,
  determined by the Morse-Bott signature of the Hessian at the saddle.

Structural framework:
  The 36-dimensional moduli space of left-invariant metrics on SU(3) decomposes
  under the U(2) = SU(2)xU(1) stabilizer at the Jensen fold into isotypic blocks:

    su(3) = u(1) + su(2) + C^2       (dim 1 + 3 + 4 = 8)
    Sym^2(su(3)^*) = Sym^2(u(1)) + (u(1) tensor su(2)) + (u(1) tensor C^2)
                   + Sym^2(su(2)) + (su(2) tensor C^2) + Sym^2(C^2)
                   = 1 + 3 + 4 + 6 + 12 + 10 = 36 (real dof)

  Under the KO-dim=6 real structure J (Baptista paper 17, eq 4.5-4.7),
  C^2 = fiber of SU(3)/U(2) = CP^2 is the "Higgs direction" (fermion-coupling),
  while u(1)+su(2) is the "gauge direction" (boson-coupling). The J_C2 parity
  acts diagonally on tensor products:

    parity(a,b) = (+1)^(# odd indices in {a,b})     where odd = C^2 = {3,4,5,6}

  This partitions the 36 metric moduli into 20 J-even ("bosonic") and 16 J-odd
  ("fermionic") basis directions. After diagonalizing the fold Hessian, each
  eigenmode carries a dominant parity, and the framework effective g_* is:

    g_*_framework = n_boson + (7/8) * n_fermion

  The mapped N_eff is obtained by normalizing to SM BBN g_*:

    N_eff_mapped = g_*_framework / g_*_SM_BBN

Data source:
  s65_shell_l4_hessian.npz (the canonical S65 36x36 Hessian at tau_fold=0.19).
  Signature (36+, 0-, 0 zero) verified in file loader.

Steps:
  1. Load canonical constants and S65 Hessian.
  2. Verify signature (36+, 0-, 0).
  3. Build J_C2 parity map on the 36 basis pairs.
  4. Decompose each of the 36 eigenmodes by dominant parity.
  5. Compute g_* and N_eff.
  6. Cross-checks:
     a. Total count 36 = n_boson + n_fermion.
     b. U(2)-isotypic cluster assignment consistency (by eigenvalue clustering).
     c. Parity-weighted mean eigenvalues distinct between boson/fermion.
     d. Robust to dominant-vs-full parity assignment (fractional parity weighting).
  7. Report gate verdict.

Author: baptista-spacetime-analyst (Session 74, W4-R)
"""

import sys
import os
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
from numpy.linalg import eigh
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import (
    tau_fold, g_star_SM, g_star_BBN, N_eff_SM, J_C2
)

print("=" * 78)
print("  N-EFF-MORSE-BOTT-74: S65 Hessian signature -> SM relativistic dof")
print("=" * 78)
print(f"  tau_fold = {tau_fold}")
print(f"  g_star_BBN = {g_star_BBN}")
print(f"  N_eff_SM = {N_eff_SM}")

t_start = time.time()

# ============================================================================
# 1. Load S65 fold Hessian data
# ============================================================================
print("\n--- 1. Loading S65 Hessian ---")

hessian_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "s65_shell_l4_hessian.npz")
d = np.load(hessian_path, allow_pickle=True)

H_fold = d["H_eff_L3"]                   # 36x36 tree+1loop Hessian at fold
evals_loaded = np.array(d["evals_L3"])   # pre-computed eigenvalues
n_pos_loaded = int(d["n_pos_L3"])
n_neg_loaded = int(d["n_neg_L3"])
tau_from_data = float(d["tau_fold"])

print(f"  H_fold shape: {H_fold.shape}")
print(f"  tau_fold (data): {tau_from_data}")
print(f"  Loaded signature: {n_pos_loaded}+, {n_neg_loaded}-")

# Verify Hessian is the canonical S65 object
assert H_fold.shape == (36, 36), f"Wrong Hessian shape: {H_fold.shape}"
assert abs(tau_from_data - tau_fold) < 1e-12, "Mismatched tau_fold"
assert n_pos_loaded == 36 and n_neg_loaded == 0, \
    f"Signature mismatch: expected (36,0), got ({n_pos_loaded},{n_neg_loaded})"

# Symmetrize explicitly, then rediagonalize with full eigenvectors
H_sym = 0.5 * (H_fold + H_fold.T)
evals, evecs = eigh(H_sym)

# Cross-check with loaded eigenvalues
max_eval_diff = np.max(np.abs(evals - evals_loaded))  # (local)
print(f"  Max |evals - evals_loaded| = {max_eval_diff:.2e}")
assert max_eval_diff < 1e-8, "Diagonalization mismatch"

n_pos = int(np.sum(evals > 1e-9))   # (local)
n_neg = int(np.sum(evals < -1e-9))  # (local)
n_zero = int(36 - n_pos - n_neg)    # (local)
print(f"  Verified signature: {n_pos}+, {n_neg}-, {n_zero} zero")

# ============================================================================
# 2. Build J_C2 parity map
# ============================================================================
print("\n--- 2. Building J_C2 parity on 36 basis pairs ---")

# su(3) = u(1) + su(2) + C^2
#   u(1)  = index 7 (Y = lambda_8 direction)
#   su(2) = indices 0,1,2 (lambda_1, lambda_2, lambda_3)
#   C^2   = indices 3,4,5,6 (lambda_4..lambda_7, the coset SU(3)/U(2) = CP^2)
#
# The 36 metric moduli are pairs (a,b) with a <= b, a,b in 0..7.
# Under J (KO-dim=6 real structure), C^2 directions are "odd" (fermionic coupling,
# they multiply the Higgs VEV), and u(1)+su(2) directions are "even" (gauge bosons).
# Metric moduli (a,b) inherit parity (-1)^(# odd-index components).

C2_INDICES = [3, 4, 5, 6]           # (local)  SU(3)/U(2) coset = CP^2
U2_INDICES = [0, 1, 2, 7]           # (local)  stabilizer u(1)+su(2)

def J_C2_parity(a: int, b: int) -> int:
    """Return +1 for J-even (bosonic) pair, -1 for J-odd (fermionic) pair."""
    n_odd = int(a in C2_INDICES) + int(b in C2_INDICES)
    return +1 if n_odd % 2 == 0 else -1

pair_list = [(a, b) for a in range(8) for b in range(a, 8)]  # (local)
assert len(pair_list) == 36

parity_arr = np.array([J_C2_parity(a, b) for (a, b) in pair_list])
n_even_basis = int(np.sum(parity_arr == +1))   # (local)
n_odd_basis = int(np.sum(parity_arr == -1))    # (local)
print(f"  Basis parity count: {n_even_basis} even (+1), {n_odd_basis} odd (-1)")
print(f"  Sanity: {n_even_basis + n_odd_basis} = 36 ? {n_even_basis + n_odd_basis == 36}")

# Sanity: the count of J-even pairs = C(dim U(2), 2) + dim U(2) + C(dim C^2, 2)
#   C(4,2)+4 = 10 symmetric pairs inside U(2) block (indices 0,1,2,7)
#   C(4,2)+4 = 10 symmetric pairs inside C^2 block, but U(2)*U(2)=even, C^2*C^2=even
#   Wait: C^2 x C^2 has TWO odd indices, so parity = (+1) (even, because (-1)^2=+1).
# Re-derive: J-even = (number of odd indices in pair is 0 or 2).
#   0 odd indices: both in U(2) (4 indices) -> pairs C(4,2)+4 = 10
#   2 odd indices: both in C^2 (4 indices) -> pairs C(4,2)+4 = 10
#   Total J-even = 20.
# J-odd = exactly 1 odd index: one in U(2), one in C^2 -> 4*4 = 16 pairs.
# Total = 20+16 = 36.  Consistent with counts above.

# ============================================================================
# 3. Partition eigenmodes by dominant J_C2 parity
# ============================================================================
print("\n--- 3. Partitioning 36 eigenmodes by dominant parity ---")

n_boson_dominant = 0                          # (local)
n_fermion_dominant = 0                        # (local)
boson_evals = []                              # (local)
fermion_evals = []                            # (local)
parity_fractions = np.zeros((36, 2))          # (local) [even_frac, odd_frac]

for k in range(36):
    v = evecs[:, k]
    w_even = float(np.sum(v[parity_arr == +1] ** 2))
    w_odd = float(np.sum(v[parity_arr == -1] ** 2))
    parity_fractions[k, 0] = w_even
    parity_fractions[k, 1] = w_odd
    if w_even >= w_odd:
        n_boson_dominant += 1
        boson_evals.append(float(evals[k]))
    else:
        n_fermion_dominant += 1
        fermion_evals.append(float(evals[k]))

boson_evals = np.array(boson_evals)       # (local)
fermion_evals = np.array(fermion_evals)   # (local)

print(f"  n_boson (dominant)   = {n_boson_dominant}")
print(f"  n_fermion (dominant) = {n_fermion_dominant}")
print(f"  sum = {n_boson_dominant + n_fermion_dominant}")
print(f"  mean boson eigenvalue   = {np.mean(boson_evals):12.4f}")
print(f"  mean fermion eigenvalue = {np.mean(fermion_evals):12.4f}")

# Fractional partition (no dominant assignment, straight sum of parity weights)
w_even_total = float(np.sum(parity_fractions[:, 0]))  # (local)
w_odd_total = float(np.sum(parity_fractions[:, 1]))   # (local)
print(f"  weighted (frac)   even = {w_even_total:.4f}")
print(f"  weighted (frac)   odd  = {w_odd_total:.4f}")
print(f"  weighted sum = {w_even_total + w_odd_total:.6f} (should be 36)")

# ============================================================================
# 4. Compute g_* and mapped N_eff
# ============================================================================
print("\n--- 4. g_* and N_eff ---")

# Dominant-parity assignment (integer count)
g_star_framework_dom = n_boson_dominant + (7.0 / 8.0) * n_fermion_dominant  # (local)
N_eff_mapped_dom = g_star_framework_dom / g_star_BBN                         # (local)

# Fractional-parity assignment (continuous)
g_star_framework_frac = w_even_total + (7.0 / 8.0) * w_odd_total  # (local)
N_eff_mapped_frac = g_star_framework_frac / g_star_BBN             # (local)

print(f"  g_*_framework (dominant)     = {g_star_framework_dom:.4f}")
print(f"  g_*_framework (fractional)   = {g_star_framework_frac:.4f}")
print(f"  N_eff_mapped (dominant)      = {N_eff_mapped_dom:.4f}")
print(f"  N_eff_mapped (fractional)    = {N_eff_mapped_frac:.4f}")
print(f"  SM reference                 = {N_eff_SM:.4f}")
print(f"  relative error (dom)         = {(N_eff_mapped_dom - N_eff_SM)/N_eff_SM*100:+.2f}%")
print(f"  relative error (frac)        = {(N_eff_mapped_frac - N_eff_SM)/N_eff_SM*100:+.2f}%")

# ============================================================================
# 5. Cross-checks
# ============================================================================
print("\n--- 5. Cross-checks ---")

# Cross-check 1: count conservation
cc1_count = (n_boson_dominant + n_fermion_dominant) == 36           # (local)
print(f"  CC1 count conservation         : {'PASS' if cc1_count else 'FAIL'}")

# Cross-check 2: basis parity distribution matches isotypic prediction
cc2_parity = (n_even_basis == 20) and (n_odd_basis == 16)           # (local)
print(f"  CC2 basis parity 20/16         : {'PASS' if cc2_parity else 'FAIL'}")

# Cross-check 3: mean boson != mean fermion eigenvalue
#   Bosonic and fermionic J-sectors should carry physically distinct mass scales.
#   Fermionic modes couple to the Higgs direction, so they should sit in a DIFFERENT
#   spectral range than pure gauge modes.
cc3_scales = not np.isclose(np.mean(boson_evals), np.mean(fermion_evals), rtol=0.01)  # (local)
print(f"  CC3 distinct mass scales       : {'PASS' if cc3_scales else 'FAIL'}")

# Cross-check 4: dominant vs fractional agreement within 1%
cc4_robust = abs(N_eff_mapped_dom - N_eff_mapped_frac) / N_eff_SM < 0.01  # (local)
print(f"  CC4 dom vs frac agreement      : {'PASS' if cc4_robust else 'FAIL'}")
print(f"      |dom - frac| = {abs(N_eff_mapped_dom - N_eff_mapped_frac):.4f}")

# Cross-check 5: signature positivity verified (no negative or zero modes)
cc5_signature = (n_pos == 36 and n_neg == 0 and n_zero == 0)        # (local)
print(f"  CC5 positive-def Hessian       : {'PASS' if cc5_signature else 'FAIL'}")

# Cross-check 6: Morse-Bott number consistency -- for a non-degenerate critical
# point with signature (n_+, n_-, 0), the Morse index = n_- = 0, meaning the
# Jensen fold is a LOCAL MINIMUM in the 36D moduli space. All relativistic dof
# at emergence must be GAPPED metric modes (no massless moduli).
morse_index = n_neg                                                  # (local)
cc6_morse_min = (morse_index == 0)                                   # (local)
print(f"  CC6 Morse index 0 (local min)  : {'PASS' if cc6_morse_min else 'FAIL'}")

all_cc = cc1_count and cc2_parity and cc3_scales and cc4_robust and cc5_signature and cc6_morse_min

# ============================================================================
# 6. Gate verdict
# ============================================================================
print("\n--- 6. Gate verdict ---")

# Use dominant-parity value as the primary gate measurement
N_eff_primary = N_eff_mapped_dom                                     # (local)

if 2.8 <= N_eff_primary <= 3.2:
    verdict = "PASS"
    reason = f"N_eff = {N_eff_primary:.4f} in [2.8, 3.2]"
elif 2.5 <= N_eff_primary <= 3.5:
    verdict = "INFO"
    reason = f"N_eff = {N_eff_primary:.4f} in [2.5, 3.5] but outside [2.8, 3.2]"
else:
    verdict = "FAIL"
    reason = f"N_eff = {N_eff_primary:.4f} outside [2.5, 3.5]"

print(f"  Gate: N-EFF-MORSE-BOTT-74")
print(f"  Threshold: PASS if N_eff in [2.8, 3.2], INFO if in [2.5, 3.5]")
print(f"  Computed:  N_eff = {N_eff_primary:.6f}")
print(f"  Verdict:   {verdict}")
print(f"  Reason:    {reason}")

# ============================================================================
# 7. Visualization
# ============================================================================
print("\n--- 7. Visualization ---")

fig, axes = plt.subplots(1, 3, figsize=(16, 5))

# Panel 1: eigenvalue spectrum, color-coded by dominant parity
ax = axes[0]
for k in range(36):
    color = "steelblue" if parity_fractions[k, 0] >= parity_fractions[k, 1] else "indianred"
    ax.scatter(k, evals[k], c=color, s=40, edgecolors="k", linewidths=0.5)
ax.set_xlabel("eigenmode index")
ax.set_ylabel("eigenvalue (mass squared)")
ax.set_title("S65 fold Hessian\nblue = J-even (boson)  red = J-odd (fermion)")
ax.set_yscale("log")
ax.grid(True, alpha=0.3)

# Panel 2: parity-fraction stacked bars
ax = axes[1]
idx = np.arange(36)
ax.bar(idx, parity_fractions[:, 0], color="steelblue", label="J-even", alpha=0.85)
ax.bar(idx, parity_fractions[:, 1], bottom=parity_fractions[:, 0], color="indianred", label="J-odd", alpha=0.85)
ax.set_xlabel("eigenmode index")
ax.set_ylabel("parity weight")
ax.set_title("Eigenvector J_C2-parity decomposition")
ax.legend()
ax.set_ylim(0, 1.05)
ax.grid(True, alpha=0.3)

# Panel 3: N_eff summary
ax = axes[2]
labels = ["framework\n(dom)", "framework\n(frac)", "SM\n(PDG)"]
values = [N_eff_mapped_dom, N_eff_mapped_frac, N_eff_SM]
colors = ["steelblue", "lightsteelblue", "darkgreen"]
ax.bar(labels, values, color=colors, edgecolor="k")
ax.axhspan(2.8, 3.2, color="green", alpha=0.15, label="PASS window")
ax.axhspan(2.5, 3.5, color="yellow", alpha=0.10, label="INFO window")
ax.set_ylabel("N_eff")
ax.set_title(f"N-EFF-MORSE-BOTT-74: {verdict}")
ax.legend()
ax.grid(True, alpha=0.3)

plt.tight_layout()
plot_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         "s74_n_eff_morse_bott.png")
plt.savefig(plot_path, dpi=150, bbox_inches="tight")
plt.close()
print(f"  Saved plot: {plot_path}")

# ============================================================================
# 8. Save data
# ============================================================================
print("\n--- 8. Saving data ---")

npz_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "s74_n_eff_morse_bott.npz")
np.savez(
    npz_path,
    gate_name="N-EFF-MORSE-BOTT-74",
    gate_verdict=verdict,
    gate_reason=reason,
    # Input Hessian
    H_fold=H_sym,
    evals=evals,
    evecs=evecs,
    n_pos=n_pos,
    n_neg=n_neg,
    n_zero=n_zero,
    morse_index=morse_index,
    # Parity structure
    C2_indices=np.array(C2_INDICES),
    U2_indices=np.array(U2_INDICES),
    pair_list=np.array(pair_list),
    parity_arr=parity_arr,
    parity_fractions=parity_fractions,
    n_even_basis=n_even_basis,
    n_odd_basis=n_odd_basis,
    # Boson/fermion partition
    n_boson_dominant=n_boson_dominant,
    n_fermion_dominant=n_fermion_dominant,
    boson_evals=boson_evals,
    fermion_evals=fermion_evals,
    w_even_total=w_even_total,
    w_odd_total=w_odd_total,
    # Results
    g_star_framework_dom=g_star_framework_dom,
    g_star_framework_frac=g_star_framework_frac,
    g_star_BBN=g_star_BBN,
    N_eff_mapped_dom=N_eff_mapped_dom,
    N_eff_mapped_frac=N_eff_mapped_frac,
    N_eff_SM=N_eff_SM,
    N_eff_primary=N_eff_primary,
    # Cross-checks
    cc1_count=cc1_count,
    cc2_parity=cc2_parity,
    cc3_scales=cc3_scales,
    cc4_robust=cc4_robust,
    cc5_signature=cc5_signature,
    cc6_morse_min=cc6_morse_min,
    all_cc=all_cc,
    tau_fold=tau_fold,
)
print(f"  Saved data: {npz_path}")

t_elapsed = time.time() - t_start  # (local)
print(f"\nTotal runtime: {t_elapsed:.2f}s")

# ============================================================================
# 9. Summary
# ============================================================================
print("\n" + "=" * 78)
print("  N-EFF-MORSE-BOTT-74 SUMMARY")
print("=" * 78)
print(f"  Signature        : (36+, 0-, 0 zero)  -- Jensen fold is local minimum")
print(f"  Basis parity     : {n_even_basis} J-even, {n_odd_basis} J-odd")
print(f"  Mode partition   : {n_boson_dominant} boson, {n_fermion_dominant} fermion")
print(f"  g_*_framework    : {g_star_framework_dom:.4f}")
print(f"  N_eff_mapped     : {N_eff_primary:.4f}  (SM = {N_eff_SM})")
print(f"  Cross-checks 6/6 : {'PASS' if all_cc else 'FAIL'}")
print(f"  Gate verdict     : {verdict}")
print(f"  Reason           : {reason}")
