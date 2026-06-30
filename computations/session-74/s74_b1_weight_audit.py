#!/usr/bin/env python3
"""
N10-B1-WEIGHT-AUDIT-74 (W4-A): Audit W_B1 = 0.15024 used in TRANSIT-PS W1-A.

Framework context
-----------------
The TRANSIT-PS-73B diagnostic (``s73b_transit_power_spectrum.py``) decomposes
the decoherence / power-spectrum observables over the three BCS branches

    B1 (acoustic, 1 mode) -- B2 (flat-optical, 4 modes) -- B3 (dispersive, 3 modes)

weighted by per-branch coefficients ``W_B1, W_B2, W_B3`` extracted from the
S70/S72 channel decomposition (``mode_weights``). There W_B1 = 0.15024 is the
fourth entry of the normalised channel mix built from the acoustic / Leggett /
optical fractions of S69 phi_eff.

This script audits that value against an independent, first-principles
projection chain: the 3x3 ``M_ib`` overlap matrix from OVERLAP-MATRIX-74 (W1-K)
which projects each BCS branch onto the emergent scalar / vector / tensor
branches via the SU(3) -> SO(3) Elliott branching of the (p,q)-labelled cells
in the 32-cell CG(24) lattice.

The audit formula (as specified in the task brief) reads:

    W_B1 = |M_{scalar, B1}|^2 * n_{B1}
           -----------------------------------
           sum_b |M_{scalar, b}|^2 * n_b

where n_b is the mode count per branch (1, 4, 3).

In the scalar-channel projection interpretation this is the relative
*spectral-weight* share of B1 in the scalar column of M, squared (amplitude ->
weight) and weighted by mode multiplicity. It is the natural "overlap-matrix"
counterpart to the channel-derived W_B1 used in TRANSIT-PS.

Substrate framing
-----------------
Neither W_B1 expression is a geometric free parameter; both are moments of the
same Dirac spectrum. TRANSIT-PS uses a *channel* projection (acoustic / Leggett
/ optical -> 8 BCS modes) while the overlap matrix uses a *SVT* projection
(scalar / vector / tensor -> 3 BCS branches). The question this audit answers
is whether those two independent moments of the same spectral content assign
comparable weight to the single B1 mode. A mismatch does not invalidate
either projection -- it tells us the scalar and Leggett channels are not
aligned, which is a structural statement about the fabric at tau_fold.

Pre-registered gate
-------------------
    N10-B1-WEIGHT-AUDIT-74:
        PASS  if audited W_B1 in [0.135, 0.165]   (within +/- 10% of 0.150)
        INFO  if audited W_B1 in [0.12 , 0.18 ]
        FAIL  otherwise

Author: Phonon-First Cosmologist (S74 W4-A, EVOI N10, Level 2)
"""

from __future__ import annotations
import os
import sys
import time
import numpy as np

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

# Canonical constants import is mandatory (S34+)
from canonical_constants import tau_fold, N_cells  # noqa: F401

t0 = time.time()

# ==============================================================================
# 1. Load inputs
# ==============================================================================
print("=" * 78)
print("N10-B1-WEIGHT-AUDIT-74 (W4-A): W_B1 audit from 3x3 overlap matrix")
print("=" * 78)
print(f"tau_fold (canonical)       = {tau_fold}")
print(f"N_cells  (canonical)       = {N_cells}")

# --- 1a. W1-K overlap matrix
path_overlap = os.path.join(SCRIPT_DIR, "s74_overlap_matrix.npz")
overlap = np.load(path_overlap, allow_pickle=True)

M = overlap["M"]                                  # (3, 3)  (rows = B1/B2/B3, cols = s/v/t)
bcs_branches = overlap["bcs_branches"]            # ['B1','B2','B3']
emergent_branches = overlap["emergent_branches"]  # ['scalar','vector','tensor']
gate_w1k = str(overlap["gate_verdict"])
tau_fold_actual = float(overlap["tau_fold_actual"])

print(f"\nLoaded W1-K overlap matrix from {os.path.basename(path_overlap)}")
print(f"  tau_fold_actual (W1-K)   = {tau_fold_actual:.6f}")
print(f"  W1-K gate verdict        = {gate_w1k}")
print(f"  M.shape                  = {M.shape}")
print(f"  BCS branches (rows)      = {list(bcs_branches)}")
print(f"  Emergent branches (cols) = {list(emergent_branches)}")

# Sanity: rows are (B1, B2, B3) in that order, cols (scalar, vector, tensor)
assert list(bcs_branches) == ["B1", "B2", "B3"], "Unexpected BCS branch order"
assert list(emergent_branches) == ["scalar", "vector", "tensor"], (
    "Unexpected emergent branch order"
)

# Mode counts per branch (from s74_overlap_matrix.py definition)
branch_modes_B1 = overlap["branch_modes_B1"]   # array [4]
branch_modes_B2 = overlap["branch_modes_B2"]   # array [0,1,2,3]
branch_modes_B3 = overlap["branch_modes_B3"]   # array [5,6,7]

