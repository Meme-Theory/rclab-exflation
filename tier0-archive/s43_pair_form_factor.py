#!/usr/bin/env python3
"""
Session 43: PAIR-FF-43 — Pair Transfer Form Factor at Finite Momentum
=====================================================================

Computes the pair transfer form factor F(q) for the BCS condensate on SU(3),
where q is the momentum transfer in KK representation space.

Physical question: Are the Cooper pairs spatially extended (BCS regime,
relevant for fabric domain walls) or localized (BEC regime, relevant for
tessellation)?

Method:
  1. Reconstruct BdG amplitudes u_k, v_k from the mean-field BCS gap equation
     using the stored V_8x8 interaction matrix and single-particle energies.
  2. Also extract pair amplitudes kappa_k = <b_k> from the exact diagonalization
     (ED) ground state pair correlation matrix (number-conserving).
  3. Compute the pair transfer form factor:
       F(q) = Sum_k u_k * v_k * exp(i * q . r_k)
     where r_k is the "position" of mode k in representation space, defined
     by the Casimir eigenvalue C_2(k) of the SU(3) representation.
  4. Also compute the pair density in representation space:
       rho_pair(r) = Sum_k |kappa_k|^2 * delta(r - r_k)
  5. Classify BCS vs BEC via xi_pair * q_F where xi_pair is the pair
     coherence length (0.808 M_KK^{-1} from S37) and q_F is the Fermi
     momentum in representation space.

Nuclear physics context:
  - In nuclear BCS, the pair transfer form factor F(q) = Sum_k u_k v_k j_0(q*r_k)
    determines two-nucleon transfer cross sections (e.g., (p,t), (t,p) reactions).
  - F(q) ~ 1/q at large q for spatially extended BCS pairs.
  - F(q) ~ constant (flat) for BEC-like tightly bound pairs.
  - The crossover criterion is k_F * xi_pair: >>1 is BCS, <<1 is BEC.
  - Reference: Paper 03 (Bogoliubov), Paper 08 (pairing collapse).

On SU(3), "position" and "momentum" in the internal space are both discrete
(representation labels). The Casimir C_2(p,q) = (p^2 + q^2 + pq + 3p + 3q)/3
serves as the analog of |r|^2 / (2m). The mode index k maps to a specific
(p,q) representation and spin component.

Author: Nazarewicz Nuclear Structure Theorist, Session 43
Date: 2026-03-14
Gate: PAIR-FF-43 (INFO)
"""

import os
import sys
import time
import numpy as np
from numpy.linalg import eigh, eigvalsh
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
t0 = time.time()

print("=" * 78)
print("Session 43: PAIR-FF-43 — Pair Transfer Form Factor at Finite Momentum")
print("=" * 78)

# ======================================================================
#  Step 1: Load stored data
# ======================================================================

pair_data = np.load(os.path.join(SCRIPT_DIR, 's37_pair_susceptibility.npz'),
                    allow_pickle=True)
inst_data = np.load(os.path.join(SCRIPT_DIR, 's37_instanton_action.npz'),
                    allow_pickle=True)
ed36_data = np.load(os.path.join(SCRIPT_DIR, 's36_multisector_ed.npz'),
                    allow_pickle=True)

V_8x8 = pair_data['V_8x8']
E_8 = pair_data['E_8']
rho = pair_data['rho']
mu = float(pair_data['mu'])  # = 0
n_modes = int(pair_data['n_modes'])  # = 8
branch_labels = list(pair_data['branch_labels'])

# BCS parameters from S37
xi_BCS = float(inst_data['xi_BCS'])         # 0.808 M_KK^{-1}
Delta_8_gap = inst_data['Delta_8_gap']        # gap for each of 8 modes
E_cond = float(pair_data['E_cond'])           # -0.137

# Pair correlation matrix from ED (number-conserving ground state)
pair_corr = ed36_data['config_4_pair_corr']   # 8x8 <b_i^dag b_j>
pair_occ = ed36_data['config_4_pair_occ']     # diagonal: <n_k>

# Gap estimates from pair susceptibility
Delta_pair = float(pair_data['Delta_pair'])   # 0.464
Delta_OES = float(pair_data['Delta_OES'])     # 0.464

print(f"\nLoaded data:")
print(f"  n_modes = {n_modes}")
print(f"  E_8 = {E_8}")
print(f"  rho = {rho}")
print(f"  mu = {mu}")
print(f"  xi_BCS = {xi_BCS:.6f} M_KK^{{-1}}")
print(f"  Delta_pair = {Delta_pair:.6f}")
print(f"  E_cond = {E_cond:.10f}")
print(f"  branch_labels = {branch_labels}")

# ======================================================================
#  Step 2: Define representation-space coordinates for each mode
# ======================================================================

print(f"\n{'='*78}")
print("REPRESENTATION-SPACE COORDINATES")
print(f"{'='*78}")

# The 8 modes come from the Dirac operator D_K on SU(3) at the fold
# (tau ~ 0.19). They belong to specific SU(3) irreducible representations
# characterized by Dynkin labels (p,q).
#
# From the spectrum structure:
# - B1 (1 mode): (0,0) sector, singlet eigenvalue. This is the adjoint
#   representation contribution at lowest Casimir. E_B1 = 0.819.
# - B2 (4 modes): (0,0) sector, 4-fold degenerate near fold.
#   E_B2 = 0.845. These are the modes that form the van Hove peak.
# - B3 (3 modes): (1,0) sector (fundamental or anti-fundamental).
#   E_B3 = 0.978.
#
# The SU(3) Casimir eigenvalue C_2(p,q) = (p^2+q^2+pq+3p+3q)/3:
#   (0,0): C_2 = 0       (trivial representation, dim=1)
#   (1,0): C_2 = 4/3     (fundamental, dim=3)
#   (0,1): C_2 = 4/3     (anti-fundamental, dim=3)
#   (1,1): C_2 = 3       (adjoint, dim=8)
#   (2,0): C_2 = 10/3    (symmetric tensor, dim=6)
#   (0,2): C_2 = 10/3    (anti-symmetric tensor, dim=6)
#   (3,0): C_2 = 6       (dim=10)
#
# NOTE: The D_K eigenvalue branches do NOT directly correspond to single
# representations. The branch labels B1, B2, B3 label eigenvalue TRACKS
# as functions of tau. At the fold, each track has contributions from
# multiple representations (Peter-Weyl mixing). However, each mode k
# has a DOMINANT representation determined by its Casimir proximity.
#
# For the form factor, the relevant "distance" between modes is the
# Casimir difference, which measures separation in representation space.
# This is the group-theoretic analog of |r_i - r_j|.

# Assignment of effective Casimir labels:
# B2[0-3]: fold eigenvalues at 0.845, near the (0,0) sector.
#   These are the 4 modes from the (0,0) sector of the spinor bundle.
#   The spinor bundle on SU(3) has dim=8 (Dirac spinor on 8-dim manifold).
#   Within (0,0), the 4 modes correspond to different spinor components
#   with the SAME Casimir C_2 = 0. But they are distinguished by their
#   K_7 quantum number (generator 7 of Gell-Mann matrices).
#
# B1: singlet at 0.819. Also (0,0) sector but different spinor branch.
#   C_2 = 0 but distinguished from B2 by the spinor structure.
#
# B3[0-2]: from (1,0) sector. C_2 = 4/3.
#   3 modes = dim of fundamental representation.

# Effective "position" in representation space:
# Use the Casimir eigenvalue as the radial coordinate in rep space.
# The angular structure is encoded in the K_7 quantum number and
# the specific weight within the representation.

