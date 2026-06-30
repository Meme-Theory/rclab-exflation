"""
S74 W1-Q: COULOMB-GAS-INSTANTON-VEFF-74
========================================

Re-compute V_eff(tau) using the Coulomb-gas partition function for the
instanton-anti-instanton plasma, instead of the dilute Boltzmann sum used
in W1-B sub-gate (a). Test whether the 309x shortfall in single-instanton
restoring force can be closed by multi-instanton condensation.

Substrate framing
-----------------
The Coulomb gas of instantons is NOT a gas of particles in a container.
It is a statistical-mechanical partition function over topologically
distinct sectors of the Jensen-deformed SU(3) gauge bundle, with each
sector labeled by (n_I, n_{Ibar}). The "Coulomb" part is the long-range
logarithmic interaction between instantons (mediated by the gauge field
propagator), which is structurally identical to the 2D Coulomb gas but
lives in the tau-direction of the moduli space, not in real space.

Structure
---------
Z_CG(tau) = sum_{n_I, n_Ibar} y(tau)^(n_I+n_Ibar) / (n_I! n_Ibar!) *
            Integral dM exp(-sum pairwise ln|x_i - x_j|)

Truncation: sectors up to (n_I + n_Ibar) <= 3.
Fugacity: y(tau) = exp(-S_inst(tau)) from S73A instanton landscape.
Pairwise interactions: log-distance terms from gauge-field propagator,
regularized with rho_min = M_KK^{-1} and rho_max = Vol(SU(3))^{1/8}.

Gate (pre-registered)
---------------------
PASS  if |dV_eff^CG/dtau| at tau=0.48 within factor 2 of driving force
      (|ratio| > 0.5  --> within factor 2  of |dV_bare/dtau|)
INFO  if within factor 10
      (0.1 < |ratio| <= 0.5)
FAIL  if |ratio| <= 0.1

The "driving force 58,673 M_KK" cited in the task plan is the spectral
action gradient dS/dtau at the fold (tau=0.19). At tau=0.48, the LOCAL
V_bare gradient is dV_bare/dtau = 445 M_KK^4. We report the gate in BOTH
normalizations so the outcome is unambiguous.

Inputs
------
computations/_shared/canonical_constants.py
computations/session-73/s73a_instanton_landscape.npz
computations/session-74/s74_moduli_stabilization.npz

Outputs
-------
computations/session-74/s74_coulomb_gas_instanton.npz
computations/session-74/s74_coulomb_gas_instanton.png
"""
import os
import sys
import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from canonical_constants import (
    M_KK,
    tau_fold,
    dS_fold,
    PI,
    Vol_SU3_Haar,
)

# =============================================================================
# Load inputs
# =============================================================================
print("=" * 70)
print("S74 W1-Q: COULOMB-GAS-INSTANTON-VEFF-74")
print("=" * 70)

d_inst = np.load(os.path.join(HERE, "s73a_instanton_landscape.npz"),
                 allow_pickle=True)
tau_inst = d_inst["tau_scan"]                 # (21,) tau grid 0..1
S_inst_arr = d_inst["S_inst_A"]               # (21,) instanton action S_inst(tau)
n_inst_unnorm = d_inst["n_inst_unnorm"]       # (21,) dilute-gas density
tau_kappa1 = float(d_inst["kappa1_crossings"][0])  # ~0.48035

d_W1B = np.load(os.path.join(HERE, "s74_moduli_stabilization.npz"),
                allow_pickle=True)
dV_bare_dtau_kappa1 = float(d_W1B["dV_bare_dtau_at_kappa1"])  # M_KK^4 (local)
force_inst_A_W1B = float(d_W1B["force_inst_A"])               # dilute one-inst
force_inst_B_W1B = float(d_W1B["force_inst_B"])
E_inst_A = float(d_W1B["E_inst_A"])  # ~0.749 M_KK^4 normalization
E_inst_B = float(d_W1B["E_inst_B"])  # 1.0 M_KK^4 normalization
tau_scan_W1B = d_W1B["tau_inst_scan"]
n_inst_on_scan_W1B = d_W1B["n_inst_on_scan"]

