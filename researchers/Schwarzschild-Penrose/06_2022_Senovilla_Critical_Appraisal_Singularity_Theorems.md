# A critical appraisal of the singularity theorems

**Author(s):** Jose M. M. Senovilla (Physics Department, University of the Basque Country UPV/EHU)
**Year:** 2021 (published in Philosophical Transactions of the Royal Society A, posted on arXiv 16 Aug 2021)
**Journal:** Philosophical Transactions of the Royal Society A
**arXiv:** 2108.07296
**Relevance:** HIGH

---

## Abstract

The 2020 Nobel prize in Physics has revived the interest in the singularity theorems and, in particular, in the Penrose theorem published in 1965. In this short paper I briefly review the main ideas behind the theorems and then proceed to an evaluation of their hypotheses and implications. I will try to dispel some common misconceptions about the theorems and their conclusions, as well as to convey some of their rarely mentioned consequences. In particular, a discussion of spacetime extensions in relation to the theorems is provided. The nature of the singularity inside black holes is also analyzed.

---

## Key Arguments and Derivations

**Section 1: Introduction.** Senovilla frames the Penrose theorem as a "first post-Einsteinian content of relativity" — not foreseen by Einstein. The fundamental novelty was the concept of trapped spheres and the use of geodesic incompleteness as a characterization of spacetime failure. The theorem had major physical consequences for black hole physics, numerical relativity, mathematical relativity, cosmology, and gravity analogs.

**Section 2: The Penrose singularity theorem.** Stated in modern terms:

> **Theorem 2.1 (Penrose singularity theorem).** In a spacetime of sufficient differentiability, if (i) the null convergence condition holds, (ii) there is a non-compact Cauchy hypersurface Sigma, and (iii) a closed future-trapped surface exists, then there are future-incomplete null geodesics.

The two key novelties are: (i) geodesic incompleteness as the characterization of spacetime failure; (ii) the concept of closed trapped surface. A Cauchy hypersurface is a spacelike slice crossed exactly once by every inextendible timelike or null curve; non-compactness of Sigma amounts to saying space is not finite. The convergence condition arises from the Raychaudhuri equation

  v^nu nabla_nu(nabla_mu v^mu) + nabla_mu v^nu nabla_nu v^mu - nabla_mu(v^nu nabla_nu v^mu) + R_rho_nu v^rho v^nu = 0

which, for hypersurface-orthogonal geodesic vector fields, gives v^nu nabla_nu(nabla_mu v^mu) = -nabla_mu v_nu nabla^mu v^nu - R_rho_nu v^rho v^nu. The condition R_rho_nu v^rho v^nu >= 0 (Eq. 2.1) is the null/timelike convergence condition and, via Einstein's equations R_mu_nu - (1/2) R g_mu_nu + Lambda g_mu_nu = (8 pi G/c^4) T_mu_nu (Eq. 2.2), becomes the strong energy condition when valid for all timelike v. In GR, Lambda makes no difference for **null** geodesics.

**Trapped spheres (§2.b-c).** For a spacelike submanifold zeta and an arbitrary vector field xi^mu deforming zeta along its flow, the initial variation of area A_zeta is delta_xi A_zeta = integral_zeta (div xi^T + H^mu xi_mu), where H^mu is the mean curvature vector (trace of the shape tensor) and xi^T is the component of xi tangent to zeta. For compact zeta, delta_xi A_zeta = integral_zeta H^mu xi_mu. If H^mu is future-timelike on zeta, the variation along any future-directed vector field is strictly negative — these are the trapped submanifolds. Stationary spacetimes cannot have compact trapped submanifolds because the variation along the timelike Killing vector vanishes. The expansion theta_n = H^mu n_mu measures the trapping; Penrose originally used the null normals. The notion is stable under small perturbations because it is defined by inequalities H^mu H_mu < 0. Penrose's original theorem used this stability to extend the Oppenheimer-Snyder conclusion (spherical dust collapse) to general, non-symmetric collapse.

