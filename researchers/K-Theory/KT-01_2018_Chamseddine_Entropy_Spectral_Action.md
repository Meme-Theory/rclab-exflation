# Entropy and the Spectral Action

**Author(s):** Ali H. Chamseddine, Alain Connes, Walter D. van Suijlekom

**Year:** 2018

**Journal:** arXiv:1809.02944 [hep-th]

---

## Abstract

We compute the information theoretic von Neumann entropy of the state associated to the fermionic second quantization of a spectral triple. We show that this entropy is given by the spectral action of the spectral triple for a specific universal function. The main result is the surprising relation between this function and the Riemann zeta function, manifested in the coefficients c(d) that multiply the d-dimensional terms in the heat expansion of the spectral triple. c(4) is a rational multiple of ζ(5) and c(2) a rational multiple of ζ(3). The functional equation gives a duality between coefficients in positive dimension (governing high-energy expansion) and coefficients in negative dimension, exchanging even with odd dimension.

---

## Historical Context

The spectral action principle [Chamseddine-Connes 1997] has been the foundational framework for noncommutative geometry, treating the spectral triple (A, H, D) as the fundamental object from which all physics emerges. A key question has always been: what determines the specific test function φ(D²/Λ²) that defines the spectral action Tr(φ(D²/Λ²))?

This paper answers that question from a thermodynamic perspective. Rather than imposing φ by hand, the authors show that a naturally arising entropy functional — the von Neumann information-theoretic entropy of a fermionic second-quantized state — **is** the spectral action for a particular choice of φ.

The result connects three deep areas:
1. **Spectral triples and noncommutative geometry** — the foundational objects of the theory
2. **Fermionic second quantization** — needed to connect to quantum field theory
3. **Riemann zeta function** — an unexpected appearance that suggests deep arithmetic structure in the framework

This is particularly significant for understanding what aspects of the spectral action are topological/K-theoretic (which would survive under perturbation of the test function) versus analytical (which depend sensitively on the choice of φ).

---

## Key Arguments and Derivations

### Section 2: Spectral Triples and Second Quantization

The starting point is a spectral triple (A, H, D) where:
- A is a C*-algebra of observables
- H is a Hilbert space
- D is a self-adjoint Dirac operator with compact resolvent

To perform **fermionic second quantization**, one constructs the complexified Clifford algebra C := Cliff_C(H_R) of the underlying real Hilbert space H_R. This Clifford algebra is equipped with a one-parameter group of automorphisms σ_t ∈ Aut(C) defined by

σ_t(A) = e^{itD} A e^{-itD}

The KMS condition at inverse temperature β is the key thermodynamic tool: a state φ on C satisfies KMS if

φ(a σ_t(b))|_{t=iβ} = φ(ba) for all a,b ∈ C

**Proposition 2.2:** For any β > 0, there exists a unique KMS_β state φ on the C*-dynamical system (C, σ_t).

### Section 2.2: The Fock Space Representation

The representation of the Clifford algebra is realized on **Fock space** ∧V_I, where V_I is the complex Hilbert space obtained by viewing the real vector space H_R with a complex structure I.

The key physical choice is the "sign" complex structure:

I = i(E_+ - E_-) = iF

where E_± are spectral projections onto positive/negative eigenspaces of D, and F = D|D|^{-1} is the sign operator.

This choice implements the **Dirac sea filling**: negative-energy eigenfunctions are reinterpreted as positive-energy antiparticles. The operator D acts as |D|, which has only positive eigenvalues.

**Proposition 2.6:** If exp(-β|D|) is trace class, the KMS state is given by

φ_β(A) = (1/Z) Tr(∧exp(-β|D|) ρ_I(A))

where Z = Tr(∧exp(-β|D|)) and ∧exp denotes the exterior algebra exponentiation (determinant).

### Section 3: Von Neumann Entropy

The von Neumann entropy of a density matrix ρ is

S(φ) = -Tr(ρ log ρ)

For composite systems, the crucial additivity property holds:

S(φ_1 ⊗ φ_2) = S(φ_1) + S(φ_2)

This additivity is inherited by the spectral action: when the second quantization is applied to direct sums of spectral triples, the Clifford algebras tensor (⊗), and therefore the entropy sums.

**Lemma 3.1:** For x > 0, the entropy of a partition of [0,1] with ratio x is

E(x) := log(x+1) - (x log x)/(x+1)

**Theorem 3.4:** The von Neumann entropy of the state φ_β equals the spectral action for the test function

h(x) := E(e^{-x}) = log(2) - x/8 + x²/64 - x³/576 + ...

Thus:

S(φ) = Tr(h(β D))

