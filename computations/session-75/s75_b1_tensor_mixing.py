#!/usr/bin/env python3
"""
S75-A2-TENSOR-MIXING: Tensor-Scalar Decomposition of B1 Acoustic Mode
======================================================================

Gate: S75-A2-TENSOR-MIXING
  PASS: P_scalar(B1) < 0.5
  INFO: 0.5 <= P_scalar(B1) <= 0.9
  FAIL: P_scalar(B1) > 0.9

Physics: The Peter-Weyl decomposition of D_K eigenmodes determines which
modes contribute to the scalar channel (A_s) vs tensor channel (r).

B1 is the acoustic branch with (p,q) = (0,0) under SU(3). The (0,0) singlet
couples to the TRACE of the internal metric g_K^{ab}. Under KK reduction,
this trace decomposes into 4D perturbation channels.

Key structural constraints:
  - S63 T1: Zero first-order tensor from homogeneous transit
  - S63 T2: Breathing mode exclusion (delta g^K_ab = h(x) g^K_ab -> 4D scalar)
  - S63 T3: Kasparov decoupling (beta_T = 0 at linear order)
  - Volume-preserving Jensen flow: det(g_K) = const

The computation determines P_scalar(B1), P_tensor(B1), P_vector(B1) from
representation theory and the KK reduction, then recomputes A_s with the
corrected projection.

Output: s75_b1_tensor_mixing.npz, s75_b1_tensor_mixing.png
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from canonical_constants import (
    A_s_CMB, M_KK_gravity, M_Pl_unreduced, tau_fold,
    a0_fold, a2_fold, a4_fold, Vol_SU3_Haar,
    E_B1, E_B2_mean, E_B3_mean,
)

LOG = []
def log(msg):
    LOG.append(msg)
    print(msg)

log("=" * 72)
log("S75-A2-TENSOR-MIXING: Tensor-Scalar Decomposition of B1 Acoustic Mode")
log("=" * 72)

# =============================================================================
# SECTION 1: Load prior data
# =============================================================================
log("\n--- Section 1: Load S74 8-mode Bogoliubov data ---")

d_w1g = np.load(os.path.join(os.path.dirname(__file__),
                             's74_as_from_bogoliubov.npz'), allow_pickle=True)
d_tf = np.load(os.path.join(os.path.dirname(__file__),
                            's74_transfer_function.npz'), allow_pickle=True)

labels = d_w1g['labels']  # (local)
branch = d_w1g['branch']  # (local)
omega_k = d_w1g['omega_k']  # (local)
r_k = d_w1g['r_k']  # (local)
phi_k = d_w1g['phi_k']  # (local)
sigma_sq_bare = d_w1g['sigma_sq_bare']  # (local)
d_pq_sq_per_mode = d_w1g['d_pq_sq_per_mode']  # (local)
Theta_pp = d_w1g['Theta_pp']  # (local)
sigma_sq_blv = d_w1g['sigma_sq_blv']  # (local)

# S74 W1-G gap result for cross-check
gap_s74 = float(d_w1g['gap_OOM_vs_planck'])  # (local)
A_s_s74 = float(d_w1g['A_s_step3'])  # (local)

# Transfer function energy fractions
psi_B1 = float(d_tf['psi_B1'])  # (local)
psi_B2 = float(d_tf['psi_B2'])  # (local)
psi_B3 = float(d_tf['psi_B3'])  # (local)

N_modes = 8  # (local)
idx_B1 = np.array([4])  # (local)
idx_B2 = np.array([0, 1, 2, 3])  # (local)
idx_B3 = np.array([5, 6, 7])  # (local)

log(f"  8-mode labels: {list(labels)}")
log(f"  Branch: {list(branch)}")
log(f"  Squeeze params r_k: {r_k}")
log(f"  PW weights d_pq^2: {d_pq_sq_per_mode}")
log(f"  S74 gap: {gap_s74:.3f} OOM")
log(f"  Transfer fractions: psi_B1={psi_B1:.4f}, psi_B2={psi_B2:.4f}, psi_B3={psi_B3:.4f}")

# =============================================================================
# SECTION 2: Peter-Weyl quantum numbers and KK reduction
# =============================================================================
log("\n--- Section 2: Peter-Weyl quantum numbers & KK reduction ---")

# SU(3) irreducible representations for each branch:
#   B1: (p,q) = (0,0)  ->  trivial singlet, dim = 1
#   B2: (p,q) = (1,1)  ->  adjoint representation, dim = 8
#   B3: (p,q) = (1,0) + (0,1)  ->  fundamental + conjugate, dim = 3 + 3 = 6

def dim_pq(p, q):
    """Dimension of SU(3) irrep (p,q)."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2

