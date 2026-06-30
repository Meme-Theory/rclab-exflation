#!/usr/bin/env python3
"""
S61 — HEAT-KERNEL-A2-61: Seeley-DeWitt a_2 from Local Curvature Integral
==========================================================================

Gate: HEAT-KERNEL-A2-61
  PASS if a_2(tau_fold) finite and H_0 in [60,80] km/s/Mpc.
  FAIL if H_0 outside [40,100] or divergent.
  INFO if H_0 well-defined but outside [60,80].

Physics:
  The Seeley-DeWitt coefficient a_2(D_K^2) is a LOCAL geometric integral,
  finite and well-defined on any compact Riemannian manifold. It does NOT
  diverge with Peter-Weyl truncation level (unlike the spectral zeta sum
  zeta_D(1) = 2776.17 which was shown to diverge in S60 PW-H0-CONV-60).

  For the spin-Dirac operator D_K on (SU(3), g_Jensen(tau)):
    D_K^2 = nabla*nabla + R/4   (Lichnerowicz formula)

  The Gilkey a_2 coefficient:
    a_2^{SD}(D_K^2) = (4pi)^{-d/2} * integral_K tr_S(R/6 - E) dvol    (*)

  where d=8, E = -R/4 (from D^2 = -(nabla^2 + E)), so R/6 - E = 5R/12.
  tr_S = trace over spinor bundle (rank 2^{d/2} = 16).

  On the homogeneous space SU(3) with left-invariant metric, R is constant:
    a_2^{SD} = (4pi)^{-4} * 16 * (5R/12) * Vol
             = (4pi)^{-4} * (20R/3) * Vol                               (1)

  CCM dictionary for M4 x K (Chamseddine-Connes-Marcolli):
  The 4D reduced Planck mass from spectral action on M^4 x K:
    M_Pl_red^2 = (f_2 / (4*pi^2)) * M_KK^2 * int_K tr_S(R/6 - E) dvol (2)
               = M_KK^2 * (20R/3) * Vol / (4*pi^2)                      (3)
               = M_KK^2 * (4*pi)^2 * a_2^{SD}                           (4)
               = M_KK^2 * 16*pi^2 * a_2^{SD}                            (5)

  Then: H_0 = sqrt(Lambda_obs / 3) * M_Pl_red (in suitable units).

  Scalar curvature R(tau) — exact analytic formula (verified S20a, 147/147):
    R(tau) = -0.25*exp(-4*tau) + 2.0*exp(-tau) - 0.25 + 0.5*exp(2*tau)  (6)

  R(0) = -0.25 + 2.0 - 0.25 + 0.5 = 2.0 (Einstein metric, verified S46).

  Volume: Vol_SU3_Haar = 8*sqrt(3)*pi^4 = 1349.74 (volume-preserving Jensen).

Author: Spectral-Geometer (Session 61)
Date: 2026-03-28
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import (
    tau_fold, Vol_SU3_Haar, M_KK, M_KK_gravity, M_KK_kerner,
    M_Pl_reduced, M_Pl_unreduced, H_0_km_s_Mpc, Omega_Lambda,
    PI, rho_Lambda_obs, Lambda_obs_MP4,
    a0_fold, a2_fold, a4_fold,  # spectral sums for comparison
    G_N, c_light, hbar_SI,
    Mpc_to_m, hbar_c_GeV_m,
)

# ==============================================================================
#  SECTION 1: Scalar Curvature R(tau) — Exact Analytic Formula
# ==============================================================================

def R_scalar(tau):
    """
    Exact scalar curvature R(tau) on Jensen-deformed SU(3).

    Convention: alpha = g0_diag = 3.0 (Killing metric normalization).
    Jensen metric: x_u1 = alpha*e^{2tau}, x_su2 = alpha*e^{-2tau}, x_C2 = alpha*e^{tau}.
    Volume-preserving: x_u1^1 * x_su2^3 * x_C2^4 = alpha^8.

    This formula verified against independent Riemann tensor computation
    (S20a: 147/147 components). Agreement to machine epsilon.

    R(0) = 2.0 exactly (bi-invariant metric is Einstein with Ric = R/8 * g).
    """
    return -0.25 * np.exp(-4*tau) + 2.0 * np.exp(-tau) - 0.25 + 0.5 * np.exp(2*tau)


def dR_dtau(tau):
    """Exact derivative dR/dtau."""
    return 1.0 * np.exp(-4*tau) - 2.0 * np.exp(-tau) + 1.0 * np.exp(2*tau)


# ==============================================================================
#  SECTION 2: Seeley-DeWitt a_2 Coefficient (Gilkey Formula)
# ==============================================================================

def a2_gilkey(tau):
    """
    Seeley-DeWitt a_2(D_K^2) for the spin-Dirac operator on (SU(3), g_Jensen(tau)).

    a_2^{SD} = (4*pi)^{-d/2} * int_K tr_S(R/6 - E) dvol

    For d=8, Lichnerowicz D^2 (E = -R/4), on homogeneous space:
      a_2^{SD} = (4*pi)^{-4} * (20*R/3) * Vol                         Eq(1)

    Derivation:
      tr_S(R/6 - E) = tr_S(R/6 + R/4) = 16 * (5R/12) = 20R/3
      (since E = -R/4 for D^2 = -(nabla^2 + E) convention,
       and R/6 - (-R/4) = R/6 + R/4 = 5R/12)
    """
    R = R_scalar(tau)
    Vol = Vol_SU3_Haar
    return (4*PI)**(-4) * (20.0 * R / 3.0) * Vol


def a2_unnormalized(tau):
    """
    The unnormalized a_2 integral (without (4pi)^{-d/2} prefactor).

    a_2^{unnorm} = (20R/3) * Vol                                       Eq(3b)

    This is the object that enters the M_Pl extraction formula directly.
    """
    R = R_scalar(tau)
    return (20.0 * R / 3.0) * Vol_SU3_Haar


def a0_gilkey(tau):
    """
    Seeley-DeWitt a_0(D_K^2) = (4pi)^{-d/2} * rank(S) * Vol.

    For d=8: a_0 = (4pi)^{-4} * 16 * Vol_SU3_Haar.
    Independent of tau (volume-preserving Jensen deformation).
    """
    return (4*PI)**(-4) * 16.0 * Vol_SU3_Haar


# ==============================================================================
#  SECTION 3: CCM Dictionary — M_Pl, G_N, H_0
# ==============================================================================

def extract_M_Pl_squared(tau, M_KK_val):
    """
    Reduced Planck mass squared from CCM spectral action on M^4 x K.

    The spectral action on M^4 x K gives the 4D Einstein-Hilbert term:
      S_EH = (f_2/(4*pi^2)) * M_KK^2 * int_K tr_S(R/6 - E) dvol * int_{M4} R_4 dvol_4

    Identifying with (1/(16*pi*G_N)) * int R_4 dvol_4:
      M_Pl_red^2 = 1/(8*pi*G_N)
                  = (f_2/(4*pi^2)) * M_KK^2 * (20*R/3) * Vol          Eq(2-3)

    With f_2 = 1 (canonical Chamseddine-Connes normalization):
      M_Pl_red^2 = M_KK^2 * a_2^{unnorm} / (4*pi^2)                   Eq(3)
                  = M_KK^2 * 16*pi^2 * a_2^{SD}                        Eq(5)

    Returns M_Pl_red^2 in GeV^2.
    """
    a2_un = a2_unnormalized(tau)
    return M_KK_val**2 * a2_un / (4.0 * PI**2)


def extract_H0(tau, M_KK_val):
    """
    Extract H_0 from the geometric a_2 and observed Lambda.

    Lambda_obs = 3 * H_0^2 / c^2 (cosmological constant as curvature)
    H_0^2 = Lambda_obs * c^2 / 3

    But we need to convert: the spectral action gives G_N, not H_0 directly.
    H_0 depends on BOTH G_N and the energy content of the universe.

    Friedmann: H_0^2 = (8*pi*G_N/3) * rho_total

    With rho_total = rho_Lambda (late universe dominated by dark energy):
      H_0^2 = (8*pi*G_N/3) * rho_Lambda

    And G_N = 1/(8*pi*M_Pl_red^2):
      H_0^2 = (1/(3*M_Pl_red^2)) * rho_Lambda

    rho_Lambda_obs = 2.7e-47 GeV^4.

    Returns H_0 in GeV.
    """
    M_Pl_sq = extract_M_Pl_squared(tau, M_KK_val)
    H0_sq = rho_Lambda_obs / (3.0 * M_Pl_sq)  # GeV^2, wait units?
    # Friedmann: H^2 = (8*pi*G/3)*rho = (8*pi/(3*M_Pl_unred^2))*rho
    # = (1/(3*M_Pl_red^2)) * rho
    # (since M_Pl_unred^2 = 8*pi * M_Pl_red^2, and 8*pi*G = 1/M_Pl_red^2)
    # H^2 = rho / (3*M_Pl_red^2)
    # Check: H_0^2 = 2.7e-47 / (3 * (2.435e18)^2) = 2.7e-47 / (1.78e37) = 1.52e-84 GeV^2
    # H_0 = 1.23e-42 GeV. Known H_0 = 1.438e-42 GeV. Close (within factor from Omega_m).

    if H0_sq < 0:
        return np.nan
    return np.sqrt(H0_sq)


def H0_to_km_s_Mpc(H0_GeV):
    """Convert H_0 from GeV to km/s/Mpc."""
    # H_0 [GeV] * (hbar_c [GeV*m]) -> dimensionless rate
    # H_0 [1/s] = H_0 [GeV] / hbar [GeV*s]
    hbar_GeV_s = 6.582119569e-25  # GeV*s
    H0_per_s = H0_GeV / hbar_GeV_s  # s^{-1}
    # Convert to km/s/Mpc: H_0 [km/s/Mpc] = H_0 [1/s] * Mpc_in_km
    Mpc_in_km = 3.0857e19  # km per Mpc  # (local)
    return H0_per_s * Mpc_in_km


# ==============================================================================
#  SECTION 4: Computation
# ==============================================================================

print("=" * 72)
print("HEAT-KERNEL-A2-61: Seeley-DeWitt a_2 from Local Curvature Integral")
print("=" * 72)

# --- Step 4a: Cross-check R(0) ---
R0 = R_scalar(0.0)
print(f"\nCross-check: R(0) = {R0:.10f}")
print(f"  Expected: 2.0 (Einstein metric)")
assert abs(R0 - 2.0) < 1e-14, f"R(0) = {R0}, expected 2.0"
print(f"  PASSED: R(0) = 2.0 to machine epsilon")

# --- Step 4b: Cross-check a_2^{SD} at fold against S46 ---
a2_fold_SD = a2_gilkey(tau_fold)
a2_fold_unnorm = a2_unnormalized(tau_fold)
R_fold = R_scalar(tau_fold)

print(f"\nAt tau_fold = {tau_fold}:")
print(f"  R(tau_fold) = {R_fold:.12f}")
print(f"  a_2^{{SD}}(tau_fold) = {a2_fold_SD:.12f}")
print(f"  a_2^{{unnorm}}(tau_fold) = {a2_fold_unnorm:.6f}")
print(f"  (20R/3) = {20*R_fold/3:.6f}")
print(f"  Vol_SU3_Haar = {Vol_SU3_Haar:.6f}")
print(f"  (4*pi)^4 = {(4*PI)**4:.6f}")

# S46 reference values
print(f"\n  S46 reference: a2_SD = 0.728235, R(0.19) = 2.018144")
print(f"  This script:   a2_SD = {a2_fold_SD:.6f}, R(0.19) = {R_fold:.6f}")
a2_s46 = 0.7282349726088738  # (local)
R_s46 = 2.018143955851359  # (local)
assert abs(a2_fold_SD - a2_s46) < 1e-10, f"a2_SD mismatch: {a2_fold_SD} vs S46 {a2_s46}"
assert abs(R_fold - R_s46) < 1e-10, f"R mismatch: {R_fold} vs S46 {R_s46}"
print(f"  PASSED: exact agreement with S46 to 10 significant digits")

# --- Step 4c: Cross-check a_0^{SD} ---
a0_SD = a0_gilkey(0.0)
print(f"\n  a_0^{{SD}} = {a0_SD:.12f}")
print(f"  = (4pi)^{{-4}} * 16 * Vol = {(4*PI)**(-4) * 16 * Vol_SU3_Haar:.12f}")
print(f"  Ratio a2_SD/a0_SD = {a2_fold_SD/a0_SD:.6f}")
print(f"  Expected: (5R/12)/1 = {5*R_fold/12:.6f}")
assert abs(a2_fold_SD/a0_SD - 5*R_fold/12) < 1e-10

# --- Step 4d: Comparison with spectral zeta sum (S42/S60) ---
print(f"\n  Spectral zeta sum a_2(spectral, S42) = {a2_fold:.6f}")
print(f"  Geometric a_2^{{SD}} = {a2_fold_SD:.12f}")
print(f"  Ratio (spectral/geometric) = {a2_fold/a2_fold_SD:.2f}")
print(f"  This confirms the S46 finding: factor = 3812 (different objects)")

# ==============================================================================
#  SECTION 5: tau Sweep — a_2^{SD}(tau) over [0, 0.5]
# ==============================================================================

print(f"\n{'='*72}")
print("SECTION 5: tau sweep [0, 0.5], N=100")
print("=" * 72)

N_tau = 100  # (local)
tau_arr = np.linspace(0, 0.5, N_tau)

R_arr = np.array([R_scalar(t) for t in tau_arr])
a2_SD_arr = np.array([a2_gilkey(t) for t in tau_arr])
a2_unnorm_arr = np.array([a2_unnormalized(t) for t in tau_arr])
a0_SD_val = a0_gilkey(0.0)  # constant (volume-preserving)

print(f"  a_0^{{SD}} = {a0_SD_val:.12f} (constant, volume-preserving)")

# M_Pl extraction at each tau (gravity route)
M_Pl_sq_arr_grav = np.array([extract_M_Pl_squared(t, M_KK_gravity) for t in tau_arr])
M_Pl_arr_grav = np.sqrt(M_Pl_sq_arr_grav)

# H_0 extraction at each tau
H0_GeV_arr_grav = np.array([extract_H0(t, M_KK_gravity) for t in tau_arr])
H0_km_s_Mpc_arr_grav = np.array([H0_to_km_s_Mpc(h) if not np.isnan(h) else np.nan
                                   for h in H0_GeV_arr_grav])

# Same with Kerner route
M_Pl_sq_arr_kern = np.array([extract_M_Pl_squared(t, M_KK_kerner) for t in tau_arr])
M_Pl_arr_kern = np.sqrt(M_Pl_sq_arr_kern)
H0_GeV_arr_kern = np.array([extract_H0(t, M_KK_kerner) for t in tau_arr])
H0_km_s_Mpc_arr_kern = np.array([H0_to_km_s_Mpc(h) if not np.isnan(h) else np.nan
                                   for h in H0_GeV_arr_kern])

# Fold values
idx_fold = np.argmin(np.abs(tau_arr - tau_fold))

print(f"\n  At tau_fold = {tau_arr[idx_fold]:.4f}:")
print(f"    R = {R_arr[idx_fold]:.10f}")
print(f"    a_2^{{SD}} = {a2_SD_arr[idx_fold]:.12f}")
print(f"    a_2^{{unnorm}} = {a2_unnorm_arr[idx_fold]:.6f}")

print(f"\n  Gravity route (M_KK = {M_KK_gravity:.4e} GeV):")
print(f"    M_Pl_red = {M_Pl_arr_grav[idx_fold]:.6e} GeV")
print(f"    M_Pl_red(obs) = {M_Pl_reduced:.6e} GeV")
print(f"    Ratio = {M_Pl_arr_grav[idx_fold]/M_Pl_reduced:.6f}")
print(f"    H_0 = {H0_km_s_Mpc_arr_grav[idx_fold]:.4f} km/s/Mpc")

print(f"\n  Kerner route (M_KK = {M_KK_kerner:.4e} GeV):")
print(f"    M_Pl_red = {M_Pl_arr_kern[idx_fold]:.6e} GeV")
print(f"    Ratio = {M_Pl_arr_kern[idx_fold]/M_Pl_reduced:.6f}")
print(f"    H_0 = {H0_km_s_Mpc_arr_kern[idx_fold]:.4f} km/s/Mpc")

# ==============================================================================
#  SECTION 6: Cross-check — H_0 from observed M_Pl
# ==============================================================================

print(f"\n{'='*72}")
print("SECTION 6: Cross-check — H_0 from observed M_Pl")
print("=" * 72)

# H_0 = sqrt(rho_Lambda / (3 * M_Pl_red^2))
H0_obs_GeV = np.sqrt(rho_Lambda_obs / (3.0 * M_Pl_reduced**2))
H0_obs_km = H0_to_km_s_Mpc(H0_obs_GeV)
print(f"  rho_Lambda = {rho_Lambda_obs:.2e} GeV^4")
print(f"  M_Pl_red = {M_Pl_reduced:.4e} GeV")
print(f"  H_0(Lambda-only) = {H0_obs_GeV:.6e} GeV = {H0_obs_km:.2f} km/s/Mpc")
print(f"  H_0(Planck 2018) = {H_0_km_s_Mpc} km/s/Mpc")
print(f"  Ratio H_0(Lambda-only)/H_0(Planck) = {H0_obs_km/H_0_km_s_Mpc:.4f}")
print(f"\n  NOTE: H_0(Lambda-only) < H_0(obs) because Omega_Lambda ~ 0.685, not 1.0")
print(f"  Correcting for Omega_Lambda: H_0 = H_0(Lambda-only)/sqrt(Omega_Lambda)")
H0_corrected_obs = H0_obs_km / np.sqrt(0.685)
print(f"  H_0(corrected) = {H0_corrected_obs:.2f} km/s/Mpc")

# ==============================================================================
#  SECTION 7: Self-consistency and Eigenvalue Bounds
# ==============================================================================

print(f"\n{'='*72}")
print("SECTION 7: Self-consistency checks")
print("=" * 72)

# Check 1: a_2/a_0 = 5R/12 at all tau
print(f"\n  Check 1: a_2^{{SD}}/a_0^{{SD}} = 5R/12")
ratio_check = a2_SD_arr / a0_SD_val
expected_ratio = 5.0 * R_arr / 12.0
max_err = np.max(np.abs(ratio_check - expected_ratio))
print(f"  Max error over all tau: {max_err:.2e}")
assert max_err < 1e-14, f"Ratio check failed: max_err = {max_err}"
print(f"  PASSED")

# Check 2: R(tau) monotonic for tau > 0
dR = np.diff(R_arr)
is_mono = np.all(dR > 0)
print(f"\n  Check 2: R(tau) monotonically increasing for tau > 0")
print(f"  dR/dtau at tau=0: {dR[0]/np.diff(tau_arr)[0]:.6f}")
print(f"  Expected: dR/dtau(0) = 1 - 2 + 1 = 0 (critical point)")
dR_exact_0 = dR_dtau(0.0)
print(f"  Exact dR/dtau(0) = {dR_exact_0:.10f}")
# R'(0) = 1*e^0 - 2*e^0 + 1*e^0 = 0 (flat at bi-invariant)
# R''(0) = -4 + 2 + 2 = 0 ... let me compute
# R'(tau) = e^{-4tau} - 2*e^{-tau} + e^{2tau}
# R''(tau) = -4*e^{-4tau} + 2*e^{-tau} + 2*e^{2tau}
# R''(0) = -4 + 2 + 2 = 0
# R'''(tau) = 16*e^{-4tau} - 2*e^{-tau} + 4*e^{2tau}
# R'''(0) = 16 - 2 + 4 = 18 > 0
# So R has an inflection point at tau=0, but increases for tau > 0
tau_test = tau_arr[1:]  # skip tau=0
R_test = R_arr[1:]
dR_test = np.diff(R_test)
is_mono_post0 = np.all(dR_test > 0)
print(f"  Monotonic for tau > {tau_arr[1]:.4f}: {is_mono_post0}")

# Check 3: Lichnerowicz bound
print(f"\n  Check 3: Lichnerowicz bound lambda_1^2 >= R/4")
# Minimum eigenvalue at fold from data
lambda_1_fold = 0.8197411120665079  # from S46 data  # (local)
R_lich = R_arr[idx_fold]
bound = R_lich / 4.0
print(f"  lambda_1^2 = {lambda_1_fold**2:.6f}")
print(f"  R/4 = {bound:.6f}")
print(f"  lambda_1^2 / (R/4) = {lambda_1_fold**2 / bound:.4f}")
print(f"  {'SATISFIED' if lambda_1_fold**2 >= bound else 'VIOLATED'}")

# ==============================================================================
#  SECTION 8: Comparison with PW Partial Sums (S60)
# ==============================================================================

print(f"\n{'='*72}")
print("SECTION 8: Comparison with PW partial sums (s60_pw_h0_conv.npz)")
print("=" * 72)

try:
    d60 = np.load('s60_pw_h0_conv.npz', allow_pickle=True)
    a2_pw_cumul = d60['a2_cumul']
    L_arr = d60['L_arr']
    a2_needed_s60 = d60['a2_needed'].item()

    print(f"\n  PW spectral sums a_2(L) = sum_{{p+q<=L}} dim^2 * sum |lambda|:")
    for i, L in enumerate(L_arr):
        print(f"    L={L}: a_2(PW) = {a2_pw_cumul[i]:.2f}")

    print(f"\n  Geometric a_2^{{SD}} = {a2_fold_SD:.6f}")
    print(f"  Geometric a_2^{{unnorm}} = {a2_fold_unnorm:.2f}")
    print(f"  a_2_needed (for M_Pl match with spectral formula) = {a2_needed_s60:.2f}")

    # The PW sum diverges; the geometric a_2 is finite
    print(f"\n  Key ratios:")
    print(f"    a_2^{{unnorm}} / a_2_needed = {a2_fold_unnorm / a2_needed_s60:.4f}")
    print(f"    This ratio tells us: does the geometric a_2 match what's needed for M_Pl?")

    # The S60 formula: M_Pl_red^2 = a_2(needed) * M_KK^2 / pi^2
    # Our formula: M_Pl_red^2 = a_2^{unnorm} * M_KK^2 / (4*pi^2)
    # So our "a_2_needed" would be a_2^{unnorm} = (20R/3)*Vol, and the S60 formula uses
    # a different normalization: a_2(S60) = a_2^{unnorm} / 4? No...
    #
    # S60: M_Pl_red^2 = a_2(S60) * M_KK^2 / pi^2
    # Us:  M_Pl_red^2 = a_2^{unnorm} * M_KK^2 / (4*pi^2)
    # So: a_2(S60)_needed / a_2^{unnorm}_needed = 1/4 * (pi^2)/(pi^2) Hmm no.
    #
    # S60: a_2_needed = M_Pl_red^2 * pi^2 / M_KK^2 = 10604
    # Us: a_2^{unnorm} = M_Pl_red^2 * 4*pi^2 / M_KK^2 = 4 * 10604 = 42416
    # But a_2^{unnorm}(fold) = 18160
    # So M_Pl_red(geom) = M_Pl_red(obs) * sqrt(18160/42416) = M_Pl_red * 0.654

    a2_needed_geom = M_Pl_reduced**2 * 4.0 * PI**2 / M_KK_gravity**2
    print(f"\n  For our formula: a_2^{{unnorm}}_needed = 4*pi^2 * M_Pl_red^2 / M_KK^2 = {a2_needed_geom:.2f}")
    print(f"  a_2^{{unnorm}}(fold) = {a2_fold_unnorm:.2f}")
    print(f"  Ratio a_2^{{unnorm}}(fold) / a_2_needed = {a2_fold_unnorm / a2_needed_geom:.6f}")
    print(f"  sqrt(ratio) = M_Pl_geom / M_Pl_obs = {np.sqrt(a2_fold_unnorm / a2_needed_geom):.6f}")

except FileNotFoundError:
    print("  s60_pw_h0_conv.npz not found — skipping PW comparison")

# ==============================================================================
#  SECTION 9: GATE VERDICT
# ==============================================================================

print(f"\n{'='*72}")
print("SECTION 9: GATE VERDICT — HEAT-KERNEL-A2-61")
print("=" * 72)

# Key results at fold
H0_fold_grav = H0_km_s_Mpc_arr_grav[idx_fold]
H0_fold_kern = H0_km_s_Mpc_arr_kern[idx_fold]
M_Pl_fold_grav = M_Pl_arr_grav[idx_fold]
M_Pl_fold_kern = M_Pl_arr_kern[idx_fold]

print(f"\n  COMPUTED QUANTITIES:")
print(f"    R(fold) = {R_fold:.10f}")
print(f"    a_2^{{SD}}(fold) = {a2_fold_SD:.12f}")
print(f"    a_2^{{unnorm}}(fold) = {a2_fold_unnorm:.6f}")
print(f"    Vol_SU3_Haar = {Vol_SU3_Haar:.6f}")
print(f"    a_0^{{SD}} = {a0_SD_val:.12f}")
print(f"")
print(f"  GRAVITY ROUTE (M_KK = {M_KK_gravity:.4e} GeV):")
print(f"    M_Pl_red(geom) = {M_Pl_fold_grav:.6e} GeV")
print(f"    M_Pl_red(obs)  = {M_Pl_reduced:.6e} GeV")
print(f"    Ratio = {M_Pl_fold_grav/M_Pl_reduced:.6f}")
print(f"    H_0(Lambda-only) = {H0_fold_grav:.4f} km/s/Mpc")
print(f"")
print(f"  KERNER ROUTE (M_KK = {M_KK_kerner:.4e} GeV):")
print(f"    M_Pl_red(geom) = {M_Pl_fold_kern:.6e} GeV")
print(f"    Ratio = {M_Pl_fold_kern/M_Pl_reduced:.6f}")
print(f"    H_0(Lambda-only) = {H0_fold_kern:.4f} km/s/Mpc")

# Correct for Omega_Lambda (H_0 computed assuming Lambda dominates;
# true H_0 = H(Lambda-only) / sqrt(Omega_Lambda))
Omega_Lam = Omega_Lambda  # 0.685 from canonical_constants
H0_fold_grav_full = H0_fold_grav / np.sqrt(Omega_Lam)
H0_fold_kern_full = H0_fold_kern / np.sqrt(Omega_Lam)

print(f"\n  CORRECTED FOR Omega_Lambda = {Omega_Lam}:")
print(f"    H_0(grav, full) = {H0_fold_grav_full:.4f} km/s/Mpc")
print(f"    H_0(kern, full) = {H0_fold_kern_full:.4f} km/s/Mpc")

# Gate verdict
print(f"\n  PRE-REGISTERED GATE: HEAT-KERNEL-A2-61")
print(f"    Criterion: PASS if a_2(tau_fold) finite AND H_0 in [60,80]")
print(f"               FAIL if H_0 outside [40,100] or divergent")
print(f"               INFO if H_0 well-defined but outside [60,80]")

a2_is_finite = np.isfinite(a2_fold_SD) and a2_fold_SD > 0

# Use the gravity route as primary (Kerner as cross-check)
H0_primary = H0_fold_grav_full  # corrected for Omega_Lambda
H0_raw = H0_fold_grav  # uncorrected (Lambda-only Friedmann)

if not a2_is_finite:
    verdict = "FAIL"
    detail = f"a_2^{{SD}} = {a2_fold_SD} is not finite positive"
elif 60 <= H0_primary <= 80:
    verdict = "PASS"
    detail = (f"a_2^{{SD}} = {a2_fold_SD:.6f} (finite). "
              f"H_0(grav,Omega_L-corrected) = {H0_primary:.2f} km/s/Mpc in [60,80].")
elif 40 <= H0_primary <= 100:
    verdict = "INFO"
    detail = (f"a_2^{{SD}} = {a2_fold_SD:.6f} (finite). "
              f"H_0(grav,Omega_L-corrected) = {H0_primary:.2f} km/s/Mpc in [40,100] but outside [60,80].")
else:
    verdict = "FAIL"
    detail = (f"a_2^{{SD}} = {a2_fold_SD:.6f} (finite). "
              f"H_0(grav,Omega_L-corrected) = {H0_primary:.2f} km/s/Mpc outside [40,100].")

print(f"\n  VERDICT: {verdict}")
print(f"  DETAIL: {detail}")

# ==============================================================================
#  SECTION 10: Save Data
# ==============================================================================

print(f"\n{'='*72}")
print("SECTION 10: Saving data")
print("=" * 72)

np.savez('s61_heat_kernel_a2.npz',
    # tau grid
    tau_arr=tau_arr,
    tau_fold=tau_fold,
    idx_fold=idx_fold,
    N_tau=N_tau,
    # Geometric quantities
    R_arr=R_arr,
    R_fold=R_fold,
    a2_SD_arr=a2_SD_arr,
    a2_unnorm_arr=a2_unnorm_arr,
    a0_SD=a0_SD_val,
    a2_SD_fold=a2_fold_SD,
    a2_unnorm_fold=a2_fold_unnorm,
    Vol_SU3_Haar=Vol_SU3_Haar,
    # M_Pl extraction (gravity route)
    M_Pl_sq_arr_grav=M_Pl_sq_arr_grav,
    M_Pl_arr_grav=M_Pl_arr_grav,
    M_Pl_fold_grav=M_Pl_fold_grav,
    # M_Pl extraction (Kerner route)
    M_Pl_sq_arr_kern=M_Pl_sq_arr_kern,
    M_Pl_arr_kern=M_Pl_arr_kern,
    M_Pl_fold_kern=M_Pl_fold_kern,
    # H_0 extraction
    H0_GeV_arr_grav=H0_GeV_arr_grav,
    H0_km_s_Mpc_arr_grav=H0_km_s_Mpc_arr_grav,
    H0_GeV_arr_kern=H0_GeV_arr_kern,
    H0_km_s_Mpc_arr_kern=H0_km_s_Mpc_arr_kern,
    H0_fold_grav_raw=H0_fold_grav,
    H0_fold_grav_corrected=H0_fold_grav_full,
    H0_fold_kern_raw=H0_fold_kern,
    H0_fold_kern_corrected=H0_fold_kern_full,
    # Reference values
    M_KK_gravity=M_KK_gravity,
    M_KK_kerner=M_KK_kerner,
    M_Pl_reduced_obs=M_Pl_reduced,
    rho_Lambda_obs=rho_Lambda_obs,
    # Spectral sums for comparison
    a2_spectral_fold=a2_fold,
    ratio_spectral_over_SD=a2_fold / a2_fold_SD,
    # Gate
    gate_name=np.array(['HEAT-KERNEL-A2-61']),
    gate_verdict=np.array([verdict]),
    gate_detail=np.array([detail]),
)

print(f"  Saved: s61_heat_kernel_a2.npz")
print(f"  Keys: tau_arr, R_arr, a2_SD_arr, a2_unnorm_arr, M_Pl_arr_grav, H0_km_s_Mpc_arr_grav, ...")

# ==============================================================================
#  SECTION 11: Plots
# ==============================================================================

print(f"\n{'='*72}")
print("SECTION 11: Plotting")
print("=" * 72)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel 1: R(tau) and a_2^{SD}(tau)
ax1 = axes[0, 0]
color1 = 'C0'
ax1.plot(tau_arr, R_arr, color=color1, lw=2, label='R(tau)')
ax1.axvline(tau_fold, color='gray', ls='--', alpha=0.5, label=f'tau_fold = {tau_fold}')
ax1.set_xlabel('tau')
ax1.set_ylabel('Scalar curvature R(tau)', color=color1)
ax1.tick_params(axis='y', labelcolor=color1)
ax1.set_title('Scalar Curvature and Seeley-DeWitt a_2')
ax1_twin = ax1.twinx()
color2 = 'C1'
ax1_twin.plot(tau_arr, a2_SD_arr, color=color2, lw=2, ls='--', label='a_2^{SD}(tau)')
ax1_twin.set_ylabel('a_2^{SD}(tau)', color=color2)
ax1_twin.tick_params(axis='y', labelcolor=color2)
lines1 = ax1.get_lines() + ax1_twin.get_lines()
labels1 = [l.get_label() for l in lines1]
ax1.legend(lines1, labels1, loc='upper left', fontsize=9)

# Panel 2: M_Pl(tau) both routes
ax2 = axes[0, 1]
ax2.plot(tau_arr, M_Pl_arr_grav / 1e18, 'C0-', lw=2, label='Gravity route')
ax2.plot(tau_arr, M_Pl_arr_kern / 1e18, 'C2-', lw=2, label='Kerner route')
ax2.axhline(M_Pl_reduced / 1e18, color='red', ls=':', lw=1.5, label=f'M_Pl(obs) = {M_Pl_reduced/1e18:.3f}')
ax2.axvline(tau_fold, color='gray', ls='--', alpha=0.5)
ax2.set_xlabel('tau')
ax2.set_ylabel('M_Pl_red [10^18 GeV]')
ax2.set_title('Reduced Planck Mass from Geometric a_2')
ax2.legend(fontsize=9)

# Panel 3: H_0(tau) both routes
ax3 = axes[1, 0]
H0_grav_full_arr = H0_km_s_Mpc_arr_grav / np.sqrt(Omega_Lam)
H0_kern_full_arr = H0_km_s_Mpc_arr_kern / np.sqrt(Omega_Lam)
ax3.plot(tau_arr, H0_grav_full_arr, 'C0-', lw=2, label='Gravity route')
ax3.plot(tau_arr, H0_kern_full_arr, 'C2-', lw=2, label='Kerner route')
ax3.axhline(H_0_km_s_Mpc, color='red', ls=':', lw=1.5, label=f'H_0(Planck) = {H_0_km_s_Mpc}')
ax3.axhspan(60, 80, alpha=0.1, color='green', label='PASS band [60,80]')
ax3.axvline(tau_fold, color='gray', ls='--', alpha=0.5)
ax3.set_xlabel('tau')
ax3.set_ylabel('H_0 [km/s/Mpc]')
ax3.set_title('H_0 from Geometric a_2 (corrected for Omega_L)')
ax3.set_ylim(0, max(200, np.nanmax(H0_grav_full_arr[np.isfinite(H0_grav_full_arr)])*1.1))
ax3.legend(fontsize=8, loc='upper right')

# Panel 4: Ratio M_Pl(geom)/M_Pl(obs) and summary text
ax4 = axes[1, 1]
ratio_grav = M_Pl_arr_grav / M_Pl_reduced
ratio_kern = M_Pl_arr_kern / M_Pl_reduced
ax4.plot(tau_arr, ratio_grav, 'C0-', lw=2, label='Gravity route')
ax4.plot(tau_arr, ratio_kern, 'C2-', lw=2, label='Kerner route')
ax4.axhline(1.0, color='red', ls=':', lw=1.5, label='Unity (exact match)')
ax4.axvline(tau_fold, color='gray', ls='--', alpha=0.5)
ax4.set_xlabel('tau')
ax4.set_ylabel('M_Pl(geom) / M_Pl(obs)')
ax4.set_title('Planck Mass Ratio')
ax4.legend(fontsize=9)

# Summary text box
summary_text = (
    f"GATE: HEAT-KERNEL-A2-61 — {verdict}\n"
    f"R(fold) = {R_fold:.6f}\n"
    f"a_2^{{SD}}(fold) = {a2_fold_SD:.6f}\n"
    f"a_2^{{unnorm}}(fold) = {a2_fold_unnorm:.1f}\n"
    f"M_Pl(grav)/M_Pl(obs) = {M_Pl_fold_grav/M_Pl_reduced:.4f}\n"
    f"M_Pl(kern)/M_Pl(obs) = {M_Pl_fold_kern/M_Pl_reduced:.4f}\n"
    f"H_0(grav) = {H0_fold_grav_full:.1f} km/s/Mpc\n"
    f"H_0(kern) = {H0_fold_kern_full:.1f} km/s/Mpc"
)
ax4.text(0.98, 0.02, summary_text, transform=ax4.transAxes,
         fontsize=8, verticalalignment='bottom', horizontalalignment='right',
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8),
         family='monospace')

plt.tight_layout()
plt.savefig('s61_heat_kernel_a2.png', dpi=150, bbox_inches='tight')
print(f"  Saved: s61_heat_kernel_a2.png")

print(f"\n{'='*72}")
print(f"  FINAL: HEAT-KERNEL-A2-61 VERDICT = {verdict}")
print(f"  {detail}")
print(f"{'='*72}")
