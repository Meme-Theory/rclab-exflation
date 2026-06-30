# Mathematical Formulation of the Quantum Theory of Electromagnetic Interaction

- **Author**: R. P. Feynman
- **Year**: 1950
- **Journal**: Physical Review **80**, 440-457
- **DOI**: 10.1103/PhysRev.80.440
- **Received**: June 8, 1950
- **Relevance**: CRITICAL — introduces the proper-time (fifth-parameter) representation of the Klein-Gordon propagator that is the historical root of the heat-kernel / Schwinger proper-time / spectral-action formalism used throughout this project.

## Abstract (verbatim)

> The validity of the rules given in previous papers for the solution of problems in quantum electrodynamics is established. Starting with Fermi's formulation of the field as a set of harmonic oscillators, the effect of the oscillators is integrated out in the Lagrangian form of quantum mechanics. There results an expression for the effect of all virtual photons valid to all orders in e^2/hbar c. It is shown that evaluation of this expression as a power series in e^2/hbar c gives just the terms expected by the aforementioned rules.
>
> In addition, a relation is established between the amplitude for a given process in an arbitrary unquantized potential and in a quantum electrodynamical field. This relation permits a simple general statement of the laws of quantum electrodynamics.
>
> A description, in Lagrangian quantum-mechanical form, of particles satisfying the Klein-Gordon equation is given in an Appendix. It involves the use of an extra parameter analogous to proper time to describe the trajectory of the particle in four dimensions.
>
> A second Appendix discusses in the special case of photons, the problem of finding what real processes are implied by the formula for virtual processes.
>
> Problems of the divergences of electrodynamics are not discussed.

## Key Arguments

1. **Oscillator elimination via path integral**. Starting from Fermi's expansion of the transverse EM field as a set of independent harmonic oscillators (coordinate q_K, conjugate to each mode K), each coupled linearly to a source gamma(t) built from particle coordinates (L_I = sum_n e_n dot-x_n . A^tr(x_n)), the paper integrates out the oscillators exactly in the Lagrangian (path-integral) form of QM. The key identity is the ground-state-to-ground-state amplitude of a driven oscillator G_00, evaluated via Gaussian path integration.

2. **Complex action as self-interaction kernel**. Integrating out each oscillator produces a *complex* effective action I = (i/4w) int int exp(-iw|t-s|) gamma(s) gamma(t) ds dt. Summing over all K modes, with polarization sums, gives the total action R (Eq. 24) — a bi-local self-interaction mediated by d+((t-s)^2 - (x_n - x_m)^2), the Feynman propagator in position space.

3. **Cancellation of Coulomb term**. The longitudinal Coulomb interaction S_c is exactly cancelled by the t=s discontinuity term I_c arising from integration-by-parts on the (K . dot-x)(K . dot-x) piece, leaving only the relativistically-invariant delta_+ kernel. This is the origin of Lorentz-invariance emerging from a non-manifestly-covariant Hamiltonian starting point.

4. **Generating-functional viewpoint (Sec. 7–8)**. Define T_{e^2}[B] as the amplitude for the particle system in external potential B_mu including all virtual photon effects. Feynman shows
   T_{e^2}[B] = exp[ -(i e^2/2) int int (delta/delta B_mu(1))(delta/delta B^mu(2)) d+(s_{12}^2) d tau_1 d tau_2 ] T_0[B],
   a compact all-orders statement of QED. Eqs. (46)-(48) "constitute a compact statement of all the laws of quantum electrodynamics."

5. **Real photons from virtual (Appendix B)**. Real-photon emission/absorption amplitudes are recovered as functional derivatives delta T_{e^2}[B] / delta B_mu(1) contracted with a classical plane wave A^PH. Bose statistics and the 1/n! combinatorial weights emerge naturally from the power-series expansion of exp(iR_{ac}).