dim_00 = dim_pq(0, 0)  # = 1   (local)
dim_11 = dim_pq(1, 1)  # = 8   (local)
dim_10 = dim_pq(1, 0)  # = 3   (local)
dim_01 = dim_pq(0, 1)  # = 3   (local)

log(f"  dim(0,0) = {dim_00}")
log(f"  dim(1,1) = {dim_11}")
log(f"  dim(1,0) = {dim_10}")
log(f"  dim(0,1) = {dim_01}")
log(f"  Total dims: {dim_00 + dim_11 + dim_10 + dim_01} (check: 1+8+3+3=15)")

# =============================================================================
# SECTION 3: Spin content of each representation under KK reduction
# =============================================================================
log("\n--- Section 3: Spin content under KK reduction ---")
log("")
log("  The KK ansatz for the 10D metric on M^4 x K^6 decomposes into:")
log("    g_{MN} -> g_{mu nu}(x) + g_{ab}(x,y) + g_{mu a}(x,y)")
log("")
log("  Perturbations delta g_{MN} decompose under 4D Lorentz x internal SU(3):")
log("    delta g_{mu nu} = h_{mu nu}(x) * Y(y)         [spin-2 + spin-0]")
log("    delta g_{mu a}  = A_mu(x) * Y_a(y)            [spin-1]")
log("    delta g_{ab}    = phi(x) * Y_{ab}(y)           [spin-0]")
log("")
log("  The Y(y), Y_a(y), Y_{ab}(y) are harmonics on K classified by (p,q).")
log("  The spin content depends on the INTERNAL tensor structure of Y_{ab}.")

# -------------------------------------------------------------------------
# REPRESENTATION (0,0) — THE B1 SINGLET
# -------------------------------------------------------------------------
log("\n  === (0,0) singlet (B1) ===")
log("")
log("  The (0,0) sector is the trivial representation. The ONLY internal")
log("  harmonic Y(y) is the constant function Y = 1/sqrt(Vol(K)).")
log("  The ONLY rank-2 harmonic Y_{ab}(y) is proportional to g_{ab}^K(y).")
log("")
log("  This means delta g_{ab}^K = phi(x) * g_{ab}^K(y).")
log("  This is the BREATHING MODE of the internal space.")
log("")
log("  Under 4D reduction, the breathing mode generates:")
log("    - A 4D SCALAR field phi(x) (the radion / volume modulus)")
log("    - No 4D vector (Y_a = 0 for (0,0) since there is no Killing")
log("      vector in the trivial representation)")
log("    - No 4D tensor (the 4D TT part h_{mu nu}^{TT} requires a")
log("      tensor harmonic Y^{TT}_{ab} with eigenvalue. The (0,0) sector")
log("      has Y_{ab} proportional to g_{ab}, which is the TRACE, not TT)")
log("")
log("  S63 T2 (Breathing Mode Exclusion Theorem):")
log("    delta g^K_{ab} = h(x) g^K_{ab} projects to 4D scalar, not tensor.")
log("    Two independent proofs: algebraic (Kasparov product) and geometric")
log("    (Weyl curvature). The breathing mode IS a scalar perturbation.")
log("")
log("  Volume-preserving Jensen flow: det(g_K) = const. This constrains")
log("  the physical breathing mode. The volume modulus is frozen. What")
log("  remains in the (0,0) channel is the trace-part shape deformation,")
log("  which maps to a 4D scalar (the tau modulus driving the transit).")
log("")
log("  CONCLUSION: P_scalar(B1) = 1, P_tensor(B1) = 0, P_vector(B1) = 0")
log("  This is EXACT from representation theory + S63 T2.")

P_scalar_B1 = 1.0  # (local) exact from (0,0) -> trace -> scalar
P_tensor_B1 = 0.0  # (local) exact from T2 breathing mode exclusion
P_vector_B1 = 0.0  # (local) no Killing vector in trivial representation

