# LaTeX Typesetting Reference Index

**Subject**: LaTeX Typesetting for Theoretical Physics
**Documents**: 14 (reference guides and style documentation)
**Primary domain**: Scientific document preparation, mathematical typesetting, journal submission
**Project relevance**: Essential for Session 25 paper preparation -- producing publication-ready manuscripts for PRD, JHEP, JGP, and CMP from the phonon-exflation computation results.

---

## Dependency Graph

```
FOUNDATIONS                          NOTATION & CONTENT
===========================          ===========================

[01] LaTeX Fundamentals ----------+
  |                               |
  v                               v
[02] AMS Mathematical -----+    [06] Differential Geometry ---+
  |                         |      |                           |
  v                         |      v                           |
[03] REVTeX (PRD) ----+     |   [07] Spectral Theory / NCG --+---+
  |                   |     |      |                           |   |
  v                   |     |      v                           |   |
[04] JHEP Style ------+     +-> [10] Symbol Conventions ------+   |
  |                   |            |                               |
  v                   |            v                               |
[05] BibLaTeX --------+     +-> [13] Custom Macros ---------------+
                      |     |    (phonon_exflation.sty)
                      |     |
                      v     v
SUBMISSION            |   PRESENTATION
===============       |   ===========================
                      |
[12] ArXiv Workflow <-+   [08] TikZ / PGF Diagrams
                      |     |
                      |     v
                      +-> [11] Figure & Table Best Practices
                      |
                      +-> [09] Scientific Writing
                      |
                      +-> [14] JGP / CMP Style
```

**Critical chains for this project**:
- No-go paper: 01 -> 02 -> 07 -> 13 -> 09 -> 04/14 -> 12
- Spectral Anatomy paper: 01 -> 02 -> 06 -> 07 -> 13 -> 09 -> 14 -> 12
- Shared infrastructure: 10 + 13 -> `phonon_exflation.sty` (used by all papers)

---

## Topic Map

### A. LaTeX Foundations (Documents 01, 02)
Document classes, preamble structure, sectioning, floats, cross-referencing, theorem environments, amsmath equation environments, symbol families, delimiter scaling, matrix environments. Required by all papers. **CRITICAL**.

### B. Journal-Specific Styles (Documents 03, 04, 14)
REVTeX for PRD (03), jheppub for JHEP (04), article class for JGP/CMP (14). Each venue has distinct formatting, bibliography, and figure requirements. Venue selection: no-go paper -> JGP or JHEP; Spectral Anatomy -> CMP. **CRITICAL** (venue-dependent).

### C. Bibliography Management (Document 05)
BibLaTeX with biber backend for JHEP/JGP/CMP. Traditional BibTeX with natbib for REVTeX/PRD. INSPIRE-HEP integration for physics literature. Single master .bib file, venue-specific compilation. **HIGH**.

### D. Physics Notation (Documents 06, 07, 10)
Differential geometry (tensors, covariant derivatives, Riemann curvature, Dirac operator, KK metric). Spectral theory / NCG (spectral triples, heat kernel, spectral action, KO-dimension, Peter-Weyl). Symbol conventions (index hierarchy, decorations, font families, disambiguation). **CRITICAL** -- the mathematical language of both papers.

### E. Visualization (Documents 08, 11)
TikZ/PGF for inline diagrams (eigenvalue flows, block-diagonal matrices, phase diagrams). Matplotlib-to-PGF pipeline for reproducible figures. booktabs for professional tables. siunitx for units and precision. Color-blind-safe palettes. Journal-specific resolution and size requirements. **HIGH**.

### F. Writing & Structure (Document 09)
Paper architecture for mathematical physics (theorem-proof) vs observational (data-analysis). Abstract formula. Introduction strategy. Results presentation for negative (no-go) and positive (theorem) results. Referee-friendly composition. **CRITICAL**.

### G. Macro Infrastructure (Document 13)
Semantic macros, `\DeclareMathOperator`, `physics` package (braket, derivatives, commutators). Complete `phonon_exflation.sty` template. Version control strategy. Conditional compilation (draft/final, compact/full). **CRITICAL** -- the single most actionable document for paper preparation.

### H. Submission Pipeline (Document 12)
ArXiv account, file preparation (.bbl pre-compilation required), metadata, category selection (hep-th, gr-qc, math-ph), versioning, cross-listing, journal submission timing. **CRITICAL** -- ArXiv posting establishes priority.

---

## Quick Reference

| If your task involves... | Read these documents | Priority |
|:---|:---|:---|
| Starting any paper from scratch | 01, 02, 13 | CRITICAL |
| Spectral action equations, D_K, heat kernel | 07, 02, 13 | CRITICAL |
| Differential geometry, KK metric, tensors | 06, 02 | CRITICAL |
| Block-diagonality theorem, formal proofs | 02, 09, 14 | CRITICAL |
| Notation consistency across papers | 10, 13 | CRITICAL |
| Submitting to CMP or JGP | 14, 12 | CRITICAL |
| Submitting to JHEP | 04, 12 | HIGH |
| Submitting to PRD | 03, 12 | HIGH |
| ArXiv preprint posting | 12 | CRITICAL |
| Bibliography / INSPIRE-HEP | 05 | HIGH |
| Eigenvalue flow diagrams, block matrices | 08, 11 | HIGH |
| Publication-quality figures (matplotlib) | 11, 08 | HIGH |
| Professional tables (data, eigenvalues) | 11 (booktabs, siunitx) | HIGH |
| Paper structure, abstract, introduction | 09 | CRITICAL |
| No-go paper (V_spec monotone, gap failure) | 09, 07, 02, 04/14, 12 | CRITICAL |
| Spectral Anatomy paper (math theorems) | 09, 14, 02, 06, 07, 12 | CRITICAL |
| Custom macros / shared .sty file | 13, 10 | CRITICAL |
| Feynman diagrams | 08 (tikz-feynman) | MEDIUM |
| Commutative diagrams | 08 (tikz-cd) | MEDIUM |
| Draft mode / line numbers for review | 01, 03 | MEDIUM |