6. **Proper-time formulation of Klein-Gordon (Appendix A)**. The Klein-Gordon equation (i d_mu - A_mu)^2 psi = m^2 psi is rewritten as a *five-dimensional* Schrödinger-like equation i d phi/d u = -(1/2)(i d_mu - A_mu)^2 phi, where u is a fifth parameter "analogous to proper time." A path integral over trajectories x_mu(u) in 4D with Lagrangian (1/2)(dx/du)^2 + (dx/du).A(x) gives the amplitude, and the Klein-Gordon Green function is recovered by integrating against exp(-i m^2 u/2):
   2i I_+(x,x') = int_0^infty d u_0 k^(0)(x, u_0; x', 0) exp(-i m^2 u_0 / 2).
   This is the first published proper-time (Schwinger-parameter) representation of the propagator and the direct ancestor of the heat-kernel representation used by Connes, DeWitt, and the spectral action.

## Key Results

- Exact elimination of transverse EM oscillators yields the complex action R (Eq. 24) containing all virtual-photon effects to all orders in e^2/hbar c.
- Cancellation I_{tr} = R - I_c + I_{transient} with I_c = -S_c (exact Coulomb cancellation) and I_{transient} → 0 adiabatically.
- All-orders generating functional T_{e^2}[B] (Eq. 54) — a closed-form non-perturbative statement of QED.
- Appendix A: Klein-Gordon propagator as proper-time integral of a free 4D kernel (Eqs. A8-A9), with automatic antiparticle (positron) interpretation via time-reversed trajectories (u integration from 0 to infinity only).
- Appendix A: fully self-interacting Klein-Gordon amplitude (Eq. A13) as a single exponential of proper-time action plus bi-local delta_+ self-interaction.
- Appendix B: Bose statistics and photon-number combinatorics derived from the structure of exp(i R_{ac}).

## Key Equations

1. **Driven-oscillator ground-state amplitude** (Eq. 14):

$$G_{00} = \exp\!\left[-\frac{1}{4\omega}\int_{-\infty}^{\infty}\!\!\int_{-\infty}^{\infty}\! e^{-i\omega|t-s|}\,\gamma(t)\gamma(s)\,dt\,ds\right]$$

2. **Complex self-action from one oscillator** (Eq. 15):

$$I = \frac{i}{4\omega}\int\!\!\int e^{-i\omega|t-s|}\,\gamma(s)\gamma(t)\,ds\,dt$$

3. **Delta-plus function** (Eq. 22-23, defines the Feynman propagator in position space):

$$\int_0^\infty e^{-ikx}\,dk = -i x^{-1} + \pi\,\delta(x) \equiv \pi\,\delta_+(x), \qquad J = -\tfrac{1}{2}\,i\,\delta_+(t^2 - r^2)$$

4. **All-orders virtual-photon action** (Eq. 24):

$$R = -\frac{1}{2}\sum_{n,m}\int\!\!\int e_n e_m\,(1 - \dot x_n(t)\!\cdot\!\dot x_m(s))\,\delta_+\!\big((t-s)^2 - (x_n(t)-x_m(s))^2\big)\,dt\,ds$$

5. **Generating functional for QED** (Eq. 54):

$$T_{e^2}[B] = \exp\!\left[-\frac{i e^2}{2}\int\!\!\int j_\mu(1)\,j^\mu(2)\,\delta_+(s_{12}^2)\,d\tau_1 d\tau_2\right]\cdot\exp\!\left[-i\int j_\nu(1)B^\nu(1)\,d\tau_1\right]$$

6. **Klein-Gordon proper-time equation** (Eq. A2):

$$i\,\frac{\partial\varphi}{\partial u} = -\frac{1}{2}(i\partial_\mu - A_\mu)^2\,\varphi$$

7. **Proper-time projection onto mass shell** (Eq. A3):

$$\psi(x) = \int_{-\infty}^{\infty} e^{-i m^2 u/2}\,\varphi(x,u)\,du$$

