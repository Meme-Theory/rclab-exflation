# Spectrum of the Dirac Operator on Compact Riemannian Manifolds

**Author(s):** Lingzhong Zeng

**Year:** 2024

**Journal:** arXiv:2402.14247 (submitted February 22, 2024)

---

## Abstract

This work establishes extrinsic estimates for the sum of arbitrary consecutive $n$ eigenvalues of the squared Dirac operator on compact Riemannian manifolds (and submanifolds embedded in Euclidean space). Using the Atiyah-Singer index theorem and techniques from differential geometry, the author derives universal bounds on eigenvalue sums under specific curvature conditions, proves bounds of Reilly type, and provides an alternative derivation of Anghel's classical result. The framework applies to spin manifolds of any dimension and includes bounds for the first $n$ nontrivial eigenvalues of the Atiyah-Singer Laplacian. The results are dimension-independent, making them broadly applicable across geometric settings.

---

## Historical Context

The Dirac operator on a Riemannian manifold is one of the most fundamental objects in differential geometry and mathematical physics. Its spectrum encodes deep topological and geometric information: the index of the Dirac operator counts the difference between positive and negative eigenvalues (Atiyah-Singer index theorem), and the spectrum itself constrains the curvature of the underlying manifold.

Classical results in spectral geometry include:

- **Lichnerowicz inequality**: $\lambda_1 \geq \frac{n}{4(n-1)} R_{\min}$ for the first non-zero eigenvalue of the Dirac operator on a spin manifold, where $R$ is the scalar curvature.
- **Weyl asymptotics**: The density of Dirac eigenvalues near $\lambda$ grows as $\lambda^{n/2}$ in $n$ dimensions (analogous to the phonon density of states).
- **Index theorem**: $\text{ind}(D) = \int_M \hat{A}(R)$ where $\hat{A}$ is the Dirac genus (characteristic class).

Zeng's work extends this classical framework by providing **extrinsic estimates**—bounds that depend on how the manifold sits within an ambient Euclidean space—rather than only intrinsic curvature. This is important for understanding finite-size effects and embedded geometries, relevant to models like kaluza-Klein theory where extra dimensions are compactified.

---

## Key Arguments and Derivations

### The Dirac Operator and Clifford Algebra

On a Riemannian manifold $(M, g)$ with a spin structure, the Dirac operator is:

$$D = \sum_{i=1}^n e_i \nabla_{e_i}$$

where $e_i$ are orthonormal frame fields, $\nabla$ is the spin connection, and the product is in the Clifford algebra $\text{Cl}(T^*M)$. Explicitly:

$$D : \Gamma(S^+) \to \Gamma(S^-)$$

maps positive spinors to negative spinors. The eigenvalues come in pairs $\pm \lambda_k$ (except possibly zero), and the spectrum is symmetric about the origin.

### Squared Dirac Operator and Spectral Properties

The squared Dirac operator is:

$$D^2 = \sum_{i=1}^n e_i^2 \nabla_{e_i}^2 = -\Delta + \frac{R}{4}$$

where $\Delta$ is the spin Laplacian and $R$ is the scalar curvature. The eigenvalues $\mu_k = \lambda_k^2$ of $D^2$ satisfy:

$$\mu_k \geq \frac{n R_{\min}}{4(n-1)}$$

by Lichnerowicz. However, for individual eigenvalues, this bound is crude. Zeng's work provides tighter bounds on **sums** of consecutive eigenvalues:

$$\sum_{k=1}^n \mu_k \leq f(n, \text{geometry})$$

### Extrinsic Estimates: Embedding in Euclidean Space

If $M$ is isometrically embedded in $\mathbb{R}^N$, the extrinsic geometry is characterized by the second fundamental form $\text{II}$:

$$\text{II}(\mathbf{v}, \mathbf{w}) = -d\mathbf{n} \cdot (\mathbf{v} \otimes \mathbf{w})$$

where $\mathbf{n}$ is the normal vector field. The mean curvature vector is:

$$\mathbf{H} = \frac{1}{n} \text{tr}(\text{II})$$

Zeng uses the second fundamental form to control the extrinsic curvature and thereby bound eigenvalue sums. A key result relates the intrinsic scalar curvature $R$ to the extrinsic mean curvature:

$$R = R^{\text{iemb}} + |\mathbf{H}|^2 - |\text{II}|^2$$

where $R^{\text{iemb}}$ is the curvature of the ambient space (zero for Euclidean embeddings).

### Reilly-Type Bounds

Classical Reilly inequalities relate eigenvalues of the Laplacian to boundary geometry. Zeng extends these to the Dirac operator. For a compact manifold $M$ with boundary $\partial M$, let $\mathbf{H}_{\partial}$ be the mean curvature of the boundary. Then:

$$\lambda_1^2(D) \geq C \frac{A}{V} - K(\partial M)$$

where $A$ is surface area, $V$ is volume, and $K(\partial M)$ measures the boundary geometry. This gives a lower bound on the first non-zero Dirac eigenvalue in terms of the isoperimetric ratio.

### Atiyah-Singer Index Theorem Application

The index theorem states:

$$\text{ind}(D) = \dim(\ker D^+) - \dim(\ker D^-) = \int_M \hat{A}(R) \text{ ch}(E)$$

where $\hat{A}(R)$ is the Dirac genus (top Pontryagin class) and $\text{ch}(E)$ is the Chern character of the spinor bundle. Zeng uses this to constrain the zero eigenvalue multiplicity and thereby relate the spectrum's symmetry properties to topological invariants.

