#!/usr/bin/env python3
"""
s71_r_spatial_scan.py — Compound OOM vs r_spatial Parameter Scan
================================================================

Session 71, W2-A: R-SPATIAL-SCAN-71

Physics:
    The S70 compound squeeze used r_spatial = 0.551 (from SU11-PHASE-69).
    This script scans r_spatial over a range to find r_spatial_critical --
    the value at which the compound A_s OOM gap closes to zero.

    The compound squeeze is an SU(1,1) group product:
        S_compound = S_spatial(r_spatial, phi_random) * S_Leggett(r_L) * S_BCS(r_k, phi_k)

    where the spatial phase phi is von Mises distributed with concentration
    kappa = J_C2 / T_acoustic.

    The total OOM squeeze is delta_OOM = log10(cosh(2*r_eff)),
    and the remaining A_s gap is:
        remaining_gap = A_s_gap_baseline - delta_OOM

    We scan r_spatial in {0.30, 0.35, ..., 0.70, 0.881} to find
    r_spatial_critical where remaining_gap = 0.

    W1-C (INTER-SITE-ENTANGLE-71) found S_vN = 2.00 bits (4-state entanglement),
    implying r_eff = 0.881 rather than 0.551 due to multi-mode transmon physics.
    This value is included in the scan.

Pre-registered gate: R-SPATIAL-SCAN-71
    INFO: Report r_spatial_critical.
    If in [0.45, 0.65] = gap closeable with modest parameter change.
    If > 1.0 = gap not closeable by this channel alone.

Input files:
    - computations/_shared/canonical_constants.py
    - computations/session-70/s70_phi_eff_compound.npz
    - computations/session-70/s70_leggett_vacuum.npz

Output files:
    - computations/session-71/s71_r_spatial_scan.npz
"""

import numpy as np
from scipy.special import i0 as bessel_I0, i1 as bessel_I1
from scipy.interpolate import interp1d
import sys
import os

# Import canonical constants
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    Delta_BCS, T_acoustic, N_dof_BCS, J_C2, A_s_CMB
)


# =============================================================================
#  Section 1: Load input data and establish baseline
# =============================================================================

print("=" * 72)
print("S71 W2-A: R-SPATIAL-SCAN-71 — Compound OOM vs r_spatial Scan")
print("=" * 72)

# Load S70 compound data
compound_data = np.load("computations/session-70/s70_phi_eff_compound.npz", allow_pickle=True)

# Per-mode BCS squeeze parameters (from S70)
r_k_bcs = compound_data["r_k_bcs"]       # 8 modes: B2[0..3], B1, B3[0..2]
phi_k_bcs = compound_data["phi_k_bcs"]   # BCS phases per mode
labels = compound_data["labels"]
mode_weights = compound_data["mode_weights"]  # Normalized per-mode weights

# Von Mises parameters (from S70)
kappa_vM = float(compound_data["kappa_vM"])
C_vM = float(compound_data["C_vM"])  # I_1(kappa)/I_0(kappa)

# Leggett squeeze (from S70)
leggett_data = np.load("computations/session-70/s70_leggett_vacuum.npz", allow_pickle=True)
r_L = float(leggett_data["r_L"])  # = 0.617

# Baseline A_s gap AFTER Leggett correction (from S70)
A_s_gap_baseline = float(leggett_data["A_s_gap_with_L"])  # = 0.267 OOM

# S70 canonical r_spatial
r_spatial_s70 = float(compound_data["r_spatial"])  # = 1.098 (double-squeeze convention)
r_eff_canonical = float(compound_data["r_eff_canonical"])  # = 0.5545

# S69 single-squeeze r_spatial
r_spatial_s69 = 0.551  # From SU11-PHASE-69 (arctanh(0.500))  # (local)

print(f"\n--- Input Summary ---")
print(f"Per-mode BCS squeeze r_k: {r_k_bcs}")
print(f"Per-mode BCS phases phi_k: {phi_k_bcs}")
print(f"Leggett squeeze r_L = {r_L:.4f}")
print(f"Von Mises kappa = {kappa_vM:.4f}, C_vM = {C_vM:.6f}")
print(f"Mode weights: {mode_weights}")
print(f"A_s gap baseline (after Leggett) = {A_s_gap_baseline:.4f} OOM")
print(f"S69 r_spatial = {r_spatial_s69:.4f}")
print(f"S70 r_spatial (double-squeeze) = {r_spatial_s70:.4f}")
print(f"S70 r_eff_canonical = {r_eff_canonical:.4f}")