n_B1 = int(len(branch_modes_B1))               # (local) = 1
n_B2 = int(len(branch_modes_B2))               # (local) = 4
n_B3 = int(len(branch_modes_B3))               # (local) = 3
n_b = np.array([n_B1, n_B2, n_B3], dtype=np.int64)   # (local)

print(f"\nBCS branch mode counts:")
print(f"  n_B1 = {n_B1}, n_B2 = {n_B2}, n_B3 = {n_B3} (total = {n_b.sum()})")
assert n_b.sum() == 8, "Total mode count != 8"

# --- 1b. Pull the 0.15024 value actually used in TRANSIT-PS W1-A
#     s73b_transit_power_spectrum.py lines 505-507: W_B1 = mode_weights[4]
#     mode_weights is the S70/S72 channel decomposition saved into s72_blueshift_tilt.npz
path_s72 = os.path.join(SCRIPT_DIR, "s72_blueshift_tilt.npz")
s72 = np.load(path_s72, allow_pickle=True)
mode_weights_s72 = s72["mode_weights"]         # (8,)
assert mode_weights_s72.shape == (8,), "S72 mode_weights not shape (8,)"

# W_B1 used in TRANSIT-PS: mode_weights[4] (B1 sits at index 4 in the 8-mode fold order)
W_B1_transit = float(mode_weights_s72[4])      # (local)
W_B2_transit = float(np.sum(mode_weights_s72[0:4]))  # (local)
W_B3_transit = float(np.sum(mode_weights_s72[5:8]))  # (local)

print(f"\nTRANSIT-PS W1-A branch weights (from S72 channel decomposition):")
print(f"  W_B1 (mode_weights[4])     = {W_B1_transit:.6f}")
print(f"  W_B2 (sum modes 0-3)       = {W_B2_transit:.6f}")
print(f"  W_B3 (sum modes 5-7)       = {W_B3_transit:.6f}")
print(f"  Sum                        = {W_B1_transit + W_B2_transit + W_B3_transit:.6f}")
assert abs((W_B1_transit + W_B2_transit + W_B3_transit) - 1.0) < 1e-8, (
    "S72 mode_weights do not sum to 1 across branches"
)

# Pre-registered reference value for the audit
W_B1_ref = 0.150                               # (local) pre-registered target
tol_pass = 0.015                               # (local) +/- 0.015 -> [0.135, 0.165]
tol_info = 0.030                               # (local) +/- 0.030 -> [0.120, 0.180]

# ==============================================================================
# 2. Print the 3x3 overlap matrix
# ==============================================================================
print("\n" + "=" * 78)
print("3x3 M_ib (rows = BCS branches, cols = emergent branches)")
print("=" * 78)
print(f"{'':>6}  {'scalar':>12}  {'vector':>12}  {'tensor':>12}  {'row sum':>10}")
for i, bname in enumerate(bcs_branches):
    rs = float(M[i, :].sum())
    print(f"{str(bname):>6}  {M[i,0]:>12.6f}  {M[i,1]:>12.6f}  {M[i,2]:>12.6f}  {rs:>10.6f}")
col_sums = M.sum(axis=0)
print(f"{'col sum':>6}  {col_sums[0]:>12.6f}  {col_sums[1]:>12.6f}  {col_sums[2]:>12.6f}")

row_dev = float(np.max(np.abs(M.sum(axis=1) - 1.0)))
print(f"\nRow-sum deviation from 1 : {row_dev:.3e}  (stochastic in rows: OK)")

# ==============================================================================
# 3. Audit formula -- "scalar column" interpretation
# ==============================================================================
#   W_B1_audit = |M_{B1, scalar}|^2 * n_B1
#                -----------------------------------
#                sum_b |M_{b, scalar}|^2 * n_b
#
# M indexed (row = BCS branch b, col = emergent j). The scalar column is j=0.
# This is the natural projection of B1's contribution onto the emergent
# scalar channel, weighted by branch multiplicity.
# ==============================================================================

scalar_col = M[:, 0]                           # (3,) [M_{B1,s}, M_{B2,s}, M_{B3,s}]
M_B1_scalar = float(scalar_col[0])             # (local)
M_B2_scalar = float(scalar_col[1])             # (local)
M_B3_scalar = float(scalar_col[2])             # (local)

scalar_sq_weighted = scalar_col ** 2 * n_b     # (local) [|M_bs|^2 * n_b]
numer = float(scalar_sq_weighted[0])           # (local) B1 term
denom = float(scalar_sq_weighted.sum())        # (local) sum_b

W_B1_audit = numer / denom                     # (local) MAIN audit value

delta = W_B1_audit - W_B1_ref                  # (local) signed difference vs 0.150
rel = delta / W_B1_ref                         # (local) relative

# ==============================================================================
# 4. Cross-checks -- alternative interpretations
# ==============================================================================

# (a) Unweighted (amplitude) projection: M_{B1,s} / sum_b M_{b,s} -- no mode counts
W_B1_amplitude = M_B1_scalar / float(scalar_col.sum())             # (local)

# (b) Amplitude squared (no n_b weighting)
W_B1_squared_no_n = (M_B1_scalar ** 2) / float((scalar_col ** 2).sum())  # (local)

