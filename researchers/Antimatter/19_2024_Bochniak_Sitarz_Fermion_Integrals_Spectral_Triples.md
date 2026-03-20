# Fermion Integrals for Finite Spectral Triples

**Authors:** Andrzej Bochniak, Andrzej Sitarz
**Year:** 2024
**Journal:** arXiv (preprint)
**arXiv:** 2403.18428

---

## Abstract

We compute fermion functional integrals (path integrals of the fermionic determinant) for finite real spectral triples—the non-commutative geometric structures underlying the spectral action approach to particle physics. Our method systematically treats each KO-dimension d = 0, 1, ..., 7 (and the periodic extension d + 8), computing the regularized determinant of the Dirac operator D acting on Grassmann variables. We provide explicit formulas for complex, real, and chiral spectral triples, and resolve phase ambiguities in the fermion integral via consistent choices of chirality and reality structure. The results reveal that the fermionic functional integral encodes topological information (Pfaffian, eta-invariant, spectral asymmetry) dependent on the KO-dimension, with direct implications for the spectral action in four-dimensional physics and higher-dimensional non-commutative geometries. Applications include the Standard Model as a finite spectral triple, BCS pairing systems, and axiomatic approaches to thermodynamics of Dirac operators. This work bridges quantum field theory on discrete geometries with topological invariants in condensed matter physics.

---

## Historical Context

The spectral action approach, developed by Chamseddine and Connes (since 2006), proposes that the action of gravity (and gauge theory) arises from the eigenvalue spectrum of a Dirac operator on a finite-dimensional non-commutative space. The simplest version couples a continuous 4D spacetime to a 0-dimensional finite spectral triple (a matrix algebra), producing the Standard Model coupled to gravity. To compute the partition function and correlation functions in this framework, one must compute the path integral of fermions—a functional integral over Grassmann fields. However, unlike QFT in flat spacetime, the geometry here is finite and discrete, and the Dirac operator acts on a finite-dimensional Hilbert space. The fermionic path integral reduces to a classical determinant of a finite matrix, but computing this determinant requires careful treatment of the real structure (conjugation), chirality, and the choice of orientation. Bochniak and Sitarz's 2024 paper fills a gap in the literature by systematically computing these determinants for all KO-dimensions and resolving ambiguities in phase factors. The work is especially relevant to phonon-exflation, which uses KO-dim = 6 and requires precise knowledge of the fermionic functional integral to validate the BCS pairing mechanism and compute thermodynamic quantities (free energy, entropy).

---

## Key Arguments and Derivations

### Finite Spectral Triples and the Dirac Operator

A **finite real spectral triple** is a tuple $(A, H_F, D)$ where:

- **A**: A finite-dimensional unitary algebra (e.g., $A = \mathbb{C} \oplus \mathbb{H} \oplus M_3(\mathbb{C})$ for the Standard Model).
- **H_F**: A finite-dimensional Hilbert space (spinor/fermion space).
- **D**: A self-adjoint Dirac operator, $D: H_F \to H_F$, with anticommute properties and spin structure.

The **real structure** J is an antiunitary operator satisfying:
- $J^2 = \pm 1$ (depending on KO-dimension).
- $J D J^{-1} = \mp D$ (chirality anticommutativity for certain signatures).
- $(aJbJ^{-1})^*=JbJa^*$ for $a,b \in A$ (commutation with algebra).

The **chiral operator** γ (or χ) anticommutes with D: $\{γ, D\} = 0$ (if the space is chiral).

### Fermionic Path Integral on Grassmann Variables

In quantum field theory, the fermionic path integral is:

$$Z_F = \int \mathcal{D}\psi \, \mathcal{D}\bar{\psi} \, e^{-S[\psi, \bar{\psi}]}$$

For a finite Hilbert space, this reduces to an ordinary Grassmann integral (Berezin integral). With a quadratic action:

$$S[\psi, \bar{\psi}] = \int dx \, \bar{\psi}(x) D[\phi(x)] \psi(x)$$

the path integral becomes:

$$Z_F = \det(D)$$

or (for Majorana fermions with real structure):

$$Z_F = \text{Pf}(D)$$

where Pf denotes the Pfaffian (square root of determinant for antisymmetric matrices arising from reality constraints).

### Computation by KO-Dimension

