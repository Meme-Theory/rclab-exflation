# The Causal Set Approach to Quantum Gravity

**Author(s):** S. Surya
**Year:** 2019
**Journal:** Living Reviews in Relativity 22, 5

---

## Abstract

Causal set theory, developed by Sorkin and others, proposes that spacetime is fundamentally discrete at the Planck scale, with discreteness manifest as a finite set of events. Rather than assuming a discrete lattice structure (which breaks Lorentz invariance), causal set theory preserves the causal ordering of events — a Lorentz-invariant concept. A spacetime emerges in the continuum limit as a densely packed poset (partially ordered set) of causally-ordered events. This comprehensive review covers the causal set program's foundations, recent developments, and observational tests, including Sorkin's prediction of a spontaneous localization ("stochastic collapse") mechanism that would produce a specific spectrum of deviations from quantum mechanics at low energies. The review also discusses how causal sets naturally incorporate cosmological predictions, including anomalies in the cosmic microwave background and the coincidence problem in dark energy.

---

## Historical Context

Quantum gravity has long been plagued by the question: "What is the nature of spacetime at Planck scales?" Three main avenues have emerged:

1. **String theory**: Extra dimensions, dualities, holography.
2. **Loop quantum gravity**: Quantized geometry, spin networks, spin foams.
3. **Causal set theory**: Discrete events ordered causally, no preferred spacetime metric at the Planck scale.

Causal set theory is unique in its minimalism: it assumes only that reality is a **poset** (partially ordered set). Two events are either causally connected (one can influence the other) or causally disconnected. No metric, no topology, no manifold — just partial order.

The program was initiated by Sorkin in the 1980s. Key inspirations include:

- **Chronology protection**: Any discrete model must preserve causality (no closed timelike curves).
- **Manifold hypothesis**: At large scales, spacetime should look like a smooth 4D Lorentzian manifold — the poset should have a continuum limit.
- **No preferred frame**: Causal structure is frame-independent, so the discrete structure should respect Lorentz invariance (or at least, Lorentz violation should be suppressed as the continuum limit is approached).

