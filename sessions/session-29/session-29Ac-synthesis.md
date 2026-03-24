# Session 29Ac Synthesis: Observational Predictions

**Date**: 2026-02-28
**Sub-session**: 29Ac (observational predictions + provocation assessment)
**Team**: phonon-sim, hawking, coordinator, baptista, hawking-2, Tesla-Resonance
**Computations**: 29c-1 (Bogoliubov spectrum), 29c-2 (k_transition), 29c-3 (CDL bounce), 29c-4 (GW spectrum)
**Gate verdicts file**: `tier0-computation/s29c_gate_verdicts.txt`
**Inputs from 29Aa/29Ab**: KC-1 through KC-5 ALL PASS. tau_cross = 0.50. t_BCS = 1.3e-41 s at M_KK = 1e16. Gi = 0.36. V_eff monotonically decreasing. L-9 first-order is the sole trapping mechanism.

---

## I. Summary

Sessions 29Aa and 29Ab established that the BCS mechanism is internally complete: the Constraint Chain passes, the backreaction is solved, the mean-field is reliable, and the first-order transition traps the modulus. Session 29Ac asks the next question: **does the mechanism predict anything observable?**

Four direct cosmological signatures were tested:

| Computation | Result | Assessment |
|:------------|:-------|:-----------|
| 29c-1 (Bogoliubov spectrum) | Non-thermal at all tau. Anti-thermal at gap edge. | MOOT -- SU(3) has no horizon; GH comparison has no physical basis. Parametric amplification, not thermal radiation. Sampling too coarse for BCS region. |
| 29c-2 (k_transition) | k = 9.4e+23 h/Mpc. 24 orders above DESI. | Correct. Structural -- inherent to any GUT-scale KK compactification. |
| 29c-3 (CDL bounce) | V_eff monotonically decreasing. No barrier. | CDL inapplicable -- formalism requires a false vacuum, which does not exist on this potential. |
| 29c-4 (GW spectrum) | f_peak = 1.3e+12 Hz. 17 orders above LISA. | Correct. M_KK-independent structural result. |

The framework's observational content lives not in these transition-epoch signatures, but in the frozen BCS state: gauge couplings, mass ratios, proton lifetime.

---

## II. 29c-1: Parametric Amplification, Not Thermal Radiation

**Script**: `tier0-computation/s29c_gibbons_hawking_temperature.py`

### The Computation

The Bogoliubov spectrum |beta_k|^2 was fit to a Bose-Einstein distribution at each tau to extract T_eff, then compared to the internal GH temperature T_GH^{int}(tau) = e^{-2tau}/pi.

| tau | T_GH^int | T_eff (BE fit) | T_eff/T_GH | R^2 of fit |
|:----|:---------|:---------------|:-----------|:-----------|
| 0.00 | 0.318 | 0.469 | 1.47 | deeply negative |
| 0.35 | 0.175 | 0.582 | 3.33 | -0.69 |
| 0.50 | 0.120 | 0.756 | 6.30 | deeply negative |
| 2.00 | 0.006 | 3.29 | 569 | deeply negative |

Mean R^2 across all tau: -72.3. The BE fit is worse than a constant at every tau. T_eff/T_GH diverges monotonically. B_k is positively correlated with omega at tau=0.50 (Pearson r = +0.74): higher-energy modes have LARGER occupation numbers. This is the signature of gap-edge parametric amplification (Parker 1969), not equilibrium horizon radiation.

**Verdict**: MOOT (test premise invalid -- GH requires a horizon; SU(3) has none). Gates P-29d and P-29g do not fire.

### Why the Question Was Wrong

The Gibbons-Hawking effect requires a cosmological event horizon. SU(3) is compact, has no boundary, no trapped surface, no event horizon. The formula T_GH = e^{-2tau}/pi is a characteristic frequency scale of the Jensen deformation -- the inverse of the SU(2) scale factor. Comparing it to T_eff extracted from a forced BE fit is comparing a geometric frequency to a statistical parameter of a non-thermal distribution. The comparison is dimensionally consistent but physically meaningless.

