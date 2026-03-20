# Coset Space Dimensional Reduction of Gauge Theories

**Author(s):** Peter Forgacs, Nicholas S. Manton

**Year:** 1980

**Journal:** Communications in Mathematical Physics, Volume 72, pp. 15-35

---

## Abstract

This foundational paper develops the **Coset Space Dimensional Reduction** (CSDR) formalism, a systematic method for constructing lower-dimensional gauge theories from higher-dimensional theories by restricting fields to be invariant under a subgroup of the internal symmetry group. The key innovation is proving that if a higher-D gauge theory is restricted such that field configurations are symmetric with respect to a coset $G/H$ (where $G$ is the gauge group and $H$ is a subgroup), then the resulting 4D theory automatically possesses a Higgs mechanism: scalar fields emerge naturally from the higher-D vector potentials and acquire vacuum expectation values consistent with the symmetry breaking $G \to H$. The formalism is entirely general and applies to any gauge group; Forgacs-Manton demonstrate applications to E_6, SO(10), and SU(5) grand unified theories.

---

## Historical Context

Kaluza-Klein theory compactified extra dimensions to recover electromagnetism. But early KK models on simple topologies (like $S^1$) yielded only abelian gauge groups. How could the Standard Model's non-abelian SU(3) × SU(2) × U(1) arise?

By the late 1970s, several approaches existed:

1. **Compactify on more complex spaces:** e.g., $M^4 \times K_d$ with $K_d$ having the right isometry group.
   - Problem: Hard to find $K_d$ with exactly the right symmetries; many degrees of freedom are wasted on unwanted gauge groups.

2. **Impose truncation ansätze:** Assume that fields depend on fewer coordinates than the full theory allows.
   - Problem: Arbitrary. Why these truncations? Are they consistent with the field equations?

3. **Use coset structure:** Forgacs and Manton's key idea: **If internal fields are valued in a coset $G/H$, the lower-dimensional theory is gauge theory of $H$ with spontaneously broken $G$ symmetry.**

Forgacs-Manton transformed dimensional reduction from an ad hoc procedure into a systematic, representation-theoretic framework. Their formalism enabled the construction of realistic GUT-like theories from pure higher-dimensional Yang-Mills, showing that the Higgs mechanism is a **geometric consequence of coset compactification**, not an additional ingredient.

---

## Key Arguments and Derivations

### 1. Coset Spaces and Symmetric Fields

A coset $G/H$ is the quotient of a Lie group $G$ by a subgroup $H$. For example:

- $SU(5)/SU(3) \times SU(2) \times U(1) \cong$ space of broken directions in SU(5)
- $SO(10)/SU(5) \times U(1)$, etc.

The tangent space at the identity coset is:

$$T_e(G/H) \cong \mathfrak{g}/\mathfrak{h}$$

where $\mathfrak{g}$ and $\mathfrak{h}$ are the Lie algebras.

A **symmetric field** on the coset is a field configuration that respects the $H$-symmetry. Formally:

$$\phi: M^4 \times (G/H) \to \mathcal{R}$$

where $\mathcal{R}$ is the representation space of $G$.

The **invariant ansatz** demands that $\phi$ is constant on $H$-orbits in $G/H$. This reduces the number of degrees of freedom from $\dim(G/H)$ to the number of $H$-invariant directions, which is typically much smaller.

### 2. Yang-Mills Theory in Higher Dimensions

Start with a pure gauge theory in $d$ dimensions:

$$\mathcal{L}_d = -\frac{1}{4g_d^2} F^a_{\mu\nu} F^{a,\mu\nu}$$

where $a$ indexes the generators of the gauge group $G$, and $\mu,\nu = 0,\ldots, d-1$.

Decompose coordinates as $x^M = (x^\mu, y^I)$ where $\mu = 0,1,2,3$ (4D) and $I = 5, \ldots, d$ (internal).

The field strength is:

$$F^a_{\mu\nu} = \partial_\mu A^a_\nu - \partial_\nu A^a_\mu + f^{abc} A^b_\mu A^c_\nu$$

$$F^a_{\mu I} = \partial_\mu A^a_I - \partial_I A^a_\mu + f^{abc} A^b_\mu A^c_I$$

$$F^a_{IJ} = \partial_I A^a_J - \partial_J A^a_I + f^{abc} A^b_I A^c_J$$

### 3. Coset Ansatz

Impose the **coset ansatz** on the gauge fields:

$$A_\mu^a(x,y) = A^{H}_\mu(x) \delta^a_H + A^{\Phi}_\mu(x) \phi^a(x) + \ldots$$

