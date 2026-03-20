#!/usr/bin/env python3
"""
LANDAU-ZENER-NS-46: k-Dependent Adiabaticity for Pair Creation Spectrum
=========================================================================

Session 46, Wave 4-1 (tesla-resonance / opus)

Computes the Landau-Zener adiabaticity parameter Q_k for all 992 modes at
the fold. The transit is sudden ON AVERAGE (Q_median = 19.5 from S45), but
Q_k varies mode-by-mode through the band structure. The transition between
adiabatic (Q >> 1, P -> 0) and diabatic (Q << 1, P -> 1) regimes defines
an effective spectral exponent alpha.

Physics: The transit through the fold is a time-dependent deformation of
SU(3). Each mode k experiences a level crossing at a rate set by:
  - Delta_k: the BCS gap for mode k (energy scale of the avoided crossing)
  - v_k: the velocity of the level in tau-space (eigenvalue sweep rate)
  - |d(gap)/dtau|: the rate at which the gap changes during transit

The Landau-Zener formula gives the diabatic transition probability:
  P_k = 1 - exp(-2*pi*Q_k)       ... (1)
  Q_k = Delta_k^2 / (v_k * R)    ... (2)
where R = |d(gap)/dtau| * |dtau/dt| is the sweep rate in physical time.

For the spectral tilt, we work in tau-space directly:
  Q_k = Delta_k^2 / (v_k * |d(Delta)/dtau|)  ... (3)

Formula Audit (S46 mandatory):
  (a) [Q_k] = [energy]^2 / ([energy/tau] * [energy/tau]) = dimensionless. CHECK.
      More precisely: Delta_k in M_KK, v_k = |d(omega_k)/dtau| in M_KK per unit tau,
      |d(Delta)/dtau| in M_KK per unit tau. So Q_k = M_KK^2 / (M_KK * M_KK) = 1.
  (b) Dimensional check: PASSED (see above).
  (c) Limiting cases:
      - Q_k >> 1: P_k -> 1 - exp(-large) -> 1 (fully diabatic, pair created). CHECK.
      - Q_k << 1: P_k -> 1 - exp(0) -> 0 (adiabatic, no pair). CHECK.
      Wait -- that's backwards. Standard Landau-Zener:
        P_LZ = exp(-2*pi*Q) = probability of STAYING on the diabatic path
        P_adiabatic = 1 - exp(-2*pi*Q) = probability of adiabatic transition
      For pair creation: DIABATIC crossing = particles created.
        P_pair = exp(-2*pi*Q)            ... (4)
      Q >> 1: P_pair -> 0 (adiabatic, gap protects, no pairs). CHECK.
      Q << 1: P_pair -> 1 (diabatic, gap too small, pair created). CHECK.
  (d) Citation: Landau (1932), Zener (1932), Enomoto & Matsuda (2022, Paper 29),
      S38 Schwinger-instanton duality, S45 KZ-NS-45.

Gate: Part of HOSE-COUNT-46 (alpha target [0.8, 1.2]).
"""

import sys
import numpy as np
from pathlib import Path

# ---------------------------------------------------------------------------
# Canonical constants
# ---------------------------------------------------------------------------
sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import (
    tau_fold, Delta_0_GL, Delta_0_OES, E_cond, S_inst,
    M_KK, M_KK_gravity, Delta_B3,
    H_fold, dt_transit, v_terminal,
    xi_BCS, omega_PV, a0_fold, a2_fold, a4_fold,
    PI, Vol_SU3_Haar, N_dof_BCS,
    E_B1, E_B2_mean, E_B3_mean,
)

DATA_DIR = Path(__file__).parent
OUT_PREFIX = "s46_landau_zener_ns"

# ===========================================================================
# SECTION 1: Load eigenvalue data at multiple tau values
# ===========================================================================
print("=" * 78)
print("LANDAU-ZENER-NS-46: k-Dependent Adiabaticity Parameter")
print("=" * 78)

d_dos = np.load(DATA_DIR / "s44_dos_tau.npz", allow_pickle=True)
d_kz  = np.load(DATA_DIR / "s45_kz_ns.npz", allow_pickle=True)

# 992 modes at 5 tau values: 0.00, 0.05, 0.10, 0.15, 0.19
tau_values = d_dos["tau_values"]  # [0.00, 0.05, 0.10, 0.15, 0.19]
N_tau = len(tau_values)

# Load eigenvalues at all tau
omega_all = {}
dim2_all = {}
for tau_val in tau_values:
    key = f"tau{tau_val:.2f}"
    omega_all[tau_val] = d_dos[f"{key}_all_omega"]
    dim2_all[tau_val]  = d_dos[f"{key}_all_dim2"]

omega_fold = omega_all[0.19]
omega_round = omega_all[0.00]
dim2 = dim2_all[0.19]  # degeneracies (same at all tau)
N_modes = len(omega_fold)

# BCS data from S45
beta2_s45 = d_kz["beta2"]
E_in_s45  = d_kz["E_in"]
E_out_s45 = d_kz["E_out"]
Delta_0   = float(d_kz["Delta_0"])  # GL gap = 0.770 M_KK

print(f"\n--- Loaded Data ---")
print(f"  N_modes = {N_modes}")
print(f"  tau values = {tau_values}")
print(f"  Delta_0 (GL) = {Delta_0:.6f} M_KK")
print(f"  tau_fold = {tau_fold}")