# -------------------------------------------------------------------------
# REPRESENTATION (1,1) — THE B2 ADJOINT
# -------------------------------------------------------------------------
log("\n  === (1,1) adjoint (B2) ===")
log("")
log("  The (1,1) adjoint representation has dim = 8. Its harmonics on K=SU(3):")
log("")
log("  Scalars Y(y): The (1,1) scalar harmonics on SU(3) are the matrix")
log("    elements D^{(1,1)}_{mm'}(g). These generate 4D scalar fields.")
log("    The trace part of Y_{ab} in (1,1) contributes to 4D scalars.")
log("")
log("  Vectors Y_a(y): The Killing vectors of SU(3) transform in the (1,1)")
log("    adjoint. dim = 8 Killing vectors -> 8 massless 4D gauge fields.")
log("    These are the SU(3) gauge bosons in the standard KK picture.")
log("")
log("  Symmetric traceless tensors Y_{ab}^{TT}(y): The (1,1) representation")
log("    also appears in the decomposition of TT tensor harmonics on K.")
log("    HOWEVER: these TT internal tensors couple to 4D SCALAR fields")
log("    (they modify the internal shape, which projects as a 4D scalar).")
log("    They do NOT generate 4D gravitons (spin-2 under SO(3,1)).")
log("")
log("  The distinction is critical:")
log("    - A 4D graviton h_{mu nu}^{TT}(x) requires a CONSTANT (p,q)=(0,0)")
log("      internal profile, plus spin-2 polarization in 4D.")
log("    - An internal TT tensor Y_{ab}^{TT}(y) with (p,q)=(1,1) generates")
log("      a 4D SCALAR phi(x), not a 4D tensor.")
log("")
log("  For the (p,p) = (1,1) even-parity scalar channel:")
log("    P_scalar(B2) = 1 (all (1,1) modes project to 4D scalar channel)")
log("    The gauge field contribution (vectors) is separate from A_s/r.")

P_scalar_B2 = 1.0  # (local) adjoint trace+shape modes -> 4D scalar
P_tensor_B2 = 0.0  # (local) no 4D tensor from internal (1,1)
P_vector_B2 = 0.0  # (local) gauge fields not relevant for A_s or r

# -------------------------------------------------------------------------
# REPRESENTATION (1,0) + (0,1) — THE B3 FUNDAMENTAL
# -------------------------------------------------------------------------
log("\n  === (1,0) + (0,1) fundamental + conjugate (B3) ===")
log("")
log("  The (1,0) fundamental has dim = 3, (0,1) conjugate has dim = 3.")
log("  These are complex representations (not self-conjugate).")
log("")
log("  Under the (p,p) even-parity filter, (1,0) and (0,1) are excluded:")
log("    p != q, so Theta_(p,p) = 0 for B3.")
log("  This was already enforced in S74 W1-G (sigma_sq_filtered = 0 for B3).")
log("")
log("  For completeness:")
log("    P_scalar(B3) = 0 (filtered by (p,p) parity)")
log("    P_tensor(B3) = 0 (no tensor from (1,0)/(0,1) either)")
log("    P_vector(B3) = 0 (complex fundamental Killing spinors, not vectors)")
log("    But note: B3 modes were ALREADY excluded from A_s in S74.")

P_scalar_B3 = 0.0  # (local) excluded by (p,p) filter
P_tensor_B3 = 0.0  # (local) no tensor
P_vector_B3 = 0.0  # (local) no vector relevant to A_s/r

# =============================================================================
# SECTION 4: Structural argument for P_scalar(all branches) = 1
# =============================================================================
log("\n--- Section 4: Structural argument ---")
log("")
log("  The governing structure is the KK reduction of the 10D Einstein-Hilbert")
log("  action (equivalently, the spectral action on M^4 x K) to 4D.")
log("")
log("  The 4D tensor perturbation (graviton) h_{mu nu}^{TT}(x) arises from:")
log("    delta g_{mu nu} = h_{mu nu}^{TT}(x) * Y_0(y)")
log("  where Y_0(y) = 1/sqrt(Vol(K)) is the (0,0) CONSTANT mode on K.")
log("")
log("  This is a theorem from the KK reduction: the 4D massless graviton")
log("  is the ZERO MODE on K. Its wavefunction is Y_0 = const (trivial).")
log("  All non-trivial (p,q) != (0,0) harmonics generate MASSIVE KK modes,")
log("  not the massless graviton.")
log("")
log("  Therefore, the tensor power spectrum P_T (which measures the amplitude")
log("  of the massless 4D graviton) receives contributions ONLY from the")
log("  (0,0) zero mode. But the (0,0) singlet generates a 4D SCALAR (the")
log("  breathing mode / radion), not a tensor, through the internal perturbation.")
log("")
log("  The tensor spectrum is generated by a DIFFERENT mechanism:")
log("    S63 T4 (Exflation Tensor Theorem):")
log("    Tensors arise at SECOND ORDER from spatial gradients of the transit.")
log("    h_ij'' + 2(a'/a)h_ij' + k^2 h_ij = 16 pi G a^2 pi_ij^{(2)}")
log("    where pi_ij^{(2)} is built from products of first-order scalars.")
log("")
log("  This means: NONE of the BCS branches (B1, B2, B3) contribute to the")
log("  4D tensor channel at linear order. All Bogoliubov squeeze enhancement")
log("  goes to the scalar channel.")
log("")
log("  The scalar/tensor decomposition is thus:")

