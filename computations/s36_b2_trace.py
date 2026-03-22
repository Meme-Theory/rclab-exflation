#!/usr/bin/env python3
"""
Session 36: B2 Resonance Trace — Does the B2 fold select √(3/2)?

HYPOTHESIS: The physical gauge coupling at the dump point tau=0.190 is
determined by the RESONANT MODES (B2 flat band at the fold), not by
all SM fermions (Connes) or one test particle (Baptista).

The B2 modes correspond to the C^2 coset subspace of su(3) under the
decomposition su(3) = u(1) + su(2) + C^2. These carry specific
hypercharge and isospin quantum numbers.

If Tr_{B2}(T_3^2) / Tr_{B2}(Y^2) = 3/2, then g'/g = sqrt(3/2)*e^{-2s}
and the 1.7% match at the dump point has an algebraic origin.

MATHEMATICAL SETUP:
  su(3) = u(1) + su(2) + C^2  (decomposition under U(2) subgroup)

  Generators (Gell-Mann basis):
    su(2): lambda_1, lambda_2, lambda_3  (indices 0,1,2)
    C^2:   lambda_4, lambda_5, lambda_6, lambda_7  (indices 3,4,5,6)
    u(1):  lambda_8  (index 7)

  B2 = C^2 subspace = span{lambda_4, lambda_5, lambda_6, lambda_7}

  Under u(1)+su(2), each C^2 generator carries:
    - Hypercharge Y (eigenvalue under ad(lambda_8))
    - Weak isospin T_3 (eigenvalue under ad(lambda_3))

  These eigenvalues come from the adjoint representation of su(3).

Author: main agent, Session 36
Date: 2026-03-07
"""

import numpy as np

print("=" * 70)
print("B2 RESONANCE TRACE: COSET QUANTUM NUMBERS")
print("=" * 70)

# ─────────────────────────────────────────────────────────────
# 1. Gell-Mann matrices (standard basis for su(3))
# ─────────────────────────────────────────────────────────────

# Gell-Mann matrices (anti-hermitian convention: T_a = i*lambda_a/2)
lam = np.zeros((8, 3, 3), dtype=complex)

lam[0] = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]])         # lambda_1
lam[1] = np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]])      # lambda_2
lam[2] = np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]])         # lambda_3
lam[3] = np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]])          # lambda_4
lam[4] = np.array([[0, 0, -1j], [0, 0, 0], [1j, 0, 0]])      # lambda_5
lam[5] = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]])          # lambda_6
lam[6] = np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]])      # lambda_7
lam[7] = np.array([[1, 0, 0], [0, 1, 0], [0, 0, -2]]) / np.sqrt(3)  # lambda_8

# Anti-hermitian generators: e_a = i*lambda_a/2
e = 1j * lam / 2

# Verify: Baptista's Y = (iI_2) = diag(-2i, i, i) = sqrt(3) * i * lambda_8
# = 2*sqrt(3) * e_7
Y_baptista = np.diag([-2j, 1j, 1j])
Y_from_lam8 = np.sqrt(3) * 1j * lam[7]
print(f"\n  Y_Baptista = diag(-2i, i, i)")
print(f"  Y from sqrt(3)*i*lambda_8: match = {np.allclose(Y_baptista, Y_from_lam8)}")

# ─────────────────────────────────────────────────────────────
# 2. Adjoint representation: ad(X)(Z) = [X, Z]
# ─────────────────────────────────────────────────────────────

print(f"\n{'─' * 70}")
print("ADJOINT ACTION ON C^2 GENERATORS")
print(f"{'─' * 70}")

# The B2 modes are the C^2 generators: lambda_4, lambda_5, lambda_6, lambda_7
# (indices 3,4,5,6 in our zero-indexed array)
B2_indices = [3, 4, 5, 6]
B2_names = ["lambda_4", "lambda_5", "lambda_6", "lambda_7"]

# Y acts on C^2 via the adjoint: ad(Y)(lambda_a) = [Y, lambda_a]
# T_3 acts via: ad(T_3)(lambda_a) = [T_3, lambda_a]
# where Y = diag(-2i, i, i) and T_3 = diag(i, -i, 0) (= i*lambda_3)

T3_matrix = np.diag([1j, -1j, 0])  # T_3 = iota(i*sigma_3) = diag(i, -i, 0)

print(f"\n  Y = diag(-2i, i, i)")
print(f"  T_3 = diag(i, -i, 0)")
print(f"\n  Adjoint action [Y, lambda_a] and [T_3, lambda_a] on C^2 generators:")

# Compute ad(Y) and ad(T_3) restricted to C^2 subspace
# We work in the real 4D basis of C^2