---

## Document Entries

---

### Document 01: LaTeX Document Preparation System (Lamport)

- **File**: `researchers/LaTeX/01_Lamport_LaTeX_Document_Preparation_System.md`
- **Year**: --
- **Relevance**: CRITICAL
- **Tags**: `document-class`, `sectioning`, `floats`, `cross-reference`, `theorem-environments`, `preamble`, `figures`, `tables`

**Summary**: Comprehensive reference for LaTeX document structure, class selection, sectioning, floats (figures/tables), and cross-referencing. Covers document classes (article, report, book) and physics-specific variants (revtex4-2, jheppub). Forms the foundation for all subsequent typesetting work.

**Key Results**:
1. Document class selection: `revtex4-2` for PRD, `jheppub` for JHEP, plain `article` for JGP/CMP/arXiv
2. `amsthm` theorem environments: theorem, lemma, proposition, definition, remark
3. Label naming convention: `sec:`, `fig:`, `tab:`, `eq:`, `thm:` prefixes
4. Subfigures via `subcaption` package for multi-panel eigenvalue/spectrum plots
5. Compile chain: pdflatex -> bibtex -> pdflatex -> pdflatex

**Key Commands**:

| Command/Environment | Description | Usage Context |
|:---|:---|:---|
| `\documentclass{revtex4-2}` | APS journal class | PRD submission |
| `\usepackage{jheppub}` | JHEP formatting | JHEP submission |
| `\newtheorem{theorem}{Theorem}[section]` | Numbered theorem env | Block-diag theorem, KO-dim=6 |
| `\begin{figure}[ht]...\end{figure}` | Float figure | Eigenvalue flow plots |
| `\begin{subfigure}` | Multi-panel figures | Round vs Jensen metric comparison |
| `\label{...}` / `\ref{...}` / `\eqref{...}` | Cross-references | All equations and sections |
| `\hypersetup{...}` | Clickable PDF links | arXiv preprint |
| `\appendix` | Switch to appendix numbering | Proof details, computation appendices |

**Dependencies**:
- *Upstream*: None (foundational)
- *Downstream*: ALL other documents (02-14)

---

### Document 02: AMS Mathematical Typesetting Guide

- **File**: `researchers/LaTeX/02_AMS_Mathematical_Typesetting_Guide.md`
- **Year**: --
- **Relevance**: CRITICAL
- **Tags**: `amsmath`, `amssymb`, `amsthm`, `equations`, `alignment`, `operators`, `symbols`, `matrices`, `delimiters`, `theorem-environments`

**Summary**: Covers amsmath (equation environments), amssymb (mathematical symbols), and amsthm (theorem structures). Provides industrial-strength multi-line equation alignment, custom math operators, delimiter scaling, matrix environments, and spacing control. Essential for all mathematical content: tensor calculus, Dirac operators, spectral action, NCG notation.

**Key Results**:
1. Equation environments hierarchy: `equation` (single), `align` (multi-line), `gather` (centered), `multline` (overflow), `split` (sub-alignment)
2. `\DeclareMathOperator` for custom operators: `\tr`, `\diag`, `\spec`, `\sgn`, `\id`, `\rank`
3. Symbol families: `\mathbb` (R,C,Z), `\mathcal` (A,H,S), `\mathfrak` (su(3), so(4))
4. Delimiter scaling: `\left...\right` (automatic), `\big...\Bigg` (manual)
5. `\notag` to suppress numbering; `\numberwithin{equation}{section}` for section-prefixed numbering

**Key Commands**:

| Command/Environment | Description | Usage Context |
|:---|:---|:---|
| `\begin{align}...\end{align}` | Multi-line aligned equations | Derivations (D_K^2, spectral action) |
| `\begin{equation}\begin{split}...\end{split}\end{equation}` | Sub-alignment within single eq | g1/g2 = e^{-2tau} derivation |
| `\DeclareMathOperator{\tr}{tr}` | Custom operator (upright) | Trace in spectral action |
| `\mathbb{R}`, `\mathcal{A}`, `\mathfrak{su}` | Symbol families | Number sets, algebras, Lie algebras |
| `\left( ... \right)` | Auto-scaling delimiters | Large fractions, integrals |
| `\begin{pmatrix}...\end{pmatrix}` | Parenthesized matrix | BdG matrix, Dirac blocks |
| `\notag` | Suppress equation number | Intermediate derivation steps |
| `\text{...}` | Roman text in math mode | Labels within equations |

**Dependencies**:
- *Upstream*: Doc 01 (LaTeX fundamentals)
- *Downstream*: Docs 06, 07, 10, 13 (notation, symbols, macros)

---

### Document 03: REVTeX 4.2 -- Physics Journal Style

- **File**: `researchers/LaTeX/03_REVTeX4_Physics_Journal_Style.md`
- **Year**: --
- **Relevance**: HIGH
- **Tags**: `revtex`, `PRD`, `PRL`, `APS`, `bibliography`, `natbib`, `dcolumn`, `ruledtabular`, `author-affiliation`, `two-column`, `preprint`

**Summary**: Official APS document class for Physical Review journals (PRD, PRL). Covers class options, author/affiliation markup (superscript addressing), BibTeX integration with natbib, decimal-aligned tables via dcolumn, two-column spanning figures, and submission workflows. Required for PRD submission of no-go results or cosmology-focused papers.

**Key Results**:
1. Class invocation: `\documentclass[aps,prd,superscriptaddress]{revtex4-2}`
2. Preprint mode for review: add `linenumbers,preprint` options
3. Multi-author affiliations with `\author{...}` + `\affiliation{...}` blocks
4. `ruledtabular` environment for professional tables; `dcolumn` for decimal alignment
5. Two-column spanning: `figure*` environment
6. BibTeX with `natbib`: `\cite`, `\citep`, `\citet`

