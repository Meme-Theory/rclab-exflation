# Underdetermination of Scientific Theory

**Author(s):** Kyle Stanford (Stanford Encyclopedia of Philosophy)

**Year:** 2023 (original entry 2006, updated 2023)

**Journal/Source:** Stanford Encyclopedia of Philosophy (plato.stanford.edu/entries/scientific-underdetermination/)

---

## Abstract

Kyle Stanford provides a comprehensive philosophical analysis of **underdetermination**: the condition in which available empirical evidence is insufficient to uniquely determine which of two or more competing theories is true. The entry traces the problem from Duhem and Quine through contemporary philosophy of science, distinguishing between **holistic underdetermination** (where hypotheses can only be tested collectively, leaving ambiguity about which fails if predictions are wrong) and **contrastive underdetermination** (where different theories make identical predictions on all observable phenomena). Stanford examines the implications for scientific realism, theory choice, and the rationality of accepting one theory over another when data underdetermine the choice. The paper addresses "unconceived alternatives"—logically possible theories not yet imagined that could be empirically equivalent to our current best theories. The entry concludes that underdetermination is a genuine epistemological challenge that affects how scientists justify their beliefs and how philosophers justify claims about scientific progress.

---

## Historical Context

The problem of underdetermination is ancient in philosophy but was formalized in 20th-century philosophy of science.

**Duhem (1905)**: Pierre Duhem noted that when an experiment contradicts a theoretical prediction, we cannot identify *which* component of the theory is false. A prediction is always derived from a conjunction of hypotheses:

$$P = (H_1 \cap H_2 \cap \cdots \cap H_n) \implies O$$

If observation $O$ fails to occur, we know $\neg O$ is true. But modus tollens only tells us that the conjunction is false:

$$\neg O \implies \neg(H_1 \cap H_2 \cap \cdots \cap H_n) \equiv (\neg H_1 \vee \neg H_2 \vee \cdots \vee \neg H_n)$$

We do not know *which* hypothesis to reject. Duhem used this as an argument for the holism of theory: theories are tested as wholes, not piece by piece.

**Quine (1951)**: Willard Van Orman Quine radicalized Duhem's insight. Not only are the specific hypotheses being tested underdetermined; the *background assumptions* (logic itself, mathematics, auxiliary hypotheses about experimental apparatus) are also part of the conjunction. In principle, we could deny any hypothesis and preserve agreement with observations by sufficiently adjusting the rest of the belief system.

$$\text{Observations} \iff \text{Belief Web}$$

The belief web is a network where any node is adjustable; adjust enough nodes (e.g., deny non-Euclidean geometry, deny quantum mechanics, deny the reliability of scales) and you can maintain consistency with observations.

**Quine-Duhem Thesis**: All theories are underdetermined by experience. Empiricism does not uniquely determine theory choice.

**Van Fraassen (1980)**: Bas van Fraassen distinguished a special case: **empirical equivalence**. Two theories are empirically equivalent if they make identical predictions for all observable phenomena, forever, under all conditions. If two theories are empirically equivalent, then *even in principle*, no experiment can distinguish them. Contrastive underdetermination is the problem of choosing between such theories.

Example: Newtonian mechanics predicts the same observable phenomena whether the universe is stationary or moving at constant velocity. In fact, Newton's laws are invariant under Galilean boosts; constant-velocity motion is unobservable. Two theories—one asserting the universe is at rest, another asserting it moves at velocity $v$—make identical predictions. Yet we (reasonably) accept that the universe's motion is ambiguous, not a fact about nature.

**Contemporary problem (2000s-2020s)**: As theoretical physics ventures into domains beyond empirical reach (string landscape, inflationary multiverse, quantum-gravity approaches), underdetermination becomes acute. There are many theories, few observations, and principled difficulty in deciding which theory to believe.

---

## Key Arguments and Derivations

### 1. Holistic Underdetermination (Duhem-Quine)

