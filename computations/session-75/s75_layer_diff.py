#!/usr/bin/env python3
"""
s75_layer_diff.py — Layer 1 vs Layer 2 BCS Sound Speed Comparison
===================================================================

Gate: S75-C3-LAYER-DIFF
  PASS: max(delta_c_b) < 0.01 (layers agree)
  INFO: 0.01 < max(delta_c_b) < 0.10
  FAIL: max(delta_c_b) > 0.10 (significant discrepancy)

Physics:
  Layer 1 (Jacobson a_2-emergent): c_b^(1) = c_Gold * (omega_b / omega_max)
    The a_2 Seeley-DeWitt coefficient generates the emergent metric. Each BCS
    branch inherits a fraction of the Goldstone sound speed proportional to its
    quasiparticle frequency relative to the maximum frequency in the spectrum.

  Layer 2 (BCS-dressed acoustic): omega_b(k) = sqrt(v_F^2 (k - k_F)^2 + Delta_b^2)
    The BCS dispersion relation for quasiparticles near the Fermi surface.
    The group velocity is v_g = d omega / dk = v_F^2 (k - k_F) / omega_b(k).
    At k = k_F this is exactly zero (gap minimum). The PROPAGATING group velocity
    for acoustic modes is evaluated at the characteristic momentum where the
    single-particle energy eps_b sets the scale: (k - k_F) ~ eps_b / v_F.
    Then: c_b^(2) = v_F * eps_b / omega_b = v_F * eps_b / sqrt(eps_b^2 + Delta_b^2).

  The comparison tests whether the two layers (emergent geometry vs BCS condensate)
  give the same per-branch propagation speeds. If they differ, the D-R2-2 dissent
  from S74 is substantiated: different layers give different horizon-crossing times,
  and hence different contributions to n_s.

Input data:
  - canonical_constants.py: c_Gold, Delta_BCS, omega_L1, etc.
  - s74_transfer_function.npz: omega_B1, omega_B2, omega_B3, c_B1, c_B2, c_B3
  - s56_gge_fabric.npz: eps_fold (8 single-particle energies at fold)

Mode-to-sector mapping (8 modes -> 3 sectors):
  B1 = mode 0 (acoustic, eps ~ 0)
  B2 = modes 1,2,3,4 (four-fold degenerate flat band)
  B3 = modes 5,6,7 (triplet dispersive)

Session 75
"""
import sys
import os
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    c_Gold, Delta_BCS, planck_ns, planck_ns_err,
    omega_L1, omega_L2, omega_H1, omega_H2, omega_H3,
    E_B1, E_B2_mean, E_B3_mean, Delta_B3, tau_fold,
    c_fabric, H_fold, dt_transit, M_KK
)

# ==============================================================================
#  SECTION 0: Load input data
# ==============================================================================

print("=" * 78)
print("S75-C3-LAYER-DIFF: Layer 1 vs Layer 2 BCS Sound Speed Comparison")
print("=" * 78)
print()

# Load S74 transfer function data (Layer 1 sector-level values)
s74 = np.load(os.path.join(os.path.dirname(__file__), 's74_transfer_function.npz'),
              allow_pickle=True)
omega_B1_s74 = float(s74['omega_B1'])  # (local)
omega_B2_s74 = float(s74['omega_B2'])  # (local)
omega_B3_s74 = float(s74['omega_B3'])  # (local)
c_B1_s74 = float(s74['c_B1'])  # (local) Layer 1 from S74
c_B2_s74 = float(s74['c_B2'])  # (local)
c_B3_s74 = float(s74['c_B3'])  # (local)

# Load S56 GGE fabric data (per-mode single-particle energies)
s56 = np.load(os.path.join(os.path.dirname(__file__), 's56_gge_fabric.npz'),
              allow_pickle=True)
eps_fold = s56['eps_fold']  # (local) 8 single-particle energies at fold (M_KK units)

print("SECTION 0: Input data loaded")
print("-" * 78)
print(f"  S74 sector frequencies: omega_B1={omega_B1_s74:.6f}, "
      f"omega_B2={omega_B2_s74:.6f}, omega_B3={omega_B3_s74:.6f}")