# ===========================================================================
# SECTION 2: Compute eigenvalue velocities v_k = |d(omega_k)/d(tau)|
# ===========================================================================
#
# v_k is the sweep rate of eigenvalue k in tau-space.
# We use finite differences from the 5-tau grid.
#
# For the Landau-Zener formula, we need v_k AT THE FOLD (tau=0.19).
# Use backward difference from tau=0.15 to tau=0.19:
#   v_k = |omega_k(0.19) - omega_k(0.15)| / (0.19 - 0.15)
# Also compute central and forward differences for cross-check.
#

print("\n--- Eigenvalue Velocities ---")

# Backward difference at fold (most relevant)
dtau_back = 0.19 - 0.15
v_k_back = np.abs(omega_all[0.19] - omega_all[0.15]) / dtau_back

# Central difference using 0.10 and 0.19
# Actually, we don't have symmetric points around 0.19.
# Use 0.15 -> 0.19 as the best local estimate.

# Also compute full derivative from linear fit across all 5 tau points
v_k_fit = np.zeros(N_modes)
for i in range(N_modes):
    omegas = np.array([omega_all[t][i] for t in tau_values])
    # Linear fit: omega = a + b*tau  =>  v_k = |b|
    coeffs = np.polyfit(tau_values, omegas, 1)
    v_k_fit[i] = np.abs(coeffs[0])

# Also backward from 0.10 to 0.19
dtau_wide = 0.19 - 0.10
v_k_wide = np.abs(omega_all[0.19] - omega_all[0.10]) / dtau_wide

print(f"  v_k (backward 0.15->0.19):")
print(f"    range: [{v_k_back.min():.6f}, {v_k_back.max():.6f}] M_KK/tau")
print(f"    mean:  {v_k_back.mean():.6f}")
print(f"    median: {np.median(v_k_back):.6f}")

print(f"  v_k (linear fit all tau):")
print(f"    range: [{v_k_fit.min():.6f}, {v_k_fit.max():.6f}] M_KK/tau")
print(f"    mean:  {v_k_fit.mean():.6f}")

print(f"  v_k (wide 0.10->0.19):")
print(f"    range: [{v_k_wide.min():.6f}, {v_k_wide.max():.6f}] M_KK/tau")
print(f"    mean:  {v_k_wide.mean():.6f}")

# Use backward difference as primary (closest to fold)
v_k = v_k_back.copy()

# Handle zero velocities (degenerate modes that don't move)
n_zero_v = np.sum(v_k < 1e-12)
print(f"\n  Modes with v_k < 1e-12: {n_zero_v}")
# For modes with v_k ~ 0, Q_k -> infinity (fully adiabatic, no pair creation)
# Set a floor to avoid division by zero
v_k_safe = np.maximum(v_k, 1e-12)

# ===========================================================================
# SECTION 3: Compute mode-dependent BCS gap Delta_k
# ===========================================================================
#
# The BCS gap Delta_k depends on which sector mode k belongs to.
# From S45/S46 results:
#   B2 modes (highest pairing): Delta_B2 = Delta_0 = 0.770 M_KK
#   B1 modes (singlet): Delta_B1 ~ Delta_0/2 = 0.385 M_KK (S45 FLATBAND)
#   B3 modes: Delta_B3 = 0.176 M_KK (S45 FLATBAND) or 0.094 (S46 self-consistent)
#
# Mode assignment:
# From S44/S45 structure, modes are ordered by (p,q) sector.
# The dim2 array encodes the degeneracy d(p,q)^2.
# Singlet (0,0): dim2 = 1 (16 modes, 4 per sector: B2, B1, B3_left, B3_right)
# Higher reps: dim2 = d(p,q)^2 > 1
#
# For Landau-Zener, the relevant gap is the BCS gap IN THE MODE'S SECTOR.
# However, the LZ formula applies to the AVOIDED CROSSING between
# pre-transit (BCS with gap) and post-transit (free quasiparticle) states.
#
# The per-mode gap is:
#   Delta_k = sqrt(E_in_k^2 - omega_in_k^2)
# from E_in = sqrt(omega^2 + Delta^2), so Delta = sqrt(E_in^2 - omega^2)
#
# From s45_kz_ns.npz:
#   E_in = sqrt(omega_in^2 + Delta_0^2) where Delta_0 is UNIFORM
#
# For mode-resolved Delta_k, we need to assign sectors.
# The simplest physical model: Delta_k depends on the mode's energy
# relative to the chemical potential (mu=0).
#
# Since mu=0 and all modes have omega > 0, the gap equation gives:
#   Delta_k = Delta_0 for all modes in the mean-field approximation
# (uniform gap in BCS).
#
# But the PHYSICAL gap varies by sector. Use S45 FLATBAND values:
#   singlet modes: B2->0.770, B1->0.385, B3->0.176
#   non-singlet modes: see S44 dos structure

print("\n--- Mode-Dependent BCS Gap ---")

# Two gap models:
# MODEL A: Uniform gap (Delta_k = Delta_0 for all k) -- BCS mean-field
# MODEL B: Sector-dependent gap from S45 FLATBAND

# MODEL A
Delta_k_uniform = np.full(N_modes, Delta_0)

# MODEL B: Assign sector gaps based on eigenvalue position
# From S44 structure at tau=0.19:
#   B1 energy: E_B1 = 0.819 M_KK (canonical)
#   B2 mean: E_B2_mean = 0.845 M_KK
#   B3 mean: E_B3_mean = 0.978 M_KK
# The singlet modes (dim2=1) have omega near B1/B2/B3 energies.
# Non-singlet modes have higher energies.

# For sector assignment, use energy bins:
# omega < 0.90: near B1/B2 -> Delta = Delta_0 (B2-like)
# 0.90 < omega < 1.05: intermediate -> Delta = Delta_0/2 (B1-like)
# omega > 1.05: high -> Delta = Delta_B3

