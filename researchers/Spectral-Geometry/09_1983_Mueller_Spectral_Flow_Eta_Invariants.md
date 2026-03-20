# Spectral Flow and Eta Invariants

**Author(s):** Werner Mueller

**Year:** 1983

**Journal:** Journal of Differential Geometry, Vol. 18, pp. 221-260

---

## Abstract

Mueller develops the theory of spectral flow for families of differential operators (particularly Dirac operators) and its relationship to eta invariants. The spectral flow measures how many eigenvalues cross zero as a parameter (e.g., a metric deformation) varies. The eta invariant measures the asymmetry between positive and negative eigenvalues. These spectral invariants are crucial for understanding topological properties and boundary conditions in spectral geometry.

---

## Historical Context

Atiyah, Patodi, and Singer (1975) introduced the eta invariant in their work on spectral asymmetry of Dirac operators. Mueller extended this to study families of operators and showed how the eta invariant relates to the spectral flow—the index of zero eigenvalues crossing.

This work is essential for:

1. Understanding how topological properties manifest in the spectrum.
2. Computing indices for Dirac operators with boundary conditions.
3. Defining spectral invariants that vary under metric deformation.
4. Quantum field theory on spaces with boundaries.

---

## Key Arguments and Derivations

### Eta Invariant for Dirac Operators

For a self-adjoint elliptic operator $D$ (e.g., Dirac operator), the eta invariant is defined as:

$$\eta(D) = \frac{1}{\pi} \int_0^\infty t^{s-1} \text{Tr}(D e^{-tD^2}) \, dt \bigg|_{s=0}$$

where the trace is over the full spectrum (including both positive and negative eigenvalues).

More directly, if the spectrum is $\{\pm \lambda_i\}$ (with multiplicities $m_\pm(\lambda_i)$):

$$\eta(D) = \sum_i [m_+(\lambda_i) - m_-(\lambda_i)]$$

This is the difference between the number of positive and negative eigenvalues (counting multiplicities).

For a self-adjoint operator, this is always an integer.

### Functional Definition via Zeta Function

The eta invariant can also be defined via analytic continuation:

$$\eta(D, s) = \frac{1}{\pi} \int_0^\infty t^{s-1} \text{Tr}(D e^{-tD^2}) dt$$

which converges for $\text{Re}(s) > 1/2$. By analytic continuation, one defines $\eta(D) = \eta(D, 0)$.

Alternatively:

$$\eta(D) = \sum_{\lambda_i > 0} \text{sign}(\lambda_i) |\lambda_i|^{-s} \bigg|_{s=0}$$

which can be related to the spectral zeta function:

$$\eta(D) = \zeta_+(s) - \zeta_-(s) \bigg|_{s=0}$$

where $\zeta_\pm$ are zeta functions for positive and negative eigenvalues separately.

### Spectral Flow for Parameter Families

Consider a family of Dirac operators $D_t$ depending on a parameter $t \in [0, 1]$ (e.g., $t = \tau$ the Jensen deformation parameter).

The **spectral flow** is the number of eigenvalues that cross zero as $t$ varies from $0$ to $1$:

$$\text{SF}(D_0, D_1) = \#\{\text{eigenvalues crossing } 0 \text{ as } t \text{ varies}\}$$

This is an integer, and it counts crossings with sign: an eigenvalue passing from negative to positive is $+1$, and vice versa.

**Theorem (Atiyah-Patodi-Singer, Mueller extension)**: The spectral flow is related to the eta invariant by:

$$\text{SF}(D_0, D_1) = \eta(D_0) - \eta(D_1)$$

This profound relationship connects the discrete index (number of zero crossings) to the analytic eta invariant (asymmetry of spectrum).

### Heat Kernel Representation of Eta Invariant

Mueller showed that the eta invariant can be computed from the heat kernel:

$$\eta(D) = \frac{1}{\sqrt{\pi}} \int_0^\infty t^{-1/2} \text{Tr}(D e^{-tD^2}) dt$$

The integrand has an asymptotic expansion as $t \to 0^+$:

$$\text{Tr}(D e^{-tD^2}) \sim \sum_{k=0}^\infty c_k t^{k/2}$$

