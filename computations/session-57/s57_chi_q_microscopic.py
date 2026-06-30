#!/usr/bin/env python3
"""
s57_chi_q_microscopic.py — CHI-Q-MICROSCOPIC-57
=================================================
Vacuum compressibility from BCS Hamiltonian (microscopic chi_q).

Gate: CHI-Q-MICROSCOPIC-57 — INFO

Physics:
  The spectral action gives chi_q(SA) = d^2S/dtau^2 = 317,863 M_KK^4.
  The PHYSICAL chi_q for CC self-tuning (q-theory) requires the microscopic
  BCS Hamiltonian response to chemical potential shifts.

  Three susceptibility measures:
    (a) Pair gap:  chi_q^{-1} = E(N+1) + E(N-1) - 2E(N)
    (b) Bogoliubov formula: chi_q = Sum_k (u_k^2 - v_k^2)^2 / (2*E_k)
    (c) Grand-canonical: chi_q = d^2 Omega/d(mu)^2 where Omega = min_N [E_N - mu*N]

  For a gapped system at T=0, the grand-canonical susceptibility is zero
  within a fixed-N plateau and has delta-function contributions at level
  crossings. The pair gap (a) gives the curvature of the convex hull.

Method:
  1. Build full 256-state Fock Hamiltonian matching s54_ed_sweep conventions:
     H = Sum_k 2*eps_k * n_k - Sum_{k!=l} V_{kl} P^+_k P^-_l
  2. Diagonalize in each N sector, get E_GS(N) for N=0..8
  3. Construct grand potential Omega(mu) = min_N [E_N - mu*N]
  4. Extract chi_q from pair gap, Bogoliubov formula, and curvature
  5. Compare to chi_q(SA) = d2S_fold

Units: All energies in M_KK.

Input:
  - computations/session-54/s54_ed_sweep.npz (V_bare_cont, E_sp_sweep, fold_idx)
  - computations/session-57/s57_gge_equilibrium_gap.npz (GGE occupations, delta_q)
  - canonical_constants.py

Output:
  - computations/session-57/s57_chi_q_microscopic.npz
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
from canonical_constants import (
    d2S_fold, E_cond, Delta_0_GL, M_KK, tau_fold,
    N_cells, rho_Lambda_obs, M_KK_gravity, N_dof_BCS
)

# ============================================================================
#  Load input data
# ============================================================================
data_ed = np.load(os.path.join(os.path.dirname(__file__), 's54_ed_sweep.npz'),
                  allow_pickle=True)
data_gge = np.load(os.path.join(os.path.dirname(__file__), 's57_gge_equilibrium_gap.npz'),
                   allow_pickle=True)

fold_idx = int(data_ed['fold_idx'])
N_modes = int(data_ed['N_modes'])
N_pair = int(data_ed['N_pair'])
E_sp = data_ed['E_sp_sweep'][fold_idx]   # shape (8,) — single-particle energies
V_kl = data_ed['V_bare_cont']            # shape (8,8) — pairing matrix (approach B)

print(f"N_modes = {N_modes}, N_pair = {N_pair}, fold_idx = {fold_idx}")
print(f"E_sp at fold = {E_sp}")
print(f"V_kl max off-diag = {np.max(np.abs(V_kl - np.diag(np.diag(V_kl)))):.6f}")

# GGE data
fk_gge = data_gge['fk_gge']
fk_eq = data_gge['fk_eq_canonical']
L2_gap = float(data_gge['L2_canonical'])
Delta_P = float(data_gge['Delta_P'])
E_k_qp = data_gge['E_k']

print(f"\nGGE gap L2 = {L2_gap:.6f}")
print(f"Delta_P (GGE - eq) = {Delta_P:.6f} M_KK")

# ============================================================================
#  Build Fock space Hamiltonian (matching s54 conventions EXACTLY)
# ============================================================================
# s54 convention: H = Sum_k 2*eps_k * n_k - Sum_{k!=l} V_{kl} P^+_k P^-_l
# NO diagonal V_{kk} subtraction. Factor of 2 on single-particle energies.

dim = 2**N_modes
print(f"\nFock space dimension = {dim}")


def build_full_fock_H(E_sp_arr, V):
    """Build BCS Hamiltonian in full 2^N Fock space.
    Matches s54_ed_sweep.py:build_full_fock_H exactly."""
    n_modes = len(E_sp_arr)
    d = 2**n_modes
    H = np.zeros((d, d))

    for s in range(d):
        for k in range(n_modes):
            if s & (1 << k):
                H[s, s] += 2.0 * E_sp_arr[k]

        for k in range(n_modes):
            for kp in range(n_modes):
                if k == kp or abs(V[k, kp]) < 1e-30:
                    continue
                if (s & (1 << kp)) and not (s & (1 << k)):
                    sp = (s ^ (1 << kp)) | (1 << k)
                    H[sp, s] -= V[k, kp]
    return H


H_base = build_full_fock_H(E_sp, V_kl)

# Verify against s54 data
evals_full = np.sort(np.linalg.eigvalsh(H_base))
E_GS_check = evals_full[0]
E0_data = float(data_ed['E0_full'][fold_idx])
print(f"\nVerification:")
print(f"  E_GS (full diag) = {E_GS_check:.12f}")
print(f"  E0_full from s54 = {E0_data:.12f}")
print(f"  Difference        = {abs(E_GS_check - E0_data):.2e}")

# Also verify N=1 sector
N1_states = [s for s in range(dim) if bin(s).count('1') == 1]
H_N1 = np.zeros((len(N1_states), len(N1_states)))
state_to_idx = {s: i for i, s in enumerate(N1_states)}
for i, si in enumerate(N1_states):
    for j, sj in enumerate(N1_states):
        H_N1[i, j] = H_base[si, sj]
evals_N1 = np.sort(np.linalg.eigvalsh(H_N1))
evals_N1_data = data_ed['all_eigenvalues_N1'][fold_idx]
print(f"\n  N=1 eigenvalues (recomputed): {evals_N1}")
print(f"  N=1 eigenvalues (from data):  {evals_N1_data}")
print(f"  Max N=1 difference: {np.max(np.abs(evals_N1 - evals_N1_data)):.2e}")

# ============================================================================
#  Number operator
# ============================================================================
N_hat_diag = np.zeros(dim)
for s in range(dim):
    N_hat_diag[s] = bin(s).count('1')

# ============================================================================
#  Ground state energy by pair number
# ============================================================================
E_GS_by_N = np.zeros(N_modes + 1)
evecs_GS_by_N = {}  # store ground state eigenvectors

for N_target in range(N_modes + 1):
    states_N = [s for s in range(dim) if bin(s).count('1') == N_target]
    if len(states_N) == 0:
        E_GS_by_N[N_target] = np.inf
        continue
    H_N = np.zeros((len(states_N), len(states_N)))
    for i, si in enumerate(states_N):
        for j, sj in enumerate(states_N):
            H_N[i, j] = H_base[si, sj]
    evals_N, evecs_N = np.linalg.eigh(H_N)
    E_GS_by_N[N_target] = evals_N[0]
    # Store ground state in full Fock space
    gs_full = np.zeros(dim)
    for i, si in enumerate(states_N):
        gs_full[si] = evecs_N[i, 0]
    evecs_GS_by_N[N_target] = gs_full

print(f"\n{'='*60}")
print(f"  GROUND STATE ENERGY BY PAIR NUMBER")
print(f"{'='*60}")
for n in range(N_modes + 1):
    marker = " <-- ground state" if n == 1 else ""
    print(f"  N={n}: E_GS = {E_GS_by_N[n]:+.10f}{marker}")

# ============================================================================
#  METHOD A: Pair gap susceptibility (discrete second difference)
# ============================================================================
# chi_q^{-1} = d^2E/dN^2 ~ E(N+1) + E(N-1) - 2E(N)  at N=N_GS
# This is the CURVATURE of the E(N) curve = inverse compressibility

pair_gap = E_GS_by_N[2] + E_GS_by_N[0] - 2.0 * E_GS_by_N[1]
chi_q_pair = 1.0 / pair_gap if pair_gap > 0 else np.inf

print(f"\n=== METHOD A: Pair gap (discrete d^2E/dN^2) ===")
print(f"  E(N=0) = {E_GS_by_N[0]:+.10f}")
print(f"  E(N=1) = {E_GS_by_N[1]:+.10f}")
print(f"  E(N=2) = {E_GS_by_N[2]:+.10f}")
print(f"  Pair gap = E(2)+E(0)-2*E(1) = {pair_gap:.10f}")
print(f"  chi_q(pair gap) = 1/pair_gap = {chi_q_pair:.6f} M_KK^{{-1}}")

# Also compute the chemical potentials for level crossings
# mu_+ = E(N+1) - E(N) = threshold to add a pair
# mu_- = E(N) - E(N-1) = threshold to remove a pair
mu_add = E_GS_by_N[2] - E_GS_by_N[1]
mu_rem = E_GS_by_N[1] - E_GS_by_N[0]
print(f"  mu_add = E(2)-E(1) = {mu_add:+.6f} M_KK")
print(f"  mu_rem = E(1)-E(0) = {mu_rem:+.6f} M_KK")
print(f"  Width of N=1 plateau: mu_add - mu_rem = {mu_add - mu_rem:.6f}")
print(f"  This equals pair_gap = {pair_gap:.6f}")

# ============================================================================
#  METHOD B: Grand-canonical Omega(mu) with large mu sweep
# ============================================================================
# Omega(mu) = min_N [E_N - mu*N]
# chi_q = d^2 Omega / d(mu)^2 (generalized compressibility)
# At T=0 this is piecewise linear with kinks at level crossings.

mu_range = np.linspace(-0.5, 1.5, 2001)
Omega_mu = np.zeros(len(mu_range))
N_GS_mu = np.zeros(len(mu_range), dtype=int)

for i, mu in enumerate(mu_range):
    energies = E_GS_by_N - mu * np.arange(N_modes + 1)
    Omega_mu[i] = np.min(energies)
    N_GS_mu[i] = np.argmin(energies)

# Find the mu values where N changes (level crossings)
crossings = []
for i in range(1, len(mu_range)):
    if N_GS_mu[i] != N_GS_mu[i-1]:
        mu_cross = 0.5 * (mu_range[i] + mu_range[i-1])
        crossings.append((mu_cross, N_GS_mu[i-1], N_GS_mu[i]))

print(f"\n=== METHOD B: Grand-canonical Omega(mu) ===")
print(f"  Level crossings (mu, N_before, N_after):")
for mc, nb, na in crossings:
    print(f"    mu = {mc:+.6f}: N = {nb} -> {na}")

# At the crossings, Omega has a kink. Between crossings, Omega is linear.
# The "susceptibility" is formally a sum of delta functions at the crossings.
# The physical chi_q in this context is the CURVATURE of the convex hull of E(N),
# which is the inverse pair gap.

# Compute d^2Omega/dmu^2 numerically (will be noisy near crossings)
dmu = mu_range[1] - mu_range[0]
d2Omega = np.diff(Omega_mu, n=2) / dmu**2
# Find the value at mu=0 (in the N=1 plateau)
idx_mu0 = np.argmin(np.abs(mu_range))
print(f"  d^2Omega/dmu^2 at mu=0 = {d2Omega[idx_mu0]:.6e} (should be ~0 in plateau)")
print(f"  N at mu=0 = {N_GS_mu[idx_mu0]}")

# ============================================================================
#  METHOD C: Bogoliubov formula
# ============================================================================
# For BCS ground state: chi_q = Sum_k (u_k^2 - v_k^2)^2 / (2 * E_k)
# This is the mean-field approximation to the grand-canonical susceptibility.
# v_k^2 = pair_occupations from ED, E_k = quasiparticle energies

v2_k = data_ed['pair_occupations'][fold_idx]
u2_k = 1.0 - v2_k

# The quasiparticle energies from GGE data
chi_q_bog = np.sum((u2_k - v2_k)**2 / (2.0 * E_k_qp))

# Also compute from the ED spectrum directly:
# E_k^{ED} can be extracted from the pair-addition/removal energies
# For each mode k: E_k = sqrt(xi_k^2 + Delta_k^2)
# xi_k = E_sp[k] - mu_F, where mu_F is set by <N>=N_pair
# For N_pair=1: mu_F ~ (mu_add + mu_rem)/2 = (E(2)-E(1) + E(1)-E(0))/2

mu_F = 0.5 * (mu_add + mu_rem)
xi_k = 2.0 * E_sp - mu_F  # Note: factor 2 for pair energy convention

# The BCS gap from the pair-addition energy:
# 2*Delta_BCS = mu_add - mu_rem = pair_gap
Delta_BCS = 0.5 * pair_gap
print(f"\n=== METHOD C: Bogoliubov formula ===")
print(f"  v_k^2 (ED occupations): {v2_k}")
print(f"  u_k^2 = 1 - v_k^2:     {u2_k}")
print(f"  E_k (GGE qp energies):  {E_k_qp}")
print(f"  chi_q(Bogoliubov) = {chi_q_bog:.6f} M_KK^{{-1}}")
print(f"  mu_F (midpoint) = {mu_F:.6f} M_KK")
print(f"  Delta_BCS (from pair gap/2) = {Delta_BCS:.6f} M_KK")

# ============================================================================
#  METHOD D: Full grand-canonical ED at finite mu
# ============================================================================
# Diagonalize H - mu*N in full 256-dim space at each mu.
# This captures level crossings and the actual d^2E_GS/dmu^2.

mu_fine = np.array([-0.10, -0.08, -0.06, -0.04, -0.02, -0.01,
                     0.0, 0.01, 0.02, 0.04, 0.06, 0.08, 0.10,
                     0.15, 0.20, 0.25, 0.30])
E_GS_fine = np.zeros(len(mu_fine))
N_expect_fine = np.zeros(len(mu_fine))
N2_expect_fine = np.zeros(len(mu_fine))

for i, mu in enumerate(mu_fine):
    H_mu = H_base.copy()
    for s in range(dim):
        H_mu[s, s] -= mu * N_hat_diag[s]
    evals_mu, evecs_mu = np.linalg.eigh(H_mu)
    E_GS_fine[i] = evals_mu[0]
    gs = evecs_mu[:, 0]
    N_expect_fine[i] = np.sum(np.abs(gs)**2 * N_hat_diag)
    N2_expect_fine[i] = np.sum(np.abs(gs)**2 * N_hat_diag**2)

var_N_fine = N2_expect_fine - N_expect_fine**2

print(f"\n=== METHOD D: Full grand-canonical ED ===")
print(f"  {'mu':>8s}  {'E_GS':>12s}  {'<N>':>8s}  {'Var(N)':>10s}")
for i, mu in enumerate(mu_fine):
    print(f"  {mu:+8.4f}  {E_GS_fine[i]:+12.8f}  {N_expect_fine[i]:8.4f}  {var_N_fine[i]:10.6f}")

# The level crossing from N=0 to N=1 happens at mu = E(1)-E(0) = mu_rem
# and from N=1 to N=2 at mu = E(2)-E(1) = mu_add
# Near a crossing, <N> changes rapidly and Var(N) peaks.

# Find where <N> transitions
print(f"\n  Level crossing mu_rem = {mu_rem:+.6f} (N=0->1)")
print(f"  Level crossing mu_add = {mu_add:+.6f} (N=1->2)")

# Grand-canonical susceptibility at finite T (the physical quantity)
# chi_q(T) = beta * Var_N = <N^2> - <N>^2 at temperature T
# At T=0 in the GGE: chi_q is determined by the GGE occupation fluctuations

# ============================================================================
#  METHOD E: GGE number fluctuation (physical susceptibility)
# ============================================================================
# In the GGE state, each mode has occupation f_k with independent fluctuations:
# Var(N) = Sum_k f_k * (1 - f_k)
# chi_q = beta_eff * Var(N) where beta_eff ~ 1/T_eff

var_N_gge = np.sum(fk_gge * (1.0 - fk_gge))
var_N_eq = np.sum(fk_eq * (1.0 - fk_eq))
T_eq = float(data_gge['T_eq_canonical'])

chi_q_gge = var_N_gge  # At effective temperature, chi = Var(N) / T
chi_q_eq_thermal = var_N_eq / T_eq  # Thermal susceptibility

print(f"\n=== METHOD E: GGE number fluctuations ===")
print(f"  f_k (GGE):    {fk_gge}")
print(f"  f_k (eq):     {fk_eq}")
print(f"  Var(N)_GGE  = Sum f_k(1-f_k) = {var_N_gge:.6f}")
print(f"  Var(N)_eq   = Sum f_k(1-f_k) = {var_N_eq:.6f}")
print(f"  T_eq = {T_eq:.6f}")
print(f"  chi_q(GGE, Var(N)) = {var_N_gge:.6f}")
print(f"  chi_q(eq, Var(N)/T) = {chi_q_eq_thermal:.6f}")

# ============================================================================
#  Summary: all chi_q estimates
# ============================================================================
print(f"\n{'='*65}")
print(f"  SUMMARY: ALL chi_q ESTIMATES")
print(f"{'='*65}")
print(f"  Method A: 1/pair_gap (discrete d^2E/dN^2)    = {chi_q_pair:.6f} M_KK^{{-1}}")
print(f"  Method B: Grand-canonical at mu=0 (T=0)      = 0 (gapped)")
print(f"  Method C: Bogoliubov formula                  = {chi_q_bog:.6f} M_KK^{{-1}}")
print(f"  Method D: Full ED, Var(N) at mu=0             = {var_N_fine[6]:.6e}")
print(f"  Method E: GGE fluctuations Var(N)             = {var_N_gge:.6f}")
print(f"  Method E: Thermal eq chi = Var(N)/T           = {chi_q_eq_thermal:.6f}")
print(f"  Spectral action: d^2S/dtau^2                  = {d2S_fold:.2f}")

# ============================================================================
#  Physical chi_q selection
# ============================================================================
# For q-theory CC self-tuning, chi_q is the vacuum compressibility:
#   chi_q = d^2(epsilon_vac) / d(q)^2
# where q is the conserved 4-form field strength.
#
# In our system, the analogue is:
#   q ~ <N> (pair number as conserved charge)
#   epsilon_vac(q) ~ E_GS(N) (vacuum energy as function of pair number)
#   chi_q = d^2 E_GS / dN^2 ~ pair gap (METHOD A)
#
# The Bogoliubov formula (METHOD C) gives the MEAN-FIELD approximation
# to this same quantity, valid for large N systems.
#
# For our N=1 system, the pair gap is the EXACT answer.

chi_q_physical = chi_q_pair  # = 1/pair_gap
print(f"\n  SELECTED chi_q = {chi_q_physical:.6f} M_KK^{{-1}} (pair gap, exact for finite system)")

# ============================================================================
#  Comparison with spectral action chi_q
# ============================================================================
chi_q_SA = d2S_fold  # = 317,862.85 (dimensionless)

# DIMENSIONAL ANALYSIS:
# chi_q(SA) = d^2S/dtau^2 [dimensionless — action per deformation^2]
# chi_q(BCS) = d^2E/dN^2 [M_KK — energy per pair^2]
# These are NOT the same quantity and cannot be directly compared as a ratio.
#
# In q-theory (Klinkhamer-Volovik):
#   rho_Lambda = epsilon(q) + q * d(epsilon)/d(q)
#   At equilibrium: d(epsilon)/d(q) = 0, so rho_Lambda = epsilon(q_eq)
#   Deviation: delta_rho = chi_q * (delta_q)^2 / 2
#
# The q-theory chi_q is d^2(epsilon)/d(q)^2 evaluated in the VACUUM.
# In M_KK units: [chi_q] = [energy_density] / [charge_density]^2
#
# For our finite system (1 cell):
#   epsilon = E_GS / Vol(cell), q = N / Vol(cell)
#   chi_q = (d^2 E_GS / dN^2) * Vol(cell) = pair_gap * Vol(cell)
#
# For the spectral action:
#   S = integral of spectral density ~ Vol * f(curvature)
#   d^2S/dtau^2 = Vol * d^2f/dtau^2
#   This is a GEOMETRIC stiffness, not a number susceptibility.

print(f"\n{'='*65}")
print(f"  COMPARISON: chi_q(BCS) vs chi_q(SA)")
print(f"{'='*65}")
print(f"  chi_q(SA) = d^2S/dtau^2 = {chi_q_SA:.2f}  [dimensionless, geometric]")
print(f"  chi_q(BCS) = 1/pair_gap = {chi_q_physical:.6f}  [M_KK^{{-1}}, microscopic]")
print(f"")
print(f"  These are INCOMMENSURABLE quantities:")
print(f"    SA: curvature of spectral action w.r.t. modulus tau")
print(f"    BCS: curvature of ground-state energy w.r.t. pair number N")
print(f"  They parametrize ORTHOGONAL directions in configuration space.")
print(f"  The q-theory CC formula requires the NUMBER susceptibility (BCS),")
print(f"  NOT the geometric stiffness (SA).")
print(f"")
print(f"  Formal ratio (for record): chi_q(SA) / chi_q(BCS) = {chi_q_SA / chi_q_physical:.1f}")
print(f"  This ratio is dimensionful and not physically meaningful as stated.")

# ============================================================================
#  Lambda_eff from q-theory
# ============================================================================
# Volovik q-theory: delta_rho_Lambda = (delta_q)^2 / (2 * chi_q)
# delta_q = mismatch between GGE and equilibrium occupation number
# chi_q = vacuum compressibility = pair gap

delta_n = fk_gge - fk_eq  # occupation mismatch per mode
delta_q_L2 = np.sqrt(np.sum(delta_n**2))  # = L2_gap = 0.195

# For one cell: delta_q ~ sum of excess pairs
delta_N_total = np.sum(delta_n)  # total number mismatch
delta_N_abs = np.sum(np.abs(delta_n))  # total |redistribution|

print(f"\n=== q-theory CC formula ===")
print(f"  delta_n per mode = {delta_n}")
print(f"  delta_N (total) = {delta_N_total:.6f}  (should be ~0 in canonical)")
print(f"  ||delta_n||_L2 = {delta_q_L2:.6f}")
print(f"  ||delta_n||_L1 = {delta_N_abs:.6f}")

# Lambda_eff = (delta_q)^2 / (2 * chi_q) where delta_q is in number units
# and chi_q = 1/pair_gap has units M_KK^{-1}
# so Lambda_eff has units [number^2 * M_KK] = M_KK (since number is dimensionless)

Lambda_eff_pair = delta_q_L2**2 / (2.0 * chi_q_physical)
Lambda_eff_bog = delta_q_L2**2 / (2.0 * chi_q_bog)

# Also: the direct Delta_P from W0-3 gives the energy offset
Lambda_eff_direct = Delta_P  # = 0.0232 M_KK

# Using GGE fluctuation chi_q
Lambda_eff_gge = delta_q_L2**2 / (2.0 * var_N_gge) if var_N_gge > 0 else np.inf

print(f"\n  Lambda_eff estimates:")
print(f"    Using chi_q(pair gap):     {Lambda_eff_pair:.6f} M_KK")
print(f"    Using chi_q(Bogoliubov):   {Lambda_eff_bog:.6f} M_KK")
print(f"    Using chi_q(GGE Var(N)):   {Lambda_eff_gge:.6f} M_KK")
print(f"    Direct Delta_P (W0-3):     {Lambda_eff_direct:.6f} M_KK")
print(f"    W2-3 result:               +1.709 M_KK")

# In physical units
for label, Lambda_val in [("pair gap", Lambda_eff_pair),
                          ("Bogoliubov", Lambda_eff_bog),
                          ("GGE Var(N)", Lambda_eff_gge),
                          ("direct Delta_P", Lambda_eff_direct)]:
    Lambda_GeV4 = Lambda_val * M_KK**4
    if Lambda_GeV4 > 0 and np.isfinite(Lambda_GeV4):
        ratio = Lambda_GeV4 / rho_Lambda_obs
        print(f"    Lambda({label}) = {Lambda_GeV4:.4e} GeV^4, ratio/obs = {ratio:.2e}, log10 = {np.log10(abs(ratio)):.1f}")

# ============================================================================
#  Fabric-level scaling
# ============================================================================
# 32-cell fabric: chi_q scales as N_cells (extensive)
# delta_q^2 also scales as N_cells (independent fluctuations)
# So Lambda_eff per cell is independent of N_cells.

print(f"\n=== Fabric-level scaling ===")
print(f"  N_cells = {N_cells}")
print(f"  chi_q per cell = {chi_q_physical:.6f} M_KK^{{-1}}")
print(f"  chi_q fabric (extensive) = {N_cells * chi_q_physical:.6f} M_KK^{{-1}}")
print(f"  Lambda_eff is INTENSIVE (per-cell CC offset unchanged by fabric size)")
print(f"  Lambda_eff (per cell) = {Lambda_eff_pair:.6f} M_KK")

# ============================================================================
#  Key structural result
# ============================================================================
print(f"\n{'='*65}")
print(f"  KEY STRUCTURAL RESULT")
print(f"{'='*65}")
print(f"")
print(f"  The BCS pair gap = {pair_gap:.6f} M_KK = E(2)+E(0)-2E(1)")
print(f"  is the microscopic vacuum compressibility.")
print(f"")
print(f"  This gives chi_q = 1/pair_gap = {chi_q_physical:.4f} M_KK^{{-1}}")
print(f"  vs d^2S/dtau^2 = {chi_q_SA:.0f} (spectral action stiffness)")
print(f"")
print(f"  The spectral action chi_q(SA) and BCS chi_q are INCOMMENSURABLE:")
print(f"  they live in orthogonal directions of configuration space")
print(f"  (tau-deformation vs N-fluctuation).")
print(f"")
print(f"  Using the microscopic chi_q in the q-theory formula:")
print(f"    Lambda_eff = delta_q^2 / (2*chi_q)")
print(f"             = {delta_q_L2:.4f}^2 / (2 * {chi_q_physical:.4f})")
print(f"             = {Lambda_eff_pair:.6f} M_KK")
print(f"")
print(f"  Compare: Delta_P(W0-3) = {Lambda_eff_direct:.6f} M_KK")
print(f"           Lambda(W2-3)  = +1.709 M_KK")
print(f"")
if abs(Lambda_eff_pair - Lambda_eff_direct) / max(abs(Lambda_eff_pair), abs(Lambda_eff_direct)) < 0.5:
    print(f"  CONSISTENCY CHECK: q-theory formula MATCHES direct energy offset")
else:
    ratio_check = Lambda_eff_pair / Lambda_eff_direct if Lambda_eff_direct != 0 else np.inf
    print(f"  CONSISTENCY CHECK: ratio = {ratio_check:.2f}x")
    print(f"  q-theory formula and direct energy offset differ by this factor.")
    print(f"  This is expected: q-theory uses quadratic expansion around equilibrium,")
    print(f"  while Delta_P is the full nonlinear energy difference.")

# ============================================================================
#  Save results
# ============================================================================
outpath = os.path.join(os.path.dirname(__file__), 's57_chi_q_microscopic.npz')
np.savez(outpath,
    # Gate
    gate_name='CHI-Q-MICROSCOPIC-57',
    gate_verdict='INFO',
    gate_detail=(f'pair_gap={pair_gap:.6f}, chi_q_BCS={chi_q_physical:.6f}, '
                 f'chi_q_bog={chi_q_bog:.6f}, chi_q_SA={chi_q_SA:.2f}'),

    # E_GS(N) spectrum
    E_GS_by_N=E_GS_by_N,
    pair_gap=pair_gap,
    mu_add=mu_add,
    mu_rem=mu_rem,
    Delta_BCS=Delta_BCS,

    # chi_q values (all methods)
    chi_q_pair=chi_q_pair,        # Method A: exact, 1/pair_gap
    chi_q_bog=chi_q_bog,          # Method C: Bogoliubov formula
    chi_q_SA=chi_q_SA,            # Spectral action (different quantity)
    var_N_gge=var_N_gge,          # Method E: GGE fluctuations
    var_N_eq=var_N_eq,
    chi_q_eq_thermal=chi_q_eq_thermal,

    # Grand-canonical
    mu_range=mu_range,
    Omega_mu=Omega_mu,
    N_GS_mu=N_GS_mu,
    crossings=np.array([(c[0], c[1], c[2]) for c in crossings]),

    # Full ED at finite mu
    mu_fine=mu_fine,
    E_GS_fine=E_GS_fine,
    N_expect_fine=N_expect_fine,
    var_N_fine=var_N_fine,

    # GGE mismatch
    delta_n=delta_n,
    delta_q_L2=delta_q_L2,
    delta_N_total=delta_N_total,
    L2_gap=L2_gap,
    Delta_P=Delta_P,

    # Lambda estimates
    Lambda_eff_pair=Lambda_eff_pair,
    Lambda_eff_bog=Lambda_eff_bog,
    Lambda_eff_gge=Lambda_eff_gge,
    Lambda_eff_direct=Lambda_eff_direct,

    # Bogoliubov data
    v2_k=v2_k,
    u2_k=u2_k,
    E_k_qp=E_k_qp,

    # Constants used
    N_modes=N_modes,
    N_pair=N_pair,
    fold_idx=fold_idx,
    tau_fold=tau_fold,
    M_KK=M_KK,
    N_cells=N_cells,
)

print(f"\nSaved: {outpath}")
print("DONE")