print(f"\nInputs loaded:")
print(f"  tau_kappa1 (from S73A)    = {tau_kappa1:.6f}")
print(f"  S_inst @ tau=0.5 (approx) = {float(CubicSpline(tau_inst, S_inst_arr)(0.5)):.4f}")
print(f"  n_inst_unnorm max         = {n_inst_unnorm.max():.6f}")
print(f"  W1-B dV_bare/dtau         = {dV_bare_dtau_kappa1:.4f} M_KK^4")
print(f"  W1-B force_inst_A         = {force_inst_A_W1B:.6f} M_KK^4")
print(f"  W1-B force_inst_B         = {force_inst_B_W1B:.6f} M_KK^4")
print(f"  E_inst_A                  = {E_inst_A:.6f} M_KK^4")
print(f"  W1-B ratio |F_A/dV_bare|  = {abs(force_inst_A_W1B)/abs(dV_bare_dtau_kappa1):.4e}")
print(f"  W1-B shortfall factor     = {abs(dV_bare_dtau_kappa1)/abs(force_inst_A_W1B):.1f}x")

# =============================================================================
# 1. Coulomb-gas geometry setup
# =============================================================================
# The log-Coulomb interaction between an instanton at moduli-position
# x_i and another at x_j is:
#     S_int(i,j) = q_i q_j * g_log * ln( |x_i - x_j| / rho_min ),
# where q_i = +1 for instanton, -1 for anti-instanton, and g_log is the
# coupling extracted from the 1-loop gauge propagator in the instanton
# background. For SU(3) on the Jensen-deformed fiber, g_log = 1 in natural
# units of the instanton action (cf. Callan-Dashen-Gross 1978, dilute-
# instanton gas two-point function).
#
# UV/IR regulators:
#   rho_min = M_KK^{-1}            (UV cutoff: nearest fibre separation)
#   rho_max = Vol_SU3^(1/8)         (IR cutoff: extent of moduli space)
# We use Vol_SU3_Haar = 8 sqrt(3) pi^4 ~ 1349.74, so:
#   R_moduli = Vol_SU3^(1/8) ~ 2.405  (dimensionless, in M_KK units)
# =============================================================================
rho_min = 1.0                          # M_KK^{-1} in units where M_KK=1       # (local)
rho_max = Vol_SU3_Haar ** (1.0 / 8.0)  # IR cutoff ~2.40                       # (local)
g_log = 1.0                            # log-coupling, SU(3) natural units     # (local)

print(f"\nCoulomb-gas geometry:")
print(f"  rho_min (UV)     = {rho_min:.4f}")
print(f"  rho_max (IR)     = {rho_max:.4f}")
print(f"  log-coupling g   = {g_log:.4f}")

# Dimensionless moduli volume in tau-direction: the instanton moduli space
# at fixed tau has a volume ratio V(tau) = (rho_max - rho_min)^2 for
# 2-instanton and (rho_max - rho_min)^4 for 3-instanton. We use the
# saddle-point value <x_i - x_j> = sqrt(V(tau)) for the log integral.
# This is the standard Callan-Dashen-Gross "mean-field Coulomb" approximation.

# =============================================================================
# 2. Pairwise interaction integrals (saddle-point / mean-field)
# =============================================================================
# In the 2-instanton sector (1 I + 1 I-bar = neutral), the pairwise
# log integral averages to:
#   <S_int> = g_log * <ln(|x_1 - x_2| / rho_min)>
# For the relative separation integrated over the annulus [rho_min, rho_max]
# with uniform measure in d^2 x:
#
#   <ln(r/rho_min)> = (rho_max^2 ln(rho_max/rho_min) - (rho_max^2-rho_min^2)/2)
#                      / (rho_max^2 - rho_min^2)
#
# This gives the mean log-distance, which is what appears in the
# Coulomb-gas saddle-point for the instanton pair.
# =============================================================================
def mean_log_distance(rmin, rmax):
    """Mean of ln(r/rmin) over the annulus [rmin, rmax] with flat 2D measure."""
    num = rmax**2 * np.log(rmax / rmin) - 0.5 * (rmax**2 - rmin**2)
    den = rmax**2 - rmin**2
    return num / den

mean_log = mean_log_distance(rho_min, rho_max)
print(f"  <ln(r/rho_min)>  = {mean_log:.6f}")

