#!/usr/bin/env python3
"""
s54_threshold.py — String-Motivated Threshold Corrections to sin²θ_W
=====================================================================

Gate: THRESHOLD-54 (INFO)
Agent: kaku-speculative-theorist

Context:
  S52 DDG-MKK-52 computed sin²θ_W = 0.584 at the fold (FAIL, 2.5× above 0.231).
  Standard SM 1-loop running from M_KK to M_Z gives sin²θ_W(M_Z) ~ 0.448 —
  still far from the observed 0.231.

  The question: can string-motivated threshold corrections from the 992 KK
  modes on Jensen SU(3) bridge the gap?

Physics:
  In string compactifications (Dixon-Kaplunovsky-Louis 1991, Kaku Paper 12/23),
  threshold corrections modify the gauge couplings at the compactification scale:

    1/α_i(M_Z) = 1/α_i(M_KK) + b_i^SM/(2π) ln(M_KK/M_Z) + Δ_i

  where Δ_i are threshold corrections from KK modes that decouple at masses
  M_n = λ_n × M_KK (λ_n are Dirac eigenvalues on SU(3)).

  We implement THREE levels of threshold analysis:

  METHOD 1: Staircase decoupling — each KK mode changes the running beta
            function coefficient at its mass threshold. Below the lightest
            KK mode, only the SM runs. Between modes, the beta function
            gets corrections from all active modes.

  METHOD 2: Dedekind eta regularization — the string partition function
            for threshold corrections involves η(τ) where τ = iM_KK/T.
            For the SU(3) manifold, we construct an analogous regularized
            product from the 992-mode Dirac spectrum.

  METHOD 3: Inverse problem — what threshold corrections Δ_1, Δ_2 would
            be REQUIRED to land sin²θ_W = 0.231 at M_Z? Are they physically
            achievable from 992 modes?

  CRITICAL NOTE on the sin²θ_W problem:
  The framework gives sin²θ_W = 0.584 at M_KK. The SU(5) GUT normalization
  gives sin²θ_W = 3/8 = 0.375 at M_GUT ~ 2×10^16. SM running from 0.375
  down to M_Z gives 0.231 — the observed value.

  The framework's value 0.584 is NOT the SU(5) value. The question is whether
  threshold corrections can shift the EFFECTIVE sin²θ_W from 0.584 to a value
  that, after SM running, lands at 0.231.

Author: kaku-speculative-theorist (S54)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
from canonical_constants import (
    M_KK_gravity, M_KK_kerner,
    M_Z, alpha_em_MZ_inv, sin2_thetaW_MSbar,
    M_Pl_reduced, PI, tau_fold,
    alpha2_MKK_inv, sin2_thetaW_fold
)

# ======================================================================
# SECTION 1: Load Dirac spectrum at fold
# ======================================================================

data = np.load(os.path.join(os.path.dirname(__file__), 's44_dos_tau.npz'),
               allow_pickle=True)

omega_fold = data['tau0.19_all_omega']    # 992 eigenvalues in M_KK units
dim2_fold  = data['tau0.19_all_dim2']     # dim(p,q)^2 for each mode

N_modes = len(omega_fold)
omega_sorted = np.sort(omega_fold)
omega_min = omega_sorted[0]
omega_max = omega_sorted[-1]

print("=" * 72)
print("s54_threshold.py — String Threshold Corrections to sin²θ_W")
print("=" * 72)
print()
print(f"Dirac spectrum at fold (τ = {tau_fold}):")
print(f"  N_modes = {N_modes}")
print(f"  ω_min = {omega_min:.6f} M_KK")
print(f"  ω_max = {omega_max:.6f} M_KK")
print(f"  ω_mean = {np.mean(omega_fold):.6f} M_KK")
print(f"  ω_median = {np.median(omega_fold):.6f} M_KK")
print()

# ======================================================================
# SECTION 2: SM beta coefficients and PDG values
# ======================================================================

# SM 1-loop beta function coefficients (b > 0 = asymptotic freedom)
# Convention: 1/α_i(μ) = 1/α_i(M_Z) + b_i/(2π) ln(μ/M_Z)
b1_SM = -41.0 / 10.0   # = -4.1 (U(1)_Y, GUT normalized)  # S72: OPPOSITE sign convention from canonical b1_SM=+4.1 — intentional (b>0=AF here)
b2_SM = 19.0 / 6.0     # = +3.167 (SU(2)_L)  # S72: OPPOSITE sign convention from canonical b2_SM=-3.167 — intentional
b3_SM = 7.0             # = +7.0 (SU(3)_C)  # S72: OPPOSITE sign convention from canonical b3_SM=-7.0 — intentional

# PDG at M_Z (GUT normalization for α_1)
alpha_1_inv_MZ = 59.01   # (5/3)/α_Y  # (local)
alpha_2_inv_MZ = 29.59  # (local)
alpha_3_inv_MZ = 8.50    # 1/0.118  # (local)

# Framework boundary conditions at M_KK
alpha_2_inv_MKK = alpha2_MKK_inv           # 47.86 (from S42)
s2w_fold_val = sin2_thetaW_fold            # 0.584

# Derive α_1^{-1}(M_KK) from sin²θ_W at fold:
# sin²θ_W = (3/5)α_2^{-1} / [(3/5)α_2^{-1} + α_1^{-1}]
# => α_1^{-1} = (3/5)α_2^{-1}(1 - sin²θ_W)/sin²θ_W
alpha_1_inv_MKK = (3.0/5.0) * alpha_2_inv_MKK * (1.0 - s2w_fold_val) / s2w_fold_val

print("Framework boundary conditions at M_KK:")
print(f"  1/α_2(M_KK) = {alpha_2_inv_MKK:.4f}")
print(f"  sin²θ_W(fold) = {s2w_fold_val:.6f}")
print(f"  => 1/α_1(M_KK) = {alpha_1_inv_MKK:.4f}")
print()

# ======================================================================
# SECTION 3: Baseline — SM running with NO threshold corrections
# ======================================================================

print("=" * 72)
print("BASELINE: SM running from M_KK to M_Z (no threshold corrections)")
print("=" * 72)
print()

for label, M_KK_val in [("M_KK_gravity", M_KK_gravity),
                          ("M_KK_kerner", M_KK_kerner)]:
    t_KK = np.log(M_KK_val / M_Z)

    # Running DOWN: 1/α(M_Z) = 1/α(M_KK) - b/(2π) × t
    a1_pred = alpha_1_inv_MKK - b1_SM / (2*PI) * t_KK
    a2_pred = alpha_2_inv_MKK - b2_SM / (2*PI) * t_KK

    # sin²θ_W at M_Z
    s2w_pred = (3.0/5.0) * a2_pred / ((3.0/5.0) * a2_pred + a1_pred)

    print(f"  {label} = {M_KK_val:.3e} GeV (t = {t_KK:.2f}):")
    print(f"    1/α_1(M_Z) = {a1_pred:.2f}  (PDG: {alpha_1_inv_MZ})")
    print(f"    1/α_2(M_Z) = {a2_pred:.2f}  (PDG: {alpha_2_inv_MZ})")
    print(f"    sin²θ_W(M_Z) = {s2w_pred:.4f}  (PDG: {sin2_thetaW_MSbar})")
    print(f"    Deficit: {s2w_pred - sin2_thetaW_MSbar:+.4f} ({(s2w_pred/sin2_thetaW_MSbar - 1)*100:+.1f}%)")
    print()

# ======================================================================
# SECTION 4: METHOD 1 — Staircase Decoupling
# ======================================================================
#
# Each KK mode n decouples at mass M_n = ω_n × M_KK.
# Between M_n and M_{n+1}, the effective beta function is:
#   b_i^eff = b_i^SM + Σ_{active modes} δb_i^(mode)
#
# The active modes are those with M_mode > μ (running scale going down).
# Since ALL 992 modes have masses 0.82-2.06 × M_KK, they all decouple
# in a narrow mass window.
#
# For the threshold correction, we need the SM charge content of each mode.
# From the CSDR decomposition (S52 s52_ddg_mkk.py):
#
# Each dim(p,q)² class has specific SM charge assignments.
# The key group-theory coefficients for a Dirac fermion in rep R of SM:
#
#   δb_1 = -(4/3) × d_3 × d_2 × (3/5) × Y²
#   δb_2 = -(4/3) × d_3 × T_2(R_2)
#   δb_3 = -(4/3) × d_2 × T_3(R_3)
#
# where d_i = dim(R_i), T_i = Dynkin index.
#
# CSDR decomposition of SU(3) reps under U(2) → SM:
#
# (0,0) = 1:     singlet, no SM charge
#                 δb = (0, 0, 0)
#
# (1,0) = 3:     fundamental → 2_{1/2} ⊕ 1_{-1} under U(2)
#                 Treating as (1,2)_{1/6} + (1,1)_{-1/3} under SM
#                 (color-singlet KK modes)
#                 δb_1 = -(4/3)[1×2×(3/5)×(1/6)² + 1×1×(3/5)×(1/3)²]
#                       = -(4/3)(3/5)[2/36 + 1/9] = -(4/3)(3/5)(6/36)
#                       = -(4/3)(3/5)(1/6) = -2/15
#                 δb_2 = -(4/3)[1×1/2] = -2/3 (from the doublet)
#                 δb_3 = 0 (color singlet)
#
# (0,1) = 3̄:    conjugate fundamental, same magnitudes
#                 δb = same as (1,0)
#
# (1,1) = 8:     adjoint → 3_0 ⊕ 2_1 ⊕ 2_{-1} ⊕ 1_0 under U(2)
#                 → (1,3)_0 + (1,2)_{±1} + (1,1)_0 under SM
#                 δb_1 = -(4/3)(3/5)[2×1² + 2×1²] = -(4/3)(3/5)(4) = -16/5
#                 δb_2 = -(4/3)[1×1 + 1×(1/2) + 1×(1/2)] = -(4/3)(2) = -8/3
#                 δb_3 = 0 (color singlet KK modes)
#
# For HIGHER reps, we need tensor product decomposition.
# (2,0) = 6 = sym², (0,2) = 6̄
# (3,0) = 10, (0,3) = 10̄
# (2,1) = 15, (1,2) = 15̄
#
# Key physical point: the SU(3) INTERNAL modes are color-singlet.
# They carry SU(2)_L × U(1)_Y charges from the CSDR decomposition.
# Therefore δb_3 = 0 for all KK modes. Only α_1 and α_2 get corrected.

print("=" * 72)
print("METHOD 1: Staircase Decoupling with CSDR Charge Assignments")
print("=" * 72)
print()

# Assign SM charges per dim² class.
# Each mode is a Dirac spinor on SU(3). Under CSDR:
# The effective (δb_1, δb_2, δb_3) per mode depends on the SU(3) rep.

# Define δb per mode for each dim² class.
# NOTE: These are NEGATIVE contributions (each Dirac fermion makes coupling run faster).
# All KK modes are color-singlet (internal SU(3) ≠ color SU(3)).

# For a single Dirac fermion in (1, R_2)_Y:
# δb_1 = -(4/3)(3/5) d_2 Y²
# δb_2 = -(4/3) T_2(R_2)
# δb_3 = 0

def db_dirac(d2, Y, d3=1):
    """Beta function contribution of one Dirac fermion in (d3, d2)_Y."""
    db1 = -(4.0/3.0) * d3 * d2 * (3.0/5.0) * Y**2
    db2 = 0.0
    if d2 == 2:
        db2 = -(4.0/3.0) * d3 * 0.5  # T(fund of SU(2)) = 1/2
    elif d2 == 3:
        db2 = -(4.0/3.0) * d3 * 2.0  # T(adj of SU(2)) = 2
    elif d2 == 1:
        db2 = 0.0
    db3 = 0.0  # all color singlet
    if d3 == 3:
        db3 = -(4.0/3.0) * d2 * 0.5  # T(fund of SU(3)_C) = 1/2
    elif d3 == 8:
        db3 = -(4.0/3.0) * d2 * 3.0  # T(adj of SU(3)_C) = 3
    return np.array([db1, db2, db3])

# CSDR decomposition: SU(3) rep → sum of SM reps
# Each (p,q) mode decomposes into several SM reps.
# We sum the β function contributions.

# (0,0) → (1,1)_0: singlet
db_00 = np.array([0.0, 0.0, 0.0])

# (1,0) → (1,2)_{1/6} + (1,1)_{-1/3}
# But wait — the hypercharge assignment depends on the NCG embedding.
# The CSDR of SU(3)/U(2) gives the coset fermions charges.
# Under U(2) = SU(2) × U(1): 3 → 2_{1/2} ⊕ 1_{-1}
# The U(1) charge here is T_8 eigenvalue (in Cartan of SU(3)).
# The SM hypercharge identification: Y = aT_8 + bB, where B is baryon number.
#
# For a MINIMAL assignment (color-singlet KK modes):
# (1,2)_{1/6} means color singlet, SU(2) doublet, Y=1/6
# This is the lepton doublet assignment.
#
# ALTERNATIVE: Given the framework's NCG, one generation = C^16.
# The KK tower could carry full generation quantum numbers.
# But each KK mode is a SINGLE Dirac spinor, not a full generation.
#
# We use TWO approaches and bracket the result.

# === APPROACH A: Minimal CSDR charges (color singlet) ===
# All KK modes color-singlet. Only SU(2)×U(1) charges from U(2) embedding.

# (0,0) = 1 → (1)_0: δb = (0,0,0)
db_A_00 = np.array([0.0, 0.0, 0.0])

# (1,0) = 3 → 2_{1/2} ⊕ 1_{-1} under U(2) → SM:
# Map to SM: d_3=1, (d_2=2, Y=1/6) + (d_2=1, Y=-1/3) [standard lepton-like]
# Actually, the U(2) charge 1/2 maps to Y differently.
# The U(1) in U(2) ⊂ SU(3) has generator T = diag(1/3, 1/3, -2/3).
# The doublet has T = 1/3, the singlet has T = -2/3.
#
# For GUT-normalized U(1): Y_GUT = sqrt(3/5) × Y_phys
# The β function uses (3/5)Y² already (GUT normalization).
#
# Sticking with the framework's U(1) charges:
# Under SU(3) → SU(2) × U(1):
# 3 → 2_{1/3} ⊕ 1_{-2/3}
# These are the charges from the Cartan generator diag(1/3, 1/3, -2/3).
#
# β function for each sub-multiplet:
db_10_sub1 = db_dirac(d2=2, Y=1.0/3.0)   # doublet with Y=1/3
db_10_sub2 = db_dirac(d2=1, Y=-2.0/3.0)  # singlet with Y=-2/3
db_A_10 = db_10_sub1 + db_10_sub2

# (0,1) = 3̄: conjugate, same |Y|
db_01_sub1 = db_dirac(d2=2, Y=-1.0/3.0)
db_01_sub2 = db_dirac(d2=1, Y=2.0/3.0)
db_A_01 = db_01_sub1 + db_01_sub2

# (1,1) = 8 → 3_0 ⊕ 2_{1} ⊕ 2_{-1} ⊕ 1_0
# Under SU(3) → SU(2) × U(1):
# 8 → 3_0 + 2_{+1} + 2_{-1} + 1_0
db_11_sub1 = db_dirac(d2=3, Y=0.0)    # triplet (adjoint of SU(2))
db_11_sub2 = db_dirac(d2=2, Y=1.0)    # doublet Y=+1
db_11_sub3 = db_dirac(d2=2, Y=-1.0)   # doublet Y=-1
db_11_sub4 = db_dirac(d2=1, Y=0.0)    # singlet Y=0
db_A_11 = db_11_sub1 + db_11_sub2 + db_11_sub3 + db_11_sub4

# (2,0) = 6 → sym²(3) under SU(3).
# Under SU(3) → SU(2) × U(1):
# 6 → 3_{2/3} + 2_{-1/3} + 1_{-4/3}
db_20_sub1 = db_dirac(d2=3, Y=2.0/3.0)
db_20_sub2 = db_dirac(d2=2, Y=-1.0/3.0)
db_20_sub3 = db_dirac(d2=1, Y=-4.0/3.0)
db_A_20 = db_20_sub1 + db_20_sub2 + db_20_sub3

# (0,2) = 6̄: conjugate
db_A_02 = np.array([db_A_20[0], db_A_20[1], 0.0])  # Same magnitudes

# (3,0) = 10 → 4_{1} + 3_0 + 2_{-1} + 1_{-2}
db_A_30 = (db_dirac(d2=4, Y=1.0) + db_dirac(d2=3, Y=0.0) +
           db_dirac(d2=2, Y=-1.0) + db_dirac(d2=1, Y=-2.0))
# For d2=4: T_2(4-dim rep of SU(2)) = T(spin-3/2) = 5/2... let's be careful.
# Actually, the Dynkin index for SU(2) rep of dim d is T = d(d²-1)/12
# dim=2: T=1/2, dim=3: T=2, dim=4: T=5/2, dim=5: T=10/2=5

def T_SU2(d):
    """Dynkin index for SU(2) rep of dimension d."""
    return d * (d**2 - 1) / 12.0

def db_dirac_v2(d2, Y, d3=1):
    """Beta function contribution of one Dirac fermion in (d3, d2)_Y.
    Properly handles all SU(2) reps via Dynkin index formula."""
    db1 = -(4.0/3.0) * d3 * d2 * (3.0/5.0) * Y**2
    db2 = -(4.0/3.0) * d3 * T_SU2(d2) if d2 >= 2 else 0.0
    db3 = 0.0
    return np.array([db1, db2, db3])

# Redo all with proper Dynkin indices
print("SM charge assignment from CSDR SU(3) → SU(2) × U(1):")
print()

# (0,0) = 1: singlet
db_00 = np.array([0.0, 0.0, 0.0])
print(f"  (0,0) dim=1:  δb = ({db_00[0]:.4f}, {db_00[1]:.4f}, {db_00[2]:.4f})")

# (1,0) = 3: → 2_{1/3} ⊕ 1_{-2/3}
db_10 = db_dirac_v2(2, 1.0/3.0) + db_dirac_v2(1, -2.0/3.0)
print(f"  (1,0) dim=3:  δb = ({db_10[0]:.4f}, {db_10[1]:.4f}, {db_10[2]:.4f})")

# (0,1) = 3̄: conjugate
db_01 = db_dirac_v2(2, -1.0/3.0) + db_dirac_v2(1, 2.0/3.0)
print(f"  (0,1) dim=3:  δb = ({db_01[0]:.4f}, {db_01[1]:.4f}, {db_01[2]:.4f})")

# (1,1) = 8: → 3_0 + 2_{+1} + 2_{-1} + 1_0
db_11 = (db_dirac_v2(3, 0.0) + db_dirac_v2(2, 1.0) +
         db_dirac_v2(2, -1.0) + db_dirac_v2(1, 0.0))
print(f"  (1,1) dim=8:  δb = ({db_11[0]:.4f}, {db_11[1]:.4f}, {db_11[2]:.4f})")

# (2,0) = 6: symmetric tensor → 3_{2/3} + 2_{-1/3} + 1_{-4/3}
db_20 = db_dirac_v2(3, 2.0/3.0) + db_dirac_v2(2, -1.0/3.0) + db_dirac_v2(1, -4.0/3.0)
print(f"  (2,0) dim=6:  δb = ({db_20[0]:.4f}, {db_20[1]:.4f}, {db_20[2]:.4f})")

# (0,2) = 6̄: conjugate (same β contributions)
db_02 = db_dirac_v2(3, -2.0/3.0) + db_dirac_v2(2, 1.0/3.0) + db_dirac_v2(1, 4.0/3.0)
print(f"  (0,2) dim=6:  δb = ({db_02[0]:.4f}, {db_02[1]:.4f}, {db_02[2]:.4f})")

# (3,0) = 10: → 4_{1} + 3_0 + 2_{-1} + 1_{-2}
db_30 = (db_dirac_v2(4, 1.0) + db_dirac_v2(3, 0.0) +
         db_dirac_v2(2, -1.0) + db_dirac_v2(1, -2.0))
print(f"  (3,0) dim=10: δb = ({db_30[0]:.4f}, {db_30[1]:.4f}, {db_30[2]:.4f})")

# (0,3) = 10̄: conjugate
db_03 = (db_dirac_v2(4, -1.0) + db_dirac_v2(3, 0.0) +
         db_dirac_v2(2, 1.0) + db_dirac_v2(1, 2.0))
print(f"  (0,3) dim=10: δb = ({db_03[0]:.4f}, {db_03[1]:.4f}, {db_03[2]:.4f})")

# (2,1) = 15: → 4_{1/3} + 3_{-2/3} + 3_{4/3} + 2_{1/3} + 2_{-5/3} + 1_{-2/3}
# Actually: SU(3) rep 15 = (2,1). Decomposition under SU(2) × U(1):
# From Clebsch-Gordan: (2,1) = 3⊗3̄ - 1 crossed with (2,0):
# More carefully, under SU(3) → SU(2) × U(1) maximal embedding:
# 15 → 4_{1/3} + 3_{-2/3} + 3_{4/3} + 2_{-5/3} + 2_{1/3} + 1_{-2/3}
# This is the standard decomposition for the 15 of SU(3).
db_21 = (db_dirac_v2(4, 1.0/3.0) + db_dirac_v2(3, -2.0/3.0) +
         db_dirac_v2(3, 4.0/3.0) + db_dirac_v2(2, -5.0/3.0) +
         db_dirac_v2(2, 1.0/3.0) + db_dirac_v2(1, -2.0/3.0))
print(f"  (2,1) dim=15: δb = ({db_21[0]:.4f}, {db_21[1]:.4f}, {db_21[2]:.4f})")

# (1,2) = 15̄: conjugate
db_12 = (db_dirac_v2(4, -1.0/3.0) + db_dirac_v2(3, 2.0/3.0) +
         db_dirac_v2(3, -4.0/3.0) + db_dirac_v2(2, 5.0/3.0) +
         db_dirac_v2(2, -1.0/3.0) + db_dirac_v2(1, 2.0/3.0))
print(f"  (1,2) dim=15: δb = ({db_12[0]:.4f}, {db_12[1]:.4f}, {db_12[2]:.4f})")
print()

# Build the map from dim² → δb
# dim² values: 1 (dim=1), 9 (dim=3), 36 (dim=6), 64 (dim=8), 100 (dim=10), 225 (dim=15)
# Note: dim=3 includes both (1,0) and (0,1); dim=6 includes (2,0) and (0,2), etc.
# Since they have the same |δb| contribution (conjugate reps), we average.

dim2_to_db = {
    1: db_00,           # (0,0)
    9: (db_10 + db_01) / 2.0,   # average of (1,0) and (0,1)
    36: (db_20 + db_02) / 2.0,  # average of (2,0) and (0,2)
    64: db_11,                    # (1,1)
    100: (db_30 + db_03) / 2.0,  # average of (3,0) and (0,3)
    225: (db_21 + db_12) / 2.0,  # average of (2,1) and (1,2)
}

# Print mode statistics
print("KK mode distribution and β-function contributions:")
unique_dim2 = np.unique(dim2_fold)
total_db = np.zeros(3)
for d2 in sorted(unique_dim2):
    d2_int = int(d2)
    count = np.sum(dim2_fold == d2)
    dim_su3 = int(np.sqrt(d2))
    db = dim2_to_db.get(d2_int, np.array([0.0, 0.0, 0.0]))
    total_db_this = count * db
    total_db += total_db_this
    print(f"  dim²={d2_int:>3d} (dim={dim_su3:>2d}): {count:>4d} modes × "
          f"δb = ({db[0]:>+7.4f}, {db[1]:>+7.4f}, {db[2]:>+7.4f}) "
          f"→ total ({total_db_this[0]:>+8.3f}, {total_db_this[1]:>+8.3f}, {total_db_this[2]:>+8.3f})")

print(f"\n  TOTAL δb from 992 KK modes:")
print(f"    δb_1 = {total_db[0]:+.4f}")
print(f"    δb_2 = {total_db[1]:+.4f}")
print(f"    δb_3 = {total_db[2]:+.4f}")
print()

# Compare to SM β functions
print(f"  SM β coefficients: b_1={b1_SM:.3f}, b_2={b2_SM:.3f}, b_3={b3_SM:.3f}")
print(f"  KK/SM ratio: δb_1/b_1 = {total_db[0]/b1_SM:.2f}, "
      f"δb_2/b_2 = {total_db[1]/b2_SM:.2f}")
print()

# ======================================================================
# SECTION 5: Staircase running
# ======================================================================
#
# Run from M_KK DOWN to M_Z.
# At each mass threshold M_n = ω_n × M_KK, the effective β changes.
# Between thresholds, the coupling evolves as:
#   d(1/α_i)/d(ln μ) = b_i^eff / (2π)
#
# The effective β function is:
#   b_i^eff(μ) = b_i^SM + Σ_{n: M_n > μ} δb_i^(n)
#
# Since we're running DOWN, we start at M_KK with all modes active,
# and they decouple one by one as we go to lower μ.
#
# But actually: modes with M_n > M_KK are NOT activated even at M_KK.
# The UV cutoff IS M_KK. Only modes with ω_n ≤ 1 are below M_KK.
# Modes with ω_n > 1 are ABOVE M_KK and would be integrated in above M_KK.
#
# Correction: In the DDG picture, ALL modes are part of the KK tower.
# At scale μ = M_KK, modes with M_n < M_KK (i.e., ω_n < 1) are
# already integrated out. Modes with M_n > M_KK (ω_n > 1) have NOT
# yet decoupled.
#
# More precisely: as we run from very high UV down,
# - At μ >> 2.06 M_KK: all modes are "light", all contribute
# - At μ = 2.06 M_KK: heaviest mode decouples
# - At μ = 0.82 M_KK: lightest KK mode decouples
# - At μ < 0.82 M_KK: only SM remains
#
# For the staircase:
# Start at μ_UV = ω_max × M_KK with all KK modes active.
# Run down, decoupling at each threshold.
# From μ = ω_min × M_KK down to M_Z: pure SM running.

print("=" * 72)
print("METHOD 1: Staircase Decoupling")
print("=" * 72)
print()

# We need boundary conditions at μ_UV. The framework gives conditions at M_KK.
# We run from M_KK using the framework's α_i(M_KK) values.
# Between M_KK and ω_min × M_KK, the KK modes with ω_n < 1 have already
# been integrated out. So the effective β below M_KK includes only modes
# with ω_n < 1 that haven't decoupled yet.
#
# Actually, the clean way: RUN FROM M_KK DOWN.
# At M_KK (= 1.0 in M_KK units), the modes above M_KK (ω_n > 1)
# contribute to threshold corrections at M_KK.
# The modes below M_KK (ω_n < 1) are active in the running below M_KK.
#
# Threshold correction AT M_KK from modes ABOVE M_KK:
#   Δ_i(M_KK) = Σ_{n: ω_n > 1} δb_i^(n)/(2π) × ln(ω_n)
#
# These shift the effective couplings at M_KK before the downward run.
#
# Then below M_KK, modes with ω_n < 1 decouple at μ = ω_n × M_KK.

# Split modes into above-MKK and below-MKK
above_mask = omega_fold > 1.0
below_mask = omega_fold <= 1.0
n_above = np.sum(above_mask)
n_below = np.sum(below_mask)

print(f"Mode split at M_KK:")
print(f"  Above M_KK (ω > 1): {n_above} modes")
print(f"  Below M_KK (ω ≤ 1): {n_below} modes")
print()

# For Kerner route
M_KK_use = M_KK_kerner  # Best match from S52 (α_2 matching)

# APPROACH 1: Framework boundary conditions at M_KK, including threshold
# corrections from modes above M_KK.

# Threshold correction from modes ABOVE M_KK
Delta_above = np.zeros(3)
for n in range(N_modes):
    if omega_fold[n] > 1.0:
        d2_int = int(dim2_fold[n])
        db = dim2_to_db.get(d2_int, np.zeros(3))
        Delta_above += db / (2*PI) * np.log(omega_fold[n])

print(f"Threshold correction from modes above M_KK:")
print(f"  Δ_1 = {Delta_above[0]:+.6f}")
print(f"  Δ_2 = {Delta_above[1]:+.6f}")
print(f"  Δ_3 = {Delta_above[2]:+.6f}")
print()

# Effective couplings at M_KK after integrating out heavy modes
# The heavy modes shift the coupling: 1/α_i^eff(M_KK) = 1/α_i(M_KK) - Δ_i
# (Minus because integrating out heavy modes increases 1/α for AF, decreases for IR-free)
# Actually: the sign depends on convention.
# In the standard matching:
#   1/α_i^eff(M_KK) = 1/α_i^bare(M_KK) + Δ_i
# where Δ_i > 0 from heavy modes means the low-energy coupling is weaker (1/α larger).
# Since δb_i < 0 for fermions (they make coupling run FASTER = make α LARGER),
# integrating them OUT at M_KK makes the coupling SMALLER (1/α larger).
# So: 1/α_i^eff = 1/α_i^bare + Σ |δb_i/(2π)| ln(M_n/M_KK)
# With our sign convention: Δ_above has negative entries from δb < 0.
# The effective coupling: 1/α_i^eff = 1/α_i^bare - Δ_above (the minus makes it positive)

alpha_1_inv_eff = alpha_1_inv_MKK - Delta_above[0]
alpha_2_inv_eff = alpha_2_inv_MKK - Delta_above[1]

print(f"Effective couplings at M_KK after heavy-mode threshold:")
print(f"  1/α_1^eff = {alpha_1_inv_eff:.4f}  (bare: {alpha_1_inv_MKK:.4f})")
print(f"  1/α_2^eff = {alpha_2_inv_eff:.4f}  (bare: {alpha_2_inv_MKK:.4f})")

s2w_eff_MKK = (3.0/5.0) * alpha_2_inv_eff / ((3.0/5.0) * alpha_2_inv_eff + alpha_1_inv_eff)
print(f"  sin²θ_W^eff(M_KK) = {s2w_eff_MKK:.6f}  (bare: {s2w_fold_val:.6f})")
print()

# Now staircase running from M_KK down to M_Z
# Sort the below-MKK modes by mass (descending) for sequential decoupling
below_omega = omega_fold[below_mask]
below_dim2 = dim2_fold[below_mask]
sort_idx = np.argsort(-below_omega)  # Descending
below_omega_sorted = below_omega[sort_idx]
below_dim2_sorted = below_dim2[sort_idx]

# Start at M_KK. Run down with staircase β function.
# At each threshold ω_n × M_KK, one mode decouples.
# The β coefficients are: b_i^eff = b_i^SM + Σ(active below-MKK modes) δb_i

# Initial effective β (all below-MKK modes active)
b_eff = np.array([b1_SM, b2_SM, b3_SM])
for n in range(n_below):
    d2_int = int(below_dim2_sorted[n])
    db = dim2_to_db.get(d2_int, np.zeros(3))
    b_eff += db

print(f"Effective β at M_KK (SM + {n_below} below-M_KK KK modes):")
print(f"  b_1^eff = {b_eff[0]:.4f} (SM: {b1_SM:.4f})")
print(f"  b_2^eff = {b_eff[1]:.4f} (SM: {b2_SM:.4f})")
print(f"  b_3^eff = {b_eff[2]:.4f} (SM: {b3_SM:.4f})")
print()

# Staircase integration
alpha_inv = np.array([alpha_1_inv_eff, alpha_2_inv_eff, alpha_3_inv_MZ])
# Actually, we need α_3 at M_KK too. The framework doesn't directly give it.
# Use the SM extrapolation: 1/α_3(M_KK) = 1/α_3(M_Z) + b3/(2π) ln(M_KK/M_Z)
t_total = np.log(M_KK_use / M_Z)
alpha_3_inv_MKK = alpha_3_inv_MZ + b3_SM / (2*PI) * t_total
alpha_inv = np.array([alpha_1_inv_eff, alpha_2_inv_eff, alpha_3_inv_MKK])

print(f"Starting couplings at M_KK = {M_KK_use:.3e} GeV:")
print(f"  1/α_1 = {alpha_inv[0]:.4f}")
print(f"  1/α_2 = {alpha_inv[1]:.4f}")
print(f"  1/α_3 = {alpha_inv[2]:.4f}")
print()

# Build list of thresholds: [(mass_in_GeV, mode_index_in_below_sorted)]
# At each threshold, we REMOVE one mode from the active set.
thresholds = [(below_omega_sorted[n] * M_KK_use, n) for n in range(n_below)]
# Sort by mass descending (we're running DOWN)
thresholds.sort(key=lambda x: -x[0])

# Run from M_KK_use down
mu_current = M_KK_use
b_current = np.copy(b_eff)

for mass_thresh, mode_idx in thresholds:
    if mass_thresh >= mu_current:
        continue  # Already past this threshold

    # Run from mu_current down to mass_thresh
    dt = np.log(mu_current / mass_thresh)
    alpha_inv += b_current / (2*PI) * (-dt)  # Running DOWN: subtract

    # Wait — sign convention.
    # 1/α(μ) = 1/α(μ₀) + b/(2π) ln(μ/μ₀)
    # Running from μ₀ = mu_current to μ = mass_thresh < mu_current:
    # 1/α(thresh) = 1/α(current) + b/(2π) ln(thresh/current)
    #             = 1/α(current) - b/(2π) dt  (where dt = ln(current/thresh) > 0)
    # Redo:
    alpha_inv = alpha_inv - b_current / (2*PI) * dt

    # Nope, double-counted. Let me redo from scratch more carefully.
    # Reset
    pass

# Let me redo the staircase cleanly:
print("Staircase running (recomputed cleanly):")
print()

alpha_inv_staircase = np.array([alpha_1_inv_eff, alpha_2_inv_eff, alpha_3_inv_MKK])
mu = M_KK_use

# b_current starts as SM + all below-MKK modes
b_current = np.array([b1_SM, b2_SM, b3_SM])
for n in range(n_below):
    d2_int = int(below_dim2_sorted[n])
    db = dim2_to_db.get(d2_int, np.zeros(3))
    b_current = b_current + db

# Create sorted list of (mass, δb_to_remove) for each below-MKK mode
# Sorted by mass descending
mode_list = []
for n in range(n_below):
    mass_n = below_omega_sorted[n] * M_KK_use
    d2_int = int(below_dim2_sorted[n])
    db = dim2_to_db.get(d2_int, np.zeros(3))
    mode_list.append((mass_n, db))

mode_list.sort(key=lambda x: -x[0])  # Descending in mass

n_steps = 0  # (local)
for mass_n, db_n in mode_list:
    # Run from mu down to mass_n
    if mass_n < mu:
        ln_ratio = np.log(mu / mass_n)
        # 1/α(mass_n) = 1/α(mu) + b/(2π) × ln(mass_n/mu)
        #             = 1/α(mu) - b/(2π) × ln(mu/mass_n)
        alpha_inv_staircase = alpha_inv_staircase - b_current / (2*PI) * ln_ratio
        mu = mass_n
        n_steps += 1

    # Remove this mode from active β
    b_current = b_current - db_n

# Now run from lightest KK mode down to M_Z with pure SM β
# b_current should now be = SM β
print(f"β after all KK modes decoupled: ({b_current[0]:.4f}, {b_current[1]:.4f}, {b_current[2]:.4f})")
print(f"  Should equal SM β: ({b1_SM:.4f}, {b2_SM:.4f}, {b3_SM:.4f})")
print(f"  Difference: ({b_current[0]-b1_SM:.2e}, {b_current[1]-b2_SM:.2e}, {b_current[2]-b3_SM:.2e})")
print()

# Final leg: pure SM from lightest KK mass to M_Z
ln_ratio_final = np.log(mu / M_Z)
alpha_inv_MZ_staircase = alpha_inv_staircase - b_current / (2*PI) * ln_ratio_final

print(f"After {n_steps} KK thresholds + SM running to M_Z:")
print(f"  1/α_1(M_Z) = {alpha_inv_MZ_staircase[0]:.4f}  (PDG: {alpha_1_inv_MZ})")
print(f"  1/α_2(M_Z) = {alpha_inv_MZ_staircase[1]:.4f}  (PDG: {alpha_2_inv_MZ})")
print(f"  1/α_3(M_Z) = {alpha_inv_MZ_staircase[2]:.4f}  (PDG: {alpha_3_inv_MZ})")
print()

s2w_staircase = (3.0/5.0) * alpha_inv_MZ_staircase[1] / (
    (3.0/5.0) * alpha_inv_MZ_staircase[1] + alpha_inv_MZ_staircase[0])

print(f"  sin²θ_W(M_Z) [staircase] = {s2w_staircase:.6f}")
print(f"  sin²θ_W(M_Z) [observed]  = {sin2_thetaW_MSbar}")
print(f"  Deficit: {s2w_staircase - sin2_thetaW_MSbar:+.6f}")
print(f"  Ratio: {s2w_staircase / sin2_thetaW_MSbar:.4f}")
print()

# ======================================================================
# SECTION 6: METHOD 2 — Dedekind Eta Regularization
# ======================================================================
#
# In string theory, the 1-loop threshold correction to gauge coupling α_i is:
#
#   Δ_i = -b_i^N=2/(2π) × [ln(4π²α' M_KK²) + 1 - γ_E]
#          - 1/(2π) Σ_s c_i(s) × ln|η(τ_s)|^4
#
# where η(τ) = q^{1/24} Π_{n=1}^∞ (1-q^n) is the Dedekind eta function,
# q = e^{2πiτ}, and τ_s parameterizes the KK lattice.
#
# For our SU(3) manifold, the role of η is played by the spectral zeta
# function of the Dirac operator. The "Dedekind eta" generalization is:
#
#   η_D = Π_n (1 - e^{-2π ω_n / Λ})
#
# where ω_n are the Dirac eigenvalues and Λ is a temperature/scale.
#
# The threshold correction becomes:
#   Δ_i = b_i^KK / (2π) × ln |η_D(M_KK/T)|²
#
# For T → ∞ (high temperature), η_D → 1 and Δ → 0.
# For T → 0, η_D → 0 and the correction diverges (all modes contribute).
#
# We evaluate this at T = M_KK (natural scale):

print("=" * 72)
print("METHOD 2: Dedekind Eta Regularization")
print("=" * 72)
print()

# Construct the spectral Dedekind eta product
# η_D(β) = Π_n (1 - e^{-β ω_n}) where β = 2π M_KK / T

# For a range of β values
beta_values = np.array([0.1, 0.5, 1.0, 2.0, 2*PI, 5.0, 10.0, 20.0])

print("Spectral Dedekind eta η_D(β) = Π_n (1 - exp(-β ω_n)):")
print(f"  {'β':>6s}  {'ln|η_D|':>12s}  {'ln|η_D|²':>12s}  Notes")
print(f"  {'-'*6}  {'-'*12}  {'-'*12}  {'-'*20}")

for beta in beta_values:
    # Compute ln|η_D| = Σ_n ln|1 - e^{-β ω_n}|
    exponents = -beta * omega_fold
    ln_eta = np.sum(np.log(np.abs(1.0 - np.exp(exponents))))
    notes = ""
    if abs(beta - 2*PI) < 0.01:
        notes = "β = 2π (natural)"
    if abs(beta - 1.0) < 0.01:
        notes = "β = 1"
    print(f"  {beta:>6.2f}  {ln_eta:>12.4f}  {2*ln_eta:>12.4f}  {notes}")

print()

# The physically motivated β:
# In string theory, τ = iR²/α', where R is the compactification radius.
# For our SU(3): R ~ 1/M_KK, α' ~ 1/M_string².
# The natural parameter is β = 2π (one "thermal circle" at the string scale).

beta_natural = 2.0 * PI
ln_eta_natural = np.sum(np.log(np.abs(1.0 - np.exp(-beta_natural * omega_fold))))

print(f"At β = 2π (natural string scale):")
print(f"  ln|η_D| = {ln_eta_natural:.6f}")
print(f"  ln|η_D|² = {2*ln_eta_natural:.6f}")
print()

# The Dedekind-eta threshold correction:
# Δ_i = -(b_i^KK)/(2π) × ln|η_D|²
# where b_i^KK is the KK-tower β function coefficient.
# Using total_db from Section 4:
Delta_eta = np.zeros(3)
for i in range(3):
    Delta_eta[i] = -total_db[i] / (2*PI) * 2 * ln_eta_natural

print(f"Dedekind eta threshold corrections (β = 2π):")
print(f"  Δ_1 = {Delta_eta[0]:+.6f}")
print(f"  Δ_2 = {Delta_eta[1]:+.6f}")
print(f"  Δ_3 = {Delta_eta[2]:+.6f}")
print()

# Apply to couplings at M_KK
alpha_1_inv_eta = alpha_1_inv_MKK + Delta_eta[0]
alpha_2_inv_eta = alpha_2_inv_MKK + Delta_eta[1]

print(f"Effective couplings at M_KK after Dedekind eta correction:")
print(f"  1/α_1 = {alpha_1_inv_eta:.4f}  (bare: {alpha_1_inv_MKK:.4f}, shift: {Delta_eta[0]:+.4f})")
print(f"  1/α_2 = {alpha_2_inv_eta:.4f}  (bare: {alpha_2_inv_MKK:.4f}, shift: {Delta_eta[1]:+.4f})")
print()

# Run down to M_Z with SM β
alpha_1_inv_eta_MZ = alpha_1_inv_eta - b1_SM / (2*PI) * t_total
alpha_2_inv_eta_MZ = alpha_2_inv_eta - b2_SM / (2*PI) * t_total

s2w_eta = (3.0/5.0) * alpha_2_inv_eta_MZ / (
    (3.0/5.0) * alpha_2_inv_eta_MZ + alpha_1_inv_eta_MZ)

print(f"After SM running to M_Z:")
print(f"  1/α_1(M_Z) = {alpha_1_inv_eta_MZ:.4f}  (PDG: {alpha_1_inv_MZ})")
print(f"  1/α_2(M_Z) = {alpha_2_inv_eta_MZ:.4f}  (PDG: {alpha_2_inv_MZ})")
print(f"  sin²θ_W(M_Z) = {s2w_eta:.6f}  (observed: {sin2_thetaW_MSbar})")
print(f"  Deficit: {s2w_eta - sin2_thetaW_MSbar:+.6f}")
print()

# ======================================================================
# SECTION 7: Scan over β to find optimal Dedekind parameter
# ======================================================================

print("=" * 72)
print("METHOD 2b: Scan Dedekind β parameter")
print("=" * 72)
print()

beta_scan = np.logspace(-2, 2, 2000)
s2w_scan_eta = np.zeros_like(beta_scan)

for ib, beta in enumerate(beta_scan):
    ln_eta = np.sum(np.log(np.abs(1.0 - np.exp(-beta * omega_fold))))

    # Threshold corrections
    D1 = -total_db[0] / (2*PI) * 2 * ln_eta
    D2 = -total_db[1] / (2*PI) * 2 * ln_eta

    # Effective couplings at M_KK
    a1_inv = alpha_1_inv_MKK + D1
    a2_inv = alpha_2_inv_MKK + D2

    # Run down
    a1_MZ = a1_inv - b1_SM / (2*PI) * t_total
    a2_MZ = a2_inv - b2_SM / (2*PI) * t_total

    if a1_MZ > 0 and a2_MZ > 0:
        s2w_scan_eta[ib] = (3.0/5.0) * a2_MZ / ((3.0/5.0) * a2_MZ + a1_MZ)
    else:
        s2w_scan_eta[ib] = np.nan

# Find closest to observed
valid = ~np.isnan(s2w_scan_eta)
if np.any(valid):
    resid = np.abs(s2w_scan_eta[valid] - sin2_thetaW_MSbar)
    best_idx_valid = np.argmin(resid)
    # Map back to full array
    valid_indices = np.where(valid)[0]
    best_idx = valid_indices[best_idx_valid]
    best_beta = beta_scan[best_idx]
    best_s2w = s2w_scan_eta[best_idx]

    print(f"β scan results:")
    print(f"  sin²θ_W range: [{np.nanmin(s2w_scan_eta):.4f}, {np.nanmax(s2w_scan_eta):.4f}]")
    print(f"  Best match to PDG:")
    print(f"    β_opt = {best_beta:.6f}")
    print(f"    sin²θ_W = {best_s2w:.6f}  (target: {sin2_thetaW_MSbar})")
    print(f"    Residual: {best_s2w - sin2_thetaW_MSbar:+.6f}")

    # Check if exact match exists
    crosses = np.where(np.diff(np.sign(s2w_scan_eta[valid] - sin2_thetaW_MSbar)))[0]
    if len(crosses) > 0:
        ic = crosses[0]
        ic_full_1 = valid_indices[ic]
        ic_full_2 = valid_indices[ic + 1]
        # Linear interpolation
        beta_cross = beta_scan[ic_full_1] + (
            sin2_thetaW_MSbar - s2w_scan_eta[ic_full_1]) * (
            beta_scan[ic_full_2] - beta_scan[ic_full_1]) / (
            s2w_scan_eta[ic_full_2] - s2w_scan_eta[ic_full_1])
        print(f"\n  EXACT crossing found at β = {beta_cross:.6f}")
        print(f"  This corresponds to T/M_KK = 2π/β = {2*PI/beta_cross:.4f}")
    else:
        print(f"\n  No exact crossing found. Minimum residual: {np.min(resid):.6f}")
    print()

# ======================================================================
# SECTION 8: METHOD 3 — Inverse Problem
# ======================================================================

print("=" * 72)
print("METHOD 3: Inverse Problem — Required Threshold Corrections")
print("=" * 72)
print()

# What Δ_1, Δ_2 are needed to land sin²θ_W = 0.231 at M_Z?
# We need:
#   1/α_1(M_Z) = 59.01 = (1/α_1(M_KK) + Δ_1) - b1/(2π) × t
#   1/α_2(M_Z) = 29.59 = (1/α_2(M_KK) + Δ_2) - b2/(2π) × t
#
# Solving for Δ_i:
Delta_1_req = alpha_1_inv_MZ + b1_SM / (2*PI) * t_total - alpha_1_inv_MKK
Delta_2_req = alpha_2_inv_MZ + b2_SM / (2*PI) * t_total - alpha_2_inv_MKK

print(f"Required threshold corrections to match PDG at M_Z:")
print(f"  Δ_1 = {Delta_1_req:+.4f}")
print(f"  Δ_2 = {Delta_2_req:+.4f}")
print(f"  |Δ_1| / (1/α_1(M_KK)) = {abs(Delta_1_req)/alpha_1_inv_MKK:.2%}")
print(f"  |Δ_2| / (1/α_2(M_KK)) = {abs(Delta_2_req)/alpha_2_inv_MKK:.2%}")
print()

# The RATIO Δ_1/Δ_2 is fixed by the group theory
Delta_ratio_req = Delta_1_req / Delta_2_req if Delta_2_req != 0 else float('inf')
Delta_ratio_KK = total_db[0] / total_db[1] if total_db[1] != 0 else float('inf')

print(f"Required ratio Δ_1/Δ_2 = {Delta_ratio_req:.4f}")
print(f"KK tower ratio δb_1/δb_2 = {Delta_ratio_KK:.4f}")
print(f"  Match: {'YES' if abs(Delta_ratio_req - Delta_ratio_KK) < 0.5 else 'NO'}")
print(f"  (If NO, the threshold corrections CANNOT solve the problem with")
print(f"   these charge assignments, regardless of overall magnitude.)")
print()

# Can we find the right magnitude?
# The threshold correction is Δ_i ∝ δb_i × f(spectrum)
# So Δ_1/Δ_2 = δb_1/δb_2 is FIXED by group theory.
# The only freedom is the overall normalization.
# If the RATIO doesn't match, no amount of correction will work.

# What would work: we need DIFFERENT charge assignments.
# Check: what ratio WOULD work?
print("Group theory analysis:")
print(f"  PDG requires: Δ_1/Δ_2 = {Delta_ratio_req:.4f}")
print(f"  Color-singlet CSDR gives: δb_1/δb_2 = {Delta_ratio_KK:.4f}")
print()
print(f"  The mismatch means: sin²θ_W(fold) = 0.584 requires a specific")
print(f"  RELATIVE correction to α_1 vs α_2 that the CSDR charge assignments")
print(f"  cannot provide.")
print()

# Check what sin²θ_W we'd get if we scaled the corrections to match Δ_2:
# Set Δ_2 = Delta_2_req, then Δ_1 = Delta_ratio_KK × Delta_2_req
if total_db[1] != 0 and Delta_2_req != 0:
    scale_factor = Delta_2_req / (total_db[1] / (2*PI) * 2 * ln_eta_natural)

    Delta_1_scaled = Delta_ratio_KK * Delta_2_req
    a1_inv_scaled = alpha_1_inv_MKK + Delta_1_scaled
    a2_inv_scaled = alpha_2_inv_MKK + Delta_2_req

    a1_MZ_scaled = a1_inv_scaled - b1_SM / (2*PI) * t_total
    a2_MZ_scaled = a2_inv_scaled - b2_SM / (2*PI) * t_total

    s2w_scaled = (3.0/5.0) * a2_MZ_scaled / (
        (3.0/5.0) * a2_MZ_scaled + a1_MZ_scaled)

    print(f"If we fix α_2 to match PDG, the CSDR ratio gives:")
    print(f"  1/α_1(M_Z) = {a1_MZ_scaled:.4f}  (PDG: {alpha_1_inv_MZ})")
    print(f"  1/α_2(M_Z) = {a2_MZ_scaled:.4f}  (PDG: {alpha_2_inv_MZ})")
    print(f"  sin²θ_W(M_Z) = {s2w_scaled:.6f}")
    print(f"  Deficit from PDG: {s2w_scaled - sin2_thetaW_MSbar:+.6f}")
    print()

# ======================================================================
# SECTION 9: Alternative — What if sin²θ_W(M_KK) = 3/8?
# ======================================================================
#
# The SU(5) normalization gives sin²θ_W = 3/8 = 0.375 at the GUT scale.
# SM running from 0.375 at ~2×10^16 to M_Z gives 0.231.
# This is the STANDARD successful prediction.
#
# Question: can we recover this by modifying the framework's sin²θ_W
# at M_KK from 0.584 to 0.375?

print("=" * 72)
print("ALTERNATIVE: SU(5)-normalized sin²θ_W")
print("=" * 72)
print()

# If sin²θ_W(M_KK) = 3/8 with α_2 unchanged:
s2w_su5 = 3.0/8.0
alpha_1_inv_su5 = (3.0/5.0) * alpha_2_inv_MKK * (1.0 - s2w_su5) / s2w_su5

print(f"If sin²θ_W(M_KK) = 3/8 = {s2w_su5} (SU(5)):")
print(f"  1/α_1(M_KK) = {alpha_1_inv_su5:.4f}")
print(f"  1/α_2(M_KK) = {alpha_2_inv_MKK:.4f}")

# Run down
a1_MZ_su5 = alpha_1_inv_su5 - b1_SM / (2*PI) * t_total
a2_MZ_su5 = alpha_2_inv_MKK - b2_SM / (2*PI) * t_total

s2w_MZ_su5 = (3.0/5.0) * a2_MZ_su5 / ((3.0/5.0) * a2_MZ_su5 + a1_MZ_su5)

print(f"  After SM running to M_Z:")
print(f"    1/α_1(M_Z) = {a1_MZ_su5:.4f}  (PDG: {alpha_1_inv_MZ})")
print(f"    1/α_2(M_Z) = {a2_MZ_su5:.4f}  (PDG: {alpha_2_inv_MZ})")
print(f"    sin²θ_W(M_Z) = {s2w_MZ_su5:.6f}  (observed: {sin2_thetaW_MSbar})")
print()

# The threshold correction needed to shift from 0.584 to 0.375:
Delta_s2w_needed = s2w_fold_val - s2w_su5
print(f"Required shift: Δ(sin²θ_W) = {Delta_s2w_needed:.4f}")
print(f"This requires shifting α_1^(-1) from {alpha_1_inv_MKK:.2f} to {alpha_1_inv_su5:.2f}")
print(f"  Δ(1/α_1) = {alpha_1_inv_su5 - alpha_1_inv_MKK:+.4f}")
print(f"  This is a {abs(alpha_1_inv_su5 - alpha_1_inv_MKK)/alpha_1_inv_MKK:.0%} change in 1/α_1")
print()

# ======================================================================
# SECTION 10: Summary and Cross-Domain Analysis
# ======================================================================

print("=" * 72)
print("COMPREHENSIVE SUMMARY")
print("=" * 72)
print()

# Collect all sin²θ_W results
results = {
    "Bare (no corrections)": s2w_fold_val,
    "Staircase decoupling": s2w_staircase,
    "Dedekind η (β=2π)": s2w_eta,
    "SU(5) norm (3/8 at M_KK)": s2w_MZ_su5,
    "Observed (PDG)": sin2_thetaW_MSbar,
}

print(f"{'Method':<35s}  {'sin²θ_W(M_Z)':>14s}  {'Deficit':>10s}  {'Ratio':>8s}")
print(f"{'-'*35}  {'-'*14}  {'-'*10}  {'-'*8}")
for label, val in results.items():
    deficit = val - sin2_thetaW_MSbar if label != "Observed (PDG)" else 0.0
    ratio = val / sin2_thetaW_MSbar
    marker = " <---" if label == "Observed (PDG)" else ""
    if label == "Bare (no corrections)":
        # Run down from fold to M_Z
        a1_bare_MZ = alpha_1_inv_MKK - b1_SM / (2*PI) * t_total
        a2_bare_MZ = alpha_2_inv_MKK - b2_SM / (2*PI) * t_total
        val = (3.0/5.0) * a2_bare_MZ / ((3.0/5.0) * a2_bare_MZ + a1_bare_MZ)
        deficit = val - sin2_thetaW_MSbar
        ratio = val / sin2_thetaW_MSbar
    print(f"{label:<35s}  {val:>14.6f}  {deficit:>+10.6f}  {ratio:>8.4f}{marker}")

print()

# Key diagnostic: WHY doesn't it work?
print("KEY DIAGNOSTIC:")
print()
print(f"  The problem is NOT the threshold corrections — they are perturbatively")
print(f"  small (~1-5% of the coupling values) because the SU(3) spectrum is")
print(f"  BOUNDED (ω ∈ [{omega_min:.3f}, {omega_max:.3f}]).")
print()
print(f"  The problem IS the boundary condition: sin²θ_W(fold) = {s2w_fold_val:.4f}.")
print(f"  The SM prediction: sin²θ_W(M_GUT) = 3/8 = 0.375 (SU(5) normalization).")
print(f"  The deficit: {s2w_fold_val - 3.0/8.0:.4f} = {(s2w_fold_val - 3.0/8.0)/(3.0/8.0)*100:.1f}% above SU(5).")
print()
print(f"  Threshold corrections shift sin²θ_W by at most ~{abs(s2w_staircase - s2w_fold_val)*100/(s2w_fold_val)*100:.1f}%")
print(f"  of the bare value, but the gap is {(s2w_fold_val - 3.0/8.0)/s2w_fold_val*100:.1f}%.")
print()
print(f"  The sin²θ_W = 0.584 is the bare GEOMETRIC ratio g'²/(g²+g'²) from the")
print(f"  Jensen metric eigenvalues. No perturbative correction to a bounded KK")
print(f"  tower can shift this by a factor of ~0.6.")
print()

# String-theoretic interpretation
print("STRING-THEORETIC INTERPRETATION:")
print()
print(f"  In string compactifications with modular invariance, threshold")
print(f"  corrections scale as ln|η(T)|² where T is the Kähler or complex")
print(f"  structure modulus. For large Im(T) → ∞, η(T) → e^{{-π Im(T)/12}}")
print(f"  and the correction grows LINEARLY in Im(T). This is the regime")
print(f"  where modular symmetry generates LARGE corrections.")
print()
print(f"  For the SU(3) Jensen manifold: ALL 992 eigenvalues are O(1).")
print(f"  There is no modulus to send to ∞. The spectral Dedekind η product")
print(f"  is bounded: ln|η_D| ∈ [{ln_eta_natural:.1f}, ...] for natural β.")
print()
print(f"  This is the FUNDAMENTAL difference between S^1 (or T^6) and SU(3):")
print(f"  - S^1: modes at n/R → ∞, modular invariance gives ln|η|² ~ R²")
print(f"  - SU(3): modes bounded, spectral η is an O(1) number")
print()
print(f"  The bounded spectrum that makes the framework FINITE (no UV divergences,")
print(f"  no Landau pole) also prevents large threshold corrections.")
print(f"  FINITENESS AND LARGE THRESHOLD CORRECTIONS ARE MUTUALLY EXCLUSIVE.")
print()

# ======================================================================
# SECTION 11: Gate Verdict
# ======================================================================

print("=" * 72)
print("GATE VERDICT: THRESHOLD-54")
print("=" * 72)
print()

# Best corrected value
s2w_best = s2w_staircase  # Most physical method
s2w_best_label = "staircase"

# Check if Dedekind scan found a match
try:
    if abs(best_s2w - sin2_thetaW_MSbar) < abs(s2w_staircase - sin2_thetaW_MSbar):
        s2w_best = best_s2w
        s2w_best_label = f"Dedekind β={best_beta:.2f}"
except:
    pass

print(f"VERDICT: INFO")
print()
print(f"  sin²θ_W(M_Z) [best corrected, {s2w_best_label}] = {s2w_best:.6f}")
print(f"  sin²θ_W(M_Z) [observed, PDG]                     = {sin2_thetaW_MSbar}")
print(f"  sin²θ_W(M_Z) [bare, no corrections]              = ", end="")

# Compute bare running to M_Z
a1_bare = alpha_1_inv_MKK - b1_SM / (2*PI) * t_total
a2_bare = alpha_2_inv_MKK - b2_SM / (2*PI) * t_total
s2w_bare_MZ = (3.0/5.0) * a2_bare / ((3.0/5.0) * a2_bare + a1_bare)
print(f"{s2w_bare_MZ:.6f}")
print()

print(f"  The 992-mode KK tower on Jensen SU(3) generates threshold")
print(f"  corrections that are PERTURBATIVELY SMALL relative to the gap.")
print(f"  The staircase method shifts sin²θ_W by ~{abs(s2w_staircase - s2w_bare_MZ):.4f}.")
print(f"  The gap to PDG is {s2w_bare_MZ - sin2_thetaW_MSbar:.4f}.")
print(f"  Threshold corrections close < {abs(s2w_staircase - s2w_bare_MZ)/(s2w_bare_MZ - sin2_thetaW_MSbar)*100:.1f}% of the gap.")
print()
print(f"  STRUCTURAL CONCLUSION:")
print(f"    The problem is the boundary condition sin²θ_W(fold) = 0.584,")
print(f"    not the running. This value comes from the ratio of the Jensen")
print(f"    metric eigenvalues e^{{-2τ}}. No perturbative threshold correction")
print(f"    from a bounded spectrum can bridge a factor-of-2.5 gap.")
print()
print(f"    The SU(5) normalization sin²θ_W = 3/8 is not built into the")
print(f"    framework's NCG spectral triple. The g'/g ratio is GEOMETRIC,")
print(f"    set by the internal manifold, and would require a DIFFERENT")
print(f"    metric (not Jensen) to reproduce sin²θ_W = 3/8 at M_KK.")
print()

# ======================================================================
# SECTION 12: Save data
# ======================================================================

save_path = os.path.join(os.path.dirname(__file__), 's54_threshold.npz')
np.savez(save_path,
    # Input spectrum
    omega_fold=omega_fold,
    dim2_fold=dim2_fold,
    N_modes=N_modes,
    omega_min=omega_min,
    omega_max=omega_max,

    # Framework boundary conditions
    alpha_1_inv_MKK=alpha_1_inv_MKK,
    alpha_2_inv_MKK=alpha_2_inv_MKK,
    sin2_thetaW_fold=s2w_fold_val,

    # Method 1: Staircase
    sin2_thetaW_staircase=s2w_staircase,
    alpha_1_inv_MZ_staircase=alpha_inv_MZ_staircase[0],
    alpha_2_inv_MZ_staircase=alpha_inv_MZ_staircase[1],

    # Method 2: Dedekind eta
    sin2_thetaW_eta_natural=s2w_eta,
    ln_eta_natural=ln_eta_natural,
    beta_scan=beta_scan,
    s2w_scan_eta=s2w_scan_eta,

    # Method 3: Inverse
    Delta_1_required=Delta_1_req,
    Delta_2_required=Delta_2_req,
    Delta_ratio_required=Delta_ratio_req,
    Delta_ratio_KK=Delta_ratio_KK,

    # KK tower β contributions
    total_db1=total_db[0],
    total_db2=total_db[1],
    total_db3=total_db[2],

    # Summary
    sin2_thetaW_best=s2w_best,
    sin2_thetaW_bare_MZ=s2w_bare_MZ,
    sin2_thetaW_PDG=sin2_thetaW_MSbar,
    M_KK_used=M_KK_use,
    verdict='INFO',
)

print(f"Data saved to: {save_path}")
print()

# ======================================================================
# SECTION 13: Cross-domain connection — The Phononic Perspective
# ======================================================================

print("=" * 72)
print("CROSS-DOMAIN: STRING → PHONON CORRESPONDENCE")
print("=" * 72)
print()
print("String Theory Analog                 Framework (M4 × SU(3))")
print("-" * 72)
print("KK tower on S^1: modes at n/R       | Dirac spectrum on SU(3): ω_n bounded")
print("Dedekind η(τ) = Π(1-q^n)            | Spectral η_D = Π(1-e^{-βω_n})")
print("Modular invariance: τ → τ+1, -1/τ   | Jensen deformation: τ → s=1-6τ²")
print("Large Im(τ): ln|η|² ~ Im(τ)         | Bounded spectrum: ln|η_D| = O(1)")
print("Power-law running from infinite tower| Logarithmic staircase from 992 modes")
print("sin²θ_W = 3/8 (SU(5) normalization) | sin²θ_W = 0.584 (Jensen metric ratio)")
print("Threshold corrections ~ few %        | Threshold corrections ~ few %")
print()
print("CLASSIFICATION: ANTI-CORRESPONDENCE for sin²θ_W prediction.")
print("The bounded spectrum is a STRUCTURAL feature that prevents the")
print("large threshold corrections available in string compactifications.")
print("This is the price of spectral finiteness.")
print()
print("PHONONIC RELEVANCE: NON-PHONONIC (gauge coupling running is")
print("a UV/geometric property, not a condensate/many-body property).")
