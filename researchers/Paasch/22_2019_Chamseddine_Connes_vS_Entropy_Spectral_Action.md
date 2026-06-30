# Entropy and the Spectral Action

**Author(s):** Ali H. Chamseddine, Alain Connes, Walter D. van Suijlekom
**Year:** 2018
**Journal:** [not stated in PDF]
**arXiv:** 1809.02944
**Relevance:** CRITICAL

---

## Abstract

We compute the information theoretic von Neumann entropy of the state associated to the fermionic second quantization of a spectral triple. We show that this entropy is given by the spectral action of the spectral triple for a specific universal function. The main result of our paper is the surprising relation between this function and the Riemann zeta function. It manifests itself in particular by the values of the coefficients c(d) by which it multiplies the d dimensional terms in the heat expansion of the spectral triple. We find that c(d) is the product of the Riemann xi function evaluated at -d by an elementary expression. In particular c(4) is a rational multiple of zeta(5) and c(2) a rational multiple of zeta(3). The functional equation gives a duality between the coefficients in positive dimension, which govern the high energy expansion, and the coefficients in negative dimension, exchanging even dimension with odd dimension.

---

## Key Arguments and Derivations

### 1. From Spectral Triple to Entropy

Given a spectral triple (A, H, D), the fermionic second quantization uses the Clifford algebra C = Cliff_C(H_R) of the underlying real Hilbert space. The operator D generates a one-parameter automorphism group sigma_t = Cliff(e^{itD}). For any inverse temperature beta > 0, there exists a unique KMS_beta state on the C*-dynamical system (C, sigma_t).

### 2. Physical Fock Representation

The key step is choosing the complex structure I = i*sign(D) on H_R (rather than the natural complex structure from H). This is the Dirac sea construction: it fills all negative-energy states, making D act as |D| with only positive eigenvalues. The KMS state is then implemented by the density matrix rho = Lambda(exp(-beta|D|)) in Fock space.

### 3. Entropy = Spectral Action

**Theorem 3.4 (Main Result):** The von Neumann entropy of the KMS_beta state equals the spectral action Tr(h(beta*D)) for the universal test function:

h(x) = E(e^{-x}) where E(t) = log(1+t) - t*log(t)/(1+t)

This function h(x) is even, positive, and satisfies h'(x) = -x/(4 cosh^2(x/2)).

Taylor expansion: h(sqrt(x)) = log(2) - x/8 + x^2/64 - x^3/576 + 17x^4/92160 - ...

### 4. Connection to Riemann Zeta Function

The moments of h are:
- 2 integral_0^infty h(x) x dx = (9/2) zeta(3)
- 2 integral_0^infty h(x) x^3 dx = (225/4) zeta(5)

More generally: integral_0^infty h(x) x^alpha dx = ((1 - 2^{-alpha-1})/(alpha+1)) * Gamma(alpha+3) * zeta(alpha+2)

### 5. Heat Expansion Coefficients

The coefficient gamma(a) of t^a in the heat expansion is:

gamma(a) = (1 - 2^{-2a})/(a) * pi^{-a} * xi(2a)

where xi is Riemann's xi function xi(s) = (1/2)s(s-1)pi^{-s/2} Gamma(s/2) zeta(s).

Key values:
- gamma(-2) = (225/4) zeta(5)
- gamma(-3/2) = 14 pi^{7/2}/45
- gamma(-1) = (9/2) zeta(3)
- gamma(-1/2) = pi^{3/2}/3
- gamma(0) = log(2)
- gamma(1/2) = 1/(2 sqrt(pi))
- gamma(1) = 1/8
- gamma(3/2) = 7 zeta(3)/(8 pi^{5/2})
- gamma(2) = 1/32
- gamma(5/2) = 93 zeta(5)/(32 pi^{9/2})

### 6. Functional Equation Duality

The functional equation of the Riemann zeta function creates a duality: coefficients in positive dimension (governing the high-energy/UV expansion) are related to coefficients in negative dimension (governing the low-energy/IR expansion), exchanging even and odd dimensions. Even-dimensional UV coefficients involve odd zeta values (zeta(3), zeta(5), ...), while odd-dimensional UV coefficients involve powers of pi.

## Key Results

1. The von Neumann entropy of the fermionic second quantization of a spectral triple IS the spectral action for the universal function h(x) = E(e^{-x})
2. The heat expansion coefficients gamma(a) are products of the Riemann xi function at -2a and an elementary prefactor
3. c(4) = (225/4) zeta(5) and c(2) = (9/2) zeta(3) — odd zeta values appear in even-dimensional terms
4. The functional equation of zeta creates a UV/IR duality exchanging even and odd dimensions
5. The entropy function h is unique (determined by KMS condition + Clifford algebra structure)
6. gamma(0) = log(2) — the zero-dimensional coefficient is exactly the entropy of one bit
7. All coefficients are determined — no free parameters in the entropy spectral action

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Entropy function | $h(x) = E(e^{-x}) = \frac{x}{1+e^x} + \log(1+e^{-x})$ | Theorem 3.4 |
| Derivative | $h'(x) = -\frac{x}{4\cosh^2(x/2)}$ | Lemma 4.1 |
| Moments | $\int_0^\infty h(x)x^\alpha\,dx = \frac{1-2^{-\alpha-1}}{\alpha+1}\Gamma(\alpha+3)\zeta(\alpha+2)$ | Eq. (12) |
| Heat coefficient | $\gamma(a) = \frac{1-2^{-2a}}{a}\pi^{-a}\xi(2a)$ | Lemma 4.6 |
| 4D coefficient | $\gamma(-2) = \frac{225}{4}\zeta(5)$ | Table in Sec. 4 |
| 2D coefficient | $\gamma(-1) = \frac{9}{2}\zeta(3)$ | Table in Sec. 4 |
| 0D coefficient | $\gamma(0) = \log 2$ | Table in Sec. 4 |

## Relevance to Phonon-Exflation

This paper is one of the most important theoretical foundations for the phonon-exflation framework. The result that entropy IS the spectral action — for a universal, parameter-free test function — means that the thermodynamics of the SU(3) fiber is completely determined by its spectral geometry. In the framework's BCS formalism, the von Neumann entropy of the post-transit GGE state is a spectral action, and its heat expansion coefficients are the a_2 and a_4 Seeley-DeWitt coefficients that control the tau-dependent effective potential. The fact that c(4) involves zeta(5) and c(2) involves zeta(3) provides exact, computable values for these coefficients — no approximation needed. The UV/IR duality from the functional equation connects the high-energy spectral structure (relevant during the transit) to the low-energy effective theory (relevant for cosmological observables). The gamma(0) = log(2) result is the entropy per fermionic mode, directly relevant to the counting of degrees of freedom in the instanton gas. Session 37's spectral post-mortem identified that the spectral action is the wrong functional for BCS physics — this paper clarifies why: the BCS entropy requires the second-quantized spectral action (this paper), not the first-quantized spectral action used in the standard NCG framework.
