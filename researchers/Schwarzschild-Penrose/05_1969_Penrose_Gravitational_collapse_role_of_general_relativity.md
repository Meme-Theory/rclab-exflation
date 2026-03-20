# Gravitational Collapse: The Role of General Relativity

## Roger Penrose (1969)

**Original publication:** Rivista del Nuovo Cimento, Serie I, Vol. 1, Numero Speciale, pp. 252--276 (1969)
**Reprinted as "Golden Oldie":** General Relativity and Gravitation **34**, 1141--1165 (2002)

---

## Abstract and Scope

This document provides a research-grade reference summary of Penrose's 1969 paper--lecture, in which he surveyed the physics of gravitational collapse in general relativity and posed the question that would become the **cosmic censorship conjecture**: whether singularities produced by gravitational collapse are generically hidden behind event horizons. The paper also introduced the **Penrose process** for extracting rotational energy from a Kerr black hole. Together with Penrose's 1965 singularity theorem, this work established the conceptual framework within which all subsequent research on black hole formation and singularity structure has been conducted.

---

## 1. The Physical Question: Is the Singularity Always Hidden?

### 1.1 Context from the Oppenheimer--Snyder Solution

By 1969, the Oppenheimer--Snyder (1939) solution for the collapse of a homogeneous pressureless dust ball was well understood. In that spherically symmetric model, the collapsing matter passes through its Schwarzschild radius $r = 2GM/c^2$, forming a trapped region from which no signal can escape. The singularity at $r = 0$ is spacelike and lies entirely inside the event horizon. An observer at spatial infinity never sees the singularity; it is causally screened.

Penrose's concern was whether this screening is an artifact of the perfect symmetry of the Oppenheimer--Snyder model, or a robust feature of gravitational collapse in general. Specifically:

> *"Does there exist a 'cosmic censor' who forbids the appearance of naked singularities, clothing each one in an absolute event horizon?"*
>
> -- R. Penrose, 1969

### 1.2 Why the Question Matters

If singularities can form without event horizons (so-called **naked singularities**), the predictive power of general relativity breaks down for observers at infinity. A naked singularity is a region of geodesic incompleteness visible from $\mathscr{I}^+$ (future null infinity), meaning that signals from arbitrarily close to the singular region can reach distant observers. Since general relativity provides no boundary conditions at a singularity, the future evolution of spacetime from given initial data would become indeterminate.

The question therefore has profound implications:

- **Determinism in classical GR:** Can the initial value problem be well-posed globally?
- **Astrophysical predictability:** Can observers at infinity predict the outcome of collapse?
- **Connection to quantum gravity:** Does nature require a quantum theory of gravity to resolve singularities, or does classical GR already contain a self-censoring mechanism?

### 1.3 Penrose's Conformal Approach

A key technical contribution of the paper was to place the question within the framework of conformal compactification. Penrose had introduced (1963, 1964) the technique of mapping the physical spacetime $(M, g_{ab})$ to an unphysical spacetime $(\tilde{M}, \tilde{g}_{ab})$ with

$$\tilde{g}_{ab} = \Omega^2 \, g_{ab}$$

where $\Omega$ is a conformal factor that vanishes at infinity, bringing $\mathscr{I}^+$ (future null infinity) and $\mathscr{I}^-$ (past null infinity) to finite locations on a conformal (Penrose--Carter) diagram. Within this framework, the **event horizon** of a black hole is defined precisely as:

$$\mathcal{H}^+ = \partial\left[ J^-(\mathscr{I}^+) \right]$$

That is, the event horizon is the boundary of the causal past of future null infinity -- the boundary of the set of events from which a signal can escape to infinity. This global definition, which requires knowledge of the full future development of the spacetime, was first given a careful treatment in this paper.

---

## 2. The Penrose Process and the Irreducible Mass

### 2.1 The Kerr Solution and the Ergosphere

The Kerr (1963) metric describes a rotating black hole of mass $M$ and angular momentum $J = aM$ (in geometrised units $G = c = 1$). In Boyer--Lindquist coordinates $(t, r, \theta, \phi)$:

$$ds^2 = -\left(1 - \frac{2Mr}{\Sigma}\right)dt^2 - \frac{4Mar\sin^2\theta}{\Sigma}\,dt\,d\phi + \frac{\Sigma}{\Delta}\,dr^2 + \Sigma\,d\theta^2 + \left(r^2 + a^2 + \frac{2Ma^2 r\sin^2\theta}{\Sigma}\right)\sin^2\theta\,d\phi^2$$

