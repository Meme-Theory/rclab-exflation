# Topological Defect Formation in a Phase Transition with Tunable Order

**Author(s):** Fumika Suzuki, Wojciech H. Zurek
**Year:** 2025
**Journal:** [INCOMPLETE - not extractable from PDF]
**arXiv:** 2312.01259
**Relevance:** HIGH

---

## Abstract

The Kibble-Zurek mechanism (KZM) describes the non-equilibrium dynamics and topological defect formation in systems undergoing second-order phase transitions. KZM has found applications in fields such as cosmology and condensed matter physics. However, it is generally not suitable for describing first-order phase transitions. It has been demonstrated that transitions in systems like superconductors or charged superfluids, typically classified as second-order, can exhibit weakly first-order characteristics when the influence of fluctuations is taken into account. Moreover, the order of the phase transition (i.e., the extent to which it becomes first rather than second order) can be tuned. We explore quench-induced formation of topological defects in such tunable phase transitions and propose that their density can be predicted by combining KZM with nucleation theory.

---

## Key Arguments and Derivations

### Modified Landau-Ginzburg Potential

The system is governed by a real scalar field $\phi$ with a modified Landau-Ginzburg potential:

$$V(\phi) = \frac{\phi^4 - 2\epsilon\phi^2}{8} - \frac{c|\phi|^3}{3}$$

The first two terms describe a standard second-order phase transition. The third term (controlled by parameter $c$) introduces first-order characteristics. When $c = 0$, this is a standard $\phi^4$ second-order transition. When $c > 0$, nucleation barriers appear.

### Linear Quench and Langevin Dynamics

The control parameter follows a linear quench $\epsilon(t) = t/\tau_Q$ with $\tau_Q$ the quench timescale. The field obeys the Langevin equation:

$$\ddot{\phi} + \eta\dot{\phi} - \partial_{xx}\phi + \partial_\phi V(\phi) = \vartheta(x,t)$$

with noise correlation $\langle\vartheta(x,t), \vartheta(x',t')\rangle = 2\eta\theta\delta(x'-x)\delta(t'-t)$ at reservoir temperature $\theta$ and damping $\eta = 1$.

### Phase Transition Regimes

For $c > 0$:
- **$\epsilon < -c^2$**: Single minimum at $\phi = 0$, symmetric (like second-order).
- **$-c^2 < \epsilon < 0$**: Two new minima at $\phi = \pm(c + \sqrt{c^2+\epsilon})$ coexist with $\phi = 0$, enabling nucleation (first-order character).
- **$\epsilon > 0$**: Two broken-symmetry minima (standard symmetry-broken phase).

The nucleation barrier height is:

$$h_{\text{barrier}} = -\frac{1}{24}(c - \sqrt{c^2+\epsilon})^2(3\epsilon + 2c(c - \sqrt{c^2+\epsilon}))$$

Both barrier position and height approach zero as $\epsilon \to 0$.

### Numerical Results

For $c = 0$ (pure second-order), the defect density obeys $n_{\text{KZM}} \propto \tau_Q^{-a}$ with best-fit $a = 0.267 \pm 0.029$, agreeing with the KZM prediction $a = 1/4$.

For $c > 0$, deviations from KZM appear at large $\tau_Q$ due to nucleation events. Faster quenches (small $\tau_Q$) prevent the field from interacting with nucleation barriers, preserving KZM scaling.

### Combining KZM with Nucleation Theory

The fraction of space $f$ occupied by the new phase due to nucleation between times $t_1$ and $t_2$ is given by the Avrami equation:

$$f = 1 - \exp(-\Omega)$$

where:

$$\Omega = \int_{t_1}^{t_2} \Gamma(\epsilon(t)) \mathcal{V}(t,t_2) \, dt$$

Here $\Gamma(\epsilon)$ is the nucleation rate per unit length:

$$\Gamma(\epsilon(t)) = A\exp[-B(\epsilon(t))/\theta]$$

with $B(\epsilon)$ the bounce action:

$$B(\epsilon(t)) = 2\int_0^{\phi_{TP}} d\phi\sqrt{2V(\phi)}$$

and $\mathcal{V}(t,t_2)$ is the volume of a nucleated bubble at time $t_2$ that formed at time $t$, determined by the bubble wall velocity $v(\epsilon)$.

**Key times:**
- $t_1$: when $\sqrt{\langle\phi^2\rangle} \approx \phi_{\text{barrier}}$ (field begins interacting with barrier)
- $t_2$: when $B(\epsilon(t_2)) = \theta$ (barrier energy equals kinetic energy)

### Central Result: Defect Density Formula

The total number of defects in a phase transition with tunable order is:

$$n = f \cdot n_{\text{nuc}} + (1-f) \cdot n_{\text{KZM}}$$

where:
- $n_{\text{KZM}} \propto \tau_Q^{-1/4}$ (from KZM for 1D with $a = 1/4$)
- $n_{\text{nuc}} \approx n_{\text{nuc}}(\epsilon^*)$ is the defect density from pure nucleation, evaluated at the time-averaged $\epsilon^*$ when fraction $f/2$ has been converted
- $f$ is the Avrami fraction

### Regime Classification