The universe does not produce thermal spectra from parametric amplification on a compact manifold with discrete eigenvalues. It produces **resonance patterns**. The Jensen deformation is a driven oscillator, and the Dirac modes are the cavity. Particle creation occurs when the drive frequency matches a resonant mode -- the parametric resonance condition: d(lambda_n)/d(tau) * d(tau)/dt ~ lambda_n, or equivalently, the adiabaticity parameter eta = lambda / |d(lambda)/d(tau)| drops below 1.

### Hidden Sector-Resolved Structure

The aggregate R^2 lumps 11,424 modes from 10 Peter-Weyl sectors into a single fit. This obscures the real physics. Sector-resolved analysis at tau = 0.30:

| Sector | n_modes | Pearson(omega, B_k) | R^2 (BE fit) | T_eff |
|:-------|:--------|:--------------------|:-------------|:------|
| (0,0) | 16 | +0.996 | -0.632 | 0.243 |
| (1,1) | 128 | +0.846 | -0.635 | 0.366 |
| (3,0) | 160 | +0.889 | **-0.335** | 0.437 |
| (0,3) | 160 | +0.889 | **-0.335** | 0.437 |

The (3,0)/(0,3) sectors -- precisely the BCS-active sectors from L-9 -- have the least negative R^2. Each sector has its own effective temperature because the Jensen deformation creates sector-dependent eigenfrequency profiles. There is no universal temperature.

### The Sampling Problem

The Bogoliubov coefficient data (s28a) is on a tau grid with spacing 0.1, covering [0, 2.0] with 21 points. The BCS transition occurs at tau ~ 0.35-0.50. The available grid points in this critical region are tau = 0.30, 0.40, 0.50 -- three points, with the BCS transition falling between them. Meanwhile, the spectral action data uses spacing 0.025 on [0, 0.5] with 21 points, including tau = 0.35. The finer grid was not used for the Bogoliubov computation.

Despite this, there IS structure visible: a correlation reversal from uncorrelated (tau=0, Pearson r=-0.022) to strongly positively correlated (tau=0.50, r=+0.739). The R^2 shows non-monotonic fluctuations at tau=0.60 and 0.90 that could contain real structure -- or could be sampling artifacts. At Delta_tau = 0.1, this cannot be resolved.

The right question was never "does B_k fit a BE distribution?" The right question is: within each sector, where does the adiabaticity parameter eta drop below 1, and does the resulting spectral entropy show structure near the BCS transition? The modes that are most strongly amplified should be at the gap edge, where lambda is smallest and |d(lambda)/d(tau)| is largest -- parametric resonance in the literal sense. Recomputing on the fine tau grid with sector-resolved diagnostics would map this resonance structure for the first time.

---

## III. 29c-2: The 24-Order Gap

**Script**: `tier0-computation/s29c_k_transition.py`

### The Computation

The BCS transition time t_BCS from 29b-2 was converted to a comoving wavenumber via entropy conservation (a * T = const):

| M_KK (GeV) | k_transition (h/Mpc) | Gap to DESI |
|:------------|:---------------------|:------------|
| 10^14 | 9.4e+21 | 22 orders |
| 10^16 | 9.4e+23 | 24 orders |
| 10^18 | 9.4e+25 | 26 orders |

Observable range: DESI 0.02-0.3 h/Mpc, Euclid 0.001-0.5 h/Mpc.

**Verdict**: FAIL (STRUCTURAL). Gate P-29c (k in DESI range) does not fire. Gate G-29e (k outside observable range) FIRES.

### The Unit Chain Is Correct

The formula k_today = H(t_BCS) * T_CMB / T_BCS was traced step by step:

| Quantity | Value | Source | Check |
|:---------|:------|:-------|:------|
| H(t_BCS) | 1.411e+14 GeV = 2.14e+38 /s | s29b ODE | H ~ M_KK^2/M_Pl (Friedmann). Correct. |
| T_BCS | 8.18e+15 GeV | T_RH ~ M_KK from s29b | Standard reheat. Correct. |
| T_CMB | 2.35e-13 GeV | 2.725 K | Measured. Correct. |
| T_CMB/T_BCS | 2.87e-29 | Ratio | 29 orders of redshift from GUT to today. |
| k [h/Mpc] | 9.39e+23 | k_phys * Mpc / (h * c) | Verified. |

Physical meaning: the comoving Hubble horizon at the BCS transition corresponds to a physical length of ~5 cm today. DESI observes at scales of 10-100 Mpc ~ 3e23--3e24 m. The ratio is 10^{24-25}.

### The Scaling Law

k ~ H * T_CMB / T_BCS ~ (M_KK^2/M_Pl) * T_CMB / M_KK ~ M_KK * T_CMB / M_Pl

This is linear in M_KK. To reach k ~ 0.1 h/Mpc requires M_KK ~ 0.1 * M_Pl / T_CMB ~ 10^{-7} GeV ~ 0.1 eV. A sub-eV KK scale means a macroscopic (~1 mm) internal space -- physically absurd for compactified SU(3).

### Framework Impact: The Scale Bridge Problem

The 24-order gap is not a failure of this particular framework. It is an inherent limitation of ALL Kaluza-Klein compactifications at M_KK >> eV. Any GUT-scale transition imprints at microscopic comoving distances because the Hubble horizon at GUT energies is microscopically small. This is the scale bridge problem: without an inflationary epoch to stretch microscopic fluctuations to cosmological scales (and the modulus rolls through in a fraction of an e-fold, so there is no such epoch), there is no direct large-scale structure signature.

This structural result permanently closes one class of observational predictions (direct LSS/CMB imprints from the transition) while clarifying where the framework's testable content actually lives:

**What is closed**:
- Direct k_transition in any galaxy survey (DESI, Euclid, SDSS)
- GW peak frequency in any detector band (LISA, LIGO, ET, PTA)
- Any cosmological-scale spatial signature of the BCS transition itself

**What remains open**:
- **Frozen-state observables**: g_1/g_2 = e^{-2*tau_frozen} is a zero-parameter gauge coupling prediction. At tau_frozen ~ 0.35-0.50, this gives g_1/g_2 = 0.37-0.50 (mild tension with the SM GUT value ~ 0.55-0.60, potentially constraining tau_frozen).
- **Proton lifetime**: tau_p ~ M_KK^4/m_p^5. For M_KK = 10^16, tau_p ~ 10^36 yr. Hyper-K accessible.
- **Mass ratio phi_paasch**: m_{(3,0)}/m_{(0,0)} at tau_frozen. Zero-parameter prediction.
- **Cosmological constant**: L-8 sector cancellation across 3-sector F_BCS sum. Representation-theoretic.
- **N_eff contribution**: KK tower as dark radiation after reheating.

The framework is not prediction-free. The predictions are indirect -- encoded in the frozen BCS ground state rather than in transition-epoch dynamics. This is analogous to the Hawking radiation problem: the theory is calculationally correct (k = 9.4e23 h/Mpc follows from verified dimensional analysis), but the signal is structurally inaccessible. The physics is real; the observation channel is closed.

---

## IV. 29c-3: CDL Inapplicable

**Script**: `tier0-computation/s29c_cdl_bounce.py`

### Why CDL Does Not Apply

The Coleman-De Luccia bounce describes quantum tunneling from a false vacuum through a potential barrier to a true vacuum. This requires: (1) a local minimum where the field sits, (2) a barrier where V_eff > V_false, (3) a lower-energy minimum on the other side.

The phonon-exflation potential V_eff(tau) = S_spectral(tau) + F_BCS(tau) has none of these. Using the heat kernel spectral action at Lambda=1, V_eff ranges from S(0) = 14,999 to S(0.5) = 10,237 -- a 32% monotonic decrease. The spectral action slope ranges from -2287 (tau=0) to -14941 (tau=0.5) per unit tau. The BCS condensation energy F_BCS ranges from -13 to -19. The ratio is 500:1. V_eff is monotonically decreasing at all tau.

