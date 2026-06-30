# Mock Theta Functions (Mathematical Foundations)

**Author:** Stefan Zwegers

**Year:** 2002

**Degree:** Ph.D. Dissertation, University of Utrecht

**Published versions:** Zwegers, S. (2002). Mock Theta Functions. Ph.D. Thesis, Utrecht; Zwegers, S. (2008). Mock Theta Functions. arXiv:0807.4834

---

## Abstract

This foundational work resolves a century-long mystery in mathematics. Ramanujan wrote down a list of theta functions in his famous "lost notebook" that did NOT satisfy the modular transformation properties of classical theta functions, yet possessed surprising internal structure and appeared in deep number-theoretic identities. Mathematicians puzzled over them for nearly a century.

Zwegers' breakthrough discovery shows that Ramanujan's mock theta functions are actually **modular forms that fail by a specific, calculable amount** (the holomorphic anomaly). This failure can be corrected by adding a non-holomorphic term (an integral of theta functions against a weight 3/2 form), producing a genuine modular form.

The paper introduces the concept of **mock modular forms**: holomorphic functions that are "almost" modular, with the anomaly encoded in a "shadow" modular form. This unifies Ramanujan's mysterious functions into a consistent mathematical framework and opens connections to physics (black hole entropy, wall-crossing), representation theory (affine Kac-Moody algebras), and combinatorics.

---

## Historical Context

### Ramanujan's Lost Notebook (1920s)

Srinivasa Ramanujan (1887-1920) was a self-taught Indian mathematician who died at 32, leaving behind a wealth of unpublished results. One of his notebooks contained a list of q-series:

$$\mu_1(q) = \sum_{n=0}^{\infty} \frac{q^{n(n+1)/2}}{(q;q)_n}$$

and similar functions, where $(q;q)_n = (1-q)(1-q^2) \cdots (1-q^n)$ is the q-Pochhammer symbol.

Ramanujan claimed these functions satisfied certain identities and had interesting arithmetic properties. He called them "mock theta functions," though he did not formally define what "mock" meant—suggesting they are "theta-like" but not quite theta functions.

### The Mystery (1920-2001)

For 80 years, mathematicians studied these functions without fully understanding their nature:

- **Rogers** and **Watson** found formulas relating them to Appell-Lerch sums and classical theta functions.
- **Selberg** and others conjectured they were related to automorphic forms but with indefinite signatures.
- **Dyson** (1970s) proposed a "rank" of partitions to explain Ramanujan's congruences, but the connection remained obscure.

The functions were clearly important—they appeared in representation theory, combinatorics, and partition asymptotics—yet mathematically, they were "orphaned": not modular, not classical theta functions, not obviously related to known structures.

### Zwegers' Breakthrough (2002)

Zwegers showed that each mock theta function f(q) can be written as:

$$f(q) = M(q) + N(q)$$

where:

- **M(q)**: A **weak Maass form** of weight 1/2—a real-analytic function that satisfies a modified modularity condition
- **N(q)**: A sum of indefinite theta functions (related to negative-definite quadratic forms)

The modularity failure of M is exactly compensated by N, which has opposite non-holomorphic behavior. The sum is modular when proper non-holomorphic corrections are included.

---

## Key Arguments and Derivations

### 1. Modular Forms and Theta Functions (Review)

A modular form of weight k is a holomorphic function f on the upper half-plane such that:

$$f\left( \frac{a\tau + b}{c\tau + d} \right) = (c\tau + d)^k f(\tau)$$

for all $(a, b, c, d) \in SL(2, \mathbb{Z})$.

Classical theta functions (Jacobi, Dedekind) are modular forms. For example, the Dedekind eta function:

$$\eta(\tau) = q^{1/24} \prod_{n=1}^{\infty} (1 - q^n), \quad q = e^{2\pi i \tau}$$

is a modular form of weight 1/2 (with a multiplicative character).

### 2. Ramanujan's Mock Theta Function and Its Non-Modularity

Consider one of Ramanujan's examples:

$$\mu_1(\tau) = \sum_{n=0}^{\infty} \frac{q^{n(n+1)/2}}{(q;q)_n}$$

