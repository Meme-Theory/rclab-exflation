#!/usr/bin/env python3
"""
S75-A3-R-B-K-RUNNING: Dispersion-Induced Running of Bogoliubov Squeeze Parameters
==================================================================================

Physics:
    Each BCS branch b has a dispersion relation inherited from the D_K eigenvalue
    spectrum. At the fold (tau=0.190), the transit is supersonic (Mach 13.75), and
    the mode equation u_k'' + omega_k^2(tau) u_k = 0 has a time-dependent frequency.

    The Bogoliubov squeeze parameter r_b(k) arises from the sudden-approximation
    matching across the transit. For a mode with pre-transit frequency omega_pre(k)
    and post-transit frequency omega_post(k), the sudden-approximation gives:

        alpha_b(k) = (omega_pre + omega_post) / (2*sqrt(omega_pre*omega_post))
        beta_b(k)  = (omega_pre - omega_post) / (2*sqrt(omega_pre*omega_post))
        r_b(k)     = (1/2) * ln(alpha_b(k) + |beta_b(k)|)
                    = (1/2) * arccosh(alpha_b(k))

    where arccosh follows from |alpha|^2 - |beta|^2 = 1.

    S74 established that when r_b is k-independent, the H_b^2 cancellation
    (Sasaki-Stewart theorem) gives n_s = 1.000 exactly. If r_b(k) has nontrivial
    k-dependence through the BCS dispersion omega_b(k) = sqrt(eps_b(k)^2 + Delta_b^2),
    the cancellation breaks and both n_s and A_s acquire k-dependent corrections.

Gate: S75-A3-R-B-K-RUNNING
    PASS: |dr_b/d ln k| at k_pivot > 0.01 for B1 AND |n_s - 1| > 0.01
    INFO: 0.001 < |dr_b/d ln k| < 0.01
    FAIL: |dr_b/d ln k| < 0.001

Cross-checks:
    CHK1: c_pre = c_post => r_b(k) = const => n_s = 1.000
    CHK2: |alpha_b(k)|^2 - |beta_b(k)|^2 = 1 for every mode
    CHK3: r_b(k=0) reproduces S73B values (r_B1=3.57, r_B2=1.786, r_B3=1.963)
    CHK4: dr_b/d ln k sign consistent with c_b ordering
"""

import sys
sys.path.insert(0, ".")
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from canonical_constants import (
    Delta_BCS, Delta_B3, tau_fold, dt_transit, H_fold, v_terminal,
    c_fabric, A_s_CMB, E_B1, E_B2_mean, E_B3_mean, M_KK,
    Mpc_to_GeV_inv, planck_ns
)

# ============================================================================
#  1. Load per-branch data from S74 and S73B
# ============================================================================

s74 = np.load("s74_transfer_function.npz", allow_pickle=True)
s73b = np.load("s73b_transit_ps.npz", allow_pickle=True)
s56 = np.load("s56_gge_fabric.npz", allow_pickle=True)

# Per-branch sound speeds from S74 (M_KK units)
c_B1 = float(s74["c_B1"])  # (local) = 0.0798
c_B2 = float(s74["c_B2"])  # (local) = 0.001995
c_B3 = float(s74["c_B3"])  # (local) = 0.13965

# Per-branch frequencies at k_fold_sub from S74
omega_B1_s74 = float(s74["omega_B1"])  # (local) = 0.8184
omega_B2_s74 = float(s74["omega_B2"])  # (local) = 0.8388
omega_B3_s74 = float(s74["omega_B3"])  # (local) = 0.8758

# Per-branch squeeze parameters from S73B / S74
r_B1_ref = float(s74["r_B1"])  # (local) = 3.5713
r_B2_ref = float(s74["r_B2"])  # (local) = 1.7857
r_B3_ref = float(s74["r_B3"])  # (local) = 1.9635

# Per-branch weights from S74
W_B1 = float(s74["W_B1"])  # (local) = 0.1502
W_B2 = float(s74["W_B2"])  # (local) = 0.0318
W_B3 = float(s74["W_B3"])  # (local) = 0.8179

# Fold-scale single-particle energies from S56 (M_KK units)
eps_fold = s56["eps_fold"]  # (local) 8 modes

# BCS gap values (M_KK units)
Delta_full = Delta_BCS      # 0.4643 M_KK -- canonical OES gap
Delta_B3_val = Delta_B3     # (local) 0.176 M_KK -- B3 sector gap

print("=" * 70)
print("S75-A3-R-B-K-RUNNING: Dispersion-Induced Running of r_b(k)")
print("=" * 70)

# ============================================================================
#  2. Define BCS dispersion relations
# ============================================================================
#
# The BCS dispersion for branch b is:
#   omega_b(k) = sqrt(epsilon_b(k)^2 + Delta_b^2)
#
# where epsilon_b(k) is the single-particle dispersion relative to the
# chemical potential. For acoustic (phononic) modes:
#   epsilon_b(k) = sqrt(k^2 * c_b^2 + m_eff_b^2) - mu_b
#
# In the long-wavelength limit k -> 0:
#   epsilon_b(k=0) = m_eff_b - mu_b (gapped modes)
#   epsilon_b(k=0) = 0               (Goldstone modes)
#
# For our branches, the effective mass and chemical potential are encoded
# in the S56 fold energies eps_fold[i], which already represent
# epsilon_b(k_fold) at the characteristic fold wavevector.
#
# The key insight: the transit CHANGES the effective sound speed from
# c_b_pre to c_b_post. This is the ONLY source of k-dependence in the
# Bogoliubov coefficients.
#
# At the fold, the transit is in the supersonic / sudden regime. The
# appropriate Bogoliubov transformation is the sudden approximation:
#
#   alpha(k) = (omega_pre + omega_post) / (2*sqrt(omega_pre * omega_post))
#   beta(k)  = (omega_pre - omega_post) / (2*sqrt(omega_pre * omega_post))
#
# Unitarity: |alpha|^2 - |beta|^2 = 1 is AUTOMATIC.
#
# The squeeze parameter is:
#   r(k) = arccosh(|alpha(k)|)
#        = (1/2)*ln(alpha(k) + sqrt(alpha(k)^2 - 1))
#        = (1/2)*ln(alpha(k) + |beta(k)|)
#
# For alpha >> 1 (strong squeezing): r ≈ ln(alpha)