# For opposite charges (+/-) the interaction is attractive:  -g_log * mean_log
# For same charges (I-I or Ibar-Ibar) the interaction is repulsive: +g_log * mean_log
# In the 2-sector we have 1 pair of opposite charges -> 1 attractive log.
# In the 3-sector (2 I + 1 Ibar) or (1 I + 2 Ibar) we have 3 pairs:
#   - 2 attractive (each I interacts with the Ibar)
#   - 1 repulsive  (the 2 same-charge particles repel)
# Net effective interaction in 3-sector: -2g*mean + 1g*mean = -g*mean_log
# In the 3-sector (3 I) or (3 Ibar), all pairs repel:
#   - 3 pairs, all repulsive: +3g*mean_log
S_int_2_sector = -g_log * mean_log                # attractive (1 pair)         # (local)
S_int_3_mixed = -g_log * mean_log                 # 3 pairs, net attractive     # (local)
S_int_3_pure = 3.0 * g_log * mean_log             # 3 pairs, all repulsive      # (local)

print(f"\nSaddle-point interaction energies:")
print(f"  S_int (2-sector, I-Ibar)     = {S_int_2_sector:+.6f}")
print(f"  S_int (3-sector, 2I+1Ibar)   = {S_int_3_mixed:+.6f}")
print(f"  S_int (3-sector, 3I or 3Ibar) = {S_int_3_pure:+.6f}")

# =============================================================================
# 3. Partition function Z_CG(tau) via (n_I, n_Ibar) sector truncation
# =============================================================================
# Z_CG = sum_{n_I, n_Ibar} y^{n_I+n_Ibar}/(n_I! n_Ibar!) * exp(-S_int_sector)
#
# sectors with n_I + n_Ibar <= 3:
#   (0,0)   -> 1
#   (1,0), (0,1) -> single instanton/anti-instanton
#   (2,0), (1,1), (0,2) -> 2-sector
#   (3,0), (2,1), (1,2), (0,3) -> 3-sector
#
# The single-particle sector has no interaction (no pair to interact with).
# We keep the spectral action volume element as the "moduli volume" that
# matches W1-B normalization: the fugacity y absorbs the Coleman one-loop
# determinant factor present in n_inst_unnorm from S73A.
# =============================================================================
def Z_CG_from_fugacity(y):
    """
    Coulomb-gas partition function truncated to n_I + n_Ibar <= 3.

    y : float or array, fugacity exp(-S_inst).
    returns Z_CG(y).
    """
    # Sector (0,0): vacuum
    Z0 = 1.0                                                                    # (local)
    # Sector (1,0) + (0,1): single instanton / anti-instanton
    Z1 = 2.0 * y                                                                # (local)
    # Sector (2,0) + (0,2): 2 I (or 2 Ibar) -- repulsive single pair
    # Number of pairs = 1, interaction = + g*mean_log (same charge)
    Z2_pure = 2.0 * (y**2 / 2.0) * np.exp(-(+g_log * mean_log))                 # (local)
    # Sector (1,1): I + Ibar -- attractive single pair
    Z2_mixed = (y**2 / (1.0 * 1.0)) * np.exp(-S_int_2_sector)                   # (local)
    # Sector (3,0) + (0,3): 3 I (or 3 Ibar) -- all 3 pairs repulsive
    Z3_pure = 2.0 * (y**3 / 6.0) * np.exp(-S_int_3_pure)                        # (local)
    # Sector (2,1) + (1,2): 2I + 1Ibar or 1I + 2Ibar -- net attractive
    Z3_mixed = 2.0 * (y**3 / (2.0 * 1.0)) * np.exp(-S_int_3_mixed)              # (local)

    return Z0 + Z1 + Z2_pure + Z2_mixed + Z3_pure + Z3_mixed

# =============================================================================
# 4. Evaluate Z_CG(tau) on the tau scan
# =============================================================================
# Interpolate S_inst(tau) and n_inst(tau) from the S73A landscape.
cs_S_inst = CubicSpline(tau_inst, S_inst_arr)
cs_n_inst = CubicSpline(tau_inst, n_inst_unnorm)

# Dense tau grid in the relevant window [0.2, 0.9]; clip to data range
tau_grid = np.linspace(0.20, 0.95, 201)                                         # (local)

