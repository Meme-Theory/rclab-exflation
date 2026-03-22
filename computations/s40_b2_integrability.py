"""
S40 W1-1: B2 Subsystem Integrability (B2-INTEG-40)

Gate: B2-INTEG-40
  PASS (B2 INTEGRABLE): <r>(B2-only) < 0.42 AND t_decay(B2) > 6 natural units
  FAIL (B2 THERMALIZES): <r>(B2-only) > 0.50 OR t_decay(B2) < 1 natural unit
  INTERMEDIATE: between these thresholds

Session 39 established:
  - Full 8-mode BCS: Brody beta=0.633 (63% GOE), INTEG-39 FAIL
  - B2 quartet carries 93% of pair wavefunction
  - Schur's lemma: B2 Casimir preserved to 3e-16, V(B2,B2) is rank-1 separable
  - LIED-39 PASS

This computation:
  1. Construct B2-only 16-state Fock space
  2. Project full H_BCS -> H_B2 (16x16)
  3. Level spacing ratio <r> within H_B2 particle-number sectors
  4. Thouless conductance g_T(B2)
  5. Survival probability P_B2(t) via exact matrix exponential
  6. B2-B1/B2-B3 coupling cross-check
"""

import numpy as np
from math import factorial, comb
from scipy import linalg
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import time

t_start = time.time()

# ============================================================
# 1. Load data and reconstruct full 256-state Hamiltonian
# ============================================================
print("=" * 70)
print("S40 W1-1: B2 Subsystem Integrability (B2-INTEG-40)")
print("=" * 70)

d_s39 = np.load('tier0-computation/s39_integrability_check.npz', allow_pickle=True)
d_rg = np.load('tier0-computation/s39_richardson_gaudin.npz', allow_pickle=True)

E_8 = d_s39['E_8']
V_phys = d_s39['V_phys']
labels = d_s39['labels']
evals_BCS_stored = d_s39['evals_BCS']

n_modes = 8
dim_full = 2**n_modes  # 256

print(f"\nE_8 = {E_8}")
print(f"Labels: {labels}")
print(f"Full Fock dim: {dim_full}")

# B2 = modes 0,1,2,3; B1 = mode 4; B3 = modes 5,6,7
B2_modes = [0, 1, 2, 3]
B1_modes = [4]
B3_modes = [5, 6, 7]
n_B2 = len(B2_modes)
dim_B2 = 2**n_B2  # 16

print(f"B2 modes: {B2_modes} (n={n_B2}, Fock dim={dim_B2})")
print(f"B2 energy: {E_8[0]:.8f} M_KK (4-fold degenerate)")

# ============================================================
# 2. Build Pauli operators in full 256-dim space
# ============================================================
I2 = np.eye(2, dtype=np.float64)
sz = np.array([[1.0, 0.0], [0.0, -1.0]])
sp = np.array([[0.0, 1.0], [0.0, 0.0]])
sm = np.array([[0.0, 0.0], [1.0, 0.0]])

def build_op(op_2x2, mode, n):
    """Build operator on mode `mode` in n-mode Fock space."""
    result = np.array([[1.0]])
    for k in range(n):
        result = np.kron(result, op_2x2 if k == mode else I2)
    return result

# Full 256-dim operators
SZ_full, SP_full, SM_full = [], [], []
for k in range(n_modes):
    SZ_full.append(build_op(sz, k, n_modes))
    SP_full.append(build_op(sp, k, n_modes))
    SM_full.append(build_op(sm, k, n_modes))

# Build full H_BCS
H_BCS = np.zeros((dim_full, dim_full))
for k in range(n_modes):
    n_k = 0.5 * (np.eye(dim_full) - SZ_full[k])
    H_BCS += 2 * E_8[k] * n_k
    for m in range(n_modes):
        H_BCS -= V_phys[k, m] * SP_full[k] @ SM_full[m]

assert np.allclose(H_BCS, H_BCS.T), "H_BCS not symmetric!"

# Verify against stored eigenvalues
evals_full, evecs_full = np.linalg.eigh(H_BCS)
assert np.allclose(np.sort(evals_full), np.sort(evals_BCS_stored), atol=1e-10), \
    "Eigenvalue mismatch with stored data!"
print(f"\nFull H_BCS eigenvalue cross-check: PASS (max delta = {np.max(np.abs(np.sort(evals_full) - np.sort(evals_BCS_stored))):.2e})")

# ============================================================
# 3. Construct B2-only projection
# ============================================================
print("\n" + "=" * 70)
print("3. B2 Subspace Projection")
print("=" * 70)

# The B2-only Fock space has 2^4 = 16 states.
# A state in the full 2^8 space is labeled by (b0, b1, ..., b7) where bi in {0,1}.
# The B2-only subspace consists of states with b4=b5=b6=b7=0 (B1 and B3 empty).

# Build the projector P_B2: a 256x16 matrix whose columns are the
# B2-only basis states in the full 256-dim space.

P_B2 = np.zeros((dim_full, dim_B2))
for state_B2 in range(dim_B2):
    # state_B2 encodes occupations of modes 0,1,2,3
    # Full state index: modes 0-3 from state_B2, modes 4-7 all zero
    # In the tensor product convention: mode 0 is the leftmost (most significant bit)
    # state_full = state_B2 * 2^4 + 0 (B1,B3 bits all zero)
    state_full = state_B2 * (2**(n_modes - n_B2))
    P_B2[state_full, state_B2] = 1.0

# Verify P_B2 is a valid projector frame
assert np.allclose(P_B2.T @ P_B2, np.eye(dim_B2)), "P_B2 not orthonormal!"
print(f"P_B2 shape: {P_B2.shape}")
print(f"P_B2^T P_B2 = I_{dim_B2}: VERIFIED")

# Project H_BCS onto B2 subspace
H_B2 = P_B2.T @ H_BCS @ P_B2
assert np.allclose(H_B2, H_B2.T), "H_B2 not symmetric!"
print(f"H_B2 shape: {H_B2.shape}")
print(f"H_B2 symmetric: VERIFIED")

# Also build H_B2 directly from B2-only operators as a cross-check
SZ_B2, SP_B2, SM_B2 = [], [], []
for k in range(n_B2):
    SZ_B2.append(build_op(sz, k, n_B2))
    SP_B2.append(build_op(sp, k, n_B2))
    SM_B2.append(build_op(sm, k, n_B2))

H_B2_direct = np.zeros((dim_B2, dim_B2))
V_B2B2 = V_phys[:4, :4]
E_B2 = E_8[0]  # All 4 B2 modes have same energy
for k in range(n_B2):
    n_k = 0.5 * (np.eye(dim_B2) - SZ_B2[k])
    H_B2_direct += 2 * E_B2 * n_k
    for m in range(n_B2):
        H_B2_direct -= V_B2B2[k, m] * SP_B2[k] @ SM_B2[m]

# Cross-check: H_B2 from projection should equal H_B2_direct
delta_H = np.linalg.norm(H_B2 - H_B2_direct, 'fro')
print(f"\n||H_B2(projected) - H_B2(direct)||_F = {delta_H:.6e}")
if delta_H < 1e-10:
    print("Cross-check: PASS (projection = direct construction)")
else:
    print(f"Cross-check: DISCREPANCY at {delta_H:.2e}")
    print("This means B2-B1/B3 coupling affects the projected H_B2 -- expected from off-diagonal V")

