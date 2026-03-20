#!/usr/bin/env python3
"""
CONST-FREEZE-42: Constants as Frozen Snapshots of Internal Geometry

PRE-REGISTERED GATE:
  PASS: A single M_KK reproduces alpha_EM and G_N within 1 OOM each
  FAIL: M_KK required for alpha and G_N differ by > 3 OOM

Physics:
  In the KK framework on M4 x K (K = SU(3) with Jensen deformation tau):

  1. GRAVITY: Dimensional reduction of the 12D Einstein-Hilbert action gives
     1/(16 pi G_N) = Vol_K * M_KK^2 / (16 pi)
     where Vol_K is the volume of SU(3) in units of R_KK^8.
     Since Jensen is volume-preserving, Vol_K is tau-INDEPENDENT.
     => G_N = 1 / (Vol_K * M_KK^2)      [natural units]

  2. GAUGE COUPLINGS: From KK reduction of the Ricci scalar (Kerner formula):
     1/(4 g_a^2) ~ g_{ab}(tau) * Vol_K
     where g_{ab}(tau) is the metric on su(3) in direction a.
     The metric components ARE the inverse gauge couplings (S23c result).

     For the Jensen deformation:
       g_U1(tau) = g_0 * e^{2tau}   [U(1) direction, index 7]
       g_SU2(tau) = g_0 * e^{-2tau} [SU(2) directions, indices 0-2]
       g_C2(tau) = g_0 * e^{tau}    [C^2 directions, indices 3-6]

     Gauge coupling ratios (convention-independent, Session 17a B-1):
       g_1/g_2 = sqrt(g_SU2/g_U1) = e^{-2tau}

  3. COSMOLOGICAL CONSTANT: From spectral action a_0 term:
     Lambda_4D = (2/pi^2) * a_0 * M_KK^4

  Strategy:
  - Extract M_KK from G_N using Vol_K (tau-independent)
  - Extract absolute gauge coupling using g_{ab}(tau_fold) and Vol_K
  - Check if the SAME M_KK gives both alpha_EM and G_N consistently

  Two approaches computed:
  (A) KK metric approach: g_{ab}(tau) directly gives coupling RATIOS
  (B) Spectral zeta approach: a_2, a_4 sums from S41 (incorrect for couplings,
      shown for comparison and to document the failure mode)

Data:
  tier0-computation/s41_constants_vs_tau.npz
  tier0-computation/s42_tau_dyn_reopening.npz
  tier0-computation/tier1_dirac_spectrum.py (jensen_metric)

Author: Tesla-Resonance (Session 42, W4-2)
"""

import numpy as np
import sys, os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
from tier1_dirac_spectrum import (
    su3_generators, compute_structure_constants, compute_killing_form,
    jensen_metric, U1_IDX, SU2_IDX
)

# ======================================================================
#  Constants
# ======================================================================

DATA_DIR = Path(__file__).parent
PI = np.pi
PI2 = PI**2

# Observed values
ALPHA_EM_OBS = 1.0 / 137.036
from canonical_constants import G_N as G_N_OBS  # m^3 kg^-1 s^-2
from canonical_constants import alpha_em_MZ_inv as ALPHA_EM_MZ_INV  # PDG 2024
from canonical_constants import rho_Lambda_obs as LAMBDA_CC_OBS_GEV4  # GeV^4

# Planck mass
from canonical_constants import M_Pl_reduced as M_PL_REDUCED  # GeV
M_Z = 91.1876                 # GeV

# ======================================================================
#  Load data
# ======================================================================

print("=" * 78)
print("CONST-FREEZE-42: Constants as Frozen Snapshots")
print("=" * 78)

d41 = np.load(DATA_DIR / 's41_constants_vs_tau.npz', allow_pickle=True)
d42 = np.load(DATA_DIR / 's42_tau_dyn_reopening.npz', allow_pickle=True)

tau_values = d41['tau_values']
tau_fold = float(d41['tau_fold'])  # 0.190
fold_idx = np.argmin(np.abs(tau_values - tau_fold))

# S41 spectral zeta sums (for reference, NOT for coupling extraction)
a0_zeta = d41['a0_cutoff0']
a2_zeta = d41['a2_cutoff0']
a4_zeta = d41['a4_cutoff0']

print(f"\nLoaded S41 data: {len(tau_values)} tau values, fold at tau = {tau_fold}")
print(f"Tau dynamics (S42): tau is effectively FROZEN (shortfall {float(d42['shortfall_best']):.0f}x)")

# ======================================================================
#  Step 1: Compute Jensen metric at each tau
# ======================================================================

print(f"\n{'='*78}")
print("STEP 1: JENSEN METRIC g_{ab}(tau)")
print("=" * 78)

gens = su3_generators()
f_abc = compute_structure_constants(gens)
B_ab = compute_killing_form(f_abc)

# Base metric normalization
g0 = jensen_metric(B_ab, 0.0)
g0_diag = g0[0, 0]  # All diagonal elements equal at tau=0
print(f"\nBase metric: g_0 = {g0_diag:.6f} * delta_ab")
print(f"  tr(g_0) = {np.trace(g0):.6f}")

# Volume of SU(3) with this metric.
# For a compact Lie group with bi-invariant metric g_ab = c * delta_ab:
# Vol(G) = integral sqrt(det g) d^n x = sqrt(det g)^{1/2} * Vol_topological
# The topological volume of SU(3) = (4 pi^2 / 3) * (2 pi)^3 = (32 pi^5)/3
# (from the Weyl integration formula for SU(3))
# But det(g) = g0^8 (8 = dim SU(3)), so sqrt(det g) = g0^4
# Vol_metric = g0^4 * Vol_topological
#
# The standard volume of SU(3) with the Killing metric normalized as
# B(X,Y) = -Tr(ad X ad Y) (our convention, B_{11} = -12):
# g_0 = |B_{11}| = 12... wait let me check

print(f"\nKilling form B_ab diagonal = {B_ab[0,0]:.4f}")
print(f"Jensen metric at tau=0: g_{'{'}ab{'}'} = |B_ab| = {g0_diag:.4f} * delta_ab")

# The volume-preserving property means:
# det(g(tau)) / det(g(0)) = L1^1 * L2^3 * L3^4 = e^{2tau} * e^{-6tau} * e^{4tau} = 1
# So Vol_K(tau) = Vol_K(0) for ALL tau. CRUCIAL.

# For our metric convention (g_0 = 3 * delta):
# det(g_0) = 3^8 = 6561
# Vol_K = sqrt(6561) * Vol_topo = 81 * Vol_topo
#
# The topological volume of SU(3):
# Vol_topo(SU(3)) = sqrt(3) * (2pi)^5 / 60
# (Marinov 1980; this is for the standard normalization where vol(S^1)=2pi)
# = sqrt(3) * 32 * pi^5 / 60 = sqrt(3) * 16 * pi^5 / 30
# Numerically: sqrt(3) * (2*pi)^5 / 60 = 1.732 * 961.39 / 60 = 27.72

# For OUR metric (g_0 = 3 * delta_ab):
# The physical radius is R = sqrt(g_0) = sqrt(3) times the unit-radius
# Vol_K(ours) = (sqrt(3))^8 * Vol_topo(unit) = 81 * Vol_topo(unit)
# But we're working in DIMENSIONLESS units where the eigenvalues of D_K
# are in units of 1/R_K. The M_KK scale sets the physical size:
# R_K = 1/M_KK.

# For the KK dimensional reduction, the key formula is:
# 1/(16 pi G_N) = M_KK^{d_K} * V_K / (16 pi)
# where d_K = 8 and V_K = Vol_K / R_K^8 = Vol_K * M_KK^8 / (1)^8
# Hmm, need to be more careful.
#
# The 12D EH action: S_12 = (1/(2 kappa_12^2)) int R_12 dvol_12
# After KK reduction: the 4D piece gives
#   1/(16 pi G_4) = Vol_K / (2 kappa_12^2)
# where kappa_12 is the 12D gravitational coupling.
#
# In natural units with the INTERNAL space having physical volume V_K:
#   G_4 = G_12 / V_K
#   G_12 = l_12^10 (12D Planck length)
#   G_4 = G_12 / V_K = l_12^10 / V_K
#
# The KK mass scale M_KK ~ V_K^{-1/8} (geometric mean radius).
# So V_K ~ M_KK^{-8} and G_4 ~ l_12^10 * M_KK^8 = (M_12_Pl)^{-10} * M_KK^8
#
# Self-consistency: M_4_Pl^2 = M_12_Pl^{10} / M_KK^8
#   => M_KK = (M_12_Pl^{10} / M_4_Pl^2)^{1/8}
# But M_12_Pl is unknown. We need a DIFFERENT relation to pin M_KK.
#
# The CORRECT approach for THIS framework (NCG spectral action):
# The spectral action on M4 x F (Connes) or M4 x K (KK) gives:
#   S_B = f_0 a_4 + f_2 Lambda^2 a_2 + f_4 Lambda^4 a_0
# where a_k are the Seeley-DeWitt coefficients of D^2 on the FULL space.
#
# For the PRODUCT space M4 x K, the a_k decompose as:
#   a_0(M4 x K) = a_0(M4) * a_0(K)   [= dim(spinor_M4) * dim(spinor_K) * Vol_4 * Vol_K]
#   a_2(M4 x K) = a_0(M4)*a_2(K) + a_2(M4)*a_0(K)
#   etc.
#
# The key: a_2(K) involves both the Ricci scalar of K and the
# volume of K. For the Einstein metric on SU(3):
#   a_2(K) = (R_K / 6) * Vol_K * dim(spinor_K)
#
# And the gauge kinetic terms come from the a_4 coefficient of the
# FLUCTUATED Dirac operator D_A, which involves:
#   a_4(D_A^2) contains integral F_mu_nu^2 * Vol_K * ...
#
# The bottom line for the KK approach (S23c):
#   1/g_a^2 = g_{aa}(tau) * Vol_K * [normalization factors]
#   1/(16 pi G_N) = Vol_K * M_KK^{dim_K} / [normalization]
#
# Since Vol_K is tau-independent (volume-preserving Jensen), G_N has
# NO tau-dependence! The gauge couplings DO depend on tau through g_{ab}.
#
# For the SELF-CONSISTENCY test, I need one ADDITIONAL input:
# the overall normalization that relates the dimensionless metric
# components g_{ab}(tau) to physical couplings.
#
# From the Kerner formula (S23c):
#   1/(4 g_eff^2) = Vol_K * g_{ab}(tau) * M_KK^{dim_K-2} / (some numerical factor)
#   1/(16 pi G_N) = Vol_K * M_KK^{dim_K-2} / (same numerical factor)
#
# Taking the ratio:
#   (16 pi G_N) / (4 g_a^2) = 1 / g_{aa}(tau)
#   => g_a^2 = (4 pi G_N) / g_{aa}(tau)
#   => alpha_a = g_a^2/(4 pi) = G_N / g_{aa}(tau)
#   => alpha_a * g_{aa}(tau) = G_N
#   => alpha_a = G_N / g_{aa}(tau) = 1 / (M_Pl^2 * g_{aa}(tau))
#
# This is the KEY FORMULA for the self-consistency test.

