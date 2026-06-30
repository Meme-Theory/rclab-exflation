#!/usr/bin/env python3
"""
s58_cc_cancellation_sweep.py — CC-CANCELLATION-SWEEP-58
=======================================================

Extends S57 CC-SIGN-57 to 50 tau values. At each tau:
  1. Compute 8 positive Dirac eigenvalues from the (0,0) irrep of D_K(tau)
  2. Assign to branches: B1 (1 mode), B2 (4 modes), B3 (3 modes)
  3. Build full 256-state BCS Hamiltonian with DOS weights (S36/S43 approach)
  4. Diagonalize -> ground state -> GGE occupations <n_k>
  5. Find equilibrium at optimal T_eq(tau) via Boltzmann fit
  6. Volovik non-equilibrium formula: Lambda_eff = sum_k delta_n_k * (E_k - mu_eff_k)
  7. Sector decomposition (B2, B1, B3) and cancellation ratio R_cancel
  8. Derivative dLambda/dtau and equation of state w(tau)

The S57 result at the fold: Lambda_eff = +0.00145 M_KK
  B2 = +0.316, B1 = -0.165, B3 = -0.150 (near cancellation, 0.46% residual)

Gate: CC-CANCELLATION-SWEEP-58 (INFO)
  - Structural: R_cancel in [0.001, 0.01] at all 50 tau
  - Accidental: R_cancel varies by > 1 OOM

Superfluid analog: In 3He-B after a quench, the non-equilibrium departure from
the BCS ground state produces vacuum energy. The Volovik formula (Papers 15-16)
gives Lambda_eff from the occupation mismatch delta_n_k between the GGE and
thermal equilibrium. The near-cancellation at the fold reflects partial
equilibration within sectors while inter-sector departure persists -- exactly
the 3He-B analog where different angular momentum channels thermalize at
different rates.

Author: Volovik-Superfluid-Universe-Theorist
Session: 58, Wave 0, Task W0-2
"""

import sys
import os
import time
import numpy as np
from scipy.optimize import minimize_scalar

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ARCHIVE_DIR = os.path.join(os.path.dirname(SCRIPT_DIR), 'computations/_shared')

sys.path.insert(0, SCRIPT_DIR)
sys.path.insert(0, ARCHIVE_DIR)

from canonical_constants import (
    E_cond, E_cond_ED_8mode, M_KK, M_KK_gravity, rho_Lambda_obs,
    tau_fold, N_cells, N_dof_BCS, rho_B2_per_mode,
)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

t_start = time.time()

N_MODES = 8  # (local)
N_FOCK = 2**N_MODES  # 256

print("=" * 78)
print("CC-CANCELLATION-SWEEP-58: Near-Cancellation Across 50 Tau Points")
print("=" * 78)

# ============================================================================
# Section 1: Dirac Spectrum Infrastructure
# ============================================================================

print("\n--- Section 1: Loading Dirac Spectrum Infrastructure ---")

from dirac_spectrum import (
    su3_generators, compute_structure_constants,
    collect_spectrum, build_cliff8
)

gens = su3_generators()
f_abc = compute_structure_constants(gens)
gammas = build_cliff8()

# ============================================================================
# Section 2: Load Reference Data
# ============================================================================

print("\n--- Section 2: Load Reference Data ---")

# S36 V_8x8 and S35 DOS
d36 = np.load(os.path.join(ARCHIVE_DIR, 's36_multisector_ed.npz'), allow_pickle=True)
V_8x8 = d36['V_8x8_full']          # 8x8 pairing matrix (fixed across tau)
E_8_fold_ref = d36['E_8_full']      # Reference E_8 at fold from S36
branch_labels = list(d36['branch_labels'])

# S35 van Hove DOS
d35 = np.load(os.path.join(ARCHIVE_DIR, 's35a_vh_impedance_arbiter.npz'), allow_pickle=True)
rho_smooth = float(d35['rho_at_physical'])  # B2 flat-band DOS

# DOS array: B2 modes get van Hove rho, B1/B3 get 1.0
rho = np.array([rho_smooth]*4 + [1.0, 1.0, 1.0, 1.0])

