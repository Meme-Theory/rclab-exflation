# The Lie Derivative of Spinor Fields: Theory and Applications

**Author(s):** L. Fatibene, R.G. McLenaghan, G. Sparano
**Year:** 2005
**Journal:** International Journal of Geometric Methods in Modern Physics, 2(3):325--358

---

## Abstract

We present a comprehensive differential-geometric treatment of the Lie derivative of spinor fields on reductive G-structures over principal bundles. The framework recovers Kosmann's classical definition as a special case and extends it to generalized infinitesimal automorphisms. We introduce the concept of the "reductive Lie derivative" — a gauge-natural generalization applicable to arbitrary vector bundles associated with the structure group. We provide new characterizations of the Killing equation and relate Penrose's spinor calculus to the modern geometric viewpoint. Applications to variational calculus and the geometry of spinor Lagrangians are discussed.

---

## Historical Context

The Lie derivative measures how a geometric object changes along the flow of a vector field. For scalars and tensors, this is straightforward: if $X$ is a vector field and $\phi$ is a scalar, then $\mathcal{L}_X \phi = X(\phi)$ (directional derivative).

For spinor fields, the situation is more delicate. Spinors are sections of a spinor bundle (an associated bundle of a principal spin bundle), and the standard Lie derivative formula (difference of pulled-back vs. original sections) involves parallel transport that depends on a \emph{choice of connection}. Different connections give different Lie derivatives — so which one is geometrically "natural"?

**Kosmann (1970s)**: Proposed that there exists a canonical choice of connection on the spinor bundle, the "Kosmann lift," such that the resulting Lie derivative is connection-independent and depends only on the underlying metric geometry. This resolved the ambiguity and became the standard definition in general relativity.

**Modern development (1980s--2000s)**: Fatibene and others realized that Kosmann's construction is a special case of a broader framework called "gauge-natural" (or "natural") transformations in differential geometry. This framework applies not only to spinors, but to all associated bundles, and provides a unified language for all "natural" (coordinate-independent) Lie derivatives.

Fatibene-McLenaghan-Sparano's 2005 paper systematizes this unified viewpoint and connects it to Penrose's original spinor calculus (1960s), showing that Penrose's spinor index-raising and lowering operations are geometric manifestations of the reductive Lie derivative.

---

## Key Arguments and Derivations

### G-Structures and Reductive Decomposition

A G-structure $P$ on a manifold $M$ is a principal bundle with structure group $G \subset GL(n, \mathbb{R})$ (or $GL(n, \mathbb{C})$). For a Riemannian manifold, the structure group is $O(n)$ (or $SO(n)$ for oriented manifolds); the frame bundle is the principal bundle, and the G-structure is a subbundle consisting of orthonormal frames.

A reductive G-structure is one where the structure group $G$ admits a reductive decomposition $\mathfrak{gl}(n) = \mathfrak{g} \oplus V$, where $\mathfrak{g}$ is the Lie algebra of $G$ and $V$ is an invariant complement. For $G = SO(n)$ (the special orthogonal group), we have:
$$\mathfrak{gl}(n) = \mathfrak{so}(n) \oplus \mathbb{R}^n$$

where $\mathbb{R}^n$ (tangent vectors) and $\mathfrak{so}(n)$ (skew-symmetric transformations) are the two parts.

The reductive decomposition induces a canonical separation of the "Lie bracket" between infinitesimal frame transformations (the $\mathfrak{so}(n)$ part) and vector field directions (the $\mathbb{R}^n$ part).

### Kosmann Lift and Canonical Connection

Given a vector field $X$ on $M$ and a reductive G-structure $P$, the Kosmann lift $X^P$ is a vector field on $P$ (the principal bundle) satisfying:
1. $X^P$ projects down to $X$ on $M$.
2. $X^P$ respects the $G$-action: $[X^P, \rho_a] = 0$ where $\rho_a$ are the fundamental vector fields generating the $G$-action.
3. $X^P$ is horizontal with respect to the \emph{canonical connection} induced by the reductive decomposition.

