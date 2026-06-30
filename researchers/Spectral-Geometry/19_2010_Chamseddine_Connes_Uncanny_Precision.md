# The Uncanny Precision of the Spectral Action

**Author(s):** Ali H. Chamseddine, Alain Connes
**Year:** 2010 (posted 2008)
**Journal:** [INCOMPLETE - not extractable from source]
**arXiv:** 0812.0165
**Relevance:** HIGH

---

## Abstract

Noncommutative geometry has been slowly emerging as a new paradigm of geometry which starts from quantum mechanics. One of its key features is that the new geometry is spectral in agreement with the physical way of measuring distances. In this paper we present a detailed introduction with an overview on the study of the quantum nature of space-time using the tools of noncommutative geometry. In particular we examine the suitability of using the spectral action as action functional for the theory. To demonstrate how the spectral action encodes the dynamics of gravity we examine the accuracy of the approximation of the spectral action by its asymptotic expansion in the case of the round sphere S^3. We find that the two terms corresponding to the cosmological constant and the scalar curvature term already give the full result with remarkable accuracy. This is then applied to the physically relevant case of S^3 x S^1 where we show that the spectral action in this case is also given, for any test function, by the sum of two terms up to an astronomically small correction, and in particular all higher order terms a_{2n} vanish. This result is confirmed by evaluating the spectral action using the heat kernel expansion where we check that the higher order terms a_4 and a_6 both vanish due to remarkable cancelations. We also show that the Higgs potential appears as an exact perturbation when the test function used is a smooth cutoff function.

---

## Key Arguments and Derivations

### 1. Spectral Triple and Reconstruction

The paper reviews the spectral triple framework (A, H, D): commutative A recovers Riemannian geometry via the reconstruction theorem. The kinematical conditions include:
- [[D, a], b] = 0 (order one)
- The "Heisenberg type" relation: sum_alpha a_0^alpha [[D, a_1^alpha], ..., [D, a_n^alpha]] = 1 (orientability, encoding sqrt(g) * volume form)

The KO-dimension shift from 4 to 10 = 4 + 6 (mod 8) = 2 (mod 8) is key: the Standard Model with neutrino mixing favors this shift, related to Majorana-Weyl fermions.

### 2. The Finite Geometry F

Classification of finite spectral triples with KO-dimension 6 yields A_F = M_2(H) + M_4(C) as the simplest solution. This selects 16 as the number of physical fermions per generation, gauge group U(1) x SU(2) x SU(3), right-handed neutrinos, and the see-saw mechanism. The order one condition [[D, a], b^0] = 0 reduces SU(2)^2 x SU(4) to the SM gauge group.

### 3. The Spectral Action

The spectral action Tr(f(D/Lambda)) with asymptotic expansion:

Tr(f(D/Lambda)) ~ 2 Lambda^4 f_4 a_0 + 2 Lambda^2 f_2 a_2 + f(0) a_4

where f_4 = integral_0^infty f(u) u^3 du, f_2 = integral_0^infty f(u) u du, f_0 = f(0). For a cutoff function (f constant near 0), all higher-order terms vanish since f^{(2k)}(0) = 0.

Properties: simplicity (counts eigenvalues in [-Lambda, Lambda]), positivity, invariance under the full unitary group of H (stronger than diffeomorphism invariance). Unimodular gravity removes the cosmological term.

### 4. Spectral Action on S^3 (Round Sphere)

The Dirac spectrum on S^n of unit radius is {+/-(n/2 + k) : k >= 0} with multiplicity 2^{[n/2]} C(k+n-1, k). For S^3, the spectrum is Z \ {-1, 0, 1} with total multiplicity of +/-m equal to (4/3)(m^3 - m), giving:

Tr(|D|^{-s}) = zeta(s-3) - zeta(s-1)

The average part of the eigenvalue counting function N(Lambda) is defined via zeta function residues:

<N(Lambda)> = sum_{k>0} (Lambda^k / k) Res_{s=k} zeta_D(s) + zeta_D(0)

### 5. Precision Estimate for S^3 x S^1

For the 4-dimensional space S^3_a x S^1_beta, the spectral action is determined by the first two terms (cosmological constant + scalar curvature) with an error of order 10^{-sigma^2} where sigma = Lambda * min(a, beta). For the visible universe at inverse temperature beta = 1/(3 K) and cutoff at Planck scale:

- Inner diameter sigma ~ 10^{31} Planck units
- Precision ~ 10^{62} accurate decimal places

All higher Seeley-DeWitt coefficients a_{2n} (n >= 2) vanish for S^3 x S^1, confirmed by local heat kernel computation showing remarkable cancelations in a_4 and a_6.

### 6. Standard Model from M x F

