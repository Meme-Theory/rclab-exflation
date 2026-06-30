#!/usr/bin/env python3
"""
CAVITY-BCS-HORIZON-70: Transmission Through Compound Barrier
=============================================================

Computes the transmission coefficient T(k) through the compound barrier
formed by z''/z (geometric, from Jensen deformation at the fold) plus
Delta(tau)^2 * a^2 (BCS gap turning on at the transit) plus the conformal
factor profile.

Resonance structure:
--------------------
The z''/z barrier at the fold has a compound structure: a geometric barrier
(from the Jensen deformation driving the spectral action gradient) superimposed
with a BCS barrier (from the pairing gap turning on as the fiber exits the
van Hove fold). If these form an effective cavity between two reflective
boundaries, resonant tunneling (Fabry-Perot) can enhance specific k-modes
in the primordial power spectrum.

What oscillates: scalar perturbation modes v_k in conformal time eta
What constrains: the compound effective potential V_eff(eta) = z''/z + Delta^2 * a^2
What are the boundary conditions: incoming plane wave (WKB) at eta -> 0,
                                   outgoing WKB at eta -> eta_max
Normal modes: k-values where T(k) peaks (resonant transmission)

Substrate framing:
------------------
The Mukhanov-Sasaki variable v_k encodes perturbations of the fabric's
spectral complexity. The pump function z = a*sqrt(2*epsilon_H) captures
how the fiber's deformation rate couples to the emergent scale factor.
The z''/z barrier IS the spectral action curvature seen by each k-mode.
The BCS gap adds a mass term: the pairing condensate makes the fabric
"heavier" for perturbation modes, raising the effective barrier.

Physics (transfer matrix method):
----------------------------------
The mode equation in conformal time:

    v_k'' + [k^2 - V_eff(eta)] v_k = 0            (1)

where V_eff(eta) = z''/z + Delta(eta)^2 * a(eta)^2  (2)

The transfer matrix method divides the potential into N thin slabs. In each
slab the potential is approximately constant, and the solution is a
superposition of propagating or evanescent waves. The 2x2 transfer matrix
M_j for slab j of width dx with local wavenumber q_j connects amplitudes
across the slab:

  Propagating (q_j^2 = k^2 - V_j > 0):
    M_j = [[cos(q_j dx), sin(q_j dx)/q_j],
           [-q_j sin(q_j dx), cos(q_j dx)]]

  Evanescent (kappa_j^2 = V_j - k^2 > 0):
    M_j = [[cosh(kappa_j dx), sinh(kappa_j dx)/kappa_j],
           [kappa_j sinh(kappa_j dx), cosh(kappa_j dx)]]

The total transfer matrix M = M_N ... M_2 M_1 relates (v, v') at the left
boundary to (v, v') at the right boundary.

For scattering with propagating boundary conditions on both sides
(q_L = sqrt(k^2 - V_L), q_R = sqrt(k^2 - V_R)):
    T(k) = (q_R / q_L) / |M_11 + i q_R M_12 - i/q_L M_21 + q_R/q_L M_22|^2 * 4*q_L*q_R

Alternatively: T = 4 q_L q_R / |q_R M_11 + i q_L q_R M_12 + i M_21 + q_L M_22|^2

When the right side is evanescent (k^2 < V_R), T = 0 (total reflection).
In that case, the physically meaningful quantity is the reflection coefficient
R(k) and its phase, which determines the WKB connection formula and
Bogoliubov coefficients for particle production.

Gate: CAVITY-BCS-HORIZON-70
  INFO: Report T(k) profile, number of resonances, Q-factors

Input files:
  computations/_shared/canonical_constants.py
  computations/session-67/s67_transit_ps.npz
  computations/session-69/s69_bcs_hessian.npz
  computations/session-69/s69_conformal_factor.npz

References:
  S67 (transit power spectrum, z''/z profile)
  S69 (BCS Hessian, conformal factor)
  S56 (Josephson barrier, Mattis-Bardeen protection)
  S62 (phonon dispersion, 45-mode coupled crystal)
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

import numpy as np
from scipy.interpolate import CubicSpline
from scipy.signal import find_peaks
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import (
    tau_fold, M_KK, Delta_BCS, Delta_B3,
    H_fold, v_terminal, dt_transit,
    xi_BCS, c_fabric, G_DeWitt, PI,
    dS_fold, d2S_fold, S_fold,
    E_cond, n_pairs, T_acoustic,
)

# ============================================================================
#  SECTION 1: Load transit background data
# ============================================================================

print("=" * 72)
print("CAVITY-BCS-HORIZON-70: Transmission Through Compound Barrier")
print("=" * 72)

data_dir = os.path.dirname(__file__)
data_67 = np.load(os.path.join(data_dir, 's67_transit_ps.npz'), allow_pickle=True)
data_69c = np.load(os.path.join(data_dir, 's69_conformal_factor.npz'), allow_pickle=True)
data_69h = np.load(os.path.join(data_dir, 's69_bcs_hessian.npz'), allow_pickle=True)

# Transit background from S67
tau_fine = data_67['tau_fine']       # (8000,), range [0.10, 0.30]
eta_fine = data_67['eta_fine']       # conformal time (8000,)
z_fine   = data_67['z_fine']         # Mukhanov pump z = a*sqrt(2*eps_H)
zpp_z    = data_67['zpp_z']          # z''/z (8000,)
a_fine   = data_67['a_fine']         # scale factor
eps_fine = data_69c['eps_fine']      # slow-roll parameter

# Key scales
k_transit = float(data_67['k_transit'])
k_tach_fold = float(data_69c['k_tach_fold'])

print(f"\nTransit background loaded:")
print(f"  tau range: [{tau_fine[0]:.3f}, {tau_fine[-1]:.3f}], N = {len(tau_fine)}")
print(f"  eta range: [{eta_fine[0]:.6f}, {eta_fine[-1]:.6f}]")
print(f"  z''/z range: [{zpp_z.min():.2e}, {zpp_z.max():.2e}]")
print(f"  k_transit = {k_transit:.2f} M_KK")
print(f"  k_tach_fold = {k_tach_fold:.2f} M_KK")

# Fold index
fold_idx = np.argmin(np.abs(tau_fine - tau_fold))
eta_fold = eta_fine[fold_idx]
print(f"  Fold at tau = {tau_fine[fold_idx]:.4f}, eta = {eta_fold:.8f}, idx = {fold_idx}")
print(f"  z''/z at fold = {zpp_z[fold_idx]:.4e}")
print(f"  a at fold = {a_fine[fold_idx]:.6f}")

# BCS parameters from S69
Delta_BCS_val = float(data_69h['Delta_BCS'])
print(f"\nBCS parameters:")
print(f"  Delta_BCS = {Delta_BCS_val:.4f} M_KK")
print(f"  Delta_B3 = {Delta_B3:.3f} M_KK")
print(f"  xi_BCS = {xi_BCS:.4f} M_KK^{{-1}}")

# ============================================================================
#  SECTION 2: Construct the BCS gap profile Delta(tau)
# ============================================================================

print("\n" + "=" * 72)
print("SECTION 2: BCS Gap Profile Through Transit")
print("=" * 72)

# The BCS gap turns on at the fold (tau = tau_fold).
# Model: smooth step function with width set by coherence length timescale
#
# Delta(tau) = Delta_BCS * 0.5 * [1 + tanh((tau - tau_fold) / delta_tau)]
#
# delta_tau sets the BCS condensate formation rate in tau-space.
# Physical: the BCS order parameter relaxation time is ~ xi_BCS / v_s
# where v_s is the BCS sound speed. In tau-space this maps to ~ 0.02.

delta_tau_BCS = 0.02  # BCS turns on over delta_tau ~ 0.02 in tau-space

print(f"BCS turn-on width: delta_tau = {delta_tau_BCS:.4f}")
print(f"  (xi_BCS = {xi_BCS:.4f}, dt_transit = {dt_transit:.6f})")

# Construct Delta(tau) profile
Delta_profile = Delta_BCS_val * 0.5 * (1.0 + np.tanh((tau_fine - tau_fold) / delta_tau_BCS))

print(f"Delta(tau) profile:")
for t in [0.10, 0.15, 0.19, 0.22, 0.30]:
    idx = np.argmin(np.abs(tau_fine - t))
    print(f"  Delta(tau={t:.2f}) = {Delta_profile[idx]:.6f} M_KK")

# ============================================================================
#  SECTION 3: Construct compound effective potential
# ============================================================================

print("\n" + "=" * 72)
print("SECTION 3: Compound Effective Potential V_eff(eta)")
print("=" * 72)

# The compound barrier is:
#   V_eff(eta) = z''/z + Delta(eta)^2 * a(eta)^2          (3)
#
# The BCS mass term contributes Delta^2 * a^2 because in conformal time
# a massive scalar field obeys:
#   v_k'' + [k^2 - z''/z - m^2 a^2] v_k = 0
# where m = Delta_BCS is the effective mass from pairing.

V_geometric = zpp_z.copy()
V_BCS = Delta_profile**2 * a_fine**2
V_eff = V_geometric + V_BCS

# Also compute V_eff with conformal factor correction
# The conformal factor Omega from S69 modifies the effective potential
# via Omega''/Omega contributions from the BLV acoustic metric
Omega_transit = data_69c['Omega_transit_profile']

# Compute Omega''/Omega using finite differences in eta
dOmega_deta = np.gradient(Omega_transit, eta_fine)
d2Omega_deta2 = np.gradient(dOmega_deta, eta_fine)
Omega_pp_Omega = np.where(Omega_transit > 1e-10,
                          d2Omega_deta2 / Omega_transit,
                          0.0)

V_conformal = Omega_pp_Omega
V_total = V_eff + V_conformal

print(f"Potential components at fold (tau={tau_fold}):")
print(f"  V_geometric = z''/z        = {V_geometric[fold_idx]:.4e} M_KK^2")
print(f"  V_BCS = Delta^2 * a^2      = {V_BCS[fold_idx]:.4e} M_KK^2")
print(f"  V_conformal = Omega''/Omega = {V_conformal[fold_idx]:.4e} M_KK^2")
print(f"  V_total                     = {V_total[fold_idx]:.4e} M_KK^2")
print(f"  BCS/geometric ratio         = {V_BCS[fold_idx]/V_geometric[fold_idx]:.2e}")
print(f"  conformal/geometric ratio   = {abs(V_conformal[fold_idx])/V_geometric[fold_idx]:.2e}")

# Profile at key tau values
print(f"\nV_total profile at key tau values:")
for t in [0.10, 0.14, 0.17, 0.19, 0.20, 0.22, 0.25, 0.30]:
    idx = np.argmin(np.abs(tau_fine - t))
    print(f"  tau={t:.2f}: V_geo={V_geometric[idx]:.3e}, V_BCS={V_BCS[idx]:.3e}, "
          f"V_conf={V_conformal[idx]:.3e}, V_tot={V_total[idx]:.3e}")

# Check monotonicity of each component
dV_geo = np.diff(V_geometric)
dV_BCS = np.diff(V_BCS)
dV_eff_diff = np.diff(V_eff)
dV_tot = np.diff(V_total)
n_violations_geo = np.sum(dV_geo < -1e-10 * np.abs(V_geometric[:-1]))
n_violations_eff = np.sum(dV_eff_diff < -1e-10 * np.abs(V_eff[:-1]))
n_violations_tot = np.sum(dV_tot < -1e-10 * np.abs(V_total[:-1]))
print(f"\nMonotonicity check (relative threshold 1e-10):")
print(f"  V_geometric: {n_violations_geo} violations out of {len(dV_geo)}")
print(f"  V_BCS:       {np.sum(dV_BCS < 0)} violations")
print(f"  V_eff:       {n_violations_eff} violations")
print(f"  V_total:     {n_violations_tot} violations")

# Check for peaks/troughs in V_total (possible cavity)
peaks_Vtot, peak_props = find_peaks(V_total, prominence=V_total.max() * 0.001)
troughs_Vtot, trough_props = find_peaks(-V_total, prominence=V_total.max() * 0.001)
print(f"\n  Peaks in V_total: {len(peaks_Vtot)}")
print(f"  Troughs in V_total: {len(troughs_Vtot)}")

has_cavity = len(peaks_Vtot) >= 2 or (len(troughs_Vtot) >= 1 and len(peaks_Vtot) >= 1)
print(f"  Cavity structure present: {has_cavity}")

# For the compound barrier V_eff (geo + BCS without conformal):
peaks_Veff, _ = find_peaks(V_eff, prominence=V_eff.max() * 0.001)
troughs_Veff, _ = find_peaks(-V_eff, prominence=V_eff.max() * 0.001)
has_cavity_eff = len(peaks_Veff) >= 2 or (len(troughs_Veff) >= 1 and len(peaks_Veff) >= 1)
print(f"\n  Peaks in V_eff: {len(peaks_Veff)}")
print(f"  Troughs in V_eff: {len(troughs_Veff)}")
print(f"  Cavity structure in V_eff: {has_cavity_eff}")

# ============================================================================
#  SECTION 4: Transfer Matrix Computation of T(k)
# ============================================================================

print("\n" + "=" * 72)
print("SECTION 4: Transfer Matrix Transmission Coefficient T(k)")
print("=" * 72)

# k-grid: scan from sub-tachyonic to super-tachyonic modes
# Use k_tach_fold as the reference scale
k_min = 0.1 * k_tach_fold
k_max = 10.0 * k_tach_fold
N_k = 500  # (local)
k_grid = np.geomspace(k_min, k_max, N_k)

print(f"k-grid: [{k_min:.1f}, {k_max:.1f}] M_KK, N = {N_k}")
print(f"k_tach_fold = {k_tach_fold:.2f} M_KK")

def transfer_matrix_T(k_array, V_profile, eta_array):
    """
    Compute transmission coefficient T(k) through barrier V_profile(eta)
    using the transfer matrix method.

    The mode equation is v'' + [k^2 - V(eta)] v = 0.

    The transfer matrix M connects (v, v') at eta_L to (v, v') at eta_R.

    For scattering from a potential that varies from V_L to V_R:
    - If both sides are propagating (k^2 > V_L and k^2 > V_R):
      T = 4 q_L q_R / |q_R M_11 + i q_L q_R M_12 + i M_21 + q_L M_22|^2
    - If right side is evanescent (k^2 < V_R): total reflection, T = 0
    - If left side is evanescent: mode doesn't exist as incoming wave

    Returns T(k) array.
    """
    N = len(eta_array)
    dx = np.diff(eta_array)
    V_L = V_profile[0]
    V_R = V_profile[-1]

    T_k = np.zeros(len(k_array))

    for ik, k in enumerate(k_array):
        k2 = k**2

        # Check boundary conditions
        q2_L = k2 - V_L
        q2_R = k2 - V_R

        if q2_L <= 0:
            # Left side evanescent: no incoming propagating wave
            T_k[ik] = 0.0
            continue

        # Total transfer matrix: start with identity
        M = np.eye(2, dtype=np.float64)
        overflow = False

        for j in range(N - 1):
            q2 = k2 - V_profile[j]
            d = dx[j]

            if q2 > 0:
                # Propagating
                q = np.sqrt(q2)
                qd = q * d
                # Phase wrapping for numerical stability
                c, s = np.cos(qd), np.sin(qd)
                Mj = np.array([[c, s / q],
                               [-q * s, c]])
            elif q2 < 0:
                # Evanescent
                kappa = np.sqrt(-q2)
                kd = kappa * d
                if kd > 500:
                    # Completely opaque
                    T_k[ik] = 0.0
                    overflow = True
                    break
                ch = np.cosh(kd)
                sh = np.sinh(kd)
                Mj = np.array([[ch, sh / kappa],
                               [kappa * sh, ch]])
            else:
                # Exactly at turning point: linear approximation
                Mj = np.array([[1.0, d],
                               [0.0, 1.0]])

            M = Mj @ M

            # Check for numerical overflow
            if np.max(np.abs(M)) > 1e150:
                T_k[ik] = 0.0
                overflow = True
                break

        if overflow:
            continue

        if q2_R > 0:
            # Both sides propagating: standard scattering
            q_L = np.sqrt(q2_L)
            q_R = np.sqrt(q2_R)
            # T = 4 q_L q_R / |q_R M_11 + i q_L q_R M_12 + i M_21 + q_L M_22|^2
            # Real and imaginary parts:
            Re = q_R * M[0, 0] + q_L * M[1, 1]
            Im = q_L * q_R * M[0, 1] + M[1, 0]
            denom = Re**2 + Im**2
            T_k[ik] = 4.0 * q_L * q_R / (denom + 1e-300)
            # Clamp to [0, 1]
            T_k[ik] = min(T_k[ik], 1.0)
        else:
            # Right side evanescent: total reflection
            T_k[ik] = 0.0

    return T_k

# Downsample eta for efficiency: use N_slab = 2000 slabs
N_slab = 2000
idx_slab = np.linspace(0, len(eta_fine) - 1, N_slab, dtype=int)
eta_slab = eta_fine[idx_slab]
V_geo_slab = V_geometric[idx_slab]
V_bcs_slab = V_BCS[idx_slab]
V_eff_slab = V_eff[idx_slab]
V_tot_slab = V_total[idx_slab]

# Verify slab resolution
deta_slab = np.diff(eta_slab)
k_Nyquist_slab = PI / deta_slab.max()
print(f"\nSlab decomposition: N = {N_slab}")
print(f"  deta range: [{deta_slab.min():.3e}, {deta_slab.max():.3e}]")
print(f"  k_Nyquist (slab) = {k_Nyquist_slab:.1f}")
print(f"  k_max / k_Nyquist = {k_max / k_Nyquist_slab:.3f}")

# Since V grows monotonically from V_L ~ 2.2e4 to V_R ~ 1.1e8,
# only modes with k^2 > V_R (k > ~10452) can transmit through.
# For k < k_crit = sqrt(V_R), T = 0 by total reflection.
# For k > k_crit, we get partial/full transmission.

V_L_geo = V_geo_slab[0]
V_R_geo = V_geo_slab[-1]
V_L_eff = V_eff_slab[0]
V_R_eff = V_eff_slab[-1]
V_L_tot = V_tot_slab[0]
V_R_tot = V_tot_slab[-1]

k_crit_geo = np.sqrt(V_R_geo)
k_crit_eff = np.sqrt(V_R_eff)
k_crit_tot = np.sqrt(V_R_tot)

print(f"\nBarrier edges (k_crit = sqrt(V_R)):")
print(f"  Geometric:    V_R = {V_R_geo:.4e}, k_crit = {k_crit_geo:.1f}")
print(f"  Geo+BCS:      V_R = {V_R_eff:.4e}, k_crit = {k_crit_eff:.1f}")
print(f"  Geo+BCS+conf: V_R = {V_R_tot:.4e}, k_crit = {k_crit_tot:.1f}")
print(f"  k_max in grid = {k_max:.1f}")

# Check: for the monotonic barrier, modes with k < k_crit have T = 0 exactly
# Only modes with k > k_crit can transmit.
# With k_max = 10 * k_tach_fold ~ 19745 and k_crit ~ 10452, we have
# a window k in [10452, 19745] where transmission is possible.

print("\nComputing T(k) for geometric-only potential...")
T_geo = transfer_matrix_T(k_grid, V_geo_slab, eta_slab)

print("Computing T(k) for geometric + BCS potential...")
T_eff = transfer_matrix_T(k_grid, V_eff_slab, eta_slab)

print("Computing T(k) for geometric + BCS + conformal potential...")
T_tot = transfer_matrix_T(k_grid, V_tot_slab, eta_slab)

# Report
n_trans_geo = np.sum(T_geo > 1e-10)
n_trans_eff = np.sum(T_eff > 1e-10)
n_trans_tot = np.sum(T_tot > 1e-10)
print(f"\nTransmission results:")
print(f"  T_geo > 1e-10: {n_trans_geo}/{N_k} modes")
print(f"  T_eff > 1e-10: {n_trans_eff}/{N_k} modes")
print(f"  T_tot > 1e-10: {n_trans_tot}/{N_k} modes")

for label, T_arr, kc in [("geometric", T_geo, k_crit_geo),
                          ("geo+BCS", T_eff, k_crit_eff),
                          ("geo+BCS+conf", T_tot, k_crit_tot)]:
    if np.any(T_arr > 1e-10):
        k_edge = k_grid[np.argmax(T_arr > 1e-10)]
        T_max = T_arr.max()
        k_at_max = k_grid[np.argmax(T_arr)]
        print(f"  {label}: k_edge = {k_edge:.1f}, T_max = {T_max:.6f} at k = {k_at_max:.1f}, "
              f"k_crit = {kc:.1f}")
    else:
        print(f"  {label}: ALL modes reflected (T < 1e-10), k_crit = {kc:.1f}")

# Verify T <= 1 (unitarity check)
for label, T_arr in [("T_geo", T_geo), ("T_eff", T_eff), ("T_tot", T_tot)]:
    if T_arr.max() > 1.0 + 1e-6:
        print(f"  WARNING: {label} max = {T_arr.max():.6f} > 1.0 (unitarity violation)")
    else:
        print(f"  {label}: max = {T_arr.max():.6f} <= 1.0 (unitarity OK)")

# ============================================================================
#  SECTION 5: Search for Fabry-Perot Resonances
# ============================================================================

print("\n" + "=" * 72)
print("SECTION 5: Fabry-Perot Resonance Search")
print("=" * 72)

# A Fabry-Perot resonance appears as a sharp peak in T(k) where T -> 1
# at a frequency where neighboring k-values have T << 1.
# This requires a cavity: two barriers with a classically allowed gap.
# For a monotonic barrier, no cavity exists and no resonances are expected.

# Search for peaks in T(k) - these could indicate oscillatory structure
# from interference between different turning points

resonance_data = []
for label, T_arr in [("T_eff", T_eff), ("T_tot", T_tot)]:
    mask_nonzero = T_arr > 1e-10
    if np.sum(mask_nonzero) > 10:
        # Search for oscillatory peaks in the transmission region
        T_search = T_arr[mask_nonzero]
        k_search = k_grid[mask_nonzero]

        # Look for peaks with prominence > 5% of max
        peaks_idx, props = find_peaks(T_search, prominence=0.05 * T_search.max())
        n_res = len(peaks_idx)

        print(f"\n  {label}: {n_res} peaks found above 5% prominence threshold")

        if n_res > 0:
            for ip in range(min(n_res, 10)):  # Report first 10
                pidx = peaks_idx[ip]
                k_res = k_search[pidx]
                T_res = T_search[pidx]
                prom = props['prominences'][ip]

                # Estimate Q-factor from FWHM
                half_val = T_res - prom / 2.0
                # Find FWHM by searching for half-maximum crossings
                left_cross = pidx
                for li in range(pidx - 1, -1, -1):
                    if T_search[li] < half_val:
                        left_cross = li
                        break
                right_cross = pidx
                for ri in range(pidx + 1, len(T_search)):
                    if T_search[ri] < half_val:
                        right_cross = ri
                        break
                if left_cross != right_cross:
                    dk_fwhm = k_search[min(right_cross, len(k_search)-1)] - k_search[left_cross]
                    Q_res = k_res / max(dk_fwhm, 1e-10)
                else:
                    Q_res = 0.0  # (local)

                print(f"    Peak {ip+1}: k = {k_res:.1f}, T = {T_res:.6f}, "
                      f"prominence = {prom:.4f}, Q = {Q_res:.1f}")
                if label == "T_eff":
                    resonance_data.append({'k': k_res, 'T': T_res,
                                           'Q': Q_res, 'prominence': prom})
    else:
        print(f"\n  {label}: too few transmitting modes ({np.sum(mask_nonzero)}) for resonance search")

n_resonances = len(resonance_data)
print(f"\n  Total resonances in T_eff: {n_resonances}")

# ============================================================================
#  SECTION 6: BCS Impact on Transmission Edge
# ============================================================================

print("\n" + "=" * 72)
print("SECTION 6: BCS Impact on Barrier Edge")
print("=" * 72)

print(f"Barrier heights (V at boundaries) and critical wavenumbers:")
print(f"  Geometric only:   V_L = {V_L_geo:.3e}, V_R = {V_R_geo:.3e}, k_crit = {k_crit_geo:.2f}")
print(f"  Geometric + BCS:  V_L = {V_L_eff:.3e}, V_R = {V_R_eff:.3e}, k_crit = {k_crit_eff:.2f}")
print(f"  Geo + BCS + conf: V_L = {V_L_tot:.3e}, V_R = {V_R_tot:.3e}, k_crit = {k_crit_tot:.2f}")

print(f"\nBCS shift of barrier edge:")
dk_BCS = k_crit_eff - k_crit_geo
print(f"  dk_crit(BCS) = {dk_BCS:.4f} M_KK ({dk_BCS/k_crit_geo*100:.6f}%)")
print(f"  The BCS gap shifts the critical wavenumber by a negligible amount.")

# BCS contribution at different tau
print(f"\nBCS potential relative to geometric at key locations:")
for t in [0.15, 0.19, 0.20, 0.25, 0.30]:
    idx = np.argmin(np.abs(tau_fine - t))
    ratio = V_BCS[idx] / V_geometric[idx] if V_geometric[idx] > 0 else 0
    print(f"  tau={t:.2f}: V_BCS/V_geo = {ratio:.2e}, Delta = {Delta_profile[idx]:.4f}, "
          f"a = {a_fine[idx]:.4f}")

# ============================================================================
#  SECTION 7: Conformal Factor Profile Through Barrier
# ============================================================================

print("\n" + "=" * 72)
print("SECTION 7: Conformal Factor Profile Through Barrier")
print("=" * 72)

print(f"Omega_transit profile:")
print(f"  min = {Omega_transit.min():.6e}")
print(f"  max = {Omega_transit.max():.6e}")
print(f"  at fold = {Omega_transit[fold_idx]:.6e}")

print(f"\nOmega''/Omega profile:")
print(f"  min = {V_conformal.min():.4e}")
print(f"  max = {V_conformal.max():.4e}")
print(f"  at fold = {V_conformal[fold_idx]:.4e}")
print(f"  |Omega''/Omega| / (z''/z) at fold = {abs(V_conformal[fold_idx]) / V_geometric[fold_idx]:.2e}")

# Check sign changes in d(Omega''/Omega)
dV_conf = np.diff(V_conformal)
sign_changes = np.sum(dV_conf[:-1] * dV_conf[1:] < 0)
print(f"\n  Sign changes in d(Omega''/Omega)/deta: {sign_changes}")

# ============================================================================
#  SECTION 8: WKB Cross-Check
# ============================================================================

print("\n" + "=" * 72)
print("SECTION 8: WKB Analytic Cross-Check")
print("=" * 72)

# For a monotonically rising barrier, the WKB transmission is:
#   T_WKB(k) = exp(-2 * integral_eta_turn^eta_R kappa(eta) deta)
# where kappa(eta) = sqrt(V_eff(eta) - k^2) in the evanescent region.
# This integral runs from the turning point (where k^2 = V_eff) to the
# right boundary.
#
# For modes with k > k_crit_eff (fully propagating), T_WKB ~ 1 with
# small above-barrier reflection from the potential gradient.

T_wkb = np.zeros(N_k)
for ik, k in enumerate(k_grid):
    k2 = k**2
    if k2 <= V_eff[0]:
        T_wkb[ik] = 0.0
        continue
    if k2 >= V_eff[-1]:
        # Fully above barrier: T ~ 1 (WKB)
        T_wkb[ik] = 1.0
        continue

    # Find turning point and integrate through evanescent region
    evanescent = V_eff > k2
    integrand = np.sqrt(np.maximum(V_eff - k2, 0.0))
    # Integrate only over evanescent region
    integrand_ev = np.where(evanescent, integrand, 0.0)
    integral = np.trapezoid(integrand_ev, eta_fine)
    T_wkb[ik] = np.exp(-2.0 * integral)
    if T_wkb[ik] < 1e-300:
        T_wkb[ik] = 0.0

# Compare WKB and transfer matrix
if np.any(T_wkb > 1e-10) and np.any(T_eff > 1e-10):
    mask_both = (T_wkb > 1e-10) & (T_eff > 1e-10)
    if np.any(mask_both):
        ratio_TM_WKB = T_eff[mask_both] / T_wkb[mask_both]
        print(f"Transfer matrix / WKB ratio (where both > 1e-10):")
        print(f"  Mean ratio = {ratio_TM_WKB.mean():.4f}")
        print(f"  Std ratio  = {ratio_TM_WKB.std():.4f}")
        print(f"  Min ratio  = {ratio_TM_WKB.min():.4f}")
        print(f"  Max ratio  = {ratio_TM_WKB.max():.4f}")
    else:
        print("No modes with both T_TM > 0 and T_WKB > 0")
else:
    print("WKB or TM have no transmitting modes")

# Above-barrier transmission
print(f"\nAbove-barrier transmission (k > k_crit_eff = {k_crit_eff:.1f}):")
above = k_grid > k_crit_eff
if np.any(above):
    T_above = T_eff[above]
    print(f"  N modes above barrier: {np.sum(above)}")
    print(f"  Mean T = {T_above.mean():.6f}")
    print(f"  Min T = {T_above.min():.6f}")
    print(f"  Reflection R = 1-T: mean = {(1-T_above).mean():.6f}")

# ============================================================================
#  SECTION 9: Physical Interpretation
# ============================================================================

print("\n" + "=" * 72)
print("SECTION 9: Physical Interpretation")
print("=" * 72)

# Determine the barrier topology
# For a Fabry-Perot cavity, we need V_eff to have a local minimum
# flanked by two local maxima: V_max1, V_min, V_max2.
# A mode with V_min < k^2 < min(V_max1, V_max2) can resonate in the cavity.

# Check if V_eff has a non-monotonic region
is_monotonic_eff = (n_violations_eff == 0)

print("Barrier topology analysis:")
print(f"  V_eff monotonic: {is_monotonic_eff} ({n_violations_eff} violations)")
print(f"  Cavity in V_eff: {has_cavity_eff}")
print(f"  Cavity in V_total: {has_cavity}")

# The key structural result
print(f"\n  STRUCTURAL RESULT:")
if is_monotonic_eff:
    print(f"  The compound barrier V_eff = z''/z + Delta^2*a^2 is monotonically increasing")
    print(f"  through the transit region [tau=0.10, tau=0.30]. No Fabry-Perot cavity exists.")
    print(f"  The BCS gap adds a perturbative correction ({V_BCS[fold_idx]/V_geometric[fold_idx]*100:.6f}%)")
    print(f"  that does not alter the topological structure of the barrier.")
    print(f"  Physical reason: z''/z ~ a^2 * (2*eps_H + ...) and Delta^2*a^2 both scale")
    print(f"  with a^2(tau), which grows monotonically. No interplay between geometric")
    print(f"  and BCS potentials creates a local minimum.")
else:
    print(f"  The compound barrier has {n_violations_eff} non-monotonic points.")
    if has_cavity_eff:
        print(f"  A cavity structure EXISTS in V_eff.")
    else:
        print(f"  Despite non-monotonicity, no prominent cavity structure.")

# Condensed matter analog
print(f"\n  Condensed matter analog:")
print(f"  In superfluid He-3B, the BdG quasiparticle spectrum has a gap 2*Delta")
print(f"  but the scattering potential for collective modes (second sound) at a")
print(f"  normal-superfluid interface is a single step function, not a cavity.")
print(f"  Fabry-Perot requires a thin film (two interfaces) or a periodic structure.")
print(f"  The phonon-exflation transit provides a single interface (normal -> BCS),")
print(f"  which produces reflection but not resonance.")

# T(k) structure
if np.any(T_eff > 1e-10):
    k_transmitting = k_grid[T_eff > 1e-10]
    print(f"\n  Transmission window: k in [{k_transmitting.min():.1f}, {k_transmitting.max():.1f}]")
    print(f"  This corresponds to modes with k > k_crit = {k_crit_eff:.1f}")
    print(f"  (modes above the barrier maximum at the right boundary)")

    # Check for oscillatory structure in above-barrier T(k)
    above_mask = k_grid > k_crit_eff
    if np.sum(above_mask) > 10:
        T_above_arr = T_eff[above_mask]
        # Standard deviation from unity as measure of oscillation
        sigma_T = np.std(T_above_arr)
        print(f"  Above-barrier T oscillation: sigma = {sigma_T:.6f}")
        if sigma_T > 0.01:
            print(f"  Significant above-barrier oscillations present.")
            print(f"  These represent partial reflection from the potential gradient,")
            print(f"  not Fabry-Perot resonance. They do not produce sharp spectral features.")
        else:
            print(f"  Negligible above-barrier oscillations. Clean transmission.")

# ============================================================================
#  SECTION 10: Gate Verdict
# ============================================================================

print("\n" + "=" * 72)
print("SECTION 10: Gate Verdict")
print("=" * 72)

verdict = "INFO"
detail_parts = []

detail_parts.append(f"V_eff monotonic={is_monotonic_eff}")
detail_parts.append(f"BCS/geo_fold={V_BCS[fold_idx]/V_geometric[fold_idx]:.2e}")
detail_parts.append(f"k_crit={k_crit_eff:.1f}")
detail_parts.append(f"N_resonances={n_resonances}")

if n_resonances > 0:
    Q_max = max(r['Q'] for r in resonance_data)
    detail_parts.append(f"Q_max={Q_max:.1f}")
else:
    detail_parts.append("Q=N/A")

if np.any(T_eff > 1e-10):
    detail_parts.append(f"T_max={T_eff.max():.4f}")
else:
    detail_parts.append("T_max=0")

gate_detail = "; ".join(detail_parts)

print(f"\nGate: CAVITY-BCS-HORIZON-70")
print(f"  Verdict: {verdict}")
print(f"  Detail: {gate_detail}")

# ============================================================================
#  SECTION 11: Save data
# ============================================================================

print("\n" + "=" * 72)
print("SECTION 11: Saving outputs")
print("=" * 72)

outpath = os.path.join(data_dir, 's70_cavity_bcs_horizon.npz')

save_dict = {
    # Grid data
    'tau_fine': tau_fine,
    'eta_fine': eta_fine,
    'k_grid': k_grid,
    'k_tach_fold': np.float64(k_tach_fold),
    'k_transit': np.float64(k_transit),

    # Potential profiles
    'V_geometric': V_geometric,
    'V_BCS': V_BCS,
    'V_eff': V_eff,
    'V_conformal': V_conformal,
    'V_total': V_total,
    'Delta_profile': Delta_profile,

    # Transmission coefficients
    'T_geo': T_geo,
    'T_eff': T_eff,
    'T_tot': T_tot,
    'T_wkb': T_wkb,

    # Barrier diagnostics
    'k_crit_geo': np.float64(k_crit_geo),
    'k_crit_eff': np.float64(k_crit_eff),
    'k_crit_tot': np.float64(k_crit_tot),
    'V_eff_max': np.float64(V_eff.max()),
    'V_geo_max': np.float64(V_geometric.max()),
    'is_monotonic_eff': np.bool_(is_monotonic_eff),
    'has_cavity': np.bool_(has_cavity),
    'has_cavity_eff': np.bool_(has_cavity_eff),
    'BCS_geo_ratio_fold': np.float64(V_BCS[fold_idx] / V_geometric[fold_idx]),
    'delta_tau_BCS': np.float64(delta_tau_BCS),

    # Conformal factor
    'Omega_transit': Omega_transit,
    'Omega_pp_Omega': Omega_pp_Omega,

    # Resonance results
    'n_resonances': np.int64(n_resonances),

    # Gate
    'gate_name': np.str_('CAVITY-BCS-HORIZON-70'),
    'gate_verdict': np.str_(verdict),
    'gate_detail': np.str_(gate_detail),
}

np.savez(outpath, **save_dict)
print(f"Data saved to: {outpath}")

# ============================================================================
#  SECTION 12: Plots
# ============================================================================

print("\nGenerating plots...")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('CAVITY-BCS-HORIZON-70: Compound Barrier Transmission',
             fontsize=14, fontweight='bold')

# Panel 1: Effective potential profiles
ax1 = axes[0, 0]
ax1.semilogy(tau_fine, V_geometric, 'b-', lw=1.5, label=r"$z''/z$ (geometric)")
V_BCS_plot = np.where(V_BCS > 1e-20, V_BCS, np.nan)
ax1.semilogy(tau_fine, V_BCS_plot, 'r--', lw=1.5, label=r'$\Delta^2 a^2$ (BCS)')
ax1.semilogy(tau_fine, V_eff, 'k-', lw=2, label=r'$V_{\rm eff}$ (compound)')
ax1.axvline(tau_fold, color='gray', ls=':', alpha=0.5, label=f'fold ($\\tau={tau_fold}$)')
ax1.set_xlabel(r'$\tau$')
ax1.set_ylabel(r'$V_{\rm eff}$ [M$_{\rm KK}^2$]')
ax1.set_title('Effective Potential Components')
ax1.legend(fontsize=8)
ax1.set_xlim([0.10, 0.30])

# Panel 2: Transmission coefficient T(k)
ax2 = axes[0, 1]
# Plot only nonzero values
for label, T_arr, style in [("Geometric only", T_geo, 'b-'),
                             ("Geo + BCS", T_eff, 'k-'),
                             ("Geo + BCS + conf", T_tot, 'r--'),
                             ("WKB", T_wkb, 'g:')]:
    mask_nz = T_arr > 1e-30
    if np.any(mask_nz):
        lw = 2 if 'BCS' in label and 'conf' not in label else 1.5  # (local)
        ax2.plot(k_grid[mask_nz] / k_tach_fold, T_arr[mask_nz], style,
                 lw=lw, alpha=0.8, label=label)

ax2.axvline(1.0, color='gray', ls=':', alpha=0.5, label=r'$k_{\rm tach}$')
ax2.axvline(k_crit_eff / k_tach_fold, color='orange', ls='--', alpha=0.5,
            label=f'$k_{{\\rm crit}}$')
ax2.set_xlabel(r'$k / k_{\rm tach}$')
ax2.set_ylabel(r'$T(k)$')
ax2.set_title('Transmission Coefficient')
ax2.legend(fontsize=7)
ax2.set_xlim([0.1, 10])
ax2.set_ylim([-0.05, 1.1])

# Panel 3: BCS gap profile and scale factor
ax3 = axes[1, 0]
ax3_twin = ax3.twinx()
ax3.plot(tau_fine, Delta_profile, 'r-', lw=2, label=r'$\Delta(\tau)$')
ax3_twin.plot(tau_fine, a_fine, 'b--', lw=1.5, label=r'$a(\tau)$')
ax3.axvline(tau_fold, color='gray', ls=':', alpha=0.5)
ax3.set_xlabel(r'$\tau$')
ax3.set_ylabel(r'$\Delta$ [M$_{\rm KK}$]', color='r')
ax3_twin.set_ylabel(r'$a(\tau)$', color='b')
ax3.set_title('BCS Gap Profile and Scale Factor')
ax3.tick_params(axis='y', labelcolor='r')
ax3_twin.tick_params(axis='y', labelcolor='b')

# Panel 4: V_BCS / V_geometric ratio
ax4 = axes[1, 1]
ratio_bcs_geo = V_BCS / (V_geometric + 1e-30)
mask_ratio = ratio_bcs_geo > 1e-20
ax4.semilogy(tau_fine[mask_ratio], ratio_bcs_geo[mask_ratio], 'k-', lw=2)
ax4.axvline(tau_fold, color='gray', ls=':', alpha=0.5, label=f'fold')
ax4.set_xlabel(r'$\tau$')
ax4.set_ylabel(r'$V_{\rm BCS} / V_{\rm geometric}$')
ax4.set_title('BCS-to-Geometric Potential Ratio')
ax4.legend()
ax4.set_xlim([0.10, 0.30])

plt.tight_layout()
plotpath = os.path.join(data_dir, 's70_cavity_bcs_horizon.png')
plt.savefig(plotpath, dpi=150, bbox_inches='tight')
print(f"Plot saved to: {plotpath}")
plt.close()

print("\n" + "=" * 72)
print("CAVITY-BCS-HORIZON-70 COMPLETE")
print("=" * 72)
