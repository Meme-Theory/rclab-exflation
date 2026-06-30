# Space-Time Approach to Quantum Electrodynamics

- **Author**: R. P. Feynman (Department of Physics, Cornell University, Ithaca, New York)
- **Year**: 1949
- **Journal**: Physical Review, Vol. 76, Number 6, September 15, 1949, pp. 769–789
- **DOI**: 10.1103/PhysRev.76.769
- **Relevance**: CRITICAL

---

## Abstract (verbatim)

> In this paper two things are done. (1) It is shown that a considerable simplification can be attained in writing down matrix elements for complex processes in electrodynamics. Further, a physical point of view is available which permits them to be written down directly for any specific problem. Being simply a restatement of conventional electrodynamics, however, the matrix elements diverge for complex processes. (2) Electrodynamics is modified by altering the interaction of electrons at short distances. All matrix elements are now finite, with the exception of those relating to problems of vacuum polarization. The latter are evaluated in a manner suggested by Pauli and Bethe, which gives finite results for these matrices also. The only effects sensitive to the modification are changes in mass and charge of the electrons. Such changes could not be directly observed. Phenomena directly observable are insensitive to the details of the modification used (except at extreme energies). For such phenomena, a limit can be taken as the range of the modification goes to zero. The results then agree with those of Schwinger. A complete, unambiguous, and presumably consistent, method is therefore available for the calculation of all processes involving electrons and photons.
>
> The simplification in writing the expressions results from an emphasis on the over-all space-time view resulting from a study of the solution of the equations of electrodynamics. The relation of this to the more conventional Hamiltonian point of view is discussed. It would be very difficult to make the modification which is proposed if one insisted on having the equations in Hamiltonian form.
>
> The methods apply as well to charges obeying the Klein-Gordon equation, and to the various meson theories of nuclear forces. Illustrative examples are given. Although a modification like that used in electrodynamics can make all matrices finite for all of the meson theories, for some of the theories it is no longer true that all directly observable phenomena are insensitive to the details of the modification used.
>
> The actual evaluation of integrals appearing in the matrix elements may be facilitated, in the simpler cases, by methods described in the appendix.

---

## Key Arguments

### 1. Space-Time View vs. Hamiltonian Method (Section 1)

Feynman argues that electrodynamics admits two complementary descriptions: field theory (Maxwell) and direct-interaction-at-a-distance between charges (Liénard-Wiechert). The Hamiltonian formulation is ill-suited to delayed interactions because it "represents the future as developing out of the present" and therefore forces introduction of field oscillator coordinates to remember the past. For virtual-quantum problems (close collisions, self-action) the interaction view is more natural: treat the whole process space-time globally rather than instant-by-instant. Relativistic invariance is then manifest, since different Lorentz observers slice the present differently but agree on the global solution.

### 2. The Fundamental Interaction (Section 2)

Starting from two-particle Schrödinger amplitudes $K(3,4;1,2)$, Feynman promotes the instantaneous Coulomb potential $e^2/r_{56}\delta(t_{56})$ to a retarded propagator $\delta_+(s_{56}^2)$ where $s_{56}^2 = t_{56}^2 - r_{56}^2$ is the invariant interval. The positive-frequency prescription $\delta_+(x) = \int_0^\infty e^{-i\omega x}d\omega/\pi = \delta(x) + (\pi i x)^{-1}$ automatically enforces that virtual quanta carry positive energy in the proper direction. Including the vector-potential contribution via $(1-\mathbf{v}_a\cdot\mathbf{v}_b)\delta_+(s^2) \to \gamma_{a\mu}\gamma_{b\mu}\delta_+(s^2)$ produces the fundamental one-quantum exchange amplitude (Eq. 4) which is the prototype for all higher-order processes. The diagrammatic content of Fig. 1 is stated explicitly: "$a$" emits a quantum at 5 (factor $K_+(5,1)$, vertex $\gamma_{a\mu}$, propagator $K_+(3,5)$ after), "$b$" absorbs it at 6 (factors $K_+(6,2)$, $\gamma_{b\mu}$, $K_+(4,6)$), with quantum propagation $\delta_+(s_{56}^2)$ summed over $\mu$ and integrated over all emission/absorption events. Temporal ordering of 5 vs. 6 is not separated — "absorption" vs. "emission" are automatically contained in the invariant $\delta_+$.

### 3. Feynman Rules in Momentum Space (Section 4)

By Fourier transformation, Feynman exhibits the now-standard rules (illustrated by the self-energy integral, Eq. 11, and Fig. 3):