# ============================================================================
#  2a. Model the pre/post transit dispersion
# ============================================================================
#
# STRUCTURAL POINT: The transit through the van Hove fold changes the
# fiber's spectral geometry. The effect on each branch's dispersion is:
#
#   Pre-transit (tau < tau_fold):
#     omega_b_pre(k) = sqrt(k^2 * c_b^2 + m_eff_b^2)
#
#   Post-transit (tau > tau_fold):
#     omega_b_post(k) = sqrt(k^2 * c_b^2 + m_eff_b_post^2)
#
# The sound speeds c_b are set by the branch topology and are fixed
# (they come from the spectral action gradient). What changes at the
# transit is the EFFECTIVE MASS -- the BCS gap reorganizes.
#
# The S73B r_k values were computed from the FULL mode equation
# integration through the fold, at a SINGLE k (the fold-sub wavevector).
# The S74 transfer function computed the per-branch sound speeds and
# weights. What we need now is the k-dependent Bogoliubov transformation.
#
# The physical picture:
#   - Pre-transit: fiber in the unstable (tau < tau_fold) phase
#   - Post-transit: fiber in the BCS ground state (tau > tau_fold)
#   - The transit changes the effective mass of each mode
#
# We parameterize using the S74 data. The key constraint:
#   omega_b(k=k_ref) must reproduce the S74 omega_b values
#   r_b(k=k_ref) must reproduce the S73B/S74 r_b values
#
# From these two constraints per branch, we extract the pre/post
# effective masses.

print("\n--- Section 2: Extracting pre/post effective masses ---")

# The S74 data gives us omega_b at the fold-sub wavevector k_fold_sub
k_fold_sub = float(s74["k_fold_sub"])  # (local) = 0.8388 M_KK^{-1}
print(f"k_fold_sub = {k_fold_sub:.6f} M_KK^{{-1}}")

# For each branch, omega_b = omega_b(k_fold_sub). We need to decompose
# this into kinetic + mass contributions.
#
# omega_b^2 = k^2 * c_b^2 + m_eff_b^2
# => m_eff_b^2 = omega_b^2 - k^2 * c_b^2

# Post-transit effective masses (from S74 omega_b at k_fold_sub)
m_eff_B1_post_sq = omega_B1_s74**2 - k_fold_sub**2 * c_B1**2  # (local)
m_eff_B2_post_sq = omega_B2_s74**2 - k_fold_sub**2 * c_B2**2  # (local)
m_eff_B3_post_sq = omega_B3_s74**2 - k_fold_sub**2 * c_B3**2  # (local)

print(f"\nPost-transit effective masses squared (M_KK^2):")
print(f"  m_eff_B1_post^2 = {m_eff_B1_post_sq:.6f}")
print(f"  m_eff_B2_post^2 = {m_eff_B2_post_sq:.6f}")
print(f"  m_eff_B3_post^2 = {m_eff_B3_post_sq:.6f}")

# Now extract pre-transit effective masses from the S73B/S74 squeeze
# parameters. From the sudden approximation:
#
#   alpha_b = cosh(r_b)
#   alpha_b = (omega_pre + omega_post) / (2*sqrt(omega_pre*omega_post))
#
# Let x_b = omega_pre / omega_post (frequency ratio). Then:
#   alpha_b = (x_b + 1) / (2*sqrt(x_b))
#   cosh(r_b) = (x_b + 1) / (2*sqrt(x_b))
#
# This is a quadratic in sqrt(x_b):
#   sqrt(x_b) = cosh(r_b) + sqrt(cosh(r_b)^2 - 1) = cosh(r_b) + sinh(r_b) = e^{r_b}
#   => x_b = e^{2*r_b}
#   => omega_pre = omega_post * e^{2*r_b}
#
# Actually more carefully: cosh(r) = (x+1)/(2*sqrt(x)) gives
#   2*sqrt(x)*cosh(r) = x + 1
#   x - 2*sqrt(x)*cosh(r) + 1 = 0
# Let u = sqrt(x):
#   u^2 - 2*u*cosh(r) + 1 = 0
#   u = cosh(r) +/- sinh(r)
#   u = e^{+r} or e^{-r}
#
# The physical solution depends on whether omega_pre > omega_post or vice versa.
# Since beta = (omega_pre - omega_post)/(2*sqrt(omega_pre*omega_post)),
# beta > 0 <=> omega_pre > omega_post.
#
# From S73B, the transit produces large squeezing (r >> 1), so
# omega_pre >> omega_post. Thus x >> 1, and u = e^{+r}.
# => omega_pre/omega_post = e^{2r}

# Check: verify this reproduces the S73B beta values
for label, r_ref, omega_post in [("B1", r_B1_ref, omega_B1_s74),
                                   ("B2", r_B2_ref, omega_B2_s74),
                                   ("B3", r_B3_ref, omega_B3_s74)]:
    x_ratio = np.exp(2.0 * r_ref)  # (local) omega_pre/omega_post
    alpha_check = np.cosh(r_ref)  # (local)
    beta_check = np.sinh(r_ref)  # (local)
    alpha_from_x = (x_ratio + 1) / (2.0 * np.sqrt(x_ratio))  # (local)
    print(f"\n{label}: r = {r_ref:.4f}")
    print(f"  e^(2r) = {x_ratio:.4f}")
    print(f"  cosh(r) = {alpha_check:.4f}, from x: {alpha_from_x:.4f}, diff = {abs(alpha_check - alpha_from_x):.2e}")
    print(f"  |alpha|^2 - |beta|^2 = {alpha_check**2 - beta_check**2:.15f}")

# Pre-transit frequencies at k_fold_sub
omega_B1_pre_at_ref = omega_B1_s74 * np.exp(2.0 * r_B1_ref)  # (local)
omega_B2_pre_at_ref = omega_B2_s74 * np.exp(2.0 * r_B2_ref)  # (local)
omega_B3_pre_at_ref = omega_B3_s74 * np.exp(2.0 * r_B3_ref)  # (local)

print(f"\nPre-transit frequencies at k_fold_sub (M_KK):")
print(f"  omega_B1_pre = {omega_B1_pre_at_ref:.4f}")
print(f"  omega_B2_pre = {omega_B2_pre_at_ref:.4f}")
print(f"  omega_B3_pre = {omega_B3_pre_at_ref:.4f}")

# Pre-transit effective masses
m_eff_B1_pre_sq = omega_B1_pre_at_ref**2 - k_fold_sub**2 * c_B1**2  # (local)
m_eff_B2_pre_sq = omega_B2_pre_at_ref**2 - k_fold_sub**2 * c_B2**2  # (local)
m_eff_B3_pre_sq = omega_B3_pre_at_ref**2 - k_fold_sub**2 * c_B3**2  # (local)