where $(q;q)_n = \prod_{k=1}^n (1 - q^k)$.

Computing the transformation under τ → -1/τ (the "S" generator of SL(2,Z)), one finds:

$$\mu_1(-1/\tau) \neq (−i\tau)^{1/2} \mu_1(\tau)$$

That is, μ_1 does NOT transform as a modular form of weight 1/2. The transformation law fails by a term involving Appell-Lerch sums:

$$\mu_1(-1/\tau) = (−i\tau)^{1/2} (\mu_1(\tau) + \text{Appell-Lerch}(\tau))$$

or equivalently:

$$\mu_1(-1/\tau) - (−i\tau)^{1/2} \mu_1(\tau) = \text{(holomorphic anomaly)}$$

This is the "mock" property: μ_1 **looks modular locally** but **fails the global transformation**. The failure (the anomaly) is small and concentrated at cusps.

### 3. The Weak Maass Form and Non-Holomorphic Completion

To resolve the non-modularity, Zwegers introduces:

$$\mu_1^*(τ) = \mu_1(\tau) + \int_{\infty}^{i\infty} \frac{\theta_3(\tau, z)}{\sqrt{(τ-\bar{\tau})} (4\pi)}  \, dz$$

where θ_3 is a classical Jacobi theta function and the integral is the "non-holomorphic completion."

The key fact: μ_1^* is a genuine **weak Maass form** of weight 1/2, satisfying:

$$(Δ_{1/2} - \frac{3}{16}) \mu_1^* = 0$$

where Δ_{1/2} is the hyperbolic Laplacian (the Casimir operator for SL(2,R)).

This equation is the analog of the modularity condition: instead of invariance under discrete SL(2,Z), the function is an eigenfunction of the continuous Laplacian.

### 4. Mock Modular Forms and Shadows

More generally, a **mock modular form** of weight k is a holomorphic function f that admits a Fourier expansion

$$f(\tau) = \sum_{n \geq N} c(n) q^n$$

and satisfies:

$$f\left( \frac{a\tau + b}{c\tau + d} \right) = (c\tau + d)^k f(\tau) + (c\tau + d)^{k} g(\tau)$$

where g is a **holomorphic anomaly** determined by another modular form h of weight 2-k, called the **shadow**:

$$g(\tau) = \int_{\infty}^{i\infty} \frac{h(\tau) \theta_3(\tau, z)}{\sqrt{\tau - \bar{\tau}}} \, dz$$

The shadow encodes the non-modularity: a form with shadow 0 is fully modular.

### 5. Zwegers' Decomposition Theorem

For Ramanujan's mock theta functions of orders 3, 5, and 7, Zwegers proves:

**Each mock theta function can be written as a sum of a weak Maass form (modular up to non-holomorphic terms) and indefinite theta functions (which are meromorphic but not holomorphic).**

This decomposition is **canonical**: the weak Maass form and the theta function are uniquely determined.

Mathematically:

$$f(\tau) = M(\tau) + \sum_n a_n \, \Theta_n(\tau)$$

where M is a weak Maass form and each Θ_n is an indefinite theta function. The sum is "balanced": the non-holomorphic part of M exactly cancels the non-modularity from the indefinite theta functions.

### 6. Physics Interpretation: Meromorphic Jacobi Forms

In black hole partition functions, one naturally encounters **meromorphic** Jacobi forms—not quite holomorphic, with poles at special loci (these correspond to multi-centered black holes).

Zwegers' theory shows that a meromorphic Jacobi form can be decomposed as:

$$\Psi(\tau, z) = \hat{\Psi}^{mock}(\tau, z) + \text{Appell-Lerch}(\tau, z) + (\text{residues at poles})$$

where:
- The mock Jacobi part has a holomorphic anomaly (reflecting the non-compactness of the CFT)
- The Appell-Lerch part encodes the wall-crossing from multi-centered decay
- The residues encode the meromorphic singularities

This connection directly motivated Dabholkar-Murthy-Zagier (2012) to study black hole partition functions through the lens of mock modularity.

---

## Key Results

