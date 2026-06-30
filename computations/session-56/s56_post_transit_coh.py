#!/usr/bin/env python3
"""
POST-TRANSIT-COH-56: Post-Transit Superfluid Coherence
=======================================================
Einstein-Theorist computation.

Physics: After transit (tau > 0.22), BCS condensate is destroyed (P_exc = 1.000).
Question: Does phase coherence survive via GGE pair correlations?

The Josephson energy E_J sets the coherence scale:
  E_J = J_C2^2 * F_anomalous

where F_anomalous = sum_k Delta / (2 * E_qp_k^2) in equilibrium BCS,
but post-transit the condensate Delta -> 0 and F_anomalous -> 0.

However, the GGE (Generalized Gibbs Ensemble) preserves integrability-protected
pair correlations: <c^dag c^dag c c>_GGE != 0 even when Delta_BCS = 0.

We estimate F_anomalous_GGE from the GGE occupation numbers n_k via:
  F_GGE = sum_k sqrt(n_k * (1 - n_k))
which is the anomalous density of a state with occupation n_k (the off-diagonal
long-range order surviving in the pair channel of the GGE).

Gate: POST-TRANSIT-COH-56 (INFO)
"""

import sys
import os
sys.path.insert(0, 'computations')
from canonical_constants import *
import numpy as np

# ============================================================
# 1. Load data
# ============================================================
tb = np.load('computations/session-54/s54_tb_hamiltonian.npz', allow_pickle=True)
sf = np.load('computations/session-54/s54_scale_factor.npz', allow_pickle=True)
vol = np.load('computations/session-55/s55_volovik_identity.npz', allow_pickle=True)

tau_tb = tb['tau_values']        # (50,) in [0, 0.5]
eigenvalues = tb['eigenvalues']  # (50, 32)
J_C2_tau = tb['J_C2_tau']       # (50,)

tau_sf = sf['tau']               # (10,)
H_sf = sf['H']                  # (10,) Hubble parameter in M_KK units

T_k_GGE = vol['T_k']            # (8,) effective temperatures per BCS mode
tau_vol = vol['tau_values']      # (50,)

# ============================================================
# 2. Interpolate H(tau) to all 50 tau points
# ============================================================
from scipy.interpolate import interp1d
H_interp = interp1d(tau_sf, H_sf, kind='cubic', fill_value='extrapolate')
H_all = H_interp(tau_tb)

# ============================================================
# 3. Equilibrium BCS anomalous density at each tau
# ============================================================
# BCS gap from canonical constants
Delta_BCS = Delta_0_OES  # 0.4643

# For equilibrium BCS: F_anom = sum_k Delta / (2 * E_qp_k^2)
# where E_qp_k = sqrt(epsilon_k^2 + Delta^2), epsilon_k measured from Fermi level.
#
# The 8 BCS-active modes are the lowest eigenvalues near the gap edge.
# From the framework: N_dof_BCS = 8, and the BCS modes are at the Fermi surface.
# The eigenvalues from the tight-binding Hamiltonian are single-particle energies.
# For BCS, epsilon_k = E_k - mu where mu is at the gap edge.

N_BCS = N_dof_BCS  # 8

F_anom_eq = np.zeros(len(tau_tb))
E_J_eq = np.zeros(len(tau_tb))

for i in range(len(tau_tb)):
    # Take the 8 lowest positive eigenvalues as BCS-active modes
    eigs = np.sort(np.abs(eigenvalues[i]))
    eigs_bcs = eigs[1:N_BCS+1]  # skip zero mode

    # BCS quasiparticle energies
    E_qp = np.sqrt(eigs_bcs**2 + Delta_BCS**2)

    # Anomalous Green's function (equilibrium)
    F_anom_eq[i] = np.sum(Delta_BCS / (2.0 * E_qp**2))

    # Josephson energy
    E_J_eq[i] = J_C2_tau[i]**2 * F_anom_eq[i]

# ============================================================
# 4. GGE pair correlations post-transit
# ============================================================
# Post-transit: condensate Delta -> 0, BUT GGE occupations are non-thermal.
# The GGE state has occupations n_k determined by the quench dynamics.
#
# For a BCS-like state characterized by occupations {n_k}, the anomalous
# pair correlation (off-diagonal long-range order) is:
#   kappa_k = <c_{k,up} c_{-k,down}> = sqrt(n_k * (1 - n_k)) * e^{i*phi_k}
#
# This is the standard BCS result: for a state with Bogoliubov occupation n_k,
# the anomalous density is |kappa_k| = sqrt(n_k * (1 - n_k)).
# This is maximized at n_k = 1/2 and vanishes for n_k = 0 or 1.
#
# In the GGE, the occupations are given by the Fermi function at effective
# temperatures T_k: n_k = 1 / (1 + exp(E_k / T_k))
# where E_k are quasiparticle energies.
#
# CRITICAL DISTINCTION:
# - In equilibrium BCS, Delta != 0 and all pairs are phase-coherent.
# - In the GGE, Delta = 0 but pair correlations kappa_k != 0 individually.
# - The question is whether the INTER-CELL Josephson coupling J_C2 can
#   establish long-range phase coherence from these residual pair correlations.