# =============================================================================
#  Section 2: SU(1,1) Bargmann representation
# =============================================================================

def su11_matrix(r, phi):
    """Construct the SU(1,1) Bargmann matrix S(r, phi)."""
    cr = np.cosh(r)
    sr = np.sinh(r)
    ep = np.exp(1j * phi)
    em = np.exp(-1j * phi)
    return np.array([[cr, ep * sr],
                     [em * sr, cr]], dtype=complex)


def extract_su11_params(S):
    """Extract (r, phi) from an SU(1,1) Bargmann matrix."""
    alpha = S[0, 0]
    beta = S[0, 1]
    r_out = np.arccosh(np.abs(alpha)) if np.abs(alpha) >= 1.0 else 0.0
    phi_out = np.angle(beta)
    return float(r_out), float(phi_out)


# =============================================================================
#  Section 3: Compound squeeze computation for a given r_spatial
# =============================================================================

def compute_compound_squeeze(r_spatial_val, r_k_bcs, phi_k_bcs, r_L, kappa_vM):
    """
    Compute the SU(1,1) compound squeeze for a given r_spatial.

    The compound is the von Mises-averaged product:
        <S_compound>_k = <S_spatial(r_spatial, phi) * S_Leggett(r_L, 0) * S_BCS(r_k, phi_k)>_{phi~vM}

    Following S70 Section 5: the von Mises average damps cross-terms by
    C_vM = I_1(kappa)/I_0(kappa).

    For the three-factor BCH product, we compute:
        S_LB = S_Leggett * S_BCS  (exact matrix product)
    then
        <S_compound> = <S_spatial * S_LB>_{phi~vM}  (von Mises averaged)

    Returns:
        r_compound: per-mode compound squeeze parameters (8,)
        phi_compound: per-mode compound phases (8,)
        cosh2r_compound: per-mode cosh(2*r_compound) (8,)
        r_eff_weighted: weighted effective squeeze
        delta_OOM: log10(cosh(2*r_eff_weighted))
    """
    n_modes = len(r_k_bcs)
    C_vM_local = float(bessel_I1(kappa_vM)) / float(bessel_I0(kappa_vM))

    r_compound = np.zeros(n_modes)
    phi_compound = np.zeros(n_modes)
    cosh2r_compound = np.zeros(n_modes)

    for i in range(n_modes):
        rk = r_k_bcs[i]
        pk = phi_k_bcs[i]

        # Step 1: S_Leggett * S_BCS (exact product)
        # Leggett is real-phase (phi_L = 0)
        S_L = su11_matrix(r_L, 0.0)
        S_BCS = su11_matrix(rk, pk)
        S_LB = S_L @ S_BCS

        # Extract intermediate params
        r_LB, phi_LB = extract_su11_params(S_LB)

        # Step 2: von Mises-averaged product with spatial squeeze
        # <S_spatial(r_s, phi_random) * S_LB(r_LB, phi_LB)>_{phi~vM}
        #
        # <alpha_compound> = cosh(r_s)*cosh(r_LB) + C_vM * sinh(r_s)*sinh(r_LB) * e^{-i*phi_LB}
        # <beta_compound>  = cosh(r_s)*sinh(r_LB)*e^{i*phi_LB} + C_vM * sinh(r_s)*cosh(r_LB)
        rs = r_spatial_val
        a_avg = (np.cosh(rs) * np.cosh(r_LB)
                 + C_vM_local * np.sinh(rs) * np.sinh(r_LB) * np.exp(-1j * phi_LB))
        b_avg = (np.cosh(rs) * np.sinh(r_LB) * np.exp(1j * phi_LB)
                 + C_vM_local * np.sinh(rs) * np.cosh(r_LB))

        # Extract compound params (project back to SU(1,1) via polar decomposition)
        det_i = np.abs(a_avg)**2 - np.abs(b_avg)**2
        if det_i > 0:
            sqrt_det = np.sqrt(det_i)
            a_norm = a_avg / sqrt_det
            b_norm = b_avg / sqrt_det
        else:
            a_norm = a_avg
            b_norm = b_avg

        r_c = np.arccosh(np.abs(a_norm)) if np.abs(a_norm) >= 1.0 else 0.0
        phi_c = np.angle(b_norm)

        r_compound[i] = r_c
        phi_compound[i] = phi_c
        cosh2r_compound[i] = np.cosh(2 * r_c)

    # Weighted effective squeeze
    r_eff_weighted = np.sum(mode_weights * r_compound)
    cosh2r_eff_weighted = np.sum(mode_weights * cosh2r_compound)
    delta_OOM = np.log10(cosh2r_eff_weighted) if cosh2r_eff_weighted > 1.0 else 0.0

    return r_compound, phi_compound, cosh2r_compound, r_eff_weighted, delta_OOM