The Bochniak-Sitarz paper organizes the calculation by KO-dimension, exploiting the fact that different KO-dimensions have fundamentally different spin structures and reality conditions.

**KO-dimension 0** (mod 8): Complex Hilbert space, no reality structure.
- Fermion integral: $Z_F = \det(D)$ (regular determinant).
- Invariant: Integer-valued (winding number in momentum space, if applicable).

**KO-dimension 1** (mod 8): Real Hilbert space with complex conjugation.
- Reality structure: $J^2 = +1$.
- Fermion integral: $Z_F = \text{Pf}(D)$ (Pfaffian of D as real antisymmetric matrix).
- Invariant: ±1 (Z_2-valued, sign).

**KO-dimension 2** (mod 8): Quaternionic structure.
- Reality structure: $J^2 = -1$.
- Decomposition: $H_F = H_+ \oplus H_-$ (even/odd chirality).
- Fermion integral: Product of determinants over chiral sectors.

**KO-dimension 6** (mod 8): Real with chiral structure. **Directly relevant to phonon-exflation.**
- Reality structure: $J^2 = +1$.
- Chirality: $\{γ, D\} = 0$, block-diagonal decomposition.
- Dirac operator: $D = \begin{pmatrix} 0 & A \\ A^\dagger & 0 \end{pmatrix}$ (up to basis change).
- Fermion integral: $Z_F = \text{Pf}(D) = \text{sign}(\det A)$ or $\text{sign}(\det A^\dagger A)^{1/2}$.
- Invariant: Z_2-valued.

### Explicit Formula for KO-dim = 6

For a KO-dim = 6 spectral triple with real Dirac operator D (odd-dimensional block structure due to chiral symmetry):

$$Z_F = (-1)^{n_-}$$

where $n_-$ is the number of negative eigenvalues of D, or equivalently:

$$Z_F = \text{Pf}(D)$$

The Pfaffian of a (2N × 2N) real antisymmetric matrix A is:

$$\text{Pf}(A) = (-1)^{N(N-1)/2} \sqrt{\det(A)}$$

(always ±1 if A has only non-zero eigenvalues).

More explicitly, if D has eigenvalues $\{\lambda_i\}$ in pairs $(\lambda_j, -\lambda_j)$, then:

$$\text{Pf}(D) = \text{sign} \prod_j \lambda_j = \text{sign}(\det(D))^{1/2}$$

with the sign encoding the Z_2 topological invariant.

### Spectral Asymmetry and Eta-Invariant

The fermionic functional integral is intimately related to the **spectral asymmetry** (eta-invariant):

$$\eta(D) = \text{sign}(0^+) + \sum_i \text{sign}(\lambda_i)$$

where the sum is over all non-zero eigenvalues of D.

The eta-invariant measures the imbalance between positive and negative eigenvalues. It appears in the **index formula**:

$$\text{Pf}(D) = e^{i\pi \eta(D)/2}$$

(modulo 2π ambiguity in phase).

For a particle-hole symmetric Hamiltonian (BCS context), the eta-invariant vanishes if the spectrum is symmetric: η(D) = 0 ⟹ Pf(D) = ±1.

### Application: Standard Model as a Finite Spectral Triple

The paper applies the formalism to the Standard Model coupled to gravity via the spectral action:

$$A = \mathbb{C} \oplus \mathbb{H} \oplus M_3(\mathbb{C})$$

(algebra for hypercharge, weak isospin, and color symmetries).

The Dirac operator D encodes the Yukawa couplings, mass matrices, and CKM mixing. The fermionic functional integral computes the one-loop fermion determinant contribution to the effective action:

$$S_{eff} = S_{gravity} + S_{gauge} + \log \text{Pf}(D) + \cdots$$

Bochniak-Sitarz show how to organize this calculation by KO-dimension, with the SM living naturally at KO-dim = 6 (or 10 = 6 + 4 mod 8 for extensions).

### Application: BCS Pairing as a Spectral Triple

A BCS superconductor can be represented as a finite spectral triple with:

- **Hilbert space**: Fock space of Cooper pair operators (lattice or continuum).
- **Dirac operator**: Bogoliubov-de Gennes Hamiltonian $H_{BdG} = \begin{pmatrix} h & \Delta \\ \Delta^\dagger & -h^* \end{pmatrix}$ (particle-hole structure).
- **Real structure**: Charge conjugation C, with $J^2 = +1$ in BDI class.

