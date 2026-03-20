# LaTeX Document Preparation System: Fundamentals

**Author(s):** Leslie Lamport (original), Donald E. Knuth (TeX base)
**Year:** 1985 (original LaTeX), 2020+ (modern distributions)
**Reference:** The LaTeX Companion (2nd ed., Mittelbach et al.)

---

## Abstract

This document provides a comprehensive reference for LaTeX document structure, class selection, sectioning strategies, environments, floats (figures and tables), and cross-referencing systems. It forms the foundation for all subsequent typesetting work in the phonon-exflation project's publication phase. Emphasis is placed on creating reproducible, maintainable LaTeX documents suitable for mathematical physics journals (JGP, CMP, PRD, JHEP).

---

## Historical Context

LaTeX emerged in 1985 as a document preparation layer over Donald Knuth's TeX system. While TeX provides low-level typesetting primitives (boxes, glue, kerns), LaTeX introduces high-level logical markup: chapters, sections, theorems, equations, and cross-references. This separation of content from presentation is essential for academic publishing, where dozens of journals may have different formatting requirements but identical mathematical content.

For the phonon-exflation project, LaTeX enables version-controlled manuscript development, collaborative editing via git, automated bibliography management, and submission to multiple archives (arXiv, journals) from a single source.

---

## Document Classes

Every LaTeX document begins with a document class declaration:

```latex
\documentclass{article}
% or
\documentclass{book}
\documentclass{report}
\documentclass{beamer}
```

### Key Article-Based Classes

- **article**: Standard for journal papers, short monographs. No chapters, typically 1-40 pages.
- **report**: Longer documents with chapters (theses, technical reports). Starts chapters on new pages.
- **book**: Full books with chapters, front/back matter, two-sided pages.

### Physics-Specific Variants

For this project's target journals, use specialized classes:

```latex
% For Physical Review D (PRD)
\documentclass{revtex4-2}

% For JHEP and Springer journals
\documentclass[a4paper,11pt]{article}
\usepackage{jheppub}  % JHEP formatting (from package)

% For Journal of Geometry and Physics
\documentclass[twocolumn]{article}
% or single-column with geometry tuning
\documentclass[11pt,a4paper]{article}
\usepackage[margin=2.5cm]{geometry}
```

### Document Class Options

Common global options passed in square brackets:

```latex
\documentclass[11pt,a4paper,twoside]{article}
% 11pt: font size (10pt default, also 12pt)
% a4paper: page size (also letterpaper, b5paper)
% twoside: two-sided printing (oneside default)
% twocolumn: two-column layout
```

---

## Preamble Structure and Packages

The preamble (between `\documentclass` and `\begin{document}`) loads packages and defines document-level settings:

```latex
\documentclass[11pt,a4paper]{article}

% Standard packages
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{lmodern}  % Latin Modern font (sharp for math)

% Language and hyphenation
\usepackage[english]{babel}

% Mathematics (CRITICAL for NCG, KK, spectral theory)
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsthm}

% Physics-specific
\usepackage{physics}      % for braket notation, derivatives
\usepackage{siunitx}      % for units

% Geometry and hyperlinks
\usepackage[margin=2.5cm]{geometry}
\usepackage{hyperref}

% Title page info
\title{Phonon Exflation Cosmology: NCG Spectral Action}
\author{Author Names}
\date{\today}

\begin{document}
\maketitle
...
\end{document}
```

---

## Sectioning Commands

Hierarchical document structure (article class has no chapters):

```latex
\section{Introduction}          % Level 1
\subsection{Motivation}         % Level 2
\subsubsection{Problem Setup}   % Level 3
\paragraph{Key Observation}     % Level 4 (usually in-line)
```

Each sectioning command:
- Auto-increments the counter
- Appears in table of contents (by default)
- Can include labels for cross-referencing

```latex
\section{Spectral Action Principle}
\label{sec:spectral-action}

In Section~\ref{sec:spectral-action}, we derive...
```

### Numbered vs Unnumbered Sections

```latex
\section{Main Result}           % numbered: 1, 2, 3, ...
\section*{Acknowledgments}      % unnumbered, no counter
\appendix
\section{Proof Details}         % becomes A, B, C, ...
```

---

## Theorem and Definition Environments

The `amsthm` package provides structured environments for mathematical statements:

```latex
\usepackage{amsthm}

% Define styles
\theoremstyle{plain}
\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}

\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{example}[theorem]{Example}

\theoremstyle{remark}
\newtheorem*{remark}{Remark}  % no numbering
```

Usage in the document:

```latex
\begin{theorem}[Jensen Deformation]
Let $(A, H, D)$ be a spectral triple on $\text{SU}(3)$.
Then the Jensen-deformed metric...
\label{thm:jensen}
\end{theorem}

\begin{proof}
By block-diagonality of $D_K$, we have...
\end{proof}
```