**Section 3: Singularity theorems.** Hawking quickly realized that trapped spheres exist in FLRW models: for flat-slice FLRW with line element ds^2 = -c^2 dt^2 + a^2(t)(d chi^2 + chi^2 d Omega^2), round spheres with constant t and chi have H_vec = (1/a)(-a_dot/c partial_t + (1/chi) partial_chi), which is timelike iff a_dot^2 > 1/chi^2. Equivalently, today, H_0 > c/D for sufficiently distant spheres centered at us. Hawking-Geroch proved cosmological singularity theorems, of which the simplest is:

> **Theorem 3.1 (Hawking).** If there is a Cauchy hypersurface Sigma with second fundamental form trace K >= b > 0 and the convergence condition (2.1) holds along the timelike geodesic congruence orthogonal to Sigma, then all timelike geodesics are past incomplete.

Then the **pattern singularity theorem** (Theorem 3.2):

> If a spacetime of sufficient differentiability satisfies (i) a curvature condition, (ii) a causality condition, (iii) an appropriate initial/boundary condition, then there are null or timelike inextensible incomplete geodesics.

The paradigmatic case is the Hawking-Penrose theorem (Theorem 3.3):

> If the convergence condition holds, there are no closed future-pointing timelike curves, a generic condition on the curvature holds, and there is one of: (a) a compact spacelike achronal hypersurface, (b) a closed trapped surface, (c) a point with re-converging light cone, then the spacetime is causal geodesically incomplete.

The generic condition amounts to having tidal effects at some point for every causal curve.

**Section 4: Critical evaluation.**

*(a) Penrose's theorem does NOT prove that black holes form in gravitational collapse.* The theorem assumes a trapped sphere exists; it does not address formation. Moreover, a theorem by Claudel [10] states that in asymptotically flat spacetimes no closed trapped surface can be seen from infinity — they are enclosed beyond the event horizon. So Penrose's theorem is a statement about the **interior** of black holes: given that a black hole forms, incompleteness must follow.

*(b) Geodesically complete spacetimes.* Senovilla lists examples:
- **Einstein static universe** (Lambda > 0): dust solution on a 3-sphere, contains compact Cauchy hypersurfaces and points with reconverging light cones, is geodesically complete. The Hawking-Penrose generic condition fails for some specific timelike geodesics.
- **de Sitter spacetime** (in closed-slice form ds^2 = -c^2 dt^2 + lambda^2 cosh^2(ct/lambda)(d chi^2 + sin^2 chi d Omega^2), lambda^2 = 3/Lambda): trapped round spheres exist (tan^2 chi > 1/sinh^2(ct/lambda)), but the Cauchy hypersurfaces are **compact**, so Theorem 2.1 does not apply. Hawking-type theorems fail because the timelike convergence condition does not hold (Lambda effect).
- **Chinea-Fernandez-Jambrina-Senovilla singularity-free perfect fluid model (Eq. 4.1)** with line element ds^2 = cosh^4(at) cosh^2(3 a rho)(-c^2 dt^2 + d rho^2) + (1/(9 a^2)) cosh^4(at) cosh^{-2/3}(3 a rho) sinh^2(3 a rho) d phi^2 + cosh^{-2}(at) cosh^{-2/3}(3 a rho) dz^2. Solves Einstein's equations with Lambda = 0 for a perfect fluid with equation of state p = rho/3 (radiation), is globally hyperbolic with non-compact Cauchy hypersurfaces, and is **geodesically complete**. The expansion (Eq. 4.3) is K = 3a sinh(at)/(cosh^3(at) cosh(3 a rho)), positive for all t > 0 but with lim_{rho -> infinity} K = 0, which is why the Hawking theorem's lower-bound requirement fails.

**General results for globally hyperbolic spacetimes.** For stationary global hyperbolic spacetimes with (2.1), geodesic completeness requires R_mu_nu xi^mu xi^nu / xi^mu xi_mu ~ k/rho_bar^2 for some constant k (fall-off with spatial distance). For dynamical open cases with non-compact Cauchy Sigma and everywhere-positive expansion K, if (2.1) holds along the timelike congruence orthogonal to Sigma, then at least one of: Lambda, the averaged energy density on Sigma, or minus the averaged scalar curvature of Sigma, must be non-positive. This says "regular cosmological models are not viable if the Universe has an approximately homogeneous distribution of matter everywhere."