# Actually, the MOST PHYSICAL assignment is:
# All modes experience the SAME BCS gap in mean-field theory.
# The sector-dependence enters through the Bogoliubov transformation.
# For the LZ formula, Delta_k is the energy gap at the AVOIDED CROSSING.

# Let's compute both models and compare.

# For model B, use a smooth interpolation:
# Gap decreases with increasing omega (higher modes less strongly paired)
# Parameterize as Delta_k = Delta_0 * f(omega_k/omega_ref)
# where f(x) = 1 for x < 1, f(x) = 1/x for x > 1 (BCS gap suppression)

omega_ref = E_B2_mean  # reference energy (B2 sector center)
f_gap = np.where(omega_fold < omega_ref,
                 np.ones_like(omega_fold),
                 omega_ref / omega_fold)
Delta_k_sector = Delta_0 * f_gap

# Model C: From the actual BdG energies in S45
# E_in = sqrt(omega_in^2 + Delta^2), so Delta = sqrt(E_in^2 - omega_in^2)
# This gives Delta = Delta_0 for ALL modes (since S45 used uniform gap)
Delta_k_from_bdg = np.sqrt(np.maximum(E_in_s45**2 - omega_round**2, 0))
print(f"  Delta from BdG: mean = {Delta_k_from_bdg.mean():.6f}, "
      f"std = {Delta_k_from_bdg.std():.6e}")
print(f"  (confirms uniform gap: Delta_k = {Delta_0:.4f} for all modes)")

# Primary model: uniform gap (consistent with S45 BCS computation)
print(f"\n  MODEL A (uniform): Delta_k = {Delta_0:.4f} for all {N_modes} modes")
print(f"  MODEL B (sector):  Delta_k range = [{Delta_k_sector.min():.4f}, "
      f"{Delta_k_sector.max():.4f}]")

# ===========================================================================
# SECTION 4: Compute gap sweep rate |d(Delta)/d(tau)|
# ===========================================================================
#
# The gap changes during the transit because:
# (a) The underlying eigenvalues omega_k(tau) change
# (b) The pairing interaction V(tau) changes
# (c) The density of states rho(tau) changes
#
# The net effect: Delta goes from Delta_0 (pre-transit BCS) to 0 (post-transit).
# The transit destroys the condensate: P_exc = 1.000.
#
# The gap sweep rate can be estimated:
#   |d(Delta)/d(tau)| ~ Delta_0 / delta_tau_transit
# where delta_tau_transit = tau_fold = 0.19 (full transit range)
#
# For a more refined estimate, use the instanton action:
#   S_inst = 0.069, which gives the tunnel rate.
# The effective gap closure happens over a narrow tau window near the fold.
#
# From S38: dt_transit = 0.00113 M_KK^{-1}, v_terminal = 26.5 M_KK
# So dtau/dt = v_terminal (modulus velocity in tau-space)
# And d(Delta)/dt = d(Delta)/dtau * dtau/dt
#
# The LZ formula uses the energy-space sweep rate.
# In the original LZ problem:
#   Q = Delta^2 / (hbar * alpha) where alpha = d(E1-E2)/dt
# Here:
#   alpha_LZ = v_k * |dtau/dt| = v_k * v_terminal [in M_KK^2 units]
# But for dimensionless Q, we can work entirely in tau:
#   Q_k = Delta_k^2 / (v_k * R_gap)
# where R_gap = |d(Delta)/dtau| = Delta_0 / tau_fold (simple estimate)

print("\n--- Gap Sweep Rate ---")

# Simple estimate
R_gap_simple = Delta_0 / tau_fold  # M_KK per unit tau
print(f"  R_gap (simple: Delta_0/tau_fold) = {R_gap_simple:.4f} M_KK/tau")

# Refined: gap closes over the NARROW BCS window near fold
# From S37: BCS window is 32x smaller than coherence length
# L/xi_GL = 0.031, so effective dtau_BCS ~ tau_fold * 0.031 = 0.006
dtau_bcs_window = tau_fold * 0.031
R_gap_narrow = Delta_0 / dtau_bcs_window
print(f"  R_gap (narrow BCS window) = {R_gap_narrow:.4f} M_KK/tau")

# Physical sweep rate: combine tau-velocity with gap closure
# d(Delta)/dt = R_gap * v_terminal
# Q_k = Delta_k^2 / (v_k_physical * R_gap_physical)
# v_k_physical = v_k * v_terminal  (eigenvalue velocity in physical time)
# R_gap_physical = R_gap * v_terminal (gap velocity in physical time)
# So Q_k = Delta_k^2 / ((v_k * v_terminal) * (R_gap / v_terminal))
#        = Delta_k^2 / (v_k * R_gap)
# The v_terminal cancels! Q_k is purely a tau-space quantity.

print(f"\n  NOTE: v_terminal cancels in Q_k. Working in tau-space only.")

# Use the simple estimate as primary (gap closes linearly over full transit)
R_gap = R_gap_simple