# ======================================================================
#  Step 2: KK COUPLING EXTRACTION (correct method)
# ======================================================================

print(f"\n{'='*78}")
print("STEP 2: KK GAUGE COUPLING FROM METRIC (S23c Formula)")
print("=" * 78)

print(f"\nKK coupling formula (from Kerner dimensional reduction):")
print(f"  1/(4 g_a^2) / (1/(16 pi G_N)) = g_{{aa}}(tau)")
print(f"  => alpha_a = g_a^2/(4 pi) = G_N / g_{{aa}}(tau) = 1/(M_Pl^2 * g_{{aa}}(tau))")
print(f"  This is M_KK-INDEPENDENT (ratio of gravity to gauge)")

# Compute metric components at each tau
g_U1_arr = np.zeros(len(tau_values))
g_SU2_arr = np.zeros(len(tau_values))
g_C2_arr = np.zeros(len(tau_values))

for i, tau in enumerate(tau_values):
    g_s = jensen_metric(B_ab, tau)
    g_U1_arr[i] = g_s[7, 7]     # U(1) direction
    g_SU2_arr[i] = g_s[0, 0]    # SU(2) direction
    g_C2_arr[i] = g_s[3, 3]     # C^2 direction

# At the fold:
g_U1_fold = g_U1_arr[fold_idx]
g_SU2_fold = g_SU2_arr[fold_idx]
g_C2_fold = g_C2_arr[fold_idx]

print(f"\nMetric components at fold (tau = {tau_fold}):")
print(f"  g_U1  = g_0 * e^{{2*{tau_fold}}} = {g_U1_fold:.6f}")
print(f"  g_SU2 = g_0 * e^{{-2*{tau_fold}}} = {g_SU2_fold:.6f}")
print(f"  g_C2  = g_0 * e^{{{tau_fold}}} = {g_C2_fold:.6f}")
print(f"  g_0 = {g0_diag:.6f}")

# Coupling ratios (convention-independent):
g1_over_g2 = np.exp(-2.0 * tau_fold)
print(f"\nCoupling ratio (Session 17a B-1, PROVEN):")
print(f"  g_1/g_2 = e^{{-2*tau}} = {g1_over_g2:.6f}")
print(f"  (g_1/g_2)^2 = {g1_over_g2**2:.6f}")

# Weinberg angle at fold:
# sin^2(theta_W) = g'^2/(g'^2 + g^2) = g_1^2/(g_1^2 + g_2^2)
# With g_1/g_2 = e^{-2tau}:
# sin^2(theta_W) = e^{-4tau} / (e^{-4tau} + 1) = 1/(1 + e^{4tau})
sin2_thetaW_fold = 1.0 / (1.0 + np.exp(4.0 * tau_fold))
sin2_thetaW_0 = 0.5  # at tau=0: g_1 = g_2 => sin^2 = 0.5
sin2_thetaW_NCG = 3.0 / 8.0  # NCG boundary = 0.375

print(f"\nWeinberg angle at fold:")
print(f"  sin^2(theta_W)(tau={tau_fold}) = {sin2_thetaW_fold:.6f}")
print(f"  sin^2(theta_W)(tau=0)     = {sin2_thetaW_0:.6f}")
print(f"  NCG prediction (GUT)      = {sin2_thetaW_NCG:.6f}")
print(f"  Observed at m_Z           = 0.23122")

# Now: absolute coupling from alpha_a = 1/(M_Pl^2 * g_{aa}(tau))
# This formula says alpha ~ 1/(M_Pl^2 * g_0) ~ 1/(6e36 * 3) ~ 5.6e-38
# This is ABSURDLY small.
#
# THE PROBLEM: g_{aa} here has dimensions of (length)^2 in KK conventions.
# In our DIMENSIONLESS code, g_0 ~ 3 (from Killing form |B_{11}| = 3).
# The PHYSICAL metric is g_{ab}^{phys} = g_{ab}^{code} * R_K^2 = g_{ab}^{code} / M_KK^2
#
# Correcting: alpha_a = G_N / (g_{aa}^{code} / M_KK^2)
#                      = G_N * M_KK^2 / g_{aa}^{code}
#                      = M_KK^2 / (M_Pl^2 * g_{aa}^{code})

# So we need M_KK. Getting M_KK from G_N requires another formula:
# 1/(16 pi G_N) = Vol_K * M_KK^8 / (16 pi)  [for 8 extra dimensions]
#
# Wait, the precise formula depends on the DIMENSION of the spectral action.
# For M4 x K with dim(K) = 8, the 12D EH action:
#   S_12 = (M_12^{10} / 2) int R_12 d^{12}x
# Reduces to:
#   S_4 = (M_12^{10} * V_K / 2) int R_4 d^4x
# Matching: M_Pl^2 = M_12^{10} * V_K
# With V_K ~ Vol_code * R_K^8 = Vol_code / M_KK^8:
#   M_Pl^2 = M_12^{10} * Vol_code / M_KK^8
#
# This has TWO unknowns: M_12 and M_KK. We need a second equation.
# From the gauge coupling:
#   1/g_a^2 ~ g_{aa}^{code} * V_K * M_12^{10} / ...
#
# Actually the CLEAN way is (S23c):
#   1/(4 g_a^2) = (1/(2 kappa_12^2)) * integral_K g_{aa} dvol_K
#                = (M_12^{10}/2) * g_{aa}^{code} * Vol_code / M_KK^8
#   1/(16 pi G_4) = (M_12^{10}/2) * Vol_code / M_KK^8
#
# Taking ratio:
#   4 g_a^2 * 16 pi G_4 = 1 / g_{aa}^{code}
#   => alpha_a = g_a^2/(4 pi) = 1 / (256 pi^2 G_4 * g_{aa}^{code})
#   => alpha_a = M_Pl^2 / (64 pi * g_{aa}^{code})
#
# Hmm, this gives alpha ~ (6e36) / (64 pi * 3) ~ 1e34. Still wrong.
# The issue is numerical prefactors.
#
# Let me do this more carefully. The Kerner formula for the EH action
# on a principal bundle P -> M4 with structure group G (dim G = n):
#
#   R_P = R_M + R_G - (1/4) g_{ab} F^a F^b
#
# Integrating over the fiber G:
#   int_G dvol_G R_P = Vol_G * R_M + int_G R_G dvol_G - (1/4) int_G g_{ab} F^a F^b dvol_G
#   = Vol_G * R_M + <R_G> * Vol_G - (1/4) g_{ab} Vol_G * F^a F^b
#   (the metric g_{ab} is constant on G for left-invariant metrics)
#
# So the 4D effective action:
#   S_4 = (M_*^{n+2} / 2) integral [Vol_G * R_M - (1/4) Vol_G * g_{ab} F^a F^b + ...] d^4x
#
# Matching:
#   1/(16 pi G_4) = M_*^{n+2} * Vol_G / 2
#   1/(4 g_eff^2) = M_*^{n+2} * Vol_G * g_{ab} / 2
#
# => g_eff^{-2} = g_{ab} / (16 pi G_4)
# => g_eff^2 = 16 pi G_4 / g_{ab}
# => alpha_eff = g_eff^2 / (4 pi) = 4 G_4 / g_{ab}
#                                   = 4 / (M_Pl^2 * g_{ab})

print(f"\n{'='*78}")
print("STEP 2b: ABSOLUTE COUPLING (Kerner formula)")
print("=" * 78)

print(f"\nKerner formula for KK reduction (P -> M4, fiber G):")
print(f"  g_eff^2 = 16 pi G_N / g_{{ab}}")
print(f"  alpha_eff = g_eff^2 / (4 pi) = 4 G_N / g_{{ab}} = 4 / (M_Pl^2 * g_{{ab}})")
print(f"\n  BUT: g_{{ab}} above is the PHYSICAL metric (dimensions of length^2)")
print(f"  Our code g_{{ab}}^{{code}} is dimensionless. Physical: g_{{ab}}^{{phys}} = g_{{ab}}^{{code}} / M_KK^2")
print(f"\n  => alpha_eff = 4 M_KK^2 / (M_Pl^2 * g_{{ab}}^{{code}})")
print(f"  => M_KK^2 = alpha_eff * M_Pl^2 * g_{{ab}}^{{code}} / 4")

