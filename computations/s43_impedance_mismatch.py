#!/usr/bin/env python3
"""
S43 W2-4: Acoustic Impedance Mismatch T(m, delta_tau) at Domain Walls
=====================================================================
Gate: IMP-FILTER-43
  PASS: Impedance filtering produces DR > 3 decades for delta_tau > 0.01
  FAIL: DR < 2 decades for all delta_tau
  INFO: DR between 2-3 decades

Physics:
  At a domain wall where tau changes by delta_tau, the BdG quasiparticle
  masses M*(tau) shift differently for each branch (B2, B1, B3).
  This creates an acoustic impedance mismatch.

  For a massive Klein-Gordon field propagating through a step in M*,
  the transmission coefficient is:
    T(k) = 4 k_1 k_2 / (k_1 + k_2)^2
  where k_1, k_2 are the PROPAGATION wavevectors on each side at the
  SAME energy omega:
    omega^2 = M_1*^2 + k_1^2 = M_2*^2 + k_2^2
    k_2 = sqrt(omega^2 - M_2*^2)

  Evanescent regime: if omega < M_2*, then k_2 is imaginary and T -> 0.

  The BdG masses at the fold are KNOWN from S40:
    M*_B2 = 2.228 M_KK, M*_B1 = 1.138 M_KK, M*_B3 = 0.990 M_KK
  and their tau-derivatives dM*/dtau are KNOWN from S40:
    dM*/dtau computed from deps/dtau and dDelta/dtau.

  We use linearized M*(tau) = M*(fold) + (dM*/dtau)*(tau - tau_fold)
  for small delta_tau (valid since delta_tau in [0.001, 0.10]).
  Cross-check: nonlinear reconstruction from raw eigenvalues.

Author: quantum-acoustics-theorist
Date: 2026-03-14
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

# ============================================================
# 1. LOAD ALL INPUT DATA
# ============================================================
base = Path(r"C:\sandbox\Ainulindale Exflation\tier0-computation")

# S42 fabric dispersion (BdG masses at fold)
fd = np.load(base / "s42_fabric_dispersion.npz", allow_pickle=True)
E_fold = fd['E_fold']       # 8 BdG quasiparticle energies at fold
eps_fold = fd['eps_fold']    # 8 single-particle energies
Delta_fold = fd['Delta_fold'] # 8 BCS gaps

# S42 Hauser-Feshbach
hf = np.load(base / "s42_hauser_feshbach.npz", allow_pickle=True)

# S40 collective inertia (derivatives at fold)
ci = np.load(base / "s40_collective_inertia.npz", allow_pickle=True)
deps_dtau = ci['deps_fold']    # d(eps)/dtau at fold, 8 values
dDelta_dtau = ci['dDelta_fold'] # d(Delta)/dtau at fold, 8 values
G_mod = float(ci['G_mod'])
tau_fold = float(ci['tau_fold_exact'])  # 0.19016

print("=" * 72)
print("S43 W2-4: ACOUSTIC IMPEDANCE MISMATCH AT DOMAIN WALLS")
print("=" * 72)

# ============================================================
# 2. ESTABLISH M*(fold) AND dM*/dtau FROM S40
# ============================================================
print("\n--- 2. QUASIPARTICLE MASSES FROM S40 ---")

# Branch identification
B2_modes = [0, 1, 2, 3]  # flat optical quartet
B1_modes = [4]            # acoustic
B3_modes = [5, 6, 7]     # dispersive optical triplet

# M* at fold (verified from S42 fabric dispersion)
M_fold = E_fold.copy()  # M* = E_k = sqrt(eps^2 + Delta^2) at k=0

# Branch-averaged masses
M1_B2 = np.mean(M_fold[B2_modes])  # 2.228 M_KK
M1_B1 = M_fold[B1_modes[0]]        # 1.138 M_KK
M1_B3 = np.mean(M_fold[B3_modes])  # 0.990 M_KK

# dM*/dtau = (eps * deps + Delta * dDelta) / E
dM_dtau_all = (eps_fold * deps_dtau + Delta_fold * dDelta_dtau) / E_fold

# Branch-averaged derivatives
dM_B2 = np.mean(dM_dtau_all[B2_modes])
dM_B1 = dM_dtau_all[B1_modes[0]]
dM_B3 = np.mean(dM_dtau_all[B3_modes])

print(f"Reference point: tau_fold = {tau_fold:.6f}")
print(f"\nBranch masses at fold:")
print(f"  M*_B2 = {M1_B2:.6f} M_KK  (mean of 4 modes)")
print(f"  M*_B1 = {M1_B1:.6f} M_KK  (single mode)")
print(f"  M*_B3 = {M1_B3:.6f} M_KK  (mean of 3 modes)")
print(f"\nMass derivatives dM*/dtau at fold:")
print(f"  dM*_B2/dtau = {dM_B2:+.6f}")
print(f"  dM*_B1/dtau = {dM_B1:+.6f}")
print(f"  dM*_B3/dtau = {dM_B3:+.6f}")

# Relative sensitivity
alpha_B2 = abs(dM_B2 / M1_B2)
alpha_B1 = abs(dM_B1 / M1_B1)
alpha_B3 = abs(dM_B3 / M1_B3)

print(f"\nRelative mass sensitivity |(dM*/dtau)/M*|:")
print(f"  B2: {alpha_B2:.6f}")
print(f"  B1: {alpha_B1:.6f} (MOST SENSITIVE, {alpha_B1/alpha_B2:.2f}x B2)")
print(f"  B3: {alpha_B3:.6f}")
print(f"  B1/B3 ratio: {alpha_B1/alpha_B3:.2f}")

# Verify S40 fold values
print(f"\nCross-check E = sqrt(eps^2 + Delta^2):")
for i in range(8):
    E_check = np.sqrt(eps_fold[i]**2 + Delta_fold[i]**2)
    branch = "B2" if i in B2_modes else ("B1" if i in B1_modes else "B3")
    print(f"  Mode {i} ({branch}): E_fold={E_fold[i]:.6f}, "
          f"sqrt(eps^2+D^2)={E_check:.6f}, diff={abs(E_fold[i]-E_check):.2e}")

# ============================================================
# 3. LINEARIZED M*(tau) and NONLINEAR CROSS-CHECK
# ============================================================
print("\n--- 3. M*(tau) RECONSTRUCTION ---")

# Linearized: M*(tau) = M*(fold) + dM/dtau * (tau - tau_fold)
# Valid for |delta_tau| << M*/|dM/dtau| ~ 1-2

# Nonlinear cross-check: use the raw eigenvalues at 9 BCS tau points
# (from s27_multisector_bcs) to track how eps(tau) varies.
# The BCS gap Delta(tau) requires the full multi-sector calculation
# (which is the S40 procedure using G_mod=5.0 on the FULL 992-mode
# spectrum, not the 8-mode singlet).
# Since we don't have Delta(tau) at other points, we ALSO linearize Delta.
# This gives: M*(tau) = sqrt((eps + deps*dtau)^2 + (Delta + dDelta*dtau)^2)

# For SMALL delta_tau (which is our regime), both approaches agree.
# Let's verify with second-order terms.

# d2M/dtau2 from chain rule:
# M = sqrt(eps^2 + Delta^2)
# dM/dtau = (eps*deps + Delta*dDelta)/M
# d2M/dtau2 = [(deps^2 + eps*d2eps + dDelta^2 + Delta*d2Delta)*M
#              - (eps*deps + Delta*dDelta)*(dM/dtau)] / M^2
# We don't have d2eps, d2Delta directly. But we can estimate:

# For the linearized approach, the error is O(delta_tau^2 * d2M/dtau2 / 2).
# At delta_tau = 0.1 (our maximum):
# delta_M_linear(B1) ~ |-1.997| * 0.1 = 0.1997
# delta_M_actual: need to estimate curvature.
# From the eigenvalue data: eps_B1 at tau=0.15 is 0.8239, at tau=0.25 is 0.8186
# d2eps/dtau2 ~ (eps(0.25) - 2*eps(0.20) + eps(0.15)) / (0.05)^2
# = (0.8186 - 2*0.8191 + 0.8239) / 0.0025 = 0.0043/0.0025 = 1.72

# Load raw eigenvalues for cross-check
bcs_data = np.load(base / "s27_multisector_bcs.npz", allow_pickle=True)
tau_bcs = bcs_data['tau_values']  # [0, 0.1, 0.15, 0.2, 0.25, 0.3, ...]

eps_B1_at_bcs = np.zeros(len(tau_bcs))
eps_B2_at_bcs = np.zeros(len(tau_bcs))
eps_B3_at_bcs = np.zeros(len(tau_bcs))

for t_idx in range(len(tau_bcs)):
    evals = bcs_data[f'evals_0_0_{t_idx}']
    pos = np.sort(evals[evals > 0])
    eps_B1_at_bcs[t_idx] = pos[0]
    eps_B2_at_bcs[t_idx] = pos[1]
    eps_B3_at_bcs[t_idx] = pos[5]

# Curvature of eps at fold (numerical 2nd derivative)
# tau = [0.15, 0.20, 0.25] gives centered difference at tau=0.20
dtau_fd = 0.05
d2eps_B1 = (eps_B1_at_bcs[4] - 2*eps_B1_at_bcs[3] + eps_B1_at_bcs[2]) / dtau_fd**2
d2eps_B2 = (eps_B2_at_bcs[4] - 2*eps_B2_at_bcs[3] + eps_B2_at_bcs[2]) / dtau_fd**2
d2eps_B3 = (eps_B3_at_bcs[4] - 2*eps_B3_at_bcs[3] + eps_B3_at_bcs[2]) / dtau_fd**2

print(f"\nSingle-particle curvature d2eps/dtau2 at fold:")
print(f"  B1: {d2eps_B1:.4f} (eps has minimum near fold)")
print(f"  B2: {d2eps_B2:.4f}")
print(f"  B3: {d2eps_B3:.4f}")
print(f"\nLinearization error at delta_tau = 0.10:")
print(f"  delta_eps_B1 (2nd order) ~ {0.5 * abs(d2eps_B1) * 0.1**2:.6f}")
print(f"  delta_eps_B1 (1st order) ~ {abs(deps_dtau[4]) * 0.1:.6f}")
if abs(deps_dtau[4]) > 1e-10:
    print(f"  Fractional error ~ {0.5 * abs(d2eps_B1) * 0.1 / abs(deps_dtau[4]):.2f}")

# ============================================================
# 4. IMPEDANCE MISMATCH TRANSMISSION COEFFICIENT
# ============================================================
print("\n--- 4. IMPEDANCE MISMATCH COMPUTATION ---")

# Physics of transmission through a mass step (Klein-Gordon):
# omega^2 = M_1^2 + k_1^2 = M_2^2 + k_2^2
# T = 4 k_1 k_2 / (k_1 + k_2)^2
# If omega < M_2: evanescent (T -> 0 for sharp step)

delta_tau_values = np.array([0.001, 0.005, 0.01, 0.02, 0.05, 0.10])
k_values = np.linspace(0.01, 10.0, 500)

# For each delta_tau, compute M* on side 2 using LINEARIZATION from S40 fold:
# M*(tau_fold + dtau) = sqrt((eps + deps*dtau)^2 + (Delta + dDelta*dtau)^2)
# This is BETTER than simple M + dM*dtau because it preserves the BdG structure.

def compute_M2(i_mode, dtau):
    """Compute BdG mass for mode i at tau_fold + dtau using linearized BdG."""
    eps_2 = eps_fold[i_mode] + deps_dtau[i_mode] * dtau
    Delta_2 = Delta_fold[i_mode] + dDelta_dtau[i_mode] * dtau
    # Gap cannot go negative (physical constraint)
    Delta_2 = max(abs(Delta_2), 0.0)
    return np.sqrt(eps_2**2 + Delta_2**2)

def transmission_KG(M1, M2, k):
    """Klein-Gordon transmission through a mass step."""
    omega_sq = M1**2 + k**2
    k2_sq = omega_sq - M2**2
    if k2_sq > 0:
        k2 = np.sqrt(k2_sq)
        return 4 * k * k2 / (k + k2)**2
    else:
        return 0.0  # total reflection (sharp step)

def transmission_KG_tunnel(M1, M2, k, d_wall):
    """Klein-Gordon transmission including tunneling through finite wall."""
    omega_sq = M1**2 + k**2
    k2_sq = omega_sq - M2**2
    if k2_sq > 0:
        k2 = np.sqrt(k2_sq)
        return 4 * k * k2 / (k + k2)**2
    else:
        kappa = np.sqrt(-k2_sq)
        DM_sq = abs(M2**2 - M1**2)
        if DM_sq < 1e-15 or k < 1e-15:
            return 0.0
        prefactor = (DM_sq / (4 * k * kappa))**2
        sinh_val = np.sinh(kappa * d_wall)
        return 1.0 / (1.0 + prefactor * sinh_val**2)


# Natural wall width from tau modulus mass
m_tau = 2.06238706  # from C-FABRIC-42
d_wall_natural = 1.0 / m_tau  # 0.485 M_KK^{-1}
print(f"Natural wall width: d_wall = 1/m_tau = {d_wall_natural:.4f} M_KK^-1")

# Storage
T_B2 = np.zeros((len(delta_tau_values), len(k_values)))
T_B1 = np.zeros((len(delta_tau_values), len(k_values)))
T_B3 = np.zeros((len(delta_tau_values), len(k_values)))

# With tunneling
T_B2_tun = np.zeros((len(delta_tau_values), len(k_values)))
T_B1_tun = np.zeros((len(delta_tau_values), len(k_values)))
T_B3_tun = np.zeros((len(delta_tau_values), len(k_values)))

print(f"\n{'dtau':>8} | {'M2_B2':>8} {'M2_B1':>8} {'M2_B3':>8} | "
      f"{'dM_B2':>8} {'dM_B1':>8} {'dM_B3':>8}")
print("-" * 75)

for d_idx, dtau in enumerate(delta_tau_values):
    # Compute M2 for each branch using BdG linearization
    # Use representative mode from each branch
    M2_B2 = compute_M2(0, dtau)  # mode 0 (B2 representative)
    M2_B1 = compute_M2(4, dtau)  # mode 4 (B1)
    M2_B3 = compute_M2(5, dtau)  # mode 5 (B3 representative)

    dM_b2 = M2_B2 - M1_B2
    dM_b1 = M2_B1 - M1_B1
    dM_b3 = M2_B3 - M1_B3

    print(f"{dtau:>8.3f} | {M2_B2:>8.5f} {M2_B1:>8.5f} {M2_B3:>8.5f} | "
          f"{dM_b2:>+8.5f} {dM_b1:>+8.5f} {dM_b3:>+8.5f}")

    for k_idx, k in enumerate(k_values):
        # Sharp step (no tunneling)
        T_B2[d_idx, k_idx] = transmission_KG(M1_B2, M2_B2, k)
        T_B1[d_idx, k_idx] = transmission_KG(M1_B1, M2_B1, k)
        T_B3[d_idx, k_idx] = transmission_KG(M1_B3, M2_B3, k)

        # With tunneling
        T_B2_tun[d_idx, k_idx] = transmission_KG_tunnel(M1_B2, M2_B2, k, d_wall_natural)
        T_B1_tun[d_idx, k_idx] = transmission_KG_tunnel(M1_B1, M2_B1, k, d_wall_natural)
        T_B3_tun[d_idx, k_idx] = transmission_KG_tunnel(M1_B3, M2_B3, k, d_wall_natural)

# ============================================================
# 5. TRANSMISSION AT REFERENCE k VALUES
# ============================================================
print("\n--- 5. TRANSMISSION COEFFICIENTS ---")

k_ref_values = [0.1, 0.5, 1.0, 2.0, 5.0, 10.0]
print(f"\nSharp step T(k) at selected momenta (no tunneling):")
print(f"{'dtau':>8} | ", end="")
for kr in k_ref_values:
    print(f"{'k='+str(kr):>24}", end="")
print()
print(f"{'':>8} | ", end="")
for kr in k_ref_values:
    print(f"{'B2':>8}{'B1':>8}{'B3':>8}", end="")
print()
print("-" * (10 + 24*len(k_ref_values)))

for d_idx, dtau in enumerate(delta_tau_values):
    print(f"{dtau:>8.3f} | ", end="")
    for kr in k_ref_values:
        k_idx = np.argmin(np.abs(k_values - kr))
        tb2 = T_B2[d_idx, k_idx]
        tb1 = T_B1[d_idx, k_idx]
        tb3 = T_B3[d_idx, k_idx]
        print(f"{tb2:>8.5f}{tb1:>8.5f}{tb3:>8.5f}", end="")
    print()

# ============================================================
# 6. EVANESCENT THRESHOLDS
# ============================================================
print("\n--- 6. EVANESCENT THRESHOLDS ---")

print(f"\nMinimum propagating k (below which T=0 for sharp step):")
print(f"{'dtau':>8} | {'k_min_B2':>10} {'k_min_B1':>10} {'k_min_B3':>10} | "
      f"{'B1 direction':>12}")
print("-" * 65)

for d_idx, dtau in enumerate(delta_tau_values):
    M2_B2 = compute_M2(0, dtau)
    M2_B1 = compute_M2(4, dtau)
    M2_B3 = compute_M2(5, dtau)

    def k_threshold(M1, M2):
        """Minimum k for propagation through the step."""
        # omega = sqrt(M1^2 + k^2) must exceed M2
        # k > sqrt(M2^2 - M1^2) if M2 > M1, else k > 0
        if M2 > M1:
            return np.sqrt(M2**2 - M1**2)
        else:
            return 0.0

    km_B2 = k_threshold(M1_B2, M2_B2)
    km_B1 = k_threshold(M1_B1, M2_B1)
    km_B3 = k_threshold(M1_B3, M2_B3)

    # B1 has dM/dtau < 0, so M2_B1 < M1_B1 for dtau > 0
    # => B1 always propagates forward (k_min = 0)
    direction = "M DECREASES" if M2_B1 < M1_B1 else "M INCREASES"

    print(f"{dtau:>8.3f} | {km_B2:>10.6f} {km_B1:>10.6f} {km_B3:>10.6f} | "
          f"{direction:>12}")

# ============================================================
# 7. DYNAMIC RANGE ANALYSIS
# ============================================================
print("\n--- 7. DYNAMIC RANGE (SINGLE WALL) ---")

# DR = log10(T_max / T_min) across the 3 branches at each (dtau, k)
DR_sharp = np.zeros((len(delta_tau_values), len(k_values)))
DR_tunnel = np.zeros((len(delta_tau_values), len(k_values)))

for d_idx in range(len(delta_tau_values)):
    for k_idx in range(len(k_values)):
        # Sharp step
        t_vals = np.array([T_B2[d_idx, k_idx], T_B1[d_idx, k_idx], T_B3[d_idx, k_idx]])
        t_prop = t_vals[t_vals > 0]
        if len(t_prop) >= 2:
            DR_sharp[d_idx, k_idx] = np.log10(t_prop.max() / t_prop.min())
        elif len(t_prop) == 1 and np.any(t_vals == 0):
            # One evanescent => effectively infinite DR at sharp step
            # But quantify as T_prop / T_evan where T_evan ~ 0
            DR_sharp[d_idx, k_idx] = 10.0  # cap at 10 decades for plotting

        # With tunneling
        t_vals_t = np.array([T_B2_tun[d_idx, k_idx], T_B1_tun[d_idx, k_idx],
                            T_B3_tun[d_idx, k_idx]])
        t_nonzero = t_vals_t[t_vals_t > 1e-30]
        if len(t_nonzero) >= 2:
            DR_tunnel[d_idx, k_idx] = np.log10(t_nonzero.max() / t_nonzero.min())
        else:
            DR_tunnel[d_idx, k_idx] = 0.0

print(f"\nDynamic range [decades] at selected k (SHARP STEP):")
print(f"{'dtau':>8} | {'k=0.1':>8} {'k=0.5':>8} {'k=1.0':>8} {'k=2.0':>8} {'k=5.0':>8} | "
      f"{'max DR':>8} {'k@max':>8}")
print("-" * 80)

DR_max_sharp = np.zeros(len(delta_tau_values))
k_at_max_sharp = np.zeros(len(delta_tau_values))

for d_idx, dtau in enumerate(delta_tau_values):
    k_refs = [0.1, 0.5, 1.0, 2.0, 5.0]
    dr_at_refs = []
    for kr in k_refs:
        idx = np.argmin(np.abs(k_values - kr))
        dr_at_refs.append(DR_sharp[d_idx, idx])

    # Find max DR (cap at 10)
    max_dr = np.min([np.max(DR_sharp[d_idx, :]), 10.0])
    max_k = k_values[np.argmax(DR_sharp[d_idx, :])]
    DR_max_sharp[d_idx] = max_dr
    k_at_max_sharp[d_idx] = max_k

    print(f"{dtau:>8.3f} | "
          f"{dr_at_refs[0]:>8.4f} {dr_at_refs[1]:>8.4f} {dr_at_refs[2]:>8.4f} "
          f"{dr_at_refs[3]:>8.4f} {dr_at_refs[4]:>8.4f} | "
          f"{max_dr:>8.4f} {max_k:>8.3f}")

print(f"\nDynamic range [decades] at selected k (WITH TUNNELING, d={d_wall_natural:.3f}):")
print(f"{'dtau':>8} | {'k=0.1':>8} {'k=0.5':>8} {'k=1.0':>8} {'k=2.0':>8} {'k=5.0':>8} | "
      f"{'max DR':>8} {'k@max':>8}")
print("-" * 80)

DR_max_tunnel = np.zeros(len(delta_tau_values))
k_at_max_tunnel = np.zeros(len(delta_tau_values))

for d_idx, dtau in enumerate(delta_tau_values):
    k_refs = [0.1, 0.5, 1.0, 2.0, 5.0]
    dr_at_refs = []
    for kr in k_refs:
        idx = np.argmin(np.abs(k_values - kr))
        dr_at_refs.append(DR_tunnel[d_idx, idx])

    max_dr = np.max(DR_tunnel[d_idx, :])
    max_k = k_values[np.argmax(DR_tunnel[d_idx, :])]
    DR_max_tunnel[d_idx] = max_dr
    k_at_max_tunnel[d_idx] = max_k

    print(f"{dtau:>8.3f} | "
          f"{dr_at_refs[0]:>8.4f} {dr_at_refs[1]:>8.4f} {dr_at_refs[2]:>8.4f} "
          f"{dr_at_refs[3]:>8.4f} {dr_at_refs[4]:>8.4f} | "
          f"{max_dr:>8.4f} {max_k:>8.3f}")

# ============================================================
# 8. WHY DR IS LARGE AT LOW k (SHARP STEP ARTIFACT)
# ============================================================
print("\n--- 8. EVANESCENT CHANNEL ANALYSIS ---")

# At low k, the B2 threshold is higher than B3 threshold because
# dM_B2/dtau > 0 (mass increases). For dtau=0.05:
# M2_B2 = 2.228 + 1.27*0.05 = 2.292 (increases)
# M2_B1 = 1.138 - 2.00*0.05 = 1.038 (decreases!)
# M2_B3 = 0.990 + 0.52*0.05 = 1.016 (increases)
#
# The thresholds for evanescent regime:
# k_min_B2 = sqrt(M2_B2^2 - M1_B2^2) = sqrt(2.292^2 - 2.228^2)
#          = sqrt(5.253 - 4.964) = sqrt(0.289) = 0.538
# k_min_B1 = 0 (M2 < M1, always propagates)
# k_min_B3 = sqrt(M2_B3^2 - M1_B3^2) = sqrt(1.032 - 0.980) = sqrt(0.052) = 0.228
#
# At k between 0.228 and 0.538:
#   B3 is evanescent (T=0 for sharp step)
#   B1 propagates (T~1)
#   B2 is evanescent (T=0 for sharp step)
# DR = infinity (sharp step) or very large (tunneling)
#
# BUT: this is the EVANESCENT regime, not the propagating regime.
# In the evanescent regime, the "dynamic range" is between tunneling
# and propagating modes.  This is physically meaningful ONLY if
# the quasiparticles actually have momenta in this range.

print(f"\nExample at delta_tau = 0.05:")
M2_B2_ex = compute_M2(0, 0.05)
M2_B1_ex = compute_M2(4, 0.05)
M2_B3_ex = compute_M2(5, 0.05)

print(f"  M1_B2 = {M1_B2:.4f} -> M2_B2 = {M2_B2_ex:.4f} (delta = {M2_B2_ex-M1_B2:+.4f})")
print(f"  M1_B1 = {M1_B1:.4f} -> M2_B1 = {M2_B1_ex:.4f} (delta = {M2_B1_ex-M1_B1:+.4f})")
print(f"  M1_B3 = {M1_B3:.4f} -> M2_B3 = {M2_B3_ex:.4f} (delta = {M2_B3_ex-M1_B3:+.4f})")

km_B2_ex = np.sqrt(max(M2_B2_ex**2 - M1_B2**2, 0))
km_B3_ex = np.sqrt(max(M2_B3_ex**2 - M1_B3**2, 0))

print(f"\n  Evanescent thresholds:")
print(f"    B2: k < {km_B2_ex:.4f} M_KK -> evanescent")
print(f"    B1: always propagating (M decreases)")
print(f"    B3: k < {km_B3_ex:.4f} M_KK -> evanescent")
print(f"\n  Critical window: k in [{km_B3_ex:.3f}, {km_B2_ex:.3f}]:")
print(f"    B1 propagates (T~1), B2 and B3 evanescent")
print(f"    DR in this window is set by tunneling rate")

# ============================================================
# 9. PROPAGATING-REGIME DYNAMIC RANGE
# ============================================================
print("\n--- 9. PROPAGATING-REGIME DR (ALL MODES ABOVE THRESHOLD) ---")

# The physically relevant DR is at k > max(k_min_B2, k_min_B3)
# where ALL 3 modes propagate.
# In this regime, T ~ 1 - epsilon for all modes, and DR is tiny.

print(f"\nDR above all thresholds (k > k_min_max):")
print(f"{'dtau':>8} | {'k_min_max':>10} | {'DR(k_min+0.1)':>14} {'DR(k=1)':>10} "
      f"{'DR(k=5)':>10} {'DR(k=10)':>10}")
print("-" * 75)

for d_idx, dtau in enumerate(delta_tau_values):
    M2_B2 = compute_M2(0, dtau)
    M2_B1 = compute_M2(4, dtau)
    M2_B3 = compute_M2(5, dtau)

    km_B2 = np.sqrt(max(M2_B2**2 - M1_B2**2, 0))
    km_B3 = np.sqrt(max(M2_B3**2 - M1_B3**2, 0))
    km_B1 = np.sqrt(max(M2_B1**2 - M1_B1**2, 0))
    k_min_max = max(km_B2, km_B3, km_B1)

    k_test_vals = [k_min_max + 0.1, 1.0, 5.0, 10.0]
    dr_vals = []
    for kt in k_test_vals:
        if kt < k_values[0] or kt > k_values[-1]:
            dr_vals.append(0.0)
            continue
        k_idx = np.argmin(np.abs(k_values - kt))
        t_vals = np.array([T_B2[d_idx, k_idx], T_B1[d_idx, k_idx], T_B3[d_idx, k_idx]])
        t_prop = t_vals[t_vals > 0]
        if len(t_prop) >= 2:
            dr_vals.append(np.log10(t_prop.max() / t_prop.min()))
        else:
            dr_vals.append(0.0)

    print(f"{dtau:>8.3f} | {k_min_max:>10.4f} | {dr_vals[0]:>14.6f} {dr_vals[1]:>10.6f} "
          f"{dr_vals[2]:>10.6f} {dr_vals[3]:>10.6f}")

# ============================================================
# 10. ANALYTICAL FORMULA FOR PROPAGATING-REGIME DR
# ============================================================
print("\n--- 10. ANALYTICAL DR IN PROPAGATING REGIME ---")

# For k >> delta_M (all modes propagating, T ~ 1):
# T = 4 k k_2 / (k + k_2)^2
# k_2 = sqrt(k^2 + M1^2 - M2^2) ~ k * sqrt(1 + (M1^2 - M2^2)/k^2)
#      ~ k + (M1^2 - M2^2)/(2k)     for k >> |delta_M|
# k_2 - k ~ (M1^2 - M2^2)/(2k) = delta(M^2)/(2k)
# Let q = (k - k_2)/(k + k_2), then R = q^2, T = 1 - R = 1 - q^2
# q ~ delta(M^2) / (4 k^2)   for k >> delta_M
# R ~ [delta(M^2)]^2 / (16 k^4)
#
# For mode i: delta(M_i^2) = M_2i^2 - M_1i^2 ~ 2 M_1i * dM_i/dtau * dtau
# R_i ~ [2 M_i * (dM_i/dtau) * dtau]^2 / (16 k^4)
#      = [M_i * (dM_i/dtau)]^2 * dtau^2 / (4 k^4)
#
# DR = log10(R_max / R_min) = log10( [M_max * dM_max]^2 / [M_min * dM_min]^2 )
#    = 2 * log10( |M_max * dM_max| / |M_min * dM_min| )
# This is INDEPENDENT of k and dtau (in the propagating regime)!

product_B2 = abs(M1_B2 * dM_B2)
product_B1 = abs(M1_B1 * dM_B1)
product_B3 = abs(M1_B3 * dM_B3)

print(f"|M * dM/dtau| products:")
print(f"  B2: |{M1_B2:.4f} * {dM_B2:+.4f}| = {product_B2:.4f}")
print(f"  B1: |{M1_B1:.4f} * {dM_B1:+.4f}| = {product_B1:.4f}")
print(f"  B3: |{M1_B3:.4f} * {dM_B3:+.4f}| = {product_B3:.4f}")

products = np.array([product_B2, product_B1, product_B3])
DR_analytic = 2 * np.log10(products.max() / products.min())

print(f"\nAnalytical DR (propagating regime, k >> delta_M):")
print(f"  DR = 2 * log10({products.max():.4f} / {products.min():.4f})")
print(f"  DR = {DR_analytic:.4f} decades")
print(f"  This is the ASYMPTOTIC DR, independent of k and delta_tau")

# Verify numerically at k=10, dtau=0.05:
d5_idx = np.argmin(np.abs(delta_tau_values - 0.05))
k10_idx = np.argmin(np.abs(k_values - 10.0))
R_B2 = 1 - T_B2[d5_idx, k10_idx]
R_B1 = 1 - T_B1[d5_idx, k10_idx]
R_B3 = 1 - T_B3[d5_idx, k10_idx]
print(f"\nNumerical check at k=10, dtau=0.05:")
print(f"  R_B2 = {R_B2:.6e}, R_B1 = {R_B1:.6e}, R_B3 = {R_B3:.6e}")
if min(R_B2, R_B1, R_B3) > 0:
    DR_num = np.log10(max(R_B2, R_B1, R_B3) / min(R_B2, R_B1, R_B3))
    print(f"  DR_numerical = {DR_num:.4f} decades")
    print(f"  DR_analytical = {DR_analytic:.4f} decades")
    print(f"  Agreement: {abs(DR_num - DR_analytic) / DR_analytic * 100:.1f}%")

# ============================================================
# 11. ASYMMETRIC DIRECTION (tau decreasing)
# ============================================================
print("\n--- 11. DIRECTIONAL ASYMMETRY ---")

T_rev_B2 = np.zeros((len(delta_tau_values), len(k_values)))
T_rev_B1 = np.zeros((len(delta_tau_values), len(k_values)))
T_rev_B3 = np.zeros((len(delta_tau_values), len(k_values)))

for d_idx, dtau in enumerate(delta_tau_values):
    M2_B2 = compute_M2(0, -dtau)  # reverse direction
    M2_B1 = compute_M2(4, -dtau)
    M2_B3 = compute_M2(5, -dtau)

    for k_idx, k in enumerate(k_values):
        T_rev_B2[d_idx, k_idx] = transmission_KG(M1_B2, M2_B2, k)
        T_rev_B1[d_idx, k_idx] = transmission_KG(M1_B1, M2_B1, k)
        T_rev_B3[d_idx, k_idx] = transmission_KG(M1_B3, M2_B3, k)

print(f"\nDirectional asymmetry T(+dtau)/T(-dtau) at k = 1.0 M_KK:")
k1_idx = np.argmin(np.abs(k_values - 1.0))
print(f"{'dtau':>8} | {'B2 fwd':>8} {'B2 rev':>8} {'B2 asym':>8} | "
      f"{'B1 fwd':>8} {'B1 rev':>8} {'B1 asym':>8} | "
      f"{'B3 fwd':>8} {'B3 rev':>8} {'B3 asym':>8}")
print("-" * 100)

for d_idx, dtau in enumerate(delta_tau_values):
    tb2f = T_B2[d_idx, k1_idx]
    tb2r = T_rev_B2[d_idx, k1_idx]
    tb1f = T_B1[d_idx, k1_idx]
    tb1r = T_rev_B1[d_idx, k1_idx]
    tb3f = T_B3[d_idx, k1_idx]
    tb3r = T_rev_B3[d_idx, k1_idx]

    a_b2 = tb2f / tb2r if tb2r > 1e-30 else float('inf')
    a_b1 = tb1f / tb1r if tb1r > 1e-30 else float('inf')
    a_b3 = tb3f / tb3r if tb3r > 1e-30 else float('inf')

    print(f"{dtau:>8.3f} | {tb2f:>8.6f} {tb2r:>8.6f} {a_b2:>8.4f} | "
          f"{tb1f:>8.6f} {tb1r:>8.6f} {a_b1:>8.4f} | "
          f"{tb3f:>8.6f} {tb3r:>8.6f} {a_b3:>8.4f}")

# ============================================================
# 12. CUMULATIVE FILTERING
# ============================================================
print("\n--- 12. CUMULATIVE FILTERING ---")

N_walls_list = [3, 10, 30, 100]

# At k=1.0, delta_tau=0.05:
print(f"\nCumulative T^N at k = 1.0, delta_tau = 0.05:")
print(f"{'N':>6} | {'T_B2^N':>12} {'T_B1^N':>12} {'T_B3^N':>12} | {'DR_cum':>10}")
print("-" * 65)

d5_idx = np.argmin(np.abs(delta_tau_values - 0.05))
t_b2_k1 = T_B2[d5_idx, k1_idx]
t_b1_k1 = T_B1[d5_idx, k1_idx]
t_b3_k1 = T_B3[d5_idx, k1_idx]

DR_cum_30 = 0.0
for N in N_walls_list:
    tn_b2 = t_b2_k1**N
    tn_b1 = t_b1_k1**N
    tn_b3 = t_b3_k1**N

    vals = np.array([tn_b2, tn_b1, tn_b3])
    vals_pos = vals[vals > 1e-30]
    if len(vals_pos) >= 2:
        dr_c = np.log10(vals_pos.max() / vals_pos.min())
    else:
        dr_c = 0.0

    if N == 30:
        DR_cum_30 = dr_c

    print(f"{N:>6} | {tn_b2:>12.6e} {tn_b1:>12.6e} {tn_b3:>12.6e} | {dr_c:>10.4f}")

# Near threshold at k=0.3 (between B3 and B2 thresholds):
print(f"\nCumulative at k = 0.3, delta_tau = 0.05 (near B3 threshold):")
k03_idx = np.argmin(np.abs(k_values - 0.3))
t_b2_k03 = T_B2[d5_idx, k03_idx]
t_b1_k03 = T_B1[d5_idx, k03_idx]
t_b3_k03 = T_B3[d5_idx, k03_idx]

print(f"  T_B2(k=0.3) = {t_b2_k03:.6e} ({'propagating' if t_b2_k03 > 0 else 'evanescent'})")
print(f"  T_B1(k=0.3) = {t_b1_k03:.6e} ({'propagating' if t_b1_k03 > 0 else 'evanescent'})")
print(f"  T_B3(k=0.3) = {t_b3_k03:.6e} ({'propagating' if t_b3_k03 > 0 else 'evanescent'})")

# ============================================================
# 13. IMPEDANCE-WEIGHTED BRANCHING RATIO vs HF
# ============================================================
print("\n--- 13. BRANCHING RATIO COMPARISON ---")

# From HF-KK-42: sector DR = 1.51 decades, doorway DR = 3.20
# Can impedance filtering improve this?

print(f"\nDegeneracy-weighted branching ratios at k = 1.0:")
print(f"{'dtau':>8} | {'BR_B2':>8} {'BR_B1':>8} {'BR_B3':>8} | "
      f"{'Selectivity':>12} {'HF ratio':>10}")
print("-" * 65)

for d_idx, dtau in enumerate(delta_tau_values):
    t_b2 = T_B2[d_idx, k1_idx]
    t_b1 = T_B1[d_idx, k1_idx]
    t_b3 = T_B3[d_idx, k1_idx]

    flux_b2 = 4 * t_b2
    flux_b1 = 1 * t_b1
    flux_b3 = 3 * t_b3
    total = flux_b2 + flux_b1 + flux_b3

    if total > 0:
        br_b2 = flux_b2 / total
        br_b1 = flux_b1 / total
        br_b3 = flux_b3 / total
    else:
        br_b2 = br_b1 = br_b3 = 0

    brs = np.array([br_b2, br_b1, br_b3])
    brs_pos = brs[brs > 1e-30]
    sel = np.log10(brs_pos.max() / brs_pos.min()) if len(brs_pos) >= 2 else 0

    print(f"{dtau:>8.3f} | {br_b2:>8.4f} {br_b1:>8.4f} {br_b3:>8.4f} | "
          f"{sel:>12.4f} {'':>2}{sel/1.51:>8.2f}x")

# ============================================================
# 14. GATE VERDICT: IMP-FILTER-43
# ============================================================
print("\n" + "=" * 72)
print("GATE VERDICT: IMP-FILTER-43")
print("=" * 72)

# The gate asks: does impedance filtering produce DR > 3 decades
# for delta_tau > 0.01?

# Two regimes:
# A. Propagating (k >> k_threshold): DR ~ 0.88 decades (analytic, asymptotic)
#    This is the STRUCTURAL limit. Cannot exceed it regardless of dtau.
# B. Evanescent/propagating boundary: DR can be arbitrarily large at
#    the sharp-step level, but tunneling limits it for finite-width walls.

# The physically relevant DR depends on the quasiparticle momentum spectrum.
# For GGE quasiparticles (created by sudden quench at the fold):
# - Average energy per pair: E_per_pair ~ 0.85 M_KK (from S42)
# - Typical k ~ sqrt(E_per_pair^2 - M*^2) ~ O(1) M_KK for B3, O(0) for B2
# - B2 quasiparticles are nearly at rest (Delta >> eps)
# - The relevant k range is O(0.1 - 1) M_KK

# In the evanescent window (k ~ 0.1-0.5), the DR CAN be large for sharp steps.
# But the NATURAL wall width d = 0.485 M_KK^{-1} limits tunneling.

# The maximum single-wall DR with tunneling:
mask_dtau = delta_tau_values >= 0.01
DR_relevant = DR_max_tunnel[mask_dtau] if np.any(mask_dtau) else np.array([0])
max_DR = np.max(DR_relevant)
dtau_best = delta_tau_values[mask_dtau][np.argmax(DR_relevant)]

# For the sharp-step case:
DR_sharp_relevant = DR_max_sharp[mask_dtau]
max_DR_sharp = np.max(DR_sharp_relevant)

print(f"\nKey results:")
print(f"  PROPAGATING regime DR (analytical, k-independent): {DR_analytic:.4f} decades")
print(f"  Max single-wall DR (sharp step, dtau >= 0.01): {max_DR_sharp:.4f} decades")
print(f"    (at dtau = {delta_tau_values[mask_dtau][np.argmax(DR_sharp_relevant)]:.3f}, "
      f"k = {k_at_max_sharp[mask_dtau][np.argmax(DR_sharp_relevant)]:.3f})")
print(f"  Max single-wall DR (with tunneling, dtau >= 0.01): {max_DR:.4f} decades")
print(f"    (at dtau = {dtau_best:.3f}, k = {k_at_max_tunnel[np.argmax(DR_relevant)]:.3f})")
print(f"  Cumulative DR (N=30, dtau=0.05, k=1): {DR_cum_30:.4f} decades")
print(f"  HF-KK-42 sector DR: 1.51 decades")
print(f"  HF-KK-42 doorway preference: 3.20")

# Sharp step allows infinite DR at the threshold
# But with tunneling + natural wall width, it's finite
# The propagating-regime asymptotic DR = 0.88 is the structural limit

# Gate classification:
# The sharp-step case gives DR = 10 (capped) at the threshold -> PASS
# But this is artificial: at the threshold, T_evanescent = 0 exactly
# This is not "filtering" -- it's a mass gap.

# The HONEST answer: In the propagating regime where all modes
# transmit, DR = 0.88 decades (STRUCTURAL). This is < 2 decades -> FAIL.

# In the evanescent regime, one mode is blocked and another propagates.
# This IS mass-dependent filtering, but it's essentially "above gap vs below gap"
# -- which is the same as the mass gap itself, not impedance mismatch.

# The impedance mismatch ADDS 0.88 decades on top of whatever the mass gap provides.
# The mass gap itself (from B3 lightest to B2 heaviest: 2.228/0.990 = 2.25)
# gives log10(2.25) = 0.35 decades of mass hierarchy.

print(f"\n  Mass hierarchy: M*_B2/M*_B3 = {M1_B2/M1_B3:.3f} = {np.log10(M1_B2/M1_B3):.3f} decades")
print(f"  Combined (mass gap + impedance): ~{np.log10(M1_B2/M1_B3) + DR_analytic:.3f} decades")

# VERDICT:
# Propagating-regime DR = 0.88 < 2.0 decades
# No single mechanism at a single wall achieves 3 decades
# Even cumulative (30 walls) gives only 0.004 decades at k=1

if max_DR > 3.0:
    verdict = "PASS"
elif max_DR < 2.0:
    # Check if sharp-step threshold physics counts
    if max_DR_sharp >= 3.0:
        # Sharp step gives 3+ decades only at k = threshold (measure zero)
        # This is the mass gap effect, not impedance filtering
        verdict = "FAIL"
        note = "(sharp-step threshold gives large DR but only at measure-zero k)"
    else:
        verdict = "FAIL"
        note = ""
else:
    verdict = "INFO"
    note = ""

print(f"\n  IMP-FILTER-43: {verdict}")
if note:
    print(f"  Note: {note}")

# ============================================================
# 15. PHYSICAL INTERPRETATION
# ============================================================
print("\n--- 15. PHYSICAL INTERPRETATION ---")
print(f"""
The impedance mismatch at a tau-step domain wall produces WEAK mass-
dependent filtering in the propagating regime.  The structural limit
is DR = {DR_analytic:.2f} decades, set by the ratio:

  max|M * dM/dtau| / min|M * dM/dtau| = {products.max():.3f} / {products.min():.3f} = {products.max()/products.min():.2f}

