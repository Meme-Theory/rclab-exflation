# What We Cannot Learn From Analogue Experiments

**Author(s):** Karen Crowther, Niels S. Linnemann, Christian Wüthrich

**Year:** 2019

**Identifier:** arXiv:1811.03859 [physics.hist-ph]

**Published in:** Synthese, Vol. 198 (Supplement 16), pp. 3701–3726 (2021)

---

## Abstract

Analogue experiments—laboratory systems engineered to mimic aspects of inaccessible physical systems—have been proposed as a route to confirming phenomena that cannot be directly observed. Examples include "dumb holes" (acoustic analogs of black holes) and Bose-Einstein condensates simulating Hawking radiation. This paper argues that **analogue experiments cannot provide genuine confirmation of phenomena in their target (inaccessible) systems**. The core impediment is that analogue experiments must presuppose the physical adequacy of the theoretical framework used to describe the target system. This creates a logical circularity: one cannot use an experiment to validate a theory when the experiment's very design is predicated on accepting that theory. The authors distinguish between two epistemic roles: (1) analogue systems can **illustrate** conceptual possibilities, and (2) they can **constrain** the set of physically realizable mechanisms. But they cannot **confirm** that a given mechanism operates in the inaccessible target system without independent justification.

---

## Historical Context

The explosion of interest in analog gravity experiments in the early 2010s generated optimistic claims about their confirmatory power. Unruh's 1981 proposal of "black hole analogs" in flowing fluids, combined with subsequent work on photonic metamaterials, cold atoms, and acoustic systems, suggested a new empirical window into quantum gravity and cosmology. Hawking radiation—one of the most speculative predictions of general relativity, inaccessible to direct observation—suddenly seemed within experimental reach.

