#!/usr/bin/env python3
"""
S77-D4-PATI-SALAM: Intermediate Symmetry in SU(3) Fiber
=========================================================

Gate: S77-D4-PATI-SALAM (INFO)
Expected: Non-existence of intermediate symmetry enhancement at tau != 0.

Physics:
  The Jensen metric on the SU(3) fiber decomposes su(3) into three irreducible
  U(2)-modules under the isotropy representation at the identity coset of SU(3)/U(2):

    Module 1: u(1) complement in u(2)   -- dim 1, eigenvalue L_1 = e^{2*tau}
    Module 2: su(2) in u(2)             -- dim 3, eigenvalue L_2 = e^{-2*tau}
    Module 3: C^2 coset directions      -- dim 4, eigenvalue L_3 = e^{tau}

  (Here 'eigenvalue' means the Jensen metric parameter lambda_i = alpha * e^{...},
   with alpha = overall scale that drops out of ratios.)

  A symmetry enhancement occurs when two or more eigenvalues coincide, because
  the metric then has a LARGER isometry group than generic Jensen.

  Subalgebra chains of su(3):
    Chain A: su(3) -> su(2) + u(1) -> u(1) + u(1)    [maximal regular]
    Chain B: su(3) -> u(2) = su(2) + u(1)             [isotropy of SU(3)/U(2)]
    Chain C: su(3) -> so(3)                            [maximal non-regular, irreducible 3D]

  For each chain, we ask: at which tau do eigenvalues coincide?

  Pati-Salam-type intermediate symmetry would require a scale (tau value) where
  SU(4)_C x SU(2)_L x SU(2)_R or a similar left-right-symmetric group embeds.
  Since our total fiber is SU(3) (rank 2, dim 8), Pati-Salam (rank 5, dim 21+6+6=33)
  CANNOT embed. The question reduces to: does the Jensen metric flow through any
  intermediate symmetry enhancement between tau=0 (bi-invariant, maximal symmetry)
  and tau=tau_fold?

Computation:
  1. Enumerate all pairs (L_i, L_j) and solve L_i(tau) = L_j(tau)
  2. For each solution, identify the enhanced symmetry group
  3. Sweep tau in [0, 1] and compute all eigenvalue ratios
  4. Check if any Pati-Salam-like (L-R symmetric) structure appears

Result: All coincidences occur at tau=0 only. No intermediate symmetry enhancement.

Session: S77 | Date: 2026-04-13
"""

import numpy as np
import sys
sys.path.insert(0, r"C:\sandbox\Ainulindale Exflation\computations")
from canonical_constants import tau_fold, PI

# =============================================================================
#  Section 1: Jensen metric eigenvalues
# =============================================================================

def jensen_eigenvalues(tau):
    """
    Jensen metric eigenvalues on SU(3) fiber.

    The metric on su(3) = u(1) + su(2) + C^2 is:
      g = L_1 * g|_{u(1)} + L_2 * g|_{su(2)} + L_3 * g|_{C^2}

    where (Baptista convention, our tau = Baptista's s):
      L_1(tau) = e^{2*tau}    [u(1) direction, dim 1]
      L_2(tau) = e^{-2*tau}   [su(2) block, dim 3]
      L_3(tau) = e^{tau}      [coset C^2, dim 4]

    The overall scale alpha is set to 1 (drops out of all ratios).
    Volume-preserving condition: L_1 * L_2^3 * L_3^4 = const.
    Check: 2*tau + 3*(-2*tau) + 4*tau = 2tau - 6tau + 4tau = 0.  Verified.
    """
    L_1 = np.exp(2 * tau)   # (local)
    L_2 = np.exp(-2 * tau)  # (local)
    L_3 = np.exp(tau)       # (local)
    return L_1, L_2, L_3

# =============================================================================
#  Section 2: Analytic coincidence analysis
# =============================================================================

print("=" * 72)
print("S77-D4-PATI-SALAM: Intermediate Symmetry in SU(3) Fiber")
print("=" * 72)