# Casimir values for each mode
C2_mode = np.zeros(n_modes)
# B2[0-3]: (0,0) sector
C2_mode[0] = 0.0  # B2[0]
C2_mode[1] = 0.0  # B2[1]
C2_mode[2] = 0.0  # B2[2]
C2_mode[3] = 0.0  # B2[3]
# B1: (0,0) sector
C2_mode[4] = 0.0  # B1
# B3[0-2]: (1,0) sector
C2_mode[5] = 4.0/3.0  # B3[0]
C2_mode[6] = 4.0/3.0  # B3[1]
C2_mode[7] = 4.0/3.0  # B3[2]

# K_7 quantum numbers (from [iK_7, D_K] = 0: each mode has definite q_7)
# From S34: B2 has 4 weights with different q_7 values
# The (0,0) representation weights under K_7:
# For the adjoint (1,1): weights are {-1, -1/2, 0, 0, 1/2, 1/2, 1, -1/2}
# For the BCS pairing with K_7 charge, we need the specific q_7 values.
# From S35: Cooper pairs carry K_7 charge +/- 1/2.
# The B2 modes have q_7 values: let's use the spinor-component labels.

# For the form factor, what matters is the DISTANCE between modes in
# representation space. Within the (0,0) sector, modes are distinguished
# only by spinor indices, not by representation labels. Their "distance"
# in SU(3) representation space is ZERO — they all sit at C_2 = 0.
# The B3 modes sit at C_2 = 4/3, giving a finite distance.

# Define an effective distance using the SU(3) metric on the weight lattice.
# The natural distance between representations (p1,q1) and (p2,q2) is:
#   d^2 = |Lambda_1 - Lambda_2|^2
# where Lambda = p*omega_1 + q*omega_2 are the highest weights in the
# root-space inner product.
# For SU(3): <omega_i, omega_j> = (A^{-1})_{ij} where A is the Cartan matrix.
#   A = [[2,-1],[-1,2]], A^{-1} = (1/3)[[2,1],[1,2]]
#   <omega_1,omega_1> = 2/3, <omega_1,omega_2> = 1/3, <omega_2,omega_2> = 2/3

# Distance from (0,0) to (1,0):
#   d^2 = <omega_1, omega_1> = 2/3
#   d = sqrt(2/3) = 0.8165 (in units of the root length)

# Distance from (0,0) to (0,1):
#   d = sqrt(2/3) = 0.8165

# Effective positions in root space (2D)
# (0,0) -> origin (0,0)
# (1,0) -> omega_1 = (1,0) in Dynkin coordinates
# (0,1) -> omega_2 = (0,1) in Dynkin coordinates

# In Cartesian coordinates using the root-space metric:
# omega_1 = (sqrt(2/3), 0) [conventional choice]
# omega_2 = (1/(2*sqrt(6)), 1/(2*sqrt(2))) ... let me use standard coords.
#
# Standard Cartesian embedding of SU(3) roots:
# Simple roots: alpha_1 = (1, 0), alpha_2 = (-1/2, sqrt(3)/2)
# Fundamental weights: omega_1 = (1/2, 1/(2*sqrt(3))), omega_2 = (0, 1/sqrt(3))
# (using the normalization |alpha|^2 = 1 for long roots)

# Fundamental weights in Cartesian:
omega_1 = np.array([0.5, 1.0/(2*np.sqrt(3))])  # = (0.5, 0.2887)
omega_2 = np.array([0.0, 1.0/np.sqrt(3)])       # = (0, 0.5774)

print(f"  Fundamental weights (Cartesian):")
print(f"    omega_1 = {omega_1}")
print(f"    omega_2 = {omega_2}")
print(f"    |omega_1|^2 = {np.dot(omega_1, omega_1):.6f} (should be 2/3 = {2/3:.6f})")
print(f"    |omega_2|^2 = {np.dot(omega_2, omega_2):.6f} (should be 2/3 = {2/3:.6f})")
print(f"    omega_1.omega_2 = {np.dot(omega_1, omega_2):.6f} (should be 1/3 = {1/3:.6f})")

# Position of each mode in the weight lattice
# (0,0) representation -> origin
# (1,0) representation -> Lambda = omega_1
# Within each representation, individual modes correspond to different
# WEIGHTS (not just the highest weight). But for the form factor, the
# relevant position is the representation label, not the specific weight.

r_mode = np.zeros((n_modes, 2))
# B2[0-3] and B1: (0,0) sector -> origin
r_mode[0] = np.array([0.0, 0.0])
r_mode[1] = np.array([0.0, 0.0])
r_mode[2] = np.array([0.0, 0.0])
r_mode[3] = np.array([0.0, 0.0])
r_mode[4] = np.array([0.0, 0.0])
# B3[0-2]: (1,0) sector -> omega_1
r_mode[5] = omega_1.copy()
r_mode[6] = omega_1.copy()
r_mode[7] = omega_1.copy()

print(f"\n  Mode positions in weight lattice:")
for k in range(n_modes):
    print(f"    {branch_labels[k]:6s}: r = ({r_mode[k,0]:.4f}, {r_mode[k,1]:.4f}), "
          f"|r| = {np.linalg.norm(r_mode[k]):.4f}, C_2 = {C2_mode[k]:.4f}")

# The inter-mode distance matrix
d_matrix = np.zeros((n_modes, n_modes))
for i in range(n_modes):
    for j in range(n_modes):
        d_matrix[i,j] = np.linalg.norm(r_mode[i] - r_mode[j])

print(f"\n  Inter-mode distance matrix (in root-length units):")
print(f"  Max distance: {np.max(d_matrix):.6f}")
print(f"  Distance B2-B3: {d_matrix[0,5]:.6f}")
print(f"  Distance B1-B3: {d_matrix[4,5]:.6f}")
print(f"  Distance B2-B1: {d_matrix[0,4]:.6f}")

# ======================================================================
#  Step 3: Reconstruct BdG amplitudes from mean-field BCS
# ======================================================================

print(f"\n{'='*78}")
print("BDG AMPLITUDES (MEAN-FIELD BCS)")
print(f"{'='*78}")

# The BCS gap equation: Delta_k = -Sum_m V_{km} * sqrt(rho_k * rho_m) * Delta_m / (2*E_m)
# where E_m = sqrt(xi_m^2 + Delta_m^2) and xi_m = E_m - mu.
#
# This was solved in S37: Delta_8_gap gives the self-consistent gaps.
# The BdG amplitudes are:
#   u_k^2 = (1/2)(1 + xi_k / E_k)
#   v_k^2 = (1/2)(1 - xi_k / E_k)
#   u_k * v_k = Delta_k / (2 * E_k)

xi = E_8 - mu  # xi_k = E_k - mu

# Use Delta_8_gap from S37 instanton calculation
Delta_k = Delta_8_gap.copy()

# Quasiparticle energies
E_qp = np.sqrt(xi**2 + Delta_k**2)

# BdG amplitudes
u_k = np.sqrt(0.5 * (1 + xi / E_qp))
v_k = np.sqrt(0.5 * (1 - xi / E_qp))

# Cross-check: u_k * v_k = Delta_k / (2 * E_k)
uv_product = u_k * v_k
uv_check = Delta_k / (2 * E_qp)

print(f"\n  Mean-field BdG amplitudes:")
print(f"  {'mode':6s}  {'xi_k':>10s}  {'Delta_k':>10s}  {'E_qp':>10s}  "
      f"{'u_k':>8s}  {'v_k':>8s}  {'u_k*v_k':>10s}  {'check':>10s}")
