"""
Session 23c: 2x2 Moment System for f_4/(f_8 Lambda^4)
======================================================

CORRECTION to s23c_moment_mapping.py:
Baptista identified that the submersion formula R_P = R_M + R_K - |F|^2 - ...
means the a_2 coefficient (moment f_8 Lambda^8) ALSO contributes to the gauge
kinetic term, not just a_4. The 4D effective action receives gauge contributions
from BOTH 12D a_2 and a_4.

The correct structure is a 2x2 LINEAR SYSTEM:

  [A  B] [f_8 Lambda^8]   [pi^2/(2 g_3^2)]     (gauge coupling)
  [C  D] [f_4 Lambda^4] = [6/(kappa^2 Vol_4)]   (Newton's constant)

where A, B, C, D are fiber integrals over (SU(3), g_Jensen(tau)).

If det(M) != 0, both f_8 Lambda^8 and f_4 Lambda^4 are UNIQUELY determined,
and beta/alpha becomes a zero-parameter prediction.

Author: KK Theorist (Session 23c)
Date: 2026-02-20
"""

import numpy as np

print("=" * 70)
print("2x2 MOMENT SYSTEM: Corrected f-dependence analysis")
print("=" * 70)
print()

# ======================================================================
# THE 12D SPECTRAL ACTION: FULL STRUCTURE
# ======================================================================

print("12D SPECTRAL ACTION ON M^4 x (SU(3), g_Jensen(tau))")
print("=" * 50)
print()
print("S = Tr(f(D_P^2 / Lambda^2))")
print("  = ... + f_8 Lambda^8 (4pi)^{-6} int a_2 dvol_P")
print("        + f_4 Lambda^4 (4pi)^{-6} int a_4 dvol_P + ...")
print()

# ======================================================================
# a_2 DECOMPOSITION (submersion formula)
# ======================================================================

print("a_2 COEFFICIENT (from R_P, submersion formula):")
print("-" * 50)
print()
print("a_2 = (1/6) int_P R_P dvol_P")
print()
print("R_P = R_M + R_K(tau) - |F|^2 - |S'|^2 + (1-1/k)|N|^2 + div")
print()
print("After fiber integration at the KK ansatz level:")
print()
print("  a_2 -> (1/6) Vol_K [R_M term]                      (4D EH)")
print("       + (1/6) [int_K R_K dvol_K] [Vol_M4 term]      (4D CC from fiber)")
print("       - (1/6) [int_K g_{ab} dvol_K] |F|^2_M          (4D YM from a_2)")
print("       - (1/6) [kinetic terms] |dpsi|^2_M              (4D scalar kinetic)")
print()
print("KEY: The -|F|^2 piece of R_P generates a gauge kinetic contribution")
print("in a_2, proportional to f_8 Lambda^8!")
print()

# ======================================================================
# a_4 DECOMPOSITION (Gilkey formula on product-type geometry)
# ======================================================================

print("a_4 COEFFICIENT (Gilkey on 12D):")
print("-" * 50)
print()
print("a_4 = int_P [c1 R_P^2 + c2 |Ric_P|^2 + c3 |Riem_P|^2 + ...] dvol_P")
print()
print("After fiber integration, the mixed terms R_{mu a nu b}^2 generate:")
print("  a_4 -> ... + [mixed fiber integral] |F|^2_M          (4D YM from a_4)")
print("             + [flux fiber integral] |omega_3|^2        (4D flux potential)")
print("             + [pure fiber integral] (4D scalar potential correction)")
print()

# ======================================================================
# THE 2x2 SYSTEM
# ======================================================================

