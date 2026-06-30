# Second Quantization and the Spectral Action

**Author(s):** Rui Dong, Masoud Khalkhali, and Walter D. van Suijlekom
**Year:** 2019 (revised 2020)
**Journal:** [Not stated in PDF]
**arXiv:** 1903.09624
**Relevance:** HIGH (Second quantization of spectral triples with chemical potential; entropy and energy as spectral actions via Bessel functions)

---

## Abstract

We consider both the bosonic and fermionic second quantization of spectral triples in the presence of a chemical potential. We show that the von Neumann entropy and the average energy of the Gibbs state defined by the bosonic and fermionic grand partition function can be expressed as spectral actions. It turns out that all spectral action coefficients can be given in terms of the modified Bessel functions. In the fermionic case, we show that the spectral coefficients for the von Neumann entropy, in the limit when the chemical potential mu approaches 0, can be expressed in terms of the Riemann zeta function. This recovers a result of Chamseddine-Connes-van Suijlekom.

---

## Key Arguments and Derivations

### 1. Fock Space and Second Quantization (Section 2)

Starting from a Hilbert space H, the bosonic and fermionic Fock spaces are F_+(H) = P_+(F(H)) and F_-(H) = P_-(F(H)). The second quantization of a self-adjoint operator H is dGamma(H), with the number operator N = dGamma(Id).

The modified Hamiltonian is K_mu = dGamma(H - mu Id) = dGamma(H) - mu N.

The Gibbs state is phi(A) = Tr(e^{-beta K_mu} A) / Tr(e^{-beta K_mu}), with density operator rho = e^{-beta K_mu} / Tr(e^{-beta K_mu}).

The von Neumann entropy: S(rho) = -Tr(rho log rho).
The average energy: <K_mu>_beta = Tr(rho K_mu) = -d/d_beta(log Z).

### 2. Spectral Triples and Second Quantization (Section 2.3)

Starting from a spectral triple (A, H, D), the paper constructs the Fock spaces F_+(H) and F_-(H). If exp(-beta|D|) is trace-class, then the density matrices rho_D define two spectral actions:

D |-> S(rho_D)  (von Neumann entropy)
D |-> <dGamma|D|>_beta  (average energy)

Both are additive under direct sums of spectral triples.

### 3. Fermionic Entropy with Chemical Potential (Section 3.1)

The one-particle Hamiltonian: H_{f,mu} = sqrt(D^2 + mu^2) Id.

The spectral function for the entropy is:

h_mu(x) = sqrt(x^2 + mu^2) / (e^{sqrt(x^2+mu^2)} + 1) + log(1 + e^{-sqrt(x^2+mu^2)})

The entropy S(rho_f) = Tr(h_{beta mu}(beta D)).

**Proposition 3.4:** The spectral action coefficients are entire functions of the order a, given by:

gamma_mu(a) = (1/sqrt(pi)) 2^{(-a+1)/2} |mu|^{(-a+3)/2} sum_{n=1}^{infty} (-1)^{n+1} n^{(a+1)/2} K_{(-a+3)/2}(n|mu|)

where K_nu is the modified Bessel function of the second kind.

**Proposition 3.5 (Poisson summation form):**

gamma_mu(a) = (Gamma(a)/2) sum_{n=-infty}^{infty} ((2a-1)(2n+1)^2 pi^2 - mu^2) / ((2n+1)^2 pi^2 + mu^2)^{a+1}

### 4. Fermionic Entropy: mu -> 0 Limit (Section 3.1)

**Lemma 3.6:** When mu in (-pi, 0), gamma_mu(a) can be expressed via the Riemann zeta function:

gamma_mu(a) = sum_{k=0}^{infty} (-1)^k (1 - 2^{-(2a+2k)}) Gamma(a+k) zeta(2a + 2k) mu^{2k} / (Gamma(a) (2k)! pi^{2a+2k})

As mu -> 0: gamma_0(a) = (1 - 2^{-2a}) Gamma(a) zeta(2a) / pi^{2a}, recovering Chamseddine-Connes-van Suijlekom.

### 5. Fermionic Average Energy (Section 3.2)

For H_{f,mu}, the average energy is also a spectral action with coefficients:

sigma_mu(a) = (1/sqrt(pi)) 2^{(-a+1)/2} |mu|^{(-a+5)/2} sum_{n=1}^{infty} (-1)^{n+1} n^{(a-1)/2} K_{(-a+5)/2}(n|mu|)

### 6. Physical Hamiltonian H'_{f,mu} = |D| - mu Id (Section 3.3-3.4)

The physically natural Hamiltonian gives simpler coefficients:

S(rho'_f) = Tr(h_{0}(beta|D| - beta mu))

with spectral coefficients expressible as gamma_0(a) plus correction terms from the chemical potential.

### 7. Bosonic Second Quantization (Section 4)

For H_{b,mu} = sqrt(D^2 + mu^2) Id with mu < 0 (required for trace-class):

The entropy spectral function:

f_mu(x) = sqrt(x^2 + mu^2) / (e^{sqrt(x^2+mu^2)} - 1) - log(1 - e^{-sqrt(x^2+mu^2)})

**Key difference:** Without chemical potential, the bosonic entropy function is singular at t=0 and the functional is not spectral. The chemical potential mu < 0 is essential for the bosonic case.

Bosonic spectral coefficients:

alpha_mu(a) = (1/sqrt(pi)) 2^{(-a+1)/2} |mu|^{(-a+3)/2} sum_{n=1}^{infty} n^{(a+1)/2} K_{(-a+3)/2}(n|mu|)

(same as fermionic but without the (-1)^{n+1} alternating sign).

---

## Key Results

1. **Von Neumann entropy as spectral action**: Both fermionic and bosonic entropies of Gibbs states from second-quantized spectral triples are spectral actions, with coefficients given by modified Bessel functions K_nu.

2. **Average energy as spectral action**: Similarly, the average energy is a spectral action with Bessel function coefficients of shifted order.

3. **Entire function property** (Proposition 3.4): The spectral coefficients gamma_mu(a) are entire functions of the order a for fixed mu < 0, enabling analytic continuation.

4. **Recovery of CCS result**: In the limit mu -> 0, fermionic entropy coefficients reduce to (1 - 2^{-2a}) Gamma(a) zeta(2a) / pi^{2a}, recovering Chamseddine-Connes-van Suijlekom.

5. **Chemical potential essential for bosons**: The bosonic case requires mu < 0 for the spectral action to be well-defined (trace-class condition).

6. **Poisson summation duality** (Proposition 3.5): Alternative expression for coefficients via Poisson summation, connecting to number-theoretic structure.

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Modified Hamiltonian | $K_\mu = d\Gamma(H - \mu\,\mathbb{1}) = d\Gamma(H) - \mu N$ | Sec. 2.1 |
| von Neumann entropy | $S(\rho) = -\mathrm{Tr}(\rho\log\rho)$ | Sec. 2.2 |
| Fermionic entropy function | $h_\mu(x) = \frac{\sqrt{x^2+\mu^2}}{e^{\sqrt{x^2+\mu^2}}+1} + \log(1 + e^{-\sqrt{x^2+\mu^2}})$ | Sec. 3.1 |
| Spectral coefficients (Bessel) | $\gamma_\mu(a) = \frac{1}{\sqrt{\pi}}2^{(-a+1)/2}|\mu|^{(-a+3)/2}\sum_{n=1}^\infty (-1)^{n+1}n^{(a+1)/2}K_{(-a+3)/2}(n|\mu|)$ | Prop. 3.4, Eq. (11) |
| Poisson form | $\gamma_\mu(a) = \frac{\Gamma(a)}{2}\sum_{n=-\infty}^\infty \frac{(2a-1)(2n+1)^2\pi^2-\mu^2}{((2n+1)^2\pi^2+\mu^2)^{a+1}}$ | Prop. 3.5, Eq. (13) |
| mu -> 0 limit | $\gamma_0(a) = \frac{(1-2^{-2a})\Gamma(a)\zeta(2a)}{\pi^{2a}}$ | Lemma 3.6 |
| Bosonic entropy function | $f_\mu(x) = \frac{\sqrt{x^2+\mu^2}}{e^{\sqrt{x^2+\mu^2}}-1} - \log(1 - e^{-\sqrt{x^2+\mu^2}})$ | Sec. 4.1 |
| Bosonic coefficients | $\alpha_\mu(a) = \frac{1}{\sqrt{\pi}}2^{(-a+1)/2}|\mu|^{(-a+3)/2}\sum_{n=1}^\infty n^{(a+1)/2}K_{(-a+3)/2}(n|\mu|)$ | Sec. 4.1 |
| Bessel integral formula | $\int_1^\infty e^{-zx}(x^2-1)^{(\nu-1)/2}x\,dx = \frac{2^\nu}{\sqrt{\pi}}\Gamma\left(\frac{\nu+1}{2}\right)z^{-\nu}K_{\nu+1}(z)$ | Lemma 3.1, Eq. (2) |
| Spectral action additivity | $S(\rho_{S\oplus T}) = S(\rho_S) + S(\rho_T)$ | Sec. 2.3 |

---

## Relevance to Phonon-Exflation

This paper provides the **mathematical foundation for the BCS/BdG spectral action** used in the framework's instanton gas analysis:

1. **Second quantization of the Dirac operator**: The framework's D_K on M4 x SU(3) is exactly the type of self-adjoint operator with compact resolvent that this paper treats. The second quantization dGamma(D_K) generates the many-body physics (Cooper pairs, pair vibrations) that the framework identifies as the mechanism for dark matter and dark energy.

2. **Chemical potential and BCS**: The paper's treatment of chemical potential mu in the modified Hamiltonian K_mu = dGamma(H - mu Id) is directly relevant to the framework's BCS analysis. Session 34 closed the canonical mu != 0 channel (PH forces mu = 0 analytically), while this paper shows that mu = 0 still gives a well-defined fermionic spectral action recovering the CCS result.

3. **Entropy as spectral action**: The von Neumann entropy S(rho) = Tr(h(beta D)) is a spectral action. This connects the framework's GGE (generalized Gibbs ensemble) permanence result to the spectral action formalism: the post-transit GGE relic has a well-defined entropy that is itself a spectral action determined by the Richardson-Gaudin conserved integrals.

4. **Bessel function coefficients**: The spectral action coefficients gamma_mu(a) in terms of modified Bessel functions K_nu provide the exact heat kernel coefficients needed for the Seeley-DeWitt expansion on the SU(3) fiber. This is the mathematical input for the a_0, a_2, a_4 hierarchy that the framework uses to evaluate the spectral action.

5. **Bosonic vs fermionic statistics**: The sign difference between fermionic (alternating) and bosonic (non-alternating) Bessel sums is directly relevant to the constant-ratio trap (F/B = 0.55) identified in the framework. The exact spectral action coefficients allow a precise comparison of bosonic and fermionic contributions.