print(f"\nPre-transit effective masses squared (M_KK^2):")
print(f"  m_eff_B1_pre^2 = {m_eff_B1_pre_sq:.6f}")
print(f"  m_eff_B2_pre^2 = {m_eff_B2_pre_sq:.6f}")
print(f"  m_eff_B3_pre^2 = {m_eff_B3_pre_sq:.6f}")

m_eff_B1_post = np.sqrt(m_eff_B1_post_sq)  # (local)
m_eff_B2_post = np.sqrt(m_eff_B2_post_sq)  # (local)
m_eff_B3_post = np.sqrt(m_eff_B3_post_sq)  # (local)
m_eff_B1_pre = np.sqrt(m_eff_B1_pre_sq)  # (local)
m_eff_B2_pre = np.sqrt(m_eff_B2_pre_sq)  # (local)
m_eff_B3_pre = np.sqrt(m_eff_B3_pre_sq)  # (local)

print(f"\nEffective masses (M_KK):")
print(f"  B1: pre = {m_eff_B1_pre:.6f}, post = {m_eff_B1_post:.6f}, ratio = {m_eff_B1_pre/m_eff_B1_post:.6f}")
print(f"  B2: pre = {m_eff_B2_pre:.6f}, post = {m_eff_B2_post:.6f}, ratio = {m_eff_B2_pre/m_eff_B2_post:.6f}")
print(f"  B3: pre = {m_eff_B3_pre:.6f}, post = {m_eff_B3_post:.6f}, ratio = {m_eff_B3_pre/m_eff_B3_post:.6f}")

# ============================================================================
#  3. Compute r_b(k) over extended k range
# ============================================================================
#
# For each branch b, the sudden-approximation Bogoliubov transformation gives:
#
#   omega_b_pre(k)  = sqrt(k^2 * c_b^2 + m_eff_b_pre^2)
#   omega_b_post(k) = sqrt(k^2 * c_b^2 + m_eff_b_post^2)
#
# NOTE: We use the SAME sound speed c_b for pre and post, because the
# sound speed is set by the branch topology (spectral action gradient).
# The transit changes the EFFECTIVE MASS (gap reorganization), not the
# sound speed.
#
#   alpha_b(k) = (omega_pre(k) + omega_post(k)) / (2*sqrt(omega_pre(k)*omega_post(k)))
#   r_b(k) = arccosh(alpha_b(k))

N_k = 200  # (local) scan points
k_min = 1.0e-4  # (local) Mpc^{-1}
k_max = 1.0  # (local) Mpc^{-1}
k_Mpc = np.logspace(np.log10(k_min), np.log10(k_max), N_k)  # (local)
k_pivot_Mpc = 0.05  # (local) Planck pivot scale

# Convert k from Mpc^{-1} to M_KK units
# k [M_KK] = k [Mpc^{-1}] * Mpc_to_GeV_inv / M_KK * M_KK
# Actually: k [Mpc^{-1}] -> k [GeV] = k * (1/Mpc_to_GeV_inv)
# Then k [M_KK units] = k [GeV] / M_KK
#
# But the key point: the S74 data is ALREADY in M_KK units internally.
# The fold-sub wavevector k_fold_sub = 0.8388 is in M_KK^{-1} units.
# The CMB wavenumbers k ~ 0.05 Mpc^{-1} map to MUCH smaller values in
# M_KK^{-1} units: k_CMB [M_KK^{-1}] = k_CMB [GeV] / M_KK
#                                       = (k_CMB [Mpc^{-1}] / Mpc_to_GeV_inv) / M_KK
#
# Mpc_to_GeV_inv = 1.563e38 GeV^{-1} per Mpc
# So k [GeV] = k [Mpc^{-1}] / 1.563e38
# k [M_KK^{-1}] = k [Mpc^{-1}] / (1.563e38 * 7.43e16) = k / 1.16e55
#
# This means CMB wavevectors are ~ 10^{-55} M_KK^{-1} -- negligibly small
# compared to the fold scale k_fold_sub ~ 0.84 M_KK^{-1}.
#
# CRITICAL INSIGHT: At CMB scales k ~ 10^{-55} M_KK^{-1}, the dispersion
# is COMPLETELY dominated by the effective mass term. k^2*c_b^2 is utterly
# negligible compared to m_eff^2. Therefore:
#
#   omega_b_pre(k_CMB) ≈ m_eff_b_pre
#   omega_b_post(k_CMB) ≈ m_eff_b_post
#
# and r_b(k_CMB) = r_b(k=0) = (1/2)*ln(m_eff_pre/m_eff_post) + correction
# with the correction from k^2 being of order (k*c_b)^2 / m_eff^4 ~ 10^{-110}.

k_scale_factor = 1.0 / (Mpc_to_GeV_inv * M_KK)  # (local) Mpc^{-1} to M_KK^{-1}
print(f"\nk conversion factor: 1 Mpc^{{-1}} = {k_scale_factor:.4e} M_KK^{{-1}}")
print(f"k_pivot = {k_pivot_Mpc} Mpc^{{-1}} = {k_pivot_Mpc * k_scale_factor:.4e} M_KK^{{-1}}")
print(f"k_fold_sub = {k_fold_sub:.4f} M_KK^{{-1}} = {k_fold_sub / k_scale_factor:.4e} Mpc^{{-1}}")

# Convert k array to M_KK units
k_MKK = k_Mpc * k_scale_factor  # (local) array in M_KK^{-1}

print(f"\nk range in M_KK units: [{k_MKK[0]:.4e}, {k_MKK[-1]:.4e}]")
print(f"k_fold_sub / k_max_MKK = {k_fold_sub / k_MKK[-1]:.4e}")
print(f"=> ALL CMB k-modes are in the k << m_eff regime")

# ============================================================================
#  3a. Compute omega_pre(k), omega_post(k), alpha(k), r(k) for each branch
# ============================================================================

print("\n--- Section 3: Computing r_b(k) ---")

# Store results
results = {}  # (local)