# Fugacity y(tau): use n_inst_unnorm from S73A (this already absorbs the
# Coleman determinant factor, so is the correct "dressed fugacity"). The
# bare exp(-S_inst) would double-count the one-loop determinant.
#
# W1-B used V_inst = -E_inst * n_inst(tau). Matching conventions:
#   y(tau) = n_inst(tau)        <-- "dressed fugacity"
# This choice makes the dilute limit of Z_CG reduce exactly to W1-B.
y_dressed = cs_n_inst(tau_grid)                                                 # (local)
y_dressed = np.maximum(y_dressed, 0.0)  # n_inst must be non-negative           # (local)

# Compute Z_CG on the grid
Z_CG_grid = Z_CG_from_fugacity(y_dressed)                                       # (local)

# V_eff(tau) from Coulomb gas:
#   V_eff = -E_inst * ln(Z_CG) / Vol_M4
# We use Vol_M4 = 1 in M_KK^4 units (the normalization W1-B used).
# Choose E_inst = E_inst_A for direct comparability with W1-B force_inst_A.
Vol_M4 = 1.0                                                                    # (local)
V_eff_CG_A = -E_inst_A * np.log(Z_CG_grid) / Vol_M4                             # (local)
V_eff_CG_B = -E_inst_B * np.log(Z_CG_grid) / Vol_M4                             # (local)

# Compute dV_eff_CG/dtau via finite differences (centered)
dV_eff_CG_dtau_A = np.gradient(V_eff_CG_A, tau_grid)                            # (local)
dV_eff_CG_dtau_B = np.gradient(V_eff_CG_B, tau_grid)                            # (local)

# Also compute the dilute-gas comparison V_inst_dilute = -E_inst * n_inst(tau)
V_dilute_A = -E_inst_A * cs_n_inst(tau_grid)                                    # (local)
V_dilute_B = -E_inst_B * cs_n_inst(tau_grid)                                    # (local)
dV_dilute_dtau_A = np.gradient(V_dilute_A, tau_grid)                            # (local)
dV_dilute_dtau_B = np.gradient(V_dilute_B, tau_grid)                            # (local)

# =============================================================================
# 5. Evaluate at tau = 0.48 (kappa=1 crossing), plus comparison table
# =============================================================================
idx_048 = np.argmin(np.abs(tau_grid - 0.48))
idx_target_array = np.argmin(np.abs(tau_grid - tau_kappa1))

def at_tau(arr, tau_val):
    idx = np.argmin(np.abs(tau_grid - tau_val))
    return float(arr[idx])

tau_probes = [0.45, 0.48, 0.55, 0.60, 0.70]                                     # (local)

print("\n" + "=" * 70)
print("COMPARISON TABLE: dilute (W1-B) vs Coulomb gas")
print("=" * 70)
print(f"{'tau':>6} | {'n_inst':>10} | {'|dV_dilute|':>12} | {'|dV_CG|':>12} | {'ratio CG/dilute':>16}")
print("-" * 70)
rows = []
for tp in tau_probes:
    n_at = float(cs_n_inst(tp))
    dv_dil = abs(at_tau(dV_dilute_dtau_A, tp))
    dv_cg = abs(at_tau(dV_eff_CG_dtau_A, tp))
    ratio = dv_cg / dv_dil if dv_dil > 1e-12 else np.nan                        # (local)
    rows.append((tp, n_at, dv_dil, dv_cg, ratio))
    print(f"{tp:>6.2f} | {n_at:>10.6f} | {dv_dil:>12.6f} | {dv_cg:>12.6f} | {ratio:>16.6f}")

# =============================================================================
# 6. Gate evaluation at tau = 0.48
# =============================================================================
dV_CG_at_048_A = abs(at_tau(dV_eff_CG_dtau_A, tau_kappa1))                      # (local)
dV_CG_at_048_B = abs(at_tau(dV_eff_CG_dtau_B, tau_kappa1))                      # (local)

# Ratio convention #1 (matches W1-B):
# compare against LOCAL dV_bare/dtau at tau=0.48 (445 M_KK^4)
ratio_local_A = dV_CG_at_048_A / abs(dV_bare_dtau_kappa1)                       # (local)
ratio_local_B = dV_CG_at_048_B / abs(dV_bare_dtau_kappa1)                       # (local)