This ratio is INDEPENDENT of k and delta_tau (it cancels in the
high-k limit of the transmission formula).

Key physics:
  1. B1 has the LARGEST sensitivity: |(dM*/dtau)/M*| = {alpha_B1:.4f}
     ({alpha_B1/alpha_B2:.1f}x B2, {alpha_B1/alpha_B3:.1f}x B3)
  2. B1 mass DECREASES with tau (dM/dtau = {dM_B1:+.3f}), while B2
     and B3 masses INCREASE. This creates directional asymmetry.
  3. In the evanescent window (k < k_threshold), modes with
     M2 > omega are totally reflected. This gives arbitrarily large
     DR at the sharp-step level, but it is the mass gap effect,
     not impedance filtering per se.
  4. With tunneling through a wall of width d = 1/m_tau = {d_wall_natural:.3f}
     M_KK^{{-1}}, the evanescent modes leak through, reducing the
     effective DR.
  5. The asymptotic propagating-regime DR of {DR_analytic:.2f} decades is a
     STRUCTURAL CONSTRAINT: no amount of wall stacking or delta_tau
     variation can exceed it in the regime where all modes propagate.

Comparison to HF:
  HF-KK-42 sector DR = 1.51 decades comes from statistical level
  density differences (rho_B3 >> rho_B2 because dim^2 weighting).
  Impedance filtering DR = {DR_analytic:.2f} decades comes from
  differential mass sensitivity to tau. These are DIFFERENT mechanisms
  that operate MULTIPLICATIVELY, but:
  1.51 + {DR_analytic:.2f} = {1.51 + DR_analytic:.2f} decades < 3.