---

## Floats: Figures and Tables

Floats are environments that LaTeX positions automatically (top/bottom of page, or separate page):

### Figures

```latex
\begin{figure}[ht]                      % h=here, t=top, b=bottom, p=page
  \centering
  \includegraphics[width=0.8\textwidth]{eigenvalue_flow.pdf}
  \caption{Eigenvalue spectrum of $D_K$ as function of $\tau$.}
  \label{fig:eigenvalue}
\end{figure}

See Figure~\ref{fig:eigenvalue} for the flow.
```

### Tables

```latex
\begin{table}[ht]
  \centering
  \begin{tabular}{c|c|c}
    $\tau$ & $\lambda_{\min}$ & $\text{gap ratio}$ \\
    \hline
    0.10 & 1.207 & 0.448 \\
    0.15 & 1.531 & 0.389 \\
    0.20 & 1.644 & 0.365 \\
  \end{tabular}
  \caption{Dirac spectrum at three $\tau$ values.}
  \label{tab:spectrum}
\end{table}
```

### Subfigures

For multi-panel figures, use `subcaption` package:

```latex
\usepackage{subcaption}

\begin{figure}
  \centering
  \begin{subfigure}{0.45\textwidth}
    \includegraphics[width=\textwidth]{panel_a.pdf}
    \caption{(a) Round metric}
    \label{fig:a}
  \end{subfigure}
  \hfill
  \begin{subfigure}{0.45\textwidth}
    \includegraphics[width=\textwidth]{panel_b.pdf}
    \caption{(b) Jensen-deformed}
    \label{fig:b}
  \end{subfigure}
  \caption{Comparison of metrics.}
  \label{fig:metric-comparison}
\end{figure}
```

---

## Cross-Referencing

LaTeX maintains automatic numbering and reference links:

```latex
\label{marker}      % Define a cross-reference anchor
\ref{marker}        % Insert number (e.g., "3.2")
\pageref{marker}    % Insert page number
\eqref{marker}      % For equations (adds parentheses)
```

### Examples in Scientific Context

```latex
\section{Main Theorem}
\label{sec:main}

\begin{equation}
  \mathcal{S}_{\text{spec}}(\tau) = \sum_{n=1}^{\infty}
    \frac{\lambda_n(\tau)}{\Lambda}
  \label{eq:spectral-action}
\end{equation}

From Equation~\eqref{eq:spectral-action}, we see that...
As proven in Section~\ref{sec:main}, the spectrum satisfies...
See Table~\ref{tab:spectrum} on page~\pageref{tab:spectrum}.
```

### Hyperref Package

Enable clickable cross-references in PDF:

```latex
\usepackage{hyperref}

\hypersetup{
  colorlinks=true,
  linkcolor=blue,        % internal links
  citecolor=blue,        % citations
  urlcolor=red,          % URLs
  pdftitle={Phonon Exflation},
  pdfauthor={Your Name},
  pdfsubject={Cosmology}
}
```

---

## Common Pitfalls

1. **Overfull hbox warnings**: Line is too long. Use `\\` to break equations, or reduce text width.
2. **Undefined references**: Run pdflatex twice to resolve forward references and citations.
3. **Float placement**: If figures "float" unexpectedly, reduce their width or use `\FloatBarrier` (from placeins package) before the next section.
4. **Bibliography not appearing**: Remember `\bibliography{file}` and run `bibtex` before final pdflatex.

---

## Workflow Checklist

For the phonon-exflation project's paper submission:

- [ ] Choose correct document class (revtex4-2 for PRD, jheppub for JHEP, article for arxiv)
- [ ] Define all theorem styles early in preamble
- [ ] Use consistent label naming: `sec:`, `fig:`, `tab:`, `eq:`, `thm:`
- [ ] Generate table of contents: `\tableofcontents` after title
- [ ] Compile twice (pdflatex -> bibtex -> pdflatex -> pdflatex)
- [ ] Check all `\ref` and `\cite` commands resolve (no "??" in output)
- [ ] Verify page count and figure quality before submission

---

## Connection to Phonon-Exflation Framework

This foundational document enables:
- Reproducible, version-controlled manuscripts for JGP, CMP, PRD, JHEP submissions
- Precise cross-referencing for the spectral action and Dirac spectrum derivations
- Professional figure placement for eigenvalue flows and phase diagrams
- Theorem environment for the proved results (block-diagonality, KO-dimension=6, SM charges)
- Multi-section organization for the no-go paper (V_spec monotone, gap equation failure) and the positive math paper (Spectral Anatomy of D_K on SU(3))

Relevance to Project: **CRITICAL** - All subsequent reference documents build on these LaTeX fundamentals.
