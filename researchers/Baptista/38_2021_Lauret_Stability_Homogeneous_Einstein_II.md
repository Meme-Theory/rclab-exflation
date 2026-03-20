# On the Stability of Homogeneous Einstein Manifolds II

**Author(s):** Jorge Lauret
**Year:** 2021
**Journal:** Journal of the London Mathematical Society (accepted June 2022)
**arXiv:** 2107.00354

---

## Abstract

This companion develops a formula for the Lichnerowicz Laplacian on $G$-invariant symmetric 2-tensors for compact homogeneous spaces $M = G/K$. The $G$-invariant spectrum is computed explicitly for Einstein metrics on generalized Wallach spaces and flag manifolds with $b_2(M) = 1$, permitting complete determination of $G$-stability and critical point type for each metric.

---

## Historical Context

Paper I established the **algorithmic framework** for computing Lichnerowicz stability via Casimir operators. Paper II executes that program on concrete families of homogeneous spaces, with particular focus on Einstein metrics that are **not** symmetric spaces — i.e., metrics arising from non-trivial deformations of symmetric structure.

The classical Einstein equations $\text{Ric}(g) = \lambda g$ admit multiple solutions even on fixed topological space $M$. For symmetric spaces (where $K = K_s$ is the stabilizer of a geodesic symmetric point), Einstein metrics are unique (up to scaling). But for non-symmetric homogeneous spaces, **multiple Einstein metrics can coexist**.

This raises a profound question: among several Einstein metrics on the same $G/K$, which are stable? Which are saddle points? The answer encodes information about the moduli space of Einstein metrics and has implications for:

1. **Geometric flows** (Kahler-Ricci flow, Ricci flow) — do they converge to stable Einstein metrics?
2. **Cosmological dynamics** — what happens if universe starts at an unstable Einstein critical point?
3. **String theory vacua** — moduli stabilization via Einstein condition

Paper II applies the Lauret formula to resolve these questions for two important families: generalized Wallach spaces and flag manifolds.

---

## Key Arguments and Derivations

### Generalized Wallach Spaces

A generalized Wallach space is a homogeneous space of the form:
$$M = \frac{SU(n)}{SU(n-2) \times U(1)^2}$$
or similar quotients by products of lower-rank groups. These spaces admit **multiple Einstein metrics**, parametrized by choice of metric on $\mathfrak{p}$.

For the Einstein condition to hold:
$$\text{Ric}(g) = \lambda g \quad \text{on } \mathfrak{p},$$
one must solve a system of polynomial equations in the metric coefficients. Typically, multiple solutions exist.

The Lichnerowicz Laplacian on Wallach spaces decomposes under $G$-invariant TT-tensors into irreducible blocks:
$$\Delta_L|_{\text{TT}} = \bigoplus_{\rho \in \hat{\mathfrak{p}}} \lambda_\rho(g) \, P_\rho,$$
where $\rho$ labels $\mathfrak{p}$-irreducibles and $\lambda_\rho(g)$ is the Casimir eigenvalue in representation $\rho$.

For Einstein metrics on Wallach spaces, Lauret proves:
$$\lambda_\rho = C_G(\rho) - 2C_K(\rho) + \text{(Einstein-specific correction)}.$$

The Einstein-specific correction arises because $\text{Ric}(g) = \lambda g$ imposes constraints: not all $\mathfrak{p}$-irreducibles admit free fluctuations; some are "locked" by the Einstein condition.

### Flag Manifolds with $b_2(M) = 1$

Flag manifolds are homogeneous spaces parametrizing nested chains of subspaces:
$$V_0 \subset V_1 \subset \cdots \subset V_k = \mathbb{C}^n.$$

The simplest case is $\text{Flag}(1,2;\mathbb{C}^3)$ (flags in $\mathbb{C}^3$ with one 1-D and one 2-D subspace), which is isomorphic to $\frac{SU(3)}{U(1) \times U(1)}$.

Flag manifolds with $b_2(M) = 1$ (one complex deformation modulus) are particularly tractable: they admit exactly one or two Einstein metrics, depending on the flag structure.

For such spaces, the second Betti number constraint $b_2 = 1$ implies that the moduli space of Kahler-Einstein metrics is 1-dimensional. This constrains the Lichnerowicz spectrum: many eigenvalues are determined by the geometry alone, independent of the specific Einstein metric chosen.

Lauret's computation for flags with $b_2 = 1$:

1. Decompose TT-tensors into $(1,1)$-forms (deformations of Kahler class) and $(1,1)$-traceless parts
2. On $(1,1)$-forms: Lichnerowicz eigenvalues match the Kahler-Ricci flow operator
3. On $(1,1)$-traceless: compute via Casimir formula restricted to primitive forms

**Result**: For each flag with $b_2 = 1$, the Lichnerowicz spectrum is **explicitly computable** and either (i) strictly positive (stable), (ii) zero eigenvalue (marginal), or (iii) negative (unstable).

### The Role of the Scalar Curvature Functional