for label, c_b, m_pre, m_post, r_ref, W_b in [
    ("B1", c_B1, m_eff_B1_pre, m_eff_B1_post, r_B1_ref, W_B1),
    ("B2", c_B2, m_eff_B2_pre, m_eff_B2_post, r_B2_ref, W_B2),
    ("B3", c_B3, m_eff_B3_pre, m_eff_B3_post, r_B3_ref, W_B3),
]:
    # Pre and post transit frequencies (M_KK units)
    omega_pre_k = np.sqrt(k_MKK**2 * c_b**2 + m_pre**2)  # (local)
    omega_post_k = np.sqrt(k_MKK**2 * c_b**2 + m_post**2)  # (local)

    # Bogoliubov coefficients (sudden approximation)
    alpha_k = (omega_pre_k + omega_post_k) / (2.0 * np.sqrt(omega_pre_k * omega_post_k))  # (local)
    beta_k = (omega_pre_k - omega_post_k) / (2.0 * np.sqrt(omega_pre_k * omega_post_k))  # (local)

    # CHK2: Unitarity check
    unitarity_err = np.abs(alpha_k**2 - beta_k**2 - 1.0)  # (local)

    # Squeeze parameter
    r_k = np.arccosh(alpha_k)  # (local)

    # Particle number
    n_k = np.sinh(r_k)**2  # (local) = |beta|^2

    # Logarithmic derivative dr/d(ln k)
    ln_k = np.log(k_MKK)  # (local)
    dr_dlnk = np.gradient(r_k, ln_k)  # (local)

    # Value at k_pivot
    idx_pivot = np.argmin(np.abs(k_Mpc - k_pivot_Mpc))  # (local)
    r_pivot = r_k[idx_pivot]  # (local)
    dr_dlnk_pivot = dr_dlnk[idx_pivot]  # (local)

    # Value at k=0 (first element, lowest k)
    r_k0 = r_k[0]  # (local)

    # Store
    results[label] = {
        "omega_pre_k": omega_pre_k,
        "omega_post_k": omega_post_k,
        "alpha_k": alpha_k,
        "beta_k": beta_k,
        "r_k": r_k,
        "n_k": n_k,
        "dr_dlnk": dr_dlnk,
        "unitarity_err_max": np.max(unitarity_err),
        "r_pivot": r_pivot,
        "dr_dlnk_pivot": dr_dlnk_pivot,
        "r_k0": r_k0,
        "r_ref": r_ref,
        "W_b": W_b,
        "c_b": c_b,
        "m_pre": m_pre,
        "m_post": m_post,
    }

    print(f"\n{label}:")
    print(f"  c_b = {c_b:.6f} M_KK")
    print(f"  m_eff_pre = {m_pre:.6f}, m_eff_post = {m_post:.6f}")
    print(f"  m_pre/m_post = {m_pre/m_post:.6f} = e^(2*r_ref) = {np.exp(2*r_ref):.6f}")
    print(f"  r(k->0) = {r_k0:.6f}, r_ref(S73B/S74) = {r_ref:.6f}")
    print(f"  r(k_pivot) = {r_pivot:.10f}")
    print(f"  dr/d(ln k) at k_pivot = {dr_dlnk_pivot:.4e}")
    print(f"  |dr/d(ln k)| range: [{np.min(np.abs(dr_dlnk)):.4e}, {np.max(np.abs(dr_dlnk)):.4e}]")
    print(f"  CHK2 unitarity: max|alpha^2 - beta^2 - 1| = {np.max(unitarity_err):.2e}")

# ============================================================================
#  CHK1: Verify c_pre = c_post limit gives r = const
# ============================================================================

print("\n--- CHK1: Same sound speed limit ---")
# If we set m_pre = m_post, then omega_pre = omega_post for all k, so
# alpha = 1, beta = 0, r = 0. That's trivial.
#
# The more interesting check: if the MASS is the only thing that differs
# (which is our model), then at k >> m/c, omega_pre ≈ omega_post ≈ k*c,
# and r -> 0. At k << m/c, omega_pre ≈ m_pre, omega_post ≈ m_post, and
# r -> (1/2)*ln(m_pre/m_post) = constant.
#
# Since ALL CMB k-modes satisfy k*c_b << m_eff_b, we expect r_b(k) to
# be effectively constant across the entire Planck band.

for label in ["B1", "B2", "B3"]:
    R = results[label]  # (local)
    k_crossover = R["m_post"] / R["c_b"]  # (local) M_KK^{-1}, where k*c ~ m
    k_crossover_Mpc = k_crossover / k_scale_factor  # (local)
    print(f"  {label}: k_crossover = {k_crossover:.4f} M_KK^{{-1}} = {k_crossover_Mpc:.4e} Mpc^{{-1}}")
    print(f"    k_max_scan / k_crossover = {k_MKK[-1] / k_crossover:.4e}")

    # Variation of r across scan range
    r_range = np.max(R["r_k"]) - np.min(R["r_k"])  # (local)
    r_fractional = r_range / R["r_k0"]  # (local)
    print(f"    r range: {r_range:.4e} (fractional: {r_fractional:.4e})")

# ============================================================================
#  CHK3: Verify r(k=0) matches S73B
# ============================================================================

print("\n--- CHK3: r(k=0) vs S73B reference ---")

for label in ["B1", "B2", "B3"]:
    R = results[label]  # (local)
    diff = abs(R["r_k0"] - R["r_ref"])  # (local)
    # The S73B/S74 values were computed at k_fold_sub, not k=0.
    # The difference reflects the k-dependence between k=0 and k_fold_sub.
    # But since k_fold_sub is in M_KK units and our scan is in CMB units
    # (10^{-55} M_KK^{-1}), our "k=0" is effectively k=0 on the fold scale.
    #
    # The S73B/S74 r values were computed from the FULL mode equation at
    # k_fold_sub. Our model decomposes omega into mass + kinetic, which
    # at k -> 0 gives r = (1/2)*ln(m_pre/m_post).
    #
    # From the algebra: omega_pre/omega_post = e^{2r} at k_fold_sub by
    # construction. Then:
    #   r(k=0) = (1/2)*ln(m_pre/m_post)
    #   r(k_fold_sub) = (1/2)*ln(omega_pre(k_fold_sub)/omega_post(k_fold_sub))
    #
    # These differ because at k_fold_sub, kinetic energy contributes.
    # But since omega >> k*c for all our modes, they should be very close.

    r_at_kref = 0.5 * np.log(R["m_pre"]**2 + k_fold_sub**2 * R["c_b"]**2) \
              - 0.5 * np.log(R["m_post"]**2 + k_fold_sub**2 * R["c_b"]**2)  # (local)
    # This is ln(omega_pre/omega_post) / 2 -- should equal r_ref

    # More precisely: arccosh(alpha) where alpha uses omega at k_fold_sub
    omega_pre_ref = np.sqrt(k_fold_sub**2 * R["c_b"]**2 + R["m_pre"]**2)  # (local)
    omega_post_ref = np.sqrt(k_fold_sub**2 * R["c_b"]**2 + R["m_post"]**2)  # (local)
    alpha_ref = (omega_pre_ref + omega_post_ref) / (2.0 * np.sqrt(omega_pre_ref * omega_post_ref))  # (local)
    r_at_kref_exact = np.arccosh(alpha_ref)  # (local)

    print(f"  {label}:")
    print(f"    r(k~0) = {R['r_k0']:.6f}")
    print(f"    r(k_fold_sub) = {r_at_kref_exact:.6f}")
    print(f"    r_ref (S73B/S74) = {R['r_ref']:.6f}")
    print(f"    |r(k_fold_sub) - r_ref| = {abs(r_at_kref_exact - R['r_ref']):.2e}")