print("THE 2x2 SYSTEM")
print("=" * 50)
print()
print("Denote x = f_8 Lambda^8, y = f_4 Lambda^4. The 4D effective action has:")
print()
print("  Gauge kinetic: (1/(4 g_3^2)) |F|^2 = [A*x + B*y] |F|^2")
print("  Einstein-Hilbert: (1/(2 kappa^2)) R = [C*x + D*y] R")
print()
print("where:")
print("  A = fiber integral of |F|^2 piece from a_2 / (6 (4pi)^6)")
print("    = (1/6) (4pi)^{-6} int_K g_{ab}(tau) dvol_K")
print("  B = fiber integral of |F|^2 piece from a_4 / (4pi)^6")
print("    = (4pi)^{-6} int_K [mixed Riem^2 coefficient] dvol_K")
print("  C = fiber integral of R_M piece from a_2 / (6 (4pi)^6)")
print("    = (1/6) (4pi)^{-6} Vol_K")
print("  D = fiber integral of R_M piece from a_4 / (4pi)^6")
print("    = (4pi)^{-6} int_K [R_K-dependent correction to EH] dvol_K")
print()
print("Physical constraints:")
print("  A*x + B*y = 1/(4 g_3^2)     ... (I)  gauge coupling")
print("  C*x + D*y = 1/(2 kappa^2)   ... (II) Newton's constant")
print()

# ======================================================================
# WHAT ARE A, B, C, D?
# ======================================================================

print("FIBER INTEGRALS: What can we compute now?")
print("=" * 50)
print()

# Load data
base = "C:/sandbox/Ainulindale Exflation/tier0-computation"
d = np.load(f"{base}/r20a_riemann_tensor.npz")
tau_data = d['tau']
R_K_data = d['R_scalar']
Ric_data = d['Ric']
K_data = d['K']
n_tau = len(tau_data)
Ric_sq_data = np.array([np.sum(Ric_data[i]**2) for i in range(n_tau)])

# A: the gauge kinetic contribution from a_2
# This is the fiber integral of g_{ab} over K, contracted with the
# structure constants to form |F|^2. For the Kerner decomposition,
# -|F|^2 in R_P involves g_{ab}(tau) the internal metric.
# On SU(3) with Jensen metric, the gauge kinetic normalization is
# int_K g_{ab} K_alpha^a K_beta^b dvol_K / Vol_K = delta_{alpha beta} * [gauge norm]
# This is EXACTLY the gauge coupling derivation from Session 17a!

print("A (gauge from a_2): Related to the gauge coupling derivation g_1/g_2 = e^{-2tau}")
print("  The |F|^2 in R_P uses the internal metric g_{ab}(tau).")
print("  For the U(1) factor: g_11(tau) = e^{2tau} => A_U1 ~ e^{2tau}")
print("  For the SU(2) factor: g_22(tau) = e^{-2tau} => A_SU2 ~ e^{-2tau}")
print("  For the SU(3) factor (full): mixed contributions")
print("  The KNOWN result: g_1/g_2 = e^{-2tau} (Session 17a, proven)")
print("  This means A propto g_{ab}(tau) which is tau-DEPENDENT but KNOWN.")
print()

print("C (EH from a_2): This is the trivial piece.")
print("  C = Vol_K / (6 (4pi)^6)")
print("  Vol_K = 12.54 (constant, volume-preserving Jensen)")
print("  C is tau-INDEPENDENT.")
print()

# B: the gauge kinetic contribution from a_4
# This is the hard one — requires the mixed R_{mu a nu b}^2 computation.
print("B (gauge from a_4): REQUIRES SESSION 24 COMPUTATION")
print("  This involves the mixed Riemann tensor components R_{mu a nu b}")
print("  after KK reduction. The Kerner decomposition gives")
print("  R_{mu a nu b} = (1/2) F_{mu nu}^c Gamma_{cab}")
print("  where Gamma_{cab} are the Christoffel symbols on the fiber.")
print("  The fiber integral of |R_{mu a nu b}|^2 involves a DIFFERENT")
print("  contraction of the fiber metric than A.")
print()

print("D (EH from a_4): Also requires Session 24")
print("  Correction to EH from a_4 involves R_K^2 type terms")
print("  integrated over the fiber. These give tau-dependent corrections")
print("  to Newton's constant.")
print()

# ======================================================================
# STRUCTURE OF THE 2x2 MATRIX
# ======================================================================

print("STRUCTURE OF THE 2x2 MATRIX")
print("=" * 50)
print()
print("M = [[A(tau), B(tau)],")
print("     [C,      D(tau)]]")
print()
print("Properties:")
print("  - C is tau-independent (Vol_K is constant)")
print("  - A, B, D are tau-dependent")
print("  - A is KNOWN from Session 17a (gauge coupling derivation)")
print("  - B is UNKNOWN (Session 24 computation)")
print("  - D is partially known from our Gilkey a_4 computation")
print()