# First: compute [Y, lambda_a] for each B2 generator
print(f"\n  {'Generator':<12s} {'[Y, lam_a]':>30s} {'[T3, lam_a]':>30s}")
print(f"  {'-'*72}")

for idx, name in zip(B2_indices, B2_names):
    comm_Y = Y_baptista @ lam[idx] - lam[idx] @ Y_baptista
    comm_T3 = T3_matrix @ lam[idx] - lam[idx] @ T3_matrix

    # Express commutators in terms of Gell-Mann matrices
    # [Y, lambda_a] should be a linear combination of C^2 generators
    # (since C^2 is an ad(u(1)+su(2))-module)

    # Check: is [Y, lam_a] in the C^2 subspace?
    # Project onto each Gell-Mann matrix: c_b = 2*Tr(lam_b * comm_Y)
    coeffs_Y = np.array([2 * np.trace(lam[b] @ comm_Y).real for b in range(8)])
    coeffs_T3 = np.array([2 * np.trace(lam[b] @ comm_T3).real for b in range(8)])

    # Clean up near-zero entries
    coeffs_Y[np.abs(coeffs_Y) < 1e-12] = 0
    coeffs_T3[np.abs(coeffs_T3) < 1e-12] = 0

    y_str = ", ".join([f"{c:.1f}*lam{i+1}" for i, c in enumerate(coeffs_Y) if c != 0])
    t3_str = ", ".join([f"{c:.1f}*lam{i+1}" for i, c in enumerate(coeffs_T3) if c != 0])

    print(f"  {name:<12s} {y_str:>30s} {t3_str:>30s}")

# ─────────────────────────────────────────────────────────────
# 3. Eigenvalues of ad(Y) and ad(T_3) on C^2
# ─────────────────────────────────────────────────────────────

print(f"\n{'─' * 70}")
print("EIGENVALUES OF ad(Y) AND ad(T_3) ON C^2 SUBSPACE")
print(f"{'─' * 70}")

# Build 4x4 matrix of ad(Y) restricted to C^2
# ad(Y)|_{C^2} in basis {lambda_4, lambda_5, lambda_6, lambda_7}
ad_Y_C2 = np.zeros((4, 4), dtype=complex)
ad_T3_C2 = np.zeros((4, 4), dtype=complex)

for i, idx_i in enumerate(B2_indices):
    comm_Y = Y_baptista @ lam[idx_i] - lam[idx_i] @ Y_baptista
    comm_T3 = T3_matrix @ lam[idx_i] - lam[idx_i] @ T3_matrix

    for j, idx_j in enumerate(B2_indices):
        # Project [Y, lam_i] onto lam_j: coefficient = 2*Tr(lam_j * [Y, lam_i])
        ad_Y_C2[j, i] = 2 * np.trace(lam[idx_j] @ comm_Y)
        ad_T3_C2[j, i] = 2 * np.trace(lam[idx_j] @ comm_T3)

# Clean
ad_Y_C2[np.abs(ad_Y_C2) < 1e-12] = 0
ad_T3_C2[np.abs(ad_T3_C2) < 1e-12] = 0

print(f"\n  ad(Y)|_{{C^2}} =")
for row in ad_Y_C2.real:
    print(f"    [{', '.join(f'{x:6.2f}' for x in row)}]")

print(f"\n  ad(T_3)|_{{C^2}} =")
for row in ad_T3_C2.real:
    print(f"    [{', '.join(f'{x:6.2f}' for x in row)}]")

# Eigenvalues
eig_Y = np.linalg.eigvals(ad_Y_C2)
eig_T3 = np.linalg.eigvals(ad_T3_C2)

# Sort by real part
eig_Y = np.sort_complex(eig_Y)
eig_T3 = np.sort_complex(eig_T3)

print(f"\n  Eigenvalues of ad(Y)|_{{C^2}}: {[f'{e.real:.4f}' for e in eig_Y]}")
print(f"  Eigenvalues of ad(T_3)|_{{C^2}}: {[f'{e.real:.4f}' for e in eig_T3]}")

# ─────────────────────────────────────────────────────────────
# 4. Traces: Tr_{B2}(Y^2) and Tr_{B2}(T_3^2)
# ─────────────────────────────────────────────────────────────

print(f"\n{'─' * 70}")
print("TRACES OVER B2 SUBSPACE")
print(f"{'─' * 70}")

# Method 1: From eigenvalues of the adjoint
# The "Y^2 trace" over B2 means Tr(ad(Y)^2 restricted to C^2)
# This equals sum of squared eigenvalues

tr_Y2_B2 = np.trace(ad_Y_C2 @ ad_Y_C2).real
tr_T32_B2 = np.trace(ad_T3_C2 @ ad_T3_C2).real