**Key Commands**:

| Command/Environment | Description | Usage Context |
|:---|:---|:---|
| `\documentclass[aps,prd,superscriptaddress]{revtex4-2}` | PRD document class | PRD submission |
| `\documentclass[...,linenumbers,preprint]{revtex4-2}` | Review mode | Referee submission |
| `\author{...}\affiliation{...}` | Author + institution | Multi-author papers |
| `\begin{ruledtabular}...\end{ruledtabular}` | Professional ruled table | Eigenvalue data tables |
| `D{.}{.}{4}` (dcolumn) | Decimal-aligned column | Numeric precision tables |
| `\begin{figure*}...\end{figure*}` | Two-column spanning figure | Full spectrum diagrams |
| `\cite{key}`, `\citep{key}`, `\citet{key}` | Citation commands | In-text references |

**Dependencies**:
- *Upstream*: Docs 01, 02 (LaTeX fundamentals, amsmath)
- *Downstream*: Doc 05 (bibliography), Doc 14 (journal-specific styles)

---

### Document 04: JHEP Submission Style Guide

- **File**: `researchers/LaTeX/04_JHEP_Submission_Style_Guide.md`
- **Year**: --
- **Relevance**: HIGH
- **Tags**: `JHEP`, `Springer`, `submission`, `arXiv`, `PACS`, `jheppub`, `open-access`, `hep-th`, `math-ph`

**Summary**: Covers JHEP (Springer/IOP) document preparation using the `jheppub.sty` package. Includes metadata markup (PACS codes, keywords), author/affiliation formatting, figure and table requirements, BibTeX integration, and full arXiv+JHEP submission workflow. JHEP is a primary target for theoretical/mathematical physics papers with spectral action and NCG content.

**Key Results**:
1. Basic setup: `\documentclass{article}` + `\usepackage{jheppub}` (NOT a standalone document class)
2. PACS codes for this project: 11.15.Ex (gauge theory), 02.30.Sa (functional analysis), 04.50.Kd (modified gravity)
3. ArXiv categories: hep-th (primary), gr-qc (cross-list), math-ph (for pure math paper)
4. Standard journal abbreviations: `Phys.\ Rev.\ D`, `Commun.\ Math.\ Phys.`, `J.\ Geom.\ Phys.`
5. Rapid publication: typically 3-6 months turnaround

**Key Commands**:

| Command/Environment | Description | Usage Context |
|:---|:---|:---|
| `\usepackage{jheppub}` | JHEP formatting package | JHEP submission |
| `\thanks{e-mail: ...}` | Author email in footnote | Author metadata |
| `\pacs{11.15.Ex, ...}` | PACS classification codes | Paper categorization |
| `\keywords{NCG, spectral action, ...}` | Paper keywords | Abstract metadata |
| `figure*` | Two-column spanning figure | Large spectrum plots |

**Dependencies**:
- *Upstream*: Docs 01, 02 (LaTeX fundamentals, amsmath)
- *Downstream*: Doc 05 (bibliography), Doc 12 (arXiv workflow)

---

### Document 05: BibLaTeX Bibliography Management

- **File**: `researchers/LaTeX/05_BibLaTeX_Bibliography_Management.md`
- **Year**: --
- **Relevance**: HIGH
- **Tags**: `BibLaTeX`, `biber`, `bibliography`, `INSPIRE-HEP`, `citations`, `DOI`, `arXiv`, `.bib`, `numeric-style`, `author-year`

**Summary**: Modern replacement for BibTeX with superior formatting flexibility, native INSPIRE-HEP integration, and rich citation commands. Covers BibLaTeX setup with biber backend, citation styles (numeric, alphabetic, author-year), .bib file format, INSPIRE-HEP export workflow, cross-referencing, and multi-bibliography support. Recommended as the bibliography system for JHEP/JGP/CMP papers.

**Key Results**:
1. Setup: `\usepackage[style=numeric, backend=biber, sorting=none]{biblatex}` + `\addbibresource{file.bib}`
2. Compilation chain: pdflatex -> **biber** (NOT bibtex) -> pdflatex -> pdflatex
3. Rich citation commands: `\cite`, `\citep`, `\citet`, `\citeauthor`, `\citeyear`, `\fullcite`
4. INSPIRE-HEP workflow: search -> export BibTeX -> copy to .bib file
5. Multiple .bib resources via `\addbibresource` (one per topic: NCG, KK, cosmology)

**Key Commands**:

| Command/Environment | Description | Usage Context |
|:---|:---|:---|
| `\usepackage[style=numeric,backend=biber]{biblatex}` | Load BibLaTeX | Preamble |
| `\addbibresource{file.bib}` | Add bibliography file | Preamble (multiple allowed) |
| `\cite{key}` | Numeric citation [1] | In-text reference |
| `\fullcite{key}` | Full bibliographic entry | Footnotes, first mention |
| `\printbibliography` | Output reference list | End of document |
| `biber paper.bcf` | Process bibliography | Compilation chain |
| `eprint = {2305.12345}` | ArXiv identifier (.bib) | Preprint entries |
| `doi = {10.1103/...}` | DOI field (.bib) | Published articles |

**Dependencies**:
- *Upstream*: Docs 01-04 (all use bibliography)
- *Downstream*: Doc 12 (arXiv workflow), Doc 14 (journal-specific styles)

---

### Document 06: Differential Geometry Notation in LaTeX

- **File**: `researchers/LaTeX/06_Differential_Geometry_Notation_LaTeX.md`
- **Year**: --
- **Relevance**: CRITICAL
- **Tags**: `differential-geometry`, `tensors`, `Riemann`, `Ricci`, `covariant-derivative`, `Christoffel`, `Dirac`, `spinors`, `metric`, `KK`, `Jensen`, `TT-decomposition`