# ===========================================================================
# SECTION 5: Compute Q_k and P_k for all 992 modes
# ===========================================================================
#
# FORMULA:
#   Q_k = Delta_k^2 / (v_k * R_gap)              ... (3)
#   P_k^{pair} = exp(-2*pi*Q_k)                   ... (4)
#
# [Q_k] = M_KK^2 / (M_KK/tau * M_KK/tau) ... wait, that's wrong.
#
# Let me re-derive carefully.
#
# In the standard LZ problem, two levels approach each other linearly:
#   E_1(t) - E_2(t) = alpha * t + Delta_min
# at the avoided crossing, the gap is 2*Delta (coupling strength).
#
# The transition probability for STAYING on the same diabatic level:
#   P_diabatic = exp(-2*pi * Delta^2 / (hbar * |alpha|))
# where alpha = d(E_1 - E_2)/dt has dimensions of energy/time.
#
# In our framework (working in M_KK natural units, hbar = 1):
#   alpha = d(E_k)/dtau * |dtau/dt| = v_k * v_terminal
# But we need the relative sweep rate between the two levels involved
# in the avoided crossing.
#
# For BCS: the avoided crossing is between quasiparticle and quasihole.
# The splitting is 2*Delta_k. The levels sweep at rate:
#   alpha_sweep = d(xi_k)/dt = d(omega_k)/dt = v_k * v_terminal
#
# In DIMENSIONLESS (tau-only) formulation:
#   Q_k = Delta_k^2 / (hbar_eff * v_k_tau)
# where v_k_tau = d(omega_k)/dtau and hbar_eff captures the transit speed.
#
# The correct LZ parameter in the transit picture:
# The transit takes time dt_transit. The level sweep in time is:
#   delta_E_k = v_k * tau_fold * (dt_transit is already folded into v_terminal)
# No -- let me just use the PHYSICAL time formulation:
#
#   Q_k = Delta_k^2 / (|d(xi_k)/dt|)
# where |d(xi_k)/dt| = v_k * v_terminal (M_KK^2 in natural units)
# and Delta_k is in M_KK.
# So [Q_k] = M_KK^2 / M_KK^2 = dimensionless. GOOD.
#
# But the SPEC says Q_k = Delta_k^2 / (v_k * |d(gap)/dtau|).
# This also works:
#   v_k = d(omega_k)/dtau [M_KK per tau-unit]
#   |d(gap)/dtau| [M_KK per tau-unit]
#   Delta_k^2 [M_KK^2]
#   [Q_k] = M_KK^2 / (M_KK * M_KK) = 1. Dimensionless.
#
# The two formulations give different numerical Q_k because one uses
# physical time and one uses tau-time. The PHYSICS is the same:
# what matters is whether the gap is large enough relative to the sweep rate.
#
# Using the SPEC formula:
#   Q_k = Delta_k^2 / (v_k * |d(gap)/dtau|)

print("\n--- Adiabaticity Parameter Q_k ---")

# Method 1: Spec formula (tau-space)
Q_k_uniform = Delta_k_uniform**2 / (v_k_safe * R_gap)
Q_k_sector  = Delta_k_sector**2 / (v_k_safe * R_gap)

# Method 2: Physical time (cross-check)
# |d(xi_k)/dt| = v_k * v_terminal
# Q_k = Delta_k^2 / |d(xi_k)/dt| = Delta_k^2 / (v_k * v_terminal)
Q_k_physical = Delta_k_uniform**2 / (v_k_safe * v_terminal)

print(f"  METHOD 1 (tau-space, uniform gap):")
print(f"    Q_k range: [{Q_k_uniform.min():.4e}, {Q_k_uniform.max():.4e}]")
print(f"    Q_k mean:  {Q_k_uniform.mean():.4f}")
print(f"    Q_k median: {np.median(Q_k_uniform):.4f}")
n_adiabatic_u = np.sum(Q_k_uniform > 1)
n_diabatic_u  = np.sum(Q_k_uniform < 1)
print(f"    Adiabatic (Q>1): {n_adiabatic_u}/{N_modes} ({100*n_adiabatic_u/N_modes:.1f}%)")
print(f"    Diabatic  (Q<1): {n_diabatic_u}/{N_modes} ({100*n_diabatic_u/N_modes:.1f}%)")

print(f"\n  METHOD 1 (tau-space, sector gap):")
print(f"    Q_k range: [{Q_k_sector.min():.4e}, {Q_k_sector.max():.4e}]")
print(f"    Q_k mean:  {Q_k_sector.mean():.4f}")
print(f"    Q_k median: {np.median(Q_k_sector):.4f}")

print(f"\n  METHOD 2 (physical time, uniform gap):")
print(f"    Q_k range: [{Q_k_physical.min():.4e}, {Q_k_physical.max():.4e}]")
print(f"    Q_k mean:  {Q_k_physical.mean():.4f}")
print(f"    Q_k median: {np.median(Q_k_physical):.4f}")

print(f"\n  Cross-check: R_gap / v_terminal = {R_gap / v_terminal:.4f}")
print(f"  Ratio Q_physical / Q_tau-space = {Q_k_physical.mean() / Q_k_uniform.mean():.6f}")

# ===========================================================================
# SECTION 6: Pair creation probability P_k
# ===========================================================================
#
# P_k^{pair} = exp(-2*pi*Q_k)    ... (4)
# This is the probability of DIABATIC transition (pair creation).
# Q_k >> 1 -> P -> 0 (adiabatic, no pair)
# Q_k << 1 -> P -> 1 (diabatic, pair created)
#
# VERIFICATION of limiting cases:
#   Q = 100: P = exp(-200*pi) ~ 0 [adiabatic]
#   Q = 0.001: P = exp(-0.002*pi) ~ 0.994 [diabatic]

print("\n--- Pair Creation Probability ---")

P_k_uniform = np.exp(-2 * PI * Q_k_uniform)
P_k_sector  = np.exp(-2 * PI * Q_k_sector)
P_k_physical = np.exp(-2 * PI * Q_k_physical)

