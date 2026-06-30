# An Accelerating Universe from Dynamical Compactification

**Author(s):** F. Darabi
**Year:** 2003
**Journal:** arXiv preprint gr-qc/0301075
**arXiv:** gr-qc/0301075
**Relevance:** HIGH

---

## Abstract

We study a (4+D)-dimensional Kaluza-Klein cosmology with a Robertson-Walker type metric having two scale factors $a$ and $R$, corresponding to D-dimensional internal space and 4-dimensional universe, respectively. By introducing an exotic matter as the space-time part of the higher dimensional energy-momentum tensor, a 4-dimensional decaying cosmological term is appeared as $\Lambda \sim R^{-2}$, playing the role of an evolving dark energy in the universe. The resulting field equations yield the exponential solutions for the scale factors. These exponential behaviors may account for the dynamical compactification of extra dimensions and the accelerating expansion of the 4-dimensional universe in terms of the Hubble parameter. The acceleration of universe may be explained by the negative pressure of the exotic matter. It is shown that the rate of compactification of higher dimensions depends on the dimension, $D$. We then obtain the Wheeler-DeWitt equation and find the general exact solutions in D-dimensions. A good correspondence between the classical solutions and the Wheeler-DeWitt solutions, in any dimension $D$, is obtained.

---

## Key Arguments and Derivations

### The Model (Sec. 2)