# Self-consistency: for EACH gauge sector, solve for M_KK:
# alpha_U1 = 4 M_KK^2 / (M_Pl^2 * g_U1)
# alpha_SU2 = 4 M_KK^2 / (M_Pl^2 * g_SU2)
# alpha_SU3 = 4 M_KK^2 / (M_Pl^2 * g_SU3)
#
# BUT: alpha_U1 and alpha_SU2 are the couplings AT M_KK (unification scale).
# At unification, alpha_1 = alpha_2 = alpha_3 = alpha_GUT ~ 1/40 (approximately).
# More precisely: at M_GUT ~ 2e16 GeV, alpha_s ~ 0.034 (SU(3)), alpha_2 ~ 0.034.
# alpha_1 normalized as (5/3) alpha_Y, with alpha_Y ~ 0.017 at M_GUT.
#
# The Kerner formula gives different coupling for each direction because
# g_{ab}(tau) is NOT proportional to delta_ab for tau != 0. This IS the
# Jensen deformation breaking gauge universality!
#
# At tau = 0 (undeformed): g_ab = g_0 * delta_ab => all couplings equal
# => alpha_unif = 4 M_KK^2 / (M_Pl^2 * g_0)
#
# For tau != 0: the couplings SPLIT. This is the g_1/g_2 = e^{-2tau} result.
# The question is: what is the OVERALL scale?
#
# From G_N (which is tau-independent):
#   M_Pl^2 = M_*^{n+2} * Vol_G
# This determines M_* in terms of M_Pl and Vol_G.
# But Vol_G depends on M_KK and the code-level Vol:
#   Vol_G = Vol_code * R_K^8 = Vol_code / M_KK^8
# And M_*^{10} = M_Pl^2 * M_KK^8 / Vol_code.
#
# For the gauge coupling at tau=0:
#   alpha_unif = 4 M_KK^2 / (M_Pl^2 * g_0)
#
# => M_KK = sqrt(alpha_unif * M_Pl^2 * g_0 / 4)
#         = (M_Pl / 2) * sqrt(alpha_unif * g_0)
#
# With alpha_unif ~ 1/40, g_0 = 3:
#   M_KK = (M_Pl/2) * sqrt(3/40) = (M_Pl/2) * 0.274 = 0.137 * M_Pl
#   = 0.137 * 2.435e18 = 3.3e17 GeV

# At tau_fold:
# alpha_SU2(M_KK) = 4 M_KK^2 / (M_Pl^2 * g_SU2_fold)
# alpha_U1(M_KK) = 4 M_KK^2 / (M_Pl^2 * g_U1_fold)
# These are the couplings of the U(1) and SU(2) gauge fields at M_KK.
# alpha_EM = alpha_U1 * alpha_SU2 / (alpha_U1 + alpha_SU2) [EM = U(1)xSU(2) mixing]

# Actually more standard: alpha_EM = alpha_2 * sin^2(theta_W)
# and sin^2(theta_W) = g_1^2/(g_1^2 + g_2^2) = alpha_1/(alpha_1 + alpha_2)
# with alpha_1/alpha_2 = g_SU2/g_U1 = e^{-4tau}
# (Note: 1/alpha_a ~ g_aa, larger metric = weaker coupling)

# Let me use a concrete approach.
# Fix M_KK by matching alpha_strong (SU(3)) at M_KK ~ M_GUT.
# The SU(3) direction is C^2 (indices 3-6), with g_C2 = g_0 * e^{tau}.
#
# WAIT: SU(3)_c coupling comes from the COLOR sector of the Hilbert space,
# not from the C^2 directions of the Jensen deformation on the INTERNAL SU(3).
# The internal SU(3) IS the gauge group -- its Killing vectors generate gauge
# transformations. The Jensen deformation changes the metric on this gauge group,
# changing the gauge couplings.
#
# There are 8 gauge bosons corresponding to 8 Killing vectors.
# The sub-decomposition su(3) = u(1) + su(2) + C^2 is:
#   u(1) -> U(1)_Y (1 direction, index 7)
#   su(2) -> SU(2)_L (3 directions, indices 0-2)
#   C^2 -> "coset" directions (4 directions, indices 3-6)
#
# In the BAPTISTA KK framework, the SM gauge group is:
#   G_SM = SU(3)_c x SU(2)_L x U(1)_Y
# But SU(3)_c comes from the FIBER (the internal SU(3)), while SU(2)_L x U(1)_Y
# comes from the isometry group decomposition.
#
# Actually no. In the Baptista papers 13-14, the FULL internal space is SU(3),
# and its isometry group IS SU(3). The gauge group from KK is SU(3) itself.
# The decomposition su(3) = u(1) + su(2) + C^2 identifies:
#   u(1) -> U(1)_Y
#   su(2) -> SU(2)_L
#   C^2 -> these are NOT a subalgebra; they correspond to the W+, W-, etc.?
#
# No, the C^2 directions are the off-diagonal generators (lambda_4 through lambda_7).
# They are NOT a Lie subalgebra.
#
# The POINT is: in the undeformed case (tau=0), all 8 generators have the same
# metric coefficient => one unified coupling. At tau != 0, the three sectors
# get different metric coefficients => the coupling SPLITS.
#
# From Baptista Paper 14 (fermion paper), the PHYSICAL identification:
#   U(1)_Y -> lambda_8 direction (index 7), coupling g' = sqrt(3) * e^{-2tau} * g
#   SU(2)_L -> lambda_{1,2,3} directions (indices 0-2), coupling g
#
# The ratio g'/g = sqrt(3) * e^{-2tau} includes a factor of sqrt(3) from the
# U(1) normalization (Baptista eq 2.85/2.88, Paper 14).
#
# So: sin^2(theta_W) = g'^2/(g'^2 + g^2) = 3 e^{-4tau}/(3 e^{-4tau} + 1)
# At tau=0: sin^2 = 3/4 (NOT 3/8!)
# At tau_fold = 0.19: sin^2 = 3 * e^{-0.76} / (3 * e^{-0.76} + 1)

sin2_fold_baptista = 3.0 * np.exp(-4*tau_fold) / (3.0 * np.exp(-4*tau_fold) + 1.0)
sin2_0_baptista = 3.0 / 4.0

print(f"\nBaptista coupling identification (Paper 14 eq 2.85/2.88):")
print(f"  g'/g = sqrt(3) * e^{{-2tau}}")
print(f"  sin^2(theta_W) = 3 e^{{-4tau}} / (3 e^{{-4tau}} + 1)")
print(f"  sin^2(theta_W)(tau=0)         = {sin2_0_baptista:.6f}")
print(f"  sin^2(theta_W)(tau={tau_fold}) = {sin2_fold_baptista:.6f}")
print(f"  Observed at m_Z               = 0.23122")

# The tau that gives sin^2 = 0.23122 at the GUT scale:
# 0.23122 = 3 e^{-4tau} / (3 e^{-4tau} + 1)
# 0.23122 * (3 e^{-4tau} + 1) = 3 e^{-4tau}
# 0.69366 e^{-4tau} + 0.23122 = 3 e^{-4tau}
# 0.23122 = (3 - 0.69366) e^{-4tau} = 2.30634 e^{-4tau}
# e^{-4tau} = 0.23122 / 2.30634 = 0.10025
# -4tau = ln(0.10025) = -2.3003
# tau = 0.5751
#
# But this is the value at M_GUT. RGE running changes sin^2 from ~0.375 at GUT
# to 0.231 at m_Z. So the GUT-scale value is ~0.375, not 0.231.
# For sin^2(GUT) = 0.375:
# 0.375 = 3 e^{-4tau} / (3 e^{-4tau} + 1)
# 0.375 * (3 e^{-4tau} + 1) = 3 e^{-4tau}
# 1.125 e^{-4tau} + 0.375 = 3 e^{-4tau}
# 0.375 = 1.875 e^{-4tau}
# e^{-4tau} = 0.2
# tau = ln(5)/4 = 0.4024
tau_weinberg_GUT = np.log(5.0) / 4.0
sin2_check = 3.0 * np.exp(-4*tau_weinberg_GUT) / (3.0 * np.exp(-4*tau_weinberg_GUT) + 1.0)

print(f"\nTo get sin^2(theta_W) = 3/8 at GUT scale:")
print(f"  Need tau = ln(5)/4 = {tau_weinberg_GUT:.6f}")
print(f"  Check: sin^2 = {sin2_check:.6f}")
print(f"  Our fold: tau_fold = {tau_fold} => sin^2 = {sin2_fold_baptista:.6f}")

# ======================================================================
#  Step 3: M_KK SELF-CONSISTENCY (THE ACTUAL GATE)
# ======================================================================

print(f"\n{'='*78}")
print("STEP 3: M_KK SELF-CONSISTENCY")
print("=" * 78)

# Route A: M_KK from G_N
# -----------------------
# The precise KK formula for n extra dimensions:
# M_Pl^2 = M_*^{2+n} * V_n
# where M_* is the fundamental (higher-D) Planck scale,
# V_n is the physical volume of the internal space.
# M_KK ~ V_n^{-1/n} (geometric mean inverse radius).
# => V_n ~ M_KK^{-n}, so M_Pl^2 = M_*^{2+n} / M_KK^n
#
# We CANNOT extract M_KK from G_N alone without knowing M_*.
# But with the gauge coupling, we get a SECOND equation:
# alpha_GUT = M_KK^2 / (M_Pl^2 * g_0_code)  [from the Kerner formula]
#
# This gives M_KK directly:
# M_KK^2 = alpha_GUT * M_Pl^2 * g_0_code
#
# Actually I need to be more careful with the numerical prefactors.
# The Kerner formula S23c:
#   1/(4 g^2) = (M_*^{10} / 2) * g_code * Vol_code / M_KK^8
#   1/(16 pi G_4) = (M_*^{10} / 2) * Vol_code / M_KK^8
#
# Ratio: (16 pi G_4) * (1/(4 g^2)) = g_code
# => g^2 = 64 pi G_4 / (4 g_code) = 16 pi G_4 / g_code
# => alpha = g^2/(4 pi) = 4 G_4 / g_code = 4 / (M_Pl^2 * g_code)
#
# BUT this g_code is the PHYSICAL metric in Planck units? NO.
# g_code is dimensionless (our convention). The physical metric is
# g_phys = g_code * L_K^2 where L_K = 1/M_KK.
#
# Let me redo from the 12D action.
# S_12 = (1/(2 kappa_12^2)) int R_{12} sqrt{g_{12}} d^12x
#
# KK ansatz: g_{12} = g_{4}(x) + g_K(y, tau) / M_KK^2
# (internal coordinates y dimensionless, physical metric = g_K/M_KK^2)
#
# After integration over K (using Vol_K^{physical} = Vol_K^{code} / M_KK^8):
# S_4 = (Vol_K^{code} / (2 kappa_12^2 M_KK^8)) int [R_4 + ...] sqrt{g_4} d^4x
#
# Matching: 1/(16 pi G_4) = Vol_K^{code} / (2 kappa_12^2 * M_KK^8)
#
# For gauge terms, from the F^2 term in the Kerner formula:
# (1/4) g_{ab}(tau) F^a F^b integrated over K:
# S_gauge = (Vol_K^{code} / (2 kappa_12^2 * M_KK^8)) * (1/4) * (g_{ab,code}/M_KK^2) int F^a F^b sqrt{g_4} d^4x
#
# => 1/(4 g_4^2) = Vol_K^{code} * g_{ab,code} / (2 kappa_12^2 * M_KK^{10})
#
# Ratio with gravity:
# (1/(4 g_4^2)) / (1/(16 pi G_4)) = g_{ab,code} / M_KK^2
# => g_4^2 = 16 pi G_4 * M_KK^2 / (4 * g_{ab,code})
#          = 4 pi G_4 * M_KK^2 / g_{ab,code}
# => alpha_4 = g_4^2/(4 pi) = G_4 * M_KK^2 / g_{ab,code}
#            = M_KK^2 / (M_Pl^2 * g_{ab,code})

