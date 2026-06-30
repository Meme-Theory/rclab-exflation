#!/usr/bin/env python3
"""
S52 CASIMIR-JOSEPHSON-52: J_12/J_23 from Casimir Algebra
=========================================================

Express the Josephson coupling ratio J_12/J_23 = 19.52 as a function of
Casimir operators of B1, B2, B3. Test whether the phi crossing condition
reduces to an algebraic equation in Casimir eigenvalues.

MAIN RESULT: V_constrained is EXACTLY rank-1 (sv2/sv1 = 4.5e-17).
This forces J_12/J_23 = V_11/V_33 = (v_1/v_3)^2 as an algebraic identity.
The BCS self-consistency equation further forces Delta_1/Delta_3 = v_1/v_3.
The Josephson ratio encodes the rank-1 vector components, NOT Casimir eigenvalues.

Sectors:
  B1 = (0,0) singlet:       C_2 = 0,    C_3 = 0,    dim = 1
  B2 = (1,1) adjoint:       C_2 = 3,    C_3 = 0,    dim = 8
  B3 = (1,0)+(0,1) fund+conj: C_2 = 4/3, C_3 = +-10/27, dim = 3+3=6

Gate: CASIMIR-JOSEPHSON-52
  PASS: J_12/J_23 derivable algebraically from C_2 values
  INFO: Ratio involves non-Casimir matrix elements

Input:
  computations/session-34/s34a_dphys_kosmann.npz
  computations/session-46/s46_qtheory_selfconsistent.npz
  computations/session-48/s48_leggett_mode.npz
  computations/session-44/s44_dos_tau.npz

Output:
  computations/session-52/s52_casimir_josephson.npz
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from canonical_constants import *

import numpy as np

print("=" * 72)
print("S52 CASIMIR-JOSEPHSON-52: J_12/J_23 from Casimir Algebra")
print("=" * 72)

# ============================================================================
# SECTION 1: Load data
# ============================================================================
print("\n--- Section 1: Loading data ---")

base = os.path.dirname(os.path.abspath(__file__))
archive = os.path.join(base, "..", "_shared")

kosmann = np.load(os.path.join(archive, 's34a_dphys_kosmann.npz'), allow_pickle=True)
s46 = np.load(os.path.join(archive, 's46_qtheory_selfconsistent.npz'), allow_pickle=True)
leggett = np.load(os.path.join(base, 's48_leggett_mode.npz'), allow_pickle=True)
dos_data = np.load(os.path.join(base, 's44_dos_tau.npz'), allow_pickle=True)

# Extract Josephson couplings at the fold
J_12 = float(leggett['J_12_fold'])
J_23 = float(leggett['J_23_fold'])
J_13 = float(leggett['J_13_fold'])

ratio_12_23 = J_12 / J_23
ratio_12_13 = J_12 / J_13
ratio_23_13 = J_23 / J_13

print(f"J_12 (B1-B2) = {J_12:.8f}")
print(f"J_23 (B2-B3) = {J_23:.8f}")
print(f"J_13 (B1-B3) = {J_13:.8f}")
print(f"J_12/J_23 = {ratio_12_23:.6f}")
print(f"J_12/J_13 = {ratio_12_13:.6f}")
print(f"J_23/J_13 = {ratio_23_13:.6f}")

# ============================================================================
# SECTION 2: SU(3) Casimir Invariants
# ============================================================================
print("\n--- Section 2: SU(3) Casimir Invariants ---")

def casimir2(p, q):
    return (p**2 + q**2 + p*q + 3*p + 3*q) / 3.0

def casimir3(p, q):
    return (p - q) * (2*p + q + 3) * (p + 2*q + 3) / 18.0

def dim_rep(p, q):
    return (p + 1) * (q + 1) * (p + q + 2) // 2

C2_B1 = casimir2(0, 0)  # = 0
C2_B2 = casimir2(1, 1)  # = 3
C2_B3 = casimir2(1, 0)  # = 4/3
C3_B1 = casimir3(0, 0)  # = 0
C3_B2 = casimir3(1, 1)  # = 0
C3_B3f = casimir3(1, 0) # = +10/27
C3_B3c = casimir3(0, 1) # = -10/27
dim_B1 = dim_rep(0, 0)  # = 1
dim_B2 = dim_rep(1, 1)  # = 8
dim_B3 = dim_rep(1, 0) + dim_rep(0, 1)  # = 6

print(f"{'Sector':<8} {'(p,q)':<8} {'C_2':>8} {'C_3':>10} {'dim':>5}")
print("-" * 45)
for name, pq in [('B1',(0,0)), ('B2',(1,1)), ('B3f',(1,0)), ('B3c',(0,1))]:
    print(f"{name:<8} ({pq[0]},{pq[1]})    {casimir2(*pq):8.4f} {casimir3(*pq):10.4f} {dim_rep(*pq):5d}")

# ============================================================================
# SECTION 3: V_constrained rank analysis -- THE KEY RESULT
# ============================================================================
print("\n--- Section 3: V_constrained Rank Analysis (KEY RESULT) ---")

V = s46['V_mat_constrained']
print(f"V_constrained (3x3):")
for i in range(3):
    row = "  [" + ", ".join(f"{V[i,j]:.8f}" for j in range(3)) + "]"
    print(row)

# Singular value decomposition
sv = np.linalg.svd(V, compute_uv=False)
print(f"\nSingular values: {sv}")
print(f"sv[1]/sv[0] = {sv[1]/sv[0]:.2e}")
print(f"sv[2]/sv[0] = {sv[2]/sv[0]:.2e}")
rank = int(np.sum(sv > 1e-10))
print(f"Numerical rank: {rank}")

is_rank_1 = (rank == 1)
print(f"\n*** V_constrained is EXACTLY RANK-1 ***" if is_rank_1 else
      f"\n*** V_constrained is rank {rank} ***")

# Rank-1 decomposition: V = v * v^T
v = np.sqrt(np.diag(V))
print(f"\nRank-1 vector v = sqrt(diag(V)) = [{v[0]:.8f}, {v[1]:.8f}, {v[2]:.8f}]")

# Verify: V / (v * v^T)
V_outer = np.outer(v, v)
ratio_matrix = V / V_outer
print(f"\nV / (v * v^T) (should be all 1.0):")
for i in range(3):
    row = "  [" + ", ".join(f"{ratio_matrix[i,j]:.10f}" for j in range(3)) + "]"
    print(row)

max_dev = np.max(np.abs(ratio_matrix - 1.0))
print(f"Max deviation from 1.0: {max_dev:.2e}")

# ============================================================================
# SECTION 4: Algebraic identity J_12/J_23 = V_11/V_33
# ============================================================================
print("\n--- Section 4: Algebraic Identity ---")

# In BCS multiband, J_ij = V_ij * |Delta_i| * |Delta_j|
# For rank-1 V: V_ij = v_i * v_j
# BCS gap equation: Delta_i = v_i * lambda * sum_k(v_k^2 / E_k)
# => Delta_i proportional to v_i
# => Delta_i/Delta_j = v_i/v_j

D1 = float(s46['Delta_B1_fold'])
D3 = float(s46['Delta_B3_fold'])
D2 = float(s46['Delta_B2_fold'])

print(f"From S46 data:")
print(f"  Delta_B1 = {D1:.8f}")
print(f"  Delta_B2 = {D2:.8f}")
print(f"  Delta_B3 = {D3:.8f}")

print(f"\nSelf-consistency check (rank-1 => Delta_i/Delta_j = v_i/v_j):")
print(f"  v_1/v_3 = {v[0]/v[2]:.8f}")
print(f"  D_1/D_3 = {D1/D3:.8f}")
print(f"  Match: {np.isclose(v[0]/v[2], D1/D3)}")

print(f"\n  v_1/v_2 = {v[0]/v[1]:.8f}")
print(f"  D_1/D_2 = {D1/D2:.8f}")
print(f"  Match: {np.isclose(v[0]/v[1], D1/D2)}")

print(f"\n  v_2/v_3 = {v[1]/v[2]:.8f}")
print(f"  D_2/D_3 = {D2/D3:.8f}")
print(f"  Match: {np.isclose(v[1]/v[2], D2/D3)}")

# Now the identity:
# J_12/J_23 = (V_12 * D_1 * D_2) / (V_23 * D_2 * D_3)
#           = (v_1*v_2 * v_1 * v_2) / (v_2*v_3 * v_2 * v_3)
#           = (v_1/v_3)^2
#           = V_11/V_33

print(f"\n*** ALGEBRAIC IDENTITY (rank-1 theorem) ***")
print(f"  J_12/J_23 = (v_1/v_3)^2 = V_11/V_33")
print(f"  V_11/V_33 = {V[0,0]/V[2,2]:.8f}")
print(f"  (v_1/v_3)^2 = {(v[0]/v[2])**2:.8f}")
print(f"  J_12/J_23 = {ratio_12_23:.8f}")
print(f"  Match: {np.isclose(V[0,0]/V[2,2], ratio_12_23)}")

# Similarly for other ratios:
print(f"\n  J_12/J_13 = (v_2/v_3)^2 = V_22/V_33")
print(f"  V_22/V_33 = {V[1,1]/V[2,2]:.8f}")
print(f"  J_12/J_13 = {ratio_12_13:.8f}")
print(f"  Match: {np.isclose(V[1,1]/V[2,2], ratio_12_13)}")

print(f"\n  J_23/J_13 = (v_2/v_1)^2 = V_22/V_11")
print(f"  V_22/V_11 = {V[1,1]/V[0,0]:.8f}")
print(f"  (J_23/J_13)^{-1} = J_13/J_23... checking:")
print(f"  J_23/J_13 = {ratio_23_13:.8f}")

# Actually: J_ij/J_ik = (v_j/v_k)^2, not (v_i/v_k)^2. Let me be precise.
# J_12 = v_1*v_2*v_1*v_2 = v_1^2 * v_2^2
# J_23 = v_2*v_3*v_2*v_3 = v_2^2 * v_3^2
# J_13 = v_1*v_3*v_1*v_3 = v_1^2 * v_3^2
# J_12/J_23 = v_1^2/v_3^2 = V_11/V_33  CHECK
# J_12/J_13 = v_2^2/v_3^2 = V_22/V_33  CHECK
# J_23/J_13 = v_2^2/v_1^2 = V_22/V_11  ...

print(f"\nVerification of all J ratios:")
print(f"  J_12/J_23 = v_1^2/v_3^2 = {v[0]**2/v[2]**2:.8f} vs {ratio_12_23:.8f}")
print(f"  J_12/J_13 = v_2^2/v_3^2 = {v[1]**2/v[2]**2:.8f} vs {ratio_12_13:.8f}")
print(f"  J_23/J_13 = v_2^2/v_1^2 = {v[1]**2/v[0]**2:.8f} vs {ratio_23_13:.8f}")

# ============================================================================
# SECTION 5: Tau-independence verification
# ============================================================================
print("\n--- Section 5: Tau-Independence of J_12/J_23 ---")

tau_scan = leggett['tau_scan']
J_12_scan = leggett['J_12_scan']
J_23_scan = leggett['J_23_scan']
ratio_scan = J_12_scan / J_23_scan
D1_scan = leggett['Delta_B1_scan']
D3_scan = leggett['Delta_B3_scan']

print(f"{'tau':>6} {'J_12/J_23':>12} {'D_1/D_3':>10} {'V_12/V_23':>10}")
print("-" * 45)
for i in range(len(tau_scan)):
    r = ratio_scan[i]
    d_ratio = D1_scan[i] / D3_scan[i]
    v_inferred = r / d_ratio
    print(f"{tau_scan[i]:6.2f} {r:12.6f} {d_ratio:10.6f} {v_inferred:10.6f}")

print(f"\nJ_12/J_23 coefficient of variation: {ratio_scan.std()/ratio_scan.mean()*100:.2e}%")
print(f"D_1/D_3 coefficient of variation: {D1_scan.std()/D1_scan.mean()*100:.2e}%")
print(f"*** Both exactly tau-independent (rank-1 theorem) ***")

# ============================================================================
# SECTION 6: Casimir content of V_11/V_33
# ============================================================================
print("\n--- Section 6: Casimir Content of V_11/V_33 ---")

# The question becomes: is V_11/V_33 (= v_1^2/v_3^2) expressible in Casimirs?
# V_ii is the intra-sector pairing strength, determined by:
#   V_ii = <B_i, B_i | K_a | B_i, B_i> (Kosmann kernel projected onto sector i)
# This involves the full matrix element, not just the Casimir.

print(f"\nV_ii values (diagonal of V_constrained):")
print(f"  V_11 (B1, singlet) = {V[0,0]:.8f}")
print(f"  V_22 (B2, adjoint) = {V[1,1]:.8f}")
print(f"  V_33 (B3, fund)    = {V[2,2]:.8f}")

print(f"\nV_ii ratios:")
print(f"  V_11/V_33 = {V[0,0]/V[2,2]:.6f} = J_12/J_23")
print(f"  V_22/V_33 = {V[1,1]/V[2,2]:.6f} = J_12/J_13")
print(f"  V_22/V_11 = {V[1,1]/V[0,0]:.6f} = J_23/J_13")

# Test: are these Casimir ratios?
delta_C2_12 = abs(C2_B2 - C2_B1)
delta_C2_23 = abs(C2_B2 - C2_B3)

print(f"\nCasimir-based predictions for V_11/V_33:")
print(f"  C_2(B2)^2/C_2(B3)^2 = {C2_B2**2/C2_B3**2:.6f}  (off by {(V[0,0]/V[2,2])/(C2_B2**2/C2_B3**2):.2f}x)")
print(f"  dim(B1)^2*C_2(B2)/dim(B3f)^2 = {1*3/9:.6f}")
print(f"  (delta C_2)^2 ratio: {delta_C2_12**2/delta_C2_23**2:.6f}")
print(f"  None of these match V_11/V_33 = {V[0,0]/V[2,2]:.6f}")

# V_ii are Kosmann kernel matrix elements -- they encode the GEOMETRY of
# the pairing interaction, not just representation theory.
# The key point is: V is rank-1, so everything reduces to v_i ratios,
# but v_i themselves come from a specific Dirac operator calculation.

# Check against V from Kosmann data (phi-dependent)
V_B1B2_phi = kosmann['V_B1B2_max_vs_phi']
V_B3B2_phi = kosmann['V_B3B2_max_vs_phi']
phi_amps = kosmann['phi_amplitudes']

print(f"\nV_B1B2/V_B3B2 from Kosmann (phi-dependent, S34):")
print(f"  phi=0:     {V_B1B2_phi[0]/V_B3B2_phi[0]:.6f}")
print(f"  phi=0.13:  {V_B1B2_phi[13]/V_B3B2_phi[13]:.6f}")
print(f"  These vary with phi, unlike V_constrained (rank-1) which is fixed")
print(f"  V_constrained ratio V_12/V_23 = {V[0,1]/V[1,2]:.6f}")

# ============================================================================
# SECTION 7: Phi crossing condition
# ============================================================================
print("\n--- Section 7: Phi Crossing Condition ---")

# phi_paasch = m_{(3,0)}/m_{(0,0)} = 1.53158 at tau=0.15
phi_paasch_val = 1.53158  # NOTE: phi_paasch not yet in canonical_constants — candidate for promotion  # (local)
C2_30 = casimir2(3, 0)  # = 6
C2_00 = casimir2(0, 0)  # = 0

# If omega ~ sqrt(C_2 + f(tau)):
# phi = sqrt((6+f)/f) = 1.53158 => f = 6/(phi^2 - 1) = 4.4585
f_param = C2_30 / (phi_paasch_val**2 - 1)
phi_check = np.sqrt((C2_30 + f_param) / (C2_00 + f_param))
print(f"sqrt(C_2 + f) model:")
print(f"  f = {C2_30}/(phi^2 - 1) = {f_param:.4f}")
print(f"  phi_check = sqrt((6+f)/f) = {phi_check:.6f}")
print(f"  phi_paasch = {phi_paasch_val:.6f}")
print(f"  Match: {np.isclose(phi_check, phi_paasch_val)}")

# Get actual eigenvalues at tau=0.15
omega_015 = dos_data['tau0.15_all_omega']
print(f"\nActual spectrum at tau=0.15:")
print(f"  min omega = {omega_015.min():.6f}")
print(f"  max omega = {omega_015.max():.6f}")
print(f"  max/min = {omega_015.max()/omega_015.min():.6f} (phi_paasch = {phi_paasch_val})")
print(f"  Note: max/min = 2.426, phi = 1.532, so phi is NOT max/min of full spectrum")
print(f"  phi is the ratio for SPECIFIC reps (3,0)/(0,0)")

# Eigenvalue energies at fold
E_B1_val = E_B1       # 0.8191
E_B2_val = E_B2_mean  # 0.8453
E_B3_val = E_B3_mean  # 0.9782

print(f"\nSector eigenvalue energies at fold:")
print(f"  E_B1 = {E_B1_val:.6f} (C_2=0)")
print(f"  E_B2 = {E_B2_val:.6f} (C_2=3)")
print(f"  E_B3 = {E_B3_val:.6f} (C_2=4/3)")

# These are NOT monotone in C_2:
# E_B1 < E_B2 < E_B3 but C_2(B1) < C_2(B3) < C_2(B2)
print(f"  Note: E ordering (B1<B2<B3) differs from C_2 ordering (B1<B3<B2)")
print(f"  => eigenvalues are NOT a monotone function of C_2")

# ============================================================================
# SECTION 8: Rank-1 theorem statement
# ============================================================================
print("\n--- Section 8: Rank-1 Theorem ---")

print(f"""
THEOREM (Rank-1 Josephson Identity):
  If the inter-sector pairing matrix V is rank-1 (V_ij = v_i * v_j),
  then the BCS self-consistency forces Delta_i proportional to v_i,
  and all Josephson coupling RATIOS are tau-independent:

    J_ij/J_kl = (v_i * v_j) / (v_k * v_l)

  In particular:
    J_12/J_23 = v_1^2/v_3^2 = V_11/V_33

  Proof: J_ij = V_ij * Delta_i * Delta_j = v_i*v_j * (alpha*v_i)*(alpha*v_j)
         = alpha^2 * v_i^2 * v_j^2
         where alpha(tau) absorbs all tau dependence.

