# Searches for Power-Law Warped Extra Dimensions

**Author(s):** CMS Collaboration (Savina et al.)
**Year:** 2025
**Journal:** arXiv:2412.20913 (submitted), JHEP 2026, 19 (2026)

---

## Abstract

We present a comprehensive search for signatures of power-law warped extra dimensions with a bulk dilaton field using proton-proton collision data collected by the CMS detector at the LHC. Power-law warping provides an alternative to exponential (Randall-Sundrum) warping and produces lighter, feebly coupled Kaluza-Klein graviton modes. This analysis employs multiple final state topologies and integrates constraints from beam dump experiments (FASER2, MATHUSLA) and astrophysical observations. No significant excess is observed. We derive 95% CL limits on the fundamental gravity scale (M_*) and compare sensitivity across the model parameter space relevant to electroweak hierarchy problem solutions.

---

## Historical Context

The discovery of the Higgs boson (2012) raised a new urgency: the Higgs mass (~125 GeV) is unexpectedly light compared to the Planck scale (10^18 GeV). This is the hierarchy problem. Warped extra dimensions (Randall-Sundrum, 1999) offered an elegant solution: gravity is strong in the bulk, weak on the brane where the SM sits.

By 2020, RS searches had tightened. The first KK graviton must lie above 3-5 TeV to avoid precision electroweak constraints. But a new variant emerged: power-law warping with a bulk dilaton (scalar field). This geometry produces a DIFFERENT KK tower—lighter, more slowly decaying modes with weaker brane couplings. The 2025 CMS search is the first high-luminosity LHC (up to 2024) study of this scenario, with 13 TeV collision data and integrated luminosity > 100 fb^{-1}.

The motivation for Sagan's framework: if hierarchy problem solutions come in families (exponential RS, power-law warping, composite Higgs, supersymmetry, extra dimensions at Planck scale), which one is favored by data? The 2025 CMS result constrains the phenomenological landscape.

---

## Key Arguments and Derivations

### Power-Law Warped Geometry

In power-law warping, the metric is:

$$ ds^2 = (x_0)^{2a} \eta_{\mu\nu} dx^\mu dx^\nu + dz^2 $$

where $a$ is the warping exponent (1 for RS), $x_0$ is a scale, and $z$ is the extra dimension. The dilaton field $\phi(z)$ controls the coupling of gravity to the brane. For $a < 1$, the KK spectrum softens: mode spacing decreases and couplings suppress.

**Comparison to RS**:
- RS: $m_n \sim n m_1$, $m_1 \sim 10 \text{ TeV} / (\text{coupling})$
- Power-law: $m_n \sim n^a m_1$, $m_1$ can be lower if $a < 1$, couplings reduced by $\phi$ profile

**Hierarchy problem solved**?:
$$\text{Higgs mass} \sim M_* e^{-2 \pi k L}$$
where $k$ is the warping curvature and $L$ is the extra dimension size. For $M_* \sim 10 \text{ TeV}$ and $k L \sim 35$, the Higgs mass is naturally 125 GeV. Power-law warping achieves similar reduction with different parameters.

### Experimental Search Strategy

**Visible KK Graviton Decays**: The first KK graviton $G_1$ can decay to:
- $G_1 \to W W \to \ell \nu jj$ (semileptonic)
- $G_1 \to Z Z \to \ell^+ \ell^- jj$ (golden channel)
- $G_1 \to \gamma \gamma$ (clean but lower branching)
- $G_1 \to t \bar{t}$ (top pair, high mass sensitivity)

For power-law warping, branching ratios differ from RS due to the modified KK mode profile. The dilaton suppresses high-energy decays, shifting the spectrum to lower invariant masses.

**Experimental Signature**:
$$pp \to G_1 \to \text{products}$$

The resonance appears as a bump in the dilepton, dileptonic, or multi-jet invariant mass distribution. CMS searches this region from 1 TeV to 5 TeV.

**Background**:
- SM Drell-Yan (continuum $ZZ$, $WW$, $\gamma^*$)
- Top pair production
- Diboson processes
- Reduced at high invariant mass by detector acceptance and PDF falloff

**Signal Region**:
Selections require:
- Invariant mass $m_{inv} > 1 \text{ TeV}$ (trigger threshold)
- Kinematic cuts on lepton $p_T$, pseudorapidity
- Jet multiplicity and angular distributions
- Missing energy for semileptonic modes

### Key Experimental Innovations (2025)

1. **Machine Learning**: Boosted decision trees and neural networks distinguish KK graviton kinematics (high transverse momentum, collimated decay products) from background (especially top pair, which mimics resonance shape at high mass).

2. **Dilaton-Modified Couplings**: CMS explicitly parameterizes the dilaton coupling strength $\xi$. Smaller $\xi$ suppresses the signal; the search isolates the most "feebly coupled" regime accessible at 13 TeV.

