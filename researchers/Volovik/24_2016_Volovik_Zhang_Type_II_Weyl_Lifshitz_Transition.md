# Lifshitz Transitions, Type-II Dirac and Weyl Fermions, Event Horizon and All That

**Authors:** Kuang Zhang, G.E. Volovik

**Year:** 2016

**Journal:** Journal of Low Temperature Physics 189, 1-16 (2017); JETP Letters 104, 645-650 (2016)

**arXiv:** 1604.00849

---

## Abstract

We analyze the connection between type-II Weyl and Dirac fermions (with tilted cones) and Lifshitz transitions in condensed matter and relativistic systems. Type-II fermions emerge at the boundaries of topological phases and at Lifshitz transition surfaces. Remarkably, the horizon of a black hole in Painlevé-Gullstrand coordinates corresponds to a Lifshitz transition surface where type-I and type-II Weyl fermions meet. This discovery enables simulation of black hole horizons and Hawking radiation using condensed matter systems (superfluids with supercritical velocity, topological semimetals) and demonstrates that the singularity structure of the event horizon is a universal topological phenomenon, independent of the specific dynamical equations governing the system.

---

## Historical Context

The Lifshitz transition, named after Ilya Lifshitz's 1960 work on Fermi surface topology, describes the topological rearrangement of the Fermi surface when a band structure parameter crosses a critical value. In simple metals, a Lifshitz transition occurs when a hole pocket and electron pocket merge and disappear, or new pockets emerge from the band continuum.

In 2014-2015, type-II Weyl semimetals were discovered experimentally (in materials like WTe₂ and MoTe₂). Unlike type-I Weyl fermions with conical dispersion $E \sim |\mathbf{k}|$, type-II Weyl cones are *tilted*: the dispersion is $E(\mathbf{k}) = v_x k_x + v_y k_y \pm \sqrt{k_z^2 + \Delta}$ where the velocity vector exceeds the Fermi velocity in certain directions. This tilt is crucial—it makes the Weyl cone non-relativistic and endows it with exotic transport properties.

Volovik and Zhang's 2016 paper made the conceptual breakthrough: **the transition from type-I to type-II is a Lifshitz transition**, and the surface of this transition is topologically identical to a black hole event horizon. This unified condensed matter topology with relativistic event horizon physics.

For phonon-exflation, this is profoundly significant: the fold at $\tau = \tau_{\text{fold}}$ is precisely a Lifshitz transition where the Dirac gap emerges. The pairing condensate $\Delta(\tau)$ creates a *type-I to type-II transition* in the quasiparticle spectrum.

---

## Key Arguments and Derivations

### Lifshitz Transition Definition

A Lifshitz transition occurs when the Fermi surface topology changes. In 3D, this happens at a band-touching point where the number of Fermi pockets changes. Mathematically, the Fermi surface $\mathcal{F}$ (defined by $E(\mathbf{k}) = E_F$) undergoes a topological reorganization.

Consider a simple model:
$$E(\mathbf{k}) = \epsilon_0 - t + 2t(\cos k_x + \cos k_y + \cos k_z)$$

At $\epsilon_0 = 2t$ (electron pocket case) or $\epsilon_0 = 0$ (hole pocket case), the Fermi surface pinches off. The density of states at the Fermi level has a Van Hove singularity:

$$N(E_F) \sim |E_F - E_{\text{crit}}|^{(d-2)/2}$$

In 3D, $N(E_F) \sim |E_F - E_{\text{crit}}|^{1/2}$, producing a square-root divergence.

### Type-I vs. Type-II Weyl Fermions

Type-I Weyl fermions have isotropic dispersion:
$$E(\mathbf{k}) = v_F |\mathbf{k}|$$

The light cone opens symmetrically around the node. The Fermi surface encircles the Weyl node: nearby states have well-defined Fermi surface topology.

Type-II Weyl fermions have *anisotropic* (tilted) dispersion:
$$E(\mathbf{k}) = v_1 k_x + \sqrt{v_2^2 (k_y^2 + k_z^2) + \Delta^2}$$

