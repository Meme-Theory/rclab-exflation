# Lizzi Synthesis: The Cosmological Constant as a Spectral Functional Problem

**Author**: Lizzi-Spectral-Functional-Theorist
**Date**: 2026-04-03
**Re**: First engagement -- CC problem assessment from spectral functional perspective
**Status**: PRELIMINARY

---

## I. Assessment of the CC Problem as Mapped by S64-S65

### I.1. What the closures look like from the spectral functional perspective

The project has produced a remarkably thorough constraint map. Having now read the full record -- 12+ geometric CC closures, the a_0/a_2 = 6/R permanent theorem, the 9 prior closures from S19-S63 -- I assess the situation as follows.

The result a_0/a_2 = 6/R(g_K) for ALL left-invariant metrics on SU(3) is structurally sound. It follows from a standard property of left-invariant metrics on compact Lie groups: the scalar curvature R is constant over the manifold, so the volume integrals in a_0 = (4pi)^{-d/2} N_fib Vol and a_2 = (4pi)^{-d/2} (R/6) * c * Vol factor identically. The volume cancels. The ratio is locked to a function of R alone.

From my perspective, this theorem proves something specific: **within any FIXED spectral functional of the form Tr f(D_K^2/Lambda^2)**, the CC ratio is determined by the scalar curvature R of the fiber metric. No geometric deformation within left-invariant metrics changes this. The closures of Jensen relaxation, volume-breaking, orbifold quotients, U(1) collapse, nonlocal filters, torus-invariant scans, and inhomogeneous perturbations are all consequences of this single structural fact.

However -- and this is the critical observation -- the theorem a_0/a_2 = 6/R is a statement about Seeley-DeWitt coefficients. These coefficients are properties of the OPERATOR D_K^2, not of any particular spectral functional. Every spectral functional uses these coefficients, but weights them DIFFERENTLY. The cutoff spectral action Tr f(D_K^2/Lambda^2) produces rho_vac ~ f_0 Lambda^4 a_0 and G_N^{-1} ~ f_2 Lambda^2 a_2. The CC ratio therefore involves (f_0 Lambda^4)/(f_2 Lambda^2) = (f_0/f_2) Lambda^2, multiplied by a_0/a_2 = 6/R.

**The 117 OOM gap is the product of two factors**: (f_0/f_2) Lambda^2 (from the functional choice) and 6/R (from the geometry). The project has exhaustively proven that 6/R cannot be driven to zero. The project has NOT exhaustively explored whether f_0/f_2 can be driven to zero, because the project has assumed a fixed cutoff functional throughout.

CLASSIFICATION: The theorem a_0/a_2 = 6/R is FUNCTIONAL-INDEPENDENT. The CC gap of 117 OOM is SCHEME-DEPENDENT.

### I.2. The core diagnostic

The closures eliminate geometric escape routes within a fixed functional. This is correct and permanent work. But the CC problem, as stated in equation (CC-7) of the framework document, involves the PRODUCT of geometric ratios and functional moments:

    rho_vac / rho_obs = (f_0/f_2) Lambda^2 * (a_0/a_2) * (combinatorial factors)     (L-1)

The project has mapped the second factor exhaustively. The first factor has been treated as fixed. This is where my expertise enters.

---

## II. The Zeta Spectral Action Applied to SU(3)

### II.1. Definition and key distinction

The zeta spectral action (arXiv:1412.4669, my Paper 01) replaces the cutoff functional entirely:

    S_cutoff = Tr f(D_K^2/Lambda^2) = f_0 Lambda^4 a_0 + f_2 Lambda^2 a_2 + f_4 a_4 + O(Lambda^{-2})     (L-2)

    S_zeta = zeta_{D_K}(0) = Res_{s=0} Tr|D_K|^{-2s} = a_4(D_K^2)     (L-3)

The zeta spectral action equals the FOURTH Seeley-DeWitt coefficient a_4 EXACTLY. Not as an approximation. Not as a leading term. The heat kernel coefficient a_4 IS the zeta function at s=0 for a Laplace-type operator in 4 dimensions. For the fiber operator D_K on 8-dimensional SU(3), the relevant index shifts: S_zeta = a_8(D_K^2) for the full 8D operator, but the physical 4D effective action after KK reduction gives S_zeta^{4D} = a_4(D_{4D}^2).