- Electron propagator: $(p-m)^{-1}$ — "reciprocal of the Dirac equation operator."
- Photon propagator: $k^{-2}$ — "reciprocal D'Alembertian of the wave equation of light."
- Vertex: $\gamma_\mu$ (with factor $e^2/\pi i$ for each virtual quantum, and $d^4k = (2\pi)^{-2}dk_1 dk_2 dk_3 dk_4$).
- Poles resolved by giving masses infinitesimal negative imaginary parts.

Diagrams are presented for: self-energy (Fig. 2, 3), radiative corrections to scattering (Fig. 4a/b/c = Eqs. 12–14), Compton scattering (Fig. 5, Eq. 15), vacuum polarization (Fig. 6, Eq. 30), and Klein-Gordon particle in three potentials (Fig. 7), two-quantum Møller corrections (Fig. 8, nine topologies), and radiative corrections to Compton (Fig. 9).

### 4. Compton Scattering (Eq. 15)

The full Klein-Nishina amplitude is written as the sum of two diagrams — absorption of $q_1$ before emission of $q_2$ (Fig. 5a) and the reverse order (Fig. 5b):

$$e_2(\not p_1 + \not q_1 - m)^{-1} e_1 + e_1(\not p_1 - \not q_2 - m)^{-1} e_2$$

Pair annihilation into two quanta is the same matrix with positron states reinterpreted as negative-time-component $p$. Whether a quantum is absorbed or emitted is read off the sign of the time component of $q$.

### 5. Convergence, Cut-off, and Mass Renormalization (Sections 5–6)

The self-energy (Eq. 11) diverges from the coincidence of the $\delta$-function singularities in $K_+$ and $\delta_+$. A convergence factor $C(k^2) = -\lambda^2/(k^2-\lambda^2)$ — interpretable as subtracting a heavy-photon contribution weighted by $G(\lambda)$ with $\int G(\lambda)d\lambda = 1$ and $\int\lambda^2 G(\lambda)d\lambda = 0$ — renders every virtual-quantum integral convergent. The self-energy then yields (Eq. 20):

$$(e^2/2\pi)\bigl[4m(\ln(\lambda/m) + 1/2) - \not p(\ln(\lambda/m) + 5/4)\bigr]$$

and for on-shell $\not p u = mu$ gives the mass shift (Eq. 21):

$$\Delta m = m(e^2/2\pi)(3\ln(\lambda/m) + 3/4)$$

The radiative correction to scattering (Eq. 22) contains the celebrated term (Eq. 24):

$$(e^2/4\pi)\Bigl[(1/2m)(\not q a - a \not q) + (4q^2/3m^2) a \bigl(\ln(m/\lambda_{\min}) - 3/8\bigr)\Bigr]$$

which produces the **anomalous magnetic moment** (the $(\not q a - a \not q)/2m$ piece gives $\alpha/2\pi$) and the **Lamb shift** (the $q^2\ln$ piece). Feynman's footnote 13 corrects the erroneous $-1$ to $-5/6$ (joining to Bethe's non-relativistic calculation) so the result agrees with French–Weisskopf and Kroll–Lamb.

### 6. Vacuum Polarization (Section 7)

A closed electron loop (Fig. 6, Eq. 32) gives a current $4\pi j_\mu = J_{\mu\nu}a_\nu$ that diverges quadratically. The Bethe-Pauli subtraction — replacing $m \to (m^2 + \lambda^2)^{1/2}$ over an entire closed loop — preserves gauge invariance ($q_\mu J_{\mu\nu} = 0$) and yields the finite result (Eq. 33):

$$J_{\mu\nu}^P = -(e^2/\pi)(q_\mu q_\nu - \delta_{\mu\nu}q^2)\Bigl[-\tfrac{1}{3}\ln(\lambda^2/m^2) - \bigl(\tfrac{4m^2+2q^2}{3q^2}\bigr)(1 - \theta/\tan\theta) - 1/9\Bigr]$$

with $q^2 = 4m^2\sin^2\theta$. The $\ln\lambda^2$ is absorbed into **charge renormalization** $\Delta(e^2)/e^2 = -(2e^2/3\pi)\ln(\lambda/m)$. The remainder gives Uehling's $q^2/5m^2$ for small $q^2$ (Lamb shift contribution) and an imaginary part for $q^2 > 4m^2$ (pair production).

### 7. Longitudinal Waves and Klein-Gordon/Meson Extensions (Sections 8–10)