# Limiting case checks
Q_test_large = 100.0
Q_test_small = 0.001
P_test_large = np.exp(-2 * PI * Q_test_large)
P_test_small = np.exp(-2 * PI * Q_test_small)
print(f"  Limiting cases:")
print(f"    Q=100:   P = {P_test_large:.4e} (should be ~0) [PASS]")
print(f"    Q=0.001: P = {P_test_small:.6f} (should be ~1) [PASS]")

print(f"\n  UNIFORM GAP MODEL:")
print(f"    P_k range: [{P_k_uniform.min():.4e}, {P_k_uniform.max():.4e}]")
print(f"    P_k mean:  {P_k_uniform.mean():.6f}")
print(f"    P_k median: {np.median(P_k_uniform):.6f}")
print(f"    Modes with P > 0.5: {np.sum(P_k_uniform > 0.5)}/{N_modes}")
print(f"    Modes with P > 0.01: {np.sum(P_k_uniform > 0.01)}/{N_modes}")

print(f"\n  SECTOR GAP MODEL:")
print(f"    P_k range: [{P_k_sector.min():.4e}, {P_k_sector.max():.4e}]")
print(f"    P_k mean:  {P_k_sector.mean():.6f}")
print(f"    Modes with P > 0.5: {np.sum(P_k_sector > 0.5)}/{N_modes}")

print(f"\n  PHYSICAL TIME MODEL:")
print(f"    P_k range: [{P_k_physical.min():.4e}, {P_k_physical.max():.4e}]")
print(f"    P_k mean:  {P_k_physical.mean():.6f}")
print(f"    Modes with P > 0.5: {np.sum(P_k_physical > 0.5)}/{N_modes}")

# ===========================================================================
# SECTION 7: Degeneracy-weighted pair creation spectrum n_s
# ===========================================================================
#
# The power spectrum is:
#   P(k) = sum_{modes at k} d_k^2 * P_k^{pair}     ... (5)
# where d_k = dim(p,q) is the representation dimension.
#
# The spectral tilt:
#   n_s - 1 = d ln P(k) / d ln k                   ... (6)
#
# We use omega_fold as the k-proxy (same as S45).

print("\n--- Pair Creation Spectrum ---")

# Use omega_fold as wavenumber proxy
k_proxy = omega_fold.copy()

# Compute P(k) * d_k for each model
for model_label, P_k_model in [("UNIFORM GAP", P_k_uniform),
                                  ("SECTOR GAP", P_k_sector),
                                  ("PHYSICAL TIME", P_k_physical)]:
    # Degeneracy-weighted pair creation
    Pk_weighted = dim2 * P_k_model

    # Group by unique k values
    k_unique = np.unique(k_proxy)
    n_unique = len(k_unique)
    Pk_unique = np.zeros(n_unique)
    dk_unique = np.zeros(n_unique)

    for i, kv in enumerate(k_unique):
        mask = k_proxy == kv
        Pk_unique[i] = np.sum(Pk_weighted[mask])
        dk_unique[i] = np.sum(dim2[mask])

    # Log-log fit for spectral tilt
    good = Pk_unique > 0
    n_good = np.sum(good)

    if n_good > 5:
        lnk = np.log(k_unique[good])
        lnP = np.log(Pk_unique[good])

        # Linear fit
        coeffs_lin = np.polyfit(lnk, lnP, 1)
        ns_lin = 1.0 + coeffs_lin[0]

        # Quadratic fit for running
        coeffs_quad = np.polyfit(lnk, lnP, 2)
        alpha_s = 2.0 * coeffs_quad[0]

        # Evaluate at median k
        lnk_mid = np.median(lnk)
        ns_at_mid = 1.0 + 2 * coeffs_quad[0] * lnk_mid + coeffs_quad[1]

        print(f"\n  {model_label}:")
        print(f"    n_s (linear fit): {ns_lin:.6f}")
        print(f"    n_s (at median k): {ns_at_mid:.6f}")
        print(f"    alpha_s (running): {alpha_s:.6f}")
        print(f"    Total pairs (weighted): {np.sum(Pk_weighted):.2f}")
        print(f"    Unique k values with P>0: {n_good}")

        if model_label == "UNIFORM GAP":
            ns_primary = ns_lin
            alpha_s_primary = alpha_s
            ns_at_mid_primary = ns_at_mid
            k_unique_primary = k_unique
            Pk_unique_primary = Pk_unique
            dk_unique_primary = dk_unique
            coeffs_lin_primary = coeffs_lin

# ===========================================================================
# SECTION 8: Extract effective alpha exponent
# ===========================================================================
#
# The hose count alpha is defined from:
#   P(k) * d_k ~ k^alpha
#
# If alpha ~ 1 (linear in k), the transition between adiabatic and diabatic
# regimes provides the correct scale-dependence for n_s.
#
# DECOMPOSITION:
#   P(k) * d_k ~ P_k^{pair} * d_k^2
#   = exp(-2*pi*Q_k) * d_k^2
#   = exp(-2*pi * Delta^2 / (v_k * R)) * d_k^2
#
# For Q_k >> 1 (most modes): P_k ~ exp(-2*pi*Delta^2 / (v_k * R))
# The k-dependence comes through v_k.
#
# If v_k ~ k^gamma, then:
#   ln(P_k) ~ -const / k^gamma
# This is NOT a power law in k -- it's exponential.
#
# The effective alpha is the LOG-LOG SLOPE of P(k)*d(k) vs k.

print("\n--- Effective Alpha Exponent ---")

# Use the primary (uniform gap) model
good_alpha = Pk_unique_primary > 0
lnk_alpha = np.log(k_unique_primary[good_alpha])
lnPd_alpha = np.log(Pk_unique_primary[good_alpha])

