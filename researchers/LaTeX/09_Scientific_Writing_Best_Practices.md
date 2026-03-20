# Scientific Writing Best Practices for Physics Papers

**Author(s):** Physics Community, Academic Writing Standards
**Year:** 2020+ (contemporary standards)
**Reference:** "How to Write a Paper" (journals), "A Student's Guide to Research" (various)

---

## Abstract

Clear scientific writing is as important as correct mathematics. This document covers structural principles for theoretical physics papers: abstract design, introduction strategy, methodology clarity, results presentation, discussion/conclusion balance, and referee-friendly composition. Emphasis is placed on mathematical physics papers (spectral action, NCG) versus experimental/observational papers. The guidelines are tailored to journals like JGP, CMP, PRD, and JHEP.

---

## Historical Context

The modern scientific paper structure (abstract, introduction, methodology, results, discussion, references) emerged in the mid-20th century and was formalized by physics and biology communities. Different journals emphasize different sections: experimental papers stress methodology and results; theoretical papers emphasize rigor and connection to prior work. Mathematical physics papers (e.g., CMP) prioritize mathematical correctness and novelty of structures.

For phonon-exflation: The no-go paper emphasizes negative results (killed mechanisms); the Spectral Anatomy paper emphasizes positive mathematical theorems. These require different narrative strategies.

---

## Paper Structure: Template

### 1. Title

Clear, specific, searchable.

**Bad**: "On Cosmology"
**Good**: "Spectral Action Principle on Noncommutative SU(3): A No-Go Result for Starobinsky Inflation"

### 2. Abstract

50-250 words. State:
- Problem/motivation (1-2 sentences)
- Main result or finding (1-2 sentences)
- Methods/approach (1 sentence)
- Implications (1-2 sentences)
- **No citations, no equations** (with rare exception in specialized fields)

**Example for no-go paper**:

"We investigate the spectral action principle applied to the Jensen-deformed SU(3) manifold, seeking a mechanism for cosmological inflation. Using noncommutative geometry, we compute the Seeley-DeWitt coefficients exactly and find that the quadratic curvature term dominates the linear term by a factor of 1000 at the base scale. This prevents Starobinsky inflation from emerging. We conclude that Starobinsky-type mechanisms cannot stabilize the spectral action on compact Lie groups of dimension >4."

---

## Introduction: Strategy and Sections

### Opening Gambit (2-3 paragraphs)

Establish context and significance **without technical detail**.

Example opening:
"The nature of cosmic expansion remains one of the deepest puzzles in physics. The standard Lambda-CDM model invokes a mysterious dark energy with equation of state $w = -1$. Alternative theories propose that geometry itself may generate inflation. Among these, the spectral action principle of noncommutative geometry offers a mathematically rigorous framework where physical law emerges from spectral geometry of spacetime."

### Literature Review (2-5 paragraphs)

- Connes' NCG framework (establish authority)
- Baptista's KK geometry (our foundation)
- Paasch's mass quantization (phonon-exflation predecessor)
- Inflation mechanisms (Starobinsky, slow-roll)
- **Explicitly state the gap**: "Yet the application to cosmology has remained incomplete, particularly regarding the coupling between metric dynamics and infrared stabilization."

### Motivation for This Work (1-2 paragraphs)

- State specific question: "Can the spectral action principle generate inflation on SU(3) with finite-dimensional quantum systems?"
- Explain why it matters: "A positive answer would reconcile quantum geometry with cosmology. A negative answer would guide future research toward mechanisms requiring additional structure."

### Roadmap (1 paragraph)

"In Section 2, we review NCG and spectral triples. Section 3 applies Jensen deformation to SU(3) and computes the Dirac spectrum numerically. Section 4 derives the spectral action via Seeley-DeWitt. Section 5 presents our main results: the no-go theorem for Starobinsky inflation. Section 6 discusses implications and closes with an agenda for extensions."

---

## Methodology: Technical Exposition

For theoretical papers, clarity of method is paramount.

### Define Your Objects

```latex
\section{Spectral Triple on SU(3)}

We work with the spectral triple $(A, \mathcal{H}, D)$ where:

\begin{itemize}
  \item $A = C^{\infty}(\text{SU}(3))$ is the algebra of smooth functions.
  \item $\mathcal{H} = L^2(\text{SU}(3)) \otimes S$ is the Hilbert space of
        $L^2$ spinors on SU(3).
  \item $D = D_K(\tau)$ is the Jensen-deformed Dirac operator,
        parameterized by $\tau \in [0, 0.5]$.
\end{itemize}

The spectral triple must satisfy three axioms...
```

