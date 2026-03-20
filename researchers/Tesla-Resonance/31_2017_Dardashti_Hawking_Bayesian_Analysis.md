# Hawking Radiation and Analogue Experiments: A Bayesian Analysis

**Author(s):** Radin Dardashti, Stephan Hartmann, Karim P. Y. Thébault, Eric Winsberg

**Year:** 2017

**Identifier:** arXiv:1604.05932 [physics.hist-ph]

**Published in:** Studies in History and Philosophy of Science Part B: Studies in History and Philosophy of Modern Physics, Vol. 67, pp. 1–11 (2019)

---

## Abstract

Analogue experiments—laboratory systems engineered to exhibit phenomena analogous to black holes, Hawking radiation, or other extreme physics—have been proposed as a route to empirically testing aspects of quantum gravity. This paper provides a Bayesian framework for quantifying when and how such experiments can legitimately provide evidence for theoretical claims about inaccessible systems. The authors prove that analogue experiments **can be confirmatory**, under the condition that **universality arguments** can be invoked. They develop a formal model of confirmation scaling: how additional analogue realisations (different physical systems embodying the same principle) accumulate evidence, and show that this accumulation exhibits a **generic saturation feature** beyond which diminishing returns dominate. The framework enables optimisation of experimental design: different analogue realisations provide different levels of confirmation, and the analysis predicts which systems would be most epistemically valuable.

---

## Historical Context

The Crowther-Linnemann-Wüthrich (2019) paper had posed a fundamental challenge to analogue gravity experiments: can they ever confirm phenomena in inaccessible domains, or are they inevitably circular? The Dardashti et al. paper (submitted late 2015, revised 2017) provides a direct counter-argument grounded in Bayesian epistemology.

The motivation was clear: Hawking radiation, acoustic black holes, and quantum-gravity phenomena were becoming experimentally accessible through cleverly designed analogue systems. Yet the philosophical literature lacked a rigorous account of what such experiments could establish. Dardashti et al. set out to formalize the epistemology, showing that with appropriate caveats and careful Bayesian accounting, analogue experiments could provide genuine, quantifiable evidence.

The paper appeared as part of a broader 2017 debate on analogue gravity in philosophy of science (Thébault, Dawid, et al.), marking the field's maturation into a rigorous discipline.

---

## Key Arguments and Derivations

### Bayesian Framework for Confirmation

The analysis begins with a hypothesis $H_T$ about the target system (e.g., "Hawking radiation exists in black holes") and prior probability $P(H_T) = p_0$.

An analogue experiment produces evidence $E_S$ (observations in the source system). The posterior probability is:

$$P(H_T | E_S) = \frac{P(E_S | H_T) \cdot P(H_T)}{P(E_S)}$$

The **confirmation factor** (or likelihood ratio) is:

$$\Lambda = \frac{P(E_S | H_T)}{P(E_S | \neg H_T)}$$

If $\Lambda > 1$, the experiment confirms $H_T$ (raises its posterior). The larger $\Lambda$, the stronger the confirmation.

For an analogue experiment to be confirmatory, one needs:

$$P(E_S | H_T) \gg P(E_S | \neg H_T)$$

That is, observing the phenomenon in the analogue system must be much more likely *if* $H_T$ is true than if it is false.

### Universality Arguments

The key to making analogue experiments confirmatory is the **universality argument**. The authors define a universality argument as a theoretical principle that applies across multiple physically distinct systems:

**Definition:** A phenomenon $P$ is universal with respect to a class of systems $\{S_1, S_2, \ldots, S_N\}$ if the existence of $P$ in system $S_i$ implies the existence of $P$ in system $S_j$ for all $i, j$ in the class.

Example: If an acoustic horizon in a fluid exhibits Hawking radiation due to the universal structure of the Hawking process (which depends only on geometric properties near the horizon, not on the specific microscopic dynamics), then observing the phenomenon in the acoustic system strongly suggests it exists in gravitational systems.

The universality argument shifts the probabilistic weight:

$$P(E_S | H_T) = P(\text{phenomenon appears in S} | \text{universal mechanism}) \approx 1$$

Whereas:

$$P(E_S | \neg H_T) = P(\text{accidental mimicry in S despite T not exhibiting the phenomenon}) \ll 1$$

Under universality, observing the phenomenon in the analogue system becomes very good evidence for $H_T$.

### Scaling with Multiple Realizations

Suppose $N$ independent analogue systems $S_1, \ldots, S_N$ are tested, and all exhibit the phenomenon $P$. If each experiment is independent, the combined likelihood ratio is:

$$\Lambda_{\text{total}} = \prod_{i=1}^{N} \Lambda_i$$

In the best case (strong universality), each $\Lambda_i \approx \Lambda_0$ (constant), so:

$$\Lambda_{\text{total}} = \Lambda_0^N$$

The posterior probability grows exponentially:

$$P(H_T | E_1, \ldots, E_N) = \frac{\Lambda_0^N \cdot p_0}{\Lambda_0^N \cdot p_0 + 1 - p_0}$$

As $N \to \infty$, this approaches 1 (certainty), provided $\Lambda_0 > 1$.

### The Saturation Feature

However, the analysis reveals a critical limit. Each successive analogue realization provides less additional confirmation than the previous one. This is because:

1. **Diminishing novelty:** If the first five analogue systems all exhibit the phenomenon, the sixth offers less new information (law of diminishing returns in Bayesian learning).

2. **Systematic correlations:** Multiple realizations may share common confounds or artifacts, reducing their independence; the product $\prod \Lambda_i$ overstates the cumulative evidence.

3. **Model uncertainty:** As $N$ increases, one begins to suspect that all the analogue systems are sharing a common artefact unrelated to the target phenomenon.

Formally, the "saturation" appears when the marginal confirmation per additional experiment drops below a threshold:

$$\frac{\partial P(H_T)}{\partial N} \to 0 \quad \text{as} N \to \infty$$

The authors calculate that for typical universality arguments (moderate $\Lambda_0 \sim 3$-10), saturation occurs around $N \sim 3$-5 independent realizations. Beyond this, additional analogue experiments have limited epistemic value unless they explore qualitatively new regimes (different parameter spaces, different physical mechanisms).

### Differential Epistemic Value

Different analogue systems contribute differently. The framework predicts:

**System Type A (Weakly analogous):** Shares only global structure with target. $\Lambda_A \sim 1.5$. Moderate confirmation.

**System Type B (Strongly analogous):** Shares local structure, boundary conditions, and effective dynamics with target. $\Lambda_B \sim 10$. Strong confirmation.

**System Type C (Across different physics domains):** Exhibits phenomenon via completely different mechanism but arrives at same observable signature. $\Lambda_C \sim 100$. Strongest confirmation (high universality).

The framework thus provides guidance for experimental investment: resources should prioritize System Type C (maximal domain variation) or Type B (high local analogy), rather than accumulating Type A realizations.

### Accounting for Alternative Hypotheses

The Bayesian framework naturally accommodates alternative explanations. Suppose there are two competing hypotheses: $H_T$ (Hawking radiation in black holes) and $H'_T$ (alternative mechanism producing similar effects). Then:

$$P(H_T | E_1, \ldots, E_N) = \frac{P(E_1, \ldots, E_N | H_T) P(H_T)}{P(E_1, \ldots, E_N | H_T) P(H_T) + P(E_1, \ldots, E_N | H'_T) P(H'_T)}$$

If both $H_T$ and $H'_T$ predict the analogue results with equal likelihood, the analogue experiment does not discriminate between them. Confirmation of $H_T$ requires that $P(E_S | H_T) > P(E_S | H'_T)$.

---

## Key Results

1. **Analogue Experiments Are Confirmatory Under Universality:** When a phenomenon arises from universal principles (independent of microscopic details), observing it in an analogue system provides genuine Bayesian evidence for the target system.

2. **Confirmation Scales Multiplicatively:** $N$ independent realisations yield a combined likelihood ratio $\Lambda^N$. Confirmation accumulates exponentially, enabling rapid confidence growth.

3. **Saturation Limits Marginal Value:** Beyond $N \sim 3$-5 realisations, additional analogue experiments yield diminishing epistemic returns. Resources should be directed to qualitatively new systems or domains.

4. **Epistemic Ranking of Analogue Designs:** Systems with stronger analogies and broader domain variation contribute more confirmation per unit cost. Framework enables optimization of experimental investment.

5. **Prior Probability Matters:** Analogue experiments do not produce certainty from ignorance. A low prior ($p_0 \ll 1$) requires many analogue successes to shift belief substantially. Universality arguments amplify small priors.

6. **Alternative Hypotheses Must Be Addressed:** Analogue results alone do not rule out alternative explanations; the framework requires explicit consideration of competing theories and their predicted probabilities.

7. **Quantitative Prediction of Confirmation:** The framework produces numerical predictions of confirmation increments, enabling comparison across different experimental programs.