**Regular black holes (Section 4.b.v).** A particular model with line-element

  ds^2 = -e^{4 beta(r)}(1 - 2 mu(r)/r) dv^2 + 2 dv dr + r^2 d Omega^2     (Eq. 4.4)

with explicit beta, mu depending only on r. The solution coincides with Schwarzschild for r >= r_g = 2 G M/c^2 and acquires a matter content satisfying the weak energy condition (hence the null convergence condition) for r < r_g. The region r_g/2 < r < r_g contains trapped round spheres. There are no curvature singularities — r = 0 is a regular center. Non-compact Cauchy hypersurfaces exist, so Penrose's theorem applies: some null geodesics must be incomplete. These are null geodesics reaching r = r_g in the past or r = r_g/2 in the future with finite affine parameter. But the metric can be regularly extended through these surfaces, and there exist **geodesically complete** extensions [34]. In the extended spacetime, the original Sigma fails to be a Cauchy hypersurface. Such regular black holes exhibit topology change: the original Sigma has topology R^3 while extended slices can be topologically R x S^2 or S^3.

**Section 4.c: The problem of extensions.** Extensions are highly non-unique. Three categories:
(i) new extensible spacetimes (e.g. Eq. 4.4 itself extends Schwarzschild non-typically);
(ii) geodesically complete inextensible spacetimes (extension of the regular black hole);
(iii) geodesically incomplete inextensible spacetimes (e.g. standard Kruskal extension).

One would think (ii) should always be preferred, but in practice, if (ii) violates a physical condition such as causality or energy positivity, other extensions are preferred. The Kerr maximal analytic extension leads to causality violation yet is standardly used.

**Section 5: The character of the singularity.** Singularity theorems say nothing about the nature of singularities. Belinskii-Khalatnikov-Lifschitz (BKL) conjectured that singularities are spacelike, local, oscillatory, and "matter does not matter" — based on the dominance of time derivatives in the field equations near the singularity. In this picture, dynamics decouples point-by-point to that of a spatially homogeneous (Bianchi) model, and the anisotropic terms diverge faster than matter terms. The competing picture is the null singularity scenario of Poisson-Israel, based on the instability of Cauchy horizons (Reissner-Nordstrom, Kerr). Recent results:
- Generically, a null piece of the singularity exists in realistic collapse starting from good initial data.
- But the null part cannot (in spherical symmetry) cover the entire singularity [Van de Moortel 2019, 60].
- So there is a BKL (non-null) portion and a null portion (see Figure 4). Collapsing matter within the star meets BKL; an observer entering the BH long after formation meets the null part.

**Section 6: Conclusions.** Singularities are NOT "consubstantial to GR": almost all gravitational systems are regular. The only possible exceptions are the very early Universe and the deep interiors of black holes. The singularity theorems therefore provide supporting evidence for the need of (quantum) corrections to GR well inside black holes and probably at the initial stages of our Universe. The most powerful theorems have little direct applicability because they do not locate the singularity. To date there is no theorem predicting the singularity in the maximally extended Kerr black hole.

## Key Results