for k in range(n_modes):
    print(f"  {branch_labels[k]:6s}  {xi[k]:10.6f}  {Delta_k[k]:10.6f}  "
          f"{E_qp[k]:10.6f}  {u_k[k]:8.6f}  {v_k[k]:8.6f}  "
          f"{uv_product[k]:10.6f}  {uv_check[k]:10.6f}")

print(f"\n  Max |u*v - Delta/(2E)| = {np.max(np.abs(uv_product - uv_check)):.2e}")
print(f"  Sum u_k^2 = {np.sum(u_k**2):.6f}")
print(f"  Sum v_k^2 = {np.sum(v_k**2):.6f}")
print(f"  Sum u_k*v_k = {np.sum(uv_product):.6f}")

# ======================================================================
#  Step 4: Also extract pair amplitudes from ED (number-conserving)
# ======================================================================

print(f"\n{'='*78}")
print("PAIR AMPLITUDES FROM EXACT DIAGONALIZATION")
print(f"{'='*78}")

# The pair correlation matrix <b_i^dag b_j> from ED gives a
# number-conserving analog of u_k * v_k.
# The anomalous density kappa_k = <b_k> is zero in ED (number conserving),
# but the pair occupation <n_k> = <b_k^dag b_k> and off-diagonal
# <b_i^dag b_j> give the pair structure.

# The pair transfer form factor from ED uses the pair occupation fractions
# as weights: F_ED(q) = Sum_k sqrt(<n_k>) * exp(i q . r_k)
# since sqrt(<n_k>) is the number-conserving analog of v_k.

print(f"\n  Pair occupations (ED):")
print(f"  {'mode':6s}  {'<n_k>':>10s}  {'sqrt(<n_k>)':>12s}  {'v_k (MF)':>10s}")
for k in range(n_modes):
    print(f"  {branch_labels[k]:6s}  {pair_occ[k]:10.6f}  {np.sqrt(pair_occ[k]):12.6f}  "
          f"{v_k[k]:10.6f}")

# Pair correlation eigendecomposition
print(f"\n  Pair correlation matrix eigenvalues:")
pair_evals, pair_evecs = eigh(pair_corr)
for i in range(n_modes):
    print(f"    lambda_{i} = {pair_evals[i]:12.8f}")

# The largest eigenvalue gives the "condensate fraction" in ED
condensate_fraction = pair_evals[-1] / np.sum(pair_occ)
print(f"\n  Condensate fraction = lambda_max / N_pair = {condensate_fraction:.6f}")
print(f"  (1.0 = pure BCS, 1/N_modes = fully fragmented)")

# The eigenvector of the largest eigenvalue is the "natural pair orbital"
# This is the ED analog of the BCS pair wavefunction
natural_pair = pair_evecs[:, -1]
print(f"\n  Natural pair orbital (eigenvector of largest eigenvalue):")
for k in range(n_modes):
    print(f"    {branch_labels[k]:6s}: {natural_pair[k]:10.6f}")

# ======================================================================
#  Step 5: Compute pair transfer form factor F(q)
# ======================================================================

print(f"\n{'='*78}")
print("PAIR TRANSFER FORM FACTOR F(q)")
print(f"{'='*78}")

# The pair transfer form factor is defined as:
#   F(q) = Sum_k w_k * exp(i q . r_k)
# where w_k are the pair weights and r_k are mode positions.
#
# For BCS mean field: w_k = u_k * v_k
# For ED: w_k = sqrt(<n_k>)  (or eigenvalue-weighted natural orbital)
#
# Since the positions are 2D (in root space), q is also 2D.
# We compute F as a function of |q| by averaging over q-directions.
#
# More precisely, for the direction-averaged form factor:
#   F_avg(|q|) = (1/2pi) integral_0^{2pi} |F(q, theta)|^2 d(theta)
# where q = |q| (cos theta, sin theta).
#
# For discrete mode positions, this evaluates to:
#   F_avg(|q|) = Sum_{k,k'} w_k w_{k'} J_0(|q| * |r_k - r_{k'}|)
# where J_0 is the Bessel function of the first kind, order 0.
# This is the pair structure factor, analogous to S(q) in scattering.
#
# In nuclear physics, the two-nucleon transfer form factor is:
#   F(q) = Sum_k u_k v_k j_0(q * r_k)
# where j_0 is the spherical Bessel function.
# Here we use the 2D analog (Bessel J_0) since the weight lattice is 2D.

from scipy.special import j0  # Bessel function J_0

# q grid in units of M_KK (or equivalently, inverse root-length units)
n_q = 500
q_max = 10.0  # in M_KK units
q_grid = np.linspace(0.0, q_max, n_q)

# --- Method 1: Mean-field BCS form factor ---
# F_BCS(q) = Sum_k (u_k * v_k) * exp(i q . r_k)
# Direction-averaged structure factor:
# S_BCS(q) = Sum_{k,k'} (u_k v_k)(u_{k'} v_{k'}) J_0(q |r_k - r_{k'}|)

S_BCS = np.zeros(n_q)
for iq, q in enumerate(q_grid):
    for k in range(n_modes):
        for kp in range(n_modes):
            d_kk = d_matrix[k, kp]
            S_BCS[iq] += uv_product[k] * uv_product[kp] * j0(q * d_kk)

# Normalize to S_BCS(0)
S_BCS_0 = S_BCS[0]
F_BCS_norm = S_BCS / max(S_BCS_0, 1e-30)

# --- Method 2: ED pair correlation form factor ---
# Use sqrt(<n_k>) as weights
w_ED = np.sqrt(pair_occ)

S_ED = np.zeros(n_q)
for iq, q in enumerate(q_grid):
    for k in range(n_modes):
        for kp in range(n_modes):
            d_kk = d_matrix[k, kp]
            S_ED[iq] += w_ED[k] * w_ED[kp] * j0(q * d_kk)

S_ED_0 = S_ED[0]
F_ED_norm = S_ED / max(S_ED_0, 1e-30)

# --- Method 3: Natural orbital form factor ---
# Use the eigenvector of the largest pair correlation eigenvalue
w_nat = np.abs(natural_pair)  # take absolute values for weights

S_nat = np.zeros(n_q)
for iq, q in enumerate(q_grid):
    for k in range(n_modes):
        for kp in range(n_modes):
            d_kk = d_matrix[k, kp]
            S_nat[iq] += w_nat[k] * w_nat[kp] * j0(q * d_kk)

S_nat_0 = S_nat[0]
F_nat_norm = S_nat / max(S_nat_0, 1e-30)

# --- Method 4: Full pair correlation matrix form factor ---
# Use the FULL off-diagonal correlations:
# S_full(q) = Sum_{k,k'} <b_k^dag b_{k'}> J_0(q |r_k - r_{k'}|)

S_full = np.zeros(n_q)
for iq, q in enumerate(q_grid):
    for k in range(n_modes):
        for kp in range(n_modes):
            d_kk = d_matrix[k, kp]
            S_full[iq] += pair_corr[k, kp] * j0(q * d_kk)

S_full_0 = S_full[0]
F_full_norm = S_full / max(S_full_0, 1e-30)