### Use Theorems and Lemmas

For papers in JGP or CMP, structure proofs formally:

```latex
\begin{theorem}[Block-Diagonality]
The Dirac operator $D_K$ is exactly block-diagonal
in the Peter-Weyl basis of $\text{SU}(3)$.
\end{theorem}

\begin{proof}
By left-invariance, [J^a, D_K] = 0 for all generators $J^a$ of $\mathfrak{su}(3)$.
By Schur's lemma, $D_K$ commutes with the representation matrices,
implying block-diagonality on the Peter-Weyl decomposition.
\end{proof}
```

---

## Results Section: Present, Don't Announce

### For Negative Results (No-Go)

**Structure**: State claim clearly, support with calculation.

```latex
\section{Main Result: Starobinsky Inflation Fails}
\label{sec:main-result}

\begin{theorem}[V_spec Monotonicity]
The spectral action $V_{\text{spec}}(\tau; \rho)$ is monotonically
increasing in $\tau$ for all $\rho \in [0.001, 0.5]$ and all
$\tau \in [0, 0.5]$.
\end{theorem}

\begin{corollary}[No Starobinsky Minimum]
The spectral action has no local minimum in the range
$\tau \in [0, 0.5]$. Therefore, Starobinsky-type inflation
mechanisms cannot be stabilized by the spectral action.
\end{corollary}

\begin{proof}
We compute $a_4(\tau)/a_2(\tau)$ numerically at 50 values of $\tau$.
Figure 1 shows this ratio grows from 1000 at $\tau=0$ to 1400 at $\tau=0.5$.
Since $V_{\text{spec}} \sim a_2 R + a_4 R^2$, the $R^2$ term dominates
and increases monotonically, precluding any minimum.
[Details in Appendix A]
\end{proof}
```

### For Positive Results (Proof)

**Structure**: Build up to the theorem with lemmas.

```latex
\section{Main Result: KO-Dimension Classification}
\label{sec:ko-dimension}

To classify the spectral triple, we appeal to the Atiyah-Singer
KO-dimension index theorem.

\begin{lemma}[Spinor Dimension]
The spinor bundle $S$ over $\text{SU}(3)$ has dimension 16.
\end{lemma}

\begin{theorem}[KO-Dimension]
The spectral triple $(A, \mathcal{H}, D)$ on $\text{SU}(3)$
has KO-dimension 6 modulo 8.
\end{theorem}

\begin{proof}
The spinor dimension 16 = 2^4 determines the KO-class by the
Clifford algebra classification. For complex dimension 3 (real 6),
the KO-class is uniquely determined...
[Complete proof]
\end{proof}
```

---

## Figures and Tables: Presentation

### Caption Strategy

Captions should be **self-contained**.

**Bad**: "Spectrum vs tau."
**Good**: "Eigenvalues of the Dirac operator $D_K(\tau)$ as function of deformation parameter $\tau$. Solid (blue) curves: fermionic modes with gap $\Delta_f(\tau)$. Dashed (red) curves: bosonic modes with gap $\Delta_b(\tau)$. Vertical line at $\tau = 0.2$ marks the phase transition where gap-edge separation becomes algebraic (5/6 vs 4/9). Data computed at 500 mesh points with $N=200$ basis functions."

### Table Presentation

```latex
\begin{table}
\centering
\begin{tabular}{c|c|c|c|c}
  $\tau$ & $\lambda_1$ & $\lambda_2$ & Gap & $V_{\text{spec}}$ \\
  \hline
  0.00 & 1.207 & 0.325 & 0.882 & $-2.14$ \\
  0.10 & 1.310 & 0.375 & 0.935 & $-1.98$ \\
  0.20 & 1.531 & 0.405 & 1.126 & $-1.75$ \\
  0.30 & 1.644 & 0.480 & 1.164 & $-1.52$ \\
\end{tabular}
\caption{Numerical data for [specific what is computed and why].
  Units: [specify]. Computational parameters: [mesh points, basis size, etc.]}
\label{tab:spectrum}
\end{table}
```

---

## Discussion: Connect to Implications

The Discussion section is often neglected but is critical for impact.

### Structure

