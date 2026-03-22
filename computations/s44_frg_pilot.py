#!/usr/bin/env python3
"""
s44_frg_pilot.py — FRG Pilot for 3-Sector BCS System (FRG-PILOT-44)

Tests whether the FRG effective action deviates from the heat kernel expansion
for the 8 gap-edge modes of the B1/B2/B3 BCS system.

Physics context:
  The system is 0-dimensional (L/xi_GL = 0.031 from S38). In 0D, the FRG is
  equivalent to exact integration of the partition function. The "Wilsonian"
  procedure is shell-by-shell integration over energy levels, which in the
  nuclear physics context is precisely the Strutinsky shell correction method.

  We implement THREE independent methods:
  1. EXACT: Full determinant ratio det(H_BdG)/det(H_normal) = exact partition fn
  2. HEAT KERNEL: Asymptotic expansion Tr f(D^2/Lambda^2) ~ a_0 + a_2/L^2 + ...
  3. WILSONIAN FRG: Shell-by-shell integration with Litim regulator, tracking
     the effective action as modes are integrated out from UV to IR.

  The FRG deviation measures how much the non-perturbative (full determinant)
  result differs from the heat kernel polynomial approximation.

Gate: FRG-PILOT-44
  PASS if >10% deviation (non-perturbative structure matters)
  FAIL if <1% deviation (heat kernel adequate)
  INFO if intermediate

Author: Nazarewicz Nuclear Structure Theorist
Session: 44, Wave 5
"""

import numpy as np
from scipy.linalg import eigvalsh, det, logm
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


# ============================================================
# 1. Load data
# ============================================================
d36 = np.load('tier0-computation/s36_mmax_authoritative.npz', allow_pickle=True)
d38 = np.load('tier0-computation/s38_cc_instanton.npz', allow_pickle=True)
d42 = np.load('tier0-computation/s42_hauser_feshbach.npz', allow_pickle=True)
d44s = np.load('tier0-computation/s44_strutinsky_diag.npz', allow_pickle=True)

# Gap-edge energies and multiplicities
E_B1 = float(d36['E_B1'])  # 0.8191
E_B2 = float(d36['E_B2'])  # 0.8453
E_B3 = float(d36['E_B3'])  # 0.9782
mult = d38['mult_k']       # [1, 4, 3]

eps = np.array([E_B1] * mult[0] + [E_B2] * mult[1] + [E_B3] * mult[2])
N = len(eps)  # 8
print(f"Gap-edge modes: N={N}")
print(f"  B1: {mult[0]}x E={E_B1:.4f}")
print(f"  B2: {mult[1]}x E={E_B2:.4f}")
print(f"  B3: {mult[2]}x E={E_B3:.4f}")

# BCS interaction matrix
Mmat = d36['Mmat_8x8'].copy()
Mmat = 0.5 * (Mmat + Mmat.T)  # Enforce symmetry

# BCS gap
Delta_0 = float(d38['Delta_0'])  # 0.770

# Full spectrum reference
S_fold = float(d44s['S_fold'])  # 250,361
strutinsky_shell_frac = float(d44s['frac_m2_at_plateau'])  # 0.019

# BCS dominant eigenvector for gap matrix
u_BCS = d36['dom_eigvec_8x8']
Delta_mat = Delta_0 * np.outer(u_BCS, u_BCS)

print(f"\nBCS: Delta_0 = {Delta_0:.4f}")
print(f"     u_BCS = {u_BCS}")
print(f"     S_fold = {S_fold:.2f}")
print(f"     Strutinsky shell frac = {strutinsky_shell_frac:.4f}")


# ============================================================
# 2. Build BdG Hamiltonian
# ============================================================
def build_BdG(eps_vals, V_mat, Delta_mat_in):
    """Build 2N x 2N BdG Hamiltonian."""
    n = len(eps_vals)
    H = np.zeros((2*n, 2*n))
    H[:n, :n] = np.diag(eps_vals) + V_mat
    H[n:, n:] = -(np.diag(eps_vals) + V_mat)
    H[:n, n:] = Delta_mat_in
    H[n:, :n] = Delta_mat_in.conj()
    return H

H_BdG = build_BdG(eps, Mmat, Delta_mat)
H_normal = build_BdG(eps, Mmat, np.zeros_like(Delta_mat))

evals_BdG = np.sort(eigvalsh(H_BdG))
evals_normal = np.sort(eigvalsh(H_normal))

print(f"\nBdG eigenvalues: {evals_BdG}")
print(f"Normal eigenvalues: {evals_normal}")
print(f"BdG spectral gap (min |E|): {np.min(np.abs(evals_BdG)):.6f}")
print(f"Normal spectral gap (min |E|): {np.min(np.abs(evals_normal)):.6f}")


# ============================================================
# 3. METHOD 1: EXACT partition function ratio (0D benchmark)
# ============================================================
# In 0D, the "spectral action" for the BdG system is:
#   S_BdG = (1/2) Tr ln |H_BdG^2| = sum_i ln |E_i|
# (the log-determinant, which is the 1-loop exact result in 0D)
#
# For a FREE system (no interactions, no pairing):
#   S_free = sum_i ln |eps_i| (particle) + sum_i ln |eps_i| (hole) = 2 * sum_i ln |eps_i|
#
# The spectral action Tr f(D^2/Lambda^2) for function f and cutoff Lambda:
#   S_f(Lambda) = sum_i f(E_i^2 / Lambda^2)

print("\n" + "="*60)
print("METHOD 1: EXACT (log-determinant)")
print("="*60)

# Log-determinant of |H|
S_exact_BdG = 0.5 * np.sum(np.log(np.abs(evals_BdG[evals_BdG != 0])**2))
S_exact_normal = 0.5 * np.sum(np.log(np.abs(evals_normal[evals_normal != 0])**2))
S_exact_free = np.sum(np.log(eps))  # Free = diagonal, no interactions, no pairing