Surya's 2019 review synthesizes two decades of development, covering:
- Mathematical foundations of posets and causality.
- Emergence of spacetime from a causal set.
- Predictions for cosmology (Sorkin's CC prediction, anomalies in the CMB).
- Experimental tests of Lorentz invariance violations.
- Computational methods for causal set simulations.

---

## Key Arguments and Derivations

### Poset and Causal Structure

A causal set is a finite or countably infinite poset $(C, \prec)$ where $x \prec y$ means "event $x$ causally precedes event $y$" (i.e., a causal signal could travel from $x$ to $y$). The relation $\prec$ is:
- **Reflexive**: $x \prec x$ (trivially).
- **Transitive**: if $x \prec y$ and $y \prec z$, then $x \prec z$.
- **Acyclic**: no closed loops (no $x \prec y \prec \ldots \prec x$).
- **Locally finite**: any interval $\{z : x \prec z \prec y\}$ contains finitely many elements.

These properties encode causality without assuming a spacetime manifold or metric.

### Emergence of Spacetime

Starting from a causal set, spacetime is reconstructed (in a continuum limit) by:

1. **Sprinkling a Poisson point process** into a Lorentzian manifold: randomly place $N$ events in a 4-volume $V$ with density $\rho = N/V$ (the "fundamental scale").

2. **Inducing the causal order** from the manifold's light-cone structure: two sprinkled events are related in the causal set if and only if they are causally connectable in the manifold.

3. **Recovering the metric** from the causal structure: the spacetime distance $d(x,y)$ between events can be inferred from the number of causal-set elements in the interval $[x, y]$ (the "layer size").

This "reverse" procedure (manifold → causal set → manifold) is called the **manifold hypothesis**: the continuum spacetime emerges from a densely-packed causal set.

Mathematically, the distance is recovered via:

$$d(x,y) \sim \frac{1}{\sqrt{\rho}} \sqrt{\text{Card}(\{z : x \prec z \prec y\})}$$

where $\text{Card}$ denotes cardinality. This is the **Brightwell-Gregory formula**, validated numerically for simple spacetimes (Minkowski, de Sitter).

### Sorkin's Cosmological Constant Prediction

Sorkin observed that a random causal set has a **zero average scalar curvature** (Ricci scalar $R = 0$ on average). However, the **variance** in the scalar curvature is non-zero. This variance corresponds to vacuum fluctuations in the curvature.

The critical insight: the energy density of these vacuum fluctuations is:

$$\rho_\Lambda \sim \frac{1}{\rho} \sim \left(\sqrt{\hbar G / c^3}\right)^2 \cdot \frac{1}{(\text{Planck length})^4}$$

In natural units, this is $\rho_\Lambda \sim 10^{113}$ J/m³ — the notorious "worst prediction in physics," disagreeing with observations by 120 orders of magnitude.

**But Sorkin's resolution**: The observed CC might not be the fundamental CC from causal set quantum fluctuations. Instead, it could be a **dynamical cosmological constant** arising from matter or dark energy evolution. The causal set prediction sets an **upper bound** on the true CC, testable through precision cosmology.

Alternatively, if the true CC is indeed $10^{-47}$ GeV⁴ (as observed), then the causal set's vacuum CC of $10^{113}$ GeV⁴ must be **cancelled by a bare CC** in the action, fine-tuned to 120 decimal places — suggesting that causal sets, too, require a solution to the CC problem.

### Observational Predictions: CMB Anomalies

Causal sets are discrete, and this discreteness is stamped into spacetime as a slight non-smoothness. The review discusses how causal-set-induced curvature fluctuations could produce:

1. **Excess power at the lowest multipoles** ($\ell \lesssim 10$) in the cosmic microwave background's angular power spectrum. This matches the observed **Planck anomaly** (the north-south asymmetry and hemisphere temperature difference).

2. **Non-Gaussian signatures** in the CMB primordial bispectrum $f_{NL}$. Planck constraints: $f_{NL}^{\text{local}} < 10$; causal sets predict a small positive contribution, potentially detectable with next-generation experiments.

3. **Ultra-high-energy cosmic ray cutoff**: If causal-set discreteness induces Lorentz violation at the Planck scale, the GZK cutoff in cosmic-ray spectra would be slightly modified. The review notes that current data are consistent with standard GZK, placing limits on the causal-set scale.

### Stochastic Collapse and Spontaneous Localization

One of Sorkin's boldest predictions is that causal-set discreteness induces **spontaneous collapse** (spontaneous localization) of the wave function — a mechanism by which macroscopic objects spontaneously decohere, explaining the quantum-to-classical transition.

The rate of collapse is:

$$\Gamma_{\text{collapse}} \sim \sqrt{\rho} \sim \frac{1}{\text{Planck length}}$$

For a macroscopic object composed of $N \sim 10^{23}$ atoms, the collapse time is $\tau_c \sim 10^{-16}$ s — rapid enough to suppress quantum superpositions on the scale of millimeters.

Experiments testing spontaneous collapse (e.g., cavity optomechanics, atom interferometry) can indirectly probe causal sets by searching for collapse-induced heating or decoherence. The review summarizes current limits, which are beginning to constrain the causal-set hypothesis.

---

## Key Results

1. **Continuum limit validity**: For sufficiently dense causal sets (density $\rho \gtrsim 10^{20}$ cm⁻⁴, corresponding to a Planck-scale discretization), the manifold hypothesis is well-approximated — spacetime emerges as a smooth continuum. At lower densities, signatures of discreteness appear.

2. **Cosmological constant upper bound**: $\rho_\Lambda^{\text{causal-set}} \sim 10^{113}$ GeV⁴, vastly exceeding observations. However, this sets a theoretical ceiling; observational CC constraints feed back into causal-set phenomenology.

3. **CMB predictions**: The theory predicts excess low-$\ell$ power (consistent with Planck anomalies) and constraints $f_{NL} \sim 0.1$–$1$ (next-generation CMB experiments like CMBS4 will test this).

4. **Lorentz violation suppression**: In the continuum limit, Lorentz violation is suppressed (by Hossenfelder's no-go theorem, the discrete structure cannot be perfectly Lorentz-invariant, but the violation scales as $\sim \rho^{-1/2}$ — tiny for dense causal sets).

5. **Collapse rate predictions**: Spontaneous collapse would induce decoherence at a rate $\sim 10^{11}$ Hz for gram-scale objects — currently undetectable but within reach of next-decade experiments.

---

## Impact and Legacy

Causal set theory is one of the most mathematically rigorous approaches to quantum gravity. Its minimalist assumptions (only causality, no background metric) are philosophically appealing. However, its observational predictions remain largely untested:

**Strengths**:
- Mathematically elegant and self-contained.
- Makes concrete predictions (CMB anomalies, spontaneous collapse, CC upper bound).
- Respects causality at the fundamental level.

**Weaknesses**:
- No clear path to matter coupling (how do the Standard Model fields arise from a poset?).
- The continuum limit is not fully proven; some argue the limit is ill-defined or ambiguous.
- Spontaneous collapse is controversial; many physicists reject it philosophically.
- The CC problem persists; causal sets do not solve it.

---

## Connection to Phonon-Exflation Framework

Phonon-exflation and causal set theory represent two complementary approaches to quantum gravity and cosmology:

### Common Ground

1. **Discrete underlying structure**: Both frameworks posit discreteness at the Planck scale, not assumed at higher scales.

2. **Emergence of spacetime**: Both argue that continuous 4D spacetime emerges from a more fundamental structure (causal poset vs. compactified internal geometry).

3. **No inflaton field**: Neither requires a scalar field for inflation; the mechanism is intrinsic.

4. **Causality-preserving**: Both preserve causal structure (causality is respected in phonon-exflation's light-cone structure; causality defines the causal set).

### Critical Differences

1. **Dimensionality**: Causal sets are discrete in 4D spacetime itself; phonon-exflation has a continuous 4D spacetime with discrete structure in the internal 6D (compactified) directions.

2. **Symmetry principles**: Causal sets rely solely on causality; phonon-exflation uses the full power of non-commutative geometry and the spectral action, which encodes gauge symmetries (electromagnetism, weak, strong interactions).

3. **Particle spectrum**: Causal sets have no built-in mechanism for the Standard Model; phonon-exflation derives particle quantum numbers from the Dirac operator's spectrum on $SU(3)$.

4. **Cosmological constant**: Causal sets predict an absurdly large CC that must be cancelled; phonon-exflation's spectral action naturally accommodates a small, emergent CC (through instanton physics in Session 38).

### Unification Opportunity

Could phonon-exflation incorporate causal-set ideas? Possibly:

- **The internal 6D space could have a causal structure** at the Planck scale, with 4D spacetime emerging as before.
- **Sorkin's CC prediction becomes a prediction for the internal geometry**, which affects the spectral action's constants.
- **Spontaneous collapse could be a feature of the BCS condensate transition**, where the macroscopic phase becomes decoherent during the transit (Session 38 paradigm).

**Key difference**: Phonon-exflation grounds the discrete structure in a concrete algebraic object (the Dirac operator on $SU(3)$ with a spectral action), whereas causal sets remain largely abstract. This gives phonon-exflation more predictive power — mass ratios, coupling constants, etc. — but also makes it more constrained (and thus more testable).

**Empirical test**: If causal sets are correct, CMB anomalies at low $\ell$ should be correlated with a tiny non-Gaussian signature ($f_{NL} \sim 1$). If phonon-exflation is correct, such anomalies would be traced to the internal geometry and linked to neutrino masses and mixing angles (PMNS matrix). Future high-precision CMB experiments will discriminate.

