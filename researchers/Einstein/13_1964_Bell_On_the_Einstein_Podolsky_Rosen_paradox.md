# On the Einstein Podolsky Rosen Paradox

**Author:** John Stewart Bell
**Year:** 1964
**Journal:** *Physics*, **1**(3), 195--200

---

## Abstract

In this landmark paper, John Bell proves that no local hidden-variable theory can reproduce all the statistical predictions of quantum mechanics for entangled particles. Specifically, he derives an inequality -- the Bell inequality -- that must be satisfied by any theory in which (a) measurement outcomes are determined by pre-existing hidden variables and (b) the measurement on one particle cannot influence the outcome on a distant particle (locality). Bell then shows that quantum mechanics violates this inequality for certain entangled states and measurement settings. The paper transforms the EPR debate from a philosophical discussion about completeness and reality into a precise, experimentally testable question. Its consequences are among the deepest in all of physics: the universe is either nonlocal or does not have definite properties prior to measurement, or both.

---

## Historical Context

### The EPR Aftermath

After the Einstein-Podolsky-Rosen paper of 1935 (Paper 09), the debate over the completeness of quantum mechanics remained largely philosophical. Bohr's response was influential in the Copenhagen community but did not provide a mathematical proof that hidden variables were impossible. Von Neumann's 1932 "impossibility proof" for hidden variables was accepted by most physicists but was based on an unjustified assumption (the linearity of expectation values for non-commuting observables).

### Bohm's Hidden-Variable Theory (1952)

David Bohm constructed an explicit hidden-variable theory (now called Bohmian mechanics or the de Broglie-Bohm pilot wave theory) that reproduces all quantum predictions exactly. This demonstrated conclusively that von Neumann's proof was flawed -- hidden variables were logically possible.

However, Bohm's theory is manifestly nonlocal: the velocity of each particle depends on the instantaneous positions of all other particles, mediated by the quantum potential. Bell, who studied Bohm's theory carefully, asked: is the nonlocality an artifact of Bohm's specific construction, or is it a necessary feature of any hidden-variable theory that reproduces quantum predictions?

### Bell's Insight

Bell's crucial insight was to separate two distinct properties that had been conflated:
1. **Hidden variables** (also called "realism"): measurement outcomes are determined by pre-existing properties, not created by the measurement.
2. **Locality**: the outcome of a measurement on one particle is independent of what measurement is performed on a distant particle.

EPR had argued: locality + completeness-criterion $\implies$ hidden variables (QM is incomplete). Bell asked the converse: if hidden variables exist AND locality holds, what are the observable consequences?

---

## Key Arguments and Derivations

### I. The Setup: Bohm's Version of EPR

Bell uses Bohm's simplified version of EPR with spin-1/2 particles. A pair of particles is prepared in the singlet state:

$$|\Psi\rangle = \frac{1}{\sqrt{2}}\left(|\uparrow\rangle_1|\downarrow\rangle_2 - |\downarrow\rangle_1|\uparrow\rangle_2\right)$$

Particle 1 goes to Alice, who measures spin along direction $\hat{a}$; particle 2 goes to Bob, who measures along $\hat{b}$. The measurements are spacelike-separated (no light signal can travel from one to the other during the measurement).

The quantum prediction for the correlation is:

$$E_{QM}(\hat{a}, \hat{b}) = \langle\Psi|\,(\hat{a}\cdot\vec{\sigma}_1)(\hat{b}\cdot\vec{\sigma}_2)\,|\Psi\rangle = -\hat{a}\cdot\hat{b} = -\cos\theta_{ab}$$

where $\theta_{ab}$ is the angle between the measurement directions.

### II. The Local Hidden-Variable Model

Bell considers the most general local hidden-variable theory. Each pair of particles carries a hidden variable $\lambda$ (possibly a vector, a function, or any mathematical object) drawn from some probability distribution $\rho(\lambda)$:

$$\int \rho(\lambda)\,d\lambda = 1, \qquad \rho(\lambda) \geq 0$$

