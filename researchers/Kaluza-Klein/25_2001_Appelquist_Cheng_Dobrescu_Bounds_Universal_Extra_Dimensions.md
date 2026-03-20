# Bounds on Universal Extra Dimensions

**Author(s):** Thomas Appelquist, Hsin-Chia Cheng, Bogdan A. Dobrescu

**Year:** 2001

**Journal:** Physical Review D 64:035002; arXiv:hep-ph/0012100

---

## Abstract

We derive experimental constraints on Universal Extra Dimensions (UED) models where all Standard Model fields propagate in the bulk of compact extra dimensions. We compute the virtual effects of Kaluza-Klein states on precision electroweak observables (S and T parameters), weak decay processes, and flavor-changing neutral currents. The primary constraint arises from weak-isospin violation effects entering at one-loop order. We find that the lower bound on the compactification scale (inverse of the extra dimension radius) depends strongly on the number of extra dimensions: for one additional dimension, $1/R > 350$ GeV at 95% CL; for two dimensions, $1/R > 400$ GeV; for three dimensions, $1/R > 500$ GeV. These bounds are substantially weaker than naive expectations based on direct KK particle production, demonstrating that virtual effects provide the most stringent constraints on low-lying KK modes. We discuss implications for collider searches at Tevatron Run II and future hadron colliders.

---

## Historical Context

By the early 2000s, the ADD (1998) and RS (1999) models had generated significant theoretical interest in extra dimensions. However, experimental bounds were limited to collider searches (looking for direct KK particle production) and sub-millimeter gravity tests. The Appelquist-Cheng-Dobrescu paper provided the first systematic study of how precision electroweak data constrain UED models.

This was crucial because it showed that precision measurements—data already available from decades of electroweak physics experiments—were more constraining than the then-imagined direct discovery searches. The paper established a methodology: compute one-loop virtual contributions of KK states to measured processes, compare to data, and extract bounds on $1/R$.

The result was somewhat surprising: UED models with $1/R \sim 300-500$ GeV were not already ruled out by existing data. This spurred experimental activity and motivated further theoretical work on UED phenomenology.

---

## Key Arguments and Derivations

### Universal Extra Dimensions Framework

In UED, all Standard Model fields propagate in $4 + n$ dimensional spacetime:

$$\mathcal{M}_{4,n} = \mathbb{R}^{1,3} \times K^n$$

where $K^n$ is a compact $n$-dimensional space (typically $\mathbb{T}^n$, a product of circles).

Kaluza-Klein decomposition of a SM field (e.g., the electron) yields:

$$\psi(x, y) = \sum_{n_1, \ldots, n_n} \psi_{n_1,\ldots,n_n}(x) \exp\left( i \sum_a n_a y_a / R_a \right)$$

where $R_a$ are the compactification radii. For simplicity, assume all radii are equal ($R_a = R$). The KK mass of a mode is:

$$m_{n_1, \ldots, n_n}^2 = m_0^2 + \left( \sum_a n_a / R \right)^2$$

where $m_0$ is the 4D rest mass and $n_a$ are winding numbers.

The lightest non-zero KK modes have mass $\sim 1/R$.

### Precision Electroweak Constraints

The Standard Model has been tested to high precision at $e^+ e^-$ colliders (LEP), especially through Z-boson measurements. Deviations from SM predictions are parametrized by two key parameters:

$$\Delta S = 16 \pi s_w^2 c_w^2 (\Delta\rho)$$

$$\Delta T = \frac{4 s_w^2}{\alpha} \Delta\rho$$

where $c_w$, $s_w$ are the Weinberg angle cosines/sines, $\alpha$ is the fine structure constant, and $\Delta\rho$ is the fractional shift in the $\rho$ parameter (the ratio $m_W^2 / (m_Z^2 \cos^2\theta_W)$).

In the Standard Model, $S \approx 0$ and $T \approx 0$ (with small radiative corrections). Global fits to LEP and other data give:

$$S = 0.03 \pm 0.10, \quad T = 0.07 \pm 0.13$$

at 68% CL (1-sigma).

### KK Contributions to S and T

In UED, virtual KK loops contribute to $S$ and $T$. The contributions come from:

1. **Box diagrams**: Two KK leptons or quarks in a loop, exchanging a KK photon or Z boson.

2. **Penguin diagrams**: One KK fermion and one KK boson, exchanging a Standard Model particle.

3. **Self-energy corrections**: KK particles running in loops for gauge boson renormalization.

For example, the KK-electron contribution to the neutron decay amplitude includes:

$$\mathcal{A} \sim \sum_{n=1}^{\infty} \int \frac{d^4 \ell}{(2\pi)^4} \frac{1}{[\ell^2 - (1/R)^2 n^2]^2}$$

Performing the integral and summing over KK levels, one obtains:

$$\Delta S_{\text{KK}} \sim \alpha \times \frac{M_Z^2}{(1/R)^2} \times f(n_{\text{extra}})$$

where $f(n_{\text{extra}})$ is a numerical function depending on the number of extra dimensions.

For one extra dimension:

$$\Delta S_{\text{KK}} \sim 0.01 - 0.05$$

(depending on the compactification scale). For three dimensions, contributions are roughly $(1/R)^2 / n_{\text{extra}}$ times smaller.

### Weak Isospin Violation Dominance

The dominant constraint on UED comes not from $S$ and $T$ directly but from weak-isospin violation—the breaking of the $SU(2)_L$ global symmetry at loop level.

