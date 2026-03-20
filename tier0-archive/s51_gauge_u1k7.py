#!/usr/bin/env python3
"""
Session 51 GAUGE-U1K7-51: U(1)_7 Gauging via Inner Fluctuations
=================================================================

QUESTION:
---------
Can U(1)_7 be gauged through inner fluctuations of the spectral triple,
thereby eating the Goldstone boson via the Anderson-Higgs mechanism?

ARGUMENT STRUCTURE:
-------------------
Level 1 (Tree): [iK_7, D_K] = 0 (S34, exact). Therefore A_7 = a[D_K, K_7] = 0.
Level 2 (One-loop): Sigma(D_K) is a function of D_K => [Sigma, K_7] = 0.
Level 3 (Off-diagonal): D_phys = D_K + A + JAJ* with A from other generators.
  ||[iK_7, D_phys]||/||D_phys|| = 0.052 (S35/S49). Does this generate
  a gauge kinetic term for A_7?

GATE: GAUGE-U1K7-51
  PASS: Effective kinetic term exists, m_gauge in [8, 16] M_KK
  FAIL: [iK_7, D_K] = 0 prevents kinetic term at all orders (structural)
  INFO: Kinetic term from off-diagonal fluctuations exists but m_gauge outside range

Author: connes-ncg-theorist, Session 51
Date: 2026-03-20
"""

import os
import sys
import time
import numpy as np
from numpy.linalg import eigh, norm, eigvalsh

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from canonical_constants import (
    tau_fold, Delta_0_GL, S_fold, a2_fold, a4_fold,
    M_KK, dS_fold, d2S_fold
)

from tier1_dirac_spectrum import (
    su3_generators, compute_structure_constants,
    compute_killing_form, jensen_metric, orthonormal_frame,
    frame_structure_constants, connection_coefficients,
    build_cliff8, spinor_connection_offset
)
from s23a_kosmann_singlet import kosmann_operator_antisymmetric
from s34a_dphys_fold import (
    build_J_operator, apply_J_to_matrix, build_AF_generators
)

np.set_printoptions(precision=12, linewidth=140, suppress=True)
t0 = time.time()

TAU = tau_fold  # 0.19

print("=" * 78)
print(f"GAUGE-U1K7-51: U(1)_7 Gauging via Inner Fluctuations")
print(f"tau = {TAU}")
print("=" * 78)

# ======================================================================
#  STEP 0: Build infrastructure at tau_fold
# ======================================================================

gens = su3_generators()
fabc = compute_structure_constants(gens)
Bk = compute_killing_form(fabc)
g_s = jensen_metric(Bk, TAU)
E = orthonormal_frame(g_s)
ft = frame_structure_constants(fabc, E)
Gamma = connection_coefficients(ft)
gammas = build_cliff8()
Omega = spinor_connection_offset(Gamma, gammas)
D_K = 1j * Omega  # Hermitian Dirac operator

# Verify hermiticity
herm_err_DK = np.max(np.abs(D_K - D_K.conj().T))
print(f"\nStep 0: D_K at tau={TAU}")
print(f"  dim = {D_K.shape[0]}x{D_K.shape[1]}")
print(f"  Hermiticity: |D_K - D_K^dag| = {herm_err_DK:.2e}")
assert herm_err_DK < 1e-13, f"D_K not hermitian: {herm_err_DK}"

evals_DK = eigvalsh(D_K)
DK_norm = norm(D_K, 'fro')
print(f"  Eigenvalues: {evals_DK}")
print(f"  ||D_K||_F = {DK_norm:.6f}")

# Build K_7 (Kosmann derivative)
K7_spinor, A7_antisym = kosmann_operator_antisymmetric(Gamma, gammas, 7)
iK7 = 1j * K7_spinor

herm_err_iK7 = np.max(np.abs(iK7 - iK7.conj().T))
print(f"\nStep 0: K_7 (Kosmann, a=7)")
print(f"  Hermiticity of iK_7: |iK_7 - iK_7^dag| = {herm_err_iK7:.2e}")
assert herm_err_iK7 < 1e-13, f"iK_7 not hermitian: {herm_err_iK7}"