On this potential, the O(4) numerical bounce gives B = 1.47e+11 and thin-wall gives B = 75,705. Both are astronomically large because there is no tunneling path -- the formalism is trying to compute a bounce on a barrierless potential and returning nonsense. CDL is INAPPLICABLE, not merely failing -- the formalism's premises are not met.

Note: the correct spectral action for V_normal is the heat kernel at Lambda=1, which matches the F_normal used in 29b (mismatch = 1.8e-12). The sharp cutoff at Lambda=10 is saturated (all 11,424 eigenvalues fall below it at every tau, returning a constant 155,984) and must not be used for V_eff comparisons.

### The CDL Question Is Moot

The physically relevant CDL question would be: can the modulus tunnel OUT of the BCS condensate toward decompactification? But since V_eff is monotone -- no potential well, no barrier -- there is nothing to tunnel out of. The trapping is by first-order latent heat (L-9), not by a potential barrier. CDL adds nothing to this system.

**Verdict**: DIAGNOSTIC (CDL inapplicable). Gate G-29d MOOT (premise invalidated).

### Trapping Is Classical and Marginal

L-9 classical first-order trapping is the sole stability mechanism:

| E_mult | KE at tau_cross | Latent heat L | KE/L | Trapped? |
|:-------|:----------------|:--------------|:-----|:---------|
| 1.5 | 3.16 | 5.63 | 0.56 | YES |
| 2.0 | 12.01 | 5.63 | 2.13 | NO (overshoots) |
| 5.0 | 65.11 | 5.63 | 11.6 | NO (overshoots) |

Only E_mult <= ~1.5 trajectories are trapped. Whether the DNP instability (SP-5) launches the modulus at E_mult <= 1.5 or higher is not determined by Session 29A computations. An overshooting modulus rolls to infinity (decompactification) because V_eff has no turning point. The correct physical computation for trapping is the dissipative modulus trajectory: integrate the equation of motion with Parker back-reaction friction and BCS latent heat extraction, determining the basin of attraction for a range of initial kinetic energies.

---

## V. 29c-4: Gravitational Waves at Ultra-High Frequency

**Script**: `tier0-computation/s29c_gw_spectrum.py`

### The Computation

GW parameters from the L-9 first-order BCS transition, using standard Hindmarsh et al. (2015, 2017) formulas:

| Parameter | Value | Notes |
|:----------|:------|:------|
| alpha (latent heat / rho_rad) | 0.0091 | M_KK-independent (both scale as M_KK^4) |
| beta/H | 7.8 (M_KK=1e18) to 7.8e4 (M_KK=1e14) | Fast nucleation |
| f_peak (sound waves) | 1.3e+12 Hz | M_KK-independent |
| h^2 Omega_peak (SW) | 6.4e-16 to 6.4e-12 | Below all detectors |

The formulas are correctly implemented. The M_KK-independence of f_peak is a structural result: in the GW frequency formula, the product (beta/H) * T_* is M_KK-independent because beta ~ 11 * M_KK and T_* ~ M_KK, so beta * T_* ~ 11 * M_KK^2, while H ~ M_KK^2/M_Pl, giving (beta/H) * T_* = 11 * M_Pl ~ const. The GW frequency is set by the Planck scale, not the KK scale.

**Verdict**: DIAGNOSTIC (STRUCTURAL). Gate G-29f (f_peak outside LISA/LIGO range) FIRES. f_peak = 1.3e12 Hz is 17 orders above LISA, 9 orders above LIGO. The 17-order gap inherits from the same dimensional analysis as 29c-2.

### The Multi-Peak Structure That Was Not Computed

The GW computation treats the BCS transition as a single event with a single alpha and beta/H. But L-9 established that the transition has **5 cusps** in d^3F/dtau^3 at sector boundaries, corresponding to 5 different irreducible representations entering or leaving the supercritical regime at different tau values.

