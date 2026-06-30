# The Cosmological Constant Problems

**Author(s):** Steven Weinberg
**Year:** 2000
**Journal:** Talk given at Dark Matter 2000, Marina del Rey, CA, February 2000 (UTTG-07-00)
**arXiv:** astro-ph/0005265
**Relevance:** CRITICAL — for a project studying phonon-exflation cosmology where the CC overshoot is the key open problem

---

## Abstract

The old cosmological constant problem is to understand why the vacuum energy is so small; the new problem is to understand why it is comparable to the present mass density. Several approaches to these problems are reviewed. Quintessence does not help with either; anthropic considerations offer a possibility of solving both. In theories with a scalar field that takes random initial values, the anthropic principle may apply to the cosmological constant, but probably to nothing else.

---

## Key Arguments and Derivations

### Section 1: Introduction — Two Cosmological Constant Problems

Weinberg identifies two distinct CC problems:

1. **The old CC problem**: Why is the vacuum energy density $\rho_V$ not very much larger? Calculable contributions (e.g., energy density in gravitational field fluctuations at graviton energies up to the Planck scale) exceed the observational bound by ~120 orders of magnitude. These terms can be cancelled by incalculable contributions, but the cancellation must be accurate to 120 decimal places.

2. **The new CC problem**: Why is $\rho_V$ not only small but also of the same order of magnitude as the present mass density of the universe, as indicated by Type Ia supernova observations (Riess et al. 1998, Perlmutter et al. 1999)?

Weinberg classifies four approaches:
- (i) Scalar field adjustment mechanisms (subject to his 1989 no-go theorem)
- (ii) Deep symmetry constraining the effective theory (deferred to Witten)
- (iii) Quintessence (Section 2)
- (iv) Anthropic principle (Section 3)

### Section 2: Quintessence

Quintessence posits that the CC is small because the universe is old. A uniform scalar field $\phi(t)$ rolls down a potential $V(\phi)$, governed by the field equation $\ddot{\phi} + 3H\dot{\phi} + V'(\phi) = 0$ with expansion rate $H = \sqrt{(3/8\pi G)(\rho_\phi + \rho_M)}$. As $\phi$ approaches a value where $V'(\phi) = 0$, it changes slowly, while $\rho_M$ steadily decreases, eventually yielding exponential expansion with $H \simeq \sqrt{8\pi G V(\phi)/3}$.

**Tracker solutions** (Zlatev, Wang, Steinhardt 1999) use potentials $V(\phi) = M^{4+\alpha}\phi^{-\alpha}$ with $\alpha > 0$. The scalar field begins with $V(\phi)$ and $\dot{\phi}^2$ much less than $\rho_M$. Initially $\phi(t) \sim t^{2/(2+\alpha)}$ so $\rho_\phi \sim t^{-2\alpha/(2+\alpha)}$ while $\rho_M \sim t^{-2}$ (faster). Eventually $\rho_M$ drops to $\rho_\phi$, after which $\rho_\phi$ decreases more slowly as $t^{-2/(4+\alpha)}$ and $\log R(t) \propto t^{4/(4+\alpha)}$.

**Weinberg's critique**: Tracker solutions do not require fine-tuning of initial conditions, but they solve neither CC problem:
- Adding a constant of order $m_{\text{Planck}}^4$ (or $m_W^4$, or $m_e^4$) to $V(\phi)$ spoils the late-time decrease of $\rho_\phi$.
- Even without such a constant, fine-tuning of the mass scale $M$ is required: $M^{4+\alpha} \approx (8\pi G)^{-1-\alpha/2} H_0^2$ to ensure the $\rho_M$-to-$\rho_\phi$ crossover occurs near the present epoch.

### Section 3: Anthropic Considerations

In cosmological theories where the observed big bang is one member of an ensemble (different expanding regions in the same spacetime, or different terms in the wave function of the universe), the observed $\rho_V$ is conditioned by the requirement that it permit intelligent life.

**Anthropic upper bound on positive $\rho_V$**: Using the spherical infall model (Peebles 1967), galaxy formation requires $\rho_V < 500\,\rho_R\,\delta_R^3/729$, where $\rho_R$ is the mass density and $\delta_R$ is a typical fractional density perturbation at recombination. This is roughly $\rho_V \lesssim$ the cosmic mass density at the earliest time of galaxy formation ($\sim 200$ times present mass density for max galactic redshift $z \sim 5$). This improves the 120 OOM discrepancy but is insufficient alone.

