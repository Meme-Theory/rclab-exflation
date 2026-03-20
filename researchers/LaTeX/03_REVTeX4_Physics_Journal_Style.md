# REVTeX 4.2: Typesetting for Physical Review Journals

**Author(s):** American Physical Society
**Year:** 2010 (REVTeX 4.1), 2019 (REVTeX 4.2)
**Reference:** REVTeX 4.2 Author's Guide, APS journals (PRD, PRL, etc.)

---

## Abstract

REVTeX is the official document class for American Physical Society (APS) journals, including Physical Review D (PRD), Physical Review Letters (PRL), and Physical Review B/E/X. This reference covers class options, document structure, author/affiliation markup, BibTeX integration, figure inclusion, and submission workflows. REVTeX is essential for the phonon-exflation project if paper submission targets PRD (cosmology/general relativity venue).

---

## Historical Context

The APS created REVTeX (Relativists' Editor and Typesetter) to standardize manuscript formatting across its journal family. REVTeX 4 (2009) introduced substantial improvements over v3.x, including better AMS-LaTeX support and modern PDF generation. REVTeX 4.2 (2019) refined the system further and remains the standard for PRD submissions.

Key advantage: REVTeX handles journal-specific formatting (two-column layout, reference format, figure placement) automatically from a single source document. Authors write in REVTeX, and the system produces camera-ready output suitable for both arXiv preprint servers and APS journals.

---

## Document Class and Options

```latex
\documentclass{revtex4-2}

% Common options:
\documentclass[a4paper,nofootinbib]{revtex4-2}
\documentclass[aps,prd,superscriptaddress]{revtex4-2}
% aps: APS journal (default)
% prd: Physical Review D (sets up for 2-column PRD layout)
% prl: Physical Review Letters (two-column, strict 3.75-page limit)
% superscriptaddress: superscript affiliation numbers
% nofootinbib: keeps footnotes separate from bibliography (default merges them)
```

---

## Document Structure

### Preamble and Title Page

```latex
\documentclass[aps,prd,superscriptaddress]{revtex4-2}

\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{graphicx}       % for figures
\usepackage{dcolumn}        % for decimal-aligned tables
\usepackage{bm}             % bold math

\begin{document}

\title{Phonon Exflation Cosmology: Spectral Action on SU(3)}

% Multi-author with superscript affiliations
\author{Author One}%
 \affiliation{Department of Physics, University One, City, Country}

\author{Author Two}%
 \affiliation{Institute of Geometry, University Two, City, Country}%
 \affiliation{Visiting Scholar, CERN, Geneva, Switzerland}

\author{Author Three}%
 \affiliation{Department of Physics, University One, City, Country}

\date{\today}

\begin{abstract}
We investigate the spectral action principle applied to...
\end{abstract}

\keywords{Noncommutative geometry, Kaluza-Klein, Cosmology}

\maketitle
```

### Superscript vs Inline Affiliations

**Superscript (preferred for multi-author, multi-affiliation papers):**

```latex
\author{A.~One}%
 \affiliation{Dept.~Physics, Univ.~One}

\author{A.~Two}%
 \affiliation{Dept.~Physics, Univ.~One}
 \affiliation{CERN}
```

**Inline (simpler for single-author):**

```latex
\author{A.~One\affiliation{Dept.~Physics, Univ.~One}}
```

---

## Sections and Cross-References

```latex
\section{Introduction}
\label{sec:intro}

In Section~\ref{sec:intro}...

\section{Spectral Geometry}
\label{sec:geometry}

\subsection{Dirac Operator}
\label{sec:dirac}

\section*{Acknowledgments}  % unnumbered

\appendix
\section{Details of Computation}
\label{app:computation}
```

---

## Equations and Theorems

REVTeX works seamlessly with amsmath:

```latex
\begin{equation}
  \mathcal{S}_{\text{spec}}(\tau) = \int_0^{\infty} t \,
    \text{tr}(e^{-tD_K^2}) \, \frac{dt}{t}
  \label{eq:spectral-action}
\end{equation}

\begin{align}
  D_K &= \gamma^{\mu} \nabla_{\mu} + m(\tau) \\
  \langle D_K^n \rangle &= \text{tr}(D_K^n) / \text{tr}(\mathbb{1})
  \label{eq:moment}
\end{align}
```

### Theorem Environments

```latex
\usepackage{amsthm}

\newtheorem{theorem}{Theorem}[section]
\newtheorem*{theorem*}{Theorem}

\begin{theorem}[Block-Diagonality]
The Dirac operator $D_K$ is exactly block-diagonal
in the Peter-Weyl basis of $\text{SU}(3)$.
\end{theorem}

\begin{proof}
By left-invariance, $[J^a, D_K] = 0$, so...
\end{proof}
```

---

## Tables with REVTeX

Use `dcolumn` for decimal-aligned numeric columns:

```latex
\usepackage{dcolumn}

\begin{table}
\caption{Eigenvalue spectrum at selected $\tau$ values}
\label{tab:spectrum}
\begin{ruledtabular}
\begin{tabular}{cD{.}{.}{4}D{.}{.}{3}}
  $\tau$ & \multicolumn{1}{c}{$\lambda_1(\tau)$} &
         \multicolumn{1}{c}{Gap} \\
  \hline
  0.10 & 1.207 & 0.225 \\
  0.15 & 1.531 & 0.149 \\
  0.20 & 1.644 & 0.133 \\
\end{tabular}
\end{ruledtabular}
\end{table}
```

`D{.}{.}{4}` means: align on decimal point, 4 digits after point.
`ruledtabular` provides horizontal lines.

---

## Figures

### Basic Inclusion

```latex
\begin{figure}
\includegraphics[width=\columnwidth]{eigenvalue_flow.pdf}
\caption{Eigenvalue flow as function of $\tau \in [0, 0.5]$.
  The vertical line marks the phase transition.}
\label{fig:eigenvalue}
\end{figure}
```

### Two-Column Spanning Figure

In two-column mode, use `figure*` to span both columns:

```latex
\begin{figure*}
\includegraphics[width=0.9\textwidth]{large_diagram.pdf}
\caption{Full spectrum and geometry interpretation.}
\label{fig:full-spectrum}
\end{figure*}
```

### Sub-figures

```latex
\usepackage{subcaption}

\begin{figure}
\begin{subfigure}{0.45\columnwidth}
  \includegraphics[width=\textwidth]{round_metric.pdf}
  \caption{(a) Round metric}
  \label{fig:round}
\end{subfigure}
\hfill
\begin{subfigure}{0.45\columnwidth}
  \includegraphics[width=\textwidth]{jensen_metric.pdf}
  \caption{(b) Jensen-deformed}
  \label{fig:jensen}
\end{subfigure}
\caption{Comparison of metrics on $\text{SU}(3)$.}
\label{fig:metrics}
\end{figure}
```

---

## Bibliography Management

REVTeX uses BibTeX. Load bibliography file in document body:

```latex
\begin{thebibliography}{99}

% Manual entry (old style):
\bibitem{Author2020}
  Author, A., et al., \textit{Journal Name} \textbf{42}, 123 (2020).

\end{thebibliography}

% OR use BibTeX (preferred):
```

### With BibTeX

In preamble:
```latex
\usepackage{natbib}
```

In document body (after main text):
```latex
\bibliography{phonon_exflation}
```

### Bibliography File Format

File: `phonon_exflation.bib`

```bibtex
@article{Connes2006,
  author = {Connes, Alain},
  title = {Noncommutative Geometry and Physics},
  journal = {Reviews of Modern Physics},
  volume = {79},
  number = {4},
  pages = {976--1041},
  year = {2006}
}

@book{Wald1984,
  author = {Wald, Robert M.},
  title = {General Relativity},
  publisher = {University of Chicago Press},
  year = {1984}
}
```

### Citation Styles

```latex
\cite{Connes2006}              % Numbered: [1]
\citep{Connes2006}             % With parens: (Connes 2006)
\citet{Connes2006}             % Text: Connes 2006
```

---

## Submission Checklist

Before uploading to arXiv or submitting to PRD:

1. **Compile Sequence**: `pdflatex -> bibtex -> pdflatex -> pdflatex`
2. **Check PDF**: Open and verify all equations, references, figures display correctly
3. **Line Numbers**: Consider adding for referee review (REVTeX provides `\linenumbers` macro)
4. **Overfull Boxes**: Run `pdflatex` and scan for warnings in .log file
5. **Bibliography**: All citations must appear in \cite commands; verify no "???" in output
6. **Figure Format**: Use PDF or EPS (not JPEG or PNG for technical figures)
7. **Hyperref**: Test all cross-references and citations are clickable

---

## Important REVTeX Options for Revision

When submitting to journals, use revision-friendly options:

```latex
\documentclass[aps,prd,superscriptaddress,linenumbers,preprint]{revtex4-2}
% linenumbers: adds line numbers for easy referee comments
% preprint: single-column format (easier to review than 2-column)
```

For camera-ready final version:
```latex
\documentclass[aps,prd,superscriptaddress,final]{revtex4-2}
% final: removes line numbers, applies journal formatting
```

---

## Common Pitfalls

1. **Missing \maketitle**: Must appear after \title, \author to generate title.
2. **Figure format**: PRL requires EPS; check specific journal requirements.
3. **Bibliography style**: APS uses specific format; bibtex handles it automatically if you use the APS .bst file.
4. **Page limit**: PRL has 3.75-page limit; PRD has no explicit limit but reviewers notice excessive length.
5. **Affiliation encoding**: Avoid special characters; use standard Unicode in author names.

---

## Workflow for Phonon-Exflation Papers

**For no-go result paper** (Journal of Geometry and Physics or CMP):
- Could use REVTeX, but CMP/JGP have different requirements (see Document 14)
- Focus: mathematical rigor, clear theorem statements

**For cosmology-focused paper** (PRD):
- REVTeX is standard
- Include observational context, comparison with DESI data
- Emphasize block-diagonality and gap equation results

**For arXiv preprint**:
- Use REVTeX with `preprint` option for initial posting
- Clear source code for versioning

---

## Connection to Phonon-Exflation Framework

REVTeX enables:
- Submission of no-go results to PRD (cosmology community venue)
- Professional formatting of multi-author phonon-exflation team papers
- Automatic BibTeX integration for citations to Baptista, Connes, Paasch references
- Decimal-aligned tables for eigenvalue and gap equation data
- Cross-referencing of Dirac spectrum, spectral action, and KK geometry sections
- Reproducible, version-controlled source for cosmology journals

Relevance to Project: **HIGH** - Required for PRD submissions and professional cosmology venue publication.