where

$$\Sigma = r^2 + a^2\cos^2\theta, \qquad \Delta = r^2 - 2Mr + a^2$$

The horizons are located at $\Delta = 0$:

$$r_{\pm} = M \pm \sqrt{M^2 - a^2}$$

An event horizon exists only when $a \leq M$ (i.e., $|J| \leq M^2$). When $a = M$, the black hole is **extremal**; the two horizons coincide.

The **ergosphere** (or ergoregion) is the region between the event horizon and the **stationary limit surface** (or ergosurface) where the Killing vector $\xi^a = (\partial/\partial t)^a$ becomes spacelike:

$$r_{\text{ergo}}(\theta) = M + \sqrt{M^2 - a^2\cos^2\theta}$$

Within the ergosphere, no observer can remain stationary with respect to infinity; the frame-dragging effect forces co-rotation with the black hole. Crucially, particles in the ergosphere can have **negative energy** as measured at infinity, since the Killing energy $E = -p_a \xi^a$ can be negative when $\xi^a$ is spacelike.

### 2.2 The Penrose Process

Penrose (1969) proposed the following thought experiment for extracting rotational energy from a Kerr black hole:

1. A particle of rest mass $m_0$ and energy $E_0 > 0$ falls from infinity into the ergosphere.
2. Inside the ergosphere, the particle splits into two fragments: fragment 1 with energy $E_1 < 0$ and fragment 2 with energy $E_2 > 0$.
3. Fragment 1 (with negative energy as measured at infinity) crosses the event horizon and falls into the black hole.
4. Fragment 2 escapes to infinity with energy $E_2 = E_0 - E_1 = E_0 + |E_1| > E_0$.

The escaping fragment carries away more energy than was sent in. Conservation requires:

$$E_2 = E_0 + |E_1|$$

The energy gained comes at the expense of the black hole's rotational energy. The black hole's mass decreases by $|E_1|$ and its angular momentum decreases correspondingly:

$$\delta M = E_1 < 0, \qquad \delta J = L_1$$

where $L_1$ is the angular momentum of the captured fragment. The condition $E_1 < 0$ requires $E_1 < \Omega_H L_1$, where

$$\Omega_H = \frac{a}{r_+^2 + a^2} = \frac{a}{2Mr_+}$$

is the angular velocity of the horizon.

### 2.3 Efficiency and the Irreducible Mass

The maximum efficiency of the Penrose process is limited by the **irreducible mass** $M_{\text{irr}}$, a concept developed quantitatively by Christodoulou (1970) and Christodoulou--Ruffini (1971) building directly on Penrose's mechanism. The total mass of a Kerr black hole decomposes as:

$$M^2 = M_{\text{irr}}^2 + \frac{J^2}{4M_{\text{irr}}^2}$$

where the irreducible mass is related to the horizon area $A$ by:

$$M_{\text{irr}} = \sqrt{\frac{A}{16\pi}}$$

and the area of the Kerr horizon is:

$$A = 4\pi(r_+^2 + a^2) = 8\pi M r_+$$

The second law of black hole mechanics (Hawking 1971) guarantees that $A$ (and hence $M_{\text{irr}}$) can never decrease in any classical process, including the Penrose process:

$$\delta A \geq 0 \quad \Longleftrightarrow \quad \delta M_{\text{irr}} \geq 0$$

The maximum extractable energy is therefore:

$$E_{\text{max}} = M - M_{\text{irr}} = M\left(1 - \frac{1}{\sqrt{2}}\sqrt{1 + \sqrt{1 - \left(\frac{a}{M}\right)^2}}\right)$$

For a maximally spinning black hole ($a = M$), $M_{\text{irr}} = M/\sqrt{2}$, and the maximum extractable fraction of the mass--energy is:

$$\frac{E_{\text{max}}}{M} = 1 - \frac{1}{\sqrt{2}} \approx 29.3\%$$

For the most general Kerr--Newman black hole (mass $M$, angular momentum $J$, charge $Q$), the Christodoulou--Ruffini mass formula generalises to:

$$M^2 = \left(M_{\text{irr}} + \frac{Q^2}{4M_{\text{irr}}}\right)^2 + \frac{J^2}{4M_{\text{irr}}^2}$$

---

## 3. The Weak Cosmic Censorship Conjecture (WCC)

### 3.1 Informal Statement

The **weak cosmic censorship conjecture** asserts that singularities formed from the gravitational collapse of physically reasonable matter, starting from generic, non-singular initial data, are never visible from future null infinity $\mathscr{I}^+$. Equivalently, naked singularities do not form in generic gravitational collapse.

