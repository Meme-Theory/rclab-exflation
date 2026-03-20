# JHEP Submission Style Guide: Springer High-Energy Physics

**Author(s):** Journal of High Energy Physics (Springer/IOP)
**Year:** 2020+ (current JHEP formatting)
**Reference:** JHEP Instructions for Authors, jheppub.sty package

---

## Abstract

JHEP (Journal of High Energy Physics) publishes cutting-edge theoretical physics research through Springer's platform. This document covers JHEP document preparation, including the jheppub.sty package, metadata markup, bibliography formatting, figure requirements, and submission workflow. JHEP is an appropriate venue for the phonon-exflation project's spectral action paper, as it accepts general QFT, cosmology, and mathematical physics contributions.

---

## Historical Context

JHEP was founded in 1998 and is now operated jointly by Springer and the Institute of Physics. It emphasizes rapid publication (typically 3-6 months) and open-access (author fees apply). Unlike traditional APS journals (PRL, PRD), JHEP uses Springer's infrastructure, which means different formatting conventions, bibliography styles, and author guidelines. JHEP has become a premier venue for theoretical high-energy physics and mathematical physics papers.

For the phonon-exflation project: JHEP is ideal for papers with emphasis on QFT, NCG, and mathematical structure rather than cosmological observables.

---

## Basic Document Structure

```latex
\documentclass{article}
\usepackage{jheppub}

% Standard packages
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{graphicx}

% Title and authors
\title{Phonon Exflation Cosmology: Spectral Action Principle
        on Noncommutative SU(3)}

\author{Author One\thanks{e-mail: [email redacted]},
        Author Two\thanks{e-mail: [email redacted]}}

\affiliation{Department of Physics, University of First Author, \\
            City, Country}

\affiliation{CERN, Geneva, Switzerland}

\date{\today}

\begin{document}

\begin{abstract}
We investigate the spectral action principle applied to...
\end{abstract}

\keywords{Noncommutative geometry, Kaluza-Klein, Cosmology}

\maketitle

\section{Introduction}
...

\end{document}
```

---

## The jheppub Package

Included in modern TeX distributions. If not available locally, download from:
https://jhep.sissa.it/jhep/help/JHEP_TeXclass.zip

Key features:
- Predefines journal name, citation format, page layout
- Automatic title page formatting
- Two-column layout with professional spacing
- Springer-compatible metadata

---

## Author and Affiliation Markup

### Multiple Authors with Superscript Numbers

```latex
\author{A.~Author\thanks{e-mail: [email redacted]},
        B.~Colleague\thanks{e-mail: [email redacted]},
        C.~Collaborator\thanks{e-mail: [email redacted]}}

\affiliation{Department of Physics, University One, City, Country}
\affiliation{CERN, Geneva, Switzerland}
\affiliation{Institute of Advanced Studies, Another City, Country}
```

The `\thanks` macro adds email addresses in footnote format.

### ORCID Integration

```latex
\author{A.~Author\thanks{e-mail: [email redacted];
                          ORCID: 0000-0001-2345-6789}}
```

---

## Metadata and Keywords

```latex
\pacs{11.15.Ex, 12.38.Bx}  % PACS codes for high-energy physics
\keywords{Noncommutative geometry, Spectral action, Kaluza-Klein,
          Cosmology, NCG, Dirac spectrum}

\maketitle
```

PACS codes should follow official classification. Common codes for this project:
- 11.15.Ex: Gauge theories and their generalizations
- 12.38.Bx: Perturbative calculations (QCD)
- 02.30.Sa: Functional analysis (for spectral theory)
- 04.50.Kd: Modified theories of gravity (for cosmological applications)

---

## Sections and Theorem Environments

```latex
\section{Introduction}
\label{sec:intro}

\section{Theoretical Framework}
\subsection{Spectral Triples}
\label{sec:spectral-triples}

\subsection{Dirac Operator on SU(3)}

\section{Main Results}

\subsection{Block-Diagonality of $D_K$}

\section*{Acknowledgments}

\appendix
\section{Computational Details}
```