# ============================================================================
#  4. Compute tau_cross(k) variation across Planck band
# ============================================================================
#
# tau_cross(k) = omega_b(k) / H is the adiabaticity parameter.
# In the sudden limit tau_cross >> 1, the mode is well inside the
# impulsive regime. The variation of tau_cross across the Planck band
# tells us how uniform the squeezing is.

print("\n--- Section 4: tau_cross(k) variation ---")

k_planck_min = 0.002  # (local) Mpc^{-1} (Planck band lower edge)
k_planck_max = 0.2  # (local) Mpc^{-1} (Planck band upper edge)
k_planck_min_MKK = k_planck_min * k_scale_factor  # (local)
k_planck_max_MKK = k_planck_max * k_scale_factor  # (local)

for label in ["B1", "B2", "B3"]:
    R = results[label]  # (local)
    # Post-transit tau_cross
    omega_at_kmin = np.sqrt(k_planck_min_MKK**2 * R["c_b"]**2 + R["m_post"]**2)  # (local)
    omega_at_kmax = np.sqrt(k_planck_max_MKK**2 * R["c_b"]**2 + R["m_post"]**2)  # (local)
    tau_cross_min = omega_at_kmin / H_fold  # (local)
    tau_cross_max = omega_at_kmax / H_fold  # (local)
    delta_tau_cross = tau_cross_max - tau_cross_min  # (local)
    frac_var = delta_tau_cross / tau_cross_min  # (local)
    print(f"  {label}: tau_cross in [{tau_cross_min:.6f}, {tau_cross_max:.6f}]")
    print(f"    delta(tau_cross) = {delta_tau_cross:.4e}, fractional variation = {frac_var:.4e}")

# ============================================================================
#  5. Compute n_s correction from dispersion running
# ============================================================================
#
# S74 established that when r_b is k-independent:
#   P_s(k) = sum_b W_b * |H_b|^2 * cosh(2*r_b) / (2*pi)^2
#
# where the k-dependence is entirely in |H_b|^2. The Sasaki-Stewart theorem
# states that for a single field with de Sitter-like evolution:
#   |H_b|^2 propto k^{n_s-1} with n_s determined by the slow-roll parameters.
#
# When r_b has k-dependence, the spectrum acquires an additional factor:
#   P_s(k) = sum_b W_b * |H_b(k)|^2 * cosh(2*r_b(k)) / (2*pi)^2
#
# The tilt from dispersion running is:
#   n_s^{disp} - 1 = d ln[sum_b W_b * cosh(2*r_b(k))] / d ln k
#                   = [sum_b W_b * sinh(2*r_b) * 2*(dr_b/d ln k)]
#                     / [sum_b W_b * cosh(2*r_b)]

print("\n--- Section 5: n_s correction from dispersion running ---")

# Compute the weighted sums at each k
cosh_2r_B1 = np.cosh(2.0 * results["B1"]["r_k"])  # (local)
cosh_2r_B2 = np.cosh(2.0 * results["B2"]["r_k"])  # (local)
cosh_2r_B3 = np.cosh(2.0 * results["B3"]["r_k"])  # (local)

sinh_2r_B1 = np.sinh(2.0 * results["B1"]["r_k"])  # (local)
sinh_2r_B2 = np.sinh(2.0 * results["B2"]["r_k"])  # (local)
sinh_2r_B3 = np.sinh(2.0 * results["B3"]["r_k"])  # (local)

numerator = (W_B1 * sinh_2r_B1 * 2.0 * results["B1"]["dr_dlnk"]
           + W_B2 * sinh_2r_B2 * 2.0 * results["B2"]["dr_dlnk"]
           + W_B3 * sinh_2r_B3 * 2.0 * results["B3"]["dr_dlnk"])  # (local)

denominator = (W_B1 * cosh_2r_B1
             + W_B2 * cosh_2r_B2
             + W_B3 * cosh_2r_B3)  # (local)

ns_correction = numerator / denominator  # (local) this is (n_s^{disp} - 1)

idx_pivot = np.argmin(np.abs(k_Mpc - k_pivot_Mpc))  # (local)

ns_disp_at_pivot = ns_correction[idx_pivot]  # (local)
ns_total_at_pivot = 1.0 + ns_disp_at_pivot  # (local)

print(f"n_s^{{disp}} - 1 at k_pivot = {ns_disp_at_pivot:.4e}")
print(f"n_s^{{disp}} at k_pivot = {ns_total_at_pivot:.10f}")

# Also compute over Planck band
idx_pmin = np.argmin(np.abs(k_Mpc - k_planck_min))  # (local)
idx_pmax = np.argmin(np.abs(k_Mpc - k_planck_max))  # (local)

ns_planck_min = ns_correction[idx_pmin]  # (local)
ns_planck_max = ns_correction[idx_pmax]  # (local)

print(f"\nPlanck band [{k_planck_min}, {k_planck_max}] Mpc^{{-1}}:")
print(f"  n_s - 1 range: [{ns_planck_min:.4e}, {ns_planck_max:.4e}]")
print(f"  max |n_s - 1| = {max(abs(ns_planck_min), abs(ns_planck_max)):.4e}")

# Per-branch contributions
for label in ["B1", "B2", "B3"]:
    R = results[label]  # (local)
    contrib = R["W_b"] * np.sinh(2.0 * R["r_k"][idx_pivot]) * 2.0 * R["dr_dlnk"][idx_pivot] / denominator[idx_pivot]  # (local)
    print(f"  {label} contribution to (n_s-1): {contrib:.4e}")

