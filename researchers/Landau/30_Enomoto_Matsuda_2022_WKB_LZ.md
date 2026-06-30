# The Exact WKB and the Landau-Zener transition for asymmetry in cosmological particle production

**Author(s):** Seishi Enomoto, Tomohiro Matsuda
**Year:** 2022 (v3: 8 Feb 2022)
**Journal:** [INCOMPLETE - not extractable from PDF]
**arXiv:** 2104.02312
**Relevance:** HIGH

---

## Abstract

Cosmological particle production by a time-dependent scalar field is common in cosmology. We focus on the mechanism of asymmetry production when interaction explicitly violates symmetry and its motion is rapid enough to create particles by itself. Combining the exact WKB analysis and the Landau-Zener transition, we point out that perturbation before the non-perturbative analysis may drastically change the structure of the Stokes lines of the theory. The Exact WKB can play an important role in avoiding such discrepancies.

---

## Key Arguments and Derivations

### 1. Setup: Particle Production via Time-Dependent Interactions

The paper begins with bosonic preheating from the action:
$$S_0 = \int d^4x \sqrt{-g}\left[\partial_\mu\phi^*\partial^\mu\phi - m^2|\phi|^2 + \xi R|\phi|^2\right]$$

Using conformal time $\eta$ and the field redefinition $\chi = a\phi$, the action simplifies to:
$$S_0 = \int d^4x\left[|\dot{\chi}|^2 - \omega^2|\chi|^2\right]$$
where $\omega^2 = a^2 m^2 + (-\Delta + \frac{\ddot{a}}{a}(6\xi - 1))$.

The Bogoliubov coefficients $\alpha$ and $\beta$ encode particle production. A constant chemical potential $\mu_\chi$ does NOT generate asymmetry -- the evolution of $|\beta_h|^2$ and $|\beta_g|^2$ are identical. A time-dependent chemical potential ($\dot{\mu} \neq 0$) is required for asymmetry production.

### 2. The Landau-Zener Model and Cosmological Particle Production (Section I.A)

The original Landau-Zener model:
$$i\hbar\frac{d}{dt}\begin{pmatrix}\psi_1\\\psi_2\end{pmatrix} = \begin{pmatrix}-\frac{v}{2}t & \Delta\\\Delta & +\frac{v}{2}t\end{pmatrix}\begin{pmatrix}\psi_1\\\psi_2\end{pmatrix}$$

decouples into Weber equations. The transfer matrix (omitting phases) is:
$$\begin{pmatrix}\psi_1^+\\\psi_2^+\end{pmatrix} = \begin{pmatrix}e^{-\pi\kappa} & \sqrt{1-e^{-2\pi\kappa}}\\\sqrt{1-e^{-2\pi\kappa}} & e^{-\pi\kappa}\end{pmatrix}\begin{pmatrix}\psi_1^-\\\psi_2^-\end{pmatrix}$$

where $\kappa = \Delta^2/v$. For the adiabatic states (diagonalizing the Hamiltonian), the transfer matrix gives the Bogoliubov transformation directly, with $|\beta|^2 = e^{-2\pi\kappa}$ being the particle production probability.

### 3. Exact WKB (EWKB) Formalism

The EWKB introduces a large parameter $\eta = \hbar^{-1}$ and writes the Schrodinger equation as:
$$\left[-\frac{d^2}{dx^2} + \eta^2 Q(x)\right]\psi(x,\eta) = 0$$

For the Landau-Zener model:
$$Q_0(x) = \Delta^2 + \frac{1}{4}v^2 t^2$$

The Stokes lines are determined solely by $Q_0$. The key structural insight is that $\psi_1$ and $\psi_2$ share the same Stokes lines despite having different sub-leading corrections. This maps to the quantum scattering problem with inverted quadratic potential $V = -\frac{1}{4}v^2 x^2$ and energy $E = \Delta^2$.

### 4. Asymmetry from Time-Dependent Off-Diagonal Elements (Section II)

For Majorana fermions with time-dependent mass $m_R(t)$, the equation of motion takes the form:
$$i\hbar\frac{d}{dt}\begin{pmatrix}X\\Y\end{pmatrix} = \begin{pmatrix}D(t) & \Delta(t)^*\\\Delta(t) & -D(t)\end{pmatrix}\begin{pmatrix}X\\Y\end{pmatrix}$$

The decoupled equations yield EWKB forms where the Stokes lines of the leading order $Q_0 = (|{\Delta}|^2 + D^2)/\hbar^2$ cannot generate asymmetry. Asymmetry arises from the sub-leading terms proportional to $\dot{\Delta}/\Delta$.

**Constant rotation** ($\Delta(t) = Ae^{2i\omega_0 t}$): Creates resonance when rotation frequency matches the level spacing $2\omega_0$. The transformation of Eq. (47) shifts both states to create degenerate pairs ($\hat{D} = 0$), enabling particle production.