Since $D$ is odd (anticommutes with the grading in chiral representation), the even powers vanish, leaving only odd powers.

The integral $\int_0^\infty t^{-1/2} t^{k/2} dt$ converges only for $k \geq 0$, and by careful analysis of the pole structure, one extracts:

$$\eta(D) = \text{(combination of } c_k \text{ for odd } k)$$

For a 4-dimensional manifold, the dominant term comes from the $k=1$ coefficient.

### Local Index Density and Eta Invariant

Mueller related the eta invariant to local geometric invariants. For a Dirac operator on a manifold with boundary, the heat kernel expansion includes boundary contributions:

$$\text{Tr}(e^{-tD^2}) = \int_M k_t(x,x) \, dV_x + \int_{\partial M} b_t(y,y) \, dA_y + \ldots$$

The volume integral gives the standard Seeley-DeWitt coefficients, while the boundary integral gives additional terms. The eta invariant is related to these boundary contributions.

Specifically, for a Dirac operator with a chosen spectral boundary condition (e.g., "chirality flips at boundary"), Mueller showed:

$$\eta(D) = \int_M (\text{local volume density}) \, dV + \int_{\partial M} (\text{local boundary density}) \, dA$$

This "local index formula" allows one to compute the eta invariant from geometric data.

### Eta Invariant Under Metric Deformation

As the metric changes, the eta invariant changes. Mueller derived the variation formula:

$$\frac{d}{dt} \eta(D_t) = -\frac{1}{\pi} \int_0^\infty t^{s-1} \text{Tr}(\dot{D}_t e^{-tD_t^2}) dt \bigg|_{s=0}$$

where $\dot{D}_t = \frac{\partial D_t}{\partial t}$.

More explicitly, if the metric changes as $g_t$:

$$\frac{d}{dt} \eta(D_{g_t}) = \text{(integral involving } \frac{\partial g_t}{\partial t} \text{ and curvature)}$$

This shows that the eta invariant is a "slow" invariant: it changes smoothly with the metric, unlike the spectral flow (which is discrete).

### Applications: Dirac Operators with Boundary Conditions

On a manifold with boundary, one must specify boundary conditions for the Dirac operator. A common choice is the **Atiyah-Patodi-Singer (APS) boundary condition**, which picks the positive spectral half of the boundary operator.

With APS boundary condition, the Dirac operator is Fredholm (has finite-dimensional kernel and cokernel), and the index is given by:

$$\text{ind}(D^+) = \text{(volume integral over interior)} + \text{(spectral flow of boundary operator)}$$

Mueller showed that the eta invariant encodes the boundary spectral flow.

### Spectral Flow on Jensen-Deformed SU(3)

For the phonon-exflation application, one would study the family of Dirac operators $D_\tau$ on SU(3) as the Jensen parameter $\tau$ varies. The spectral flow measures how many eigenvalues pass through zero.

If $\text{SF}(0, \tau_{\max}) = 0$, then no eigenvalues cross zero, and the eta invariant changes smoothly from $\eta(D_0)$ to $\eta(D_{\tau_{\max}})$.

If $\text{SF} \neq 0$, then some eigenvalues have changed sign, indicating a topological or geometric transition.

Mueller's methods allow one to compute $\text{SF}$ exactly from the heat kernel, without explicitly tracking all eigenvalues.

### Index Formula and Spectral Flow

Mueller proved a general index formula for Dirac operators:

$$\text{ind}(D^+) = \int_M \hat{A}(M) \wedge \text{ch}(E) + \frac{1}{2}(\eta(D) - \eta(\partial M))$$

where the first integral is the volume contribution and the second term is the boundary contribution via the eta invariant.

For closed manifolds (no boundary), $\eta(\partial M) = 0$, so:

$$\text{ind}(D^+) = \int_M \hat{A}(M) \wedge \text{ch}(E)$$

---

## Key Results

1. **Eta invariant definition**: $\eta(D) = \sum_i \text{sign}(\lambda_i)$ (difference of positive and negative eigenvalue counts).

