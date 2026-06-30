# MICROSCOPE Mission: Final Results of the Test of the Equivalence Principle

**Author(s):** Pierre Touboul, Gilles Metris, Manuel Rodrigues, Joel Berge, Alain Robert, Quentin Baghi, Yves Andre, Judicael Bedouet, Damien Boulanger, Stefanie Bremer, Patrice Carle, Ratana Chhun, Bruno Christophe, Valerio Cipolla, Thibault Damour, Pascale Danto, Louis Demange, Hansjoerg Dittus, Oceane Dhuicque, Pierre Fayet, Bernard Foulon, Pierre-Yves Guidotti, Daniel Hagedorn, Emilie Hardy, Phuong-Anh Huynh, Patrick Kayser, Stephanie Lala, Claus Lammerzahl, Vincent Lebat, Francoise Liorzou, Meike List, Frank Loffler, Isabelle Panet, Martin Pernot-Borras, Laurent Perraud, Sandrine Pires, Benjamin Pouilloux, Pascal Prieur, Alexandre Rebray, Serge Reynaud, Benny Rievers, Hanns Selig, Laura Serron, Timothy Sumner, Nicolas Tanguy, Patrizia Torresi, and Pieter Visser
**Year:** 2022
**Journal:** Physical Review Letters (published); also Classical and Quantum Gravity companion papers
**arXiv:** 2209.15487
**Relevance:** CRITICAL

---

## Abstract

The MICROSCOPE mission was designed to test the Weak Equivalence Principle (WEP), stating the equality between the inertial and the gravitational masses, with a precision of $10^{-15}$ in terms of the Eotvos ratio $\eta$. Its experimental test consisted of comparing the accelerations undergone by two collocated test masses of different compositions as they orbited the Earth, by measuring the electrostatic forces required to keep them in relative equilibrium. This was done with ultra-sensitive differential electrostatic accelerometers onboard a drag-free satellite. The mission lasted two and a half years, cumulating five-months-worth of science free-fall data, two thirds with a pair of test masses of different compositions -- Titanium and Platinum alloys -- and the last third with a reference pair of test masses of the same composition -- Platinum. We summarize the data analysis, with an emphasis on the characterization of the systematic uncertainties due to thermal instabilities and on the correction of short-lived events which could mimic a WEP violation signal. We found no violation of the WEP, with the Eotvos parameter of the Titanium and Platinum pair constrained to $\delta(\text{Ti},\text{Pt}) = [-1.5 \pm 2.3~(\text{stat}) \pm 1.5~(\text{syst})] \times 10^{-15}$ at $1\sigma$ in statistical errors.

---

## Key Arguments and Derivations

### 1. Experimental Concept

MICROSCOPE tests the WEP by comparing the accelerations of two collocated test masses of different composition in Earth orbit. The Eotvos ratio is defined as:
$$\eta_{A,B} = 2\frac{a_A - a_B}{a_A + a_B} \approx \left(\frac{m_g}{m_i}\right)_A - \left(\frac{m_g}{m_i}\right)_B = \delta(A,B)$$

Two sensor units are used: SUREF (two Platinum-Rhodium test masses, same composition -- reference) and SUEP (Platinum-Rhodium inner mass + Titanium-Aluminum-Vanadium outer mass -- EP test).

### 2. Measurement Principle

The satellite orbits in a sun-synchronous, dawn-dusk orbit at ~700 km altitude. The test masses are controlled by electrostatic forces to maintain equilibrium. The differential acceleration is measured along the sensitive $x$-axis. The satellite can be spun around the $y$-axis to increase the modulation frequency of the Earth's gravitational signal. A WEP violation would produce a signal at the EP frequency $f_{\text{EP}}$ (the sum of orbital and spin frequencies).

The projected measurement equation on the sensitive axis is:
$$\Gamma_{d,x}^{\text{corr}} = \tilde{b}_{0,d,x} + \delta_x g_x + \delta_z g_z + \Delta_x S_{xx} + \Delta_z S_{xz} + n_{d,x}$$
where $\delta_x$ is the Eotvos parameter, $g_x$ is the Earth gravity projection, and $n_{d,x}$ is noise.

### 3. Calibration and Systematic Error Budget

Instrumental defects are parameterized by off-centerings ($\Delta_x$, $\Delta_y$, $\Delta_z$), sensitivity matrices ($[A_d]$, $[A_c]$), and coupling matrices ($[C_d]$). Off-centerings $\Delta_x$ and $\Delta_z$ are estimated from science data using the Earth gravity gradient at $2f_{\text{EP}}$. Dedicated calibration sessions estimate other parameters by shaking the satellite at frequency $f_{\text{cal}}$.