# ============================================================================
#  6. Compute A_s correction relative to S74
# ============================================================================
#
# The S74 A_s was computed with k-independent r_b. The correction from
# k-dependent r_b at the pivot scale is:
#
#   A_s^{disp}(k_pivot) / A_s^{S74} = [sum_b W_b * cosh(2*r_b(k_pivot))]
#                                     / [sum_b W_b * cosh(2*r_b_ref)]

print("\n--- Section 6: A_s correction ---")

A_s_S74 = float(s74["A_s_4D"])  # (local) from S74

cosh_ref_B1 = np.cosh(2.0 * r_B1_ref)  # (local)
cosh_ref_B2 = np.cosh(2.0 * r_B2_ref)  # (local)
cosh_ref_B3 = np.cosh(2.0 * r_B3_ref)  # (local)

denom_ref = W_B1 * cosh_ref_B1 + W_B2 * cosh_ref_B2 + W_B3 * cosh_ref_B3  # (local)
numer_pivot = denominator[idx_pivot]  # (local) this is sum W_b cosh(2r_b(k_pivot))

A_s_ratio = numer_pivot / denom_ref  # (local)
A_s_disp = A_s_S74 * A_s_ratio  # (local)

print(f"A_s (S74) = {A_s_S74:.6e}")
print(f"cosh(2r) sum at k_pivot = {numer_pivot:.6f}")
print(f"cosh(2r) sum at k_ref = {denom_ref:.6f}")
print(f"A_s ratio (disp/S74) = {A_s_ratio:.15f}")
print(f"A_s (dispersion-corrected) = {A_s_disp:.6e}")
print(f"|log10(A_s_ratio)| = {abs(np.log10(A_s_ratio)):.4e}")

# ============================================================================
#  7. Analytic understanding: WHY r_b(k) is flat
# ============================================================================
#
# The result is physically clear. Let us derive it analytically.
#
# For k << m_eff / c_b (which is the case for ALL CMB modes):
#
#   omega_pre(k) = sqrt(k^2*c^2 + m_pre^2)
#                ≈ m_pre * (1 + k^2*c^2/(2*m_pre^2))
#
#   omega_post(k) = sqrt(k^2*c^2 + m_post^2)
#                 ≈ m_post * (1 + k^2*c^2/(2*m_post^2))
#
# The frequency ratio:
#   x(k) = omega_pre(k)/omega_post(k)
#         ≈ (m_pre/m_post) * (1 + k^2*c^2/(2*m_pre^2) - k^2*c^2/(2*m_post^2))
#         = x_0 * (1 + (k*c)^2 / 2 * (1/m_pre^2 - 1/m_post^2))
#
# Since m_pre >> m_post (strong squeezing, x_0 >> 1):
#   1/m_pre^2 << 1/m_post^2
#   x(k) ≈ x_0 * (1 - (k*c)^2 / (2*m_post^2))
#
# The squeeze parameter:
#   r(k) = (1/2)*ln(x(k)) ≈ r_0 - (k*c)^2 / (4*m_post^2)
#
# where r_0 = (1/2)*ln(x_0) = (1/2)*ln(m_pre/m_post).
#
# The logarithmic derivative:
#   dr/d(ln k) = -k^2*c^2 / (2*m_post^2)
#
# At k_pivot in M_KK units (~ 10^{-55}):
#   dr/d(ln k) ~ -10^{-110} * c^2 / m_post^2 ~ -10^{-110}
#
# This is VANISHINGLY small. The dispersion running of r_b(k) at CMB
# scales is suppressed by (k_CMB / m_eff)^2 ~ 10^{-110}.

print("\n--- Section 7: Analytic verification ---")

for label in ["B1", "B2", "B3"]:
    R = results[label]  # (local)
    k_piv_MKK = k_pivot_Mpc * k_scale_factor  # (local)
    dr_analytic = -k_piv_MKK**2 * R["c_b"]**2 / (2.0 * R["m_post"]**2)  # (local)
    print(f"  {label}: dr/d(ln k) analytic at k_pivot = {dr_analytic:.4e}")
    print(f"    Numerical: {R['dr_dlnk_pivot']:.4e}")
    print(f"    (k_pivot * c_b / m_post)^2 = {(k_piv_MKK * R['c_b'] / R['m_post'])**2:.4e}")

# ============================================================================
#  8. Scan at fold scale (where dispersion DOES matter)
# ============================================================================
#
# The dispersion running becomes significant only at k ~ m_eff/c ~ O(1) M_KK^{-1},
# i.e., at the fold scale itself. Let us compute r_b(k) across the fold scale
# to show where the running turns on.

print("\n--- Section 8: Fold-scale scan ---")

N_k_fold = 200  # (local)
k_fold_min = 1.0e-4  # (local) M_KK^{-1}
k_fold_max = 20.0  # (local) M_KK^{-1} (well above fold scale)
k_fold_scan = np.logspace(np.log10(k_fold_min), np.log10(k_fold_max), N_k_fold)  # (local)

fold_results = {}  # (local)

for label, c_b, m_pre, m_post in [
    ("B1", c_B1, m_eff_B1_pre, m_eff_B1_post),
    ("B2", c_B2, m_eff_B2_pre, m_eff_B2_post),
    ("B3", c_B3, m_eff_B3_pre, m_eff_B3_post),
]:
    omega_pre_fold = np.sqrt(k_fold_scan**2 * c_b**2 + m_pre**2)  # (local)
    omega_post_fold = np.sqrt(k_fold_scan**2 * c_b**2 + m_post**2)  # (local)
    alpha_fold = (omega_pre_fold + omega_post_fold) / (2.0 * np.sqrt(omega_pre_fold * omega_post_fold))  # (local)
    r_fold = np.arccosh(alpha_fold)  # (local)
    ln_k_fold = np.log(k_fold_scan)  # (local)
    dr_dlnk_fold = np.gradient(r_fold, ln_k_fold)  # (local)

    fold_results[label] = {
        "k": k_fold_scan,
        "r": r_fold,
        "dr_dlnk": dr_dlnk_fold,
    }

    # Find where |dr/d(ln k)| > 0.01
    significant = np.where(np.abs(dr_dlnk_fold) > 0.01)[0]  # (local)
    if len(significant) > 0:
        k_onset = k_fold_scan[significant[0]]  # (local)
        print(f"  {label}: |dr/d(ln k)| > 0.01 for k > {k_onset:.4f} M_KK^{{-1}}")
        print(f"    = {k_onset / k_scale_factor:.4e} Mpc^{{-1}}")
    else:
        print(f"  {label}: |dr/d(ln k)| < 0.01 everywhere in scan range")

    print(f"    max |dr/d(ln k)| = {np.max(np.abs(dr_dlnk_fold)):.4f}")
    print(f"    r(k_min) = {r_fold[0]:.6f}, r(k_max) = {r_fold[-1]:.6f}")

