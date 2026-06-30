# Elasticity tetrads, mixed axial-gravitational anomalies, and (3+1)-d quantum Hall effect

**Author(s):** J. Nissinen, G.E. Volovik
**Year:** 2019
**Journal:** Physical Review Research 1, 023007 (2019)
**arXiv:** 1812.03175
**Relevance:** CRITICAL

---

## Abstract

For two-dimensional topological insulators, the integer and intrinsic quantum Hall effect is described by the gauge anomalous (2+1)-dimensional Chern-Simons response. Here, we show that three-dimensional crystalline topological insulators with no other symmetries are described by a topological (3+1)-dimensional mixed CS term. In addition to the electromagnetic U(1) gauge field, this term contains elasticity tetrad fields $E^a_\mu(r,t) = \partial_\mu X^a(r,t)$ which are gradients of crystalline U(1) phase fields $X^a(r,t)$ and describe the deformations of the crystal. The response of the Hall conductance to deformations is quantized in terms of weak momentum-space topological invariants. The elasticity tetrads, being gradients of lattice U(1) fields, have canonical dimension of inverse length.

---

## Key Arguments and Derivations

### Elasticity Tetrad Fields
The crystal structure is described by three deformed crystallographic coordinate planes, surfaces of constant phase $X^a(\mathbf{r}, t) = 2\pi n_a$ ($a = 1,2,3$). The elasticity tetrads are:

$$E^a_\mu(x) = \partial_\mu X^a(x)$$

with dimension of crystal momentum (inverse length). In the undeformed case, $X^a(\mathbf{r}, t) = \mathbf{K}_a \cdot \mathbf{r}$ where $\mathbf{K}_a$ are primitive reciprocal lattice vectors.

### Integrability (Torsion-free) Condition
In the absence of dislocations:
$$T^a = dE^a = 0$$

When dislocations are present, $T^a \neq 0$ and the torsion equals the dislocation density.

### 3+1d Topological Action
The QH response in 3+1d is:

$$S_{3+1d}[A] = \frac{1}{8\pi^2} \sum_{a=1}^{3} N_a \int d^4x \, \epsilon^{\alpha\beta\mu\nu} E^a_\alpha A_\beta \partial_\mu A_\nu$$

The integer coefficients $N_a$ are antisymmetric integrals of Green's functions (momentum-space topological invariants). The Hall conductance is:

$$\sigma^{ij} = \epsilon^{ijk} \frac{\sum_a N_a E^a_k(x)}{4\pi^2}$$

quantized in planes perpendicular to the weak Hall index $G_i = \sum_a N_a E^a_i$.

### Anomaly Cancellation (Callan-Harvey)
In the presence of dislocations ($T^a \neq 0$), the current divergence is anomalous:

$$\partial_\mu J^\mu = -\frac{1}{8\pi^2} \frac{1}{4} F_{\alpha\beta} \sum_a N_a T^a_{\mu\nu} \epsilon^{\alpha\beta\mu\nu}$$

This is canceled by fermion zero modes on dislocations (1+1d covariant anomaly), implementing the Callan-Harvey anomaly inflow mechanism.

### Dimensionless Metric
The metric from elasticity tetrads $g_{\mu\nu} = E^a_\mu E^b_\nu \delta_{ab}$ is dimensionful. The interval $dn^2 = g_{\mu\nu} dx^\mu dx^\nu$ is dimensionless — it counts spacetime distances in terms of lattice points.

### Gravitational Implications
If gravitational spacetime metric is identified with the elasticity metric, then Newton's constant, cosmological constant, and particle masses become dimensionless. This is a "dimensionless physics" where all physical parameters are pure numbers.

## Key Results

1. Elasticity tetrads $E^a_\mu = \partial_\mu X^a$ have canonical dimension of inverse length
2. 3+1d QHE described by mixed Chern-Simons with elasticity tetrads and EM gauge field
3. Prefactors $N_a$ are quantized momentum-space topological invariants
4. Hall conductance response to deformation is quantized: $d\sigma^{ij}/dE^a_k = (e^2/2\pi h) \epsilon^{ijk} N_a$
5. Dislocations carry torsion; anomaly inflow on dislocations via Callan-Harvey mechanism
6. Extension to all odd spatial dimensions is straightforward
7. Dimensionless gravitational coupling if metric identified with elasticity metric

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Elasticity tetrad | $E^a_\mu = \partial_\mu X^a(x)$ | Eq. (10) |
| 3+1d CS action | $S = \frac{1}{8\pi^2} \sum_a N_a \int d^4x \, \epsilon^{\alpha\beta\mu\nu} E^a_\alpha A_\beta \partial_\mu A_\nu$ | Eq. (14) |
| Topological invariant | $N_a = \frac{1}{8\pi^2} \int d\omega \int_{\text{BZ}} dS^i_a \, \text{Tr}[(G\partial_\omega G^{-1})(G\partial_{k_i} G^{-1})(G\partial_{k_j} G^{-1})]$ | Eq. (15) |
| Hall conductance | $\sigma^{ij} = \epsilon^{ijk} \sum_a N_a E^a_k / (4\pi^2)$ | Eq. (24) |
| Torsion = dislocations | $T^a_{\mu\nu} = \partial_\mu E^a_\nu - \partial_\nu E^a_\mu$ | Eq. (31) |
| Anomaly inflow | $\partial_\mu J^\mu = -\frac{1}{32\pi^2} F_{\alpha\beta} \sum_a N_a T^a_{\mu\nu} \epsilon^{\alpha\beta\mu\nu}$ | Eq. (32) |

## Relevance to Phonon-Exflation

This is one of the most directly relevant Volovik papers to the framework:
- **Elasticity tetrads as gravitational tetrads**: The framework treats the SU(3) fiber as a crystalline medium; the elasticity tetrads provide the mathematical language for how deformations of this medium generate effective gravity
- **Dimensionless physics**: If the metric comes from elasticity tetrads, all couplings become dimensionless — this connects to the framework's dimensionless Dirac operator on SU(3) where all masses are eigenvalue ratios
- **Torsion = dislocations**: The framework's instanton gas creates "defects" in the vacuum crystal; these carry torsion and support anomaly inflow
- **Mixed Chern-Simons**: The 3+1d CS term with elasticity tetrads connects to the framework's spectral action, which generates topological terms from the Dirac operator spectrum
- **Topological protection of $N_a$**: The quantized invariants parallel the framework's topological indices (BDI class, Pfaffian $\mathbb{Z}_2$) that protect the mechanism chain
- **Callan-Harvey on dislocations**: The anomaly inflow on defects parallels the framework's chiral anomaly structure in the Dirac spectrum