### 3.2 Formal Statement

Let $(\Sigma, h_{ab}, K_{ab})$ be a complete, asymptotically flat initial data set for the Einstein equations satisfying physically reasonable energy conditions (e.g., the dominant energy condition). Then:

> **WCC (Penrose 1969):** For *generic* such initial data, the maximal Cauchy development $(M, g_{ab})$ possesses a complete future null infinity $\mathscr{I}^+$.

More precisely, the conjecture requires that the conformally completed spacetime $(\tilde{M}, \tilde{g}_{ab})$ admits a $\mathscr{I}^+$ that is complete in the sense that every null generator of $\mathscr{I}^+$ is complete (extends to infinite affine parameter in both directions along $\mathscr{I}^+$).

The completeness of $\mathscr{I}^+$ ensures that no singularity is visible to observers at infinity: any singularity must lie outside $J^-(\mathscr{I}^+)$, i.e., behind an event horizon.

### 3.3 Key Features of the Formulation

- **Genericity:** The conjecture does not claim that naked singularities are impossible in all solutions, but rather that they do not arise from *generic* initial data. Fine-tuned or measure-zero initial configurations may produce naked singularities without contradicting WCC.

- **Physically reasonable matter:** The matter content must satisfy appropriate energy conditions (typically the dominant energy condition: $T_{ab}v^a$ is future-causal for any future-directed timelike $v^a$).

- **Asymptotic flatness:** The conjecture is formulated for isolated gravitating systems, not cosmological spacetimes.

- **Completeness of initial data:** The initial hypersurface $\Sigma$ must itself be non-singular and complete, ruling out initial data that already contain naked singularities.

---

## 4. The Strong Cosmic Censorship Conjecture (SCC)

### 4.1 Motivation: Determinism in General Relativity

While WCC concerns what distant observers can see, the **strong cosmic censorship conjecture** addresses a more fundamental issue: the determinism of general relativity itself. The initial value problem in GR is well-posed within the **maximal globally hyperbolic development** (MGHD) of Cauchy initial data. However, some exact solutions (notably the Kerr and Reissner--Nordstrom interiors) possess **Cauchy horizons** -- boundaries beyond which the initial data no longer uniquely determine the spacetime.

If Cauchy horizons generically persist, then general relativity fails as a deterministic theory: multiple inequivalent extensions of the spacetime beyond the Cauchy horizon are possible, and the theory provides no mechanism for choosing among them.

### 4.2 Formal Statement

> **SCC (Penrose 1979):** For *generic* asymptotically flat initial data satisfying appropriate energy conditions, the maximal globally hyperbolic development (MGHD) is **inextendible** as a suitably regular Lorentzian manifold.

The regularity requirement is important. The conjecture has been formulated at various regularity classes:

| Version | Inextendibility requirement | Strength |
|---------|---------------------------|----------|
| $C^0$-SCC | Inextendible as a continuous Lorentzian manifold | Strongest |
| $C^2$-SCC | Inextendible as a $C^2$ Lorentzian manifold | Classical |
| $H^1_{\text{loc}}$-SCC | Christoffel symbols not locally $L^2$ | Intermediate |

Stronger inextendibility implies weaker: $C^0 \Rightarrow H^1_{\text{loc}} \Rightarrow C^2$.

### 4.3 The Blue-Shift Instability

Penrose identified a key physical mechanism supporting SCC: the **blue-shift instability** at Cauchy horizons. An observer approaching the inner (Cauchy) horizon of a Kerr or Reissner--Nordstrom black hole sees radiation from the external universe infinitely blue-shifted. This suggests that in a realistic perturbation of these exact solutions, the energy density diverges at the Cauchy horizon, converting it into a singularity and preventing extension of the spacetime.

The blue-shift factor for a signal emitted at advanced time $v$ near the Cauchy horizon grows as:

$$\frac{\lambda_{\text{emitted}}}{\lambda_{\text{received}}} \sim e^{-\kappa_- v}$$

where $\kappa_-$ is the surface gravity of the inner horizon:

$$\kappa_- = \frac{r_+ - r_-}{2(r_-^2 + a^2)}$$

This exponential blue-shift drives the instability that is expected to enforce SCC.

---

## 5. Distinction Between WCC and SCC

The two conjectures are **logically independent**. Neither implies the other:

| Scenario | WCC | SCC |
|----------|-----|-----|
| Schwarzschild collapse (generic perturbation) | Satisfied | Satisfied |
| Spacetime with naked singularity visible from $\mathscr{I}^+$ but with inextendible MGHD | Violated | Satisfied |
| Spacetime with complete $\mathscr{I}^+$ but extendible Cauchy horizon | Satisfied | Violated |
| Both naked singularity and extendible Cauchy horizon | Violated | Violated |

### 5.1 Physical Distinction

- **WCC** is about **observability**: can an observer at infinity see a singularity?
- **SCC** is about **determinism**: does the initial data uniquely determine the entire spacetime?

### 5.2 Geometric Distinction

- **WCC** constrains the causal structure of singularities relative to $\mathscr{I}^+$ (the conformal boundary).
- **SCC** constrains the structure of the Cauchy development as a whole, including the black hole interior.

A spacetime can satisfy WCC (singularity hidden behind an event horizon with complete $\mathscr{I}^+$) while violating SCC (the singularity inside the black hole is a Cauchy horizon allowing non-unique extensions). The Kerr interior, taken at face value, provides exactly this scenario -- though the generic instability of the Cauchy horizon is expected to restore SCC.

---

## 6. Examples That Test Cosmic Censorship

### 6.1 Overextremal Kerr: $a > M$

The Kerr metric with $a > M$ has no real roots of $\Delta = r^2 - 2Mr + a^2$, and therefore no event horizon. The ring singularity at $\Sigma = 0$ ($r = 0$, $\theta = \pi/2$) is naked -- visible from all of spacetime.

This is not a counterexample to WCC because:

1. The overextremal Kerr solution does not arise from gravitational collapse of physically reasonable initial data.
2. Attempts to "overspin" an existing Kerr black hole past the extremal limit (Wald 1974) fail: a test particle carrying sufficient angular momentum to push $a$ past $M$ also carries sufficient energy to increase $M$ proportionally. The centrifugal barrier repels particles that would violate $a \leq M$.
3. More refined gedanken experiments (Hubeny 1999, Jacobson--Sotiriou 2009) involving near-extremal black holes initially appeared to allow overspinning, but second-order backreaction effects (Sorce--Wald 2017) restore the bound.

The upshot: cosmic censorship appears to be self-consistently enforced at the extremal threshold.

### 6.2 Overcharged Reissner--Nordstrom: $|Q| > M$

The Reissner--Nordstrom metric,

$$ds^2 = -f(r)\,dt^2 + f(r)^{-1}\,dr^2 + r^2\,d\Omega^2, \qquad f(r) = 1 - \frac{2M}{r} + \frac{Q^2}{r^2}$$

has horizons at $r_{\pm} = M \pm \sqrt{M^2 - Q^2}$, which exist only for $|Q| \leq M$. When $|Q| > M$, the singularity at $r = 0$ is naked.

Testing WCC:
- **Wald (1974):** An extremal Reissner--Nordstrom black hole repels test particles that would overcharge it; the electromagnetic repulsion exceeds the gravitational attraction.
- **Hubeny (1999):** For a *near-extremal* ($Q$ slightly less than $M$) black hole, a charged test particle can apparently push $Q$ past $M$. However, this neglects self-force and backreaction.
- **Zimmerman--Vega--Poisson--Haas (2013), Sorce--Wald (2017):** When backreaction is included at second order, the inequality $|Q| \leq M$ is preserved.

### 6.3 Shell-Crossing Singularities in Dust Collapse

In the Lemaitre--Tolman--Bondi (LTB) solution for inhomogeneous dust collapse, two types of singularity can form:

- **Shell-focusing singularity:** Matter converges to $r = 0$. Depending on the initial density profile, this can be either covered (black hole) or naked. For certain choices of initial data (e.g., Christodoulou 1984, Joshi--Dwivedi 1993), the shell-focusing singularity is at least locally naked.

- **Shell-crossing singularity:** Different radial shells of dust intersect, producing a caustic in the matter flow. These singularities are gravitationally weak (the metric can be extended through them, and tidal forces remain finite), and are generally considered physically spurious -- they are artifacts of the pressureless matter model and are resolved by the introduction of pressure.

Shell-crossing singularities are naked but are not regarded as genuine counterexamples to WCC because:
1. They are gravitationally weak (not "genuine" curvature singularities in the sense relevant to censorship).
2. They disappear when realistic matter models with pressure are used.
3. They do not represent an obstruction to the unique evolution of initial data.

### 6.4 Choptuik Critical Collapse