# S57 fold values for cross-check
d57 = np.load(os.path.join(SCRIPT_DIR, 's57_cc_sign.npz'), allow_pickle=True)
Lambda_fold_s57 = float(d57['Lambda_volovik_total'])
Lambda_B2_fold_s57 = float(d57['Lambda_B2'])
Lambda_B1_fold_s57 = float(d57['Lambda_B1'])
Lambda_B3_fold_s57 = float(d57['Lambda_B3'])
fk_gge_s57 = d57['fk_gge']
w_fold_s57 = float(d57['w_GGE'])

# S54 tau grid
d54 = np.load(os.path.join(SCRIPT_DIR, 's54_ed_sweep.npz'), allow_pickle=True)
tau_values = d54['tau_values']  # (50,)
fold_idx = int(d54['fold_idx'])
N_tau = len(tau_values)

print(f"V_8x8 norm = {np.linalg.norm(V_8x8):.6f}")
print(f"rho_smooth (B2 DOS) = {rho_smooth:.6f}")
print(f"tau grid: {N_tau} points in [{tau_values[0]:.4f}, {tau_values[-1]:.4f}]")
print(f"fold_idx = {fold_idx}, tau_fold = {tau_values[fold_idx]:.4f}")
print(f"S57 Lambda_volovik at fold = {Lambda_fold_s57:.6f} M_KK")

# ============================================================================
# Section 3: Compute Dirac Eigenvalues at Each Tau
# ============================================================================

print("\n--- Section 3: Dirac Spectrum Sweep ---")

E_8_sweep = np.zeros((N_tau, N_MODES))  # 8 branch energies at each tau

for t in range(N_tau):
    tau = tau_values[t]

    # Compute (0,0) irrep eigenvalues only (16 eigenvalues, fast)
    evals_raw, _ = collect_spectrum(tau, gens, f_abc, gammas, max_pq_sum=0, verbose=False)
    evals_arr = np.array(evals_raw)

    # Extract Dirac eigenvalues (imaginary parts of column 0)
    dirac_evals = evals_arr[:, 0].imag

    # Sort positive eigenvalues -> [B1, B2x4, B3x3] by energy
    pos_evals = np.sort(dirac_evals[dirac_evals > 1e-10])

    if len(pos_evals) != 8:
        print(f"  WARNING: tau={tau:.4f} has {len(pos_evals)} positive eigenvalues (expected 8)")
        # Pad or truncate
        if len(pos_evals) < 8:
            pos_evals = np.pad(pos_evals, (0, 8-len(pos_evals)),
                               mode='constant', constant_values=pos_evals[-1])
        else:
            pos_evals = pos_evals[:8]

    # Branch assignment: sort by value, then identify clusters
    # At the fold: B1 (smallest, 1 mode), B2 (next cluster of 4), B3 (top cluster of 3)
    # The ordering is: B1[0], B2[0], B2[1], B2[2], B2[3], B3[0], B3[1], B3[2]
    # Mapping to S36 convention: [B2[0..3], B1, B3[0..2]]
    # S36: pos_idx order is [B1_idx, B2_idx, B3_idx] then reorders to [B2, B1, B3]
    # Since the eigenvalues come out sorted: [B1, B2_0..3, B3_0..2]
    # We remap to S36 convention: [B2_0, B2_1, B2_2, B2_3, B1, B3_0, B3_1, B3_2]
    E_8_sweep[t, 0:4] = pos_evals[1:5]   # B2 (4 modes)
    E_8_sweep[t, 4] = pos_evals[0]        # B1 (1 mode, lowest)
    E_8_sweep[t, 5:8] = pos_evals[5:8]    # B3 (3 modes)

    if t % 10 == 0 or t == fold_idx:
        tag = " <-- FOLD" if t == fold_idx else ""
        print(f"  tau[{t:2d}]={tau:.4f}: B1={pos_evals[0]:.6f}, "
              f"B2={np.mean(pos_evals[1:5]):.6f}, B3={np.mean(pos_evals[5:8]):.6f}{tag}")

