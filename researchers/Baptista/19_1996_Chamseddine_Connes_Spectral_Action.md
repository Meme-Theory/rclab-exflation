# The Spectral Action Principle

**Author(s):** Ali H. Chamseddine and Alain Connes
**Year:** 1996
**Journal:** Communications in Mathematical Physics 186 (1997) 731-750
**arXiv:** hep-th/9606001
**Relevance:** CRITICAL

---

## Abstract

We propose a new action principle to be associated with a noncommutative space (A, H, D). The universal formula for the spectral action is (psi, D psi) + Trace(chi(D/Lambda)) where psi is a spinor on the Hilbert space, Lambda is a scale and chi a positive function. When this principle is applied to the noncommutative space defined by the spectrum of the standard model one obtains the standard model action coupled to Einstein plus Weyl gravity. There are relations between the gauge coupling constants identical to those of SU(5) as well as the Higgs self-coupling, to be taken at a fixed high energy scale.

---

## Key Arguments and Derivations

### Section 1: Introduction

The paper begins by recalling that the laws of physics are encoded by the action functional I = I_E + I_SM, where I_E is the Einstein action and I_SM is the standard model action. The symmetry group of this action is the semidirect product G = U ⋊ Diff(M) of local gauge transformations and diffeomorphisms.

The authors recall that in noncommutative geometry, one replaces the manifold M by a spectral triple (A, H, D): an involutive algebra A of operators on a Hilbert space H together with a self-adjoint unbounded operator D. For a Riemannian spin manifold, A = C^infty(M), H = L^2(M, S) (L^2 spinors), and D is the Dirac operator. No information is lost in this trade. The geodesic distance is recovered by d(x,y) = Sup{|a(x) - a(y)| ; a in A, ||[D,a]|| <= 1}.

The key axioms include a Z/2 grading gamma with gamma D = -D gamma, and a real structure J satisfying J^2 = epsilon, JD = epsilon' DJ, J gamma = epsilon'' gamma J where epsilon, epsilon', epsilon'' in {-1, 1} are determined by n mod 8.

The crucial new hypothesis is: "The physical action only depends upon Sigma" (the spectrum of D). This is stronger than diffeomorphism invariance.

The algebra for the Standard Model is identified as A = C^infty(M) tensor A_F, where A_F = C + H + M_3(C) (complex numbers, quaternions, 3x3 matrices). The product geometry gives H = L^2(M,S) tensor H_F, D = slashed-partial_M tensor 1 + gamma_5 tensor D_F, where D_F is the Yukawa coupling matrix.

Inner fluctuations of the metric are given by D = D_0 + A + JAJ^{-1}, where A = sum a_i[D_0, b_i]. For M x F, these fluctuations are parametrized exactly by the SM gauge bosons (gamma, W^pm, Z, gluons) and the Higgs field.

The central claim is verified: Trace chi(D/Lambda) = I_E + I_G + I_GH + I_H + I_C + O(Lambda^{-infty}), reproducing the full bosonic SM action coupled to Einstein-Weyl gravity.

### Section 2: Einstein-Yang-Mills System

As a warmup, the authors consider A = C^infty(M) tensor M_N(C). The Dirac operator with internal fluctuations is D = e^mu_a gamma^a((partial_mu + omega_mu) tensor 1_N + 1 tensor (-i/2 g_0 A^i_mu T^i)). They compute D^2 and apply the heat kernel expansion.

Using Tr e^{-tP} ~ sum_{n>=0} t^{(n-m)/d} integral a_n(x,P) dv(x) with m=4, d=2, the spectral action Tr chi(P) ~ sum f_n a_n(P) with moments f_0 = integral chi(u) u du, f_2 = integral chi(u) du, f_{2(n+2)} = (-1)^n chi^{(n)}(0).

The Seeley-DeWitt coefficients are computed:
- a_0(P) = (N/4pi^2) integral sqrt(g) d^4x
- a_2(P) = (N/48pi^2) integral sqrt(g) R d^4x
- a_4(P) = (1/16pi^2)(N/360) integral d^4x sqrt(g) [(12 R^{;mu}_{mu} + 5R^2 - 8 R_{mu nu} R^{mu nu} - 7 R_{mu nu rho sigma} R^{mu nu rho sigma}) + (120/N) g^2 F^i_{mu nu} F^{mu nu i}]