The 3-decade target requires a mechanism beyond single-wall impedance.
""")

# ============================================================
# 16. SUMMARY TABLE
# ============================================================
print("--- SUMMARY TABLE ---")
print(f"{'Quantity':<45} {'Value':>15} {'Units':<15}")
print("-" * 75)
print(f"{'M*_B2 (fold)':<45} {M1_B2:>15.5f} {'M_KK':<15}")
print(f"{'M*_B1 (fold)':<45} {M1_B1:>15.5f} {'M_KK':<15}")
print(f"{'M*_B3 (fold)':<45} {M1_B3:>15.5f} {'M_KK':<15}")
print(f"{'dM*_B2/dtau':<45} {dM_B2:>+15.5f} {'M_KK':<15}")
print(f"{'dM*_B1/dtau':<45} {dM_B1:>+15.5f} {'M_KK':<15}")
print(f"{'dM*_B3/dtau':<45} {dM_B3:>+15.5f} {'M_KK':<15}")
print(f"{'|(dM*/dtau)/M*|_B2':<45} {alpha_B2:>15.6f} {'':<15}")
print(f"{'|(dM*/dtau)/M*|_B1':<45} {alpha_B1:>15.6f} {'':<15}")
print(f"{'|(dM*/dtau)/M*|_B3':<45} {alpha_B3:>15.6f} {'':<15}")
print(f"{'B1/B2 sensitivity ratio':<45} {alpha_B1/alpha_B2:>15.2f} {'':<15}")
print(f"{'B1/B3 sensitivity ratio':<45} {alpha_B1/alpha_B3:>15.2f} {'':<15}")
print(f"{'d_wall (= 1/m_tau)':<45} {d_wall_natural:>15.4f} {'M_KK^-1':<15}")
print(f"{'|M*dM/dtau|_B2':<45} {product_B2:>15.4f} {'M_KK^2':<15}")
print(f"{'|M*dM/dtau|_B1':<45} {product_B1:>15.4f} {'M_KK^2':<15}")
print(f"{'|M*dM/dtau|_B3':<45} {product_B3:>15.4f} {'M_KK^2':<15}")
print(f"{'DR (propagating, analytical)':<45} {DR_analytic:>15.4f} {'decades':<15}")
print(f"{'DR (max, with tunneling)':<45} {max_DR:>15.4f} {'decades':<15}")
print(f"{'DR (max, sharp step)':<45} {max_DR_sharp:>15.4f} {'decades':<15}")
print(f"{'DR (cum, N=30, dtau=0.05, k=1)':<45} {DR_cum_30:>15.4f} {'decades':<15}")
print(f"{'HF-KK-42 sector DR':<45} {1.51:>15.2f} {'decades':<15}")
print(f"{'Combined HF + impedance':<45} {1.51+DR_analytic:>15.2f} {'decades':<15}")
print(f"{'Gate verdict':<45} {verdict:>15} {'':<15}")

# ============================================================
# 17. SAVE DATA
# ============================================================
outfile = base / "s43_impedance_mismatch.npz"
np.savez(outfile,
    # Gate
    verdict=np.array([verdict]),
    gate_DR_propagating=np.array([DR_analytic]),
    gate_DR_max_tunnel=np.array([max_DR]),
    gate_DR_max_sharp=np.array([max_DR_sharp]),
    gate_dtau_at_max=np.array([dtau_best]),
    gate_HF_DR=np.array([1.51]),
    gate_DR_cumulative_30=np.array([DR_cum_30]),
    gate_DR_combined=np.array([1.51 + DR_analytic]),

    # Masses at fold
    M_fold=M_fold,
    M_B2_fold=np.array([M1_B2]),
    M_B1_fold=np.array([M1_B1]),
    M_B3_fold=np.array([M1_B3]),

    # Mass derivatives
    dM_dtau_all=dM_dtau_all,
    dM_B2=np.array([dM_B2]),
    dM_B1=np.array([dM_B1]),
    dM_B3=np.array([dM_B3]),
    alpha_B2=np.array([alpha_B2]),
    alpha_B1=np.array([alpha_B1]),
    alpha_B3=np.array([alpha_B3]),

    # M*dM/dtau products
    product_B2=np.array([product_B2]),
    product_B1=np.array([product_B1]),
    product_B3=np.array([product_B3]),

    # Wall width
    d_wall_natural=np.array([d_wall_natural]),
    m_tau=np.array([m_tau]),

    # Transmission data
    delta_tau_values=delta_tau_values,
    k_values=k_values,
    T_B2=T_B2,
    T_B1=T_B1,
    T_B3=T_B3,
    T_B2_tun=T_B2_tun,
    T_B1_tun=T_B1_tun,
    T_B3_tun=T_B3_tun,
    T_rev_B2=T_rev_B2,
    T_rev_B1=T_rev_B1,
    T_rev_B3=T_rev_B3,

    # Dynamic range
    DR_sharp=DR_sharp,
    DR_tunnel=DR_tunnel,
    DR_max_sharp=DR_max_sharp,
    DR_max_tunnel=DR_max_tunnel,
    k_at_max_sharp=k_at_max_sharp,
    k_at_max_tunnel=k_at_max_tunnel,

    # Input reference
    tau_fold=np.array([tau_fold]),
    G_mod=np.array([G_mod]),
    eps_fold=eps_fold,
    Delta_fold=Delta_fold,
)
print(f"\nData saved to: {outfile}")

# ============================================================
# 18. PLOTS
# ============================================================
fig, axes = plt.subplots(2, 3, figsize=(18, 11))
fig.suptitle(f"S43 W2-4: Acoustic Impedance Mismatch at Domain Walls\n"
             f"Gate: IMP-FILTER-43 = {verdict} | "
             f"Propagating DR = {DR_analytic:.2f} decades", fontsize=13, fontweight='bold')

# Panel A: BdG mass structure at fold
ax = axes[0, 0]
modes = np.arange(8)
colors = ['red']*4 + ['blue'] + ['green']*3
labels_done = set()
for i in range(8):
    branch = "B2" if i < 4 else ("B1" if i == 4 else "B3")
    label = branch if branch not in labels_done else None
    labels_done.add(branch)
    ax.bar(i, M_fold[i], color=colors[i], alpha=0.7, label=label)
ax.set_xlabel('Mode index', fontsize=12)
ax.set_ylabel(r'$M^*$ [$M_{KK}$]', fontsize=12)
ax.set_title('A: BdG Quasiparticle Masses at Fold', fontsize=11)
ax.legend(fontsize=10)
ax.set_ylim(0, 2.5)

# Panel B: Mass sensitivity dM/dtau
ax = axes[0, 1]
ax.bar(modes, dM_dtau_all, color=colors, alpha=0.7)
ax.axhline(0, color='k', linewidth=0.5)
ax.set_xlabel('Mode index', fontsize=12)
ax.set_ylabel(r'$dM^*/d\tau$', fontsize=12)
ax.set_title('B: Mass Sensitivity (B1 is opposite sign)', fontsize=11)

# Panel C: T(k) at delta_tau = 0.05
ax = axes[0, 2]
d_plot = np.argmin(np.abs(delta_tau_values - 0.05))
ax.plot(k_values, T_B2[d_plot, :], 'r-', linewidth=2, label=f'B2 ($M^*={M1_B2:.3f}$)')
ax.plot(k_values, T_B1[d_plot, :], 'b-', linewidth=2, label=f'B1 ($M^*={M1_B1:.3f}$)')
ax.plot(k_values, T_B3[d_plot, :], 'g-', linewidth=2, label=f'B3 ($M^*={M1_B3:.3f}$)')

# Mark thresholds
M2_B2_05 = compute_M2(0, 0.05)
M2_B3_05 = compute_M2(5, 0.05)
km_B2_05 = np.sqrt(max(M2_B2_05**2 - M1_B2**2, 0))
km_B3_05 = np.sqrt(max(M2_B3_05**2 - M1_B3**2, 0))
ax.axvline(km_B2_05, color='red', linestyle=':', alpha=0.5, label=f'$k_{{min}}^{{B2}}={km_B2_05:.2f}$')
ax.axvline(km_B3_05, color='green', linestyle=':', alpha=0.5, label=f'$k_{{min}}^{{B3}}={km_B3_05:.2f}$')

ax.set_xlabel(r'$k$ [$M_{KK}$]', fontsize=12)
ax.set_ylabel(r'$T(k)$', fontsize=12)
ax.set_title(r'C: Transmission at $\delta\tau = 0.05$', fontsize=11)
ax.legend(fontsize=8, loc='lower right')
ax.set_xlim(0, 3)
ax.set_ylim(0.95, 1.001)

# Panel D: T(k) near threshold (log scale, larger delta_tau)
ax = axes[1, 0]
d_plot2 = np.argmin(np.abs(delta_tau_values - 0.10))
ax.semilogy(k_values, np.clip(T_B2[d_plot2, :], 1e-10, 1), 'r-', linewidth=2, label='B2')
ax.semilogy(k_values, np.clip(T_B1[d_plot2, :], 1e-10, 1), 'b-', linewidth=2, label='B1')
ax.semilogy(k_values, np.clip(T_B3[d_plot2, :], 1e-10, 1), 'g-', linewidth=2, label='B3')
ax.axhline(1e-3, color='gray', linestyle='--', alpha=0.5, label='3-decade target')
ax.set_xlabel(r'$k$ [$M_{KK}$]', fontsize=12)
ax.set_ylabel(r'$T(k)$', fontsize=12)
ax.set_title(r'D: Transmission at $\delta\tau = 0.10$ (log)', fontsize=11)
ax.legend(fontsize=10)
ax.set_xlim(0, 3)

# Panel E: DR(k) for multiple delta_tau
ax = axes[1, 1]
for d_idx, dtau in enumerate(delta_tau_values):
    if dtau >= 0.01:
        # Cap at 5 for plotting
        dr_capped = np.clip(DR_sharp[d_idx, :], 0, 5)
        ax.plot(k_values, dr_capped, linewidth=1.5,
                label=f'$\\delta\\tau = {dtau}$')
ax.axhline(3.0, color='red', linestyle='--', linewidth=1, alpha=0.7, label='3-decade target')
ax.axhline(DR_analytic, color='purple', linestyle='-.', linewidth=1, alpha=0.7,
           label=f'Asymptotic = {DR_analytic:.2f}')
ax.axhline(1.51, color='blue', linestyle=':', linewidth=1, alpha=0.7, label='HF-KK-42')
ax.set_xlabel(r'$k$ [$M_{KK}$]', fontsize=12)
ax.set_ylabel('Dynamic Range [decades]', fontsize=12)
ax.set_title('E: Single-Wall DR (sharp step)', fontsize=11)
ax.legend(fontsize=8, loc='upper right')
ax.set_xlim(0, 5)
ax.set_ylim(0, 5)

# Panel F: M*dM/dtau products (bar chart)
ax = axes[1, 2]
branches = ['B2', 'B1', 'B3']
prods = [product_B2, product_B1, product_B3]
bar_colors = ['red', 'blue', 'green']
bars = ax.bar(branches, prods, color=bar_colors, alpha=0.7)
ax.set_ylabel(r'$|M^* \cdot dM^*/d\tau|$ [$M_{KK}^2$]', fontsize=12)
ax.set_title(f'F: Impedance Product (sets asymptotic DR = {DR_analytic:.2f})', fontsize=11)
for bar, prod in zip(bars, prods):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.02,
            f'{prod:.3f}', ha='center', fontsize=10)

plt.tight_layout()
plotfile = base / "s43_impedance_mismatch.png"
plt.savefig(plotfile, dpi=150)
plt.close()
print(f"Plot saved to: {plotfile}")

print("\n" + "=" * 72)
print("COMPUTATION COMPLETE")
print("=" * 72)