# Cross-check at fold against S36
print(f"\nFold cross-check:")
print(f"  S36 E_8: {E_8_fold_ref}")
print(f"  S58 E_8: {E_8_sweep[fold_idx]}")
print(f"  Max diff: {np.max(np.abs(E_8_sweep[fold_idx] - E_8_fold_ref)):.6f}")
# Note: S36 used tau=0.20, we use tau=0.1939. Small discrepancy expected.

print(f"\nDirac sweep complete in {time.time()-t_start:.1f}s")

# ============================================================================
# Section 4: BCS Hamiltonian and GGE at Each Tau
# ============================================================================

print("\n--- Section 4: Full Fock BCS + GGE Sweep ---")


def build_full_fock_H(xi, V, rho_dos, n_modes=8):
    """Build BCS pair Hamiltonian in full 2^N Fock space.

    H = sum_k 2*xi_k * n_k - sum_{k,k'} V_{kk'} * sqrt(rho_k*rho_k') * P+_k P_{k'}

    This is the S36/S43 construction with DOS-weighted pairing.
    """
    dim = 2**n_modes
    H = np.zeros((dim, dim))

    for s in range(dim):
        for k in range(n_modes):
            if s & (1 << k):
                H[s, s] += 2.0 * xi[k]

        for k in range(n_modes):
            for kp in range(n_modes):
                if k == kp:
                    continue
                v_eff = V[k, kp] * np.sqrt(rho_dos[k] * rho_dos[kp])
                if abs(v_eff) < 1e-30:
                    continue
                if (s & (1 << kp)) and not (s & (1 << k)):
                    sp = (s ^ (1 << kp)) | (1 << k)
                    H[sp, s] -= v_eff

    return H


def extract_occupations(psi_gs, n_modes=8):
    """Extract <n_k> from full Fock space ground state."""
    dim = 2**n_modes
    nk = np.zeros(n_modes)
    for k in range(n_modes):
        for s in range(dim):
            if (s >> k) & 1:
                nk[k] += abs(psi_gs[s])**2
    return nk


def boltzmann_eq(T, E_pair):
    """Canonical N=1 equilibrium: f_k = exp(-E_pair_k/T) / Z.

    E_pair are pair energies (2*xi).
    """
    if T <= 1e-15:
        f = np.zeros_like(E_pair)
        f[np.argmin(E_pair)] = 1.0
        return f
    boltz = np.exp(-E_pair / T)
    return boltz / np.sum(boltz)


def volovik_formula(fk_gge, fk_eq, E_pair, T_eq):
    """Volovik non-equilibrium vacuum energy per mode.

    Lambda_k = delta_f_k * (E_pair_k - mu_eff_k)
    where mu_eff_k = T_eq * ln((1-f_eq_k)/f_eq_k).
    """
    delta_fk = fk_gge - fk_eq
    eps_small = 1e-15  # (local)
    fk_eq_safe = np.clip(fk_eq, eps_small, 1.0 - eps_small)
    mu_eff_k = T_eq * np.log((1.0 - fk_eq_safe) / fk_eq_safe)
    return delta_fk * (E_pair - mu_eff_k)


# Storage
fk_gge_sweep = np.zeros((N_tau, N_MODES))
fk_eq_sweep = np.zeros((N_tau, N_MODES))
T_eq_sweep = np.zeros(N_tau)
E_GGE_sweep = np.zeros(N_tau)
E_BCS_sweep = np.zeros(N_tau)
E_eq_sweep = np.zeros(N_tau)
N_avg_sweep = np.zeros(N_tau)
E_cond_sweep = np.zeros(N_tau)

Lambda_eff_sweep = np.zeros(N_tau)
Lambda_B2_sweep = np.zeros(N_tau)
Lambda_B1_sweep = np.zeros(N_tau)
Lambda_B3_sweep = np.zeros(N_tau)
Lambda_permode_sweep = np.zeros((N_tau, N_MODES))

Delta_E_sweep = np.zeros(N_tau)
P_vac_sweep = np.zeros(N_tau)
w_sweep = np.zeros(N_tau)

B2_idx = [0, 1, 2, 3]
B1_idx = [4]
B3_idx = [5, 6, 7]

