# Gluonic vacuum, q-theory, and the cosmological constant

**Author(s):** F.R. Klinkhamer, G.E. Volovik
**Year:** 2009
**Journal:** Phys. Rev. D 79, 063527 (2009)
**arXiv:** 0811.4347
**Relevance:** CRITICAL

---

## Abstract

In previous work, q-theory was introduced to describe the gravitating macroscopic behavior of a conserved microscopic variable q. In this article, the gluon condensate of quantum chromodynamics is considered in terms of q-theory. The remnant vacuum energy density (i.e., cosmological constant) of an expanding universe is estimated as $K^3_{\text{QCD}}/E^2_{\text{Planck}}$, with string tension $K_{\text{QCD}} \approx (10^2 \text{MeV})^2$ and gravitational scale $E_{\text{Planck}} \approx 10^{19}$ GeV. The only input for this estimate is general relativity, quantum chromodynamics, and the Hubble expansion of the present Universe.

---

## Key Arguments and Derivations

### II. Gluon Condensate
The QCD gluon condensate is identified as a concrete realization of the vacuum variable $q$:

$$q(x) = \langle 0 | \frac{1}{4\pi^2} G^a_{\mu\nu}(x) G^{a\mu\nu}(x) | 0 \rangle$$

This is the Shifman-Vainshtein-Zakharov condensate ($q \approx 10^{-2}$ GeV$^4$). The energy-momentum tensor takes the cosmological-constant form $T_{\mu\nu}(q) = \rho_{\text{vac}}(q) g_{\mu\nu}$ with $\rho_{\text{vac}} = \epsilon(q) - q \, d\epsilon/dq$.

### III-IV. Equation for q
The "master gauge field" formalism yields the equation of motion. For a Yang-Mills vacuum, $d\epsilon/dq = \mu = \text{const}$, confirming $q$ is conserved with chemical potential $\mu$.

### V. Effective Potential
Using asymptotic freedom and the conformal anomaly at one loop:

$$\epsilon(q) = \epsilon_0 + b_1 q \ln(q/q_c)$$

with $b_1 = \frac{1}{32}(\frac{11}{3}N_c - \frac{2}{3}N_f)$ for $N_c = 3$, $N_f = 2$. The vacuum compressibility is $\chi = (b_1 q)^{-1} > 0$ for the non-Abelian case.

### VI. Cosmological Constant from QCD
The self-sustained gluonic vacuum has $\rho_{\text{vac}}(q_0) = 0$ exactly. But in the expanding universe, the gluon condensate is perturbed and:

$$\rho_{\text{vac}} \sim f |H| \Lambda^3_{\text{QCD}}$$

Using Friedmann equation $H^2 = (8\pi/3)\Lambda/E^2_{\text{Planck}}$, the remnant cosmological constant is:

$$\Lambda = k_\Lambda K^3_{\text{QCD}}/E^2_{\text{Planck}} \approx (3 \times 10^{-3} \text{eV})^4$$

with numerical factor $k_\Lambda \sim 10^{-6}$. This is the correct order of magnitude for the observed dark energy.

### VII. Crossover Time
The crossover from matter-dominated to vacuum-dominated expansion occurs at:

$$t_{\text{cross}} \approx (6\pi k_\Lambda)^{-1/2} E^2_{\text{Planck}} K^{-3/2}_{\text{QCD}} \approx 2 \times 10^{17} \text{s}$$

which is of the order of the observed age of the universe.

## Key Results

1. The QCD gluon condensate provides a concrete, physical realization of the q-variable
2. The remnant CC scales as $\Lambda \sim K^3_{\text{QCD}}/E^2_{\text{Planck}}$, reproducing the observed $(2 \text{ meV})^4$
3. The non-analytic $|H| \Lambda^3_{\text{QCD}}$ dependence arises from infrared confinement physics
4. The crossover time $t_{\text{cross}} \sim 10^{17}$ s matches observation
5. A stable self-sustained vacuum requires non-Abelian gauge theory ($b_1 > 0$)
6. The vacuum compressibility $\chi$ plays a crucial role in the dynamics

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Gluon condensate | $q = \langle \frac{1}{4\pi^2} G^a_{\mu\nu} G^{a\mu\nu} \rangle$ | Eq. (2.4) |
| Effective potential | $\epsilon(q) = \epsilon_0 + b_1 q \ln(q/q_c)$ | Eq. (5.1a) |
| Vacuum energy | $\rho_{\text{vac}} = \epsilon_0 - b_1 q(\mu)$ | Eq. (5.2b) |
| CC estimate | $\Lambda = k_\Lambda K^3_{\text{QCD}}/E^2_{\text{Planck}}$ | Eq. (6.7) |
| Hubble perturbation | $\rho_{\text{vac}} \sim f |H| \Lambda^3_{\text{QCD}}$ | Eq. (6.3) |
| Crossover time | $t_{\text{cross}} \approx (6\pi k_\Lambda)^{-1/2} E^2_P K^{-3/2}_{\text{QCD}}$ | Eq. (7.2) |

## Relevance to Phonon-Exflation

This paper provides the most concrete bridge between q-theory and the phonon-exflation framework:
- The gluon condensate as $q$-variable directly parallels the framework's treatment of the SU(3) fiber vacuum as a condensed-matter-like medium
- The $\rho_{\text{vac}} \sim |H| \Lambda^3_{\text{QCD}}$ scaling connects to the framework's CC mechanism: the Hubble expansion perturbs the vacuum away from its self-tuned equilibrium
- The non-analytic infrared behavior (Gribov confinement, $m(k) \sim \Lambda^3/k^2$) that produces the $|H|$ term is analogous to the instanton gas dynamics in the framework
- The conformal anomaly driving the effective potential parallels the framework's spectral action trace anomaly
- The QCD vacuum compressibility connects to the framework's BCS compressibility of the paired ground state
- User insight "q-theory is F-theory in a dress" is validated: same variational principle ($d\rho/dq = 0$ vs $dV/d\phi = 0$), different language
