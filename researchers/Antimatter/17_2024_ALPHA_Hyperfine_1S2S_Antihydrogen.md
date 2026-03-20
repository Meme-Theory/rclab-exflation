# Precision Spectroscopy of the Hyperfine Components of the 1S-2S Transition in Antihydrogen

**Authors:** ALPHA Collaboration (M. Ahmadi, B. X. R. Alves, C. J. Baker, et al.)
**Year:** 2024
**Journal:** Nature Physics 20, 749–754 (2024)
**DOI:** 10.1038/s41567-024-02712-9

---

## Abstract

The ALPHA collaboration reports the first measurement of **both hyperfine components** of the 1S-2S transition in antihydrogen using stimulated Raman excitation. The measurement achieves a precision of approximately 50 MHz (parts per billion relative to the transition frequency), a 70-fold improvement over the previous best measurement. From the measured transition frequencies, we extract the antihydrogen ground-state hyperfine splitting, Δν_hfs(anti-H) = 1420.4051 ± 0.0029 GHz, and compare it with hydrogen. No statistically significant deviation from CPT (charge-parity-time) symmetry is observed, placing the most stringent limit to date on CPT-violating parameters in the lepton sector, specifically the SME coefficients (b_μ) for the electron and positron. The result constrains new physics beyond the Standard Model at the level of 10^(-16), nearly two orders of magnitude below previous bounds.

---

## Historical Context

CPT symmetry—the combination of charge conjugation (C), parity inversion (P), and time reversal (T)—is one of the most fundamental principles of quantum field theory. It was proven as a theorem (Lüders-Pauli, 1954) that any local, Lorentz-invariant quantum field theory must respect CPT. However, string theory and other theories beyond the Standard Model propose mechanisms that could violate CPT at the Planck scale, with small residual effects at low energies. Testing CPT experimentally requires comparing identical particles and their antiparticles with unprecedented precision. Antihydrogen—the antimatter counterpart of hydrogen—is ideal for this test because (1) it can be produced and trapped magnetically (unlike other antimatter species), (2) its spectroscopy can be performed with the same techniques as hydrogen, and (3) a measurement to 10^(-10) precision would probe physics at tera-electron-volt energy scales. The ALPHA experiment, launched in 2010, spent over a decade developing trap technology and cooling methods to make such measurements possible. The 2024 hyperfine result represents the culmination of these efforts, using Raman spectroscopy (resonant two-photon excitation via an intermediate state) to achieve 50 MHz precision on a 1420 GHz transition—a relative precision of 3.5 × 10^(-11).

---

## Key Arguments and Derivations

### Experimental Setup: Magneto-Optical Trap (MOT) for Antihydrogen

**Antihydrogen production and trapping:**

The ALPHA apparatus produces antihydrogen via charge-exchange collisions between antiprotons and positrons in the ultra-high-vacuum environment of the ALPHA trap:

$$\bar{p} + e^+ \rightarrow \bar{H} + \gamma$$

The antihydrogen atoms are born with kinetic energy ~5-10 eV. To trap them, the experiment uses a **Penning-Malmberg trap** (radial electric and axial magnetic confinement) combined with a **superconducting octupole magnetic field** providing a magnetic bottle at the ends. Antihydrogen atoms, with magnetic moment μ ≈ 1.4 Bohr magnetons, are confined to regions of low field strength (field-free region near the trap center).

Temperatures achieved: ~30 mK (from evaporative cooling of trapped antimatter). Typical number of antihydrogen atoms in trap: 500–5000 per cycle.

### Hyperfine Structure and the 1S-2S Transition

The 1S ground state of hydrogen (and antihydrogen) has hyperfine splitting due to the magnetic interaction between the electron (or positron) magnetic moment and the nuclear (or antiproton) magnetic moment:

$$\Delta E_{hfs} = \frac{8}{3} \frac{\alpha^2 m_e c^2}{(1 + m_e/M)^3} \frac{\mu_N \mu_e}{c^2} \frac{1}{I(I+1)}$$

For hydrogen-1 (I = 1/2 for proton), this gives Δν_hfs ≈ 1420.4 GHz, corresponding to the famous **21-cm line** used in radio astronomy.

The 1S state splits into two hyperfine levels:
- **1S, F = 0** (antiparallel spins, lower energy)
- **1S, F = 1** (parallel spins, upper energy)

The **1S-2S transition** is a two-photon excitation:

$$|1S, F\rangle + 2 \hbar \omega_{Lyman} \rightarrow |2S, F\rangle$$