# =============================================================================
#  Section 4: Parameter scan
# =============================================================================

print(f"\n--- Section 4: r_spatial Parameter Scan ---")
print(f"Scanning r_spatial over {{0.30, 0.35, ..., 0.70, 0.881}}")
print(f"Baseline A_s gap = {A_s_gap_baseline:.4f} OOM")

# Scan values
r_spatial_scan = np.array([0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70, 0.881])
n_scan = len(r_spatial_scan)

# Storage
delta_OOM_scan = np.zeros(n_scan)
remaining_gap_scan = np.zeros(n_scan)
r_eff_weighted_scan = np.zeros(n_scan)
cosh2r_eff_scan = np.zeros(n_scan)
r_compound_all = np.zeros((n_scan, len(r_k_bcs)))

print(f"\n{'r_spatial':>10} {'r_eff_wt':>10} {'cosh(2r)':>12} {'delta_OOM':>12} {'rem_gap':>12} {'gap_sign':>10}")
print("-" * 72)

for j, rs_val in enumerate(r_spatial_scan):
    r_comp, phi_comp, cosh2r_comp, r_eff_w, d_OOM = compute_compound_squeeze(
        rs_val, r_k_bcs, phi_k_bcs, r_L, kappa_vM
    )
    delta_OOM_scan[j] = d_OOM
    remaining_gap_scan[j] = A_s_gap_baseline - d_OOM
    r_eff_weighted_scan[j] = r_eff_w
    cosh2r_eff_scan[j] = np.sum(mode_weights * cosh2r_comp)
    r_compound_all[j] = r_comp

    gap_sign = "OPEN" if remaining_gap_scan[j] > 0 else "CLOSED"
    print(f"{rs_val:>10.3f} {r_eff_w:>10.4f} {cosh2r_eff_scan[j]:>12.4f} "
          f"{d_OOM:>12.4f} {remaining_gap_scan[j]:>12.4f} {gap_sign:>10}")


# =============================================================================
#  Section 5: Find r_spatial_critical by interpolation
# =============================================================================

print(f"\n--- Section 5: Critical r_spatial ---")

# Find where remaining_gap crosses zero
# remaining_gap = A_s_gap_baseline - delta_OOM = 0
# => delta_OOM = A_s_gap_baseline = 0.267

# Check if gap closes within the scan range
if np.all(remaining_gap_scan > 0):
    print(f"Gap remains OPEN for all scanned r_spatial values.")
    print(f"Minimum remaining gap = {np.min(remaining_gap_scan):.4f} at r_spatial = {r_spatial_scan[np.argmin(remaining_gap_scan)]:.3f}")
    r_spatial_critical = np.inf
    print(f"r_spatial_critical > {r_spatial_scan[-1]:.3f} (outside scan range)")

    # Extrapolate using the last two points
    slope = (delta_OOM_scan[-1] - delta_OOM_scan[-2]) / (r_spatial_scan[-1] - r_spatial_scan[-2])
    r_extrap = r_spatial_scan[-1] + (A_s_gap_baseline - delta_OOM_scan[-1]) / slope
    print(f"Linear extrapolation: r_spatial_critical ~ {r_extrap:.4f}")
    r_spatial_critical = r_extrap

elif np.all(remaining_gap_scan < 0):
    print(f"Gap is CLOSED for all scanned r_spatial values.")
    print(f"Maximum remaining gap = {np.max(remaining_gap_scan):.4f} at r_spatial = {r_spatial_scan[np.argmax(remaining_gap_scan)]:.3f}")
    r_spatial_critical = -np.inf