print(f"\n  Form factor values at key q points:")
print(f"  {'q':>8s}  {'F_BCS':>10s}  {'F_ED':>10s}  {'F_nat':>10s}  {'F_full':>10s}")
for q_val in [0.0, 0.5, 1.0, 2.0, 3.0, 5.0, 7.0, 10.0]:
    iq = np.argmin(np.abs(q_grid - q_val))
    print(f"  {q_grid[iq]:8.3f}  {F_BCS_norm[iq]:10.6f}  {F_ED_norm[iq]:10.6f}  "
          f"{F_nat_norm[iq]:10.6f}  {F_full_norm[iq]:10.6f}")

# ======================================================================
#  Step 6: Analyze the form factor structure
# ======================================================================

print(f"\n{'='*78}")
print("FORM FACTOR ANALYSIS")
print(f"{'='*78}")

# The key physics: with ONLY two distinct positions in representation space
# (r=0 for B2+B1, r=omega_1 for B3), the form factor has a very specific
# structure:
#
# S(q) = W_0^2 + 2*W_0*W_1*J_0(q*d) + W_1^2
# where W_0 = Sum_{k in (0,0)} w_k,  W_1 = Sum_{k in (1,0)} w_k,
# and d = |omega_1| = sqrt(1/3) (distance between the two sectors).

d_01 = np.linalg.norm(omega_1)
print(f"  Distance between (0,0) and (1,0) sectors: d = {d_01:.6f}")
print(f"    = sqrt(1/3) = {np.sqrt(1/3):.6f}")

# Decompose weights into (0,0) and (1,0) sectors
W_0_BCS = np.sum(uv_product[:5])   # B2[0-3] + B1
W_1_BCS = np.sum(uv_product[5:])   # B3[0-2]

W_0_ED = np.sum(w_ED[:5])
W_1_ED = np.sum(w_ED[5:])

print(f"\n  Sector-decomposed weights:")
print(f"    BCS: W_0 = {W_0_BCS:.6f}, W_1 = {W_1_BCS:.6f}, ratio W_1/W_0 = {W_1_BCS/W_0_BCS:.6f}")
print(f"    ED:  W_0 = {W_0_ED:.6f},  W_1 = {W_1_ED:.6f},  ratio W_1/W_0 = {W_1_ED/W_0_ED:.6f}")

# Verify the two-sector formula
# S(q) = W_0^2 + 2*W_0*W_1*J_0(q*d) + W_1^2
# At q=0: S(0) = (W_0 + W_1)^2
# At large q: S -> W_0^2 + W_1^2 (J_0 -> 0)
# Minimum: when J_0(q*d) = -1, impossible (J_0 min ~ -0.403)

S_BCS_analytic = np.zeros(n_q)
for iq, q in enumerate(q_grid):
    S_BCS_analytic[iq] = W_0_BCS**2 + 2*W_0_BCS*W_1_BCS*j0(q*d_01) + W_1_BCS**2

# But this ignores WITHIN-sector structure. Since all modes in a sector
# have the same position (r=0 or r=omega_1), the within-sector form factor
# is flat: F(q) = const within each sector. The only q-dependence comes
# from the INTER-sector interference.

# Verify: analytic vs numerical
max_diff = np.max(np.abs(S_BCS - S_BCS_analytic))
print(f"\n  Analytic vs numerical S_BCS: max diff = {max_diff:.2e}")

# Asymptotic behavior
S_BCS_q0 = (W_0_BCS + W_1_BCS)**2
S_BCS_qinf = W_0_BCS**2 + W_1_BCS**2

print(f"\n  Asymptotic values:")
print(f"    S_BCS(0) = {S_BCS_q0:.6f}  (computed: {S_BCS[0]:.6f})")
print(f"    S_BCS(inf) = {S_BCS_qinf:.6f}")
print(f"    Asymptotic ratio S(inf)/S(0) = {S_BCS_qinf/S_BCS_q0:.6f}")

# The form factor oscillates around S(inf)/S(0)
# The oscillation amplitude is controlled by:
oscillation_amplitude = 2 * W_0_BCS * W_1_BCS / S_BCS_q0
print(f"    Oscillation amplitude (2*W_0*W_1/S(0)) = {oscillation_amplitude:.6f}")

# First zero of J_0: q*d = 2.4048
q_first_zero = 2.4048 / d_01
print(f"    First zero of J_0 at q = {q_first_zero:.4f} M_KK")

# First minimum of J_0: q*d = 3.8317
q_first_min = 3.8317 / d_01
J0_min = j0(3.8317)
print(f"    First minimum of J_0 at q = {q_first_min:.4f} M_KK (J_0 = {J0_min:.4f})")

# ======================================================================
#  Step 7: BCS vs BEC classification
# ======================================================================

print(f"\n{'='*78}")
print("BCS vs BEC CLASSIFICATION")
print(f"{'='*78}")

# The standard BCS-BEC crossover criterion:
#   k_F * xi_pair >> 1: BCS regime (extended pairs, pair size >> inter-particle spacing)
#   k_F * xi_pair << 1: BEC regime (compact pairs, pair size << inter-particle spacing)
#   k_F * xi_pair ~ 1: crossover
#
# In the nuclear context:
#   - Nuclear BCS: xi ~ 10-30 fm, inter-nucleon spacing ~ 2 fm => BCS
#   - Deuteron: xi ~ 2 fm => BEC-like (tightly bound)
#   - Neutron matter at low density: BCS-BEC crossover
#
# For this system on SU(3):
#   - xi_BCS = 0.808 M_KK^{-1} (from S37 instanton action)
#   - "Fermi momentum" in rep space: q_F ~ 1/a where a is the lattice spacing
#     in the weight lattice. For SU(3), a = |alpha| = 1 (root length).
#   - So k_F ~ 1 M_KK (one inverse root length).
#   - Product: k_F * xi = 0.808
#
# However, xi_BCS was computed from xi = v_F / (pi * Delta), which uses
# the Fermi velocity. This gives the coherence length in the tau-direction,
# not in representation space.
#
# For the coherence length in representation space, we need:
#   xi_rep = 1 / Delta_q
# where Delta_q is the pair momentum spread.
# From the form factor, the pair size is:
#   R_pair^2 = -d^2 ln F(q) / dq^2 |_{q=0}

# Second derivative of S(q) at q=0:
# S(q) = W_0^2 + 2*W_0*W_1*J_0(q*d) + W_1^2
# dS/dq = 2*W_0*W_1 * d * J_0'(q*d)
# d^2S/dq^2 = 2*W_0*W_1 * d^2 * J_0''(q*d)
# At q=0: J_0(0) = 1, J_0'(0) = 0, J_0''(0) = -1/2
# So d^2S/dq^2|_0 = 2*W_0*W_1 * d^2 * (-1/2) = -W_0*W_1*d^2

d2S_dq2_0 = -W_0_BCS * W_1_BCS * d_01**2

# Mean-square pair radius in rep space:
# <r^2> = -d^2 ln F / dq^2 |_{q=0} = -(d^2S/dq^2) / S(0)
r2_pair = -d2S_dq2_0 / S_BCS_q0
r_rms = np.sqrt(r2_pair)

print(f"\n  Pair coherence length estimates:")
print(f"    xi_BCS (tau-direction, S37) = {xi_BCS:.6f} M_KK^{{-1}}")
print(f"    d^2S/dq^2|_0 = {d2S_dq2_0:.6f}")
print(f"    <r^2>_pair = {r2_pair:.6f} (root-length)^2")
print(f"    R_rms (pair size in rep space) = {r_rms:.6f} root-lengths")
print(f"    = {r_rms * 1.0:.6f} M_KK^{{-1}} (using root length = 1/M_KK)")