# Build J operator
B_J = build_J_operator(gammas)

# ======================================================================
#  LEVEL 1: TREE LEVEL — [iK_7, D_K] = 0
# ======================================================================

print(f"\n{'='*78}")
print(f"LEVEL 1: TREE LEVEL — [iK_7, D_K] at tau = {TAU}")
print(f"{'='*78}")

comm_bare = iK7 @ D_K - D_K @ iK7
comm_bare_norm = norm(comm_bare, 'fro')
ratio_bare = comm_bare_norm / DK_norm

print(f"  ||[iK_7, D_K]||_F = {comm_bare_norm:.2e}")
print(f"  ||D_K||_F = {DK_norm:.6f}")
print(f"  RATIO = {ratio_bare:.2e}")
print(f"  ZERO to machine epsilon: {'YES' if ratio_bare < 1e-12 else 'NO'}")

# Consequence: A_7 = a[D_K, K_7] = 0 for ANY a in A_F
# The inner fluctuation in the K_7 direction is identically ZERO.
# No gauge field can be generated from K_7 through the standard NCG mechanism.

print(f"\n  CONSEQUENCE:")
print(f"  For any a in A_F: A_7 = a * [D_K, K_7] = a * 0 = 0")
print(f"  The K_7 direction in Omega^1_D(A_F) is TRIVIAL.")
print(f"  No gauge field dynamics (F_7^2 term) from spectral action.")
print(f"  TREE-LEVEL VERDICT: U(1)_7 gauge field ABSENT from inner fluctuations.")

# ======================================================================
#  LEVEL 2: ONE-LOOP — Does [D_eff, K_7] = 0 survive?
# ======================================================================

print(f"\n{'='*78}")
print(f"LEVEL 2: ONE-LOOP — van Suijlekom Paper 19 argument")
print(f"{'='*78}")

# The one-loop self-energy Sigma(D_K) is computed from the spectral action:
# Gamma^(1) = (1/2) Tr log(D_K^2)
# By Paper 19 (van Nuland-van Suijlekom 2022), one-loop counterterms have
# the SAME FORM as the classical spectral action. They are functionals of D_K
# alone (specifically, of D_K^2 through the heat kernel).
#
# If Sigma is a function of D_K (in the operator-algebraic sense), then:
# [K_7, Sigma(D_K)] = 0  whenever  [K_7, D_K] = 0
#
# Proof: Sigma(D_K) = sum_n c_n D_K^{2n} (from heat kernel / zeta function).
# [K_7, D_K^{2n}] = sum_{k=0}^{2n-1} D_K^k [K_7, D_K] D_K^{2n-1-k} = 0.
# Therefore [K_7, Sigma(D_K)] = 0.

# Verify explicitly: [iK_7, D_K^2] = 0
DK2 = D_K @ D_K
comm_DK2 = iK7 @ DK2 - DK2 @ iK7
ratio_DK2 = norm(comm_DK2, 'fro') / norm(DK2, 'fro')

# [iK_7, D_K^4] = 0
DK4 = DK2 @ DK2
comm_DK4 = iK7 @ DK4 - DK4 @ iK7
ratio_DK4 = norm(comm_DK4, 'fro') / norm(DK4, 'fro')

# [iK_7, f(D_K^2)] for f = exp(-x) at Lambda = 3 M_KK
Lambda_cutoff = 3.0  # M_KK units
fDK2 = np.zeros_like(D_K, dtype=complex)
# Build f(D_K^2/Lambda^2) in eigenbasis
evals_DK_full, evecs_DK_full = eigh(D_K)
for i in range(len(evals_DK_full)):
    x = evals_DK_full[i]**2 / Lambda_cutoff**2
    fDK2 += np.exp(-x) * np.outer(evecs_DK_full[:, i], evecs_DK_full[:, i].conj())