print(f"  S_exact(BdG)    = {S_exact_BdG:.6f}")
print(f"  S_exact(normal) = {S_exact_normal:.6f}")
print(f"  S_exact(free)   = {S_exact_free:.6f}")
print(f"  S_exact(BdG) - S_exact(normal) = {S_exact_BdG - S_exact_normal:.6f}")
print(f"  S_exact(normal) - S_exact(free) = {S_exact_normal - S_exact_free:.6f}")

# Spectral action with various cutoff functions
def S_spectral(evals_sq, Lambda, cutoff='connes'):
    """Spectral action Tr f(D^2/Lambda^2) for given eigenvalues-squared."""
    x = evals_sq / Lambda**2
    if cutoff == 'connes':
        f = np.where(x < 1, (1 - x)**2, 0.0)
    elif cutoff == 'sharp':
        f = np.where(x < 1, 1.0, 0.0)
    elif cutoff == 'gaussian':
        f = np.exp(-x)
    elif cutoff == 'heat':
        f = np.exp(-x)  # Same as Gaussian for heat kernel
    else:
        raise ValueError(f"Unknown cutoff: {cutoff}")
    return np.sum(f)


# ============================================================
# 4. METHOD 2: HEAT KERNEL expansion
# ============================================================
print("\n" + "="*60)
print("METHOD 2: HEAT KERNEL EXPANSION")
print("="*60)

# For the 8-mode system, the heat kernel coefficients of D^2 = diag(eps_i^2)
# (free case, no interactions):
a0_free = float(N)  # = 8
a2_free = np.sum(eps**2)  # = Tr(D^2)
a4_free = 0.5 * np.sum(eps**4)  # = (1/2) Tr(D^4)
a6_free = (1.0/6.0) * np.sum(eps**6)

# For the interacting (normal) system, D_eff^2 has eigenvalues = evals_normal^2
evals_normal_sq = evals_normal**2
a0_normal = float(2*N)  # BdG doubles modes
a2_normal = np.sum(evals_normal_sq)
a4_normal = 0.5 * np.sum(evals_normal_sq**2)
a6_normal = (1.0/6.0) * np.sum(evals_normal_sq**3)

# For the paired (BdG) system:
evals_BdG_sq = evals_BdG**2
a0_BdG = float(2*N)
a2_BdG = np.sum(evals_BdG_sq)
a4_BdG = 0.5 * np.sum(evals_BdG_sq**2)
a6_BdG = (1.0/6.0) * np.sum(evals_BdG_sq**3)

print(f"  Free:   a0={a0_free}, a2={a2_free:.6f}, a4={a4_free:.6f}")
print(f"  Normal: a0={a0_normal}, a2={a2_normal:.6f}, a4={a4_normal:.6f}")
print(f"  BdG:    a0={a0_BdG}, a2={a2_BdG:.6f}, a4={a4_BdG:.6f}")

# Heat kernel vs exact spectral action comparison
# Use Connes cutoff f(x) = (1-x)^2 theta(1-x)
# HK expansion: Tr f(D^2/L^2) ~ a0*f_0 - a2*f_2/L^2 + a4*f_4/L^4 - ...
# For f(x) = (1-x)^2: f_0 = int_0^1 f(x)dx = 1/3
# But actually for discrete spectrum, the HK is the Taylor expansion:
# Tr f(D^2/L^2) = sum_i f(eps_i^2/L^2)
#               = sum_i [1 - 2*eps_i^2/L^2 + eps_i^4/L^4] (for Connes)
#               = N - 2*Tr(D^2)/L^2 + Tr(D^4)/L^4 (for L >> eps_max)

Lambda_vals = np.logspace(np.log10(1.0), np.log10(10.0), 100)

# Exact spectral action
S_exact_L_BdG = np.array([S_spectral(evals_BdG_sq, L) for L in Lambda_vals])
S_exact_L_normal = np.array([S_spectral(evals_normal_sq, L) for L in Lambda_vals])

# 3-term heat kernel expansion (Connes cutoff)
# f(x) = (1-x)^2 = 1 - 2x + x^2  for x < 1
# Tr f = N - 2*sum(eps^2)/L^2 + sum(eps^4)/L^4  for all eps^2/L^2 < 1
def S_HK_3term(a0, a2, a4, L):
    return a0 - 2*a2/L**2 + a4/L**4

# 4-term
def S_HK_4term(a0, a2, a4, a6, L):
    return a0 - 2*a2/L**2 + a4/L**4 - (2.0/3.0)*a6/L**6

S_HK3_BdG = np.array([S_HK_3term(a0_BdG, a2_BdG, a4_BdG, L) for L in Lambda_vals])
S_HK3_normal = np.array([S_HK_3term(a0_normal, a2_normal, a4_normal, L) for L in Lambda_vals])
S_HK4_BdG = np.array([S_HK_4term(a0_BdG, a2_BdG, a4_BdG, a6_BdG, L) for L in Lambda_vals])

# Relative error of HK expansion vs exact
err_HK3_BdG = np.abs(S_HK3_BdG - S_exact_L_BdG) / np.maximum(np.abs(S_exact_L_BdG), 1e-20)
err_HK3_normal = np.abs(S_HK3_normal - S_exact_L_normal) / np.maximum(np.abs(S_exact_L_normal), 1e-20)
err_HK4_BdG = np.abs(S_HK4_BdG - S_exact_L_BdG) / np.maximum(np.abs(S_exact_L_BdG), 1e-20)


# ============================================================
# 5. METHOD 3: WILSONIAN FRG (shell-by-shell integration)
# ============================================================
print("\n" + "="*60)
print("METHOD 3: WILSONIAN FRG (Litim regulator)")
print("="*60)