# ======================================================================
# INVERTIBILITY CHECK
# ======================================================================

print("INVERTIBILITY: When does det(M) = 0?")
print("-" * 50)
print()
print("det(M) = A*D - B*C")
print()
print("det = 0 requires A*D = B*C, i.e., A/C = B/D")
print("  A/C = [gauge fiber integral from a_2] / [Vol_K]")
print("  B/D = [gauge fiber integral from a_4] / [EH fiber integral from a_4]")
print()
print("These are DIFFERENT ratios because:")
print("  A/C involves g_{ab}(tau) (the metric on K)")
print("  B/D involves R_{abcd}(tau) contracted with the gauge connection")
print()
print("For det = 0, these two DIFFERENT geometric quantities would have to")
print("be EXACTLY equal. This is a fine-tuned coincidence with no algebraic reason.")
print("=> det(M) != 0 generically. The system IS invertible.")
print()

# ======================================================================
# HIERARCHY ANALYSIS
# ======================================================================

print("HIERARCHY ANALYSIS: Which contribution dominates?")
print("=" * 50)
print()
print("The a_2 contributions come with factor f_8 Lambda^8.")
print("The a_4 contributions come with factor f_4 Lambda^4.")
print()
print("If Lambda >> 1 (in appropriate units), then f_8 Lambda^8 >> f_4 Lambda^4")
print("(assuming f_8/f_4 ~ O(1), which is true for most test functions f).")
print()
print("This means:")
print("  - In the gauge sector: A*x >> B*y => gauge coupling dominated by a_2")
print("  - In the EH sector: C*x >> D*y => Newton's constant dominated by a_2")
print()
print("If both are a_2-dominated, the system degenerates:")
print("  A*x ~ 1/(4g_3^2) and C*x ~ 1/(2kappa^2)")
print("  => A/C = kappa^2/(2g_3^2) (one constraint on fiber geometry)")
print("  and x = f_8 Lambda^8 is determined, but y = f_4 Lambda^4 is UNCONSTRAINED!")
print()
print("This is the WORST CASE: f_4 Lambda^4 is free, beta/alpha has one free param.")
print("BF = 5-15 (back to Scenario A without mapping).")
print()
print("HOWEVER: If there is a HIERARCHY INVERSION in one sector...")
print("  If A is suppressed (small gauge contribution from a_2) while C is not,")
print("  then the gauge coupling constrains f_4 Lambda^4 through B*y,")
print("  while Newton's constant constrains f_8 Lambda^8 through C*x.")
print("  This gives the clean-separation result.")
print()

# ======================================================================
# PHYSICAL CHECK: IS A SUPPRESSED?
# ======================================================================

print("PHYSICAL CHECK: Is A naturally small?")
print("=" * 50)
print()
print("A comes from the -|F|^2 term in R_P.")
print("The Kerner decomposition (Paper 06, eq 26-30) gives:")
print("  R_P = R_M + R_K + (1/4) g_{ab} F^a_{mu nu} F^{b mu nu}")
print()
print("The coefficient of |F|^2 in R_P is:")
print("  (1/4) int_K g_{ab}(tau, y) dvol_K(y)")
print()
print("For the Killing metric (tau = 0, bi-invariant):")
print("  g_{ab} = (1/12) delta_{ab} (Killing form normalization)")
print("  int_K g_{ab} dvol_K = (1/12) delta_{ab} Vol_K")
print()
print("For the Jensen-deformed metric:")
print("  g is diagonal in the U(1)/SU(2)/C^2 decomposition")
print("  g_11 = e^{2tau}, g_22 = e^{-2tau} (3x3), g_33 = e^{tau} (4x4)")
print("  int_K g_{ab} dvol_K = block-diagonal in these sectors")
print()
print("The KEY QUESTION: What is A/C numerically?")
print()

# Compute A/C ratio
# C = Vol_K / (6 (4pi)^6)
# A = (1/6) (4pi)^{-6} <g_{ab}(tau)>_K where <> means volume average
# A/C = <g_{ab}(tau)>_K / Vol_K (per gauge index pair)
# For the full trace: sum_a g_{aa} = e^{2tau} + 3*e^{-2tau} + 4*e^{tau}
# At tau = 0: trace = 1 + 3 + 4 = 8 (= dim SU(3))

