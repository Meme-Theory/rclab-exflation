# Custom LaTeX Macros for Large Physics Papers

**Author(s):** LaTeX Community, Macro Design Best Practices
**Year:** 2020+ (contemporary practices)
**Reference:** "The TeXbook" (Knuth), "LaTeX Companion" (Mittelbach et al.), `physics` package

---

## Abstract

Macros (custom LaTeX commands) are essential for large, multi-section papers. Well-designed macros enforce consistent notation, reduce typing errors, and facilitate notation changes. This document covers macro design patterns: semantic vs presentational macros, operator definitions, braket notation, derivative notation via the `physics` package, and team-wide macro libraries. For the phonon-exflation project, a centralized macro file ensures all authors use identical notation for spectral triples, Dirac operators, and quantum numbers.

---

## Historical Context

Donald Knuth designed TeX to separate content from presentation. LaTeX extends this via macros (\command). A well-designed macro library makes a paper maintainable: changing notation requires editing one definition, not 200 occurrences. The `physics` package (2013-) provides pre-built macros for physicists, including braket notation and derivatives. Modern collaborative papers use shared macro files in git to enforce consistency.

For phonon-exflation: Consistent notation for (A, H, D), D_K, lambda_n, tau, and [p,q] quantum numbers across 4-6 authors requires a shared macro library.

---

## Macro Fundamentals

### Simple Substitution

```latex
% Define
\newcommand{\stiple}{(A, \mathcal{H}, D)}

% Use (same effect as typing the expansion)
The spectral triple \stiple\ generates...
% Expands to: The spectral triple (A, \mathcal{H}, D) generates...
```

### Macro with One Argument

```latex
\newcommand{\repr}[1]{\lambda_{#1}}

% Use
The $n$-th eigenvalue is \repr{n}.
% Expands to: The $n$-th eigenvalue is \lambda_{n}.
```

### Macro with Multiple Arguments

```latex
\newcommand{\innerproduct}[2]{\langle #1 | #2 \rangle}

% Use
The overlap is \innerproduct{\psi}{\phi}.
% Expands to: The overlap is \langle \psi | \phi \rangle.
```

### Optional Arguments

```latex
\newcommand{\tensor}[3][space]{
  #2^{\phantom{X}}_{#3}  % optional [space] for formatting
}

% Use (with and without optional arg)
\tensor{T}{a}{b}      % Uses default [space]
\tensor[big]{T}{a}{b} % Specifies big spacing
```

---

## Semantic vs Presentational Macros

**Semantic macro**: Name describes what it is, not how it looks.
**Presentational macro**: Name describes how it looks.

### Anti-Pattern (Presentational)

```latex
\newcommand{\bold}[1]{\mathbf{#1}}
\newcommand{\italics}[1]{\textit{#1}}

% Problem: Later, if you want to change bold to red,
% you must rename \bold everywhere in your paper.
% The name no longer describes the content.
```

### Better Pattern (Semantic)

```latex
\newcommand{\algebra}[1]{\mathcal{#1}}  % Names mean "Lie algebra"
\newcommand{\hilbertspace}{\mathcal{H}}
\newcommand{\diracop}{D_K}

% Now if you change Hilbert space notation from \mathcal to \mathfrak,
% only the definition changes:
% \renewcommand{\hilbertspace}{\mathfrak{H}}
```

---

## Operator Definitions

### Using \DeclareMathOperator

```latex
\usepackage{amsmath}

% Define operators
\DeclareMathOperator{\tr}{tr}      % trace
\DeclareMathOperator{\id}{id}      % identity
\DeclareMathOperator{\diag}{diag}  % diagonal part
\DeclareMathOperator{\rank}{rank}  % rank
\DeclareMathOperator{\spec}{spec}  % spectrum
\DeclareMathOperator{\sign}{sign}  % sign function

% Usage
\[
  \tr(D_K^n) = \sum_i \lambda_i^n
\]
```

Why not just type `tr`? Because `\DeclareMathOperator` adds proper spacing and font:
- `tr(x)` with `\DeclareMathOperator` looks like function notation
- `tr(x)` typed directly looks like three separate variables

### Physics Operators