Specifically:

1. **$H$-components ($a \in H$):** Gauge fields $A^a_\mu(x)$ depend on $x$ only (4D). These become the 4D gauge bosons of the unbroken group $H$.

2. **$G/H$ components ($a \in G \setminus H$):** Gauge fields $A^a_\mu(x)$ vanish on the background (they are set to zero at the classical level). The fields $A^a_I(y)$ from the internal directions acquire vacuum expectation values related to the coset geometry. These become scalars in 4D.

3. **Internal directions:** Set $A_I^a = 0$ for $a \in H$ (internal gauge fixing). The components $A_I^a$ for $a \in G/H$ satisfy a consistency condition.

**The key condition:** The internal field strengths $F^a_{IJ}$ and $F^a_{\mu I}$ vanish on-shell:

$$F^a_{IJ} = 0, \quad F^a_{\mu I} = 0 \quad (a \in G/H)$$

This is achieved if $A_I^a = 0$ for all $a$, and the internal geometry self-consistently enforces this constraint.

### 4. Emergence of Scalars from Higher-D Geometry

The crucial step: dimensional reduction of the higher-D Lagrangian using the coset ansatz yields **scalar fields** in 4D.

From the component $F^a_{\mu I}$:

$$F^a_{\mu I} = \partial_\mu A^a_I - \partial_I A^a_\mu$$

In the coset ansatz, the internal $A^a_I$ parameterize the "direction" in the coset. As $x$ varies, the point in the coset $G/H$ can shift. A scalar field $\phi^a(x)$ (for each generator $a \in G/H$) encodes this shift:

$$A^a_I \leftrightarrow \phi^a(x) \partial_I \xi(y)$$

where $\xi(y)$ is a coordinate on the coset. Upon integration over the internal space, the action becomes:

$$S_4 = \int d^4x \, V(y) \left[ -\frac{1}{4} F^H_{\mu\nu} F^{H,\mu\nu} + D_\mu \phi^a D^\mu \phi_a - V(\phi) \right]$$

where $V(y) = \int dy^d$ is the volume of the internal space, $F^H$ are the 4D field strengths for $H$-generators, $D_\mu \phi = \partial_\mu \phi + [A^H_\mu, \phi]$, and $V(\phi)$ is the **Higgs potential**.

**The Higgs potential** arises entirely from the internal field strength $F^a_{IJ}$:

$$V(\phi) \propto F^a_{IJ} F^{a,IJ} |_{\text{reduced}}$$

In the coset ansatz, this becomes:

$$V(\phi) = \lambda \left( |\phi|^2 - v^2 \right)^2$$

or more generally, a potential whose minimum is at $\langle \phi \rangle = v \neq 0$, breaking $G \to H$ spontaneously.

### 5. Representation-Theoretic Decomposition

Under the unbroken gauge group $H$, the scalars $\phi^a$ transform as:

$$\phi^a \to U(h) \phi^a$$

where $U(h)$ is a representation of $H$. The representation is determined by how the coset coordinates transform:

$$G/H \to U(g)^{-1} U(h) G/H$$

For $G = SU(5)$ and $H = SU(3) \times SU(2) \times U(1)$:

- The coset $SU(5)/SU(3) \times SU(2) \times U(1)$ has dimension 24 (= 24 generators in $SU(5)$ minus 16 in $H$).
- These 24 coset directions decompose into $H$-representations:
  - **Higgs doublets:** $(\mathbf{1}, \mathbf{2})$ under $SU(3) \times SU(2)$
  - **Lepto-quark singlets:** $(\mathbf{3}, \mathbf{1})$ under $SU(3) \times SU(2)$
  - ... (other multiplets)

Each multiplet appears with a multiplicity determined by the Casimir operators and the detailed coset structure.

### 6. Consistency of the Truncation

Forgacs-Manton prove that the coset ansatz is **consistent** in the following sense:

**Theorem:** If the higher-D gauge field configuration satisfies the coset ansatz and obeys the 4D equations of motion, then it automatically satisfies the higher-D equations of motion.

**Proof sketch:** The higher-D Euler-Lagrange equations split into:
- 4D equations (from varying $A^H_\mu$ and $\phi^a$)
- Internal equations (from varying $A_I$)

The internal equations reduce to a **consistency condition** on the coset structure, which is automatically satisfied by the coset geometry.

### 7. Generalization to Multiple Cosets and Product Spaces

If internal space is $M^4 \times G_1/H_1 \times G_2/H_2 \times \ldots$, then:

- 4D gauge group: $H_1 \times H_2 \times \ldots$
- 4D matter: Scalars from each coset sector, transforming as indicated multiplets.
- 4D Higgs potential: Minima determined by the product structure.

This gives great flexibility in model building. One starts with a large gauge group $G$ in higher dimensions, compactifies on a series of cosets, and arrives at a low-energy spectrum with multiple Higgs sectors, flavor structure, etc.

---

## Key Results

1. **Coset ansatz is consistent:** Dimensional reduction on coset spaces automatically yields a lower-dimensional gauge theory that is a consistent truncation.

2. **Scalars emerge geometrically:** Higgs fields are not added by hand but emerge from the internal geometry of the coset.

3. **Higgs potential determined:** The potential is entirely determined by the coset structure and internal gauge kinetics; no free parameters.

4. **Representation theory encodes matter:** The spectrum of 4D fermions and scalars is determined by how the higher-D representations decompose under $H$.

5. **Systematic model building:** For any choice of $G$ and $H$, the 4D spectrum is uniquely determined. This enables systematic search for realistic GUT-like theories.

---

## Impact and Legacy

**Immediate impact:**

- CSDR became the standard method for dimensional reduction in higher-dimensional gauge theories.
- Enabled construction of realistic 4-generation or higher-generation GUTs from pure higher-D Yang-Mills.

**Subsequent applications:**

- Freund-Rubin compactification: Applied coset structure to gravitational theories.
- String theory: Calabi-Yau and other coset-like internal geometries used in heterotic and Type II compactifications.
- Supergravity: Cremmer-Julia-Scherk combined CSDR with supersymmetry to build 11D-to-4D SUGRA reductions.

**Modern relevance:**

- Every string compactification uses coset-space ideas (even if not CSDR explicitly).
- AdS/CFT: Anti-de Sitter spaces are cosets ($AdS_n = SO(n-1,2)/SO(n-1,1)$); compactifications on cosets within AdS spaces are studied extensively.
- Supersymmetric model building: CSDR + supercoset spaces = comprehensive framework for SUSY GUTs.

---

## Connection to Phonon-Exflation Framework

The phonon-exflation framework uses coset-space concepts analogously:

1. **Internal coset structure:** The SU(3) fiber in M4 × SU(3) is itself a coset-like structure. The distinction between "left-invariant" generators (like K_7 in the framework) and "right-coset" directions mirrors Forgacs-Manton's decomposition.

2. **Scalar emergence:** In the framework, the "phonon excitations" (Dirac spectrum modes) on SU(3) play the role of scalars. Just as CSDR shows scalars emerge from internal geometry, the framework shows particle masses emerge from spectral eigenvalues.

3. **Higgs potential analog:** The spectral action $S_{spec}[D_K(\tau)]$ is a functional of the fold parameter $\tau$ (analogous to the Higgs vev). The potential landscape is determined by the geometry, not imposed by hand.

4. **Representation theory:** The K_7 charge (a discrete symmetry in the framework) decomposes the Dirac spectrum into irreps, analogous to how $SU(2)$ doublets and singlets emerge from $SU(5)/SU(3) \times SU(2)$.

5. **Consistent truncation:** The framework's claim that only low-energy phonons contribute (truncation to a finite number of states) parallels CSDR: internal consistency ensures the truncation is valid.

**Baptista connection:** In Session 33a, Baptista's KK reduction explicitly uses CSDR principles (though not always labeled as such). The dimensional reduction from M4 × SU(3) to M4 × S^7 (in the limit where SU(3) shrinks to its maximal torus) involves a coset structure.

**Relevance Rating:** VERY HIGH. CSDR is the foundational framework for understanding how internal symmetries emerge from higher-D geometry. Phonon-exflation's use of M4 × SU(3) is a direct application of coset-space dimensional reduction ideas.

---

## References

- Forgacs, P., Manton, N. S. (1980). "Coset Space Dimensional Reduction of Gauge Theories." Commun. Math. Phys. 72, 15-35.
- Cremmer, E., Julia, B., Scherk, J. (1978). "Supergravity in Theory in 11 Dimensions." Phys. Lett. B 76, 409-412.
- Freund, P. G. O., Rubin, M. A. (1980). "Dynamics of Dimensional Reduction." Phys. Lett. B 97, 233-235.
- Weinberg, S., Witten, E. (1980). "Limits on Massless Particles." Phys. Lett. B 96, 59-62.
- van Suijlekom, W. D. (2019). "Noncommutative Geometry and Particle Physics." Springer.
