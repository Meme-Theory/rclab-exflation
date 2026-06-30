# Entropy and the Spectral Action

**Author(s):** Ali H. Chamseddine, Alain Connes and Walter D. van Suijlekom
**Year:** 2018
**Journal:** (preprint)
**arXiv:** 1809.02944
**Relevance:** CRITICAL

---

## Abstract

We compute the information theoretic von Neumann entropy of the state associated to the fermionic second quantization of a spectral triple. We show that this entropy is given by the spectral action of the spectral triple for a specific universal function. The main result of our paper is the surprising relation between this function and the Riemann zeta function. It manifests itself in particular by the values of the coefficients c(d) by which it multiplies the d dimensional terms in the heat expansion of the spectral triple. We find that c(d) is the product of the Riemann xi function evaluated at -d by an elementary expression. In particular c(4) is a rational multiple of zeta(5) and c(2) a rational multiple of zeta(3). The functional equation gives a duality between the coefficients in positive dimension, which govern the high energy expansion, and the coefficients in negative dimension, exchanging even dimension with odd dimension.

---

## Key Arguments and Derivations

### Section 1: Introduction

The spectral action Tr(chi(D^2/Lambda^2)) is additive for direct sums of spectral triples. The authors identify another natural additive functional: the von Neumann entropy of the KMS state arising from fermionic second quantization. Second quantization transforms direct sums into tensor products, and von Neumann entropy is additive for tensor product states, yielding an additive functional called the "entropy" S(A, H, D) of the spectral triple.

The main result: the entropy equals the spectral action for a specific universal test function chi(x) = h(sqrt(x)), where h is intimately related to the Riemann zeta function.

### Section 2: Spectral Triples and Second Quantization

**2.1 KMS condition:** For a C*-dynamical system (C, sigma_t), a KMS_beta state phi satisfies phi(a sigma_t(b))|_{t=i beta} = phi(ba). For a matrix algebra with sigma_t(A) = e^{itH} A e^{-itH}, the unique KMS_beta state is rho = Z e^{-beta H} where Z = 1/Tr(e^{-beta H}).

**Proposition 2.2:** For the Clifford algebra C = Cliff_C(H_R) with sigma_t = Cliff(e^{itD}), there exists a unique KMS_beta state psi_beta for any beta > 0.

**2.2 Fermionic second quantization:** The complex structure I = i sign(D) = i(E_+ - E_-) defines the "physical" Fock representation, where D acts as |D| (only positive eigenvalues). The Dirac sea is filled.

**Proposition 2.6:** The one-parameter group sigma_t is implemented in the physical Fock representation by W(t) = bigwedge exp(it|D|). The KMS_beta state is psi_beta(A) = (1/Z) Tr(bigwedge exp(-beta|D|) gamma_I(A)).

### Section 3: von Neumann Entropy

The von Neumann entropy S(phi) = -Tr(rho log rho) is additive for tensor products.

**Lemma 3.1:** The entropy of a partition into intervals with ratio x is E(x) = log(x+1) - x log(x)/(x+1). Note E(x) = E(1/x).

**Lemma 3.3:** For a positive trace class T and the state from bigwedge T, S(phi) = Tr(E(T)).

**Theorem 3.4 (Main result):** The von Neumann entropy of the KMS_beta state equals the spectral action:

S(psi_beta) = Tr(h(beta D))

where h(x) = E(e^{-x}) = x/(1 + e^x) + log(1 + e^{-x}).

The function h is even, positive, with h'(x) = -x/(4 cosh^2(x/2)).

### Section 4: The Function h and Riemann's xi Function

The Taylor expansion: h(x) = log(2) - x^2/8 + x^4/64 - x^6/576 + 17x^8/92160 - ...

**Lemma 4.2:** 1/(4 cosh^2(sqrt(x)/2)) = sum_Z [(2pi n + pi)^2 - x] / [(2pi n + pi)^2 + x]^2, connecting h' to an Eisenstein series.

**Proposition 4.4:** h has the integral representation h(x) = integral_0^infty e^{-tx^2} g-tilde(t) dt, where g-tilde(t) = g(t)/2t involves the theta function derivative q d_q theta_4(0,q) with q = e^{-1/(4t)}.

**Lemma 4.5 (Key moments):**
- 2 integral_0^infty h(x) x dx = 9 zeta(3)/2
- 2 integral_0^infty h(x) x^3 dx = 225 zeta(5)/4
- General: integral_0^infty h(x) x^alpha dx = (1 - 2^{-alpha-1})/(alpha+1) Gamma(alpha+3) zeta(alpha+2)

