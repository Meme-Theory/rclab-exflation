#!/usr/bin/env python3
"""
s42_kz_fnl.py — Kibble-Zurek defect density and primordial non-Gaussianity f_NL
==============================================================================

Gate: FNL-42
PASS: |f_NL| in [0.5, 100]
FAIL: |f_NL| > 200 (excluded by Planck) or |f_NL| < 0.01 (undetectable)

Physics:
- BCS transition at the fold is second-order, Z_2 universality (GL-CUBIC-36)
- BDI winding = 0, U(1)_7 restored post-transit: NO persistent BCS defects
- Relevant defects are in the TAU FIELD: spatial regions where tau crossed
  the fold at different times (KZ mechanism on the modulus)
- The fabric IS space: defects in tau(x) are domain walls

Critical exponents for Z_2 (3D Ising) universality:
  nu = 0.6301, z = 2.02
  z_KZ = nu*z / (1 + nu*z) = 0.560

Author: gen-physicist (FNL-42)
Session: 42
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# ─── Configuration ──────────────────────────────────────────────────────────

ROOT = Path(r"C:\sandbox\Ainulindale Exflation")
TIER0 = ROOT / "tier0-computation"

def scalar(arr):
    """Convert a numpy array (possibly shape (1,)) to a Python float."""
    return float(np.asarray(arr).flat[0])

# ─── Physical constants ────────────────────────────────────────────────────

from canonical_constants import hbar_SI  # J s
from canonical_constants import c_light as c_SI  # m/s
from canonical_constants import G_N as G_N_SI  # m^3 kg^-1 s^-2
from canonical_constants import GeV_to_kg
M_Pl_SI = np.sqrt(hbar_SI * c_SI / G_N_SI)
GeV_per_kg = 1.0 / GeV_to_kg
M_Pl_GeV = M_Pl_SI * GeV_per_kg  # ~1.22e19 GeV
from canonical_constants import hbar_c_GeV_m as hbar_c_GeVm  # GeV m
from canonical_constants import Mpc_to_m as Mpc_m  # 1 Mpc in meters

# ─── Load input data ───────────────────────────────────────────────────────

stiff = np.load(TIER0 / "s42_gradient_stiffness.npz", allow_pickle=True)
dyn   = np.load(TIER0 / "s36_tau_dynamics.npz", allow_pickle=True)
inst  = np.load(TIER0 / "s37_instanton_action.npz", allow_pickle=True)
gl    = np.load(TIER0 / "s36_gl_cubic_check.npz", allow_pickle=True)
const = np.load(TIER0 / "s42_constants_snapshot.npz", allow_pickle=True)
c41   = np.load(TIER0 / "s41_constants_vs_tau.npz", allow_pickle=True)

# Extract scalars
Z_fold     = scalar(stiff["Z_fold"])         # 74,731 (spectral stiffness at fold)
G_DeWitt   = scalar(stiff["G_DeWitt"])       # 5.0 (DeWitt supermetric)
c_fabric   = scalar(stiff["c_fabric"])       # 210 (fabric sound speed)
dS_fold    = scalar(stiff["dS_fold"])        # dS/dtau at fold
d2S_fold   = scalar(stiff["d2S_fold"])       # d^2S/dtau^2 at fold
S_fold     = scalar(stiff["S_fold"])         # S at fold

tau_Q_raw  = scalar(dyn["an_S_full_dt_transit"])  # ~1.13e-3 (transit time, M_KK^{-1})
tau_fold   = scalar(dyn["tau_fold"])               # 0.19016
v_fold_raw = abs(scalar(dyn["traj_S_full_tau00p40_v_fold"]))  # ~29 (|dtau/dt| at fold)

xi_BCS     = scalar(inst["xi_BCS"])           # 0.808 M_KK^{-1}
Delta_BCS  = scalar(inst["Delta_0_num"])      # 0.365 M_KK

M_KK_grav  = scalar(const["M_KK_from_GN"])   # 7.43e16 GeV
M_KK_gauge = scalar(const["M_KK_kerner"])     # 5.04e17 GeV
a2_fold    = scalar(const["a2_fold"])         # 2776.2
a4_fold    = scalar(const["a4_fold"])         # 1350.7
a0_fold    = scalar(const["a0_fold"])         # 6440
fold_idx   = int(scalar(const["fold_idx"]))   # 7

universality = str(gl["universality_class"])  # BCS_Z2
c2_gl = scalar(gl["c2_tau020"])               # 2.366
c3_gl = scalar(gl["c3_tau020"])               # -0.0016
c4_gl = scalar(gl["c4_tau020"])               # -0.810

# a_2(tau) array for derivatives
tau_arr = c41["tau_values"]
a2_arr  = c41["a2_cutoff0"]

print("=" * 72)
print("FNL-42: Kibble-Zurek Defect Density and Primordial f_NL")
print("=" * 72)

# ═══════════════════════════════════════════════════════════════════════════
# STEP 1: Critical exponents and KZ scaling
# ═══════════════════════════════════════════════════════════════════════════

nu = 0.6301     # correlation length exponent (3D Ising / Z_2)
z  = 2.02       # dynamical critical exponent (Model A / TDGL)
z_KZ = nu * z / (1.0 + nu * z)  # KZ exponent

# Microscopic relaxation time
tau_0 = 1.0 / Delta_BCS  # ~2.74 M_KK^{-1}

# BCS window (from S36)
BCS_window = 0.03  # tau units

print(f"\n--- Step 1: Critical exponents ---")
print(f"  Universality class      = {universality}")
print(f"  nu = {nu}, z = {z}")
print(f"  z_KZ = nu*z/(1+nu*z)    = {z_KZ:.4f}")
print(f"  xi_0 (BCS coherence)    = {xi_BCS:.6f} M_KK^{{-1}}")
print(f"  Delta_BCS               = {Delta_BCS:.6f} M_KK")
print(f"  tau_0 = 1/Delta          = {tau_0:.6f} M_KK^{{-1}}")

# ═══════════════════════════════════════════════════════════════════════════
# STEP 2: Fabric-corrected quench rate
# ═══════════════════════════════════════════════════════════════════════════
#
# The fabric stiffness Z acts as an effective mass for spatial tau-variations.
# tau_Q_fabric = tau_Q * sqrt(1 + Z/G_mod)
#
# Physical meaning: the gradient energy Z*(nabla tau)^2 resists spatial
# inhomogeneity, effectively enlarging the domain size and slowing the
# effective quench seen by each point.

ratio_ZG = Z_fold / G_DeWitt
sqrt_factor = np.sqrt(1.0 + ratio_ZG)
tau_Q_fabric = tau_Q_raw * sqrt_factor

# Quench rate ratio
Q = tau_Q_fabric / tau_0  # dimensionless quench rate

print(f"\n--- Step 2: Fabric-corrected quench rate ---")
print(f"  tau_Q (raw transit)     = {tau_Q_raw:.6e} M_KK^{{-1}}")
print(f"  Z_fold                  = {Z_fold:.1f}")
print(f"  G_DeWitt                = {G_DeWitt:.1f}")
print(f"  Z/G                     = {ratio_ZG:.1f}")
print(f"  sqrt(1 + Z/G)           = {sqrt_factor:.2f}")
print(f"  tau_Q_fabric            = {tau_Q_fabric:.6e} M_KK^{{-1}}")
print(f"  Q = tau_Q_fabric/tau_0  = {Q:.6f}")
print(f"  REGIME: {'slow quench (Q>1)' if Q > 1 else 'FAST QUENCH (Q<1)'}")

# ═══════════════════════════════════════════════════════════════════════════
# STEP 3: KZ correlation length and defect density
# ═══════════════════════════════════════════════════════════════════════════
#
# Standard KZ scaling:
#   xi_KZ = xi_0 * Q^{z_KZ}
#
# For Q < 1 (fast quench): xi_KZ < xi_0 (smaller domains)
# For Q > 1 (slow quench): xi_KZ > xi_0 (larger domains)

xi_KZ = xi_BCS * Q**z_KZ

# Defect density (3D)
n_KZ = 1.0 / xi_KZ**3

# Freeze-out time (KZ hat-time):
# t_hat = (tau_Q_fabric^{nu*z} * tau_0)^{1/(1+nu*z)}
# = tau_0 * Q^{nu*z/(1+nu*z)} = tau_0 * Q^{z_KZ}
t_hat = tau_0 * Q**z_KZ

# The freeze-out happens at |t - t_c| = t_hat from the critical point.
# For fast quench (Q < 1), t_hat < tau_0: the system freezes almost immediately.
# The transit traverses the BCS window in time tau_Q_fabric.
# The freeze-out occurs at fraction t_hat/tau_Q_fabric of the transit.
freeze_frac = min(t_hat / tau_Q_fabric, 1.0)

# The tau variation within a KZ domain (spatial coherence):
# delta_tau_KZ = v_fold * t_hat (if t_hat < tau_Q_fabric)
#              = BCS_window (if t_hat > tau_Q_fabric, i.e., the whole window is frozen)
#
# BUT: v_fold = |dtau/dt| ~ 29 is the tau-field velocity in M_KK natural time.
# The fabric-corrected velocity is v_eff = v_fold / sqrt_factor (slowed by stiffness).
# Actually, v_fold is from the homogeneous trajectory — it gives the rate of
# tau change for the WHOLE fabric. The KZ delta_tau is the SPATIAL variation:
# how much tau differs between adjacent domains at freeze-out.
#
# The correct estimate: at freeze-out, the reduced temperature is
#   epsilon_hat = t_hat / tau_Q_fabric = Q^{z_KZ - 1} (if z_KZ < 1)
# The order parameter variation between domains:
#   delta_phi ~ phi_eq(epsilon_hat) ~ epsilon_hat^{beta}  (beta = 0.3265 for 3D Ising)
# Translating to tau variation:
#   delta_tau_KZ = BCS_window * epsilon_hat

beta_Ising = 0.3265  # order parameter exponent, 3D Ising
epsilon_hat = Q**(z_KZ)  # Note: z_KZ < 1, Q < 1, so epsilon_hat < 1
# Actually epsilon_hat = t_hat / tau_Q_fabric, not Q^z_KZ.
# epsilon_hat = (tau_0 * Q^{z_KZ}) / tau_Q_fabric = Q^{z_KZ} / Q = Q^{z_KZ - 1}
epsilon_hat_correct = Q**(z_KZ - 1.0)

# For Q = 0.05 and z_KZ = 0.56:
# epsilon_hat = 0.05^{-0.44} ~ 0.05^{-0.44} ~ 5.5
# This exceeds 1 → the entire BCS window is frozen.
# When epsilon_hat > 1, the system never gets close enough to criticality
# to enter the impulse regime — it's ALWAYS in the frozen regime.
# delta_tau_KZ = BCS_window (maximum, entire window frozen)

delta_tau_KZ = BCS_window * min(epsilon_hat_correct, 1.0)
# Actually in the FAST quench limit where epsilon_hat > 1, the KZ mechanism
# says the ENTIRE system is frozen. This means:
# - Every point crosses the fold independently
# - The spatial variation is set by the initial conditions, not KZ dynamics
# - delta_tau across a domain is the FULL BCS window

print(f"\n--- Step 3: KZ correlation length ---")
print(f"  Q = tau_Q_fabric/tau_0  = {Q:.6f}")
print(f"  z_KZ                    = {z_KZ:.4f}")
print(f"  xi_KZ = xi_0 * Q^z_KZ  = {xi_KZ:.6f} M_KK^{{-1}}")
print(f"  n_KZ = 1/xi_KZ^3       = {n_KZ:.4e} M_KK^3")
print(f"  t_hat (freeze-out time) = {t_hat:.6e} M_KK^{{-1}}")
print(f"  freeze fraction t_hat/tau_Q = {freeze_frac:.4f}")
print(f"  epsilon_hat = Q^(zKZ-1) = {epsilon_hat_correct:.4f}")
print(f"  {'ENTIRE WINDOW FROZEN' if epsilon_hat_correct >= 1.0 else 'Partial freeze-out'}")
print(f"  delta_tau_KZ            = {delta_tau_KZ:.6f}")

# ═══════════════════════════════════════════════════════════════════════════
# STEP 4: Physical scales
# ═══════════════════════════════════════════════════════════════════════════

print(f"\n--- Step 4: Physical scales ---")

M_KK_primary = M_KK_grav  # Use gravity route as primary

for label, M_KK in [("gravity", M_KK_grav), ("gauge", M_KK_gauge)]:
    L_KK = hbar_c_GeVm / M_KK         # M_KK^{-1} in meters
    xi_m = xi_KZ * L_KK               # xi_KZ in meters
    xi_Mpc = xi_m / Mpc_m             # xi_KZ in Mpc
    n_Mpc = 1.0 / xi_Mpc**3           # defect density in Mpc^{-3}

    print(f"\n  [{label}: M_KK = {M_KK:.3e} GeV]")
    print(f"    L_KK = M_KK^{{-1}}    = {L_KK:.3e} m")
    print(f"    xi_KZ                = {xi_m:.3e} m  = {xi_Mpc:.3e} Mpc")
    print(f"    n_KZ                 = {n_Mpc:.3e} Mpc^{{-3}}")

L_KK_prim = hbar_c_GeVm / M_KK_primary
xi_KZ_m = xi_KZ * L_KK_prim
xi_KZ_Mpc = xi_KZ_m / Mpc_m

# Hubble rate at the KK scale: H ~ M_KK^2 / M_Pl (radiation domination)
H_KK = M_KK_primary**2 / M_Pl_GeV   # in GeV
H_MKK = H_KK / M_KK_primary          # in M_KK units (dimensionless)
H_inv_MKK = 1.0 / H_MKK              # Hubble radius in M_KK^{-1}

print(f"\n  Hubble scale:")
print(f"    H (at KK scale)       = {H_KK:.3e} GeV = {H_MKK:.3e} M_KK")
print(f"    H^{{-1}}               = {H_inv_MKK:.3e} M_KK^{{-1}}")
print(f"    xi_KZ * H             = {xi_KZ * H_MKK:.3e}")
print(f"    N_domains/Hubble^3    = {(H_inv_MKK / xi_KZ)**3:.3e}")

xi_KZ_Hubble = xi_KZ * H_MKK
N_domains_Hubble = (H_inv_MKK / xi_KZ)**3

# ═══════════════════════════════════════════════════════════════════════════
# STEP 5: Spectral action derivatives (for delta N formalism)
# ═══════════════════════════════════════════════════════════════════════════
#
# The spectral action S[D_K(tau)] gives:
#   S = a_0 f_0 + a_2 f_2 R + a_4 f_4 (gauge + Higgs)
#
# The a_2 coefficient multiplies the Einstein-Hilbert term.
# A spatial variation in tau → spatial variation in effective M_Pl^2:
#   M_Pl^2(x) proportional to a_2(tau(x))
#
# The curvature perturbation from delta N formalism:
#   zeta = delta N = N_tau * delta_tau + (1/2) N_tautau * (delta_tau)^2 + ...
# where N = ln(a) = number of e-folds.
#
# For the modulus contribution to expansion:
#   N_tau = (1/2) * d ln(a_2) / d tau
#   N_tautau = (1/2) * d^2 ln(a_2) / d tau^2

# Compute d(a_2)/dtau and d^2(a_2)/dtau^2 by finite differences
if fold_idx > 0 and fold_idx < len(tau_arr) - 1:
    dt_plus = tau_arr[fold_idx + 1] - tau_arr[fold_idx]
    dt_minus = tau_arr[fold_idx] - tau_arr[fold_idx - 1]
    da2_dtau = (a2_arr[fold_idx + 1] - a2_arr[fold_idx - 1]) / (dt_plus + dt_minus)
    d2a2_dtau2 = 2.0 * (a2_arr[fold_idx + 1] / dt_plus
                         - a2_arr[fold_idx] * (1/dt_plus + 1/dt_minus)
                         + a2_arr[fold_idx - 1] / dt_minus) / (dt_plus + dt_minus)
else:
    da2_dtau = (a2_arr[fold_idx] - a2_arr[fold_idx - 1]) / (tau_arr[fold_idx] - tau_arr[fold_idx - 1])
    d2a2_dtau2 = 0.0

dln_a2 = da2_dtau / a2_fold
d2ln_a2 = d2a2_dtau2 / a2_fold - (da2_dtau / a2_fold)**2

# delta N derivatives
N_tau = 0.5 * dln_a2                  # d(N)/d(tau)
N_tautau = 0.5 * d2ln_a2             # d^2(N)/d(tau)^2

print(f"\n--- Step 5: Spectral action derivatives ---")
print(f"  a_2(tau_fold)           = {a2_fold:.2f}")
print(f"  da_2/dtau               = {da2_dtau:.4f}")
print(f"  d(ln a_2)/dtau          = {dln_a2:.6f}")
print(f"  d^2(ln a_2)/dtau^2      = {d2ln_a2:.6f}")
print(f"  N_tau = (1/2) d ln a_2  = {N_tau:.6f}")
print(f"  N_tautau                = {N_tautau:.6f}")

# ═══════════════════════════════════════════════════════════════════════════
# STEP 6: f_NL computation — three routes
# ═══════════════════════════════════════════════════════════════════════════

print(f"\n--- Step 6: f_NL computation ---")

# ─── ROUTE 1: delta N formalism (geometric nonlinearity of a_2) ───────────
#
# f_NL^{local} = (5/6) * N_tautau / N_tau^2
#
# This is the STANDARD result for non-Gaussianity from a modulus field
# with nonlinear mapping tau → N. It's always present regardless of
# inflation model.
#
# Physical interpretation: the spectral action's curvature in tau-space
# means that equal perturbations in tau produce UNEQUAL perturbations
# in the expansion history. This is the irreducible geometric f_NL.

if abs(N_tau) > 1e-30:
    f_NL_deltaN = (5.0 / 6.0) * N_tautau / N_tau**2
else:
    f_NL_deltaN = 0.0

print(f"\n  ROUTE 1: delta N formalism")
print(f"    f_NL = (5/6) * N_tt/N_t^2 = {f_NL_deltaN:.4f}")

# ─── ROUTE 2: KZ defect statistics (Poisson / chi-squared) ────────────────
#
# The KZ domains are independent realizations. At scales >> xi_KZ,
# the perturbation field is a sum of N_domains independent contributions.
# By CLT, the field is Gaussian with corrections ~ 1/sqrt(N).
#
# The non-Gaussianity at scale L:
#   f_NL(L) ~ (xi_KZ / L)^{3/2}  (for L >> xi_KZ)
#
# At CMB scales, L ~ H^{-1} ~ 10^{16} xi_KZ → f_NL is suppressed.
# At the KZ scale itself, f_NL ~ O(1).
#
# The CMB-scale defect f_NL:

f_NL_KZ_CMB = (xi_KZ_Hubble)**1.5  # ~ (xi_KZ * H)^{3/2}
print(f"\n  ROUTE 2: KZ defect statistics at CMB scales")
print(f"    xi_KZ / H^{{-1}}         = {xi_KZ_Hubble:.3e}")
print(f"    f_NL ~ (xi_KZ*H)^{{3/2}} = {f_NL_KZ_CMB:.3e}")
print(f"    (NEGLIGIBLE: defect scale far sub-Hubble)")

# ─── ROUTE 3: Modulated reheating / curvaton ──────────────────────────────
#
# The tau field modulates the BCS transition timing across space.
# Different spatial regions undergo the transition at slightly different
# tau values, creating a spatially-varying reheating surface.
#
# The GGE relic (S38) carries an entropy that depends on tau through
# the BCS gap: s_GGE(tau) ~ f(Delta(tau)).
#
# The non-Gaussianity from modulated reheating:
#   f_NL = (5/6) * [d^2 ln(Gamma)/d(tau)^2] / [d ln(Gamma)/d(tau)]^2
#
# where Gamma is the effective "decay rate" of the modulus into radiation.
# Here Gamma is controlled by the BCS dynamics: Gamma ~ Delta(tau).
#
# Near the fold, Delta varies sharply:
#   d ln Delta / d tau ~ 1/BCS_window ~ 33
#   d^2 ln Delta / d tau^2 ~ 1/BCS_window^2 ~ 1111
#
# The combined delta N including the BCS modulation:
#   N_tau_total = N_tau + (1/4) * d ln(s_GGE) / d tau
#               ~ N_tau + (1/4) * d ln Delta / d tau
#
# For the BCS gap: Delta ~ (tau - tau_c)^{1/2} near T_c (mean-field)
# So d ln Delta / d tau ~ 1/(2*(tau - tau_c)) diverges at the fold.
# We evaluate at the edge of the BCS window:
# d ln Delta / d tau |_{BCS edge} ~ 1 / (2 * BCS_window/2) = 1/BCS_window

dln_Delta_dtau = 1.0 / BCS_window  # ~33
d2ln_Delta_dtau2 = 1.0 / BCS_window**2  # ~1111

# Total N_tau including BCS modulation (the 1/4 factor is for radiation
# domination: rho ~ s^{4/3}, N ~ (1/4) ln(rho) ~ (1/3) ln(s))
N_tau_total = N_tau + (1.0 / 3.0) * dln_Delta_dtau
N_tautau_total = N_tautau + (1.0 / 3.0) * d2ln_Delta_dtau2

if abs(N_tau_total) > 1e-30:
    f_NL_modulated = (5.0 / 6.0) * N_tautau_total / N_tau_total**2
else:
    f_NL_modulated = 0.0

print(f"\n  ROUTE 3: Modulated reheating (BCS-sourced)")
print(f"    d ln Delta / d tau    = {dln_Delta_dtau:.2f}")
print(f"    d^2 ln Delta / d tau^2 = {d2ln_Delta_dtau2:.2f}")
print(f"    N_tau_total           = {N_tau_total:.6f}")
print(f"    N_tautau_total        = {N_tautau_total:.6f}")
print(f"    f_NL (mod. reheating) = {f_NL_modulated:.4f}")

# ─── ROUTE 4: Pure KZ scaling of the bispectrum ───────────────────────────
#
# For a Z_2 transition traversed at rate Q:
#   f_NL^{KZ} ~ Q^{-gamma_KZ} at scale k_KZ
# where gamma_KZ = z_KZ * (4-d)/(d*z + 2) (connected 3-point scaling)
#
# In d=3: gamma_KZ = z_KZ * 1/(3z+2) = 0.560 / 8.06 = 0.069
# f_NL(k_KZ) ~ Q^{-0.069} (weak Q dependence)

gamma_KZ = z_KZ / (3.0 * z + 2.0)
f_NL_KZ_local = Q**(-gamma_KZ)

print(f"\n  ROUTE 4: KZ bispectrum scaling at k_KZ")
print(f"    gamma_KZ              = {gamma_KZ:.4f}")
print(f"    f_NL(k_KZ)            = {f_NL_KZ_local:.4f}")
print(f"    (at k_KZ only, suppressed at CMB scales)")

# ═══════════════════════════════════════════════════════════════════════════
# STEP 7: Determine the DOMINANT channel
# ═══════════════════════════════════════════════════════════════════════════
#
# The question: which mechanism dominates at CMB scales?
#
# ROUTE 1 (delta N): Always present. Scale-independent. Value ~ O(1) if
# a_2(tau) has significant curvature relative to its slope squared.
#
# ROUTE 2 (KZ defect statistics): Suppressed by (xi_KZ * H)^{3/2} ~ 10^{-24}.
# NEGLIGIBLE at CMB scales.
#
# ROUTE 3 (modulated reheating): Present if the BCS transition timing
# varies across space. The key question is whether the delta_tau_KZ
# perturbation at the KZ scale propagates to CMB scales.
#
# For the HOMOGENEOUS transit (all of space crosses simultaneously),
# there is NO spatial variation in reheating → f_NL = 0 from this route.
#
# The KZ mechanism provides the SPATIAL VARIATION. But the variation is
# at scale xi_KZ << H^{-1}. At CMB scales, the variation averages out
# by CLT: the effective delta_tau at CMB scales is:
#   delta_tau(L) = delta_tau_KZ / sqrt(N_domains(L))
#                = delta_tau_KZ * (xi_KZ / L)^{3/2}
#
# The modulated reheating f_NL at CMB scales:
#   f_NL^{mod}(CMB) = f_NL_modulated * (delta_tau(CMB) / delta_tau_KZ)^{-1}
#                    × (additional suppression from averaging)
#
# Actually, the delta N formalism applied to the tau perturbation power
# spectrum gives:
#   P_zeta(k) = N_tau^2 * P_delta_tau(k)
#   B_zeta(k) = N_tau^3 * B_delta_tau(k) + N_tau^2 * N_tautau * [P*P terms]
#
# The second term is the standard delta N f_NL:
#   f_NL = (5/6) * N_tautau / N_tau^2 * (if tau perturbations dominate zeta)
#
# This is INDEPENDENT of the source of tau perturbations (quantum, KZ, etc.)
# as long as the tau perturbation power P_delta_tau is non-zero at CMB scales.
#
# The critical question becomes: what is the tau perturbation power at CMB scales?
#
# Scenario A: tau perturbations come from quantum fluctuations during inflation
#   → P_delta_tau(k) ~ (H_inf / (2*pi))^2 / (2*epsilon_H) at superhorizon scales
#   → f_NL = (5/6) * N_tautau / N_tau^2 (pure delta N)
#   → BUT: this requires tau to be LIGHT during inflation (m_tau < H_inf)
#
# Scenario B: tau perturbations come from the KZ mechanism
#   → P_delta_tau(k) localized at k ~ k_KZ ~ 1/xi_KZ
#   → At k_CMB << k_KZ: white noise (if walls decay) with amplitude ~ delta_tau_KZ^2 * xi_KZ^3
#   → f_NL at CMB scales: present but suppressed by spectral transfer
#
# For the framework, tau is a GEOMETRIC modulus — its mass is:
#   m_tau^2 ~ d2S/dtau2 / Vol_SU3 ~ 318,000 / 1350 ~ 236 M_KK^2
# This is ENORMOUS compared to H^2 ~ (M_KK^2/M_Pl)^2 ~ 4e-5 M_KK^2
# So tau is HEAVY during inflation: m_tau >> H_inf.
#
# For a heavy field: quantum fluctuations are suppressed by exp(-m_tau^2/H^2).
# The tau perturbation at CMB scales comes ENTIRELY from the KZ mechanism.

Vol_SU3 = scalar(stiff["Vol_SU3_Haar"])
m_tau_sq = d2S_fold / Vol_SU3
m_tau = np.sqrt(m_tau_sq)

print(f"\n--- Step 7: Dominant channel ---")
print(f"  m_tau^2                 = {m_tau_sq:.1f} M_KK^2")
print(f"  m_tau                   = {m_tau:.3f} M_KK")
print(f"  H (at KK)              = {H_MKK:.3e} M_KK")
print(f"  m_tau / H               = {m_tau / H_MKK:.3e}")
print(f"  → tau is HEAVY (m >> H): quantum fluctuations exponentially suppressed")
print(f"  → Tau perturbations at CMB scales come from KZ mechanism only")

# KZ perturbation power at CMB scales:
# For domain walls that decay (tau-domain walls are unstable — single attractor):
# P_delta_tau(k) ~ delta_tau_KZ^2 * xi_KZ^3  for k < k_KZ
# This is white noise (flat spectrum) injected at the phase transition.

P_dtau_KZ = delta_tau_KZ**2 * xi_KZ**3  # in M_KK^{-3} (power spectrum amplitude)

# The dimensionless power spectrum at CMB scale k_CMB:
# Delta^2_tau(k) = k^3 / (2*pi^2) * P_tau(k)
# k_CMB ~ H_MKK (Hubble scale at KK epoch)
Delta2_tau_CMB = (H_MKK)**3 / (2 * np.pi**2) * P_dtau_KZ

# The curvature perturbation power from tau:
# Delta^2_zeta(k) = N_tau_total^2 * Delta^2_tau(k)
Delta2_zeta_tau = N_tau_total**2 * Delta2_tau_CMB

# Compare to observed CMB power:
Delta2_zeta_obs = 2.1e-9  # A_s from Planck

# Fraction of CMB power from KZ tau perturbations:
r_power = Delta2_zeta_tau / Delta2_zeta_obs

print(f"\n  KZ perturbation power at CMB scales:")
print(f"    delta_tau_KZ          = {delta_tau_KZ:.6f}")
print(f"    P_delta_tau_KZ        = {P_dtau_KZ:.6e} M_KK^{{-3}}")
print(f"    Delta^2_tau(k_CMB)    = {Delta2_tau_CMB:.6e}")
print(f"    Delta^2_zeta(tau)     = {Delta2_zeta_tau:.6e}")
print(f"    Delta^2_zeta(obs)     = {Delta2_zeta_obs:.6e}")
print(f"    r_power (tau/obs)     = {r_power:.6e}")

# ═══════════════════════════════════════════════════════════════════════════
# STEP 8: Final f_NL — correct multi-field treatment
# ═══════════════════════════════════════════════════════════════════════════
#
# CRITICAL PHYSICS: The curvaton formula f_NL = 5/(4r) applies to a COHERENT
# field perturbation at CMB scales. The KZ mechanism produces INCOHERENT
# perturbations at scale xi_KZ << H^{-1}. These are stochastic, not coherent.
#
# At CMB scales, each Hubble-volume patch contains N_domains ~ 10^9 KZ cells.
# By the central limit theorem, the averaged tau perturbation is:
#   <delta_tau>_Hubble ~ delta_tau_KZ / sqrt(N_domains)
# and the non-Gaussianity (skewness) is suppressed by:
#   f_NL(CMB) ~ f_NL(KZ scale) / N_domains
#
# The curvaton formula does NOT apply because:
# 1. The tau perturbation is incoherent (many independent domains per Hubble)
# 2. The field is heavy (m_tau >> H → no quantum fluctuations at CMB scales)
# 3. The transit is fast (tau_Q * H << 1 → homogeneous within each Hubble patch)
#
# CORRECT multi-field delta N:
# For N_domains independent KZ cells within a Hubble volume:
#   P_zeta(k_CMB) = N_tau^2 * P_delta_tau(k_CMB)
#   B_zeta(k_CMB) = N_tau^2 * N_tautau * [P*P] + N_tau^3 * B_delta_tau
#
# The first term (geometric nonlinearity) gives:
#   f_NL^{geo} = (5/6) * N_tautau / N_tau^2  (independent of KZ details)
# BUT it requires P_delta_tau(k_CMB) ≠ 0, i.e., tau perturbations AT CMB scales.
#
# The second term (intrinsic non-Gaussianity of KZ field) gives:
#   f_NL^{KZ} ~ N_domains^{-1} × f_NL(KZ scale) ~ 10^{-9}
#
# Since tau is HEAVY (m_tau / H = 2522), there are NO quantum tau perturbations
# at CMB scales. The ONLY tau perturbations come from KZ, which is stochastic.
#
# Therefore: P_delta_tau at CMB scales is from the white-noise KZ spectrum,
# and the effective r_power computed above (2.0e-3) is correct for the POWER,
# but the non-Gaussianity is suppressed by 1/N_domains because the underlying
# field is a sum of independent contributions.
#
# FINAL f_NL at CMB scales:
#   f_NL = f_NL^{inflaton} + f_NL^{KZ_stochastic}
#
# where:
#   f_NL^{inflaton}: from whatever field generates the primordial perturbations
#     (single-field slow-roll → O(0.01), or multi-field → model-dependent)
#   f_NL^{KZ_stochastic}: the KZ contribution, suppressed by 1/N_domains
#
# For the delta N applied to the stochastic KZ field:
#   f_NL^{KZ,geo} = (5/6) * N_tautau / N_tau^2 × r_power^2
#   (the r^2 suppression because both bispectrum and power contribute at CMB)
#
# More precisely, for two uncorrelated sources (inflaton + KZ stochastic):
#   f_NL = [f_NL^{inf} * P_inf^2 + f_NL^{tau,eff} * P_tau^2] / (P_inf + P_tau)^2
#
# With P_tau / P_inf = r_power = 2e-3:
#   f_NL ≈ f_NL^{inf} * (1 - 2*r_power) + f_NL^{tau,eff} * r_power^2

# f_NL from the KZ tau field at CMB scales:
# The stochastic field's non-Gaussianity at scale L >> xi_KZ:
#   S_3(L) = <zeta^3(L)> / <zeta^2(L)>^{3/2} ~ 1/sqrt(N_domains(L))
# This means f_NL_tau_eff ~ f_NL_intrinsic / sqrt(N_domains)

# Route 1 f_NL applied to the stochastic average:
f_NL_tau_stochastic = f_NL_deltaN / N_domains_Hubble

# Route 3 modulated reheating applied stochastically:
f_NL_mod_stochastic = f_NL_modulated / N_domains_Hubble

# The inflaton f_NL: we don't know the inflaton model, so we use the
# single-field consistency relation as a floor:
# f_NL^{single-field} = (5/12)(1 - n_s) ≈ (5/12)(0.035) ≈ 0.015
f_NL_inflaton = (5.0 / 12.0) * 0.035  # ≈ 0.015

# Total f_NL:
f_NL_total = f_NL_inflaton + f_NL_tau_stochastic * r_power**2 + f_NL_mod_stochastic * r_power**2

# However, there is one MORE channel that could matter:
# The MODULATED REHEATING from inflaton perturbations.
# If the inflaton perturbation delta_phi modulates when the BCS transition happens,
# this creates a correlated perturbation at CMB scales.
#
# The inflaton perturbation is delta_phi ~ H/(2*pi*sqrt(2*epsilon)).
# This translates to delta_tau ~ (d tau / d phi) * delta_phi.
# For the spectral action potential: d tau / d phi depends on the
# inflaton-modulus coupling, which the framework does not specify.
#
# IN THE FRAMEWORK: the spectral action S[D_K(tau)] is the ENTIRE potential.
# If tau IS the inflaton (which TAU-DYN-36 showed is NOT viable — fast roll),
# then there's no separate inflaton and f_NL would be from a non-slow-roll mechanism.
#
# The framework's position: a SEPARATE inflaton is required (because tau fast-rolls).
# The inflaton-tau coupling is NOT determined by the spectral action alone.
# Therefore, the modulated reheating f_NL from the inflaton-tau coupling
# is a MODEL-DEPENDENT quantity that the framework cannot predict from
# first principles without specifying the inflaton sector.
#
# HOWEVER: we can bound it. If the inflaton is the ONLY light field,
# and it couples to tau only gravitationally, then the modulated reheating
# contribution is:
#   f_NL^{mod, inflaton} ~ (5/6) * N_tautau / N_tau^2 × r_grav
# where r_grav = (M_KK / M_Pl)^2 ~ 3.7e-5 (gravitational coupling).
#
# This gives f_NL^{mod, grav} ~ 28 * 3.7e-5 ~ 0.001 (negligible).
#
# If the inflaton couples directly to the spectral action (e.g., through
# a_2 dependence on the inflaton), the coupling is model-dependent.
#
# CONCLUSION: The framework's ROBUST prediction is:
# f_NL = f_NL^{inflaton} + negligible KZ corrections
# = O(0.01) from single-field slow-roll
# with a POSSIBLE additional contribution from inflaton-tau coupling
# that is model-dependent.

r_grav = (M_KK_primary / M_Pl_GeV)**2
f_NL_mod_grav = f_NL_deltaN * r_grav

f_NL_final = f_NL_inflaton + f_NL_mod_grav
dominant_route = "inflaton floor + gravitational modulation"

# But report the RANGE:
# Minimum: single-field floor ~ 0.015
# Maximum: if inflaton couples strongly to tau, up to f_NL_deltaN ~ -28
# (but this would be excluded by Planck if |f_NL| > 10)

f_NL_min = f_NL_inflaton  # 0.015
f_NL_max = f_NL_deltaN     # -28 (if tau dominates — but excluded by Planck AND by fast-roll)

print(f"\n--- Step 8: Final f_NL (correct multi-field treatment) ---")
print(f"\n  Stochastic CLT suppression:")
print(f"    N_domains/Hubble^3    = {N_domains_Hubble:.3e}")
print(f"    f_NL^{{tau,stochastic}}  = {f_NL_tau_stochastic:.3e} (delta N / N_dom)")
print(f"    f_NL^{{mod,stochastic}}  = {f_NL_mod_stochastic:.3e} (mod reheating / N_dom)")
print(f"    → Both NEGLIGIBLE at CMB scales")
print(f"\n  Inflaton contribution:")
print(f"    f_NL^{{inflaton}} (SR)   = {f_NL_inflaton:.4f}")
print(f"    r_grav = (M_KK/M_Pl)^2 = {r_grav:.3e}")
print(f"    f_NL^{{mod,grav}}        = {f_NL_mod_grav:.4e}")
print(f"    f_NL (TOTAL)            = {f_NL_final:.4f}")
print(f"\n  RANGE (model-dependent):")
print(f"    f_NL_min (SR floor)   = {f_NL_min:.4f}")
print(f"    f_NL_max (full coupling) = {f_NL_max:.2f} (excluded if |f_NL|>10)")
print(f"    Dominant route:       {dominant_route}")
print(f"\n  KEY PHYSICS:")
print(f"    tau is HEAVY (m/H = {m_tau/H_MKK:.0f}): no quantum perturbations at CMB")
print(f"    KZ domains sub-Hubble (xi*H = {xi_KZ_Hubble:.1e}): CLT suppresses NG")
print(f"    Transit homogeneous (tau_Q*H = {tau_Q_fabric*H_MKK:.1e}): same timing across Hubble")
print(f"    → Framework predicts f_NL ~ {f_NL_final:.3f} (indistinguishable from LCDM)")

# ═══════════════════════════════════════════════════════════════════════════
# STEP 9: Wall energetics and defect cross-checks
# ═══════════════════════════════════════════════════════════════════════════

# Wall energy density
E_wall = 0.5 * Z_fold * (delta_tau_KZ / xi_KZ)**2  # M_KK^4
epsilon_wall = E_wall / a0_fold

# Wall tension (energy per unit area)
sigma_wall = Z_fold * delta_tau_KZ**2 / xi_KZ  # M_KK^3

# Gravitational coupling
G_sigma = (M_KK_primary / M_Pl_GeV)**2 * sigma_wall  # dimensionless (G * sigma in nat. units)

# Wall lifetime
tau_wall = xi_KZ / c_fabric  # in M_KK^{-1}

# Defect contribution to CMB anisotropy
delta_T_defect = G_sigma * xi_KZ_Hubble

print(f"\n--- Step 9: Wall energetics ---")
print(f"  E_wall (density)        = {E_wall:.4e} M_KK^4")
print(f"  epsilon_wall = E/rho    = {epsilon_wall:.4e}")
print(f"  sigma_wall (tension)    = {sigma_wall:.4e} M_KK^3")
print(f"  G*sigma                 = {G_sigma:.4e}")
print(f"  tau_wall                = {tau_wall:.4e} M_KK^{{-1}}")
print(f"  tau_wall * H            = {tau_wall * H_MKK:.4e}")
print(f"  (delta T/T)_defect      = {delta_T_defect:.4e}")

# ═══════════════════════════════════════════════════════════════════════════
# STEP 10: Sensitivity analysis
# ═══════════════════════════════════════════════════════════════════════════

print(f"\n--- Step 10: Sensitivity analysis ---")

# Vary BCS window
print(f"\n  Varying BCS window width:")
bw_vals = [0.005, 0.01, 0.02, 0.03, 0.05, 0.1]
fnl_bw = []
for bw in bw_vals:
    dl = 1.0 / bw
    d2l = 1.0 / bw**2
    Nt = N_tau + (1.0/3.0) * dl
    Ntt = N_tautau + (1.0/3.0) * d2l
    fn = (5.0/6.0) * Ntt / Nt**2 if abs(Nt) > 1e-30 else 0.0
    fnl_bw.append(fn)
    print(f"    BCS_window = {bw:.3f} → f_NL(delta N) = {fn:.3f}")

# Vary Z_fold
print(f"\n  Varying Z_fold factor:")
zf_factors = [0.01, 0.1, 0.5, 1.0, 2.0, 10.0, 100.0]
for zf in zf_factors:
    Z_var = Z_fold * zf
    tQf = tau_Q_raw * np.sqrt(1.0 + Z_var / G_DeWitt)
    Qvar = tQf / tau_0
    xi_var = xi_BCS * Qvar**z_KZ
    P_var = BCS_window**2 * min(Qvar**(z_KZ - 1.0), 1.0)**2 * xi_var**3
    D2_var = H_MKK**3 / (2*np.pi**2) * P_var
    r_var = N_tau_total**2 * D2_var / Delta2_zeta_obs
    print(f"    Z*{zf:<5.2f} = {Z_var:>10.0f}: Q={Qvar:.4f}, xi_KZ={xi_var:.6f}, r_power={r_var:.2e}")

# ═══════════════════════════════════════════════════════════════════════════
# GATE VERDICT
# ═══════════════════════════════════════════════════════════════════════════

print(f"\n{'=' * 72}")
print(f"FINAL RESULTS")
print(f"{'=' * 72}")

f_abs = abs(f_NL_final)
if 0.5 <= f_abs <= 100:
    verdict = "PASS"
elif f_abs > 200:
    verdict = "FAIL_EXCLUDED"
elif f_abs < 0.01:
    verdict = "FAIL_UNDETECTABLE"
elif 0.01 <= f_abs < 0.5:
    verdict = "MARGINAL"
elif 100 < f_abs <= 200:
    verdict = "MARGINAL_HIGH"
else:
    verdict = "UNKNOWN"

planck_central = -0.9
planck_sigma = 5.1
cmbs4_sigma = 0.5

consistent_planck = abs(f_NL_final - planck_central) < 2 * planck_sigma
detectable_cmbs4 = f_abs > cmbs4_sigma

print(f"\n  Kibble-Zurek parameters:")
print(f"    xi_0 (BCS)            = {xi_BCS:.4f} M_KK^{{-1}}")
print(f"    tau_Q (raw)           = {tau_Q_raw:.4e} M_KK^{{-1}}")
print(f"    tau_Q_fabric          = {tau_Q_fabric:.4e} M_KK^{{-1}}")
print(f"    Q = tau_Q/tau_0       = {Q:.6f}")
print(f"    z_KZ                  = {z_KZ:.4f}")
print(f"    xi_KZ                 = {xi_KZ:.6f} M_KK^{{-1}}")
print(f"    xi_KZ                 = {xi_KZ_m:.3e} m = {xi_KZ_Mpc:.3e} Mpc")
print(f"    n_KZ = 1/xi_KZ^3     = {n_KZ:.4e} M_KK^3")
print(f"    N_domains/Hubble^3   = {N_domains_Hubble:.3e}")

print(f"\n  Non-Gaussianity (all routes):")
print(f"    f_NL (delta N, if tau dominant)  = {f_NL_deltaN:.4f}")
print(f"    f_NL (mod. reheating, if tau dom)= {f_NL_modulated:.4f}")
print(f"    f_NL (KZ stochastic at CMB)      = {f_NL_tau_stochastic:.4e}")
print(f"    f_NL (mod. stochastic at CMB)    = {f_NL_mod_stochastic:.4e}")
print(f"    f_NL (KZ at CMB, direct)         = {f_NL_KZ_CMB:.4e}")
print(f"    r_power (KZ/obs)                 = {r_power:.4e}")
print(f"    Dominant route:                  {dominant_route}")
print(f"    f_NL (FINAL)                     = {f_NL_final:.4f}")
print(f"    f_NL RANGE: [{f_NL_min:.3f}, {f_NL_max:.1f}] (model-dependent)")

print(f"\n  Gate FNL-42:")
print(f"    |f_NL|                = {f_abs:.4f}")
print(f"    Criterion [0.5,100]   → {verdict}")
print(f"    Planck ({planck_central}+/-{planck_sigma}):   {'CONSISTENT' if consistent_planck else 'EXCLUDED'}")
print(f"    CMB-S4 (sigma~{cmbs4_sigma}):   {'DETECTABLE' if detectable_cmbs4 else 'BELOW threshold'}")
print(f"    LCDM prediction:      f_NL ~ 0")

# ═══════════════════════════════════════════════════════════════════════════
# SAVE DATA
# ═══════════════════════════════════════════════════════════════════════════

save_dict = dict(
    gate_name=np.array(["FNL-42"]),
    verdict=np.array([verdict]),

    # Critical exponents
    nu=nu, z_dyn=z, z_KZ=z_KZ,
    universality_class=np.array([universality]),
    beta_Ising=beta_Ising,

    # Input parameters
    xi_BCS=xi_BCS, Delta_BCS=Delta_BCS, tau_0=tau_0,
    tau_Q_raw=tau_Q_raw, Z_fold=Z_fold, G_DeWitt=G_DeWitt,
    tau_fold=tau_fold, c_fabric=c_fabric,
    BCS_window=BCS_window,
    M_KK_grav=M_KK_grav, M_KK_gauge=M_KK_gauge,

    # Derived: quench
    ratio_ZG=ratio_ZG, sqrt_factor=sqrt_factor,
    tau_Q_fabric=tau_Q_fabric, Q=Q,

    # Derived: KZ
    xi_KZ=xi_KZ, n_KZ=n_KZ,
    t_hat=t_hat, freeze_frac=freeze_frac,
    epsilon_hat=epsilon_hat_correct,
    delta_tau_KZ=delta_tau_KZ,
    xi_KZ_m=xi_KZ_m, xi_KZ_Mpc=xi_KZ_Mpc,

    # Hubble
    H_KK=H_KK, H_MKK=H_MKK,
    xi_KZ_Hubble=xi_KZ_Hubble,
    N_domains_Hubble=N_domains_Hubble,

    # Spectral action derivatives
    a2_fold=a2_fold, da2_dtau=da2_dtau, d2a2_dtau2=d2a2_dtau2,
    dln_a2=dln_a2, d2ln_a2=d2ln_a2,
    N_tau=N_tau, N_tautau=N_tautau,
    dS_fold=dS_fold, d2S_fold=d2S_fold, S_fold=S_fold,

    # Mass
    m_tau=m_tau, m_tau_sq=m_tau_sq, Vol_SU3=Vol_SU3,

    # Power spectrum
    P_dtau_KZ=P_dtau_KZ, Delta2_tau_CMB=Delta2_tau_CMB,
    Delta2_zeta_tau=Delta2_zeta_tau, Delta2_zeta_obs=Delta2_zeta_obs,
    r_power=r_power,

    # GL coefficients
    c2_gl=c2_gl, c3_gl=c3_gl, c4_gl=c4_gl,

    # f_NL results
    f_NL_deltaN=f_NL_deltaN,
    f_NL_modulated=f_NL_modulated,
    f_NL_KZ_CMB=f_NL_KZ_CMB,
    f_NL_KZ_local=f_NL_KZ_local,
    f_NL_tau_stochastic=f_NL_tau_stochastic,
    f_NL_mod_stochastic=f_NL_mod_stochastic,
    f_NL_inflaton=f_NL_inflaton,
    f_NL_mod_grav=f_NL_mod_grav,
    f_NL_final=f_NL_final,
    f_NL_min=f_NL_min,
    f_NL_max=f_NL_max,
    r_grav=r_grav,
    dominant_route=np.array([dominant_route]),

    # Wall energetics
    E_wall=E_wall, epsilon_wall=epsilon_wall,
    sigma_wall=sigma_wall, G_sigma=G_sigma,
    tau_wall=tau_wall, delta_T_defect=delta_T_defect,

    # Observational
    planck_central=planck_central, planck_sigma=planck_sigma,
    cmbs4_sigma=cmbs4_sigma,
    consistent_planck=consistent_planck,
    detectable_cmbs4=detectable_cmbs4,

    # Sensitivity
    sens_bw=np.array(bw_vals),
    sens_fnl_bw=np.array(fnl_bw),
)

np.savez(TIER0 / "s42_kz_fnl.npz", **save_dict)
print(f"\nData saved to: {TIER0 / 's42_kz_fnl.npz'}")

# ═══════════════════════════════════════════════════════════════════════════
# PLOT
# ═══════════════════════════════════════════════════════════════════════════

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("FNL-42: Kibble-Zurek Defect Density and Primordial $f_{NL}$",
             fontsize=14, fontweight='bold')

# Panel 1: Z(tau) and fabric stiffness
ax1 = axes[0, 0]
tau_g = stiff["tau_grid"]
Z_sp = stiff["Z_spectral"]
ax1.semilogy(tau_g, Z_sp, 'b-o', markersize=5, label='$Z(\\tau)$')
ax1.axvline(tau_fold, color='r', ls='--', alpha=0.6, label=f'$\\tau_{{fold}}$={tau_fold:.3f}')
ax1.axhline(G_DeWitt, color='gray', ls=':', alpha=0.5, label=f'$G_{{DeWitt}}$={G_DeWitt}')
ax1.set_xlabel('$\\tau$')
ax1.set_ylabel('$Z(\\tau)$')
ax1.set_title('Fabric Stiffness $Z(\\tau)$')
ax1.legend(fontsize=8)
ax1.grid(True, alpha=0.3)
# Annotate the ratio
ax1.annotate(f'$Z/G = {ratio_ZG:.0f}$\n$\\sqrt{{1+Z/G}} = {sqrt_factor:.0f}$',
             xy=(0.05, 0.75), xycoords='axes fraction', fontsize=9,
             bbox=dict(boxstyle='round', fc='lightyellow', alpha=0.8))

# Panel 2: f_NL vs BCS window width
ax2 = axes[0, 1]
bw_range = np.linspace(0.003, 0.15, 300)
fnl_range = []
for bw in bw_range:
    dl = 1.0 / bw
    d2l = 1.0 / bw**2
    Nt = N_tau + (1.0/3.0) * dl
    Ntt = N_tautau + (1.0/3.0) * d2l
    fnl_range.append((5.0/6.0) * Ntt / Nt**2 if abs(Nt) > 1e-30 else 0.0)
fnl_range = np.array(fnl_range)

ax2.plot(bw_range, fnl_range, 'b-', linewidth=2, label='$f_{NL}^{\\delta N}$')
ax2.axhline(0.5, color='green', ls='--', alpha=0.6, label='CMB-S4 $1\\sigma$')
ax2.axhline(100, color='red', ls='--', alpha=0.6, label='$f_{NL} = 100$')
ax2.axvline(BCS_window, color='purple', ls=':', alpha=0.8,
            label=f'BCS window = {BCS_window}')
ax2.scatter([BCS_window], [f_NL_modulated], color='red', s=100, zorder=5,
            label=f'Framework: $f_{{NL}}$ = {f_NL_modulated:.2f}')
ax2.set_xlabel('BCS window width $\\Delta\\tau$')
ax2.set_ylabel('$f_{NL}$ (local)')
ax2.set_title('$f_{NL}$ vs BCS Window (delta N formalism)')
ax2.legend(fontsize=7, loc='upper right')
ax2.set_ylim(0, min(max(5, f_NL_modulated * 3), 150))
ax2.grid(True, alpha=0.3)

# Panel 3: xi_KZ vs quench rate Q
ax3 = axes[1, 0]
Q_range = np.logspace(-3, 2, 200)
xi_range = xi_BCS * Q_range**z_KZ
n_range = 1.0 / xi_range**3

ax3_twin = ax3.twinx()
ax3.loglog(Q_range, xi_range, 'b-', linewidth=2, label='$\\xi_{KZ}$')
ax3_twin.loglog(Q_range, n_range, 'r-', linewidth=1.5, alpha=0.5, label='$n_{KZ}$')
ax3.axvline(Q, color='green', ls='--', alpha=0.6, label=f'$Q = {Q:.4f}$')
ax3.axhline(xi_BCS, color='gray', ls=':', alpha=0.4, label=f'$\\xi_0 = {xi_BCS:.3f}$')
ax3.scatter([Q], [xi_KZ], color='red', s=100, zorder=5)
ax3.set_xlabel('$Q = \\tau_{Q,fabric} / \\tau_0$')
ax3.set_ylabel('$\\xi_{KZ}$ ($M_{KK}^{-1}$)', color='b')
ax3_twin.set_ylabel('$n_{KZ}$ ($M_{KK}^3$)', color='r')
ax3.set_title('KZ Correlation Length and Defect Density')
ax3.legend(fontsize=8, loc='upper left')
ax3.grid(True, alpha=0.3)

# Panel 4: Summary
ax4 = axes[1, 1]
ax4.axis('off')
ax4.set_title('Gate FNL-42 Summary', fontsize=12, fontweight='bold')

# Determine color by verdict
vcolor = {'PASS': 'lightgreen', 'FAIL_EXCLUDED': 'lightcoral',
          'FAIL_UNDETECTABLE': 'lightyellow', 'MARGINAL': 'lightyellow'}.get(verdict, 'white')

summary = (
    f"GATE: FNL-42 | VERDICT: {verdict}\n\n"
    f"Kibble-Zurek:\n"
    f"  Q = tau_Q_fabric/tau_0 = {Q:.4f}  (FAST QUENCH)\n"
    f"  xi_KZ = {xi_KZ:.4f} M_KK^(-1) = {xi_KZ_m:.1e} m\n"
    f"  n_KZ = {n_KZ:.1e} M_KK^3\n"
    f"  N_domains/Hubble = {N_domains_Hubble:.1e}\n\n"
    f"f_NL routes (intrinsic):\n"
    f"  delta N (if tau dom.)  = {f_NL_deltaN:.1f}\n"
    f"  Mod. reheating         = {f_NL_modulated:.2f}\n"
    f"  KZ stochastic (CLT)    = {f_NL_tau_stochastic:.1e}\n\n"
    f"Why KZ f_NL is negligible:\n"
    f"  tau HEAVY: m_tau/H = {m_tau/H_MKK:.0f}\n"
    f"  xi_KZ*H = {xi_KZ_Hubble:.1e} (sub-Hubble)\n"
    f"  CLT: N_dom = {N_domains_Hubble:.1e}\n"
    f"  r_power = {r_power:.1e}\n\n"
    f"f_NL (FINAL) = {f_NL_final:.4f}\n"
    f"  Range: [{f_NL_min:.3f}, {f_NL_max:.1f}]\n\n"
    f"Observations:\n"
    f"  Planck: {planck_central}+/-{planck_sigma}: {'OK' if consistent_planck else 'EXCL'}\n"
    f"  CMB-S4 (sigma {cmbs4_sigma}): {'DET' if detectable_cmbs4 else 'BELOW'}\n"
    f"  LCDM: f_NL ~ 0 (SAME AS FRAMEWORK)"
)
ax4.text(0.02, 0.98, summary, transform=ax4.transAxes,
         fontsize=8.5, verticalalignment='top', fontfamily='monospace',
         bbox=dict(boxstyle='round', facecolor=vcolor, alpha=0.8))

plt.tight_layout()
plt.savefig(TIER0 / "s42_kz_fnl.png", dpi=150, bbox_inches='tight')
print(f"Plot saved to: {TIER0 / 's42_kz_fnl.png'}")

print(f"\n{'=' * 72}")
print("DONE.")
print(f"{'=' * 72}")
