#!/usr/bin/env python3
"""
S75-B3-FOLD-STIFFNESS: ATDHFB Collective Mass Under GGE Backreaction
=====================================================================

Gate: S75-B3-FOLD-STIFFNESS
  PASS: tau_turn in [0.45, 0.70]
  INFO: tau_turn in [0.30, 0.45] or [0.70, 1.00]
  FAIL: tau_turn > 1.00 or no turning point found

Physics:
  The ATDHFB (Adiabatic Time-Dependent HFB) collective inertia for the
  Jensen deformation tau is computed following Baran, Sheikh, Dobaczewski,
  Nazarewicz (2011) [Paper 16]. The key modification: the GGE relic from
  the fold transit freezes occupation numbers n_k at non-thermal values,
  which modifies both the BCS coherence factors (u_k, v_k) and the
  quasiparticle energies E_k^{qp} entering the collective mass formula.

  ATDHFB collective mass formula (perturbative cranking, Paper 16 Eq. 60):

    M^{Cp} = sum_{k,l} |<k|dH/dtau|l>|^2 * (eta^+_{kl})^2 / (E_k + E_l)^3
                                                                       (1)

  where eta^+_{kl} = u_k*v_l + v_k*u_l (BCS coherence factor combination)
  and E_k = sqrt((eps_k - lambda)^2 + Delta^2) are quasiparticle energies.

  GGE modification: n_k are frozen, not thermal. Coherence factors from
  v_k^2 = n_k, u_k^2 = 1 - n_k. Quasiparticle energies from
  E_k = Delta / (2*u_k*v_k) which differs from standard BCS E_k.

  Equation of motion: M(tau)*d^2tau/dt^2 + dV_eff/dtau = 0

References:
  - Paper 16: Baran et al., PRC 84, 054321 (2011) -- ATDHFB collective inertia
  - Paper 17: Dussel et al., PRC 76, 011302 (2007) -- Ultrasmall BCS
  - S56: GGE fabric data (s56_gge_fabric.npz)
  - S74: Moduli stabilization (s74_moduli_stabilization.npz)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import CubicSpline
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import (
    tau_fold, Delta_BCS, dS_fold, d2S_fold, S_fold,
    M_ATDHFB, Z_fold, G_DeWitt, dt_transit, v_terminal,
    E_cond, N_dof_BCS, Delta_0_GL
)

# ============================================================================
#  SECTION 1: Load Data
# ============================================================================

print("=" * 72)
print("S75-B3-FOLD-STIFFNESS: ATDHFB Collective Mass + GGE Backreaction")
print("=" * 72)

base_dir = os.path.dirname(__file__)

d56 = np.load(os.path.join(base_dir, 's56_gge_fabric.npz'), allow_pickle=True)
nk_GGE = d56['nk_DE']           # 16 GGE occupation numbers
eps_fold = d56['eps_fold']       # 8 single-particle energies at fold

d74 = np.load(os.path.join(base_dir, 's74_moduli_stabilization.npz'), allow_pickle=True)
tau_scan_74 = d74['tau_scan']     # [0.15, 1.70], 500 pts
V_bare_74 = d74['V_bare_scan']
V_GGE_74 = d74['V_GGE_scan']
V_dressed_c = d74['V_dressed_c']  # V_bare + V_GGE
Delta_scan = d74['Delta_scan']
pos_evals_fold = d74['pos_evals_fold']

print(f"\nData loaded:")
print(f"  S56: {len(nk_GGE)} GGE modes, eps_fold: {len(eps_fold)} levels")
print(f"  S74: tau in [{tau_scan_74[0]:.3f}, {tau_scan_74[-1]:.3f}], {len(tau_scan_74)} pts")

# ============================================================================
#  SECTION 2: BCS Coherence Factors from GGE Occupations
# ============================================================================

# The 16 modes are 8 independent + 8 time-reversed partners.
N_modes = 8  # (local) 4 B2 + 1 B1 + 3 B3
nk_indep = nk_GGE[:N_modes]  # (local)

vk2 = nk_indep.copy()   # (local) v_k^2 = n_k
uk2 = 1.0 - vk2         # (local) u_k^2 = 1 - n_k
vk = np.sqrt(vk2)       # (local)
uk = np.sqrt(uk2)        # (local)

N_particles = 2.0 * np.sum(vk2)  # (local) 2 for TR pairs

print(f"\nBCS coherence factors (GGE-frozen):")
print(f"  N_particles = {N_particles:.6f}")
print(f"  v_k^2 = {vk2}")

# Quasiparticle energies: E_k = Delta / (2*u_k*v_k)
# This follows from BCS: v_k^2 = (1/2)(1 - xi_k/E_k) and E_k = sqrt(xi_k^2 + Delta^2)
# Combined: E_k = Delta / (2*sqrt(n_k*(1-n_k))) = Delta / (2*u_k*v_k)
Delta_at_fold = Delta_BCS  # = 0.4643 M_KK

Ek_qp = Delta_at_fold / (2.0 * uk * vk)  # (local) GGE quasiparticle energies
xi_k = Ek_qp * (1.0 - 2.0 * vk2)  # (local) effective single-particle energies

print(f"  E_k^qp = {Ek_qp}")
print(f"  xi_k (effective) = {xi_k}")

# ============================================================================
#  SECTION 3: Mode Energy Derivatives deps_k/dtau
# ============================================================================

# From the spectral flow: the D_K eigenvalues shift with tau.
# eps_fold are the 8 BCS mode energies at tau ~ 0.194.
# At tau = 0 (round SU(3)), eps_k = 0 (all degenerate).
# The Hellmann-Feynman estimate: deps_k/dtau ~ eps_k / tau_fold.

tau_fold_actual = float(d56['tau_fold_actual'])  # (local) ~ 0.194

deps_dtau = eps_fold / tau_fold_actual  # (local)
# The Goldstone mode (eps_fold[0] ~ 0) has near-zero derivative.
# Give it a small nonzero value (protected by symmetry):
deps_dtau[0] = 0.01 * deps_dtau[1]  # (local) 1% of next mode

print(f"\nMode energy derivatives deps_k/dtau:")
print(f"  {deps_dtau}")

# Chemical potential derivative from particle number conservation:
#   dlambda/dtau = sum_k (deps_k/dtau / E_k^3) / sum_k (1/E_k^3)
weights_Ek3 = 1.0 / Ek_qp**3  # (local)
dlambda_dtau = np.sum(deps_dtau * weights_Ek3) / np.sum(weights_Ek3)  # (local)
dxi_dtau = deps_dtau - dlambda_dtau  # (local)

print(f"  dlambda/dtau = {dlambda_dtau:.6f}")

# ============================================================================
#  SECTION 4: ATDHFB Collective Mass at the Fold
# ============================================================================

# Derivation from Paper 16 (perturbative cranking, Eq. 60):
#
# The ATDHFB-Cp mass for a single collective coordinate q = tau is:
#
#   M = sum_{k<l} 2 * |<k|dh/dtau|l>|^2 * (eta^+_{kl})^2 / (E_k + E_l)^3  (2)
#
# where eta^+_{kl} = u_k*v_l + v_k*u_l.
#
# The diagonal (k=l) contribution uses the self-consistent relation:
#   u_k*dv_k/dtau - v_k*du_k/dtau = -Delta/(2*E_k^2) * dxi_k/dtau       (3)
#
# yielding the diagonal cranking mass:
#   M_diag = 2 * sum_k [Delta * dxi_k/dtau / (2*E_k^2)]^2 / E_k^3
#          = (Delta^2/2) * sum_k (dxi_k/dtau)^2 / E_k^7                  (4)
#
# With factor 2 for time-reversed pairs:
#   M = Delta^2 * sum_k (dxi_k/dtau)^2 / E_k^7                           (5)
#
# For the off-diagonal contribution (k != l), we add:
#   M_offdiag = 2 * sum_{k<l} |h'_{kl}|^2 * (eta^+_{kl})^2 / (E_k+E_l)^3  (6)
#
# The off-diagonal matrix elements |h'_{kl}| are typically smaller than
# diagonal ones but can be significant at level crossings (Paper 16 result).
# For the fold (van Hove singularity), levels cluster, enhancing off-diagonal.

# --- Diagonal contribution ---
M_diag = Delta_at_fold**2 * np.sum(dxi_dtau**2 / Ek_qp**7)  # (local) Eq. (5)

# --- Off-diagonal contribution ---
# Matrix elements |<k|dh/dtau|l>|^2 for k != l.
# At the fold, the spectral density is high. Use the Fermi golden rule estimate:
# |h'_{kl}|^2 ~ (deps_k/dtau * deps_l/dtau) * coupling_strength
# where coupling_strength ~ Delta / (E_k * E_l) from the pairing interaction.
# This is the standard Landau-Zener coupling at avoided crossings.

M_offdiag = 0.0  # (local)
for k in range(N_modes):
    for l in range(k+1, N_modes):
        eta_plus_kl = uk[k]*vk[l] + vk[k]*uk[l]  # (local)
        # Off-diagonal matrix element estimate (Paper 16 Eq. 41):
        # Use the pairing-induced coupling: h'_{kl} ~ Delta * deps_k/dtau / (E_k * E_l)
        h_kl_sq = (Delta_at_fold * np.sqrt(np.abs(deps_dtau[k] * deps_dtau[l]))
                   / (Ek_qp[k] * Ek_qp[l]))**2  # (local)
        denom = (Ek_qp[k] + Ek_qp[l])**3  # (local)
        M_offdiag += 2.0 * h_kl_sq * eta_plus_kl**2 / denom

M_fold_total = M_diag + M_offdiag  # (local)
offdiag_frac = M_offdiag / M_fold_total if M_fold_total > 0 else 0  # (local)

print(f"\nATDHFB Collective Mass at fold:")
print(f"  M_diag    = {M_diag:.6f} M_KK^{{-2}}")
print(f"  M_offdiag = {M_offdiag:.6f} M_KK^{{-2}}")
print(f"  M_total   = {M_fold_total:.6f} M_KK^{{-2}}")
print(f"  Off-diagonal fraction = {offdiag_frac:.4f}")
print(f"  Canonical M_ATDHFB (S40) = {M_ATDHFB}")
print(f"  Ratio M_GGE / M_canonical = {M_fold_total / M_ATDHFB:.4f}")

# ============================================================================
#  CHK1: M(tau) must be positive (ATDHFB stability)
# ============================================================================
chk1_pass = M_fold_total > 0  # (local)
print(f"\n--- CHK1: M(tau) > 0 ---")
print(f"  M_total = {M_fold_total:.6f} > 0: {'PASS' if chk1_pass else 'FAIL'}")

# ============================================================================
#  CHK2: Delta -> 0 limit reduces to cranking formula
# ============================================================================
# In the limit Delta -> 0 with FIXED occupation numbers (GGE frozen):
#   E_k = Delta/(2*u_k*v_k) -> 0
#   M_diag = Delta^2 * sum dxi^2 / E_k^7 = Delta^2 * sum dxi^2*(2*u_k*v_k)^7/Delta^7
#          = (2*u_k*v_k)^7 * sum dxi^2 / Delta^5 -> DIVERGES
#
# This is the correct physical behavior: in nuclear physics, the cranking
# mass diverges at level crossings where the pairing gap is suppressed
# (Paper 16, Fig. 2 -- sharp peaks in M at Delta->0 regions).
#
# The non-pairing cranking mass uses eps_k directly (no BCS coherence):
#   M_crank = sum_{k != l} |<k|dh/dtau|l>|^2 / (eps_k - eps_l)^2
# This is finite for non-degenerate levels but diverges at degeneracies.
#
# Test: compute M for progressively smaller Delta and verify divergence.

Delta_tests = np.array([0.5, 0.1, 0.01, 0.001]) * Delta_at_fold  # (local)
M_vs_Delta = []  # (local)
for dt in Delta_tests:
    Ek_t = dt / (2.0 * uk * vk)  # (local)
    M_t = dt**2 * np.sum(dxi_dtau**2 / Ek_t**7)  # (local)
    M_vs_Delta.append(M_t)
M_vs_Delta = np.array(M_vs_Delta)  # (local)

# Check divergence: M should scale as 1/Delta^5
# M_diag ~ Delta^2 * sum(dxi^2 / E^7)
# With E = Delta/(2*u*v), we get E^7 = Delta^7/(2*u*v)^7
# So M_diag ~ Delta^2 * (2*u*v)^7 * sum(dxi^2) / Delta^7 = C / Delta^5
# where C = (2*u*v)^7 * sum(dxi^2) is independent of Delta.
# The successive ratio M(Delta_i)/M(Delta_{i+1}) should equal (Delta_{i+1}/Delta_i)^5.

# Successive M ratios: M(smaller Delta) / M(larger Delta) should grow as (Delta_ratio)^{-5}
ratios_chk2 = M_vs_Delta[1:] / M_vs_Delta[:-1]  # (local) larger/smaller
step_ratios = Delta_tests[:-1] / Delta_tests[1:]  # (local) e.g., [5, 10, 10]
expected_M_ratios = step_ratios**5  # (local) [3125, 1e5, 1e5]

print(f"\n--- CHK2: Delta -> 0 divergence (cranking limit) ---")
print(f"  Delta/Delta_0  |  M_diag       |  M ratio   | Expected")
for i, dt in enumerate(Delta_tests):
    if i > 0:
        print(f"  {dt/Delta_at_fold:.4f}        | {M_vs_Delta[i]:.4e} | "
              f"{ratios_chk2[i-1]:.1f}    | {expected_M_ratios[i-1]:.1f}")
    else:
        print(f"  {dt/Delta_at_fold:.4f}        | {M_vs_Delta[i]:.4e} | ---        | ---")

# Check log-ratio match
log_err = np.abs(np.log10(ratios_chk2) - np.log10(expected_M_ratios))  # (local)
scaling_ok = bool(np.all(log_err < 0.1))  # (local)
chk2_pass = scaling_ok  # (local)
print(f"  Log-ratio errors: {log_err}")
print(f"  1/Delta^5 scaling: {'PASS' if chk2_pass else 'FAIL'}")

# ============================================================================
#  SECTION 5: Effective Potential (Extended Range)
# ============================================================================

# The S74 scan covers [0.15, 1.70]. For the turning point calculation,
# we need V_eff at potentially larger tau.
# Extend the potential using quadratic extrapolation from the last portion.

# Fit the high-tau tail (tau > 1.0) to a polynomial for extrapolation
high_mask = tau_scan_74 > 1.0  # (local)
tau_high = tau_scan_74[high_mask]  # (local)
V_high = V_dressed_c[high_mask]  # (local)

# Quadratic fit: V(tau) ~ a + b*tau + c*tau^2
poly_coeff = np.polyfit(tau_high, V_high, 2)  # (local)

# Extend scan to tau = 10.0 (generous upper bound)
# Start AFTER the last S74 point to avoid duplicate x-values
tau_extend = np.linspace(tau_scan_74[-1] + 0.01, 10.0, 500)  # (local)
V_extend = np.polyval(poly_coeff, tau_extend)  # (local)

# Concatenate
tau_full = np.concatenate([tau_scan_74, tau_extend])  # (local)
V_full = np.concatenate([V_dressed_c, V_extend])  # (local)

V_eff_spl = CubicSpline(tau_full, V_full)  # (local)
dV_eff_spl = V_eff_spl.derivative()  # (local)

V_fold_val = V_eff_spl(tau_fold)  # (local)
dV_fold_val = dV_eff_spl(tau_fold)  # (local)

print(f"\nEffective potential (extended to tau=10):")
print(f"  V_eff(tau_fold) = {V_fold_val:.4f} M_KK^4")
print(f"  dV_eff/dtau(fold) = {dV_fold_val:.4f} M_KK^4")
print(f"  V_eff(tau=5) = {float(V_eff_spl(5.0)):.1f}")
print(f"  V_eff(tau=10) = {float(V_eff_spl(10.0)):.1f}")
print(f"  Polynomial: {poly_coeff[0]:.4f}*tau^2 + {poly_coeff[1]:.4f}*tau + {poly_coeff[2]:.4f}")

# ============================================================================
#  SECTION 6: Compute M(tau) Over Extended Range
# ============================================================================

# The BCS gap Delta(tau) from S74 decreases with tau.
# Beyond the S74 range, extrapolate: Delta(tau) -> 0 for large tau
# (pairing weakens as internal geometry expands).
Delta_spl = CubicSpline(tau_scan_74, Delta_scan, extrapolate=True)  # (local)

# Delta must not go negative; floor at small positive value.
def Delta_ext(tau_val):
    """BCS gap with safe extrapolation."""
    if tau_val <= tau_scan_74[-1]:
        d = float(Delta_spl(tau_val))
    else:
        # Linear extrapolation from last slope
        dDelta_end = float(Delta_spl.derivative()(tau_scan_74[-1]))  # (local)
        d = Delta_scan[-1] + dDelta_end * (tau_val - tau_scan_74[-1])
    return max(d, 1e-4)  # floor to avoid singularity

def compute_M_ATDHFB_full(tau_val):
    """Compute ATDHFB collective mass at given tau (diag + offdiag)."""
    Delta_tau = Delta_ext(tau_val)  # (local)

    # GGE occupations are FROZEN -- u_k, v_k do not change with tau.
    # Only E_k changes through Delta(tau):
    Ek_tau = Delta_tau / (2.0 * uk * vk)  # (local)

    # Diagonal
    M_d = Delta_tau**2 * np.sum(dxi_dtau**2 / Ek_tau**7)  # (local)

    # Off-diagonal
    M_od = 0.0  # (local)
    for k in range(N_modes):
        for l in range(k+1, N_modes):
            eta_kl = uk[k]*vk[l] + vk[k]*uk[l]  # (local)
            h_kl_sq = (Delta_tau * np.sqrt(np.abs(deps_dtau[k]*deps_dtau[l]))
                       / (Ek_tau[k]*Ek_tau[l]))**2  # (local)
            M_od += 2.0 * h_kl_sq * eta_kl**2 / (Ek_tau[k] + Ek_tau[l])**3

    return max(M_d + M_od, 1e-10)

# Compute M(tau) on the full extended grid
M_full = np.array([compute_M_ATDHFB_full(t) for t in tau_full])  # (local)
M_spl = CubicSpline(tau_full, M_full)  # (local)
dM_spl = M_spl.derivative()  # (local)

print(f"\nCollective mass profile (extended):")
print(f"  M(tau_fold) = {M_full[0 + np.argmin(np.abs(tau_full - tau_fold))]:.4f}")
print(f"  M(tau=0.50) = {float(M_spl(0.50)):.4f}")
print(f"  M(tau=1.00) = {float(M_spl(1.00)):.4f}")
print(f"  M(tau=2.00) = {float(M_spl(2.00)):.6e}")
print(f"  M(tau=5.00) = {float(M_spl(5.00)):.6e}")

# ============================================================================
#  SECTION 7: Initial Conditions and Energy Conservation
# ============================================================================

# ---- Initial velocity: two estimates ----
#
# (A) v_terminal from S38: assumes M_ATDHFB = 1.695 (pre-GGE).
#     v = 26.545 M_KK.
#
# (B) Self-consistent with GGE mass: The transit kinetic energy comes from
#     the spectral action gradient doing work over the transit distance:
#       KE = |dS_fold| * delta_tau_transit
#     where delta_tau_transit ~ dt_transit * v ~ small.
#     More precisely: from the spectral action itself.
#     The spectral action drives the transit. At the fold, the force is
#     F = -dS/dtau = -58672.8 M_KK^4. The transit velocity is set by
#     energy conservation:
#       (1/2)*M*v^2 = work done = F * delta_tau
#     From S38: delta_tau = v_terminal * dt_transit ~ 26.5 * 0.00113 ~ 0.030
#     So KE_old = 58672.8 * 0.030 = 1760 M_KK^4
#     With M = 1.695: v_old = sqrt(2*1760/1.695) = 45.6 (but S38 got 26.5 --
#     different because S38 includes friction/dissipation).
#
# (C) Momentum-preserving: If the MOMENTUM p = M_old * v_old is the
#     conserved quantity during the GGE formation (not velocity),
#     then v_new = M_old * v_old / M_new.
#     This is physically motivated: the GGE relic forms DURING the transit,
#     and momentum p = M*v_dot is the generator of tau-translations.
#
# Use approach (C) as the physically self-consistent choice:

fold_idx_full = np.argmin(np.abs(tau_full - tau_fold))  # (local)
M_at_fold = M_full[fold_idx_full]  # (local)

# Momentum from S38 transit
p_transit = M_ATDHFB * v_terminal  # (local) momentum (old M * old v)
v_tau_0_momentum = p_transit / M_at_fold  # (local) self-consistent velocity
v_tau_0_direct = v_terminal  # (local) direct S38 value (for comparison)

# Also compute from force * transit time: v ~ F*dt/M
v_tau_0_force = abs(dS_fold) * dt_transit / M_at_fold  # (local) F*dt/M

print(f"\nInitial velocity estimates:")
print(f"  (A) v_terminal (S38, M={M_ATDHFB:.3f}) = {v_terminal:.4f} M_KK")
print(f"  (B) F*dt/M (force impulse) = {v_tau_0_force:.4f} M_KK")
print(f"  (C) p-conserving: p = {p_transit:.4f}, v = p/M = {v_tau_0_momentum:.4f} M_KK")
print(f"  Using (C): momentum-preserving, self-consistent with GGE mass")

v_tau_0 = v_tau_0_momentum  # (local) self-consistent choice

KE_0 = 0.5 * M_at_fold * v_tau_0**2  # (local)
E_total_0 = KE_0 + V_fold_val  # (local)

print(f"\nInitial conditions (self-consistent):")
print(f"  v_tau(0) = {v_tau_0:.6f} M_KK")
print(f"  M(fold)  = {M_at_fold:.4f} M_KK^{{-2}}")
print(f"  KE_0     = {KE_0:.6f} M_KK^4")
print(f"  V(fold)  = {V_fold_val:.4f} M_KK^4")
print(f"  E_total  = {E_total_0:.6f} M_KK^4")
print(f"  KE/V ratio = {KE_0 / V_fold_val:.4f}")

# Find tau_turn from energy conservation:
#   V_eff(tau_turn) = E_total_0
V_target = E_total_0  # (local)

tau_dense = np.linspace(tau_fold, 10.0, 50000)  # (local)
V_dense = V_eff_spl(tau_dense)  # (local)

crossings = np.where(V_dense >= V_target)[0]  # (local)

if len(crossings) > 0:
    tau_turn_EC = float(tau_dense[crossings[0]])  # (local) energy conservation
    turning_point_found = True  # (local)
    V_at_turn = float(V_eff_spl(tau_turn_EC))  # (local)
    print(f"\n  TURNING POINT (energy conservation):")
    print(f"  tau_turn = {tau_turn_EC:.6f}")
    print(f"  V(tau_turn) = {V_at_turn:.4f}")
    print(f"  Delta_V = {V_at_turn - V_fold_val:.4f}")
else:
    tau_turn_EC = float('inf')  # (local)
    turning_point_found = False  # (local)
    print(f"\n  NO TURNING POINT in [tau_fold, 10.0]")
    print(f"  V_eff(10) = {float(V_eff_spl(10.0)):.1f}")
    print(f"  V_target  = {V_target:.1f}")

# ============================================================================
#  SECTION 8: ODE Integration for Trajectory
# ============================================================================

def eom_rhs(t, y):
    """Equation of motion: M*d^2tau/dt^2 + (1/2)*dM/dtau*v^2 + dV/dtau = 0"""
    tau_val, v_val = y
    tau_c = np.clip(tau_val, tau_full[0], tau_full[-1])  # (local)

    M_val = max(float(M_spl(tau_c)), 1e-10)  # (local)
    dM_val = float(dM_spl(tau_c))  # (local)
    dV_val = float(dV_eff_spl(tau_c))  # (local)

    # Euler-Lagrange: M*a + (1/2)*dM*v^2 + dV = 0
    accel = -(0.5 * dM_val * v_val**2 + dV_val) / M_val  # (local)
    return [v_val, accel]

def v_zero_event(t, y):
    return y[1]
v_zero_event.terminal = True
v_zero_event.direction = -1

t_span_ode = (0, 50.0)  # (local) generous
y0 = [tau_fold, v_tau_0]  # (local)

sol = solve_ivp(eom_rhs, t_span_ode, y0,
                events=v_zero_event,
                max_step=0.005, rtol=1e-10, atol=1e-12,
                method='DOP853')

print(f"\nODE integration:")
print(f"  Status: {sol.message}")
print(f"  Steps: {len(sol.t)}")
print(f"  t_final = {sol.t[-1]:.6f} M_KK^{{-1}}")
print(f"  tau_final = {sol.y[0,-1]:.6f}")
print(f"  v_final = {sol.y[1,-1]:.6f}")

if sol.t_events[0].size > 0:
    tau_turn_ODE = float(sol.y_events[0][0, 0])  # (local)
    t_turn_ODE = float(sol.t_events[0][0])  # (local)
    print(f"  Turning point: tau = {tau_turn_ODE:.6f} at t = {t_turn_ODE:.6f}")
else:
    tau_turn_ODE = float(sol.y[0,-1])  # (local)
    t_turn_ODE = float(sol.t[-1])  # (local)
    print(f"  No turning point; final tau = {tau_turn_ODE:.6f}")

# ============================================================================
#  CHK3: Energy Conservation Along Trajectory
# ============================================================================

E_traj = []  # (local)
for i in range(len(sol.t)):
    tau_i = np.clip(sol.y[0,i], tau_full[0], tau_full[-1])  # (local)
    M_i = float(M_spl(tau_i))  # (local)
    V_i = float(V_eff_spl(tau_i))  # (local)
    E_traj.append(0.5 * M_i * sol.y[1,i]**2 + V_i)
E_traj = np.array(E_traj)  # (local)

E_conserv_err = float(np.max(np.abs(E_traj - E_traj[0])) / np.abs(E_traj[0]))  # (local)

print(f"\n--- CHK3: Energy conservation ---")
print(f"  E_0 = {E_traj[0]:.6f}")
print(f"  E_final = {E_traj[-1]:.6f}")
print(f"  Max relative error = {E_conserv_err:.2e}")
chk3_pass = E_conserv_err < 1e-3  # (local)
print(f"  {'PASS' if chk3_pass else 'FAIL'} (threshold: 1e-3)")

# ============================================================================
#  SECTION 9: Best tau_turn and Gate Verdict
# ============================================================================

# Use energy conservation result (no ODE integration errors) when available.
# The ODE provides the time-domain information.
if turning_point_found:
    tau_turn_best = tau_turn_EC  # (local)
elif sol.t_events[0].size > 0:
    tau_turn_best = tau_turn_ODE  # (local)
else:
    tau_turn_best = float('inf')  # (local)

# If both methods give results, compare:
if turning_point_found and sol.t_events[0].size > 0:
    print(f"\nTurning point comparison:")
    print(f"  Energy conservation: tau = {tau_turn_EC:.6f}")
    print(f"  ODE integration:    tau = {tau_turn_ODE:.6f}")
    print(f"  Difference: {abs(tau_turn_EC - tau_turn_ODE):.6f}")
    # Use energy conservation (analytical, more reliable)
    tau_turn_best = tau_turn_EC

# BCS gap at turning point
Delta_at_turn = Delta_ext(tau_turn_best)  # (local)
M_at_turn = float(M_spl(min(tau_turn_best, tau_full[-1])))  # (local)

print(f"\nResults at turning point:")
print(f"  tau_turn = {tau_turn_best:.6f}")
print(f"  Delta(tau_turn) = {Delta_at_turn:.6f} M_KK")
print(f"  M(tau_turn) = {M_at_turn:.6e} M_KK^{{-2}}")
if sol.t_events[0].size > 0:
    print(f"  Transit time fold->turn = {t_turn_ODE:.6f} M_KK^{{-1}}")

# Gate verdict
print(f"\n{'='*72}")
print(f"GATE: S75-B3-FOLD-STIFFNESS")
print(f"{'='*72}")
print(f"  tau_turn = {tau_turn_best:.6f}")

TAU_PASS_LO = 0.45  # (local)
TAU_PASS_HI = 0.70  # (local)
TAU_INFO_LO = 0.30  # (local)
TAU_INFO_HI = 1.00  # (local)

if not turning_point_found and sol.t_events[0].size == 0:
    verdict = "FAIL"  # (local)
    verdict_msg = "No turning point found"  # (local)
elif TAU_PASS_LO <= tau_turn_best <= TAU_PASS_HI:
    verdict = "PASS"
    verdict_msg = f"tau_turn = {tau_turn_best:.4f} in [{TAU_PASS_LO}, {TAU_PASS_HI}]"
elif TAU_INFO_LO <= tau_turn_best < TAU_PASS_LO:
    verdict = "INFO"
    verdict_msg = f"tau_turn = {tau_turn_best:.4f} in [{TAU_INFO_LO}, {TAU_PASS_LO})"
elif TAU_PASS_HI < tau_turn_best <= TAU_INFO_HI:
    verdict = "INFO"
    verdict_msg = f"tau_turn = {tau_turn_best:.4f} in ({TAU_PASS_HI}, {TAU_INFO_HI}]"
elif tau_turn_best > TAU_INFO_HI:
    verdict = "FAIL"
    verdict_msg = f"tau_turn = {tau_turn_best:.4f} > {TAU_INFO_HI} (overshoot too large)"
elif tau_turn_best < TAU_INFO_LO:
    verdict = "INFO"
    verdict_msg = (f"tau_turn = {tau_turn_best:.4f} < {TAU_INFO_LO} "
                   f"(insufficient overshoot, delta_tau = {tau_turn_best - tau_fold:.4f})")
else:
    verdict = "FAIL"
    verdict_msg = f"tau_turn = {tau_turn_best:.4f} -- outside all bands"

print(f"  Verdict: {verdict}")
print(f"  {verdict_msg}")
print(f"\n--- Cross-checks ---")
print(f"  CHK1 (M > 0):              {'PASS' if chk1_pass else 'FAIL'}")
print(f"  CHK2 (1/Delta^5 scaling):   {'PASS' if chk2_pass else 'FAIL'}")
print(f"  CHK3 (Energy conservation): {'PASS' if chk3_pass else 'FAIL'} (err={E_conserv_err:.2e})")

# ============================================================================
#  SECTION 10: Save Data
# ============================================================================

save_path = os.path.join(base_dir, 's75_fold_stiffness_renorm.npz')

np.savez(save_path,
    gate_name='S75-B3-FOLD-STIFFNESS',
    gate_verdict=verdict,
    tau_turn=tau_turn_best,
    M_fold_ATDHFB=M_fold_total,
    M_diag=M_diag,
    M_offdiag=M_offdiag,
    offdiag_fraction=offdiag_frac,
    M_ATDHFB_canonical=M_ATDHFB,
    M_ratio=M_fold_total / M_ATDHFB,
    Delta_at_fold=Delta_at_fold,
    Delta_at_turn=Delta_at_turn,
    Ek_qp=Ek_qp,
    vk2=vk2,
    uk2=uk2,
    xi_k=xi_k,
    nk_GGE=nk_indep,
    deps_dtau=deps_dtau,
    dxi_dtau=dxi_dtau,
    dlambda_dtau=dlambda_dtau,
    v_tau_0=v_tau_0,
    KE_0=KE_0,
    E_total_0=E_total_0,
    tau_scan=tau_full,
    M_scan=M_full,
    V_eff=V_full,
    t_traj=sol.t,
    tau_traj=sol.y[0],
    v_traj=sol.y[1],
    E_traj=E_traj,
    chk1_M_positive=chk1_pass,
    chk2_cranking_limit=chk2_pass,
    chk3_energy_conservation=chk3_pass,
    chk3_error=E_conserv_err,
)

print(f"\nData saved: {save_path}")

# ============================================================================
#  SECTION 11: Plot
# ============================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# (a) Collective mass
ax = axes[0, 0]
# Only plot the physically meaningful range
plot_mask = tau_full <= 5.0  # (local)
ax.semilogy(tau_full[plot_mask], M_full[plot_mask], 'b-', lw=1.5,
            label='M(tau) [ATDHFB+GGE]')
ax.axhline(M_ATDHFB, color='gray', ls='--', alpha=0.7,
           label=f'M_ATDHFB (S40) = {M_ATDHFB}')
ax.axvline(tau_fold, color='r', ls=':', alpha=0.7, label=f'tau_fold')
if tau_turn_best < 10:
    ax.axvline(tau_turn_best, color='g', ls='--', lw=2,
               label=f'tau_turn = {tau_turn_best:.3f}')
ax.fill_between([TAU_PASS_LO, TAU_PASS_HI],
                [ax.get_ylim()[0]]*2, [ax.get_ylim()[1]]*2 if ax.get_ylim()[1] > 0 else [1e6]*2,
                alpha=0.1, color='green', label='PASS band')  # (local)
ax.set_xlabel('tau')
ax.set_ylabel(r'M(tau) [$M_{KK}^{-2}$]')
ax.set_title('(a) ATDHFB Collective Mass (GGE-modified)')
ax.legend(fontsize=7, loc='upper left')
ax.set_xlim(0.15, 5.0)

# (b) Effective potential with energy level
ax = axes[0, 1]
ax.plot(tau_full[plot_mask], V_full[plot_mask], 'k-', lw=1.5, label=r'$V_{eff}(\tau)$')
ax.axhline(V_target, color='orange', ls='--', lw=1.5,
           label=f'E_total = {V_target:.0f}')
ax.axvline(tau_fold, color='r', ls=':', alpha=0.7)
if tau_turn_best < 10:
    ax.axvline(tau_turn_best, color='g', ls='--', lw=2)
    ax.plot(tau_turn_best, float(V_eff_spl(min(tau_turn_best, tau_full[-1]))),
            'go', ms=8, zorder=5)
ax.fill_betweenx([ax.get_ylim()[0] if ax.get_ylim()[0] > 0 else 1000,
                   max(V_target*1.1, V_full[plot_mask].max())],
                 TAU_PASS_LO, TAU_PASS_HI, alpha=0.1, color='green')
ax.set_xlabel('tau')
ax.set_ylabel(r'$V_{eff}$ [$M_{KK}^4$]')
ax.set_title('(b) Effective Potential + Energy Level')
ax.legend(fontsize=8)
ax.set_xlim(0.15, 5.0)

# (c) Phase space
ax = axes[1, 0]
ax.plot(sol.y[0], sol.y[1], 'b-', lw=1.5)
ax.plot(sol.y[0, 0], sol.y[1, 0], 'rs', ms=8, label='Start (fold)')
if sol.t_events[0].size > 0:
    ax.plot(tau_turn_ODE, 0, 'go', ms=8,
            label=f'Turn (tau={tau_turn_ODE:.3f})')
ax.axhline(0, color='gray', ls='-', alpha=0.3)
ax.axvspan(TAU_PASS_LO, TAU_PASS_HI, alpha=0.1, color='green', label='PASS band')
ax.set_xlabel('tau')
ax.set_ylabel(r'$\dot{\tau}$ [$M_{KK}$]')
ax.set_title('(c) Phase Space Trajectory')
ax.legend(fontsize=8)

# (d) Energy conservation
ax = axes[1, 1]
if len(sol.t) > 1:
    rel_err = (E_traj - E_traj[0]) / np.abs(E_traj[0])  # (local)
    ax.plot(sol.t, rel_err, 'r-', lw=1.5)
    ax.set_xlabel(r't [$M_{KK}^{-1}$]')
    ax.set_ylabel(r'$(E - E_0) / |E_0|$')
    ax.set_title(f'(d) Energy Conservation (max err = {E_conserv_err:.2e})')
    ax.axhline(0, color='gray', ls='--', alpha=0.5)

# Gate verdict banner
color_map = {'PASS': 'lightgreen', 'INFO': 'lightyellow', 'FAIL': 'lightsalmon'}  # (local)
fig.text(0.5, 0.02,
         f'Gate S75-B3-FOLD-STIFFNESS: {verdict} | tau_turn = {tau_turn_best:.4f} | '
         f'M(fold) = {M_fold_total:.3f} | CHK1={chk1_pass} CHK2={chk2_pass} CHK3={chk3_pass}',
         ha='center', fontsize=10, fontweight='bold',
         bbox=dict(boxstyle='round', facecolor=color_map.get(verdict, 'white')))

plt.tight_layout(rect=[0, 0.05, 1, 1])
plot_path = os.path.join(base_dir, 's75_fold_stiffness_renorm.png')
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
print(f"Plot saved: {plot_path}")

print(f"\n{'='*72}")
print(f"DONE. Gate: {verdict}")
print(f"{'='*72}")