Each cusp is a separate sub-transition with its own alpha and beta/H. The resulting GW spectrum would be a superposition of 5 peaked spectra, not a single peak. The relative amplitudes and frequencies of the 5 peaks are determined by the sector-specific latent heats and transition widths. This multi-peaked structure is a distinctive prediction that generic first-order transitions do not produce -- although the entire spectrum sits at f ~ 10^{12} Hz, the RELATIVE spacing between peaks is a parameter-free structural fingerprint.

Alpha = 0.0091 is a weak transition. The standard GW formulas assume thermal bubble nucleation in a radiation-dominated plasma, but the BCS transition is driven by modulus rolling -- "beta/H" here measures the modulus crossing rate, not the nucleation rate. O(1) corrections are possible, but the 17-order gap to any detector is robust against such corrections.

---

## VI. The Resonance Structure

### Parametric Resonance on Jensen-Deformed SU(3)

The Bogoliubov particle creation in KC-1 is parametric amplification of the Dirac field by the time-varying Jensen metric. The Jensen deformation is a driven oscillator, and the Dirac modes are the cavity. The parametric resonance condition:

    d(lambda_n)/d(tau) * (d(tau)/dt) ~ lambda_n

or equivalently: eta = lambda / |d(lambda)/d(tau)| ~ 1 / (d(tau)/dt). The modes most strongly amplified are those at the gap edge, where lambda is smallest and |d(lambda)/d(tau)| is largest. This is why B_k is largest at the gap edge -- parametric resonance in the literal sense.

The connection to phononic crystals: the Jensen-deformed SU(3) is a phononic crystal with a time-dependent bandgap. When the bandgap closes (small lambda_min), modes pile up at the gap edge (van Hove singularity, KC-5) and parametric amplification is maximized. The BCS condensation is the acoustic analog of band inversion in a topological phononic crystal -- the gap closes, the modes mix, and a new ground state forms.

This is not metaphor. The mathematics is identical. The Bogoliubov transformation in KC-1 is the same as the scattering matrix of a phononic crystal with time-varying periodicity. The BCS gap equation in KC-5 is the same as the condition for band inversion in a phononic crystal driven through a topological phase transition.

### The Chladni Pattern of the Internal Space

Every vibrating structure has characteristic patterns at its resonant frequencies. On Jensen-deformed SU(3), the "Chladni pattern" is the spatial distribution of B_k across the internal manifold. No computation has yet mapped this real-space distribution -- which regions of SU(3) are most excited, whether particle creation is concentrated near the SU(2) subgroup (which shrinks under Jensen deformation) or spread over the full SU(3), and whether there are "quiet" nodal regions where production is suppressed.

### The Volovik Connection

In superfluid vacuum models (Volovik), the modulus velocity d(tau)/dt plays the role of the superfluid velocity. The Landau critical velocity is set by the spectral gap: v_Landau = min(lambda_n(tau) / |k_n|). When the modulus velocity exceeds this critical velocity, the vacuum becomes unstable and excitations are produced -- exactly the adiabaticity condition eta < 1 from KC-1.

The L-9 first-order transition is the analog of the lambda-transition in helium: a discontinuous change in the ground state that releases latent heat and traps the system in a new phase. The BCS condensate is the superfluid phase. The modulus rolling is the normal fluid flow. Both systems are described by the same Bogoliubov-de Gennes formalism, both have a gap equation, both have a first-order transition with latent heat, both have a critical velocity above which the condensate is destroyed.

---

## VII. Provocation Assessment

The 29Ac prompt defined three structural isomorphisms (Claims A, B, C) to test against computation.

### Claim A: CMB = Internal Gibbons-Hawking Radiation

**Strong form**: NOT SUPPORTED. T_eff/T_GH = 3.33. R^2 = -0.69. No horizon on SU(3).