**Definition**: A set of hypotheses is holistically underdetermined if predictions depend on the *conjunction* of all hypotheses, and failure of a prediction does not identify which hypothesis is false.

**Formal structure**:
- Suppose we have hypotheses $H_1, \ldots, H_n$ and auxiliary assumptions $A_1, \ldots, A_m$.
- Theory $T = H_1 \cap \cdots \cap H_n \cap A_1 \cap \cdots \cap A_m$.
- Prediction: $T \implies O$ (observation $O$ should occur).
- Outcome: $\neg O$ (observation fails).
- Conclusion: $T$ is false, i.e., at least one of the $H_i$ or $A_j$ is false.

**Problem**: We don't know which. There are $n + m$ possible sources of error. Underdetermination becomes worse if:
- Auxiliary assumptions are numerous (they always are).
- Hypotheses are highly interconnected (modern physics is interconnected).
- Observation is indirect (most observations are).

**Example from cosmology**:
- Hypothesis $H_1$: Dark energy has constant equation of state $w = -1$ (ΛCDM).
- Hypothesis $H_2$: The expansion history is scale-invariant (FRW with flat geometry).
- Auxiliary $A_1$: Observations of Type Ia supernovae luminosity distances are calibrated correctly.
- Auxiliary $A_2$: Redshift measurements have negligible error.
- Auxiliary $A_3$: Gravitational lensing bias is $< 10\%$.

Suppose future observations show a deviation: the expansion rate deviates from ΛCDM predictions by 5%. Which is false?
- $H_1$ (maybe dark energy is not constant)?
- $H_2$ (maybe geometry is curved)?
- $A_1$ (maybe supernovae luminosity is biased)?
- $A_2$ (maybe redshift calibration has systematic error)?
- $A_3$ (maybe lensing bias is actually 20%)?

Holistic underdetermination says: *the observation doesn't tell you*. You must choose based on background assumptions, past success, simplicity, or pragmatism—not logic.

### 2. Contrastive Underdetermination (Empirical Equivalence)

**Definition**: Two theories $T_1$ and $T_2$ are empirically equivalent if they make identical predictions for all observable phenomena, under all conditions, forever.

**Formal structure**:
- For any observation $O$ and any condition $C$, $T_1$ predicts $O$ iff $T_2$ predicts $O$.
- Therefore, no conceivable experiment can distinguish $T_1$ from $T_2$.

**Consequence**: If $T_1$ and $T_2$ are empirically equivalent but make different claims about unobservable entities, then empiricism cannot determine which is true.

**Classic example (Newton vs. rotating universe)**:

Newton's laws are invariant under Galilean transformations:
$$\vec{r}'(t) = \vec{r}(t) + \vec{v}t$$

where $\vec{v}$ is a constant velocity. If the universe's center of mass moves at velocity $\vec{v}$, Newton's equations for relative motions are unchanged. Therefore:

- **Theory 1**: The universe's center of mass is at rest.
- **Theory 2**: The universe's center of mass moves at velocity $\vec{v} = (1 \text{ m/s}, 0, 0)$.