# ============================================================
# 4. Diagonalize H_B2 and analyze level statistics
# ============================================================
print("\n" + "=" * 70)
print("4. H_B2 Eigenspectrum and Level Statistics")
print("=" * 70)

evals_B2, evecs_B2 = np.linalg.eigh(H_B2)
print(f"\nH_B2 eigenvalues ({dim_B2} states):")
for i, e in enumerate(evals_B2):
    print(f"  |{i:2d}>: E = {e:.8f}")

# Build pair number operator for B2
N_B2_op = np.zeros((dim_B2, dim_B2))
for k in range(n_B2):
    N_B2_op += 0.5 * (np.eye(dim_B2) - SZ_B2[k])

# Classify eigenstates by pair number
N_B2_exp = np.diag(evecs_B2.T @ N_B2_op @ evecs_B2)
print(f"\nPair number classification:")
for n_pair in range(n_B2 + 1):
    mask = np.abs(N_B2_exp - n_pair) < 0.5
    idx = np.where(mask)[0]
    n_sec = len(idx)
    sec_evals = np.sort(evals_B2[idx])
    expected_dim = comb(n_B2, n_pair)
    print(f"  N={n_pair}: dim={n_sec} (expected C({n_B2},{n_pair})={expected_dim}), "
          f"E = {sec_evals}")

# Level spacing ratio <r> within each sector
print(f"\n--- Level Spacing Ratio <r> per B2 Sector ---")
r_B2_sectors = {}
r_B2_all = []
w_B2_all = []
for n_pair in range(n_B2 + 1):
    mask = np.abs(N_B2_exp - n_pair) < 0.5
    idx = np.where(mask)[0]
    sec_evals = np.sort(evals_B2[idx])
    n_sec = len(sec_evals)

    if n_sec < 4:
        print(f"  N={n_pair} (dim={n_sec}): too small for <r> statistics")
        continue

    spacings = np.diff(sec_evals)
    spacings = spacings[spacings > 1e-12]
    if len(spacings) < 3:
        print(f"  N={n_pair} (dim={n_sec}): insufficient non-degenerate spacings")
        continue

    r_vals = [min(spacings[i], spacings[i+1]) / max(spacings[i], spacings[i+1])
              for i in range(len(spacings) - 1)]
    r_mean = np.mean(r_vals)
    r_std = np.std(r_vals) / np.sqrt(len(r_vals)) if len(r_vals) > 1 else 0
    r_B2_sectors[n_pair] = (r_mean, r_std, len(r_vals))
    r_B2_all.append(r_mean)
    w_B2_all.append(n_sec)

    if r_mean < 0.42:
        cls = "POISSON"
    elif r_mean > 0.50:
        cls = "GOE"
    else:
        cls = "intermediate"

    print(f"  N={n_pair} (dim={n_sec}): <r> = {r_mean:.4f} +/- {r_std:.4f} "
          f"(n_ratios={len(r_vals)}) [{cls}]")

# Global <r> for B2
if len(r_B2_all) > 0:
    r_B2_global = np.average(r_B2_all, weights=w_B2_all)
else:
    # Fall back: use all B2 eigenvalues (unsectored)
    spacings_all = np.diff(evals_B2)
    spacings_all = spacings_all[spacings_all > 1e-12]
    r_vals_all = [min(spacings_all[i], spacings_all[i+1]) / max(spacings_all[i], spacings_all[i+1])
                  for i in range(len(spacings_all) - 1)]
    r_B2_global = np.mean(r_vals_all)

print(f"\n  B2 global weighted <r> = {r_B2_global:.4f}")
print(f"  Reference: Poisson = 0.386, GOE = 0.536")

# The 16-state B2 Fock space has sectors: N=0(1), N=1(4), N=2(6), N=3(4), N=4(1)
# Only N=2 has enough states (6) for meaningful statistics.
# We should also compute the UNSECTORED statistics as a diagnostic.
print(f"\n--- Unsectored B2 Level Statistics ---")
spacings_unsectored = np.diff(evals_B2)
spacings_unsectored = spacings_unsectored[spacings_unsectored > 1e-12]
if len(spacings_unsectored) >= 3:
    r_unsectored = [min(spacings_unsectored[i], spacings_unsectored[i+1]) /
                    max(spacings_unsectored[i], spacings_unsectored[i+1])
                    for i in range(len(spacings_unsectored) - 1)]
    r_unsectored_mean = np.mean(r_unsectored)
    print(f"  Unsectored <r> = {r_unsectored_mean:.4f} (from {len(r_unsectored)} ratios)")
    print(f"  NOTE: Unsectored mixes symmetry sectors, which ALWAYS pushes toward Poisson")
    print(f"  (Berry-Tabor: superimposed independent spectra -> Poisson)")

# ============================================================
# 5. Richardson-Gaudin integrability test for B2-only
# ============================================================
print("\n" + "=" * 70)
print("5. B2-Only Richardson-Gaudin Integrability Analysis")
print("=" * 70)

# V(B2,B2) rank structure
U_B2, S_B2, Vt_B2 = np.linalg.svd(V_B2B2)
print(f"\nV(B2,B2) singular values: {S_B2}")
print(f"Rank-1 fraction: {S_B2[0]**2 / np.sum(S_B2**2):.6f}")
rank1_frac_B2 = S_B2[0]**2 / np.sum(S_B2**2)

# Build rank-1 and remainder
V_B2_rank1 = S_B2[0] * np.outer(U_B2[:, 0], Vt_B2[0, :])
V_B2_rem = V_B2B2 - V_B2_rank1

print(f"||V_B2_rank1||_F = {np.linalg.norm(V_B2_rank1, 'fro'):.6f}")
print(f"||V_B2_rem||_F = {np.linalg.norm(V_B2_rem, 'fro'):.6f}")
print(f"||V_B2_rem||/||V_B2|| = {np.linalg.norm(V_B2_rem, 'fro') / np.linalg.norm(V_B2B2, 'fro'):.6f}")

# For B2, all 4 modes are degenerate (E_B2 = 0.8453).
# With degenerate energies and rank-1 V, the system is a SINGLE quasi-spin S=2.
# H_B2(rank-1) = 2*E_B2 * N - sigma_1 * (sum_k u_k sigma_+^k)(sum_m u_m sigma_-^m)
# This is equivalent to H = 2*E*N - G*S_+*S_- where S_+ = sum u_k sigma_+^k
# and G = sigma_1 (largest singular value).
# A single quasi-spin is trivially integrable: H, S^2, S_z are all conserved.

# For rank-1 V, build the "pair creation" operator
u1_B2 = U_B2[:, 0]  # First left singular vector
print(f"\nRank-1 coupling vector u_1: {u1_B2}")

# Quasi-spin operators for the degenerate B2 subspace
# S_+ = sum_k u_k * sigma_+^k (weighted pair creation)
S_plus_B2 = sum(u1_B2[k] * SP_B2[k] for k in range(n_B2))
S_minus_B2 = sum(u1_B2[k] * SM_B2[k] for k in range(n_B2))
S_z_B2 = sum(0.5 * SZ_B2[k] for k in range(n_B2))