for t in range(N_tau):
    tau = tau_values[t]
    xi = E_8_sweep[t]        # single-particle (half-pair) energies
    E_pair = 2.0 * xi        # pair energies
    mu = 0.0  # particle-hole symmetric (local)

    # Build and diagonalize full Fock Hamiltonian
    H_full = build_full_fock_H(xi - mu, V_8x8, rho, N_MODES)
    H_full = 0.5 * (H_full + H_full.T)  # symmetrize
    evals, evecs = np.linalg.eigh(H_full)

    E_BCS_sweep[t] = evals[0]
    psi_gs = evecs[:, 0]

    # GGE occupations
    fk_gge = extract_occupations(psi_gs, N_MODES)
    fk_gge_sweep[t] = fk_gge
    N_avg_sweep[t] = np.sum(fk_gge)

    # E_GGE = sum_k <n_k> * 2*xi_k (post-quench, pairing destroyed)
    E_GGE_sweep[t] = np.sum(fk_gge * E_pair)
    Delta_E_sweep[t] = E_GGE_sweep[t] - E_BCS_sweep[t]

    # Condensation energy
    E_normal = E_pair[np.argmin(E_pair)]  # lowest pair energy
    E_cond_sweep[t] = E_BCS_sweep[t] - E_normal

    # Equilibrium fit
    def L2_canonical(T):
        f_eq = boltzmann_eq(T, E_pair)
        return np.sum((fk_gge - f_eq)**2)

    result = minimize_scalar(L2_canonical, bounds=(0.01, 50.0), method='bounded',
                             options={'xatol': 1e-15})
    T_eq = result.x
    T_eq_sweep[t] = T_eq
    fk_eq = boltzmann_eq(T_eq, E_pair)
    fk_eq_sweep[t] = fk_eq
    E_eq_sweep[t] = np.sum(fk_eq * E_pair)

    # Volovik formula
    Lambda_pm = volovik_formula(fk_gge, fk_eq, E_pair, T_eq)
    Lambda_permode_sweep[t] = Lambda_pm
    Lambda_eff_sweep[t] = np.sum(Lambda_pm)
    Lambda_B2_sweep[t] = np.sum(Lambda_pm[B2_idx])
    Lambda_B1_sweep[t] = np.sum(Lambda_pm[B1_idx])
    Lambda_B3_sweep[t] = np.sum(Lambda_pm[B3_idx])

    # Vacuum pressure and w
    P_vac_sweep[t] = N_avg_sweep[t] - E_GGE_sweep[t]
    if abs(E_GGE_sweep[t]) > 1e-15:
        w_sweep[t] = P_vac_sweep[t] / E_GGE_sweep[t]
    else:
        w_sweep[t] = 0.0

    if t % 10 == 0 or t == fold_idx:
        tag = " <-- FOLD" if t == fold_idx else ""
        print(f"  tau[{t:2d}]={tau:.4f}: E_BCS={E_BCS_sweep[t]:.6f}, "
              f"<N>={N_avg_sweep[t]:.4f}, Lambda_V={Lambda_eff_sweep[t]:+.6f}, "
              f"B2={Lambda_B2_sweep[t]:+.4f}, B1+B3={Lambda_B1_sweep[t]+Lambda_B3_sweep[t]:+.4f}, "
              f"w={w_sweep[t]:.4f}{tag}")

print(f"\nBCS + GGE sweep complete in {time.time()-t_start:.1f}s")

# ============================================================================
# Section 5: Cancellation Ratio
# ============================================================================

print("\n--- Section 5: Cancellation Ratio ---")

Lambda_B1B3_sweep = Lambda_B1_sweep + Lambda_B3_sweep
R_cancel = np.zeros(N_tau)
for t in range(N_tau):
    denom = max(abs(Lambda_B2_sweep[t]), abs(Lambda_B1B3_sweep[t]))
    if denom > 1e-20:
        R_cancel[t] = abs(Lambda_eff_sweep[t]) / denom
    else:
        R_cancel[t] = 1.0

R_cancel_min = np.min(R_cancel)
R_cancel_max = np.max(R_cancel)
R_cancel_mean = np.mean(R_cancel)
R_cancel_fold = R_cancel[fold_idx]
R_cancel_ratio = R_cancel_max / R_cancel_min if R_cancel_min > 0 else float('inf')

