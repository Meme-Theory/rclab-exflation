# Physics Symbol Conventions and Notation Standards

**Author(s):** ISO 80000 committee, IUPAP (International Union of Pure and Applied Physics), CODATA
**Year:** 2009+ (ISO 80000 parts), 2020+ (modern updates)
**Reference:** ISO 80000-2 (Mathematical notation), ISO 80000-13 (Space and time in physics)

---

## Abstract

Consistent symbol notation across a multi-section paper ensures readability and professionalism. This document covers standard physics conventions: Greek vs Latin indices, decorations (hat, bar, tilde, dagger), font families (calligraphic, fraktur, blackboard bold), spacing around operators, and domain-specific conventions (tensors, operators, states). Emphasis is placed on maintaining notation consistency within the phonon-exflation project across multiple authors and papers.

---

## Historical Context

Scientists have always used symbols, but standardization emerged gradually. The International Organization for Standardization (ISO) codified mathematical and physical notation in ISO 80000 (2009-2019), replacing the older ISO 31. Physicists additionally follow CODATA (Internationally Recommended Values of Physical Constants) for standard notation. Failure to maintain consistent notation is a primary source of confusion in collaborative manuscripts.

For phonon-exflation: Multiple authors and venues (JHEP, PRD, CMP, JGP) require agreed-upon conventions to avoid notation conflicts.

---

## Index Notation: Systematic Approach

### Greek Indices (Spacetime, 4D)

```latex
% Spacetime indices: \mu, \nu, \rho, \sigma, \lambda, \alpha, \beta, \gamma
% Run 0, 1, 2, 3

g_{\mu\nu}              % metric tensor
T^{\mu\nu}              % contravariant tensor
\nabla_{\mu}            % covariant derivative
\partial_{\mu} A_{\nu}  % partial derivative
```

**Convention**: Use Greek for spacetime in 4D GR, cosmology contexts.

### Latin Indices (Spatial 3D)

```latex
% Spatial indices: i, j, k, l, m, n
% Run 1, 2, 3

\gamma_{ij}             % spatial metric
\partial_i V            % spatial gradient
\epsilon_{ijk}          % Levi-Civita (totally antisymmetric)
```

**Convention**: Use Latin for 3D spatial parts of 4D tensor.

### Internal/Fiber Indices

```latex
% Gauge/Lie algebra indices: a, b, c, d
% Run 1, ..., \dim(G)

A_{\mu}^{a}             % gauge field (SU(3): a = 1,...,8)
F_{\mu\nu}^{a}          % field strength
T^{a}_{bc}              % structure constants
```

### Spinor and Component Indices

```latex
% Spinor indices (Dirac): \alpha, \beta
% Run 1, 2, 3, 4

\psi_{\alpha}           % 4-component Dirac spinor
\gamma^{\mu}_{\alpha\beta}  % gamma matrix component

% Weyl spinors: A, B, \dot{A}, \dot{B} (primed for conjugate)
\psi_{A}, \quad \bar{\psi}^{\dot{A}}
```

---

## Decorations: Hats, Bars, Tildes, Daggers

### Conventions

```latex
% Quantum operators (hat): \hat{X}
\hat{H}                 % Hamiltonian operator
\hat{p}                 % momentum operator
\hat{a}, \hat{a}^{\dagger}  % creation/annihilation operators

% Complex conjugate (bar): \bar{z}
\bar{z}                 % complex conjugate of z
\overline{\psi}         % or \overline{} for longer expressions
\psi^*                  % alternative notation (not preferred in modern physics)

% Tilde: \tilde{X}
\tilde{g}_{\mu\nu}      % perturbed metric
\tilde{Q}               % modified quantity

% Dagger (adjoint): X^{\dagger}
A^{\dagger}             % Hermitian adjoint of operator A
|\psi\rangle^{\dagger} = \langle\psi|  % adjoint of state

% Dot and double-dot: \dot{X}, \ddot{X}
\dot{a}(t)              % first time derivative
\ddot{a}(t)             % second time derivative
```

### When to Use Each

- **Hat** ($\hat{A}$): Operators in quantum mechanics and field theory
- **Bar** ($\bar{\psi}$): Complex conjugate or Dirac conjugate ($\bar{\psi} = \psi^{\dagger} \gamma^0$)
- **Tilde** ($\tilde{g}$): Perturbations, transformed, or modified quantities
- **Dagger** ($A^{\dagger}$): Hermitian adjoint of operators
- **Dot** ($\dot{a}$): Time derivatives in cosmology/dynamical systems

