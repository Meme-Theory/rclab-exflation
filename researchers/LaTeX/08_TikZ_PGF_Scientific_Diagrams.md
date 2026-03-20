# TikZ/PGF: Professional Scientific Diagrams in LaTeX

**Author(s):** Till Tantau (TikZ/PGF), Physics Community (tikz-feynman, tikz-cd)
**Year:** 2005+ (TikZ initial), 2020+ (modern packages)
**Reference:** TikZ Manual (CTAN), tikz-feynman documentation, tikz-cd package

---

## Abstract

TikZ/PGF is a powerful LaTeX graphics framework for creating publication-quality scientific diagrams directly in LaTeX source code. This document covers coordinate systems, curve plotting, Feynman diagrams (tikz-feynman), commutative diagrams (tikz-cd), spectral plots, and eigenvalue flow diagrams. TikZ integration enables the phonon-exflation project to embed phase diagrams, eigenvalue spectra, and geometric visualizations directly in papers without external figure files.

---

## Historical Context

Till Tantau created TikZ (2005) as a comprehensive graphics system built on PGF (Portable Graphics Format). TikZ became the standard for academic scientific diagrams because diagrams are generated from code rather than WYSIWYG tools, enabling version control, reproducibility, and consistent styling with the document. Specialized packages like tikz-feynman (2014) and tikz-cd (2012) extend TikZ for specific domains.

For phonon-exflation: Eigenvalue flows, block-diagonal matrices, and phase transition diagrams are ideal for TikZ; they can be embedded inline in manuscripts and automatically regenerated if data changes.

---

## Basic Setup and Coordinates

### Loading TikZ

```latex
\usepackage{tikz}
\usetikzlibrary{arrows.meta,shapes,positioning}
```

### Simple Path Drawing

```latex
\begin{tikzpicture}
  \draw (0,0) -- (1,0) -- (1,1) -- (0,1) -- cycle;
  % Draws a square: (0,0) to (1,0) to (1,1) to (0,1) and back to origin
\end{tikzpicture}
```

### Coordinate Systems

```latex
\begin{tikzpicture}[scale=2]  % magnify 2x
  \draw[thick] (0,0) -- (1,0);  % horizontal line
  \draw[thick] (0,0) -- (0,1);  % vertical line

  % Labels
  \node at (0.5, -0.2) {x-axis};
  \node at (-0.2, 0.5) {y-axis};
\end{tikzpicture}
```

---

## Curves and Function Plots

### Bezier Curves

```latex
\begin{tikzpicture}
  % Quadratic Bezier curve (.. controls point .. end)
  \draw (0,0) .. controls (1,1) .. (2,0);

  % Cubic Bezier
  \draw (0,0) .. controls (0,1) and (2,1) .. (2,0);
\end{tikzpicture}
```

### Function Graphing

```latex
\usepackage{pgfplots}

\begin{tikzpicture}
  \begin{axis}[
    xlabel=$\tau$,
    ylabel=$\lambda_n(\tau)$,
    width=10cm, height=6cm,
    grid=major
  ]
    % Plot eigenvalue flow
    \addplot[smooth,thick] table {eigenvalues.dat};

    % Add vertical line at phase transition
    \addplot[dashed,red] coordinates {(0.2, 0) (0.2, 3)};

    \legend{$\lambda_1$, Transition};
  \end{axis}
\end{tikzpicture}
```

Example data file (`eigenvalues.dat`):
```
tau    lambda_1
0.0    1.207
0.1    1.310
0.2    1.531
0.3    1.644
```

---

## Nodes, Arrows, and Annotations

### Node Positioning

```latex
\begin{tikzpicture}
  % Define nodes
  \node (A) at (0,0) {Start};
  \node (B) at (2,0) {End};

  % Draw arrow between nodes
  \draw[->,thick] (A) -- (B);

  % Alternative arrow styles
  \draw[->,double] (A) -- (B);
  \draw[<->,thick] (A) -- (B);
  \draw[dashed,->] (A) -- (B);
\end{tikzpicture}
```

### Labeled Nodes

```latex
\begin{tikzpicture}
  \node[circle,draw,thick] (D) at (1,1) {$D_K$};
  \node[rectangle,draw,thick] (E) at (3,1) {Eigenvalues};
  \draw[->,thick] (D) -- node[above] {Spectral} (E);
\end{tikzpicture}
```

### Node Shapes

```latex
\node[circle,draw] (A) {A};      % circle
\node[rectangle,draw] (B) {B};   % rectangle
\node[diamond,draw] (C) {C};     % diamond
\node[ellipse,draw] (D) {D};     % ellipse
```