Choptuik (1993) discovered that in the spherically symmetric Einstein--scalar field system, there exists a critical solution at the threshold of black hole formation. For a one-parameter family of initial data parametrised by $p$:

- $p > p^*$: a black hole forms with mass $M_{\text{BH}} \propto (p - p^*)^\gamma$ where $\gamma \approx 0.37$.
- $p = p^*$: a naked singularity forms (the critical solution is self-similar and singular).
- $p < p^*$: the scalar field disperses to infinity.

The critical solution $p = p^*$ has **codimension one** in the space of initial data -- it requires fine-tuning of one parameter. This is consistent with WCC under the genericity condition: the naked singularity is non-generic (measure zero in initial data space).

### 6.5 Christodoulou's Rigorous Results for Scalar Fields

Christodoulou (1999) proved a definitive result for the spherically symmetric Einstein--scalar field system:

> For the Einstein equations coupled to a massless scalar field in spherical symmetry, naked singularities arising from regular initial data are **non-generic**: the set of initial data leading to naked singularities has codimension at least one in the space of all regular initial data.

This remains one of the strongest rigorous results supporting WCC.

---

## 7. The Penrose Inequality

### 7.1 Statement

If WCC holds, then the total (ADM) mass of an asymptotically flat spacetime containing a black hole must satisfy a lower bound in terms of the area of the outermost apparent horizon (or minimal surface). This is the **Penrose inequality**:

$$\boxed{M_{\text{ADM}} \geq \sqrt{\frac{A}{16\pi}}}$$

where $A$ is the area of the outermost marginally outer trapped surface (apparent horizon). Equality holds if and only if the spacetime is exactly Schwarzschild.

### 7.2 Heuristic Derivation

Penrose's argument (1973) proceeds as follows:

1. Assume WCC holds, so the collapse produces a black hole.
2. By the area theorem (Hawking 1971), the final black hole has area $A_{\text{final}} \geq A$.
3. The final state is a Kerr black hole (by the no-hair theorem / final state conjecture) with mass $M_{\text{final}} \leq M_{\text{ADM}}$ (energy can be radiated as gravitational waves).
4. For a Kerr black hole, $M_{\text{final}} \geq M_{\text{irr}} = \sqrt{A_{\text{final}}/(16\pi)}$.
5. Combining: $M_{\text{ADM}} \geq M_{\text{final}} \geq \sqrt{A_{\text{final}}/(16\pi)} \geq \sqrt{A/(16\pi)}$.

The Penrose inequality is therefore a **necessary condition** for WCC. A violation of the Penrose inequality would disprove cosmic censorship.

### 7.3 The Riemannian Penrose Inequality

The time-symmetric (Riemannian) case restricts to initial data with $K_{ab} = 0$ (vanishing extrinsic curvature), so the constraint equations reduce to:

$$R_h \geq 0$$

where $R_h$ is the scalar curvature of the Riemannian 3-metric $h_{ab}$. The apparent horizon becomes a minimal surface.

**Theorem (Huisken--Ilmanen, 2001):** For an asymptotically flat Riemannian 3-manifold $(\Sigma, h)$ with non-negative scalar curvature,

$$M_{\text{ADM}} \geq \sqrt{\frac{A_{\max}}{16\pi}}$$

where $A_{\max}$ is the area of the largest connected component of the outermost minimal surface. The proof uses **inverse mean curvature flow** (IMCF) and the monotonicity of the Geroch/Hawking mass along the flow.

**Theorem (Bray, 2001):** Under the same hypotheses,

$$M_{\text{ADM}} \geq \sqrt{\frac{A}{16\pi}}$$

where $A$ is the **total** area of the outermost minimal surface (possibly with multiple connected components). Bray's proof uses a novel conformal flow of metrics.

### 7.4 The Full (Lorentzian) Penrose Inequality

The general Penrose inequality, without the time-symmetry assumption, remains **open**. It is one of the major unsolved problems in mathematical general relativity.

For the charged case (Reissner--Nordstrom), the conjectured inequality generalises to:

$$M_{\text{ADM}} \geq \frac{1}{2}\left(\sqrt{\frac{A}{4\pi}} + \frac{Q^2}{\sqrt{A/(4\pi)}}\right)$$

---

## 8. Status of the Conjecture

### 8.1 Rigorous Results Supporting WCC