Alice's outcome $A(\hat{a}, \lambda)$ depends on her measurement direction $\hat{a}$ and the hidden variable $\lambda$, but NOT on Bob's measurement direction $\hat{b}$. Similarly, Bob's outcome $B(\hat{b}, \lambda)$ depends on $\hat{b}$ and $\lambda$, but NOT on $\hat{a}$.

This is the **locality condition**: the outcome at each detector depends only on the local measurement setting and the shared hidden variable, not on anything happening at the distant detector.

The outcomes are $A(\hat{a}, \lambda) = \pm 1$ and $B(\hat{b}, \lambda) = \pm 1$.

The correlation function in the hidden-variable theory is:

$$E(\hat{a}, \hat{b}) = \int \rho(\lambda)\,A(\hat{a}, \lambda)\,B(\hat{b}, \lambda)\,d\lambda$$

### III. The Bell Inequality (Original Form)

Bell derives an inequality that $E(\hat{a}, \hat{b})$ must satisfy. Consider three measurement directions $\hat{a}$, $\hat{b}$, $\hat{c}$. Since $A = \pm 1$ and $B = \pm 1$:

$$E(\hat{a}, \hat{b}) - E(\hat{a}, \hat{c}) = \int \rho(\lambda)\left[A(\hat{a},\lambda)B(\hat{b},\lambda) - A(\hat{a},\lambda)B(\hat{c},\lambda)\right]d\lambda$$

Since the singlet state gives perfect anticorrelation along the same axis ($E(\hat{b},\hat{b}) = -1$), the hidden-variable theory must have $A(\hat{b},\lambda) = -B(\hat{b},\lambda)$ for all $\lambda$. Substituting $B(\hat{b},\lambda) = -A(\hat{b},\lambda)$:

$$E(\hat{a}, \hat{b}) - E(\hat{a}, \hat{c}) = -\int \rho(\lambda)\,A(\hat{a},\lambda)A(\hat{b},\lambda)\left[1 - A(\hat{b},\lambda)A(\hat{c},\lambda)\right]d\lambda$$

Taking absolute values and using $|A| = 1$:

$$|E(\hat{a}, \hat{b}) - E(\hat{a}, \hat{c})| \leq \int \rho(\lambda)\left|1 - A(\hat{b},\lambda)A(\hat{c},\lambda)\right|d\lambda$$

Since $A(\hat{b},\lambda)A(\hat{c},\lambda) = \pm 1$, the integrand is either 0 or 2. Therefore:

$$|E(\hat{a}, \hat{b}) - E(\hat{a}, \hat{c})| \leq 1 + E(\hat{b}, \hat{c})$$

This is **Bell's inequality**.

### IV. Quantum Violation

The quantum prediction $E_{QM}(\hat{a}, \hat{b}) = -\cos\theta_{ab}$ violates Bell's inequality for appropriate choices of measurement directions. Choose $\hat{a}$, $\hat{b}$, $\hat{c}$ coplanar with $\hat{b}$ bisecting the angle between $\hat{a}$ and $\hat{c}$, so $\theta_{ab} = \theta_{bc} = \theta/2$ and $\theta_{ac} = \theta$.

Bell's inequality requires:

$$|\cos(\theta/2) - \cos\theta| \leq 1 - \cos(\theta/2)$$

Using $\cos\theta = 2\cos^2(\theta/2) - 1$:

$$|\cos(\theta/2) - 2\cos^2(\theta/2) + 1| \leq 1 - \cos(\theta/2)$$

For $\theta = 2\pi/3$ ($\theta/2 = \pi/3$, $\cos(\pi/3) = 1/2$):

Left side: $|1/2 - 2(1/4) + 1| = |1| = 1$

Right side: $1 - 1/2 = 1/2$

So $1 \leq 1/2$, which is FALSE. The quantum prediction violates Bell's inequality.

### V. The CHSH Inequality