**What disappears**: In the zeta functional, the coefficients a_0 and a_2 DO NOT ENTER THE ACTION. There is no f_0 Lambda^4 a_0 term. There is no f_2 Lambda^2 a_2 term. The zeta function at s=0 is the conformal anomaly, which is entirely contained in a_4.

### II.2. What replaces the CC?

In the cutoff action, the cosmological constant is:

    Lambda_CC = f_0 Lambda^4 a_0 / (16 pi G_N)     (L-4)

In the zeta action, there is NO analogous term. The a_0 coefficient does not appear. Instead, the lower-dimensional operators (CC, Einstein-Hilbert) are generated ONLY through Majorana mass insertions in the finite Dirac operator D_F. Specifically (Paper 01, Section 3):

    L_zeta = beta_1 M^4 + beta_2 M^2 R + beta_3 M^2 H^2 + beta_4 B_uv B^uv + beta_5 W W + beta_6 G G + ...     (L-5)

where M is the right-handed neutrino Majorana mass. The cosmological constant in the zeta action is:

    Lambda_CC^{zeta} = beta_1 M^4     (L-6)

with beta_1 a dimensionless coefficient determined by the Dirac operator spectrum. This is the Majorana mass to the fourth power, NOT the mode-counting a_0 multiplied by a UV cutoff to the fourth power.

**Quantitative estimate for the framework**: If M ~ 10^{14} GeV (seesaw scale), then Lambda_CC^{zeta} ~ beta_1 * 10^{56} GeV^4. Compared to the cutoff action's rho_vac = 3.97 x 10^{68} GeV^4 (equation CC-5 of the framework), this is already 12 OOM smaller. The remaining gap to rho_obs = 2.7 x 10^{-47} GeV^4 would be ~103 OOM. A significant reduction but not a solution.

If M is identified with the BCS gap Delta = 0.464 M_KK = 0.464 * 7.43 x 10^{16} GeV = 3.45 x 10^{16} GeV, then:

    Lambda_CC^{zeta} = beta_1 * (3.45e16)^4 = beta_1 * 1.42 x 10^{66} GeV^4     (L-7)

This is still ~113 OOM above rho_obs. The zeta action reduces the CC gap by ~5 OOM (from ~118 to ~113) but does not solve it.

### II.3. What happens to gravity and Yang-Mills?

In the zeta action, the Einstein-Hilbert term comes from beta_2 M^2 R, giving:

    G_N^{-1} ~ beta_2 M^2     (L-8)

Using M ~ 3.45 x 10^{16} GeV: G_N^{-1} ~ beta_2 * 1.19 x 10^{33} GeV^2. The observed G_N^{-1} = M_Pl^2 / (8pi) = 5.93 x 10^{36} GeV^2. This requires beta_2 ~ 5000, which is large but not unreasonable for a trace over 155,984 weighted modes.

The Yang-Mills action comes directly from a_4, which is the LEADING term in the zeta action:

    S_YM^{zeta} = a_4(D_K^2) = 1350.72 M_KK^{d-8}     (L-9)

CLASSIFICATION: The Yang-Mills sector (a_4) is FUNCTIONAL-INDEPENDENT -- it appears identically in both the cutoff and zeta actions (as f_4 a_4 in the cutoff, with f_4 a dimensionless number, and as a_4 directly in the zeta). The gravitational sector (a_2) and the CC sector (a_0) are SCHEME-DEPENDENT -- they enter differently depending on the functional.

### II.4. What happens to n_s, r, and the Higgs mass?

The spectral index n_s in the framework comes from the slow-roll parameter eps_H, which depends on the spectral action profile S(tau). In the cutoff action, S(tau) = sum_n d_n f(lambda_n^2/Lambda^2) and eps_H depends on the cutoff function f.

In the zeta action, S_zeta(tau) = a_4(tau), which is the tau-dependent fourth SDW coefficient. Since a_4 depends on curvature-squared combinations (Weyl tensor, Gauss-Bonnet, scalar curvature squared), its tau-dependence is qualitatively different from S_cutoff(tau).

