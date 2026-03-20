# Penrose (1965): Gravitational Collapse and Space-Time Singularities

**Citation:** R. Penrose, "Gravitational Collapse and Space-Time Singularities," *Physical Review Letters* **14**, 57--59 (1965).
**DOI:** [10.1103/PhysRevLett.14.57](https://doi.org/10.1103/PhysRevLett.14.57)
**Nobel Prize:** 2020 Nobel Prize in Physics --- "for the discovery that black hole formation is a robust prediction of the general theory of relativity."

---

## 1. Historical Context: The Symmetry Problem

### 1.1 The State of the Art Before 1965

The Schwarzschild solution (1916) and its maximal analytic extension (Kruskal 1960, Szekeres 1960) contain a curvature singularity at $r = 0$, where the Kretschmann scalar $R_{\mu\nu\rho\sigma} R^{\mu\nu\rho\sigma} = 48 M^2 / r^6$ diverges. The Oppenheimer--Snyder (1939) dust-collapse solution similarly terminates at a singularity. However, these solutions all possess exact spherical symmetry, which raises a sharp question: **are the singularities genuine features of gravitational collapse, or mere artifacts of the idealized symmetry?**

The prevailing view in the Soviet school, led by Lifshitz and Khalatnikov (1963), was that singularities were *not* generic features of general solutions to Einstein's equations. Their analysis of perturbations around the Kasner solution led them to conclude:

> "The presence of a singularity in time is NOT a necessary property of cosmological models of the general theory of relativity."

That is, they believed that the measure-zero set of initial data leading to singularities would be unstable under perturbation, and that generic gravitational collapse would somehow avoid singular behavior. This position was later retracted: after Penrose's theorem, Belinskii, Khalatnikov, and Lifshitz (BKL, 1970) revisited their analysis and discovered the oscillatory ("mixmaster") approach to the singularity, confirming that singularities *do* appear in the general solution.

### 1.2 The Kerr Solution and the Question of Generality

The Kerr solution (1963) for a rotating black hole introduced additional structure --- an inner Cauchy horizon, ring singularity, and timelike character of the singularity in the maximally extended spacetime. This made the question of generality even more pressing. The Kerr singularity is qualitatively different from Schwarzschild: it is timelike rather than spacelike, and the maximal extension contains closed timelike curves. Whether *any* of these features survive perturbation away from exact axisymmetry was completely unknown.

### 1.3 Penrose's Breakthrough

Penrose's 1965 paper resolved this debate definitively by introducing an entirely new methodology. Rather than analyzing specific solutions or perturbation series, he deployed **global differential-geometric and topological methods** --- techniques that had never before been applied in general relativity. The key innovation was to prove the *existence* of singular behavior (geodesic incompleteness) without constructing the singularity explicitly, and without any symmetry assumptions whatsoever.

The paper is remarkably brief --- barely three pages --- yet it is arguably the most influential single result in general relativity since the field equations themselves.

---

## 2. The Trapped Surface

### 2.1 Intuitive Motivation

In flat Minkowski spacetime, consider a standard 2-sphere $S^2$ of radius $R$. The two families of future-directed null geodesics orthogonal to $S^2$ are:

- **Outgoing:** expanding (diverging away from the center), with positive expansion $\theta_{+} > 0$
- **Ingoing:** contracting (converging toward the center), with negative expansion $\theta_{-} < 0$

In a sufficiently strong gravitational field, the gravitational attraction can be so intense that *even the outgoing light rays are dragged inward* --- both families converge. This is the physical content of a trapped surface.

### 2.2 Formal Definition

Let $(M, g_{\mu\nu})$ be a spacetime. A **closed trapped surface** $\mathcal{T}$ is a compact (without boundary), spacelike, 2-dimensional submanifold of $M$ such that the expansions of *both* families of future-directed null geodesics orthogonal to $\mathcal{T}$ are everywhere negative on $\mathcal{T}$:

$$
\theta_{+} < 0 \quad \text{and} \quad \theta_{-} < 0 \quad \text{everywhere on } \mathcal{T}.
$$

Here $\theta_{\pm}$ are the **null expansion scalars** associated with the two independent future-directed null normal vector fields $\ell^{\mu}$ and $n^{\mu}$ to $\mathcal{T}$.

### 2.3 The Expansion Scalar

Given a null normal $k^{\mu}$ to $\mathcal{T}$ and the induced metric $q_{\mu\nu}$ on the 2-surface (the "screen space" orthogonal to $k^{\mu}$ and its conjugate null direction), the expansion is:

$$
\theta = q^{\mu\nu} \nabla_{\mu} k_{\nu} = \nabla_{\mu} k^{\mu} \big|_{\text{projected}}
$$

This measures the fractional rate of change of the cross-sectional area $\delta A$ of an infinitesimal beam of null geodesics:

$$
\theta = \frac{1}{\delta A} \frac{d(\delta A)}{d\lambda}
$$

where $\lambda$ is the affine parameter along the null geodesics.

### 2.4 Variants

| Surface Type | Condition |
|---|---|
| **Future trapped** | $\theta_{+} < 0$, $\theta_{-} < 0$ |
| **Marginally outer trapped (MOTS)** | $\theta_{+} = 0$, $\theta_{-} < 0$ |
| **Outer trapped** | $\theta_{+} < 0$, $\theta_{-} \leq 0$ |
| **Untrapped (normal)** | $\theta_{+} > 0$, $\theta_{-} < 0$ |
| **Anti-trapped** | $\theta_{+} > 0$, $\theta_{-} > 0$ |

The apparent horizon is the outermost marginally outer trapped surface (MOTS).

### 2.5 Trapped Surfaces in Schwarzschild

In the Schwarzschild spacetime with mass $M$, every 2-sphere of symmetry at $r < 2M$ (inside the event horizon) is a trapped surface. The event horizon $r = 2M$ is foliated by marginally trapped surfaces.

---

## 3. The Null Energy Condition

### 3.1 Statement

The **null convergence condition** (often called the null energy condition via the Einstein equations) requires:

$$
R_{\mu\nu} \, k^{\mu} k^{\nu} \geq 0 \quad \text{for all null vectors } k^{\mu}.
$$

### 3.2 Physical Interpretation via Einstein's Equations

Using the Einstein field equations $G_{\mu\nu} = 8\pi T_{\mu\nu}$ (in geometrized units $G = c = 1$), the null convergence condition is equivalent to:

$$
T_{\mu\nu} \, k^{\mu} k^{\nu} \geq 0 \quad \text{for all null vectors } k^{\mu}
$$

which is the **null energy condition** (NEC). This states that the energy density measured by any observer moving along a null ray is non-negative. For a perfect fluid with energy density $\rho$ and pressure $p$:

$$
\text{NEC} \iff \rho + p \geq 0.
$$

### 3.3 Hierarchy of Energy Conditions

The null energy condition is the *weakest* of the standard energy conditions:

$$
\text{DEC} \implies \text{WEC} \implies \text{NEC} \impliedby \text{SEC}
$$

where:
- **NEC:** $T_{\mu\nu} k^{\mu} k^{\nu} \geq 0$ for null $k^{\mu}$
- **WEC:** $T_{\mu\nu} u^{\mu} u^{\nu} \geq 0$ for timelike $u^{\mu}$ (implies NEC by continuity)
- **SEC:** $(T_{\mu\nu} - \tfrac{1}{2} T \, g_{\mu\nu}) u^{\mu} u^{\nu} \geq 0$ for timelike $u^{\mu}$ (implies NEC but not WEC)
- **DEC:** $T_{\mu\nu} u^{\mu} u^{\nu} \geq 0$ and $T^{\mu}{}_{\nu} u^{\nu}$ is non-spacelike, for timelike $u^{\mu}$

The fact that Penrose's theorem requires only the NEC --- the weakest condition --- makes the result maximally robust. Classical matter satisfies all of these conditions. Quantum fields can violate even the NEC (e.g., Casimir effect), but only locally and subject to quantum energy inequalities.

---

## 4. The Raychaudhuri Equation and the Focusing Theorem

### 4.1 Kinematic Decomposition

Given a congruence of null geodesics with tangent vector field $k^{\mu}$ ($k^{\mu} \nabla_{\mu} k^{\nu} = 0$, affinely parameterized), the transverse deformation tensor is:

$$
B_{\mu\nu} = \nabla_{\nu} k_{\mu}
$$

projected onto the 2-dimensional screen space orthogonal to $k^{\mu}$. This decomposes into:

$$
B_{\mu\nu} = \frac{1}{2} \theta \, q_{\mu\nu} + \sigma_{\mu\nu} + \omega_{\mu\nu}
$$

where:
- $\theta = q^{\mu\nu} B_{\mu\nu}$ is the **expansion** (trace part)
- $\sigma_{\mu\nu}$ is the **shear** (symmetric traceless part): $\sigma^2 \equiv \frac{1}{2}\sigma_{\mu\nu}\sigma^{\mu\nu} \geq 0$
- $\omega_{\mu\nu}$ is the **vorticity** (antisymmetric part): $\omega^2 \equiv \frac{1}{2}\omega_{\mu\nu}\omega^{\mu\nu} \geq 0$

### 4.2 The Raychaudhuri Equation for Null Geodesics

The evolution of the expansion along the congruence is governed by:

$$
\boxed{\frac{d\theta}{d\lambda} = -\frac{1}{2}\theta^2 - \sigma_{\mu\nu}\sigma^{\mu\nu} + \omega_{\mu\nu}\omega^{\mu\nu} - R_{\mu\nu}\,k^{\mu} k^{\nu}}
$$

This is a purely geometric identity --- it follows from the definition of curvature via the Ricci identity, without invoking any field equations.

**Comparison with the timelike version:** For a congruence of timelike geodesics with tangent $u^{\mu}$ in a 4-dimensional spacetime:

$$
\frac{d\theta}{d\tau} = -\frac{1}{3}\theta^2 - \sigma_{\mu\nu}\sigma^{\mu\nu} + \omega_{\mu\nu}\omega^{\mu\nu} - R_{\mu\nu}\,u^{\mu} u^{\nu}
$$

The coefficient $1/2$ (null) vs. $1/3$ (timelike) reflects the dimensionality of the transverse space (2 vs. 3).

### 4.3 The Focusing Theorem (Null Version)

**Theorem (Focusing).** Let $k^{\mu}$ be the tangent field of a hypersurface-orthogonal ($\omega_{\mu\nu} = 0$) congruence of null geodesics. If the null convergence condition holds ($R_{\mu\nu} k^{\mu} k^{\nu} \geq 0$), then the Raychaudhuri equation reduces to:

$$
\frac{d\theta}{d\lambda} \leq -\frac{1}{2}\theta^2
$$

**Consequence:** If at some initial affine parameter $\lambda_0$ the expansion is $\theta_0 = \theta(\lambda_0) < 0$, then:

$$
\frac{1}{\theta(\lambda)} \geq \frac{1}{\theta_0} + \frac{\lambda - \lambda_0}{2}
$$

which implies $\theta \to -\infty$ within finite affine parameter:

$$
\lambda - \lambda_0 \leq \frac{2}{|\theta_0|}
$$

Physically: **an initially converging congruence of null geodesics must develop a caustic (focal point) within finite affine parameter**, provided the null energy condition holds and the congruence is vorticity-free.

### 4.4 Relevance to Trapped Surfaces

For a trapped surface $\mathcal{T}$, the null geodesics orthogonal to $\mathcal{T}$ are automatically hypersurface-orthogonal (they are the generators of the null hypersurface emanating from $\mathcal{T}$), so $\omega_{\mu\nu} = 0$. Since $\theta < 0$ initially (by definition of trapped), the focusing theorem guarantees a caustic along every null geodesic emanating from $\mathcal{T}$ within affine parameter $\lambda \leq 2/|\theta_{\text{max}}|$, where $\theta_{\text{max}} = \max_{\mathcal{T}}(\theta_+, \theta_-)$ (the least negative initial expansion).

---

## 5. The Penrose Singularity Theorem (1965)

### 5.1 Precise Statement

**Theorem (Penrose, 1965).** *Let $(M, g_{\mu\nu})$ be a connected spacetime satisfying the following three conditions:*

1. **Null convergence condition:** $R_{\mu\nu} \, k^{\mu} k^{\nu} \geq 0$ for every null vector $k^{\mu}$.

2. **Global hyperbolicity with non-compact Cauchy surface:** There exists a non-compact Cauchy hypersurface $\Sigma$ (equivalently, the spacetime is globally hyperbolic and $\Sigma$ is non-compact).

3. **Trapped surface:** There exists a closed (compact, without boundary) future-trapped surface $\mathcal{T} \subset M$.

*Then $(M, g_{\mu\nu})$ is future null geodesically incomplete: there exists at least one inextendible future-directed null geodesic with finite affine length.*

### 5.2 Significance of Each Condition

| Condition | Role in the Proof | Physical Meaning |
|---|---|---|
| Null convergence | Ensures focusing via Raychaudhuri equation | Gravity is attractive for light; matter has non-negative null energy density |
| Non-compact Cauchy surface | Provides the topological obstruction for the contradiction | Spacetime is globally hyperbolic and spatially open (asymptotically flat or similar) |
| Closed trapped surface | Seeds the focusing; the initial $\theta < 0$ on a compact set | Gravitational field is strong enough that light is trapped |

### 5.3 Remarks on the Conditions

- **Global hyperbolicity** ensures well-posed initial value formulation and good causal structure (no closed causal curves, existence of maximal causal geodesics between causally related points).
- The **non-compact** Cauchy surface excludes spatially closed cosmologies. (The cosmological version, requiring a point with reconverging light cone rather than a trapped surface, is Hawking's 1967 theorem.)
- The conclusion is **null geodesic incompleteness**, not timelike geodesic incompleteness. These are logically independent notions.

---

## 6. Proof Strategy

The proof is by contradiction. Assume all three hypotheses hold and additionally assume the spacetime is **null geodesically complete** (every inextendible null geodesic has infinite affine length). We derive a contradiction.

### Step 1: Focusing Forces Conjugate Points

By the focusing theorem (Section 4.3), the null convergence condition combined with $\theta < 0$ on $\mathcal{T}$ guarantees that every future-directed null geodesic $\gamma$ orthogonal to $\mathcal{T}$ develops a conjugate point to $\mathcal{T}$ within finite affine parameter $\lambda \leq 2/|\theta_0|$. (A conjugate point is where infinitesimally neighboring geodesics from $\mathcal{T}$ focus to a single point.) By the assumption of geodesic completeness, all these geodesics extend beyond their conjugate points.

### Step 2: Conjugate Points Remove Generators from the Boundary

A fundamental result in causal geometry states: *a null geodesic $\gamma$ starting on a closed surface $\mathcal{T}$ lies on the boundary $\partial I^+(\mathcal{T})$ (the "edge of the future" of $\mathcal{T}$) only up to the first conjugate point.* Beyond a conjugate point, $\gamma$ enters the interior $\text{int}(I^+(\mathcal{T}))$.

This is because at a conjugate point, there exists a nearby null geodesic that nearly intersects $\gamma$. The resulting "broken" null curve can be deformed into a timelike curve, showing that points beyond the conjugate point are in the chronological future, not on the boundary.

### Step 3: The Boundary of the Future is Compact

Since *every* generator of $\partial I^+(\mathcal{T})$ acquires a conjugate point within bounded affine parameter, and since the generators leave $\partial I^+(\mathcal{T})$ at their conjugate points, the achronal boundary $\partial I^+(\mathcal{T})$ is a **compact** set. (It is the image of the compact trapped surface $\mathcal{T}$ under the null geodesic flow, restricted to bounded affine parameter, and the generators all terminate within this bounded region.)

### Step 4: The Topological Contradiction

Define the projection map $\pi: \partial I^+(\mathcal{T}) \to \Sigma$ by flowing each point on $\partial I^+(\mathcal{T})$ along the integral curves of $\text{grad}(t)$ (the gradient of a global time function with $\Sigma = t^{-1}(0)$) down to the Cauchy surface $\Sigma$. This map $\pi$ is:

- **Continuous** (by continuity of the flow)
- **Injective** (by achronality of $\partial I^+(\mathcal{T})$: each integral curve of the timelike gradient field meets the achronal set at most once)
- **Open** (the image is an open subset of $\Sigma$)

Therefore $\pi$ is a homeomorphism onto its image $\pi(\partial I^+(\mathcal{T})) \subseteq \Sigma$. But:

- $\partial I^+(\mathcal{T})$ is **compact** (from Step 3)
- $\Sigma$ is **non-compact** (by hypothesis)
- $\pi(\partial I^+(\mathcal{T}))$ is a compact, open subset of $\Sigma$

A non-compact, connected topological manifold cannot contain a non-empty subset that is simultaneously open and compact. (Such a set would be both open and closed --- since compact subsets of Hausdorff spaces are closed --- contradicting connectedness unless the set is the entire space, but then $\Sigma$ would be compact.)

**Contradiction.** Therefore the assumption of null geodesic completeness is false. $\blacksquare$

### 6.1 Summary Diagram of the Proof Logic

```
Trapped surface (theta < 0 on compact T)
         |
         | Raychaudhuri + NEC
         v
All null generators acquire conjugate points (within finite lambda)
         |
         | Causal geometry: generators leave boundary at conjugate points
         v
Boundary of the future, d I^+(T), is compact
         |
         | Injection into Cauchy surface
         v
Compact open subset of non-compact Sigma  --->  CONTRADICTION
         |
         v
Null geodesic incompleteness (singularity)
```

---

## 7. What the Theorem Does NOT Say

Penrose's theorem is an existence result of great generality, but its very generality means it provides almost no information about the *nature* of the singularity. The following are common misconceptions.

### 7.1 It Does Not Specify the Causal Character of the Singularity

The theorem says nothing about whether the singularity is:
- **Spacelike** (as in Schwarzschild): a "crushing" singularity that lies in the future of all infalling observers
- **Timelike** (as in Reissner--Nordstrom or Kerr interior): a singularity that can be avoided
- **Null**: a singularity approached along null directions

Different exact solutions exhibit all three types, and the theorem does not distinguish among them.

### 7.2 It Does Not Prove Curvature Divergence

The conclusion is **geodesic incompleteness** --- the existence of an inextendible geodesic with finite affine length. This is not the same as curvature divergence. There exist geodesically incomplete spacetimes where:
- All curvature invariants remain bounded (e.g., certain pp-wave spacetimes)
- The spacetime is locally extendible but globally inextendible due to topological obstructions
- The Kretschmann scalar $R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}$ remains finite

The theorem proves that "something goes wrong" with the spacetime, but does not specify *what* goes wrong.

### 7.3 It Does Not Prove the Existence of Black Holes

A black hole is defined by the existence of an **event horizon** --- a global causal boundary shielding the singularity from distant observers. Penrose's theorem proves the existence of incomplete geodesics but says nothing about whether an event horizon forms. The singularity could, in principle, be **naked** (visible to external observers).

### 7.4 It Does Not Specify Uniqueness or Location

The theorem guarantees the existence of *at least one* incomplete null geodesic. It does not say:
- How many geodesics are incomplete
- Where the incomplete geodesic is located
- Whether all geodesics entering the trapped region are incomplete
- Whether timelike geodesics are also incomplete

### 7.5 It Does Not Apply to Spatially Closed Universes

The requirement of a *non-compact* Cauchy surface excludes spatially closed ($S^3$ or $T^3$) cosmologies. The cosmological singularity theorems (Hawking 1967, Hawking--Penrose 1970) address this case with different hypotheses.

### 7.6 The Gap Between Incompleteness and Physical Singularity

Formally, geodesic incompleteness means the spacetime manifold $(M, g_{\mu\nu})$ is "too small" --- a freely falling particle or light ray reaches the "edge" in finite proper time or affine parameter. Whether this represents:
- A genuine curvature singularity (physical prediction)
- A Cauchy horizon beyond which determinism breaks down
- A mere coordinate/topological artifact of the chosen manifold

requires additional analysis beyond the scope of the theorem.

---

## 8. The Hawking--Penrose Theorem (1970)

### 8.1 Motivation

Penrose's 1965 theorem applies to gravitational collapse (trapped surface, non-compact Cauchy surface, null incompleteness). Hawking's 1967 theorem applies to cosmology (reconverging light cone, compact or non-compact Cauchy surface, timelike incompleteness). The **Hawking--Penrose theorem** (1970) provides a single unified result encompassing both scenarios.

**Citation:** S.W. Hawking and R. Penrose, "The Singularities of Gravitational Collapse and Cosmology," *Proc. R. Soc. Lond. A* **314**, 529--548 (1970).

### 8.2 Statement

**Theorem (Hawking--Penrose, 1970).** *A spacetime $(M, g_{\mu\nu})$ is not timelike and null geodesically complete if the following conditions hold:*

1. **Strong energy condition (timelike convergence condition):**
$$R_{\mu\nu} \, u^{\mu} u^{\nu} \geq 0 \quad \text{for all timelike } u^{\mu}$$
(This implies the null convergence condition by continuity.)

2. **Generic condition:** Every inextendible timelike or null geodesic contains a point where:
$$k_{[\alpha} R_{\beta]\gamma\delta[\epsilon} k_{\phi]} k^{\gamma} k^{\delta} \neq 0$$
(The curvature is not "specially aligned" with the geodesic; this holds generically.)

3. **No closed timelike curves** (chronology condition).

4. **At least one of the following:**
   - (a) There exists a compact achronal set without edge (a closed spacelike hypersurface --- spatially closed universe).
   - (b) There exists a closed trapped surface.
   - (c) There exists a point $p$ such that the expansion of the future (or past) directed null geodesics from $p$ becomes negative (reconverging light cone).

*Then the spacetime contains at least one incomplete timelike or null geodesic.*

### 8.3 Comparison with Penrose 1965

| Feature | Penrose 1965 | Hawking--Penrose 1970 |
|---|---|---|
| Energy condition | Null ($R_{\mu\nu} k^{\mu} k^{\nu} \geq 0$) | Strong ($R_{\mu\nu} u^{\mu} u^{\nu} \geq 0$) |
| Causality condition | Global hyperbolicity | Chronology (weaker) |
| Trapping condition | Closed trapped surface | Trapped surface OR closed universe OR reconverging light cone |
| Generic condition | Not required | Required |
| Conclusion | Null geodesic incompleteness | Timelike or null geodesic incompleteness |
| Scope | Gravitational collapse | Collapse and cosmology |

### 8.4 The Role of the Generic Condition

The generic condition ensures that tidal forces act non-trivially on every geodesic, preventing pathological spacetimes where geodesics are "shielded" from focusing by exact algebraic alignment with the curvature. It holds for all known physically realistic spacetimes and fails only for highly symmetric, measure-zero configurations.

---

## 9. Connection to Cosmic Censorship

### 9.1 The Problem Raised by the Theorem

Penrose's theorem proves that singularities are inevitable under very general conditions, but it says *nothing* about whether those singularities are hidden behind event horizons. This gap motivated Penrose to formulate the **cosmic censorship conjectures** (1969).

### 9.2 Weak Cosmic Censorship (WCC)

**Conjecture (Penrose, 1969).** *Singularities arising from gravitational collapse of physically reasonable matter from generic initial conditions are always hidden within event horizons --- no naked singularities are visible to distant observers.*

Formally: for generic asymptotically flat initial data satisfying suitable energy conditions, the maximal Cauchy development possesses a complete future null infinity $\mathscr{I}^+$.

### 9.3 Strong Cosmic Censorship (SCC)

**Conjecture (Penrose, 1979).** *For generic initial data, the maximal globally hyperbolic development is inextendible --- general relativity is deterministic.*

Formally: for generic compact or asymptotically flat initial data, the maximal Cauchy development $(M, g_{\mu\nu})$ is inextendible as a suitably regular Lorentzian manifold.

The strong version addresses the internal structure of black holes: it asserts that the Cauchy horizons found in exact solutions (Kerr, Reissner--Nordstrom) are unstable and would be replaced by singularities under perturbation, preventing extension beyond the Cauchy horizon.

### 9.4 Current Status

Both conjectures remain **open** in full generality as of 2025. Key results:
- **Christodoulou (1999):** Proved WCC for the spherically symmetric Einstein--scalar field system.
- **Dafermos (2003--present):** Extensive work on SCC for Kerr and Reissner--Nordstrom, showing that the Cauchy horizon is generically singular in $C^0$ but the metric may be extendible in $C^0$ (refuting the $C^0$ formulation of SCC for some cases).
- **Counterexamples:** Known counterexamples exist in higher dimensions and for fine-tuned initial data, but generic counterexamples in 3+1 dimensions satisfying physical energy conditions are not known.

### 9.5 The Logical Chain

```
Penrose 1965 theorem
     |
     |  Proves singularities are inevitable
     |  but silent on visibility
     v
Cosmic Censorship Conjectures (Penrose 1969, 1979)
     |
     |  Conjectured: singularities are hidden (WCC)
     |  Conjectured: determinism is preserved (SCC)
     v
Still open: the most important unsolved problems
in mathematical general relativity
```

---

## 10. Key Equations

### 10.1 The Raychaudhuri Equation (Null Congruences)

$$
\frac{d\theta}{d\lambda} = -\frac{1}{2}\theta^2 - \sigma_{\mu\nu}\sigma^{\mu\nu} + \omega_{\mu\nu}\omega^{\mu\nu} - R_{\mu\nu} k^{\mu} k^{\nu}
$$

### 10.2 The Focusing Inequality

For vorticity-free, null-energy-condition-satisfying congruences:

$$
\frac{d\theta}{d\lambda} \leq -\frac{1}{2}\theta^2
$$

### 10.3 The Blowup Estimate

If $\theta(\lambda_0) = \theta_0 < 0$:

$$
\theta(\lambda) \leq \frac{\theta_0}{1 + \frac{1}{2}\theta_0(\lambda - \lambda_0)} \to -\infty \quad \text{as } \lambda \to \lambda_0 + \frac{2}{|\theta_0|}
$$

### 10.4 The Null Energy Condition

$$
R_{\mu\nu}\,k^{\mu} k^{\nu} \geq 0 \quad \forall\; k^{\mu} \text{ null}
$$

Equivalently via Einstein's equations:

$$
T_{\mu\nu}\,k^{\mu} k^{\nu} \geq 0 \quad \forall\; k^{\mu} \text{ null}
$$

### 10.5 The Expansion Scalar

$$
\theta = q^{\mu\nu} \nabla_{\mu} k_{\nu} = \frac{1}{\delta A}\frac{d(\delta A)}{d\lambda}
$$

### 10.6 The Strong Energy Condition (Hawking--Penrose)

$$
R_{\mu\nu}\,u^{\mu} u^{\nu} \geq 0 \quad \forall\; u^{\mu} \text{ timelike}
$$

Equivalently:

$$
\left(T_{\mu\nu} - \frac{1}{2}T\,g_{\mu\nu}\right) u^{\mu} u^{\nu} \geq 0 \quad \forall\; u^{\mu} \text{ timelike}
$$

### 10.7 The Generic Condition

For a null geodesic with tangent $k^{\mu}$:

$$
k_{[\alpha}\,R_{\beta]\gamma\delta[\epsilon}\,k_{\phi]}\,k^{\gamma}\,k^{\delta} \neq 0 \quad \text{at some point on every geodesic}
$$

### 10.8 Einstein Field Equations

$$
R_{\mu\nu} - \frac{1}{2}R\,g_{\mu\nu} + \Lambda\,g_{\mu\nu} = 8\pi\,T_{\mu\nu}
$$

---

## Appendix A: Glossary

| Term | Definition |
|---|---|
| **Affine parameter** | Parameter $\lambda$ along a geodesic such that $k^{\mu}\nabla_{\mu}k^{\nu} = 0$ |
| **Achronal set** | A set no two of whose points are connected by a timelike curve |
| **Cauchy surface** | A spacelike hypersurface intersected exactly once by every inextendible causal curve |
| **Conjugate point** | A point where infinitesimally neighboring geodesics from a surface refocus |
| **Expansion scalar** ($\theta$) | Divergence of a geodesic congruence; rate of change of cross-sectional area |
| **Future null geodesic incompleteness** | Existence of a future-inextendible null geodesic with finite affine length |
| **Global hyperbolicity** | Existence of a Cauchy surface; equivalently, strong causality + compact causal diamonds |
| **Null convergence condition** | $R_{\mu\nu}k^{\mu}k^{\nu} \geq 0$ for null $k^{\mu}$ |
| **Screen space** | The 2-dimensional spacelike subspace orthogonal to both null directions at a point of a null hypersurface |
| **Shear** ($\sigma_{\mu\nu}$) | Traceless symmetric part of the deformation tensor; distortion without volume change |
| **Trapped surface** | Compact spacelike 2-surface with $\theta_+ < 0$ and $\theta_- < 0$ |
| **Vorticity** ($\omega_{\mu\nu}$) | Antisymmetric part of the deformation tensor; rotation of the congruence |

## Appendix B: Timeline

| Year | Event |
|---|---|
| 1916 | Schwarzschild solution; coordinate singularity at $r = 2M$ |
| 1939 | Oppenheimer--Snyder: dust collapse to singularity under spherical symmetry |
| 1960 | Kruskal--Szekeres: maximal extension of Schwarzschild; true singularity at $r=0$ confirmed |
| 1961 | Raychaudhuri equation applied to cosmological models |
| 1963 | Kerr solution; Lifshitz--Khalatnikov claim singularities are non-generic |
| **1965** | **Penrose: trapped surfaces and the singularity theorem** |
| 1967 | Hawking: cosmological singularity theorem (Big Bang) |
| 1969 | Penrose: cosmic censorship conjecture |
| 1970 | Hawking--Penrose: unified singularity theorem |
| 1970 | BKL: oscillatory approach to the singularity (retraction of 1963 claim) |
| 1991 | Christodoulou--Klainerman: nonlinear stability of Minkowski space |
| 2020 | Nobel Prize to Penrose (shared with Genzel and Ghez for Sgr A*) |

---

## References

1. R. Penrose, "Gravitational Collapse and Space-Time Singularities," *Phys. Rev. Lett.* **14**, 57--59 (1965). [ADS](https://ui.adsabs.harvard.edu/abs/1965PhRvL..14...57P/abstract)
2. S.W. Hawking and R. Penrose, "The Singularities of Gravitational Collapse and Cosmology," *Proc. R. Soc. Lond. A* **314**, 529--548 (1970).
3. J.M.M. Senovilla and D. Garfinkle, "The 1965 Penrose Singularity Theorem," *Class. Quantum Grav.* **32**, 124008 (2015). [arXiv:1410.5226](https://arxiv.org/abs/1410.5226)
4. K. Landsman, "Penrose's 1965 singularity theorem: from geodesic incompleteness to cosmic censorship," *Gen. Relativ. Gravit.* **54**, 115 (2022). [Springer](https://link.springer.com/article/10.1007/s10714-022-02973-w)
5. S.W. Hawking and G.F.R. Ellis, *The Large Scale Structure of Space-Time* (Cambridge University Press, 1973).
6. R.M. Wald, *General Relativity* (University of Chicago Press, 1984).
7. Nobel Prize in Physics 2020: [Scientific Background](https://www.nobelprize.org/prizes/physics/2020/popular-information/)
8. A.K. Raychaudhuri, "Relativistic Cosmology. I," *Phys. Rev.* **98**, 1123 (1955).
