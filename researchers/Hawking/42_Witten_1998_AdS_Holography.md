# Anti de Sitter Space and Holography

**Author(s):** Edward Witten
**Year:** 1998
**Journal:** Adv. Theor. Math. Phys. 2, 253-291 (1998)
**arXiv:** hep-th/9802150
**Relevance:** HIGH

---

## Abstract

Recently, it has been proposed by Maldacena that large $N$ limits of certain conformal field theories in $d$ dimensions can be described in terms of supergravity (and string theory) on the product of $d+1$-dimensional AdS space with a compact manifold. Here we elaborate on this idea and propose a precise correspondence between conformal field theory observables and those of supergravity: correlation functions in conformal field theory are given by the dependence of the supergravity action on the asymptotic behavior at infinity. In particular, dimensions of operators in conformal field theory are given by masses of particles in supergravity. As quantitative confirmation of this correspondence, we note that the Kaluza-Klein modes of Type IIB supergravity on $\text{AdS}_5 \times S^5$ match with the chiral operators of $\mathcal{N}=4$ super Yang-Mills theory in four dimensions. With some further assumptions, one can deduce a Hamiltonian version of the correspondence and show that the $\mathcal{N}=4$ theory has a large $N$ phase transition related to the thermodynamics of AdS black holes.

---

## Key Arguments and Derivations

### 1. Introduction

Witten builds on Maldacena's proposal that the large $N$ limit of conformally invariant theories in $d$ dimensions is governed by supergravity (and string theory) on $\text{AdS}_{d+1}$ times a compact manifold. The primary example is $\mathcal{N}=4$ super Yang-Mills in 4D with gauge group $SU(N)$, conjecturally equivalent to Type IIB superstring theory on $\text{AdS}_5 \times S^5$, with string coupling $g_s \propto g_{YM}^2$, $N$ units of five-form flux, and radius of curvature $(g_{YM}^2 N)^{1/4}$.

The paper's central contribution is a precise recipe for computing CFT observables from the supergravity partition function. The boundary of $\text{AdS}_{d+1}$ is the conformal compactification $M_d$ of $d$-dimensional Minkowski space. The conformal group $SO(2,d)$ acts on both $\text{AdS}_{d+1}$ and its boundary, providing the organizing symmetry.

### 2. Boundary Behavior (Section 2)

**2.1 Euclidean AdS.** The Euclidean version of $\text{AdS}_{d+1}$ is the open unit ball $B_{d+1}$ with metric:

$$ds^2 = \frac{4 \sum_{i=0}^d dy_i^2}{(1-|y|^2)^2}$$

The boundary is the sphere $S^d$. The metric does not extend to the boundary; instead one picks a function $f$ with a first-order zero on the boundary and defines $d\tilde{s}^2 = f^2 ds^2$, which restricts to a metric on $S^d$ defined only up to conformal transformations. Thus the boundary inherits only a conformal structure.

In the half-space representation ($x_0 > 0$):

$$ds^2 = \frac{1}{x_0^2} \sum_{i=0}^d (dx_i)^2$$

The boundary is $\mathbb{R}^d$ at $x_0 = 0$ plus a point $P$ at $x_0 = \infty$.

**2.2 Massless Field Equations.** For a scalar field $\phi$ obeying $D^i D_i \phi = 0$ on $\text{AdS}_{d+1}$: given any function $\phi_0$ on the boundary $S^d$, there is a unique extension to $B_{d+1}$ obeying the field equation. Uniqueness follows from the absence of square-integrable zero modes. The Green's function (solution singular at one boundary point) is:

$$K(x) = c \frac{x_0^d}{(x_0^2 + |x|^2)^d}$$

For gravity, the Graham-Lee theorem guarantees that any conformal structure on $S^d$ sufficiently close to the standard one arises uniquely from an Einstein metric on $B_{d+1}$ with negative cosmological constant.

**2.3 The Central Ansatz.** The paper proposes the precise AdS/CFT dictionary:

$$\left\langle \exp \int_{S^d} \phi_0 \, \mathcal{O} \right\rangle_{\text{CFT}} = Z_S(\phi_0)$$

where $Z_S(\phi_0) = \exp(-I_S(\phi))$ is the supergravity partition function with boundary condition $\phi \to \phi_0$ at infinity. For gravity:

$$Z_{\text{CFT}}(h) = Z_S(h)$$

where $h$ is the conformal structure on the boundary. For gauge fields with boundary value $A_0$:

$$\left\langle \exp \int_{S^d} J^a A_0^a \right\rangle_{\text{CFT}} = Z_S(A_0)$$

**2.4 Sample Calculations.** For a massless scalar with action $I(\phi) = \frac{1}{2}\int |d\phi|^2$, the two-point function evaluates to:

$$I(\phi) = \frac{cd}{2} \int \frac{\phi_0(x)\phi_0(x')}{|x-x'|^{2d}} \, dx \, dx'$$

confirming the operator $\mathcal{O}$ has conformal dimension $d$. For $U(1)$ gauge theory, the result reproduces the expected form for a conserved current two-point function.

The Chern-Simons term in the 5D supergravity action produces the chiral anomaly of the boundary theory -- a nontrivial consistency check.

**2.5 Massive Fields.** For a scalar of mass $m$ on $\text{AdS}_{d+1}$, the boundary operator $\mathcal{O}$ has conformal dimension:

$$\Delta = \frac{1}{2}\left(d + \sqrt{d^2 + 4m^2}\right)$$

determined by $\Delta(\Delta - d) = m^2$. Stability requires $m^2 \geq -d^2/4$ (the Breitenlohner-Freedman bound), allowing "tachyonic" fields that correspond to relevant perturbations ($\Delta < d$) of the boundary CFT.

**2.6 Comparison to Experiment.** The Kaluza-Klein spectrum of Type IIB on $\text{AdS}_5 \times S^5$ (computed by Kim, Romans, and van Nieuwenhuizen) matches precisely with the chiral operators of $\mathcal{N}=4$ SYM. Specifically, the $k$-fold symmetric traceless product of 6 scalars in SYM has dimension $\Delta = k$ for $k \geq 2$, matching KK masses $m^2 = k(k-4)$.

### 3. Hamiltonian Approach and Phase Transitions (Section 3)

**3.1 Hamiltonian Interpretation.** By slicing $\text{AdS}$ by constant-time surfaces, one obtains a Hamiltonian version: the Hilbert space of string theory on $\text{AdS}_{d+1} \times W$ equals the Hilbert space of the CFT on $S^{d-1}$.

**3.2 Hawking-Page Phase Transition.** For the $\mathcal{N}=4$ theory on $S^3$, at low temperature the dominant saddle point is thermal AdS (no black hole). Above a critical temperature $T_c \sim 1/R$ (where $R$ is the $S^3$ radius), the AdS-Schwarzschild black hole dominates -- the Hawking-Page phase transition. In the dual field theory, this is a large $N$ deconfinement transition.

**3.3 Wilson Loops and Confinement.** Witten proposes computing Wilson loops via minimal surfaces in AdS. For the conformal $\mathcal{N}=4$ theory, the potential between quarks goes as $1/L$ (Coulombic), not confining. But by studying theories at finite temperature or with broken conformal invariance, one can explore confinement from the AdS side.

---

## Key Results

1. Established the precise AdS/CFT dictionary: CFT correlation functions = dependence of supergravity action on boundary data.
2. Derived the mass-dimension relation $\Delta(\Delta - d) = m^2$ linking bulk masses to boundary operator dimensions.
3. Matched the full Kaluza-Klein spectrum of Type IIB on $\text{AdS}_5 \times S^5$ with chiral operators of $\mathcal{N}=4$ SYM.
4. Showed the Chern-Simons term in 5D supergravity reproduces the chiral anomaly of the boundary theory.
5. Identified the Hawking-Page phase transition in AdS-Schwarzschild as a large $N$ deconfinement transition in the dual gauge theory.
6. Proposed the computation of Wilson loops via minimal surfaces in AdS space.
7. Demonstrated the Breitenlohner-Freedman stability bound $m^2 \geq -d^2/4$ for scalars in AdS, corresponding to unitarity bounds on operator dimensions.

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| AdS metric (ball) | $ds^2 = \frac{4\sum dy_i^2}{(1-\|y\|^2)^2}$ | Eq. (2.1) |
| AdS metric (half-space) | $ds^2 = \frac{1}{x_0^2}\sum_{i=0}^d (dx_i)^2$ | Eq. (2.6) |
| CFT/AdS ansatz (scalar) | $\langle e^{\int \phi_0 \mathcal{O}} \rangle_{\text{CFT}} = Z_S(\phi_0)$ | Eq. (2.11) |
| CFT/AdS ansatz (gravity) | $Z_{\text{CFT}}(h) = Z_S(h)$ | Eq. (2.12) |
| Supergravity partition function | $Z_S(\phi_0) = \exp(-I_S(\phi))$ | Eq. (2.10) |
| Scalar two-point function | $I(\phi) = \frac{cd}{2}\int \frac{\phi_0(x)\phi_0(x')}{|x-x'|^{2d}} dx\,dx'$ | Eq. (2.23) |
| Mass-dimension relation | $\Delta(\Delta - d) = m^2$ | Eq. (2.43) |
| Operator dimension | $\Delta = \frac{1}{2}(d + \sqrt{d^2 + 4m^2})$ | Eq. (2.44) |
| Massive scalar action | $I(\phi) = \frac{1}{2}\int d\mu\,(|d\phi|^2 + m^2\phi^2)$ | Eq. (2.33) |
| $p$-form mass-dimension | $(\Delta + p)(\Delta + p - d) = m^2$ | Eq. (2.45) |

---

## Relevance to Phonon-Exflation

The AdS/CFT correspondence provides structural context for the phonon-exflation framework in several ways. The Kaluza-Klein spectrum on $\text{AdS}_5 \times S^5$ and the mass-dimension relation $\Delta(\Delta-d) = m^2$ are directly analogous to the KK spectrum on $M_4 \times SU(3)$ that determines the Dirac operator eigenvalues central to the framework. The Hawking-Page phase transition -- a thermal deconfinement transition in the boundary theory -- provides a partial structural parallel to the instanton-driven fold transition in the framework, though the analogy is weakened by the absence of an AdS geometry in the phonon-exflation setting. The holographic principle's encoding of bulk degrees of freedom on a lower-dimensional boundary resonates with the framework's encoding of 4D physics in the internal geometry, but the framework operates in a fundamentally different regime (compact internal space with evolving modulus, not asymptotically AdS).