Gauge invariance ($\partial A_\mu/\partial x_\mu = 0$) is automatic: the identity $(\not p_k + \not q - m)^{-1}\not q(\not p_k - m)^{-1} = (\not p_k - m)^{-1} - (\not p_k + \not q - m)^{-1}$ (Eq. 34) makes every emission amplitude proportional to $q_\mu\gamma_\mu$ vanish. The Klein-Gordon sector (Section 9) requires a new two-quantum seagull vertex $-\delta_{\mu\nu}$ from the $A_\mu A_\mu$ term and stronger convergence ($\int\lambda^2 G(\lambda)d\lambda = 0$) because of gradient couplings. Meson theories (scalar, pseudoscalar, vector, pseudovector; neutral and charged; various couplings) are cast in the same diagrammatic language, with pseudoscalar-pseudovector equivalence noted only to lowest order.

---

## Key Results

1. **Feynman rules for QED established**: propagator $(\not p - m)^{-1}$ for electrons, $k^{-2}$ for photons, vertex $\gamma_\mu$, with factor $e^2/\pi i$ per virtual quantum and $d^4k$ integration.
2. **Invariant photon propagator** $\delta_+(s^2)$ replacing $\delta(s^2)/r$ — unifies retarded and advanced contributions and combines longitudinal + transverse waves relativistically.
3. **Diagrammatic algorithm**: each topologically distinct diagram is summed with equal weight; time ordering of vertices along a line is irrelevant.
4. **Compton scattering amplitude (Eq. 15)** as sum of two diagrams, reproducing Klein-Nishina.
5. **Self-energy mass shift** $\Delta m = (3\alpha/2\pi)m\ln(\lambda/m) + \text{finite}$ (Eq. 21).
6. **Anomalous magnetic moment**: the $(\not q a - a \not q)/2m$ term in Eq. 24 reproduces Schwinger's $\alpha/2\pi$ (stated, not written out as a numerical value, but equivalent to Schwinger's result via the stated equivalence).
7. **Lamb shift contribution** from the $(4q^2/3m^2)(\ln(m/\lambda_{\min}) - 3/8)$ term in Eq. 24, together with the Uehling $q^2/5m^2$ piece from vacuum polarization (Section 7).
8. **Charge renormalization** $\Delta e^2/e^2 = -(2\alpha/3\pi)\ln(\lambda/m)$ — logarithmic (not quadratic) divergence is noted as "suspiciously unique" to electrodynamics.
9. **Gauge invariance / current conservation** $\partial A_\mu/\partial x_\mu = 0$ follows automatically from the identity (Eq. 34); preserved only if the Bethe-Pauli loop subtraction scheme is used.
10. **Closed-loop rules**: odd number of vertices gives zero (Furry); loops with four or more vertices are convergent without a cut-off.
11. **Klein-Gordon extension** introduces a two-quantum seagull vertex $\delta_{\mu\nu}$ (Eq. 36, Fig. 7b).
12. **Møller-to-second-order** catalogued as nine topologically distinct diagrams (Fig. 8a–i) with the exchange-symmetry subtraction applied at the end.
13. **Appendix method** for evaluating loop integrals: Feynman parameter $a^{-1}b^{-1} = \int_0^1 dx\,(ax + b(1-x))^{-2}$ (Eq. 14a), Wick-rotation-style contour closure giving $\int d^4k(k^2-L)^{-3} = (8iL)^{-1}$ (Eq. 10a), and parametric differentiation to generate higher-order integrals.

---

## Key Equations