For a fixed homogeneous space $G/K$, the scalar curvature functional $S(g) = \int V_g \, dV_g$ is a $G$-invariant function on the space of $G$-invariant metrics. Einstein metrics are critical points:
$$\delta S|_g = 0 \Leftrightarrow \text{Ric}(g) = \lambda g.$$

The Hessian at an Einstein critical point is precisely the Lichnerowicz Laplacian:
$$\delta^2 S|_g[h, h] = \int_M \langle h, \Delta_L h \rangle \, dV.$$

Stability type classification:
- **Local minimum** ($\Delta_L \geq 0$): $S$ increases in all perturbation directions → metric is stable
- **Saddle** (mixed spectrum): $S$ increases in some directions, decreases in others
- **Local maximum** ($\Delta_L \leq 0$): $S$ decreases in all directions → metric is unstable

For Einstein metrics on Wallach spaces, Lauret finds a **three-way split**:
- Type A: stable (all eigenvalues $> 0$)
- Type B: saddle with 1-2 negative eigenvalues
- Type C: unstable (many negative eigenvalues)

---

## Key Results

1. **Lichnerowicz Spectrum for Wallach Spaces**: For generalized Wallach spaces $SU(n)/SU(n-2) \times U(1)^2$, the spectrum is completely determined by the Einstein metric choice and the Casimir formula. Explicit tables provided.

2. **Stability Classification of Wallach Einstein Metrics**: Among the known Einstein metrics on standard Wallach spaces, stable, saddle-point, and unstable examples are identified and catalogued by critical point type.

3. **Flag Manifold Stability**: For flag manifolds with $b_2 = 1$, the Lichnerowicz Laplacian decouples into $(1,1)$-forms (Kahler-Ricci flow) and primitive $(1,1)$-tensors (Casimir-determined). Stability is computable in closed form.

4. **Kahler-Einstein Metrics**: For Kahler flag manifolds, stability of Einstein metrics correlates with the geometry of the scalar curvature form $\rho = \text{Ric}(g)$. Positive scalar curvature $\Rightarrow$ typically stable.

5. **Moduli Space Structure**: The critical point structure (stable vs. saddle) encodes information about the topology of the moduli space of Einstein metrics on $G/K$. Multiple Einstein metrics on the same space need not have the same stability type.

6. **Algorithm Verification**: The Casimir formula from Paper I is verified on all computed examples: no discrepancies, supporting its universal validity.

---

## Impact and Legacy

Paper II catalyzed a systematic search for new Einstein metrics, especially examples with exotic stability properties (saddle points, maxima). Combined with Paper I, it enabled:

- **Complete classification** of Einstein metrics on flag manifolds up to dimension 8
- **Moduli space topology** — understanding how Einstein metrics bifurcate under parameter changes
- **Geometric flow dynamics** — predicting convergence or blow-up in Ricci/Kahler-Ricci flows
- **Holographic applications** — relating Einstein metric stability to RG flow stability in AdS/CFT

The work is now standard reference for any project involving Einstein deformations, parameter-dependent geometries, or metric moduli.

---

## Connection to Phonon-Exflation Framework

**CRITICAL APPLICATION**: The Jensen deformation parameter $\tau$ sweeps through a 1-parameter family of Einstein metrics on SU(3):
$$g_\tau = \text{(round metric at } \tau=0\text{)} \to \text{(deformed Einstein at } \tau \in (0, 0.285]).$$

As $\tau$ increases, the metric leaves the symmetric space $SU(3) = SU(3)/\{\text{id}\}$ and becomes a **non-symmetric homogeneous space** $SU(3)/K_\tau$ where $K_\tau$ depends on the deformation structure.

Paper II directly addresses: **What happens to Einstein stability as we deform away from the round metric?**

The two key computations needed:

1. **At the fold** ($\tau \to 0.285$): Is $\Delta_L$ positive-definite (stable), or do negative eigenvalues emerge (instability)?
   - If stable: the deformation is a smooth family of Einstein metrics, phonon-exflation can proceed
   - If unstable: the geometry becomes a **saddle point** of the scalar curvature functional, triggering instability

2. **Along the path** ($\tau \in (0, 0.285)$): Does the stability type change? (e.g., stable at $\tau=0$, saddle at $\tau=0.15$, unstable at $\tau=0.285$?)
   - Smooth transition: metric perturbations remain under control
   - Discontinuity in eigenvalue sign: signals a phase transition in the geometry itself

**ROADMAP FOR GATE DECISION**:
- Use Lauret Paper II's algorithm on the Jensen deformation family
- Compute Lichnerowicz spectrum at 10-15 values of $\tau$ spanning $[0, 0.285]$
- Check if $\min(\text{spec}(\Delta_L)) \geq 0$ throughout
- Compare minimum eigenvalue to $3m^2$ (lightest Dirac mode)
- Verdict: Gate LICHNEROWICZ-STAB-BX PASS or FAIL

Paper II provides the **exact method** for this tau-sweep stability analysis, taking the framework from "theoretically possible" to "computationally resolved."