def trace_g(tau):
    return np.exp(2*tau) + 3*np.exp(-2*tau) + 4*np.exp(tau)

print("Trace of g_Jensen(tau) (= gauge kinetic normalization):")
for t in [0.0, 0.3, 0.5, 1.0]:
    print(f"  tau = {t:.1f}: tr(g) = {trace_g(t):.4f}")
print()
print("At tau = 0: tr(g) = 8 (= dim K). This is O(1).")
print("C = Vol_K / 6 = 12.54/6 = 2.09")
print("A (trace) = tr(g) / 6 ~ 8/6 = 1.33 (at tau=0)")
print()
print("A/C = tr(g)/Vol_K ~ 8/12.54 = 0.638")
print()
print("A and C are the SAME ORDER OF MAGNITUDE!")
print("=> No hierarchy inversion. Both sectors are a_2-dominated.")
print("=> The 2x2 system DEGENERATES in the large-Lambda limit.")
print()

# ======================================================================
# THE SUBTLE POINT: a_4 GAUGE CONTRIBUTION IS GENUINELY DIFFERENT
# ======================================================================

print("BUT WAIT: a_4 gauge contribution is a DIFFERENT INVARIANT")
print("=" * 50)
print()
print("The a_2 gauge term comes from g_{ab} F^a F^b (metric contraction).")
print("The a_4 gauge term comes from R_{mu a nu b} R^{mu a nu b} which involves")
print("Christoffel symbols Gamma^c_{ab} = (1/2) f^c_{ab} + ... (Lie group).")
print()
print("In the Kerner decomposition:")
print("  R_{mu a nu b} = (1/2) nabla_mu A_nu^c * f_{cab} + ...")
print()
print("After squaring and fiber integration:")
print("  a_4 gauge term ~ int_K Gamma^c_{ab} Gamma^d_{ef} g^{ae} g^{bf} dvol_K * |F|^2")
print("  This involves STRUCTURE CONSTANTS, not just the metric!")
print()
print("So B/D involves different geometric invariants from A/C.")
print("The 2x2 system IS non-degenerate in principle.")
print()
print("BUT: The HIERARCHY f_8 Lambda^8 >> f_4 Lambda^4 means the a_4")
print("contributions are SUPPRESSED by Lambda^{-4} relative to a_2.")
print("At the practical level, the a_4 corrections to gauge coupling and")
print("Newton's constant are TINY perturbations of the a_2-dominated values.")
print()

# ======================================================================
# FINAL ASSESSMENT
# ======================================================================

