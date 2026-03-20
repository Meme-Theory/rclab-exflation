# On the Stability of Homogeneous Einstein Manifolds

**Author(s):** Jorge Lauret
**Year:** 2021
**Journal:** Asian Journal of Mathematics (accepted 2022)
**arXiv:** 2105.06336

---

## Abstract

Let $g$ be a $G$-invariant Einstein metric on a compact homogeneous space $M = G/K$. This work develops a formula for the Lichnerowicz Laplacian of $g$ restricted to $G$-invariant transverse-traceless (TT) tensors, enabling systematic study of stability properties as a critical point of the scalar curvature functional. Special attention is given to naturally reductive metrics.

---

## Historical Context

Einstein metrics on homogeneous spaces occupy a central place in differential geometry and physics. These metrics generalize the round metric on spheres and symmetric spaces, representing geometric configurations with extremal scalar curvature under constraint. Understanding their stability — whether they minimize, maximize, or saddle-point the scalar curvature — has profound implications for both cosmology and the geometry of moduli spaces.

Lauret's contribution modernizes the stability analysis of Einstein metrics on homogeneous spaces via the Lichnerowicz Laplacian, a fundamental tool originating in general relativity (perturbations of Einstein metrics) and now central to geometric analysis. Prior work on Einstein stability relied on ad-hoc calculations for specific manifold families. This paper provides a **universal algorithmic framework**: for any homogeneous space $G/K$, one can compute stability via Casimir operators and representation theory, bypassing case-by-case analysis.

The Lichnerowicz Laplacian acting on symmetric 2-tensors encodes linearized Einstein equations and is defined as:
$$\Delta_L h_{\mu\nu} = \Delta h_{\mu\nu} + 2\,\text{Ric}(h_{\mu\nu}) - g^{\rho\sigma} R_{\rho\mu\sigma\nu} h_{\rho\sigma},$$
where $\Delta$ is the Laplace-Beltrami operator. On TT-tensors ($\text{tr}(h)=0, \nabla^\mu h_{\mu\nu}=0$), this reduces to a pure algebraic/spectral computation.

---

## Key Arguments and Derivations

### The Lichnerowicz Laplacian on Homogeneous Spaces

For a homogeneous space $M = G/K$ with $G$-invariant metric $g$, the tangent space at the identity coset decomposes into the isotropy Lie algebra $\mathfrak{k}$ and its orthogonal complement $\mathfrak{p}$:
$$\mathfrak{g} = \mathfrak{k} \oplus \mathfrak{p}.$$

The metric $g$ restricts to $\mathfrak{p}$. Symmetric 2-tensors on $M$ correspond to $G$-equivariant mappings $h: \mathfrak{g} \times \mathfrak{g} \to \mathbb{R}$ satisfying:
$$h([X,Y], Z) = 0 \quad \text{for all } X,Y \in \mathfrak{g}, Z \in \mathfrak{p}.$$

For TT-tensors, further constraints apply:
- Traceless: $g^{\mu\nu} h_{\mu\nu} = 0$
- Divergence-free: $\nabla^\mu h_{\mu\nu} = 0$

On homogeneous spaces, these become **purely algebraic conditions** via the Peter-Weyl decomposition. The Lichnerowicz Laplacian restricted to $G$-invariant TT-tensors becomes:
$$\Delta_L|_{\text{TT}} = \Delta + 2\,\text{Ric} - R_{\text{component}}.$$

Lauret's key formula expresses all terms via Casimir operators of $G$ restricted to $\mathfrak{p}$-representations:
$$\lambda_L = C_G - 2C_K + \text{geometric constants from } g.$$

Here $C_G$ and $C_K$ are Casimir eigenvalues in representation-theoretic bases.

### Einstein Condition as Constraint

Einstein metrics satisfy:
$$\text{Ric}(g) = \lambda g \quad \text{(normalized so } \lambda = \frac{n-1}{2V}\text{)}$$
where $n = \dim(M)$ and $V$ is the scalar curvature.

On homogeneous spaces, this becomes an **algebraic eigenvalue problem** in the adjoint representation. For $G/K$ to admit an Einstein metric requires a specific balance: the Killing form restricted to $\mathfrak{p}$ must yield positive scalar curvature eigenvalues across all $\mathfrak{p}$-irreducibles.