**Principle of mediocrity** (Vilenkin): We should expect to find ourselves in a big bang typical of those permitting intelligent life. The probability of observing $\rho_V$ is $d\mathcal{P}(\rho_V) = \mathcal{N}(\rho_V)\,\mathcal{P}_{\text{a priori}}(\rho_V)\,d\rho_V$, where $\mathcal{N}(\rho_V)$ is the fraction of baryons ending up in galaxies and $\mathcal{P}_{\text{a priori}}$ is the a priori distribution. Since $\mathcal{N}(\rho_V)$ is non-zero only in a narrow range much smaller than particle physics energy scales, $\mathcal{P}_{\text{a priori}}$ is approximately constant in this range.

**Martel-Shapiro-Weinberg calculation** (1998): Using the Gunn-Gott spherical infall model, the probability of $\Omega_V \leq 0.7$ is 5% to 12% depending on the estimate of $\sigma$ (rms fractional density perturbation at recombination). The observed vacuum energy is somewhat low but not implausibly so. This provides a potential solution to both the old and new CC problems.

**Garriga-Vilenkin challenge**: They argued that in models with a scalar field $\phi$ in a very flat potential satisfying $|V'(\phi)/V(\phi)| \ll \sqrt{8\pi G}$ and $|V''(\phi)/V(\phi)| \ll 8\pi G$, the a priori distribution $\mathcal{P}_{\text{a priori}}(V(\phi)) \propto 1/|V'(\phi)|$ could vary appreciably within the anthropically allowed range.

**Weinberg's response**: For potentials of the form $V(\phi) = V_1 f(\lambda\phi)$ where $V_1$ is a large energy density, $\lambda > 0$ is very small, and $f(x)$ has a simple zero at $x = a$ with derivatives of order unity, the slow-roll conditions require $\lambda \ll \sqrt{8\pi G}\,(\rho_V/V_1)$. The fractional variation of $\mathcal{P}_{\text{a priori}}$ in the anthropically allowed range is $\sim |V_{\text{max}}/V_1| \ll 1$, confirming the flatness assumption.

**Key conclusion on scope**: A scalar field with a very flat potential, when quantized, produces very light bosons that should have been observed if the field couples to standard model particles. Therefore anthropic considerations via such scalar fields may apply to the CC but probably to nothing else — the field can only couple to itself and gravitation (and possibly a hidden sector).

## Key Results