print(f"  S74 sector velocities:  c_B1={c_B1_s74:.6e}, "
      f"c_B2={c_B2_s74:.6e}, c_B3={c_B3_s74:.6e}")
print(f"  S56 eps_fold (8 modes): {eps_fold}")
print(f"  Delta_BCS = {Delta_BCS:.6f} M_KK")
print(f"  c_Gold    = {c_Gold:.6f} M_KK")
print()

# ==============================================================================
#  SECTION 1: Per-mode BCS quasiparticle frequencies
# ==============================================================================

print("SECTION 1: Per-mode BCS quasiparticle structure")
print("-" * 78)

# Mode-to-sector mapping
# B1 = mode 0 (acoustic)
# B2 = modes 1,2,3,4 (flat-band quartet)
# B3 = modes 5,6,7 (dispersive triplet)
mode_labels = ['B1[0]', 'B2[1]', 'B2[2]', 'B2[3]', 'B2[4]',
               'B3[5]', 'B3[6]', 'B3[7]']  # (local)
sector_map = [0, 1, 1, 1, 1, 2, 2, 2]  # (local) 0=B1, 1=B2, 2=B3
sector_names = ['B1', 'B2', 'B3']  # (local)

# Single-particle energies at fold
eps_b = np.abs(eps_fold)  # (local) take absolute values (mode 0 is ~0)

# BCS quasiparticle frequency: omega_b = sqrt(eps_b^2 + Delta_b^2)
# The gap Delta_b may differ per sector. For B1 and B2, use the global Delta_BCS.
# For B3, use Delta_B3 (smaller gap due to distance from Fermi surface).
Delta_per_mode = np.full(8, Delta_BCS)  # (local) default: global BCS gap
Delta_per_mode[5:8] = Delta_B3  # B3 modes use the B3-sector gap

omega_b = np.sqrt(eps_b**2 + Delta_per_mode**2)  # (local) BCS quasiparticle frequencies

print("  Mode |  eps_b (M_KK) |  Delta_b (M_KK) |  omega_b (M_KK) |  sector")
print("  " + "-" * 72)
for i in range(8):
    print(f"  {mode_labels[i]:6s}| {eps_b[i]:13.6f} | {Delta_per_mode[i]:15.6f} | "
          f"{omega_b[i]:15.6f} | {sector_names[sector_map[i]]}")

# Sector-averaged frequencies (for comparison with S74)
omega_B1_calc = omega_b[0]  # (local) single mode
omega_B2_calc = np.mean(omega_b[1:5])  # (local) average of 4 modes
omega_B3_calc = np.mean(omega_b[5:8])  # (local) average of 3 modes

print()
print(f"  Sector averages: omega_B1={omega_B1_calc:.6f}, "
      f"omega_B2={omega_B2_calc:.6f}, omega_B3={omega_B3_calc:.6f}")
print(f"  S74 values:      omega_B1={omega_B1_s74:.6f}, "
      f"omega_B2={omega_B2_s74:.6f}, omega_B3={omega_B3_s74:.6f}")

# omega_max: the maximum quasiparticle frequency across all 8 modes
omega_max = np.max(omega_b)  # (local)
print(f"  omega_max = {omega_max:.6f} M_KK (mode {np.argmax(omega_b)})")
print()

# ==============================================================================
#  SECTION 2: Layer 1 — Jacobson a_2-emergent sound speeds
# ==============================================================================

print("SECTION 2: Layer 1 (Jacobson a_2-emergent) sound speeds")
print("-" * 78)

# Layer 1 formula: c_b^(1) = c_Gold * (omega_b / omega_max)
#
# Physical origin: The emergent metric from the a_2 Seeley-DeWitt coefficient
# sets the maximum propagation speed c_Gold (the Goldstone speed). Each BCS
# branch propagates at a fraction of this speed determined by the ratio of its
# quasiparticle energy to the cutoff energy. This is the "top-down" route:
# geometry (a_2) determines propagation.
#
# Eq. (1): c_b^(1) = c_Gold * omega_b / omega_max

c_L1 = c_Gold * omega_b / omega_max  # (local) Layer 1 per-mode sound speeds

