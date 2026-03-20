# Review of Particle Physics (2024)

**Author(s):** S. Navas et al., Particle Data Group (PDG)
**Year:** 2024
**Journal:** Physical Review D, 110, 030001
**DOI:** 10.1103/PhysRevD.110.030001
**Website:** pdg.lbl.gov
**Summary Tables:** Included in Phys. Rev. D volume; full review available online

---

## Abstract

The 2024 Review of Particle Physics is a comprehensive reference compiling all measured properties of elementary particles and resonances. Using data from 2,717 new measurements from 869 papers published since the 2022 edition, the Review lists, evaluates, and averages measured properties of gauge bosons (W, Z, photon, gluon), the Higgs boson (discovered 2012), leptons (electron, muon, tau, neutrinos), quarks (u, d, s, c, b, t), mesons, and baryons. The Review includes 97 review articles covering specialized topics: precision electroweak tests, flavor physics, cosmology, dark matter, and particle interactions. It serves as the particle physics community's authoritative reference for all experimental results and is updated annually.

---

## Historical Context

The PDG began as a paper-based compilation in 1957, edited by A. Rosenfeld and colleagues. The goal was simple: provide a single reference for measured particle properties rather than requiring researchers to consult hundreds of journals and preprints.

Over decades, the PDG evolved:
- **1957-1975**: Paper tables, manual compilation
- **1975-2000**: Computer-generated tables, increasingly comprehensive
- **2000-2012**: Digital databases, online access, continuous updates
- **2012-2024**: Real-time databases (pdgLive), automated mass averaging, external link integration

The 2024 edition represents 67 years of accumulated experimental data. It documents the pre-discovery world (pre-2012, Higgs undiscovered), the post-Higgs era (2012-2024), and the emerging BSM constraints from the LHC.

**Role in Paasch Program**: The PDG is the ultimate experimental benchmark. Any claim that a mass formula (Paasch, Koide, Palazzi) predicts particle masses must be tested against the current PDG values—and those values change as measurements improve.

---

## Key Arguments and Derivations

### Mass Averaging Procedure

The PDG does not simply report the most recent measurement. Instead, it computes a **weighted average** of all available measurements, accounting for:

1. **Stated Uncertainty**: Each experiment reports σ_i for measurement i
2. **Systematic Errors**: Detector calibration, backgrounds, etc.
3. **Correlations**: Multiple measurements from the same experiment share systematic uncertainties
4. **Outliers**: Measurements with statistically unusual discrepancies from others are flagged or downweighted (BLUE method: Best Linear Unbiased Estimator)

For a quantity Q measured by N experiments with results Q_i ± σ_i:

$$\langle Q \rangle = \frac{\sum_i w_i Q_i}{\sum_i w_i}$$

where $w_i = 1 / σ_i^2$ (inverse variance weights).

The **resulting uncertainty** is:

$$σ_{\langle Q \rangle} = \frac{1}{\sqrt{\sum_i w_i}}$$

For highly precise measurements, this can reduce reported uncertainty below any single experiment's σ.

### Example: Tau Lepton Mass (2024)

Recent measurements by Belle II (2023), PDG compilation (2024):

| Source | m_τ (MeV) | σ (MeV) | Year |
|:-------|:----------|:--------|:-----|
| Belle II | 1776.856 | 0.074 | 2023 |
| PDG 2022 | 1776.86 | 0.12 | 2022 |
| PDG 2024 | 1776.85 | 0.09 | 2024 |

The 2024 PDG average includes Belle II's improved measurement (0.074 MeV uncertainty, the most precise tau mass to date), leading to a slightly lower central value and reduced overall uncertainty.

**Comparison with predictions**:
- Koide formula: m_τ = 1776.9688 MeV (Δ = +0.12 MeV, or ~1.3σ from PDG 2024)
- Kosinov formula: m_τ = 1776.7586 MeV (Δ = -0.09 MeV, or ~1σ from PDG 2024)
- Palazzi interpolation: m_τ ~ 1776 MeV (Δ ~ -0.85 MeV, or ~9σ—poor agreement)

### Key 2024 Updates

**Higgs Boson**:
- Mass: m_H = 125.09 ± 0.24 GeV (post-ATLAS/CMS combination 2023)
- Width: Γ_H < 4.1 MeV (95% CL, SM predicts ~4 MeV)
- Couplings: Consistent with SM to <20% across all decay channels

