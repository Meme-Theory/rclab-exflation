---
name: heat-kernel-validity-tiers
description: Classification of heat kernel computations by validity on finite discrete spectrum (S45 audit). Determines which spectral quantities are exact, approximate, or artifact on the truncated SU(3) Dirac spectrum.
type: project
---

## Heat Kernel Validity Audit (HEAT-KERNEL-AUDIT-45)

**Why:** Multiple S44-S45 computations applied continuum heat kernel formulas to the 992-level truncated Dirac spectrum. The finite spectrum has fundamentally different analytic structure (entire zeta, convergent Taylor, d_s->0 as sigma->0) from the continuum (meromorphic zeta, asymptotic SD expansion, d_s->8).

**Three tiers established:**

1. **VALID (exact):** Spectral action S(Lambda), heat trace K(sigma), spectral zeta moments at any s
2. **APPROXIMATION:** SD coefficients a_0/a_2/a_4 (converge as max_pq_sum -> inf, ~30-50% truncation error for a_2), G_N extraction
3. **ARTIFACT:** Spectral dimension d_s(sigma) in UV regime (goes to 0 not 8), analytic torsion T (extensive in N, diverges with truncation, T~10^20301 is unphysical), any quantity requiring zeta poles

**How to apply:**
- d_s and torsion routes to CC: CLOSED (artifact, not just failed)
- Use Weyl counting d_Weyl=6.81 instead of d_s for dimension
- Spectral action monotonicity theorem (CUTOFF-SA-37) is Tier 1 -- unaffected
- CC gap computations using a_0, a_2 have ~50% error but qualitative conclusion (120-order gap) survives
- DIMFLOW-44 and SIGMA-SELECT-45: search for "walking sigma" is structurally ill-posed on finite crystal
- TRUNCATED-TORSION-45 (T_singlet=0.147) is less severe artifact but still partial sum

**Key numerical evidence:**
- K(0) = 6440 (finite, not divergent)
- d_s(sigma=1e-4) = 0.0005 (should be 8 on continuum)
- d_s overshoots to 15+ at sigma~10 (impossible on continuum)
- Taylor expansion converges to machine epsilon at 20 terms (not asymptotic)
- Moment ratios A_{2(n+1)}/A_{2n} -> lambda_max^2 = 4.25 (not curvature-related)

**S46 UPDATE (A2-GEOMETRIC-46):** The "~30-50% truncation error for a_2" in Tier 2 was incorrect. The project's "spectral a_2" = zeta_D(1) = 2776.17 is NOT the Seeley-DeWitt coefficient a_2^{SD} = 0.728. They are structurally different objects (ratio = 3812). The spectral zeta function zeta_D(s) has a pole at s=1 for d=8, so zeta_D(1) diverges on the full continuum spectrum. On the truncated spectrum it converges but is UV-dominated (grows with Lambda_max^6). The M_KK extraction formula uses zeta_D(1) correctly as the spectral moment; calling it "a_2" is a naming convention, not a claim that it equals the SD coefficient. Tier 2 should read: "SD coefficients are O(1) geometric quantities (a_2^{SD} = 0.728); the spectral sums called 'a_2' in the project are spectral zeta moments (different objects). G_N extraction uses the moments consistently."