For the product M x F with the spectral action plus fermionic bilinear <J xi, D_A eta>:
- Inner fluctuations give U(1) x SU(2) x SU(3) gauge field and Higgs doublet
- Gauge couplings satisfy unification constraint
- Yukawa coupling constraint: Y^2 = 4g^2, where Y^2 = sum_sigma [(y_nu^sigma)^2 + (y_e^sigma)^2 + 3(y_u^sigma)^2 + 3(y_d^sigma)^2]
- Top mass ~ 1.04 x observed (neglecting lighter Yukawas)
- Higgs quartic coupling lambda(Lambda) ~ g_3^2 b/a^2

The running from unification scale Lambda ~ 10^{17} GeV yields realistic low-energy physics but a Higgs mass ~ 170 GeV (now excluded, indicating new physics between 10^2 and 10^{17} GeV).

### 7. Running of Dimensionful Couplings

For the inverse Newton constant Z_g = 1/G, the running is Z_g = Z_g-bar (1 + (1/2) a_1 k^2/Z_g-bar), showing moderate change from low energy to Planck scale. The Higgs mass term -Lambda^2 H^2 presents a fine-tuning problem, geometrically interpreted as: why is the finite space F so large in Planck units?

---

## Key Results

1. **Spectral action precision**: On S^3 x S^1, the first two terms of the asymptotic expansion reproduce the full spectral action to 10^{62} decimal places.

2. **Vanishing of higher coefficients**: a_{2n} = 0 for n >= 2 on S^3 x S^1, verified by both direct computation and heat kernel expansion.

3. **SM from spectral action**: A_F = M_2(H) + M_4(C) yields the full Standard Model with neutrino mixing, Higgs mechanism, and see-saw.

4. **Yukawa constraint**: Y^2 = 4g^2 at unification scale.

5. **Geometric hierarchy problem**: Size of F in Planck units parallels the size of space.

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Spectral action | $\mathrm{Tr}(f(D/\Lambda)) \sim 2\Lambda^4 f_4 a_0 + 2\Lambda^2 f_2 a_2 + f(0)a_4$ | Eq. (8) |
| Full expansion | $\mathrm{Tr}(f(D/\Lambda)) \sim 2\Lambda^4 f_4 a_0 + 2\Lambda^2 f_2 a_2 + f_0 a_4 + \ldots + \Lambda^{-2k}f_{-2k}a_{4+2k} + \ldots$ | Eq. (7) |
| Distance formula | $\mathrm{Distance}(x,y) = \sup\{|f(x)-f(y)| : \|[D,f]\|\leq 1\}$ | Sec. 1 |
| Orientation | $\sum_\alpha a_0^\alpha[[D,a_1^\alpha],\ldots,[D,a_n^\alpha]] = 1$ | Eq. (1) |
| Volume form | $\sqrt{g}\,d^4x = \sum_\alpha a_0^\alpha da_1^\alpha \wedge \ldots \wedge da_4^\alpha$ | Eq. (9) |
| Inner fluctuation | $D_A = D + A + JAJ^{-1},\; A = \sum a_j[D,b_j]$ | Eq. (10) |
| Yukawa constraint | $Y^2 = 4g^2$ | Eq. (11) |
| Newton running | $Z_g = \bar{Z}_g(1 + \frac{1}{2}a_1\frac{k^2}{\bar{Z}_g})$ | Eq. (12) |
| S^4 zeta | $\mathrm{Tr}(|D|^{-s}) = \frac{4}{3}(\zeta(s-3) - \zeta(s-1))$ | Eq. (27) |
| Average N | $\langle N(\Lambda)\rangle = \sum_{k>0}\frac{\Lambda^k}{k}\mathrm{Res}_{s=k}\zeta_D(s) + \zeta_D(0)$ | Eq. (25) |
| Heat-zeta relation | $\mathrm{Res}_{s=-2\alpha}\zeta_D(s) = \frac{2a_\alpha}{\Gamma(-\alpha)}$ | Eq. (17) |
| f moments | $f_4 = \int_0^\infty f(u)u^3\,du,\; f_2 = \int_0^\infty f(u)u\,du,\; f_0 = f(0)$ | Sec. 1 |

---

## Relevance to Phonon-Exflation

This paper provides the quantitative foundation for the spectral action computations in the phonon-exflation framework. The precision analysis on S^3 x S^1 directly informs the project's spectral action calculations on M4 x SU(3), where the tau-dependent fiber geometry replaces the simple circle. The vanishing of higher Seeley-DeWitt coefficients a_{2n} for n >= 2 on the round product is a benchmark against which the project's non-trivial tau-dependent results (where a_4 does NOT generally vanish) can be compared. The paper's derivation of the Standard Model from A_F = M_2(H) + M_4(C) is the starting point for the project's analysis of how SM parameters emerge from the D_K(tau) spectrum during compactification. The identified tension between the predicted 170 GeV Higgs and the observed 125 GeV is one of the open questions the project's instanton gas physics could potentially address.
