#!/usr/bin/env python3
"""
s65_gap_antijensen.py — GAP-ANTIJENSEN-65: BCS Gap Survival Off-Jensen
========================================================================

Gate: GAP-ANTIJENSEN-65
  PASS: Delta(s) > 0.1 * Delta_0 for all s within dynamical range (condensate survives)
  FAIL: Delta drops to 0 before s reaches 10% of dynamical range (destroyed early)
  INFO: Gap closes but only beyond dynamical range (safe for physical trajectory)

Context:
  S64 W1-D proved: transit trajectory deviates 18.2% from Jensen curve within the
  2D volume-preserving diagonal subspace. The deviation is structurally confined
  (U(2)-invariance preservation theorem), lying entirely within the (L_su2, L_c2, L_u1)
  scale factor space.

  The anti-Jensen direction is the steepest R-descent eigenvector in the
  volume-preserving subspace (from s64_hessian_descent.npz). This direction:
  - Shrinks SU(2) (dg_su2 < 0)
  - Expands C^2 (dg_c2 > 0)
  - Slightly expands U(1) (dg_u1 > 0)
  - Is at 135.5 degrees from the Jensen tangent (broadly anti-Jensen)

  Question: Does the BCS condensate survive this off-Jensen deformation?

Method:
  1. Load the anti-Jensen direction from s64_hessian_descent.npz
  2. Parametrize path: g(s) = g_fold + s * v_descent (linear in metric space)
  3. At each s, build metric -> ON frame -> connection -> Omega -> Dirac spectrum
  4. Solve self-consistent BCS gap equation: 1 = V * sum_k 1/(2*E_k)
     where E_k = sqrt(xi_k^2 + Delta^2), xi_k = |lambda_k| - mu
  5. Track Delta(s)/Delta_0 and identify critical s_c (if any)
  6. Compare s_c to dynamical range s_dyn (18.2% deviation)

  Also track: spectral action S(s), scalar curvature R(s), spectral gap,
  and BCS occupation-weighted spectral action S_occ(s).

  VOLUME NORMALIZATION: The linear path in metric space does not preserve
  det(g) = const. At each step, we normalize back to the volume-preserving
  constraint surface: g -> g * (det(g_fold)/det(g))^{1/8}.

Superfluid-vacuum perspective (Volovik):
  In 3He-B, the BCS gap is topologically protected by the BDI invariant Z_2 = -1
  (S44 N3-BDG-44). This protects the gap from VANISHING but not from SHRINKING.
  The gap magnitude depends on the pairing interaction V and the density of states
  near the Fermi surface — both of which change under metric deformation.

  The physical analog: deforming the superfluid container (pressure anisotropy)
  shifts the quasiparticle spectrum and modifies the pairing strength, but the
  gap cannot close continuously in class BDI — it can only vanish via a first-order
  transition where the system exits the topological phase entirely.

  This computation tests whether the metric deformation along the transit trajectory
  is sufficient to trigger such a transition.

Author: volovik-superfluid-universe-theorist, Session 65
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
import sys
import os
import time

t_start = time.time()

script_dir = Path(__file__).parent
sys.path.insert(0, str(script_dir))
archive_dir = script_dir.parent / 'computations/_shared'
sys.path.insert(0, str(archive_dir))

from canonical_constants import (
    tau_fold, Delta_0_OES, E_B1, S_fold, PI,
    E_B2_mean, E_B3_mean, E_cond, E_cond_ED_8mode,
    a0_fold, a2_fold, N_dof_BCS, Vol_SU3_Haar,
    M_KK, dt_transit,
)

from dirac_spectrum import (
    su3_generators, compute_structure_constants, compute_killing_form,
    u2_invariant_metric, orthonormal_frame, frame_structure_constants,
    connection_coefficients, spinor_connection_offset,
    validate_connection, validate_omega_hermitian,
    build_cliff8, dirac_operator_on_irrep, get_irrep,
    U1_IDX, SU2_IDX, C2_IDX,
)

print("=" * 78)
print("  GAP-ANTIJENSEN-65: BCS Gap Survival Along Anti-Jensen Direction")
print("=" * 78)

# =============================================================================
# Section 1: Load anti-Jensen direction and fold data
# =============================================================================
print("\n--- Section 1: Loading data ---")

d_hess = np.load(script_dir / 's64_hessian_descent.npz', allow_pickle=True)
d_occ = np.load(script_dir / 's64_occ_spec.npz', allow_pickle=True)
d_bdg = np.load(script_dir / 's64_bdg_kasparov.npz', allow_pickle=True)

g_fold = d_hess['g_fold']          # (8,8) diagonal metric at fold
dR_vp = d_hess['dR_vp']            # (36,) steepest R-descent in VP subspace
tau_fold_val = float(d_hess['tau_fold'])
R_fold = float(d_hess['R_fold_ref'])

Delta_0 = Delta_0_OES              # 0.464 M_KK (canonical BCS gap at fold)
mu_0 = E_B1                        # 0.819 M_KK (chemical potential)

print(f"  tau_fold = {tau_fold_val}")
print(f"  R_fold = {R_fold:.6f}")
print(f"  Delta_0 = {Delta_0:.6f} M_KK")
print(f"  mu_0 = {mu_0:.6f} M_KK")
print(f"  g_fold diagonal = {np.diag(g_fold)}")

# Extract descent direction as 8x8 diagonal perturbation
# (dR_vp has 36 components: 8 diagonal + 28 off-diagonal, all off-diagonal are zero)
delta_g = np.zeros((8, 8))
for i in range(8):
    delta_g[i, i] = dR_vp[i]

print(f"  delta_g diagonal = {np.diag(delta_g)}")
print(f"  Volume-preserving check: Tr(g^-1 dg) = {np.sum(np.diag(delta_g) / np.diag(g_fold)):.2e}")

# Dynamical range from W1-D: 18.2% deviation
# |delta_g| / |g_fold| = 0.182 at dynamical boundary
norm_g_fold = np.linalg.norm(np.diag(g_fold))
norm_dg = np.linalg.norm(np.diag(delta_g))
s_dyn = 0.182 * norm_g_fold / norm_dg      # step parameter at dynamical range
s_max = 0.50 * norm_g_fold / norm_dg       # 50% deviation (task spec)

print(f"  |g_fold| = {norm_g_fold:.4f}")
print(f"  |delta_g| = {norm_dg:.6f}")
print(f"  s_dyn (18.2% range) = {s_dyn:.2f}")
print(f"  s_max (50% range) = {s_max:.2f}")

# =============================================================================
# Section 2: Build Lie algebra infrastructure
# =============================================================================
print("\n--- Section 2: Lie algebra infrastructure ---")

gens = su3_generators()
f_abc = compute_structure_constants(gens)
B_ab = compute_killing_form(f_abc)
gammas = build_cliff8()

# Verify fold metric matches Jensen
s0 = tau_fold_val
L1_fold = np.exp(2 * s0)
L2_fold = np.exp(-2 * s0)
L3_fold = np.exp(s0)
g_jensen_fold = u2_invariant_metric(B_ab, L1_fold, L2_fold, L3_fold)
assert np.allclose(g_jensen_fold, g_fold, atol=1e-10), "Fold metric mismatch"
print(f"  Jensen metric verified at s={s0}")

# Base Killing form scale: B_0 = 3.0 (diagonal elements of |B_ab|)
B_0 = np.abs(B_ab[0, 0])
print(f"  B_0 (Killing normalization) = {B_0:.1f}")


def collect_spectrum_from_metric(g_metric, gens, f_abc, gammas, max_pq_sum=3):
    """
    Compute Dirac spectrum on (SU(3), g_metric) for an arbitrary
    positive-definite left-invariant metric.

    Returns:
        omega_00: sorted |eigenvalue| array for (0,0) sector (16 values)
        omega_all: sorted |eigenvalue| array for all sectors with multiplicities
        mult_all: corresponding PW multiplicities
        S_full: full spectral action sum_{p,q} dim(p,q)^2 * sum_j |lambda_j|
    """
    E = orthonormal_frame(g_metric)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)
    Omega = spinor_connection_offset(Gamma, gammas)

    # (0,0) sector: D = Omega
    evals_00_raw = np.linalg.eigvals(Omega)
    omega_00 = np.sort(np.abs(evals_00_raw))

    all_omega = []
    all_mult = []
    S_full = 0.0

    # (0,0) sector
    for ev in omega_00:
        all_omega.append(ev)
        all_mult.append(1)  # PW mult = dim(0,0)^2 = 1
    S_full += np.sum(omega_00)

    # Higher sectors
    irreps = []
    for p in range(max_pq_sum + 1):
        for q in range(max_pq_sum + 1 - p):
            if p == 0 and q == 0:
                continue
            dim_pq = (p + 1) * (q + 1) * (p + q + 2) // 2
            C2 = (p**2 + q**2 + p * q + 3 * p + 3 * q) / 3.0
            irreps.append((C2, p, q, dim_pq))
    irreps.sort()

    for C2_val, p, q, dim_pq in irreps:
        try:
            rho, dim_check = get_irrep(p, q, gens, f_abc)
            D_pi = dirac_operator_on_irrep(rho, E, gammas, Omega)
            evals_pi = np.linalg.eigvals(D_pi)
            omega_pi = np.abs(evals_pi)
            for ev in omega_pi:
                all_omega.append(ev)
                all_mult.append(dim_pq)
            S_full += dim_pq**2 * np.sum(omega_pi)
        except NotImplementedError:
            continue

    all_omega = np.array(all_omega)
    all_mult = np.array(all_mult)
    sort_idx = np.argsort(all_omega)
    return omega_00, all_omega[sort_idx], all_mult[sort_idx], S_full


def solve_bcs_gap(omega_modes, mu, V_pair, Delta_init=0.5, tol=1e-10, max_iter=500):
    """
    Solve the self-consistent BCS gap equation:
      1 = V * sum_k 1/(2*E_k)
    where E_k = sqrt(xi_k^2 + Delta^2), xi_k = |omega_k| - mu.

    This is equivalent to finding Delta such that:
      Delta = V * sum_k Delta/(2*E_k) = V/2 * sum_k Delta/sqrt(xi_k^2 + Delta^2)

    Using the standard iterative form:
      1/V = sum_k 1/(2*sqrt(xi_k^2 + Delta^2))

    Given V, solve for Delta by bisection or Newton's method.
    If the gap equation has no solution (pairing too weak), returns 0.

    Returns:
        Delta: self-consistent gap (M_KK units)
        converged: bool
    """
    xi_k = np.abs(omega_modes) - mu

    # Check if pairing is possible: at Delta->0, RHS = sum 1/(2|xi_k|)
    # If all xi_k != 0, this sum is finite. Gap equation has solution if
    # V * sum 1/(2|xi_k|) > 1, i.e., pairing strong enough.
    xi_nonzero = xi_k[np.abs(xi_k) > 1e-15]
    if len(xi_nonzero) == 0:
        # All modes at Fermi surface — gap exists for any V > 0
        return Delta_init, True

    rhs_at_zero = np.sum(1.0 / (2.0 * np.abs(xi_nonzero)))
    if V_pair * rhs_at_zero < 1.0 and len(xi_nonzero) == len(xi_k):
        return 0.0, True  # No solution: pairing too weak

    # Bisection for Delta
    Delta_lo = 1e-15
    Delta_hi = 10.0 * max(np.max(np.abs(xi_k)), Delta_init)

    for _ in range(max_iter):
        Delta_mid = 0.5 * (Delta_lo + Delta_hi)
        E_k = np.sqrt(xi_k**2 + Delta_mid**2)
        rhs = V_pair * np.sum(1.0 / (2.0 * E_k))
        if rhs > 1.0:
            Delta_lo = Delta_mid
        else:
            Delta_hi = Delta_mid
        if (Delta_hi - Delta_lo) / max(Delta_hi, 1e-20) < tol:
            break

    Delta_out = 0.5 * (Delta_lo + Delta_hi)
    return Delta_out, True


def extract_bcs_coupling(omega_modes, mu, Delta_target):
    """
    Extract the effective pairing coupling V from the known gap Delta_target
    at the fold metric. This V is then used at deformed metrics.

    V = 1 / sum_k 1/(2*E_k) at the fold.
    """
    xi_k = np.abs(omega_modes) - mu
    E_k = np.sqrt(xi_k**2 + Delta_target**2)
    V = 1.0 / np.sum(1.0 / (2.0 * E_k))
    return V


# =============================================================================
# Section 3: Verify fold spectrum and extract pairing coupling
# =============================================================================
print("\n--- Section 3: Fold spectrum verification ---")

omega_00_fold, omega_all_fold, mult_all_fold, S_full_fold = \
    collect_spectrum_from_metric(g_fold, gens, f_abc, gammas, max_pq_sum=3)

print(f"  S_full at fold: {S_full_fold:.2f} (canonical: {S_fold:.2f})")
print(f"  Match: {abs(S_full_fold - S_fold)/S_fold:.2e}")
print(f"  (0,0) sector |lambda| values:")

# Identify the 8 BCS modes (unique values in (0,0) sector)
unique_vals_00 = np.unique(np.round(omega_00_fold, 8))
for om in unique_vals_00:
    mult = np.sum(np.abs(omega_00_fold - om) < 1e-6)
    xi = om - mu_0
    print(f"    |lambda| = {om:.6f}, mult = {mult}, xi = {xi:+.6f}")

# The 8 BCS modes correspond to the positive eigenvalues in (0,0) sector
# grouped into B1 (2, near 0.820), B2 (8, near 0.845), B3 (6, near 0.971)
# But since they come in +/- pairs, the 16 |eigenvalues| give 8 distinct modes
# Wait, the sector has 16 eigenvalues (dim=1, spinor dim=16)
# These correspond to 8 distinct |lambda| values (each with multiplicity 2 from chirality)

# For BCS: use the unique |lambda| values with their multiplicities
# The relevant modes for pairing are those near the Fermi surface (mu = 0.819)
bcs_modes = omega_00_fold  # All 16 values

# Extract coupling V from known Delta_0 at fold
V_pair = extract_bcs_coupling(bcs_modes, mu_0, Delta_0)
print(f"\n  Effective pairing V = {V_pair:.6f} M_KK")

# Self-consistency check: solve gap equation with this V at fold
Delta_check, conv = solve_bcs_gap(bcs_modes, mu_0, V_pair, Delta_init=Delta_0)
print(f"  Self-consistency: Delta_BCS = {Delta_check:.6f} (target: {Delta_0:.6f})")
print(f"  Deviation: {abs(Delta_check - Delta_0)/Delta_0:.2e}")

# =============================================================================
# Section 4: Path computation — 11 points from s=0 to s_max
# =============================================================================
print("\n--- Section 4: Anti-Jensen path computation ---")

N_points = 11
s_values = np.linspace(0, s_max, N_points)
frac_values = s_values * norm_dg / norm_g_fold  # fractional deviation

# Results arrays
Delta_path = np.zeros(N_points)
S_full_path = np.zeros(N_points)
R_scalar_path = np.zeros(N_points)
omega_00_path = np.zeros((N_points, 16))
spectral_gap_path = np.zeros(N_points)
det_g_path = np.zeros(N_points)
L_su2_path = np.zeros(N_points)
L_c2_path = np.zeros(N_points)
L_u1_path = np.zeros(N_points)
E_cond_path = np.zeros(N_points)
min_xi_path = np.zeros(N_points)
bcs_converged = np.zeros(N_points, dtype=bool)

det_fold = np.linalg.det(g_fold)

print(f"  Computing {N_points} points from f=0 to f={frac_values[-1]:.2f}")
print(f"  Dynamical range at f=0.182 (s={s_dyn:.1f})")
print(f"  {'idx':>3} {'frac':>6} {'s':>8} {'L_su2':>8} {'L_c2':>8} {'L_u1':>8} "
      f"{'Delta':>8} {'D/D0':>6} {'S_full':>10} {'gap':>8} {'min_xi':>8}")
print("  " + "-" * 95)

for i, s in enumerate(s_values):
    # Construct deformed metric (linear path)
    g_deformed = g_fold + s * delta_g

    # Volume normalization: project back to det(g) = det(g_fold)
    det_g = np.linalg.det(g_deformed)
    scale_factor = (det_fold / det_g) ** (1.0 / 8.0)
    g_normalized = g_deformed * scale_factor

    det_g_path[i] = np.linalg.det(g_normalized)

    # Extract scale factors L1, L2, L3 from normalized metric
    L_su2_path[i] = g_normalized[0, 0] / B_0
    L_c2_path[i] = g_normalized[3, 3] / B_0
    L_u1_path[i] = g_normalized[7, 7] / B_0

    # Compute Dirac spectrum at this metric
    omega_00_s, omega_all_s, mult_all_s, S_full_s = \
        collect_spectrum_from_metric(g_normalized, gens, f_abc, gammas, max_pq_sum=3)

    omega_00_path[i] = omega_00_s
    S_full_path[i] = S_full_s

    # Scalar curvature from spectral action: a_2 ~ R * Vol
    # Actually compute R directly from the Milnor formula
    E = orthonormal_frame(g_normalized)
    ft = frame_structure_constants(f_abc, E)
    # Milnor formula: R = -1/2 sum_{abc} ft_{abc}^2 + 1/4 sum_{ab} (sum_c ft_{cab})^2
    term1 = -0.5 * np.sum(ft**2)
    traces = np.einsum('cab->ab', ft)
    term2 = 0.25 * np.sum(traces**2)
    R_scalar_path[i] = term1 + term2

    # BCS gap equation
    # Use chemical potential fixed at mu_0 (adiabatic approximation:
    # mu adjusts slowly compared to gap dynamics)
    bcs_modes_s = omega_00_s  # 16 modes from (0,0) sector

    # Also compute with fixed mu and V
    Delta_s, conv = solve_bcs_gap(bcs_modes_s, mu_0, V_pair, Delta_init=Delta_0)
    Delta_path[i] = Delta_s
    bcs_converged[i] = conv

    # Spectral gap (minimum Bogoliubov QP energy)
    xi_s = np.abs(bcs_modes_s) - mu_0
    E_bdg_s = np.sqrt(xi_s**2 + Delta_s**2) if Delta_s > 0 else np.abs(xi_s)
    spectral_gap_path[i] = np.min(E_bdg_s)
    min_xi_path[i] = np.min(np.abs(xi_s))

    # Condensation energy estimate (using gap and DOS)
    if Delta_s > 0:
        E_cond_path[i] = -0.5 * np.sum(np.abs(bcs_modes_s)) * (Delta_s / np.mean(np.abs(bcs_modes_s)))**2
    else:
        E_cond_path[i] = 0.0

    Delta_ratio = Delta_s / Delta_0 if Delta_0 > 0 else 0.0
    print(f"  {i:3d} {frac_values[i]:6.3f} {s:8.2f} {L_su2_path[i]:8.4f} {L_c2_path[i]:8.4f} "
          f"{L_u1_path[i]:8.4f} {Delta_s:8.5f} {Delta_ratio:6.3f} {S_full_s:10.1f} "
          f"{spectral_gap_path[i]:8.5f} {min_xi_path[i]:8.5f}")

# =============================================================================
# Section 5: Identify critical s_c and compare to dynamical range
# =============================================================================
print("\n--- Section 5: Gap survival analysis ---")

Delta_ratio_path = Delta_path / Delta_0
threshold = 0.1  # FAIL if Delta < 0.1 * Delta_0 (local)

# Find critical s_c where Delta drops below threshold
critical_idx = np.where(Delta_ratio_path < threshold)[0]
if len(critical_idx) > 0:
    idx_c = critical_idx[0]
    s_c = s_values[idx_c]
    frac_c = frac_values[idx_c]
    # Interpolate more precisely
    if idx_c > 0:
        # Linear interpolation between idx_c-1 and idx_c
        f1, f2 = frac_values[idx_c - 1], frac_values[idx_c]
        d1, d2 = Delta_ratio_path[idx_c - 1], Delta_ratio_path[idx_c]
        frac_c_interp = f1 + (threshold - d1) * (f2 - f1) / (d2 - d1)
        s_c_interp = frac_c_interp * norm_g_fold / norm_dg
    else:
        frac_c_interp = frac_c
        s_c_interp = s_c
    print(f"  CRITICAL POINT: Delta/Delta_0 < {threshold} at f = {frac_c_interp:.4f} (s = {s_c_interp:.2f})")
    gap_closes = True
else:
    print(f"  NO CRITICAL POINT: Delta/Delta_0 > {threshold} throughout range [0, {frac_values[-1]:.2f}]")
    gap_closes = False
    s_c = np.inf
    frac_c_interp = np.inf

# Dynamical range comparison
print(f"\n  Dynamical range: f_dyn = 0.182 (s_dyn = {s_dyn:.2f})")
print(f"  Maximum deviation: f_max = {frac_values[-1]:.3f} (s_max = {s_max:.2f})")
print(f"  Delta at dynamical range:")

# Find Delta at f ~ 0.182
idx_dyn = np.argmin(np.abs(frac_values - 0.182))
Delta_at_dyn = Delta_path[idx_dyn]
ratio_at_dyn = Delta_ratio_path[idx_dyn]
print(f"    Delta(f=0.182) = {Delta_at_dyn:.6f} M_KK")
print(f"    Delta(f=0.182)/Delta_0 = {ratio_at_dyn:.4f}")

# 10% of dynamical range
frac_10pct = 0.1 * 0.182
idx_10pct = np.argmin(np.abs(frac_values - frac_10pct))
Delta_at_10pct = Delta_path[idx_10pct]
ratio_at_10pct = Delta_ratio_path[idx_10pct]
print(f"    Delta(f=0.018) = {Delta_at_10pct:.6f} M_KK")
print(f"    Delta(f=0.018)/Delta_0 = {ratio_at_10pct:.4f}")

# Minimum Delta in the entire range
Delta_min = np.min(Delta_path)
idx_min = np.argmin(Delta_path)
print(f"\n  Minimum Delta: {Delta_min:.6f} M_KK at f = {frac_values[idx_min]:.3f}")
print(f"  Minimum Delta/Delta_0: {Delta_min/Delta_0:.4f}")

# =============================================================================
# Section 6: Gate verdict
# =============================================================================
print("\n--- Section 6: Gate verdict ---")

# PASS: Delta(s) > 0.1 * Delta_0 for all s within dynamical range
# FAIL: Delta drops to 0 before s reaches 10% of dynamical range
# INFO: Gap closes but only beyond dynamical range

if gap_closes and frac_c_interp < 0.1 * 0.182:
    gate_verdict = "FAIL"
    gate_detail = (f"Delta drops below {threshold}*Delta_0 at f={frac_c_interp:.4f}, "
                   f"before 10% of dynamical range (f=0.018). "
                   f"BCS condensate destroyed early.")
elif not gap_closes or frac_c_interp > 0.182:
    # Check if Delta > threshold at all points within dynamical range
    within_dyn = frac_values <= 0.182
    if np.all(Delta_ratio_path[within_dyn] > threshold):
        gate_verdict = "PASS"
        gate_detail = (f"Delta/Delta_0 > {threshold} for all f <= 0.182 (dynamical range). "
                       f"Min Delta/Delta_0 = {np.min(Delta_ratio_path[within_dyn]):.4f} at "
                       f"f = {frac_values[within_dyn][np.argmin(Delta_ratio_path[within_dyn])]:.3f}. "
                       f"BCS condensate SURVIVES off-Jensen transit.")
        if gap_closes:
            gate_detail += (f" Gap closes at f={frac_c_interp:.4f} (beyond dynamical range).")
    else:
        gate_verdict = "FAIL"
        worst_idx = np.argmin(Delta_ratio_path[within_dyn])
        gate_detail = (f"Delta/Delta_0 = {Delta_ratio_path[within_dyn][worst_idx]:.4f} < {threshold} "
                       f"at f = {frac_values[within_dyn][worst_idx]:.3f} within dynamical range.")
else:
    gate_verdict = "INFO"
    gate_detail = (f"Gap closes at f={frac_c_interp:.4f}, within dynamical range "
                   f"but beyond 10% threshold. Marginal.")

gate_value = float(np.min(Delta_ratio_path[frac_values <= 0.182])) if np.any(frac_values <= 0.182) else float(Delta_ratio_path[0])
gate_threshold = threshold

print(f"  Gate: GAP-ANTIJENSEN-65")
print(f"  Verdict: {gate_verdict}")
print(f"  Value: min(Delta/Delta_0) within dynamical range = {gate_value:.6f}")
print(f"  Threshold: {gate_threshold}")
print(f"  Detail: {gate_detail}")

# =============================================================================
# Section 7: Additional diagnostics
# =============================================================================
print("\n--- Section 7: Diagnostics ---")

# Spectral action along path
print(f"\n  Spectral action S(f):")
print(f"    S(0) = {S_full_path[0]:.2f}")
print(f"    S(0.182) = {S_full_path[idx_dyn]:.2f}")
print(f"    S(0.50) = {S_full_path[-1]:.2f}")
print(f"    Fractional change at dyn range: {(S_full_path[idx_dyn] - S_full_path[0])/S_full_path[0]:.4f}")

# Scalar curvature
print(f"\n  Scalar curvature R(f):")
print(f"    R(0) = {R_scalar_path[0]:.6f}")
print(f"    R(0.182) = {R_scalar_path[idx_dyn]:.6f}")
print(f"    R(0.50) = {R_scalar_path[-1]:.6f}")

# Level crossing check (do eigenvalues reorder?)
print(f"\n  Level structure at fold:")
unique_fold = np.unique(np.round(omega_00_path[0], 6))
print(f"    Unique |lambda|: {unique_fold}")

print(f"  Level structure at f=0.50:")
unique_max = np.unique(np.round(omega_00_path[-1], 6))
print(f"    Unique |lambda|: {unique_max}")

# BDI protection check
# In class BDI, the gap is protected by Z_2 = -1 topological invariant
# The gap can only close via a topological phase transition
# Check if any eigenvalue crosses zero (sign change in xi_k)
print(f"\n  Fermi surface crossing check:")
for i in range(N_points):
    xi_i = omega_00_path[i] - mu_0
    n_below = np.sum(xi_i < 0)
    n_above = np.sum(xi_i > 0)
    if i == 0 or i == N_points - 1 or i == idx_dyn:
        print(f"    f={frac_values[i]:.3f}: {n_below} modes below mu, {n_above} above mu")

# =============================================================================
# Section 8: Save results
# =============================================================================
print("\n--- Section 8: Saving results ---")

output_path = script_dir / 's65_gap_antijensen.npz'
np.savez(output_path,
    # Gate
    gate_name='GAP-ANTIJENSEN-65',
    gate_verdict=gate_verdict,
    gate_detail=gate_detail,
    gate_value=gate_value,
    gate_threshold=gate_threshold,
    # Path parameters
    s_values=s_values,
    frac_values=frac_values,
    s_dyn=s_dyn,
    s_max=s_max,
    # BCS results
    Delta_path=Delta_path,
    Delta_ratio_path=Delta_ratio_path,
    Delta_0=Delta_0,
    mu_0=mu_0,
    V_pair=V_pair,
    bcs_converged=bcs_converged,
    # Spectrum
    omega_00_path=omega_00_path,
    S_full_path=S_full_path,
    R_scalar_path=R_scalar_path,
    spectral_gap_path=spectral_gap_path,
    min_xi_path=min_xi_path,
    # Metric
    L_su2_path=L_su2_path,
    L_c2_path=L_c2_path,
    L_u1_path=L_u1_path,
    det_g_path=det_g_path,
    # Derived
    E_cond_path=E_cond_path,
    # Critical point
    gap_closes=gap_closes,
    frac_c_interp=frac_c_interp if gap_closes else np.inf,
)
print(f"  Saved: {output_path}")

# =============================================================================
# Section 9: Plot
# =============================================================================
print("\n--- Section 9: Plotting ---")

fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle('GAP-ANTIJENSEN-65: BCS Gap Survival Along Anti-Jensen Direction',
             fontsize=14, fontweight='bold')

# Panel 1: Delta/Delta_0 vs fractional deviation
ax = axes[0, 0]
ax.plot(frac_values, Delta_ratio_path, 'b-o', linewidth=2, markersize=5)
ax.axhline(y=threshold, color='r', linestyle='--', linewidth=1, label=f'Threshold = {threshold}')
ax.axvline(x=0.182, color='g', linestyle=':', linewidth=1.5, label='Dynamical range (18.2%)')
ax.set_xlabel('Fractional deviation from fold |delta g|/|g|')
ax.set_ylabel('Delta(s) / Delta_0')
ax.set_title('BCS Gap Survival')
ax.legend(fontsize=8)
ax.set_ylim(bottom=0)
ax.grid(True, alpha=0.3)

# Panel 2: Spectral action along path
ax = axes[0, 1]
ax.plot(frac_values, S_full_path / S_full_path[0], 'k-o', linewidth=2, markersize=5)
ax.axvline(x=0.182, color='g', linestyle=':', linewidth=1.5, label='Dynamical range')
ax.set_xlabel('Fractional deviation')
ax.set_ylabel('S(s) / S(fold)')
ax.set_title('Spectral Action')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 3: Scale factors along path
ax = axes[0, 2]
ax.plot(frac_values, L_su2_path, 'r-o', linewidth=2, markersize=4, label='L_su2')
ax.plot(frac_values, L_c2_path, 'b-o', linewidth=2, markersize=4, label='L_c2')
ax.plot(frac_values, L_u1_path, 'g-o', linewidth=2, markersize=4, label='L_u1')
ax.axvline(x=0.182, color='gray', linestyle=':', linewidth=1.5)
ax.set_xlabel('Fractional deviation')
ax.set_ylabel('Scale factor L')
ax.set_title('Metric Scale Factors')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 4: Eigenvalue waterfall (0,0 sector)
ax = axes[1, 0]
for j in range(16):
    ax.plot(frac_values, omega_00_path[:, j], 'b-', linewidth=0.8, alpha=0.5)
ax.axhline(y=mu_0, color='r', linestyle='--', linewidth=1, label=f'mu = {mu_0:.3f}')
ax.axvline(x=0.182, color='g', linestyle=':', linewidth=1.5)
ax.set_xlabel('Fractional deviation')
ax.set_ylabel('|lambda| (M_KK)')
ax.set_title('(0,0) Sector Eigenvalues')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 5: Scalar curvature
ax = axes[1, 1]
ax.plot(frac_values, R_scalar_path, 'm-o', linewidth=2, markersize=5)
ax.axvline(x=0.182, color='g', linestyle=':', linewidth=1.5, label='Dynamical range')
ax.set_xlabel('Fractional deviation')
ax.set_ylabel('R (scalar curvature)')
ax.set_title('Scalar Curvature R(g)')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 6: Spectral gap and min |xi|
ax = axes[1, 2]
ax.plot(frac_values, spectral_gap_path, 'b-o', linewidth=2, markersize=5, label='BdG gap')
ax.plot(frac_values, min_xi_path, 'r-s', linewidth=1.5, markersize=4, label='min |xi_k|')
ax.axvline(x=0.182, color='g', linestyle=':', linewidth=1.5, label='Dynamical range')
ax.set_xlabel('Fractional deviation')
ax.set_ylabel('Energy (M_KK)')
ax.set_title('Spectral Gap & Fermi Surface Distance')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plot_path = script_dir / 's65_gap_antijensen.png'
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
print(f"  Plot saved: {plot_path}")

# =============================================================================
# Summary
# =============================================================================
elapsed = time.time() - t_start
print(f"\n{'=' * 78}")
print(f"  GAP-ANTIJENSEN-65 SUMMARY")
print(f"{'=' * 78}")
print(f"  Gate: GAP-ANTIJENSEN-65 — {gate_verdict}")
print(f"  min(Delta/Delta_0) within dynamical range = {gate_value:.6f}")
print(f"  Delta(fold) = {Delta_0:.6f} M_KK")
print(f"  Delta(f=0.182) = {Delta_at_dyn:.6f} M_KK ({ratio_at_dyn:.2%} of fold)")
print(f"  Delta(f=0.50) = {Delta_path[-1]:.6f} M_KK ({Delta_ratio_path[-1]:.2%} of fold)")
if gap_closes:
    print(f"  Gap closes at f = {frac_c_interp:.4f} ({frac_c_interp/0.182:.1f}x dynamical range)")
else:
    print(f"  Gap does NOT close within range [0, {frac_values[-1]:.2f}]")
print(f"  S(fold) = {S_full_path[0]:.2f}, S(0.182) = {S_full_path[idx_dyn]:.2f} "
      f"({(S_full_path[idx_dyn]-S_full_path[0])/S_full_path[0]:.2%} change)")
print(f"  R(fold) = {R_scalar_path[0]:.6f}, R(0.182) = {R_scalar_path[idx_dyn]:.6f}")
print(f"  Elapsed: {elapsed:.2f}s")
print(f"{'=' * 78}")