print(f"\nCORRECT Kerner coupling formula:")
print(f"  alpha_a(M_KK) = M_KK^2 / (M_Pl^2 * g_{{aa}}^{{code}})")
print(f"  G_N involves M_* which cancels in the ratio.")
print(f"\n  Solving for M_KK from alpha_a:")
print(f"  M_KK^2 = alpha_a(M_KK) * M_Pl^2 * g_{{aa}}^{{code}}")

# At unification (tau = 0): all g_aa = g_0 = 3.0
# alpha_unif(M_GUT) ~ 1/40 (standard GUT)
alpha_GUT = 1.0 / 40.0  # approximate

M_KK_from_alpha_sq = alpha_GUT * M_PL_REDUCED**2 * g0_diag
M_KK_from_alpha_0 = np.sqrt(M_KK_from_alpha_sq)

print(f"\n--- APPROACH A: M_KK from alpha_GUT at tau=0 ---")
print(f"  alpha_GUT = {alpha_GUT:.4f}")
print(f"  g_0 = {g0_diag:.4f}")
print(f"  M_KK^2 = alpha_GUT * M_Pl^2 * g_0 = {M_KK_from_alpha_sq:.4e} GeV^2")
print(f"  M_KK = {M_KK_from_alpha_0:.4e} GeV")
print(f"  M_KK / M_Pl = {M_KK_from_alpha_0 / M_PL_REDUCED:.4f}")

# At fold (tau = 0.19): use SU(2) coupling as reference
# alpha_2(M_KK) = M_KK^2 / (M_Pl^2 * g_SU2_fold)
# At M_GUT: alpha_2 ~ 1/30 (from running)
alpha_2_GUT = 1.0 / 30.0  # approximate at GUT

M_KK_from_alpha2_fold_sq = alpha_2_GUT * M_PL_REDUCED**2 * g_SU2_fold
M_KK_from_alpha2_fold = np.sqrt(M_KK_from_alpha2_fold_sq)

print(f"\n--- APPROACH B: M_KK from alpha_2 at tau_fold ---")
print(f"  alpha_2(M_GUT) ~ {alpha_2_GUT:.4f}")
print(f"  g_SU2(fold) = {g_SU2_fold:.6f}")
print(f"  M_KK = {M_KK_from_alpha2_fold:.4e} GeV")

# CHECK: alpha_1 from same M_KK
alpha_1_check = M_KK_from_alpha2_fold**2 / (M_PL_REDUCED**2 * g_U1_fold)
print(f"\n  Cross-check alpha_1 = M_KK^2 / (M_Pl^2 * g_U1) = {alpha_1_check:.6f}")
print(f"  Ratio alpha_1/alpha_2 = {alpha_1_check/alpha_2_GUT:.6f}")
print(f"  Expected: g_SU2/g_U1 = e^{{-4*{tau_fold}}} = {np.exp(-4*tau_fold):.6f}")
print(f"  CHECK: {alpha_1_check/alpha_2_GUT:.6f} vs {np.exp(-4*tau_fold):.6f} => CONSISTENT")

# EM coupling:
# 1/alpha_EM = 1/alpha_1 + 1/alpha_2 (at unification scale)
# Actually: alpha_EM = alpha_1 * alpha_2 / (alpha_1 + alpha_2) * (something)
# More precisely: alpha_EM = alpha_2 * sin^2(theta_W)
alpha_EM_at_MKK = alpha_2_GUT * sin2_fold_baptista
print(f"\n  alpha_EM(M_KK) = alpha_2 * sin^2(theta_W) = {alpha_EM_at_MKK:.6f}")
print(f"  1/alpha_EM(M_KK) = {1.0/alpha_EM_at_MKK:.2f}")

# --- NOW: the self-consistency test ---
# The question is whether M_KK from gauge coupling is consistent with
# M_KK from gravity. But G_N gives M_Pl^2, and the Kerner formula gives
# alpha = M_KK^2 / (M_Pl^2 * g_code). So M_KK is DERIVED from alpha + M_Pl.
# There is no independent M_KK from G_N in the Kerner formula!
# G_N (or M_Pl) is an INPUT, not a prediction.
#
# The REAL self-consistency test is different:
# Given M_KK (from any source), do BOTH alpha_EM AND G_N come out right?
# alpha_EM = M_KK^2 / (M_Pl^2 * f(g_code, tau))
# This is one equation with one unknown (M_KK). Given M_Pl, it fixes M_KK.
# Then G_N = 1/M_Pl^2 is just the input. No tension possible.
#
# The gate question REALLY is: does a SINGLE M_KK give BOTH:
#   (a) the correct gauge coupling ratios (sin^2 theta_W)
#   (b) a reasonable overall coupling scale (alpha_GUT ~ 1/40)
#   (c) G_N through the 12D gravitational coupling
#
# (a) and (b) determine M_KK and M_*. (c) then determines Vol_K.
# Self-consistency: Vol_K must be POSITIVE and FINITE.

# From (a)+(b): M_KK^2 = alpha_GUT * M_Pl^2 * g_0 (at tau=0)
# From (c): M_Pl^2 = M_*^{10} * Vol_code / M_KK^8
# => M_*^{10} = M_Pl^2 * M_KK^8 / Vol_code

# Volume of SU(3) in our units:
# Vol(SU(3)) = sqrt(3) * (4 pi^2)^3 / 12 (standard, unit Killing metric)
# For our Killing form B_{11} = -3, g_0 = 3:
# Vol_code = 3^4 * Vol_unit = 81 * sqrt(3) * (4*pi^2)^3 / 12
Vol_SU3_unit = np.sqrt(3) * (4*PI2)**3 / 12  # standard (unit Killing) ~ 1041
Vol_code = g0_diag**4 * Vol_SU3_unit  # our convention (g_0 = 3)

print(f"\n{'='*78}")
print("STEP 3b: VOLUME AND HIGHER-D PLANCK MASS")
print("=" * 78)
print(f"\n  Vol(SU(3))_unit = sqrt(3) * (4 pi^2)^3 / 12 = {Vol_SU3_unit:.2f}")
print(f"  Vol_code = g_0^4 * Vol_unit = {g0_diag}^4 * {Vol_SU3_unit:.2f} = {Vol_code:.2f}")

# M_*^{10} = M_Pl^2 * M_KK^8 / Vol_code
M_KK_use = M_KK_from_alpha_0  # from alpha_GUT at tau=0
M_star_10 = M_PL_REDUCED**2 * M_KK_use**8 / Vol_code
M_star = M_star_10**0.1
print(f"\n  Using M_KK = {M_KK_use:.4e} GeV:")
print(f"  M_*^10 = M_Pl^2 * M_KK^8 / Vol_code = {M_star_10:.4e} GeV^10")
print(f"  M_* = {M_star:.4e} GeV")
print(f"  M_* / M_KK = {M_star/M_KK_use:.4f}")
print(f"  M_* / M_Pl = {M_star/M_PL_REDUCED:.4f}")

# Physical volume: V_phys = Vol_code / M_KK^8
V_phys = Vol_code / M_KK_use**8
R_KK = V_phys**(1.0/8.0)

print(f"\n  Physical volume = Vol_code / M_KK^8 = {V_phys:.4e} GeV^-8")
print(f"  = {V_phys:.4e} GeV^-8 = ({V_phys**(1/8):.4e})^8 GeV^-8")
print(f"  R_KK = V_phys^(1/8) = {R_KK:.4e} GeV^-1")
print(f"  1/R_KK = {1.0/R_KK:.4e} GeV = M_KK^eff")
print(f"  Check: should be ~ M_KK = {M_KK_use:.4e} GeV")
print(f"  Ratio: {(1.0/R_KK)/M_KK_use:.4f}")

# The ratio is not exactly 1 because Vol_code is not (2pi)^8.
# But the order of magnitude should match.

# ======================================================================
#  Step 4: THE GATE -- M_KK consistency
# ======================================================================

print(f"\n{'='*78}")
print("STEP 4: GATE EVALUATION")
print("=" * 78)

# The gate asks: does a single M_KK reproduce alpha_EM and G_N within 1 OOM?
#
# In the Kerner KK framework:
#   alpha_a = M_KK^2 / (M_Pl^2 * g_aa)
#   G_N = 1/M_Pl^2 (INPUT, not a prediction from M_KK alone)
#
# G_N by itself does NOT determine M_KK. It determines M_Pl.
# M_KK is determined by matching a gauge coupling.
#
# So the gate is really: does the M_KK from gauge coupling matching
# give a REASONABLE M_* (above the electroweak scale, below Planck)?
# And: are the coupling RATIOS consistent with observation?
#
# Let me reformulate the gate as the task intended:
#
# APPROACH 1: Use spectral action a_2 to get M_KK from G_N.
#   1/G_N ~ a_2 * M_KK^2 => M_KK ~ M_Pl * sqrt(1/a_2)
#   (This is what S41 computed, with a_2 = spectral zeta sum)
#
# APPROACH 2: Use spectral action a_4 to get alpha_EM.
#   alpha ~ a_4 (dimensionless, no M_KK needed)
#   Then use a_4 + alpha_obs to extract M_KK
#
# The S41 spectral zeta sums are:
#   a_2 = sum mult * |lambda|^{-2} = 2776 (at fold)
#   a_4 = sum mult * |lambda|^{-4} = 1351 (at fold)
#
# For the heat-kernel expansion, the PROPER Seeley-DeWitt a_2 coefficient
# on a d-dimensional compact Riemannian manifold is:
#   a_2^{SD}(D^2) = (4 pi)^{-d/2} * (1/6) * int R dvol
#
# For SU(3) (d=8) with bi-invariant metric, R = 3 (Ricci scalar in our normalization):
#   a_2^{SD} = (4 pi)^{-4} * (1/6) * 3 * Vol = (4pi)^{-4} * Vol / 2
#
# The spectral zeta sum zeta(1) = sum |lambda|^{-2} * mult is related to
# a_2^{SD} but with additional normalization involving (4pi)^{d/2}.
#
# The S41 values ALREADY include multiplicity correctly, but they are
# the RAW spectral sums, not the (4pi)^{-d/2}-normalized SD coefficients.
# For coupling extraction, what matters is which formula we use.
#
# Let me just use the S41 approach as intended by the task:
#   1/G_N = c_G * a_2 * M_KK^2  (some normalization c_G)
#   1/alpha = c_alpha * a_4       (some normalization c_alpha)
# And ask: for WHAT c_G and c_alpha is this self-consistent?
#
# The task says:
#   1/G_N = (96/pi^2) f_2 a_2 M_KK^2
#   1/g^2 = f_4 a_4  (NOT divided by pi^2 -- different convention)
#
# Let me use the task's normalization directly.

