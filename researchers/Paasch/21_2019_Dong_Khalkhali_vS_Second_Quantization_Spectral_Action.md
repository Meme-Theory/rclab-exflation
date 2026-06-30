# Second Quantization and the Spectral Action

**Author(s):** Rui Dong, Masoud Khalkhali, Walter D. van Suijlekom
**Year:** 2020 (v2; originally 2019)
**Journal:** [not stated in PDF]
**arXiv:** 1903.09624
**Relevance:** CRITICAL

---

## Abstract

We consider both the bosonic and fermionic second quantization of spectral triples in the presence of a chemical potential. We show that the von Neumann entropy and the average energy of the Gibbs state defined by the bosonic and fermionic grand partition function can be expressed as spectral actions. It turns out that all spectral action coefficients can be given in terms of the modified Bessel functions. In the fermionic case, we show that the spectral coefficients for the von Neumann entropy, in the limit when the chemical potential mu approaches 0, can be expressed in terms of the Riemann zeta function. This recovers a result of Chamseddine-Connes-van Suijlekom.

---

## Key Arguments and Derivations

### 1. Framework: Second Quantization of Spectral Triples

Starting from a spectral triple (A, H, D), the paper constructs both fermionic and bosonic second quantizations. The Fock space construction uses:
- Fermionic: Clifford algebra Cliff_C(H_R) with CAR (canonical anti-commutation relations)
- Bosonic: CCR (canonical commutation relations) algebra

The chemical potential mu is introduced via the grand canonical ensemble, modifying the density matrix from exp(-beta|D|) to exp(-beta(|D| - mu)).

### 2. Fermionic Second Quantization with Chemical Potential

The fermionic grand partition function is:
Z_f(beta, mu) = det(1 + exp(-beta(|D| - mu)))

The von Neumann entropy of the fermionic Gibbs state is:
S_f = Tr(h_f(beta(D^2)^{1/2}, beta*mu))

where h_f(x, y) = E(e^{-(x-y)}) and E is the binary partition entropy function E(t) = log(1+t) - t*log(t)/(1+t).

The spectral action coefficients involve modified Bessel functions K_nu. Specifically, the coefficient of t^{-a} in the heat expansion involves integrals of the form:
integral_0^infty h_f(sqrt(v), y) v^{a-1} dv

### 3. Bosonic Second Quantization with Chemical Potential

For bosons, the grand partition function is:
Z_b(beta, mu) = det(1 - exp(-beta(|D| - mu)))^{-1}

(valid when mu < min|spec(D)|). The von Neumann entropy of the bosonic Gibbs state:
S_b = Tr(h_b(beta(D^2)^{1/2}, beta*mu))

where h_b involves the Bose-Einstein entropy function.

### 4. Spectral Action Coefficients via Bessel Functions

All spectral action coefficients can be expressed in terms of modified Bessel functions of the second kind K_nu(z). For the fermionic entropy:

gamma_f(a, y) = (2/Gamma(a)) * sum_{n=1}^infty (-1)^{n+1} (n*y)^a K_a(n*y) / n

For the bosonic entropy:

gamma_b(a, y) = (2/Gamma(a)) * sum_{n=1}^infty (n*y)^a K_a(n*y) / n

### 5. Recovery of Chamseddine-Connes-van Suijlekom at mu = 0

In the limit mu -> 0 for fermions, the spectral coefficients reduce to expressions involving the Riemann zeta function, recovering the result of Chamseddine, Connes, and van Suijlekom (1809.02944). Specifically:

gamma_f(a, 0) = (1 - 2^{-2a}) * Gamma(2a+2) * zeta(2a+1) / (a * Gamma(a))

### 6. Average Energy as Spectral Action

The average energy <E> = Tr(|D| rho) of the Gibbs state can also be expressed as a spectral action with different coefficients, again expressible in terms of Bessel functions. This provides a complete thermodynamic dictionary translating between spectral geometry and statistical mechanics.

## Key Results

1. Both fermionic and bosonic von Neumann entropies of second-quantized spectral triples are spectral actions
2. All spectral action coefficients are expressible in terms of modified Bessel functions K_nu
3. The average energy of the Gibbs state is also a spectral action
4. At mu = 0, fermionic coefficients reduce to Riemann zeta values (recovering Chamseddine-Connes-vS)
5. The bosonic case requires mu < min|spec(D)| for convergence
6. The chemical potential mu parameterizes a one-parameter family of spectral action test functions
7. The formalism applies to arbitrary spectral triples, not just commutative ones

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Fermionic partition function | $Z_f(\beta,\mu) = \det(1 + e^{-\beta(|D|-\mu)})$ | Sec. 3 |
| Bosonic partition function | $Z_b(\beta,\mu) = \det(1 - e^{-\beta(|D|-\mu)})^{-1}$ | Sec. 4 |
| Fermionic entropy | $S_f = \text{Tr}(h_f(\beta\sqrt{D^2}, \beta\mu))$ | Theorem in Sec. 3 |
| Fermionic coefficient | $\gamma_f(a,y) = \frac{2}{\Gamma(a)}\sum_{n=1}^\infty \frac{(-1)^{n+1}(ny)^a K_a(ny)}{n}$ | Sec. 3 |
| Bosonic coefficient | $\gamma_b(a,y) = \frac{2}{\Gamma(a)}\sum_{n=1}^\infty \frac{(ny)^a K_a(ny)}{n}$ | Sec. 4 |
| mu=0 limit | $\gamma_f(a,0) = \frac{(1-2^{-2a})\Gamma(2a+2)\zeta(2a+1)}{a\,\Gamma(a)}$ | Recovery of CCS |

## Relevance to Phonon-Exflation

This paper is foundational for the phonon-exflation framework's treatment of the spectral action at finite density. The BCS condensate on the SU(3) fiber corresponds precisely to a second-quantized spectral triple at non-zero chemical potential. The Dong-Khalkhali-vS result that the entropy IS the spectral action (for a specific test function involving Bessel functions) means the thermodynamics of the instanton gas/GGE relic can be computed directly from the spectral geometry. The chemical potential mu maps to the BCS gap parameter in the framework's BdG formalism. The distinction between fermionic and bosonic second quantization is essential because the framework's quasiparticle spectrum contains both (Bogoliubov quasiparticles are fermionic; collective modes are bosonic). The result that spectral action coefficients involve Bessel functions K_nu connects directly to the asymptotic expansion used in Session 37's spectral post-mortem, where the Seeley-DeWitt coefficients a_2 and a_4 control the tau-dependent potential.