| Result | Authors | Year |
|--------|---------|------|
| Naked singularities non-generic for Einstein--scalar field (spherical symmetry) | Christodoulou | 1999 |
| Riemannian Penrose inequality (single horizon) | Huisken--Ilmanen | 2001 |
| Riemannian Penrose inequality (multiple horizons) | Bray | 2001 |
| Nonlinear stability of Schwarzschild (exterior) | Dafermos--Holzegel--Rodnianski--Taylor | 2021 |
| Nonlinear stability of slowly rotating Kerr | Klainerman--Szeftel; Giorgi--Klainerman--Szeftel | 2022--2024 |
| Backreaction restores extremality bound (gedanken experiments) | Sorce--Wald | 2017 |

### 8.2 Results Concerning SCC

| Result | Authors | Year |
|--------|---------|------|
| Blue-shift instability at Cauchy horizon (linear) | Penrose (1968); McNamara (1978) | -- |
| $C^0$ stability of Kerr Cauchy horizon (i.e., $C^0$-SCC *fails* for Kerr) | Dafermos--Luk | 2017 |
| $C^2$-SCC holds for Einstein--Maxwell--scalar field in spherical symmetry | Dafermos | 2003--2005 |
| SCC challenged for near-extremal RN-dS ($\Lambda > 0$) | Cardoso--Costa--Destounis--Hintz--Jansen | 2018 |

### 8.3 Known "Counterexamples" and Their Status

| Example | Type | Why not a genuine counterexample |
|---------|------|----------------------------------|
| Overextremal Kerr ($a > M$) | Exact solution | Does not form from collapse; cannot be reached by overspinning |
| Overcharged RN ($\|Q\| > M$) | Exact solution | Does not form from collapse; backreaction prevents overcharging |
| Choptuik critical solution | Numerical | Codimension-1 (non-generic) in initial data space |
| LTB shell-crossing | Exact dust solution | Gravitationally weak; resolved by pressure |
| LTB shell-focusing (some profiles) | Exact dust solution | Non-generic for some formulations; genericity debated |
| $d \geq 5$ black strings/rings | Higher-dimensional | Gregory--Laflamme instability; outside 4D scope of original conjecture |
| AdS$_4$ superradiance | Asymptotically AdS | Conjecture formulated for asymptotically flat spacetimes |

### 8.4 The Role of Genericity

The genericity condition is the crux of the conjecture. All known examples of naked singularity formation from regular initial data occur at the boundary between data that disperses and data that forms black holes (the "critical" threshold). These occupy a set of measure zero -- or at least positive codimension -- in the space of initial data. The conjecture survives precisely because it claims only that *generic* collapse produces clothed singularities, not that *every* collapse does.

Establishing genericity rigorously requires:

1. A suitable topology on the space of initial data.
2. Proof that the set of data producing naked singularities has empty interior (or measure zero, or positive codimension) in that topology.

This programme has been carried out only for the spherically symmetric Einstein--scalar field system (Christodoulou 1999).

### 8.5 Open Problems

1. **Full nonlinear stability of Kerr** (for all sub-extremal $a < M$) -- now partially established.
2. **Lorentzian Penrose inequality** -- no proof exists.
3. **Weak cosmic censorship beyond spherical symmetry** -- no rigorous results.
4. **Strong cosmic censorship for Kerr** -- $C^0$-SCC fails (Dafermos--Luk), but $C^2$-SCC is expected to hold.
5. **SCC in the presence of a positive cosmological constant** -- the competition between exponential decay (from $\Lambda > 0$) and blue-shift instability is not fully resolved.
6. **The role of quantum effects** -- Hawking radiation may fundamentally alter the censorship picture.

---

## 9. Connection to the Singularity Theorems (Penrose 1965)

### 9.1 The 1965 Theorem

Penrose's 1965 singularity theorem is the direct precursor to the 1969 censorship question. The theorem states:

> **Theorem (Penrose, 1965):** A spacetime $(M, g_{ab})$ cannot be future null geodesically complete if:
> 1. $R_{ab} k^a k^b \geq 0$ for all null vectors $k^a$ (**null convergence condition** / null energy condition via Einstein's equations).
> 2. There exists a non-compact Cauchy surface $\Sigma$.
> 3. There exists a closed trapped surface $\mathcal{T}$ in $M$.

A **closed trapped surface** is a compact spacelike 2-surface $\mathcal{T}$ such that the expansion scalars of both families of future-directed null geodesics orthogonal to $\mathcal{T}$ are everywhere negative:

$$\theta_+ < 0 \quad \text{and} \quad \theta_- < 0 \quad \text{on } \mathcal{T}$$

The theorem guarantees the existence of **incomplete geodesics** (a singularity in the sense of geodesic incompleteness) but says nothing about:

- The **nature** of the singularity (curvature blow-up, or merely incompleteness).
- The **location** of the singularity (inside or outside an event horizon).
- The **visibility** of the singularity from infinity.

### 9.2 The Raychaudhuri Equation

The proof relies on the **Raychaudhuri equation** for a congruence of null geodesics with tangent vector $k^a$, affine parameter $\lambda$, expansion $\theta$, shear $\sigma_{ab}$, and vorticity $\omega_{ab}$:

$$\frac{d\theta}{d\lambda} = -\frac{1}{n-2}\theta^2 - \sigma_{ab}\sigma^{ab} + \omega_{ab}\omega^{ab} - R_{ab}k^a k^b$$

For a hypersurface-orthogonal congruence ($\omega_{ab} = 0$), and assuming the null convergence condition ($R_{ab}k^ak^b \geq 0$), this gives:

$$\frac{d\theta}{d\lambda} \leq -\frac{1}{n-2}\theta^2$$

If $\theta = \theta_0 < 0$ initially (as on a trapped surface), then $\theta \to -\infty$ within affine parameter $\lambda \leq (n-2)/|\theta_0|$: the congruence **focuses** to a caustic in finite affine parameter. This focusing, combined with topological arguments (the incompatibility of a compact trapped surface with a non-compact Cauchy surface in a geodesically complete spacetime), yields the theorem.

### 9.3 From Singularity Theorems to Cosmic Censorship

The 1965 theorem raises the censorship question directly:

- The theorem guarantees that singularities **form** (given trapped surfaces and energy conditions).
- It does **not** guarantee that singularities are **hidden**.
- The 1969 conjecture is precisely the assertion that, generically, the singularities guaranteed by the theorem are always clothed by event horizons.

In this sense, the cosmic censorship conjecture is the natural "second act" following the singularity theorems: having established that singularities are inevitable, the question becomes whether they are always invisible.

---

## 10. Key Equations -- Collected Reference

### Kerr Metric and Horizons

$$\Delta = r^2 - 2Mr + a^2, \qquad r_{\pm} = M \pm \sqrt{M^2 - a^2}$$

### Ergosphere Boundary

$$r_{\text{ergo}}(\theta) = M + \sqrt{M^2 - a^2\cos^2\theta}$$

### Horizon Angular Velocity

$$\Omega_H = \frac{a}{r_+^2 + a^2}$$

### Christodoulou Mass Formula (Kerr)

$$M^2 = M_{\text{irr}}^2 + \frac{J^2}{4M_{\text{irr}}^2}$$

### Christodoulou--Ruffini Mass Formula (Kerr--Newman)

$$M^2 = \left(M_{\text{irr}} + \frac{Q^2}{4M_{\text{irr}}}\right)^2 + \frac{J^2}{4M_{\text{irr}}^2}$$

### Irreducible Mass and Horizon Area

$$M_{\text{irr}} = \sqrt{\frac{A}{16\pi}}, \qquad A = 8\pi M r_+$$

### Penrose Inequality

$$M_{\text{ADM}} \geq \sqrt{\frac{A}{16\pi}}$$

### Raychaudhuri Equation (Null Geodesic Congruence, $\omega = 0$)

$$\frac{d\theta}{d\lambda} = -\frac{1}{n-2}\theta^2 - \sigma_{ab}\sigma^{ab} - R_{ab}k^ak^b$$

### Trapped Surface Condition

$$\theta_+ < 0 \quad \text{and} \quad \theta_- < 0$$

### Blue-Shift Factor at Cauchy Horizon

$$\frac{\lambda_{\text{emitted}}}{\lambda_{\text{received}}} \sim e^{-\kappa_- v}, \qquad \kappa_- = \frac{r_+ - r_-}{2(r_-^2 + a^2)}$$

### Event Horizon (Global Definition)

$$\mathcal{H}^+ = \partial\!\left[J^-(\mathscr{I}^+)\right]$$

That is, the event horizon is the *boundary* of the causal past of future null infinity.

### Black Hole Region

$$\mathcal{B} = M \setminus J^-(\mathscr{I}^+)$$

The black hole region is the *complement* of $J^-(\mathscr{I}^+)$ in $M$. The event horizon $\mathcal{H}^+$ is the boundary $\partial \mathcal{B}$; these are distinct objects.

---

## Appendix: Chronological Context

| Year | Development |
|------|------------|
| 1939 | Oppenheimer--Snyder: dust collapse to a black hole |
| 1963 | Kerr: rotating black hole solution |
| 1963--64 | Penrose: conformal compactification, Penrose diagrams |
| 1965 | **Penrose singularity theorem** (trapped surfaces $\Rightarrow$ incompleteness) |
| **1969** | **Penrose: "Gravitational Collapse: The Role of General Relativity"** -- cosmic censorship conjecture, Penrose process |
| 1970 | Christodoulou: irreducible mass |
| 1970 | Hawking--Penrose: general singularity theorems |
| 1971 | Hawking: area theorem ($\delta A \geq 0$) |
| 1971 | Christodoulou--Ruffini: mass formula for Kerr--Newman |
| 1973 | Penrose: the Penrose inequality |
| 1973 | Bardeen--Carter--Hawking: laws of black hole mechanics |
| 1974 | Wald: impossibility of destroying horizon of extremal Kerr--Newman |
| 1979 | Penrose: strong cosmic censorship conjecture |
| 1986 | Penrose: refined SCC formulation (inextendibility of MGHD) |
| 1993 | Choptuik: critical phenomena in gravitational collapse |
| 1999 | Christodoulou: naked singularities non-generic (spherical scalar field) |
| 2001 | Huisken--Ilmanen: Riemannian Penrose inequality (IMCF proof) |
| 2001 | Bray: Riemannian Penrose inequality (conformal flow proof) |
| 2017 | Dafermos--Luk: $C^0$ stability of Kerr Cauchy horizon |
| 2017 | Sorce--Wald: new proof that gedanken experiments cannot destroy horizons |
| 2020 | Nobel Prize in Physics to Penrose (with Genzel and Ghez) |

---

## References

1. R. Penrose, "Gravitational collapse and space-time singularities," *Phys. Rev. Lett.* **14**, 57--59 (1965).
2. R. Penrose, "Gravitational collapse: The role of general relativity," *Riv. Nuovo Cim.* **1**, 252--276 (1969). Reprinted in *Gen. Rel. Grav.* **34**, 1141--1165 (2002).
3. D. Christodoulou, "Reversible and irreversible transformations in black-hole physics," *Phys. Rev. Lett.* **25**, 1596--1597 (1970).
4. D. Christodoulou and R. Ruffini, "Reversible transformations of a charged black hole," *Phys. Rev. D* **4**, 3552--3555 (1971).
5. S. W. Hawking, "Gravitational radiation from colliding black holes," *Phys. Rev. Lett.* **26**, 1344--1346 (1971).
6. R. Penrose, "Naked singularities," *Ann. N.Y. Acad. Sci.* **224**, 125--134 (1973).
7. R. M. Wald, "Gedanken experiments to destroy a black hole," *Ann. Phys.* **82**, 548--556 (1974).
8. R. Penrose, "Singularities and time-asymmetry," in *General Relativity: An Einstein Centenary Survey*, eds. S. W. Hawking and W. Israel, Cambridge University Press (1979).
9. M. W. Choptuik, "Universality and scaling in gravitational collapse of a massless scalar field," *Phys. Rev. Lett.* **70**, 9--12 (1993).
10. D. Christodoulou, "The instability of naked singularities in the gravitational collapse of a scalar field," *Ann. Math.* **149**, 183--217 (1999).
11. G. Huisken and T. Ilmanen, "The inverse mean curvature flow and the Riemannian Penrose inequality," *J. Diff. Geom.* **59**, 353--437 (2001).
12. H. L. Bray, "Proof of the Riemannian Penrose inequality using the positive mass theorem," *J. Diff. Geom.* **59**, 177--267 (2001).
13. M. Dafermos and J. Luk, "The interior of dynamical vacuum black holes I: The $C^0$-stability of the Kerr Cauchy horizon," arXiv:1710.01722 (2017).
14. J. Sorce and R. M. Wald, "Gedanken experiments to destroy a black hole. II. Kerr-Newman black holes cannot be overcharged or overspun," *Phys. Rev. D* **96**, 104014 (2017).
15. J. M. M. Senovilla, "The 1965 Penrose singularity theorem," *Class. Quantum Grav.* **32**, 124008 (2015).
16. R. Penrose, "The question of cosmic censorship," *J. Astrophys. Astron.* **20**, 233--248 (1999).

---

*Document prepared as a research-grade reference summary. All equations in LaTeX notation. This summary synthesises the original 1969 paper with subsequent developments to provide a self-contained account of the cosmic censorship programme as initiated by Penrose.*
