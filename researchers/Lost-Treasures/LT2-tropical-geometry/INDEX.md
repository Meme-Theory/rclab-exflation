# Lost Treasures 2: Tropical Geometry Applied to Spectral Theory and Physics

## Overview

This folder contains three comprehensive reference documents on tropical geometry—a branch of algebraic geometry studying piecewise-linear limits via non-Archimedean valuations—applied to spectral theory, integrable systems, and non-Hermitian physics.

The central question guiding this collection is: **Can the BCS staircase $E_{GS}(N)$ be understood as a tropicalization of the spectral action?**

Tropical geometry provides tools for:
- Characterizing spectral degeneracies (exceptional points, avoided crossings) via valuations and Newton polygons
- Parameterizing integrable system solutions using tropical theta functions (piecewise-linear analogues of Riemann theta functions)
- Understanding how classical smooth dynamics become discrete/piecewise-linear in non-Archimedean limits
- Connecting Yang-Baxter integrability to soliton dynamics and scattering

## Papers

### 1. Tropical Spectral Curves, Fay's Trisecant Identity, and Generalized Ultradiscrete Toda Lattice
- **Authors:** Rei Inoue and Shinsuke Iwao
- **Year:** 2010
- **arXiv:** 1003.0057
- **Themes:** Tropical geometry of integrable systems, ultradiscrete limits, tropical Riemann theta functions, tropical Jacobian varieties
- **Key Result:** Tropical Fay identity generalized to arbitrary genus tropical curves; general solutions to T(M,N) via tropical theta functions
- **Relevance:** Direct template for expressing the Toda lattice spectral curve as a piecewise-linear object. If BCS quasi-particle spectrum has Toda-like structure, tropical methods apply directly.

### 2. A Tropical Geometric Approach to Exceptional Points
- **Authors:** Ayan Banerjee, Rimika Jaiswal, Madhusudan Manjunath, and Awadhesh Narayan
- **Year:** 2023
- **arXiv:** 2301.13485
- **Themes:** Tropical characterization of non-Hermitian degeneracies, Newton polygons, amoebas, exceptional points, non-Hermitian skin effect
- **Key Result:** EP order determined by tropical roots (bend loci); universality under disorder; holonomy preserved in tropical limit
- **Relevance:** Framework for classifying degeneracies (avoided crossings) in any spectral problem. BCS level crossings could be characterized via tropical polynomial tropicalization.

### 3. Integrable Structure of Box-Ball Systems: Crystal, Bethe Ansatz, Ultradiscretization and Tropical Geometry
- **Authors:** Rei Inoue, Atsuo Kuniba, and Taichiro Takagi
- **Year:** 2012
- **Journal:** Journal of Physics A, Vol. 45
- **arXiv:** 1109.5349
- **Themes:** Box-ball cellular automaton, ultradiscrete integrable systems, crystal bases, Yang-Baxter structure, tropical Jacobi inversion
- **Key Result:** Double origin of integrability (quantum and classical limits meet in ultradiscrete systems); elastic soliton scattering encoded in R-matrix; solutions via tropical theta functions
- **Relevance:** Demonstrates how discrete solitonic systems (balls in boxes = Cooper pairs in a trap?) remain integrable and solvable via tropical methods. Suggests BCS might admit hidden integrable structure.

---

## Thematic Grouping

### Tropical Geometry Fundamentals
- Paper 1, Sections 2.1--2.3: Introduction to tropical curves, tropicalization, smooth tropical curves
- Paper 2, Section "Tropical Semiring and Valuations": Definition of tropical operations and valuations
- Paper 3, Section "Ultradiscretization and Tropical Geometry": Process of passing from classical to tropical via non-Archimedean limits

### Spectral Curves and Jacobian Varieties
- Paper 1, Sections 2.5, 3.1: Tropical Jacobian as quotient $\mathbb{R}^g / \mathbb{Z}^g B$; isolevel sets isomorphic to Jacobians
- Paper 3, Section "Spectral Curves in the Tropical Setting": Mapping algebraic spectral curves to tropical curves; theta-function parameterization preserved

### Integrable Systems and Solitons
- Paper 1, Sections 3.2--4.3: Generalized Toda lattice T(M,N), Lax pairs, spectral polynomials, bilinear form
- Paper 3, Sections "Box-Ball System as Ultradiscrete Toda" and "Solitons and Tropical Geometry": Connection between Toda lattice and BBS; elastic scattering via Yang-Baxter

### Non-Hermitian Systems and Degeneracies
- Paper 2, Sections "Proposition 2" through "Three-Site Gain-Loss Model": Tropical characterization of exceptional point orders; Newton polygons as diagnostic tools
- Paper 2, Sections "Non-Hermitian SSH Model" and "Hatano-Nelson Model with Disorder": Applications to model non-Hermitian systems; universality under disorder

### Theta Functions: Classical and Tropical
- Paper 1, Section 2.3: Tropical Riemann theta function definition and quasi-periodicity
- Paper 3, Section "Tropical Riemann Theta Functions and BBS Solutions": Parameterization of integrable system solutions via tropical theta functions

---

## Framework Relevance Matrix