Clauser, Horne, Shimony, and Holt (1969) derived a more practical version, applicable without assuming perfect anticorrelation. For four measurement settings ($\hat{a}$, $\hat{a}'$ for Alice; $\hat{b}$, $\hat{b}'$ for Bob):

$$S = E(\hat{a},\hat{b}) - E(\hat{a},\hat{b}') + E(\hat{a}',\hat{b}) + E(\hat{a}',\hat{b}')$$

Any local hidden-variable theory satisfies:

$$|S| \leq 2$$

**Proof:** For any $\lambda$:

$$A(\hat{a},\lambda)[B(\hat{b},\lambda) - B(\hat{b}',\lambda)] + A(\hat{a}',\lambda)[B(\hat{b},\lambda) + B(\hat{b}',\lambda)]$$

Since $B = \pm 1$, either $B(\hat{b}) = B(\hat{b}')$ (so the first bracket is 0 and the second is $\pm 2$) or $B(\hat{b}) = -B(\hat{b}')$ (so the first is $\pm 2$ and the second is 0). Either way, the expression equals $\pm 2$. Averaging over $\lambda$: $|S| \leq 2$.

**Quantum prediction:** Choose the optimal measurement settings: $\hat{a}$ at $0$, $\hat{a}'$ at $\pi/2$, $\hat{b}$ at $\pi/4$, $\hat{b}'$ at $3\pi/4$ (angles measured from a fixed axis in the measurement plane). The inter-detector angles are:

$$\theta_{ab} = \pi/4, \quad \theta_{ab'} = 3\pi/4, \quad \theta_{a'b} = \pi/4, \quad \theta_{a'b'} = \pi/4$$

Using $E_{QM}(\hat{a},\hat{b}) = -\cos\theta_{ab}$:

$$E(\hat{a},\hat{b}) = -\cos(\pi/4) = -\frac{1}{\sqrt{2}}$$
$$E(\hat{a},\hat{b}') = -\cos(3\pi/4) = +\frac{1}{\sqrt{2}}$$
$$E(\hat{a}',\hat{b}) = -\cos(\pi/4) = -\frac{1}{\sqrt{2}}$$
$$E(\hat{a}',\hat{b}') = -\cos(\pi/4) = -\frac{1}{\sqrt{2}}$$

$$S_{QM} = -\frac{1}{\sqrt{2}} - \frac{1}{\sqrt{2}} - \frac{1}{\sqrt{2}} - \frac{1}{\sqrt{2}} = -\frac{4}{\sqrt{2}} = -2\sqrt{2}$$

Therefore $|S_{QM}| = 2\sqrt{2} \approx 2.828 > 2$.

The quantum value $2\sqrt{2}$ is the **Tsirelson bound** -- the maximum violation achievable by any quantum state. It exceeds the local hidden-variable bound of 2 by a factor of $\sqrt{2}$.

---

## Physical Interpretation

### What Bell's Theorem Rules Out

Bell's theorem rules out the conjunction of two assumptions:
1. **Realism (hidden variables):** Measurement outcomes are determined by pre-existing properties.
2. **Locality:** The outcome at one location is independent of the measurement choice at a distant location.

If experiments violate Bell's inequality (and they do), then at least one of these assumptions must be abandoned.

### The Three Options

1. **Abandon realism (Copenhagen-like):** Measurement outcomes are not determined until the measurement is performed. The wave function is a complete description -- there are no hidden variables. This is the majority position in quantum foundations.

2. **Abandon locality (Bohmian mechanics):** Hidden variables exist, but they are nonlocal -- the outcome at one location depends on the measurement setting at the distant location, mediated instantaneously by the quantum potential. Bohmian mechanics takes this route.

3. **Abandon both:** Some interpretations (e.g., QBism, relational QM) reject both classical realism and objective locality, treating quantum states as informational rather than ontological.

### No Faster-Than-Light Signaling

Despite the nonlocality implied by Bell violations, the correlations cannot be used for faster-than-light communication. Alice's local measurement statistics are independent of Bob's measurement choice:

$$P(A = +1|\hat{a}) = \frac{1}{2} \quad \text{regardless of } \hat{b}$$

The nonlocality is hidden in the correlations, which can only be observed by comparing results from both sides -- which requires classical communication. This is the "peaceful coexistence" between quantum nonlocality and relativistic causality.

### Fine's Theorem (1982)

Arthur Fine proved that the following are equivalent:
1. A local hidden-variable model exists for the correlations.
2. All Bell/CHSH inequalities are satisfied.
3. A joint probability distribution exists for all four observables $(A, A', B, B')$.

The violation of Bell inequalities is therefore equivalent to the non-existence of a classical joint probability distribution -- a fundamentally non-classical feature of quantum mechanics.

---

## Impact and Legacy

### Experimental Tests

**Freedman and Clauser (1972):** First experimental test using entangled photons from calcium cascades. Results violated Bell's inequality, consistent with QM.

**Aspect, Dalibard, and Roger (1982):** Used time-varying polarizer settings to close the "locality loophole" (the possibility that the detectors could communicate during the measurement). Results confirmed QM.

**Hensen et al. (2015), Giustina et al. (2015), Shalm et al. (2015):** "Loophole-free" Bell tests closing both the locality loophole and the detection loophole simultaneously. All confirmed quantum mechanics.

**Nobel Prize 2022:** Awarded to Clauser, Aspect, and Zeilinger "for experiments with entangled photons, establishing the violation of Bell inequalities and pioneering quantum information science."

### Quantum Information Theory

Bell's theorem is the foundation of device-independent quantum information processing:
- **Quantum key distribution (Ekert 1991):** The security of entanglement-based QKD is guaranteed by Bell inequality violations -- any eavesdropper would reduce the correlations.
- **Randomness certification:** Bell violations certify that measurement outcomes are genuinely random, not determined by any local mechanism.
- **Self-testing:** Bell violations can certify the quantum state and measurements without trusting the devices.

---

## Connections to Modern Physics

### Tsirelson's Bound and the CHSH Inequality

The quantum maximum $|S| = 2\sqrt{2}$ is not the algebraic maximum ($|S| = 4$, achievable with no-signaling but post-quantum correlations). Why does quantum mechanics stop at $2\sqrt{2}$? This question has driven research into "information causality" (Pawlowski et al., 2009) and "macroscopic locality" (Navascues and Wunderlich, 2010) as principles that might single out quantum correlations from the space of all no-signaling theories.

### Bell Inequalities and Quantum Gravity

In approaches to quantum gravity where spacetime and quantum mechanics emerge from a deeper structure, the Bell violation $S = 2\sqrt{2}$ becomes a prediction that must be derived rather than assumed. In Kaluza-Klein frameworks where the 4D quantum state is a projection from higher-dimensional classical geometry, the mechanism for producing Bell violations is an open problem. The fiber bundle holonomy of the internal space provides a potential geometric source of the non-commutative algebra needed for $S > 2$, but computing the precise CHSH value from the geometry remains one of the critical open challenges.

### Contextuality and the Kochen-Specker Theorem

Bell's theorem has a "non-locality" flavor (it involves spatially separated measurements). The Kochen-Specker theorem (1967) establishes a related but distinct result: even for a single system, non-contextual hidden variables (where the outcome of measuring an observable is independent of which other compatible observables are measured simultaneously) are incompatible with quantum mechanics. Together, Bell and Kochen-Specker establish that quantum mechanics is fundamentally non-classical in ways that go beyond mere indeterminism.

### Entanglement Monogamy

Bell violations exhibit "monogamy": if Alice and Bob share maximal entanglement (achieving $S = 2\sqrt{2}$), then neither can be entangled with a third party. This monogamy property is fundamental to quantum cryptography and has deep connections to the structure of spacetime in holographic quantum gravity (the monogamy of mutual information in AdS/CFT).