# S^2 = S+S- + Sz(Sz - 1) ... careful with non-orthonormal u_k
# Actually for PAIR operators with non-orthonormal u_k, S+S- is NOT standard SU(2)
# Let's check the algebra directly:
# [S_-, S_+] = sum_{k} |u_k|^2 * [sigma_-^k, sigma_+^k] = -sum_k |u_k|^2 * sigma_z^k
comm_mp = S_minus_B2 @ S_plus_B2 - S_plus_B2 @ S_minus_B2
expected_comm = -sum(u1_B2[k]**2 * SZ_B2[k] for k in range(n_B2))
print(f"||[S-, S+] - expected||_F = {np.linalg.norm(comm_mp - expected_comm, 'fro'):.2e}")

# Since u_k are NOT all equal, this is NOT standard SU(2) unless u_k are uniform.
# Check uniformity:
print(f"u_k values: {u1_B2}")
print(f"u_k std/mean: {np.std(u1_B2)/np.abs(np.mean(u1_B2)):.4f}")

# Build the rank-1 Hamiltonian for B2 and check its spectrum
H_B2_rank1 = np.zeros((dim_B2, dim_B2))
for k in range(n_B2):
    n_k = 0.5 * (np.eye(dim_B2) - SZ_B2[k])
    H_B2_rank1 += 2 * E_B2 * n_k
    for m in range(n_B2):
        H_B2_rank1 -= V_B2_rank1[k, m] * SP_B2[k] @ SM_B2[m]

evals_B2_rank1 = np.linalg.eigvalsh(H_B2_rank1)
print(f"\nH_B2(rank-1) eigenvalues: {evals_B2_rank1}")

# Compare with full H_B2
print(f"H_B2(full) eigenvalues:   {evals_B2}")
print(f"Max |delta E|: {np.max(np.abs(evals_B2 - evals_B2_rank1)):.6e}")

# H_B2 with remainder
H_B2_rem = H_B2_direct - H_B2_rank1
print(f"\n||H_B2_rem||_F = {np.linalg.norm(H_B2_rem, 'fro'):.6e}")
print(f"||H_B2_rem||/||H_B2||_F = {np.linalg.norm(H_B2_rem, 'fro') / np.linalg.norm(H_B2_direct, 'fro'):.6e}")

# ============================================================
# 6. Thouless conductance for B2
# ============================================================
print("\n" + "=" * 70)
print("6. B2 Thouless Conductance")
print("=" * 70)

# Thouless conductance g_T = |delta_n / delta_E|^2
# where delta_n is the level displacement when boundary conditions change.
#
# For our discrete system, we use a twist: perturb the hopping phase of
# one B2 mode by exp(i*phi), compute eigenvalue sensitivity.
#
# Alternatively, use the matrix element formulation:
# g_T ~ (V_rms / Delta)^2 where V_rms is the integrability-breaking
# perturbation and Delta is the mean level spacing.
#
# Here we take V_rem (non-separable part of V_B2B2) as the perturbation.

# Method 1: V_rem in H_B2 eigenbasis
H_B2_rem_eigbasis = evecs_B2.T @ H_B2_rem @ evecs_B2
off_diag_B2 = H_B2_rem_eigbasis - np.diag(np.diag(H_B2_rem_eigbasis))
V_rms_B2 = np.sqrt(np.mean(off_diag_B2**2))

# Mean level spacing within the largest sector (N=2, dim=6)
N_B2_exp_B2 = np.diag(evecs_B2.T @ N_B2_op @ evecs_B2)
mask_N2 = np.abs(N_B2_exp_B2 - 2) < 0.5
idx_N2 = np.where(mask_N2)[0]
sec_evals_N2 = np.sort(evals_B2[idx_N2])
mean_spacing_B2_N2 = np.mean(np.diff(sec_evals_N2)) if len(sec_evals_N2) > 1 else 1.0

# Overall mean spacing
mean_spacing_B2_all = np.mean(np.diff(evals_B2))

g_T_B2_N2 = V_rms_B2 / mean_spacing_B2_N2
g_T_B2_all = V_rms_B2 / mean_spacing_B2_all

print(f"\nV_rms(B2 perturbation) = {V_rms_B2:.6e}")
print(f"Mean spacing (N=2 sector) = {mean_spacing_B2_N2:.6e}")
print(f"Mean spacing (all B2) = {mean_spacing_B2_all:.6e}")
print(f"Thouless g_T (N=2) = {g_T_B2_N2:.6f}")
print(f"Thouless g_T (all) = {g_T_B2_all:.6f}")
print(f"  g_T << 1: localized (integrable)")
print(f"  g_T ~ 1: delocalized (chaotic)")

# Method 2: Twist boundary condition
# Add a phase twist phi to mode 0: sigma_+^0 -> e^{i*phi} sigma_+^0
# This is equivalent to adding a perturbation delta_H ~ phi * current_operator
# The Thouless conductance is the curvature of eigenvalues with respect to phi.
phi_vals = np.linspace(0, 0.01, 5)
evals_twist = []
for phi in phi_vals:
    H_twist = np.zeros((dim_B2, dim_B2), dtype=np.complex128)
    for k in range(n_B2):
        n_k = 0.5 * (np.eye(dim_B2) - SZ_B2[k])
        H_twist += 2 * E_B2 * n_k
        for m_idx in range(n_B2):
            phase = np.exp(1j * phi) if k == 0 else 1.0
            phase_m = np.exp(-1j * phi) if m_idx == 0 else 1.0
            H_twist -= V_B2B2[k, m_idx] * phase * phase_m * (SP_B2[k] @ SM_B2[m_idx]).astype(np.complex128)
    evals_twist.append(np.linalg.eigvalsh(H_twist))

evals_twist = np.array(evals_twist)
# Numerical second derivative: d^2E/dphi^2
d2E_dphi2 = np.zeros(dim_B2)
for i in range(dim_B2):
    # Use finite difference
    if len(phi_vals) >= 3:
        dphi = phi_vals[1] - phi_vals[0]
        d2E_dphi2[i] = (evals_twist[2, i] - 2*evals_twist[1, i] + evals_twist[0, i]) / dphi**2

g_T_twist = np.abs(d2E_dphi2) / (mean_spacing_B2_all * dim_B2) if mean_spacing_B2_all > 0 else np.zeros(dim_B2)
print(f"\nTwist Thouless conductance (per level):")
print(f"  Mean g_T(twist) = {np.mean(g_T_twist):.6e}")
print(f"  Max g_T(twist) = {np.max(g_T_twist):.6e}")

# ============================================================
# 7. Survival probability P_B2(t)
# ============================================================
print("\n" + "=" * 70)
print("7. B2 Survival Probability P_B2(t)")
print("=" * 70)

# We need the BCS PAIRED ground state, not the vacuum.
# The vacuum (N=0) is trivially in B2 and never decays.
# The physically relevant state is the lowest N=1 eigenstate,
# which is the Richardson-Gaudin one-pair ground state with 93% B2 weight.

# Build pair number operator in full space
N_pair_full = np.zeros((dim_full, dim_full))
for k in range(n_modes):
    N_pair_full += 0.5 * (np.eye(dim_full) - SZ_full[k])

N_pair_diag = np.diag(evecs_full.T @ N_pair_full @ evecs_full)

# Find N=1 ground state
mask_N1 = np.abs(N_pair_diag - 1) < 0.5
idx_N1 = np.where(mask_N1)[0]
N1_evals = evals_full[idx_N1]
gs_N1_idx = idx_N1[np.argmin(N1_evals)]
psi_gs_N1 = evecs_full[:, gs_N1_idx]
E_gs_N1 = evals_full[gs_N1_idx]

