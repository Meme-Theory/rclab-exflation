# Penrose & Rindler --- Spinors and Space-Time

> **Full Title:** *Spinors and Space-Time*
> **Authors:** Roger Penrose & Wolfgang Rindler
> **Publisher:** Cambridge University Press (Cambridge Monographs on Mathematical Physics)
> **Volume 1:** *Two-Spinor Calculus and Relativistic Fields* (1984), x + 458 pp.
> **Volume 2:** *Spinor and Twistor Methods in Space-Time Geometry* (1986), x + 501 pp.

---

## Purpose and Scope

These two volumes constitute the definitive reference for the 2-spinor calculus in general relativity and the mathematical foundations of twistor theory. Volume 1 develops the full algebraic and differential machinery of 2-component spinors on a Lorentzian 4-manifold. Volume 2 extends this to twistor methods, the geometry of null congruences, conformal infinity, and quasi-local definitions of gravitational mass-energy.

The central thesis: **spinors are not auxiliary objects bolted onto tensor calculus --- they are the more primitive structure from which tensors are derived.** Every tensor on a 4-dimensional Lorentzian manifold decomposes into spinorial parts, and this decomposition reveals structure that is invisible at the tensor level.

---

## Volume 1 --- Two-Spinor Calculus and Relativistic Fields

### Chapter Structure

| Ch. | Title |
|-----|-------|
| 1 | The geometry of world-vectors and spin-vectors |
| 2 | Abstract indices and spinor algebra |
| 3 | Spinors and world-tensors |
| 4 | Differentiation and curvature |
| 5 | Fields in space-time |

---

### 1. The Spinor Algebra and $\mathrm{SL}(2,\mathbb{C})$

#### 1.1 The Double Cover of the Lorentz Group

The restricted Lorentz group $\mathrm{SO}^+(1,3)$ --- the identity component of the group preserving the Minkowski metric $\eta_{\mu\nu} = \mathrm{diag}(+1,-1,-1,-1)$ --- has as its universal covering group the special linear group:

$$\mathrm{SL}(2,\mathbb{C}) = \{ M \in \mathrm{GL}(2,\mathbb{C}) \mid \det M = 1 \}$$

The covering homomorphism is 2-to-1:

$$\mathrm{SL}(2,\mathbb{C}) \xrightarrow{\ 2:1\ } \mathrm{SO}^+(1,3)$$

with kernel $\{+I, -I\}$. The isomorphism $\mathrm{SL}(2,\mathbb{C}) \cong \mathrm{Spin}(1,3) \cong \mathrm{Sp}(2,\mathbb{C})$ reflects the fact that $\mathrm{SL}(2,\mathbb{C})$ preserves a symplectic (antisymmetric, non-degenerate) bilinear form on $\mathbb{C}^2$.

The construction proceeds via the Hermitian matrix correspondence. Any real 4-vector $V^\mu$ maps to a $2 \times 2$ Hermitian matrix:

$$V^{AA'} = \frac{1}{\sqrt{2}} \begin{pmatrix} V^0 + V^3 & V^1 - iV^2 \\ V^1 + iV^2 & V^0 - V^3 \end{pmatrix}$$

The determinant of this matrix equals $\frac{1}{2}\eta_{\mu\nu} V^\mu V^\nu$. A Lorentz transformation $V^\mu \mapsto \Lambda^\mu{}_\nu V^\nu$ corresponds to:

$$V^{AA'} \mapsto M^A{}_B \, V^{BB'} \, \bar{M}^{A'}{}_{B'}, \qquad M \in \mathrm{SL}(2,\mathbb{C})$$

Both $M$ and $-M$ give the same Lorentz transformation, which is the geometric origin of spin-$\frac{1}{2}$ behaviour.

#### 1.2 The Fundamental Representations: Unprimed and Primed Spinors

The two inequivalent fundamental representations of $\mathrm{SL}(2,\mathbb{C})$ give rise to two species of 2-component spinor:

- **Unprimed (left-handed) spinors** $\psi^A$, with $A \in \{0, 1\}$, transforming under $M \in \mathrm{SL}(2,\mathbb{C})$:

$$\psi^A \mapsto M^A{}_B \, \psi^B$$

- **Primed (right-handed, complex conjugate) spinors** $\chi^{A'}$, with $A' \in \{0', 1'\}$, transforming under the complex conjugate representation $\bar{M}$:

$$\chi^{A'} \mapsto \bar{M}^{A'}{}_{B'} \, \chi^{B'}$$

The primed representation is inequivalent to the unprimed one (unlike in Euclidean signature), which is a signature feature of Lorentzian geometry. The two representations are related by complex conjugation:

$$\overline{\psi^A} = \bar{\psi}^{A'}$$

Higher-valence spinors carry multiple indices of both kinds, e.g., $T^{AB}{}_{C'D'}$.

#### 1.3 Null Flags and the Geometry of Spin-Vectors

A single non-zero spinor $\kappa^A$ determines:

1. A **null direction** (flagpole): the null vector $k^\mu$ corresponding to $k^{AA'} = \kappa^A \bar{\kappa}^{A'}$.
2. A **flag plane**: a half-plane containing the flagpole direction, whose orientation in the 2-dimensional space transverse to $k^\mu$ is determined by the phase of $\kappa^A$.

Under $\kappa^A \mapsto e^{i\theta}\kappa^A$, the flagpole is unchanged but the flag plane rotates by $2\theta$. Under $\kappa^A \mapsto -\kappa^A$ (a $2\pi$ rotation), the flag returns to its original position but the spinor has changed sign --- this is the geometric manifestation of spinorial double-valuedness.

#### 1.4 Spin-Frames (Dyads)

A **spin-frame** or **dyad** is a pair of spinors $(o^A, \iota^A)$ normalized so that:

$$o^A \iota_A = 1$$

equivalently $\epsilon_{AB} o^A \iota^B = 1$ (or by convention, in some treatments $o_A \iota^A = 1$). Any spinor can be expanded in the dyad basis:

$$\psi^A = \psi^0 \, o^A + \psi^1 \, \iota^A$$

where $\psi^0 = \psi^A \iota_A$ and $\psi^1 = -\psi^A o_A$.

The associated null tetrad is:

$$l^a = o^A \bar{o}^{A'}, \quad n^a = \iota^A \bar{\iota}^{A'}, \quad m^a = o^A \bar{\iota}^{A'}, \quad \bar{m}^a = \iota^A \bar{o}^{A'}$$

with $l^a n_a = 1$, $m^a \bar{m}_a = -1$, all other inner products vanishing. This is the Newman--Penrose null tetrad.

> **Convention note.** The normalization $l^a n_a = +1$, $m^a \bar{m}_a = -1$ used here (the Penrose--Rindler convention) differs in sign from the original Newman--Penrose (1962) convention $\ell_\mu n^\mu = -1$, $m_\mu \bar{m}^\mu = +1$ (see Paper 08 in this folder). The two conventions are related by an overall sign flip in the metric completeness relation and produce sign differences in some spin coefficients. When comparing equations between this document and Paper 08, the normalization convention must be tracked.

---

### 2. Abstract Index Notation and the Spinor Metric

#### 2.1 Abstract Index Convention

Penrose and Rindler introduce and systematically employ **abstract index notation**, in which indices are labels denoting the type of a tensor or spinor, not components in a basis. A tensor $T^{ab}{}_{c}$ denotes an element of $\mathcal{T}^{(2,1)}$ --- the label $a$ says "contravariant slot of type vector," not "the $a$-th component."

This convention eliminates the notational ambiguity between a tensor as a geometric object and its array of components, while retaining the powerful computational facility of index manipulation.

#### 2.2 The Spinor Metric $\epsilon_{AB}$

The $\mathrm{SL}(2,\mathbb{C})$-invariant antisymmetric bilinear form on spin-space:

$$\epsilon_{AB} = -\epsilon_{BA}, \qquad \epsilon_{01} = 1$$

This is the **spinor metric**, analogous to $g_{\mu\nu}$ but antisymmetric. Its inverse satisfies:

$$\epsilon^{AB} \epsilon_{CB} = \delta^A_C$$

with the sign convention:

$$\epsilon^{01} = -1 \quad (\text{so that } \epsilon^{AB} = -\epsilon_{AB} \text{ as matrices})$$

Index raising and lowering is performed as:

$$\psi_A = \psi^B \epsilon_{BA}, \qquad \psi^A = \epsilon^{AB} \psi_B$$

**The order of contraction matters** because of the antisymmetry:

$$\psi_A = \psi^B \epsilon_{BA} = -\psi^B \epsilon_{AB}$$

This sign subtlety is a persistent source of error. The mnemonic: **the summed index comes first on epsilon when lowering**.

Similarly, the conjugate spinor metric $\epsilon_{A'B'}$ raises and lowers primed indices with identical conventions.

#### 2.3 Fundamental Identities

The completeness relation for $\epsilon$:

$$\epsilon_{AB} \epsilon^{CD} = \delta_A^C \delta_B^D - \delta_A^D \delta_B^C$$

For any pair of spinors:

$$\kappa^A \lambda_A = -\lambda^A \kappa_A$$

Any antisymmetric spinor of valence $\binom{0}{2}$ is proportional to $\epsilon_{AB}$:

$$X_{[AB]} = \frac{1}{2} X_{CD} \epsilon^{CD} \epsilon_{AB}$$

This reflects the fact that $\bigwedge^2(\mathbb{C}^2) \cong \mathbb{C}$: there is only one independent antisymmetric 2-spinor (up to scale).

---

### 3. The Spinor--Tensor Correspondence

#### 3.1 The Infeld--van der Waerden Symbols

The bridge between tensor indices $\mu, \nu, \ldots$ and spinor index pairs $AA', BB', \ldots$ is provided by the **Infeld--van der Waerden symbols** (soldering form):

$$\sigma^\mu{}_{AA'}$$

These are the components (in a chosen basis) of the isomorphism between the tangent space $T_pM$ and the space of Hermitian spinors $S \otimes \bar{S}$. In a standard basis, they reduce to $\frac{1}{\sqrt{2}}(\mathbf{1}, \boldsymbol{\sigma})$ where $\boldsymbol{\sigma} = (\sigma_1, \sigma_2, \sigma_3)$ are the Pauli matrices.

#### 3.2 The Fundamental Correspondence

Every world-tensor index $a$ corresponds to a pair of spinor indices $AA'$:

$$V^a \longleftrightarrow V^{AA'}$$

The spacetime metric is encoded as:

$$g_{ab} = \epsilon_{AB} \epsilon_{A'B'}$$

or equivalently $g^{ab} = \epsilon^{AB} \epsilon^{A'B'}$. This is the spinor form of the metric --- the entire metrical structure of spacetime is contained in the pair of epsilon spinors.

#### 3.3 Null Vectors and Flagpoles

A vector $k^a$ is **null** if and only if it factorizes as a product of a spinor with its conjugate:

$$k^a \text{ is null} \iff k^{AA'} = \xi^A \bar{\xi}^{A'}$$

for some spinor $\xi^A$. The spinor $\xi^A$ is the **flagpole spinor** of the null vector. Conversely, a general (possibly non-null) vector $V^a$ corresponds to $V^{AA'}$ which is a general Hermitian matrix --- it cannot be factored as a simple product $\alpha^A \bar{\beta}^{A'}$ unless $V^a$ is null.

#### 3.4 Decomposition of Antisymmetric Tensors

Any real antisymmetric tensor (2-form) $F_{ab} = F_{[ab]}$ decomposes as:

$$F_{ab} = F_{ABA'B'} = \varphi_{AB} \epsilon_{A'B'} + \bar{\varphi}_{A'B'} \epsilon_{AB}$$

where $\varphi_{AB} = \varphi_{(AB)}$ is a symmetric spinor. For the electromagnetic field tensor, $\varphi_{AB}$ is the **Maxwell spinor**, encoding the three complex components of the self-dual part of the field.

The Maxwell spinor factorizes as:

$$\varphi_{AB} = \alpha_{(A} \beta_{B)}$$

and the two spinors $\alpha^A, \beta^A$ define the two **principal null directions** of the electromagnetic field (the eigenvectors of the electromagnetic energy-momentum tensor).

#### 3.5 General Decomposition Principle

Any symmetric spinor $\phi_{AB\ldots L}$ of valence $n$ (i.e., with $n$ symmetric indices) can be factored:

$$\phi_{AB\ldots L} = \alpha_{(A} \beta_B \cdots \lambda_{L)}$$

into $n$ spinors (not necessarily distinct), unique up to ordering and rescaling. This is the **spinor version of the fundamental theorem of algebra**: a symmetric spinor of rank $n$ is equivalent to a homogeneous polynomial of degree $n$ in two variables, and the factorization corresponds to finding the roots of that polynomial. Each factor $\alpha^A$ defines a **principal null direction**.

---

### 4. Covariant Derivative and Curvature in Spinor Form

#### 4.1 The Spinor Covariant Derivative

The spacetime covariant derivative $\nabla_a$ translates into the spinor derivative:

$$\nabla_a \longleftrightarrow \nabla_{AA'}$$

Acting on spinors, $\nabla_{AA'}$ must satisfy:

$$\nabla_{AA'} \epsilon_{BC} = 0, \qquad \nabla_{AA'} \epsilon_{B'C'} = 0$$

(metricity of the spin connection), and the torsion-free condition. These requirements uniquely determine the spin connection.

#### 4.2 The Curvature Spinors

The Riemann tensor $R_{abcd}$, with its 20 independent components in 4 dimensions, decomposes into three irreducible spinor parts under $\mathrm{SL}(2,\mathbb{C})$:

$$R_{abcd} = R_{ABA'B'CDC'D'}$$

The full decomposition is:

$$\boxed{R_{ABA'B'CDC'D'} = \Psi_{ABCD}\,\epsilon_{A'B'}\epsilon_{C'D'} + \bar{\Psi}_{A'B'C'D'}\,\epsilon_{AB}\epsilon_{CD} + \Phi_{ABC'D'}\,\epsilon_{A'B'}\epsilon_{CD} + \Phi_{CDA'B'}\,\epsilon_{AB}\epsilon_{C'D'} + 2\Lambda\left(\epsilon_{AC}\epsilon_{BD}\epsilon_{A'C'}\epsilon_{B'D'} - \epsilon_{AD}\epsilon_{BC}\epsilon_{A'D'}\epsilon_{B'C'}\right)}$$

where:

| Spinor | Symmetry | Components | Tensor Counterpart |
|--------|----------|------------|-------------------|
| $\Psi_{ABCD} = \Psi_{(ABCD)}$ | Totally symmetric | 5 complex = 10 real | Weyl tensor $C_{abcd}$ |
| $\Phi_{ABA'B'} = \Phi_{(AB)(A'B')} = \bar{\Phi}_{ABA'B'}$ | Hermitian, symmetric in each pair | 9 real | Trace-free Ricci tensor $R_{ab} - \frac{1}{4}Rg_{ab}$ |
| $\Lambda = \frac{R}{24}$ | Scalar | 1 real | Ricci scalar $R$ |

**Total: 10 + 9 + 1 = 20 independent real components**, matching the Riemann tensor.

#### 4.3 The Weyl Spinor $\Psi_{ABCD}$

The **Weyl spinor** $\Psi_{ABCD}$ is the spinor equivalent of the Weyl conformal curvature tensor $C_{abcd}$. It is totally symmetric, $\Psi_{ABCD} = \Psi_{(ABCD)}$, and has 5 complex components. In a spin-frame $(o^A, \iota^A)$, these are the **five Weyl scalars** of the Newman--Penrose formalism:

$$\Psi_0 = \Psi_{ABCD}\, o^A o^B o^C o^D$$
$$\Psi_1 = \Psi_{ABCD}\, o^A o^B o^C \iota^D$$
$$\Psi_2 = \Psi_{ABCD}\, o^A o^B \iota^C \iota^D$$
$$\Psi_3 = \Psi_{ABCD}\, o^A \iota^B \iota^C \iota^D$$
$$\Psi_4 = \Psi_{ABCD}\, \iota^A \iota^B \iota^C \iota^D$$

The Weyl spinor encodes the part of curvature that propagates as gravitational radiation and exists in vacuum ($R_{ab} = 0$ implies $\Phi_{ABA'B'} = 0$ and $\Lambda = 0$, leaving only $\Psi_{ABCD}$).

#### 4.4 The Ricci Spinor $\Phi_{ABA'B'}$

The **Ricci spinor** (or **Ricci--spinor**) encodes the trace-free part of the Ricci tensor:

$$\Phi_{ABA'B'} = \Phi_{(AB)(A'B')}$$

It is Hermitian: $\bar{\Phi}_{ABA'B'} = \Phi_{ABA'B'}$. Its 9 real components correspond to the 9 independent components of the trace-free Ricci tensor $S_{ab} = R_{ab} - \frac{1}{4}Rg_{ab}$.

Through the Einstein field equations $R_{ab} - \frac{1}{2}Rg_{ab} + \Lambda_{\text{cosm}} g_{ab} = 8\pi T_{ab}$, the Ricci spinor is determined by the matter content:

$$\Phi_{ABA'B'} = 4\pi \left( T_{ABA'B'} - \frac{1}{4} T \, \epsilon_{AB} \epsilon_{A'B'} \right)$$

#### 4.5 The Bianchi Identity in Spinor Form

The Bianchi identity $\nabla_{[e} R_{ab]cd} = 0$ becomes, in spinor language:

$$\nabla^{AA'} \Psi_{ABCD} = \nabla_{(B}{}^{A'} \Phi_{CD)A'B'} + \epsilon_{B(C} \nabla_{D)}{}^{A'} \cdot 3\Lambda$$

In vacuum ($\Phi_{ABA'B'} = 0$, $\Lambda = 0$), this reduces to the remarkably simple:

$$\nabla^{AA'} \Psi_{ABCD} = 0$$

This is a **massless free-field equation of spin 2** --- the propagation equation for linearized gravitational waves.

---

### 5. The Petrov Classification

#### 5.1 Principal Spinors and the Classification

By the fundamental theorem of symmetric spinor decomposition ($\S$3.5), the Weyl spinor factors as:

$$\Psi_{ABCD} = \alpha_{(A}\, \beta_B\, \gamma_C\, \delta_{D)}$$

The four spinors $\alpha^A, \beta^A, \gamma^A, \delta^A$ (the **principal spinors**) each define a **principal null direction** (PND) of the gravitational field. The Petrov type is determined by their coincidence pattern:

| Petrov Type | PND Pattern | Canonical Form | Multiplicity |
|-------------|-------------|----------------|-------------|
| **I** (general) | $\{\alpha, \beta, \gamma, \delta\}$ all distinct | $\alpha_{(A}\beta_B\gamma_C\delta_{D)}$ | $(1,1,1,1)$ |
| **II** | Two coincide: $\alpha = \beta$ | $\alpha_{(A}\alpha_B\gamma_C\delta_{D)}$ | $(2,1,1)$ |
| **D** (degenerate) | Two pairs coincide: $\alpha = \beta$, $\gamma = \delta$ | $\alpha_{(A}\alpha_B\gamma_C\gamma_{D)}$ | $(2,2)$ |
| **III** | Three coincide: $\alpha = \beta = \gamma$ | $\alpha_{(A}\alpha_B\alpha_C\delta_{D)}$ | $(3,1)$ |
| **N** (null) | All four coincide: $\alpha = \beta = \gamma = \delta$ | $\alpha_A\alpha_B\alpha_C\alpha_D$ | $(4)$ |
| **O** (conformally flat) | $\Psi_{ABCD} = 0$ | $0$ | --- |

#### 5.2 Algebraic Speciality

A spacetime is **algebraically special** if it is of type II, D, III, N, or O --- equivalently, if the Weyl spinor has a **repeated principal null direction**. The **Goldberg--Sachs theorem** states that in a vacuum spacetime, a null direction $\kappa^A$ is a repeated PND of $\Psi_{ABCD}$ if and only if the associated null congruence $l^a = \kappa^A \bar{\kappa}^{A'}$ is geodesic and shear-free.

#### 5.3 Physical Interpretation

| Type | Gravitational Analogy | Example Spacetime |
|------|----------------------|-------------------|
| I | General tidal field | Generic perturbation |
| II | Longitudinal + transverse radiation | Robinson--Trautman solutions |
| D | Pure Coulomb-type field | Schwarzschild, Kerr, Reissner--Nordstr\"om |
| III | Longitudinal radiation | Special exact solutions |
| N | Transverse null radiation | pp-waves, gravitational plane waves |
| O | No free gravitational field | Friedmann--Lema\^itre--Robertson--Walker |

Type D is the type of all known physically relevant black hole solutions. The Kerr metric has:

$$\Psi_2 \neq 0, \qquad \Psi_0 = \Psi_1 = \Psi_3 = \Psi_4 = 0$$

in a principal null frame, with the two repeated PNDs aligned along the ingoing and outgoing principal null directions.

---

### 6. Massless Free-Field Equations in Spinor Form

#### 6.1 The General Zero-Rest-Mass Equation

A **massless free field of spin $s$** is described by a totally symmetric spinor field $\varphi_{AB\ldots L}$ with $2s$ indices (for $s > 0$), satisfying:

$$\boxed{\nabla^{AA'} \varphi_{AB\ldots L} = 0}$$

This is the **zero-rest-mass (ZRM) free-field equation**. The field has **helicity** $+s$ (or $-s$ for the primed version). Specific cases:

| Spin $s$ | Field | Spinor | Equation | Physical Field |
|----------|-------|--------|----------|---------------|
| $0$ | Scalar | $\varphi$ | $\nabla^{AA'}\nabla_{AA'}\varphi = 0$ | Conformally coupled scalar |
| $\frac{1}{2}$ | Weyl neutrino | $\varphi_A$ | $\nabla^{AA'}\varphi_A = 0$ | Massless Dirac / Weyl field |
| $1$ | Maxwell | $\varphi_{AB}$ | $\nabla^{AA'}\varphi_{AB} = 0$ | Source-free electromagnetic field |
| $\frac{3}{2}$ | Rarita--Schwinger | $\varphi_{ABC}$ | $\nabla^{AA'}\varphi_{ABC} = 0$ | Massless spin-$\frac{3}{2}$ |
| $2$ | Linearized gravity | $\varphi_{ABCD}$ | $\nabla^{AA'}\varphi_{ABCD} = 0$ | Linearized Weyl tensor |

#### 6.2 Source-Free Maxwell Equations

The Maxwell equations $\nabla^a F_{ab} = 0$ and $\nabla_{[a}F_{bc]} = 0$, combined, are equivalent to the single spinor equation:

$$\nabla^{AA'}\varphi_{AB} = 0$$

where $F_{ab} = \varphi_{AB}\epsilon_{A'B'} + \bar{\varphi}_{A'B'}\epsilon_{AB}$. The two real tensor equations collapse into one holomorphic spinor equation --- this is a central demonstration of the economy of the spinor formalism.

#### 6.3 The Massive Dirac Equation

For completeness: the **massive** Dirac equation in 2-spinor form is the coupled system:

$$\nabla^{AA'}\psi_A = \mu \bar{\chi}^{A'}, \qquad \nabla^{AA'}\chi_A = \mu \bar{\psi}^{A'}$$

where $\mu = m/(\sqrt{2}\hbar)$ and $(\psi_A, \chi_A)$ form the two chiral components. In the massless limit $\mu \to 0$, these decouple into independent ZRM equations.

---

### 7. The Newman--Penrose (Spin-Coefficient) Formalism

#### 7.1 Spin Coefficients

Given a spin-frame $(o^A, \iota^A)$ with associated null tetrad $(l^a, n^a, m^a, \bar{m}^a)$, the covariant derivatives of the basis spinors define the **twelve complex spin coefficients**:

$$\nabla_{AA'} o_B = -(\gamma_{AA'B}{}^0)\, o_B + \text{terms with } \iota_B$$

Explicitly, the twelve NP spin coefficients are:

| Symbol | Definition | Symbol | Definition |
|--------|-----------|--------|-----------|
| $\kappa$ | $o^A o^B \nabla_{AA'} o_B \bar{o}^{A'}$ | $\nu$ | $\iota^A \iota^B \nabla_{AA'} \iota_B \bar{\iota}^{A'}$ |
| $\rho$ | $o^A \iota^B \nabla_{AA'} o_B \bar{o}^{A'}$ | $\mu$ | $\iota^A o^B \nabla_{AA'} \iota_B \bar{\iota}^{A'}$ |
| $\sigma$ | $o^A o^B \nabla_{AA'} o_B \bar{\iota}^{A'}$ | $\lambda$ | $\iota^A \iota^B \nabla_{AA'} \iota_B \bar{o}^{A'}$ |
| $\tau$ | $o^A \iota^B \nabla_{AA'} o_B \bar{\iota}^{A'}$ | $\pi$ | $\iota^A o^B \nabla_{AA'} \iota_B \bar{o}^{A'}$ |
| $\varepsilon$ | $\frac{1}{2}(o^A \nabla_{A0'} o_A)$ | $\gamma$ | $\frac{1}{2}(\iota^A \nabla_{A1'} \iota_A)$ |
| $\beta$ | $\frac{1}{2}(o^A \nabla_{A1'} o_A)$ | $\alpha$ | $\frac{1}{2}(\iota^A \nabla_{A0'} \iota_A)$ |

The spin coefficients encode the optical properties of the null congruences:
- $\kappa = 0$: the $l^a$ congruence is geodesic.
- $\rho$: its expansion and twist (divergence and rotation).
- $\sigma$: its shear (distortion of a cross-sectional circle into an ellipse).

#### 7.2 Directional Derivatives

The four NP directional derivative operators are:

$$D = l^a \nabla_a, \quad \Delta = n^a \nabla_a, \quad \delta = m^a \nabla_a, \quad \bar{\delta} = \bar{m}^a \nabla_a$$

The Ricci identities, Bianchi identities, and field equations are then written as a system of first-order PDEs in these operators, with the spin coefficients and Weyl/Ricci scalars as unknowns.

#### 7.3 Compacted Spin-Coefficient (GHP) Formalism

The **Geroch--Held--Penrose (GHP)** formalism is a refinement that retains only spin-coefficient quantities that are covariant under spin-frame rescalings $o^A \mapsto \lambda\, o^A$, $\iota^A \mapsto \lambda^{-1}\iota^A$. Each quantity carries a **GHP type** $(p, q)$ --- its boost weight and spin weight. Only four of the twelve spin coefficients ($\kappa, \sigma, \rho, \tau$ and their primes) are GHP-covariant; the remaining four ($\varepsilon, \beta, \gamma, \alpha$) encode gauge freedom.

---

## Volume 2 --- Spinor and Twistor Methods in Space-Time Geometry

### Chapter Structure

| Ch. | Title |
|-----|-------|
| 6 | Twistors |
| 7 | Null congruences |
| 8 | Classification of curvature tensors |
| 9 | Conformal infinity |
| App. | Spinor-valued differential forms |

---

### 8. Twistor Theory

#### 8.1 The Twistor Equation

In flat (or conformally flat) spacetime, a **twistor** arises as a solution of the **twistor equation** (or Penrose's "equation for local twistors"):

$$\boxed{\nabla_{A'(A}\,\omega_{B)} = 0}$$

Equivalently, writing this out:

$$\nabla_{A'}{}^{(A}\,\omega^{B)} = 0 \qquad \Longleftrightarrow \qquad \nabla_{A'A}\,\omega_B + \nabla_{A'B}\,\omega_A = 0$$

This equation states that the symmetrized derivative of $\omega^A$ vanishes. In Minkowski space, the general solution is:

$$\omega^A = \omega_0^A - i\, x^{AA'}\pi_{A'}$$

where $\omega_0^A$ and $\pi_{A'}$ are constant spinors and $x^{AA'}$ is the position spinor. A **twistor** $Z^\alpha$ is defined as the pair:

$$Z^\alpha = (\omega^A,\, \pi_{A'})$$

with $\alpha = 0, 1, 2, 3$ being a 4-component twistor index. The twistor $Z^\alpha$ lives in **twistor space** $\mathbb{T} \cong \mathbb{C}^4$.

#### 8.2 The Incidence Relation

The fundamental link between twistor space and Minkowski space is the **incidence relation**:

$$\boxed{\omega^A = i\, x^{AA'}\pi_{A'}}$$

Given a twistor $Z^\alpha = (\omega^A, \pi_{A'})$ with $\pi_{A'} \neq 0$, the incidence relation defines a set of spacetime points $x^{AA'}$. Because this is two complex equations for four real unknowns (the position), the solution set is:

- **For a given twistor**: a totally null, self-dual 2-plane ($\alpha$-plane) in complexified Minkowski space $\mathbb{CM}$.
- **Restricted to real Minkowski space**: a null geodesic (a light ray) with specific spinor data attached.

Conversely, a spacetime point $x$ corresponds to a projective line $\mathbb{CP}^1 \subset \mathbb{PT}$ in projective twistor space.

| Object in $\mathbb{M}$ | Corresponds to in $\mathbb{PT}$ |
|------------------------|--------------------------------|
| Point $x^a$ | Line $\mathbb{CP}^1$ |
| Null geodesic | Point $Z^\alpha$ |
| Light cone of $x$ | Line through $Z$ meeting $\mathbb{PN}$ |

#### 8.3 Projective Twistor Space

**Projective twistor space** $\mathbb{PT} = \mathbb{CP}^3$ is obtained from $\mathbb{T} \cong \mathbb{C}^4 \setminus \{0\}$ by identifying:

$$Z^\alpha \sim \lambda Z^\alpha, \qquad \lambda \in \mathbb{C}^*$$

The twistor pseudo-norm (Hermitian inner product of signature $(+,+,-,-)$) is:

$$\Sigma = Z^\alpha \bar{Z}_\alpha = \omega^A \bar{\pi}_A + \bar{\omega}^{A'}\pi_{A'} = 2\,\mathrm{Im}(\omega^A \bar{\pi}_A)$$

This divides projective twistor space into three regions:

| Region | Condition | Spacetime Interpretation |
|--------|-----------|------------------------|
| $\mathbb{PT}^+$ | $\Sigma > 0$ | Positive helicity (right-handed) |
| $\mathbb{PN}$ | $\Sigma = 0$ | Null twistors --- real null geodesics in $\mathbb{M}$ |
| $\mathbb{PT}^-$ | $\Sigma < 0$ | Negative helicity (left-handed) |

#### 8.4 Twistor Inner Product and Dual Twistors

The **dual twistor** $W_\alpha$ transforms under the contragredient representation. For a twistor $Z^\alpha = (\omega^A, \pi_{A'})$, the complex conjugate is a dual twistor:

$$\bar{Z}_\alpha = (\bar{\pi}_{A}, \bar{\omega}^{A'})$$

Note the swap and index adjustment. The twistor inner product is:

$$Z^\alpha \bar{Z}_\alpha = \omega^A \bar{\pi}_A + \bar{\omega}^{A'} \pi_{A'}$$

For two distinct twistors $Z^\alpha$ and $W^\alpha$:

$$Z^\alpha W_\alpha = \omega^A \rho_A + \varpi^{A'}\pi_{A'}$$

where $W^\alpha = (\varpi^A, \rho_{A'})$. This is the natural $\mathrm{SU}(2,2)$-invariant pairing, and $\mathrm{SU}(2,2)$ is the twistor group --- the double cover of the conformal group $\mathrm{SO}(2,4)$ of compactified Minkowski space.

#### 8.5 Massless Fields and the Penrose Transform

Penrose's contour integral formula expresses a massless field of helicity $n/2$ in terms of twistor data. For $n \geq 0$ (positive helicity):

$$\varphi_{A\ldots B}(x) = \frac{1}{2\pi i}\oint \pi_{A'}\cdots\pi_{B'}\, f(Z^\alpha)\, \pi_{C'}\, d\pi^{C'}$$

where $f(Z^\alpha)$ is a holomorphic function on (a region of) twistor space, homogeneous of degree $(-n-2)$. More precisely, $f$ represents a cohomology class in $H^1(\mathbb{PT}, \mathcal{O}(-n-2))$.

This is the **Penrose transform**: it establishes a bijection between:

$$H^1(U \subset \mathbb{PT},\, \mathcal{O}(-n-2)) \quad \longleftrightarrow \quad \text{ZRM fields of helicity } n/2 \text{ on } U' \subset \mathbb{CM}$$

The power of this correspondence is that it converts a system of PDEs (the zero-rest-mass equations) into a problem of complex-analytic geometry (sheaf cohomology on projective space).

#### 8.6 The Infinity Twistor and Conformal Symmetry Breaking

In the full twistor framework, Minkowski space has the conformal group $\mathrm{SU}(2,2)$ as its symmetry group, which acts linearly on twistor space. The selection of a particular Minkowski space (breaking conformal invariance to Poincar\'e invariance) is encoded in the **infinity twistor** $I^{\alpha\beta}$:

$$I^{\alpha\beta} = \begin{pmatrix} \epsilon^{AB} & 0 \\ 0 & 0 \end{pmatrix}$$

The infinity twistor picks out a preferred structure in twistor space that corresponds to the point at infinity in spacetime (or more precisely, the structure of null infinity).

---

### 9. Conformal Infinity and Asymptotic Structure

#### 9.1 Penrose's Conformal Compactification

Penrose and Rindler give a thorough treatment of the conformal boundary of spacetime. One performs a conformal rescaling $\hat{g}_{ab} = \Omega^2 g_{ab}$ where $\Omega \to 0$ at infinity, attaching a boundary that represents "points at infinity." The boundary decomposes into:

- **$\mathscr{I}^+$ (future null infinity, "scri-plus")**: where outgoing light rays end. Topologically $\mathbb{R} \times S^2$.
- **$\mathscr{I}^-$ (past null infinity)**: where incoming light rays originate.
- **$i^0$ (spatial infinity)**: a single point representing $r \to \infty$ at fixed $t$.
- **$i^+$ (future timelike infinity)**: where timelike worldlines end.
- **$i^-$ (past timelike infinity)**: where timelike worldlines begin.

#### 9.2 The Bondi--Sachs Mass

At $\mathscr{I}^+$, the Bondi mass-energy $M_B(u)$ is defined as a 2-surface integral on cross-sections of $\mathscr{I}^+$. In the spinor formalism, the Bondi news function $N$ (encoding outgoing gravitational radiation) is related to the asymptotic shear $\sigma^0$ of outgoing null geodesics:

$$N = \dot{\bar{\sigma}}^0$$

The Bondi mass-loss formula:

$$\frac{dM_B}{du} = -\frac{1}{4\pi}\oint_{S^2} |N|^2 \, dS \leq 0$$

guarantees that the Bondi mass is non-increasing: gravitational radiation always carries positive energy to infinity.

#### 9.3 Peeling Property

Penrose's **peeling theorem** describes the asymptotic falloff of the Weyl spinor along outgoing null geodesics approaching $\mathscr{I}^+$. In an appropriate frame:

$$\Psi_{ABCD} = \frac{\Psi^{(4)}_{ABCD}}{r} + \frac{\Psi^{(3)}_{ABCD}}{r^2} + \frac{\Psi^{(2)}_{ABCD}}{r^3} + \frac{\Psi^{(1)}_{ABCD}}{r^4} + \frac{\Psi^{(0)}_{ABCD}}{r^5} + \mathcal{O}(r^{-6})$$

where $\Psi^{(k)}$ is of Petrov type $\{$N, III, II, I, I$\}$ respectively for $k = 4, 3, 2, 1, 0$. The leading term is always type N, representing transverse radiation --- the gravitational field "peels off" in algebraic type as one moves toward infinity.

---

### 10. Quasi-Local Mass: The Penrose Construction

#### 10.1 Motivation

In general relativity, gravitational energy is notoriously non-local --- there is no local energy density for the gravitational field. Global definitions (ADM mass, Bondi mass) exist at spatial/null infinity, but a physically meaningful definition associated with a finite region --- a **quasi-local mass** --- remained a major open problem.

Penrose's construction (1982) uses twistor theory to define a quasi-local mass-energy associated with any closed spacelike 2-surface $\mathcal{S}$ (topologically $S^2$) in spacetime.

#### 10.2 The 2-Surface Twistor Space

On a general curved spacetime, the twistor equation $\nabla_{A'(A}\omega_{B)} = 0$ has no global solutions. Penrose's idea: restrict to a 2-surface $\mathcal{S}$ and define a **2-surface twistor space** $\mathbb{T}^\alpha(\mathcal{S})$ as the space of solutions of the twistor equation restricted to $\mathcal{S}$.

On a topological 2-sphere in a general spacetime, the 2-surface twistor space is 4-dimensional (matching flat-space twistor space), with each element $Z^\alpha = (\omega^A, \pi_{A'})$ satisfying:

$$\delta\omega^A = i\, \pi^{A'}\delta x_{A'}{}^A$$

along curves on $\mathcal{S}$, where $\delta$ denotes differentiation tangent to $\mathcal{S}$.

#### 10.3 The Kinematic Twistor

The **kinematic twistor** $A_{\alpha\beta}$ is a symmetric twistor defined by a 2-surface integral over $\mathcal{S}$:

$$A_{\alpha\beta}\, Z^\alpha W^\beta = -\frac{1}{4\pi G}\oint_\mathcal{S} \left[\omega^A \varpi^B \Psi_{ABCD}\, \hat{\epsilon}^{CD} + \text{conjugate and Ricci terms}\right] d\mathcal{S}$$

where $Z^\alpha = (\omega^A, \pi_{A'})$ and $W^\beta = (\varpi^A, \rho_{A'})$ are 2-surface twistors, and $\hat{\epsilon}^{CD}$ is the surface area element in spinor form. The integral collects contributions from both the Weyl curvature (free gravitational field) and the Ricci curvature (matter).

In flat space or at infinity, $A_{\alpha\beta}$ encodes the **total 4-momentum $p^{AA'}$** and **angular momentum $M^{AB}, \bar{M}^{A'B'}$** of the system:

$$A_{\alpha\beta} = \begin{pmatrix} M^{AB} & p^{AB'} \\ p^{A'B} & \bar{M}^{A'B'} \end{pmatrix}$$

#### 10.4 The Quasi-Local Mass

The quasi-local mass $m$ is extracted from the kinematic twistor and infinity twistor via:

$$m^2 = \frac{A_{\alpha\beta}\, A_{\gamma\delta}\, I^{\alpha\gamma}\, I^{\beta\delta}}{2\, I^{\alpha\beta}\, I^{\gamma\delta}\, A_{\alpha\gamma}\, \epsilon_{\beta\delta}}$$

or more directly, from the eigenvalues of the kinematic twistor contracted with the infinity twistor. The quantity $p^a p_a = m^2$ corresponds to the squared norm of the total 4-momentum.

#### 10.5 The Contortion Problem

A 2-surface $\mathcal{S}$ is **non-contorted** if its 2-surface twistor space admits a real structure compatible with the spacetime reality conditions (the twistor norm has signature $(+,+,-,-)$ on $\mathbb{T}(\mathcal{S})$). It is **contorted** if the presence of Weyl curvature at $\mathcal{S}$ disrupts this structure.

For non-contorted surfaces, the quasi-local mass is well-defined and agrees with known results:
- At $\mathscr{I}^+$: reproduces the Bondi mass.
- At spatial infinity: reproduces the ADM mass.
- For a sphere in Schwarzschild: gives $m_{\text{Schwarzschild}}$.

For contorted surfaces, the construction encounters difficulties, and the quasi-local mass may not be uniquely defined. This remains an active area of research.

---

### 11. Applications to Exact Solutions

#### 11.1 Schwarzschild Spacetime (Type D)

The Schwarzschild solution in spinor form: the only non-vanishing Weyl scalar is:

$$\Psi_2 = -\frac{M}{r^3}$$

in a principal null frame, confirming Petrov type D. The two repeated PNDs are the ingoing and outgoing radial null directions.

#### 11.2 Kerr Spacetime (Type D)

The Kerr metric is also type D with:

$$\Psi_2 = -\frac{M}{(r - ia\cos\theta)^3}$$

The principal null directions are the Kinnersley tetrad legs, aligned with the repeated principal spinors of $\Psi_{ABCD}$.

#### 11.3 Gravitational Plane Waves (Type N)

For a pp-wave with profile $H(u, \zeta, \bar{\zeta})$:

$$\Psi_4 = \frac{\partial^2 H}{\partial \zeta^2}$$

is the only nonvanishing Weyl scalar, confirming Petrov type N. The single (quadruply-repeated) PND is the wave propagation direction.

#### 11.4 Robinson--Trautman Solutions (Type II)

These are expanding, twist-free, shear-free null congruences. They provide radiative spacetimes that settle down to Schwarzschild, and are generically Petrov type II with one repeated PND.

---

### 12. Key Identities and Formulae: Quick Reference

#### Metric decomposition
$$g_{ab} = \epsilon_{AB}\,\epsilon_{A'B'}$$

#### Null vector decomposition
$$k^{AA'} = \kappa^A \bar{\kappa}^{A'}$$

#### Electromagnetic decomposition
$$F_{ABA'B'} = \varphi_{AB}\,\epsilon_{A'B'} + \bar{\varphi}_{A'B'}\,\epsilon_{AB}$$

#### Curvature decomposition
$$R_{abcd} \longleftrightarrow \Psi_{ABCD} \oplus \Phi_{ABA'B'} \oplus \Lambda$$

#### Einstein equation in spinor form
$$\Phi_{ABA'B'} = 4\pi\left(T_{ABA'B'} - \tfrac{1}{4}T\,\epsilon_{AB}\epsilon_{A'B'}\right), \qquad \Lambda = \frac{R}{24}$$

#### ZRM equation
$$\nabla^{AA'}\varphi_{AB\ldots L} = 0$$

#### Twistor definition
$$Z^\alpha = (\omega^A,\, \pi_{A'}), \qquad \omega^A = ix^{AA'}\pi_{A'}$$

#### Twistor equation
$$\nabla_{A'(A}\,\omega_{B)} = 0$$

#### Twistor pseudo-norm
$$\Sigma = Z^\alpha \bar{Z}_\alpha = \omega^A \bar{\pi}_A + \bar{\omega}^{A'}\pi_{A'}$$

#### Index raising/lowering
$$\psi_A = \psi^B\epsilon_{BA}, \qquad \psi^A = \epsilon^{AB}\psi_B$$

#### Spin-frame normalization
$$o^A\iota_A = 1$$

---

## Notation Conventions Summary

| Symbol | Meaning |
|--------|---------|
| $a, b, c, \ldots$ | Abstract spacetime tensor indices |
| $A, B, C, \ldots$ | Unprimed (left-handed) spinor indices, values $\{0, 1\}$ |
| $A', B', C', \ldots$ | Primed (right-handed) spinor indices, values $\{0', 1'\}$ |
| $\alpha, \beta, \gamma, \ldots$ | Twistor indices, values $\{0, 1, 2, 3\}$ |
| $\epsilon_{AB}$ | Spinor metric (Levi-Civita on spin-space) |
| $\nabla_{AA'}$ | Spinor covariant derivative |
| $\Psi_{ABCD}$ | Weyl spinor (5 complex components) |
| $\Phi_{ABA'B'}$ | Ricci spinor (trace-free, 9 real components) |
| $\Lambda$ | Curvature scalar $= R/24$ |
| $o^A, \iota^A$ | Spin-frame (dyad) |
| $l^a, n^a, m^a, \bar{m}^a$ | Newman--Penrose null tetrad |
| $Z^\alpha = (\omega^A, \pi_{A'})$ | Twistor |
| $\mathbb{T}$ | Twistor space $\cong \mathbb{C}^4$ |
| $\mathbb{PT}$ | Projective twistor space $\cong \mathbb{CP}^3$ |
| $\mathscr{I}^{\pm}$ | Future/past null infinity |

---

## References

- Penrose, R. & Rindler, W. (1984). *Spinors and Space-Time, Vol. 1: Two-Spinor Calculus and Relativistic Fields.* Cambridge University Press.
- Penrose, R. & Rindler, W. (1986). *Spinors and Space-Time, Vol. 2: Spinor and Twistor Methods in Space-Time Geometry.* Cambridge University Press.
- Newman, E. T. & Penrose, R. (1962). "An approach to gravitational radiation by a method of spin coefficients." *J. Math. Phys.* **3**, 566--578.
- Geroch, R., Held, A. & Penrose, R. (1973). "A space-time calculus based on pairs of null directions." *J. Math. Phys.* **14**, 874--881.
- Penrose, R. (1982). "Quasi-local mass and angular momentum in general relativity." *Proc. R. Soc. Lond. A* **381**, 53--63.
- Penrose, R. (1967). "Twistor algebra." *J. Math. Phys.* **8**, 345--366.
