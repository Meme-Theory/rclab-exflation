# Inflation Library

**Papers:** 16 | **Date Range:** 1997–2022 | **Domain:** Inflationary cosmology, EFT of inflation, cosmological constant problem
**Project Relevance:** Reference library for CC overshoot diagnosis — exflation's spectral action predicts vacuum energy ~120 OOM too large. These papers contain the mathematical machinery that inflation uses to handle the same energy scales.

---

## Dependency Graph

```
                    FORMALISM CORE
                    ─────────────
    [04 Brandenberger]──→ Perturbation theory foundations
           │
    [01 Baumann TASI] ──→ Full scalar/tensor derivation
           │
    [02 Lyth-Riotto] ───→ Particle physics model zoo
           │
    [03 Maldacena] ─────→ Non-Gaussianity / bispectrum
           │
    [05 Encyclopaedia] ─→ 74+ models vs data
           │
    [06 Kofman-Linde-Starobinsky] → Reheating / parametric resonance
                                          │
                    EFT FRAMEWORK           │ (energy transfer)
                    ─────────────           │
    [07 Cheung et al] ──→ Single-field EFT ←┘
           │
    [08 Senatore-Zaldarriaga] → Multifield extension
           │
    [09 Lopez Nacir et al] ──→ Dissipative extension
           │
    [10 Burgess] ───────→ UV sensitivity / hierarchy / GREFT
           │
    [11 Achúcarro-Palma] → Observational status 2022
                                          │
                    CC PROBLEM              │ (constraints)
                    ──────────             │
    [12 Weinberg] ──────→ The 120 OOM problem + no-go
           │
    [13 Bousso-Polchinski] → Landscape / discretuum
           │
    [14 Padmanabhan] ───→ Emergent gravity / vacuum weight
           │
    [15 Padilla] ───────→ Radiative instability / sequestering
           │
    [16 Planck 2018 X] ─→ n_s, r observational benchmarks
```

---

## Topic Map

### A. Inflation Formalism (Papers 01–06)
The mathematical machinery of slow-roll inflation: how quantum fluctuations become density perturbations, the Mukhanov-Sasaki equation, power spectra derivations, and post-inflation energy transfer via parametric resonance. **Start here** for the perturbation theory that exflation must reproduce or replace.

### B. Effective Field Theory of Inflation (Papers 07–11)
The symmetry-breaking operator expansion for fluctuations around quasi-de Sitter backgrounds. Controls what operators are allowed, what hierarchies arise, and how UV sensitivity propagates. **The direct analog** of the spectral action's moment hierarchy (a_0, a_2, a_4).

### C. Cosmological Constant Problem (Papers 12–15)
The 120 OOM discrepancy itself: Weinberg's formulation, no-go theorems, landscape approaches, radiative instability analysis, and proposed solutions. **The target problem** — exflation's CC overshoot is a specific instance of this general crisis.

### D. Observational Constraints (Paper 16)
Planck 2018 constraints on n_s, r, running, and model selection. The observational benchmark that both inflation and exflation must satisfy.

---

## Quick Reference

| If your task involves... | Read these | Priority |
|:---|:---|:---|
| CC overshoot / vacuum energy calculation | 12, 15, 14 | CRITICAL |
| Energy transfer at transit / reheating math | 06, 09 | CRITICAL |
| EFT operator hierarchy ↔ spectral moments | 07, 10 | CRITICAL |
| n_s prediction comparison | 16, 01, 05 | HIGH |
| Non-Gaussianity / bispectrum | 03, 07 | HIGH |
| Perturbation theory foundations | 04, 01 | HIGH |
| Landscape / discretuum / vacuum counting | 13 | MEDIUM |
| Model classification / zoo | 02, 05 | MEDIUM |
| Multifield / additional light fields | 08 | MEDIUM |
| Emergent gravity ↔ spectral action | 14 | MEDIUM |

---

## Paper Entries

### Paper 01: Baumann — TASI Lectures on Inflation [CRITICAL]
- **File**: `01_2009_Baumann_TASI_Inflation.md`
- **arXiv**: 0907.5424
- **Year**: 2009
- **Authors**: Daniel Baumann
- **Relevance**: CRITICAL
- **Tags**: slow-roll, Mukhanov equation, scalar spectrum, tensor spectrum, consistency relation, Lyth bound

### Paper 02: Lyth & Riotto — Particle Physics Models of Inflation
- **File**: `02_1999_Lyth_Riotto_Particle_Physics_Inflation.md`
- **arXiv**: hep-ph/9807278
- **Year**: 1999
- **Authors**: David H. Lyth, Antonio Riotto
- **Relevance**: HIGH
- **Tags**: eta problem, hybrid inflation, SUSY inflation, F-term, D-term, model classification

### Paper 03: Maldacena — Non-Gaussianity [CRITICAL]
- **File**: `03_2003_Maldacena_NonGaussianity.md`
- **arXiv**: astro-ph/0210603
- **Year**: 2003
- **Authors**: Juan Maldacena
- **Relevance**: CRITICAL
- **Tags**: bispectrum, in-in formalism, consistency relation, f_NL, ADM formalism, squeezed limit

### Paper 04: Brandenberger — Perturbation Theory Lectures
- **File**: `04_2003_Brandenberger_Perturbation_Lectures.md`
- **arXiv**: hep-th/0306071
- **Year**: 2003
- **Authors**: Robert H. Brandenberger
- **Relevance**: HIGH
- **Tags**: gauge-invariant perturbations, Mukhanov-Sasaki, Jeans instability, trans-Planckian

