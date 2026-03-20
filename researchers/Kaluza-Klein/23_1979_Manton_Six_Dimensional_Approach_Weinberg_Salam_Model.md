# A New Six-Dimensional Approach to the Weinberg-Salam Model

**Author(s):** Nicholas S. Manton

**Year:** 1979

**Journal:** Nuclear Physics B 158:141–153

---

## Abstract

We show that the Weinberg-Salam electroweak model can be embedded in a six-dimensional spacetime with pure Yang-Mills theory. The Standard Model gauge group SU(2) × U(1), together with the Higgs field and its interactions, emerges from the dimensional reduction of 6D Yang-Mills on a compact internal space. The Higgs mass and vacuum expectation value are geometric quantities determined by the compactification geometry. This provides a unified picture where electroweak symmetry breaking arises purely from geometry, without introducing the Higgs as an independent degree of freedom. The mechanism demonstrates that the gauge sector, scalar sector, and scalar-gauge couplings in the Standard Model all have a common geometric origin in higher dimensions.

---

## Historical Context

Manton's 1979 paper was a landmark in understanding how the Weinberg-Salam model emerges from pure higher-dimensional geometry. While Kaluza's original 1921 work showed how Einstein gravity and Maxwell electromagnetism emerge from 5D general relativity, and Klein (1926) developed quantum mechanics in this context, the question of how more complex gauge theories (especially non-abelian ones) emerge geometrically remained open.

Manton's key insight was that non-abelian gauge theories, which seem to require fundamental scalar fields (like the Higgs) at four dimensions, could instead be understood as dimensional reduction of pure Yang-Mills in higher dimensions. The Higgs field is not fundamental; it is a component of the higher-dimensional metric or connection.

This result influenced decades of research in extra-dimensional model building and established a paradigm: physical scalars at 4D can have geometric origins in higher dimensions. This is central to modern approaches to the hierarchy problem and grand unification.

---

## Key Arguments and Derivations

### Dimensional Reduction of 6D Yang-Mills

Consider 6D Yang-Mills theory with gauge group $G$ on a manifold $\mathcal{M}_4 \times K$, where $\mathcal{M}_4$ is 4D spacetime and $K$ is a compact internal space.

The 6D Yang-Mills action is:

$$S = \int d^6 x \sqrt{-g} \, \text{Tr}(F^{(6)} \wedge * F^{(6)})$$

where $F^{(6)} = dA^{(6)} - A^{(6)} \wedge A^{(6)}$ is the 6D Yang-Mills curvature and $*$ is the Hodge dual.

The metric decomposes as:

$$g_{AB}^{(6)} = \begin{pmatrix} g_{\mu\nu}^{(4)} & 0 \\ 0 & g_{ij}^{(K)} \end{pmatrix}$$

where $A, B = 0, \ldots, 5$; $\mu, \nu = 0, \ldots, 3$; $i, j = 4, 5$.

The 6D gauge field decomposes as:

$$A^{(6)} = A_\mu^{(4)} dx^\mu + A_i^{(4)} dx^i$$

where $A_\mu^{(4)}$ are the 4D gauge fields and $A_i^{(4)}$ (components along internal directions) become 4D scalars.

### Reduction on $S^1$ (Circle Compactification)

For the simplest case, $K = S^1$ (one compact dimension), compactify at radius $R$. Expand the 6D fields in Fourier modes:

$$A_\mu(x, y) = \sum_{n=-\infty}^{\infty} a_\mu^{(n)}(x) e^{i n y / R}$$

$$A_y(x, y) = \sum_{n=-\infty}^{\infty} \phi_n(x) e^{i n y / R}$$

The 6D Yang-Mills action yields a 4D effective action after integrating out the compact direction.

At low energies (below the compactification scale $M_c \sim 1/R$), only the zero modes $n=0$ survive:

$$S_{\text{eff}} = \int d^4 x \left[ -\frac{1}{4} F_{\mu\nu} F^{\mu\nu} + \frac{1}{2} (D_\mu \phi_0)^2 + V_{\text{eff}}(\phi_0) \right]$$

where $\phi_0 = A_y^{(0)}$ is the 4D scalar from the internal gauge field component, and $D_\mu$ is the covariant derivative in the gauge group $G$.

Crucially, the potential $V_{\text{eff}}(\phi_0)$ arises from higher-dimensional geometry:

$$V_{\text{eff}}(\phi_0) = \text{Tr}([A_i, A_j] [A^i, A^j]) / R^2$$

This is a pure geometric term—no Higgs potential needs to be added by hand.

### Embedding SU(2) × U(1) in 6D SU(3)

To obtain the Weinberg-Salam gauge group $SU(2)_L \times U(1)_Y$, Manton constructs a specific embedding in 6D $SU(3)$ Yang-Mills:

$$SU(3) \supset SU(2)_L \times U(1)_Y$$

The 6D SU(3) connection has components $A_A^{\alpha\beta}$ ($\alpha, \beta = 1, 2, 3$). The internal $S^1$ compactification breaks $SU(3)$ down to $SU(2) \times U(1)$ (and possibly additional factors, depending on the specific compactification geometry).

The 4D scalars are the internal components:

$$\phi = A_4 + i A_5$$

in the adjoint of $SU(3)$. After reduction, $\phi$ decomposes into components transforming under $SU(2)_L \times U(1)_Y$.