print(f"R_cancel range: [{R_cancel_min:.6f}, {R_cancel_max:.6f}]")
print(f"R_cancel at fold: {R_cancel_fold:.6f}")
print(f"R_cancel mean: {R_cancel_mean:.6f}")
print(f"R_cancel max/min ratio: {R_cancel_ratio:.2f}")

# Gate classification
if R_cancel_min >= 0.001 and R_cancel_max <= 0.01:
    gate_class = "STRUCTURAL"
    print(f"\nR_cancel in [0.001, 0.01] at all tau -> STRUCTURAL")
elif R_cancel_ratio > 10.0:
    gate_class = "ACCIDENTAL"
    print(f"\nR_cancel varies by > 1 OOM -> ACCIDENTAL")
else:
    gate_class = "INTERMEDIATE"
    print(f"\nR_cancel outside [0.001,0.01] but variation < 1 OOM -> INTERMEDIATE")

# ============================================================================
# Section 6: Derivative dLambda/dtau and w(tau)
# ============================================================================

print("\n--- Section 6: dLambda/dtau and w(tau) ---")

dtau = tau_values[1] - tau_values[0]
dLambda_dtau = np.gradient(Lambda_eff_sweep, dtau)

print(f"dLambda/dtau at fold: {dLambda_dtau[fold_idx]:.6f} M_KK/rad")
print(f"dLambda/dtau range: [{dLambda_dtau.min():.6f}, {dLambda_dtau.max():.6f}]")

print(f"\nw(tau) profile:")
print(f"  w at fold: {w_sweep[fold_idx]:.6f}")
print(f"  w range: [{w_sweep.min():.4f}, {w_sweep.max():.4f}]")
print(f"  w mean: {w_sweep.mean():.4f}")
print(f"  w < -1/3 (accelerating) count: {np.sum(w_sweep < -1.0/3.0)}/{N_tau}")

# ============================================================================
# Section 7: Cross-Check Against S57 at Fold
# ============================================================================

print("\n--- Section 7: S57 Cross-Check ---")

print(f"\nS57 vs S58 at fold (tau={tau_values[fold_idx]:.4f}):")
print(f"  Lambda_volovik:  S57={Lambda_fold_s57:+.6f}  S58={Lambda_eff_sweep[fold_idx]:+.6f}")
print(f"  Lambda_B2:       S57={Lambda_B2_fold_s57:+.6f}  S58={Lambda_B2_sweep[fold_idx]:+.6f}")
print(f"  Lambda_B1:       S57={Lambda_B1_fold_s57:+.6f}  S58={Lambda_B1_sweep[fold_idx]:+.6f}")
print(f"  Lambda_B3:       S57={Lambda_B3_fold_s57:+.6f}  S58={Lambda_B3_sweep[fold_idx]:+.6f}")
print(f"  w:               S57={w_fold_s57:.4f}  S58={w_sweep[fold_idx]:.4f}")

# GGE occupations comparison
print(f"\n  GGE occupations at fold:")
print(f"  {'Mode':>8s}  {'S57':>12s}  {'S58':>12s}  {'diff':>12s}")
for k in range(N_MODES):
    diff = fk_gge_sweep[fold_idx, k] - fk_gge_s57[k]
    print(f"  {branch_labels[k]:>8s}  {fk_gge_s57[k]:12.6f}  "
          f"{fk_gge_sweep[fold_idx, k]:12.6f}  {diff:+12.6f}")

# Energy comparison
print(f"\n  Energy at fold:")
print(f"  E_BCS:    S58={E_BCS_sweep[fold_idx]:.6f} M_KK")
print(f"  E_GGE:    S58={E_GGE_sweep[fold_idx]:.6f} M_KK")
print(f"  Delta_E:  S58={Delta_E_sweep[fold_idx]:+.6f} M_KK")
print(f"  E_cond:   S58={E_cond_sweep[fold_idx]:.6f} M_KK (S36: {E_cond_ED_8mode:.6f})")
print(f"  <N>:      S58={N_avg_sweep[fold_idx]:.6f}")

