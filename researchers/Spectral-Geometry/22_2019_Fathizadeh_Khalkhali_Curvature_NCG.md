# Curvature in Noncommutative Geometry

**Author(s):** Farzad Fathizadeh and Masoud Khalkhali
**Year:** 2019 (revised 2020)
**Journal:** [INCOMPLETE - not extractable from source]
**arXiv:** 1901.07438
**Relevance:** MEDIUM

---

## Abstract

Our understanding of the notion of curvature in a noncommutative setting has progressed substantially in the past 10 years. This new episode in noncommutative geometry started when a Gauss-Bonnet theorem was proved by Connes and Tretkoff for a curved noncommutative two torus. Ideas from spectral geometry and heat kernel asymptotic expansions suggest a general way of defining local curvature invariants for noncommutative Riemannian type spaces where the metric structure is encoded by a Dirac type operator. To carry explicit computations however one needs quite intriguing new ideas. We give an account of the most recent developments on the notion of curvature in noncommutative geometry in this paper.

---

## Key Arguments and Derivations

**Heat kernel approach to curvature.** The central strategy is to extract curvature from heat kernel asymptotics: for a Laplace type operator $P$, the heat kernel $k(t, x, x)$ admits the expansion $k(t,x,x) \sim (4\pi t)^{-m/2} \sum_{k \geq 0} a_{2k}(x, P) t^k$, where the Gilkey-Seeley-DeWitt coefficients $a_{2k}$ encode curvature. $a_0 = \text{tr}(1)$ gives volume, $a_2 = \text{tr}(E - R/6)$ gives scalar curvature.

**Gauss-Bonnet for noncommutative tori.** For the noncommutative 2-torus $T^2_\theta$ with conformally perturbed metric $g = e^h(dx^2 + dy^2)$, the spectral formulation $\zeta(0) + 1 = \frac{1}{6}\chi(M)$ provides the correct generalization. The scalar curvature formula in the noncommutative case is much more complicated than the classical $K = -\frac{1}{2}e^{-h}\Delta h$, involving modular automorphisms and divided differences.

**Pseudodifferential calculus.** The computation requires Connes' pseudodifferential calculus for $C^*$-dynamical systems. The "rearrangement lemma" and Newton divided differences play a key technical role in organizing the non-trivial algebraic expressions that arise.

**Scalar curvature of NC 4-tori.** The paper extends curvature computations to noncommutative 4-tori, computing the term $a_4$ which classically contains the Riemann tensor components. Functional relations between the modular operator and curvature components are derived.

**Ricci curvature.** Using a Weitzenbock formula $D^2 = \nabla^*\nabla + \mathcal{K}$, the Ricci curvature is defined as a spectral functional. For the curved NC 2-torus, explicit formulas are obtained.

**Beyond conformally flat metrics.** The paper discusses extensions to non-conformally flat metrics, warped products, and matrix-valued metrics, including a matrix Gauss-Bonnet theorem.

## Key Results

1. Gauss-Bonnet theorem for noncommutative 2-torus with general conformal structures
2. Explicit scalar curvature formulas for NC 2-tori and NC 4-tori involving modular automorphisms
3. The term $a_4$ for NC 4-tori with non-conformally flat metrics, containing Riemann tensor analogue
4. Ricci curvature as a spectral functional via Weitzenbock formula
5. Matrix Gauss-Bonnet theorem for matrix-valued metrics
6. Curvature of the determinant line bundle for NC tori

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Weyl's law | $N(\lambda) \sim \frac{\omega_n \text{Vol}(M)}{(2\pi)^n} \lambda^{n/2}$ | Eq. (1) |
| Spectral zeta function | $\zeta(s) = \sum \lambda_j^{-s}$ | Eq. (2) |
| Gilkey $a_0$ | $a_0(x, P) = \text{tr}(1)$ | Sec. 2.2 |
| Gilkey $a_2$ | $a_2(x, P) = \text{tr}(E - R/6)$ | Sec. 2.2 |
| Gilkey $a_4$ | $a_4(x,P) = \frac{1}{360}\text{tr}(-12R_{;kk} + 5R^2 - 2R_{jk}R^{jk} + 2R_{ijkl}R^{ijkl} - 60RE + 180E^2 + 60E_{;kk} + 30\Omega_{ij}\Omega^{ij})$ | Sec. 2.2 |
| Lichnerowicz formula | $D^2 = \nabla^*\nabla - \frac{1}{4}R$ | Sec. 2.2 |
| Laplace type operator | $P = -g^{ij}\partial_i\partial_j + \text{lower orders}$ | Sec. 2.2 |
| Classical Gaussian curvature | $K = -\frac{1}{2}e^{-h}\Delta h$ for $g = e^h(dx^2 + dy^2)$ | Sec. 2.1 |

## Relevance to Phonon-Exflation

This review provides the mathematical foundations for computing curvature invariants (scalar, Ricci) on the noncommutative fiber geometry of the M4 x SU(3) spectral triple. The Seeley-DeWitt coefficients $a_0, a_2, a_4$ computed here are exactly the quantities that enter the spectral action expansion, which the project uses to analyze stabilization mechanisms ($a_4/a_2$ ratio). The discussion of heat kernel asymptotics for curved NC spaces directly underpins the spectral action computations at the core of the framework.