---

## Impact and Legacy

This paper has become the reference for quantifying analogue experiments' epistemic value. Its impact includes:

- **Philosophical Rigor in Experimental Planning:** Experimental teams now cite the Bayesian framework when justifying analogue proposals, explicitly invoking universality arguments and estimating marginal confirmation gains.

- **Resolution of the Crowther Debate:** While not entirely rebutting the circularity objection, Dardashti et al. show that circularity can be avoided if universality is sufficiently robust. The debate shifted from "can analogs ever confirm?" to "under what conditions are universality arguments justified?"

- **Comparative Assessment:** The framework enabled comparison of competing experimental programs (e.g., acoustic black holes vs. photonic systems vs. cold-atom systems), helping allocate resources to the highest-value efforts.

- **Meta-Scientific Tool:** The saturation feature has been applied beyond physics—to astrobiology, climate modeling, and other domains where direct access to a system is impossible.

---

## Connection to Phonon-Exflation Framework

**The Framework as a Test of Universality:**

The phonon-exflation framework predicts specific values for fundamental constants (e.g., $\sin^2\theta_W = 3/8$, fine-structure constant $\alpha \approx 1/137$, mass ratios) derived from the SU(3) spectral geometry. These predictions are analogous in the Dardashti sense: if they hold across multiple independent observational domains (precision electroweak tests, cosmology, astrophysics), the framework's universality argument is strengthened.

**Multi-Domain Confirmation:**

The framework's predictions have been tested across:
- Precision measurements of $\alpha$ (S35, ALPHA-ENV-43).
- Spectroscopic observations (LRD masses, formation rates).
- Cosmological constraints (DESI BAO, S8 tension).
- Fundamental constant variations (JWST spectral features).

Each independent observational domain acts as an "analogue realization" in the Dardashti sense. If the framework's predictions hold across all these domains (analogous to seeing Hawking radiation in five different laboratory systems), the Bayesian confirmation accumulates multiplicatively.

**Saturation Consideration:**

According to the Dardashti analysis, the framework's confirmation from cosmological tests is approaching saturation: 3-5 independent tests (DESI S8, JWST LRD masses, ALPHA-ENV, BBN constraints, CMB polarization) may represent the threshold beyond which marginal returns diminish. Further confirmation would require:
- Qualitatively new physics (e.g., detection of GWs with polarization signature).
- Tests in regimes previously unexplored (e.g., TeV-scale collider signatures, cosmic-ray anomalies).
- Independent domains fundamentally disconnected from cosmology and astrophysics.

**Addressing Alternative Hypotheses:**

The Dardashti framework requires explicit accounting for competing theories (LCDM, modified gravity, quintessence, etc.). The framework's posterior probability depends not just on how well it explains observations but on how these probabilities compare to alternatives:

$$P(\text{phonon-exflation} | \text{data}) \propto \frac{P(\text{data} | \text{phonon-exflation})}{P(\text{data} | \text{LCDM, alternatives})}$$

If LCDM and the framework fit the data equally well, the framework gains no confirmation relative to LCDM, even if both fit better than alternative theories.

**Universality Argument for the Framework:**

The strongest universality claim would be: "The SU(3) spectral structure is universal—any physical system exhibiting this symmetry should exhibit the predicted spectrum, regardless of whether it's cosmological, condensed-matter, or quantum-field-theoretic."

If this universality can be established theoretically (via group-theoretic or topological arguments), then observations of the predicted spectrum in diverse physical domains accumulate confirmation exponentially.

---

## References and Further Reading

- Dardashti, R., Hartmann, S., Thébault, K. P. Y., & Winsberg, E. (2019). "Hawking radiation and analogue experiments: A Bayesian analysis." *Studies in History and Philosophy of Science Part B: Studies in History and Philosophy of Modern Physics*, 67, 1–11.
- Crowther, K., Linnemann, N., & Wüthrich, C. (2019). "What we cannot learn from analogue experiments." *Synthese*, 198(16), 3701–3726.
- Thébault, K. P. Y. (2019). "What can we learn from analogue experiments?" *Studies in History and Philosophy of Science Part B: Studies in History and Philosophy of Modern Physics*, 68, 1–13.
- Shackel, N. (2004). "How to do the history of philosophy of physics: Reflections on Sklar." *British Journal for the Philosophy of Science*, 55(3), 513–540.
- Mayo, D. G. (1996). *Error and the Growth of Experimental Knowledge.* University of Chicago Press.