The scalar curvature functional $S(g) = \int_M V \,dV_g$ has critical points precisely at Einstein metrics. Stability of a critical point is determined by the second variation:
$$\delta^2 S|_{\text{Einstein}} = \int_M \langle h, \Delta_L h \rangle \, dV.$$

If $\Delta_L$ has non-negative spectrum on TT-tensors, the Einstein metric is **stable** (a local minimum); negative eigenvalues signal instability (saddle/maximum).

### Naturally Reductive Metrics

A homogeneous space $G/K$ is naturally reductive if the isotropy representation $K \to GL(\mathfrak{p})$ admits an $\text{Ad}(K)$-invariant complement. For such spaces, the Einstein condition simplifies dramatically: any $G$-invariant metric is a critical point of the scalar curvature functional restricted to $G$-invariant metrics.

For naturally reductive spaces, Lauret derives:
$$\lambda_L(\text{TT}) = C_\mathfrak{p}^{(G)} - 2C_\mathfrak{k}^{(G)} + \text{(metric-dependent lower-order terms)}.$$

This formula is **fully computable** given the structure constants of $\mathfrak{g}/\mathfrak{k}$.

---

## Key Results

1. **Universal Lichnerowicz Formula**: For any compact homogeneous Einstein space $G/K$, the Lichnerowicz Laplacian spectrum on $G$-invariant TT-tensors is computable via Casimir operators and the Peter-Weyl decomposition. No explicit metric computation required.

2. **Stability Criterion**: An Einstein metric $g$ on $G/K$ is stable (in the Einstein-Hilbert sense) if and only if $\min(\text{spec}(\Delta_L|_{\text{TT}})) \geq 0$.

3. **Naturally Reductive Subfamily**: On naturally reductive spaces, the stability spectrum depends only on $\mathfrak{g}, \mathfrak{k}$ and the metric scale, not on geometric details of the curvature tensor.

4. **Computation Algorithm**: Stability analysis reduces to finite-dimensional linear algebra in representation theory: decompose TT-tensors under $\mathfrak{p}$-irreducibles, apply Casimir operators, extract eigenvalues.

5. **Examples**: Detailed calculations for Wallach spaces, flag manifolds, and symmetric spaces demonstrate the method's applicability.

---

## Impact and Legacy

This paper has become the **foundational reference** for algorithmic stability analysis of Einstein metrics on homogeneous spaces. Its Lichnerowicz formula enables researchers to:
- Classify Einstein metrics on any given homogeneous space by stability type
- Search for new stable (or unstable) examples systematically
- Understand how perturbations to Einstein metrics propagate (key for cosmology and topology)

Subsequent work (Schwahn 2023, Duboeuf-Malek-Samtleben 2023) builds directly on Lauret's Casimir-based framework, extending it to new examples and holographic settings. The formula has proven essential for studying deformations of Einstein metrics — exactly what is needed when a homogeneous space undergoes a parameter-dependent geometric transition.

---

## Connection to Phonon-Exflation Framework

**CRITICAL APPLICATION**: The M4 x SU(3) metric deforms under the Jensen parameter $\tau \in [0, 0.285]$. At $\tau=0$ (round metric), SU(3) admits the standard Einstein metric. As $\tau$ increases, the geometry becomes the **non-standard Einstein metric** solved in Baptista papers #13-18.

Lauret's formula directly computes the Lichnerowicz spectrum on SU(3) for **both the round and the deformed Einstein metrics**:
- At $\tau=0$: $\lambda_L(\text{round}) \geq 0$ (known stable)
- At $\tau > 0$: $\lambda_L(\text{deformed}) = ?$ (THE #1 DECISIVE GATE)

The stability margin $\lambda_L - 3m^2$ (where $m = \text{mass of lightest field}$) determines whether:
- $\lambda_L > 3m^2$ → tensor perturbations stable (phonon-exflation viable)
- $\lambda_L < 3m^2$ → tensor modes become tachyonic (geometric instability, mechanism breaks)

**DIRECT COMPUTATION ROADMAP**:
1. Extract $\mathfrak{g}, \mathfrak{k}$ for SU(3) (done, Session 20)
2. Use Lauret's Casimir formula to compute eigenvalues of $\Delta_L$ on TT-tensors
3. Compare to $3m^2$ from Dirac spectrum (known: $m^2 \sim 0.001-0.01$ in natural units)
4. Verdict: Gate PASS or FAIL

This is the singular uncomputed step blocking full validation of the framework's geometric stability. Paper 37 provides the **exact algorithm** to execute it.
