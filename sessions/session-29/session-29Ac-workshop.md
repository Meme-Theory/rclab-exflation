# Session 29Ac Synthesis: Observational Predictions and Scrutiny

**Date**: 2026-02-28
**Sub-session**: 29Ac (observational predictions + provocation assessment + deep scrutiny)
**Team**: phonon-sim (phonon-exflation-sim), hawking (hawking-theorist), coordinator, baptista (baptista-spacetime-analyst), hawking-2 (hawking-theorist)
**Computations**: 29c-1 (GH temperature), 29c-2 (k_transition), 29c-3 (CDL bounce), 29c-4 (GW spectrum)
**Gate verdicts file**: `tier0-computation/s29c_gate_verdicts.txt` (v2, revised after scrutiny)
**Inputs from 29Aa/29Ab**: KC-1 through KC-5 ALL PASS. tau_cross = 0.50. t_BCS = 1.3e-41 s at M_KK = 1e16. Gi = 0.36. V_eff monotonically decreasing. L-9 first-order is the sole trapping mechanism.

---

## I. Session 29Ac Question

Sessions 29Aa and 29Ab established that the BCS mechanism is internally complete: the Constraint Chain passes, the backreaction is solved, the mean-field is reliable, and the first-order transition traps the modulus. Session 29Ac asks the next question: **does the mechanism predict anything observable?**

Four direct cosmological signatures were tested:
1. Internal Gibbons-Hawking temperature vs Bogoliubov spectrum (Claim A)
2. Transition wavenumber k_transition vs DESI/Euclid range (Claim B)
3. CDL bounce action for vacuum stability
4. Gravitational wave spectrum from the first-order transition

---

## II. Computation Results

### 29c-1: Internal Gibbons-Hawking Temperature

**Script**: `tier0-computation/s29c_gibbons_hawking_temperature.py`
**Agent**: phonon-sim

The Bogoliubov spectrum |beta_k|^2 was fit to a Bose-Einstein distribution at each tau to extract T_eff, then compared to the internal GH temperature T_GH^{int}(tau) = e^{-2tau}/pi.

| tau | T_GH^int | T_eff (BE fit) | T_eff/T_GH | R^2 of fit |
|:----|:---------|:---------------|:-----------|:-----------|
| 0.00 | 0.318 | 0.469 | 1.47 | deeply negative |
| 0.35 | 0.175 | 0.582 | 3.33 | -0.69 |
| 0.50 | 0.120 | 0.756 | 6.30 | deeply negative |
| 2.00 | 0.006 | 3.29 | 569 | deeply negative |

- Mean R^2 across all tau: -72.3. The Bose-Einstein fit is worse than a constant at every tau.
- T_eff/T_GH diverges monotonically. No quasi-thermal regime exists.
- B_k is positively correlated with omega at tau=0.50 (Pearson r = +0.74): anti-thermal. Higher-energy modes have LARGER occupation numbers. This is the signature of gap-edge parametric amplification (Parker 1969), not equilibrium horizon radiation.

**T_GH formula correction** (phonon-sim self-correction, confirmed by hawking-2): The script used T_GH = e^{-2tau}/pi. The correct GH analog for an expanding internal space is T = H_internal/(2*pi) = (4/3)*dtau_dt/(2*pi), which depends on the modulus velocity. At dtau/dt = 2.19 (from 29b-2), T_GH ~ 0.465, close to T_eff ~ 0.469 at tau=0. However, the spectrum SHAPE is non-thermal (R^2 deeply negative), so the single-point match is not physically meaningful.

**Sector dependence** (baptista): Singlet sector shows quasi-thermal R^2 = 0.98 but higher representations give R^2 = 0.43-0.62. The non-thermality is sector-dependent, consistent with Parker production on a space with non-trivial representation structure: different sectors have different eigenfrequency profiles under the Jensen deformation, so there is no universal temperature.

**Conceptual note** (baptista): The Gibbons-Hawking effect requires a horizon. SU(3) is compact with no boundary, no trapped surface, no event horizon. The T_GH^{int} formula is a characteristic frequency scale, not a physical temperature. The FAIL verdict on 29c-1 is correct, but the question was mis-specified -- there was never a physical reason to expect a thermal Gibbons-Hawking spectrum on a horizonless manifold.