The canonical connection is the unique $G$-invariant connection on $P$ such that:
$$\nabla_X Y = [X, Y] + \frac{1}{2} [X, [Y, \cdot]]_V$$

where the bracket is the Lie bracket of vector fields, and $[\cdot, \cdot]_V$ denotes projection onto the $V$ component of the reductive decomposition.

For an orthonormal frame bundle with $\mathfrak{so}(n)$ as the structure Lie algebra, this canonical connection is precisely the Levi-Civita connection (the unique torsion-free, metric-compatible connection on a Riemannian manifold).

### Lie Derivative via Kosmann Lift

With the Kosmann lift in hand, the Lie derivative of a spinor field $\psi$ along $X$ is defined as:
$$\mathcal{L}_X \psi = \text{lim}_{t \to 0} \frac{\psi(p) - (\text{Parallel transport along } \phi_t(p) \text{ by } X^P) \psi(\phi_t(p))}{t}$$

where $\phi_t$ is the flow of $X$, and parallel transport uses the Levi-Civita connection on the spinor bundle.

The key result (Fatibene et al.): This Lie derivative is \emph{independent of the choice of spinor bundle connection} (all metric-compatible, torsion-free connections on the spinor bundle give the same answer). Thus, the Kosmann Lie derivative is a purely geometric, connection-independent object.

Explicitly, the formula is:
$$\mathcal{L}_X \psi = X(\psi) + \frac{1}{4} (\nabla_\mu X_\nu) \gamma^{\mu\nu} \psi$$

where $\gamma^{\mu\nu} = [\gamma^\mu, \gamma^\nu] / 2$ are the commutators of Dirac matrices, and $\nabla_\mu X_\nu = \partial_\mu X_\nu - \Gamma^\lambda_{\mu\nu} X_\lambda$ is the covariant derivative of the vector field.

The term $\frac{1}{4} (\nabla_\mu X_\nu) \gamma^{\mu\nu}$ is the "spin contribution" — it accounts for the fact that spinors rotate as the vector field's direction varies.

### Killing Spinors and the Killing Equation

A Killing spinor is a solution to:
$$\nabla_\mu \zeta = \lambda \gamma_\mu \zeta$$

for some constant $\lambda$ (often taken to be $\lambda = 0$ for "covariantly constant spinors" or $\lambda \neq 0$ for "Killing spinors with parameter").

Fatibene et al. provide a new characterization: a spinor $\zeta$ is a Killing spinor if and only if its Lie derivative along \emph{every} vector field vanishes:
$$\mathcal{L}_X \zeta = 0 \quad \forall X$$

This equivalence connects the algebraic Killing equation (a differential equation) to the geometric condition (invariance under all flows) — providing intuition for why Killing spinors are so special.

### Reductive Lie Derivative and Gauge-Natural Bundles

The reductive Lie derivative extends to any associated bundle $E = P \times_G F$ (where $F$ is a representation of $G$). The general formula is:
$$\mathcal{L}_X s = X(s) + \rho_*(X^P) s$$

where $s$ is a section of $E$, $X(s)$ is the directional derivative, and $\rho_*(X^P)$ is the infinitesimal action of the Kosmann lift on the fiber representation.

For spinor fields (where $F$ is the spinor representation of $\text{Spin}(n)$), this reduces to the Kosmann formula. For vector fields (where $F = \mathbb{R}^n$), it reduces to the standard Lie derivative $\mathcal{L}_X Y = [X, Y]$.

This unification shows that there is a \emph{canonical} (metric-independent, connection-independent) Lie derivative on every associated bundle, not just spinors.

### Connection to Penrose Spinor Calculus