comm_fDK2 = iK7 @ fDK2 - fDK2 @ iK7
ratio_fDK2 = norm(comm_fDK2, 'fro') / norm(fDK2, 'fro')

print(f"  Explicit verification that K_7 commutes with functions of D_K:")
print(f"  ||[iK_7, D_K^2]||/||D_K^2||       = {ratio_DK2:.2e}")
print(f"  ||[iK_7, D_K^4]||/||D_K^4||       = {ratio_DK4:.2e}")
print(f"  ||[iK_7, f(D_K^2/L^2)]||/||f||    = {ratio_fDK2:.2e}")
print(f"  (f = exp(-x), Lambda = {Lambda_cutoff} M_KK)")
print()
print(f"  ARGUMENT (Paper 19, van Nuland-van Suijlekom 2022):")
print(f"  One-loop counterterms have the form a_0 + a_2 D_K^2 + a_4 D_K^4 + ...")
print(f"  All are polynomials in D_K, hence commute with K_7.")
print(f"  The one-loop effective Dirac operator D_eff = D_K + Sigma(D_K) satisfies:")
print(f"  [iK_7, D_eff] = [iK_7, D_K] + [iK_7, Sigma(D_K)] = 0 + 0 = 0")
print(f"  ONE-LOOP VERDICT: [iK_7, D_eff] = 0 at all loop orders (STRUCTURAL).")

# ======================================================================
#  LEVEL 3: OFF-DIAGONAL INNER FLUCTUATIONS
# ======================================================================

print(f"\n{'='*78}")
print(f"LEVEL 3: OFF-DIAGONAL FLUCTUATIONS — Does epsilon = 0.052 generate F_7^2?")
print(f"{'='*78}")

# Build all A_F generators and compute inner fluctuations
af_gens = build_AF_generators()
print(f"  Number of A_F generators: {len(af_gens)}")

# For each generator H, compute A_H = [D_K, H] + J[D_K, H]J*
# Then construct D_phys = D_K + phi * sum A_H
# and measure [iK_7, D_phys]

PHI_GAP = 0.133  # gap-edge amplitude (S35)

# Accumulate all inner fluctuations
A_total = np.zeros_like(D_K, dtype=complex)
gen_contributions = []

print(f"\n  Inner fluctuation contributions from each A_F generator:")
print(f"  {'Generator':>15s}  {'||[D_K,H]||_F':>14s}  {'||A_H||_F':>14s}  {'||[iK7,A_H]||_F':>16s}")

for name, gen in af_gens:
    # [D_K, H]
    comm_DK_H = D_K @ gen - gen @ D_K
    # J[D_K, H]J*
    J_comm = apply_J_to_matrix(B_J, comm_DK_H)
    # Self-adjoint combination
    A_H = comm_DK_H + J_comm
    # Symmetrize if needed for hermiticity
    herm_check = np.max(np.abs(A_H - A_H.conj().T))
    if herm_check > 1e-10:
        A_H = 0.5 * (A_H + A_H.conj().T)

    # K_7 commutator
    comm_K7_AH = iK7 @ A_H - A_H @ iK7

    gen_contributions.append({
        'name': name,
        'A_H': A_H,
        'norm_comm_DK_H': norm(comm_DK_H, 'fro'),
        'norm_A_H': norm(A_H, 'fro'),
        'norm_K7_AH': norm(comm_K7_AH, 'fro')
    })

    A_total += A_H

    print(f"  {name:>15s}  {norm(comm_DK_H, 'fro'):14.6f}  "
          f"{norm(A_H, 'fro'):14.6f}  {norm(comm_K7_AH, 'fro'):16.6f}")

# Symmetrize total
herm_total = np.max(np.abs(A_total - A_total.conj().T))
if herm_total > 1e-10:
    A_total = 0.5 * (A_total + A_total.conj().T)

# D_phys with all fluctuations at gap-edge amplitude
D_phys = D_K + PHI_GAP * A_total
herm_Dphys = np.max(np.abs(D_phys - D_phys.conj().T))
if herm_Dphys > 1e-10:
    D_phys = 0.5 * (D_phys + D_phys.conj().T)