**Verdict**: FAIL. Non-thermal spectrum. Gates P-29d (ratio in [0.5, 2.0]) and P-29g (T_GH redshifted = 2.725 K) do not fire.

---

### 29c-2: Transition Wavenumber k_transition

**Script**: `tier0-computation/s29c_k_transition.py`
**Agent**: phonon-sim

The BCS transition time t_BCS from 29b-2 was converted to a comoving wavenumber k_transition = a(t_BCS) * H(t_BCS) for each M_KK.

| M_KK (GeV) | k_transition (h/Mpc) | Gap to DESI |
|:------------|:---------------------|:------------|
| 10^14 | 9.4e+21 | 22 orders |
| 10^16 | 9.4e+23 | 24 orders |
| 10^18 | 9.4e+25 | 26 orders |

- Scaling: k ~ M_KK^1.0 (exact linear, dimensional analysis).
- Observable range: DESI 0.02-0.3 h/Mpc, Euclid 0.001-0.5 h/Mpc.
- To reach k ~ 0.1 h/Mpc would require M_KK ~ 1 eV (sub-eV KK mass, physically absurd for compactification).

**Structural result** (phonon-sim, hawking-2): k_transition = H_BCS * T_CMB/T_BCS ~ M_KK * T_CMB / M_Pl in natural units. The inaccessibility is INHERENT to any KK compactification at M_KK >> keV. Not a model choice -- dimensional analysis.

**Verdict**: FAIL (STRUCTURAL). Gate P-29c (k in DESI range) does not fire. Gate G-29e (k outside observable range) FIRES.

---

### 29c-3: CDL Bounce Action -- REVISED (Bug Found, PASS RETRACTED)

**Script**: `tier0-computation/s29c_cdl_bounce.py` (REVISED v2)
**Agent**: phonon-sim (computation), scrutinized by hawking-2 and baptista

**Bug identified during scrutiny**: The original computation used `S_LC_total_sharp[Lambda=10]` for V_normal. This spectral action is CONSTANT at 155,984 across all tau (all 11,424 eigenvalues fall below Lambda=10 at every tau). This created an artificial barrier of ~12.6 spectral units on a flat background, producing B = 0.016 (meaningless).

**Corrected computation**: V_normal uses `S_LC_total_heat[Lambda=1]`, which ranges from 14,999 (tau=0) to 10,237 (tau=0.5). Verification: mismatch with 29b F_normal = 1.8e-12 (machine epsilon).

**Corrected results**:

| Method | B | Notes |
|:-------|:--|:------|
| O(4) numerical (corrected) | 1.47e+11 | No tunneling (V_eff monotone) |
| Thin-wall scenario 2 (corrected) | 75,705 | No tunneling |
| O(4) numerical (RETRACTED) | ~~0.016~~ | Bug: flat V_normal |
| Thin-wall (RETRACTED) | ~~39.3~~ | Bug: flat V_normal |

- V_eff = S_spectral + F_BCS is monotonically decreasing at all tau.
- There is NO local minimum, NO barrier, NO false vacuum, NO true vacuum in the CDL sense.
- The CDL bounce formalism DOES NOT APPLY.

**Bounce direction error** (baptista): The original bounce profile had tau(r=0) = 0.000, tau(r_max) = 0.119 -- tunneling OUT of the BCS well, not INTO it. The physical scenario (modulus rolling from tau=0 toward large tau) has the BCS onset as a target, not a starting point. The directional setup was inverted. Irrelevant to the corrected conclusion (CDL inapplicable regardless) but noted for completeness.

**Trapping reassessment** (from 29b-2, now the ONLY stability mechanism):

| E_mult | KE at tau_cross | Latent heat L | KE/L | Trapped? |
|:-------|:----------------|:--------------|:-----|:---------|
| 1.5 | 3.16 | 5.63 | 0.56 | YES |
| 2.0 | 12.01 | 5.63 | 2.13 | NO (overshoots) |
| 5.0 | 65.11 | 5.63 | 11.6 | NO (overshoots) |

Trapping is MARGINAL. Only E_mult <= ~1.5 trajectories are trapped by L-9. No CDL backup for overshooting trajectories. Whether the DNP instability (SP-5) launches the modulus at E_mult <= 1.5 or higher is not determined by Session 29A computations.