# Task normalization:
# Lambda = (2/pi^2) f_0 a_0 M_KK^4
# 1/G_N = (96/pi^2) f_2 a_2 M_KK^2
# 1/g^2 = f_4 a_4  (spectral action convention)

f0, f2, f4 = 1.0, 1.0, 1.0

# From 1/G_N:
# M_Pl^2 = (96/pi^2) * a_2 * M_KK^2  (since 1/G_N = M_Pl^2 in natural units / (8 pi))
# Actually: 1/G_N in natural units = M_Pl^2 (for REDUCED Planck mass, where G = 1/(8 pi M_Pl^2))
# Careful: the CCM formula gives 1/kappa^2 = (96 f_2 Lambda^2 - f_0 c)/(24 pi^2)
# with kappa^2 = 16 pi G_N. So:
# 1/(16 pi G_N) = (96 f_2 Lambda^2)/(24 pi^2) [dropping Yukawa term for M_KK extraction]
#               = 4 f_2 Lambda^2 / pi^2
# => G_N = pi^2 / (64 pi f_2 Lambda^2) = pi / (64 f_2 Lambda^2)
# => Lambda^2 = pi / (64 f_2 G_N)
#
# BUT: Lambda here is the NCG cutoff, NOT M_KK. In the NCG framework,
# Lambda plays the role of M_KK (the highest KK mode scale).
#
# If we identify Lambda = M_KK:
# M_KK^2 = pi / (64 G_N) = pi * M_Pl^2 * 8 pi / 64 = pi^2 M_Pl^2 / 8
# => M_KK = (pi / (2 sqrt(2))) * M_Pl
#
# This is TOO LARGE -- it gives M_KK ~ M_Pl, whereas we need M_KK ~ M_GUT < M_Pl.
#
# The resolution: the formula includes a_2 (internal space contribution).
# The S41 a_2 is the INTERNAL SPACE spectral sum, not the 4D term.
# In the PRODUCT geometry M4 x K:
#   a_2(M4 x K) = a_0(K) * a_2(M4) + a_0(M4) * a_2(K)
# For flat M4: a_2(M4) = 0, so a_2(M4 x K) = a_0(M4) * a_2(K)
# where a_0(M4) = dim(spinor_4D) * Vol(M4) / (4pi)^2 = 4 * Vol(M4) / (4pi)^2
#
# The task prescription:
#   1/G_N = (96/pi^2) * a_2^K * M_KK^2
# This uses a_2^K directly (the internal coefficient) with M_KK^2 providing dimensions.

print(f"\nTask prescription (CCM normalization):")
print(f"  1/G_N = (96/pi^2) * f_2 * a_2^K * M_KK^2")
print(f"  1/g^2 = f_4 * a_4^K")
print(f"  Lambda_cc = (2/pi^2) * f_0 * a_0^K * M_KK^4")

# Route A: M_KK from G_N
# 1/G_N = (96/pi^2) * a_2 * M_KK^2
# M_Pl^2 * 8 pi = (96/pi^2) * a_2 * M_KK^2  [since G_N = 1/(8 pi M_Pl^2)]
# Wait: G_N = 1/(8 pi M_Pl^2) (reduced) or G_N = 1/M_Pl^2 (non-reduced)?
# Using REDUCED: G_N = 1/(8 pi M_Pl_red^2), so 1/G_N = 8 pi M_Pl_red^2
# => 8 pi M_Pl_red^2 = (96/pi^2) a_2 M_KK^2
# => M_KK^2 = 8 pi^3 M_Pl_red^2 / (96 a_2) = pi^3 M_Pl_red^2 / (12 a_2)

a2_fold_val = a2_zeta[fold_idx]
M_KK_from_GN_sq = PI**3 * M_PL_REDUCED**2 / (12.0 * a2_fold_val)
M_KK_from_GN = np.sqrt(M_KK_from_GN_sq)

print(f"\n--- Route A: M_KK from G_N ---")
print(f"  M_KK^2 = pi^3 * M_Pl^2 / (12 * a_2)")
print(f"  a_2 = {a2_fold_val:.4f}")
print(f"  M_KK = {M_KK_from_GN:.4e} GeV")
print(f"  M_KK / M_Pl = {M_KK_from_GN / M_PL_REDUCED:.6f}")
log10_MKK_GN = np.log10(M_KK_from_GN)

# Route B: M_KK from alpha_EM
# 1/g^2 = a_4^K (at M_KK). This is the UNIFIED coupling.
# alpha_unif = g^2/(4 pi) = 1/(4 pi a_4)
alpha_unif_from_a4 = 1.0 / (4.0 * PI * a4_zeta[fold_idx])
g2_unif = 1.0 / a4_zeta[fold_idx]

# EM coupling at M_KK: alpha_EM(M_KK) = alpha_unif * sin^2(theta_W)
# Use the Baptista Weinberg angle at fold:
alpha_EM_MKK = alpha_unif_from_a4 * sin2_fold_baptista
alpha_EM_MKK_inv = 1.0 / alpha_EM_MKK

print(f"\n--- Route B: alpha_EM from spectral zeta ---")
print(f"  1/g^2 = a_4 = {a4_zeta[fold_idx]:.4f}")
print(f"  alpha_unif = 1/(4 pi a_4) = {alpha_unif_from_a4:.6e}")
print(f"  sin^2(theta_W) at fold = {sin2_fold_baptista:.6f}")
print(f"  alpha_EM(M_KK) = {alpha_EM_MKK:.6e}")
print(f"  1/alpha_EM(M_KK) = {alpha_EM_MKK_inv:.2f}")

# Running to m_Z:
# 1/alpha_EM(m_Z) = 1/alpha_EM(M_KK) + b * ln(M_KK/m_Z)
# b ~ 2.06 (empirical, increasing going down in energy)
# If M_KK = M_KK_from_GN ~ 1.7e17 GeV:
b_run = 2.06
if M_KK_from_GN > M_Z:
    delta_alpha_inv = b_run * np.log(M_KK_from_GN / M_Z)
else:
    delta_alpha_inv = 0
alpha_EM_mZ_predicted_inv = alpha_EM_MKK_inv + delta_alpha_inv

print(f"\n  Running from M_KK to m_Z:")
print(f"  Delta(1/alpha_EM) = {b_run} * ln({M_KK_from_GN:.2e}/{M_Z}) = {delta_alpha_inv:.2f}")
print(f"  1/alpha_EM(m_Z) predicted = {alpha_EM_MKK_inv:.2f} + {delta_alpha_inv:.2f} = {alpha_EM_mZ_predicted_inv:.2f}")
print(f"  1/alpha_EM(m_Z) observed  = {ALPHA_EM_MZ_INV:.3f}")

# The spectral zeta approach gives alpha too SMALL (1/alpha too LARGE).
# 1/alpha_EM(M_KK) = 1/(alpha_unif * sin^2) = 4 pi a_4 / sin^2
# = 4 pi * 1351 / 0.552 = 30,720

# Alternative: what M_KK would be needed from alpha alone?
# Need alpha_EM(m_Z) = 1/128 after running.
# alpha_EM(M_KK) = alpha_unif * sin^2
# 1/alpha_EM(m_Z) = 1/alpha_EM(M_KK) + b * ln(M_KK/m_Z) = 128
# 1/alpha_EM(M_KK) = 128 - b * ln(M_KK/m_Z)
# Also: alpha_unif = 1/(4 pi a_4)
# alpha_EM(M_KK) = sin^2 / (4 pi a_4)
# 1/alpha_EM(M_KK) = 4 pi a_4 / sin^2 = 30,720 (way too large)
#
# This means: the spectral zeta sum a_4 = 1351 is WAY too large.
# The correct a_4^{gauge} (from representation traces, CCM) should be ~ 1-10.
# The spectral zeta sum counts ALL modes with 1/lambda^4 weighting,
# which is dominated by the many low-lying modes.
#
# DIAGNOSIS: S41's a_4 = spectral zeta function zeta_{D_K}(2), NOT the
# Seeley-DeWitt a_4. These are different objects. The SD a_4 is a local
# geometric invariant (curvature integrals). The zeta function is global.
# For coupling extraction, the CCM paper uses the SD a_4 (which comes from
# REPRESENTATION TRACES over H_F, not from the KK spectrum).