print("=" * 70)
print("FINAL ASSESSMENT: 2x2 SYSTEM STRUCTURE")
print("=" * 70)
print()
print("The 2x2 system M * [x, y]^T = [gauge, gravity]^T has the structure:")
print()
print("  M = [[A, B], [C, D]]")
print()
print("where A ~ C ~ O(Vol_K) and B ~ D ~ O(fiber_integrals).")
print("The moments are x = f_8 Lambda^8, y = f_4 Lambda^4.")
print()
print("CASE 1: Lambda >> Lambda_GUT")
print("  x >> y (assuming f_8/f_4 ~ O(1))")
print("  System is a_2-dominated: A*x ~ gauge, C*x ~ gravity")
print("  y is UNCONSTRAINED => beta/alpha has one free parameter")
print("  BF = 5-15")
print()
print("CASE 2: Lambda ~ Lambda_GUT (the natural scale)")
print("  x and y are comparable (Lambda^4 difference compensated by f_8/f_4)")
print("  Full 2x2 system needed. det(M) generically nonzero.")
print("  y is determined => beta/alpha is a zero-parameter prediction")
print("  BF = 30-70")
print()
print("CASE 3: Lambda << Lambda_GUT")
print("  Unphysical (Lambda must be >= GUT scale for the spectral action")
print("  to reproduce the SM at low energies)")
print()
print("THE DECISIVE QUESTION:")
print("What is the relationship between Lambda (UV cutoff) and the")
print("GUT unification scale? If Lambda = Lambda_GUT (the minimal choice),")
print("then f_8 Lambda^4 ~ f_8/f_4 * y, and the ratio f_8/f_4 must be O(1)")
print("for the expansion to make sense. In this case, x and y ARE comparable,")
print("and the full 2x2 system applies.")
print()
print("In Connes-Chamseddine, Lambda IS the unification scale:")
print("  Lambda = Lambda_GUT ~ 10^{16} GeV")
print("  f_k are O(1) dimensionless numbers")
print("  The hierarchy f_8 Lambda^8 >> f_4 Lambda^4 does NOT hold")
print("  because the Lambda factors are ALREADY INCLUDED in the moments!")
print()
print("CORRECTION: In the spectral action S = Tr(f(D^2/Lambda^2)):")
print("  The expansion is sum f_{D-2k} Lambda^{D-2k} a_k")
print("  where f_n = int f(u) u^{(n-1)/2} du are DIMENSIONLESS moments.")
print("  f_8 Lambda^8 vs f_4 Lambda^4 means f_8 * Lambda^8 vs f_4 * Lambda^4.")
print("  With Lambda ~ 10^16 GeV, Lambda^8/Lambda^4 = Lambda^4 ~ 10^64.")
print("  So x >> y UNLESS f_4 >> f_8 * Lambda^4, which is unphysical.")
print()
print("WAIT — re-reading the conventions...")
print("  Actually: f_n are n-th MOMENTS of f, defined as:")
print("  f_n = int_0^infty f(u) u^{(n/2-1)} du  (Connes convention)")
print("  For a test function f with f(u) ~ 1 for u < 1 and f(u) ~ 0 for u >> 1:")
print("  f_n ~ 1/(n/2) for all n (all moments are O(1))")
print()
print("  So f_8 ~ f_4 ~ O(1) and:")
print("  f_8 Lambda^8 / (f_4 Lambda^4) ~ Lambda^4 ~ 10^64 (in GeV)")
print()
print("  => The a_2 contribution DOMINATES by 64 orders of magnitude!")
print("  => The a_4 contribution to gauge coupling is NEGLIGIBLE.")
print("  => Baptista's A contamination threat is REAL but TINY.")
print("  => In practice, f_8 Lambda^8 is fixed by BOTH gauge and gravity from a_2.")
print("  => f_4 Lambda^4 is unconstrained by the leading-order equations.")
print()
print("=" * 70)
print("REVISED CONCLUSION")
print("=" * 70)
print()
print("1. At leading order (Lambda^8 terms): a_2 fixes f_8 Lambda^8 from")
print("   BOTH gauge coupling AND Newton's constant. These give ONE constraint")
print("   on f_8 Lambda^8 and a consistency check (A/C = g_3^2 kappa^2 / 2).")
print()
print("2. At subleading order (Lambda^4 terms): a_4 enters as a CORRECTION.")
print("   f_4 Lambda^4 is constrained only if the a_4 correction is large enough")
print("   to be measured. In practice, it is suppressed by Lambda^{-4} ~ 10^{-64}.")
print()
print("3. UNLESS there is a CANCELLATION in the a_2 gauge term.")
print("   If the gauge contribution from a_2 vanishes at some special tau")
print("   (e.g., because tr(g_Jensen) = 0 at some tau — but this never happens),")
print("   then a_4 becomes the leading gauge term and fixes f_4 Lambda^4.")
print()
print("4. BOTTOM LINE: f_4 Lambda^4 is NOT fixed by CCM constraints in the")
print("   standard spectral action framework. beta/alpha has ONE free parameter.")
print("   BF = 5-15.")
print()
print("5. THE ESCAPE: If the framework provides an INDEPENDENT constraint on")
print("   f_4/(f_8 Lambda^4) — for example, from the NCG spectral triple or")
print("   from a deeper principle — then beta/alpha becomes predictive.")
print("   This requires going BEYOND the standard spectral action.")
print()
print("SESSION 24 PRIORITY:")
print("  - Compute A/C ratio explicitly (consistency check between g_3 and G_N)")
print("  - This is the GAUGE-GRAVITY UNIFICATION CONDITION from SU(3) geometry")
print("  - If A/C matches kappa^2/(2g_3^2), the framework is self-consistent")
print("  - beta/alpha remains the ONE free parameter (BF = 5-15)")
print("  - Any additional constraint on f_4/(f_8 Lambda^4) is a BONUS")