print("  Formula: c_b^(1) = c_Gold * omega_b / omega_max")
print(f"  c_Gold = {c_Gold:.6f}, omega_max = {omega_max:.6f}")
print()
print("  Mode |  omega_b/omega_max |  c_L1 (M_KK) |  sector")
print("  " + "-" * 60)
for i in range(8):
    print(f"  {mode_labels[i]:6s}| {omega_b[i]/omega_max:18.6f} | {c_L1[i]:13.6e} | "
          f"{sector_names[sector_map[i]]}")

# Sector averages for Layer 1
c_L1_B1 = c_L1[0]  # (local)
c_L1_B2 = np.mean(c_L1[1:5])  # (local)
c_L1_B3 = np.mean(c_L1[5:8])  # (local)

print()
print(f"  Layer 1 sector averages: c_B1={c_L1_B1:.6e}, "
      f"c_B2={c_L1_B2:.6e}, c_B3={c_L1_B3:.6e}")
print(f"  S74 stored values:       c_B1={c_B1_s74:.6e}, "
      f"c_B2={c_B2_s74:.6e}, c_B3={c_B3_s74:.6e}")
print()

# ==============================================================================
#  SECTION 3: Layer 2 — BCS-dressed acoustic sound speeds
# ==============================================================================

print("SECTION 3: Layer 2 (BCS-dressed acoustic) sound speeds")
print("-" * 78)

# Layer 2 formula: BCS dispersion omega_b(k) = sqrt(v_F^2 (k-k_F)^2 + Delta_b^2)
#
# Group velocity: v_g = d omega / dk = v_F^2 (k - k_F) / omega_b(k)
#
# At k = k_F: v_g = 0 (gap minimum). For propagating modes, evaluate at the
# characteristic momentum where the kinetic energy equals the single-particle
# energy: v_F * (k - k_F) = eps_b, so (k - k_F) = eps_b / v_F.
#
# Substituting:
#   v_g = v_F * eps_b / sqrt(eps_b^2 + Delta_b^2) = v_F * eps_b / omega_b
#
# Eq. (2): c_b^(2) = v_F * eps_b / omega_b
#
# What is v_F? In the fiber lattice, v_F is the Fermi velocity. The natural
# identification is with the Bogoliubov-Anderson sound speed c_BA (the
# characteristic velocity for BCS quasiparticles). In S74, c_BA = 0.399 M_KK
# was used. But the FUNDAMENTAL Fermi velocity on the fiber lattice is c_Gold
# (the Goldstone speed), since c_Gold is the maximum group velocity of the
# acoustic branch before BCS dressing.
#
# We compute Layer 2 with v_F = c_Gold for apples-to-apples comparison with
# Layer 1, which also uses c_Gold as its velocity scale.
# We also check v_F = c_BA = 0.399 as the S74 convention.

v_F_primary = c_Gold  # (local) primary: Goldstone speed as Fermi velocity
c_BA_s74 = 0.399  # (local) S74 Bogoliubov-Anderson sound speed

# Layer 2 with v_F = c_Gold
c_L2_cGold = np.zeros(8)  # (local)
for i in range(8):
    if eps_b[i] < 1e-10:
        # Mode 0 (B1 acoustic): eps -> 0, so c_b^(2) -> 0.
        # But this is the GAP MINIMUM regime. For the B1 acoustic branch,
        # the physical sound speed is NOT the BCS group velocity at k_F.
        # It is the sound speed of the gapless Goldstone mode.
        # In the BCS limit, the acoustic branch is the Anderson-Bogoliubov
        # phonon with c_AB = v_F / sqrt(d) where d is the spatial dimension.
        # For d=1 (fiber lattice): c_AB = v_F.
        # We use: c_B1^(2) = v_F * (1 - (Delta/omega_min)^2)^{1/2} where
        # omega_min is the minimum nonzero quasiparticle frequency.
        # Since eps_B1 ~ 0 and omega_B1 ~ Delta, this gives c_B1^(2) ~ 0.
        # The physical resolution: B1 is the Nambu-Goldstone boson of the
        # broken U(1). Its speed is set by the condensate density and
        # compressibility, not by the BCS gap formula.
        # We use c_B1_NG = v_F * sqrt(n_cond / n_total) as the NG speed.
        # At the fold, n_cond/n_total ~ 1 (full condensation), so c_B1_NG ~ v_F.
        # This is a KNOWN subtlety: the BCS gap formula gives v_g = 0 for the
        # acoustic branch because eps_B1 = 0, but the physical Goldstone mode
        # propagates at c_AB = v_F.
        c_L2_cGold[i] = v_F_primary  # Goldstone (Anderson-Bogoliubov) mode
    else:
        c_L2_cGold[i] = v_F_primary * eps_b[i] / omega_b[i]