# In the Wilsonian picture for a DISCRETE spectrum, the FRG amounts to:
# Start at k = Lambda (all modes regulated), progressively unfreeze modes
# as k decreases past their energies.
#
# Gamma_k = sum_{|E_i| > k} contribution_i(integrated out)
#         + sum_{|E_i| < k} regulated contribution (active)
#
# With Litim regulator R_k = (k^2 - E_i^2) theta(k^2 - E_i^2):
# The regularized propagator is 1/(k^2 + Sigma_i) for active modes
# and 1/(E_i^2 + Sigma_i) for frozen modes.
#
# The key FRG contribution beyond heat kernel:
# The heat kernel treats each mode independently (one-body).
# The FRG includes how integrating out high-energy modes MODIFIES
# the effective action for the remaining low-energy modes (many-body).
#
# For the BCS interaction, this is the SCREENING of the pairing
# interaction as high-energy modes are integrated out.

def wilsonian_frg(evals_sq, V_interaction, Lambda_max, N_k=10000):
    """
    Wilsonian FRG for discrete spectrum with interactions.

    At each k, modes with E_i^2 > k^2 are "integrated out" and contribute
    to the effective action. Modes with E_i^2 < k^2 are regularized.

    The interaction V modifies the effective action for remaining modes
    through screening/antiscreening (RPA-type corrections).

    Returns: Gamma_0 (full effective action at k=0), trajectory
    """
    n = len(evals_sq)
    dk = Lambda_max / N_k
    k_grid = np.linspace(Lambda_max, 0.0, N_k + 1)

    # Track flowing quantities
    Omega_k = 0.0  # Vacuum energy
    Omega_traj = [0.0]
    Sigma_k = np.zeros(n)  # Self-energy corrections

    # Sort eigenvalues for shell-by-shell integration
    sort_idx = np.argsort(evals_sq)[::-1]  # Largest first
    evals_sorted = evals_sq[sort_idx]
    V_sorted = V_interaction[np.ix_(sort_idx, sort_idx)] if V_interaction is not None else None

    for step in range(N_k):
        k = k_grid[step]
        k_next = k_grid[step + 1]
        k_mid = 0.5 * (k + k_next)
        if k_mid <= 0:
            Omega_traj.append(Omega_k)
            continue

        # Identify which modes are being integrated out in this step
        # (modes with k_next^2 < E_i^2 < k^2)
        active = (evals_sorted < k_mid**2)  # Modes still regulated
        frozen = ~active  # Modes already integrated out

        # Litim regulator contribution:
        # dGamma/dk = (1/2) sum_{active} 2k / (k^2 + Sigma_i)
        dOmega = 0.0
        for i in range(n):
            if active[i]:
                # Propagator with regulator
                G_i = 1.0 / (k_mid**2 + Sigma_k[i])
                # Regulator derivative
                dR_i = 2.0 * k_mid
                dOmega += 0.5 * G_i * dR_i

        # Self-energy flow from interaction (RPA-type screening)
        if V_sorted is not None:
            for i in range(n):
                if active[i]:
                    dSigma = 0.0
                    for j in range(n):
                        if active[j]:
                            G_j = 1.0 / (k_mid**2 + Sigma_k[j])
                            dSigma += V_sorted[i, j] * G_j * 2.0 * k_mid * G_j
                    Sigma_k[i] += dSigma * dk

        Omega_k += dOmega * dk
        Omega_traj.append(Omega_k)

    return Omega_k, np.array(Omega_traj), k_grid


# Run FRG for BdG system (paired)
print("\nRunning Wilsonian FRG (paired)...")
# Use BdG eigenvalues-squared as the spectrum
# Interaction in BdG eigenbasis
V_BdG_full = np.zeros((2*N, 2*N))
V_BdG_full[:N, :N] = Mmat
V_BdG_full[N:, N:] = -Mmat
evecs_BdG = np.linalg.eigh(H_BdG)[1]
V_BdG_eigbasis = evecs_BdG.T @ V_BdG_full @ evecs_BdG

Omega_FRG_BdG, traj_BdG, k_grid = wilsonian_frg(
    evals_BdG_sq, V_BdG_eigbasis, Lambda_max=3.0, N_k=10000
)
print(f"  Omega_FRG(BdG) = {Omega_FRG_BdG:.6f}")

# Run FRG for normal system
print("Running Wilsonian FRG (normal)...")
evecs_normal = np.linalg.eigh(H_normal)[1]
V_norm_eigbasis = evecs_normal.T @ V_BdG_full @ evecs_normal

Omega_FRG_normal, traj_normal, _ = wilsonian_frg(
    evals_normal_sq, V_norm_eigbasis, Lambda_max=3.0, N_k=10000
)
print(f"  Omega_FRG(normal) = {Omega_FRG_normal:.6f}")

# Run FRG without interactions (pure spectral, no V)
print("Running Wilsonian FRG (no interaction)...")
Omega_FRG_free_BdG, traj_free_BdG, _ = wilsonian_frg(
    evals_BdG_sq, None, Lambda_max=3.0, N_k=10000
)
Omega_FRG_free_normal, traj_free_normal, _ = wilsonian_frg(
    evals_normal_sq, None, Lambda_max=3.0, N_k=10000
)
print(f"  Omega_FRG(free, BdG spectrum) = {Omega_FRG_free_BdG:.6f}")
print(f"  Omega_FRG(free, normal spectrum) = {Omega_FRG_free_normal:.6f}")


# ============================================================
# 6. COMPARISON: FRG vs Heat Kernel vs Exact
# ============================================================
print("\n" + "="*60)
print("COMPARISON: THREE METHODS")
print("="*60)

# At Lambda = 2.5 (well above all modes):
L_ref = 2.5

# Exact spectral action
S_exact_BdG_Lref = S_spectral(evals_BdG_sq, L_ref)
S_exact_normal_Lref = S_spectral(evals_normal_sq, L_ref)

# Heat kernel 3-term
S_HK3_BdG_Lref = S_HK_3term(a0_BdG, a2_BdG, a4_BdG, L_ref)
S_HK3_normal_Lref = S_HK_3term(a0_normal, a2_normal, a4_normal, L_ref)