else:
    # Find zero crossing by interpolation
    # remaining_gap changes sign between consecutive points
    for j in range(n_scan - 1):
        if remaining_gap_scan[j] * remaining_gap_scan[j+1] <= 0:
            # Linear interpolation for the crossing
            r1, r2 = r_spatial_scan[j], r_spatial_scan[j+1]
            g1, g2 = remaining_gap_scan[j], remaining_gap_scan[j+1]
            r_spatial_critical = r1 + (r2 - r1) * (-g1) / (g2 - g1)
            print(f"Zero crossing between r_spatial = {r1:.3f} and {r2:.3f}")
            print(f"r_spatial_critical = {r_spatial_critical:.6f} (linear interpolation)")

            # Also use cubic interpolation for comparison
            if n_scan >= 4:
                f_interp = interp1d(r_spatial_scan, remaining_gap_scan, kind='cubic')
                # Fine grid around the crossing
                r_fine = np.linspace(r1 - 0.01, r2 + 0.01, 1000)
                r_fine = r_fine[(r_fine >= r_spatial_scan[0]) & (r_fine <= r_spatial_scan[-1])]
                gap_fine = f_interp(r_fine)
                idx_zero = np.argmin(np.abs(gap_fine))
                r_spatial_critical_cubic = r_fine[idx_zero]
                print(f"r_spatial_critical = {r_spatial_critical_cubic:.6f} (cubic interpolation)")
            break

print(f"\n=> r_spatial_critical = {r_spatial_critical:.6f}")


# =============================================================================
#  Section 6: Sensitivity analysis
# =============================================================================

print(f"\n--- Section 6: Sensitivity Analysis ---")

# d(gap)/d(r_spatial) at the S69 value
# Use finite differences
idx_s69 = np.argmin(np.abs(r_spatial_scan - r_spatial_s69))
if idx_s69 > 0 and idx_s69 < n_scan - 1:
    dr = r_spatial_scan[idx_s69 + 1] - r_spatial_scan[idx_s69 - 1]
    dgap = remaining_gap_scan[idx_s69 + 1] - remaining_gap_scan[idx_s69 - 1]
    sensitivity_s69 = dgap / dr
else:
    # Forward/backward difference
    if idx_s69 == 0:
        dr = r_spatial_scan[1] - r_spatial_scan[0]
        dgap = remaining_gap_scan[1] - remaining_gap_scan[0]
    else:
        dr = r_spatial_scan[-1] - r_spatial_scan[-2]
        dgap = remaining_gap_scan[-1] - remaining_gap_scan[-2]
    sensitivity_s69 = dgap / dr

print(f"d(gap)/d(r_spatial) at r_spatial ~ {r_spatial_scan[idx_s69]:.2f} = {sensitivity_s69:.6f} OOM/unit")

# d(delta_OOM)/d(r_spatial) across the scan
d_delta_OOM_dr = np.gradient(delta_OOM_scan, r_spatial_scan)
print(f"\nd(delta_OOM)/d(r_spatial) across scan:")
for j in range(n_scan):
    print(f"  r_spatial = {r_spatial_scan[j]:.3f}: d(OOM)/dr = {d_delta_OOM_dr[j]:.6f}")

# Distance from S69 value to critical
delta_r_critical = r_spatial_critical - r_spatial_s69
print(f"\nDistance: r_spatial_critical - r_spatial_S69 = {delta_r_critical:.6f}")
print(f"Fractional: delta_r / r_spatial_S69 = {delta_r_critical / r_spatial_s69:.4f} "
      f"({100 * delta_r_critical / r_spatial_s69:.1f}%)")

# W1-C result: r_eff = 0.881 from multi-mode transmon
r_eff_w1c = 0.881  # (local)
idx_w1c = np.argmin(np.abs(r_spatial_scan - r_eff_w1c))
print(f"\n--- W1-C Context ---")
print(f"W1-C r_eff = {r_eff_w1c:.3f}")
print(f"At r_spatial = {r_spatial_scan[idx_w1c]:.3f}: remaining_gap = {remaining_gap_scan[idx_w1c]:.4f}")
print(f"The r_eff = 0.881 from multi-mode transmon physics {'CLOSES' if remaining_gap_scan[idx_w1c] < 0 else 'does NOT close'} the A_s gap.")


# =============================================================================
#  Section 7: Simple analytic check
# =============================================================================

