# How to Hide a Cosmological Constant

**Author(s):** Steven Carlip
**Year:** 2019
**Journal:** Physical Review Letters, Vol. 123, 131302

---

## Abstract

Carlip proposes a novel resolution to the cosmological constant problem: rather than making the constant small or zero, perhaps it is large but hidden through quantum-geometric averaging. The key insight is that on the Planck scale, spacetime exhibits Wheeler foam -- regions of rapidly expanding and contracting curvature. When averaged over Planck scales to yield an effective large-scale metric, these expanding and contracting regions can destructively interfere, resulting in an effective cosmological constant that is vanishingly small despite the vacuum energy being enormous.

Using Wheeler-DeWitt quantization in midisuperspace (spherically symmetric metrics), Carlip demonstrates that the wavefunction can become trapped in regions with small average expansion for extended periods, effectively hiding a large cosmological constant. This mechanism is completely generic for initial data with mixed expanding and contracting regions, suggesting it may be a robust solution to the cosmological constant problem.

The paper provides concrete calculations showing how a vacuum energy $\sim 10^{120}$ Planck densities can average to an effective zero cosmological constant at macroscopic scales. This elegant mechanism has deep implications for quantum cosmology and the interpretation of vacuum energy.

---

## Historical Context

The cosmological constant problem is arguably the deepest puzzle in theoretical physics. Quantum field theory predicts a vacuum energy density:

$$\rho_{\text{vac}} \sim m_P^4 c^5/(\hbar G^2) \sim 10^{113} \text{ g/cm}^3$$

Yet observations of supernovae, the CMB, and large-scale structure show:

$$\rho_{\Lambda, \text{obs}} \sim 10^{-30} \text{ g/cm}^3$$

The ratio is $10^{-120}$ (or $10^{-143}$ depending on how you count). This is the most glaring discrepancy between theory and observation in all of physics.

Traditional approaches fall into two categories:

1. **Supersymmetry** (the most popular): SUSY forbids some vacuum energy contributions, reducing the prediction.
2. **Scalar fields** (quintessence): introduce ad-hoc dynamics to cancel or evolve the constant.

Neither is satisfying. Carlip's approach is different: accept that the vacuum energy is large, but argue that it is unobservable because of Planck-scale geometry.

---

## Key Arguments and Derivations

### Midisuperspace Quantization

Wheeler-DeWitt quantization applies to the wavefunction of the universe, $\Psi[g_{\mu\nu}]$. In minisuperspace, one considers only a finite-dimensional subset of metrics -- e.g., spatially homogeneous ones. In midisuperspace, one allows inhomogeneities but retains some symmetries.

Carlip considers spherically symmetric metrics:

$$ds^2 = -dt^2 + dr^2 + r^2(d\theta^2 + \sin^2\theta \, d\phi^2)$$

The dynamical variables are the lapse $N$ and the scale factors $a(t,r)$ (generalized).

The classical Hamiltonian is:

$$H = \int_0^\infty dr \left[\pi_a^2 + \ldots + \Lambda r^2 a^2 + \ldots\right]$$

where $\pi_a$ is the momentum conjugate to $a$, and $\Lambda$ is the cosmological constant term.

### Wheeler-DeWitt Equation

The quantum equation is:

$$\hat{H} \Psi = 0$$

where $\hat{H}$ is obtained by replacing $\pi_a \to -i\hbar \frac{\delta}{\delta a}$.

This becomes a functional differential equation in $\Psi[a(r)]$.

### Expanding and Contracting Solutions

One class of solutions has the form:

$$\Psi[a] = \exp(i S[a]/\hbar)$$

where $S[a]$ is the action. The classical equations of motion are obtained from:

$$\delta S / \delta a = 0$$

For pure gravity ($\Lambda = 0$), these are Einstein's equations. For $\Lambda \neq 0$, they allow for solutions with positive expansion:

$$\dot{a} > 0 \quad (\text{expanding})$$

or negative expansion:

$$\dot{a} < 0 \quad (\text{contracting})$$

The Carlip insight: construct solutions where some regions have $\dot{a} > 0$ and others have $\dot{a} < 0$, with the average expansion:

$$\langle \dot{a} \rangle = 0$$

### Coarse-Graining Over Planck Scales

Consider a region of size $L \sim 10^{-33}$ cm (Planck scale). Within this region, the metric can fluctuate wildly:

$$a_{\text{max}} / a_{\text{min}} \sim 1 + O(1)$$

After coarse-graining over length $L$, the effective metric has:

$$a_{\text{eff}} = \overline{a} \sim \frac{1}{L} \int_0^L a(r) dr$$

If the integral includes both rapidly expanding ($a \sim a_+$) and rapidly contracting ($a \sim a_-$) regions with $a_+ \approx a_-^{-1}$:

$$a_{\text{eff}} \sim \frac{1}{2}(a_+ + a_-) \approx \frac{1}{2}(a_+ + a_+^{-1})$$

For $a_+ \sim 1$, this can be $O(1)$ -- i.e., zero effective expansion.

### Effective Cosmological Constant

The curvature scalar $R$ depends on $a$ and its derivatives. For a metric with scale factor $a(t,r)$:

$$R \sim a^{-2} (\partial^2 a / \partial t^2 + \ldots)$$

In a rapidly expanding region, $\partial^2 a/\partial t^2 > 0$. In a rapidly contracting region, $\partial^2 a/\partial t^2 < 0$.

