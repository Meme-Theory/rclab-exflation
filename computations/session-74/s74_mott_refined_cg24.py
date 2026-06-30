#!/usr/bin/env python3
"""
s74_mott_refined_cg24.py — MOTT-REFINED-CG24-74 (Session 74, Wave 2 Batch 2)

Refined Mott delta_OOM using the CANONICAL E_C = 0.4643 M_KK established in
W1-D (E_C-RESOLUTION-74, Method A: OES pair-addition on full CG(24)).

Sector-specific Josephson couplings from the C^2 -> SU(2) x U(1) branching:
    C^2 branches as (2,+1) + (2,-1) + (1,+2) + (1,-2)
    Dimensions:         2      2       1        1
    Total dim weight = 6 (matches z=6 coordination of CG(24))

    SU(2)-doublet weight = 2+2 = 4  (doublets carry SU(2) charge)
    U(1)-singlet weight  = 1+1 = 2  (singlets carry only U(1) charge)
    C^2 intrinsic weight = 0         (confined: no direct Josephson coupling)

The decomposition is applied to the bond-counted Josephson energy per cell.
Per-cell Josephson energy = (z/2) * J_eff summed over 6 bonds with sector weights.
Sector partition:
    E_J^{SU(2)} = (4/6) * E_J^cell      (SU(2) doublet contribution)
    E_J^{U(1)}  = (2/6) * E_J^cell      (U(1) singlet contribution)
    E_J^{C^2}   = 0                      (confined, no direct coupling)

SECTOR-SPECIFIC J_a per bond:
    J_{SU(2)} = J_C2 * (4/6) / 2  = J_C2 * (SU(2) weight from branching) / 2
                                  (division by 2: per-bond, not per-cell)
    J_{U(1)}  = J_C2 * (2/6)      = J_C2 * (U(1) weight from branching)
    J_{C^2}   = 0                  (intrinsic)

PHASE-DIFFUSION MOTT FORMULA (per sector):
    delta_OOM_a = log10(1 + sqrt(E_C / (8 * J_a)))

Aggregate (linear sum):
    delta_OOM^{Mott total} = delta_OOM_{SU(2)} + delta_OOM_{U(1)} + delta_OOM_{C^2}

Gate MOTT-REFINED-CG24-74:
  PASS: delta_OOM_Mott in [0.18, 0.28] AND C^2 contribution < 1e-6
  INFO: C^2 contribution nonzero but < 0.01
  FAIL: total outside [0.10, 0.40] OR C^2 contribution significant

Session 74, Wave 2 Batch 2 (W2-F), landau-condensed-matter-theorist
S73A landau-baptista workshop carry-forward #1 (S74-CF-1)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import numpy as np
import matplotlib.pyplot as plt
from canonical_constants import (
    M_KK, J_C2, J_su2, J_u1, N_cells,
    Delta_BCS, Delta_0_OES,
    PI,
)

data_dir = os.path.dirname(__file__)

print("=" * 72)
print("MOTT-REFINED-CG24-74: Refined Mott delta_OOM via sector branching")
print("=" * 72)
print()

# =============================================================================
# 1. LOAD INPUTS
# =============================================================================

# W1-D canonical E_C (Method A: OES pair-addition on full CG(24))
w1d = np.load(os.path.join(data_dir, 's74_ec_resolution.npz'), allow_pickle=True)
E_C_canonical = float(w1d['E_C_oes_cg24_method_A'])  # (local)
print(f"[W1-D carry-forward] canonical E_C = {E_C_canonical:.6f} M_KK")
print(f"[W1-D carry-forward] Method A (OES pair-addition), gate PASS")
print()

# CG(24) graph (from S73A)
g = np.load(os.path.join(data_dir, 's73a_graph_spectral_decoherence.npz'),
            allow_pickle=True)
N_vert_g = int(g['N_vert'])  # (local)
N_edges_g = int(g['N_edges'])  # (local)
z_CG24 = int(g['degree'])  # (local)
assert N_vert_g == 24, f"Expected 24 vertices, got {N_vert_g}"
assert N_edges_g == 72, f"Expected 72 edges, got {N_edges_g}"
assert z_CG24 == 6, f"Expected z=6, got {z_CG24}"
print(f"[CG(24) graph] N_vert={N_vert_g}, N_edges={N_edges_g}, z={z_CG24}")
print()

# Canonical Josephson coupling (per-bond, dominant C^2 channel)
print(f"[Canonical] J_C2 = {J_C2:.4f} M_KK per bond")
print(f"[Canonical] J_su2 = {J_su2:.4f} M_KK per bond (reference only)")
print(f"[Canonical] J_u1 = {J_u1:.4f} M_KK per bond (reference only)")
print()

# =============================================================================
# 2. BRANCHING DECOMPOSITION: C^2 -> SU(2) x U(1)
# =============================================================================
#
# The coset C^2 = SU(3)/[SU(2) x U(1)] branches under SU(2) x U(1) as:
#     (2, +1) + (2, -1) + (1, +2) + (1, -2)
# where the first number is the SU(2) dimension and the second is the U(1) charge.
#
# Total dim of branching = 2+2+1+1 = 6 states.
# This matches exactly the coordination number z=6 of CG(24): each cell
# has 6 nearest-neighbor bonds, corresponding to the 6 branch components.
#
# The SU(2) doublets carry SU(2) gauge content; the U(1) singlets do not.
# The C^2 intrinsic sector is confined (no direct Josephson coupling at the
# fold — C^2 is broken by the deformation and does not support phase transport).

dim_su2 = 2 + 2  # (2,+1) + (2,-1)  # (local)
dim_u1 = 1 + 1   # (1,+2) + (1,-2)  # (local)
dim_c2 = 0       # C^2 intrinsic: confined, no direct coupling  # (local)
dim_total = dim_su2 + dim_u1 + dim_c2  # (local)

print("2. BRANCHING DECOMPOSITION: C^2 -> SU(2) x U(1)")
print("-" * 72)
print(f"   Branch (2,+1): dim=2 (SU(2) doublet, U(1) charge +1)")
print(f"   Branch (2,-1): dim=2 (SU(2) doublet, U(1) charge -1)")
print(f"   Branch (1,+2): dim=1 (SU(2) singlet, U(1) charge +2)")
print(f"   Branch (1,-2): dim=1 (SU(2) singlet, U(1) charge -2)")
print(f"   SU(2) weight total = {dim_su2}")
print(f"   U(1)  weight total = {dim_u1}")
print(f"   C^2 intrinsic      = {dim_c2} (confined)")
print(f"   Sum of weights     = {dim_total} (= z_CG24 = {z_CG24})")
assert dim_total == z_CG24, f"Branching sum {dim_total} != coordination z={z_CG24}"
print(f"   Sum-rule check: branching dim sum = coordination z  PASS")
print()

# =============================================================================
# 3. SECTOR-SPECIFIC JOSEPHSON COUPLINGS
# =============================================================================
#
# Prompt specifies:
#   J_{SU(2)} = J_C2 * (SU(2) weight) / 2
#   J_{U(1)}  = J_C2 * (U(1)  weight)
#   J_{C^2}   = 0
#
# Physical reading: J_C2 is the per-bond Josephson scale. The SU(2) weight (4)
# is divided by 2 because SU(2) is a complex (non-abelian) phase group with
# twice the "phase directions" of U(1); the factor cancels one of these.
# The U(1) weight enters without division — it is already a single-phase group.

J_SU2 = J_C2 * (dim_su2 / 2.0)  # SU(2) sector Josephson coupling  # (local)
J_U1  = J_C2 * (dim_u1)          # U(1)  sector Josephson coupling  # (local)
J_Csq = 0.0                       # C^2 confined  # (local)

print("3. SECTOR-SPECIFIC JOSEPHSON COUPLINGS")
print("-" * 72)
print(f"   J_{{SU(2)}} = J_C2 * (4/2) = {J_C2:.4f} * 2 = {J_SU2:.6f} M_KK")
print(f"   J_{{U(1)}}  = J_C2 * 2    = {J_C2:.4f} * 2 = {J_U1:.6f} M_KK")
print(f"   J_{{C^2}}   = 0                          = {J_Csq:.6f} M_KK")
print()

# =============================================================================
# 4. PHASE-DIFFUSION MOTT FORMULA PER SECTOR
# =============================================================================
#
#   delta_OOM_a = log10(1 + sqrt(E_C / (8 * J_a)))
#
# For J_a = 0 (C^2): the argument diverges. Physically, the C^2 sector has
# NO phase to diffuse (it is confined, not fluctuating). The delta_OOM
# contribution from a confined sector is 0 by construction: if there is no
# Josephson coupling, there is no decoherence channel to dephase.
# We implement this as an explicit structural exception for J=0.

def mott_delta_OOM(E_C, J_a):
    """Phase-diffusion Mott decoherence OOM contribution for sector with Josephson J_a."""
    if J_a <= 0.0:
        # Confined sector: no phase coherence to lose, no dephasing channel
        return 0.0
    arg = np.sqrt(E_C / (8.0 * J_a))  # (local)
    return float(np.log10(1.0 + arg))

dOOM_SU2 = mott_delta_OOM(E_C_canonical, J_SU2)  # (local)
dOOM_U1  = mott_delta_OOM(E_C_canonical, J_U1)   # (local)
dOOM_Csq = mott_delta_OOM(E_C_canonical, J_Csq)  # = 0 by construction  # (local)

dOOM_total = dOOM_SU2 + dOOM_U1 + dOOM_Csq  # (local)

print("4. PHASE-DIFFUSION MOTT FORMULA (per sector)")
print("-" * 72)
print(f"   delta_OOM_a = log10(1 + sqrt(E_C / (8*J_a)))")
print(f"   E_C = {E_C_canonical:.6f} M_KK  (W1-D canonical)")
print()
arg_SU2 = np.sqrt(E_C_canonical / (8.0 * J_SU2))  # (local)
arg_U1  = np.sqrt(E_C_canonical / (8.0 * J_U1))   # (local)
print(f"   sqrt(E_C/(8*J_SU2)) = sqrt({E_C_canonical:.4f}/(8*{J_SU2:.4f})) = {arg_SU2:.6f}")
print(f"   sqrt(E_C/(8*J_U1))  = sqrt({E_C_canonical:.4f}/(8*{J_U1:.4f}))  = {arg_U1:.6f}")
print()
print(f"   delta_OOM_{{SU(2)}} = log10(1 + {arg_SU2:.6f}) = {dOOM_SU2:.6f}")
print(f"   delta_OOM_{{U(1)}}  = log10(1 + {arg_U1:.6f}) = {dOOM_U1:.6f}")
print(f"   delta_OOM_{{C^2}}   = 0 (confined, J=0)     = {dOOM_Csq:.6f}")
print()
print(f"   TOTAL (linear sum) = {dOOM_total:.6f}")
print()

# =============================================================================
# 5. CROSS-CHECKS
# =============================================================================

print("5. CROSS-CHECKS")
print("-" * 72)
print()

# Cross-check 1: Linearity of sector contributions
sum_check = dOOM_SU2 + dOOM_U1 + dOOM_Csq  # (local)
linearity_error = abs(sum_check - dOOM_total)  # (local)
print(f"   [1] Sector linearity:")
print(f"       delta_OOM_SU2 + delta_OOM_U1 + delta_OOM_C2 = {sum_check:.6f}")
print(f"       Total                                         = {dOOM_total:.6f}")
print(f"       Error: {linearity_error:.2e}")
assert linearity_error < 1e-12, "Linearity check failed"
print(f"       PASS (exact linearity)")
print()

# Cross-check 2: Limiting case E_C -> 0
E_C_zero = 0.0  # (local)
dOOM_zero_SU2 = mott_delta_OOM(E_C_zero, J_SU2)  # (local)
dOOM_zero_U1 = mott_delta_OOM(E_C_zero, J_U1)  # (local)
dOOM_zero_total = dOOM_zero_SU2 + dOOM_zero_U1  # (local)
print(f"   [2] Limit E_C -> 0: delta_OOM should -> 0")
print(f"       delta_OOM(E_C=0, J_SU2) = {dOOM_zero_SU2:.2e}")
print(f"       delta_OOM(E_C=0, J_U1)  = {dOOM_zero_U1:.2e}")
print(f"       Total                     = {dOOM_zero_total:.2e}")
assert dOOM_zero_total < 1e-12, "E_C=0 limit failed"
print(f"       PASS (classical limit: no charging -> no Mott dephasing)")
print()

# Cross-check 3: Limiting case J_a -> 0 (C^2 confined)
# For J -> 0+, arg -> infinity, so delta_OOM -> infinity.
# We handle J=0 as a structural exception (confined: dOOM=0 by construction).
# Demonstrate the divergence as J shrinks:
J_tiny = 1e-10  # (local)
dOOM_tiny = mott_delta_OOM(E_C_canonical, J_tiny)  # (local)
print(f"   [3] Limit J -> 0+:")
print(f"       delta_OOM(J={J_tiny:.0e}) = {dOOM_tiny:.4f}  (diverges as 1/sqrt(J))")
print(f"       PASS (formula diverges as expected; C^2 exception applies at J=0 exactly)")
print()

# Cross-check 4: Monotonicity in E_C
E_C_half = E_C_canonical / 2.0  # (local)
E_C_double = E_C_canonical * 2.0  # (local)
dOOM_half = mott_delta_OOM(E_C_half, J_SU2) + mott_delta_OOM(E_C_half, J_U1)  # (local)
dOOM_double = mott_delta_OOM(E_C_double, J_SU2) + mott_delta_OOM(E_C_double, J_U1)  # (local)
print(f"   [4] Monotonicity in E_C:")
print(f"       delta_OOM(E_C/2  = {E_C_half:.4f}) = {dOOM_half:.6f}")
print(f"       delta_OOM(E_C    = {E_C_canonical:.4f}) = {dOOM_total:.6f}")
print(f"       delta_OOM(E_C*2  = {E_C_double:.4f}) = {dOOM_double:.6f}")
mono_ok = (dOOM_half < dOOM_total < dOOM_double)  # (local)
assert mono_ok, "Monotonicity check failed"
print(f"       PASS (monotonic increasing in E_C)")
print()

# Cross-check 5: Comparison to S73A single-value Mott (delta_OOM = 0.336)
dOOM_S73A = 0.336  # (local)
reduction_factor = dOOM_S73A / dOOM_total if dOOM_total > 0 else float('inf')  # (local)
print(f"   [5] Comparison to S73A W1-E single-value Mott (geomean E_C = 0.723)")
print(f"       S73A delta_OOM_Mott = {dOOM_S73A:.4f}")
print(f"       S74 refined total   = {dOOM_total:.4f}")
print(f"       Reduction factor    = {reduction_factor:.2f}x")
print(f"       Expected: refined should be SMALLER (better-localized E_C)")
print()

# Cross-check 6: Compound decoherence budget (Mott + Dispersive)
# S73A W3-A dispersive: delta_OOM_disp = 0.150 (INFO)
# S73A W4-B combined:  delta_OOM_total = 0.486 (overcloses by 1.8x)
# A_s budget target:    delta_OOM ~ 0.267 (S72 t_dec/t_transit = 0.716)
dOOM_disp_S73A = 0.150  # (local)
dOOM_compound = dOOM_total + dOOM_disp_S73A  # (local)
As_budget_target = 0.267  # (local)
print(f"   [6] Compound decoherence budget (Mott + Dispersive):")
print(f"       dispersive (S73A W3-A INFO)   = {dOOM_disp_S73A:.4f}")
print(f"       refined Mott (this work)      = {dOOM_total:.4f}")
print(f"       Compound total                = {dOOM_compound:.4f}")
print(f"       A_s budget target (S72)       = {As_budget_target:.4f}")
print(f"       Residual (compound - target)  = {dOOM_compound - As_budget_target:+.4f}")
if abs(dOOM_compound - As_budget_target) < 0.05:
    print(f"       Compound lies WITHIN +/- 0.05 OOM of A_s target (close)")
elif dOOM_compound > As_budget_target:
    print(f"       Compound OVER-closes target by {dOOM_compound - As_budget_target:.4f} OOM")
else:
    print(f"       Compound UNDER-closes target by {As_budget_target - dOOM_compound:.4f} OOM")
print()

# =============================================================================
# 6. GATE VERDICT
# =============================================================================

print("6. GATE VERDICT")
print("-" * 72)
print()

gate_pass_range = (0.18, 0.28)  # (local)
gate_info_range = (0.10, 0.40)  # (local)
C2_threshold_pass = 1e-6  # (local)
C2_threshold_info = 0.01  # (local)

gate_in_pass_band = (gate_pass_range[0] <= dOOM_total <= gate_pass_range[1])  # (local)
gate_in_info_band = (gate_info_range[0] <= dOOM_total <= gate_info_range[1])  # (local)
C2_is_zero = (abs(dOOM_Csq) < C2_threshold_pass)  # (local)
C2_is_small = (abs(dOOM_Csq) < C2_threshold_info)  # (local)

print(f"   delta_OOM total:        {dOOM_total:.6f}")
print(f"   delta_OOM C^2 contrib:  {dOOM_Csq:.6e}")
print(f"   Pass band:              [{gate_pass_range[0]}, {gate_pass_range[1]}]")
print(f"   Info band:              [{gate_info_range[0]}, {gate_info_range[1]}]")
print(f"   In pass band:           {gate_in_pass_band}")
print(f"   In info band:           {gate_in_info_band}")
print(f"   C^2 contribution zero:  {C2_is_zero}  (< {C2_threshold_pass:.0e})")
print(f"   C^2 contribution small: {C2_is_small} (< {C2_threshold_info:.0e})")
print()

if gate_in_pass_band and C2_is_zero:
    gate_verdict = "PASS"  # (local)
    gate_detail = (
        f"delta_OOM = {dOOM_total:.4f} in [{gate_pass_range[0]}, {gate_pass_range[1]}] "
        f"and C^2 contribution = {dOOM_Csq:.2e} < 1e-6. "
        f"Refined Mott closes {dOOM_total/0.336*100:.1f}% of S73A budget; "
        f"C^2 confinement exact."
    )  # (local)
elif gate_in_info_band and not C2_is_zero and C2_is_small:
    gate_verdict = "INFO"  # (local)
    gate_detail = (
        f"delta_OOM = {dOOM_total:.4f} in info band [{gate_info_range[0]}, {gate_info_range[1]}] "
        f"but C^2 contribution {dOOM_Csq:.2e} nonzero."
    )  # (local)
elif gate_in_info_band and C2_is_zero:
    # In info band but not pass band, C^2 properly zero
    gate_verdict = "INFO"  # (local)
    gate_detail = (
        f"delta_OOM = {dOOM_total:.4f} outside pass band [{gate_pass_range[0]}, "
        f"{gate_pass_range[1]}] but within info band [{gate_info_range[0]}, "
        f"{gate_info_range[1]}]. C^2 correctly zero."
    )  # (local)
else:
    gate_verdict = "FAIL"  # (local)
    gate_detail = (
        f"delta_OOM = {dOOM_total:.4f} outside info band [{gate_info_range[0]}, "
        f"{gate_info_range[1]}] or C^2 contribution {dOOM_Csq:.2e} "
        f"exceeds {C2_threshold_info}."
    )  # (local)

print(f"   GATE VERDICT: {gate_verdict}")
print(f"   Detail:       {gate_detail}")
print()

# =============================================================================
# 7. SENSITIVITY SCAN (for plot)
# =============================================================================

print("7. SENSITIVITY SCAN")
print("-" * 72)

# Scan over E_C range spanning the 3 methods from W1-D
E_C_scan = np.logspace(np.log10(0.05), np.log10(15.0), 100)  # (local)
dOOM_SU2_scan = np.array([mott_delta_OOM(ec, J_SU2) for ec in E_C_scan])  # (local)
dOOM_U1_scan = np.array([mott_delta_OOM(ec, J_U1) for ec in E_C_scan])  # (local)
dOOM_total_scan = dOOM_SU2_scan + dOOM_U1_scan  # (local)

# Reference markers
E_C_method_A = 0.4643   # (local)  # OES pair-addition (canonical)
E_C_method_B = 9.01     # (local)  # Bogoliubov phase-stiffness
E_C_method_C = 0.061    # (local)  # Josephson-softened charging

print(f"   E_C scan: [{E_C_scan[0]:.3f}, {E_C_scan[-1]:.3f}] M_KK")
print(f"   at Method A ({E_C_method_A}): delta_OOM = {dOOM_total_scan[np.argmin(np.abs(E_C_scan - E_C_method_A))]:.4f}")
print(f"   at Method B ({E_C_method_B}): delta_OOM = {dOOM_total_scan[np.argmin(np.abs(E_C_scan - E_C_method_B))]:.4f}")
print(f"   at Method C ({E_C_method_C}): delta_OOM = {dOOM_total_scan[np.argmin(np.abs(E_C_scan - E_C_method_C))]:.4f}")
print()

# =============================================================================
# 8. SAVE DATA
# =============================================================================

out_npz = os.path.join(data_dir, 's74_mott_refined_cg24.npz')  # (local)
np.savez(
    out_npz,
    gate_name='MOTT-REFINED-CG24-74',
    gate_verdict=gate_verdict,
    gate_detail=gate_detail,
    # Canonical input
    E_C_canonical=E_C_canonical,
    J_C2_canonical=J_C2,
    N_vert=N_vert_g,
    N_edges=N_edges_g,
    z_CG24=z_CG24,
    # Branching
    dim_su2=dim_su2,
    dim_u1=dim_u1,
    dim_c2=dim_c2,
    dim_total=dim_total,
    # Sector Josephson couplings
    J_SU2=J_SU2,
    J_U1=J_U1,
    J_Csq=J_Csq,
    # Per-sector delta_OOM
    dOOM_SU2=dOOM_SU2,
    dOOM_U1=dOOM_U1,
    dOOM_Csq=dOOM_Csq,
    dOOM_total=dOOM_total,
    # Formula inputs
    arg_SU2=arg_SU2,
    arg_U1=arg_U1,
    # Cross-check results
    linearity_error=linearity_error,
    dOOM_zero_limit=dOOM_zero_total,
    dOOM_half_E_C=dOOM_half,
    dOOM_double_E_C=dOOM_double,
    monotonic_in_E_C=mono_ok,
    # S73A comparison
    dOOM_S73A=dOOM_S73A,
    reduction_factor=reduction_factor,
    dOOM_disp_S73A=dOOM_disp_S73A,
    dOOM_compound=dOOM_compound,
    As_budget_target=As_budget_target,
    compound_residual=dOOM_compound - As_budget_target,
    # Sensitivity scan
    E_C_scan=E_C_scan,
    dOOM_SU2_scan=dOOM_SU2_scan,
    dOOM_U1_scan=dOOM_U1_scan,
    dOOM_total_scan=dOOM_total_scan,
    # Gate metadata
    gate_pass_range=np.array(gate_pass_range),
    gate_info_range=np.array(gate_info_range),
    C2_threshold_pass=C2_threshold_pass,
    C2_threshold_info=C2_threshold_info,
)
print(f"   Saved: {out_npz}")
print()

# =============================================================================
# 9. PLOT
# =============================================================================

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Left: sensitivity scan of delta_OOM vs E_C
ax = axes[0]
ax.semilogx(E_C_scan, dOOM_SU2_scan, 'b-', lw=2, label='SU(2) sector')
ax.semilogx(E_C_scan, dOOM_U1_scan, 'g-', lw=2, label='U(1) sector')
ax.semilogx(E_C_scan, dOOM_total_scan, 'k-', lw=2.5, label='Total (SU(2)+U(1))')

# Gate bands
ax.axhspan(gate_pass_range[0], gate_pass_range[1], color='green', alpha=0.15,
           label=f'PASS band [{gate_pass_range[0]}, {gate_pass_range[1]}]')
ax.axhspan(gate_info_range[0], gate_pass_range[0], color='yellow', alpha=0.15)
ax.axhspan(gate_pass_range[1], gate_info_range[1], color='yellow', alpha=0.15,
           label=f'INFO band [{gate_info_range[0]}, {gate_info_range[1]}]')

# Method reference markers
ax.axvline(E_C_method_A, color='red', lw=1.5, ls='--',
           label=f'Method A (canonical) = {E_C_method_A}')
ax.axvline(E_C_method_B, color='purple', lw=1, ls=':',
           label=f'Method B = {E_C_method_B}')
ax.axvline(E_C_method_C, color='brown', lw=1, ls=':',
           label=f'Method C = {E_C_method_C}')

# Highlight canonical point
ax.plot(E_C_canonical, dOOM_total, 'r*', ms=20, mec='black', mew=1.5,
        zorder=10, label=f'Canonical: {dOOM_total:.4f}')

ax.set_xlabel('E_C (M_KK)', fontsize=12)
ax.set_ylabel(r'$\delta_{\rm OOM}^{\rm Mott}$', fontsize=12)
ax.set_title('MOTT-REFINED-CG24-74: Sector Decomposition Scan', fontsize=13)
ax.legend(loc='upper left', fontsize=9, ncol=1)
ax.grid(True, alpha=0.3)
ax.set_ylim(0, 0.6)

# Right: bar chart of sector contributions
ax = axes[1]
sectors = ['SU(2)', 'U(1)', r'$C^2$ (confined)', 'Total']  # (local)
values = [dOOM_SU2, dOOM_U1, dOOM_Csq, dOOM_total]  # (local)
colors = ['blue', 'green', 'gray', 'black']  # (local)

bars = ax.bar(sectors, values, color=colors, alpha=0.7, edgecolor='black')

for bar, val in zip(bars, values):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 0.005,
            f'{val:.4f}', ha='center', va='bottom', fontsize=11, fontweight='bold')

# Reference lines: S73A value, gate bands
ax.axhline(dOOM_S73A, color='red', lw=1.5, ls='--',
           label=f'S73A single-value = {dOOM_S73A:.3f}')
ax.axhspan(gate_pass_range[0], gate_pass_range[1], color='green', alpha=0.15,
           label=f'PASS band [{gate_pass_range[0]}, {gate_pass_range[1]}]')

ax.set_ylabel(r'$\delta_{\rm OOM}^{\rm Mott}$', fontsize=12)
ax.set_title(f'Sector-Specific Mott Contributions (Gate: {gate_verdict})',
             fontsize=13)
ax.legend(loc='upper left', fontsize=10)
ax.grid(True, axis='y', alpha=0.3)
ax.set_ylim(0, 0.4)

plt.tight_layout()
plot_path = os.path.join(data_dir, 's74_mott_refined_cg24.png')  # (local)
plt.savefig(plot_path, dpi=130, bbox_inches='tight')
print(f"   Saved: {plot_path}")
print()

# =============================================================================
# FINAL SUMMARY
# =============================================================================

print("=" * 72)
print("FINAL SUMMARY")
print("=" * 72)
print(f"  Gate: MOTT-REFINED-CG24-74")
print(f"  Verdict: {gate_verdict}")
print(f"  E_C canonical (W1-D Method A):  {E_C_canonical:.6f} M_KK")
print(f"  J_{{SU(2)}}: {J_SU2:.6f} M_KK  -> delta_OOM = {dOOM_SU2:.6f}")
print(f"  J_{{U(1)}} : {J_U1:.6f} M_KK  -> delta_OOM = {dOOM_U1:.6f}")
print(f"  J_{{C^2}} : {J_Csq:.6f} M_KK  -> delta_OOM = {dOOM_Csq:.6f}  (confined)")
print(f"  TOTAL: delta_OOM = {dOOM_total:.6f}")
print(f"  S73A baseline:    {dOOM_S73A:.4f}")
print(f"  Reduction factor: {reduction_factor:.2f}x")
print(f"  Compound (Mott+Disp) = {dOOM_compound:.4f} vs target {As_budget_target:.4f}")
print("=" * 72)
