# Black Hole Entropy is the Noether Charge

**Author(s):** Robert M. Wald
**Year:** 1993
**Journal:** Physical Review D 48, R3427-R3431 (1993)
**arXiv:** gr-qc/9307038
**Relevance:** HIGH

---

## Abstract

We consider a general, classical theory of gravity in $n$ dimensions, arising from a diffeomorphism invariant Lagrangian. In any such theory, to each vector field, $\xi^a$, on spacetime one can associate a local symmetry and, hence, a Noether current $(n-1)$-form, $\mathbf{j}$, and (for solutions to the field equations) a Noether charge $(n-2)$-form, $\mathbf{Q}$, both of which are locally constructed from $\xi^a$ and the fields appearing in the Lagrangian. Assuming only that the theory admits stationary black hole solutions with a bifurcate Killing horizon (with bifurcation surface $\Sigma$), and that the canonical mass and angular momentum of solutions are well defined at infinity, we show that the first law of black hole mechanics always holds for perturbations to nearby stationary black hole solutions. The quantity playing the role of black hole entropy in this formula is simply $2\pi$ times the integral over $\Sigma$ of the Noether charge $(n-2)$-form associated with the horizon Killing field (normalized so as to have unit surface gravity). Furthermore, we show that this black hole entropy always is given by a local geometrical expression on the horizon of the black hole. We thereby obtain a natural candidate for the entropy of a dynamical black hole in a general theory of gravity.

---

## Key Arguments and Derivations

### Framework: Diffeomorphism Invariant Lagrangian

Consider a theory on an $n$-dimensional manifold $M$ with dynamical fields $\phi$ (including the metric $g_{ab}$) and Lagrangian $n$-form $\mathbf{L}$. Under a first-order variation:

$$\delta\mathbf{L} = \mathbf{E}\delta\phi + d\boldsymbol{\Theta}$$

where $\mathbf{E} = 0$ are the equations of motion and $\boldsymbol{\Theta}$ is the symplectic potential $(n-1)$-form. The symplectic current is:

$$\boldsymbol{\Omega}(\phi, \delta_1\phi, \delta_2\phi) = \delta_1[\boldsymbol{\Theta}(\phi, \delta_2\phi)] - \delta_2[\boldsymbol{\Theta}(\phi, \delta_1\phi)]$$

### Noether Current and Charge

For any vector field $\xi^a$ on $M$, diffeomorphism invariance ($\hat{\delta}\mathbf{L} = \mathcal{L}_\xi\mathbf{L} = d(\xi \cdot \mathbf{L})$) implies a Noether current:

$$\mathbf{j} = \boldsymbol{\Theta}(\phi, \mathcal{L}_\xi\phi) - \xi \cdot \mathbf{L}$$

On solutions ($\mathbf{E} = 0$), $\mathbf{j}$ is closed: $d\mathbf{j} = 0$, so there exists a Noether charge $(n-2)$-form $\mathbf{Q}$ with $\mathbf{j} = d\mathbf{Q}$.

### Canonical Energy and Angular Momentum

For an asymptotically flat spacetime with time translation $t^a$ and rotation $\varphi^a$:

$$\delta E = \int_\infty (\delta\mathbf{Q}[t] - t \cdot \boldsymbol{\Theta})$$
$$\delta J = -\int_\infty \delta\mathbf{Q}[\varphi]$$

### The First Law

For a stationary black hole with bifurcation surface $\Sigma$, the Killing field $\xi^a = t^a + \Omega_H^{(\mu)} \varphi^a_{(\mu)}$ vanishes on $\Sigma$. The fundamental identity yields:

$$\delta\int_\Sigma \mathbf{Q} = \delta E - \Omega_H^{(\mu)}\delta J_{(\mu)}$$

For perturbations to nearby stationary black holes, $\delta\mathbf{Q} = \kappa \delta\tilde{\mathbf{Q}}$ on $\Sigma$ (where $\tilde{\mathbf{Q}}$ is the Noether charge of the unit-surface-gravity Killing field). This gives the first law:

$$\frac{\kappa}{2\pi}\delta S = \delta E - \Omega_H^{(\mu)}\delta J_{(\mu)}$$

