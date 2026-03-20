# AMS-LaTeX: Mathematical Typesetting for Theoretical Physics

**Author(s):** American Mathematical Society (amsmath, amssymb, amsthm)
**Year:** 1997 (AMS-LaTeX), 2020+ (modern updates)
**Reference:** User's Guide for the amsmath Package (AMS documentation)

---

## Abstract

The American Mathematical Society (AMS) LaTeX packages provide industrial-strength environments for mathematical typesetting. This document covers amsmath (equation environments), amssymb (mathematical symbols), and amsthm (theorem structures). These are essential for the phonon-exflation project's heavy mathematical content: tensor calculus, Dirac operators, spectral action, NCG notation, and multi-page derivations.

---

## Historical Context

Before AMS-LaTeX, plain TeX and standard LaTeX lacked robust equation environments. Donald Knuth's TeX provided `$$...$$` for display math, but offered no alignment, numbering, or multi-line capabilities. The American Mathematical Society developed amsmath (1997) to provide professional-grade display math for their journal publications. Today, amsmath is the de-facto standard for any serious mathematics typesetting.

For this project: KK geometry, NCG spectral triples, Dirac spectra, and gap equations require aligned derivations, custom operators, and precise symbol placement.

---

## The amsmath Package

Load it early in your preamble:

```latex
\usepackage{amsmath}
\usepackage{amssymb}      % for \mathbb, \mathcal, \mathfrak
\usepackage{amsthm}       % for theorem environments
```

---

## Equation Environments

### Basic Unnumbered Display Math

```latex
\[
  E = mc^2
\]
```

### Numbered Equation

```latex
\begin{equation}
  S_{\text{spec}}(\tau) = \frac{1}{2\pi}
    \int_0^{\infty} t \, \text{tr}\left(e^{-tD_K^2}\right) \, dt
  \label{eq:spectral-action}
\end{equation}
```

Every equation environment creates a number. Use `*` to suppress:

```latex
\begin{equation*}
  D_K = \nabla_K + i\gamma^5 m(\tau)
\end{equation*}
```

### Alignment Environments

For multi-line derivations with aligned equality signs:

```latex
\begin{align}
  \text{LHS} &= \text{step 1} \\
             &= \text{step 2} \\
             &= \text{RHS}
\end{align}
```

Each line is numbered by default. Suppress specific lines with `\notag`:

```latex
\begin{align}
  D_K^2 &= \nabla_K^2 + \text{scalar curvature} \\
        &\quad + \text{torsion correction} \notag \\
        &= -\lambda_n^2(\tau)
  \label{eq:dk-squared}
\end{align}
```

### Gather Environment

For centered equations (no alignment):

```latex
\begin{gather}
  \text{Dirac operator:} \quad D_K = \gamma^{\mu} \nabla_{\mu} + m(\tau) \\
  \text{Eigenvalue equation:} \quad D_K \psi_n = \lambda_n \psi_n
\end{gather}
```

### Multline Environment

For very long equations that span multiple lines (unaligned):

```latex
\begin{multline}
  \mathcal{S}_{\text{total}}(\tau) =
    \int_0^{\infty} t^{a_4/2 - 1} \text{tr}\left(e^{-tD_K^2}\right) \, dt \\
    + \text{higher-order corrections}
  \label{eq:long-action}
\end{multline}
```

### Split Environment (Sub-display)

For alignment within a larger equation:

```latex
\begin{equation}
\begin{split}
  g_1(\tau) - g_2(\tau) &= e^{-2\tau} \\
  \Rightarrow \quad \log\left(\frac{g_1}{g_2}\right) &= -2\tau
\end{split}
\label{eq:coupling-ratio}
\end{equation}
```

---

## Automatic Operators and Functions

Define custom operators for consistency:

```latex
\DeclareMathOperator{\tr}{tr}      % trace
\DeclareMathOperator{\id}{id}      % identity
\DeclareMathOperator{\diag}{diag}  % diagonal
\DeclareMathOperator{\rank}{rank}  % rank
\DeclareMathOperator{\spec}{spec}  % spectrum
```

Usage in equations:

```latex
\tr(D_K^n) = \sum_{i} \lambda_i^n
```

vs. without operator:

```latex
tr(D_K^n) = \sum_{i} \lambda_i^n  % looks wrong without \tr
```

### Physics-Specific Operators

```latex
\DeclareMathOperator{\sgn}{sgn}    % sign function
\renewcommand{\Re}{\operatorname{Re}}  % real part (redefines existing \Re)
\renewcommand{\Im}{\operatorname{Im}}  % imaginary part (redefines existing \Im)
```

---

## Mathematical Symbols

`amssymb` provides comprehensive mathematical symbols unavailable in standard LaTeX:

### Blackboard Bold (Number Sets)

```latex
\mathbb{R}, \mathbb{C}, \mathbb{N}, \mathbb{Z}, \mathbb{H}
% produces: R, C, N, Z, H (double-struck)
```

Usage:
```latex
\text{Eigenvalues} \in \mathbb{R} \cup i\mathbb{R}
```

### Calligraphic (for algebras and spaces)

```latex
\mathcal{A}   % algebra A
\mathcal{H}   % Hilbert space H
\mathcal{S}   % spectral action S
```

### Fraktur (for Lie algebras)

```latex
\mathfrak{su}(3), \mathfrak{so}(4), \mathfrak{g}
```

### Additional Symbols