print("\n--- Section 2: Analytic Coincidence Analysis ---")
print()
print("Jensen eigenvalues:")
print("  L_1(tau) = e^{2*tau}   [u(1), dim 1]")
print("  L_2(tau) = e^{-2*tau}  [su(2), dim 3]")
print("  L_3(tau) = e^{tau}     [C^2 coset, dim 4]")
print()

# Pair (1,2): L_1 = L_2
# e^{2*tau} = e^{-2*tau} => 2*tau = -2*tau => tau = 0
print("Pair (L_1, L_2): e^{2*tau} = e^{-2*tau}")
print("  => 2*tau = -2*tau => 4*tau = 0 => tau = 0")
print("  Enhanced symmetry at tau=0: u(1) and su(2) have same scale")
print()

# Pair (1,3): L_1 = L_3
# e^{2*tau} = e^{tau} => 2*tau = tau => tau = 0
print("Pair (L_1, L_3): e^{2*tau} = e^{tau}")
print("  => 2*tau = tau => tau = 0")
print("  Enhanced symmetry at tau=0: u(1) and C^2 have same scale")
print()

# Pair (2,3): L_2 = L_3
# e^{-2*tau} = e^{tau} => -2*tau = tau => -3*tau = 0 => tau = 0
print("Pair (L_2, L_3): e^{-2*tau} = e^{tau}")
print("  => -2*tau = tau => 3*tau = 0 => tau = 0")
print("  Enhanced symmetry at tau=0: su(2) and C^2 have same scale")
print()

# Triple: L_1 = L_2 = L_3
print("Triple (L_1, L_2, L_3): all three equal => tau = 0")
print("  => bi-invariant (round) metric, full SU(3)_L x SU(3)_R / Z_3 isometry")
print()

print("CONCLUSION (analytic): ALL eigenvalue coincidences occur at tau = 0 ONLY.")
print("No intermediate symmetry enhancement exists for tau != 0.")
print()

# =============================================================================
#  Section 3: Numerical verification — eigenvalue ratios over tau sweep
# =============================================================================

print("--- Section 3: Numerical Verification ---")
print()

N_tau = 10001  # (local)
tau_arr = np.linspace(0.0, 1.0, N_tau)  # (local)

L1_arr = np.exp(2 * tau_arr)   # (local)
L2_arr = np.exp(-2 * tau_arr)  # (local)
L3_arr = np.exp(tau_arr)       # (local)

# Ratios
r12 = L1_arr / L2_arr  # = e^{4*tau}, monotonically increasing  (local)
r13 = L1_arr / L3_arr  # = e^{tau}, monotonically increasing     (local)
r23 = L2_arr / L3_arr  # = e^{-3*tau}, monotonically decreasing  (local)

# Verify ratios at tau=0
assert abs(r12[0] - 1.0) < 1e-14, f"r12(0) = {r12[0]} != 1"
assert abs(r13[0] - 1.0) < 1e-14, f"r13(0) = {r13[0]} != 1"
assert abs(r23[0] - 1.0) < 1e-14, f"r23(0) = {r23[0]} != 1"

print(f"Ratios at tau=0:     r12={r12[0]:.15f}, r13={r13[0]:.15f}, r23={r23[0]:.15f}")
print(f"  (all = 1.0 => bi-invariant metric, maximal symmetry)")
print()

# Ratios at tau_fold
idx_fold = np.argmin(np.abs(tau_arr - tau_fold))  # (local)
print(f"Ratios at tau_fold={tau_fold}:")
print(f"  r12 = L1/L2 = e^{{4*tau}} = {r12[idx_fold]:.6f}")
print(f"  r13 = L1/L3 = e^{{tau}}   = {r13[idx_fold]:.6f}")
print(f"  r23 = L2/L3 = e^{{-3*tau}} = {r23[idx_fold]:.6f}")
print()