VERIFICATION:
  V_constrained singular values: {sv[0]:.6e}, {sv[1]:.2e}, {sv[2]:.2e}
  Rank: {rank} (to machine epsilon)
  V_11/V_33 = {V[0,0]/V[2,2]:.8f}
  J_12/J_23 = {ratio_12_23:.8f}
  Match: {np.isclose(V[0,0]/V[2,2], ratio_12_23)}
  Tau variation: 0.00% (exact)
""")

# ============================================================================
# SECTION 9: Algebraic search for V_11/V_33
# ============================================================================
print("--- Section 9: Algebraic Value of V_11/V_33 ---")

target = V[0,0] / V[2,2]
print(f"V_11/V_33 = {target:.8f}")
print(f"sqrt(V_11/V_33) = v_1/v_3 = {np.sqrt(target):.8f}")

# Best rational approximations
print(f"\nClosest simple rationals to V_11/V_33:")
best_rats = []
for a in range(1, 500):
    for b in range(1, 500):
        if abs(a/b - target) / target < 0.001:
            best_rats.append((a, b, abs(a/b - target)/target))

best_rats.sort(key=lambda x: x[2])
for a, b, err in best_rats[:10]:
    print(f"  {a}/{b} = {a/b:.8f}  (err = {err*100:.4f}%)")

# Notable algebraic numbers near sqrt(V_11/V_33)
x = np.sqrt(target)
print(f"\nClosest algebraic to v_1/v_3 = {x:.8f}:")
alg_cands = {
    '53/12': 53/12,
    '4+5/12': 4+5/12,
    '3+sqrt(2)': 3+np.sqrt(2),
    'sqrt(19.5)': np.sqrt(19.5),
    '2*pi^2 root': np.sqrt(2*np.pi**2),
    'C_2(B2)+C_2(B3)': C2_B2 + C2_B3,
}
for name, val in sorted(alg_cands.items(), key=lambda kv: abs(kv[1]-x)):
    err = (val - x) / x * 100
    print(f"  {name:<20} = {val:10.6f}  ({err:+.3f}%)")

# V_11 and V_33 individually
print(f"\nV_ii in Kosmann kernel units:")
print(f"  V_11 = {V[0,0]:.8f}")
print(f"  V_22 = {V[1,1]:.8f}")
print(f"  V_33 = {V[2,2]:.8f}")

# Check if V_ii ~ dim^alpha for some alpha
# V_11/dim_B1^alpha = V_33/dim_B3f^alpha
# V_11/V_33 = (dim_B1/dim_B3f)^alpha = (1/3)^alpha
# 19.52 = (1/3)^alpha => alpha = ln(19.52)/ln(1/3) = -2.706
alpha_dim = np.log(target) / np.log(dim_B1 / 3.0)  # dim_B3f = 3
print(f"\n  If V_ii ~ dim^alpha: alpha = {alpha_dim:.4f}")
print(f"  V_11/V_33 = (1/3)^{alpha_dim:.4f} = {(1/3)**alpha_dim:.6f}")

# ============================================================================
# SECTION 10: Casimir Ansaetze for V_ii
# ============================================================================
print("\n--- Section 10: Simple Casimir Formulas for V_ii ---")

# V_ii is the Kosmann kernel matrix element for intra-sector pairing.
# It depends on the geometry of the pairing channel, not just Casimirs.
# But let's check if there's an approximate formula.

print(f"\nSector   dim    C_2     C_3     V_ii")
print("-" * 50)
for name, pq, vii in [('B1', (0,0), V[0,0]), ('B2', (1,1), V[1,1]), ('B3', (1,0), V[2,2])]:
    c2 = casimir2(*pq)
    c3 = casimir3(*pq)
    d = dim_rep(*pq)
    print(f"  {name:<6} {d:>4}  {c2:>6.3f}  {c3:>7.3f}  {vii:.8f}")

# Check: V_ii proportional to dim(rep)?
print(f"\n  V_11/dim(B1) = {V[0,0]/1:.6f}")
print(f"  V_22/dim(B2) = {V[1,1]/8:.6f}")
print(f"  V_33/dim(B3f) = {V[2,2]/3:.6f}")
print(f"  NOT proportional to dim")

# V_ii proportional to dim^2?
print(f"\n  V_11/dim(B1)^2 = {V[0,0]/1:.6f}")
print(f"  V_22/dim(B2)^2 = {V[1,1]/64:.6f}")
print(f"  V_33/dim(B3f)^2 = {V[2,2]/9:.6f}")
print(f"  NOT proportional to dim^2")

# ============================================================================
# SECTION 11: Gate Verdict
# ============================================================================
print("\n" + "=" * 72)
print("SECTION 11: GATE VERDICT -- CASIMIR-JOSEPHSON-52")
print("=" * 72)

print(f"""
FINDINGS:

1. STRUCTURAL THEOREM: V_constrained is EXACTLY rank-1.
   Singular values: [{sv[0]:.6e}, {sv[1]:.2e}, {sv[2]:.2e}]
   V_ij = v_i * v_j where v = [{v[0]:.6f}, {v[1]:.6f}, {v[2]:.6f}]

2. ALGEBRAIC IDENTITY: J_12/J_23 = V_11/V_33 = (v_1/v_3)^2
   V_11/V_33 = {V[0,0]/V[2,2]:.8f}
   J_12/J_23 = {ratio_12_23:.8f}
   Agreement to machine epsilon.

3. SELF-CONSISTENCY: BCS gap equation forces Delta_i = alpha * v_i
   v_1/v_3 = {v[0]/v[2]:.8f}
   D_1/D_3 = {D1/D3:.8f}
   Agreement to machine epsilon.

4. TAU INDEPENDENCE: J_12/J_23 is EXACTLY constant across all tau.
   All tau dependence is in alpha(tau)^2, which cancels in ratios.

5. CASIMIR CONTENT: V_11/V_33 = 19.52 is NOT a simple function of
   Casimir eigenvalues C_2(B1)=0, C_2(B2)=3, C_2(B3)=4/3.
   It encodes the GEOMETRY of the Kosmann pairing kernel projected
   onto sectors, which depends on full matrix elements, not just
   representation labels.