# Layer 2 with v_F = c_BA (S74 convention)
c_L2_cBA = np.zeros(8)  # (local)
for i in range(8):
    if eps_b[i] < 1e-10:
        c_L2_cBA[i] = c_BA_s74  # Anderson-Bogoliubov mode
    else:
        c_L2_cBA[i] = c_BA_s74 * eps_b[i] / omega_b[i]

print("  Formula: c_b^(2) = v_F * eps_b / omega_b  (BCS group velocity)")
print(f"  v_F choices: c_Gold = {c_Gold:.6f}, c_BA = {c_BA_s74:.6f}")
print()
print("  === v_F = c_Gold (primary) ===")
print("  Mode |  eps_b/omega_b  |  c_L2 (M_KK)  |  sector")
print("  " + "-" * 58)
for i in range(8):
    ratio = eps_b[i] / omega_b[i] if omega_b[i] > 0 else 0  # (local)
    note = " [NG mode]" if eps_b[i] < 1e-10 else ""  # (local)
    print(f"  {mode_labels[i]:6s}| {ratio:15.6f} | {c_L2_cGold[i]:13.6e} | "
          f"{sector_names[sector_map[i]]}{note}")

print()
print("  === v_F = c_BA (S74 convention) ===")
print("  Mode |  eps_b/omega_b  |  c_L2 (M_KK)  |  sector")
print("  " + "-" * 58)
for i in range(8):
    ratio = eps_b[i] / omega_b[i] if omega_b[i] > 0 else 0  # (local)
    note = " [NG mode]" if eps_b[i] < 1e-10 else ""  # (local)
    print(f"  {mode_labels[i]:6s}| {ratio:15.6f} | {c_L2_cBA[i]:13.6e} | "
          f"{sector_names[sector_map[i]]}{note}")
print()

# ==============================================================================
#  SECTION 4: Fractional difference delta_c_b = |c_L1 - c_L2| / c_L1
# ==============================================================================

print("SECTION 4: Fractional difference delta_c_b = |c_L1 - c_L2| / c_L1")
print("-" * 78)

# Primary comparison: v_F = c_Gold for both layers
delta_cb_cGold = np.abs(c_L1 - c_L2_cGold) / np.where(c_L1 > 0, c_L1, 1e-30)  # (local)

# Secondary comparison: Layer 2 with v_F = c_BA
delta_cb_cBA = np.abs(c_L1 - c_L2_cBA) / np.where(c_L1 > 0, c_L1, 1e-30)  # (local)

print("  === Primary: v_F = c_Gold ===")
print("  Mode |  c_L1          |  c_L2          |  delta_c_b  | sector")
print("  " + "-" * 72)
for i in range(8):
    print(f"  {mode_labels[i]:6s}| {c_L1[i]:14.6e} | {c_L2_cGold[i]:14.6e} | "
          f"{delta_cb_cGold[i]:11.6f} | {sector_names[sector_map[i]]}")

max_delta_primary = np.max(delta_cb_cGold)  # (local)
argmax_primary = np.argmax(delta_cb_cGold)  # (local)

print()
print(f"  max(delta_c_b) = {max_delta_primary:.6f} at mode {mode_labels[argmax_primary]}")
print()

print("  === Secondary: v_F = c_BA ===")
print("  Mode |  c_L1          |  c_L2          |  delta_c_b  | sector")
print("  " + "-" * 72)
for i in range(8):
    print(f"  {mode_labels[i]:6s}| {c_L1[i]:14.6e} | {c_L2_cBA[i]:14.6e} | "
          f"{delta_cb_cBA[i]:11.6f} | {sector_names[sector_map[i]]}")

max_delta_secondary = np.max(delta_cb_cBA)  # (local)
argmax_secondary = np.argmax(delta_cb_cBA)  # (local)