```latex
\Box              % d'Alembertian
\diamond          % generic operator
\star             % Hodge star
\flat, \sharp     % musical isomorphisms (lowering/raising indices)
\angle, \sphericalangle  % angles
\varnothing       % empty set (better than \emptyset)
\nexists          % negated exists
\approx           % approximately equal
\equiv            % identically equal
\ll, \gg          % much less/greater than
\lesssim, \gtrsim % less/greater than or similar
```

---

## Delimiters and Scaling

### Automatic Scaling with `\left` and `\right`

```latex
\left( \frac{\partial D_K}{\partial \tau} \right)^2

\left[ \sum_{n=1}^{\infty} \lambda_n \right]_{|\tau=0.5}

\left\{ \psi : D_K \psi = \lambda_n \psi \right\}
```

### Manual Scaling

When automatic scaling fails or looks wrong:

```latex
\big(, \Big(, \bigg(, \Bigg(   % increasing sizes
\big), \Big), \bigg), \Bigg)
\big|, \Big|, \bigg|, \Bigg|   % vertical bars
\big\{, \Big\{, \bigg\{, \Bigg\{  % braces
```

Example:
```latex
\Bigg( \int_0^{\infty} e^{-\lambda t} \, dt \Bigg)
```

### Invisible Delimiters

Sometimes you need a scaled delimiter on only one side:

```latex
\left. \frac{dV}{d\tau} \right|_{\tau=0.15}
% The \left. creates invisible left delimiter
```

---

## Array Environments

### Matrix

```latex
\begin{pmatrix}
  a_{11} & a_{12} \\
  a_{21} & a_{22}
\end{pmatrix}

% Other variants:
% bmatrix: [...]
% vmatrix: |...|  (determinant)
% Vmatrix: ||...||
% smallmatrix: inline size
```

### General Array

```latex
\begin{array}{c|c}
  \lambda_+ & \lambda_- \\
  \hline
  1.531 & 0.117
\end{array}

% Alignment: l (left), c (center), r (right)
% Separators: | (vertical line), \hline (horizontal line)
```

---

## Spacing in Math Mode

### Built-in Spaces

```latex
a \, b      % thin space (3/18 em)
a \: b      % medium space (4/18 em)
a \; b      % thick space (5/18 em)
a \quad b   % one em
a \qquad b  % two em
a \! b      % negative thin space
```

Usage example:

```latex
\int_0^{\infty} e^{-\lambda t} \, dt  % \, after limit improves spacing
\text{tr}(A B) = \text{tr}(B A)       % use \text{} for words
```

### Text within Equations

```latex
D_K \text{ is block-diagonal }  \Rightarrow \text{ CPT is preserved}
```

---

## Numbering Control

### Counters and Labeling

```latex
\begin{align}
  \text{Eq. 1} \label{eq:one}   \\
  \text{Eq. 2} \label{eq:two}   \\
  \text{Eq. 3} \notag            % no number for this line
\end{align}

% Reference:
From \eqref{eq:one} and \eqref{eq:two}...
```

### Reset Numbering per Section

In preamble:

```latex
\numberwithin{equation}{section}  % eqs numbered 1.1, 1.2, 2.1, etc.
```

---

## Theorem Environments with amsmath

```latex
\usepackage{amsthm}

\theoremstyle{plain}
\newtheorem{theorem}{Theorem}[section]
\newtheorem{corollary}[theorem]{Corollary}

\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}

\begin{theorem}[Block-Diagonality of D_K]
\label{thm:dk-block}
Let $(A, H, D)$ be the Jensen-deformed spectral triple.
Then $D_K$ is exactly block-diagonal in the Peter-Weyl basis,
with block dimensions given by $r_i^2$ for representation $i$.
\end{theorem}

\begin{proof}
Left-invariance implies...
\end{proof}
```

---

## Common Pitfalls

1. **Mismatched parentheses in `\left...\right`**: Both must be present (use `.` for invisible).
2. **Equation numbering reset**: Check `\numberwithin{equation}{section}` behavior.
3. **Symbol collision**: `\times` (product) vs `\cdot` (dot product) - use intentionally.
4. **Decimal alignment**: Use `S` column specifier from `siunitx` package for tables, not manual spacing.

---

## Best Practices for NCG and Differential Geometry

### Tensor Index Notation

```latex
\[
  g_{\mu\nu}, \quad
  \Gamma^{\lambda}_{\mu\nu}, \quad
  R^{\rho}_{\sigma\mu\nu}, \quad
  \nabla_{\mu} T^{\alpha\beta}
\]
```

### Dirac Operator Notation

```latex
D_K = \gamma^{\mu}(\tau) \nabla_{\mu} + m(\tau) \mathbb{1}

\langle \psi | D_K | \phi \rangle
```

### Spectral Notation

```latex
(A, H, D) \quad \text{spectral triple}

\text{KO-dim} = 6

\lambda_n(\tau), \quad \psi_n(\tau) \quad \text{eigenvalues/eigenvectors}
```

---

## Connection to Phonon-Exflation Framework

AMS-LaTeX enables:
- Precise tensor notation for KK geometry (covariant derivatives, Riemann tensors)
- Multi-line aligned derivations for the spectral action computation
- Custom operators (\tr, \diag, \spec) for Dirac spectrum expressions
- Theorem environments for proved results (block-diagonality, KO-dimension=6, SM charges)
- Mathematical rigor required for JGP and CMP submissions
- Proper alignment of gap equations and eigenvalue flows

Relevance to Project: **CRITICAL** - amsmath is the foundation for all mathematical content in Phonon-Exflation papers.