# (c) Linear "scalar column share, mode-count weighted"
scalar_lin_weighted = scalar_col * n_b                              # (local)
W_B1_linear_n = float(scalar_lin_weighted[0]) / float(scalar_lin_weighted.sum())  # (local)

# (d) "Mode-weighted scalar overlap": for each branch sum |M_{b,s}| over modes
#     = n_b * M_{b,s}; same as (c). Kept for clarity.

# (e) Row-B1 diagonal (pure SVT content of B1 in the scalar channel)
W_B1_row = M_B1_scalar / float(M[0, :].sum())                        # (local)

print("\n" + "=" * 78)
print("Audit: Alternative projections of scalar-channel B1 share")
print("=" * 78)
print(f"  (main) |M_{{B1,s}}|^2 * n_B1 / sum_b |M_{{b,s}}|^2 * n_b = {W_B1_audit:.6f}")
print(f"  (a)    amplitude    M_{{B1,s}} / sum M_{{b,s}}             = {W_B1_amplitude:.6f}")
print(f"  (b)    squared no-n |M_{{B1,s}}|^2 / sum |M_{{b,s}}|^2       = {W_B1_squared_no_n:.6f}")
print(f"  (c)    linear n-wt  n_B1*M_{{B1,s}} / sum n_b*M_{{b,s}}      = {W_B1_linear_n:.6f}")
print(f"  (e)    B1 row frac  M_{{B1,s}} / sum_j M_{{B1,j}}            = {W_B1_row:.6f}")

# ==============================================================================
# 5. Comparison to W_B1_transit = 0.150
# ==============================================================================
print("\n" + "=" * 78)
print(f"Audit W_B1 vs TRANSIT-PS W_B1 = {W_B1_ref:.3f}")
print("=" * 78)
print(f"  W_B1 (audit, main)         = {W_B1_audit:.6f}")
print(f"  W_B1 (transit W1-A)        = {W_B1_transit:.6f}")
print(f"  W_B1 (pre-reg reference)   = {W_B1_ref:.6f}")
print(f"  delta (audit - ref)        = {delta:+.6f}")
print(f"  relative deviation         = {rel*100:+.2f} %")

# Also compare the audit expression to the exact 0.15024 value used in code
delta_vs_transit = W_B1_audit - W_B1_transit   # (local)
rel_vs_transit = delta_vs_transit / W_B1_transit   # (local)
print(f"  delta (audit - transit)    = {delta_vs_transit:+.6f}")
print(f"  relative vs transit        = {rel_vs_transit*100:+.2f} %")

# ==============================================================================
# 6. Gate verdict
# ==============================================================================
pass_lo, pass_hi = W_B1_ref - tol_pass, W_B1_ref + tol_pass   # [0.135, 0.165]
info_lo, info_hi = W_B1_ref - tol_info, W_B1_ref + tol_info   # [0.120, 0.180]

if pass_lo <= W_B1_audit <= pass_hi:
    verdict = "PASS"
elif info_lo <= W_B1_audit <= info_hi:
    verdict = "INFO"
else:
    verdict = "FAIL"

gate_name = "N10-B1-WEIGHT-AUDIT-74"
print("\n" + "=" * 78)
print(f"Gate {gate_name}: {verdict}")
print("=" * 78)
print(f"  PASS window  : [{pass_lo:.3f}, {pass_hi:.3f}]")
print(f"  INFO window  : [{info_lo:.3f}, {info_hi:.3f}]")
print(f"  Computed     : W_B1 = {W_B1_audit:.6f}")
print(f"  Threshold    : +/- {tol_pass:.3f} around {W_B1_ref:.3f} for PASS")

# ==============================================================================
# 7. Save
# ==============================================================================
out = os.path.join(SCRIPT_DIR, "s74_b1_weight_audit.npz")
np.savez(
    out,
    # main audit result
    W_B1_audit=W_B1_audit,
    W_B1_transit=W_B1_transit,
    W_B1_ref=W_B1_ref,
    delta=delta,
    rel=rel,
    delta_vs_transit=delta_vs_transit,
    rel_vs_transit=rel_vs_transit,
    # inputs
    M=M,
    scalar_col=scalar_col,
    n_b=n_b,
    M_B1_scalar=M_B1_scalar,
    M_B2_scalar=M_B2_scalar,
    M_B3_scalar=M_B3_scalar,
    mode_weights_s72=mode_weights_s72,
    W_B2_transit=W_B2_transit,
    W_B3_transit=W_B3_transit,
    # alternative projections (cross-checks)
    W_B1_amplitude=W_B1_amplitude,
    W_B1_squared_no_n=W_B1_squared_no_n,
    W_B1_linear_n=W_B1_linear_n,
    W_B1_row=W_B1_row,
    # gate
    gate_name=gate_name,
    gate_verdict=verdict,
    pass_lo=pass_lo,
    pass_hi=pass_hi,
    info_lo=info_lo,
    info_hi=info_hi,
    tau_fold_actual=tau_fold_actual,
)
print(f"\nSaved: {out}")
print(f"Elapsed: {time.time() - t0:.2f} s")