**Summary**: Comprehensive reference for tensor notation, covariant derivatives, Christoffel symbols, Riemann/Ricci/scalar curvature, metric conventions, Dirac operator/spinor notation, and metric perturbation theory in LaTeX. Directly applicable to KK geometry on M4 x SU(3), Jensen deformation, and TT decomposition used throughout the project.

**Key Results**:
1. Index convention: Greek (mu,nu) for 4D spacetime, Latin (i,j) for 3D spatial, (a,b) for Lie algebra/internal space
2. KK extended metric as 2x2 block matrix: g_AB with A,B in {0,...,3,5,...}
3. Jensen deformation: g_{mu nu}(tau) = e^{tau Q_{mu nu}} g^(0)_{mu nu}
4. TT decomposition: h^TT with traceless + transverse conditions
5. Custom macros: `\cov`, `\Riem`, `\Ricci`, `\DiracM`, `\metric`
6. Metric signature convention: explicit choice between (-,+,+,+) and (+,-,-,-) required at document start

**Key Commands**:

| Command/Environment | Description | Usage Context |
|:---|:---|:---|
| `R^{\rho}_{\sigma\mu\nu}` | Riemann tensor | Curvature computations |
| `\nabla_{\mu}` | Covariant derivative | KK geometry, Dirac operator |
| `\Gamma^{\lambda}_{\mu\nu}` | Christoffel symbols | Connection coefficients |
| `\Box \phi` | d'Alembertian | Wave operator |
| `\{\gamma^{\mu}, \gamma^{\nu}\} = 2g^{\mu\nu}` | Clifford algebra | Dirac operator definition |
| `h_{\mu\nu}^{\text{TT}}` | TT perturbation | Stability analysis |
| `\newcommand{\Riem}[4]{R^{#1}_{#2#3#4}}` | Riemann macro | Shorthand in derivations |
| `\star \omega` | Hodge star | Differential forms |

**Dependencies**:
- *Upstream*: Docs 01, 02 (LaTeX, amsmath)
- *Downstream*: Doc 07 (NCG notation extends this), Doc 10 (symbol conventions)

---

### Document 07: Spectral Theory and NCG Notation in LaTeX

- **File**: `researchers/LaTeX/07_Spectral_Theory_NCG_Notation_LaTeX.md`
- **Year**: --
- **Relevance**: CRITICAL
- **Tags**: `NCG`, `spectral-triple`, `Dirac-operator`, `heat-kernel`, `spectral-action`, `KO-dimension`, `Seeley-DeWitt`, `Peter-Weyl`, `block-diagonal`, `SU(3)-representations`, `cyclic-cohomology`

**Summary**: Specialized notation for noncommutative geometry: spectral triples (A, H, D), Dirac operator properties, heat kernel expansions, spectral action principle, KO-dimension classification, cyclic cohomology, Seeley-DeWitt coefficients, SU(3) representation labels (p,q), and eigenvalue/moment notation. THE core notation document for the phonon-exflation framework's mathematical content.

**Key Results**:
1. Spectral triple: (C^infty(SU(3)), L^2(SU(3) x S), D_K)
2. Heat kernel: Z(t) = tr(e^{-tD^2}) ~ t^{-dim/2}(a_0 + a_2 t + a_4 t^2 + ...)
3. Spectral action: S_spec = tr(f(D/Lambda)) ~ Lambda^4 a_0 + Lambda^2 a_2 + a_4 log Lambda
4. Peter-Weyl block decomposition: D_K = bigoplus_r D_{K,r} x 1_r
5. Sector labels: (p,q) for SU(3) irreps, with eigenvalues lambda_n^{(p,q)}(tau)
6. Spectral moments: M_k = sum lambda_n^k / dim(H)
7. Custom macros: `\stiple`, `\sact`, `\KOdim`, `\hk`, `\spec`

**Key Commands**:

| Command/Environment | Description | Usage Context |
|:---|:---|:---|
| `(A, \mathcal{H}, D)` | Spectral triple notation | NCG framework definition |
| `\text{tr}(e^{-tD^2})` | Heat kernel trace | Seeley-DeWitt expansion |
| `\mathcal{S}_{\text{spec}}(\tau)` | Spectral action | Central computation |
| `\text{KO-dim} = 6` | KO-dimension | Classification result |
| `D_K = \bigoplus_r D_{K,r} \otimes \mathbb{1}_r` | Block decomposition | Block-diagonality theorem |
| `\lambda_n^{(p,q)}(\tau)` | Sector eigenvalue | Spectrum parameterization |
| `a_0, a_2, a_4` | Seeley-DeWitt coefficients | Heat kernel expansion |
| `\zeta_D(s) = \text{tr}(\|D\|^{-s})` | Spectral zeta function | Dimension spectrum |
| `\newcommand{\sact}{\mathcal{S}_{\text{spec}}}` | Spectral action macro | Preamble shorthand |

**Dependencies**:
- *Upstream*: Docs 02, 06 (amsmath, differential geometry)
- *Downstream*: Doc 10 (symbol conventions), Doc 13 (macros)

---

### Document 08: TikZ/PGF Scientific Diagrams

- **File**: `researchers/LaTeX/08_TikZ_PGF_Scientific_Diagrams.md`
- **Year**: --
- **Relevance**: HIGH
- **Tags**: `TikZ`, `PGF`, `pgfplots`, `diagrams`, `Feynman`, `commutative-diagrams`, `eigenvalue-flow`, `phase-diagram`, `block-diagonal`, `visualization`, `externalize`

**Summary**: Professional scientific diagram framework for LaTeX. Covers coordinate systems, Bezier curves, pgfplots for data plotting, Feynman diagrams (tikz-feynman), commutative diagrams (tikz-cd), eigenvalue flow visualization, block-diagonal matrix diagrams, phase diagrams, and custom reusable styles. Enables version-controlled inline diagrams that auto-regenerate with the document.