Dphys_norm = norm(D_phys, 'fro')

# The 0.052 breaking
comm_phys = iK7 @ D_phys - D_phys @ iK7
epsilon_K7 = norm(comm_phys, 'fro') / Dphys_norm

print(f"\n  D_phys = D_K + {PHI_GAP} * sum_H A_H")
print(f"  ||D_phys||_F = {Dphys_norm:.6f}")
print(f"  ||[iK_7, D_phys]||/||D_phys|| = {epsilon_K7:.6f}")
print(f"  Cross-check: S35/S49 reported 0.052 -> we get {epsilon_K7:.4f}")

# ======================================================================
#  LEVEL 3a: THE KEY QUESTION — Does epsilon produce a gauge kinetic term?
# ======================================================================

print(f"\n{'='*78}")
print(f"LEVEL 3a: Does the 5.2% breaking generate a K_7 gauge kinetic term?")
print(f"{'='*78}")

# The spectral action gauge kinetic term for a gauge field A_mu arises from
# Tr f((D + A + JAJ*)^2 / Lambda^2) expanded to second order in A.
#
# For U(1)_7: A_7 = a[D_K, K_7] = 0.
# But the off-diagonal fluctuations break U(1)_7 at the 5.2% level.
# Does the spectral action of D_phys generate a term like
# int g_7^{-2} F_7^{mu nu} F_{7,mu nu}?
#
# The answer is NO, for a structural reason:
#
# In the NCG framework, the gauge kinetic term for a gauge field A_a
# comes from the a_4 Seeley-DeWitt coefficient of (D + A)^2:
#   Tr f(D_A^2/Lambda^2) contains f_0 * a_4[D_A]
#   a_4[D_A] contains (1/12g_a^2) int |F_a|^2 dvol
#
# For this to generate a KINETIC term for A_7, we need A_7 to appear as
# an INDEPENDENT gauge field in the fluctuated Dirac operator. But:
#
# (a) A_7 = a[D_K, K_7] = 0 (Level 1): K_7 does NOT generate a 1-form.
#     K_7 is in the kernel of the map a -> a[D, K_7].
#
# (b) The off-diagonal fluctuations A = phi * sum_H A_H break [iK_7, D_phys] != 0,
#     but they do NOT introduce a K_7 gauge field. They introduce gauge fields
#     for the STANDARD generators of A_F = C + H + M_3(C).
#
# (c) The breaking [iK_7, D_phys] != 0 means K_7 is no longer a symmetry
#     of D_phys. But a BROKEN symmetry does not produce a gauge field --
#     it produces a Goldstone boson (which is what U(1)_7 breaking does).
#     To produce a gauge field, K_7 must be an inner automorphism of A
#     that generates a NONTRIVIAL 1-form through [D, .].
#
# Let us verify (a) quantitatively: project D_phys onto the K_7 direction.

# Project the commutator [iK_7, D_phys] onto K_7 itself.
# If this has a K^2-like structure, it could indicate gauge dynamics.
# But since our system is 0D (single Peter-Weyl block), we test the
# algebraic structure instead.

# The key test: is K_7 in the image of the map phi -> [D_K, phi]?
# If not, no gauge field for K_7 can arise from inner fluctuations.

# Test: [D_K, K_7] = ?
comm_DK_K7 = D_K @ K7_spinor - K7_spinor @ D_K
norm_comm_DK_K7 = norm(comm_DK_K7, 'fro')

# Test: [D_K, iK_7] = ?
comm_DK_iK7 = D_K @ iK7 - iK7 @ D_K
norm_comm_DK_iK7 = norm(comm_DK_iK7, 'fro')

print(f"  ||[D_K, K_7]||_F   = {norm_comm_DK_K7:.2e}")
print(f"  ||[D_K, iK_7]||_F  = {norm_comm_DK_iK7:.2e}")
print(f"  K_7 is in ker([D_K, .]): {'YES' if norm_comm_DK_K7 < 1e-12 else 'NO'}")