print(f"\n{'='*78}")
print("DIAGNOSTIC: WHY THE SPECTRAL ZETA SUM GIVES WRONG alpha")
print("=" * 78)
print(f"\n  S41 computes: a_4 = Sum_n mult_n * |lambda_n|^{{-4}} = {a4_zeta[fold_idx]:.2f}")
print(f"  This is the spectral ZETA FUNCTION zeta_{{D_K}}(2), a global spectral invariant.")
print(f"")
print(f"  The CCM gauge coupling uses the Seeley-DeWitt a_4^{{SD}} coefficient,")
print(f"  which is a LOCAL GEOMETRIC invariant (curvature integrals over K).")
print(f"  For an Einstein space, a_4^{{SD}} involves Riem^2, Ric^2, R^2 integrals.")
print(f"")
print(f"  These are DIFFERENT QUANTITIES related by Mellin transform.")
print(f"  The zeta sum has a_4^{{zeta}} ~ 1351 (sum over many KK modes).")
print(f"  The SD coefficient a_4^{{SD}} for gauge coupling is O(1) (rep traces).")
print(f"  Ratio: a_4^{{zeta}} / a_4^{{SD}} ~ 1000 (three orders of magnitude).")
print(f"")
print(f"  CONCLUSION: S41's spectral zeta sums CANNOT be directly used for")
print(f"  coupling extraction. They encode the KK tower structure, not the")
print(f"  zero-mode gauge couplings. The Kerner metric approach (Step 2) is correct.")

# ======================================================================
#  Step 5: CORRECT GATE EVALUATION (Kerner approach)
# ======================================================================

print(f"\n{'='*78}")
print("STEP 5: GATE EVALUATION (Kerner metric approach)")
print("=" * 78)

# From the Kerner formula:
# alpha_a = M_KK^2 / (M_Pl^2 * g_aa^code)
# This has ONE unknown: M_KK.
# G_N = 1/(8 pi M_Pl^2) is an INPUT (M_Pl is observed).
#
# Solving for M_KK from alpha_EM:
# alpha_EM(m_Z) = 1/128 (observed)
# alpha_EM(M_KK) = alpha_EM(m_Z) - Delta_alpha_running
#
# For SU(2): alpha_2(M_KK) = M_KK^2 / (M_Pl^2 * g_SU2_fold)
# Running: 1/alpha_2(m_Z) ~ 30 (observed)
# 1/alpha_2(M_KK) ~ 1/alpha_2(m_Z) - b_2*ln(M_KK/m_Z) ~ 30 - 0.53*ln(M_KK/m_Z)
# (b_2 for SU(2): 1-loop: b_2 = (22 - 4*3 - 1/3)/6 ~ 19/6 ~ 3.17, but
#  d(1/alpha_2)/d(ln mu) = b_2/(2pi) ~ 0.50)

# Let me just solve self-consistently.
# Target: alpha_2(m_Z) = 1/29.587 (PDG)
# RGE: 1/alpha_2(mu) = 1/alpha_2(m_Z) + (b_2/(2pi)) * ln(mu/m_Z)
# With b_2 = 19/6 (SM one-loop), but d(1/alpha)/dln(mu) < 0 for asymptotically free.
# Actually: d(alpha_2^{-1})/d(ln mu) = -b_2/(2pi) for SU(2).
# SU(2) is asymptotically free: b_2 = (22/3 - 4*3/3 - 1/6) = 22/3 - 4 - 1/6 = 19/6 (yes, b>0 => AF)
# Hmm, SU(2) with N_f=3 families: b_2 = 11 - 2/3*6 - 1/6 = 11 - 4 - 0.167 ~ 6.83
# No: b_2 = (11*C_A - 2*N_f*T_f)/(3) for the first coefficient
# SU(2): C_A = 2, fermion reps: 6 doublets per generation * 3 gen = 18? No.
# Let me just use known numbers.
# At 1-loop: d(1/alpha_i)/d(ln mu) = -b_i/(2pi)
# b_1 = -(41/10), b_2 = 19/6, b_3 = 7 (SM, MS-bar)
# Sign: alpha_2 decreases at higher energy (AF). So 1/alpha_2 INCREASES at higher mu.
# Going from m_Z up: 1/alpha_2(mu) = 1/alpha_2(m_Z) + (19/6)/(2pi) * ln(mu/m_Z)
#                                   = 29.587 + 0.505 * ln(mu/m_Z)

b2_SM = 19.0 / 6.0  # SU(2) one-loop beta coefficient
# d(1/alpha_2)/d(ln mu) = b2/(2 pi) = 0.505

# At M_KK: 1/alpha_2(M_KK) = 29.587 + (b2/(2pi)) * ln(M_KK/m_Z)
# Also: 1/alpha_2(M_KK) = M_Pl^2 * g_SU2_fold / M_KK^2
# => M_Pl^2 * g_SU2_fold / M_KK^2 = 29.587 + 0.505 * ln(M_KK/m_Z)

# Solve iteratively
def solve_MKK_from_alpha2(g_code, M_Pl, m_Z, alpha2_mZ_inv, b2, tol=1e-6, max_iter=100):
    """Solve M_KK self-consistently from SU(2) coupling."""
    # Initial guess: ignore running
    MKK = np.sqrt(M_Pl**2 * g_code / alpha2_mZ_inv)

    for i in range(max_iter):
        alpha2_MKK_inv = alpha2_mZ_inv + (b2 / (2*PI)) * np.log(MKK / m_Z)
        MKK_new = np.sqrt(M_Pl**2 * g_code / alpha2_MKK_inv)
        if abs(MKK_new - MKK) / MKK < tol:
            return MKK_new, alpha2_MKK_inv
        MKK = MKK_new
    return MKK, alpha2_MKK_inv

alpha2_mZ_inv = 29.587  # PDG

M_KK_kerner, alpha2_MKK_inv = solve_MKK_from_alpha2(
    g_SU2_fold, M_PL_REDUCED, M_Z, alpha2_mZ_inv, b2_SM
)

print(f"\nSelf-consistent M_KK from SU(2) coupling (Kerner):")
print(f"  g_SU2(fold) = {g_SU2_fold:.6f}")
print(f"  1/alpha_2(m_Z) = {alpha2_mZ_inv}")
print(f"  b_2 = {b2_SM:.4f}")
print(f"  M_KK = {M_KK_kerner:.4e} GeV")
print(f"  1/alpha_2(M_KK) = {alpha2_MKK_inv:.4f}")
print(f"  alpha_2(M_KK) = {1.0/alpha2_MKK_inv:.6f}")
log10_MKK_kerner = np.log10(M_KK_kerner)

# Cross-check: alpha_1 at M_KK
alpha1_MKK = M_KK_kerner**2 / (M_PL_REDUCED**2 * g_U1_fold)
print(f"\n  Cross-check:")
print(f"  alpha_1(M_KK) = M_KK^2 / (M_Pl^2 * g_U1) = {alpha1_MKK:.6f}")
print(f"  1/alpha_1(M_KK) = {1.0/alpha1_MKK:.4f}")

# What 1/alpha_1 should be from running:
# b_1 = -41/10 (U(1)_Y increases at high energy, NOT AF)
# d(1/alpha_1)/d(ln mu) = b_1/(2 pi) = -0.653
# Going up from m_Z: 1/alpha_1 DECREASES
b1_SM = -41.0 / 10.0
alpha1_mZ_inv = 59.0  # PDG (GUT normalization: alpha_1 = (5/3) alpha_Y)
alpha1_MKK_inv_from_running = alpha1_mZ_inv + (b1_SM / (2*PI)) * np.log(M_KK_kerner / M_Z)

print(f"  From RGE: 1/alpha_1(M_KK) = {alpha1_mZ_inv} + ({b1_SM/(2*PI):.3f})*ln({M_KK_kerner:.2e}/{M_Z})")
print(f"            = {alpha1_MKK_inv_from_running:.4f}")
print(f"  From Kerner: 1/alpha_1(M_KK) = {1.0/alpha1_MKK:.4f}")
print(f"  RATIO: {(1.0/alpha1_MKK) / alpha1_MKK_inv_from_running:.4f}")

# EM coupling at M_KK and m_Z
alpha_EM_kerner = 1.0 / (1.0/alpha1_MKK + alpha2_MKK_inv)
# Actually: 1/alpha_EM = 1/alpha_1 + 1/alpha_2 is NOT right.
# alpha_EM^{-1} = (alpha_1 + alpha_2)/(alpha_1 * alpha_2 * sin^2 * cos^2 ...)
# Simpler: at any scale, 1/alpha_EM = (1/alpha_1 + 1/alpha_2) * correction
# Actually the exact relation is:
# e = g sin(theta_W) = g' cos(theta_W)
# alpha_EM = alpha_2 * sin^2(theta_W) = alpha_1 * cos^2(theta_W) [GUT normalized alpha_1]
# Hmm, depends on normalization.
# Standard: 1/alpha_EM = (3/5)/alpha_1 + 1/alpha_2 (with GUT-normalized alpha_1)
# = alpha_1^{-1}*(3/5) + alpha_2^{-1}
# = 59*(3/5) + 29.587 = 35.4 + 29.587 = 64.987 (at m_Z)
# 1/alpha_EM(m_Z) = 128 ish. So: 1/alpha_EM = (3/5)/alpha_1 + 1/alpha_2 is wrong.

# The correct formula: alpha_EM = alpha_2 * sin^2(theta_W)
# With sin^2(theta_W) = alpha_1/(alpha_1 + alpha_2) [at given scale]
# => alpha_EM = alpha_1 * alpha_2 / (alpha_1 + alpha_2)
# => 1/alpha_EM = (alpha_1 + alpha_2)/(alpha_1 * alpha_2) = 1/alpha_1 + 1/alpha_2
#
# But alpha_1 here is in the GUT normalization? No, alpha_1 = g_Y^2/(4pi) with
# the GUT normalization g_1 = sqrt(5/3) g_Y.
#
# OK let me just use: 1/alpha_EM = 1/alpha_1_GUT * (5/3) + 1/alpha_2
# => 1/alpha_EM = (5/3) * 59 + 29.587 = 98.33 + 29.587 = 127.9. YES.
#
# At M_KK:

alpha_EM_MKK_kerner_inv = (5.0/3.0) * (1.0/alpha1_MKK) + alpha2_MKK_inv
alpha_EM_mZ_kerner_inv = (5.0/3.0) * alpha1_mZ_inv + alpha2_mZ_inv

print(f"\n  EM coupling (Kerner):")
print(f"  1/alpha_EM = (5/3)/alpha_1 + 1/alpha_2")
print(f"  At M_KK: 1/alpha_EM = (5/3)*{1.0/alpha1_MKK:.4f} + {alpha2_MKK_inv:.4f} = {alpha_EM_MKK_kerner_inv:.4f}")
print(f"  At m_Z : 1/alpha_EM = (5/3)*{alpha1_mZ_inv:.1f} + {alpha2_mZ_inv:.3f} = {alpha_EM_mZ_kerner_inv:.4f}")
print(f"  Observed 1/alpha_EM(m_Z) = {ALPHA_EM_MZ_INV:.3f}")

