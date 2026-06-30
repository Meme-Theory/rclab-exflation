#!/usr/bin/env python3
"""
S58 MASS-VARIATION-58: Paper 16 eq 7.1 Mass Variation Integral
==============================================================

Paper 16 (Baptista 2024, arXiv:2406.09503) Section 7:
  c^2 d/ds m^2(s) = -(d_A g_K)_{dot gamma_M}(p_V, p_V)

For the cosmological transit (no gauge fields, A=0), the covariant
derivative reduces to the Lie derivative along spacetime:
  (d_A g_K)_X(U,V) = (L_X g_K)(U,V)

For the Jensen family g_K(tau) = diag(alpha*e^{2tau}, alpha*e^{-2tau},
alpha*e^{-2tau}, alpha*e^{-2tau}, alpha*e^{tau}, alpha*e^{tau},
alpha*e^{tau}, alpha*e^{tau}) on the decomposition
u(1) + su(2) + C^2 (dims 1+3+4 = 8):

  tr(g_K^{-1} dg_K/dtau) = 1*2 + 3*(-2) + 4*1 = 2 - 6 + 4 = 0

This VANISHES identically because the Jensen deformation is volume-preserving
(det g_K = const). This is the trace formula from the task spec.

HOWEVER: the trace vanishing means the AVERAGE mass is preserved, but
individual representation masses change because their Casimir eigenvalues
couple differently to the three metric directions. The physical mass
variation must be computed per-representation.

This script computes:
1. The analytic trace tr(g_K^{-1} dg_K/dtau) = 0 (verification)
2. Per-representation mass variation from the Dirac/Laplacian eigenvalues
3. Representation-weighted fractional mass shift delta_m/m
4. DM-relevant mass shift (B2 sector, the BCS condensate)

Gate: MASS-VARIATION-58 (INFO) -- dm/dtau changes DM prediction by > 10%?

Author: baptista-spacetime-analyst
Session: 58
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import *
import numpy as np
from scipy.integrate import trapezoid
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

print("=" * 80)
print("S58 MASS-VARIATION-58: Paper 16 eq 7.1 Mass Variation Integral")
print("=" * 80)

# =============================================================================
# PART 1: Jensen Metric and Analytic Trace
# =============================================================================

print("\n--- Part 1: Analytic Trace of g_K^{-1} dg_K/dtau ---")

# Jensen metric scales on the three Ad(U(2))-invariant directions
# u(1): dim 1, scale e^{2s}
# su(2): dim 3, scale e^{-2s}
# C^2: dim 4, scale e^{s}

def jensen_scales(s):
    """Return (x1, x2, x3) and their multiplicities (1, 3, 4)."""
    x1 = np.exp(2.0 * s)     # u(1) direction
    x2 = np.exp(-2.0 * s)    # su(2) direction (x3)
    x3 = np.exp(1.0 * s)     # C^2 direction (x4)
    return x1, x2, x3

def d_ln_scales(s):
    """Return d/ds ln(x_i) for each direction."""
    # d/ds ln(e^{2s}) = 2
    # d/ds ln(e^{-2s}) = -2
    # d/ds ln(e^{s}) = 1
    return 2.0, -2.0, 1.0

# Multiplicities
mult = np.array([1, 3, 4])  # u(1), su(2), C^2

# Trace: sum_i mult_i * d(ln x_i)/ds
d_ln = np.array(d_ln_scales(0.0))  # constant in s (exponential scales)
trace_gK_inv_dgK = np.sum(mult * d_ln)

print(f"  d(ln x_1)/dtau = {d_ln[0]:+.1f}  (u(1), mult=1)")
print(f"  d(ln x_2)/dtau = {d_ln[1]:+.1f}  (su(2), mult=3)")
print(f"  d(ln x_3)/dtau = {d_ln[2]:+.1f}  (C^2, mult=4)")
print(f"  tr(g_K^{{-1}} dg_K/dtau) = 1*({d_ln[0]:+.0f}) + 3*({d_ln[1]:+.0f}) + 4*({d_ln[2]:+.0f})")
print(f"                           = {trace_gK_inv_dgK:.1f}")
print(f"  --> EXACTLY ZERO (volume-preserving Jensen deformation)")

# Volume verification at multiple tau
print(f"\n  Volume preservation check:")
for s_test in [0.0, 0.1, 0.19, 0.3, 0.5]:
    x1, x2, x3 = jensen_scales(s_test)
    vol = x1**1 * x2**3 * x3**4
    print(f"    tau={s_test:.2f}: det(g_K)/det(g_K(0)) = {vol:.12f}  (should be 1.0)")

# =============================================================================
# PART 2: The Naive Trace Formula (Task Spec) is Zero
# =============================================================================

print("\n--- Part 2: Naive Trace Formula from Task Spec ---")
print("  dm/dtau = m * tr(g_K^{-1} dg_K/dtau) / (2*(d_K+4))")
print(f"  d_K = dim(SU(3)) = 8")
print(f"  2*(d_K + 4) = 2*12 = 24")
print(f"  tr(g_K^{{-1}} dg_K/dtau) = 0  (proven above)")
print(f"  --> dm/dtau = 0 for ANY m, at ANY tau")
print(f"  --> delta_m/m = 0 identically")
print(f"\n  STRUCTURAL RESULT: The naive trace formula gives ZERO mass variation")
print(f"  because the Jensen deformation is volume-preserving.")
print(f"  This is a consequence of det(g_K) = const => tr(g_K^{{-1}} dg_K/dtau) = 0.")

# =============================================================================
# PART 3: Per-Representation Mass Variation (Physical)
# =============================================================================

print("\n--- Part 3: Per-Representation Mass Variation from Eigenvalues ---")

# Load the s54 tight-binding Hamiltonian data
data = np.load(os.path.join(os.path.dirname(__file__), 's54_tb_hamiltonian.npz'),
               allow_pickle=True)
tau_values = data['tau_values']   # (50,)
eigenvalues = data['eigenvalues'] # (50, 32)
cell_labels = data['cell_labels'] # (32, 2) -- (p,q) for each cell
cell_dims = data['cell_dims']     # (32,)
cell_casimirs = data['cell_casimirs']  # (32,)

N_tau = len(tau_values)
N_cells = eigenvalues.shape[1]

print(f"  Loaded: {N_tau} tau values, {N_cells} cells")
print(f"  tau range: [{tau_values[0]:.4f}, {tau_values[-1]:.4f}]")

# Identify key cells by (p,q) label
# B1 = (0,0): trivial, dim=1
# B2 = (1,1): adjoint, dim=8 -- the BCS condensate sector
# B3 = (1,0) and (0,1): fundamental, dim=3 each

cell_names = {}
for i in range(N_cells):
    p, q = cell_labels[i]
    cell_names[i] = f"({p},{q})"

# Find B1, B2, B3 indices
B1_idx = None
B2_idx = None
B3_10_idx = None  # (1,0)
B3_01_idx = None  # (0,1)

for i in range(N_cells):
    p, q = cell_labels[i]
    if p == 0 and q == 0:
        B1_idx = i
    elif p == 1 and q == 1:
        B2_idx = i
    elif p == 1 and q == 0:
        B3_10_idx = i
    elif p == 0 and q == 1:
        B3_01_idx = i

print(f"\n  Key cells:")
print(f"    B1 = ({cell_labels[B1_idx,0]},{cell_labels[B1_idx,1]}), "
      f"idx={B1_idx}, dim={cell_dims[B1_idx]}, C2={cell_casimirs[B1_idx]:.4f}")
print(f"    B2 = ({cell_labels[B2_idx,0]},{cell_labels[B2_idx,1]}), "
      f"idx={B2_idx}, dim={cell_dims[B2_idx]}, C2={cell_casimirs[B2_idx]:.4f}")
print(f"    B3(1,0) = idx={B3_10_idx}, dim={cell_dims[B3_10_idx]}, C2={cell_casimirs[B3_10_idx]:.4f}")
print(f"    B3(0,1) = idx={B3_01_idx}, dim={cell_dims[B3_01_idx]}, C2={cell_casimirs[B3_01_idx]:.4f}")

# Per-cell mass variation: m(tau) = sqrt(eigenvalue(tau)) for each cell
# But eigenvalue[0] for (0,0) is ~0 (zero mode), skip it for ratios

# For each cell, compute:
#   fractional_mass_change = [m(tau_final) - m(tau_initial)] / m(tau_initial)
# where m ~ sqrt(eigenvalue) for each representation

# Also compute the continuous dm/dtau

# Eigenvalues represent E(tau) for each cell. In the KK picture, m^2 ~ E.
# So m(tau) ~ sqrt(E(tau)).

# Skip cell 0 (B1 = zero mode, eigenvalue ~ 0)
print(f"\n  Per-representation mass evolution:")
print(f"  {'Cell':>8s} {'(p,q)':>6s} {'dim':>4s} {'E(0)':>10s} {'E(0.19)':>10s} {'E(0.5)':>10s} "
      f"{'dE/E(0->fold)':>14s} {'dE/E(0->0.5)':>14s}")

# Find fold index (tau closest to 0.19)
fold_idx = np.argmin(np.abs(tau_values - tau_fold))
print(f"  (fold at tau={tau_values[fold_idx]:.4f}, idx={fold_idx})")

mass_changes_fold = np.zeros(N_cells)
mass_changes_full = np.zeros(N_cells)

for i in range(N_cells):
    E_0 = eigenvalues[0, i]
    E_fold = eigenvalues[fold_idx, i]
    E_end = eigenvalues[-1, i]

    if E_0 > 1e-10:  # skip zero mode
        dE_fold = (E_fold - E_0) / E_0
        dE_end = (E_end - E_0) / E_0
        mass_changes_fold[i] = dE_fold
        mass_changes_full[i] = dE_end
    else:
        mass_changes_fold[i] = np.nan
        mass_changes_full[i] = np.nan

    if i < 12:  # Print first 12 cells
        p, q = cell_labels[i]
        print(f"  {i:>8d} ({p},{q}){' ':>2s} {cell_dims[i]:>4d} {E_0:>10.6f} {E_fold:>10.6f} "
              f"{E_end:>10.6f} {mass_changes_fold[i]:>+14.6f} {mass_changes_full[i]:>+14.6f}")

# =============================================================================
# PART 4: Weighted Mass Variation (DM-relevant)
# =============================================================================

print("\n--- Part 4: DM-Relevant Mass Variation ---")

# The DM candidate in this framework is the BCS condensate in the B2 sector
# (adjoint representation (1,1), dim=8).
# The GGE quasiparticle relic is the DM carrier.

# B2 mass evolution
E_B2 = eigenvalues[:, B2_idx]
m_B2 = np.sqrt(np.abs(E_B2))  # mass ~ sqrt(eigenvalue)

# dm/dtau via numerical derivative
dm_B2_dtau = np.gradient(m_B2, tau_values)

# Fractional mass change dm/m
dm_over_m_B2 = dm_B2_dtau / m_B2

print(f"\n  B2 (adjoint, dim=8) mass evolution:")
print(f"    m_B2(0) = {m_B2[0]:.6f}  (M_KK units)")
print(f"    m_B2(fold) = {m_B2[fold_idx]:.6f}")
print(f"    m_B2(0.5) = {m_B2[-1]:.6f}")
print(f"    delta_m/m (0 -> fold) = {(m_B2[fold_idx] - m_B2[0])/m_B2[0]:+.6f}")
print(f"    delta_m/m (0 -> 0.5) = {(m_B2[-1] - m_B2[0])/m_B2[0]:+.6f}")

delta_m_over_m_B2_fold = (m_B2[fold_idx] - m_B2[0]) / m_B2[0]
delta_m_over_m_B2_full = (m_B2[-1] - m_B2[0]) / m_B2[0]

# B3 mass evolution (fundamental reps)
E_B3_10 = eigenvalues[:, B3_10_idx]
E_B3_01 = eigenvalues[:, B3_01_idx]
m_B3_10 = np.sqrt(np.abs(E_B3_10))
m_B3_01 = np.sqrt(np.abs(E_B3_01))

print(f"\n  B3(1,0) mass evolution:")
print(f"    m(0) = {m_B3_10[0]:.6f}, m(fold) = {m_B3_10[fold_idx]:.6f}, m(0.5) = {m_B3_10[-1]:.6f}")
print(f"    delta_m/m (0 -> fold) = {(m_B3_10[fold_idx] - m_B3_10[0])/m_B3_10[0]:+.6f}")

print(f"\n  B3(0,1) mass evolution:")
print(f"    m(0) = {m_B3_01[0]:.6f}, m(fold) = {m_B3_01[fold_idx]:.6f}, m(0.5) = {m_B3_01[-1]:.6f}")
print(f"    delta_m/m (0 -> fold) = {(m_B3_01[fold_idx] - m_B3_01[0])/m_B3_01[0]:+.6f}")

# =============================================================================
# PART 5: Integral Form of Mass Variation
# =============================================================================

print("\n--- Part 5: Integral Form ---")

# The Paper 16 mass variation for a particle in rep R with internal
# eigenvalue lambda_R(tau) gives:
#
#   m^2(tau) = lambda_R(tau) * m^2_KK
#
# so dm^2/m^2 = d(lambda_R)/lambda_R.
#
# The INTEGRATED fractional mass-squared change is:
#   delta(m^2)/m^2 = integral_0^{tau_f} (1/lambda_R) * (dlambda_R/dtau) dtau
#                  = ln(lambda_R(tau_f)) - ln(lambda_R(0))
#
# This is exact (no approximation needed for the integral).

print(f"\n  Integrated ln(m^2) change for each key cell:")
print(f"  (This equals integral_0^tau_f d(ln lambda)/dtau dtau)")

for idx, name in [(B2_idx, "B2(1,1)"), (B3_10_idx, "B3(1,0)"),
                   (B3_01_idx, "B3(0,1)")]:
    E_0 = eigenvalues[0, idx]
    E_fold = eigenvalues[fold_idx, idx]
    E_end = eigenvalues[-1, idx]
    if E_0 > 1e-10:
        ln_ratio_fold = np.log(E_fold / E_0)
        ln_ratio_full = np.log(E_end / E_0)
        # dm/m = (1/2) * d(ln m^2) = (1/2) * d(ln E)
        dm_m_fold = 0.5 * ln_ratio_fold
        dm_m_full = 0.5 * ln_ratio_full
        print(f"    {name}: ln(E_fold/E_0) = {ln_ratio_fold:+.6f}, "
              f"ln(E_0.5/E_0) = {ln_ratio_full:+.6f}")
        print(f"    {' ':>8s}  delta_m/m(fold) = {dm_m_fold:+.6f}, "
              f"delta_m/m(0.5) = {dm_m_full:+.6f}")

# =============================================================================
# PART 6: Continuous dm/dtau Profile (Paper 16 eq 7.1 Decomposition)
# =============================================================================

print("\n--- Part 6: Continuous dm/dtau Decomposition ---")

# For each direction (u(1), su(2), C^2), the contribution to dm^2/dtau
# for a given representation R is:
#
#   dm^2/dtau|_direction = -p_V^2(direction) * d(ln g_ii)/dtau
#
# where p_V^2(direction) is the internal momentum squared projected onto
# that direction.
#
# For a representation (p,q), the Casimir C_2(p,q) = (p^2 + pq + q^2 + 3p + 3q)/3
# governs the total internal kinetic energy. The DECOMPOSITION into u(1), su(2),
# C^2 directions depends on the representation structure.
#
# The Jensen deformation acts as:
#   d(ln g)/dtau on u(1): +2
#   d(ln g)/dtau on su(2): -2
#   d(ln g)/dtau on C^2: +1
#
# The mass variation for a representation with internal momentum components
# (p_u1, p_su2, p_C2) is:
#   d(m^2)/dtau = -[2*p_u1^2 - 2*p_su2^2 + 1*p_C2^2]
#               = -2*p_u1^2 + 2*p_su2^2 - p_C2^2
#
# The trace-zero condition means: sum over ALL reps (weighted) gives zero net change.
# But individual reps can have large shifts.

# Numerical verification: compute d(eigenvalue)/dtau for each cell
dE_dtau = np.gradient(eigenvalues, tau_values, axis=0)  # (50, 32)

# Fractional rate: (1/E) dE/dtau
frac_rate = np.zeros_like(dE_dtau)
for i in range(N_cells):
    mask = eigenvalues[:, i] > 1e-10
    frac_rate[mask, i] = dE_dtau[mask, i] / eigenvalues[mask, i]
    frac_rate[~mask, i] = np.nan

# Weighted trace (should be zero if volume-preserving)
# Weight by dim^2 (Peter-Weyl weight) * eigenvalue
weighted_trace = np.zeros(N_tau)
total_weight = np.zeros(N_tau)
for i in range(N_cells):
    w = cell_dims[i]**2  # Peter-Weyl weight
    mask = eigenvalues[:, i] > 1e-10
    weighted_trace[mask] += w * dE_dtau[mask, i]
    total_weight[mask] += w * eigenvalues[mask, i]

# The weighted fractional rate
wfr = np.divide(weighted_trace, total_weight, where=total_weight > 0,
                out=np.zeros(N_tau))

print(f"\n  Weighted trace (dim^2-weighted sum of dE/dtau):")
print(f"    At tau=0:    {wfr[0]:+.6e}")
print(f"    At tau=fold: {wfr[fold_idx]:+.6e}")
print(f"    At tau=0.5:  {wfr[-1]:+.6e}")
print(f"    Max |wfr|:   {np.nanmax(np.abs(wfr)):.6e}")

# The fact that this is NOT zero (unlike the analytic trace) is because
# the tight-binding Hamiltonian eigenvalues are NOT simply Casimir eigenvalues
# times metric scales. The inter-cell hopping modifies the spectrum.

# =============================================================================
# PART 7: DM Prediction Impact
# =============================================================================

print("\n--- Part 7: DM Prediction Impact ---")

# The DM prediction depends on:
# 1. m_DM ~ M_KK * sqrt(eigenvalue) at the post-transit value
# 2. Omega_DM ~ (n_DM * m_DM) / rho_crit
#
# The mass variation during transit affects m_DM through:
#   delta(m_DM)/m_DM = (1/2) * delta(E)/E
#
# where E is the eigenvalue of the relevant representation.

# Compute for ALL cells
print(f"\n  Fractional mass change |delta_m/m| for all cells (0 -> 0.5):")
print(f"  {'idx':>4s} {'(p,q)':>6s} {'dim':>4s} {'|delta_m/m|':>12s} {'>10%?':>6s}")

cells_above_10pct = 0
for i in range(N_cells):
    E_0 = eigenvalues[0, i]
    E_end = eigenvalues[-1, i]
    if E_0 > 1e-10:
        dm_m = abs(0.5 * np.log(E_end / E_0))
        above = dm_m > 0.10
        if above:
            cells_above_10pct += 1
        p, q = cell_labels[i]
        flag = "YES" if above else "no"
        print(f"  {i:>4d} ({p},{q}){' ':>2s} {cell_dims[i]:>4d} {dm_m:>12.6f} {flag:>6s}")

# Key DM cell: B2
E_B2_0 = eigenvalues[0, B2_idx]
E_B2_end = eigenvalues[-1, B2_idx]
dm_m_B2_exact = abs(0.5 * np.log(E_B2_end / E_B2_0))

print(f"\n  DM-critical B2 sector:")
print(f"    |delta_m/m|_B2 (0 -> 0.5) = {dm_m_B2_exact:.6f}")
print(f"    |delta_m/m|_B2 (0 -> fold) = {abs(0.5 * np.log(eigenvalues[fold_idx, B2_idx] / E_B2_0)):.6f}")
print(f"    Exceeds 10%? {'YES' if dm_m_B2_exact > 0.10 else 'NO'}")

# Also check from fold to end (post-transit)
E_B2_fold = eigenvalues[fold_idx, B2_idx]
dm_m_B2_post = abs(0.5 * np.log(E_B2_end / E_B2_fold))
print(f"    |delta_m/m|_B2 (fold -> 0.5) = {dm_m_B2_post:.6f}")

# =============================================================================
# PART 8: Comparison of Trace Formula vs Actual
# =============================================================================

print("\n--- Part 8: Trace Formula vs Actual ---")

# The task spec formula: dm/dtau = m * tr(g_K^{-1} dg_K/dtau) / (2*(d_K+4))
# gives ZERO for volume-preserving Jensen.
#
# The ACTUAL per-representation mass variation is NON-ZERO because:
# 1. Individual eigenvalues shift (some up, some down)
# 2. The tight-binding hopping integrals break the simple Casimir structure
# 3. The trace only constrains the SUM, not individual terms
#
# Physical interpretation: the Jensen deformation redistributes internal
# kinetic energy between the u(1), su(2), and C^2 directions while
# preserving the total volume. This is an anisotropic distortion that
# changes individual masses while preserving a weighted average.

d_K = 8  # dim(SU(3))
denominator = 2.0 * (d_K + 4)  # = 24

trace_formula_dm = trace_gK_inv_dgK / denominator  # = 0

print(f"  Task spec formula: dm/dtau = m * {trace_gK_inv_dgK:.1f} / {denominator:.0f} = 0")
print(f"  Actual B2 mass shift (0->0.5): {dm_m_B2_exact:+.6f}")
print(f"  Actual B2 mass shift (0->fold): {abs(0.5 * np.log(E_B2_fold / E_B2_0)):+.6f}")
print(f"\n  The trace formula is ZERO by construction (volume-preserving).")
print(f"  Individual representation masses change by {dm_m_B2_exact*100:.1f}% (B2)")
print(f"  to {np.nanmax(np.abs(mass_changes_full))*50:.1f}% (largest cell) over the full transit.")

# Maximum absolute mass change across all cells
valid_mask = ~np.isnan(mass_changes_full)
max_abs_change = np.max(np.abs(mass_changes_full[valid_mask]))
max_cell = np.argmax(np.abs(mass_changes_full * valid_mask.astype(float)))

print(f"\n  Maximum |delta_E/E| across all cells: {max_abs_change:.6f} at cell {max_cell} "
      f"({cell_labels[max_cell,0]},{cell_labels[max_cell,1]})")
print(f"  Maximum |delta_m/m|: {0.5*max_abs_change:.6f}")

# =============================================================================
# PART 9: Summary Table
# =============================================================================

print("\n--- Part 9: Summary ---")

# Compute delta_m/m for representative cells using exact log formula
summary_cells = [
    (B2_idx, "B2(1,1)_adjoint"),
    (B3_10_idx, "B3(1,0)_fund"),
    (B3_01_idx, "B3(0,1)_fund"),
]

# Add a few higher reps
for i in range(N_cells):
    p, q = cell_labels[i]
    if (p, q) in [(0, 2), (2, 0), (1, 2), (2, 2)]:
        summary_cells.append((i, f"({p},{q})"))

print(f"\n  {'Cell':>20s} | {'delta_m/m (0->fold)':>20s} | {'delta_m/m (0->0.5)':>20s} | {'>10%':>5s}")
print(f"  {'-'*20}-+-{'-'*20}-+-{'-'*20}-+-{'-'*5}")

for idx, name in summary_cells:
    E_0 = eigenvalues[0, idx]
    E_fold = eigenvalues[fold_idx, idx]
    E_end = eigenvalues[-1, idx]
    if E_0 > 1e-10:
        dm_fold = 0.5 * np.log(E_fold / E_0)
        dm_end = 0.5 * np.log(E_end / E_0)
        flag = "YES" if abs(dm_end) > 0.10 else "no"
        print(f"  {name:>20s} | {dm_fold:>+20.6f} | {dm_end:>+20.6f} | {flag:>5s}")

# =============================================================================
# GATE VERDICT
# =============================================================================

print("\n" + "=" * 80)
print("GATE VERDICT: MASS-VARIATION-58")
print("=" * 80)

print(f"\n  1. Naive trace formula: dm/dtau = m * tr(g_K^{{-1}} dg_K/dtau) / (2*(d_K+4))")
print(f"     tr(g_K^{{-1}} dg_K/dtau) = 0 EXACTLY (volume-preserving Jensen)")
print(f"     --> Trace formula gives ZERO mass variation at all tau")
print(f"\n  2. Actual per-representation mass variation (from eigenvalue evolution):")
print(f"     B2 (DM sector): |delta_m/m| = {dm_m_B2_exact:.6f} over [0, 0.5]")
print(f"     B2 (DM sector): |delta_m/m| = {abs(0.5 * np.log(E_B2_fold / E_B2_0)):.6f} over [0, fold]")

gate_threshold = 0.10  # (local)
gate_pass = dm_m_B2_exact > gate_threshold

if gate_pass:
    verdict = "INFO: YES — B2 mass varies by > 10%"
else:
    verdict = "INFO: NO — B2 mass varies by < 10%"

print(f"\n  Gate criterion: |delta_m/m|_B2 > 10%?")
print(f"  Answer: |delta_m/m|_B2 = {dm_m_B2_exact:.4f} = {dm_m_B2_exact*100:.1f}%")
print(f"  VERDICT: {verdict}")

print(f"\n  PHYSICAL INTERPRETATION:")
print(f"  The volume-preserving Jensen deformation has tr(g_K^{{-1}} dg_K/dtau) = 0")
print(f"  identically, so the Paper 16 eq 7.1 trace formula gives zero mass variation.")
print(f"  This is a STRUCTURAL constraint: any volume-preserving internal deformation")
print(f"  preserves the weighted-average mass.")
print(f"")
print(f"  Individual representation masses DO shift (anisotropic redistribution),")
print(f"  but the B2 sector (DM carrier) shift of {dm_m_B2_exact*100:.1f}% is {'above' if gate_pass else 'below'}")
print(f"  the 10% threshold for DM prediction significance.")
print(f"")
print(f"  IMPORTANT CAVEAT: These are tight-binding eigenvalues, not Dirac eigenvalues.")
print(f"  The Dirac operator eigenvalues may show different mass variation because")
print(f"  the Dirac spectrum depends on the FULL metric (including off-diagonal terms),")
print(f"  not just the Casimir weights. The tight-binding approximation captures the")
print(f"  leading behavior but may miss sub-leading corrections.")

# =============================================================================
# PLOTS
# =============================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Plot 1: Eigenvalue evolution for key cells
ax = axes[0, 0]
for idx, name, color in [(B2_idx, "B2(1,1)", "red"),
                          (B3_10_idx, "B3(1,0)", "blue"),
                          (B3_01_idx, "B3(0,1)", "green")]:
    ax.plot(tau_values, eigenvalues[:, idx], label=name, color=color, linewidth=2)
ax.axvline(tau_fold, color='gray', linestyle='--', alpha=0.5, label=f'fold (tau={tau_fold})')
ax.set_xlabel('tau')
ax.set_ylabel('Eigenvalue E(tau)')
ax.set_title('Key Cell Eigenvalue Evolution')
ax.legend()
ax.grid(True, alpha=0.3)

# Plot 2: Fractional mass change dm/m
ax = axes[0, 1]
for idx, name, color in [(B2_idx, "B2(1,1)", "red"),
                          (B3_10_idx, "B3(1,0)", "blue"),
                          (B3_01_idx, "B3(0,1)", "green")]:
    E = eigenvalues[:, idx]  # (local)
    dm_m = 0.5 * np.log(E / E[0])
    ax.plot(tau_values, dm_m, label=name, color=color, linewidth=2)
ax.axvline(tau_fold, color='gray', linestyle='--', alpha=0.5)
ax.axhline(0.10, color='orange', linestyle=':', alpha=0.7, label='10% threshold')
ax.axhline(-0.10, color='orange', linestyle=':', alpha=0.7)
ax.set_xlabel('tau')
ax.set_ylabel('delta_m / m')
ax.set_title('Fractional Mass Change (exact log)')
ax.legend()
ax.grid(True, alpha=0.3)

# Plot 3: dm/dtau rate for B2
ax = axes[1, 0]
for idx, name, color in [(B2_idx, "B2(1,1)", "red"),
                          (B3_10_idx, "B3(1,0)", "blue"),
                          (B3_01_idx, "B3(0,1)", "green")]:
    E = eigenvalues[:, idx]  # (local)
    dE = np.gradient(E, tau_values)
    rate = 0.5 * dE / E
    ax.plot(tau_values, rate, label=name, color=color, linewidth=2)
ax.axvline(tau_fold, color='gray', linestyle='--', alpha=0.5)
ax.axhline(0, color='black', linewidth=0.5)
ax.set_xlabel('tau')
ax.set_ylabel('(1/m) dm/dtau')
ax.set_title('Mass Variation Rate (Paper 16 eq 7.1)')
ax.legend()
ax.grid(True, alpha=0.3)

# Plot 4: All cells mass variation at tau=0.5
ax = axes[1, 1]
dm_m_all = []
labels_all = []
for i in range(N_cells):
    E_0 = eigenvalues[0, i]
    E_end = eigenvalues[-1, i]
    if E_0 > 1e-10:
        dm_m_all.append(0.5 * np.log(E_end / E_0))
        p, q = cell_labels[i]
        labels_all.append(f"({p},{q})")

colors = ['red' if abs(v) > 0.10 else 'steelblue' for v in dm_m_all]
ax.barh(range(len(dm_m_all)), dm_m_all, color=colors)
ax.set_yticks(range(len(dm_m_all)))
ax.set_yticklabels(labels_all, fontsize=7)
ax.axvline(0.10, color='orange', linestyle=':', label='+10%')
ax.axvline(-0.10, color='orange', linestyle=':', label='-10%')
ax.set_xlabel('delta_m / m  (tau: 0 -> 0.5)')
ax.set_title('Mass Variation All Cells')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3, axis='x')

plt.tight_layout()
plt.savefig(os.path.join(os.path.dirname(__file__), 's58_mass_variation.png'), dpi=150)
print(f"\n  Plot saved: s58_mass_variation.png")

# =============================================================================
# SAVE DATA
# =============================================================================

output_path = os.path.join(os.path.dirname(__file__), 's58_mass_variation.npz')
np.savez(output_path,
    tau_values=tau_values,
    eigenvalues=eigenvalues,
    cell_labels=cell_labels,
    cell_dims=cell_dims,
    cell_casimirs=cell_casimirs,
    fold_idx=fold_idx,
    trace_gK_inv_dgK=trace_gK_inv_dgK,
    dm_m_B2_exact=dm_m_B2_exact,
    dm_m_B2_fold=abs(0.5 * np.log(E_B2_fold / E_B2_0)),
    dm_m_B2_full=dm_m_B2_exact,
    mass_changes_fold=mass_changes_fold,
    mass_changes_full=mass_changes_full,
    gate_name=np.array(['MASS-VARIATION-58']),
    gate_verdict=np.array([verdict]),
    gate_detail=np.array([
        f"tr(g_K^-1 dg_K/dtau)=0 (vol-preserving). "
        f"B2 |dm/m|={dm_m_B2_exact:.4f} over [0,0.5]. "
        f"Threshold 0.10. {N_cells} cells, {cells_above_10pct} above 10%."
    ])
)
print(f"  Data saved: s58_mass_variation.npz")

print("\n" + "=" * 80)
print("COMPUTATION COMPLETE")
print("=" * 80)