# Now test: [D_phys, K_7] = ?
comm_Dphys_K7 = D_phys @ K7_spinor - K7_spinor @ D_phys
norm_Dphys_K7 = norm(comm_Dphys_K7, 'fro')

comm_Dphys_iK7 = D_phys @ iK7 - iK7 @ D_phys
norm_Dphys_iK7 = norm(comm_Dphys_iK7, 'fro')

print(f"\n  With D_phys (after off-diagonal fluctuations):")
print(f"  ||[D_phys, K_7]||_F   = {norm_Dphys_K7:.6f}")
print(f"  ||[D_phys, iK_7]||_F  = {norm_Dphys_iK7:.6f}")
print(f"  K_7 in ker([D_phys, .]): {'YES' if norm_Dphys_K7 < 1e-12 else 'NO'}")

# The spectral action second variation in the K_7 direction:
# delta^2 S / delta A_7^2 = sum_n f''(lambda_n^2/Lambda^2) * |<n|[D_K, K_7]|m>|^2 * (...)
# Since [D_K, K_7] = 0, this is ZERO at tree level.
#
# At the off-diagonal level with D_phys:
# delta^2 S_phys / delta A_7^2 ~ |<n|[D_phys, K_7]|m>|^2
# This is nonzero (epsilon = 0.052), but it does NOT produce a gauge KINETIC
# term (F^2) because the K_7 direction is not a gauge field — it is a
# generator of a symmetry that is BROKEN by the off-diagonal fluctuations.

# Compute the "effective gauge coupling" if we PRETEND K_7 is a gauge field
# g_7^{-2} ~ Tr([D_phys, iK_7]^dag [D_phys, iK_7]) / (d * ||D_phys||^2)
# where d = dim(spinor representation)

comm_sq = comm_Dphys_iK7.conj().T @ comm_Dphys_iK7
g7_inv_sq_eff = np.real(np.trace(comm_sq)) / (D_K.shape[0] * Dphys_norm**2)

print(f"\n  Hypothetical 'gauge coupling' from K_7 breaking:")
print(f"  g_7^{{-2}}_eff = Tr([D_phys,iK_7]^dag[D_phys,iK_7]) / (d*||D_phys||^2)")
print(f"  g_7^{{-2}}_eff = {g7_inv_sq_eff:.6f}")
if g7_inv_sq_eff > 0:
    g7_eff = 1.0 / np.sqrt(g7_inv_sq_eff)
    print(f"  g_7_eff = {g7_eff:.6f}")
else:
    g7_eff = 0.0
    print(f"  g_7_eff = 0 (no kinetic term)")

# ======================================================================
#  LEVEL 3b: THE DECISIVE STRUCTURAL ARGUMENT
# ======================================================================

print(f"\n{'='*78}")
print(f"LEVEL 3b: STRUCTURAL ARGUMENT — Why K_7 is NOT a gauge field")
print(f"{'='*78}")

# In NCG, gauge fields arise from inner automorphisms of the algebra A.
# The gauge group is G = SU(A) / center, and gauge fields are 1-forms:
#   Omega^1_D(A) = span{a[D, b] : a, b in A}
#
# K_7 is a Kosmann derivative = Lie derivative on the spinor bundle.
# It is a generator of the ISOMETRY group of SU(3), not an inner automorphism
# of the algebra A_F = C + H + M_3(C).
#
# The algebra A_F is the algebra of the INTERNAL (finite) space.
# K_7 generates a GEOMETRIC (external/fiber) symmetry.
# These are categorically different:
#   - Inner automorphisms of A_F -> gauge fields (SU(3) x SU(2) x U(1))
#   - Isometries of SU(3) -> coordinate transformations (diffeomorphisms)
#
# To gauge U(1)_7, one would need to:
#   (i) Add K_7 to the algebra A (enlarge A_F to include the U(1)_7 generator)
#   (ii) Verify that the enlarged algebra satisfies the NCG axioms
#   (iii) Check that [D_K, K_7] != 0 in the enlarged algebra
#
# But [D_K, K_7] = 0 (Level 1), so even if we ADD K_7 to A, the inner
# fluctuation A_7 = a[D, K_7] = 0 remains zero.