| # | Equation | Role |
|---|----------|------|
| (3) | $\delta_+(x) = \int_0^\infty e^{-i\omega x}d\omega/\pi = \delta(x) + (\pi i x)^{-1}$ | Positive-frequency delta function for photon propagator |
| (4) | $K^{(1)}(3,4;1,2) = -ie^2\iint K_{+a}(3,5)K_{+b}(4,6)\gamma_{a\mu}\gamma_{b\mu}\delta_+(s_{56}^2)K_{+a}(5,1)K_{+b}(6,2)d\tau_5 d\tau_6$ | Fundamental one-quantum exchange amplitude |
| (6) | $K^{(1)}(2,1) = -ie^2\iint K_+(2,4)\gamma_\mu K_+(4,3)\gamma_\mu K_+(3,1)d\tau_3 d\tau_4\,\delta_+(s_{43}^2)$ | One-loop electron self-energy in coordinate space |
| (10) | $-\delta_+(s_{21}^2) = \pi^{-1}\int \exp(-ik\cdot x_{21})k^{-2}d^4k$ | Fourier transform: photon propagator in momentum space |
| (11) | $\Sigma(p) = (e^2/\pi i)\int \gamma_\mu(\not p - \not k - m)^{-1}\gamma_\mu k^{-2}d^4k$ | Self-energy in momentum space |
| (12) | $M = (e^2/\pi i)\int \gamma_\mu(\not p_2 - \not k - m)^{-1}a(\not p_1 - \not k - m)^{-1}\gamma_\mu k^{-2}d^4k$ | Vertex correction to scattering |
| (15) | $M_{\text{Compton}} = e_2(\not p_1 + \not q_1 - m)^{-1}e_1 + e_1(\not p_1 - \not q_2 - m)^{-1}e_2$ | Compton scattering amplitude |
| (17) | $C(k^2) = \int_0^\infty -\lambda^2(k^2 - \lambda^2)^{-1}G(\lambda)d\lambda$ | Photon convergence factor |
| (20) | $\Sigma(p) = (e^2/2\pi)[4m(\ln(\lambda/m) + 1/2) - \not p(\ln(\lambda/m) + 5/4)]$ | Evaluated self-energy |
| (21) | $\Delta m = m(e^2/2\pi)(3\ln(\lambda/m) + 3/4)$ | Electron mass renormalization |
| (24) | $\delta M = (e^2/4\pi)\bigl[(1/2m)(\not q a - a\not q) + (4q^2/3m^2)a(\ln(m/\lambda_{\min}) - 3/8)\bigr]$ | Anomalous moment + Lamb shift pieces |
| (32) | $J_{\mu\nu} = -(e^2/\pi i)\int \mathrm{Sp}[(\not p + \not q - m)^{-1}\gamma_\nu(\not p - m)^{-1}\gamma_\mu]d^4p$ | Vacuum polarization tensor |
| (33) | $J_{\mu\nu}^P = -(e^2/\pi)(q_\mu q_\nu - \delta_{\mu\nu}q^2)\bigl[-\tfrac{1}{3}\ln(\lambda^2/m^2) - \bigl(\tfrac{4m^2+2q^2}{3q^2}\bigr)(1 - \theta/\tan\theta) - 1/9\bigr]$ | Gauge-invariant vacuum polarization |
| (34) | $(\not p_k + \not q - m)^{-1}\not q(\not p_k - m)^{-1} = (\not p_k - m)^{-1} - (\not p_k + \not q - m)^{-1}$ | Ward-like identity enforcing gauge invariance |
| (14a) | $a^{-1}b^{-1} = \int_0^1 dx(ax + b(1-x))^{-2}$ | Feynman parameterization |

---

## Relevance to Phonon-Exflation

The phonon-exflation framework posits that observable physics emerges from spectral moments of $D_K$ on Jensen-deformed $SU(3)$. The connection to Feynman's 1949 paper is foundational at three layers:

1. **Feynman rules = perturbative expansion of the spectral action.** The bare spectral action $\mathrm{Tr}\,f(D/\Lambda)$ generates the Standard Model Lagrangian as a heat-kernel sum of Seeley-DeWitt coefficients. Once the SM Lagrangian is identified, the full apparatus of Feynman — propagators $(\not p - m)^{-1}$, vertex factors $\gamma_\mu$, loop integrals with convergence factors — is *exactly* the machinery that converts the spectral action into amplitudes a detector can measure. Every phonon-exflation computation computation that evaluates a QED/QCD/EW process on the substrate implicitly imports Eqs. (4)–(15) of this paper as the translation layer from spectral moments to cross sections.

2. **Diagrammatic vocabulary for relay patterns on the substrate.** In the phonon-exflation picture, "a particle" is a relay pattern propagating through the fiber's gauge connection. A Feynman diagram is literally the space-time history of such a relay: each $K_+$ propagator is the substrate's amplitude for a phononic excitation to propagate between fiber events, each vertex $\gamma_\mu$ is the local excitation of a fiber's eigenvalue spectrum by another relay, each $\delta_+(s^2)$ is the invariant retarded-plus-positive-frequency prescription for how excitations communicate across the fabric. The 1949 paper's diagrammatic language is therefore not merely borrowed — it is the *canonical* description of what happens on the fabric when two relay patterns overlap at a single fiber (Feynman's words in Fig. 1 and the interpretation of Eq. 4 translate directly).

3. **Convergence-factor modification and the substrate cut-off.** Feynman's convergence factor $C(k^2) = -\lambda^2/(k^2 - \lambda^2)$ with $\lambda\to\infty$ after mass/charge renormalization is philosophically analogous to the substrate's intrinsic cut-off at $M_{\mathrm{KK}}$: phononic excitations above the KK threshold are not available as asymptotic states, and their effect on low-energy observables is absorbed into renormalized couplings. The phonon-exflation program replaces the ad hoc Pauli-Villars prescription with a physically concrete cut-off dictated by the spectral geometry. Feynman's own footnote that "electrodynamics is suspiciously unique in the mildness of its divergence" (paragraph before Appendix D) is a hint that the geometric origin of the SM couplings may explain the logarithmic-only character of charge renormalization — a question the spectral-action derivation is uniquely positioned to address.