Both theories predict identical observable phenomena (positions of stars relative to each other, planetary orbits, etc.). Yet they differ on an unobservable fact (the universe's absolute motion).

We reasonably believe **Theory 1** is correct, but not because observations force us to. It is correct *by convention*—we choose a reference frame at rest relative to the cosmic microwave background. But there is no empirical argument that this choice is uniquely correct.

### 3. Rational Theory Choice Under Underdetermination

**The problem**: If theories are underdetermined, on what grounds do scientists choose one over another?

**Laudan's response (1984)**: Distinguish between theories that are *merely possible* and theories that are *rationally defensible*. Laudan argues that underdetermination is not as bad as it seems because:

1. **Most possible theories are irrational to believe** (they are inconsistent with well-established background knowledge, e.g., the laws of thermodynamics, the periodic table of elements).

2. **A few theories remain rationally defensible** (they are consistent with all background knowledge, fit the data, and have not been refuted).

3. **Scientists choose among the defensible theories using pragmatic criteria**: simplicity, explanatory scope, internal consistency, past success, fruitfulness (does the theory generate new research programs?).

Formally:

$$\text{Rationally Defensible Theories} = \{\text{Theories consistent with } B \text{ and fitting } D\}$$

where $B$ is background knowledge and $D$ is data. Scientists choose from this set using criteria like Occam's razor.

**Quine's response**: Quine resists Laudan's optimism. He argues that the set of rationally defensible theories is still underdetermined; background knowledge $B$ is itself underdetermined and subject to revision. Therefore, even the set of defensible theories is not uniquely determined.

**Pragmatist resolution**: In practice, scientists break the tie by choosing theories that:
- Solve the problem at hand (the "working hypothesis" approach).
- Extend naturally from proven frameworks (evolutionary progress, not revolutionary change).
- Have demonstrable empirical success on neighboring problems.
- Generate predictions in new domains (fecundity).

### 4. Unconceived Alternatives

**Modern insight (Stanford, 2006-2023)**: Even if we restrict to currently defensible theories, we face a deeper problem: **unconceived alternatives**.

An **unconceived alternative** is a logically possible theory that:
- Is empirically equivalent to our current best theory.
- Has not yet been imagined by any scientist.
- Would, if imagined, be rationally defensible.

**Historical evidence**: Stanford documents patterns where unconceived alternatives turned out to be true:

1. **Dalton's atoms** (1808): Before Dalton, chemistry was purely phenomenological. Ratios of combining masses seemed to suggest discrete particles, but no one imagined discrete atoms with fixed relative weights. Once imagined, atoms became empirically successful.

2. **Waves vs. corpuscles in light**: For 150 years, Newton's corpuscular theory and Huygens' wave theory were empirically equivalent on most phenomena. It took new experiments (interference, diffraction) to distinguish them. A third alternative—light as electromagnetic waves (Maxwell)—was later imagined.

3. **Spacetime**: Before Einstein, physicists understood relativity phenomenologically (Lorentz transformations leave Maxwell's equations invariant). But Einstein imagined a new alternative: spacetime is a geometric manifold, and light-speed invariance reflects spacetime structure, not dynamical properties of the luminiferous ether. This alternative was empirically equivalent to Lorentz's ether theory on all tested phenomena but conceptually superior.

4. **Quantum mechanics alternatives**: De Broglie-Bohm mechanics (1926) is empirically equivalent to standard quantum mechanics on all known experiments. It was not widely imagined until decades later. Its discovery did not change any experimental predictions but changed conceptual understanding.

**Stanford's argument**:

$$P(\text{New empirically equivalent theory in next 10 years}) > P(\text{No new underdetermined alternatives})$$

Historical evidence suggests that whenever a field exists long enough, new empirically equivalent alternatives *are* imagined. The set of unconceived alternatives is non-empty and large.

**Implication**: Even if we accept Laudan's pragmatism (choose among defensible theories), we cannot be confident that the future won't reveal an alternative we didn't imagine that:
- Is equally well supported by current observations.
- Makes very different predictions for future observations.
- Is now rationally defensible in light of new knowledge (e.g., computational power, new experimental techniques).

### 5. String Theory Case Study

Stanford's entry uses string theory as a contemporary case study in underdetermination:

- **String landscape**: The theory admits $\geq 10^{500}$ possible vacuum solutions, each corresponding to a different set of particle physics constants and coupling strengths.

- **Empirical equivalence**: All landscape vacua make the same predictions at low energies (particle masses, coupling constants are as we observe them). Therefore, all landscape models are empirically equivalent to ΛCDM.

- **Underdetermination**: No experiment can distinguish which landscape vacuum is "true" (string theory doesn't predict a unique vacuum).

- **Unconceived alternatives**: Competitors to string theory (loop quantum gravity, asymptotic safety, causal sets) are also empirically equivalent to ΛCDM on known data. New alternatives could be imagined that are equally compatible with observations.

**Conclusion**: String theory exemplifies acute underdetermination. It is not that the theory is empirically refuted; it is that *no conceivable experiment* can choose between string theory and alternatives. This is not a failing of string theory alone—it is a structural feature of quantum gravity, where scales are beyond observation.

---

## Key Results

1. **Duhem-Quine thesis**: All theories are underdetermined by experience. Empirical data confirm or refute conjunctions of hypotheses, not individual hypotheses.

2. **Empirical equivalence problem**: Two or more theories can make identical predictions for all observable phenomena, yet differ on unobservable facts. Empiricism cannot choose between them.

3. **Rational theory choice is pragmatic, not logical**: When theories are underdetermined, scientists choose based on simplicity, explanatory scope, past success, and fecundity—not on logical necessity.

4. **Laudan's defense**: The set of rationally defensible theories is narrowed by background knowledge and data-fitting. But this defense doesn't eliminate underdetermination; it reduces it.

5. **Unconceived alternatives are real**: Historically, scientists have repeatedly imagined new theories empirically equivalent to established ones. The set of unconceived alternatives is likely non-empty.

6. **Implications for theory choice**: Even our current best theories may be underdetermined by current evidence. Future observations and imagined alternatives could overturn current consensus.

7. **String theory as exemplar**: The string landscape and quantum-gravity frameworks exemplify underdetermination at its most acute. No experiment can choose between landscape vacua or between string theory and competitors.

---

## Impact and Legacy

Stanford's encyclopedia entry has become the canonical reference for underdetermination in contemporary philosophy of science:

- **In physics**: Philosophers of physics (Smolin, Wallace, Steinhardt) cite Stanford when arguing that theoretical physics has become untethered from observation.

- **In cosmology**: The entry is cited in debates about inflation, dark energy, and multiverse theories, where "no experiment can ever determine the truth."

- **In AI/ML**: Epistemologists cite Stanford when discussing the "alignment problem"—how do we choose between machine-learning models that fit training data equally well but make different predictions on unseen data?

- **In methodology**: Science education uses Stanford's framework to teach scientists about the limits of empiricism and the role of pragmatism in theory choice.

---

## Connection to Phonon-Exflation Framework

**Critical for assessing the framework's epistemic status.**

The phonon-exflation framework faces all three forms of underdetermination that Stanford identifies.

### Type 1: Holistic Underdetermination

The framework's predictions depend on a conjunction of assumptions:

$$H_1: \text{M4 × SU(3) is the correct geometry}$$
$$H_2: \text{Dirac spectrum determines all physics}$$
$$H_3: \text{Pairing instability drives expansion}$$
$$A_1: \text{Heat kernel asymptotics converge to machine epsilon}$$
$$A_2: \text{BCS approximation is valid}$$
$$A_3: \text{Friedmann-BCS coupling is perturbative}$$

Suppose observations showed a 20% deviation from ΛCDM (e.g., $w = -0.85$ instead of $-1.0$). Which hypothesis is false?

- Maybe $H_1$ (geometry is not M4 × SU(3))?
- Maybe $H_2$ (the Dirac spectrum is not the determinant)?
- Maybe $H_3$ (pairing doesn't couple to cosmology)?
- Maybe $A_1$ (heat kernel asymptotic expansion breaks down at the scales of interest)?
- Maybe $A_2$ (BCS theory is inapplicable in the early universe)?
- Maybe $A_3$ (perturbation theory fails and we need non-perturbative dynamics)?

Holistic underdetermination says the data alone don't tell you. You must use judgment, background assumptions, and pragmatism.

### Type 2: Contrastive Underdetermination

On current observational data, phonon-exflation is **empirically equivalent to ΛCDM**:
- Both predict $\Omega_k = 0$ (flat geometry).
- Both predict $n_s \approx 0.96$ (scalar spectral index).
- Both accommodate $H_0$, $\Omega_m$, $\Omega_\Lambda$ to within errors.
- Both are consistent with BAO data, CMB temperature, structure formation.

Therefore, **no current experiment distinguishes phonon-exflation from ΛCDM**. They are empirically equivalent on all tested phenomena.

This is not a weakness of phonon-exflation—it is a consequence of the underdetermination Stanford describes. But it means the framework must be justified by pragmatic criteria (elegance, unification, explanatory scope) rather than empirical superiority.

### Type 3: Unconceived Alternatives

The phonon-exflation framework competes with:
- ΛCDM (standard model + general relativity).
- Quintessence (slow-roll scalar field).
- K-mouflage (scalar field with higher-derivative interactions).
- Modified gravity (MOND, f(R) gravity, etc.).
- Ekpyrotic cosmology (contracting phase before bang).
- Bounce cosmology (universe avoids singularity).
- Multiverse/landscape (string theory vacua).

Each of these is empirically equivalent to ΛCDM on current data. But future observations (e.g., primordial gravitational waves, non-Gaussian features in the CMB, precise measurements of $w(z)$) could distinguish among them—or reveal entirely new unconceived alternatives.

### Sagan Agent's Challenge (Stanford Framework)

Stanford's analysis suggests that the phonon-exflation framework must achieve **one of two things**:

**Option A (Falsifiability)**: Identify a discriminant observable and make a quantitative prediction. E.g., "Phonon-exflation predicts $w = -0.97 \pm 0.03$ and $r = 0.08$. If observations show $w < -1.02$ or $r > 0.15$, the framework is ruled out."

Once you make such a prediction (before data analysis), you commit to falsifiability. This follows Mukhanov's standard (Paper 31) and Rovelli's requirement (Paper 29).

**Option B (Pragmatic Justification)**: Accept that the framework is empirically equivalent to ΛCDM on foreseeable observations. But argue that it is superior on pragmatic grounds:
- **Unification**: It unifies gravity, particles, and dark energy in a single framework.
- **Simplicity**: It reduces free parameters (no separate inflaton, no separate dark energy scalar).
- **Explanatory scope**: It explains particle masses and coupling constants from geometry.

Option B requires explicit acknowledgment: "Phonon-exflation and ΛCDM are empirically equivalent on current data. We believe phonon-exflation is more likely to be true because [pragmatic reasons], not because observations force us to." This is honest epistemology.

### The Framework's Status Under Stanford

**Current status**: The framework has neither made a falsifiable prediction (Option A) nor explicitly embraced pragmatic justification (Option B). It exists in a gray zone: claiming empirical motivation while lacking empirical content.

**Recommendation**: The Sagan agent should use Stanford's framework to force a choice:

1. **Commit to Option A**: Compute a novel prediction and let data decide.
2. **Commit to Option B**: Acknowledge empirical equivalence and justify the framework on elegance/unification grounds.
3. **Find an unconceived alternative**: Imagine a theory not yet considered that would also explain the data and be empirically equivalent to phonon-exflation. Use this to highlight the severity of underdetermination.

Stanford's paper is the Sagan agent's tool for holding the framework accountable to epistemic standards.

---

## Bibliography & Further Reading

- Duhem, P. (1905). *The Aim and Structure of Physical Theory*. (Translated 1954, Princeton University Press.)
- Quine, W. V. O. (1951). "Two dogmas of empiricism." *Philosophical Review*, 60(1), 20-43.
- Kuhn, T. S. (1962). *The Structure of Scientific Revolutions*. University of Chicago Press.
- van Fraassen, B. C. (1980). *The Scientific Image*. Oxford University Press.
- Laudan, L. (1984). *Science and Values*. University of California Press.
- Stanford, K. (2006/2023). "Underdetermination of scientific theory." *Stanford Encyclopedia of Philosophy*, edited by E. N. Zalta.
- Smolin, L. (2007). *The Trouble with Physics*. Houghton Mifflin.
- Wallace, D. (2020). "The epistemology of precision cosmology." *European Journal for Philosophy of Science*, 10(3), 49.