1. **Penrose singularity theorem (Theorem 2.1)** — null convergence + non-compact Cauchy hypersurface + closed future-trapped surface => future incomplete null geodesics.
2. **Hawking theorem (Theorem 3.1)** — Cauchy hypersurface with K >= b > 0 + timelike convergence along orthogonal congruence => all timelike geodesics past incomplete.
3. **Hawking-Penrose theorem (Theorem 3.3)** — convergence + no closed timelike curves + generic condition + one of three trapped-set alternatives => causal geodesic incompleteness.
4. **Pattern singularity theorem (Theorem 3.2)** — the common structure: curvature condition + causality + initial/boundary condition => incomplete geodesics.
5. **Misinterpretation correction** — Penrose's theorem is about the **interior** of black holes, not about black-hole **formation** (Claudel's theorem shows closed trapped surfaces are hidden behind event horizons in asymptotically flat spacetimes).
6. **Examples evading all the theorems**: Einstein static universe (fails generic condition), de Sitter in closed-slice form (Cauchy hypersurfaces compact, convergence fails along timelike for Lambda > 0), CFJS radiation-perfect-fluid model (expansion not bounded below away from zero).
7. **Dynamical open cases**: globally hyperbolic spacetimes with positive K on non-compact Sigma and (2.1) along the normal timelike congruence must have Lambda or averaged energy density or minus averaged scalar curvature of Sigma non-positive.
8. **Regular black holes** (Eq. 4.4) satisfy weak energy condition and null convergence but can be extended through the singularity predicted by the theorem to geodesically-complete spacetimes in which the original Cauchy surface ceases to be Cauchy.
9. **Character of the singularity**: combined BKL + null singularity picture. Collapsing matter meets BKL; late-falling observer meets a null singularity.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Convergence condition | R_rho_nu v^rho v^nu >= 0 | Eq. 2.1 |
| Einstein's equations | R_mu_nu - (1/2) R g_mu_nu + Lambda g_mu_nu = (8 pi G/c^4) T_mu_nu | Eq. 2.2 |
| Raychaudhuri (general) | v^nu nabla_nu(nabla_mu v^mu) + nabla_mu v^nu nabla_nu v^mu - nabla_mu(v^nu nabla_nu v^mu) + R_rho_nu v^rho v^nu = 0 | §2 |
| Variation of area | delta_xi A_zeta = integral_zeta (div xi^T + H^mu xi_mu) | §2.b |
| Compact variation | delta_xi A_zeta = integral_zeta H^mu xi_mu | §2.b |
| Expansion along n | theta_n = H^mu n_mu | §2.b |
| FLRW mean curvature | H_vec = (1/a)(-a_dot/c partial_t + (1/chi) partial_chi) | §3 |
| Trapping criterion | a_dot^2 > 1/chi^2 (equivalently H_0 > c/D) | §3 |
| Regular BH line element | ds^2 = -e^{4 beta(r)}(1 - 2 mu(r)/r) dv^2 + 2 dv dr + r^2 d Omega^2 | Eq. 4.4 |
| CFJS singularity-free metric | ds^2 = cosh^4(at) cosh^2(3 a rho)(-c^2 dt^2 + d rho^2) + ... | Eq. 4.1 |
| CFJS energy density | (8 pi G/c^4) rho = 15 a^2 cosh^{-4}(at) cosh^{-4}(3 a rho) | Eq. 4.2 |
| CFJS expansion | K = 3 a sinh(at)/(cosh^3(at) cosh(3 a rho)) | Eq. 4.3 |

## Relevance to Phonon-Exflation

Senovilla's critical appraisal is the best modern summary of what singularity theorems actually require and what they do not prove. For the phonon-exflation framework, the key takeaways are: (1) Penrose's theorem does not prove singularity formation, only that trapped surfaces inside an already-existing black hole imply incompleteness; this is directly relevant because the framework claims the cosmogenetic transit through tau ~ 0.19 is a first-order phase transition rather than a singularity, so "incomplete geodesics" in the emergent M4 description are absorbed into the substrate spectral description at the fold. (2) The dynamical-case theorem for globally hyperbolic open spacetimes (averaged energy density or Lambda must be non-positive to avoid incompleteness) is the cosmological analog of the Russo-Townsend result about dynamical compactifications — both narrow the avenues by which the framework can produce acceleration from extra structure. (3) Senovilla's "regular black hole" example (Eq. 4.4) is architecturally similar to the framework's Level-3 emergence: a region with trapped surfaces and honest-to-goodness geodesic incompleteness at one description level can be **extended** at a deeper level (for the framework, the substrate spectral description) to a geodesically complete picture in which the original "Cauchy hypersurface" is no longer Cauchy. The framework's "L-3 PET" (Level-3 Penrose-type theorem applied to internal SU(3)) should be understood in exactly this sense. The framework's WCH compatibility (Weyl curvature C^2 = 5/14 non-zero but minimum at tau = 0) fits Senovilla's point that the character of the singularity (BKL vs null) is not fixed by the theorems themselves.