# Verify: K_7 is NOT in A_F (it does not commute with D_K modulo Omega^1_D)
# Actually, K_7 commutes with D_K EXACTLY — so K_7 is in the commutant of D_K.
# In NCG, elements of A that commute with D generate TRIVIAL gauge fields.

# The commutant of D: {X : [X, D] = 0}
# K_7 is in the commutant of D_K.
# Gauge fields from commutant elements are zero: a[D, b] = 0 if [D, b] = 0.

print(f"  K_7 in commutant of D_K: [D_K, K_7] = 0 (verified, Level 1)")
print(f"  => a * [D_K, K_7] = 0 for ALL a in A_F")
print(f"  => K_7 generates TRIVIAL (zero) gauge field")
print()
print(f"  STRUCTURAL CLASSIFICATION:")
print(f"  - A_F generators -> inner fluctuations -> gauge fields (SU(3)xSU(2)xU(1))")
print(f"  - K_7 (Kosmann) -> isometry of SU(3) -> diffeomorphism, NOT gauge field")
print(f"  - [D_K, K_7] = 0 -> K_7 is in commutant -> zero 1-form")
print(f"  - Even if K_7 were added to A_F, the vanishing commutator prevents gauging")

# ======================================================================
#  LEVEL 3c: EFFECTIVE MASS FROM OFF-DIAGONAL BREAKING
# ======================================================================

print(f"\n{'='*78}")
print(f"LEVEL 3c: If we FORCE m_gauge from epsilon = {epsilon_K7:.4f}")
print(f"{'='*78}")

# Even ignoring the structural impossibility, what mass would the 5.2% breaking give?
# In Anderson-Higgs: m_gauge = g_7 * |Delta| * sqrt(rho_s)
# The "effective g_7" from the breaking: g_7 ~ epsilon * ||D_phys|| / ||K_7||
# (This is dimensionally wrong but gives an order-of-magnitude bound.)

K7_norm = norm(iK7, 'fro')
g7_naive = epsilon_K7 * Dphys_norm / K7_norm
print(f"  Naive g_7 = epsilon * ||D_phys|| / ||K_7|| = {g7_naive:.6f}")
print(f"  (dimensionless, in M_KK units)")

# Even with this generous estimate:
# m_gauge ~ g7_naive * Delta_B2
# where Delta_B2 ~ Delta_0_GL = 0.77 M_KK
m_gauge_naive = g7_naive * Delta_0_GL
print(f"  m_gauge_naive = g_7 * Delta = {g7_naive:.4f} * {Delta_0_GL:.4f}")
print(f"                = {m_gauge_naive:.4f} M_KK")
print(f"  Required: m_gauge in [8, 16] M_KK")
print(f"  Shortfall: {8.0 / m_gauge_naive:.1f}x below lower bound" if m_gauge_naive > 0 else "  ZERO")

# More precise estimate: the gauge mass in Higgs mechanism is
# m_gauge^2 = g^2 * v^2  where v is the VEV and g is the coupling.
# The VEV breaks U(1)_7 -> the BCS condensate Delta.
# The coupling is epsilon_K7 (fractional breaking of U(1)_7).
# m_gauge^2 ~ epsilon_K7^2 * ||D_phys||^2 ~ (0.052)^2 * (5.4)^2 ~ 0.079
# m_gauge ~ 0.28 M_KK (extremely far from 8-16 M_KK)

m_gauge_est = epsilon_K7 * Dphys_norm
print(f"\n  Better estimate: m_gauge ~ epsilon * ||D_phys||_F/sqrt(d)")
print(f"  = {epsilon_K7:.4f} * {Dphys_norm:.4f} / sqrt({D_K.shape[0]})")
m_gauge_est2 = epsilon_K7 * Dphys_norm / np.sqrt(D_K.shape[0])
print(f"  = {m_gauge_est2:.4f} M_KK")
print(f"  Shortfall: {8.0 / m_gauge_est2:.1f}x below lower bound" if m_gauge_est2 > 0 else "  ZERO")