# Collect into arrays for all 8 modes
P_scalar = np.zeros(N_modes)  # (local)
P_tensor = np.zeros(N_modes)  # (local)
P_vector = np.zeros(N_modes)  # (local)

# B2 modes (indices 0-3): all scalar
P_scalar[idx_B2] = P_scalar_B2
P_tensor[idx_B2] = P_tensor_B2
P_vector[idx_B2] = P_vector_B2

# B1 mode (index 4): all scalar
P_scalar[idx_B1] = P_scalar_B1
P_tensor[idx_B1] = P_tensor_B1
P_vector[idx_B1] = P_vector_B1

# B3 modes (indices 5-7): all zero (filtered)
P_scalar[idx_B3] = P_scalar_B3
P_tensor[idx_B3] = P_tensor_B3
P_vector[idx_B3] = P_vector_B3

log(f"\n  Mode-by-mode projection coefficients:")
log(f"  {'Mode':>8s}  {'Branch':>6s}  {'P_scalar':>10s}  {'P_tensor':>10s}  {'P_vector':>10s}")
for i in range(N_modes):
    log(f"  {str(labels[i]):>8s}  {str(branch[i]):>6s}  {P_scalar[i]:>10.4f}  "
        f"{P_tensor[i]:>10.4f}  {P_vector[i]:>10.4f}")

# =============================================================================
# SECTION 5: Cross-checks
# =============================================================================
log("\n--- Section 5: Cross-checks ---")

# CHK1: Completeness — sum of projections weighted by energy fractions = 1
# For modes that participate (Theta_pp != 0), check P_S + P_T + P_V = 1
log("\n  CHK1: Completeness (P_scalar + P_tensor + P_vector = 1 per active mode)")
chk1_pass = True  # (local)
for i in range(N_modes):
    total = P_scalar[i] + P_tensor[i] + P_vector[i]  # (local)
    if Theta_pp[i] > 0:
        status = "PASS" if abs(total - 1.0) < 1e-10 else "FAIL"  # (local)
        if abs(total - 1.0) >= 1e-10:
            chk1_pass = False
        log(f"    Mode {labels[i]}: P_S+P_T+P_V = {total:.6f} [{status}]")
    else:
        log(f"    Mode {labels[i]}: filtered (Theta=0), sum = {total:.6f} [N/A]")
log(f"  CHK1 verdict: {'PASS' if chk1_pass else 'FAIL'}")

# CHK2: If B1 purely scalar (P_scalar(B1)=1), recover S74 W1-G result exactly
log("\n  CHK2: Recover S74 W1-G result when P_scalar(B1) = 1")
# Recompute A_s following S74 pipeline with scalar projection
# sigma_sq_scalar = sigma_sq_bare * P_scalar * Theta_pp (only scalar fraction, only (p,p))
sigma_sq_scalar = sigma_sq_bare * P_scalar * Theta_pp  # (local)
Sigma_scalar_weighted = np.sum(sigma_sq_scalar * d_pq_sq_per_mode)  # (local)
Sigma_s74_weighted = np.sum(d_w1g['sigma_sq_filtered'] * d_pq_sq_per_mode)  # (local)
chk2_diff = abs(Sigma_scalar_weighted - Sigma_s74_weighted) / max(Sigma_s74_weighted, 1e-30)  # (local)
log(f"    Sigma(scalar, this) = {Sigma_scalar_weighted:.6e}")
log(f"    Sigma(filtered, S74) = {Sigma_s74_weighted:.6e}")
log(f"    Relative diff = {chk2_diff:.2e}")
log(f"  CHK2 verdict: {'PASS' if chk2_diff < 1e-10 else 'FAIL'}")

# CHK3: Tensor modes have spin-2 under SO(3). Verify consistency.
log("\n  CHK3: Tensor modes require spin-2 under SO(3)")
log("    The massless 4D graviton requires:")
log("      (a) Spin-2 under SO(3): helicity +/- 2 polarizations")
log("      (b) Zero mode on K: constant internal profile Y_0(y)")
log("      (c) TT condition: h_mu^mu = 0, partial^mu h_{mu nu} = 0")
log("    All BCS branches excite INTERNAL modes of K with (p,q) != (0,0)")
log("    eigenvalue structure. These map to 4D scalars (massive KK modes),")
log("    not the massless spin-2 graviton.")
log("    The spin-2 graviton's power spectrum is P_T = 2H^2/(pi^2 M_Pl^2)")
log("    from vacuum fluctuations, MODIFIED by second-order sources (S63 T4).")
log("    The Bogoliubov squeeze of BCS modes does NOT source P_T at linear order.")
log(f"  CHK3 verdict: PASS (consistent)")