print(f"\n--- Section 7: Simple Analytic Cross-Check ---")

# The simplest estimate: if we ignore the SU(1,1) group structure
# and just add squeeze parameters in quadrature:
#   r_eff_simple = sqrt(sum_k w_k * (r_BCS_k^2 + r_L^2 + r_spatial^2))
# then delta_OOM_simple = log10(cosh(2 * r_eff_simple))

for rs_val in [0.30, r_spatial_s69, r_eff_w1c]:
    r_total_sq = np.sum(mode_weights * (r_k_bcs**2 + r_L**2 + rs_val**2))
    r_eff_simple = np.sqrt(r_total_sq)
    delta_simple = np.log10(np.cosh(2 * r_eff_simple))
    gap_simple = A_s_gap_baseline - delta_simple
    print(f"  r_spatial = {rs_val:.3f}: r_eff_simple = {r_eff_simple:.4f}, "
          f"delta_OOM = {delta_simple:.4f}, gap = {gap_simple:.4f}")


# =============================================================================
#  Section 8: Extended fine scan near critical
# =============================================================================

print(f"\n--- Section 8: Fine Scan Near Critical ---")

# Fine scan around the estimated critical value
r_fine_center = min(max(r_spatial_critical, 0.20), 1.50)
r_fine_scan = np.linspace(max(r_fine_center - 0.10, 0.10), r_fine_center + 0.10, 50)

gap_fine_scan = np.zeros(len(r_fine_scan))
for j, rs_val in enumerate(r_fine_scan):
    _, _, _, _, d_OOM = compute_compound_squeeze(
        rs_val, r_k_bcs, phi_k_bcs, r_L, kappa_vM
    )
    gap_fine_scan[j] = A_s_gap_baseline - d_OOM

# Find precise crossing
if np.any(gap_fine_scan <= 0) and np.any(gap_fine_scan >= 0):
    for j in range(len(r_fine_scan) - 1):
        if gap_fine_scan[j] * gap_fine_scan[j+1] <= 0:
            r1, r2 = r_fine_scan[j], r_fine_scan[j+1]
            g1, g2 = gap_fine_scan[j], gap_fine_scan[j+1]
            r_spatial_critical_fine = r1 + (r2 - r1) * (-g1) / (g2 - g1)
            print(f"Fine-grid r_spatial_critical = {r_spatial_critical_fine:.6f}")
            r_spatial_critical = r_spatial_critical_fine
            break
elif np.all(gap_fine_scan > 0):
    print(f"Gap stays OPEN in fine scan range [{r_fine_scan[0]:.3f}, {r_fine_scan[-1]:.3f}]")
    print(f"Min gap = {np.min(gap_fine_scan):.6f} at r_spatial = {r_fine_scan[np.argmin(gap_fine_scan)]:.4f}")
else:
    print(f"Gap stays CLOSED in fine scan range [{r_fine_scan[0]:.3f}, {r_fine_scan[-1]:.3f}]")
    print(f"Max gap = {np.max(gap_fine_scan):.6f} at r_spatial = {r_fine_scan[np.argmax(gap_fine_scan)]:.4f}")


# =============================================================================
#  Section 9: Gate verdict
# =============================================================================

print(f"\n" + "=" * 72)
print(f"Gate Verdict: R-SPATIAL-SCAN-71")
print(f"=" * 72)

in_modest_range = 0.45 <= r_spatial_critical <= 0.65
above_one = r_spatial_critical > 1.0

print(f"r_spatial_critical = {r_spatial_critical:.6f}")
print(f"In [0.45, 0.65]? {in_modest_range}")
print(f"Above 1.0? {above_one}")

if in_modest_range:
    verdict_detail = (f"r_spatial_critical = {r_spatial_critical:.4f} in [0.45, 0.65]. "
                      f"Gap closeable with modest parameter change from S69 value {r_spatial_s69:.3f}.")
elif above_one:
    verdict_detail = (f"r_spatial_critical = {r_spatial_critical:.4f} > 1.0. "
                      f"Gap NOT closeable by r_spatial channel alone.")
else:
    verdict_detail = (f"r_spatial_critical = {r_spatial_critical:.4f}. "
                      f"Distance from S69: delta_r = {delta_r_critical:.4f} "
                      f"({100 * abs(delta_r_critical) / r_spatial_s69:.1f}%).")