### Section 4: The Riemann Zeta Function

The remarkable discovery is that h(x) is intimately connected to the Riemann ξ function.

The heat kernel expansion of a differential operator is

Tr(e^{-t D²}) ~ Σ_d a_d t^{d/2}

where the coefficients a_d are Seeley-DeWitt coefficients. For the spectral action Tr(h(D)), one needs

∫_0^∞ h(v^{1/2}) v^{a-1} dv

**Lemma 4.5** computes these moments:

∫_0^∞ h(x) x dx = (9/2) ζ(3)

∫_0^∞ h(x) x³ dx = (225/4) ζ(5)

More generally:

∫_0^∞ h(x) x^β dx = (1 - 2^{-β-1}) Γ(β+2) ζ(β+1) / β

**Lemma 4.6:** The coefficient c(a) of t^a in the heat expansion is

c(a) = (1 - 2^{-2a})/(a π^a) ξ(2a)

where ξ is Riemann's ξ-function:

ξ(s) := (1/2) s(s-1) π^{-s/2} Γ(s/2) ζ(s)

This coefficient is an entire function of a ∈ ℂ.

For negative integers a = -n:

c(-1) = 9ζ(3)/2
c(-2) = 225ζ(5)/4
c(-3) = -21ζ(7)/8

**Key structural observation:** The functional equation of ζ(s) induces a duality between high-energy terms (positive dimension, a < 0) and low-energy terms (odd dimension, half-integer a).

---

## Key Results

1. **Entropy = Spectral Action**: The von Neumann entropy of the fermionic second-quantized KMS state is precisely the spectral action for a universal test function h(x). This provides a thermodynamic/information-theoretic justification for the spectral action principle.

2. **Zeta Function Emergence**: The moments of h(x) are expressible in terms of the Riemann ξ function. Odd zeta values ζ(2n+1) appear as coefficients in the heat expansion. This is unexpected and suggests deep arithmetic structure underlying the spectral triple.

3. **Functional Duality**: The functional equation for ζ relates the coefficients in positive and negative dimensions. High-energy expansion (even dimension) is dual to low-energy expansion (odd dimension, half-integer scaling). This is a structural constraint on how spectral actions organize themselves.

4. **Additivity Structure**: The entropy functional is additive under direct sums of spectral triples because second quantization converts ⊕ → ⊗ and entropy converts ⊗ → +. This is a fundamental structural property preserved by the K-theoretic aspects of the theory.

---

## Impact and Legacy

This 2018 paper provides a direct answer to a long-standing question in noncommutative geometry: **where does the spectral action come from?** Rather than imposing it axiomatically, Chamseddine-Connes-van Suijlekom show it arises naturally from information-theoretic considerations in quantum field theory.

The appearance of the Riemann zeta function is particularly striking. It suggests that the arithmetic structure of zeta — encoded in its functional equation and special values — is fundamental to how the spectral action decomposes under heat-kernel expansion. This opens questions about which aspects of the decomposition are K-theoretic invariants (protected by index theory) and which are analytical artifacts (dependent on the choice of h).

The paper has become essential in understanding the **thermodynamic foundations** of the spectral action principle and has stimulated work on entropy in noncommutative geometry more broadly.

---

## Connection to Phonon-Exflation Framework

**Highly relevant.** The framework uses the spectral action principle applied to the internal geometry D_K on M⁴ × SU(3). The question of which parts of the spectral action are K-theoretic versus analytical is central:

- **K-theoretic aspects**: The partition function Z = Tr(∧exp(-β|D|)), the index of D_K, the K-homology class determined by the spectral triple, and the Chern character all survive perturbations of the test function h. These are what the S71 workshop identified as **scheme-independent**.

- **Analytical aspects**: The heat-kernel coefficients a_d depend on the choice of h via the moments ∫h(x)x^d dx. The Higgs mass, Weinberg angle, and coupling constants are sensitive to changes in h. These are what the workshop identified as **scheme-dependent**.

This paper provides the technical framework for understanding that partition. The entropy computation shows that **additivity** (both spectral action and entropy sum for direct sums) is a preserved feature. This supports the framework's use of spectral moment additivity when computing masses and coupling constants from the second spectral moment (gravity) and fourth spectral moment (Yang-Mills).

The appearance of zeta-function structure may also be relevant to the framework's observation that the spectral density of D_K has arithmetic properties that control the particle spectrum.

**Papers to read together**: 
- Chamseddine-Connes 1997 (original spectral action)
- Van Suijlekom 2015-2024 (spectral action phenomenology)
- Connes reconstruction theorem (0810.2088) to understand what is geometrically determined vs. analytically chosen