print(f"\nN=1 BCS ground state energy: {E_gs_N1:.8f}")
print(f"N=1 pair number check: <N> = {N_pair_diag[gs_N1_idx]:.6f}")

# Also report the vacuum
gs_idx = np.argmin(evals_full)
print(f"Vacuum (N=0) energy: {evals_full[gs_idx]:.8f}, <N> = {N_pair_diag[gs_idx]:.4f}")
print(f"NOTE: Vacuum is trivially B2-only (P_B2=1 forever). Using N=1 state for decay.")

# Project N=1 ground state onto B2 subspace
psi_B2_proj = P_B2.T @ psi_gs_N1  # 16-component vector
norm_B2 = np.linalg.norm(psi_B2_proj)
print(f"\n||P_B2 |GS_N1>|| = {norm_B2:.8f}")
print(f"B2 weight of N=1 ground state: {norm_B2**2:.8f}")

# Cross-check with stored pair wavefunction
psi_pair_stored = d_rg['psi_pair_s38']
B2_weight_stored = np.sum(psi_pair_stored[:4]**2)
print(f"S38 stored B2 weight: {B2_weight_stored:.8f}")

if norm_B2 > 1e-10:
    psi_B2_init = psi_B2_proj / norm_B2  # Normalized initial state in B2 subspace
else:
    print("WARNING: N=1 ground state has negligible B2 weight!")
    psi_B2_init = evecs_B2[:, 0]

# For the DECAY calculation, we evolve in the FULL 256-dim space.
# Use the B2-projected N=1 state (normalized, lifted back to full space).
# P_B2(t) = ||P_B2 exp(-iHt) |psi_B2(0)>||^2

psi_full_B2_init = P_B2 @ psi_B2_init  # Lift back to 256-dim
norm_check = np.linalg.norm(psi_full_B2_init)
print(f"||psi_B2_init (full space)|| = {norm_check:.10f}")

# Decompose initial state in full energy eigenbasis
coeffs = evecs_full.T @ psi_full_B2_init
print(f"Sum |c_n|^2 = {np.sum(np.abs(coeffs)**2):.10f} (should be 1)")

# Time evolution: P_B2(t) = |sum_n |c_n|^2 exp(-i E_n t)|^2
# Wait -- that's the RETURN probability to the initial state.
# The SURVIVAL probability in the B2 SUBSPACE is:
# P_B2(t) = ||P_B2 exp(-iHt) |psi>||^2 = sum_{k in B2} |<k|exp(-iHt)|psi>|^2
# which requires the projection onto the full B2 subspace, not just back to |psi>.

# For the B2 subspace survival probability:
# P_B2(t) = <psi| exp(+iHt) P_B2^full exp(-iHt) |psi>
# where P_B2^full = P_B2 @ P_B2^T is the full-space projector onto B2 states.

# In the energy eigenbasis:
# P_B2(t) = sum_{n,m} c_n* c_m exp(i(E_n-E_m)t) * (P_B2^full)_{nm}
# where (P_B2^full)_{nm} = <n|P_B2^full|m>

P_B2_full = P_B2 @ P_B2.T  # 256x256 projector
P_B2_eigbasis = evecs_full.T @ P_B2_full @ evecs_full  # (P_B2)_{nm} in energy basis

# Also compute the return probability (fidelity):
# F(t) = |<psi(0)|exp(-iHt)|psi(0)>|^2 = |sum_n |c_n|^2 exp(-i E_n t)|^2

# Time grid
# The relevant timescale is set by the level spacing: t ~ 2*pi / Delta_E
# Also compute up to the Nazarewicz estimate t_decay ~ 0.13
Delta_E_min = np.min(np.abs(np.diff(evals_full[evals_full < evals_full[gs_idx] + 5])))
t_max = max(30.0, 2 * np.pi / Delta_E_min * 3) if Delta_E_min > 0 else 30.0
t_max = min(t_max, 100.0)  # Cap at 100 natural units
n_t = 2000

t_arr = np.linspace(0, t_max, n_t)

print(f"\nTime evolution: t in [0, {t_max:.2f}], {n_t} points")
print(f"Minimum energy gap (near GS): {Delta_E_min:.6e}")

# Efficient computation using eigendecomposition
# P_B2(t) = sum_{n,m} c_n* c_m * (P_B2)_{nm} * exp(i*(E_n - E_m)*t)
# This is expensive for full sum. Use matrix form:
# P_B2(t) = Tr[rho(t) @ P_B2^full] where rho(t) = |psi(t)><psi(t)|
# = sum_{n,m} c_n c_m* exp(-i(E_n-E_m)t) P_B2_{mn}

# Precompute the double sum matrix
# A_{nm} = c_n * c_m* * (P_B2)_{mn}
A_mat = np.outer(coeffs, np.conj(coeffs)) * P_B2_eigbasis.T

P_B2_t = np.zeros(n_t)
F_return_t = np.zeros(n_t)

for it, t in enumerate(t_arr):
    phases = np.exp(-1j * evals_full * t)
    # P_B2(t) = sum_{n,m} A_{nm} exp(-i(E_n - E_m)t)
    # = sum_{n,m} A_{nm} exp(-i*E_n*t) exp(+i*E_m*t)
    # = phases^dag @ A @ phases... no.
    # P_B2(t) = |sum_n c_n exp(-iE_n t) <n|P_B2^full|psi(t)>...
    # Let me just compute it directly:
    psi_t_coeffs = coeffs * np.exp(-1j * evals_full * t)
    # P_B2(t) = psi_t^dag @ P_B2_eigbasis @ psi_t
    P_B2_t[it] = np.real(np.conj(psi_t_coeffs) @ P_B2_eigbasis @ psi_t_coeffs)
    # Return probability
    F_return_t[it] = np.abs(np.sum(np.abs(coeffs)**2 * np.exp(-1j * evals_full * t)))**2

print(f"\nP_B2(0) = {P_B2_t[0]:.8f} (should be 1.0)")
print(f"F_return(0) = {F_return_t[0]:.8f} (should be 1.0)")

# Find decay time: when P_B2(t) first drops below 1/e
idx_decay = np.where(P_B2_t < 1.0/np.e)[0]
if len(idx_decay) > 0:
    t_decay_B2 = t_arr[idx_decay[0]]
    print(f"\nP_B2 decay time (1/e): t_decay = {t_decay_B2:.6f} natural units")
else:
    t_decay_B2 = np.inf
    print(f"\nP_B2 never drops below 1/e in [0, {t_max:.1f}]!")
    print(f"  Min P_B2 = {np.min(P_B2_t):.6f} at t = {t_arr[np.argmin(P_B2_t)]:.4f}")

# Also extract the INITIAL decay rate via short-time expansion:
# P_B2(t) ~ 1 - Gamma_B2 * t + ... (exponential) or 1 - (sigma*t)^2 + ... (quadratic)
# Fit to first few points
dt_short = t_arr[1]
if dt_short > 0:
    dP_dt_0 = (P_B2_t[1] - P_B2_t[0]) / dt_short
    d2P_dt2_0 = (P_B2_t[2] - 2*P_B2_t[1] + P_B2_t[0]) / dt_short**2
    print(f"\nShort-time expansion:")
    print(f"  dP/dt|_0 = {dP_dt_0:.6e}")
    print(f"  d2P/dt2|_0 = {d2P_dt2_0:.6e}")
    # Quadratic decay: P ~ 1 - (sigma*t)^2 -> sigma^2 = -d2P/dt2/2
    if d2P_dt2_0 < 0:
        sigma_zeno = np.sqrt(-d2P_dt2_0 / 2)
        t_zeno = 1.0 / sigma_zeno
        print(f"  Zeno time: t_Z = 1/sigma = {t_zeno:.6f}")
        print(f"  Energy spread: sigma = {sigma_zeno:.6f}")