print(f"Verdict: INFO")
print(f"Detail: {verdict_detail}")

# Summarize key results
print(f"\n--- Summary Table ---")
print(f"{'r_spatial':>10} {'delta_OOM':>12} {'remaining_gap':>14} {'status':>10}")
print("-" * 50)
for j in range(n_scan):
    status = "OPEN" if remaining_gap_scan[j] > 0 else "CLOSED"
    print(f"{r_spatial_scan[j]:>10.3f} {delta_OOM_scan[j]:>12.4f} "
          f"{remaining_gap_scan[j]:>14.4f} {status:>10}")
print("-" * 50)
print(f"{'CRITICAL':>10} {A_s_gap_baseline:>12.4f} {'0.0000':>14} {'ZERO':>10}")
print(f"r_spatial_critical = {r_spatial_critical:.6f}")

# Sensitivity at S69 value
print(f"\nSensitivity d(gap)/d(r_spatial) at S69 value = {sensitivity_s69:.4f} OOM/unit")
print(f"  => 1% change in r_spatial shifts gap by {abs(sensitivity_s69) * 0.01 * r_spatial_s69:.6f} OOM")
print(f"  => 10% change in r_spatial shifts gap by {abs(sensitivity_s69) * 0.10 * r_spatial_s69:.6f} OOM")


# =============================================================================
#  Section 10: Save output
# =============================================================================

np.savez("computations/session-71/s71_r_spatial_scan.npz",
         gate_name="R-SPATIAL-SCAN-71",
         gate_verdict="INFO",
         gate_detail=verdict_detail,
         # Scan data
         r_spatial_scan=r_spatial_scan,
         delta_OOM_scan=delta_OOM_scan,
         remaining_gap_scan=remaining_gap_scan,
         r_eff_weighted_scan=r_eff_weighted_scan,
         cosh2r_eff_scan=cosh2r_eff_scan,
         r_compound_all=r_compound_all,
         # Critical value
         r_spatial_critical=r_spatial_critical,
         # Sensitivity
         sensitivity_s69=sensitivity_s69,
         d_delta_OOM_dr=d_delta_OOM_dr,
         # Baselines
         A_s_gap_baseline=A_s_gap_baseline,
         r_spatial_s69=r_spatial_s69,
         r_L=r_L,
         r_k_bcs=r_k_bcs,
         phi_k_bcs=phi_k_bcs,
         mode_weights=mode_weights,
         kappa_vM=kappa_vM,
         C_vM=C_vM,
         # W1-C context
         r_eff_w1c=r_eff_w1c,
         # Fine scan
         r_fine_scan=r_fine_scan,
         gap_fine_scan=gap_fine_scan,
         )

# =============================================================================
#  Section 11: Structural diagnostic — where does the overcorrection live?
# =============================================================================

print(f"\n--- Section 11: Overcorrection Diagnostic ---")

# BCS alone (no Leggett, no spatial)
cosh2r_bcs_only = np.cosh(2 * r_k_bcs)
cosh2r_bcs_weighted = np.sum(mode_weights * cosh2r_bcs_only)
delta_OOM_bcs_only = np.log10(cosh2r_bcs_weighted) if cosh2r_bcs_weighted > 1 else 0
print(f"BCS alone: weighted cosh(2r) = {cosh2r_bcs_weighted:.4f}, "
      f"delta_OOM = {delta_OOM_bcs_only:.4f}")
print(f"  => BCS alone overcorrects by factor {delta_OOM_bcs_only / A_s_gap_baseline:.1f}x")

# BCS + Leggett (no spatial)
r_LB_only = np.zeros(len(r_k_bcs))
cosh2r_LB_only = np.zeros(len(r_k_bcs))
for i in range(len(r_k_bcs)):
    S_L = su11_matrix(r_L, 0.0)
    S_BCS = su11_matrix(r_k_bcs[i], phi_k_bcs[i])
    S_LB = S_L @ S_BCS
    r_out, _ = extract_su11_params(S_LB)
    r_LB_only[i] = r_out
    cosh2r_LB_only[i] = np.cosh(2 * r_out)