# ======================================================================
#  Step 6: FINAL GATE
# ======================================================================

print(f"\n{'='*78}")
print("STEP 6: FINAL GATE EVALUATION")
print("=" * 78)

# Route A: M_KK from G_N via spectral zeta (task prescription)
# This gave M_KK(G_N) = M_KK_from_GN from the a_2 spectral zeta sum

# Route B: M_KK from alpha_EM via Kerner metric
# This gave M_KK(alpha_2) = M_KK_kerner from the Jensen metric

print(f"\n  M_KK (from G_N, spectral zeta a_2)  = {M_KK_from_GN:.4e} GeV  (log10 = {log10_MKK_GN:.2f})")
print(f"  M_KK (from alpha_2, Kerner metric)  = {M_KK_kerner:.4e} GeV  (log10 = {log10_MKK_kerner:.2f})")

OOM_diff = abs(log10_MKK_GN - log10_MKK_kerner)
print(f"  |Delta log10(M_KK)| = {OOM_diff:.2f}")

if OOM_diff < 1.0:
    gate_verdict = "PASS"
    gate_reason = f"|Delta log10(M_KK)| = {OOM_diff:.2f} < 1 OOM"
elif OOM_diff > 3.0:
    gate_verdict = "FAIL"
    gate_reason = f"|Delta log10(M_KK)| = {OOM_diff:.2f} > 3 OOM"
else:
    gate_verdict = "MARGINAL"
    gate_reason = f"|Delta log10(M_KK)| = {OOM_diff:.2f} (between 1 and 3 OOM)"

print(f"\n  GATE: CONST-FREEZE-42")
print(f"  VERDICT: {gate_verdict}")
print(f"  Reason: {gate_reason}")

# ======================================================================
#  Step 7: LITHIUM-7
# ======================================================================

print(f"\n{'='*78}")
print("STEP 7: LITHIUM-7")
print("=" * 78)

# The Li-7 problem: BBN predicts Li-7/H ~ 5.2e-10, observed ~ 1.6e-10
# Sensitivity: d ln(Li-7/H) / d ln(alpha) ~ -8 (Coc et al. 2007)
# To resolve: need delta_alpha/alpha ~ +0.15

# In this framework:
# alpha depends on tau through g_{ab}(tau).
# alpha_2(tau) = M_KK^2 / (M_Pl^2 * g_SU2(tau)) = M_KK^2 / (M_Pl^2 * g_0 * e^{-2tau})
# So alpha_2(tau) propto e^{2tau} (increases with tau).
# alpha_EM(tau) = alpha_2(tau) * sin^2(theta_W(tau))
# sin^2 = 3 e^{-4tau} / (3 e^{-4tau} + 1)
# d(alpha_EM)/dtau is complicated.

# At BBN (z ~ 10^9, T ~ 1 MeV):
# Tau is FROZEN at tau_fold (W2-2: transit too fast, finished long before BBN)
# => alpha at BBN = alpha at fold = alpha today
# => NO resolution of Li-7 problem

# HOWEVER: during the transit (tau: 0 -> 0.19), alpha changes by:
alpha_ratio_transit = g_SU2_arr[0] / g_SU2_fold  # alpha propto 1/g_SU2, so ratio is flipped
# Actually alpha propto e^{2tau}, so alpha(0.19)/alpha(0) = e^{2*0.19}/e^0 = e^{0.38} = 1.462
alpha_change = np.exp(2.0 * tau_fold)  # alpha grows by this factor during transit
delta_alpha_over_alpha = alpha_change - 1.0

print(f"\nDuring transit (tau: 0 -> {tau_fold}):")
print(f"  alpha_2 propto e^{{2tau}}")
print(f"  alpha_2(fold) / alpha_2(0) = e^{{2*{tau_fold}}} = {alpha_change:.4f}")
print(f"  delta_alpha/alpha = {delta_alpha_over_alpha:.4f} = {delta_alpha_over_alpha*100:.2f}%")
print(f"  (alpha was ~{delta_alpha_over_alpha*100:.0f}% SMALLER before transit)")
print(f"\n  Li-7 needs: delta_alpha/alpha ~ +15% at BBN relative to today")
print(f"  Framework gives: alpha at BBN = alpha today (tau frozen)")
print(f"  VERDICT: Li-7 NOT RESOLVED")

# Full alpha_EM variation vs tau:
alpha_EM_vs_tau = np.zeros(len(tau_values))
for i, tau in enumerate(tau_values):
    s2 = 3.0 * np.exp(-4*tau) / (3.0 * np.exp(-4*tau) + 1.0)
    # alpha_EM propto (1/g_SU2) * sin^2 propto e^{2tau} * sin^2(tau)
    # Normalize to fold value:
    alpha_EM_vs_tau[i] = (g_SU2_fold / g_SU2_arr[i]) * (s2 / sin2_fold_baptista)

print(f"\nalpha_EM(tau) / alpha_EM(fold):")
print(f"  {'tau':>6s}  {'ratio':>10s}  {'delta%':>10s}")
for i, tau in enumerate(tau_values):
    print(f"  {tau:6.3f}  {alpha_EM_vs_tau[i]:10.6f}  {(alpha_EM_vs_tau[i]-1)*100:+10.4f}%")

# ======================================================================
#  Step 8: COSMOLOGICAL CONSTANT
# ======================================================================

print(f"\n{'='*78}")
print("STEP 8: COSMOLOGICAL CONSTANT")
print("=" * 78)

# Lambda_4D = (2/pi^2) * a_0 * M_KK^4
# a_0 = 6440, M_KK ~ few * 10^17 GeV
M_KK_best = M_KK_kerner  # use the Kerner result
rho_Lambda = (2.0 / PI2) * a0_zeta[fold_idx] * M_KK_best**4
CC_ratio = rho_Lambda / LAMBDA_CC_OBS_GEV4

print(f"\n  rho_Lambda^spectral = (2/pi^2) * {a0_zeta[fold_idx]:.0f} * ({M_KK_best:.2e})^4")
print(f"  = {rho_Lambda:.4e} GeV^4")
print(f"  rho_Lambda^observed = {LAMBDA_CC_OBS_GEV4:.2e} GeV^4")
print(f"  RATIO = {CC_ratio:.4e} (~ 10^{np.log10(CC_ratio):.0f})")
print(f"  Standard CC problem. NOT resolved.")

# ======================================================================
#  Step 9: DERIVATIVE TABLE (running rates at fold)
# ======================================================================

print(f"\n{'='*78}")
print("STEP 9: RUNNING RATES (d/dtau at fold)")
print("=" * 78)

# From Jensen metric:
# g_U1(tau) = g_0 * e^{2tau}, so d(g_U1)/dtau = 2 g_U1
# g_SU2(tau) = g_0 * e^{-2tau}, so d(g_SU2)/dtau = -2 g_SU2
# alpha_2 propto 1/g_SU2, so d(alpha_2)/dtau = 2 alpha_2
# => d ln(alpha_2)/dtau = +2 (EXACT)

print(f"\nExact analytic results (from Jensen metric):")
print(f"  d ln(g_U1)/dtau  = +2  (U(1) direction stiffens)")
print(f"  d ln(g_SU2)/dtau = -2  (SU(2) direction softens)")
print(f"  d ln(g_C2)/dtau  = +1  (coset direction, intermediate)")
print(f"  d ln(alpha_2)/dtau = +2 (coupling INCREASES with tau)")
print(f"  d ln(alpha_1)/dtau = -2 (coupling DECREASES with tau)")
print(f"  d ln(G_N)/dtau     = 0  (ZERO: Vol_K constant, no tau dep)")

# For alpha_EM:
# d ln(alpha_EM)/dtau at fold:
# alpha_EM = alpha_2 * sin^2(theta_W)
# sin^2 = 3 e^{-4tau} / (3 e^{-4tau} + 1) ≡ f(tau)
# d ln(sin^2)/dtau = d(sin^2)/dtau / sin^2
# d(sin^2)/dtau = 3 * (-4) e^{-4tau} / (3 e^{-4tau} + 1) - 3 e^{-4tau} * 3 * (-4) e^{-4tau} / (3 e^{-4tau} + 1)^2
# = -12 e^{-4tau} / (3 e^{-4tau} + 1) + 36 e^{-8tau} / (3 e^{-4tau} + 1)^2
# = -12 e^{-4tau} (3 e^{-4tau} + 1 - 3 e^{-4tau}) / (3 e^{-4tau} + 1)^2
# = -12 e^{-4tau} / (3 e^{-4tau} + 1)^2
# d ln(sin^2)/dtau = [-12 e^{-4tau} / (3 e^{-4tau} + 1)^2] / [3 e^{-4tau} / (3 e^{-4tau} + 1)]
# = -4 / (3 e^{-4tau} + 1)

dln_sin2_dtau_fold = -4.0 / (3.0 * np.exp(-4*tau_fold) + 1.0)
dln_alphaEM_dtau_fold = 2.0 + dln_sin2_dtau_fold

print(f"\n  d ln(sin^2(theta_W))/dtau at fold = {dln_sin2_dtau_fold:.6f}")
print(f"  d ln(alpha_EM)/dtau = d ln(alpha_2)/dtau + d ln(sin^2)/dtau")
print(f"  = 2 + ({dln_sin2_dtau_fold:.6f}) = {dln_alphaEM_dtau_fold:.6f}")

# Compare with clock constraint (Session 22d E-3):
# dalpha/alpha = -3.08 * dtau
clock_coeff = float(d41['clock_coeff'])
print(f"\n  Clock constraint (Session 22d E-3): dalpha/alpha = {clock_coeff} * dtau")
print(f"  Our Kerner result:                  dalpha_EM/alpha_EM = {dln_alphaEM_dtau_fold:.4f} * dtau")
print(f"  Discrepancy: Kerner gives {dln_alphaEM_dtau_fold:.2f}, clock gives {clock_coeff}")
print(f"  Note: clock constraint was derived from full Dirac spectrum running,")
print(f"  not from the KK metric. Different observables.")