By 2018, when Crowther, Linnemann, and Wüthrich wrote their critique, the landscape had shifted. Several claimed detections of analog Hawking radiation had been published (Jeff Steinhauer's work with sonic horizons, for instance), yet none had achieved universal acceptance. A deeper epistemological question loomed: **can an analog experiment ever genuinely confirm a phenomenon in its inaccessible target domain?**

The paper is part of a broader philosophical backlash against uncritical enthusiasm for analogs, including contemporaneous work by philosophers such as Thébault (2019) and Dardashti et al. (2017). It marks a mature phase in the field where optimism is tempered by rigorous scrutiny of what experiments can and cannot establish.

---

## Key Arguments and Derivations

### The Source-Target Distinction

The fundamental framework separates any analogue experiment into two systems:

**Source System (S):** The engineered laboratory setup, directly controllable and observable. Example: acoustic waves in a flowing fluid.

**Target System (T):** The inaccessible theoretical domain to which the source is meant to be an analog. Example: gravitational collapse and Hawking radiation near a black hole event horizon.

The analogy is formalized by a **mapping function** $\phi$ that relates quantities in S to quantities in T:

$$\phi: \text{(observables in S)} \to \text{(observables in T)}$$

For example, the acoustic density perturbations in the flowing fluid map to metric perturbations in curved spacetime, and the sound speed maps to the speed of light.

### The Modeling Framework Assumption

Every analogue construction requires a **modelling framework** $\mathcal{F}_T$ that describes the target system theoretically. For black hole analogs, this framework is general relativity + quantum field theory on curved spacetime.

The framework $\mathcal{F}_T$ is not directly testable on the target system (by definition, the target is inaccessible). Instead, the analogue experiment tests whether the source system, **when governed by laws isomorphic to $\mathcal{F}_T$**, exhibits the predicted phenomena.

The circularity arises here: to validate $\mathcal{F}_T$ using an analogue experiment, one must:
1. Assume $\mathcal{F}_T$ describes the target system correctly.
2. Map the source to the target via $\phi$.
3. Observe predictions of $\mathcal{F}_T$ in the source.
4. Conclude that $\mathcal{F}_T$ is validated for the target.

But step 1 is precisely what is in question. The experiment is circular.

### Formal Characterization of the Gap

Let $P_T$ be a proposition about the target system: "Hawking radiation exists at the event horizon of a black hole." The target system is inaccessible, so $P_T$ cannot be directly tested.

An analogue experiment tests instead $P_S = \phi^{-1}(P_T)$: "An analogous radiation phenomenon emerges in the source system according to the mapping $\phi$."

Success (observing $P_S$) does **not** logically imply $P_T$ without additional assumptions:

$$P_S \not\Rightarrow P_T \quad \text{without additional justification}$$

The additional justification would need to establish:
- **Physical adequacy:** The modelling framework $\mathcal{F}_T$ correctly describes the target system.
- **Isomorphism robustness:** The mapping $\phi$ preserves all physically relevant properties (not just selected ones).
- **Absence of artefacts:** The observed phenomenon $P_S$ is not an artefact of the source system's specific microscopic details but genuinely arises from the universal principles governing $P_T$.

None of these can be established *via* the analogue experiment itself without begging the question.

### Illustrative vs. Confirmatory Roles

The authors argue that analogue experiments can play two legitimate roles:

**1. Illustration:** An analogue experiment can make a theoretical prediction vivid and concrete, helping physicists and the public understand how the phenomenon works in principle. The source system serves as a "proof of concept" for a mechanism.

**2. Constraint:** An analogue experiment can rule out certain microscopic implementations. If a phenomenon arises in the source system despite differences in microscopic detail, it suggests the phenomenon is robust to microscopic variations—a genuine constraint.

However, neither role constitutes confirmation of the target phenomenon. Confirmation requires that the phenomenon must occur *given the target system's true microscopic dynamics*, not given some isomorphic system's dynamics.

### The Problem of Multiple Realizations

Suppose an analogue experiment successfully exhibits phenomenon $P$ in source system S with microscopic Hamiltonian $H_S$. A second analogue realization in a different source system S' also exhibits $P$, with microscopic Hamiltonian $H'_S$ vastly different from $H_S$.

The universality is suggestive: perhaps $P$ arises from principles deeper than the microscopic details, making it more likely that $P$ also occurs in the target. But **universality across sources does not imply universality to the target** in the absence of independent theoretical grounding. The two sources might accidentally agree while diverging from the target.

---

## Key Results

1. **Analogue Experiments Cannot Confirm Inaccessible Phenomena:** Logical circularity is intrinsic; any confirmation attempt presupposes the framework one is trying to validate.

2. **The Mapping Function Must Be Justified Independently:** The analogy $\phi$ between source and target cannot itself be validated via the analogue experiment; it must be grounded in independent theoretical reasoning.

3. **Hawking Radiation Analogs Remain Inconclusive:** Observations of acoustic analog Hawking radiation in laboratory systems do not confirm that Hawking radiation occurs in actual black holes, contra optimistic claims in the literature.

4. **Multiple Realizations Are Epistemically Weak:** If two different analogue systems both exhibit a phenomenon, it suggests the phenomenon is robust, but this is not confirmation for the target system; it merely raises the prior probability.

5. **Illustration and Constraint Are Legitimate:** Analogue systems remain valuable for conceptual understanding and for establishing that a mechanism is physically possible (not forbidden by unknown constraints).

6. **Abduction to Explanation Still Requires Caution:** Even if an analogue experiment makes a phenomenon seem more "probable," the inference from "possible in source" to "actual in target" requires explicit justification beyond the experiment.

---

## Impact and Legacy

This paper has become the standard reference in the philosophy of science literature on analog experiments. Its impact includes:

- **Tempering Enthusiasm:** Subsequent proposals for analog experiments are more cautious about claimed confirmatory power, clearly distinguishing between "we can model this" and "we have confirmed this exists."

- **Methodological Refinement:** The paper catalyzed work on "analogue validation" (Dardashti et al. 2017), exploring under what conditions analogs can provide evidence (answer: under strict Bayesian accounting, with modest credence updates).

- **Experimental Design Reflection:** Teams proposing new analog experiments (particularly in gravitational-wave physics and quantum gravity) now carefully articulate what they hope to constrain or illustrate, rather than claiming confirmation.

- **Philosophical Standards in Physics:** The critique elevated the standard of philosophical clarity in physics about what can be learned from indirect experiments.

---

## Connection to Phonon-Exflation Framework

**The Framework as an Analogue Mapping:**

The phonon-exflation framework posits that the large-scale structure of spacetime and the particle spectrum emerge from excitations of a topologically ordered SU(3) fiber. In essence, the framework treats 4D cosmology as a "target system" (inaccessible to direct microscopic observation) and proposes that condensed-matter physics of the fiber provides the "source system" (the fundamental dynamics).

Under the Crowther-Linnemann-Wüthrich analysis, the framework is vulnerable to the same circularity: **the framework must assume that the effective-field-theory description of cosmology (Friedmann equations, particle spectrum, etc.) correctly maps to the underlying SU(3) dynamics**. This assumption cannot itself be validated by observing cosmological phenomena, because those phenomena are precisely the target system.

**Implications for Framework Validation:**

The critique suggests three possible responses:

1. **Seek Independent Grounding:** The SU(3) fiber is not truly "inaccessible"—it might be tested through precision tests of fundamental constants, quantum-gravity experiments at the TeV scale, or gravitational-wave polarization measurements (these would constitute independent validation of the modelling framework).

2. **Embrace the Illustrative Role:** The framework's primary value might be conceptual—showing that an emergent-gravity/condensed-matter route to cosmology is internally consistent and not logically forbidden. This is legitimate, but more modest.

3. **Apply Bayesian Constraint:** Multiple independent observations (S8 tension, dark energy dynamism, JWST LRDs, etc.) all seem consistent with the framework's predictions. While no single observation confirms, the convergence across diverse datasets can raise the posterior probability (Dardashti-style approach).

**The Ansatz Problem:**

A meta-level application of the critique: the framework's success in deriving the Standard Model quantum numbers ($\alpha \approx 1/137$, etc.) from the spectral action is often heralded as a triumph. But the framework must assume that the spectral-action ansatz correctly captures the dynamics. This is a modelling-framework assumption. The derivation of the Standard Model is conditional on the ansatz being "physically adequate"—a condition not independently validated.

**Toward Independent Tests:**

To escape the circularity, the framework would need to:
- Predict a new phenomenon not yet observed (e.g., a specific form of Lorentz violation, a new decay channel, an anomaly in precision tests).
- Show that this phenomenon is specific to the framework and not shared by all emergent-gravity models.
- Observe the phenomenon independently, in a domain (e.g., fundamental physics) not built into the framework.

The ALPHA-ENV-43 test (precision measurement of $\Delta\alpha$ in voids vs. filaments) is one such attempt at an independent discriminant.

---

## References and Further Reading

- Crowther, K., Linnemann, N., & Wüthrich, C. (2019). "What we cannot learn from analogue experiments." *Synthese*, 198(16), 3701–3726.
- Dardashti, R., Hartmann, S., Thébault, K. P. Y., & Winsberg, E. (2017). "Hawking radiation and analogue experiments: A Bayesian analysis." *Studies in History and Philosophy of Science Part B*, 67, 1–11.
- Thébault, K. P. Y. (2019). "What can we learn from analogue experiments?" *Studies in History and Philosophy of Science Part B*, 68, 1–13.
- Unruh, W. G. (1981). "Experimental black-hole evaporation?" *Physical Review Letters*, 46(21), 1351.
- Jacobson, T. (2015). "Introductory notes on black hole thermodynamics." arXiv:gr-qc/0410039.