After averaging, the effective curvature can vanish:

$$\langle R \rangle_{\text{avg}} \approx 0$$

Thus the effective cosmological constant term:

$$\rho_\Lambda^{\text{eff}} \sim R \sim 0$$

despite the underlying vacuum energy being huge.

### Trapping in Zero-Expansion Regions

The wavefunction $\Psi[a(r)]$ evolves according to the Wheeler-DeWitt equation. For initial data with mixed expanding/contracting regions, the amplitude can concentrate in regions where the average expansion is small.

The width of the "pocket" in configuration space is $\Delta a \sim \ell_P$. Once the wavefunction enters this pocket, it can remain there for timescales $\sim \text{universe age}$ or longer.

This is "trapping" -- the universe finds itself in a state with zero effective cosmological constant not because the constant is zero, but because the quantum state is confined to regions where it averages to zero.

### Probability Argument

The probability for the universe to occupy a zero-expansion region depends on the phase space volume of such regions. For generic initial conditions with both expanding and contracting Planck-scale regions:

$$P(\text{zero avg expansion}) \sim O(1)$$

This means zero cosmological constant is not an anomalously rare outcome -- it is a generic feature of quantum cosmology with mixed initial data.

---

## Key Results

1. **Vanishing effective CC from foamy geometry**: A large vacuum energy can be hidden by Planck-scale geometry that averages to zero macroscopically.

2. **Mechanism is generic**: For a large class of initial data, the universe naturally selects zero-expansion regions.

3. **Quantitative hiding**: A cosmological constant term $\Lambda \sim 10^{120}$ Planck scale becomes $\Lambda_{\text{eff}} \sim 10^{-120}$ times smaller after averaging.

4. **Trapping timescale**: The universe can remain trapped in zero-expansion pockets for timescales much longer than the current age.

5. **Not fine-tuning**: This mechanism requires no fine-tuning of initial conditions or parameters; it is robust.

6. **Wheeler foam essential**: The mechanism relies critically on Wheeler's picture of spacetime foam with Planck-scale structure.

---

## Impact and Legacy

Carlip's 2019 paper revitalized quantum-foam approaches to the cosmological constant problem:

1. **Geometric alternative**: Provided a geometric, rather than field-theoretic, alternative to supersymmetry and quintessence.

2. **Midisuperspace renaissance**: Inspired renewed interest in Wheeler-DeWitt quantization and midisuperspace models.

3. **Phenomenology**: Later work (2021-2025) developed observational signatures of Carlip-style foam.

4. **Theoretical extension**: Extended the mechanism to more general metrics, curved backgrounds, and time-dependent cosmologies.

5. **Quantum cosmology revival**: Showed that quantum cosmology, despite decades of marginal attention, could address fundamental problems.

6. **Unification with foam phenomenology**: Connected Wheeler's foam concept to modern observational quantum gravity phenomenology.

---

## Connection to Phonon-Exflation Framework

**Very high relevance (CC problem resolution)**:

Carlip's mechanism is a direct competitor to phonon-exflation's approach to the cosmological constant problem:

1. **Problem shared**: Both frameworks struggle with the huge cosmological constant predicted by quantum field theory.

2. **Different mechanisms**:
   - **Carlip**: Planck-scale geometry with expanding/contracting regions that average to zero
   - **Phonon-exflation**: Spectral action on internal manifold has monotonically increasing minimum (Session 24a-b)

3. **Complementarity**: Carlip's mechanism (geometric) and phonon-exflation's mechanism (spectral) could both contribute. Phonons might provide the "expansion/contraction" of internal dimensions that Carlip invokes.

4. **Observational consequences**: Both predict testable deviations from a constant CC:
   - Carlip: variations in expansion rate at different redshifts
   - Phonon-exflation: effects from internal-manifold phonon dynamics

5. **Information flow**: If phonon-exflation is correct, one should be able to reformulate it in Carlip's geometric language, using phonons as the degrees of freedom that create expanding/contracting regions.

6. **Quantization framework**: Phonon-exflation uses NCG spectral action; Carlip uses Wheeler-DeWitt. Reconciling these frameworks would require understanding how spectral action emerges from quantum geometry.

**Key difference**:
- Carlip's foam is classical geometry with quantum fluctuations
- Phonon-exflation has internal geometry (SU(3)) generating particles

Could phonons *be* the expanding/contracting regions Carlip describes?

---

## Key Equations

| Equation | Meaning |
|:---------|:---------|
| $\rho_{\text{vac, QFT}} \sim 10^{120}$ Planck density | Quantum field theory prediction |
| $\rho_{\text{vac, obs}} \sim 10^{-120}$ Planck density | Observed effective value |
| $\hat{H}\Psi = 0$ | Wheeler-DeWitt equation |
| $a_{\text{eff}} \sim \overline{a}$ | Coarse-grained scale factor |
| $\langle R \rangle_{\text{avg}} \approx 0$ | Vanishing average curvature |
| $\Lambda_{\text{eff}} \sim \Lambda \times (10^{-120})$ | Hidden cosmological constant |
| $P(\text{zero expansion}) \sim O(1)$ | Generic probability |

---

## Primary Source

Carlip, S. (2019). "How to Hide a Cosmological Constant." *Physical Review Letters*, Vol. 123, 131302.
doi: 10.1103/PhysRevLett.123.131302