### Theorem Environments

JHEP integrates with amsthm:

```latex
\usepackage{amsthm}

\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}

\newtheorem*{remark}{Remark}

\begin{theorem}[Block-Diagonality on Peter-Weyl]
Let $(A, H, D)$ be the Jensen-deformed spectral triple on $\text{SU}(3)$.
Then $D_K = \bigoplus_{i} D_{K,i} \otimes \mathbb{1}_{r_i}$
where the sum is over irreducible representations.
\end{theorem}

\begin{proof}
The Casimir operator satisfies $[\mathcal{C}, D_K] = 0$
by left-invariance, implying...
\end{proof}
```

---

## Equations

JHEP uses amsmath seamlessly:

```latex
\begin{equation}
  \mathcal{S}_{\text{spec}} = \int_0^{\infty} t \,
    \text{tr}\left(e^{-tD_K^2}\right) \frac{dt}{t}
  \label{eq:spectral-action}
\end{equation}

\begin{align}
  D_K &= \gamma^{\mu}(\tau) \nabla_{\mu} + m(\tau) \\
  \{D_K, \gamma^5\} &= 0 \quad \text{(chirality)} \\
  [J^a, D_K] &= 0 \quad \text{(left-invariance)}
  \label{eq:dk-properties}
\end{align}
```

---

## Figures and Tables

### Figure Inclusion

```latex
\begin{figure}
\centering
\includegraphics[width=0.8\textwidth]{eigenvalue_spectrum.pdf}
\caption{Eigenvalue spectrum of $D_K(\tau)$ for $\tau \in [0, 0.5]$.
  Solid curves: fermionic modes. Dashed curves: bosonic modes.
  The gap decreases approximately as $(1-0.4\tau)$.}
\label{fig:spectrum}
\end{figure}
```

### Multi-Panel Figures

```latex
\usepackage{subcaption}

\begin{figure}
\centering
\begin{subfigure}{0.45\textwidth}
  \includegraphics[width=\textwidth]{round_metric_spectrum.pdf}
  \caption{Round metric}
  \label{fig:round}
\end{subfigure}
\hfill
\begin{subfigure}{0.45\textwidth}
  \includegraphics[width=\textwidth]{jensen_metric_spectrum.pdf}
  \caption{Jensen-deformed metric}
  \label{fig:jensen}
\end{subfigure}
\caption{Comparison of Dirac spectra.}
\label{fig:spectrum-comparison}
\end{figure}
```

### Tables

```latex
\begin{table}
\centering
\begin{tabular}{c|c|c|c}
  $\tau$ & $\lambda_1$ & $\lambda_2$ & Gap \\
  \hline
  0.10 & 1.207 & 0.325 & 0.882 \\
  0.15 & 1.531 & 0.405 & 1.126 \\
  0.20 & 1.644 & 0.480 & 1.164 \\
\end{tabular}
\caption{First two eigenvalues and gap at selected $\tau$ values.}
\label{tab:eigenvalues}
\end{table}
```

---

## Bibliography with BibTeX

### Preamble and Compilation

```latex
\usepackage{cite}  % or \usepackage{natbib}
```

At end of document:

```latex
\section*{References}
\bibliography{phonon_exflation}  % loads phonon_exflation.bib
```

Compilation sequence:
```bash
pdflatex paper.tex
bibtex paper.aux
pdflatex paper.tex
pdflatex paper.tex
```

### BibTeX Entry Format