**Verdict**: DIAGNOSTIC (CDL inapplicable). Original PASS RETRACTED. Gate G-29d MOOT (premise invalidated). Gate P-29e does not fire.

---

### 29c-4: Gravitational Wave Spectrum

**Script**: `tier0-computation/s29c_gw_spectrum.py`
**Agent**: phonon-sim

GW parameters from the L-9 first-order BCS transition, using standard Hindmarsh et al. (2015, 2017) formulas.

| Parameter | Value | Notes |
|:----------|:------|:------|
| alpha (latent heat / rho_rad) | 0.0091 | M_KK-independent (both scale as M_KK^4) |
| beta/H | 7.8 (M_KK=1e18) to 7.8e4 (M_KK=1e14) | Fast nucleation |
| f_peak (sound waves) | 1.3e+12 Hz | M_KK-independent |
| h^2 Omega_peak (SW) | 6.4e-16 to 6.4e-12 | Below all detectors |

- f_peak is M_KK-independent: T_* and beta/H both scale linearly with M_KK, canceling in the frequency formula. f_peak ~ M_Pl because beta/H * T_* = const * M_Pl. This is a structural result, not model-specific.
- f_peak = 1.3e12 Hz is 17 orders above LISA (1e-4 to 1e-1 Hz) and 9 orders above LIGO (10 to 1e3 Hz).
- alpha = 0.0091: weak transition. The multi-sector cascade (5 cusps from L-9) would produce a distinctive multi-peaked spectrum, but the entire spectrum is at ultra-high frequency.

**Non-standard scenario note** (baptista): The standard GW formulas assume thermal bubble nucleation in a radiation-dominated plasma. The BCS transition is driven by modulus rolling, not thermal nucleation. "beta/H" here measures the modulus crossing time / Hubble time, not the nucleation rate / Hubble rate. O(1) corrections possible, but the 17-order gap is robust.

**Verdict**: DIAGNOSTIC (STRUCTURAL). Gate G-29f (f_peak outside LISA/LIGO range) FIRES. Gate P-29f (f_peak in LISA range) does not fire.

---

## III. CDL PASS Retraction: Technical Detail

This section documents the bug, correction, and impact for the record.

**Root cause**: The `s28a_spectral_action_comparison.npz` file contains multiple spectral action arrays at different Lambda cutoffs. The script selected `S_LC_total_sharp` at index [3] (Lambda=10). At this cutoff, all 11,424 Dirac eigenvalues on Jensen-deformed SU(3) fall below Lambda=10 at every tau in [0, 0.5]. The sharp-cutoff spectral action therefore returns the SAME value (155,984.0000) at all tau -- it is saturated. The V_BCS potential, computed as this constant plus F_BCS(tau), showed a shallow dip from the BCS condensation energy alone, creating an artificial "barrier" and "false vacuum."

**Correction**: Replaced with `S_LC_total_heat` at Lambda=1 (heat kernel regularization), which gives S(0) = 14,999, S(0.5) = 10,237 -- a 32% decrease. This matches the F_normal used in the 29b free energy comparison (mismatch = 1.8e-12). On this physical potential, V_eff is monotonically decreasing and there is no barrier.

**Impact on Session 29A narrative**:
- The "robust attractor" and "CDL recapture of overshooting trajectories" claims from the original synthesis are RETRACTED.
- Trapping is now understood to be L-9 classical first-order ONLY, with a narrow window (E_mult <= ~1.5).
- The DNP launch energy becomes a critical unknown: if SP-5 produces E_mult > 1.5, the modulus overshoots and decompactifies.
- This is a new structural vulnerability not present in the pre-scrutiny assessment.

---

## IV. Provocation Assessment

The 29Ac prompt (Section I) defined three structural isomorphisms (Claims A, B, C) to test against computation.

### Claim A: CMB = Internal Gibbons-Hawking Radiation

**Strong form**: NOT SUPPORTED. T_eff/T_GH = 3.33 at tau=0.35. R^2 = -0.69 (non-thermal). No horizon on SU(3), so the GH thermal spectrum is not expected (baptista).