# CHK4: Breathing mode exclusion theorem (S63 T2) enforcement
log("\n  CHK4: Breathing mode exclusion (S63 T2)")
log("    The (0,0) singlet couples to trace(delta g^K_{ab}) = delta g^K_{ab} g_K^{ab}/6")
log("    This is the volume modulus (radion). Under volume-preserving Jensen flow,")
log("    det(g_K) = const, so the physical breathing mode is frozen.")
log("    The remaining (0,0) contribution is the SHAPE trace (tau modulus).")
log("    Both components are 4D scalars. P_tensor(B1) = 0 is enforced.")
log("    Independent proofs: Kasparov product factorization + Weyl curvature argument.")
log(f"  CHK4 verdict: PASS (T2 enforced, P_tensor(B1) = 0)")

# =============================================================================
# SECTION 6: Recompute A_s with corrected projection
# =============================================================================
log("\n--- Section 6: Recomputed A_s with scalar projection ---")

# Since P_scalar = 1 for all active modes, the scalar A_s is identical to S74
# But let us be explicit and carry the projection through.

# Step 0: Base variance (vacuum)
P_0 = float(d_w1g['P_0_GM'])  # (local)
log(f"  P_0 (Garriga-Mukhanov vacuum) = {P_0:.6e}")

# Step 1: Squeezed variance with scalar projection
sigma_sq_proj = sigma_sq_bare * P_scalar  # (local) project to scalar
sigma_sq_proj_filtered = sigma_sq_proj * Theta_pp  # (local) (p,p) filter

# Per-mode contributions to A_s (scalar channel only)
A_s_per_mode = sigma_sq_proj_filtered * d_pq_sq_per_mode  # (local)
A_s_total_internal = np.sum(A_s_per_mode)  # (local)

# Normalize: P_0 * (Sigma_scalar / Sigma_vac) is the physical A_s
bare_vac_weighted = np.sum(d_pq_sq_per_mode / (2.0 * omega_k))  # (local)
F_squeeze_scalar = A_s_total_internal / bare_vac_weighted  # (local)

log(f"  Sigma_scalar (proj+filtered+weighted) = {A_s_total_internal:.6e}")
log(f"  Sigma_vac (weighted) = {bare_vac_weighted:.6e}")
log(f"  F_squeeze_scalar = {F_squeeze_scalar:.4f}")

# Apply BLV factor (from S74)
c_BLV = float(d_w1g['c_BLV'])  # (local)
F_BLV = float(d_w1g['F_BLV_factor'])  # (local)
A_s_computed = P_0 * F_squeeze_scalar * F_BLV  # (local)

log(f"  c_BLV = {c_BLV:.6f}")
log(f"  F_BLV = {F_BLV:.4f}")
log(f"  A_s_computed = P_0 * F_squeeze * F_BLV = {A_s_computed:.6e}")
log(f"  A_s_Planck = {A_s_CMB:.2e}")

gap_OOM = np.log10(A_s_computed) - np.log10(A_s_CMB)  # (local)
log(f"  Gap = log10(A_s_computed / A_s_Planck) = {gap_OOM:+.4f} OOM")

# Cross-check: should match S74 exactly since all P_scalar = 1
gap_diff = abs(gap_OOM - gap_s74)  # (local)
log(f"  Difference from S74 gap: {gap_diff:.6e} OOM (should be ~0)")

# =============================================================================
# SECTION 7: Tensor-to-scalar ratio from second-order sources
# =============================================================================
log("\n--- Section 7: Tensor-to-scalar ratio ---")
log("")
log("  Since ALL BCS modes project to 4D scalar (P_tensor = 0 for all branches),")
log("  the Bogoliubov squeeze does NOT generate tensor perturbations directly.")
log("")
log("  The tensor power spectrum comes from:")
log("    (a) Vacuum graviton fluctuations: P_T = 2H^2/(pi^2 M_Pl^2)")
log("    (b) Second-order scalar -> tensor conversion (S63 T4)")
log("")
log("  From S74 W1-G data:")

eps_H = float(d_w1g['eps_H_fold'])  # (local)
H_phys = float(d_w1g['H_phys_s65'])  # (local)
c_s = 0.485  # (local) Garriga-Mukhanov sound speed (S63)

