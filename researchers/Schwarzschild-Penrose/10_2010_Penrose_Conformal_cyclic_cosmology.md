# Conformal Cyclic Cosmology (CCC)

## Roger Penrose (2010)

**Primary Source:** *Cycles of Time: An Extraordinary New View of the Universe* (The Bodley Head, 2010)
**Foundational Paper:** R. Penrose, "Before the Big Bang: An Outrageous New Perspective and Its Implications for Particle Physics," *Proc. EPAC 2006*, Edinburgh, pp. 2759--2763 (2006)
**Key Technical Papers:**
- R. Penrose, "The Basic Ideas of Conformal Cyclic Cosmology," in *Death and Anti-Death*, Vol. 6, ed. C. Tandy (Ria University Press, 2009)
- P. Tod, "The Equations of Conformal Cyclic Cosmology," *Gen. Relativ. Gravit.* **47**, 17 (2015); arXiv:1309.7248
- K.P. Tod, "Penrose's Weyl Curvature Hypothesis and Conformally-Cyclic Cosmology," *J. Phys.: Conf. Ser.* **229**, 012013 (2010)
- P. Nurowski, "Toward Fixing a Framework for Conformal Cyclic Cosmology," *Gen. Relativ. Gravit.* **55**, 100 (2023); arXiv:2212.06914
- K.A. Meissner and R. Penrose, "The Physics of Conformal Cyclic Cosmology," arXiv:2503.24263 (2025)

---

## Table of Contents

