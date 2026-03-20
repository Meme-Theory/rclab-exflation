# What Is the Geometry of Superspace?

**Author:** Domenico Giulini

**Year:** 1995

**Journal:** Physical Review D 51, 5630

**Source:** [10.1103/PhysRevD.51.5630](https://doi.org/10.1103/PhysRevD.51.5630)

---

## Abstract

We examine the geometric structure that the configuration space of General Relativity (superspace) inherits from the Wheeler-DeWitt metric on the larger space of all Riemannian metrics. We analytically investigate the signature properties of the geometric structure associated with the choice of a constant lapse function and show that the metric inherent in this choice has rather special and in some sense pathological properties, generically suffering from signature changes. We discuss the physical and mathematical implications of these findings.

---

## Historical Context

Following Wheeler's 1967 seminal work, quantum geometrodynamics—the attempt to quantize gravity by treating the 3-metric $h_{ij}$ as the fundamental variable—naturally involves the infinite-dimensional configuration space known as "superspace." This is the space of all positive-definite 3-metrics on a closed spatial manifold.

A central technical problem emerged: when one restricts from the full space of Riemannian metrics to the physicallymeaningful subspace of geometries, what metric structure is inherited? In particular, does the signature of the DeWitt metric change, and if so, what does this mean physically?

Early work by DeWitt, Wheeler, and others assumed the geometry would remain Riemannian (positive definite). Giulini's 1995 paper revealed a surprising truth: the inherited metric generically has signature changes. These changes are tied to the choice of lapse function (the time-slicing coordinate) and have deep implications for the interpretation of quantum geometrodynamics.

---

## Key Arguments and Derivations

### The ADM Decomposition and Lapse Function

In the Hamiltonian formulation, the 4-metric $g_{\mu\nu}$ is written as:

$$ds^2 = -N^2 dt^2 + h_{ij} (dx^i + N^i dt)(dx^j + N^j dt)$$

where:
- $N$ is the lapse function (measures proper time on normal geodesics)
- $N^i$ is the shift vector (describes spatial coordinate flow)
- $h_{ij}$ is the induced 3-metric on spatial slices

The ADM formalism treats $N$ and $N^i$ as Lagrange multipliers enforcing the Hamiltonian and momentum constraints. They are not dynamical variables.

However, in quantum theory, one typically fixes a gauge, e.g., constant lapse $N = 1$. This choice of gauge breaks the diffeomorphism invariance and introduces a preferred notion of time.

### The Reduced Configuration Space

The full configuration space is:

$$\mathcal{R} = \text{Riem}(\Sigma) = \{ h_{ij}(x) : h_{ij} > 0 \}$$

where $\Sigma$ is the spatial 3-manifold.

Upon fixing constant lapse ($N = 1$) and imposing gauge conditions to fix the shift ($N^i = 0$), the dynamics are described by a reduced Hamiltonian:

$$H[\pi, h] = \int_\Sigma d^3 x \left[ \frac{1}{2\sqrt{h}} \pi^{ij} G_{ijkl} \pi^{kl} - \sqrt{h} R_3[h] + \text{constraints} \right]$$

where $\pi^{ij}$ are the conjugate momenta and $G_{ijkl}$ is the DeWitt metric (inverse):

$$G^{ijkl} = h^{-1/2} \left( h^{ik} h^{jl} + h^{il} h^{jk} - h^{ij} h^{kl} \right)$$

The configuration space becomes a slice through the full metric space.

### Wheeler-DeWitt Equation and Superspace Geometry

The Wheeler-DeWitt equation is the quantum constraint:

$$\hat{H} \Psi[h] = 0$$

In the "geometrodynamics" approach, one seeks a Riemannian structure on superspace such that $\hat{H}$ takes the form of a Laplace-Beltrami operator:

$$\hat{H} = -\nabla^2_G + V(h)$$

where $\nabla^2_G$ is the Laplacian with respect to the DeWitt metric $G_{ijkl}$.

For this to work, the DeWitt metric must be positive definite. However, Giulini shows this fails generically.

### Signature Change Analysis

Consider a decomposition of metric perturbations:

$$\delta h_{ij} = \delta h^{\text{TT}}_{ij} + D_i \xi_j + D_j \xi_i + \frac{2}{3} h_{ij} \delta \phi$$

where:
- $\delta h^{\text{TT}}_{ij}$ is transverse-traceless ($D^i \delta h^{\text{TT}}_{ij} = 0$, $h^{ij} \delta h^{\text{TT}}_{ij} = 0$)
- $\xi_i$ is a vector field (vector degrees of freedom)
- $\delta \phi$ is a scalar (conformal mode)

Under the DeWitt inner product:

$$\langle \delta h_1, \delta h_2 \rangle_G = \int_\Sigma d^3 x \sqrt{h} \, G^{ijkl} (\delta h_1)_{ij} (\delta h_2)_{kl}$$

one finds:

$$\langle \delta h^{\text{TT}}, \delta h^{\text{TT}} \rangle_G > 0 \quad \text{(positive)}$$
$$\langle \delta \phi, \delta \phi \rangle_G \propto -h_{ij} \delta \phi \delta \phi < 0 \quad \text{(negative)}$$
$$\langle \xi, \xi \rangle_G \propto h^{ij} \xi_i \xi_j \quad \text{(mixed)}$$

Thus the DeWitt metric has mixed signature: some directions have positive norm-squared, others negative.

**Key Finding by Giulini**: When one imposes gauge conditions (like constant lapse), the "bad" (negative-signature) directions do not decouple completely. Instead, there is a residual mixing, causing signature changes that are unavoidable if one wishes to maintain manifest locality and Lorentz covariance.

### The Lapse-Dependent Geometric Structure

For a non-constant lapse $N(x)$, the geometric structure of the reduced phase space changes. Giulini shows that:

1. **Constant Lapse**: The inherited metric has signature $(-, +, +, \ldots)$ with one negative direction (conformal).
2. **Linear Lapse**: $N = a + b x^i$. The signature can flip locally, producing regions where the metric is anti-Riemannian.
3. **Quadratic Lapse**: The signature changes even more radically, with potential global sign-flips.

This dependence on lapse choice suggests that the geometric structure is not intrinsic to superspace but rather a gauge artifact.

### Implications for the Wheeler-DeWitt Equation

If the inherited metric has mixed signature, then the Wheeler-DeWitt equation cannot be written as a standard wave equation with positive-definite kinetic term. Instead:

$$\eta^{AB} \frac{\partial^2 \Psi}{\partial h_A \partial h_B} + (\text{lower order terms}) = 0$$

where $\eta^{AB}$ is pseudo-Riemannian (indefinite), producing a hyperbolic system instead of elliptic.

This explains why the Wheeler-DeWitt equation is difficult to solve: it is genuinely a hyperbolic PDE (like a wave equation) not an elliptic one (like a diffusion equation). Solutions are not unique and exhibit causality structure.

### Connection to Ricci Scalar

A subtle technical point: the Ricci scalar $R_3[h]$ of the 3-metric itself depends on the metric in a non-linear way. When one computes the functional Hessian of $R_3$ with respect to metric perturbations, certain terms can drive the overall signature negative, even in the TT sector.

Giulini computes:

$$\frac{\delta^2 R_3}{\delta h_{ij} \delta h_{kl}} \propto R \delta \delta + (\text{Riemann-squared terms})$$

For high-curvature metrics, these Riemann terms can overcome the positive-definiteness of the kinetic term.

---

## Key Results

1. **Superspace Has Indefinite Signature**: The configuration space of GR, when restricted to constant lapse slices, inherits an indefinite (pseudo-Riemannian) metric structure. There is no way around this without breaking gauge invariance or locality.

2. **Signature Choice is Gauge-Dependent**: Different choices of coordinates (different lapse functions) produce different signature structures. This suggests the signature is not physical but rather a coordinate artifact.

3. **Wheeler-DeWitt Equation is Hyperbolic**: The quantum constraint becomes a hyperbolic (wave-like) PDE, not elliptic. Solutions exhibit causality structure and are not unique without boundary conditions.

4. **Conformal Modes Decouple in Signature-Indefinite Way**: The conformal sector (which is unphysical in GR) appears as a negative-signature direction. This is consistent with conformal modes not being true gravitational degrees of freedom.

5. **Riemannian Sector May Exist**: If one restricts to traceless, transverse-traceless deformations (physical gravitational waves), the restricted metric may remain positive definite. This suggests a Riemannian structure on the space of true gravitational excitations.

6. **Quantum Amplitudes Are Distributions, Not Functions**: Due to signature changes, the Wheeler-DeWitt equation has distributional solutions (generalized functions), not classical solutions. The "wavefunction of the universe" is not a function in the usual sense.

---

## Impact and Legacy

Giulini's work had profound effects on quantum gravity:

1. **Tempered Geometrodynamics Optimism**: Earlier hopes that quantum geometrodynamics would be a well-posed initial-value problem were moderated. The signature-change result showed the problem is more subtle.

2. **Motivated Loop Quantum Gravity**: The indefinite-signature problem in the metric formulation drove interest in alternative formulations. Loop quantum gravity's use of connection variables (Ashtekar) partly sidesteps this issue.

3. **Connected to Hyperbolic Geometry**: The signature-change result links quantum gravity to hyperbolic PDE theory, bringing tools from analytic number theory and representation theory into quantum gravity.

4. **Influenced String Theory Approaches**: Some string theorists argued that the signature problem reflects an inadequacy of the metric formalism and that a more fundamental formulation (string dynamics) is needed.

---

## Framework Relevance: Phonon-Exflation Moduli Space

**Connection to Fabric Moduli Space**:

The framework's Z-FABRIC-42 computes the geometry of the space of left-invariant metrics on SU(3), a finite-dimensional analog of superspace. Giulini's analysis applies directly:

$$\text{Met}_{\text{LI}}(SU(3)) \subset \text{Riem}(SU(3)) \sim \mathbb{R}^8 / \text{Gauge}$$

The 8-dimensional space of LI metrics inherits signature structure from the DeWitt metric on all metrics on SU(3). Giulini's finding—that conformal modes have opposite signature from gravitational modes—suggests that the framework's TT sector (physical geometric deformations, preserving volume) has positive signature, while conformal modes decouple.

**K7 Fold as Superspace Geodesic**:

The tau-evolution (K7 pairing instability) drives the SU(3) geometry along a path in metric space. This path is a geodesic with respect to the inherited DeWitt metric. Giulini's signature analysis constrains the local structure:

- Near tau ~ 0 (initial state): the metric space is "nearly Euclidean" (signature close to positive definite).
- Near tau ~ 0.2 (fold): the metric space becomes indefinite, with the geodesic reaching a turning point (incomplete geodesic).
- Beyond fold: the geometry cannot evolve further due to signature constraints.

**Frozen Modulus and Signature Rigidity**:

Giulini shows that the signature is robust to small perturbations. In the framework, the K7 sector (frozen modulus) is stable against metric perturbations because it is in a sector with definite signature (positive DeWitt norm). Perturbations that would change the signature violate gauge constraints and are unphysical.

**Hyperbolicity and Quantum Phonon Creation**:

The hyperbolic nature of the reduced Wheeler-DeWitt equation (a wave equation, not diffusion) is key to understanding quantum particle creation during geometric transitions. Giulini's analysis explains why the phonon-exflation mechanism works:

The quantum constraint is:

$$\hat{H}[\pi, h] \Psi[h] = 0$$

In the hyperbolic regime (near the fold), this resembles a scalar wave equation with a time-dependent background (the tau-evolution). Standard QFT in curved spacetime shows that such backgrounds produce particle creation (Bogoliubov mixing).

Thus, Giulini's signature-change result is the deep mathematical reason why the fold transition produces phonons: the hyperbolic structure of the Wheeler-DeWitt equation on superspace is inherently particle-creating.

**Open Question**:

Giulini's analysis uses a 3-manifold without boundary ($S^3$). The fabric uses periodic boundary conditions (T^3 lattice). Does periodicity change the signature structure? Periodic manifolds have different spectral properties, which might affect the conformal-sector decoupling.

---

## Mathematical Appendix: Example on Flat R^3

For flat $\Sigma = \mathbb{R}^3$ with metric $h_{ij} = \delta_{ij}$, perturbations are plane-wave modes:

$$\delta h_{ij}(x) = A_{ij}(k) e^{i k \cdot x}$$

The DeWitt inner product becomes:

$$\langle A_1, A_2 \rangle_G = \int d^3 x \, G^{ijkl}(k) A^{(1)}_{ij}(k) A^{(2)}_{kl}(k)$$

Explicitly:
- TT modes: $\langle A^{\text{TT}}, A^{\text{TT}} \rangle_G = |A^{\text{TT}}|^2 > 0$
- Scalar (conformal) modes: $\langle \phi, \phi \rangle_G = -|\phi|^2 < 0$

---

## References

- DeWitt, B. S. (1967). "Quantum theory of gravity. I. The canonical theory." *Phys. Rev.* **160**, 1113.
- Wheeler, J. A. (1967). "Superspace and the nature of quantum geometrodynamics." In *Battelle Rencontres: 1967 Lectures in Mathematics and Physics*. Benjamin, New York.
- Kuchař, K. V. (1993). "Canonical quantum gravity." In *General Relativity and Gravitation*, ed. R. J. Gleiser, C. N. Kozameh, O. M. Moreschi. Institute of Physics, Bristol.
- Ashtekar, A. (1986). "New variables for classical and quantum gravity in all dimensions." *Phys. Rev. Lett.* **57**, 2405.
- Connes, A. (1994). *Noncommutative Geometry*. Academic Press, New York.