Penrose's spinor calculus (1960s) uses abstract spinor indices ($\alpha, \beta, \ldots$) and defines operations like "raising/lowering" via the $\epsilon$-symbol (antisymmetric spinor). The geometric meaning was initially obscure.

Fatibene et al. show that Penrose's raising/lowering operations correspond precisely to the action of $SO(n)$ infinitesimal transformations (elements of $\mathfrak{so}(n)$) on spinors via the reductive Lie derivative. Specifically, the Penrose operator $\tilde{\nabla}$ (used to construct spinor derivatives in curved spacetime) is:
$$\tilde{\nabla}_a \zeta^{\alpha} = \nabla_a \zeta^\alpha + \frac{1}{4} T_a^{bc} \Sigma_{bc}^{\alpha\beta} \zeta_\beta$$

where $\Sigma_{bc}$ are the spin generators, and $T_a^{bc}$ encodes the "spin content" — precisely the spin contribution term from the reductive Lie derivative.

---

## Key Results

1. **Kosmann Lie derivative is connection-independent**: The standard definition for spinor Lie derivatives is purely geometric; different connections give the same result.

2. **Reductive Lie derivative unifies all natural derivatives**: All associated bundles (not just spinors) have a canonical, metric-compatible Lie derivative via the reductive decomposition.

3. **Killing spinors = fully invariant spinors**: A spinor is Killing iff its Lie derivative along every vector field vanishes — a purely geometric characterization.

4. **Penrose spinor calculus is geometric**: Penrose's index operations are manifestations of $\mathfrak{so}(n)$ infinitesimal actions under the reductive Lie derivative.

5. **Variational formulation**: The reductive Lie derivative simplifies variational problems for spinor Lagrangians; the Euler-Lagrange equations take canonical form.

---

## Impact and Legacy

Fatibene-McLenaghan-Sparano's paper became a standard reference for mathematicians and mathematical physicists working on spinor geometry. It is cited extensively in:
- **General relativity** (especially supergravity, where spinor variation is central)
- **Differential geometry** (G-structures, natural bundles, gauge theories)
- **Mathematical physics** (variational formulations of field theories with spinors)

The paper resolved longstanding conceptual questions about spinor derivatives and provided a unified framework that applies to all geometric objects, not just spinors.

---

## Connection to Phonon-Exflation Framework

**Direct application**: The Kosmann-Lichnerowicz Lie derivative is central to the Baptista framework (Papers 17--18).

In the phonon-exflation context:
- The internal manifold is SU(3), which has a natural spin structure (it is a Lie group, hence parallelizable).
- Spinor fields on SU(3) are sections of the spinor bundle associated to the spin structure.
- The Kosmann Lie derivative along the Jensen deformation direction measures how the spinor spectrum evolves under the deformation.
- The Killing spinor condition ($\nabla_\mu \zeta = 0$) selects covariantly constant spinors — these are precisely the modes that couple minimally to the internal geometry.

**Specific computation**: In Baptista Papers 17--18, the Dirac operator $D_K$ on SU(3) is computed using a Kosmann-covariant derivative:
$$D_K = \gamma^\mu \left( \partial_\mu + \frac{1}{4} \omega_\mu^{ab} \gamma_{ab} \right)$$

where $\omega_\mu^{ab}$ is the spin connection (uniquely determined by the metric and the reductive G-structure). This is the Fatibene-Sparano formula applied to the Dirac operator on SU(3).

**Jensen deformation**: When the metric on SU(3) deforms via the Jensen parameter $\tau$, the Kosmann Lie derivative along $\partial_\tau$ gives:
$$\frac{d}{d\tau} \text{Dirac spectrum} = \text{(infinitesimal action of the Kosmann Lie derivative in the } \tau \text{ direction)}$$

This is computed in Sessions 7--8 and used throughout the phonon-exflation analysis.

**Thematic**: Fatibene et al. provide the mathematical foundation for treating spinors on curved, deforming internal manifolds — exactly the scenario in the phonon-exflation framework.