**Key Results**:
1. pgfplots: `\addplot table {data.dat}` for plotting simulation output directly
2. tikz-feynman: Feynman diagram generation with fermion/boson/scalar line styles
3. tikz-cd: Commutative diagrams for exact sequences and categorical structures
4. Eigenvalue flow diagram template (tau vs lambda_n with phase transition markers)
5. Block-diagonal matrix visualization template (colored blocks + zero off-diagonal)
6. Externalization: `\tikzexternalize` for caching compiled diagrams
7. Compilation requires `-shell-escape` flag for some features

**Key Commands**:

| Command/Environment | Description | Usage Context |
|:---|:---|:---|
| `\usepackage{tikz}` | Load TikZ | Preamble |
| `\usepackage{pgfplots}` | Function/data plotting | Eigenvalue spectra |
| `\usepackage[compat=1.1.0]{tikz-feynman}` | Feynman diagrams | QFT interactions |
| `\usepackage{tikz-cd}` | Commutative diagrams | Category theory, exact sequences |
| `\begin{axis}[xlabel=...,ylabel=...]` | Plot axes | Data visualization |
| `\addplot[smooth,thick] table {file.dat}` | Plot from data file | Simulation output |
| `\tikzexternalize[prefix=tikz/]` | Cache diagrams | Compilation speed |
| `\tikzset{style-name/.style={...}}` | Custom reusable style | Consistent diagrams |

**Dependencies**:
- *Upstream*: Doc 01 (LaTeX fundamentals)
- *Downstream*: Doc 11 (figure best practices)

---

### Document 09: Scientific Writing Best Practices

- **File**: `researchers/LaTeX/09_Scientific_Writing_Best_Practices.md`
- **Year**: --
- **Relevance**: CRITICAL
- **Tags**: `writing`, `paper-structure`, `abstract`, `introduction`, `results`, `discussion`, `no-go`, `theorem`, `referee`, `JGP`, `CMP`, `PRD`, `JHEP`, `active-voice`, `methodology`

**Summary**: Structural principles for theoretical physics papers: abstract design, introduction strategy (opening gambit, lit review, motivation, roadmap), methodology with formal theorem/proof structure, results presentation for both negative (no-go) and positive (theorem) papers, discussion balance, and referee-friendly composition. Tailored to JGP/CMP (math-focused) vs PRD (physics-focused) structures.

**Key Results**:
1. Two distinct structures: Mathematical Physics (Setup -> Theorem -> Proof -> Corollaries) vs Observational (Data/Methods -> Analysis -> Results -> Discussion)
2. Abstract formula: problem (1-2 sent) + result (1-2 sent) + method (1 sent) + implications (1-2 sent)
3. For no-go results: state claim as formal theorem, support with calculation, corollary states physical consequence
4. Caption strategy: self-contained, complete, readable without figure
5. Active voice preferred: "We computed" not "The spectrum was computed"
6. Specific example abstract provided for the no-go paper

**Key Commands**:

| Command/Environment | Description | Usage Context |
|:---|:---|:---|
| `\begin{theorem}[V_spec Monotonicity]` | Formal theorem statement | Main no-go result |
| `\begin{corollary}[No Starobinsky Minimum]` | Physical consequence | After theorem |
| `\begin{proof}...\end{proof}` | Rigorous proof | JGP/CMP papers |
| `\section*{Acknowledgments}` | Unnumbered section | End matter |
| `\appendix` | Appendix start | Computational details |

**Dependencies**:
- *Upstream*: Docs 01-02 (LaTeX structure, theorem environments)
- *Downstream*: All papers (meta-document about HOW to write)

---

### Document 10: Physics Symbol Conventions

- **File**: `researchers/LaTeX/10_Physics_Symbol_Conventions.md`
- **Year**: --
- **Relevance**: HIGH
- **Tags**: `notation`, `symbols`, `indices`, `decorations`, `fonts`, `ISO-80000`, `conventions`, `style-file`, `disambiguation`, `calligraphic`, `fraktur`, `blackboard-bold`

**Summary**: Comprehensive notation standards following ISO 80000 and IUPAP conventions. Covers systematic index notation (Greek/Latin/fiber/spinor), decorations (hat, bar, tilde, dagger, dot), font families (calligraphic, fraktur, blackboard bold, bold), spacing conventions, cross-domain symbol conflicts, and a project-specific notation table template.

**Key Results**:
1. Index hierarchy: Greek (mu,nu = 4D spacetime) > Latin (i,j = 3D spatial) > Internal (a,b = gauge/Lie) > Spinor (alpha,beta)
2. Decoration rules: hat = quantum operator, bar = conjugate, tilde = perturbation, dagger = adjoint, dot = time derivative
3. Font rules: mathcal = spaces/algebras, mathfrak = Lie algebras, mathbb = number sets, mathbf = vectors
4. Symbol disambiguation: use font distinctions to resolve conflicts (R vs mathbb{R} vs hat{R})
5. Style file recommendation: `phonon-exflation-conventions.sty` with shared macros

**Key Commands**:

| Command/Environment | Description | Usage Context |
|:---|:---|:---|
| `\hat{H}` | Quantum operator | Hamiltonian |
| `\bar{\psi}` / `\overline{\psi}` | Dirac conjugate | Spinor fields |
| `\tilde{g}_{\mu\nu}` | Perturbed metric | Perturbation theory |
| `A^{\dagger}` | Hermitian adjoint | Operator algebra |
| `\dot{a}(t)` | Time derivative | Cosmology, dynamics |
| `\mathcal{H}` | Hilbert space | NCG framework |
| `\mathfrak{su}(3)` | Lie algebra | SU(3) structure |
| `\mathbb{R}` | Real numbers | Number sets |
| `\section*{Notation}` table | Notation reference | Start of paper |