# Time-averaged survival probability (long-time)
# P_B2(infty) = sum_n |c_n|^2 * (P_B2)_{nn} (diagonal terms only)
P_B2_inf = np.sum(np.abs(coeffs)**2 * np.diag(P_B2_eigbasis))
print(f"\nLong-time average P_B2(inf) = {P_B2_inf:.6f}")
print(f"  (This is the IPR-weighted B2 projection: 1/N_eff for B2 content)")

# ============================================================
# 8. Fermi Golden Rule cross-check
# ============================================================
print("\n" + "=" * 70)
print("8. Fermi Golden Rule Cross-Check")
print("=" * 70)

# The B2-B1 and B2-B3 coupling matrix elements
V_B2_B1 = V_phys[:4, 4]
V_B2_B3 = V_phys[:4, 5:]

print(f"\nB2-B1 coupling: V(B2,B1) = {V_B2_B1}")
print(f"  ||V(B2,B1)|| = {np.linalg.norm(V_B2_B1):.6f}")
print(f"  All equal: {np.allclose(V_B2_B1, V_B2_B1[0])}")

print(f"\nB2-B3 coupling matrix:")
for i in range(4):
    print(f"  B2[{i}]: {V_B2_B3[i]}")
print(f"  ||V(B2,B3)||_F = {np.linalg.norm(V_B2_B3):.6f}")

# B2 level spacing (within B2-only Hamiltonian)
spacings_B2 = np.diff(evals_B2)
mean_sp_B2 = np.mean(spacings_B2[spacings_B2 > 1e-12])
print(f"\nB2-only mean level spacing: {mean_sp_B2:.6f}")

# FGR decay rate: Gamma ~ 2*pi * |V_coupling|^2 * rho_chaotic
# V_coupling = typical B2-to-outside matrix element
# rho_chaotic = density of states in the B1+B3 bath

# Estimate rho_chaotic from the full spectrum restricted to non-B2 states
# The "bath" states have at least one B1 or B3 mode occupied.
# Count: 256 - 16 = 240 bath states
n_bath = dim_full - dim_B2
bandwidth = evals_full[-1] - evals_full[0]
rho_bath = n_bath / bandwidth

# Average coupling: use off-diagonal blocks of H_BCS in B2/bath decomposition
H_coupling = P_B2.T @ H_BCS @ (np.eye(dim_full) - P_B2_full)
# This is 16 x 240 matrix
V_coupling_rms = np.sqrt(np.mean(H_coupling**2))

# More targeted: use the N=1 sector coupling
# In N=1, B2 states are the 4 single-B2-mode states; bath states are the 4 B1/B3 states
# H_coupling_N1 is 4x4
H_1_full = np.diag(2 * E_8) - V_phys  # 8x8 one-pair Hamiltonian
V_B2_bath_N1 = V_phys[:4, 4:]  # 4x4 (B2 to B1+B3)
V_coupling_N1_rms = np.sqrt(np.mean(V_B2_bath_N1**2))

Gamma_FGR = 2 * np.pi * V_coupling_rms**2 * rho_bath
Gamma_FGR_N1 = 2 * np.pi * V_coupling_N1_rms**2 * (4 / (2 * np.max(np.abs(E_8 - E_8[0]))))
t_decay_FGR = 1.0 / Gamma_FGR if Gamma_FGR > 0 else np.inf

print(f"\nFermi Golden Rule estimates:")
print(f"  V_coupling_rms (full Fock) = {V_coupling_rms:.6e}")
print(f"  V_coupling_rms (N=1 sector) = {V_coupling_N1_rms:.6e}")
print(f"  Bath density rho = {rho_bath:.4f}")
print(f"  Gamma_FGR (full) = {Gamma_FGR:.6f}")
print(f"  t_decay_FGR = 1/Gamma = {t_decay_FGR:.6f}")
print(f"\n  Naz estimate: Gamma ~ 7.5, t_decay ~ 0.13")
print(f"  Our Gamma_FGR / Naz Gamma = {Gamma_FGR / 7.5:.4f}")

# Targeted Naz-style estimate: use V(B2,B1) and V(B2,B3) directly
V_B2_out_sq = np.sum(V_B2_B1**2) + np.sum(V_B2_B3**2)
V_B2_out_rms = np.sqrt(V_B2_out_sq / (4 + 12))  # 4 B2-B1 + 12 B2-B3 elements

# Density of chaotic states: from S39, the B1+B3 sector has ~240 states over bandwidth ~17
# But the RELEVANT density is for states at the B2 energy
rho_at_B2_E = dim_full / bandwidth  # crude estimate
Gamma_Naz = 2 * np.pi * V_B2_out_rms**2 * rho_at_B2_E
t_decay_Naz = 1.0 / Gamma_Naz if Gamma_Naz > 0 else np.inf

print(f"\n  V_B2_out_rms = {V_B2_out_rms:.6f}")
print(f"  rho(at B2 energy) ~ {rho_at_B2_E:.2f}")
print(f"  Gamma_Naz(recalc) = {Gamma_Naz:.4f}")
print(f"  t_decay_Naz(recalc) = {t_decay_Naz:.4f}")

# ============================================================
# 9. B2-only level statistics within the N=2 sector (largest)
# ============================================================
print("\n" + "=" * 70)
print("9. N=2 Sector Detailed Analysis")
print("=" * 70)

# The N=2 sector has C(4,2) = 6 states. This is the ONLY sector large enough
# for any statistical analysis. Let's examine it carefully.

mask_N2_B2 = np.abs(N_B2_exp_B2 - 2) < 0.5
idx_N2_B2 = np.where(mask_N2_B2)[0]
evals_N2 = np.sort(evals_B2[idx_N2_B2])

print(f"\nN=2 sector of H_B2: dim = {len(evals_N2)}")
print(f"Eigenvalues: {evals_N2}")
spacings_N2 = np.diff(evals_N2)
print(f"Spacings: {spacings_N2}")

if len(spacings_N2) >= 3:
    r_N2 = [min(spacings_N2[i], spacings_N2[i+1]) / max(spacings_N2[i], spacings_N2[i+1])
             for i in range(len(spacings_N2) - 1)]
    r_N2_mean = np.mean(r_N2)
    r_N2_vals = r_N2
    print(f"Level ratios r_i: {r_N2}")
    print(f"<r> = {r_N2_mean:.4f}")
    print(f"  Poisson: 0.386, GOE: 0.536")
else:
    r_N2_mean = float('nan')
    r_N2_vals = []
    print("Insufficient spacings for ratio statistics")

# For a 6-dimensional sector, the sampling statistics are poor.
# But we can also check degeneracy patterns.
# For integrable (rank-1 V), the N=2 sector should decompose into
# quasi-spin multiplets: S=2 has m_S = -2,...,2 giving 5 states at N=2 level,
# but the pair-number decomposition is different from the Sz decomposition.