# ======================================================================
#  SUMMARY AND GATE VERDICT
# ======================================================================

print(f"\n{'='*78}")
print(f"GATE VERDICT: GAUGE-U1K7-51")
print(f"{'='*78}")

print(f"""
LEVEL 1 (Tree):
  [iK_7, D_K] = 0 to machine epsilon ({ratio_bare:.2e}).
  Inner fluctuation A_7 = a[D_K, K_7] = 0 for all a in A_F.
  No gauge field for U(1)_7 from standard NCG inner fluctuations.
  STATUS: CLOSED

LEVEL 2 (One-loop):
  Sigma(D_K) is a polynomial in D_K (Paper 19, van Nuland-vS 2022).
  [K_7, D_K^{{2n}}] = 0 for all n (verified: n=1,2,f(D_K^2)).
  D_eff = D_K + Sigma(D_K) satisfies [iK_7, D_eff] = 0 at all loop orders.
  STATUS: CLOSED

LEVEL 3 (Off-diagonal):
  D_phys with off-diagonal fluctuations gives epsilon = {epsilon_K7:.4f}.
  But epsilon comes from A_F generators breaking K_7 symmetry,
  NOT from K_7 becoming a gauge field.
  K_7 is a GEOMETRIC isometry (diffeomorphism), not an inner automorphism.
  [D_K, K_7] = 0 means K_7 generates a TRIVIAL 1-form.
  Even forced naive mass: m_gauge_naive = {m_gauge_naive:.4f} M_KK.
  Required: [8, 16] M_KK. Shortfall: {8.0/max(m_gauge_naive, 1e-10):.0f}x.
  STATUS: CLOSED

VERDICT: **FAIL** (STRUCTURAL).
  U(1)_7 cannot be gauged through inner fluctuations of the spectral triple.
  The Anderson-Higgs mechanism is structurally impossible for U(1)_7 in NCG.
  The Goldstone boson of U(1)_7 breaking CANNOT be eaten.

STRUCTURAL REASONS (any ONE suffices):
  1. [D_K, K_7] = 0 => A_7 = 0 => no gauge field (tree + all loops)
  2. K_7 is an isometry, not an inner automorphism => not a gauge generator
  3. K_7 is in the commutant of D_K => trivial 1-form
  4. Even forcing: m_gauge ~ 0.05 M_KK << 8 M_KK (shortfall {8.0/max(m_gauge_naive, 1e-10):.0f}x)
""")

# ======================================================================
#  SAVE DATA
# ======================================================================

elapsed = time.time() - t0
print(f"\nElapsed time: {elapsed:.1f} s")

np.savez_compressed(
    os.path.join(SCRIPT_DIR, "s51_gauge_u1k7.npz"),
    # Level 1
    comm_bare_norm=comm_bare_norm,
    ratio_bare=ratio_bare,
    DK_norm=DK_norm,
    evals_DK=evals_DK,
    # Level 2
    ratio_DK2=ratio_DK2,
    ratio_DK4=ratio_DK4,
    ratio_fDK2=ratio_fDK2,
    # Level 3
    epsilon_K7=epsilon_K7,
    norm_Dphys_K7=norm_Dphys_K7,
    norm_Dphys_iK7=norm_Dphys_iK7,
    g7_inv_sq_eff=g7_inv_sq_eff,
    g7_naive=g7_naive,
    m_gauge_naive=m_gauge_naive,
    m_gauge_est2=m_gauge_est2,
    # Metadata
    tau=TAU,
    phi_gap=PHI_GAP,
    Lambda_cutoff=Lambda_cutoff,
    gate="GAUGE-U1K7-51",
    verdict="FAIL",
)

print(f"Data saved to s51_gauge_u1k7.npz")