Using the Gauss-Bonnet relation and Weyl tensor, the bosonic action becomes I_b with Einstein, Yang-Mills, Weyl gravity (C_{mu nu rho sigma}^2), Euler (R*R*), and cosmological terms.

Normalization conditions yield: N m_0^2 f_2 / 24pi^2 = 1/kappa_0^2 = 1/(8 pi G_0) and f_4 g_0^2 / 12pi^2 = 1.

### Section 3: Standard Model

The full SM spectral triple is described. The algebra is A_2 = C + H + M_3(C). The Hilbert space H_2 has basis given by quarks Q = (u_L, d_L, d_R, u_R) and leptons L = (nu_L, e_L, e_R). The Dirac operator D_2 contains the Yukawa coupling matrices k^d_0, k^u_0, k^e_0 (3x3 family mixing matrices).

Inner fluctuations produce the gauge fields B_mu (U(1)), A^alpha_mu (SU(2)_w), V^i_mu (SU(3)_c) with gauge couplings g_{01}, g_{02}, g_{03}, plus the Higgs doublet H.

The bosonic spectral action for the Standard Model yields (Eq. 3.16):

I = (9m_0^4/pi^2)(5/4)f_0 integral sqrt(g) d^4x + (3m_0^2/4pi^2) f_2 integral sqrt(g) [(5/4)R - 2y^2 H*H] + (f_4/4pi^2) integral sqrt(g) [gravity terms + 3y^2(D_mu H* D^mu H - R/6 H*H) + g_{03}^2 G^i_{mu nu} G^{mu nu i} + g_{02}^2 F^alpha_{mu nu} F^{mu nu alpha} + (5/3) g_{01}^2 B_{mu nu} B^{mu nu} + 3z^2 (H*H)^2 - y^2 (H*H)^{;mu}_{mu}]

where y^2 = Tr(|k^d_0|^2 + |k^u_0|^2 + (1/3)|k^e_0|^2) and z^2 = Tr((|k^d_0|^2 + |k^u_0|^2)^2 + (1/3)|k^e_0|^4).

After normalization, the gauge coupling unification conditions emerge: g_{03}^2 = g_{02}^2 = (5/3) g_{01}^2, identical to SU(5) unification.

### Section 4: Conclusions and Predictions

The RG equations with SM content give:
- Unification scale Lambda ~ 10^15 GeV
- sin^2(theta_w) ~ 0.21 (10% off experimental 0.2325)
- Higgs mass prediction: 160 - 180 GeV (from lambda_0 = (4/3) g_{03}^2 (z^2/y^4) at unification)
- The slight disagreement indicates the SM spectrum must be modified at some intermediate scale

### Appendix

Provides the general formula for heat kernel coefficients for a Dirac operator of block form with off-diagonal scalar S, yielding expressions for a_0, a_2, a_4 in terms of Tr(1), Tr(S^2), Tr(S^4), F_{mu nu}, and curvature invariants.

## Key Results

