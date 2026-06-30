# The 1965 Penrose singularity theorem

**Author(s):** Jose M. M. Senovilla (Fisica Teorica, Universidad del Pais Vasco) and David Garfinkle (Dept. of Physics, Oakland University and Michigan Center for Theoretical Physics)
**Year:** 2014 (arXiv v2 posted 7 Jan 2015), published as a "GR Milestone" in Classical and Quantum Gravity
**Journal:** Classical and Quantum Gravity (GR Milestone)
**arXiv:** 1410.5226
**Relevance:** HIGH

---

## Abstract

We review the first modern singularity theorem, published by Penrose in 1965. This is the first genuine post-Einsteinian result in General Relativity, where the fundamental and fruitful concept of closed trapped surface was introduced. We include historical remarks, an appraisal of the theorem's impact, and relevant current and future work that belongs to its legacy.

---

## Key Arguments and Derivations

**Section 1: Introduction.** 1965 was a pivotal year for GR, with the discovery of the Cosmic Background Radiation and the first modern singularity theorem (Penrose, [248] in their reference list). Penrose's theorem introduced: (i) geodesic incompleteness as the characterization of spacetime failure, (ii) the use of Cauchy hypersurfaces and global hyperbolicity, and (iii) the novel concept of closed trapped surfaces.

**Section 2: Before 1955.** Senovilla and Garfinkle trace the pre-history of singularities in GR:
- Friedman's 1922 closed dust models contained "creation times" where a(t) vanishes and mass density diverges whenever Lambda < 4 pi G T_tt / c^2.
- The extended de Sitter solution (same positive-constant-curvature manifold as the static version) revealed that the area function 4 pi r^2 could be a time coordinate when cosh^2(c t_bar/lambda) sin^2 chi_bar > 1.
- Lemaitre (1927, 1933) constructed the Lemaitre-Tolman dust model, demonstrated the instability of the Einstein static universe, and gave up spherical symmetry to confirm singularities in Bianchi I models: "anisotropy can no more prevent the vanishing of space". Lemaitre also correctly understood the Schwarzschild horizon at r = alpha as an apparent singularity, finding explicit regular extensions.
- Oppenheimer-Snyder (1939) showed that spherical dust collapse matches Schwarzschild vacuum at chi = chi_0 via alpha = A sin^3 chi_0, with the star ending in a catastrophic singularity where a(t) -> 0.
- Einstein himself (1939) "proved" the Schwarzschild singularity is not physically realizable by considering circular orbits of self-gravitating particles; he also introduced the Einstein-Straus vacuole (1945), which is complementary to the Oppenheimer-Snyder model.
- Godel (1949) discovered a rotating, geodesically-complete, totally-vicious solution with closed timelike curves through every point.

**Section 3: 1955-1965 — Raychaudhuri's equation and Komar's theorem.** Less than one month after Einstein's death (18 April 1955), Raychaudhuri published the first modern singularity theorem [259]. The Raychaudhuri equation follows from the Ricci identity by contraction:

  u^nu nabla_nu nabla_mu u^mu + nabla_mu u_nu nabla^nu u^mu - nabla_mu(u^nu nabla_nu u^mu) + R_rho_nu u^rho u^nu = 0     (Eq. 4)

For an affinely-parametrized geodesic vector field u^mu, the third term vanishes. Splitting nabla_mu u_nu = S_mu_nu + A_mu_nu into symmetric and antisymmetric parts, and assuming u^mu is hypersurface-orthogonal (A_mu_nu = 0) and null or unit timelike, one obtains

  u^nu nabla_nu(nabla_mu u^mu) = -S_mu_nu S^mu_nu - R_rho_nu u^rho u^nu

The expansion theta = nabla_mu u^mu = S^mu_mu (Eq. 5) satisfies the key property: if R_rho_nu u^rho u^nu >= 0 and theta is negative (positive) at some point, then theta -> -infinity in finite affine parameter (or proper time) along the congruence. This is the focusing effect. The geometric condition

  R_rho_nu u^rho u^nu >= 0     (Eq. 6)