**Lemma 4.6 (Main structural result):** The coefficient of t^a in the heat expansion is

gamma(a) = (1 - 2^{-2a}) / a * pi^{-a} xi(2a)

where xi(s) = (1/2) s(s-1) pi^{-s/2} Gamma(s/2) zeta(s) is Riemann's xi function.

This is an entire function of a. The table of values:

| a | gamma(a) |
|:--|:---------|
| -2 | 225 zeta(5)/4 |
| -3/2 | 14 pi^{7/2}/45 |
| -1 | 9 zeta(3)/2 |
| -1/2 | pi^{3/2}/3 |
| 0 | log(2) |
| 1/2 | 1/(2 sqrt(pi)) |
| 1 | 1/8 |
| 3/2 | 7 zeta(3)/(8 pi^{5/2}) |
| 2 | 1/32 |
| 5/2 | 93 zeta(5)/(32 pi^{9/2}) |

The functional equation of xi gives a duality: coefficients in even positive dimension correspond to coefficients in odd negative dimension and vice versa.

## Key Results

1. The von Neumann entropy of the fermionic second quantization of a spectral triple IS a spectral action, with a universal test function h(x) = E(e^{-x})
2. The test function h is intimately related to the Riemann xi function: the heat expansion coefficient is gamma(a) = (1 - 2^{-2a})/a * pi^{-a} xi(2a)
3. In dimension 4: the a_2 coefficient involves zeta(3) and the a_4 coefficient involves zeta(5)
4. The functional equation of the Riemann zeta function produces a duality between high-energy (positive dimension) and low-energy (negative dimension) coefficients
5. The entropy function h is even, positive, with Gaussian-type decay

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Entropy = spectral action | $S(\psi_\beta) = \text{Tr}(h(\beta D))$ | Thm 3.4 |
| Entropy function | $h(x) = E(e^{-x}) = \frac{x}{1+e^x} + \log(1 + e^{-x})$ | After Thm 3.4 |
| Partition entropy | $E(x) = \log(x+1) - \frac{x\log x}{x+1}$ | Lemma 3.1 |
| KMS density | $\rho = \bigwedge\exp(-\beta\lvert D\rvert),\quad Z = \text{Tr}(\rho)$ | Prop 2.6 |
| Derivative | $h'(x) = -\frac{x}{4\cosh^2(x/2)}$ | Lemma 4.1 |
| Heat coefficient | $\gamma(a) = \frac{1-2^{-2a}}{a}\,\pi^{-a}\,\xi(2a)$ | Lemma 4.6 |
| Moments | $\int_0^\infty h(x)\,x^\alpha\,dx = \frac{1-2^{-\alpha-1}}{\alpha+1}\,\Gamma(\alpha+3)\,\zeta(\alpha+2)$ | Eq. (12) |
| 4D moments | $2\int_0^\infty h(x)\,x\,dx = \frac{9\zeta(3)}{2},\quad 2\int_0^\infty h(x)\,x^3\,dx = \frac{225\zeta(5)}{4}$ | Eq. (11) |
| Integral representation | $h(x) = \int_0^\infty e^{-tx^2}\,\tilde{g}(t)\,dt$ | Prop 4.4 |

## Relevance to Phonon-Exflation

1. **Entropy as spectral action:** This provides a thermodynamic interpretation of the spectral action. The project's instanton gas (Session 37-38) and GGE relic state involve exactly the kind of fermionic second quantization studied here. The von Neumann entropy of the post-transit state is computable via this spectral action formula.

2. **Natural test function:** The function h(x) = E(e^{-x}) is distinguished — it is the UNIQUE test function arising from thermodynamic (KMS) considerations. The project has treated the test function chi as arbitrary; this paper selects a canonical choice tied to entropy.

3. **Zeta values in heat coefficients:** The appearance of zeta(3) in a_2 and zeta(5) in a_4 provides specific numerical coefficients for the spectral action expansion on M4 x SU(3). The project's computation of a_2/a_4 hierarchy (Session 24a) could be evaluated with these specific coefficients.

4. **High-energy/low-energy duality:** The functional equation duality between positive and negative dimensional coefficients may be relevant to understanding the relationship between the tau -> 0 (high energy, early universe) and tau -> tau_fold (low energy, late universe) regimes of the framework.

5. **BCS connection:** The fermionic second quantization at inverse temperature beta is precisely the BCS mean-field framework. The KMS state is the BCS ground state at temperature 1/beta. This directly connects to the project's BCS mechanism chain (Session 35).