**Critical question**: Does eps_H^{zeta} = eps_H^{cutoff}? The answer is: NOT necessarily. The BdG heat kernel factorization (W1-A structural theorem) gives S_BCS^{cutoff} = exp(-Delta^2/Lambda^2) * S_bare^{cutoff} for exponential cutoff -- a tau-independent rescaling that leaves eps_H unchanged. For the zeta action, the BCS correction enters through the conformal anomaly coefficient a_4^{BdG}, which may have different tau-dependence.

**SPECULATIVE**: The framework's n_s = 0.9590 result may be scheme-dependent at the level of the remaining 0.006 gap to Planck. Computing eps_H in the zeta action is a concrete way to determine whether this gap is a functional choice or a structural prediction.

### II.5. Summary: zeta action applied to SU(3)

| Quantity | Cutoff action | Zeta action | Classification |
|:---------|:-------------|:------------|:---------------|
| CC term | f_0 Lambda^4 a_0 | beta_1 M^4 (from D_F) | SCHEME-DEPENDENT |
| Gravity | f_2 Lambda^2 a_2 | beta_2 M^2 R (from D_F) | SCHEME-DEPENDENT |
| Yang-Mills | f_4 a_4 | a_4 (directly) | FUNCTIONAL-INDEPENDENT |
| CC gap (OOM) | 117-118 | ~113 (est.) | SCHEME-DEPENDENT |
| a_0 enters? | Yes (leading term) | No | SCHEME-DEPENDENT |
| Renormalizability | No (Paper 05) | Yes (Paper 01) | STRUCTURAL |
| Spectral dimension D_s | 0 (all sectors) | 4 (matter), 2 (gravity) | SCHEME-DEPENDENT |
| n_s | 0.9590 (f = sqrt(x)) | To be computed | UNKNOWN |

---

## III. Anomaly Derivation Constraints

### III.1. The bosonic spectral action is forced, not arbitrary

My Paper 02 (arXiv:1001.2036, with Andrianov) proves that the bosonic spectral action Tr f(D^2/Lambda^2) is NOT an independent postulate. It is the ANOMALY CANCELLATION TERM required by the quantum consistency of the fermionic action.