# Check: are any ratios = 1 for tau > 0?
eps_tol = 1e-10  # (local)
coincidences_12 = tau_arr[(np.abs(r12 - 1.0) < eps_tol) & (tau_arr > eps_tol)]  # (local)
coincidences_13 = tau_arr[(np.abs(r13 - 1.0) < eps_tol) & (tau_arr > eps_tol)]  # (local)
coincidences_23 = tau_arr[(np.abs(r23 - 1.0) < eps_tol) & (tau_arr > eps_tol)]  # (local)

print(f"Coincidences at tau > 0 (within tol={eps_tol}):")
print(f"  L1=L2: {len(coincidences_12)} found")
print(f"  L1=L3: {len(coincidences_13)} found")
print(f"  L2=L3: {len(coincidences_23)} found")
print()

# =============================================================================
#  Section 4: Subalgebra chain classification
# =============================================================================

print("--- Section 4: Subalgebra Chain Classification ---")
print()
print("su(3) subalgebra chains (Dynkin classification):")
print()

print("Chain A: su(3) -> su(2) + u(1) -> u(1) + u(1)")
print("  Maximal regular subalgebra. Under SU(2) x U(1) ⊂ SU(3):")
print("  Ad(SU(3)) = 8 -> (3,0) + (1,0) + (2,+1) + (2,-1)")
print("  = su(2)[dim 3] + u(1)[dim 1] + C^2[dim 4]")
print("  This IS the Jensen decomposition. Enhanced symmetry: tau=0 only.")
print()

print("Chain B: su(3) -> u(2) = su(2) + u(1)")
print("  Same as Chain A (U(2) is the isotropy subgroup of SU(3)/CP^2).")
print("  The Jensen metric IS the most general Ad(U(2))-invariant metric.")
print()

print("Chain C: su(3) -> so(3) [irreducible embedding]")
print("  5-dimensional representation of SO(3) in SU(3).")
print("  Under this embedding, 8 -> 3 + 5 (adjoint + symmetric traceless).")
print("  The SO(3)-invariant metric is a 2-parameter family (different from Jensen).")
print("  This chain does NOT contain a U(1) factor => no EM-like gauge field.")
print("  Not relevant to Pati-Salam or Standard Model embedding.")
print()

print("Chain D: su(3) -> direct u(1) + u(1) [Cartan subalgebra]")
print("  8 -> (2) adjoint roots + (6) root spaces.")
print("  This gives the KK tower decomposition but no intermediate symmetry.")
print()

# =============================================================================
#  Section 5: Pati-Salam embedding impossibility
# =============================================================================

print("--- Section 5: Pati-Salam Embedding Impossibility ---")
print()
print("Pati-Salam group: SU(4)_C x SU(2)_L x SU(2)_R")
print(f"  dim = 15 + 3 + 3 = 21, rank = 3 + 1 + 1 = 5")
print(f"  SU(3) fiber: dim = 8, rank = 2")
print()
print("Dimensional obstruction:")
print(f"  dim(PS) = 21 > dim(SU(3)) = 8")
print(f"  rank(PS) = 5 > rank(SU(3)) = 2")
print()
print("Neither a Pati-Salam group nor any left-right symmetric extension")
print("SU(2)_L x SU(2)_R x U(1) (dim=7, rank=3) can embed in SU(3) (rank=2).")
print()

# Check: SU(2)_L x SU(2)_R x U(1)
dim_LR = 3 + 3 + 1  # = 7  (local)
rank_LR = 1 + 1 + 1  # = 3  (local)
print(f"Left-Right symmetric: SU(2)_L x SU(2)_R x U(1)")
print(f"  dim = {dim_LR}, rank = {rank_LR}")
print(f"  rank obstruction: {rank_LR} > 2 = rank(SU(3))")
print(f"  => CANNOT embed as subalgebra of su(3)")
print()