# Ratio convention #2 (task-plan reference):
# compare against dS/dtau @ fold = 58,673 M_KK (UV trace gradient)
ratio_dSfold_A = dV_CG_at_048_A / dS_fold                                       # (local)
ratio_dSfold_B = dV_CG_at_048_B / dS_fold                                       # (local)

# W1-B dilute reference at tau=0.48
dV_dilute_at_048_A = abs(at_tau(dV_dilute_dtau_A, tau_kappa1))                  # (local)
ratio_dilute_A = dV_dilute_at_048_A / abs(dV_bare_dtau_kappa1)                  # (local)

print("\n" + "=" * 70)
print(f"GATE EVALUATION at tau = {tau_kappa1:.6f}")
print("=" * 70)
print(f"  W1-B dilute |dV/dtau|              = {dV_dilute_at_048_A:.6f} M_KK^4")
print(f"  W1-B dilute ratio / dV_bare        = {ratio_dilute_A:.6e}  (309x shortfall)")
print("  -----")
print(f"  Coulomb-gas |dV/dtau| (E_inst_A)   = {dV_CG_at_048_A:.6f} M_KK^4")
print(f"  Coulomb-gas |dV/dtau| (E_inst_B)   = {dV_CG_at_048_B:.6f} M_KK^4")
print(f"  ratio vs |dV_bare/dtau|  (A)       = {ratio_local_A:.6e}")
print(f"  ratio vs |dV_bare/dtau|  (B)       = {ratio_local_B:.6e}")
print(f"  ratio vs dS/dtau_fold (A)          = {ratio_dSfold_A:.6e}")
print(f"  ratio vs dS/dtau_fold (B)          = {ratio_dSfold_B:.6e}")

# Enhancement factor over dilute
enhancement_A = dV_CG_at_048_A / dV_dilute_at_048_A if dV_dilute_at_048_A > 1e-15 else np.nan
print(f"  Coulomb-gas enhancement over dilute = {enhancement_A:.6f}x")

# Gate: PASS if ratio_local > 0.5 (within factor 2)
#       INFO if 0.1 < ratio_local <= 0.5 (within factor 10)
#       FAIL if ratio_local <= 0.1
verdict = "FAIL"
if ratio_local_A > 0.5:
    verdict = "PASS"
elif ratio_local_A > 0.1:
    verdict = "INFO"

print(f"\n  ratio_local_A = {ratio_local_A:.4e}")
print(f"  PASS threshold (factor 2 of driving)  : >= 0.5")
print(f"  INFO threshold (factor 10 of driving) : >= 0.1")
print(f"  GATE VERDICT: {verdict}")

# =============================================================================
# 7. Cross-checks
# =============================================================================
print("\n" + "=" * 70)
print("CROSS-CHECKS")
print("=" * 70)

# Cross-check 1: dilute limit (y -> 0)
# For y << 1, Z_CG ~ 1 + 2y, so -ln(Z_CG) ~ -2y and
# dV_eff_CG/dtau ~ -2 * E_inst * dy/dtau.
# The dilute single-instanton force was -E_inst * dn_inst/dtau.
# So the Coulomb gas with y_dressed = n_inst gives dilute_limit * 2.
# The factor of 2 arises because Coulomb gas counts I AND I-bar separately
# (charge-neutral sum), while W1-B counted only the single-instanton sector.
tau_dilute_check = 0.25                                                         # (local)
y_check = float(cs_n_inst(tau_dilute_check))                                    # (local)
Z_check = Z_CG_from_fugacity(y_check)                                           # (local)
V_check = -E_inst_A * np.log(Z_check)                                           # (local)
V_linear_check = -E_inst_A * 2.0 * y_check                                      # (local)
dilute_ratio = V_check / V_linear_check if abs(V_linear_check) > 1e-15 else np.nan
print(f"  Cross-check 1 (dilute y -> 0 limit at tau={tau_dilute_check}):")
print(f"    y(tau)             = {y_check:.6f}")
print(f"    V_CG               = {V_check:.6f}")
print(f"    V_linear (-2*E*y)  = {V_linear_check:.6f}")
print(f"    ratio              = {dilute_ratio:.6f}  (should be near 1 for y<<1)")