is the timelike or null convergence condition depending on the character of u^mu; via Einstein's equations and the case Lambda = 0, it is the strong energy condition. The **Raychaudhuri-Komar singularity theorem (Theorem 1)** assumes Lambda = 0, a perfect-fluid energy-momentum tensor T_mu_nu = rho u_mu u_nu + p(g_mu_nu + u_mu u_nu) with geodesic and irrotational u^mu; if theta is positive (or negative) at an instant of time and (6) holds, then rho diverges in finite past (or future) along every integral curve.

**Section 4: The 1965 theorem.**

> **Theorem 2 (Penrose singularity theorem).** If the spacetime contains a non-compact Cauchy hypersurface Sigma and a closed future-trapped surface, and if the convergence condition (6) holds for null u^mu, then there are future incomplete null geodesics.

**§4.1 Incompleteness.** Defining singularities is hard because (i) singularities are not in the spacetime by definition; (ii) curvature tensors depend on bases; (iii) curvature invariants can vanish while the spacetime is singular; (iv) conical singularities involve bad tangent bundles; (v) there are spacetimes with vanishing curvature and incomplete geodesics; (vi) directional singularities exist. Penrose's insight: use incomplete endless curves as the definition. All singularity theorems since prove merely the existence of geodesic incompleteness. Curvature growth along incomplete geodesics cannot exceed (tau - tau_hat)^{-2} in a parallel-propagated frame.

**§4.2 Closed trapped surfaces.** A closed trapped surface is a 2-dimensional imbedded submanifold S (surface), compact without boundary (closed), such that the two families of light rays emerging orthogonally from S towards the future converge initially. If k^mu_+ and k^mu_- are the future-directed affine-parametrized null normals with expansions theta_+/- = nabla_mu k^mu_+/- (defined up to multiplicative factors), the surface is future-trapped if theta_+ < 0 and theta_- < 0 (Eq. 8). Equivalently, the mean curvature vector H^mu is future-timelike. The definition uses **inequalities**, so trapped surfaces are stable under small perturbations of the spacetime.

**Section 5: Immediate impact of the theorem.** Hawking (1965-1967) adapted Penrose's ideas to the past direction, producing singularity theorems for cosmology. The **Hawking-Penrose theorem (Theorem 3)**:

> If the convergence (6) and generic (9) conditions hold for causal vectors, there are no closed timelike curves, and there exists at least one of: a closed achronal imbedded hypersurface, a closed trapped surface, or a point with re-converging light cone, then the spacetime has incomplete causal geodesics.

The generic condition is u_[rho R_alpha]_beta lambda_[mu u_sigma] u^beta u^lambda != 0 (Eq. 9). This holds in arbitrary dimension, with the "closed trapped surface" replaced by a co-dimension-2 trapped submanifold.

**§5.1 Classical singularity theorems — discussion.**

*§5.1.1 Curvature conditions.* (6) and (9) are necessary. (9) is rarely violated (Einstein static universe is an exception). In GR with Lambda > 0, (6) depends on Lambda's sign — which is wrong for the modern observed Lambda. Inflationary models violate (6) classically.

*§5.1.2 Causality conditions.* Two purposes: (a) prevent closed timelike curves, (b) ensure the existence of maximal (longest) geodesics between causally related events. Global hyperbolicity (existence of a Cauchy hypersurface) implies compactness of the space of causal curves between two events, from which maximal geodesics exist.

*§5.1.3 Boundary/initial conditions.* From the curvature condition, all causal geodesics focus (ergo have caustics/focal points). From the causality condition, maximal geodesics without focal points exist between any two events. The contradiction requires a finite upper bound on proper time, which is supplied by the initial/boundary condition (positive expansion of slices, closed trapped surfaces, or points with reconverging light cones). Senovilla emphasizes: **geodesic incompleteness cannot be proven without the initial/boundary condition.** The CFJS model [55, 280] shows that strict (6) plus everywhere-expanding Cauchy hypersurfaces is not enough.

**§5.1.5 Conclusion of the theorems.** Weak: they merely predict at least one incomplete causal geodesic, not its location, strength, extension, or character.

**Section 6: Observational consequences.**

