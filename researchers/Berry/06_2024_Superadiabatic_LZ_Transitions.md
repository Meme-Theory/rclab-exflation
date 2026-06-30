# Partial Landau-Zener transitions and applications to qubit shuttling

**Author(s):** Jonas R. F. Lima, Guido Burkard
**Year:** 2024
**Journal:** [not stated in PDF; preprint]
**arXiv:** 2408.03173
**Relevance:** HIGH

---

## Abstract

The transition dynamics of two-state systems with time-dependent energy levels, first considered by Landau, Zener, Majorana, and Stuckelberg, is one of the basic models in quantum physics and has been used to describe various physical systems. We propose here a generalization of the Landau-Zener (LZ) problem characterized by distinct paths of the instantaneous eigenstates as the system evolves in time while keeping the instantaneous eigenenergies exactly as in the standard LZ model. We show that these paths play an essential role in the transition probability P between the two states, and can lead to a substantial reduction of P, being possible even to achieve P = 0 in an instructive extreme case, and also to large P even in the absence of any anticrossing point. The partial LZ model can describe valley transition dynamics during charge and spin shuttling in semiconductor quantum dots.

---

## Key Arguments and Derivations

### Standard LZ Model and Its Limitation

The standard LZ model has H = -r . sigma with r = (Delta_0/2, 0, alpha*t/2), giving a straight-line Hamiltonian curve in the xz plane. The transition probability is the celebrated LZ formula P_LZ = exp(-2*pi*Delta_0^2 / hbar*alpha). The key insight of this paper is that the LZ formula depends ONLY on the eigenvalues (energy gap and level velocity), but different Hamiltonian curves in the xz plane -- keeping the same eigenvalues -- produce fundamentally different transition probabilities.

### Generalized (Partial) LZ Model

The authors construct a Hamiltonian with the same instantaneous eigenvalues E_pm = pm Omega_alpha/2 (where Omega_alpha = sqrt(Delta_0^2 + alpha^2 t^2)) but with new instantaneous eigenvectors parametrized by a second parameter beta:

|psi_pm> = C_pm(t) (alpha*t -/+ Omega_alpha, -/+beta*t + Omega_beta)^T

where Omega_beta = sqrt(Delta_0^2 + beta^2 t^2). This produces the Hamiltonian (Eq. 2) which reduces to the standard LZ model for beta = 0 but traces a hyperbolic curve in the xz plane for 0 < beta < alpha.

### The Superadiabatic Regime

The central discovery: for 0 < beta < ~2*alpha, the transition probability P is LESS than P_LZ -- the superadiabatic regime. At beta = alpha, P = 0 unconditionally (regardless of driving velocity and energy gap). The system is unconditionally adiabatic because the Hamiltonian curve is a straight back-and-forth trajectory on the positive x-axis (z = 0, theta identically 0).

The modified adiabaticity condition is Delta_0^2 / hbar|alpha - beta| >> 1, which is weaker than the standard condition Delta_0^2 / hbar*alpha >> 1 when beta is between 0 and 2*alpha.

### Role of the Angle theta and Bloch Sphere Rotation

The angle theta(t) = arctan[((alpha*Omega_beta - beta*Omega_alpha)*t) / Delta_0^2] in the xz plane governs transitions. The angular velocity at the crossing point, theta_dot(0) = |alpha - beta|/Delta_0, determines adiabaticity. For beta = alpha, theta_dot(0) = 0 and the eigenvectors do not rotate -- hence no transition. For beta <= 0, the eigenvectors trace a closed circle on the Bloch sphere; for beta > 0, an open path.

The transition probability is symmetric under interchange of alpha and beta, which means the case alpha = 0, beta > 0 (constant eigenvalues, no anticrossing) gives P = P_LZ with beta replacing alpha. This proves that LZ transitions can occur without any avoided crossing, purely from eigenvector rotation in the Bloch sphere.

### Failure of the DDP Formula

The Dykhne-Davis-Pechukas (DDP) formula fails for this model because the function E(t) = sqrt(z^2(t) + x^2(t)) is the same as in the standard LZ case, so DDP predicts P = P_LZ regardless of beta. The failure arises because the zero t_c = i*Delta_0/alpha of E(t) also yields H(t_c) = 0.

### Approximations

For beta > 0, the Demkov-Kunike model (z(t) = a*tanh(bt)) provides a good approximation. For beta <= 0, the superlinear LZ model gives a fair approximation via DDP.

### Application to Electron Shuttling