print()
print(f"  max(delta_c_b) = {max_delta_secondary:.6f} at mode {mode_labels[argmax_secondary]}")
print()

# ==============================================================================
#  SECTION 5: Structural analysis — why the layers differ (or agree)
# ==============================================================================

print("SECTION 5: Structural analysis of layer difference")
print("-" * 78)

# The two formulas:
#   Layer 1: c_b^(1) = c_Gold * omega_b / omega_max
#   Layer 2: c_b^(2) = c_Gold * eps_b / omega_b  (with v_F = c_Gold)
#
# Their ratio:
#   c_L2 / c_L1 = (eps_b / omega_b) * (omega_max / omega_b)
#               = eps_b * omega_max / omega_b^2
#
# Using omega_b^2 = eps_b^2 + Delta_b^2:
#   c_L2 / c_L1 = eps_b * omega_max / (eps_b^2 + Delta_b^2)
#
# For delta_c_b = 0 (perfect agreement), we need:
#   c_L2 / c_L1 = 1  =>  eps_b * omega_max = eps_b^2 + Delta_b^2 = omega_b^2
#                     =>  eps_b = omega_b^2 / omega_max = (eps_b^2 + Delta_b^2) / omega_max
#
# This is a nontrivial constraint. The layers agree IFF:
#   omega_b / omega_max = eps_b / omega_b, i.e., omega_b^2 = eps_b * omega_max.
#
# This is the GEOMETRIC MEAN condition: omega_b = sqrt(eps_b * omega_max).
# Deviations from this condition quantify the layer mismatch.

ratio_L2_L1 = np.where(c_L1 > 0, c_L2_cGold / c_L1, 0)  # (local)
geometric_test = omega_b**2 / (eps_b * omega_max)  # (local) should be 1 for agreement
# Handle mode 0 separately (eps_b ~ 0)
geometric_test[0] = 1.0  # (local) B1 mode handled as NG mode

print("  Structural condition for layer agreement: omega_b^2 = eps_b * omega_max")
print("  Ratio omega_b^2 / (eps_b * omega_max) = 1 means agreement")
print()
print("  Mode |  c_L2/c_L1  | omega_b^2/(eps*omega_max) | sector")
print("  " + "-" * 62)
for i in range(8):
    if eps_b[i] < 1e-10:
        print(f"  {mode_labels[i]:6s}| {ratio_L2_L1[i]:11.6f} | {'  [NG mode, special]':>25s} | "
              f"{sector_names[sector_map[i]]}")
    else:
        print(f"  {mode_labels[i]:6s}| {ratio_L2_L1[i]:11.6f} | {geometric_test[i]:25.6f} | "
              f"{sector_names[sector_map[i]]}")
print()

# Physical interpretation: the deviation from the geometric mean condition
# measures how much the BCS gap Delta_b "bends" the dispersion away from what
# the a_2-emergent metric predicts. For eps_b >> Delta_b (weak pairing),
# omega_b ~ eps_b and c_L2 ~ c_Gold -> agreement. For eps_b << Delta_b
# (strong pairing), omega_b ~ Delta_b and c_L2 -> 0 -> maximal disagreement.

for i in range(8):
    if eps_b[i] > 1e-10:
        gap_ratio = Delta_per_mode[i] / eps_b[i]  # (local)
        print(f"  {mode_labels[i]}: Delta/eps = {gap_ratio:.4f} "
              f"({'weak pairing' if gap_ratio < 1 else 'strong pairing'})")
print()

# ==============================================================================
#  SECTION 6: Sector-averaged comparison
# ==============================================================================

print("SECTION 6: Sector-averaged comparison")
print("-" * 78)

# Sector averages
c_L1_sectors = np.array([c_L1[0], np.mean(c_L1[1:5]), np.mean(c_L1[5:8])])  # (local)
c_L2_sectors = np.array([c_L2_cGold[0], np.mean(c_L2_cGold[1:5]),
                         np.mean(c_L2_cGold[5:8])])  # (local)
delta_sectors = np.abs(c_L1_sectors - c_L2_sectors) / np.where(
    c_L1_sectors > 0, c_L1_sectors, 1e-30)  # (local)

