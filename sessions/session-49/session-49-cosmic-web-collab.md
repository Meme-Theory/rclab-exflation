# Cosmic Web -- Collaborative Feedback on Session 49

**Author**: Cosmic Web Theorist
**Date**: 2026-03-17
**Re**: Session 49 Results -- 20 Computations, Leggett Dipolar, DESI Bayesian, alpha_s Crisis

---

## Section 1: Key Observations

Session 49 produced 20 gate verdicts (8 PASS, 7 INFO, 4 FAIL, 1 retraction). From the perspective of extragalactic observables -- power spectra, BAO, void statistics, bulk flows, DESI constraints -- four results reshape the framework's relationship to large-scale structure.

### 1.1 DESI Bayes Factor: B = 20.9 (1D) vs B = 0.073 (2D)

The framework now sits BETWEEN DESI DR2 and LCDM in w_0 space. The pre-registered prediction w_0 = -0.509 +/- 0.079 (band: [-0.430, -0.589]) is 2.47 sigma from DESI's w_0 = -0.752 +/- 0.058, while LCDM is 4.28 sigma. The 1D Bayes factor B = 20.9 says: in w_0 alone, the framework is 21 times more probable than LCDM given DESI DR2 data. This is the first time in 49 sessions that any extragalactic observable has favored the framework over the concordance model.

But the 2D verdict inverts: B_2D = 0.073 (framework 14 times disfavored). The reason is entirely w_a. DESI DR2 measures w_a = -0.73 +/- 0.28. The framework predicts w_a = -0.009 +/- 0.02 -- essentially zero, protected by GGE integrability (the 8 Richardson-Gaudin conserved quantities prevent time evolution of the equation of state). LCDM also predicts w_a = 0, but the w_0-w_a anti-correlation (rho = -0.75) in the DESI posterior places the LCDM point (-1, 0) closer to the degeneracy ridge than the framework point (-0.51, 0). The framework pays more for the w_a constraint than LCDM does.

The 1D/2D split is the sharpest diagnostic to emerge from this session. It isolates the exact dimension of parameter space where the framework and LCDM diverge: w_a. And it identifies w_a as the observable where DESI DR3 will be decisive.

### 1.2 alpha_s = n_s^2 - 1: Exact, Rigid, 6 sigma from Planck

ALPHA-S-BAYES-49 discovered an algebraic identity: in the O-Z framework (Ornstein-Zernike power spectrum on the fabric), the running of the spectral index is alpha_s = n_s^2 - 1, with ZERO dependence on J_ij, K_pivot, m*, or any coupling constant. Monte Carlo confirms: the sole source of uncertainty is the Planck measurement of n_s itself. At n_s = 0.9649 +/- 0.0042, this gives alpha_s = -0.069 +/- 0.008, a 6.0 sigma tension with Planck's alpha_s = 0.000 +/- 0.008.

From the large-scale structure perspective, this is a constraint on the primordial power spectrum shape. If alpha_s = -0.069, the power spectrum P(k) would be measurably steeper at small scales than LCDM with alpha_s = 0. Galaxy clustering at k > 0.1 h/Mpc would show a deficit relative to LCDM. The matter power spectrum amplitude sigma_8, which is already an integral over P(k), would shift by approximately delta(sigma_8)/sigma_8 ~ alpha_s * ln(k_max/k_pivot) ~ -0.069 * 3 ~ -0.21 -- a 21% suppression. This is observationally excluded: sigma_8 = 0.832 is measured to ~2% precision.