1. [The Central Idea](#1-the-central-idea)
2. [Mathematical Framework: Conformal Rescaling](#2-mathematical-framework-conformal-rescaling)
3. [The Weyl Curvature Hypothesis](#3-the-weyl-curvature-hypothesis)
4. [The Tod-Penrose Proposal for Suppressed Weyl Curvature](#4-the-tod-penrose-proposal-for-suppressed-weyl-curvature)
5. [The Cosmological Constant and Asymptotic de Sitter Structure](#5-the-cosmological-constant-and-asymptotic-de-sitter-structure)
6. [The Fate of Massive Particles](#6-the-fate-of-massive-particles)
7. [Information Transfer Between Aeons: Hawking Points](#7-information-transfer-between-aeons-hawking-points)
8. [Observational Claims: Concentric Circles in the CMB](#8-observational-claims-concentric-circles-in-the-cmb)
9. [The Second Law of Thermodynamics and Gravitational Entropy](#9-the-second-law-of-thermodynamics-and-gravitational-entropy)
10. [Mathematical Details of the Conformal Crossover](#10-mathematical-details-of-the-conformal-crossover)
11. [Criticisms and Open Problems](#11-criticisms-and-open-problems)
12. [Key Equations](#12-key-equations-collected)

---

## 1. The Central Idea

Conformal Cyclic Cosmology proposes that the history of the universe consists of an infinite succession of *aeons*---each one an entire cosmological epoch running from a Big Bang to an indefinitely expanding future. The infinite future of each aeon is conformally identified with the Big Bang singularity of the next.

The key physical observation is that **conformal geometry becomes exact at two critical epochs**:

### 1.1 The Remote Future

In the far future of an aeon with a positive cosmological constant $\Lambda > 0$, the universe undergoes exponential (de Sitter) expansion. Over timescales vastly exceeding the current age of the universe ($\gg 10^{10}$ yr), all structure is diluted:

- All black holes evaporate via Hawking radiation on timescales of order $\sim 10^{67}$--$10^{100}$ years.
- Penrose hypothesises that all rest mass eventually decays or "fades out."
- The universe becomes dominated by massless radiation (photons, gravitons) in an exponentially expanding, increasingly homogeneous spacetime.

Since massless fields are **conformally invariant**---their physics depends only on the light-cone structure (the angles between null geodesics) and not on distance scales---the remote future is described *exactly* by conformal geometry. The metric loses physical significance except for its conformal equivalence class.

### 1.2 The Big Bang

At the Big Bang, the universe was radiation-dominated. The stress-energy tensor of a radiation fluid has vanishing trace:

$$T^{\mu}{}_{\mu} = 0$$

This means the physics is conformally invariant: the equations governing massless fields (Maxwell's equations, the Yang-Mills equations, the conformally coupled scalar field) are all invariant under

$$g_{\mu\nu} \;\longrightarrow\; \tilde{g}_{\mu\nu} = \Omega^{2}\, g_{\mu\nu}$$

At the very earliest moments, when the universe was effectively a plasma of massless (or ultra-relativistic) particles, distances and times had no intrinsic meaning---only angles and causal relationships mattered.

### 1.3 The Identification

Since both the remote future and the Big Bang are described by conformal geometry alone, Penrose proposes that **they are the same 3-surface**, viewed from opposite sides:

$$\mathscr{I}^{+}_{\text{(previous aeon)}} \;\equiv\; \mathscr{B}_{\text{(next aeon)}}$$

where $\mathscr{I}^{+}$ denotes future conformal infinity (a spacelike 3-surface when $\Lambda > 0$) and $\mathscr{B}$ denotes the Big Bang hypersurface of the next aeon. The full spacetime manifold is then:

$$\mathscr{M} = \cdots \cup \mathscr{A}_{n-1} \cup \mathscr{X}_{n-1} \cup \mathscr{A}_{n} \cup \mathscr{X}_{n} \cup \mathscr{A}_{n+1} \cup \cdots$$

where each $\mathscr{A}_{k}$ is an aeon and each $\mathscr{X}_{k}$ is a **crossover surface** connecting the future infinity of aeon $k$ to the Big Bang of aeon $k+1$.

---

## 2. Mathematical Framework: Conformal Rescaling

### 2.1 Conformal Equivalence

Two Lorentzian metrics $g_{\mu\nu}$ and $\tilde{g}_{\mu\nu}$ on a manifold $\mathscr{M}$ are **conformally related** if there exists a smooth positive function $\Omega$ such that:

$$\tilde{g}_{\mu\nu} = \Omega^{2}\, g_{\mu\nu}$$

A conformal transformation preserves:
- **Null geodesics** (light rays): the causal structure is unchanged.
- **Angles** between vectors at a point.
- **The Weyl tensor** (with appropriate index placement): $\tilde{C}^{\alpha}{}_{\beta\gamma\delta} = C^{\alpha}{}_{\beta\gamma\delta}$.

It does **not** preserve:
- Distances and proper times.
- The Ricci tensor and Ricci scalar (these acquire $\Omega$-dependent correction terms).
- The Einstein equations (these are not conformally invariant).

### 2.2 Two Physical Metrics and the Bridging Metric

The CCC construction involves three metrics in the neighbourhood of a crossover surface $\mathscr{X}$:

1. **The physical metric of the previous aeon** $\hat{g}_{\mu\nu}$: this is the actual spacetime geometry in which the previous aeon evolves. As one approaches $\mathscr{I}^{+}$ of the previous aeon, distances diverge.

2. **The physical metric of the next aeon** $\check{g}_{\mu\nu}$: this is the actual geometry in which the Big Bang of the next aeon occurs. Near $\mathscr{B}$, the scale factor vanishes and curvature diverges.

3. **The bridging (unphysical) metric** $g_{\mu\nu}$: a smooth, non-degenerate metric defined in a neighbourhood of $\mathscr{X}$. Both physical metrics are conformally related to this bridging metric.

The conformal relations are:

$$\hat{g}_{\mu\nu} = \hat{\Omega}^{2}\, g_{\mu\nu}$$

$$\check{g}_{\mu\nu} = \check{\Omega}^{2}\, g_{\mu\nu}$$

where:
- $\hat{\Omega} \to \infty$ as one approaches $\mathscr{X}$ from the previous aeon (the physical metric diverges at future infinity).
- $\check{\Omega} \to 0$ as one approaches $\mathscr{X}$ from the next aeon (the physical metric degenerates at the Big Bang).

### 2.3 The Reciprocal Hypothesis

Penrose's central gauge condition connecting the two conformal factors is the **reciprocal hypothesis**:

$$\boxed{\hat{\Omega}\, \check{\Omega} = -1}$$

This is a critical constraint. It means:

$$\check{\Omega} = -\hat{\Omega}^{-1}$$

and therefore the two physical metrics are related by:

$$\check{g}_{\mu\nu} = \hat{\Omega}^{-4}\, \hat{g}_{\mu\nu}$$

The sign convention (the minus sign) is chosen so that the orientation of time is preserved across the crossover: the future-directed timelike direction in the previous aeon maps to the future-directed timelike direction in the next aeon.

### 2.4 Transformation of Curvature Quantities

Under $\tilde{g}_{\mu\nu} = \Omega^{2}\, g_{\mu\nu}$, with $\Upsilon_{\mu} = \Omega^{-1} \nabla_{\mu}\Omega$:

**Christoffel symbols:**

$$\tilde{\Gamma}^{\alpha}_{\beta\gamma} = \Gamma^{\alpha}_{\beta\gamma} + \delta^{\alpha}_{\beta}\,\Upsilon_{\gamma} + \delta^{\alpha}_{\gamma}\,\Upsilon_{\beta} - g_{\beta\gamma}\,\Upsilon^{\alpha}$$

**Ricci tensor:**

$$\tilde{R}_{\mu\nu} = R_{\mu\nu} - 2\nabla_{\mu}\Upsilon_{\nu} + 2\Upsilon_{\mu}\Upsilon_{\nu} - g_{\mu\nu}\bigl(\nabla_{\alpha}\Upsilon^{\alpha} + 2\Upsilon_{\alpha}\Upsilon^{\alpha}\bigr)$$

**Ricci scalar** (in $d = 4$; the $(\partial\Omega)^2$ terms cancel exactly when the spacetime dimension equals four):

$$\tilde{R} = \Omega^{-2}\, R - 6\,\Omega^{-3}\,\Box\Omega$$

Equivalently, $\tilde{R} = \Omega^{-2}\bigl(R - 6\,\Omega^{-1}\Box\Omega\bigr)$. In general dimension $n$, the formula is $\tilde{R} = \Omega^{-2}R - 2(n{-}1)\Omega^{-3}\Box\Omega - (n{-}1)(n{-}4)\Omega^{-4}g^{\mu\nu}\partial_\mu\Omega\,\partial_\nu\Omega$.

**Weyl tensor (invariance):**

$$\tilde{C}_{\mu\nu\rho\sigma} = C_{\mu\nu\rho\sigma} \qquad \text{(with all indices lowered using the respective metrics)}$$

More precisely, the mixed-index form is strictly invariant:

$$\tilde{C}^{\alpha}{}_{\beta\gamma\delta} = C^{\alpha}{}_{\beta\gamma\delta}$$

while the fully covariant form transforms as $\tilde{C}_{\alpha\beta\gamma\delta} = \Omega^{2}\, C_{\alpha\beta\gamma\delta}$.

---

## 3. The Weyl Curvature Hypothesis

### 3.1 Statement

Penrose's **Weyl Curvature Hypothesis** (WCH), first proposed in 1979, states that the Weyl curvature tensor vanishes at the Big Bang:

$$\boxed{C_{\alpha\beta\gamma\delta} = 0 \quad \text{at } \mathscr{B}\text{ (the Big Bang)}}$$

This means the initial singularity is **conformally flat**: the spacetime geometry near the Big Bang is (conformally) the same as flat Minkowski space or a Friedmann-Lemaitre-Robertson-Walker (FLRW) model.

### 3.2 Physical Interpretation

The Weyl tensor encodes the **freely gravitational degrees of freedom**---tidal forces, gravitational waves, and the tendency of matter to clump. The Ricci tensor, by contrast, is determined locally by the matter content via Einstein's equations.

- $C_{\alpha\beta\gamma\delta} = 0$ means **no gravitational clumping**: the universe begins in a perfectly smooth, homogeneous state.
- As the universe evolves, gravitational instabilities grow, structure forms, and $C_{\alpha\beta\gamma\delta}$ increases monotonically in some averaged sense.
- In the far future, supermassive black holes represent regions of extreme Weyl curvature. Their evaporation via Hawking radiation effectively "destroys" this curvature information, returning the Weyl tensor to negligibly small values across the exponentially expanding spacetime.

### 3.3 Contrast with the Final State

At the end of an aeon, after all black holes have evaporated and the universe is dominated by a smooth radiation bath in de Sitter spacetime, the Weyl curvature is again effectively zero (or at least conformally negligible). This makes the future infinity $\mathscr{I}^{+}$ conformally flat as well, consistent with the WCH being automatically satisfied at the Big Bang of the next aeon.

### 3.4 The Riemann Decomposition

The full Riemann curvature tensor decomposes as:

$$R^{\alpha\beta}{}_{\gamma\delta} = C^{\alpha\beta}{}_{\gamma\delta} + E^{\alpha\beta}{}_{\gamma\delta} + \tfrac{1}{6}\, R\, \delta^{[\alpha}_{\gamma}\, \delta^{\beta]}_{\delta}$$

where $E^{\alpha\beta}{}_{\gamma\delta}$ contains the trace-free Ricci part. At the Big Bang, $C = 0$ means the entire curvature is determined by the matter content alone (through the Ricci tensor), and the gravitational field carries no independent degrees of freedom.

---

## 4. The Tod-Penrose Proposal for Suppressed Weyl Curvature

### 4.1 Why the Big Bang Was Special

The central puzzle of cosmology that CCC addresses is: *Why did the Big Bang have such extraordinarily low gravitational entropy?* The observed homogeneity and isotropy of the early universe (confirmed by the CMB to one part in $10^{5}$) is profoundly unlikely if initial conditions were chosen at random from the space of all possible initial data.

Penrose famously estimated (in *The Emperor's New Mind*, 1989) that the probability of the observed initial state is of order:

$$\frac{1}{10^{10^{123}}}$$

This number arises from the Bekenstein-Hawking entropy formula applied to the observable universe if all its mass were in a single black hole, representing the maximum entropy state.

### 4.2 Isotropic Singularities

The mathematical framework for the WCH was developed substantially by Paul Tod. An **isotropic singularity** (or **isotropic cosmological singularity**) is a cosmological singularity that can be removed by a conformal rescaling of the metric:

$$\tilde{g}_{\mu\nu} = \Psi^{2}\, g_{\mu\nu}$$

where $\Psi \to 0$ at the singularity, and the rescaled metric $\tilde{g}_{\mu\nu}$ is regular (non-singular) across the initial hypersurface $\Sigma$.

Key properties of isotropic singularities:

1. The singularity occurs on a spacelike hypersurface in the unphysical metric.
2. The Weyl tensor remains finite at the singularity (since $\tilde{C}^{\alpha}{}_{\beta\gamma\delta} = C^{\alpha}{}_{\beta\gamma\delta}$ is invariant).
3. For a radiation fluid with equation of state $p = \frac{1}{3}\rho$, the conformal factor behaves as $\Psi \sim \tau^{1}$ in conformal time $\tau$, which is smooth and differentiable.

### 4.3 Well-Posedness

Tod and collaborators showed that the evolution equations for the conformally rescaled, unphysical geometry can be expressed as a **first-order symmetric hyperbolic system** (a Fuchsian system):

$$A_{0}(u)\,\frac{\partial u}{\partial \tau} = A_{i}(u)\,\frac{\partial u}{\partial x^{i}} + B(u)\,u + \frac{1}{\tau}\,C(u)\,u$$

with appropriate Fuchsian conditions ($C(u_{0})\,u_{0} = 0$ and no positive integer eigenvalues of $(A_{0}(u_{0}))^{-1}C(u_{0})$). The freely specifiable data reduces to the 3-metric $h^{0}_{ij}$ on the initial hypersurface of the unphysical spacetime.

This establishes that the WCH yields a **well-posed initial-value problem**: given a 3-metric on $\Sigma$, the subsequent evolution is determined, and the Weyl tensor is guaranteed to vanish at $\Sigma$.

---

## 5. The Cosmological Constant and Asymptotic de Sitter Structure

### 5.1 The Role of $\Lambda > 0$

A positive cosmological constant is **essential** to CCC. Without it, the conformal future boundary $\mathscr{I}^{+}$ would not be spacelike, and the crossover construction would fail.

With $\Lambda > 0$, the late universe is asymptotically **de Sitter**: the metric approaches

$$ds^{2} = dt^{2} - e^{2Ht}\bigl(dx^{2} + dy^{2} + dz^{2}\bigr)$$

where $H = \sqrt{\Lambda/3}$ is the Hubble parameter of de Sitter space. The exponential expansion has critical consequences:

1. **All structure is diluted**: matter density falls as $\rho \propto a^{-3}$ (or $a^{-4}$ for radiation), becoming negligible against the constant dark energy density $\rho_{\Lambda} = \Lambda / (8\pi G)$.

2. **Horizons form**: each observer's causal future is bounded by a cosmological event horizon. Regions of spacetime become permanently causally disconnected.

3. **The Weyl curvature is "ironed out"**: gravitational perturbations are exponentially redshifted and diluted, so $C_{\alpha\beta\gamma\delta} \to 0$ at $\mathscr{I}^{+}$.

### 5.2 Conformal Boundary Structure

For a spacetime with $\Lambda > 0$ and vanishing matter, the conformal boundary $\mathscr{I}^{+}$ is a **spacelike** 3-surface. This contrasts with:
- $\Lambda = 0$: $\mathscr{I}^{+}$ is a null surface.
- $\Lambda < 0$: $\mathscr{I}$ is timelike (anti-de Sitter).

The spacelike character of $\mathscr{I}^{+}$ (when $\Lambda > 0$) matches the spacelike character of the Big Bang singularity $\mathscr{B}$, making the conformal identification geometrically natural.

### 5.3 Boundary Condition at $\mathscr{I}^{+}$

At conformal infinity with vanishing matter trace, the conformal factor $\Theta$ (with $g_{\mu\nu} = \Theta^{2}\tilde{g}_{\mu\nu}$ where $\Theta \to 0$ at $\mathscr{I}^{+}$) satisfies:

$$g^{\mu\nu}\,\partial_{\mu}\Theta\,\partial_{\nu}\Theta = \frac{\Lambda}{3} \quad \text{at } \mathscr{I}^{+}$$

and the Weyl tensor vanishes at the boundary:

$$C_{\mu\nu\rho\sigma}\,\partial^{\sigma}\Theta = 0 \quad \text{at } \mathscr{I}^{+}$$

### 5.4 Starobinsky Expansion

Near $\mathscr{I}^{+}$ with $\Lambda = 3H^{2}$, the metric admits a **Starobinsky expansion**:

$$g = dt^{2} - e^{2Ht}\, h_{ij}\, dx^{i}\, dx^{j}$$

$$h_{ij} = a_{ij} + e^{-2Ht}\, b_{ij} + e^{-3Ht}\, c_{ij} + \cdots$$

The coefficient $b_{ij}$ is universally determined by the free data $a_{ij}$:

$$b_{ij} = H^{-2}\Bigl(\rho_{ij} - \tfrac{1}{4}\,\rho\, a_{ij}\Bigr)$$

where $\rho_{ij}$ and $\rho$ are the Ricci tensor and Ricci scalar of the "boundary metric" $a_{ij}$. The **free data** at $\mathscr{I}^{+}$ consists of the 3-metric $a_{ij}$ and a trace-free, divergence-free symmetric tensor $c_{ij}$:

$$a^{ij}\, c_{ij} = 0, \qquad D_{i}\, c^{ij} = 0$$

These data encode, respectively, the conformal 3-geometry and the gravitational radiation content at infinity. The rescaling freedom is:

$$(a_{ij},\, c_{ij}) \;\longrightarrow\; (\theta^{2}\, a_{ij},\; \theta^{-1}\, c_{ij})$$

for any smooth positive function $\theta$ on $\mathscr{I}^{+}$.

### 5.5 De Sitter Group and Mass

Penrose notes a subtle but important point: with $\Lambda > 0$ fundamental, the relevant symmetry group of particle physics should be the **de Sitter group** $SO(4,1)$ rather than the Poincare group $ISO(3,1)$. Mass is a **Casimir operator** of the Poincare group, but it is *not* a Casimir operator of the de Sitter group. This means that in the presence of a fundamental $\Lambda$, rest mass need not be an absolute constant for a stable particle---it can evolve over cosmological timescales.

---

## 6. The Fate of Massive Particles

### 6.1 The Rest-Mass Decay Hypothesis

For CCC to function, conformal invariance must become exact in the remote future. This requires that **all rest mass eventually vanishes**. Penrose proposes several mechanisms:

#### Proton Decay

Grand unified theories (GUTs) generically predict proton decay, albeit with half-lives exceeding current experimental bounds ($\tau_{p} > 10^{34}$ yr). In the context of CCC, even extremely long-lived baryons must ultimately decay. Since electric charge is conserved, the ultimate positively charged decay products would be positrons---which themselves must eventually undergo mass fade-out.

#### Black Hole Evaporation

The most important mass-destruction mechanism. A black hole of mass $M$ radiates thermally at the **Hawking temperature**:

$$T_{H} = \frac{\hbar\, c^{3}}{8\pi\, G\, M\, k_{B}}$$

The evaporation timescale is:

$$t_{\text{evap}} \sim \frac{5120\,\pi\, G^{2}\, M^{3}}{\hbar\, c^{4}}$$

For a supermassive black hole of mass $\sim 10^{10}\, M_{\odot}$, this gives $t_{\text{evap}} \sim 10^{100}$ yr. Through this process, all the mass-energy originally captured by black holes is converted into massless Hawking radiation (primarily photons and gravitons).

#### Asymptotic Mass Fade-Out

Penrose's most speculative proposal: even stable particles like the electron (and positron) undergo a gradual loss of rest mass over cosmological timescales due to the de Sitter group structure replacing the Poincare group. The ground state of hydrogen gradually dissociates as the electron and proton masses fade:

$$m_{e}(t) \to 0, \qquad m_{p}(t) \to 0 \qquad \text{as } t \to \infty$$

Electric charge $e$ and $\hbar$ remain constant throughout this process.

### 6.2 The Massless Final State

After all these processes, the remote future of each aeon consists of:
- An exponentially expanding de Sitter background.
- A dilute bath of photons and gravitons (massless, conformally invariant).
- Possibly some residual charged massless particles.
- No massive particles, no black holes, no bound structures.

This state is conformally identical to a compact, hot radiation-dominated universe---i.e., a Big Bang.

---

## 7. Information Transfer Between Aeons: Hawking Points

### 7.1 The Concept

CCC predicts that the crossover surface $\mathscr{X}$ is not a total information barrier. Certain physical signals from the previous aeon can propagate through the conformal rescaling and appear as imprints in the next aeon's CMB.

The most dramatic predicted signal comes from the **Hawking evaporation of supermassive black holes** in the previous aeon. The final burst of Hawking radiation from such an evaporation event is concentrated at a single spacetime point on $\mathscr{I}^{+}$---a **Hawking point**.

### 7.2 Physical Mechanism

In the previous aeon, a supermassive black hole of mass $M \sim 10^{10}\, M_{\odot}$ at the centre of a galaxy cluster evaporates over $\sim 10^{100}$ years. As the hole shrinks, its Hawking temperature rises and the radiation becomes increasingly energetic. The final evaporation event releases a burst of very high-energy radiation.

Under the conformal rescaling to the next aeon, this event maps to a single point on $\mathscr{B}$ (the Big Bang of the next aeon). The enormous energy of the Hawking burst, concentrated at this point, propagates outward as a spherical shell of enhanced radiation. By the time of last scattering (the epoch when the CMB was emitted), this shell has expanded to a characteristic angular scale.

### 7.3 Predicted CMB Signatures

Hawking points should appear as:

1. **Anomalous hot spots**: localised regions of elevated temperature in the CMB, with angular diameters of approximately **3--4 degrees** (angular radii $\sim 0.03$--$0.04$ radians).

2. **Concentric rings of low temperature variance**: surrounding each Hawking point, a family of concentric circles with anomalously low variance in temperature fluctuations.

3. **Correlation with large-scale structure**: the temperature fluctuations at Hawking points should correlate with galactic cluster masses observed in the current aeon, since both are seeded by the same previous-aeon structure.

### 7.4 Gravitational Wave Transfer

In addition to electromagnetic radiation, **gravitational waves** can propagate through the crossover. The Weyl tensor, being conformally invariant (in the appropriate sense), carries information about gravitational radiation from the previous aeon into the next.

The 2025 paper by Meissner and Penrose introduces a **Gravitational Wave Epoch (GWE)**---a period immediately following the crossover in which gravitational wave energy dominates the dynamics. This GWE may explain why Hawking spots appear approximately **twice as large** as naively expected: the gravitational wave-dominated period introduces additional expansion before the standard radiation-dominated era begins.

### 7.5 Spinor and Twistor Methods

The mass-energy conservation law across the crossover is derived using **2-spinor and twistor techniques**. In the spinor formalism:

- The Weyl spinor $\Psi_{ABCD}$ (totally symmetric, representing the spin-2 gravitational field) satisfies the massless field equation:

$$\nabla^{AA'}\Psi_{ABCD} = 0$$

- Using the **twistor equation** $\nabla_{A'(A}\varpi^{B)} = 0$ and the Killing spinor equation $\nabla_{A'(A}\kappa^{BC)} = 0$, one constructs conserved integrals that measure mass-energy via spin reduction:

$$\phi_{AB} = \Psi_{ABCD}\,\kappa^{CD}$$

which satisfies $\nabla^{AA'}\phi_{AB} = 0$ (a Maxwell-like equation), yielding a closed 2-form whose integral over a 2-sphere gives a conserved mass-energy charge.

---

## 8. Observational Claims: Concentric Circles in the CMB

### 8.1 Gurzadyan-Penrose (2010)

In November 2010, V.G. Gurzadyan and R. Penrose published a preprint claiming that observations of the CMB from the WMAP satellite and the BOOMERanG experiment showed an **excess of concentric circles** of anomalously low temperature variance, compared with simulations based on the standard $\Lambda$CDM model. They reported a significance of up to **6$\sigma$** for the most prominent ring families.

**References:**
- V.G. Gurzadyan and R. Penrose, "Concentric circles in WMAP data may provide evidence of violent pre-Big-Bang activity," arXiv:1011.3706 (2010)

### 8.2 Independent Rebuttals (2010--2011)

Three independent groups rapidly challenged the Gurzadyan-Penrose result:

1. **Wehus and Eriksen** (arXiv:1012.1268): Found that the concentric low-variance circles were consistent with $\Lambda$CDM Gaussian random simulations when using the correct power spectrum.

2. **Moss, Scott, and Zibin** (arXiv:1012.1305): Showed that the claimed anomalies arose from an inappropriate choice of comparison power spectrum in the Gurzadyan-Penrose simulations.

3. **Hajian** (arXiv:1012.1656): Independently confirmed no statistically significant excess of concentric circles.

The core issue was that Gurzadyan and Penrose had used simulations with a power spectrum that did not match the $\Lambda$CDM theoretical prediction, leading to a spurious detection.

### 8.3 Updated Claims (2011--2013)

Gurzadyan and Penrose responded with updated analyses, arguing that the significance depends on whether one uses the **realisation-specific** WMAP power spectrum (affected by cosmic variance) or the **theoretical** $\Lambda$CDM spectrum. However, the independent reanalyses all used the theoretical $\Lambda$CDM spectrum and still found no significant signal.

### 8.4 Hawking Points Paper (2018)

In 2018, D. An, K.A. Meissner, P. Nurowski, and R. Penrose presented a more refined analysis:

- **Data**: Planck 70 GHz satellite data and WMAP data.
- **Claim**: Detection of numerous anomalous circular spots of significantly elevated temperature, with angular radii between 0.03 and 0.04 radians, at confidence levels exceeding 99.98% when compared against 10,000 standard $\Lambda$CDM simulations.
- **Identification**: These spots were proposed as "Hawking points"---remnants of supermassive black hole evaporation from the previous aeon.

**Reference:** D. An, K.A. Meissner, P. Nurowski, R. Penrose, "Apparent evidence for Hawking points in the CMB Sky," *Mon. Not. R. Astron. Soc.* **495**(3), 3403--3408 (2020); arXiv:1808.01740

### 8.5 Further Reanalysis (2020)

Jow and Scott (arXiv:1909.09672) reanalysed the Hawking points claim and found that the ostensibly anomalous hot spots were **consistent with the standard inflationary picture** once the **look-elsewhere effect** was properly accounted for. When searching over the full sky for the most extreme fluctuation, finding spots at the claimed significance level is expected in $\Lambda$CDM.

### 8.6 Current Status

The observational evidence for CCC signatures in the CMB remains **controversial and not widely accepted**. The debate continues, with CCC proponents pursuing higher-resolution analyses and critics maintaining that no statistically robust signal has been demonstrated beyond what standard $\Lambda$CDM predicts.

---

## 9. The Second Law of Thermodynamics and Gravitational Entropy

### 9.1 The Entropy Problem

The second law of thermodynamics states that entropy never decreases in a closed system. The early universe had extraordinarily low entropy (as evidenced by its near-perfect homogeneity), while the late universe has enormously high entropy (dominated by supermassive black holes). In any cyclic cosmology, one must explain how a high-entropy final state can give rise to a low-entropy initial state without violating the second law.

### 9.2 Penrose's Resolution: Two Kinds of Entropy

Penrose distinguishes between:

1. **Matter entropy** $S_{\text{matter}}$: the thermodynamic entropy of radiation, gas, etc. This is related to the Ricci curvature (via Einstein's equations, which relate Ricci curvature to the stress-energy tensor).

2. **Gravitational entropy** $S_{\text{grav}}$: the entropy associated with gravitational degrees of freedom, encoded in the Weyl curvature. Black holes represent the maximum of gravitational entropy, with the **Bekenstein-Hawking formula**:

$$S_{\text{BH}} = \frac{k_{B}\, c^{3}\, A}{4\, G\, \hbar}$$

where $A$ is the event horizon area.

### 9.3 The Entropy "Reset"

The crucial claim is that the second law is *not* violated at the crossover. Instead, what happens is:

1. **During the aeon**: Both matter entropy and gravitational entropy increase. Gravitational clumping produces black holes with enormous Bekenstein-Hawking entropy ($S_{\text{BH}} \sim 10^{90}\, k_{B}$ for a $10^{10}\, M_{\odot}$ hole). The total entropy is dominated by black hole entropy.

2. **Black hole evaporation**: As each black hole evaporates, Penrose argues that the information (and hence entropy) stored in the black hole is **destroyed**---not radiated away in a unitary process. This is Penrose's stance on the black hole information paradox: information is genuinely lost. The evaporated Hawking radiation has far less entropy than the original black hole.

3. **At the crossover**: With all black holes gone and all rest mass decayed, the universe contains only a smooth, homogeneous radiation bath. The gravitational entropy (Weyl curvature) is essentially zero. The matter entropy, while nonzero, corresponds to a state that is conformally equivalent to a hot, dense, homogeneous Big Bang---which is precisely a **low gravitational entropy** state.

4. **In the next aeon**: Gravitational entropy is free to grow again from its minimum. The second law holds *within* each aeon, and across the crossover, the total entropy budget is effectively "reset" because the dominant contribution (gravitational/black hole entropy) has been removed by evaporation.

### 9.4 The Key Asymmetry

The second law in CCC is fundamentally a statement about the **Weyl curvature**:

$$\text{Weyl curvature hypothesis:} \qquad C_{\alpha\beta\gamma\delta}\big|_{\mathscr{B}} = 0, \qquad C_{\alpha\beta\gamma\delta}\big|_{\mathscr{I}^{+}} \approx 0$$

The Weyl tensor is small at both the beginning and the end of each aeon, but the *direction* of entropy increase is well-defined within the aeon: gravitational clumping grows $C_{\alpha\beta\gamma\delta}$ from the initial state, producing the arrow of time.

### 9.5 Objection: Is Information Really Lost?

This is one of the most controversial aspects of CCC. Mainstream quantum mechanics (and the AdS/CFT correspondence in string theory) strongly suggests that black hole evaporation is a **unitary** process---information is preserved. If information is not lost, the entropy of the Hawking radiation equals that of the original black hole, and the entropy "reset" does not occur. Penrose explicitly rejects unitarity in this context, proposing instead that quantum gravity introduces a fundamental information loss that is essential for CCC to work.

---

## 10. Mathematical Details of the Conformal Crossover

### 10.1 Setup

Consider the crossover surface $\mathscr{X}$ separating the previous aeon $\hat{\mathscr{A}}$ (with physical metric $\hat{g}_{\mu\nu}$) from the next aeon $\check{\mathscr{A}}$ (with physical metric $\check{g}_{\mu\nu}$). Let $g_{\mu\nu}$ be the smooth bridging metric in a neighbourhood of $\mathscr{X}$.

**Conformal relations:**

$$\hat{g}_{\mu\nu} = \hat{\Omega}^{2}\, g_{\mu\nu}, \qquad \check{g}_{\mu\nu} = \check{\Omega}^{2}\, g_{\mu\nu}$$

**Boundary behaviour:**

$$\hat{\Omega} \to \infty, \qquad \check{\Omega} \to 0 \qquad \text{as one approaches } \mathscr{X}$$

**Reciprocal hypothesis:**

$$\hat{\Omega}\, \check{\Omega} = -1 \qquad \text{on } \mathscr{X}$$

### 10.2 The Phantom Field

The conformal factor $\hat{\Omega}$ (or equivalently $\check{\Omega}$) is not freely specifiable. Penrose proposes that it satisfies a **phantom field equation**---a second-order hyperbolic equation determined by the matter content and geometry of the previous aeon.

The philosophy of CCC requires that rest mass $\mu$ plays no role near $\mathscr{X}$. The rest-mass condition is expressed through a quantity $\Pi_{\mu}$ built from the conformal factor:

$$\Pi_{\mu} = \nabla_{\mu}\bigl(\hat{\Omega}^{-1}\bigr) = -\hat{\Omega}^{-2}\,\nabla_{\mu}\hat{\Omega}$$

This quantity $\Pi_{\mu}$ is **smooth through the crossover** and is **invariant under the reciprocal hypothesis** $\hat{\Omega} \to -\check{\Omega}^{-1}$.

The phantom field equation is a wave equation for $\hat{\Omega}$ (or $\hat{\Omega}^{-1}$) that encodes how the matter content of the previous aeon determines the conformal factor---and hence, via the reciprocal hypothesis, the initial data for the next aeon. The equation takes the schematic form of a conformally coupled scalar field equation:

$$\Box\phi + \frac{1}{6}\,R\,\phi - 4\alpha\,\phi^{3} = 0$$

where $\phi$ is related to the conformal factor and $\alpha$ is a coupling constant related to $\Lambda$.

### 10.3 Conformal Scalar Field Formulation

The conformally invariant scalar field equation in four dimensions is:

$$\Box\phi + \frac{1}{6}\, R\, \phi = 0$$

(with potential nonlinear $\phi^3$ self-interaction for the generalised case). Under $\tilde{g}_{\mu\nu} = \Omega^{2}\, g_{\mu\nu}$ and $\tilde{\phi} = \Omega^{-1}\, \phi$, both the equation and the associated pseudo-stress-energy tensor

$$D_{\mu\nu} = 4\,\phi_{\mu}\,\phi_{\nu} - g_{\mu\nu}\bigl(g^{\alpha\beta}\,\phi_{\alpha}\,\phi_{\beta}\bigr) - 2\,\phi\,\nabla_{\mu}\phi_{\nu} + 2\,\phi^{2}\, L_{\mu\nu} + 2\alpha\,\phi^{4}\, g_{\mu\nu}$$

(where $L_{\mu\nu} = -\frac{1}{2}(R_{\mu\nu} - \frac{1}{6}R\, g_{\mu\nu})$ is the Schouten tensor) are conformally invariant:

$$D_{\mu\nu}(\tilde{\phi},\, \tilde{g}_{\alpha\beta},\, \alpha) = \Omega^{-2}\, D_{\mu\nu}(\phi,\, g_{\alpha\beta},\, \alpha)$$

This conformal scalar field provides a model for the phantom field that carries information across the crossover.

### 10.4 The FLRW Toy Model

For the simplest case of FLRW cosmologies with radiation and $\Lambda > 0$, the Friedmann equation in conformal time $\tau$ is:

$$\left(\frac{da}{d\tau}\right)^{2} = \frac{\kappa\beta}{3} - k\, a^{2} + \frac{\Lambda}{3}\, a^{4}$$

where $a(\tau)$ is the scale factor, $\kappa = 8\pi G$, $\beta$ is the radiation constant ($\rho\, a^{4} = \beta = \text{const}$), and $k \in \{-1, 0, +1\}$ is the spatial curvature.

The aeon transition is governed by the remarkable relation:

$$\boxed{a(\tau_{F} - \tau)\; a(\tau) = \left(\frac{\kappa\beta}{\Lambda}\right)^{1/2}}$$

where $\tau_{F}$ is the conformal time at future infinity. This equation shows that the scale factor at "time before the end" is reciprocally related to the scale factor at "time after the beginning," mediated by the combination $\kappa\beta/\Lambda$. It is the concrete realisation of the reciprocal hypothesis for FLRW spacetimes.

### 10.5 The Rescaled Weyl Tensor

Friedrich's conformal field formulation introduces the **rescaled Weyl tensor**:

$$d_{\alpha\beta\gamma\delta} := \Theta^{-1}\, C_{\alpha\beta\gamma\delta}$$

where $\Theta$ is the conformal compactification factor ($\Theta \to 0$ at $\mathscr{I}^{+}$). This rescaled tensor remains smooth at $\mathscr{I}^{+}$ and satisfies the conservation equation:

$$\nabla^{\delta}\, d_{\alpha\beta\gamma\delta} = 0$$

The finiteness of $d_{\alpha\beta\gamma\delta}$ at conformal infinity guarantees that gravitational radiation information can be transmitted smoothly through the crossover.

### 10.6 Conformal Time and the "74% Result"

In the FLRW toy model with observationally determined cosmological parameters, the universe at the present epoch is approximately **74% of the way through its total conformal time** to $\mathscr{I}^{+}$. This means that in conformal terms, we are well past the midpoint of our aeon's history---though in proper time, an infinite duration remains.

---

## 11. Criticisms and Open Problems

### 11.1 The Electron Mass Problem

The most immediate objection to CCC is the stability of the electron. The electron is the lightest charged lepton, and no decay mode is known or expected in the Standard Model. Electric charge is absolutely conserved (to the best of our knowledge), so the electron cannot simply decay into massless products while conserving charge. Penrose's proposed "mass fade-out" converts electrons into massless charged particles, but such particles (travelling at the speed of light) have no precedent in known physics and raise serious theoretical difficulties. As Sean Carroll has noted: converting electrons to massless charged particles does not solve the problem---it merely replaces it with an equally problematic entity.

### 11.2 Information Loss in Black Holes

CCC **requires** that information is genuinely lost during black hole evaporation---that Hawking radiation is thermal and does not encode the infalling quantum state. This contradicts the now-mainstream view (supported by AdS/CFT) that black hole evaporation is unitary. If information is preserved, the entropy "reset" at the crossover fails, and the thermodynamic argument for CCC collapses.

Recent quantum information analyses (2023) have shown that the assumed loss of degrees of freedom inside black holes is incompatible with the standard quantum notion of entropy, challenging the entropy-reset mechanism.

### 11.3 The Conformal Factor Ambiguity

A fundamental open problem: the conformal factor $\hat{\Omega}$ connecting the two aeons is not uniquely determined. Proposals by Tod, Newman, and Nurowski disagree with one another and with Penrose's original assumptions. Nurowski (2023) showed that certain conformal factor choices proposed by Penrose are inconsistent with the phantom field equation, and only specific relations survive scrutiny. This remains a major hurdle: without a unique prescription for $\hat{\Omega}$, CCC lacks predictive power at the level of the crossover.

### 11.4 No Explanation for Inflation-Like Phenomena

The standard $\Lambda$CDM model uses cosmic inflation to explain:
- The flatness problem (why $k \approx 0$).
- The horizon problem (why the CMB is isotropic across causally disconnected regions).
- The origin of the nearly scale-invariant primordial power spectrum.

CCC addresses the horizon problem (causal contact exists in the previous aeon) but does **not** provide a mechanism for generating the observed nearly scale-invariant perturbation spectrum. Penrose is explicitly critical of inflation, but CCC has not yet demonstrated that it can reproduce the detailed CMB power spectrum predictions that inflation matches.

### 11.5 Dark Matter and Baryon Asymmetry

CCC does not address:
- The nature of dark matter.
- The observed matter-antimatter asymmetry (baryon asymmetry).
- The detailed particle physics of the Standard Model.

These are fundamental cosmological puzzles that any complete alternative to the standard model must eventually confront.

### 11.6 Observational Evidence Is Disputed

As discussed in Section 8, the claimed CMB signatures (concentric circles and Hawking points) have not survived independent scrutiny. Three groups found no significant concentric circles (2010--2011), and the Hawking points claim (2018) was challenged as consistent with $\Lambda$CDM once the look-elsewhere effect is included (2020). No CCC prediction has achieved consensus acceptance in the observational community.

### 11.7 Quantum Gravity

CCC operates entirely within classical general relativity (plus semiclassical Hawking radiation). The crossover surface is treated classically, with no input from quantum gravity. It is plausible that quantum gravitational effects at or near the Planck scale fundamentally alter the crossover geometry in ways that CCC does not account for. Loop quantum gravity, for instance, resolves the Big Bang singularity via a quantum bounce rather than a conformal identification, suggesting that the CCC picture may be an approximation that breaks down precisely where it matters most.

### 11.8 Carroll's Objection: The Physical Mechanism

Sean Carroll has raised the question: even granting the mathematical possibility of conformally mapping the late universe onto the early universe, **what physical process actually causes this to happen?** The Steinhardt-Turok ekpyrotic/cyclic model, for example, provides a concrete dynamical mechanism (colliding branes) for the cyclic transition. Carroll argues that CCC lacks an analogous dynamical explanation---it identifies two conformally equivalent states but does not explain *why* the transition occurs.

---

## 12. Key Equations (Collected)

### Conformal Rescaling

$$\tilde{g}_{\mu\nu} = \Omega^{2}\, g_{\mu\nu}$$

### Reciprocal Hypothesis

$$\hat{\Omega}\, \check{\Omega} = -1$$

### Two Physical Metrics

$$\hat{g}_{\mu\nu} = \hat{\Omega}^{2}\, g_{\mu\nu}, \qquad \check{g}_{\mu\nu} = \check{\Omega}^{2}\, g_{\mu\nu}$$

$$\check{g}_{\mu\nu} = \hat{\Omega}^{-4}\, \hat{g}_{\mu\nu}$$

### Weyl Tensor Conformal Invariance

$$\tilde{C}^{\alpha}{}_{\beta\gamma\delta} = C^{\alpha}{}_{\beta\gamma\delta}$$

$$\tilde{C}_{\alpha\beta\gamma\delta} = \Omega^{2}\, C_{\alpha\beta\gamma\delta}$$

### Weyl Curvature Hypothesis

$$C_{\alpha\beta\gamma\delta}\big|_{\mathscr{B}} = 0$$

### Ricci Tensor Transformation

$$\tilde{R}_{\mu\nu} = R_{\mu\nu} - 2\nabla_{\mu}\Upsilon_{\nu} + 2\Upsilon_{\mu}\Upsilon_{\nu} - g_{\mu\nu}\bigl(\nabla_{\alpha}\Upsilon^{\alpha} + 2\Upsilon_{\alpha}\Upsilon^{\alpha}\bigr)$$

where $\Upsilon_{\mu} = \Omega^{-1}\nabla_{\mu}\Omega$.

### Ricci Scalar Transformation

$$\tilde{R} = \Omega^{-2}\, R - 6\,\Omega^{-3}\,\Box\Omega$$

### Conformal Boundary Condition ($\Lambda > 0$)

$$g^{\mu\nu}\,\partial_{\mu}\Theta\,\partial_{\nu}\Theta\big|_{\mathscr{I}^{+}} = \frac{\Lambda}{3}$$

### Einstein Equation (Vacuum + $\Lambda$)

$$R_{\mu\nu} = \Lambda\, g_{\mu\nu}$$

### Weyl Spinor Field Equation

$$\nabla^{AA'}\Psi_{ABCD} = 0$$

### Weyl Spinor Decomposition

$$C_{\mu\nu\rho\sigma} = \Psi_{ABCD}\, \varepsilon_{A'B'}\, \varepsilon_{C'D'} + \varepsilon_{AB}\, \varepsilon_{CD}\, \bar{\Psi}_{A'B'C'D'}$$

### Twistor Equation

$$\nabla_{A'(A}\varpi^{B)} = 0$$

### Killing Spinor Equation

$$\nabla_{A'(A}\kappa^{BC)} = 0$$

### Spin Reduction (Gravitational to Electromagnetic)

$$\phi_{AB} = \Psi_{ABCD}\,\kappa^{CD}, \qquad \nabla^{AA'}\phi_{AB} = 0$$

### Friedmann Equation (FLRW + Radiation + $\Lambda$, Conformal Time)

$$\left(\frac{da}{d\tau}\right)^{2} = \frac{\kappa\beta}{3} - k\, a^{2} + \frac{\Lambda}{3}\, a^{4}$$

### Aeon Transition Relation (FLRW Toy Model)

$$a(\tau_{F} - \tau)\; a(\tau) = \left(\frac{\kappa\beta}{\Lambda}\right)^{1/2}$$

### Bekenstein-Hawking Entropy

$$S_{\text{BH}} = \frac{k_{B}\, c^{3}\, A}{4\, G\, \hbar}$$

### Hawking Temperature

$$T_{H} = \frac{\hbar\, c^{3}}{8\pi\, G\, M\, k_{B}}$$

### Rescaled Weyl Tensor (Friedrich)

$$d_{\alpha\beta\gamma\delta} = \Theta^{-1}\, C_{\alpha\beta\gamma\delta}, \qquad \nabla^{\delta}\, d_{\alpha\beta\gamma\delta} = 0$$

### Conformally Invariant Scalar Field Equation

$$\Box\phi + \frac{1}{6}\, R\, \phi - 4\alpha\,\phi^{3} = 0$$

### Conformal Scalar Field Pseudo-Stress-Energy

$$D_{\mu\nu} = 4\,\phi_{\mu}\,\phi_{\nu} - g_{\mu\nu}\bigl(g^{\alpha\beta}\,\phi_{\alpha}\,\phi_{\beta}\bigr) - 2\,\phi\,\nabla_{\mu}\phi_{\nu} + 2\,\phi^{2}\, L_{\mu\nu} + 2\alpha\,\phi^{4}\, g_{\mu\nu}$$

$$D_{\mu\nu}(\tilde{\phi},\, \tilde{g},\, \alpha) = \Omega^{-2}\, D_{\mu\nu}(\phi,\, g,\, \alpha)$$

### Starobinsky Expansion Near $\mathscr{I}^{+}$

$$h_{ij} = a_{ij} + e^{-2Ht}\, b_{ij} + e^{-3Ht}\, c_{ij} + \cdots$$

$$b_{ij} = H^{-2}\Bigl(\rho_{ij} - \tfrac{1}{4}\,\rho\, a_{ij}\Bigr)$$

### Epsilon Spinor Conformal Scaling

$$\tilde{\varepsilon}_{AB} = \Omega\, \varepsilon_{AB}, \qquad \tilde{\varepsilon}^{AB} = \Omega^{-1}\, \varepsilon^{AB}$$

### Conformal Weight

$$Q \to \tilde{Q} = \Omega^{w}\, Q$$

where $w$ is the conformal weight of $Q$.

---

## Appendix: Timeline of Key CCC Publications

| Year | Authors | Title / Description |
|------|---------|---------------------|
| 1979 | Penrose | Weyl curvature hypothesis first proposed (in *Singularities and Time-Asymmetry*) |
| 2006 | Penrose | "Before the Big Bang" --- first statement of CCC (EPAC Proceedings) |
| 2009 | Penrose | "The Basic Ideas of Conformal Cyclic Cosmology" --- extended exposition |
| 2010 | Penrose | *Cycles of Time* --- book-length treatment |
| 2010 | Gurzadyan, Penrose | Claimed detection of concentric circles in WMAP/BOOMERanG data |
| 2010--2011 | Wehus-Eriksen, Moss-Scott-Zibin, Hajian | Independent rebuttals of concentric circles claim |
| 2013 | Gurzadyan, Penrose | Updated analysis of low-variance circles |
| 2015 | Tod | "The Equations of CCC" --- systematic derivation of field equations |
| 2018 | An, Meissner, Nurowski, Penrose | "Apparent evidence for Hawking points in the CMB Sky" |
| 2020 | Jow, Scott | Reanalysis finding Hawking points consistent with $\Lambda$CDM |
| 2023 | Nurowski | "Toward fixing a framework for CCC" --- constraining conformal factors |
| 2023 | Various | Quantum information analyses of CCC entropy arguments |
| 2025 | Meissner, Penrose | "The Physics of CCC" --- gravitational wave epoch, spinor methods |

---

*This document is a research-grade reference summary. It synthesises material from Penrose's published works, the technical literature by Tod, Nurowski, Friedrich, and collaborators, and the observational analyses by Gurzadyan, An, Meissner, and others. For definitive statements, the reader should consult the original sources cited above.*