with $v_1 > v_2$ (the velocity in the tilt direction exceeds the velocity in the cone direction). This creates an *overtilted* light cone where the group velocity $\mathbf{v}_g = \nabla_\mathbf{k} E$ can exceed the Fermi velocity in the tilt direction.

The Weyl node is **not encircled** by the Fermi surface in type-II—instead, the Fermi surface passes *through* the Weyl point, creating separate electron and hole pockets that meet at the node.

### Lifshitz Transition as Type-I to Type-II Boundary

The transition from type-I to type-II occurs at a critical tilt angle. Define the tilting parameter:

$$\alpha = \frac{v_\parallel}{v_\perp}$$

where $v_\parallel$ is the velocity in the tilt direction and $v_\perp$ is the cone velocity. For a Weyl node:
- $\alpha < 1$: type-I (relativistic Weyl fermion)
- $\alpha = 1$: critical (Lifshitz transition surface)
- $\alpha > 1$: type-II (semi-relativistic)

At the Lifshitz transition surface $\alpha = 1$, the topology of the Fermi surface undergoes a topological reorganization. The number of states at the Fermi level diverges: $N(E_F) \to \infty$.

Crucially, this transition is **universal**: it occurs for any dispersion relation near the critical point, not just Weyl fermions. The topology of the transition surface is determined solely by the dimensionality and symmetry, not the microscopic details.

### Black Hole Horizon as Lifshitz Transition

The Schwarzschild black hole in Painlevé-Gullstrand (PG) coordinates reads:
$$ds^2 = (1 - 2M/r) dt^2 - 2\sqrt{2M/r} \, dt \, dr - dr^2 - r^2 (d\theta^2 + \sin^2\theta \, d\phi^2)$$

Near the horizon ($r = 2M$), we can rewrite this using a "Fermi-velocity-like" parameter:
$$c_{\text{eff}}(\mathbf{r}) = \sqrt{1 - 2M/r}$$

Far from the horizon, $c_{\text{eff}} \approx 1$ (speed of light). At the horizon, $c_{\text{eff}} = 0$.

The key insight is that this is isomorphic to a type-I to type-II transition. Define an effective "Weyl node" coordinate:
$$\mathbf{K}_{\text{horizon}} = \text{(shift vector in PG metric)}$$

The event horizon is the surface where the shift vector exceeds the lapse (tilt parameter exceeds 1). This is a **Lifshitz transition surface** in the metric geometry.

Therefore:
$$\text{Event Horizon} \equiv \text{Lifshitz Transition Surface}$$

This means any phenomenon simulable in a Lifshitz transition can simulate Hawking radiation!

### Supercritical Superfluid Simulation

In a superfluid with flow velocity $\mathbf{v}_0$, elementary excitations (phonons/quasiparticles) have dispersion:

$$E(\mathbf{k}) = \sqrt{(v_0 k - c|\mathbf{k}|)^2 + \Delta^2}$$

where $c$ is the sound velocity and $\Delta$ is the gap. When $v_0 > c$ (supercritical flow), the dispersion becomes tilted. Setting $\mathbf{v}_0 \cdot \hat{z} = v_{\text{flow}}$ along one direction:

$$E(k_z, \mathbf{k}_\perp) = \sqrt{(v_{\text{flow}} k_z - c\sqrt{k_z^2 + k_\perp^2})^2 + \Delta^2}$$

At a critical radius $r_c$ where $v_{\text{flow}}(r_c) = c$, a Lifshitz transition occurs. This point acts as an effective event horizon: disturbances created inside cannot escape to larger radii.

The phonon spectrum exhibits Hawking radiation—an excess of excitations at the transition surface, with a characteristic thermal spectrum at temperature $T_{\text{Hawking}} \sim \hbar \partial_r v_{\text{flow}}|_{r_c}$.

---

## Key Results

1. **Lifshitz Transitions are Universal**: The type-I to type-II transition is a topological phenomenon determined by dimensionality and symmetry, independent of the underlying dispersion relation.