# BCS-BEC crossover parameter
# The "inter-particle spacing" in rep space: there are 8 modes in a space
# of size ~ d_01 = 0.577. So the effective spacing is:
n_total_modes = 8
V_rep = d_01  # 1D effective volume in rep space (for the two-sector system)
a_rep = V_rep / (n_total_modes - 1)  # Mean spacing
q_F_rep = np.pi / a_rep  # Fermi momentum in rep space

print(f"\n  Inter-particle spacing in rep space: a = {a_rep:.6f}")
print(f"  Fermi momentum (rep space): q_F = {q_F_rep:.4f}")

# BCS-BEC criterion: xi_pair / a
crossover_ratio = r_rms / a_rep
print(f"\n  BCS-BEC crossover ratio R_pair / a_rep = {crossover_ratio:.4f}")

# Alternative: use the WITHIN-SECTOR structure
# Since all modes in (0,0) have r=0 and all modes in (1,0) have r=omega_1,
# the pair has only TWO spatial "bins". This is fundamentally a two-site
# problem, not a continuous-space BCS.
print(f"\n  IMPORTANT: The internal space has only TWO distinct positions")
print(f"    5 modes at r=0 (B2[0-3] + B1)")
print(f"    3 modes at r=omega_1 (B3[0-2])")
print(f"    Pair lives on a TWO-SITE system in representation space.")

# Fraction of pair weight at each site:
f_site0_BCS = W_0_BCS**2 / S_BCS_q0
f_site1_BCS = W_1_BCS**2 / S_BCS_q0
f_cross_BCS = 2 * W_0_BCS * W_1_BCS / S_BCS_q0

f_site0_ED = np.sum(pair_corr[:5,:5]) / S_full_0
f_site1_ED = np.sum(pair_corr[5:,5:]) / S_full_0
f_cross_ED = 2 * np.sum(pair_corr[:5,5:]) / S_full_0

print(f"\n  Pair weight decomposition:")
print(f"  {'':20s}  {'BCS MF':>10s}  {'ED':>10s}")
print(f"  {'Site 0 (0,0)':20s}  {f_site0_BCS:10.6f}  {f_site0_ED:10.6f}")
print(f"  {'Site 1 (1,0)':20s}  {f_site1_BCS:10.6f}  {f_site1_ED:10.6f}")
print(f"  {'Cross-site':20s}  {f_cross_BCS:10.6f}  {f_cross_ED:10.6f}")
print(f"  {'Total':20s}  {f_site0_BCS+f_site1_BCS+f_cross_BCS:10.6f}  "
      f"{f_site0_ED+f_site1_ED+f_cross_ED:10.6f}")

# ======================================================================
#  Step 8: The pair transfer form factor in the GGE
# ======================================================================

print(f"\n{'='*78}")
print("GGE PAIR TRANSFER FORM FACTOR")
print(f"{'='*78}")

# Post-transit, the system is in a GGE (Generalized Gibbs Ensemble) with
# 59.8 quasiparticle pairs (from S38). The GGE conserves 8 Richardson-Gaudin
# integrals. The pair correlation in the GGE is different from the ground state.
#
# In the GGE: <b_k^dag b_k> = n_k^{GGE} (occupation numbers set by the
# 8 conserved integrals, NOT thermal).
#
# From S38 sudden quench analysis:
#   P_exc = 1.000 (complete depletion of condensate)
#   E_exc = 443 * |E_cond| (massive excitation energy)
#   n_qp = 59.8 quasiparticle pairs
#
# In the quenched state, the pair correlations are determined by the
# Bogoliubov transformation at the NEW (post-quench) Hamiltonian.
# Since Delta -> 0 post-quench (no condensate), we have:
#   u_k -> 1, v_k -> 0 for epsilon_k > mu
#   u_k -> 0, v_k -> 1 for epsilon_k < mu
#
# But mu = 0 and all epsilon_k > 0 in this system. So:
#   u_k -> 1, v_k -> 0 for all k (post-quench)
#   => F_GGE(q) -> 0 (no pair correlations in GGE!)
#
# This is the correct result: the condensate is completely destroyed by
# the transit (P_exc = 1.000). The GGE has NO long-range pair order.
# Quasiparticle pairs are uncorrelated.
#
# However, there are SHORT-RANGE pair correlations surviving in the GGE,
# from the diagonal pair occupations. These give a form factor:

# For the GGE, the pair occupation is set by the quench dynamics.
# The post-quench occupation of the k-th pair level is:
#   n_k^{GGE} = |<psi_quenched | b_k^dag b_k | psi_quenched>|
# With complete excitation, n_k -> 1/2 (maximum entropy subject to
# conserved integrals).
# But actually: the quench maps the BCS ground state |BCS> of the
# pre-quench Hamiltonian to excited states of the post-quench Hamiltonian.
# The occupation in the quasiparticle basis is:
#   <f_k^dag f_k> = sin^2(theta_k)
# where theta_k is the rotation angle between pre- and post-quench
# Bogoliubov bases.

# Since post-quench Delta = 0: u_k^{post} = 1, v_k^{post} = 0
# Pre-quench: u_k^{pre}, v_k^{pre} as computed above
# The overlap: sin^2(theta_k) = (v_k^{pre})^2

n_GGE = v_k**2  # Post-quench quasiparticle occupation

print(f"  Post-quench quasiparticle occupations (sin^2 theta_k):")
for k in range(n_modes):
    print(f"    {branch_labels[k]:6s}: n_GGE = {n_GGE[k]:.6f} "
          f"(v_k^2 = {v_k[k]**2:.6f})")

n_total_qp = np.sum(n_GGE)
print(f"  Total quasiparticle pairs: {n_total_qp:.4f}")

# The pair correlations in the GGE (uncorrelated quasiparticles):
# <b_k^dag b_{k'}> = delta_{kk'} * u_k * v_k * (1 - 2*n_GGE_k)
# For k=k': <b_k^dag b_k> = u_k * v_k * (1 - 2*v_k^2) = u_k * v_k * (u_k^2 - v_k^2)
#                          = u_k * v_k * xi_k / E_k
# Since 1 - 2*v_k^2 = xi_k/E_k.

# Actually, in the GGE with completely destroyed condensate:
# The anomalous average <b_k> = 0 (number conservation restored)
# But the pair occupation <b_k^dag b_k> = v_k^2 (from frozen Bogoliubov amplitudes)

# The pair form factor in the GGE uses the RESIDUAL pair correlations.
# Since the condensate fraction is zero, the form factor comes from
# uncorrelated pair fluctuations:
# F_GGE(q) = Sum_k n_GGE_k * exp(i q . r_k)
# (no coherent enhancement)

S_GGE = np.zeros(n_q)
for iq, q in enumerate(q_grid):
    for k in range(n_modes):
        for kp in range(n_modes):
            if k == kp:
                d_kk = 0.0
                S_GGE[iq] += n_GGE[k]  # diagonal only
            # Off-diagonal: zero (uncorrelated quasiparticles)

# S_GGE(q) = Sum_k n_GGE_k = constant (no q-dependence for uncorrelated pairs!)
S_GGE_0 = np.sum(n_GGE)
F_GGE_norm = S_GGE / max(S_GGE_0, 1e-30)

print(f"\n  GGE form factor: F_GGE(q) = constant = {S_GGE_0:.6f}")
print(f"  This is q-INDEPENDENT: uncorrelated pairs have no spatial structure")
print(f"  (analogous to a dilute gas of localized pairs = BEC-side)")