# Cross-check 2: log-Coulomb cutoff sensitivity
# Shift rho_max by +/-20% and check the tau=0.48 answer changes by < 10%
def eval_Z_CG_at_048(rho_max_local):
    mean_log_loc = mean_log_distance(rho_min, rho_max_local)                    # (local)
    S2 = -g_log * mean_log_loc                                                  # (local)
    S3_mixed = -g_log * mean_log_loc                                            # (local)
    S3_pure = 3.0 * g_log * mean_log_loc                                        # (local)
    # Recompute on grid
    Z_grid = np.zeros_like(tau_grid)                                            # (local)
    for i, _tg in enumerate(tau_grid):
        y_i = float(cs_n_inst(_tg))                                             # (local)
        y_i = max(y_i, 0.0)                                                     # (local)
        Z_grid[i] = (
            1.0
            + 2.0 * y_i
            + 2.0 * (y_i**2 / 2.0) * np.exp(-S3_pure / 3.0 * 1.0)  # same-charge pair = g*ln
            + (y_i**2) * np.exp(-S2)
            + 2.0 * (y_i**3 / 6.0) * np.exp(-S3_pure)
            + 2.0 * (y_i**3 / 2.0) * np.exp(-S3_mixed)
        )
    V_eff_loc = -E_inst_A * np.log(Z_grid)                                      # (local)
    dV_loc = np.gradient(V_eff_loc, tau_grid)                                   # (local)
    return abs(dV_loc[idx_target_array])

# Simpler: rebuild with adjusted mean_log
def eval_dV_CG_at_048_with_rmax(rho_max_local):
    mean_log_loc = mean_log_distance(rho_min, rho_max_local)                    # (local)
    S2 = -g_log * mean_log_loc                                                  # (local)
    S3_mixed = -g_log * mean_log_loc                                            # (local)
    S3_pure = 3.0 * g_log * mean_log_loc                                        # (local)
    S_same_pair = g_log * mean_log_loc  # interaction for (2,0) same-charge pair  # (local)

    y_vec = np.maximum(cs_n_inst(tau_grid), 0.0)                                # (local)
    Z_vec = (
        1.0
        + 2.0 * y_vec
        + 2.0 * (y_vec**2 / 2.0) * np.exp(-S_same_pair)
        + (y_vec**2) * np.exp(-S2)
        + 2.0 * (y_vec**3 / 6.0) * np.exp(-S3_pure)
        + 2.0 * (y_vec**3 / 2.0) * np.exp(-S3_mixed)
    )
    V_loc = -E_inst_A * np.log(Z_vec)                                           # (local)
    dV_loc = np.gradient(V_loc, tau_grid)                                       # (local)
    return abs(dV_loc[idx_target_array])

dV_rmax_plus = eval_dV_CG_at_048_with_rmax(rho_max * 1.2)                       # (local)
dV_rmax_minus = eval_dV_CG_at_048_with_rmax(rho_max * 0.8)                      # (local)
dV_rmax_half = eval_dV_CG_at_048_with_rmax(rho_max * 0.5)                       # (local)
dV_rmax_double = eval_dV_CG_at_048_with_rmax(rho_max * 2.0)                     # (local)
rel_shift_p20 = abs(dV_rmax_plus - dV_CG_at_048_A) / dV_CG_at_048_A             # (local)
rel_shift_m20 = abs(dV_rmax_minus - dV_CG_at_048_A) / dV_CG_at_048_A            # (local)

print(f"\n  Cross-check 2 (log-Coulomb cutoff sensitivity):")
print(f"    rho_max = {rho_max:.4f}  ->  |dV|@0.48 = {dV_CG_at_048_A:.6f}")
print(f"    rho_max x 1.2          ->  |dV|@0.48 = {dV_rmax_plus:.6f}  (shift {rel_shift_p20*100:.2f}%)")
print(f"    rho_max x 0.8          ->  |dV|@0.48 = {dV_rmax_minus:.6f}  (shift {rel_shift_m20*100:.2f}%)")
print(f"    rho_max x 0.5          ->  |dV|@0.48 = {dV_rmax_half:.6f}")
print(f"    rho_max x 2.0          ->  |dV|@0.48 = {dV_rmax_double:.6f}")
cutoff_robust = (rel_shift_p20 < 0.10) and (rel_shift_m20 < 0.10)               # (local)
print(f"    within 10% for +/-20% shift: {cutoff_robust}")