# Actually with all energies degenerate, H_B2(rank-1) = 2*E*N - G*A^+*A^-
# where A^+ = sum_k u_k sigma_+^k. In the N=2 sector, only the
# state |A^+ applied twice to vacuum> (if it exists) gets shifted.
# Other N=2 states are orthogonal to the paired state and stay at 4*E.

# Let's verify: what does rank-1 H look like in N=2?
evals_N2_rank1 = np.sort(np.linalg.eigvalsh(
    evecs_B2[:, idx_N2_B2].T @ H_B2_rank1 @ evecs_B2[:, idx_N2_B2]))
# Wait, better: diag in the natural basis
# Build N=2 projector for B2
P_N2 = np.zeros((dim_B2, len(idx_N2_B2)))
for i, idx in enumerate(idx_N2_B2):
    P_N2[idx, i] = 1.0

# No, idx_N2_B2 are indices into the EIGENBASIS of H_B2, not the computational basis.
# Let me redo: find N=2 states in the computational basis.
N_B2_comp = np.zeros(dim_B2)
for state in range(dim_B2):
    n_occ = bin(state).count('1')
    N_B2_comp[state] = n_occ

# Wait, the pair number is the number of occupied modes. In our convention,
# state |0> = all unoccupied (vacuum), state |15> = all occupied (4 pairs).
# But the Pauli encoding: sigma_z |0> = +|0> (unoccupied), sigma_z |1> = -|1> (occupied)
# n_k = (1 - sigma_z)/2, so |0> has n=0, |1> has n=1.
# State index in binary: bit k=1 means mode k occupied.
# But the tensor product ordering: mode 0 is leftmost bit.

# Recompute: for state index s, the occupation of mode k is:
# bit at position k (from MSB) is (s >> (n_B2 - 1 - k)) & 1
N_B2_comp_correct = np.zeros(dim_B2)
for state in range(dim_B2):
    n_occ = 0
    for k in range(n_B2):
        bit = (state >> (n_B2 - 1 - k)) & 1
        n_occ += bit
    N_B2_comp_correct[state] = n_occ

# Verify: N_B2_op should give these values on computational basis states
for state in range(dim_B2):
    e_s = np.zeros(dim_B2)
    e_s[state] = 1.0
    n_val = e_s @ N_B2_op @ e_s
    assert abs(n_val - N_B2_comp_correct[state]) < 1e-10, \
        f"State {state}: computed {n_val}, expected {N_B2_comp_correct[state]}"

# N=2 computational basis states
comp_N2_idx = np.where(N_B2_comp_correct == 2)[0]
print(f"\nN=2 computational basis states: {comp_N2_idx}")
print(f"  (Binary: {[format(s, f'0{n_B2}b') for s in comp_N2_idx]})")

# Project H_B2 and H_B2_rank1 onto N=2 sector
P_N2_comp = np.zeros((dim_B2, len(comp_N2_idx)))
for i, idx in enumerate(comp_N2_idx):
    P_N2_comp[idx, i] = 1.0

H_B2_N2 = P_N2_comp.T @ H_B2_direct @ P_N2_comp
H_B2_N2_rank1 = P_N2_comp.T @ H_B2_rank1 @ P_N2_comp

evals_N2_direct = np.sort(np.linalg.eigvalsh(H_B2_N2))
evals_N2_rank1_direct = np.sort(np.linalg.eigvalsh(H_B2_N2_rank1))

print(f"\nN=2 eigenvalues (full V_B2): {evals_N2_direct}")
print(f"N=2 eigenvalues (rank-1 V):  {evals_N2_rank1_direct}")
print(f"Max |delta E| (rank-1 vs full): {np.max(np.abs(evals_N2_direct - evals_N2_rank1_direct)):.6e}")

# Count degeneracies in rank-1 case
diffs_r1 = np.diff(evals_N2_rank1_direct)
print(f"\nN=2 rank-1 spacings: {diffs_r1}")
n_degenerate_r1 = np.sum(np.abs(diffs_r1) < 1e-8)
print(f"Number of degenerate pairs (rank-1): {n_degenerate_r1}")
print(f"  Expected: 5 degenerate (only 1 state shifted by pairing) -> 4 degenerate + 1 shifted")

# ============================================================
# 10. CROSS-CHECK: Exact S^2_B2 conservation within B2-only Hamiltonian
# ============================================================
print("\n" + "=" * 70)
print("10. S^2_B2 Conservation within B2-Only Hamiltonian")
print("=" * 70)

# Build S^2 for the B2 quasi-spin (all 4 modes, equal weight)
Sp_B2_total = sum(SP_B2[k] for k in range(n_B2))
Sm_B2_total = sum(SM_B2[k] for k in range(n_B2))
Sz_B2_total = sum(0.5 * SZ_B2[k] for k in range(n_B2))
S2_B2_total = Sp_B2_total @ Sm_B2_total + Sz_B2_total @ Sz_B2_total - Sz_B2_total

# Check [S^2, H_B2]
comm_S2_HB2 = S2_B2_total @ H_B2_direct - H_B2_direct @ S2_B2_total
eta_S2_HB2 = np.linalg.norm(comm_S2_HB2, 'fro') / (np.linalg.norm(S2_B2_total, 'fro') * np.linalg.norm(H_B2_direct, 'fro'))
print(f"\n||[S^2_B2, H_B2(full V)]||_F / norms = {eta_S2_HB2:.6e}")

# Check [S^2, H_B2_rank1]
comm_S2_HB2r1 = S2_B2_total @ H_B2_rank1 - H_B2_rank1 @ S2_B2_total
eta_S2_HB2r1 = np.linalg.norm(comm_S2_HB2r1, 'fro') / (np.linalg.norm(S2_B2_total, 'fro') * np.linalg.norm(H_B2_rank1, 'fro'))
print(f"||[S^2_B2, H_B2(rank-1)]||_F / norms = {eta_S2_HB2r1:.6e}")

# S^2 expectation values in H_B2 eigenstates
S2_B2_in_HB2 = np.diag(evecs_B2.T @ S2_B2_total @ evecs_B2)
print(f"\nS^2_B2 in H_B2 eigenstates:")
for i in range(dim_B2):
    n_pair_i = round(N_B2_exp_B2[i])
    s_val = (-1 + np.sqrt(1 + 4*S2_B2_in_HB2[i])) / 2 if S2_B2_in_HB2[i] >= -0.01 else -1
    print(f"  |{i:2d}> (N={n_pair_i}): S^2 = {S2_B2_in_HB2[i]:.6f}, s ~ {s_val:.3f}, E = {evals_B2[i]:.6f}")

# Check if S^2 is a good quantum number
S2_deviation = np.abs(S2_B2_in_HB2 - np.round(S2_B2_in_HB2 * 4) / 4)
print(f"\nMax |S^2 - s(s+1)| = {np.max(S2_deviation):.6e}")
if np.max(S2_deviation) < 0.01:
    print("S^2_B2 IS a good quantum number within B2-only Hamiltonian")
    S2_is_conserved = True
else:
    print(f"S^2_B2 is NOT a good quantum number (max deviation {np.max(S2_deviation):.4f})")
    S2_is_conserved = False

# ============================================================
# 11. Within-S^2-sector level statistics (if S^2 is conserved)
# ============================================================
print("\n" + "=" * 70)
print("11. Level Statistics within S^2 Sectors")
print("=" * 70)