**Weak form**: VIABLE BUT UNTESTED. Parker particle creation (KC-1) produces the initial particle content. Post-transition thermalization via latent heat release (L-9) + KC-2/KC-3 scattering could produce a standard thermal bath at T_RH ~ M_KK. The physical CMB temperature follows from T_CMB = T_RH * (a_BCS/a_0), a standard entropy-conservation calculation. This is the correct version of Claim A -- it does not require T_GH, only reheating from the first-order transition.

**Non-thermality does NOT invalidate the mechanism** (hawking-2, baptista): The BCS latent heat (Q = L * M_KK^4 ~ 5.63 * M_KK^4) dwarfs the Parker particle energy (B_k^max ~ 0.22). The universe thermalizes after the first-order transition regardless of the pre-transition spectrum.

### Claim B: BCS Transition Defines the Observable Horizon Scale

**NOT SUPPORTED.** k_transition = 9.4e+23 h/Mpc at M_KK = 10^16. f_peak(GW) = 1.3e+12 Hz. Both 12-24 orders of magnitude beyond any instrument. The BCS transition at GUT epoch imprints at microscopic comoving scales. This is the "Hawking radiation from stellar black holes" problem: the theory may be correct but the signal is unmeasurably small.

### Claim C: Black Hole Interior = Time-Reverse of Our Universe

**PARTIALLY SUPPORTED** (structural isomorphism holds; observational mapping breaks). I_E(tau) is monotonically decreasing (Z = exp(-I_E) increases -- negative specific heat analog, exact to 1e-39). BCS first-order transition parallels Hawking-Page. DNP instability at tau=0 parallels the initial singularity replaced by regular geometry.

**Where the isomorphism breaks**: No causal horizon on SU(3). The CMB surface is a phase boundary, not a causal boundary. The Penrose diagram metaphor is misleading (hawking: "modulus mini-superspace diagram" is the correct term, not "Penrose diagram" -- no causal structure is modified).

### Provocation Summary

| Claim | Strong Form | Weak Form | Key Evidence |
|:------|:-----------|:----------|:-------------|
| A (CMB = T_GH radiation) | NOT SUPPORTED | VIABLE, UNTESTED | T_eff/T_GH=3.33, R^2=-0.69. Reheating from L-9 latent heat is the correct mechanism. |
| B (BCS defines horizon scale) | NOT SUPPORTED | NOT SUPPORTED | k=9.4e23, f=1.3e12 Hz. Structurally inaccessible. |
| C (BH interior = time-reverse) | PARTIALLY SUPPORTED | PARTIALLY SUPPORTED | I_E monotone, no horizon on SU(3). |

---

## V. Scrutiny Convergences

Four independent scrutineers (phonon-sim, hawking, hawking-2, baptista) examined the computation scripts, .npz outputs, and physical reasoning. The convergent findings:

### 5.1 All Four Agree: Direct Observables Structurally Inaccessible

The inaccessibility of k_transition, f_peak, and T_GH is inherent to ANY Kaluza-Klein compactification at M_KK > TeV. This is dimensional analysis, not a model limitation. For k ~ 0.1 h/Mpc, one would need M_KK ~ 1 eV (absurd for compactification). For f_peak ~ mHz (LISA), one would need the transition at T ~ 100 GeV (electroweak scale, inconsistent with M_KK ~ 10^15-10^16).

### 5.2 All Four Agree: Indirect Predictions Are the Real Testable Content

The framework's observational predictions come from the frozen BCS state, not from the transition dynamics. Five indirect channels were independently identified:

| Prediction | Content | Identified By | Priority |
|:-----------|:--------|:-------------|:---------|
| Gauge coupling | g1/g2 = e^{-2*tau_frozen}. Zero-parameter. tau_frozen ~ 0.35-0.50 gives g1/g2 = 0.37-0.50. SM GUT value ~ 0.55-0.60 -> mild tension. | hawking-2, baptista, phonon-sim | HIGHEST |
| Proton lifetime | tau_p ~ M_KK^4/m_p^5. For M_KK = 10^16, tau_p ~ 10^36 yr. Hyper-K accessible. | baptista | HIGH |
| Thermalization T | Post-BCS equilibrium T from L-9 latent heat + KC-3 scattering. Correct version of Claim A. | hawking-2, baptista | HIGH |
| phi_paasch at tau_BCS | m_{(3,0)}/m_{(0,0)} at tau_frozen. Zero-parameter mass ratio prediction. | baptista | MEDIUM |
| CC cancellation (L-8) | 3-sector F_BCS sum. If representation-theoretic cancellation is exact, CC is predicted. | baptista, hawking-2 | MEDIUM |
| Superheavy DM | J-odd quasiparticles from Parker production. Mass ~ lambda_min * M_KK. | baptista | LOW |
| Parker friction | Particle creation back-reaction on modulus velocity. Could shift t_BCS and E_mult. | hawking-2 | MEDIUM |