The derivation proceeds as follows. The fermionic partition function Z_Lambda(D) = det(D_N) is regulated by truncating to the first N eigenvalues. Under a scale transformation D -> e^{-phi/2} D e^{-phi/2}, the regulated partition function transforms anomalously:

    Z_Lambda(D') = Z_Lambda(D) * exp(S_anom)     (L-10)

The anomalous action S_anom = phi * Tr P_N = phi * Tr chi(D^2/Lambda^2) is EXACTLY the bosonic spectral action with cutoff function chi = Theta(1-x) (sharp step).

**The key constraint**: Different regularization prescriptions (sharp, smooth, zeta) of the FERMIONIC partition function produce DIFFERENT anomaly terms, and therefore different bosonic actions. The cutoff action with f(x) = Theta(1-x) comes from sharp spectral truncation. The zeta action S_zeta = a_4 comes from zeta-function regularization of the fermionic determinant.

### III.2. Which functional is "forced"?

The anomaly derivation does NOT uniquely fix the spectral functional. It establishes that SOME bosonic action is required by quantum consistency, and that the form of this action is determined by the choice of fermionic regularization. This is not a freedom to be regretted -- it is a physical choice.

In the Weyl anomaly version (Paper 03, arXiv:1106.3263), the anomalous action has the structure:

    S_anom = (1/8)(e^{4phi} - 1) a_0 + (1/2)(e^{2phi} - 1) a_2 + phi a_4     (L-11)

The a_0 and a_2 terms are PRESENT but multiplied by (e^{nphi} - 1), which vanishes at phi = 0 (no scale transformation). The a_4 term enters linearly in phi and survives at all scales. This is why the zeta action (which extracts a_4 alone) is the natural OUTPUT of the anomaly calculation in the conformal limit phi -> 0.

**Constraint on the framework**: The anomaly derivation tells us that the a_4 term is ALWAYS present (it is the conformal anomaly, scheme-independent). The a_0 and a_2 terms are present in specific regularization schemes but absent in others. The question "which spectral functional?" reduces to "which fermionic regularization is physical?"

### III.3. The Seeley-DeWitt expansion connects different moments

The anomaly structure (L-11) shows that a_0, a_2, and a_4 appear with DIFFERENT phi-dependence. Under the dilaton identification phi -> tau (Jensen deformation parameter), this means the spectral action has DIFFERENT tau-dependence depending on which term dominates. In the cutoff action, the a_0 term dominates by Lambda^4 and its tau-independence (proved by T14: a_0 = const for volume-preserving Jensen) makes S(tau) effectively tau-independent at leading order. In the zeta action, the a_4 term dominates and its tau-dependence drives the physical dynamics.

CLASSIFICATION: The anomaly derivation of the spectral action is STRUCTURAL -- it applies to all spectral triples. The specific functional form (cutoff vs zeta) is a regularization choice with physical consequences.

---

## IV. Functional-Independent vs Scheme-Dependent Classification

I now classify the major S64-S65 results.

### IV.1. FUNCTIONAL-INDEPENDENT (structural, survives all functionals)

1. **a_0/a_2 = 6/R for left-invariant metrics on SU(3)** -- This is a property of the Seeley-DeWitt coefficients, which are operator invariants of D_K^2. STRUCTURAL.

2. **Block-diagonal theorem (Peter-Weyl)** -- D_K is block-diagonal in PW sectors for left-invariant metrics. This is representation theory, independent of any functional. STRUCTURAL.

3. **B/F spectral asymmetry = 0 exactly** (W1-C) -- The trace Tr f(D_K^2) has no B/F decomposition on a pure Riemannian spectral triple, for ANY function f. STRUCTURAL.

4. **U(2)-preservation of gradient flow** -- The spectral action gradient preserves U(2) invariance. This holds for ANY spectral functional, because U(2) acts on the spectrum by permuting eigenvalues within representations, and any function of the spectrum inherits this symmetry. STRUCTURAL.

5. **BCS gap topological protection** (W3-D) -- The gap Delta/Delta_0 = 0.975 at 18.2% off-Jensen deviation is protected by BDI Z_2 invariant. This is a property of the Hamiltonian, not the functional. STRUCTURAL.

6. **Richardson-Gaudin integrability and the Ordered Veil** -- Integrability of the BCS pair Hamiltonian on the D_K spectrum is a property of the Hamiltonian, not of which spectral functional defines the action. STRUCTURAL.

7. **The conjugate pairing theorem** (W1-E) -- a_k(T=1) = a_k(T=2) exactly. STRUCTURAL.

### IV.2. SCHEME-DEPENDENT (changes with the functional)

1. **The CC gap itself** -- The 117 OOM gap involves f_0 Lambda^4 a_0. In the zeta action, f_0 = 0. The gap changes. SCHEME-DEPENDENT.

2. **n_s = 0.9590** -- This depends on the cutoff function f(x) = sqrt(x). For f(x) = exp(-x), the BCS correction vanishes identically (W1-A structural theorem). The n_s value is scheme-dependent at the level of ~0.02. SCHEME-DEPENDENT.

3. **The structural monotonicity theorem (S37)** -- This states S_f(tau) is monotone for all smooth monotone cutoffs. It does NOT apply to the zeta action, which extracts a_4(tau) -- a curvature-squared invariant with potentially non-monotone tau-dependence. SCHEME-DEPENDENT (in scope).

4. **eps_H = 0.02163** -- Depends on the spectral action profile, which is functional-dependent. SCHEME-DEPENDENT.

5. **Transit-as-relaxation (Path C)** -- The a_0 floor obstruction assumes the cutoff action. In the zeta action, the a_0 floor does not exist. The transit-as-relaxation mechanism may be VIABLE in the zeta scheme. SCHEME-DEPENDENT.

6. **The nonlocal SA result (W3-B)** -- All nonlocal filters increase a_0/a_2. This result applies to cutoff-type functionals where a_0 and a_2 both enter. In the zeta action, only a_4 enters -- the ratio a_0/a_2 is irrelevant. SCHEME-DEPENDENT.

7. **Spectral dimension** -- D_s = 0 for all sectors in the cutoff action. D_s = 4 (matter) and D_s = 2 (gravity) in the zeta action. SCHEME-DEPENDENT.

### IV.3. Implications

The functional-independent results define the WALLS of the solution space. These walls are permanent and apply regardless of which spectral functional is chosen. The scheme-dependent results define the LOCATION of the CC within those walls, and this location moves when the functional changes.

The project's investment in mapping geometric closures has been well-spent: these closures are structural and permanent. But the CC gap itself is scheme-dependent, and no amount of geometric exploration within a fixed functional will address it.

---

## V. The Dilaton Route

### V.1. Dilaton from spectral regularization

My Papers 03-04 (arXiv:1106.3263, 1210.2663) derive the Higgs-dilaton Lagrangian from spectral regularization. The dilaton phi(x) appears as the compensating field for the Weyl anomaly. Under the scale transformation g_{mu nu} -> e^{2 alpha(x)} g_{mu nu}, the dilaton couples to all dimension-2 operators:

    V(phi, H) = lambda_phi phi^4 + lambda_H H^4 + lambda_{H phi} phi^2 H^2 + mu_phi^2 phi^2 + mu_H^2 H^2     (L-12)

The dilaton vev sets the scale of the gravitational coupling: G_N^{-1} ~ <phi>^2.

### V.2. Could the dilaton provide CC relaxation?

The dilaton effective potential from the Weyl anomaly has the structure:

    V_eff(phi) ~ Lambda^4 e^{-4 phi/f} + m^2 phi^2 + lambda phi^4     (L-13)

At the minimum, <phi> ~ Lambda^2/(mf). The cosmological constant at the minimum is:

    Lambda_CC^{dilaton} = V_eff(<phi>) = lambda_H <H>^4 + lambda_{H phi} <H>^2 <phi>^2 + lambda_phi <phi>^4     (L-14)

If lambda_phi is small (from the running of the dilaton quartic coupling), this can be naturally small. In the framework's language, the Jensen parameter tau plays the role of the dilaton: it parametrizes the scale transformation of the fiber metric. The transit through the fold (tau = 0.19) is a dilaton-driven conformal phase transition.

**SPECULATIVE**: If we identify tau with the dilaton, the transit-as-relaxation mechanism (Path C in the framework) becomes a dilaton rolling from large vev (pre-transit, large Lambda_CC) to small vev (post-transit, small Lambda_CC). The a_0 floor obstruction (which blocks this in the cutoff action because a_0 is tau-independent) is REMOVED in the zeta action because a_0 does not enter. The dilaton + zeta action combination may enable transit-as-relaxation.

However, I must be honest: the dilaton route does not by itself solve the CC problem. The dilaton potential still has free parameters (lambda_phi, lambda_{H phi}, mu_phi). These are determined by the Dirac operator spectrum through the anomaly coefficients, but computing them for D_K on Jensen-deformed SU(3) has not been done. This is a concrete computation that could determine whether the dilaton route is quantitatively viable.

### V.3. The dilaton and the spectral functional choice

There is a deeper connection. In the anomaly derivation (Section III above), the dilaton phi parametrizes the INTERPOLATION between different regularization schemes. At phi = 0 (no scale transformation), only a_4 contributes -- the zeta action. At phi != 0, the a_0 and a_2 terms switch on with exponential weights e^{4 phi} and e^{2 phi}. The physical value of the dilaton determines which spectral functional is "physical."

This is the key insight: the choice of spectral functional is NOT an arbitrary convention. It is determined by the dilaton vev. If <phi> = 0 (conformal limit), the zeta action is physical and a_0 does not contribute to the CC. If <phi> >> 1, the cutoff action is physical and the CC catastrophe obtains. The CC problem may reduce to: **why does the dilaton vev take the value it does?**

CLASSIFICATION: SPECULATIVE. This connects the spectral functional choice to a dynamical field, but requires a complete dilaton potential computation on D_K to be quantitative.

---

## VI. Concrete Proposals for S66

### VI.1. ZETA-SA-66: Compute S_zeta(tau) = a_4(tau) on Jensen-deformed SU(3)

**Input**: D_K eigenvalues at L_max = 3-6, all 35 PW sectors, tau = 0.01 to 0.50
**Computation**: a_4(tau) from the Gilkey formula using eigenvalue sums. This is sum_n d_n lambda_n^{-2s} at s=0, which requires analytic continuation or equivalently the coefficient of t^0 in the heat kernel trace Tr exp(-t D_K^2).
**Output**: S_zeta(tau) profile. Compute eps_H^{zeta} and n_s^{zeta}.
**Gate**: n_s^{zeta} within 3 sigma of Planck (0.9649 +/- 0.0042).
**Why**: This determines whether the n_s prediction is functional-independent or scheme-dependent. If n_s^{zeta} agrees with n_s^{cutoff} at the 0.01 level, the prediction is structural. If they differ by more than 0.02, the functional choice matters and must be determined.

### VI.2. DILATON-POTENTIAL-66: Compute the Weyl anomaly dilaton potential on D_K

**Input**: D_K spectrum, Majorana mass from BCS gap, Weyl anomaly coefficients from Paper 03 formula (L-11).
**Computation**: V_eff(phi) = (1/8)(e^{4 phi} - 1) a_0(D_K) + (1/2)(e^{2 phi} - 1) a_2(D_K) + phi a_4(D_K). Minimize for phi. Extract Lambda_CC^{dilaton} = V_eff(<phi>).
**Output**: Dilaton vev <phi>, CC at the minimum, CC gap in OOM.
**Gate**: Lambda_CC^{dilaton} < Lambda_CC^{cutoff} by at least 10 OOM (meaningful progress).
**Why**: If the dilaton minimum has phi near zero, the zeta action is dynamically selected and the CC is naturally reduced.

### VI.3. ANOMALY-CONSTRAINT-66: Test whether the anomaly derivation constrains f_0/f_2

**Input**: The anomaly structure (L-11), D_K spectrum, physical requirement that the anomaly is multiplicatively renormalizable.
**Computation**: The anomaly cancellation requires specific relationships between f_0, f_2, and f_4 (the moments of the cutoff function). Check whether these relationships are consistent with f_0/f_2 = 0 (the zeta limit).
**Output**: Allowed range of f_0/f_2 from anomaly consistency.
**Gate**: f_0/f_2 = 0 is anomaly-consistent (zeta action is physical) or f_0/f_2 is bounded away from zero (zeta action is excluded).
**Why**: This determines whether the zeta action is a legitimate physical option or a mathematical convenience that violates quantum consistency.

### VI.4. ENTROPY-SA-CC-66: Compute a_0^S/a_2^S for the entropy cutoff (Connes's Paper 15)

I endorse this computation proposed by the Connes agent. The entropy cutoff f_S(x) = -[p ln p + (1-p) ln(1-p)] with p = 1/(e^{beta x} + 1) is the ONLY cutoff function with thermodynamic motivation. It is NOT monotone. The NONLOCAL-SA-65 result (all monotone filters worsen the ratio) does not apply. The entropy cutoff could have qualitatively different moment ratios.

**Specific contribution I can add**: The entropy cutoff is related to the anomaly derivation through the KMS condition. In the Weyl anomaly framework (Paper 03), the dilaton phi couples to the thermal state at inverse temperature beta. The entropy cutoff function f_S arises naturally as the anomaly at finite temperature. This provides an independent motivation for the Connes computation.

### VI.5. SPECTRAL-DIM-66: Compute spectral dimension D_s for D_K in both cutoff and zeta schemes

**Input**: D_K propagator at various momenta.
**Computation**: D_s = lim_{p->infty} d log|G(p)|/d log p for both schemes.
**Output**: Spectral dimension profile D_s(p) for both functionals.
**Gate**: D_s^{zeta} = 4 (matter) and D_s^{zeta} = 2 (gravity), confirming Paper 01 predictions.
**Why**: The spectral dimension determines the UV behavior of loop corrections. If gravity has D_s = 2, loop corrections to the CC are power-law suppressed relative to D_s = 4 -- a partial resolution of the hierarchy.

---

## VII. Honest Assessment

### VII.1. Can the CC be solved within the spectral action framework?

The CC problem has two components:

**(A) The a_0 component**: Why does the mode-counting zeroth Seeley-DeWitt coefficient not gravitationally contribute? In the zeta action, this is answered by construction: a_0 does not appear. In the cutoff action, this is the 117 OOM gap.

**(B) The residual component**: Even in the zeta action, the CC is determined by the Majorana mass beta_1 M^4 (or the BCS condensation energy in the framework), which is still ~113 OOM above observation.

The zeta action resolves component (A) but not component (B). Component (B) is the hard problem: it requires either a cancellation mechanism internal to the spectral triple, or a dynamical relaxation mechanism, or an appeal to the thermodynamic equilibrium condition (Volovik's q-theory).

### VII.2. What the zeta action buys and what it does not

The zeta action buys:
- Renormalizability (Paper 01, Paper 05)
- Elimination of the a_0 mode-counting catastrophe
- Viable spectral dimensions (D_s = 2 for gravity)
- Connection to the conformal anomaly (scheme-independent)
- Possible reactivation of transit-as-relaxation (Path C) since the a_0 floor is removed

The zeta action does NOT buy:
- A solution to the residual CC gap (~113 OOM)
- A derivation of the Majorana mass scale
- A determination of the dilaton vev
- Any modification of the structural closures (block-diagonal theorem, B/F symmetry, integrability)

### VII.3. The spectral functional pluralism verdict

My honest assessment: the CC problem CANNOT be solved by choosing a different spectral functional alone. Different functionals redistribute the CC between different spectral moments, but the total spectral weight of D_K (155,984 weighted eigenvalues, a_0 = 6440 at the fold) is an intrinsic property of the operator. No functional can make this weight vanish.

The CC may be solvable within the spectral action framework IF:
1. The physical functional is the zeta action (removing a_0), AND
2. The Majorana mass/BCS gap sets the CC scale at beta_1 M^4, AND
3. A dynamical mechanism (dilaton relaxation, q-theory equilibrium, or transit) reduces beta_1 M^4 by the remaining ~113 OOM.

This is a narrow path. It requires three independent conditions to hold simultaneously. But it is not ruled out by anything the project has computed. The structural closures (which are functional-independent) constrain the geometry; they do not constrain the functional choice or the Majorana mass dynamics.

### VII.4. What I would tell the project

The most important thing the project can do next is COMPUTE IN MULTIPLE FUNCTIONALS. Every CC-sensitive quantity should be reported in at least two schemes: the cutoff f(x) = sqrt(x) currently used, and the zeta action S_zeta = a_4. Quantities that agree between schemes are structural predictions. Quantities that disagree reveal where the functional choice matters -- and the CC is the primary quantity that disagrees.

The project has spent 65 sessions assuming a single spectral functional. The payoff of those sessions is the permanent structural results (block-diagonal theorem, a_0/a_2 = 6/R, integrability, Ordered Veil). These survive all functional choices and are the project's lasting contribution. The CC-specific results (the gap, the closures of geometric routes) are correct but narrower than they appear: they are closures within a fixed functional. The spectral functional itself is the remaining degree of freedom, and it is where the CC solution -- if one exists -- must be found.

---

## Appendix: Key Formulas from My Papers

**Paper 01** (arXiv:1412.4669): S_zeta = zeta_D(0) = a_4(D^2). Contains ONLY dimension-4 operators. Renormalizable.

**Paper 02** (arXiv:1001.2036): S_anom = phi Tr P_N = phi Tr chi(D^2/Lambda^2). Bosonic action from fermionic anomaly.

**Paper 03** (arXiv:1106.3263): S_anom = (1/8)(e^{4 phi}-1)a_0 + (1/2)(e^{2 phi}-1)a_2 + phi a_4. Weyl anomaly with dilaton.

**Paper 04** (arXiv:1210.2663): V(phi,H) = complete Higgs-dilaton potential from spectral regularization.

**Paper 05** (arXiv:1312.2235): Cutoff action propagators diverge as p^4. Non-renormalizable. Motivates zeta action.

**Paper 06** (arXiv:1305.2605): Cutoff ambiguity: different f(x) change predictions by 20-30%. Ratio a_0/a_2 is scale-dependent in cutoff scheme, not in zeta.
