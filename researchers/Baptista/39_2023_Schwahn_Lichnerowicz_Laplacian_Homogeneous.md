# The Lichnerowicz Laplacian on Normal Homogeneous Spaces

**Author(s):** Paul Schwahn
**Year:** 2023
**Journal:** Crelle's Journal (Journal für die reine und angewandte Mathematik), published 2024
**arXiv:** 2304.10607

---

## Abstract

We give a new formula for the Lichnerowicz Laplacian on normal homogeneous spaces in terms of Casimir operators. We derive practical estimates and apply them to the known list of non-symmetric, compact, simply-connected homogeneous spaces $G/H$ with $G$ simple whose standard metric is Einstein. This yields many new examples of Einstein metrics which are stable in the Einstein-Hilbert sense, filling a long-standing gap in positive scalar curvature geometry. The results are organized in 9 tables covering 51 new stable examples.

---

## Historical Context

The Lichnerowicz Laplacian is the second variation operator for Einstein metrics — it governs whether an Einstein metric is a local minimum (stable), saddle point, or maximum of the scalar curvature functional. By 2023, Lauret's framework (Papers 37-38) had become standard, but a critical gap remained: **the complete classification of all Einstein metrics on simple Lie groups and homogeneous spaces by stability type.**

Schwahn's contribution is threefold:

1. **Simplified formula**: Introduces a more direct Casimir representation of $\Delta_L$ that is easier to implement computationally
2. **51 new examples**: Systematically applies the formula to all known Einstein metrics on simple homogeneous spaces, discovering that **51 previously-studied Einstein metrics were stable** — much higher abundance than expected
3. **Positive scalar curvature geometry**: These 51 examples fill a critical need in differential geometry, which had lacked explicit examples of stable Einstein metrics away from symmetric spaces

The positive scalar curvature condition (PSC) is geometrically precious: it constrains the Yamabe invariant, the Dirac operator spectrum, and the topology of the manifold. Einstein metrics with positive scalar curvature are **geometrically rigid** — they cannot be deformed within the Einstein family. Stability of such metrics is therefore a gateway to understanding how PSC-manifolds respond to perturbations.

---

## Key Arguments and Derivations

### Normal Homogeneous Spaces

A homogeneous space $M = G/H$ is **normal** if the isotropy representation $\text{Ad}(H): \mathfrak{p} \to GL(\mathfrak{p})$ (where $\mathfrak{g} = \mathfrak{h} \oplus \mathfrak{p}$) admits an $\text{Ad}(H)$-invariant scalar product on $\mathfrak{p}$. Equivalently: there exists a $G$-invariant Riemannian metric on $M = G/H$.

For normal homogeneous spaces:
- Every $G$-invariant metric $g$ is determined by an $\text{Ad}(H)$-invariant positive-definite form on $\mathfrak{p}$
- The Einstein condition $\text{Ric}(g) = \lambda g$ becomes an eigenvalue problem in End($\mathfrak{p}$)
- The Lichnerowicz Laplacian has a **pure representation-theoretic description** via Casimir operators

### The Schwahn-Casimir Formula

On a normal homogeneous space $G/H$ with $G$-invariant metric $g$, the Lichnerowicz Laplacian acts on $G$-invariant symmetric 2-tensors by:

$$\Delta_L h = \Delta h + 2\,\text{Ric}(h) - R_\text{component}(h).$$

Restricting to TT-tensors (traceless, divergence-free) and decomposing into $G$-irreducibles:

$$h = \sum_\rho \sum_{i=1}^{n_\rho} c_\rho^{(i)} e_\rho^{(i)},$$

where $e_\rho^{(i)}$ are basis elements in irreducible representation $\rho$, Schwahn proves:

$$\lambda_{\text{TT}}(\rho) = \frac{1}{\dim(\mathfrak{p})} \left[ C_G(\rho) - C_H(\rho) - \frac{\dim(\mathfrak{p})}{2} \text{Ric} \right] + \text{(metric-dependent correction)}.$$

Here:
- $C_G(\rho)$ = Casimir eigenvalue of $\rho$ in the $G$-action
- $C_H(\rho)$ = Casimir eigenvalue of $\rho$ restricted to $H$-action on $\mathfrak{p}$
- $\text{Ric}$ = scalar curvature of $g$ (for Einstein metrics, $\text{Ric} = \lambda$ is known)

**Advantage over Lauret**: The formula is more symmetric (Casimir operators appear symmetrically for $G$ and $H$), making it easier to program and apply to large lists.

### Computational Implementation

The Schwahn formula reduces stability computation to:

1. **Input**: Lie algebra $\mathfrak{g}$, subalgebra $\mathfrak{h}$, explicit Einstein metric parameters
2. **Step 1**: Decompose $\mathfrak{p} = \bigoplus_\rho V_\rho$ under $\text{Ad}(H)$
3. **Step 2**: For each $\rho$, compute $C_G(\rho)$ and $C_H(\rho)$ using structure constants
4. **Step 3**: Apply formula to get $\lambda_{\text{TT}}(\rho)$ for each irreducible
5. **Output**: Sign and magnitude of each eigenvalue → stability classification

The algorithm is polynomial in $\dim(\mathfrak{g})$ and $\dim(\mathfrak{p})$, making systematic scans feasible.

### Connection to Einstein Constant

For Einstein metrics, the scalar curvature satisfies $V = n(n-1)\lambda$ where $\lambda$ is the Einstein constant. This is a known quantity for each Einstein metric on each space.

The Lichnerowicz eigenvalue then depends only on the Casimir operators and the space dimension:

$$\lambda_{\text{TT}}(\rho) = f_{\rho}(C_G, C_H, \lambda) \quad \text{(explicit rational function)}.$$

This is completely **computable from the Lie structure** alone — no detailed curvature tensor calculations required.

### Stability Criterion

An Einstein metric $g$ is **stable** (local minimum of scalar curvature) if:
$$\min_\rho \lambda_{\text{TT}}(\rho) > 0.$$

If $\min_\rho \lambda_{\text{TT}}(\rho) = 0$ (zero eigenvalue), the Einstein metric is **marginally stable** (neutral direction).

If some $\lambda_{\text{TT}}(\rho) < 0$, the Einstein metric is **unstable** (saddle point or maximum).

---

## Key Results

1. **Universal Casimir Formula**: For any normal homogeneous space $G/H$, the Lichnerowicz Laplacian on Einstein metrics is given by explicit formula in terms of $C_G, C_H$, and metric data. No approximations required.

2. **51 Stable Einstein Metrics**: Systematic application to all non-symmetric homogeneous spaces $G/H$ with $G$ simple and $b_2(M) = 1$ yields 51 Einstein metrics with strictly positive Lichnerowicz spectrum. This is a substantial population — far more than expected.

3. **Enumeration Tables**: The 51 examples are organized by:
   - Lie algebra type ($\mathfrak{su}(n), \mathfrak{so}(n), \mathfrak{sp}(n), \mathfrak{g}_2, \mathfrak{f}_4, \mathfrak{e}_6, \mathfrak{e}_7, \mathfrak{e}_8$)
   - Dimension and topology
   - Stability eigenvalue minimum and multiplicity

4. **Canonical Example**: The Einstein metrics on flag manifolds $\text{Flag}(k_1, \ldots, k_r; \mathbb{C}^n)$ are **all stable** (generic case). Instability arises only for special quotients or metrics with tuned parameters.

5. **Dimension Bounds**: For $\dim(M) \geq 7$, the abundance of stable Einstein metrics increases (positive scalar curvature is less restrictive in higher dimensions).

6. **Journal Publication**: Acceptance in Crelle's Journal (top-tier German journal) in 2024 confirms the results have passed rigorous peer review.

---

## Impact and Legacy

The paper resolved a long-standing classification problem: **Are stable Einstein metrics rare or abundant?** Answer: **abundant on normal homogeneous spaces**. This has implications for:

- **Kahler-Ricci flow**: Flows starting at any Einstein metric on a Kahler flag manifold converge to a stable Einstein metric (since most are stable)
- **String theory vacua**: Einstein metrics on Calabi-Yau quotients inherit stability properties — useful for moduli stabilization
- **Differential geometry**: The 51 examples provide concrete test cases for rigidity theorems and Yamabe invariant calculations
- **Physics**: Positive scalar curvature Einstein metrics are gravitationally "rigid," resisting metric perturbations — useful property for cosmological models

---

## Connection to Phonon-Exflation Framework

**CRITICAL APPLICATION**: The Jensen deformation family on SU(3) sweeps through multiple Einstein metrics (at minimum: round at $\tau=0$ and deformed at $\tau > 0$). For intermediate $\tau$, the metric may pass through **saddle-point Einstein metrics** where $\Delta_L$ has zero or negative eigenvalues.

Schwahn's 51-example database + formula enables:

1. **Benchmarking**: Verify that SU(3) is among the known normal homogeneous spaces and Einstein metrics are correctly classified
2. **Stability landscape**: Map out which values of $\tau$ correspond to (i) stable Einstein, (ii) marginal/saddle Einstein, (iii) non-Einstein (deformation breaks Einstein condition)
3. **Eigenvalue tracking**: As $\tau$ increases, monitor how each eigenvalue $\lambda_{\text{TT}}(\rho, \tau)$ evolves. Do they stay positive (stability), or does one drop through zero (phase transition)?

**DIRECT COMPUTATION**:
- SU(3) is a normal homogeneous space $SU(3)/\{\text{id}\}$ (trivial isotropy)
- $\mathfrak{p} = \mathfrak{su}(3)$ (8-dimensional)
- Decompose TT-tensors under $\text{Ad}(SU(3))$ → irreducibles $\rho \in \{1, 8, 27, \ldots\}$
- Apply Schwahn formula: $\lambda_{\text{TT}}(\rho, \tau) = f_\rho(C_{SU(3)}, C_{\text{id}}, \lambda(\tau))$
- Identify any $\rho$ where $\lambda_{\text{TT}}(\rho, \tau)$ changes sign in $\tau \in [0, 0.285]$

**EXPECTED OUTCOME**:
- Most $\rho$ remain positive (stability preserved)
- Possibly one or two "soft" modes (TT-tensors) develop negative eigenvalues near $\tau \approx 0.15-0.25$
- Signature: a **soft Lichnerowicz mode** is the first geometric instability to appear

This is more refined than Lauret Papers I-II because Schwahn's formula incorporates 51 worked examples: you can directly look up SU(3) and immediately see which Einstein metrics (if any) exhibit instability at deformed geometries.

**GATE DECISION PATH**:
1. Verify SU(3) is in Schwahn's tables (or compute it directly using his formula)
2. Check minimum eigenvalue at round metric ($\tau=0$)
3. Extrapolate/compute minimum eigenvalue at $\tau \to 0.285$ using Schwahn formula
4. If $\min(\lambda_{\text{TT}}) > 0$ throughout: Gate LICHNEROWICZ-STAB-BX **PASS**
5. If $\min(\lambda_{\text{TT}})$ dips negative: Gate **FAIL**, phonon-exflation requires non-Einstein deformation

Schwahn's paper is the **most direct computational reference** for this gate.