### 5.3 CDL Bug: Universal Agreement on Retraction

All four scrutineers identified the flat V_normal (Lambda=10 saturation) as the bug. phonon-sim fixed and reran the script. hawking-2 independently verified the constant 155,984 value. baptista additionally noted the inverted bounce direction. The PASS retraction is unanimous.

### 5.4 Marginal Trapping Is a New Structural Vulnerability

Pre-scrutiny: trapping was presented as robust (CDL backup + L-9 + Arrhenius).
Post-scrutiny: trapping is L-9 only, effective for E_mult <= ~1.5. The DNP launch energy (from SP-5 instability) is the critical unknown. If E_mult > 1.5, the modulus overshoots and is NOT recaptured. This narrows the viable parameter space and should be a priority for Session 29B.

### 5.5 Gate Mis-specification

baptista: P-29d and P-29g were conditioned on the Gibbons-Hawking temperature, which requires a horizon. SU(3) has no horizon. These gates tested a quantity with no physical basis on this geometry. The FAIL verdict is correct but the question was wrong. Future gates should be framed around reheating temperature (from L-9 latent heat), not GH temperature.

---

## VI. Gate Verdicts (29Ac Only)

### Soft Gates

| ID | Condition | Verdict | Decisive Number |
|:---|:----------|:--------|:----------------|
| G-29d | B < 400 (CDL bounce) | **MOOT** (premise invalidated) | CDL inapplicable. V_eff monotone, no barrier. |
| G-29e | k_transition outside DESI/Euclid | **FIRES** | k = 9.4e+23 h/Mpc, 24 orders above DESI |
| G-29f | f_peak outside LISA/LIGO | **FIRES** | f_peak = 1.3e+12 Hz, 17 orders above LISA |

### Positive Signals

| ID | Condition | Verdict | Decisive Number |
|:---|:----------|:--------|:----------------|
| P-29c | k in DESI range | Does not fire | k = 9.4e+23, structurally inaccessible |
| P-29d | T_eff/T_GH in [0.5, 2.0] | Does not fire | Ratio = 3.33. Gate mis-specified (no horizon). |
| P-29e | B > 400 (stable) | Does not fire | CDL inapplicable. L-9 marginal (E_mult <= 1.5). |
| P-29f | f_peak in LISA range | Does not fire | f_peak = 1.3e+12 Hz |
| P-29g | T_GH redshifted = 2.725 K | Cannot be evaluated | Non-thermal spectrum invalidates premise. |

### Summary

- Hard closes: 0
- Soft gates fired: 2/3 (G-29e, G-29f). 1 moot (G-29d).
- Positive signals: 0/5
- New constraints: 4 (GH-1, KT-1, CDL-1, GW-1)

---

## VII. Constraint Map (29Ac)

| ID | What is proven | Source | Surviving solution space |
|:---|:---------------|:-------|:------------------------|
| 29Ac-GH1 | Bogoliubov spectrum non-thermal at all tau. B_k positively correlated with omega (anti-thermal, r=+0.74). R^2 = -72 mean. Sector-dependent: singlet quasi-thermal (R^2=0.98), higher sectors non-thermal (R^2=0.43-0.62). | 29c-1 | Parker mechanism confirmed. Thermalization via KC-2/KC-3 + L-9 latent heat required for CMB connection. |
| 29Ac-KT1 | k_transition = 9.4e+23 h/Mpc (M_KK=1e16). k ~ M_KK^1.0 (exact). 24 orders above DESI. Inherent to any KK compactification at M_KK > TeV. | 29c-2 | Direct LSS/CMB imprint inaccessible. Indirect effects (N_eff, baryogenesis, frozen-tau observables) open. |
| 29Ac-CDL1 | V_eff monotonically decreasing. No CDL barrier. B_corrected = 1.47e+11. Original B=0.016 RETRACTED (flat V_normal from Lambda=10 saturation). | 29c-3 (v2) | CDL tunneling ruled out as trapping or escape mechanism. L-9 classical trapping only, marginal (E_mult <= ~1.5). DNP launch energy is critical unknown. |
| 29Ac-GW1 | f_peak = 1.3e+12 Hz (M_KK-independent). alpha = 0.0091 (weak). h^2*Omega = 6.4e-16 to 6.4e-12. 17 orders above LISA. | 29c-4 | GW signal unobservable. Multi-peaked spectrum from L-9 cascade exists but at ultra-high frequency. |