# Webb bound:
# |dalpha/alpha| < 1e-5 at z ~ 2-4
# => |dtau| < 1e-5 / |dln_alpha/dtau| ~ 1e-5 / 0.33 ~ 3e-5
# Tau frozen => bound automatically satisfied

print(f"\n  Webb bound |dalpha/alpha| < 1e-5 => |dtau| < {1e-5/abs(dln_alphaEM_dtau_fold):.2e}")
print(f"  Tau frozen post-transit => AUTOMATICALLY SATISFIED")

# ======================================================================
#  SUMMARY
# ======================================================================

print(f"\n{'='*78}")
print("SUMMARY TABLE")
print("=" * 78)

print(f"\n| Quantity | At fold (tau={tau_fold}) | Observed | Status |")
print(f"|:---------|:----------------------|:---------|:-------|")
print(f"| sin^2(theta_W) at M_KK | {sin2_fold_baptista:.4f} | ~0.375 (GUT) | {sin2_fold_baptista:.4f} vs 0.375 |")
print(f"| 1/alpha_2 at M_KK | {alpha2_MKK_inv:.1f} | ~44 (GUT) | Kerner |")
print(f"| M_KK (Kerner, alpha_2) | {M_KK_kerner:.2e} GeV | — | log10={log10_MKK_kerner:.2f} |")
print(f"| M_KK (spectral zeta, G_N) | {M_KK_from_GN:.2e} GeV | — | log10={log10_MKK_GN:.2f} |")
print(f"| |Delta log10(M_KK)| | {OOM_diff:.2f} | <1 PASS, >3 FAIL | **{gate_verdict}** |")
print(f"| CC (rho_Lambda) | {rho_Lambda:.2e} GeV^4 | {LAMBDA_CC_OBS_GEV4:.2e} | 10^{np.log10(CC_ratio):.0f} discrepancy |")
print(f"| Li-7 | tau frozen | needs +15% | NOT RESOLVED |")
print(f"| d ln(alpha_EM)/dtau | {dln_alphaEM_dtau_fold:.4f} | — | Exact (Jensen) |")
print(f"| d ln(G_N)/dtau | 0 (exact) | <1e-12/yr | Auto-satisfied |")

print(f"\n{'='*78}")
print(f"GATE: CONST-FREEZE-42")
print(f"VERDICT: {gate_verdict}")
print(f"REASON: {gate_reason}")
print(f"{'='*78}")

# ======================================================================
# SAVE
# ======================================================================

save_dict = {
    'tau_values': tau_values,
    'tau_fold': tau_fold,
    'fold_idx': fold_idx,
    # Jensen metric
    'g_U1': g_U1_arr,
    'g_SU2': g_SU2_arr,
    'g_C2': g_C2_arr,
    'g_U1_fold': g_U1_fold,
    'g_SU2_fold': g_SU2_fold,
    'g_C2_fold': g_C2_fold,
    'g0_diag': g0_diag,
    # Spectral zeta sums (for reference)
    'a0_fold': a0_zeta[fold_idx],
    'a2_fold': a2_zeta[fold_idx],
    'a4_fold': a4_zeta[fold_idx],
    # Coupling predictions
    'sin2_thetaW_fold': sin2_fold_baptista,
    'alpha2_MKK_inv': alpha2_MKK_inv,
    'alpha_EM_MKK_inv_kerner': alpha_EM_MKK_kerner_inv,
    # M_KK
    'M_KK_kerner': M_KK_kerner,
    'M_KK_from_GN': M_KK_from_GN,
    'log10_MKK_kerner': log10_MKK_kerner,
    'log10_MKK_GN': log10_MKK_GN,
    'OOM_diff': OOM_diff,
    # Running rates
    'dln_alphaEM_dtau': dln_alphaEM_dtau_fold,
    'dln_GN_dtau': 0.0,
    'clock_coeff': clock_coeff,
    # alpha_EM vs tau (normalized to fold)
    'alpha_EM_vs_tau_normalized': alpha_EM_vs_tau,
    # CC
    'rho_Lambda_spectral': rho_Lambda,
    'CC_ratio': CC_ratio,
    # Gate
    'gate_verdict': np.array([gate_verdict]),
    'gate_name': np.array(['CONST-FREEZE-42']),
}

np.savez(DATA_DIR / 's42_constants_snapshot.npz', **save_dict)
print(f"\nSaved: {DATA_DIR / 's42_constants_snapshot.npz'}")

# ======================================================================
# PLOTTING
# ======================================================================

fig, axes = plt.subplots(2, 3, figsize=(18, 10))
fig.suptitle('CONST-FREEZE-42: Constants as Frozen Snapshots',
             fontsize=14, fontweight='bold')

# Panel 1: Jensen metric components vs tau
ax = axes[0, 0]
ax.plot(tau_values, g_U1_arr, 'r^-', ms=4, label=r'$g_{U(1)} = g_0 e^{2\tau}$')
ax.plot(tau_values, g_SU2_arr, 'bs-', ms=4, label=r'$g_{SU(2)} = g_0 e^{-2\tau}$')
ax.plot(tau_values, g_C2_arr, 'gD-', ms=4, label=r'$g_{C^2} = g_0 e^{\tau}$')
ax.axvline(tau_fold, color='gray', ls='--', alpha=0.5)
ax.axhline(g0_diag, color='gray', ls=':', alpha=0.3)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$g_{aa}(\tau)$')
ax.legend(fontsize=8)
ax.set_title('Jensen metric components')

# Panel 2: sin^2(theta_W) vs tau
ax = axes[0, 1]
sin2_vs_tau = 3.0 * np.exp(-4*tau_values) / (3.0 * np.exp(-4*tau_values) + 1.0)
ax.plot(tau_values, sin2_vs_tau, 'ko-', ms=4)
ax.axvline(tau_fold, color='gray', ls='--', alpha=0.5)
ax.axhline(0.375, color='blue', ls=':', alpha=0.5, label='NCG (3/8)')
ax.axhline(0.231, color='red', ls=':', alpha=0.5, label='Observed (m_Z)')
ax.axhline(sin2_fold_baptista, color='green', ls=':', alpha=0.5,
           label=f'fold: {sin2_fold_baptista:.4f}')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$\sin^2(\theta_W)$ at $M_{KK}$')
ax.legend(fontsize=8)
ax.set_title('Weinberg angle vs deformation')

# Panel 3: alpha_EM(tau)/alpha_EM(fold) vs tau
ax = axes[0, 2]
ax.plot(tau_values, alpha_EM_vs_tau, 'ko-', ms=4)
ax.axvline(tau_fold, color='gray', ls='--', alpha=0.5)
ax.axhline(1.0, color='gray', ls='-', alpha=0.3)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$\alpha_{EM}(\tau) / \alpha_{EM}(\tau_{fold})$')
ax.set_title(r'$\alpha_{EM}$ running with deformation')

# Panel 4: M_KK comparison (bar chart)
ax = axes[1, 0]
bars = ax.bar(['Kerner\n(alpha_2)', 'Spectral zeta\n(G_N)'],
              [log10_MKK_kerner, log10_MKK_GN],
              color=['steelblue', 'firebrick'], edgecolor='k', alpha=0.8)
ax.set_ylabel(r'$\log_{10}(M_{KK}$ / GeV)')
ax.set_title(f'M_KK self-consistency: {gate_verdict}')
ax.text(0.5, 0.95, f'|$\\Delta$| = {OOM_diff:.2f} OOM',
        transform=ax.transAxes, ha='center', va='top', fontsize=12,
        fontweight='bold', color='green' if OOM_diff < 1 else ('orange' if OOM_diff < 3 else 'red'))

# Panel 5: Spectral zeta sums (a_2, a_4) -- for context
ax = axes[1, 1]
ax.plot(tau_values, a2_zeta, 'b^-', ms=4, label=r'$a_2 = \sum \lambda^{-2}$')
ax2 = ax.twinx()
ax2.plot(tau_values, a4_zeta, 'rs-', ms=4, label=r'$a_4 = \sum \lambda^{-4}$')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$a_2$', color='b')
ax2.set_ylabel(r'$a_4$', color='r')
ax.tick_params(axis='y', labelcolor='b')
ax2.tick_params(axis='y', labelcolor='r')
lines1, labels1 = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax.legend(lines1 + lines2, labels1 + labels2, fontsize=8, loc='upper right')
ax.axvline(tau_fold, color='gray', ls='--', alpha=0.5)
ax.set_title('Spectral zeta sums (S41)')

# Panel 6: Summary text
ax = axes[1, 2]
ax.axis('off')
summary_text = (
    f"CONST-FREEZE-42 Results\n"
    f"{'='*40}\n\n"
    f"Fold: tau = {tau_fold}\n\n"
    f"Jensen metric at fold:\n"
    f"  g_U1 = {g_U1_fold:.4f}, g_SU2 = {g_SU2_fold:.4f}\n"
    f"  sin^2(theta_W) = {sin2_fold_baptista:.4f}\n\n"
    f"M_KK (Kerner, alpha_2) = {M_KK_kerner:.2e}\n"
    f"M_KK (zeta, G_N)       = {M_KK_from_GN:.2e}\n"
    f"|Delta log10| = {OOM_diff:.2f} OOM\n\n"
    f"d ln(alpha_EM)/dtau = {dln_alphaEM_dtau_fold:.4f}\n"
    f"d ln(G_N)/dtau = 0 (exact)\n\n"
    f"CC: 10^{np.log10(CC_ratio):.0f} discrepancy\n"
    f"Li-7: NOT RESOLVED\n\n"
    f"GATE: {gate_verdict}\n"
    f"({gate_reason})"
)
ax.text(0.05, 0.95, summary_text, transform=ax.transAxes,
        fontsize=9, verticalalignment='top', fontfamily='monospace',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

plt.tight_layout()
plt.savefig(DATA_DIR / 's42_constants_snapshot.png', dpi=150, bbox_inches='tight')
print(f"Saved: {DATA_DIR / 's42_constants_snapshot.png'}")

print(f"\n{'='*78}")
print(f"CONST-FREEZE-42 COMPLETE")
print(f"GATE VERDICT: {gate_verdict}")
print(f"{'='*78}")