```bibtex
@article{Connes2006,
  author = {Connes, Alain},
  title = {Noncommutative Geometry and Physics},
  journal = {Rev.\ Mod.\ Phys.},
  volume = {79},
  pages = {976--1041},
  year = {2006},
  doi = {10.1103/RevModPhys.79.976}
}

@article{Chamseddine2007,
  author = {Chamseddine, Ali H. and Connes, Alain},
  title = {Why the Standard Model},
  journal = {J.\ Geom.\ Phys.},
  volume = {58},
  pages = {38--47},
  year = {2008},
  doi = {10.1016/j.geomphys.2007.09.011},
  eprint = {0706.3688}
}

@book{Wald1984,
  author = {Wald, Robert M.},
  title = {General Relativity},
  publisher = {University of Chicago Press},
  address = {Chicago},
  year = {1984}
}
```

### Citation Commands

```latex
\cite{Connes2006}        % Numbered [1]
\cite{Connes2006,Wald1984}  % Multiple [1,2]
```

---

## ArXiv Submission Workflow

### 1. Prepare Files

Create a submission directory:
```
phonon-exflation-jhep/
  phonon_exflation.tex
  phonon_exflation.bbl    (compiled bibliography)
  fig_eigenvalue.pdf
  fig_spectrum.pdf
```

### 2. Compile Bibliography

```bash
pdflatex paper.tex
bibtex paper.aux
```

This produces `paper.bbl` (compiled bibliography file).

### 3. Create ArXiv-Ready Source

Copy all files into a single directory. Remove .aux, .log, .out files:

```bash
ls -la  # verify only .tex, .bbl, .pdf files present
```

### 4. Upload to ArXiv

- Go to https://arxiv.org/
- Select "Submit" -> "New Submission"
- Choose category: hep-th (High Energy Physics - Theory) or math-ph (Mathematical Physics)
- Cross-list: Also check gr-qc (General Relativity and Quantum Cosmology) if cosmological focus
- Upload .tar or .zip file containing tex + bbl + figures
- Preview PDF to verify formatting

### 5. Upload to JHEP

After arXiv posting:
- Visit https://jhep.sissa.it/
- Use journal submission system
- Include arXiv identifier in submission form
- JHEP will review within 1-2 weeks typically

---

## Important JHEP Conventions

### Abbreviations

Use standard abbreviations for common journals:

```latex
Phys.\ Rev.\ D         % Physical Review D
Phys.\ Rev.\ Lett.     % Physical Review Letters
Nucl.\ Phys.\ B        % Nuclear Physics B
Phys.\ Lett.\ B        % Physics Letters B
J.\ High Energy Phys.  % Journal of High Energy Physics
Commun.\ Math.\ Phys.  % Communications in Mathematical Physics
J.\ Geom.\ Phys.       % Journal of Geometry and Physics
```

### DOI Format

Always include DOI if available:

```latex
\href{https://doi.org/10.1103/PhysRevD.99.065001}
     {Phys.\ Rev.\ D \textbf{99}, 065001 (2019)}
```

---

## Common Pitfalls

1. **Bibliography not compiling**: Run `bibtex` on the .aux file, not the .tex file directly.
2. **Orphan references**: Check all \cite commands have matching entries in .bib file.
3. **Figure format**: PDF preferred; avoid JPEG for technical diagrams.
4. **Line breaks in titles**: Use `{}` to protect capitalization: `{NCG}` not `ncg`.
5. **Email addresses in \thanks**: Include them; JHEP extracts these for correspondence.

---

## Document Class Alternatives

If jheppub is unavailable:

```latex
\documentclass[11pt,a4paper]{article}
\usepackage{geometry}
\geometry{margin=2.5cm}

% Manually approximate JHEP formatting
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{graphicx}
```

This works but lacks JHEP's professional polish.

---

## Connection to Phonon-Exflation Framework

JHEP format enables:
- Submission to high-profile HEP theory venue
- Professional presentation of spectral action and NCG content
- Cross-listing on arXiv with hep-th + gr-qc categories
- Automatic DOI assignment upon publication
- International peer review with fast turnaround
- Open-access publication (with author fees)
- Integration with INSPIRE-HEP literature database

Relevance to Project: **HIGH** - JHEP is primary target for mathematical physics and QFT-focused paper.
