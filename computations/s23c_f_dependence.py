"""
Session 23c: Analysis of f-dependence in beta/alpha
====================================================

Addresses baptista's question: Does beta/alpha depend on the spectral
action test function f? If so, what is the BF impact?

Author: KK Theorist (Session 23c)
Date: 2026-02-20
"""

import numpy as np

print("=" * 60)
print("f-DEPENDENCE ANALYSIS: beta/alpha in spectral action")
print("=" * 60)
print()

# ======================================================================
# THE SPECTRAL ACTION EXPANSION
# ======================================================================

print("SPECTRAL ACTION EXPANSION on M^4 x K (D=12):")
print()
print("S = Tr(f(D_P^2 / Lambda^2))")
print("  ~ f_0 Lambda^12 a_0 + f_2 Lambda^10 a_2 + f_4 Lambda^8 a_4 + ...")
print()
print("where f_k = integral f(u) u^(5-k) du  (for D=12)")
print()

# ======================================================================
# WHAT GENERATES alpha AND beta
# ======================================================================

print("ALPHA (EH coefficient):")
print("  From a_2: alpha = f_2 Lambda^10 Vol_K R_K(tau) / (6 (4pi)^6)")
print("  [Actually: alpha is the tau-INDEPENDENT piece = f_2 Lambda^10 Vol_K / (6 (4pi)^6)]")
print("  [The R_K(tau) piece is the modulus POTENTIAL from a_2]")
print()

print("BETA (flux coefficient) -- THREE SCENARIOS:")
print()

print("SCENARIO A: beta from spectral action a_4")
print("  beta arises from the a_4 heat kernel coefficient on M^4 x K.")
print("  The mixed Riemann components R_{mu a nu b} generate |F|^2 terms,")
print("  which after fiber averaging contain |omega_3|^2 contributions.")
print()
print("  In this case:")
print("    beta = f_4 Lambda^8 * [geometric integral] / (4pi)^6")
print("    beta/alpha = (f_4/f_2) * (1/Lambda^2) * [geom ratio]")
print()
print("  f-DEPENDENT: YES. Depends on f_4/f_2 and Lambda^2.")
print("  Can f_4/f_2 be determined?")
print("    - For f = characteristic function chi_{[0,1]}: f_4/f_2 = 1")
print("    - For f = Gaussian exp(-x): f_k = Gamma(6-k), f_4/f_2 = Gamma(2)/Gamma(4) = 1/6")
print("    - For general f: free parameter")
print()
print("  HOWEVER: In Connes-Chamseddine NCG, the SM Lagrangian requires")
print("  specific RATIOS of f_k to reproduce the correct relative normalizations")
print("  of the EH, YM, and Higgs terms. This constrains f_4/f_2 to a narrow range.")
print("  The constraint comes from: alpha_strong/alpha_EM at unification scale.")
print()
print("  BF assessment: 5-15 (one partially constrained parameter)")
print()

print("SCENARIO B: beta from topological (Chern-Simons) term")
print("  The Cartan 3-form omega_3 on SU(3) is related to the Chern-Simons 3-form")
print("  of the canonical connection. A topological term integral H_3 ^ *H_3 in the")
print("  12D action has a QUANTIZED coefficient (integer n).")
print()
print("  In this case:")
print("    beta = n * [topological normalization]")
print("    beta/alpha = n / (f_2 Lambda^10 Vol_K / (6(4pi)^6))")
print()
print("  f-DEPENDENT: YES (through alpha). But n is discrete.")
print("  If n=1 is required by consistency, beta/alpha has ONE continuous free param")
print("  (the combination f_2 Lambda^10).")
print()
print("  BF assessment: 3-10 (topological quantization helps)")
print()

print("SCENARIO C: beta from geometry alone (most optimistic)")
print("  In Freund-Rubin (Paper 10), the 4-form flux F_4 = c * vol_K is the")
print("  unique harmonic form on K. Its coefficient c is determined by the")
print("  11D equations of motion with no free parameters.")
print("  The analog in 12D: the 3-form flux omega_3 on SU(3) is the UNIQUE")
print("  bi-invariant 3-form (up to normalization). Its contribution to the")
print("  potential is fixed by the geometry of (SU(3), g_Jensen).")
print()
print("  For this to work in the spectral action, the flux term must arise")
print("  from D_P^2 in a way that the f-dependence CANCELS in beta/alpha.")
print("  This happens IF both alpha and beta come from the SAME a_k coefficient")
print("  (e.g., both from a_2, or both from a_4).")
print()
print("  If alpha and beta both come from a_2:")
print("    alpha = f_2 Lambda^10 * [geom_1]")
print("    beta = f_2 Lambda^10 * [geom_2]")
print("    beta/alpha = [geom_2]/[geom_1] = pure geometry")
print()
print("  This is possible if the flux contribution arises from the R_P")
print("  decomposition in a_2, not from a_4. Specifically:")
print("    R_P = R_M + R_K - |A|^2 + |S|^2 + |N|^2  (submersion formula)")
print("  The cross terms could generate flux-like contributions at the a_2 level.")
print()
print("  BF assessment: 50-100 (zero free parameters)")
print()

# ======================================================================
# THE DECISIVE QUESTION
# ======================================================================

print("=" * 60)
print("THE DECISIVE QUESTION FOR SESSION 24")
print("=" * 60)
print()
print("Does the flux term beta * |omega_3|^2 in the FR potential arise from:")
print("  (A) The a_4 coefficient  => beta/alpha depends on f_4/(f_2 Lambda^2)")
print("  (B) A topological term   => beta/alpha depends on n/(f_2 Lambda^10)")
print("  (C) The a_2 coefficient  => beta/alpha = pure geometry")
print()
print("The answer determines the Bayes factor:")
print("  (A) => BF = 5-15    (one constrained parameter)")
print("  (B) => BF = 3-10    (topological + one continuous)")
print("  (C) => BF = 50-100  (zero free parameters)")
print()

# ======================================================================
# WHAT WE CAN SAY NOW
# ======================================================================

print("WHAT WE CAN DETERMINE NOW (without Session 24 computation):")
print()
print("The Baptista framework (Paper 15) writes the 4D action from the 12D EH:")
print("  S_12D = integral R_P dvol_P")
print()
print("After fiber integration (Baptista eq 3.28):")
print("  L = R_M - |d phi|^2 - 5|d psi|^2 - V(phi, psi)")
print()
print("V(phi, psi) contains ONLY R_K(psi). There is NO |omega_3|^2 term")
print("in the CLASSICAL (tree-level) Baptista action.")
print()
print("The |omega_3|^2 term enters ONLY through:")
print("  1. The CW 1-loop correction (eq 3.87) -- CLOSED (Session 18)")
print("  2. An ADDITIONAL term in the 12D action beyond EH")
print("     (e.g., R^2 gravity, Chern-Simons, or spectral action a_4)")
print()
print("CONCLUSION: In the pure EH framework, beta = 0 and there is NO FR")
print("double-well. The flux term REQUIRES going beyond EH -- either to")
print("R^2 gravity or to the spectral action.")
print()
print("In the SPECTRAL ACTION, both alpha (from a_2) and the modulus potential")
print("(from a_2 + a_4) arise from the same operator D_P^2. The question is")
print("whether the |omega_3|^2 structure emerges from a_4 with an f-dependent")
print("coefficient, or from the a_2 submersion decomposition with an")
print("f-independent coefficient.")
print()
print("THIS IS THE KEY COMPUTATION FOR SESSION 24.")