---

## VIII. Probability Note

**Pre-29Ac**: 15-22% panel (pre-registered for "Full PASS, no observables" scenario, from 29Ac prompt Section IX).

**29Ac result**: Full PASS confirmed (from 29Aa + 29Ab). 0/5 positive signals in 29Ac. 4 new constraints. CDL PASS retracted, revealing marginal trapping (E_mult <= 1.5 only).

**Adjustments within the 15-22% range**:

Upward:
- Five indirect observational channels identified. The framework is not prediction-free -- predictions exist but were not tested in this sub-session.

Downward:
- CDL retraction reveals marginal trapping. Whether DNP launches at E_mult <= 1.5 is unknown.
- The frozen-tau gauge coupling g1/g2 = 0.37-0.50 shows mild tension with the SM GUT value ~0.55-0.60 (requires tau_frozen ~ 0.29 vs dynamics predicting tau ~ 0.35-0.50).
- 0/5 positive signals. All direct signatures structurally inaccessible.

**Coordinator structural estimate**: 15-18% panel (lower half of pre-registered range). The CDL retraction and marginal trapping are unanticipated downward drivers. The identification of indirect prediction channels prevents further downward drift. Sagan checkpoint required for formal assessment.

---

## IX. Session 29B Priorities (from 29Ac)

New priorities identified during 29Ac scrutiny, in addition to those already queued from Session 28 fusion:

| Priority | Content | Source | Urgency |
|:---------|:--------|:-------|:--------|
| Frozen-tau gauge coupling | g1/g2 = e^{-2*tau_frozen} vs SM RG prediction at M_GUT | hawking-2, baptista, phonon-sim | HIGHEST |
| DNP launch energy | What E_mult does the TT instability (SP-5) produce? Determines trapping viability. | CDL retraction consequence | HIGH |
| Parker friction | Particle creation back-reaction on modulus velocity. Could shift t_BCS and E_mult. | hawking-2 | HIGH |
| Thermalization temperature | Post-BCS equilibrium T from L-9 latent heat + KC-3 scattering. Correct Claim A. | hawking-2, baptista | HIGH |
| 3-sector CC cancellation (L-8) | Sum F_BCS across sectors with representation multiplicities. | baptista, hawking-2 | MEDIUM |

---

## X. Output Files

| File | Content | Status |
|:-----|:--------|:-------|
| `tier0-computation/s29c_gibbons_hawking_temperature.{py,npz,png}` | 29c-1 (GH temperature) | Original (correct) |
| `tier0-computation/s29c_k_transition.{py,npz,png}` | 29c-2 (k_transition) | Original (correct) |
| `tier0-computation/s29c_cdl_bounce.{py,npz,png}` | 29c-3 (CDL bounce) | REVISED v2 (bug fixed) |
| `tier0-computation/s29c_gw_spectrum.{py,npz,png}` | 29c-4 (GW spectrum) | Original (correct) |
| `tier0-computation/s29c_gate_verdicts.txt` | Gate verdicts | REVISED v2 |
| `sessions/session-29/session-29Ac-synthesis.md` | This file | |

---

*Session 29Ac synthesis by coordinator. Four computations, four scrutineers, one CDL retraction. Direct observational signatures structurally inaccessible at GUT scale. Indirect predictions (gauge coupling, proton lifetime, mass spectrum, CC cancellation) identified as the framework's actual testable content. Gate classification follows protocol: number first, classify second, interpret third.*