# The maximal semisimple subalgebra of su(3) is su(2) + u(1), rank 2
# There is NO way to fit two independent su(2) factors
print("Maximal subalgebras of su(3) [Dynkin, 1952]:")
print("  Regular: su(2) + u(1)  [rank 2]")
print("  Special: so(3)         [rank 1, irreducible embedding]")
print("  No room for SU(2)_L x SU(2)_R — would need rank >= 3.")
print()

# =============================================================================
#  Section 6: Symmetry breaking pattern with tau
# =============================================================================

print("--- Section 6: Symmetry Breaking Pattern ---")
print()

tau_values = [0.0, 0.05, 0.10, 0.15, tau_fold, 0.25, 0.50, 1.00]  # (local)

print(f"{'tau':>8s} | {'L_1':>10s} | {'L_2':>10s} | {'L_3':>10s} | {'L1/L2':>10s} | {'L2/L3':>10s} | {'L1/L3':>10s} | Symmetry")
print("-" * 100)

for t in tau_values:
    L1, L2, L3 = jensen_eigenvalues(t)  # (local)
    r_12 = L1 / L2  # (local)
    r_23 = L2 / L3  # (local)
    r_13 = L1 / L3  # (local)

    if abs(t) < 1e-15:
        sym = "SU(3)_L x SU(3)_R / Z_3 (bi-invariant)"  # (local)
    else:
        sym = "(SU(3) x SU(2) x U(1)) / Z_6 (Jensen)"  # (local)

    print(f"{t:8.4f} | {L1:10.6f} | {L2:10.6f} | {L3:10.6f} | {r_12:10.6f} | {r_23:10.6f} | {r_13:10.6f} | {sym}")

print()

# =============================================================================
#  Section 7: Monotonicity analysis — eigenvalue ratios are strictly monotone
# =============================================================================

print("--- Section 7: Monotonicity of Eigenvalue Ratios ---")
print()

# d/dtau (L1/L2) = d/dtau (e^{4*tau}) = 4*e^{4*tau} > 0 for all tau
# d/dtau (L1/L3) = d/dtau (e^{tau}) = e^{tau} > 0 for all tau
# d/dtau (L2/L3) = d/dtau (e^{-3*tau}) = -3*e^{-3*tau} < 0 for all tau
# ALL ratios are STRICTLY MONOTONE => they pass through 1 exactly once, at tau=0.

dr12_dtau = 4 * np.exp(4 * tau_arr)    # (local) always > 0
dr13_dtau = np.exp(tau_arr)              # (local) always > 0
dr23_dtau = -3 * np.exp(-3 * tau_arr)   # (local) always < 0

print(f"d(L1/L2)/dtau = 4*e^{{4*tau}}:  min = {dr12_dtau.min():.6e} (at tau=0), always > 0")
print(f"d(L1/L3)/dtau = e^{{tau}}:      min = {dr13_dtau.min():.6e} (at tau=0), always > 0")
print(f"d(L2/L3)/dtau = -3*e^{{-3*tau}}: max = {dr23_dtau.max():.6e} (at tau=1), always < 0")
print()

print("All three eigenvalue ratios are STRICTLY MONOTONE for all tau.")
print("Each passes through 1 (= coincidence) exactly once: at tau = 0.")
print("Therefore NO intermediate symmetry enhancement can exist for tau > 0.")
print()

# =============================================================================
#  Section 8: What WOULD be needed for Pati-Salam-type intermediate symmetry
# =============================================================================

print("--- Section 8: What Would Be Required ---")
print()
print("For an intermediate Pati-Salam or L-R symmetric scale between M_KK and M_Z,")
print("one would need EITHER:")
print()
print("  (a) A fiber group G with rank >= 3 containing su(2)_L x su(2)_R x u(1)_B-L")
print("      Examples: SU(4), SO(10), E_6")
print("      SU(3) fails: rank 2 < 3 required.")
print()
print("  (b) A deformation flow tau(mu) where two eigenvalues CROSS at tau_PS != 0,")
print("      creating a temporary symmetry enhancement.")
print("      Jensen flow fails: all ratios strictly monotone, no crossing possible.")
print()
print("  (c) A non-Jensen deformation (e.g., breaking the Ad(U(2)) invariance) that")
print("      introduces new coincidence points.")
print("      This would require abandoning the symmetric space structure SU(3)/U(2).")
print()
print("None of these are available in the M4 x SU(3) framework.")
print()

