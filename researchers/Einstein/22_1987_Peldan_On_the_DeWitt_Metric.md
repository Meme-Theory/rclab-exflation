# On the DeWitt Metric

**Author:** Peter Peldan

**Year:** 1987

**Journal:** Journal of Geometry and Physics 4, 493

**Source:** [10.1016/0393-0440(87)90004-0](https://doi.org/10.1016/0393-0440(87)90004-0) | [ADS](https://ui.adsabs.harvard.edu/abs/1987JGP.....4..493P/abstract)

---

## Abstract

This paper provides a comprehensive differential-geometric analysis of the DeWitt metric on the space of Riemannian metrics of a compact manifold. The DeWitt metric naturally emerges in the Hamiltonian formulation of General Relativity through the canonical constraint analysis. We examine the differential-geometric properties of this metric, including its signature, curvature, and geodesic structure. We discuss the connection between the DeWitt metric and the topology of superspace, establishing foundational results for the geometry of quantum gravity configuration spaces.

---

## Historical Context

General Relativity can be formulated in two mathematically distinct ways: the covariant (Lagrangian) picture and the canonical (Hamiltonian) picture. The Lagrangian approach, pioneered by Einstein and refined by Dirac, focuses on the metric tensor $g_{\mu\nu}$ as the fundamental dynamical variable and derives equations of motion from the action principle.

The Hamiltonian approach, developed by Dirac and Arnowitt-Deser-Misner (ADM), transforms this into a dynamical system in the space of spatial metrics. Here, the primary variables are the 3-metric $h_{ij}$ on spatial slices and their conjugate momenta $\pi^{ij}$. The dynamics are constrained by the Hamiltonian and momentum constraints.

A natural question arises: what is the geometric structure of the space of all possible 3-metrics $h_{ij}$ on a closed 3-manifold $\Sigma$? What metric tensor should one use to measure distances in this space? In 1967, John Wheeler proposed a metric:

$$G_{ijkl}(h) = \sqrt{h} \left( h_{ik} h_{jl} + h_{il} h_{jk} - h_{ij} h_{kl} \right)$$

This metric—called the Wheeler metric or DeWitt metric—is not arbitrary. It emerges naturally from the kinetic term in the ADM Hamiltonian constraint and represents the inertia tensor of the gravitational field itself. Peldan's 1987 work was the first rigorous study of the differential-geometric properties of this metric.

---

## Key Arguments and Derivations

### Construction of the DeWitt Metric

The configuration space of General Relativity is the space of all Riemannian metrics on a compact 3-manifold $\Sigma$:

$$\text{Riem}(\Sigma) = \{ h_{ij} : h_{ij} \text{ positive definite}, h_{ij} \in C^\infty(\Sigma) \}$$

This space is infinite-dimensional. A point in $\text{Riem}(\Sigma)$ is a full metric tensor $(h_{ij})$.

The tangent space at a metric $h$ consists of symmetric 2-tensor fields (metric perturbations) $\delta h_{ij}$. A Riemannian metric on the tangent space must define a notion of distance between nearby metrics.

The DeWitt metric uses a tensor-product structure. For two perturbations $\delta h^{(1)}_{ij}$ and $\delta h^{(2)}_{kl}$, their inner product is:

$$\langle \delta h^{(1)}, \delta h^{(2)} \rangle_G = \int_\Sigma d^3 x \sqrt{h} \, G^{ijkl}(h) \, \delta h^{(1)}_{ij} \, \delta h^{(2)}_{kl}$$

where

$$G^{ijkl} = h^{-1/2} \left( h^{ik} h^{jl} + h^{il} h^{jk} - h^{ij} h^{kl} \right)$$

Peldan analyzes the metric tensor $G_{ijkl}$ as an object on the infinite-dimensional manifold $\text{Riem}(\Sigma)$ and asks: what are its geometric properties?

### Signature Analysis

The most striking result concerns the metric's signature. For a generic metric $h$, the tensor $G_{ijkl}$ is not uniformly positive or negative definite. Instead, it has mixed signature:

- **Trace-free perturbations** (transverse-traceless or TT modes): positive eigenvalues
- **Conformal perturbations** $\delta h_{ij} = 2 h_{ij} \delta \phi$: negative eigenvalues
- **Mixed modes**: zero eigenvalues

More precisely, decompose $\delta h_{ij}$ as:

$$\delta h_{ij} = \delta h^{\text{TT}}_{ij} + \frac{1}{3} h_{ij} \delta h^{(\text{trace})} + (\text{conformal})$$

Then:
- $\langle \delta h^{\text{TT}}, \delta h^{\text{TT}} \rangle_G > 0$
- $\langle \text{conformal}, \text{conformal} \rangle_G < 0$

This signature change is not pathological—it reflects the physical fact that conformal transformations of the metric do not change the gravitational degrees of freedom. The conformal sector is "unphysical" in the canonical theory and naturally decouples.

**Signature**: indefinite (or in restricted sectors: Riemannian)

### Curvature of Superspace

Peldan computes the Riemann curvature tensor of the DeWitt metric. The Levi-Civita connection on $\text{Riem}(\Sigma)$ with metric $G_{ijkl}$ is non-trivial and exhibits curvature.

For a simple case: if $\Sigma = S^3$ and we restrict to Einstein metrics (constant Ricci scalar), the restricted manifold is finite-dimensional. Peldan shows that its Riemannian curvature can be computed explicitly:

$$R_{abcd} = \frac{1}{3} (g_{ac} g_{bd} - g_{ad} g_{bc}) + \text{corrections}$$

For the full infinite-dimensional space $\text{Riem}(\Sigma)$, the curvature is more complex. Geodesic deviation equations take the form:

$$\frac{D^2}{dt^2} V^{ij} + R^{ijkl} V_{kl} = 0$$

where $V^{ij}$ is a variation vector (metric perturbation) along a geodesic path through metric space, and $D/dt$ is the covariant derivative compatible with $G_{ijkl}$.

### Geodesics in Superspace

A geodesic in the space of metrics represents a path of constant "velocity" in metric space. The geodesic equations are:

$$\frac{D h_{ij}}{dt} = 0$$

where $D/dt$ is the covariant derivative with respect to the DeWitt connection.

Peldan proves that:

1. **Geodesics are well-defined**: For any initial metric $h_0$ and any metric perturbation (tangent vector) $\dot{h}_0$, there exists a unique geodesic $h(t)$ with $h(0) = h_0$ and $\dot{h}(0) = \dot{h}_0$.

2. **Geodesics may not be globally defined**: The geodesic may reach a singularity (e.g., metrics with vanishing volume) in finite affine parameter.

3. **Geodesic completeness**: The space $\text{Riem}(\Sigma)$ is geodesically incomplete unless additional restrictions are imposed.

### Topology and Moduli

A profound observation by Peldan: the topology of the space of metrics depends on the underlying 3-manifold $\Sigma$:

- If $\Sigma$ is simply connected (like $S^3$), the diffeomorphism group is connected, and $\text{Riem}(\Sigma)/\text{Diff}(\Sigma)$ (quotient by gauge transformations) is a Hausdorff manifold.

- If $\Sigma$ has non-trivial topology, the moduli space can be disconnected, with different components corresponding to topologically distinct metrics.

For the KK case of interest to the framework (Sigma = $S^1 \times \Sigma_3$), the DeWitt metric on the full metric space decomposes into sectors labeled by compactification radius $R$ and shape of $\Sigma_3$.

---

## Key Results

1. **DeWitt Metric is Well-Defined but Indefinite**: The metric on the space of Riemannian metrics is canonical and emerges from the ADM formalism, but it has mixed signature. This is a feature, not a bug—it reflects the unphysical (conformal) directions.

2. **Superspace Inherits Lorentzian Signature**: When restricted to physical (gauge-invariant) degrees of freedom, the DeWitt metric becomes Riemannian, consistent with the hyperbolic nature of Einstein's equations.

3. **Geodesic Structure is Non-Trivial**: Paths of minimal "metric distance" in superspace are not straight lines but curves determined by the DeWitt connection. These geodesics represent natural evolutions of the geometry.

4. **Connection to Quantum Gravity**: The DeWitt metric is essential for understanding the Wheeler-DeWitt equation:

$$\hat{H} \Psi[h] = 0$$

where $\Psi[h]$ is the wavefunction of the universe. The norm on the space of wavefunctions is induced by the DeWitt metric.

5. **Superspace Topology is Non-Trivial**: The moduli space of metrics modulo diffeomorphisms has a rich topological structure, with implications for quantum gravity path integrals.

---

## Impact and Legacy

Peldan's paper was foundational for the field of quantum geometrodynamics and superspace geometry:

1. **Established Rigor for Wheeler's Proposal**: Wheeler's 1967 intuition was vindicated. The DeWitt metric is the "right" way to measure distances in superspace.

2. **Inspired Loop Quantum Gravity**: Subsequent work by Ashtekar, Smolin, and others used the DeWitt metric as a starting point for constructing quantum geometry operators.

3. **Linked to Supergravity**: In supersymmetric versions of gravity, the DeWitt metric appears as the target space metric for the supergravity action. Peldan's analysis clarified the geometric meaning.

4. **Provided Tools for Moduli Space Analysis**: The differential geometry of infinite-dimensional metric spaces, developed here, became essential for studying string theory moduli spaces.

---

## Connection to Phonon-Exflation Framework

**Direct Application: Z-FABRIC-42 and DeWitt Metric on SU(3)**

In Session 42, the framework computed the DeWitt metric $G_{AB}$ on the space of left-invariant metrics on the SU(3) fiber. Peldan's formalism provides the mathematical foundation:

$$G_{AB}(g) = \text{(measure-preserving form on } \text{Met}_{\text{LI}}(SU(3)))$$

where indices $A, B$ label the 8 generators of SU(3) and $g$ is a metric in the family.

**Tau-Geodesics and the Fold**:

The framework's K7 pairing instability drives the SU(3) metric along a 1-dimensional path (tau-evolution) in the 8-dimensional moduli space of left-invariant metrics. The existence and structure of this geodesic is determined by the DeWitt metric.

At the fold (around tau ~ 0.2), the geometry becomes singular or turns around. Peldan's analysis of geodesic incompleteness directly applies: the geodesic in metric space reaches a turning point where the volume-preserving deformation becomes impossible.

**Signature Implications**:

Peldan shows that conformal modes decouple (negative signature in DeWitt metric). In the framework, the K7 sector is conformal-neutral (volume-preserving TT deformations), suggesting that the gravitational degrees of freedom are purely TT and thus have positive DeWitt signature throughout the transit.

**Connection to Frozen Modulus**:

The stability of tau during the cosmic evolution (freeze at the fold) corresponds to tau being a geodesic fixed point in the DeWitt metric. Perturbations to tau decay back to the fold—a statement about the curvature and signature of the DeWitt metric near this point.

**Open Question**:

Peldan's analysis assumes a closed manifold $\Sigma = S^3$ for the spatial 3-manifold. The fabric is a T^3 lattice (toroidal topology), not spherical. Does the DeWitt metric change qualitatively under this topological change? Periodic vs. closed boundary conditions affect the spectrum of geometric operators and may alter the moduli structure.

---

## Mathematical Appendix: Explicit Formula on S^3

For $\Sigma = S^3$ with the round metric $h_{ij}^{(0)}$ of radius $a$, the DeWitt metric at this point is:

$$G^{ijkl}(h^{(0)}) = a^{-2} \left[ \delta^{(i|}\delta^{k|} \delta^{|j)}\delta^{|l)} - \frac{1}{3} \delta^{ij} \delta^{kl} \right]$$

(up to proportionality). Perturbations $\delta h_{ij}$ decompose into spherical harmonics on $S^3$, and each harmonic sector has a definite sign under $G^{ijkl}$.

---

## References

- Wheeler, J. A. (1967). "Superspace and the Nature of Quantum Geometrodynamics." In *Battelle Rencontres: 1967 Lectures in Mathematics and Physics*. Benjamin, New York.
- DeWitt, B. S. (1967). "Quantum Theory of Gravity. I. The Canonical Theory." *Phys. Rev.* **160**, 1113.
- Arnowitt, R., Deser, S., Misner, C. W. (1962). "The Dynamics of General Relativity." In *Gravitation: An Introduction to Current Research*, ed. L. Witten. Wiley, New York.
- Ashtekar, A., Lewandowski, J. (2004). "Background independent quantum gravity: a status report." *Class. Quant. Grav.* **21**, R53.
- Connes, A., Chamseddine, A. H. (2007). "The spectral action principle." *Comm. Math. Phys.* **186**, 731.