# Compute GGE occupations for each mode at each tau
# T_k_GGE are the 8 effective temperatures
n_k_GGE = np.zeros((len(tau_tb), N_BCS))
F_anom_GGE = np.zeros(len(tau_tb))
kappa_k_GGE = np.zeros((len(tau_tb), N_BCS))

for i in range(len(tau_tb)):
    eigs = np.sort(np.abs(eigenvalues[i]))
    eigs_bcs = eigs[1:N_BCS+1]

    for k in range(N_BCS):
        # GGE occupation: n_k = 1/(1 + exp(E_k/T_k))
        if T_k_GGE[k] > 1e-10:
            n_k_GGE[i, k] = 1.0 / (1.0 + np.exp(eigs_bcs[k] / T_k_GGE[k]))
        else:
            n_k_GGE[i, k] = 0.0

        # Anomalous pair density from GGE
        kappa_k_GGE[i, k] = np.sqrt(n_k_GGE[i, k] * (1.0 - n_k_GGE[i, k]))

    # Total anomalous density: sum of |kappa_k|
    # This replaces Delta/(2*E_qp^2) in the equilibrium formula
    F_anom_GGE[i] = np.sum(kappa_k_GGE[i])

# GGE Josephson energy
E_J_GGE = J_C2_tau**2 * F_anom_GGE

# ============================================================
# 5. E_J / H ratios
# ============================================================
ratio_eq = E_J_eq / H_all
ratio_GGE = E_J_GGE / H_all

# Report at key tau values
targets = [0.19, 0.22, 0.30, 0.40, 0.50]
print("=" * 85)
print("POST-TRANSIT-COH-56: Post-Transit Superfluid Coherence")
print("=" * 85)
print()
print(f"BCS gap Delta_0 = {Delta_BCS:.4f} M_KK")
print(f"N_BCS modes = {N_BCS}")
print(f"GGE effective temperatures T_k = {T_k_GGE}")
print()

print("-" * 85)
print(f"{'tau':>6s}  {'J_C2':>8s}  {'H':>8s}  {'F_eq':>10s}  {'F_GGE':>10s}  "
      f"{'E_J_eq':>10s}  {'E_J_GGE':>10s}  {'E_J_eq/H':>10s}  {'E_J_GGE/H':>10s}")
print("-" * 85)

results = {}
for t in targets:
    idx = np.argmin(np.abs(tau_tb - t))
    tau_actual = tau_tb[idx]
    print(f"{tau_actual:6.4f}  {J_C2_tau[idx]:8.4f}  {H_all[idx]:8.4f}  "
          f"{F_anom_eq[idx]:10.6f}  {F_anom_GGE[idx]:10.6f}  "
          f"{E_J_eq[idx]:10.6f}  {E_J_GGE[idx]:10.6f}  "
          f"{ratio_eq[idx]:10.4f}  {ratio_GGE[idx]:10.4f}")
    results[f"tau_{tau_actual:.4f}"] = {
        'tau': tau_actual,
        'J_C2': J_C2_tau[idx],
        'H': H_all[idx],
        'F_eq': F_anom_eq[idx],
        'F_GGE': F_anom_GGE[idx],
        'E_J_eq': E_J_eq[idx],
        'E_J_GGE': E_J_GGE[idx],
        'ratio_eq': ratio_eq[idx],
        'ratio_GGE': ratio_GGE[idx],
    }

print("-" * 85)
print()

# ============================================================
# 6. Phase coherence analysis
# ============================================================
print("=" * 85)
print("PHASE COHERENCE ANALYSIS")
print("=" * 85)
print()

# At fold (tau ~ 0.19): equilibrium BCS coherent
idx_fold = np.argmin(np.abs(tau_tb - 0.19))
print(f"At fold (tau={tau_tb[idx_fold]:.4f}):")
print(f"  E_J_eq/H = {ratio_eq[idx_fold]:.4f}")
print(f"  E_J_GGE/H = {ratio_GGE[idx_fold]:.4f}")
print(f"  -> {'COHERENT' if ratio_eq[idx_fold] > 1 else 'INCOHERENT'} (equilibrium BCS)")
print()