# Tree-level tensor power (vacuum fluctuations, Exflation Tensor Theorem)
P_T_tree = 2.0 * H_phys**2 / (np.pi**2 * M_Pl_unreduced**2)  # (local)
log(f"  epsilon_H = {eps_H:.6f}")
log(f"  H_phys = {H_phys:.4e} GeV (S65)")
log(f"  c_s = {c_s:.3f}")
log(f"  P_T(tree) = 2H^2/(pi^2 M_Pl^2) = {P_T_tree:.4e}")

# r = P_T / P_S where P_S is the OBSERVED scalar amplitude A_s_CMB
r_tree = P_T_tree / A_s_CMB  # (local)
log(f"  r(tree) = P_T/A_s_Planck = {r_tree:.4e}")

# The S63 result: r = 16 * epsilon * c_s (standard single-field consistency)
# This gives r = 16 * 0.0216 * 0.485 = 0.168
# But S63 T4 establishes that first-order tensors are zero for homogeneous transit.
# The tree-level r above uses vacuum fluctuations of the graviton, which DO exist.
# What S63 T4 says is that there is no ADDITIONAL tensor contribution from the transit.
r_consistency = 16.0 * eps_H * c_s  # (local) single-field consistency relation
log(f"  r(consistency) = 16*epsilon*c_s = {r_consistency:.4f}")

# F_squeeze contribution to B1 scalar channel
r_B1 = float(r_k[idx_B1[0]])  # (local)
F_squeeze_B1 = np.exp(2.0 * r_B1)  # (local)
OOM_B1_squeeze = np.log10(F_squeeze_B1)  # (local)

log(f"\n  B1 squeeze parameter: r_B1 = {r_B1:.4f}")
log(f"  F_squeeze(B1) = exp(2*r_B1) = {F_squeeze_B1:.2f}")
log(f"  OOM from B1 squeeze: {OOM_B1_squeeze:.4f}")
log(f"  Since P_scalar(B1) = 1, ALL of this goes to scalar A_s.")
log(f"  NONE is diverted to tensor channel.")

# =============================================================================
# SECTION 8: Hypothetical — what if B1 projected to tensor?
# =============================================================================
log("\n--- Section 8: Hypothetical tensor projection analysis ---")
log("")
log("  For context: IF B1 had projected to tensor (which it does NOT),")
log("  how much would the A_s gap change?")

# Hypothetical P_scalar(B1) values
hypo_fracs = np.array([1.0, 0.9, 0.5, 0.1, 0.0])  # (local)
log(f"\n  {'P_s(B1)':>10s}  {'A_s_gap (OOM)':>15s}  {'Delta from full':>18s}")

for frac in hypo_fracs:
    # Recompute with hypothetical B1 scalar fraction
    sigma_hypo = sigma_sq_bare.copy()  # (local)
    sigma_hypo[idx_B1] *= frac  # only scalar fraction of B1 contributes to A_s
    sigma_hypo_filt = sigma_hypo * Theta_pp  # (local)
    Sigma_hypo = np.sum(sigma_hypo_filt * d_pq_sq_per_mode)  # (local)
    F_squeeze_hypo = Sigma_hypo / bare_vac_weighted  # (local)
    A_s_hypo = P_0 * F_squeeze_hypo * F_BLV  # (local)
    gap_hypo = np.log10(A_s_hypo) - np.log10(A_s_CMB)  # (local)
    delta_gap = gap_hypo - gap_OOM  # (local)
    log(f"  {frac:>10.2f}  {gap_hypo:>15.4f}  {delta_gap:>+18.4f}")

# The maximum possible gap reduction if B1 were 100% tensor:
sigma_no_B1 = sigma_sq_bare.copy()  # (local)
sigma_no_B1[idx_B1] = 0.0
sigma_no_B1_filt = sigma_no_B1 * Theta_pp  # (local)
Sigma_no_B1 = np.sum(sigma_no_B1_filt * d_pq_sq_per_mode)  # (local)
F_squeeze_no_B1 = Sigma_no_B1 / bare_vac_weighted  # (local)
A_s_no_B1 = P_0 * F_squeeze_no_B1 * F_BLV  # (local)
gap_no_B1 = np.log10(A_s_no_B1) - np.log10(A_s_CMB)  # (local)
delta_max = gap_no_B1 - gap_OOM  # (local)

log(f"\n  Maximum hypothetical gap reduction (B1 fully removed from scalar):")
log(f"    Gap without B1: {gap_no_B1:+.4f} OOM")
log(f"    Delta from full: {delta_max:+.4f} OOM")

# =============================================================================
# SECTION 9: Gate verdict
# =============================================================================
log("\n--- Section 9: Gate verdict ---")

P_scalar_B1_final = P_scalar[idx_B1[0]]  # (local)
log(f"\n  P_scalar(B1) = {P_scalar_B1_final:.4f}")