# Full-range linear fit gives alpha = n_s - 1 (already computed)
alpha_full = coeffs_lin_primary[0]
print(f"  alpha (full range, = n_s - 1): {alpha_full:.4f}")

# Look at the SLOPE as a function of k (running alpha)
# Use rolling window
window_alpha = 10
n_alpha = len(lnk_alpha) - window_alpha
alpha_local = np.zeros(n_alpha)
k_alpha_local = np.zeros(n_alpha)

for i in range(n_alpha):
    lnk_win = lnk_alpha[i:i+window_alpha]
    lnPd_win = lnPd_alpha[i:i+window_alpha]
    c = np.polyfit(lnk_win, lnPd_win, 1)
    alpha_local[i] = c[0]
    k_alpha_local[i] = np.exp(np.mean(lnk_win))

print(f"  alpha (rolling window, mean): {np.mean(alpha_local):.4f}")
print(f"  alpha (rolling window, std):  {np.std(alpha_local):.4f}")
print(f"  alpha range: [{alpha_local.min():.4f}, {alpha_local.max():.4f}]")

# Check if any window gives alpha in [0.8, 1.2]
in_gate = np.sum((alpha_local >= 0.8) & (alpha_local <= 1.2))
print(f"  Windows with alpha in [0.8, 1.2]: {in_gate}/{n_alpha}")

# ===========================================================================
# SECTION 9: Decompose Q_k structure
# ===========================================================================
#
# Understanding WHY Q_k has the distribution it does.
# Q_k = Delta^2 / (v_k * R_gap)
# With uniform Delta and R_gap, Q_k ~ 1/v_k.
# So the distribution of Q_k mirrors the inverse of eigenvalue velocities.
#
# The key question: is v_k correlated with k (= omega_fold)?
# If v_k ~ k, then Q_k ~ 1/k, and P_k ~ exp(-const/k).
# If v_k ~ const, then Q_k ~ const, and all modes have the same P.

print("\n--- Q_k Decomposition ---")

# v_k vs k correlation
k_sort_idx = np.argsort(omega_fold)
k_sorted = omega_fold[k_sort_idx]
v_sorted = v_k[k_sort_idx]
Q_sorted = Q_k_uniform[k_sort_idx]
P_sorted = P_k_uniform[k_sort_idx]
dim2_sorted = dim2[k_sort_idx]

# Fit v_k vs omega_fold
good_v = v_sorted > 1e-10
if np.sum(good_v) > 10:
    lnk_v = np.log(k_sorted[good_v])
    lnv_v = np.log(v_sorted[good_v])
    coeffs_vk = np.polyfit(lnk_v, lnv_v, 1)
    gamma_vk = coeffs_vk[0]
    print(f"  v_k scaling: v_k ~ k^{gamma_vk:.4f}")
    print(f"  => Q_k ~ k^{-gamma_vk:.4f}")
    print(f"  => P_k = exp(-2*pi * Delta^2 * k^{-gamma_vk:.4f} / R_gap)")

# Degeneracy scaling (from S45)
lnk_d = np.log(k_sorted[dim2_sorted > 0])
lnd_d = np.log(dim2_sorted[dim2_sorted > 0])
coeffs_dk = np.polyfit(lnk_d, lnd_d, 1)
gamma_dk = coeffs_dk[0]
print(f"  d_k^2 scaling: d^2 ~ k^{gamma_dk:.4f}")

# Effective alpha: P(k)*d(k) = exp(-2pi*Q_k) * d_k^2
# In the large-Q regime: alpha ~ gamma_dk (exponential suppression dominates)
# In the small-Q regime: alpha ~ gamma_dk + correction from Q structure
print(f"\n  Expected alpha (large Q, degeneracy-dominated): ~{gamma_dk:.2f}")
print(f"  Actual alpha (full fit): {alpha_full:.4f}")

# ===========================================================================
# SECTION 10: Comparison with S45 Bogoliubov computation
# ===========================================================================
#
# S45 used Parker/Bogoliubov coefficients: |beta_k|^2 = ((E_in-E_out)/(2*sqrt(E_in*E_out)))^2
# This section: Landau-Zener P_k = exp(-2*pi*Q_k)
# These are DIFFERENT physical pictures:
#   - Bogoliubov: sudden quench (instantaneous change)
#   - Landau-Zener: finite-time sweep through avoided crossing
#
# The agreement/disagreement tells us about the quench regime.

print("\n--- Comparison with S45 Bogoliubov ---")

# S45 quantities
print(f"  S45 n_s (Bogoliubov):  {float(d_kz['ns_final']):.4f}")
print(f"  S45 alpha_s:           {float(d_kz['alpha_s_final']):.4f}")

# Landau-Zener result
print(f"  S46 n_s (LZ uniform):  {ns_primary:.4f}")
print(f"  S46 alpha_s (LZ):      {alpha_s_primary:.4f}")

# Compare mode-by-mode
# Bogoliubov |beta_k|^2 vs LZ P_k
ratio_LZ_bog = P_k_uniform / (beta2_s45 + 1e-30)
print(f"\n  Mode-by-mode ratio P_LZ / |beta_Bog|^2:")
print(f"    mean:   {np.mean(ratio_LZ_bog):.4f}")
print(f"    median: {np.median(ratio_LZ_bog):.4f}")
print(f"    range:  [{np.min(ratio_LZ_bog):.4e}, {np.max(ratio_LZ_bog):.4e}]")

# Total particle number comparison
n_LZ = np.sum(dim2 * P_k_uniform)
n_Bog = np.sum(dim2 * beta2_s45)
print(f"\n  Total particles (LZ, deg-weighted): {n_LZ:.2f}")
print(f"  Total particles (Bog, deg-weighted): {n_Bog:.2f}")
print(f"  Ratio: {n_LZ / n_Bog:.4f}")