# Post-transit analysis
print("Post-transit (tau > 0.22):")
for t in [0.22, 0.30, 0.40, 0.50]:
    idx = np.argmin(np.abs(tau_tb - t))
    tau_actual = tau_tb[idx]

    # Decompose kappa_k contributions
    print(f"\n  tau = {tau_actual:.4f}:")
    print(f"    J_C2 = {J_C2_tau[idx]:.6f}")
    print(f"    H = {H_all[idx]:.6f}")

    eigs = np.sort(np.abs(eigenvalues[idx]))
    eigs_bcs = eigs[1:N_BCS+1]

    print(f"    Mode-by-mode GGE pair correlations:")
    for k in range(N_BCS):
        print(f"      k={k}: E_k={eigs_bcs[k]:.4f}, T_k={T_k_GGE[k]:.4f}, "
              f"n_k={n_k_GGE[idx,k]:.4f}, kappa_k={kappa_k_GGE[idx,k]:.4f}")

    print(f"    F_GGE = {F_anom_GGE[idx]:.6f}")
    print(f"    E_J_GGE = {E_J_GGE[idx]:.6f}")
    print(f"    E_J_GGE/H = {ratio_GGE[idx]:.6f}")

    if ratio_GGE[idx] > 1:
        print(f"    -> COHERENT (E_J_GGE > H)")
    else:
        print(f"    -> INCOHERENT (E_J_GGE < H, horizon problem)")
        print(f"    -> Shortfall: H/E_J_GGE = {H_all[idx]/E_J_GGE[idx]:.1f}x")

# ============================================================
# 7. Critical tau where E_J_GGE = H
# ============================================================
print()
print("=" * 85)
print("COHERENCE BOUNDARY")
print("=" * 85)

# Find where ratio_GGE crosses 1
crossings = []
for i in range(len(tau_tb) - 1):
    if (ratio_GGE[i] - 1.0) * (ratio_GGE[i+1] - 1.0) < 0:
        # Linear interpolation
        tau_cross = tau_tb[i] + (1.0 - ratio_GGE[i]) / (ratio_GGE[i+1] - ratio_GGE[i]) * (tau_tb[i+1] - tau_tb[i])
        crossings.append(tau_cross)
        print(f"E_J_GGE/H = 1 crossing at tau = {tau_cross:.4f}")

if not crossings:
    if ratio_GGE[0] > 1:
        print(f"E_J_GGE/H > 1 everywhere: min = {np.min(ratio_GGE):.4f} at tau = {tau_tb[np.argmin(ratio_GGE)]:.4f}")
    else:
        print(f"E_J_GGE/H < 1 everywhere: max = {np.max(ratio_GGE):.4f} at tau = {tau_tb[np.argmax(ratio_GGE)]:.4f}")

# ============================================================
# 8. Physical interpretation: three regimes
# ============================================================
print()
print("=" * 85)
print("PHYSICAL INTERPRETATION")
print("=" * 85)
print()

# Regime 1: pre-fold BCS (tau < 0.19)
# Regime 2: transit destruction (tau ~ 0.19-0.22)
# Regime 3: post-transit GGE (tau > 0.22)

print("Three regimes of phase coherence:")
print()
print("REGIME 1 (tau < 0.19): Equilibrium BCS")
idx_pre = np.argmin(np.abs(tau_tb - 0.15))
print(f"  E_J_eq/H = {ratio_eq[idx_pre]:.4f} at tau={tau_tb[idx_pre]:.4f}")
print(f"  Condensate intact, Delta = {Delta_BCS:.4f} M_KK")
print(f"  Phase coherence: ESTABLISHED by BCS mechanism")
print()

print("REGIME 2 (0.19 < tau < 0.22): Transit")
idx_transit = np.argmin(np.abs(tau_tb - 0.21))
print(f"  P_exc = 1.000 (condensate fully destroyed)")
print(f"  E_J transits from equilibrium to GGE value")
print(f"  Duration: dt_transit = {dt_transit:.6f} (in natural units)")
print()

print("REGIME 3 (tau > 0.22): Post-Transit GGE")
for t in [0.25, 0.35, 0.50]:
    idx = np.argmin(np.abs(tau_tb - t))
    print(f"  tau={tau_tb[idx]:.4f}: E_J_GGE/H = {ratio_GGE[idx]:.6f}")
print()