# But there might be RESIDUAL off-diagonal correlations from the quench.
# In the sudden quench approximation, the post-quench state preserves
# the pre-quench pair correlations projected onto the conserved integrals.
# The off-diagonal elements <b_k^dag b_{k'}>_{GGE} for k != k' are:
#   <b_k^dag b_{k'}>_{GGE} = u_k v_k u_{k'} v_{k'} * P_{kk'}
# where P_{kk'} encodes the projection onto the GGE diagonal ensemble.
# For the Richardson-Gaudin integrable model:
#   P_{kk'} = (1 - 2*n_GGE_k) * delta_{kk'}  [only for fully dephased GGE]
# The off-diagonal pair correlations VANISH in the dephased GGE.

# However, at FINITE TIME after the quench, there are residual oscillating
# correlations. The pair form factor is time-dependent:
# <b_k^dag(t) b_{k'}(t)> = u_k v_k u_{k'} v_{k'} * cos(2*(E_k - E_{k'})*t)
# This dephases on the timescale 1/delta_E ~ 1/BW where BW is the bandwidth.

# For the STEADY-STATE GGE (t -> infinity), F(q) is flat.
# For the TRANSIENT state, F(q) shows oscillations.

# Compute the coherent part (pre-quench pair correlations):
S_coherent = np.zeros(n_q)
for iq, q in enumerate(q_grid):
    for k in range(n_modes):
        for kp in range(n_modes):
            d_kk = d_matrix[k, kp]
            # Coherent pair correlation from pre-quench BCS ground state
            # projected onto post-quench basis
            S_coherent[iq] += uv_product[k] * uv_product[kp] * j0(q * d_kk)

# This is just S_BCS again -- the pre-quench form factor
# At t>0, this gets modulated by dephasing factors

print(f"\n  Pre-quench vs GGE comparison:")
print(f"    Pre-quench: S(0) = {S_BCS_q0:.6f}, S(inf)/S(0) = {S_BCS_qinf/S_BCS_q0:.6f}")
print(f"    GGE (t->inf): S(q) = {S_GGE_0:.6f} (flat)")
print(f"    Ratio GGE/pre-quench at q=0: {S_GGE_0/S_BCS_q0:.6f}")

# ======================================================================
#  Step 9: Pair spatial extent and classification
# ======================================================================

print(f"\n{'='*78}")
print("PAIR SPATIAL EXTENT AND CLASSIFICATION")
print(f"{'='*78}")

# Summary of spatial scales:
L_SU3 = np.pi  # Characteristic size of SU(3) ~ pi/M_KK (in M_KK^{-1})
# Actually the diameter of SU(3) in the bi-invariant metric is pi * sqrt(2)
# for the normalization where the shortest geodesic loop has length 2*pi.
# But in our units (root length = 1/M_KK), the relevant scale is the
# distance between representations, which is d_01 = sqrt(1/3).

print(f"  Spatial scales (in M_KK^{{-1}} or root-length units):")
print(f"    Inter-sector distance d_01 = {d_01:.6f}")
print(f"    Pair RMS radius (BCS MF) = {r_rms:.6f}")
print(f"    BCS coherence length xi = {xi_BCS:.6f}")
print(f"    Ratio xi_BCS / d_01 = {xi_BCS / d_01:.4f}")
print(f"    Ratio R_rms / d_01 = {r_rms / d_01:.4f}")

# The crucial comparison: pair size vs system size
# In nuclear physics:
#   xi / R_nucleus ~ 3-10 (pair extends across the nucleus = BCS)
#   xi / R_nucleus < 1 (pair localized = BEC)
ratio_BCS = xi_BCS / d_01
print(f"\n  Classification criterion:")
print(f"    xi_BCS / d_01 = {ratio_BCS:.4f}")
if ratio_BCS > 2.0:
    pair_character = "EXTENDED BCS"
    print(f"    --> EXTENDED BCS (pairs span multiple representation sectors)")
elif ratio_BCS > 0.5:
    pair_character = "BCS-BEC CROSSOVER"
    print(f"    --> BCS-BEC CROSSOVER (pair size comparable to sector spacing)")
else:
    pair_character = "COMPACT BEC"
    print(f"    --> COMPACT BEC (pairs localized within single sector)")

# The pair concentration ratio: what fraction of the pair lives in each sector?
W_1_fraction = W_1_BCS / (W_0_BCS + W_1_BCS)
print(f"\n  Pair weight in (1,0) sector: {W_1_fraction*100:.2f}%")
print(f"  Pair weight in (0,0) sector: {(1-W_1_fraction)*100:.2f}%")
print(f"  This means {W_1_fraction*100:.1f}% of the pair extends to the next representation sector.")

# Also compute: how much does the pair amplitude vary across modes
# WITHIN the same sector?
uv_B2 = uv_product[:4]
uv_B1 = uv_product[4]
uv_B3 = uv_product[5:]

print(f"\n  Within-sector pair amplitude variation:")
print(f"    B2: u*v = {uv_B2} (CV = {np.std(uv_B2)/np.mean(uv_B2)*100:.1f}%)")
print(f"    B1: u*v = {uv_B1:.6f}")
print(f"    B3: u*v = {uv_B3} (CV = {np.std(uv_B3)/np.mean(uv_B3)*100:.1f}%)")

# ======================================================================
#  Step 10: The Pippard vs London limit
# ======================================================================

print(f"\n{'='*78}")
print("PIPPARD vs LONDON LIMIT")
print(f"{'='*78}")

# In superconductivity, the Pippard coherence length xi_0 vs the London
# penetration depth lambda_L determines the Type I/II classification.
# Ginzburg-Landau parameter kappa = lambda_L / xi_0:
#   kappa < 1/sqrt(2): Type I (Pippard, long coherence)
#   kappa > 1/sqrt(2): Type II (London, short coherence)
#
# The analog here: xi_BCS (coherence in tau-space) vs the inter-sector
# distance d_01 (penetration in representation space).
#
# This is a mixed classification: the pair extends ~1.4 sectors in
# representation space (BCS-BEC crossover) but has xi/BW = 13.95 in
# tau-space (strong BCS).

xi_over_BW = float(inst_data['xi_BCS_over_BW'])
BW = float(inst_data['B2_bw'])

print(f"  BCS coherence length: xi = {xi_BCS:.6f} M_KK^{{-1}}")
print(f"  B2 bandwidth: BW = {BW:.6f}")
print(f"  xi / BW = {xi_over_BW:.4f} (>> 1 = Pippard limit in tau-space)")
print(f"  xi / d_01 = {ratio_BCS:.4f} (> 1 = extended in rep space)")
print(f"\n  Conclusion: The pair is")
print(f"    - PIPPARD-TYPE in tau-space (xi >> BW, many levels within coherence volume)")
print(f"    - WEAKLY EXTENDED in rep-space (xi ~ 1.4 * d_01)")
print(f"    - BCS-BEC CROSSOVER for inter-sector correlations")

# For the GGE (post-transit):
print(f"\n  GGE (post-transit):")
print(f"    Pair correlations: DESTROYED (P_exc = 1.000)")
print(f"    Form factor: FLAT (uncorrelated quasiparticles)")
print(f"    Spatial character: LOCALIZED (no long-range pair order)")
print(f"    Relevant for: TESSELLATION (pairs are granular, not extended)")

# ======================================================================
#  Step 11: Cross-checks
# ======================================================================

print(f"\n{'='*78}")
print("CROSS-CHECKS")
print(f"{'='*78}")