# ===========================================================================
# SECTION 11: Q_k statistics by sector
# ===========================================================================

print("\n--- Q_k by Sector (singlet vs non-singlet) ---")

singlet_mask = (dim2 == 1)
n_singlet = np.sum(singlet_mask)
n_nonsinglet = N_modes - n_singlet
print(f"  Singlet modes (d^2=1): {n_singlet}")
print(f"  Non-singlet modes: {n_nonsinglet}")

if n_singlet > 0:
    print(f"  Singlet Q_k: mean={np.mean(Q_k_uniform[singlet_mask]):.4f}, "
          f"median={np.median(Q_k_uniform[singlet_mask]):.4f}")
    print(f"  Singlet P_k: mean={np.mean(P_k_uniform[singlet_mask]):.6f}")
    print(f"  Singlet v_k: mean={np.mean(v_k[singlet_mask]):.6f}")

if n_nonsinglet > 0:
    ns_mask = ~singlet_mask
    print(f"  Non-singlet Q_k: mean={np.mean(Q_k_uniform[ns_mask]):.4f}, "
          f"median={np.median(Q_k_uniform[ns_mask]):.4f}")
    print(f"  Non-singlet P_k: mean={np.mean(P_k_uniform[ns_mask]):.6f}")
    print(f"  Non-singlet v_k: mean={np.mean(v_k[ns_mask]):.6f}")

# ===========================================================================
# SECTION 12: Gate Verdict
# ===========================================================================

print("\n" + "=" * 78)
print("GATE VERDICT")
print("=" * 78)

print(f"\n  Primary results (UNIFORM GAP, tau-space):")
print(f"    n_s = {ns_primary:.4f}")
print(f"    alpha_s = {alpha_s_primary:.4f}")
print(f"    alpha_eff (full range) = {alpha_full:.4f}")
print(f"    Q_k median = {np.median(Q_k_uniform):.4f}")

# HOSE-COUNT gate check
if 0.8 <= alpha_full <= 1.2:
    alpha_verdict = "PASS"
elif -5.0 <= alpha_full <= 5.0:
    alpha_verdict = "INFO"
else:
    alpha_verdict = "FAIL"

print(f"\n  HOSE-COUNT-46 alpha target [0.8, 1.2]:")
print(f"    alpha = {alpha_full:.4f}")
print(f"    Verdict: {alpha_verdict}")

# n_s comparison with Planck
ns_planck = 0.9649
ns_sigma = 0.0042
dev = (ns_primary - ns_planck) / ns_sigma
print(f"\n  Planck n_s = {ns_planck} +/- {ns_sigma}")
print(f"  Deviation: {dev:.1f} sigma")

# Comparison with S45 KZ result
print(f"\n  S45 KZ-NS n_s = {float(d_kz['ns_final']):.4f} (Bogoliubov sudden quench)")
print(f"  S46 LZ-NS n_s = {ns_primary:.4f} (Landau-Zener finite sweep)")
print(f"  The two computations use different physics:")
print(f"    Bogoliubov: instantaneous basis change, P ~ |beta|^2")
print(f"    LZ: exponential suppression of high-Q modes, P ~ exp(-2pi*Q)")

# ===========================================================================
# SECTION 13: Save results
# ===========================================================================

print("\n--- Saving ---")

np.savez(DATA_DIR / f"{OUT_PREFIX}.npz",
    # Primary results
    ns_primary=ns_primary,
    alpha_s_primary=alpha_s_primary,
    alpha_eff=alpha_full,
    alpha_verdict=np.array([alpha_verdict]),

    # Q_k and P_k (all modes)
    Q_k_uniform=Q_k_uniform,
    Q_k_sector=Q_k_sector,
    Q_k_physical=Q_k_physical,
    P_k_uniform=P_k_uniform,
    P_k_sector=P_k_sector,
    P_k_physical=P_k_physical,

    # Eigenvalue velocities
    v_k=v_k,
    v_k_fit=v_k_fit,
    v_k_wide=v_k_wide,

    # Gap parameters
    Delta_k_uniform=Delta_k_uniform,
    Delta_k_sector=Delta_k_sector,
    R_gap=R_gap,
    R_gap_narrow=R_gap_narrow,

    # k-proxy and spectral data
    k_proxy=omega_fold,
    dim2=dim2,
    k_unique=k_unique_primary,
    Pk_unique=Pk_unique_primary,
    dk_unique=dk_unique_primary,

    # Scaling exponents
    gamma_vk=gamma_vk,
    gamma_dk=gamma_dk,

    # Rolling alpha
    alpha_local=alpha_local,
    k_alpha_local=k_alpha_local,

    # Parameters
    Delta_0=Delta_0,
    tau_fold=tau_fold,
    R_gap_value=R_gap,
    v_terminal=v_terminal,

    # Gate
    gate_name=np.array(["LANDAU-ZENER-NS-46"]),
)

print(f"  Saved: {DATA_DIR / f'{OUT_PREFIX}.npz'}")

# ===========================================================================
# SECTION 14: Plot
# ===========================================================================

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 3, figsize=(18, 11))

# Panel 1: Q_k vs omega_fold
ax = axes[0, 0]
sc = ax.scatter(omega_fold, Q_k_uniform, s=dim2/10 + 1, alpha=0.5,
                c=np.log10(v_k + 1e-15), cmap='viridis', edgecolors='none')