8. **Free KG kernel** (Eq. A8):

$$k^{(0)}(x,u_0;x',0) = (4\pi^2 u_0^2 i)^{-1}\exp\!\left[-\frac{i(x_\mu - x'_\mu)^2}{2 u_0}\right]$$

9. **Feynman propagator as proper-time integral** (Eq. A9):

$$2 i\,I_+(x,x') = \int_0^\infty\! \frac{du_0}{4\pi^2 u_0^2 i}\exp\!\left[-\frac{i}{2}\!\left(m^2 u_0 + \frac{(x-x')^2}{u_0}\right)\right]$$

10. **Classical action along 4D trajectory** (Eq. A6):

$$S = -\int_0^{u_0}\!\left[\frac{1}{2}\!\left(\frac{dx_\mu}{du}\right)^{\!2} + \frac{dx_\mu}{du}A^\mu(x)\right] du$$

11. **Self-interacting Klein-Gordon amplitude** (Eq. A13):

$$\exp\!\left\{-i\!\int_0^{u_0}\!\!\left[\frac{1}{2}\dot x^2 + \dot x\!\cdot\! B\right]du - \frac{i e^2}{2}\!\int_0^{u_0}\!\!\int_0^{u_0}\!\! \dot x_\mu(u)\dot x^\mu(u')\,\delta_+((x(u)-x(u'))^2)\,du\,du'\right\}$$

## Relevance to Phonon-Exflation

1. **Proper-time = heat-kernel bridge**. Eq. (A9) is the Lorentzian analog of the heat-kernel representation of a propagator, G(x,x') = int_0^infty ds <x| e^{-s(D^2 + m^2)} |x'>. Wick-rotating u_0 → -i s gives exactly the Seeley-DeWitt heat-kernel integrand used in the spectral action Tr f(D_K^2/Lambda^2). Feynman's fifth parameter u IS the Schwinger proper-time parameter that becomes the heat-kernel "time" in Connes' construction. The project's spectral action moments a_0, a_2, a_4 are coefficients in the small-u expansion of exactly this integrand, evaluated on the Jensen-deformed SU(3) Dirac operator instead of the free KG kernel.

2. **Feynman parameters / delta_+ propagator**. Eq. (24) exhibits the bi-local delta_+ kernel that, upon Wick rotation, becomes 1/(k^2 + m^2) and underlies all Feynman-parameter loop-integral tricks. The project's one-loop computations on D_K eigenvalues (e.g., pending zeta-regularized effective action Gamma[tau]) are the eigenvalue-sum analogs of Feynman-parameter integrals — same combinatorial structure, discrete spectrum in place of continuous momentum.

3. **Action-first methodology**. The paper's pedagogical arc — write the Lagrangian, eliminate gauge fields by Gaussian integration, obtain an effective bi-local action, expand to read off Feynman rules — is precisely the methodology the Feynman-Theorist agent applies to candidate frameworks (Step 1 of the Feynman Test: "write the action"). The project's post-transit EFT (S55, 8-mode Lagrangian with V_kl) is constructed in the same spirit.

4. **Classical limit and stationary phase**. The emergence of classical trajectories from the stationary-phase condition on S_p + R (the extremal path y=0 argument in footnote 7) is the template for how the GPE simulation's classical field equations emerge as the saddle point of a path integral over phonon-field configurations — what Bogoliubov corrections then add are the y-quadratic fluctuations Feynman keeps track of here.

5. **Positron-as-time-reversed trajectory**. The integration u_0: 0 → infinity in Eq. (A9), automatically producing the Feynman pole prescription 1/(p^2 - m^2 + i epsilon), is the same mechanism that in the project's CP-shield arguments (Majorana/[J,D_K]=0) enforces the particle-antiparticle structure via the KO-dimension-6 sign pattern of the real-structure J. The proper-time integral's restriction to positive u_0 is the Lorentzian root of what becomes a KO-dimension statement in the NCG framework.