# ============================================================================
# Section 8: Representative Tau Points and Full Table
# ============================================================================

print("\n--- Section 8: Sector Decomposition at 5 Representative Tau ---")

repr_idx = [0, 12, fold_idx, 35, 49]
print(f"\n{'tau':>8s}  {'Lambda_eff':>12s}  {'Lambda_B2':>12s}  {'Lambda_B1':>12s}  "
      f"{'Lambda_B3':>12s}  {'R_cancel':>10s}  {'w':>8s}")
print("-" * 82)
for t in repr_idx:
    print(f"{tau_values[t]:8.4f}  {Lambda_eff_sweep[t]:+12.6f}  "
          f"{Lambda_B2_sweep[t]:+12.6f}  {Lambda_B1_sweep[t]:+12.6f}  "
          f"{Lambda_B3_sweep[t]:+12.6f}  {R_cancel[t]:10.6f}  {w_sweep[t]:8.4f}")

# Full sweep table
print(f"\n--- Full Sweep Table ---")
print(f"{'idx':>3s}  {'tau':>7s}  {'Lambda_eff':>12s}  {'R_cancel':>10s}  "
      f"{'dL/dtau':>10s}  {'w':>8s}  {'<N>':>8s}  {'T_eq':>8s}  {'E_cond':>8s}")
print("-" * 88)
for t in range(N_tau):
    print(f"{t:3d}  {tau_values[t]:7.4f}  {Lambda_eff_sweep[t]:+12.6f}  "
          f"{R_cancel[t]:10.6f}  {dLambda_dtau[t]:+10.4f}  "
          f"{w_sweep[t]:8.4f}  {N_avg_sweep[t]:8.4f}  {T_eq_sweep[t]:8.4f}  "
          f"{E_cond_sweep[t]:8.6f}")

# ============================================================================
# Section 9: Physical Units and CC Gap
# ============================================================================

print("\n--- Section 9: Physical Units ---")

Lambda_eff_GeV4 = Lambda_eff_sweep * M_KK**4
Lambda_ratio = np.abs(Lambda_eff_GeV4) / rho_Lambda_obs
Lambda_log10 = np.log10(np.maximum(Lambda_ratio, 1e-300))

Delta_E_GeV4 = Delta_E_sweep * M_KK**4
Delta_E_ratio = np.abs(Delta_E_GeV4) / rho_Lambda_obs
Delta_E_log10 = np.log10(np.maximum(Delta_E_ratio, 1e-300))

print(f"\nVolovik formula at fold:")
print(f"  Lambda_eff = {Lambda_eff_GeV4[fold_idx]:.4e} GeV^4")
print(f"  |Lambda/Lambda_obs| = {Lambda_ratio[fold_idx]:.4e}")
print(f"  CC gap = {Lambda_log10[fold_idx]:.1f} orders")

print(f"\nDirect method at fold:")
print(f"  Delta_E = {Delta_E_GeV4[fold_idx]:.4e} GeV^4")
print(f"  |Delta_E/Lambda_obs| = {Delta_E_ratio[fold_idx]:.4e}")
print(f"  CC gap = {Delta_E_log10[fold_idx]:.1f} orders")

# ============================================================================
# Section 10: Gate Verdict
# ============================================================================

print("\n" + "=" * 78)
print("GATE VERDICT: CC-CANCELLATION-SWEEP-58")
print("=" * 78)

Lambda_all_positive = np.all(Lambda_eff_sweep > 0)
Delta_all_positive = np.all(Delta_E_sweep > 0)
w_all_accel = np.all(w_sweep < -1.0/3.0)

print(f"\nClassification: {gate_class}")
print(f"R_cancel range: [{R_cancel_min:.6f}, {R_cancel_max:.6f}]")
print(f"R_cancel max/min ratio: {R_cancel_ratio:.2f}")
print(f"Lambda_eff range: [{Lambda_eff_sweep.min():+.6f}, {Lambda_eff_sweep.max():+.6f}] M_KK")
print(f"Lambda_eff sign: {'ALL POSITIVE' if Lambda_all_positive else 'SIGN CHANGES' if np.any(Lambda_eff_sweep < 0) and np.any(Lambda_eff_sweep > 0) else 'ALL NEGATIVE'}")
print(f"Delta_E sign: {'ALL POSITIVE' if Delta_all_positive else 'MIXED'}")
print(f"w range: [{w_sweep.min():.4f}, {w_sweep.max():.4f}]")
print(f"w < -1/3 at all tau: {w_all_accel}")