*§6.1 Cosmic censorship.* Weak: singularities are hidden behind horizons. Strong: singularities are non-timelike (i.e. spacetime is globally hyperbolic). Penrose's inequality Area(S) <= 16 pi (G M/c^2)^2 (Eq. 14 of their numbering) for an asymptotically flat initial data with apparent horizon S and ADM mass M is implied by weak cosmic censorship; a violation would produce a naked singularity.

*§6.2 Critical gravitational collapse.* Choptuik's critical phenomena: for a one-parameter family of initial data with parameter p, if p* is the threshold between dispersal and black-hole formation, then for p slightly greater than p*,

  M ~ (p - p*)^gamma     (Eq. 10)

with universal gamma and the critical (p = p*) solution exhibiting discrete or continuous self-similarity, ending in a naked singularity in finite proper time — but only for the single value p = p*, i.e. non-generic.

*§6.3 BKL singularities.* BKL guess: near the singularity, dominant terms in the field equations are those with time derivatives, spatial derivatives are negligible, so dynamics decouples point-by-point to that of a homogeneous Bianchi IX (Mixmaster) model. In this picture, singularities are spacelike, local, oscillatory, and "matter doesn't matter" (except for scalar fields). Numerical work by Berger-Moncrief and Garfinkle et al. has confirmed BKL for Gowdy, U(1), and generic cases (modulo spikes).

*§6.4 Null singularities.* Poisson-Israel picture: Cauchy horizons of Reissner-Nordstrom/Kerr/regular black holes are unstable; perturbations turn them into null singularities. BKL + null picture: star-comoving observers meet BKL, late-entering observers meet null singularities.

*§6.5 Black strings.* 5D black strings (product of S^1 and Schwarzschild) are unstable (Gregory-Laflamme). Numerical simulations (Choptuik-Lehner et al., Lehner-Pretorius) show the endpoint is a cascade of ever-smaller spatial structures that pinches off in finite time, forming a **naked singularity**. Thus cosmic censorship appears to hold in 4D but to be violated in 5D.

**Section 7: Long-term impact.**

*§7.1 Boundaries and conformal diagrams.* Penrose's conformal compactification [245, 246, 249] gives conformal boundaries; Friedrich developed the conformal field equations. Other constructions: g-boundary (Geroch), b-boundary (Schmidt), a-boundary, causal c-boundary (Geroch-Kronheimer-Penrose).

*§7.2 Trapped submanifolds.* The mean curvature vector H^mu is the right object to characterize trapping in arbitrary codimension. For a spacelike zeta of dimension (n-m), the shape tensor K^nu_AB is defined by e^mu_A nabla_mu e^nu_B = Gamma_bar^C_AB e^nu_C - K^nu_AB. Its trace is H^mu = gamma^AB K^mu_AB. Trapping classification (Table 1) for co-dimension 2:
- future trapped: theta^+ < 0, theta^- < 0
- weakly future trapped: theta^+ <= 0, theta^- <= 0
- marginally future trapped (MTS): theta^+ = 0, theta^- <= 0 (or swap)
- stationary or minimal: theta^+ = 0, theta^- = 0 (H^mu = 0)

MOTS (marginally outer trapped surfaces) replace event horizons as quasilocal black-hole boundaries. Dynamical horizons and future trapping horizons are spacelike/null foliations by MOTS. Stability of MOTS is controlled by an elliptic operator whose principal real eigenvalue gives stability. "Clairvoyance" of trapped surfaces: trapped surfaces can extend to flat regions of spacetime. The concept of "core of a black hole" as the minimal region sustaining all closed future-trapped surfaces has been developed. Penrose inequality and Hoop conjecture are two major directions.