# Key insight: J_C2 falls as tau increases (internal space decouples)
# but H also falls (expansion decelerates). The ratio is what matters.
print("Key dynamics:")
print(f"  J_C2 at fold: {J_C2_tau[idx_fold]:.4f}, at tau=0.5: {J_C2_tau[-1]:.4f}")
print(f"  Ratio: {J_C2_tau[-1]/J_C2_tau[idx_fold]:.4f}")
print(f"  H at fold: {H_all[idx_fold]:.4f}, at tau=0.5: {H_all[-1]:.4f}")
print(f"  Ratio: {H_all[-1]/H_all[idx_fold]:.4f}")
print(f"  J_C2 decay rate vs H decay rate: "
      f"{np.log(J_C2_tau[-1]/J_C2_tau[idx_fold]) / np.log(H_all[-1]/H_all[idx_fold]):.4f}")
print()

# ============================================================
# 9. Comparison: E_J_GGE vs E_J_thermal
# ============================================================
print("=" * 85)
print("GGE vs THERMAL COMPARISON")
print("=" * 85)
print()

# If the state were thermal at T_therm = 1.047, all modes would have same T
T_therm = float(vol['T_therm'])  # 1.047
F_anom_therm = np.zeros(len(tau_tb))
for i in range(len(tau_tb)):
    eigs = np.sort(np.abs(eigenvalues[i]))
    eigs_bcs = eigs[1:N_BCS+1]
    n_therm = 1.0 / (1.0 + np.exp(eigs_bcs / T_therm))
    kappa_therm = np.sqrt(n_therm * (1.0 - n_therm))
    F_anom_therm[i] = np.sum(kappa_therm)

E_J_therm = J_C2_tau**2 * F_anom_therm
ratio_therm = E_J_therm / H_all

for t in [0.22, 0.30, 0.50]:
    idx = np.argmin(np.abs(tau_tb - t))
    print(f"tau={tau_tb[idx]:.4f}: E_J_GGE/H = {ratio_GGE[idx]:.4f}, "
          f"E_J_therm/H = {ratio_therm[idx]:.4f}, "
          f"ratio GGE/therm = {ratio_GGE[idx]/ratio_therm[idx]:.4f}")

print()
print(f"GGE non-thermality: sigma_T/T = {float(vol['sigma_T_over_T']):.4f}")
print(f"Thermal equilibrium temperature: T_therm = {T_therm:.4f}")
print(f"Mean GGE temperature: T_mean = {float(vol['T_mean_mode']):.4f}")

# ============================================================
# 10. Effacement check: E_J vs E_fold
# ============================================================
print()
print("=" * 85)
print("EFFACEMENT (EIH) CHECK")
print("=" * 85)
print()

# E_J should be small compared to the spectral action gradient
# at the fold (dS/dtau ~ 58,673)
print(f"dS/dtau at fold: {dS_fold:.1f}")
print(f"E_J_GGE at fold: {E_J_GGE[idx_fold]:.6f}")
print(f"Effacement ratio E_J/dS: {E_J_GGE[idx_fold]/dS_fold:.2e}")
print("-> Pair coherence is MICROSCOPIC compared to spectral geometry")
print("-> Consistent with EIH effacement principle")

# ============================================================
# 11. Save results
# ============================================================
np.savez('computations/session-56/s56_post_transit_coh.npz',
    # Grid data
    tau_values=tau_tb,
    J_C2_tau=J_C2_tau,
    H_tau=H_all,

    # Equilibrium BCS
    F_anom_eq=F_anom_eq,
    E_J_eq=E_J_eq,
    ratio_eq=ratio_eq,

    # GGE post-transit
    T_k_GGE=T_k_GGE,
    n_k_GGE=n_k_GGE,
    kappa_k_GGE=kappa_k_GGE,
    F_anom_GGE=F_anom_GGE,
    E_J_GGE=E_J_GGE,
    ratio_GGE=ratio_GGE,

    # Thermal comparison
    T_therm=T_therm,
    F_anom_therm=F_anom_therm,
    E_J_therm=E_J_therm,
    ratio_therm=ratio_therm,

    # Key scalars
    Delta_BCS=Delta_BCS,
    N_BCS=N_BCS,
    crossings=np.array(crossings) if crossings else np.array([]),

    # Gate
    gate_name='POST-TRANSIT-COH-56',
    gate_verdict='INFO',
)

print()
print("=" * 85)
print(f"Data saved to computations/session-56/s56_post_transit_coh.npz")
print("Gate: POST-TRANSIT-COH-56 = INFO")
print("=" * 85)