1. The spectral action Tr chi(D/Lambda) + (psi, D psi) is a universal action principle for noncommutative geometries that reproduces the full Standard Model coupled to gravity
2. Gauge coupling unification: g_3^2 = g_2^2 = (5/3) g_1^2 at the cutoff scale, identical to SU(5)
3. The Higgs self-coupling is predicted: lambda(Lambda) = (16 pi / 3) alpha_3(Lambda)
4. Higgs mass prediction: 160-180 GeV
5. Unification scale Lambda ~ 10^15 GeV
6. sin^2(theta_w) predicted at ~0.21
7. The conformal Higgs coupling xi_0 = 1/6 is predicted
8. The R^2 term has zero bare coupling (b_0 = 0)
9. Inner fluctuations of the product geometry M x F reproduce exactly the SM gauge and Higgs fields

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Spectral action | $\text{Tr}\,\chi(D/\Lambda) + \langle\psi, D\psi\rangle$ | Eq. (1.28) |
| Algebra | $A = C^\infty(M) \otimes (C \oplus H \oplus M_3(C))$ | Eq. (1.16)-(1.17) |
| Product Dirac | $D = \partial\!\!\!/\,_M \otimes 1 + \gamma_5 \otimes D_F$ | Eq. (1.19) |
| Inner fluctuations | $D = D_0 + A + JAJ^{-1},\quad A = \sum a_i[D_0, b_i]$ | Eq. (1.23) |
| Heat expansion | $\text{Tr}\,\chi(P) \simeq \sum_{n\geq 0} f_n\, a_n(P)$ | Eq. (2.14) |
| Moments | $f_0 = \int_0^\infty \chi(u)\,u\,du,\quad f_2 = \int_0^\infty \chi(u)\,du,\quad f_{2(n+2)} = (-1)^n \chi^{(n)}(0)$ | Eq. (2.15) |
| Seeley-DeWitt a_0 | $a_0 = (4\pi)^{-m/2}\,\text{Tr}(\mathbf{1})$ | Eq. (2.16) |
| Seeley-DeWitt a_4 | $a_4 = \frac{(4\pi)^{-m/2}}{360}\text{Tr}[(-12R^{;\mu}_\mu + 5R^2 - 2R_{\mu\nu}R^{\mu\nu} + 2R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma})\mathbf{1} - 60RE + 180E^2 + 60E^{;\mu}_\mu + 30\Omega_{\mu\nu}\Omega^{\mu\nu}]$ | Eq. (2.16) |
| Gauge unification | $g_{03}^2 = g_{02}^2 = \tfrac{5}{3}\,g_{01}^2$ | Eq. (3.18) |
| Weinberg angle | $\sin^2\theta_w = \tfrac{3}{8}\left(1 - \tfrac{109}{18\pi}\alpha_{\rm em}\ln\tfrac{\Lambda}{M_Z}\right)$ | Eq. (3.27) |
| Higgs coupling | $\lambda(\Lambda) = \tfrac{16\pi}{3}\,\alpha_3(\Lambda)$ | Eq. (3.31) |
| Normalized action | $I_b = \int d^4x\sqrt{g}\left[\frac{1}{2\kappa_0^2}R - \mu_0^2 H^*H + a_0 C^2 + \ldots + \frac{1}{4}F^2 + |D_\mu H|^2 - \xi_0 R|H|^2 + \lambda_0(H^*H)^2\right]$ | Eq. (3.20) |
| Bare parameters | $\mu_0^2 = \frac{4}{3\kappa_0^2},\quad a_0 = -\frac{9}{8g_{03}^2},\quad b_0 = 0,\quad \xi_0 = \frac{1}{6}$ | Eq. (3.21) |
| General a_4 formula | $a_4 = \frac{1}{4\pi^2}\int\sqrt{g}\,d^4x\left[\frac{\text{Tr}(1)}{360}(\text{gravity}) + \text{Tr}[(D_\mu S + [A_\mu,S])^2 - \frac{R}{6}S^2] - \frac{1}{6}\text{Tr}\,F_{\mu\nu}F^{\mu\nu} + \text{Tr}\,S^4\right]$ | Eq. (A.6) |

## Relevance to Phonon-Exflation

This is the foundational paper for the spectral action principle used throughout the phonon-exflation framework. The key connections are:

1. **M4 x F product geometry**: The framework uses exactly this product structure M4 x SU(3), where the finite space F is replaced by the internal manifold SU(3). The Seeley-DeWitt coefficients a_0, a_2, a_4 from this paper are the quantities computed in sessions 19d, 20a, 24a of the project.

2. **Heat kernel expansion**: The expansion Tr chi(D^2/Lambda^2) ~ f_0 Lambda^4 a_0 + f_2 Lambda^2 a_2 + f_4 a_4 + ... is the mathematical backbone of the spectral action computations. The project's constant-ratio trap (F/B = 0.55) and monotonicity theorems directly concern the tau-dependence of these coefficients.

3. **Inner fluctuations = gauge fields**: The formula D = D_0 + A + JAJ^{-1} is the mechanism by which the project's Dirac operator D_K(tau) produces physical gauge content. The U(1)_7 breaking by Cooper pairs (Session 35) operates within this framework.

4. **Conformal coupling xi_0 = 1/6**: This prediction appears in the project's analysis of the Higgs-sigma portal (closed Session 22c, Trap 3).

5. **Wilsonian interpretation**: The spectral action as a bare Wilsonian action at cutoff Lambda directly parallels the project's treatment of the spectral action during the tau-transit as describing geometry during transit.