1. The old CC problem (120 OOM discrepancy between calculated vacuum energy contributions and observation) and the new CC problem (coincidence of $\rho_V$ with present matter density) are logically distinct.
2. Quintessence (tracker solutions) does not solve either CC problem — it requires fine-tuning of the mass scale $M$ and is unstable to additive constants in the potential.
3. The anthropic bound from galaxy formation gives $\rho_V < 500\,\rho_R\,\delta_R^3/729$, improving from 120 OOM to $\sim 200\times$ present density.
4. The Martel-Shapiro-Weinberg anthropic calculation gives 5-12% probability of $\Omega_V \leq 0.7$, consistent with observation.
5. For a broad class of potentials $V(\phi) = V_1 f(\lambda\phi)$, the a priori probability distribution is flat within the anthropically allowed range, validating the Martel-Shapiro-Weinberg calculation against the Garriga-Vilenkin critique.
6. Anthropic selection via flat-potential scalar fields may apply to the CC but probably to nothing else, due to observational constraints on light scalars.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Quintessence field eq. | $\ddot{\phi} + 3H\dot{\phi} + V'(\phi) = 0$ | Eq. (1) |
| Friedmann expansion rate | $H = \sqrt{\frac{3}{8\pi G}(\rho_\phi + \rho_M)}$ | Eq. (2) |
| Scalar field energy density | $\rho_\phi = \frac{1}{2}\dot{\phi}^2 + V(\phi)$ | Eq. (3) |
| Matter energy conservation | $\dot{\rho}_M = -3H(\rho_M + p_M)$ | Eq. (4) |
| Tracker potential | $V(\phi) = M^{4+\alpha}\phi^{-\alpha}$ | Eq. (5) |
| Tracker fine-tuning condition | $M^{4+\alpha} \approx (8\pi G)^{-1-\alpha/2} H_0^2$ | Eq. (6) |
| Anthropic upper bound | $\rho_V < \frac{500\,\rho_R\,\delta_R^3}{729}$ | Eq. (7) |
| Anthropic probability | $d\mathcal{P}(\rho_V) = \mathcal{N}(\rho_V)\,\mathcal{P}_{\text{a priori}}(\rho_V)\,d\rho_V$ | Eq. (8) |
| Normalized probability | $d\mathcal{P}(\rho_V) = \frac{\mathcal{N}(\rho_V)\,d\rho_V}{\int \mathcal{N}(\rho_V')\,d\rho_V'}$ | Eq. (9) |
| Integrated probability CDF | $\mathcal{P}(\leq \rho_V) = 1 + (1+\beta)e^{-\beta} + \frac{1}{2\ln 2 - 1}\int_\beta^\infty e^{-x} dx\left\{-2\sqrt{\beta x} + \beta + 2x\ln\left[\sqrt{\beta/x} + 1\right]\right\}$ | Eq. (10) |
| Beta parameter | $\beta \equiv \frac{1}{2\sigma^2}\left(\frac{729\,\rho_V}{500\,\rho_R}\right)^{2/3}$ | Eq. (11) |
| Slow-roll conditions | $\left\lvert\frac{V'(\phi)}{V(\phi)}\right\rvert \ll \sqrt{8\pi G}$ and $\left\lvert\frac{V''(\phi)}{V(\phi)}\right\rvert \ll 8\pi G$ | Eq. (12) |
| Slow-roll field velocity | $\dot{\phi} \simeq -\frac{t\,V'(\phi)}{1 + 3\eta}$ | Eq. (13) |
| A priori probability | $\mathcal{P}_{\text{a priori}}(V(\phi)) \propto \frac{1}{\lvert V'(\phi)\rvert}$ | Eq. (16) |
| Generic flat potential | $V(\phi) = V_1 f(\lambda\phi)$ | Eq. (17) |
| Slow-roll coupling bound | $\lambda \ll \sqrt{8\pi G}\left(\frac{\rho_V}{V_1}\right)$ | Eq. (18) |
| Anthropically allowed field range | $\lvert\phi - a/\lambda\rvert_{\max} \simeq \frac{V_{\max}}{\lambda V_1 \lvert f'(a)\rvert}$ | Eq. (19) |
| Flatness of a priori distribution | $\left\lvert\frac{V''(\phi)}{V'(\phi)}\right\rvert\,\lvert\phi - a/\lambda\rvert_{\max} \simeq \left\lvert\frac{V_{\max}}{V_1}\right\rvert \ll 1$ | Eq. (20) |
| General scalar Lagrangian | $\mathcal{L} = -\frac{Z}{2}\partial_\mu\phi\,\partial^\mu\phi - V_1 f(\phi/M)$ | Eq. (21) |

## Relevance to Phonon-Exflation

Weinberg's paper is directly relevant to the CC overshoot problem in the phonon-exflation framework. The spectral action on $M^4 \times K$ (with $K$ the Jensen-deformed SU(3) fiber) produces the zeroth Seeley-DeWitt coefficient $a_0$ as the cosmological constant and the second coefficient $a_2$ as the Einstein-Hilbert action — these are DIFFERENT spectral moments of the same Dirac operator $D_K$, not independent parameters. This structural relationship is precisely the kind of constraint that Weinberg's no-go theorem (from his 1989 review, referenced here) targets: any adjustment mechanism for $\rho_V$ must avoid the no-go by operating at a level deeper than effective field theory. The spectral action formalism does operate at this deeper level — the CC and Newton's constant are both outputs of a single eigenvalue problem, not separately tunable knobs. Weinberg's conclusion that anthropic considerations may be the only viable approach to the CC implicitly assumes that no structural mechanism connects $\rho_V$ to other physical constants; the spectral triple does exactly this, making the CC the zeroth moment of the same operator whose second moment gives gravity. The 120 OOM discrepancy that Weinberg emphasizes corresponds precisely to the spectral action's $a_0$ overshoot — the raw spectral sum over 155,984 eigenvalues gives a vacuum energy enormously larger than observed, which is the framework's key open problem (DILUTION-CC).