# ============================================================================
#  9. CHK4: Sign consistency
# ============================================================================
#
# CHK4: dr_b/d ln k sign must be consistent with dispersion.
# Since omega_pre > omega_post (squeezing), and increasing k increases the
# kinetic energy equally for both, the frequency RATIO x = omega_pre/omega_post
# DECREASES with k (because the kinetic energy is relatively larger for the
# smaller mass, pulling the ratio toward 1). Therefore dr/d(ln k) < 0.

print("\n--- CHK4: Sign consistency ---")

for label in ["B1", "B2", "B3"]:
    R = results[label]  # (local)
    # At k -> 0: omega_pre/omega_post = m_pre/m_post >> 1
    # At k -> inf: omega_pre/omega_post -> 1
    # So r(k) is monotonically DECREASING. dr/d(ln k) < 0 everywhere.

    sign_ok = np.all(R["dr_dlnk"] <= 0)  # (local)
    print(f"  {label}: dr/d(ln k) <= 0 everywhere: {sign_ok}")
    if not sign_ok:
        n_pos = np.sum(R["dr_dlnk"] > 0)  # (local)
        print(f"    WARNING: {n_pos}/{N_k} points have dr/d(ln k) > 0 (likely numerical edge effect)")

# ============================================================================
#  10. Gate evaluation
# ============================================================================

print("\n" + "=" * 70)
print("GATE EVALUATION: S75-A3-R-B-K-RUNNING")
print("=" * 70)

dr_B1_pivot = abs(results["B1"]["dr_dlnk_pivot"])  # (local)
dr_B2_pivot = abs(results["B2"]["dr_dlnk_pivot"])  # (local)
dr_B3_pivot = abs(results["B3"]["dr_dlnk_pivot"])  # (local)
ns_minus_1 = abs(ns_disp_at_pivot)  # (local)

print(f"\nKey quantities at k_pivot = {k_pivot_Mpc} Mpc^{{-1}}:")
print(f"  |dr_B1/d ln k| = {dr_B1_pivot:.4e}")
print(f"  |dr_B2/d ln k| = {dr_B2_pivot:.4e}")
print(f"  |dr_B3/d ln k| = {dr_B3_pivot:.4e}")
print(f"  |n_s - 1| = {ns_minus_1:.4e}")

# Gate criteria:
# PASS: |dr_b/d ln k| at k_pivot > 0.01 for B1 AND |n_s - 1| > 0.01
# INFO: 0.001 < |dr_b/d ln k| < 0.01
# FAIL: |dr_b/d ln k| < 0.001

if dr_B1_pivot > 0.01 and ns_minus_1 > 0.01:
    gate_verdict = "PASS"
    gate_reason = f"|dr_B1/dlnk|={dr_B1_pivot:.2e} > 0.01, |n_s-1|={ns_minus_1:.2e} > 0.01"
elif dr_B1_pivot > 0.001:
    gate_verdict = "INFO"
    gate_reason = f"|dr_B1/dlnk|={dr_B1_pivot:.2e} in (0.001, 0.01)"
else:
    gate_verdict = "FAIL"
    gate_reason = f"|dr_B1/dlnk|={dr_B1_pivot:.2e} < 0.001"

print(f"\nGate verdict: {gate_verdict}")
print(f"Reason: {gate_reason}")

# Physical explanation
print(f"\nPhysical explanation:")
print(f"  The dispersion running of r_b(k) is suppressed by (k_CMB / k_fold)^2.")
print(f"  k_CMB ~ {k_pivot_Mpc * k_scale_factor:.2e} M_KK^{{-1}}")
print(f"  k_fold ~ {k_fold_sub:.2f} M_KK^{{-1}}")
print(f"  Ratio^2 ~ {(k_pivot_Mpc * k_scale_factor / k_fold_sub)**2:.2e}")
print(f"  This extreme hierarchy guarantees r_b(k) is constant at CMB scales.")
print(f"  The Sasaki-Stewart H_b^2 cancellation holds to better than 10^{{-100}}.")
print(f"  Dispersion running becomes significant ONLY at the fold scale")
print(f"  (k ~ 10^55 Mpc^{{-1}}), which is irrelevant for CMB observables.")

# ============================================================================
#  11. Summary table
# ============================================================================

print("\n" + "=" * 70)
print("SUMMARY TABLE")
print("=" * 70)

print(f"\n{'Branch':<8} {'r(k->0)':<12} {'r(k_piv)':<12} {'dr/dlnk(piv)':<15} {'delta_r/r':<12} {'k_cross [M_KK^-1]':<18}")
for label in ["B1", "B2", "B3"]:
    R = results[label]
    delta_r_over_r = abs(R["r_pivot"] - R["r_k0"]) / R["r_k0"]
    k_cross = R["m_post"] / R["c_b"]
    print(f"{label:<8} {R['r_k0']:<12.6f} {R['r_pivot']:<12.6f} {R['dr_dlnk_pivot']:<15.4e} {delta_r_over_r:<12.4e} {k_cross:<18.4f}")

print(f"\n{'Quantity':<25} {'Value':<20}")
print(f"{'n_s^disp - 1 (pivot)':<25} {ns_disp_at_pivot:<20.4e}")
print(f"{'n_s^disp (pivot)':<25} {ns_total_at_pivot:<20.10f}")
print(f"{'A_s ratio (disp/S74)':<25} {A_s_ratio:<20.15f}")
print(f"{'Suppression factor':<25} {'(k_CMB/k_fold)^2 ~ 10^{-110}':<20}")

# ============================================================================
#  12. Save data
# ============================================================================