# ============================================================================
# Section 11: Save
# ============================================================================

results = {
    # Grid
    'tau_values': tau_values,
    'fold_idx': np.int64(fold_idx),
    'N_tau': np.int64(N_tau),
    'N_modes': np.int64(N_MODES),

    # Dirac spectrum
    'E_8_sweep': E_8_sweep,
    'E_8_fold_ref': E_8_fold_ref,

    # GGE and equilibrium
    'fk_gge_sweep': fk_gge_sweep,
    'fk_eq_sweep': fk_eq_sweep,
    'T_eq_sweep': T_eq_sweep,
    'N_avg_sweep': N_avg_sweep,

    # Energies
    'E_BCS_sweep': E_BCS_sweep,
    'E_GGE_sweep': E_GGE_sweep,
    'E_eq_sweep': E_eq_sweep,
    'E_cond_sweep': E_cond_sweep,
    'Delta_E_sweep': Delta_E_sweep,

    # Volovik formula
    'Lambda_eff_sweep': Lambda_eff_sweep,
    'Lambda_B2_sweep': Lambda_B2_sweep,
    'Lambda_B1_sweep': Lambda_B1_sweep,
    'Lambda_B3_sweep': Lambda_B3_sweep,
    'Lambda_permode_sweep': Lambda_permode_sweep,

    # Cancellation
    'R_cancel': R_cancel,
    'R_cancel_min': np.float64(R_cancel_min),
    'R_cancel_max': np.float64(R_cancel_max),
    'R_cancel_mean': np.float64(R_cancel_mean),
    'R_cancel_fold': np.float64(R_cancel_fold),
    'R_cancel_ratio': np.float64(R_cancel_ratio),
    'gate_class': np.array([gate_class]),

    # Derivatives
    'dLambda_dtau': dLambda_dtau,

    # Equation of state
    'P_vac_sweep': P_vac_sweep,
    'w_sweep': w_sweep,

    # Physical units
    'Lambda_eff_GeV4': Lambda_eff_GeV4,
    'Lambda_log10': Lambda_log10,
    'Delta_E_GeV4': Delta_E_GeV4,
    'Delta_E_log10': Delta_E_log10,

    # Gate
    'gate_name': np.array(['CC-CANCELLATION-SWEEP-58']),
    'gate_verdict': np.array(['INFO']),
    'gate_criterion': np.array(['R_cancel in [0.001, 0.01] = STRUCTURAL']),

    # Parameters
    'M_KK': np.float64(M_KK),
    'rho_Lambda_obs': np.float64(rho_Lambda_obs),
    'V_8x8': V_8x8,
    'rho_dos': rho,
    'branch_labels': np.array(branch_labels),
}

np.savez(os.path.join(SCRIPT_DIR, 's58_cc_cancellation_sweep.npz'), **results)
print(f"\nSaved: computations/session-58/s58_cc_cancellation_sweep.npz")

# ============================================================================
# Section 12: Plot
# ============================================================================

print("\n--- Section 12: Generating Plot ---")

fig, axes = plt.subplots(2, 3, figsize=(18, 10))