# Cross-check 3: Z_CG positivity / attraction enhancement
# For attractive I-Ibar interaction, Z_CG > Z_dilute (with the same y)
Z_dilute_exact = 1.0 + 2.0 * y_dressed + 2.0 * (y_dressed**2 / 2.0) + y_dressed**2 + 2.0 * (y_dressed**3 / 6.0) + 2.0 * (y_dressed**3 / 2.0)  # (local)
Z_CG_larger = (Z_CG_grid >= Z_dilute_exact - 1e-12)                             # (local)
all_larger = bool(np.all(Z_CG_larger))                                          # (local)
frac_larger = float(np.mean(Z_CG_larger))                                       # (local)
print(f"\n  Cross-check 3 (Z_CG > Z_dilute for attractive I-Ibar):")
print(f"    Z_CG > Z_dilute  fraction of grid = {frac_larger*100:.2f}%")
print(f"    all: {all_larger}")

# Cross-check 4: Z_CG > 0 everywhere (partition function positivity)
Z_positive = bool(np.all(Z_CG_grid > 0))                                        # (local)
print(f"\n  Cross-check 4 (Z_CG > 0 everywhere):")
print(f"    min Z_CG = {Z_CG_grid.min():.6f}")
print(f"    all positive: {Z_positive}")

# =============================================================================
# 8. Save outputs
# =============================================================================
out_npz = os.path.join(HERE, "s74_coulomb_gas_instanton.npz")
np.savez(
    out_npz,
    # Grid
    tau_grid=tau_grid,
    tau_kappa1=tau_kappa1,
    # Inputs
    S_inst_grid=cs_S_inst(tau_grid),
    n_inst_grid=cs_n_inst(tau_grid),
    y_dressed=y_dressed,
    # Partition function and potential
    Z_CG_grid=Z_CG_grid,
    V_eff_CG_A=V_eff_CG_A,
    V_eff_CG_B=V_eff_CG_B,
    dV_eff_CG_dtau_A=dV_eff_CG_dtau_A,
    dV_eff_CG_dtau_B=dV_eff_CG_dtau_B,
    # Dilute comparison
    V_dilute_A=V_dilute_A,
    V_dilute_B=V_dilute_B,
    dV_dilute_dtau_A=dV_dilute_dtau_A,
    dV_dilute_dtau_B=dV_dilute_dtau_B,
    # Gate numbers
    dV_CG_at_048_A=dV_CG_at_048_A,
    dV_CG_at_048_B=dV_CG_at_048_B,
    dV_dilute_at_048_A=dV_dilute_at_048_A,
    dV_bare_dtau_kappa1=dV_bare_dtau_kappa1,
    ratio_local_A=ratio_local_A,
    ratio_local_B=ratio_local_B,
    ratio_dSfold_A=ratio_dSfold_A,
    ratio_dSfold_B=ratio_dSfold_B,
    enhancement_A=enhancement_A,
    # Cutoff sensitivity
    rho_min=rho_min,
    rho_max=rho_max,
    g_log=g_log,
    mean_log=mean_log,
    dV_rmax_plus=dV_rmax_plus,
    dV_rmax_minus=dV_rmax_minus,
    dV_rmax_half=dV_rmax_half,
    dV_rmax_double=dV_rmax_double,
    rel_shift_p20=rel_shift_p20,
    rel_shift_m20=rel_shift_m20,
    cutoff_robust=cutoff_robust,
    # Z_CG positivity and attraction
    all_Z_positive=Z_positive,
    frac_Z_larger_than_dilute=frac_larger,
    # Comparison table
    tau_probes=np.array(tau_probes),
    table_n_at=np.array([r[1] for r in rows]),
    table_dv_dil=np.array([r[2] for r in rows]),
    table_dv_cg=np.array([r[3] for r in rows]),
    table_ratio=np.array([r[4] for r in rows]),
    # Gate verdict
    gate_name="COULOMB-GAS-INSTANTON-VEFF-74",
    gate_verdict=verdict,
)
print(f"\nSaved: {out_npz}")

# =============================================================================
# 9. Plot
# =============================================================================
fig, axes = plt.subplots(2, 2, figsize=(12, 9))