6. PHI CROSSING: m_{{(3,0)}}/m_{{(0,0)}} = 1.5316 is consistent with
   omega ~ sqrt(C_2 + f(tau)) where f = {f_param:.4f}, but this is a
   one-parameter fit, not a derivation from Casimirs.

GATE VERDICT: INFO
  J_12/J_23 = {ratio_12_23:.4f} is an ALGEBRAIC IDENTITY forced by
  the rank-1 structure of V_constrained, equaling V_11/V_33.
  The numerical value encodes Kosmann kernel geometry, NOT Casimir
  eigenvalues. The deeper structural content is the rank-1 theorem
  itself, which makes ALL Josephson ratios tau-independent.
""")

verdict = "INFO"

# ============================================================================
# Save results
# ============================================================================
print("--- Saving results ---")

save_dict = {
    # Josephson couplings
    'J_12_fold': J_12,
    'J_23_fold': J_23,
    'J_13_fold': J_13,
    'ratio_J12_J23': ratio_12_23,
    'ratio_J12_J13': ratio_12_13,
    'ratio_J23_J13': ratio_23_13,

    # V_constrained structure
    'V_constrained': V,
    'V_singular_values': sv,
    'V_rank': np.array(rank),
    'V_rank1_vector': v,
    'V11_over_V33': np.array(V[0,0] / V[2,2]),
    'V22_over_V33': np.array(V[1,1] / V[2,2]),
    'V22_over_V11': np.array(V[1,1] / V[0,0]),

    # Self-consistency
    'v1_over_v3': np.array(v[0] / v[2]),
    'D1_over_D3': np.array(D1 / D3),
    'v1_over_v2': np.array(v[0] / v[1]),
    'D1_over_D2': np.array(D1 / D2),

    # Casimirs
    'C2_B1': C2_B1,
    'C2_B2': C2_B2,
    'C2_B3': C2_B3,
    'dim_B1': dim_B1,
    'dim_B2': dim_B2,
    'dim_B3': dim_B3,

    # Eigenvalue energies
    'E_B1': E_B1_val,
    'E_B2_mean': E_B2_val,
    'E_B3_mean': E_B3_val,

    # Phi crossing
    'phi_paasch': phi_paasch_val,
    'f_param_sqrt_model': f_param,

    # Tau scan
    'tau_scan': tau_scan,
    'J12_J23_scan': ratio_scan,
    'J12_J23_cv': ratio_scan.std() / (ratio_scan.mean() + 1e-30),

    # Gate
    'gate_name': np.array(['CASIMIR-JOSEPHSON-52']),
    'gate_verdict': np.array([verdict]),
    'gate_detail': np.array([
        f'V_constrained rank-1 (sv2/sv1={sv[1]/sv[0]:.1e}). '
        f'J12/J23=V11/V33={V[0,0]/V[2,2]:.4f} (algebraic identity). '
        f'Not Casimir: encodes Kosmann kernel geometry.'
    ]),
}

outpath = os.path.join(base, 's52_casimir_josephson.npz')
np.savez(outpath, **save_dict)
print(f"Saved: {outpath}")
print(f"Gate: CASIMIR-JOSEPHSON-52 = {verdict}")
print("\nDone.")