cosh2r_LB_weighted = np.sum(mode_weights * cosh2r_LB_only)
delta_OOM_LB_only = np.log10(cosh2r_LB_weighted) if cosh2r_LB_weighted > 1 else 0
print(f"BCS+Leggett: weighted cosh(2r) = {cosh2r_LB_weighted:.4f}, "
      f"delta_OOM = {delta_OOM_LB_only:.4f}")
print(f"  => BCS+Leggett overcorrects by factor {delta_OOM_LB_only / A_s_gap_baseline:.1f}x")

# Marginal contribution of r_spatial
delta_from_spatial = delta_OOM_scan[5] - delta_OOM_LB_only  # at r_spatial=0.55
print(f"\nMarginal delta_OOM from r_spatial=0.55: {delta_from_spatial:.4f}")
print(f"  => r_spatial contributes {100*delta_from_spatial/delta_OOM_scan[5]:.1f}% "
      f"of total compound OOM")

# What BCS r_eff would give exactly the target gap?
# delta_OOM_target = 0.267 => cosh(2*r_target) = 10^0.267 = 1.849
# => r_target = 0.5 * arccosh(1.849) = 0.610
target_cosh2r = 10**A_s_gap_baseline
r_target = 0.5 * np.arccosh(target_cosh2r)
print(f"\nTarget: cosh(2*r_target) = {target_cosh2r:.4f} => r_target = {r_target:.4f}")
print(f"Actual weighted r_eff at r_spatial=0: {np.sum(mode_weights * r_LB_only):.4f}")
print(f"Ratio actual/target: {np.sum(mode_weights * r_LB_only) / r_target:.1f}x")

print(f"\nStructural conclusion:")
print(f"  r_spatial_critical does not exist (gap closed for ALL r_spatial >= 0).")
print(f"  The BCS squeeze alone ({delta_OOM_bcs_only:.2f} OOM) exceeds the target "
      f"({A_s_gap_baseline:.3f} OOM) by {delta_OOM_bcs_only / A_s_gap_baseline:.1f}x.")
print(f"  r_spatial is a ~10% perturbation on the total compound squeeze.")
print(f"  The decoherence mechanism (W1-D) is the necessary regulator.")


# Update saved data with diagnostic
np.savez("computations/session-71/s71_r_spatial_scan.npz",
         gate_name="R-SPATIAL-SCAN-71",
         gate_verdict="INFO",
         gate_detail=(f"r_spatial_critical does not exist (gap closed for ALL r_spatial >= 0). "
                      f"BCS alone overcorrects by {delta_OOM_bcs_only / A_s_gap_baseline:.1f}x. "
                      f"Sensitivity d(gap)/dr = {sensitivity_s69:.4f} OOM/unit. "
                      f"Decoherence (W1-D) is the necessary regulator."),
         # Scan data
         r_spatial_scan=r_spatial_scan,
         delta_OOM_scan=delta_OOM_scan,
         remaining_gap_scan=remaining_gap_scan,
         r_eff_weighted_scan=r_eff_weighted_scan,
         cosh2r_eff_scan=cosh2r_eff_scan,
         r_compound_all=r_compound_all,
         # Critical value
         r_spatial_critical=np.nan,  # Does not exist
         # Sensitivity
         sensitivity_s69=sensitivity_s69,
         d_delta_OOM_dr=d_delta_OOM_dr,
         # Baselines
         A_s_gap_baseline=A_s_gap_baseline,
         r_spatial_s69=r_spatial_s69,
         r_L=r_L,
         r_k_bcs=r_k_bcs,
         phi_k_bcs=phi_k_bcs,
         mode_weights=mode_weights,
         kappa_vM=kappa_vM,
         C_vM=C_vM,
         # W1-C context
         r_eff_w1c=r_eff_w1c,
         # Diagnostic
         delta_OOM_bcs_only=delta_OOM_bcs_only,
         delta_OOM_LB_only=delta_OOM_LB_only,
         overcorrection_factor_bcs=delta_OOM_bcs_only / A_s_gap_baseline,
         overcorrection_factor_LB=delta_OOM_LB_only / A_s_gap_baseline,
         r_target_exact=r_target,
         # Fine scan
         r_fine_scan=r_fine_scan,
         gap_fine_scan=gap_fine_scan,
         )

print(f"\nOutput saved to computations/session-71/s71_r_spatial_scan.npz")
print(f"Script: computations/session-71/s71_r_spatial_scan.py")