# Check 1: Sum rule for form factor at q=0
SR_q0_BCS = S_BCS[0]
SR_expected = (np.sum(uv_product))**2
print(f"  Check 1: S_BCS(0) = {SR_q0_BCS:.10f}")
print(f"           (Sum u*v)^2 = {SR_expected:.10f}")
print(f"           Match: {abs(SR_q0_BCS - SR_expected) < 1e-10}")

# Check 2: Large-q limit
SR_qinf_computed = S_BCS[-1]
SR_qinf_expected = W_0_BCS**2 + W_1_BCS**2
print(f"\n  Check 2: S_BCS(q_max) = {SR_qinf_computed:.10f}")
print(f"           W_0^2 + W_1^2 = {SR_qinf_expected:.10f}")
# Note: not exactly equal because J_0 hasn't fully decayed at q=10

# Check 3: Pair occupation sum
print(f"\n  Check 3: Sum <n_k> = {np.sum(pair_occ):.6f} (should = 1 for N_pair=1)")

# Check 4: Condensate fraction
print(f"\n  Check 4: Condensate fraction = {condensate_fraction:.6f}")
print(f"           (from largest eigenvalue of pair correlation matrix)")
print(f"           Nuclear benchmark: >0.8 for well-deformed BCS (Paper 03)")

# Check 5: Natural orbital vs BCS pair wavefunction
# The natural orbital should be proportional to v_k (in BCS)
natural_norm = natural_pair / np.max(np.abs(natural_pair))
v_norm = v_k / np.max(v_k)
overlap = np.abs(np.dot(natural_pair, v_k / np.linalg.norm(v_k)))
print(f"\n  Check 5: |<natural_orbital | v_k>| = {overlap:.6f}")
print(f"           (1.0 = perfect BCS, 0 = completely different pairing)")

# Check 6: Verify that pair_corr is a rank-1 + correction structure
# In BCS: <b_i^dag b_j> = v_i * v_j + correction
# Rank of pair_corr
rank_1_approx = np.outer(np.sqrt(pair_occ), np.sqrt(pair_occ))
residual = pair_corr - rank_1_approx
print(f"\n  Check 6: Pair correlation rank structure")
print(f"    ||rank-1 approx|| = {np.linalg.norm(rank_1_approx):.6f}")
print(f"    ||residual|| = {np.linalg.norm(residual):.6f}")
print(f"    Relative residual = {np.linalg.norm(residual)/np.linalg.norm(pair_corr):.4f}")

# ======================================================================
#  Step 12: Summary table
# ======================================================================

print(f"\n{'='*78}")
print("SUMMARY TABLE")
print(f"{'='*78}")

print(f"\n  Quantity                         Value          Unit")
print(f"  {'='*60}")
print(f"  BCS coherence length xi          {xi_BCS:.6f}      M_KK^{{-1}}")
print(f"  Pairing gap Delta_pair           {Delta_pair:.6f}      M_KK")
print(f"  Inter-sector distance d_01       {d_01:.6f}      root-lengths")
print(f"  Pair RMS radius R_rms            {r_rms:.6f}      root-lengths")
print(f"  xi / d_01                        {ratio_BCS:.4f}")
print(f"  R_rms / d_01                     {r_rms/d_01:.4f}")
print(f"  xi / BW (tau-space)              {xi_over_BW:.4f}")
print(f"  Condensate fraction              {condensate_fraction:.6f}")
print(f"  W_1/W_0 (inter-sector weight)    {W_1_BCS/W_0_BCS:.6f}")
print(f"  S(inf)/S(0) (asymptotic ratio)   {S_BCS_qinf/S_BCS_q0:.6f}")
print(f"  Oscillation amplitude            {oscillation_amplitude:.6f}")
print(f"  GGE pair correlation             ZERO (flat F(q))")
print(f"  {'='*60}")
print(f"  CLASSIFICATION: {pair_character}")
print(f"  GGE STATE: LOCALIZED (uncorrelated, relevant for tessellation)")

# ======================================================================
#  Step 13: SAVE
# ======================================================================

print(f"\n{'='*78}")
print("SAVING RESULTS")
print(f"{'='*78}")

save_dict = {
    # Input parameters
    'V_8x8': V_8x8,
    'E_8': E_8,
    'rho': rho,
    'mu': mu,
    'n_modes': n_modes,
    'branch_labels': np.array(branch_labels),

    # BdG amplitudes (mean-field)
    'xi_k': xi,
    'Delta_k': Delta_k,
    'E_qp': E_qp,
    'u_k': u_k,
    'v_k': v_k,
    'uv_product': uv_product,

    # Pair correlation (ED)
    'pair_corr': pair_corr,
    'pair_occ': pair_occ,
    'pair_evals': pair_evals,
    'pair_evecs': pair_evecs,
    'natural_pair_orbital': natural_pair,
    'condensate_fraction': condensate_fraction,

    # Representation space coordinates
    'C2_mode': C2_mode,
    'r_mode': r_mode,
    'd_matrix': d_matrix,
    'omega_1': omega_1,
    'omega_2': omega_2,
    'd_01': d_01,

    # Form factors
    'q_grid': q_grid,
    'S_BCS': S_BCS,
    'F_BCS_norm': F_BCS_norm,
    'S_ED': S_ED,
    'F_ED_norm': F_ED_norm,
    'S_nat': S_nat,
    'F_nat_norm': F_nat_norm,
    'S_full': S_full,
    'F_full_norm': F_full_norm,
    'S_GGE': S_GGE,
    'F_GGE_norm': F_GGE_norm,

    # Sector decomposition
    'W_0_BCS': W_0_BCS,
    'W_1_BCS': W_1_BCS,
    'W_0_ED': W_0_ED,
    'W_1_ED': W_1_ED,

    # Spatial extent
    'r2_pair': r2_pair,
    'r_rms': r_rms,
    'xi_BCS': xi_BCS,
    'ratio_xi_d01': ratio_BCS,
    'pair_character': np.array([pair_character]),

    # BCS-BEC crossover
    'crossover_ratio': crossover_ratio,
    'xi_over_BW': xi_over_BW,

    # Asymptotic form factor
    'S_BCS_q0': S_BCS_q0,
    'S_BCS_qinf': S_BCS_qinf,
    'oscillation_amplitude': oscillation_amplitude,
    'q_first_zero': q_first_zero,
    'q_first_min': q_first_min,

    # GGE
    'n_GGE': n_GGE,
    'n_total_qp': n_total_qp,

    # Cross-checks
    'natural_orbital_overlap': overlap,
    'pair_corr_residual_norm': np.linalg.norm(residual)/np.linalg.norm(pair_corr),

    # Gate
    'gate_name': np.array(['PAIR-FF-43']),
    'gate_type': np.array(['INFO']),
}

out_npz = os.path.join(SCRIPT_DIR, 's43_pair_form_factor.npz')
np.savez_compressed(out_npz, **save_dict)
print(f"Saved: {out_npz}")
print(f"  Size: {os.path.getsize(out_npz) / 1024:.1f} KB")

# ======================================================================
#  Step 14: PLOT
# ======================================================================

print(f"\nGenerating plots...")

fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# --- Panel (a): Form factor F(q) for different methods ---
ax = axes[0, 0]
ax.plot(q_grid, F_BCS_norm, 'b-', lw=2, label='BCS mean-field (u*v)')
ax.plot(q_grid, F_ED_norm, 'r--', lw=2, label='ED (sqrt(<n_k>))')
ax.plot(q_grid, F_full_norm, 'g-.', lw=2, label='ED (full corr. matrix)')
ax.plot(q_grid, F_GGE_norm, 'k:', lw=2, label='GGE (uncorrelated)')