**Inverse rotation** ($\Delta(t) = Ae^{-2i\omega_0 t}$): Ruins the resonance. The two states are shifted apart ($\hat{D} = 4\omega_0$), suppressing particle production.

This directional asymmetry (rotation vs. inverse rotation) is the origin of asymmetric particle production.

### 5. Perturbation Destroys Stokes Line Structure

A central warning of the paper: perturbative expansion before non-perturbative (EWKB) analysis can drastically change the Stokes line structure. The symmetry-violating interaction requires multiple coupled fields, whose Stokes lines differ from any single-field truncation. Previous approaches that used perturbative expansion to reduce multi-component equations to solvable single-field forms may give qualitatively wrong results for the asymmetry.

### 6. Connection to Schwinger Mechanism

The paper draws connections between the Landau-Zener transition and the Schwinger mechanism for pair creation in strong fields. Both share the WKB tunneling integral structure with $|\beta|^2 \sim e^{-2\pi\kappa}$ where $\kappa$ involves the ratio of a gap (or mass) squared to a "velocity" (or field strength).

## Key Results

1. A constant chemical potential does not generate particle-antiparticle asymmetry in non-perturbative production; a time-dependent $\mu$ (or time-dependent off-diagonal elements) is required.
2. The Landau-Zener transfer matrix provides the Bogoliubov transformation for cosmological particle production, with $|\beta|^2 = e^{-2\pi\kappa}$ ($\kappa = \Delta^2/v$).
3. The EWKB Stokes lines are determined by the leading-order potential $Q_0 = \Delta^2 + \frac{1}{4}v^2 t^2$ and are identical for particle and antiparticle sectors at leading order.
4. Asymmetry arises from sub-leading corrections involving $\dot{\Delta}/\Delta$, i.e., the time-dependence of the off-diagonal (symmetry-violating) interaction.
5. Perturbative expansion before non-perturbative analysis can destroy the Stokes line structure and give qualitatively wrong asymmetry predictions.
6. Rotational direction of the off-diagonal element determines particle vs. antiparticle production -- resonance occurs only when rotation matches the level splitting.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Bosonic preheating action | $S_0 = \int d^4x[\|\dot{\chi}\|^2 - \omega^2\|\chi\|^2]$ | Eq. (2) |
| Frequency | $\omega^2 = a^2 m^2 + (-\Delta_{\text{Lap}} + \frac{\ddot{a}}{a}(6\xi-1))$ | Eq. (3) |
| Landau-Zener Hamiltonian | $H = \begin{pmatrix}-vt/2 & \Delta\\\Delta & vt/2\end{pmatrix}$ | Eq. (18) |
| EWKB form | $[-d^2/dx^2 + \eta^2 Q(x)]\psi = 0$ | Eq. (21) |
| Stokes line potential | $Q_0(x) = \Delta^2 + \frac{1}{4}v^2 t^2$ | Eq. (24) |
| Adiabatic parameter | $\kappa = \Delta^2/v$ | Eq. (32) |
| LZ transition probability | $P = e^{-2\pi\kappa} = e^{-2\pi\Delta^2/v}$ | Eq. (31)/(34) |
| Adiabatic energies | $E_\pm = \pm\sqrt{\Delta^2 + v^2 t^2/4}$ | Eq. (33) |
| General 2-level system | $i\hbar\dot{\Psi} = \begin{pmatrix}D(t) & \Delta^*(t)\\\Delta(t) & -D(t)\end{pmatrix}\Psi$ | Eq. (44) |
| Decoupled EWKB (X) | $\ddot{\hat{X}} + \left(\frac{-iD\dot{\Delta}^*}{\hbar\Delta^*} + \frac{i\dot{D}}{\hbar} + \frac{|\Delta|^2+D^2}{\hbar^2} + \frac{\ddot{\Delta}^*}{2\Delta^*} - \frac{3(\dot{\Delta}^*)^2}{4(\Delta^*)^2}\right)\hat{X} = 0$ | Eq. (50) |
| Trivial Stokes equation | $\ddot{\hat{X}} + \frac{|\Delta|^2 + D^2}{\hbar^2}\hat{X} = 0$ | Eq. (52) |

## Relevance to Phonon-Exflation

This paper provides the mathematical machinery connecting the Landau-Zener transition to cosmological particle creation, which is central to the Schwinger-instanton duality identified in Session 38. The result $S_{\text{Schwinger}}(0.070) \approx S_{\text{inst}}(0.069)$ found in the framework is precisely the WKB tunneling integral $\kappa = \Delta^2/v$ computed here. The paper's demonstration that asymmetry requires time-dependent off-diagonal elements (not just a chemical potential) maps onto the framework's finding that the transit dynamics (not the static BCS ground state) generates the particle spectrum. The warning about perturbation destroying Stokes line structure is directly relevant to the framework's careful treatment of the instanton gas as a non-perturbative object.