**Dependencies**:
- *Upstream*: Doc 02 (amssymb provides font families)
- *Downstream*: Doc 13 (macros implement these conventions)

---

### Document 11: Figure & Table Best Practices

- **File**: `researchers/LaTeX/11_Figure_Table_Best_Practices_LaTeX.md`
- **Year**: --
- **Relevance**: HIGH
- **Tags**: `figures`, `matplotlib`, `PGF`, `booktabs`, `siunitx`, `color-blind`, `resolution`, `DPI`, `subfigures`, `caption`, `tables`, `journal-requirements`

**Summary**: Publication-quality figure preparation pipeline: matplotlib-to-PGF export (fonts match document), color-blind-safe palettes (Okabe-Ito), resolution standards (300 DPI print, 600 DPI line art), format hierarchy (PDF > EPS > PNG), subfigure layouts, professional table formatting with booktabs, number formatting with siunitx, and journal-specific figure requirements.

**Key Results**:
1. Matplotlib PGF pipeline: set `pgf.texsystem='pdflatex'`, add amsmath to preamble, export .pgf
2. Color-blind safe: Okabe-Ito palette or distinct line styles (solid/dashed/dotted)
3. Resolution: 300 DPI min for journal, 600 DPI for line art (CMP requires 600)
4. Format: PDF primary (vector, lossless), EPS for legacy, avoid PNG for technical figures
5. booktabs: `\toprule`, `\midrule`, `\bottomrule` (no vertical lines)
6. siunitx: `\SI{0.511}{\mega\electronvolt}`, automatic number formatting
7. Journal-specific widths: PRD (<=3.5in), JHEP (<=80mm), JGP (<=8cm), CMP (600 DPI line art)

**Key Commands**:

| Command/Environment | Description | Usage Context |
|:---|:---|:---|
| `\usepackage{booktabs}` | Professional tables | All papers |
| `\toprule` / `\midrule` / `\bottomrule` | Table rules | Clean formatting |
| `\usepackage{siunitx}` | Number/unit formatting | Precision display |
| `\SI{value}{unit}` | Formatted quantity | In-text numbers |
| `S[table-format=1.3]` (siunitx) | Aligned numeric column | Data tables |
| `\begin{subfigure}{0.45\textwidth}` | Multi-panel figure | Comparison plots |
| `fig.savefig('file.pgf')` (Python) | PGF export | matplotlib pipeline |
| `\input{file.pgf}` | Include PGF figure | LaTeX document |

**Dependencies**:
- *Upstream*: Docs 01, 08 (LaTeX figures, TikZ/pgfplots)
- *Downstream*: None (terminal)

---

### Document 12: ArXiv Submission Workflow

- **File**: `researchers/LaTeX/12_ArXiv_Submission_Workflow.md`
- **Year**: --
- **Relevance**: CRITICAL
- **Tags**: `arXiv`, `submission`, `preprint`, `.bbl`, `metadata`, `categories`, `versioning`, `hep-th`, `gr-qc`, `math-ph`, `priority`

**Summary**: Complete ArXiv submission procedure: account setup, file preparation (pre-compile .bbl since ArXiv cannot run biber/bibtex), directory structure, metadata entry, submission process, versioning (v1/v2/v3), cross-listing strategy, post-submission workflow, and common errors with fixes.

**Key Results**:
1. ArXiv categories: hep-th (primary), gr-qc (cross-list), math-ph (secondary), math.DG (secondary)
2. **CRITICAL**: ArXiv cannot run BibTeX/biber -- must pre-compile to .bbl and include via `\input{paper.bbl}`
3. File archive: tar.gz or zip containing .tex + .bbl + all figure .pdf files
4. Metadata limits: title <= 200 chars (no LaTeX symbols), abstract <= 1920 chars (plain text)
5. Ancillary files: simulation data, code, supplementary PDFs in `anc/` directory
6. Submission timeline: ArXiv post Day 0, journal submission Day 0-3

**Key Commands**:

| Command/Environment | Description | Usage Context |
|:---|:---|:---|
| `\input{paper.bbl}` | Include pre-compiled bibliography | ArXiv submission |
| `tar -czf paper.tar.gz *.tex *.bbl *.pdf` | Create submission archive | File preparation |
| `pdflatex paper.tex` (local test) | Verify compilation | Pre-submission check |
| `\usepackage[hidelinks]{hyperref}` | Fix hyperref issues | ArXiv compatibility |
| `mkdir anc/` | Ancillary files directory | Supplementary data |

**Dependencies**:
- *Upstream*: Docs 01-05, 11 (LaTeX, bibliography, figures)
- *Downstream*: None (terminal submission step)

---

### Document 13: LaTeX Macros for Physics Papers

- **File**: `researchers/LaTeX/13_LaTeX_Macros_Physics_Papers.md`
- **Year**: --
- **Relevance**: CRITICAL
- **Tags**: `macros`, `style-file`, `phonon_exflation.sty`, `physics-package`, `braket`, `semantic`, `operators`, `version-control`, `conditional`, `draft-mode`

**Summary**: Comprehensive guide to custom LaTeX macro design for large multi-author papers. Covers semantic vs presentational macros, `\DeclareMathOperator`, the `physics` package (braket, derivatives, commutators), and a complete `phonon_exflation.sty` team macro file template with version control and conditional compilation.

**Key Results**:
1. Semantic macros (name = meaning): `\diracK` not `\bold_DK`
2. `\DeclareMathOperator`: `\tr`, `\id`, `\diag`, `\rank`, `\spec`, `\sign`, `\Re`, `\Im`, `\Aut`, `\ad`, `\Ad`
3. `physics` package: `\ket`, `\bra`, `\braket`, `\norm`, `\expval`, `\mel`, `\pdv`, `\dv`, `\comm`
4. COMPLETE `phonon_exflation.sty` template with sections: spectral geometry, eigenvalues, quantum numbers, operators, spectral action, parameters, metrics
5. Conditional macros: `\newif\ifCompactNotation` for venue-specific notation; `\newif\ifDraft` with `showframe`
6. Best practices: 1-3 args max, document in comments, test in all venues