**Weak form**: VIABLE BUT UNTESTED. Parker particle creation (KC-1) produces the initial particle content. Post-transition thermalization via latent heat release (L-9) + KC-2/KC-3 scattering could produce a standard thermal bath at T_RH ~ M_KK. The physical CMB temperature would follow from T_CMB = T_RH * (a_BCS/a_0) by standard entropy conservation. This is the correct version of Claim A -- it requires reheating from the first-order transition, not T_GH.

Non-thermality does NOT invalidate the mechanism: the BCS latent heat (Q ~ 5.63 * M_KK^4) dwarfs the Parker particle energy (B_k^max ~ 0.22). The universe thermalizes after the first-order transition regardless of the pre-transition spectrum.

### Claim B: BCS Transition Defines the Observable Horizon Scale

**NOT SUPPORTED.** k_transition = 9.4e+23 h/Mpc. f_peak = 1.3e+12 Hz. Both 12-24 orders beyond any instrument. This is the Hawking radiation from stellar black holes problem: the theory may be correct but the signal is unmeasurably small.

### Claim C: Black Hole Interior = Time-Reverse of Our Universe

**PARTIALLY SUPPORTED.** I_E(tau) is monotonically decreasing (Z = exp(-I_E) increases -- negative specific heat analog, exact to 1e-39). BCS first-order parallels Hawking-Page. DNP instability at tau=0 parallels the initial singularity replaced by regular geometry.

**Where the isomorphism breaks**: No causal horizon on SU(3). The CMB surface is a phase boundary, not a causal boundary. The correct term is "modulus mini-superspace diagram" (hawking), not "Penrose diagram" -- no causal structure is modified.

| Claim | Strong Form | Weak Form | Key Evidence |
|:------|:-----------|:----------|:-------------|
| A (CMB = T_GH radiation) | NOT SUPPORTED | VIABLE, UNTESTED | T_eff/T_GH=3.33, R^2=-0.69. Reheating from L-9 is the correct mechanism. |
| B (BCS defines horizon scale) | NOT SUPPORTED | NOT SUPPORTED | k=9.4e23, f=1.3e12 Hz. Structurally inaccessible. |
| C (BH interior = time-reverse) | PARTIALLY SUPPORTED | PARTIALLY SUPPORTED | I_E monotone, no horizon on SU(3). |

---

## VIII. Gate Verdicts and Constraint Map

### Soft Gates

| ID | Condition | Verdict | Decisive Number |
|:---|:----------|:--------|:----------------|
| G-29d | B < 400 (CDL bounce) | **MOOT** (premise invalidated) | CDL inapplicable. V_eff monotone. |
| G-29e | k_transition outside DESI/Euclid | **FIRES** | k = 9.4e+23 h/Mpc |
| G-29f | f_peak outside LISA/LIGO | **FIRES** | f_peak = 1.3e+12 Hz |

### Positive Signals

| ID | Condition | Verdict | Decisive Number |
|:---|:----------|:--------|:----------------|
| P-29c | k in DESI range | Does not fire | k = 9.4e+23, structurally inaccessible |
| P-29d | T_eff/T_GH in [0.5, 2.0] | Does not fire | Ratio = 3.33. No horizon on SU(3); gate premise invalid. |
| P-29e | B > 400 (stable) | Does not fire | CDL inapplicable (V_eff monotone). L-9 marginal (E_mult <= 1.5). |
| P-29f | f_peak in LISA range | Does not fire | f_peak = 1.3e+12 Hz |
| P-29g | T_GH redshifted = 2.725 K | Cannot be evaluated | Non-thermal spectrum invalidates premise. |

### Gate Summary

- Hard closes: 0
- Soft gates fired: 2/3 (G-29e, G-29f). 1 moot (G-29d).
- Positive signals: 0/3 valid (P-29c, P-29e, P-29f). 2 moot (P-29d, P-29g: no horizon on SU(3)).
- New constraints: 4 (GH-1, KT-1, CDL-1, GW-1)

### Constraint Map (29Ac)