2. **Spectral flow = change in eta**: $\text{SF}(D_0, D_1) = \eta(D_0) - \eta(D_1)$ (discrete index from analytic invariant).

3. **Heat kernel formula**: Eta invariant computable from heat kernel trace via odd-power coefficients.

4. **Index theorem with boundary**: Index includes volume integral plus boundary term (via eta invariant).

5. **Metric variation**: Eta invariant changes smoothly under metric deformation.

6. **APS boundary condition**: Natural framework for manifolds with boundary.

---

## Impact and Legacy

Mueller's work is foundational for:

- **Index theory**: Secondary characteristic classes, index formulas with boundaries.
- **Quantum field theory**: Spectral flow constraints on vacuum states, anomalies.
- **Topology and geometry**: Connecting topological properties to spectral data.
- **String theory**: Eta invariants in D-brane boundary conditions.
- **Gauge theory**: Moduli space topology via spectral flow.

Citations: ~800+.

---

## Connection to Phonon-Exflation Framework

**Relevance: MEDIUM to HIGH, particularly for topological consistency**

The phonon-exflation framework studies the Dirac operator $D_K$ on M4 x SU(3) as a function of the Jensen deformation parameter $\tau$. Mueller's spectral flow and eta invariant provide tools for monitoring topological changes.

### Direct Applications:

1. **Spectral flow under Jensen deformation**: As $\tau$ varies from 0 to some maximum value $\tau_{\max}$, the Dirac eigenvalues change. Mueller's spectral flow measures how many eigenvalues cross zero.

   If $\text{SF}(D_0, D_{\tau_{\max}}) = 0$, the topology is preserved (no phase transitions). If $\text{SF} \neq 0$, there is a topological change.

   Sessions 20 and 24 computed the Dirac spectrum at fixed $\tau$ values. Session 31 could track spectral flow by computing the spectrum at multiple $\tau$ values and counting crossings.

2. **Eta invariant as topological marker**: The eta invariant $\eta(D_\tau)$ characterizes the asymmetry of the positive and negative Dirac eigenvalues. For the standard SU(3) metric (no deformation, $\tau = 0$), the eta invariant is:

$$\eta(D_0) = \text{(computed from heat kernel)}$$

As $\tau$ changes, $\eta(D_\tau)$ varies. Mueller's formula predicts the variation.

3. **Index and spectral flow**: If the phonon-exflation framework is to have a consistent quantum measure (fermionic path integral), the index of the Dirac operator must be well-defined. Mueller's index formula with eta invariant ensures this.

4. **Chirality and sign symmetry**: The Dirac operator on M4 x SU(3) has a natural chirality operator $\gamma_5 = \gamma^0 \gamma^1 \gamma^2 \gamma^3 \gamma^4 \ldots$ (product of all gamma matrices). This grading splits the spectrum into $\pm$ eigenvalues.

   Mueller's eta invariant measures the asymmetry between the two halves. If the Jensen deformation breaks chirality (which it may not, since it's a metric deformation), the eta invariant would change.

5. **Constraint on deformations**: If the phonon-exflation framework specifies that certain topological invariants must be conserved (e.g., the index of the Dirac operator must remain constant), then Mueller's spectral flow must vanish. This constrains the allowed metrics.

   Specifically: if the phonon-exflation program requires that the number of positive and negative eigenvalues remain equal, then $\text{SF} = 0$.

6. **Boundary effects and internal boundaries**: Although SU(3) is a closed manifold (no boundary), the product M4 x SU(3) could be truncated (e.g., spatially finite M4), creating effective boundaries. Mueller's methods handle this via APS boundary conditions.

7. **One-loop contribution and eta**: In quantum field theory, the one-loop fermionic contribution includes the eta invariant:

$$S_{\text{1-loop,ferm}} = -\frac{1}{2}(\zeta_D'(0) + \frac{\pi}{2} \eta(D)) + \ldots$$

Mueller's methods compute both terms from heat kernels, giving the fermionic contribution to the effective action as a function of $\tau$.

**Session 31 relevance**: BA-31-3 (orientation test / eta invariant), BA-31-5 (functional determinant variation), and BA-31-6 (spectral flow and topological consistency) all depend directly on Mueller's framework.