# Panel 1: Lambda_eff(tau) - both methods
ax = axes[0, 0]
ax.plot(tau_values, Lambda_eff_sweep, 'b-', lw=2, label='Volovik formula')
ax.plot(tau_values, Delta_E_sweep, 'r--', lw=1.5, label='Direct $\\Delta E$')
ax.axvline(tau_values[fold_idx], color='gray', ls=':', alpha=0.5, label='fold')
ax.axhline(0, color='gray', ls='-', alpha=0.2)
ax.set_xlabel('$\\tau$')
ax.set_ylabel('$\\Lambda_{\\mathrm{eff}}$ ($M_{KK}$)')
ax.set_title('(a) Vacuum Energy vs $\\tau$')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 2: R_cancel(tau)
ax = axes[0, 1]
ax.semilogy(tau_values, R_cancel, 'k-', lw=2)
ax.axhline(0.001, color='green', ls='--', alpha=0.7, label='structural floor')
ax.axhline(0.01, color='green', ls='--', alpha=0.7, label='structural ceiling')
ax.axvline(tau_values[fold_idx], color='gray', ls=':', alpha=0.5)
ax.set_xlabel('$\\tau$')
ax.set_ylabel('$R_{\\mathrm{cancel}}$')
ax.set_title('(b) Cancellation Ratio')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 3: Sector decomposition
ax = axes[0, 2]
ax.plot(tau_values, Lambda_B2_sweep, 'b-', lw=2, label='B2 (4 modes)')
ax.plot(tau_values, Lambda_B1_sweep, 'r-', lw=2, label='B1 (1 mode)')
ax.plot(tau_values, Lambda_B3_sweep, 'g-', lw=2, label='B3 (3 modes)')
ax.plot(tau_values, Lambda_eff_sweep, 'k--', lw=1.5, label='Total')
ax.axhline(0, color='gray', ls='-', alpha=0.3)
ax.axvline(tau_values[fold_idx], color='gray', ls=':', alpha=0.5)
ax.set_xlabel('$\\tau$')
ax.set_ylabel('$\\Lambda_{\\mathrm{sector}}$ ($M_{KK}$)')
ax.set_title('(c) Sector Decomposition')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 4: w(tau)
ax = axes[1, 0]
ax.plot(tau_values, w_sweep, 'k-', lw=2)
ax.axhline(-1.0/3.0, color='red', ls='--', alpha=0.7, label='$w = -1/3$')
ax.axhline(-1.0, color='blue', ls='--', alpha=0.7, label='$w = -1$')
ax.axvline(tau_values[fold_idx], color='gray', ls=':', alpha=0.5)
ax.set_xlabel('$\\tau$')
ax.set_ylabel('$w(\\tau)$')
ax.set_title('(d) Equation of State')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 5: dLambda/dtau
ax = axes[1, 1]
ax.plot(tau_values, dLambda_dtau, 'k-', lw=2)
ax.axhline(0, color='gray', ls='-', alpha=0.3)
ax.axvline(tau_values[fold_idx], color='gray', ls=':', alpha=0.5)
ax.set_xlabel('$\\tau$')
ax.set_ylabel('$d\\Lambda_{\\mathrm{eff}}/d\\tau$ ($M_{KK}$)')
ax.set_title('(e) $\\Lambda$ Derivative')
ax.grid(True, alpha=0.3)

# Panel 6: GGE occupations at fold
ax = axes[1, 2]
modes = np.arange(N_MODES)
w_bar = 0.35  # (local)
ax.bar(modes - w_bar/2, fk_gge_sweep[fold_idx], w_bar, color='blue', alpha=0.7, label='GGE')
ax.bar(modes + w_bar/2, fk_eq_sweep[fold_idx], w_bar, color='red', alpha=0.7, label='Equilibrium')
ax.set_xlabel('Mode index')
ax.set_ylabel('Occupation $f_k$')
ax.set_title(f'(f) Occupations at Fold ($\\tau$={tau_values[fold_idx]:.3f})')
ax.legend(fontsize=8)
ax.set_xticks(modes)
ax.set_xticklabels(branch_labels, rotation=45, fontsize=7)
ax.grid(True, alpha=0.3)

fig.suptitle(f'CC-CANCELLATION-SWEEP-58: Near-Cancellation ({gate_class})\n'
             f'$R_{{\\mathrm{{cancel}}}}$ $\\in$ [{R_cancel_min:.4f}, {R_cancel_max:.4f}], '
             f'max/min = {R_cancel_ratio:.1f}x', fontsize=12)
plt.tight_layout()
plt.savefig(os.path.join(SCRIPT_DIR, 's58_cc_cancellation_sweep.png'), dpi=150,
            bbox_inches='tight')
print("Saved: computations/session-58/s58_cc_cancellation_sweep.png")

print(f"\nTotal runtime: {time.time()-t_start:.1f}s")
print("DONE")