### Higgs as Goldstone Boson

A key result is that the Higgs field emerges as a Goldstone boson of the higher-dimensional geometry. The Higgs VEV:

$$\langle \phi \rangle = v$$

corresponds to a Wilson line:

$$W = \exp\left( i \oint A_5 dy \right) = \exp(i v)$$

This Wilson line acts as an order parameter for the compactification geometry. When $v \neq 0$, the $SU(3)$ gauge symmetry is broken to $SU(2) \times U(1)$ in the low-energy 4D theory.

### Higgs Potential

The effective Higgs potential arises from the 6D Yang-Mills action. Manton shows that the quadratic and quartic terms emerge naturally:

$$V(\phi) \sim -\mu^2 |\phi|^2 + \lambda |\phi|^4$$

with the coefficients determined by the compactification radius $R$ and the gauge coupling $g_{YM}$:

$$\mu^2 \propto 1/R^2, \quad \lambda \propto g_{YM}^2$$

This means the Higgs mass and quartic coupling are not free parameters but are determined by the geometry and the fundamental gauge coupling.

### Electroweak Symmetry Breaking Mechanism

Electroweak symmetry breaking occurs when the Higgs potential develops a minimum at $\langle \phi \rangle = v \neq 0$. This happens when:

$$\frac{dV}{d|\phi|} \bigg|_{|\phi|=v} = 0$$

$$-2\mu^2 v + 4\lambda v^3 = 0$$

$$v = \sqrt{\mu^2 / (2\lambda)}$$

The ratio $v^2 / \lambda$ determines the Higgs mass:

$$m_H^2 = -\mu^2 + 3\lambda v^2 = \mu^2$$

All these quantities—the VEV, Higgs mass, and coupling strengths—are geometric: they depend only on $R$ and $g_{YM}$.

---

## Key Results

1. **Higgs from geometry**: The Higgs field and its potential emerge purely from 6D Yang-Mills, not from an independent scalar sector.

2. **Unified gauge-scalar origin**: Gauge bosons (from $A_\mu^{(4)}$) and the Higgs (from $A_i^{(4)}$) have the same geometric source.

3. **Compactification scale**: The Higgs mass and coupling are related to the compactification radius: $m_H \sim 1/R$.

4. **No fundamental scalar**: Unlike the Standard Model where the Higgs is postulated, here it is derived. This eliminates the need to fine-tune a scalar sector.

5. **Grand unification hints**: The embedding of SU(2)×U(1) in larger groups (SU(3), SU(5)) suggests unification at the compactification scale.

---

## Impact and Legacy

Manton's 1979 paper was foundational for extra-dimensional approaches to the Standard Model:

- **Kaluza-Klein phenomenology**: Established the program of deriving low-energy physics from higher-dimensional geometry.
- **Heterotic string theory**: String compactifications often realize Manton's mechanism for obtaining realistic gauge groups.
- **Modern grand unification**: Many GUT scenarios in extra dimensions follow the Manton paradigm.
- **Composite Higgs models**: Ideas about the Higgs as a composite or geometric object drew inspiration from Manton's work.
- **Higgs boson discovery implications**: When the Higgs was discovered at 125 GeV, questions about its fundamental nature led back to works like Manton's proposing geometric origins.

The paper is a touchstone for understanding how dimensional reduction provides a unified picture of gauge interactions and scalar fields.

---

## Connection to Phonon-Exflation Framework

**Geometric Higgs**: Manton's principle—that the Higgs emerges from internal geometry—is directly parallel to phonon-exflation. In the framework, the electron mass and coupling constants emerge from the SU(3) fiber geometry encoded in the Dirac spectrum on homogeneous spaces.

**Internal compactification**: Both Manton's 6D Yang-Mills and phonon-exflation use internal compact geometry (6D YM on $S^1$, phonon-exflation on SU(3)) to generate effective 4D scalars and masses.

**Wilson line analogy**: Manton's Wilson line acting as an order parameter parallels phonon-exflation's tau field—both are geometric order parameters for internal compactification.

**Dimensionality**: Manton works in 6D (4+2); phonon-exflation is effectively 7D (4+3). The SU(3) fiber is 8-dimensional as a manifold, but the effective dynamics (via spectral action) focus on the 3-dimensional radii subspace.

**Potential generation**: Manton's potential arises from compactification geometry; phonon-exflation's masses arise from spectral action variation—both are consequences of internal geometry, not ad hoc.

**Electroweak scale**: Manton's Higgs mass depends on $1/R$ (compactification scale); phonon-exflation's weak scale depends on the spectral action monotonicity across tau-space, both generating hierarchy geometrically.

**Relevance**: Manton's work demonstrates the conceptual viability of deriving Standard Model structure from internal geometry. Phonon-exflation applies this principle to a dynamical (tau-evolving) internal geometry, with the added feature that the internal fiber couples to 4D cosmology through the spectral action and BCS dynamics.

---

## References

- Manton, N. S. "A New Six-Dimensional Approach to the Weinberg-Salam Model." Nucl. Phys. B 158 (1979) 141–153.
- DeWitt, B. S. "Dynamical Theory of Groups and Fields." In *Relativity, Groups and Topology*, edited by C. DeWitt and B. DeWitt. Gordon and Breach, 1964.
- Related: Witten, E. "Dimensional Reduction of Superstring Models." Phys. Lett. B 155 (1985) 151–155.
