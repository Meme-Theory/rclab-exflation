# Do Extraordinary Claims Require Extraordinary Evidence?

**Author(s):** Paul Copan, William Lane Craig
**Year:** 2018
**Journal:** Philosophia, Vol. 46, pp. 1319-1328; philosophical essay

---

## Abstract

We examine the validity and implications of Carl Sagan's famous dictum: "Extraordinary claims require extraordinary evidence." This principle, widely cited in philosophy of science, cosmology, and skepticism, is intuitive but logically problematic. We analyze what "extraordinary" means (improbable? inconsistent with background knowledge? metaphysically grand?), what counts as "evidence" (statistical significance? prior probability? theoretical fit?), and whether the principle is coherent. We argue that Sagan's standard is formally equivalent to a likelihood ratio or Bayesian update, but it introduces semantic ambiguity and potential circularity. We propose a refined formulation: a claim's credibility depends on the strength of the evidence for it relative to plausible alternatives, weighted by prior probability. This standard—the **Bayesian criterion**—is more precise and avoids the pitfalls of Sagan's intuitive version. We discuss applications to contemporary debates (dark energy, inflation, quantum gravity, cosmological fine-tuning) and show that Sagan's principle, while rhetorically powerful, does not settle questions about burden of proof or model selection.

---

## Historical Context

Carl Sagan, the renowned astronomer and science communicator, popularized the phrase "Extraordinary claims require extraordinary evidence" as a shorthand for scientific skepticism. Sagan used it to critique pseudoscience, paranormal claims, and unfounded speculations. The principle appeals to common sense: if a claim is wildly implausible (e.g., "I can read minds"), one should demand strong evidence before believing it.

However, the principle has been frequently invoked in debates about theoretical physics, cosmology, and metaphysics, where "extraordinary" is subjective and "evidence" is multifaceted. In cosmology, for instance:
- Is the claim that dark energy exists "extraordinary"? (Answer: It was, before 1998. Now it is observationally confirmed.)
- Is the claim that multiple universes exist "extraordinary"? (Answer: Philosophically, yes; scientifically, it emerges from inflation theory.)
- Is the claim that quantum gravity modifies spacetime "extraordinary"? (Answer: Yes, but is the evidence for it extraordinary?)

Copan and Craig (2018) argue that Sagan's principle, while superficially appealing, is **logically incoherent as stated** and must be replaced by a more rigorous Bayesian formulation.

---

## Key Arguments and Derivations

### Sagan's Standard (Informal Statement)

The principle is typically stated as:

**"Extraordinary claims require extraordinary evidence."**

What does this mean?

**Interpretation 1: Probabilistic**
A claim with low prior probability $P(H)$ requires a high likelihood ratio $\mathcal{L} = P(D|H) / P(D|\neg H)$ to shift belief to high posterior probability $P(H|D)$.

**Interpretation 2: Pragmatic**
Claims inconsistent with well-established background knowledge (e.g., the laws of thermodynamics) require evidence comparable in weight to the evidence that established the background knowledge in the first place.

**Interpretation 3: Metaphysical**
Claims that posit novel entities or fundamentally new physics (e.g., new particle types, new dimensions, new forces) require more rigorous evidence than claims adjusting parameters of existing theories.

### Bayesian Reformulation

Bayes' theorem states:

$$ P(H|D) = \frac{P(D|H) P(H)}{P(D)} = \frac{P(D|H) P(H)}{P(D|H) P(H) + P(D|\neg H) P(\neg H)} $$

Define the **likelihood ratio** (Bayes factor):

$$ B = \frac{P(D|H)}{P(D|\neg H)} $$

Then:

$$ \frac{P(H|D)}{P(\neg H|D)} = B \cdot \frac{P(H)}{P(\neg H)} $$

**The posterior odds are the prior odds times the likelihood ratio.**

Now, consider two claims: H1 (ordinary) and H2 (extraordinary). Suppose both predict the same data D equally well, so $B_1 = B_2$. However, P(H1) >> P(H2) (the ordinary claim is more probable a priori). Then:

$$ \frac{P(H1|D)}{P(\neg H1|D)} >> \frac{P(H2|D)}{P(\neg H2|D)} $$

**The same evidence favors the ordinary claim more strongly.** For H2 to be favored despite lower prior, it must have a **larger likelihood ratio** (stronger evidence). This is Sagan's principle in Bayesian form.

### The Problem of Vagueness

Sagan's standard uses three undefined terms:

1. **"Extraordinary"**: Does this refer to:
   - Low prior probability? (subjective; depends on the observer's knowledge)
   - Inconsistency with established laws? (but every revolutionary theory seems inconsistent until confirmed)
   - High novelty? (but how much novelty triggers the "extraordinary" label?)

2. **"Claims"**: What is a claim? A specific hypothesis? A model family? A theory?

3. **"Evidence"**: Does this mean:
   - Statistical significance? (p-values, confidence intervals)
   - Likelihood ratio? (model comparison)
   - Posterior probability? (depends on prior choice)

Without clear definitions, Sagan's principle devolves into rhetoric: a speaker labels a claim "extraordinary" (implicitly dismissing it) and then demands "extraordinary evidence" (setting a high and possibly arbitrary bar).

### Copan-Craig Critique

**Problem 1: Circularity**

Suppose you believe the Standard Model of particle physics with high confidence. A new claim contradicts the SM and is therefore "extraordinary." By Sagan's principle, it requires "extraordinary evidence." But what counts as extraordinary evidence? Copan and Craig argue this is circular: **you're using the very theory you're evaluating to set the evidentiary bar.**

**Example**: In the 1960s, neutrinos were hypothesized on theoretical grounds but had not been directly detected. The claim "neutrinos exist" contradicted observational knowledge (no direct detection) and was "extraordinary." Yet weak evidence from beta-decay kinematics was sufficient because the theoretical motivation was strong. Sagan's principle would have demanded even stronger evidence, potentially excluding the correct answer.

**Problem 2: Asymmetry**

Sagan's principle treats the claim H and its negation $\neg H$ asymmetrically. If H is "extraordinary," then demanding high evidence for H is reasonable. But $\neg H$ may also be extraordinary (e.g., "dark energy does not exist" contradicts 1998 supernova observations). Should $\neg H$ also require extraordinary evidence?

Bayesian reasoning treats them symmetrically: whichever hypothesis (H or $\neg H$) has lower prior should require stronger likelihood to be favored.

**Problem 3: Prior Dependence**

The threshold for "extraordinary evidence" depends on the prior probability of H. But priors are subjective (different experts may assign different priors). Sagan's principle fails to address this subjectivity.

**Example**: An astrophysicist and a philosopher may assign different prior probabilities to the existence of a multiverse (prior range: 10% to 90%). Sagan's principle gives no guidance on whose prior is correct, and thus cannot determine whether current evidence is "extraordinary" enough.

### The Refined Bayesian Standard

Copan and Craig propose:

**The credibility of a claim H given data D is determined by:**

$$ \text{Credibility}(H | D) = \frac{P(D|H) P(H)}{P(D|H) P(H) + \sum_i P(D|H_i) P(H_i)} $$

**In plain language:**
1. List all plausible hypotheses (H, H1, H2, ...).
2. Assign prior probabilities to each (based on theoretical motivation, background knowledge, etc.).
3. For each hypothesis, compute the likelihood of the observed data.
4. Apply Bayes' theorem to update posterior probabilities.
5. The hypothesis with the highest posterior probability is most credible.

**Advantages of this formulation:**
- **Precise**: Probabilities are explicit; subjective priors are declared openly.
- **Symmetric**: All hypotheses are treated the same way.
- **Consistent**: Incorporates both prior knowledge and new evidence in a principled way.
- **Falsifiable**: You can check whether the resulting posterior matches expert consensus.

---

## Key Results

1. **Sagan's Principle is Incoherent as Stated**: The phrase "extraordinary claims require extraordinary evidence" uses undefined terms and invites circular reasoning. It is intuitive but not rigorous.

2. **Bayesian Reformulation Clarifies the Issue**: When translated to Bayesian terms, the principle becomes: claims with low prior probability require high likelihood ratios to be favored. This is tautological—it's a logical truth, not an empirical principle.

3. **Subjectivity Cannot Be Avoided**: Any principled approach to evidence evaluation requires assigning prior probabilities, which are unavoidably subjective (though informed by background knowledge). Sagan's principle does not solve this problem; it obscures it.

4. **Rhetorical Power vs. Logical Rigor**: Sagan's phrase is powerful rhetoric (it correctly conveys that skepticism is warranted for outlandish claims), but it is not a rigorous scientific principle.

5. **Applications to Contemporary Physics**:
   - **Dark energy (1998)**: The claim "the universe is accelerating" contradicted prior expectations. It was "extraordinary." But the evidence (Type Ia supernovae distances, CMB-BAO consistency) was statistically robust. Sagan's principle would have demanded even more evidence, but the claim was correct. This suggests the principle was too conservative.
   - **Inflation (1980s)**: The claim "the universe underwent exponential expansion in the early universe" was speculative and "extraordinary." But it explained key observations (flatness of universe, abundance of primordial elements) and made testable predictions (CMB anisotropy spectrum). Sagan's principle would demand extraordinary evidence, but moderate evidence suffices because the explanatory power is high.
   - **Dark matter**: The claim "most of the universe's matter is non-luminous and weakly interacting" was "extraordinary" in the 1970s. Evidence was indirect (galaxy rotation curves). Yet the claim is now widely accepted. Sagan's principle was again too conservative.

6. **The Standard Applies to All Claims Equally**: Extraordinariness is not a property of a claim itself but a relationship between the claim and an observer's prior knowledge. The same claim is ordinary to one expert and extraordinary to another. Bayesian reasoning accommodates this; Sagan's principle does not.

---

## Impact and Legacy

The Copan-Craig paper (2018) is a philosophical critique of a widely invoked scientific maxim. Its impact:

1. **Philosophical Rigor**: The paper elevated the discussion of Sagan's principle from rhetorical invocation to formal analysis, establishing that the principle requires Bayesian interpretation to be coherent.

2. **Practical Guidance for Science**: The refined Bayesian standard is now recommended in philosophy of science and scientific methodology courses. It emphasizes the importance of explicit prior assignments and model comparison rather than vague appeals to burden of proof.

3. **Debates on Fine-Tuning and Multiverse**: The paper's analysis applies directly to contemporary debates in cosmology:
   - Is the claim "the cosmological constant is fine-tuned to 120+ decimal places" extraordinary? Yes, in that it contradicts expectations of naturalness.
   - Does this constitute evidence for a multiverse (where different universes have different Lambda)? Not by Sagan's principle alone; it requires comparing the posterior probability of the multiverse to single-universe hypotheses.
   - The Bayesian framework clarifies: the multiverse hypothesis must have not just lower prior (fewer expected universes) but also higher likelihood (better explaining the observed fine-tuning) to be favored.

4. **Limits of Skepticism**: The paper also highlights a risk: using Sagan's principle to dismiss unconventional claims can freeze paradigms. Revolutionary theories (heliocentrism, evolution, quantum mechanics) were "extraordinary" but are now standard. The principle must be applied judiciously, with explicit consideration of both prior probability and evidential strength.

---

## Connection to Phonon-Exflation Framework

**Phonon-exflation is an "extraordinary claim" by Sagan's standard, and the framework must justify its extraordinary evidence demands.**

Key connections:

1. **The Claim**: Phonon-exflation proposes that particles are phononic excitations of a compactified M4 x SU(3) manifold, and dark energy arises from the spectral action on this geometry. This is philosophically grand (reinterprets the Standard Model and gravity as emergent phenomena) and theoretically novel (noncommutative geometry).

2. **Prior Probability**: In the landscape of theoretical physics (string theory, quantum gravity, loop quantum gravity, causal dynamical triangulations, etc.), phonon-exflation is one of many speculative frameworks. Its prior probability is low—say, P(phonon-exflation) ~ 1-5% among viable alternatives.

3. **Evidence Demanded**: By Sagan's principle (or the Bayesian refinement), the framework must provide evidence with likelihood ratio $\mathcal{L} = P(D | \text{phonon-exflation}) / P(D | \text{LCDM})$ sufficiently high to overcome its low prior. What is "sufficiently high"? The Bayes factor should be >> 1, ideally > 3 (moderate evidence).

4. **Current Empirical Status**:
   - **Particle physics**: Phonon-exflation reproduces SM quantum numbers from NCG geometry. However, it fails to predict sin²θ_W and mass ratios correctly (Sessions 23-24). Evidence: weak, slightly negative (the predictions are off).
   - **Cosmology**: Phonon-exflation predicts w = -1 (static dark energy). DESI 2025 measures $w_0 = -0.72$ with 4.7-sigma deviation (Paper 27). Evidence: strongly negative.
   - **Fine-tuning**: Phonon-exflation claims to address the cosmological constant problem via geometric BCS dynamics. This is speculative (BCS integration not yet performed). Evidence: neutral to negative (claim not yet substantiated).

5. **Sagan's Verdict**: Phonon-exflation makes extraordinary claims but currently provides **no** evidence with likelihood ratio > 1. The best evidence (particle physics) is weak; the cosmology evidence (DESI w deviation) is negative. By Copan-Craig's Bayesian standard, the posterior probability of phonon-exflation is **lower than its prior**, because current data are less likely under the framework than under LCDM.

6. **What Evidence Would Suffice?**: To overcome its low prior (1-5%), phonon-exflation would need:
   - **Prediction of sin²θ_W to better than 1% precision** (current prediction 3/8 = 0.375; measured 0.231; error ~ 60%)
   - **Prediction of w(z) that matches DESI DR2** (current prediction w = -1; measured w0 ~ -0.72)
   - **A derivation of the SM mass spectrum from geometry alone**, without additional fitting parameters
   - **A demonstrated mechanism for BCS gap energy to exactly cancel vacuum energy**, removing fine-tuning

   Until these are achieved, the framework remains extraordinary in both claim and (lack of) evidence.

---

## Appendix: Bayesian Model Comparison Example

**Scenario**: Compare LCDM vs. Phonon-Exflation using DESI 2025 data.

**Priors**:
- P(LCDM) = 0.95 (standard model of cosmology, 30+ years of consistency)
- P(Phonon-Exflation) = 0.05 (novel framework, not yet widely accepted)

**Likelihoods** (based on Paper 27):
- $P(D | \text{LCDM}) \propto \exp(-\chi^2_\text{LCDM} / 2) = \exp(-47.3 / 2)$ [χ² = 47.3]
- $P(D | \text{Phonon-Exfl}) = ?$ [Framework predicts w = -1; data favor w ~ -0.72. Likelihood is low.]

If phonon-exflation uses w = -1 (no freedom to adjust), then:
$$\chi^2_\text{Phonon-Exfl} > 47.3 \quad (\text{worse than LCDM})$$

Suppose $\chi^2_\text{Phonon-Exfl} = 65$ (fitting poorly). Then:
$$\mathcal{L}_\text{Phonon-Exfl} / \mathcal{L}_\text{LCDM} = \exp(-(65-47.3)/2) = \exp(-8.85) \approx 0.0001$$

**Posterior odds**:
$$\frac{P(\text{Phonon-Exfl} | D)}{P(\text{LCDM} | D)} = \frac{0.05}{0.95} \times 0.0001 = 0.0000526$$

The framework is **200,000× less likely** given the data. This is a decisive rejection.

**Conclusion**: By Bayesian reasoning (the Copan-Craig standard), phonon-exflation is **extraordinarily unlikely** given current data. Either the framework must be revised (e.g., by allowing w to evolve), or it should be abandoned.