# Panel (a): V_eff(tau) dilute vs Coulomb gas
ax = axes[0, 0]
ax.plot(tau_grid, V_dilute_A, "b-", label="Dilute (W1-B, E_inst_A)", lw=2)
ax.plot(tau_grid, V_eff_CG_A, "r--", label="Coulomb gas (E_inst_A)", lw=2)
ax.axvline(tau_kappa1, color="gray", ls=":", label=f"tau_kappa1={tau_kappa1:.3f}")
ax.set_xlabel("tau")
ax.set_ylabel(r"$V_{\rm inst}(\tau)$  [M_KK^4]")
ax.set_title("(a) Instanton effective potential")
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel (b): dV/dtau dilute vs Coulomb gas
ax = axes[0, 1]
ax.plot(tau_grid, dV_dilute_dtau_A, "b-", label="Dilute dV/dtau", lw=2)
ax.plot(tau_grid, dV_eff_CG_dtau_A, "r--", label="Coulomb gas dV/dtau", lw=2)
ax.axvline(tau_kappa1, color="gray", ls=":")
ax.axhline(0, color="k", lw=0.5)
ax.set_xlabel("tau")
ax.set_ylabel(r"$dV_{\rm inst}/d\tau$  [M_KK^4]")
ax.set_title("(b) Restoring force")
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel (c): |dV/dtau| vs driving force |dV_bare/dtau|
ax = axes[1, 0]
ax.semilogy(tau_grid, np.abs(dV_dilute_dtau_A) + 1e-16,
            "b-", label="|dV_dilute/dtau|", lw=2)
ax.semilogy(tau_grid, np.abs(dV_eff_CG_dtau_A) + 1e-16,
            "r--", label="|dV_CG/dtau|", lw=2)
ax.axhline(abs(dV_bare_dtau_kappa1), color="g", ls="-",
           label=f"|dV_bare/dtau|={abs(dV_bare_dtau_kappa1):.1f}")
ax.axhline(0.5 * abs(dV_bare_dtau_kappa1), color="orange", ls=":",
           label="PASS threshold (factor 2)")
ax.axhline(0.1 * abs(dV_bare_dtau_kappa1), color="r", ls=":",
           label="FAIL threshold (factor 10)")
ax.axvline(tau_kappa1, color="gray", ls=":")
ax.set_xlabel("tau")
ax.set_ylabel(r"$|dV/d\tau|$  [M_KK^4]")
ax.set_title("(c) Restoring force vs driving force (log scale)")
ax.legend(fontsize=8, loc="lower right")
ax.grid(True, alpha=0.3)

# Panel (d): Z_CG ratio over Z_dilute (enhancement by multi-inst attraction)
ax = axes[1, 1]
Z_ratio = Z_CG_grid / Z_dilute_exact
ax.plot(tau_grid, Z_ratio, "k-", lw=2)
ax.axhline(1, color="b", ls="--", label="Z_CG = Z_dilute")
ax.axvline(tau_kappa1, color="gray", ls=":")
ax.set_xlabel("tau")
ax.set_ylabel(r"$Z_{\rm CG}(\tau) / Z_{\rm dilute}(\tau)$")
ax.set_title("(d) Coulomb gas enhancement over dilute")
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

fig.suptitle(f"S74 W1-Q: Coulomb-gas instanton V_eff -- verdict: {verdict}",
             fontsize=13, fontweight="bold")
fig.tight_layout()
out_png = os.path.join(HERE, "s74_coulomb_gas_instanton.png")
fig.savefig(out_png, dpi=120)
print(f"Saved: {out_png}")

# =============================================================================
# Summary
# =============================================================================
print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)
print(f"Gate: COULOMB-GAS-INSTANTON-VEFF-74")
print(f"Verdict: {verdict}")
print(f"Coulomb-gas |dV_eff/dtau| at tau=0.48  : {dV_CG_at_048_A:.6f} M_KK^4")
print(f"W1-B dilute |dV/dtau| at tau=0.48      : {dV_dilute_at_048_A:.6f} M_KK^4")
print(f"Enhancement factor (CG / dilute)        : {enhancement_A:.6f}x")
print(f"Ratio CG / |dV_bare/dtau|              : {ratio_local_A:.4e}")
print(f"W1-B dilute ratio                      : {ratio_dilute_A:.4e}")
print(f"Remaining shortfall                    : {1.0/ratio_local_A:.1f}x  (was 309x in W1-B)")