In the Standard Model, weak isospin is nearly exact at tree level. However, KK fermions break isospin through their couplings. A specific example is the KK-quark contribution to the $u$-quark and $d$-quark self-energies, which are not equal due to their different interactions with the Higgs.

The isospin-violating amplitude is:

$$\mathcal{A}_{\text{isospin}} \sim \frac{\alpha}{\sin^2\theta_W} \sum_n \frac{m_{u}^2 - m_d^2}{(1/R)^2 n^2}$$

This contribution is suppressed by the quark mass difference and the loop factor, but it is substantial for $1/R \sim 300$ GeV.

Comparing to precision data:

$$|\mathcal{A}_{\text{isospin}}| < \Delta_{\text{exp}}$$

yields:

$$1/R > 350 \text{ GeV (1D)}, \quad 1/R > 400 \text{ GeV (2D)}, \quad 1/R > 500 \text{ GeV (3D)}$$

---

## Key Results

1. **Compactification scale bounds**:
   - 1 extra dimension: $1/R > 350$ GeV (95% CL)
   - 2 extra dimensions: $1/R > 400$ GeV
   - 3 extra dimensions: $1/R > 500$ GeV

2. **Precision constraints dominate**: Precision electroweak data provide tighter bounds than direct KK production searches at Tevatron (which were not sensitive to KK resonances below ~1 TeV).

3. **Weak isospin violation is the primary constraint**: Loop contributions to weak isospin-violating processes outweigh $S$ and $T$ parameter shifts.

4. **N-dimension scaling**: The bound scales roughly as $(1/R)_{\text{bound}} \sim 350 \text{ GeV} \times \sqrt{n}$, indicating that more extra dimensions are less constrained individually (the KK density of states is lower).

5. **Collider signatures**: With $1/R \sim 300-500$ GeV, direct KK particle production (e.g., $q \bar{q} \to g^{(1)} \bar{g}^{(1)}$) is within Tevatron Run II reach (~2 TeV center-of-mass energy), but signal rates are small due to limited phase space.

6. **Flavor physics**: Additional constraints from rare decays (e.g., $K_L \to \mu^+ \mu^-$, $B \to X_s \gamma$) provide complementary bounds, though precision electroweak remains the strongest.

---

## Impact and Legacy

The Appelquist-Cheng-Dobrescu paper established the standard methodology for constraining UED:

- **Precision electroweak as a tool**: Subsequent analyses used S, T, and other oblique parameters to constrain BSM physics, including many extra-dimensional scenarios.
- **Tevatron searches**: Experiments at Fermilab searched for KK particle resonances and missing energy signatures predicted by UED.
- **LHC constraints**: With $\sqrt{s} = 7-13$ TeV, LHC searches dramatically improved bounds: $1/R > 1.3$ TeV (2011) to $1/R > 2.0$ TeV (2016) for certain scenarios.
- **Flavor physics**: The paper motivated detailed studies of KK-mediated flavor-changing neutral currents.
- **Model building**: The bounds guided theorists in constructing viable BSM scenarios with extra dimensions that avoid precision constraints.

---

## Connection to Phonon-Exflation Framework

**KK compactification scale**: Just as Appelquist et al. constrain the UED compactification scale using precision electroweak data, phonon-exflation's internal SU(3) geometry has a characteristic "compactification scale" related to the K_7 modulus and tau dynamics.

**Precision constraints as tools**: The framework's particle masses and coupling constants should ultimately be confronted with precision measurements (neutrino mixing, CKM matrix, etc.). The methodology of extracting bounds from precision data, developed in the UED literature, applies directly.

**Virtual corrections**: UED's one-loop virtual KK corrections to electroweak processes parallel the framework's spectral action one-loop corrections (van Suijlekom, 2020). Both generate finite corrections to coupling constants and masses.

**Weak isospin violation**: The framework predicts specific patterns of isospin violation through the SU(3) geometry (e.g., the generator matrices and Casimir values). Precision weak decay data could test these predictions, similar to how UED is constrained.

**Compactification phenomenology**: Both frameworks require determining a "compactification scale" or equivalent geometric parameter:
- UED: $1/R \sim 300$ GeV – 2 TeV
- Phonon-exflation: K_7 mass $\sim$ few GeV (dynamically set by BCS pairing)

**Tower of states**: UED has a dense tower of KK modes; phonon-exflation has discrete Dirac spectrum on SU(3). Both produce virtual corrections and potential new physics signatures.

**Relevance**: The Appelquist et al. paper provides a roadmap for extracting constraints on the framework from precision data. Once the phonon-exflation model makes specific quantitative predictions for weak decay rates, neutrino mixing matrix elements, and coupling constant running, precision electroweak data can constrain the internal geometry (tau, K_7 mass, SU(3) deformation).

---

## References

- Appelquist, Cheng, Dobrescu. "Bounds on Universal Extra Dimensions." Phys. Rev. D 64 (2001) 035002.
- Cheng, Dobrescu, Tait. "Cosmological and Astrophysical Constraints on Kaluza-Klein Masses." Phys. Rev. D 60 (1999) 075015.
- Dobrescu, Morrissey. "Universal Extra Dimensions and the Higgs Boson Mass." JHEP 0704 (2007) 053.
- CMS Collaboration. "Search for Resonances in the Mass Distribution of Jet Pairs with one b-tagged Jet in Proton-Proton Collisions at $\sqrt{s} = 8$ TeV." Phys. Lett. B 740 (2015) 83–104.