print(f"\n  Method 1: From adjoint matrices")
print(f"    Tr_{{B2}}(ad(Y)^2) = {tr_Y2_B2:.6f}")
print(f"    Tr_{{B2}}(ad(T_3)^2) = {tr_T32_B2:.6f}")
print(f"    Ratio Tr(T_3^2)/Tr(Y^2) = {tr_T32_B2/tr_Y2_B2:.6f}")

# Method 2: From squared eigenvalues
tr_Y2_eig = np.sum(eig_Y**2).real
tr_T32_eig = np.sum(eig_T3**2).real
print(f"\n  Method 2: From eigenvalue sums")
print(f"    Sum(y_i^2) = {tr_Y2_eig:.6f}")
print(f"    Sum(t3_i^2) = {tr_T32_eig:.6f}")
print(f"    Ratio = {tr_T32_eig/tr_Y2_eig:.6f}")

# ─────────────────────────────────────────────────────────────
# 5. THE KEY QUESTION: Is the ratio 3/2?
# ─────────────────────────────────────────────────────────────

print(f"\n{'=' * 70}")
print("THE KEY QUESTION: Does Tr_B2(T_3^2)/Tr_B2(Y^2) = 3/2?")
print(f"{'=' * 70}")

ratio = tr_T32_B2 / tr_Y2_B2
target = 3/2

print(f"\n  Computed ratio: {ratio:.10f}")
print(f"  Target (3/2):   {target:.10f}")
print(f"  Match: {np.isclose(ratio, target)}")

if np.isclose(ratio, target):
    print(f"\n  >>> YES! Tr_B2(T_3^2)/Tr_B2(Y^2) = 3/2 EXACTLY <<<")
    print(f"\n  This means:")
    print(f"    g'/g|_{{B2 resonance}} = sqrt(3/2) * e^{{-2s}}")
    print(f"    At s=0.190: g'/g = {np.sqrt(3/2) * np.exp(-2*0.190):.6f}")
    print(f"    SM at M_KK: g'/g = 0.852")
    print(f"    Deviation: {abs(np.sqrt(3/2)*np.exp(-0.38) - 0.852)/0.852*100:.1f}%")
    print(f"\n  The B2 fold selects sqrt(3/2). The resonance IS the coupling.")
else:
    print(f"\n  Ratio = {ratio:.6f}, NOT 3/2 = {target:.6f}")
    print(f"  The B2 trace does not give sqrt(3/2).")
    print(f"  Deviation from 3/2: {abs(ratio - target)/target*100:.1f}%")

# ─────────────────────────────────────────────────────────────
# 6. ALSO CHECK: What coupling ratio does the B2 trace give?
# ─────────────────────────────────────────────────────────────

print(f"\n{'─' * 70}")
print("PHYSICAL IMPLICATIONS OF B2 TRACE RATIO")
print(f"{'─' * 70}")

# The B2 trace gives the coupling ratio for a theory where only
# the B2 (C^2 coset) modes contribute to the gauge kinetic term
r_B2 = np.sqrt(ratio)
sin2_B2 = ratio / (1 + ratio)

print(f"\n  g'/g|_{{B2}} = sqrt({ratio:.4f}) = {r_B2:.6f}")
print(f"  sin^2|_{{B2}} at s=0 = {ratio:.4f}/{1+ratio:.4f} = {sin2_B2:.6f}")

print(f"\n  Comparison of all three methods at s=0:")
print(f"  {'Method':<25s} {'g\'/g':>8s} {'sin^2':>8s}")
print(f"  {'-'*45}")
print(f"  {'Baptista (1 eigenvalue)':<25s} {np.sqrt(3):>8.4f} {3/4:>8.4f}")
print(f"  {'B2 resonance trace':<25s} {r_B2:>8.4f} {sin2_B2:>8.4f}")
print(f"  {'Connes (all fermions)':<25s} {np.sqrt(3/5):>8.4f} {3/8:>8.4f}")

print(f"\n  Ordering: Baptista > B2 > Connes (if B2 is intermediate)")
print(f"  B2 sits BETWEEN single-eigenvalue and full-trace.")

# Save
np.savez('tier0-computation/s36_b2_trace.npz',
         ad_Y_C2=ad_Y_C2,
         ad_T3_C2=ad_T3_C2,
         eig_Y=eig_Y,
         eig_T3=eig_T3,
         tr_Y2_B2=np.array([tr_Y2_B2]),
         tr_T32_B2=np.array([tr_T32_B2]),
         ratio=np.array([ratio]),
         )
print(f"\nData saved: tier0-computation/s36_b2_trace.npz")