1. **Restate main finding** (1 paragraph): "We have shown that the spectral action on SU(3) with Jensen deformation does not admit Starobinsky inflation. This contradicts earlier conjectures."

2. **Why does it matter?** (1-2 paragraphs): "This result suggests that the spectral action principle, while mathematically elegant, requires additional mechanisms to generate inflation. Either [mechanism A] must be incorporated, or [mechanism B] must be extended."

3. **Limitations and caveats** (1 paragraph): "Our analysis assumes KO-dimension 6. Extension to higher-dimensional internal spaces remains open. We also neglect loop corrections, which could in principle modify the spectral action."

4. **Future directions** (1 paragraph): "Three avenues merit investigation: (1) Incorporating fermionic condensates, (2) Adding explicit gauge-field coupling, (3) Extending to non-associative algebras."

---

## Conclusion: Decisive and Brief

**Rule**: Never introduce new results in Conclusion.

**Good conclusion**:
"We have established that Starobinsky-type inflation cannot emerge from the spectral action on SU(3). The mathematical framework is sound, but the physical dynamics preclude this mechanism. Future research must explore alternative geometric stabilization schemes or accept that spectral geometry alone cannot generate cosmological inflation."

---

## Mathematical vs Experimental Paper Structure

### Mathematical Physics (JGP, CMP target)

1. **Abstract** - Result + novelty
2. **Introduction** - Context + motivation + roadmap
3. **Setup** - Define objects, state axioms
4. **Main Theorem** - Explicit, numbered
5. **Proof** - Complete, rigorous
6. **Corollaries** - Applications
7. **Conclusion** - Implications
8. **References**

### Observational/Experimental (PRD target)

1. **Abstract** - Motivation + data + conclusion
2. **Introduction** - Context + prior work + gaps
3. **Data/Methods** - Instrumentation, calibration, statistical approach
4. **Analysis** - Processing pipeline
5. **Results** - Tables, plots, error bars
6. **Discussion** - Interpretation, comparison to models
7. **Conclusion** - Summary
8. **References**

---

## Reviewer-Friendly Writing

### What Reviewers Want

1. **Clarity**: Can a specialist outside your subfield understand the claim?
2. **Honesty**: Do you acknowledge limitations?
3. **Completeness**: Are all results proven or referenced?
4. **Relevance**: Does this matter to the field?

### Techniques

- **Use headings liberally**: Section headings help reviewers navigate.
- **Define notation upfront**: Introduce all symbols before use.
- **State theorems formally**: Don't hide results in prose.
- **Cite prior work**: Be generous with citations; shows awareness of literature.
- **Acknowledge debt**: "Building on Baptista's framework [Ref], we extend..."

---

## Common Pitfalls in Physics Writing

1. **Equation dumping**: Equations without explanation. Always introduce: "We have the Dirac equation [equation number], which governs..."

2. **Vague references**: "As is known" or "It is clear that..." without citation or proof.

3. **Overstated claims**: "We have proven inflation" when you've only shown one mechanism fails.

4. **Dense paragraphs**: Break long paragraphs into 2-3 shorter ones.

5. **Inconsistent notation**: Use D_K consistently, not D_K in Section 2, D in Section 3.

6. **No figure references**: "Figure 1" appears in caption but text never mentions it.

---

## Stylistic Guidelines

### Tense

- **Established facts**: Use present tense. "The spectral action provides..."
- **Your work**: Use past tense. "We computed the spectrum at 50 values of tau."
- **Future work**: Use future tense. "This approach will be extended to..."

### Voice

**Active voice is preferred in science**:

- Bad: "The spectrum was computed by the authors."
- Good: "We computed the spectrum."

Exception: When agency is irrelevant or abstract.
- OK: "Numerical errors were minimized."

### Paragraphing

Each paragraph should have:
1. Topic sentence (what the paragraph is about)
2. 2-4 supporting sentences
3. Closing sentence (transition to next)

---

## Connection to Phonon-Exflation Framework

Scientific writing standards enable:
- Clear communication of no-go results (V_spec monotone, gap equation failure)
- Rigorous presentation of positive theorems (block-diagonality, KO-dimension=6)
- Professional papers accepted by top mathematical physics venues (JGP, CMP)
- Effective peer review by making claims transparent and provable
- Reproducible science via detailed methodology sections
- Impact in the broader cosmology/theoretical physics community

Relevance to Project: **CRITICAL** - The difference between a publishable paper and rejection often lies in writing clarity, not mathematical correctness.