| ID | What is proven | Source | Surviving solution space |
|:---|:---------------|:-------|:------------------------|
| 29Ac-GH1 | Bogoliubov spectrum non-thermal at all tau. B_k positively correlated with omega (r=+0.74). Sector-dependent: (3,0)/(0,3) have least negative R^2. | 29c-1 | Parker mechanism confirmed. Sector-resolved resonance structure unresolved at current grid. Thermalization via KC-2/KC-3 + L-9 latent heat required for CMB connection. |
| 29Ac-KT1 | k_transition = 9.4e+23 h/Mpc (M_KK=1e16). k ~ M_KK^1.0 (exact). 24 orders above DESI. Inherent to any KK compactification at M_KK > TeV. | 29c-2 | Direct LSS/CMB imprint permanently closed. Framework predictions redirect to frozen-state observables: g1/g2, proton lifetime, phi_paasch, L-8 CC cancellation. |
| 29Ac-CDL1 | V_eff monotonically decreasing. No CDL barrier. CDL formalism inapplicable (no false vacuum on this potential). | 29c-3 | L-9 classical trapping only, marginal (E_mult <= ~1.5). DNP launch energy is critical unknown. Dissipative trajectory needed to determine trapping basin. |
| 29Ac-GW1 | f_peak = 1.3e+12 Hz (M_KK-independent). alpha = 0.0091 (weak). 17 orders above LISA. Multi-peaked sector cascade structure exists but at ultra-high frequency. | 29c-4 | GW signal unobservable. Multi-peak spacing is a parameter-free structural fingerprint but observationally moot at GUT scale. |

---

## IX. Probability

**Pre-registered range**: 15-22% panel (for "Full PASS, no observables" scenario from 29Ac prompt).

**Upward**:
- Five indirect observational channels identified (gauge coupling, proton lifetime, phi_paasch, CC cancellation, N_eff). The framework is not prediction-free.
- Parametric resonance structure is real physics -- anti-thermal B_k and sector dependence confirm Parker mechanism.

**Downward**:
- Trapping is marginal (L-9 only, E_mult <= ~1.5). Whether DNP launches within this window is undetermined.
- The frozen-tau gauge coupling g1/g2 = 0.37-0.50 shows mild tension with SM GUT value ~0.55-0.60.
- 0/5 positive signals. All direct transition-epoch signatures structurally inaccessible.

**Estimate**: 15-18% panel (lower half of pre-registered range). Marginal trapping is the primary downward driver. Indirect prediction channels prevent further drift. Sagan checkpoint required for formal assessment.

---

## X. Output Files

| File | Content | Status |
|:-----|:--------|:-------|
| `tier0-computation/s29c_gibbons_hawking_temperature.{py,npz,png}` | 29c-1 (Bogoliubov spectrum) | |
| `tier0-computation/s29c_k_transition.{py,npz,png}` | 29c-2 (k_transition) | |
| `tier0-computation/s29c_cdl_bounce.{py,npz,png}` | 29c-3 (CDL bounce) | |
| `tier0-computation/s29c_gw_spectrum.{py,npz,png}` | 29c-4 (GW spectrum) | |
| `tier0-computation/s29c_gate_verdicts.txt` | Gate verdicts | |
| `sessions/session-29/session-29Ac-synthesis.md` | This file | |
| `sessions/session-29/session-29Ac-workshop.md` | Workshop notes | |

---

*Session 29Ac: four computations. The universe does not produce thermal spectra from parametric amplification on a compact manifold with discrete eigenvalues. It produces resonance patterns. Each sector of SU(3) rings at its own frequencies. The Jensen deformation sweeps those frequencies in time. Where the sweep rate matches a mode spacing, there is amplification. Where it does not, there is silence. The particles we observe are the sand grains that collected at the antinodes. The BCS condensation is the moment when the vibrating plate cracks -- a first-order structural failure that freezes the pattern in place. The right computation is not "fit a thermal distribution." The right computation is "map the resonance."*