| Framework Concept | Paper 1 | Paper 2 | Paper 3 | BCS Connection |
|:---|:---:|:---:|:---:|:---|
| Spectral curves | **XXX** | X | **XXX** | Quasi-particle spectrum as curve? |
| Tropical theta functions | **XXX** | - | **XXX** | Parameterize BCS pairing states? |
| Jacobian varieties | **XX** | - | **XX** | Phase space of pairing configs? |
| Exceptional points / avoided crossings | X | **XXX** | - | Level crossings in BCS |
| Yang-Baxter integrability | - | - | **XXX** | Hidden BCS structure? |
| Ultradiscretization | **XX** | - | **XXX** | BCS as discrete limit? |
| Newton polygons / amoebas | - | **XXX** | - | Visualize avoided crossing patterns |
| Conserved charges | **XX** | - | **XXX** | Pairing number, total energy |
| Elastic scattering | - | - | **XX** | Pair interactions? |

---

## Open Questions

1. **Does the BCS ground-state staircase $E_{GS}(N)$ exhibit a tropical spectral curve structure?**
   - If yes: use tropical theta functions to parameterize the staircase without solving mean-field equations
   - If no: what obstruction prevents tropicalization? (Fermion sign problem? Pair-nonconservation interactions?)

2. **Is the Bogoliubov-de Gennes Hamiltonian Yang-Baxter integrable or deformable to Yang-Baxter form?**
   - If yes: apply combinatorial Bethe ansatz / crystal base methods to BCS
   - If no: identify the integrable subalgebra (Richardson-Gaudin model has been shown related; see framework status)

3. **How does the tropical limit of the Dirac spectrum in NCG relate to the phonon-exflation spectral action?**
   - The spectral action is $S[\mathcal{D}] = \sum \lambda_i$ over Dirac eigenvalues
   - In a piecewise-linear (tropical) limit, could this become min-plus arithmetic on eigenvalue loci?

4. **Can Volovik's 3He-A phonon dispersion be tropicalized to recover BBS-like dynamics?**
   - Superfluid 3He-A has gapless chiral phonons; tropicalizing the dispersion might yield discrete phonon solitons
   - Would directly link phonon-exflation cosmology to integrable systems

5. **What is the Newton polygon of the BCS quasi-particle characteristic polynomial?**
   - For weak coupling, does it exhibit transitions (tangencies, edge changes) as pairing parameters vary?
   - Do such transitions correlate with level-crossing phenomena?

---

## Recommended Reading Order

**For new readers:**
1. Start with Paper 2 (Banerjee et al. 2023): Most accessible, concrete examples (gain-loss models, SSH model), visual (amoebas, Newton polygons)
2. Move to Paper 3 (Kuniba et al. 2012): Broader historical context, connection of quantum and classical limits
3. Deep dive into Paper 1 (Inoue--Iwao 2010): Advanced technical details, tropical Fay identity, proofs

**For framework users:**
1. Skim Paper 1, Section 2 (tropical basics) for notation
2. Use Paper 2 for methodology (tropicalization, Newton polygon construction, disorder robustness)
3. Reference Paper 3 for integrable systems interpretation (spectral curves, theta functions, solitons)

**For BCS/phonon-exflation connection:**
1. Read Paper 3, Section "Tropical Riemann Theta Functions and BBS Solutions" for the parameterization template
2. Study Paper 1, Section 4 (T(3,2) example) for how theta functions solve a concrete integrable system
3. Examine Paper 2's "Newton Polygons and Amoebas" section for visualizing avoided crossings
4. Attempt to construct the tropical spectral curve of the Bogoliubov-de Gennes Hamiltonian

---

## Key Equations & Concepts (Quick Reference)

| Concept | Definition | Paper | Section |
|:---|:---|:---:|:---|
| **Tropical polynomial** | $\text{Val}(X,Y) = \min_w[\text{val}(a_w) + w_1 X + w_2 Y]$ | 1 | 2.1 |
| **Good tropicalization** | Curve + fibers are nonsingular | 1 | 2.1 |
| **Tropical root** | Bend locus of piecewise-linear function | 1, 2 | 2.1, "Tropicalization of Characteristic..." |
| **Tropical Riemann theta** | $\Theta(Z;B) = \min_{m \in \mathbb{Z}^g}[...]$ | 1, 3 | 2.3, "Tropical Riemann..." |
| **Tropical Jacobian** | $J(\Gamma) = \mathbb{R}^g / \mathbb{Z}^g B$ | 1, 3 | 2.5, "Spectral Curves..." |
| **Exceptional point order** | Max denominator in Puiseux exponents | 2 | Definition 1 |
| **Newton polygon** | Convex hull of exponent pairs $(\eta, \zeta)$ | 2 | "Newton Polygons..." |
| **Amoeba** | Image of $\log : V \to \mathbb{R}^n$ for algebraic variety | 2 | "Newton Polygons..." |
| **Ultradiscretization** | Tropical limit via $\hbar \to 0$, logarithmic re-scaling | 3 | "Ultradiscretization..." |
| **Box-ball system** | Discrete cellular automaton with conserved quantities | 3 | "The Box-Ball System Defined" |

---

## Suggested Extensions

1. **Search for tropical geometry in BdG literature:** Query for "piecewise-linear," "min-plus algebra," or "tropical" in quasi-particle energy calculations
2. **Construct tropical spectral curve for 2-level BCS model:** Start with the simplest case (single pair level) and build up
3. **Test tropical Jacobi inversion on BCS pairing dynamics:** Use tropical theta functions to predict $E_{GS}(N)$ without mean-field calculation
4. **Examine Volovik phonon dispersion for Yang-Baxter structure:** Check if 3He-A phonon Hamiltonian decomposes into R-matrices
5. **Investigate Richardson-Gaudin integrability of BCS:** This algebraic structure is known related to BCS; tropical treatment might reveal hidden solitonic aspects