---

## Feynman Diagrams (tikz-feynman)

### Loading and Basic Setup

```latex
\usepackage[compat=1.1.0]{tikz-feynman}

\begin{tikzpicture}
  \begin{feynman}
    \vertex (a) at (0, 0) {$e^-$};
    \vertex (b) at (2, 0);
    \vertex (c) at (4, 0) {$e^-$};
    \diagram* {
      a -- [fermion] b -- [fermion] c,
      b -- [photon] (2, 1.5) {$\gamma$},
    };
  \end{feynman}
\end{tikzpicture}
```

### Particle Types

```latex
\diagram* {
  a -- [fermion] b,      % solid line (fermion)
  b -- [boson] c,        % wavy line (boson/photon)
  b -- [scalar] d,       % dashed line (scalar)
  b -- [ghost] e,        % dotted line (ghost)
};
```

### Two-point and Vertex Functions

```latex
\begin{tikzpicture}
  \begin{feynman}
    \vertex (a) {$a$};
    \vertex[right=2cm of a] (b) {$b$};
    \vertex[below=0.5cm of a] (a') {$a'$};
    \vertex[below=0.5cm of b] (b') {$b'$};

    \diagram* {
      (a) -- [fermion] (b),
      (a') -- [fermion] (b'),
    };
  \end{feynman}
\end{tikzpicture}
```

---

## Commutative Diagrams (tikz-cd)

### Loading tikz-cd

```latex
\usepackage{tikz-cd}

\begin{tikzcd}
  A \arrow{r}{\phi} \arrow{d}{\psi}
  & B \arrow{d}{\chi} \\
  C \arrow{r}{\rho}
  & D
\end{tikzcd}
```

This produces:
```
phi:     A -----> B
psi|     |chi
    v    v
    C -----> D
      rho
```

### Complex Diagram Example

```latex
\begin{tikzcd}[row sep=1.5cm, column sep=1.5cm]
  & \text{Hilbert Space } \mathcal{H} \\
  A \arrow{ur}{\text{acts on}} & & D \arrow{ll}[swap]{self-adjoint} \\
  & \text{Spectral Triple } (A, \mathcal{H}, D) \arrow{ul} \arrow{ur}
\end{tikzcd}
```

### Exact Sequences

```latex
\begin{tikzcd}
  0 \arrow{r} & A \arrow{r}{f} & B \arrow{r}{g} & C \arrow{r} & 0
\end{tikzcd}
```

---

## Eigenvalue Flow Diagram

### Example: D_K Spectrum Evolution

```latex
\begin{tikzpicture}[scale=1.2]
  % Horizontal axis (tau)
  \draw[->] (0,0) -- (5,0) node[right] {$\tau$};
  \draw[->] (0,0) -- (0,4) node[above] {$\lambda_n(\tau)$};

  % Grid
  \draw[gray,thin] (0,0) grid (5,4);

  % Draw eigenvalue curves (simplified)
  \draw[thick,blue] plot[smooth] coordinates {
    (0, 1.2) (1, 1.3) (2, 1.5) (3, 1.6) (4, 1.7)
  };
  \node[blue] at (4.2, 1.7) {$\lambda_1$};

  \draw[thick,red] plot[smooth] coordinates {
    (0, 0.3) (1, 0.35) (2, 0.4) (3, 0.45) (4, 0.5)
  };
  \node[red] at (4.2, 0.5) {$\lambda_2$};

  % Phase transition line
  \draw[dashed,green,thick] (2, 0) -- (2, 4);
  \node[green] at (2, -0.3) {Transition};

  % Labels
  \draw[thick] (0, 0.1) -- (0, -0.1) node[below] {0};
  \draw[thick] (4, 0.1) -- (4, -0.1) node[below] {0.5};
\end{tikzpicture}
```

---

## Matrix and Block Diagrams

### Block-Diagonal Visualization

```latex
\begin{tikzpicture}
  % Outer matrix box
  \draw[thick] (0,0) rectangle (4,4);

  % Blocks
  \draw[thick,blue] (0,2) rectangle (2,4);
  \node at (1,3) [align=center] {$D_{K,1}$};

  \draw[thick,red] (2,0) rectangle (4,2);
  \node at (3,1) [align=center] {$D_{K,2}$};

  % Zero blocks
  \draw[dashed] (0,0) rectangle (2,2);
  \draw[dashed] (2,2) rectangle (4,4);

  \node at (4.5, 2) {$D_K = \begin{pmatrix}
    D_{K,1} & 0 \\ 0 & D_{K,2} \end{pmatrix}$};
\end{tikzpicture}
```