if S2_is_conserved:
    # Classify by (N, S) quantum numbers
    print("\nClassification by (N_pair, S^2):")
    S2_rounded = np.round(S2_B2_in_HB2 * 4) / 4  # Round to s(s+1) values
    unique_quantum = set()
    for i in range(dim_B2):
        n_pair_i = round(N_B2_exp_B2[i])
        s2_i = S2_rounded[i]
        unique_quantum.add((n_pair_i, s2_i))

    for (n_p, s2_v) in sorted(unique_quantum):
        mask = (np.abs(N_B2_exp_B2 - n_p) < 0.5) & (np.abs(S2_B2_in_HB2 - s2_v) < 0.1)
        idx = np.where(mask)[0]
        s_val = (-1 + np.sqrt(1 + 4*s2_v)) / 2 if s2_v >= -0.01 else -1
        sec_evals = np.sort(evals_B2[idx])
        print(f"  N={n_p}, S={s_val:.1f} (S^2={s2_v:.2f}): dim={len(idx)}, E={sec_evals}")
else:
    print("S^2 not conserved; sector analysis not applicable.")
    # Still do N-sector analysis
    print("\nN-sector only:")
    for n_p in range(n_B2 + 1):
        mask = np.abs(N_B2_exp_B2 - n_p) < 0.5
        idx = np.where(mask)[0]
        sec_evals = np.sort(evals_B2[idx])
        print(f"  N={n_p}: dim={len(idx)}, E={sec_evals}")

# ============================================================
# 12. Analytic check: 4 degenerate modes with rank-1 V
# ============================================================
print("\n" + "=" * 70)
print("12. Analytic Structure of B2 (4 Degenerate Modes)")
print("=" * 70)

# With 4 degenerate modes at energy epsilon and rank-1 interaction V = G*|u><u|,
# the Hamiltonian is: H = 2*eps*N - G*(sum_k u_k P_k^+)(sum_m u_m P_m^-)
#
# The "collective" pair operator A^+ = sum_k u_k P_k^+ creates the "paired" state.
# In the N-pair sector, the only state that feels the interaction is:
# |N, paired> = (A^+)^N |vac> / normalization
# All other N-pair states are orthogonal to A^+ and have energy 2*eps*N.
#
# This means: in each N-sector, there is AT MOST 1 non-trivially shifted level.
# All others are degenerate at 2*eps*N.
#
# With the full V_B2B2 (not rank-1), the degeneracy is broken.
# The DEGREE of breaking determines the level statistics.

# Quantify: energy spread within each N sector
print(f"\nEnergy spread within N sectors (measures degeneracy breaking):")
for n_p in range(n_B2 + 1):
    mask = np.abs(N_B2_exp_B2 - n_p) < 0.5
    idx = np.where(mask)[0]
    sec_evals = np.sort(evals_B2[idx])

    if len(sec_evals) > 1:
        spread = sec_evals[-1] - sec_evals[0]
        # Compare with rank-1 spread
        mask_r1 = mask  # Same states
        sec_evals_r1 = np.sort(np.linalg.eigvalsh(
            evecs_B2[:, idx].T @ H_B2_rank1 @ evecs_B2[:, idx]))
        spread_r1 = sec_evals_r1[-1] - sec_evals_r1[0]

        # Actually, diagonalize rank-1 in the N=n_p sector directly
        H_B2_rank1_Np = P_N2_comp.T @ H_B2_rank1 @ P_N2_comp if n_p == 2 else None

        print(f"  N={n_p}: full spread = {spread:.6f}, rank-1 spread = {spread_r1:.6f}, "
              f"excess = {spread - spread_r1:.6f}")
    else:
        print(f"  N={n_p}: single state, E = {sec_evals[0]:.6f}")

# ============================================================
# GATE VERDICT
# ============================================================
print("\n" + "=" * 70)
print("GATE VERDICT: B2-INTEG-40")
print("=" * 70)

# Collect decisive numbers
print(f"\n--- DECISIVE NUMBERS ---")
print(f"  1. B2-only <r> (N=2 sector, 6 states): {r_N2_mean:.4f}" if not np.isnan(r_N2_mean) else "  1. B2-only <r>: insufficient data")
print(f"  2. B2-only <r> (global weighted): {r_B2_global:.4f}")
print(f"  3. B2-only <r> (unsectored): {r_unsectored_mean:.4f}" if 'r_unsectored_mean' in dir() else "  3. N/A")
print(f"  4. B2 survival decay time: t_decay = {t_decay_B2:.4f} natural units" if t_decay_B2 < np.inf else f"  4. B2 survival: NO DECAY in [0, {t_max:.1f}] (min P = {np.min(P_B2_t):.4f})")
print(f"  5. Thouless g_T(B2, N=2) = {g_T_B2_N2:.6f}")
print(f"  6. ||V_B2_rem||/||V_B2|| = {np.linalg.norm(V_B2_rem, 'fro') / np.linalg.norm(V_B2B2, 'fro'):.4f}")
print(f"  7. S^2_B2 conserved within B2: {'YES' if S2_is_conserved else 'NO'} (max dev = {np.max(S2_deviation):.4e})")
print(f"  8. V(B2,B2) rank-1 fraction: {rank1_frac_B2:.4f}")
print(f"  9. FGR decay rate Gamma = {Gamma_FGR:.4f}, t_FGR = {t_decay_FGR:.4f}")
print(f" 10. Long-time average P_B2(inf) = {P_B2_inf:.4f}")

# Gate classification
# PASS: <r> < 0.42 AND t_decay > 6
# FAIL: <r> > 0.50 OR t_decay < 1
# INTERMEDIATE: between

# Use the best available <r>:
# The N=2 sector (6 states, 4 ratios) is the only sector with enough data.
# But 4 ratios is very few. Use it with caution.
r_decisive = r_N2_mean if not np.isnan(r_N2_mean) else r_B2_global

# For decay time: use the actual survival probability computation
t_decisive = t_decay_B2

print(f"\n  Decisive <r> = {r_decisive:.4f}")
print(f"  Decisive t_decay = {t_decisive:.4f}" if t_decisive < np.inf else f"  Decisive t_decay = INF (never decays below 1/e)")

if r_decisive < 0.42 and (t_decisive > 6 or t_decisive == np.inf):
    gate_verdict = "PASS"
    gate_detail = f"B2 INTEGRABLE: <r>={r_decisive:.4f} < 0.42, t_decay={t_decisive:.4f} > 6"
elif r_decisive > 0.50 or (t_decisive < 1 and t_decisive != np.inf):
    gate_verdict = "FAIL"
    if r_decisive > 0.50:
        gate_detail = f"B2 THERMALIZES: <r>={r_decisive:.4f} > 0.50"
    else:
        gate_detail = f"B2 THERMALIZES: t_decay={t_decisive:.4f} < 1"
else:
    gate_verdict = "INTERMEDIATE"
    gate_detail = f"<r>={r_decisive:.4f} in [0.42, 0.50], t_decay={t_decisive:.4f}"

print(f"\n{'='*70}")
print(f"GATE B2-INTEG-40: {gate_verdict}")
print(f"  {gate_detail}")
print(f"{'='*70}")