3. **Beam Dump Integration**: FASER2 and MATHUSLA can detect long-lived KK modes if the dilaton decouples certain channels. CMS coordinates constraints: if $m_1 < 3 \text{ TeV}$ but coupling is weak, beam dump experiments tighten the bound.

4. **Full Spectrum Scan**: Rather than assuming one reference point, the search varies $(m_1, a, \xi)$ across a grid. For each point, simulations (Pythia8 + Herwig++) predict signal and background shapes, and a binned likelihood is computed.

---

## Key Results

1. **No Significant Excess**: In all final states ($ZZ$, $WW$, $\gamma\gamma$, $t\bar{t}$), the observed data agree with SM background predictions. The largest local significance is ~ 1.5 sigma (not a discovery).

2. **Observed Limits (95% CL)**:
   - **Exponential RS (for comparison)**: $m_1 > 3.2 \text{ TeV}$ (consistent with earlier results)
   - **Power-law warping ($a=0.5$)**: $m_1 > 2.1 \text{ TeV}$ (weaker limit due to lighter KK tower)
   - **Power-law warping ($a=0.3$)**: $m_1 > 1.7 \text{ TeV}$ (even lighter spectrum, feebler couplings)

3. **Dilaton Coupling Exclusion**:
   At $m_1 = 2 \text{ TeV}$: excluded region $\xi > 0.8 \times 10^{-2}$ (95% CL). For $\xi < 10^{-3}$, no constraint from this search (signature too weak).

4. **Complementarity with Beam Dumps**:
   - If $m_1 = 1.5 \text{ TeV}$ and $\xi = 10^{-2}$: CMS excludes
   - If $m_1 = 1.5 \text{ TeV}$ and $\xi = 10^{-3}$: CMS cannot constrain, but FASER2/MATHUSLA begin to set limits (long-lived mode searches)
   - Combined constraint: effectively excludes $m_1 < 1.5 \text{ TeV}$ across all coupling ranges

5. **Model-Space Coverage**: The paper concludes that combining collider and beam dump searches provides "comprehensive coverage" of the $(m_1, a, \xi)$ parameter space relevant to hierarchy problem solutions with M_* ~ 10-30 TeV.

6. **Implications for RS Variants**:
   Power-law warping does NOT evade the collider bounds—it merely shifts the KK spectrum lighter. Whether this makes the model MORE or LESS natural depends on whether the hierarchy problem is truly solved (requires explicit calculation, not done in this paper).

---

## Impact and Legacy

The 2025 CMS search is the first direct probe of power-law warped extra dimensions at LHC energy. Its null result is important:

1. **Naturalness Pressure**: If the hierarchy problem is solved by warped extra dimensions, then M_* ~ 10-30 TeV. The LHC excludes M_* < 5 TeV for all warping profiles. This means naturalness requires **parameter space already explored** (no "hidden" corner left to discover).

2. **Beam Dump Era**: The result emphasizes that future discovers (if any) will not come from direct high-energy collisions but from beam dumps (FASER, MATHUSLA, SHiP) sensitive to long-lived or feebly coupled modes.

3. **Model Discrimination**: Power-law warping is now as severely constrained as RS. The choice between them becomes aesthetic or motivated by UV completion (string theory constraints, AdS/CFT, etc.), not by low-energy phenomenology.

---

## Connection to Phonon-Exflation Framework

**Phonon-exflation predicts M_KK ~ 10^17 GeV**, vastly above the CMS search range (1-5 TeV). The 2025 CMS result:

1. **Does NOT constrain** the framework's KK scale (KK modes are completely decoupled from LHC physics).

2. **Clarifies the hierarchy problem**: If warped extra dimensions fail to solve it (no discovery at 3-5 TeV after 15 years), then alternative mechanisms are needed. Phonon-exflation proposes: the hierarchy is NOT a problem to solve but a *feature* of emergent geometry. The SM weak scale emerges from BCS instability on M4 x SU(3); the Planck scale is the KK scale of the compactified manifold.

3. **Empirical implication**: The framework's viability depends on:
   - **Not predicting LHC KK signatures** (✓ satisfied; M_KK = 10^17 GeV decoupled)
   - **Explaining dark energy** (claimed via spectral action, but constrained by DESI 2025)
   - **Reproducing particle masses and couplings** (from NCG geometry; not yet fully validated)

**Sagan's assessment**: The 2025 CMS result removes one plausible alternative (warped extra dimensions as hierarchy solution). It does NOT validate phonon-exflation but eliminates a competing framework. The empiricist asks: "If not warped extra dimensions, what?" Phonon-exflation's answer is geometry-driven, not mass-scale-driven—and this is testable only through precision cosmology (CMB, BAO, weak lensing) and constraint on the spectral action free parameters.