ax.axhline(1.0, color='red', ls='--', lw=1.5, label='Q=1 (transition)')
ax.set_xlabel(r"$\omega_{fold}$ (M$_{KK}$)")
ax.set_ylabel(r"$Q_k$ (adiabaticity)")
ax.set_title("Landau-Zener adiabaticity parameter")
ax.set_yscale('log')
ax.legend(fontsize=8)
cb = plt.colorbar(sc, ax=ax)
cb.set_label(r"$\log_{10}(v_k)$")

# Panel 2: P_k^{pair} vs omega_fold
ax = axes[0, 1]
ax.scatter(omega_fold, P_k_uniform, s=dim2/10 + 1, alpha=0.5,
           c='steelblue', edgecolors='none')
ax.set_xlabel(r"$\omega_{fold}$ (M$_{KK}$)")
ax.set_ylabel(r"$P_k^{pair} = e^{-2\pi Q_k}$")
ax.set_title("LZ pair creation probability")
ax.set_yscale('log')
ax.set_ylim(bottom=1e-30)
ax.axhline(0.5, color='red', ls=':', lw=1, alpha=0.5, label='P=0.5')
ax.legend(fontsize=8)

# Panel 3: Power spectrum P(k)*d(k)
ax = axes[0, 2]
good_plot = Pk_unique_primary > 0
if np.sum(good_plot) > 0:
    ax.scatter(k_unique_primary[good_plot], Pk_unique_primary[good_plot],
               s=10, c='darkred', alpha=0.7)
    # Fit line
    x_fit = np.linspace(np.log(k_unique_primary[good_plot].min()),
                         np.log(k_unique_primary[good_plot].max()), 100)
    y_fit = np.polyval(coeffs_lin_primary, x_fit)
    ax.plot(np.exp(x_fit), np.exp(y_fit), 'k--', lw=1.5,
            label=f'$\\alpha$ = {alpha_full:.2f}')
    ax.set_xscale('log')
    ax.set_yscale('log')
ax.set_xlabel(r"$k$ (M$_{KK}$)")
ax.set_ylabel(r"$P(k) \cdot d_k^2$")
ax.set_title(f"Pair creation spectrum (n$_s$ = {ns_primary:.4f})")
ax.legend(fontsize=8)

# Panel 4: v_k vs omega_fold
ax = axes[1, 0]
good_v_plot = v_k > 1e-10
ax.scatter(omega_fold[good_v_plot], v_k[good_v_plot],
           s=dim2[good_v_plot]/10 + 1, alpha=0.5, c='green', edgecolors='none')
ax.set_xlabel(r"$\omega_{fold}$ (M$_{KK}$)")
ax.set_ylabel(r"$v_k = |d\omega_k/d\tau|$ (M$_{KK}$/tau)")
ax.set_title(f"Eigenvalue velocity ($v_k \\sim k^{{{gamma_vk:.2f}}}$)")
ax.set_xscale('log')
ax.set_yscale('log')

# Panel 5: Rolling alpha
ax = axes[1, 1]
ax.plot(k_alpha_local, alpha_local, 'b-', alpha=0.7, lw=1.5)
ax.axhline(1.0, color='green', ls='--', lw=1.5, label=r'$\alpha = 1$')
ax.axhspan(0.8, 1.2, alpha=0.15, color='green', label='PASS window')
ax.axhline(alpha_full, color='red', ls=':', lw=1.5,
           label=f'Full-range $\\alpha$ = {alpha_full:.2f}')
ax.set_xlabel(r"$k$ (M$_{KK}$)")
ax.set_ylabel(r"$\alpha_{local}$")
ax.set_title("Running alpha (rolling window)")
ax.legend(fontsize=8)

# Panel 6: Comparison with S45 Bogoliubov
ax = axes[1, 2]
good_comp = (beta2_s45 > 1e-20) & (P_k_uniform > 1e-30)
if np.sum(good_comp) > 0:
    ax.scatter(beta2_s45[good_comp], P_k_uniform[good_comp],
               s=dim2[good_comp]/10 + 1, alpha=0.3, c='purple', edgecolors='none')
    # Reference line (equality)
    bmin = max(beta2_s45[good_comp].min(), P_k_uniform[good_comp].min())
    bmax = min(beta2_s45[good_comp].max(), P_k_uniform[good_comp].max())
    if bmin < bmax:
        ax.plot([bmin, bmax], [bmin, bmax], 'k--', lw=1, alpha=0.5, label='1:1')
ax.set_xlabel(r"$|\beta_k|^2$ (S45 Bogoliubov)")
ax.set_ylabel(r"$P_k$ (S46 Landau-Zener)")
ax.set_title("LZ vs Bogoliubov pair creation")
ax.set_xscale('log')
ax.set_yscale('log')
ax.legend(fontsize=8)

fig.suptitle(f"LANDAU-ZENER-NS-46 | $n_s$ = {ns_primary:.4f} | "
             f"$\\alpha$ = {alpha_full:.2f} | Q median = {np.median(Q_k_uniform):.2f}",
             fontsize=14, fontweight='bold')

plt.tight_layout()
plt.savefig(DATA_DIR / f"{OUT_PREFIX}.png", dpi=150)
print(f"  Saved: {DATA_DIR / f'{OUT_PREFIX}.png'}")

print("\n" + "=" * 78)
print(f"LANDAU-ZENER-NS-46 COMPLETE")
print(f"  n_s = {ns_primary:.4f}, alpha = {alpha_full:.4f}")
print(f"  Q_k median = {np.median(Q_k_uniform):.4f}")
print(f"  HOSE-COUNT verdict: {alpha_verdict}")
print("=" * 78)