**Key Commands**:

| Command/Environment | Description | Usage Context |
|:---|:---|:---|
| `\ProvidesPackage{phonon_exflation}` | Package declaration | Style file header |
| `\newcommand{\stiple}{(\algebra{A}, \hilbert, D)}` | Spectral triple macro | All papers |
| `\newcommand{\diracK}{D_K}` | Dirac operator macro | All papers |
| `\newcommand{\eigval}[1]{\lambda_{#1}}` | Eigenvalue macro | Spectrum references |
| `\newcommand{\saction}{S_{\text{spec}}}` | Spectral action macro | Central computation |
| `\newcommand{\vspec}{V_{\text{spec}}}` | Spectral potential macro | No-go result |
| `\DeclareMathOperator{\tr}{tr}` | Trace operator | Spectral action |
| `\usepackage{physics}` | Physics notation package | Braket, derivatives |
| `\ket{\psi}`, `\braket{\psi}{\phi}` | Dirac notation | Quantum states |
| `\pdv{f}{x}` | Partial derivative | Derivations |
| `\comm{A}{B}` | Commutator [A,B] | Operator algebra |

**Dependencies**:
- *Upstream*: Docs 02, 06, 07, 10 (amsmath, notation, symbols)
- *Downstream*: All papers (shared infrastructure)

---

### Document 14: Journal of Geometry and Physics / CMP Style

- **File**: `researchers/LaTeX/14_Journal_Geometry_Physics_CMP_Style.md`
- **Year**: --
- **Relevance**: CRITICAL
- **Tags**: `JGP`, `CMP`, `Elsevier`, `Springer`, `mathematical-physics`, `theorem-numbering`, `submission`, `reviewer-response`, `open-access`, `venue-strategy`, `Editorial-Manager`

**Summary**: Detailed submission guidelines for JGP (Elsevier) and CMP (Springer), the two primary mathematical physics venues. Covers document class setup (plain article for both), theorem/proof environment standards, reference formatting, figure requirements, submission workflow (Editorial Manager), review timeline, revision response strategy, and strategic venue selection.

**Key Results**:
1. JGP: `\documentclass[11pt]{article}` + `\usepackage{natbib}` + geometry margins. 20-30 pages typical. 2 free color figures.
2. CMP: `\documentclass[11pt,a4paper]{article}` with standard amsmath/amsthm. 30-50+ pages. B/W preferred. Highest rigor.
3. Theorem numbering: within-section preferred (Theorem 1.1, 1.2)
4. CMP reference format differs from standard BibTeX output -- manual adjustment may be needed
5. Strategic venue selection: No-go paper -> JGP (geometry+cosmology, faster). Spectral Anatomy -> CMP (pure math physics, higher prestige).
6. Timeline: Editorial screening 0-5 days, review 2-8 weeks, decision week 8. Major revisions = 3 months.
7. Suggested reviewers: 1-2 names with emails required at submission.

**Key Commands**:

| Command/Environment | Description | Usage Context |
|:---|:---|:---|
| `\documentclass[11pt]{article}` | Standard class | Both JGP and CMP |
| `\usepackage{natbib}` | Bibliography (JGP) | JGP submission |
| `\begin{thebibliography}{99}` | Manual bibliography (CMP) | CMP submission |
| `\newtheorem{theorem}{Theorem}[section]` | Section-numbered theorem | Both venues |
| `\theoremstyle{plain/definition/remark}` | amsthm styles | Formal structure |
| `\thanks{e-mail: ...}` | Author email | CMP author markup |
| `\keywords{NCG; spectral action; ...}` | Paper keywords | Both venues |

**Dependencies**:
- *Upstream*: Docs 01-03, 05, 09 (LaTeX, amsmath, REVTeX, bibliography, writing)
- *Downstream*: None (terminal venue document)

---

## Cross-Document Command Concordance

Commands, environments, and packages referenced across multiple documents. Use this table to find ALL relevant documentation for a given tool.

| Command/Package | Documents | Notes |
|:---|:---|:---|
| `\begin{align}...\end{align}` | 02, 06, 07 | Primary equation environment for multi-line derivations |
| `\begin{theorem}...\end{theorem}` | 01, 02, 09, 14 | Doc 14 specifies section-numbering for JGP/CMP |
| `\begin{proof}...\end{proof}` | 02, 09, 14 | Required for JGP/CMP; Doc 09 covers proof strategy |
| `\DeclareMathOperator` | 02, 13 | Doc 02 introduces; Doc 13 provides full operator list |
| `\mathbb`, `\mathcal`, `\mathfrak` | 02, 07, 10 | Doc 10 specifies usage rules per symbol |
| `\cite`, `\citep`, `\citet` | 03, 04, 05 | natbib (03/04) vs BibLaTeX (05) -- see compatibility table below |
| `\usepackage{hyperref}` | 01, 12 | Doc 12: use `[hidelinks]` for ArXiv compatibility |
| `figure` / `figure*` | 01, 03, 04, 08, 11 | Doc 11 for quality; Docs 03/04 for venue-specific sizes |
| `booktabs` | 11, 03 | Doc 11 primary; replaces `ruledtabular` (Doc 03, REVTeX-only) |
| `siunitx` | 11, 03 | Doc 11 primary; Doc 03 uses `dcolumn` as REVTeX alternative |
| `tikz` / `pgfplots` | 08, 11 | Doc 08 for creation; Doc 11 for publication-quality export |
| `\newcommand` / macros | 01, 02, 06, 07, 10, 13 | Doc 13 is the definitive macro guide |
| `physics` package | 13 | `\ket`, `\bra`, `\braket`, `\pdv`, `\dv`, `\comm` |
| `.bbl` pre-compilation | 05, 12 | Doc 12: ArXiv requires it; Doc 05: biber produces it |
| `\appendix` | 01, 09 | Doc 01 for mechanics; Doc 09 for content strategy |
| `\keywords` | 03, 04, 14 | Venue-specific keyword formatting |