**Top Quark**:
- Mass: m_t = 172.74 ± 0.30 GeV (Tevatron + LHC combination)
- Width: Γ_t = 2.00 ± 0.29 GeV
- Production rate: Consistent with NNLO QCD predictions

**W Boson**:
- Mass: m_W = 80.369 ± 0.017 GeV (2024 update from CDF 2022 measurement, slight tension with SM)
- Width: Γ_W = 2.085 ± 0.042 GeV

**Bottom and Charm Quarks**:
- m_b = 4.18 ± 0.04 GeV (running mass at μ = m_b)
- m_c = 1.27 ± 0.02 GeV
- Both subject to scale-dependence in QCD; reported at conventional scales

**Neutrino Masses**:
- m_{ν_1} + m_{ν_2} + m_{ν_3} < 0.12 eV (95% CL from cosmology, tritium beta decay)
- Mass splittings: Δm²_{23} = 2.453 ± 0.034 × 10^{-3} eV² (normal hierarchy)

### Precision Electroweak Tests

The SM has been tested at sub-percent precision:

- **sin²θ_W (weak mixing angle)**: 0.2249 ± 0.0005 from electron-positron collisions at Z pole (LEP, 1989-2000)
- **α_s (strong coupling)**: 0.1179 ± 0.0010 from multiple processes (tau decay, deep inelastic scattering, jet production, Higgs width)
- **α (fine-structure constant)**: 1/137.035999084 ± 21 (precision from Rydberg constant and atomic physics)

These precisions are some of the most stringent tests of any physical theory.

### Flavor Physics

The 2024 PDG includes extensive flavor-changing neutral current (FCNC) measurements and lepton universality tests:

- **B → K*μμ** (angular observables): Slight tensions (~2σ) with SM in forward-backward asymmetry
- **R_K (≡ BR(B→Kμμ)/BR(B→Kee))**: Measurement 2022 = 0.846 ± 0.060, SM = 1.0, ~2.6σ deviation
- **g-2 electron**: Discrepancy between theory and experiment resolved; tension with muon g-2 remains at 4.8σ

### Dark Matter & Cosmology

The PDG 2024 includes:
- **Axion searches**: Upper limits on axion mass and coupling from direct detection (CAST, ADMX)
- **Dark matter relic density**: Ω_DM h² = 0.120 ± 0.001 (Planck CMB)
- **Baryon asymmetry**: Y_B = (8.7 ± 0.1) × 10^{-11} (CMB + BBN)

---

## Key Results

1. **Comprehensive Experimental Reference**: The 2024 PDG documents >100 fundamental particles and resonances with precision ranging from 0.001% (electron mass, fine-structure constant) to orders of magnitude (heavy baryon widths).

2. **SM Validation**: All precision electroweak tests confirm the SM to sub-percent accuracy. No significant deviations except:
   - Muon g-2 (4.8σ tension)
   - B → Kμμ anomalies (2-2.6σ)
   - H₀ tension (5σ, but cosmological, not particle physics)

3. **Higgs Properties Locked Down**: The 2012-2024 measurements have pinned Higgs mass, couplings, and width. The Higgs is the final major discovery; searches now focus on rare decays and BSM modifications.

4. **Neutrino Mass Hierarchy Narrowing**: Future oscillation measurements and cosmology will soon determine whether masses follow normal (m₁ < m₂ < m₃) or inverted (m₃ < m₁ ~ m₂) hierarchy.

5. **Top Quark Precision Growing**: m_t measured to 0.17% precision (172.74 ± 0.30 GeV). RG evolution of weak-scale couplings depends critically on m_t; continued precision improvements matter for high-scale unification tests.

---

## Impact and Legacy

The PDG is cited in nearly every particle physics paper published. It is:
- The standard reference in graduate particle physics courses
- The benchmark for beyond-SM model building (do predicted particles exist? at what mass?)
- The experimental constraint on precision electroweak fits (global χ² tests of new physics)

The annual PDG update is eagerly awaited by the community; any significant change in measured values (e.g., Belle II tau mass improvement, CDF W mass tension) cascades through the field.

---

## Connection to Phonon-Exflation Framework

**Direct connection: CRITICAL validation target**

The phonon-exflation framework makes predictions for *all* fundamental particle masses. These predictions must be tested against the PDG 2024 values:

### Mass Predictions to Test

Paasch's formula (or spectral action loop expansion) should predict:

| Particle | PDG 2024 (MeV) | Framework Prediction | Discrepancy |
|:---------|:----------------|:-------------------|:-----------|
| e | 0.5109989 | ? | ? |
| μ | 105.6583 | ? | ? |
| τ | 1776.85 ± 0.09 | ? | ? |
| u | 2.16⁺⁰·⁴⁹₋₀.₄₉ | ? | ? |
| d | 4.67⁺⁰·⁴₋₀.₃₁ | ? | ? |
| s | 93 ± 11 | ? | ? |
| c | 1270 ± 20 | ? | ? |
| b | 4180 ± 40 | ? | ? |
| W | 80369 ± 17 | ? | ? |
| Z | 91187 ± 2 | ? | ? |
| H | 125090 ± 240 | ? | ? |

If the framework computes these to within PDG uncertainties (which range from 0.01% for leptons to 10% for u,d,s quarks), the framework is experimentally validated.

### Validation Procedure (Sessions 43+)

1. **Compute** mass predictions from spectral action loop corrections on M₄ × S¹ × SU(3)
2. **Compare** each prediction m_i^{pred} vs m_i^{PDG} using:
   $$\chi^2 = \sum_i \frac{(m_i^{\text{pred}} - m_i^{\text{PDG}})^2}{σ_i^2}$$
3. **Accept or Reject**:
   - χ² < # particles → framework agrees with PDG
   - χ² > 5 × # particles → framework is disfavored at >2σ

### Paasch Mass Formula vs PDG

Paasch's original work (1970s-1980s) claimed m_i = m_0 (1 + s n_i^4)^a for generation-dependent discrete numbers n_i. Updating this formula against PDG 2024 values:

**For leptons**:
- m_e = 0.511 MeV (n = 1)
- m_μ = 105.66 MeV (n = 2) → ratio = 206.8
- m_τ = 1776.85 MeV (n = 3) → ratio to m_μ = 16.82

If m ∝ n^a, then:
$$\frac{m_τ}{m_μ} = \left(\frac{3}{2}\right)^a = 16.82 \quad \Rightarrow \quad a ≈ 5.3$$

But m_μ/m_e = 206.8 = (2)^a → a ≈ 7.7 (inconsistent).

This suggests Paasch's simple power law *fails* for leptons and requires refinement. The framework's spectral action loop expansion should provide the correction.

### Experimental Priorities (2024-2025)

Measurements most relevant to Paasch/framework validation:
1. **Belle II tau mass** (2024 precision: 0.074 MeV) — pins down τ sector
2. **LHCb b-quark precision** — improving m_b determinations
3. **Future collider m_t** — Electron-Positron Collider (ILC/CLIC) will measure m_t to 0.1% via threshold scans
4. **Neutrino mass hierarchy** — oscillation + cosmology in 2025-2030 will determine ordering

If the framework can match PDG 2024 values to <1%, it achieves the status of a viable mass generation mechanism.

---

## References

- Navas, S., et al. (Particle Data Group). (2024). "Review of Particle Physics." Physical Review D 110, 030001.
- Workman, R.L., et al. (PDG Collaboration). (2022). "Review of Particle Physics." Progress of Theoretical Physics Supplement 203, 1-1.
- ATLAS & CMS Collaborations. (2023). "A combination of measurements of the Higgs boson mass and the test of compatibility between its couplings and the Standard Model predictions." arXiv:2308.16188.
- Zyla, P.A., et al. (PDG Collaboration). (2020). "Review of Particle Physics." Progress of Theoretical and Experimental Physics 2020(8), 083C01.

---

## Appendix: PDG 2024 Quark Mass Values at μ = 2 GeV

| Quark | Running Mass (MeV) | Uncertainty | Note |
|:------|:------------------|:-----------|:-----|
| u | 2.16 | +0.49, -0.49 | Relatively large uncertainty |
| d | 4.67 | +0.41, -0.31 | Light quark mixing |
| s | 93 | ± 11 | From K meson data |
| c | 1270 | ± 20 | From D meson |
| b | 4180 | ± 40 | 3× uncertainty of c |
| t | 172.74 | ± 0.30 | GeV scale; pole mass ~ 163 GeV |

**Note**: Light quark masses (u, d, s) depend on the renormalization scale μ and scheme (MS vs pole mass). PDG quotes running masses at μ = 2 GeV in the MS̄ scheme. The uncertainties reflect current lattice QCD and experimental constraints.