### Black Hole Entropy as Noether Charge

The entropy is:

$$S = 2\pi\int_\Sigma \tilde{\mathbf{Q}}$$

where $\tilde{\mathbf{Q}}$ is constructed by: (1) expressing $\mathbf{Q}$ in terms of $\xi^a$ and $\nabla_a\xi_b$, (2) setting $\xi^a = 0$ on $\Sigma$, and (3) replacing $\nabla_a\xi_b$ by the binormal $\epsilon_{ab}$.

For general relativity, this recovers $S = A/4G$ (Bekenstein-Hawking). For higher-derivative theories, it gives the Wald entropy formula.

### Euclidean Equivalence

The Euclidean action $I$ satisfies:

$$\frac{\kappa}{2\pi}I = E - \Omega_H^{(\mu)}J_{(\mu)} - \int_\Sigma \mathbf{Q}$$

so that the Euclidean procedure gives the same entropy: $S = 2\pi\int_\Sigma \mathbf{Q}$.

---

## Key Results

1. In **any** diffeomorphism-invariant theory of gravity, the first law of black hole mechanics holds with entropy given by $S = 2\pi\int_\Sigma \tilde{\mathbf{Q}}$ -- the Noether charge of the horizon Killing field.
2. The entropy is always a **local geometrical expression** on the horizon.
3. For general relativity: $S = A/(4G)$. For Lovelock gravity, $f(R)$ theories, etc.: the Wald formula gives the correct generalization.
4. The second law of black hole mechanics is related to positivity of total Noether flux through the horizon.
5. The Euclidean approach and the Noether charge approach give identical results.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Lagrangian variation | $\delta\mathbf{L} = \mathbf{E}\delta\phi + d\boldsymbol{\Theta}$ | Eq. (3) |
| Symplectic current | $\boldsymbol{\Omega} = \delta_1\boldsymbol{\Theta}_2 - \delta_2\boldsymbol{\Theta}_1$ | Eq. (4) |
| Noether current | $\mathbf{j} = \boldsymbol{\Theta}(\phi,\mathcal{L}_\xi\phi) - \xi\cdot\mathbf{L}$ | Eq. (7) |
| On-shell closure | $d\mathbf{j} = -\mathbf{E}\mathcal{L}_\xi\phi$; $\mathbf{j} = d\mathbf{Q}$ on solutions | Eqs. (8-9) |
| Surface gravity | $\xi^a\nabla_a\xi^b = \kappa\xi^b$ | Eq. (1) |
| Horizon Killing field | $\xi^a = t^a + \Omega_H^{(\mu)}\varphi^a_{(\mu)}$ | Eq. (21) |
| First law | $\frac{\kappa}{2\pi}\delta S = \delta E - \Omega_H^{(\mu)}\delta J_{(\mu)}$ | Eq. (25) |
| Wald entropy | $S = 2\pi\int_\Sigma \tilde{\mathbf{Q}}$ | Eq. (26) |
| Canonical energy | $\delta E = \int_\infty(\delta\mathbf{Q}[t] - t\cdot\boldsymbol{\Theta})$ | Eq. (16) |
| Canonical angular momentum | $\delta J = -\int_\infty \delta\mathbf{Q}[\varphi]$ | Eq. (17) |
| Euclidean action identity | $\frac{\kappa}{2\pi}I = E - \Omega_H J - \int_\Sigma\mathbf{Q}$ | Eq. (31) |

## Relevance to Phonon-Exflation

Wald's result that black hole entropy is a Noether charge -- a local geometrical quantity determined by the Lagrangian -- provides the gravitational counterpart to the spectral action = entropy identity (Paper 20). In the phonon-exflation framework, the spectral action $\text{Tr}(f(D^2/\Lambda^2))$ plays the role of both the action AND the entropy (by CCS's theorem). Wald's result shows this is expected: for any diffeomorphism-invariant Lagrangian, the entropy IS a derived quantity from the action. The framework's spectral action is such a Lagrangian, and its "entropy" in Wald's sense is the Noether charge of the Dirac operator -- precisely what CCS compute from second quantization.