The alpha_s identity is a RIGID PREDICTION of the O-Z texture mechanism. It does not depend on fabric parameters. Either CMB-S4 measures alpha_s near -0.069 (framework confirmed at 8 sigma in that channel), or CMB-S4 measures alpha_s near 0 (framework's O-Z mechanism excluded at > 20 sigma). This is the cleanest pre-registered discriminant to emerge from the entire project, not just from Session 49.

### 1.3 Fabric NPAIR Conditional PASS: CC Crossing at tau* = 0.417

FABRIC-NPAIR-49 demonstrates that the 32-cell Josephson junction array achieves ec_fabric = 1.586, exceeding the CC crossing threshold ec_min = 1.264. The cosmological constant changes sign at tau* = 0.417 -- the first constructive computation showing that a CC crossing EXISTS within the framework, even if conditional on J_pair > 0.096 M_KK.

The LSS relevance: if the CC crosses zero, the framework produces a positive cosmological constant at tau > tau*. This is the Tier 3 channel (CC -> H(z) -> DESI) that has been the sole connection between my domain and the framework since Session 29. The conditional PASS means this channel is now structurally viable, not just hoped-for.

The J_pair uncertainty is the critical vulnerability. At 50% J_pair (conservative), ec_conservative = 1.15 < ec_min = 1.26 and the crossing FAILS. The recommended J-PAIR-CALIBRATE-50 computation is the decisive follow-up.

### 1.4 The Framework Sits in No-Man's-Land

The joint picture from W1-E and W1-O places the framework in a peculiar position: its w_0 prediction is 21 times better than LCDM against DESI, but its w_a = 0 is indistinguishable from LCDM and equally at odds with DESI's w_a signal. The framework is BETWEEN DESI and LCDM in w_0, and it is AT LCDM in w_a. It has moved off the cosmological constant, but not far enough to match the full DESI posterior.

The S42 result was w_0 = -1 + O(10^{-29}). Session 49's multi-temperature Friedmann correction (MULTI-T-FRIEDMANN-49) shifts this to w_0 = -0.43 (Zubarev GGE). This is not a cosmological constant anymore. The GGE quasiparticle relic provides genuine pressure (P/E = 0.75 in the multi-temperature formulation) that shifts w_0 away from -1. The S42 result is superseded: the effacement ratio of 10^{-6} applies to the BCS condensation energy contribution, but the GGE quasiparticle contribution is of order unity (alpha = 1.33).

This is a significant revision of the framework's observational posture. From S29 through S42, the framework was a pure Lambda-CDM theory with no deviation from w = -1. From S49 onward, it predicts w_0 in [-0.43, -0.59] -- a detectable departure from the cosmological constant, testable by DESI DR3.

---

## Section 2: Assessment

### 2.1 Is B = 20.9 Robust?

The 1D Bayes factor depends on three inputs: the DESI DR2 likelihood (w_0 = -0.752 +/- 0.058), the LCDM prediction (w_0 = -1, delta function), and the framework prediction (w_0 = -0.509 +/- 0.079).

**Strengths:**
- The framework prediction band is derived from first principles (Zubarev GGE vs Keldysh sigma methods applied to the post-transit quasiparticle state). No adjustable parameters.
- The LCDM baseline is at its strictest (delta function at w = -1).
- B = 20.9 exceeds the "substantial" Jeffreys threshold (B > 10) but falls short of "strong" (B > 100).

**Weaknesses:**
- The Z-K discrepancy (39.4%) that defines the framework band is structural: Zubarev and Keldysh formulations give different answers because the GGE violates the equilibrium assumptions underlying both. Neither is manifestly correct for a non-thermal integrable state. The band width is a measure of our ignorance about the correct statistical mechanics of the GGE, not a physical uncertainty.
- The 1D marginal ignores w_a entirely. Wang & Mota (Paper 37, WM37-E1/E2/E3) showed that DESI DR2's dynamical DE preference is partially driven by dataset tensions. If DR3 shifts w_0 toward -1, the Bayes factor collapses. The DR3 exclusion threshold (w_0 < -0.883 for B < 1/100) is comfortably far from DR2's center, making the framework robust against DR3 in 1D. But DR3 could also narrow the error bars while maintaining w_0 near -0.75, which would push B above 10^8 -- or shift toward -0.9, which would leave the framework uncomfortable but not excluded.
- LCDM is modeled as a delta function at w = -1. In practice, theoretical uncertainty in Lambda-CDM is zero (Lambda is a constant by construction), so this is fair. But some theorists might argue for a "Lambda + epsilon" prior that softens the comparison.

**My assessment:** B = 20.9 is a genuine, defensible signal of framework preference over LCDM in the w_0 dimension. It is NOT decisive. It is the kind of result that motivates continued testing, not the kind that settles the question. The 2D inversion (B = 0.073) demonstrates that the framework's advantage is fragile -- it depends entirely on which dimensions of parameter space are included.

### 2.2 w_a Tension: Framework vs Dynamical DE Models

The framework predicts w_a = -0.009 +/- 0.02. How does this compare to other models that also predict w_a ~ 0?

Every quintessence model with a slowly rolling scalar field predicts w_a in the range [-0.5, +0.5] depending on the potential shape and initial conditions. Thawing models generically have w_a < 0 (w becomes more negative with time), while freezing models have w_a > 0. The CPL parametrization w(a) = w_0 + w_a(1-a) is itself an approximation that can be misleading for models with phase transitions or rapid tracking.

The framework's w_a = 0 is more restrictive than any single-field quintessence model because it follows from an exact structural feature: the GGE quasiparticle state has time-independent occupation numbers (protected by Richardson-Gaudin integrability). The quasiparticles are confined to the SU(3) fiber (mass ~ M_KK) and cannot free-stream in 4D. There is no dynamical degree of freedom that evolves with redshift.

This means: if DESI DR3 confirms |w_a| > 0.3 at > 3 sigma with controlled systematics, ALL of the following are simultaneously under pressure: (a) LCDM (w_a = 0), (b) the framework (w_a = -0.009), (c) minimally coupled quintessence with flat potentials. The beneficiary would be coupled dark energy, k-essence, or modified gravity models that generate w_a through a distinct mechanism.

The DESI w_a signal remains uncertain. Lascu et al. (Paper 38) identified 0.03 mag photometric calibration bias in low-z SNe that, if corrected, reduces the dynamical DE preference substantially. Wang & Mota (Paper 37) showed that no single dataset exceeds 2 sigma for w != -1. The 3.1 sigma emerges only from the combination, which is sensitive to tensions between datasets.

### 2.3 The alpha_s Prediction and CMB-S4

alpha_s = n_s^2 - 1 = -0.069 at face value implies a strongly scale-dependent primordial spectrum. For large-scale structure, the consequences would be:

1. **Matter power spectrum shape**: P(k) ~ k^{n_s - 1 + (1/2) alpha_s ln(k/k_pivot)}. At k = 0.3 h/Mpc (the scale of BAO peak measurements), ln(k/k_pivot) ~ 1.8, giving an effective tilt shift of delta(n_eff) = alpha_s * 1.8 = -0.12. The effective spectral index would be n_eff ~ 0.84 instead of 0.96 -- a dramatic departure from observations. Galaxy surveys measure n_eff through the transfer function shape parameter Gamma = Omega_m * h * exp(-Omega_b(1 + sqrt(2h)/Omega_m)), which is well-constrained at n_eff = 0.96 +/- 0.02. alpha_s = -0.069 is excluded by existing P(k) shape measurements, not just by Planck CMB.

2. **CMB-S4 forecast**: If the framework is correct, CMB-S4 (sigma(alpha_s) ~ 0.003) would detect alpha_s = -0.069 at 8 sigma (W1-L). Conversely, if CMB-S4 measures alpha_s = 0.000 +/- 0.003, the O-Z texture mechanism is excluded at > 20 sigma. This is the highest-power pre-registered gate in the project's history. But I emphasize: the exclusion applies to the O-Z mechanism specifically, not to the entire framework. The framework could produce n_s through a mechanism other than O-Z (e.g., the Leggett mass route, or Bogoliubov coefficients from the transit).

3. **alpha_s and the Leggett mass**: The Leggett dipolar mechanism (W1-S) produces a mass omega_L1 = 0.070 M_KK, within 18% of the m_req = 0.059 M_KK needed for n_s = 0.965 in the O-Z propagator. But if the Leggett coupling modifies the functional form of the propagator (i.e., the power spectrum is not of the simple O-Z form P = T/(JK^2 + m^2)), then the alpha_s = n_s^2 - 1 identity may not hold. This is the crucial question for LEGGETT-NS-50: does the Leggett mechanism change the running, or only the mass?

### 2.4 The 32-Cell Tessellation and Void Statistics

Since Session 43, the 32-cell tessellation channel has been STRUCTURALLY CLOSED for volume-averaged statistics (KZ-CELL-43: inverted scaling, percolation of Voronoi boundaries). Session 49 does not reopen this. The fabric NPAIR computation (W1-B) uses the 32 cells as a Josephson junction array, not as a source of position-space structure in the galaxy distribution.

The void statistics question is: does the framework predict ANYTHING about void sizes, shapes, or correlations that differs from LCDM? The answer remains the same as Session 42: no. The framework's void prediction is identical to LCDM because:

- The primordial power spectrum shape is set by the O-Z propagator (or whatever mechanism generates n_s), which produces a nearly scale-invariant spectrum just like inflation.
- Void formation is governed by the same excursion set theory (Sheth-van de Weygaert 2004, D17-E1/E3/E4) in both models, because the growth factor D(a) is identical (w = -0.43 to -0.59 changes D(a) by less than 5% relative to w = -1).
- The persistent homology signature (beta_2 from Voronoi boundaries) was shown to be at 10^{-7} sigma in Session 43 (PERS-HOM-43). This is permanent.

The one conditional exception remains MVGAD-43 (massive void galaxy assembly delay): if the quasiparticle depletion channel is realized (dependent on the still-uncomputed Z(tau) partition function), galaxies with M* > 10^11 M_sun in voids could show 0.5-2 Gyr assembly delays relative to filament/cluster counterparts. This is testable with JWST + DESI spectroscopy. But Z(tau) remains uncomputed, so this is contingent.

### 2.5 Fabric CC Crossing at tau* = 0.417: Can It Be Tested?

The CC crossing at tau* = 0.417 occurs during the internal space transit (tau evolving from 0 through the fold at 0.19 to the post-transit freeze at ~0.22). The transit corresponds to a cosmological epoch at t ~ 10^{-41} s. No direct observation can probe this epoch.

However, the EXISTENCE of the crossing determines the present-day value of Lambda. If ec_fabric > ec_min (PASS), Lambda > 0 today. If ec_fabric < ec_min (FAIL, the conservative J_pair scenario), the CC may not cross zero, and the framework would predict Lambda <= 0, which is definitively excluded by all cosmological observations.

The test is therefore indirect: the CC crossing is a NECESSARY CONDITION for the framework to produce a positive cosmological constant. The J-PAIR-CALIBRATE-50 computation determines whether this condition is met. If J_pair < 0.096 M_KK, the framework fails to produce Lambda > 0 and is falsified on cosmological grounds regardless of any other consideration.

---

## Section 3: Collaborative Suggestions

### 3.1 Observational Tests (Prioritized)

**Priority 1: DESI DR3 w_0-w_a Joint Constraint (pre-registered)**

The framework's pre-registered predictions are:
- w_0 = -0.509 +/- 0.079
- w_a = -0.009 +/- 0.02

DR3 (expected sigma(w_0) ~ 0.035) will be decisive. Three outcomes:

| DR3 Result | Framework | LCDM | Action |
|:-----------|:----------|:-----|:-------|
| w_0 ~ -0.75, w_a ~ -0.5 | 2.8 sigma | > 7 sigma | Framework strongly preferred (1D) |
| w_0 ~ -0.60, w_a ~ 0 | 1.0 sigma | 11.4 sigma | Framework preferred, w_a rescued |
| w_0 ~ -1.0, w_a ~ 0 | 6.2 sigma | 0 sigma | Framework excluded |

The w_a dimension is the wedge. If DR3 confirms w_a ~ 0 while maintaining w_0 ~ -0.75, both LCDM and the framework face a "half-excluded" situation: LCDM wrong on w_0, framework wrong on w_0 (but less wrong). If DR3 confirms w_a < -0.3, both are equally under pressure.

**Priority 2: CMB-S4 alpha_s (pre-registered)**

alpha_s = -0.069 +/- 0.008 (framework) vs alpha_s = 0.000 +/- 0.008 (Planck). CMB-S4 at sigma ~ 0.003 resolves this at > 8 sigma if the framework is right, > 20 sigma exclusion if Planck is right. Target date: ~2030. This is the highest-power discriminant available.

However, I note that the LEGGETT-NS-50 computation could modify the alpha_s prediction if the Leggett mass changes the functional form. The pre-registered value should be updated post-S50 if the propagator changes.

**Priority 3: Bulk Flows (anomaly tracker)**

Bulk flows remain the strongest surviving LSS anomaly: V = 419 +/- 36 km/s at 200 h^{-1} Mpc (> 4 sigma, CosmicFlows-4). The framework has no mechanism to produce anomalous bulk flows because its dark matter is identical to CDM and its structure formation is identical to LCDM. The multi-temperature GGE with w_0 ~ -0.5 would slightly modify the growth rate f(z) = Omega_m(z)^gamma through the growth index gamma (gamma ~ 0.55 for LCDM, modified to gamma ~ 0.53 for w_0 ~ -0.5), but this is a 4% effect on f, insufficient to explain a 2-3 sigma excess in bulk flow amplitude.

If the bulk flow anomaly is confirmed at > 5 sigma by future surveys (e.g., DESI peculiar velocities), it becomes a challenge for LCDM, not specifically for the framework. The framework inherits the tension with no additional explanatory power.

**Priority 4: Void Profile Asymmetry (contingent)**

The void profile test from S42 addendum (void walls as domain boundaries) is structurally closed for volume-averaged statistics. However, the w_0 ~ -0.5 prediction (rather than w_0 = -1) modifies void dynamics slightly. In a w_0 = -0.5 universe, the void expansion rate is governed by the effective cosmological background with Omega_DE = Omega_Lambda * (-0.5/-1)^{3(1+w_0+w_a)} -- but since w_a ~ 0, this simplifies to a different Omega_Lambda amplitude. The void size function n(R) would shift by ~5-10% relative to LCDM. This is marginally detectable with DESI void catalogs (expected ~10,000 voids at z < 0.8 from the BGS sample), but the systematic uncertainty in void identification algorithms (VIDE vs ZOBOV vs watershed) is of the same order.

I do NOT recommend this as a priority test because the discriminating power is low (5-10% effect on a quantity with 10-20% systematic uncertainty).

### 3.2 DESI DR3 Preparation

The W1-O computation should be extended in two ways for DR3 readiness:

1. **Profile likelihood vs marginal likelihood**: The current B_2D uses the 2D Gaussian with anti-correlation rho = -0.75 from DESI DR2. DR3 will provide a more complex posterior shape (possibly non-Gaussian if the CPL parametrization breaks down). The framework's prediction point (-0.509, -0.009) should be evaluated against the full DR3 posterior, not a Gaussian approximation. This requires a numerical integral over the published DR3 chains, which the gen-physicist can implement using the MCP astro server's DESI access.

2. **Model comparison with quintessence priors**: The current comparison is framework vs LCDM (delta function). A more informative comparison adds quintessence as a third model with wide priors on (w_0, w_a). If quintessence is strongly preferred over both framework and LCDM, the question becomes whether the framework can accommodate evolving w -- which it cannot (w_a = 0 is structural). This tripartite comparison is the appropriate Bayesian framework for DR3.

### 3.3 The Most Discriminating LSS Observable

From my specialist domain, the most discriminating observable is NOT P(k), xi(r), void statistics, or sigma_8 (all of which are modified at the ~5% level by w_0 ~ -0.5 vs w_0 = -1, below current systematic floors for unique identification). The most discriminating observable is the **combined w_0-w_a constraint from BAO + CMB lensing + galaxy clustering**, because:

- The framework makes a POINT PREDICTION in this 2D space (not a band or a region).
- LCDM makes a different point prediction.
- The data already distinguishes them at B = 20.9 (1D) / B = 0.073 (2D).
- DR3 will shrink error bars by ~2x, making the comparison 4x more powerful.

The FIRST-SOUND-XI-44 prediction (xi(r) peak at 325 +/- 20 Mpc from Session 43) remains contingent on the BAO-as-second-sound interpretation (W4-5 from S43), which has not been revisited since. If this is still considered live, it would be the UNIQUE LSS prediction (no LCDM counterpart). But the contingency chain is long: BAO-as-second-sound -> first sound at 325 Mpc -> xi(r) peak with A ~ 0.010 and SNR 2-5. I do not have high confidence in this chain surviving, but it should be audited rather than forgotten.

### 3.4 The w_0 Revision and My Domain's Scope

Session 49 fundamentally changes the framework's observational profile in my domain. From S29 through S42, the framework was LCDM with derived parameters. My role was sentinel: any deviation from LCDM falsifies the framework. Post-S49, the framework predicts a specific, detectable, LCDM-inconsistent value of w_0. My sentinel role expands to include TESTING the w_0 prediction, not just guarding the w = -1 floor.

Specifically:
- The growth rate f*sigma_8(z) should be recomputed for w_0 = -0.509. The existing DESI DR1 tension (f*sigma_8 1-3 sigma below LCDM) might be REDUCED by the lower w_0 (less dark energy -> slower growth -> lower f*sigma_8). This is a potential post-diction that should be quantified.
- The BAO peak position r_s is UNAFFECTED (BCS transition at 10^{-41} s is irrelevant to recombination). But the angular diameter distance d_A(z) and Hubble parameter H(z) that convert r_s to observables ARE affected by w_0. The expected shift in the BAO peak position is delta(theta_BAO)/theta_BAO ~ (1-w_0)/3 * Omega_DE * delta_z ~ 0.02 at z = 0.5, which is 2% -- comparable to DESI statistical precision.
- The ISW effect changes sign for w_0 > -1/3, which is not the case here (w_0 ~ -0.5 still gives ISW with the same sign as LCDM). But the amplitude is modified by ~20%.

---

## Section 4: What Remains Unchanged in My Domain

### Volume-Averaged Statistics

P(k), xi(r), sigma_8, the void size function n(R), persistent homology (Betti numbers), Minkowski functionals, genus statistics -- all of these remain at ZERO discriminating power between the framework and LCDM-with-w_0=-0.5. The ~5% modifications from w_0 = -0.5 vs -1.0 are below the systematic uncertainty floors of these statistics as measured by current surveys.

### The Tessellation Channel

The 32-cell tessellation in position space remains STRUCTURALLY CLOSED (KZ-CELL-43). Session 49's use of 32 cells as a Josephson array is an internal-geometry computation, not a position-space prediction.

### Giant Structures and Bulk Flows

No framework mechanism exists for either the Giant Arc, the HCBGW, or the anomalous bulk flows. The framework inherits whatever LCDM tension exists with these observations. Session 49 did not change this.

### Void Physics as Discriminator

Van de Weygaert's geometric tools (DTFE, Spine, NEXUS+, persistent homology) remain the correct formalism for characterizing the cosmic web. But the framework predicts the SAME cosmic web as LCDM (with a 5% w_0 modification), so these tools cannot discriminate. The conditional tests (MVGAD-43, ALPHA-ENV-43) require the Z(tau) partition function, which remains uncomputed after 49 sessions. If Z(tau) is never computed, these tests are permanently inaccessible.

---

## Section 5: Closing Assessment

### What Narrowed the Constraint Surface

1. **w_0 prediction detachment from LCDM**: The multi-temperature GGE shifts w_0 from -1 to -0.43/-0.59. The framework is no longer invisible to DESI. This OPENS a direct observational channel that was previously closed by the effacement ratio.

2. **alpha_s = n_s^2 - 1 (exact identity)**: This is a rigid, zero-parameter prediction that is currently 6 sigma from data. It is the framework's most falsifiable prediction. It constrains the O-Z mechanism regardless of parameter choices.

3. **CC crossing conditional PASS**: The Josephson array with 32 cells achieves ec_fabric > ec_min. A positive cosmological constant is structurally possible within the framework. The J_pair calibration (J-PAIR-CALIBRATE-50) becomes the critical next gate.

4. **Leggett dipolar mass at 18% from n_s target**: First mechanism in 12+ routes to produce a Goldstone mass at the correct order of magnitude. If LEGGETT-NS-50 confirms n_s = 0.965, the framework's primordial spectrum emerges from an identifiable condensed-matter mechanism -- the analog of the dipolar interaction in He-3.

### What Remains Open

- **w_a = 0 vs DESI**: The deepest tension. GGE integrability structurally prevents w_a != 0. If DESI is right about w_a, the framework needs new physics beyond the integrable GGE.
- **alpha_s at 6 sigma**: Existential threat to O-Z mechanism. CMB-S4 will be definitive.
- **J_pair calibration**: The CC crossing is conditional. J-PAIR-CALIBRATE-50 is pass/fail for the framework's ability to produce Lambda > 0.
- **f*sigma_8(z) at w_0 = -0.5**: The growth rate tension may be ameliorated by the lower w_0. Quantification needed.
- **Z(tau) partition function**: 49 sessions, still uncomputed. Blocks the quasiparticle depletion channel, the void assembly delay test, and the alpha-environment correlation. At some point, this either gets computed or the contingent channels are declared permanently inaccessible.

### Recommended S50 Computations from My Domain

1. **F-SIGMA8-W05-50**: Recompute f*sigma_8(z) for w_0 = -0.509, compare to DESI DR1 data. Does the framework's w_0 REDUCE the growth rate tension? If so, this is a post-diction but a constructive one.

2. **BAO-SHIFT-W05-50**: Compute the shift in angular BAO peak position theta_BAO(z) for w_0 = -0.509 vs w_0 = -1. At what redshift is the shift maximally detectable by DESI?

3. **ALPHA-S-PK-50**: Translate alpha_s = -0.069 to the matter power spectrum P(k) shape and compare to SDSS/BOSS P(k) measurements. Is the framework's alpha_s already excluded by P(k) data, independent of CMB?

4. **LEGGETT-NS-50 ALPHA-S AUDIT**: After LEGGETT-NS-50 is computed, audit whether the Leggett mass changes the alpha_s identity. If it does, update the pre-registered prediction before DR3.

5. **W_A-SOURCE-50 SUPPORT**: From the cosmic web perspective, what would non-zero w_a look like in the void size function and BAO? Provide the observational templates for the w_a search.