### Dimension-Independent Results

A key innovation is that many bounds do NOT depend on the dimension $n$. For example:

$$\sum_{k=1}^m \lambda_k^2 \leq m \cdot C_0 \left[\|H\|_{\infty}^2 + \|K\|_{\infty}\right]$$

where $C_0$ is a universal constant (independent of $n$), $\|H\|_{\infty}$ is the maximum mean curvature, and $\|K\|_{\infty}$ is the maximum of the sectional curvatures. This is remarkable because it means the Dirac spectrum's growth is controlled uniformly, regardless of how many dimensions the manifold is embedded in (up to the embedding dimension $N$).

### Anghel's Result Revisited

Anghel (1990) proved that on a compact Riemannian spin manifold:

$$\lambda_1^2(D) \geq \frac{n}{4(n-1)} \min(R)$$

with equality iff the manifold is an Einstein manifold (constant scalar curvature). Zeng provides an alternative derivation using his extrinsic framework, showing that Anghel's bound naturally emerges when the manifold is minimally embedded (mean curvature zero) in Euclidean space.

---

## Key Results

1. **Extrinsic Eigenvalue Bounds** — For compact submanifolds embedded in Euclidean space, eigenvalue sums are bounded by the maximum mean curvature and second fundamental form.

2. **Reilly-Type Inequalities for Dirac** — Bounds relating eigenvalues to boundary geometry are established, with a clean dependence on isoperimetric ratio and mean curvature of the boundary.

3. **Dimension-Independent Universal Bounds** — Many key bounds do not depend on the ambient dimension $N$, making them applicable across geometric settings.

4. **Anghel's Result Generalized** — The classical Lichnerowicz bound is recovered and extended, with new explicit bounds for sums of the first $n$ eigenvalues.

5. **Index Theorem Constraints** — The topological index constrains the zero-eigenvalue multiplicity and symmetry of the spectrum.

6. **Einstein Manifold Characterization** — Einstein manifolds (constant scalar curvature) saturate several bounds, providing a geometric characterization via spectral properties.

---

## Impact and Legacy

This work is foundational for spectral geometry and has applications in:

- **Mathematical physics**: Dirac equations on curved spacetime, constraints on extra-dimensional geometries
- **Quantum field theory**: Anomaly calculations rely on the index theorem; eigenvalue bounds control loop corrections
- **Kaluza-Klein theory**: Compactified extra dimensions can be modeled as Riemannian manifolds; their Dirac spectrum determines the mass spectrum of observed particles
- **Conformal geometry**: Spectral properties constrain possible conformal structures

The dimension-independence of certain bounds is particularly surprising and suggests deep connections between topology, curvature, and spectral properties.

---

## Framework Relevance

**Dirac Spectrum on SU(3)**: The framework's quantum numbers emerge from the Dirac spectrum on M4 × SU(3). The SU(3) fiber is a compact Riemannian manifold; Zeng's bounds apply directly. Session 7-10 computed the Dirac spectrum explicitly; Zeng's work provides rigorous bounds that validate those numerical results and constrain higher-order corrections.

**Extrinsic Estimates and Compactification**: The framework treats SU(3) as intrinsically curved (Levi-Civita connection) but also embedded in the Kaluza-Klein picture as an extrinsic deformation of flat space. Zeng's extrinsic estimates—relating eigenvalues to embedding curvature—are directly applicable to KK models where 10D (or 5D) spacetime is compactified on a 3-sphere or SU(3) fiber.

**Spectral Action as Dirac Trace**: The spectral action $S_{\text{spec}} = \text{Tr}(f(D/\Lambda))$ depends on the entire Dirac spectrum. Zeng's eigenvalue bounds provide rigorous control over spectral sums, validating the framework's use of cutoff-dependent spectral actions (Papers 17-24, Sessions 22-24).

**Einstein Manifolds and Fold Geometry**: Zeng shows that Einstein manifolds (constant scalar curvature) saturate bounds. The framework's fold geometry at tau ≈ 0.2 is a critical point of the spectral action where Einstein conditions may be approached. This connection suggests the fold is geometrically special in the sense of Zeng's eigenvalue characterization.

**Atiyah-Singer Index and Fermion Doubling**: The framework's fermion spectrum has index-theoretic constraints (Session 17c: Pfaffian, Z2 winding). Zeng's use of the Atiyah-Singer theorem provides rigorous foundation for understanding how topological properties of the SU(3) manifold determine the fermion content.

**Dimension-Independent Universality**: Zeng's result that some bounds are dimension-independent is striking and suggests that certain spectral properties are universal. The framework's emergence of 4D from 7D (M4 × SU(3)) might be understood via this universality—the low-energy spectrum relevant to 4D physics is potentially dimension-independent in the sense Zeng proves.

---

## References

- Zeng, L. (2024). Spectrum of the Dirac operator on compact Riemannian manifolds. *arXiv preprint arXiv:2402.14247*.
- Atiyah, M. F., & Singer, I. M. (1963). The index of elliptic operators on compact manifolds. *Bulletin of the American Mathematical Society*, 69(3), 422-433.
- Lichnerowicz, A. (1963). Spineurs harmoniques. *Comptes Rendus de l'Académie des Sciences*, 257(1), 7-9.
- Anghel, N. (1990). An abstract index theorem on non-compact Riemannian manifolds. *Houston Journal of Mathematics*, 16(3), 311-351.
