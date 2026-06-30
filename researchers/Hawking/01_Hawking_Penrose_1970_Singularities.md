# The Singularities of Gravitational Collapse and Cosmology

**Author(s):** S. W. Hawking, R. Penrose
**Year:** 1970
**Journal:** Proc. R. Soc. Lond. A 314, 529-548 (1970)
**arXiv:** N/A (pre-arXiv)
**Relevance:** MEDIUM

---

## Abstract

A new theorem on space-time singularities is presented which largely incorporates and generalizes the previously known results. The theorem implies that space-time singularities are to be expected if either the universe is spatially closed or there is an 'object' undergoing relativistic gravitational collapse (existence of a trapped surface) or there is a point $p$ whose past null cone encounters sufficient matter that the divergence of the null rays through $p$ changes sign somewhere to the past of $p$ (i.e. there is a minimum apparent solid angle, as viewed from $p$ for small objects of given size). The theorem applies if the following four physical assumptions are made: (i) Einstein's equations hold (with zero or negative cosmological constant), (ii) the energy density is nowhere less than minus each principal pressure nor less than minus the sum of the three principal pressures (the 'energy condition'), (iii) there are no closed timelike curves, (iv) every timelike or null geodesic enters a region where the curvature is not specially alined with the geodesic. (This last condition would hold in any sufficiently general physically realistic model.) In common with earlier results, timelike or null geodesic incompleteness is used here as the indication of the presence of space-time singularities. No assumption concerning existence of a global Cauchy hypersurface is required for the present theorem.

---

## Key Arguments and Derivations

### 1. Introduction and Motivation (Section 1)

The paper opens by noting the fundamental instability of gravitation for large mass concentrations. The Chandrasekhar limit (~1.3 solar masses) implies gravitational collapse is inevitable for sufficiently massive stars that have exhausted nuclear fuel. On cosmological scales, the same instability manifests in the big bang singularity of expanding models.

The authors review five prior singularity theorems (I-V):
- **Theorem I** (Penrose 1965): Uses trapped surfaces but requires a non-compact global Cauchy hypersurface -- too strong.
- **Theorem II** (Hawking 1966a): Requires compact spacelike hypersurface with everywhere diverging normals -- restricts to "closed, everywhere expanding" models.
- **Theorems III, IV** (Geroch 1966, Hawking 1966b): Require non-existence of horizons or global Cauchy hypersurface.
- **Theorem V** (Hawking 1967): Requires divergence of ALL timelike and null geodesics through a point to change sign -- stronger than desired.

The new theorem incorporates all five while avoiding their individual weaknesses, with only two reservations: it requires no closed timelike curves and uses the slightly stronger energy condition (3.4).

### 2. Definitions and Lemmas (Section 2)

The paper develops the mathematical machinery of causal structure theory:

- **Space-time**: 4-dimensional differentiable Hausdorff paracompact manifold with pseudo-Riemannian metric of signature $(+,-,-,-)$ and time-orientation.
- **Causal curves**: Limits of timelike curves; continuous but not necessarily smooth.
- **Chronological sets**: $I^+(p) = \{x : p \ll x\}$ (open future), $J^+(p) = \{x : p \preccurlyeq x\}$.
- **Achronal sets**: Sets containing no pair of points connected by a timelike curve.
- **Domain of dependence**: $D^+(S) = \{x : \text{every past-inextendible timelike curve through } x \text{ meets } S\}$.
- **Cauchy horizon**: $H^+(S) = \overline{D^+(S)} - I^-[D^+(S)]$.
- **Strong causality**: Holds at $p$ if arbitrarily small causally convex neighborhoods of $p$ exist.
- **Conjugate points**: Points on a causal geodesic where neighboring geodesics refocus.
- **Future-trapped set**: Non-empty achronal closed set $S$ for which $E^+(S)$ is compact.

Key lemmas established:
- **Lemma 2.8**: If a causal geodesic from $p$ to $q$ contains conjugate points between them, a longer timelike curve from $p$ to $q$ exists.
- **Lemma 2.9**: Null geodesics on $\dot{I}^+[S]$ or $H^+(S)$ cannot contain conjugate points except at endpoints.
- **Lemma 2.10**: No closed timelike curves + every inextendible null geodesic has conjugate points implies strong causality throughout.
- **Lemma 2.11**: If $J^+(p) \cap J^-(q)$ is compact with strong causality, a maximum-length timelike geodesic from $p$ to $q$ exists.
- **Lemma 2.12**: If $S$ is future-trapped with strong causality on $\dot{I}^+[S]$, a future-inextendible timelike curve $\gamma \subset \text{int } D^+(E^+(S))$ exists.

### 3. The Theorem and Corollary (Section 3)

**Theorem.** No space-time $M$ can satisfy all of the following three requirements together:
- (3.1) $M$ contains no closed timelike curves,
- (3.2) every inextendible causal geodesic in $M$ contains a pair of conjugate points,
- (3.3) there exists a future- (or past-) trapped set $S \subset M$.

**Analysis of conditions:**

Condition (3.2) follows from three physical requirements: causal geodesic completeness, the energy condition, and a generality assumption. The energy condition states:

$$t^a t_a = 1 \implies R_{ab} t^a t^b \geq 0$$

With Einstein's equations $R_{ab} - \frac{1}{2}R g_{ab} = -\kappa T_{ab}$, this becomes:

$$\varepsilon + \sum_i p_i \geq 0 \quad \text{and} \quad \varepsilon + p_i \geq 0$$

where $\varepsilon$ is energy density and $p_i$ are principal pressures. The generality condition requires that every causal geodesic $\gamma$ with tangent $k^a$ contains a point where $k_{[a} R_{b]cd[e} k_{f]} k^c k^d \neq 0$.

The Raychaudhuri equation drives the proof:

$$D\theta + \frac{1}{3}\theta^2 \leq -\sigma_{ab}\sigma^{ab} - R_{ab}k^ak^b \leq 0$$

where $\theta = \nabla_a t^a$ is the divergence/expansion. This implies $D^2 W \leq 0$ for volume element $W$, guaranteeing focal points on complete geodesics.

**Corollary.** A space-time $M$ cannot satisfy causal geodesic completeness if, together with Einstein's equations, the following four conditions hold:
- (3.20) $M$ contains no closed timelike curves.
- (3.21) The energy condition is satisfied at every point.
- (3.22) The generality condition is satisfied for every causal geodesic.
- (3.23) $M$ contains either (i) a trapped surface, or (ii) a point $p$ for which the convergence of all null geodesics through $p$ changes sign somewhere to the past of $p$, or (iii) a compact spacelike hypersurface.

The proof constructs a future-trapped set $S$, applies Lemma 2.12 to obtain a future-inextendible timelike curve in int $D^+(E^+(S))$, then uses the time-reverse to construct a past-trapped set $T$. Maximum-length timelike geodesics between points on the two curves would need conjugate points (by condition 3.2), but this is contradicted by their maximality (Lemma 2.11).

### Appendix: Application to the Observed Universe

The authors argue that the 2.7 K microwave background radiation implies the required reconvergence condition for past null geodesics from Earth. If the radiation is interpreted as a relic of a hot early universe, the matter density ensures that past-directed null geodesics from the present epoch encounter enough matter for their divergence to change sign. This establishes condition (3.23)(ii) for our universe, meaning that (under conditions 3.20-3.22) our universe must be geodesically incomplete in the past -- i.e., there was a singularity.

---

## Key Results

1. Unified singularity theorem subsuming all five prior results (Penrose I, Hawking II-IV, Hawking V) while requiring weaker hypotheses than any individual predecessor.
2. Established that space-time singularities (geodesic incompleteness) are generic under physically reasonable energy conditions, not artifacts of symmetry.
3. Three distinct physical scenarios yield singularities: gravitational collapse (trapped surface), cosmological (compact spatial hypersurface), and observational (past null cone reconvergence).
4. The theorem reveals that at least one causal geodesic must reach the singularity before any repeated focusing occurs -- providing a (minimal) structural constraint on singularity character.
5. Applied to the observed universe: the 2.7 K CMB radiation provides evidence that condition (3.23)(ii) holds, implying a past singularity.
6. The energy condition $\varepsilon + \sum p_i \geq 0$ and $\varepsilon + p_i \geq 0$ is the minimal requirement -- violated only by a positive cosmological constant $\Lambda > 0$, whose effects are negligible at large curvatures.

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Energy condition | $R_{ab} t^a t^b \geq 0$ for $t^a t_a = 1$ | Eq. (3.4) |
| Strong energy condition | $\varepsilon + \sum_i p_i \geq 0$ and $\varepsilon + p_i \geq 0$ | Eqs. (3.7)-(3.8) |
| Raychaudhuri equation | $D\theta + \frac{1}{3}\theta^2 + \sigma_{ab}\sigma^{ab} + R_{ab}k^ak^b = 0$ | Eq. (3.17) |
| Raychaudhuri trace | $D\theta + \frac{1}{3}\theta^2 \leq 0$ (under energy condition) | Eq. (3.17) |
| Volume focusing | $D^2 W \leq 0$ for volume element $W$ with $DW = \frac{1}{3}\theta W$ | Eqs. (3.18)-(3.19) |
| Weak energy condition | $R_{ab} l^a l^b \geq 0$ for $l^a l_a = 0$ | Eq. (3.9) |
| Generality condition | $k_{[a} R_{b]cd[e} k_{f]} k^c k^d \neq 0$ at some point on each geodesic | Eq. (3.10) |
| Domain of dependence | $D^+(S) = \{x : \text{every past-inextendible timelike curve through } x \text{ meets } S\}$ | Eq. (2.2) |
| Cauchy horizon | $H^+(S) = \overline{D^+(S)} - I^-[D^+(S)]$ | Eq. (2.3) |

---

## Relevance to Phonon-Exflation

The Hawking-Penrose singularity theorems apply to the full $M_4 \times K$ geometry of the phonon-exflation framework. In the framework, the strong energy condition (SEC) is generically violated in the effective 4D theory due to the Kaluza-Klein reduction from the internal SU(3) fiber: the tau-dependent compactification contributes effective negative pressure terms that violate $\varepsilon + 3p \geq 0$. This SEC violation is precisely what allows exflation (accelerated expansion) without a conventional inflaton. The theorem's requirement of a "trapped set" maps onto the framework's fold geometry at finite tau, and the cosmological application via the CMB reconvergence condition provides the observational anchor. The key structural insight is that the framework evades the singularity theorem not by abandoning general relativity but by modifying the effective energy conditions through the internal geometry -- the instanton transit through the fold replaces the classical singularity with a quantum critical transition.