The (4+D)-dimensional metric with Robertson-Walker type internal space:
$$ds^2 = -N^2(t)dt^2 + R^2(t)\frac{dr_i dr^i}{(1+kr^2/4)^2} + a^2(t)\frac{d\rho_a d\rho^a}{(1+k'\rho^2)}$$

where $R(t)$ is the 4D scale factor, $a(t)$ is the internal space radius, $N(t)$ is the lapse function, and $k' = 0$ (flat compact internal space with topology $S^D$).

The energy-momentum tensor has vanishing pressure along extra dimensions ($p_D = 0$, brane-world motivated: matter confined to 4D). The 4D exotic matter has equation of state:
$$p_\chi = \left(\frac{m}{3} - 1\right)\rho_\chi, \quad 0 \leq m \leq 2$$
which gives negative pressure (violating the strong energy condition, required for acceleration).

### Decaying Cosmological Term (Secs. 2-3)

The continuity equation with this equation of state gives $\rho_\chi(R) = \rho_\chi(R_0)(R_0/R)^m$. Identifying $\Lambda \equiv \rho_\chi(R)$ yields a decaying cosmological term:
$$\Lambda(R) = \Lambda(R_0)\left(\frac{R_0}{R}\right)^m$$

For $m = 2$: $\Lambda(R) = 3/R^2$ (with $\Lambda(R_0)R_0^2 = 3$).

### Einstein Equations and Solutions (Secs. 3-4)

With the gauge $N(t) = R^3(t)a^D(t)$ and $m = 2$, the Lagrangian simplifies to:
$$L = \frac{1}{2}\dot{X}^2 + \frac{D(D-1)}{12}\dot{Y}^2 + \frac{D}{2}\dot{X}\dot{Y}$$
where $X = \ln R$, $Y = \ln a$.

The equations of motion give $\ddot{X} = 0$ and $\ddot{Y} = 0$, yielding exponential solutions:
$$R(t) = l_p e^{Ht}, \quad a(t) = l_p e^{\beta t}$$

The Hamiltonian constraint $H = 0$ requires:
$$\frac{1}{2}\alpha^2 + \frac{D(D-1)}{12}\beta^2 + \frac{D}{2}\alpha\beta = 0$$

This is satisfied only for $\alpha > 0, \beta < 0$ (expanding universe, contracting internal space) or vice versa.

### Dimension-Dependent Compactification (Sec. 4)

For $D > 1$, the expansion rate $\alpha$ and compactification rate $\beta$ are related:
$$\alpha_\pm = \frac{D\beta}{2}\left[-1 \pm \sqrt{1 - \frac{2}{3}\left(1 - \frac{1}{D}\right)}\right]^{-1}$$

For given $H > 0$: higher $D$ gives faster universe expansion but slower compactification of extra dimensions. The deceleration parameter $q = -\ddot{R}R/\dot{R}^2 = -1$ (de Sitter).

The cosmological term decays exponentially: $\Lambda(t) = 3l_p^{-2}e^{-2Ht}$.

### Wheeler-DeWitt Equation (Secs. 5-6)

The WDW equation in the $(X, Y)$ mini-superspace:
$$\left[(D-1)\frac{\partial^2}{\partial X^2} + \frac{6}{D}\frac{\partial^2}{\partial Y^2} - 6\frac{\partial^2}{\partial X \partial Y}\right]\Psi(X,Y) = 0$$

Separable solutions exist:
$$\Psi_D^\pm(R,a) = C_\pm R^{p_\pm(D,\gamma)} a^{q_\pm(D,\gamma)}$$

The wave functions are peaked on the classical trajectories $Ra = 1$ (for $D = 1$) and the generalized loci for $D > 1$, confirming classical-quantum correspondence.

### Symmetry Properties

- The Lagrangian is invariant under $R \to R^{-1}, a \to a^{-1}$ (time reversal)
- For $D = 3$: dynamical symmetry $a \leftrightarrow R$ exists
- The model is singularity-free: both $R$ and $a$ are non-zero at $t = 0$

---

## Key Results

1. Exponential solutions: $R(t) = l_p e^{Ht}$ (accelerating universe) and $a(t) = l_p e^{\beta t}$ (compactifying internal space)
2. Decaying cosmological term $\Lambda \sim R^{-2}$ emerges from exotic matter with $p_\chi = (m/3 - 1)\rho_\chi$
3. The rate of compactification depends on dimension $D$: higher $D$ means slower compactification
4. Classical-quantum correspondence: WDW wave functions peak exactly on classical trajectories for all $D$
5. The closed universe with $\Lambda \neq 0$ is equivalent to a flat universe with $\Lambda = 0$
6. Deceleration parameter $q = -1$ (de Sitter expansion)
7. Singularity-free: both scale factors start at Planck length $l_p$

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Metric | $ds^2 = -N^2 dt^2 + R^2\frac{dr_i dr^i}{(1+kr^2/4)^2} + a^2 d\rho_a d\rho^a$ | Eq. (1) |
| Exotic EOS | $p_\chi = (m/3 - 1)\rho_\chi$ | Eq. (3) |
| Decaying $\Lambda$ | $\Lambda(R) = 3/R^2$ (for $m = 2$) | Eq. (10) |
| Solutions | $R = l_p e^{Ht}$, $a = l_p e^{\beta t}$ | Eqs. (29-30) |
| Hamiltonian constraint | $\frac{1}{2}\alpha^2 + \frac{D(D-1)}{12}\beta^2 + \frac{D}{2}\alpha\beta = 0$ | Eq. (24) |
| $\alpha$-$\beta$ relation | $\alpha_\pm = \frac{D\beta}{2}\left[-1 \pm \sqrt{1 - \frac{2}{3}(1 - 1/D)}\right]^{-1}$ | Eq. (26) |
| WDW equation | $\left[(D-1)\partial_X^2 + \frac{6}{D}\partial_Y^2 - 6\partial_X\partial_Y\right]\Psi = 0$ | Eq. (43) |

## Relevance to Phonon-Exflation

This paper is a direct KK cosmology precursor to the exflation mechanism. The coupled exponential solutions $R(t) \sim e^{Ht}$ and $a(t) \sim e^{\beta t}$ with $\beta < 0$ are the classical version of what the phonon-exflation framework computes quantum-mechanically: 4D expansion driven by internal-space compactification. The Hamiltonian constraint linking $\alpha$ and $\beta$ is a classical limit of the spectral action's coupled dynamics between tau (internal modulus) and 4D scale factor. The dimension-dependence of the compactification rate ($D = 6$ for the framework's SU(3)) directly constrains the expansion-compactification balance. The decaying cosmological term $\Lambda \sim R^{-2}$ foreshadows the framework's finding that the cosmological constant arises from the instanton gas dynamics during transit.