ax.axhline(S_BCS_qinf/S_BCS_q0, color='blue', ls=':', alpha=0.5,
           label=f'BCS asymptote = {S_BCS_qinf/S_BCS_q0:.4f}')
ax.axvline(q_first_zero, color='gray', ls='--', alpha=0.5,
           label=f'1st J_0 zero = {q_first_zero:.2f}')

ax.set_xlabel('q (M_KK)', fontsize=12)
ax.set_ylabel('F(q) / F(0)', fontsize=12)
ax.set_title('(a) Pair Transfer Form Factor', fontsize=13)
ax.legend(fontsize=7, loc='upper right')
ax.grid(True, alpha=0.3)
ax.set_xlim(0, q_max)
ax.set_ylim(0, 1.1)

# --- Panel (b): BdG amplitudes ---
ax = axes[0, 1]
x_pos = np.arange(n_modes)
width = 0.25

bars1 = ax.bar(x_pos - width, u_k, width, label='u_k', color='steelblue', alpha=0.8)
bars2 = ax.bar(x_pos, v_k, width, label='v_k', color='coral', alpha=0.8)
bars3 = ax.bar(x_pos + width, uv_product, width, label='u_k*v_k', color='seagreen', alpha=0.8)

ax.set_xlabel('Mode index k', fontsize=12)
ax.set_ylabel('Amplitude', fontsize=12)
ax.set_title('(b) BdG Amplitudes', fontsize=13)
ax.set_xticks(x_pos)
ax.set_xticklabels(branch_labels, fontsize=8, rotation=45)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3, axis='y')

# --- Panel (c): Pair correlation matrix ---
ax = axes[1, 0]
im = ax.imshow(pair_corr, cmap='RdBu_r', vmin=-0.05, vmax=0.30,
               interpolation='nearest', aspect='equal')
plt.colorbar(im, ax=ax, label='<b_i^dag b_j>')
ax.set_xticks(range(n_modes))
ax.set_yticks(range(n_modes))
ax.set_xticklabels(branch_labels, fontsize=7, rotation=45)
ax.set_yticklabels(branch_labels, fontsize=7)
ax.set_title(f'(c) Pair Correlation Matrix (ED)\n'
             f'Condensate frac = {condensate_fraction:.4f}', fontsize=12)

# --- Panel (d): Pair spatial structure ---
ax = axes[1, 1]

# Plot modes in representation space
# Site 0 (0,0) modes: at origin
# Site 1 (1,0) modes: at omega_1

# Size of markers proportional to pair weight
uv_scaled = uv_product / np.max(uv_product) * 500

# Plot B2 modes (small offsets to distinguish)
offsets_B2 = np.array([[-0.02, -0.02], [0.02, -0.02], [-0.02, 0.02], [0.02, 0.02]])
for k in range(4):
    pos = r_mode[k] + offsets_B2[k]
    ax.scatter(pos[0], pos[1], s=uv_scaled[k], c='steelblue',
               edgecolors='black', linewidth=0.5, zorder=5,
               label='B2' if k == 0 else None)

# B1
ax.scatter(r_mode[4, 0] + 0.03, r_mode[4, 1] + 0.03, s=uv_scaled[4],
           c='orange', edgecolors='black', linewidth=0.5, zorder=5,
           label='B1')

# B3 modes
offsets_B3 = np.array([[-0.02, -0.02], [0.02, -0.02], [0.0, 0.02]])
for k in range(3):
    pos = r_mode[5+k] + offsets_B3[k]
    ax.scatter(pos[0], pos[1], s=uv_scaled[5+k], c='coral',
               edgecolors='black', linewidth=0.5, zorder=5,
               label='B3' if k == 0 else None)

# Draw inter-sector connection with width proportional to cross-correlation
lw_cross = abs(f_cross_BCS) * 10
ax.plot([0, omega_1[0]], [0, omega_1[1]], 'k-', lw=lw_cross, alpha=0.3,
        label=f'Cross-sector: {f_cross_BCS:.3f}')

# Labels
ax.annotate('(0,0) sector\n5 modes', xy=(0, -0.06), ha='center', fontsize=9)
ax.annotate('(1,0) sector\n3 modes', xy=(omega_1[0], omega_1[1]+0.05),
            ha='center', fontsize=9)

ax.set_xlabel('x (root space)', fontsize=12)
ax.set_ylabel('y (root space)', fontsize=12)
ax.set_title(f'(d) Pair in Rep Space\n'
             f'xi/d_01={ratio_BCS:.2f} ({pair_character})', fontsize=12)
ax.legend(fontsize=7, loc='lower right')
ax.set_xlim(-0.15, 0.70)
ax.set_ylim(-0.15, 0.50)
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)

# Add overall title
fig.suptitle('PAIR-FF-43: Pair Transfer Form Factor at Finite Momentum\n'
             f'8-mode BCS on SU(3), xi/d_01={ratio_BCS:.2f}, '
             f'GGE: uncorrelated (flat F(q))',
             fontsize=14, fontweight='bold')
plt.tight_layout(rect=[0, 0, 1, 0.93])

out_png = os.path.join(SCRIPT_DIR, 's43_pair_form_factor.png')
plt.savefig(out_png, dpi=150)
plt.close()
print(f"Plot saved: {out_png}")

# ======================================================================
#  FINAL SUMMARY
# ======================================================================

elapsed = time.time() - t0

print(f"\n{'='*78}")
print(f"FINAL SUMMARY: PAIR-FF-43")
print(f"{'='*78}")
print(f"\n  Gate: PAIR-FF-43 (INFO)")
print(f"\n  1. BdG amplitudes reconstructed from mean-field BCS gap equation")
print(f"     Delta_k = {Delta_k}")
print(f"     u_k * v_k = {uv_product}")
print(f"\n  2. Form factor F(q) computed for q in [0, {q_max}] M_KK")
print(f"     - Only TWO distinct positions in rep space: (0,0) at origin, (1,0) at omega_1")
print(f"     - d_01 = {d_01:.6f} root-lengths")
print(f"     - F(q) = two-site structure: oscillates with period 2pi/d_01 = {2*np.pi/d_01:.2f}")
print(f"     - Asymptotic: F(inf)/F(0) = {S_BCS_qinf/S_BCS_q0:.4f}")
print(f"\n  3. Classification: {pair_character}")
print(f"     xi_BCS / d_01 = {ratio_BCS:.4f} (>1 but not >>1)")
print(f"     Pair RMS radius = {r_rms:.6f} root-lengths")
print(f"     Cross-sector weight = {f_cross_BCS*100:.2f}%")
print(f"     Condensate fraction = {condensate_fraction:.4f}")
print(f"\n  4. GGE (post-transit):")
print(f"     F_GGE(q) = FLAT (uncorrelated quasiparticles)")
print(f"     No long-range pair order (P_exc = 1.000)")
print(f"     Quasiparticle pairs = {n_total_qp:.1f} (localized in rep space)")
print(f"     --> Relevant for TESSELLATION, not domain walls")
print(f"\n  5. Physical interpretation:")
print(f"     Pre-transit: Cooper pair spans ~{ratio_BCS:.1f} rep-space sectors (weakly extended)")
print(f"     Post-transit: pairs uncorrelated, no spatial structure")
print(f"     The GGE relic has the spatial character of a granular gas,")
print(f"     not an extended superfluid. This is consistent with")
print(f"     tessellation-scale structure rather than smooth domain walls.")
print(f"\n  Runtime: {elapsed:.1f}s")
print(f"{'='*78}")