print(f"\nAt Lambda = {L_ref}:")
print(f"  {'':20s} {'Exact':>12s} {'HK 3-term':>12s} {'HK error':>12s}")
print(f"  {'BdG (paired)':20s} {S_exact_BdG_Lref:12.6f} {S_HK3_BdG_Lref:12.6f} "
      f"{abs(S_HK3_BdG_Lref - S_exact_BdG_Lref)/S_exact_BdG_Lref*100:12.6f}%")
print(f"  {'Normal':20s} {S_exact_normal_Lref:12.6f} {S_HK3_normal_Lref:12.6f} "
      f"{abs(S_HK3_normal_Lref - S_exact_normal_Lref)/S_exact_normal_Lref*100:12.6f}%")

# The BCS-specific deviation = difference between paired and normal
delta_S_exact = S_exact_BdG_Lref - S_exact_normal_Lref
delta_S_HK3 = S_HK3_BdG_Lref - S_HK3_normal_Lref
print(f"\n  delta_S (BdG - normal):")
print(f"  {'Exact':20s} {delta_S_exact:12.6f}")
print(f"  {'HK 3-term':20s} {delta_S_HK3:12.6f}")

# The FRG adds interaction corrections on top of the spectral sum.
# The "FRG beyond heat kernel" = self-energy screening corrections from V.
delta_FRG_int = (Omega_FRG_BdG - Omega_FRG_free_BdG) - (Omega_FRG_normal - Omega_FRG_free_normal)
print(f"\n  FRG interaction corrections:")
print(f"    BdG: Omega(with V) - Omega(free) = {Omega_FRG_BdG - Omega_FRG_free_BdG:.6f}")
print(f"    Normal: Omega(with V) - Omega(free) = {Omega_FRG_normal - Omega_FRG_free_normal:.6f}")
print(f"    delta_FRG_int (BCS-specific) = {delta_FRG_int:.6f}")

# ============================================================
# 7. PROPER GATE METRIC: FRG deviation at 8-mode level
# ============================================================
# The question is: does the heat kernel expansion miss significant physics
# at the gap edge?
#
# For the 8 gap-edge modes, we compare:
# A. Exact spectral action S_f(Lambda) = sum_i f(E_i^2/Lambda^2) [EXACT]
# B. Heat kernel 3-term approximation [TRUNCATION]
# C. FRG = exact + interaction corrections [FULL]
#
# Deviation (A vs B): pure HK truncation error, no interactions
# Deviation (C vs A): interaction corrections beyond single-particle
# Deviation (C vs B): total non-HK effects

print("\n" + "="*60)
print("GATE METRIC COMPUTATION")
print("="*60)

# Scan over Lambda to find where HK breaks down
Lambda_gate = np.linspace(1.0, 5.0, 50)

dev_AB_BdG = []   # HK truncation error (BdG)
dev_AB_norm = []  # HK truncation error (normal)
dev_pairing = []  # BCS-specific effect on spectral action
dev_FRG_int = []  # FRG interaction corrections

for L in Lambda_gate:
    # A: Exact
    SA_BdG = S_spectral(evals_BdG_sq, L)
    SA_norm = S_spectral(evals_normal_sq, L)

    # B: HK 3-term
    SB_BdG = S_HK_3term(a0_BdG, a2_BdG, a4_BdG, L)
    SB_norm = S_HK_3term(a0_normal, a2_normal, a4_normal, L)

    # Truncation error
    dev_AB_BdG.append(abs(SB_BdG - SA_BdG) / max(abs(SA_BdG), 1e-20) * 100)
    dev_AB_norm.append(abs(SB_norm - SA_norm) / max(abs(SA_norm), 1e-20) * 100)

    # BCS-specific: how much does pairing change the spectral action?
    # This is |S(BdG) - S(normal)| / S(normal)
    if abs(SA_norm) > 1e-20:
        dev_pairing.append(abs(SA_BdG - SA_norm) / abs(SA_norm) * 100)
    else:
        dev_pairing.append(0)

dev_AB_BdG = np.array(dev_AB_BdG)
dev_AB_norm = np.array(dev_AB_norm)
dev_pairing = np.array(dev_pairing)

print(f"\nHK truncation error (BdG) at Lambda=2.5: {dev_AB_BdG[np.argmin(np.abs(Lambda_gate-2.5))]:.4f}%")
print(f"HK truncation error (norm) at Lambda=2.5: {dev_AB_norm[np.argmin(np.abs(Lambda_gate-2.5))]:.4f}%")
print(f"BCS-specific deviation at Lambda=2.5: {dev_pairing[np.argmin(np.abs(Lambda_gate-2.5))]:.4f}%")

# Find Lambda where HK breaks down (error > 1%)
idx_break_BdG = np.where(dev_AB_BdG > 1)[0]
idx_break_norm = np.where(dev_AB_norm > 1)[0]
L_break_BdG = Lambda_gate[idx_break_BdG[0]] if len(idx_break_BdG) > 0 else None
L_break_norm = Lambda_gate[idx_break_norm[0]] if len(idx_break_norm) > 0 else None
print(f"\nHK breakdown Lambda (BdG, >1%): {L_break_BdG}")
print(f"HK breakdown Lambda (norm, >1%): {L_break_norm}")


# ============================================================
# 8. NUCLEAR ANALOGY: Strutinsky smoothing = heat kernel
# ============================================================
# The Strutinsky energy theorem says:
#   E_total = E_smooth (LDM) + delta_shell
# where delta_shell = sum_i eps_i - integral eps g_smooth(eps) deps
#
# The spectral action Tr f(D^2/Lambda^2) IS E_smooth for appropriate f.
# The shell correction is what the heat kernel misses.
#
# From STRUTINSKY-DIAG-44: shell correction fraction = 1.89% (m2 plateau)
# This is for the FULL 992-mode spectrum.
#
# For the 8 gap-edge modes, the "shell correction" is:
# delta_shell_8 = sum_i f(eps_i^2/L^2) - sum_i [HK expansion at order n]
# This equals the HK truncation error.