The fermionic functional integral:

$$Z_F = \det(H_{BdG}) = \text{Pf}(H_{BdG})$$

encodes the free energy of the condensate. The paper shows explicitly how to compute Pf(H_BdG) in the BDI framework.

---

## Key Results

1. **Systematic KO-dimension formulas**: Explicit expressions for fermion functional integrals in all KO-dimensions d = 0–7, with periodicity d → d + 8.

2. **Phase ambiguities resolved**: The paper identifies and fixes sign ambiguities (via consistent chirality/reality choices) that plague earlier treatments.

3. **KO-dim = 6 result**: Pfaffian of D is Z_2-valued and related to the signed product of positive eigenvalues (or negative/positive ratio).

4. **Spectral asymmetry connection**: The eta-invariant η(D) encodes the fermion loop contribution and is gauge-invariant.

5. **Standard Model one-loop**: The SM fermion determinant at KO-dim = 6 can now be computed in closed form, with implications for running couplings and electroweak symmetry breaking.

6. **BCS thermodynamics**: For a superconductor in the BDI class (KO-dim = 6), the Pfaffian directly gives the Helmholtz free energy.

---

## Impact and Legacy

- **Bridge between NCG and solid-state physics**: Connects spectral action (Connes) with Bogoliubov theory (condensed matter), enabling cross-fertilization.
- **Rigorization of spectral action**: Provides solid mathematical foundation for fermion loops in finite spectral triple framework.
- **BCS in NCG language**: Opens path to studying superconductivity and superfluidity using spectral triples, with implications for topological phases.
- **Quantum thermodynamics**: The Pfaffian formulation enables exact computation of free energies in finite systems, relevant to quantum information and thermodynamics.

---

## Connection to Phonon-Exflation Framework

**Critical and direct.** This paper provides the mathematical machinery for Session 41 (Theorem 1):

1. **KO-dim = 6 spectral triple**: Phonon-exflation uses KO-dim = 6 (Session 7 theorem). The framework defines the geometry as a finite real spectral triple with D_K (Klein-type Dirac operator).
   - Bochniak-Sitarz provide the explicit formula for computing Z_F = Pf(D_K) at KO-dim = 6.

2. **Pfaffian invariant**: The paper shows that Pf(D) is Z_2-valued in KO-dim = 6, matching the framework's assumption that the topological invariant is a single bit.
   - Sessions 17c and 34 computed Pf(D_K) = -1 (non-trivial topological phase).
   - This paper's formalism validates that such a computation is mathematically well-defined.

3. **Fermionic action and BCS**: The paper's treatment of BCS (Bogoliubov-de Gennes Hamiltonian) as a spectral triple directly applies to the framework's mechanism.
   - The BCS pairing instability (Session 35, RG-BCS-35 theorem) is formulated via the Dirac operator D_K in BDI class.
   - Bochniak-Sitarz show how to compute the Pfaffian for such systems, enabling calculation of the condensate free energy.

4. **Session 38 instanton gas**: The instanton gas (dense configuration of BCS pair creation events) can be modeled as a time-dependent perturbation of the spectral triple.
   - The fermionic functional integral changes discontinuously at the transit (from Pf = -1 to a new state), reflecting the topological phase transition.
   - Bochniak-Sitarz's machinery computes the phase factor e^{iπη(D)/2} before and after, tracking the topological jump.

5. **Eta-invariant and entanglement entropy**: The eta-invariant η(D) is related to the entanglement entropy of the fermionic ground state (von Neumann entropy).
   - Paper 20 (Chamseddine-Connes) shows S_vN = η(D) for certain spectral triples.
   - This connects Session 38's observation of GGE permanence to the framework's spectral geometry.

6. **Theorem 1 formulation**: Session 41 states a theorem about the fermionic spectral action computed via Bochniak-Sitarz formalism.
   - The theorem depends critically on having the correct expression for Pf(D) at KO-dim = 6, which this paper provides.

**Summary**: Bochniak-Sitarz 2024 is the foundational paper validating the mathematical machinery used to compute Pfaffians and fermionic functional integrals in the framework. Without it, Session 41's theoretical claims would lack rigorous justification.