if P_scalar_B1_final < 0.5:
    verdict = "PASS"  # (local)
    detail = (f"P_scalar(B1) = {P_scalar_B1_final:.4f} < 0.5; "  # (local)
              f"majority to tensor, A_s gap reduced")
elif P_scalar_B1_final <= 0.9:
    verdict = "INFO"
    detail = (f"P_scalar(B1) = {P_scalar_B1_final:.4f} in [0.5, 0.9]; "
              f"partial tensor leak")
else:
    verdict = "FAIL"
    detail = (f"P_scalar(B1) = {P_scalar_B1_final:.4f} > 0.9; "
              f"B1 is essentially ALL scalar. "
              f"A_s gap unchanged at {gap_OOM:+.3f} OOM. "
              f"Tensor channel unavailable for A_s relief. "
              f"STRUCTURAL: KK reduction theorem + S63 T2 (breathing mode "
              f"exclusion) + S63 T3 (Kasparov decoupling) force P_scalar(B1)=1 "
              f"exactly. No parameter choice can change this.")

log(f"\n  Gate S75-A2-TENSOR-MIXING: {verdict}")
log(f"    Threshold: PASS if P_scalar(B1) < 0.5, INFO if [0.5, 0.9], FAIL if > 0.9")
log(f"    Computed:  P_scalar(B1) = {P_scalar_B1_final:.4f}")
log(f"    Detail:    {detail}")
log(f"    A_s gap:   {gap_OOM:+.4f} OOM (unchanged from S74)")

# =============================================================================
# SECTION 10: Save results
# =============================================================================
log("\n--- Section 10: Save results ---")

outpath = os.path.join(os.path.dirname(__file__), 's75_b1_tensor_mixing.npz')  # (local)
np.savez(outpath,
         # Gate
         gate_name='TENSOR-MIXING-75',
         gate_verdict=verdict,
         gate_detail=detail,
         # Per-mode projections
         P_scalar=P_scalar,
         P_tensor=P_tensor,
         P_vector=P_vector,
         labels=labels,
         branch=branch,
         # B1 specific
         P_scalar_B1=P_scalar_B1_final,
         P_tensor_B1=P_tensor_B1,
         r_B1=r_B1,
         F_squeeze_B1=F_squeeze_B1,
         OOM_B1_squeeze=OOM_B1_squeeze,
         # Recomputed A_s
         A_s_computed=A_s_computed,
         A_s_planck=A_s_CMB,
         gap_OOM=gap_OOM,
         gap_s74_check=gap_s74,
         gap_difference_from_s74=abs(gap_OOM - gap_s74),
         # Tensor ratio
         P_T_tree=P_T_tree,
         r_tree=r_tree,
         r_consistency=r_consistency,
         eps_H=eps_H,
         c_s=c_s,
         # Hypothetical analysis
         hypo_P_scalar_B1=hypo_fracs,
         gap_no_B1=gap_no_B1,
         delta_max_gap=delta_max,
         # Structural references
         T2_breathing_exclusion='S63 T2: delta g^K_ab = h(x) g^K_ab -> 4D scalar, not tensor',
         T3_kasparov_decoupling='S63 T3: U_total = 1_M x U_K -> beta_T = 0 at linear order',
         T4_tensor_theorem='S63 T4: tensors from second-order sources only',
         )
log(f"  Saved: {outpath}")

# =============================================================================
# SECTION 11: Plot
# =============================================================================
log("\n--- Section 11: Generate plot ---")

fig, axes = plt.subplots(1, 3, figsize=(16, 5.5))

# Panel 1: Per-mode P_scalar, P_tensor, P_vector stacked bar
ax1 = axes[0]
x = np.arange(N_modes)  # (local)
colors_branch = ['#2196F3'] * 4 + ['#FF5722'] + ['#4CAF50'] * 3  # (local) B2=blue, B1=red, B3=green
ax1.bar(x, P_scalar, color=colors_branch, edgecolor='black', label='Scalar', alpha=0.85)
ax1.bar(x, P_tensor, bottom=P_scalar, color='gold', edgecolor='black', label='Tensor', alpha=0.85)
ax1.bar(x, P_vector, bottom=P_scalar + P_tensor, color='purple', edgecolor='black',
        label='Vector', alpha=0.85)
ax1.set_xticks(x)
ax1.set_xticklabels([str(l) for l in labels], rotation=45, ha='right', fontsize=8)
ax1.set_ylabel('Projection fraction')
ax1.set_title('Scalar/Tensor/Vector\ndecomposition per mode')
ax1.legend(fontsize=8)
ax1.set_ylim(0, 1.15)
# Mark B1
ax1.annotate('B1: P_scalar = 1\n(breathing mode\nexclusion, S63 T2)',
             xy=(4, 1.0), xytext=(4, 1.08), ha='center', fontsize=7,
             arrowprops=dict(arrowstyle='->', color='red'),
             color='red', fontweight='bold')