```latex
\renewcommand{\Re}{\operatorname{Re}}  % real part (redefines existing \Re)
\renewcommand{\Im}{\operatorname{Im}}  % imaginary part (redefines existing \Im)
\DeclareMathOperator{\Aut}{Aut}    % automorphism group
\DeclareMathOperator{\ad}{ad}      % adjoint representation
\DeclareMathOperator{\Ad}{Ad}      % Adjoint representation
```

---

## The `physics` Package

### Loading and Braket Notation

```latex
\usepackage{physics}

% Braket notation
\ket{\psi}              % |psi>
\bra{\psi}              % <psi|
\braket{\psi}{\phi}     % <psi|phi>
\ketbra{\psi}{\phi}     % |psi><phi| (outer product)
\norm{\psi}             % ||psi||

% Quantum mechanics
\expval{A}              % <A> (expectation value)
\expval{A}{\psi}        % <psi|A|psi>

% Matrix elements
\mel{\alpha}{O}{\beta}  % <alpha|O|beta>
```

### Derivative Notation

```latex
\usepackage{physics}

% Partial derivatives
\pdv{f}{x}              % df/dx
\pdv{f}{x}{y}           % d^2 f/dx dy
\pdv[n]{f}{x}           % d^n f/dx^n

% Total derivatives
\dv{f}{x}               % df/dx (same as \pdv for functions of one variable)
\dv[2]{f}{x}            % d^2 f/dx^2

% Functional derivatives
\fdv{F}{\phi}           % delta F / delta phi

% Usage in equations
\frac{\pdv{V}{\tau}}{\pdv{V}{\phi}} = \frac{1}{m_{(3,0)}}
```

### Commutators and Anticommutators

```latex
\usepackage{physics}

\comm{A}{B}             % [A,B]
\acomm{A}{B}            % {A,B} (anticommutator)
\poissonbracket{f}{g}   % {f,g}
```

---

## Building a Team Macro File

### Create `phonon_exflation.sty`

```latex
% phonon_exflation.sty
% Macro definitions for phonon-exflation cosmology papers
% Use: \usepackage{phonon_exflation}

\ProvidesPackage{phonon_exflation}[2024/02/21 Phonon-exflation framework]

% Core packages
\RequirePackage{amsmath}
\RequirePackage{amssymb}
\RequirePackage{physics}

% ========== SPECTRAL GEOMETRY ==========

% Spectral triple components
\newcommand{\algebra}[1]{\mathcal{#1}}
\newcommand{\hilbert}{\mathcal{H}}
\newcommand{\stiple}{(\algebra{A}, \hilbert, D)}

% Dirac operator
\newcommand{\diracK}{D_K}
\newcommand{\diracKtau}[1]{D_K(#1)}

% Eigenvalues and states
\newcommand{\eigval}[1]{\lambda_{#1}}
\newcommand{\eigstate}[1]{\psi_{#1}}
\newcommand{\eigpair}[1]{(\eigval{#1}, \eigstate{#1})}

% ========== QUANTUM NUMBERS ==========

% SU(3) representation labels
\newcommand{\reprlabel}[2]{(#1, #2)}
\newcommand{\repr}[3]{#1_{\reprlabel{#2}{#3}}}

% Usage: \repr{\psi}{p}{q} gives psi_{(p,q)}

% ========== OPERATORS ==========

\DeclareMathOperator{\tr}{tr}
\DeclareMathOperator{\id}{id}
\DeclareMathOperator{\diag}{diag}
\DeclareMathOperator{\rank}{rank}
\DeclareMathOperator{\spec}{spec}
\DeclareMathOperator{\kodimdim}{KO\text{-}dim}

% ========== SPECTRAL ACTION ==========

\newcommand{\saction}{S_{\text{spec}}}
\newcommand{\sactiontau}[1]{S_{\text{spec}}(#1)}
\newcommand{\vspec}{V_{\text{spec}}}
\newcommand{\vspecdata}[2]{V_{\text{spec}}(#1; #2)}

% Seeley-DeWitt coefficients
\newcommand{\sdcoeff}[1]{a_{#1}}

% ========== PARAMETERS ==========

\newcommand{\defparam}{\tau}  % deformation parameter
\newcommand{\defrange}{[0, 0.5]}

% ========== METRICS ==========

\newcommand{\metricround}{g^{(0)}_{\mu\nu}}
\newcommand{\metricjensen}{\tilde{g}_{\mu\nu}(\tau)}

\endinput
```