where ω_Lyman ≈ 3 × 10^15 rad/s (UV, λ ≈ 121.6 nm).

**Two hyperfine components**: Because the 2S state also has hyperfine splitting (though smaller due to reduced hyperfine constant in the 2S orbital), there are multiple possible 1S-2S transitions:

1. (1S, F=0) → (2S, F=0)
2. (1S, F=0) → (2S, F=1)
3. (1S, F=1) → (2S, F=0)
4. (1S, F=1) → (2S, F=1)

Selection rules (Δ F = 0, ±1 for two-photon, parity-allowed transitions) and experimental resolution typically yield **two dominant lines** separated by ~10 GHz, corresponding to the two hyperfine components of the 1S state.

### Stimulated Raman Excitation

Rather than direct two-photon absorption at 121.6 nm (difficult to generate stably), the ALPHA collaboration uses **stimulated Raman excitation**:

$$|1S\rangle \xrightarrow{L_1} |{\text{virtual intermediate}}\rangle \xrightarrow{L_2} |2S\rangle$$

Two laser beams (frequencies ω₁ and ω₂) are applied simultaneously, exciting via an off-resonant intermediate state. The effective two-photon detuning is:

$$\Delta = (2\hbar\omega_{1S \to 2S}) - \hbar(\omega_1 + \omega_2)$$

By tuning ω₁ and ω₂ (derived from a single master laser via frequency shifting), resonance occurs when Δ = 0, i.e., when the two-photon frequency matches the 1S-2S gap.

**Advantages over direct absorption:**
- Both photons can be in the visible/near-UV (easily generated and stabilized).
- Rabi oscillations allow precision measurement via coherent manipulation.
- Background from single-photon ionization is suppressed.

### Measurement Protocol

1. **Prepare antihydrogen**: Cool to ~30 mK in the trap.
2. **Scan Raman frequency**: Vary (ω₁ + ω₂)/2 in small steps, recording resonance signal.
3. **Detect transitions**: Atoms excited to 2S are field-ionized (weak electric field pulse), and positrons are detected by silicon detectors.
4. **Extract peak center**: Fit Lorentzian lineshape to resonance curve (natural linewidth ~100 Hz, broadened to ~1 MHz by Stark effect and beam spectral width).
5. **Average multiple measurements**: 1000s of antihydrogen events per frequency point, repeated over many weeks, allowing statistical errors to drop to ~50 MHz.

**Two peaks resolve separately:**

The two hyperfine components have different 1S-2S transition frequencies because of the different F values and resulting different hyperfine structures in the 2S state:

$$\nu_{1S(F=0) \to 2S} \approx \nu_0 + \Delta \nu_{hfs}^{(2S)} \cdot c_0$$
$$\nu_{1S(F=1) \to 2S} \approx \nu_0 + \Delta \nu_{hfs}^{(2S)} \cdot c_1$$

where c₀, c₁ are coefficients of order 1, and the difference ~10 GHz is resolved.

### Extracting the Hyperfine Splitting

From the two resolved peak frequencies, the **ground-state (1S) hyperfine splitting** is extracted via a model-dependent but robust relation:

$$\Delta \nu_{1S}^{hfs} = f(\nu_1, \nu_2, a_{2S})$$

where a_{2S} is the hyperfine constant of the 2S state (known from hydrogen with high precision), and ν₁, ν₂ are the two measured peaks.

**Result (2024)**:

$$\Delta \nu_{hfs}(\bar{H}) = 1420.4051 \pm 0.0029 \text{ GHz}$$

**Comparison with hydrogen:**

$$\Delta \nu_{hfs}(H) = 1420.405751768... \text{ GHz (CODATA)}$$

**Difference:**

$$\Delta \nu_{hfs}(H) - \Delta \nu_{hfs}(\bar{H}) = 0.000651 \text{ GHz} \pm 0.0029 \text{ GHz}$$

$$= 651 \text{ kHz} \pm 2.9 \text{ MHz}$$

The error bar (~3 MHz) is consistent with statistical and systematic errors. The observed difference is consistent with **zero** to within ~0.22 standard deviations—no significant CPT violation detected.

### CPT Violation Constraints: SME Coefficients

If CPT is violated, the Standard Model Extension (SME) parametrizes the deviation as a Lorentz-invariant but CPT-odd term in the Lagrangian:

$$\mathcal{L}_{CPT-odd} = b_\mu \bar{\psi} \gamma^\mu \gamma^5 \psi$$

where b_μ is a background four-vector (fixed in the cosmic rest frame) and ψ is the fermion field.

For electrons (in hydrogen) and positrons (in antihydrogen), the SME coefficients are:

$$b_e, \quad b_{\bar{e}}$$

The CPT-violating energy shift is:

$$\delta E = (b_e^0 - b_{\bar{e}}^0) \cdot c$$

(only the time component contributes to energy; spatial components decouple due to rest-frame kinematics).

**Constraint:**

$$|b_e^0 - b_{\bar{e}}^0| < 2 \times 10^{-25} \text{ GeV}$$

(This limit is ~200 times better than previous bounds from the 1S-2S transition in hydrogen alone, and ~100 times better than muon-based constraints from muonium.)

---

## Key Results

1. **First measurement of both hyperfine components in antihydrogen**: 1S(F=0)-2S and 1S(F=1)-2S transitions resolved to ~50 MHz precision each.

2. **Antihydrogen hyperfine splitting measured**: Δν_hfs(anti-H) = 1420.4051 ± 0.0029 GHz, achieving 10^(-11) relative precision.

3. **No CPT violation detected**: Measured value agrees with hydrogen value to within experimental error (650 ± 2900 kHz difference, consistent with zero).

4. **SME coefficient limit**: |b_e^0 - b_{\bar{e}}^0| < 2 × 10^(-25) GeV, constraining CPT violation at 10^(-16) level (parts per quadrillion).

5. **Technology milestone**: Demonstrates that antihydrogen spectroscopy can achieve precision competitive with hydrogen, opening door to future 1S-2S measurements at even higher precision (target: 10^(-12) via laser frequency stabilization).

6. **Magnetic moment bound**: Ratio of antiproton to proton magnetic moments tested to <10^(-9) precision (indirect from hyperfine).

---

## Impact and Legacy

- **Fundamental tests of CPT**: Sets the most stringent laboratory limit on CPT-violating parameters in the lepton sector as of 2024.
- **Antimatter physics maturation**: Demonstrates that antimatter atoms can be spectroscopically studied with precision equal to matter. Opens path to tests of other fundamental symmetries (Lorentz invariance, CPT in different sectors).
- **Standard Model validation**: Provides no evidence for beyond-SM physics at 10^(-16) scales, placing constraints on various BSM models (extra dimensions, string theory axions, etc.).
- **Nextgen experiments**: Inspires plans for even higher precision (MUSASHI in Japan, GBAR in CERN, antihydrogen laser spectroscopy with improved cooling).
- **Gravity tests**: Antihydrogen in free fall is a candidate for testing the weak equivalence principle for antimatter (AEGIS experiment).

---

## Connection to Phonon-Exflation Framework

**Indirect but significant.** CPT symmetry is hardwired into the framework:

1. **[J, D_K] = 0 theorem (Session 17a, permanent)**: The framework's fermionic Dirac operator D_K commutes with the chirality operator J = γ_F γ_PA γ_CHI, encoding CPT protection algebraically.
   - No matter the metric evolution (parameterized by τ), CPT cannot spontaneously break.
   - This algebraic protection parallels the experimental robustness shown by ALPHA: even with extreme precision, no CPT violation appears.

2. **Antimatter sector**: The phonon-exflation framework includes both particles and antiparticles (pairs of real spectral triples in the Wick-rotated formulation).
   - ALPHA's measurement of antihydrogen hyperfine structure is a direct observable test of whether the antiparticle sector behaves as the framework predicts.
   - If [J, D_K] = 0 is exact, the hyperfine splitting must be identical for H and anti-H (modulo μ≠0 corrections, which the framework expects are small).

3. **BDI protection of CPT**: In the BDI topological classification (Papers 15, 16), the chiral symmetry {S, H} = 0 is intimately linked to CPT.
   - Session 35 proved [iK_7, D_K] = 0 (no mixing across chiral sectors), strengthening the algebraic case for CPT permanence.

4. **Pfaffian sign as CPT witness**: The Pfaffian Pf(D_K) = -1 (Sessions 17c, 34) is a CPT-odd topological invariant. Its sign is invariant under CPT but changes under CPT violation.
   - ALPHA's null result (no CPT violation) is consistent with the framework's assumption Pf(D_K) = const.

5. **Cosmic implications**: If the framework is correct, then CPT violation should be absent at laboratory scales (as ALPHA confirms) and also absent at all observable scales in the early universe during the transit.
   - Session 38's result that the instanton gas preserves the GGE topology (no dissipation of topological charge) relies on CPT holding throughout.

**Summary**: ALPHA provides empirical validation that the foundational assumption [J, D_K] = 0 (CPT conservation) is robust, supporting the theoretical framework at one of its most basic levels.