# ============================================================
# 13. PLOT
# ============================================================
print("\n" + "=" * 70)
print("13. Generating Plot")
print("=" * 70)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle(f'B2-INTEG-40: B2 Subsystem Integrability | Verdict: {gate_verdict}',
             fontsize=14, fontweight='bold')

# Panel (a): B2 level spectrum by N-sector
ax = axes[0, 0]
colors_N = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
for n_p in range(n_B2 + 1):
    mask = np.abs(N_B2_exp_B2 - n_p) < 0.5
    sec_evals = evals_B2[mask]
    for e in sec_evals:
        ax.plot([n_p - 0.3, n_p + 0.3], [e, e], color=colors_N[n_p], linewidth=2)
ax.set_xlabel('Pair number N')
ax.set_ylabel('Energy (M_KK)')
ax.set_title('(a) B2 Level Spectrum by N-sector')
ax.set_xticks(range(n_B2 + 1))

# Panel (b): Level spacing distribution (N=2 sector + Poisson/GOE references)
ax = axes[0, 1]
if len(spacings_N2) > 0:
    # Unfolded spacings
    mean_sp_N2 = np.mean(spacings_N2)
    s_unfolded_N2 = spacings_N2 / mean_sp_N2

    ax.bar(range(len(s_unfolded_N2)), s_unfolded_N2, color='steelblue', alpha=0.7,
           label=f'N=2 spacings (unfolded)')
    ax.axhline(y=1.0, color='gray', linestyle='--', alpha=0.5)

    # Mark the r-values
    if len(r_N2_vals) > 0:
        ax2 = ax.twinx()
        ax2.plot(range(len(r_N2_vals)), r_N2_vals, 'ro-', linewidth=2, markersize=8, label='r-ratios')
        ax2.axhline(y=0.386, color='green', linestyle=':', linewidth=1.5, label='Poisson (0.386)')
        ax2.axhline(y=0.536, color='red', linestyle=':', linewidth=1.5, label='GOE (0.536)')
        ax2.set_ylabel('Level ratio r')
        ax2.legend(loc='upper right', fontsize=8)
        ax2.set_ylim(0, 1)

ax.set_xlabel('Spacing index')
ax.set_ylabel('Unfolded spacing s')
r_display = f'{r_N2_mean:.3f}' if not np.isnan(r_N2_mean) else 'N/A'
ax.set_title(f'(b) N=2 Sector: <r> = {r_display}')
ax.legend(loc='upper left', fontsize=8)

# Panel (c): Survival probability P_B2(t)
ax = axes[1, 0]
ax.plot(t_arr, P_B2_t, 'b-', linewidth=2, label='$P_{B2}(t)$ (subspace survival)')
ax.plot(t_arr, F_return_t, 'r--', linewidth=1.5, alpha=0.7, label='$F(t)$ (return probability)')
ax.axhline(y=1.0/np.e, color='gray', linestyle=':', alpha=0.5, label='$1/e$')
ax.axhline(y=P_B2_inf, color='green', linestyle='--', alpha=0.5, label=f'$P_{{B2}}(\\infty)$ = {P_B2_inf:.3f}')
if t_decay_B2 < np.inf:
    ax.axvline(x=t_decay_B2, color='orange', linestyle='--', alpha=0.7,
               label=f'$t_{{decay}}$ = {t_decay_B2:.2f}')
ax.set_xlabel('Time (natural units)')
ax.set_ylabel('Probability')
ax.set_title('(c) B2 Subspace Survival Probability')
ax.legend(fontsize=8)
ax.set_xlim(0, t_max)
ax.set_ylim(0, 1.05)

# Panel (d): V_phys block structure heatmap
ax = axes[1, 1]
im = ax.imshow(np.abs(V_phys), cmap='YlOrRd', aspect='equal')
plt.colorbar(im, ax=ax, label='|V|')
# Draw sector boundaries
for x in [3.5, 4.5]:
    ax.axvline(x=x, color='white', linewidth=2)
    ax.axhline(y=x, color='white', linewidth=2)
ax.set_xticks(range(8))
ax.set_xticklabels([str(l) for l in labels], rotation=45, fontsize=7)
ax.set_yticks(range(8))
ax.set_yticklabels([str(l) for l in labels], fontsize=7)
ax.set_title('(d) V_phys Block Structure')

# Add text annotation for B2 block
ax.annotate('B2', xy=(1.5, 1.5), fontsize=14, color='white', fontweight='bold', ha='center', va='center')
ax.annotate('B1', xy=(4, 4), fontsize=10, color='white', fontweight='bold', ha='center', va='center')
ax.annotate('B3', xy=(6, 6), fontsize=10, color='white', fontweight='bold', ha='center', va='center')

plt.tight_layout()
plt.savefig('tier0-computation/s40_b2_integrability.png', dpi=150, bbox_inches='tight')
print("Plot saved: tier0-computation/s40_b2_integrability.png")

# ============================================================
# 14. SAVE DATA
# ============================================================
print("\n" + "=" * 70)
print("14. Saving Data")
print("=" * 70)

save_dict = dict(
    # Gate
    gate_verdict=np.array([gate_verdict]),
    gate_detail=np.array([gate_detail]),

    # B2 eigenspectrum
    evals_B2=evals_B2,
    evecs_B2=evecs_B2,
    H_B2=H_B2_direct,

    # Level statistics
    r_B2_N2=np.array(r_N2_mean if not np.isnan(r_N2_mean) else -1.0),
    r_B2_global=np.array(r_B2_global),
    r_B2_unsectored=np.array(r_unsectored_mean if 'r_unsectored_mean' in dir() else -1.0),

    # Decay
    t_decay_B2=np.array(t_decay_B2 if t_decay_B2 < np.inf else -1.0),
    P_B2_t=P_B2_t,
    F_return_t=F_return_t,
    t_arr=t_arr,
    P_B2_inf=np.array(P_B2_inf),

    # Thouless
    g_T_B2_N2=np.array(g_T_B2_N2),
    g_T_B2_all=np.array(g_T_B2_all),
    V_rms_B2=np.array(V_rms_B2),
    mean_spacing_B2_N2=np.array(mean_spacing_B2_N2),

    # V decomposition
    V_B2B2=V_B2B2,
    V_B2_rank1=V_B2_rank1,
    V_B2_rem=V_B2_rem,
    rank1_frac_B2=np.array(rank1_frac_B2),
    svd_B2=S_B2,

    # S^2 conservation
    S2_is_conserved=np.array(S2_is_conserved),
    S2_max_deviation=np.array(np.max(S2_deviation)),
    S2_B2_in_eigenstates=S2_B2_in_HB2,
    eta_S2_HB2=np.array(eta_S2_HB2),

    # Coupling
    V_B2_B1=V_B2_B1,
    V_B2_B3=V_B2_B3,
    Gamma_FGR=np.array(Gamma_FGR),
    t_decay_FGR=np.array(t_decay_FGR),

    # Cross-check
    delta_H_projection=np.array(delta_H),

    # Full BCS for reference
    evals_BCS=evals_full,
    N_pair_in_eigenstates=N_B2_exp_B2,
)

np.savez('tier0-computation/s40_b2_integrability.npz', **save_dict)
print("Data saved: tier0-computation/s40_b2_integrability.npz")

t_end = time.time()
print(f"\nTotal runtime: {t_end - t_start:.1f}s")
print("\n" + "=" * 70)
print("COMPUTATION COMPLETE")
print("=" * 70)