For valley transitions during electron spin shuttling in Si/SiGe quantum dots, the valley Hamiltonian has both real and imaginary parts of the intervalley coupling varying in time, producing non-LZ Hamiltonian curves. Using the angular velocity criterion, the authors show that tuning shuttling velocity to limit theta_dot <= 10^8 rad/s achieves shuttling fidelity exceeding 99.99% at average velocity 0.5 m/s -- a drastic improvement over standard LZ-based strategies.

## Key Results

1. Different Hamiltonian curves in the xz plane produce different transition probabilities even with identical eigenvalue landscapes.
2. A superadiabatic regime exists for 0 < beta < ~2*alpha where P < P_LZ.
3. At beta = alpha, the system is unconditionally adiabatic: P = 0 regardless of energy gap and driving speed.
4. LZ transitions can occur without any avoided crossing (alpha = 0 case), purely from eigenvector rotation.
5. The DDP formula fails for this model, calling into question its general validity.
6. P is symmetric under interchange of alpha and beta.
7. Shuttling fidelity exceeding 99.99% is achievable by controlling angular velocity rather than linear velocity.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| LZ formula | $P_{LZ} = \exp(-2\pi\Delta_0^2/\hbar\alpha)$ | Sec. I |
| Generalized eigenvectors | $\mid\psi_\pm\rangle = C_\pm(t)\left(\alpha t \mp \Omega_\alpha,\;\mp\beta t + \Omega_\beta\right)^T$ | Eq. (1) |
| Generalized Hamiltonian | $H = \frac{-\Omega_\alpha}{2(\Omega_\alpha\Omega_\beta - \alpha\beta t^2)}\begin{pmatrix}(\alpha\Omega_\beta - \beta\Omega_\alpha)t & \Delta_0^2 \\ \Delta_0^2 & (\beta\Omega_\alpha - \alpha\Omega_\beta)t\end{pmatrix}$ | Eq. (2) |
| Angle in xz plane | $\theta(t) = \arctan\left(\frac{(\alpha\Omega_\beta - \beta\Omega_\alpha)t}{\Delta_0^2}\right)$ | Eq. (3) |
| Demkov-Kunike approximation | $P_{DK} \approx \frac{\sinh^2(\pi a/b)}{\sinh^2(\pi\sqrt{a^2 + \Delta_0^2}/b)}$ | Eq. (4) |
| Superlinear LZ approximation | $P_{SL} \approx e^{-\pi\frac{\Delta_0^2}{2(\alpha - \beta)}}$ | Eq. (5) |
| Intervalley coupling | $\Delta(\mathbf{r}) = C_0\int e^{-2ik_0 z}U(x,y,z)\mid\Psi_{x,y,z}(\mathbf{r})\mid^2 d^3x$ | Eq. (A3) |
| Valley splitting | $E_{VS}(\mathbf{r}) = 2\mid\Delta(\mathbf{r})\mid$ | Eq. (A4) |
| Valley Hamiltonian | $H = \begin{pmatrix}0 & \Delta(\mathbf{r}) \\ \Delta(\mathbf{r})^* & 0\end{pmatrix}$ | Eq. (B1) |
| Valley eigenstates | $\alpha_\pm(\mathbf{r}) = \frac{1}{\sqrt{2}}\begin{pmatrix}e^{i\theta(\mathbf{r})/2} \\ \pm e^{-i\theta(\mathbf{r})/2}\end{pmatrix}$ | Eq. (B2) |
| Modified adiabaticity condition | $\Delta_0^2/\hbar\mid\alpha - \beta\mid \gg 1$ | Sec. III |
| Angular velocity at crossing | $\dot{\theta}(0) = \mid\alpha - \beta\mid/\Delta_0$ | Sec. III |

## Relevance to Phonon-Exflation

This paper directly addresses how the geometry of the Hamiltonian curve -- not just the energy landscape -- determines transit probabilities. In the phonon-exflation framework, the Dirac operator on M4 x SU(3) traces a path through parameter space as tau evolves, and the transit between topological sectors is governed by exactly this type of non-standard Landau-Zener physics. The superadiabatic regime (P = 0 at beta = alpha) provides a mechanism for the Ordered Veil: if the fiber's geometric parameters are tuned such that the effective beta matches the effective alpha, the system remains adiabatic even during fast transit, naturally suppressing excitations. The proof that transitions arise from eigenvector rotation rather than energy-level crossings directly parallels the framework's emphasis on holonomy (geometric phase) over dynamical phase in determining the fate of the transit.