print("\n" + "="*60)
print("NUCLEAR ANALOGY: Shell Correction at Gap Edge")
print("="*60)

# Shell correction for the 8 gap-edge modes at Lambda = 2.5
L_ref = 2.5
S_exact_8_BdG = S_spectral(evals_BdG_sq, L_ref)
S_HK3_8_BdG = S_HK_3term(a0_BdG, a2_BdG, a4_BdG, L_ref)
S_HK4_8_BdG = S_HK_4term(a0_BdG, a2_BdG, a4_BdG, a6_BdG, L_ref)

delta_shell_3 = S_exact_8_BdG - S_HK3_8_BdG
delta_shell_4 = S_exact_8_BdG - S_HK4_8_BdG

print(f"  S_exact(BdG, L=2.5) = {S_exact_8_BdG:.8f}")
print(f"  S_HK3(BdG, L=2.5)  = {S_HK3_8_BdG:.8f}")
print(f"  S_HK4(BdG, L=2.5)  = {S_HK4_8_BdG:.8f}")
print(f"  delta_shell (3-term) = {delta_shell_3:.8f} ({delta_shell_3/S_exact_8_BdG*100:.4f}%)")
print(f"  delta_shell (4-term) = {delta_shell_4:.8f} ({delta_shell_4/S_exact_8_BdG*100:.4f}%)")

# The key comparison: BCS effect vs shell correction vs effacement
print(f"\n  Scale hierarchy (absolute):")
print(f"    S_fold (full 992)     = {S_fold:.2f}")
print(f"    S_exact(8 modes, BdG) = {S_exact_8_BdG:.6f}")
print(f"    |delta_S(BCS)|        = {abs(delta_S_exact):.6f}")
print(f"    |delta_shell(3-term)| = {abs(delta_shell_3):.8f}")
print(f"    |delta_shell(4-term)| = {abs(delta_shell_4):.8f}")

# Effacement ratios
print(f"\n  Effacement (relative to S_fold):")
print(f"    8-mode / S_fold       = {S_exact_8_BdG / S_fold:.6e}")
print(f"    delta_BCS / S_fold    = {abs(delta_S_exact) / S_fold:.6e}")
print(f"    delta_shell / S_fold  = {abs(delta_shell_3) / S_fold:.6e}")


# ============================================================
# 9. THE KEY TEST: Does FRG reveal non-perturbative structure
#    that heat kernel CANNOT capture?
# ============================================================
print("\n" + "="*60)
print("KEY TEST: Non-perturbative content")
print("="*60)

# In a FINITE system with DISCRETE spectrum, the exact spectral action
# sum_i f(E_i^2/L^2) is NOT an expansion -- it is an exact finite sum.
# The heat kernel "expansion" is simply a Taylor approximation to this sum.
#
# The FRG in 0D is equivalent to the exact result (no truncation error
# from the flow itself, only from the LPA truncation).
#
# So: "FRG beyond heat kernel" = (exact sum) - (Taylor expansion)
#                               = shell correction (Strutinsky)
#
# Plus: interaction corrections from V (screening/antiscreening)
#       These are GENUINELY beyond the spectral action.

# Test 1: Shell correction (exact vs HK expansion)
# At Lambda = 2.5 (well in plateau region):
shell_frac_8 = abs(delta_shell_3) / abs(S_exact_8_BdG) * 100
print(f"\n  Test 1: Shell correction (8 modes)")
print(f"    |delta_shell| / S_exact = {shell_frac_8:.6f}%")
print(f"    Strutinsky (992 modes)  = {strutinsky_shell_frac*100:.4f}%")

# Test 2: BCS modification of spectrum
# How much does BCS pairing change Tr f(D^2/L^2)?
bcs_frac_8 = abs(delta_S_exact) / abs(S_exact_normal_Lref) * 100
print(f"\n  Test 2: BCS spectral modification")
print(f"    |S(BdG) - S(normal)| / S(normal) = {bcs_frac_8:.6f}%")

# Test 3: Interaction vertex screening (FRG-specific)
# This is the difference between FRG with V and FRG without V
vert_BdG = abs(Omega_FRG_BdG - Omega_FRG_free_BdG)
vert_norm = abs(Omega_FRG_normal - Omega_FRG_free_normal)
vert_frac_BdG = vert_BdG / max(abs(Omega_FRG_free_BdG), 1e-20) * 100
vert_frac_norm = vert_norm / max(abs(Omega_FRG_free_normal), 1e-20) * 100
print(f"\n  Test 3: Interaction vertex corrections")
print(f"    |Omega(V) - Omega(0)| / Omega(0) (BdG)    = {vert_frac_BdG:.4f}%")
print(f"    |Omega(V) - Omega(0)| / Omega(0) (normal) = {vert_frac_norm:.4f}%")

# Test 4: Combined non-perturbative metric
# = max of (shell correction, BCS modification, vertex screening)
# evaluated relative to the 8-mode spectral action
combined_metric = max(shell_frac_8, bcs_frac_8, vert_frac_BdG)
print(f"\n  Combined metric (max of Tests 1-3): {combined_metric:.6f}%")


# ============================================================
# 10. ADDITIONAL: Exact 0D partition function comparison
# ============================================================
print("\n" + "="*60)
print("EXACT 0D PARTITION FUNCTION")
print("="*60)

# In 0D, the exact effective action is:
# Gamma_exact = -ln Z = -(1/2) ln det(H^2) = -sum_i ln|E_i|
# (up to an irrelevant constant)
#
# This is EXACTLY the spectral action with f(x) = -ln(x)/2 (log cutoff).
# The heat kernel expansion of -ln(det) is the asymptotic series.
#
# For the Connes cutoff, the spectral action is a DIFFERENT functional
# than the partition function. They agree only at leading order.

