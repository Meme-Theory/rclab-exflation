# Information in Black Hole Radiation

**Authors**: Don N. Page
**Year**: 1993
**Journal**: *Physical Review Letters*, **71**, 3743--3746

---

## Abstract (Analytical Summary)

Page addresses the fundamental question: if black hole evaporation is unitary, what is the entanglement entropy of the Hawking radiation as a function of time? He shows that for a system of total Hilbert space dimension $mn$ (where $m$ is the dimension of the radiation subsystem and $n$ is the dimension of the black hole subsystem), the average entanglement entropy of the smaller subsystem in a random pure state is:

$$\langle S \rangle \approx \ln m - \frac{m}{2n} \qquad (m \leq n)$$

This means the entanglement entropy of the radiation grows approximately linearly with the number of emitted quanta (as each new quantum adds entanglement with the black hole interior), until the "Page time" $t_P$ when the radiation entropy equals the black hole entropy ($m = n$, i.e., half the total degrees of freedom have been radiated). After the Page time, the entropy decreases, eventually returning to zero when the black hole has fully evaporated. This inverted-V shape is the **Page curve**, which has become the benchmark that any proposed resolution of the information paradox must reproduce.

---

## Historical Context

### The Information Paradox circa 1993

By 1993, the information paradox was 17 years old. The community was roughly split:

1. **Information is lost** (Hawking's position): The evolution is non-unitary. The final state is mixed.
2. **Information is preserved** (the string theory consensus, building): The evolution is unitary. The radiation is in a pure state. Information is encoded in subtle correlations.

But if information is preserved, a specific prediction follows: the entanglement entropy of the radiation must follow a particular curve. Page's contribution was to derive this curve, providing a quantitative test for any proposed resolution.

### Page's Background

Don Page had been Hawking's student and close collaborator. He was one of the first to argue (1980) that information should be preserved, based on the principle that quantum gravity should be unitary. His 1993 paper made this argument quantitative.

### Entanglement Entropy and Quantum Information

By 1993, quantum information theory was beginning to emerge as a field. The concept of entanglement entropy as a measure of quantum correlations was well-established in condensed matter (von Neumann entropy of reduced density matrices) but had not been systematically applied to the black hole problem.

---

## Key Arguments and Derivations

### Setup: A Pure State in a Bipartite System

Consider a quantum system with total Hilbert space $\mathcal{H} = \mathcal{H}_A \otimes \mathcal{H}_B$, where $\dim(\mathcal{H}_A) = m$ and $\dim(\mathcal{H}_B) = n$, with $m \leq n$. The total state is pure: $|\psi\rangle \in \mathcal{H}$.

The reduced density matrix for subsystem $A$ is:
$$\rho_A = \text{Tr}_B |\psi\rangle\langle\psi|$$

The entanglement entropy is:
$$S_A = -\text{Tr}(\rho_A \ln \rho_A)$$

For a pure total state, $S_A = S_B$ (the entanglement entropy is symmetric).

### Page's Theorem: Average Entropy of a Random Pure State

Page considers a random pure state $|\psi\rangle$ drawn uniformly from the Haar measure on $\mathcal{H}$. He computes the average entanglement entropy:

$$\langle S_A \rangle = \sum_{k=n+1}^{mn} \frac{1}{k} - \frac{m-1}{2n}$$

For $m, n \gg 1$ with $m \leq n$:

$$\langle S_A \rangle \approx \ln m - \frac{m}{2n}$$

**Interpretation**: The average entanglement entropy of the smaller subsystem is nearly maximal ($\ln m$ would be the maximum, achieved for a maximally mixed $\rho_A$). The correction $-m/(2n)$ is small when $m \ll n$.

The derivation uses results from random matrix theory. The eigenvalues of $\rho_A$ for a random pure state follow the Marchenko--Pastur distribution (for $m, n \to \infty$ with fixed ratio). The computation involves averaging over the unitary group.

### Application to Black Hole Evaporation

Identify:
- $A$ = Hawking radiation (subsystem that has been emitted)
- $B$ = black hole (remaining subsystem)
- $mn$ = total Hilbert space dimension = $e^{S_0}$, where $S_0$ is the initial Bekenstein--Hawking entropy

At time $t$, the radiation has $m(t)$ effective degrees of freedom and the black hole has $n(t)$. If the evolution is unitary, the total state remains pure, and Page's formula applies.

**Early time** ($m \ll n$): The radiation subsystem is small. The entanglement entropy grows:
$$S_{\text{rad}} \approx \ln m \approx S_{\text{rad,thermal}}$$

where $S_{\text{rad,thermal}}$ is the thermal entropy of the radiation. The radiation appears thermal -- consistent with Hawking's calculation.

**Page time** ($m = n$, i.e., half the degrees of freedom have been radiated): The entropy reaches its maximum:
$$S_{\text{rad,max}} \approx \ln m = \frac{1}{2} S_0$$

**Late time** ($m \gg n$): Now the black hole is the smaller subsystem, and:
$$S_{\text{rad}} = S_{\text{BH}} \approx \ln n \approx S_{\text{BH,Bekenstein-Hawking}}$$

The entanglement entropy decreases, tracking the (shrinking) black hole's Bekenstein--Hawking entropy.

**Final state** ($n = 1$, black hole fully evaporated): $S_{\text{rad}} = 0$. The radiation is in a pure state. Information is recovered.

### The Page Curve

The entanglement entropy as a function of time traces the **Page curve**:

$$S_{\text{rad}}(t) = \begin{cases} S_{\text{rad,thermal}}(t) & t < t_P \\ S_{\text{BH}}(t) & t > t_P \end{cases}$$

where $t_P$ is the Page time. The curve is:
- Rising (approximately linearly) before the Page time
- Falling (approximately tracking $A(t)/4G$) after the Page time
- Zero at both the beginning and the end

The shape is an inverted V (or more precisely, a smooth curve that rises, peaks, and falls).

### The Page Time

The Page time $t_P$ is the time when half the initial entropy has been radiated. For a Schwarzschild black hole of initial mass $M_0$:

$$t_P \sim t_{\text{evap}} \cdot \left(1 - 2^{-2/3}\right) \approx 0.37 \, t_{\text{evap}}$$

The factor comes from the mass-time relation $M(t) = M_0 (1 - t/t_{\text{evap}})^{1/3}$ and the entropy $S \propto M^2$. The precise value depends on the emission model. The Page time is when the radiation subsystem dimension equals the black hole subsystem dimension ($m = n$), so that half the initial entropy has been radiated. Since $S \propto M^2$, a relatively small fractional mass loss corresponds to a large fractional entropy loss.

### Hawking's Prediction vs. the Page Curve

Hawking's 1975 calculation gives a radiation state that appears exactly thermal at all times. If taken at face value, the entanglement entropy of the radiation grows linearly forever:

$$S_{\text{Hawking}} = S_{\text{rad,thermal}}(t) \quad \text{for all } t$$

This diverges from the Page curve after $t_P$. The discrepancy between the Hawking curve and the Page curve is the quantitative statement of the information paradox.

---

## Physical Interpretation

### What the Page Curve Means

The Page curve encodes the assumption that the total evolution is unitary and that the black hole has a finite number of microstates ($e^{S_0}$). If either assumption is wrong -- if information is lost or if the black hole has infinitely many states -- the Page curve does not apply.

The rising phase ($t < t_P$) is physically obvious: each emitted Hawking quantum is entangled with its interior partner, adding one unit of entanglement entropy.

The falling phase ($t > t_P$) is the interesting part. It requires that the late-time Hawking quanta are NOT independent of the early-time radiation -- they must be correlated with it. These correlations are the mechanism by which information escapes the black hole.

### The Scrambling Time vs. Page Time

Two important timescales:
- **Scrambling time** $t_s \sim M \ln M$: The time for information dropped into the black hole to be "scrambled" throughout the horizon and begin to appear in the radiation. (Hayden and Preskill, 2007)
- **Page time** $t_P \sim M^3$: The time for half the entropy to be radiated.

The scrambling time is much shorter than the Page time: $t_s \ll t_P$. This means that after the Page time, any information dropped into the black hole emerges in the radiation almost immediately (in scrambling time).

### Thermalization vs. Unitarity

Before the Page time, the radiation looks thermal and there is no contradiction between Hawking's calculation and unitarity. The subtleties arise only after the Page time, which requires waiting for an astronomically long time ($\sim M^3$ in Planck units). This is why the information paradox is so hard to resolve observationally: the corrections to thermality are exponentially small in $S_0$ before the Page time.

---

## Impact and Legacy

### The Page Curve as a Diagnostic

The Page curve has become the gold standard for any proposed resolution of the information paradox. A successful resolution must:
1. Reproduce the Hawking thermal spectrum at early times (before Page time)
2. Reproduce the Page curve's decrease after the Page time
3. Give $S = 0$ at the end of evaporation

### Hayden--Preskill Protocol (2007)

Hayden and Preskill sharpened Page's analysis by considering the black hole as a quantum information processing system. They showed that if the black hole is a "fast scrambler" (scrambling time $\sim \ln S_0$), then after the Page time, any information thrown into the black hole can be decoded from the Hawking radiation in just $O(\ln S_0)$ additional emissions. This makes the black hole the most efficient information mirror in nature.

### The Island Formula and Page Curve (2019)

The most dramatic recent development: Penington (2019) and Almheiri, Engelhardt, Marolf, and Maxfield (2019) derived the Page curve from semiclassical gravity using the "island formula":

$$S_{\text{rad}} = \min\left\{\text{ext}\left[\frac{A(\partial I)}{4G_N} + S_{\text{bulk}}(I \cup R)\right]\right\}$$

Before the Page time, the extremum has no island ($I = \emptyset$), and $S_{\text{rad}} = S_{\text{bulk}}(R)$ grows linearly (the Hawking calculation).

After the Page time, a new saddle point appears with a non-empty island $I$ inside the black hole. The island contribution $A(\partial I)/4G_N \approx S_{\text{BH}}$ dominates, and $S_{\text{rad}} \approx S_{\text{BH}}(t)$ decreases.

The transition between the two saddles at $t = t_P$ reproduces the Page curve exactly (to leading order in $G_N$).

### Implications for Quantum Gravity

Page's analysis assumes that the black hole Hilbert space is finite-dimensional ($\dim = e^{S_0}$). This is a strong assumption:
- It is supported by the Bekenstein--Hawking entropy formula
- It is supported by the holographic principle
- It implies that the black hole interior has a finite number of degrees of freedom
- It is in tension with the seemingly infinite volume of the black hole interior in classical GR (the "bag of gold" paradox)

---

## Connections to Modern Physics

1. **Quantum error correction in gravity**: The island formula can be understood in terms of quantum error correction: the information about the black hole interior is encoded in the Hawking radiation via a quantum error-correcting code. The island is the "recovery" region. The transition at the Page time corresponds to the threshold of the code.

2. **Replica wormholes**: The island formula arises from a gravitational path integral computation using the replica trick. The "replica wormholes" are saddle points that connect different replicas of the spacetime. These are the gravitational instantons that implement the Page curve.

3. **Quantum extremal surfaces**: The generalization of the Ryu--Takayanagi formula to include quantum corrections (Engelhardt and Wall, 2015) -- the quantum extremal surface (QES) prescription -- is the key ingredient. The island is bounded by a QES inside the black hole.

4. **Complexity and the black hole interior**: After the Page time, the interior of the black hole is encoded in the radiation (via the island). Reconstructing the interior from the radiation requires a quantum computation of exponential complexity (Harlow and Hayden, 2013; Brown et al., 2016). This connects the information paradox to quantum computational complexity.

5. **For the exflation framework**: In a Kaluza--Klein framework, the Page curve analysis extends to include the internal degrees of freedom. The total Hilbert space is $\mathcal{H} = \mathcal{H}_{4D} \otimes \mathcal{H}_K$, and the entanglement entropy of the radiation includes contributions from both the 4D and internal sectors. If the internal space evolves (exflation), the effective number of internal degrees of freedom changes over time, modifying the Page curve. The "Page time" would depend on both the 4D horizon area and the compactification volume, providing a distinctive signature of the KK framework. The island formula in the full higher-dimensional spacetime could involve "internal islands" -- regions of the internal space that contribute to the radiation entropy.