# =============================================================================
#  Section 9: Connection to W2-D FAIL (Weinberg angle threshold)
# =============================================================================

print("--- Section 9: Connection to W2-D (Weinberg Angle FAIL) ---")
print()
print("W2-D FAIL established: the L-R threshold correction route to sin^2(theta_W)")
print("gives sin^2 = -0.308, permanently closing that mechanism.")
print()
print("This result is CONSISTENT with the present finding:")
print("  - L-R symmetry (SU(2)_L x SU(2)_R) requires rank >= 3.")
print("  - SU(3) fiber has rank 2.")
print("  - Even if we artificially imposed L-R structure, the Jensen flow")
print("    provides no intermediate scale where L-R breaking could occur.")
print("  - The negative sin^2 in W2-D arises precisely because the L-R embedding")
print("    is geometrically impossible in SU(3).")
print()
print("Together, W2-D and the present result close the entire Pati-Salam")
print("intermediate symmetry channel in the SU(3) fiber framework.")
print()

# =============================================================================
#  Section 10: Gate verdict
# =============================================================================

print("=" * 72)
print("GATE: S77-D4-PATI-SALAM (INFO)")
print("=" * 72)
print()
print("Finding: Non-existence of intermediate symmetry enhancement CONFIRMED.")
print()
print("Evidence (three independent arguments):")
print("  1. ANALYTIC: All three eigenvalue ratios L_i/L_j are exponentials of")
print("     linear functions of tau. Each equals 1 iff tau = 0. No other solution.")
print()
print("  2. MONOTONICITY: All ratios are strictly monotone (derivatives are")
print("     sign-definite exponentials). A monotone function crosses any value")
print("     at most once => coincidence at tau=0 only.")
print()
print("  3. RANK OBSTRUCTION: Pati-Salam (rank 5) and L-R symmetric (rank 3)")
print("     groups cannot embed in SU(3) (rank 2). Even without the Jensen")
print("     analysis, the embedding is algebraically impossible.")
print()
print("Verdict: INFO — non-existence confirmed by all three arguments.")
print("         No intermediate symmetry enhancement exists in M4 x SU(3)")
print("         between tau=0 (bi-invariant) and tau=tau_fold.")
print()
print("Structural implication: The SM gauge group (SU(3)_c x SU(2)_L x U(1)_Y)")
print("  as embedded via (SU(3) x SU(2) x U(1))/Z_6 isometry is the UNIQUE")
print("  gauge content for tau > 0. There is no 'desert' with different gauge")
print("  symmetry between M_KK and M_Z — the gauge group is fixed by geometry")
print("  at the moment tau departs from zero.")
print()

# =============================================================================
#  Save data
# =============================================================================

npz_path = r"C:\sandbox\Ainulindale Exflation\computations\s77_pati_salam_embed.npz"  # (local)

np.savez(npz_path,
         tau_arr=tau_arr,
         L1_arr=L1_arr,
         L2_arr=L2_arr,
         L3_arr=L3_arr,
         r12=r12,
         r13=r13,
         r23=r23,
         dr12_dtau=dr12_dtau,
         dr13_dtau=dr13_dtau,
         dr23_dtau=dr23_dtau,
         tau_fold=np.array([tau_fold]),
         coincidences_12_count=np.array([len(coincidences_12)]),
         coincidences_13_count=np.array([len(coincidences_13)]),
         coincidences_23_count=np.array([len(coincidences_23)]),
         # Summary flags
         intermediate_symmetry_exists=np.array([False]),
         pati_salam_embeds=np.array([False]),
         LR_symmetric_embeds=np.array([False]),
         )

print(f"Data saved to: {npz_path}")
print()
print("DONE.")