# Exact partition function difference (BdG vs normal)
ln_Z_BdG = -S_exact_BdG  # = -(1/2) sum ln(E_i^2)
ln_Z_normal = -S_exact_normal
delta_ln_Z = ln_Z_BdG - ln_Z_normal

print(f"  ln Z(BdG)    = {ln_Z_BdG:.6f}")
print(f"  ln Z(normal) = {ln_Z_normal:.6f}")
print(f"  delta(ln Z)  = {delta_ln_Z:.6f}")
print(f"  This is the BCS condensation free energy in 0D:")
print(f"  F_cond = -T * delta(ln Z) = {-delta_ln_Z:.6f} (at T=1)")

# Heat kernel expansion of ln det(H^2):
# ln det(H^2) = Tr ln(H^2) = sum_i ln(E_i^2)
# HK expansion: Tr ln(D^2/L^2) ~ a_0 ln(L^2) - a_2/L^2 - a_4/(2L^4) - ...
# (the zeta function regularized version)
# For FINITE spectrum, this IS the exact sum -- no HK expansion needed.

# The spectral action Tr f(D^2/L^2) with various f:
# 1. f(x) = (1-x)^2: Connes cutoff. Polynomial, HK = Taylor = exact for L >> E_max
# 2. f(x) = e^{-x}: Gaussian/heat kernel. HK IS the heat kernel. Exact for any L
# 3. f(x) = -ln(x)/2: Log (partition function). NOT a cutoff function (diverges)
#    Must be regulated: f_reg(x) = -ln(x + mu^2/L^2)/2

# The POINT: for a FINITE discrete spectrum, the spectral action is a finite sum.
# The heat kernel expansion is its Taylor series in 1/Lambda^2.
# The "FRG deviation" = terms beyond the Taylor truncation = shell correction.
# There is NO mysterious non-perturbative physics: the exact answer is just
# the sum, and the HK is its polynomial approximation.

# But INTERACTIONS (V) introduce genuine non-perturbative effects:
# They change the spectrum (BdG vs normal), and they contribute
# screening/antiscreening corrections that are NOT captured by
# Tr f(D^2_free/Lambda^2).

# Definitive comparison:
# Does Tr f(D^2_BdG/L^2) differ from Tr f(D^2_free/L^2) + perturbative corrections?
# The perturbative corrections from V are: delta_S ~ Tr(V * dS/dD^2)
# = sum_i V_ii * f'(E_i^2/L^2) * 2*E_i / L^2

# First-order perturbative correction to spectral action from BCS pairing:
# Delta modifies D -> D_BdG, so D^2 -> D^2 + Delta^2 (schematically)
# Perturbative: Tr f((D^2 + Delta^2)/L^2) ~ Tr f(D^2/L^2) + Tr[Delta^2 * f'(D^2/L^2)/L^2]

evals_normal_pos = np.abs(evals_normal)
evals_BdG_pos = np.abs(evals_BdG)

# Perturbative estimate of pairing effect:
# delta_S_pert = sum_i [f(E_BdG_i^2/L^2) - f(E_normal_i^2/L^2)]
#             ~ sum_i f'(E_normal_i^2/L^2) * (E_BdG_i^2 - E_normal_i^2) / L^2
L_test = 2.5
x_norm = evals_normal_sq / L_test**2
x_BdG = evals_BdG_sq / L_test**2
# For Connes: f'(x) = -2(1-x) for x < 1, 0 for x > 1
f_prime = np.where(x_norm < 1, -2*(1 - x_norm), 0.0)
delta_x = x_BdG - x_norm
S_pert_correction = np.sum(f_prime * delta_x)
S_exact_correction = S_exact_BdG_Lref - S_exact_normal_Lref

print(f"\n  Perturbative BCS correction to S_f:")
print(f"    delta_S (exact)       = {S_exact_correction:.8f}")
print(f"    delta_S (1st order)   = {S_pert_correction:.8f}")
print(f"    Ratio (pert/exact)    = {S_pert_correction/S_exact_correction:.6f}")
pert_error = abs(S_pert_correction - S_exact_correction) / abs(S_exact_correction) * 100
print(f"    Perturbative error    = {pert_error:.4f}%")
print(f"    (This measures how non-perturbative the BCS effect is on the spectral action)")


# ============================================================
# 11. FULL GATE ASSESSMENT
# ============================================================
print("\n" + "="*60)
print("FULL GATE ASSESSMENT: FRG-PILOT-44")
print("="*60)

# Metrics summary:
print(f"\n  METRIC 1: HK truncation error (shell correction)")
print(f"    8 modes at L=2.5:  {shell_frac_8:.6f}%")
print(f"    992 modes (Strutinsky m2): {strutinsky_shell_frac*100:.4f}%")

print(f"\n  METRIC 2: BCS spectral modification")
print(f"    |S(BdG) - S(normal)| / S(normal): {bcs_frac_8:.6f}%")
print(f"    Perturbative error: {pert_error:.4f}%")

print(f"\n  METRIC 3: FRG vertex corrections")
print(f"    Paired (BdG): {vert_frac_BdG:.4f}%")
print(f"    Normal: {vert_frac_norm:.4f}%")

print(f"\n  METRIC 4: Effacement ratios (vs S_fold = {S_fold:.0f})")
print(f"    8-mode S_exact / S_fold = {S_exact_8_BdG/S_fold:.2e}")
print(f"    BCS modification / S_fold = {abs(S_exact_correction)/S_fold:.2e}")
print(f"    Shell correction / S_fold = {abs(delta_shell_3)/S_fold:.2e}")