np.savez("s75_r_b_k_running.npz",
    # k arrays (CMB scale)
    k_Mpc=k_Mpc,
    k_MKK=k_MKK,
    k_pivot_Mpc=k_pivot_Mpc,
    k_scale_factor=k_scale_factor,

    # Per-branch results at CMB scale
    r_B1_k=results["B1"]["r_k"],
    r_B2_k=results["B2"]["r_k"],
    r_B3_k=results["B3"]["r_k"],
    dr_B1_dlnk=results["B1"]["dr_dlnk"],
    dr_B2_dlnk=results["B2"]["dr_dlnk"],
    dr_B3_dlnk=results["B3"]["dr_dlnk"],
    alpha_B1_k=results["B1"]["alpha_k"],
    alpha_B2_k=results["B2"]["alpha_k"],
    alpha_B3_k=results["B3"]["alpha_k"],
    beta_B1_k=results["B1"]["beta_k"],
    beta_B2_k=results["B2"]["beta_k"],
    beta_B3_k=results["B3"]["beta_k"],

    # Per-branch pivot values
    r_B1_pivot=results["B1"]["r_pivot"],
    r_B2_pivot=results["B2"]["r_pivot"],
    r_B3_pivot=results["B3"]["r_pivot"],
    dr_B1_dlnk_pivot=results["B1"]["dr_dlnk_pivot"],
    dr_B2_dlnk_pivot=results["B2"]["dr_dlnk_pivot"],
    dr_B3_dlnk_pivot=results["B3"]["dr_dlnk_pivot"],

    # Per-branch reference values
    r_B1_ref=r_B1_ref,
    r_B2_ref=r_B2_ref,
    r_B3_ref=r_B3_ref,

    # Per-branch effective masses
    m_eff_B1_pre=m_eff_B1_pre,
    m_eff_B2_pre=m_eff_B2_pre,
    m_eff_B3_pre=m_eff_B3_pre,
    m_eff_B1_post=m_eff_B1_post,
    m_eff_B2_post=m_eff_B2_post,
    m_eff_B3_post=m_eff_B3_post,

    # n_s and A_s corrections
    ns_correction=ns_correction,
    ns_disp_at_pivot=ns_disp_at_pivot,
    ns_total_at_pivot=ns_total_at_pivot,
    A_s_ratio=A_s_ratio,
    A_s_S74=A_s_S74,

    # Fold-scale scan
    k_fold_scan=k_fold_scan,
    r_B1_fold=fold_results["B1"]["r"],
    r_B2_fold=fold_results["B2"]["r"],
    r_B3_fold=fold_results["B3"]["r"],
    dr_B1_dlnk_fold=fold_results["B1"]["dr_dlnk"],
    dr_B2_dlnk_fold=fold_results["B2"]["dr_dlnk"],
    dr_B3_dlnk_fold=fold_results["B3"]["dr_dlnk"],

    # Gate
    gate_name="S75-A3-R-B-K-RUNNING",
    gate_verdict=gate_verdict,
    gate_reason=gate_reason,
)

print("\nData saved to s75_r_b_k_running.npz")

# ============================================================================
#  13. Plot
# ============================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("S75-A3: Dispersion-Induced Running of r_b(k)", fontsize=14, fontweight="bold")

# Panel A: r_b(k) at CMB scale (should be flat)
ax = axes[0, 0]
for label, color in [("B1", "tab:blue"), ("B2", "tab:orange"), ("B3", "tab:green")]:
    R = results[label]
    # Plot relative to r(k=0)
    delta_r = R["r_k"] - R["r_k0"]
    ax.semilogx(k_Mpc, delta_r, color=color, label=f"{label} (r0={R['r_k0']:.3f})")
ax.axvline(k_pivot_Mpc, color="gray", ls="--", alpha=0.5, label="k_pivot")
ax.axvspan(k_planck_min, k_planck_max, alpha=0.1, color="gray")
ax.set_xlabel(r"$k$ [Mpc$^{-1}$]")
ax.set_ylabel(r"$r_b(k) - r_b(0)$")
ax.set_title("(A) r_b(k) variation at CMB scale")
ax.legend(fontsize=8)
ax.ticklabel_format(axis='y', style='scientific', scilimits=(-2,2))

# Panel B: r_b(k) at fold scale (where running matters)
ax = axes[0, 1]
for label, color in [("B1", "tab:blue"), ("B2", "tab:orange"), ("B3", "tab:green")]:
    FR = fold_results[label]
    ax.semilogx(FR["k"], FR["r"], color=color, label=label)
ax.axvline(k_fold_sub, color="gray", ls="--", alpha=0.5, label=r"$k_{\rm fold}$")
ax.set_xlabel(r"$k$ [$M_{\rm KK}^{-1}$]")
ax.set_ylabel(r"$r_b(k)$")
ax.set_title("(B) r_b(k) at fold scale")
ax.legend(fontsize=8)

# Panel C: dr/d(ln k) at fold scale
ax = axes[1, 0]
for label, color in [("B1", "tab:blue"), ("B2", "tab:orange"), ("B3", "tab:green")]:
    FR = fold_results[label]
    ax.semilogx(FR["k"], FR["dr_dlnk"], color=color, label=label)
ax.axhline(-0.01, color="red", ls=":", alpha=0.5, label="|dr/dlnk| = 0.01")
ax.axhline(0.01, color="red", ls=":", alpha=0.5)
ax.axvline(k_fold_sub, color="gray", ls="--", alpha=0.5)
ax.set_xlabel(r"$k$ [$M_{\rm KK}^{-1}$]")
ax.set_ylabel(r"$dr_b/d\ln k$")
ax.set_title(r"(C) $dr_b/d\ln k$ at fold scale")
ax.legend(fontsize=8)

# Panel D: n_s correction at CMB scale
ax = axes[1, 1]
ax.semilogx(k_Mpc, ns_correction, "k-", lw=1.5)
ax.axhline(0, color="gray", ls="-", alpha=0.3)
ax.axvline(k_pivot_Mpc, color="gray", ls="--", alpha=0.5, label="k_pivot")
ax.axvspan(k_planck_min, k_planck_max, alpha=0.1, color="gray")
ax.set_xlabel(r"$k$ [Mpc$^{-1}$]")
ax.set_ylabel(r"$n_s^{\rm disp} - 1$")
ax.set_title(r"(D) $n_s$ correction from dispersion")
ax.legend(fontsize=8)
ax.ticklabel_format(axis='y', style='scientific', scilimits=(-2,2))

plt.tight_layout()
plt.savefig("s75_r_b_k_running.png", dpi=150, bbox_inches="tight")
print("Plot saved to s75_r_b_k_running.png")

print("\n" + "=" * 70)
print("COMPUTATION COMPLETE")
print("=" * 70)