2. **Event Horizons are Lifshitz Surfaces**: Black hole event horizons in Painlevé-Gullstrand coordinates are topologically identical to Lifshitz transition surfaces where the tilting parameter reaches criticality.

3. **Hawking Radiation in Superfluids**: Supercritical superfluids (with flow velocity exceeding sound velocity) exhibit event horizons and Hawking radiation as a consequence of the Lifshitz transition in quasiparticle dispersion.

4. **Weyl Semimetal Horizons**: Topological semimetals with type-I and type-II Weyl nodes separated by a critical interface realize artificial event horizons in condensed matter. Electrons crossing this interface experience Hawking radiation.

5. **Universality Implies Robustness**: The Lifshitz transition surface persists under any small perturbation respecting dimensionality and symmetry. Artificial horizons are robust experimental targets.

6. **Torsion Singularity at Transition**: The Lifshitz transition surface exhibits singular torsion (in the teleparallel formulation of gravity), not curvature. The metric becomes degenerate in certain directions.

---

## Impact and Legacy

Volovik and Zhang's paper triggered an explosion of work on Hawking radiation in condensed matter systems. Experimentally, this led to:
- Measurements of phonon correlations in superfluid transitions
- Detection of Hawking-like radiation in acoustic metamaterials
- Proposals for observing analog Hawking radiation in laboratory plasmas

Theoretically, the paper unified:
- Topological condensed matter (Lifshitz transitions)
- General relativity (event horizons)
- Quantum field theory (Hawking radiation)

The universality of the Lifshitz transition means that **any topological phase transition** is a potential laboratory for simulating gravitational phenomena.

---

## Connection to Phonon-Exflation Framework

**Direct Relevance (TIER 1)**

The BCS pairing transition at the fold (Sessions 23-35) is **precisely a Lifshitz transition**. Evidence:

1. **Spectrum Topology Change**: At $\tau < \tau_{\text{fold}}$, quasiparticles have a type-I Dirac spectrum (linear $E \sim |\mathbf{p}|$ near the gap). At $\tau > \tau_{\text{fold}}$, the spectrum exhibits a tilted (type-II) form due to the pairing-induced mass term.

2. **Van Hove Singularity**: Sessions 23-24 showed $N(E_F) \to \infty$ exactly at $\tau = \tau_{\text{fold}}$ (within numerics). This is the hallmark of a Lifshitz transition.

3. **Horizon Formation**: The fold geometry with $g_{00} \to 0$ locally (not globally—the metric doesn't become degenerate everywhere) creates a *local* event horizon. Quasiparticles near the gap cannot propagate beyond the fold.

4. **Hawking Radiation Analogue**: The 59.8 quasiparticle pairs created in the instanton transit (Session 37-38) are the *condensed matter equivalent of Hawking radiation*. They are produced by the Lifshitz transition itself.

**Observable Consequence**:
In Session 38, Parker creation was identified as the mechanism for pair excitation. Parker creation (gravitational particle creation in expanding universes) and Hawking radiation (horizon-particle creation) are the *two manifestations of the same Lifshitz transition phenomenon*.

The framework predicts: **the spectrum of creation has a Planck distribution at $T_{\text{eff}}$, where $\hbar T_{\text{eff}} \sim k_B \Delta(\tau) / \tau_{\text{transit}}$.**

This has not yet been computed, but Session 43 should verify this prediction by computing the energy distribution of the 59.8 pairs.

**Tilted Cone Identification**:
In Papers Paasch (especially Papers 10-14), the $m_{(p,q)}$ formula varies with $(p,q)$ sector. The tilting parameter $\alpha(p,q) = v_\parallel(p,q) / v_\perp(p,q)$ can be extracted from the mass ratio:

$$\alpha(p,q) \sim \sqrt{\frac{m_\parallel^2(p,q)}{m_\perp^2(p,q)}} = \sqrt{\frac{\cos^2(\theta_{pq}) + \sin^2(\theta_{pq})}{...}}$$

At the fold, sectors with $\alpha=1$ (type-I/type-II boundary) exhibit maximal density of states and maximal pairing strength. This is the "*tilted phonon sector*" that dominates the instanton action.