# The PRIMARY gate metric: maximum deviation of FRG (= exact non-perturbative)
# from heat kernel (= polynomial approximation) for the 8 gap-edge modes.
#
# This is Test 1 (shell correction) at the reference Lambda.
# Test 2 (BCS modification) measures something different: the effect of
# pairing on the spectrum itself, which changes BOTH the exact and HK values.
# Test 3 (vertex screening) is beyond the spectral action entirely.
#
# The FRG "sees" beyond the heat kernel in two ways:
# 1. Exact sum vs Taylor truncation (= shell correction, metric 1)
# 2. Interaction-induced modifications (= vertex corrections, metric 3)
#
# For the gate, we use the maximum of these:

gate_metric = max(shell_frac_8, bcs_frac_8)
gate_metric_with_vert = max(gate_metric, vert_frac_BdG)

# Also: at what Lambda does the HK break down by >10%?
idx_10pct = np.where(dev_AB_BdG > 10)[0]
L_10pct = Lambda_gate[idx_10pct[0]] if len(idx_10pct) > 0 else None

print(f"\n  GATE METRIC (8-mode level): {gate_metric:.6f}%")
print(f"  GATE METRIC (with vertex): {gate_metric_with_vert:.6f}%")
if L_10pct:
    print(f"  HK breaks down (>10%) at Lambda = {L_10pct:.2f}")
else:
    print(f"  HK never exceeds 10% error for Lambda in [{Lambda_gate[0]:.1f}, {Lambda_gate[-1]:.1f}]")

# VERDICT
if gate_metric > 10:
    verdict = "PASS"
    verdict_detail = f"FRG deviation {gate_metric:.2f}% > 10% (non-perturbative structure at gap edge)"
elif gate_metric < 1:
    verdict = "FAIL"
    verdict_detail = f"FRG deviation {gate_metric:.4f}% < 1% (heat kernel adequate)"
else:
    verdict = "INFO"
    verdict_detail = f"FRG deviation {gate_metric:.4f}% in [1%, 10%] range"

print(f"\n  VERDICT: {verdict}")
print(f"  DETAIL: {verdict_detail}")
print(f"  NOTE: Even where FRG reveals deviations from HK at the 8-mode level,")
print(f"        effacement (8-mode/S_fold ~ {S_exact_8_BdG/S_fold:.2e}) renders")
print(f"        these corrections invisible in the full spectral action.")


# ============================================================
# 12. Save all results
# ============================================================
np.savez('tier0-computation/s44_frg_pilot.npz',
    # Input
    eps_modes=eps,
    mult=mult,
    N_modes=N,
    Delta_0=Delta_0,
    Mmat_8x8=Mmat,
    u_BCS=u_BCS,
    # Spectra
    evals_BdG=evals_BdG,
    evals_normal=evals_normal,
    evals_BdG_sq=evals_BdG_sq,
    evals_normal_sq=evals_normal_sq,
    # Exact results
    S_exact_BdG=S_exact_BdG,
    S_exact_normal=S_exact_normal,
    S_exact_free=S_exact_free,
    delta_S_exact=delta_S_exact,
    # Heat kernel coefficients
    a0_BdG=a0_BdG, a2_BdG=a2_BdG, a4_BdG=a4_BdG, a6_BdG=a6_BdG,
    a0_normal=a0_normal, a2_normal=a2_normal, a4_normal=a4_normal,
    # Shell correction
    delta_shell_3=delta_shell_3,
    delta_shell_4=delta_shell_4,
    shell_frac_8=shell_frac_8,
    # BCS modification
    bcs_frac_8=bcs_frac_8,
    pert_error=pert_error,
    S_pert_correction=S_pert_correction,
    S_exact_correction=S_exact_correction,
    # FRG results
    Omega_FRG_BdG=Omega_FRG_BdG,
    Omega_FRG_normal=Omega_FRG_normal,
    Omega_FRG_free_BdG=Omega_FRG_free_BdG,
    Omega_FRG_free_normal=Omega_FRG_free_normal,
    vert_frac_BdG=vert_frac_BdG,
    vert_frac_norm=vert_frac_norm,
    # Lambda scan
    Lambda_gate=Lambda_gate,
    dev_AB_BdG=dev_AB_BdG,
    dev_AB_norm=dev_AB_norm,
    dev_pairing=dev_pairing,
    # Full scan
    Lambda_vals=Lambda_vals,
    S_exact_L_BdG=S_exact_L_BdG,
    S_exact_L_normal=S_exact_L_normal,
    S_HK3_BdG=S_HK3_BdG[:len(Lambda_vals)],
    S_HK3_normal=S_HK3_normal[:len(Lambda_vals)],
    err_HK3_BdG=err_HK3_BdG,
    err_HK3_normal=err_HK3_normal,
    # FRG flow trajectories
    traj_BdG=traj_BdG,
    traj_normal=traj_normal,
    traj_free_BdG=traj_free_BdG,
    traj_free_normal=traj_free_normal,
    k_grid=k_grid,
    # Reference
    S_fold=S_fold,
    strutinsky_shell_frac=strutinsky_shell_frac,
    # Effacement
    eff_8mode_over_Sfold=S_exact_8_BdG/S_fold,
    eff_BCS_over_Sfold=abs(S_exact_correction)/S_fold,
    eff_shell_over_Sfold=abs(delta_shell_3)/S_fold,
    # Gate
    gate_metric=gate_metric,
    gate_metric_with_vert=gate_metric_with_vert,
    gate_verdict=verdict,
    gate_detail=verdict_detail,
    L_break_BdG=L_break_BdG if L_break_BdG is not None else 0.0,
    L_break_norm=L_break_norm if L_break_norm is not None else 0.0,
)
print(f"\nData saved to tier0-computation/s44_frg_pilot.npz")


# ============================================================
# 13. Plots
# ============================================================
fig, axes = plt.subplots(2, 3, figsize=(18, 10))