---

## Phase Diagrams

### Temperature vs Parameter Space

```latex
\usepackage{pgfplots}

\begin{tikzpicture}
  \begin{axis}[
    xlabel=$\tau$ (deformation),
    ylabel=$T$ (temperature),
    width=10cm, height=7cm,
    xmin=0, xmax=1, ymin=0, ymax=1
  ]
    % Phase region 1 (white)
    \addplot[fill=white,draw=black,thick]
      coordinates {(0,0) (0.3,0) (0.3,0.5) (0,0.5)};
    \node at (0.15, 0.25) {Phase I};

    % Phase region 2 (gray)
    \addplot[fill=gray!50,draw=black,thick]
      coordinates {(0.3,0) (1,0) (1,0.5) (0.3,0.5)};
    \node at (0.65, 0.25) {Phase II};

    % Phase boundary
    \addplot[thick,red] coordinates {(0.3,0) (0.3,0.5)};
    \node[red] at (0.35, 0.6) {Transition};
  \end{axis}
\end{tikzpicture}
```

---

## Advanced: Custom TikZ Styles

### Define Reusable Styles

```latex
\tikzset{
  eigenvalue/.style={thick, blue},
  phase-boundary/.style={dashed, red, line width=2pt},
  operator-box/.style={rectangle, draw=black, thick,
                       inner sep=0.5cm, font=\Large},
  arrow-label/.style={above, midway, font=\small}
}

% Usage
\begin{tikzpicture}
  \node[operator-box] (D) at (0,0) {$D_K$};
  \node[operator-box] (E) at (3,0) {Spectrum};
  \draw[->,eigenvalue] (D) -- (E);
  \draw[phase-boundary] (1.5, -1) -- (1.5, 1);
\end{tikzpicture}
```

---

## Embedding TikZ in Documents

### Inline Diagram

```latex
\section{Dirac Spectrum}

In Figure~\ref{fig:spectrum}, we plot the eigenvalue
flow of $D_K(\tau)$:

\begin{figure}[ht]
\centering
\begin{tikzpicture}[scale=1.5]
  % Diagram code here
\end{tikzpicture}
\caption{Eigenvalue spectrum as function of $\tau$.}
\label{fig:spectrum}
\end{figure}
```

### Exporting to PDF

Compile with:
```bash
pdflatex -shell-escape paper.tex
```

The `-shell-escape` flag allows LaTeX to call external programs (e.g., Ghostscript for special effects).

---

## Performance and Compilation

### Large Diagrams

For complex documents with many TikZ diagrams, compilation may slow. Use `externalize`:

```latex
\usetikzlibrary{external}
\tikzexternalize[prefix=tikz/]

\begin{document}
  % Diagrams are compiled once and cached
\end{document}
```

This stores compiled diagrams in subdirectory `tikz/`, avoiding recompilation.

---

## Common Pitfalls

1. **Coordinate misalignment**: Verify units and scaling match axes.
2. **Label overlap**: Use `node[above right=2mm]` to add padding.
3. **PDF size**: Many TikZ diagrams can bloat PDF. Externalize large batches.
4. **Compilation time**: Complex diagrams slow LaTeX. Test with `--draft` mode first.

---

## Practical Examples for Phonon-Exflation

### Gap Equation Visualization

```latex
\begin{tikzpicture}
  % Axes
  \draw[->] (0,0) -- (6,0) node[right] {$\tau$};
  \draw[->] (0,0) -- (0,3) node[above] {$\Delta(\tau)$};
  \draw[thick] (0,0) grid (6,3);

  % Gap function (schematic)
  \draw[thick,blue] plot[smooth] coordinates {
    (0,0) (1,0.5) (2,1.0) (3,1.2) (4,1.0) (5,0.5) (6,0)
  };

  % Stability region (shaded)
  \fill[red!20] (1,0) -- (1,1.5) -- (5,1.5) -- (5,0) -- cycle;
  \node at (3, 1.75) {Unstable};
\end{tikzpicture}
```

---

## Connection to Phonon-Exflation Framework

TikZ enables:
- Embedded eigenvalue flow diagrams (no external figure files)
- Block-diagonal matrix visualization for D_K structure
- Phase transition diagrams for cosmological scenarios
- Feynman diagrams for QFT interactions (future extensions)
- Spectral data plots directly from simulation outputs
- Publication-quality figures that version-control with source
- Reproducible diagrams across all paper venues (JHEP, PRD, CMP, JGP)

Relevance to Project: **HIGH** - Enables professional in-document visualization of spectral data and geometric structures.