**Temperature variations** are the dominant systematic error source. The thermal sensitivity of the sensor unit and front-end electronics was characterized through dedicated sessions with on-board heaters. Temperature variations at $f_{\text{EP}}$ are attenuated by a factor of $\sim 500$ between the external radiator and the sensor unit.

### 4. Glitch Handling

Short-lived "glitches" (likely from crackles in the satellite's multi-layer insulator) can mimic a WEP violation signal at $f_{\text{EP}}$. A recursive $\sigma$-clipping technique identifies outliers, and a masking window (1 second before, 15 seconds after each outlier) removes transients. The M-ECM (Modified-Expectation-Conditional-Maximization) technique handles the resulting unevenly-sampled data by maximizing the likelihood through conditional expectation of missing data.

### 5. Final Results

The combined result from eighteen SUEP sessions and nine SUREF sessions:
- **SUEP**: $\delta(\text{Ti},\text{Pt}) = [-1.5 \pm 2.3~(\text{stat}) \pm 1.5~(\text{syst})] \times 10^{-15}$
- **SUREF**: $\delta(\text{Pt},\text{Pt}) = [0.0 \pm 1.1~(\text{stat}) \pm 2.3~(\text{syst})] \times 10^{-15}$

The null result of SUREF confirms no unaccounted systematic errors in the SUEP measurement. The overall systematics upper bound is $1.5 \times 10^{-15}$ for SUEP. This improves previous constraints by a factor of 4.6 and approaches the designed $10^{-15}$ precision.

### 6. Implications for New Physics

The result constrains extensions of GR involving new long-range forces. In theories with a light spin-0 boson (dilaton from string theory) or a spin-1 boson $U$ coupled to baryon number, leptonic number, or electromagnetic currents, MICROSCOPE places unprecedented limits on coupling strengths. The paper notes that if the EP is violated, it would signal new interactions beyond the standard model of particle physics.

---

## Key Results

1. $\delta(\text{Ti},\text{Pt}) = [-1.5 \pm 2.3~(\text{stat}) \pm 1.5~(\text{syst})] \times 10^{-15}$ -- no WEP violation detected.
2. Reference instrument null result: $\delta(\text{Pt},\text{Pt}) = [0.0 \pm 1.1~(\text{stat}) \pm 2.3~(\text{syst})] \times 10^{-15}$.
3. Improvement by factor 4.6 over first MICROSCOPE results (2017).
4. Tightest bound on WEP validity achieved to date (as of 2022).
5. Systematic errors dominated by temperature variations (thermal sensitivity characterized via dedicated sessions).
6. Glitch correction technique (M-ECM) validated with mock violation signals.
7. Constrains long-range interactions from dilaton or $U$-boson models.

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Eotvos ratio | $\eta_{A,B} = 2(a_A - a_B)/(a_A + a_B) \approx (m_g/m_i)_A - (m_g/m_i)_B$ | Eqs. (1)-(2) |
| Measurement equation | $\vec{\Gamma}_d^{\text{meas}} = \vec{K}_{0,d} + [A_c]([T] - [I_n])\vec{\Delta} + \ldots + \delta(2,1)\vec{g}_{\text{sat}} + 2[A_d]\vec{\Gamma}_c^{\text{app}} + \vec{n}_d$ | Eq. (3) |
| Corrected model | $\Gamma_{d,x}^{\text{corr}} = \tilde{b}_{0,d,x} + \delta_x g_x + \delta_z g_z + \Delta_x S_{xx} + \Delta_z S_{xz} + n_{d,x}$ | Eq. (4) |
| Final EP constraint | $\delta(\text{Ti},\text{Pt}) = [-1.5 \pm 2.3~(\text{stat}) \pm 1.5~(\text{syst})] \times 10^{-15}$ | Eq. (5) |
| EP frequency (V2 mode) | $f_{\text{EP2}} = f_{\text{orb}} + f_{\text{spin2}} = 0.92499 \times 10^{-3}$ Hz | Table II |
| EP frequency (V3 mode) | $f_{\text{EP3}} = f_{\text{orb}} + f_{\text{spin3}} = 3.11133 \times 10^{-3}$ Hz | Table II |

---

## Relevance to Phonon-Exflation

This paper provides the tightest experimental constraint on the Weak Equivalence Principle, directly setting the precision floor that the phonon-exflation framework must satisfy. The framework's M4 $\times$ SU(3) geometry predicts that the internal fiber modulus $\tau$ is frozen at a universal value independent of composition. Any composition-dependent shift in the effective gravitational mass arising from the SU(3) fiber would manifest as an Eotvos ratio $\delta \neq 0$. The MICROSCOPE result demands $|\delta| < 10^{-15}$, which the framework interprets as requiring exact effacement of the SU(3) modulus from gravitational dynamics -- a condition the block-diagonal theorem ($[D_K]$ independent of external environment) is designed to guarantee.