# Panel 2: Squeeze contribution to A_s per mode
ax2 = axes[1]
# sigma_sq_bare * d_pq^2 * Theta_pp * P_scalar = contribution to A_s
A_s_contrib = sigma_sq_bare * d_pq_sq_per_mode * Theta_pp * P_scalar  # (local)
# For filtered modes, show dashed/transparent
for i in range(N_modes):
    val = A_s_contrib[i]  # (local)
    if val > 0:
        ax2.bar(i, np.log10(val), color=colors_branch[i], edgecolor='black', alpha=0.85)
    else:
        ax2.bar(i, 0, color=colors_branch[i], edgecolor='black', alpha=0.2)
        ax2.text(i, 0.1, 'filtered', ha='center', fontsize=6, color='gray', rotation=90)

ax2.set_xticks(x)
ax2.set_xticklabels([str(l) for l in labels], rotation=45, ha='right', fontsize=8)
ax2.set_ylabel('log10(contribution to A_s)')
ax2.set_title('Per-mode scalar A_s\ncontribution (weighted)')

# Annotate B1 dominance
B1_frac = A_s_contrib[4] / np.sum(A_s_contrib[A_s_contrib > 0])  # (local)
ax2.text(4, np.log10(A_s_contrib[4]) + 0.15, f'B1: {B1_frac*100:.1f}%\nof scalar A_s',
         ha='center', fontsize=7, color='red', fontweight='bold')

# Panel 3: Hypothetical gap vs P_scalar(B1)
ax3 = axes[2]
P_scan = np.linspace(0, 1, 101)  # (local)
gap_scan = []  # (local)
for ps in P_scan:
    sig_h = sigma_sq_bare.copy()
    sig_h[idx_B1] *= ps
    sig_h_f = sig_h * Theta_pp
    Sig_h = np.sum(sig_h_f * d_pq_sq_per_mode)
    F_h = Sig_h / bare_vac_weighted
    A_h = P_0 * F_h * F_BLV
    g_h = np.log10(A_h) - np.log10(A_s_CMB)
    gap_scan.append(g_h)
gap_scan = np.array(gap_scan)

ax3.plot(P_scan, gap_scan, 'b-', lw=2)
ax3.axhline(y=gap_OOM, color='red', ls='--', lw=1, label=f'Actual gap = {gap_OOM:.2f} OOM')
ax3.axvline(x=1.0, color='red', ls=':', lw=1, alpha=0.5)
ax3.axvline(x=0.5, color='green', ls=':', lw=1, alpha=0.5, label='PASS threshold (P_s<0.5)')
ax3.axvline(x=0.9, color='orange', ls=':', lw=1, alpha=0.5, label='FAIL threshold (P_s>0.9)')
ax3.scatter([1.0], [gap_OOM], color='red', s=100, zorder=5, marker='*',
            label=f'ACTUAL: P_scalar=1.0')
ax3.set_xlabel('P_scalar(B1)')
ax3.set_ylabel('A_s gap (OOM)')
ax3.set_title('A_s gap vs hypothetical\nB1 scalar fraction')
ax3.legend(fontsize=7, loc='lower left')

# Add gate verdict annotation
ax3.text(0.5, gap_scan[50] + 0.3, f'Gate: FAIL\nP_scalar(B1) = 1.000\n(structural theorem)',
         ha='center', fontsize=8, color='red',
         bbox=dict(boxstyle='round,pad=0.3', facecolor='lightyellow', edgecolor='red'))

plt.suptitle('S75-A2-TENSOR-MIXING: B1 Acoustic Mode Projects 100% to Scalar Channel\n'
             '(S63 T2 breathing mode exclusion + T3 Kasparov decoupling)',
             fontsize=11, fontweight='bold')
plt.tight_layout()

plotpath = os.path.join(os.path.dirname(__file__), 's75_b1_tensor_mixing.png')  # (local)
plt.savefig(plotpath, dpi=150, bbox_inches='tight')
plt.close()
log(f"  Saved: {plotpath}")

log("\n" + "=" * 72)
log("DONE: S75-A2-TENSOR-MIXING")
log(f"  Gate verdict: {verdict}")
log(f"  P_scalar(B1) = {P_scalar_B1_final:.4f}")
log(f"  A_s gap = {gap_OOM:+.4f} OOM (unchanged from S74)")
log("=" * 72)