### BibTeX vs BibLaTeX Compatibility

| Venue | Bibliography System | Compilation | Documents |
|:---|:---|:---|:---|
| PRD (REVTeX) | BibTeX + natbib | pdflatex -> bibtex -> pdflatex x2 | 03, 05 |
| JHEP | BibLaTeX + biber OR BibTeX | pdflatex -> biber -> pdflatex x2 | 04, 05 |
| JGP | natbib (BibTeX) | pdflatex -> bibtex -> pdflatex x2 | 05, 14 |
| CMP | Manual `thebibliography` preferred | pdflatex only | 05, 14 |
| ArXiv | Pre-compiled .bbl (either source) | pdflatex only | 05, 12 |

**Recommendation**: Maintain a single master `.bib` file. Use BibLaTeX/biber for JHEP drafts, BibTeX/natbib for PRD/JGP, and export to `thebibliography` for CMP. ArXiv always receives pre-compiled .bbl.

---

## Notation Conventions

Notation standards derived from Documents 06, 07, and 10. All papers should follow these conventions and include a notation table at the start.

### Index Conventions
| Index type | Letters | Range | Document |
|:---|:---|:---|:---|
| 4D spacetime | mu, nu, rho, sigma | 0,1,2,3 | 06, 10 |
| 3D spatial | i, j, k | 1,2,3 | 06, 10 |
| Internal (Lie algebra) | a, b, c | 1,...,8 | 06, 10 |
| Spinor | alpha, beta | 1,...,dim(S) | 06, 10 |
| SU(3) irrep labels | (p,q) | non-negative integers | 07 |

### Decoration Conventions
| Decoration | Meaning | Example | Document |
|:---|:---|:---|:---|
| Hat | Quantum operator | `\hat{H}` | 10 |
| Bar / overline | Conjugate | `\bar{\psi}` | 10 |
| Tilde | Perturbation | `\tilde{g}` | 10 |
| Dagger | Hermitian adjoint | `A^{\dagger}` | 10 |
| Dot | Time derivative | `\dot{a}` | 10 |

### Font Conventions
| Font | Usage | Example | Document |
|:---|:---|:---|:---|
| `\mathbb` | Number sets | R, C, Z | 02, 10 |
| `\mathcal` | Spaces, algebras | A, H, S | 02, 07, 10 |
| `\mathfrak` | Lie algebras | su(3), so(4) | 02, 07, 10 |
| `\mathbf` | Classical vectors | **v**, **F** | 10 |
| Roman (`\text`) | Labels in math | tr, spec, diag | 02, 13 |

---

## Journal Selection Guide

| Journal | Class/Package | Bibliography | Figures | Page limit | Turnaround | Target paper | Documents |
|:---|:---|:---|:---|:---|:---|:---|:---|
| PRD | `revtex4-2` | natbib/BibTeX | <=3.5in (1-col) | ~15-25 pp | 3-6 months | No-go (physics) | 03, 05, 12 |
| JHEP | `article` + `jheppub` | BibLaTeX or BibTeX | <=80mm | No strict limit | 3-6 months | No-go (theory) | 04, 05, 12 |
| JGP | `article` (11pt) | natbib/BibTeX | <=8cm, 2 free color | 20-30 pp | 4-8 weeks | No-go (geom+cosmo) | 14, 05, 12 |
| CMP | `article` (11pt, a4) | Manual preferred | <=84mm, B/W, 600 DPI | 30-50+ pp | 4-8 weeks | Spectral Anatomy | 14, 05, 12 |
| ArXiv | Any (standalone) | Pre-compiled .bbl | Any (PDF preferred) | None | Immediate | Both papers | 12 |

### Recommended Venue Strategy (Session 25)

**No-go paper** (V_spec monotone, gap equation failure):
1. Write using Doc 09 (structure) + Doc 07 (NCG notation) + Doc 13 (macros)
2. Primary venue: JGP (Doc 14) -- geometry emphasis, faster review
3. Secondary venue: JHEP (Doc 04) -- theory audience, open access
4. Post to ArXiv (Doc 12): hep-th primary, gr-qc + math-ph cross-list

**Spectral Anatomy paper** (block-diagonality, KO-dimension, mathematical theorems):
1. Write using Doc 09 (structure) + Doc 14 (rigorous proofs) + Doc 06/07 (notation) + Doc 13 (macros)
2. Primary venue: CMP (Doc 14) -- highest prestige for mathematical physics
3. Secondary venue: JGP (Doc 14) -- faster turnaround
4. Post to ArXiv (Doc 12): math-ph primary, hep-th cross-list

---

## Shared Infrastructure Files

Three shared files should be created for Session 25 paper preparation (from cross-document analysis of Docs 06, 07, 10, 11, 13):

1. **`phonon_exflation.sty`** -- Shared notation macros consolidating Docs 06, 07, 10, 13. Template provided in Doc 13. Used by ALL papers for notation consistency.
2. **`phonon_exflation.bib`** -- Master bibliography file for ~50+ citations (Connes, Baptista, Paasch, etc.). Managed per Doc 05. Single source, venue-specific compilation.
3. **`figures/generate_all.py`** -- Automated figure pipeline from tier0-computation .npz data -> publication-quality PDF/PGF. Per Docs 08 and 11.

---

**Index generation date**: 2026-02-21
**Generated by**: Specialist (reader) + Coordinator (assembler)
**Source documents**: 14 LaTeX reference guides in `researchers/LaTeX/`