**§7.3 Isoperimetric inequalities and the Hoop conjecture.** Penrose inequality: Area(S) <= 16 pi M^2 (Eq. 14 in the paper's numbering), proven in the Riemannian (time-symmetric) case by Huisken-Ilmanen [185] and Bray [47]. Hoop conjecture (Thorne): black hole horizons form when, and only when, a mass gets compacted so its circumference in every direction is C . 4 pi G M/c^2.

**Section 8: 21st century singularity theorems.**

*§8.1 Mathematical advances.* Pre-requisites for C^{1,1} Lorentzian metrics (Kunzinger et al.). Theorems for infinite-space (open) cosmological spacetimes in which a closed trapped surface partly outside a BH horizon exists [313]; this gives some information on singularity location and implies the Universe contains causally disconnected regions.

*§8.2 Quantum effects.* Averaged energy conditions survive quantum violations. Fewster-Galloway singularity theorem under weakened energy conditions. Ford's point that quantum fluctuations of spacetime itself may invalidate pointwise focusing.

*§8.3 Inflation and Lambda > 0.* Effectively a violation of the curvature condition. Borde-Vilenkin: weak energy condition violations alone don't save inflation from past geodesic incompleteness; Borde-Guth-Vilenkin (2003) confirmed past incompleteness of inflationary spacetimes as long as an appropriate averaged Hubble parameter is positive. Lambda > 0 has the wrong sign for (6); Galloway and others have incorporated it explicitly in modified theorems, raising the number of topological possibilities especially in higher dimensions.

*§8.4 Averages.* Raychaudhuri (1998) showed non-rotating singularity-free open cosmologies must have vanishing space-time averages. Senovilla (2007-2008): for a globally-hyperbolic spacetime with non-compact Cauchy Sigma, positive everywhere expansion K, non-negative averaged energy density/scalar curvature, Lambda >= 0, and (6) along the normal congruence, non-vanishing of any of (Lambda, averaged energy density, minus averaged scalar curvature) implies past timelike geodesic incompleteness. Physical interpretation: geodesically complete models have vanishing spatial averages, ergo are not "cosmological" in the realistic sense.

*§8.5 Trapped submanifolds of arbitrary dimension and extra space dimensions.* Galloway-Senovilla (2010) [133]: for a spacelike submanifold zeta of codimension m, if the expansion theta_n is initially negative and the curvature tensor satisfies

  R_mu_nu_rho_sigma N^mu N^rho P^nu_sigma >= 0     (Eq. 15)

along a geodesic normal to zeta, then there is a focal point to zeta along gamma at or before affine parameter u = (m - n)/theta_n. This reduces to (6) for co-dimension 1 or 2. For m > 2, (15) is interpreted physically as "tidal force in directions initially tangent to zeta is attractive on average". The Penrose and Hawking-Penrose theorems survive with (15) replacing (6), and arbitrary-codimension closed trapped submanifolds replacing the closed trapped surface. **Application to extra-dimensional spaces:** Penrose himself in 2003 [254] argued that compactified extra spatial dimensions are classically unstable due to singularity theorems, developing singularities "within a tiny fraction of a second". His original argument needed ad-hoc splittings and restrictions on Ricci tensors because Theorems 2 and 3 applied only to co-dimensions 1, 2, and 4. With the Galloway-Senovilla generalization, the basic argument acquires wider applicability — it suffices that the compact extra-dimensional space **or any of its compact lower-dimensional subsets** satisfy the trapping condition, while the restriction on Ricci curvatures is replaced by the averaged tidal-force condition.

## Key Results

1. **Theorem 2 (Penrose 1965)**: non-compact Cauchy Sigma + closed future-trapped surface + null convergence => future incomplete null geodesics.
2. **Raychaudhuri equation and the focusing effect** (Eq. 4): the source of all singularity theorems.
3. **Closed trapped surface** defined by theta_+ < 0, theta_- < 0 (Eq. 8); equivalently, mean curvature vector H^mu is future-timelike. Stable under small perturbations.
4. **Hawking-Penrose theorem (Theorem 3)**: the preeminent singularity theorem. Convergence + generic + no CTC + one of three trapped alternatives => causal geodesic incompleteness.
5. **Pattern singularity theorem (Theorem 4)**: curvature + causality + boundary/initial condition => incomplete geodesics.
6. **Geodesic completeness requires failure of the boundary/initial condition** (not just failure of one of the other hypotheses).
7. **CFJS singularity-free perfect fluid model [55]** and Einstein/de Sitter/Godel spacetimes: explicit examples of geodesically-complete spacetimes satisfying many (but not all) of the hypotheses.
8. **BKL conjecture** confirmed numerically and mathematically in Gowdy, U(1), and generic cases.
9. **Penrose inequality** proven in the Riemannian case (Huisken-Ilmanen, Bray).
10. **Galloway-Senovilla arbitrary-codimension singularity theorem (§8.5)** with curvature condition (15) generalizes Penrose/Hawking-Penrose to trapped submanifolds of any codimension.
11. **Penrose's 2003 argument for classical instability of compactified extra dimensions [254]** is placed on firmer footing by (15).
12. **Effort-based result**: black strings form naked singularities (cosmic censorship violation in 5D).

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Einstein eq | R_mu_nu - (1/2) R g_mu_nu + Lambda g_mu_nu = (8 pi G/c^4) T_mu_nu | Eq. 1 |
| Raychaudhuri | u^nu nabla_nu nabla_mu u^mu + nabla_mu u_nu nabla^nu u^mu - nabla_mu(u^nu nabla_nu u^mu) + R_rho_nu u^rho u^nu = 0 | Eq. 4 |
| Expansion | theta = nabla_mu u^mu | Eq. 5 |
| Convergence condition | R_rho_nu u^rho u^nu >= 0 | Eq. 6 |
| Perfect fluid | T_mu_nu = rho u_mu u_nu + p(g_mu_nu + u_mu u_nu) | Eq. 7 |
| Future trapped (Penrose) | theta_+ < 0, theta_- < 0 | Eq. 8 |
| Generic condition | u_[rho R_alpha]_beta lambda_[mu u_sigma] u^beta u^lambda != 0 | Eq. 9 |
| Critical scaling (Choptuik) | M ~ (p - p*)^gamma | Eq. 10 |
| Penrose inequality | Area(S) <= 16 pi (G M/c^2)^2 | Eq. 14 |
| GS curvature condition | R_mu_nu_rho_sigma N^mu N^rho P^nu_sigma >= 0 | Eq. 15 |
| Area-angular momentum | Area(S) >= 8 pi |J| | §7.3 |
| Positive-mass-like | M >= |Q|, M >= sqrt(|J|) | §7.3 |

## Relevance to Phonon-Exflation

This review's section 8.5 is the single most directly on-point result for the phonon-exflation framework. Penrose's 2003 argument [254] that classically compactified extra dimensions are unstable, placed on rigorous footing by the Galloway-Senovilla arbitrary-codimension theorem using the averaged curvature condition (Eq. 15), is the direct "no-go" that the framework must navigate. In particular: the framework's SU(3) fiber is a compact internal space, so if the fiber were **static** and tidal forces along the fiber were attractive on average, the framework would face classical geodesic incompleteness in a tiny fraction of a second (in the emergent-GR description). The phonon-exflation escape is that the internal SU(3) fiber is **dynamical in tau** (the Jensen deformation), so the "static internal space" assumption of Penrose-Galloway-Senovilla simply does not apply. This parallels the escape route for the GMN no-go (Faruk 2024, Russo-Townsend 2019): dynamical internal geometry evades the static-compactification singularity theorems. The block-diagonality theorem for D_K is the substrate-level analog of Birkhoff rigidity, and the framework's "L-3 PET" (Level-3 Penrose-type theorem applied to internal SU(3)) should be read against §5.1.3's point that the initial/boundary condition, not just curvature and causality, is what ultimately forces incompleteness. The WCH hypothesis (|C|^2 = 5/14 minimum but non-zero at tau = 0) and the Petrov-type transition D -> II at the dump point correspond, at the emergent-GR level, to the regions near the "singularity" where the pattern theorem's conclusion activates — but the substrate description extends through this region, analogously to Senovilla's regular-black-hole extensions (§4.2 of Senovilla's Critical Appraisal, and mentioned here too). Finally, the BKL conjecture's spacelike/local/oscillatory picture of cosmological singularities is an appropriate comparison point for the framework's "first-order phase transition at the fold (tau = 0.190), no singularity" statement: where BKL predicts chaotic oscillation, the framework predicts integrable ordered GGE relic behavior.