print("  Sector |  c_L1          |  c_L2          |  delta_c_b  |  N_modes")
print("  " + "-" * 70)
N_modes = [1, 4, 3]  # (local)
for i, name in enumerate(sector_names):
    print(f"  {name:6s} | {c_L1_sectors[i]:14.6e} | {c_L2_sectors[i]:14.6e} | "
          f"{delta_sectors[i]:11.6f} | {N_modes[i]}")
print()
print(f"  max(delta_c_b) by sector = {np.max(delta_sectors):.6f}")
print()

# ==============================================================================
#  SECTION 7: Impact on n_s (if delta_c_b > 0.01)
# ==============================================================================

print("SECTION 7: Impact on n_s from layer difference")
print("-" * 78)

# If the sound speeds differ between layers, the horizon-crossing condition
# k * c_b = a(tau) * H(tau) gives different tau_cross for each layer.
# Different tau_cross means different H(tau_cross) and hence different P_zeta(k).
#
# The spectral index n_s = 1 + d ln P_zeta / d ln k.
# If P_zeta changes due to changed c_b, then:
#   delta_n_s ~ 2 * delta_c_b * (d ln H / d ln tau) * (d tau / d ln c_b)
#
# For small delta_c_b, the correction is:
#   delta_n_s ~ -2 * epsilon_H * delta_c_b / c_b
# where epsilon_H = -dH/dN is the Hubble slow-roll parameter.
#
# In the transit regime, epsilon_H is NOT small (supersonic transit). But
# the correction to n_s from delta_c_b is still proportional to delta_c_b itself.
#
# More precisely: tau_cross scales as c_b^{-1} (from k*c_b = aH), so
#   d tau_cross / tau_cross = -d c_b / c_b
# and n_s correction:
#   delta_n_s = (d n_s / d ln tau_cross) * (delta_c_b / c_b)
#
# The key factor is d n_s / d ln tau_cross. In the frozen superhorizon plateau
# (established in S67 TRANSIT-PS-67 and S68 ACOUSTIC-TRANSFER-68),
# the primordial spectrum is EXACTLY scale-invariant (n_s = 1, alpha_s = 0)
# because all modes freeze at the SAME amplitude once superhorizon.
# The change in tau_cross does NOT change the frozen amplitude — it only
# changes WHEN the mode freezes, not WHAT it freezes to.
#
# Therefore: delta_n_s = 0 REGARDLESS of delta_c_b, because the primordial
# spectrum is frozen at scale-invariant. The n_s = 0.9649 tilt comes from
# spectral geometry (the D_K eigenvalue spectrum), not from mode-by-mode
# horizon crossing dynamics.

# Nevertheless, compute the formal correction for completeness
# Using the S74 Hubble profile H(tau) ~ H_fold * (tau/tau_fold)^{-p}
# with p determined by the a_2 evolution.
# epsilon_H = p (constant in power-law) ~ 1 for de Sitter-like near fold
p_hubble = 1.0  # (local) approximate power-law index near fold

delta_ns_formal = np.zeros(8)  # (local)
for i in range(8):
    if c_L1[i] > 1e-30:
        # delta_n_s ~ 2 * p * (delta_c_b) — but in frozen plateau, this is irrelevant
        delta_ns_formal[i] = 2 * p_hubble * delta_cb_cGold[i]

max_delta_ns = np.max(np.abs(delta_ns_formal))  # (local)

print("  Formal delta_n_s from changed horizon crossing (upper bound):")
print("  Mode |  delta_c_b  |  delta_n_s (formal) | sector")
print("  " + "-" * 56)
for i in range(8):
    print(f"  {mode_labels[i]:6s}| {delta_cb_cGold[i]:11.6f} | {delta_ns_formal[i]:19.6e} | "
          f"{sector_names[sector_map[i]]}")

print()
print(f"  max|delta_n_s| = {max_delta_ns:.6e}")
print(f"  Planck n_s     = {planck_ns} +/- {planck_ns_err}")
print(f"  delta_n_s / sigma_ns = {max_delta_ns / planck_ns_err:.4f}")
print()
print("  HOWEVER: This formal bound OVERSTATES the effect.")
print("  The primordial spectrum is FROZEN at scale-invariant (S67/S68 established).")
print("  Changed tau_cross changes WHEN a mode freezes, not WHAT it freezes to.")
print("  The n_s tilt comes from spectral geometry, not horizon-crossing dynamics.")
print("  Therefore: the PHYSICAL delta_n_s from layer difference is ZERO.")
print()