- **$f = 0$**: No nucleation. Pure KZM regime. Valid for fast quenches or low temperature.
- **$f = 1$**: Complete nucleation before the second-order point. Defect density from nucleation theory alone.
- **$0 < f < 1$**: Mixed regime. KZM for the unaffected fraction, nucleation theory for the converted fraction.

### Discrepancy Analysis

The discrepancy between KZM prediction and the actual defect density is:

$$\delta = \left|\frac{n - n_{\text{KZM}}}{n_{\text{KZM}}}\right| = f\left|1 - \frac{n_{\text{nuc}}}{n_{\text{KZM}}}\right|$$

This quantity increases with both $c$ (first-order strength) and $\theta$ (temperature), and is well-predicted by the combined formula Eq. (10).

### Parametric Dependencies

- **Higher $\theta$**: Increases nucleation rate, larger deviation from KZM.
- **Larger $c$**: Nucleation barriers persist longer, deviations even at small $\tau_Q$.
- **For $c = 1$, $\theta = 0.01$**: $v(\epsilon) = 0.026\epsilon + 0.016$, $n_{\text{nuc}}(\epsilon) = 144\epsilon + 74$.
- **For $c = 1$, $\theta = 0.001$**: Low nucleation rate, only small deviation from KZM.

---

## Key Results

1. KZM remains valid for describing defect formation in weakly first-order transitions when combined with nucleation theory via the formula $n = fn_{\text{nuc}} + (1-f)n_{\text{KZM}}$.
2. For purely second-order transitions ($c=0$), numerics confirm $n_{\text{KZM}} \propto \tau_Q^{-1/4}$ in agreement with KZM theory.
3. The Avrami fraction $f$ provides a quantitative diagnostic for distinguishing KZM-dominated ($f \approx 0$) from nucleation-dominated ($f \approx 1$) regimes.
4. Fast quenches (small $\tau_Q$) preserve KZM scaling even for $c > 0$, because the field traverses the nucleation region too quickly for bubbles to form.
5. The combined formula accurately predicts defect densities across the full range of transition orders and quench rates.
6. Experimental validation could be pursued in liquid crystal Fredericks transitions where the transition order is tunable.

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Modified LG potential | $V(\phi) = (\phi^4 - 2\epsilon\phi^2)/8 - c|\phi|^3/3$ | Eq. (1) |
| Langevin equation | $\ddot{\phi} + \eta\dot{\phi} - \partial_{xx}\phi + \partial_\phi V = \vartheta(x,t)$ | Eq. (2) |
| Noise correlation | $\langle\vartheta(x,t),\vartheta(x',t')\rangle = 2\eta\theta\delta(x'-x)\delta(t'-t)$ | Eq. (3) |
| Barrier height | $h_{\text{barrier}} = -\frac{1}{24}(c-\sqrt{c^2+\epsilon})^2(3\epsilon+2c(c-\sqrt{c^2+\epsilon}))$ | Eq. (4) |
| Nucleation rate | $\Gamma(\epsilon) = A\exp[-B(\epsilon)/\theta]$ | Eq. (5) |
| Bounce action | $B(\epsilon) = 2\int_0^{\phi_{TP}}d\phi\sqrt{2V(\phi)}$ | Eq. (6) |
| Avrami equation | $f = 1 - \exp(-\Omega)$ | Eq. (7) |
| Avrami integral | $\Omega = \int_{t_1}^{t_2}\Gamma(\epsilon(t))\mathcal{V}(t,t_2)dt$ | Eq. (8) |
| Fixed-$\epsilon$ Avrami | $f_{\text{fixed}} = 1 - \exp(-\frac{1}{2}v\Gamma t^2)$ | Eq. (9) |
| Combined defect density | $n = fn_{\text{nuc}} + (1-f)n_{\text{KZM}}$ | Eq. (10) |
| Discrepancy | $\delta = f|1 - n_{\text{nuc}}/n_{\text{KZM}}|$ | Eq. (11) |
| KZM scaling (1D) | $n_{\text{KZM}} \propto \tau_Q^{-1/4}$ | Section: Numerical |
| Bubble velocity (fitted) | $v(\epsilon) = 0.026\epsilon + 0.016$ ($c=1$, $\theta=0.01$) | Supplemental |
| Nucleation defects (fitted) | $n_{\text{nuc}}(\epsilon) = 144\epsilon + 74$ ($c=1$, $\theta=0.01$) | Supplemental |

---

## Relevance to Phonon-Exflation

This paper is directly relevant to the framework's BCS transit mechanism. Session 36 found GL-CUBIC-36: the BCS transit exhibits Z$_2$ universality class, which could be either second-order or weakly first-order depending on the cubic coupling. Suzuki and Zurek demonstrate precisely how to handle this ambiguity: the combined formula $n = fn_{\text{nuc}} + (1-f)n_{\text{KZM}}$ interpolates smoothly between KZM (second-order) and nucleation (first-order) regimes using the Avrami fraction $f$ as the diagnostic. For the framework, the instanton gas (Session 37-38: $S_{\text{inst}} = 0.069$, dense regime) may correspond to the nucleation events in Suzuki-Zurek's model, with the Avrami fraction $f$ determined by the ratio of instanton tunneling rate to transit speed. The result that fast quenches preserve KZM scaling is consistent with the framework's finding that the transit is fast ($\omega_\tau = 8.27$ vs. $\omega_{\text{att}} = 1.43$, Session 38 inverted Born-Oppenheimer).