---

## Font Families

### Calligraphic (Fancy/Script)

```latex
\mathcal{A}   % Algebra
\mathcal{H}   % Hilbert space
\mathcal{L}   % Lagrangian or Lie group
\mathcal{M}   % Manifold
\mathcal{S}   % Action or spectrum
\mathcal{G}   % Gauge group
```

**Use**: Spaces, algebras, function spaces, group names.

### Fraktur (Gothic)

```latex
\mathfrak{g}          % Lie algebra (lower case)
\mathfrak{su}(3)      % specific Lie algebra
\mathfrak{gl}_n       % general linear algebra
\mathfrak{so}(4)      % orthogonal algebra
```

**Use**: Lie algebras, sometimes for differential forms.

### Blackboard Bold (Double-Struck)

```latex
\mathbb{R}   % Real numbers
\mathbb{C}   % Complex numbers
\mathbb{Z}   % Integers
\mathbb{N}   % Natural numbers
\mathbb{Q}   % Rationals
\mathbb{H}   % Quaternions or Hilbert space (context-dependent)
\mathbb{G}   % Groups (sometimes, e.g., \mathbb{G}_m)
```

**Use**: Number fields, formal sets.

### Bold (Roman)

```latex
\mathbf{v}   % Vector (3D spatial)
\mathbf{F}   % Force vector
\mathbf{B}   % Magnetic field

% Note: For 4-vectors, use plain: A^{\mu}, not \mathbf{A}^{\mu}
```

**Use**: Classical vectors (rarely in modern theoretical physics; tensor notation preferred).

---

## Specific Domain Conventions

### Quantum Mechanics Notation

```latex
% States and operators
|\psi\rangle            % ket (state)
\langle\psi|            % bra (covector)
\langle\psi|\hat{O}|\phi\rangle  % expectation value

% Commutators and anticommutators
[\hat{A}, \hat{B}] = \hat{A}\hat{B} - \hat{B}\hat{A}  % commutator
\{\hat{A}, \hat{B}\} = \hat{A}\hat{B} + \hat{B}\hat{A}  % anticommutator

% Eigenvalue equations
\hat{H}|\psi_n\rangle = E_n |\psi_n\rangle
```

### General Relativity / Differential Geometry

```latex
% Curvature tensors
R^{\rho}_{\sigma\mu\nu}      % Riemann tensor (one index down)
R_{\mu\nu}                   % Ricci tensor
R                            % scalar curvature (plain Roman)
g_{\mu\nu}                   % metric tensor
\Gamma^{\lambda}_{\mu\nu}    % Christoffel connection

% Derivatives
\partial_{\mu}               % partial derivative
\nabla_{\mu}                 % covariant derivative
\Box = \nabla^2              % d'Alembertian
```

### Field Theory

```latex
% Fields
\phi(x), \psi(x)             % classical fields
\Phi(x), \Psi(x)             % quantum field operators
A_{\mu}^{a}                  % gauge field
F_{\mu\nu}                   % field strength

% Coupling constants
g, e, \lambda, y_t           % coupling constants (lowercase Greek/Latin)

% Actions and Lagrangians
\mathcal{L}                  % Lagrangian density
\mathcal{S} = \int d^4x \mathcal{L}  % action

% Propagators and correlators
\Delta_F(x-y)                % Feynman propagator
\langle\phi(x)\phi(y)\rangle % correlation function
```

### Thermodynamics / Statistical Mechanics

```latex
T                            % temperature
\beta = 1/(k_B T)           % inverse temperature
\mu                          % chemical potential
Z = \sum_n e^{-\beta E_n}   % partition function (Gothic: \mathfrak{Z})

% Thermodynamic potentials
F, G, H, U                   % free energy, Gibbs, enthalpy, internal energy
S                            % entropy
```

---

## Spacing Conventions

### Spacing Around Operators

```latex
% Multiplication (implicit, no explicit times)
a b              % product (no \times or \cdot needed in math mode)

% Dot product
\mathbf{a} \cdot \mathbf{b}  % three-vector dot product
T^{\mu\nu} g_{\mu\nu}        % tensor contraction (implicit, no dot)

% Cross product
\mathbf{a} \times \mathbf{b}

% Tensor product
A \otimes B      % outer product, representation tensor

% Direct sum
V \oplus W       % direct sum of vector spaces
```