# ==============================================================================
#  SECTION 8: Gate verdict
# ==============================================================================

print("SECTION 8: Gate verdict S75-C3-LAYER-DIFF")
print("=" * 78)

# Use per-mode max for the gate (most stringent test)
gate_value = max_delta_primary  # (local)

if gate_value < 0.01:
    gate_verdict = "PASS"
    gate_reason = (f"max(delta_c_b) = {gate_value:.6f} < 0.01. "
                   "Layers agree to better than 1%.")
elif gate_value < 0.10:
    gate_verdict = "INFO"
    gate_reason = (f"max(delta_c_b) = {gate_value:.6f} in [0.01, 0.10). "
                   "Measurable but small discrepancy.")
else:
    gate_verdict = "FAIL"
    gate_reason = (f"max(delta_c_b) = {gate_value:.6f} > 0.10. "
                   "Significant discrepancy between layers.")

print(f"  Gate value:    max(delta_c_b) = {gate_value:.6f}")
print(f"  Gate verdict:  {gate_verdict}")
print(f"  Gate reason:   {gate_reason}")
print()

# D-R2-2 dissent evaluation
print("  D-R2-2 dissent (S74): 'Two layers give different c_b values'")
if gate_verdict == "FAIL":
    print("  SUBSTANTIATED — layers disagree at >10% level")
    print(f"  But: delta_n_s = 0 because primordial spectrum is frozen")
else:
    print(f"  Quantified: layers differ by max {gate_value:.1%}")
    print(f"  Impact on n_s: NONE (primordial spectrum frozen at scale-invariant)")
    print(f"  The dissent is structurally correct (layers DO give different c_b)")
    print(f"  but physically irrelevant for n_s (frozen spectrum theorem).")
print()

# Physical interpretation
print("  PHYSICAL INTERPRETATION:")
print("  Layer 1 (a_2-emergent) and Layer 2 (BCS-dressed) give different sound")
print("  speeds because they encode different physics:")
print("    - Layer 1 is the GEOMETRIC propagation speed from the emergent metric")
print("    - Layer 2 is the CONDENSATE group velocity from BCS dressing")
print("  The geometric mean condition omega_b^2 = eps_b * omega_max would make")
print("  them equal, but this is not generically satisfied.")
print("  The discrepancy is LARGEST for modes where Delta_b/eps_b is far from 1")
print("  (i.e., where BCS dressing most strongly modifies the bare dispersion).")
print("  However, this discrepancy does NOT affect n_s because the primordial")
print("  power spectrum is frozen in the superhorizon plateau (S67/S68).")
print()

# ==============================================================================
#  SECTION 9: Save results
# ==============================================================================

outpath = os.path.join(os.path.dirname(__file__), 's75_layer_diff.npz')  # (local)
np.savez(outpath,
         # Per-mode arrays
         eps_fold=eps_fold,
         Delta_per_mode=Delta_per_mode,
         omega_b=omega_b,
         c_L1=c_L1,
         c_L2_cGold=c_L2_cGold,
         c_L2_cBA=c_L2_cBA,
         delta_cb_cGold=delta_cb_cGold,
         delta_cb_cBA=delta_cb_cBA,
         delta_ns_formal=delta_ns_formal,
         # Sector averages
         c_L1_sectors=c_L1_sectors,
         c_L2_sectors=c_L2_sectors,
         delta_sectors=delta_sectors,
         # Scalars
         omega_max=omega_max,
         max_delta_primary=max_delta_primary,
         max_delta_secondary=max_delta_secondary,
         max_delta_ns=max_delta_ns,
         # Metadata
         gate_name=np.array('S75-C3-LAYER-DIFF'),
         gate_verdict=np.array(gate_verdict),
         gate_reason=np.array(gate_reason),
         v_F_primary=v_F_primary,
         c_BA_s74=c_BA_s74)

print(f"Results saved to {outpath}")
print("DONE.")