---

## Using the Team Macro File

In all phonon-exflation papers:

```latex
\documentclass[11pt]{article}
\usepackage{phonon_exflation}

\begin{document}

\section{Spectral Triple}

We study the spectral triple $(\stiple)$ where
the algebra is $C^{\infty}(\text{SU}(3))$.
The Dirac operator $\diracK$ satisfies...

The eigenvalues $\eigval{n}(\defparam)$ and eigenstates
$\eigstate{n}(\defparam)$ evolve as $\defparam \in \defrange$.

The spectral action is $\saction(\defparam) = \sum_n \eigval{n}(\defparam)$.

For representation $\reprlabel{p}{q}$, the quantum number sector
carries dimension $(2p+1)(2q+1)$.

\end{document}
```

---

## Advantages of Macro Files

1. **Consistency**: All papers use identical notation
2. **Ease of update**: Change definition once, all papers update
3. **Error reduction**: Less typing = fewer typos
4. **Onboarding**: New authors learn notation from one file
5. **Collaboration**: Shared .sty file in git repository

---

## Version Control Best Practice

In git repository:

```
phonon-exflation/
  phonon_exflation.sty          # Shared macros
  papers/
    no-go_paper/
      paper.tex
      paper.bbl
      figures/
    spectral_anatomy/
      paper.tex
      paper.bbl
      figures/
```

All `paper.tex` files load `phonon_exflation.sty`:

```latex
\usepackage{../../../phonon_exflation}
```

Or with `\graphicspath` and path setup:

```latex
\usepackage{../phonon_exflation}  % relative path to shared .sty
```

---

## Advanced: Conditional Macros

### Switching Between Notations

Sometimes you need different notation for different venues:

```latex
\usepackage[<option>]{phonon_exflation}

% In phonon_exflation.sty
\newif\ifCompactNotation
\CompactNotationtrue  % or false

\ifCompactNotation
  \newcommand{\diracK}{D}      % compact version
\else
  \newcommand{\diracK}{D_K}    % full version
\fi
```

Use in document preamble:

```latex
\usepackage[compact]{phonon_exflation}  % uses short notation
```

### Draft vs Final

```latex
\newif\ifDraft
\Drafttrue  % set to false for final submission

\ifDraft
  \usepackage{geometry}
  \geometry{margin=1in, showframe}  % show frame for layout checking
\fi
```

---

## Common Pitfalls

1. **Circular definitions**: Macro A depends on B, B on C, C on A -> infinite loop.
2. **Over-parameterization**: Macro with 5 arguments is hard to remember; simplify.
3. **No documentation**: Future you won't remember what \xyz does. Add comments.
4. **Fragile macros**: Use `\DeclareRobustCommand` if used in section headings.

---

## Macro Template for Phonon-Exflation

```latex
\newcommand{\mycommand}[1]{%
  % Description: explains what this macro does
  % Usage: \mycommand{argument} produces output
  % Example: \mycommand{D_K} yields ...
  %
  \ifthenelse{\equal{#1}{}}%
    {\textbf{Error: empty argument}}%
    {definition here}%
}
```

---

## Best Practices

1. **One semantic macro per concept**: No `\eigvalLambda` and `\eigenvalue` for same thing.
2. **Clear naming**: \diracK is clearer than \DK or \d_k.
3. **Minimal arguments**: Keep to 1-3 arguments max.
4. **Use \def sparingly**: \newcommand is safer (prevents accidental redefinition).
5. **Document in comments**: Tell future authors what each macro is for.
6. **Test in all venues**: What works in revtex might fail in jheppub; test early.

---

## Connection to Phonon-Exflation Framework

Custom macros enable:
- Uniform notation across 4-6 author team
- Rapid notation changes without re-typing (e.g., if D_K -> \hat{D} for some paper)
- Version control of mathematical definitions in .sty file
- Reduced errors in complex multi-page papers
- Professional appearance via consistent formatting
- Collaborative writing without notation conflicts
- Submission to multiple venues (JHEP, CMP, JGP, PRD) with minimal changes

Relevance to Project: **CRITICAL** - For multi-author papers, shared macro file is essential infrastructure.