### Functional/Calculus Spacing

```latex
% Differential
f(x) \, dx       % \, adds thin space for readability
\int f(x) \, dx  % standard integral notation

% Functional derivative
\frac{\delta S}{\delta \phi(x)}  % functional derivative

% Partial derivatives
\frac{\partial}{\partial x^{\mu}}  % vertical spacing

% Total time derivative
\frac{d}{dt}, \quad \dot{a}(t)
```

---

## Cross-Domain Symbol Conflicts

### Potentially Ambiguous Symbols

```latex
% R: Could mean real numbers, curvature, universal gas constant
\mathbb{R}                   % real numbers (use blackboard bold)
R                            % curvature scalar (plain)

% Z: Could mean integers, partition function, impedance
\mathbb{Z}                   % integers (use blackboard bold)
Z                            % partition function (plain, or \mathfrak{Z})

% H: Could mean Hamiltonian, Hilbert space, enthalpy
\hat{H}                      % Hamiltonian operator (use hat)
\mathcal{H}                  % Hilbert space (use calligraphic)
H                            % enthalpy (plain, context-dependent)
```

**Strategy**: Use font distinctions (hat, calligraphic, blackboard) to disambiguate.

---

## Notation for Phonon-Exflation Specific Terms

Create a **notation table** at the start of each paper:

```latex
\section*{Notation}

\begin{tabular}{ll}
  Symbol & Meaning \\
  \hline
  $(A, \mathcal{H}, D)$ & Spectral triple \\
  $D_K$ & Dirac operator on SU(3) \\
  $\lambda_n(\tau)$ & Eigenvalues as function of deformation \\
  $(p,q)$ & SU(3) representation labels \\
  $\tau$ & Jensen deformation parameter \\
  $\mathcal{S}_{\text{spec}}$ & Spectral action \\
  $a_{2k}$ & Seeley-DeWitt coefficients \\
  KO-dim & K-theory (real) dimension \\
\end{tabular}
```

---

## Creating a Style Guide for Collaboration

### Team Conventions Document

```latex
% phonon-exflation-conventions.sty

% Spacing and consistency
\newcommand{\stiple}{(A, \mathcal{H}, D)}
\newcommand{\dirac}{D_K}
\newcommand{\saction}{\mathcal{S}_{\text{spec}}}
\newcommand{\repr}[2]{(#1,#2)}  % representation (p,q)

% Ensure all authors use same definitions
\newcommand{\komode}{\text{KO-dim}}  % vs \textrm{KO-dim}
```

Import in all papers:
```latex
\usepackage{phonon-exflation-conventions}
```

---

## Common Pitfalls

1. **Inconsistent index notation**: Using $i$ for both spatial and Lie algebra indices (confusing).
2. **Forgetting blackboard bold**: Writing $R$ for real numbers instead of $\mathbb{R}$.
3. **Mixing decorations**: Using both $\hat{A}$ and $\tilde{A}$ interchangeably without clear distinction.
4. **No notation section**: Assuming readers remember all definitions from 50 pages earlier.
5. **Unicode vs LaTeX**: Avoid typing `α` directly; always use `\alpha` (LaTeX command).

---

## Checklist Before Submission

- [ ] All indices used consistently (Greek = spacetime, Latin = spatial, etc.)
- [ ] All operators have appropriate decorations (\hat for quantum, \bar for conjugate)
- [ ] Font families used distinctly (\mathcal for spaces, \mathfrak for algebras, \mathbb for numbers)
- [ ] Spacing correct around differentials and integrals (\, after dx)
- [ ] Notation section included early in paper
- [ ] All unusual symbols explained at first use
- [ ] References to notation consistent throughout (no D_K vs D switching)

---

## Connection to Phonon-Exflation Framework

Notation consistency enables:
- Clear communication across multiple authors (team papers)
- Reproducible manuscripts for different venues (JHEP, PRD, CMP, JGP)
- Professional appearance in peer review
- Reduced errors from symbol misinterpretation
- Faster reading comprehension for specialists
- Automated symbol checking via style files

Relevance to Project: **HIGH** - Consistent notation is non-negotiable in multi-author theoretical physics papers.