1. **Ramanujan's Mystery Resolved**: The "lost notebook" mock theta functions are now understood as members of a coherent mathematical class: mock modular forms with specific shadows.

2. **Universal Structure**: All Ramanujan's examples fit into the framework of weak Maass forms and indefinite theta functions. This provides a unified perspective on previously disparate identities.

3. **Modular Completion**: Each mock modular form f(τ) admits a unique completion f*(τ) = f(τ) + (non-holomorphic integral) that is genuinely modular. The non-holomorphic part encodes information about the shadow.

4. **Congruence and Arithmetic**: Zwegers' framework explains why mock theta functions satisfy Ramanujan's congruences and have intricate number-theoretic properties. The shadow—a classical modular form—carries the arithmetic information.

5. **Universal Mock Theta Functions**: Zwegers and Zagier later developed "universal" mock theta functions (generalizations of the classical examples) that capture the essence of mock modularity in its greatest generality.

6. **Applications to Partition Functions**: The framework applies to finite partition functions, generating function asymptotics, and quantum state counts in systems with walls-crossing.

---

## Impact and Legacy

Zwegers' work (2002) opened a new field:

- **Modern mathematics** (post-2002): Mock modular forms are now a standard tool in number theory, representation theory, and combinatorics. They appear in the study of:
  - Affine Kac-Moody algebras (moonshine phenomena)
  - Donaldson-Thomas invariants (wall-crossing formulas)
  - Cryptographic curves (arithmetic geometry)

- **Physics** (2010+): Recognition that black hole partition functions are mock modular (Dabholkar-Murthy-Zagier 2012) sparked new collaborations between string theory, quantum gravity, and mathematics.

- **Computational**: Algorithms for computing coefficients of mock modular forms (previously intractable for some Ramanujan functions) are now available, enabling explicit verification of congruences and identities.

- **Prizes**: Zwegers' work was awarded the *Salem Prize* (2008) for contributions to analysis, and his ideas have influenced subsequent Fields medallists and major funding.

---

## Connection to Phonon-Exflation Framework

**Speculative but Promising**: If the framework's BCS partition function Z(q) = Σ_N d_N(T) q^N is a finite q-series (finite N due to bounded system size), then:

1. **Finite truncation**: Unlike classical modular forms (infinite Fourier series), Z(q) is a polynomial in q. A finite partition sum cannot be a true modular form, but can be a **mock modular form** or a **quasi-modular deformation**.

2. **Shadows and wall-crossing**: The framework claims a BCS pairing transition (normal ↔ condensed). This is a "wall-crossing" in the q-space (phase transition boundary). Zwegers' theory suggests the shadow (the modular anomaly) encodes this transition.

3. **Integrable structure**: With 8 conserved charges (as claimed), the system is integrable. Integrable systems often exhibit quasi-modular structure in their partition functions. The 8 charges would generate 8 "shadow" forms.

4. **GGE permanence**: The "generalized Gibbs ensemble" (GGE) that never thermalizes could be reflected in the mock modular structure: the "mock" part (non-modular, reflecting non-equilibrium) is permanent, while the true modular part (equilibrium) decays.

5. **Number-theoretic properties**: If Z(q) has Ramanujan-like congruence properties, this would be evidence of underlying mock modularity, suggesting a deep arithmetic structure to the BCS staircase.

**Status**: No explicit mock modular structure has been demonstrated for BCS partition functions. But Zwegers' machinery provides tools to investigate: compute Z(q) for finite N, check for anomalies under modular transformations (generalized or deformed), and search for shadow forms encoded in the system's integrals of motion.

---

## References

- Zwegers, S. (2002). Mock Theta Functions. Ph.D. Thesis, University of Utrecht.
- Zwegers, S. (2008). Mock Theta Functions. arXiv:0807.4834
- Zagier, D. (2009). Ramanujan's Mock Theta Functions and Their Applications. Astérisque 326, 143-181.
- Ramanujan, S. (1988). The Lost Notebook and Other Unpublished Papers. Springer.
- Dabholkar, A., Murthy, S., Zagier, D. (2012). Quantum Black Holes, Wall Crossing, and Mock Modular Forms. arXiv:1208.4074