### Paper 05: Martin, Ringeval, Vennin — Encyclopaedia Inflationaris
- **File**: `05_2014_Martin_Ringeval_Vennin_Encyclopaedia.md`
- **arXiv**: 1303.3787
- **Year**: 2014
- **Authors**: Jérôme Martin, Christophe Ringeval, Vincent Vennin
- **Relevance**: MEDIUM
- **Tags**: model catalog, n_s-r plane, ASPIC, Planck confrontation, 74+ models

### Paper 06: Kofman, Linde, Starobinsky — Reheating [CRITICAL]
- **File**: `06_1997_Kofman_Linde_Starobinsky_Reheating.md`
- **arXiv**: hep-ph/9704452
- **Year**: 1997
- **Authors**: Lev Kofman, Andrei Linde, Alexei Starobinsky
- **Relevance**: CRITICAL
- **Tags**: preheating, parametric resonance, Floquet theory, broad resonance, backreaction, particle production

### Paper 07: Cheung et al — EFT of Inflation [CRITICAL]
- **File**: `07_2008_Cheung_et_al_EFT_Inflation.md`
- **arXiv**: 0709.0293
- **Year**: 2008
- **Authors**: Clifford Cheung, Paolo Creminelli, A. Liam Fitzpatrick, Jared Kaplan, Leonardo Senatore
- **Relevance**: CRITICAL
- **Tags**: unitary gauge, Goldstone boson, speed of sound, non-Gaussianity, ghost inflation, operator hierarchy

### Paper 08: Senatore & Zaldarriaga — Multifield EFT
- **File**: `08_2010_Senatore_Zaldarriaga_Multifield_EFT.md`
- **arXiv**: 1009.2093
- **Year**: 2010
- **Authors**: Leonardo Senatore, Matias Zaldarriaga
- **Relevance**: HIGH
- **Tags**: multifield, shift-symmetric, coset G/H, SUSY, additional light scalars

### Paper 09: Lopez Nacir et al — Dissipative EFT [CRITICAL]
- **File**: `09_2012_LopezNacir_et_al_Dissipative_EFT.md`
- **arXiv**: 1109.4192
- **Year**: 2012
- **Authors**: Diana Lopez Nacir, Rafael A. Porto, Leonardo Senatore, Matias Zaldarriaga
- **Relevance**: CRITICAL
- **Tags**: dissipation, friction, noise, trapped inflation, f_NL enhancement, stochastic

### Paper 10: Burgess — EFT and Inflation
- **File**: `10_2018_Burgess_EFT_Inflation.md`
- **arXiv**: 1711.10592
- **Year**: 2018
- **Authors**: C.P. Burgess
- **Relevance**: MEDIUM
- **Tags**: UV sensitivity, GREFT, power counting, naturalness, hierarchy problem, semiclassical expansion

### Paper 11: Achúcarro & Palma — Inflation Theory & Observations
- **File**: `11_2022_Achucarro_Palma_Inflation_Theory_Obs.md`
- **arXiv**: 2203.08128
- **Year**: 2022
- **Authors**: Ana Achúcarro, Gonzalo A. Palma
- **Relevance**: MEDIUM
- **Tags**: Snowmass, observational targets, r bound, f_NL, features, future experiments

### Paper 12: Weinberg — CC Problems [CRITICAL]
- **File**: `12_2000_Weinberg_CC_Problems.md`
- **arXiv**: astro-ph/0005265
- **Year**: 2000
- **Authors**: Steven Weinberg
- **Relevance**: CRITICAL
- **Tags**: 120 OOM, old CC problem, new CC problem, no-go theorem, anthropic, quintessence

### Paper 13: Bousso & Polchinski — Four-form Fluxes
- **File**: `13_2000_Bousso_Polchinski_Fourform_Fluxes.md`
- **arXiv**: hep-th/0004134
- **Year**: 2000
- **Authors**: Raphael Bousso, Joseph Polchinski
- **Relevance**: MEDIUM
- **Tags**: discretuum, landscape, four-form flux, membrane nucleation, Brown-Teitelboim, Weinberg window

### Paper 14: Padmanabhan — CC Weight of Vacuum
- **File**: `14_2003_Padmanabhan_CC_Weight_Vacuum.md`
- **arXiv**: hep-th/0212290
- **Year**: 2003
- **Authors**: T. Padmanabhan
- **Relevance**: MEDIUM
- **Tags**: emergent gravity, vacuum energy, unimodular, Planck fluctuations, Zeldovich estimate

### Paper 15: Padilla — CC Lectures [CRITICAL]
- **File**: `15_2015_Padilla_CC_Lectures.md`
- **arXiv**: 1502.05296
- **Year**: 2015
- **Authors**: Antonio Padilla
- **Relevance**: CRITICAL
- **Tags**: radiative instability, Weinberg no-go detail, sequestering, Kaloper-Padilla, fine-tuning

### Paper 16: Planck 2018 X — Constraints on Inflation [HIGH]
- **File**: `16_2020_Planck_2018_X_Inflation.md`
- **arXiv**: 1807.06211
- **Year**: 2020
- **Authors**: Planck Collaboration
- **Relevance**: HIGH
- **Tags**: n_s=0.9649, r<0.056, no running, HZ ruled out 8.4σ, plateau models favored