# (a) BdG vs Normal spectrum
ax = axes[0, 0]
ax.plot(range(2*N), evals_BdG, 'bo', ms=7, label='BdG (paired)')
ax.plot(range(2*N), evals_normal, 'r^', ms=6, label='Normal', alpha=0.7)
ax.axhline(0, color='k', lw=0.5)
ax.set_xlabel('Mode index')
ax.set_ylabel('Energy (M_KK)')
ax.set_title('BdG vs Normal Spectrum (8 gap-edge modes)')
ax.legend(fontsize=9)

# (b) HK truncation error vs Lambda
ax = axes[0, 1]
ax.semilogy(Lambda_gate, dev_AB_BdG, 'b-', lw=2, label='BdG HK3 error')
ax.semilogy(Lambda_gate, dev_AB_norm, 'r--', lw=2, label='Normal HK3 error')
ax.semilogy(Lambda_gate, dev_pairing, 'g:', lw=2, label='BCS modification')
ax.axhline(10, color='k', ls='--', alpha=0.3, label='PASS (10%)')
ax.axhline(1, color='orange', ls='--', alpha=0.3, label='FAIL (1%)')
ax.set_xlabel(r'$\Lambda$ (M_KK)')
ax.set_ylabel('Deviation (%)')
ax.set_title('HK Expansion Error vs Cutoff')
ax.legend(fontsize=8)
ax.set_ylim(1e-8, 100)

# (c) Spectral action: exact vs HK
ax = axes[0, 2]
ax.plot(Lambda_vals, S_exact_L_BdG, 'b-', lw=2, label='Exact (BdG)')
ax.plot(Lambda_vals, S_exact_L_normal, 'r-', lw=2, label='Exact (Normal)')
ax.plot(Lambda_vals, S_HK3_BdG[:len(Lambda_vals)], 'b--', lw=1, alpha=0.5, label='HK3 (BdG)')
ax.plot(Lambda_vals, S_HK3_normal[:len(Lambda_vals)], 'r--', lw=1, alpha=0.5, label='HK3 (Normal)')
ax.set_xlabel(r'$\Lambda$ (M_KK)')
ax.set_ylabel(r'$\mathrm{Tr}\, f(D^2/\Lambda^2)$')
ax.set_title('Spectral Action: Exact vs HK')
ax.legend(fontsize=8)

# (d) FRG flow trajectories
ax = axes[1, 0]
k_plot = k_grid
n_pts = min(len(k_plot), len(traj_BdG)-1)
ax.plot(k_plot[:n_pts], traj_BdG[1:n_pts+1], 'b-', lw=1.5, label='BdG + V')
ax.plot(k_plot[:n_pts], traj_normal[1:n_pts+1], 'r-', lw=1.5, label='Normal + V')
ax.plot(k_plot[:n_pts], traj_free_BdG[1:n_pts+1], 'b--', lw=1, alpha=0.5, label='BdG free')
ax.plot(k_plot[:n_pts], traj_free_normal[1:n_pts+1], 'r--', lw=1, alpha=0.5, label='Normal free')
for e in [E_B1, E_B2, E_B3]:
    ax.axvline(e, color='gray', ls=':', alpha=0.3)
ax.set_xlabel('RG scale k')
ax.set_ylabel(r'$\Omega(k)$')
ax.set_title('FRG Vacuum Energy Flow')
ax.legend(fontsize=8)

# (e) Scale hierarchy
ax = axes[1, 1]
labels = ['S_fold\n(992)', 'S_exact\n(8 BdG)', '|delta_BCS|', '|delta_shell|']
vals = [S_fold, S_exact_8_BdG, abs(S_exact_correction), abs(delta_shell_3)]
colors = ['steelblue', 'coral', 'seagreen', 'gold']
log_vals = [np.log10(max(v, 1e-20)) for v in vals]
bars = ax.bar(range(len(labels)), log_vals, color=colors)
ax.set_xticks(range(len(labels)))
ax.set_xticklabels(labels, fontsize=9)
ax.set_ylabel(r'$\log_{10}$(magnitude)')
ax.set_title('Scale Hierarchy')
for bar, v in zip(bars, vals):
    ax.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.1,
            f'{v:.2e}', ha='center', va='bottom', fontsize=7)

# (f) Gate verdict summary
ax = axes[1, 2]
metrics = ['HK trunc\n(shell)', 'BCS mod\n(spectrum)', 'Vertex\n(FRG)', 'Pert err\n(non-pert)']
metric_vals = [shell_frac_8, bcs_frac_8, vert_frac_BdG, pert_error]
colors_m = ['blue', 'green', 'red', 'purple']
bars2 = ax.bar(range(len(metrics)), metric_vals, color=colors_m, alpha=0.7)
ax.axhline(10, color='k', ls='--', alpha=0.3)
ax.axhline(1, color='orange', ls='--', alpha=0.3)
ax.set_xticks(range(len(metrics)))
ax.set_xticklabels(metrics, fontsize=8)
ax.set_ylabel('Deviation (%)')
ax.set_title(f'FRG-PILOT-44: {verdict}')
ax.set_yscale('symlog', linthresh=0.001)
for bar, d in zip(bars2, metric_vals):
    y_pos = max(bar.get_height(), 0.0001)
    ax.text(bar.get_x() + bar.get_width()/2., y_pos * 1.5 if y_pos > 0.01 else y_pos + 0.01,
            f'{d:.4f}%', ha='center', va='bottom', fontsize=7)

plt.suptitle(f'FRG-PILOT-44: Functional RG for 8 Gap-Edge BCS Modes\n'
             f'Gate: {verdict} | Metric = {gate_metric:.4f}% | '
             f'Effacement = {S_exact_8_BdG/S_fold:.2e}',
             fontsize=12, fontweight='bold')
plt.tight_layout()
plt.savefig('tier0-computation/s44_frg_pilot.png', dpi=150, bbox_inches='tight')
print("Plot saved to tier0-computation/s44_frg_pilot.png")

print("\n=== DONE ===")
